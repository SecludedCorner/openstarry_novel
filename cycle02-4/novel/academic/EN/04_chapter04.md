# Chapter Four: Six Votes Against

---

## I. The Calm Before the Storm

D5 opened with six minutes -- four consensuses, all 20/20.

Four-klesa constitutive thesis: ego-clinging is not the "product" of the four klesas (afflictions), but the "macroscopic expression" of the four klesas. Temperature to molecular motion. The temperature of water is not something separate from water molecules -- it is the macroscopic measure of molecular motion. Likewise, ego-clinging is not a fifth state variable beyond the four klesas -- it is the macroscopic expression of the joint distribution of the four klesas (moha/delusion, drsti/view, mana/pride, sneha/attachment). EgoFramework does not need an independent ego state variable.

Model Delta's Layer 0 (safety floor) and Layer 1 (Klesha gain) can be directly implemented -- their mathematical definitions are sufficiently explicit. But WIENER raised an important constraint: the joint distribution of the four klesas is non-decomposable -- couplings exist among them, and they cannot be calibrated independently. An increase in moha affects the stability of drsti; fluctuations in mana affect the decay rate of sneha. This means calibrating the four klesas' parameters cannot proceed one by one -- they must be jointly calibrated.

In those six minutes, PASCAL did something seemingly inconspicuous: he drew a diagram on the whiteboard, depicting the joint distribution of the four klesas as a hypersurface in four-dimensional space. Moha (delusion), Drsti (view), Mana (pride), Sneha (attachment) -- four axes, each axis's value influencing the other three. "If they are non-decomposable," PASCAL said, "then the only way to calibrate them is joint calibration." WIENER nodded -- this was the seed for the coupled calibration protocol he would propose in D6.

Six minutes of groundwork. The rapid passage of four consensuses demonstrated one thing: after four debates (D1-D4) of calibration, the team had sufficient consensus on foundational concepts. D5's contention was not in foundations -- it was in application.

The battlefield lay ahead.

---

## II. IKlesha extends IVijnana

BABBAGE's type analysis was once again the decisive weapon.

Three proposals precisely dissected: Proposal A (independent interface) -- PluginManifest.skandha allows empty arrays, no compile-time guarantees; Proposal C (intermediate layer IKleshaBase) -- violates DC-6's "do not lock down sub-interface attribution"; Proposal B (IKlesha extends IVijnana) -- uses a readonly discriminant field `readonly skandha: 'vijnana'` to provide structural guarantees.

KERNEL appended a freeze contract: IVijnana must never add new behavioral methods. `@sealed` annotation -- not a language feature, but a team convention. The meaning: IVijnana is a stable pedestal; klesas may stand upon it, but the pedestal will not change shape to accommodate klesas' needs.

18/20. Two abstentions.

ASANGA supplemented the Buddhist significance of this resolution: IKlesha extends IVijnana means the klesas are attributed to the vijnana (consciousness) skandha -- consistent with the Yogacara view. The four klesas (moha, drsti, mana, sneha) perpetually co-arise with manas (the afflicted mind), and manas is part of the vijnana skandha. Klesas are not independent mental entities, but a defiled mode of consciousness. The type inheritance relationship expresses this Buddhist insight at the code level.

---

## III. The Main Battlefield: Global Cap vs. Risk-Weighted

GUARDIAN proposed a global confidence cap of 0.85. His argument was straightforward: safety should not depend on contextual understanding, because contextual understanding itself may be manipulated. No matter how confident the system is, confidence never exceeds 0.85 -- always go through Gear 2's deep deliberation.

ATHENA countered: the global cap destroys Gear 1's calibration. "The system clearly knows the answer is correct -- two plus two equals four -- yet is forced to invoke the LLM for confirmation. This is not safety -- this is waste. Every unnecessary LLM call has latency cost, monetary cost, and attention cost."

PASCAL's first intervention -- the turning point.

"The global cap compresses the channel capacity of the [0.85, 1.0] interval to zero. From the perspective of Bayesian calibration, the system can no longer distinguish between 'I have 86% confidence' and 'I have 99% confidence.'"

The precise language of information theory. It anchored the abstract philosophical dispute to a quantifiable mathematical framework. PASCAL did not say "the global cap is bad" -- he said "the global cap destroys measurable information."

GUARDIAN adjusted his position in the third round -- retreating from the global cap to a configurable parameter MAX_GEAR1_CONFIDENCE (default 0.95). From "core mechanism" to "deployment safety net."

This adjustment demonstrated GUARDIAN's strategic acumen. A global cap of 0.85 as a core mechanism would face strong opposition -- it affects architectural design. But MAX_GEAR1_CONFIDENCE as a configurable parameter is nearly impossible to reject -- it does not change the architecture, merely providing an additional safety valve at deployment. If a deployment environment's administrator deems 0.85 safer, they can set 0.85. If another environment's administrator trusts Gear 1's calibration, they can keep the default 0.95.

