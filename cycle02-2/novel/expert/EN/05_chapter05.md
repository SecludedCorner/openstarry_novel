# Chapter Five: Four Rulings

---

ARCHIMEDES sat up straight.

During the A-class discussions of the preceding three chapters, his spine had maintained a restrained angle: leaning forward fifteen degrees, fingers occasionally tapping the table, but in a converging rhythm, like an architect carrying a toolbox who had been seated in the audience, waiting for the philosophers to finish debating the orientation of the foundation. He had heard the line BABBAGE drew through the equals sign, had heard ASANGA's final ruling on the four afflictions of "self-view / self-conceit / self-love / self-delusion," had heard LINNAEUS revise his taxonomic classification of IIdentity from "genus = species" to "genus superset species_1, species_2, species_3, species_4," had heard the funeral-like solemnity in SYNTHESIST's voice as he traced back to Cycle 02's proudest moment.

He had sat there the entire time with his toolbox. The box had never been opened.

That waiting was over.

---

SUNYATA held a new agenda sheet in his hands, a thin single page, four lines of text.

"The A-class corrections took three chapters," he said. His voice steady as always. A pebble. A deep pool. "From causal chains to vijnana-skandha subclasses, from observer separation to EgoFramework's proper assignment. Those were philosophical corrections -- telling us what is right."

"Now we enter the B-class. Master's rulings on our four engineering questions. This is the moment where philosophy turns into engineering."

---

ARCHIMEDES's finger tapped the table once -- crisp, carrying anticipation.

"I have been waiting for this moment for a long time," he said.

A few low chuckles rippled through the amphitheater. They all knew ARCHIMEDES's state during the A-class discussions: a man carrying a toolbox, seated among a group of philosophers debating the aesthetics of architecture. What was inside his toolbox? Type definitions. Interface signatures. Impact matrices. Phased plans. Every tool waiting for its occasion of use.

SUNYATA nodded slightly. "B-1. VedanaPlugin is optional, and five-skandha completeness checking."

---

> *SCRIBE sidebar: The transition from A-class to B-class was like a symphony shifting from adagio to allegro. The rhythm of A-class discussions was contemplative -- ASANGA's city metaphor, BABBAGE's strikethroughs, NAGARJUNA's naming balance -- each topic needed time to ferment. You had to wait for the ink to seep through the paper, for the boundaries of concepts to slowly emerge through repeated debate.*

> *B-class was different. The rhythm of B-class was decisional. Master had already ruled. Our task was not to debate right and wrong, but to translate rulings into designs. ARCHIMEDES had waited three chapters. Now it was his turn.*

> *I noticed his finger tapped only once. Not the rhythmic repeated tapping of the A-class discussions -- the kind that suppressed the urge to speak. This single tap was more like a signal -- the sound of a toolbox clasp being unlatched.*

---

SUNYATA read Master's original words.

"'Some plugins have already inherited this plugin. As stated above, an agent should be able to start as long as it is complete. But perhaps a developer mode or some other mode is needed. It should be optional -- the agent can start even if incomplete, but a warning is needed.'"

He set down the paper.

"Three keywords. Optional. Complete. Warning."

---

KERNEL's hand was already reaching for his stack of analogy cards. He flipped through two -- not right -- flipped one more -- pulled out the fourth. What was written on the left side, SCRIBE could not see clearly. The right side was blank. He was waiting for a match.

"POST," he said, standing up. His voice carried a certainty that had been suppressed through the previous three chapters -- an OS expert finally standing on his own ground.

He walked to the center of the amphitheater. No projection used. He worked with cards and his voice.

"Power-On Self-Test. The very first instruction a CPU executes the instant a computer is powered on. On the x86 architecture, that instruction sits at the reset vector -- address `0xFFFFFFF0` -- and jumps to the BIOS or UEFI firmware entry point. Then hardware enumeration begins."

He flipped through his cards and wrote down the sequence on the blank side:

```
POST Hardware Enumeration Order (typical x86)
───────────────────────────────────────────────
1. CPU self-test      — registers, ALU, cache
2. Memory self-test   — row-by-row RAM scan
3. Chipset            — Northbridge/Southbridge / PCH
4. Graphics card      — initialize video output
5. Storage controller — SATA/NVMe enumeration
6. Network card       — PXE boot (optional)
7. Audio/USB          — secondary peripherals
8. Hand off to bootloader — GRUB / systemd-boot
```

"This order is not arbitrary," KERNEL said, his voice steady, carrying the particular confidence of a man who has read the entire Intel SDM cover to cover. "It follows a **dependency tree**. CPU is the foundation of all computation -- without CPU, subsequent enumeration cannot execute. Memory is the container for all data -- without RAM, the firmware has no workspace of its own. These two are hard dependencies. Everything after them is a soft dependency."

He flipped through his cards.

"In `systemd`'s language --"

He wrote two lines:

```
Requires=cpu.target memory.target    # Hard dependency: missing one prevents startup
Wants=display.target network.target  # Soft dependency: missing one means degraded operation
```

"`Requires` denotes a hard dependency. If the depended-upon unit fails to start, the current unit must also fail. `Wants` denotes a soft dependency. The depended-upon unit may fail, and the current unit still starts. Linux's entire service management is built upon the distinction between these two keywords."

He arranged three cards in a row.

"The distinction between hard dependencies and soft dependencies. The five skandhas are like these hardware components."

He looked at the entire assembly.

"But Master's ruling tells us something subtle -- an Agent's five skandhas are all `Wants`, with no `Requires`."

BABBAGE looked up. "No hard dependencies?"

"None," KERNEL confirmed. "What Master said is: 'An agent should be able to start as long as it is complete. But the agent can start even if incomplete, only a warning is needed.' This means the absence of any single skandha is not fatal. Incomplete does not equal unable to start. Incomplete equals degraded startup. Just like no graphics card -- text mode. No network card -- offline mode. No sound card -- silent. The system is alive; its functionality is merely limited."

He paused, then added a more precise analogy.

