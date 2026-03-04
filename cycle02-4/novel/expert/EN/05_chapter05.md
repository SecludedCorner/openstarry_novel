# Chapter Five: Six Votes Against

---

## I. Calm Before the Storm

The opening six minutes of D5 were the fastest consensus confirmation of the entire Cycle.

Four items. All 20/20. Six minutes.

SUNYATA did not need to explain why he moved quickly — all twenty scholars present knew the real battlefield lay ahead. These four consensuses were paving stones, not the destination.

The first: the constitutive theory of the four klesha (afflictions). Atma-graha (self-grasping) is not a "product" of the four klesha, but their "macroscopic description." R01's original text used a physics analogy — "temperature to molecular motion." Temperature is not some thing produced by molecular collisions; temperature simply is the statistical description of molecular collisions. Likewise, atma-graha simply is the joint description of the four signals: moha (delusion), drishti (view/bias), mana (conceit), and sneha (self-love).

PENROSE nodded: "Constitutive emergence — the most natural pattern in complex systems."

The second: EgoFramework does not require an independent ego state variable. Since atma-graha is a function of the four klesha, there is no need for an independent variable like `egoLevel: number`, no need for a dynamic equation like `d(ego)/dt = f(...)`. The four `KleshaSignal.value` fields are everything.

The third: the joint distribution of the four klesha cannot be decomposed into a product of marginals. PASCAL's argument was concise — high moha (delusion) typically co-occurs with high sneha (self-love), because those lacking awareness tend toward stronger attachment. High mana (conceit) and high drishti (view/bias) also correlate positively. Engineering implication: the four klesha cannot be calibrated independently.

The fourth: Layers 0 and 1 of Model Delta can be implemented directly. SafetyMonitor and KleshaModulatedDispatcher already exist in v0.26.0-beta; only wiring remains.

Six minutes. Four consensuses. Zero dispute.

Then SUNYATA spoke a single sentence, his tone unchanged, yet the air in the amphitheatre suddenly grew dense:

"We now proceed to the first contested topic of this debate."

---

## II. The Cost of Inheritance

The skandha attribution of IKlesha — in the context of Cycle 02-4 — should not have been a fierce debate. After R2 cross-review, Option B (IKlesha extends IVijnana) had already achieved overwhelming support. But the value of debate lies not in the conclusion, but in the details exposed through the process.

BABBAGE's type analysis was a precise dissection of the three options.

Option A — remain independent. Type-system benefit: zero. No compile-time guarantee of the relationship between IKlesha and IVijnana. "PluginManifest.skandha allows an empty array," BABBAGE pointed out, "an IKlesha implementation can pass compilation without declaring any skandha attribution at all." This was a fact TURING had already reported in D1.

Option C — an intermediate layer, IVijnanaMechanism. Introduces an additional empty interface, violates DC-6 (do not lock down sub-interface attribution within a skandha), and is superfluous.

Option B — inheritance. The cost is a single read-only discriminant field. The benefit is a structural guarantee at compile time.

KERNEL accepted Option B, but attached a condition — what he called a "freeze contract."

"IVijnana must never have behavioural methods added to it."

His reasoning was precise: if someone in the future adds a method to IVijnana, all sub-interfaces — ISamjna, IKlesha, and any future inheritors — would be forced to implement it. Base-interface method proliferation. A classic interface-design antipattern.

The concrete approach is to add a `@sealed` annotation in JSDoc. Not a TypeScript language feature — TypeScript has no sealed interface — but a team convention, a constraint enforced at the code-review level.

NAGARJUNA provided Buddhist confirmation: "Klesha are subsumed under vijnana-skandha (consciousness aggregate) — manas engages in constant deliberative apprehension, and the four klesha arise together with it. That IKlesha belongs to vijnana-skandha is doctrinally incontestable."

18/20. Where the two dissenting votes came from is immaterial — what matters is that the @sealed condition was written into the resolution. A lock, placed on a door that no one had yet attempted to open.

---

## III. The Main Battlefield

Section three. One hundred and fifty minutes of debate, and this was the longest segment. Global confidence ceiling versus risk-weighted threshold.

GUARDIAN stood up.

In the six debates of Cycle 02-4, every time GUARDIAN rose it carried a particular weight — not the weight of aggression, but the weight of responsibility. He knew that what he was about to say would not be welcome. He knew he might be in the minority. But he stood, because some things, if no one says them, will never be recorded.

