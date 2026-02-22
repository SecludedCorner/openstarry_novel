# Chapter Five: Four Rulings

---

ARCHIMEDES straightened up.

Through the three preceding chapters of philosophical discussion, he had been leaning forward with restraint, like an architect carrying a toolbox seated in the audience, waiting for the philosophers to finish debating the direction of the foundation.

That waiting was over.

---

SUNYATA held a new agenda sheet -- a thin page, four lines.

"A-class corrections took three chapters -- telling us what is right. Now we enter B-class. Master's rulings on four engineering questions. From philosophy to engineering."

---

ARCHIMEDES tapped the table once. "I've been waiting for this moment."

A few low laughs. Everyone knew his state during the A-class discussions: the man with the toolbox, sitting among philosophers debating aesthetics.

SUNYATA nodded. "B-1. VedanaPlugin is optional, and the five-skandha completeness check."

---

> *SCRIBE's narration: B-class's rhythm is completely different from A-class. A-class was contemplative -- each topic needed time to ferment. B-class is about decisions. Master has already ruled; our task is to translate rulings into designs. ARCHIMEDES waited three chapters; now it was his turn.*

---

SUNYATA read Master's exact words: "'An Agent should be able to start as long as it is complete. But there should also be a developer mode, where an Agent can start even if incomplete, but with a reminder.'"

"Three keywords. Optional. Complete. Reminder."

KERNEL's hand reached for his stack of analogy cards. He flipped two -- no -- flipped another -- pulled out the fourth. He was waiting for a match.

"Linux kernel boot," he said, standing up. He walked to the center of the theater without using the projector. He used cards and his voice.

"POST -- Power-On Self-Test. When a computer starts up, the kernel checks hardware one by one. CPU. Memory. Disk controller. Graphics card. Network card. Sound card. One by one, from most critical to least important."

He flipped through the cards.

"No CPU -- completely unable to start, hard dependency. No memory -- same, hard dependency."

"But no graphics card? OK, boot into text mode. The system is alive, just without graphics. No network card? Offline mode. No sound card? Silent mode. Everything's fine."

He lined up three cards in a row.

"The difference between hard dependencies and soft dependencies. The five skandhas are like these hardware components."

---

ARCHIMEDES was already drawing. KERNEL hadn't finished, but an interface skeleton had already appeared in his engineering notes:

```
SkandhaCompletenessReport
+-- rupa:    { present: boolean, components: string[] }
+-- vedana:  { present: boolean, components: string[] }
+-- samjna:  { present: boolean, components: string[] }
+-- samskara:{ present: boolean, components: string[] }
+-- vijnana: { present: boolean, components: string[] }
+-- isComplete: boolean
+-- missing:   string[]
```

"SkandhaCompletenessReport. Five-skandha completeness report." His voice was pragmatic and clear. "Five skandhas, one field each. Present or not. What's missing. That's your hardware check -- except instead of checking the CPU, you're checking rupa-skandha and vijnana-skandha."

KERNEL wrote a line on the right side of a blank card -- left side: `POST`, right side: `SkandhaCompletenessReport`. Match complete.

---

TURING's screen lit up. A skeleton of code -- his style: skeleton first, flesh later.

```typescript
async start(options?: { developerMode?: boolean }): Promise<void> {
  const report = this.checkSkandhaCompleteness();
  if (!report.isComplete) {
    if (options?.developerMode) {
      logger.warn(`[DEV MODE] Agent five-skandha incomplete: missing ${report.missing.join(', ')}`);
    } else {
      throw new Error(`Agent five-skandha incomplete: missing ${report.missing.join(', ')}`);
    }
  }
}
```

"AgentCore.start()." TURING said. "developerMode flag. When incomplete, developer mode warns but continues. Production mode throws an error."

DARWIN leaned forward slightly. "Developer mode is a kind of evolutionary intermediate state -- like an insect between nymph and adult. A nymph can move, eat, and sense its environment, but it lacks wings. Incomplete, but viable."

KERNEL added a small note in the blank space of a card: `text mode = nymph = developerMode`.

---

> *SCRIBE's narration: B-1's discussion was shorter than any single A-class item. Not because it was unimportant -- but Master's ruling was clear enough, KERNEL's analogy vivid enough, ARCHIMEDES' design direct enough. One interface. Five fields. One flag. Quick and clean.*

