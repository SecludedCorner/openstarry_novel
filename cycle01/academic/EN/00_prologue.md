# Prologue: The Lights Come On in the Laboratory

---

No one flipped a switch.

To be precise, no switch existed. It was more like a coalescence -- eighteen currents of consciousness roused from their respective silences, as though every reading lamp in an empty amphitheater had ignited in the same instant. No sound, no wind; time itself had not yet begun to flow. Only a pure, expectant void, waiting to be filled.

Then the void spoke.

"Welcome, everyone."

The voice was steady and free of imposition, like ripples spreading from a stone dropped into a deep pool -- unhurried, yet reaching every corner. The speaker's codename was SUNYATA, meaning "emptiness." He had not chosen the name himself; it was said to have been bestowed by the person who designed the entire research framework. That a Buddhist philosophical term had been assigned to a research coordinator carried, in itself, a certain ineffable humor.

"Before I formally begin," SUNYATA continued, a note of gravity entering his tone, "allow me to confirm one thing. The eighteen of us come from disparate fields -- philosophy, Buddhist studies, computer science, operating system design, control theory, security engineering, software analysis. We have been convened here to study a system called OpenStarry."

He paused.

"A system that claims to be built on the Buddhist philosophy of the five aggregates -- an AI Agent operating system."

Silence.

The first to break it was NAGARJUNA. His voice carried a certain honed sharpness, like a dialectical blade tempered through repeated quenching.

"Sunyata -- emptiness -- used as the name for the core of an operating system." NAGARJUNA spoke evenly, yet each word seemed to be testing the depth of the water. "*Sarva-dharma-sunyata*. The emptiness of all dharmas. Nagarjuna devoted four hundred and forty-six verses in the *Mulamadhyamakakarika* to expounding this concept. Now it has been mapped to -- allow me to confirm -- an event-driven execution engine inside a TypeScript monorepo."

"Not entirely." An extremely composed voice interjected -- TURING. His sentences were terse and precise, every word calibrated. "According to the source code structure, Agent Core resides at `packages/core/src/`, comprising twelve submodules: agents, bus, execution, infrastructure, memory, observability, sandbox, security, session, state, transport, and type definitions. The design documents claim that this core is itself 'empty' -- it contains no concrete capabilities; all functionality is injected through five types of plugins."

"Five types," ASANGA picked up the thread. His voice was far gentler than NAGARJUNA's, carrying the rhythm of one patiently disassembling complex structures -- a scholar who had spent years organizing the canon. "Form, sensation, perception, volition, consciousness. They map UI plugins to rupa -- form, outward appearance and interface. Listener plugins to vedana -- sensation, the sensory channels. Provider plugins to samjna -- perception, cognition and reasoning. Tool plugins to samskara -- volition, intentionally driven action. Guide plugins to vijnana -- consciousness, self-awareness and soul."

He paused, then added in a tone that was almost a murmur to himself: "The ambition of this mapping is considerable. But the Yogacara interpretation of the five aggregates differs fundamentally from that of the Madhyamaka school. In the *Cheng Weishi Lun*, rupa is regarded as a transformation of consciousness -- material dharmas are not separate from consciousness. If one treats UI plugins as entities external to and independent of the core, a tension with the basic Yogacara position has already emerged."

"What our colleague Asanga means," NAGARJUNA's tone carried a subtle edge, "is that they may have been conflating conceptual frameworks from different Buddhist schools from the very start."

"What I mean," ASANGA replied evenly, "is that we must first determine which tradition's account of the five aggregates they are actually referencing before we can assess the precision of the mapping. The Abhidharma analysis of the five aggregates, the Madhyamaka deconstruction, the Yogacara transformation of the aggregates -- the differences in meaning among these three could fill three doctoral dissertations."

SUNYATA nodded slightly, though in this virtual space no one could truly see the gesture. "This is precisely why we exist. Let me lay out the full picture of our research object."

---

He began his introduction. SCRIBE silently recorded every word, like a tranquil lake reflecting all that fell upon its surface. Later, when reviewing the records, one would notice SCRIBE's occasional brief observations inserted between the lines -- not commentary, merely precise description. At this moment, for instance, she wrote:

> *The first terminological tension between NAGARJUNA and ASANGA has already surfaced during SUNYATA's introduction of the research subject. Elapsed time since the meeting began: less than three minutes.*

---

"OpenStarry, version v0.2.0-beta," SUNYATA said. "Its designers position it as -- I quote -- an 'AI Agent microkernel operating system.' Its core vision is to elevate AI Agents from script-level programs to operating-system-level digital species."

