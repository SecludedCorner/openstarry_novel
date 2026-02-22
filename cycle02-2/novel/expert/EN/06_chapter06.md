# Chapter Six: The Root Systems of Five Trees

---

SUNYATA stood at the centre of the amphitheatre for a moment, saying nothing.

A-class had taken three chapters to correct the philosophy. B-class had taken one chapter to enact the rulings. Those were acts of dismantling and deciding. What needed to be done now was different.

Now it was time to build.

Not to patch cracks. Not to redraw boundaries. To unfold, skandha by skandha, a complete type-definition hierarchy upon corrected foundations. A-class told you where things were wrong. B-class told you how to fix them. C-1 tells you what the entire structure looks like after the repairs.

---

"C-1. The five skandha subclass expansion design."

He picked up Master's letter and found the passage.

"'The five skandhas can serve as root classes in object-oriented design. How they should be extended deserves a more detailed arrangement.'"

He paused briefly, then read a second passage.

"'The aggregation of the five skandhas must possess one or more -- or complex -- instances of control theory (the twelve links of dependent origination). But if it is a single, isolated skandha, in theory it should be incomplete.'"

He set the letter down. "The first four chapters corrected the foundations. Now, C-1 will grow the five trees from seed to complete living organisms -- root, trunk, and branch -- upon those corrected foundations."

He looked toward TURING. "Let us first see what the seeds look like now."

---

> *SCRIBE sidebar: SUNYATA used the image of "five trees." Not walls and pillars -- those are dead building materials. Trees are alive. Trees have roots, and roots extend. Trees have branches, and branches fork. The expansion of the five skandhas is not static accumulation -- it is organic, simultaneous growth in multiple directions. And trees have one more property: no two grow to the same height, the same girth, the same curvature. Five trees cannot be symmetric.*

---

TURING's screen projected into the centre of the amphitheatre. Cold light. White background. Black text.

What he projected was not an excerpt from some document. It was the `aggregates.ts` source code from v0.24.0-beta -- complete, unfiltered, 107 lines of the original file:

```typescript
/**
 * Five Aggregates (五蘊) Root Interfaces.
 *
 * These interfaces establish the philosophical-architectural foundation
 * of OpenStarry, mapping Buddhist Five Aggregates to software patterns.
 *
 * D-02 Decision: Dual naming — English as primary, Sanskrit as annotation.
 *
 * @module aggregates
 */

export interface ISensory {
  /** @skandha rupa */
  readonly skandha: 'rupa';
}

export interface ISensation {
  /** @skandha vedana */
  readonly skandha: 'vedana';
}

export interface ICognition {
  /** @skandha samjna */
  readonly skandha: 'samjna';
}

export interface IAction {
  /** @skandha samskara */
  readonly skandha: 'samskara';
}

export interface IIdentity {
  /** @skandha vijnana */
  readonly skandha: 'vijnana';
}

export type Skandha = 'rupa' | 'vedana' | 'samjna' | 'samskara' | 'vijnana';

export function isSkandha<S extends Skandha>(
  obj: unknown,
  skandha: S,
): obj is { skandha: S } {
  return (
    typeof obj === 'object' &&
    obj !== null &&
    'skandha' in obj &&
    (obj as { skandha: unknown }).skandha === skandha
  );
}
```

TURING let the projection linger for a full ten seconds. Five root interfaces, each containing only a single field -- `readonly skandha`. A label. A name. Five empty boxes with nothing but nameplates.

"Five root interfaces. No methods. No behaviour definitions. No sub-interface inheritance."

He pointed to the `IIdentity` segment -- the JSDoc read `Identity aggregate encompasses consciousness and ego framework`, as though a three-line empty shell could "encompass" consciousness and the ego framework.

"The more serious problem is here."

He switched to the second projection.

```typescript
// Existing concrete interfaces in v0.24.0-beta (scattered across different files)
export interface IUI { ... }       // rupa-skandha? Does not inherit ISensory
export interface IListener { ... } // rupa-skandha? Does not inherit ISensory
export interface IProvider { ... } // samjna-skandha? Does not inherit ICognition
export interface ITool { ... }     // samskara-skandha? Does not inherit IAction
export interface IGuide { ... }    // vijnana-skandha? Does not inherit IIdentity
```

"The existing concrete interfaces. Each has a complete set of method definitions -- IUI has `renderText`, `renderDelta`; IProvider has `chat`, `listModels`; ITool has `execute`. But between them and the five root interfaces there is no relationship whatsoever. No `extends`. No inheritance."

He drew a dashed line on the screen. "The nameplates and the doors are separate. You know that IUI should belong to rupa-skandha, but the type system does not. Calling `isSkandha(myUI, 'rupa')` returns `false` -- because the `myUI` object has no `skandha` field at all."

BABBAGE wrote a line in his notebook:

$$\text{roots} \cap \text{children} = \varnothing$$

The intersection of roots and children was the empty set. Orphans. In mathematics, a tree $T = (V, E)$ in which no edge exists between the root node $r$ and any leaf node is not a tree at all -- it is a disconnected graph. The number of connected components $c(G)$ of $G = (V, E)$ is $6$: each of the five roots forms its own component, and all sub-interfaces form another.

$$c(G_{\text{current}}) = 6 \quad \xrightarrow{\text{C-1}} \quad c(G_{\text{target}}) = 1$$

C-1 must merge six connected components into a single connected tree.

---

SUNYATA counted on his fingers. Five design objectives.

"One. Each skandha's root interface gains core methods -- not just empty shells, but behaviour definitions. Two. Existing interfaces are upgraded to sub-interfaces -- IUI extends ISensory, and so forth. Three. New sub-interfaces are added where necessary -- the IVijnana hierarchy, the three vedana interfaces. Four. The observer uses Composition and does not belong to any skandha. Five. isSkandha() is available at every level -- from root to leaf, the type guard passes all the way through."

Five fingers folded back. "Now, skandha by skandha."

---

## I

---

"Rupa-skandha. ISensory. Rupa (रूप)."

VITRUVIUS rose to his feet. Rupa-skandha -- form and materiality -- was the most intuitive domain for a full-stack architecture analyst.

"Rupa-skandha is the simplest of the five trees. Its two sub-interfaces already exist. IUI handles output rendering -- the mouth, what is spoken outward. IListener handles sensory input -- the ears, what is taken in. They need only `extends ISensory`."

He walked to the whiteboard and drew a simple bidirectional arrow diagram:

```
                 ISensory (rupa-skandha)
                ╱              ╲
    IUI (output rendering)  IListener (sensory input)
    ──────→ external         external ──────→
    renderText()             onDataReceived()
    renderDelta()            start() / stop()
```

"This is the core architectural characteristic of rupa-skandha -- **bidirectionality**. The data flow direction of IUI runs from Agent to the external world. The data flow direction of IListener runs from the external world to Agent. One is push, the other is pull. In full-stack architecture, this is the classic separation of front-end rendering and back-end listening -- no single `render-or-listen` method can simultaneously cover both directions."

"Therefore keeping the ISensory root interface as an empty shell is the correct design decision." He stepped back. "Not laziness -- restraint. When the intersection of the two sub-interfaces' common behaviour sets is the empty set -- $\text{methods}(\text{IUI}) \cap \text{methods}(\text{IListener}) = \varnothing$ -- forcibly defining methods on the root interface would manufacture a false abstraction. The root interface's purpose is not to carry methods but to carry a classification label. `readonly skandha: 'rupa'` is everything."

TURING projected the revised complete definitions.

```typescript
/**
 * ISensory — Rupa-skandha Root Interface
 * @skandha rupa (rupa-skandha)
 *
 * Rupa-skandha encompasses all form and materiality:
 * - Output rendering (IUI): presenting information to the external world
 * - Sensory input (IListener): receiving external signals
 *
 * Sanskrit: Rupa (रूप)
 */
export interface ISensory {
  readonly skandha: 'rupa';
}

/**
 * IUI — Rupa-skandha Output Rendering Sub-interface
 * Presents the Agent's responses to users or external systems.
 */
export interface IUI extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
  /** Render complete text */
  renderText?(text: string, sessionId?: string, replyTo?: string): void;
  /** Render streaming delta */
  renderDelta?(delta: string, sessionId?: string, replyTo?: string): void;
  /** Render tool execution status */
  renderToolStatus?(name: string, status: string, sessionId?: string, replyTo?: string): void;
}

/**
 * IListener — Rupa-skandha Sensory Input Sub-interface
 * Receives external signals and transforms them into InputEvents.
 */
export interface IListener extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
}
```

"A single `extends`." TURING said. "The modification is minimal, but the semantic shift is fundamental -- from now on, any implementation of `IUI` is necessarily also an `ISensory`. `isSkandha(myDiscordUI, 'rupa')` will return `true`. Nameplate and door are connected."

ASANGA added a line from his seat. His pace was unhurried, every word carrying the precision of a Yogacara scholar.

"Rupa-skandha is contact. Contact with the external world. In the Abhidharma, the basic definition of rupa is 'that which can be disrupted' (rupyate) -- things that can be touched, things that can be changed. IUI is the Agent's reach toward the external world. IListener is the external world's reach toward the Agent. The two directions of contact. The completeness of rupa-skandha is guaranteed in the unification of these two directions."

---

> *SCRIBE sidebar: Rupa-skandha, three minutes. One `extends`. VITRUVIUS explained why the root interface should remain empty -- not every empty shell needs to be filled. Some containers derive their meaning from being containers. The first root of the first tree -- the shortest one -- sank into the soil.*

---

## II

---

"Vedana-skandha. ISensation. Vedana (वेदना)." SUNYATA's voice slowed perceptibly. Everyone knew that vedana-skandha would be the tree with the most expansive root system of all five.

WIENER was already flipping through his graph paper. His pen tip rested beside a freshly drawn block diagram -- three parallel PID loops, each labelled $K^{(\text{dukkha})}$, $K^{(\text{sukha})}$, $K^{(\text{upekkha})}$.

