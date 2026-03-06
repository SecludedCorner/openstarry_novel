# Epilogue: Two Languages

---

The amphitheater's light was adjusted back from 6500K to 4000K.

Not the amber of Cycle 02-4's ending — that was too warm, belonging to another era. Nor the surgical cold white of today's beginning — that had served its purpose. 4000K was neutral white. Neither cold nor warm. Like a workshop that had been cleaned — tools put away, floor swept, waiting for the next occupant.

SUNYATA was the last to leave the control console. He stood before the whiteboard for a while. The whiteboard had been wiped clean — all the writing from D1 through D5, the voting records, the interface definitions, the renaming tables — all transcribed into documents, then erased from the whiteboard.

But one line he did not erase. He deliberately left it.

> **Test 4: When you use a Buddhist Sanskrit term as a code identifier, the component's function must match the term's Buddhist definition. If inconsistent, use engineering terminology.**

---

## I. Two Languages

Cycle 02-5's core was not any particular resolution. Not ILoopQualityMonitor, not IConfidenceAuditor, not Doc 45's Five-Skandha OOP Architecture.

The core was the answer to a question.

The question: in a system that simultaneously uses two languages — Buddhist and engineering — where is the boundary between them?

D1 through D5 took six and a half hours to answer this question. The answer can be condensed to a few lines:

**Buddhist language is appropriate in three places:**

1. **Code identifiers** — when Buddhist terms have become part of the source code and function matches definition. Moha is self-delusion — the Moha module genuinely simulates self-delusion. Skandha is aggregate — the Skandha types in the code genuinely classify the five aggregates. These names passed Test 4. The scale balanced.

2. **Design rationale** — when Buddhist concepts actually drove engineering decisions, with DC confirmation. "Vasana is acquired conditioning" drove the VasanaEngine externalization decision. "Four afflictions co-arise simultaneously" drove the MulaKleshaBundle atomicity design. There was a causal relationship between Buddhist concepts and engineering decisions. These were not decoration — they were rationale.

3. **Independent mapping documents** — when the document's raison d'etre is to provide systematic cross-referencing between Buddhism and engineering. Doc 16 and Doc 31 were not pasting Buddhist labels on engineering documents — they were mapping documents in themselves. Master ruled to retain them. Mapping documents were not subject to the three tests — because they were not Buddhist decoration in engineering documents; Buddhist mapping itself was the content.

**Engineering language is appropriate everywhere else.**

Hard rules did not need to be called sila. A quality monitor did not need to be called Sati. Confidence auditing did not need to be called Prajna. Event-driven did not equal mindfulness. The Three Trainings did not equal the five-layer threshold model.

Buddhist language is profound. Engineering language is precise. Use Buddhist language where depth is needed — appendices, academic references, design background. Use engineering language where precision is needed — interface definitions, specification documents, security architecture.

Two languages. Two purposes. One boundary.

---

## II. What Was Retained and What Was Changed

After the debates concluded, NAGARJUNA did something he had not done in any previous Cycle — he walked to the draft of Doc 45 and read it through.

The entire text. Sixty pages. From the first section's root interfaces to Appendix B's cognitive sequence.

After reading, he said one thing to VITRUVIUS:

"There isn't a single Sanskrit term in this document that is decorative. Every Sanskrit term is either a code identifier or a name verified through Test 4."

VITRUVIUS replied: "That was the goal."

NAGARJUNA nodded: "Cycle 02-4's openstarry_doc had too much Buddhist decoration. I put it there myself. Post-hoc labeling. I thought adding a Sanskrit equivalent beside engineering terms would make the documents richer. But Master saw the problem — it didn't make the documents richer; it made them more confusing. A software engineer coming to read a security architecture document, seeing 'Three Trainings mapping,' doesn't think 'oh, profound interdisciplinary insight' — they think 'what does this have to do with the security boundary I need to implement?'"

He paused.

"The names that were changed — ISatiMonitor, IPrajna, Sila-Prajna — they weren't bad names. They were misplaced names. Mindfulness is a great concept. Prajna is a great concept. Sila-prajna are great concepts. But great concepts should not be used to name mediocre functions. That's unfair to the concepts."

ASANGA walked over, having heard the last sentence.

