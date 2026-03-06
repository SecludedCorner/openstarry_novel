# Chapter 2: Boundaries

---

## I. Zero Minority Opinions

D1's opening had no ceremony.

Unlike Cycle 02-3's D1 opening — that time there was PASCAL's self-introduction, graph theory formulas, the symbolism of "the twentieth seat." Nor like Cycle 02-4's D1 — where four IGearArbiter Schemes were laid on the table, undercurrents already surging before the debate began.

Cycle 02-5's D1 opening was SUNYATA standing before the whiteboard, writing a question in red marker:

**"What are the principles for Buddhist content in openstarry_doc engineering documents?"**

One question. But the answer to this question would determine the fate of thirteen documents, the disposition of fifty mapping instances, and the boundary line for all of the research team's future work.

---

The D1-Q1 vote took only five minutes.

Not because there was no disagreement. It was because disagreement had been absorbed by the framework at R0.

The four-tier framework (KEEP / RELOCATE / REMOVE / FILE REVIEW) and three tests (Necessity / Code Identity / Decision Driver) were established at R0 by SUNYATA, NAGARJUNA, PASCAL, and ASANGA. In R1's B2 research report, this framework was argued from three completely different angles — NAGARJUNA's two truths, PASCAL's damage asymmetry, ASANGA's functional determination — three paths, one conclusion. In R2's cross-review, not a single reviewer raised an objection to the framework itself.

When a framework is simultaneously supported by three independent theoretical systems, the debate is not "whether to accept this framework" but "whether any counterexample can overturn it."

No one raised a hand. No one asked a question.

SUNYATA initiated the vote.

20/20.

Unanimous.

ARCHIMEDES drew a checkmark in his notebook. Then he turned to the next page — the B1 audit report's 50 specimens, divided into three batches, awaiting batch-by-batch voting.

---

## II. NAGARJUNA's Confession

D1-Q2 was item-by-item adjudication. 50 mapping instances. Three batches.

**Batch A**: 5 mappings explicitly criticized by Master.

SUNYATA projected the five mappings on screen:

1. Sila (precepts) = Hard Rules
2. Upaya (skillful means) = Soft Rules / Adaptive
3. Smrti (mindfulness) = Monitoring / Event-driven
4. The Three Trainings mapping
5. Two additional decorative labels in Doc 41

These five were all directly named and criticized by Master in his letter. In theory, this should have been the simplest vote — Master had already taken a position.

But SUNYATA did not want this vote to become a rubber stamp. He wanted the team to reach the same conclusion on their own, using their own framework.

"Three tests. Item by item." he said.

NAGARJUNA stood up.

In debates, when NAGARJUNA stood up it usually meant he was about to cite scripture — a certain chapter, a certain verse of the Mulamadhyamakakarika. His posture was solemn, like a dharma teacher preparing to give a discourse at a ceremony. His voice was typically steady, carrying the echo of a monastery corridor.

But this time, he stood up not to cite scripture. He stood up to acknowledge.

"A-1 through A-3 — precepts, skillful means, mindfulness —" he said. His voice was still steady. But within that steadiness was a new texture — not a dharma teacher's solemnity, but a scholar's candor.

"These were added after the D5 debate ended in Cycle 02-3."

He paused. Twenty faces watched him.

"Not conclusions derived from debate. Labels added after the fact."

Another pause.

"**Post-hoc labeling.**" He used this term. Precise, unflinching. Like a surgeon pointing at his own incision and saying "this cut was crooked."

"Hard Rules don't need to be called sila." he continued. "Their function is rule enforcement, not precept practice. Using sila to label them is not describing function — it's performing —" he paused, as if weighing a word's gravity.

"Performing religious decoration."

---

Three seconds of silence in the amphitheater.

Three seconds is a long time in a debate. Long enough for everyone to digest what NAGARJUNA had just said. A Buddhist scholar — the team's most senior Madhyamaka specialist — had with his own hands torn off a label he himself had affixed. This was not being refuted by others. Not retreating in debate. It was voluntary acknowledgment.

PASCAL wrote a formula in his notebook. His finger paused on the paper — the tapping motion he made when calculating expected values — then wrote:

$$P(\text{post-hoc label is decorative} | \text{creator voluntarily admits}) \to 1.0$$

Posterior probability approaching 1. When the label's creator admits it is decorative, no further evidence is needed.

GUARDIAN raised his hand. Not to object — to add an observation.

"From a security document perspective." he said. His voice carried a security expert's characteristic prudence — every word like a risk assessment. "The sila label increases the reader's cognitive load. Readers need to simultaneously understand two terminology systems — engineering and Buddhist. If sila and Hard Rules are the same thing, why give it two names? If they're not the same thing, then this table is making an imprecise analogy. Either way, it's harmful to security documentation."

ARCHIMEDES nodded. A pragmatist's confirmation — no philosophical argument needed, one engineering fact was enough.

D1-Q2-A: 5 Master-criticized mappings -> all REMOVE.

20/20.

---

## III. Fine-Grained Separation

**Batch B**: 8 academic content items.

This batch was more nuanced. Not black-and-white KEEP or REMOVE — gray-zone RELOCATE.