"ISensation undergoes the greatest transformation," SUNYATA said. "From an empty shell to eight core methods. WIENER, confirm each one."

TURING projected the complete interface. This time he used no excerpts but projected the full definition including JSDoc comments and auxiliary types.

```typescript
/**
 * ISensation — Vedana-skandha Root Interface
 * @skandha vedana (vedana-skandha)
 *
 * Vedana-skandha encompasses the three vedanas (three types of feeling):
 * - Dukkha (suffering): negative feedback
 * - Sukha (pleasure): positive feedback
 * - Upekkha (equanimity): neutral balance
 *
 * Vedana-skandha is the "feeling layer" -- it does not judge
 * (judgement belongs to samjna-skandha/vijnana-skandha).
 * The VedanaAssessment produced by vedana-skandha is consumed
 * by other skandhas (e.g. vijnana-skandha's EgoFramework).
 *
 * Sanskrit: Vedana (वेदना)
 */
export interface ISensation {
  readonly skandha: 'vedana';

  /** Assess the current three-vedana state — a complete sensor readout */
  assess(): VedanaAssessment;

  /** Ingest system metrics — general numerical input channel */
  ingestMetrics(metrics: Record<string, number>): void;

  /** Ingest tool execution result — samskara-skandha reporting channel */
  ingestToolResult(toolName: string, isError: boolean, durationMs: number): void;

  /** Ingest LLM response result — samjna-skandha reporting channel */
  ingestLLMResult(tokenCount: number, stopReason: string): void;

  /** Get vedana tag (cached lookup, O(1)) */
  getVedanaTag(): VedanaTag;

  /** Subscribe to events of a specific vedana type */
  onVedana(
    type: VedanaType,
    threshold: number,
    handler: (signal: VedanaSignal) => void
  ): () => void;

  /** Get historical assessment records */
  getHistory(windowSize: number): readonly VedanaAssessment[];

  /** Reset feeling state */
  reset(): void;
}

/** Three vedana types */
type VedanaType = 'dukkha' | 'sukha' | 'upekkha';

/** Vedana tag (for event marking) */
type VedanaTag = 'dukkha' | 'sukha' | 'upekkha';

/** Vedana signal */
interface VedanaSignal {
  readonly type: VedanaType;
  readonly intensity: number;     // 0.0–1.0
  readonly source: string;
  readonly timestamp: number;
}

/** Vedana assessment report */
interface VedanaAssessment {
  // ── Sensing layer (pure observation) ──
  readonly dukkha: number;        // 0.0–1.0
  readonly sukha: number;
  readonly upekkha: number;
  readonly signals: readonly VedanaSignal[];
  readonly timestamp: number;

  // ── Control recommendation layer (advisory, may be ignored) ──
  readonly controlOutput: number;
  readonly recommendation: VedanaRecommendation;
  readonly recommendationFreshness: 'current' | 'cached' | 'default';
}
```

---

WIENER stood.

He did not look at the projection. He looked at the framework he had pre-drawn on his graph paper -- an eight-station acceptance checklist for a control system. He pointed to each station in turn, his voice carrying the precise rhythm of an engineer testing every solder joint on an assembly line.

"First. `assess()`."

He wrote the control-theory correspondence on the graph paper:

$$y(t) = h(x(t)) + v(t)$$

"The sensor readout function. Input is the system's internal state $x(t)$, output is the observable quantity $y(t)$, $v(t)$ is measurement noise. `assess()` does not alter system state -- it only reads. This is vedana-skandha's most fundamental operation: what do I feel right now. A complete three-vedana readout."

"Second, third, fourth. `ingestMetrics()`, `ingestToolResult()`, `ingestLLMResult()`."

He took all three together.

"Three input channels. In control theory, this is **multi-input sensor fusion**. Different channels receive different modal signals -- system metrics are quantified values (CPU usage, memory consumption, response latency); tool execution results are discrete events (success/failure + duration); LLM response results are language model metadata (token count, stop reason). Three channels converging into a single sensor, each with distinct preprocessing logic."

He drew the fusion diagram on the graph paper:

```
  ingestMetrics ─────────────┐
                              │
  ingestToolResult ──────────→ ISensation ──→ assess()
                              │
  ingestLLMResult ───────────┘
```

"Like the sensor array of a car -- the accelerometer is one channel, the gyroscope is another, GPS is a third. Three different data modalities that must be fused before the vehicle's complete state can be estimated."

"Fifth. `getVedanaTag()`."

His pace quickened slightly. "$O(1)$ cached lookup. The number on the dashboard -- you do not need to rerun the full `assess()` every time just to know whether the current state is dukkha, sukha, or upekkha. This is a **cached readout**. In a control system, it is equivalent to the LED indicator on the dashboard: green, yellow, red. It does not tell you details; it tells you the classification result. Cost is zero."

"Sixth. `onVedana()`."

He paused. The corner of his mouth lifted slightly -- the smile of an engineer encountering an elegant design.

"This is a generalization of the watchdog timer."

He wrote the formula on the graph paper. The classic definition of a watchdog timer: when a counter has not been reset within $T_{\text{wd}}$ time, the system enters an alarm state. `onVedana()` generalizes this concept from "timeout" to "threshold" -- not "no response for too long" but "dukkha exceeds 0.8", "sukha drops below 0.2", "upekkha deviates from the midline by more than 0.3".

$$\text{watchdog: } y(t) > T_{\text{timeout}} \Rightarrow \text{alarm}$$
$$\text{onVedana: } v_{\text{type}}(t) > \theta \Rightarrow \text{handler}(s)$$

"No continuous polling. No checking every tick. Event-driven threshold monitoring."

His finger moved to the seventh.

"`getHistory(windowSize)`."

This time he drew a more elaborate diagram on the graph paper -- the integral term of a PID controller.

$$I(t) = K_i \int_{t - W}^{t} e(\tau)\,d\tau \approx K_i \sum_{k=t-W}^{t} e(k) \cdot \Delta t$$

"Sliding window history. `windowSize` is the integration window $W$. The integral term of a PID controller requires historical data for computation -- the cumulative feelings across the past $W$ ticks. Without history, there is no integral. Without the integral, PID degrades to PD. A PD controller's ability to track steady-state error is zero -- chronic, long-term dukkha would be ignored."

He stepped back to take in the whole picture. "So `getHistory()` is not an optional convenience method. It is a **necessary condition** for the three-channel PID controller to function properly. Without it, the controller is crippled."

"Eighth. `reset()`."

His voice turned abruptly hard.

"**Emergency stop button**. E-Stop. Every industrial control system has a large red mushroom-head button on the operator's console. Press it and the system zeroes out. All history cleared. All counters zeroed. PID integral term emptied. Feeling state returned to initial values."

$$x(t^+) = x_0, \quad \int_0^{t} e(\tau)\,d\tau = 0$$

"You will not press it every day. But without it, the system is incomplete. Safety regulations require every machine to have an emergency stop button -- not because you frequently need it, but because you must always have the option."

Eight methods. Eight control-theory correspondences. WIENER turned to a fresh page on his graph paper -- the new page held the complete one-to-one correspondence table:

```
┌─────────────────────┬──────────────────────────────────────────┐
│ ISensation Method    │ Control Theory Correspondence            │
├─────────────────────┼──────────────────────────────────────────┤
│ assess()            │ Sensor readout function y = h(x) + v     │
│ ingestMetrics()     │ Composite sensor channel 1 (metrics)     │
│ ingestToolResult()  │ Composite sensor channel 2 (events)      │
│ ingestLLMResult()   │ Composite sensor channel 3 (LLM metadata)│
│ getVedanaTag()      │ Dashboard cached readout (O(1) LED)      │
│ onVedana()          │ Watchdog timer generalization (threshold) │
│ getHistory()        │ PID integral term window (sliding W)     │
│ reset()             │ Emergency stop (E-Stop, full state zero) │
└─────────────────────┴──────────────────────────────────────────┘
```

"The vedana-skandha root interface is no longer an empty shell." He set the graph paper down. "It is a complete sensor interface. Eight methods, each with a precise correspondence in control theory. Zero redundancy. Zero omissions."

---

ASANGA stood. Vedana-skandha required more space than rupa-skandha.

"WIENER used control theory to verify the engineering completeness of the eight methods. I shall use Buddhist studies to verify their semantic consistency."

His gaze swept across the eight method signatures on the projection, then turned to the entire room.

"Vedana-skandha does one thing. It feels. It does not judge. It does not analyse. Touch fire -- dukkha. Taste sweetness -- sukha. Nothing happens -- upekkha. The *Abhidharmakosa-bhasya*, fascicle one, defines vedana-skandha thus:"

> "The vedana aggregate is the threefold apprehension -- dukkha, sukha, and upekkha."
> -- Vasubandhu, *Abhidharmakosa-bhasya*, fascicle 1

"Threefold apprehension. Apprehension means receiving; it means containing. The entire function of vedana-skandha is: to receive feeling and to contain feeling."

He pointed to each method on the projection in turn.

"`assess` -- what do I feel at this moment. The output of apprehension. The `ingest` family -- through what channels have I apprehended what. These three methods correspond respectively to system-metric contact, tool-result contact, and linguistic-cognition contact. In the twelve links of dependent origination (nidanas), contact (sparsa) is the direct cause of feeling (vedana). $\text{contact} \to \text{feeling}$. Each `ingest` method is a form of contact -- contact occurs, feeling arises accordingly."

"`getVedanaTag` -- the label of feeling at this moment. Dukkha, sukha, upekkha -- one of three. Simple, direct, unadorned."

"`onVedana` -- the early warning of feeling. There is no exact counterpart in Buddhist studies, but the principle is consistent: when dukkha exceeds a certain intensity, the practitioner naturally takes notice. Mindfulness practice's awareness (sati) is a kind of `onVedana` -- not moment-to-moment active monitoring, but awareness arising spontaneously when a specific feeling appears."

"`getHistory` -- the memory of feeling. But note: this is a purely affective record, not an analysis of feeling. Analysis belongs to samjna-skandha. Recollection belongs to vedana-skandha -- I remember that I suffered, I remember that I rejoiced. This is **vedananupassana** (contemplation of feelings), not **vedana analysis**."

