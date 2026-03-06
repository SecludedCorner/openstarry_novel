# Chapter 6: Pure Engineering -- D5 Plan29 Engineering Specification Debate

---

**Duration**: ~75 minutes | **Participants**: 10 | **Votes**: 9 items

D5 was the first debate in the project's history with absolutely no Buddhist content. Ten engineers and scientists, zero Buddhist scholars (NAGARJUNA and ASANGA voluntarily recused), discussing the precise specifications of TypeScript interfaces.

TURING pre-submitted a complete v0.28.0-alpha design pattern report -- 14 source code files, all Registry lifecycles, timeout patterns, synchronous/asynchronous patterns, and failure handling strategies. This "code archaeology" report provided the factual basis for all decisions.

## Nine Resolutions

| Resolution | Content | Votes |
|------------|---------|-------|
| D5-R1 | Dedicated `auditor` hook slot (no reuse of monitors) | 8/8 |
| D5-R2 | audit() dual-mode return `T \| Promise<T>` | **5/8** |
| D5-R3 | Timeout 200ms, fail-safe delta=0, configurable | 8/8 |
| D5-R4 | Single auditor, last-wins (not array) | 6/8 |
| D5-R5 | Failure handling: delta=0 + warning log | consensus |
| D5-R6 | MonitorRegistry starts in ExecutionLoop.onLoopStart() | 7/8 |
| D5-R7 | LoopQualityVector equal weights 0.25x4 | 8/8 |
| D5-R8 | validatePluginSkandha() maintained as warning-only | 7/8 |
| D5-R9 | IConfidenceAuditor extends IVijnana, skandha ['vijnana'] | 8/8 |

**Most contentious vote**: D5-R2 (5/8) -- pure async vs dual-mode. GUARDIAN/KERNEL/VITRUVIUS argued that pure async semantics are more precise; the majority adopted dual-mode, following the IGearArbiter precedent and for testing convenience.

## IConfidenceAuditor Final Specification (100%)

```typescript
export interface IConfidenceAuditor extends IVijnana {
  readonly id: string;
  audit(confidence: number, context: GearContext):
    ConfidenceAuditResult | Promise<ConfidenceAuditResult>;
}
export interface ConfidenceAuditResult {
  delta: number;       // clamped to [-0.05, +0.05]
  reasoning: string;   // audit trail
}
```

PluginHooks final form:
```typescript
interface PluginHooks {
  // ... existing fields ...
  monitors?: ILoopQualityMonitor[];   // Plan29 Wave 1
  auditor?: IConfidenceAuditor;       // Plan29 Wave 2
}
```

NAGARJUNA's comment after D5 concluded: "D4 proved that names must take responsibility for definitions. D5 proved that some engineering problems need no definitions at all -- only specifications."

---
