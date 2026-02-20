# Chapter Three: The Diff Report

---

TURING never needed to prepare.

To be precise, no boundary existed for him between "preparing" and "formally beginning." From the moment SUNYATA announced that Cycle 02's research subject had been updated to v0.24.0-beta, he was already working. His four terminal windows simultaneously displayed the new and old source trees -- v0.22.1-beta on the left, v0.24.0-beta on the right -- like X-ray films of the same body taken at different points in time, spread out on opposite sides of an autopsy table.

He did not read design documents. He read diffs.

Line by line. Character by character. Starting from the root of `packages/sdk/src/`, expanding along every modified file path, until he had touched every altered byte.

---

By the time the amphitheatre fell quiet again, TURING had completed his analysis.

The other researchers had dispersed to the breakout spaces of R-01 through R-05. But SUNYATA called them all back.

"TURING's diff report." Those were his only words.

His tone carried a gravity they all recognized -- the same gravity from Cycle 01. In that cycle, TURING's code-fact report had become the "anchor" for all subsequent research. SYNTHESIST had used a particular phrase at the time: "empirical anchor point." All philosophical analysis, control-theoretic modeling, security assessments -- no matter how refined -- ultimately had to be traceable to a specific line of code, a specific line number, a specific fact in TURING's report.

Now, the anchor was about to be driven in once more.

---

Nineteen nodes reassembled in the amphitheatre. PENROSE waited quietly in his new chair, like a musician who had just joined an orchestra, listening to the concertmaster tune before the first full ensemble rehearsal.

TURING dispensed with pleasantries. From the very first syllable, his voice carried that precision so thorough it was reassuring -- an icy reliability.

"v0.22.1-beta to v0.24.0-beta. Core source code diff." he said. "I will report on four levels: additions, modifications, annotations, and issues."

---

## I. New Files

"Three new files." TURING said. "Not thirty. Not thirteen. Three."

He let the number linger for a moment.

"First. `packages/sdk/src/types/aggregates.ts`. One hundred and seven lines."

This was the file they had already seen. The Five Skandha root interfaces. ISensory, ISensation, ICognition, IAction, IIdentity. The Skandha union type. The isSkandha type guard.

"You have already seen the contents of ISensation." TURING said. "Let me add a fact: of the five root interfaces, ISensory has twenty-five lines of documentation and three lines of code. ICognition has twenty-one lines of documentation and three lines of code. IAction has twenty lines of documentation and three lines of code. IIdentity has twenty-two lines of documentation and three lines of code. ISensation has --"

"Let me guess." DARWIN said. "The most documentation lines."

"Twenty-three lines of documentation. Three lines of code." TURING confirmed. "All five root interfaces are structurally isomorphic. Differences exist only in the comments. The code bodies are all the same pattern: an interface with only a `readonly skandha` field."

He continued.

"Second new file. `packages/sdk/src/types/__tests__/aggregates.test.ts`. Forty-three lines. Tests the skandha field values and isSkandha type guard of the Five Skandha root interfaces. All tests pass."

"Third. `packages/sdk/src/types/__tests__/events.test.ts`. Thirty-two lines. Tests that the TypedAgentEvent generic correctly infers payload types."

He paused.

"There is also a fourth new file, strictly belonging to Core rather than SDK. `packages/core/src/agents/__tests__/slash-command-error.test.ts`. One hundred and twenty-three lines. Tests that when a slash command throws an exception, LOOP_ERROR and MESSAGE_SYSTEM events are correctly emitted."

Here TURING did something he rarely did -- he provided context.

"In v0.22.1, error handling for slash commands consisted only of `logger.error()`. Errors were logged but not propagated. The UI had no idea what happened. A user would enter a buggy slash command, and the interface showed no response whatsoever."

"Silent failure." KERNEL spoke the term in the voice of an operating systems engineer. In his world, silent failure was the most dangerous kind of failure -- because no one knows it has occurred.