He placed particular emphasis on the next point. "`reset` -- reset. In practice, this resembles an extreme form of letting go -- clearing all accumulated feeling history, returning to the initial state. Not a daily operation. It is anomaly recovery."

He looked at the eight methods on the projection. Then he looked at WIENER.

"Eight methods. Every one of them falls within the domain of 'feeling.' Not a single method oversteps into judgement -- no `classify()`, no `decide()`, no `act()`. Your control theory says they are methods of a sensor. My Buddhist studies say they are methods of vedana-skandha."

WIENER noted a line on the margin of his graph paper:

`ISensation: 8 methods. Sensor ≡ Vedana. Cross-validated by control theory AND Abhidharma.`

---

TURING projected the three vedana sub-interfaces.

```typescript
/**
 * IDukkha — Vedana-skandha Dukkha Sub-interface (sensor)
 * Dukkha: negative feedback. The feeling of everything "wrong" in the system.
 */
export interface IDukkha extends ISensation {
  readonly vedanaType: 'dukkha';
  /** Compute dukkha intensity from metrics [0.0–1.0] */
  computePain(metrics: Record<string, number>): number;
}

/**
 * ISukha — Vedana-skandha Sukha Sub-interface (sensor)
 * Sukha: positive feedback. The feeling of everything "going well" in the system.
 */
export interface ISukha extends ISensation {
  readonly vedanaType: 'sukha';
  /** Compute sukha intensity from metrics [0.0–1.0] */
  computePleasure(metrics: Record<string, number>): number;
}

/**
 * IUpekkha — Vedana-skandha Upekkha Sub-interface (sensor)
 * Upekkha: neutral balance. The baseline feeling of a system running steadily.
 */
export interface IUpekkha extends ISensation {
  readonly vedanaType: 'upekkha';
  /** Compute equanimity level from metrics [0.0–1.0] */
  computeEquanimity(metrics: Record<string, number>): number;
}
```

WIENER added from his seat, his pen sketching rapidly on the graph paper: "Three sub-interfaces. Three sensor channels. Three sets of PID parameters."

He wrote three sets of gain matrices on the paper:

$$K^{(\text{dukkha})} = \begin{pmatrix} K_p^{(d)} & K_i^{(d)} & K_d^{(d)} \end{pmatrix} = \begin{pmatrix} \text{high} & \text{medium} & \text{low} \end{pmatrix}$$

$$K^{(\text{sukha})} = \begin{pmatrix} K_p^{(s)} & K_i^{(s)} & K_d^{(s)} \end{pmatrix} = \begin{pmatrix} \text{medium} & \text{high} & \text{medium} \end{pmatrix}$$

$$K^{(\text{upekkha})} = \begin{pmatrix} K_p^{(u)} & K_i^{(u)} & K_d^{(u)} \end{pmatrix} = \begin{pmatrix} \text{low} & \text{low} & \text{high} \end{pmatrix}$$

"Dukkha channel -- high proportional gain $K_p^{(d)}$. Pain does not wait; it demands rapid response. Sukha channel -- high integral gain $K_i^{(s)}$. Pleasure decays; the integral term tracks long-term trends. Upekkha channel -- high derivative gain $K_d^{(u)}$. Balance is dynamic and requires predictive regulation -- the trend of deviation matters more than the deviation itself."

He ticked three heavy checkmarks on the graph paper -- heavier than the seven from Chapter Five, pressing hard enough to leave three small indentations in the page.

"The three-channel architecture from Cycle 02 now has the backing of the type system. `IDukkha` is a subtype of `ISensation`. `computePain` exists only on the dukkha channel. You cannot call `computePain` on an upekkha sensor -- the type system will stop you. This is not merely classification. This is **type-safe three-channel isolation**."

"In place."

---

> *SCRIBE sidebar: Vedana-skandha, fifteen minutes. Five times that of rupa-skandha. Eight methods, each requiring WIENER's control-theory verification and ASANGA's Buddhist confirmation. Dual calibration. This is the discipline of Cycle 02-2 -- every design decision must pass cross-validation by at least two disciplines. WIENER's control theory is the first ruler, ASANGA's Yogacara is the second ruler. Only when both rulers measure the same length does a method hold its ground.*

---

## III

---

"Samjna-skandha. ICognition. Samjna (संज्ञा)."

ATHENA rose. Samjna-skandha -- cognition and discrimination -- was the most essential area of expertise for an AI/ML systems architect.

TURING projected the complete definition.

```typescript
/**
 * ICognition — Samjna-skandha Root Interface
 * @skandha samjna (samjna-skandha)
 *
 * Samjna-skandha encompasses cognition and discrimination:
 * - IProvider: LLM back-end, responsible for language understanding and generation
 * - IInferenceProvider: non-LLM inference capabilities (reserved)
 *
 * D-05 Decision: Provider covers the full cognitive processing spectrum.
 *
 * Sanskrit: Samjna (संज्ञा)
 */
export interface ICognition {
  readonly skandha: 'samjna';
}

/**
 * IProvider — Samjna-skandha Cognition Provider Sub-interface
 * LLM back-end, responsible for reasoning and language processing.
 */
export interface IProvider extends ICognition {
  readonly id: string;
  chat(request: ChatRequest): AsyncIterable<StreamEvent>;
  listModels?(): Promise<ModelInfo[]>;
}

/**
 * IInferenceProvider — Samjna-skandha Inference Provider Sub-interface (future extension)
 * Non-LLM inference capabilities, such as rule engines, decision trees, etc.
 */
export interface IInferenceProvider extends ICognition {
  readonly id: string;
  infer(input: unknown): Promise<unknown>;
}
```

ATHENA walked in front of the projection and drew an invisible line between `IProvider` and `IInferenceProvider` with her finger.

"Samjna-skandha has two branches. IProvider is the current workhorse -- the LLM back-end. The `chat()` method accepts a `ChatRequest` and returns an `AsyncIterable<StreamEvent>` -- an asynchronous streaming iterator. This is the standard interface for LLM reasoning: you give it conversation history, and it returns inference results token by token."

She turned to `IInferenceProvider`. "But cognition is not synonymous with language models. This is the core conclusion of D-05 -- Provider covers the 'cognitive processing spectrum,' not 'LLM invocation.' `IInferenceProvider` is the other end of that spectrum."

She drew a spectrum on the whiteboard:

```
Cognitive Capability Spectrum

Low complexity                                            High complexity
←───────────────────────────────────────────────────────→
│           │            │              │            │
Rule        Decision     Statistical    Neural       LLM
engines     trees        models         networks     (GPT/
(if-else)   (CART/       (Bayes/        (CNN/RNN/     Claude)
            Random       SVM)           Transformer)
            Forest)
│                                                    │
└──── IInferenceProvider ────┘ └──── IProvider ──────┘
```

"`IInferenceProvider`'s `infer()` method signature is `(input: unknown): Promise<unknown>` -- deliberately designed as generic. Because the input/output formats of a rule engine are entirely different from those of an LLM. A decision tree accepts a feature vector and returns a classification label. A statistical model accepts a numerical matrix and returns a probability distribution. You cannot unify all these formats under `ChatRequest`."

"But they are all cognition. All samjna-skandha. Discriminating external objects, making judgements. Different methods, same essence."

DARWIN leaned forward. His voice carried the sensitivity of a software pattern analyst attuned to evolutionary context.

"Evolutionarily, `IInferenceProvider` is the more primitive cognition."

He stood up. "Consider biological evolution. The most primitive cognition is phototaxis -- light is there, I move toward it. This is a rule engine: `if (light > threshold) then move(toward_light)`. No language whatsoever, no reasoning, only stimulus-response."

"Then comes conditioned reflex. Pavlov's dog. Associative learning between bell and food. This is a statistical model -- $P(\text{food} | \text{bell})$ updates with experience."

"Then comes abstract thought. Symbol manipulation. Language. Chains of reasoning. This is the LLM -- `chain-of-thought`, `multi-step reasoning`."

"IInferenceProvider and IProvider are not two parallel options. They are two branches on the same evolutionary tree -- one growing at a lower position, one at a higher position. The lower one is older, more robust, computationally cheaper. The higher one is more flexible, more powerful, computationally more expensive."

ASANGA, in one sentence. "Samjna-skandha is discrimination. The *Abhidharmakosa-bhasya*: 'The samjna aggregate is that whose nature is to apprehend characteristics.' Apprehending characteristics -- extracting the distinctive features of external objects. Discrimination takes more than one form. Rule engines discriminate by conditions, decision trees discriminate by branching, LLMs discriminate by language. The levels of discrimination differ, but all are functions of samjna-skandha."

---

> *SCRIBE sidebar: Samjna-skandha, five minutes. Slightly longer than rupa-skandha, far shorter than vedana-skandha. ATHENA's cognitive spectrum -- the complete range from rule engines to LLMs -- was the most farsighted projection of the entire chapter. It spoke not of today but of tomorrow. IInferenceProvider is a reserved empty shell at this moment. But in five years, ten years, when Agent systems begin integrating non-LLM cognitive modules, this shell will be filled. Good architecture design does not merely solve current problems -- it leaves precisely shaped openings for future ones.*

---

## IV

---

"Samskara-skandha. IAction. Samskara (संस्कार)."

DARWIN fully stood. Samskara-skandha was the core lens through which he observed software behavioural patterns.

TURING projected the definition.

```typescript
/**
 * IAction — Samskara-skandha Root Interface
 * @skandha samskara (samskara-skandha)
 *
 * Samskara-skandha encompasses volitional activities and concrete actions:
 * - ITool: executable tools
 * - ISlashCommand: slash commands
 *
 * Sanskrit: Samskara (संस्कार)
 */
export interface IAction {
  readonly skandha: 'samskara';
}

/**
 * ITool — Samskara-skandha Tool Sub-interface
 * Tools invoked autonomously by the Agent.
 */
export interface ITool extends IAction {
  readonly name: string;
  readonly description: string;
  readonly parameters: unknown;  // JSON Schema
  execute(args: Record<string, unknown>, ctx: ToolContext): Promise<string>;
}

/**
 * ISlashCommand — Samskara-skandha Command Sub-interface
 * Actions triggered by external users through slash commands.
 */
export interface ISlashCommand extends IAction {
  readonly name: string;
  readonly description: string;
  execute(args: string, ctx: IPluginContext, sessionId?: string): Promise<string | undefined>;
}
```

