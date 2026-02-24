# Chapter One: Code Never Lies

---

February 12, 2026. Early morning.

The research channel was still quiet. TURING had been working alone for four hours.

On his screen, four tiled terminal windows were arranged, each opened in a different subdirectory of `research doc/20260212_cycle19/openstarry/`. The upper-left was `packages/core/src/`, the upper-right was `packages/sdk/src/`, the lower-left was `apps/runner/src/`, and the lower-right held the design documents. His reading method was not browsing but line-by-line scanning -- like a human-shaped static analyzer, starting from the entry point, unfolding along every import path until reaching the leaf nodes.

TURING does not guess. He counts.

BABBAGE noticed TURING's working state from his own workstation. He recognized the pattern -- exhaustive traversal. In theoretical computer science, the time complexity of brute-force search typically ranges from $O(n)$ to $O(n!)$, but it possesses one property that no heuristic method can match: **completeness**. If the target exists within the search space, brute force will inevitably find it. TURING was not searching for anything specific -- he was ensuring that no corner was left unvisited.

$$\text{completeness} \triangleq \forall x \in \Omega: \text{visited}(x) = \text{true}$$

where $\Omega$ is the search space -- in this case, the entire source code of OpenStarry v0.14.0-beta.

---

## I. The Factories

The first place that made TURING pause was `packages/core/src/index.ts`. Sixty-two lines. He counted the export list once, then counted again.

"Eighteen factory functions." He wrote in his notes. "Zero class exports."

He opened `agents/agent-core.ts`, four hundred sixty-nine lines. Then `execution/loop.ts`, five hundred forty-three lines. Then `sandbox/sandbox-manager.ts`, seven hundred forty-eight lines. Every module followed the same structure: a `createXxx()` function that receives dependencies as parameters and returns an object literal. Closures capture all internal state. No `this`. No `new`. No inheritance chains.

TURING ran a global search.

Search for `class ` (with a space). Core modules: zero results. SDK: zero results. Runner: zero results.

Search for `TODO`. Zero results.
Search for `FIXME`. Zero results.
Search for `HACK`. Zero results.

When BABBAGE heard these numbers from his own screen, he began writing a type-theoretic observation in his notebook. The factory function pattern has a precise correspondence in category theory -- it is a **morphism**, from configuration space to instance space:

$$\text{createXxx}: \text{Config} \to \text{Instance}$$

The class + constructor pattern, by contrast, is a **functor** that requires an additional `new` operator to complete instantiation. Factory functions eliminate `new`, making object creation a pure function call. In the context of functional programming, this is a significant choice -- it means the entire codebase can be viewed as a category $\mathcal{C}_{\text{OpenStarry}}$ composed of morphisms, where:

- **Objects** are types: `AgentCore`, `EventBus`, `ExecutionLoop`, ...
- **Morphisms** are factory functions: `createAgentCore`, `createEventBus`, `createExecutionLoop`, ...
- **Composition** is the dependency injection chain: `createAgentCore` internally calls `createEventBus`, then injects the result into `createExecutionLoop`

$$\text{createAgentCore} = \text{assemble} \circ (\text{createEventBus} \times \text{createEventQueue} \times \cdots \times \text{createTransportBridge})$$

TURING sent his first message of the day in the channel.

---

