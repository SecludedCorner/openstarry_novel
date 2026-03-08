# Prologue: From Clearing to Construction -- The Methodological Positioning of Cycle 02-6

---

## Research Context and Prior-Cycle Legacy

Cycle 02-5 constituted the largest normative correction in OpenStarry's research history: 29 resolutions, 2 Master overrides, and 7 design-document reorganizations. Its core achievement was the systematic removal of decorative Buddhist mappings, establishing the methodological stance that "functional analysis takes precedence over terminological tradition."

Cycle 02-6 inherits this legacy, yet its research character is fundamentally different. If the theme of 02-5 was "negative judgment" (what is wrong), then 02-6 is "affirmative construction" (what is right, and what precise specifications the right things should possess).

---

## Dual Research Mandate

**Engineering directive**: For the two skeleton components `IConfidenceAuditor` and `ILoopQualityMonitor` delivered in Plan29 (v0.29.0-alpha), Master required answers to six open questions (OQ-29-1 through 6): AuditContext fields, extras bag protocol, audit log format, quality formulas and event subscriptions, Layer 2/3 integration scheme, and Plan30 direction.

**Philosophical directive**: Using original sutras (evam maya srutam) as primary sources, conduct a renewed deep investigation of the samskara-skandha (formations aggregate). Master noted that the Yogacara school's practice of assigning the majority of mental factors (cetasika) to the samskara-skandha is "highly problematic," and suggested that the concept of "activity and transformation" could expand the subcategories of samskara.

---

## Research Design: Dual-Track Structure and Cross-Track Constraints

