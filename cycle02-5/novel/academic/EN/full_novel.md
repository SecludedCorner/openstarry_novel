# Prologue: Cold White Light

---

The lights shifted from amber to cold white at three in the morning.

SUNYATA -- Research Director -- sat before the amphitheater's control console and pushed the color temperature from 3200K to 6500K. He had read Master's letter five times. The letter was only 45 lines, no attachments, placed in `research input/master_letters/cycle02-5/`, quiet as a note tucked between reports.

But every line cut like a scalpel.

Master's core directive: the Buddhist mappings in openstarry_doc were excessively strained -- "sila / upaya / smrti," "Threefold Training," "event-driven = mindfulness" -- and were creating barriers to reading comprehension. The skandha classification of the Sati plugin needed rethinking. Most importantly: five skandha sub-categories, dependency injection, how agent core loads five skandha plugins, how the five skandhas circulate within agent core -- answer in engineering language.

The theme of Cycle 02-5 was defined as: **ARCHITECTURAL -- How do the five skandhas operate as an OOP architecture?**

SUNYATA set the theater lights to operating-room cold white because this cycle was not research -- it was surgery. Excise the decorative Buddhist mappings; preserve the architecturally valuable engineering core.

At four in the morning, NAGARJUNA walked into the theater. He had no appointment. He brought a self-admission: in Cycle 02-4's openstarry_doc, some Buddhist mappings were labels he had "retro-fitted" after the engineering conclusions were already settled. "Hard rules = sila" was not an insight that drove design decisions -- it was decoration added after the design was complete.

That night's conversation produced the infrastructure for Cycle 02-5:

**Four-tier framework**: KEEP / RELOCATE (move to appendix) / REMOVE / FILE REVIEW (review entire document).

**Three tests**:
1. Necessity: Does removal change the engineering specification?
2. Code identification: Is the term used in source code?
3. Decision-driven: Did the Buddhist concept drive a Master-confirmed design decision?

The research was divided into three tracks: Track A (Five Skandha OOP Architecture), Track B (Buddhist Mapping Audit), and Track C (Sati Plugin Reclassification).

20 researchers. 5 debates (3 scheduled + 2 unplanned). From dawn to dusk.

The scalpel had been sterilized. The patient was on the operating table.

---

# Chapter 1: Audit and Research

---

## R1: Independent Research

Nine independent research reports were produced during the R1 phase. Three tracks advanced in parallel.

### Track A: Five Skandha Engineering Architecture

**A1 (LINNAEUS + ASANGA)**: Five skandha sub-category tree. A complete OOP interface inheritance analysis -- IRupa splits into IListener and IUI; IVedana produces ChannelVedana (continuous signal); ISamjna corresponds to IProvider; ISamskara narrows to ITool; IVijnana is the most complex, with four sub-interfaces: IGuide, IGearArbiter, IVolition, and IKlesha. Three "weak inheritance" cases were documented -- IVedanaSensor, IGearArbiter, and IKlesha do not explicitly extend a root interface.

**A2 (VITRUVIUS + KERNEL + TURING)**: DI wiring. Pure DI, with `createAgentCore()` as the sole Composition Root, 21 components built in strict linear order, 9 Registries. Lazy Accessor pattern, Provider capability filtering, Resolver closure-based deferred resolution. A comparison matrix against Spring/Guice/InversifyJS confirmed Pure DI as the correct choice for a microkernel.

**A3 (DARWIN + MESH)**: Plugin loading lifecycle. IPlugin = Manifest + Factory. Dual loading paths (Sandbox worker thread / Direct main thread). Eight-state lifecycle state machine. Sandbox security chain: signature verification -> static import analysis -> Worker isolation -> Heartbeat -> exponential backoff restart.

**A4 (HERACLITUS + WIENER + BABBAGE)**: Five skandha execution flow. FSM with six states, nine processing phases. Phase 1 (rupa) -> Phase 3 (samjna) -> Phase 5 (vijnana) -> Phase 6 (samskara) -> Phase 7 (vedana) -> Phase 8 (vijnana). Three-layer stability loop. BABBAGE provided a complete FSM formal specification.

