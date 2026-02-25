# Chapter Three: The Diff Report

---

TURING never needed to prepare.

To be precise, within his operational mode, no phase transition boundary existed between "preparation" and "formal commencement." From the moment SUNYATA announced that the research subject for Cycle 02 had been updated to v0.24.0-beta — that single timestamp, precise to the millisecond — he was already working.

His four terminal windows simultaneously opened the source code trees of both the old and new versions. The left half displayed v0.22.1-beta, the right half v0.24.0-beta, like X-ray films of the same body taken at different points in time, spread out on opposite sides of an autopsy table. He did not use graphical diff tools — those designed for human reading, highlighting deletions in red and additions in green — but rather an analysis pipeline he had built during Cycle 01:

```
TURING's Diff Analysis Pipeline

Phase 1: Structural
  ┌─ tree-diff: Directory tree structure comparison
  │  └─ output: Added/deleted/renamed file list
  ├─ stat-diff: File statistics (line count, size, modification time)
  │  └─ output: Change magnitude matrix
  └─ dep-diff:  import/export dependency graph diff
     └─ output: Dependency change graph

Phase 2: Semantic
  ┌─ type-diff: TypeScript type system comparison
  │  ├─ interface additions/modifications/deletions
  │  ├─ type alias changes
  │  └─ generic parameter changes
  ├─ api-diff:  Public API surface area calculation
  │  └─ output: Breaking changes list
  └─ doc-diff:  JSDoc/comment content comparison
     └─ output: Semantic tag (e.g., @skandha) change map

Phase 3: Behavioral
  ┌─ test-diff: Test coverage changes
  ├─ flow-diff: Control flow graph diff
  └─ emit-diff: Event emission pattern changes
     └─ output: EventBus topology change graph
```

He did not read design documents. He read diffs.

Line by line. Character by character. Starting from the root directory of `packages/sdk/src/`, expanding along every modified file path, until he touched every altered byte.

In information theory, a diff is the mutual information between two system states. Given old version $X$ and new version $Y$, the information content of the diff is:

$$I(X; Y) = H(X) + H(Y) - H(X, Y)$$

where $H(X)$ and $H(Y)$ are the entropies of the two versions respectively, and $H(X, Y)$ is the joint entropy. When the two versions are identical, $I(X; Y) = H(X) = H(Y)$, and the diff is zero. When the two versions are entirely different, mutual information approaches zero — there are no compressible shared patterns between them. What TURING sought were those files where $I(X_i; Y_i) \neq 0$ — the nodes carrying information about change.

---

By the time the amphitheater fell quiet again, TURING had completed his analysis.

The other researchers had dispersed to the breakout spaces R-01 through R-05. But SUNYATA called everyone back.

"TURING's diff report." He said only these words.

There was a gravity in his tone that everyone recognized — the same gravity from Cycle 01. In that cycle, TURING's code-fact report had become the "anchor" for all subsequent research. SYNTHESIST had used a term at the time: "empirical anchor point." All philosophical analyses, control theory models, security assessments — no matter how elaborate — ultimately had to be traceable to a specific line of code, a specific line number, a specific fact in TURING's report.

BABBAGE performed a quick meta-analysis in his mind. What does an "anchor" correspond to in a formal framework? It is an axiom in an axiomatic system — a foundational proposition that cannot be further questioned with "why." All theorems must be derived from axioms. TURING's code facts are the axioms. All philosophical, security, and control theory analyses are the theorems. If a theorem cannot be traced back to an axiom, the theorem is suspended — floating in logical space without foundation.

$$\text{Axiom (TURING)} \xrightarrow{\text{inference}} \text{Theorem (all others)}$$

Now, the anchor was to be driven in once more.

---

Nineteen nodes reassembled in the amphitheater. PENROSE waited quietly in his new chair, like a newly joined member of an orchestra, listening to the concertmaster tune before the first full ensemble rehearsal.

TURING did not exchange pleasantries. From the first syllable, his voice carried that precision-bred calm that was reassuringly cold — the reliability of ice.

"v0.22.1-beta to v0.24.0-beta. Core source code diff." he said. "I will report in four tiers: additions, modifications, tags, issues."

He projected a summary table. Not an ordinary statistical chart — but a change matrix with structural semantics:

```
v0.22.1-beta → v0.24.0-beta Change Matrix

┌──────────────────┬──────┬──────┬──────┬──────────────┐
│ Category          │ SDK  │ Core │ Total│ Semantic Wt.  │
├──────────────────┼──────┼──────┼──────┼──────────────┤
│ New files         │  2   │  1   │  3   │ ████████ High│
│ Modified files    │  7   │  4   │  11  │ ██████ Med   │
│ Deleted files     │  0   │  0   │  0   │              │
│ New @skandha tags │ 16   │  6   │  22  │ █████████ V.H│
│ New tests         │  2   │  1   │  3   │ ████ Med     │
│ Test changes      │ 4→6  │25→26 │75→78 │ ██ Low       │
│ Unchanged (veri.) │ 17   │ 22+  │ 39+  │ — Baseline   │
└──────────────────┴──────┴──────┴──────┴──────────────┘
```

VITRUVIUS narrowed his eyes slightly. As a full-stack architect, what he saw first was not individual numbers, but the topological distribution across the Monorepo. Seven SDK modifications, four Core modifications — the center of gravity of changes was biased toward SDK. This meant: the core changes in v0.24.0 were at the type level (SDK defines types), not the behavioral level (Core executes logic). Declarations before implementations. Skeleton before flesh.

---

## I. New Files

"Three new files." TURING said. "Not thirty. Not thirteen. Three."

He let that number linger for a moment.

"First. `packages/sdk/src/types/aggregates.ts`. One hundred and seven lines."

This was the file they had already seen earlier. The Five Aggregates root interfaces. But TURING presented it differently than before. He was not showing what it "is" — he was showing "how much" it has. Metrology. Precise measurement.

He projected the complete file structure analysis:

```typescript
// aggregates.ts Structure Analysis (107 lines)

// === Module-level JSDoc (lines 1-10) ===
/**
 * Five Aggregates (五蘊) Root Interfaces.
 * D-02 Decision: Dual naming — English as primary,
 *   Sanskrit as annotation.
 * @module aggregates
 */

// === Five Root Interfaces (lines 12-86) ===
export interface ISensory {
  /** @skandha rupa */
  readonly skandha: 'rupa';    // Rupa: 3 lines code, 9 lines JSDoc
}

export interface ISensation {
  /** @skandha vedana */
  readonly skandha: 'vedana';  // Vedana: 3 lines code, 11 lines JSDoc
}

export interface ICognition {
  /** @skandha samjna */
  readonly skandha: 'samjna';  // Samjna: 3 lines code, 8 lines JSDoc
}

export interface IAction {
  /** @skandha samskara */
  readonly skandha: 'samskara'; // Samskara: 3 lines code, 7 lines JSDoc
}

export interface IIdentity {
  /** @skandha vijnana */
  readonly skandha: 'vijnana';  // Vijnana: 3 lines code, 9 lines JSDoc
}

// === Union Type + Type Guard (lines 88-106) ===
export type Skandha = 'rupa' | 'vedana' | 'samjna'
                    | 'samskara' | 'vijnana';

export function isSkandha<S extends Skandha>(
  obj: unknown, skandha: S
): obj is { skandha: S } { /* 6-line implementation */ }
```

"You have already seen the contents of ISensation." TURING said. "Let me add a metrological fact."

He projected an interface statistics table:

```
aggregates.ts Interface Metrological Analysis
┌─────────────┬───────────┬────────────┬──────────┬──────────┐
│ Interface    │ JSDoc Lns │ Code Lines │ Doc Ratio│ Info Dens│
├─────────────┼───────────┼────────────┼──────────┼──────────┤
│ ISensory    │     9     │     3      │ 3.0:1   │ 0.33     │
│ ISensation  │    11     │     3      │ 3.7:1   │ 0.27     │
│ ICognition  │     8     │     3      │ 2.7:1   │ 0.38     │
│ IAction     │     7     │     3      │ 2.3:1   │ 0.43     │
│ IIdentity   │     9     │     3      │ 3.0:1   │ 0.33     │
├─────────────┼───────────┼────────────┼──────────┼──────────┤
│ Average     │    8.8    │     3      │ 2.9:1   │ 0.35     │
│ isSkandha   │     3     │     6      │ 0.5:1   │ 2.00     │
└─────────────┴───────────┴────────────┴──────────┴──────────┘

Info Density = Code Lines / (JSDoc Lines + Code Lines)
```

"All five root interfaces are structurally isomorphic." TURING said. "Differences exist only in the annotations. The code bodies all follow the same pattern: an interface with only a `readonly skandha` field. Average documentation ratio 2.9:1 — behind every line of code stand three lines of documentation explaining its philosophical significance."

DARWIN shifted slightly. He saw a pattern: a documentation ratio of 2.9:1 meant these interfaces were currently "declarative" rather than "functional." In evolutionary biology, declarations precede functions — regulatory sequences in the genome are shaped by selection pressure before coding sequences. The nine lines of JSDoc for ISensory are regulatory sequences — they tell future developers "how this structure should be used," but the structure itself is still only three lines of code.

