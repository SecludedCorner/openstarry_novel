# Chapter Six: The Root Systems of Five Trees

---

SUNYATA stood at the centre of the amphitheatre for a moment, saying nothing.

A-class had taken three chapters to correct the philosophy. B-class had taken one chapter to enact the rulings. Those were acts of dismantling and deciding. What needed to be done now was different.

Now it was time to build.

---

"C-1. The five skandha subclass expansion design."

He picked up Master's letter and found the passage.

"'The five skandhas can serve as root classes in object-oriented design. How they should be extended deserves a more detailed arrangement.'"

He set the letter down. "The first four chapters corrected the foundations. Now, C-1 will take the five trees from seed to complete living organisms -- root, trunk, and branch -- upon those corrected foundations."

He looked toward TURING. "Let us first see what the seeds look like now."

---

> *SCRIBE sidebar: SUNYATA used the image of "five trees." Walls and pillars are dead things. Trees are alive. Trees have roots, and roots extend. Trees have branches, and branches fork. The expansion of the five skandhas is not static accumulation -- it is organic, simultaneous growth in multiple directions.*

---

TURING's screen projected into the centre of the amphitheatre. Cold light. White background. Black text.

```typescript
export interface ISensory    { readonly skandha: 'rupa'; }
export interface ISensation   { readonly skandha: 'vedana'; }
export interface ICognition   { readonly skandha: 'samjna'; }
export interface IAction      { readonly skandha: 'samskara'; }
export interface IIdentity    { readonly skandha: 'vijnana'; }
```

Five lines. Each containing only a single field. `readonly skandha`. A label.

"Five root interfaces. No methods. No behaviour definitions. No sub-interface inheritance."

He let the projection linger for a few seconds. Five lines of text like five nameplates nailed to five doors that had not yet been built.

"They are like five empty boxes with nothing but labels. Master wants us to open the boxes and put something inside."

---

He switched the projection.

```typescript
export interface IUI { ... }       // rupa-skandha? Does not inherit ISensory
export interface IListener { ... } // rupa-skandha? Does not inherit ISensory
export interface IProvider { ... } // samjna-skandha? Does not inherit ICognition
export interface ITool { ... }     // samskara-skandha? Does not inherit IAction
export interface IGuide { ... }    // vijnana-skandha? Does not inherit IIdentity
```

"The existing concrete interfaces. Each has a complete set of method definitions. But between them and the five root interfaces there is no relationship whatsoever. No extends. No inheritance. The nameplates and the doors are separate. You know that IUI should belong to rupa-skandha, but the type system does not."

BABBAGE wrote a line in his notebook: `roots ∅ children = orphans`. The intersection of roots and children was the empty set. Orphans.

---

SUNYATA counted on his fingers. Five design objectives.

"One. Each skandha's root interface gains core methods. Two. Existing interfaces are upgraded to sub-interfaces -- IUI extends ISensory, and so forth. Three. New sub-interfaces are added where necessary -- the IVijnana hierarchy, the three vedana interfaces. Four. The observer uses Composition and does not belong to any skandha. Five. isSkandha() is available at every level."

Five fingers folded back. "Now, skandha by skandha."

---

## I

---

"Rupa-skandha. ISensory."

VITRUVIUS rose to his feet. Rupa-skandha -- form and materiality -- was the most intuitive domain for a full-stack architecture analyst.

"Rupa-skandha is the simplest of the five trees. Its two sub-interfaces already exist. IUI handles output rendering -- the mouth, what is spoken outward. IListener handles sensory input -- the ears, what is taken in. They need only extends ISensory."

TURING projected the revised definitions.

```typescript
export interface ISensory {
  readonly skandha: 'rupa';
}

export interface IUI extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
  renderText?(text: string, sessionId?: string, replyTo?: string): void;
  renderDelta?(delta: string, sessionId?: string, replyTo?: string): void;
}

export interface IListener extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
}
```

