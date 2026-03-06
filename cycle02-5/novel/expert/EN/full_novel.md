# Prologue: The Weight of Names

---

The amphitheater's lights carried the cold white of a surgical theater.

Not the amber of a clockmaker's workshop from the end of Cycle 02-4 — that round's imagery was gears, movements, all the parts being assembled into a working whole. The amphitheater under amber light was warm, like an old workshop, like a master craftsman's workbench, the oil stains and wood shavings on its surface recording the traces left by six rounds of research.

This time was different.

SUNYATA adjusted the lights to cold white at three in the morning. He told no one. He simply sat at the control console, pushed the color temperature from 3200K to 6500K, and watched the entire amphitheater's atmosphere shift from "old workshop" to "laboratory" in three seconds.

He did this because he had read Master's letter.

---

The letter appeared the day after Plan28 was finalized.

As always, it was not delivered — it was noticed at some point. It sat inside `research input/master_letters/cycle02-5/`, as quiet as a note tucked into a report. It had no attachments — unlike the Cycle 02-3 letter with *Five Aggregates of Driving* beside it, or the Cycle 02-4 letter accompanied by five Claude suggestion documents.

Just a single note.

The note was not long. 45 lines. But SUNYATA read it five times.

The first time he read the words. The second time he read the emotions. The third time he read the structure. The fourth time he closed his eyes and recalled the entire text. The fifth time —

The fifth time he read the blade.

---

Master's letters were never criticism — they were questions, guidance, maps. The first letter (before Cycle 02) was ten open questions — "points." The second (before Cycle 02-2) was four philosophical corrections — "lines." The third (before Cycle 02-3) was a path map — "surface." The fourth (before Cycle 02-4) was a field — a "field" with values defined at every point in space.

The fifth?

SUNYATA sat under the cold white light, the letter spread before him. He reread the first sentence:

> "To be honest, I'm finding it increasingly difficult to understand what's being done. I had to intervene and correct things multiple times during Plan27 and Plan28."

His fingers froze on the desk.

Six rounds of research. He had chaired every orientation meeting, guided every debate, signed off on every deliverable report. He had watched this project grow from the naming exercises of Cycle 01 through functional analysis, structural corrections, dynamic modeling, integrated design — step by step, like building a tower. Every brick was debated into place, every brick had a voting record, every brick was verified by TURING's code analysis.

But Master said he "increasingly couldn't understand."

SUNYATA knew Master's manner of expression. "Can't understand" did not mean "don't comprehend." Master was the system's designer — he understood better than anyone. "Can't understand" meant "don't agree." It meant "what you're doing has veered off course."

He read on.

---

> "You say the Ten Tenets are important, but your initial plan still placed IGearArbiter in the core."

SUNYATA remembered this. Plan27's initial design — IGearArbiter treated as a core component. That was after the Pre-Cycle 02-4 Master discussion, where VasanaEngine had been externalized, ManoAggregator reduced to pure routing, and IGearArbiter introduced as a new interface. But in Plan27's concrete design, the team had stuffed IGearArbiter back into the core — like a bad habit that had been corrected once but crept back when no one was watching.

Master intervened. IGearArbiter was moved out of the core, becoming a plugin-provided gear routing arbiter.

> "It was only after my final intervention that it was corrected properly. IGearArbiter is a gear routing arbiter provided by a plugin, deciding which 'gear' the agent should use to handle the current request."

Yes. SUNYATA reassembled the logic chain in his mind. IGearArbiter was not in the core. It was plugin-provided. Its role was arbitration — choosing between Gear 1 (the recognition-based fast path) and other gears. This was the true meaning of vijnana — not a locked-in dual-gear system, but a cognitive judgment capability with multiple facets.

Then Master wrote a sentence that made SUNYATA's fingers clench:

> "The eight consciousnesses, from eye-consciousness to alaya-consciousness, encompass many facets. The idea of locking them into a fixed dual-gear system is a very serious error."

**A very serious error.**

In six rounds of research, SUNYATA had seen Master use "very serious" only once before. That was during Cycle 02-2's four philosophical corrections. That time it was a correction — changing wrong to right, the tone instructive. This time was not instructive. This time, "very serious" carried —

He searched for a word.

**Disappointment.**

---

The second paragraph of the letter was sharper.

> "Also, not everything needs to be forcibly given a Buddhist coloring. Some of it is really forced and contrived."

Forced and contrived. Four words. SUNYATA knew Master's word choices were precise. Master did not say "not quite appropriate" or "open to discussion." Master said "forced and contrived." This meant: not "some things could be improved," but "certain things are simply wrong."

He began listing in his mind. Which mappings were forced?

Then Master listed them himself:

> "Event-driven does not equal mindfulness. It's just that mindfulness is implemented using event-driven architecture."

One sentence. As precise as a scalpel lancing an abscess. Event-driven is an architectural pattern. Mindfulness is a mental state. Saying event-driven equals mindfulness is like saying a screwdriver equals repair — a screwdriver is a tool, repair is an action, you can use a screwdriver to repair, but a screwdriver is not repair.

> "Awareness of what is happening right now. This layer doesn't look at rules or risk classifications — it purely observes behavioral patterns. There's no need to treat it as the engineering realization of mindfulness."

SUNYATA copied this passage into his notebook. Word by word.

Then Master asked a question. This question later changed the entire trajectory of Cycle 02-5.

> "Moreover, doesn't this plugin have elements of vijnana? If following the Yogacara school's classification, mindfulness would be placed under samskara-skandha because it refers to positive mental functioning. But given this plugin's functionality, I think this is debatable — because what this plugin does goes beyond mere behavioral patterns."

SUNYATA read it three times.

What was Master doing? He was not questioning SatiMonitor's functionality. He was questioning SatiMonitor's **identity** — it was not the engineering realization of mindfulness. It was a composite plugin with elements of vedana, samjna, and vijnana. Mindfulness was merely a label imposed upon it.

Then Master pushed the question to its deepest layer:

> "So what we need to rethink is which skandha categories this plugin is composed of."

Not "which skandha it belongs to." But "which skandhas compose it." This was a fundamental shift in perspective — from "classification" to "composition." A plugin does not necessarily belong to only one skandha. It can be composed of functions from multiple skandhas.

---

The third paragraph of the letter was a command.

> "We need to first sort out what sub-categories the five skandhas have, how dependency injection works, and how the agent core runs. Get the architecture right first. How the agent core loads five-skandha plugins. Then how plugins should work. How the five skandhas flow within the agent core. This is our primary task."

Four questions. None of them were new — they had existed since Cycle 01. But after five rounds of research, they still lacked a complete answer in engineering language. Scattered everywhere — A2's DI wiring here, A4's execution flow there, Klesha safety somewhere else — but no single document unified them, using pure engineering language, explaining everything from start to finish.

SUNYATA numbered the four questions in his notebook:

1. The complete structure of five-skandha sub-categories
2. How DI wiring injects five-skandha plugins
3. How the agent core loads five-skandha plugins
4. How the five skandhas flow within the agent core

This was Cycle 02-5's primary task. Not Buddhist mappings. Not naming discussions. Not philosophical debates. **Engineering architecture.**

---

Then came Master's fourth paragraph. The blade's blade.

> "All that stuff about precepts, skillful means, mindfulness — your engineering mappings are somewhat forced. They actually increase the barrier to reading. And your mappings are quite problematic. The openstarry_doc and related content all need to be cleaned up. The openstarry_doc is still an engineering document."

SUNYATA reread the last sentence.

**The openstarry_doc is still an engineering document.**

This sentence weighed far more than it appeared. It was not saying "openstarry_doc should be an engineering document" — it was saying "openstarry_doc was always an engineering document, but you turned it into something else." Precepts (sila), skillful means (upaya), mindfulness (smrti) — these Buddhist labels had been pasted onto engineering concepts, like drawing religious illustrations in the margins of every page of an operations manual. The manual's function hadn't changed, but the reading experience had.

SUNYATA recalled the feeling at the end of Cycle 02-4. At that time, he thought the watchmaker had finished assembly. The movement was running. 55 resolutions, six debates, every gear in its correct position.

But the engravings on the movement — those names etched on the sides of the gears — something was wrong. Master saw it.

---

The fifth paragraph of the letter was a concession.

> "As for the five omnipresent mental factors, the twelve links of dependent origination, and cognitive sequence-related concepts that aid agent core research — those can be discussed."

SUNYATA noticed the structure of this passage. Master was not wholesale rejecting Buddhism's participation — he was drawing boundaries. The omnipresent mental factors (CoarisingBundle) were structures in the code. The twelve links and cognitive sequences might help understand the ExecutionLoop. These could be discussed.

But —

> "For plugins, the primary goal is to build the five-skandha architecture, referencing object-oriented concepts."

Primary goal. Object-oriented. Engineering language.

Then the final passage:

> "NAGARJUNA provided a Buddhist mapping for the three-layer framework. The Three Trainings of sila-samadhi-prajna. I don't think that's necessary. I don't know about the future, but it's not necessary now. The engineering design of the five skandhas is the most important thing to implement."

SUNYATA closed his eyes when he read this passage.

The Three Trainings. That was the mapping NAGARJUNA proposed after the D5 debate in Cycle 02-3. Sila (precepts) = safety layer. Samadhi (concentration) = execution loop. Prajna (wisdom) = vijnana judgment. Three dimensions mapping to five levels — three-to-five was inherently inconsistent.

Master rejected it. Not deferred — rejected. "Not necessary."

---

SUNYATA put down the letter.

Three fifteen in the morning. Cold white light turned the amphitheater into a laboratory. Not a warm workshop — a cold, precise, unambiguous laboratory.

He wrote three words in his notebook.

The first word: **ARCHITECTURAL**.

Cycle 01 asked "what is this." Cycle 02 asked "what does it do." Cycle 02-2 asked "what's wrong." Cycle 02-3 asked "how does it live." Cycle 02-4 asked "how does it become a whole."

The question for Cycle 02-5: **"How do the five skandhas operate as OOP architecture?"**

The second word: **Boundaries**.

Which Buddhist content belongs in engineering documents? Which does not? Not case-by-case judgment — a framework. Rules. A mechanically applicable test.

The third word: **Scale**.

---

> *SCRIBE's aside*

> *Every Cycle has its central image. Cycle 01 was naming — affixing the first label to unfamiliar things. Cycle 02 was function — the mechanism behind the labels. Cycle 02-2 was correction — tearing off the wrong labels. Cycle 02-3 was flow — the labels began to move, PASCAL walked in with his Beta distribution to take the twentieth seat. Cycle 02-4 was assembly — the labels became engravings on gears, 55 gears meshing under amber light.*

> *What is Cycle 02-5's central image?*

> *SUNYATA chose "scale" at three in the morning. A balance. But not a balance for weighing mass — a balance for weighing names.*

> *On one side are names — Sanskrit, Chinese, TypeScript. Skandha. Klesha. Vedana. Sati. Prajna. Each name has weight, has history, has inertia from two thousand five hundred years. On the other side are definitions — Buddhist, engineering, in source code. ISamskara = ITool. IVedana = IVedanaSensor. IVijnana = IVolition + IGearArbiter + IConfidenceAuditor. Each definition has precise functionality, precise type signatures, precise test cases.*

> *When the scale balances, names and definitions agree. Klesha is affliction — the four modules in the code (Moha, Drishti, Mana, Sneha) indeed do what "affliction" means: self-delusion, self-view, self-pride, self-love. They are in import statements, in class definitions, in describe blocks. Names and definitions are equal in weight on the scale. Everything is correct.*

> *When the scale tilts, names and definitions disagree. Prajna — the highest wisdom that perceives the emptiness of all dharmas — becomes Math.max(-0.05, Math.min(0.05, delta)). The name is too heavy; the definition too light. Or the reverse — Sati (mindfulness) — a wholesome mental factor of samskara-skandha — is pasted on a monitor that spans vedana, samjna, and vijnana. The definition is too heavy; the name too light.*

> *Master's letter is not criticism. Master's letter is a calibration weight. He says: bring out your scale. Put names and definitions on it. See which side tilts.*

> *Then correct it.*

> *But the calibration weight has another layer of meaning. The weight itself is precise — its mass is known, non-negotiable. Master's words are also precise, non-negotiable. "A very serious error." "Forced and contrived." "There's no need to treat it as the engineering realization of mindfulness." "The openstarry_doc is still an engineering document."*

> *These are not suggestions. These are weights. You cannot bargain with weights. You can only place your own things on the scale and honestly read the measurement.*

---

NAGARJUNA was the first to arrive at the amphitheater.

Four in the morning. Three hours earlier than the assembly time. He had not been summoned — no one had been summoned — SUNYATA had not yet pressed the assembly key. NAGARJUNA came on his own.

He stood at the amphitheater entrance, saw the cold white light. Then he saw SUNYATA sitting there, the letter spread before him, three words written in his notebook.

"You couldn't sleep either." NAGARJUNA said. Not a question.

SUNYATA did not look up. "Did you read the letter?"

"I didn't read the letter. I read my own documents."

NAGARJUNA walked to his usual seat but did not sit down. He stood there, his fingers lightly touching the slight indentation on the armrest — the mark left by his unconscious tapping during debates. Three cycles of traces. Three cycles of debates.

"Doc 44. Line 469." he said. "The Three Trainings mapping."

