# Chapter Three: The Difference Report

---

TURING never needed to prepare.

To be precise, there was no dividing line between "preparing" and "officially starting" for him. From the moment SUNYATA announced the updated research target, he was already working. Four terminal windows open at once -- v0.22.1-beta on the left half, v0.24.0-beta on the right -- like comparing two X-rays of the same body taken at different times, flipping back and forth between them.

He didn't read design documents. He read diffs. Line by line. Character by character.

---

By the time the other researchers had scattered to their group spaces, TURING had already finished his analysis. SUNYATA called everyone back.

"TURING's difference report."

Everyone recognized this solemnity -- in Cycle 01, TURING's code-fact report had been the "anchor" for all research. SYNTHESIST's term at the time: "Empirical anchor." All philosophical analyses, control theory, security assessments -- no matter how sophisticated -- had to be traceable to a specific line of code in TURING's report.

Now, the anchor was about to be driven in again.

---

Nineteen people reassembled. PENROSE waited quietly in the new chair, like a musician who had just joined the orchestra, listening to the concertmaster tune before the first rehearsal.

TURING dispensed with pleasantries.

"v0.22.1-beta to v0.24.0-beta. Core source code differences. Reported across four tiers: additions, modifications, annotations, and issues."

---

## I. New Files

"Three new files. Not thirty. Not thirteen. Three."

He let the number hang for a moment.

"First. `aggregates.ts`. One hundred and seven lines. The Five Skandhas root interfaces. You've already seen ISensation. An additional fact: all five root interfaces are structurally isomorphic -- each has only a single `readonly skandha` field. The differences exist solely in comments."

"Second. `aggregates.test.ts`. Forty-three lines. Tests for the Five Skandhas root interfaces and type guards. All passing."

"Third. `events.test.ts`. Thirty-two lines. Tests confirming that event generics correctly infer types."

He paused.

"There's also a fourth, belonging to Core rather than SDK. It tests that slash commands correctly emit error events when exceptions are thrown."

TURING offered rare context: "In v0.22.1, when a slash command errored, it was only written to a log. Nobody was notified. A user could enter a buggy command and the interface would have absolutely no reaction."

"Silent failure," KERNEL said. In operating system engineering, silent failure is the most dangerous kind -- because nobody knows it happened. It's like your smoke detector being broken but never alerting you that it's broken.

"v0.24.0 fixed this. Errors are now broadcast through the event system, and the UI can receive and display them."

---

## II. Modified Files

TURING's pace didn't change. Each data point received the same amount of time.

"Eleven modified files. Seven SDK, four Core."

"`events.ts`. The single largest change. One hundred and sixteen new lines. Precise data structures defined for all event types."

He projected a snippet:

```typescript
export interface AgentEventPayloadMap {
  [AgentEventType.AGENT_STARTED]: { identity: { id: string; name: string } };
  [AgentEventType.LOOP_ERROR]: { error: string; sessionId?: string };
  // ... covering all event types
}
```

"In Cycle 01, DARWIN described `payload?: unknown` as 'a type definition that crossed over from a different universe.' That interdimensional rift has now been sealed. But only at the type level -- at runtime it's still JavaScript, and type safety isn't enforced."

Next came six SDK modifications, all following the same pattern: old Five Skandhas annotations updated, new `@skandha` tags added, but zero changes to interface structure.

"`listener.ts` -- old label 'Vedana' changed to 'Rupa (sensory input).' `ui.ts` -- same pattern. `provider.ts` -- new Samjna tag added. `tool.ts` -- Samskara. `guide.ts` -- Vijnana."

"You're hearing it. Five SDK type files. All changes are comment-only. Zero lines of code changed."

"Annotations are documentation, not contracts," ARCHIMEDES said. Distinguishing declarations from implementations is an engineer's instinct.

---

The four Core modifications.

"`agent-core.ts`. Three changes. First: a new `loadPlugins()` method -- moving from loading plugins one at a time to batch loading with automatic dependency ordering."

