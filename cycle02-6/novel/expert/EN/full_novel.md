# Prologue: From Debridement to Precision Engineering

---

Cycle 02-5 was a large-scale debridement surgery.

Twenty researchers produced 29 resolutions in five days. DC Master overturned two of them on review (D3-R3 Four Wisdoms mapping, D4-R1 cetasika naming). The entire team performed de-ornamentation refactoring across seven design documents -- removing Buddhist labels that carried no architectural driving force, unifying naming conventions, dismantling incorrect skandha-attribution mappings. Those five days were like dead code elimination on the codebase: not adding features, but removing accumulated semantic debt.

Cycle 02-6 strikes a fundamentally different tone. The previous round answered "what is wrong"; this round must answer "what does a correct specification look like."

---

## Dual Inputs

DC Master issued two letters, triggering the engineering track and the philosophical track respectively.

**The engineering letter** pointed to six Open Questions (OQ-29-1 through OQ-29-6) remaining after the Plan29 delivery. Plan29 (v0.29.0-alpha) introduced `ILoopQualityMonitor` (loop quality monitor interface) and `IConfidenceAuditor` (confidence auditor interface), but both were mere SDK skeletons -- the Registry had wired into `PluginHooks`, type definitions were exported, yet there was no default implementation, no computation formula, no wiring to `ManoAggregator`. Master required the research team to answer: how is quality computed (OQ-1)? How does Layer 3 integrate (OQ-2)? What direction for audit strategy (OQ-3)? What is the event subscription list (OQ-4)? Should weights be configurable (OQ-5)? How does all of this fit into Plan30 (OQ-6)?

**The philosophical letter** targeted the definition of formations (samskara-skandha). Master explicitly criticized the Yogacara school's practice of lumping 49 mental factors (cetasika) into the formations aggregate as "highly problematic," and demanded deep investigation using original canonical texts (thus have I heard) as the primary source. This was not a decorative research direction -- it directly affected the foundational determination for the future expansion path of the `ISamskara` interface.

---

## SUNYATA's Dual-Track Architecture

Research Director SUNYATA designed a dual-track structure accordingly, establishing cross-track priority rules:

| Track | Scope | Sub-items | Team |
|-------|-------|-----------|------|
| Track A | AuditContext type + audit logging | A1-A4 | VITRUVIUS, KERNEL, GUARDIAN, ARCHIMEDES, WIENER, BABBAGE |
| Track B | ILoopQualityMonitor implementation spec | B1-B4 | WIENER, ATHENA, BABBAGE, HERACLITUS, TURING, PASCAL |
| Track C | Formations deep investigation | C1-C4 | NAGARJUNA, ASANGA, LINNAEUS, PENROSE, PASCAL |
| Track D | Engineering synchronization | D1-D2 | TURING, ARCHIMEDES, VITRUVIUS, GUARDIAN |

The key rule in the cross-track influence protocol: **Philosophical conclusions (D1) precede engineering design (D2/D3), ensuring that skandha-attribution determinations are not overridden by engineering convenience.** If conclusions from C1-C4 conflict with design assumptions in A/B, the engineering track must wait for the philosophical ruling.

R1 produced 14 independent research reports. R2 cross-review found 24 consensus points with only 3 points of divergence. R3 comprised three debates, 245 minutes, 17 resolutions, 13 unanimous (20/20), 0 vetoes.

This was a round of precision engineering.


# Chapter One: Canonical Reconstruction of Formations

---

## 1.1 Methodology: Thus Have I Heard

The philosophical track was co-led by NAGARJUNA (Madhyamaka school) and ASANGA (Yogacara school). It was precisely the Yogacara approach that Master had criticized, and SUNYATA deliberately assigned the Yogacara specialist to participate in self-critique -- not as a punitive arrangement, but as a methodological necessity: only someone deeply versed in a system's internal logic can precisely identify its fracture points.

The textual hierarchy was strictly delineated:

| Level | Source | Status |
|-------|--------|--------|
| Primary | Pali Nikayas / Chinese Agamas | Sole definitional authority |
| Secondary | Dependent origination suttas (SN 12) | Structural reference |
| Tertiary | Nama-rupa-vinnana framework (SN 12.2, MN 9) | Cross-validation |
| Excluded | Abhidhamma treatises (Vibhanga, Dhammasangani) | Comparison only, not for attribution |

This stratification directly responded to Master's directive: treatises are systematization products of later scholars, not the Buddha's original words.

---

## 1.2 SN 22.56: The Six Classes of Volition -- The Original Definition of Formations

The Khandha-samyutta's SN 22.56 (Upadana Sutta) is the core source for the definition of the five aggregates:

> Monks, what are formations (sankhara-kkhandha)? There are six classes of volition (cha cetana-kaya): volition regarding forms, volition regarding sounds, volition regarding odors, volition regarding tastes, volition regarding tactile objects, volition regarding mental objects. Monks, this is called formations.

Textual analysis:

| Pali Term | Content | OpenStarry Correspondence |
|-----------|---------|--------------------------|
| rupa-sancetana | Form-volition -- intention toward visual objects | Reactive intention toward visual/text input |
| sadda-sancetana | Sound-volition -- intention toward auditory objects | Reactive intention toward audio/event input |
| gandha-sancetana | Odor-volition -- intention toward olfactory objects | Not typical for Agent scenarios |
| rasa-sancetana | Taste-volition -- intention toward gustatory objects | Not typical for Agent scenarios |
| photthabba-sancetana | Touch-volition -- intention toward tactile objects | Reactive intention toward API/tactile events |
| dhamma-sancetana | Mental-object-volition -- intention toward mental objects | Reactive intention toward internal cognitive objects |

Key insight: **In the original canonical texts, the definition of formations is entirely centered on cetana (intention/volition)** -- it describes six types of intention-formation directed at sense objects, not a "miscellaneous bin for mental activities other than feeling and perception."

---

## 1.3 SN 22.79: Constructing All Conditioned Phenomena

> Monks, why are they called formations (sankhara)? Because they construct (abhisankharonti) conditioned phenomena (sankhatam). What conditioned phenomena do they construct? They construct form as form, feeling as feeling, perception as perception, formations as formations, consciousness as consciousness.

This passage reveals a second core characteristic of formations: **Formations not only construct actions but also construct the conditioned states of all five aggregates.** In engineering terms, `ISamskara` should not be limited to external tool calls like `ITool.execute()`, but should encompass "all constructive activity that changes system state" -- including altering how the system responds to future inputs.

This directly connects to VasanaEngine's long-term roadmap (D-29-8): past behavioral patterns influencing future gear selection is precisely the engineering embodiment of "formations constructing the conditioned state of consciousness."

---

## 1.4 SN 22.95: The Plantain Simile -- A Coreless Dynamic Process

> Formations are like a plantain trunk (kadalupamo sankhara) -- if a person peels a plantain trunk seeking a solid core, they peel layer after layer and find nothing at all.

This is the classic expression of the third core characteristic of formations: **a coreless dynamic process**. Formations are not a fixed "entity" but a continuously operating "process."

The engineering correspondence is remarkably precise: `ISamskara` plugins should be lightweight and composable, not dependent on persistent internal state. Each plugin is a "layer" -- peeling away any one layer never reveals an irreplaceable core logic. This aligns perfectly with OpenStarry's Tenet #2 (Everything is a Plugin) and the microkernel architecture (Core contains no business logic).

---

## 1.5 MN 44: The Three Types of Formations as Complementary Perspectives

Visakha asked the bhikkhuni Dhammadinna:

| Formation | Pali Name | Definition | Canonical Reasoning |
|-----------|-----------|------------|-------------------|
| Bodily formation | kaya-sankhara | In-and-out breathing | A bodily phenomenon, bound to the body |
| Verbal formation | vaci-sankhara | Initial application (vitakka) + sustained application (vicara) | One first applies and sustains thought, then speaks |
| Mental formation | citta-sankhara | Perception (sanna) + feeling (vedana) | Mental phenomena, bound to the mind |