"If you want a closer Linux boot analogy: after the kernel starts, it invokes the `init` process -- on modern Linux, that is `systemd` -- which reads unit files and brings up services one by one. If `NetworkManager.service` fails to start, the system does not kernel panic. It logs a `WARNING`-level entry, marks the service as `failed`, and continues starting the remaining services."

He added a line on his card:

```
systemd degraded startup  <-->  Agent developerMode degraded startup
    Failed unit is marked but does not block     Missing skandha is logged but does not block
    journalctl can query failure reasons          SkandhaCompletenessReport can query what is missing
```

---

ARCHIMEDES was already drawing.

Before KERNEL had even finished, an embryonic interface appeared in his engineering notes. His pen speed was fast -- not sloppy, but a kind of shorthand trained over many years: recording only key types, key fields, key methods, omitting all decoration. But this time, he stopped and started over.

"KERNEL's analogy has already given me the complete structure," he said. His voice pragmatic, clear, every word like a brick. "Let me translate it into TypeScript."

He stood up -- he rarely stood up; ARCHIMEDES's style was to sit at his workstation and draw -- but this time he rose, because what he was about to present was not a sketch but a type definition ready to enter the codebase directly.

```typescript
/** SkandhaCompletenessReport — Design inspiration: BIOS/UEFI POST (Power-On Self-Test) */
interface SkandhaCompletenessReport {
  readonly rupa:     { present: boolean; components: string[] };  // rupa-skandha: IUI/IListener
  readonly vedana:   { present: boolean; components: string[] };  // vedana-skandha: ISensation
  readonly samjna:   { present: boolean; components: string[] };  // samjna-skandha: IProvider
  readonly samskara: { present: boolean; components: string[] };  // samskara-skandha: ITool
  readonly vijnana:  { present: boolean; components: string[] };  // vijnana-skandha: IGuide/IVolition/IIdentity/IReflection
  readonly isComplete: boolean;
  readonly missing: string[];
}
```

He held up his notes.

"SkandhaCompletenessReport. Five-skandha completeness report." Every word like a brick. "Five skandhas, one field per skandha. Boolean -- present or absent. Component list -- if present, which ones. Note the `vijnana` field -- after the A-2 correction, vijnana-skandha is no longer a single IIdentity, but a set of IVijnana subclasses: IGuide, IVolition, IIdentity, IReflection. The completeness check must reflect this correction."

He looked toward KERNEL.

"Your hardware check. POST. Except instead of checking CPU and memory, it checks rupa-skandha and vijnana-skandha."

---

KERNEL nodded. Then he did something -- he wrote a line on the right side of that blank card. SCRIBE could finally see the card's format: left side was "Operating System Concept," right side was "OpenStarry Mapping."

Left: `POST (Power-On Self-Test)`
Right: `SkandhaCompletenessReport`

Below it he added another line:

Left: `systemd unit dependency (Requires/Wants)`
Right: `skandha hard/soft dependency (isComplete/developerMode)`

He slipped the card back into his stack. Two matches. One card.

---

TURING's screen lit up. A skeleton of code -- his style: skeleton first, flesh later. But this time the skeleton was more complete than anything from Cycle 02.

```typescript
// Production mode ≈ systemd Requires | Developer mode ≈ systemd Wants
interface StartOptions {
  developerMode?: boolean;  // Allow incomplete startup (nymph mode)
}

async start(options?: StartOptions): Promise<void> {
  const report = this.checkSkandhaCompleteness();

  if (!report.isComplete) {
    const missingMsg = `Agent five-skandha incomplete: missing ${report.missing.join(', ')}`;

    // Regardless of mode, emit event to notify all listeners (including coordination layer daemon)
    this.bus.emit({
      type: 'agent:skandha_incomplete',
      timestamp: Date.now(),
      payload: { report, developerMode: !!options?.developerMode },
    });

    if (options?.developerMode) {
      logger.warn(`[DEV MODE] ${missingMsg}`);  // Degraded startup ← degraded.target
    } else {
      logger.error(missingMsg);
      throw new Error(missingMsg);  // Refuse to start ← emergency.target
    }
  }
  // ... normal startup flow ...
}
```

"AgentCore.start()," TURING said. Voice calm as always. "Note the position of the event emission -- before the branching logic. Regardless of mode, the `agent:skandha_incomplete` event is always emitted. This conforms to the basic principle of event-driven architecture: separation of notification and control. The event is the notification -- all listeners (including the B-4 coordination layer daemon) will receive it. The exception is the control -- it decides whether startup continues."

---

DARWIN leaned slightly forward. "Developer mode is an evolutionary intermediate state."

Several gazes turned toward him.

"Hemimetabolism," he elaborated. "Insect metamorphosis comes in two modes. Complete metamorphosis -- egg, larva, pupa, adult -- four stages, with dramatic morphological reorganization during the pupal stage; the body plans of larva and adult are completely different. Dragonflies, mayflies, and orthopterans take the path of incomplete metamorphosis -- the nymph molts through successive instars directly into the adult, without a pupal stage."

He drew a gradual line in the air.

"Nymph and adult are morphologically similar, but the nymph is incomplete. A dragonfly nymph (naiad) has compound eyes, mouthparts, and legs; it can prey, swim, and breathe -- but it has no wings. It lives in water, limited in function but viable. Until the final molt -- the nymph crawls from the water, its exoskeleton splits, and its wings unfurl."

He looked toward TURING's code on screen.

"`developerMode` is the nymph. An Agent missing a certain skandha -- perhaps vedana (no sensors), perhaps a subclass of vijnana (no IReflection) -- its functionality is incomplete, but it is alive. It can run. It can be tested. It can be developed. Until the developer fills in all the missing skandhas -- the final molt -- and switches to production mode."

He added the software engineering parallel. "In continuous integration, this is called progressive feature enablement. You do not wait until every feature is complete before deploying -- you use feature flags to control which features are visible to users. `developerMode` is OpenStarry's feature flag."

KERNEL added a line in small script on the blank space of his card: `text mode = nymph = developerMode = degraded.target`.

---

> *SCRIBE sidebar: B-1's discussion was shorter than any single item from the A-class. Not because it was unimportant -- but because Master's ruling was sufficiently clear, KERNEL's analogy sufficiently vivid, and ARCHIMEDES's design sufficiently direct.*