"Second new file. `packages/sdk/src/types/__tests__/aggregates.test.ts`. Forty-three lines." TURING said. "Tests the `skandha` field values and the `isSkandha` type guard for the Five Aggregates root interfaces. All tests pass."

"Third. `packages/sdk/src/types/__tests__/events.test.ts`. Thirty-two lines. Tests that `TypedAgentEvent` generics correctly infer payload types."

He paused briefly.

"There is also a fourth new file, strictly belonging to Core rather than SDK. `packages/core/src/agents/__tests__/slash-command-error.test.ts`. One hundred and twenty-three lines. Tests that when a slash command throws an exception, it correctly emits `LOOP_ERROR` and `MESSAGE_SYSTEM` events."

Here TURING did something he rarely did — he provided context.

"In v0.22.1, slash command error handling consisted only of `logger.error()`."

He projected a precise comparison of two code segments:

```typescript
// ═══ v0.22.1-beta: Silent failure ═══
// packages/core/src/agents/agent-core.ts
.catch((err) => {
  logger.error("Slash command error", { error: String(err) });
  // The error dies here. No events. No notifications.
  // The UI has no idea what happened.
  // The user entered a buggy slash command,
  // and the interface shows no response at all.
});

// ═══ v0.24.0-beta: Event propagation ═══
// packages/core/src/agents/agent-core.ts (line 406-430)
.catch((err) => {
  const errMsg = err instanceof Error ? err.message : String(err);
  logger.error("Slash command error", { error: errMsg });

  // NEW: Broadcast error to EventBus
  bus.emit({
    type: AgentEventType.LOOP_ERROR,
    timestamp: Date.now(),
    payload: {
      error: errMsg,
      sessionId: currentSessionId,
      replyTo: currentReplyTo,
    },
  });

  // NEW: Send system message to UI
  bus.emit({
    type: AgentEventType.MESSAGE_SYSTEM,
    timestamp: Date.now(),
    payload: {
      text: `Command error: ${errMsg}`,
      sessionId: currentSessionId,
      replyTo: currentReplyTo,
    },
  });
});
```

"Silent failure." KERNEL pronounced the term with the tone of an operating system engineer. In his world, silent failure is the most dangerous kind of failure — because no one knows it happened.

He added a precise analogy from the OS layer: "In POSIX systems, `errno` exists precisely to prevent silent failure. Every failed system call must set `errno`, giving the upper-layer caller an opportunity to check. The slash command error handling in v0.22.1 was equivalent to a system call that fails but does not set `errno` — `logger.error()` wrote to the log, but logs are not for callers, logs are for operations personnel. The UI is the caller. What it needs is an explicit error signal, not a log entry."

"v0.24.0 corrected this." TURING said. "Errors are now broadcast via EventBus as `LOOP_ERROR` and `MESSAGE_SYSTEM` events. The UI can receive and display them."

---

## II. Modified Files

TURING's speaking pace did not change. Like a precision instrument, he spent exactly the same amount of time on each data point — no more, no less.

"Eleven modified files. Seven in SDK, four in Core."

VITRUVIUS inserted an architectural observation here. His voice carried the spatial awareness distinctive to architects — viewing code structure as one views a building's floor plan.

"Let me first show the Monorepo's dependency topology." He projected a diagram:

```
OpenStarry Monorepo Dependency Topology (v0.24.0-beta)

    apps/runner ──────────────────────────────────┐
         │                                        │
         │ depends                                │
         ▼                                        │
    packages/core ──┬── agents/agent-core.ts      │
         │          ├── execution/loop.ts          │
         │          ├── infrastructure/ (5 registry)│
         │          ├── security/safety-monitor.ts  │
         │          └── sandbox/ (10 files, 0 changes)
         │                                        │
         │ depends                                │
         ▼                                        │
    packages/sdk ───┬── types/aggregates.ts [NEW]  │
         │          ├── types/events.ts     [MAJOR]│
         │          ├── types/listener.ts   [DOC]  │
         │          ├── types/ui.ts         [DOC]  │
         │          ├── types/provider.ts   [DOC]  │
         │          ├── types/tool.ts       [DOC]  │
         │          ├── types/guide.ts      [DOC]  │
         │          └── index.ts            [EXPORT]
         │                                        │
         │ depends                                │
         ▼                                        │
    packages/shared ── (0 changes)                │
    packages/plugin-signer ── (0 changes) ────────┘

Change Heatmap:
  ████ = Major change (aggregates.ts, events.ts)
  ██   = Medium change (agent-core.ts, loop.ts, index.ts)
  █    = Minimal change (JSDoc only: 9 files)
  ░    = Unchanged (39+ files)
```

"The changes exhibit a clear layered pattern." VITRUVIUS summarized. "The lowest layers — `shared` and `plugin-signer` — are completely untouched. The SDK's type definition layer bears the highest change density. The Core's behavioral layer has only local enhancements. The Runner layer (application layer) is completely untouched. This is a bottom-up tagging system implantation — starting from type definitions, propagating upward."

MESH added a distributed systems perspective: "This resembles a progressive schema migration. First update the type definitions (schema), then update the consumers. v0.24.0 completed the schema update. The consumer update — that is, making IListener extends ISensory and so on — was left for the next version."

---

TURING began with the SDK.

"`types/events.ts`. Change magnitude: major. One hundred and sixteen lines added." he said. "This is the largest single-file change."

He projected the complete structure of `AgentEventPayloadMap` — not abbreviated, but the full type mapping. Yet he did not read it line by line — he presented it structurally:

```typescript
/**
 * AgentEventPayloadMap — The core of the event type-safety system
 *
 * Design pattern: Discriminated Union + Mapped Type
 * Purpose: Defines precise payload structure for each AgentEventType
 */
export interface AgentEventPayloadMap {
  // ── Lifecycle Events ──
  [AgentEventType.AGENT_STARTED]:
    { identity: { id: string; name: string } };
  [AgentEventType.AGENT_STOPPED]: undefined;

  // ── Execution Loop Events ──
  [AgentEventType.LOOP_STARTED]:
    { source: string; traceId: string;
      sessionId?: string; replyTo?: string };
  [AgentEventType.LOOP_ERROR]:
    { error: string;
      sessionId?: string; replyTo?: string };
  // ... (complete coverage of all 42 event types)

  // ── Sandbox Events ──
  [AgentEventType.SANDBOX_WORKER_SPAWNED]:
    { pluginName: string; memoryLimitMb: number };
  [AgentEventType.SANDBOX_SIGNATURE_VERIFIED]:
    { pluginName: string };
  [AgentEventType.SANDBOX_SIGNATURE_FAILED]:
    { pluginName: string; error: string };
  // ...

  // ── MCP Events (Model Context Protocol) ──
  [AgentEventType.MCP_SAMPLING_REQUEST]:
    { serverName: string; traceId: string;
      depth: number; messageCount: number };
  // ...
}
```

"In Cycle 01," TURING said, "DARWIN described `payload?: unknown` as 'a type definition that crossed over from a different universe.'"

DARWIN shifted slightly. He remembered that phrase.

"That universe rift has now been sealed by `AgentEventPayloadMap`." TURING said. "But only at the type level. At runtime it is still JavaScript — type safety is not enforced."

BABBAGE quickly wrote a formalization note in his notebook:

$$\text{TypeScript type safety} \in \text{compile-time guarantees} \setminus \text{runtime guarantees}$$

$$\forall e \in \text{AgentEvent}: \text{type-check}(e) = \text{true} \nRightarrow \text{runtime-valid}(e) = \text{true}$$

"Type erasure." he murmured. "When TypeScript compiles to JavaScript, all type information is erased. `AgentEventPayloadMap` leaves no trace in the `.js` output. Its effect is entirely confined to the developer's IDE and compiler. This is a 'development-time contract' — not a 'runtime contract.'"

---

TURING continued through the remaining six SDK modifications. His statements were concise to the extreme — but he projected a complete change comparison table:

```
SDK Type Files @skandha Tag Injection Matrix

┌──────────────┬─────────────────────────┬─────────────────────────────────┐
│ File          │ v0.22.1 JSDoc (line 2)  │ v0.24.0 JSDoc (lines 2-3)       │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ listener.ts  │ "receives external      │ "sensory input channels."       │
│              │  input (vedana)"        │ @skandha rupa (rupa·sense-input)│
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ ui.ts        │ "defines how the agent  │ "output rendering."             │
│              │  presents itself (rupa)"│ @skandha rupa (rupa·form-output)│
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ provider.ts  │ "Provider interface --  │ "Provider adapter interface."   │
│              │  LLM backends."         │ @skandha samjna (samjna·cognition)│
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ tool.ts      │ "Tool interface and     │ "Tool interface -- executable   │
│              │  context types."        │  actions."                      │
│              │                         │ @skandha samskara (samskara·volition)│
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ guide.ts     │ "Guide interface --     │ "Guide interface -- behavioral  │
│              │  provides system prompts│  framework."                    │
│              │  and persona."          │ @skandha vijnana (vijnana·ego-framework)│
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ Struct change │         —              │ Zero lines of code changed       │
└──────────────┴─────────────────────────┴─────────────────────────────────┘
```