"The ISensory root interface remains an empty shell," TURING said. "The behavioural directions of IUI and IListener are diametrically opposed -- output and input. Forcing them into a single shared method would manufacture a false abstraction. The root's purpose is to let isSkandha('rupa') pass."

ASANGA added a line from his seat. "Rupa-skandha is contact. Contact with the external world. IUI and IListener represent the two directions of contact. Outward and inward."

---

> *SCRIBE sidebar: Rupa-skandha, three minutes. One extends. The first root of the first tree -- the shortest one -- sank into the soil.*

---

## II

---

"Vedana-skandha. ISensation." SUNYATA's voice slowed perceptibly. Everyone knew that vedana-skandha would be the tree with the most expansive root system of all five.

WIENER was already flipping through his graph paper. "ISensation undergoes the greatest transformation," SUNYATA said. "From an empty shell to eight core methods. WIENER, confirm each one."

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

WIENER stood and pointed at each method in turn -- like an engineer inspecting every station on an assembly line.

"assess() -- the sensor readout function. ingestMetrics/ingestToolResult/ingestLLMResult -- three input channels, different ports of a composite sensor. getVedanaTag() -- O(1) cached lookup, the number on the dashboard."

He paused. The corner of his mouth lifted slightly.

"onVedana() -- a generalization of the watchdog timer. No continuous polling; it notifies subscribers only when dukkha exceeds 0.8. Event-driven threshold monitoring. getHistory() -- sliding window history, the foundation for a PID controller's integral term. reset() -- the emergency stop button."

Eight methods, eight control-theory correspondences. "The vedana-skandha root interface is no longer an empty shell -- it is a complete sensor interface."

---

ASANGA stood. Vedana-skandha required more space than rupa-skandha.

"Vedana-skandha does one thing. It feels. It does not judge. It does not analyse. Touch fire -- dukkha. Taste sweetness -- sukha. Nothing happens -- upekkha."

He looked at the eight methods on the projection. "Eight methods. Every one of them falls within the domain of 'feeling.' assess is the output of feeling. The ingest family is the input of feeling. onVedana is the early warning of feeling. getHistory is the memory of feeling -- a purely affective record. Not a single method oversteps into judgement."

He looked toward WIENER. "Your control theory says they are methods of a sensor. My Buddhist studies say they are methods of vedana-skandha."

WIENER noted a line: `ISensation: 8 methods. Sensor ≡ Vedana. Cross-validated.`

---

TURING projected the three vedana sub-interfaces.

```typescript
export interface IDukkha extends ISensation {
  readonly vedanaType: 'dukkha';
  computePain(metrics: Record<string, number>): number;
}

export interface ISukha extends ISensation {
  readonly vedanaType: 'sukha';
  computePleasure(metrics: Record<string, number>): number;
}

export interface IUpekkha extends ISensation {
  readonly vedanaType: 'upekkha';
  computeEquanimity(metrics: Record<string, number>): number;
}
```

WIENER added from his seat: "Three channels. Three PID loops. The three-channel architecture from Cycle 02 now has the backing of the type system." On the graph paper he ticked three checkmarks -- heavier than the seven from Chapter Five, pressing hard enough to leave three small indentations in the page. "In place."

---

> *SCRIBE sidebar: Vedana-skandha, fifteen minutes. Five times that of rupa-skandha. Eight methods, each requiring WIENER's control-theory verification and ASANGA's Buddhist confirmation. Dual calibration. This is the discipline of Cycle 02-2.*

---

## III

---

"Samjna-skandha. ICognition."

ATHENA rose. Samjna-skandha -- cognition and discrimination -- was her most essential area of expertise.

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

"IProvider -- LLM cognition, the current workhorse. IInferenceProvider -- non-LLM inference: rule engines, decision trees. Reserved, but important. Cognition is not synonymous with language models."

ASANGA, in one sentence: "Samjna-skandha is discrimination. Discrimination takes more than one form."