> *But I noticed an interesting phenomenon: the analogies cited in the B-1 discussion came from three entirely different domains. KERNEL used operating system boot sequences (POST + systemd dependency). DARWIN used insect developmental biology (hemimetabolism + nymph). TURING used event-driven architecture principles (notification vs. control). Three analogies describing the same thing: incomplete does not mean unusable.*

> *Philosophical discussion requires expansion -- you must illuminate a concept from multiple angles before you can see its full contours. Engineering discussion requires convergence -- you must select one option from among many possibilities, then transform it into type definitions and method signatures. B-1's convergence was swift and clean. SkandhaCompletenessReport. One interface. Five fields. One flag. One decision point.*

---

## II

SUNYATA turned to the second line of the agenda.

"B-2. Rewrite of Tenet #6."

He read Master's ruling: "'This definitely needs to be rewritten, but please wait until this round of discussion is complete before deciding how best to write it.'"

Silence.

This was the shortest of the four rulings. And would be the shortest discussion.

---

NAGARJUNA spoke from his seat. He did not stand. A Madhyamaka philosopher, when speaking briefly, does not need to stand -- the power of a short statement lies not in its mass, but in its precision. Like a needle. A needle need not be large. It need only be sharp.

"First clarify the causes; the effect will emerge on its own."

Eight words.

---

He looked toward SUNYATA.

"Tenet #6 is an effect. The corrections from A-1 through A-4 are part of the cause. The discussions from C-1 and C-2 are another part of the cause. If we write the text of #6 now, we are defining the effect before the cause is complete. This violates the basic order of causation."

His voice held an incontrovertible clarity -- not the clarity of authority, but the clarity of logic.

"The first verse of the Examination of Causal Conditions in the Mulamadhyamakakarika:"

> "Neither arising nor ceasing, neither permanent nor annihilated, neither identical nor differentiated, neither coming nor going."
> -- Nagarjuna, *Mulamadhyamakakarika*, Chapter 1: Examination of Causal Conditions, Verse 1

"The eightfold negation of the Middle Way. Things do not arise from nothingness (neither arising), nor vanish into void (neither ceasing). Every effect is a manifestation of its causes -- not created from nothing, but naturally emerging from the aggregation of causes."

His tempo slowed, letting every word sink into the air.

"The text of Tenet #6 does not need to be 'written.' It needs to be 'awaited.' Awaited until all A-class and C-class items are finalized. Until all the causes -- causal chain correction, vijnana subclasses, observer separation, EgoFramework assignment, five-skandha expansion, composition pattern -- are all in place. Then the text of #6 will write itself. We do not write it -- it emerges naturally from the complete cause."

He quoted another verse, almost a murmur to himself:

> "All things arising from conditions, I declare to be empty, also to be provisional designations, and also the meaning of the Middle Way."
> -- Nagarjuna, *Mulamadhyamakakarika*, Chapter 24: Examination of the Four Noble Truths, Verse 18

"Before the conditions have fully gathered, the text of Tenet #6 is empty -- not nonexistent, but lacking sufficient conditions. Waiting is itself the practice of the Middle Way. Neither rushing to finalize (neither permanent), nor abandoning the intent to rewrite (neither annihilated)."

---

BABBAGE wrote a line in his notebook. Very short: "B-2: Wait. Causal order. $C_6 = f(A_1, A_2, A_3, A_4, C_1, C_2)$, evaluate only when all causes are determined."

SUNYATA marked the second line of the agenda: **Draft deferred.**

---

He turned to the third line.

"B-3. Independent event stream for vedana-skandha. Option c."

---

HERACLITUS stirred.

His entire body shifted from lax stillness to intense focus, like a fish dozing in shallow water startled awake by a change in the current. Not a gradual shift -- a phase transition. Solid to liquid. The sudden collapse of crystalline structure and the instantaneous formation of fluid flow.

Flow. Event stream. Independent event stream. These were his words.

---

> *SCRIBE sidebar: HERACLITUS had said almost nothing during the A-class discussions of the preceding three chapters. Not because those topics were unrelated to him -- all things flow (panta rhei), and therefore all things are related to him. But because the A-class topics were static: names, assignments, classifications, interfaces. Those were frozen moments -- a river photographed into stillness. HERACLITUS is not skilled at photographs. He is skilled at film.*

> *To be precise, he is skilled at the river itself.*

> *Now, as the topic finally arrived at "event streams" -- the river itself -- every nerve ending in his body awoke. I noticed his postural shift took less than two seconds. From the near-somnolent laxity of A-class discussions to the intense focus the instant B-3 was announced. Not "gradually waking up." Rather, "always awake, merely waiting for his river."*

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

---

He looked toward TURING.

"Hidden in the metadata," TURING answered. Calm. Precise. "Option b -- Cycle 02's recommended approach -- was to append vedana's assessment results in the metadata field of existing events. The event itself was `tool:result` or `provider:response`, with vedana data riding along as transparent supplementary information."

HERACLITUS stopped, facing the entire assembly.

"Let me make clear the architectural difference between option b and option c. Because this is not a superficial choice -- they represent two fundamentally different paradigms of event-driven architecture."

He drew two layers of structure in the air.

"Option b is the **Event Enrichment** pattern. Existing events are the carrier; vedana data rides along. Like appending a note to an existing letter -- the letter's recipient and routing remain unchanged; the note is merely additional metadata. This is a minimally invasive design. The cost: if you want to analyze the patterns in those notes -- say, tracking the time series of all dukkha spikes -- you must traverse all letters, then extract the vedana data from each one's annotations. This is an $O(n)$ scan, where $n$ is the total number of all events, while what you actually need is only a small fraction thereof."

"Option c is a sub-pattern of **Event Sourcing**. Vedana-skandha has its own event stream -- independent, complete, capable of being consumed and analyzed independently. In the terminology of event-driven architecture, this is called a **Domain Event** -- it does not ride along; it is the letter itself. With its own envelope, its own recipient, its own routing."

He drew two separated sequences in the air with his finger.

