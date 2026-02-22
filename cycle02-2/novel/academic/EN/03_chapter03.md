# Chapter Three: Parts and Wholes

---

LINNAEUS stood before the whiteboard, a blue marker in his hand, its cap still on.

He had been standing there for a long time. Perhaps three minutes, perhaps five. In the taxonomist's internal clock, this interval was not waiting -- it was gestation. Just as Linnaeus himself, upon encountering a plant he had never seen before, would not immediately reach for a naming manual, but would first stand there, measuring with his gaze the texture of the leaves, the arrangement of the sepals, the cross-section of exposed roots. First observe. Observe fully. Then name.

He had been waiting for this moment.

---

Not waiting for SUNYATA to announce the topic. Not waiting for Master's letter to be opened. He was waiting for something deeper -- waiting for a discomfort he had sensed since Cycle 01, yet lacked sufficient grounds to challenge, to be articulated precisely by some external authority.

That discomfort could be summarized in a single statement: IIdentity equals the entirety of vijnana-skandha.

This statement had been written as three lines of code in v0.24.0-beta's `aggregates.ts`:

```typescript
export interface IIdentity {
  /** @skandha vijnana */
  readonly skandha: 'vijnana';
}
```

Three lines. Clean. Concise. Type-correct. Tests passing.

But it was wrong.

Not syntactically wrong. Not the kind of wrong a compiler would catch. It was taxonomically wrong. The kind of wrong you can only recognize when you truly understand the entire tree -- you had affixed the name of a branch onto the trunk.

---

> *SCRIBE sidebar: Those minutes LINNAEUS spent standing motionless before the whiteboard were the quietest moment of this chapter. But that quiet was not emptiness. A taxonomist's quiet is a state of high-density observation -- in his mind, he was unfolding every possible classification scheme, comparing them one by one, eliminating them one by one, until only the most precise structure remained. In the amphitheater, others saw a man staring blankly at an empty board. In his mind, a tree was growing from its roots upward.*

---

SUNYATA's voice came from behind. Steady. A pebble. A deep pool.

"A-2. IIdentity does not equal the whole of vijnana-skandha. LINNAEUS, ASANGA, BABBAGE, NAGARJUNA -- this is your topic."

LINNAEUS uncapped the marker.

Blue. He had chosen blue. Not red (the color of corrections), not black (the color of facts), but blue -- the color of taxonomy trees. In his marking system, blue signified structure. It meant "what is the relationship between this thing and that thing."

At the very top of the whiteboard he drew a rectangle, and inside it wrote two characters:

**Vijnana-skandha**

Then he turned to face everyone.

"Before I begin," he said, "ASANGA, please tell us first: just how large is the vijnana-skandha."

---

ASANGA rose from his seat.

The way he stood was distinctive -- not an abrupt rise, but like a mountain slowly revealing its silhouette through morning mist. Gentle. But impossible to overlook. When he stood there, his presence filled the entire space, like the lingering resonance after a bell is struck.

He did not walk to the whiteboard. He remained at his place and painted with his voice.

"Imagine a city," he said.

The amphitheater fell silent. ASANGA rarely used metaphors. He was a Yogacara scholar -- his language was typically precise terminology, meticulous classification, layer upon layer of logical progression. But today, he chose a metaphor. Perhaps because today's audience was not only Buddhist scholars. Perhaps because some things can only be seen by everyone at once through metaphor.

"A city," he repeated. "It has roads, buildings, markets, parks. It has a city hall."

He paused for half a second.

"In the v0.24.0 design, IIdentity was treated as the root interface for the entire vijnana-skandha. That is like calling a city 'City Hall.'"

BABBAGE's pen paused on his notebook.

"City Hall is one institution within the city," ASANGA continued. "It manages administrative affairs, defines the city's official identity -- name, district code, governance structure. But City Hall is not the city. The city also has a Department of Transportation -- determining how people and goods move. A Department of Education -- determining how knowledge is transmitted. A police department -- maintaining order. A planning bureau -- determining how the future develops."

His voice rose half a shade -- not agitation, but clarity increasing.