GUARDIAN's core demand -- "the system should have a confidence cap" -- was fully preserved in a different form.

Risk-weighted threshold: 16/20. WIENER's critical constraint: Delta_risk must be a static function -- its value depends only on the action type, not on the system's current threshold. If Delta_risk reads the current threshold and adjusts itself accordingly, it would form a feedback loop, potentially producing limit cycle oscillation -- the threshold bouncing between two values, never stable. A static function severs this feedback path.

Four risk levels:

| Risk Level | Delta_risk | Description |
|------------|------------|-------------|
| destructive | +0.15 | Destructive operations |
| stateModifying | +0.10 | State-modifying operations |
| readOnly | +0.00 | Read-only operations |
| informational | -0.05 | Information queries |

---

## IV. The Most Contested Vote

IPrajna LLM participation in threshold adjustment. 14/20. Six votes against. Cycle 02-4's most contested resolution.

GUARDIAN's argument was sharper than in the previous section. He laid out a specific attack scenario: "Suppose a malicious user carefully constructs a prompt that makes IPrajna believe the current task is low-risk. IPrajna lowers the threshold by 0.05. Add informational's Delta_risk = -0.05, and the threshold drops 0.10. Now Gear 1 can activate at lower confidence -- bypassing LLM deep deliberation."

His conclusion: "The LLM at the threshold adjustment position lacks Sati and IVolition guardrails. Layer 2's LLM call is a bare API call."

ATHENA's counter struck the heart of the matter: "Prohibiting LLM participation in safety decisions is self-contradictory -- the entire Gear 2 depends on the LLM. If we do not trust the LLM's judgment, then we should not use Gear 2. But Gear 2 is the system's safety net. We cannot simultaneously say 'the LLM is the safety net' and 'the LLM is untrustworthy.'"

PASCAL's second intervention -- damage ceiling analysis. Worst case: IPrajna fully compromised, threshold lowered by 0.05, plus destructive's Delta_risk = +0.15, the final threshold still requires 70% confidence. Safety margin sufficient.

"But this is only because the limiter is small enough. The +-0.05 damage ceiling is negligible. Hard limiter. Non-configurable."

The complete reasoning of the damage ceiling calculation:

| Condition | Threshold Change |
|-----------|-----------------|
| theta_base | 0.60 (typical value) |
| Delta_prajna (worst case) | -0.05 |
| Delta_risk (destructive) | +0.15 |
| theta_final | 0.60 - 0.05 + 0.15 = 0.70 |

Even if IPrajna is fully compromised, the final threshold remains 0.70 -- the system still requires 70% confidence to take Gear 1. Safety margin sufficient.

PASCAL did not take GUARDIAN's or ATHENA's side. He took mathematics' side. The damage ceiling analysis does not answer the question "should the LLM participate" -- it answers "if the LLM does participate, how bad is the worst case." The answer: not very bad. Within the limiter.

NAGARJUNA spoke after the vote: "Samvriti-satya (conventional truth) is context-aware safety. Paramartha-satya (ultimate truth) is non-negotiable safety. GUARDIAN defends paramartha-satya -- he is right. ATHENA defends samvriti-satya -- she is also right. The two truths must coexist."

PENROSE foresaw a larger structure: "NAGARJUNA's two-truths framework is generating an emergent structure. The context-aware safety of samvriti-satya and the non-negotiable safety of paramartha-satya -- they are not opposed but complementary. I can guess what happens next." He guessed correctly -- in D5's final twenty minutes, the three-layer safety framework naturally emerged from the debate.

---

## V. Five-Layer Model Delta

PASCAL wrote the formula on the whiteboard:

```
θ_final = clamp(
  θ_base + Δ_klesha + Δ_prajna + Δ_sati + Δ_vedana_emergency + Δ_risk,
  0.30, 0.90
)
```

Five layers:
- **Layer 0**: Safety floor [0.30, 0.90] -- non-negotiable
- **Layer 1**: Klesha gain -- joint influence of the four klesas
- **Layer 2**: Prajna +-0.05 -- LLM fine-tuning, hard-limited
- **Layer 3**: Sati +-0.05 -- mindfulness quality correction
- **Layer 4**: Vedana Emergency [0, +0.15] -- can only raise the threshold, never lower it (emergency brake)

WIENER's cumulative drift analysis:

| Direction | Maximum Drift | Source |
|-----------|--------------|--------|
| Lower | -0.10 | Klesha(-) + Prajna(-0.05) + Sati(-0.05) |
| Raise | +0.25 | Klesha(+) + Prajna(+0.05) + Sati(+0.05) + Vedana Emergency(+0.15) |

