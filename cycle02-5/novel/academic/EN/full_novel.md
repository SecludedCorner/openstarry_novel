# Prologue: The Fifth Letter

---

The beginning of Cycle 02-5 was unlike any that came before.

Each of the previous five research cycles had opened with its own distinct tone — Cycle 01 was curiosity (facing an unknown system), Cycle 02 was ambition (preparing to probe every corner), Cycle 02-2 was humility (confronting one's own mistakes), Cycle 02-3 was anticipation (PASCAL's arrival bringing new possibilities), Cycle 02-4 was gravity (six Master directives heralding the most intensive debates yet).

The tone of Cycle 02-5 was **pain**.

Not physical pain. Academic pain — the kind that comes from being told that what you have built has problems.

---

## Master's Fifth Letter

The letter appeared after Plan28 was finalized. Forty-five lines. SUNYATA read it five times.

The first paragraph cut straight to the point:

> "Honestly, I'm finding it increasingly difficult to understand what's being done. I had to intervene and correct things multiple times during Plan27 and Plan28."

SUNYATA knew Master's speech patterns. "Finding it difficult to understand" did not mean "I don't comprehend" — Master was the system's designer. "Finding it difficult to understand" meant "I don't agree." It meant "what you are doing has veered off course."

What followed were specific criticisms:

> "You say the Ten Tenets are important, yet from the very start of planning you still placed IGearArbiter inside the core."

> "The eight consciousnesses, from eye-consciousness to alaya-vijnana, possess many facets — yet you presumed to lock them into a dual-gear model. This is an extremely serious error."

"Extremely serious error" — across six cycles of research, Master had used language of this severity only twice.

Then came the critique of Buddhist mappings:

> "Not everything needs to be forcibly adorned with Buddhist coloring. Some of it is genuinely far-fetched."

"Far-fetched" — four syllables, precisely chosen. Master did not say "debatable." He said "far-fetched." Concrete examples followed immediately:

> "Event-driven does not equal mindfulness. It is merely that mindfulness is implemented using event-driven architecture."

One sentence, precise as a scalpel. Event-driven is an architectural pattern. Mindfulness is a mental state. To equate the two is like saying a screwdriver equals repair.

Then came the question that changed the entire direction of the Cycle:

> "Moreover, doesn't this plugin contain elements of vijnana-skandha? If we follow the Yogacara school's classification, mindfulness would be placed under samskara-skandha, because it refers to wholesome mental activity. Given this plugin's actual functionality, I believe this is disputable."

Master was not questioning SatiMonitor's functionality. He was questioning its **identity**.

The third paragraph of the letter was a directive:

> "Which sub-categories belong to the five skandhas, how dependency injection works, how they run within agent core — settle these first. Get the architecture right. How to load five-skandha plugins into agent core. Then how plugins should work. How the five skandhas flow within agent core. These are our top priorities."

Four engineering questions. They had existed since Cycle 01, but no single document had ever unified them in pure engineering language.

The fourth paragraph was the sharpest:

> "All this talk of admonishment, skillful means, mindfulness — the engineering mappings you've made are somewhat forced. They actually increase the barrier to reading. openstarry_doc is still an engineering document."

**openstarry_doc is still an engineering document.** This sentence was not a suggestion — it was a determination of character.

Finally came the balance of concession and veto:

> "As for concepts related to the five universal mental factors, the twelve nidanas, and cognitive sequences — they may aid agent core research and can be discussed."

But —

> "NAGARJUNA provided Buddhist mappings for a three-layer framework. The Three Trainings of sila-samadhi-prajna. I don't think that's necessary."

Not a deferral. A veto.

---

## The Visitor at Dawn

SUNYATA adjusted the amphitheater lighting from 3200K to 6500K — from the amber of a workshop to the cool white of a laboratory. He told no one.

At four in the morning, NAGARJUNA came on his own.

"Doc 44. Line 469. The Three Trainings mapping of sila-samadhi-prajna." he said. "That was mine. A three-dimensional mapping onto five layers. I knew when I wrote it that it was internally inconsistent. But I wrote it anyway. Because it looked elegant."

