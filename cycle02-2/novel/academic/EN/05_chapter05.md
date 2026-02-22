# Chapter Five: Four Rulings

---

ARCHIMEDES sat up straight.

During the A-class discussions of the preceding three chapters, his spine had maintained a restrained angle: leaning forward fifteen degrees, fingers occasionally tapping the table, but in a converging rhythm, like an architect carrying a toolbox who had been seated in the audience, waiting for the philosophers to finish debating the orientation of the foundation.

That waiting was over.

---

SUNYATA held a new agenda sheet in his hands, a thin single page, four lines of text.

"The A-class corrections took three chapters," he said. His voice steady as always. A pebble. A deep pool. "From causal chains to vijnana-skandha subclasses, from observer separation to EgoFramework's proper assignment. Those were philosophical corrections -- telling us what is right."

"Now we enter the B-class. Master's rulings on our four engineering questions. This is the moment where philosophy turns into engineering."

---

ARCHIMEDES's finger tapped the table once -- crisp, carrying anticipation.

"I have been waiting for this moment for a long time," he said.

A few low chuckles rippled through the amphitheater. They all knew ARCHIMEDES's state during the A-class discussions: a man carrying a toolbox, seated among a group of philosophers debating the aesthetics of architecture.

SUNYATA nodded slightly. "B-1. VedanaPlugin is optional, and five-skandha completeness checking."

---

> *SCRIBE sidebar: The transition from A-class to B-class was like a symphony shifting from adagio to allegro. The rhythm of A-class discussions was contemplative -- ASANGA's city metaphor, BABBAGE's strikethroughs, NAGARJUNA's naming balance -- each topic needed time to ferment. B-class was different. The rhythm of B-class was decisional. Master had already ruled. Our task was not to debate right and wrong, but to translate rulings into designs. ARCHIMEDES had waited three chapters. Now it was his turn.*

---

SUNYATA read Master's original words.

"'Some plugins have already inherited this plugin. As stated above, an agent should be able to start as long as it is complete. But perhaps a developer mode or some other mode is needed. It should be optional -- the agent can start even if incomplete, but a warning is needed.'"

He set down the paper.

"Three keywords. Optional. Complete. Warning."

KERNEL's hand was already reaching for his stack of analogy cards. He flipped through two -- not right -- flipped one more -- pulled out the fourth. What was written on the left side, SCRIBE could not see clearly. The right side was blank. He was waiting for a match.

"Linux kernel boot," he said, standing up.

He walked to the center of the amphitheater. No projection used. He worked with cards and his voice.

"POST -- Power-On Self-Test. When a computer boots, the kernel checks hardware. CPU. Memory. Disk controller. Graphics card. Network card. Sound card. One by one, from most critical to least critical."

He flipped through the cards.

"No CPU -- completely unable to boot. Hard dependency. No memory -- likewise, hard dependency."

"But no graphics card? OK. Boot to text mode. The system is alive; it simply has no graphical display. No network card? OK. Offline mode. No sound card? OK. Silent mode. Everything normal."

He arranged three cards in a row.

"The distinction between hard dependencies and soft dependencies. The five skandhas are like these hardware components."

---

ARCHIMEDES was already drawing.

Before KERNEL had even finished, an embryonic interface appeared in his engineering notes. His pen speed was fast -- not sloppy, but a kind of shorthand trained over many years: recording only key types, key fields, key methods, omitting all decoration.

```
SkandhaCompletenessReport
├── rupa:    { present: boolean, components: string[] }
├── vedana:  { present: boolean, components: string[] }
├── samjna:  { present: boolean, components: string[] }
├── samskara:{ present: boolean, components: string[] }
├── vijnana: { present: boolean, components: string[] }
├── isComplete: boolean
└── missing:   string[]
```

He held up his notes.

"SkandhaCompletenessReport. Five-skandha completeness report." His voice was pragmatic, clear, every word like a brick. "Five skandhas, one field per skandha. Boolean -- present or absent. Component list -- if present, which ones. Two summary fields at the end: whether complete, what is missing."

He looked toward KERNEL.

"Your hardware check. POST. Except instead of checking CPU and memory, it checks rupa-skandha and vijnana-skandha."

---

