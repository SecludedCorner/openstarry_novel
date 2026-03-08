# Chapter Three: The Four-Dimensional Quality Vector and Observer Design

---

## 3.1 Mapping from Design Spec to SDK Dimensions

Plan29's SDK interface already defined field names for the four-dimensional vector, but left the computation formulas empty. The mapping between Doc 43 design spec and SDK implementation is:

| Doc 43 Design Spec | SDK Field Name | Semantics | Formula Symbol |
|--------------------|---------------|-----------|---------------|
| Continuity | `coherence` | Logical consistency of routing decisions | C |
| Granularity | `efficiency` | Resource utilization efficiency of tool execution | E |
| Speed | `convergence` | Goal convergence | Conv |
| Equanimity | `stability` | Oscillation stability of confidence | S |

---

## 3.2 Common Parameters

| Symbol | Definition | Default | Source |
|--------|-----------|---------|--------|
| W | Sliding window size | 10 ticks | Design choice: balancing sensitivity and stability |
| W_warmup | Warm-up period | 5 ticks | Minimum statistical significance |
| Q_default | Warm-up composite score | 0.5 | Neutral default (does not trigger L3 adjustment) |

Warm-up rule: If `tickCount < W_warmup`, all dimensions return 0.5, composite = 0.5. Data during warm-up still enters the sliding window but no quality reports are emitted externally.

---

## 3.3 coherence (C): Routing Consistency

**Semantics**: Measures the consistency of cognitive loop routing decisions. Rapid gear oscillation (1->2->1->2) indicates system indecision.

**Formula**:

$$C = 1 - \frac{\text{gearSwitchCount}}{W - 1}$$

Where `gearSwitchCount` = number of gear value changes within window W, and `W-1` = worst case (a switch every tick).

**Input event**: `gear:switch` (`payload.gear`)

**Implementation**: Maintain a circular buffer of length W recording the most recent W gear values. On each new event, O(1) update -- increment the new adjacent-difference count, remove the old one.

**Edge cases**:

| Scenario | Behavior | Rationale |
|----------|----------|-----------|
| No `gear:switch` events | C = 1.0 | No oscillation = perfect consistency |
| Window has fewer than W entries | denominator = max(actualCount - 1, 1) | Avoid division by zero |
| W = 1 | C = 1.0 | A single tick cannot oscillate |

---

## 3.4 efficiency (E): Tool Execution Efficiency

**Semantics**: The ratio of successfully executed tool calls to proposed tool calls.

**Formula**:

$$E = \begin{cases} \frac{\text{successfulExec}}{\text{totalProposed}} & \text{if } \text{totalProposed} > 0 \\ 1.0 & \text{otherwise (pure dialogue loop)} \end{cases}$$

**Input events**:

| Event | Purpose | Notes |
|-------|---------|-------|
| `action:proposed` | Denominator | Each tool call proposal |
| `tool:result` | Numerator | Successful execution |
| `tool:error` | Implicit (Phase 2) | Not counted in numerator |
| `tool:blocked` | Implicit (Phase 2) | Not counted in numerator |

**Design choice**: Pure dialogue loops (no tool calls) are defined as E = 1.0 -- no penalty for tool-free scenarios. This is because the efficiency dimension measures "whether proposed actions succeeded," and not proposing actions is not the same as low efficiency.

---

## 3.5 convergence (Conv): Goal Convergence

**Semantics**: Whether the system's routing decisions consistently push in the same direction. The longer the system consecutively selects the same gear, the more convergent the loop.

**Formula**:

$$\text{Conv} = \frac{\text{longestConsistentStreak}}{W}$$