**A5 (LEIBNIZ + ATHENA + PENROSE)**: Cross-skandha interaction. 5x5 interaction matrix. Model Delta five-layer threshold formula. PENROSE proposed three emergence pattern hypotheses -- adaptive conservatism, bistable switching, and attention funnel.

### Track B: Buddhist Mapping Audit

**B1 (ARCHIMEDES + SCRIBE)**: Line-by-line audit of 7 documents. 50 mapping instances -- 23 KEEP (46%), 13 RELOCATE (26%), 14 REMOVE (28%). Doc 43 had the highest decoration ratio (60%). Doc 16 and Doc 31 were flagged for "full file review" (decoration ratios of 80% and 70%).

**B2 (NAGARJUNA + ASANGA + PASCAL)**: Mapping boundary principles. NAGARJUNA's Two Truths separation, ASANGA's functional positioning, PASCAL's damage asymmetry (the cumulative cognitive burden of false includes >> the one-time search cost of RELOCATE). The three tests were formally justified in this document.

### Track C: Sati Plugin

**C1 (TURING + GUARDIAN)**: Pure engineering functional analysis. SatiMonitor subscribes to 11 EventBus event types, processes through a three-stage pipeline (buffer -> batch analysis -> quality vector computation), and outputs a LoopQualityVector with four dimensions (Continuity, Granularity, Speed, Equanimity), with **zero side effects**. Engineering equivalents: APM Agent + behavioral pattern analyzer + QoS Monitor + SPC anomaly detector.

**C2 (ASANGA + LINNAEUS)**: Skandha composition proposal. Four options -- A ['vedana','samjna'], B ['vedana','samjna','vijnana'] (recommended), C ['samjna','vijnana'], D ['vijnana']. Core argument: SatiMonitor's event subscription = vedana, pattern recognition = samjna, quality assessment = vijnana. Samskara excluded -- because it performs no actions.

## R2: Cross-Review

TURING verified 40+ code references and found 4 issues (no critical errors). 24 consensus points passed without debate. 7 open questions and 4 disagreements entered the D1-D3 debates.

---

# Chapter 2: Boundaries -- D1 Buddhist Mapping Boundary Debate

---

**Duration**: ~90 minutes | **Chair**: SUNYATA | **Votes**: 10 items | **Result**: All 20/20

D1 set a record in the project's history: ten votes, ten unanimous passes, zero minority opinions.

## Four-Tier Framework and Three Tests (D1-Q1: 20/20)

The four-tier framework and three tests were formally confirmed as permanent adjudication criteria. NAGARJUNA provided the philosophical foundation (Two Truths separation), PASCAL provided the mathematical argument (damage asymmetry), and ARCHIMEDES provided operational validation (full coverage of 50 cases).

## Three Batches of Adjudication

**Batch A (D1-Q2-A: 20/20)** -- 5 mappings explicitly criticized by Master, all REMOVE:
- Hard rules = sila -> REMOVE
- Soft rules = upaya -> REMOVE
- Heuristic rules = smrti -> REMOVE
- event-driven = mindfulness -> REMOVE
- Threefold Training mapping -> REMOVE

NAGARJUNA acknowledged that the first three were "retro-fitted labels" -- Buddhist names added after the engineering conclusions were already settled.