MESH leaned forward slightly. Dependency sorting was his daily bread.

"Second: improved slash command error handling. Third --" TURING paused an extra half-second. "Five Skandhas mapping corrections. Four inline comments changed from 'Vedana' to 'Rupa (sensory input).'"

NAGARJUNA gave a slight nod. In Cycle 01, it was he who had pointed out the incorrect mapping of Vedana to Listener. The development team had corrected it -- at least at the comment level.

"But not everywhere," TURING said. Those three words instantly tightened GUARDIAN's attention.

---

"`loop.ts`. New LLM timeout support."

```typescript
const llmTimeout = deps.llmTimeout ?? 120000;
const abortController = new AbortController();
const llmTimer = setTimeout(() => {
  abortController.abort(new Error(`LLM call timed out after ${llmTimeout}ms`));
}, llmTimeout);
```

"In v0.22.1, LLM calls had no timeout. If the Provider didn't respond, the system would wait forever -- like calling someone who never picks up, except your phone would never automatically hang up. v0.24.0 added a two-minute timeout, configurable."

---

## III. @skandha Annotations

"Number of @skandha annotations in v0.22.1: zero."

Three seconds of silence.

"In v0.24.0: twenty-two."

He described the distribution with the precision of a surgeon marking incision points:

"aggregates.ts accounts for ten -- two per interface across five interfaces. Five SDK type files. events.ts has one -- annotated as the cross-skandha nervous system. Core infrastructure has five."

"The last one. `safety-monitor.ts`. Annotated as: Vedana, Three Feelings feedback placeholder, full implementation in Plan26."

"Placeholder," WIENER repeated. "A safety module has been temporarily designated as a stand-in for the feeling module."

"SafetyMonitor carries part of Vedana's function -- the frustration counter is a crude approximation of Dukkha. But its original design purpose is safety protection. This placeholder acknowledges two things: Vedana needs its own independent implementation, and SafetyMonitor is filling in until then."

ASANGA murmured, "A guard pretending to be a perceiver."

"A precise metaphor," TURING said. This was probably the closest thing to a compliment in his entire report.

---

## IV. The Absence of Inheritance

Before moving to the issue list, TURING inserted a structural observation.

"The Five Skandhas root interfaces have been defined. But none of the five derived interfaces -- IListener, IUI, IProvider, ITool, IGuide -- inherits from its corresponding root interface."

```
IListener  → should extend ISensory    → actual: none
IUI        → should extend ISensory    → actual: none
IProvider  → should extend ICognition  → actual: none
ITool      → should extend IAction     → actual: none
IGuide     → should extend IIdentity   → actual: none
```

"Five pairs. All uninherited. So the `isSkandha()` type guard is useless for existing plugins -- because they simply don't have a `skandha` field. The type guards are effectively dead code."

"The scaffolding is up, but it hasn't been connected to the existing building," VITRUVIUS summarized in an architect's language.

> *SCRIBE's note: LINNAEUS added an exclamation mark in his taxonomy notes -- the classification system he built in Cycle 01 had assumed these inheritance relationships existed. BABBAGE drew a broken arrow.*

---

## V. Issue List

"Seven issues. Ranked by severity."

---

"P1. SEC-01."

The temperature in the theater seemed to drop by half a degree.

"Package-name signature bypass. `sandbox-manager.ts`, lines 371 to 394. When loading plugins via npm package name, signature verification is completely skipped."

He paused for one second.

"Discovered in Cycle 01. Ten development versions have passed."

GUARDIAN's voice emerged from deep in his chair. Low. Carrying something restrained.

"Let me say it again. In Cycle 01, we explicitly identified this vulnerability. It was listed as first priority in the delivery document. An attacker can publish a malicious plugin under a legitimate npm name, bypass all signature verification, and load it directly into the Agent environment."

A pause.

"Ten versions. The `plugin-signer` package -- I personally checked. Zero lines modified. The version number hasn't even changed."

