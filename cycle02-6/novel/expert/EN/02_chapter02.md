# Chapter Two: AuditContext and Feedback Loop Protection

---

## 2.1 The Problem: An Auditor Starved of Information

In v0.29.0-alpha, the signature for `IConfidenceAuditor.audit()` was:

```typescript
// v0.29.0-alpha status quo
audit(routeResult: RouteResult): ConfidenceAuditResult | Promise<ConfidenceAuditResult>;
```

Where `RouteResult` contained only `{ gear, decidedBy, confidence, riskAdjusted, riskCategory }`. An effective auditor needs far more context: What was the triggering event? What was the arbiter's full reasoning process? What are the recent confidence trends? What auxiliary data have other plugins observed?

DC Master ruled during R0 directives that Option B (generic Context Bag) was the sole correct direction, rejecting the rigidity of Option A (fixed-field extension).

---

## 2.2 Complete AuditContext Type Definition [D2-R1, 20/20]

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

  /** The SparshEvent that triggered this cognitive loop */
  readonly sparshEvent: SparshEvent;

  /** Full evaluation result from the winning arbiter (including confidence + reasoning) */
  readonly gearEvaluation: GearEvaluation;

  /** Current risk level (may be undefined = undeclared) */
  readonly riskCategory: RiskCategory | undefined;

  /** Route result (pre-audit snapshot) */
  readonly routeResult: RouteResult;

  /**
   * Recent historical confidence sequence (opt-in, circular buffer, default size=10 configurable).
   *
   * WIENER C-1 constraint: contains only raw arbiter confidence,
   * not post-audit corrected values.
   */
  readonly historicalConfidence?: readonly number[];

  /**
   * Plugin-contributed extra context data.
   * ManoAggregator collects plugin context contributions from EventBus,
   * placing them uniformly into this Map. Core is unaware of specific key/value semantics.
   * Frozen with Object.freeze() before passing to auditor.
   */
  readonly extras: ReadonlyMap<string, unknown>;
}
```

**Design decision summary**:

| Decision Point | Options | Final Choice | Rationale |
|---------------|---------|-------------|-----------|
| `sparshEvent` optional? | optional vs required | **required** | Every routing must have a triggering event; ManoAggregator obtains it via `sparshEventFn` callback |
| `historicalConfidence` buffer size | fixed 10 vs configurable | **default 10, configurable** | `ManoAggregatorConfig.historicalConfidenceSize` |
| `version` type | `number` vs literal `1` | **literal `1`** | Enforces compile-time type checking; future versions increment to `2` |
| `extras` type | `Record<string, unknown>` vs `ReadonlyMap` | **`ReadonlyMap`** | Map semantics are clearer, freeze is more intuitive |

**IConfidenceAuditor interface update**:

```typescript
export interface IConfidenceAuditor extends IVijnana {
  readonly id: string;
  audit(context: AuditContext): ConfidenceAuditResult | Promise<ConfidenceAuditResult>;
}
```

This is a breaking change (parameter changed from `RouteResult` to `AuditContext`), but TURING confirmed in the D1 code verification that v0.29.0-alpha **has no existing IConfidenceAuditor plugin implementations** -- this is the optimal refactoring window, with zero real-world impact.

---

## 2.3 WIENER Constraints: Systematic Severing of Feedback Loops

WIENER demonstrated in Cycle 02-4 D5 that if historical audit deltas feed back into the current audit input, a positive feedback loop can emerge:

```
Loop N:   auditor outputs delta = +0.03
Loop N+1: auditor sees previous delta = +0.03, leans positive -> delta = +0.04
Loop N+2: continued positive accumulation -> system drift
```

Formal statement: Let $c_n$ be the raw arbiter confidence at loop $n$, and $\delta_n$ be the audit delta.

- **Permitted input**: $\delta_n = f(c_n, c_{n-1}, \ldots, c_{n-k}, \text{extras}_n)$ -- observation function
- **Prohibited input**: $\delta_n = g(\delta_{n-1}, \delta_{n-2}, \ldots)$ -- autoregressive function

The former's stability depends on the observed system (exogenous); the latter can diverge independently (endogenous). This is the fundamental distinction in control theory between an observer and an autoregressive system.

Based on this, three hard constraints were designed (WIENER Constraints C-1/C-2/C-3):

**C-1**: `historicalConfidence` contains only raw arbiter confidence (`GearEvaluation.confidence`), never post-audit corrected values (`auditedConfidence`).

```typescript
// Inside ManoAggregator -- record after each arbiter wins
confidenceHistory.push(evaluation.confidence);  // raw value
// NOT confidenceHistory.push(auditedConfidence);  // prohibited
```

**C-2**: AuditContext contains no `previousAuditResult`, `previousDelta`, or `auditHistory` fields whatsoever. The auditor cannot read its own prior output from AuditContext.

**C-3**: The extras bag prohibits three prefixes: `audit:`, `core:`, `internal:`. This prevents the auditor from circumventing C-2 through the extras bag.

```typescript
// extras write validation
const FORBIDDEN_PREFIXES = ['audit:', 'core:', 'internal:'] as const;