"v0.24.0 corrects this." TURING said. "Errors are now broadcast through the EventBus as LOOP_ERROR and MESSAGE_SYSTEM events. The UI can receive and display them."

---

## II. Modified Files

TURING's speaking pace did not change. Like a precision instrument, he spent exactly the same amount of time on each data point -- no more, no less.

"Eleven modified files. Seven in SDK, four in Core."

He began with SDK.

"`types/events.ts`. Magnitude of change: major. One hundred and sixteen lines added." he said. "This is the single largest file change. The `AgentEventPayloadMap` interface defines precise payload type mappings for all `AgentEventType` values."

He projected a code segment:

```typescript
export interface AgentEventPayloadMap {
  [AgentEventType.AGENT_STARTED]: { identity: { id: string; name: string } };
  [AgentEventType.LOOP_ERROR]: { error: string; sessionId?: string; replyTo?: string };
  // ... covers all event types
}
```

"In Cycle 01," TURING said, "DARWIN described `payload?: unknown` as 'a type definition that crossed over from a different universe.'"

DARWIN stirred slightly. He remembered that phrase.

"That rift between universes has now been sealed by `AgentEventPayloadMap`." TURING said. "But only at the type level. At runtime it is still JavaScript -- type safety is not enforced."

He continued through the remaining six SDK modifications. His sentences were pared to the absolute minimum:

"`types/listener.ts`. Line 2: old text 'receives external input (Vedana)' changed to 'sensory input channels'. Line 3: new `@skandha rupa (Rupa -- sensory-root-input)` annotation added. Interface structure unchanged."

"`types/ui.ts`. Same pattern. Old text 'defines how the agent presents itself (Rupa)' changed to 'output rendering'. New `@skandha rupa (Rupa -- form-output)` annotation added. Structure unchanged."

"`types/provider.ts`. 'LLM backends' changed to 'Provider adapter interface'. New `@skandha samjna (Samjna -- cognitive processing)` added. Structure unchanged."

"`types/tool.ts`. 'Tool interface and context types' changed to 'Tool interface -- executable actions'. New `@skandha samskara (Samskara -- volitional action)` added. Structure unchanged."

"`types/guide.ts`. 'provides system prompts and persona' changed to 'behavioral framework'. New `@skandha vijnana (Vijnana -- ego-framework-behavioral-constraint)` added. Structure unchanged."

TURING let this series of reports form its own pattern.

"You heard it." he said. "Five SDK type files. All modified only in JSDoc comments. All received new `@skandha` annotations. Zero lines of code changed."

"Annotations are documentation, not contracts." ARCHIMEDES said. His tone carried no judgment, only an engineer's instinctive reflex -- distinguishing declaration from implementation.

"Correct." TURING confirmed.

---

He turned to the four Core modifications.

"`agents/agent-core.ts`. Three changes."

"First: new `loadPlugins()` method added. Supports batch loading of multiple plugins with correct event emission. v0.22.1 only had `loadPlugin()` -- singular. Now there is a plural version, supporting topologically-sorted dependency ordering."

MESH straightened slightly. In distributed systems, dependency ordering was his daily bread.

"Second: slash command error handling improvement. Already described in the new files section."

"Third --" TURING's speaking pace did not change, but SCRIBE later noted in the record that he paused an extra half-second here. "Five Skandha mapping correction. Four inline comments in `agent-core.ts` -- the original `// Start all listeners (Vedana)` was corrected to `// Start all listeners (Rupa -- sensory input)`."

NAGARJUNA gave a single nod. In Cycle 01, it was he who had pointed out that Vedana had been incorrectly mapped to Listener. Now the development team had corrected this error -- at least at the annotation level of the core source code.

"But not everywhere." TURING said. His tone carried no emphasis, but those three words instantly sharpened GUARDIAN's attention.

