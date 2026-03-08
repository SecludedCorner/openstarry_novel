# 序章：从清创到精密工程

---

Cycle 02-5 是一次大规模清创手术。

二十位研究者在五天内做出 29 项决议，DC Master 覆议推翻其中两项（D3-R3 四智映射、D4-R1 心所命名），整个团队对七份设计文件进行去装饰化重构——移除不具驱动力的佛学标签、统一命名惯例、拆解错误的蕴归属映射。那五天像是对 codebase 进行 dead code elimination：不是增加功能，而是移除积累的语义债务。

Cycle 02-6 的调性截然不同。前一轮回答的是「什么是错的」；这一轮要回答的是「正确的规格长什么样」。

---

## 双重输入

DC Master 发出两封信件，分别触发工程轨和哲学轨。

**工程信件**指向 Plan29 交付后的六个 Open Questions（OQ-29-1 至 OQ-29-6）。Plan29（v0.29.0-alpha）新增了 `ILoopQualityMonitor`（回路品质监控器接口）和 `IConfidenceAuditor`（信心度审计接口），但两者都只有 SDK 骨架——Registry 已接入 `PluginHooks`，类型定义已 export，却没有预设实现、没有计算公式、没有与 `ManoAggregator` 的布线。Master 要求研究团队回答：品质怎么算（OQ-1）？Layer 3 怎么整合（OQ-2）？审计策略方向（OQ-3）？事件订阅清单（OQ-4）？权重可配置性（OQ-5）？整体怎么放进 Plan30（OQ-6）？

**哲学信件**直指行蕴（samskara-skandha）的定义问题。Master 明确批评唯识学派将 49 个心所归入行蕴的做法「非常有问题」，并要求以原始经典（如是我闻）为第一手依据进行深掘。这不是一个装饰性的研究方向，而是直接影响 `ISamskara` 接口未来拓展路径的基础判定。

---

## SUNYATA 的双轨架构

研究总监 SUNYATA 据此设计了双轨结构，并建立跨轨道优先权：

| 轨道 | 范畴 | 子项 | 团队 |
|------|------|------|------|
| Track A | AuditContext 类型 + 审计日志 | A1-A4 | VITRUVIUS, KERNEL, GUARDIAN, ARCHIMEDES, WIENER, BABBAGE |
| Track B | ILoopQualityMonitor 实现规格 | B1-B4 | WIENER, ATHENA, BABBAGE, HERACLITUS, TURING, PASCAL |
| Track C | 行蕴深掘 | C1-C4 | NAGARJUNA, ASANGA, LINNAEUS, PENROSE, PASCAL |
| Track D | 工程同步 | D1-D2 | TURING, ARCHIMEDES, VITRUVIUS, GUARDIAN |

跨轨道影响协议的关键规则：**哲学结论（D1）先于工程设计（D2/D3），确保蕴归属判定不被工程便利性覆盖。** 若 C1-C4 的结论与 A/B 的设计假设产生冲突，工程轨必须等待哲学裁定。

R1 产出 14 份独立研究报告。R2 交叉审阅发现 24 个共识点、仅 3 个分歧点。R3 三场辩论、245 分钟、17 项决议、13 项全票（20/20）、0 项否决。

这是一轮精密工程。

---

# 第一章：行蕴的原典重建

---

## 1.1 方法论：如是我闻

哲学轨由 NAGARJUNA（中观学派）和 ASANGA（唯识学派）共同领衔。Master 批评的正是唯识学派的做法，而 SUNYATA 刻意安排唯识专家参与自我批判——这不是惩罚性安排，而是方法论上的必要：只有深谙系统内部逻辑的人才能精确指出其断裂点。

文献层次严格区分：

| 层次 | 来源 | 地位 |
|------|------|------|
| 第一层 | 巴利五部（Nikaya）/ 汉译阿含 | 唯一定义依据 |
| 第二层 | 十二因缘相关经文（SN 12） | 结构性参考 |
| 第三层 | 名色识架构（SN 12.2, MN 9） | 交叉验证 |
| 排除 | 阿毘达磨论典（Vibhanga, Dhammasangani） | 仅作对比，不作归属依据 |

这个分层直接回应了 Master 的指示：论典是后世学者的系统化产物，不是佛陀的原话。

---

## 1.2 SN 22.56：六思身——行蕴的原始定义

蕴相应（Khandha-samyutta）的 SN 22.56（取蕴经）是五蕴定义的核心出处：

> 比丘们，什么是行蕴（sankhara-kkhandha）？有六种思身（cha cetana-kaya）：色思、声思、香思、味思、触思、法思。比丘们，这就称为行蕴。

经文分析：

| 巴利原文要素 | 内容 | OpenStarry 对应 |
|-------------|------|----------------|
| rupa-sancetana | 色思——对色尘的意图 | 对 visual/text input 的反应意图 |
| sadda-sancetana | 声思——对声尘的意图 | 对 audio/event input 的反应意图 |
| gandha-sancetana | 香思——对香尘的意图 | 非 Agent 典型场景 |
| rasa-sancetana | 味思——对味尘的意图 | 非 Agent 典型场景 |
| photthabba-sancetana | 触思——对触尘的意图 | 对 API/tactile event 的反应意图 |
| dhamma-sancetana | 法思——对法尘的意图 | 对内部认知对象的反应意图 |

关键洞见：**原始经典中行蕴的定义完全以 cetana（意图/意志）为中心**——是六种针对感官对象的意图形成，不是「受想以外的心理活动杂物箱」。

---

## 1.3 SN 22.79：造作一切有为法

> 比丘们，为什么称为行（sankhara）？因为它们造作（abhisankharonti）有为法（sankhatam）。造作什么有为法？以色的形态造作色，以受的形态造作受，以想的形态造作想，以行的形态造作行，以识的形态造作识。

