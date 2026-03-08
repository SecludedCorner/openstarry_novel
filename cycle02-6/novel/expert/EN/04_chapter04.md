# Chapter Four: Option C -- The Architectural Decision for Independent Channels

---

## 4.1 Problem Space: How Layer 3 Integrates

The original question from OQ-29-2:

> How does Layer 3 (Delta_loopQuality) integrate into the Model Delta five-layer model? Additive stacking, multiplicative scaling, or independent channels?

The five-layer model in v0.29.0-alpha:

| Layer | Name | Target | Implementation Status |
|-------|------|--------|----------------------|
| L0 | Safety Floor/Ceiling | Global clamp [0.30, 0.90] | Implemented in v0.28.0 |
| L1 | Klesha | baseThreshold += klesha gain | Implemented in v0.28.0 |
| L2 | Audit Delta | confidence += clamp(delta, +-0.05) | Implemented in v0.29.0 |
| L3 | LoopQuality | **TBD** | Not implemented |
| L4 | VedanaEmergency | threshold += boost [0, +0.15] | Implemented in v0.28.0 |

Layer 2 was already wired (audit delta added to confidence), while Layer 3 was completely blank. LoopQualityMonitor's SDK + Registry were in place, but its output (`LoopQualityVector`) was not connected to any routing logic.

---

## 4.2 Three-Option Comparison: Why Not A or B

### Option A: Additive Stacking

```
theta_final = clamp(theta_base + DeltaL1 + DeltaL2 + DeltaL3 + DeltaL4, 0.30, 0.90)
```

**Advantage**: Fully consistent with the existing model (all deltas summed), implementable in one line.

**WIENER's stability analysis**:

Let $V = (c - \theta)^2$ be the Lyapunov candidate function. Under Option A, $c_{\text{eff}} = c + \Delta_{L2} + \Delta_{L3}$, threshold unchanged.

$$\dot{V} = 2(c_{\text{eff}} - \theta)(\dot{\Delta}_{L2} + \dot{\Delta}_{L3})$$

If $\Delta_{L2}$ and $\Delta_{L3}$ share the same sign and are both increasing, $\dot{V} > 0$ (Lyapunov function increasing = instability trend). Co-directional accumulation in the worst case can reach +0.08 (0.05 + 0.03), exceeding the design intent of any single-layer clamp.

More dangerously, **cross-amplification**: the audit delta is based on arbiter confidence, and loopQuality also observes routing behavior. Both may react in the same direction to the same anomaly, forming indirect coupling.

**Conclusion**: Option A **cannot guarantee stability** under co-directional L2/L3 accumulation.

### Option B: Multiplicative Scaling

```
theta_adjusted = theta_after_L2 * (1 + loopQualityFactor)
```

Expanding: $c_{\text{eff}} = (c + \Delta_{L2}) \times (1 + f_{L3}) = c + \Delta_{L2} + c \cdot f_{L3} + \Delta_{L2} \cdot f_{L3}$

The cross-term $\Delta_{L2} \cdot f_{L3}$ constitutes direct coupling. Even if each channel is individually bounded, the cross-term can amplify overall displacement. Additionally, multiplication transforms the system from linear to nonlinear, drastically increasing the complexity of Lyapunov stability analysis. Boundary behavior is also poor: at low confidence (e.g., 0.35), the multiplicative adjustment is too small (0.035) to be meaningful.

**Conclusion**: Option B introduces **non-negligible cross-terms**, making stability analysis intractable.

### Option C: Independent Channels

```
L2: confidence_adjusted = confidence + clampAuditDelta(audit.delta)  [+-0.05]
L3: theta_adjusted = max(thresholdFloor, theta * (1 - alpha * q))    [alpha=0.10]
```

L2 adjusts **confidence**, L3 adjusts **threshold**. The two act on different variables, constituting two independent control channels.

---

## 4.3 Stability Proof for Option C

**Control system model**:

| Role | Element | Description |
|------|---------|-------------|
| Plant | Agent behavior | Gear selection -> action quality |
| Sensor | ILoopQualityMonitor | Observes behavioral quality |
| Controller | L3 threshold adjustment | Fine-tunes the pass threshold based on quality |
| Disturbance | IConfidenceAuditor | Corrects confidence estimates |

**Lyapunov analysis**:

Let $V = (c_{\text{eff}} - \theta_{\text{eff}})^2$

- Channel 1: $c_{\text{eff}} = c + \Delta_{L2}$, where $\Delta_{L2}$ depends only on arbiter output
- Channel 2: $\theta_{\text{eff}} = \theta \times (1 - \alpha \cdot q)$, where $q$ depends only on EventBus events