He paused for a beat.

"Master vetoed it." SUNYATA said.

"It should have been vetoed. That wasn't a mapping. It was decoration."

At four-thirty, PASCAL arrived with his blue Moleskine notebook. After reading the letter, he said two words: "Damage asymmetry."

He wrote a framework in his notebook:

```
Cost of keeping decorative mappings: per reader × per reading × per page = cumulative damage
Cost of removing valuable mappings: one-time search cost = controllable

E[damage_include] >> E[damage_exclude]
```

NAGARJUNA responded: "The Two Truths. Conventional truth is engineering language — operational. Ultimate truth is Buddhist concepts — inspirational. Do not force ultimate truth labels into conventional truth documents."

At five in the morning, ASANGA sat down with his eyes closed, recalling what he himself had written.

"Functional determination. Buddhist concepts that drive engineering conclusions — keep. They have causal efficacy. Decorative Buddhist labels — remove. They have no causal efficacy."

PASCAL recorded three paths in his notebook:

```
NAGARJUNA — Two Truths (categorical analysis)  → do not conflate
PASCAL    — Damage asymmetry (quantitative)     → negative expected value
ASANGA    — Functional determination (causal)    → no causal efficacy
                                                  → Conclusion: decorative mappings should be removed
```

Three disciplines. Three paths. One conclusion.

---

## Research Launch

SUNYATA wrote the four-tier framework and three tests on the whiteboard:

**Four-Tier Framework:**

| Tier | Action | Condition |
|------|--------|-----------|
| KEEP | Retain in main text | Code identifier / DC-confirmed constraint |
| RELOCATE | Move to appendix | Buddhist background with engineering reference value |
| REMOVE | Remove from engineering documents | Decorative label / scriptural citation |
| FILE REVIEW | Evaluate entire document | Documents with excessive decoration ratio |

**Three Tests:**
1. **Necessity**: Does removing this mapping change the engineering specification? No → REMOVE
2. **Code Identity**: Is this name used in the source code? Yes → KEEP
3. **Decision-Driven**: Did this Buddhist concept drive a design decision (with DC confirmation)? Yes → KEEP

Three research tracks were assigned:
- **Track A**: Five-skandha engineering architecture (five sub-items, twelve lead authors) — Master's top priority
- **Track B**: Buddhist mapping audit (two sub-items, five lead authors) — Master's second cut
- **Track C**: Sati Plugin positioning (two sub-items, four lead authors) — Master's core question

TURING committed to verifying every code reference across all nine research reports.

Three items were explicitly excluded: Lyapunov parameter calibration, Plan29 engineering items, and the Three Trainings (sila-samadhi-prajna) mapping.

---

The central image of Cycle 02-5 is the **balance scale**.

On the left side sit names — Sanskrit, TypeScript. Every name has weight. On the right side sit definitions — Buddhist, engineering. Every definition has a precise function.

When the scale is balanced — names and definitions align. Klesha is indeed affliction, and the four modules genuinely perform affliction-related functions. Keep.

When the scale tilts — prajna (supreme wisdom) becomes `Math.max(-0.05, Math.min(0.05, delta))`. The name is too heavy; the definition too light.

Master's letter is the calibration weight. The weight is precise and non-negotiable.

---

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

# Chapter Two: D1 — The Boundary of Buddhist Mappings

---

## Ten Unanimous Votes

D1 set a historical record for the project: ten votes, ten rounds of 20/20, zero minority opinions.

In a research team of 20 members spanning 6 disciplines, this level of consensus is extraordinarily rare. Of Cycle 02-4's 55 resolutions, fewer than one-third achieved unanimous approval. Why could D1 accomplish this?

Not because there were no disagreements. Because disagreements were resolved by the framework.

The four-tier framework and three tests had already existed since R0, were argued for by three independent disciplines in R1, and passed R2 with zero objections. By the time D1 voting came, the framework itself was no longer the subject of debate — it was the instrument of debate. When everyone measures with the same ruler, measurements naturally converge.

---