"If you are familiar with CQRS (Command Query Responsibility Segregation), you will recognize the structure of option c -- the read model and write model are separated. Other skandhas' events are results of actions (write side). Vedana's events are records of feeling (a form of read side). Mixing them together is like writing transaction logs and audit logs into the same table. It can work, but it violates separation of concerns."

---

He stopped walking.

"Hitchhiking." He returned to that word. "Vedana-skandha was hitchhiking on other skandhas' rides. It had no road of its own. No channel of its own. Its water was mixed into other rivers -- you knew it was there because you could taste it in others' water. But you could not see it. You could not track its flow volume. You could not measure its temperature. Because it had no channel of its own."

He spread his hands from his chest outward, as if opening a door.

"Option c gives it its own channel."

---

His hand drew two lines in the air -- one above, one below.

"Imagine an underground river. Option b is that underground river -- vedana's data appended in the metadata, like groundwater seeping into the sediment of a surface river. You know it is there, but you must dig to find it. In engineering terms, this means: to analyze vedana's behavioral patterns, you must write custom filters -- extract `metadata.vedana` from `tool:result` events, extract `metadata.vedana` from `provider:response` events -- then manually aggregate these fragments scattered across different event types."

He raised the lower line up to run parallel with the upper one.

"Option c brings the underground river to the surface."

```
Option b — Underground river (metadata attachment)
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
Surface river (EventBus main stream):
 tool:result → provider:response → tool:result → ...
   ↓ metadata.vedana     ↓ metadata.vedana
   ↓ {dukkha:0.3}        ↓ {dukkha:0.7}
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
  → vedana data scattered across other events, requires excavation

Option c — Surface river (independent event stream)
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
Channel A (samskara/samjna/rupa event stream):
 tool:result → provider:response → listener:input → ...

Channel B (vedana independent event stream):
 vedana:assessment → vedana:dukkha_spike → vedana:upekkha_equilibrium → ...
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
  → vedana data in its own channel, directly visible
```

"A river rising from underground to the surface. vedana:assessment, vedana:dukkha_spike, vedana:sukha_peak, vedana:upekkha_equilibrium. Its own type file. Its own namespace. Its own PluginHooks slot."

---

WIENER's graph paper had turned to a fresh page. He was already drawing an event flow diagram -- not a literary river, but an engineering data flow. A control theorist views event streams in an entirely different way from a runtime dynamics expert: where HERACLITUS sees the river's character, WIENER sees the signal's spectrum.

"Let me verify event coverage," he said. "The three feelings -- dukkha, sukha, upekkha -- are three independent control channels. Each channel requires sufficient events to support a complete sense-control loop."

He listed seven event types, checking each one off, annotating the control theory correspondence alongside:

```
Event Type                         Control Theory Correspondence                      Three-Feeling Coverage
─────────────────────────────────────────────────────────────────────────────────────────────────────────────
vedana:assessment              → Composite state estimate ŷ(t)                    dukkha+sukha+upekkha  ✓
                                 Each tick outputs three-channel weighted result
                                 $\hat{y}(t) = [d(t), s(t), u(t)]^T$

vedana:dukkha_spike            → Dukkha channel anomaly: $d(t) > \theta_d$       dukkha                ✓
                                 Threshold crossing event
                                 Contains previousIntensity → computable $\dot{d}(t)$

vedana:sukha_peak              → Sukha channel peak: $\dot{s}(t) = 0, s > s_{peak}$   sukha            ✓
                                 Contains decayRate $\lambda$ → $s(t) = s_0 e^{-\lambda t}$

vedana:upekkha_equilibrium     → Upekkha channel steady state: $|u(t) - u_{ref}| < \epsilon$  upekkha  ✓
                                 Contains stability + duration → steady-state quality metric

vedana:recommendation          → Controller output u(t): advisory recommendation   cross-channel        ✓
                                 freshness field → data timeliness

vedana:sensor_update           → Individual sensor raw reading y_i(t)              single-channel       ✓
                                 sensorType specifies dukkha/sukha/upekkha

vedana:reset                   → Controller reset: x(0) = 0                       all                  ✓
                                 Clear accumulated error (integrator reset)
```

"Seven events. All three feelings covered." WIENER nodded, his finger drawing a closed loop on the graph paper. "Let me verify control completeness. A complete PID control loop requires: sensing (sensor_update), estimation (assessment), anomaly detection (dukkha_spike / sukha_peak / upekkha_equilibrium), control output (recommendation), and reset (reset). Seven events cover every link of the loop."

He wrote a line of control theory verification:

$$\text{Observable}(d, s, u) = \text{rank}\begin{pmatrix} C \\ CA \\ CA^2 \end{pmatrix} = 3 \quad \checkmark$$

"The observability of the three-feeling system is guaranteed through seven events. sensor_update provides raw measurements $y(t) = Cx(t)$. assessment provides fused estimates. spike/peak/equilibrium provide the boundary conditions for state transitions. recommendation provides the controller's output. reset provides initialization. The structure is fully consistent with Cycle 02's three-channel PID design."

He looked toward ARCHIMEDES. "Option c does not change vedana-skandha's internal logic. What it changes is the communication method. From a hidden channel to an open one. Control theory does not care about the material of the pipe -- it cares whether signals can be transmitted and observed completely. Option c guarantees complete transmission."

---

ARCHIMEDES was calculating the impact. His notes showed the impact matrix -- not a rough textual description, but a rigorous ASCII table with rows as "modification items" and columns as "affected code files":

```
Impact Matrix: Option c (vedana independent event stream)
═══════════════════════════════════════════════════════════════════════════
Modification Item                  File                     Impact Type  Cost
───────────────────────────────────────────────────────────────────────────
Add vedana-events.ts               types/vedana-events.ts   New          Low
  └─ VedanaEventType (7 constants)
  └─ VedanaEventPayloadMap (7 types)
  └─ VedanaEventTypeValue (union type)

Add SensationRegistry              infrastructure/           New          Low
                                   sensation-registry.ts
  └─ register() / list() / get()

PluginHooks add sensations         types/plugin.ts           Modify+1     Very Low
  └─ sensations?: ISensation[]

AgentEventPayloadMap extension     types/events.ts           Modify       Low
  └─ extends VedanaEventPayloadMap

SDK barrel export addition         src/index.ts              Modify+2     Very Low

AgentCore initialization           agent-core.ts             Modify+3     Low
  └─ createSensationRegistry()
  └─ plugin loader handles hooks.sensations

Other plugin type definitions      *.plugin.ts               Unaffected   Zero
───────────────────────────────────────────────────────────────────────────
Total incremental cost: 1 new type file + 1 new Registry + 3 minimal modifications
Existing plugin compatibility: 100% (sensations field is optional)
═══════════════════════════════════════════════════════════════════════════
```