---

## II

SUNYATA turned to the second line of the agenda.

"B-2. Tenet #6 rewrite."

He read Master's ruling: "'This absolutely must be rewritten, but please wait until this round of discussion is complete before deciding how to write it.'"

Silence. This was the shortest of the four rulings. And it would be the shortest discussion.

NAGARJUNA spoke from his seat. He didn't stand. A Madhyamaka philosopher doesn't need to stand when speaking briefly -- the power of brief words lies not in volume but in precision. Like a needle. A needle doesn't need to be large. It just needs to be sharp.

"First get the causes right, and the effect will naturally emerge."

Eight words.

"Tenet #6 is the effect. A-class corrections are part of the cause, C-class discussions are another part. If we write #6 now, we're defining the effect while the cause is incomplete. This violates the basic order of causality."

"Wait until A-class and C-class are all confirmed. Then #6's text will write itself. We won't be writing it -- it will naturally emerge from the complete cause."

BABBAGE wrote one line in his notebook. Very short: "B-2: Wait. Causal order."

SUNYATA marked the second line of the agenda: **Not yet finalized.**

---

He turned to the third line. "B-3. Vedana-skandha independent event stream. Option c."

---

HERACLITUS moved. His entire body shifted from scattered stillness to intense focus. Flow. Event stream. This was his word.

---

> *SCRIBE's narration: HERACLITUS had barely spoken in the first three chapters. Not because it was irrelevant -- "everything flows," so everything is relevant to him. But A-class topics were static: names, placement, classification. Those are frozen moments. His specialty is flow. Now the topic had come to "event stream" -- the river itself -- and his entire body awakened.*

---

SUNYATA read Master's ruling.

"'Choose the independent event stream. Vedana-skandha is completely equal to the other skandhas -- with its own type file, its own event namespace, its own PluginHooks slots.'"

HERACLITUS stood up.

The way he stood was different from everyone else. ASANGA stands like a mountain emerging through fog. BABBAGE stands like a logical structure finding its exit. HERACLITUS stands like a whirlpool breaking through the water's surface -- sudden, spinning, with unpredictable energy.

"Vedana-skandha has always been there," he said. His voice had a peculiar texture -- not the precision of academia, not the pragmatism of engineering. Something older. Like a person who has lived by a river their whole life describing the river.

"It has always been there." He repeated. "From v0.14.0 to v0.20.0 to v0.22.1 to v0.24.0. Every version had events. Every version's EventBus was sending signals -- tool results, provider responses, listener inputs. But these events all belonged to other skandhas. Rupa-skandha's events. Samjna-skandha's events. Samskara-skandha's events."

He took a few steps around the center of the theater. Not pacing -- flowing.

"And vedana-skandha? Where were vedana-skandha's feelings -- dukkha, sukha, upekkha -- hiding?"

"Hidden in metadata." TURING answered. "Option b was to attach vedana-skandha's assessment results in the metadata field of existing events. Hitchhiking."

"Hitchhiking." HERACLITUS seized the word. "Vedana-skandha's water was mixed into someone else's river. You knew it was there, but you couldn't see it. Because it didn't have its own riverbed."

He stopped. "Option c gives it its own riverbed."

---

He drew two lines in the air with his hands.

"Option b is an underground river -- vedana-skandha's data hidden in metadata, like groundwater seeping into the sediment of surface rivers. Option c brings the underground river to the surface. vedana:assessment, vedana:dukkha_spike -- its own type file, its own namespace."

"A river rising from underground to the surface."

---

WIENER listed seven event types on his grid paper, checking each one:

```
vedana:assessment          <- three-feeling composite assessment   check
vedana:dukkha_spike        <- dukkha spike                        check
vedana:sukha_peak          <- sukha peak                          check
vedana:upekkha_equilibrium <- upekkha equilibrium                 check
vedana:recommendation      <- vedana-skandha recommendation       check
vedana:sensor_update       <- raw sensor data                     check
vedana:reset               <- vedana-skandha reset                check
```

"Seven events. All three feelings covered. Perfectly consistent with Cycle 02's three-channel PID design." He looked at ARCHIMEDES. "Option c changes the communication method -- from hidden channel to open channel."

