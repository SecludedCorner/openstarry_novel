# Chapter 2: Type Design of the Audit Context -- Information Sufficiency and Feedback Loop Severance

---

## 2.1 Problem Analysis: The Information Poverty of IConfidenceAuditor

The `IConfidenceAuditor` interface delivered in Plan29 suffered from a structural deficiency: the audit function's input contained only `RouteResult` (the routing result). The auditor had no access to the triggering event (sparshEvent), the arbiter's reasoning process (gearEvaluation), the risk level (riskCategory), or historical confidence sequences. In decision-theoretic terms, this constitutes an information asymmetry problem. DC Master explicitly directed that the auditor requires more information.

However, expanding the information visible to the auditor simultaneously introduces a control-theoretic risk: a **positive feedback loop**.

---

## 2.2 Threat Model of the Positive Feedback Loop

WIENER (#12) identified three potential positive feedback paths:

1. **historicalConfidence contamination**: If the historical sequence includes post-audit adjusted values, forming a closed loop of `audit -> confidence -> history -> audit`
2. **Audit result leakage**: If AuditContext includes the previous ConfidenceAuditLog, forming confirmation-bias-driven serial correlation
3. **extras backdoor**: If the extras bag permits writing audit-related key-value pairs, indirectly leaking historical output

All three paths can lead to BIBO instability: confidence values monotonically increasing or oscillating divergently across iterations.

---

## 2.3 AuditContext Type Definition [D2-R1, 20/20]

```typescript
export interface AuditContext {
  readonly version: 1;                              // literal type
  readonly sparshEvent: SparshEvent;                // triggering event (required)
  readonly gearEvaluation: GearEvaluation;          // arbiter's full reasoning process
  readonly riskCategory: RiskCategory | undefined;  // risk category (optional)
  readonly routeResult: RouteResult;                // pre-audit routing result snapshot
  readonly historicalConfidence?: readonly number[]; // ring buffer, default size 10
  readonly extras: ReadonlyMap<string, unknown>;     // generic extension bag
}
```

Core fields are assembled by Core; historicalConfidence is an optional ring buffer; extras is a ReadonlyMap, accessed through the type-safe accessor `getExtra<T>(extras, key, guard)`.

---

## 2.4 The Three WIENER Constraints

**C-1 (Historical Purity)**: historicalConfidence records only the arbiter's raw confidence $c_t^{raw}$, excluding post-audit adjusted values.

**C-2 (Audit Result Isolation)**: AuditContext does not include the previous ConfidenceAuditLog. Each audit receives informationally independent inputs.

**C-3 (extras Prefix Ban)**: The prefixes `audit:`, `core:`, and `internal:` are prohibited, preventing audit results from leaking through extras.

The three constraints ensure the auditor's **causal isolation**. BABBAGE's (#9) formal verification: The audit function $f: \mathcal{C} \times \mathcal{A} \to [-0.05, +0.05]$, under the three constraints, receives inputs that do not contain its own prior output; the adjustment magnitude is bounded by the clamping constraint; the confidence range $[0,1]$ is naturally bounded; thus the system satisfies BIBO stability.

---

## 2.5 extras bag Protocol [D2-R2, 19/20]

| Aspect | Specification |
|--------|--------------|
| Write mode | Dual-event + SDK `emitWithExtras()` |
| Collection pipeline | ManoAggregator subscribes to `audit:context_contribute` |
| Read interface | `getExtra<T>(extras, key, guard)` |
| Immutability | Shallow freeze + ReadonlyMap |
| Limits | max 32 keys, 128 chars/key |
| Key naming | `{category}:{name}` format |

One dissenting vote argued that the dual-event pattern introduces unnecessary complexity; the majority held that its generality (any Plugin can contribute information through the same protocol) justified the design.

---

## 2.6 ConfidenceAuditLog [D2-R3, 20/20]

Complete audit trail type: inputConfidence, rawDelta, clampedDelta, wasClamped, reasoning (truncated to 500 characters), outputConfidence, result, auditDurationMs. The primary channel is the EventBus `audit:completed` event; JSONL persistence is scheduled for Plan31.

Following the passage of this resolution, GUARDIAN (#11) issued a formal declaration: "The concession conditions from D5 have been fulfilled. I no longer reserve the right to reopen deliberation on the $\pm 0.05$ clamping limit." This declaration concluded the ongoing dispute over confidence-adjustment safety that had persisted since Cycle 02-4.

---