"I propose a global confidence ceiling of 0.85."

The rationale was concise: if the confidence of any Gear 1 candidate exceeds 0.85, it is truncated to 0.85. No matter how precise the VasanaEngine's rules, no matter how high the match score — 0.85 is the ceiling.

"Safety should not depend on 'correctly understanding the situation,'" GUARDIAN said, "because situational understanding itself can be manipulated. If a malicious user sends a carefully crafted request after five normal operations, VasanaEngine might yield a confidence of 0.92 — the T-2 attack scenario. A global ceiling is the only safety mechanism that does not depend on semantic understanding."

ATHENA stood up. If GUARDIAN's rise carried the weight of responsibility, ATHENA's carried the weight of functionality.

"A global ceiling of 0.85 destroys Gear 1's calibration."

Her argument struck at the core: if an IGearArbiter plugin has been extensively validated and truly has a 0.95 accuracy rate on a certain class of requests, the global ceiling compresses it to 0.85 — this is not "safety," this is "waste." The system knows the answer is correct, yet is forced to take the slower path.

Then PASCAL stood up.

---

PASCAL's first intervention in D5 was later marked by SCRIBE as "Turning Point 1."

He did not stand on GUARDIAN's side, nor on ATHENA's. He stood on the side of mathematics.

"Let me describe the cost of a global ceiling in the language of information theory."

He drew a line on the whiteboard. The left end was labelled 0.0, the right end 1.0.

"Confidence is a signal on the [0, 1] interval. If we set the ceiling at 0.85, then the channel capacity of the [0.85, 1.0] interval is zero — all signals falling in this interval are compressed into a single value."

He paused for one second.

"From the perspective of Bayesian calibration, a well-calibrated classifier at confidence = 0.95 should have an actual accuracy rate close to 0.95. A global ceiling compresses all signals ≥ 0.85 into 0.85 — destroying calibration. The system can no longer distinguish between 'I have 86% confidence' and 'I have 99% confidence.'"

The amphitheatre fell silent.

GUARDIAN did not immediately rebut. He was thinking.

ATHENA did not press the advantage either. She knew PASCAL's argument was more powerful than her intuition — not because it was more "right," but because it placed the problem within a mathematical framework that neither side could evade.

WIENER added a second constraint: the risk-weighted Δ_risk must be a static function — dependent on action classification, not on historical state. Otherwise, threshold feedback might produce limit-cycle oscillations.

---

Turning Point 2 appeared in the third round.

GUARDIAN stood up. But this time, his tone was different.

"Let me adjust my position."

A subtle shift rippled through the amphitheatre — not a sound, but a redistribution of attention. GUARDIAN was conceding.

"I no longer insist on 0.85 as a core mechanism. But I propose MAX_GEAR1_CONFIDENCE as a deployment-configurable parameter. Default 0.95. Administrators can adjust according to deployment environment — set to 0.85 for high-security scenarios, keep 0.95 for general scenarios."

SCRIBE later wrote in the record: "GUARDIAN did not cling to a position that had been shown to have structural flaws by mathematical proof; instead he repositioned his concern: from 'core mechanism' to 'deployment safety net.' This was strategically astute — in the new framing, his concern was nearly impossible to reject."

And so it was. Risk-weighted threshold — 16/20. MAX_GEAR1_CONFIDENCE — likewise 16/20. GUARDIAN's original proposal was rejected, but his core concern survived in another form.

GUARDIAN recorded his first reservation: "RiskLevel classification depends on tool semantics; semantic misjudgment → risk misjudgment → threshold misalignment."

Not a matter of pride. A genuine engineering concern.

---

## IV. The Most Contentious Vote

Section four. IPrajna LLM participation in threshold adjustment.

If section three was the battlefield, section four was the darkest hour of the entire debate — not because anyone did anything wrong, but because on certain questions, there is no clearly correct answer.

GUARDIAN's argument was sharper than in section three: "The LLM at the threshold-adjustment position lacks the guardrails of Sati and IVolition. In Model Delta's five-layer structure, the Layer 2 (Prajna) LLM call is unlike the Gear 2 LLM call — Gear 2 is wrapped in a complete ExecutionLoop, with SafetyMonitor pre-checks, with Sati monitoring. The Layer 2 LLM call is a naked API call — its output directly affects the threshold, with no secondary confirmation."