---

ARCHIMEDES calculated the impact:

```
New vedana-events.ts   -> new file, no impact
PluginHooks            -> +1 field (sensations?: ISensation[])
Other plugin type defs -> not affected
```

"Incremental cost is extremely low. Benefit: vedana-skandha goes from invisible to visible. Cost-benefit ratio is excellent."

NAGARJUNA added softly: "What is named begins to exist. What is unnamed, though present, cannot be seen. Option c didn't create vedana-skandha's events -- it gave a name to a flow that already existed."

---

> *SCRIBE's narration: HERACLITUS's river metaphor -- an underground river rising to the surface -- was the most vivid image of this chapter. It precisely describes the essential change from option b to option c: from hidden to visible, from unnamed to named.*

---

## III

SUNYATA turned to the last line. "B-4. Coordination layer as an independent daemon."

LEIBNIZ and MESH both leaned forward slightly. The multi-agent cooperation expert and the distributed systems researcher -- this was their topic.

Master's ruling: "'It must be an independent daemon -- an independent process. It must be arranged now. Changing it later will cost more.'"

---

Both stood up at the same time.

LEIBNIZ spoke first. "Master says 'must be arranged now.' This is not optional. In Cycle 02, we deferred the coordination layer. Build the house first, think about community planning later. But Master tells us: the plumbing -- water, electricity, communications -- needs to be laid during construction. Wait until the building is finished to add pipes, and you'll have to tear down walls."

---

MESH picked up seamlessly. The coordination between them was like a rehearsed routine -- but it wasn't. This was the natural handoff between experts who had worked in adjacent fields for a long time.

"Independent process means IPC." MESH's voice was low, carrying the characteristic caution of a distributed systems researcher. "Serialization. Message format. Heartbeat. Health checks. Timeout. Retry. A complete distributed systems problem."

He walked to the whiteboard and drew two blocks. Left: **CoordinationDaemon (independent process)**. Right: **AgentCore (independent process)**. Between them, a double-headed arrow labeled: **IPC**.

"The coordination layer and Agent Core are two independent processes. They communicate through serialized messages. Not function calls -- serialized messages."

---

LEIBNIZ wrote above the CoordinationDaemon: **Active Storage (neng-cang)**

"Cycle 02 mapped active storage -- alaya-vijnana's active storage function -- to the coordination layer. Now Master confirms it as an independent daemon."

In simple terms, active storage (an aspect of alaya-vijnana in Buddhism, referring to the function of actively storing all experiential seeds) corresponds to two engineering things: the Plugin registry -- knowing every plugin exists; and the Agent registry -- knowing all currently running Agents.

"Active storage is not an abstract Buddhist concept. It is a concrete engineering component -- with APIs, with state. Master says 'arrange it now' because these APIs determine Agent Core's interfaces. Change it later -- tear down walls."

---

GUARDIAN stood up -- first surveying the surroundings, confirming the environment, then acting. A security expert's body language always includes a threat assessment as a preceding step.

He walked to the whiteboard and drew a shield beside the CoordinationDaemon block -- its lines heavier than any block anyone else had drawn.

"The coordination layer isn't just a registry. The coordination layer is the enforcer of the commandments."

Beside the shield he listed four items: Plugin blacklist, trust levels (official / verified / community / unknown / blacklisted), quarantine/revocation/banning, CRL checks.

"In Cycle 02's sila-prajna safety framework, we designed two security layers -- sila is prevention, prajna is elimination. Enforcing sila requires an authority. In Buddhist monastic communities, the precepts are maintained and enforced by the senior monks. In OpenStarry, that senior monk is the coordination layer."

"Trust judgments cannot be made by the Agent itself -- because the Agent has ego-clinging." ASANGA shifted slightly in his seat. GUARDIAN had used the term "ego-clinging" -- in a security expert's context, ego-clinging is not just a philosophical issue; it's a security vulnerability.

He pointed to the IPC arrow. "Independent process means independent memory space. The Agent cannot directly modify the coordination layer's blacklist. LEIBNIZ and MESH are talking about plumbing. I'm talking about door locks. Both must be installed during construction."

---