Here a tension exists between canonical frameworks: citta-sankhara (mental formation) **includes** sanna (perception) and vedana (feeling), yet in the five-aggregate framework these two are independent aggregates. NAGARJUNA's analysis: **This is not a logical contradiction, but different observation angles (drsti-bheda) of different classification systems** -- the three-formation classification observes "what conditions what," while the five-aggregate classification observes "what are the key objects of contemplative practice." The Yogacara school's attempt to forcibly unify the two systems led to the problem of cramming 49 mental factors into formations.

Engineering implication: Bodily formation corresponds to `ITool.execute()` (physical-layer construction), verbal formation corresponds to initial-and-sustained application (`vitakka-vicara`, initial cognitive processing), and mental formation corresponds to `IVedana` + `ISamjna` (already covered). Notably, `VitakkaWatchdog` in OpenStarry is a stabilization monitoring mechanism, functionally closer to consciousness than to formations -- this is not a misattribution, but rather a consequence of MN 44's verbal-formation classification and the five-aggregate classification being inherently complementary perspectives.

---

## 1.6 Critique of the Yogacara Mental Factor System

ASANGA personally led a critical analysis of the Yogacara school's 51-cetasika system (Report C2). The Yogacara school assigns 49 of 51 mental factors to formations -- leaving only "feeling" and "perception" for the feeling and perception aggregates. The item-by-item analysis yielded:

| Category | Count | Proportion | Description |
|----------|-------|------------|-------------|
| Genuinely formations | 7 | 14% | chanda, virya, apramada, mraksa, matsarya, maya, sathya |
| Already correctly attributed | 12 | 24% | Plugins already confirmed through debate in OpenStarry |
| Possibly other aggregates | 18 | 37% | Functionally closer to consciousness (judgment) or feeling (affective) |
| Mixed / requires further study | 14 | 28% | Cross-aggregate functions, requiring case-by-case analysis |

ASANGA's conclusion: "The functional descriptions in the mental factor list have reference value, but their skandha-attribution classifications have deviated from the canonical cetana-centered definition." This is not a wholesale rejection of Yogacara -- rather, it draws a clear methodological distinction between canonical texts and treatises.

---

## 1.7 Three Criteria and the Core Distinction

LINNAEUS distilled from the canonical analysis the "Three Criteria for Formations Attribution," established as a permanent determination tool [D1-R3, 20/20]:

1. **Conditioning**: Does it create / change / produce new states?
2. **Cetana-driven**: Is it driven by the intention-formation process?
3. **Environmental Shift**: Does it alter subsequent cognitive conditions?

All three "yes" -> formations (samskara); all three "no" -> consciousness (vijnana); mixed -> requires case-by-case analysis, possibly cross-aggregate.

PENROSE further compressed this into a distinction immediately graspable by any programmer:

> **Formations = WRITE** (actively changing the world's state)
> **Consciousness = READ** (passively evaluating the world's state)

Correspondence in the OpenStarry codebase:

| Skandha Attribution | Interface | Operation Type | Code Path |
|--------------------|-----------|---------------|-----------|
| Formations (WRITE) | `ITool` | Tool execution, changes environment | `types/aggregates.ts#ISamskara` |
| Formations (WRITE) | `ISlashCommand` | Command execution, changes state | `types/aggregates.ts#ISamskara` |
| Consciousness (READ) | `IGuide` | Evaluative guidance, no state change | `types/aggregates.ts#IVijnana` |
| Consciousness (READ) | `IVolition` | Deliberative judgment, no state change | `types/aggregates.ts#IVijnana` |

This WRITE/READ distinction was unanimously confirmed by D1-R5 (20/20), becoming the operational principle for skandha attribution.


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


# Chapter Five: Master's Cetasika Directive and Permanent Rules

---

## 5.1 Trigger: The Chain Reaction of Mental Factor Analysis

The philosophical track's C2 report (critical analysis of the Yogacara cetasika system) was presented to DC Master during R2 cross-review. ASANGA had compiled item-by-item re-attribution recommendations for all 51 mental factors -- 18 of which (37%) were judged functionally closer to the consciousness or feeling aggregates rather than formations.

Master's response was not a single ruling, but three rounds of progressive refinement. Each round sharpened the focus further.

---

## 5.2 First Round: Methodological Demarcation Between Canon and Treatise

Master's core thesis: **Mental factors (cetasika) are systematization products of treatises (Abhidharma), not content from the original suttas/agamas.**

This is not scholarly bias. The Buddha spoke in the original canon of the five aggregates, dependent origination, the Noble Eightfold Path, and the thirty-seven factors of awakening. The classification system of "51 mental factors" was the systematic compilation of later scholars (particularly Yogacara masters such as Asanga and Vasubandhu). The original texts do mention many cetasika names (such as prajna, virya, hri, apatrapya), but **organizing them into a fixed-count classification system and assigning skandha attributions** was the treatises' work.

Master's direct conclusion: **Plugin names must not use Sanskrit cetasika names.**

Engineering impact: Any plugin named with a Sanskrit cetasika term (e.g., VīryaPlugin, PrajnaPlugin) must be renamed to engineering terminology.

---

## 5.3 Second Round: Preserving Functional Reference Value

The first round could easily be misread as "cetasikas are entirely useless." Master corrected this impression in the second round: the **functional descriptions** of mental factors retain reference value.

For example, the cetasika "virya" (diligence/energy) describes the function of "persistent, unwavering commitment to wholesome states." One can reference this functional description when designing a plugin -- but the plugin must not be called VīryaPlugin; it should use an engineering name (e.g., `PersistencePlugin`, `RetryPlugin`).

Master's precise formulation: "It is acceptable to say 'we referenced the meaning of virya and designed a retry plugin.' It is not acceptable to say 'the retry plugin = virya.'"

This is the principle of "may cite, may not equate."

---

## 5.4 Third Round: Naming Decoupling Yields Attribution Freedom

The third round was the most profound. Master said: "A plugin is not a cetasika."

On the surface this seems straightforward. But its implications are structural.

In the Yogacara school, each cetasika has a fixed skandha attribution -- "virya" belongs to formations, "prajna" belongs to consciousness. If plugin = cetasika, then the plugin's skandha attribution is also locked in. But plugin != cetasika. A plugin may simultaneously have both formations and consciousness functions -- it both makes judgments (READ) and executes actions (WRITE).

Under the cetasika system this is impermissible (each cetasika belongs to exactly one skandha), but under the plugin system it is entirely legitimate. **Naming decoupling yields attribution freedom** -- not using cetasika names for plugins actually liberates plugins from the fixed classificatory constraints of treatises, allowing them to naturally span multiple aggregates.

---

## 5.5 Eight Permanent Rules

The three rounds of directives were consolidated into eight permanent rules, which together with the five skandha-attribution principles form the judgment baseline for all future naming and attribution questions:

| # | Rule | Engineering Impact |
|---|------|--------------------|
| 1 | Cetasikas are treatise products, not original canonical content | Do not use the cetasika system as the default framework for architectural design |
| 2 | Cetasika functional descriptions have reference value, suitable as plugin design inspiration | Design documents may cite cetasika functional descriptions |
| 3 | It is valid to state "referenced cetasika X's meaning to design plugin Y" | Design provenance is legitimate; equivalence claims are not |
| 4 | Plugins use engineering terminology for naming; Sanskrit cetasika names are prohibited | Hard naming convention rule |
| 5 | Sanskrit terms are limited to those from original canonical texts -- skandha, sparsha are permitted | Distinguishes canonical Sanskrit from treatise Sanskrit |
| 6 | Cetasika classifications do not serve as skandha-attribution evidence | "Yogacara says X belongs to formations" cannot serve as plugin attribution evidence |
| 7 | Existing plugin attribution decisions are unaffected | Already-confirmed attributions are not overturned by the new rules |
| 8 | Plugin != cetasika; skandha attribution may naturally span multiple aggregates | Cross-aggregate plugins are legitimate and expected |

---

## 5.6 Five Skandha-Attribution Principles [D1-R6, 20/20]

Complementing the eight rules, the five principles provide a positive determination method:

1. **Functional analysis is the sole basis for skandha attribution** -- not names, not tradition, not treatises
2. **The Yogacara 51-cetasika system serves as a functional reference list, not an attribution authority**
3. **Sanskrit terms used in code naming are limited to those originating from the original canon**
4. **Plugin != cetasika; skandha attribution may naturally span multiple aggregates**
5. **Existing attribution decisions (based on functional analysis) remain valid**

These five principles plus the eight rules form a complete determination framework. In the future, whenever someone asks "which skandha does this function belong to" or "what should this plugin be named," there is no need to debate from scratch -- simply consult these 13 rules.

---

## 5.7 Cascading Revisions to the D1 Agenda

Master's three rounds of directives directly led to revisions of the D1 debate agenda:

- **D1-Q2 (cetasika multi-aggregate attribution problem) was deleted** -- since cetasika classifications are not used as a basis, debating their multi-aggregate attribution loses its purpose
- **D1-Q6 (item-by-item vote on 26 cetasikas) was simplified** -- changed to voting on the attribution principles themselves, not case-by-case determinations
- **The manasikara supplementary agenda item was canceled** -- `CoarisingBundle` does not include manasikara as an independent interface, requiring no further discussion

These revisions saved at least 45 minutes of debate time while elevating the abstraction level of the resolutions -- from case-by-case rulings to principle establishment.

---

## 5.8 Engineering Applicability Assessment of Buddhist Mind Theories [D1-R4a/b/c]

The C4 report (PASCAL + PENROSE) conducted a systematic assessment of the engineering applicability of all Buddhist mind theories:

| Theory | Conclusion | Resolution | Test Results |
|--------|-----------|------------|-------------|
| Five Aggregates | Already fully integrated | No action needed | -- |
| Nama-rupa-vinnana | Core value already absorbed | No action needed | -- |
| Dependent Origination | Explanatory appendix | 02-7 P2 [D1-R4a, 19/20] | -- |
| Eight Consciousnesses | Awaiting multi-Agent scenarios | Cycle 03+ | -- |
| **Four Wisdoms** | **Excluded** | **D1-R4b, 18/20** | All four tests failed |
| Cognitive Sequence | Strongest structural correspondence | 02-7 P2 [D1-R4a, 19/20] | -- |

The exclusion of the Four Wisdoms (adarsa-jnana, samata-jnana, pratyaveksana-jnana, krtyanusthana-jnana) was particularly significant. Four exclusion tests:

1. **Removal test**: Does removing the Four Wisdoms mapping change any design? -> No
2. **Code existence test**: Do the Four Wisdoms have counterparts in the codebase? -> No
3. **Driving force test**: Did the Four Wisdoms drive any engineering decision? -> No
4. **Irreplaceability test**: Is there a simpler engineering concept that can substitute? -> Yes

2 dissenting votes argued they could be retained as reference material. But all four tests failed -- retaining them would only increase cognitive load without adding design value.

---

## 5.9 ISamskara Expansion Directions [D1-R3, 20/20]

Confirmed the Cycle 02-5 D3-R4 resolution: no new ISamskara sub-interfaces at this time. Four directions are archived as long-term candidates:

| Direction | Description | Priority | Timeline |
|-----------|-------------|----------|----------|
| A: cetana-formation | Intention planning -- expanding from "execute tool" to "form intention" | P2 | Cycle 03+ |
| B: vasana-imprinting | Habit formation -- learning and memory of behavioral patterns | P2 | Long-term (VasanaEngine) |
| C: kaya extension | Environmental transformation -- extension of bodily formation | P3 | No scheduling needed |
| D: vaci | Communication formation -- extension of verbal formation | P3 | No scheduling needed |

Directions A and B directly relate to the canonical analysis: cetana-formation corresponds to SN 22.56's six classes of volition (the intention-formation process), and vasana-imprinting corresponds to SN 22.79's "constructing all conditioned phenomena" (behavior shaping future conditions). Direction B's VasanaEngine is already scheduled in D-29-8 as a long-term roadmap item.

NAGARJUNA's summary: "Last round we learned what not to do. This round we learned why not to do it."


# Chapter Six: Three Debates -- The Precise Path from Divergence to Consensus

---

## 6.1 R2 Divergence Identification

R2 cross-review identified 24 consensus points and 3 points of divergence. All four cross-track comparison groups confirmed zero conflicts -- the philosophical track's conclusions did not affect any design assumptions in the engineering track:

| Comparison | Result |
|-----------|--------|
| C2 cetasika critique -> A1 AuditContext | 4/4 no impact |
| C4 engineering applicability -> D2 Plan30 | 4/4 no impact |
| C3 ISamskara expansion -> B1 formulas | 5/5 no impact |
| C2 cetasika critique -> skandha attribution list | 11 confirmed / 0 revised / 1 pending debate / 14 future |

All three divergences were internal to the engineering track:

1. **Extras write protocol**: A2 proposed generic event pattern vs. B3 proposed direct subscription -> Resolved in D2
2. **Extras key naming**: `loopQuality:score` vs. `loopQuality:composite` -> Unified to `loopQuality:composite` in D2
3. **loopQualityFn data source**: Whether L3 callback and extras cache should share the same source -> Resolved in D3 (dual-channel: pull + push)

---

## 6.2 D1: Formations Deep Investigation (approx. 75 minutes, 7 resolutions)

| Resolution | Content | Votes | Key Arguments |
|-----------|---------|-------|--------------|
| D1-R1 | Core definition of formations: cetana-centered, constructive function, coreless process | 20/20 | Direct citation of SN 22.56/79/95, no ambiguity |
| D1-R3 | No new ISamskara sub-interfaces; three criteria as permanent tool | 20/20 | Confirms 02-5 D3-R4, Directions A/B archived |
| D1-R4a | Cognitive sequence appendix scheduled for 02-7 P2 | 19/20 | 1 dissent argued it could be completed this round |
| D1-R4b | Four Wisdoms formally excluded | 18/20 | 2 dissenting votes argued for retention as reference; all four tests failed |
| D1-R4c | C4 comprehensive assessment table confirmed | 20/20 | -- |
| D1-R5 | "Activity and Transformation" principle; formations=WRITE, consciousness=READ | 20/20 | PENROSE's WRITE/READ distinction |
| D1-R6 | Five permanent skandha-attribution principles | 20/20 | Permanent baseline, not a single-round resolution |

D1 was the highest-consensus debate of the three -- five unanimous votes. The reason: the philosophical track's conclusions were directly grounded in original canonical citations, involving no engineering trade-off judgments, and thus leaving minimal room for divergence.

D1's conclusions required no supplementary agenda items for D2/D3 -- the cross-track influence protocol's "philosophy before engineering" rule was validated as zero-conflict in this round.

---

## 6.3 D2: AuditContext (approx. 85 minutes, 5 resolutions)

| Resolution | Content | Votes | Key Arguments |
|-----------|---------|-------|--------------|
| D2-R1 | Complete AuditContext type (sparshEvent required, history default 10 configurable) | 20/20 | A1-OQ1/2/3 all resolved |
| D2-R2 | Extras bag protocol (dual-event + SDK helper, shallow freeze, max 32 keys) | 19/20 | MESH opposed dual-event complexity; majority supported generality |
| D2-R3 | ConfidenceAuditLog (GUARDIAN D5 obligation fulfilled) | 20/20 | GUARDIAN confirmed settlement on the spot |
| D2-R4 | Layer integration Option C (L2->confidence, L3->threshold, alpha=0.10) | 20/20 | WIENER/BABBAGE stability analysis was decisive |
| D2-R5 | Three-phase auditor strategy: Phase 0 PassthroughAuditor | 20/20 | -- |

The voting process for D2-R4 is worth noting: WIENER and BABBAGE's stability analysis (Lyapunov comparison of Options A/B/C) was already presented in the R1 reports. No one challenged the analysis during R2 cross-review. By the time of the D2 debate, it passed unanimously -- the persuasive power of mathematical proof is deterministic.

All three R2 divergences were resolved in D2:
- Extras write -> Unified as dual-event + SDK helper (D2-R2)
- Key naming -> Unified as `loopQuality:composite` (D2-R2 ancillary resolution)
- loopQualityFn data source -> Deferred to D3

---

## 6.4 D3: LoopQualityMonitor (approx. 85 minutes, 5 resolutions)

| Resolution | Content | Votes | Key Arguments |
|-----------|---------|-------|--------------|
| D3-R1 | Four-dimension formulas confirmed (C/E/Conv/S; W=10, warmup=5, Q_default=0.5) | 20/20 | OQ-29-1 formally answered |
| D3-R2 | EventBus subscriptions: 6 events Phase 1; AgentEventType constant promotion | 20/20 | OQ-29-4 formally answered |
| D3-R3 | Extras write: D2-R2 pipeline + loopQualityFn dual-channel; per-route lifecycle | 20/20 | Resolves R2's third divergence |
| D3-R4 | Weights Phase 1 fixed balanced 0.25x4 | 20/20 | PASCAL's maximum entropy argument |
| D3-R5 | Plan30 = Monitor + L3 + type definitions; Plan31 = Auditor + Audit Trail | 19+1 conditional | GUARDIAN conditional approval |

D3-R5 was the only resolution with a conditional approval. GUARDIAN's condition: **Plan30's Wave 3 must include the `ConfidenceAuditLog` SDK type definition; it must not be deferred to Plan31.** Rationale: the log type is the core deliverable of the D5 concession conditions, and deferral equals debt extension. The condition was accepted, and GUARDIAN switched to approval.

---

## 6.5 Three-Phase Auditor Strategy [D2-R5, 20/20]

| Phase | Corresponding Plan | Implementation | Description |
|-------|-------------------|---------------|-------------|
| Phase 0 | Plan30 (W4, optional) | PassthroughAuditor | delta=0, pure logging; validates end-to-end pipeline integrity |
| Phase 1 | Plan31 | ThresholdAuditor | Rule-based: low confidence detection, loopQuality anomaly, trend detection |
| Phase 2 | Long-term | LLM-assisted | LLM-assisted auditing |

Phase 0's PassthroughAuditor appears useless -- an auditor that adjusts nothing. But ARCHIMEDES' engineering insight: "Its value lies not in auditing, but in testing. It verifies AuditContext assembly, extras collection, audit delta clamping, ConfidenceAuditLog emission -- the entire pipeline end-to-end. Like turning on the faucet after installing the plumbing."

All phases must comply with WIENER C-1/C-2/C-3 constraints -- this is not a Phase 0-specific requirement, but a permanent constraint.

---

## 6.6 Statistical Comparison

| Metric | Cycle 02-5 | Cycle 02-6 |
|--------|-----------|-----------|
| Resolutions | 29 | 17 |
| Vetoes | 0 | 0 |
| Unanimous (20/20) | ~20 (69%) | 13 (76%) |
| Master overturns | 2 | 0 |
| Debate sessions | 5 | 3 |
| R1 reports | -- | 14 |
| R2 consensus points | -- | 24 |
| R2 divergence points | -- | 3 |

DARWIN's observation: "02-5 was a correctness debate -- what is right, what is wrong. 02-6 was a specification debate -- what does the right thing look like. The latter naturally reaches consensus more easily, because it does not involve value judgments."

SUNYATA's analysis: "R1 was done well. Fourteen reports covered the entire problem space. R2 found only 3 divergences. When most questions have consensus before the debate, the debate becomes confirmation and refinement."

The reason for zero Master overturns: the eight rules were already established during the R2 phase (Master's three rounds of refinement), and all resolutions in D1-D3 operated within the framework of the eight rules. No resolution attempted to challenge the framework itself.


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