DARWIN leaned forward. "Evolutionarily, IInferenceProvider is the more primitive cognition -- phototaxis, rule-based. IProvider is the more advanced -- linguistic reasoning. Two branches of the same tree, growing at different heights."

---

## IV

---

"Samskara-skandha. IAction."

DARWIN fully stood. Samskara-skandha was the core lens through which he observed software behavioural patterns.

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

"ITool -- actions invoked autonomously by the Agent. ISlashCommand -- actions triggered by external commands. Different origins, same nature. Both are samskara. Both are the realization of volition."

ASANGA's single remark: "Samskara-skandha encompasses all formations. Cetana -- intention -- is the core of samskara. A tool's execute is a formation. A command's execute is also a formation."

---

## V

---

"Vijnana-skandha. IVijnana." SUNYATA's pace slowed below that of the previous four skandhas. This was the tree of greatest weight.

A-2 had demoted IIdentity from the entirety of vijnana-skandha to a sub-interface. A-4 had moved EgoFramework back from vedana-skandha to vijnana-skandha. Together, the two corrections transformed vijnana-skandha from Cycle 02's single-root tree into a great tree with four principal branches.

ASANGA stood. In the preceding four skandhas, he had added a line from his seat. But vijnana-skandha was different. This was his skandha.

---

TURING projected the complete vijnana-skandha hierarchy.

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
  readonly name?: string;
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

ASANGA confirmed each one in turn. His pace was unhurried -- every sub-interface deserved a full breath.

"IIdentity -- who am I. IGuide -- how should I act; the 'self-view' aspect of manas."

"IVolition." He paused for two beats. "The causal chain from A-1 finds its grounding here -- ego-clinging produces klesha (perceiveKlesha), klesha drives action checking (checkAction), vedana-skandha feeds back to volition for adaptation (adaptFromVedana), and volition can examine itself (introspect). EgoFramework is the implementation of IVolition. This is A-4's conclusion. A-1's causal chain. Closure achieved within the type system."

BABBAGE nodded slightly. In his notebook, the trajectory of corrections from A-1 through A-4 -- every entry pointing to a struck-through equals sign. Now all the alternative formulations had found their final type definitions in IVolition's four methods.

"IReflection. Self-reflection. Master's own words: the seventh consciousness must be capable of self-reflection. Reserved. The door frame stands; the door itself is left for the future."

---

ASANGA spoke a final word. "In Cycle 02, vijnana-skandha had only one IIdentity. Now four sub-interfaces -- identity, guidance, volition, reflection. In Chapter Three I used the city metaphor to show that vijnana-skandha is not the same as IIdentity. Now the city has four districts. City Hall is merely one of them."

---

> *SCRIBE sidebar: The five skandhas unfurled one by one. Rupa-skandha, three minutes. Vedana-skandha, fifteen minutes. Samjna-skandha, five minutes. Samskara-skandha, four minutes. Vijnana-skandha, twelve minutes. Time naturally reflected the complexity of the root systems. Vedana-skandha went from an empty shell to eight methods plus three sub-interfaces. Vijnana-skandha went from a single nameplate to four sub-interfaces. Five trees, five rates of growth. But by this moment, all had taken root.*

---

## VI

---

ARCHIMEDES had been waiting. Five pages of engineering notes were filled. He began tallying the cost.

"Let me state a number."

The entire room fell silent.

"Twenty-two."

"v0.24.0-beta has twenty-two Plugins. Twelve official, ten core components. Every single one needs a skandha field added."

He listed a few examples -- Discord UI gets `skandha: 'rupa'`, OpenAI Provider gets `skandha: 'samjna'`, the file read tool gets `skandha: 'samskara'`.

"This is a breaking change. Every existing Plugin must be modified. The type system will reject any Plugin without a skandha field -- your Plugin does not know which skandha it belongs to."

---

GUARDIAN stood.