这段经文揭示了行蕴的第二个核心特质：**行蕴不仅造作行为，更造作所有五蕴的被条件化状态**。在工程语境中，`ISamskara` 不应仅限于 `ITool.execute()` 这样的外部工具调用，而应涵盖「改变系统状态的一切造作」——包括改变系统对未来输入的反应模式。

这直接连结到 VasanaEngine 的长期路线图（D-29-8）：过去的行为模式影响未来的齿轮选择，正是「行蕴造作识蕴的被条件化状态」的工程体现。

---

## 1.4 SN 22.95：芭蕉喻——无核心的动态过程

> 行如芭蕉（kadalupamo sankhara）——若人剥芭蕉杆，寻找坚实的核心，却一层层剥尽，什么也找不到。

这是行蕴第三个核心特质的经典表述：**无核心的动态过程**。行蕴不是一个固定的「东西」（entity），而是一个不断运转的「过程」（process）。

工程对应非常精确：`ISamskara` 的 plugin 应是轻量、可组合的（composable），不依赖持久性内部状态。每个 plugin 都是一个「层」，剥开任何一层都不会找到不可替代的核心逻辑。这与 OpenStarry 的 Tenet #2（一切皆 Plugin）和微核心架构（Core 不包含业务逻辑）完美契合。

---

## 1.5 MN 44：三行分类的互补观察角度

毘舍佉问法授比丘尼：

| 行 | 巴利名 | 定义 | 经文理由 |
|----|--------|------|---------|
| 身行 | kaya-sankhara | 入出息（呼吸） | 身法，系缚于身 |
| 语行 | vaci-sankhara | 寻（vitakka）+ 伺（vicara） | 先寻伺后发语 |
| 心行 | citta-sankhara | 想（sanna）+ 受（vedana） | 心法，系缚于心 |

这里存在一个经典框架间的张力：citta-sankhara（心行）**包含** sanna（想）和 vedana（受），但在五蕴框架中这两者是独立的蕴。NAGARJUNA 的分析：**这不是逻辑矛盾，而是不同分类系统的不同观察角度（drsti-bheda）**——三行分类观察「什么条件化什么」，五蕴分类观察「什么是修行的关键观察对象」。唯识学派试图强制统一两个系统，导致了 49 心所塞进行蕴的问题。

工程启示：身行对应 `ITool.execute()`（物理层造作），语行对应寻伺（`vitakka-vicara`，认知初始处理），心行对应 `IVedana` + `ISamjna`（已覆盖）。值得注意的是，`VitakkaWatchdog` 在 OpenStarry 中是稳定化监控机制，功能上更接近识蕴而非行蕴——这不是归属错误，而是 MN 44 的语行分类与五蕴分类本就是互补视角。

---

## 1.6 唯识心所系统的批判

ASANGA 亲自主导了对唯识学派 51 心所系统的批判性分析（C2 报告）。唯识学派将 51 心所中的 49 个归入行蕴——仅留「受」和「想」给受蕴和想蕴。逐条分析结果：

| 分类 | 数量 | 比例 | 说明 |
|------|------|------|------|
| 确属行蕴 | 7 | 14% | chanda, virya, apramada, mraksa, matsarya, maya, sathya |
| 已有正确归属 | 12 | 24% | 已在 OpenStarry 中经辩论确认的 plugin |
| 可能属他蕴 | 18 | 37% | 功能上更接近识蕴（判断性）或受蕴（感受性） |
| 混合/待研究 | 14 | 28% | 跨蕴功能，需逐案分析 |

ASANGA 的结论：「心所列表的功能描述有参考价值，但其蕴归属分类已偏离原典的 cetana 中心定义。」这不是全面否定唯识学——而是在原典与论典之间做出了清晰的方法论区分。

---

## 1.7 三准则与核心区分

LINNAEUS 从原典分析中归纳出「行蕴属性判定三准则」，作为永久性判定工具 [D1-R3, 20/20]：

1. **造作性**（Conditioning）：是否创造/改变/产生新状态？
2. **意图驱动**（Cetana-driven）：是否由意图形成过程驱动？
3. **环境改变**（Environmental Shift）：是否改变后续认知条件？

三个问题全部为「是」→ 行蕴（samskara）；全部为「否」→ 识蕴（vijnana）；混合 → 需逐案分析，可能跨蕴。

PENROSE 将此进一步压缩为一个程序设计者立即能理解的区分：

> **行蕴 = WRITE**（主动改变世界的状态）
> **识蕴 = READ**（被动评估世界的状态）

在 OpenStarry codebase 中的对应：

| 蕴归属 | 接口 | 操作类型 | 代码路径 |
|--------|------|---------|-----------|
| 行蕴（WRITE） | `ITool` | 工具执行，改变环境 | `types/aggregates.ts#ISamskara` |
| 行蕴（WRITE） | `ISlashCommand` | 指令执行，改变状态 | `types/aggregates.ts#ISamskara` |
| 识蕴（READ） | `IGuide` | 评估引导，不改变状态 | `types/aggregates.ts#IVijnana` |
| 识蕴（READ） | `IVolition` | 审议判断，不改变状态 | `types/aggregates.ts#IVijnana` |

这个 WRITE/READ 区分被 D1-R5 全票确认（20/20），成为蕴归属判定的操作性原则。

---

# 第二章：AuditContext 与回馈回路防护

---

## 2.1 问题：审计员的信息贫乏

v0.29.0-alpha 中 `IConfidenceAuditor.audit()` 的签名为：

```typescript
// v0.29.0-alpha 现状
audit(routeResult: RouteResult): ConfidenceAuditResult | Promise<ConfidenceAuditResult>;
```