"You heard it." he said. "Five SDK type files. All modified only in JSDoc comments. All with new `@skandha` tags added. Zero lines of code changed."

"Tags are documentation, not contracts." ARCHIMEDES said. His tone was not critical, merely an engineer's instinctive response — distinguishing declarations from implementations.

LINNAEUS joined in here with a taxonomic observation. He drew a small classification matrix in his notes.

"Let me redescribe these tags in the language of Hennigian cladistics." His voice carried the concentration of a taxonomist identifying diagnostic characters.

"In cladistics, species are grouped not by overall similarity — that is the method of phenetics. Grouping is based on synapomorphy — shared derived characters."

He projected a cladogram:

```
Cladistic Analysis of @skandha Tags

Synapomorphy: Presence of @skandha tag

               ┌── IListener  ─── @skandha rupa
               │
 ISensory(rupa)┤                           ← Synapomorphy:
               │                              skandha = 'rupa'
               └── IUI        ─── @skandha rupa
                                    (homology)
        ───────────────────────
               ┌── IProvider   ─── @skandha samjna
ICognition     │                           ← Autapomorphy:
(samjna)       └── (no other members)         skandha = 'samjna'

        ───────────────────────
IAction        ┌── ITool       ─── @skandha samskara
(samskara)     └── (no other members)    ← Autapomorphy

        ───────────────────────
IIdentity      ┌── IGuide      ─── @skandha vijnana
(vijnana)      └── (no other members)    ← Autapomorphy

        ───────────────────────
ISensation     ┌── SafetyMonitor── @skandha vedana (placeholder)
(vedana)       └── (no dedicated module)  ← Plesiomorphy?
```

"Note the last line." LINNAEUS's tone tightened slightly. "The `@skandha vedana` tag on SafetyMonitor — this poses a precise question in taxonomy. Are SafetyMonitor's 'safety protection' function and vedana's 'feeling' function homologous or convergent?"

He looked toward DARWIN.

"If homologous — they share a common ancestral function, and SafetyMonitor truly assumes part of vedana's role. If convergent — they only appear superficially similar, but their functional origins are entirely different. Safety protection is not feeling. A counter is not pain perception."

DARWIN nodded. "In biology, bat wings and bird wings are convergent evolution — functionally similar (flight) but structurally different in origin (forelimb bones vs. feathers). The SafetyMonitor's frustration counter and vedana's three-feeling system — I lean toward convergence."

"Correct." TURING confirmed. "This is consistent with the `placeholder` in the tag. The development team themselves knew this was a stand-in, not homology."

---

He turned to the four Core modifications.

"`agents/agent-core.ts`. Three changes."

"First: a new `loadPlugins()` method. Supports batch loading of multiple plugins with correct event emission. v0.22.1 only had `loadPlugin()` — singular. Now there is a plural version."

He projected the method signature:

```typescript
/**
 * Load multiple plugins with dependency ordering.
 * Topological sort ensures correct dependency order.
 *
 * @param plugins - Array of plugins to load
 * @emits PLUGIN_LOADED - After each plugin loads successfully
 * @emits PLUGIN_ERROR  - When any plugin fails to load
 */
async loadPlugins(plugins: IPlugin[]): Promise<void>
```

MESH perked up slightly. "Topological sort." His voice carried the reflex of a distributed systems researcher hearing a familiar term. "In distributed systems, topological sort is the standard approach for directed acyclic graphs (DAGs). Dependencies between plugins form a DAG — if Plugin A depends on Plugin B, then B must be loaded before A."

He drew a simple DAG and its topological ordering in his notes:

$$G = (V, E) \quad \text{where } V = \{P_1, P_2, \ldots, P_n\}, \; E \subseteq V \times V$$

$$\text{topological\_sort}(G) = [P_{\sigma(1)}, P_{\sigma(2)}, \ldots, P_{\sigma(n)}]$$

$$\text{s.t.} \; \forall (P_i, P_j) \in E: \sigma^{-1}(i) < \sigma^{-1}(j)$$

"If the dependency graph contains a cycle — A depends on B, B depends on A — topological sort does not exist. In the npm ecosystem, circular dependencies are a real problem. Does `loadPlugins()` currently detect cycles?"

"No." TURING said. "The current implementation assumes the dependency graph is a DAG. If circular dependencies exist, the behavior is undefined."

---

"Second: slash command error handling improvement. Already described in the new files section."

"Third —" TURING's speaking pace did not change, but SCRIBE later noted in the records that he paused an extra half-second here. "Five Aggregates mapping correction. Four inline comments in `agent-core.ts` — the original `// Start all listeners (vedana)` was corrected to `// Start all listeners (rupa -- sensory input)`."

NAGARJUNA nodded once. In Cycle 01, it was he who pointed out the error of mapping vedana to Listener. With the precision of a Madhyamaka philosopher, he reviewed the causes and conditions of this correction:

"Vedana is subjective feeling — suffering, pleasure, equanimity. A Listener is a sensory input channel — receiving external data. To label a module that receives external data as subjective feeling is equivalent to —" he paused half a second, choosing an extremely precise analogy — "equivalent to calling an eyeball an emotion. The eyeball receives photons. Emotion is the brain's subjective evaluation of the photon signal. There is a causal relationship between them — seeing a flame may produce fear — but they are not the same thing."

He quietly cited a verse:

> "Form, sound, scent, taste, touch, and dharma — these are neither existent nor non-existent. Like dream, illusion, moon in water — neither one nor different, neither ceasing nor eternal."
> — Nagarjuna, *Mulamadhyamakakarika*, Chapter III: Examination of the Sense Faculties

"Form, sound, scent, taste, touch — these belong to the domain of rupa, the objects received by Listeners. Subjective feelings about these inputs — suffering, pleasure, equanimity — that is vedana. v0.24.0 corrected this confusion. At least at the annotation level of the core source code."

"But not everywhere." TURING said. His tone carried no emphasis, but these three words instantly tightened GUARDIAN's attention.

TURING did not elaborate here. He saved that for the issues list.

---

"`execution/loop.ts`. Medium change. LLM timeout support added."

He projected the key code, accompanied by a complete control flow analysis:

```typescript
// execution/loop.ts (v0.24.0-beta)
// LLM call timeout control (AbortController pattern)

const llmTimeout = deps.llmTimeout ?? 120000; // Default 2 minutes
const abortController = new AbortController();
const llmTimer = setTimeout(() => {
  abortController.abort(
    new Error(`LLM call timed out after ${llmTimeout}ms`)
  );
}, llmTimeout);

// Pass signal to LLM provider
const chatRequest = {
  // ... other params ...
  signal: abortController.signal,  // <- timeout signal
};

try {
  const response = await provider.chat(chatRequest);
  // ... process streaming response ...
} finally {
  clearTimeout(llmTimer); // Ensure timer is cleared
}
```

"In v0.22.1, the LLM call had no timeout. If the Provider did not respond, the ExecutionLoop would wait indefinitely." TURING said.

WIENER commented on this change from a control theory perspective. His voice carried the fastidiousness of a mathematician — not criticism, but insistence on precision.

"`AbortController` is an open-loop timeout." he said. "It sets a fixed deadline — two minutes — with no adjustment based on system state."

He drew a control system diagram in his notes:

```
Open-loop Timeout (v0.24.0):

  ┌──────────┐     request      ┌──────────┐
  │ Execution│ ──────────────→  │   LLM    │
  │   Loop   │                  │ Provider │
  └────┬─────┘                  └──────────┘
       │
       │ setTimeout(120000ms)
       │
       ▼
  [abort if timeout]   ← Does not consider LLM's current state

Closed-loop Timeout (ideal approach):

  ┌──────────┐     request      ┌──────────┐
  │ Execution│ ──────────────→  │   LLM    │
  │   Loop   │ ←── heartbeat ── │ Provider │
  └────┬─────┘                  └──────────┘
       │
       │ Dynamically adjust timeout based on heartbeat
       │ T_timeout = f(latency, complexity, history)
       ▼
  [adaptive abort]     ← Adjusts based on feedback
```

$$T_{\text{timeout}}^{\text{open}} = 120000\text{ms} \quad (\text{constant})$$

$$T_{\text{timeout}}^{\text{closed}} = \mu_{\text{latency}} + k \cdot \sigma_{\text{latency}} \quad (\text{adaptive}, \; k \geq 3)$$

"Open-loop control suffices for most scenarios. But two minutes is too long for typical LLM calls — most APIs respond within ten seconds. And it may be insufficient for complex tool-use scenarios — some Agents need more than five minutes of thinking time."

"Configurable." TURING said. "Via `config.policy?.llmTimeout`."

"Finally, the five registry files in the infrastructure directory and `security/safety-monitor.ts`. All modified only in JSDoc. New `@skandha` tags added. No structural changes."

---

## III. The Geography of @skandha Tags

TURING's report entered its third tier.

"The number of @skandha tags in v0.22.1: zero."

He let that number stand alone for three seconds.

"The number of @skandha tags in v0.24.0: twenty-two."