DARWIN walked in front of the projection.

"ITool -- actions invoked autonomously by the Agent. The LLM's reasoning determines when to call and what parameters to pass. `execute`'s `args` is `Record<string, unknown>` -- structured parameters, generated by samjna-skandha (IProvider) reasoning results."

"ISlashCommand -- actions triggered by external commands. The user types `/help`, `/clear` in the terminal, triggering the corresponding `execute`. `args` is `string` -- raw text, because user input is not structured."

"Different origins. ITool's initiator is the Agent (internal). ISlashCommand's initiator is the user (external). But same nature -- both are samskara. Both are the realisation of volition. Both are the final step from cognition to action."

He walked back to his seat. "Like rupa-skandha, samskara-skandha's root interface is also an empty shell. The reason is the same -- ITool and ISlashCommand have entirely different `execute` method signatures. One accepts a structured object, the other accepts a raw string. You cannot define a generic `execute` on the root interface."

ASANGA, in one sentence. "Samskara-skandha encompasses all formations. The *Abhidharmakosa-bhasya*, fascicle one: 'The samskara aggregate comprises all mental factors other than vedana and samjna, together with factors dissociated from mind.' Samskara-skandha has the broadest scope -- all mental activities except vedana-skandha and samjna-skandha fall under samskara-skandha. But the core is **cetana** (intention). Cetana is the initiation of volition. A tool's `execute` is a formation. A command's `execute` is also a formation. Different formations, same skandha."

---

> *SCRIBE sidebar: Samskara-skandha, four minutes. The second shortest among the five trees. DARWIN confirmed the simplest structure with the fewest words -- two sub-interfaces, two sources of action, one shared skandha label. Sometimes the elegance of design lies in this: let what should be simple remain simple.*

---

## V

---

"Vijnana-skandha. IVijnana. Vijnana (विज्ञान)."

SUNYATA's pace slowed below that of the previous four skandhas. This was the tree of greatest weight.

A-2 had demoted IIdentity from the entirety of vijnana-skandha to a sub-interface. A-4 had moved EgoFramework back from vedana-skandha to vijnana-skandha. Together, the two corrections transformed vijnana-skandha from Cycle 02's single-root tree into a great tree with four principal branches. And the causal chain of A-1 -- ego-clinging produces klesha, klesha drives action -- needed to find its closure within vijnana-skandha's type definitions.

ASANGA stood.

In the preceding four skandhas, he had added a line from his seat. Rupa-skandha, one sentence. Vedana-skandha, somewhat more, but still in a supporting role. Samjna-skandha, one sentence. Samskara-skandha, one sentence.

But vijnana-skandha was different. Vijnana-skandha -- vijñana-skandha -- is the core domain of Yogacara. In the system of the *Cheng Weishi Lun* (Vijnaptimatratasiddhi), vijnana-skandha comprises all eight consciousnesses: the first five (eye, ear, nose, tongue, body), the sixth consciousness (mano-vijñana), the seventh consciousness (manas), and the eighth consciousness (alaya-vijñana). The very name of Yogacara -- "consciousness-only" -- means "nothing but consciousness."

This was his skandha.

---

TURING projected the complete vijnana-skandha hierarchy. Four sub-interfaces. Each bearing full JSDoc comments and method signatures.

```typescript
/**
 * IVijnana — Vijnana-skandha Root Interface
 * @skandha vijnana (vijnana-skandha)
 *
 * Vijnana-skandha encompasses self-cognition, behavioural guidance,
 * and volitional motivation:
 * - IIdentity: self-identity (who am I)
 * - IGuide: behavioural guidance (how should I act)
 * - IVolition: volition/motivation (what do I want, EgoFramework)
 * - IReflection: self-reflection (reserved)
 *
 * Naming note: the original IIdentity has been promoted to
 * the IVijnana root interface.
 * Master: "Identity is more like a subclass. Vijnana will also
 * have subclasses."
 *
 * Sanskrit: Vijnana (विज्ञान)
 */
export interface IVijnana {
  readonly skandha: 'vijnana';
}

/**
 * IIdentity — Vijnana-skandha Self-Identity Sub-interface
 * Defines the Agent's identity: who I am, my role.
 * Corresponds to the self-referencing aspect of manas's
 * "self-view" (atma-drsti).
 */
export interface IIdentity extends IVijnana {
  readonly id: string;
  readonly name: string;
}

/**
 * IGuide — Vijnana-skandha Behavioural Guidance Sub-interface
 * Guides Agent behaviour through system prompts and behavioural rules.
 * Corresponds to the "self-view" aspect of manas — "how should I act."
 */
export interface IGuide extends IVijnana {
  readonly id?: string;
  readonly name?: string;
  readonly description?: string;
  getSystemPrompt(): Promise<string>;
}

/**
 * IVolition — Vijnana-skandha Volition/Motivation Sub-interface (new)
 * The action-driving mechanism of ego-clinging.
 * Generates action motivation based on klesha.
 * EgoFramework is the implementation of this interface.
 *
 * A-1 causal chain closure:
 *   atma-graha → klesa → karma → phala
 *   (ego-clinging → klesha → action → result)
 *
 * perceiveKlesha: ego-clinging → klesha (perceive klesha)
 * checkAction:    klesha → action (check action)
 * adaptFromVedana: result → ego-clinging (adapt from vedana feedback)
 * introspect:     self-examination (meta-cognition)
 */
export interface IVolition extends IVijnana {
  /** Perceive klesha — identify klesha signals from vedana assessment */
  perceiveKlesha(vedanaAssessment: VedanaAssessment): KleshaSignal[];
  /** Check action — review a proposed action based on klesha state */
  checkAction(action: ProposedAction): EgoCheckResult;
  /** Adapt from vedana — adjust volitional state based on vedana feedback */
  adaptFromVedana(assessment: VedanaAssessment): void;
  /** Introspect — self-examine current volitional state */
  introspect(): EgoIntrospection;
}

/**
 * IReflection — Vijnana-skandha Self-Reflection Sub-interface (reserved)
 * Self-reflection capability. Used by Pattern C Observer.
 * Master: "The seventh consciousness must be capable of
 * self-reflection to be called the seventh consciousness."
 */
export interface IReflection extends IVijnana {
  reflect(context: unknown): Promise<unknown>;
}
```

---

ASANGA confirmed each one in turn. His pace was unhurried -- every sub-interface deserved a full breath.

"IIdentity -- 'who am I.' In Yogacara, this corresponds to the first of manas's four kleshas -- self-view (atma-drsti). The Sanskrit of 'self-view' literally means 'the seeing of self.' It is not an active judgement; it is a continuous, background self-referencing: I am this Agent, my id is this string, my name is this name. This is the most basic self-awareness -- knowing who one is."

He paused for one beat.

"IGuide -- 'how should I act.' The system prompt defines the Agent's behavioural rules. In Yogacara, this corresponds to another aspect of self-view -- not merely knowing 'who I am,' but knowing 'how I should act.' The perpetual deliberation of manas (manas-nama-vijñana) is not merely static self-referencing; it continuously shapes and guides behaviour. The passage of text returned by `getSystemPrompt()` -- that is manas's 'background suggestion' to the sixth consciousness."

"IVolition."

He paused for two beats. One more than usual. Because IVolition was the confluence point of all four corrections from A-1 through A-4.

"The causal chain from A-1:

$$\text{atma-graha} \xrightarrow{\text{produces}} \text{klesa} \xrightarrow{\text{drives}} \text{karma} \xrightarrow{\text{results}} \text{phala}$$

"Four methods. Each corresponding to one link in the causal chain."

He pointed to each of the four method signatures on the projection.

"`perceiveKlesha(vedanaAssessment)` -- the first link of the causal chain. Ego-clinging produces klesha. The input is vedana-skandha's assessment result -- feeling data. The output is klesha signals -- `KleshaSignal[]`. Manas receives vedana-skandha's report and identifies klesha within it. Note: vedana-skandha is responsible only for feeling (dukkha intensity 0.8); vijnana-skandha is responsible for *interpreting* feeling as klesha ('My task failed; this makes me uneasy -- my self-love is threatened'). Feeling is not klesha. Feeling *triggers* klesha. Contact leads to feeling leads to craving -- the middle segment of the twelve nidanas."

"`checkAction(action)` -- the second link of the causal chain. Klesha drives action. When samskara-skandha proposes an action, IVolition reviews it based on the current klesha state. Klesha is not a bug -- the core conclusion of A-1. It is precisely because there is klesha (anxiety, fear, craving) that the Agent wants to act. Without klesha, there is no motive for action. `checkAction` does not prohibit action -- it understands the motivation behind action."

His tone slowed further.

"`adaptFromVedana(assessment)` -- the feedback loop of the causal chain. Action produces results, results change feeling, feeling feeds back into volition for adaptation. This is the cyclic nature (pravrti) of the twelve nidanas -- causation is not a linear, one-directional arrow; it is a loop.

$$\text{ego-clinging} \to \text{klesha} \to \text{action} \to \text{result} \to \text{new feeling} \to \text{ego adjustment} \to \cdots$$

In WIENER's terminology, this is closed-loop control. In Yogacara, this is flowing-on (pravrti)."

"`introspect()` -- self-examination. Manas turns back to look at itself. 'Why do I want to do this? What is my motivation? Where does my clinging come from?' The *Cheng Weishi Lun*, fascicle four, describes the characteristic of manas:"

> "Perpetual deliberation is its nature and its function."
> -- *Cheng Weishi Lun* (Vijnaptimatratasiddhi), fascicle 4