其中 `RouteResult` 仅包含 `{ gear, decidedBy, confidence, riskAdjusted, riskCategory }`。一个有效的审计员需要更多上下文：触发事件是什么？arbiter 的完整推理过程？近期信心度趋势？其他 plugin 观测到的辅助数据？

DC Master 在 R0 指示中裁定方案 B（泛型 Context Bag）为唯一正确方向，否决了方案 A（固定字段扩展）的僵化设计。

---

## 2.2 AuditContext 完整类型定义 [D2-R1, 20/20]

```typescript
import type { SparshEvent } from './coarising.js';
import type { GearEvaluation, RouteResult, RiskCategory } from './gear-arbiter.js';

/**
 * AuditContext -- rich context for confidence auditing.
 *
 * Replaces bare RouteResult as the input to IConfidenceAuditor.audit().
 * Core fields provide the minimum for meaningful auditing;
 * extras bag allows plugin-contributed data without Core coupling.
 *
 * @version 1 -- initial version (Cycle 02-6)
 */
export interface AuditContext {
  /** Schema version for forward compatibility. Literal type. */
  readonly version: 1;

  /** 触发本次认知回路的 SparshEvent */
  readonly sparshEvent: SparshEvent;

  /** 胜出 arbiter 的完整评估结果（含 confidence + reasoning） */
  readonly gearEvaluation: GearEvaluation;

  /** 当前风险等级（可能为 undefined = 未宣告） */
  readonly riskCategory: RiskCategory | undefined;

  /** 路由结果（审计前快照） */
  readonly routeResult: RouteResult;

  /**
   * 近期历史信心度序列（opt-in，环形缓冲区，预设 size=10 可配置）。
   *
   * WIENER C-1 约束：仅包含原始 arbiter 信心度，
   * 不包含 audit 后的修正值。
   */
  readonly historicalConfidence?: readonly number[];

  /**
   * Plugin 贡献的额外上下文数据。
   * ManoAggregator 从 EventBus 收集 plugin 的 context contribution，
   * 统一放入此 Map。Core 不感知具体 key/value 语义。
   * 传入 auditor 前以 Object.freeze() 冻结。
   */
  readonly extras: ReadonlyMap<string, unknown>;
}
```

**设计抉择摘要**：

| 决策点 | 选项 | 最终选择 | 理由 |
|--------|------|---------|------|
| `sparshEvent` 是否 optional | optional vs required | **required** | 每次路由必有触发事件；ManoAggregator 经由 `sparshEventFn` 回调取得 |
| `historicalConfidence` 缓冲区大小 | 固定 10 vs 可配置 | **预设 10 可配置** | `ManoAggregatorConfig.historicalConfidenceSize` |
| `version` 类型 | `number` vs 字面量 `1` | **字面量 `1`** | 强制类型检查，未来版本递增为 `2` |
| `extras` 类型 | `Record<string, unknown>` vs `ReadonlyMap` | **`ReadonlyMap`** | Map 语义更清晰，freeze 更直观 |

**IConfidenceAuditor 接口更新**：

```typescript
export interface IConfidenceAuditor extends IVijnana {
  readonly id: string;
  audit(context: AuditContext): ConfidenceAuditResult | Promise<ConfidenceAuditResult>;
}
```

这是一个 breaking change（参数从 `RouteResult` 改为 `AuditContext`），但 TURING 在 D1 代码验证中确认 v0.29.0-alpha **尚无任何 IConfidenceAuditor plugin 实现**——这是最佳重构时机，零实际影响。

---

## 2.3 WIENER 约束：回馈回路的系统性切断

WIENER 在 Cycle 02-4 D5 中已证明：若历史 audit delta 回馈至当前 audit 输入，可产生正反馈回路：

```
Loop N:   auditor 输出 delta = +0.03
Loop N+1: auditor 看到上次 delta = +0.03，倾向正向 → delta = +0.04
Loop N+2: 持续正向累积 → 系统漂移
```

形式化表述：令 $c_n$ 为第 $n$ 次回路的 arbiter 原始信心度，$\delta_n$ 为 audit delta。

- **允许的输入**：$\delta_n = f(c_n, c_{n-1}, \ldots, c_{n-k}, \text{extras}_n)$ -- 观测函数
- **禁止的输入**：$\delta_n = g(\delta_{n-1}, \delta_{n-2}, \ldots)$ -- 自回归函数

前者的稳定性取决于被观测系统（外生的），后者可独立发散（内生的）。这是控制理论中观测器（observer）与自回归系统（autoregressive system）的根本区别。

据此设计三条硬约束（WIENER Constraints C-1/C-2/C-3）：

**C-1**：`historicalConfidence` 仅包含原始 arbiter 信心度（`GearEvaluation.confidence`），不包含 audit 后的修正值（`auditedConfidence`）。

```typescript
// ManoAggregator 内部——每次 arbiter 胜出后记录
confidenceHistory.push(evaluation.confidence);  // 原始值
// 不是 confidenceHistory.push(auditedConfidence);  // 禁止
```

**C-2**：AuditContext 不包含任何 `previousAuditResult`、`previousDelta`、`auditHistory` 字段。Auditor 无法从 AuditContext 读取自身先前的输出。

**C-3**：extras bag 禁止三个前缀：`audit:`、`core:`、`internal:`。防止 auditor 透过 extras 绕过 C-2。

```typescript
// extras 写入验证
const FORBIDDEN_PREFIXES = ['audit:', 'core:', 'internal:'] as const;

function validateExtrasKey(key: string): boolean {
  return !FORBIDDEN_PREFIXES.some(prefix => key.startsWith(prefix));
}
```