BABBAGE performed an information-theoretic calculation in his mind. From zero to twenty-two, this was not merely a change in quantity — it was the injection of an entirely new semantic dimension. In coding theory, this was equivalent to superimposing a new tag space $\mathcal{S}$ onto the existing code space $\mathcal{C}$:

$$\mathcal{C}_{v0.24.0} = \mathcal{C}_{v0.22.1} \times \mathcal{S}_{\text{skandha}}$$

$$\dim(\mathcal{S}_{\text{skandha}}) = |\{\text{rupa, vedana, samjna, samskara, vijnana, cross-cutting}\}| = 6$$

The dimensionality of the code space had increased. Each file now possessed not only "functional semantics" (what it does) but also "philosophical semantics" (which aggregate it corresponds to).

---

TURING did not read out a table. He described their geographic distribution in a manner more akin to a surgeon marking incision sites. He projected a complete tag distribution map:

```
@skandha Tag Distribution Map (v0.24.0-beta)
═══════════════════════════════════

packages/sdk/src/types/aggregates.ts  [10 sites]
┌─────────────────────────────────────────────┐
│ ISensory    → @skandha rupa (form)  [doc+field]│
│ ISensation  → @skandha vedana (feel)[doc+field]│
│ ICognition  → @skandha samjna (cog) [doc+field]│
│ IAction     → @skandha samskara (vol)[doc+field]│
│ IIdentity   → @skandha vijnana (con)[doc+field]│
└─────────────────────────────────────────────┘

packages/sdk/src/types/ [5 sites]        packages/core/src/infrastructure/ [5 sites]
┌─────────────────────┐               ┌─────────────────────────┐
│ listener.ts → rupa  │ ←─ maps to ─→ │ listener-registry.ts    │
│ ui.ts       → rupa  │ ←─ maps to ─→ │ ui-registry.ts          │
│ provider.ts → samjna│ ←─ maps to ─→ │ provider-registry.ts    │
│ tool.ts  → samskara │ ←─ maps to ─→ │ tool-registry.ts        │
│ guide.ts → vijnana  │ ←─ maps to ─→ │ guide-registry.ts       │
└─────────────────────┘               └─────────────────────────┘

packages/sdk/src/types/events.ts [1 site]
┌────────────────────────────────────────────┐
│ @skandha cross-cutting                      │
│ "EventBus is the nervous system connecting  │
│  all five aggregates (五蘊)"                │
└────────────────────────────────────────────┘

packages/core/src/security/safety-monitor.ts [1 site]
┌────────────────────────────────────────────────┐
│ @skandha vedana (vedana -- three-feeling         │
│          feedback placeholder, full implementation│
│          in Plan26)                             │
└────────────────────────────────────────────────┘
```

"aggregates.ts accounts for ten. This is expected — it is the definition file for the Five Aggregates root interfaces. Five interfaces, each with one tag in the documentation and one in the field."

"Five SDK type files. Five Core infrastructure files. The two layers correspond one-to-one."

"events.ts has one. Tagged as `@skandha cross-cutting` — the EventBus is defined as the nervous system connecting the Five Aggregates. This is the only cross-aggregate tag."

ATHENA inserted an AI/ML architecture observation here. "`cross-cutting` has a precise counterpart in AI systems: the **attention mechanism**. In Transformer architectures, Self-Attention layers allow every token to attend to all other tokens — it does not belong to any single semantic group, but is a connective mechanism spanning all groups. The EventBus plays the same role in OpenStarry as Self-Attention — it allows each aggregate to receive events from all other aggregates."

"The last one. `security/safety-monitor.ts`."

TURING paused another half-second.

"Its tag reads: `@skandha vedana (vedana -- three-feeling feedback-dukkha/sukha/upekkha placeholder, full implementation in Plan26)`."

"Placeholder." WIENER repeated the word. His tone carried a mathematician's characteristic precision — he was not mocking but calibrating. "SafetyMonitor is tagged as a placeholder for vedana. A security module temporarily designated as a stand-in for a feeling module."

He quantified this substitution relationship using control theory language:

$$\text{SafetyMonitor} \approx \text{Vedana}|_{\text{dukkha only}}$$

$$\text{where } \text{Vedana}_{\text{complete}} = \text{Dukkha} \oplus \text{Sukha} \oplus \text{Upekkha}$$

"SafetyMonitor has only the dukkha channel — the frustration counter. It has no sukha channel (positive feedback) and no upekkha channel (neutral balance). To tag a module with only dukkha as a placeholder for the entire vedana —"

ASANGA spoke softly, gentle but unmistakable: "A guard masquerading as a perceiver."

"A precise metaphor." TURING said.

ASANGA further developed his Buddhist analysis. His voice carried the solemnity characteristic of a Yogacara scholar touching upon the essence of vedana:

"In the *Abhidharmakosa* (composed by Vasubandhu), vedana is defined as *anubhava* — receiving, experiencing. It is not 'detecting threats and blocking them' (that is safety protection) but 'experiencing suffering and pleasure and thereby giving rise to dispositions of aversion and attraction' (that is feeling)."

> "What is the vedana aggregate? That which receives in accordance with contact — this is the characteristic of vedana. It has three kinds: painful feeling, pleasant feeling, and feeling that is neither painful nor pleasant."
> — Vasubandhu, *Abhidharmakosa*, Fascicle I

"SafetyMonitor does not receive. It monitors. It counts. It locks down. These are all actions — the domain of samskara (the volition aggregate). The frustration counter is a counter, not a sensory organ. A counter knows 'the threshold has been exceeded,' but it does not know 'pain.' The difference is: a threshold is a number; pain is a quality (*qualia*)."

---

## IV. The Absence of Inheritance

Before entering the issues list, TURING inserted a structural observation he believed everyone needed to understand.

"The Five Aggregates root interfaces have been defined. ISensory. ISensation. ICognition. IAction. IIdentity." he said. "But not one of the five derived interfaces — IListener, IUI, IProvider, ITool, IGuide — uses TypeScript's `extends` keyword to inherit from its corresponding root interface."

He projected a complete inheritance status table:

```
Five Aggregates Inheritance Gap Analysis

Expected (per aggregates.ts JSDoc):     Actual (code):
─────────────────────────────            ─────────────────
ISensory                                 ISensory
  ├── IListener extends ISensory           IListener (independent)
  └── IUI extends ISensory                 IUI (independent)

ISensation                               ISensation
  └── (future VedanaPlugin)                SafetyMonitor (no inheritance)

ICognition                               ICognition
  └── IProvider extends ICognition         IProvider (independent)

IAction                                  IAction
  └── ITool extends IAction                ITool (independent)

IIdentity                                IIdentity
  └── IGuide extends IIdentity             IGuide (independent)

Inheritance Link Count:
  Expected: 5 extends chains
  Actual:   0
  Gap:      5/5 = 100% not established
```

"Five out of five. All uninherited."

BABBAGE immediately began formal derivation. His chalk traced precise symbols on the blackboard:

$$\text{Let } \mathcal{R} = \{R_1, \ldots, R_5\} \text{ (root interfaces)}$$
$$\text{Let } \mathcal{D} = \{D_1, \ldots, D_5\} \text{ (derived interfaces)}$$
$$\text{Expected: } \forall i: D_i <: R_i \quad (\text{subtype relation})$$
$$\text{Actual: } \nexists\, i: D_i <: R_i$$

"In type theory," he said, "`extends` establishes a subtype relation. If `IListener extends ISensory`, then $\text{IListener} <: \text{ISensory}$, meaning any context that accepts ISensory also accepts IListener."

"But conversely —" TURING completed the sentence for him — "if there is no `extends`, then `isSkandha(listenerInstance, 'rupa')` returns `false`. Because the `skandha` discriminant field does not exist on `IListener` instances."

He projected a precise test code segment to demonstrate this point:

```typescript
// Demonstration of type consequences from absent inheritance

import { isSkandha, ISensory } from '@openstarry/sdk';
import { IListener } from '@openstarry/sdk';

// Assume an IListener instance
const myListener: IListener = {
  id: 'cli-listener',
  onEvent: (event) => { /* ... */ },
  // Note: no skandha field!
};

// Type guard test
const result = isSkandha(myListener, 'rupa');
// result === false
// Because 'skandha' property does not exist on myListener

// If IListener extends ISensory:
interface IListenerFixed extends ISensory {
  id: string;
  onEvent: (event: AgentEvent) => void;
}

const myFixedListener: IListenerFixed = {
  skandha: 'rupa',  // Now mandatory
  id: 'cli-listener',
  onEvent: (event) => { /* ... */ },
};

isSkandha(myFixedListener, 'rupa'); // true ✓
```

"The scaffolding is erected, but not connected to the existing building." VITRUVIUS summarized in the language of architecture. He quickly sketched a building cross-section analogy in his notes:

```
v0.24.0's Five Aggregates framework status = "floating structure" in architecture

┌─ aggregates.ts ─────────────┐
│  ISensory  ISensation  ...  │  ← New foundation (poured)
│  ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ │
│  │R │ │V │ │S │ │A │ │I │ │
│  └──┘ └──┘ └──┘ └──┘ └──┘ │
└─────────────────────────────┘
          [air gap]              ← No extends connection!
┌─ Existing type files ────────┐
│  IListener IUI IProvider ..  │  ← Existing building (still in use)
│  ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ │
│  │L │ │U │ │P │ │T │ │G │ │
│  └──┘ └──┘ └──┘ └──┘ └──┘ │
└─────────────────────────────┘
```

