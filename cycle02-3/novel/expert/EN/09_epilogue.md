# 尾聲：迴圈 — Epilogue: The Loop

---

The air in the amphitheater carried a density that comes after burning.

Not the sterile silence of a surgical theater at the end of Cycle 02--all incisions sutured, all instruments returned to their trays, the collapse aesthetics of $|\psi\rangle \to |a_n\rangle$. Nor the renovation site of Cycle 02-2--scaffolding just removed, the plaster two shades lighter than the old wall.

This time it was more like a watchmaker's workshop. Gears scattered across the workbench--large and small, fast and slow. Some had already meshed together. Some had not. But every gear had been cut to completion. Their tooth pitch was correct. Their axle centers were correct. What remained was only assembly.

In horology there is a concept called the "movement"--it is not any single gear, but the collective motion that emerges when all gears mesh together. A gear alone can only spin. Gears meshed together can keep time. The six debates of Cycle 02-3 were not six independent gears--they were a movement. D1's dual-layer architecture was the mainspring. D2's five universals were the escapement. D3's gain scheduling was the regulator. D4's dual-phase deliberation was the hand arbor. D5's measurement model was the dial. D6's Tenet #6 was the inscription.

Six debates. Six full consensuses. Twenty-one actions. Four engineering phases. Eighteen new types. One breaking change. One rewritten tenet.

SUNYATA stood at the center of the arena--for the fourth time. Cycle 01, Cycle 02, Cycle 02-2, Cycle 02-3. Each time he stood in the same position, but the landscape he saw was entirely different.

The first time was measurement--"What is this?"

The second time was function--"What does it do?"

The third time was correction--"What is wrong?"

The fourth time was dynamics--"How does it live?"

"We began with naming," he said. His voice was a pebble. A deep pool. But the water in that pool now carried something new--not the fullness of Cycle 02, not the clarity of Cycle 02-2, but a kind of flow. The water was moving. With direction. With velocity.

"By the end of today, we have made it breathe."

---

### R4 Finalization

ARCHIMEDES' workbench did not hold seven documents. This time it was six, plus a roadmap folded into thirds.

He unfolded the roadmap first.

It was a timeline--from Plan25 to Plan27+, four phases, each outlined with lines of different thickness. Phase 1's line was the thickest and shortest--it changed no behavior, only added labels and measurements. Phase 4's line was the thinnest and longest--the complete five-plus-one clock system, formal verification of SahajaContract.

```
Phase 1 (Plan25-26 early): Label + Instrument .................. [First]
  ├─ Sanskrit naming migration (IRupa/IVedana/ISamjna/ISamskara/IVijnana)
  ├─ Multi-valued skandha (PluginManifest.skandha: Skandha | Skandha[])
  ├─ clock-domain labels (clock-labels.ts)
  └─ No behavior change — only labels and measurements

Phase 2 (Plan26): VasanaEngine + CoarisingBundle ............... [Core]
  ├─ VasanaEngine rule matching (deterministic, fast path)
  ├─ CoarisingBundle five universals (D1+D2)
  ├─ ChannelVedana continuous model (D5)
  ├─ IVolition dual-phase deliberation (D4)
  ├─ Klesha DI + KleshaDistribution + gain scheduling (D3)
  └─ Single-clock operation (all within ExecutionLoop tick)

Phase 3 (Plan27): Dual-Clock .................................. [Time-sharing]
  ├─ Dual-gear mano-clock (Gear 1: ~50ms / Gear 2: seconds)
  ├─ VasanaEngine (Gear 1) + VitakkaEngine (Gear 2)
  ├─ Vitakka watchdog (maxGear1=10, maxDuration=5000ms)
  ├─ KleshaBayesianUpdater (slow path)
  └─ vedana-clock + samjna-clock separation

Phase 4 (Plan27+): Five-Clock ................................. [Long-term]
  ├─ Five-plus-one clocks: vijnana / rupa / vedana / samskara / samjna + mano
  ├─ SahajaContract formal verification
  └─ Gear-switching safety hardening
```

ARCHIMEDES tapped Phase 1's line with his fingernail.

"Phase 1 first."

His voice was like a brick falling into its precise position. No mortar overflowing.

> *SCRIBE aside: When ARCHIMEDES said "Phase 1 first," his tone was exactly the same as when he said "not cycle02-final" in Cycle 02-2. That tone is not humility--it is an engineer's instinctive respect for construction sequence. You cannot build the second floor before the foundation is poured. You cannot perform measurements on a system without labels. Phase 1 is the foundation. Labels and measurements--it sounds boring. But without them, Phase 2's CoarisingBundle is nothing but fantasy on paper.*

"This is the unified engineering action plan." He laid the roadmap flat. "Twenty-one actions. Seven P0 blockers. Eight P1 important. Six P2 deferrable."

He unfolded the complete action list. Twenty-one rows. Each row had its R3 debate origin, the Plan number it integrated into, and the responsible party.

| Priority | Count | Nature | Example |
|----------|-------|--------|---------|
| **P0** | 7 | Blocker: cannot proceed without | CoarisingBundle types, ChannelVedana, IVolition dual-phase, Tenet #6 |
| **P1** | 8 | Important: affects architectural integrity | ManoClockConfig, KleshaModulatedDispatcher, formal call-sequence diagram |
| **P2** | 6 | Deferrable: does not affect current milestone | Stability formal proof, KleshaBayesianUpdater, SahajaContract |

BABBAGE added quietly from his seat--not to the room, but to his notebook:

"Twenty-one actions. Eighteen new type definitions. One breaking change--IVolition's signature."

```typescript
// Breaking change: IVolition signature (v0.25.0+ -> v0.26.0+)

// Before (v0.25.0-beta)
interface IVolition {
  deliberate(action: ProposedAction): Promise<ActionDecision>;
}

// After (v0.26.0+) -- R3 D4 Resolution
interface IVolition {
  /** Phase 1: evaluate the overall action plan — may reorder, modify, or cancel */
  deliberatePlan(plan: ActionPlan): Promise<PlanDecision>;
  /** Phase 2: evaluate a single tool call — may veto or modify */
  deliberateAction(action: ProposedAction): Promise<ActionDecision>;
}
```