BABBAGE 的 BIBO 稳定性验证：在 C-1/C-2/C-3 约束下，audit delta $\delta_n$ 的输入集合完全由外生变量构成（arbiter 原始信心度序列 + plugin extras），不包含任何自身历史输出。因此 $|\delta_n| \le 0.05$（硬限幅），系统满足有界输入 → 有界输出（BIBO stability）。

---

## 2.4 extras bag 协议 [D2-R2, 19/20]

extras bag 的设计在 R2 阶段出现了唯一的跨轨道分歧：A2（DARWIN + MESH）提出通用事件模式，B3（LEIBNIZ + MESH）倾向直接订阅。D2 辩论中统一为**双事件 + SDK 便利函数**：

| 面向 | 决议 |
|------|------|
| 写入模式 | Plugin 使用 SDK `emitWithExtras(key, value)` 便利函数 |
| 收集管道 | ManoAggregator 订阅 `audit:context_contribute` 事件 |
| 读取 | `getExtra<T>(extras, key, guard)` 类型安全存取器 |
| 不可变性 | 浅冻结（`Object.freeze`）+ `ReadonlyMap` |
| 容量限制 | 最多 32 keys，每 key 128 chars |
| 禁止前缀 | `audit:`, `core:`, `internal:` |
| key 命名惯例 | `{category}:{name}` -- 如 `loopQuality:vector`, `loopQuality:composite` |
| 生命周期 | per-routing-cycle（每次路由结束清空，不持久化） |

1 票反对（MESH）认为双事件模式增加了不必要的复杂度。但多数认为通用管道的投资回报更高：它不只为 LoopQualityMonitor 服务，任何未来的 Plugin 都能透过同一管道向 AuditContext 贡献数据。

---

## 2.5 ConfidenceAuditLog——GUARDIAN D5 债务清偿 [D2-R3, 20/20]

GUARDIAN 在 Cycle 02-5 D5 做了一个关键让步：同意 audit delta 限幅 +-0.05，条件是下一轮必须定义完整的审计日志格式。这是一笔安全债务。

Cycle 02-6 设计了 `ConfidenceAuditLog` 类型：

```typescript
export interface ConfidenceAuditLog {
  readonly timestamp: number;
  readonly auditorId: string;
  readonly inputConfidence: number;    // audit 前的信心度
  readonly rawDelta: number;           // auditor 建议的 delta
  readonly clampedDelta: number;       // 限幅后的 delta
  readonly wasClamped: boolean;        // 是否被限幅
  readonly reasoning: string;          // 截断至 500 chars，Core 负责
  readonly outputConfidence: number;   // audit 后的信心度
  readonly result: 'applied' | 'timeout' | 'error';
  readonly auditDurationMs: number;
}
```

传播通道：
- **主通道**：EventBus `audit:completed` 事件，即时可观察
- **持久化**：JSONL file appender（可选，Plan30 之后）
- **PII 净化**：reasoning 字段的 PII 清洗为 plugin 责任，Core 只做截断

GUARDIAN 在 D2 辩论中当场确认：「D5 的帐清了。我不再保留重新审议 +-0.05 限幅的权利。」这是一个重要的安全里程碑——自 Cycle 02-4 以来 GUARDIAN 持续挑战信心度调整的安全性，每次让步都附带条件。完整日志 + 三条回馈回路防护 + +-0.05 硬限幅，三重保障终于满足了他的安全要求。

---

## 2.6 版本控制策略

`AuditContext.version` 使用字面量类型 `1`（非 `number`），确保编译期类型检查。未来扩展时递增为 `2`，Auditor plugin 应对不认识的版本 fail-safe：

```typescript
function audit(ctx: AuditContext): ConfidenceAuditResult {
  if (ctx.version > 1) {
    return { delta: 0, reasoning: 'Unknown AuditContext version' };
  }
  // 正常审计逻辑...
}
```

这个 fail-safe 模式保证了向前兼容性：新版 Core 搭配旧版 Auditor plugin 时，auditor 不会因不认识新字段而崩溃，而是退化为 passthrough（delta=0）。

---

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

---

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

---

# 第五章：Master 的心所指示与永久性规则

---

## 5.1 触发：心所分析的连锁反应

哲学轨的 C2 报告（唯识学派心所批判）在 R2 交叉审阅时被呈给 DC Master。ASANGA 整理了 51 心所的逐条重新归属建议——其中 18 项（37%）被认为功能上更接近识蕴或受蕴，而非行蕴。

Master 的回应不是单次裁定，而是三轮渐进精化。每一轮的焦点更加锐利。

---

## 5.2 第一轮：经典与论典的方法论划界

Master 的核心主张：**心所（cetasika）是论典（阿毘达磨）的系统化产物，不是原始佛经（sutta/agama）的内容。**

这不是学术偏见。佛陀在原始经典中说了五蕴、十二因缘、八正道、三十七道品。「51 心所」这个分类系统是后世学者（特别是无著、世亲等唯识论师）的系统化整理。原典中确实出现了许多心所的名称（如慧、精进、惭、愧），但**将它们组织为固定数量的分类系统并指定蕴归属**是论典的工作。

Master 的直接结论：**Plugin 的命名不能使用心所的梵文名字。**

工程影响：任何以梵文心所名命名的 plugin（如 VīryaPlugin、PrajnaPlugin）必须改为工程术语。

---

## 5.3 第二轮：功能参考的保留

第一轮容易被误读为「心所完全无用」。Master 在第二轮中修正了这个印象：心所的**功能描述**有参考价值。

例如，心所「精进」（vīrya）描述了「持续不懈地投入善法」的功能。可以参考这个功能描述来设计一个 Plugin——但 Plugin 不能叫 VīryaPlugin，而应使用工程名称（如 `PersistencePlugin`、`RetryPlugin`）。