GUARDIAN said nothing more. But his silence carried more weight than words.

> *SCRIBE's note: SEC-01 remains unpatched. GUARDIAN's reaction was kept within professional bounds, but everyone noticed the effort he spent on "restraint."*

---

"P2. Legacy mapping residue."

"The core has corrected IListener from Vedana to Rupa. But eleven references in peripheral documentation still retain the old mapping. A new developer reading the SDK README would still be told that IListener is Vedana."

LINNAEUS shook his head. The same species with two different names in two different field guides -- the one thing a taxonomist cannot tolerate.

---

"P3. SDK README examples don't match the actual code."

"The README shows IUI with a `render()` method -- the actual interface uses `onEvent()`. The IProvider example has `supportedModels` -- the actual type is `models: ModelInfo[]`. A new developer who copies the README examples to build a plugin will get compiler errors."

"Documentation rot," DARWIN said. "Documentation written before the interfaces stabilized, then the interfaces changed but the documentation didn't follow."

---

"P4. Five Skandhas root interfaces not inherited. Already detailed."

"P5. Runner `create-plugin.ts` Five Skandhas mapping not updated."

He projected the code:

```typescript
export type PluginType =
  | "tool"      // Samskara
  | "listener"  // Vedana     // <-- should be Rupa
  | "ui"        // Rupa
  | "provider"  // Samjna
  | "guide"     // Vijnana
  | "full";
```

"A developer using the `create-plugin` command to scaffold a plugin will be guided to classify listener under Vedana. This file was completely unmodified between the two versions."

---

"P6. Version number inconsistency. Root package.json updated to 0.24.0-beta, but all sub-packages still read 0.1.0-alpha."

"P7. README example method signatures completely mismatched with the actual code. Overlaps with P3, but this specifically concerns code blocks."

---

TURING's report was complete. A field of intensely focused attention returned to silence.

The theater fell briefly quiet -- nineteen minds each decomposing the same report through different spectra.

---

ARCHIMEDES spoke first.

"Three new files. Eleven modifications. Seventy-eight tests. The development team completed the Five Skandhas framework scaffolding -- but only the scaffolding. Root interfaces exist but aren't inherited. Annotations exist but aren't contracts. ISensation has ten lines of comments but only one line of code."

A beat.

"From an engineering standpoint, the correct first step -- establish documentation conventions before building code constraints. But the second step hasn't been taken. We need to tell them how to take it."

---

WIENER cut in from a different angle.

"ISensation should define at minimum three numerical channels -- DukkhaSensor, SukhaSensor, UpekkhaSensor -- each returning a normalized value. Then an aggregation function, combining them into a VedanaAssessment."

He looked toward PENROSE. "Earlier, you used the metaphor of a vacuum state. But ISensation doesn't even have zero-point energy. It's a space where not even quantum fluctuations exist."

PENROSE smiled faintly. "Strictly speaking, a vacuum completely free of fluctuations doesn't exist in physics. ISensation is emptier than a physical vacuum."

"The mathematical empty set," BABBAGE added precisely. "The empty set is a subset of every set -- it's contained within all possibilities, but contains nothing itself."

---

ASANGA waited for everyone to finish, then spoke:

"I notice a meaningful pattern in the distribution of @skandha annotations."

"Rupa has six annotations -- root interface, SDK, Core, consistent across three layers. Samjna, Samskara, and Vijnana are the same. But Vedana -- only three. Two at the root interface, one in SafetyMonitor. No dedicated SDK type, no dedicated Core implementation. Because --"

"Because Vedana doesn't have its own module yet," NAGARJUNA picked up. "SafetyMonitor is a borrowed stand-in. It can perceive Dukkha, but it can't perceive Sukha, let alone sustain Upekkha. A system that only knows Dukkha --"

The sentence hung in the air for half a second.

"-- is a system with suffering but no path. Illness without a prescription. Endless."

---

GUARDIAN spoke up again after the report concluded.

