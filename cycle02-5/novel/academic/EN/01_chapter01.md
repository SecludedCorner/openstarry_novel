# Chapter One: Audit and Preparation

---

## R1 Independent Research

Nine studies launched simultaneously. Three tracks, fifteen lead authors.

### Track A: Five-Skandha Engineering Architecture

Track A was Master's top priority — answering the four core questions of five-skandha architecture in pure engineering language. Five sub-items were divided among twelve researchers:

| Sub-item | Lead Authors | Content |
|----------|-------------|---------|
| A1 Skandha Sub-categories | LINNAEUS + ASANGA | Complete sub-category tree of the five skandhas, cross-referenced with SDK source code |
| A2 DI Wiring | VITRUVIUS + KERNEL + TURING | Complete DI chain from agent-core → plugin-loader → loop |
| A3 Plugin Loading | DARWIN + MESH | Complete flow from agent.json to running hooks |
| A4 Execution Flow | HERACLITUS + WIENER + BABBAGE | sparsha → vedana → samjna → volition → tools → feedback |
| A5 Cross-Skandha Interaction | LEIBNIZ + ATHENA + PENROSE | Interaction matrix of vedana→klesha→arbiter→volition→action |

A1's sub-category tree revealed an important structural feature: vijnana-skandha possesses the most sub-interfaces (IGearArbiter, IVolition, IKlesha, IConfidenceAuditor), while samskara-skandha is the simplest (the single ITool interface). This asymmetry is meaningful — vijnana-skandha is "judgment," and the dimensions of judgment are naturally more numerous than the dimensions of "action."

A2 traced the complete dependency injection chain. Three researchers spent two days, starting from AgentCore's constructor, through PluginLoader's registry dispatch, to every hook invocation point in ExecutionLoop. Conclusion: the DI chain is complete, but with two known gaps — IVedanaSensor weak inheritance (does not inherit IVedana) and VedanaAssessment wiring defaults to neutral values.

A4 produced a complete five-skandha execution flow diagram. HERACLITUS, with his sensitivity to dynamic processes, traced the complete lifecycle of a SparshEvent from birth to death. WIENER redescribed the same flow in control theory language — the system is a closed-loop controller, user goals are reference inputs, Context is state feedback, and Tool Call is the control variable. BABBAGE formalized it, using a finite state machine to prove the flow's termination property.

### Track B: Buddhist Mapping Audit

B1 was led by ARCHIMEDES and SCRIBE. The engineering practice expert scanned seven openstarry_doc files, document by document, mapping by mapping. The method was a mechanical application of the three tests — every Buddhist mapping was tested three times, and results were recorded in the audit table.

Final results: 50 mapping instances.

| Disposition | Count | Examples |
|-------------|-------|----------|
| KEEP | 23 | Skandha type names, Klesha module names, DC-confirmed constraints, CoarisingBundle |
| RELOCATE | 13 | PASCAL's mathematical formalizations, MN 18 scriptural citations, Buddhist design rationale |
| REMOVE | 14 | sila/upaya/smrti labels, event-driven=mindfulness, Three Trainings mapping |

Nearly half were KEEP — not all Buddhist content is decoration. Some are identity (Klesha module names), some are decisions (the five-skandha classification drove the PluginHooks design). But 14 items marked REMOVE — pure decoration whose removal changes no engineering specification.

ARCHIMEDES made a precise judgment: "We're not removing the entire table. We're removing one column." He did not use a sledgehammer on a walnut — he used a scalpel to separate engineering content from Buddhist decoration.

Two special documents were flagged for FILE REVIEW: Doc 16 (Plugin type philosophical mapping, decoration ratio ~80%) and Doc 31 (eight-consciousness runtime model, decoration ratio ~70%). Their problem was not individual mappings, but the positioning of the entire document — was it an engineering document with embedded Buddhism? Or an independent document whose purpose was Buddhist mapping?

B2 was constructed by NAGARJUNA, ASANGA, and PASCAL — three people building the mapping boundary principles. A framework of three dimensions:

- **NAGARJUNA (Two Truths)**: Conventional truth = engineering language. Ultimate truth = Buddhist concepts. Do not force ultimate truth labels into conventional truth documents.
- **PASCAL (Damage Asymmetry)**: The damage of False Include is cumulative (number of readers × number of readings × cognitive switching cost). The damage of False Exclude is one-time (search cost). E[cumulative] >> E[one-time]. When in doubt, lean toward removal.
- **ASANGA (Causal Efficacy)**: Does the Buddhist concept drive an engineering outcome? Has causal efficacy → keep. Has no causal efficacy → remove.

Three disciplines, three paths, one conclusion — decorative mappings should be removed.

### Track C: Sati Plugin Positioning

C1 was led by TURING and GUARDIAN for functional analysis. TURING listed SatiMonitor's four functions in pure engineering terms: event subscription, sliding window, pattern recognition, quality metrics. And one critical "does not" — does not execute any action, does not modify any state, does not issue any command.

GUARDIAN's engineering analogy: a hybrid of APM Agent + Behavioral Analytics + QoS Monitor + SPC Anomaly Detector.

C2 was led by ASANGA and LINNAEUS for skandha composition analysis. They proposed four schemes:

| Scheme | Skandha Composition | Rationale |
|--------|-------------------|-----------|
| A | vedana + samjna | Sensing + recognition, simplest |
| B | vedana + samjna + vijnana | Sensing + recognition + evaluative judgment |
| C | samjna + vijnana | Recognition + evaluation, vedana too thin |
| D | Pure vijnana | All cognitive activity belongs to vijnana |

All four schemes had logical support, but each also had weaknesses. The final answer would be decided in the D2 debate.

---

## R2 Cross-Review

Twenty researchers formed a cross-review network — each reviewing at least two reports not authored by themselves.

TURING performed the most critical work — a comprehensive verification of all code references. Over 40 references were checked one by one against the v0.28.0-alpha source code. Result: four issues (under 10% error rate), all of low or medium severity. No critical errors.

He said six words: "References are clean. Ready for debate."

R2 summary:
- **24 consensus points**: across all three tracks, the foundation was solid
- **7 open questions**: debates had clear focal points
- **4 divergence points**: debates would have genuine exchanges

The pipeline was clear. The operating theater was ready.

---