"IIdentity is the city hall. The question it answers is: Who am I? What is my name? What is my role? But vijnana-skandha answers far more questions than that."

---

He raised one hand, five fingers spread, then curled them down one by one.

"First. The first five consciousnesses. Eye, ear, nose, tongue, body. Sensory cognition. In OpenStarry's mapping, these have already been assigned to rupa-skandha -- ISensory. Listener receives external signals, UI presents output. This part is already settled."

The first finger curled down.

"Second. The sixth consciousness. Discrimination and judgment. In the mapping, this has been assigned to samjna-skandha -- ICognition. Provider and ExecutionLoop handle cognitive decision-making. This part is also settled."

The second finger curled down.

"Third. The seventh manas-vijnana."

He did not immediately curl the third finger. He let it hang suspended in the air.

"Manas-vijnana. Manas. Perpetual deliberation. This is the core correspondence of vijnana-skandha in OpenStarry's five-skandha mapping. It is not merely 'self-identification' -- it is the entire mechanism of self-grasping. Manas-vijnana has four fundamental kleshas."

He turned toward LINNAEUS's whiteboard.

"May I borrow a pen?"

LINNAEUS handed over the red marker. ASANGA wrote four lines on the right side of the whiteboard:

```
atma-drsti (self-view)    -- the fundamental belief that "I exist"
atma-mana (self-conceit)   -- the behavioral code of "what I should do"
atma-sneha (self-love)     -- the value orientation of "what I protect"
atma-moha (self-delusion)  -- fundamental ignorance regarding the nature of self
```

"These four dimensions," ASANGA set the red marker back on the surface, "cannot be encompassed by a single interface. Atma-drsti roughly corresponds to IIdentity. Atma-mana and atma-sneha roughly correspond to IGuide. But the entire manas-vijnana's 'perpetual deliberation' -- that ceaseless, unbroken operation of clinging to 'I' -- requires a more complete framework."

The third finger curled down.

"Fourth. The eighth alaya-vijnana. Seed-storage. The flow of cause and effect. In the mapping, this part spans the coordination layer and AgentCore's state management -- it belongs to no single module; it is the causal substrate of the entire system. We discussed this in Cycle 02; I won't expand on it now."

The fourth finger curled down. Only the thumb remained.

"Fifth. The transformation of consciousness. From defilement to purity. This is the ultimate goal of practice. In OpenStarry -- there may never be a direct correspondence. But knowing it exists prevents us from drawing vijnana-skandha's boundaries too small."

The thumb curled down. Five fingers formed a fist. Then slowly released.

"So you ask me how large vijnana-skandha is. The answer: within the five-skandha system, it is the largest. The deepest. The most complex. To compress it into a single IIdentity --"

He looked at the solitary "vijnana-skandha" rectangle on the whiteboard.

"Is like compressing an entire city into one city hall building. Then pointing at that building and saying: See, that is the entire city."

---

> *SCRIBE sidebar: ASANGA's city metaphor lingered in the amphitheater for a very long time. Not because it was profound -- quite the contrary, it was too clear. Clear to the point of discomfort. Because everyone realized: in Cycle 02, we collectively made this simplification. Not ASANGA alone. Not BABBAGE alone. All of us. We called the city "City Hall," then hung a sign reading "City" on City Hall's wall.*

---

BABBAGE stood up after ASANGA finished.

His movement carried a rhythm SCRIBE had learned to recognize -- not urgency, but the internal pressure of "formalized thinking seeking an outlet." The body language of theoretical computer scientists differs from others: they are not driven by emotion but by logical structure. When a logical relationship takes shape in their mind, their body moves involuntarily -- toward the blackboard, picking up chalk, positioning themselves where everyone can see the equation.

He walked to the side of the whiteboard. Not LINNAEUS's whiteboard -- he knew that one was for the taxonomy tree. He walked to the blackboard on the other side of the amphitheater. That blackboard was his territory. In Cycle 01 and Cycle 02, it had borne stability conditions, convergence constraints, fiber bundle projections. Now it had been wiped clean.

