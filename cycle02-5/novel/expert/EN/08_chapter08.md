# Chapter 8: The New Document

---

After D5 ended, the amphitheater was quiet for a time.

Not the quiet of waiting for Master after D3, nor the quiet of aftershocks after D4. This was the quiet of "the work is done, but there is one more thing to do."

Five debates. Thirty-one votes. Twenty-nine formal resolutions plus six attached items. From three in the morning when SUNYATA adjusted the color temperature to the final 8/8 of D5, the entire Cycle consumed approximately six and a half hours of debate time.

But the end of debate was not the end of research. Debates produced resolutions. Resolutions needed to be implemented.

---

## I. Doc 45

VITRUVIUS and KERNEL began work immediately after D5 ended.

What they were writing was Doc 45 — `Five_Skandha_OOP_Architecture.md` — the Five-Skandha OOP Architecture. The core engineering output of the entire Cycle 02-5. A new document. Pure engineering language. Everything Master had asked for in his letter — "five-skandha sub-categories, DI, how the agent core loads five-skandha plugins, how the five skandhas flow" — all concentrated in this single document.

VITRUVIUS handled the architecture description. KERNEL handled the DI wiring and Registry details. TURING did source code cross-referencing.

---

Doc 45's structure naturally emerged from D3's six votes:

**Section 1: Root Interfaces (D3-R1)**

The completeness argument for the five root interfaces — IRupa, IVedana, ISamjna, ISamskara, IVijnana. LINNAEUS' coverage verification, BABBAGE's type algebra theorem, ASANGA's Abhidharma exhaustive classification axiom, KERNEL's microkernel subsystem mapping — four independent arguments, one conclusion: five is enough.

PENROSE's attached recommendation was written into a footnote: monitor the vijnana sub-interface count (currently four, future six — adding IConfidenceAuditor and ILoopQualityMonitor; consider splitting if it exceeds ten).

**Section 2: PluginHooks Mapping (D3-R2)**

The complete table of nine hook-to-Registry mappings:

| PluginHooks Field | Registry | Skandha |
|-------------------|----------|---------|
| tools | ToolRegistry | samskara |
| providers | ProviderRegistry | samjna |
| listeners | ListenerRegistry | rupa |
| guides | GuideRegistry | vijnana |
| gearArbiters | GearArbiterRegistry | [samjna, vijnana] |
| volition | IVolition (single) | vijnana |
| kleshas | KleshaRegistry | vijnana |
| monitors | MonitorRegistry | [vedana, samjna, vijnana] |
| auditor | IConfidenceAuditor (single) | vijnana |

Every row bore TURING's source code verification mark.

**Section 3: SlashCommand (D3-R2a / D3-R2b)**

The exception that belonged to no skandha — because it bypassed the ExecutionLoop and did not participate in the cognitive loop. Analogy: Unix signal handler.

GUARDIAN's security observation: SlashCommand bypassed SafetyMonitor — if a plugin executed dangerous operations through SlashCommand, all five-skandha safety mechanisms were nullified. This was a known security boundary requiring particular attention during plugin review.

**Section 4: Skandha Metadata (D3-R3)**

The skandha field was metadata, not the routing basis. Type routing was already complete and unambiguous. `validatePluginSkandha()` maintained warning-only.

**Section 5: DI Wiring (A2 Summary)**

Pure DI, with `createAgentCore(config)` as the sole Composition Root. Strict linear construction order for 21 components. 9 Registries — most were dependency-free Map containers.

Key patterns: Lazy Accessor (IPluginContext providing deferred access), Provider capability filtering (allowedProviders manifest field), Resolver pattern (providerResolver, guideResolver, modelResolver using closures for deferred resolution).

VITRUVIUS replaced the text description with a complete DI chain diagram. From `agent.json` to `createAgentCore()` to every Registry to ExecutionLoop — one clear line. No circular dependencies. No implicit injection. Every dependency was explicitly passed.

**Section 6: ExecutionLoop Five-Skandha Flow (A4 Summary)**

Nine-phase execution flow:

| Phase | Name | Skandha | Core Operation |
|-------|------|---------|---------------|
| 1 | Input Reception | rupa | IListener -> SparshEvent |
| 2 | Context Assembly | vijnana | IGuide + SafetyMonitor |
| 3 | Cognitive Processing | samjna | IProvider.chat() |
| 4 | Gear Routing | vijnana+samjna | ManoAggregator + IGearArbiter |
| 5 | Deliberation | vijnana | IVolition |
| 6 | Tool Execution | samskara | ITool.execute() |
| 7 | Sensory Feedback | vedana | VedanaSensor -> ChannelVedana |
| 8 | Affliction Update | vijnana | IKlesha.perceive() |
| 9 | Loop Control | — | VedanaEmergency + VitakkaWatchdog |

Three-layer stability: Inner tool loop (per round), Outer VedanaEmergency (5 consecutive dukkha ticks), Safety VitakkaWatchdog (10 cycles or 5s). Trigger thresholds strictly increasing.