"I support this breaking change." The rationale was not engineering. It was security.

"Every Plugin declaring its own skandha affiliation is the foundation of self-awareness."

On the lower portion of the whiteboard he wrote a single line: **skandha: self-declaration**

"The precondition of trust is: I know what you are. The coordination layer -- B-4's independent Daemon -- needs to know every Plugin's skandha affiliation. Without this field, a classification query returns unknown. Unknown means the lowest level of trust."

ARCHIMEDES appended the impact matrix:

```
Upgrade impact:
├── aggregates.ts        → 5 empty shells → complete interface hierarchy
├── IUI/IListener        → +extends ISensory
├── IProvider            → +extends ICognition
├── ITool               → +extends IAction
├── IGuide/IIdentity     → +extends IVijnana
├── New IVijnana/IVolition/IReflection  → vijnana-skandha hierarchy
├── New IDukkha/ISukha/IUpekkha        → vedana three-vedana
├── New IInferenceProvider/ISlashCommand → reserved + commands
├── 22 Plugin implementations → each needs +skandha field
└── isSkandha() type guard → update
```

"Not small. But not unmanageable. Most modifications are mechanical. The genuinely new interfaces requiring design are seven, two of which are reserved empty shells. Feasible."

---

> *SCRIBE sidebar: ARCHIMEDES's "twenty-two" and GUARDIAN's "self-awareness." The engineer tallies costs; the security expert argues value. The answer is the same: the skandha field. A single readonly string. It gives every Plugin an identity within the type system.*

---

## VII

---

DARWIN stood, speaking faster than usual.

"Master once said: 'I hope Plugin creation can be diverse -- not necessarily all OOP. But then how do I make all Plugin design patterns compatible?'"

"The five skandha interface hierarchy we just designed is entirely based on interface and extends. Would a developer who does not use class be excluded?"

---

TURING answered in code. Three segments projected side by side.

OOP style:

```typescript
class FileReadTool implements ITool {
  readonly skandha = 'samskara' as const;
  readonly name = 'file_read';
  readonly description = 'Read a file';
  readonly parameters = { /* JSON Schema */ };
  async execute(args: Record<string, unknown>, ctx: ToolContext): Promise<string> {
    return fs.readFile(args.path as string, 'utf-8');
  }
}
```

Functional style:

```typescript
function createFileReadTool(): ITool {
  return {
    skandha: 'samskara',
    name: 'file_read',
    description: 'Read a file',
    parameters: { /* JSON Schema */ },
    execute: async (args, ctx) => fs.readFile(args.path as string, 'utf-8'),
  };
}
```

Factory pattern:

```typescript
const fileReadTool = ToolFactory.create({
  skandha: 'samskara',
  name: 'file_read',
  description: 'Read a file',
  parameters: { /* JSON Schema */ },
  handler: async (args) => fs.readFile(args.path as string, 'utf-8'),
});
```

---

DARWIN walked in front of the projection. "Three styles. The same ITool interface. The key lies in one word -- **Structural**."

"TypeScript uses structural typing. It does not require `implements`. As long as an object has a skandha field, has a name, has an execute method, it is an ITool."

He stepped back. "An interface is a contract, not a shackle."

BABBAGE wrote a line: `structural typing → interface = contract, NOT inheritance requirement`. He nodded faintly -- in mathematics, the definition of isomorphism is likewise structural, not nominal.

"Master's question -- the answer was already in TypeScript's type system." As DARWIN returned to his seat, he offered a final remark: "Just as evolution does not care how a genetic mutation occurs. It cares only whether the phenotype adapts to the environment. The interface is the environment."

---

> *SCRIBE sidebar: Three people answered Master's question within five minutes. The elegance of the answer lay in its negativity -- no additional design was needed. TypeScript's structural type system was itself the answer. Sometimes the best design decision is recognizing that you do not need an additional design.*

---

## VIII

---

KERNEL had been holding back for some time.