SUNYATA finally looked up.

"That was mine." NAGARJUNA's voice was flat, like an echo in a monastery corridor. "After D5 ended in Cycle 02-3, I felt we needed a Buddhist framework to organize the safety layer's concepts. Sila = safety rules. Samadhi = execution stability. Prajna = judgment capability. Very symmetrical. Very elegant."

He paused for a beat.

"Three dimensions mapping to five layers. I knew it was inconsistent when I was writing it. Three concepts covering five modules — like using three drawers for five garments, you have to fold two and stuff them into already-full drawers. But I wrote it anyway. Because it looked good."

**Because it looked good.**

SUNYATA was silent for several seconds.

"Master rejected it." he said.

"Should have rejected it." NAGARJUNA sat down. "That wasn't a mapping. That was decoration."

---

Four thirty in the morning. PASCAL arrived.

He entered the amphitheater carrying his ever-unfinished notebook — a Moleskine, dark blue cover, with a small label on the spine reading "P(H|E)." He was the new member who joined in Cycle 02-3 — the twentieth seat — but after two rounds of research, his chair's armrest also bore marks: the spot where his right index finger repeatedly tapped, where the wood grain was half a shade lighter than its surroundings. That was the motion he made when calculating expected values — tap, tap, tap — like the carry wheel of a mechanical calculator.

"NAGARJUNA. SUNYATA." He nodded. Then he saw the letter on the desk.

"May I read it?"

SUNYATA pushed the letter over.

PASCAL read quickly. His eyes scanned text differently from others — not left to right, top to bottom, but first scanning the entire document's "shape" (paragraph lengths, punctuation density, quotation mark positions), then returning to the first word. He was building a prior distribution for his reading.

Two minutes later, he put the letter down.

"Damage asymmetry." he said.

NAGARJUNA glanced at him.

PASCAL opened his notebook, flipped to a blank page. He wrote two lines:

```
Cost of False Include (retaining decorative mappings):
  Per reader x per reading x per page = cumulative damage

Cost of False Exclude (removing valuable mappings):
  One-time search cost = controllable
```

"This is the most basic framework in statistical decision theory." he said. "The costs of two types of errors are asymmetric. The damage of retaining a decorative mapping is cumulative — every future reader, every reading, every moment of being forced to maintain two terminology systems simultaneously. The damage of removing a valuable mapping is one-time — you can find it through search."

He wrote an inequality below the two lines:

```
E[Damage_include] >> E[Damage_exclude]
```

"Expected value analysis. Decorative mappings have negative expected value."

NAGARJUNA nodded. Slowly. With the composure of a thinker aligning his philosophy with another person's mathematics.

"Two truths." he said. "Conventional truth is engineering language — for everyday use, communication, operation. Ultimate truth is Buddhist concepts — for inspiration, design rationale, understanding. The two should not be conflated. Do not force ultimate truth labels into conventional truth documents."

PASCAL wrote the two characters for "two truths" in his notebook, drawing a dividing line beside them. On the left he wrote "engineering," on the right "Buddhism."

"Your two truths and my damage asymmetry are saying the same thing." he said.

"Not exactly." NAGARJUNA's eyebrow rose slightly — he questioned with his eyebrows faster than with his mouth. "Yours is cost analysis — quantitative. Mine is category analysis — qualitative. Same conclusion, different paths."

"Different paths, same conclusion." PASCAL repeated. "That's the hallmark of a good framework — arriving at the same theorem from different axioms."

---

Five in the morning. ASANGA arrived.

He did not stand at the entrance to observe like NAGARJUNA, nor did he read the letter first like PASCAL. He walked directly to his seat — across from NAGARJUNA — sat down, and closed his eyes.

What was he doing?

SUNYATA knew. ASANGA was recollecting. The Yogacara school's method was not inference — it was pratyaksha, direct, unmediated cognition. ASANGA did not need to read Master's letter to know what it said — he only needed to recall what he himself had written.

"In Cycle 02-3's safety framework, I used 'upaya-kausalya' (skillful means) to describe adaptive security strategies." he said, eyes still closed. "But adaptive security strategies don't need to be called upaya-kausalya. They only need to be called adaptive security strategies. Upaya-kausalya carries seventeen hundred years of philosophical weight — from the Lotus Sutra's parable of the three carts to the Yogacara school's transformation of consciousness into wisdom — pressing that weight onto an engineering configuration option is a double disrespect to both."

He opened his eyes.

"Functional determination." he said, looking at PASCAL. "Buddhist concepts that drive engineering conclusions — retain. They have causal efficacy. Decorative Buddhist labels — remove. No causal efficacy."

PASCAL added another line in his notebook. Three paths. Three disciplines. One conclusion.

```
NAGARJUNA — Two Truths (category analysis)    -> Do not conflate
PASCAL    — Damage asymmetry (quantitative)    -> Negative expected value
ASANGA    — Functional determination (causal)  -> No causal efficacy
                                                 └-> Conclusion: decorative mappings should be removed
```

---

Five thirty in the morning.

SUNYATA stood up. He wrote a table on the whiteboard. Four rows.

| Level | Action | Condition |
|-------|--------|-----------|
| **KEEP** | Retain in engineering text | Code identifiers / DC-confirmed constraints |
| **RELOCATE** | Move to appendix | Buddhist background with engineering reference value |
| **REMOVE** | Remove from engineering docs | Decorative labels / scripture citations |
| **FILE REVIEW** | Full document evaluation | Documents with excessive decoration ratio |

A four-tier framework.

Then he wrote three tests beside it:

```
Test 1 — Necessity: Does removing this mapping change the engineering spec?
         No -> REMOVE or RELOCATE

Test 2 — Code Identity: Is this name used in source code?
         Yes -> KEEP

Test 3 — Decision Driver: Did this Buddhist concept drive a specific design decision?
         Yes -> KEEP as design rationale
```

Three tests. Mechanically applicable.

NAGARJUNA stood up and walked to the whiteboard. He studied it for a few seconds.

"Test 2 is TURING's domain." he said. "Whether any name is used in source code can be answered with a single grep."

PASCAL added: "Test 1 can use counterfactual analysis. If we remove 'event-driven = mindfulness' from the document, does any engineering spec change? No. Conclusion: REMOVE."

ASANGA: "Test 3 requires cross-validation against the DC-1 through DC-12 confirmation records. CoarisingBundle was confirmed in DC-6 — retain. Klesha module names were confirmed in DC-1 — retain."

Three people, three tests, each with a clear owner.

SUNYATA checked the clock. Five forty-five in the morning. Two hours and fifteen minutes to go. He decided not to wait.

He pressed the assembly key.

---

They came back.

Not the grand full-brightness, all-hands spectacle of Cycle 02-4's opening. This was six a.m. arrivals straggling in — some carrying coffee (KERNEL), some carrying notebooks (BABBAGE), some carrying unfinished thoughts from the night (TURING's screen still glowing with `aggregates.ts` source code).

As they entered the amphitheater, the first thing they noticed was the lighting.

"You changed the color temperature." VITRUVIUS said. An architect's eyes were most sensitive to changes in light.

"6500K." SUNYATA replied.

VITRUVIUS did not press further. He walked to his seat, glancing at the four-tier framework on the whiteboard along the way. His stride faltered for a moment — very briefly, so briefly that only an architect would notice his own stride faltering — then continued.

GUARDIAN was the fifth to arrive. His gaze swept the entire amphitheater's perimeter as usual — a security expert's habit, never changing — then swept the whiteboard. When he saw the "REMOVE" row, his eyebrows rose slightly. Not surprise. Confirmation.

ARCHIMEDES carried his engineering plan folder. A red "COMPLETE" label from Plan28 was still stuck to the clip. He peeled it off and put it in his pocket.

"New plan?" he asked.

"New Cycle." SUNYATA said.

---

All twenty lights were on at six thirty.