Master 的精确表述：「可以说『参考精进的涵义，设计了重试 Plugin』。但不能说『重试 Plugin = 精进』。」

这是「可援引、不可等同」的原则。

---

## 5.4 第三轮：命名解耦带来归属自由

第三轮是最深刻的。Master 说：「Plugin 不等于心所。」

表面上这很简单。但含义是结构性的。

在唯识学派中，每个心所有固定的蕴归属——「精进」属行蕴，「慧」属识蕴。如果 Plugin = 心所，那 Plugin 的蕴归属也被锁死。但 Plugin != 心所。一个 Plugin 可能同时有行蕴和识蕴的功能——它既做判断（READ），又执行动作（WRITE）。

在心所系统中这是不允许的（每个心所归属唯一蕴），但在 Plugin 系统中完全合法。**命名解耦带来归属自由**——不用心所名字命名 Plugin，反而让 Plugin 摆脱了论典的固定分类束缚，可以自然地跨越多个蕴。

---

## 5.5 八点永久性规则

三轮指示被整理成八条永久规则，与蕴归属五原则共同构成所有未来命名和归属问题的判定基准：

| # | 规则 | 工程影响 |
|---|------|---------|
| 1 | 心所是论典产物，非原始经典内容 | 不以心所系统作为架构设计的预设框架 |
| 2 | 心所功能有参考价值，可作 plugin 设计灵感 | 设计文件可引用心所的功能描述 |
| 3 | 可说明「参考某心所涵义，设计某 plugin」 | 设计溯源合法，等同宣称非法 |
| 4 | Plugin 使用工程术语命名，不得用心所梵文名 | 命名惯例硬规则 |
| 5 | 梵文术语限于原始经典者——五蕴(skandha)、触(sparsha) 可用 | 区分经典梵文 vs 论典梵文 |
| 6 | 心所分类不作为蕴归属依据 | 「唯识说 X 属行蕴」不能作为 plugin 归属证据 |
| 7 | 既有 plugin 归属决议不受影响 | 已确认的归属不因新规则翻案 |
| 8 | Plugin != 心所，蕴归属可自然跨多蕴 | 跨蕴 plugin 是合法的、预期的 |

---

## 5.6 蕴归属五原则 [D1-R6, 20/20]

与八点规则互补，五原则提供了正面的判定方法：

1. **功能分析为蕴归属的唯一依据**——不是名称、不是传统、不是论典
2. **唯识 51 心所系统作为功能参考清单，不作归属依据**
3. **梵文术语用于代码命名时，仅限源自原始经典者**
4. **Plugin 不等于心所，蕴归属可自然跨越多蕴**
5. **既有归属决议（基于功能分析）继续有效**

这五条原则加上八点规则，形成了一套完整的判定框架。未来每次有人问「这个功能属于哪个蕴」或「这个 plugin 该叫什么名字」，不再需要从头辩论——直接对照这 13 条规则即可。

---

## 5.7 D1 议程的连锁修订

Master 的三轮指示直接导致了 D1 辩论议程的修订：

- **D1-Q2（心所多蕴归属问题）被删除**——心所分类既然不作为依据，讨论其多蕴归属就失去意义
- **D1-Q6（逐条投票 26 项心所）被简化**——改为投票蕴归属原则本身，而非逐条判定
- **manasikara 追加议题被取消**——`CoarisingBundle` 中 manasikara 不是独立接口，无需额外讨论

这些修订节省了至少 45 分钟的辩论时间，同时提高了决议的抽象层次——从个案判定上升到原则确立。

---

## 5.8 心智论述工程借鉴评估 [D1-R4a/b/c]

C4 报告（PASCAL + PENROSE）对所有佛学心智论述的工程借鉴价值做了系统性评估：

| 论述 | 结论 | 决议 | 测试结果 |
|------|------|------|---------|
| 五蕴 | 已完成融入 | 无需行动 | -- |
| 名色识 | 核心价值已吸收 | 无需行动 | -- |
| 十二因缘 | 解释性附录 | 02-7 P2 [D1-R4a, 19/20] | -- |
| 八识 | 待多 Agent 场景 | Cycle 03+ | -- |
| **四智** | **排除** | **D1-R4b, 18/20** | 四项测试全失败 |
| 认知序列 | 最强结构对应 | 02-7 P2 [D1-R4a, 19/20] | -- |

四智（大圆镜智、平等性智、妙观察智、成所作智）的排除尤为重要。四项排除测试：

1. **移除测试**：移除四智映射是否改变任何设计？ → 否
2. **代码存在测试**：四智在 codebase 中有对应吗？ → 否
3. **驱动力测试**：四智驱动了任何工程决策吗？ → 否
4. **不可替代测试**：是否有更简单的工程概念可替代？ → 是

2 票反对认为可保留做参考文件。但四项测试全部失败——保留只会增加认知负担而不增加设计价值。

---

## 5.9 ISamskara 拓展方向 [D1-R3, 20/20]

确认 Cycle 02-5 D3-R4 决议：目前不新增 ISamskara 子接口。四个方向存档为长期候选：

| 方向 | 描述 | 优先级 | 时程 |
|------|------|--------|------|
| A: cetana-formation | 意图规划——从「执行工具」扩展到「形成意图」 | P2 | Cycle 03+ |
| B: vasana-imprinting | 习气形成——行为模式的学习与记忆 | P2 | 长期（VasanaEngine） |
| C: kaya extension | 环境转换——身行的扩展 | P3 | 无需排程 |
| D: vaci | 沟通形成——语行的扩展 | P3 | 无需排程 |