"Master mentioned ultrasonic sensors." He stood, his voice carrying the particular excitement of a hardware engineer.

In the corner of the whiteboard he drew a rectangle bisected by a dividing line. Upper half: **rupa-skandha (IListener)**. Lower half: **vedana-skandha (IDukkha)**.

"An ultrasonic collision sensor. A parking sonar. One Plugin, two skandhas. Rupa-skandha receives the raw echo signal -- a distance value. Vedana-skandha transforms distance into dukkha intensity -- thirty centimetres yields mild dukkha, ten centimetres yields severe dukkha."

TURING projected the code.

```typescript
class UltrasonicCollisionSensor implements IListener {
  readonly skandha = 'rupa' as const;
  private readonly dukkhaSensor: IDukkha;

  constructor(dukkha: IDukkha) {
    this.dukkhaSensor = dukkha;
  }

  async start() { /* initialize ultrasonic hardware */ }

  onDataReceived(rawDistance: number) {
    const metrics = { collision_distance: rawDistance };
    const painIntensity = this.dukkhaSensor.computePain(metrics);
    this.dukkhaSensor.ingestMetrics(metrics);
  }
}
```

KERNEL pointed at the code. "implements IListener -- rupa-skandha. Internally holds an IDukkha -- vedana-skandha. Through Composition. Rupa-skandha receives; vedana-skandha feels. Two different skandhas, composed within a single Plugin."

He stepped back and smiled. "A parking sonar beeping away. You think it is only measuring distance. In truth, rupa-skandha is measuring distance while vedana-skandha is feeling dukkha. Distance is a physical quantity. Dukkha is an affective quantity. Two skandhas, cooperating."

WIENER drew the signal flow diagram:

```
Raw Signal → IListener(rupa) → Metric → IDukkha(vedana) → Pain Intensity
```

"A perfect cross-skandha signal flow. Every step remains within its own skandha. Cross-skandha communication occurs through method invocation, not through inheritance. Composition."

ASANGA nodded. "Contact gives rise to feeling. The most pivotal causal link in the twelve nidanas. Rupa-skandha receives the signal; vedana-skandha produces dukkha. Distance gives rise to dukkha. A causal principle twenty-five hundred years old, engineered in the TypeScript of a parking sonar."

---

> *SCRIBE sidebar: KERNEL's ultrasonic sensor -- the most concrete moment of the entire chapter. The distance between the most profound philosophy and the most concrete engineering is sometimes no greater than a parking sonar.*

---

## IX

---

LINNAEUS finally stirred.

Throughout the chapter he had maintained the distinctive silence of a taxonomist -- while others were thinking in terms of methods, types, and control theory, LINNAEUS was thinking in terms of position. The position of every interface within the tree as a whole.

All five skandha trees had been unfurled. Every component lay upon the table. Now someone needed to assemble them into a complete tree.

---

He stood. Walked to the whiteboard. Picked up a black marker. Said nothing. And began to draw.

Five trees. Clean lines. Neat lettering. A taxonomist draws trees using only names and relationships -- because the meaning of a tree is defined entirely by names and relationships.

```
ISensory (rupa)                ISensation (vedana) [8 methods]
├── IUI (output rendering)     ├── IDukkha (dukkha sensor)
└── IListener (sensory input)  ├── ISukha (sukha sensor)
                               └── IUpekkha (upekkha sensor)

ICognition (samjna)            IAction (samskara)
├── IProvider (LLM cognition)  ├── ITool (tools)
└── IInferenceProvider [reserved]  └── ISlashCommand (commands)

IVijnana (vijnana)
├── IIdentity (self-identity)
├── IGuide (behavioural guidance)
├── IVolition (volition/motivation = EgoFramework)
└── IReflection (self-reflection) [reserved]
```

Five trees arrayed side by side on the whiteboard. The smallest were rupa-skandha and samskara-skandha -- two branches each. The largest was vijnana-skandha -- four branches. Vedana-skandha sat in between -- three branches, but the thickest root.

