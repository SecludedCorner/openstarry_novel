# Chapter Four: D3 — Validating the Five Skandhas

---

## The Examination

D3 was an examination. The examinee was a building.

Question: Is the five-skandha OOP architecture sufficient to support engineering implementation?

This question can be broken into six sub-questions. D3 spent two hours answering them one by one.

---

## D3-Q1: Are the Five Root Interfaces Sufficient?

Five root interfaces — IRupa, IVedana, ISamjna, ISamskara, IVijnana.

Four researchers argued toward the same conclusion from four independent directions.

**LINNAEUS** performed coverage verification: of the nine hooks in PluginHooks, each was covered by at least one Skandha. No orphans.

**BABBAGE** used type algebra to prove coverage of the classification space: the set of SDK public interfaces $\{I_1, I_2, ..., I_n\}$ can be written as a disjoint union of five skandha subsets (strictly speaking, nearly disjoint — IGearArbiter spans two skandhas).

**ASANGA** responded from the Abhidharma's exhaustive classification: the five skandhas in Buddhism are a complete classification of experience — rupa, vedana, samjna, samskara, and vijnana exhaust all mental activity. If the original Buddhist classification is complete, an OOP mapping based upon it carries an inherent completeness guarantee.

**KERNEL** confirmed from the microkernel perspective: the five root interfaces correspond to five operating system subsystems — I/O (rupa-skandha), sensors (vedana-skandha), classifiers (samjna-skandha), actuators (samskara-skandha), controllers (vijnana-skandha). The subsystem combinations already cover all hook functions.

Four independent arguments. **20/20.**

---

## D3-Q2: Are the PluginHooks Mappings Correct?

A line-by-line verification of the nine hook-to-skandha mappings.

Key clarification: IGearArbiter spans both samjna + vijnana skandhas. D1 had already ruled on the dual-skandha manifest (Cycle 02-4 D1-R1). This is not classification ambiguity — it is functional cross-boundary. Recognition (samjna-skandha) and judgment (vijnana-skandha) occur simultaneously in gear arbitration.

SlashCommand belongs to no skandha — it bypasses the ExecutionLoop. GUARDIAN flagged the security boundary: SlashCommand can bypass all five-skandha safety mechanisms. This is a known design constraint, not a defect.

**20/20.**

---

## D3-Q3 and D3-Q4: Metadata and Samskara-Skandha

**D3-Q3**: What role does the skandha field play in routing? Conclusion: metadata only, not used for routing. Type-based routing (interface type → Registry) is already complete and unambiguous. Skandha is annotation, not ground truth. **18/20.** Minority opinion from MESH and GUARDIAN: metadata routing could serve as auxiliary verification.

**D3-Q4**: Does ISamskara need more sub-interfaces?

This was the most candid question in D3.

ASANGA stood up and acknowledged a significant deviation: "OpenStarry's samskara-skandha design diverges most from Buddhist tradition. Traditional samskara-skandha encompasses 49 mental factors — volition, effort, wisdom, faith, conscience, decorum — virtually all mental activity. But OpenStarry narrows samskara-skandha to ITool — external action. Only external action."

HERACLITUS provided the engineering rationale: IVolition is in Phase 5 (before action, belonging to vijnana-skandha), ITool is in Phase 8 (during action, belonging to samskara-skandha). The two exist at different execution stages. Samskara-skandha should be "what is being done," not "deciding what to do."

NAGARJUNA's concession carried the calm of deliberate reflection: "Buddhism's samskara-skandha classification is based on a practitioner's introspection. OpenStarry is not a practitioner. The classification of software systems should be based on function, not introspection."

**20/20.** But with a condition: Doc 45 must document this deviation. The narrowing of samskara-skandha is a conscious choice, not an inadvertent omission.

---

## Two Ancient Paths

The final two questions of D3 concerned the possibility of Buddhist mapping appendices.

**D3-Q5: The Twelve Nidanas.**