$$\dot{V} = 2(c_{\text{eff}} - \theta_{\text{eff}})(\dot{\Delta}_{L2} + \alpha \cdot \theta \cdot \dot{q})$$

Because $\Delta_{L2}$ does not depend on $q$, and $q$ does not depend on $\Delta_{L2}$, there are **no cross-terms**.

Each channel independently satisfies BIBO:

- $|\Delta_{L2}| \le 0.05$ (hard clamp)
- $\alpha \cdot q \in [0, 0.10]$ ($\alpha = 0.10$, $q \in [0, 1]$)

**BIBO Stability Theorem (informal)**: Under Option C, if L2 and L3 each independently satisfy BIBO stability, and L2 does not depend on L3 output nor L3 on L2 output, then the overall system is BIBO stable.

**Proof sketch**: L2 and L3 form parallel control channels. The stability of a parallel system is equivalent to the conjunction of each channel's independent stability (parallel interconnection theorem). Each channel has a hard clamp, therefore BIBO stable. L0 Safety Floor/Ceiling provides a global safety net.

**Rigorous Lyapunov proof deferred to Cycle 02-7** (P1 Lyapunov parameter calibration).

---

## 4.4 Semantic Symmetry

Option C's semantic distinction is exceptionally clear:

| Dimension | L2 (Audit) | L3 (LoopQuality) |
|-----------|-----------|-------------------|
| Target variable | confidence | threshold |
| Semantic question | "Is this arbiter's judgment reliable?" | "Is the current system state suitable for the fast path?" |
| Control theory analogy | State estimator correction | Setpoint adjustment |
| Direction | Adjusts the credibility of the "measurement" | Adjusts the strictness of the "pass gate" |
| Input source | AuditContext (arbiter result) | EventBus (monitor observations) |
| Numerical range | +-0.05 | alpha * q in [0, 0.10] |

WIENER's assessment: "This is the cleanest separation I have seen. The two channels each have a clear physical meaning and will not contaminate each other."

---

## 4.5 Alpha Parameter Selection

| alpha | Max adjustment at theta=0.6 | Assessment |
|-------|-----------------------------|------------|
| 0.05 | 0.57 (drop 0.03) | Ultra-conservative |
| **0.10** | **0.54 (drop 0.06)** | **Recommended default** |
| 0.15 | 0.51 (drop 0.09) | Aggressive |
| 0.20 | 0.48 (drop 0.12) | Excessive -- may breach thresholdFloor |

WIENER's rationale for alpha = 0.10:

1. Maximum adjustment of roughly +-6%, within human-perceptible range, facilitating debugging
2. Comparable in magnitude to L2's +-0.05 -- L3 will not drown out L2
3. Conservative starting point, adjustable based on simulation data

**Semantic interpretation of the L3 formula**:

| compositeLoopQuality | theta_adjusted (theta=0.6) | Meaning |
|---------------------|---------------------------|---------|
| 1.0 (best quality) | 0.54 (theta * 0.9) | System running stably -> slightly relax threshold -> easier fast path |
| 0.5 (medium quality) | 0.57 (theta * 0.95) | Moderate adjustment |
| 0.0 (worst / no observation) | 0.60 (theta * 1.0) | Conservative degradation -- threshold unchanged |

---

## 4.6 Dual-Channel Delivery of Quality Scores

The quality monitor's output has two consumers with different needs:

| Consumer | What It Needs | Channel |
|----------|--------------|---------|
| ManoAggregator (L3 threshold adjustment) | Real-time composite number | **pull**: `loopQualityFn()` callback |
| IConfidenceAuditor (rich background) | Four-dimensional vector + composite | **push**: extras bag via EventBus |

**Pull channel**: `loopQualityFn` injected into `createManoAggregator`, called synchronously within `route()` each time it is needed.

```typescript
export function createManoAggregator(
  bus: EventBus,
  config: ManoAggregatorConfig,
  baseThresholdFn?: () => number,
  vedanaFn?: () => ChannelVedana,
  vedanaEmergencyConfig?: VedanaEmergencyConfig,
  auditor?: IConfidenceAuditor,
  loopQualityFn?: () => number,  // new: returns compositeLoopQuality in [0, 1]
): ManoAggregator
```

**Push channel**: The Monitor uses SDK `emitWithExtras()` to simultaneously emit:
- `loopQuality:updated` event (subscribed by ManoAggregator, used for internal cache update of the pull callback)
- `audit:context_contribute` event (collected by ManoAggregator into the extras bag)