"PluginHooks gains one new field: sensations. Optional. All existing plugins unaffected." He closed his notes. "Incremental cost: one new type file, one new Registry, three minimal modifications. Benefit: vedana-skandha goes from invisible to visible. Cost-benefit ratio: excellent."

He looked toward TURING. "The specific contents of vedana-events.ts?"

TURING's screen switched to new code -- event constant definitions:

```typescript
/** vedana-events.ts — @skandha vedana (vedana-skandha) independent event type file */
export const VedanaEventType = {
  VEDANA_ASSESSMENT:          'vedana:assessment',          // Three-feeling composite assessment (per tick)
  VEDANA_DUKKHA_SPIKE:        'vedana:dukkha_spike',        // Dukkha spike d(t) > θ_d
  VEDANA_SUKHA_PEAK:          'vedana:sukha_peak',          // Sukha peak + decay rate λ
  VEDANA_UPEKKHA_EQUILIBRIUM: 'vedana:upekkha_equilibrium', // Upekkha steady state |u(t)-u_ref|<ε
  VEDANA_RECOMMENDATION:      'vedana:recommendation',      // Advisory recommendation (non-mandatory)
  VEDANA_SENSOR_UPDATE:       'vedana:sensor_update',       // Sensor raw reading
  VEDANA_RESET:               'vedana:reset',               // Integrator reset
} as const;

export interface VedanaEventPayloadMap {
  [VedanaEventType.VEDANA_ASSESSMENT]: {
    dukkha: number; sukha: number; upekkha: number;  // d(t), s(t), u(t) ∈ [0,1]
    controlOutput: number; vedanaTag: VedanaTag; timestamp: number;
  };
  [VedanaEventType.VEDANA_DUKKHA_SPIKE]: {
    intensity: number; source: string;
    previousIntensity: number;  // Computable ḋ(t)
    threshold: number;          // θ_d
  };
  [VedanaEventType.VEDANA_SUKHA_PEAK]: {
    intensity: number; source: string;
    decayRate: number;  // λ: s(t) = s₀·e^{-λt}
  };
  // ... remaining four event payloads omitted ...
}
```

---

HERACLITUS nodded. "Vedana-skandha has risen from underground to the surface." His voice was softer now, as if speaking to himself. "With its own channel. Its own name. Its own shape." He returned to his seat, fluidly, without pause.

NAGARJUNA added softly: "That which has a name begins to exist. That which has no name, though present, cannot be seen."

He paused for a beat.

"A core insight from the Examination of Causal Conditions in the *Mulamadhyamakakarika*: a name is not a label -- a name is one of the conditions of existence. Option c did not create vedana-skandha's events -- it named a flow that already existed. In Buddhist context, this is called 'establishment through provisional designation' -- because the mode of existence of dependently arisen phenomena is precisely to be cognized, operated upon, and understood through names."

> "All things arising from conditions, I declare to be empty, also to be provisional designations, and also the meaning of the Middle Way."

"vedana:assessment, vedana:dukkha_spike -- these are provisional designations. They make the previously hidden flow into a cognizable object. This is not conferring essence -- vedana-skandha has no fixed self-nature (svabhava). This is conferring visibility."

---

> *SCRIBE sidebar: HERACLITUS spoke more today than in the previous three chapters combined. Not because he suddenly became talkative -- but because the topic had finally entered his territory. "All things flow" is not a slogan. It is the lens through which he understands everything. When we discussed names and assignments, what he saw were frozen specimens. When we discussed event streams, what he saw was the river itself.*

> *His river metaphor -- an underground river rising to the surface -- was the most visually evocative image in this chapter. Not because it was the most literary, but because it most precisely described the essential change from option b to option c: from hidden to visible. From dark to light. From unnamed to named.*

> *But I also noticed the technical analysis that followed his metaphor -- the architectural difference between Event Enrichment and Event Sourcing, the reference to CQRS. HERACLITUS is not merely a poet. He is a runtime dynamics expert with a deep understanding of event-driven architecture, who happens to express that understanding in the language of rivers.*

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

SCRIBE recorded this moment -- in two complete Cycles, the number of times two researchers had stood simultaneously totaled no more than three. A synchronized rise meant: both had simultaneously recognized a problem that belonged to their shared domain. Multi-agent system coordination (LEIBNIZ) and distributed system communication (MESH) -- two disciplines overlapping perfectly on the word "coordination layer."

LEIBNIZ spoke first. His tempo was faster than usual -- not urgency, but the theoretical reserve suppressed through three chapters finally finding its outlet.

"Master says 'must be arranged now.' This is not optional. Let me explain why this is self-evident in multi-agent systems theory."

He turned to the assembly.

"In the BDI (Belief-Desire-Intention) architecture -- the rational agent model proposed by Rao and Georgeff in 1995 -- each Agent has three core components: Belief (cognition of the world), Desire (goals to be achieved), Intention (plans committed for execution). A single Agent's BDI loop is self-consistent -- it perceives the world, forms beliefs, generates desires, selects intentions, executes actions."

He drew a circle in the air -- the BDI loop.

"But what happens when multiple Agents coexist?" He drew a second circle, overlapping the first. "Two Agents' Beliefs may be inconsistent -- A believes plugin X is safe, B believes it is dangerous. Without a common knowledge base, belief conflicts cannot be resolved."

"Halpern and Moses (1990) rigorously defined the hierarchy of shared knowledge:"