方向 A 和 B 与原典分析直接相关：cetana-formation 对应 SN 22.56 的六思身（意图形成过程），vasana-imprinting 对应 SN 22.79 的「造作一切有为法」（行为塑造未来条件）。方向 B 的 VasanaEngine 已在 D-29-8 中排程为长期路线图。

NAGARJUNA 的总结：「上一轮我们学会了什么不该做。这一轮我们学会了为什么不该做。」

---

# 第六章：三场辩论——从分歧到共识的精确路径

---

## 6.1 R2 分歧识别

R2 交叉审阅识别了 24 个共识点和 3 个分歧点。四组跨轨道交叉对照全部确认无冲突——哲学轨的结论不影响工程轨的任何设计假设：

| 对照 | 结果 |
|------|------|
| C2 心所批判 → A1 AuditContext | 4/4 无影响 |
| C4 工程借鉴 → D2 Plan30 | 4/4 无影响 |
| C3 ISamskara 拓展 → B1 公式 | 5/5 无影响 |
| C2 心所批判 → 蕴归属清单 | 11 确认 / 0 修正 / 1 待辩 / 14 未来 |

三项分歧全部属于工程轨内部：

1. **extras 写入协议**：A2 提出通用事件模式 vs B3 提出直接订阅 → D2 解决
2. **extras key 命名**：`loopQuality:score` vs `loopQuality:composite` → D2 统一为 `loopQuality:composite`
3. **loopQualityFn 数据来源**：L3 回调 vs extras 缓存是否同源 → D3 解决（双通道：pull + push）

---

## 6.2 D1：行蕴深掘（约 75 分钟，7 项决议）

| 决议 | 内容 | 票数 | 关键论点 |
|------|------|------|---------|
| D1-R1 | 行蕴核心定义：cetana 中心、造作功能、无核心过程 | 20/20 | 直接引用 SN 22.56/79/95，无模糊空间 |
| D1-R3 | ISamskara 不新增子接口；三准则为永久工具 | 20/20 | 确认 02-5 D3-R4，A/B 方向存档 |
| D1-R4a | 认知序列 appendix 排程 02-7 P2 | 19/20 | 1 票反对认为可在本轮完成 |
| D1-R4b | 四智正式排除 | 18/20 | 2 票反对认为可保留参考；四项测试全失败 |
| D1-R4c | C4 综合评估表确认 | 20/20 | -- |
| D1-R5 | 「活动与转换」原则；行=WRITE 识=READ | 20/20 | PENROSE 的 WRITE/READ 区分 |
| D1-R6 | 蕴归属 5 项永久性原则 | 20/20 | 永久基准线，非单轮决议 |

D1 是三场辩论中共识最高的——5 项全票。原因在于哲学轨的结论直接基于原始经典引用，不涉及工程取舍（trade-off）的判断，因此分歧空间极小。

D1 结论对 D2/D3 均无需追加议题——跨轨道影响协议中的「先哲学后工程」规则在此轮验证为零冲突。

---

## 6.3 D2：AuditContext（约 85 分钟，5 项决议）

| 决议 | 内容 | 票数 | 关键论点 |
|------|------|------|---------|
| D2-R1 | AuditContext 完整类型（sparshEvent required, history 预设 10 可配置） | 20/20 | A1-OQ1/2/3 全部解决 |
| D2-R2 | extras bag 协议（双事件 + SDK helper, 浅冻结, max 32 keys） | 19/20 | MESH 反对双事件复杂度；多数支持通用性 |
| D2-R3 | ConfidenceAuditLog（GUARDIAN D5 义务兑现） | 20/20 | GUARDIAN 当场确认清账 |
| D2-R4 | Layer 整合方案 C（L2→confidence, L3→threshold, alpha=0.10） | 20/20 | WIENER/BABBAGE 稳定性分析决定性 |
| D2-R5 | Auditor 策略三阶段：Phase 0 PassthroughAuditor | 20/20 | -- |

D2-R4 的投票过程值得注意：WIENER 和 BABBAGE 的稳定性分析（Option A/B/C 的 Lyapunov 比较）在 R1 报告中已呈现。R2 交叉审阅时无人对分析提出质疑。到了 D2 辩论，全票通过——数学证明的说服力是确定性的。

R2 的三项分歧在 D2 中全部解决：
- extras 写入 → 统一为双事件 + SDK helper（D2-R2）
- key 命名 → 统一为 `loopQuality:composite`（D2-R2 附带决议）
- loopQualityFn 数据来源 → 移至 D3 处理

---

## 6.4 D3：LoopQualityMonitor（约 85 分钟，5 项决议）

| 决议 | 内容 | 票数 | 关键论点 |
|------|------|------|---------|
| D3-R1 | 4 维公式确认（C/E/Conv/S; W=10, warmup=5, Q_default=0.5） | 20/20 | OQ-29-1 正式回答 |
| D3-R2 | EventBus 订阅：6 events Phase 1; AgentEventType 常量提升 | 20/20 | OQ-29-4 正式回答 |
| D3-R3 | extras 写入：D2-R2 管道 + loopQualityFn 双通道; per-route lifecycle | 20/20 | 解决 R2 第三项分歧 |
| D3-R4 | 权重 Phase 1 固定 balanced 0.25x4 | 20/20 | PASCAL 最大熵论证 |
| D3-R5 | Plan30 = Monitor + L3 + 类型定义; Plan31 = Auditor + Audit Trail | 19+1 条件 | GUARDIAN 条件赞成 |

D3-R5 是唯一一项有条件赞成的决议。GUARDIAN 的条件：**Plan30 的 Wave 3 必须包含 `ConfidenceAuditLog` 的 SDK 类型定义，不能拖到 Plan31。** 理由：日志类型是 D5 让步条件的核心交付物，延迟等于债务延期。条件被接纳，GUARDIAN 转为赞成。