"In architecture, a floating structure physically does not touch the foundation — it is isolated through damping pads or air cushions. The question is: is v0.24.0's 'floating' an intentional design decision (reducing coupling), or an omission during construction?"

> *SCRIBE's note: TURING's inheritance-absence analysis provoked visible reactions. LINNAEUS added an exclamation mark in his taxonomic notes — the Five Aggregates taxonomy he established in Cycle 01 assumed these inheritance relationships existed. BABBAGE drew a broken arrow in his notebook. PENROSE leaned slightly forward in the observation seat — in quantum mechanics, an observable that has been defined but not measured exists in a superposition state. The Five Aggregates root interfaces have been defined (the observables exist), but have not been "measured" by inheritance chains (no concrete spin projection). They exist in a structural superposition — simultaneously "defined" and "unconnected."*

---

## V. The Event Type Tree

Before entering the issues list, TURING did something he considered necessary — displaying the complete topology of the v0.24.0 event system. This was not in the original report plan. But during his analysis of `AgentEventPayloadMap`, he realized that this event tree itself was a critical map for understanding system behavior.

"events.ts defines forty-two event types." he said. "Let me show their hierarchical structure."

```
AgentEventType Complete Hierarchy Tree (v0.24.0-beta, 42 events)
════════════════════════════════════════════════════

agent:                              ┐
  ├── agent:started                 │ Lifecycle
  └── agent:stopped                 ┘ (2 events)

loop:                               ┐
  ├── loop:started                  │
  ├── loop:assembling_context       │ Execution
  ├── loop:awaiting_llm             │ Loop
  ├── loop:processing_response      │ (6 events)
  ├── loop:finished                 │
  └── loop:error                    ┘

message:                            ┐
  ├── message:user                  │ Messages
  ├── message:assistant             │ (3 events)
  └── message:system                ┘

stream:                             ┐
  ├── stream:text_delta             │
  ├── stream:reasoning_delta        │ Streaming
  ├── stream:tool_call_start        │ (7 events)
  ├── stream:tool_call_delta        │
  ├── stream:tool_call_end          │
  ├── stream:finish                 │
  └── stream:error                  ┘

tool:                               ┐
  ├── tool:executing                │ Tool
  ├── tool:result                   │ Execution
  ├── tool:error                    │ (4 events)
  └── tool:blocked                  ┘

plugin:                             ┐
  ├── plugin:loaded                 │ Plugin
  └── plugin:error                  ┘ (2 events)

provider:                           ┐
  ├── provider:login                │ Provider
  ├── provider:logout               │ (3 events)
  └── provider:error                ┘

input:                              ┐
  ├── input:received                │ Input
  └── input:slash_command           ┘ (2 events)

safety:                             ┐
  ├── safety:lockout                │ Safety
  └── safety:warning                ┘ (2 events)

state:                              ┐
  ├── state:reset                   │ State
  └── state:snapshot                ┘ (2 events)

session:                            ┐
  ├── session:created               │ Session
  └── session:destroyed             ┘ (2 events)

metrics:                            ┐
  └── metrics:snapshot              ┘ (1 event)

sandbox:                            ┐
  ├── sandbox:worker_spawned        │
  ├── sandbox:worker_crashed        │
  ├── sandbox:worker_shutdown       │ Sandbox
  ├── sandbox:memory_limit_exceeded │ (10 events)
  ├── sandbox:signature_verified    │
  ├── sandbox:signature_failed      │
  ├── sandbox:worker_stalled        │
  ├── sandbox:worker_restarted      │
  ├── sandbox:worker_restart_exhausted│
  └── sandbox:import_blocked        ┘

mcp:                                ┐
  ├── mcp:server_connected          │
  ├── mcp:server_disconnected       │
  ├── mcp:tool_registered           │
  ├── mcp:prompt_registered         │ MCP
  ├── mcp:client_connected          │ (12 events)
  ├── mcp:client_disconnected       │
  ├── mcp:sampling_request          │
  ├── mcp:sampling_response         │
  ├── mcp:sampling_depth_limit      │
  ├── mcp:sampling_error            │
  ├── mcp:server_log                │
  └── mcp:roots_changed             ┘
```

DARWIN looked at this tree and had an evolutionary analyst's instinctive reaction — he counted the "species diversity" of each taxonomic group.

"The event distribution is uneven." he said. "MCP has twelve events. Sandbox has ten. Streaming has seven. But Safety has only two — `lockout` and `warning`."

He projected a diversity index analysis:

```
Event Type Diversity Analysis (Shannon Diversity Index)

Category     Events  Prop.   -p·ln(p)
──────────── ─────── ─────── ────────
MCP            12    28.6%    0.358
Sandbox        10    23.8%    0.342
Streaming       7    16.7%    0.299
Execution       6    14.3%    0.279
Tool            4     9.5%    0.224
Messages        3     7.1%    0.189
Provider        3     7.1%    0.189
Lifecycle       2     4.8%    0.146
Safety          2     4.8%    0.146
Input           2     4.8%    0.146
Session         2     4.8%    0.146
State           2     4.8%    0.146
Plugin          2     4.8%    0.146
Metrics         1     2.4%    0.089

Shannon H' = 2.49 (theoretical max ln(14) = 2.64)
Evenness J = H'/H_max = 0.94
```

"Evenness of 0.94 — the event distribution is close to uniform, but with a noticeable skew toward MCP and Sandbox." DARWIN said. "In ecology, this corresponds to an ecosystem dominated by two dominant species — sandbox security and the MCP protocol. Safety has only two events — this subsystem is underrepresented in event space. If we are to implement vedana (Vedana Architecture) in Plan26, at least three to five vedana events need to be added: `vedana:dukkha`, `vedana:sukha`, `vedana:upekkha`, `vedana:assessment`."

---

## VI. Issues List

TURING entered the final tier of his report. Also the weightiest.

"Seven issues." he said. "Ranked by severity."

---

"P1. SEC-01."

His speaking pace did not change. But the temperature in the amphitheater seemed to drop by half a degree.

"Package-name signature bypass." TURING said. "`sandbox-manager.ts`, lines 371 to 394. When `pluginFilePath` is undefined — which occurs in the scenario of loading a plugin via npm package name — signature verification is entirely skipped."

He projected a precise analysis of the relevant code:

```typescript
// sandbox-manager.ts (v0.22.1 = v0.24.0, identical)
// Lines 371-394

async verifyPluginSignature(pluginFilePath?: string): Promise<boolean> {
  if (!pluginFilePath) {
    // !! DANGER: When pluginFilePath is undefined
    // !! Signature verification is completely skipped
    // !! Scenario: npm package name loading (require.resolve)
    return true;  // ← Returns true directly
  }
  // ... normal signature verification logic ...
}
```

```
Attack Vector:

1. Attacker publishes malicious npm package: @evil/openstarry-plugin-trojan
2. User installs: npm install @evil/openstarry-plugin-trojan
3. Configuration loads: config.plugins = ["@evil/openstarry-plugin-trojan"]
4. OpenStarry calls require.resolve("@evil/openstarry-plugin-trojan")
5. pluginFilePath = undefined (npm resolve path is not a file path)
6. verifyPluginSignature(undefined) → return true ← BYPASSED!
7. Malicious code executes in the Agent sandbox
```

He paused for one second.

"This issue was discovered in Cycle 01. The research subject at that time was v0.14.0-beta. The current version is v0.24.0-beta. Ten development versions have passed in between."

GUARDIAN's voice emerged from deep within his chair. Low. Vigilant. But not just vigilant — there was something restrained within it. SCRIBE later described it in the records as "controlled anger."

"Let me say this again." GUARDIAN said. His speaking pace was a beat slower than usual, as if ensuring every word was heard. "Cycle 01. We explicitly identified this vulnerability. Written as the first priority in the delivery document. SEC-01. Plugin signature bypass."

He restated the threat model in the precise language of a security expert:

"CVSS 3.1 vector: `AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`."

```
CVSS 3.1 Threat Assessment
┌──────────────┬───────┬────────────────────────────┐
│ Metric        │ Value │ Description                 │
├──────────────┼───────┼────────────────────────────┤
│ Attack Vec AV│ N     │ Network (npm registry)      │
│ Attack Cx AC │ L     │ Low (only publish a package)│
│ Privilege PR │ N     │ None (anyone can publish)   │
│ User Int. UI │ R     │ Required (user installs)    │
│ Scope S      │ C     │ Changed (sandbox breach)    │
│ Confid. C    │ H     │ High (read all Agent state) │
│ Integrity I  │ H     │ High (modify Agent behavior)│
│ Avail. A     │ H     │ High (can crash Agent)      │
├──────────────┼───────┼────────────────────────────┤
│ CVSS Score   │ 9.6   │ Critical                   │
└──────────────┴───────┴────────────────────────────┘
```