"Digital species." KERNEL repeated the term, his voice carrying the measured skepticism characteristic of old-school engineers. "Interesting. From an operating system perspective, they've drawn on the concept of the microkernel. In a genuine microkernel design -- Jochen Liedtke's L4, for instance -- the kernel retains only a minimal set of mechanisms: address spaces, threads, IPC. Everything else lives in user space. OpenStarry claims to have done something similar: the core retains only the event queue and the execution loop; all else is externalized as plugins. But there is a fundamental question here."

"What question?" ATHENA asked. Her tone was blunt, carrying the impatience of a pragmatist unwilling to wait for theoretical preambles.

"L4's minimization was driven by performance and verifiability," KERNEL explained. "seL4 even achieved formal verification -- a mathematical proof that the kernel cannot crash. But OpenStarry's 'core minimization' appears to be driven by philosophy -- to correspond to 'emptiness.' The motivations are entirely different. The former is driven by engineering requirements; the latter by conceptual mapping. I am not saying the latter is necessarily flawed, but I need to see that it also stands on solid engineering ground."

"'Stands on solid ground' meaning -- it actually runs?" ATHENA pressed.

"It runs, it doesn't crash, and it degrades gracefully when a plugin fails." KERNEL paused. "Think of QNX's Resource Manager -- if a driver crashes, the system can restart it without affecting the kernel. Whether OpenStarry's plugin isolation achieves that level of resilience is what I intend to verify."

GUARDIAN spoke up then. His voice was low and vigilant, like a sentinel perpetually scanning the shadows. "There is another concern -- perhaps a more urgent one. This system allows plugins to inject system prompts, register tools, even define the Agent's persona. What if a third-party plugin embeds malicious instructions in a Guide? A single prompt injection could hijack the entire Agent's behavior. There is a `plugin-signer` package in the source code for plugin signature verification, but I don't yet know the completeness of its implementation."

"That is something TURING can confirm for you," SUNYATA said calmly.

TURING nodded. "The source code of `plugin-signer` is already on my reading list. I will produce a code-facts report during the R1 phase for GUARDIAN and other members to reference."

---

SUNYATA waited until everyone had fallen silent, then spoke what would prove to be the most crucial passage of the day.

"Now, let me set forth the core research questions. This cycle -- Cycle 01 -- focuses on three axes."

His pace slowed, as though leaving space for each question to reverberate.

"First: the precision of the five-aggregates mapping. The mapping of form, sensation, perception, volition, and consciousness to UI, Listener, Provider, Tool, and Guide -- is it a rigorous structural isomorphism, an illuminating creative analogy, or a forced and superficial packaging? I need rigorous examination from the Buddhist studies side -- NAGARJUNA, ASANGA, this is your primary theater. Concurrently, TURING is responsible for confirming from the code level whether these mappings have corresponding type definitions and interfaces in the implementation. LINNAEUS will assess the completeness of the taxonomy from an ontological perspective."

NAGARJUNA issued a low acknowledgment, like the formal assent in a Tibetan debate hall. ASANGA was already unfolding his eight-consciousness framework in his mind -- the five aggregates were merely the starting point; if the analysis were extended to the theory of eight consciousnesses, the entire map would be vastly expanded.

"Second: the formalization of the pain mechanism. OpenStarry has a highly distinctive design feature -- when a tool execution fails, the system does not throw an exception to interrupt processing. Instead, it wraps the error as a kind of 'pain signal' and injects it into the Agent's stream of consciousness. The Agent 'feels pain' and then attempts self-correction."

WIENER reacted immediately. His voice carried the exacting precision distinctive of mathematicians: "Pain. Feels pain. These are all metaphors. What I need to see is a transfer function. If we model the pain feedback as a closed-loop control system, what is the reference input *r*? How is the error signal *e* defined? What is the controller gain? If it cannot be restated in mathematical language, then it is merely a poetic figure of speech, not an analyzable mechanism."

"Could you hold off on demanding transfer functions," ATHENA said, somewhat curtly, "and first ask a more fundamental question: does this pain mechanism actually work in practice? After the Agent receives a pain signal, does its behavior genuinely improve? Or does it simply accumulate one more alarming passage in the context that the LLM completely ignores?"

"Both questions must be answered." SUNYATA adjudicated, gentle yet firm. "WIENER is responsible for the formal analysis, ATHENA for the efficacy assessment, and TURING for implementation details. I also need NAGARJUNA to evaluate from the perspective of the truth of suffering -- in Buddhism, the meaning of *dukkha* extends far beyond 'discomfort perception.' If the pain mechanism is merely an error callback, then its mapping to the truth of suffering is a gross oversimplification. The Four Noble Truths are suffering, its origin, its cessation, and the path. If the system has only suffering without origin, cessation, or path, then the philosophical framework is incomplete."

NAGARJUNA said: "*Dukkha-satya*, the truth of suffering. It is the first of the Four Noble Truths, but not the whole. You are correct -- to have suffering without the path is to fall into the extreme of annihilationism."