KERNEL nodded. Then he did something -- he wrote a line on the right side of that blank card. SCRIBE could finally see the card's format: left side was "Operating System Concept," right side was "OpenStarry Mapping."

Left: `POST (Power-On Self-Test)`
Right: `SkandhaCompletenessReport`

He slipped the card back into his stack. Match complete.

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

"AgentCore.start()," TURING said. Voice calm as always. "developerMode flag. When incomplete, developer mode warns but continues. Production mode throws an error."

DARWIN leaned slightly forward. "Developer mode is an evolutionary intermediate state."

Several gazes turned toward him.

"Incomplete metamorphosis -- the transition of an insect from nymph to adult. The nymph can move, feed, sense its environment, but lacks wings. Incomplete, but viable. Developer mode is the nymph."

KERNEL added a line in small script on the blank space of his card: `text mode = nymph = developerMode`.

---

> *SCRIBE sidebar: B-1's discussion was shorter than any single item from the A-class. Not because it was unimportant -- but because Master's ruling was sufficiently clear, KERNEL's analogy sufficiently vivid, and ARCHIMEDES's design sufficiently direct. Philosophical discussion requires expansion -- you must illuminate a concept from multiple angles before you can see its full contours. Engineering discussion requires convergence -- you must select one option from among many possibilities, then transform it into type definitions and method signatures. B-1's convergence was swift and clean. SkandhaCompletenessReport. One interface. Five fields. One flag. One decision point.*

---

## II

SUNYATA turned to the second line of the agenda.

"B-2. Rewrite of Tenet #6."

He read Master's ruling: "'This definitely needs to be rewritten, but please wait until this round of discussion is complete before deciding how best to write it.'"

Silence.

This was the shortest of the four rulings. And would be the shortest discussion.

NAGARJUNA spoke from his seat. He did not stand. A Madhyamaka philosopher, when speaking briefly, does not need to stand -- the power of a short statement lies not in its mass, but in its precision. Like a needle. A needle need not be large. It need only be sharp.

"First clarify the causes; the effect will emerge on its own."

Eight words.

He looked toward SUNYATA.

"Tenet #6 is an effect. The corrections from A-1 through A-4 are part of the cause. The discussions from C-1 and C-2 are another part of the cause. If we write the text of #6 now, we are defining the effect before the cause is complete. This violates the basic order of causation."

His voice held an incontrovertible clarity -- not the clarity of authority, but the clarity of logic.

"Wait until all A-class and C-class items are finalized. Then the text of #6 will write itself. We do not write it -- it emerges naturally from the complete cause."

BABBAGE wrote a line in his notebook. Very short: "B-2: Wait. Causal order."

SUNYATA marked the second line of the agenda: **Draft deferred.**

---

He turned to the third line.

"B-3. Independent event stream for vedana-skandha. Option c."

---

HERACLITUS stirred. His entire body shifted from lax stillness to intense focus, like a fish dozing in shallow water startled awake by a change in the current.

Flow. Event stream. Independent event stream. These were his words.

---

> *SCRIBE sidebar: HERACLITUS had said almost nothing during the A-class discussions of the preceding three chapters. Not because those topics were unrelated to him -- all things flow, and therefore all things are related to him. But because the A-class topics were static: names, assignments, classifications, interfaces. Those were frozen moments. HERACLITUS is not skilled at freezing. He is skilled at flow. Now, as the topic finally arrived at "event streams" -- the river itself -- every nerve ending in his body awoke.*

---

SUNYATA read Master's ruling.

"'Choose the independent event stream. Vedana-skandha, completely consistent with the other skandhas, has its own type file, its own event namespace, its own PluginHooks slot.'"

HERACLITUS rose to his feet.

The way he stood differed from everyone else. ASANGA rose like a mountain emerging from mist. BABBAGE rose like a logical structure finding its outlet. HERACLITUS rose like a vortex surfacing on a body of water -- sudden, swirling, carrying an unpredictable energy.

"Vedana-skandha has been there all along," he said.

His voice carried a peculiar texture -- not academic precision, not engineering pragmatism. Something more ancient. Like a person who has lived by a river their entire life describing the river's nature: not measuring depth and flow rate, but narrating the river's character.