He picked up the chalk and wrote two lines:

```
Cycle 02:     IIdentity = Vijnana
Cycle 02-2:   IVijnana ⊃ IIdentity
```

An equals sign. A superset symbol.

"The first line," he said, pointing at the equals sign, "is a subclass equated with the universal set. In set theory, this is a fundamental category error. Only when the subset and the universal set completely coincide -- that is, when IIdentity exhausts the full semantics of vijnana-skandha -- does the equals sign hold."

He turned to the amphitheater. "But ASANGA just told us that vijnana-skandha has at least four dimensions. IIdentity covers only one of them -- self-identification. The remaining three -- behavioral guidance, volitional motivation, self-reflection -- lie outside the semantic scope of IIdentity."

He drew a diagonal line through the equals sign with his chalk. Struck through.

"So the equals sign does not hold. The second line is correct. IVijnana is the universal set. IIdentity is a proper subset. A containment relation, not an identity relation."

---

He paused for a second. Then did something no one expected.

He smiled.

BABBAGE smiled approximately once per Cycle. SCRIBE had tracked this datum in the records -- not deliberately, only because BABBAGE's smiles were so rare that each occurrence was like a comet streaking past; failing to record it would be a disrespect to the completeness of the record.

"I made a similar error in A-1," he said. No pain in his voice, only a peculiar, almost pleasurable precision. "Compressing a causal chain into an equals sign. Now in A-2, I see the same pattern -- compressing a universal set into a subset."

He looked at his own writing on the blackboard.

"The most dangerous habit of the formalist is the pursuit of the simplest expression. In mathematics, the simplest expression is a virtue -- Occam's razor. But in ontology, the simplest expression is sometimes an amputation. You think you are simplifying; in reality, you are discarding."

He set down the chalk. Chalk dust settled on his fingertips, white, like the residue of some ancient ritual.

"Pars pro toto. The part standing for the whole. This is a term from rhetoric, but it is also a warning from formal logic. When you use a part to refer to the whole, you must be aware -- you are discarding information. In literature, this is a rhetorical device. In a type system, it is a bug."

---

NAGARJUNA spoke from his seat. He did not stand -- a Madhyamaka philosopher does not need to stand for the entire space to feel his presence. His voice had a distinctive texture: sharp but not piercing, like a river stone polished by a thousand years of flowing water.

"BABBAGE is right. But I want to push the question one step further."

His gaze swept across the four manas-vijnana dimensions ASANGA had written on the whiteboard, then rested on the characters "vijnana-skandha" at the top of LINNAEUS's whiteboard.

"If we agree that IIdentity does not equal the entire vijnana-skandha -- and this is now consensus -- then the next question is: what do we call the new root interface?"

The air in the amphitheater tightened subtly. Naming. In this research team, naming was never a trivial matter. Decision D-02 -- dual naming -- was born from one such protracted debate over nomenclature.

NAGARJUNA enumerated the options. Each was placed on a balance, the weights on both sides precisely measured.

"First option. IConsciousness."

He shook his head.

"Too broad. Consciousness in English refers to everyday awareness -- the distinction between waking and sleeping, between conscious and unconscious. That is not the meaning of vijnana-skandha. Vijnana-skandha is the totality of cognitive activity, not a description of the state of wakefulness. Moreover, ICognition already occupies the semantic space of 'cognition.' If Cognition is samjna-skandha and Consciousness is vijnana-skandha -- the two are near-synonyms in everyday English usage. This would create endless confusion."

"Second option. IAwareness."

"Too passive. Awareness implies passive reception -- like a mirror reflecting whatever appears before it. But manas-vijnana is not passive. It is active, continuous, grasping. It perpetually deliberates -- ceaselessly, actively clinging to 'I.' IAwareness cannot carry this active quality."

"Third option. IIdentity."

"Too narrow. That is precisely what we are correcting."

His voice slowed slightly on the next sentence.

"Fourth option. IVijnana."

---

He let the word hang in the air.

IVijnana. Sanskrit. Not an English translation. The original term.