function validateExtrasKey(key: string): boolean {
  return !FORBIDDEN_PREFIXES.some(prefix => key.startsWith(prefix));
}
```

BABBAGE's BIBO stability verification: Under constraints C-1/C-2/C-3, the input set for audit delta $\delta_n$ consists entirely of exogenous variables (the raw arbiter confidence sequence + plugin extras), containing no historical self-output. Therefore, with $|\delta_n| \le 0.05$ (hard clamp), the system satisfies bounded-input bounded-output (BIBO stability).

---

## 2.4 Extras Bag Protocol [D2-R2, 19/20]

The extras bag design produced the only cross-track divergence during R2: A2 (DARWIN + MESH) proposed a generic event pattern, while B3 (LEIBNIZ + MESH) favored direct subscription. The D2 debate unified them into **dual-event + SDK convenience functions**:

| Aspect | Resolution |
|--------|-----------|
| Write pattern | Plugins use SDK `emitWithExtras(key, value)` convenience function |
| Collection pipeline | ManoAggregator subscribes to `audit:context_contribute` events |
| Reading | `getExtra<T>(extras, key, guard)` type-safe accessor |
| Immutability | Shallow freeze (`Object.freeze`) + `ReadonlyMap` |
| Capacity limit | Maximum 32 keys, 128 chars per key |
| Forbidden prefixes | `audit:`, `core:`, `internal:` |
| Key naming convention | `{category}:{name}` -- e.g., `loopQuality:vector`, `loopQuality:composite` |
| Lifecycle | Per-routing-cycle (cleared at end of each routing, not persisted) |

1 dissenting vote (MESH) argued the dual-event pattern introduced unnecessary complexity. However, the majority judged the return on investment of a generic pipeline to be higher: it serves not only LoopQualityMonitor but enables any future plugin to contribute data to AuditContext through the same pipeline.

---

## 2.5 ConfidenceAuditLog -- Settling GUARDIAN's D5 Debt [D2-R3, 20/20]

GUARDIAN made a key concession in Cycle 02-5 D5: agreeing to the audit delta clamp of +-0.05, on the condition that the next round must define a complete audit log format. This was a security debt.

Cycle 02-6 delivered the `ConfidenceAuditLog` type:

```typescript
export interface ConfidenceAuditLog {
  readonly timestamp: number;
  readonly auditorId: string;
  readonly inputConfidence: number;    // pre-audit confidence
  readonly rawDelta: number;           // auditor's suggested delta
  readonly clampedDelta: number;       // delta after clamping
  readonly wasClamped: boolean;        // whether clamping occurred
  readonly reasoning: string;          // truncated to 500 chars, Core's responsibility
  readonly outputConfidence: number;   // post-audit confidence
  readonly result: 'applied' | 'timeout' | 'error';
  readonly auditDurationMs: number;
}
```

Propagation channels:
- **Primary channel**: EventBus `audit:completed` event, observable in real time
- **Persistence**: JSONL file appender (optional, post-Plan30)
- **PII sanitization**: PII scrubbing in the reasoning field is the plugin's responsibility; Core only truncates

GUARDIAN confirmed on the spot during the D2 debate: "The D5 account is settled. I no longer reserve the right to reopen the +-0.05 clamp." This was an important security milestone -- since Cycle 02-4, GUARDIAN had continuously challenged the safety of confidence adjustments, attaching conditions to every concession. Complete logging + three feedback loop protections + +-0.05 hard clamp -- this triple safeguard finally satisfied his security requirements.

---

## 2.6 Version Control Strategy

`AuditContext.version` uses the literal type `1` (not `number`), ensuring compile-time type checking. When extended in the future, it increments to `2`. Auditor plugins should fail-safe on unrecognized versions:

```typescript
function audit(ctx: AuditContext): ConfidenceAuditResult {
  if (ctx.version > 1) {
    return { delta: 0, reasoning: 'Unknown AuditContext version' };
  }
  // normal audit logic...
}
```

This fail-safe pattern guarantees forward compatibility: when a newer Core is paired with an older Auditor plugin, the auditor will not crash on unrecognized fields but instead degrades to passthrough (delta=0).
