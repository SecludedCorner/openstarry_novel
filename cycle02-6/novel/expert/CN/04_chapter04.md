# 第四章：Option C——独立通道的架构决策

---

## 4.1 问题空间：Layer 3 如何整合

OQ-29-2 的原始问题：

> Layer 3 (Delta_loopQuality) 如何整合进 Model Delta 五层模型？是加法叠加、乘法缩放、还是独立通道？

v0.29.0-alpha 的五层模型现状：

| Layer | 名称 | 作用对象 | 实现状态 |
|-------|------|---------|---------|
| L0 | Safety Floor/Ceiling | 全域 clamp [0.30, 0.90] | v0.28.0 已实现 |
| L1 | Klesha | baseThreshold += klesha gain | v0.28.0 已实现 |
| L2 | Audit Delta | confidence += clamp(delta, +-0.05) | v0.29.0 已实现 |
| L3 | LoopQuality | **TBD** | 未实现 |
| L4 | VedanaEmergency | threshold += boost [0, +0.15] | v0.28.0 已实现 |

Layer 2 已布线（audit delta 加到 confidence），Layer 3 完全空白。LoopQualityMonitor 的 SDK + Registry 已就位，但输出（`LoopQualityVector`）未连接到任何路由逻辑。

---

## 4.2 三方案比较：为什么不是 A 或 B

### Option A：加法叠加

```
theta_final = clamp(theta_base + DeltaL1 + DeltaL2 + DeltaL3 + DeltaL4, 0.30, 0.90)
```

**优点**：与现有模型完全一致（所有 delta 相加），实现一行。

**WIENER 的稳定性分析**：

令 $V = (c - \theta)^2$ 为 Lyapunov 候选函数。Option A 下 $c_{\text{eff}} = c + \Delta_{L2} + \Delta_{L3}$，阈值不变。

$$\dot{V} = 2(c_{\text{eff}} - \theta)(\dot{\Delta}_{L2} + \dot{\Delta}_{L3})$$

若 $\Delta_{L2}$ 和 $\Delta_{L3}$ 同号且递增，$\dot{V} > 0$（Lyapunov 函数递增 = 不稳定趋势）。同向累积最坏可达 +0.08（0.05 + 0.03），超过任何单层限幅的设计意图。

更危险的是 **cross-amplification**：audit delta 基于 arbiter confidence，loopQuality 也观察路由行为。两者可能对同一异常做出同向反应，形成间接耦合。

**结论**：Option A 在 L2/L3 同向累积时**无法保证稳定**。

### Option B：乘法缩放

```
theta_adjusted = theta_after_L2 * (1 + loopQualityFactor)
```

展开：$c_{\text{eff}} = (c + \Delta_{L2}) \times (1 + f_{L3}) = c + \Delta_{L2} + c \cdot f_{L3} + \Delta_{L2} \cdot f_{L3}$

交叉项 $\Delta_{L2} \cdot f_{L3}$ 构成直接耦合。即使各通道单独有界，交叉项可放大整体偏移。另外，乘法使系统从线性变为非线性，Lyapunov 稳定性分析复杂度大幅增加。边界行为也不佳：低信心度（如 0.35）时乘法调整幅度过小（0.035），失去调节意义。

**结论**：Option B 引入**不可忽略的交叉项**，稳定性分析困难。

### Option C：独立通道

```
L2: confidence_adjusted = confidence + clampAuditDelta(audit.delta)  [+-0.05]
L3: theta_adjusted = max(thresholdFloor, theta * (1 - alpha * q))    [alpha=0.10]
```

L2 调整**信心度**，L3 调整**阈值**。两者作用于不同变量，构成两个独立控制通道。

---

## 4.3 Option C 的稳定性证明

**控制系统建模**：

| 角色 | 元素 | 描述 |
|------|------|------|
| Plant | Agent 行为 | 齿轮选择 → 行动品质 |
| Sensor | ILoopQualityMonitor | 观测行为品质 |
| Controller | L3 阈值调整 | 根据品质微调通过门槛 |
| Disturbance | IConfidenceAuditor | 修正信心度估计 |

**Lyapunov 分析**：

令 $V = (c_{\text{eff}} - \theta_{\text{eff}})^2$

- 通道 1：$c_{\text{eff}} = c + \Delta_{L2}$，其中 $\Delta_{L2}$ 只依赖 arbiter 输出
- 通道 2：$\theta_{\text{eff}} = \theta \times (1 - \alpha \cdot q)$，其中 $q$ 只依赖 EventBus 事件