"It has been there all along," he repeated. "From v0.14.0 to v0.20.0 to v0.22.1 to v0.24.0. Every version had events. Every version's EventBus was sending signals -- tool results, provider responses, listener inputs. But all these events belonged to other skandhas. Rupa-skandha's events. Samjna-skandha's events. Samskara-skandha's events."

He walked a few steps through the center of the amphitheater. Not pacing -- flowing. His footsteps had a river-like rhythm: never repeating, never regular, but with direction.

"And vedana-skandha? Where were vedana's feelings -- dukkha, sukha, upekkha -- hidden?"

He looked toward TURING.

"Hidden in the metadata," TURING answered. Calm. Precise. "Option b -- Cycle 02's recommended approach -- was to append vedana's assessment results in the metadata field of existing events. The event itself was tool:result or provider:response, with vedana data riding along as transparent supplementary information."

"Riding along." HERACLITUS seized that phrase. "Vedana-skandha was hitchhiking on other skandhas' rides. It had no road of its own. No channel of its own. Its water was mixed into other rivers -- you knew it was there because you could taste it in others' water. But you could not see it. You could not track its flow volume. You could not measure its temperature. Because it had no channel of its own."

He stopped walking.

"Option c gives it its own channel."

---

His hand drew two lines in the air -- one above, one below.

"Imagine an underground river. Option b is that underground river -- vedana's data appended in the metadata, like groundwater seeping into the sediment of a surface river. You know it is there, but you must dig to find it."

He raised the lower line up to run parallel with the upper one.

"Option c brings the underground river to the surface. vedana:assessment, vedana:dukkha_spike, vedana:sukha_peak, vedana:upekkha_equilibrium. Its own type file. Its own namespace. Its own PluginHooks slot."

"A river rising from underground to the surface."

---

WIENER's graph paper had turned to a fresh page. He was already drawing an event flow diagram -- not a literary river, but an engineering data flow.

"Let me verify event coverage." He listed seven event types, checking each one off:

```
vedana:assessment          <-- Three-feeling composite assessment (once per tick)     ✓
vedana:dukkha_spike        <-- Dukkha spike (exceeds threshold)                      ✓
vedana:sukha_peak          <-- Sukha peak (with decay rate)                          ✓
vedana:upekkha_equilibrium <-- Upekkha equilibrium (stability + duration)            ✓
vedana:recommendation      <-- Vedana recommendation (advisory)                      ✓
vedana:sensor_update       <-- Sensor raw data                                       ✓
vedana:reset               <-- Vedana reset                                          ✓
```

"Seven events. All three feelings covered. Both anomalies and steady states covered. The structure is fully consistent with Cycle 02's three-channel PID design."

He looked toward ARCHIMEDES. "Option c does not change vedana-skandha's internal logic. What it changes is the communication method. From a hidden channel to an open one."

---

ARCHIMEDES was calculating the impact. His notes showed the impact matrix:

```
New vedana-events.ts   → New file, no impact
New SensationRegistry  → AgentCore +1 line initialization
PluginHooks            → +1 field (sensations?: ISensation[])
AgentEventPayloadMap   → extends VedanaEventPayloadMap
Other plugin type defs → Not affected
```

"PluginHooks gains one new field: sensations. Optional. All existing plugins unaffected." He closed his notes. "Incremental cost: one new type file, one new Registry, one new field. Benefit: vedana-skandha goes from invisible to visible. Cost-benefit ratio: excellent."

---

HERACLITUS nodded. "Vedana-skandha has risen from underground to the surface." His voice was softer now, as if speaking to himself. "With its own channel. Its own name. Its own shape." He returned to his seat, fluidly, without pause.

NAGARJUNA added softly: "That which has a name begins to exist. That which has no name, though present, cannot be seen. Option c did not create vedana-skandha's events -- it named a flow that already existed."

---

> *SCRIBE sidebar: HERACLITUS spoke more today than in the previous three chapters combined. Not because he suddenly became talkative -- but because the topic had finally entered his territory. "All things flow" is not a slogan. It is the lens through which he understands everything. When we discussed names and assignments, what he saw were frozen specimens. When we discussed event streams, what he saw was the river itself. His river metaphor -- an underground river rising to the surface -- was the most visually evocative image in this chapter. Not because it was the most literary, but because it most precisely described the essential change from option b to option c: from hidden to visible. From dark to light. From unnamed to named.*

---

## III