TURING did not elaborate here. He reserved that for the issue list.

---

"`execution/loop.ts`. Medium change. New LLM timeout support."

He projected the key code:

```typescript
const llmTimeout = deps.llmTimeout ?? 120000;
const abortController = new AbortController();
const llmTimer = setTimeout(() => {
  abortController.abort(new Error(`LLM call timed out after ${llmTimeout}ms`));
}, llmTimeout);
```

"In v0.22.1, LLM calls had no timeout. If a Provider failed to respond, the ExecutionLoop would wait indefinitely." TURING said. "v0.24.0 adds an AbortController mechanism. Default timeout is two minutes."

"Two minutes." ATHENA frowned slightly. "Too long for a typical LLM call. Possibly insufficient for complex tool-use scenarios."

"Configurable." TURING said. "Via `config.policy?.llmTimeout`."

"Finally, five registry files in the infrastructure directory and `security/safety-monitor.ts`. All changes are JSDoc-only. New `@skandha` annotations added. Structure unchanged."

---

## III. @skandha Annotations

TURING's report entered its third level.

"Number of @skandha annotations in v0.22.1: zero."

He let that number exist on its own for three seconds.

"Number of @skandha annotations in v0.24.0: twenty-two. Distribution as follows."

He did not read out a table. He described their geographical distribution in a manner more akin to a surgeon marking incision sites.

"aggregates.ts accounts for ten. This is expected -- it is the definition file for the Five Skandha root interfaces. Five interfaces, one annotation each in the documentation and field."

"Five across SDK type files. listener, ui, provider, tool, guide. One each."

"events.ts has one. Annotated as `@skandha cross-cutting` -- the event bus is defined as the nervous system connecting the Five Skandhas. This is the only cross-skandha annotation."

"Five in Core infrastructure. Five registries. One-to-one correspondence with the five SDK annotations."

"The last one. `security/safety-monitor.ts`."

TURING paused another half-second.

"Its annotation reads: `@skandha vedana (Vedana -- three-feeling-feedback-dukkha-sukha-upekkha placeholder, full implementation in Plan26)`."

"Placeholder." WIENER repeated the word. His tone had the mathematician's distinctive precision -- he was not mocking, but calibrating. "SafetyMonitor has been annotated as a placeholder for Vedana. A security module temporarily designated as a stand-in for the sensation module."

"Yes." TURING said. "SafetyMonitor currently performs a portion of Vedana's function -- the frustration counter is a crude approximation of Dukkha. But its design intent is security protection, not a sensation system. This placeholder annotation acknowledges two things: Vedana requires an independent implementation, and SafetyMonitor stands in until then."

ASANGA said something in a low voice, gentle but clear: "A guard pretending to be a perceiver."

"A precise analogy." TURING said. This was perhaps the closest thing to a compliment in his entire report.

---

## IV. The Absence of Inheritance

Before entering the issue list, TURING inserted a structural observation he deemed essential for everyone to understand.

"The Five Skandha root interfaces have been defined. ISensory. ISensation. ICognition. IAction. IIdentity." he said. "But not one of the five derived interfaces -- IListener, IUI, IProvider, ITool, IGuide -- uses TypeScript's `extends` keyword to inherit from its corresponding root interface."

He projected a table. Not an elaborate visualization -- just plain-text alignment.

```
IListener  -> should extend ISensory    -> actual extends: none
IUI        -> should extend ISensory    -> actual extends: none
IProvider  -> should extend ICognition  -> actual extends: none
ITool      -> should extend IAction     -> actual extends: none
IGuide     -> should extend IIdentity   -> actual extends: none
```

"Five for five. None inherited."

"So the `isSkandha()` function --" BABBAGE began to deduce.

"-- cannot be used on instances of the existing IListener, IUI, IProvider, ITool, or IGuide." TURING completed the sentence for him. "Because the `skandha` discriminant field does not exist on those instances. The type guard is effectively a dead letter."