ARCHIMEDES unfolded the Batch B list from the B1 audit report. Eight mapping instances, each with "residual engineering reference value" but not engineering spec itself.

The first case set the template for the entire RELOCATE disposition.

Doc 37. Section 9. PASCAL's mathematical formalization from Cycle 02-4 for Klesha gain scheduling — $Var(\epsilon) = f(\theta_{moha})$. The formula itself was pure mathematics — it described how the Moha parameter affects the variance of random perturbation. But the formula's context included Buddhist citations — explaining why "delusion" (moha) was used to name this parameter.

ARCHIMEDES performed fine-grained separation.

"The mathematical formalization stays in the main text." he said. "Var(epsilon) = f(theta_moha) has independent engineering value — it describes a measurable system behavior. But the Buddhist citations — why moha corresponds to 'delusion,' why the four Buddhist afflictions are used to organize gain scheduling — these are design rationale, not engineering spec. Move to appendix."

This "retain the mathematics, move the Buddhism" fine-grained separation became the gold standard for RELOCATE dispositions. Each RELOCATE case was handled this way: find the interface between engineering content and Buddhist content, cut along it with a scalpel, engineering content stays in place, Buddhist content moves to appendix.

The MN 18 scripture citation moved from Doc 38's main text to appendix. Doc 41's DD-13 Buddhist background explanation moved to appendix. Doc 44 Section 10's Buddhist design rationale moved to Appendix_C. Each item had a concrete placement plan — not discarded, but relocated.

D1-Q2-B: 8 academic content items -> all RELOCATE.

20/20.

---

## IV. Proof of Identity

**Batch C**: 7 code identifiers and DC confirmations.

This was the clearest case group for Test 2 (Code Identity Test) among the three tests.

Skandha type names. CoarisingBundle's omnipresent mental factor structure. Klesha's four affliction module names — Moha (self-delusion), Drishti (self-view), Mana (self-pride), Sneha (self-love). DC-1 through DC-12 confirmed constraints.

TURING did a very TURING thing.

He did not express an opinion. He simply executed a command on his terminal:

```bash
rg "Moha|Drishti|Mana|Sneha" --type ts -l
```

Seventeen files appeared on screen. Seventeen. From `klesha/moha.ts` to `tests/klesha.spec.ts` — Moha was not a label; it was part of the code. It appeared in import statements, in class definitions, in describe blocks, in test expect assertions.

"Test 2 passes." TURING said. Three words.

Then he executed another line:

```bash
rg "CoarisingBundle|Skandha|Vedana|Samjna|Samskara|Vijnana" --type ts -l
```

More files. The names of the five skandhas permeated every corner of the type system. `IRupa`, `IVedana`, `ISamjna`, `ISamskara`, `IVijnana` — these were not decoration. These were root interfaces. They defined the type structure of the entire plugin system.

DARWIN added a software engineering perspective: "Renaming Moha to Ignorance wouldn't increase clarity — it would increase unfamiliarity. Developers worldwide have already seen Moha in the docs, Moha in the code, Moha in the tests. The cost of renaming is irreversible."

LINNAEUS confirmed from the taxonomy angle: "These names have become the system's taxonomic labels. They're not additive — they're identity-defining. Moha is not a label pasted on something. Moha is the thing's name."

D1-Q2-C: 7 code identifiers and DC confirmations -> all KEEP.

20/20.

---

Three Batches. 5 + 8 + 7 = 20 mappings. Three unanimous votes.

SUNYATA wrote beside the counter on the whiteboard:

```
D1-Q1: Framework   -- 20/20
D1-Q2-A: REMOVE    -- 20/20
D1-Q2-B: RELOCATE  -- 20/20
D1-Q2-C: KEEP      -- 20/20
```

Four votes, zero dissent.

---

## V. Two Scalpels

D1-Q3 and D1-Q4 were two precise surgeries.

**D1-Q3**: The sila/upaya/smrti comparison table in Doc 38. Three columns, six rows, each row a forced pairing of a Buddhist concept and an engineering concept.

GUARDIAN raised his hand again. His observation was as precise as before:

"The very existence of this table is a cognitive trap. A reader sees sila = Hard Rules and tries to understand what sila means. Then they discover that the Buddhist definition of sila (precepts, moral restraint, self-discipline) and the engineering definition of Hard Rules (inviolable safety rules, programmatic boundary conditions) share only superficial similarity. They spent time understanding an imprecise analogy when they could have spent the same time understanding the engineering spec itself."

No one objected.

D1-Q3: REMOVE. 20/20.

**D1-Q4**: The Three Trainings mapping table in Doc 44.

NAGARJUNA stood up again. Briefer this time.

"Three dimensions mapping to five layers was my classification error. I retract it."

One sentence. Fifteen words. No argument. No elaboration.

Retraction was more powerful than argument.

D1-Q4: REMOVE. 20/20.

---

## VI. The Fate of Two Documents

The latter half of D1 entered more complex territory.

**D1-Q5**: Should Doc 43 be renamed? SUNYATA made a procedural decision — "Doc 43's naming depends on the D2 debate's conclusion regarding the Sati Plugin's skandha classification. Deferred." Unanimous agreement to defer.