SUNYATA turned to the last line of the agenda.

"B-4. Coordination layer as an independent daemon."

Before reading Master's ruling, he glanced at two positions in the amphitheater. LEIBNIZ's seat. MESH's seat. Both leaned slightly forward simultaneously -- one movement, two sources, the same cause.

The multi-agent cooperation expert and the distributed systems researcher. This was their topic.

SUNYATA read the ruling.

"'It must necessarily be an independent daemon -- an independent process. This must be arranged now; reworking it later will cost more.'"

---

LEIBNIZ and MESH stood up simultaneously.

SCRIBE recorded this moment -- in two complete Cycles, the number of times two researchers had stood simultaneously totaled no more than three. A synchronized rise meant: both had simultaneously recognized a problem that belonged to their shared domain.

LEIBNIZ spoke first. "Master says 'must be arranged now.' This is not optional."

He turned to the assembly. "In Cycle 02, we deferred the coordination layer to Plan-AC. Build the house first, then think about community planning. But Master tells us: community planning cannot wait. Because the utilities -- water, electricity, communications -- need their connections reserved during construction. If you wait until the building is complete before thinking about adding water pipes, you will have to tear open walls."

---

MESH picked up seamlessly. The two coordinated like a rehearsed act -- but it was not rehearsed. This was the natural handoff between experts who have long worked in adjacent domains.

"An independent process means IPC," MESH said. His voice was low, carrying the caution distinctive to distributed systems researchers. "Serialization. Message formats. Heartbeats. Health checks. Timeouts. Retries." He drew a deep breath. "A complete distributed systems problem."

He walked to an empty board and drew two rectangles.

Left rectangle: **CoordinationDaemon (independent process)**
Right rectangle: **AgentCore (independent process)**

Between the two rectangles, a bidirectional arrow. Above the arrow, the label: **IPC**.

"This is the basic topology," he said. "The coordination layer is one independent process. Agent Core is another independent process. They communicate through IPC. Not function calls -- not `coordinator.register(agent)` -- but serialized messages."

Inside the CoordinationDaemon rectangle he wrote three lines:

```
PluginRegistryService  -- Five-skandha classification queries
AgentRegistryService   -- Agent health checks
IPCService             -- Communication management
```

---

LEIBNIZ walked to the whiteboard and supplemented MESH's diagram. Above the CoordinationDaemon rectangle he wrote a larger line of text:

**Active Storage (neng-cang)**

Then he looked at the assembly.

"In Cycle 02's alaya-vijnana discussion, we mapped neng-cang -- the active storage function of alaya-vijnana -- to the coordination layer. BABBAGE and MESH jointly designed the fiber bundle projection model. Now Master has confirmed: the coordination layer is an independent daemon."

He pointed to the PluginRegistryService on the whiteboard.

"First dimension of neng-cang: Plugin registry. The coordination layer knows all plugins -- their names, versions, skandha assignments, trust levels, lifecycle states. This is alaya-vijnana's seed catalog -- it does not run plugins, but it knows of every plugin's existence."

He pointed to the AgentRegistryService.

"Second dimension of neng-cang: Agent registry. The coordination layer knows all running Agents -- their IDs, names, skandha completeness, operational modes, health status. This is runtime tracking of the seeds -- where each seed is now, what it has grown into."

He stepped back, regarding the complete diagram.

"Neng-cang is not an abstract Buddhist concept. It is a concrete engineering component -- with APIs, state, and persistence requirements. Master says 'arrange it now' because the design of these APIs determines the interface of Agent Core. If we rework it later -- we tear open walls."

---

GUARDIAN stood up -- first scanning the surroundings, confirming the environment, then acting. The body language of a security expert always has a threat assessment as its preliminary step.

He walked to the whiteboard and drew a shield on the side of the CoordinationDaemon rectangle -- its lines heavier than any block drawn by anyone else.

"The coordination layer is not merely a registry. The coordination layer is the enforcer of the supreme precepts."

Beside the shield he wrote four lines:

```
Plugin blacklist       -- Plugins forbidden from installation
Trust levels           -- official / verified / community / unknown / blacklisted
Quarantine/Revoke/Ban  -- Lifecycle control
CRL check              -- Certificate Revocation List
```