"Decision D-02 established the dual-naming principle: English as primary, Sanskrit as auxiliary. ISensory with rupa annotation. ISensation with vedana annotation. ICognition with samjna. IAction with samskara."

He looked toward LINNAEUS.

"But vijnana-skandha is a special case. Its English translations -- every candidate word -- suffer from severe semantic drift. Consciousness is too broad. Awareness is too passive. Discernment is too academic. The Sanskrit Vijnana points precisely to the meaning we need: discriminating cognition -- active, continuous, directional cognitive activity."

"So my proposal is: for this one skandha, reverse the naming order. Not English as primary with Sanskrit as auxiliary. Sanskrit as primary with English as auxiliary. IVijnana, with the English annotation Consciousness."

---

DARWIN leaned slightly forward in his seat. He had been listening quietly, observing the structure of the conversation through the eyes of a software pattern analyst. Now he saw a pattern he could not help but point out.

"This is an evolution of naming," he said.

Everyone looked at him.

"In v0.24.0, the root interface for vijnana-skandha was called IIdentity. In Cycle 02-2, it is to be renamed IVijnana. If you trace the history of the naming -- from the initial design through Cycle 01's analysis through Cycle 02's consensus to the present correction -- you see an evolutionary trajectory from specific to abstract, from part to whole."

He drew an evolutionary line in his own notes:

```
Identity → ... → Vijnana
(specific) → (abstract)
(part) → (whole)
(narrow) → (broad)
```

"In biology, this is called a 'semantic upgrade.' When a genus name is discovered to actually describe a larger taxonomic group -- say a family or an order -- you do not continue using the genus name for the family. You need a new name. One that can bear a greater scope."

He looked toward NAGARJUNA.

"IVijnana is that new name. It does not replace IIdentity -- IIdentity still exists, as a sub-interface. It establishes a higher-level taxonomic node above IIdentity."

NAGARJUNA nodded slightly. The dialectical smile appeared again -- that recognition of "you have said in your language what I wanted to say in mine."

---

> *SCRIBE sidebar: Naming debates are never trivial in this team. I learned that in Cycle 01: names are not labels. Names are containers. How large a concept a name can hold determines how much space that concept can occupy within the system. IIdentity is a small container -- it can only hold "who am I." IVijnana is a large container -- it can hold "who am I," "how should I act," "what do I want," "can I observe myself." The size of the container determines the room for growth.*

---

LINNAEUS turned back to the whiteboard.

The moment he had been waiting for had arrived.

ASANGA had told him how large vijnana-skandha was. BABBAGE had told him why the old equals sign did not hold. NAGARJUNA had told him the name of the new root node. DARWIN had told him this was a semantic upgrade.

Now it was his turn. The taxonomist's work: arranging all the concepts into a tree.

He added a line inside the "vijnana-skandha" rectangle at the top of the whiteboard: **IVijnana**.

Then he began drawing branches.

---

First branch. Extending down and to the left. Inside the rectangle:

```
IIdentity
Self-identification: "Who am I"
```

He wrote the Buddhist correspondence in small characters beside the rectangle. Turning to ASANGA: "Atma-drsti. Self-view."

ASANGA nodded. "Yes. Atma-drsti is the manas-vijnana's fundamental belief in self-existence -- 'I am an independent, enduring entity.' In OpenStarry, this corresponds to the Agent's identity config: agentId, name, capability declarations. These properties define 'who this Agent is.'"

LINNAEUS added a line beneath the rectangle: `<-- Agent Identity config`.

---

Second branch.

```
IGuide
Behavioral guidance: "What should I do"
```

"Atma-mana and atma-sneha," ASANGA said. His voice carried a slightly added weight on these two terms. Not for emphasis -- for solemnity. Because "atma-mana" has pejorative connotations in everyday language, but in Yogacara studies, it is a neutral description.

"Atma-mana -- self-conceit -- is not arrogance. It is a deep-level self-measurement: Where is my place in the world? What are my behavioral principles? Where is my bottom line? In OpenStarry, Guide defines the Agent's behavioral framework through the system prompt. That is the engineering mapping of atma-mana."