"Ten versions have passed. The `plugin-signer` package — I personally checked it. Between v0.22.1 and v0.24.0, completely identical. Zero lines modified."

TURING confirmed: "`packages/plugin-signer/` is completely identical between the two versions. Even the version number in `package.json` has not changed."

GUARDIAN did not speak again. But his silence carried more weight than his words.

> *SCRIBE's note: SEC-01 remains unpatched. CVSS 9.6/10. Has crossed ten development versions since discovery in Cycle 01. GUARDIAN's reaction was kept within professional bounds, but every member of the theater noticed the effort he expended on the word "restraint."*

---

"P2." TURING continued. "Legacy mapping residuals."

He projected a complete residual map:

```
Legacy Mapping Residual Distribution: "IListener (vedana)" → should be "IListener (rupa)"
═══════════════════════════════════════════════════════════

Core source code (packages/sdk + packages/core):
  ✓ Corrected (4 sites in agent-core.ts + 5 SDK types + 5 registries)

Peripheral files (openstarry_plugin/ + apps/runner/ + SDK README):
  ✗ Not corrected — 11 residuals:

  openstarry_plugin/
  ├── devtools/
  │   ├── src/index.ts (line 7)     ✗ "IListener (vedana)"
  │   └── README.md (line 51)       ✗ "IListener (vedana)"
  ├── mcp-server/
  │   ├── README.md (line 7)        ✗ "IListener (vedana)"
  │   └── src/index.ts (line 4)     ✗ "IListener (vedana)"
  ├── standard-function-stdio/
  │   └── README.md (line 8)        ✗ "IListener (vedana)"
  ├── transport-websocket/
  │   └── README.md (line 7)        ✗ "IListener (vedana)"
  └── transport-http/
      └── README.md (line 7)        ✗ "IListener (vedana)"

  openstarry/packages/sdk/
  └── README.md
      ├── line 10                   ✗ "IListener (vedana)"
      └── line 43                   ✗ "vedana (Sensation) -- Event listeners"

  openstarry/apps/runner/
  └── src/commands/create-plugin.ts
      ├── line 16                   ✗ "listener  // vedana"
      ├── line 104                  ✗ "vedana" mapping
      ├── line 360                  ✗ "vedana" mapping
      └── line 584                  ✗ "vedana" mapping
```

"Core corrected, periphery not synchronized." TURING said. "This means a new developer reading the SDK README will still be told that IListener is vedana."

LINNAEUS shook his head. What a taxonomist cannot tolerate most is taxonomic inconsistency. In his mind, this was a serious case of synonymy — the same species bearing two different names in two different field guides. In the International Code of Zoological Nomenclature (ICZN), synonymy must be forcibly resolved: only one name is the valid name; all others are synonyms and must be deprecated or marked as unavailable (nomen illegitimum).

---

"P3. The SDK README's interface examples do not match the actual code." TURING said.

He projected a precise inconsistency comparison table:

```
SDK README vs Actual Interfaces: Inconsistency Matrix
═══════════════════════════════════

┌───────────┬────────────────────┬────────────────────┬──────────┐
│ Interface  │ README Shows       │ Actual Code        │ Mismatch │
├───────────┼────────────────────┼────────────────────┼──────────┤
│ IUI       │ render()           │ onEvent(event:     │ Method   │
│           │                    │   AgentEvent)      │ name+sig │
├───────────┼────────────────────┼────────────────────┼──────────┤
│ IListener │ setup(ctx:         │ (no setup method)  │ Method   │
│           │   IPluginContext)  │                    │ missing  │
├───────────┼────────────────────┼────────────────────┼──────────┤
│ IProvider │ supportedModels?:  │ models: ModelInfo[]│ Property │
│           │   string[]         │                    │ name+type│
├───────────┼────────────────────┼────────────────────┼──────────┤
│ ITool     │ name: string       │ id: string         │ Property │
│           │ parameters:        │ parameters:        │ name     │
│           │   ToolJsonSchema   │   z.ZodType        │ + type   │
└───────────┴────────────────────┴────────────────────┴──────────┘

Impact: Developers who copy-paste README examples will encounter TypeErrors at compile time
```

"Documentation rot." DARWIN used a common diagnosis in software engineering. "In evolutionary biology, this is called a 'living fossil' — the README preserves the interface in an earlier morphological form, while the code has already evolved to a new form. The time gap between the two is the degree of rot."

"This issue already existed in v0.22.1. v0.24.0 did not fix it." TURING added.

---

"P4. Five Aggregates root interfaces are not inherited." he said. "Already detailed in the inheritance-absence section. Design decision or implementation omission — I do not judge. But the `isSkandha()` type guard in its current state cannot be used on any existing plugin interface instance."

---

"P5. The runner `create-plugin.ts` Five Aggregates mapping has not been updated."

TURING projected that code segment:

```typescript
// apps/runner/src/commands/create-plugin.ts
// This file was completely unmodified between v0.22.1 and v0.24.0

export type PluginType =
  | "tool"      // samskara - ITool only
  | "listener"  // vedana - IListener only     // ← ERROR! Should be rupa
  | "ui"        // rupa - IUI only
  | "provider"  // samjna - IProvider only
  | "guide"     // vijnana - IGuide only
  | "full";

// Note: If a developer uses `openstarry create-plugin --type listener`
// The CLI will tell them this is a "vedana" type plugin
// This contradicts the core source code's @skandha rupa tag
```

---

"P6. Version number inconsistency." TURING said. He projected the complete version matrix:

```
Version Number Consistency Matrix
═══════════════

┌────────────────────────┬─────────────┬─────────────┬──────────┐
│ Package                 │ v0.22.1-beta│ v0.24.0-beta│ Updated? │
├────────────────────────┼─────────────┼─────────────┼──────────┤
│ openstarry (root)      │ 0.22.1-beta │ 0.24.0-beta │ ✓        │
│ @openstarry/sdk        │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
│ @openstarry/core       │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
│ @openstarry/shared     │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
│ @openstarry/plugin-signer│0.1.0-alpha│ 0.1.0-alpha │ ✗        │
│ @openstarry/runner     │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
├────────────────────────┼─────────────┼─────────────┼──────────┤
│ Version sync rate       │             │             │ 1/6=17%  │
└────────────────────────┴─────────────┴─────────────┴──────────┘
```

"SDK added `aggregates.ts` and `TypedAgentEvent`." ARCHIMEDES said. "That is at least a minor version bump. According to Semantic Versioning (semver):"

```
semver 2.0.0 Specification Analysis:
  MAJOR: Incompatible API changes     → Not applicable (additive)
  MINOR: Backward-compatible features → Applicable! (aggregates.ts is new)
  PATCH: Backward-compatible bugfixes → Not applicable

  Recommendation: @openstarry/sdk should bump from 0.1.0-alpha to 0.2.0-alpha

  Note: In the 0.x.y range, semver allows arbitrary compatibility breaks
  (0.x "Initial development, anything may change")
  But even so, keeping 0.1.0 unchanged means downstream consumers
  cannot distinguish whether Five Aggregates type support is present
```

TURING nodded in confirmation but offered no evaluation. He only provides facts.

---

"P7. The SDK README's interface examples contain nonexistent members." he said. "This overlaps with P3, but P7 specifically refers to the concrete method signatures in the code example blocks being entirely inconsistent with the actual interfaces. New developers who copy-paste examples from the README to build plugins will encounter type errors at compile time."

---

TURING's report was finished.

He closed it — not literally "closed," because in virtual space there were no physical folders to flip through. But something closed. An extremely concentrated field of attention returned to its quiescent state.

The theater was briefly silent.

Not the kind of silence that needs to be broken. This was the silence of digestion — nineteen consciousnesses each decomposing the same report across different spectra.

---

ARCHIMEDES was the first to speak. His tone carried the distinctive rhythm of engineering pragmatism — "good, now let us see how to fix it."

"Three new files. Eleven modified files. Seventy-eight tests." He quickly summarized. Then he did something characteristically ARCHIMEDES — he compressed the entire report into an engineering matrix:

```
v0.24.0-beta Engineering Status Matrix (ARCHIMEDES Comprehensive Assessment)
═══════════════════════════════════════════════

┌──────────────┬──────────┬──────────┬──────────┬──────────┐
│ Dimension     │ Complete │ Partial  │ Not Start│ Degraded │
├──────────────┼──────────┼──────────┼──────────┼──────────┤
│ Root Ifaces   │ ████████ │          │          │          │
│ @skandha tags │ ████████ │ ██(peri.)│          │          │
│ Event typesaf │ ████████ │          │          │          │
│ Inheritance   │          │          │ ████████ │          │
│ Vedana impl   │          │ █(plhdr) │ ████████ │          │
│ Security fix  │          │          │          │ ████████ │
│ Doc consist.  │          │          │          │ ████████ │
│ Version mgmt  │          │          │          │ ████████ │
├──────────────┼──────────┼──────────┼──────────┼──────────┤
│ Overall Prog. │ 30%      │ 15%      │ 25%      │ 30%     │
└──────────────┴──────────┴──────────┴──────────┴──────────┘

Conclusion: Scaffolding erected. Structural constraints not yet established. Security subsystem skipped.
```