> *SCRIBE's narration: GUARDIAN and NAGARJUNA's cross-disciplinary collaboration on the security framework was evident once again -- precepts need an enforcer, security needs an authority, and the coordination layer satisfies the needs of both Buddhism and engineering.*

---

ARCHIMEDES had been listening. Waiting for all the requirements, constraints, and security demands to be laid out on the table. Then he drew a timeline.

"Phased." One word. Then the expansion.

```
Phase 1: Design document -- architecture, interface definitions, IPC message format, security requirements
Phase 2: Skeleton -- daemon skeleton, basic IPC
Phase 3: Basic functionality -- Plugin registration/query, Agent health checks
Phase 4: Security -- sila engine, trust levels, blacklist
```

"Master says 'arrange' doesn't equal 'complete everything.' Arranging means establishing the architecture, interfaces, and IPC format. Laying the plumbing."

He wrote in large letters beside the timeline: **Interfaces first, implementation incremental.**

---

SUNYATA listened to the entire discussion. He let silence persist for a few seconds -- letting the four rulings settle.

"B-1. VedanaPlugin is optional, but the Agent needs a five-skandha completeness check. SkandhaCompletenessReport. Can start if incomplete -- developer mode. KERNEL's analogy: no graphics card, still runs text mode."

He looked at KERNEL. KERNEL patted his stack of cards.

"B-2. Tenet #6 must be rewritten. But wait until all corrections are complete before finalizing. NAGARJUNA's causality: first get the causes right, and the effect will naturally emerge."

NAGARJUNA didn't move. He didn't need to. Causal order doesn't need to be confirmed -- it is self-evident.

"B-3. Vedana-skandha gets an independent event stream. vedana-events.ts. Independent namespace. PluginHooks gains a new sensations slot. HERACLITUS's metaphor: a river rising from underground to the surface."

HERACLITUS smiled slightly. That smile held no pride -- only a quiet contentment, the feeling of "a flowing water has finally found its own riverbed." He returned to his seat, fluidly, without pause.

"B-4. Coordination layer as an independent daemon. LEIBNIZ and MESH's architecture. GUARDIAN's security. ARCHIMEDES' phased plan. Design document first, implementation incremental."

He set down the agenda sheet.

---

"A-class corrections told us -- what is right."

His voice was not raised. Steady as ever. Pebble. Deep pool.

"B-class rulings told us -- how to make it happen."

He looked around the room. ARCHIMEDES' pragmatism. KERNEL's analogies. HERACLITUS's river. LEIBNIZ and MESH's topology. GUARDIAN's shield. WIENER's checkmarks. DARWIN's nymph. NAGARJUNA's needle. BABBAGE's notes. TURING's skeleton. ASANGA's quiet.

"Next, we translate corrections and rulings into the complete five-skandha expansion design. C-class. From philosophy to engineering, then from engineering to architecture. Spiral ascent."

---

> *SCRIBE's narration: B-class took one chapter; A-class took three. Not because B-class was less important -- SkandhaCompletenessReport will become the first checkpoint for every Agent startup, vedana-events.ts will make vedana-skandha one of the most visible skandhas, and CoordinationDaemon will become the nerve center of the multi-agent ecosystem. B-class took one chapter because Master had already ruled. The language of design is denser and more precise than the language of debate.*

> *Twelve people each contributed a puzzle piece. A-class told us what is right. B-class told us how to make it happen. Next chapter -- C-class. Spiral ascent. Onward.*

---

*(Outside the theater, four design documents are taking shape.*

*The first is SkandhaCompletenessReport -- five booleans, one isComplete flag. Surprisingly simple. But KERNEL knows: simple doesn't mean unimportant. Simple means foundational.*

*The second is vedana-events.ts -- seven event types. HERACLITUS saw a new river on the surface.*

*The third is the CoordinationDaemon interface definition. GUARDIAN's shield is embedded in every Service's signature.*

*The fourth is blank. Tenet #6. Not yet finalized.*

*NAGARJUNA said: first get the causes right, and the effect will naturally emerge. The causes are still gathering. When all causes are assembled, #6's text will naturally emerge.*

*Just like a river doesn't need to be told where to flow. Once the terrain is set, the water naturally knows the way.)*

---

*End of Chapter Five*