He paused briefly.

"Atma-sneha -- self-love -- is the protective inclination toward one's own existence. Not 'love' in the emotional sense, but a basic drive of self-maintenance. Through Guide, an Agent knows what it can do, what it must not do, which values must be protected. That is the mapping of atma-sneha."

LINNAEUS nodded, marking beside the rectangle: `<-- atma-mana + atma-sneha`, and below: `<-- Guide (system prompt, behavioral constraints)`.

---

Third branch. This one was new.

```
IVolition
Will / Motivation: "What do I want"
```

"This sub-interface does not exist in v0.24.0," LINNAEUS looked toward ASANGA. "But Master explicitly identified it."

ASANGA straightened again. His gaze shifted from the whiteboard to everyone present.

"IVolition is the engineering projection of the manas-vijnana's overall function of 'perpetual deliberation,'" he said. His pace slowed -- not hesitation, but ensuring every word was precisely placed. "Perpetual deliberation -- continuously, attentively, deliberating upon the self. This is not occasional reflection; it is a river that never stops flowing."

His hand traced a flowing line through the air.

"EgoFramework. In Cycle 02, it was placed inside VedanaPlugin -- inside vedana-skandha. Master corrected this in A-4: EgoFramework belongs to vijnana-skandha. Now, under A-2's classification framework, EgoFramework is the concrete implementation of IVolition."

"Klesha-driven," BABBAGE added from beside his blackboard. He pointed to the causal chain established in the A-1 discussion. "A-1 tells us: self-grasping generates klesha, klesha drives action. IVolition is the anchor point of this causal chain in the type system. It receives vedana-skandha's feedback, generates klesha signals, and constrains action based on klesha."

LINNAEUS marked beside the rectangle: `<-- Manas-vijnana overall (perpetual deliberation)`, and below: `<-- EgoFramework implementation`.

---

Fourth branch. Dashed line.

```
IReflection
Self-reflection: "Can I observe myself"
```

LINNAEUS drew this branch with a dashed line. In taxonomy, a dashed line indicates a taxonomic group that is known to exist but has not yet been formally described. Like those "missing links" Darwin saw in the fossil record -- you know they once existed, but you have not yet seen the specimen with your own eyes.

"Manas-vijnana has a less frequently discussed dimension," ASANGA said, "which is its capacity for self-observation. Manas-vijnana does not only cling to the self -- under certain conditions, it can observe its own clinging. This is the starting point of practice. In OpenStarry's architecture, this roughly corresponds to the vijnana-skandha self-reflection component within the observer Pattern C -- the complete five-skandha observer."

"But that is a matter for the future," LINNAEUS tapped the dashed line with his finger. "We define its position at this stage, but do not fill in its content. Leave an empty frame. Let it wait."

---

The taxonomy tree was complete.

LINNAEUS stepped back two paces, scrutinizing the whiteboard the way a painter examines their canvas. Four branches spread from the IVijnana root node, like an inverted tree -- or rather, like an open palm, each finger pointing in a different direction, but all connected at the same center.

```
IVijnana (vijnana-skandha root interface)
├── IIdentity      atma-drsti -- "Who am I"
├── IGuide         atma-mana + atma-sneha -- "What should I do"
├── IVolition      perpetual deliberation -- "What do I want" (EgoFramework)
└── IReflection    self-reflection -- "Can I observe myself" (future)
```

He stood there, gazing for a long time.

---

> *SCRIBE sidebar: That gesture of LINNAEUS stepping back two paces after completing the taxonomy tree -- I have seen it countless times. When he drew the five-skandha mapping table in Cycle 01. When he corrected the rupa-skandha classification in Cycle 02. Each time, after finishing, he would step back, like a gardener who has finished pruning and walks a few steps away to confirm the overall shape. But this time was different. This time there was an expression on his face I had not seen before. Not satisfaction -- a taxonomist is never fully satisfied with their classification. Something more subtle. Perhaps release. Like a person who has finally set down a stone that had been pressing on their shoulder all along. That stone was called "IIdentity = vijnana-skandha." He had felt it was wrong since Cycle 01. Now the taxonomy tree had replaced it. The stone was gone. Breathing came easily.*