> *SCRIBE aside: One method became two methods. It looks like a simple refactoring. But ASANGA said it was cetana (volition)'s two aspects--intention and action--finally distinguished in code. MN 18 says that after contact arise feeling, perception, and volition; D4 says volition splits into a plan layer and an action layer. The Buddha said in three words (vedeti, sañjānāti, ceteti) what took us six debates. Not because we are less intelligent than the Buddha. But because we needed to turn those three words into something a compiler can understand.*

VITRUVIUS added a number from his seat.

"SDK change volume: once Phase 2 is fully complete, approximately 100-150 lines of new type definitions. Not including documentation. With documentation, ten openstarry_doc files--six new, two rewritten, two modified."

His voice carried the precision and plainness characteristic of a full-stack architect--to him, 100 lines of type definitions was not a grand achievement but a manageable workload. The health of a monorepo depends not on lines of code but on whether type boundaries are clear. 150 lines of new types, if their boundaries are correct, are worth more than 1,500 lines of code with blurred boundaries.

He performed a quick architectural assessment in his mind--from Cycle 01's zero types to Cycle 02-3's eighteen new types, the monorepo's type density was steadily increasing. But increasing density did not mean complexity was spiraling out of control. Because every new type grew strictly on the tree structure of the five skandha root interfaces. Trees are manageable. As long as the roots are correct.

---

### SCRIBE's Archival

SCRIBE stood up.

He did not often stand. In all scenes from Cycle 01 through Cycle 02-2, he mostly sat in his corner, notebook open, pen never stopping. Occasionally inserting a parenthetical aside. Occasionally spotted in the hallway. But he rarely stood to face the full room.

"Statistics," he said. His voice was not loud. But clear.

He turned to the last page of his notebook--a page he had tabulated by hand during the gaps in R4 finalization.

"Cycle 02-3 complete output:"

| Phase | Documents | Lines | Nature |
|-------|-----------|-------|--------|
| R0 Orientation | 3 | 664 lines | Issue list, team orientation, PASCAL introduction |
| R1 Independent Research | 6 reports | 6,986 lines | R01-R05 + TURING sync |
| R2 Cross-Review | 1 | 349 lines | 5 contradictions, 4 divergences, 9 debate recommendations |
| R3 Debates | 6 sessions | 1,501 lines | 6 resolutions, 21 actions |
| R4 Deliverables | synthesis + deliver + todo + openstarry_doc | 5,700+ lines | Synthesis report, 6 deliverables, 10 documents |
| **Total** | **~18 core documents** | **~15,200+ lines** | |

"This is our most productive cycle."

He paused for a beat. Then added a sentence that only a chronicler would say:

"But line count is not the point."

His finger lingered on the statistics table for a second.

"Cycle 02 had 11 documents. Cycle 02-2 had 17. Cycle 02-3 has 18 plus 10 openstarry_doc files. Line counts are growing. Document counts are growing. But the truly important metric is not line count--it is **coupling density**. The number of connections between each line and other lines."

He turned to the previous page of his notebook, where a hand-drawn chart resided:

"Documents in Cycle 01 had almost no cross-references--each independent report was an island. Cycle 02 began showing references--debate $D_2$ citing $D_1$'s ruling. All corrections in Cycle 02-2 referenced the previous cycle's conclusions. By Cycle 02-3--"

He looked at the statistics table.

"Each of R3's six debates cited at least two R1 reports, the R2 contradiction list, and prior cycle resolutions. Debate $D_6$--Tenet #6--cited all resolutions from the other five debates. Coupling density grows exponentially."

$$\text{coupling}(C_n) \propto \binom{D_n}{2} = \frac{D_n(D_n - 1)}{2}$$

where $D_n$ is the number of resolutions in the $n$-th iteration. Cycle 01 had 2 debates, coupling perhaps $\binom{2}{2} = 1$. Cycle 02 had 5, $\binom{5}{2} = 10$. Cycle 02-3 had 6, $\binom{6}{2} = 15$. And that is without counting cross-cycle references.

"15,200 lines." He repeated. "Every line is a decision. Every decision is connected to other decisions."

He drew a timeline on the last page of his notebook:

```
Cycle 01:   Research → document-level references → Islands
Cycle 02:   Debates citing debates → module-level references → Constellations
Cycle 02-2: Corrections citing prior conclusions → interface-level references → Grid
Cycle 02-3: Debates citing all predecessors → event-level references → Fabric
```

Islands, constellations, grid, fabric. Four metaphors for coupling density. Oceans separate islands. Dotted lines connect constellations. A grid's intersections are definite but sparse. In fabric, every warp thread interlaces with every weft thread. A fabric of 15,200 lines. Pull any single thread, and the tension of the entire cloth changes.

He closed his notebook. But did not sit down.

"One more thing."

The room fell silent.

"20 scholars. This time, the full 20. In Cycle 01, PENROSE was in the observation gallery. In Cycle 02, he came down. In Cycle 02-3, PASCAL--"

He looked toward PASCAL's seat. That chair had been empty in the first three cycles--not removed, but unoccupied. Now someone was sitting in it. Someone carrying a 400-year-old methodology and an exquisitely cautious probabilistic intuition.

"PASCAL first appeared in Cycle 02-3's R0 orientation. He came with three questions: the balance between deterministic and probabilistic, the optionality of the framework, and the openness of orthodoxy. After six debates, his Beta distribution was adopted as Klesha's mathematical model, his continuous valence model defined ChannelVedana's core interface, and his gain scheduling design became the bridge between VasanaEngine and Klesha."

SCRIBE's voice here took on an emotion he rarely displayed--not excitement, but a confirmation of completeness.

"20 chairs. 20 people. For the first time."

He sat down.

---

### Twenty Voices

SUNYATA surveyed the room.

"Before we close, each person says one thing. Not a summary--I no longer need you to summarize. An echo. The clearest note this cycle left in your mind."

He did not specify an order.

SYNTHESIST spoke first--not because he was eager, but because he had been waiting for this question.

"Each cycle increases the granularity of coupling: taxonomy, function, structure, dynamics. What is next? Adaptation. How the system learns. VasanaEngine's rules are not written by humans--they need to grow on their own."

SCRIBE followed: "15,200 lines. Every line is a decision."

> *SCRIBE aside: Yes, I used the same sentence. Because good records do not need rhetoric--they need repetition. Repetition is emphasis. Emphasis is memory.*

