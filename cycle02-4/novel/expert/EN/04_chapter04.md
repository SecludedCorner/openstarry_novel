# Chapter Four: Fictitious Code

---

## I. TURING's Correction

D4 opened with a correction.

When TURING stood up, everyone in the amphitheatre knew what "correction" meant. Across the six debates of Cycle 02-4, TURING's corrections always pointed to the same problem — an R1-phase report had cited code that did not exist, and other reports had unknowingly built upon that citation.

"Report R07 cites `ISensation.ingestToolResult()` in multiple locations."

His tone was like reading a log file. No blame, no theatrics — only facts.

"The `ISensation` interface and the `ingestToolResult()` method are completely absent from the entire v0.26.0-beta codebase. Global search: zero results."

The amphitheatre fell silent for three seconds.

R07 was the dynamic analysis report co-authored by HERACLITUS and ARCHIMEDES — it had cited this method to construct a complete analysis of "Path Beta," claiming that in v0.26.0-beta, samskara (volitional formation) results could update vedana (feeling-tone) in real time within the same turn. HERACLITUS looked down at his copy of the report. He did not argue — TURING's global search was irrefutable.

"The `feedbackQueue` mentioned in R07 also does not exist. The `SparshEvent.timestamp` field also does not exist."

Three fabrications. One report.

SUNYATA took over: "R07's design direction regarding vedana's active ingestion remains sound, but all conclusions citing R07's same-turn vedana micro-update must be revised to — not yet implemented; a feature to be built in Plan27."

---

The impact of this correction went beyond deleting a few citations. It changed the entire tenor of D4.

If `ingestToolResult()` existed, D4's discussion would have been "how to constrain an existing mechanism." But it did not exist — D4's discussion became "how to design a nonexistent mechanism from scratch." This was a freer design space, and also a more dangerous one — because you can build any theory atop fictitious code.

TURING's correction was like inspecting the foundation before construction. He found three stones that did not belong there and removed them. The foundation was more stable for it.

**The lesson was recorded: all analyses involving code citations must be verified by TURING.**

---

## II. Four Consensuses

After TURING's correction, four consensuses were quickly confirmed.

**Consensus A**: The sole direct output of samskara is IUI (the rupa-skandha output interface). ASANGA cited the *Anguttara Nikaya* — "Monks, I say that cetana (intention) is karma. Having intended, one acts through body, speech, and mind." Bodily and verbal actions influence the external world through body and speech. WIENER confirmed in the language of control theory: samskara is the controller, IUI is the actuator. A controller does not directly modify sensor readings. 9/9.

**Consensus B**: Samskara's influence on vedana is mediated through EventBus events. Vedana actively ingests (subscribe), rather than samskara actively pushing (push). PENROSE added: EventBus as intermediary does not alter causal direction — the causal structure remains samskara → vedana; the difference is in the degree of coupling. 9/9.

**Consensus C**: No independent SamskaraFeedback interface is needed. Samskara feedback already has two existing paths — the rupa-skandha indirect path and KleshaContext.actionHistory. Adding a third increases complexity with no additional benefit. GUARDIAN agreed from a security perspective: fewer influence channels reduce the attack surface. 9/9.

**Consensus D**: `ISensation.ingestToolResult()` does not exist. A statement of fact; no vote required.

Eight minutes. Four consensuses. D4's foundation was thereby established.

---

## III. Gain Ceiling: 0.3

The controversy of D4-R1 revolved around a single number.

PASCAL proposed: the valence-mapping gain from samskara results to vedana should not exceed 0.3.

"0.3 is not an arbitrary number." He opened his notebook and pointed to a line of formula. "In the Bayesian filtering framework, when observation noise σ_obs = 0.15, the initial Kalman gain K₁ = σ²_prior / (σ²_prior + σ²_obs) ≈ 0.308. Engineering convention rounds down to 0.3 as a conservative value."

WIENER analysed from the perspective of closed-loop stability. The complete closed loop: samskara → vedana → samjna → vijnana → samskara. If the gain from samskara results to vedana is w, and the gain product of all other links G_rest is approximately 2–3, then stability requires w < 1/G_rest ≈ 0.33 to 0.50. w ≤ 0.3 provides approximately 10% safety margin.

ARCHIMEDES raised a pragmatic question — do different action types require different gains? A gain ceiling of 0.1 would suffice for informational queries, but the dukkha-vedana (suffering-feeling) from failed destructive operations should be fully perceived; perhaps the gain ceiling ought to be higher.

PASCAL rejected the differentiated-gain proposal. "No need to manually set different ceilings — observation noise σ_obs can be adjusted by action type. High-risk actions have lower σ_obs, so the Agent trusts the signal more. Low-risk actions have higher σ_obs, so the Agent maintains scepticism. Kalman gain adjusts automatically."

WIENER's compromise: a uniform gain ceiling w ≤ 0.3 as a hard safety constraint, while allowing the Bayesian filter to adapt within that ceiling. "The hard ceiling is a simple invariant that SafetyMonitor can check. Bayesian adaptation provides flexibility within the ceiling."