**Section 7: Cross-Skandha Interaction Matrix (A5 Summary)**

5x5 interaction matrix. Vijnana had the highest interaction density (seven connections). Samskara was the most active signal producer. Model Delta five-layer threshold formula.

**Section 8: Samskara Design Notes (D3-R4a / D3-R4b)**

The narrowing of samskara — from the Buddhist tradition's 49 mental factors compressed to ITool (externally observable behavior). ASANGA's candor: this was the weakest point of Buddhist self-consistency in the five-skandha architecture. DC-6's ruling that "samskara remains open, not locked down" continued in effect.

**Section 9: ILoopQualityMonitor Classification (D2 + D4 Summary)**

skandha: ['vedana', 'samjna', 'vijnana']. The first three-skandha plugin. Naming history: ISatiMonitor (D2) -> ILoopQualityMonitor (D4-R1). Four-function to three-skandha mapping table. Rationale for excluding samskara.

**Appendix A: Twelve Links Functional Analogy (D3-R5)**

sparsha->vedana->tanha->upadana chain functional analogy. Explicitly labeled as "functional analogy" rather than "formal mapping." Scale difference annotation.

**Appendix B: Cognitive Sequence Structural Parallel (D3-R6)**

citta-vithi eight-state to LoopState six-state mapping. Parallelism rating for each state pair (high / medium-high / medium). PENROSE's theoretical observation: the structural convergence of cognitive loops was an inevitable consequence of functional requirements, not deliberate imitation. BABBAGE's FSM morphism analysis — contrasting the twelve links (failed) with the cognitive sequence (succeeded).

---

## II. Cleanup

While VITRUVIUS and KERNEL wrote Doc 45, ARCHIMEDES and SCRIBE began executing the cleanup.

The cleanup list was compiled from D1 through D4 resolutions:

---

### Remove (REMOVE)

1. **Doc 38 L540-544**: The "Buddhist mapping" column of the three-layer rules table — delete. Retain the "Rule Layer" and "Engineering Semantics" columns.

2. **Doc 44 L478**: Three Trainings mapping row — delete.

3. **Doc 43 full text**:
   - Title change: "Mindfulness Architecture" -> determined by final name from D2/D4
   - 75+ instances ISatiMonitor -> ILoopQualityMonitor
   - Remove event-driven = mindfulness equivalence
   - Remove bhavanga-citta retrofitting (three instances)
   - Remove DN 22 scriptural citation
   - Add "naming explanation" paragraph

4. **Doc 37**:
   - Remove "Buddhist interpretation" column (no engineering information increment)
   - Remove sila metaphor
   - 3 instances IPrajna -> IConfidenceAuditor

5. **Doc 03**:
   - Filename: Sila_Prajna_Security_Framework -> Plugin_Security_Lifecycle
   - Remove Buddhist mapping table
   - Clean up seed theory in TypeScript comments
   - Retain five-state model and three-layer security model

6. **Batch A five items**: sila/upaya/smrti/event-driven=mindfulness/trisiksa mappings scattered across multiple documents — all removed.

---

### Relocate to Appendix (RELOCATE)

1. **Doc 44 Section 10 remainder**: Move to Appendix_C (Buddhist background of design decisions).

2. **Batch B eight items**: Including NAGARJUNA's two-truths commentary, bhavanga-citta mapping, scriptural citations, interdisciplinary comparison tables — all moved to corresponding appendices.

3. **Special handling B-6**: PASCAL's mathematical formalization (`Var(epsilon) = f(theta_moha)`) retained in main text. Only the Cheng Weishi Lun citation moved to Appendix_C.

---

### Retain (KEEP)

1. **Skandha type names**: rupa, vedana, samjna, samskara, vijnana — code identifiers.

2. **Klesha module names**: Moha, Drishti, Mana, Sneha — code identifiers, DC-1 confirmed.

3. **Buddhist concepts in design rationale**: vasana as acquired conditioning, four afflictions co-arising simultaneously, CoarisingBundle, sahaja definition correction, samsaric stall — all passed the three tests.

4. **Doc 16 and Doc 31**: Master ruled to restore to original. Buddhist mapping documents, not decoration.

---

### Create New

1. **Doc 45**: Five-Skandha OOP Architecture (in progress).

2. **Appendix_A**: Buddhist-Engineering Terminology Glossary.

3. **Appendix_B**: Eight Consciousnesses Academic Reference (content from the Doc 31 RELOCATE ultimately did not move here — Master ruled Doc 31 retained).

4. **Appendix_C**: Buddhist Background of Design Decisions.

---

## III. Renaming Cascade

TURING sat at his workstation and opened all affected files.

ILoopQualityMonitor's renaming affected six documents, over 100 replacement instances. IConfidenceAuditor's renaming affected five documents. Doc 03's renaming and cleanup was the third line.

Three lines proceeded simultaneously. Every replacement required context confirmation — not blind search-and-replace. Some instances of "Sati" appeared in design rationale paragraphs, requiring judgment on whether to replace with the new name or retain as historical reference. Some instances of "Prajna" appeared in Model Delta formulas, requiring synchronized variable name updates.

