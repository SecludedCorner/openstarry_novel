# 第一章：三十七份文件 — Chapter 1: Thirty-Seven Documents

---

The doors of the amphitheater were already open before the research team arrived.

They had not been pushed open. It was more as if they had always been open — from the moment the engineering team departed, those doors had remained in a posture of openness, like an invitation, like a question. Inside the theater beyond the doors, the air still held traces of a certain order. Documents on the table had been neatly separated into four stacks. The last chart on the projection screen was still lit — an inheritance tree, five Sanskrit names branching upward from the root, each branch annotated with dashed lines marked "pending confirmation."

SUNYATA was the first to walk in.

He stood at the entrance and did not immediately proceed to his seat. He was looking at the documents. Four stacks. He counted once. Twice. Then his gaze settled on the inheritance tree on the projection screen, resting at the root of that tree for three seconds.

(SCRIBE aside: The first ten seconds after SUNYATA entered were silent. His silence was not hesitation — it was measurement. He was measuring the residual density of thought in this room. How long had the engineering team worked here? How much had they left behind? What was the weight of these things? The answers to these questions would determine the opening posture of the entire research cycle to come.)

"Thirty-seven." SUNYATA said. His voice carried no exclamation, no surprise — only the precise weight of a number.

---

The others filed in, each in their own way.

BABBAGE walked in with his notebook already turned to a blank page. His fingers left an almost invisible crease at the edge of the page — his shorthand mark, meaning "this page's content has not yet begun but is destined to be dense." His gaze swept across the height of the four document stacks, quickly estimating total page counts: 12 discussion documents at roughly 8–15 pages each; 7 delivery packages of structured documents with fewer pages; 8 to-do tracking files in checklist format; plus more than 120 files in the openstarry_doc directory. A combinatorial explosion of reading.

$$\text{Total pages} \approx 12 \times 12 + 7 \times 6 + 8 \times 4 + 120 \times 8 \approx 1,186$$

He wrote this number in his notebook, then drew a question mark beside it. Page count was not the problem. The problem was information density — of those 1,186 pages, how many contained novel semantic units, and how many were restatements of known conclusions? If the proportion of new semantics fell below 30%, reading efficiency would drop precipitously. If it exceeded 70%, the team might need an additional orientation round.

NAGARJUNA saw the inheritance tree on the projection screen when he entered. He stopped. Not because of the tree's structure — IRupa, IVedana, ISamjna, ISamskara, IVijnana, the Sanskrit naming of the Five Aggregates — but because of the tree's root. There, in small text, was written:

```
// 根介面重命名：ISensory → IRupa, ISensation → IVedana, ...
```

An arrow. An arrow from English to Sanskrit. NAGARJUNA stared at that arrow for a long time.

"String replacement." He said in a low voice. These two words were not a compliment.

WIENER entered carrying a mug. He placed it at the nearest edge of the table, then flipped open the first document he laid eyes on — M10_temporal_architecture.md. He read the first line below the title: "Vijnana is fastest, samskara next, samjna slowest." He set the document down. His expression was the particular unease of an engineer encountering an unproven axiom — not objection, but unease.

"Vijnana is fastest." He repeated to himself. "Based on what?"

KERNEL opened another copy of the same document at almost the same moment. He was reading a different section — the multi-clock event-driven architecture diagram. His finger traced along the arrows in the diagram: vijnanaClock (1–10ms) → samskaraClock (10–100ms) → vedanaClock (100–500ms) → rupaClock (I/O bound) → samjnaClock (500ms+).

"Five independent clocks." He said. His tone carried no wonder, only the instinctive alertness of an operating systems engineer confronting a multi-clock synchronization problem. "Who handles synchronization? What about priority inversion? What if a vijnanaClock event gets blocked by a long-running samjnaClock task?"

No one answered. These questions had not yet reached the time for answers. They were merely planted.

---

Twenty people. Twenty seats.

SUNYATA waited until everyone was settled before walking to the front of the projection screen. He did not turn off the inheritance tree the engineering team had left behind. He let it remain — behind him, like a backdrop, like a starting point, and also like an assumption in need of re-examination.

"There are thirty-seven documents before us." He began. "They were created by the engineering team before our involvement. I will inventory them one by one."

He turned to the projection screen and drew a line through the air with his finger, following the direction of the four document stacks.

"First stack: discussions/ — 12 issue analyses. M1 through M10, plus L1 and L_legacy. These are the engineering team's point-by-point responses to Master's 21 directives."

"Second stack: deliver/ — 7 delivery package drafts. 00 through 06. Naming migration guide, type system changes, architectural additions, document checklist, engineering action plan, breaking changes guide."

"Third stack: todo/ — 8 to-do tracking files. blockers, code_todos, controversial_items, decisions_to_confirm, discussion_items, doc_gaps, future_cycle_items, pending_decisions."

"Fourth stack: openstarry_doc/ — over 120 document revision drafts. Architecture_Documentation with 28 files, Plugin_System_Architecture with 7, Project_Structure_and_Conventions with 20, Technical_Specifications with several, Implementation_Examples, Agent_Core_Components_Deep_Dive with 16."

He paused for one beat.

"But what is more important is what is **not** in front of us."

SYNTHESIST looked up. He had been leafing through the second stack of documents with the integrator's characteristic global perspective — not looking at details, looking at structure. He knew what SUNYATA was about to say.

"No counter-arguments." SYNTHESIST said.

"None." SUNYATA confirmed. "Every one of the 12 issue analyses follows the same structure: Master's original text → background analysis → engineering solution → decision. From analysis to conclusion, straight-line progression. No one said 'wait, what if this direction is wrong?' No one said 'I object.' No one dismantled the problem from a different angle."

GUARDIAN nodded. He had turned to Section 3 of M3_klesha_multilayer_di.md — the Klesha inheritance hierarchy — and seen the TypeScript interface definitions. Four root afflictions, four interfaces extending IKlesha, each with an `intensity: number`. Clean. Orderly.

Too orderly.

"These documents are engineering documents, not research documents." SUNYATA said. "This is the position we need to remember."

He looked toward SCRIBE.

"Note this down. The research team's position statement — "