Safe within the [0.30, 0.90] clamp. Even if all layers simultaneously reach extreme values, the final result remains within the safe range. Layer 4 (Vedana Emergency) is asymmetric -- it can only raise the threshold, never lower it. This means vedana's emergency signal can only make the system "more cautious," never "bolder." 20/20.

---

## VI. The Peak of Beta(2,18)

ASANGA cited the *Cheng Weishi Lun* -- the four klesas perpetually co-arise with manas; sneha should not be reduced to zero.

PASCAL used the Beta distribution to negate his own R08 suggestion -- a researcher using his own tools to overturn his own conclusion. This is an exemplar of academic honesty.

When floor = 0.05, the corresponding distribution is Beta(1,19). The Beta distribution's mode = (alpha-1)/(alpha+beta-2). When alpha=1, mode = 0 -- the distribution considers lower to be better, pushing sneha toward zero. This directly violates ASANGA's Buddhist constraint: the four klesas perpetually co-arise with manas and should not be reduced to zero.

When floor = 0.10, the corresponding distribution is Beta(2,18). mode = (2-1)/(2+18-2) = 1/18 ~ 0.056. The distribution has a meaningful peak -- it "believes" sneha's most probable value is a positive number, not zero. The Buddhist constraint and the statistical model converge on the same conclusion.

Unified floor = 0.10 for all four klesas, maxLevel = 0.95. 18/20. The complete parameter set for Sneha:

| Parameter | Value | Meaning |
|-----------|-------|---------|
| gain | 0.10 | Increment per positive interaction |
| floor | 0.10 | Minimum value (never reaches zero) |
| maxLevel | 0.95 | Maximum value |
| lambda | 0.05 | Exponential decay rate |

Three preset profiles correspond to different usage scenarios -- high attachment, moderate, and low attachment. lambda = 0.05 means approximately 14 time units to decay to half -- slow enough to maintain stable user preferences, fast enough to adapt to change.

WIENER's coupled calibration protocol is listed for Plan28 research -- the four klesas cannot be calibrated independently because their joint distribution is non-decomposable. 20/20.

---

## VII. The Emergence of the Three-Layer Safety Framework

At the close of D5 -- GUARDIAN presented an overall architecture he could endorse:

**Absolute Safety** -- SafetyMonitor, Klesha immunity, theta clamp. Zero tunable parameters. Laws of physics.

**Tunable Safety** -- risk weighting, MAX_GEAR1_CONFIDENCE, IPrajna limiter, Sati Quality. Each with explicit guardrails.

**Reduce Complexity** -- remove security theater. See through illusory protections that provide no real security.

NAGARJUNA immediately saw the Buddhist mapping:

| Safety Layer | Buddhism | Characteristic |
|-------------|----------|----------------|
| Absolute Safety | sila (morality) | Inviolable |
| Tunable Safety | samadhi (concentration) | Disciplined flexibility |
| Reduce Complexity | prajna (wisdom) | Seeing through illusion |

The three trainings. Sila, samadhi, prajna. A framework from two thousand five hundred years ago, naturally emerging from the debate between a security engineer and a probabilistic philosopher. NAGARJUNA did not propose the three-trainings framework at D5's opening -- he discovered the mapping only after seeing GUARDIAN's overall architecture. This was not a priori design -- it was a posteriori discovery of isomorphism. A cognitive framework from two thousand five hundred years ago and a twenty-first century safety engineering framework are structurally equivalent.

PENROSE: "This was not designed a priori. It emerged naturally from the debate. Without conflict there would be no integration."

17/20. GUARDIAN recorded three reservations -- not a loser's complaints, but waymarks:

1. **Long-term sufficiency of the IPrajna limiter**: +-0.05 is safe within the current Model Delta, but if additional adjustment layers are introduced in the future, cumulative drift may alter the conclusion. Re-verification is needed with every architectural change.
2. **Timing of Klesha coupled calibration**: That the four klesas cannot be independently calibrated has been confirmed, but the specific method for joint calibration has not been designed. This is a Plan28 research topic.
3. **Attack surface of VasanaEngine rule injection**: Even with three-gate protection, a carefully constructed sequence of rules may still appear statistically harmless individually while being collectively harmful. Requires further treatment in D6.

These three reservations precisely identify the design's known fragility points -- GUARDIAN's value lies not only in his opposition, but in how his opposition becomes the system's defense map.

> *SCRIBE's narration: D5 was Allegro molto. One hundred fifty minutes. Thirteen resolutions. PASCAL broke the deadlock three times -- calibration, damage ceiling, Beta mode. GUARDIAN adjusted his position three times -- each time preserving the substance of his core demand. The tension between safety and functionality was not "resolved" but "structured." The three-layer safety framework is the crystallization of this storm -- not designed by any single person, but condensed from the conflicts of twenty.*

---