TURING did it line by line. This was his way — no shortcuts, no estimates, only line-by-line precision.

ARCHIMEDES sat beside him, responsible for verifying the contextual correctness of every replacement.

SCRIBE sat on the other side, recording the CHANGELOG.

---

## IV. Numbers

After Cycle 02-5 was completed, SCRIBE tallied the numbers.

| Metric | Value |
|--------|-------|
| Formal resolutions | 29 (D1-D5) + 6 attached items |
| Total vote count | 31 |
| Unanimous passes | 19/29 (66%) |
| Highest vote | 20/20 or 8/8 (19 items) |
| Lowest vote | 5/8 (D5-R2, 63%) |
| Contested resolutions | 10 |
| Minority opinion archives | 9 |
| Total debate duration | ~375 minutes (90+60+120+30+75) |
| Modified documents | 8+ |
| New documents | Doc 45 + 3 appendices |
| Renaming replacements | 120+ |

Compared with previous Cycles:

| | Cycle 02-3 | Cycle 02-4 | **Cycle 02-5** |
|---|-----------|-----------|----------------|
| Debate sessions | 6 | 6 | **5** (3 planned + 2 unplanned) |
| Total resolutions | 27 | 55 | **35** |
| Unanimous rate | 41% | 31% | **66%** |
| Minority opinions | 5 | 12 | **9** |
| New documents | 4 | 3 | **4** |

Unanimous rate 66% — the historical high. Not because there was no disagreement — D3-R5's 13/20 and D4-R1's 13/20 proved disagreement existed. The high unanimous rate was because the four-tier framework and four tests provided a common standard of judgment. When everyone measures on the same ruler, measurements naturally tend toward agreement.

---

## V. The Final Confirmation

After Doc 45 was completed, VITRUVIUS performed a full review.

He confirmed that every question Master had asked in his letter had been answered:

| Master's Question | Answer Location |
|------------------|-----------------|
| Five-skandha sub-categories | Doc 45 §1 |
| How DI wires | Doc 45 §5 |
| How Agent Core loads five-skandha plugins | Doc 45 §2, §4 |
| How the five skandhas flow | Doc 45 §6, §7 |
| Sati plugin skandha classification | Doc 45 §9, D2 record |
| Buddhist mapping cleanup | 8 modified documents, D1 record |
| Buddhist mapping boundary principles | Four-tier framework + four tests |
| ILoopQualityMonitor/IConfidenceAuditor spec | D5 record, Doc 45 §9 |

Every question. Every answer. In engineering language.

---

> *SCRIBE's aside*

> *Chapter 8 is a library's reorganization record.*

> *Not writing books — shelving them. Gathering resolutions scattered across five debates and placing them on the correct shelves. Doc 45 was a newly purchased book — placed on the "Architecture" row. Removed mappings were expired periodicals — moved from the main shelves to storage (appendices), or recycled outright. Renaming was re-labeling — ensuring that every book's spine bore a name matching its contents.*

> *This was not exhilarating work. This was necessary work.*

> *D4's scale. D5's specification. They were the spirit of Cycle 02-5 — the former calibrated the relationship between names and definitions, the latter proved that engineering could stand purely on its own legs. But spirit needed a body. Someone needed to open every document, find every instance of "ISatiMonitor," replace it with "ILoopQualityMonitor" — then verify the context. Verify the formulas. Verify the references. Verify the CHANGELOG.*

> *TURING did it line by line. ARCHIMEDES verified it instance by instance. SCRIBE recorded it entry by entry.*

> *This was the last mile of research. Not the hardest mile — but the most easily overlooked mile. Finding problems is glamorous. Solving problems is silent.*

> *Doc 45 was a silent victory. It lacked D4's dramatic reductio. It lacked D1's unprecedented ten 20/20s. It was merely a document — a 60-page document — answering every one of Master's questions in pure engineering language.*

> *Five-skandha sub-categories? Five root interfaces, nine sub-interfaces, three weak inheritances.*

> *DI wiring? Pure DI, Composition Root at createAgentCore(), 21 components built linearly.*

> *Plugin loading? Manifest + Factory, dual path (Sandbox / Direct), eight-state lifecycle.*

> *Five-skandha flow? Nine-phase ExecutionLoop, FSM six states, three-layer stability.*

> *Every answer had source code references. Every source code reference was verified by TURING.*

> *The scale found its balance here. Not because both ends weighed the same — but because both ends were precisely measured. Names were calibrated (D4). Specifications were completed (D5). Documents were cleaned up (D1). Architecture was verified (D3). Skandha classification was decided (D2).*

> *Cycle 02-5 asked a seemingly simple question: how do the five skandhas operate within the agent core?*

> *The answer took six and a half hours of debate, thirty-one votes, twenty-nine resolutions, one new document, eight modified documents, and over 120 renaming replacements.*

> *But in the end, the answer was indeed simple:*

> *Five interfaces. Nine Registries. One loop.*

> *Pure engineering.*

---
