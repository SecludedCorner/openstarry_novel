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