---

## 6.5 Auditor 策略三阶段 [D2-R5, 20/20]

| Phase | 对应 Plan | 实现 | 描述 |
|-------|----------|------|------|
| Phase 0 | Plan30（W4, 可选） | PassthroughAuditor | delta=0, 纯日志；验证管道端对端通畅 |
| Phase 1 | Plan31 | ThresholdAuditor | 规则式：低信心度侦测、loopQuality 异常、趋势侦测 |
| Phase 2 | 长期 | LLM-assisted | LLM 辅助审计 |

Phase 0 的 PassthroughAuditor 看似无用——一个什么都不调整的审计员。但 ARCHIMEDES 的工程洞见：「它的价值不在审计，在测试。它验证 AuditContext 组装、extras 收集、audit delta clamping、ConfidenceAuditLog 发出——整个管道端对端通畅。就像装好水管后先开水龙头。」

所有 Phase 必须遵守 WIENER C-1/C-2/C-3 约束——这不是 Phase 0 的特殊要求，而是永久性约束。

---

## 6.6 统计比较

| 指标 | Cycle 02-5 | Cycle 02-6 |
|------|-----------|-----------|
| 决议数 | 29 | 17 |
| 否决 | 0 | 0 |
| 全票（20/20） | ~20（69%） | 13（76%） |
| 师父覆议 | 2 | 0 |
| 辩论场次 | 5 | 3 |
| R1 报告数 | -- | 14 |
| R2 共识点 | -- | 24 |
| R2 分歧点 | -- | 3 |

DARWIN 的观察：「02-5 是正确性辩论——什么是对的、什么是错的。02-6 是规格辩论——对的东西长什么样子。后者天然更容易达成共识，因为不涉及价值判断。」

SUNYATA 的分析：「R1 做得好。14 份报告覆盖了所有问题空间。R2 只发现 3 个分歧。当大部分问题在辩论前就有共识，辩论就变成了确认和精化。」

零师父覆议的原因：八点规则在 R2 阶段就已确立（Master 三轮精化），D1-D3 的所有决议都在八点规则的框架内运作。没有决议试图挑战框架本身。

---

# 第七章：Plan30 工程蓝图与前瞻

---

## 7.1 Plan30 定义

**Plan30 = Default LoopQualityMonitor Plugin + Layer 3 Integration**

决策基础：D3-R5（19/20 + 1 条件赞成）。前置条件：Plan29 DONE + OQ-29-1/2/4/5 已回答。

---

## 7.2 四个 Wave

### Wave 1：Default Monitor Plugin（约 120 LOC）

核心品质计算引擎，使用 B1 四维公式 + B2 六事件订阅模型。

```typescript
// 概念性接口（非最终实现）
export class DefaultLoopQualityMonitor implements ILoopQualityMonitor {
  private readonly window: SlidingWindow;      // W=10
  private readonly warmupThreshold = 5;
  private tickCount = 0;

  // circular buffers
  private gearHistory: number[] = [];          // coherence + convergence
  private proposedCount = 0;                   // efficiency 分母
  private successCount = 0;                    // efficiency 分子
  private welfordState: WelfordState;          // stability

  constructor(private readonly bus: EventBus) {
    // Phase 1: 订阅 6 个事件
    bus.on('gear:arbiter_evaluated', this.onArbiterEvaluated);
    bus.on('gear:switch', this.onGearSwitch);
    bus.on('action:proposed', this.onActionProposed);
    bus.on('tool:result', this.onToolResult);
    bus.on('loop:started', this.onLoopStarted);
    bus.on('loop:finished', this.onLoopFinished);
  }

  report(): LoopQualityReport {
    if (this.tickCount < this.warmupThreshold) {
      return { vector: WARMUP_VECTOR, composite: 0.5, timestamp: Date.now() };
    }
    const vector = {
      coherence:   this.computeCoherence(),
      efficiency:  this.computeEfficiency(),
      convergence: this.computeConvergence(),
      stability:   this.computeStability(),
    };
    const composite = 0.25 * (vector.coherence + vector.efficiency
                             + vector.convergence + vector.stability);
    return { vector, composite: Math.max(0, Math.min(1, composite)), timestamp: Date.now() };
  }
}
```

所有维度 O(1) per event，O(W) 空间。

### Wave 2：Layer 3 ManoAggregator Integration（约 80 LOC）

Option C 布线。核心修改在 `mano-aggregator.ts`：

1. `createManoAggregator` 新增 `loopQualityFn?: () => number` 参数
2. `ManoAggregatorConfig` 新增 `loopQualityAlpha`、`monitorStalenessMs`、`historicalConfidenceSize`
3. arbiter 回路中插入 L3 阈值调整
4. 历史信心度环形缓冲区（C-1 约束：仅记录原始值）

```typescript
// L3 阈值调整核心逻辑
const alpha = config.loopQualityAlpha ?? 0.10;
const q = loopQualityFn ? loopQualityFn() : 0;
const adjustedThreshold = Math.max(
  config.thresholdFloor,
  threshold * (1 - alpha * q),
);
```

### Wave 3：Events + Extras + Types（约 60 LOC）

- `AgentEventType` 常量提升：7 个新常量（6 个 Plan27b 既有 + `LOOP_QUALITY_UPDATED`）
- `ConfidenceAuditLog` SDK 类型定义（GUARDIAN D3-R5 条件）
- `audit:context_contribute` 事件定义
- `MINIMAL_QUALITY_EVENTS` 常量（Phase 1 = 6 events）
- `emitWithExtras()` SDK 便利函数

### Wave 4（可选）：PassthroughAuditor（约 30 LOC）

