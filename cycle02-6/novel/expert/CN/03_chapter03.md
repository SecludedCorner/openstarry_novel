# 第三章：四维品质向量与观测器设计

---

## 3.1 设计规格到 SDK 维度的映射

Plan29 的 SDK 接口已定义了四维向量的字段名，但计算公式留空。Doc 43 设计规格与 SDK 实现之间的映射如下：

| Doc 43 设计规格 | SDK 字段名 | 语义 | 公式符号 |
|----------------|-----------|------|---------|
| Continuity（连续性） | `coherence` | 路由决策的逻辑一致性 | C |
| Granularity（精细度） | `efficiency` | 工具执行的资源利用效率 | E |
| Speed（速度） | `convergence` | 目标收敛性 | Conv |
| Equanimity（平衡性） | `stability` | 信心度的振荡稳定性 | S |

---

## 3.2 通用参数

| 符号 | 定义 | 预设值 | 来源 |
|------|------|--------|------|
| W | 滑动窗口大小 | 10 ticks | 设计选择：平衡灵敏度与稳定性 |
| W_warmup | 暖机期 | 5 ticks | 最小统计显著性 |
| Q_default | 暖机期复合分数 | 0.5 | 中性预设（不触发 L3 调整） |

暖机期规则：若 `tickCount < W_warmup`，所有维度回传 0.5，composite = 0.5。暖机期数据仍计入滑动窗口，但不对外发出品质报告。

---

## 3.3 coherence（C）：路由一致性

**语义**：衡量认知回路路由决策的一致程度。齿轮快速振荡（1->2->1->2）表示系统犹豫不决。

**公式**：

$$C = 1 - \frac{\text{gearSwitchCount}}{W - 1}$$

其中 `gearSwitchCount` = 窗口 W 内 gear 值变化的次数，`W-1` = 最坏情况（每 tick 都切换）。

**输入事件**：`gear:switch`（`payload.gear`）

**实现**：维护长度 W 的 circular buffer，记录最近 W 次 gear 值。每次新事件进入时，O(1) 更新——增加新的相邻差异计数，移除旧的。

**边界案例**：

| 情况 | 行为 | 理由 |
|------|------|------|
| 无 `gear:switch` 事件 | C = 1.0 | 无振荡 = 完美一致 |
| 窗口数据不足 W 笔 | 分母 = max(actualCount - 1, 1) | 避免除以零 |
| W = 1 | C = 1.0 | 单 tick 无法振荡 |

---

## 3.4 efficiency（E）：工具执行效率

**语义**：提案的工具调用中成功执行的比率。

**公式**：

$$E = \begin{cases} \frac{\text{successfulExec}}{\text{totalProposed}} & \text{if } \text{totalProposed} > 0 \\ 1.0 & \text{otherwise (纯对话回路)} \end{cases}$$

**输入事件**：

| 事件 | 用途 | 备注 |
|------|------|------|
| `action:proposed` | 分母 | 每次工具调用提案 |
| `tool:result` | 分子 | 成功执行 |
| `tool:error` | 隐含（Phase 2） | 不计入分子 |
| `tool:blocked` | 隐含（Phase 2） | 不计入分子 |

**设计选择**：纯对话回路（无工具调用）定义为 E = 1.0，不惩罚无工具场景。这是因为效率维度衡量的是「提出的行动是否成功」，没有提出行动不等于效率低。

---

## 3.5 convergence（Conv）：目标收敛性

**语义**：系统路由决策是否朝同一方向持续推进。连续选择同一齿轮越久，表示回路越收敛。

**公式**：

$$\text{Conv} = \frac{\text{longestConsistentStreak}}{W}$$

**Phase 2 替代方案（ATHENA 建议）**：指数移动平均（EMA）

$$\text{consistency}_t = \begin{cases} 1.0 & \text{if } \text{gear}_t = \text{gear}_{t-1} \\ 0.0 & \text{otherwise} \end{cases}$$

$$\text{EMA}_t = \alpha \cdot \text{consistency}_t + (1 - \alpha) \cdot \text{EMA}_{t-1}, \quad \alpha = \frac{2}{W + 1}$$

Phase 1 使用 streak 方法（简单、可解释）；Phase 2 有运行数据后再评估是否切换 EMA。

**输入事件**：`gear:switch`。注意 convergence 和 coherence 使用同一来源，但计算逻辑不同：coherence 测量切换频率，convergence 测量最长连续同向。

---

## 3.6 stability（S）：信心度稳定性

**语义**：arbiter 信心度的波动程度。基于方差的倒数映射。

**公式**：

$$S = 1 - \min\left(1, \frac{\sigma^2}{0.25}\right)$$

其中 $\sigma^2$ 为窗口 W 内 confidence 值的（母体）方差，0.25 为保守上界（二值分布 {0,1} 的方差 = 0.25，[0,1] 均匀分布的方差 $\approx 0.083$）。