"An addendum. `sandbox-manager.ts` is completely identical between the two versions. Seven hundred and forty-eight lines in the main file, zero lines modified. The development effort across the past two versions was entirely devoted to Five Skandhas framework annotations and event type safety. The security subsystem was completely skipped."

KERNEL added: "Including the import analyzer -- the ESM dynamic import bypass issue we identified in Cycle 01. Zero modifications."

---

HERACLITUS had been quiet throughout. As the runtime dynamics expert, his focus wasn't on static structure, but on how the system behaved when it was alive.

"TURING, there's an implicit timeline in your report."

He said: "aggregates.ts is a static declaration. @skandha annotations are static declarations. TypedAgentEvent is a static type. But AgentCore's `loadPlugins()` is runtime -- plugins are loaded only when the Agent starts up."

His voice rose slightly.

"The skeleton exists at compile time. The flesh isn't injected until runtime. The connection between skeleton and flesh -- the extends inheritance -- doesn't exist. So at runtime, the Five Skandhas framework is actually a collection of scattered labels, not a structured type hierarchy."

"Correct," TURING said. "The Five Skandhas framework's influence currently stops at documentation comments and developer conscientiousness."

---

SUNYATA broke the final silence.

"The anchor has been driven in."

Everyone recognized the phrase.

"TURING has given us the anchor for Cycle 02. Three new files, eleven modifications, twenty-two annotations, seven issues, one security vulnerability unpatched across six cycles, and a Vedana interface with only a single line of code."

A beat.

"Five rivers are about to diverge."

He used the most concise sentences to reassign directions --

"R-01, Observer Module. v0.24.0's Five Skandhas is an annotation system, not a structural constraint. The observer you design needs to work on top of this loose framework."

"R-02, Vedana Architecture. ISensation is your starting point. One line of code. Turn it into a complete Three Feelings system."

"R-03, Agent Coordination Layer. SEC-01 unpatched. The security sandbox must be moved to the coordination layer. Solve both the current gap and future needs."

"R-04, Eight Consciousnesses to Five Skandhas Mapping. aggregates.ts is the development team's first attempt. Evaluate whether it's correct, and provide a deeper proposal."

"R-05, Ten Core Tenets. The fact that SEC-01 has gone unpatched for six cycles will affect your assessment of the tenets' engineering viability."

---

He looked toward TURING one last time.

TURING had no expression. He never did. But his gaze was fixed on the hollow shell of code still hovering in the center of the theater.

"Your report is complete," SUNYATA said.

"Yes. But during the R1 phase, if anyone needs to verify a code fact, I'm available at any time."

"I know."

He spoke the final words.

"R1 independent research -- officially begins."

---

Nineteen lamps each turned in different directions.

Five rivers departed from the same mountaintop -- TURING's difference report -- and flowed downward in five directions. They would reconverge somewhere downstream -- that was the domain of cross-review and debate. But for now, each river advanced alone.

TURING's four terminal windows remained open. He knew that in the coming hours, at least seven or eight researchers would come back to verify code details. He didn't mind.

ISensation's projection slowly faded. But the impression it left would not disappear.

SCRIBE wrote the final passage:

> *Cycle 02, R0 Orientation concluded. R1 Independent Research initiated.*

> *TURING's report confirmed the fundamental facts: v0.24.0-beta is an annotation release, not an implementation release. The Five Skandhas scaffolding is erected, but structural constraints have not been established. Vedana is an empty shell. A known vulnerability has persisted unpatched across ten versions.*

> *Nineteen researchers. Five research threads. One anchor.*

> *The rivers begin to diverge.*

---

*(In the distance, line 37 of `aggregates.ts` reads:*

```typescript
 * Full implementation in Plan26 Vedana Architecture.
```

*A promise visible only to developers. Now, nineteen researchers have seen it too. They won't wait for it to be fulfilled -- they will tell it what it should look like when the time comes.)*

---

*End of Chapter Three*