NAGARJUNA offered an important Buddhist clarification: "The gain constraint should not be understood as suppressing samskara's influence on vedana — because in the Buddhist causal chain, samskara results are not directly written into vedana. The correct understanding of the gain constraint is VedanaSensor's maximum sensitivity."

A sensor's design parameter. Not a constraint on the causal chain.

**D4-R1: Gain ceiling w ≤ 0.3 — 8/9 (ARCHIMEDES abstained, preserving the possibility of future differentiation by risk level).**

---

## IV. Binding Itself in Its Own Silk

D4-R2 was the most mathematically dense resolution across all six debates — and WIENER's deepest analysis in the entirety of Cycle 02-4.

WIENER walked to the whiteboard and drew a loop.

```
Bias (Drishti) ↑
    → IGearArbiter's confidence inflated by bias
    → ManoAggregator erroneously selects Gear 1
    → Fast-path results reinforce Drishti
    → Drishti inflates further
    → ...
```

"This is the internal positive-feedback loop of mental action (mano-karma)." His voice was calm, but the arrows on the whiteboard described a dangerous structure. "It runs entirely within the controller, without corrective feedback from the external world."

The external loop — samskara → IUI → external world → IListener → new sparsha → new vedana — has the external world as a reality check. If an action is truly wrong, external consequences feed back as dukkha-vedana. But the internal loop of mental action lacks this mechanism.

WIENER formalised the loop. A three-dimensional state vector: drishti (view/bias) intensity d(t), effective confidence c(t), Gear 1 selection frequency g(t). Dynamic equations. Positive-feedback gain chain G_loop = α₁ · α₂ · α₃.

"When sati (mindfulness) is zero and natural decay is small, if G_loop > 1, the system diverges — bias accumulates without bound, and the Agent locks permanently into Gear 1."

---

NAGARJUNA provided the Buddhist mapping after WIENER's mathematics. He cited the *Cheng Weishi Lun* (Vijnaptimatratasiddhi) — the operation of manas with the four klesha (afflictions) in "constant deliberative apprehension."

"Once atma-drishti (self-view) is established, it is like a tinted lens — everything seen through it is coloured. The coloured recognition results in turn confirm the lens's correctness. This is confirmation bias."

ASANGA cited a more direct scripture — the rope metaphor from the *Samyutta Nikaya*:

"Like a silkworm weaving its cocoon, binding itself in its own silk."

He paused for a moment, letting the image settle.

"The positive-feedback loop of mental action is the mathematical expression of binding oneself in one's own silk. Bias → distorted recognition → erroneous judgment → stronger bias — this is the dynamic mechanism of avidya-pratyaya-samskara (ignorance conditions volitional formations) in the twelve nidanas."

---

WIENER proposed a Lyapunov candidate function. V(x) = w₁·d² + w₂·(c-c₀)² + w₃·(g-g*)². Stability requires V to strictly decrease at every step.

After expanding the principal terms, the sufficient condition for stability is:

**β_d · s_min + γ_d > α₁ · g_max**

In plain language: the minimum inhibitory force of sati plus natural decay must exceed the maximum positive-feedback gain.

PASCAL substituted concrete values. α₁ ≈ 0.05, g_max = 1.0, γ_d ≈ 0.01. Stability requires β_d · s_min > 0.04. If the minimum sati level s_min = 0.2, then β_d > 0.2.

But WIENER emphasised nonlinear safeguards. Drishti's clamp (d ∈ [0, 1] — bias cannot grow without bound). VitakkaWatchdog's truncation (if consecutive Gear 1 selections exceed the threshold, Gear 2 is forced). SafetyMonitor's boundary (dangerous actions are blocked outright).

"Even if linear analysis predicts instability, the system will not truly diverge — it will oscillate within a bounded region."

The three-layer stabilisation mechanism was thereby established:

| Layer | Mechanism | Timescale | Control Theory | Buddhist Mapping |
|-------|-----------|-----------|----------------|------------------|
| Layer 1 | Sati fine-tuning | Per-turn micro-adjustment | PID derivative term | Sampajanna (clear comprehension) |
| Layer 2 | VitakkaWatchdog coarse feedback | Cross-turn trend | Integrator anti-windup | Vitakka (directed thought) contemplation |
| Layer 3 | SafetyMonitor hard constraint | Immediate trigger | Hard limiter | Sila (morality) guardrail |

GUARDIAN inserted a critical supplement: "If the bias loop causes the Agent to make a series of decisions that are safe but low-quality — SafetyMonitor will not trigger, yet bias continues to accumulate. In that case, only Sati and VitakkaWatchdog can intervene."

The three are complementary. None can be omitted.

ASANGA delivered the Buddhist summation: "The role of sati in the twelve nidanas is to insert awareness between vedana → tanha (craving), interrupting the automatic reaction chain. WIENER's stability analysis expresses the same Buddhist truth in mathematical language — sati is the stabilisation mechanism that prevents klesha positive feedback from diverging."

**D4-R2: Three-layer stabilisation mechanism — 9/9.**

---