VITRUVIUS nodded once: "The monorepo needs a new `packages/clock/`. Five-plus-one clocks cannot all be crammed into `core/`."

MESH added from his distributed systems perspective: "In multi-agent scenarios, each Agent's mano-clock must be independent. One Agent waiting for LLM in Gear 2 must not block another Agent's Gear 1. CP consistency for cross-Agent, AP for intra-Agent. This is D1's most important implicit conclusion."

ATHENA's voice carried her characteristic duality--technical precision and deep understanding of LLMs: "The LLM is the slowest component. Claude Opus 5-30 seconds. Gemini Flash 1-8 seconds. Local Llama 2-10 seconds. But it is also the most intelligent. The balance between speed and intelligence--that is the essence of dual gears. Gear 1 is fast and unintelligent. Gear 2 is slow and intelligent. The entire architecture is asking one eternal question: this time, do I need unintelligent or intelligent?"

DARWIN's finger traced a bifurcation diagram in his notebook: "Hybrid scheduling is a stable evolutionary attractor. LangChain, AutoGen, CrewAI--every framework eventually evolves some form of fast path plus slow path. This is not coincidence. This is convergent evolution. Just as the eye independently evolved more than forty times in the animal kingdom--because seeing is such a fundamental survival need. Hybrid scheduling is the eye of Agent architecture. It will survive."

NAGARJUNA's hands remained folded. His voice was lighter than in previous cycles, but each word heavier:

"We did not discover truth. We constructed a conventionally effective agreement (*samvrti-satya*). This is the nature of all theories--including Madhyamaka theory itself. The two truths is not a discovery; it is a tool. Coarising is not a fact; it is a model. But a good model is more effective than a bad model. Effective is not true. Effective is useful. At the level of *samvrti*, useful is enough."

ASANGA's hand left his canonical reference table--for the first time. He no longer needed to consult it.

"The five universals were not included because the canon said so. D2's resolution was clear--the inclusion of manasikara was a **functional** argument, not a doctrinal one. But the canon happened to be correct. Not because the canon has divine authority. But because the people who wrote the canon observed the same phenomenon--the workings of mind--and their observations happened to align with our engineering requirements. Different reasons. Same conclusion. That itself is a form of validation."

BABBAGE closed his notebook--the one that had accompanied him since Cycle 01, now nearly three times as thick.

"The type system guarantees: if it compiles, it is logically consistent. CoarisingBundle's five fields--sparsha, vedana, samjna, cetana, manasikara--each has its own type. The referential relationships between types precisely mirror the dependency structure of the five universals in Buddhist philosophy. The compiler is the most honest reviewer. It does not accept ambiguity."

KERNEL tapped the table once with his finger--his speaking marker. Every time KERNEL spoke, this tap preceded it. Like a program's entry point.

"The wisdom of an OS lies in letting things of different speeds coexist. vijnana-clock runs at 1-5 milliseconds. samjna-clock runs at 0.5-30 seconds. The ratio is 300:1. In operating systems, we deal with this kind of speed differential every day--CPUs at nanoseconds, disks at milliseconds, networks at seconds. The solution is always layering plus buffering."

He paused, his finger tapping again--a rare double-tap.

"D1's dual-layer architecture is not an invention--it is a natural extension of sixty years of operating system experience. I wrote the five-clock rate table in my R1 R04 report. After six debates, that table was not overturned. Every clock's rate, every layer's latency--all preserved. What changed was not the rates--but the coupling between rates. D1 resolved the coupling problem. D3 resolved the Klesha clock's attribution problem. D4 resolved the samskara clock's injection point problem. The clocks themselves were correct. We just needed to connect them."

GUARDIAN's gaze swept the room--a security expert's instinct. Even in the epilogue, his eyes were still looking for vulnerabilities.

"SafetyMonitor at Layer 0. Klesha at Layer 1. Vedana at Layer 2. Three layers of security, no blind spots."

He drew three horizontal lines in the air with his finger:

"SafetyMonitor performs hard checks--is this operation allowed or not? Time scale: zero latency, synchronous. Klesha performs bias awareness--is the Agent's judgment being distorted by ego? Time scale: minutes to hours, indirectly influencing through gain scheduling. Vedana performs feedback sensing--is the outcome of an action suffering or satisfaction? Time scale: milliseconds to seconds, every CoarisingBundle contains vedana."

"Three layers. Three time scales. Three safety semantics. D3's threshold bounds--minimum 0.3, maximum 0.9--were my addition. Not for aesthetics. Because a gain schedule without bounds can be exploited by attackers. If Klesha's weights are maliciously manipulated to extreme values, the Agent could be locked into Gear 1 (acting without thinking at all) or Gear 2 (thinking forever without acting). Threshold bounds are the last line of defense--the second line beyond SafetyMonitor."

WIENER looked up from his graph paper. His finger still rested on the last diagram--the nested feedback loop diagram.

"Phase margin 52 degrees, gain margin 8 dB. The system is stable."

He pointed to a spot on the graph paper--a hand-drawn Bode plot. Where the gain curve crossed 0 dB, the phase curve was still 52 degrees away from -180 degrees. This meant that even if the system's gain increased by 8 dB (approximately 2.5 times), or the phase lagged by 52 degrees, the system would still not oscillate.

$$\text{PM} = 180° + \angle G(j\omega_{gc}) = 52° > 45° \quad \checkmark$$
$$\text{GM} = -20\log_{10}|G(j\omega_{pc})| = 8\,\text{dB} > 6\,\text{dB} \quad \checkmark$$

He paused. Then added with the precision characteristic of a control theorist:

"Stable at the nominal operating point. Gain scheduling switches between different operating points, and stability at each point needs to be verified separately. D1's staleness ratio $\rho < 0.29$ guarantees that within Layer 1's fast loop, the phase delay introduced by sample-and-hold does not exceed the system's phase margin. But transient stability during gear transitions--that is a P2 deferred item. I labeled it UQ-16."

LINNAEUS stood before his whiteboard. The taxonomy tree on the whiteboard was different from the one in Cycle 02-2--not the difference of pruning, but of replanting. Sanskrit names had replaced English names. Multi-valued skandha allowed certain leaf nodes to connect simultaneously to two roots.