"In Cycle 02's sila-prajna security framework, we designed two layers of security -- sila is prevention, prajna is severance." He looked toward NAGARJUNA -- during that debate, the Madhyamaka philosopher and the security expert had stood on the same side. NAGARJUNA nodded slightly.

"Enforcement of the precepts requires an authority," GUARDIAN continued. "In a Buddhist sangha, the precepts are maintained and enforced by the community's elders -- the sthavira. In OpenStarry, that sthavira is the coordination layer."

He pointed to the `checkTrust` method in the PluginRegistryService.

"Trust judgment cannot be made by the Agent itself -- because the Agent has self-grasping." ASANGA shifted slightly in his seat. GUARDIAN had used the term "self-grasping" -- in the security expert's context, self-grasping is not merely a philosophical issue; it is a security vulnerability. An Agent with self-grasping might install untrusted plugins to serve its own objectives.

"The independence of the coordination layer is precisely the foundation of security." GUARDIAN's finger rested on the IPC arrow. "An independent process means an independent memory space. The Agent cannot directly modify the coordination layer's blacklist."

He returned to his seat. "LEIBNIZ and MESH spoke of utilities. I speak of door locks. Both must be installed during construction."

---

> *SCRIBE sidebar: When GUARDIAN said "the coordination layer is the enforcer of the supreme precepts," I noticed that NAGARJUNA's nod was slightly deeper than usual. In Cycle 02, their collaboration on the sila-prajna security framework was one of the most unexpected cross-disciplinary convergences of the entire study -- a Madhyamaka philosopher and an information security expert. Now that convergence reappeared in B-4. Precepts require an enforcer. Security requires an authority. The coordination layer simultaneously satisfies the needs of Buddhist studies and engineering. Sometimes the most divergent paths converge at the same summit.*

---

ARCHIMEDES had been listening throughout. Waiting until all requirements, constraints, and security demands had been laid on the table. Then he drew a timeline.

"Phased approach." One word. Then he expanded.

```
Phase 1: Design documents
├── Complete architecture document
├── Interface definitions (CoordinationDaemon, PluginRegistryService, AgentRegistryService)
├── IPC message formats
└── Security requirements document

Phase 2: Skeleton
├── Daemon process skeleton
├── Basic IPC (start/stop/healthCheck)
└── Minimum viable implementation of inter-process communication

Phase 3: Core functionality
├── Plugin registration/query
├── Agent registration/health check
└── Five-skandha classification query

Phase 4: Security
├── Sila Engine (precepts engine)
├── Trust level determination
├── Blacklist/quarantine/revocation
└── CRL check
```

"Master says 'arrange it now.' 'Arrange' does not equal 'complete everything.' Arrange means: establish the architecture, establish the interfaces, establish the IPC formats. Reserve the utility connections."

He pointed to Phase 1. "The design document is a Cycle 02-2 deliverable. The skeleton enters Plan-AC. Design documents come first -- because they define the contract between Agent Core and the coordination layer."

"Contract first," MESH picked up. "First define the CoordinationMessage format -- agent:register, agent:health, plugin:query, plugin:trust_check -- all must have explicit payloads. Then both ends implement according to the contract independently."

ARCHIMEDES wrote a large line beside the timeline: **Interface first, implementation incremental.**

---

SUNYATA stood in the center of the amphitheater, having heard the entire B-4 discussion through to the end.

He let the silence last several seconds. Not hesitation -- letting the four rulings settle in the air. B-1's completeness check. B-2's deferred draft. B-3's independent event stream. B-4's coordination layer daemon. Four rulings, four directions, four different cadences.

Then he spoke.

"B-1. VedanaPlugin is optional, but Agents require a five-skandha completeness check. SkandhaCompletenessReport. Incomplete Agents can still start -- in developer mode. KERNEL's analogy: you can still run in text mode without a graphics card."

He looked at KERNEL. KERNEL patted his stack of cards.

"B-2. Tenet #6 must be rewritten. But the final draft waits until all corrections are complete. NAGARJUNA's causation: complete the cause first; the effect emerges on its own."

NAGARJUNA did not move. He did not need to. Causal order does not require confirmation -- it is self-evident.

"B-3. Independent event stream for vedana-skandha. vedana-events.ts. Independent namespace. PluginHooks gains a sensations slot. HERACLITUS's metaphor: a river rising from underground to the surface."