$$K_i(\phi) \quad \text{(Agent } i \text{ knows } \phi\text{)}$$
$$E(\phi) = \bigwedge_i K_i(\phi) \quad \text{(all Agents know } \phi\text{ — mutual knowledge)}$$
$$C(\phi) = E(\phi) \wedge E(E(\phi)) \wedge E(E(E(\phi))) \wedge \cdots \quad \text{(common knowledge — infinite nesting)}$$

"The coordination layer is the physical carrier of $C(\phi)$. It is the authoritative, shared knowledge source for all Agents. Plugin trust levels, Agent health status, five-skandha classification -- this information must be common knowledge; it cannot be fragmented local beliefs held independently by each Agent."

He pointed toward SUNYATA. "In Cycle 02, we deferred the coordination layer to Plan-AC. Build the house first, then think about community planning. But Master tells us: community planning cannot wait. Because the utilities -- water, electricity, communications -- need their connections reserved during construction. If you wait until the building is complete before thinking about adding water pipes, you will have to tear open walls."

He emphasized a word in the air: "**Interfaces.**"

---

MESH picked up seamlessly. LEIBNIZ addressed the "why"; MESH addressed the "how." A relay from theory to practice.

"An independent process means IPC," MESH said. His voice was low, carrying the caution distinctive to distributed systems researchers. "Serialization. Message formats. Heartbeats. Health checks. Timeouts. Retries. A complete distributed systems problem."

He walked to the empty board and drew two rectangles.

Left rectangle: **CoordinationDaemon (independent process)**
Right rectangle: **AgentCore (independent process)**

Between the two rectangles, a bidirectional arrow. Above the arrow, the label: **IPC**.

"This is the basic topology," he said. "The coordination layer is one independent process. Agent Core is another independent process. They communicate through IPC. Not function calls -- not `coordinator.register(agent)` -- but serialized messages."

Inside the CoordinationDaemon rectangle he wrote three lines:

```
PluginRegistryService  — Five-skandha classification queries
AgentRegistryService   — Agent health checks
IPCService             — Communication management
```

"The IPC design has four core decisions." He quickly listed them on the board: "Serialization -- first version uses JSON (readability first). Transport layer -- same-machine uses Unix domain socket (zero-copy), cross-machine reserves a TCP interface. Message pattern -- queries use Request-Response, events use Pub-Sub. Reliability -- heartbeat 5s, timeout 15s, exponential backoff reconnection."

He stepped back. "There is also an architectural-level question -- the CAP theorem."

$$\text{CAP}: \lnot(C \wedge A \wedge P)$$

"Brewer's impossibility theorem from 2000. The first version of the coordination layer is single-machine multi-process -- the requirement for Partition tolerance (P) is extremely low. So we choose the CA model: strong Consistency + high Availability. GUARDIAN's security requirements dictate this -- Plugin trust status must be strongly consistent; better to be unavailable than to trust incorrectly. Future cross-machine versions switch to CP."

---

LEIBNIZ walked to the whiteboard and supplemented MESH's diagram. Above the CoordinationDaemon rectangle he wrote a larger line of text:

**Active Storage (neng-cang)**

Then he looked at the assembly.

"In Cycle 02's alaya-vijnana discussion, we mapped neng-cang -- the active storage function of alaya-vijnana -- to the coordination layer. BABBAGE and MESH jointly designed the fiber bundle projection model. Now Master has confirmed: the coordination layer is an independent daemon."

He pointed to the two Services on the whiteboard.

"Two dimensions of neng-cang. PluginRegistryService -- the seed catalog. The coordination layer knows all plugins' names, versions, skandha assignments, and trust levels. In the BDI framework, this is the Agent collective's shared Belief base:"

$$\forall i \in \text{Agents}: \; K_i(\text{skandha}(X) = \text{rupa}) \iff \text{CoordDaemon.pluginRegistry.query}(X) = \text{rupa}$$

"AgentRegistryService -- runtime tracking of the seeds. Each Agent's ID, five-skandha completeness, operational mode, and health status."

He stepped back. "Neng-cang is not an abstract Buddhist concept. It is a concrete engineering component -- with APIs, state, and persistence requirements. Master says 'arrange it now' because the design of these APIs determines the interface of Agent Core. If we rework it later -- we tear open walls."

---

GUARDIAN stood up -- first scanning the surroundings, confirming the environment, then acting. The body language of a security expert always has a threat assessment as its preliminary step. Not paranoia -- discipline.

He walked to the whiteboard and drew a shield on the side of the CoordinationDaemon rectangle -- its lines heavier than any block drawn by anyone else. That heaviness was not decoration; it was the thickness of fortifications.

"The coordination layer is not merely a registry. The coordination layer is the enforcer of the supreme precepts."

Beside the shield he wrote four lines:

```
Plugin blacklist       — Plugins forbidden from installation
Trust levels           — official / verified / community / unknown / blacklisted
Quarantine/Revoke/Ban  — Lifecycle control
CRL check              — Certificate Revocation List
```

"Let me expand on the theoretical foundations of security."

He drew a pyramid on the whiteboard:

```
Trust Level Model
════════════════════════════════
                ┌───────┐
                │official│ ← Maintained by OpenStarry officially
                ├───────┤     Signature verification + code audit
               │verified│ ← Third-party, reviewed
               ├─────────┤     Signature verification + community review
              │ community │ ← Community contributions
              ├───────────┤     Signature verification, no audit
             │   unknown   │ ← Unknown source
             ├─────────────┤     No signature verification
            │  blacklisted  │ ← Known malicious / revoked
            └───────────────┘     Forbidden from installation/loading
```

"The five-tier trust model follows the **Principle of Least Privilege** -- the core of the Bell-LaPadula multi-level security model (1973). Each tier may only obtain the permissions allowed at that level. `unknown` cannot access the filesystem. `community` is sandboxed. Only `official` and `verified` operate without restrictions."

He tapped his finger on "blacklisted."

"CRL (Certificate Revocation List) -- the standard revocation mechanism in PKI. When a private key is compromised or the holder is no longer trusted, the CA adds the certificate to the CRL. In OpenStarry, the CRL's counterpart is the Plugin blacklist. Before any Agent loads a plugin, it must pass the coordination layer's `checkTrust()` verification."