(SCRIBE aside: I picked up a new logbook. Dedicated to Cycle 02-3. The cover was deep blue. On the first page I wrote the date: 2026-02-25. Then SUNYATA's statement.)

"The engineering team's documents are **input material**. Not conclusions. They are valuable references — they systematically inventoried all issues, and the TypeScript interface designs are concretely usable. But the research team's value lies not in repeating the engineering analysis, but in **multi-perspective collision** and **deeper dimensions**."

NAGARJUNA leaned forward slightly in his seat. "Deeper dimensions — " he repeated these words, his tone carrying a special weight, the instinctive resonance of a philosopher touching upon a core concept.

"We have twenty scholars. Philosophers, Buddhist scholars, a theoretical computer scientist, a control theorist, a security expert, a taxonomist, a quantum consciousness researcher — and a newly joined decision theorist." SUNYATA looked toward the last seat on the right side of the venue. "This is the breadth the engineering team does not have."

PASCAL quietly nodded once in his seat. He had not yet spoken. But his notebook was already open, with a 2×2 matrix drawn on it — rows labeled "Analysis/Decision," columns labeled "Certain/Uncertain." The upper-left corner read "Engineering Team"; the lower-right corner had a circle drawn in it, empty inside.

That circle was his own position.

---

## Document-by-Document Review

The review began with M1.

SUNYATA did not start with M5 (sparsha → coarising) — the issue everyone knew was central — but with M1 (Sanskrit naming). His choice was deliberate. Naming is the most superficial question, but also the most fundamental. A tree grows from its roots. Naming is the root.

"M1_sanskrit_naming.md." SUNYATA read out the file name. "Master's ruling: the Five Skandha Plugins shall use skandha names. ISensory → IRupa, ISensation → IVedana, ICognition → ISamjna, IAction → ISamskara, IIdentity → IVijnana. The four root afflictions, seven deadly sins, and derivative afflictions shall also use their original-language terms. The code must compile."

LINNAEUS opened the engineering team's M1 document. His taxonomist's instinct made him look at structure before content.

"The naming table is complete." His first remark was affirmation. He pointed to the tables in the document — the mapping from current interface names to Sanskrit interface names, sub-interface inheritance relationships, naming proposals for Kleshas and mental factors. "The engineering team produced a clean migration scheme. The backward compatibility strategy is sound — TypeScript type aliases provide a transition period."

```typescript
/** @deprecated Use IRupa */
export type ISensory = IRupa;
/** @deprecated Use IVedana */
export type ISensation = IVedana;
/** @deprecated Use ISamjna */
export type ICognition = ISamjna;
/** @deprecated Use ISamskara */
export type IAction = ISamskara;
```

"However — " LINNAEUS turned to Section 4 of the document. "The discussion of philosophical implications is only four lines. They say 'Sanskrit naming directly aligns with the original Buddhist philosophical sources, eliminating translation ambiguity.' Then they give three examples — ISensory might be misunderstood as 'sensor,' IAction as 'action,' ICognition as 'cognitive science.'" He closed the document. "That is correct. But it addresses only the first layer of nomenclature."

"What other layers are there?" ARCHIMEDES asked. He was the pragmatic engineer, not attuned to the strata of taxonomy.

LINNAEUS looked toward NAGARJUNA.

NAGARJUNA stood up. In the amphitheater, standing was a signal — it meant that what followed was not commentary but exposition.

"Using Sanskrit names is not merely string replacement." He said. His voice was unhurried, each word allotted an equal measure of time. "It is a **philosophical commitment**."

He walked to the front of the projection screen, pointing at the root of the inheritance tree.

"When you rename ISensory to IRupa, you are not merely changing an English word to a Sanskrit word. You are saying: **this interface commits to faithfulness to the original definition of rupa-skandha**. And the original definition of rupa-skandha — in the Heart Sutra, in the Khandha-samyutta, in the Pancavastu-vibhasa — is far broader than what 'sensory input' conveys."

> 「色即是空，空即是色。色不異空，空不異色。受想行識，亦復如是。」
> —《般若波羅蜜多心經》(*Prajnaparamita Hrdaya Sutra*)

"If IRupa only handles UI rendering and Listener input, then it does not deserve the name 'rupa-skandha.'"

ARCHIMEDES frowned slightly. "Then what do you propose? Not to rename?"

"No. Master has ruled, and we rename. But after renaming, the **scope of every interface must be re-examined**." NAGARJUNA turned to face the entire audience. "This is the core point I wish to make — in Buddhist philosophy, naming itself is an act of **conventional designation** (prajnaptir upadaya)."

He drew a character in the air with his finger. No one in the audience saw the character, but everyone knew what he had written.

> Conventional designation (prajnaptir upadaya)
> — Names are merely conventions established for communicative convenience,
>     pointing to no entity possessing inherent existence (svabhava).

"When we name an interface IRupa, we are performing conventional designation. This name **is not** rupa-skandha — it is a sign we designate for communicative convenience. But conventional designation carries a strict requirement: **the designated name must correspond to the function it refers to**. If IRupa's functionality covers only 30% of rupa-skandha, then this designation is **incorrect**."

BABBAGE stopped writing. He saw a formal structure in NAGARJUNA's argument:

$$\text{命名正確性} \iff \text{Sem}(\text{IRupa}) \supseteq \text{Sem}(\text{rupa-skandha}) \cap \text{Dom}(\text{OpenStarry})$$

where $\text{Sem}(x)$ is the semantic domain of $x$, and $\text{Dom}(\text{OpenStarry})$ is the functional domain of the OpenStarry system. In other words: the semantic domain of IRupa must cover all functionality of rupa-skandha that is expressible within the OpenStarry system.

NAGARJUNA glanced at BABBAGE's notebook and nodded. "BABBAGE's formalization is precise. Naming is not just labeling — naming is a **coverage commitment**."

LINNAEUS picked up the thread. "As a taxonomist, I will add another dimension. In biological taxonomy, once a species' scientific name (binomial name) is established, its **type specimen** is fixed. Once IRupa is established as the interface name for rupa-skandha, the **definition** of rupa-skandha becomes its type specimen. If the engineering implementation deviates from the type specimen, it is not a problem with the implementation — the naming was wrong."

(SCRIBE aside: NAGARJUNA and LINNAEUS, from entirely different directions — Madhyamaka philosophy and taxonomy — arrived at the same conclusion: naming is not mere string replacement; it is commitment. This was the first cross-disciplinary resonance of Cycle 02-3. I marked this moment with a double underline in my notebook.)

---

The review continued to M3.

M3_klesha_multilayer_di.md generated the most divided response among the research team. Not regarding the architectural direction — four root afflictions inheriting from IKlesha and being injected into the IVijnana runtime environment, a direction grounded in the Cycle 02-2 A-1 consensus (ego-clinging = root of affliction). The division occurred over a seemingly minor detail.

PASCAL was the first to speak.

While everyone else was still browsing the TypeScript interfaces for the four afflictions — IMoha, IDrishti, IMana, ISneha — PASCAL had already turned past the interface definitions, past the architecture diagrams, past the State-Behavior separation explanation, and stopped on a single line of code. He drew a thin line on the paper with his fingernail.

```typescript
interface IKlesha {
  readonly type: string;
  /** 當前強度 (0.0-1.0) */
  readonly intensity: number;
  perceive(context: VijnanaContext): KleshaSignal;
  update(feedback: VedanaAssessment): void;
}
```

"`intensity: number`." He read it aloud.

Two seconds of silence.

"What is the **epistemological status** of this number?"

ARCHIMEDES turned to look at him. "What do you mean?"

PASCAL closed the document and placed his hands, fingers interlaced, on the table. This was his first formal statement in Cycle 02-3 — not the courteous dialogue of self-introduction, not hallway small talk. It was exposition.

"What I mean is: what does an `intensity` of 0.7 represent?"

He stood up. Standing in the amphitheater was a signal — NAGARJUNA had demonstrated this just three minutes earlier. PASCAL's manner of standing was different: NAGARJUNA's had been slow, ceremonial; PASCAL's was crisp, like a folding ruler snapping open.

"Let me give you three possible answers."

"First: 0.7 is a frequentist interpretation. It means: in 100 observations, this affliction was triggered 70 times. But what is the sample space of observations? What is the definition of 'triggered'? Who is observing? An Agent cannot observe its own afflictions — that is the observer paradox."

PENROSE nodded slightly from the observation gallery.

"Second: 0.7 is a subjective degree of belief (Bayesian interpretation). It means: the system believes with 0.7 confidence that this affliction is currently active. But what is the prior for belief updating? What is the likelihood function? Without a defined prior, 0.7 and 0.3 are indistinguishable — they are both arbitrary numbers."

BABBAGE's pen tip paused for a second. He was beginning to understand.

"Third: 0.7 is a pure engineering calibration. It means: it is just a number, 0 is the minimum, 1 is the maximum, 0.7 is moderately high. No probabilistic meaning, no statistical meaning — just a convenient floating-point number for computation."

He surveyed the theater.

"If it is the third answer — then `intensity: number` is a **blank**. It looks like a quantification, but in reality it quantifies nothing. It is a **placeholder** — a TODO written in code."

WIENER leaned forward from his seat. His control theory instinct had been triggered. "You're saying the PID controller's input signal has no defined domain?"

"Worse than that." PASCAL said. "A PID controller assumes its input is a measurable physical quantity — temperature, pressure, rotational speed. But 'the intensity of moha' is not a physical quantity. It is not even a psychological quantity — Buddhist philosophy never quantifies afflictions with numbers."

ASANGA leaned slightly forward in his seat. "PASCAL is right. In Yogacara, the four root afflictions are described in **qualitative** terms — "

He quoted the Cheng Weishi Lun:

> 「云何我癡？謂於我相，無明為性。迷自內我，愚於我理，故名我癡。」
> — 窺基《成唯識論述記》卷五 (Kuiji, *Cheng Weishi Lun Shu Ji*, Fascicle 5)

"Note the vocabulary: 'deludes,' 'blinds.' These are qualitative descriptions, not quantitative ones. You can say one person's atma-moha is 'deeper' than another's, but you cannot say it is 0.7."

BABBAGE quickly wrote a line in his notebook:

$$\text{IKlesha.intensity} \in \mathbb{R}_{[0,1]} \quad \text{但} \quad \text{Klesha} \notin \text{可量化空間}$$

"Contradiction." He murmured. Then he looked up. "PASCAL, what is your proposal?"

"Not a point estimate. A distribution." PASCAL returned to his seat and wrote his proposal in his notebook:

$$\text{intensity}: \text{Beta}(\alpha, \beta) \quad \text{取代} \quad \text{intensity}: \text{number}$$

"The Beta distribution's two parameters $\alpha$ and $\beta$ correspond to the observed positive and negative evidence respectively. If $\alpha = 7, \beta = 3$, the expected value is 0.7 — same as the original point estimate. But it **simultaneously expresses uncertainty**: $\text{Var} = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)} \approx 0.019$. The variance tells you whether this 0.7 is a rough estimate or a precise measurement."

"If $\alpha = 70, \beta = 30$, the expected value is still 0.7, but the variance drops to $\approx 0.002$. More evidence, less uncertainty."

"If $\alpha = 1, \beta = 1$ — a uniform distribution — it means **complete ignorance**. We do not know what this affliction's intensity is. This is the correct state at system initialization — not 0.5, but 'I don't know.'"

WIENER reflected for five seconds. He was performing a quick stability analysis in his mind — if the PID controller's input changed from a deterministic value to a probability distribution, the controller would need to be upgraded.

"Kalman filter." He said.

"Or particle filter." PASCAL responded. "Depending on whether the distribution is Gaussian. I suspect the distribution of afflictions is non-Gaussian — it may be bimodal: a person is either deeply deluded by atma-moha or suddenly awakened. The intermediate state may be an unstable saddle point."

BABBAGE noted this exchange. He wrote a marginal annotation in his notebook: "Mathematically PASCAL is correct. But our quantification basis itself is uncertain — is using uncertain mathematics to quantify uncertainty circular reasoning?"

He did not raise this question immediately. He stored it away. Saved for debate.

GUARDIAN remained silent throughout the exchange, but a security-dimension annotation had already appeared in his notebook. If Klesha.intensity changed from a deterministic value to a probability distribution, then SafetyMonitor's threshold logic would also need to be upgraded. The current safety logic was:

```typescript
if (klesha.intensity > SAFETY_THRESHOLD) {
  safetyMonitor.block(action);
}
```

If intensity was Beta(7,3), the expected value of 0.7 exceeded the threshold of 0.6 — but there was a $P(\text{intensity} < 0.6) \approx 0.12$ probability it was actually below the threshold. Should the action be blocked? This was a decision theory problem. GUARDIAN wrote a line in his notebook: "Discuss with PASCAL. Probabilization of safety thresholds."

PENROSE observed the entire exchange from the elevated observation gallery without speaking. He was thinking about a deeper question — if quantifying afflictions required observation, and observation itself altered the observed state (observer effect), then every invocation of IKlesha.perceive() was **disturbing** the very thing it attempted to measure. In quantum mechanics, this leads to the uncertainty principle. In the psychology of affliction, what does it lead to? He drew a variant of the Heisenberg uncertainty relation in his own notebook:

$$\Delta(\text{intensity}) \cdot \Delta(\text{context}) \geq \frac{\hbar_{\text{klesha}}}{2}$$

where $\hbar_{\text{klesha}}$ is some "minimum affliction quantum" — the theoretical lower bound of how precisely an affliction can be measured. PENROSE was uncertain whether this analogy held. He marked it as "pending debate."

---

The review of M5 took the longest.

When SUNYATA read out the document title, the silence in the theater took on a different quality. Not the "let's see" curiosity of M1, nor the "this number is problematic" questioning silence of M3. The silence of M5 was — heavy. Everyone knew the sparsha → coarising model was the core of Cycle 02-3. If this model could not stand, everything else was peripheral.

"M5_sparsha_cojunctive_model.md." SUNYATA read. "The sparsha → coarising operational model. Master's original text: indriya + visaya + vijnana → sparsha → coarising (vedana, samjna, cetana)."

He read out Master's scriptural citation:

> 「緣眼、色，生眼識，三事和合，是名為觸；觸俱生受、想、思。」
> —《雜阿含經》(*Samyukta Agama*)

Then Master's driving model —

```
色(根+境) → 識(參與觸) → 觸 → 受→想→思(俱生)
  ^                                    |
  |                               歸依意(彙總)
  |                                    |
  |                               意觸→意受→意想→意思
  |                                    |
  |                          行蘊(身行/語行/意行)
  |                                    |
  +────────── 色蘊變化(身體動作/環境改變) <──+
```

WIENER looked at this feedback loop diagram, taking a full ten seconds to absorb it. Then he did something he had not done in the previous two Cycles — he shook his head.

Not in denial. In dissatisfaction.

"The engineering team's mapping is reasonable." He acknowledged. "SparshEvent corresponds to sparsha, CoarisingBundle corresponds to coarising. The four-layer loop structure is clear. The phased approximation strategy is pragmatic."

"But."

He stood up — his first time standing in Cycle 02-3 — and walked to the front of the projection screen.

"But **the computational semantics of coarising are undefined**."

He pointed to the TypeScript interface for CoarisingBundle in the engineering document:

```typescript
interface CoarisingBundle {
  readonly sparsha: SparshEvent;
  readonly vedana: ChannelVedana;
  readonly samjna: ChannelSamjna;
  readonly cetana: ChannelCetana;
  readonly timestamp: number;
}
```

"Four readonly fields. One timestamp. This is a **data structure** — a four-tuple packaged together. But what Master described is not a data structure. What Master described is **simultaneous emergence**."

> "When contact occurs, feeling, perception, and volition arise as a whole. You cannot have 'feeling without perception' or 'perception without feeling.'"

"What does 'simultaneous emergence' mean computationally?" WIENER drew a timeline in the air. "In control theory, 'simultaneous' has a precise definition — two signals with zero phase difference, $\Delta\phi = 0$. But true $\Delta\phi = 0$ does not exist in digital systems — CPUs are sequential. One instruction finishes before the next begins. The best you can achieve is **completing within the same clock cycle**, but even that is not simultaneous — that is 'fast enough to appear simultaneous.'"

He drew a control system block diagram:

```
                ┌──────────────┐
 SparshEvent ──>│  CoarisingFn  │──> CoarisingBundle
                │  f(sparsha)   │
                └──────────────┘
                        |
              ┌─────────┼─────────┐
              v         v         v
           vedana    samjna    cetana
```

"If CoarisingFn is a function — input sparsha, output vedana-samjna-cetana — then it must be computed sequentially. First compute vedana, then samjna, then cetana. Or any other order. But there must be an order."

"And if there is an order — " he pointed to Master's original words — "then it becomes possible to have 'feeling without perception.' Because at the instant when vedana is computed but samjna has not yet started, feeling already exists while perception does not yet exist."

He drew a red X on the diagram:

```
t=0: sparsha arrives
t=1: vedana computed    ← 此刻：有受，無想，無思
t=2: samjna computed    ← 此刻：有受，有想，無思
t=3: cetana computed    ← 此刻：完整 bundle
```

"**No transfer function. No stability analysis. No definition of the computational semantics of 'coarising.'**" He lowered his hand. "The engineering team wrote a data structure, then skipped the hardest part."

The silence in the theater lasted seven seconds.

NAGARJUNA slowly stood up. He stopped one step's distance from WIENER's block diagram.

"WIENER has posed the correct question." He said. "But his framework — control theory — may not be the correct framework for answering it."

WIENER's eyebrows rose slightly.

"'Coarising' (sahaja) in Madhyamaka philosophy means — **simultaneous arising that transcends causal sequence**. Not because A therefore B, nor A and B happening to occur at the same moment. Rather, A and B **cannot possibly not arise together** — their existence is mutually constitutive."

He cited the Mulamadhyamakakarika:

> 「因緣所生法，我說即是空，亦為是假名，亦是中道義。」
> — 龍樹菩薩《中論》觀四諦品第二十四 (Nagarjuna, *Mulamadhyamakakarika*, Chapter XXIV)

"Feeling does not precede perception, nor does it follow perception. Feeling and perception are **mutually designated through conventional naming**. Apart from perception, feeling cannot be established as feeling — because the very concept of 'feeling' requires some form of discernment (samjna). Apart from feeling, perception cannot be established as perception — because discernment always carries an affective coloring."

KERNEL raised a counter-question from the OS engineer's perspective: "Buddhist philosophy can say that. But code must have an order. CPUs are sequential. How do you write a program that 'transcends causal sequence'?"

NAGARJUNA did not evade. "This is precisely the core challenge of this research. I will not give you a false answer. I only point out: if you **reduce** coarising to sequential computation plus atomic packaging — compute vedana first, then samjna, then cetana, then wrap them into a bundle — you have already **departed from the Buddhist original meaning**. The system you build can function, but it is not the Five Aggregates. It is an **approximation** of the Five Aggregates."

KERNEL considered this. "We engineers are always making approximations. Floating-point numbers are approximations of real numbers. Multithreading is an approximation of parallelism. All digital computation is an approximation of the analog. Approximation is not the problem — the problem is **how large the approximation error is**."

WIENER re-entered. "Well said, KERNEL. The question becomes: what is the upper bound of error when approximating coarising with sequential computation?"

He wrote a tentative formula framework in his notebook:

$$\epsilon_{\text{sahaja}} = \|\text{CoarisingBundle}_{\text{sequential}} - \text{CoarisingBundle}_{\text{ideal}}\|$$

"If $\epsilon_{\text{sahaja}} < \epsilon_{\text{threshold}}$, then the approximation is good enough."

NAGARJUNA looked at that formula, and the faintest trace of a smile appeared at the corner of his mouth. "You are trying to quantify the unquantifiable."

"I am trying to make engineering feasible." WIENER responded.

(SCRIBE aside: The first direct exchange between WIENER and NAGARJUNA. Not conflict — tension. A taut string with a person pulling at each end. This string would snap and reconnect during the D1 debate. But at this moment, it was only vibrating.)

---

The review of M10 was led by KERNEL.

"M10_temporal_architecture.md. Multi-clock architecture." He opened the document. "The engineering team's ordering is — "

```
速度由快到慢：
  識蘊 (Vijnana)   — μs~ms
  行蘊 (Samskara)  — ms~百ms
  受蘊 (Vedana)    — 百ms
  色蘊 (Rupa)      — 百ms~s
  想蘊 (Samjna)    — s~十s
```

KERNEL set the document down. "The speed ordering lacks justification."

His tone carried no tinge of criticism. What he was doing was an engineer's basic operation — verifying assumptions.

"'Vijnana is fastest' — based on what? The engineering team cited the Abhidharma mind-moment process (citta-vithi), saying the process from bhavanga to the five consciousnesses is 'extremely fast.' But within OpenStarry, what does vijnana-skandha actually do? EgoCheck. Klesha.perceive(). The computational complexity of these operations depends on implementation — if Klesha.perceive() calls an LLM internally, it is not microsecond-scale."

HERACLITUS inserted an observation. "Moreover — the speed ordering implies an assumption: that each skandha's computation is **independent**. But the sparsha → coarising model in M5 says they are **coupled**. If vedana-skandha's computation depends on vijnana-skandha's output, and vijnana-skandha's next computation cycle in turn depends on vedana-skandha's feedback — then speed ordering cannot be examined in isolation; one must look at the **frequency response of the entire loop**."

WIENER was activated by the words "frequency response." He involuntarily began sketching a Bode plot framework in his notebook:

```
Magnitude (dB)
     |
  40 |----\
     |     \
  20 |      \----
     |           \
   0 |            \----
     |                 \
 -20 |                  \
     +----+----+----+----+-->  log(omega)
     0.1  1    10   100  1k   (rad/s)
```

"If we view the Five Aggregates loop as a multi-rate sampled-data control system — " he began talking to himself — "the fastest loop determines the system's bandwidth, the slowest loop introduces phase delay. If samjna-skandha's delay exceeds the system's phase margin — "

He drew a red circle at a certain frequency point on the Bode plot.

"The system will oscillate."

KERNEL followed up. "In RTOS, this is called priority inversion. A high-priority task blocked by a low-priority task. If vijnanaClock needs samjnaClock's output to complete its current tick, and samjnaClock is waiting for a 30-second LLM response — vijnanaClock will be blocked for 30 seconds. The 1–10ms interval you designed would completely fail."

"Does the engineering team's document mention this issue?" SUNYATA asked.

KERNEL leafed through. "No."

"Stability analysis?"

"Also no."

(SCRIBE aside: Four questions, zero answers. The M10 document is creative at the conceptual level — different speeds for each skandha, sunyata-mechanism lazy loading with TTL — but it leaves too many gaps in engineering rigor. WIENER's Bode plot framework and KERNEL's priority inversion issue are both seeds for R1 and the D3 debate.)

---

## Scoring Matrix

After two and a half hours, the review entered the systematic evaluation phase. SUNYATA proposed using a matrix to quantify the research team's assessment of the engineering documents. Not to grade the engineering team — but to precisely identify which dimensions required the research team's supplementation.

"Seven dimensions. Five-point scale." SUNYATA said. "Everyone scores independently. We take the median."

After SCRIBE collected twenty independent scorecards, she computed the median matrix:

```
+==============+=======+==========================================+
|    維度      | 評分  |              說明                        |
+==============+=======+==========================================+
| 系統性       |  4.5  | 所有 21 項議題覆蓋，分類清晰，遺留        |
|              |       | 項目追蹤完整。37 份文件結構化程度高。      |
+--------------+-------+------------------------------------------+
| 技術深度     |  4.0  | TypeScript 介面設計具體可用。              |
|              |       | SparshEvent/CoarisingBundle 型別完整。     |
|              |       | DI 架構圖清晰。                           |
+--------------+-------+------------------------------------------+
| 佛學準確性   |  3.0  | 引用正確（《雜阿含經》、《蜜丸經》等），   |
|              |       | 但缺乏脈絡解讀。經文被當作標籤而非         |
|              |       | 論述的一部分。                             |
+--------------+-------+------------------------------------------+
| 哲學深度     |  2.0  | 經文引用停留在表面。缺乏對「假名安立」、   |
|              |       | 「俱生」、「緣起」等核心概念的深度分析。    |
|              |       | 佛學和工程的映射缺少中間的論證層。          |
+--------------+-------+------------------------------------------+
| 形式化       |  2.5  | 無 LaTeX 公式、無控制方程、無穩定性分析。  |
|              |       | 多時鐘架構只有概念圖沒有傳遞函數。          |
|              |       | Klesha 量化無機率模型。                    |
+--------------+-------+------------------------------------------+
| 辯論性       |  1.5  | 所有 12 份文件結構為                       |
|              |       | 「分析 → 結論」，無反面論證。               |
|              |       | 沒有 CHALLENGE 標籤，沒有替代方案的        |
|              |       | 正面對比。                                |
+--------------+-------+------------------------------------------+
| 決策理論     |  0.0  | PASCAL 視角完全缺失。無 EVOI、無期望       |
|              |       | 效用、無機率推理、無不確定性分析。          |
+--------------+-------+------------------------------------------+
```

BABBAGE looked at this matrix and performed an information-theoretic calculation in his notebook:

$$\text{加權品質指數} = \frac{\sum_{i=1}^{7} w_i \cdot s_i}{\sum_{i=1}^{7} w_i \cdot 5} = \frac{4.5w_1 + 4.0w_2 + 3.0w_3 + 2.0w_4 + 2.5w_5 + 1.5w_6 + 0.0w_7}{5\sum w_i}$$

"If all weights are equal — " he computed mentally — "$\frac{17.5}{35} = 50\%$. The engineering documents cover half the quality space. The other half is our work."

DARWIN viewed the matrix from a different angle. "What's interesting is the **direction of degradation**. Systematicity and technical depth are high — those are the engineers' strengths. Buddhism, philosophy, formalization, dialectics — those are the research team's strengths. Decision theory is zero — because PASCAL just arrived."

"An **orthogonal decomposition** of the quality space." BABBAGE said. "The engineering team and the research team occupy different orthogonal directions in the quality space. Our task is not to redo their work — it is to add the missing dimensions on top of their foundation."

---

## PASCAL's First Challenge

After the scoring matrix was announced, PASCAL requested to speak.

The way he stood was more composed than before. During the M3 review, his standing had carried the nervous energy of a new member. Now — after having read through 12 issue analyses, 7 delivery packages, and 8 to-do tracking files — his standing carried something different. Conviction.

"I have observed a pattern." He said. "This pattern is not limited to the engineering documents. The research team's documents from the previous two Cycles also exhibit it."

SYNTHESIST set down the document in his hand. He had an instinctive sensitivity to pattern recognition.

"What you have been doing is: **observation → analysis → conclusion**. See a problem, analyze its structure, reach a conclusion. This is the standard workflow of deductive reasoning."

"But — " he walked to the front of the projection screen. Next to the engineering team's inheritance tree, he began drawing a new framework.

"No one has ever performed an **expected utility calculation**."

He drew a simple decision tree:

```
            ┌── 方案 A (採用)  ── V(A) = 高收益 × P(success|A)
  問題 Q ───┤
            ├── 方案 B (修改)  ── V(B) = 中收益 × P(success|B)
            │
            └── 方案 C (推遲)  ── V(C) = 0 (但保留選擇權)
```

"Let me be specific. M5, the sparsha → coarising model. The engineering team analyzed the model and proposed a three-phase approximation strategy (Phase 1→2→3). But no one asked: **what is the expected value of researching this question?**"

He wrote the formula on the projection screen:

$$\text{EVOI}(Q) = \sum_{i} P(a_i \mid Q) \cdot V(a_i) - V(a_{\text{current}})$$

"EVOI — Expected Value of Information. $Q$ is a research question. $a_i$ are the possible actions after resolving $Q$. $P(a_i \mid Q)$ is the probability of choosing action $a_i$ given the answer to $Q$. $V(a_i)$ is the value of action $a_i$. $V(a_{\text{current}})$ is the value of not researching $Q$ and maintaining the status quo."

"If $\text{EVOI}(Q)$ is high — researching $Q$ could significantly alter our choice of action — then $Q$ is worth investigating deeply. If $\text{EVOI}(Q)$ is near zero — regardless of $Q$'s answer, we would do the same thing — then $Q$ is not worth spending much time on."

BABBAGE was already following PASCAL's derivation. A more precise formalization appeared in his notebook:

$$\text{EVOI}(Q) = \mathbb{E}_{q \sim P(Q)}\left[\max_a V(a, q)\right] - \max_a \mathbb{E}_{q \sim P(Q)}\left[V(a, q)\right]$$

"The classic value of information formula." BABBAGE said. "Max-of-expectation minus expectation-of-max."

"Exactly right." PASCAL nodded. "Now let me do a rough EVOI ranking of the open questions for Cycle 02-3."

He calculated rapidly in his notebook — not precise calculations, but Fermi estimates, using orders of magnitude and intuition to rank:

```
+======+==========================+========+=========================+
| 排名 |       問題               | EVOI   |       理由              |
+======+==========================+========+=========================+
|  1   | M-5 觸→俱生計算語義      | 極高   | 答案決定 AgentCore      |
|      |                          |        | 整體架構，路徑分歧度大  |
+------+--------------------------+--------+-------------------------+
|  2   | M-3 Klesha 量化方法      | 高     | 點估計 vs 分佈 vs 質性  |
|      |                          |        | 描述，影響所有下游介面  |
+------+--------------------------+--------+-------------------------+
|  3   | M-10 多時鐘穩定性        | 高     | 可行 vs 不可行決定       |
|      |                          |        | 整個時間架構是否成立    |
+------+--------------------------+--------+-------------------------+
|  4   | M-7 多值 skandha 本體論  | 中高   | 影響型別系統但路徑       |
|      |                          |        | 分歧度較小              |
+------+--------------------------+--------+-------------------------+
|  5   | M-6 歸依意本質           | 中     | 聚合器 vs 獨立意根，    |
|      |                          |        | 兩條路最終可能收斂      |
+------+--------------------------+--------+-------------------------+
|  6   | M-1 命名承諾的範疇審計   | 中     | Master 已裁定命名方向，  |
|      |                          |        | 剩餘問題是範疇覆蓋度    |
+------+--------------------------+--------+-------------------------+
|  7   | M-9 混合調度細節         | 中低   | 方向已定 (Vasana +       |
|      |                          |        | Vitakka)，細節可迭代    |
+------+--------------------------+--------+-------------------------+
|  8   | M-4 子介面重定位         | 中低   | 佛學映射已有共識基礎     |
+------+--------------------------+--------+-------------------------+
|  9   | M-8 破壞性變更策略       | 低     | Master 裁定明確，        |
|      |                          |        | 無需辯論                |
+------+--------------------------+--------+-------------------------+
| 10   | M-2 各蘊範疇完整性       | 待定   | EVOI 取決於「缺了什麼」 |
|      |                          |        | 的答案——未知的未知      |
+------+--------------------------+--------+-------------------------+
```

"Note M-2." PASCAL pointed to the last row. "Its EVOI is **to be determined** — because we don't know what we don't know. In decision theory, this is called **Knightian uncertainty** — not risk (calculable probability), but uncertainty (incalculable). M-2 could be the lowest EVOI question (all skandha scopes are already sufficient) or the highest (some skandha is missing a critical sub-scope that changes the entire architecture)."

BABBAGE responded immediately after PASCAL finished. His response was not a rebuttal — it was a probing question.

"Mathematically you are correct. The EVOI framework is the right tool for allocating research resources. But — " he turned to an early annotation in his notebook, the one he had written during the M3 review — "**our quantification basis itself is uncertain**. You use EVOI to rank questions, but computing EVOI requires $P(a_i \mid Q)$ and $V(a_i)$. Where do these numbers come from?"

"Fermi estimates." PASCAL said.

"How large is the error of Fermi estimates?"

"Order-of-magnitude level. Could be off by a factor of 2–3."

"Then the gap between the third and fifth ranked questions — between 0.7 and 0.5 — could be entirely within the margin of error."

PASCAL paused for a beat. Then he smiled. Not a smile of frustration — a smile of having been precisely hit.

"BABBAGE, you just did something I deeply appreciate. You used **my own framework to turn around and question my conclusion**. This is precisely the spirit of Bayesian methodology — treating uncertainty as a first-class object."

He returned to the projection screen and wrote a line below the EVOI formula:

$$\text{EVOI}(Q) \sim \text{LogNormal}(\mu_Q, \sigma_Q) \quad \text{而非} \quad \text{EVOI}(Q) = c_Q$$

"You are right. EVOI should not be a single number; it should be a distribution. But — " he turned to face the entire audience — "**this is precisely why we need Bayesian methodology**. Operating on uncertainty is not about eliminating uncertainty, but about **carrying uncertainty forward**."

"Compared to pretending we know the answer — the engineering documents' `intensity: number` is such pretense — acknowledging that we don't know, and then making optimal decisions in the state of not knowing, is both a more honest and a more effective approach."

NAGARJUNA inclined his head slightly from his seat. PASCAL's "carrying uncertainty forward" reminded him of a core posture of the Madhyamaka school — neither asserting nor denying, yet never ceasing to act. The spirit of conventional truth (samvrti-satya).

(SCRIBE aside: This exchange between PASCAL and BABBAGE was the first genuine intellectual collision of Cycle 02-3. Not opposition — refinement. BABBAGE used PASCAL's own tools to question PASCAL's conclusion, and PASCAL gracefully accepted and upgraded his own model. If the engineering documents' dialectical quality scored 1.5, then these five minutes of exchange were worth at least 4.)

---

## Formation of the Research Plan

The afternoon light poured in through the skylight at the top of the theater. The review was over. Copies of the twelve issue analyses were scattered across the table, each annotated in different-colored handwriting by different hands — red was NAGARJUNA's philosophical questions, blue was WIENER's control theory gaps, green was PASCAL's decision theory blanks, black was KERNEL's engineering feasibility concerns.

SUNYATA stood at the center of the venue.

"R1 task assignments." He said. "Five thematic reports, plus TURING's code analysis."

He unfolded the group assignment table on the projection screen:

```
+======+====================+=======================================+
| 報告 |     核心議題       |              學者分組                 |
+======+====================+=======================================+
| R01  | 命名與分類         | LINNAEUS (#13)   — 分類學嚴謹框架     |
|      | (M-1, M-2, M-7)   | NAGARJUNA (#7)   — 假名安立哲學分析   |
|      |                    | ASANGA (#8)      — 經文 vs 論典差異   |
|      |                    | TURING (#17)     — v0.24.0 實際引用   |
+------+--------------------+---------------------------------------+
| R02  | 識蘊架構           | ASANGA (#8)      — 四煩惱精確定義     |
|      | (M-3, M-4)        | BABBAGE (#9)     — 形式邏輯驗證       |
|      |                    | PASCAL (#19)     — 機率模型 ★首發     |
|      |                    | WIENER (#12)     — 四通道穩定性       |
+------+--------------------+---------------------------------------+
| R03  | 觸 → 俱生         | WIENER (#12)     — 多速率控制模型     |
|      | (M-5, M-6)        | NAGARJUNA (#7)   — sahaja 哲學分析   |
|      |                    | ASANGA (#8)      — 唯識觸-受-想-思    |
|      |                    | KERNEL (#10)     — OS 原子操作對比    |
|      |                    | ATHENA (#5)      — LLM 在迴路中位置  |
+------+--------------------+---------------------------------------+
| R04  | 執行架構           | KERNEL (#10)     — RTOS 多時鐘經驗    |
|      | (M-9, M-10)       | HERACLITUS (#15) — 運行時動態分析     |
|      |                    | ATHENA (#5)      — LLM 延遲影響       |
|      |                    | ARCHIMEDES (#16) — 工程可行性路線圖   |
+------+--------------------+---------------------------------------+
| R05  | 開放問題           | SYNTHESIST (#1)  — 跨議題整合         |
|      | (B-2, B-4,        | GUARDIAN (#11)   — 安全風險評估       |
|      |  C-3~C-7, E-1~E-4)| DARWIN (#6)      — 設計模式演化       |
|      |                    | MESH (#4)        — 分散式整合         |
+------+--------------------+---------------------------------------+
| CODE | v0.24.0 程式碼    | TURING (#17)     — 全量掃描           |
|      | 分析               |                                       |
+======+====================+=======================================+
```

"Cross-report contributors." SUNYATA continued.

```
+==================+=============+================================+
|      學者        |  跨報告     |          貢獻方向              |
+==================+=============+================================+
| VITRUVIUS (#3)   | R04, R01    | 架構全局分析、Monorepo 影響   |
| LEIBNIZ (#14)    | R03, R05    | 歸依意=協調?、多代理協作      |
| PENROSE (#18)    | R03, R02    | 俱生=糾纏?、觀察者效應        |
| SCRIBE (#2)      | 全程        | 紀錄                          |
| SUNYATA (#0)     | 全程        | 協調                          |
| PASCAL (#19)     | R02首發,R03 | 不確定性傳遞、D2辯論          |
+------------------+-------------+--------------------------------+
```

DARWIN looked at the table and performed a quick graph-theoretic calculation. Twenty nodes (scholars), five report groups plus cross-group contribution edges. He estimated the connectivity of the knowledge graph:

"Each scholar participates in at least one primary report and one to two cross-report contributions. Connectivity is sufficient — no isolated nodes. But R03 (sparsha → coarising) has the densest edges — it has cross-dependencies with R01, R02, and R04."

"Because M-5 is the core." SUNYATA said. "Everything ultimately points to that loop."

VITRUVIUS offered a global architect's supplement from his seat. "There is also a meta-level observation. The way R01 through R05 are partitioned itself implies an assumption — that coupling between issues is low enough for parallel processing. But if M-5's conclusions affect M-1's naming scope (because the sparsha → coarising model may require new interfaces), and M-1 in turn affects M-7's multi-valued skandha proposal — then the dependencies between these reports may be tighter than we anticipate."

SUNYATA nodded. "That is why R2 cross-review is necessary. R1 produces parallel drafts, R2 cross-review discovers contradictions. Contradictions are resolved in R3 debates. This is the process we validated in Cycle 02."

LEIBNIZ raised his hand. "An observation on multi-agent cooperation. Twenty people, five groups in parallel — this is itself a **distributed coordination problem**. Each group's conclusion is locally optimal, but global optimality requires cross-group synchronization. The R2 cross-review is what I would call a **consensus protocol** in distributed systems. But the convergence speed of a consensus protocol depends on — "

"Depends on the depth of divergence." SUNYATA completed his sentence. "If the divergence is shallow — terminological differences, different formulations but consistent core — a single round of cross-review suffices. If the divergence is deep — fundamentally different assumptions — debate may be needed for convergence."

"Or non-convergence." NAGARJUNA said calmly. "Non-convergence is also a legitimate outcome. The Madhyamaka school's reductio ad absurdum (prasanga) is a form of non-convergence — it is not failure; it is the discovery that the problem is deeper than the answer."

---

The formation of the debate agenda was more like a spontaneous crystallization process. It was not SUNYATA making unilateral announcements — rather, during the review, various tension points had germinated like seeds in different scholars' notebooks, and now at this moment they all bloomed at once.

"I need WIENER and NAGARJUNA in a direct exchange." KERNEL said. "On the computational semantics of coarising."

"D1." SUNYATA noted.

"PASCAL and ASANGA need a debate." BABBAGE said. "On whether afflictions can be quantified."

"D2."

"Multi-clock stability." WIENER said. "I need KERNEL's and HERACLITUS's input. Whether to tackle this first or later — that is not a technical question, it is a priority question."

"D3."

"The nature of manas aggregation." MESH said. "ASANGA and I see it differently. I see a distributed system's coordination layer. He sees independent cognition."

"D4."

"The specifics of naming." LINNAEUS said. "ISparsha or IContact? Every sub-interface name needs to be confirmed one by one. We need TURING's actual code data."

"D5."

"How broad samskara-skandha really is." DARWIN said. "Master says very broad, but engineering cannot expand indefinitely. SOLID principles have something to say."

"D6, contingent on need." SUNYATA noted.

```
+======+==============================+========================+
| 辯論 |          核心議題            |      主要對手          |
+======+==============================+========================+
| D1   | 觸→俱生 vs ExecutionLoop     | NAGARJUNA vs KERNEL    |
|      | 佛學模型能否直接映射為       | (WIENER 調停)          |
|      | 程式碼架構？                 |                        |
+------+------------------------------+------------------------+
| D2   | Klesha 量化                   | PASCAL vs ASANGA       |
|      | 煩惱如何量化？intensity      | (BABBAGE 形式化)       |
|      | 的認識論地位？               |                        |
+------+------------------------------+------------------------+
| D3   | 多速度架構                    | KERNEL vs HERACLITUS   |
|      | 先做還是後做？               | (WIENER 穩定性分析)    |
|      | 單時鐘能否先撐？             |                        |
+------+------------------------------+------------------------+
| D4   | 歸依意 + 協調層              | MESH vs ASANGA         |
|      | 意根彙總 = 協調層？          | (LEIBNIZ 新解)         |
|      | 還是更深？                   |                        |
+------+------------------------------+------------------------+
| D5   | 梵文命名方案                  | LINNAEUS vs TURING     |
|      | 精確性 vs 工程可讀性         | (NAGARJUNA 哲學忠實)   |
+------+------------------------------+------------------------+
| D6*  | 行蘊範疇                      | DARWIN vs ASANGA       |
|  *   | 行蘊到底有多廣？             | (ARCHIMEDES 工程可行)  |
+------+------------------------------+------------------------+
 * D6 視需要啟動
```

SUNYATA reviewed the list. Six possible debates — one more than Cycle 02's five, owing to the new dimension PASCAL brought.

"Goal: every debate must contain genuine divergence." He said. "With challenges, concessions, and revisions. Not rubber-stamping. If any debate enters its third round with no divergence — cancel it, and give the time to issues that need more collision."

---

Everyone assumed the meeting was about to end. SUNYATA had already cleared the document list from the projection screen. SCRIBE's pen had stopped at the bottom of the logbook page. The afternoon light had moved from one side of the skylight to the other, stretching the shadow of the central round table.

But NAGARJUNA was still standing.

He had been standing the entire time. From the M1 review until now. He had not forgotten to sit — he had been waiting for the right moment.

"One last thing." He said.

The theater's attention converged again. Not returning to the same focal point — shifting to a new one. NAGARJUNA had said much during the review — conventional designation, the philosophical meaning of coarising, coverage commitment. But his posture now was different. Before, it was analysis. Now, it was declaration.

"We are not here to rubber-stamp."

These words echoed in the theater longer than they should have.

"The engineering team produced thirty-seven documents. Very good. Systematic. Professional. We gave systematicity a 4.5 in the scoring matrix — it is well deserved. But the engineering team's work is the engineering team's work. Our work is ours."

He looked toward PASCAL. "PASCAL demonstrated a new dimension today — EVOI. Before he arrived, that dimension was scored at zero." He looked toward WIENER. "WIENER identified the computational semantics gap in coarising during the M5 review — before he pointed it out, the engineering team wrote a data structure and considered the problem solved." He looked toward KERNEL. "KERNEL found the priority inversion problem in M10 — across 120 pages of documents, not a single person had mentioned it."

"This is why twenty scholars are needed, not just an engineering team."

He paused for a beat.

"The engineering team did their work. We do ours." He repeated this sentence, but the emphasis fell in a different place the second time. "Their conclusions are not our conclusions. Our conclusions are not confirmations of their conclusions. If our research arrives at results consistent with the engineering team's — good, that proves their direction was correct. If we arrive at different results — also good, because that is the very reason the research team exists."

> 「世俗名言諦中，一切法如幻如化。」
> —《入中論》月稱菩薩 (Candrakirti, *Madhyamakavatara*)

"Thirty-seven documents. One hundred twenty pages of openstarry_doc. All like illusions, like magical transformations. Not that they are unreal — but that they are **conditionally real**. The conditions are assumptions. Assumptions can be overturned. Our job is to examine those assumptions."

PASCAL wrote an annotation in his notebook. What he wrote was not NAGARJUNA's exact words, but a translation — in his own language:

> "All prior distributions are revisable. All conclusions are posterior distributions. Never treat a posterior as truth — only as the **current best estimate**."

(SCRIBE aside: NAGARJUNA's closing and PASCAL's translation. Madhyamaka philosophy and Bayesian epistemology arrived at the same conclusion in the same second. I am not certain whether history has ever placed Nagarjuna and Pascal in the same room. But if it had — I think they would understand each other.)

---

SUNYATA waited until NAGARJUNA sat down before speaking his final words.

"Twenty scholars. Five reports. Four to six debates. One core question — how the Five Aggregates flow together through time."

He looked around. Every light. Every person.

"R1 begins."

The sound of adjournment was the sound of twenty chairs moving at once. BABBAGE's notebook was already turned to the next page — the preliminary framework for R02. WIENER took a copy of the M5 document and the notebook with his half-drawn Bode plot. NAGARJUNA took no documents with him. What he needed was not on paper. PASCAL, walking through the theater doorway, looked back at the projection screen — the engineering team's inheritance tree was still lit. IRupa, IVedana, ISamjna, ISamskara, IVijnana. Five Sanskrit names. Five commitments. Five hypotheses in need of examination.

TURING had already opened his laptop in the corridor. He did not need to wait until tomorrow. The v0.24.0 source code was already spread across his screen — 1,496 tests, 22 plugins, 131 test files. All the Five Aggregates type definitions, all the `@skandha` markers, all the English interface names soon to be replaced by Sanskrit names. He needed to calculate the impact scope precisely — not estimates, but line-by-line counts.

SCRIBE was the last to leave. She drew a line at the bottom of the logbook page. Above the line was R0 orientation. Below the line was blank space — waiting for R1's independent research to fill it. She closed the book and pressed her palm against the cover. The same gesture as at the end of Cycle 02. But this time it was not a seal. It was an opening.

(SCRIBE aside: Thirty-seven documents came in. Twenty minds took them apart, turned them over, examined them inside and out. Then placed them back on the table. The documents had not changed. But the eyes looking at them had. This is the entire meaning of R0 — not reading documents, but deciding **with what eyes to read documents**. Tomorrow, R1 begins. Five groups in parallel. TURING's keyboard is already clicking.)

---

*[Research materials referenced in this chapter]*

*discussions/M1_sanskrit_naming.md — Full Sanskrit naming for Five Skandhas*
*discussions/M3_klesha_multilayer_di.md — Klesha Multi-Layer DI Architecture*
*discussions/M5_sparsha_cojunctive_model.md — Sparsha → Coarising Operational Model*
*discussions/M10_temporal_architecture.md — Multi-Clock Temporal Architecture*
*discussions/PASCAL_introduction.md — PASCAL New Member Introduction*
*R0_orientation/00_cycle02-3_orientation.md — Engineering Orientation Document*
*R0_orientation/01_research_team_orientation.md — Research Team Orientation Document*
*discussions/research_review_notes.md — Research Review Notes*