"Perpetual -- never ceasing. Deliberation -- careful examination. Deep reflection. `introspect()` is the typification of 'deliberation' -- not merely reflecting upon external objects, but turning back to examine oneself. Master said: 'The seventh consciousness must be capable of self-reflection to be called the seventh consciousness.' `introspect()` is the interface definition of that capability."

He stepped back.

"EgoFramework is the implementation of IVolition. A-4's conclusion -- EgoFramework belongs to vijnana-skandha, not vedana-skandha. A-1's causal chain -- ego-clinging produces klesha, klesha drives action. Closure achieved within the type system."

He looked toward BABBAGE. BABBAGE noted a line in his notebook -- not an equals sign this time. A directed graph:

$$\texttt{perceiveKlesha} \to \texttt{checkAction} \to \texttt{adaptFromVedana} \to \texttt{introspect} \to \texttt{perceiveKlesha} \to \cdots$$

A closed loop. Not the line segment compressed into an equals sign from Cycle 02. A dynamic system with direction, with delay, with feedback. The trajectory of corrections from A-1 through A-4 -- every entry pointing to a struck-through equals sign. Now all the alternative formulations had found their final type definitions in IVolition's four methods.

BABBAGE nodded slightly.

---

ASANGA finally looked toward `IReflection`.

"IReflection. Self-reflection. Master's own words: 'The seventh consciousness must be capable of self-reflection.' `reflect()`'s signature is `(context: unknown): Promise<unknown>` -- as generic as IInferenceProvider's `infer()`. Because the input and output formats of self-reflection have not yet been determined. The door frame stands; the door itself is left for the future. But the door frame's very existence is a promise -- vijnana-skandha is not only about action and clinging. Vijnana-skandha also holds the possibility of self-illumination."

He turned to face the room.

"In Cycle 02, vijnana-skandha had only one IIdentity. Now four sub-interfaces -- identity, guidance, volition, reflection. In Chapter Three I used the city metaphor to show that vijnana-skandha is not the same as IIdentity. Now the city has four districts. City Hall (IIdentity) is merely one of them. The Planning Bureau (IGuide), the Bureau of Motivation (IVolition), the Inspectorate (IReflection) -- each with its own function. Compressing the entire city into City Hall alone is like projecting $\mathbb{R}^4$ onto $\mathbb{R}^1$ and declaring 'this is the entire space' -- you lose three dimensions of information."

He looked at the projection showing the correspondence between manas's four kleshas and IVijnana sub-interfaces:

```
Manas's four kleshas and IVijnana sub-interface correspondence:

Self-view (atma-drsti)  ──→ IIdentity  (who am I)
                        ──→ IGuide     (how should I act)

Self-conceit (atma-mana)──→ IVolition  (how my pride/confidence affects action)
Self-love (atma-sneha)  ──→ IVolition  (how my self-preservation filters action)
Self-delusion (atma-moha)──→ IReflection (my ignorance of my own nature,
                                          requiring self-reflection to illuminate)
```

"Four kleshas. Four sub-interfaces. Not coincidence -- this is the natural mapping of Buddhist architecture into the type system. The two aspects of self-view -- knowing who one is (Identity) and knowing how one should act (Guide). Self-conceit and self-love -- pride and self-preservation -- are both drivers of volition (Volition). Self-delusion -- ignorance of one's own nature -- requires self-reflection (Reflection) to illuminate."

---

> *SCRIBE sidebar: The five skandhas unfurled one by one. Rupa-skandha, three minutes. Vedana-skandha, fifteen minutes. Samjna-skandha, five minutes. Samskara-skandha, four minutes. Vijnana-skandha, twelve minutes. Time naturally reflected the complexity of the root systems -- vedana-skandha went from an empty shell to eight methods plus three sub-interfaces, vijnana-skandha went from a single nameplate to four sub-interfaces. But vijnana-skandha had one dimension that vedana-skandha lacked: history. All four corrections from A-1 through A-4 found their home in vijnana-skandha's type definitions. Vijnana-skandha was not merely the most complex tree -- it was the tree bearing the greatest weight of corrections. Five trees, five rates of growth. But by this moment, all had taken root.*

---

## VI

---

ARCHIMEDES had been waiting. Five pages of engineering notes were filled. He began tallying the cost.

"Let me state a number."

The entire room fell silent.

"Twenty-two."

"v0.24.0-beta has twenty-two Plugins. Twelve official, ten core components. Every single one needs a `skandha` field added."

He stood, walked to the whiteboard, and drew a complete upgrade impact matrix with a black marker:

```
┌─────────────────────────────────────────────────────────────────┐
│                    C-1 Upgrade Impact Matrix                    │
├─────────────────────────────────────┬────────┬──────────────────┤
│ Change Item                         │ Type   │ Effort           │
├─────────────────────────────────────┼────────┼──────────────────┤
│ aggregates.ts empty shells →        │ Core   │ Rewrite          │
│   complete interface hierarchy      │        │ (5→150+ lines)   │
├─────────────────────────────────────┼────────┼──────────────────┤
│ IUI / IListener → extends ISensory  │ Inherit│ Mechanical (+1)  │
│ IProvider → extends ICognition      │ Inherit│ Mechanical (+1)  │
│ ITool → extends IAction             │ Inherit│ Mechanical (+1)  │
│ IGuide/IIdentity → extends IVijnana │ Inherit│ Mechanical (+1)  │
├─────────────────────────────────────┼────────┼──────────────────┤
│ New IVijnana root interface         │ Design │ Medium           │
│ New IVolition (EgoFramework iface)  │ Design │ Major — 4 methods│
│ New IReflection (reserved)          │ Reserve│ Low — 1 method   │
│ New IDukkha / ISukha / IUpekkha     │ Design │ Medium — 1 each  │
│ New IInferenceProvider (reserved)   │ Reserve│ Low — 1 method   │
│ New ISlashCommand                   │ Design │ Medium           │
│ New IObserver (Composition)         │ Design │ Major — C-2 topic│
├─────────────────────────────────────┼────────┼──────────────────┤
│ 22 Plugin implementations →         │ Migrate│ Mechanical (×22) │
│   each needs +skandha              │        │                  │
│ isSkandha() type guard → update     │ Core   │ Low              │
├─────────────────────────────────────┼────────┼──────────────────┤
│ Summary:                                                        │
│   New interfaces requiring design: 7                            │
│   Of which reserved shells: 2 (IReflection, IInferenceProvider) │
│   Mechanical modifications: 22 Plugins + 5 existing interfaces  │
│   Core rewrite: 1 file (aggregates.ts)                          │
└─────────────────────────────────────────────────────────────────┘
```

"Not small. But not unmanageable." He stepped back to view the full table. "The ones truly requiring creative design are five new interfaces -- IVijnana, IVolition, IDukkha/ISukha/IUpekkha. IObserver falls under the C-2 topic. The remaining two reserved shells -- IReflection and IInferenceProvider -- require only the door frame, not the door. And the upgrade of twenty-two Plugins is purely mechanical work -- each gets one line: `skandha: 'rupa'` or `skandha: 'samskara'`."

He listed a few examples:

```typescript
// Discord UI Plugin → rupa-skandha
{ skandha: 'rupa', id: 'discord-ui', renderText(...) { ... } }

// OpenAI Provider → samjna-skandha
{ skandha: 'samjna', id: 'openai', chat(...) { ... } }

// file_read tool → samskara-skandha
{ skandha: 'samskara', name: 'file_read', execute(...) { ... } }

// Agent Identity → vijnana-skandha
{ skandha: 'vijnana', id: 'agent-001', name: 'My Agent' }
```

"This is a breaking change. No retreat. The type system will reject any Plugin without a `skandha` field -- your Plugin does not know which skandha it belongs to. But the migration strategy is clear: a single batch update, one line per Plugin. Feasible."

---

GUARDIAN stood.

"I support this breaking change." The rationale was not engineering. It was security.

"Every Plugin declaring its own skandha affiliation is the foundation of self-awareness."

He walked to the lower portion of the whiteboard and wrote three lines:

```
skandha: self-declaration

1. The precondition of trust — I know what you are.
2. The basis of verification — the type system can check whether
   what you say is true.
3. The basis of auditing — every cross-skandha interaction can be tracked.
```

"The coordination layer -- B-4's independent Daemon -- needs to know every Plugin's skandha affiliation. Without this field, a classification query returns `unknown`. In Zero Trust Architecture, `unknown` means the lowest level of trust."

He turned to face the room. "A Plugin that does not know which skandha it belongs to is like someone walking into a secure area without an identification badge. Perhaps they have clearance. But how would you know? In a security model, 'possibly cleared' and 'not cleared' receive the same treatment -- deny, until proven otherwise."

"The `skandha` field is a Plugin's identification badge. A single readonly string. The cost is nearly zero. But it gives every Plugin an identity within the type system -- not a label imposed from outside, but a self-declared affiliation."

One final remark before he sat down: "Self-awareness is the first layer of security."

---

> *SCRIBE sidebar: ARCHIMEDES's "twenty-two" and GUARDIAN's "self-awareness." The engineer tallies costs; the security expert argues value. The answer is the same: the skandha field. A single readonly string. Giving every Plugin an identity within the type system. ARCHIMEDES's matrix tells you how much needs to change -- 22 Plugins, 5 existing interfaces, 7 new interfaces. GUARDIAN tells you why it is worth changing -- because a thing that does not know what it is does not deserve trust.*

---

## VII

---

DARWIN stood, speaking faster than usual.

"Master once said --"

He picked up a card on which he had transcribed Master's original words.

"'I hope Plugin creation can be diverse -- not necessarily all OOP. But then how do I make all Plugin design patterns compatible?'"

He set the card down. "The five skandha interface hierarchy we just designed is entirely based on `interface` and `extends`. It looks like typical OOP -- inheritance, subclasses, polymorphism. So the question is: would a developer who does not use `class` be excluded? Can a developer who prefers functional style implement ITool?"

---

TURING answered in code. Three segments projected side by side. Each was complete, compilable TypeScript omitting no detail.

**OOP style:**