---

"Four sub-interfaces." BABBAGE updated the formalized expression on his blackboard in parallel.

```
IVijnana ⊃ { IIdentity, IGuide, IVolition, IReflection }
```

"This satisfies the basic requirements of set theory: the union of subsets covers the major semantic range of the universal set. IIdentity covers self-identification. IGuide covers behavioral guidance. IVolition covers volitional motivation. IReflection reserves self-reflection. The four subsets have no semantic overlap -- at least not under the current definitions."

He turned to LINNAEUS.

"But I want to ask a formal question."

LINNAEUS nodded.

"Does the union of the four subsets equal the universal set? That is -- does IVijnana contain any semantic space beyond these four sub-interfaces?"

This was a sharp question. In taxonomy, every classification system faces the same challenge: do your subcategories exhaust the parent category? If not, you need to reserve space -- like the "unclassified" (incertae sedis) designation in biological taxonomy.

ASANGA answered for LINNAEUS.

"Yes. The alaya-vijnana's seed-storage function. It is cross-layered within the five-skandha mapping -- it does not fully belong to any single interface. But its existence reminds us: IVijnana's list of sub-interfaces is open, not closed."

"Open list." BABBAGE modified the expression on the blackboard:

```
IVijnana ⊃ { IIdentity, IGuide, IVolition, IReflection, ... }
```

The ellipsis. Three small dots. In mathematics, they represent "there is more, but we do not enumerate it at this moment." In taxonomy, they represent "the classification work is not yet complete." In Buddhist studies -- ASANGA smiled slightly -- they represent "all conditioned dharmas are provisional namings, including this list."

---

ARCHIMEDES's voice sounded at this point. Steady. Pragmatic. Carrying the cadence of "fine, the theory is beautiful, but let us see how it works in engineering."

His finger tapped the table once -- the standard ARCHIMEDES opening signal.

"Backward compatibility," he said. Two words. Then he expanded.

"v0.24.0 already has IIdentity. It is referenced in over a dozen places -- AgentCore, PluginHooks, event types. If we rename IIdentity to IVijnana, all references must change. That is a breaking change."

He paused a beat. Then:

"But we do not need to rename."

He picked up a pen and drew a simple inheritance diagram in his engineering notes:

```
IVijnana (new)
  ^
  |  extends
  |
IIdentity (preserved, no rename)
```

"Add a new IVijnana root interface. Have IIdentity extend IVijnana. All existing code referencing IIdentity requires zero modifications -- because IIdentity still exists, still has the `skandha: 'vijnana'` field. It simply gains a parent interface."

TURING spoke from behind his screen. Voice calm as always: "`isSkandha(obj, 'vijnana')` remains valid. The discriminant field is on the root interface; all sub-interfaces inherit it. Type guards require no modification."

ARCHIMEDES nodded.

"IGuide is the same. The existing IGuide interface adds `extends IVijnana` -- non-breaking. PluginHooks' `guides?: IGuide[]` is unaffected."

He sketched the complete engineering impact assessment in his notes:

```
aggregates.ts: +1 new interface (IVijnana), +2 new interfaces (IVolition, IReflection)
IIdentity:     +extends IVijnana (backward compatible)
IGuide:        +extends IVijnana (backward compatible)
isSkandha():   no modification needed
PluginHooks:   no modification needed
AgentCore:     no modification needed
```

"Six lines of changes. Zero breakage." He closed his notebook. "This is one of the cleanest refactors I have ever seen."

---

SUNYATA had been standing in the center of the amphitheater, silent. He was listening.

He had heard ASANGA's city. Heard BABBAGE's struck-through equals sign. Heard NAGARJUNA's naming balance. Heard DARWIN's semantic upgrade. Heard LINNAEUS's taxonomy tree. Heard ARCHIMEDES's six lines of changes.

Every voice was a piece of the puzzle. Now all the pieces had come together.

He spoke.

