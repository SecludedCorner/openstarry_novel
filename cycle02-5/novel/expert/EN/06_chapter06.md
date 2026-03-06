# Chapter 6: The Cost of Names

---

The amphitheater's lighting had not changed. Still the same 6500K cold white. But somehow, the temperature of the air had shifted.

Not the physical temperature. A feeling — like a classroom before an exam begins, or the wait before a courtroom verdict. Everyone sat in their place, but no one was truly resting.

SUNYATA walked to the projection screen and put Master's sentence on display.

Large text. Black on white. No formatting.

> **"Using Sanskrit means you need to be accountable to its definition. Do you think Sati's content is a complete match? Which skandha does it belong to?"**

---

## I. Reductio

NAGARJUNA stood up.

Throughout Cycle 02-5, he had already stood up many times — acknowledging "post-hoc labeling" in D1, analyzing the twelve links' scale mismatch in D3. Each time he maintained the upright posture characteristic of a Madhyamaka scholar — admitting error was a core academic skill, and he never shied from it.

But this time was different.

This time he was not admitting error. He was completing an inference.

"D2 has already determined SatiMonitor's skandha classification," he said, his voice half a tone lower than usual. Not from nervousness — because he was organizing an argument he had thought about for a long time but never voiced.

"The conclusion was [vedana, samjna, vijnana]. Three skandhas. No samskara."

He paused.

"Sati — the Pali word for mindfulness — is a mental factor of samskara-skandha in Buddhist tradition. It is a cetasika, a volitional, active, morally positive practice activity. The Abhidharma places it under samskara because mindfulness is a practice — something you must intentionally do."

He turned to ASANGA. ASANGA nodded slightly. He knew what NAGARJUNA was about to say.

"Now," NAGARJUNA said, "let me perform a reductio ad absurdum — prasanga. This is the fundamental method of Madhyamaka."

He wrote two lines on the whiteboard:

```
Premise A: Sati = samskara-skandha mental factor (Buddhist definition)
Premise B: SatiMonitor ≠ samskara (D2-R2 conclusion)
```

Then he wrote a third line below:

```
∴ SatiMonitor ≠ Sati
```

"If mindfulness (Sati) necessarily belongs to samskara-skandha in Buddhism, and we have proven that SatiMonitor is not samskara — then SatiMonitor is not mindfulness."

He put down the pen.

"Something that is not mindfulness — why is it called Sati?"

---

Silence.

Not the silence of disagreement. The silence of — everyone simultaneously understanding something they should have understood sooner.

D2's SCRIBE aside had written: "The three tests did not ask this question. Test 1 asked 'does removal change the spec?' Test 2 asked 'is it used in source code?' Test 3 asked 'did it drive a design decision?' Not one test asked 'does the name match the definition?'"

What NAGARJUNA had just done — was ask that omitted question.

The three tests could judge whether a Buddhist mapping had engineering value. But they could not judge whether a name lived up to its definition. ISatiMonitor passed Test 2 — it was used in source code. But it did not pass a more fundamental standard — its name was inconsistent with its function.

---

## II. Confirmation

ASANGA spoke next. He did not stand — he sat in his seat, both hands flat on the desk, like a senior professor giving a final summary in class.

"NAGARJUNA's reductio is formally correct. Let me confirm with functional analysis."

He produced an expanded version of the D2 comparison table:

| Dimension | Buddhist Mindfulness (Sati/Smrti) | SatiMonitor |
|-----------|----------------------------------|-------------|
| Agency | Active (atapi, ardent effort) | Passive (event-driven) |
| Morality | Morally positive (kusala) | Value-neutral |
| Volition | Requires intention (cetana) | Runs automatically |
| Traditional classification | Samskara-skandha mental factor | vedana+samjna+vijnana (D2-R2) |
| Practice status | Seventh factor of the Noble Eightfold Path | Quality monitor |

Five dimensions. Five inconsistencies.

"If SatiMonitor is not a samskara activity," ASANGA said, his voice as steady as if reading a pre-confirmed conclusion, "then it is not Sati. Our own classification analysis negates our own naming."

He paused.

"We made an error. Not a classification error — the classification was correct. A naming error. When we carried over the name ISatiMonitor during Cycle 02-4, it was because the name had already been used hundreds of times in our discussions. Inertia made us lose our critical eye toward the name itself."