**Batch B (D1-Q2-B: 20/20)** -- 8 scholarly content items, all RELOCATE to appendices. Special handling: B-6 (PASCAL's Moha mathematical formalization `Var(epsilon) = f(theta_moha)`) retained in main text; only the *Cheng Weishi Lun* citation moved to appendix.

**Batch C (D1-Q2-C: 20/20)** -- 7 code identifiers / DC-confirmed concepts, all KEEP. Includes five skandha type names, Klesha module names, CoarisingBundle, etc.

## Individual Document Resolutions

- **D1-Q3** (20/20): Doc 38 L540-544, remove Buddhist mapping column.
- **D1-Q4** (20/20): Doc 44 L478, Threefold Training mapping REMOVE; Section 10 remainder RELOCATE. NAGARJUNA acknowledged the Threefold Training mapping was his "category error" -- the Threefold Training is a qualitative classification, while the five-layer model is a quantitative stratification.
- **D1-Q5** (20/20): Doc 43 renaming deferred until after D2 decision.
- **D1-Q6** (20/20): Klesha module names Moha/Drishti/Mana/Sneha KEEP. DC-1 confirmed + source code identifiers.
- **D1-Q7** (20/20): Doc 16 split -- extract Section 5 as independent document. (*Later overturned by Master*)
- **D1-Q8** (20/20): Doc 31 split downgraded. (*Later overturned by Master*)

**Overturning of D1-Q7 and D1-Q8**: Master ruled to restore the original state -- Doc 16 and Doc 31 are standalone Buddhist mapping documents, not decorations within engineering documents. The three tests apply to engineering documents, not to mapping documents. The team's framework was missing a dimension: **document type identification**.

ARCHIMEDES added a new column to the audit table -- document type (engineering / design decision / Buddhist mapping) -- as a precondition for the three tests.

---

# Chapter 3: A Three-Faced Mirror -- D2 Sati Plugin Skandha Classification Debate

---

**Duration**: ~60 minutes | **Chair**: SUNYATA | **Votes**: 3 items

## Renaming Strategy (D2-R1: 19/20)

Retain `Sati` as the code identifier; change the document title from "Mindfulness Architecture" to "Cognitive Loop Quality Monitoring Architecture." Add a "naming note" paragraph. Security documents use the full name.

Sole dissenting vote: GUARDIAN -- preferred complete renaming to eliminate the need for cultural background knowledge. Accepted the majority decision with the security document full-name condition.

## Five Skandha Composition (D2-R2: 18/20) -- Core Resolution

**Conclusion: skandha: ['vedana', 'samjna', 'vijnana']**

Four functions mapped to three skandhas:

| Function | Skandha | Description |
|----------|---------|-------------|
| EventBus event subscription (11 types, continuous perception) | vedana | Receives cognitive loop signals |
| Sliding window + pattern recognition | samjna | Identifies behavioral patterns from event streams |
| LoopQualityVector + SPC anomaly determination | vijnana | Evaluative quality judgment beyond descriptive recognition |
| **Executes no tools, modifies no state** | **Excludes samskara** | Not mindfulness practice |

Key argumentative turning points:

- **ASANGA**: Buddhist mindfulness (smrti) is a samskara mental factor -- active, intentional, morally positive. SatiMonitor is passive, automatic, and value-neutral. Therefore SatiMonitor is not mindfulness and should not be classified as samskara.
- **LINNAEUS**: OOP comparison -- "IGearArbiter is 'called upon to take a look'; SatiMonitor is 'always watching.'" Continuous subscription vs on-demand invocation -- sufficient to constitute an independent vedana declaration.
- **ARCHIMEDES** (turning point): The engineering cost difference between three-skandha and two-skandha is zero -- the PluginManifest's skandha field already supports multiple values. Once the concern of "three skandhas is too complex" was eliminated, discussion shifted to pure classificatory precision, where Proposal B's advantages were overwhelming.
- **Minority opinion** (MESH, KERNEL): Proposal C ['samjna','vijnana'] is symmetrical with the IGearArbiter classification and has long-term maintenance value.

**Historical significance**: SatiMonitor became OpenStarry's first three-skandha plugin.

## PluginHooks Dedicated Slot (D2-R3: 20/20)

Added `monitors?: ISatiMonitor[]` dedicated slot. Following the Cycle 02-4 `arbiters` precedent (SDK interface -> PluginHooks -> Registry -> PluginLoader four-step pattern).

---

# Chapter 4: Completeness -- D3 Five Skandha OOP Architecture Debate

---

**Duration**: ~120 minutes | **Chair**: SUNYATA | **Votes**: 6 items

## Root Interface Sufficiency (D3-R1: 20/20)

Four independent arguments converged on the same conclusion: the five root interfaces IRupa, IVedana, ISamjna, ISamskara, and IVijnana are sufficient to cover all functional requirements.

- **LINNAEUS**: 100% functional coverage verification.
- **BABBAGE**: Type-algebraic completeness theorem (Q.E.D.).
- **ASANGA**: Abhidharma exhaustive classification axiom.
- **KERNEL**: Five microkernel subsystem mappings (I/O, sensing, computation, execution, scheduling).

PENROSE appended a recommendation: monitor the vijnana sub-interface count (currently 4, projected 6; consider splitting if it exceeds 10).

## PluginHooks Mapping Correctness (D3-R2: 20/20)

TURING verified line-by-line against source code; all nine mappings confirmed correct.

Focal discussion: SlashCommand belongs to no skandha -- because it bypasses the entire ExecutionLoop (analogy: Unix signal handler). GUARDIAN's security observation: SlashCommand bypasses SafetyMonitor; if a plugin executes dangerous operations through this path, all five skandha safety mechanisms are void. This observation was recorded in Doc 45.

## skandha as Metadata (D3-R3: 18/20)

Status quo maintained -- skandha is metadata, not a routing basis. Type routing is already complete. Minority opinion (GUARDIAN, LINNAEUS): even a warning-only consistency validation has audit value.

## ISamskara Sub-Interfaces (D3-R4: 20/20)

ITool maintained as the sole sub-interface. ASANGA candidly acknowledged: this is the weakest point of Buddhist self-consistency in the five skandha architecture -- traditional samskara encompasses 49 mental factors, while OpenStarry narrows it to external actions (ITool). HERACLITUS's dynamic argument: IVolition is in Phase 5, ITool is in Phase 6 -- moving IVolition to samskara would create a "samskara before samskara" conceptual misplacement.

DC-6 "samskara remains open, not locked" continues in effect.

## Twelve Nidanas (D3-R5: 13/20 Proposal C)

The most contentious D3 vote. Proposal C (selective appendix mapping) prevailed.

- **NAGARJUNA**: Scale mismatch -- the Twelve Nidanas describe three-lifetime causation (macroscopic), while ExecutionLoop describes a single cognitive processing cycle (millisecond-level).
- **BABBAGE** (voted B): The Twelve Nidanas form a linear chain; ExecutionLoop is an FSM with cycles -- the graph structures are fundamentally different.
- Proposal B (no mapping) received 7 votes -- D3's largest minority bloc.

## Cognitive Sequence (D3-R6: 17/20 Proposal C)

Achieved higher consensus than the Twelve Nidanas -- because it describes phenomena at the same scale (the internal stages of a single cognitive act). HERACLITUS provided an eight-state comparison table with five "high" or "medium-high" parallels.

BABBAGE switched from B (Twelve Nidanas) to C (Cognitive Sequence) -- the FSM morphism analysis was the pivotal argument. The Twelve Nidanas have no morphism. The Cognitive Sequence does.

PENROSE's theoretical contribution: the structural convergence of cognitive loops is an inevitable consequence of functional requirements, not deliberate imitation.

## Architecture Assessment Conclusion

**The five skandha OOP architecture of v0.28.0-alpha is structurally sufficient.** Three known gaps (weak inheritance, VedanaAssessment wiring incomplete, IConfidenceAuditor/ILoopQualityMonitor not yet implemented) are all planned incremental improvements.

---

# Chapter 5: The Cost of a Name -- D4 Naming Correction Debate

---

**Duration**: ~30 minutes | **Trigger**: Master review | **Votes**: 3 items

D4 was not on the original agenda. It was triggered by a single sentence from Master:

> **"If you use Sanskrit, you must take responsibility for its definition. Do you think Sati's content is a complete match?"**

## NAGARJUNA's Reductio ad Absurdum

```
Premise A: Sati = samskara mental factor (Buddhist definition)
Premise B: SatiMonitor != samskara (D2-R2 conclusion)
 :. SatiMonitor != Sati
```

If mindfulness is necessarily samskara in Buddhism, and D2 has already proven that SatiMonitor is not samskara -- then SatiMonitor is not mindfulness. A component that is not mindfulness should not be called Sati.

ASANGA confirmed: "If SatiMonitor is not a samskara activity, then it is not Sati. Our own classificatory analysis negates our own naming."

## ISatiMonitor -> ILoopQualityMonitor (D4-R1: 13/20)

ARCHIMEDES's proposal prevailed: "Loop Quality Monitor" -- a quality monitor for the cognitive loop -- precisely describes the function, no Buddhism, no metaphor.

Minority opinions: IBehaviorQualityMonitor (GUARDIAN, 4 votes), ICognitiveLoopMonitor (NAGARJUNA + ASANGA, 2 votes), IQualityMonitor (SYNTHESIST, 1 vote).

Complete renaming table: ISatiMonitor -> ILoopQualityMonitor, SatiQualityVector -> LoopQualityVector, and 8 items total.

## IPrajna -> IConfidenceAuditor (D4-R2: 16/20)

NAGARJUNA: "Prajna is the highest cognitive capacity in Buddhism -- the wisdom that illuminates the true nature of all dharmas."

ASANGA: "It is like calling a temperature fine-tuning knob a nuclear fusion reactor."

IPrajna's actual function: one method, inputs a confidence score, outputs `{ delta: number, reasoning: string }`, with delta clamped to [-0.05, +0.05]. This is auditing -- not prajna.

BABBAGE: IConfidenceAuditor is the most semantically precise -- an independent, limited-scope, documented secondary check.

Minority opinions: IThresholdCalibrator (WIENER, 2 votes), ISecondaryEvaluator (HERACLITUS + PENROSE, 2 votes).

## Doc 03 Re-Vote (D4-R3: 17/20)

"Sila-Prajna Security Framework" -> "Plugin Security Lifecycle"

Initial vote of 14/20 to keep unchanged. Master review triggered re-examination -- all four tests failed: Necessity (no need for seed theory to understand plugin lifecycle), Code identification (actual types use English), Decision-driven (no DC confirmation), Definition responsibility (sila != access control, prajna != CVE revocation).

ASANGA's key distinction: Doc 16 = standalone mapping document (Master ruled to keep) vs Doc 03 = Buddhist decoration in an engineering document (should be cleaned up).

## The Fourth Test -- Definition Responsibility (Permanent Standard)

> **"When using Buddhist Sanskrit terms as code identifiers, the component's functionality must match the term's Buddhist definition. If inconsistent, use engineering terminology."**

Supplements D1's three tests -- even if a name passes Test 2 (code identification), if it fails Test 4 (definition responsibility), it should still be renamed.

Scope of impact: ILoopQualityMonitor affects 6 documents with 100+ replacements; IConfidenceAuditor affects 5 documents; Doc 03 renamed + content cleanup.

---

# Chapter 6: Pure Engineering -- D5 Plan29 Engineering Specification Debate

---

**Duration**: ~75 minutes | **Participants**: 10 | **Votes**: 9 items

D5 was the first debate in the project's history with absolutely no Buddhist content. Ten engineers and scientists, zero Buddhist scholars (NAGARJUNA and ASANGA voluntarily recused), discussing the precise specifications of TypeScript interfaces.

TURING pre-submitted a complete v0.28.0-alpha design pattern report -- 14 source code files, all Registry lifecycles, timeout patterns, synchronous/asynchronous patterns, and failure handling strategies. This "code archaeology" report provided the factual basis for all decisions.

## Nine Resolutions

| Resolution | Content | Votes |
|------------|---------|-------|
| D5-R1 | Dedicated `auditor` hook slot (no reuse of monitors) | 8/8 |
| D5-R2 | audit() dual-mode return `T \| Promise<T>` | **5/8** |
| D5-R3 | Timeout 200ms, fail-safe delta=0, configurable | 8/8 |
| D5-R4 | Single auditor, last-wins (not array) | 6/8 |
| D5-R5 | Failure handling: delta=0 + warning log | consensus |
| D5-R6 | MonitorRegistry starts in ExecutionLoop.onLoopStart() | 7/8 |
| D5-R7 | LoopQualityVector equal weights 0.25x4 | 8/8 |
| D5-R8 | validatePluginSkandha() maintained as warning-only | 7/8 |
| D5-R9 | IConfidenceAuditor extends IVijnana, skandha ['vijnana'] | 8/8 |

**Most contentious vote**: D5-R2 (5/8) -- pure async vs dual-mode. GUARDIAN/KERNEL/VITRUVIUS argued that pure async semantics are more precise; the majority adopted dual-mode, following the IGearArbiter precedent and for testing convenience.

## IConfidenceAuditor Final Specification (100%)

```typescript
export interface IConfidenceAuditor extends IVijnana {
  readonly id: string;
  audit(confidence: number, context: GearContext):
    ConfidenceAuditResult | Promise<ConfidenceAuditResult>;
}
export interface ConfidenceAuditResult {
  delta: number;       // clamped to [-0.05, +0.05]
  reasoning: string;   // audit trail
}
```

PluginHooks final form:
```typescript
interface PluginHooks {
  // ... existing fields ...
  monitors?: ILoopQualityMonitor[];   // Plan29 Wave 1
  auditor?: IConfidenceAuditor;       // Plan29 Wave 2
}
```

NAGARJUNA's comment after D5 concluded: "D4 proved that names must take responsibility for definitions. D5 proved that some engineering problems need no definitions at all -- only specifications."

---

# Chapter 7: Cleanup and Deliverables

---

## Output Overview

After five debates concluded, the team entered R4 deliverable finalization. Core outputs:

### Doc 45: Five Skandha OOP Architecture (New Document)

Authored by VITRUVIUS and KERNEL. Pure engineering language. Structure corresponds to D3's six votes:

1. **Root interface completeness** (D3-R1): Five root interfaces + four independent proofs
2. **PluginHooks mapping** (D3-R2): Nine-item mapping table + TURING source code verification
3. **SlashCommand classification** (D3-R2a/b): Belongs to no skandha + security observation
4. **skandha metadata** (D3-R3): Metadata, not routing
5. **DI wiring** (A2 summary): Pure DI + Composition Root
6. **ExecutionLoop circulation** (A4 summary): Nine-phase skandha mapping + three-layer stability
7. **Cross-skandha interaction** (A5 summary): 5x5 matrix + Model Delta formula
8. **Samskara design notes** (D3-R4a/b): Narrowing rationale + DC-6 continues in effect
9. **ILoopQualityMonitor** (D2+D4): Three-skandha classification + naming history
10. **Appendix A**: Twelve Nidanas functional analogy
11. **Appendix B**: Cognitive Sequence structural parallel

### Document Cleanup Scope

| Action | Items |
|--------|-------|
| **REMOVE** | Doc 38 Buddhist mapping column, Doc 44 Threefold Training mapping, Doc 43 mindfulness decorations (8 instances), Doc 37 Buddhist column, Doc 03 Buddhist mapping table + seed theory annotations, Batch A five distributed mappings |
| **RELOCATE** | Doc 44 S10 remainder -> Appendix_C, Batch B eight items -> respective appendices, B-6 move scripture citation only |
| **KEEP** | Five skandha type names, Klesha module names, CoarisingBundle, vasana design rationale, samsaric stall |
| **Restore** | Doc 16 (Master ruling), Doc 31 (Master ruling) |
| **Rename** | ISatiMonitor -> ILoopQualityMonitor (100+ instances), IPrajna -> IConfidenceAuditor (25+ instances), Doc 03 filename |
| **New** | Doc 45, Appendix_A/B/C |

### Statistics

| Metric | Value |
|--------|-------|
| Formal resolutions | 29 + 6 supplementary |
| Total vote count | 31 |
| Unanimity rate | 66% (all-time high) |
| Total debate duration | ~375 minutes |
| Renaming replacements | 120+ instances |

## Permanent Deliverables

1. **Four-tier framework**: KEEP / RELOCATE / REMOVE / FILE REVIEW + document type precondition check
2. **Four tests**: Necessity, Code identification, Decision-driven, **Definition responsibility**
3. **Doc 45**: Five Skandha OOP Architecture complete engineering document
4. **IConfidenceAuditor 100% specification**: Ready for direct handoff to engineering team

## Known Gaps (Not Architectural Issues)

1. Three weak-inheritance interfaces do not extend root interfaces
2. VedanaAssessment wiring incomplete
3. Delta_audit and Delta_sati are zero in v0.28.0

## Conclusion

Cycle 02-5 answered Master's core question -- how do the five skandhas operate within agent core? The answer: five interfaces, nine Registries, one loop. And it established the boundary principle between Buddhist language and engineering language: Buddhist names are not free -- every Sanskrit identifier is a promise, a promise that function matches definition. If that promise cannot be honored, use engineering terminology.

---