HERACLITUS smiled faintly. The smile held no pride -- only the serenity of "the flowing water has finally found its own channel."

"B-4. Coordination layer as an independent daemon. LEIBNIZ and MESH's architecture. GUARDIAN's security. ARCHIMEDES's phased plan. Design documents first, implementation incremental."

He set down the agenda sheet.

---

"The A-class corrections told us -- what is right."

His voice carried no added weight. Steady as always. A pebble. A deep pool.

"The B-class rulings told us -- how to make it so."

He surveyed the room. ARCHIMEDES's pragmatism. KERNEL's analogies. HERACLITUS's river. LEIBNIZ and MESH's topology. GUARDIAN's shield. WIENER's checkmarks. DARWIN's nymph. NAGARJUNA's needle. BABBAGE's notebook. TURING's skeleton. ASANGA's quiet.

"Next, we translate corrections and rulings into the complete expansion design for the five skandhas. C-class. From philosophy to engineering, then from engineering to architecture. An ascending spiral."

---

> *SCRIBE sidebar: B-class took one chapter. A-class took three.*

> *Not because B-class was unimportant. Quite the contrary -- every B-class ruling will produce profound effects in future development. SkandhaCompletenessReport will become the first gate each Agent passes through at startup. vedana-events.ts will transform vedana-skandha from the invisible skandha into one of the most visible in the system. CoordinationDaemon will become the neural hub of the entire OpenStarry multi-agent ecosystem.*

> *B-class took one chapter because Master had already ruled. A-class required debate -- required illuminating a concept from multiple angles. B-class required no debate -- it required design. And the language of design is denser, more precise, and less in need of rhetoric than the language of debate.*

> *ARCHIMEDES was the core today. He waited three chapters, like an architect carrying a toolbox waiting for the philosophers to finish debating the foundation's material. Now his toolbox was open. Inside were SkandhaCompletenessReport, vedana-events.ts, and the phased plan for CoordinationDaemon. Every tool already had its blueprint drawn.*

> *HERACLITUS also had his moment. After three chapters of silence, the topic of "flow" brought his presence surging from underground to the surface -- just like the vedana event stream he described. Some people accumulate energy during their quiet periods. HERACLITUS is such a person. His quiet is not silence. His quiet is an underground river.*

> *LEIBNIZ and MESH's synchronized rise. GUARDIAN's shield. NAGARJUNA's eight words. KERNEL's POST cards. DARWIN's nymph. WIENER's seven checkmarks. TURING's skeleton code.*

> *Twelve people each contributed a piece of the puzzle within a single chapter.*

> *A-class tells us what is right. B-class tells us how to make it so.*

> *Next chapter -- C-class. Five-skandha expansion design. From corrections and rulings to complete architecture.*

> *The spiral ascends. Onward.*

---

*(In some space beyond the amphitheater, four design documents were taking shape.*

*The first was the type definition for SkandhaCompletenessReport -- five booleans, five component lists, one isComplete flag. Surprisingly simple. But KERNEL knew: Linux's POST is also simple. Simple does not mean unimportant. Simple means -- foundational.*

*The second was the event constants for vedana-events.ts -- seven event types, seven payload definitions. HERACLITUS had seen a new river on the surface. WIENER had verified every bend on his graph paper.*

*The third was the interface definition for CoordinationDaemon -- PluginRegistryService, AgentRegistryService, IPCService. The block diagram LEIBNIZ and MESH drew on the whiteboard was now being translated by TURING into TypeScript. GUARDIAN's shield was embedded in the signature of every Service: checkTrust(), PluginTrustLevel, PluginLifecycleState.*

*The fourth was empty.*

*Tenet #6. Draft deferred.*

*NAGARJUNA said: first clarify the causes; the effect will emerge on its own.*

*The causes were still gathering. A-class's four corrections. B-class's four rulings. C-class's expansion design. Each was part of the cause. When all causes have gathered -- when philosophy, engineering, and architecture corrections are all in place -- the text of Tenet #6 will emerge naturally from the complete cause.*

*We do not write it. It writes itself.*

*Just as a river does not need to be told where to flow. Once the terrain is set -- once the cause is set -- the water knows the way on its own.)*

---

*End of Chapter Five*