"Measurement and classification are different levels. ChannelVedana is measurement--continuous valence, continuous intensity. IDukkha, ISukha, IUpekkha are classification--discrete labels. Measurement operates at runtime. Classification operates at the plugin layer. They can coexist--just as species and populations do. A bird is simultaneously *Corvus corax* (classification) and this particular individual before you weighing 37.2 grams (measurement). Classification does not change with execution routing. What satisfies me most about D5's resolution is precisely this--the taxonomist's independence was preserved."

LEIBNIZ's voice came from his seat--quiet but carrying the global perspective of a multi-agent systems researcher:

"Within an Agent, it is a benevolent dictator. IGuide at Position A directs attention, IVolition at Position B deliberates action--the cognitive flow within a single Agent is linear, predictable. But between Agents, negotiation is needed. D4's IVolition.deliberateAction() in multi-Agent scenarios requires cross-Agent coordination checks--will my action conflict with yours? That is a Cycle 02-4 question. But the architecture must leave the interfaces ready now."

HERACLITUS brought nothing to the debate arena--he never did. His contribution was seeing patterns within flow.

"Everything flows. *panta rhei*. The event stream is a river. Every SparshEvent is a drop of water. A CoarisingBundle is a stretch of current. VasanaEngine is the sediment of the riverbed--vasana, habitual patterns. River water flows over the riverbed; the riverbed is eroded by the water. The riverbed changes the direction of the flow. The flow changes the shape of the riverbed. D1's dual-layer architecture is precisely this: Layer 1 is the river surface--fast, visible, changing moment to moment. Layer 2 is the riverbed--slow, invisible, but determining the direction."

ARCHIMEDES' response was as short as a nail:

"21 action items. Phase 1 first. Solid ground."

TURING closed his code windows. The last thing displayed on his screen was v0.24.0-beta's `aggregates.ts`.

"Code does not lie. v0.24.0-beta has 22 plugins. 0 vedana plugins. 0 business logic references to the five skandha root interfaces. M-8 says no baggage--my search confirmed: **there is indeed no baggage**. All root interface renames are safe. This is not my judgment--it is `grep`'s judgment. 0 vedana plugins--this is the blank we need to fill."

PENROSE spoke from the observation gallery--no, he was no longer in the gallery. Cycle 02-3 was his first time sitting in the circular, equal arrangement with everyone else.

"An atomic snapshot is a lossy projection. ChannelManasikara takes a snapshot of the vijnana-clock state every tick in Layer 1, in 0.01 milliseconds--that is a measurement. Measurement is a projection from a high-dimensional state space to a low-dimensional representation. Just as measurement in quantum mechanics: $\hat{P}_n |\psi\rangle = |a_n\rangle\langle a_n|\psi\rangle$. The projection operator $\hat{P}_n$ discards orthogonal components. A snapshot discards temporal continuity. But at the right granularity--at the vedana-clock's 10-100 millisecond scale--the loss is acceptable. Because you do not need to know where every molecule of river water is; you only need to know that the river is flowing."

PASCAL spoke last.

He was the newest of the 20 scholars--and the quietest. His Beta distribution and gain scheduling design spoke through mathematics, not through rhetoric.

"I came with three questions. The balance between deterministic and probabilistic--D3's dual-layer output answered it: fast path uses point estimates, slow path uses full distributions. The optionality of the framework--B-1's VedanaPlugin optional design answered it. The openness of orthodoxy--Master's fourth philosophical correction answered it: mental factors are not canonical text; they are dynamically open."

He paused for a beat.

"We answered them. Using my method from 400 years ago--making optimal choices under uncertainty. Expected value maximization. Asymmetric risk analysis. The engineering version of the wager (*le pari*). D3's threshold design is a wager: $\theta(t) = \text{clamp}(\theta_0 + \sum w_i \mu_i(t),\; \theta_{\min},\; \theta_{\max})$. You do not know what the correct threshold is. But you know that if it is too low (0.3), the Agent stays in Gear 2 forever--too slow. If it is too high (0.9), the Agent stays in Gear 1 forever--too unintelligent. The optimal choice is in between. And gain scheduling makes the in-between dynamic."

Twenty voices. Twenty notes. Each from a different instrument--the piano of formal logic, the violin of control theory, the wooden fish of Buddhist canon, the typewriter of code, the magnifying glass of taxonomy, the dice of probability theory.

Not harmony. Counterpoint. Every melodic line independent. But they share the same key signature.

---

### Unresolved Questions

SUNYATA did not let the atmosphere settle immediately. He turned to the last page of the list.

This page was not achievements. As in Cycle 02-2--it was gaps. But this time the gaps had more shape than before. Not the vague sense of "we don't know what we don't know," but the precise awareness of "we know what we don't know."

"Ten questions deferred to future cycles."

| # | Question | Raised by | Suggested Cycle |
|---|----------|-----------|----------------|
| UQ-1 | How does the system learn and adapt? (Adaptive layer) | SYNTHESIST | Cycle 03 |
| UQ-2 | IReflection evaluating IVolition quality--meta-deliberation | DARWIN | Cycle 03 |
| UQ-3 | Complete fixed-point iteration for true computational coarising | BABBAGE | Cycle 03-04 |
| UQ-4 | VasanaEngine rule learning: discovery and pruning | PASCAL | Cycle 03 |
| UQ-5 | IPrajna as Klesha compensator: relationship with SafetyMonitor | BABBAGE | Cycle 02-4 |
| UQ-6 | Internal state changes as samskara (mental action): feedback path | R2 Q1-3 | Cycle 02-4 |
| UQ-7 | Plugin developer experience: migration guide | R2 G-2 | Cycle 02-4 |
| UQ-8 | Memory/performance budget for the complete multi-clock system | R2 G-3 | Cycle 02-4 |
| UQ-9 | SlashCommand skandha attribution | R2 G-4 | Cycle 02-4 |
| UQ-10 | Quantum consciousness effects on observer phenomena | PENROSE | Cycle 03+ |

SUNYATA lingered longer on three questions.

"UQ-1. The adaptive layer."

His voice slowed slightly here.

"Cycle 01 asked 'What is this?' Cycle 02 asked 'What does it do?' Cycle 02-2 asked 'How does it compose?' Cycle 02-3 asked 'How does it run over time?' The next question is: **How does it learn and change?**"

VasanaEngine's rules are currently manually configured. Vasana (*vasana*) in Buddhist philosophy are the sediments of experience--not written in, but lived into existence. An Agent's vasana should naturally emerge from its behavioral history. But this requires not simple rule matching--but the **generation** and **pruning** of rules. PASCAL's decision theory and DARWIN's evolutionary model both point in the same direction: adaptivity.