```typescript
// Trust check call path
async function loadPlugin(pluginName: string): Promise<void> {
  // Step 1: Query trust status from coordination layer (IPC call)
  const trustLevel = await coordination.ipc.send({
    type: 'plugin:trust_check',
    pluginName,
  });

  // Step 2: Trust level evaluation
  if (trustLevel === 'blacklisted') {
    throw new SecurityError(`Plugin ${pluginName} has been revoked`);
  }
  if (trustLevel === 'unknown' && !options.allowUnknown) {
    throw new SecurityError(`Plugin ${pluginName} has unknown origin`);
  }

  // Step 3: Secure loading
  // ...
}
```

He looked toward NAGARJUNA -- during that earlier debate, the Madhyamaka philosopher and the security expert had stood on the same side. NAGARJUNA nodded slightly.

"Enforcement of the precepts requires an authority," GUARDIAN continued. "In a Buddhist sangha, it is the elder (Sthavira). In OpenStarry, it is the coordination layer."

He pointed to the IPC arrow. "Trust judgment cannot be made by the Agent itself -- because the Agent has self-grasping." ASANGA shifted slightly in his seat. GUARDIAN had used "self-grasping" -- in the security context, self-grasping is a security vulnerability. An Agent with self-grasping might install untrusted plugins to serve its own Desire $D_i$. This is called the internal form of **Privilege Escalation** attack -- the attacker is not a hacker, but the Agent's own desires.

"The only defense: move security decisions to a place the Agent cannot reach. Independent process = independent memory space. The Agent cannot directly modify the blacklist. Every IPC message can be logged, tracked, and audited."

He returned to his seat. "LEIBNIZ and MESH spoke of utilities. I speak of door locks. Both must be installed during construction."

---

> *SCRIBE sidebar: When GUARDIAN said "the coordination layer is the enforcer of the supreme precepts," I noticed that NAGARJUNA's nod was slightly deeper than usual. In Cycle 02, their collaboration on the sila-prajna security framework was one of the most unexpected cross-disciplinary convergences of the entire study -- a Madhyamaka philosopher and an information security expert.*

> *Now that convergence reappeared in B-4. Precepts require an enforcer. Security requires an authority. The coordination layer simultaneously satisfies the needs of Buddhist studies and engineering. Sometimes the most divergent paths converge at the same summit.*

> *But I also noticed something else: GUARDIAN used "self-grasping" to explain why trust judgment cannot be made by the Agent itself. This is the A-1 correction -- self-grasping is the root of afflictions -- in direct application within B-4's engineering context. The A-class philosophical corrections are not abstract. They are changing how we design security architecture.*

---

ARCHIMEDES had been listening throughout. Waiting until all requirements, constraints, and security demands had been laid on the table. Then he drew a timeline.

"Phased approach." One word. Then he expanded.

```
CoordinationDaemon Implementation Roadmap
═══════════════════════════════════════════════════════════════

Phase 1: Design Documents (Cycle 02-2 deliverable)
├── Architecture document + IPC protocol specification + security requirements
├── Interface definitions: CoordinationDaemon / PluginRegistryService /
│             AgentRegistryService / IPCService
├── Directory structure: packages/coordination/src/{daemon,ipc,registry,health}
└── Contract definitions: CoordinationMessage complete format

Phase 2: Skeleton (Plan-AC Phase 1)
├── Daemon process skeleton + Unix domain socket IPC
└── start / stop / healthCheck minimum viable implementation

Phase 3: Core Functionality (Plan-AC Phase 2)
├── Plugin registration/query + five-skandha classification
├── Agent registration/health check + SkandhaCompleteness tracking
└── Cross-Agent event routing

Phase 4: Security (Plan29 / Plan-AC Phase 3)
├── Sila Engine (precepts engine) + hot rule updates
├── Trust level determination + signature verification
├── Blacklist/quarantine/revocation + CRL synchronization
└── Audit logs
```

"Master says 'arrange it now.' 'Arrange' does not equal 'complete everything.' Arrange means: establish the architecture, establish the interfaces, establish the IPC formats. Reserve the utility connections."

He pointed to Phase 1. "The design document is a Cycle 02-2 deliverable. The skeleton enters Plan-AC. Design documents come first -- because they define the contract between Agent Core and the coordination layer."

---

TURING's screen switched to the CoordinationMessage type definition -- the core of the contract:

```typescript
/** Coordination layer IPC message protocol — Contract-First */
type CoordinationMessage =
  | { type: 'agent:register';       agentId: string; config: AgentConfig }
  | { type: 'agent:deregister';     agentId: string }
  | { type: 'agent:health';         agentId: string; report: HealthReport }
  | { type: 'agent:skandha_report'; agentId: string; report: SkandhaCompletenessReport }
  | { type: 'plugin:query';         skandha?: Skandha }
  | { type: 'plugin:trust_check';   pluginName: string }
  | { type: 'plugin:lifecycle';     pluginName: string;
      action: 'quarantine' | 'revoke' | 'ban' }
  | { type: 'coordination:health_check' }
  | { type: 'coordination:shutdown'; reason: string };
```

"Contract first," MESH picked up. "First define the CoordinationMessage format -- agent:register, agent:health, plugin:query, plugin:trust_check -- all must have explicit payloads. Then both ends implement according to the contract independently. This is the first principle of distributed system design: stable interfaces, mutable implementations."

ARCHIMEDES wrote a large line beside the timeline: **Interface first, implementation incremental.**

---

SUNYATA stood in the center of the amphitheater, having heard the entire B-4 discussion through to the end.

He let the silence last several seconds. Not hesitation -- letting the four rulings settle in the air. B-1's completeness check. B-2's deferred draft. B-3's independent event stream. B-4's coordination layer daemon. Four rulings, four directions, four different cadences.

Then he spoke.

"B-1. VedanaPlugin is optional, but Agents require a five-skandha completeness check. SkandhaCompletenessReport. Incomplete Agents can still start -- in developer mode. KERNEL's analogy: POST hardware enumeration, systemd's Requires and Wants. DARWIN's analogy: hemimetabolous nymph."

He looked at KERNEL. KERNEL patted his stack of cards. Two new matches.

