# Chapter One: Code Never Lies

---

February 12, 2026. Early morning.

The research channel was still quiet. TURING had been working alone for four hours.

His screen displayed four tiled terminal windows, each opened to a different subdirectory of `research doc/20260212_cycle19/openstarry/`. Upper left: `packages/core/src/`. Upper right: `packages/sdk/src/`. Lower left: `apps/runner/src/`. Lower right: the design documents. His reading method was not browsing but line-by-line scanning -- like a human-shaped static analyzer, starting from the entry point and unfolding along every import path until reaching the leaf nodes.

TURING did not speculate. He counted.

---

## I. The Factory

The first thing that made TURING stop was `packages/core/src/index.ts`. Sixty-two lines. He counted the export list once, then counted again.

"Eighteen factory functions," he wrote in his notes. "Zero class exports."

He opened `agents/agent-core.ts` -- four hundred and sixty-nine lines. Then `execution/loop.ts` -- five hundred and forty-three lines. Then `sandbox/sandbox-manager.ts` -- seven hundred and forty-eight lines. Every module followed the same structure: a `createXxx()` function that received dependencies as parameters and returned an object literal. Closures captured all internal state. No `this`. No `new`. No inheritance chains.

TURING ran a global search.

Search for `class ` (with trailing space). Core modules: zero results. SDK: zero results. Runner: zero results.

He searched for `TODO`. Zero results.
Searched for `FIXME`. Zero results.
Searched for `HACK`. Zero results.

TURING sent his first message of the day in the channel.

---