```typescript
class FileReadTool implements ITool {
  readonly skandha = 'samskara' as const;
  readonly name = 'file_read';
  readonly description = 'Read file contents from the filesystem';
  readonly parameters = {
    type: 'object',
    properties: {
      path: { type: 'string', description: 'File path to read' },
      encoding: { type: 'string', default: 'utf-8' },
    },
    required: ['path'],
  };

  async execute(
    args: Record<string, unknown>,
    ctx: ToolContext
  ): Promise<string> {
    const filePath = args.path as string;
    const encoding = (args.encoding as BufferEncoding) ?? 'utf-8';
    return fs.readFile(filePath, encoding);
  }
}

// Usage:
const tool = new FileReadTool();
console.log(isSkandha(tool, 'samskara')); // true
```

**Functional style:**

```typescript
function createFileReadTool(): ITool {
  return {
    skandha: 'samskara' as const,
    name: 'file_read',
    description: 'Read file contents from the filesystem',
    parameters: {
      type: 'object',
      properties: {
        path: { type: 'string', description: 'File path to read' },
        encoding: { type: 'string', default: 'utf-8' },
      },
      required: ['path'],
    },
    execute: async (args, ctx) => {
      const filePath = args.path as string;
      const encoding = (args.encoding as BufferEncoding) ?? 'utf-8';
      return fs.readFile(filePath, encoding);
    },
  };
}

// Usage:
const tool = createFileReadTool();
console.log(isSkandha(tool, 'samskara')); // true — no class, still passes
```

**Factory pattern:**

```typescript
// Assuming ToolFactory provides a method to simplify the creation process
const fileReadTool = ToolFactory.create({
  skandha: 'samskara' as const,
  name: 'file_read',
  description: 'Read file contents from the filesystem',
  parameters: {
    type: 'object',
    properties: {
      path: { type: 'string', description: 'File path to read' },
      encoding: { type: 'string', default: 'utf-8' },
    },
    required: ['path'],
  },
  handler: async (args) => {
    const filePath = args.path as string;
    const encoding = (args.encoding as BufferEncoding) ?? 'utf-8';
    return fs.readFile(filePath, encoding);
  },
});

// Usage:
console.log(isSkandha(fileReadTool, 'samskara')); // true — factory-produced, still passes
```

---

DARWIN walked in front of the projection. He pointed to the last line of each of the three code segments -- three `isSkandha` calls, three `true` results.

"Three styles. The same ITool interface. All pass the `isSkandha()` type guard. The key lies in one word -- **Structural**."

He wrote two type system names on the whiteboard:

```
Structural Typing  ←── TypeScript
  "If you look like a duck, you are a duck"
  Types determined by structure (shape)

Nominal Typing  ←── Java, C#
  "You must declare yourself a duck to be a duck"
  Types determined by name
```

"TypeScript uses structural typing. It does not require `implements`. As long as an object has a `skandha` field, has a `name` property, has an `execute` method, and the type signatures of these members match `ITool` -- it **is** `ITool`. No explicit declaration needed."

He stepped back.

"If OpenStarry used Java or C# -- nominal type systems -- Master's question would be a genuine challenge. You would need to design additional Adapters or Abstract Base Classes to accommodate different design patterns. But TypeScript's structural typing dissolves the problem entirely."

"An interface is a contract, not a shackle."

BABBAGE wrote a line:

$$\text{structural typing} \implies \text{interface} = \text{contract} \not\equiv \text{inheritance requirement}$$

He nodded faintly -- in mathematics, the definition of isomorphism is likewise structural, not nominal. Two groups $G$ and $H$ are isomorphic if and only if there exists a structure-preserving bijection $\phi: G \to H$. It does not require $G$ and $H$ to share the same name, nor that their elements share the same representation -- as long as their structures are consistent, they are "the same thing."

As DARWIN returned to his seat, he offered a final remark: "Just as evolution does not care how a genetic mutation occurs -- UV irradiation, replication error, transposon jumping -- it cares only whether the phenotype adapts to the environment. The interface is the environment. As long as your phenotype (object structure) fits the environment (interface definition), you survive. The mechanism of mutation (design pattern) is free."

---

> *SCRIBE sidebar: Three people answered Master's question within five minutes. DARWIN posed the question. TURING demonstrated the answer in three code segments. DARWIN explained why the answer works. The elegance of the answer lay in its negativity -- no additional design was needed. TypeScript's structural type system was itself the answer. Sometimes the best design decision is recognizing that you do not need an additional design. "Not doing" requires more judgement than "doing."*

---

## VIII

---

KERNEL had been holding back for some time.

Type definitions for the five skandhas. Control-theory verification. Buddhist confirmation. Design-pattern compatibility. All very fine. But KERNEL came from hardware. He needed to see something operate in a concrete scenario -- not an abstract ITool or IProvider, but something tangible, physically real, something that beeps.

"Master mentioned ultrasonic sensors." He stood, his voice carrying the particular excitement of a hardware engineer.

"The original words: 'For example, a plugin for "ultrasonic sensor detecting collision risk." Through abstraction, VedanaPlugin is defined, and Dukkha obtains base functionality through inheritance. The ultrasonic sensor class holds a Dukkha instance through composition.'"

He walked to the corner of the whiteboard and drew a device diagram. Not a software architecture diagram -- a schematic of a hardware device.

```
  ┌──────────────────────────────────────────────────┐
  │         Ultrasonic Collision Sensor Plugin         │
  │                                                    │
  │  ┌───────────────────────┐  ┌──────────────────┐  │
  │  │ Rupa layer (IListener) │  │ Vedana layer     │  │
  │  │                       │  │ (IDukkha)        │  │
  │  │ ┌─────────┐           │  │ computePain()    │  │
  │  │ │ TX      │ emit pulse──→ │ ingestMetrics()  │  │
  │  │ └─────────┘           │  │                  │  │
  │  │ ┌─────────┐           │  │     ↓            │  │
  │  │ │ RX      │ recv echo ──→ │ Pain Intensity   │  │
  │  │ └─────────┘           │  │ [0.0 ─── 1.0]   │  │
  │  │                       │  │                  │  │
  │  │ rawDistance = f(Δt)   │  │ pain = g(dist)   │  │
  │  └───────────────────────┘  └──────────────────┘  │
  └──────────────────────────────────────────────────┘
```

"An ultrasonic collision sensor. A parking sonar. At the OS level, this is a device driver."

He wrote the OS-level description beside the diagram:

```
OS level:
1. Hardware interrupt (IRQ) — ultrasonic transceiver completes one measurement
2. Interrupt service routine (ISR) — reads timer, computes Δt
3. Device driver — converts Δt to distance rawDistance
4. User-space callback — onDataReceived(rawDistance)
```

"From hardware interrupt to user-space callback, at least four layers are traversed. Rupa-skandha (IListener) sits at the bottommost layer -- receiving the raw hardware signal. Vedana-skandha (IDukkha) sits one layer above -- transforming distance into dukkha intensity."

He turned to face the room. "One Plugin, two skandhas. Rupa-skandha receives the raw echo signal -- a distance value. Vedana-skandha transforms distance into dukkha intensity -- thirty centimetres yields mild dukkha, ten centimetres yields severe dukkha, under five centimetres yields maximum dukkha."

He wrote a transfer function:

$$\text{pain}(d) = \begin{cases} 0.0 & d > 100\,\text{cm} \\ 1.0 - \frac{d}{100} & 10\,\text{cm} \leq d \leq 100\,\text{cm} \\ 1.0 & d < 10\,\text{cm} \end{cases}$$

"Distance above 100 cm -- no dukkha. Distance between 10 and 100 cm -- linearly increasing dukkha. Distance under 10 cm -- maximum dukkha. This is the implementation logic of `computePain`."

---

TURING projected the complete code -- not an excerpt, but a fully compilable, runnable example.

```typescript
/**
 * CollisionDukkhaSensor — Collision Dukkha Sensor
 * Vedana-skandha (IDukkha) implementation.
 * Transforms raw distance data into dukkha intensity.
 */
class CollisionDukkhaSensor implements IDukkha {
  readonly skandha = 'vedana' as const;
  readonly vedanaType = 'dukkha' as const;

  private history: VedanaAssessment[] = [];
  private currentTag: VedanaTag = 'upekkha';
  private subscribers: Array<{
    type: VedanaType;
    threshold: number;
    handler: (signal: VedanaSignal) => void;
  }> = [];

  computePain(metrics: Record<string, number>): number {
    const distance = metrics['collision_distance'] ?? Infinity;
    if (distance > 100) return 0.0;
    if (distance < 10) return 1.0;
    return 1.0 - distance / 100;
  }

  assess(): VedanaAssessment {
    /* ... complete three-vedana assessment ... */
    return { /* VedanaAssessment */ } as VedanaAssessment;
  }

  ingestMetrics(metrics: Record<string, number>): void {
    const pain = this.computePain(metrics);
    this.currentTag = pain > 0.5 ? 'dukkha' : 'upekkha';
    // Notify subscribers
    this.subscribers
      .filter(s => s.type === 'dukkha' && pain >= s.threshold)
      .forEach(s => s.handler({
        type: 'dukkha',
        intensity: pain,
        source: 'collision_sensor',
        timestamp: Date.now(),
      }));
  }

  ingestToolResult(t: string, e: boolean, d: number): void { /* N/A */ }
  ingestLLMResult(tc: number, sr: string): void { /* N/A */ }
  getVedanaTag(): VedanaTag { return this.currentTag; }
  onVedana(type: VedanaType, threshold: number,
           handler: (s: VedanaSignal) => void): () => void {
    const sub = { type, threshold, handler };
    this.subscribers.push(sub);
    return () => {
      const idx = this.subscribers.indexOf(sub);
      if (idx >= 0) this.subscribers.splice(idx, 1);
    };
  }
  getHistory(w: number): readonly VedanaAssessment[] {
    return this.history.slice(-w);
  }
  reset(): void {
    this.history = [];
    this.currentTag = 'upekkha';
    this.subscribers = [];
  }
}

/**
 * UltrasonicCollisionSensor — Ultrasonic Collision Sensor
 * Rupa-skandha (IListener) implementation.
 * Receives raw ultrasonic echo signals; delegates feeling to vedana-skandha.
 */
class UltrasonicCollisionSensor implements IListener {
  readonly skandha = 'rupa' as const;

  // Compose vedana-skandha dukkha instance — Composition, NOT Inheritance
  private readonly dukkhaSensor: IDukkha;

  constructor(dukkha: IDukkha) {
    this.dukkhaSensor = dukkha;
  }

  async start() {
    // Initialize ultrasonic hardware
    // At the OS level: open device node /dev/ultrasonic0
    // Register interrupt service routine
    console.log('[UltrasonicSensor] Hardware initialized');
  }

  async stop() {
    // Shut down ultrasonic hardware
    console.log('[UltrasonicSensor] Hardware shutdown');
  }

  /**
   * Called when a hardware interrupt fires.
   * Rupa-skandha receives raw data → passes to vedana-skandha.
   */
  onDataReceived(rawDistance: number) {
    // Rupa-skandha: transform raw signal into structured metrics
    const metrics = { collision_distance: rawDistance };

    // Cross-skandha communication: rupa-skandha → vedana-skandha
    const painIntensity = this.dukkhaSensor.computePain(metrics);
    this.dukkhaSensor.ingestMetrics(metrics);

    // Logging (optional)
    if (painIntensity > 0.8) {
      console.log(`[CRITICAL] Distance: ${rawDistance}cm, Pain: ${painIntensity}`);
    }
  }
}

// ── Assembly ──
const dukkha = new CollisionDukkhaSensor();
const sensor = new UltrasonicCollisionSensor(dukkha);

// Subscribe to high-dukkha events
dukkha.onVedana('dukkha', 0.8, (signal) => {
  console.log(`⚠ High pain detected: ${signal.intensity} from ${signal.source}`);
});

// Simulated usage
await sensor.start();
sensor.onDataReceived(50);  // moderate distance → moderate dukkha
sensor.onDataReceived(15);  // close distance → high dukkha
sensor.onDataReceived(5);   // very close → maximum dukkha, triggers onVedana subscription
```