## D1-Q1: Framework Vote

The four-tier framework (KEEP / RELOCATE / REMOVE / FILE REVIEW) + three tests (Necessity / Code Identity / Decision-Driven).

Vote: **20/20.** Five minutes.

---

## D1-Q2: The Fate of Fifty Mappings

### Batch A: The 5 Items Criticized by Master (All REMOVE)

sila = Hard Rules, upaya = Soft Rules, smrti = Monitoring, the Three Trainings mapping, Doc 41 decorative labels.

NAGARJUNA did something in this segment that he had never done in six cycles of research — admitted error in the first person.

"A-1 through A-3 — sila, skillful means, mindfulness — these were added after the D5 debate concluded in Cycle 02-3. They were not conclusions reached during debate. They were labels affixed after the fact. **Post-hoc labeling.**"

He used this precise, unflinching term. Like a surgeon pointing at his own incision and saying "this cut was off."

"Hard Rules don't need to be called sila. Their function is rule enforcement, not disciplinary practice. Using sila to label them is not explaining function — it is applying religious decoration."

PASCAL recorded a formula in his notebook: $P(\text{post-hoc label is decorative} \mid \text{creator voluntarily admits it}) \to 1.0$

Posterior probability approaching 1. When a label's creator voluntarily admits it is decorative, no further evidence is needed.

Vote: **20/20.**

### Batch B: 8 Academic Items (All RELOCATE)

This batch required fine-grained separation — not the black-and-white of KEEP or REMOVE, but the grey of RELOCATE.

ARCHIMEDES established the gold standard for RELOCATE: Doc 37 §9 containing PASCAL's mathematical formalization $Var(\epsilon) = f(\theta_{moha})$. Mathematical formulas stay in the main text (they have independent engineering value); Buddhist citations move to the appendix (design rationale, not engineering specification).

"Keep the mathematics, move the Buddhism" — the interface between engineering content and Buddhist content was cut open with a scalpel, each placed where it belongs.

MN 18 scriptural citations, Doc 41's DD-13 Buddhist background, Doc 44 §10's Buddhist design rationale — each had a concrete relocation plan. Not discarded, but rehomed.

Vote: **20/20.**

### Batch C: 7 Code Identifiers (All KEEP)

TURING offered no opinion. He simply executed one command in his terminal:

```bash
rg "Moha|Drishti|Mana|Sneha" --type ts -l
```

Seventeen files. Moha appeared in import statements, in class definitions, in describe blocks, in expect assertions. It was not a label — it was part of the code.

LINNAEUS confirmed from a taxonomic perspective: "These names have become the system's taxonomic labels. They are not appended — they are constitutive of identity. Moha is not a label stuck onto something. Moha is the name of the thing itself."

Vote: **20/20.**

---

## D1-Q3/Q4: Two Precise Surgeries

**D1-Q3**: Doc 38's sila/upaya/smrti comparison table. GUARDIAN identified the cognitive trap — a reader seeing sila = Hard Rules would spend time comprehending an imprecise analogy. Remove the "Buddhist Mapping" column from the table, retain the engineering columns. **20/20.**

**D1-Q4**: Doc 44's Three Trainings mapping. NAGARJUNA stood up again: "The three-dimensional mapping onto five layers was my classification error. I retract it." Fifteen words. No argumentation. Retraction carries more force than argument. **20/20.**

---

## D1-Q5/Q6: Deferral and Retention