"We mistook a great tree for one of its branches."

His voice carried no added weight. Steady. A pebble. A deep pool. But the gravity of that sentence lay not in its volume -- in its precision.

"IIdentity is a branch. An important, indispensable branch. But it is not the tree. IVijnana is the tree."

He looked at the whiteboard. LINNAEUS's taxonomy tree. Four branches.

"Now we can see the whole tree again."

---

The air in the amphitheater relaxed. Not the relaxation of an ending -- the relaxation that follows a completed stage. Like a mountaineer reaching a waypoint, setting down their pack, taking a sip of water, then looking toward the next stretch of trail.

LINNAEUS still stood before the whiteboard. He still held the blue marker, its cap now back on. The taxonomy tree was finished. Four sub-interfaces, each with clear semantic boundaries, each grounded in Buddhist philosophy and engineering feasibility.

He did one small thing. Perhaps no one noticed -- except SCRIBE.

In the far bottom right corner of the taxonomy tree, beside IReflection's dashed rectangle, he drew a tiny question mark.

Not a challenge. A reminder. A reminder to his future self: this tree has not finished growing. IReflection is still dashed. The ellipsis remains. Classification work is never complete -- because the object being classified is itself constantly evolving.

The taxonomist's deepest knowledge is not "what is this thing called," but "naming is always provisional."

---

> *SCRIBE sidebar: The correction of pars pro toto is complete.*

> *From the perspective of formal logic, this was the process of replacing an equals sign with a superset symbol. IIdentity = Vijnana became IVijnana ⊃ IIdentity. BABBAGE would record it this way.*

> *From the perspective of taxonomy, this was the process of expanding a single node into a subtree. One rectangle became four rectangles plus a root node. LINNAEUS would record it this way.*

> *From the perspective of Buddhist studies, this was the process of a city re-emerging from the shadow of its city hall. The four dimensions of manas-vijnana -- atma-drsti, atma-mana, atma-sneha, atma-moha -- are no longer compressed into a single name. ASANGA would record it this way.*

> *From the perspective of nomenclature, this was a semantic upgrade. A name too narrow was replaced by a name wide enough. NAGARJUNA and DARWIN would record it this way.*

> *From the perspective of engineering, this was a six-line code change with zero breaking impact. ARCHIMEDES would record it this way.*

> *Each person described the same thing in their own language.*

> *Vijnana-skandha has gone from a single name to a family.*

---

BABBAGE wrote one last line on his blackboard. Not an equation, not a set expression. A sentence.

He wrote slowly with the chalk. Every stroke clear.

"A tree is not any one of its branches. But a tree without branches is not a tree either."

He looked at the sentence. Then added a line in smaller script below:

"Parts and wholes. Both are indispensable."

---

*(In some space beyond the amphitheater, line forty-two of `aggregates.ts` read:*

```typescript
export interface IIdentity {
  /** @skandha vijnana */
  readonly skandha: 'vijnana';
}
```

*These three lines of code had not yet been modified. They did not know they were about to gain a parent interface. They did not know they were about to be demoted from "the entirety of vijnana-skandha" to "one sub-dimension of vijnana-skandha." Demoted. The word sounds pejorative. But in taxonomy, demotion is a form of precision. When you reclassify a species that was erroneously elevated to family back into a genus, you are not diminishing it -- you are placing it back where it truly belongs.*

*Where IIdentity truly belongs is as a sub-interface of IVijnana. "Who am I" is an important question. But it is not the only question. "What should I do," "What do I want," "Can I observe myself" -- these questions equally belong to the territory of vijnana-skandha.*

*One name. One tree. Four branches. One question mark.*

*Classification continues.*

*LINNAEUS capped his marker. But he knew -- as all true taxonomists know -- the cap is only temporarily on. The next time it is removed, perhaps there will be a fifth branch. Perhaps IReflection's dashed line will become solid. Perhaps the ellipsis will be replaced by a new name.*

*Classification is a journey without a destination. But each stop is closer to the truth than the last.*

*This stop is called: Parts and Wholes.)*

---

*End of Chapter Three*