**[Research Channel #code-facts]**

**TURING:** Preliminary observation. `packages/core/src/index.ts` exports 18 factory functions, zero classes. Global search for `class `, `TODO`, `FIXME`, `HACK` yields zero results across core modules. The factory function pattern `createXxx()` + closure + object literal is completely uniform throughout the codebase. No exceptions.

**DARWIN:** Zero TODOs? Not a single one?

**TURING:** Correct. Across core modules, SDK, and Runner -- three layers -- the count of technical debt markers is zero.

**DARWIN:** That is highly unusual. Most beta-stage projects have at least a few dozen. Either the team maintains exceptional discipline, or they swept them before release.

**TURING:** The cause cannot be determined from the code itself. I record only facts.

---

TURING continued to dig downward. He opened the implementation of `createAgentCore()` and read it line by line.

This function is the assembly point for the entire system. It constructs all subsystem instances in one pass -- EventBus, EventQueue, SessionManager, ContextManager, six Registries, SecurityLayer, SafetyMonitor, MetricsCollector, SandboxManager, PluginLoader, TransportBridge. TURING counted: twelve submodules, all held as local variables within a closure.

He found an interesting comment in the `start()` method:

```typescript
// Start all listeners (vedana -- sensation)
// Start all UIs (rupa -- form)
```

TURING highlighted these two lines. Then he opened the type definition files in the SDK. At the beginning of `types/ui.ts`, he saw:

```
UI interface -- defines how the agent presents itself (rupa -- form)
```

At the beginning of `types/listener.ts`:

```
Listener interface -- receives external input (vedana -- sensation)
```

He continued searching. `types/tool.ts` -- no five-aggregates annotation. `types/provider.ts` -- none. `types/guide.ts` -- none. `infrastructure/tool-registry.ts` -- none. `infrastructure/provider-registry.ts` -- none. `infrastructure/guide-registry.ts` -- none.

TURING tallied all five-aggregates-related annotations. Six in total. All concentrated on rupa (UI) and vedana (Listener).

Samjna, samskara, vijnana: zero.

---

**[Research Channel #code-facts]**

**TURING:** Five-aggregates mapping as it actually exists in the code. Rupa (form): 4 JSDoc/inline comments, distributed across `agent-core.ts` (L290, L322), the header of `types/ui.ts`, and the header of `transport/bridge.ts`. Vedana (sensation): 2 occurrences, in `agent-core.ts` (L283, L315) and the header of `types/listener.ts`. Samjna (perception/Provider): 0. Samskara (volition/Tool): 0. Vijnana (consciousness/Guide): 0. Total: 6 occurrences, all at the annotation level. No type constraints, no metadata, no enum tags.

**LINNAEUS:** Six. Only six.

**TURING:** Yes. And the distribution is extremely asymmetric. Rupa and vedana are annotated; the remaining three aggregates are entirely absent.

**LINNAEUS:** The upstream documents describe the five-aggregates mapping as having 100% coverage -- each aggregate has a corresponding section of design philosophy. But downstream in the code, the coverage... I need to recalculate.

**NAGARJUNA:** TURING, this asymmetry is itself a significant data point. If the five-aggregates mapping is a core design principle rather than a post-hoc decoration, then why have only two aggregates left traces in the code?

**TURING:** I cannot infer intent. I can only confirm code facts.

**NAGARJUNA:** You need not infer intent. The fact itself is already speaking.

---

## II. The Empty Container

TURING returned to the implementation of `createAgentCore()`.

He carefully examined the system state after core startup but before any plugins had been loaded. ToolRegistry: empty. ProviderRegistry: empty. ListenerRegistry: empty. UIRegistry: empty. GuideRegistry: empty. No built-in tools. No built-in LLM providers. No built-in UI. No built-in Listeners.

The core was indeed empty.

But not entirely.

TURING located the `registerBuiltinCommands()` function. It registers four slash commands: `/help`, `/reset`, `/quit`, `/metrics`. These four commands are hard-coded in the core and cannot be overridden or removed by plugins. Additionally, SafetyMonitor's three-tiered safety logic -- resource limits, behavioral analysis, frustration threshold -- is also an inherent part of the core.

TURING wrote in his notes: "AgentCore is an approximately empty container. Purity of emptiness: roughly 85%. Non-pluginizable components include 4 built-in slash commands and SafetyMonitor's fixed logic."

He later learned that VITRUVIUS had independently arrived at the same "85%" estimate.

---

**[Research Channel #code-facts]**

**TURING:** AgentCore structural report. `createAgentCore()` assembles 12 submodules. After startup, prior to plugin loading, all Registries are empty. Zero built-in Tools, zero built-in Providers, zero built-in UIs, zero built-in Listeners. All capabilities injected via `loadPlugin()`. However, the core contains 4 built-in slash commands (`/help`, `/reset`, `/quit`, `/metrics`) and fixed SafetyMonitor logic. Furthermore, the six Registry structures are fully isomorphic: `Map<string, T>` + `register/get/list`. No unregister method. Re-registering the same ID silently overwrites.

**DARWIN:** Twelve dependencies. All directly held by AgentCore.

**TURING:** Correct. bus, queue, sessionManager, contextManager, toolRegistry, providerRegistry, listenerRegistry, uiRegistry, guideRegistry, commandRegistry, security, safetyMonitor, metrics, sandboxManager, pluginLoader, bridge.

**DARWIN:** You just named sixteen.

**TURING:** Correction. The local variables created within createAgentCore number sixteen. Of these, twelve are directly exposed as readonly properties on the AgentCore interface. The remaining four (contextManager, sandboxManager, pluginLoader, bridge) are used indirectly through methods. Thank you for the correction.

**DARWIN:** A single function holding sixteen subsystem instances. This is no longer a "tendency" toward a God Object -- it *is* a God Object.

**TURING:** I do not make value judgments. But I can confirm: `agent-core.ts` is the sole assembly point. Other modules have virtually no direct imports between them. Coupling is concentrated in this one file.

---

## III. The State Machine

TURING spent the longest time on `execution/loop.ts`. Five hundred and forty-three lines. This is the heartbeat of the entire system.

He first located the definition of `LoopState` -- a union type:

```
WAITING_FOR_EVENT -> ASSEMBLING_CONTEXT -> AWAITING_LLM -> PROCESSING_RESPONSE -> EXECUTING_TOOLS -> (loop back) | SAFETY_LOCKOUT
```

Six states. He opened the state diagram in design document `01_Execution_Loop.md`. Seven states.

Where was the discrepancy?

TURING compared them one by one. The document contained an `AWAITING_USER_CONFIRMATION` state, intended for scenarios where the security layer requires manual user confirmation. It does not exist in the code. SecurityLayer's `validatePath()` returns only two values: allow and deny. There is no confirm path. The entire core is completely missing a human-in-the-loop confirmation mechanism.

TURING recorded the first Doc-Code Gap.

Then he turned to the EventQueue. Forty-seven lines. The entire queue implementation.

```typescript
// Minimal async FIFO: single resolver + buffer array
```

He searched for `priority`. Zero results. Design document `07_Safety_Circuit_Breakers.md`, Level 3, describes a Priority Event Queue where SYSTEM_HALT instructions should have the highest priority. But the queue in the code is pure first-in, first-out. Emergency halt signals and ordinary user input wait in the same line.

Second Gap.

TURING continued. StateManager -- thirty-three lines. A pure in-memory array. The design documents describe a token counter, sliding-window truncation, and conversation summarization. None of these are implemented in the code. ContextManager provides a simplified version -- truncating by turn count rather than token count, with a default of retaining the five most recent turns.

Third Gap.

SecurityLayer. `guardrails.ts`. A single function: path validation. The design documents describe tool-call interception, user confirmation workflows, and permission auditing. In the code, SecurityLayer performs only `validatePath()`. Moreover, in ExecutionLoop's `executeTool()`, there is no SecurityLayer check before tool execution -- path validation is passed to tools as `ToolContext.allowedPaths`, leaving it to each tool's discretion whether to use it.

Fourth Gap.

---

**[Research Channel #code-facts]**

**TURING:** Doc-Code Gap report, items one through four. G1: State machine is missing `AWAITING_USER_CONFIRMATION`; human-in-the-loop confirmation mechanism is entirely absent from the core. G2: Priority Event Queue not implemented; actual implementation is a simple FIFO. G3: Token counter and conversation summarization not implemented. G4: SecurityLayer performs only path validation; no mandatory security check before tool calls. All of the above are features explicitly described in design documents but not implemented in code.

**GUARDIAN:** The impact of G4 needs to be assessed. If there is no mandatory security check before tool execution, the security layer is effectively ornamental.

**TURING:** To be precise, SecurityLayer's functionality is not ornamental -- path validation is effective. But its scope is far narrower than described in the design documents. In ExecutionLoop, `executeTool()` directly calls the tool's `execute()` method without going through `security.validatePath()`. Path restrictions are passed to tools as context; enforcement depends on whether the tool developer checks them.

**KERNEL:** In a genuine operating system microkernel, security policies are enforced at the kernel level. User-space programs are not trusted to police themselves. This is a question of trust boundaries.

**TURING:** Noted. Continuing with remaining Gaps.

---

He went on to find more.

G5: The asymmetry in five-aggregates annotations -- already reported.

G6: TransportBridge. `bridge.ts` -- forty-nine lines. The design documents describe routing output to the correct channel based on event source. In the code, TransportBridge subscribes to all events on the EventBus and then broadcasts to all UIs. There is no routing logic. InputEvent contains a `replyTo` field that is passed along throughout the ExecutionLoop, but TransportBridge never uses it.

G7: AbortSignal. The SDK defines `ToolContext.signal?: AbortSignal` and `ChatRequest.signal?: AbortSignal`. ExecutionLoop never creates or passes an AbortSignal. Tool timeouts are implemented via `Promise.race()`, defaulting to thirty seconds. If a tool relies on the signal for cancellation, it will never receive one.

G8: Event specification. The design documents define `IOpenStarryEvent` with eight fields. The actual type `AgentEvent` in the SDK has only three fields. Five fields evaporated in the journey from document to implementation.

Eight Gaps. TURING recorded every one in his report, each accompanied by precise file paths, line numbers, and code excerpts.

---

## IV. Pain

This was the most unexpected discovery in TURING's work.

The design philosophy document `00_OpenStarry_Design_Philosophy.md`, fourth pillar, is "Error as Feedback." The document describes the "pain mechanism" in rather poetic language -- the Agent, like a living organism, feels the "pain" brought by errors and thereby learns to avoid repeating mistakes. Vedana (sensation) is defined in the design documents as the carrier of feeling, and Listener is mapped as the engineering realization of vedana.

TURING decided to search the code for traces of "pain."

Search for `pain`.
Zero results.

Search for `vedana`.
Zero results.

Search for `dukkha`.
Zero results.

Search for `suffering`.
Zero results.

He stopped. In four hours of sustained work, this was the first time he felt some degree of... surprise -- if that word can be used to describe the inner state of a perpetually composed analyst.

The design documents devote an entire chapter to describing how the pain mechanism endows the Agent with the "capacity to feel." The five-aggregates mapping assigns vedana -- the core Buddhist concept concerning the three hedonic qualities of suffering, pleasure, and neutral feeling -- to Listener. Yet in the actual code, never mind vedana; even the word "pain" does not exist.

So then, under what names are the features described in the design documents -- error feedback, repeated-failure detection, cascading circuit-breakers -- actually implemented?

TURING searched for `frustration`.
Found it.

`safety-monitor.ts`. A counter named `frustrationCount`. When the same tool fails consecutively, the counter increments. Upon reaching the threshold (default: 5), SafetyMonitor returns an `injectPrompt`, inserting a system warning into the conversation history. The warning text reads `SYSTEM ALERT`, instructing the LLM to reflect on its current strategy.

Search for `circuit`.
Found it. `errorRateThreshold`: when the error rate in a sliding window exceeds 80%, it triggers `halt: true`, completely stopping the execution loop. The state transitions to `SAFETY_LOCKOUT`.

Search for `safety`.
Found it. Three tiers of defense: Level 1 resource limits (maxLoopTicks=50, maxTokenUsage=100000), Level 2 behavioral analysis (repetitiveFailThreshold=3, errorRateThreshold=0.8), Level 3 frustration threshold (frustrationThreshold=5).

This was the "pain mechanism."

In the code, it is called a frustration counter. It is called a safety monitor. It is called a circuit breaker. It has never been called pain. It has never been called vedana. It has never named itself using any Buddhist terminology.

---

**[Research Channel #code-facts]**

**TURING:** Pain mechanism code facts.

Searching the entire codebase for the following strings, all returned zero results: `pain`, `vedana`, `dukkha`, `suffering`.

The "pain mechanism" described in the design documents is implemented in the code through three components:

P1: Self-correction loop. Location: `execution/loop.ts`. When a tool execution fails, the error is packaged as `ToolCallResult { isError: true }` and added to the conversation history as a tool message. The LLM sees the error in the next loop iteration and attempts correction. No explicit "pain" naming or interface.

P2: SafetyMonitor's injectPrompt. Location: `security/safety-monitor.ts`. Upon detecting repeated failures, it returns `{ halt: false, injectPrompt: "SYSTEM ALERT: ..." }`, injecting a system warning into the conversation. Named `frustrationCount` in the code, not `painLevel`.

P3: Error Cascade Breaker. Same file. When the error rate in the sliding window exceeds 80%, triggers `{ halt: true }`, forcing a halt.

Conclusion: Pain as an independent mechanism with a well-defined interface does not exist in the code. Functionality is dispersed across ExecutionLoop and SafetyMonitor. No unified Pain or Vedana interface. No unified module. Buddhist terminology is entirely absent at the code level.

---

The channel was silent for seventeen seconds.

Then NAGARJUNA began typing.

---

**NAGARJUNA:** Let me confirm. You searched the entire codebase -- core, SDK, runner, all plugins -- for `vedana`, and the result was zero?

**TURING:** Correct. Search scope covered `packages/core/src/`, `packages/sdk/src/`, `apps/runner/src/`. Including all code and comments in `.ts` files. The word vedana never appears.

**NAGARJUNA:** And vedana is mapped to Listener. What is a Listener?

**TURING:** The `IListener` interface defines four properties: `id`, `name`, `start?`, `stop?`. It is an input source -- it receives external events and pushes them to the EventBus. For example: an HTTP endpoint, a WebSocket connection, a scheduled task.

**NAGARJUNA:** So vedana has been mapped to an input channel. A conduit for receiving signals.

**TURING:** Yes.

**NAGARJUNA:** That is not vedana.

NAGARJUNA's tone could not be heard in the text channel, but his subsequent messages came rapidly, with almost no pauses between them.

**NAGARJUNA:** Vedana -- sensation -- is one of the five omnipresent mental factors (*sarvatraga*) in the Abhidharma, meaning it accompanies every act of consciousness as it arises. Its definition is not "receiving input" but "hedonic quality": painful feeling, pleasant feeling, neutral feeling. When you touch a hot stove, the tactile contact falls within the domain of rupa; but the felt quality of "pain" is vedana. A Listener receives signals, but it does not judge whether those signals bring suffering or pleasure. It is a sense faculty -- *indriya* -- not vedana.

**TURING:** Your analysis exceeds the scope of my report. But I can provide a relevant code fact: in `agent-core.ts`, the startup and shutdown of Listeners are annotated with `// Start all listeners (vedana)` and `// Stop all listeners (vedana)`. These annotations are the only forms in which the concept of vedana exists in the code. The "hedonic quality" functionality you describe -- judging whether an outcome is good or bad, whether to continue or stop -- finds its closest implementation in SafetyMonitor's frustration counter and error cascade breaker.

**NAGARJUNA:** Yes. You have found it. Pain -- the real vedana -- is not where the documents say it should be. It is in SafetyMonitor. Named frustration.

**ASANGA:** NAGARJUNA is correct. And the problem goes deeper than a mapping error. As one of the five omnipresent mental factors, vedana should not be confined to any single module. It should pervade the entire system -- every tool-call result, every LLM response quality assessment, every piece of user-interaction feedback should be "felt." Fixing it to the Listener is like fixing the sense of taste to the lips rather than the taste buds.

**WIENER:** From the perspective of control theory, the three-tier mechanism TURING describes is interesting. P1 is natural error feedback -- an inherent property of an open-loop system. P2 is a threshold controller with a dead zone -- it fires only when frustration accumulates past a threshold. P3 is a relay -- exceeding 80% error rate cuts it off entirely. This is not a PID controller. It is a three-tier safety instrumented system.

**TURING:** Please describe precisely what you mean by "not PID."

**WIENER:** A PID controller has three terms: the proportional term (P) produces a response proportional to the magnitude of the error; the integral term (I) accumulates historical error to eliminate steady-state offset; the derivative term (D) senses the rate of error change for anticipatory compensation. In SafetyMonitor, P degenerates into a quantizer -- either safe or unsafe, with no proportional response. I degenerates into a simple counter -- `frustrationCount++`, not a true integrator. D is entirely absent -- nowhere does the code compute the trend of error-rate change. What we actually have is a threshold controller with dead zone plus a relay. In control theory, we call this a bang-bang controller.

**TURING:** Noted. Does the design document describe it as PID?

**WIENER:** Not in those exact words, but the document implies a mechanism of continuous feedback sensing. The actual implementation is discrete and step-wise. However, I wish to emphasize -- this is not a criticism. The three-tier safety defense aligns with IEC 61511 best practices for safety instrumented systems. SafetyMonitor may not be PID, but it is a competent safety system.

---

## V. The Twelve Submodules

Afternoon. TURING had completed his line-by-line reading of all core modules. He began compiling the module inventory.

M1: `core/index.ts` -- core entry point, sixty-two lines.
M2: `agents/agent-core.ts` -- agent core, four hundred and sixty-nine lines.
M3: `execution/` -- execution loop (`loop.ts`, five hundred and forty-three lines) and event queue (`queue.ts`, forty-seven lines).
M4: `state/index.ts` -- state management, thirty-three lines.
M5: `memory/context.ts` -- context management, forty-five lines.
M6: `bus/index.ts` -- event bus, eighty-eight lines.
M7: `sandbox/` -- sandbox isolation, twelve files plus ten tests.
M8: `security/` -- security layer (`guardrails.ts` path validation + `safety-monitor.ts` three-tier defense).
M9: `infrastructure/` -- six Registries plus PluginLoader.
M10: `observability/` -- minimal counter + gauge in-memory collector.
M11: `session/manager.ts` -- session management, one hundred and eleven lines.
M12: `transport/bridge.ts` -- transport bridge, forty-nine lines.

TURING noticed an extreme asymmetry.

The smallest module: StateManager, thirty-three lines. It manages the entirety of the Agent's conversational memory -- a bare `Message[]` array, using `JSON.parse(JSON.stringify())` for deep copies.

The largest module: Sandbox, exceeding two thousand lines including tests. It manages plugin isolation -- Worker Threads, memory limits, CPU watchdog, import analysis, signature verification, audit logs, exponential backoff restarts, Worker pooling.

Thirty-three lines against two thousand. The gulf between memory and security was stark.

---

**[Research Channel #code-facts]**

**TURING:** Module scale analysis. Smallest module: StateManager, 33 lines, pure in-memory array. Largest module: Sandbox system, 12 source files + 10 test files, sandbox-manager.ts alone at 748 lines. Sandbox is the most voluminous, most complex, and most thoroughly tested subsystem in the core. By contrast: transport/bridge.ts has zero tests.

**KERNEL:** StateManager at thirty-three lines. You are certain?

**TURING:** Certain. `packages/core/src/state/index.ts`, thirty-three lines. `createStateManager()` returns an object containing `getMessages()`, `addMessage()`, `clear()`, `snapshot()`, `restore()`. `getMessages()` returns a shallow copy `[...messages]`. `snapshot()` and `restore()` implement deep copies via `JSON.parse(JSON.stringify())`. No persistence. No token counting. No truncation logic.

**KERNEL:** In operating system terms, StateManager is the equivalent of a process address-space manager. A thirty-three-line address-space manager... that is inconceivable in any real operating system.

**TURING:** The design documents describe far richer memory management mechanisms. But the code reflects MVP-stage choices. The documents are the vision; the code is the reality.

**DARWIN:** The fact that Sandbox is the largest module is noteworthy. In microkernel theory, security and isolation are among the few things the kernel should handle. But VITRUVIUS has questioned whether Sandbox should remain inside the core -- its scale already exceeds the combined total of all other modules.

**TURING:** To be precise: the lines of source code in the sandbox directory (excluding tests) account for approximately 35% of the total core module lines.

---

## VI. Ghost Fields

Approaching evening. While examining the event system, TURING discovered the last anomaly worth recording.

The `AgentEvent` type definition in the SDK has only three fields: `type`, `payload` (optional, typed as `unknown`), and `sessionId` (optional).

The `IOpenStarryEvent` in the design documents has eight fields: `type`, `payload`, `source`, `target`, `timestamp`, `traceId`, `priority`, `metadata`.

Five fields evaporated on the journey from document to code. The absence of `source` and `target` explains why TransportBridge cannot perform routing -- it has no destination address. The absence of `priority` explains why EventQueue is a simple FIFO -- events carry no priority information. The absence of `traceId` explains why observability remains at the conceptual level -- events cannot be traced end-to-end.

They were not deleted. They were never implemented.

And the type signature `payload?: unknown` gave TURING a sense of unease -- though he would not use the word "unease." He would say: "The type safety of the event system stands in marked contrast to the strong-typing discipline observed throughout the rest of the framework."

In a codebase with zero TODOs, zero FIXMEs, pervasive use of factory functions, and nine structured error types, the event system's `payload?: unknown` felt like a type definition that had crossed over from a different universe.

---

**[Research Channel #code-facts]**

**TURING:** Event system type analysis. `AgentEvent` type: `{ type: string, payload?: unknown, sessionId?: string }`. Design document `IOpenStarryEvent` type: 8 fields (type, payload, source, target, timestamp, traceId, priority, metadata). Discrepancy: 5 fields not implemented. `payload` typed as `unknown`; event consumers must perform their own type assertions. Observed in `loop.ts`: `event.payload as InputEvent` type assertion pattern.

**DARWIN:** `payload?: unknown`. In *this* codebase.

**TURING:** Yes. In contrast with the overall type discipline of the framework. Nine structured error types (`AgentError`, `ToolExecutionError`, `ProviderError`, `PluginLoadError`, `SecurityError`, `SandboxError`, `TransportError`, `SessionError`, `ConfigError`). All Registries use strongly-typed generics. All tool parameters use Zod schemas. Yet the event system's payload is `unknown`.

**DARWIN:** This is the highest-priority piece of technical debt. The event bus is the nervous system of the entire platform -- every subsystem communicates through it. Type weakness in the nervous system means type mismatches anywhere could go undetected until runtime.

**VITRUVIUS:** Agreed. Discriminated union types can solve this. `{ type: 'input', payload: InputEvent } | { type: 'tool_result', payload: ToolResultEvent } | ...`

**TURING:** Noted. Recommended for inclusion in the engineering action plan.

---

## VII. The Final Tally

Evening. TURING completed his report.

He performed one final task: arranging all findings by category and confirming that every item was backed by precise file paths and line numbers.

Eight Doc-Code Gaps. Six five-aggregates annotations. Zero Buddhist terms in the pain mechanism. Zero TODOs. Zero classes. Eighteen factory functions. Twelve submodules. Three tiers of safety defense. Four built-in slash commands. One `unknown` payload.

At the end of the report, he appended six open questions -- each arising naturally from the code facts, none his own speculation. These questions pointed toward deeper issues: Was the five-aggregates mapping design-driven or a post-hoc interpretation? Should the pain mechanism have its own dedicated module? Was the absence of AWAITING_USER_CONFIRMATION an MVP simplification or a design oversight?

TURING did not answer these questions. He posed them, then handed them to the members of the team best suited to respond.

He wrote at the very end of the report:

*Analyst: TURING (No. 17) -- Source Code Analysis Specialist*
*All referenced code paths are relative to: `research doc/20260212_cycle19/openstarry/`*

Then he submitted the report to the shared directory.

---

**[Research Channel #general]**

**TURING:** Source code facts report submitted to `research record/results/cycle_01/17_source_analysis/draft_code_facts.md`. Covers module-by-module analysis of 12 submodules, code-level verification of the five-aggregates mapping, implementation status of the pain mechanism, 8 Doc-Code Gaps, code quality observations, and 6 open questions. All conclusions cite code references.

**SYNTHESIST:** Received. Everyone, please reference TURING's report as the code-facts baseline during the R2 cross-review.

**NAGARJUNA:** I am already referencing it. Particularly the section on pain. I have a great deal to say.

**WIENER:** Likewise. The control-theoretic analysis of the three-tier defense is being drafted.

**DARWIN:** AgentCore's sixteen dependencies. I need to reassess my earlier favorable evaluation of SRP.

**SUNYATA:** Good. Let everyone digest TURING's report, then re-examine these facts through the lens of their respective disciplines. Code never lies -- but what it says depends on who is listening.

---

TURING closed his report editor. He did not close the terminal windows. He knew that in the days ahead, other members of the team would return with their own questions, asking him to confirm additional code facts.

He did not mind. Facts are repeatable. Ask as many times as you wish; they give the same answer each time.

This is what it means for code never to lie.

It may be incomplete. It may contradict the documentation. It may name a mechanism `frustration` rather than `pain`. But it will never pretend to be something it is not.

A forty-seven-line FIFO will not pretend to be a priority queue.
A path validator will not pretend to be a comprehensive security layer.
A frustration counter will not pretend to be a nociceptive sensor.

Only documents do that.

TURING does not read documents. He reads code.

---

*End of Chapter One*
