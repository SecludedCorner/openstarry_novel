# Chapter Six: The Root Systems of Five Trees

---

SUNYATA stood at the center of the theater for a moment without saying anything.

A-class took three chapters to correct the philosophy. B-class took one chapter to implement the rulings. Those were dismantling and decision-making. What came next was different -- now it was time to build.

---

"C-1. Five-skandha subclass expansion design."

He picked up Master's letter: "'The five skandhas can serve as Root Classes. How to expand them can be arranged in more detail.'"

"The previous four chapters corrected the foundation. Now, C-1 is about growing those five trees from seeds into complete living things with roots, trunks, and branches -- on the corrected foundation."

---

> *SCRIBE's narration: SUNYATA used the imagery of "five trees." Trees are alive -- their roots extend, their branches fork. The expansion of the five skandhas is not static stacking; it is organic, growing simultaneously in multiple directions.*

---

TURING's screen projected to the center of the theater.

```typescript
export interface ISensory    { readonly skandha: 'rupa'; }
export interface ISensation   { readonly skandha: 'vedana'; }
export interface ICognition   { readonly skandha: 'samjna'; }
export interface IAction      { readonly skandha: 'samskara'; }
export interface IIdentity    { readonly skandha: 'vijnana'; }
```

Five lines. Each with only one field -- a label.

"Five root interfaces. No methods. No behavior definitions. No sub-interface inheritance. They're like five empty boxes with nothing but labels. Master wants us to open the boxes and put things inside."

---

He switched the projection to show the existing concrete interfaces -- IUI, IListener, IProvider, ITool, IGuide -- each with complete method definitions, but with no relationship to the five root interfaces. No extends. The nameplates and the doors were separate.

BABBAGE wrote a line in his notebook: `roots intersect children = orphans`. The intersection of roots and children was the empty set. Orphans.

---

SUNYATA counted on his fingers. Five design goals.

"One, add core methods to root interfaces. Two, upgrade existing interfaces to sub-interfaces. Three, add necessary new sub-interfaces. Four, observers use Composition and don't belong to any skandha. Five, isSkandha() available at all levels."

"Now, expand skandha by skandha."

---

## I

---

"Rupa-skandha. ISensory."

VITRUVIUS stood up. "Rupa-skandha is the simplest. Two sub-interfaces already exist. IUI handles output rendering -- the mouth, speaking outward. IListener handles sensory input -- the ear, listening inward. They just need to extends ISensory."

TURING projected the modified definitions:

```typescript
export interface ISensory {
  readonly skandha: 'rupa';
}

export interface IUI extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
  renderText?(text: string, sessionId?: string): void;
  renderDelta?(delta: string, sessionId?: string): void;
}

export interface IListener extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
}
```

"The ISensory root interface stays as an empty shell. IUI and IListener point in completely opposite directions -- output and input. Forcing a unification would create a false abstraction."

ASANGA added a line. "Rupa-skandha is contact -- contact with the external world. IUI and IListener represent the two directions of contact. Outward and inward."

---

> *SCRIBE's narration: Rupa-skandha, three minutes. One extends. The shortest root has entered the soil.*

---

## II

---

"Vedana-skandha. ISensation." SUNYATA's voice slowed slightly. Everyone knew vedana-skandha would be the tree with the most extensive root system.

TURING projected the complete interface.

```typescript
export interface ISensation {
  readonly skandha: 'vedana';
  assess(): VedanaAssessment;
  ingestMetrics(metrics: Record<string, number>): void;
  ingestToolResult(toolName: string, isError: boolean, durationMs: number): void;
  ingestLLMResult(tokenCount: number, stopReason: string): void;
  getVedanaTag(): VedanaTag;
  onVedana(type: VedanaType, threshold: number, handler: (signal: VedanaSignal) => void): () => void;
  getHistory(windowSize: number): readonly VedanaAssessment[];
  reset(): void;
}
```

WIENER stood up and went through the eight methods one by one.