**D1-Q6**: Klesha's four affliction module names. Moha, Drishti, Mana, Sneha — retain or rename?

TURING had already answered this question with his search results. But SUNYATA wanted the team to walk through the complete logic.

Test 2: Are Moha/Drishti/Mana/Sneha used in source code? -> Yes. Seventeen files.

Test 3: Did they drive design decisions? -> Yes. DC-1 confirmed the affliction module naming — Master personally chose Sneha to replace "self-love."

Both tests passed. KEEP.

D1-Q6: 20/20.

---

Then came D1-Q7 and D1-Q8.

Two suspicious documents. Doc 16 and Doc 31. The two that ARCHIMEDES had flagged as FILE REVIEW in the B1 audit — decoration ratios of approximately 80% and 70% respectively.

This was the only topic in D1 that generated substantial discussion.

ARCHIMEDES presented the audit results for both documents.

"Doc 16: Plugin Type Philosophical Mapping." he said. "Core engineering content is concentrated in Section 5 — three Observer Pattern composition approaches (Pattern A/B/C). The remaining 80% is philosophical mapping of Buddhist concepts to software patterns. Proposed Scheme B: extract Section 5 as an independent document `16_Observer_Composition_Pattern.md`, delete the rest."

BABBAGE immediately raised his hand. He pushed up his glasses — this motion meant he was about to perform precise formal analysis.

"Doc 31 Section 6.3's IPC Cocycle condition has mathematical rigor." he said. "It's not a Buddhist mapping — it's a formalized concurrency constraint. It deserves independent preservation. Suggest modifying Scheme B: Section 3.1 merges into Doc 35 (sensory processing), Section 6.3 becomes independent as `31_IPC_Cocycle_Condition.md`, remainder demoted to Appendix_B."

BABBAGE's modification was accepted.

D1-Q7: Doc 16 split. 20/20.
D1-Q8: Doc 31 split (with BABBAGE's modification). 20/20.

---

Ten votes. Ten unanimous passes.

D1 concluded.

SUNYATA looked at the ten rows of tallies on the whiteboard:

```
D1-Q1  : 20/20
D1-Q2-A: 20/20
D1-Q2-B: 20/20
D1-Q2-C: 20/20
D1-Q3  : 20/20
D1-Q4  : 20/20
D1-Q5  : 20/20 (deferred)
D1-Q6  : 20/20
D1-Q7  : 20/20
D1-Q8  : 20/20
```

A first in the project's history: zero minority opinions across the entire session.

---

> *SCRIBE's aside*

> *D1 was a battlefield cleanup without a war.*

> *Ten votes. Ten 20/20s. Zero minority opinions. In a 20-member team spanning 6 disciplines, this degree of consensus is extraordinarily rare. Cycle 02-3's highest consensus record was D6's (Amended Gamma) 20/20 — but that was only one vote, not ten. Among Cycle 02-4's 55 resolutions, fewer than a third were unanimous.*

> *Why did D1 achieve ten unanimous votes?*

> *Not because there was no disagreement. Disagreement existed — ARCHIMEDES hesitated when auditing Doc 16, BABBAGE had modifications to Doc 31's disposition, GUARDIAN had independent security observations for each Batch A item. Disagreement did not cease to exist. Disagreement was resolved by the framework.*

> *The four-tier framework and three tests were not invented during the debate — they existed since R0. In R1 they were argued by three independent disciplines. In R2 they passed with zero objections. By the time of D1's votes, the framework itself was no longer the subject of debate — it was the tool of debate. When everyone measures on the same ruler, the measurements naturally agree.*

> *NAGARJUNA's two times standing up were D1's emotional center of gravity. The first time — "post-hoc labeling" — he acknowledged his own misstep. The second time — "I retract it" — he executed the correction. In academic research, admitting error requires more courage than proving correctness. PASCAL described this with a formula: the posterior probability of creator-admitted decoration approaches 1.0. But what the formula cannot describe is NAGARJUNA's posture when he stood — not deflated, but upright. Admitting error is not disgrace. Admitting error is the core of Madhyamaka philosophy — emptiness can dispel all views. Including one's own views.*

> *But D1 held a hidden seed. The split decisions for D1-Q7 and D1-Q8 — Doc 16 and Doc 31 being split — would later be overturned by Master's own hand. The reason was not that the team's judgment was wrong, but that the team's judgment framework was still missing a dimension. The framework distinguished between "engineering content" and "Buddhist decoration" but did not distinguish between "Buddhism embedded in an engineering document" and "an independent document whose purpose is Buddhist mapping."*

> *Doc 16 was not an engineering document with embedded Buddhism. Doc 16 was itself a Buddhist mapping document — its raison d'etre was to provide systematic cross-referencing between Buddhism and engineering. Judging it by "decoration ratio 80%" was like judging a poem by "prose ratio 80%" — the wrong standard.*

> *But this insight would not appear until D4. It would await Master's own pointing out.*

> *For now, in the glow of D1's ten 20/20s, no one saw that seed.*

---