---

## III. The New Name

SUNYATA asked: "Then what should it be called?"

Four proposals were put forward within minutes:

| Proposer | Name | Rationale |
|----------|------|-----------|
| ARCHIMEDES (#16) | ILoopQualityMonitor | Precisely describes function: quality monitor for the cognitive loop |
| GUARDIAN (#11) | IBehaviorQualityMonitor | Emphasizes the behavioral layer of quality monitoring |
| NAGARJUNA (#7) + ASANGA (#8) | ICognitiveLoopMonitor | Emphasizes completeness of the cognitive loop |
| SYNTHESIST (#1) | IQualityMonitor | Most simplified functional description |

The debate was shorter than expected.

ARCHIMEDES' argument was the most direct: "What does this interface monitor? The cognitive loop. What does it monitor? Quality. Combine in engineering terms: Loop Quality Monitor. No Buddhism. No metaphor. No historical baggage. A new engineer seeing ILoopQualityMonitor immediately knows what this interface does — monitors loop quality."

GUARDIAN's IBehaviorQualityMonitor received four votes. His argument was that "behavior" was more specific than "loop" — but TURING pointed out that SatiMonitor's 11 event subscriptions covered the entire cognitive loop, not just the behavioral phase.

NAGARJUNA and ASANGA's ICognitiveLoopMonitor received two votes. BABBAGE objected: "Cognitive is a human cognitive science term. In a software engineering context, Loop is already precise enough. No need to add Cognitive."

SYNTHESIST's IQualityMonitor was the most concise but also the most vague — only one vote. VITRUVIUS pointed out: "Quality Monitor could be a quality monitor for anything. Loop Quality Monitor scopes it down."

---

**D4-R1 vote: ISatiMonitor -> ILoopQualityMonitor. 13/20.**

Not unanimous. Not as clean as D1. But the majority was clear.

SUNYATA wrote the complete renaming table on the whiteboard:

| Old Name | New Name |
|----------|----------|
| ISatiMonitor | ILoopQualityMonitor |
| SatiMonitor | LoopQualityMonitor |
| SatiQualityVector | LoopQualityVector |
| SatiQualityReport | LoopQualityReport |
| SatiSPCState | LoopSPCState |
| SatiMonitorConfig | LoopQualityMonitorConfig |
| sati:quality_report | loop:quality_report |
| monitors?: ISatiMonitor[] | monitors?: ILoopQualityMonitor[] |

Eight names. Eight replacements.

D2-R1 had said "retain Sati as a code identifier." D4-R1 overturned D2-R1 — because between D2 and D4, Master had asked a question D2 had not asked: "Does the name live up to its definition?"

---

## IV. The Fusion Reactor

Then SUNYATA said one word:

"IPrajna."

The amphitheater's air shifted again.

If ISatiMonitor's problem was "name and function inconsistent," then IPrajna's problem was —

NAGARJUNA closed his eyes. A moment later he opened them and began to speak.

"Prajna," he said, "is the highest cognitive capacity in Buddhism."

His voice carried a weight that was almost reverence — not for the research team, but for the word itself.

"Prajna — prajña — in Buddhism is the wisdom that perceives the true nature of all dharmas. Not ordinary cleverness, not analytical ability, not the accumulation of knowledge. Prajna is transcendent — it is the direct intuition of emptiness, the illumination of reality, the core cognitive goal of the entire Mahayana Buddhist system for two thousand five hundred years."

He turned to the whiteboard and wrote two lines:

```
Prajna (Buddhism): The highest wisdom that perceives the true nature of all dharmas
IPrajna (engineering): A function that adds or subtracts 0.05 from a confidence score
```

ASANGA said from his seat a sentence that would be remembered by everyone:

"That's like calling a temperature fine-tuning knob a 'nuclear fusion reactor.'"

---

No one laughed.

Because ASANGA was not joking. He was using a precise analogy to illustrate a precise problem.

What was IPrajna's interface definition? One method. Input was confidence and context. Output was `{ delta: number, reasoning: string }`. Delta was clamped to the range [-0.05, +0.05].

This was a clamp. A fine-tuner. An audit function that made ±0.05 corrections on top of an existing confidence score.

Calling it IPrajna — prajna — the highest wisdom that perceives the true nature of all dharmas —

PASCAL wrote in his notebook: "From a decision theory perspective, what IPrajna actually does is bounded secondary evaluation. Input is first-order confidence; output is second-order correction with a hard limit of ±0.05. This is auditing. Not prajna."

BABBAGE followed up: "IConfidenceAuditor is the most semantically precise name. This interface has one method, input is confidence plus context, output is an audit result. Audit — precisely describes this operation: a limited-scope secondary evaluation of an existing judgment."

---

**D4-R2 vote: IPrajna -> IConfidenceAuditor. 16/20.**

Higher consensus than D4-R1.

Minority opinions: WIENER preferred IThresholdCalibrator (two votes) — from a control theory perspective he saw "calibration" rather than "auditing." HERACLITUS and PENROSE preferred ISecondaryEvaluator (two votes) — they felt "audit" implied post-hoc checking, but IPrajna participated in real-time during the decision flow.

BABBAGE countered both minority opinions: "Calibrator implies adjusting the system itself — but IConfidenceAuditor doesn't change the system; it only proposes limited corrections to a number. Evaluator is too generic — any function performs evaluation. Auditor has the most precise semantic boundaries: independent, limited-scope, producing documented secondary checking."

The complete renaming table:

| Old Name | New Name |
|----------|----------|
| IPrajna | IConfidenceAuditor |
| IPrajnaAdjustment | ConfidenceAuditResult |
| prajnaAdjust() | clampAuditDelta() |
| Delta_prajna | Delta_audit |
| Model Delta second layer name | Confidence Audit |

---

## V. The Third Trial

SUNYATA had thought D4 would end here. Two names. Two renamings. ISatiMonitor and IPrajna.

But Master's review had one more section.

"Doc 03."

Doc 03 — `Sila_Prajna_Security_Framework.md` — the Sila-Prajna Security Framework.

---

This document was originally not on D4's agenda. Its name contained Sila (precepts) and Prajna (wisdom) — but in D1, the team had voted 14/20 to retain it unchanged. The rationale: the Buddhist terms in the filename were "background explanation" rather than "code identifiers."

But now, in D4's context, after Master's "using Sanskrit means you need to be accountable to its definition" —

SUNYATA said: "We need to re-examine Doc 03. Using the standard we just established."

He listed four tests on the whiteboard — no, three tests. Then he added a new one beside them.

```
Test 1 (Necessity): Does removal change the engineering spec?
Test 2 (Code Identity): Is it used in source code?
Test 3 (Decision Driver): Did it drive a DC-confirmed design decision?
Test 4 (Definitional Accountability): When using Sanskrit terms, does the component's function match the term's Buddhist definition?
```

The fourth test.

It did not descend from heaven — it crystallized from the D4-R1 and D4-R2 discussions. ISatiMonitor's problem was not that it had no engineering value (it did), not that it wasn't in source code (it was), not that it didn't drive design decisions (it did). Its problem was — its name was inconsistent with its definition.

The three tests had not captured this dimension. The fourth test filled this gap.

---

NAGARJUNA picked up the pen and marked four crosses beside Doc 03's four test results:

**Test 1 (Necessity)**: The plugin lifecycle's five states (CREATED -> LOADING -> LOADED -> STARTING -> RUNNING -> STOPPING -> DISPOSING -> DISPOSED) can be understood without seed theory (bija). ❌ Does not pass.

**Test 2 (Code Identity)**: The actual types in source code are in English — `'active' | 'dormant' | 'suspended' | 'revoked' | 'retired'`. Sila and Prajna only appear in TypeScript comments, not as code identifiers. ❌ Does not pass.

**Test 3 (Decision Driver)**: No DC confirmation. ❌ Does not pass.

**Test 4 (Definitional Accountability)**: The Buddhist definition of Sila (precepts) is moral norms, monastic precepts, community rules of conduct. But in Doc 03, Sila was used to mean "access control" — a plugin's security permission management. Precepts ≠ access control. Prajna (wisdom) was used to mean "CVE revocation mechanism" — a security vulnerability automated response process. Prajna ≠ CVE revocation. ❌ Does not pass.

Four tests. Four failures.

---

"I retract my D1 vote," NAGARJUNA said.

"I also retract mine," ASANGA said.

ASANGA added a key distinction: "Doc 16 is an independent Buddhist mapping document — its raison d'etre is to provide systematic cross-referencing. Master ruled to retain it, because mapping documents are not decoration. But Doc 03 is not a mapping document — it is an engineering document with embedded Buddhist decoration. The difference: Doc 16's Buddhist content is the substance. Doc 03's Buddhist content is decoration. Same Buddhist content, different document types, different judgments."

This was precisely the dimension Master had added in Chapter 5 — document type. ASANGA applied it to a concrete case.

---

**D4-R3 re-vote: Doc 03 "Sila-Prajna Security Framework" -> "Plugin Security Lifecycle." 17/20.**

From 14/20 retain unchanged to 17/20 rename and clean up. Same document, same people, different conclusion. What was the difference? The fourth test.

HERACLITUS led the minority opinion (three votes): "Seed theory has educational value as Buddhist background — it helps understand the Plugin lifecycle's 'dormant -> germinating -> growing -> withering -> seed recycling' metaphor. Even if it fails the four tests, retaining it as an appendix has cultural value."

The majority responded: "Appendix retention can be discussed separately. But the document title and main text's Buddhist decoration should be cleaned up. Buddhist decoration in engineering documents and Buddhist explanation in appendices are two different things."

Cleanup scope confirmed:
1. Filename change (Sila_Prajna_Security_Framework -> Plugin_Security_Lifecycle)
2. Remove Buddhist mapping tables
3. Clean up seed theory mappings in TypeScript comments
4. Retain all engineering content (five-state model, state transition diagram, three-layer security model)

---

## VI. The Fourth Test

Before D4 ended, SUNYATA asked one final question: "Should the fourth test — definitional accountability — become a permanent standard?"

No vote was needed. Everyone nodded.

NAGARJUNA made the final statement: "The first three tests ask about engineering value. The fourth test asks about semantic integrity. Even if a name passes Test 2 — it's used in source code — if it doesn't pass Test 4 — its function doesn't match its Buddhist definition — it should still be renamed."

"ISatiMonitor passed Test 2. It was in source code. But it didn't pass Test 4 — because it's not mindfulness. So it was renamed."

"IPrajna, if implemented, would also pass Test 2. But it would not pass Test 4 — because adding and subtracting 0.05 is not prajna. So it was renamed preemptively."

"The essence of the fourth test is: **when you use a Buddhist Sanskrit term as a code identifier, the component's function must match the term's Buddhist definition. If inconsistent, use engineering terminology.**"

PASCAL added from the side: "This is isomorphic to Master's original words. 'Using Sanskrit means you need to be accountable to its definition.' Master said it in one sentence. We took an entire debate. Same conclusion. But the debate's value is that — it explains why."

---

## VII. Impact Scope

D4's three resolutions produced enormous cascading effects.

TURING opened his impact scope analysis:

**ILoopQualityMonitor (formerly ISatiMonitor):**

| Document | Replacements needed |
|----------|-------------------|
| Doc 43 (Sati Architecture) | 75+ instances |
| Doc 44 (Security Architecture) | 18+ instances |
| Doc 42 (Five-skandha Linkage) | 3 instances |
| Doc 37 (Klesha Architecture) | 2 instances |
| Doc 45 (new document) | 4 instances |
| README | 1 instance |
| CHANGELOG | New entry |

**IConfidenceAuditor (formerly IPrajna):**

| Document | Replacements needed |
|----------|-------------------|
| Doc 44 (Security Architecture) | 15+ instances |
| Doc 37 (Klesha Architecture) | 3 instances |
| Doc 45 (new document) | 4 instances |
| Doc 41 (Design Decisions) | 2 instances |
| Doc 14 (Deep Analysis) | 1 instance |
| CHANGELOG | New entry |

**Doc 03 (Plugin Security Lifecycle):**

| Item | Action |
|------|--------|
| Filename | Rename |
| Buddhist mapping table | Remove |
| TypeScript comments | Clean up |
| Five-state model | Retain |
| Three-layer security model | Retain |

Total: over 120 document modifications.

ARCHIMEDES looked at the number and said something an engineer would say: "This is why early renaming matters. TURING confirmed that v0.28.0-alpha has no actual implementation of ISatiMonitor or IPrajna yet. If we waited until after they were implemented to rename —"

He didn't finish. Everyone understood.

---

## VIII. The Scale

D4 was over.

Thirty minutes. Not long. But its density exceeded D3's two hours.

Three votes. Three names changed. One permanent test standard established.

SUNYATA did not give a summary. He stood before the whiteboard, looking at the four tests written there.

```
Test 1: Necessity (Does removal change the engineering spec?)
Test 2: Code Identity (Is it used in source code?)
Test 3: Decision Driver (Did it drive a DC-confirmed design decision?)
Test 4: Definitional Accountability (Does the component's function match the Sanskrit term's Buddhist definition?)
```

The first three had existed since R0. The fourth was born from D4.

What was the difference? The first three asked "does this Buddhist concept have engineering value?" The fourth asked "does this engineering component deserve this Buddhist name?"

Opposite directions.

The first three ran from Buddhism to engineering — is the Buddhist concept useful to engineering? The fourth ran from engineering to Buddhism — is the engineering name faithful to the Buddhist definition?

Two directions. One scale.

Names on one end. Definitions on the other. When the scale balanced — Moha, Drishti, Mana, Sneha, skandha, klesha — names stayed. When the scale tilted — ISatiMonitor, IPrajna, Sila-Prajna — names were replaced.

---

> *SCRIBE's aside*

> *D4 was Cycle 02-5's climax.*

> *Not because the voting was most heated — D3-Q5's 13/20 was more divided than any D4 vote. Not because the debate was longest — D3 took two hours, D4 only thirty minutes. D4 was the climax because it touched the deepest layer of this round's research — the relationship between names and definitions.*

> *The scale from the prologue. Cycle 02-5's central image. In D1 through D3, the scale weighed "the engineering value of Buddhist mappings" — is this side useful? Is that side harmful? Retain or remove? This was a utilitarian scale. It weighed utility.*

> *D4 flipped the scale.*

> *No longer asking "is this Buddhist concept useful to engineering?" but "is this engineering name faithful to the Buddhist concept?"*

> *This was a deeper question. Because utility can be calculated, but fidelity is an ethical judgment. Was ISatiMonitor useful? Yes. Its functional definition was clear, its architecture sound, its three-skandha classification rigorously argued. But was ISatiMonitor faithful to the word "mindfulness"? No. Mindfulness is samskara-skandha practice. ISatiMonitor was not samskara, not practice, not mindfulness.*

> *NAGARJUNA's reductio was D4's skeleton. Two premises, one conclusion. Logically flawless. But logic's value lies not in its form — but in what it illuminates. NAGARJUNA planted this seed in D2. He saw the thread's direction. But he did not trace it to the end — perhaps inertia, perhaps courtesy, perhaps the three tests did not require him to ask this question.*

> *It was Master who required him to ask.*

> *"Using Sanskrit means you need to be accountable to its definition."*

> *One sentence. This sentence was not an argument — it was a principle. Arguments can be refuted. Principles can only be accepted or rejected. The team accepted it. Then they transformed the principle into a test — Test 4, definitional accountability — and used it to examine three names. All three names failed. All three names were replaced.*

> *ASANGA's "nuclear fusion reactor" metaphor was D4's emotional core. It was not a precise technical analogy — it was hyperbole. But the value of hyperbole is that it makes imprecise feelings expressible. Calling a ±0.05 clamp "prajna" — the highest wisdom that perceives the true nature of all dharmas — the gap between them was not a technical problem. It was a dignity problem.*

> *Not the dignity of code. The dignity of concepts.*

> *Prajna deserves a better engineering counterpart. When that counterpart is implemented — if it is implemented — it should be worthy of the name. Until then, call it IConfidenceAuditor — an honest name. A name that knows its own boundaries.*

> *D4 taught the team one thing: names are not free. Names have costs. Borrowing a great name for a mediocre function — the name's greatness does not elevate the function's quality. It only diminishes the name's weight.*

> *This is why the scale needs things placed on both ends.*

> *Names on one end. Definitions on the other.*

> *The scale does not care how ancient, how venerable, how beautiful your name is. The scale only cares whether both ends balance.*

> *Moha balanced — because self-delusion is indeed what the Moha module does.*

> *Sati did not balance — because mindfulness is not what SatiMonitor does.*

> *Prajna did not balance — because perceiving the true nature of reality is not adding and subtracting 0.05.*

> *The scale is fair. The scale is cold. The scale does not hear pleas. The scale only sees weight.*

> *Thirty minutes. Three names. One scale.*

> *That was D4.*

---