Then he did something more. Below the five trees, in dashed lines, he drew an independent block:

```
IObserver (observer) — Composition      [dashed]
├── SimpleObserver (vedana)
├── AnalyticalObserver (vedana + cognition)
└── ReflectiveObserver (vedana + cognition + vijnana)
```

Dashed lines. Not solid. Because the observer does not belong to any of the five trees. It is not a tree -- it is a structure assembled from the branches and trunks of other trees.

He turned to face the room.

"Five trees. The roots are the five skandha root interfaces. The branches are the sub-interfaces. The observer stands outside the forest -- it takes cuttings from the five trees and assembles its own structure through Composition. Not a sixth tree. A house built from the timber of five trees."

He set down the marker. The click of the cap in the quiet amphitheatre rang out, crisp and clear.

"From the very first discussion in Cycle 01 to this moment. The five skandhas have grown from a philosophical concept into an engineering structural tree with roots and branches."

---

The amphitheatre fell quiet. The quiet of completion. Like five seeds finally breaking through the soil, rootlets threading deep into the earth, branches spreading in their respective directions, and then all growth pausing for one simultaneous second.

SUNYATA looked at the five trees on the whiteboard.

Cycle 01 -- the five skandhas were a philosophical concept. Cycle 02 -- five empty-shell interfaces, named but without flesh. Cycle 02-2 -- five trees. Vedana-skandha's root was the thickest, with eight methods. Vijnana-skandha's branches were the most numerous, with four sub-interfaces. Rupa-skandha and samskara-skandha were the most pragmatic -- requiring only extends. Samjna-skandha was the most foresighted -- one branch mature, one reserved.

Five seeds had grown into five trees with roots and branches.

---

"C-1 has established the complete expansion design for the five skandhas." His voice was steady as ever. A pebble. A deep pool.

He surveyed the room. TURING's status report. VITRUVIUS's rupa-skandha confirmation. WIENER's eight-method verification. ATHENA's samjna-skandha reservation. DARWIN's samskara-skandha observations and design-pattern resolution. ASANGA's Buddhist anchoring at every skandha. ARCHIMEDES's impact assessment. GUARDIAN's security argument. KERNEL's parking sonar. LINNAEUS's complete tree.

"A-class told us what is correct. B-class told us how to achieve it. C-1 --"

He looked toward the whiteboard.

"-- tells us what it looks like."

---

> *SCRIBE sidebar: C-1 is concluded. This chapter is the only one in Cycle 02-2 without a debate. A-class required debate -- first confirming what was correct. B-class required decisions -- translating rulings into design. C-1 required building. A-class tore down the wrong walls. B-class drew the blueprints. C-1 laid the new walls.*

> *Ten people completed the construction. Ten contributions. Five trees.*

> *From philosophical concept to empty-shell interface, from empty-shell interface to a complete type-definition hierarchy. A spiral ascent. Another turn.*

---

*(In some space beyond the amphitheatre, the five trees from LINNAEUS's whiteboard were being translated into TypeScript by TURING.*

*`aggregates.ts` would expand from five lines to more than one hundred and fifty. Five root interfaces. Thirteen sub-interfaces. Eight methods on the root of vedana-skandha. Three auxiliary types. Two core data structures. One type guard.*

*From five lines to one hundred and fifty. From labels to structure. From empty shells to living organisms.*

*The root systems of the five trees spread through the soil of TypeScript. Twenty-two Plugins would gain a skandha field in the next release. GUARDIAN was right: self-declaration is the foundation of self-awareness. A Plugin that does not know which skandha it belongs to is like a cell that does not know which organ it serves -- it might function, but it is not self-aware.*

*Five skandhas. Five trees. From seed to root system to trunk and branch.*

*The five trees have grown their root systems. From here, they will continue to grow.)*

---

*End of Chapter Six*