**Welford's Online Algorithm**：

```
State: count, mean, M2

on each new confidence value x:
  count += 1
  delta = x - mean
  mean += delta / count
  delta2 = x - mean
  M2 += delta * delta2

variance = M2 / count  // population variance
```

滑动窗口版本需维护 circular buffer + 增量更新，仍为 O(1) per event。

**输入事件**：`gear:arbiter_evaluated`（`payload.confidence`）

**边界案例**：

| 情况 | S 值 | 理由 |
|------|------|------|
| 无 arbiter 事件 | 1.0 | 无波动 = 完美稳定 |
| 所有 confidence 相同 | 1.0 | 方差 = 0 |
| confidence 在 0/1 间交替 | 0.0 | 最大不稳定 |

---

## 3.7 Composite Score 与权重

**公式** [D3-R4, 20/20]：

$$Q = w_C \cdot C + w_E \cdot E + w_{\text{Conv}} \cdot \text{Conv} + w_S \cdot S$$

Phase 1 权重全部固定为 0.25（等权重）。PASCAL 的最大熵论证：在没有经验数据支持任何维度更重要的前提下，最大熵原则（Maximum Entropy Principle）指示给每个可能性相同的权重——这不是懒惰，而是在无信息时的最优策略。

Phase 2 权重可配置，存储在 monitor plugin config 中（不是 `ManoAggregatorConfig`——计算者拥有其参数）。三组预设：

| 预设 | coherence | efficiency | convergence | stability |
|------|-----------|-----------|-------------|-----------|
| balanced | 0.25 | 0.25 | 0.25 | 0.25 |
| stability-focused | 0.15 | 0.20 | 0.15 | 0.50 |
| efficiency-focused | 0.15 | 0.50 | 0.20 | 0.15 |

验证约束：$\sum w_i = 1.0$，每个 $w_i \in [0, 1]$。

**值域保证**：每个维度 $d_i \in [0, 1]$，权重 $w_i \in [0, 1]$，$\sum w_i = 1.0$，因此 $Q \in [0, 1]$。这个有界性对 L3 整合的 BIBO 稳定性至关重要。

---

## 3.8 观测器性质：控制理论视角

WIENER 特别强调四维公式的**纯观测函数**性质——这是控制理论中观测器（observer）的定义：

- **输入**：系统事件流（不可控，只读）
- **状态**：内部滑动窗口（不影响被观测系统）
- **输出**：LoopQualityVector（只读报告，不回写）

Monitor 的蕴归属 = [vedana, samjna, vijnana]，**排除 samskara**。四个公式均为观测计算，绝不修改 EventBus 上的事件、不调用任何 plugin、不触发任何行动。这确保了观测器不会干扰被观测系统——控制理论中的「非侵入性观测」原则。

**Lyapunov 稳定性前瞻**：stability 维度（S）的方差时间序列为 Cycle 02-7 的 Lyapunov 稳定性分析提供基础数据。若 $\sigma^2$ 持续下降，符合 Lyapunov 函数递减条件的前提。

---

## 3.9 EventBus 事件订阅 [D3-R2, 20/20]

**Phase 1（MINIMAL_QUALITY_EVENTS = 6）**：

1. `gear:arbiter_evaluated` → stability（confidence 值）
2. `gear:switch` → coherence + convergence（gear 值）
3. `action:proposed` → efficiency 分母
4. `tool:result` → efficiency 分子
5. `loop:started` → tick 计数、窗口重置
6. `loop:finished` → 触发品质报告发出

**Phase 2（+5 EXTENDED_QUALITY_EVENTS）**：

7. `sparsha:contact` → 输入频率分析
8. `tool:error` → 细化效率计算
9. `tool:blocked` → 安全阻挡频率
10. `vitakka:stall` → 认知停滞侦测
11. `action:executed` → 执行延迟分析

**退化原则**（HERACLITUS）：缺失事件 → 安全预设值，不报错。效率缺失 → 1.0（假设正常），稳定性缺失 → 0.5（中性）。「缺失是信息，不是错误。」

**Plan30 行动项**：Plan27b 中散落在代码里的事件字符串必须提升为 `AgentEventType` 常量——7 个新常量（6 个既有 + `LOOP_QUALITY_UPDATED`）。

---

## 3.10 计算复杂度摘要

| 维度 | 每事件 | 每报告 | 空间 |
|------|--------|--------|------|
| coherence | O(1) | O(1) | O(W) circular buffer |
| efficiency | O(1) | O(1) | O(1) 两个计数器 |
| convergence | O(1) | O(1) | O(W) circular buffer |
| stability | O(1) | O(1) | O(W) circular buffer + Welford state |
| **composite** | -- | O(1) | -- |

**整体**：O(1) per event，O(1) per report，O(W) 空间。在 W=10 的情况下，内存开销可忽略不计。