"assess() -- sensor reading. Three ingest methods -- input channels from different interfaces. getVedanaTag() -- cached query. onVedana() -- event-driven threshold monitoring; notify only when dukkha exceeds 0.8. getHistory() -- sliding window history. reset() -- emergency stop."

"The vedana-skandha root interface is no longer an empty shell -- it is a complete sensor interface."

---

ASANGA stood up. "Vedana-skandha does one thing: feel. No judgment, no analysis. Touch fire -- dukkha. Taste something sweet -- sukha. Nothing happening -- upekkha. Eight methods, and every one of them stays within the scope of 'feeling.' Not a single method crosses the line into judgment."

He looked at WIENER. "Your control theory calls them sensor methods. My Buddhism calls them vedana-skandha methods. Same thing, two languages."

---

TURING projected three feeling sub-interfaces -- IDukkha, ISukha, IUpekkha -- each inheriting from ISensation, each with its own compute method.

WIENER added: "Three channels. Three PID loops. Cycle 02's three-channel architecture, now with type system guarantees." He made three heavy checkmarks on his grid paper. "In place."

---

> *SCRIBE's narration: Vedana-skandha, fifteen minutes -- five times as long as rupa-skandha. Eight methods required control theory validation and Buddhist confirmation. Dual calibration -- that is the discipline of Cycle 02-2.*

---

## III

---

"Samjna-skandha. ICognition."

ATHENA stood up.

```typescript
export interface ICognition {
  readonly skandha: 'samjna';
}

export interface IProvider extends ICognition {
  readonly id: string;
  chat(request: ChatRequest): AsyncIterable<StreamEvent>;
  listModels?(): Promise<ModelInfo[]>;
}

export interface IInferenceProvider extends ICognition {
  readonly id: string;
  infer(input: unknown): Promise<unknown>;
}
```

"IProvider -- LLM cognition, the current workhorse. IInferenceProvider -- non-LLM inference: rule engines, decision trees. Cognition is not equal to language model."

DARWIN leaned forward. "Evolutionarily, IInferenceProvider is more primitive cognition -- phototaxis. IProvider is more advanced -- linguistic reasoning. Two branches of the same tree."

---

## IV

---

"Samskara-skandha. IAction."

```typescript
export interface IAction {
  readonly skandha: 'samskara';
}

export interface ITool extends IAction {
  readonly name: string;
  readonly description: string;
  readonly parameters: unknown;
  execute(args: Record<string, unknown>, ctx: ToolContext): Promise<string>;
}

export interface ISlashCommand extends IAction {
  readonly name: string;
  readonly description: string;
  execute(args: string, ctx: IPluginContext, sessionId?: string): Promise<string | undefined>;
}
```

DARWIN stood up. "ITool -- actions autonomously invoked by the Agent. ISlashCommand -- actions triggered by external commands. Different sources, same nature. Both are the realization of will."

ASANGA, in one sentence: "Samskara-skandha encompasses all volitional formations. A tool's execute is a formation; a command's execute is also a formation."

---

## V

---

"Vijnana-skandha. IVijnana." SUNYATA spoke more slowly than for the previous four skandhas. This was the heaviest tree.

A-2 had demoted IIdentity from the entire vijnana-skandha to a sub-interface. A-4 had moved EgoFramework back to vijnana-skandha. Two corrections transformed vijnana-skandha from a single root to a four-branched tree.

ASANGA stood up. For the previous four skandhas, he had only supplemented a line or two from his seat. Vijnana-skandha was different -- this was his skandha.

---

TURING projected the complete vijnana-skandha system.

```typescript
export interface IVijnana {
  readonly skandha: 'vijnana';
}

export interface IIdentity extends IVijnana {
  readonly id: string;
  readonly name: string;
}

export interface IGuide extends IVijnana {
  readonly id?: string;
  getSystemPrompt(): Promise<string>;
}

export interface IVolition extends IVijnana {
  perceiveKlesha(vedanaAssessment: VedanaAssessment): KleshaSignal[];
  checkAction(action: ProposedAction): EgoCheckResult;
  adaptFromVedana(assessment: VedanaAssessment): void;
  introspect(): EgoIntrospection;
}

export interface IReflection extends IVijnana {
  reflect(context: unknown): Promise<unknown>;
}
```