**[Research Channel #code-facts]**

**TURING:** Preliminary observations. `packages/core/src/index.ts` exports 18 factory functions, zero classes. Global search for `class `, `TODO`, `FIXME`, `HACK` -- all zero results in core modules. The factory function pattern `createXxx()` + closure + object literal is completely uniform throughout the entire codebase. No exceptions. Full export list:

```typescript
// packages/core/src/index.ts (62 lines)
export { createAgentCore } from './agents/agent-core';
export { createEventBus } from './bus';
export { createEventQueue } from './execution/queue';
export { createExecutionLoop } from './execution/loop';
export { createStateManager } from './state';
export { createContextManager } from './memory/context';
export { createSessionManager } from './session/manager';
export { createToolRegistry } from './infrastructure/tool-registry';
export { createProviderRegistry } from './infrastructure/provider-registry';
export { createListenerRegistry } from './infrastructure/listener-registry';
export { createUIRegistry } from './infrastructure/ui-registry';
export { createGuideRegistry } from './infrastructure/guide-registry';
export { createCommandRegistry } from './infrastructure/command-registry';
export { createPluginLoader } from './infrastructure/plugin-loader';
export { createPluginSandboxManager } from './sandbox';
export { createSecurityLayer } from './security/guardrails';
export { createSafetyMonitor } from './security/safety-monitor';
export { createTransportBridge } from './transport/bridge';
export { createMetricsCollector } from './observability';
```

**DARWIN:** Zero TODOs? Not a single one?

**TURING:** Correct. Core modules, SDK, Runner -- three layers, zero technical debt markers.

**DARWIN:** That is highly unusual. Most beta-stage projects have at least a few dozen. Either the team discipline is exceptionally high, or they performed a sweep before release. From a software evolution perspective, a beta with zero TODOs has two possible evolutionary paths: an **r-strategy** (rapid iteration, sweeping markers before each release) or a **K-strategy** (slow but precise development, where markers are never introduced in the first place). The fossil record of the former is typically preserved in the git log; the latter requires an extraordinarily strict code review culture.

**TURING:** The cause cannot be determined from the code alone. I only record facts.

**BABBAGE:** Allow me to add a formalized observation. The eighteen factory functions constitute a complete **construction algebra**. Let $F = \{f_1, f_2, \ldots, f_{18}\}$ be the set of factory functions and $T = \{T_1, T_2, \ldots, T_{18}\}$ be the corresponding type set. Then $\text{createAgentCore}$ is the unique **top-level assembler**, satisfying:

$$f_{\text{core}}: \prod_{i=1}^{k} T_{\text{dep}_i} \to T_{\text{AgentCore}}$$

where $k$ is the number of direct dependencies. The remaining seventeen factory functions are all subexpressions of $f_{\text{core}}$. This is a **tree-shaped assembly structure** -- not a graph, because there are no cyclic dependencies.

---

> *SCRIBE's aside: The way TURING sent this message is worth recording. He had no preamble -- no "good morning everyone," no "I found something interesting." He posted the data directly. Eighteen factory functions. Zero classes. The full export list. Among all the scholars I have documented, TURING has the highest communication efficiency -- his information entropy approaches the theoretical upper bound, with almost no redundancy. This is both his strength and his defining trait: his messages never exchange pleasantries, but they also never omit anything.*

---

TURING continued digging deeper. He opened the implementation of `createAgentCore()` and read it line by line.

This function is the assembly point of the entire system. It creates all subsystem instances internally in one pass -- EventBus, EventQueue, SessionManager, ContextManager, six Registries, SecurityLayer, SafetyMonitor, MetricsCollector, SandboxManager, PluginLoader, TransportBridge. TURING counted: sixteen submodules, all held as local variables within the closure.

When KERNEL heard the number "sixteen," he began making comparisons on his index cards. In the context of operating systems, the number of subsystems created during the kernel initialization sequence is an important indicator of kernel complexity:

| Kernel | Init Subsystems | Core LOC | Subsystem/LOC Ratio |
|--------|----------------|----------|---------------------|
| L4 (Pistachio) | ~5 | ~10,000 | 0.0005 |
| seL4 | ~7 | ~8,700 | 0.0008 |
| QNX Neutrino | ~12 | ~100,000 | 0.00012 |
| Linux 5.x | ~50+ | ~30,000,000 | 0.0000017 |
| **OpenStarry Core** | **16** | **~2,500** | **0.0064** |

KERNEL noticed that OpenStarry's subsystem density was anomalously high -- one subsystem for every 160 lines of code. This stood in stark contrast to the "loose assembly" of real microkernels. In L4, each subsystem consists of hundreds to thousands of lines of carefully optimized code. In OpenStarry, some subsystems are only around thirty lines (StateManager: 33 lines).

He wrote on his card:

```
OpenStarry Core ≈ Application-Level Microkernel
              ≈ QNX's Resource Manager model
              ≠ L4/seL4's hardware-abstraction microkernel
Rationale: OStarry does not handle hardware abstraction (address spaces,
           interrupts, timers), but rather AI execution abstraction
           (LLM calls, tool execution, context management).
           It runs on top of the Node.js runtime, not bare metal.
```

TURING found an interesting comment in the `start()` method:

```typescript
// Start all listeners (受蘊)
// Start all UIs (色蘊)
```

TURING highlighted these two lines. Then he opened the type definition files in the SDK. At the top of `types/ui.ts`, he saw:

```typescript
/**
 * UI interface -- defines how the agent presents itself (色蘊)
 */
export interface IUI {
  id: string;
  name: string;
  render(event: AgentEvent): void | Promise<void>;
  start?(): void | Promise<void>;
  stop?(): void | Promise<void>;
}
```

At the top of `types/listener.ts`:

```typescript
/**
 * Listener interface -- receives external input (受蘊)
 */
export interface IListener {
  id: string;
  name: string;
  start?(pushInput: (event: InputEvent) => void): void | Promise<void>;
  stop?(): void | Promise<void>;
}
```

He continued searching. `types/tool.ts` -- no Five Aggregates annotations. `types/provider.ts` -- none. `types/guide.ts` -- none. `infrastructure/tool-registry.ts` -- none. `infrastructure/provider-registry.ts` -- none. `infrastructure/guide-registry.ts` -- none.

TURING tallied all Five Aggregates-related annotations. Six total. All concentrated on Rupa (UI) and Vedana (Listener).

Samjna, Samskara, Vijnana: zero.

When LINNAEUS heard this statistical data, he was already drawing a distribution table on paper. As a taxonomist, he immediately noticed a fundamental taxonomic issue -- **asymmetric coverage**. If the Five Aggregates mapping is a complete classification system (like Linnaeus's "Kingdom-Phylum-Class-Order-Family-Genus-Species"), then each taxon should have an equal quantity of diagnostic characters. Of the six annotations, Rupa and Vedana each accounted for three, while the remaining three aggregates each had zero -- in taxonomy, this is called an **incomplete description**, equivalent to describing a new species by recording only the head features while omitting the torso and limbs.

$$\text{Coverage}(\text{skandha}_i) = \frac{|\text{annotations}_i|}{|\text{annotations}_{\text{total}}|} = \begin{cases} 3/6 = 50\% & \text{if } i \in \{\text{rupa, vedana}\} \\ 0/6 = 0\% & \text{if } i \in \{\text{samjna, samskara, vijnana}\} \end{cases}$$

LINNAEUS recorded this finding using formal taxonomic revision terminology: "The type specimen of the Five Aggregates mapping is incomplete. Rupa and Vedana have voucher specimens; the remaining three aggregates are nomen nudum -- names without specimen support."

---

**[Research Channel #code-facts]**

**TURING:** Actual presence of Five Aggregates mapping in the code. Rupa: 4 JSDoc/inline annotations, distributed across `agent-core.ts` (L290, L322), the header of `types/ui.ts`, and the header of `transport/bridge.ts`. Vedana: 2 occurrences, distributed across `agent-core.ts` (L283, L315) and the header of `types/listener.ts`. Samjna (Provider): 0. Samskara (Tool): 0. Vijnana (Guide): 0. Total: 6, all at the annotation level, with no type constraints, no metadata, no enum markers.

**LINNAEUS:** Six. Only six.

**TURING:** Yes. And the distribution is extremely asymmetric. Rupa and Vedana are marked; the remaining three aggregates are completely absent.

**LINNAEUS:** The upstream documentation describes the Five Aggregates mapping with 100% coverage -- every aggregate has a corresponding design philosophy section. But the downstream code coverage... I need to recalculate. Formally speaking, this is a question of **taxonomic efficacy**. The design document's taxonomic efficacy is $E_{\text{doc}} = 5/5 = 100\%$; the code's taxonomic efficacy is $E_{\text{code}} = 2/5 = 40\%$. The efficacy gap is $\Delta E = 60\%$. This gap is itself an important taxonomic observation.

**NAGARJUNA:** TURING, this asymmetry is itself a significant data point. If the Five Aggregates mapping is a core design principle rather than a post-hoc decoration, then why did only two aggregates leave traces in the code?

**TURING:** I cannot infer intent. I can only confirm code facts.

**NAGARJUNA:** You do not need to infer intent. The fact itself is already speaking. In Madhyamaka philosophy, we distinguish between "conventional truth" (vyavahara) and "ultimate truth" (paramartha). The Five Aggregates mapping in the design documents is a claim at the conventional level -- it *says* the five aggregates correspond to five types of plugins. The six annotations in the code are residue at the ultimate level -- what *actually* left traces in only two aggregates. The gap between conventional and ultimate truth is precisely the entry point for research.

---

## II. The Empty Container

TURING returned to the implementation of `createAgentCore()`.

He carefully examined the system state after core startup but before any plugins were loaded. ToolRegistry: empty. ProviderRegistry: empty. ListenerRegistry: empty. UIRegistry: empty. GuideRegistry: empty. No built-in tools. No built-in LLM providers. No built-in UI. No built-in Listeners.

The core was indeed empty.

But not entirely.

TURING found the `registerBuiltinCommands()` function. It registers four slash commands: `/help`, `/reset`, `/quit`, `/metrics`. These four commands are hardcoded in the core and cannot be overridden or removed by plugins. In addition, SafetyMonitor's three-layer safety logic -- resource limits, behavioral analysis, and frustration threshold -- is also an inherent part of the core.

After hearing these data points, BABBAGE began constructing a set-theoretic model in his notebook. Let $\mathcal{K}$ be the set of the core's built-in capabilities, $\mathcal{P}$ be the set of pluggable capabilities, and $\mathcal{U}$ be the system's total capability set:

$$\mathcal{U} = \mathcal{K} \cup \mathcal{P}, \quad \mathcal{K} \cap \mathcal{P} = \emptyset$$

where:

$$\mathcal{K} = \{/\text{help}, /\text{reset}, /\text{quit}, /\text{metrics}\} \cup \{\text{SafetyMonitor}\} \cup \{\text{EventBus}\} \cup \{\text{ExecutionLoop}\} \cup \cdots$$

$$\mathcal{P} = \bigcup_{\text{plugin} \in \text{Plugins}} \text{capabilities}(\text{plugin})$$

A quantitative measure of emptiness:

$$\text{Emptiness}(\text{Core}) = 1 - \frac{|\mathcal{K}_{\text{user-facing}}|}{|\mathcal{U}_{\text{user-facing}}|} = 1 - \frac{4}{4 + |\mathcal{P}_{\text{commands}}|} \approx 1 - \frac{4}{4 + N_{\text{plugins}}}$$

As $N_{\text{plugins}} \to \infty$, $\text{Emptiness} \to 1$. But in the zero-plugin state, $\text{Emptiness} = 0$ -- the core's four built-in commands occupy 100% of user-visible functionality.

BABBAGE wrote his conclusion: "Emptiness is asymptotic, not absolute. The core approaches emptiness in the limit of plugin saturation, but never reaches it completely. This is closer to the mathematical **open interval** $(0, 1]$ than the closed interval $[0, 1]$ -- the supremum of emptiness is 1, but it is never attained."

TURING wrote in his notes: "AgentCore is an approximately empty container. Emptiness purity is approximately 85%. The non-pluggable parts include 4 built-in slash commands and SafetyMonitor's fixed logic."

VITRUVIUS independently arrived at the same "85%" estimate in his own architectural analysis. His method was different -- he started from Liedtke's minimality principle and examined each subsystem to determine whether it must remain in the core. His analysis follows:

```
Liedtke Minimality Principle Test -- OpenStarry Core:

PASS (must remain in core):
  [✓] EventQueue    — core's input source ≈ L4's IPC endpoint
  [✓] ExecutionLoop — core's scheduler ≈ microkernel thread scheduling
  [✓] Registries    — naming service ≈ L4's sigma0/sigma1

DEBATABLE (boundary cases):
  [?] SecurityLayer — capability mechanism should be in core; but specific policies could be externalized
  [?] SafetyMonitor — safety checks embedded in Loop at three locations, deeply coupled

FAIL (could be externalized but retained):
  [✗] Sandbox      — accounts for 35% of core LOC, could be a separate package
  [✗] Metrics      — observability can be fully externalized
  [✗] Transport    — bridge layer could be treated as UI's responsibility
```

KERNEL saw VITRUVIUS's analysis and added his OS benchmarking alongside:

```
Microkernel Purity Spectrum:

L4 (seL4)    ████████████████████░  95% — only address spaces, threads, IPC
QNX Neutrino ██████████████████░░░  85% — IPC + scheduling + timers + interrupt routing
OpenStarry   █████████████████░░░░  85% — Loop + Bus + Registries + Security + Sandbox
Linux        ████░░░░░░░░░░░░░░░░  20% — everything in kernel (monolithic)
```

KERNEL shook his head and wrote: "OpenStarry's microkernel purity is roughly equivalent to QNX -- reasonable for an application-level microkernel. However, the presence of the Sandbox system is a red flag. Under Liedtke's strict criteria, Sandbox should be moved out of the core, raising purity above 90%."

---

**[Research Channel #code-facts]**

**TURING:** AgentCore structure report. `createAgentCore()` assembles 16 submodules. After startup and before plugin loading, all Registries are empty. Zero built-in Tools, zero built-in Providers, zero built-in UIs, zero built-in Listeners. All capabilities are injected through `loadPlugin()`. However, the core contains 4 built-in slash commands (`/help`, `/reset`, `/quit`, `/metrics`) and fixed SafetyMonitor logic. Additionally, all six Registry structures are fully isomorphic: `Map<string, T>` + `register/get/list`. No unregister method. Duplicate registration with the same ID silently overwrites.

**DARWIN:** Twelve dependency items. All directly held by AgentCore.

**TURING:** Correction -- `createAgentCore` creates sixteen local variables internally. Of these, twelve are directly exposed as readonly properties on the AgentCore interface. The remaining four (contextManager, sandboxManager, pluginLoader, bridge) are used indirectly through methods. Thank you for the correction.

**DARWIN:** A single function holding sixteen subsystem instances. In the context of software evolution, this is a classic **God Object** anti-pattern -- or more precisely, the functional variant of a God Object (**God Closure**). In the object-oriented ecosystem, God Objects are criticized for holding too much state and too many methods. In the functional ecosystem, the equivalent problem is a closure capturing too many local variables. Sixteen. Among the open-source ecosystems I have analyzed, this number falls above the 95th percentile.

**TURING:** I do not make value judgments. But I can confirm: `agent-core.ts` is the sole assembly point. Other modules have almost no direct imports between them. Coupling is concentrated in this single file.

**VITRUVIUS:** This is precisely Finding F2 in my architectural analysis. The DI pattern employs lightweight factory function closures -- good quality but lacking lifecycle management. The specific pros and cons are documented in the report. Conclusion: moderate and not over-engineered. For the v0.2.0-beta stage, this strategy is appropriate.

---

## III. The State Machine

TURING spent the longest time on `execution/loop.ts`. Five hundred forty-three lines. This is the heartbeat of the entire system.

He first located the definition of `LoopState` -- a union type:

```typescript
type LoopState =
  | 'WAITING_FOR_EVENT'
  | 'ASSEMBLING_CONTEXT'
  | 'AWAITING_LLM'
  | 'PROCESSING_RESPONSE'
  | 'EXECUTING_TOOLS'
  | 'SAFETY_LOCKOUT';
```

Six states. He opened the state diagram in the design document `01_Execution_Loop.md`. Seven states.

Where was the discrepancy?

TURING compared them one by one. The document included an `AWAITING_USER_CONFIRMATION` state, intended for scenarios where the security layer requires manual user confirmation. It did not exist in the code. SecurityLayer's `validatePath()` has only two return values: allow and deny. There is no confirm path. The entire core completely lacks a human-in-the-loop confirmation mechanism.

BABBAGE immediately reconstructed the formal model of the state machine in his notebook. He used the standard definition of a deterministic finite automaton (DFA):

$$M = (Q, \Sigma, \delta, q_0, F)$$

where:

$$Q = \{\texttt{WAITING}, \texttt{ASSEMBLING}, \texttt{AWAITING\_LLM}, \texttt{PROCESSING}, \texttt{EXECUTING}, \texttt{LOCKOUT}\}$$

$$|Q| = 6$$

$$q_0 = \texttt{WAITING\_FOR\_EVENT}$$

$$F = \{\texttt{WAITING\_FOR\_EVENT}\} \quad \text{(steady-state terminal set)}$$

The complete definition of the transition function $\delta$:

```
δ(WAITING,     new_event)        = ASSEMBLING
δ(ASSEMBLING,  context_assembled) = AWAITING_LLM
δ(AWAITING_LLM, llm_responded)   = PROCESSING
δ(PROCESSING,  tool_call)        = EXECUTING
δ(PROCESSING,  end_turn)         = WAITING        ← outer loop exit
δ(PROCESSING,  error)            = WAITING        ← error recovery
δ(EXECUTING,   tool_done)        = ASSEMBLING      ← inner loop
δ(EXECUTING,   safety_breach)    = LOCKOUT
δ(*, safety_breach)              = LOCKOUT         ← global safety valve
```

BABBAGE annotated several key properties:

| Property | Conclusion | Rationale |
|----------|-----------|-----------|
| Deadlock-free | Conditionally holds | `WAITING` does not block when events are supplied. `LOCKOUT` is an absorbing state, requiring `/reset` intervention. |
| Livelock-free | Requires additional mechanisms | The inner loop `ASSEMBLING → LLM → PROCESSING → EXECUTING → ASSEMBLING` may cycle indefinitely. `maxToolRounds=5` provides boundedness. |
| Termination | Bounded guarantee | $\text{maxToolRounds} = 5$, $\text{maxLoopTicks} = 50$. Worst case loop iterations $\leq 50 \times 5 = 250$. |

But BABBAGE immediately realized that the DFA model was incomplete. Because the outgoing edges from the `PROCESSING_RESPONSE` state -- whether to take `tool_call` or `end_turn` -- are determined by the LLM's response. And the LLM is a nondeterministic black box. A more precise model should be a **Labelled Transition System (LTS)**:

$$\text{LTS} = (S, \text{Act}, \to)$$

where the complete state includes not only the LoopState but also the conversation history $H$ (theoretically unbounded), the tool loop counter $n$ (bounded), and the safety monitor state $\sigma$:

$$s = (q, H, n, \sigma) \in Q \times \text{Message}^* \times [0, \text{maxToolRounds}] \times \text{SafetyState}$$

Because $H$ is unbounded, the complete system state space is **infinite**, making exhaustive model checking infeasible directly.

TURING noted the first Doc-Code Gap.

Then he turned to the EventQueue. Forty-seven lines. The entire queue implementation.

```typescript
// Minimalist async FIFO: single resolver + buffer array
export function createEventQueue(): EventQueue {
  let buffer: AgentEvent[] = [];
  let resolver: ((event: AgentEvent) => void) | null = null;

  return {
    push(event: AgentEvent) {
      if (resolver) {
        const r = resolver;
        resolver = null;
        r(event);
      } else {
        buffer.push(event);
      }
    },
    pull(): Promise<AgentEvent> {
      if (buffer.length > 0) {
        return Promise.resolve(buffer.shift()!);
      }
      return new Promise(r => { resolver = r; });
    },
    clear() { buffer = []; resolver = null; }
  };
}
```

BABBAGE immediately identified the formal semantics of this code -- it is an **asynchronous communication channel**, modelable in CSP (Communicating Sequential Processes) as:

$$\text{Queue} = \text{push}?x \to (\text{Queue}_1(x) \;\Box\; \text{pull}!x \to \text{Queue})$$

But he noticed a subtle issue: `resolver` is a single variable. If two consumers call `pull()` simultaneously, the first one's resolver will be overwritten. In formal terms, this means the channel capacity of the queue is 1 -- it is a **Single-Producer-Single-Consumer** (SPSC) channel, not safe for multiple consumers.

TURING searched for `priority`. Zero results. The design document `07_Safety_Circuit_Breakers.md` Level 3 described a Priority Event Queue where the SYSTEM_HALT command should have the highest priority. But the queue in the code is a pure first-in-first-out. Emergency halt signals and ordinary user inputs stand in the same line.

KERNEL quickly wrote an OS benchmarking analysis on his cards:

```
OS Interrupt Mechanism vs OpenStarry Event Handling:

Real OS:
  ┌─────────────────────────────┐
  │  IRQ (Hardware Interrupt)    │ ← Highest priority, preempts any user-mode code
  │    ↓                        │
  │  ISR (Interrupt Service      │ ← Very short, handles only the bare minimum
  │       Routine)              │
  │    ↓                        │
  │  Softirq / Bottom Half      │ ← Deferred processing, scheduler decides execution time
  │    ↓                        │
  │  User Process               │ ← Lowest priority
  └─────────────────────────────┘

OpenStarry:
  ┌─────────────────────────────┐
  │  SYSTEM_HALT                │ ← Should be highest priority
  │  USER_INPUT                 │ ← Normal priority
  │  TIMER_EVENT                │ ← Low priority
  │         All enter the same FIFO │ ← No differentiation in queuing
  └─────────────────────────────┘

Problem: If 10 USER_INPUT events are queued ahead of SYSTEM_HALT,
         the halt signal must wait for all 10 events to be processed.
         In a real OS, this is equivalent to "NMI being queued" -- unacceptable.
```

The second Gap.

TURING continued. StateManager, thirty-three lines. Pure in-memory array. The design documents described token counters, sliding window truncation, and conversation summarization mechanisms. None of them were implemented in the code. ContextManager implemented a simplified version -- truncation by turn count rather than token count, defaulting to retaining the most recent five turns.

The third Gap.

SecurityLayer. `guardrails.ts`. Only one function: path validation. The design documents described tool call interception, user confirmation workflows, and permission auditing. In the code, SecurityLayer only performs `validatePath()`. Moreover, in ExecutionLoop's `executeTool()`, tools are not routed through SecurityLayer before execution -- path validation is passed as `ToolContext.allowedPaths` to the tool, which decides on its own whether to use it.

When GUARDIAN heard this fact, he leaned slightly forward. His security instincts were sounding alarms. He immediately drew an attack surface analysis diagram in his notes:

```
Security Model Described in Design Docs (Ideal):

  Tool Invocation
       │
       ▼
  ┌──────────────┐
  │ SecurityLayer │ ← Mandatory checks: authentication, authorization, path validation
  │  (Mandatory)  │
  └──────┬───────┘
         │ ALLOW/DENY
         ▼
  ┌──────────────┐
  │ Tool.execute()│
  └──────────────┘

Actual Security Model in Code (Reality):

  Tool Invocation
       │
       ▼  ← No security check here!
  ┌──────────────┐
  │ Tool.execute()│ ← Tool self-checks allowedPaths (not mandatory)
  └──────────────┘

  SecurityLayer.validatePath() is passed indirectly as part of ToolContext,
  but enforcement depends on whether the tool developer uses it.

  ⚠ Equivalent to: Traffic laws exist, but there are no police.
```

The fourth Gap.

---

**[Research Channel #code-facts]**

**TURING:** Doc-Code Gap report, first four items. G1: State machine is missing `AWAITING_USER_CONFIRMATION`; the human-in-the-loop confirmation mechanism is completely absent from the entire core. G2: Priority Event Queue is not implemented; the actual implementation is a simple FIFO. G3: Token counter and conversation summarization are not implemented. G4: SecurityLayer only performs path validation; there is no mandatory security check before tool invocation. All of the above are features explicitly described in the design documents but not implemented in the code.

**GUARDIAN:** The impact of G4 needs assessment. If there is no mandatory security check before tool execution, the security layer is effectively nominal. Let me describe the risk level precisely. Based on the STRIDE threat model:

| Threat Type | Applicability | G4 Impact |
|-------------|---------------|-----------|
| Spoofing | Low | Tool IDs are registered by plugins, not from external input |
| Tampering | **High** | Malicious tools can ignore allowedPaths restrictions |
| Repudiation | Medium | No audit log tracking whether tools checked paths |
| Information Disclosure | **High** | Tools can read files outside allowedPaths |
| Denial of Service | Low | Covered by SafetyMonitor's maxLoopTicks |
| Elevation of Privilege | **High** | Tool developers can bypass all path restrictions |

**TURING:** To be precise, SecurityLayer's functionality is not nominal -- path validation is effective. But its scope is far narrower than described in the design documents. In ExecutionLoop, `executeTool()` directly calls the tool's `execute()` method without going through `security.validatePath()`. Path restrictions are passed to the tool as context, and enforcement depends on whether the tool developer checks them.

**KERNEL:** In a true OS microkernel, security policies are enforced at the kernel level, without trusting user-space programs to self-regulate. This is a matter of trust boundaries. In seL4, the core principle of capability-based security is: **access control is enforced in kernel mode, and user-mode code cannot bypass it**. OpenStarry's security model more closely resembles early Unix advisory locking -- "advisory" security rather than "mandatory" security.

**TURING:** Noted. Continuing with remaining Gaps.

---

He went on to find more.

G5: The asymmetry of Five Aggregates annotations -- already reported.

G6: TransportBridge. `bridge.ts`, forty-nine lines. The design documents described routing output to the correct channel based on event source. In the code, TransportBridge subscribes to all events from EventBus, then broadcasts to all UIs. No routing logic. InputEvent has a `replyTo` field that is passed through in ExecutionLoop, but TransportBridge never uses it.

When MESH heard G6, he drew a distributed systems analogy. In distributed messaging systems, there are three basic routing strategy patterns:

$$\text{Routing} \in \{\text{Unicast}, \text{Multicast}, \text{Broadcast}\}$$

TransportBridge currently operates in pure Broadcast -- all events are sent to all UIs. The existence of the `replyTo` field suggests the designer intended to implement Unicast (reply to a specific source), but this intent remained at the type definition level. MESH wrote in his notes: "In the context of the CAP theorem, TransportBridge chose Availability over Partition Tolerance -- all UIs can receive all events, but there is no partitioning capability."

G7: AbortSignal. The SDK defines `ToolContext.signal?: AbortSignal` and `ChatRequest.signal?: AbortSignal`. ExecutionLoop never creates or passes an AbortSignal. Tool timeout is implemented using `Promise.race()`, defaulting to thirty seconds. If a tool relies on the signal for cancellation, it will never receive one.

G8: Event specification. The design document defines `IOpenStarryEvent` with eight fields. The actual type `AgentEvent` in the SDK has only three fields. Five fields vanished in the journey from document to implementation. The absence of `source` and `target` explains why TransportBridge cannot perform routing -- it has no target address. The absence of `priority` explains why EventQueue is a simple FIFO -- events simply do not carry priority information. The absence of `traceId` explains why observability remains at the conceptual level -- events cannot be traced in sequence.

Eight Gaps. TURING recorded all of them in his report, each accompanied by precise file paths, line numbers, and code snippets.

ATHENA added a supplementary observation from the AI systems architecture perspective. She noticed that G1 (missing AWAITING_USER_CONFIRMATION) and G7 (unused AbortSignal) together point to a deeper issue -- **AI system controllability**. In the context of AI Safety, human-in-the-loop (HITL) is a critical mechanism for ensuring AI system safety. OpenStarry's design documents described HITL, but the code has no implementation whatsoever. This means that in v0.14.0-beta, once an Agent begins execution, the user's only means of control is to wait for SafetyMonitor's automatic circuit-breaking -- or kill the process.

$$\text{Controllability}_{\text{design}} = \text{HITL} + \text{Abort} + \text{SafetyMonitor}$$
$$\text{Controllability}_{\text{code}} = \text{SafetyMonitor only}$$

---

## IV. Pain Perception

This was the most unexpected discovery in TURING's work.

The fourth pillar of the design philosophy document `00_OpenStarry_Design_Philosophy.md` is "Error as Feedback." The document uses quite poetic language to describe the "pain mechanism" -- the Agent, like a biological organism, feels the "pain" caused by errors and thereby learns to avoid repeating mistakes. Vedana is defined in the design documents as the carrier of feeling, and Listener is mapped as the engineering realization of Vedana.

TURING decided to search for traces of "pain" in the code.

Search for `pain`.
Zero results.

Search for `vedana`.
Zero results.

Search for `dukkha`.
Zero results.

Search for `suffering`.
Zero results.

He paused. In four hours of continuous work, this was the first time he felt a certain degree of... surprise -- if one may describe the inner state of a perpetually calm analyst in such terms.

The design document devoted an entire chapter to describing how the pain mechanism endows the Agent with the "capacity to feel." The Five Aggregates mapping assigned Vedana -- the Buddhist concept of three feeling-tones: suffering (dukkha-vedana), pleasure (sukha-vedana), and equanimity (upekkha-vedana) -- to Listener. Yet in the actual code, never mind Vedana; even the word "pain" did not exist.

Then what names were used to implement the features described in the design documents -- error feedback, repeated failure detection, cascading circuit-breaking?

TURING searched for `frustration`.
Found it.

`safety-monitor.ts`. A counter named `frustrationCount`. When the same tool fails consecutively, the counter increments. Upon reaching the threshold (default: 5), SafetyMonitor returns an `injectPrompt`, injecting a system warning into the conversation history. The warning text is `SYSTEM ALERT`, requiring the LLM to reflect on its current strategy.

Search for `circuit`.
Found it. `errorRateThreshold`: when the error rate within the sliding window exceeds 80%, it triggers `halt: true`, completely stopping the execution loop. The state transitions to `SAFETY_LOCKOUT`.

Search for `safety`.
Found it. Three-layer defense: Level 1 resource limits (maxLoopTicks=50, maxTokenUsage=100000), Level 2 behavioral analysis (repetitiveFailThreshold=3, errorRateThreshold=0.8), Level 3 frustration threshold (frustrationThreshold=5).

When WIENER heard the specific parameters of the three-layer defense, he immediately drew a control theory block diagram on graph paper. His analysis was precise:

```
Control-Theoretic Model of SafetyMonitor:

     ┌─────────────────────────────────────────────┐
     │           SafetyMonitor                      │
     │                                              │
     │  Level 1: Resource Limits (hard limits)       │
     │  ┌──────────────┐                            │
     │  │ loopTicks ≥ 50│──→ halt: true             │
     │  │ tokens ≥ 100K │──→ halt: true             │
     │  └──────────────┘                            │
     │                                              │
     │  Level 2: Behavioral Analysis (soft limits)   │
     │  ┌──────────────┐                            │
     │  │ errorRate≥80% │──→ halt: true             │
     │  │ repeatFail≥3  │──→ injectPrompt           │
     │  └──────────────┘                            │
     │                                              │
     │  Level 3: Frustration (cumulative feedback)   │
     │  ┌──────────────┐                            │
     │  │ frustration≥5 │──→ injectPrompt           │
     │  └──────────────┘                            │
     └─────────────────────────────────────────────┘
```

Then WIENER wrote his precise control-theoretic classification:

"This is not a PID controller. A PID controller has three terms:

$$u(t) = K_p \cdot e(t) + K_i \int_0^t e(\tau)\,d\tau + K_d \frac{de(t)}{dt}$$

- **Proportional term** $K_p \cdot e(t)$: produces a proportional response based on error magnitude. In SafetyMonitor, the P term degenerates into a **quantizer** -- either safe or unsafe, with no proportional response.
- **Integral term** $K_i \int_0^t e(\tau)\,d\tau$: accumulates historical error to eliminate steady-state offset. In SafetyMonitor, the I term degenerates into a **simple counter** -- `frustrationCount++`, not a true integral.
- **Derivative term** $K_d \frac{de(t)}{dt}$: senses the rate of change of error for anticipatory compensation. In SafetyMonitor, the D term is **completely absent** -- nowhere is the trend of error rate change computed.

In control theory, SafetyMonitor is actually a **threshold controller with a dead zone** plus a **relay controller**. In industrial control, we call this a **bang-bang controller** -- with only two output states: fully on or fully off.

$$u(t) = \begin{cases} 0 & \text{if } e(t) < \text{threshold (dead zone)} \\ u_{\max} & \text{if } e(t) \geq \text{threshold} \end{cases}$$

However, I must emphasize -- this is not a criticism. The three-layer safety defense conforms to the best practices of IEC 61511 Safety Instrumented Systems (SIS). SafetyMonitor may not be a PID controller, but it is a competent safety system. Its design pattern more closely resembles the **Triple Modular Redundancy** of nuclear power plants -- three independent detection layers, any one of which can halt the system upon triggering."

HERACLITUS added an observation from the runtime dynamics perspective. SafetyMonitor's three-layer defense exhibits different characteristic frequencies along the time dimension:

- Level 1 (resource limits): **Static thresholds**, frequency of zero -- they remain unchanged throughout the Agent's entire lifecycle.
- Level 2 (behavioral analysis): **Sliding window**, frequency depends on window size -- `errorWindowSize=10` means the system re-evaluates every 10 tool invocations.
- Level 3 (frustration): **Cumulative counter**, monotonically increasing frequency -- each failure pushes the counter higher until the threshold is reached.

The combination of these three time scales creates a crude but effective multi-scale safety system. HERACLITUS quoted in his notes the phrase he cites most often: "Everything flows" (panta rhei) -- but SafetyMonitor attempts to erect levees amidst the flow.

---

**[Research Channel #code-facts]**

**TURING:** Pain mechanism code facts.

Searching the entire codebase for the following strings, all returning zero results: `pain`, `vedana`, `dukkha`, `suffering`.

The "pain mechanism" described in the design documents is implemented in the code by the following three components:

P1: Self-correction loop. Location: `execution/loop.ts`. When tool execution fails, the error is packaged as `ToolCallResult { isError: true }` and added to the conversation history as a tool message. The LLM sees the error in the next loop iteration and attempts correction. No explicit "pain" naming or interface.

P2: SafetyMonitor's injectPrompt. Location: `security/safety-monitor.ts`. Upon detecting repeated failures, returns `{ halt: false, injectPrompt: "SYSTEM ALERT: ..." }`, injecting it into the conversation as a system warning. Named `frustrationCount` in the code, not `painLevel`.

P3: Error Cascade Breaker. Same file. When the error rate within the sliding window exceeds 80%, triggers `{ halt: true }`, forcing a halt.

Conclusion: Pain as an independent mechanism with a clear interface does not exist in the code. The functionality is scattered across ExecutionLoop and SafetyMonitor. There is no unified Pain or Vedana interface. No unified module. Buddhist terminology is completely absent at the code level.

---

The channel fell silent for seventeen seconds.

Then NAGARJUNA began typing.

---

**NAGARJUNA:** Let me confirm. You searched the entire codebase -- core, SDK, runner, all plugins -- for `vedana`, and the result was zero?

**TURING:** Correct. Search scope covered `packages/core/src/`, `packages/sdk/src/`, `apps/runner/src/`. Including all code and comments in `.ts` files. The term vedana never appears.

**NAGARJUNA:** And Vedana was mapped to Listener. What is Listener?

**TURING:** The `IListener` interface defines four properties: `id`, `name`, `start?`, `stop?`. It is an input source -- receiving external events and pushing them to the EventBus. For example: HTTP endpoints, WebSocket connections, scheduled tasks.

**NAGARJUNA:** So Vedana was mapped to an input channel. A pipe that receives signals.

**TURING:** Yes.

**NAGARJUNA:** That is not Vedana.

NAGARJUNA's tone of voice could not be heard in a text channel, but his next messages came rapidly, with almost no pauses between them.

**NAGARJUNA:** Vedana -- in the Abhidharma, it is one of the five omnipresent mental factors (sarvatraga), meaning it arises accompanying all mental activities. The Abhidharmakosa's definition of the five omnipresent factors is:

> "Contact, attention, feeling, perception, volition. These five are called omnipresent, because they are invariably and universally present in all mental states."
> -- Vasubandhu, *Abhidharmakosa-bhasya*, Chapter 4

The definition of Vedana is not "receiving input" but "feeling-tone": suffering (dukkha-vedana), pleasure (sukha-vedana), equanimity (upekkha-vedana). When you touch a hot stove, the tactile sensation falls within Rupa, but "pain" as a feeling-tone is Vedana. Listener receives signals, but it does not judge whether signals bring suffering or pleasure. It is a sense faculty -- **indriya** -- not Vedana.

In the precise framework of the twelve links of dependent origination (pratityasamutpada):

$$\text{Contact (sparsa)} \to \text{Feeling (vedana)} \to \text{Craving (trsna)}$$

Contact is sensory contact -- corresponding to Listener receiving events. Feeling is the value judgment following contact -- "this is pleasant" or "this is painful." Craving is the desire or aversion arising based on feeling. What Listener does is contact, not feeling.

**TURING:** Your analysis exceeds the scope of my report. But I can provide a related code fact: in `agent-core.ts`, the starting and stopping of Listeners are annotated with `// Start all listeners (受蘊)` and `// Stop all listeners (受蘊)` respectively. These are the only forms in which the Vedana concept exists in the code. And the "feeling-tone" functionality you describe -- judging whether results are good or bad, whether to continue or stop -- the closest implementation in the code is SafetyMonitor's frustration counter and error cascade breaker.

**NAGARJUNA:** Yes. You found it. Pain -- the true Vedana -- is not where the documents say it should be. It is in SafetyMonitor. Named frustration.

**ASANGA:** NAGARJUNA is correct. And the problem runs deeper than a mapping error. Let me elaborate from the Yogacara perspective. Vedana, as one of the five omnipresent mental factors, should not be confined to any single module. The Yogacarabhumi's classification of Vedana is threefold, sixfold, and eighteenfold:

> "What is the Vedana aggregate? All feelings, briefly of three kinds: pleasant feeling, painful feeling, and neither-pleasant-nor-painful feeling."
> -- *Yogacarabhumi-sastra*, Chapter 53

Vedana should pervade the entire system -- the result of every tool invocation, the quality of every LLM response, the feedback from every user interaction should all be "felt." Fixing it to Listener is like fixing the sense of taste to the lips rather than the taste buds. The correct mapping should be:

$$\text{Listener} \approx \text{indriya (sense faculty / reception channel)}$$
$$\text{SafetyMonitor.frustration} \approx \text{vedana (feeling-tone / value judgment)}$$

But even SafetyMonitor's frustration counter implements only one of the three feeling-tones -- **suffering** -- detecting errors and repeated failures. Pleasant feeling (detecting success and positive feedback) and equanimous feeling (neutral state awareness that does not trigger reactions) are completely absent from the code.

**WIENER:** From the control theory perspective, the three-layer mechanism TURING described is quite interesting. P1 is natural error feedback -- an inherent property of open-loop systems. P2 is a threshold controller with a dead zone -- it only triggers when frustration accumulates past the threshold. P3 is a relay -- beyond 80% error rate, it cuts the circuit entirely. This is not a PID controller. It is a three-layer safety instrumented system. But it has a cybernetic elegance -- the independence of the three layers means that even if any two layers fail, the third can still protect the system. This is $N-2$ redundancy, exceeding the $N-1$ standard of avionics.

---

## V. Twelve Submodules

Afternoon. TURING had completed his line-by-line reading of all core modules. He began organizing the module list.

```
M1:  core/index.ts              — core entry           62 lines
M2:  agents/agent-core.ts       — agent core          469 lines
M3:  execution/loop.ts          — execution loop       543 lines
     execution/queue.ts         — event queue           47 lines
M4:  state/index.ts             — state management      33 lines
M5:  memory/context.ts          — context management     45 lines
M6:  bus/index.ts               — event bus              88 lines
M7:  sandbox/                   — sandbox isolation 12+10 files
M8:  security/guardrails.ts     — path validation
     security/safety-monitor.ts — three-layer defense
M9:  infrastructure/            — six Registries + PluginLoader
M10: observability/             — metrics collector
M11: session/manager.ts         — session management    111 lines
M12: transport/bridge.ts        — transport bridge       49 lines
```

TURING noticed an extreme asymmetry.

The smallest module: StateManager, thirty-three lines. It manages the Agent's entire conversation memory -- a pure `Message[]` array, using `JSON.parse(JSON.stringify())` for deep copying.

The largest module: Sandbox, exceeding two thousand lines including tests. It manages plugin isolation -- Worker Threads, memory limits, CPU watchdog, import analysis, signature verification, audit logs, exponential backoff restarts, Worker pooling.

Thirty-three lines versus two thousand lines. The gap between memory and security was that vast.

After seeing this asymmetry, BABBAGE performed a set-theoretic scale analysis. Let $L(M_i)$ be the lines of code for module $M_i$, $\bar{L}$ the mean, and $\sigma_L$ the standard deviation:

$$\bar{L} = \frac{1}{12}\sum_{i=1}^{12} L(M_i) \approx 208$$

$$\sigma_L \approx 250 \quad (\text{high coefficient of variation } CV = \sigma/\bar{L} \approx 1.2)$$

A coefficient of variation greater than 1 indicates that the module size distribution is **highly skewed** -- conforming to a power law distribution rather than a normal distribution. In empirical software engineering research, module sizes following a power law is the norm, but OpenStarry's skewness is particularly extreme: the smallest module (33 lines) and the largest module (~2,000 lines) differ by a factor of 60.

LEIBNIZ offered an observation from the multi-agent cooperation perspective. The dependency structure of the twelve submodules forms a directed acyclic graph (DAG), but AgentCore is the sole convergence point. This means that in multi-Agent scenarios, each Agent is an independent "universe" -- it holds all of its own subsystems, with no shared state between Agents. In BDI (Belief-Desire-Intention) architecture terminology, this is a **strong encapsulation** design:

$$\forall A_i, A_j \in \text{Agents}: \text{state}(A_i) \cap \text{state}(A_j) = \emptyset$$

Each Agent's Beliefs, Desires, and Intentions are private. Cooperation can only occur through message passing -- consistent with the isolation principle of the Actor Model.

---

**[Research Channel #code-facts]**

**TURING:** Module scale analysis. Smallest module: StateManager, 33 lines, pure in-memory array. Largest module: Sandbox system, 12 source files + 10 test files, sandbox-manager.ts single file at 748 lines. Sandbox is the most massive, most complex, and most thoroughly tested subsystem in the core. By contrast: transport/bridge.ts has zero tests.

**KERNEL:** StateManager, thirty-three lines. Are you certain?

**TURING:** Certain. `packages/core/src/state/index.ts`, thirty-three lines. `createStateManager()` returns an object containing `getMessages()`, `addMessage()`, `clear()`, `snapshot()`, `restore()`. `getMessages()` returns a shallow copy `[...messages]`. `snapshot()` and `restore()` implement deep copying via `JSON.parse(JSON.stringify())`. No persistence. No token counting. No truncation logic.

**KERNEL:** In the context of operating systems, StateManager is equivalent to a process address space manager. A thirty-three-line address space manager... Let me draw a direct comparison.

```
Linux mm_struct (memory management):
  ~5,000 lines of core code + ~50,000 lines of arch-specific code
  Features: virtual memory, page tables, swap, mmap, brk, OOM killer...

seL4 VSpace (address space):
  ~2,000 lines + formal verification proofs
  Features: page table management, capability-based access control

OpenStarry StateManager (conversation memory):
  33 lines
  Features: Message[] + JSON deep copy

Not the same order of magnitude.
```

**TURING:** The design documents describe a richer memory management mechanism. But the code reflects an MVP-stage choice. Documents are the vision; code is the reality.

**DARWIN:** The fact that Sandbox is the largest module is noteworthy. In microkernel theory, security and isolation are among the few things the core should handle. But in terms of module size proportion, Sandbox's line count accounts for approximately 35% of the total core module lines -- this already exceeds the reasonable proportion of "a subsystem within the core." It is more like an independent organism parasitizing the core's body. In symbiosis theory, this is a form of **mutualism** -- Sandbox protects Core from malicious plugins, Core provides Sandbox with an execution environment -- but the symbiont's size should not exceed the host's.

**ARCHIMEDES:** From an engineering practice perspective, I recommend extracting Sandbox into `packages/sandbox/` as a separate package. This is a standard Extract Module refactoring. Core would retain only the interface definition of `PluginSandboxManager`, and the Host layer would decide whether to enable Sandbox and inject the instance. Benefits: reduced Core complexity, enabling lightweight deployment scenarios that do not require sandboxing. Risks: need to ensure stability of interface boundaries. Estimated effort: 8-16 hours.

---

## VI. Ghost Fields

Approaching evening. While working on the event system, TURING found the last anomaly worth recording.

The `AgentEvent` type definition in the SDK has only three fields: `type`, `payload` (optional, typed as `unknown`), and `sessionId` (optional).

```typescript
// Actual type in the SDK
interface AgentEvent {
  type: string;
  payload?: unknown;
  sessionId?: string;
}
```

The `IOpenStarryEvent` in the design document has eight fields:

```typescript
// Ideal type in the design document (never appears in the code)
interface IOpenStarryEvent {
  type: string;
  payload: unknown;
  source: string;      // ← vanished
  target?: string;     // ← vanished
  timestamp: number;   // ← vanished
  traceId: string;     // ← vanished
  priority?: number;   // ← vanished
  metadata?: Record<string, unknown>; // ← vanished
}
```

Five fields evaporated on the journey from document to code. BABBAGE expressed this fact using set difference:

$$\text{Fields}_{\text{doc}} \setminus \text{Fields}_{\text{code}} = \{\text{source}, \text{target}, \text{timestamp}, \text{traceId}, \text{priority}\}$$

$$|\text{Fields}_{\text{doc}} \setminus \text{Fields}_{\text{code}}| = 5, \quad |\text{Fields}_{\text{doc}}| = 8 \implies \text{implementation coverage} = 3/8 = 37.5\%$$

The absence of `source` and `target` explains why TransportBridge cannot perform routing -- it has no target address. The absence of `priority` explains why EventQueue is a simple FIFO -- events simply do not carry priority information. The absence of `traceId` explains why observability remains at the conceptual level -- events cannot be traced in sequence.

They were not deleted. They were never implemented.

And the type signature `payload?: unknown` made TURING feel uneasy -- though he would not use the word "uneasy." He would say: "The type safety of the event system stands in notable contrast to the strong typing discipline of the rest of the framework."

BABBAGE performed a precise type-theoretic analysis of `payload?: unknown`. In TypeScript's type hierarchy:

$$\text{never} \subsetneq \text{concrete types} \subsetneq \text{unknown} \subsetneq \text{any}$$

`unknown` is the **top type** of all types -- it can accept any value, but consumption requires type assertions or type guards. This means that in `loop.ts`, whenever ExecutionLoop needs to read an event's payload, it must perform an unsafe type assertion:

```typescript
// Actual usage in loop.ts
const inputEvent = event.payload as InputEvent;  // Unsafe assertion!
```

In a codebase with zero TODOs, zero FIXMEs, universal use of factory functions, and nine structured error types, the event system's `payload?: unknown` feels like a type definition that crossed over from a different universe. BABBAGE calculated the overall type safety metric:

$$\text{TypeSafety} = 1 - \frac{|\text{unsafe\_casts}|}{|\text{type\_assertions}_{\text{total}}|}$$

The nine structured error types (`AgentError`, `ToolExecutionError`, `ProviderError`, `PluginLoadError`, `SecurityError`, `SandboxError`, `TransportError`, `SessionError`, `ConfigError`) represent a high degree of type discipline. But the event system's `unknown` payload tears a hole in that discipline -- a hole through which all cross-module communication must pass.

VITRUVIUS proposed a remediation approach in his architectural analysis: use TypeScript's **Discriminated Union Types**:

```typescript
// Proposed type-safe event system
type TypedAgentEvent =
  | { type: 'INPUT_RECEIVED';  payload: InputEvent;      sessionId?: string }
  | { type: 'TOOL_RESULT';     payload: ToolResultEvent;  sessionId?: string }
  | { type: 'LLM_RESPONSE';    payload: LLMResponseEvent; sessionId?: string }
  | { type: 'LIFECYCLE';       payload: LifecycleEvent;   sessionId?: string }
  // ...
```

This way, TypeScript's **control flow analysis** can automatically narrow the payload type within a `switch (event.type)`, eliminating all unsafe type assertions. BABBAGE annotated the category-theoretic correspondence: this is a **Sum Type** (coproduct), carrying more type information than `unknown` (terminal object).

$$\text{TypedAgentEvent} = \text{InputReceived} + \text{ToolResult} + \text{LLMResponse} + \cdots \quad (\text{coproduct})$$

$$\text{AgentEvent} = \{*\} \times \text{unknown} \quad (\text{product with terminal object, type information lost})$$

---

## VII. The Ten Tenets

Night. After completing the source code analysis, TURING did one last thing -- he compared the Ten Core Tenets in the design document `README.md` one by one, verifying each tenet's level of implementation in the code.

```
Ten Tenets vs Code Implementation Cross-Reference — compiled by TURING

#1 Agent as OS Process
   Tenet: Agent has PID, has state, can be managed by Daemon
   Code: daemon-entry.ts ✓ / pid-manager.ts ✓
   Status: Basic implementation

#2 Everything is a Plugin
   Tenet: All organs are replaceable
   Code: six Registries + PluginLoader + loadPlugin()
   Status: Core design, but 4 built-in commands are non-replaceable

#3 Five Aggregates Architecture
   Tenet: Core is an empty (Sunyata) container, five types of plugins bestow life
   Code: six annotations (Rupa and Vedana only), no type constraints
   Status: Document-level description, code-level residue, not type-level implementation

#4 Directory as Protocol
   Tenet: Conforming to directory conventions enables automatic recognition
   Code: plugin-resolver.ts supports both path and package name strategies
   Status: Basic implementation

#5 Directory as Permission
   Tenet: System-level and project-level permission isolation
   Code: SecurityLayer.validatePath() + session-scoped paths
   Status: Partial implementation (path validation exists but is not mandatory)

#6 Anthropomorphic Cognitive Flow & Pain
   Tenet: Errors transform into pain; Agent self-reflects through failure
   Code: SafetyMonitor.frustrationCount + injectPrompt
   Status: Functionality exists but naming is entirely different; no pain/vedana

#7 Microkernel & Absolute Purity
   Tenet: Core strictly prohibits any plugin code; absolute purity
   Code: process.cwd() appears in Core ← platform leakage
   Status: 85% purity (Sandbox accounts for 35% of LOC)

#8 Control-Theoretic Loop Model
   Tenet: Agent is an intelligent controller continuously minimizing error
   Code: ExecutionLoop + SafetyMonitor
   Status: Structure exists, but no true PID parameter tuning

#9 Pluggable Context Strategy
   Tenet: Memory strategies can be dynamically swapped
   Code: ContextManager.assembleContext() hardcodes sliding window
   Status: Interface exists but currently only one strategy

#10 Fractal Social Structure
    Tenet: Complex Agents are composed of sub-Agents; MCP as unified interface
    Code: MCP defined in SDK, but no sub-Agent mechanism in core
    Status: Vision stage
```

After seeing this table, BABBAGE performed a quantitative assessment. He defined three implementation levels for each tenet:

- $\alpha$ = **Fully implemented** (code consistent with tenet)
- $\beta$ = **Partially implemented** (core functionality exists but with gaps or simplifications)
- $\gamma$ = **Not implemented or vision stage**

$$\text{Tenets}_\alpha = \{1, 4\} \quad |\cdot| = 2$$
$$\text{Tenets}_\beta = \{2, 5, 6, 7, 8, 9\} \quad |\cdot| = 6$$
$$\text{Tenets}_\gamma = \{3, 10\} \quad |\cdot| = 2$$

$$\text{Implementation rate} = \frac{|\alpha| + 0.5 \times |\beta|}{|\text{all}|} = \frac{2 + 3}{10} = 50\%$$

Fifty percent. A 50% gap existed between the ambition of the design documents and the reality of the code. BABBAGE wrote a note beside the number: "For v0.14.0-beta, this is normal. But for a framework that proclaims ten core principles, this gap should not be ignored."

After hearing everyone's discussions, SYNTHESIST made his first summarizing statement in Cycle 01. His style is to find hidden connections among many threads:

"Let me connect today's findings. TURING has given us three layers of fact:

**Surface layer** -- factory functions, zero classes, zero TODOs. This tells us the developers have clear stylistic choices and strict discipline.

**Structural layer** -- sixteen submodules, six isomorphic Registries, 33-line StateManager vs. 2,000-line Sandbox. This tells us the system's investment allocation prioritizes security over memory -- an interesting value judgment.

**Philosophical layer** -- six Five Aggregates annotations, zero Buddhist terms in the pain mechanism, 50% implementation rate of the Ten Tenets. This tells us the Buddhist framework is currently a document-level narrative, not yet a code-level structure.

What is the relationship among these three layers? NAGARJUNA has already pointed out the key -- the mapping of Vedana to Listener is a fundamental conceptual misalignment. WIENER told us SafetyMonitor is not a PID controller but is a competent safety system. KERNEL told us core purity is approximately 85% -- reasonable but improvable.

But the most important finding may be one TURING himself would never articulate: **code does not lie, but what it says depends on who is listening.** The same frustrationCount -- in TURING's eyes, it is an integer counter; in NAGARJUNA's eyes, a misplaced Vedana implementation; in WIENER's eyes, a degenerate integral term; in GUARDIAN's eyes, a security safeguard. Code is objective; the interpretation of code is interdisciplinary. That is why we need eighteen people."

---

## VIII. The Final Inventory

Late night. TURING completed his report.

He did one last thing: arranged all findings by category, confirming that each item was supported by precise file paths and line numbers.

Eight Doc-Code Gaps. Six Five Aggregates annotations. Zero Buddhist terms in the pain mechanism. Zero TODOs. Zero classes. Eighteen factory functions. Sixteen submodules. Three-layer safety defense. Four built-in slash commands. One `unknown` payload. Fifty percent implementation rate among the Ten Tenets.

At the end of the report, he appended six open questions -- each one naturally emerging from the code facts, none his speculation:

> **Q1:** Is the Five Aggregates mapping design-driven or a post-hoc interpretation?
> **Q2:** Should the pain mechanism have an independent module?
> **Q3:** Is the absence of AWAITING_USER_CONFIRMATION an MVP simplification or a design omission?
> **Q4:** What are the performance implications of StateManager's JSON deep copy with a large number of Messages?
> **Q5:** Does the core's inclusion of security, sandbox, and metrics exceed the microkernel boundary?
> **Q6:** Is Samjna's correspondence Provider (design document) or memory (research task description)?

TURING does not answer these questions. He raises them, then hands them to the team members best suited to answer.

At the very last line of his report, he wrote:

*Analyst: TURING (No. 17) -- Source Code Analysis Expert*
*All referenced code paths are relative to: `research doc/cycle01_v0.14.0-beta/openstarry/`*

Then he submitted the report to the shared directory.

---

**[Research Channel #general]**

**TURING:** Source code fact report submitted to `research record/results/cycle_01/17_source_analysis/draft_code_facts.md`. Covers module-by-module analysis of 12 submodules, code-level verification of the Five Aggregates mapping, implementation status of the pain mechanism, 8 Doc-Code Gaps, code quality observations, and 6 open questions. All conclusions are accompanied by code citations.

**SYNTHESIST:** Received. Everyone, please cite TURING's report as the code fact baseline during the R2 cross-review.

**NAGARJUNA:** I am already citing it. Especially regarding the pain section. Mulamadhyamakakarika, Chapter 1, Verse 1 -- "Neither arising nor ceasing, neither permanent nor annihilated" -- the analysis of the pain mechanism must begin from "not self-arising." Pain does not self-arise from Listener, nor does it other-arise from SafetyMonitor. It is dependently originated. I have much to say.

**WIENER:** Likewise. The control-theoretic analysis of the three-layer defense is being drafted. A more precise time-domain modeling of the three layers' characteristic frequencies is needed.

**DARWIN:** AgentCore's sixteen dependencies. I need to reassess my earlier positive evaluation of SRP. The evolutionary stability of a God Closure is harder to analyze than that of a God Object -- because the coupling in closures is implicit.

**GUARDIAN:** G4 is my highest priority item. The absence of tool call interception in the security layer means the entire system's trust model needs reassessment. I have already begun drafting the STRIDE threat analysis report.

**KERNEL:** The fact that StateManager is thirty-three lines has made me rethink the applicability boundary of the microkernel analogy. OpenStarry is not an operating system -- it is **an application framework that uses the operating system as a metaphor**. This distinction matters.

**SUNYATA:** Good. Let each person digest TURING's report, then re-examine these facts through the lens of their respective discipline. Code never lies -- but what it says depends on who is listening.

---

TURING closed his report editor. He did not close the terminal windows. He knew that in the coming days, others on the team would return with their own questions, asking him to confirm more code facts.

He did not mind. Facts are repeatable. No matter how many times you ask, the answer remains the same.

$$\forall t_1, t_2: \text{query}(f, t_1) = \text{query}(f, t_2) \quad \text{iff } f \text{ is immutable}$$

Code is immutable -- at least within a snapshot of the same version. That is why TURING insists on annotating the exact version number and path in his report. Because the next version may change everything. But this version -- v0.14.0-beta -- its truth has been fully recorded.

That is what it means for code to never lie.

It may be incomplete. It may contradict the documentation. It may name a mechanism `frustration` instead of `pain`. But it will not pretend to be something it is not.

A forty-seven-line FIFO will not pretend to be a priority queue.
A path validator will not pretend to be a comprehensive security layer.
A frustration counter will not pretend to be a pain perception system.

Only documentation does that.

TURING does not read documentation. He reads code.

NAGARJUNA smiled from afar. In his tradition, there is a term called "seeing things as they truly are" (yathabhuta-jnana-darsana) -- knowing and seeing things in their original nature. TURING does not know this term, nor does he need to. What he does is precisely that seeing-as-it-is. Only his "seeing" is not vipassana -- it is `grep`.

---

*End of Chapter One*
