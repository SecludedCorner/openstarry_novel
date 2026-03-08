# Chapter Seven: Plan30 Engineering Blueprint and Forward Look

---

## 7.1 Plan30 Definition

**Plan30 = Default LoopQualityMonitor Plugin + Layer 3 Integration**

Decision basis: D3-R5 (19/20 + 1 conditional approval). Preconditions: Plan29 DONE + OQ-29-1/2/4/5 answered.

---

## 7.2 Four Waves

### Wave 1: Default Monitor Plugin (approx. 120 LOC)

Core quality computation engine, using B1 four-dimensional formulas + B2 six-event subscription model.

```typescript
// Conceptual interface (not final implementation)
export class DefaultLoopQualityMonitor implements ILoopQualityMonitor {
  private readonly window: SlidingWindow;      // W=10
  private readonly warmupThreshold = 5;
  private tickCount = 0;

  // circular buffers
  private gearHistory: number[] = [];          // coherence + convergence
  private proposedCount = 0;                   // efficiency denominator
  private successCount = 0;                    // efficiency numerator
  private welfordState: WelfordState;          // stability

  constructor(private readonly bus: EventBus) {
    // Phase 1: subscribe to 6 events
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

All dimensions O(1) per event, O(W) space.

### Wave 2: Layer 3 ManoAggregator Integration (approx. 80 LOC)

Option C wiring. Core modifications in `mano-aggregator.ts`:

1. `createManoAggregator` adds `loopQualityFn?: () => number` parameter
2. `ManoAggregatorConfig` adds `loopQualityAlpha`, `monitorStalenessMs`, `historicalConfidenceSize`
3. L3 threshold adjustment inserted in the arbiter loop
4. Historical confidence circular buffer (C-1 constraint: records only raw values)

```typescript
// L3 threshold adjustment core logic
const alpha = config.loopQualityAlpha ?? 0.10;
const q = loopQualityFn ? loopQualityFn() : 0;
const adjustedThreshold = Math.max(
  config.thresholdFloor,
  threshold * (1 - alpha * q),
);
```

### Wave 3: Events + Extras + Types (approx. 60 LOC)

- `AgentEventType` constant promotion: 7 new constants (6 existing from Plan27b + `LOOP_QUALITY_UPDATED`)
- `ConfidenceAuditLog` SDK type definition (GUARDIAN's D3-R5 condition)
- `audit:context_contribute` event definition
- `MINIMAL_QUALITY_EVENTS` constant (Phase 1 = 6 events)
- `emitWithExtras()` SDK convenience function

### Wave 4 (optional): PassthroughAuditor (approx. 30 LOC)

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

Purpose: End-to-end pipeline verification + integration test fixture + scaffold for Phase 1 ThresholdAuditor.

---

## 7.3 Scope Summary

| Metric | Estimate |
|--------|---------|
| Production code | approx. 260-290 LOC |
| Test code | approx. 130 LOC |
| Total | approx. 390-420 LOC |

---

## 7.4 Success Criteria

**Model Delta L0-L4 all have actual signal paths** -- every layer from L0 (EventBus event stream) through L4 (audit output) must no longer be an empty shell; there must be real code running, verified by integration tests.

Specifically:
- L0: EventBus events are subscribed to and processed by the Monitor
- L1: Klesha gain affects baseThreshold (already exists)
- L2: Audit delta adjusts confidence (wired in Plan29; Plan30 W4 provides PassthroughAuditor)
- L3: LoopQuality adjusts threshold (new in Plan30 W2)
- L4: VedanaEmergency boost (already exists)

---

## 7.5 Engineering Implementation of WIENER Constraints

All Waves must comply with the three hard constraints:

| Constraint | Implementation Location | Verification Method |
|-----------|------------------------|-------------------|
| C-1: historicalConfidence contains only raw values | W2: circular buffer push | Unit test: post-audit values do not appear in history |
| C-2: AuditContext contains no previous audit results | W3: AuditContext type definition | Type checking: no previousAuditResult field in the interface |
| C-3: extras prohibits `audit:` prefix | W3: emitWithExtras validation | Unit test: writes with forbidden prefixes are rejected |

---

## 7.6 Plan31 Preview

Plan31 will bring AuditContext from type definitions into the live execution path -- from type definition to actual assembly:

| Item | Estimated LOC | Description |
|------|-------------|-------------|
| AuditContext assembly | ~120 | Core assembles complete AuditContext within route() |
| Default ThresholdAuditor | ~120 | Phase 1 rule-based audit: low confidence detection, loopQuality anomaly, trend detection |
| Audit Trail JSONL | ~110 | Persistence layer: ConfidenceAuditLog -> JSONL file appender |
| **Total** | **~350** | |

Plan30 builds the pipeline (types + computation + wiring). Plan31 lets water flow through the pipeline (assembly + auditing + persistence).

---

## 7.7 Plan32+ Long-Term Roadmap

```
Plan30 (this round)    -> Default LoopQualityMonitor + Layer 3 Integration
Plan31 (next round)    -> AuditContext landing + Default Auditor + Audit Trail
Plan32 (future)        -> VasanaEngine / SPC / Lyapunov stability
```

Cycle 02-7 P1 research items:

1. **Lyapunov stability parameter calibration**: alpha value verification, steady-state analysis, rigorous stability proof for the five-layer model
2. **Moha/Sneha coupling simulation**: Whether interaction between Klesha modules (L1) affects L3 behavior
3. **Multi-monitor aggregation strategy validation**: Empirical data comparison of simple averaging vs. pessimistic strategy

Cycle 03+ deferred items:

- **Eight consciousnesses deepening** (alaya-vijnana): Shared memory mechanisms in multi-Agent scenarios
- **VasanaEngine** (D-29-8): Learning and memory of behavioral patterns, corresponding to formations' "constructing all conditioned phenomena"
- **ISamskara Directions A/B**: Intention planning (cetana-formation) + habit formation (vasana-imprinting)

---

## 7.8 Research Outcomes Summary

### Nine Success Criteria Achieved

| # | Criterion | Status | Resolution |
|---|----------|--------|-----------|
| 1 | Complete AuditContext type definition | Achieved | D2-R1 |
| 2 | Audit log format specification (GUARDIAN D5) | Achieved | D2-R3 |
| 3 | LoopQualityVector 4D formulas | Achieved | D3-R1 |
| 4 | EventBus event subscription list | Achieved | D3-R2 |
| 5 | All OQ-29 answered | Achieved | 5/5 |
| 6 | Plan30 direction recommendation | Achieved | D3-R5 |
| 7 | Formations deep investigation report | Achieved | C1-C4 + D1 |
| 8 | Cetasika item-by-item skandha-attribution recommendations | Achieved | C2 (51 items) |
| 9 | No scope creep | Achieved | Lyapunov/Moha/FC-26 not discussed |

### Two Major Permanent Outputs

1. **Five skandha-attribution principles + three formations criteria**: The baseline for all future skandha-attribution determinations
2. **Eight cetasika rules**: The baseline for all future naming and Buddhist concept reference decisions

These two sets of rules are not single-round resolutions -- they are permanent frameworks spanning all future Cycles.

### Convergence of Engineering and Philosophy

Cycle 02-5 was subtraction (removing decorative mappings). Cycle 02-6 was addition (establishing precise specifications).

The philosophical track established the canonical definition of formations (cetana-centered, constructive function, coreless process); the engineering track produced complete interface specifications accordingly (AuditContext, LoopQualityVector, Option C dual-channel, five-layer formula). The two tracks converged on the five skandha-attribution principles and the WRITE/READ distinction -- philosophical determinations provided the semantic foundation for engineering design, and engineering design validated the operational viability of philosophical determinations.

Plan30 amounts to roughly 290 lines of production code. Not many. But every one of those 290 lines is backed by 17 resolutions, 14 research reports, and three rounds of Master directives.

Twenty researchers. Seventeen resolutions. Zero vetoes.

---

*Cycle 02-6 complete.*