**Phase 2 alternative (ATHENA's proposal)**: Exponential Moving Average (EMA)

$$\text{consistency}_t = \begin{cases} 1.0 & \text{if } \text{gear}_t = \text{gear}_{t-1} \\ 0.0 & \text{otherwise} \end{cases}$$

$$\text{EMA}_t = \alpha \cdot \text{consistency}_t + (1 - \alpha) \cdot \text{EMA}_{t-1}, \quad \alpha = \frac{2}{W + 1}$$

Phase 1 uses the streak method (simple, interpretable); Phase 2 will evaluate whether to switch to EMA once operational data is available.

**Input event**: `gear:switch`. Note that convergence and coherence use the same source but differ in computation: coherence measures switching frequency, while convergence measures the longest consistent run.

---

## 3.6 stability (S): Confidence Stability

**Semantics**: The degree of fluctuation in arbiter confidence. Based on inverse variance mapping.

**Formula**:

$$S = 1 - \min\left(1, \frac{\sigma^2}{0.25}\right)$$

Where $\sigma^2$ is the (population) variance of confidence values within window W, and 0.25 is a conservative upper bound (variance of a binary distribution {0,1} = 0.25; variance of a [0,1] uniform distribution $\approx 0.083$).

**Welford's Online Algorithm**:

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

The sliding-window version maintains a circular buffer + incremental updates, still O(1) per event.

**Input event**: `gear:arbiter_evaluated` (`payload.confidence`)

**Edge cases**:

| Scenario | S Value | Rationale |
|----------|---------|-----------|
| No arbiter events | 1.0 | No fluctuation = perfect stability |
| All confidence values identical | 1.0 | Variance = 0 |
| Confidence alternating between 0 and 1 | 0.0 | Maximum instability |

---

## 3.7 Composite Score and Weights

**Formula** [D3-R4, 20/20]:

$$Q = w_C \cdot C + w_E \cdot E + w_{\text{Conv}} \cdot \text{Conv} + w_S \cdot S$$

Phase 1 weights are all fixed at 0.25 (equal weighting). PASCAL's maximum entropy argument: absent empirical data supporting any dimension as more important, the Maximum Entropy Principle dictates assigning equal weight to each possibility -- this is not laziness but the optimal strategy under zero information.

Phase 2 weights are configurable, stored in the monitor plugin config (not `ManoAggregatorConfig` -- the calculator owns its parameters). Three presets:

| Preset | coherence | efficiency | convergence | stability |
|--------|-----------|-----------|-------------|-----------|
| balanced | 0.25 | 0.25 | 0.25 | 0.25 |
| stability-focused | 0.15 | 0.20 | 0.15 | 0.50 |
| efficiency-focused | 0.15 | 0.50 | 0.20 | 0.15 |

Validation constraint: $\sum w_i = 1.0$, each $w_i \in [0, 1]$.

**Range guarantee**: Each dimension $d_i \in [0, 1]$, weights $w_i \in [0, 1]$, $\sum w_i = 1.0$, therefore $Q \in [0, 1]$. This boundedness is critical for L3 integration's BIBO stability.

---

## 3.8 Observer Properties: A Control Theory Perspective

WIENER particularly emphasized the **pure observation function** nature of the four-dimensional formulas -- this is the definition of an observer in control theory:

- **Input**: System event stream (uncontrollable, read-only)
- **State**: Internal sliding window (does not affect the observed system)
- **Output**: LoopQualityVector (read-only report, no write-back)

The Monitor's skandha attribution = [vedana, samjna, vijnana], **excluding samskara**. All four formulas are observational computations that never modify events on the EventBus, never call any plugin, and never trigger any action. This ensures the observer does not interfere with the observed system -- the principle of "non-invasive observation" in control theory.

**Lyapunov stability look-ahead**: The variance time series from the stability dimension (S) provides foundational data for Cycle 02-7's Lyapunov stability analysis. If $\sigma^2$ consistently decreases, it meets the prerequisite for Lyapunov function monotonic decrease.

---

## 3.9 EventBus Event Subscriptions [D3-R2, 20/20]

**Phase 1 (MINIMAL_QUALITY_EVENTS = 6)**:

1. `gear:arbiter_evaluated` -> stability (confidence value)
2. `gear:switch` -> coherence + convergence (gear value)
3. `action:proposed` -> efficiency denominator
4. `tool:result` -> efficiency numerator
5. `loop:started` -> tick counting, window reset
6. `loop:finished` -> triggers quality report emission

**Phase 2 (+5 EXTENDED_QUALITY_EVENTS)**:

7. `sparsha:contact` -> input frequency analysis
8. `tool:error` -> refined efficiency calculation
9. `tool:blocked` -> security block frequency
10. `vitakka:stall` -> cognitive stall detection
11. `action:executed` -> execution latency analysis

**Degradation principle** (HERACLITUS): Missing event -> safe default value, no error. Missing efficiency -> 1.0 (assume normal), missing stability -> 0.5 (neutral). "Absence is information, not error."

**Plan30 action item**: Event strings scattered throughout the code in Plan27b must be promoted to `AgentEventType` constants -- 7 new constants (6 existing + `LOOP_QUALITY_UPDATED`).

---

## 3.10 Computational Complexity Summary

| Dimension | Per Event | Per Report | Space |
|-----------|----------|------------|-------|
| coherence | O(1) | O(1) | O(W) circular buffer |
| efficiency | O(1) | O(1) | O(1) two counters |
| convergence | O(1) | O(1) | O(W) circular buffer |
| stability | O(1) | O(1) | O(W) circular buffer + Welford state |
| **composite** | -- | O(1) | -- |

**Overall**: O(1) per event, O(1) per report, O(W) space. With W=10, memory overhead is negligible.