Keys in extras:
- `loopQuality:composite` -> composite score (number)
- `loopQuality:vector` -> four-dimensional vector object

LEIBNIZ's key constraint: "The quality score's lifecycle is per-routing-cycle. At the end of each routing, the extras bag is cleared. No accumulation, no persistence." A one-tick delay is acceptable -- quality is a historical indicator and does not require microsecond-level real-time resolution.

---

## 4.7 Boundary Condition Analysis

**No Monitor Plugin (G-0 degradation path)**: `loopQualityFn` returns `undefined` or `q_default = 0`, L3 has no effect: `theta_adjusted = theta` (multiplied by 1.0). System behavior is identical to when no ILoopQualityMonitor exists.

**Stale Monitor report**: Set `monitorStalenessMs = 5000` (configurable). If expired, treat as no observation -> q = 0. WIENER's rationale: a stale observation is equivalent to introducing a "phantom signal," consistent with the effective-duration concept in zero-order hold (ZOH).

**Multiple Monitor aggregation**: Phase 1 uses simple averaging (reduces the noise impact of individual monitors). BABBAGE's proposed pessimistic strategy (take the minimum) was rejected -- a single anomalous monitor should not disproportionately influence the overall result.

**compositeLoopQuality = 1.0 extreme value**: If `theta = thresholdFloor = 0.30`, then `theta_adjusted = 0.27 < thresholdFloor`. Fix: L3 adjustment must still obey L0:

```typescript
const adjustedThreshold = Math.max(
  config.thresholdFloor,
  threshold * (1 - loopQualityAlpha * compositeLoopQuality),
);
```

---

## 4.8 Complete Five-Layer Formula (Post-Option C Integration)

```
theta_base                                        // base threshold (config-injected)
  + L1: Sigma(w_k * K_k)                         // Klesha gain (baseThresholdFn)
  + L4: thresholdBoost                            // VedanaEmergency boost
  = theta_intermediate

theta_adjusted = max(thresholdFloor,
                     theta_intermediate * (1 - alpha * q))  // L3: LoopQuality
theta_final = min(thresholdCeiling, theta_adjusted)         // L0 ceiling

confidence_adjusted = confidence
                    + clampAuditDelta(audit.delta)          // L2: Audit

routing = (confidence_adjusted > theta_final)
        ? arbiter_gear
        : default_gear
```

**Layer execution order**: L4 (VedanaEmergency) -> L1 (Klesha) -> L3 (LoopQuality) -> comparison (with L2-adjusted confidence). L4 takes priority because it handles safety-critical emergency states.

**Worst-case L2/L3 interaction**: confidence increases by 0.05 and threshold decreases by 0.06 -> net effect approximately 0.11. Still within L0 safety bounds (`thresholdFloor` + `maxConfidenceByGear` jointly constrain).

---

## 4.9 ManoAggregator Code Integration Point

In `mano-aggregator.ts`, within the arbiter loop, insert L3 adjustment after the existing threshold calculation at L134-L138:

```typescript
// existing: L0 + L1 + risk adjustment
const threshold = evaluation.riskCategory
  ? computeAdjustedThreshold(
      effectiveBaseThreshold, evaluation.riskCategory,
      config.riskDelta, config.thresholdFloor, config.thresholdCeiling)
  : effectiveBaseThreshold;

// new: Layer 3 -- LoopQuality threshold adjustment
const loopQualityAlpha = config.loopQualityAlpha ?? 0.10;
const q = loopQualityFn ? loopQualityFn() : 0;
const adjustedThreshold = Math.max(
  config.thresholdFloor,
  threshold * (1 - loopQualityAlpha * q),
);

// modified: use adjustedThreshold
if (evaluation.confidence > adjustedThreshold) {
  // ... existing routing logic ...
}
```

New `ManoAggregatorConfig` fields:

```typescript
export interface ManoAggregatorConfig {
  // ... existing fields ...
  readonly loopQualityAlpha?: number;       // [0, 0.2], default: 0.10
  readonly monitorStalenessMs?: number;     // default: 5000
  readonly historicalConfidenceSize?: number; // default: 10
}
```

WIENER's closing statement: "Option C's stability guarantee rests on the assumption of two-channel independence. If a future design breaks this independence (e.g., letting the auditor read loopQuality and adjust its delta accordingly), the stability guarantee no longer holds. The auditor can see `loopQuality:composite` in the extras bag, but WIENER C-1/C-2/C-3 ensure that even seeing it does not create a positive feedback loop -- because the auditor's delta does not feed back into loopQuality's computation."