ASANGA confirmed each one.

"IIdentity -- who am I. IGuide -- what should I do."

"IVolition." He paused for two beats. "A-1's causal chain lands here -- ego-clinging produces klesa (perceiveKlesha), klesa drives action checking (checkAction), vedana-skandha's feedback goes to volition for adaptation (adaptFromVedana), and volition can self-examine (introspect). The corrections from A-1 through A-4 achieve closure in the type system."

"IReflection. Self-reflection. Reserved. The door frame is there; the door panel is left for the future."

Finally he said: "In Cycle 02, vijnana-skandha had only one IIdentity. Now there are four sub-interfaces -- identity, guidance, volition, self-reflection. In Chapter Three I used the city metaphor to say vijnana-skandha is not equal to IIdentity. Now the city has four districts."

---

> *SCRIBE's narration: Five skandhas expanded one by one. Rupa-skandha three minutes, vedana-skandha fifteen, samjna-skandha five, samskara-skandha four, vijnana-skandha twelve. Time naturally reflected root system complexity. Five trees, five growth rates, but all have taken root.*

---

## VI

---

ARCHIMEDES had been waiting. Five pages of engineering notes were filled.

"Let me give you a number. Twenty-two."

"v0.24.0-beta has twenty-two Plugins. Every one of them needs a skandha field added."

He gave a few examples -- Discord UI gets `skandha: 'rupa'`, OpenAI Provider gets `skandha: 'samjna'`, file read tool gets `skandha: 'samskara'`.

"This is a breaking change. The type system will reject any Plugin without a skandha field."

---

GUARDIAN stood up. "I support this breaking change." The reason wasn't engineering -- it was security.

"Every Plugin declaring its own skandha membership is the foundation of self-awareness. The coordination layer needs to know each Plugin's membership. Without this field, classification queries return unknown. Unknown means lowest trust."

ARCHIMEDES added: "Most modifications are mechanical. The truly new interfaces that need designing are seven, two of which are reserved empty shells. Feasible."

---

> *SCRIBE's narration: ARCHIMEDES' "twenty-two" and GUARDIAN's "self-awareness." The engineer calculates cost; the security expert argues value. The answer is the same: the skandha field. A readonly string that gives every Plugin an identity in the type system.*

---

## VII

---

DARWIN stood up, speaking faster than usual.

"Master said -- 'Plugins don't necessarily all have to be OOP, but how do you make different design patterns compatible?'"

TURING answered with three side-by-side code snippets: OOP style with `class implements ITool`, functional style with `function createTool(): ITool`, factory pattern with `ToolFactory.create()`. Three styles, the same ITool interface.

DARWIN explained the keyword -- **Structural**.

"TypeScript uses structural typing. You don't need to write `implements`. As long as an object has a skandha field, has a name, has an execute method, it is an ITool. The interface is a contract, not a shackle."

BABBAGE wrote a line: `structural typing -> interface = contract, NOT inheritance requirement`.

"Master's question -- the answer was already in TypeScript's type system."

---

> *SCRIBE's narration: The elegance of the answer lies in its negativity -- no additional design is needed. Sometimes the best design decision is recognizing that you don't need additional design.*

---

## VIII

---

KERNEL had been holding back for a long time. "Master mentioned the ultrasonic sensor."

He drew a rectangle in a corner of the whiteboard. Upper half: **Rupa-skandha (IListener)**. Lower half: **Vedana-skandha (IDukkha)**.

"Ultrasonic collision sensor. Parking radar. One Plugin, two skandhas. Rupa-skandha receives raw echo signals -- distance values. Vedana-skandha converts distance into dukkha intensity -- thirty centimeters is mild dukkha, ten centimeters is intense dukkha."

TURING projected code -- UltrasonicCollisionSensor implements IListener, internally holding IDukkha. Rupa-skandha receives, vedana-skandha feels, composed within a single Plugin through Composition.