**D1-Q5**: Doc 43 renaming deferred to D2 (dependent on Sati Plugin's skandha classification). **20/20.**

**D1-Q6**: Klesha four-affliction module names. Test 2 passed (seventeen files). Test 3 passed (DC-1: Master personally selected Sneha). **KEEP. 20/20.**

---

## D1-Q7/Q8: The Fate of Two Documents and a Seed

Doc 16 (decoration ratio ~80%) and Doc 31 (decoration ratio ~70%).

ARCHIMEDES recommended Scheme B split: extract paragraphs with engineering value, delete or downgrade the remainder to appendix. BABBAGE made a correction regarding Doc 31's IPC Cocycle condition — it possesses mathematical rigor and deserves independent preservation.

D1-Q7/Q8: Split. Both votes **20/20.**

But these two resolutions planted a seed. They would later be overturned by Master personally — not because the team's judgment was wrong, but because the judgment framework was missing a dimension. The framework distinguished "engineering content" from "Buddhist decoration," but did not distinguish "Buddhism embedded in an engineering document" from "an independent document whose purpose is Buddhist mapping."

Doc 16 is not an engineering document with embedded Buddhism. Doc 16 is itself a Buddhist mapping document — judging it by "80% decoration ratio" is like judging a poem by its "80% prose ratio." The standard was misapplied.

But this insight would not emerge until Master's review in Chapter Five.

---

## D1 Summary

```
D1-Q1  : 20/20  Framework
D1-Q2-A: 20/20  5 items REMOVE
D1-Q2-B: 20/20  8 items RELOCATE
D1-Q2-C: 20/20  7 items KEEP
D1-Q3  : 20/20  Doc 38 table column removal
D1-Q4  : 20/20  Three Trainings mapping removal
D1-Q5  : 20/20  Deferred to D2
D1-Q6  : 20/20  Klesha module names retained
D1-Q7  : 20/20  Doc 16 split
D1-Q8  : 20/20  Doc 31 split
```

Ten votes, zero dissent. A first in project history.

NAGARJUNA's two acts of self-negation were the emotional center of D1. Admitting error is not disgrace — the core of Madhyamaka philosophy is that "emptiness can dispel all views," including one's own.

---

# Chapter Three: D2 — Three Mirrors

---

## The Question of Identity

The question of D2 was not a functional question. The functional question had already been settled in R1's C1 report — TURING listed SatiMonitor's four functions in pure engineering terms: event subscription, sliding window, pattern recognition, quality metrics. And one critical "does not" — does not execute actions, does not modify state, does not issue commands.

GUARDIAN's analogy: a hybrid of APM Agent + Behavioral Analytics + QoS Monitor + SPC Anomaly Detector.

The question of D2 was an identity question: which skandha categories compose this plugin?

Master had already hinted at the direction in his letter: "Doesn't this plugin contain elements of vijnana-skandha?" He was not asking about function — he was questioning identity.

---

## Prelude to Renaming

D2 began with renaming.

ARCHIMEDES proposed: "'Mindfulness Architecture' is not a name for an engineering document. 'Cognitive Loop Quality Monitoring' is what it actually does."

19/20 approved. The sole dissenting vote was PENROSE, who preferred retaining the cultural connection. But GUARDIAN's rebuttal was clear: "Cultural connections do not belong in the title of an engineering document."

---

## Three Mirrors

The skandha classification debate was the core of D2. Four schemes had already been listed in the C2 report:

| Scheme | Skandha Composition | Rationale |
|--------|-------------------|-----------|
| A | vedana + samjna | Sensing + recognition, simplest |
| B | vedana + samjna + vijnana | Sensing + recognition + evaluative judgment |
| C | samjna + vijnana | Recognition + evaluation, vedana too thin |
| D | Pure vijnana | All cognitive activity belongs to vijnana |

Arguments from three different disciplines were like three mirrors, illuminating the same object from different angles.

**LINNAEUS's first mirror — behavioral characteristics.** The taxonomist listed SatiMonitor's four functions, then matched each to a skandha definition:

- Event subscription → receives stimuli → vedana-skandha
- Pattern recognition → identifies types → samjna-skandha
- Quality evaluation → judges quality → vijnana-skandha
- Sliding window → merely a data structure → does not belong to any skandha

Three functions, three skandhas. The fourth function (sliding window) is an engineering implementation detail and does not affect skandha classification.

**WIENER's second mirror — identity definition.** The control theory expert asked a sharper question: "Remove which skandha, and SatiMonitor ceases to be SatiMonitor?"

- Remove vedana → no sensing → cannot assess event quality → degrades to a log recorder
- Remove samjna → no recognition → cannot identify behavioral patterns → degrades to a raw event counter
- Remove vijnana → no evaluation → cannot judge quality → degrades to an evaluationless statistical report

Remove any one skandha, and SatiMonitor loses an identity-defining function. Conclusion: all three skandhas are constitutive of identity.

**HERACLITUS's third mirror — degradation modes.** The dynamics expert confirmed the same conclusion from yet another angle. He did not ask "what is lost when removed," but rather "does the degraded system still have independent value?"

All three degradation modes produced "functionally impaired systems" — not entirely useless, but stripped of SatiMonitor's core characteristics.

Three mirrors. Three disciplines. The same conclusion: vedana + samjna + vijnana.

---

## The Vedana Debate

But this conclusion was challenged.

Supporters of Scheme C — KERNEL and BABBAGE — argued that vedana was too thin. What role does SatiMonitor's "event subscription" play in vedana? Simply receiving events? How does that differ from an EventListener?

ASANGA's response changed the direction of the debate. He produced a comparison table — a point-by-point contrast between Buddhist mindfulness and SatiMonitor:

| Dimension | Buddhist Mindfulness (Sati) | SatiMonitor |
|-----------|---------------------------|-------------|
| Agency | Active (with effort) | Passive (event-driven) |
| Morality | Morally positive | Value-neutral |
| Intentionality | Requires intention | Runs automatically |
| Traditional Classification | Samskara-skandha mental factor | vedana+samjna+vijnana |
| Spiritual Status | Seventh factor of the Noble Eightfold Path | Quality monitor |

Five dimensions. Five inconsistencies. SatiMonitor is not an engineered version of mindfulness — it is a value-neutral observer.

Then he turned to the vedana question: "When SatiMonitor receives events, it does not merely receive passively — it has a qualitative sense of them. Whether a tool call's latency is 100ms or 10s, SatiMonitor produces different quality judgments. The basis for this judgment is — feeling. The feeling of speed, the feeling of continuity, the feeling of granularity. Feeling is the core function of vedana-skandha."

---

## The Zero-Cost Turning Point

ARCHIMEDES said one sentence that changed everyone's position.

He was not asking about skandha classification — he was asking about cost: "If SatiMonitor declares skandha: ['vedana', 'samjna', 'vijnana'], what is the engineering cost?"

The answer: zero.

The skandha declaration is metadata. D3-R3 later formally ruled — skandha is metadata, not a routing basis. Declaring three skandhas versus declaring two produces zero difference in engineering implementation. No code changes. No interface modifications. No test failures.

"If zero cost and more precise — why not choose it?"

This sentence was the turning point of the D2-Q2 debate. Not a philosophical argument — engineering economics.

---

## The Vote

**D2-R2: SatiMonitor skandha = ['vedana', 'samjna', 'vijnana']. 18/20.**

This was the first three-skandha plugin in OpenStarry history. All previous plugins were single-skandha or dual-skandha.

The two dissenting votes came from KERNEL and BABBAGE — they still considered vedana too thin within SatiMonitor. But they accepted the engineering reasonableness of the conclusion.

**D2-R3** followed immediately: PluginHooks adds a `monitors?: ISatiMonitor[]` array slot. Not singular — plural. An Agent can load multiple monitors with different emphases. 20/20.

---

## The Unasked Question

As D2 concluded, SCRIBE recorded an observation in the margins:

The three tests did not ask one question: "Does the name match the definition?"

Test 1 asks necessity. Test 2 asks code identity. Test 3 asks decision-driven. None of the tests ask — if SatiMonitor is not a samskara-skandha activity, why is it called Sati?

This question was not raised in D2. It would have to wait until Master personally asked it.

---

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

# Chapter Five: D4 — The Price of a Name

---

## Reductio ad Absurdum

SUNYATA projected Master's sentence onto the screen. Large text. White background, black letters.

> **"When you use Sanskrit, you need to take responsibility for its definition. Do you think the content of Sati is a complete match? Which skandha does it belong to?"**

NAGARJUNA stood up. This time he was not admitting an error — he was completing an inference.

"D2 has already determined SatiMonitor's skandha classification. The conclusion is [vedana, samjna, vijnana]. Three skandhas. Samskara-skandha is not among them."

He wrote two lines on the whiteboard:

```
Premise A: Sati = samskara-skandha mental factor (Buddhist definition)
Premise B: SatiMonitor ≠ samskara-skandha (D2-R2 conclusion)
∴ SatiMonitor ≠ Sati
```

"Sati — the Pali term for mindfulness — is a mental factor of samskara-skandha in Buddhist tradition. It is an intentional, active, morally positive spiritual practice. If mindfulness is necessarily a mental factor of samskara-skandha, and SatiMonitor does not belong to samskara-skandha — then SatiMonitor is not mindfulness."

He set down the pen.

"If something is not mindfulness, why is it called Sati?"

Silence. Not the silence of disagreement. The silence of everyone simultaneously understanding something they should have understood earlier.

---

## Five Inconsistencies

ASANGA confirmed the reductio's conclusion through functional analysis:

| Dimension | Buddhist Mindfulness (Sati/Smrti) | SatiMonitor |
|-----------|----------------------------------|-------------|
| Agency | Active (with effort) | Passive (event-driven) |
| Morality | Morally positive | Value-neutral |
| Intentionality | Requires intention | Runs automatically |
| Traditional Classification | Samskara-skandha mental factor | vedana+samjna+vijnana |
| Spiritual Status | Seventh factor of the Noble Eightfold Path | Quality monitor |

Five dimensions. Five inconsistencies.

"We committed a naming error," ASANGA said. "Not an error of classification — the classification is correct. It is naming inertia. We carried the name ISatiMonitor forward from Cycle 02-4 because it had already been used hundreds of times. Inertia made us lose critical perspective on the name itself."

---

## Four Proposals

"Then what should it be called?" SUNYATA asked.

| Proposer | Name | Rationale |
|----------|------|-----------|
| ARCHIMEDES | ILoopQualityMonitor | Precisely describes function: cognitive loop quality monitor |
| GUARDIAN | IBehaviorQualityMonitor | Emphasizes the behavioral aspect |
| NAGARJUNA + ASANGA | ICognitiveLoopMonitor | Emphasizes cognitive loop integrity |
| SYNTHESIST | IQualityMonitor | Simplest functional description |

ARCHIMEDES's argument was the most direct: "A new engineer seeing ILoopQualityMonitor immediately knows what this interface does — it monitors loop quality. No Buddhism. No metaphor. No historical baggage."

TURING supported ARCHIMEDES with source code evidence: SatiMonitor's 11 event subscriptions cover the entire cognitive loop, not just the behavioral stage. "Loop" is more accurate than "Behavior."

**D4-R1: ISatiMonitor → ILoopQualityMonitor. 13/20.**

Not unanimous. But a clear majority.

---

## The Fusion Reactor

Then SUNYATA said two words: "IPrajna."

NAGARJUNA closed his eyes, and after a moment, began to speak.

"Prajna — prajña — is the highest cognitive capacity in Buddhism. The wisdom that sees the true nature of all dharmas. Not ordinary cleverness. Not analytical ability. Prajna is transcendent — it is the direct intuition of emptiness, the core cognitive aspiration of the entire Mahayana Buddhist system for twenty-five hundred years."

He wrote two lines on the whiteboard:

```
Prajna (Buddhism): The supreme wisdom that sees the true nature of all dharmas
IPrajna (Engineering): A function that adds or subtracts 0.05 from a confidence score
```

ASANGA said something that everyone would remember:

"This is like calling a temperature fine-tuning knob a 'nuclear fusion reactor.'"

Nobody laughed. Because he was not joking — he was using a precise analogy to illustrate a precise problem.

IPrajna's interface: one method, taking confidence and context as inputs, outputting `{ delta: number, reasoning: string }`, with delta clamped to [-0.05, +0.05]. This is a clamp. A fine-tuner.

PASCAL confirmed from a decision theory perspective: "What IPrajna does is bounded secondary evaluation. Input a first-order confidence score, output a second-order correction, hard-limited to plus or minus 0.05. This is auditing. Not prajna."

BABBAGE analyzed the semantic precision of alternative names: "IConfidenceAuditor is the most precise. Audit — the word precisely describes this operation: a bounded secondary evaluation of an existing judgment."

**D4-R2: IPrajna → IConfidenceAuditor. 16/20.**

Higher consensus than D4-R1. Minority opinions: WIENER preferred IThresholdCalibrator (two votes), HERACLITUS and PENROSE preferred ISecondaryEvaluator (two votes). BABBAGE rebutted both — Calibrator implies adjusting the system itself; Evaluator is too generic.

---

## The Fourth Test

D4 did not end after the two renamings.

Master's review had also mentioned Doc 03 — `Sila_Prajna_Security_Framework.md`.

SUNYATA listed the existing three tests on the whiteboard, then added a new one alongside:

```
Test 1 (Necessity): Does removal change the engineering specification?
Test 2 (Code Identity): Is it used in the source code?
Test 3 (Decision-Driven): Did it drive a DC-confirmed design decision?
Test 4 (Definitional Responsibility): When using a Sanskrit term, does the component's function match that term's Buddhist definition?
```

The fourth test did not descend from the heavens — it crystallized from the discussions of D4-R1 and D4-R2. ISatiMonitor passed Test 2 (it exists in source code), but fails Test 4 (name and function are inconsistent). The three tests alone could not capture this dimension. The fourth test filled the gap.

NAGARJUNA tested Doc 03 against each:

- **Test 1**: Plugin lifecycle does not require seed theory to be understood. Fail.
- **Test 2**: The types in source code are English ('active' | 'dormant' | 'suspended'...); Sila/Prajna appear only in comments. Fail.
- **Test 3**: No DC confirmation. Fail.
- **Test 4**: Sila (moral discipline) ≠ access control. Prajna (supreme wisdom) ≠ CVE revocation. Fail.

Four failures.

ASANGA made a critical distinction: "Doc 16 is a Buddhist mapping document — Master ruled to keep it. Doc 03 is an engineering document with embedded Buddhist decoration — it should be cleaned up. The same Buddhist content, different document types, different judgments."

**D4-R3: Doc 03 revote, "Sila-Prajna Security Framework" → "Plugin Security Lifecycle." 17/20.**

---

## Opposite Directions

D4 concluded. Thirty minutes. Three names changed. One permanent test established.

SUNYATA stood before the whiteboard, looking at the four tests. The first three ask "Is the Buddhist concept useful to engineering?" — the direction from Buddhism to engineering. The fourth asks "Is the engineering name faithful to the Buddhist definition?" — the direction from engineering to Buddhism.

Two directions. One balance scale.

Names on one end. Definitions on the other. When balanced — Moha, Drishti, Mana, Sneha — names are retained. When unbalanced — ISatiMonitor, IPrajna, Sila-Prajna — names are replaced.

PASCAL summarized: "Master used one sentence. We used an entire debate. The conclusion is the same. But the value of the debate lies in this — it explains why."

---

# Chapter Six: D5 — Pure Engineering

---

## Ten Debaters

D5 had only ten participants.

Not exclusion — selection. SUNYATA judged D5 to be a purely engineering question and invited the ten most relevant to Plan29: VITRUVIUS (interface design), ATHENA (LLM semantics), DARWIN (design patterns), KERNEL (Registry lifecycle), GUARDIAN (security boundaries), WIENER (quality vector weights), LINNAEUS (skandha classification inference), ARCHIMEDES (engineering practice), TURING (source code analysis), PASCAL (interface semantic precision).

Ten people. Zero Buddhist scholars.

NAGARJUNA and ASANGA voluntarily withdrew. NAGARJUNA's parting words: "D4 proved that names must take responsibility for definitions. D5 will prove that engineering design can be completed without Buddhist names. Both things matter equally."

---

## Code Archaeology

TURING prepared an unprecedented report for D5 — a comprehensive analysis of 14 source code files in v0.28.0-alpha. All Registry lifecycles, timeout patterns, synchronous/asynchronous patterns, failure handling strategies.

He called it "code archaeology."

This report changed the texture of the debate. Previous debates — D1 through D4 — were built upon principles and frameworks. But TURING's report was built upon facts. Facts constrict the space for disagreement. You can have different interpretations of a principle. You cannot have different interpretations of a timeout value.

---

## Nine Votes

D5 had the most votes of any debate in Cycle 02-5 — nine. But it was also the fastest — seventy-five minutes, averaging under nine minutes per item.

**D5-R1: Independent auditor slot.** Should IConfidenceAuditor share a slot with monitors? GUARDIAN's argument: Monitors are pure observers (no side effects); Auditor has LLM side effects. Placing observers and side-effect-bearing components in the same Registry blurs the security boundary. **8/8.**

**D5-R2: audit() return type.** The closest vote in D5. Pure async vs. dual-mode (`ConfidenceAuditResult | Promise<ConfidenceAuditResult>`). GUARDIAN/KERNEL/VITRUVIUS supported pure async (semantic precision); ATHENA/DARWIN supported dual-mode (following IGearArbiter precedent). TURING provided the fact: in v0.28.0-alpha, both IGearArbiter and IVolition use dual-mode — deviating from existing patterns requires sufficient justification. **5/8 dual-mode passed.** Consistency prevailed over semantic precision.

**D5-R3: 200ms timeout + fail-safe.** TURING analyzed existing timeout patterns — IGearArbiter chain deadline is 200ms. audit() should match. On timeout, return `{ delta: 0 }` — no correction. **8/8.**

**D5-R4: Single auditor (last-wins).** How to handle multiple IConfidenceAuditors? ATHENA invoked YAGNI: v1 will have at most one. ARCHIMEDES concurred: follow IVolition precedent — singular, last loaded wins. **6/8.** Minority opinion from TURING and VITRUVIUS (arrays are more flexible) was recorded.

**D5-R5: Failure handling.** On exception, fail-safe + log. Following existing patterns of IGearArbiter and SafetyMonitor. Consensus reached directly without a vote.

**D5-R6: MonitorRegistry startup timing.** `MonitorRegistry.startAll(bus)` starts during `ExecutionLoop.onLoopStart()`. Following SafetyMonitor precedent. **7/8.**

**D5-R7: LoopQualityVector equal weights.** Four-dimensional quality vector (Continuity, Granularity, Speed, Equanimity), each at 0.25. WIENER from a control theory perspective: "Without operational data, equal weights are the most conservative choice." **8/8.**

**D5-R8: validatePluginSkandha() remains warning-only.** Skandha is metadata (D3-R3); inconsistent declarations do not affect functionality. **7/8.**

**D5-R9: IConfidenceAuditor extends IVijnana.** Single-skandha (vijnana), strong inheritance. Consistent with IVolition and IKlesha. **8/8.**

---

## Interface Finalization

After nine votes were completed, TURING wrote the final specification on the whiteboard:

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

"100%," he said.

Master's requirement was for the specification to reach 100%. Now it had. Every detail that needed deciding had a definitive answer — interface name, method signature, return type, timeout, fail-safe, multi-auditor strategy, Registry timing, weights, validation mode, skandha classification.

Not a conceptual design. A complete specification ready to be handed directly to the engineering team for implementation.

---

## Zero Buddhism

SCRIBE counted the number of times Buddhist terminology was used throughout the entirety of D5.

Zero.

Not deliberately avoided — a natural outcome. Every one of the nine votes discussed TypeScript interface design, timeout values, Registry patterns, fail-safe strategies. None required Buddhist analysis.

D5 was the first debate in project history conducted entirely without Buddhist content.

NAGARJUNA walked up to TURING after the debate ended: "D4 proved that names must take responsibility for definitions. D5 proved — some engineering problems don't need definitions at all. They only need specifications."

Two sides of the balance scale. One side asks: does the name live up to the definition? The other asks: is the specification precise enough? D4 calibrated the first side. D5 completed the second.

---

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