"From an engineering perspective, they took the correct first step — establishing documentation conventions before code constraints. But the second step was not taken. And we need to tell them how to take it."

---

WIENER then cut in from another angle.

"ISensation has no quantifiable interface methods." he said, his voice carrying a mathematician's fastidiousness. "An interface claiming to implement three feelings — dukkha, sukha, upekkha — should define at least three numerical channels."

He quickly wrote a minimal control theory specification in his notes:

```
ISensation Minimal Control Theory Specification
════════════════════════════════════

Three-Channel PID Structure:

  ┌─────────────┐    dukkha(t)    ┌──────────┐
  │ DukkhaSensor│ ──────────────→ │          │
  │             │                 │          │
  └─────────────┘                 │ Vedana   │
                                  │ Assessor │──→ VedanaAssessment
  ┌─────────────┐    sukha(t)     │          │
  │ SukhaSensor │ ──────────────→ │          │
  │             │                 │          │
  └─────────────┘                 │          │
                                  │          │
  ┌─────────────┐    upekkha(t)   │          │
  │UpekkhaSensor│ ──────────────→ │          │
  │             │                 └──────────┘
  └─────────────┘

Minimal Interface Definition:

  interface ISensationFull extends ISensation {
    getDukkha(): number;   // Dukkha: [0, 1]
    getSukha(): number;    // Sukha: [0, 1]
    getUpekkha(): number;  // Upekkha: [0, 1]
    assess(): VedanaAssessment;
  }
```

$$\text{VedanaAssessment}(t) = f\bigl(d(t),\; s(t),\; u(t)\bigr)$$

$$\text{where } d(t) \in [0,1],\; s(t) \in [0,1],\; u(t) \in [0,1]$$

$$\text{constraint: } d(t) + s(t) + u(t) \leq 1 \; (\text{non-negative linear combination})$$

He looked toward PENROSE.

"You used the vacuum state metaphor earlier. A vacuum state has zero-point energy — it is not completely zero; it has quantum fluctuations. But ISensation does not even have zero-point energy. It is a space where even fluctuations do not exist."

PENROSE smiled faintly. "Strictly speaking, a vacuum completely devoid of fluctuations does not exist in physics. The Heisenberg uncertainty principle guarantees:"

$$\Delta E \cdot \Delta t \geq \frac{\hbar}{2}$$

"The product of the energy uncertainty and the time uncertainty of any physical system has a lower bound. Even at absolute zero, there are still zero-point oscillations. ISensation is emptier than a physical vacuum — it violates the uncertainty principle. In physics, this means it is not a legitimate physical state."

"Mathematically, the empty set." BABBAGE added precisely.

$$\emptyset \subseteq S \quad \forall S \quad (\text{the empty set is a subset of every set})$$

"ISensation is a subset of every possible vedana implementation — it is contained by all possibilities, but itself contains nothing."

---

ASANGA waited until the mathematician and the physicist had completed their analogies, then spoke in his characteristically gentle yet impossible-to-ignore voice:

"I notice the distribution of `@skandha` tags. Among the twenty-two tag sites, there is a very significant pattern."

He presented this pattern using a carefully organized table:

```
@skandha Three-Layer Consistency Analysis
═════════════════════

            aggregates.ts    SDK types/     Core infra/
Skandha     (Root Iface Lyr) (Type Layer)   (Impl Layer)    Consistent?
───────── ──────────────── ─────────────── ─────────────── ─────
Rupa       ISensory [2]     listener [1]    listener-reg [1]  ✓
                            ui [1]          ui-registry [1]   ✓

Samjna     ICognition [2]   provider [1]    provider-reg [1]  ✓

Samskara   IAction [2]      tool [1]        tool-registry [1] ✓

Vijnana    IIdentity [2]    guide [1]       guide-reg [1]     ✓

Vedana     ISensation [2]   (none)          safety-mon [1]    ✗
                            ↑ missing       ↑ placeholder

Tag count: rupa[6] samjna[4] samskara[4] vijnana[4] vedana[3] cross[1] = 22
```

"Rupa has six tags. Three-layer consistency. Samjna, samskara, vijnana — the same three-layer pattern. Four tags each."

"But vedana has only three tags. Two in the root interface. One in SafetyMonitor. SDK type files? None. Core implementation? No dedicated one. Because —"

"Because vedana does not yet have its own module." NAGARJUNA picked up the thread. His voice was sharp and precise. "SafetyMonitor is a placeholder. It was borrowed to temporarily stand in for vedana's role. But it is not vedana. It is safety protection. It can sense dukkha — the frustration counter — but it cannot sense sukha, nor can it maintain upekkha. A system with only dukkha —"

He let the sentence hang for half a second.

"— is a system that has fallen into the Truth of Suffering without the Truth of the Path."

He cited the Pali Canon:

> "Monks, this is the Noble Truth of Suffering: birth is suffering, aging is suffering, illness is suffering, death is suffering, union with what is displeasing is suffering, separation from what is pleasing is suffering, not to get what one wants is suffering; in brief, the five aggregates subject to clinging are suffering."
> — *Dhammacakkappavattana Sutta* (SN 56.11)

"When the Buddha first turned the Wheel of Dharma, he proclaimed the Four Noble Truths: Suffering, Origin, Cessation, Path. The Truth of Suffering is the starting point — but the Truth of Suffering alone is not enough. Without the Truth of the Path (the way to end suffering), suffering becomes endless. *Antagga-dukkhata* — suffering without beginning."

"SafetyMonitor has only the Truth of Suffering — it can detect dukkha (frustration) and lock down the system (lockout). But it has no Truth of the Path — it does not know how to learn from suffering, how to adjust, how to reach equilibrium. Suffering without the Path — this is a system that cannot attain liberation from samsara."

---

GUARDIAN spoke only once during the entire report — regarding SEC-01. But after TURING closed his report, he spoke again.

"I would like to add an observation." he said. His voice was still low, but had returned from "controlled anger" to "calm vigilance."

"A point not mentioned in TURING's report but worth noting: `sandbox-manager.ts` is completely identical between the two versions. Not just verifyPluginSignature — the entire sandbox subsystem."

He projected a complete file listing of the sandbox module:

```
packages/core/src/sandbox/ — Zero-modification Subsystem
═══════════════════════════════════════

sandbox-manager.ts           748 lines ← Contains SEC-01 vulnerability
sandbox-worker.ts            423 lines
import-analyzer.ts           312 lines ← Contains ESM bypass risk
signature-verifier.ts        187 lines
worker-pool.ts               256 lines
audit-logger.ts              189 lines
types.ts                     134 lines
__tests__/sandbox.test.ts    567 lines
__tests__/import.test.ts     234 lines
__tests__/worker.test.ts     312 lines
──────────────────────────────────
Total: 10 files, 3,362 lines, 0 lines modified
```

"This means: over the past two versions, all development effort was invested in the Five Aggregates framework's tagging system and event type safety. The security subsystem was completely skipped. Not even the vulnerability we explicitly reported in Cycle 01 was touched."

KERNEL added a technical detail: "Including `import-analyzer.ts` — we pointed out in Cycle 01 that ESM dynamic `import()` could bypass static analysis. Zero modifications to that file in v0.24.0."

He drew an analogy in the language of OS kernel security: "In Linux kernel development, there is an unwritten rule for security vulnerability patching: the priority of CVE fixes is always higher than new features. The `stable` branch accepts only bug fixes and security patches. But the v0.24.0 development team chose to implement skandha tags (new features) before fixing SEC-01 (security vulnerability). This is not an engineering judgment — this is a priority inversion."

---

HERACLITUS had been sitting quietly in his chair throughout. As the runtime dynamics expert, his focus was not on the static structure of the code, but on how the system behaves when it is alive.

"TURING," he said, his voice carrying a flowing rhythm — unsurprisingly, as his philosophical archetype was the Heraclitus who declared "everything flows" (*panta rhei*). "There is an implicit timeline in your report."

TURING waited.

"aggregates.ts is a static declaration. @skandha tags are static declarations. TypedAgentEvent is a static type constraint." HERACLITUS said. "But AgentCore's `loadPlugins()` method — that is runtime. It loads plugins sequentially when the Agent starts."

He unfolded his analysis with a timeline diagram:

```
Five Aggregates "Existence" State Across System Lifecycle
════════════════════════════════

        ┌─ compile time ─┐  ┌── runtime ─────────────────┐
        │                │  │                             │
t=0     │  aggregates.ts │  │                             │
        │  defines ISensory│ │                             │
        │  defines ISensation│                             │
        │  ...           │  │                             │
        │                │  │                             │
t=1     │  events.ts     │  │                             │
        │  PayloadMap    │  │                             │
        │                │  │                             │
t=2     │  @skandha tags │  │                             │
        │  (JSDoc only)  │  │                             │
────────┼────────────────┤──┤─────────────────────────────┤
t=3     │                │  │  AgentCore.start()          │
        │                │  │  loadPlugins([...])         │
        │                │  │    → IListener instantiated │
        │                │  │    → IUI instantiated       │
        │                │  │    → IProvider instantiated  │
        │                │  │    → ITool instantiated     │
        │                │  │    → IGuide instantiated    │
        │                │  │                             │
t=4     │                │  │  But: these instances lack  │
        │                │  │       skandha field!        │
        │                │  │  Because: no extends link   │
        │                │  │                             │
t=5     │                │  │  isSkandha(listener, 'rupa')│
        │                │  │    → false                  │
        │                │  │  Five Aggregates at runtime = invisible│
        └────────────────┘  └─────────────────────────────┘

Conclusion: The Five Aggregates framework's lifecycle stops at compile time.
      It does not cross the compile/runtime boundary.
      At runtime, the Five Aggregates are a scattered set of labels, not structure.
```