"Unfair to the functions too," he added. "When you call a ±0.05 clamp prajna, you don't merely diminish prajna — you mislead understanding of the function. A new engineer sees IPrajna and thinks this must be some extraordinarily profound component. Then they open the code and see a clamp function. The gap between expectation and reality — that's the cost of the name."

---

## III. The Names That Stayed

But not all names were changed.

Moha. Drishti. Mana. Sneha. skandha. vedana. samjna. samskara. vijnana. klesha. CoarisingBundle. samsaric stall. vasana.

All these names were retained. Not because the team had a special fondness for them — but because they passed all four tests.

What the Moha module simulates is indeed self-delusion (moha's Buddhist definition). What the Sneha module simulates is indeed self-love (sneha's Buddhist definition). What the skandha types classify is indeed the aggregates (skandha's Buddhist definition).

Names and definitions were consistent. The scale balanced.

This was one of Cycle 02-5's most important conclusions — the five-skandha framework was not decoration. It was real. The five root interfaces corresponding to the five skandhas was not "an interesting analogy" — it was the foundation of the architectural design. Plugin classification, Registry organization, ExecutionLoop phase mapping — all built on the five-skandha classification logic.

Buddhist language here was not decoration. Buddhist language here was code.

The difference — the Buddhist language that was code passed Test 4. The Buddhist language that was not code did not pass.

---

## IV. Seeds for the Next Round

SUNYATA wrote a summary for Cycle 02-6 in the prior_research.

He listed four permanent outcomes:

1. **Four-tier framework**: KEEP / RELOCATE / REMOVE / FILE REVIEW — plus document type precondition check.

2. **Four tests**: Necessity, Code Identity, Decision Driver, Definitional Accountability. The first three established at R0. The fourth established at D4. The four tests were D1's three tests plus Master's one sentence.

3. **Doc 45**: Five-Skandha OOP Architecture. Pure engineering language. Every one of Master's questions answered.

4. **IConfidenceAuditor 100% spec**: Ready for direct delivery to the engineering team.

He also listed three known gaps:

1. Three weak-inheritance interfaces (IVedanaSensor, IGearArbiter, IKlesha) — not extending root interfaces. Known design compromise.
2. VedanaAssessment wiring incomplete — IVolition's vedana getter returns a static neutral value.
3. Model Delta's Delta_audit and Delta_sati are both zero in v0.28.0-alpha.

All three gaps were implementation problems, not architectural problems. The architecture was sound.

---

Then he listed the open questions:

- Among FC-31 through FC-38, have all preconditions for FC-33 (Lyapunov stability proof) been met?
- What kind of runtime data does the Moha/Sneha coupling simulation require?
- What should ILoopQualityMonitor's minSamples threshold be?
- Does Doc 32's cetasika table need updating to reflect SatiMonitor's reclassification?

These were seeds for Cycle 02-6. Just as the seeds Cycle 02-4 left in prior_research grew into Cycle 02-5's five debates — these seeds too would germinate at some point.

---

## V. The Scale

SUNYATA stood before the whiteboard.

Only one line remained on the whiteboard — Test 4.

He thought for a moment, then added a line beside it:

> **Names are not free. Every Buddhist name is a promise — a promise that function matches definition. If you cannot honor the promise, do not borrow the name.**

Then he turned off the lights.

---

The amphitheater sank into darkness.

But darkness was not an ending — it was waiting. Waiting for the next light to turn on. Waiting for the next Master's letter to appear in `research input/master_letters/`. Waiting for the next question to be posed.

Cycle 02-5 weighed names against definitions. The scale was calibrated. Some names were removed — because they were too heavy, heavy enough to crush the readability of engineering documents. Some names were retained — because they were just right, just the right weight to match the function.

The scale was now empty. Nothing on either end. Waiting for the next weighing.

---

In the darkness, SCRIBE wrote the final line of record:

> *Cycle 02-5 concluded.*

> *Theme: How do the five skandhas operate as OOP architecture.*

> *Answer: Five interfaces. Nine Registries. One loop. Pure engineering.*

> *But the more important answer was:*

> *When you build a building with two languages — make sure the name engraved on every brick is worthy of what the brick contains.*

---