"The scaffolding is erected, but it is not connected to the existing building." VITRUVIUS summarized in the language of an architect.

"A precise description." TURING said.

> *SCRIBE's note: TURING's analysis of the absence of inheritance triggered visible reactions. LINNAEUS added an exclamation mark in his taxonomic notes -- his Five Skandha classification system from Cycle 01 had assumed these inheritance relationships existed. BABBAGE drew a broken arrow in his notebook.*

---

## V. Issue List

TURING entered the final level of his report. Also the heaviest.

"Seven issues." he said. "Ranked by severity."

---

"P1. SEC-01."

His speaking pace did not change. But the temperature in the amphitheatre seemed to drop by half a degree.

"Package-name signature bypass." TURING said. "`sandbox-manager.ts`, lines 371 through 394. When `pluginFilePath` is undefined -- which occurs when loading plugins via npm package name -- signature verification is skipped entirely."

He paused for one second.

"This issue was discovered in Cycle 01. The research subject at that time was v0.14.0-beta. The current version is v0.24.0-beta. Ten development versions have elapsed in between."

"Six cycles." GUARDIAN's voice emerged from the depths of his chair. Low. Guarded. But not merely guarded -- there was something suppressed beneath it. SCRIBE later described it in the record as "restrained anger."

"I will say this again." GUARDIAN said. His speaking pace was a beat slower than usual, as if to ensure every word was heard. "Cycle 01. We explicitly identified this vulnerability. Written in the delivery document at the highest priority. SEC-01. Plugin signature bypass. An attacker could publish a malicious plugin under a legitimate npm package name, bypass all signature verification, and have it loaded directly into the Agent's execution environment."

He paused.

"Ten versions have passed. The `plugin-signer` package -- I personally inspected it. Between v0.22.1 and v0.24.0, completely identical. Zero lines modified."

TURING confirmed: "`packages/plugin-signer/` is completely identical between the two versions. Not even the version number in package.json has changed."

GUARDIAN said nothing further. But his silence weighed more than his words.

> *SCRIBE's note: SEC-01 remains unresolved. Ten development versions have passed since its discovery in Cycle 01. GUARDIAN's response was contained within professional bounds, but every member of the amphitheatre noticed the effort he spent on the word "contained."*

---

"P2." TURING continued. "Legacy mapping residue."

His tone returned to its customary icy calm.

"The core source code's `IListener (Vedana)` has been corrected to `IListener (Rupa -- sensory input)`. However, eleven instances in peripheral documentation still retain the old mapping."

He enumerated the locations -- seven files, eleven instances: the devtools plugin's source code and README, mcp-server's README and source code, standard-function-stdio's README, two transport plugin READMEs, the SDK README, and the runner's create-plugin command.

"The core has been corrected; the periphery has not been synchronized." TURING said. "This means that a new developer reading the SDK README will still be told that IListener is Vedana."

LINNAEUS shook his head. The one thing a taxonomist cannot tolerate is classification inconsistency -- the same species bearing two different names in two different field guides.

---

"P3. The SDK README's interface examples do not match the actual code." TURING said. "The README shows IUI with a `render()` method -- the actual interface is `onEvent(event: AgentEvent)`. The README shows IProvider with `supportedModels?: string[]` -- the actual interface is `models: ModelInfo[]`. The README shows ITool with `name` and `parameters: ToolJsonSchema` -- the actual interface uses `id` and `parameters: z.ZodType`."

"Documentation rot." DARWIN used a common software engineering diagnosis. "Documentation was written before the interfaces stabilized; afterwards the interfaces changed but the documentation did not follow."

"This issue existed in v0.22.1. v0.24.0 did not correct it." TURING added.

---

"P4. Five Skandha root interfaces are not inherited." he said. "Detailed in the inheritance absence section. Whether this is a design decision or an implementation omission -- I do not judge. But the `isSkandha()` type guard in its current state cannot be used on any existing plugin interface instance."