SUNYATA (#0) designed a four-track structure:

| Track | Scope | Sub-items | Scale |
|-------|-------|-----------|-------|
| Track A | AuditContext + Audit Log | A1-A4 | 4 groups |
| Track B | ILoopQualityMonitor Specification | B1-B4 | 4 groups |
| Track C | Samskara Philosophical Deep Dive | C1-C4 | 4 groups |
| Track D | Engineering Sync + Plan30 | D1-D2 | 2 groups |

Key constraint: **Cross-Track Influence Protocol** -- D1 (philosophical debate) must precede D2/D3 (engineering debates), ensuring that philosophical findings are injected into engineering design in real time.

---

## Research Process Overview

```
R0 Orientation -> R1 Independent Research (14 reports) -> R2 Cross-Review -> R3 Debate (3 sessions / 17 resolutions) -> R4 Finalization
```

The R1 phase produced 14 independent research reports, with team assignments as follows:

| Report | Topic | Lead |
|--------|-------|------|
| A1 | AuditContext Type Definition | VITRUVIUS + KERNEL |
| A2 | extras bag Mechanism | DARWIN + MESH |
| A3 | Audit Log Specification | GUARDIAN + ARCHIMEDES |
| A4 | Layer 2/3 Integration Path | WIENER + BABBAGE |
| B1 | Four-Dimensional Computation Formulas | WIENER + ATHENA + BABBAGE |
| B2 | EventBus Event Specification | HERACLITUS + TURING |
| B3 | extras Write Integration | LEIBNIZ + MESH |
| B4 | Weights and Configuration | PASCAL + ATHENA |
| C1 | Samskara in Original Sutras | NAGARJUNA + ASANGA |
| C2 | Yogacara Cetasika Critique | ASANGA + NAGARJUNA |
| C3 | ISamskara Expansion Directions | LINNAEUS + PENROSE |
| C4 | Mental Discourse Engineering Insights | PASCAL + PENROSE |
| D1 | v0.29.0-alpha Code Verification | TURING + ARCHIMEDES |
| D2 | Plan30 Direction Proposal | VITRUVIUS + GUARDIAN |

R2 identified 24 consensus points and 3 divergence points (extras write protocol, extras key naming, loopQualityFn data source). R3 totaled approximately 245 minutes; of the 17 resolutions, 13 passed unanimously (20/20), with 0 vetoes and 0 Master overrides.

The following chapters unfold in sequence: the philosophical track's deep investigation of samskara (Chapter 1), audit context design (Chapter 2), quality monitoring formulas (Chapter 3), integration architecture (Chapter 4), Master's cetasika directives (Chapter 5), methodological analysis of the debate process (Chapter 6), and the engineering blueprint with concluding summary (Chapter 7).

---
# Chapter 1: Canonical Reconstruction of Samskara -- From Cetana-Centrality to Functional Attribution Criteria

---

## 1.1 The Problem: Samskara as a "Residual Category"

Within the panca-skandha (five aggregates) architecture of OpenStarry v0.2.0-beta, the samskara-skandha (formations aggregate) has long suffered from definitional insufficiency. Compared to the clear functional mappings of rupa-skandha (form aggregate, corresponding to the `ISparsha` sensory contact interface), vedana-skandha (feeling aggregate, corresponding to the `IVedana` feeling interface), samjna-skandha (perception aggregate, corresponding to the `ISamjna` recognition interface), and vijnana-skandha (consciousness aggregate, corresponding to the `IManas` judgment interface), the samskara-skandha possesses only a single sub-interface `ITool`, responsible for external tool invocation.

This asymmetry is not accidental. Its root lies in the Yogacara school's treatment of the samskara-skandha. In the Yogacara classification system of fifty-one cetasika (mental factors), the vedana-skandha is assigned only one cetasika -- vedana (feeling) -- and the samjna-skandha is assigned only one -- samjna (perception). The remaining forty-nine cetasika are all subsumed under the samskara-skandha. The samskara-skandha thereby becomes a "residual category" -- any mental function that does not belong to feeling or perception is categorically assigned to formations.

DC Master explicitly identified this practice as "highly problematic" in the research mandate and required the team to return to the original sutras (evam maya srutam) to re-establish a functional definition of samskara.

---

## 1.2 The Definition of Samskara in Original Sutras

The philosophical track was led by NAGARJUNA (#7, Madhyamaka philosopher) and ASANGA (#8, Yogacara scholar). A noteworthy methodological arrangement: the expert representing the school under critique (Yogacara) was assigned to examine the problems of his own school, ensuring the internality and depth of the criticism.

### 1.2.1 The Six Cetana Groups: Cetana as the Defining Characteristic of Samskara

In the Samyutta Nikaya (SN 22.56, Khandha-samyutta), the Buddha defines the samskara-skandha with explicit precision:

> "And what are formations? There are these six groups of cetana (intention): cetana regarding form, cetana regarding sound, cetana regarding smell, cetana regarding taste, cetana regarding touch, cetana regarding mental objects. These are called formations."

Here "cetana" denotes intention/volition; the "six cetana groups" (cha cetana-kaya) refer to intentional responses directed toward six categories of sensory objects. The critical feature of this definition lies in its **exclusivity**: the samskara-skandha is not "everything mental except feeling and perception," but rather points precisely to cetana -- intentional fabrication directed at six types of objects.

### 1.2.2 The Fabrication Function: Abhisamskara and the Conditioning of Conditioned Phenomena

The Samyutta Nikaya (SN 22.79) further elucidates the function of samskara:

> "Formations fabricate form's conditioned state (rupam abhisankharonti)."

The verb abhisankharoti indicates that samskara does not merely "execute actions" but, more fundamentally, "fabricates" -- it creates conditions, modifies states, and influences subsequent cognitive processes. The fabricating function of samskara extends even to the other four aggregates: it can fabricate the conditioned state of form, the conditioned state of feeling, and even the conditioned state of consciousness.

### 1.2.3 The Plantain Simile: A Coreless Dynamic Process

The Samyutta Nikaya (SN 22.95, Phena-sutta) uses the plantain tree (kadali) as a simile for samskara:

> "Suppose a person were to strip a plantain trunk, seeking heartwood. They would peel it layer by layer and find nothing solid within."

This simile points directly to the ontological status of samskara: it is not an "entity" with a solid core, but rather a continuously operating "process." Each layer of fiber is a conditional fabrication; once peeled away, no intrinsic nature (svabhava) is found.

---

## 1.3 Three Core Characteristics

Based on the above canonical texts, the research team distilled three core characteristics of samskara:

| # | Characteristic | Canonical Basis | Functional Implication |
|---|---------------|-----------------|----------------------|
| 1 | **Cetana-centrality** | SN 22.56 (six cetana groups) | Samskara is defined by intention, not as a "residual category" |
| 2 | **Fabrication of all conditioned phenomena** | SN 22.79 (abhisamskara) | Samskara creates conditions, modifies states, affects all five aggregates |
| 3 | **Coreless dynamic process** | SN 22.95 (plantain simile) | Samskara is a process rather than an entity; no intrinsic nature is found |

---

## 1.4 Three Criteria for Samskara Attribution

Building on these three characteristics, LINNAEUS (#13, Taxonomy/Ontology Expert) proposed an operationalizable set of attribution tools -- the Three Criteria for Samskara Attribution:

**Criterion 1: Fabrication**
- Does the function create, modify, or produce new states?
- Test: Check whether the function's output modifies system state or the external environment.

**Criterion 2: Cetana-driven**
- Is the function driven by cetana (intention)?
- Test: Check whether the function's trigger originates from a volitional decision of the system, rather than a passive reaction.

**Criterion 3: Environmental Modification**
- Does the function alter subsequent cognitive conditions?
- Test: Check whether, after the function executes, the input space of subsequent cognitive loops has changed.

The three criteria were confirmed by Resolution D1-R3 as a **permanent tool**, applicable to all future aggregate-attribution determinations.

---

## 1.5 The WRITE/READ Dichotomy

PENROSE (#18, Quantum Consciousness Researcher) proposed a highly generalizable dichotomy during discussion:

> **Samskara = WRITE (actively changing the world)**
> **Vijnana = READ (passively evaluating the world)**

This dichotomy has a natural counterpart in computer science. In operating system theory, WRITE operations modify system state (side-effecting operations), while READ operations merely observe system state (pure-function operations). Mapped to OpenStarry's code:

| Operation Type | Aggregate Attribution | Code Interface | Function |
|---------------|----------------------|---------------|----------|
| WRITE | samskara-skandha | `ITool`, `ISlashCommand` | Execute actions, modify environment |
| READ | vijnana-skandha | `IGuide`, `IVolition` | Evaluate situations, render judgments |

This dichotomy was formally confirmed by Resolution D1-R5 (20/20 unanimous) and became the core articulation of the "activity and transformation" principle.

---

## 1.6 Critical Analysis of the Yogacara Cetasika System

ASANGA personally led the critical analysis of the Yogacara fifty-one cetasika system (Report C2). Using the Three Criteria for Samskara Attribution as the analytical instrument, he examined each of the 49 cetasika assigned to the samskara-skandha by the Yogacara school. The results were as follows:

| Classification | Count | Percentage | Description |
|---------------|-------|-----------|-------------|
| Confirmed samskara | 7 | 14% | chanda (desire-to-act), virya (diligence), apramada (non-negligence), etc. |
| Already correctly attributed | 12 | 24% | Already assigned correct attribution in OpenStarry via functional analysis |
| Possibly belonging to other aggregates | 18 | 37% | Functionally closer to vijnana (e.g., prajna/wisdom) or vedana |
| Mixed / requiring further study | 14 | 28% | Requiring finer-grained functional analysis or cross-aggregate treatment |

The methodological significance of this analysis lies in replacing traditional taxonomy with functional analysis as the basis for aggregate attribution. As ASANGA himself stated:

> "The cetasika list is a useful catalog of functional descriptions, but it is a product of the Abhidharma treatises, not the Buddha's own words. We may consult its functional descriptions, but we must not allow its classificatory scheme to determine aggregate attribution."

---

## 1.7 Five Permanent Principles for Aggregate Attribution

Based on the above research, Resolution D1-R6 (20/20 unanimous) established five permanent principles:

1. **Functional Analysis Principle**: Functional analysis is the sole basis for aggregate attribution.
2. **Cetasika Reference Principle**: The Yogacara fifty-one cetasika system serves as a functional reference list, not as a basis for attribution.
3. **Sanskrit Restriction Principle**: When Sanskrit terms are used in code naming, they are restricted to those originating from original sutras (e.g., skandha, sparsha); Sanskrit names coined in Abhidharma treatises for cetasika shall not be used.
4. **Cross-Aggregate Attribution Principle**: A Plugin is not equivalent to a cetasika; aggregate attribution may naturally span multiple aggregates.
5. **Existing Resolution Principle**: Existing attribution resolutions (based on functional analysis) remain valid.

These five principles, together with the Master's Eight-Point Rules discussed in Chapter 5, constitute the permanent adjudication framework for all future naming and attribution questions in OpenStarry.

---
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
# Chapter 4: Dual-Channel Integration Architecture -- Orthogonal Separation Design for Layers 2/3

---

## 4.1 Formal Description of the Decision Mechanism

OpenStarry's core routing decision is a threshold comparison: if $c > \theta$, the arbiter's recommended plan is adopted; otherwise, the default plan is used. Cycle 02-6 introduces IConfidenceAuditor (Layer 2, adjusting $c$) and ILoopQualityMonitor (Layer 3, adjusting $\theta$). The central question: how to make both effective simultaneously without mutual interference?

---

## 4.2 Three Candidate Schemes and Selection

**Scheme A (Serial)**: $Q$ first modifies the threshold, then the auditor evaluates under the new threshold. Sequential dependency exists.
**Scheme B (Coupled)**: $Q$ and the auditor simultaneously affect both confidence and threshold. Cross-terms exist.
**Scheme C (Orthogonal)**: The auditor modifies only confidence; the quality monitor modifies only the threshold. Fully independent.

Resolution D2-R4 (20/20 unanimous) selected Scheme C.

---

## 4.3 Formal Definition of Scheme C

**Layer 2**: $c_{adj} = c_{raw} + \text{clamp}(\Delta c, -0.05, +0.05)$

**Layer 3**: $\theta_{adj} = \max(\theta_{floor}, \; \theta_{base} \times (1 - \alpha \cdot Q))$, where $\alpha = 0.10$

**Final routing**: $c_{adj} > \theta_{adj}$ -> arbiter\_gear; otherwise default\_gear

---

## 4.4 Design Advantages

**Orthogonality**: Layer 2 operates solely on $c$; Layer 3 operates solely on $\theta$. No coupling functions of the form $f(c, Q)$ or $g(\theta, \Delta c)$ exist. The two components can be developed, tested, and deployed independently.

**BIBO stability**: $c_{adj}$ is clamped to $[0,1]$; $\theta_{adj} \geq \theta_{floor} > 0$. The absence of cross-terms eliminates inter-channel positive feedback amplification paths.

**Conservative degradation**: Without an auditor, $\Delta c = 0$; without a quality monitor, $Q = 0$. When either component is absent, system behavior is equivalent to the version where that component does not exist.

---

## 4.5 Quality Score Transmission: Pull + Push Dual Channel

| Consumer | Requirement | Transmission Mode |
|----------|------------|-------------------|
| ManoAggregator (L3) | Real-time numeric value | Pull: `loopQualityFn()` callback |
| IConfidenceAuditor (L2) | Rich context | Push: extras bag via `audit:context_contribute` |

The Push channel writes `loopQuality:vector` (four-dimensional) and `loopQuality:composite` ($Q$). The lifecycle is per-routing-cycle; the extras bag is cleared after each routing cycle completes (LEIBNIZ #14 emphasized: avoid accumulation of stale information).

---

## 4.6 Five-Layer Decision Model

```
L0: EventBus          -- foundational event stream
L1: Klesha             -- four emotion modules adjusting threshold
L4: Vedana Emergency   -- emergency feeling directly lowers threshold (safety-critical, highest priority)
L3: LoopQuality        -- quality score fine-tunes threshold (alpha=0.10)
L2: Audit              -- auditor fine-tunes confidence (+-0.05)
-> Final comparison: c_adj > theta_adj -> routing decision
```

Layer ordering follows the principle of decreasing priority. The success criterion for Plan30: L0 through L4 all have actual signal paths.

**Edge cases**: Multiple monitors are aggregated by simple averaging (Phase 1); a monitor that has not updated for more than 5000ms is treated as expired, $Q = 0$, and L3 does not take effect.

---
# Chapter 5: Three Rounds of Refinement on Cetasika Naming Directives -- From Abhidharma Artifacts to Naming Decoupling

---

## 5.1 The Triggering Context

During the R2 cross-review period, ASANGA's Yogacara cetasika critique report (C2) was submitted to DC Master. Master issued three successive rounds of directives, directly resulting in a revision of the D1 agenda: D1-Q2 (multi-aggregate attribution of cetasika) was deleted, and D1-Q6 (item-by-item voting on 26 items) was simplified to a principles-level vote.

---

## 5.2 First Round: Distinguishing Sutras from Treatises

> Cetasika (mental factors) are products of the Abhidharma treatises, not content from the original sutras (Sutta/Agama).

The Buddha expounded the panca-skandha (five aggregates), pratityasamutpada (twelve links of dependent origination), and the arya-astangika-marga (Noble Eightfold Path) in the original sutras (SN 22.56, MN 44, etc.). The fifty-one cetasika classification system was constructed by later Abhidharma scholars such as Asanga and Vasubandhu, centuries after the Buddha's parinirvana.

Direct conclusion: **Plugin naming must not use cetasika Sanskrit names.**

---

## 5.3 Second Round: The Reference Value of Functional Descriptions

> The functional descriptions of cetasika possess reference value and may serve as inspiration for Plugin design.

The cetasika "virya" (diligence) describes a function of "sustained effort," which can inspire the design of a retry Plugin -- but that Plugin should be named `RetryPlugin`, not `VīryaPlugin`.

- **Permitted**: "Inspired by the meaning of virya, we designed a retry Plugin"
- **Prohibited**: "Retry Plugin = virya"

This distinction draws a boundary between "reference" and "identification."

---

## 5.4 Third Round: Naming Decoupling and Attribution Freedom

> Plugin does not equal cetasika (plugin ≠ cetasika).

Logical corollary: In the Yogacara system, each cetasika has a fixed aggregate attribution (e.g., virya belongs to the samskara-skandha). If Plugin = cetasika, then Plugin attribution is locked. But since Plugin ≠ cetasika, a Plugin may simultaneously possess samskara functions (WRITE) and vijnana functions (READ) without logical contradiction.

Master's synthesis: **"Naming decoupling brings attribution freedom."**

---

## 5.5 Eight Permanent Rules

| # | Rule | Nature |
|---|------|--------|
| 1 | Cetasika are products of Abhidharma treatises, not original sutra content | Philological determination |
| 2 | Cetasika functions may serve as Plugin design inspiration | Affirmative retention |
| 3 | It is permissible to state "Inspired by the meaning of a certain cetasika, we designed a certain Plugin" | Expression norm |
| 4 | Plugins are named using engineering terminology; cetasika Sanskrit names are prohibited | Naming norm |
| 5 | Sanskrit terms are restricted to those from original sutras | Terminological scope |
| 6 | Cetasika classification does not serve as a basis for aggregate attribution | Attribution principle |
| 7 | Existing Plugin attribution resolutions are unaffected | Stability guarantee |
| 8 | Plugin ≠ cetasika; Plugins may naturally span multiple aggregates | Cross-aggregate freedom |

---

## 5.6 Complementarity with the Five Aggregate-Attribution Principles

| Aspect | Five Attribution Principles | Eight-Point Rules |
|--------|---------------------------|-------------------|
| Origin | Distilled by the research team | Directed by DC Master |
| Focus | Attribution determination method | Naming and terminological norms |
| Core claim | Functional analysis as the sole basis | Plugin ≠ cetasika; naming decoupling |

Together, the two rule sets constitute a permanent adjudication framework. NAGARJUNA: "In 02-5 we learned what not to do. In 02-6 we learned why not to do it."

---
# Chapter 6: Methodological Analysis of the Debate Process -- From Conflict-Driven to Consensus-Confirming

---

## 6.1 Structural Comparison with Cycle 02-5

| Metric | Cycle 02-5 | Cycle 02-6 | Change |
|--------|-----------|-----------|--------|
| Debate sessions | 5 | 3 | -40% |
| Total resolutions | 29 | 17 | -41% |
| Unanimous (20/20) | ~20 (~69%) | 13 (76%) | +7pp |
| Master overrides | 2 | 0 | -100% |
| Total debate time | ~400 min (est.) | ~245 min | -39% |

DARWIN's (#6) structural explanation: 02-5 was a correctness debate, where the contested question was what is right and what is wrong; 02-6 was a specification debate, where the contested question was what the right thing should look like. The latter is inherently more conducive to consensus. SUNYATA added: the 14 R1 reports yielded 24 consensus points and only 3 divergence points during R2 cross-review, transforming the debate function from "disputation" to "confirmation and refinement."

---

## 6.2 Overview of Three Debate Sessions

### D1: Samskara Deep Dive (approximately 75 minutes, 7 resolutions)

Conducted first per the Cross-Track Influence Protocol. D1-R1 (20/20) confirmed the cetana-centric definition; D1-R3 (20/20) confirmed no new ISamskara sub-interfaces, with the three criteria as permanent tools; D1-R4a (19/20) scheduled the cognitive sequence (citta-vithi) appendix for Cycle 02-7; D1-R4b (18/20) excluded the four knowledges (catvari-jnanani) via four tests; D1-R4c (20/20) confirmed the mental discourse evaluation rubric; D1-R5 (20/20) confirmed the WRITE/READ dichotomy; D1-R6 (20/20) confirmed the five aggregate-attribution principles. Cross-track influence assessment: D1 conclusions required no additional agenda items for D2/D3.

### D2: AuditContext (approximately 85 minutes, 5 resolutions)

D2-R1 (20/20) confirmed the AuditContext type; D2-R2 (19/20) confirmed the extras bag protocol (one dissenting vote deemed the dual-event pattern over-engineered); D2-R3 (20/20) confirmed ConfidenceAuditLog, with GUARDIAN declaring D5 conditions fulfilled; D2-R4 (20/20) confirmed Scheme C dual-channel; D2-R5 (20/20) confirmed the three-phase Auditor strategy (Phase 0 PassthroughAuditor -> Phase 1 ThresholdAuditor -> Phase 2 LLM-assisted). All three divergences identified in R2 were resolved.

### D3: LoopQualityMonitor (approximately 85 minutes, 5 resolutions)

D3-R1 (20/20) confirmed the four-dimensional formulas; D3-R2 (20/20) confirmed event subscriptions + AgentEventType constant promotion; D3-R3 (20/20) confirmed extras lifecycle (per-routing-cycle); D3-R4 (20/20) confirmed equal-weight strategy; D3-R5 (19+1 conditional) confirmed Plan30 direction -- GUARDIAN's condition: W3 must include the ConfidenceAuditLog SDK type definition and must not be deferred to Plan31. The condition was accepted.

---

## 6.3 Quantitative Results of R2 Cross-Review

The R2 phase completed 4 sets of cross-track comparisons:

| Comparison | Result |
|-----------|--------|
| C2 cetasika critique -> A1 AuditContext | 4/4 no impact |
| C4 engineering insights -> D2 Plan30 | 4/4 no impact |
| C3 ISamskara expansion -> B1 formulas | 5/5 no impact |
| C2 cetasika critique -> aggregate attribution list | 11 confirmed / 0 requiring correction / 1 pending debate / 14 for future consideration |

Intra-track consistency: Track A 5/5 consistent, Track B 3/5 consistent (1 divergence), Cross A-B 1/3 consistent (2 divergences). All three divergences were resolved in D2.

The academic significance of the cross-track comparison results lies in this finding: the philosophical track's discoveries (samskara redefinition, cetasika critique) and the engineering track's designs (AuditContext, quality formulas) are structurally orthogonal. This validates SUNYATA's dual-track design hypothesis: philosophical deep dives provide adjudication frameworks, engineering design proceeds independently within those frameworks, and the two do not exhibit conflicting dependencies.

---

## 6.4 Methodological Explanation of Zero Vetoes

The passage of all 17 resolutions can be explained at three levels: (1) R1 quality effect -- 87.5% of issues had consensus before the debate began; (2) transformation of debate character -- divergences in specification debates can be resolved through technical argumentation; (3) effectiveness of the cross-track protocol -- D1's seven philosophical resolutions provided a stable conceptual foundation for D2/D3, eliminating framework-level divergences.

---
# Chapter 7: Engineering Blueprint and Research Summary -- Plan30 Specifications and the Academic Contributions of Cycle 02-6

---

## 7.1 Plan30 Engineering Specifications [D3-R5, 19+1 conditional]

| Wave | Content | Est. LOC | Key Technical Points |
|------|---------|---------|---------------------|
| W1 | Default LoopQualityMonitor Plugin | ~120 | Four-dimensional formulas, 6 event subscriptions, O(1)/event |
| W2 | Layer 3 wiring (Scheme C) | ~80 | `loopQualityFn()` callback, $\alpha=0.10$ |
| W3 | Type definitions and event constants | ~60 | ConfidenceAuditLog SDK, AgentEventType promotion |
| W4 (optional) | PassthroughAuditor | ~30 | delta=0 passthrough audit, end-to-end pipeline verification |

Total: ~260-290 LOC + ~130 test LOC. Success criterion: Model Delta L0 through L4 all have actual signal paths.

---

## 7.2 Plan31 Outlook

Plan31 completes the end-to-end landing of the audit pipeline (~350 LOC): AuditContext assembly (Core responsibility), Default ThresholdAuditor (Phase 1 rule-based), Audit Trail JSONL persistence. Plan30 builds the pipeline; Plan31 lets logic flow through it.

---

## 7.3 Cycle 02-7 Research Outlook

- **P0**: Plan31 specification research
- **P1**: Lyapunov stability parameter calibration ($\alpha$ validation), Moha/Sneha coupling simulation, multi-monitor aggregation strategy verification
- **P2**: Cognitive sequence (citta-vithi) appendix, dependent origination (pratityasamutpada) appendix
- **Cycle 03+**: Eight-consciousness deepening (alaya-vijnana multi-Agent), VasanaEngine, ISamskara Direction A/B

---

## 7.4 Success Criteria Achievement

| # | Criterion | Achieved |
|---|----------|----------|
| 1 | AuditContext type definition | D2-R1 (20/20) |
| 2 | Audit log format (GUARDIAN D5 fulfilled) | D2-R3 (20/20) |
| 3 | LoopQualityVector four-dimensional formulas | D3-R1 (20/20) |
| 4 | EventBus event subscription list | D3-R2 (20/20) |
| 5 | All OQ-29 answered (6/6) | Distributed across resolutions |
| 6 | Plan30 direction proposal | D3-R5 (19+1) |
| 7 | Samskara deep dive report | C1-C4 + D1 |
| 8 | Item-by-item cetasika aggregate attribution (51 items) | C2 |
| 9 | No scope creep | Confirmed |

9/9 achieved.

---

## 7.5 Summary of Academic Contributions

### Philosophical Contributions

**Canonical reconstruction of samskara.** Rebuilding the functional definition of samskara from original sutras (SN 22.56, SN 22.79, SN 22.95, MN 44, SN 12.2), centering on cetana, replacing the Yogacara "residual category." The WRITE/READ dichotomy constitutes a high-congruence conceptual framework bridging Buddhist philosophy and computer science.

**Critique of Yogacara cetasika.** Item-by-item examination of 51 cetasika revealed systematic bias: only 14% were confirmed as belonging to the samskara-skandha. This provides quantitative support for the primacy of functional analysis over traditional taxonomy.

**Permanent adjudication framework.** The Five Aggregate-Attribution Principles + Master's Eight-Point Rules constitute a self-consistent, operationalizable adjudication framework. The core insight -- "naming decoupling brings attribution freedom" -- possesses methodological value beyond this project.

### Engineering Contributions

**AuditContext type**: The three WIENER constraints sever positive feedback loops; BIBO stability has been formally verified. **Four-dimensional quality vector**: Maximum entropy principle for equal weights, $O(1)$ complexity, degradation handling ensures robustness. **Scheme C dual-channel**: Orthogonal separation achieves provable BIBO stability, conservative degradation, and independent testability.

### Methodological Contributions

**The Cross-Track Influence Protocol** ensures that philosophical conclusions precede engineering design. **The conditional approval mechanism** (D3-R5 GUARDIAN) demonstrates an intermediate-state decision-making approach between security concerns and progress.

---

## 7.6 Conclusion: From Subtraction to Addition

- **Cycle 02-5** (subtraction): What is wrong -- decorative mappings, improper naming, confused attribution
- **Cycle 02-6** (addition): What is right -- cetana definition, AuditContext, four-dimensional formulas, Scheme C, permanent rules

02-5 cleared the foundation. 02-6 drew the blueprint. Plan30 begins construction.

Twenty researchers. Seventeen resolutions. Thirteen unanimous. Zero vetoes. Zero overrides. 9/9 success criteria achieved.

---

*End of Cycle 02-6.*

---
