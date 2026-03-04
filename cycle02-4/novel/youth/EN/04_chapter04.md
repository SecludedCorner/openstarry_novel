# Chapter Four: Six Votes Against

---

## Before the Storm

The first six minutes of the fifth debate (D5) were quiet. Four consensus items, all 20/20.

The most important one: ego-clinging is not an independent thing.

It's the combined effect of four klesa (afflictions) -- just like temperature isn't something separate from water molecules; it's the macroscopic manifestation of molecular motion. You don't need a "thermometer" to store temperature -- you just need to know how the molecules are moving. Likewise, you don't need an "ego module" -- you just need to track four afflictions, and ego-clinging naturally emerges.

There was also a technical resolution: IKlesha (the affliction interface) inherits from IVijnana (the consciousness interface). BABBAGE used type analysis to prove that if klesa doesn't inherit from vijnana, orphan objects appear in the type system. In plain language: afflictions must "belong to" some skandha; they can't be homeless drifters.

Six minutes of paving. The storm was coming.

---

## Global Cap vs. It Depends

GUARDIAN proposed a safety measure: no matter how confident the system is, confidence never exceeds 0.85. Deep deliberation by the LLM is always required.

His reasoning: safety should not depend on the system's own understanding of the situation -- because the understanding itself could be wrong.

ATHENA countered: "The system clearly knows that two plus two equals four, yet it's forced to ask the LLM 'Is two plus two four?' That's not safety; that's waste."

PASCAL said one sentence that broke the deadlock.

"A global cap compresses the channel capacity between 0.85 and 1.0 to zero. The system can't distinguish 'I'm 86% confident' from 'I'm 99% confident.'"

In plain language: if you decree that the highest possible exam score is 85, then a student who scored 86 and one who scored 100 look identical on the transcript. You've lost the ability to differentiate.

GUARDIAN was smart -- he didn't cling to his position. He changed "global cap" to "configurable cap parameter" (default 0.95). Meaning: the deployer can decide whether to set a cap. Architecture unaffected. A deployment-time safety valve, not a core mechanism.

Then came risk-weighted thresholds -- different types of actions get different bars:

| Action type | Extra threshold | What it's like |
|-------------|----------------|---------------|
| Destructive | +0.15 | Deleting files -> must be very sure |
| State-modifying | +0.10 | Changing settings -> must be fairly sure |
| Read-only | +0.00 | Just looking -> normal threshold |
| Informational | -0.05 | Asking a question -> slightly lower bar |

16/20 passed.

---

## The Most Controversial Vote

14/20. Six votes against. The most controversial resolution of Cycle 02-4.

The question: let the LLM fine-tune decision thresholds?

GUARDIAN: "LLM invocations are bare API calls -- no safety guardrails. If the LLM is manipulated, it can lower the threshold."

ATHENA: "Banning the LLM from participating in safety decisions is self-contradictory -- the entire Gear 2 depends on the LLM. You can't say the LLM is a safety net on one hand and say the LLM is untrustworthy on the other."

PASCAL did the math. He didn't say "I think it's safe" or "I think it's not safe." He said: "Let's calculate."

Imagine the worst case: the LLM is fully compromised. It lowers the threshold by 0.05. But the risk weight for destructive actions is +0.15. So the net effect is +0.10 -- the threshold is actually higher. Even in the mildest case (informational, -0.05), adding the LLM's -0.05, the threshold only drops by 0.10, still requiring 70% confidence. Safety margin holds.

"But -- only because the clamp is small enough. +/-0.05. Hard clamp. Non-configurable."

PASCAL didn't take anyone's side. He took math's side.

NAGARJUNA said after the vote: "GUARDIAN defends absolute safety -- no compromise. ATHENA defends contextual safety -- adapting to circumstances. The two must coexist."

---

## Five-Layer Cake

PASCAL drew a formula on the whiteboard -- the five-layer structure of the decision threshold:

Bottom layer (Layer 0): safety floor. No matter what, the threshold cannot go below 0.30 or above 0.90. Like the safety cable in an elevator -- no matter which button you press, the cable is there.

Layer 1: influence of klesa. The joint effect of four afflictions -- drsti (view), sneha (attachment), mana (pride), and moha (delusion). The heavier the afflictions, the higher the threshold -- just as the more anxious you are, the more cautious you become when making decisions.
Layer 2: LLM fine-tuning. +/-0.05. Small enough to almost ignore, but preserving the LLM's ability to participate in adjustment.
Layer 3: sati quality correction. +/-0.05. High sati quality allows the threshold to dip slightly (more trust in observations); low quality nudges it up.
Layer 4: vedana emergency signal. Can only raise the threshold (+0.15), never lower it. Like an emergency brake -- you can only press it, not release it.

WIENER verified: even if all layers simultaneously hit their extreme values, the final result stays within the safe range.

This means: even the worst case won't spiral out of control. This isn't "probably safe." This is "mathematically proven safe." 20/20.

---

## Should Not Reach Zero

ASANGA cited a classical Buddhist text: the four afflictions are always present with manas (the self-referencing mind). Sneha (attachment) should not reach zero.

PASCAL supported this view with statistics. Using Beta distributions for the analysis -- if sneha's floor is set at 0.05, the statistical model says "the lower the better, ideally zero." But if the floor is set at 0.10, the statistical model says "the most likely value is about 0.056 -- a positive number."

In plain language: a floor of 0.05 is too low -- statistically, the optimal solution trends toward zero, meaning the floor is effectively meaningless. A floor of 0.10 is just right -- statistically, the optimal solution is a positive number, giving the floor real significance.

Buddhism and statistics converged on the same conclusion: sneha's floor is 0.10. It should not reach zero. 18/20.

Interestingly, PASCAL was negating his own earlier suggestion. In his R08 report, he recommended floor = 0.05, but the Beta distribution told him 0.05 doesn't work.

A researcher using his own tools to overturn his own conclusion. This isn't embarrassing. This is science. Science doesn't mean "I'm always right." Science means "when the evidence tells me I'm wrong, I change."

---

## Three-Layer Safety Framework

In D5's final twenty minutes, something emerged that nobody had designed in advance.

GUARDIAN stepped back, looked at all the resolutions on the whiteboard, and suddenly saw an overarching structure:

**Layer One**: absolute safety -- non-adjustable hard constraints. Like the laws of physics.
**Layer Two**: adjustable safety -- flexible parameters with guardrails. Like traffic rules.
**Layer Three**: reducing complexity -- removing false security that provides no real protection. Like tearing down useless fences.

NAGARJUNA instantly saw the Buddhist mapping: sila (precepts) -- must not be violated. samadhi (concentration) -- disciplined flexibility. prajna (wisdom) -- seeing through illusion.

Three layers. Not one. Safety isn't a monolith. Some safety is absolute (you must never kill). Some safety is relative (speed limits depend on road conditions). Some "safety" is actually illusory (removing useless fences actually makes things safer).

A framework from two thousand five hundred years ago, naturally emerging in today's debate. Nobody designed it in advance. PENROSE later said: "Without conflict, there would be no integration. If D5 hadn't had GUARDIAN and ATHENA's opposition, the three-layer framework would never have appeared."

17/20. GUARDIAN recorded three reservations -- not a loser's complaints, but waymarks. Precisely marking the design's known weaknesses. These waymarks will be examined one by one in future Cycles.

> *SCRIBE's narration: D5 took one hundred and fifty minutes. The longest debate. Thirteen resolutions. PASCAL broke deadlocks three times. GUARDIAN adjusted his position three times -- but each time preserved his core concern. The tension between safety and functionality wasn't "resolved" -- it was "structured."*

---