KERNEL smiled. "A parking radar going beep-beep-beep. You think it's only measuring distance. Actually rupa-skandha is measuring distance, vedana-skandha is feeling dukkha. Distance is a physical quantity; dukkha is a felt quantity. Two skandhas collaborating."

ASANGA nodded. "Contact gives rise to feeling -- the most essential link of the twelve nidanas. A causal principle from twenty-five hundred years ago, engineered into a parking radar's TypeScript."

---

> *SCRIBE's narration: The distance between the most profound philosophy and the most concrete engineering is sometimes only as close as a parking radar.*

---

## IX

---

LINNAEUS finally moved. The taxonomist had remained silent through the entire chapter -- while others thought about methods and types, he thought about position. The position of every interface on the entire tree.

All five skandha trees had been expanded. Now someone needed to assemble them into a complete tree.

---

He walked to the whiteboard, picked up the marker, and began drawing directly.

```
ISensory (rupa-skandha)            ISensation (vedana-skandha) [8 methods]
+-- IUI (output rendering)         +-- IDukkha (dukkha sensor)
+-- IListener (sensory input)      +-- ISukha (sukha sensor)
                                   +-- IUpekkha (upekkha sensor)

ICognition (samjna-skandha)        IAction (samskara-skandha)
+-- IProvider (LLM cognition)      +-- ITool (tools)
+-- IInferenceProvider [reserved]  +-- ISlashCommand (commands)

IVijnana (vijnana-skandha)
+-- IIdentity (self-identification)
+-- IGuide (behavioral guidance)
+-- IVolition (will/motivation = EgoFramework)
+-- IReflection (self-reflection) [reserved]
```

Five trees side by side on the whiteboard. Then below them, he drew an independent block with dashed lines:

```
IObserver (observer) -- Composition      [dashed lines]
+-- SimpleObserver (vedana)
+-- AnalyticalObserver (vedana + cognition)
+-- ReflectiveObserver (vedana + cognition + vijnana)
```

Dashed lines -- because the observer doesn't belong to any of the five trees. It takes branches from the five trees and assembles them into its own structure through Composition. Not a sixth tree, but a house built from the wood of five trees.

He set down the marker. "From Cycle 01 to now. The five skandhas have gone from philosophical concepts to engineering structure trees with roots and branches."

---

The theater fell quiet. Like five seeds breaking soil, roots extending into the earth, branches reaching out in their own directions.

SUNYATA looked at the five trees on the whiteboard.

Cycle 01 -- the five skandhas were philosophical concepts. Cycle 02 -- five empty-shell interfaces. Cycle 02-2 -- five trees. Vedana-skandha had the thickest roots, with eight methods. Vijnana-skandha had the most branches, with four sub-interfaces. Rupa-skandha and samskara-skandha were the most pragmatic -- just needing extends. Samjna-skandha was the most forward-looking -- one mature branch, one reserved.

---

"C-1 established the complete expansion design for the five skandhas."

"A-class told us what is right. B-class told us how to make it happen. C-1 --"

He looked at the whiteboard.

"Tells us what it looks like."

---

> *SCRIBE's narration: C-1 is finished. There was no debate in this chapter. A-class needed debate -- confirming what is right. B-class needed decisions -- translating rulings into designs. C-1 needed building. Ten people completed the construction. Five trees. From philosophical concepts to empty-shell interfaces, from empty-shell interfaces to a complete type definition system. Spiral ascent, one more turn.*

---

*(Outside the theater, LINNAEUS's five trees on the whiteboard are being translated by TURING into TypeScript.*

*`aggregates.ts` will expand from five lines to over one hundred fifty. Five root interfaces, thirteen sub-interfaces, eight methods on vedana-skandha's root.*

*From five lines to one hundred fifty. From labels to structure. From empty shells to living organisms.*

*The root systems of the five trees spread through TypeScript's soil. Twenty-two Plugins will gain a skandha field -- self-declaration is the foundation of self-awareness.*

*The five trees have grown their root systems. Next, they will continue to grow.)*

---

*End of Chapter Six*