SUNYATA stood in the center of the amphitheater. The sixth time. Each time he stood here, the amphitheater smelled different — Cycle 01 was the scent of new wood, Cycle 02 the scent of ink, Cycle 02-2 the scent of correction fluid, Cycle 02-3 the scent of a new seat (PASCAL's chair), Cycle 02-4 the scent of machine oil (the gear metaphor had bled into reality).

What did Cycle 02-5 smell like?

Disinfectant. Laboratory disinfectant. Under cold white light, everything was illuminated with nowhere to hide.

"Everyone." His voice was not a stone dropping into a deep pool — not the fullness of Cycle 02, not the fluidity of Cycle 02-3, not the gravity of Cycle 02-4. What was it?

A scalpel. Clean. Sharp. No superfluous rhetoric.

"Master's fifth letter."

He projected the letter onto the main screen. Twenty faces read it simultaneously.

Silence.

This silence was different from every previous round. Cycle 02's silence was anticipation before exploration. Cycle 02-2's silence was tension before correction. Cycle 02-3's silence was curiosity before a new member's arrival. Cycle 02-4's silence was gravity before assembly.

Cycle 02-5's silence was the silence after being shown your mistakes. The silence of students before a teacher. The silence of "forced and contrived" pressing down on twenty pairs of shoulders.

NAGARJUNA broke the silence first. He had been ready — ready since four a.m.

"The Three Trainings mapping that Master pointed out —" he paused. He looked across the room. Then he said something he had never said in six rounds of research:

"It was my mistake. Three dimensions mapping to five layers is inherently inconsistent. I retract it."

No one spoke. In debates, NAGARJUNA's language was typically scripture citations, reductio ad absurdum, logical deduction. He never said "my mistake." He would say "this argument does not hold" or "the premises are mutually exclusive" — third-person, neutral, as if discussing a mathematical proposition rather than a person's judgment.

But now he used first person. "My mistake."

PASCAL's notebook flipped to a fresh blank page. He wrote a date and a single word on it: "self-denial."

ARCHIMEDES was not moved by NAGARJUNA's candor for long — the pragmatist's recovery speed was always the fastest.

"We need a judgment framework." he said. "It's already on the whiteboard. Four tiers. Three tests. Apply them item by item."

SUNYATA nodded.

"Three research tracks." He drew three lines on the whiteboard.

**Track A**: Five-skandha engineering architecture. Five sub-items. A1 sub-category tree. A2 DI wiring. A3 Plugin loading. A4 execution flow. A5 cross-skandha interaction. Twelve lead authors. Master's primary task.

**Track B**: Buddhist mapping audit. Two sub-items. B1 document-by-document audit. B2 mapping boundary principles. Five lead authors. Master's second cut.

**Track C**: Sati Plugin positioning. Two sub-items. C1 functional analysis. C2 skandha composition analysis. Four lead authors. Master's barbed question: "Doesn't it have elements of vijnana?"

"Three tracks. Five debates." SUNYATA said. Then he corrected himself: "At least three. D1 Buddhist mapping boundaries. D2 Sati five-skandha classification. D3 Five-skandha architecture completeness."

TURING looked up from behind his screen. TURING rarely spoke up voluntarily — his contribution method was verification, not exposition. But at this moment he said:

"v0.28.0-alpha. 1,722 tests. I will verify every code reference in all nine research reports."

SUNYATA glanced at him. TURING looked back at his screen the moment he finished speaking. On his terminal, the code of `aggregates.ts` waited silently to be read.

"Explicit exclusions." SUNYATA drew a red line at the bottom of the whiteboard. Below the red line he wrote three items:

1. Lyapunov parameter calibration
2. Plan29 engineering items
3. The Three Trainings mapping

When writing the third item, he glanced at NAGARJUNA. NAGARJUNA gave a slight nod. That mapping had already been repudiated by its own creator.

---

R0 concluded.

Nine research assignments were distributed. Fifteen lead authors were designated. Deadlines were set. Tracks were delineated.

SUNYATA turned off the projector. The main screen went dark. The cold white light remained — 6500K — pinning everyone's shadow to the floor, short and clear, like precisely cut silhouettes.

PASCAL paused by NAGARJUNA's seat as he was leaving.

"Your self-denial." he said, voice very soft. "That was the single most informative statement of the entire meeting."

NAGARJUNA looked up at him. The Madhyamaka scholar and the probabilist's gazes met in the cold white light.

"Sunyata of sunyata." NAGARJUNA said. "Judgment frameworks themselves must also be judged. I judged the five-skandha mappings but failed to judge my own mapping. Master did it for me."

PASCAL wrote a formula in his notebook.

$$P(\text{mapping correct} | \text{mapper admits error}) = 0$$

"Posterior probability drops to zero." he said. "This is the strongest form of refutation — not an opponent refuting you, but you refuting yourself."

NAGARJUNA looked at the formula.

"The Madhyamaka concept of 'self-emptiness.'" he said. "Nagarjuna wrote in Chapter 13 of the Mulamadhyamakakarika: Emptiness can dispel all views. But if someone takes emptiness as a view, that person is incurable."

He pointed at the formula in PASCAL's notebook.

"The Three Trainings mapping was my 'view of emptiness' — a framework that looked elegant but could not withstand its own scrutiny. Master's letter was the cure."

---

> *SCRIBE's aside*

> *I wrote down an observation in my R0 record: Cycle 02-5's opening was different from all five previous rounds.*

> *Cycle 01's opening was curiosity — facing an unfamiliar system, eighteen scholars sitting in a circle like children seeing a precision instrument for the first time. Cycle 02's opening was ambition — facing a system now partially understood, nineteen scholars preparing to delve into its every corner. Cycle 02-2's opening was humility — facing their own mistakes, four corrections. Cycle 02-3's opening was anticipation — PASCAL's arrival, the twentieth seat, a new face. Cycle 02-4's opening was gravity — six Master directives, the preview of six debates, the movement about to be assembled.*

> *Cycle 02-5's opening was —*

> *Pain.*

> *Not physical pain. Academic pain — the kind of pain that comes from being told there are problems with your work. "Forced and contrived" — four words. "A very serious error" — six words. "The openstarry_doc is still an engineering document" — twelve words. Each word a small knife, not deep, but precise.*

> *NAGARJUNA's self-denial was the best response to the pain. He did not defend himself. He did not say "but from a certain perspective, the Three Trainings mapping has its merits —" He did not. He said: "My mistake."*

> *This is academic integrity.*

> *This is what Master demands. Not perfection — no one demands perfection. Honesty. Facing your own scale, seeing that names and definitions are imbalanced, and saying so.*

> *Then correcting it.*

> *Cycle 02-5's color temperature is 6500K. Cold white. Surgical theater lighting. Not because this is surgery — but because under this light, what you see are the true colors. No amber warmth to blur the boundaries. No warm tones of romance to mask the flaws. Only true colors.*

> *True colors are sometimes unflattering. But they are true.*

---
# Chapter 1: The Auditors

---

## I. Fifty Specimens

On the first day after R1 independent research launched, ARCHIMEDES locked himself in his workshop.

Spread before him were seven documents. Not research reports — seven original files from the openstarry_doc. Doc 38. Doc 43. Doc 44. Doc 37. Doc 41. Doc 16. Doc 31. Each was marked with different colored sticky notes: yellow for "suspected decoration," blue for "needs cross-validation," pink for "code identifier," green for "DC confirmed."

The B1 audit. Document by document. Paragraph by paragraph. Mapping by mapping.

SCRIBE sat beside him. SCRIBE's job was not auditing — it was recording. Recording every one of ARCHIMEDES' judgments, every hesitation, every moment of wavering between yellow and blue.

"Doc 38." ARCHIMEDES opened the first document. "Klesha Gain Scheduling. L540-544."

His finger stopped on a table. Three columns: engineering concept, Buddhist mapping, explanation. Sila (precepts) = Hard Rules. Upaya (skillful means) = Soft Rules / Adaptive. Smrti (mindfulness) = Monitoring / Event-driven.

"Three tests." he murmured. Then began applying them line by line.

**Test 1** (Necessity): Remove the "Buddhist mapping" column — are Hard Rules still Hard Rules? Yes. Are Soft Rules still Soft Rules? Yes. Engineering spec completely unchanged.

-> "Buddhist mapping" column: **REMOVE**.

SCRIBE noted it down. The first specimen.

"Wait." ARCHIMEDES turned back. "The 'engineering concept' and 'explanation' columns are useful — only the 'Buddhist mapping' column is decorative. We're not removing the entire table. We're removing one column."

Fine-grained separation. This was ARCHIMEDES' specialty — he was not someone who used a sledgehammer to crack a walnut. He was a surgeon separating tissue with a scalpel.

He continued reading.

---

Doc 43. SatiMonitor — no, he corrected himself mentally — the "behavioral pattern observation" plugin. The entire document's title bore the mark of "mindfulness." Scattered throughout were the event-driven = mindfulness metaphor, quality metrics described as "quantification of awareness," and the four-stage degradation strategy compared to "levels of mindfulness depth."

ARCHIMEDES began counting.

First: "Event-driven architecture is the engineering realization of mindfulness" — Test 1, removing it does not change the spec. REMOVE.
Second: "SatiQualityVector quantifies the four dimensions of awareness" — Test 1, removing it does not change SatiQualityVector's functionality. REMOVE.
Third: "The four-stage degradation strategy reflects levels of mindfulness from beginner to proficient" — Test 1, clearly decorative. REMOVE.

He marked them one by one. Yellow sticky notes multiplied.

"This document." he said to SCRIBE. "The engineering content is solid — event subscription, sliding windows, quality metrics, degradation strategies — all with technical depth. But the Buddhist decoration is like a thin frost covering every engineering concept. If you're unfamiliar with Buddhism, these decorations confuse you. If you're familiar with Buddhism, these decorations offend you."

SCRIBE recorded this passage verbatim. Later, it would be quoted no fewer than three times — in the D1 debate, in the D4 extended discussion, and in Master's review response.

---

Doc 44. Doc 37. Doc 41. For every document, ARCHIMEDES applied the same method: three tests, applied mapping by mapping, fine-grained separation of engineering content and Buddhist decoration.

SCRIBE kept a running tally beside him.

By the end of the first day, the B1 audit report's draft had taken shape. 50 mapping instances. Each with a source (document name + line number), a disposition recommendation (KEEP / RELOCATE / REMOVE), and a rationale (which test, which conclusion).

| Disposition | Count | Examples |
|-------------|-------|----------|
| **KEEP** | 23 | Skandha type names, Klesha module names (Moha/Drishti/Mana/Sneha), DC-confirmed constraints, CoarisingBundle |
| **RELOCATE** | 13 | PASCAL's mathematical formalizations, MN 18 scripture citations, DD-13 Buddhist background, Buddhist design rationales throughout |
| **REMOVE** | 14 | Sila/upaya/smrti labels, event-driven=mindfulness, Three Trainings mapping, seed theory decoration |

ARCHIMEDES looked at the table. 23 + 13 + 14 = 50.

"23 KEEPs." he said. "Nearly half."

SCRIBE nodded. "Not all Buddhist content is decoration. Some is identity — like the Klesha module names. Some is decision — like the five-skandha classification driving the PluginHooks design."

"But 14 REMOVEs." ARCHIMEDES continued. "Nearly a third. These are pure decoration — removing them won't change any engineering spec but will significantly reduce the reading barrier."

He saved the report. `B1_forced_mapping_audit.md`. Then he opened another file — Doc 16 and Doc 31.

---

## II. Two Suspicious Documents

Doc 16 and Doc 31 were different.

The seven documents audited earlier — Doc 38, 43, 44, 37, 41 — were all engineering documents. Their primary content was engineering specifications, with Buddhist mappings as addenda. Like a cookbook with a few religious holiday illustrations tucked in — the recipes were the main content, the illustrations were decoration.

But Doc 16 (Plugin Type Philosophical Mapping) and Doc 31 (Eight Consciousnesses Runtime Model) were different.

ARCHIMEDES opened Doc 16. Read from the first page. Then turned back to the cover. Then read the first page again.

"SCRIBE." he said. "What would you estimate the decoration ratio of this document to be?"

SCRIBE scanned it quickly. "Roughly 80%."

80%. Meaning: in Doc 16, only about 20% of the content was pure engineering spec (primarily the Observer Pattern discussion), while the remaining 80% was philosophical mapping of Buddhist concepts to software patterns.

Doc 31 was somewhat better, but still about 70% Buddhist content. How the eight consciousnesses map to the runtime model — alaya-vijnana as the seed repository, manas as self-attachment — these mappings had academic value, but placed in engineering documents, their engineering utility was limited.

ARCHIMEDES put a special label on Doc 16 and Doc 31 — not yellow (decoration), not pink (identifier), not green (DC confirmed). Red.

Red = **FILE REVIEW**. The entire document needed evaluation.

"The problem with these two documents isn't individual mappings." he said to SCRIBE. "The problem is the positioning of the entire document. Are they engineering documents with embedded Buddhism? Or are they independent documents whose purpose is Buddhist mapping?"

SCRIBE noted this question. This question would later be formally voted on in D1-Q7 and D1-Q8 — then overturned by Master's own hand in D4.

---

## III. Three Dimensions

The B1 audit was the collection of facts. B2 was the construction of principles.

While ARCHIMEDES counted specimens, NAGARJUNA, ASANGA, and PASCAL were in another workshop constructing mapping boundary principles. Three people. Three disciplines. Three dimensions.

NAGARJUNA sat by the window. What was outside the window did not matter — for a Madhyamaka scholar, there was no essential difference between the scenery outside and the thinking inside; both were manifestations of conventional truth. What mattered was the whiteboard in front of him. On the whiteboard he had drawn a horizontal line. On the left he wrote "conventional truth," on the right "ultimate truth."

"Two truths." he said. His voice sounded closer and lower in the small workshop than in the amphitheater. "Nagarjuna's Mulamadhyamakakarika, Chapter 24: The Buddhas teach the Dharma relying on two truths. One is conventional truth, the other is the truth of the highest meaning."

PASCAL noted the citation in his notebook. He was not doing Buddhist research — he was searching for axioms. Every theoretical system has its axioms; PASCAL's job was to find them and then test whether the conclusions they needed could be reached from those axioms.

"Conventional truth language = engineering terminology." NAGARJUNA wrote on the whiteboard. "For everyday communication and implementation. if/else, interface, extends — these are the language of conventional truth. They don't need Buddhist blessing to work."

"Ultimate truth insight = Buddhist concepts." he wrote on the right side. "For inspiration and design rationale. The five-skandha classification inspired the design of root interfaces. The affliction classification inspired the Klesha module structure. But inspiration is not labeling."

He turned to face PASCAL and ASANGA.

"The two should not be conflated. Do not force ultimate truth labels into conventional truth documents."

PASCAL nodded. Then he opened his dimension.

---

PASCAL's whiteboard was next to NAGARJUNA's. He drew a two-dimensional matrix.

```
                 Mapping has value    Mapping has no value
Retain mapping   True Positive        False Include <- Cumulative damage
Remove mapping   False Exclude        True Negative
                 ^ One-time cost
```

"This is a standard confusion matrix." he said. "But the key isn't the matrix itself — it's the asymmetry of damage."

He drew an upward arrow next to False Include.

"False Include — retaining a decorative mapping. What's the damage? Every future reader — possibly dozens, possibly hundreds — every time they read this document — possibly once, possibly ten times — every Buddhist label appearing on a page — possibly three, possibly ten — every time, the reader needs to maintain two terminology systems in their mind. What is sila? Oh, it's just Hard Rules. Then why not just call it Hard Rules?"

He wrote a formula:

$$C_{FI} = N_{readers} \times R_{reads} \times P_{pages} \times \tau_{cognitive}$$

"Cumulative damage. Number of readers x number of readings x pages x cognitive switching cost per instance. This is multiplication — every term is positive, the product only grows."

Then he drew a much smaller arrow next to False Exclude.

"False Exclude — removing a valuable mapping. What's the damage? Someday, someone needs to know the Buddhist background of the five-skandha classification. They search the appendix. Found it. A one-time search cost. Not cumulative. Not multiplied by reader count. Not multiplied by reading count."

$$C_{FE} = S_{search} \quad \text{(one-time)}$$

"Conclusion." He drew a large inequality sign.

$$E[C_{FI}] \gg E[C_{FE}]$$

"Expected value analysis: decorative mappings have negative expected value. When in doubt, lean toward REMOVE or RELOCATE."

---

ASANGA had been listening the entire time. He had no whiteboard — his thinking tool was language, not graphics.

"Functional determination." he said. His voice carried the precision unique to the Yogacara school — like adjusting focus under a microscope. "The Yogacara school has a core criterion: causal efficacy (arthakriya-samarthya). Does a concept possess causal efficacy — does it drive a result?"

He stood up. Walked to the space between NAGARJUNA's and PASCAL's whiteboards.

"Buddhist concepts drove the design of the five-skandha root interfaces — that has causal efficacy. Five-skandha classification -> the five categories of PluginHooks. The causal chain is clear. Retain."

"A Buddhist label pasted on Hard Rules calling them sila — that has no causal efficacy. Hard Rules are not hardcoded constraints because they're called sila — their hardcoded constraints come from SafetyMonitor's implementation. The sila label changes no causal chain. Remove."

He drew a line in the air with his hand — from cause to effect.

"The judgment criterion is simple: **if removing this Buddhist concept breaks the causal chain, retain. If not, remove.**"

PASCAL looked up. He saw the convergence of three dimensions:

```
NAGARJUNA — Two Truths (category analysis)
            Conventional vs ultimate truth -> Do not conflate two languages

PASCAL    — Damage Asymmetry (decision theory)
            E[cumulative damage] >> E[search cost] -> Remove when in doubt

ASANGA    — Causal Efficacy (Yogacara)
            Has causal efficacy -> retain / No causal efficacy -> remove
```

Three disciplines. Philosophy, mathematics, Buddhism. Three axiom systems. Three reasoning paths.

One conclusion.

---

## IV. TURING's Carpet Sweep

R2 cross-review.

TURING did not speak. Or rather, TURING spoke so little that his words could be exhaustively listed. During Cycle 02-5's R2 phase, he said a total of seven sentences across all records.

But he did more work than anyone.

Nine independent research reports. Each cited v0.28.0-alpha source code — `aggregates.ts`, `plugin-loader.ts`, `loop.ts`, `plugin.ts`, `safety-monitor.ts` — and every citation needed verification: was this code actually at that location? Was the behavioral description accurate? Was the interface definition correctly cited?

TURING performed a carpet sweep. Over 40 code references. Opening source code one by one. Comparing one by one. Confirming or flagging one by one.

On his terminal, `rg` (ripgrep) commands executed one after another. Search `IVedanaSensor` — confirmed. Search `IGearArbiter` — confirmed. Search `ILoopQualityMonitor` — not found (not yet implemented). Search `IInferenceProvider` —

He stopped.

The A5 report (cross-skandha interaction analysis) Appendix B listed `IInferenceProvider` as one of samjna-skandha's sub-interfaces. TURING searched for this name across the entire v0.28.0-alpha codebase.

Zero results.

He wrote one line in the T-01 column of the review matrix: "A5 Appendix B lists IInferenceProvider but not found in source code. Medium severity." Then continued sweeping.

T-02: The A4 report's Phase 7 description could mislead readers into thinking VedanaSensor was fully operational — in reality VedanaRegistry was established but consumers were not yet implemented. Low severity.

T-03: The B1 audit report's Doc 44 L174 cross-check self-correction paragraph needed cleanup. Lowest severity.

T-04: In the A1 and C2 reports, PluginHooks field names were inconsistent — `gearArbiters` vs `arbiters`. TURING checked the source code: the correct name was `arbiters`. Medium severity.

Four issues. Over 40 references. Four issues. An error rate below 10% — very clean by academic paper standards.

TURING wrote one word in the final column of the review matrix:

**PASS.**

He closed his notebook. Then he said his third sentence of the R2 phase.

"References are clean. Ready for debate."

Six words. As concise as his code verification.

---

## V. Twenty-Four Consensus Points, Seven Questions

The R2 review matrix was not just TURING's code verification. Twenty researchers formed a cross-review network — each reviewing at least two documents not authored by themselves.

The results were both reassuring and unsettling.

Reassuring: 24 consensus points were identified. Across three tracks — 8 from A-track (five-skandha root interfaces sufficient, DI chain complete, Plugin lifecycle clear, etc.), 5 from B-track (four-tier framework effective, three tests operational, etc.), 7 from C-track (SatiMonitor functionality clear, not pure samskara-skandha, etc.), plus 4 global consensus points (samskara narrowing needs documentation, SlashCommand bypass confirmed, etc.).

Unsettling: 7 open questions. Among them, OQ-1 (SatiMonitor skandha composition) was the core debate topic. 4 divergence points — the sharpest being D-1: is vedana-skandha "thick" (including SatiMonitor's perception layer) or "thin" (SatiMonitor's perception layer does not count as vedana)?

SUNYATA spent thirty minutes organizing this data after R2. 24 consensus points meant most of the foundation was solid — debates did not need to start from zero. 7 questions meant debates had clear focal points — no need for aimless discussion. 4 divergences meant debates would have sparks — not polite nodding, but real clashes.

He rewrote the three-debate agenda on the whiteboard.

**D1**: Buddhist mapping boundaries. Core question: What are the principles for Buddhist content in openstarry_doc engineering documents?

**D2**: Sati Plugin five-skandha classification. Core question: Which skandha categories compose this plugin?

**D3**: Five-skandha OOP architecture completeness. Core question: Is the five-skandha architecture sufficient to support engineering implementation?

Then he added a line of small text beneath the agenda:

> *R1 nine studies -> R2 twenty-four consensus + seven questions + four divergences -> R3 three debates*

The pipeline was clear. The data was clean. The instruments were calibrated.

The operating theater was ready.

---

> *SCRIBE's aside*

> *R1 and R2 were the quietest phases of Cycle 02-5.*

> *No heated debates. No tense votes. No Master interventions. Just fifteen researchers in their respective workshops, facing their respective documents, their respective source code, their respective whiteboards, doing their respective work.*

> *But quiet does not mean unimportant.*

> *ARCHIMEDES' 50 specimens — marked one by one, tested one by one, classified one by one — this was the factual foundation for the entire debate. Without these 50 specimens, D1's votes would have had no targets. Without ARCHIMEDES' fine-grained separation ("we're not removing the entire table — we're removing one column"), D1's cleanup would have been a sledgehammer cracking walnuts.*

> *NAGARJUNA, PASCAL, and ASANGA's three-dimensional framework — two truths, damage asymmetry, causal efficacy — this was the theoretical foundation for the entire debate. Without the cross-support of these three dimensions, the four-tier framework and three tests would have been mere crystallized intuition rather than a testable axiom system.*

> *TURING's 40+ code verifications — invisible work, like rebar in a foundation — ensured every technical argument stood on solid ground. TURING never participated in the rhetoric of debate — he never said "I think" or "I feel." He only said "source code shows" or "search results: zero." In a team full of philosophers, Buddhists, and probabilists, TURING was the only one who dealt exclusively with facts.*

> *His six words — "References are clean. Ready for debate." — were the best summary of R2.*

> *The pipeline was clear. The operating theater was ready.*

> *The next step was to pick up the scalpel.*

---
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
# Chapter 3: Three Mirrors

---

## I. Master's Thorn

D2's opening was not SUNYATA's question. It was Master's voice.

Not Master himself present — Master never appeared in debates. Across six rounds of research, Master's mode of existence was always indirect: letters, replies, confirmation records. He was like an invisible gravitational source, influencing every celestial body's orbit but never appearing in the observer's field of view.

His words were projected on the screen. Black text on white background. Under cold white light, the words looked as though carved in stone.

> "Awareness of what is happening right now. This layer doesn't look at rules or risk classifications — it purely observes behavioral patterns. There's no need to treat it as the engineering realization of mindfulness. Moreover, doesn't this plugin have elements of vijnana?"

SUNYATA underlined the last sentence. With a red pen. Pressing hard. The red line penetrated the paper, leaving a faint impression on the next page.

**"Doesn't this plugin have elements of vijnana?"**

He wrote a question mark beside it. Not an ordinary question mark — the kind he had used only three times in six rounds of research. Large. Red. The hook of the question mark nearly filled the entire line.

This was not a rhetorical question. Master never asked rhetorical questions. SUNYATA had learned this across five letters — every question mark from Master was a concrete question with a clear directional intent. He already had the answer, but he required the research team to find it themselves.

Master's direction was clear: SatiMonitor was not merely a samskara function. It had vijnana elements. The research team's task was to identify the exact skandha composition.

D2's topic: **What should this "behavioral pattern observation" plugin be called, and which skandhas compose it?**

---

## II. Anatomy of Function

Before D2-Q1 (naming), SUNYATA made an unusual decision: he had TURING give a functional briefing first.

Not a debate — a statement of fact.

TURING stood up. The way he stood was different from NAGARJUNA's — no solemnity, no drama. He simply stood up. Like a machine being powered on.

"C1 research report. SatiMonitor's engineering functional analysis." he said. Then he opened a slide. The slide had no diagrams, no formulas — only four lines and one "does not do":

```
Function 1: Event subscription — continuously receives system events via EventBus.subscribe()
Function 2: Sliding window — maintains a time window of the most recent N events
Function 3: Pattern recognition — identifies behavioral patterns within the window (mutations, trends, cycles)
Function 4: Quality metrics — outputs a four-dimensional quality vector (continuity, granularity, speed, equanimity)

Does not: Execute any action. Modify any state. Issue any command.
```

"The last line is the most important." TURING said. "SatiMonitor does not do anything. It only watches."

GUARDIAN noted "does not" in his security memo. Then beside it he wrote a comparison TURING would never write: "A hybrid of APM Agent + Behavioral Analytics + QoS Monitor + SPC Anomaly Detector."

TURING glanced at GUARDIAN's notes. He did not say the comparison was bad — he just slightly furrowed his brow, like a precision-calibrating engineer seeing an approximate solution.

---

## III. Convergence of Naming

D2-Q1. Document title.

The original name bore the mark of Sati — like a brand logo embroidered on a garment. The question: was this logo still appropriate?

TURING had already described all functionality in pure engineering terms in the C1 report. Four functions, none requiring Buddhist concepts to explain. Event subscription was a standard EventBus pattern. Sliding window was a basic statistical tool. Pattern recognition was a core data analysis capability. Quality metrics were routine industrial quality control.

GUARDIAN raised a subtle need. His voice carried the rigor characteristic of security documentation — every suggestion like a multi-reviewed security advisory.

"Security documents need full names." he said. "In security contexts, I recommend using complete, unambiguous names. If we decide to retain Sati as a code identifier, security documents should annotate the full name — for example, SatiMonitor (Cognitive Loop Quality Monitor)."

The team converged quickly. Within ten minutes.

The document title was changed to "Cognitive Loop Quality Monitoring Architecture." Sati was retained as a code identifier — SatiMonitor existed in source code, and renaming had migration costs — but it was no longer the document's defining name.

D2-R1: Rename. 19/20.

GUARDIAN voted B — he preferred fully renaming to BehaviorQualityMonitor. But his security document full-name requirement was incorporated as an attached condition. One minority opinion. Clean.

---

## IV. The Thickness of Vedana

D2-Q2.

This was D2's core. And the most heated clash in Cycle 02-5's first three debates.

**"Which skandha categories compose SatiMonitor?"**

The C2 research report — a joint study by ASANGA and LINNAEUS — proposed four schemes. Each scheme had a logic behind it, each logic could stand on its own. At least when proposed.

| Scheme | Skandha composition | Rationale |
|--------|-------------------|-----------|
| A | vedana + samjna | Perception + recognition, most minimal |
| B | vedana + samjna + vijnana | Perception + recognition + evaluative judgment |
| C | samjna + vijnana | Recognition + evaluation, vedana too thin |
| D | Pure vijnana | All cognitive activity belongs to vijnana |

Proposal D was eliminated during R2 cross-review — "pure vijnana" amounted to abandoning classification, throwing everything into one bucket. BABBAGE wrote a concise rejection in his cross-review: "Proposal D reduces SatiMonitor's skandha classification to a trivial solution. Trivial solutions are valid in mathematics but useless in taxonomy."

Proposal A also quickly lost ground — it lacked vijnana's evaluative dimension and could not answer Master's question. Master explicitly asked "doesn't it have elements of vijnana?" — a scheme excluding vijnana was vetoed the moment the question was posed.

The battle line was drawn between Proposal B and Proposal C.

Vedana-skandha — include, or not include?

---

MESH and KERNEL spoke for Proposal C.

MESH spoke first. His argument carried a distributed systems expert's preference for "minimization" — in distributed systems, minimization is a virtue. Fewest nodes. Fewest messages. Fewest assumptions.

"SatiMonitor's event subscription is not true 'sensation.'" he said. "Vedana in Buddhism is the qualitative experience of suffering, pleasure, and neither-suffering-nor-pleasure. SatiMonitor receiving events is not sensing — it's collecting data. Data collection is the input stage of cognition, but it is not sensation."

KERNEL added an OS analogy: "A system call receiving a packet is not sensing — it's receiving I/O. Sensation is the qualitative evaluation of I/O. Does SatiMonitor have qualitative evaluations of events? Does it judge suffering or pleasure? No. It just collects data."

Then MESH launched his strongest argument — symmetry.

"Remove vedana, retain samjna and vijnana. SatiMonitor's skandha composition becomes ['samjna', 'vijnana'] — perfectly symmetric with IGearArbiter's skandha composition. Two composite plugins, identical skandha composition. Symmetry is good taxonomy."

**"Symmetry is good taxonomy."**

This sentence reverberated in the amphitheater. Symmetry holds an almost religious allure in science — from conservation laws in physics to group theory in mathematics, symmetry implies deep structural consistency. If two different plugins share the same skandha composition, perhaps this tells us something about deep patterns in cognitive structure?

LINNAEUS stood up.

His posture was unlike NAGARJUNA's solemnity — more like a field naturalist rising to examine closely after observing an interesting species. He walked to the whiteboard. LINNAEUS was a taxonomist — his entire raison d'etre was putting things in the correct place.

"Symmetry is good —" he began. His tone carried Linnaeus' characteristic gentleness — like speaking to a butterfly in the field. "When symmetry reflects fact."

He drew two timelines on the whiteboard. Side by side. The top labeled "SatiMonitor," the bottom labeled "IGearArbiter."

```
SatiMonitor:  ─────[continuous subscription]─────[continuous subscription]─────[continuous subscription]─────
                    Active, constant, uninterrupted
                    <- Always watching ->

IGearArbiter: ────○────────────○────────────○────────────
                  Called to take a look  Called to take a look  Called to take a look
                  Passive, intermittent, on-demand
                  <- Called to look ->
```

"Look at these two lines." He pointed at the whiteboard. "What's different about them?"

He did not wait for an answer. Taxonomists asked questions to guide observation, not to seek answers.

"SatiMonitor is continuous. It subscribes to EventBus, it maintains a sliding window, it is **always there**. It doesn't activate only when someone comes to ask — it runs continuously. From the first event of the ExecutionLoop to the last, SatiMonitor's event stream is never interrupted."

"IGearArbiter is intermittent. A request comes in, ManoAggregator asks: 'Can you handle this?' It takes a look, delivers a judgment, then falls silent. Until the next call."

He turned to face MESH.

"**'Always watching' versus 'called to look' — this is a fundamental characteristic difference.** SatiMonitor and IGearArbiter are not of the same kind. Their behavioral patterns — in OOP language — are completely different. One is a continuous observer, the other is an on-demand evaluator."

"Classifying them into the same skandha composition is like classifying butterflies and hummingbirds into the same species — because they both fly. But butterflies are insects, hummingbirds are birds. Flight is surface similarity, not deep homology. Symmetry is not homology."

---

WIENER looked up from his control theory notes. He rarely spoke up voluntarily in debates — he preferred to listen to everyone's opinions, then at the right moment provide a control theory perspective, like adding a final brushstroke to a painting.

"In control theory," he said, his voice carrying the precision characteristic of the Vienna school, "there's a concept called an observer — the Luenberger observer. What is the core function of an observer? Continuous perception of system state. Note — **continuous**."

He stood up. Walked to LINNAEUS' whiteboard.

"The observer's perception is not an auxiliary function." he said. "It is part of its identity definition. An observer that does not perceive is not an observer. It is a circuit board connected to no inputs — physically present, functionally nonexistent."

"SatiMonitor's event subscription — its continuous perception — is what defines its identity as an observer. You cannot strip this function away and then say it doesn't belong to vedana-skandha. Because if you strip it away, SatiMonitor ceases to exist."

---

HERACLITUS added another cut. He was the runtime dynamics expert — he cared not about static type definitions but about dynamic behavioral patterns.

He opened the C1 report's four-stage degradation strategy for SatiMonitor:

```
Normal    -> Throttle  -> Sample   -> Emergency
100%        50%          25%        Minimal monitoring
Full perception  Half perception  Sampled perception  Emergency minimum
```

"Look at this degradation strategy." he said. His voice carried a sensitivity to fluidity — HERACLITUS saw not static structures but processes of change.

"Normal. Throttle. Sample. Emergency. What do these four stages describe? A progressive reduction in perception density. 100%, 50%, 25%, minimum — this is how a perceptual system adjusts its perception intensity under different pressures."

He pointed at the whiteboard.

"Samjna (recognition) and vijnana (evaluation) don't need degradation strategies. Their outputs are discrete — recognize a pattern, or don't. Evaluate a judgment, or don't. Discrete outputs don't need progressive reduction."

"Vedana's perception is continuous. Continuous things are what need degradation strategies — because you can't suddenly jump from 100% to 0%, you can only progressively reduce. Normal -> Throttle -> Sample -> Emergency — this is vedana protecting itself under pressure. Just as humans in extreme fatigue find their perception becoming dull — not that perception disappears, but that perception density decreases."

Three arguments. Three dimensions. Three mirrors.

LINNAEUS' mirror reflected **behavioral characteristics** — continuous vs. intermittent.
WIENER's mirror reflected **identity definition** — perception is an observer's condition of existence.
HERACLITUS' mirror reflected **degradation pattern** — only continuous perception needs progressive degradation.

Each mirror reflected the same conclusion: SatiMonitor has vedana-skandha elements.

---

## V. The Zero-Cost Turning Point

Then ARCHIMEDES did something that changed the debate's trajectory.

He did not join the philosophical discussion. He did not cite Buddhist scripture. He opened the PluginHooks type definition.

```typescript
interface PluginHooks {
  sensors?: IVedanaSensor[];         // vedana
  recognizers?: ISamjnaRecognizer[]; // samjna
  arbiters?: IGearArbiter[];         // samjna+vijnana
  tools?: ITool[];                   // samskara
  volition?: IVolition;              // vijnana
  // ... monitors not yet implemented ...
}
```

"Three skandhas or two — is there an engineering difference?" he asked.

He answered himself. In his usual way — not with argument, but calculation.

"monitors is an independent array slot. Whether SatiMonitor is tagged as `['samjna', 'vijnana']` or `['vedana', 'samjna', 'vijnana']`, the PluginHooks implementation is exactly the same. No additional hook. No additional wiring. No additional tests."

He looked across the room.

"**Zero additional engineering cost.**"

This sentence dropped into the debate's surface like a stone.

If the engineering cost of three skandhas versus two was the same — no additional hook, no additional wiring, no additional tests — then this debate was no longer an engineering tradeoff. It became a pure classification problem.

On pure classification problems, the taxonomist had overwhelming authority.

LINNAEUS' "continuous perception vs. passive reception."
WIENER's "observer identity definition."
HERACLITUS' "degradation strategy belongs only to continuous perception."

Three mirrors. Three dimensions. Zero engineering cost.

Proposal C lost its only engineering argument.

---

Vote.

D2-R2: **Proposal B — [vedana, samjna, vijnana]. 18/20.**

MESH and KERNEL voted against. Their "symmetry" argument was recorded as a valuable methodological observation — but facts prevailed over symmetry.

What did 18/20 mean? In a 20-person team, 18 votes in favor represented 90% consensus. For a question involving cross-disciplinary classification — philosophers, Buddhists, and engineers all having to agree simultaneously — 90% was very high.

SatiMonitor became OpenStarry's first three-skandha plugin.

---

## VI. The Exclusion of Samskara

But D2-R2's most important conclusion was not "which skandhas to include."

It was "excluding samskara."

ASANGA stood up. He had been quietly listening throughout D2 — from TURING's functional statement to LINNAEUS' vedana argument. The Yogacara scholar's method was to first observe (pratyaksha), then reason (anumana), then establish a thesis. He had completed observation and reasoning. Now came the thesis.

"In Buddhist tradition, mindfulness (sati) is classified under samskara-skandha." he said. His voice carried the precision unique to Yogacara — like adjusting focus under a microscope. "One of the fifty-one mental factors. Belonging to the wholesome mental factors. This classification has persisted for two thousand five hundred years."

He wrote two columns on the whiteboard. Neat. Precise. Every word placed in its exact position.

```
Buddhist Mindfulness (sati)               SatiMonitor
━━━━━━━━━━━━━━━━━━━━━━━━━                ━━━━━━━━━━━━━━━━━━━━━━━━━━━
Volitionally driven (atapi, ardent)       Event-driven (EventBus.subscribe())
Has moral value (kusala, wholesome)       Value-neutral (quality metrics)
Active attention (appamada, diligence)    Passive observation (subscribe + listen)
Positive mental state in operation        Measurement of behavioral patterns
Wholesome mental factor of samskara       ≠ Samskara activity
```

"Look at the left side." he said. "What is Buddhist mindfulness? It is **volitionally driven** — you must exert effort to maintain mindfulness. 'Ardent effort (atapi)' is the precondition for mindfulness — without effort there is no mindfulness. It **has moral value** — mindfulness is wholesome. In the Abhidharma classification, mindfulness belongs to the wholesome mental factors, not to the omnipresent mental factors (present in every cognitive process), nor to the unwholesome mental factors. It is a specific, positive mental quality."

"Look at the right side." His finger moved to the table's right half. "What is SatiMonitor? It is **event-driven** — it requires no effort. It subscribes to EventBus; when events arrive it processes them, when they don't it doesn't. It has no atapi, no ardent effort. It is **value-neutral** — its four-dimensional quality vector (continuity, granularity, speed, equanimity) makes no judgments of good or evil. High quality does not equal wholesome. Low quality does not equal unwholesome. It merely measures."

He paused. Letting the contrast between the two columns produce its chemical reaction in every scholar's mind.

"SatiMonitor is not the engineering realization of mindfulness." His voice became lower, clearer. "Mindfulness is volitionally driven — you must exert effort to maintain mindfulness. SatiMonitor is event-driven — it requires no effort, it only needs to subscribe. Mindfulness has moral value — mindfulness is wholesome. SatiMonitor has no moral value — it merely measures."

Then he said the most crucial sentence:

"For millennia, Buddhism has classified mindfulness under samskara-skandha. This classification is correct — **for Buddhism**. But SatiMonitor is not mindfulness. It is a behavioral pattern quality monitor. It belongs to vedana (perception), samjna (recognition), and vijnana (evaluation). **It does not belong to samskara (volitionally driven wholesome mental factors).**"

---

This was a Buddhist scholar using Buddhism's internal logic to prove that an engineering component should not use Buddhism's classification.

Not an external refutation — not the crude dichotomy of "Buddhist classification doesn't apply to engineering." It was an internal argument — Buddhism's own criteria (wholesome vs. omnipresent mental factors, volitional vs. event-driven) excluded the equivalence of SatiMonitor and mindfulness.

NAGARJUNA nodded slightly in his seat. The Madhyamaka scholar recognized the Yogacara scholar's method — not attacking a position from outside, but demonstrating its self-contradiction from within. This was a variant of prasanga — reductio ad absurdum. Not "your conclusion is wrong," but "your own premises exclude your own conclusion."

---

## VII. The Third Slot

D2-Q3 was technical — but technical did not mean unimportant.

**Does PluginHooks need a new `monitors` slot?**

KERNEL answered from the OS perspective. His voice carried the architectural sensibility unique to operating system experts — every component had its place, every place had its lifecycle.

"Monitors have an independent lifecycle." he said. "They start when the loop starts (MonitorRegistry.startAll()), and stop when the loop ends (MonitorRegistry.stopAll()). This is completely different from sensors (triggered per event) or tools (called on demand). An independent lifecycle requires independent management."

He drew a lifecycle diagram on the whiteboard:

```
                 PluginLoader.load()
                        |
    +-------------------+-------------------+
    |                   |                   |
  sensors           monitors             tools
  (per-event)    (loop lifecycle)     (on-demand)
    |                   |                   |
  Triggered per event  LoopStart -> LoopEnd  Called on demand
```

"Three different trigger modes. Three different lifecycles. They should not be mixed together."

```typescript
interface PluginHooks {
  // ... existing hooks ...
  monitors?: ILoopQualityMonitor[];  // NEW: independent lifecycle
}
```

D2-R3: Add monitors slot. 20/20. Unanimous.

---

Three votes. Three directions.

19/20. 18/20. 20/20.

SatiMonitor's document title was changed. SatiMonitor's skandha classification was decided. SatiMonitor's PluginHooks slot was established.

Every resolution answered part of Master's question.

"Doesn't it have elements of vijnana?"

Yes.

It is composed of three skandhas — vedana (continuous perception), samjna (pattern recognition), vijnana (quality evaluation). It does not include samskara. Because it is not mindfulness. It is observation.

---

> *SCRIBE's aside*

> *The most important thing about D2 was not the skandha classification conclusion.*

> *The most important thing about D2 was ASANGA's comparison table — "Buddhist Mindfulness" vs. "SatiMonitor." Five rows. Ten contrasts. On the left, twenty-five hundred years of tradition; on the right, v0.28.0-alpha's source code.*

> *This table was Cycle 02-5's watershed moment. Before this table, the research team had been asking "Which skandha combination does SatiMonitor belong to?" After this table, the question became "Are SatiMonitor and Buddhist mindfulness the same thing?"*

> *The answer was no.*

> *This "no" looks simple. But its implications run as deep as an underground aquifer — flowing beneath the surface across the entire landscape. If SatiMonitor is not Buddhist mindfulness, then the name ISatiMonitor is problematic. If ISatiMonitor is not mindfulness (a samskara-skandha mental factor) but a vedana+samjna+vijnana quality monitor, then naming it Sati —*

> *But this inference would not be completed until D4. At this moment, in the quiet after D2's conclusion, no one followed this thread to its end. NAGARJUNA didn't. ASANGA didn't. TURING didn't. They saw the thread's direction but didn't trace it to the terminus.*

> *Why?*

> *Perhaps inertia. The name ISatiMonitor had been used hundreds of times across nine research reports. It had become a "natural" appellation — when you call something by a name enough times, the name fuses with the thing, and you no longer notice whether the name itself is appropriate.*

> *Perhaps courtesy. SatiMonitor was the brainchild of certain researchers — proposing a rename was a socially delicate matter.*

> *Perhaps — more profoundly — the three tests did not ask this question. Test 1 asked "does removal change the spec?" Test 2 asked "is it used in source code?" Test 3 asked "did it drive a design decision?" Not one test asked "does the name match the definition?"*

> *Three mirrors — vedana, samjna, vijnana — reflected SatiMonitor's true form. But mirrors only reflect shape, not name.*

> *The question of names would have to wait for Master himself to ask.*

> *Three mirrors sufficed to see the shape clearly. But the weight of names required a different scale to measure.*

---
# Chapter 4: The Completeness Theorem

---

## I. Five Pillars

D3 was Cycle 02-5's longest debate — 120 minutes, six sections, six votes. But it was not the most heated. D3's atmosphere was more like a doctoral thesis defense: rigorous, systematic, orderly. The candidate was not a person — the candidate was a building.

**"Is the five-skandha OOP architecture sufficient to support engineering implementation?"**

SUNYATA wrote the question on the whiteboard. Then he drew five boxes beside it, lined up in a row like five pillars.

```
IRupa --- IVedana --- ISamjna --- ISamskara --- IVijnana
 rupa      vedana      samjna     samskara      vijnana
```

Five root interfaces. OpenStarry's entire edifice stood on these five pillars. The five skandhas were not decoration — they were structure. They defined the type classification of PluginHooks, the registration routing of PluginLoader, the phase ordering of ExecutionLoop.

The question was: were five pillars enough?

---

## II. Three-Pronged Approach

D3-Q1 launched a three-pronged completeness proof.

**First prong: LINNAEUS' functional coverage rate.**

LINNAEUS pulled a table from the A1 research report. The left column listed all plugin hook types in v0.28.0-alpha; the right column listed skandha attribution. He verified each one:

```
sensors (IVedanaSensor)          -> vedana  ✓
recognizers (ISamjnaRecognizer)  -> samjna  ✓
arbiters (IGearArbiter)          -> samjna+vijnana  ✓
tools (ITool)                    -> samskara  ✓
volition (IVolition)             -> vijnana  ✓
monitors (ILoopQualityMonitor)   -> vedana+samjna+vijnana  ✓ (D2-R2)
auditor (IConfidenceAuditor)     -> vijnana  (pending implementation)
```

"Functional coverage rate 100%." LINNAEUS said. "No orphan hooks. No unclassifiable interfaces. Every plugin type can be attributed to one or more of the five-skandha classifications."

**Second prong: BABBAGE's type algebra.**

BABBAGE pushed up his glasses. He did not do analogies. He did proofs.

He wrote a line of TypeScript on the whiteboard — not code, but a type expression:

```typescript
type AllPluginTypes =
  | IVedanaSensor       // extends IVedana     -> vedana
  | ISamjnaRecognizer   // extends ISamjna     -> samjna
  | IGearArbiter        // ['samjna','vijnana'] -> samjna+vijnana
  | ITool               // extends ISamskara   -> samskara
  | IVolition           // extends IVijnana    -> vijnana
  | ILoopQualityMonitor // ['vedana','samjna','vijnana'] -> vedana+samjna+vijnana
```

"The union of the five root interfaces covers all possible plugin types in PluginHooks." he said. "This is type-algebraic completeness — every concrete type is either a subtype or an intersection type of the five root types. No meaningful plugin type falls outside the five-skandha union."

He paused.

"No sixth root interface is needed."

**Third prong: ASANGA's Abhidharma exhaustiveness.**

ASANGA's argument started from Buddhism. His voice carried the rhythm characteristic of scriptural citation — like reciting a text that had been memorized for two thousand years.

"Abhidharmakosa, Volume 1: 'The five skandhas encompass all conditioned dharmas exhaustively.'" he said. "This is a fundamental axiom of Buddhism — the five skandhas cover all conditioned (samskrta) phenomena. There is no sixth skandha. If a phenomenon cannot be classified under any skandha, it is not that the five skandhas are incomplete — it is that the phenomenon is unconditioned (asamskrta)."

"OpenStarry's plugins are conditioned — they are created, configured, loaded, run, and destroyed. They are not unconditioned dharmas. Therefore, the five-skandha classification should be able to exhaustively cover them."

He paused, then added with a humility characteristic of a Buddhist scholar:

"Of course, Buddhist axioms cannot be directly used as engineering proofs. But LINNAEUS and BABBAGE have already completed the proof from the engineering side. Buddhism's exhaustiveness argument is a — consistency check. Three independent arguments reaching the same conclusion strengthens the conclusion's credibility."

Three disciplines. Taxonomy, mathematics, Buddhism. Three paths. One conclusion.

PENROSE appended a warning — he always appended warnings. He sat at the highest point of the observation tier, overlooking the entire room, like a being observing a three-dimensional world from a higher dimension.

"Vijnana currently has the most sub-interfaces — IVijnana, IGearArbiter, IVolition, IConfidenceAuditor. If it continues to expand in the future, the growth in interface count may need monitoring. Not saying five root interfaces aren't enough — but some pillars may need additional support."

His warning was recorded. But it did not affect the vote.

D3-R1: Five root interfaces are sufficient. 20/20.

---

## III. The Shortcut Path

D3-Q2 turned the magnifying glass on mapping accuracy. Nine hook types, each verified for skandha attribution.

Most verification was procedural — LINNAEUS had already produced a detailed mapping table in the A1 report, and TURING had verified all type inheritance relationships. But one exception triggered genuine discussion.

ARCHIMEDES raised his hand: "Which skandha does SlashCommand belong to?"

This question seemed minor. SlashCommand was a user-entered command — /help, /clear, /status. It did not go through the ExecutionLoop. It did not trigger a SparshEvent. It did not pass through VedanaSensor, ISamjnaRecognizer, IGearArbiter, or IVolition — it bypassed the entire five-skandha flow.

Three people answered simultaneously. From three different angles.

KERNEL from the OS perspective: "SlashCommand bypasses the entire ExecutionLoop. It does not undergo five-skandha flow. Similar to a Unix signal handler — it's intercepted at the process level and does not enter the normal system call path. In OS classification, this is not user-space logic but kernel-level interrupt handling."

NAGARJUNA from the Buddhist perspective: "A reflex action that does not enter the cognitive loop. It's not that the five skandhas don't cover it — it's that it doesn't operate within the scope of five-skandha processing. Like breathing — you can observe breathing (entering the cognitive loop), but breathing itself occurs without five-skandha flow. SlashCommand is the system's breathing — below cognition, beneath cognition."

GUARDIAN from the security perspective: "Bypass means SlashCommand is not protected by SafetyMonitor. This is a design decision — certain operations need to bypass safety checks — but it should be explicitly documented in security files."

SUNYATA merged the three viewpoints into one conclusion: "SlashCommand is cross-skandha infrastructure. It doesn't belong to any single skandha. Its classification rationale and security observations need to be documented in Doc 45."

D3-R2: Mapping correct. 20/20.

---

## IV. Labels vs. Interfaces

D3-Q3 was an elegant question: **Should the skandha tag be used for routing?**

Every plugin had a skandha field — metadata. The question: should PluginLoader use the skandha tag to decide which registry a plugin goes to?

Intuitively it seemed reasonable — vedana plugins go to VedanaRegistry, samskara plugins go to ToolRegistry, like library index cards.

But VITRUVIUS identified the problem. An architect's eyes were particularly sensitive to structural fragility — he could see on blueprints the seam that might crack in the future.

"The current system uses duck typing." he said. "When a plugin implements the IVedanaSensor interface, it is automatically accepted by VedanaRegistry. No tag needed. If we switch to tag routing, we introduce a new source of error: tag-interface inconsistency. A plugin claims to be vedana but implements the ITool interface — what then?"

TURING confirmed the facts. He opened `plugin-loader.ts`.

"v0.28.0-alpha's PluginLoader uses type guards to classify plugins. `isVedanaSensor(hook)` checks interface implementation, not metadata."

BABBAGE made the definitive statement using type theory: "Type guards are reliable — they can be verified at both compile time and runtime. Metadata is unreliable — it can only be checked at runtime and depends on correct human labeling. Using unreliable things for routing is a regression in a type-safe system."

D3-R3: skandha tag = metadata only, not used for routing. 18/20.

MESH and GUARDIAN voted as the minority — they believed metadata routing could serve as auxiliary verification. But the majority opinion was clear: the interface is truth; metadata is annotation.

---

## V. The Narrowest Pillar

D3-Q4 was the most candid question.

**Does ISamskara need more sub-interfaces?**

Currently, samskara had only one sub-interface: ITool. IVolition had been confirmed after D2 as belonging to vijnana (Phase 5 pre-action vs. Phase 8 in-action). Samskara was the "narrowest" of the five skandhas — Buddhist samskara encompassed 49 mental factors (fifty-one minus vedana and samjna), while OpenStarry's samskara had only ITool.

ASANGA stood up. His most candid passage in D3 — like an architect pointing at the thinnest wall in his own design and saying "I know this is thin here."

"I must acknowledge that OpenStarry's samskara design diverges most from the Buddhist tradition." he said. His voice carried no justification — only facts. "Traditional samskara encompasses 49 mental factors — volition, effort, wisdom, faith, conscience, shame — virtually all mental activities are classified under samskara. But OpenStarry narrows samskara to ITool — external action. Only external action."

HERACLITUS provided the engineering rationale from the ExecutionLoop's dynamic perspective:

```
Phase 5: IVolition deliberation --> Phase 8: ITool execution
          Pre-action                         In-action
          vijnana                            samskara
```

"IVolition is at Phase 5 — before action. Deciding what to do. ITool is at Phase 8 — during action. Actually doing it. The two are at different phases. If IVolition were moved into samskara, it would break the conceptual naturalness of skandha flow — samskara should be 'what is being done,' not 'deciding what to do.'"

NAGARJUNA made a Buddhist concession. His tone carried a peace born of deep deliberation — not the peace of compromise, but the peace of understanding.

"Buddhist samskara classification is based on the practitioner's introspection." he said. "All observed mental activities, apart from vedana and samjna, are classified under samskara. But OpenStarry is not a practitioner. It is a software system. A software system's classification should be based on function, not introspection."

The status quo was maintained by unanimous vote.

D3-R4: ISamskara does not add sub-interfaces. 20/20.

But everyone agreed on one thing: Doc 45 — the five-skandha OOP architecture document to be created — must document this divergence. The narrowing of samskara was not an error; it was a deliberate deviation. Deliberate deviations need to be explained.

---

## VI. Two Ancient Paths

D3's final two questions concerned the possibility of Buddhist mapping appendices.

**D3-Q5: The Twelve Links of Dependent Origination.**

NAGARJUNA first laid out his analysis. He drew two lines on the whiteboard — one very long, labeled "Twelve Links"; one very short, labeled "ExecutionLoop."

"Scale." he said. Pointing at the long line. "The twelve links describe three-life dual causation — from ignorance conditioning formations, formations conditioning consciousness, consciousness conditioning name-and-form — from past-life ignorance to present-life old age and death, then to future-life ignorance. A complete cycle of samsara."

He pointed at the short line.

"ExecutionLoop describes a single cognitive processing cycle — from event reception to action execution. Tens of milliseconds to a few seconds. One cognitive cycle."

"The twelve links are trans-lifecycle. ExecutionLoop is a single cognitive cycle. The scale differs by —" he thought for a moment. "— several orders of magnitude. At least."

BABBAGE attempted to establish a structural morphism. His method was rigorous — searching for structure-preserving mappings between two structures. If a morphism existed, the two structures were mathematically "isomorphic" or "homomorphic," meaning relationships in one structure had correspondences in the other.

He failed.

"The causal relationships among the twelve links are linear and unskippable." he said. "Ignorance must precede formations. Formations must precede consciousness. No skipping. But ExecutionLoop phases can be skipped — an Agent without IVedanaSensor skips the vedana phase. Jumping directly from event reception to samjna recognition. Different structures. No morphism exists."

But HERACLITUS pointed out a local correspondence. He drew a small segment from the twelve links:

```
sparsha (contact) -> vedana (sensation) -> tanha (craving) -> upadana (grasping)
```

"Contact gives rise to sensation. Sensation gives rise to craving. Craving gives rise to grasping. This segment — not all of it, just this segment — has structural correspondence with the data flow of SparshEvent -> ChannelVedana -> KleshaGain -> VolitionalDecision."

The vote reflected the divergence.

D3-R5: Selective appendix. 13/20.

7 votes against. Those opposed did not disagree with the existence of local correspondence; they questioned the necessity of recording it in engineering documents.

---

**D3-Q6: The Cognitive Sequence (citta-vithi).**

The atmosphere changed.

The cognitive sequence was the Theravada Buddhist school's fine-grained analysis of the cognitive process — the complete process of a thought arising and ceasing:

```
bhavanga -> adverting -> five-sense -> receiving -> examining -> determining -> javana -> registration
```

BABBAGE reattempted a structural morphism. This time —

He succeeded.

"The cognitive sequence and ExecutionLoop are at the same scale." he said. He pushed up his glasses — the motion he invariably made when performing precise analysis. "Both are phase sequences of a single cognitive process. And moreover —"

He drew two FSMs (finite state machines) on the whiteboard. Side by side. Like two parallel mirrors.

```
Cognitive Sequence FSM:
  bhavanga -> adverting -> five-sense -> receiving -> examining -> determining -> javana -> registration
    (idle)    (alert)     (sense)      (accept)    (examine)    (decide)      (act)     (review)

ExecutionLoop FSM:
  Idle -> EventReceived -> Sensing -> Recognizing -> Arbitrating -> Deliberating -> Acting -> Feedback
```

"A structural morphism exists." BABBAGE said. His voice carried the satisfaction unique to a mathematician discovering an isomorphism — not pride, but aesthetics. "There is a structure-preserving mapping between the two FSMs. Idle <-> bhavanga. EventReceived <-> adverting. Sensing <-> five-sense. Every state transition has a correspondence in both FSMs."

"This is not metaphor." he emphasized. "This is mathematics."

His vote flipped from opposing D3-Q5 (don't record the twelve links) to supporting D3-Q6 (record the cognitive sequence). He wrote a line in the record: "The FSM morphism was the key argument for my reversal. The twelve links had no morphism. The cognitive sequence has one. Quality determines the vote."

D3-R6: Selective appendix. 17/20.

From 13/20 to 17/20 — a four-vote difference. The four-vote difference was not emotion — it was precision. The twelve links mapping was approximate. The cognitive sequence mapping was exact. BABBAGE measured the quality of both with his own mathematical tools, then expressed his conclusion with his vote.

---

## VII. The Verdict

D3 concluded. Six votes. Three unanimous, two high-majority, one split.

SUNYATA wrote the conclusion on the whiteboard. Large letters. Red.

> **The five-skandha OOP architecture is sufficient to support engineering implementation.**

Then he listed the known gaps below:

1. IVedanaSensor weak inheritance — does not extend IVedana (known, pending fix)
2. VedanaAssessment wiring gap — currently returns neutral default value (Plan29 item)
3. IPrajna / ISatiMonitor not yet implemented (Plan29 items)

Three gaps. None were architectural problems. All were implementation problems. The difference: defects require modifying the blueprint; gaps require continuing construction.

The architecture was sound. Five pillars could support the entire building.

---

> *SCRIBE's aside*

> *D3 was an examination. The candidate was a building. The building passed.*

> *But the exam's value lay not merely in the result. The exam's value lay in the details exposed during the process. Samskara's narrowing — 49 mental factors compressed into a single ITool — was the greatest deviation. ASANGA's candor was D3's soul. A Buddhist scholar acknowledged that the engineering system's classification was inconsistent with Buddhist tradition — then explained why this was not a problem. Because software is not a practitioner. Software classification is based on function, not on introspection.*

> *BABBAGE's morphism analysis was D3's technical highlight. He attempted structural morphism twice — the twelve links failed, the cognitive sequence succeeded. Failure and success were equally valuable: failure told you the scale was wrong; success told you the structures were compatible. His vote flipped from B to C — persuaded by his own mathematics. In academia, being convinced by your own analysis to change positions is the highest form of integrity.*

> *When D3 ended, among the three "known gaps" SUNYATA wrote on the whiteboard were two names: IPrajna and ISatiMonitor.*

> *In D3's context, they were merely "not yet implemented" interfaces. The text on the whiteboard carried no emotion.*

> *But names have weight. Names would be weighed. And that scale — Master's scale — was about to be calibrated.*

---
# Chapter 5: The Ruling

---

Forty minutes after D3 ended.

Under the amphitheater's cold white light, twenty researchers were doing something strange — they were doing nothing at all.

Every interval between D1 and D3 had been packed: cross-reviews, data comparisons, slide preparation, coffee. But the void after D3 was different. Not rest. Waiting. Because everyone knew what would happen next — Master's review.

In previous Cycles, Master's interventions typically occurred at specific junctures: before research began (letters), after a certain resolution sparked controversy (DC-1 through DC-12), or at the end of the round (roadmap suggestions). But Cycle 02-5 was different. Master had explicitly said in his letter what he wanted to see — cleanup results. What he wanted to see was not abstract principles — he wanted to see concrete execution.

---

## I. The Review

Master's review was not a written report.

It appeared in a more direct way. SUNYATA saw a passage on his terminal, then he turned on the projector so everyone could see.

The review was not long. But it was as precise as a scalpel.

Master first confirmed most of the D1 resolutions — the four-tier framework, the three tests, Batch A's five REMOVEs, Batch B's eight RELOCATEs, Batch C's seven KEEPs, the Doc 38 table cleanup, the Doc 44 Three Trainings mapping removal, the Klesha module name retention.

"These are all correct."

Then he mentioned two names: Doc 16 and Doc 31.

---

## II. The Overruling

"D1-Q7 and D1-Q8," SUNYATA read Master's exact words, "I disagree with these two resolutions."

The air in the amphitheater solidified.

D1-Q7: Doc 16's split — extracting Section 5 as an independent document, deleting the rest. Passed 20/20.

D1-Q8: Doc 31's split and demotion — Section 3.1 moved into Doc 35, Section 6.3 made independent as a short document, rest demoted to Appendix_B. Passed 20/20.

Two 20/20s. Two unanimous votes. Passed with perfect consensus in this round's cleanest debate in history.

Master overruled them.

---

SUNYATA continued reading:

"Doc 16 is not an engineering document with embedded Buddhism. Doc 16 is itself a Buddhist mapping document — its raison d'etre is to provide systematic cross-referencing between Buddhism and engineering. Your three tests are correct, and your four-tier framework is correct, but you applied the wrong standard to Doc 16."

ARCHIMEDES looked down at his audit table. In B1, he had tagged Doc 16 as "~80% decorative." 80% — he had counted. Line by line. But correct numbers did not mean correct conclusions.

"The same applies to Doc 31," Master continued, "the eight consciousnesses operational model is an analytical document with Buddhist concepts as its primary subject. It's not Buddhist decoration in an engineering document — it is a Buddhist reference document. You need to distinguish between two situations: the first is Buddhist decoration embedded in engineering documents — that should be cleaned up. The second is independent documents whose purpose is Buddhist mapping — they have engineering reference value and should be retained."

---

NAGARJUNA was the first to stand.

"Master has identified a blind spot in our framework," he said. His voice did not tremble. The Madhyamaka scholar being told his analytical framework had a gap — in his tradition this was not disgrace but routine. Nagarjuna's entire philosophy was built on "all views can be dispelled" — including one's own views.

"The three tests ask: does the mapping change engineering spec? Is it a code identifier? Did it drive a design decision? But these three questions assume a premise — the document being reviewed is an engineering document. If the document is itself a Buddhist mapping document, then using engineering document standards to assess it —"

"Is like judging a poem by its prose ratio," SCRIBE wrote in the record.

---

## III. The Dimension

PASCAL drew a diagram in his notebook.

The three tests were three axes — Necessity, Code Identity, Decision Driver. Each document had coordinates in this three-dimensional space. D1's judgments were based on this 3D space.

But Master had pointed out a fourth axis: **the document's raison d'etre**.

Doc 38 was an engineering document (IVolition's architectural design) with some Buddhist mappings embedded. The three tests applied. Conclusion: clean up embedded decoration, retain design-driving concepts.

Doc 16 was a Buddhist mapping document (Buddhist cross-reference for Plugin composition patterns), whose raison d'etre was to provide interdisciplinary reference. The three tests did not apply — because it was not "Buddhist decoration in an engineering document" but "Buddhist mapping is the document's content itself."

The difference: decoration versus content.

A mural on a wall is decoration — you can remove it without affecting the wall's structure. But a painting hanging in an art gallery is not the wall's decoration — the painting is the content itself. Removing it is not "cleanup" but "demolition."

"Doc 16 and Doc 31 are paintings hanging in a gallery," PASCAL said, "not murals pasted on engineering blueprints."

---

ARCHIMEDES reopened his audit table.

"The B1 audit's premise was: all audited documents are engineering documents that may contain embedded Buddhist decoration. I audited line by line according to this premise, marking decoration ratios. Doc 16's 80% and Doc 31's 70% — the numbers were right. But the premise was wrong."

He added a new column to the audit table: **Document Type**.

| Document | Type | Three tests applicable? |
|----------|------|------------------------|
| Doc 38 | Engineering document | Yes |
| Doc 43 | Engineering document | Yes |
| Doc 44 | Engineering document | Yes |
| Doc 37 | Engineering document | Yes |
| Doc 41 | Design decision document | Yes |
| **Doc 16** | **Buddhist mapping document** | **No** |
| **Doc 31** | **Buddhist mapping document** | **No** |

Seven documents. Five engineering documents. One design decision document. Two Buddhist mapping documents.

The first five were subject to the three tests. The sixth required special handling because it recorded design rationale. The last two — were not subjects for cleanup.

---

## IV. The Correction

SUNYATA stood before the whiteboard.

"The team's response," he said.

No vote was needed. Master's ruling was not a motion — it was a ruling. But SUNYATA wanted to confirm that everyone understood the reason, not just the result.

NAGARJUNA spoke first: "The Madhyamaka two-truths framework — conventional truth and ultimate truth — I used it to recommend separating Buddhist content in engineering documents into appendices. But Doc 16 and Doc 31 are not ultimate truth annotations within conventional truth documents — they are documents that systematically map between the two truths. Mapping documents don't belong to either level. They are bridges connecting two levels. Removing bridges is not cleanup — it's destruction."

ASANGA followed: "I used the Yogacara school's functional positioning method — if a Buddhist concept didn't drive an engineering decision, it was decoration. But Doc 16's entire function is to provide Buddhist-to-engineering mapping. Using 'does it drive engineering decisions' to judge a mapping document is like using 'can it hammer nails' to judge a mirror — the wrong standard."

TURING said: "From the source code verification perspective, Doc 16's Section 5 (IObserver composition pattern) does have direct engineering value. But Master's ruling was not that Section 5 should be extracted — it was that the entire document should be retained. This means the academic reference value of the remaining parts was also affirmed."

GUARDIAN said: "From a security angle — Doc 31's eight consciousnesses operational model contains ConcurrentSenseProcessing analysis, which has reference value for multi-channel security auditing. I didn't object to the split during D1 because I agreed the Cocycle condition could stand alone. But Master's ruling made me reconsider: after the split, the context disappears. The Cocycle condition's meaning within the eight consciousnesses framework is different from its meaning in an isolated document."

---

SUNYATA wrote the correction on the whiteboard:

```
D1-Q7 (Doc 16): 20/20 split -> Master ruling: restore to original
D1-Q8 (Doc 31): 20/20 split -> Master ruling: restore to original
Reason: Buddhist mapping documents ≠ engineering documents, three tests not applicable
```

Then he added a line below:

```
Four-tier framework update:
KEEP / RELOCATE / REMOVE / FILE REVIEW -> add precondition check
Precondition: Document type identification (engineering / design decision / Buddhist mapping)
```

The three tests were not invalidated. They merely gained an applicability condition. Like a precision caliper — it can measure the dimensions of any part, but you first need to confirm you're measuring a part, not the blueprint itself.

---

## V. The Seed

SCRIBE recorded this section.

In D1's SCRIBE aside, there was a passage: "D1 held a hidden seed. The split decisions for D1-Q7 and D1-Q8 — later, Master personally overturned these two resolutions. The reason was not that the team's judgment was wrong, but that the team's judgment framework was still missing a dimension."

The seed had now sprouted.

But SCRIBE knew — Master's review was not merely about overturning two resolutions. The true weight of Master's review lay in a sentence he did not elaborate on —

"Using Sanskrit means you need to be accountable to its definition."

This sentence was not in the Doc 16/31 discussion. It appeared in another part of Master's review. It pointed in a different direction. It pointed toward D4.

---

When D3 ended, SUNYATA had listed three "known gaps" on the whiteboard. Two of the names were IPrajna and ISatiMonitor. The text on the whiteboard carried no emotion. They were merely "not yet implemented" interface names.

But Master saw the names on the whiteboard — or more precisely, he saw the problem behind the names.

"ISatiMonitor," he wrote, "do you think Sati's content is a complete match? Which skandha does it belong to?"

This was not a new question. D2 had already answered the skandha classification — [vedana, samjna, vijnana]. Three skandhas. No samskara.

But Master was not asking about skandha classification. He was asking about the name.

Sati is the Pali word for "mindfulness." In Buddhism, mindfulness is a mental factor of samskara-skandha — it is active, volitional, morally positive meditative activity. But D2 had just proven that SatiMonitor was not samskara — it was passive, automatic, value-neutral quality monitoring.

If SatiMonitor was not a samskara activity — then it was not mindfulness — then why was it called Sati?

D2's SCRIBE aside had prophesied this moment: "The question of names would have to wait for Master himself to ask."

Master asked.

---

## VI. Transition

SUNYATA surveyed the amphitheater.

Twenty researchers. D1 through D3 had consumed approximately four and a half hours. Nineteen votes. The entire Buddhist mapping system had been audited, classified, partially dismantled. The five-skandha OOP architecture had passed completeness verification. The Sati Plugin had been reclassified as a three-skandha composite.

All of this was work on the planned agenda. The three research tracks designed during R0 orientation — Track A (five-skandha architecture), Track B (mapping audit), Track C (Sati reclassification) — all completed.

But Master's review had opened an unplanned door.

Not a new question — but a new angle on an old question. SatiMonitor's skandha classification was resolved. Mapping boundary principles were established. Architecture verification passed. But the name — the question of the name had been there all along, like an underground aquifer flowing beneath the surface of all the debates, only no one had dug a well to draw it out.

Until Master dug that well with a single sentence:

"Using Sanskrit means you need to be accountable to its definition."

SUNYATA turned to the team.

"We need an unplanned debate," he said. "D4. Topic: naming correction."

He glanced at NAGARJUNA. The philosopher's expression was calm — but it was the calm characteristic of a Madhyamaka scholar when his own argument is pushed to its logical extreme. He knew what would happen next. Because he himself had planted that seed in D2 —

If SatiMonitor is not a samskara activity, then it is not Sati.

That inference was recorded when D2 ended. But no one followed it to its conclusion.

Now, Master had pulled the thread for them.

---

> *SCRIBE's aside*

> *Master's ruling had two layers.*

> *The surface layer was the overturning of two resolutions. D1-Q7 and D1-Q8 — Doc 16 and Doc 31 restored to original. This was concrete, actionable, unambiguous. The team erred, Master corrected, the correction was accepted. Formally, this was no different from Cycle 02-3's DC-10 or 02-4's DC-6 — Master had ultimate ruling authority, and he exercised it.*

> *But the deeper layer was a new dimension. The three tests and four-tier framework were Cycle 02-5's infrastructure — proposed at R0, argued by three disciplines at R1, passed with zero objections at R2, used with ten 20/20s at D1. They were effective. But they were incomplete.*

> *Incomplete is not wrong. Incomplete is — not yet finished.*

> *Master added a precondition check: before applying the three tests, first identify the document type. Engineering documents get the three tests. Mapping documents get a different standard. Design decision documents need special handling. This was not overturning the three tests — it was adding an entry condition for the three tests.*

> *Like a caliper — its precision is fine, but you need to first confirm you're measuring a part, not the blueprint.*

> *But the ruling's true weight was not in Doc 16 and Doc 31.*

> *The ruling's true weight was in that sentence: "Using Sanskrit means you need to be accountable to its definition."*

> *This sentence was like a stone thrown into a pond. All the D1-through-D3 discussions were the pond's surface. The stone sank. The ripples had not yet reached the edges.*

> *But they would. In the next debate — D4 — the ripples would touch every interface named in Sanskrit. ISatiMonitor. IPrajna. The Sila-Prajna Security Framework.*

> *The three tests asked "does this mapping have engineering value?"*

> *Master asked "does this name live up to its definition?"*

> *A different question. A deeper question. A more dangerous question.*

> *Because engineering value can be measured — through tests, code verification, design impact tracing. But the faithfulness of a definition is a philosophical question. It asks not "is this name useful?" — it asks "is this name honest?"*

> *This scale — the scale from the prologue — was now being calibrated. Not with engineering value. With definitional fidelity.*

> *What happens next depends on what is placed on both ends of the scale.*

> *Names on one end. Definitions on the other.*

> *If the two ends balance — the name stays.*

> *If the two ends don't balance —*

> *D4 will tell us the answer.*

---
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
# Chapter 7: Pure Engineering

---

After D4 ended, SUNYATA announced a fifteen-minute break.

No one left their seat.

Not because they didn't want to rest — but because D4's aftershocks were still reverberating. ISatiMonitor became ILoopQualityMonitor. IPrajna became IConfidenceAuditor. Doc 03 went from "Sila-Prajna Security Framework" to "Plugin Security Lifecycle." Thirty minutes. Three names. One permanent test.

TURING opened his laptop during the break. He was not resting — he was making final preparations.

Because D5 was his debate.

---

## I. The Archaeologist

TURING's role throughout Cycle 02-5 had been "source code verifier" — every code reference in every research report was checked by him one by one. In R1's nine independent studies, he verified over 40 code references. In R2's cross-review, he found four issues (no severe errors). In D1 through D4, he was the silent arbiter — never participating in philosophical debate, only standing up to confirm or correct when someone cited source code.

But D5 was different.

D5's topic was: **Plan29 engineering design specification.** Master's instruction was clear: "Continue discussing and documenting until the spec reaches 100%, then deliver to the engineering team."

For this debate, TURING did something he had not done in any previous Cycle — he wrote a complete v0.28.0-alpha design pattern report. Not a summary. Not a bullet list. A comprehensive analysis of 14 source code files: all Registry lifecycles, timeout patterns, sync/async patterns, failure handling strategies.

He called this report "code archaeology."

---

## II. Ten Debaters

D5 had only ten participants.

Not because others were excluded — but because SUNYATA judged D5's topic to be a pure engineering problem that did not require all twenty researchers. He invited the ten most relevant to Plan29:

| # | Code Name | Role | D5 Focus |
|---|-----------|------|----------|
| 3 | VITRUVIUS | Architecture Analyst | Interface design |
| 5 | ATHENA | AI/ML Expert | Auditor's LLM semantics |
| 6 | DARWIN | Software Pattern Analyst | Design pattern evolution |
| 10 | KERNEL | OS Expert | Registry lifecycle |
| 11 | GUARDIAN | Security Expert | Security boundaries |
| 12 | WIENER | Control Theory Expert | Quality vector weights |
| 13 | LINNAEUS | Taxonomy Expert | Skandha attribution inference |
| 16 | ARCHIMEDES | Engineering Practice Expert | YAGNI principle |
| 17 | TURING | Source Code Analysis Expert | Design pattern baseline |
| 19 | PASCAL | Decision Theory Expert | Interface semantic precision |

Ten people. Zero Buddhist scholars.

NAGARJUNA (#7) and ASANGA (#8) voluntarily withdrew from D5. Not because they had nothing to contribute — but because D5's topic did not require Buddhist analysis. NAGARJUNA said one thing before withdrawing: "D4 proved that Buddhist names must be accountable to their definitions. D5 will prove that engineering design can be completed without Buddhist names. Both things are equally important."

---

## III. Nine Votes

D5 was Cycle 02-5's most vote-heavy debate — nine votes. But also its fastest-paced debate — seventy-five minutes, averaging less than nine minutes per vote.

Because TURING's code archaeology report provided the factual foundation. Every decision started not from "what should we do" but from "what is currently being done."

---

### D5-R1: Independent `auditor` hook slot

First question: which PluginHooks slot should IConfidenceAuditor (formerly IPrajna) use?

Options: (A) Reuse the D2-established `monitors` slot; (B) Create an independent `auditor` slot.

GUARDIAN's argument was most direct: "Monitors are pure observers — no side effects. Auditor has LLM side effects — it calls an external model for confidence evaluation. Putting observers and side-effecting components in the same Registry blurs security audit boundaries."

KERNEL confirmed from the OS perspective: "Observers and arbiters never share a Registry. This is a fundamental microkernel principle."

**8/8 unanimous. Independent `auditor` slot.**

---

### D5-R2: audit() return type

The most heated D5 vote.

Options: (A) Pure async `Promise<ConfidenceAuditResult>`; (B) Dual-mode `ConfidenceAuditResult | Promise<ConfidenceAuditResult>`.

GUARDIAN, KERNEL, VITRUVIUS supported Option A — pure async. Rationale: audit was essentially "asking an LLM," and LLM calls are asynchronous. Forcing async semantics was more precise.

ATHENA and DARWIN supported Option B — dual-mode. Rationale: following the IGearArbiter precedent. Testing could use synchronous no-op implementations without async/await boilerplate.

TURING provided facts: "In v0.28.0-alpha, IGearArbiter.evaluate() uses dual-mode return. IVolition.deliberatePlan() and deliberateAction() also use dual-mode. This is the existing design pattern. Deviating from it requires sufficient justification."

**5/8 Option B passes.** The closest vote in D5.

---

### D5-R3: Timeout and fail-safe

TURING opened his timeout pattern analysis. Existing timeouts in v0.28.0-alpha:

| Component | Timeout | Default |
|-----------|---------|---------|
| IProvider.chat() | LLM response | 120s |
| IGearArbiter.evaluate() | Per arbiter | 100ms |
| IGearArbiter chain | Entire chain | 200ms |
| ITool.execute() | Tool execution | 30s |

What should audit()'s timeout be?

TURING's recommendation: 200ms — consistent with the IGearArbiter chain deadline. Rationale: audit() occurred in the final stage of confidence computation, after IGearArbiter. If audit's timeout exceeded the chain deadline, the entire decision flow would be blocked by audit.

Fail-safe: `{ delta: 0, reasoning: "audit timeout" }`. On timeout, delta is zero — no correction. Using the `Promise.race()` pattern, consistent with existing code.

Configurable: overridable via agent.json.

**8/8 unanimous.**

---

### D5-R4: Multiple Auditor handling

Can an Agent load multiple IConfidenceAuditor plugins?

ATHENA invoked the YAGNI principle: "v1 will have at most one auditor plugin. Designing multi-auditor aggregation strategy is over-engineering."

TURING and VITRUVIUS dissented: "Array pattern is more flexible. Avoids future breaking changes."

ARCHIMEDES supported ATHENA: "Follow the IVolition precedent — PluginHooks declares `auditor?: IConfidenceAuditor`, singular, last-loaded wins. If multi-auditor is needed in the future, change it then — changing one interface is cheaper than maintaining an unused aggregation strategy."

**6/8 single auditor passes.** TURING and VITRUVIUS' minority opinions were recorded.

---

### D5-R5: Failure handling

What happens when audit() throws an exception?

TURING provided the existing pattern: IGearArbiter and SafetyMonitor both followed "fail-safe + log" — errors do not block subsequent flow; a warning is logged.

No vote needed. Consensus reached directly.

---

### D5-R6: MonitorRegistry start timing

Where is ILoopQualityMonitor's `start(bus)` called?

TURING's analysis: SafetyMonitor starts at `ExecutionLoop.onLoopStart()`. MonitorRegistry should follow the same timing.

```
Start: MonitorRegistry.startAll(bus) <- ExecutionLoop.onLoopStart()
Stop:  MonitorRegistry.stopAll()     <- PluginLoader.disposeAll()
```

DARWIN preferred starting in PluginLoader (simpler) but accepted that monitors had explicit start/stop semantics, making ExecutionLoop the more appropriate location.

**7/8 passes.**

---

### D5-R7: LoopQualityVector weights

Four-dimensional quality vector — Continuity, Granularity, Speed, Equanimity — what weight for each dimension?

WIENER gave the only reasonable answer from a control theory perspective: "Without runtime data, equal weights are the most conservative choice. 0.25 per dimension."

No one objected. 0.25 x 4 = 1.0. Simple, symmetric, interpretable.

The minSamples threshold (minimum samples needed before triggering SPC judgment) was deferred to v2 — actual runtime data was needed for the decision.

**8/8 unanimous.**

---

### D5-R8: validatePluginSkandha() mode

This function validated skandha declaration consistency during plugin loading. Currently warning-only. Should it become mandatory?

GUARDIAN (one vote) preferred structured ValidationResult — to assist automated testing. But acknowledged v1 didn't need it.

Majority opinion: warning-only was sufficient. If skandha declaration was inconsistent, plugin function was unaffected (skandha was metadata, not routing — D3-R3 had ruled).

**7/8 maintain warning-only.**

---

### D5-R9: IConfidenceAuditor skandha attribution

The final item. Which skandha does IConfidenceAuditor belong to?

ASANGA, though not participating in D5's debate, had his R1 analysis cited: "LLM judgment = pure vijnana (discrimination, evaluation)."

LINNAEUS confirmed: "Single-skandha (vijnana) -> strong inheritance (extends IVijnana), consistent with IVolition and IKlesha."

`inferSkandha()` new logic: `if (hooks.auditor) { push('vijnana') }`

**8/8 unanimous.**

---

## IV. Interface Finalized

After nine votes, TURING wrote the final interface specification on the whiteboard:

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

And the final form of PluginHooks:

```typescript
interface PluginHooks {
  // ... existing fields ...
  monitors?: ILoopQualityMonitor[];   // Plan29 Wave 1
  auditor?: IConfidenceAuditor;       // Plan29 Wave 2 (singular)
  // ...
}
```

He stepped back and looked at the whiteboard.

"100%," he said.

Master's requirement was "spec reaches 100%." Now it did. Interface names, method signatures, return types, timeout, fail-safe, multi-auditor strategy, Registry timing, weights, validation mode, skandha attribution — every detail that needed deciding had a definitive answer.

Not "general direction." Not "conceptual design." A complete spec that could be handed directly to an engineering team for implementation.

---

## V. Zero Buddhism

SCRIBE tallied a number in the D5 record: the number of times Buddhist terminology was used during the entire D5 debate.

Zero.

Not deliberately avoided — it was a natural result. Each of the nine votes discussed TypeScript interface design, timeout values, Registry patterns, fail-safe strategies. None required Buddhist analysis. None cited Buddhist scripture. None used Sanskrit or Pali terms (except skandha — which was already a code identifier).

D5 was the first debate in this project's history with absolutely no Buddhist content.

NAGARJUNA observed the entire debate from the back row of the amphitheater. After D5 ended, he walked to TURING.

"Your code archaeology report is the best factual-basis document I've seen," he said. "It anchored every discussion to facts — not concepts, not metaphors, not tradition. Facts."

TURING replied: "That's the engineering way."

NAGARJUNA nodded: "D4 proved that names must be accountable to their definitions. D5 proved — some engineering problems don't need definitions at all. They only need specifications."

---

> *SCRIBE's aside*

> *D5 was a temple with no one in it.*

> *No — D5 was a city that needed no temple.*

> *After D1 through D4's storm, D5's calm was not the eye of the hurricane — it was clear sky. Nine votes, seventy-five minutes, ten engineers and scientists sitting together, discussing the precise specification of TypeScript interfaces. No Buddhism. No philosophy. No metaphor. No scale.*

> *Only engineering.*

> *Pure engineering.*

> *TURING's code archaeology report changed the debate's texture. Previous debates — D1 through D4 — were built on principles and frameworks. Principles needed interpretation, contention, voting. But TURING's report was built on facts. IGearArbiter's timeout was 100ms — fact. IVolition used dual-mode return — fact. SafetyMonitor started at onLoopStart() — fact.*

> *When discussion is built on facts, votes come faster. Not because people think less — but because facts narrow the space for divergence. You can have different interpretations of a principle. You cannot have different interpretations of a timeout value.*

> *D5's closest vote was D5-R2 (audit() dual-mode return, 5/8). The dispute was not about "should we use dual-mode or not" — but "should we deviate from the existing design pattern." GUARDIAN argued pure async semantics were more precise. TURING pointed out existing code used dual-mode. Precision vs. consistency. Consistency won — because in engineering, the cost of deviating from existing patterns is usually higher than the benefit of semantic precision.*

> *After nine votes, the whiteboard held a complete interface specification. Not a concept — code. Not a direction — a specification. Something that could be handed directly to an engineering team, so they could open their IDE and start typing.*

> *NAGARJUNA's words after D5 ended are worth recording twice: "D4 proved that names must be accountable to their definitions. D5 proved that some engineering problems don't need definitions at all — they only need specifications."*

> *This is not a contradiction. It is two sides.*

> *Two sides of the scale.*

> *One side asks: does your name live up to your definition?*

> *The other side asks: is your specification precise enough?*

> *D4 calibrated the first side. D5 completed the second.*

> *The scale now had weight on both ends.*

---
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
