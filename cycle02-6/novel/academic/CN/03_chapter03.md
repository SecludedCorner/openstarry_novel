# 第三章：四维品质向量 —— 认知回路的量化评估框架

---

## 3.1 问题定义

OpenStarry 的 AI Agent 运作于认知回路中：sparsha → vedana → samjna → samskara → manas/vijnana → 下一轮输入。`ILoopQualityMonitor` 需对此回路的运作品质进行即时量化评估。品质是多维概念，单一指标不足。WIENER（#12）与 ATHENA（#5）设计了四维品质向量（LoopQualityVector），经 D3-R1（20/20）确认。

---

## 3.2 四维公式

设滑动窗口大小 $W = 10$，暖机期 $W_{warmup} = 5$。

### 3.2.1 一致性（Coherence）

$$\text{coherence} = 1 - \frac{\text{switchCount}}{W - 1}$$

衡量路由决策稳定性。高值表示 Agent 持续在同一处理模式下运作，低值表示频繁切换。输入事件：`gear:switch`。

### 3.2.2 效率（Efficiency）

$$\text{efficiency} = \frac{\text{success}}{\text{proposed}} \quad (\text{若 proposed} = 0, \text{则} = 1.0)$$

衡量工具调用成功率。退化处理：无 proposed 事件时预设 1.0。输入事件：`action:proposed`, `tool:result`。

### 3.2.3 收敛性（Convergence）

$$\text{convergence} = \frac{\text{longestStreak}}{W}$$

衡量 Agent 是否趋近稳定状态。与效率的区别：效率衡量"总量"，收敛性衡量"趋势"—— 8 次成功集中在最后 8 次（收敛性 0.8）与散布在窗口各处（可能仅 0.3）意义不同。输入事件：`gear:switch`。

### 3.2.4 稳定性（Stability）

$$\text{stability} = 1 - \min\left(1, \frac{\sigma^2}{0.25}\right)$$

衡量仲裁器信心度输出的方差。分母 0.25 为宽松正规化基准。输入事件：`gear:arbiter_evaluated`。

---

## 3.3 复合品质分数与权重

$$Q = \sum_{i=1}^{4} w_i \cdot d_i, \quad Q \in [0, 1]$$

Phase 1 等权重 $w_i = 0.25$。理论依据为 PASCAL（#19）的最大熵论证：在缺乏先验知识的情况下，最大熵原则（Jaynes 1957）要求均匀分配权重。D3-R4（20/20）确认 Phase 1 固定等权重、Phase 2 可配置（balanced / stability-focused / efficiency-focused 三组预设）。

---

## 3.4 滑动窗口与计算复杂度

| 参数 | 值 | 理由 |
|------|-----|------|
| $W$ | 10 | 敏感度与稳健性之间的平衡 |
| $W_{warmup}$ | 5 | 暖机期避免小样本偏差 |
| $Q_{default}$ | 0.5 | 暖机期内的中性预设值 |

所有计算 $O(1)$ per event、$O(W)$ 空间，确保品质监控不成为性能瓶颈。

---

## 3.5 EventBus 事件订阅 [D3-R2, 20/20]

**Phase 1（6 事件）**：`gear:arbiter_evaluated`（稳定性）、`gear:switch`（一致性+收敛性）、`action:proposed`（效率）、`tool:result`（效率）、`loop:started`（窗口管理）、`loop:finished`（窗口管理）。

**Phase 2（+5 事件）**：`sparsha:contact`, `tool:error`, `tool:blocked`, `vitakka:stall`, `action:executed`。

**退化原则**（HERACLITUS #15）："缺失是信息，不是错误。"缺失事件使用安全预设值（效率 1.0、稳定性 0.5），不抛出异常。同时将散布于代码中的事件字符串字面量统一提升为 `AgentEventType` 常量。

---