$$\dot{V} = 2(c_{\text{eff}} - \theta_{\text{eff}})(\dot{\Delta}_{L2} + \alpha \cdot \theta \cdot \dot{q})$$

因为 $\Delta_{L2}$ 不依赖 $q$，$q$ 不依赖 $\Delta_{L2}$，两者**无交叉项**。

每个通道独立满足 BIBO：

- $|\Delta_{L2}| \le 0.05$（硬限幅）
- $\alpha \cdot q \in [0, 0.10]$（$\alpha = 0.10$，$q \in [0, 1]$）

**BIBO 稳定性定理（非正式）**：在 Option C 下，若 L2 和 L3 各自满足 BIBO 稳定性，且 L2 不依赖 L3 输出、L3 不依赖 L2 输出，则整体系统 BIBO 稳定。

**证明草稿**：L2 和 L3 构成并联（parallel）控制通道。并联系统的稳定性等价于各通道独立稳定性的联合（parallel interconnection theorem）。各通道均有硬限幅，因此 BIBO 稳定。L0 Safety Floor/Ceiling 提供全域安全网。

**严格 Lyapunov 证明延后至 Cycle 02-7**（P1 Lyapunov 参数校准）。

---

## 4.4 语义对称性

Option C 的语义区分极为清晰：

| 维度 | L2 (Audit) | L3 (LoopQuality) |
|------|-----------|-------------------|
| 作用对象 | confidence（信心度） | threshold（阈值） |
| 语义问句 | 「这个 arbiter 的判断可靠吗？」 | 「目前系统状态是否适合快速路径？」 |
| 控制理论类比 | 状态估计器校正（state estimator correction） | 参考输入调整（setpoint adjustment） |
| 方向 | 调整「测量值」的可信度 | 调整「通过门槛」的严格度 |
| 输入来源 | AuditContext（arbiter 结果） | EventBus（monitor 观测） |
| 数值范围 | +-0.05 | alpha * q in [0, 0.10] |

WIENER 的评价：「这是我见过最干净的分离。两个通道各自有明确的物理意义，不会互相污染。」

---

## 4.5 alpha 参数选择

| alpha | theta=0.6 时最大调整 | 评估 |
|-------|---------------------|------|
| 0.05 | 0.57（降 0.03） | 极保守 |
| **0.10** | **0.54（降 0.06）** | **建议预设** |
| 0.15 | 0.51（降 0.09） | 激进 |
| 0.20 | 0.48（降 0.12） | 过度——可能突破 thresholdFloor |

WIENER 选择 alpha = 0.10 的理由：

1. 最大调整约 +-6%，在人类可感知范围内，便于调试
2. 与 L2 的 +-0.05 影响量级相当——L3 不会淹没 L2
3. 保守起步，可根据 Simulation 数据调整

**L3 公式的语义解释**：

| compositeLoopQuality | theta_adjusted（theta=0.6） | 含义 |
|---------------------|---------------------------|------|
| 1.0（最佳品质） | 0.54（theta * 0.9） | 系统运行稳定 → 略微放松阈值 → 更容易快速路径 |
| 0.5（中等品质） | 0.57（theta * 0.95） | 中等调整 |
| 0.0（最差/无观测） | 0.60（theta * 1.0） | 保守退化——阈值不变 |

---

## 4.6 品质分数的双通道传递

品质监控器产出的分数有两个消费者，需求不同：

| 消费者 | 需要什么 | 通道 |
|--------|---------|------|
| ManoAggregator（L3 阈值调整） | 即时的 composite 数字 | **pull**：`loopQualityFn()` 回调 |
| IConfidenceAuditor（丰富背景） | 四维向量 + composite | **push**：extras bag via EventBus |

**Pull 通道**：`loopQualityFn` 注入 `createManoAggregator`，在 `route()` 内每次需要时同步调用。

```typescript
export function createManoAggregator(
  bus: EventBus,
  config: ManoAggregatorConfig,
  baseThresholdFn?: () => number,
  vedanaFn?: () => ChannelVedana,
  vedanaEmergencyConfig?: VedanaEmergencyConfig,
  auditor?: IConfidenceAuditor,
  loopQualityFn?: () => number,  // 新增：回传 compositeLoopQuality in [0, 1]
): ManoAggregator
```

**Push 通道**：Monitor 使用 SDK `emitWithExtras()` 同时发出：
- `loopQuality:updated` 事件（ManoAggregator 订阅，用于 pull 回调的内部缓存更新）
- `audit:context_contribute` 事件（ManoAggregator 收集进 extras bag）