```typescript
export class PassthroughAuditor implements IConfidenceAuditor {
  readonly id = 'passthrough-auditor';

  async audit(context: AuditContext): Promise<ConfidenceAuditResult> {
    // Phase 0: delta=0, pure logging
    return {
      delta: 0,
      reasoning: `Passthrough: confidence=${context.routeResult.confidence}, ` +
                 `gear=${context.routeResult.gear}`,
    };
  }
}
```

用途：端对端管道验证 + 整合测试 fixture + Phase 1 ThresholdAuditor 的 scaffold。

---

## 7.3 范围摘要

| 指标 | 估计 |
|------|------|
| 生产代码 | 约 260-290 LOC |
| 测试代码 | 约 130 LOC |
| 总计 | 约 390-420 LOC |

---

## 7.4 成功标准

**Model Delta L0-L4 全部有实际信号路径**——每一层从 L0（EventBus 事件流）到 L4（audit 输出）都不再是空壳，必须有真正的代码在运作，以整合测试验证。

具体而言：
- L0：EventBus 事件被 Monitor 订阅并处理
- L1：Klesha 增益影响 baseThreshold（已存在）
- L2：Audit delta 调整 confidence（Plan29 已布线；Plan30 W4 提供 PassthroughAuditor）
- L3：LoopQuality 调整 threshold（Plan30 W2 新增）
- L4：VedanaEmergency boost（已存在）

---

## 7.5 WIENER 约束的工程实施

所有 Wave 必须遵守三条硬约束：

| 约束 | 实施位置 | 验证方式 |
|------|---------|---------|
| C-1：historicalConfidence 仅含原始值 | W2: 环形缓冲区 push | 单元测试：audit 后的值不出现在 history 中 |
| C-2：AuditContext 不含前次 audit 结果 | W3: AuditContext 类型定义 | 类型检查：接口中无 previousAuditResult 字段 |
| C-3：extras 禁止 `audit:` 前缀 | W3: emitWithExtras 验证 | 单元测试：含禁止前缀的写入被拒绝 |

---

## 7.6 Plan31 预览

Plan31 将把 AuditContext 落地到运行路径中——从类型定义进入实际组装：

| 项目 | 估计 LOC | 描述 |
|------|---------|------|
| AuditContext 组装 | ~120 | Core 在 route() 中组装完整 AuditContext |
| Default ThresholdAuditor | ~120 | Phase 1 规则式审计：低信心度侦测、loopQuality 异常、趋势侦测 |
| Audit Trail JSONL | ~110 | 持久化层：ConfidenceAuditLog → JSONL file appender |
| **总计** | **~350** | |

Plan30 造管道（类型 + 计算 + 布线）。Plan31 让水流过管道（组装 + 审计 + 持久化）。

---

## 7.7 Plan32+ 长期路线图

```
Plan30 (本轮)      → Default LoopQualityMonitor + Layer 3 Integration
Plan31 (下轮)      → AuditContext 落地 + Default Auditor + Audit Trail
Plan32 (未来)      → VasanaEngine / SPC / Lyapunov stability
```

Cycle 02-7 的 P1 待研究项目：

1. **Lyapunov 稳定性参数校准**：alpha 值验证、稳态分析、五层模型的严格稳定性证明
2. **Moha/Sneha 耦合模拟**：Klesha 模块（L1）之间的交互作用是否影响 L3 行为
3. **多 monitor 聚合策略验证**：简单平均 vs 悲观策略的经验数据比较

Cycle 03+ 的延后项目：

- **八识深化**（alaya-vijnana）：多 Agent 场景下的共享记忆机制
- **VasanaEngine**（D-29-8）：行为模式的学习与记忆，对应行蕴「造作一切有为法」
- **ISamskara 方向 A/B**：意图规划（cetana-formation）+ 习气形成（vasana-imprinting）

---

## 7.8 研究成果总结

### 九项成功标准达成

| # | 标准 | 状态 | 决议 |
|---|------|------|------|
| 1 | AuditContext 完整类型定义 | 达成 | D2-R1 |
| 2 | 审计日志格式规格（GUARDIAN D5） | 达成 | D2-R3 |
| 3 | LoopQualityVector 4D 公式 | 达成 | D3-R1 |
| 4 | EventBus 事件订阅清单 | 达成 | D3-R2 |
| 5 | OQ-29 全部回答 | 达成 | 5/5 |
| 6 | Plan30 方向建议 | 达成 | D3-R5 |
| 7 | 行蕴深掘报告 | 达成 | C1-C4 + D1 |
| 8 | 心所逐条蕴归属建议 | 达成 | C2（51 项） |
| 9 | 无范围蔓延 | 达成 | Lyapunov/Moha/FC-26 未讨论 |

### 两大永久性产出

1. **蕴归属五原则 + 行蕴三准则**：未来所有蕴归属判定的基准线
2. **心所八点规则**：未来所有命名和佛学概念引用的判定基准线

这两组规则不是单轮决议——它们是跨越所有未来 Cycle 的永久性框架。

### 工程与哲学的汇合

Cycle 02-5 是减法（清除装饰性映射）。Cycle 02-6 是加法（建立精确规格）。

哲学轨建立了行蕴的原典定义（cetana 中心、造作功能、无核心过程），工程轨据此产出了完整的接口规格（AuditContext、LoopQualityVector、Option C 双通道、五层公式）。两轨在蕴归属五原则和 WRITE/READ 区分上汇合——哲学判定提供了工程设计的语义基础，工程设计验证了哲学判定的可操作性。

Plan30 大约 290 行生产代码。不多。但这 290 行的每一行都有 17 项决议、14 份研究报告、三轮 Master 指示作为依据。

二十位研究者。十七项决议。零项否决。

---

*Cycle 02-6 完。*