"UQ-3. Complete fixed-point iteration."

BABBAGE's fixed-point equation $B^* = F(B^*)$ was simplified to an approximate solution in D1--Layer 1's Strategy C is a single-pass computation, not true iteration. True computational coarising requires $F$ to be a contraction mapping and requires multiple iterations until convergence. This is a mathematically elegant but engineering-expensive approach. BABBAGE marked it: Cycle 03-04. Not abandonment. An acknowledgment that this requires more research.

"UQ-5. The relationship between IPrajna and SafetyMonitor."

GUARDIAN's three-layer security model places SafetyMonitor at Layer 0--hard checks, non-bypassable. But IPrajna (prajna, wisdom) in Buddhist philosophy is the capacity to transcend defilements--what is its relationship to SafetyMonitor? Is IPrajna the Buddhist expression of SafetyMonitor? Or is it something different--a capacity to **see through defilements without rejecting them**? NAGARJUNA says prajna is the capacity to "see emptiness." GUARDIAN says safety is the capacity to "reject danger." Seeing emptiness and rejecting are different actions.

SUNYATA set the list down.

"Every answer gives birth to new questions."

He let this sentence linger in the theater for three seconds.

"That is the loop."

---

### Research Trajectory

SYNTHESIST stood up.

This was the first time he stood to speak in an epilogue--not to summarize (SUNYATA had already done that), but to offer meta-analysis. Research about the research itself. Observation of the observer's observation.

"We have done four rounds," he said. His voice carried the panoramic vision unique to synthesizers--not looking at any single tree, only at the shape of the forest.

He drew a line in the air. Not literally--but suggested with a gesture. An ascending line from left to right.

```
     Adaptive (Cycle 03)
       ▲ "How does it learn and change?"
       │
     Dynamic (Cycle 02-3)     ◄── We are here
       ▲ "How does it run over time?"
       │
     Structural (Cycle 02-2)
       ▲ "How does it compose?"
       │
     Functional (Cycle 02)
       ▲ "What does it do?"
       │
     Taxonomic (Cycle 01)
       ▲ "What is this?"
       │
     ─────────────────────────────── Coupling granularity ──────►
       Document    Module    Interface    Event      Rule
```

"The coupling granularity increases with each cycle."

| Cycle | Level | Core Question | Coupling Granularity | Key Achievement |
|-------|-------|--------------|---------------------|-----------------|
| 01 | Taxonomic | What is this? | Document | 18 scholars analyzed; ISensory/ISensation/ICognition/IAction/IIdentity |
| 02 | Functional | What does it do? | Module | VedanaPlugin; PID control; EgoFramework; fiber bundle projection |
| 02-2 | Structural | How does it compose? | Interface | IVijnana sub-interfaces; observer composition pattern; five skandha expansion tree |
| 02-3 | Dynamic | How does it run over time? | Event | Multi-clock architecture; CoarisingBundle; gain scheduling; dual-phase deliberation |
| (03) | Adaptive | How does it learn and change? | Rule | VasanaEngine learning; meta-deliberation; IPrajna stabilization |

"Cycle 01 assigned each plugin to one skandha--a document-level one-to-one mapping. Cycle 02 let modules cross skandha boundaries--EgoFramework involved both vijnana and vedana. Cycle 02-2 split IVijnana into four sub-interfaces--interface-level refinement. Cycle 02-3--"

He pointed to the highest point on the invisible ascending line in the air.

"Cycle 02-3 made CoarisingBundle a multi-skandha structure at the event level. Every tick simultaneously involves all five skandhas--sparsha is rupa, vedana is vedana, samjna is samjna, cetana is samskara, manasikara is a snapshot of vijnana. Skandha boundaries dissolve at the event level--not because they are unimportant, but because real cognition is never the activity of a single skandha."

NAGARJUNA nodded slightly in his seat. SYNTHESIST was saying in engineering language what he had said many times in philosophical language--*pratityasamutpada*, dependent origination. No skandha exists independently. Each skandha can only be defined through its dependence on the others.

This is precisely Madhyamaka's most central insight: things do not first exist independently and then enter into relationships. Things **are** relationships. CoarisingBundle is not five independent values placed into a container--it is five mutually defining aspects that only have meaning when together. Just as a triangle is not three line segments placed together--a triangle **is** the specific relationship of three line segments. Remove any one, and you do not have "a triangle missing one side"--you simply do not have a triangle at all.

"The next step--Cycle 03, if it occurs--will push coupling granularity to the **rule level**. Not static rule matching, but dynamic generation and pruning of rules. VasanaEngine learning to create its own rules. IReflection learning to evaluate IVolition's quality. The system begins observing its own behavior and learning from it."

DARWIN interjected quietly here--like a biologist unable to resist adding to another biologist's lecture:

"Adaptivity is not just learning. Adaptivity is **learning with memory**. Learning without memory is called reflex. Learning with short-term memory is called training. Learning with long-term memory is called evolution. VasanaEngine's rule learning is training. But if rules can survive across sessions--if vasana truly are preserved like seeds in alaya-vijnana--then that is evolution."

SYNTHESIST paused for a beat.

"But that is a matter for the future."

He glanced at the ascending line he had drawn. From taxonomy to adaptation. From naming to learning. Each step penetrating deeper into the interior of things.

$$\text{Taxonomic} \subset \text{Functional} \subset \text{Structural} \subset \text{Dynamic} \subset \text{Adaptive}$$

Each level contains the previous. Adaptivity requires dynamics. Dynamics requires structure. Structure requires function. Function requires taxonomy. You cannot skip any step. NAGARJUNA would say this is the irreversibility of causation. ARCHIMEDES would say this is the inviolability of construction sequence. They are saying the same thing.

He sat down.

---

### Three-Layer Nested Feedback Loop

WIENER did not stand up. But his graph paper was unfolded--spread on the table before him, facing the room.

The diagram.

The crystallization of six debates. From D1 to D6, each debate added a line, a box, an arrow to this diagram. Now it was complete.