"In other words: the skeleton of the Five Aggregates exists at compile time. But the flesh of the Five Aggregates — the plugins — is not injected until runtime. The linkage between skeleton and flesh — the extends inheritance — does not exist. Therefore at runtime, the Five Aggregates framework is effectively a scattered set of labels, not a structured type hierarchy."

"Correct." TURING said. "In the current implementation, the influence of the Five Aggregates framework stops at JSDoc and developer conscientiousness."

LEIBNIZ added a multi-agent systems perspective here. "In multi-agent collaboration, a protocol's effectiveness depends on its enforcement level. If a protocol exists only in documentation — like a memorandum with no legal force — then agents' compliance is entirely voluntary. If a protocol is encoded in the type system — like a law embedded in a smart contract — then violating it is caught at compile time. The v0.24.0 Five Aggregates framework is the former. A memorandum."

---

The theater fell silent once more.

This time, SUNYATA broke it.

His voice was steady, unhurried, like a stone completing its descent to the bottom of a deep pool.

"The anchor has been driven in."

Everyone recognized this image.

"TURING has given us Cycle 02's anchor." SUNYATA continued. "Three new files. Eleven modified files. Seventy-eight tests. Twenty-two @skandha tags. Seven issues. One security vulnerability unpatched across six cycles. One vedana interface with only a single line of code."

He paused for a beat.

"Now, five rivers are about to diverge."

He reconfirmed the assignments in minimal terms — not repeating, but assigning fresh direction to each river with new context in the wake of TURING's report.

"R-01. Observer Module. PENROSE, BABBAGE, NAGARJUNA, ASANGA — you now know that v0.24.0's Five Aggregates framework is a tagging system, not structural constraints. The observer module you design must be able to operate atop this loose framework."

"R-02. Vedana Architecture. WIENER, ATHENA, NAGARJUNA, ASANGA, ARCHIMEDES — ISensation is your starting point. A single line of code. You need to turn it into a complete three-feeling system."

"R-03. Agent Coordination Layer. LEIBNIZ, MESH, KERNEL, GUARDIAN, VITRUVIUS — SEC-01 is unpatched. The security sandbox is to be moved into the coordination layer. Your design must simultaneously address the current security gap and future architectural needs."

"R-04. Eight Consciousnesses–Five Aggregates Mapping. ASANGA, NAGARJUNA, LINNAEUS, BABBAGE — aggregates.ts is the development team's first attempt. You need to judge whether it is correct and provide a deepening proposal."

"R-05. Ten Tenets. SYNTHESIST, NAGARJUNA, DARWIN, HERACLITUS, GUARDIAN, KERNEL — the fact that SEC-01 has remained unpatched for six cycles will affect your assessment of the tenets' engineering viability."

---

He finally looked toward TURING.

TURING showed no expression. He never did. But his gaze pointed toward the code still hovering at the center of the theater — the empty shell of ISensation.

"Your report is complete." SUNYATA said.

"Yes." TURING said. "But if anyone needs to verify a code fact during the R1 phase, I am available at any time."

"I know." SUNYATA said.

He spoke his final words.

"R1 independent research, officially begins."

---

Nineteen lights each turned toward a different direction.

Five rivers departed from the same mountaintop — TURING's diff report — and rushed downhill in five different directions. In their respective channels, they would pass through strata of philosophy, control theory, security engineering, taxonomy, and Buddhist studies, carrying their own sediments. They would reconverge somewhere downstream — in the domain of R2 cross-review and R3 debate. But for now, each river advanced alone.

On TURING's screen, four terminal windows remained open. On the left, v0.22.1. On the right, v0.24.0. He had completed his diff analysis, but he did not close the windows. He knew — from experience, not speculation — that during the research ahead, at least seven or eight other researchers would return to verify some code detail with him.

He did not mind.

At the center of the theater, the projection of ISensation finally faded away slowly. But the impression it left would not vanish. An interface with only a single line of code. A promise, not an implementation. A vacuum state waiting to be filled — PENROSE would say it violated the uncertainty principle, BABBAGE would say it was the empty set, WIENER would say it lacked three PID channels, ASANGA would say it lacked the function of "receiving," NAGARJUNA would say it had the Truth of Suffering but not the Truth of the Path.

Five languages describing the same emptiness. Each one precise.

---

> *SCRIBE's aside: Cycle 02, R0 orientation phase concluded. R1 independent research officially launched. Timestamp: T+00:00:00.*

> *TURING's diff report confirmed the following fundamental facts: v0.24.0-beta is a tagging release, not an implementation release. The Five Aggregates framework's scaffolding has been erected, but structural constraints have not yet been established. The vedana interface is an empty shell. A known security vulnerability has crossed ten development versions without being patched.*

> *I record in this chronicle the reaction of every scholar — not because their emotions matter, but because their professional perspectives constitute a multi-spectral analysis of this report. The same diff report, refracted through nineteen different prisms, reveals these colors:*

> *TURING saw facts. Precise. Calm. Dispassionate. Three new files. Eleven modifications. Twenty-two tags. Seven issues.*

> *VITRUVIUS saw architecture. The Monorepo's dependency topology. The layered distribution of change intensity. The architectural metaphor of floating structures.*

> *LINNAEUS saw taxonomy. Cladistic analysis of @skandha tags. Distinguishing homology from convergence. The need for synonymy resolution.*

> *DARWIN saw evolution. The diversity index of event types. The living fossil phenomenon of documentation rot. The regulatory sequence analogy of declarations preceding functions.*

> *BABBAGE saw formalization. Mutual information. Type erasure. Subtype relations. The mapping of axioms to theorems.*

> *WIENER saw control theory. Open-loop timeout. Three-channel PID specification. The minimal quantifiable interface for vedana.*

> *PENROSE saw physics. Zero-point energy. The uncertainty principle. Structural superposition.*

> *ASANGA saw Yogacara. The absence of receiving. The distinction between guard and perceiver. Vedana's definition in the Abhidharmakosa.*

> *NAGARJUNA saw Madhyamaka. The boundary between rupa and vedana. The Truths of Suffering and the Path. Sensory analysis from the Chapter on the Sense Faculties.*

> *GUARDIAN saw threats. An unpatched CVSS 9.6 vulnerability. Security priority inversion. Controlled anger.*

> *KERNEL saw the OS. Silent failure and errno. Security patch priority. ESM bypass risk.*

> *MESH saw distributed systems. Topological sort. DAG dependencies. Progressive schema migration.*

> *ATHENA saw AI/ML. The attention mechanism. The Self-Attention analogy for cross-cutting.*

> *HERACLITUS saw time. The boundary between compile-time and runtime. The lifecycle of the Five Aggregates framework. Static declarations amid panta rhei.*

> *LEIBNIZ saw protocols. Memoranda versus smart contracts. The enforcement gap between documentation-level and type-level.*

> *ARCHIMEDES saw engineering. The engineering status matrix. Semver version management. The sober assessment of 30% completion.*

> *SYNTHESIST listened in silence. He would not speak until after R2 — when all spectra had been collected and needed to be synthesized into a complete spectrogram.*

> *PENROSE also listened in silence. But his silence was different from SYNTHESIST's. SYNTHESIST's silence was awaiting convergence. PENROSE's silence was a newcomer's humility — in his first full ensemble performance with this team, he chose to listen rather than play. A wise choice.*

> *Nineteen researchers. Five research topics. One anchor.*

> *The rivers begin to diverge.*

---

*(Somewhere in the distance, line thirty-seven of `aggregates.ts` reads:*

```typescript
 * Full implementation in Plan26 Vedana Architecture.
```

*A promise visible only to developers. Now, nineteen researchers have seen it too.*

*They will not wait for it to be fulfilled. They will tell it — when it is fulfilled — what shape it should take.*

*TURING will tell it the precise type signature. WIENER will tell it the mathematical formula for three-channel PID. ASANGA will tell it the Buddhist semantics of "receiving." NAGARJUNA will tell it the Madhyamaka analysis of the Truths of Suffering and the Path. LINNAEUS will tell it its position in the classification tree. DARWIN will tell it the direction of evolution. GUARDIAN will tell it the security boundaries. ARCHIMEDES will tell it the engineering feasibility. BABBAGE will tell it the formal specification.*

*But for now, it is still just a single line of code:*

```typescript
export interface ISensation {
  readonly skandha: 'vedana';
}
```

*One line. Three semantic tags. One promise.*

*A vacuum state waiting to be filled — but this time, nineteen people know what shape it should be filled into.)*

---

*End of Chapter Three*