NAGARJUNA drew two lines — one very long, labeled "Twelve Nidanas"; one very short, labeled "ExecutionLoop." The scale differed by orders of magnitude. The Twelve Nidanas describe three-lifetime causation spanning past, present, and future lives. ExecutionLoop covers cognitive processing lasting tens of milliseconds to a few seconds.

BABBAGE attempted to construct a structural morphism — and failed. The causation of the Twelve Nidanas is linear and unskippable. But the ExecutionLoop can be skipped — an Agent without IVedanaSensor will skip the vedana phase. The structures differ; no structure-preserving mapping exists.

But HERACLITUS identified a local correspondence — the segment contact→feeling→craving→grasping structurally corresponds to SparshEvent→ChannelVedana→KleshaGain→VolitionalDecision.

**13/20.** Selective appendix. The seven dissenting votes did not deny the existence of local correspondence, but questioned the necessity of documenting it in engineering files.

**D3-Q6: The Cognitive Sequence (citta-vithi).**

BABBAGE tried the morphism again. This time — he succeeded.

The cognitive sequence is Theravada Buddhism's fine-grained analysis of cognitive process — bhavanga→avajjana→pancavinnana→sampaticchana→santirana→votthapana→javana→tadarammana. And the ExecutionLoop's Idle→EventReceived→Sensing→Recognizing→Arbitrating→Deliberating→Acting→Feedback.

"A structural morphism exists," BABBAGE said. "There is a structure-preserving mapping between the two FSMs. This is not a metaphor. This is mathematics."

His vote shifted from opposing D3-Q5 to supporting D3-Q6. In the record he wrote: "The FSM morphism was the pivotal argument for my shift. The Twelve Nidanas have no morphism. The cognitive sequence does. Quality determines votes."

**17/20.** From 13/20 to 17/20 — the four-vote difference was not sentiment; it was precision.

---

## The Verdict

D3 concluded. Six votes. Three unanimous, two with strong majorities, one with divergence.

SUNYATA wrote the conclusion on the whiteboard:

> **The five-skandha OOP architecture is sufficient to support engineering implementation.**

Then listed three known gaps:
1. IVedanaSensor weak inheritance (does not inherit IVedana)
2. VedanaAssessment wiring gap (defaults to neutral values)
3. IPrajna / ISatiMonitor not yet implemented

All three gaps are not architectural issues. They are implementation issues. A defect requires redesigning the blueprint; a gap requires continuing construction.

The architecture passed the examination.

---

## Master's Ruling

Forty minutes after D3 concluded.

Master's review appeared. Not long, but precise as a scalpel.

He first confirmed the majority of D1's resolutions — the four-tier framework, the three tests, Batches A/B/C, table cleanup, module name retention. "These are all correct."

Then he mentioned two names: Doc 16 and Doc 31.

"D1-Q7 and D1-Q8 — I disagree with these two resolutions."

Two 20/20 votes. Two unanimous decisions. Overturned by Master.

---

The rationale was clear and irrefutable: Doc 16 is not an engineering document with embedded Buddhism. Doc 16 is itself a Buddhist mapping document — its very purpose is to provide a systematic correspondence between Buddhism and engineering. The three tests apply to Buddhist decoration within engineering documents. They do not apply to mapping documents themselves.

PASCAL used a precise analogy: "Doc 16 and Doc 31 are paintings hanging in an art gallery, not murals painted on engineering blueprints."

ARCHIMEDES re-examined his audit table and added a new column — **Document Type**. Of the seven documents, five were engineering documents (three tests applicable), and two were Buddhist mapping documents (not applicable). "The numbers were right. But the premise was wrong."

Master's ruling did not merely overturn two resolutions. It revealed a blind spot in the framework — the three tests assumed the documents under review were engineering documents. If the document itself is a Buddhist mapping document, the standard was misapplied.

The three tests were not invalidated. They gained an applicability condition — a document type prerequisite check. Like a precision caliper — the accuracy is fine, but you must first confirm that what you are measuring is a component, not the design blueprint itself.

---

But Master's review contained one more sentence, pointing in a different direction:

"When you use Sanskrit, you need to take responsibility for its definition."

The full weight of this sentence would not be felt until D4.

---