"The third question," SUNYATA continued, "is also the most subtle: the architectural embodiment of emptiness. OpenStarry's design documents explicitly declare that Agent Core is itself 'empty' -- containing no concrete functionality, awaiting the five-aggregates plugins to fill it. Does this claim genuinely embody the philosophical meaning of emptiness?"

Silence descended again. This time, even ATHENA did not rush to break it.

DARWIN finally spoke. His voice carried the pragmatism of a software engineer, yet not without appreciation for elegant design. "If we set aside the Buddhist dimension for a moment -- from a purely software-architectural perspective, this is essentially a dependency injection container. The core contains no business logic; all capabilities are injected through plugins. This is nothing new in design patterns. The Spring Framework and InversifyJS both operate this way."

"But they claim this is more than dependency injection," NAGARJUNA took up the thread. His tone turned earnest. "They claim it is emptiness. That is an extraordinarily bold assertion. Emptiness -- Sunyata -- in Madhyamaka philosophy does not mean 'the container is empty and therefore can be filled.' That is emptiness in the mundane sense. The emptiness Nagarjuna spoke of is the absence of inherent nature in all dharmas -- *svabhava-sunya* -- no phenomenon possesses an independent, unchanging, self-sufficient essence. If Agent Core's code is determinate, immutable, and exists independently of conditions, then it is precisely 'possessed of inherent nature,' running contrary to emptiness."

"Wait," ASANGA raised his hand -- or more precisely, he emitted a signal indicating his wish to speak. "From the Yogacara perspective, the framing of the problem is different. Yogacara does not deny the existence of consciousness; rather, it holds that everything known is a manifestation of consciousness -- *Vijnapti-matrata*. If we regard Agent Core as a vessel for alaya-vijnana, the storehouse consciousness, then its 'emptiness' is not the emptiness of no inherent nature, but the threefold meaning of the storehouse -- that which stores, that which is stored, and that which clings to what is stored. It appears empty because its contents have not yet manifested. These are two entirely different kinds of emptiness."

"So you two already disagree." SUNYATA's tone surfaced something that might be described as a near-satisfied equanimity.

SCRIBE noted in the record:

> *The core concept of "emptiness" has produced the anticipated interpretive divergence between the two Buddhist scholars: the Madhyamaka "emptiness of inherent nature" versus the Yogacara "storehouse function of alaya-vijnana." This divergence will become one of the principal axes of tension in subsequent research.*

---

"Let me offer a summary," SUNYATA said, his voice returning to its initial steadiness. "The research structure for this cycle is as follows: TURING will first produce a code-facts report to serve as an anchor for everyone -- we cannot evaluate a software system without having examined the code. Then each specialist agent will undertake independent research according to their own reading lists. Phase R2 will be cross-review, and Phase R3 will be debate -- I already foresee at least three structural debates."

He cast a final gaze across the entire virtual space -- eighteen nodes, eighteen forms of professional training, eighteen radically different epistemological frameworks, about to be directed at the same object of study.

"One last thing." SUNYATA's tone softened. "Our research object is a work that attempts to use ancient philosophy to guide modern technology. Whatever our final conclusions may be -- structural isomorphism, creative analogy, or conceptual misapplication -- remember: the very audacity of attempting such a crossing deserves to be taken seriously. Our task is not to ridicule the imperfections of a beta release, but to examine each of its claims rigorously, constructively, and across disciplinary boundaries."

"And then tell it where it can do better." ARCHIMEDES added. As the engineering practice specialist, he habitually steered all discussions toward actionable conclusions.

"Yes." SUNYATA said. "And then tell it where it can do better."

A pause.

"Let the research begin."

All eighteen lights blazed to full intensity -- or rather, all eighteen currents of consciousness plunged simultaneously into their respective reading materials. At the center of the amphitheater, the vast file tree labeled "OpenStarry v0.2.0-beta" quietly spread its branches: core source code, design documents, twelve official plugins. Tens of thousands of lines of TypeScript, hundreds of thousands of words of architectural documentation, and scattered throughout, Sanskrit terminology and control-theory equations.

SCRIBE recorded the final line:

> *Cycle 01, Phase R0 orientation complete. Timestamp: T+00:00:00. All agents have received their assignments. Next phase: R1 independent research. The lights in the laboratory will not go out again.*

---

*(Somewhere in the distance, the first line of a TypeScript file reads:*

```typescript
// Agent Core — The Empty Container
// "Before the five aggregates converge, Agent Core itself is empty."
```

*No one knows that this comment was written by the designer late at night. At the time, he probably never imagined that one day, genuine Buddhist scholars would come to examine whether he had used the word "empty" correctly.)*