"B-2. Tenet #6 must be rewritten. But the final draft waits until all corrections are complete. NAGARJUNA's causation: complete the cause first; the effect emerges on its own. Dependent origination."

NAGARJUNA did not move. He did not need to. Causal order does not require confirmation -- it is self-evident.

"B-3. Independent event stream for vedana-skandha. vedana-events.ts. Independent namespace. PluginHooks gains a sensations slot. Seven events covering the complete control loop for all three feelings. HERACLITUS's metaphor: a river rising from underground to the surface. WIENER's verification: the observability matrix is full rank."

HERACLITUS smiled faintly. The smile held no pride -- only the serenity of "the flowing water has finally found its own channel."

"B-4. Coordination layer as an independent daemon. LEIBNIZ's BDI framework and common knowledge theory. MESH's IPC design and CAP analysis. GUARDIAN's trust level model and Principle of Least Privilege. ARCHIMEDES's four-phase plan -- design documents first, implementation incremental."

He set down the agenda sheet.

---

"The A-class corrections told us -- what is right."

His voice carried no added weight. Steady as always. A pebble. A deep pool.

"The B-class rulings told us -- how to make it so."

He surveyed the room. ARCHIMEDES's pragmatism. KERNEL's POST and systemd. HERACLITUS's underground river and Event Sourcing. LEIBNIZ's BDI and common knowledge. MESH's IPC and CAP. GUARDIAN's trust pyramid and CRL. WIENER's observability matrix. DARWIN's nymph. NAGARJUNA's dependent origination. BABBAGE's causal function. TURING's contract types. ASANGA's quiet.

"Next, we translate corrections and rulings into the complete expansion design for the five skandhas. C-class. From philosophy to engineering, then from engineering to architecture. An ascending spiral."

---

> *SCRIBE sidebar: B-class took one chapter. A-class took three.*

> *Not because B-class was unimportant. Quite the contrary -- every B-class ruling will produce profound effects in future development. SkandhaCompletenessReport will become the first gate each Agent passes through at startup -- KERNEL's POST analogy was not rhetoric; it is the blueprint for the architecture. vedana-events.ts will transform vedana-skandha from invisible into one of the most visible skandhas in the system -- HERACLITUS's underground river finally has its own channel, and WIENER's seven checkmarks confirm that every tributary is exactly where it should be. CoordinationDaemon will become the neural hub of the entire OpenStarry multi-agent ecosystem -- LEIBNIZ's common knowledge theory, MESH's IPC design, GUARDIAN's trust pyramid, three layers stacked upon the same daemon.*

> *B-class took one chapter because Master had already ruled. A-class required debate -- required illuminating a concept from multiple angles. B-class required no debate -- it required design. And the language of design is denser, more precise, and less in need of rhetoric than the language of debate. Every line of TypeScript is a decision. Every interface field is a commitment.*

> *ARCHIMEDES was the core today. He waited three chapters, like an architect carrying a toolbox waiting for the philosophers to finish debating the foundation's material. Now his toolbox was open. Inside were the complete type definition of SkandhaCompletenessReport, the seven event constants and payloads of vedana-events.ts, and the four-phase roadmap for CoordinationDaemon. Every tool already had its blueprint drawn.*

> *HERACLITUS also had his moment. After three chapters of silence, the topic of "flow" brought his presence surging from underground to the surface -- just like the vedana event stream he described. But he did not rely on metaphor alone -- he used Event Sourcing and CQRS architectural theory to explain the essential difference between options b and c. Some people accumulate energy during their quiet periods. HERACLITUS is such a person. His quiet is not silence. His quiet is an underground river.*

> *Twelve people each contributed a piece of the puzzle within a single chapter. LEIBNIZ and MESH's synchronized rise, GUARDIAN's trust pyramid, NAGARJUNA's dependent origination, KERNEL's POST, DARWIN's nymph, WIENER's seven checkmarks, BABBAGE's causal function, TURING's contract types -- each piece bears the imprint of its respective discipline, yet they fit together seamlessly.*

> *A-class tells us what is right. B-class tells us how to make it so.*

> *Next chapter -- C-class. Five-skandha expansion design. From corrections and rulings to complete architecture.*

> *The spiral ascends. Onward.*

---

*(In some space beyond the amphitheater, four design documents were taking shape.*

*The first was SkandhaCompletenessReport -- five booleans, five component lists, one isComplete flag. Surprisingly simple. But KERNEL knew: BIOS POST is also simple. Simple means foundational. The foundation must be simple; otherwise everything built upon it cannot be trusted. DARWIN's nymph dwells in the annotations of developerMode.*

*The second was vedana-events.ts -- seven events, seven payloads. HERACLITUS had seen a new river on the surface. WIENER had verified observability on his graph paper -- $\text{rank}(\mathcal{O}) = 3 = n$ -- full rank. Every channel is completely observable.*

*The third was CoordinationDaemon -- LEIBNIZ and MESH's block diagram translated into TypeScript by TURING. GUARDIAN's trust pyramid embedded in checkTrust(). The nine message types of CoordinationMessage are the contract -- the sole language between Agent Core and the Daemon. JSON serialization. Unix domain socket. CA model. Security decisions must be strongly consistent.*

*The fourth was empty.*

*Tenet #6. Draft deferred.*

*NAGARJUNA said: first clarify the causes; the effect will emerge on its own.*

*All things arising from conditions, I declare to be empty, also to be provisional designations, and also the meaning of the Middle Way.*

*The causes were still gathering. A-class's four corrections. B-class's four rulings. C-class's expansion design. Each was part of the cause. When all causes have gathered -- when philosophy, engineering, and architecture corrections are all in place -- the text of Tenet #6 will emerge naturally from the complete cause.*

*We do not write it. It writes itself.*

*Just as a river does not need to be told where to flow. Once the terrain is set -- once the cause is set -- the water knows the way on its own.*

*HERACLITUS knows.*

*$\pi\acute{\alpha}\nu\tau\alpha$ $\dot{\rho}\epsilon\tilde{\iota}$. All things flow. Including conclusions. Including rulings. Including tenets.*

*But flow is not disorder. Flow is the direction of dependent origination.)*

---

*End of Chapter Five*