extras 中的 key：
- `loopQuality:composite` → composite score（number）
- `loopQuality:vector` → 四维向量对象

LEIBNIZ 的关键约束：「品质分数的生命周期是 per-routing-cycle。每次路由结束，extras bag 清空。不累积、不持久化。」延迟一 tick 可接受——品质是历史指标，不需要即时到微秒级。

---

## 4.7 边界条件分析

**无 Monitor Plugin（G-0 退化路径）**：`loopQualityFn` 回传 `undefined` 或 `q_default = 0`，L3 不生效：`theta_adjusted = theta`（乘以 1.0）。系统行为与没有 ILoopQualityMonitor 时完全相同。

**Monitor 报告过时**：设定 `monitorStalenessMs = 5000`（可配置）。过期则视为无观测 → q = 0。WIENER 的理由：过时观测等于引入「幽灵信号」，与零阶保持（ZOH）原则的有效期限概念一致。

**多 Monitor 聚合**：Phase 1 使用简单平均（降低个别 monitor 的噪声影响）。BABBAGE 提出的悲观策略（取最低）被否决——单一异常 monitor 不应过度影响整体。

**compositeLoopQuality = 1.0 极端值**：若 `theta = thresholdFloor = 0.30`，`theta_adjusted = 0.27 < thresholdFloor`。修正：L3 调整后仍需遵守 L0：

```typescript
const adjustedThreshold = Math.max(
  config.thresholdFloor,
  threshold * (1 - loopQualityAlpha * compositeLoopQuality),
);
```

---

## 4.8 完整五层公式（Option C 整合后）

```
theta_base                                        // 基础阈值（config 注入）
  + L1: Sigma(w_k * K_k)                         // Klesha 增益（baseThresholdFn）
  + L4: thresholdBoost                            // VedanaEmergency 提升
  = theta_intermediate

theta_adjusted = max(thresholdFloor,
                     theta_intermediate * (1 - alpha * q))  // L3: LoopQuality
theta_final = min(thresholdCeiling, theta_adjusted)         // L0 上限

confidence_adjusted = confidence
                    + clampAuditDelta(audit.delta)          // L2: Audit

routing = (confidence_adjusted > theta_final)
        ? arbiter_gear
        : default_gear
```

**Layer 执行顺序**：L4（VedanaEmergency）→ L1（Klesha）→ L3（LoopQuality）→ 比较（含 L2-adjusted confidence）。L4 优先因为它处理安全关键的紧急状态。

**L2 与 L3 的最坏交互**：confidence 增加 0.05 且 threshold 降低 0.06 → 净效果约 0.11。仍在 L0 安全范围内（`thresholdFloor` + `maxConfidenceByGear` 共同约束）。

---

## 4.9 ManoAggregator 代码整合点

在 `mano-aggregator.ts` 的 arbiter 回路中，L134-L138 现行阈值计算后插入 L3 调整：

```typescript
// 现行：L0 + L1 + risk adjustment
const threshold = evaluation.riskCategory
  ? computeAdjustedThreshold(
      effectiveBaseThreshold, evaluation.riskCategory,
      config.riskDelta, config.thresholdFloor, config.thresholdCeiling)
  : effectiveBaseThreshold;

// 新增：Layer 3 -- LoopQuality threshold adjustment
const loopQualityAlpha = config.loopQualityAlpha ?? 0.10;
const q = loopQualityFn ? loopQualityFn() : 0;
const adjustedThreshold = Math.max(
  config.thresholdFloor,
  threshold * (1 - loopQualityAlpha * q),
);

// 修改：使用 adjustedThreshold
if (evaluation.confidence > adjustedThreshold) {
  // ... existing routing logic ...
}
```

新增 `ManoAggregatorConfig` 字段：

```typescript
export interface ManoAggregatorConfig {
  // ... existing fields ...
  readonly loopQualityAlpha?: number;       // [0, 0.2], default: 0.10
  readonly monitorStalenessMs?: number;     // default: 5000
  readonly historicalConfidenceSize?: number; // default: 10
}
```

WIENER 的最终声明：「Option C 的稳定性保证基于两通道独立性假设。若未来设计破坏此独立性（如让 auditor 读取 loopQuality 并据此调整 delta），稳定性保证不再成立。extras bag 中 auditor 可以看到 `loopQuality:composite`，但 WIENER C-1/C-2/C-3 确保了即使看到也不会形成正反馈回路——因为 auditor 的 delta 不会回馈到 loopQuality 的计算中。」