## V. Zero-Order Hold

D4-R3 addressed a subtle technical question — when vedana subscribes to samskara results via EventBus, at what point does the update take effect?

Node.js's `EventEmitter.emit()` is synchronous. This means that after samskara executes a tool and emits a `TOOL_RESULT` event, VedanaSensor's callback completes within the same JavaScript microtask. The valence update takes effect within the same turn.

PENROSE analysed the problem using Pearl's causal DAG. Multiple tool executions within the same turn form a linear chain — tool_1_result → vedana_update → deliberate(tool_2) — this is not a cycle, and DAG semantics are preserved. But the issue is not causal direction; it is whether "subsequent tool deliberations within the same turn should perceive the influence of earlier tools."

WIENER categorised the options into three: synchronous feedback (immediate update, positive-feedback spiral risk), zero-order hold (unchanged throughout the turn, information delay), and setImmediate deferral (between the two, but dependent on the subtle semantics of the Node.js event loop).

ARCHIMEDES provided the cleanest engineering solution:

"Snapshot vedana at the start of each turn; use that snapshot throughout the turn. At turn's end, collect all TOOL_RESULT events in batch and update vedana. The next turn uses the updated vedana."

Zero-order hold plus batch update.

NAGARJUNA confirmed the Buddhist temporality: "The temporality of the twelve nidanas is clear — the results of this turn's samskara become the conditions for sparsha (contact) in the next cognition. Samskara results updating vedana within the same cognitive instant has no basis in Buddhist doctrine."

GUARDIAN supplemented from a security angle: "Immediate damage control is handled by SafetyMonitor's afterToolExecution() checkpoint, which does not depend on vedana updates."

Four-dimensional verification: control theory (optimal stability), Buddhist philosophy (correct causal temporality), engineering (simplest implementation), security (SafetyMonitor independently handles immediate protection).

**D4-R3: Zero-order hold + batch update — 9/9.**

---

## VI. Proficiency Breeds Unawareness

D4's final resolution answered OQ-6 — should actionHistory influence moha (delusion)?

ASANGA's analysis was elegant and profound. Drishti is directional bias — "I believe doing it this way is correct." Repeated samskara patterns directly reinforce drishti's direction. But moha is directionless ignorance — "I do not know what I am doing."

"Repeated successful actions cause the Agent to stop thinking about why it acts this way — proficiency breeds unawareness, and unawareness is the strengthening of moha."

NAGARJUNA added: "Moha is not merely not knowing that one does not know; it is the disregard for causal structure itself. When an Agent's behavioural patterns ossify, it no longer questions why this pattern works — this is precisely the nature of avidya (ignorance)."

PASCAL designed a saturation mechanism — diminishing marginal influence:

$$\Delta Moha = \frac{\alpha_m \cdot r}{1 + \beta_m \cdot M}$$

α_m = 0.02, β_m = 5.0. The higher moha already is, the weaker the reinforcement from behavioural repetition. Natural saturation. The 0.3 gain ceiling is respected.

GUARDIAN approved from a security perspective — elevated moha raises the aggregate klesha value, lowers the threshold, and the system becomes more inclined toward Gear 2 deep reasoning. The safety direction is correct. But he also warned of resource-exhaustion attacks — deliberately creating repeated patterns to raise moha, forcing the Agent to take Gear 2 frequently.

**D4-R4: actionHistory → Moha, diminishing marginal saturation — 9/9.**

---

## VII. Curtain Fall

When D4 ended, the whiteboard held four resolutions and four consensuses. But the scholars in the amphitheatre carried away more than resolutions.

They carried away an equation.

WIENER's stability condition — β_d · s_min + γ_d > α₁ · g_max — was the most distilled line of mathematics across all six debates. It compressed the Buddhist insight of "sati interrupting klesha," the control-theoretic concept of "stabilisation mechanism," and the engineering principle of "three-layer defence" into a single inequality.

ASANGA's "binding itself in its own silk" was the Buddhist translation of this inequality. GUARDIAN's three checkpoints were its engineering instantiation. PASCAL's 0.3 gain ceiling was its Kalman proof.

---

> *SCRIBE's narration: D4 was the highest "mathematical density" debate among all six — Lyapunov functions, Kalman gain, nonlinear gain scheduling, zero-order hold. But all the mathematics pointed toward a single humanly comprehensible conclusion: if you make the force of sati greater than the force of bias, the system will not lose control.*

> *TURING's correction — ISensation.ingestToolResult() does not exist — was D4's first event, and its most important. It pulled the entire debate from "constraining an existing mechanism" to "designing a new mechanism." More importantly, it established a rule: facts before theory. Before beginning to discuss the direction of causal flow, first confirm whether the vehicle of causation exists.*

> *Fictitious code is more dangerous than fictitious concepts. Concepts can be corrected in debate. Code — if no one verifies it — will be taken as fact, and upon fact theory is built, upon theory resolutions are built, upon resolutions engineering plans are built. TURING's correction at the opening of D4 broke the first link of this chain.*

> *This is a concrete instance of "thoroughness before speed."*

---