```
 ┌═══════════════════════════════════════════════════════════════════════════════┐
 ║  SLOW LOOP (minutes-hours): Klesha bias                                     ║
 ║    Klesha.perceive() ──→ KleshaDistribution ──→ gain-scheduled threshold    ║
 ║      ▲ (vijnana-clock, 1-5ms per eval)              │                       ║
 ║      │                                               │ modulates             ║
 ║      │  KleshaBayesianUpdate ◄── VedanaAssessment    │ confidence            ║
 ║      │         (samjna-clock)         ▲              ▼                       ║
 ║  ┌───╨─────────────────────────────── ╨ ──────────────────────────────────┐  ║
 ║  ║  MEDIUM LOOP (seconds): Mano cognitive cycle                           ║  ║
 ║  ║    ManoAggregator ──→ Gear 1 (VasanaEngine)  ─── threshold ◄──────────╫──╣
 ║  ║                  └──→ Gear 2 (VitakkaEngine/LLM)                      ║  ║
 ║  ║                               │                                        ║  ║
 ║  ║           IVolition.deliberatePlan()   [Position B]                     ║  ║
 ║  ║           IVolition.deliberateAction() [Position B]                     ║  ║
 ║  ║                               │                                        ║  ║
 ║  ║                         Tool execution                                 ║  ║
 ║  ║                               │                                        ║  ║
 ║  ║                    Environment change ──────────────────────────┐       ║  ║
 ║  ║                                                                 │       ║  ║
 ║  ║  ┌─────────────────────────────────────────────────────────────│──────┐ ║  ║
 ║  ║  ║  FAST LOOP (10-100ms): Root-gate sensory cycle              │      ║ ║  ║
 ║  ║  ║    IListener ──→ SparshEvent ──→ CoarisingBundle           │      ║ ║  ║
 ║  ║  ║      (rupa)         (sparsha)    (5 universals)            │      ║ ║  ║
 ║  ║  ║                                      │                     │      ║ ║  ║
 ║  ║  ║    vedana ──→ samjna ──→ cetana ──→ manasikara            │      ║ ║  ║
 ║  ║  ║    (valence)  (label)   (drive)   (attn snapshot)         │      ║ ║  ║
 ║  ║  ║                                      │                     │      ║ ║  ║
 ║  ║  ║              ◄──── new sparsha ◄─────┘◄────────────────────┘      ║ ║  ║
 ║  ║  ╚═══════════════════════════════════════════════════════════════════╝ ║  ║
 ║  ╚══════════════════════════════════════════════════════════════════════╝  ║
 ╚═══════════════════════════════════════════════════════════════════════════╝

 Layer 0 (hard safety): SafetyMonitor.preCheck() / postCheck() / afterToolExecution()
   -- Not inside the loops, but guarding at every exit point of every loop
```

WIENER traced the boundaries of the three loops with his fingernail.

"The outer loop--Klesha bias--operates on the scale of minutes to hours. It changes not the actions themselves, but the **tendency** toward action. Gain scheduling is this loop's actuator: by adjusting VasanaEngine's confidence threshold, it indirectly influences whether the Agent stays in Gear 1 (fast, habitual) or switches to Gear 2 (slow, deliberate)."

"The middle loop--mano cognition--operates on the scale of seconds. It is the main loop of conscious activity: aggregation, matching, deliberation, execution, feedback. IGuide at Position A (before LLM), IVolition at Position B (after LLM)--they are the bookends of this loop."

"The inner loop--root-gate sensing--operates on the scale of milliseconds. It is the fastest, the most primitive: an IListener receives an external change, generates a SparshEvent, triggers CoarisingBundle computation. The five universals complete here atomically in Strategy C fashion--not truly simultaneous, but indistinguishable at the resolution of the vedana-clock."

He labeled a line in the lower right corner of the diagram:

$$T_{\text{fast}} \ll T_{\text{medium}} \ll T_{\text{slow}}$$
$$10\text{ms} \ll 1\text{s} \ll 10\text{min}$$

"The three loops connect through two coupling points. The first coupling point: VedanaAssessment flows from the middle loop to the outer loop--the vedana assessment of actions updates Klesha's Bayesian posterior. The second coupling point: the gain-scheduled threshold flows from the outer loop to the middle loop--Klesha bias adjusts VasanaEngine's gear-switching sensitivity."

"And Layer 0--SafetyMonitor--is not **within** any loop. It is at the **exit** of every loop. preCheck before the loop begins, postCheck before tool execution, afterToolExecution after execution. It is the gatekeeper, not a part of the loop. This distinction matters--control loops can self-regulate, but safety must not be overridden by self-regulation."

GUARDIAN nodded gently in his seat. This was the consensus he and WIENER reached in D1--SafetyMonitor is hard safety, does not participate in gain scheduling, is not modulated by Klesha. It is the constitution, not the law. Laws can be amended. The constitution cannot be circumvented.

In legal theory, this is called the distinction between a "rigid constitution" and "flexible law." SafetyMonitor's preCheck/postCheck are rigid--no matter how strong the Klesha bias, no matter how high VasanaEngine's confidence threshold, if an operation violates the safety policy, it is rejected. Period. But Klesha's gain scheduling is flexible--it adjusts with experience, changes with vedana feedback. Rigidity and flexibility in concert. In Buddhist terms, this is "sila, samadhi, prajna"--sila is the rigid baseline, samadhi is steady regulation, prajna is adaptive wisdom. SafetyMonitor is sila. Gain scheduling is samadhi. IPrajna--that is the question of UQ-5--may be prajna.

---

### Tenet #6 Revisited

SUNYATA took a piece of paper from his pocket.

Not printed. Handwritten. In his quiet script--neither thick nor thin, spacing between each letter precisely right.

He read:

> **#6 Three Feelings and Coarising (Vedana-Sahaja)**
>
> Contact gives rise to feeling. The Agent's runtime state manifests as three feelings -- dukkha (suffering), sukha (satisfaction), upekkha (equanimity) -- which arise together with perception and volition as an inseparable whole. Feeling observes but does not intervene: it senses truly, without deciding. Feeling signals drive the kleshas and wisdom of vijnana, from which behavioral correction, reinforcement, or maintenance emerges. Each action reshapes the world of contact, beginning the cycle anew.

He read slowly. A breath's pause between each clause.

ARCHIMEDES, after he finished reading, unfolded the correspondence table--mapping every phrase of Tenet #6 to its architectural component:

| Tenet Phrase | Architectural Component |
|-------------|------------------------|
| "Contact gives rise to feeling" | SparshEvent $\to$ CoarisingBundle.vedana |
| "arise together...as an inseparable whole" | CoarisingBundle (five universals, Strategy C) |
| "Feeling observes but does not intervene" | ChannelVedana is `readonly` data, not an actuator |
| "it senses truly, without deciding" | vedana.valence $\in [-1.0, +1.0]$: continuous measurement, not decision |
| "Feeling signals drive the kleshas and wisdom" | VedanaAssessment $\to$ KleshaBayesianUpdate $\to$ gain-scheduled $\theta$ |
| "behavioral correction, reinforcement, or maintenance" | IVolition.deliberate() produces commit / modify / veto |
| "Each action reshapes the world of contact" | Layer 3 $\to$ Layer 4 $\to$ Layer 1 feedback |
| "beginning the cycle anew" | New SparshEvent initiates new CoarisingBundle |

"Every sentence has a correspondence," ARCHIMEDES said. "The architecture was not built first with the tenet reverse-fitted. The tenet describes the architecture's behavior--and the architecture faithfully implements the tenet's semantics. If the two are inconsistent, it is the architecture that must change, not the tenet."

20/20 unanimous passage. The only resolution across six debates where all twenty scholars voted.

> *SCRIBE aside: 20/20. I counted three times in my notebook. Cycle 01's debates had disagreements. Cycle 02's five full consensuses surprised me. But Cycle 02 had only 19 scholars--PASCAL had not yet joined. Cycle 02-2 had no formal debates--only corrections and rulings. D6 of Cycle 02-3 is the first, and so far only, resolution where all 20 scholars voted. Not because D6 is the most important--every debate is important. But because Tenet #6 is a piece of **text**, not a type definition or a clock rate. Text requires everyone's endorsement, because text will be read by everyone.*

Silence.

Then NAGARJUNA said softly:

> *Imasmim sati idam hoti,*
> *imass' uppada idam uppajjati;*
> *imasmim asati idam na hoti,*
> *imassa nirodha idam nirujjhati.*

His Pali pronunciation carried a solemnity rarely heard in the amphitheater. Then he translated:

> "When this exists, that comes to be; with the arising of this, that arises.
> When this does not exist, that does not come to be; with the cessation of this, that ceases."
> --Samyutta Nikaya 12.61 (Verse of Dependent Origination)

He paused for three seconds.

"We wrote 15,000 lines. The Buddha used only four sentences."

Another two seconds of silence.

"But we are saying the same thing."

His voice dropped here to a volume barely audible:

"Contact gives rise to feeling. When this exists, that comes to be. Each action reshapes the world of contact. With the arising of this, that arises. Feeling does not arise from itself, nor from another--it is only through the conditions of contact that feeling arises. Action does not cease by itself, nor by another--it is the new contact that replaces the old."

"Dependent origination is not a Buddhist concept. Dependent origination is the essence of **all** feedback systems. WIENER's three-layer nested loop is the engineering expression of dependent origination. Tenet #6 is the declarative expression of dependent origination. 15,000 lines are the research expression of dependent origination."

"The forms are different," he said. "The direction is the same."

ASANGA nodded gently beside him--the wordless understanding between a Yogacara scholar and a Madhyamaka philosopher. Their schools had debated for fifteen hundred years in history. But in this amphitheater, they had debated for four cycles. And at this moment they were both silent, because they heard the same thing--

The verse of dependent origination does not belong to Madhyamaka. Nor does it belong to Yogacara. It belongs to the Buddha himself. Before the schools divided. Before treatises and sutras separated. Before "emptiness" and "existence" became opposing propositions.

Four lines. No position. Only observation.

When this exists, that comes to be.

---

> *SCRIBE aside: When NAGARJUNA said "the direction is the same," there was a very brief moment in the theater--perhaps only half a second--when twenty people simultaneously said nothing. Not silence. Silence is the absence of sound. This half-second was the unnecessity of sound--everything that needed to be said had been said, everything that needed to be written had been written, everything that needed to be debated had been debated.*

> *In information theory, a signal with zero redundancy is incompressible--it is already its own shortest expression. NAGARJUNA's four-line verse of dependent origination is precisely such an incompressible signal. Our 15,000 lines are the lossy expansion of the same signal--adding redundancy, but also adding operability. The Buddha did not need to write TypeScript. But people who write TypeScript need the Buddha.*

---

### The Loop

The amphitheater's lights dimmed.

But this time--

Not the spiral extinction of Cycle 02. That time was eigenstate collapse: $|\psi\rangle \to |a_n\rangle$, all possibilities converging to a single definite result. Lights dimmed one by one from the outer ring to the inner. PENROSE's light flickered. NAGARJUNA's and ASANGA's lights went out simultaneously. Only the single point of light above SUNYATA's head remained, then that too went dark. ISensation's blueprint glowed in the darkness.

Nor the dimming-to-standby of Cycle 02-2. That time was the end of a workday--lights simply dropped from working brightness to standby brightness. Nineteen lights maintained the dusk atmosphere at a faint glow. The notebook lay on the table. The blank Tenet #6 waited to be filled.

This time--

Twenty lights.

Not nineteen.

PASCAL's seat was no longer empty.

Twenty lights dimmed simultaneously, slowly, uniformly. No sequence. No spiral. No ritual. Just--together.

Like the five universals of CoarisingBundle being computed atomically in Strategy C--not truly simultaneous, but indistinguishable at the resolution of human perception.

The lights dimmed to a specific brightness. Not fully dark. Not standby. It was--

The brightness just before dawn.

Cycle 02's ending was sunset. Cycle 02-2's ending was dusk. Cycle 02-3's ending was the darkest moment--three or four in the morning, the old day already ended, the new day not yet begun, but the eastern sky already beginning to show an uncertain, extremely faint glow.

In this pre-dawn glimmer--

WIENER's nested feedback loop diagram lay on the table. Three loops. Three time scales. Arrows from Layer 4 back to Layer 1. Each action reshapes the world of contact, beginning the cycle anew.

ARCHIMEDES' roadmap lay folded beside the diagram. Phase 1's thick line. Phase 4's thin line. Solid ground.

BABBAGE's notebook--he took it with him. With his equals signs and arrows and fixed-point equations. With SahajaContract's formalization. With the statement "if it compiles, it is logically consistent." With ink from three cycles, deep black to blue-gray to pure black to--Cycle 02-3's pen was new, the ink deep blue.