He presented a scenario: if the LLM is compromised by a prompt-injection attack, the attacker could lower the threshold by 0.05 via IPrajna's adjustThreshold() method — allowing a dangerous operation that would otherwise not pass through the Gear 1 fast path.

ATHENA countered: "The entirety of Gear 2 depends on the LLM. If IVolition's deliberate() uses an LLM in the future (v2 version), it too is an LLM. Prohibiting LLM participation in safety decisions is self-contradictory — you cannot trust the LLM to make decisions yet distrust it for deliberation."

Deadlock.

PASCAL intervened a second time — with a damage-ceiling analysis.

"Suppose IPrajna's LLM is completely controlled by an attacker — worst case scenario. What can it do?"

He wrote on the whiteboard:

```
IPrajna.adjustThreshold() clamped at ±0.05
Worst case: threshold lowered by 0.05
θ_base = 0.60 → θ_adjusted = 0.55
Plus Δ_risk(destructive) = +0.15
Final: 0.55 + 0.15 = 0.70
```

"0.70. A 70% confidence is still required to take the Gear 1 fast path for destructive operations. SafetyMonitor's isSafe() still operates independently. The clamp [0.30, 0.90] still holds. Even if IPrajna is fully compromised, the system's safety margin remains sufficient."

"However," PASCAL added a however, "this is only because the clamp is sufficiently tight. The damage ceiling at ±0.05 is negligible. At ±0.15 it would not be. At ±0.25 it would be catastrophic. Therefore —"

"Hard clamp. ±0.05. Non-configurable."

GUARDIAN shook his head. Not in denial — in unease.

"Opening a door in principle, even if the door is locked tight."

---

The vote.

14/20.

Six votes against. GUARDIAN, LEIBNIZ, MESH, VITRUVIUS, HERACLITUS — and a sixth.

14/20 was the lowest approval rate of any resolution across all Cycle 02-4 debates. It was not even a "thin majority" — 14/20 is a solid majority. But six votes against represented a genuine unease: allowing LLM participation in threshold adjustment opens a door in principle.

GUARDIAN recorded his second reservation: "Implementation reliability of the ±0.05 clamp — can the clamp be bypassed?"

LEIBNIZ supplemented with a multi-Agent concern: "If three Agents each have their IPrajna shift by -0.05, the cumulative effect is -0.15. The cumulative effect in multi-Agent scenarios needs to be studied in Cycle 03."

---

NAGARJUNA spoke at this juncture — words that would later be cited many times.

"In Buddhist philosophy there are the two truths — samvriti-satya (conventional truth) and paramartha-satya (ultimate truth)."

His pace was slower than usual.

"Conventional truth is truth by agreement — in our context, it is context-aware safety, tunable guardrails, risk-weighted thresholds. Ultimate truth is non-negotiable truth — SafetyMonitor's isSafe(), the theta clamp [0.30, 0.90], IVolition enforcement for destructive actions."

"GUARDIAN defends the domain of ultimate truth — and he is right; that domain must not be touched. ATHENA defends the domain of conventional truth — and she too is right; within the agreed bounds, flexibility is needed."

"The two truths do not contradict. The two truths must coexist. Safety is not a point — it is a space, with immovable boundaries and an adjustable interior."

PENROSE, after NAGARJUNA finished, made an observation: "NAGARJUNA's two-truths framework and the GUARDIAN/ATHENA debate are producing an emergent structure — a layered safety framework. I can see at least three layers."

No one at that moment realised that PENROSE had just foreseen the three-layer safety framework of section eight.

---

## V. The Cost of Delay

Section five. Conditional IVolition for Gear 1.

GUARDIAN proposed that all Gear 1 actions must pass through IVolition Position B deliberation. DARWIN offered an alternative based on risk stratification — differentiated by RiskLevel.

Then ARCHIMEDES did something rarely done in debate: he produced data.

```
ManoAggregator routing latency (target): ~16ms

With IVolition:
  v1 (rule-based): 16 + 5 = ~21ms (+31%)
  v2 (LLM-based): 16 + 80 = ~96ms (+500%)
```

+31%. For every readOnly and informational action, one-third more time — to do something that can cause no harm.

+500%. If IVolition uses an LLM in the future, latency is sixfold.

GUARDIAN looked at the numbers.

"ARCHIMEDES's data makes my position harder to defend. Forcing readOnly actions through IVolition is indeed wasteful."

