# Chapter 3: The Four-Dimensional Quality Vector -- A Quantitative Assessment Framework for the Cognitive Loop

---

## 3.1 Problem Definition

OpenStarry's AI Agent operates within a cognitive loop: sparsha -> vedana -> samjna -> samskara -> manas/vijnana -> next-cycle input. `ILoopQualityMonitor` must provide real-time quantitative assessment of this loop's operational quality. Quality is a multidimensional concept; a single metric is insufficient. WIENER (#12) and ATHENA (#5) designed the four-dimensional quality vector (LoopQualityVector), confirmed by Resolution D3-R1 (20/20).

---

## 3.2 The Four-Dimensional Formulas

Let the sliding window size be $W = 10$ and the warm-up period be $W_{warmup} = 5$.

### 3.2.1 Coherence

$$\text{coherence} = 1 - \frac{\text{switchCount}}{W - 1}$$

Measures routing decision stability. A high value indicates that the Agent continues operating in the same processing mode; a low value indicates frequent switching. Input event: `gear:switch`.

### 3.2.2 Efficiency

$$\text{efficiency} = \frac{\text{success}}{\text{proposed}} \quad (\text{if proposed} = 0, \text{then} = 1.0)$$

Measures tool invocation success rate. Degenerate handling: defaults to 1.0 when no proposed events exist. Input events: `action:proposed`, `tool:result`.

### 3.2.3 Convergence

$$\text{convergence} = \frac{\text{longestStreak}}{W}$$

Measures whether the Agent is approaching a stable state. The distinction from efficiency: efficiency measures "aggregate volume," while convergence measures "trend" -- 8 successes concentrated in the last 8 iterations (convergence 0.8) versus scattered throughout the window (possibly only 0.3) carry different meanings. Input event: `gear:switch`.

### 3.2.4 Stability

$$\text{stability} = 1 - \min\left(1, \frac{\sigma^2}{0.25}\right)$$

Measures the variance of the arbiter's confidence output. The denominator 0.25 serves as a lenient normalization baseline. Input event: `gear:arbiter_evaluated`.

---

## 3.3 Composite Quality Score and Weights

$$Q = \sum_{i=1}^{4} w_i \cdot d_i, \quad Q \in [0, 1]$$

Phase 1 uses equal weights $w_i = 0.25$. The theoretical justification is PASCAL's (#19) maximum entropy argument: in the absence of prior knowledge, the principle of maximum entropy (Jaynes 1957) requires uniform weight distribution. Resolution D3-R4 (20/20) confirmed Phase 1 fixed equal weights and Phase 2 configurable weights (three presets: balanced / stability-focused / efficiency-focused).

---

## 3.4 Sliding Window and Computational Complexity

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| $W$ | 10 | Balance between sensitivity and robustness |
| $W_{warmup}$ | 5 | Warm-up period to avoid small-sample bias |
| $Q_{default}$ | 0.5 | Neutral default value during warm-up |

All computations are $O(1)$ per event with $O(W)$ space, ensuring that quality monitoring does not become a performance bottleneck.

---

## 3.5 EventBus Event Subscriptions [D3-R2, 20/20]

**Phase 1 (6 events)**: `gear:arbiter_evaluated` (stability), `gear:switch` (coherence + convergence), `action:proposed` (efficiency), `tool:result` (efficiency), `loop:started` (window management), `loop:finished` (window management).

**Phase 2 (+5 events)**: `sparsha:contact`, `tool:error`, `tool:blocked`, `vitakka:stall`, `action:executed`.

**Degradation principle** (HERACLITUS #15): "Absence is information, not error." Missing events use safe default values (efficiency 1.0, stability 0.5) and do not throw exceptions. Concurrently, event string literals scattered throughout the codebase are promoted to `AgentEventType` constants.

---