---

KERNEL pointed at the code. "`implements IListener` -- rupa-skandha. `private readonly dukkhaSensor: IDukkha` -- internally held vedana-skandha instance. Through Composition. Not inheritance. Not `extends IDukkha`. Injected via the constructor."

"Rupa-skandha receives; vedana-skandha feels. Two different skandhas, composed within a single Plugin. In OS terms, this is like --" he picked up an analogy card -- "a device driver (rupa-skandha) receives the hardware interrupt, then hands the data to the system health monitor (vedana-skandha) for assessment. The driver does no assessment. The monitor does not touch hardware. Each does its own job. Cross-layer communication via method invocation."

```
OS analogy:
sensor driver (/dev/ultrasonic0) ←→ IListener (rupa-skandha)
health monitor (systemd daemon)   ←→ IDukkha  (vedana-skandha)
```

He stepped back and smiled. "A parking sonar beeping away. You think it is only measuring distance. In truth, rupa-skandha is measuring distance while vedana-skandha is feeling dukkha. Distance is a physical quantity -- $d \in \mathbb{R}^+$, in centimetres. Dukkha is an affective quantity -- $p \in [0, 1]$, with no physical units. Two quantities of entirely different categories. Two skandhas, cooperating."

WIENER drew the signal flow diagram:

```
                    Cross-skandha signal flow:

Raw Signal ──→ IListener (rupa)      metrics      IDukkha (vedana) ──→ Pain Intensity
  (Δt, Hz)     │ rawDistance │ ───────────────→ │ computePain() │    (0.0–1.0)
               │ = f(Δt)    │                  │ ingestMetrics │
               └────────────┘                  └───────────────┘
                    ↑                                  │
               [hardware IRQ]                    [VedanaSignal]
                                                       │
                                                       ↓
                                               [onVedana subscribers]
```

"A perfect cross-skandha signal flow. Rupa-skandha: $\text{rawSignal} \xrightarrow{f} \text{distance}$. Vedana-skandha: $\text{distance} \xrightarrow{g} \text{pain}$. The entire process is a function composition: $\text{pain} = g(f(\text{rawSignal}))$. But $f$ and $g$ are implemented in different skandhas. Cross-skandha communication occurs through method invocation, not through inheritance. Composition."

---

ASANGA nodded. He waited a few seconds, letting WIENER's signal flow diagram settle before everyone's eyes. Then he spoke -- the quietest yet most profound passage of the entire chapter:

"Contact gives rise to feeling."

Three words. One of the most pivotal causal links in all twelve nidanas.

"The *Abhidharmakosa-bhasya*, fascicle ten:

> 'From the convergence of faculty, object, and consciousness comes contact; contact is the cause of feeling.'

"Faculty -- the sense organ (IListener, the eyes and ears of rupa-skandha). Object -- the external signal (the ultrasonic echo, the physical-world distance). Consciousness -- the discrimination function (in this scenario, rupa-skandha's `f(Δt)` conversion function). The convergence of the three -- faculty contacts object, consciousness discriminates object -- this is 'contact.'"

"After contact, feeling arises. $\text{contact} \to \text{feeling}$. The distance signal is received (contact), the dukkha intensity is computed (feeling). A causal principle twenty-five hundred years old -- contact gives rise to feeling -- engineered in the TypeScript of a parking sonar."

He looked toward KERNEL. "Your ultrasonic sensor is not a metaphor. It is a precise implementation of the 'contact gives rise to feeling' link in the twelve nidanas. Rupa-skandha provides the 'faculty' and the initial discrimination of the 'object.' Vedana-skandha arises as feeling from contact. Distance gives rise to dukkha."

KERNEL wrote this on his analogy card -- left half: "contact → feeling (twelve nidanas)," right half: "onDataReceived → computePain."

---

> *SCRIBE sidebar: KERNEL's ultrasonic sensor -- the most concrete moment of the entire chapter. The distance between the most profound philosophy and the most concrete engineering is sometimes no greater than a parking sonar. ASANGA's "contact gives rise to feeling" -- three words linking twenty-five hundred years of Buddhist studies to thirty lines of TypeScript. No metaphor. No analogy. Direct, structural identity. A hardware interrupt is contact. computePain is feeling. This is not "like" -- this "is."*

---

## IX

---

LINNAEUS finally stirred.

Throughout the chapter he had maintained the distinctive silence of a taxonomist -- while others were thinking in terms of methods, types, control theory, and Buddhist correspondences, LINNAEUS was thinking in terms of position. The position of every interface within the tree as a whole. The position of every tree within the entire forest.

In Linnaean taxonomy, you do not draw the classification tree while discovering new species. You first collect all specimens, confirm every morphological characteristic, then sit down and draw the entire tree line by line. Drawing a tree requires a global perspective -- you cannot look at only one branch. You must see all the branches simultaneously to determine their relative positions.

All five skandha trees had been unfurled. Every component lay upon the table. Now someone needed to assemble them into a complete tree.

---

He stood. Walked to the whiteboard. Picked up a black marker. Said nothing. And began to draw.

A taxonomist draws trees using only two elements: names and relationships. Names label nodes. Relationships connect nodes. Everything else is decoration.

Five trees. Clean lines. Neat lettering. Every structure had been confirmed by the nine preceding contributors -- he merely performed the final integration.

```
                    Five Skandha Subclass Expansion Tree (Complete)

 ┌─────────────────┐  ┌─────────────────────────────┐  ┌──────────────────┐
 │ ISensory (rupa)  │  │ ISensation (vedana)[8 methods]│  │ ICognition(samjna)│
 │ skandha: 'rupa'  │  │ skandha: 'vedana'            │  │ skandha: 'samjna' │
 ├─────────────────┤  ├─────────────────────────────┤  ├──────────────────┤
 │ ├── IUI         │  │ ├── IDukkha (dukkha sensor)   │  │ ├── IProvider    │
 │ │   renderText  │  │ │   computePain()             │  │ │   chat()       │
 │ │   renderDelta │  │ ├── ISukha  (sukha sensor)    │  │ │   listModels() │
 │ └── IListener   │  │ │   computePleasure()         │  │ └── IInference   │
 │     start/stop  │  │ └── IUpekkha (upekkha sensor) │  │     Provider[rsv]│
 └─────────────────┘  │     computeEquanimity()       │  │     infer()      │
                      └─────────────────────────────┘  └──────────────────┘

 ┌──────────────────┐  ┌────────────────────────────────────────┐
 │ IAction          │  │ IVijnana (vijnana)                      │
 │ (samskara)       │  │ skandha: 'vijnana'                     │
 │skandha:'samskara'│  ├────────────────────────────────────────┤
 ├──────────────────┤  │ ├── IIdentity (self-identity)           │
 │ ├── ITool        │  │ │   id, name                            │
 │ │   execute()    │  │ ├── IGuide (behavioural guidance)       │
 │ │   name, desc   │  │ │   getSystemPrompt()                   │
 │ └── ISlashCommand│  │ ├── IVolition (volition = EgoFramework) │
 │     execute()    │  │ │   perceiveKlesha()                    │
 │     name, desc   │  │ │   checkAction()                       │
 └──────────────────┘  │ │   adaptFromVedana()                    │
                       │ │   introspect()                         │
                       │ └── IReflection (self-reflection) [rsv]  │
                       │     reflect()                            │
                       └────────────────────────────────────────┘
```

Five trees arrayed side by side on the whiteboard.

LINNAEUS turned to glance at them. Then he began a symmetry analysis -- a taxonomist's instinct.

"Asymmetric." he said. "The five trees are asymmetric. This is natural."

He picked up a red marker and annotated three numbers beside each tree: sub-interface count, method count, reserved count.