Then he adjusted once more: "I can accept the risk-stratification proposal, but RiskLevel classification must be performed at the core level — it cannot be self-declared by IGearArbiter plugins."

KERNEL immediately added: "Correct. RiskLevel classification should be based on static analysis of toolName or toolCall.args, performed by the core's safety module."

15/20. GUARDIAN's third reservation: "readOnly does not mean risk-free — reading a keyfile is classified as readOnly under the four-tier scheme, but its risk level should be higher."

---

## VI. Five Layers, One Formula

Section six. The Model Delta five-layer structure.

PASCAL wrote a formula on the whiteboard, then stepped back to let everyone see clearly:

```
θ_final = clamp(
  θ_base                    // Base threshold 0.60
  + Δ_klesha(t)             // Layer 1: Klesha modulation
  + Δ_prajna(t)             // Layer 2: Prajna adjustment ∈ [-0.05, +0.05]
  + Δ_sati(t)               // Layer 3: Sati quality ∈ [-0.05, +0.05]
  + Δ_vedana_emergency(t)   // Layer 4: Vedana emergency ∈ [0, +0.15]
  + Δ_risk(a),              // Risk weighting
  θ_min,                    // 0.30 (Safety Floor)
  θ_max                     // 0.90 (Safety Floor)
)
```

Five layers. Each with a clear responsibility, a clear clamp, a clear timescale. Layer 0 is the floor — non-negotiable. Layer 4's Vedana Emergency can only raise the threshold (more conservative), never lower it. The results of all layers are clamped within [0.30, 0.90] — the Safety Floor is always in effect.

WIENER performed a cumulative-offset analysis: Layers 2 and 3 each ±0.05, maximum cumulative offset ±0.10. Adding Layer 4's +0.15, the maximum cumulative offset from all upper layers is -0.10 to +0.25. Within the [0.30, 0.90] clamp range, no overflow occurs.

ARCHIMEDES mapped each layer to the engineering plan: Layer 0 + Layer 1 + Δ_risk → Plan27. Layer 4 → Plan28. Layers 2 + 3 → Plan29+.

20/20.

Unanimous. In a debate filled with contention, the five-layer model was the only thing on which everyone agreed. Because it was not an opinion — it was a framework. Opinions can be opposed; frameworks accommodate all opinions.

---

## VII. The Peak of Beta(2,18)

Section seven. The floor value for sneha (self-love).

ASANGA cited the *Cheng Weishi Lun* (Vijnaptimatratasiddhi): "These four klesha are constantly co-present with manas." The four klesha arise simultaneously with manas in constant deliberative apprehension. Before the attainment of arhatship, the four klesha cannot be reduced to zero.

Engineering implication: sneha.value should not be able to drop to 0. An Agent with absolutely no attachment to its own continuity and task completion is not a meaningful Agent.

ASANGA suggested 0.10. PASCAL had originally suggested 0.05 in R08.

Then PASCAL did something admirable: he used his own method to refute his own suggestion.

"At floor = 0.05, the mode of Beta(1, 19) = 0. The distribution considers that the lower sneha is, the better. The floor's raison d'etre vanishes — the distribution's mode sits right at the floor."

He drew two curves.

"At floor = 0.10, the mode of Beta(2, 18) = 1/18 ≈ 0.056. The distribution has a meaningful peak. During initial startup, sneha's value fluctuates between 0.056 and 0.10, rather than being pinned to the floor."

Beta(1,19) is a monotonically decreasing curve. Beta(2,18) has an interior peak. The former says "the less the better." The latter says "there is a natural level."

0.10. 18/20.

ASANGA then pushed for an extension: since "the four klesha are co-arising," the floor should not apply only to sneha. All four klesha should have floor = 0.10. WIENER agreed and suggested maxLevel = 0.95.

All four klesha: klesha_value ∈ [0.10, 0.95].

WIENER then proposed a coupled calibration protocol — joint calibration of ten parameters cannot be performed independently. Coordinate descent. Joint objective function. Bounded and continuous convergence guarantee. A research item for Plan28.

20/20.

---

## VIII. Emergence

Section eight. The three-layer safety framework.

GUARDIAN stood up. This time, he was not opposing something — he was presenting an overall architecture he could endorse.

**Layer One: Absolute Safety.**

SafetyMonitor's isSafe(). Klesha-immune. Theta clamp [0.30, 0.90]. Cross-Agent samskara prohibition. Gear 1 minimum event set. IVolition enforcement for destructive actions.