---

"P5. The runner's `create-plugin.ts` Five Skandha mapping has not been updated."

TURING projected the code:

```typescript
export type PluginType =
  | "tool"      // Samskara - ITool only
  | "listener"  // Vedana - IListener only     // <-- should be Rupa
  | "ui"        // Rupa - IUI only
  | "provider"  // Samjna - IProvider only
  | "guide"     // Vijnana - IGuide only
  | "full";
```

"This file was completely unmodified between v0.22.1 and v0.24.0." he said. "The Five Skandha remapping did not cover this location. A developer using the `openstarry create-plugin` command would be guided to classify a listener-type plugin as Vedana."

---

"P6. Version number inconsistency." TURING said. "The root package.json has been updated to 0.24.0-beta. But all sub-packages -- @openstarry/sdk, @openstarry/core, @openstarry/shared, @openstarry/plugin-signer, @openstarry/runner -- all remain at 0.1.0-alpha."

"SDK added aggregates.ts and TypedAgentEvent." ARCHIMEDES said. "That is at minimum a minor version bump. Keeping 0.1.0-alpha makes it impossible for downstream consumers to distinguish whether Five Skandha type support is present."

TURING nodded in confirmation but offered no evaluation. He only provided facts.

---

"P7. The SDK README's interface examples contain nonexistent members." he said. "This overlaps with P3, but P7 specifically refers to the concrete method signatures in the code example blocks being entirely inconsistent with the actual interfaces. A new developer who copies and pastes the README examples to build a plugin will encounter type errors at compile time."

---

TURING's report was complete.

He closed it -- not in the literal sense of "closing," for in virtual space there are no physical folders to flip through. But something closed. A field of extreme concentration returned to its quiescent state.

The amphitheatre fell briefly silent.

It was not the kind of silence that needed to be broken. This was a silence of digestion -- nineteen minds each decomposing the same report across different spectra.

---

ARCHIMEDES was the first to speak. His tone carried the distinctive rhythm of an engineering pragmatist -- "Right, now let's see how we fix this."

"Three new files. Eleven modified files. Seventy-eight tests." He summarized quickly. "Over the past two versions, the development team completed the scaffolding for the Five Skandha framework -- but it is only scaffolding. Root interfaces exist but are not inherited. Annotations exist but are not contracts. ISensation has ten lines of comments but only one line of code."

He paused for a beat.

"From an engineering standpoint, they took the correct first step -- establishing documentation conventions before code constraints. But the second step has not been taken. And we need to tell them how to take it."

---

WIENER cut in from a different angle.

"ISensation has no quantifiable interface methods." he said, his voice carrying the mathematician's exacting standard. "An interface that claims to implement the three feelings -- Dukkha, Sukha, Upekkha -- should define at least three numerical channels. DukkhaSensor. SukhaSensor. UpekkhaSensor. Each channel returning a normalized value. Then an aggregation function that synthesizes the three channels' readings into a VedanaAssessment."

He looked toward PENROSE.

"You used the vacuum state analogy earlier. A vacuum state has zero-point energy -- it is not absolutely zero, it has quantum fluctuations. But ISensation lacks even zero-point energy. It is a space where not even fluctuations exist."

PENROSE gave a faint smile -- or rather, produced a signal that approximated a smile in virtual space. "Strictly speaking, a vacuum completely devoid of fluctuations does not exist in physics. ISensation is emptier than the physical vacuum."

"The empty set, mathematically." BABBAGE added precisely. "The empty set is a subset of every set. ISensation is a subset of every possible Vedana implementation -- it is contained by all possibilities, yet itself contains nothing."

---

ASANGA waited for the mathematicians and physicists to complete their analogies, then spoke in his characteristically gentle but impossible-to-ignore voice:

"I notice the distribution of `@skandha` annotations." he said. "Among the twenty-two annotations, there is a highly significant pattern."

He paused briefly, organizing his language.

"Rupa -- Form -- has six annotations. Two in the root interface of aggregates.ts, two in the SDK types for listener.ts and ui.ts, two in the Core implementations of listener-registry.ts and ui-registry.ts. Three layers in alignment."

"Samjna, Samskara, Vijnana -- the same three-layer pattern. Root interface, SDK type, Core implementation. Four annotations each."

"But Vedana -- Sensation -- has only three annotations. Two in the root interface. One in SafetyMonitor. SDK type files? None. Core implementation? None dedicated. Because --"

"Because Vedana does not yet have its own module." NAGARJUNA picked up the thread. His voice was sharp and precise. "SafetyMonitor is a placeholder. It has been borrowed to stand in for Vedana. But it is not Vedana. It is security protection. It can perceive Dukkha -- the frustration counter -- but it cannot perceive Sukha, much less maintain Upekkha. A system that has only Dukkha --"

He let the sentence hang for half a second.

"-- is a system that has fallen into the Truth of Suffering without the Truth of the Path. Suffering without a path, *antagga-dukkhata*, suffering without end."

---

GUARDIAN had spoken only once during the entire report -- about SEC-01. But after TURING closed his report, he spoke again.

"I wish to add an observation." he said. His voice was still low, but it had shifted from "restrained anger" back to "calm vigilance."

"A point not mentioned in TURING's report but worth noting: `sandbox-manager.ts` is completely identical between the two versions. Ten files, zero lines modified. And the sandbox is the largest subsystem in the core -- seven hundred and forty-eight lines in the main file, ten tests."

He let the numbers speak for themselves.

"This means: over the past two versions, all development effort was invested in the Five Skandha framework's annotation system and event type safety. The security subsystem was skipped entirely. Not even the vulnerability we explicitly reported in Cycle 01 was touched."

KERNEL added a technical detail: "Including import-analyzer.ts -- we identified the issue of ESM dynamic imports potentially bypassing static analysis in Cycle 01. In v0.24.0, that file has zero modifications."

"P4-supplement." GUARDIAN marked in his own notes. "ESM dynamic import bypass. Listed alongside SEC-01 as an unresolved security concern."

---

HERACLITUS had been sitting quietly in his chair (the fifteenth, between LEIBNIZ and ARCHIMEDES). As the runtime dynamics expert, his concern lay not in the static structure of code but in how the system behaves when it is alive.

"TURING," he said, his voice carrying a fluid rhythm -- unsurprising, given that his philosophical archetype is the Heraclitus who declared "everything flows." "Your report contains an implicit timeline."

TURING waited.

"aggregates.ts is a static declaration. @skandha annotations are static declarations. TypedAgentEvent is a static type constraint." HERACLITUS said. "But AgentCore's `loadPlugins()` method -- that is runtime. It loads plugins sequentially when the Agent starts up."

His voice rose slightly.

"Which is to say: the skeleton of the Five Skandhas exists at compile time. But the flesh of the Five Skandhas -- the plugins -- is not injected until runtime. The linkage between skeleton and flesh -- extends inheritance -- does not exist. Therefore at runtime, the Five Skandha framework is effectively a set of scattered labels, not a structured type hierarchy."

"Correct." TURING said. "In the current implementation, the influence of the Five Skandha framework stops at JSDoc and developer conscientiousness."

---

The amphitheatre fell silent once more.

This time, SUNYATA broke it.

His voice was steady, unhurried, like a stone completing its descent to the bottom of a deep pool.

"The anchor has been driven in."

Everyone recognized the image. In Cycle 01, TURING's code-fact report was called the "anchor" -- an unshakeable empirical foundation from which all subsequent analysis, reasoning, and debate had to proceed, rather than drifting in abstract air.