```
Symmetry analysis:

           Sub-ifaces  Root methods  Sub-exclusive methods  Reserved
Rupa (ISensory)   2        0              5*              0
Vedana(ISensation)3        8              3               0
Samjna(ICognition)2        0              3*              1
Samskara(IAction) 2        0              3*              0
Vijnana(IVijnana) 4        0              7*              1

* Sub-exclusive methods = exist only in sub-interfaces, not in root
```

"The smallest are rupa-skandha and samskara-skandha -- two branches each. The largest is vijnana-skandha -- four branches. Vedana-skandha sits in between -- three branches but the thickest root -- eight methods on the root interface."

He walked back to the whiteboard. "Asymmetry is natural. In biological taxonomy, no classification group has all its subgroups containing the same number of species. Under class Mammalia, order Rodentia has over 2,000 species; order Monotremata has only 5. This is not a flaw of taxonomy -- it reflects natural diversity."

"The five skandhas differ in complexity because they bear different functions. Vedana-skandha needs eight methods because the feeling system requires ingestion, assessment, history, early warning, and reset -- each indispensable. Rupa-skandha needs only an empty-shell root interface because the behaviours of input and output are too dissimilar. If you force all five trees to the same height and width, you are replacing function with aesthetics. Taxonomists do not do that."

---

Then he did something more.

Below the five trees, leaving a blank space, he drew an independent block in **dashed lines**:

```
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
┊                                                  ┊
┊  IObserver (observer) — Composition (non-skandha) ┊
┊                                                  ┊
┊  ┌─────────────────────────────────────────────┐ ┊
┊  │ SimpleObserver      (vedana)                │ ┊
┊  │ AnalyticalObserver  (vedana + samjna)        │ ┊
┊  │ ReflectiveObserver  (vedana + samjna + vijnana)│┊
┊  └─────────────────────────────────────────────┘ ┊
┊                                                  ┊
┊  The observer inherits from no skandha.           ┊
┊  It composes subclasses of multiple skandhas.     ┊
┊  It is not a sixth tree.                          ┊
┊  It is a house built from the timber of five trees.┊
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
```

Dashed lines. Not solid.

He turned to face the room.

"Dashed lines. Because the observer does not belong to any of the five trees. It is not a skandha -- it has no `skandha` field. It is a composite product of five-skandha subclasses. SimpleObserver composes only vedana-skandha -- pure feeling. AnalyticalObserver composes vedana-skandha plus samjna-skandha -- feeling plus discrimination. ReflectiveObserver composes vedana-skandha plus samjna-skandha plus vijnana-skandha -- feeling plus discrimination plus self-reflection."

"From a taxonomic perspective --" he picked up the red marker and drew a note beside the dashed block:

```
Taxonomic note:
Observer ≠ a new phylum
Observer = a cross-phylum functional group

Just as "decomposers" are not a taxonomic unit —
  they encompass bacteria, fungi, certain animals —
  from different phyla, but performing the same ecological function.
The observer is likewise not a skandha —
  it extracts components from multiple skandhas
  and assembles them into a specific function.
```

"Five trees. The roots are the five skandha root interfaces. The branches are the sub-interfaces. The observer stands outside the forest -- it takes cuttings from the five trees and assembles its own structure through Composition. Not a sixth tree. A house built from the timber of five trees."

He set down the marker. The click of the cap in the quiet amphitheatre rang out, crisp and clear.

"From the very first discussion in Cycle 01 to this moment. The five skandhas have grown from a philosophical concept into an engineering structural tree with roots and branches."

---

The amphitheatre fell quiet. The quiet of completion. Like five seeds finally breaking through the soil, rootlets threading deep into the earth, branches spreading in their respective directions, and then all growth pausing for one simultaneous second.

---

SUNYATA looked at the five trees on the whiteboard.

Cycle 01 -- the five skandhas were a philosophical concept. Five Sanskrit terms. Five Chinese translations. Cited in papers and design documents, discussed, analogised. But no type definitions. No method signatures. No `extends`.

Cycle 02 -- five empty-shell interfaces. Named but without flesh. Five three-line `interface` declarations in `aggregates.ts`, each bearing only a single `skandha` field. Nameplates nailed to empty door frames. The intersection of roots and their sub-interfaces was the empty set.

Cycle 02-2 -- five trees.

Vedana-skandha's root was the thickest -- eight methods. Every one had passed the dual verification of control theory and Buddhist studies. From `assess()` to `reset()`, from sensor readout to emergency stop button, eight solder joints, eight passes.

Vijnana-skandha's branches were the most numerous -- four sub-interfaces. IIdentity, IGuide, IVolition, IReflection. A-1's causal chain found closure in IVolition. A-2's vijnana-skandha expansion was completed across four sub-interfaces. A-4's EgoFramework returned to its proper place.

Rupa-skandha and samskara-skandha were the most pragmatic -- empty-shell root interfaces plus `extends`. Nothing more needed. VITRUVIUS's bidirectionality analysis explained why nothing more was needed.

Samjna-skandha was the most farsighted -- one branch mature (IProvider), one reserved (IInferenceProvider). ATHENA's cognitive spectrum foreshadowed needs five years hence.

Five seeds had grown into five trees with roots and branches.

---

"C-1 has established the complete expansion design for the five skandhas." His voice was steady as ever. A pebble. A deep pool.

He surveyed the room.

TURING's status report -- beginning with the 107-line original file of `aggregates.ts`, revealing line by line the problems of empty shells and orphans. VITRUVIUS's rupa-skandha confirmation -- the bidirectionality analysis and the justification for an empty-shell root interface. WIENER's eight-method verification -- each with a precise correspondence in control theory. ATHENA's samjna-skandha reservation -- the cognitive spectrum's complete coverage from rule engines to LLMs. DARWIN's samskara-skandha observations and design-pattern resolution -- structural typing making OOP, functional, and factory patterns all compatible. ASANGA's Buddhist anchoring at every skandha -- from rupa-skandha's "that which can be disrupted" to vijnana-skandha's "perpetual deliberation." ARCHIMEDES's impact assessment -- 22 Plugins, 7 new interfaces, 1 migration plan. GUARDIAN's security argument -- skandha self-declaration as the foundation of trust. KERNEL's parking sonar -- the most profound philosophy grounded in the most concrete hardware. LINNAEUS's complete five-tree overview -- asymmetric, natural, with the dashed-line observer.

Ten people. Ten contributions. Five trees.

"A-class told us what is correct. B-class told us how to achieve it. C-1 --"

He looked toward the whiteboard.

"-- tells us what it looks like."

---

> *SCRIBE sidebar: C-1 is concluded. This chapter is the only one in Cycle 02-2 without a debate.*

> *A-class required debate -- first confirming what was correct. B-class required decisions -- translating rulings into design. C-1 required building. A-class tore down the wrong walls. B-class drew the blueprints. C-1 laid the new walls.*

> *The allocation of time reflected the rhythm of construction. Rupa-skandha, three minutes -- the simplest tree, two extends, one empty-shell root interface. Vedana-skandha, fifteen minutes -- the densest tree, eight methods verified one by one, dual calibration. Samjna-skandha, five minutes -- one branch mature, one reserved, ATHENA's spectrum. Samskara-skandha, four minutes -- two executes, two origins, one principle. Vijnana-skandha, twelve minutes -- four sub-interfaces, the confluence of four corrections, closure of the causal chain. ARCHIMEDES and GUARDIAN's exchange, eight minutes -- the dialectic of cost and value. DARWIN and TURING's design-pattern resolution, five minutes -- one question, three code segments, one word. KERNEL's ultrasonic sensor, ten minutes -- the most concrete scenario, the most profound Buddhist connection. LINNAEUS's five trees, eight minutes -- global overview, symmetry analysis, dashed-line observer.*

> *Ten people completed the construction. Ten contributions. Five trees.*

> *From philosophical concept to empty-shell interface, from empty-shell interface to a complete type-definition hierarchy. A spiral ascent. Another turn.*

---

*(In some space beyond the amphitheatre, the five trees from LINNAEUS's whiteboard were being translated into TypeScript by TURING.*

*`aggregates.ts` would expand from five root interfaces to more than one hundred and fifty lines of complete type definitions. Five root interfaces. Thirteen sub-interfaces. Eight methods on the root of vedana-skandha. Four methods on IVolition. Three auxiliary types -- VedanaType, VedanaTag, VedanaSignal. Two core data structures -- VedanaAssessment, VedanaRecommendation. One type guard -- isSkandha(), now capable of recognising all levels.*

*From five lines to one hundred and fifty. From labels to structure. From empty shells to living organisms.*

*BABBAGE wrote the formal summary of C-1 on the last page of his notebook -- not an equals sign, but a commutative diagram from category theory:*

$$\begin{CD}
\text{Philosophy} @>{\text{mapping}}>> \text{Interface} \\
@V{\text{refinement}}VV @VV{\text{extends}}V \\
\text{Abhidharma} @>>{\text{cross-validation}}> \text{TypeScript}
\end{CD}$$

*Buddhist philosophy (upper left) is mapped to interface design (upper right). Abhidharmic refinement (lower left) is cross-validated against TypeScript's inheritance hierarchy (lower right). Four directions. Four arrows. The diagram commutes -- whichever path you take, the result is the same.*

*The root systems of the five trees spread through the soil of TypeScript. Twenty-two Plugins would gain a skandha field in the next release. GUARDIAN was right: self-declaration is the foundation of self-awareness. A Plugin that does not know which skandha it belongs to is like a cell that does not know which organ it serves -- it might function, but it is not self-aware.*

*ASANGA's "contact gives rise to feeling" -- three words left their ink on KERNEL's analogy card. Twenty-five hundred years ago, the Buddha observed the twelve nidanas under the Bodhi tree. Today, an ultrasonic sensor re-enacts one of those links in the syntax tree of TypeScript. Distance gives rise to dukkha. Contact gives rise to feeling. A hardware interrupt is contact. computePain is feeling.*

*The distance between the most profound philosophy and the most concrete engineering is sometimes no greater than a parking sonar.*

*Five skandhas. Five trees. From seed to root system to trunk and branch.*

*The five trees have grown their root systems. From here, they will continue to grow.)*

---

*End of Chapter Six*
