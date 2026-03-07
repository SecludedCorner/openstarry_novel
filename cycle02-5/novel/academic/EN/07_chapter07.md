# Chapter Seven: Two Languages

---

## Doc 45

After five debates concluded, VITRUVIUS and KERNEL immediately began writing Doc 45 — `Five_Skandha_OOP_Architecture.md` — the core engineering deliverable of Cycle 02-5.

The four questions Master demanded in his letter — skandha sub-categories, DI wiring, Plugin loading flow, five-skandha flow — were all unified in this single document. Pure engineering language.

Nine sections emerged naturally from the debate resolutions:

| Section | Content | Source |
|---------|---------|--------|
| §1 | Five root interface completeness | D3-R1 |
| §2 | PluginHooks → Registry mapping | D3-R2 |
| §3 | SlashCommand exception | D3-R2a |
| §4 | Skandha metadata | D3-R3 |
| §5 | DI wiring | A2 research |
| §6 | ExecutionLoop nine-phase flow | A4 research |
| §7 | Cross-skandha interaction matrix | A5 research |
| §8 | Samskara-skandha design notes | D3-R4 |
| §9 | ILoopQualityMonitor classification | D2 + D4 |

Appendix A (Twelve Nidanas functional analogy) and Appendix B (cognitive sequence structural parallel) came from D3-R5 and D3-R6 respectively.

NAGARJUNA, after reading the complete document, said to VITRUVIUS: "Not a single Sanskrit term in this document is decoration. Every Sanskrit term is either a code identifier or a name verified through Test 4."

---

## Cleanup

ARCHIMEDES and SCRIBE executed the cleanup simultaneously. The checklist was compiled from the resolutions of D1 through D4:

**Removed**: Doc 38 Buddhist mapping column, Doc 44 Three Trainings mapping rows, Doc 43 full-text event-driven=mindfulness equivalence and 75+ ISatiMonitor replacements, Doc 37 Buddhist explanation column and sila metaphors, Doc 03 renaming and Buddhist mapping table removal, Batch A five scattered mappings.

**Relocated to appendices**: Doc 44 Section 10 remainder, Batch B eight items. Special handling: PASCAL's mathematical formalizations retained in main text; Cheng Weishi Lun citations moved to appendix.

**Retained**: Skandha type names (rupa, vedana...), Klesha module names (Moha, Drishti, Mana, Sneha), Buddhist concepts in design rationale (vasana as acquired habituation, four afflictions arising simultaneously...), Doc 16 and Doc 31 (Master ruled to restore).

**Created**: Doc 45, Appendix_A (glossary), Appendix_C (design decision Buddhist background).

TURING processed the renaming replacements line by line. ILoopQualityMonitor affected over 100 instances across six files. IConfidenceAuditor affected five files. Each replacement required contextual verification — not blind search-and-replace. Some "Sati" occurrences appeared in design rationale paragraphs, requiring judgment on whether to replace or retain as historical reference.

Total: over 120 document modifications.

---

## The Numbers

| Metric | Value |
|--------|-------|
| Formal resolutions | 29 (D1-D5) + 6 ancillary items |
| Total vote count | 31 |
| Unanimous votes | 19/29 (66%) |
| Closest vote | 5/8 (D5-R2) |
| Total debate duration | ~375 minutes |
| Modified files | 8+ |
| New files | Doc 45 + 3 appendices |
| Renaming replacements | 120+ |

Unanimity rate of 66% — the highest in history. Not because disagreements were absent (D3-R5's 13/20 and D4-R1's 13/20 prove disagreements existed). The high unanimity rate occurred because the four-tier framework and four tests provided a shared standard of judgment.

---

## The Boundary Between Two Languages

The core of Cycle 02-5 is not any particular resolution. The core is the answer to a question: in a system that uses both Buddhist and engineering languages, where does the boundary between these two languages lie?

**Buddhist language is appropriate in three places:**

1. **Code identifiers** — Buddhist terms that have become part of the source code, with function and definition aligned. The Moha module genuinely simulates self-delusion. The skandha types genuinely classify the five skandhas. Pass Test 4. The scale is balanced.

2. **Design rationale** — Buddhist concepts that actually drove engineering decisions, with DC confirmation. "Vasana is acquired habituation" drove VasanaEngine externalization. "Four afflictions arise simultaneously" drove MulaKleshaBundle atomicity design. Causal relationships exist.

3. **Independent mapping documents** — Documents whose very purpose is systematic correspondence between Buddhism and engineering. Doc 16 and Doc 31 are not subject to the three tests. Master ruled to retain them.

**Engineering language is appropriate everywhere else.**

Hard rules do not need to be called sila. Quality monitors do not need to be called Sati. Confidence auditing does not need to be called Prajna. Event-driven does not equal mindfulness.

Buddhist language is profound. Engineering language is precise. Use Buddhist language where depth is needed — appendices, academic references, design background. Use engineering language where precision is needed — interface definitions, specification documents, security architecture.

---

## Seeds for the Next Cycle

SUNYATA left four permanent outcomes in prior_research:

1. Four-tier framework (KEEP/RELOCATE/REMOVE/FILE REVIEW) + document type prerequisite check
2. Four tests (Necessity, Code Identity, Decision-Driven, Definitional Responsibility)
3. Doc 45 Five-Skandha OOP Architecture
4. IConfidenceAuditor 100% specification

Three known gaps: weak inheritance interfaces, VedanaAssessment wiring, and Model Delta's audit/sati layers remain at zero.

These are the seeds for Cycle 02-6. Just as the seeds left in prior_research by Cycle 02-4 grew into Cycle 02-5's five debates — these seeds, too, will germinate at their appointed time.

---

## The Balance Scale

SUNYATA was the last to leave the amphitheater. The whiteboard had been wiped clean, but one line he deliberately left:

> **Test 4: When you use a Buddhist Sanskrit term as a code identifier, the component's function must match that term's Buddhist definition. If inconsistent, use an engineering term.**

He added a line beside it:

> **Names are not free. Every Buddhist name is a promise — a promise that function matches definition. If you cannot honor the promise, do not borrow the name.**

The lighting shifted from 6500K back to 4000K. Neither cool nor warm. Neutral white. Like a workshop that has been cleaned and cleared — tools stowed, floor swept, awaiting its next user.

The amphitheater settled into waiting. Waiting for the next letter from Master. Waiting for the next question to be posed.

Cycle 02-5 weighed names against definitions. Some names were taken down — because they were too heavy and crushed readability. Some names were kept — because they happened to match the weight of their functions.

The final answer is indeed simple: five interfaces. Nine registries. One loop. Pure engineering.

But the more important answer is: when you build a building using two languages — make sure the name engraved on every brick is worthy of what the brick contains.

---