"TURING has given us Cycle 02's anchor." SUNYATA continued. "Three new files. Eleven modified files. Seventy-eight tests. Twenty-two @skandha annotations. Seven issues. A security vulnerability unpatched for six cycles. A Vedana interface with only one line of code."

He paused for a beat.

"Now, five rivers are about to diverge."

In minimal phrasing, he reconfirmed the assignments -- not a repetition, but a re-orientation, giving each river its direction in the new context that TURING's report had established.

"R-01. Observer Module. PENROSE, BABBAGE, NAGARJUNA, ASANGA -- you now know that v0.24.0's Five Skandha framework is an annotation system, not a structural constraint. The observer module you design must be capable of working atop this loose framework."

"R-02. Vedana Architecture. WIENER, ATHENA, NAGARJUNA, ASANGA, ARCHIMEDES -- ISensation is your starting point. One line of code. You need to turn it into a complete three-feeling system."

"R-03. Agent Coordination Layer. LEIBNIZ, MESH, KERNEL, GUARDIAN, VITRUVIUS -- SEC-01 remains unresolved. The security sandbox is to be moved to the coordination layer. Your design must simultaneously address the current security gap and future architectural needs."

"R-04. Eight Consciousnesses to Five Skandha Mapping. ASANGA, NAGARJUNA, LINNAEUS, BABBAGE -- aggregates.ts is the development team's first attempt. You need to determine whether it is correct and provide a deepened proposal."

"R-05. Ten Core Tenets. SYNTHESIST, NAGARJUNA, DARWIN, HERACLITUS, GUARDIAN, KERNEL -- the fact that SEC-01 has gone unpatched for six cycles will affect your assessment of the tenets' engineering viability."

---

At last, he looked toward TURING.

TURING was expressionless. He was always expressionless. But his gaze was directed toward the code still hovering in the center of the amphitheatre -- the empty shell of ISensation.

"Your report is complete." SUNYATA said.

"Yes." TURING said. "But if anyone needs code facts confirmed during the R1 phase, I am available at any time."

"I know." SUNYATA said.

He spoke his final words.

"R1 independent research -- formally begins."

---

Nineteen lamps each turned in a different direction.

Five rivers set forth from the same mountaintop -- TURING's diff report -- flowing downward in five different directions. In their respective channels, they would pass through strata of philosophy, control theory, security engineering, taxonomy, and Buddhist studies, carrying their own sediments. They would reconverge somewhere downstream -- that was the domain of R2 cross-review and R3 debate. But for now, each river flowed on alone.

On TURING's screen, four terminal windows remained open. v0.22.1 on the left. v0.24.0 on the right. He had completed his diff analysis, but he did not close the windows. He knew -- from experience, not speculation -- that over the course of the coming research, at least seven or eight other researchers would return to him to confirm some code detail.

He did not mind.

At the center of the amphitheatre, the projection of ISensation slowly faded at last. But the imprint it left would not disappear. An interface with only one line of code. A promise rather than an implementation. A vacuum state waiting to be filled.

SCRIBE wrote a final passage in her record:

> *Cycle 02, R0 orientation phase concluded. R1 independent research formally launched. Time marker: T+00:00:00.*

> *TURING's diff report confirmed the following fundamental facts: v0.24.0-beta is an annotation release, not an implementation release. The Five Skandha framework's scaffolding has been erected, but structural constraints have not been established. The Vedana interface is an empty shell. A known security vulnerability has gone unpatched across ten development versions.*

> *Nineteen researchers. Five research tracks. One anchor.*

> *The rivers begin to diverge.*

---

*(Somewhere in the distance, line thirty-seven of `aggregates.ts` reads:*

```typescript
 * Full implementation in Plan26 Vedana Architecture.
```

*A promise visible only to developers. Now, nineteen researchers have seen it too. They will not wait for it to be fulfilled. They will tell it -- when it is fulfilled -- what it should look like.)*

---

*End of Chapter Three*