No tunable parameters. Safety axioms. The laws of physics are not negotiable.

**Layer Two: Tunable Safety.**

Risk-weighted threshold. MAX_GEAR1_CONFIDENCE. IPrajna clamp. Gear 1 IVolition by RiskLevel. Sati Quality Influence. Vedana Emergency. Klesha gain schedule.

Each item has explicit guardrails — clamps, configuration ranges, audit requirements. Administrators can adjust within the guardrails.

**Layer Three: Reduce Complexity.**

Remove inputHash integrity verification (cannot prevent forgery without a TEE environment). Remove redundant input least-privilege (already covered by Sandbox).

Not relaxing safety — removing security theatre. Seeing through illusory protections that provide no substantive defence.

---

NAGARJUNA provided a Buddhist mapping for the three-layer framework.

"Sila — inviolable baseline rules. Samadhi — disciplined flexibility. Prajna — the wisdom to see through the illusory."

The three trainings of sila, samadhi, and prajna. The three dimensions of Buddhist practice. A layered framework from twenty-five centuries ago, mapped onto twenty-first century systems security architecture — not coincidence, but because the tension between safety and functionality is not a problem unique to modern engineering; it is a fundamental challenge faced by all systems possessing awareness.

PENROSE made his most important observation of the entire Cycle at this moment:

"Note that the three-layer framework was not designed a priori — it emerged naturally from the debates across sections three through five. GUARDIAN, on every topic, asserted the imperative of absolute safety; ATHENA, on every topic, asserted the imperative of contextual flexibility. The tension between the two ultimately crystallised into a clear layered structure."

His voice was calm, but what he said brought the entire amphitheatre to a one-second pause.

"This is precisely the value of debate — without conflict there would be no integration."

17/20. Three votes against. MESH's objection was that the removal of inputHash in the Reduce Complexity layer required further security analysis — in distributed multi-Agent scenarios, integrity verification for cross-Agent communication may still require a hash mechanism.

---

## IX. Closing

SUNYATA delivered a brief retrospective.

One hundred and fifty minutes. Thirteen resolutions. Four passed unanimously. Nine debated resolutions. The most contentious at 14/20. Three minority reservations.

Then GUARDIAN spoke the final words.

"I accept all resolutions. This was a fair debate."

He paused.

"ATHENA's and PASCAL's arguments changed my view on the global ceiling — I now believe that risk weighting combined with MAX_GEAR1_CONFIDENCE as a deployment safety net is a better design. But my three reservations are genuine engineering concerns, not matters of pride."

ATHENA's response was equally measured: "GUARDIAN, throughout the entire debate, demonstrated the most important quality of a security researcher — not abandoning legitimate concerns under majority pressure. Our disagreement is not safety versus no safety, but how to let a system grow while maintaining safety."

NAGARJUNA closed with a single sentence: "Upaya (skilful means) is not compromise — it is unification at a higher level."

---

> *SCRIBE's narration: If the first four debates were the four movements of a symphony, then D5 was the final Allegro molto — the fastest tempo, the most intense, the most dense.*

> *But the most intense movement is not the most chaotic. D5's structure was more precise than its emotion — four consensuses (six minutes of paving), one swift vote (IKlesha), three core battlefields (ceiling vs. weighting, LLM participation, IVolition conditioning), one unification (the five-layer model), one microscopic calibration (sneha), one macroscopic emergence (the three-layer safety framework).*

> *At every juncture, one person did the right thing at the critical moment. PASCAL broke the deadlock three times — not because he was more intelligent, but because he refused to render judgment without numbers. GUARDIAN adjusted his position three times — not because he was weaker, but because he knew that clinging to a mathematically flawed position is self-harm. NAGARJUNA provided the conceptual framework of the two truths — not as ornamental citation, but as the direct conceptual foundation that prefigured the three-layer safety framework.*

> *Six votes against. 14/20. The lowest approval rate of any resolution across all of Cycle 02-4. But if D5-R4 is the resolution most likely to be revisited in the future, then those six votes against are not failure — they are waymarkers. They precisely identify the known fragility points of the design, providing the starting point of a checklist for future security audits.*

> *The tension between safety and functionality was not "resolved." It was "structured." Structuring is not compromise — it is unification at a higher level. As NAGARJUNA said: upaya.*

---