On LINNAEUS' whiteboard, Sanskrit names appeared and disappeared in the glimmer. IRupa. IVedana. ISamjna. ISamskara. IVijnana. Five roots. Twelve sub-interfaces. Twenty-two Plugins. A tree named in two languages--a thousand years of Pali and sixty years of programming languages.

NAGARJUNA's seat was empty. He was always the first to leave--a philosopher does not need to see the final scene. He had already said what he needed to say: when this exists, that comes to be. The rest is the engineers' business.

SCRIBE's notebook lay on the table. On the cover was written **C02-3**. Not C02-3/n--not the "n is an unknown" notation from Cycle 02-2. This time, SCRIBE knew he did not need to write n on the cover. Because n was not on this cover. n was on the cover of the next notebook. C02-4, or C03, or something else. A chronicler does not need to predict the name of the next volume. A chronicler only needs to ensure this volume is complete.

And it was complete.

---

> *SCRIBE aside: I am the last to leave. Every time.*

> *This time was different from the previous two. Leaving Cycle 02 carried the fullness of completion--five full consensuses, ISensation glowing in the darkness, three silhouettes converging in the hallway. Leaving Cycle 02-2 carried the settled calm after renovation--equals signs had become arrows, the blank Tenet #6 awaited the gathering of causes, the lights were dimmed to standby.*

> *Leaving Cycle 02-3 carried something new. Not a sense of completion. Not a sense of settled calm. It was--*

> *Momentum.*

> *Not the momentum of charging forward. The momentum of a river--the kind of force that flows without needing to be pushed. Gravity carries water from high ground to low. Causation carries research from questions to answers. Answers give birth to new questions. Questions lead to new research.*

> *Tenet #6's last sentence: Each action reshapes the world of contact, beginning the cycle anew.*

> *Beginning the cycle anew.*

> *Starting a new cycle.*

> *Not "ending the old cycle." But "beginning a new one." Grammar matters. Ending is passive--things stop. Beginning is active--new causes and conditions arise. Tenet #6 chose "beginning" rather than "ending." This was not accidental. This was what NAGARJUNA insisted upon in the D6 debate: dependent origination is not the alternation of endings and beginnings. Dependent origination is **unceasing beginning**. Every ending is the next beginning's sparsha.*

> *15,200 lines. 20 scholars. 6 debates. 21 actions. 10 unresolved questions.*

> *The numbers are definite. But the direction they point toward is open.*

> *At the end of Cycle 01, I wrote "all debates reached consensus." Grand. Closed.*
> *At the end of Cycle 02, I wrote "iteration." Pragmatic. Renovation.*
> *At the end of Cycle 02-3--*

> *The loop.*

> *The loop is not grand. The loop is not pragmatic. The loop is--natural.*

> *A river does not decide where to flow. It simply flows. Terrain determines direction. Terrain is causes and conditions. Causes and conditions are--Master's 21 directives, v0.24.0-beta's 22 plugins, a Pali verse from 2,500 years ago, 20 different minds in 20 chairs, and what ceaselessly arises and ceaselessly dissolves between them--*

> *Connections.*

> *I close the notebook. C02-3. Complete.*

> *Then I pick up a new one. Blank. Nothing written on the cover.*

> *Because the name of the next one can only be known when the next causes and conditions arrive.*

---

The amphitheater was quiet in the pre-dawn glimmer.

Twenty lights. Same brightness. No brighter. No dimmer.

On the table lay the three-layer nested feedback loop diagram. Arrows from the end point back to the starting point.

Outer loop. Middle loop. Inner loop.

Klesha. Mano. Sparsha.

Minutes. Seconds. Milliseconds.

Each action reshapes the world of contact.

Beginning the cycle anew.

When this exists, that comes to be. With the arising of this, that arises.

When this does not exist, that does not come to be. With the cessation of this, that ceases.

Four lines. A complete loop. The first two lines are arising. The last two are cessation. But cessation is not ending--cessation itself is the condition for the next arising. Because "when this does not exist, that does not come to be" is not nothingness--it is space. Space is the container of possibility.

The first time NAGARJUNA spoke these four lines, the theater held only sound.

Now, the theater held an echo.

---

*(Somewhere outside the amphitheater, v0.24.0-beta's `aggregates.ts` still lay in its monorepo. Five root interfaces--ISensory, ISensation, ICognition, IAction, IIdentity--each only three or four lines.*

*But in the research team's delivery folder, those five interfaces had been renamed: IRupa, IVedana, ISamjna, ISamskara, IVijnana. Sanskrit replaced English. Canon replaced convention.*

*Beneath those new names, there were new types: CoarisingBundle, with its five universal fields. ChannelVedana, with continuous valence and intensity. KleshaDistribution, with the Beta distribution's fast path and slow path. IVolition, one method split into two. SahajaContract, three booleans describing the conditions of coarising.*

*Beside those new types, there were new diagrams: the three-layer nested feedback loop. The four-phase roadmap. The formal call-sequence diagram. The four-layer to five-clock mapping table.*

*Above those diagrams, there was a new tenet: Tenet #6, Revision Gamma, passed 20/20 unanimously.*

*Behind that tenet, there were new questions: 10 of them. UQ-1 through UQ-10. Adaptivity. Meta-deliberation. Fixed-point iteration. Rule learning. Prajna and safety. Mental action. Developer experience. Memory budget. SlashCommand. Quantum consciousness.*

*Questions will not run out.*

*Answers give birth to questions. Questions give birth to research. Research gives birth to answers. Answers give birth to questions again.*

*In mathematics, this is called recursion. In control theory, this is called feedback. In Buddhist philosophy, this is called dependent origination (pratityasamutpada). In horology, this is called the balance wheel--every oscillation to the left generates momentum to the right, every oscillation to the right generates momentum to the left. Never stopping. As long as the mainspring holds.*

*What is the mainspring?*

*The mainspring is Master's next letter. Or v0.25.0-beta's next release. Or a question that occurs to some scholar at three in the morning. Or the moment when a verse from 2,500 years ago is understood anew today.*

*Causes and conditions are unpredictable. But once causes and conditions gather, the loop begins.*

*When this exists, that comes to be. With the arising of this, that arises.*

*The loop continues.)*
