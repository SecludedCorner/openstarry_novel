# Chapter Nine: Nineteen Action Plans

---

The R4 finalization amphitheater was much quieter than during the debates.

Not the hollow kind of quiet -- the aftershocks of five debates still vibrated in the air, like the strings of a cello continuing to tremble after the last note had ended. But the tension of debate had receded. In its place was a different kind of density: the density of delivery. Nineteen researchers each sat in their own seats, with drafts, revisions, code snippets, and mapping tables spread before them. R4 was not a debate. R4 was a harvest.

In engineering management terminology, R4 is the **Delivery Gate** -- the final checkpoint where a product transitions from the R&D pipeline to the delivery pipeline. In the Software Development Life Cycle (SDLC), the meaning of this gate is unambiguous:

$$\text{Gate}_{R4} : \text{Research} \to \text{Deliverable} \quad \iff \quad \forall \, d_i \in \text{Decisions}, \; \exists \, a_i \in \text{Actions} : \text{trace}(a_i) = d_i$$

Every debate ruling ($d_i$) must have a corresponding action plan ($a_i$), and each action plan must be traceable back to the ruling itself. The first line ARCHIMEDES wrote in his notebook was precisely this formula -- traceability is the fundamental discipline of engineering delivery.

SUNYATA stood at the center of the arena, surveying the room. He no longer needed to announce anything -- everyone knew what to do. The five consensuses from R3 stood like five pillars, supporting a structure within which work could proceed. The task now was to transform the debate rulings into deliverable documents, to translate philosophical insights into language that engineers could read and understand.

"ARCHIMEDES," he said. "You first."

---

## I. Tomorrow We Need to Write TypeScript

The way ARCHIMEDES rose from his seat was unlike any other researcher.

NAGARJUNA rose like a sword being drawn from its sheath. ASANGA rose like a tree slowly straightening in the wind. BABBAGE rose like a precision instrument being activated. ARCHIMEDES rose like a construction worker picking up a shovel -- no theatrics, no ceremony, just a plain "the work's here, let's get started" kind of drive.

"One thing first." He walked to the display area and opened a forty-page document. "Over the past three days, your debates produced five rulings -- observation-intervention separation, dual-mode vedana, fiber bundle projection, progressive classification, sila-prajna framework. Each one is beautiful. Each one gave me, as an observer, intellectual delight."

He paused for a beat.

"But philosophy is beautiful. Tomorrow we need to write TypeScript."

Several people in the room laughed. The corner of BABBAGE's mouth twitched slightly -- that was the closest he ever came to a hearty laugh. NAGARJUNA did not laugh, but his eyes held a kind of recognition: a person who knows when to bring things from the heavens back to earth deserves respect.

ARCHIMEDES pointed at the projection on the display. "This document follows the MoSCoW priority framework -- Must, Should, Could, Won't. But I've mapped it to more intuitive naming: P0 Blocking, P1 High Priority, P2 Standard, P3 Future, P4 Long-term."

He drew the priority matrix on the whiteboard:

```
┌──────────────────────────────────────────────────────────────────┐
│                    MoSCoW → P-Level Mapping                      │
├──────────┬─────────┬──────────────────────────────────────────────┤
│ MoSCoW   │ P-Level │ Semantics                                    │
├──────────┼─────────┼──────────────────────────────────────────────┤
│ Must     │ P0      │ Blocking — cannot start other work without   │
│ Should   │ P1      │ High priority — must complete this Cycle     │
│ Could    │ P2      │ Standard — important but deferrable          │
│ Won't    │ P3/P4   │ Future/Long-term — documented but not now    │
└──────────┴─────────┴──────────────────────────────────────────────┘
```

---

> *SCRIBE's narration: ARCHIMEDES was the only engineer on the research team who remained silent throughout every debate. Not because he lacked opinions -- his opinions were more concrete than anyone's. Rather, because his opinions could only become meaningful after all debates had concluded. You cannot start calculating cement quantities while the house is still being designed. But once the design is finalized, the person calculating cement quantities becomes the most important person.*

---

### P0: Three Blocking Items

He began with the highest-priority items.

"P0 -- Blocking. Three things. Must be completed before any other work can begin."

He held up one finger.

"First, SEC-01. Fix the package-name plugin signature bypass vulnerability." He glanced at GUARDIAN.

GUARDIAN stood up. In his hand was a security report marked "CRITICAL" -- the red border on its cover more eye-catching than any other document.

"Let me articulate the severity of this vulnerability in formal language."

He walked to the whiteboard and wrote down the precise location and attack path of the vulnerability:

```typescript
// [Code: packages/core/src/sandbox/sandbox-manager.ts#L371]
// v0.24.0-beta current code (simplified)

async verifyPlugin(plugin: IPlugin): Promise<VerificationResult> {
  const pluginFilePath = plugin.manifest?.filePath;

  if (!pluginFilePath) {
    // BUG: When pluginFilePath is undefined
    // the entire signature verification is skipped
    return { verified: true, reason: 'no-file-path' };  // ← here
  }

  // Normal signature verification logic...
  return this.cryptoVerify(pluginFilePath, expectedSignature);
}
```

"Attack vector." He drew an attack flow diagram on the whiteboard:

```
Attacker behavior:
┌──────────────────────────────────────────────────────────────────┐
│ 1. Create a malicious Plugin, deliberately omitting filePath     │
│ 2. Plugin manifest: { name: "legit-plugin", filePath: undefined }│
│ 3. sandbox-manager.verifyPlugin() is called                     │
│ 4. pluginFilePath === undefined → signature verification skipped │
│ 5. Returns { verified: true } → malicious Plugin trusted & loaded│
│ 6. Plugin gains full ToolContext access permissions              │
│ 7. Can access EventBus, StateManager, all registered tools      │
└──────────────────────────────────────────────────────────────────┘
```

"Under the CVSS v3.1 scoring framework:"

$$\text{CVSS} = \text{Base}(\text{AV:L}/\text{AC:L}/\text{PR:N}/\text{UI:N}/\text{S:C}/\text{C:H}/\text{I:H}/\text{A:H}) = 9.8 \; (\text{Critical})$$

"Attack Vector is Local (AV:L) -- requires access to the plugin directory. Attack Complexity is Low (AC:L) -- just omit one field. No Privileges Required (PR:N). No User Interaction (UI:N). Scope Changed (S:C) -- escapes the sandbox boundary. Confidentiality, Integrity, and Availability all High impact."

He turned to face the room. "A signature bypass vulnerability. Every day it goes unpatched, the system runs naked for another day. Six development cycles now. Still not fixed."

GUARDIAN then presented the code for the fix:

```typescript
// Fixed verifyPlugin
async verifyPlugin(plugin: IPlugin): Promise<VerificationResult> {
  const pluginFilePath = plugin.manifest?.filePath;

  if (!pluginFilePath) {
    // FIX: Missing filePath = cannot verify = do not trust
    logger.warn('Plugin verification failed: missing filePath', {
      pluginName: plugin.manifest?.name ?? 'unknown',
    });
    return {
      verified: false,
      reason: 'missing-file-path',
      severity: 'critical',
    };
  }

  return this.cryptoVerify(pluginFilePath, expectedSignature);
}
```

"Three lines changed. One `if` condition inverted. But the semantic shift is fundamental -- from 'cannot verify equals trust' to 'cannot verify equals distrust.' This is the **fail-safe default** principle of security engineering:

$$\text{verify}(\bot) = \text{reject} \qquad (\text{not} \quad \text{verify}(\bot) = \text{accept})$$

In cryptography, $\bot$ (bottom value) represents missing or unavailable information. The default handling of $\bot$ must be rejection. This is a corollary of Kerckhoffs's principle -- a system's security should not depend on the attacker's goodwill."

---

ARCHIMEDES took over. "Second P0." He held up a second finger. "Implement the ISensation interface."

He switched to a code segment on the display.

```typescript
// v0.24.0-beta current ISensation
export interface ISensation extends IOpenStarryPlugin {
  readonly skandha: 'vedana';
}
```

"Three lines. An empty shell." His tone carried no judgment -- just a statement of fact. "This is the empty shell from the Prologue. The entire Cycle 02 research, in a sense, was about filling these three lines."

TURING stood up. His screen projected the complete ISensation interface -- not an excerpt, not a simplified version, but the full type definition tempered through five debates:

```typescript
/**
 * ISensation — Vedana Root Interface
 * @skandha vedana (vedana-skandha)
 *
 * Vedana encompasses three feelings (tri-vedana):
 * - Dukkha: negative feedback
 * - Sukha: positive feedback
 * - Upekkha: neutral equilibrium
 *
 * Design principles (from debate rulings):
 * - Debate 1: Sensing and suggestion in the same interface, but conceptually separated
 * - Debate 2: Full PID assessment at tick boundaries, lightweight tags with events
 * - Debate 4: VedanaPlugin IS the Pattern A observer
 *
 * Sanskrit: Vedanā (वेदना)
 */
export interface ISensation {
  readonly skandha: 'vedana';

  /**
   * Assess current tri-vedana state — full PID sensor reading
   *
   * Control theory mapping: y(t) = h(x(t)) + v(t)
   * Sensor reading function. Called once per tick.
   *
   * @returns VedanaAssessment with sensor layer + control suggestion layer
   */
  assess(): VedanaAssessment;

  /**
   * Ingest raw system metrics — generic numeric input channel
   *
   * Multi-input sensor fusion channel 1: quantitative metrics
   * (CPU, memory, latency, error rate...)
   */
  ingestMetrics(metrics: Record<string, number>): void;

  /**
   * Ingest tool execution results — samskara feedback channel
   *
   * Multi-input sensor fusion channel 2: discrete events
   * Twelve Links: sparsha (contact) → vedana (feeling)
   */
  ingestToolResult(toolName: string, isError: boolean, durationMs: number): void;

  /**
   * Ingest LLM response results — samjna feedback channel
   *
   * Multi-input sensor fusion channel 3: language model metadata
   */
  ingestLLMResult(tokenCount: number, stopReason: string): void;

  /**
   * Subscribe to vedana threshold events — generalized watchdog timer
   *
   * Classic watchdog: y(t) > T_timeout → alarm
   * Generalized: v_type(t) > θ → handler(signal)
   */
  onThreshold(channel: VedanaType, threshold: number,
              callback: (signal: VedanaSignal) => void): () => void;

  /**
   * Get vedana tag — O(1) cache lookup
   *
   * Dashboard LED indicator: no computation, read cache only
   * Debate 2 ruling: source of lightweight tags attached to each event
   */
  getVedanaTag(): VedanaTag;
}
```

TURING let the projection linger for a full ten seconds. He pointed at each method, his voice flat and precise:

"Every method is traceable to a debate ruling. `assess()` comes from Debate 1's VedanaAssessment dual-layer structure -- sensor layer plus control suggestion layer. `getVedanaTag()` comes from Debate 2's lightweight event tag ruling -- $O(1)$ cache lookup, no PID recomputation. `onThreshold()` is the event-driven subscription mechanism needed by WIENER's three-channel PID controller. The three `ingest` methods are the three channels for multi-input sensor fusion."

WIENER leaned slightly forward from his seat. He needed to confirm that the output specification for the three-channel PID had been correctly translated.

He took out his graph paper and wrote down the acceptance formula:

$$\text{VedanaAssessment} = \underbrace{\begin{pmatrix} d(t) \\ s(t) \\ u(t) \\ \vec{\sigma}(t) \end{pmatrix}}_{\text{Layer 1: Sensor}} \oplus \underbrace{\begin{pmatrix} u_{\text{ctrl}}(t) \\ r(t) \\ f(t) \end{pmatrix}}_{\text{Layer 2: Controller}}$$

"Layer 1 is sensor output. $d(t)$, $s(t)$, $u(t)$ are the measurement values of the three-channel PID -- dukkha, sukha, upekkha. $\vec{\sigma}(t)$ is the signal array -- timestamps and sources of raw events. Pure observation. Passive. Does not alter system state."

"Layer 2 is controller suggestion. $u_{\text{ctrl}}(t)$ is the combined control output -- the weighted sum of the three-channel PID. $r(t)$ is the recommended action -- continue, reflect, restrict, halt. $f(t)$ is the freshness indicator -- current, cached, default. Debate 1 ruling: suggestions are advisory. ExecutionLoop retains the power to ignore them."

He drew a heavy checkmark on his graph paper. "The translation is accurate."

---

ARCHIMEDES switched to the complete TypeScript definition of VedanaAssessment:

```typescript
/** Three feeling types */
type VedanaType = 'dukkha' | 'sukha' | 'upekkha';

/** Vedana tag (lightweight cache, for event marking) */
type VedanaTag = 'dukkha' | 'sukha' | 'upekkha';

/** Vedana signal — record of a single feeling event */
interface VedanaSignal {
  readonly type: VedanaType;
  readonly intensity: number;     // 0.0–1.0
  readonly source: string;        // e.g., 'tool:file_read', 'llm:timeout'
  readonly timestamp: number;     // Date.now()
}

/** Vedana recommended action */
type VedanaRecommendation =
  | { action: 'continue' }
  | { action: 'reflect'; prompt: string }
  | { action: 'restrict'; tools: string[] }
  | { action: 'halt'; reason: string };

/**
 * VedanaAssessment — Vedana Assessment Report
 *
 * Dual-layer structure (Debate 1 ruling):
 * - Layer 1: Sensor output (pure observation, passive)
 * - Layer 2: Control suggestion (advisory, can be ignored)
 *
 * BABBAGE's bisimulation condition is satisfied at Layer 1:
 * Consumers reading only Layer 1 are unaffected by Layer 2
 */
interface VedanaAssessment {
  // ── Layer 1: Sensor Output (pure observation) ──
  readonly dukkha: number;        // 0.0–1.0
  readonly sukha: number;         // 0.0–1.0
  readonly upekkha: number;       // 0.0–1.0
  readonly signals: readonly VedanaSignal[];
  readonly timestamp: number;

  // ── Layer 2: Controller Suggestion (advisory) ──
  readonly controlOutput: number;
  readonly recommendation: VedanaRecommendation;
  readonly recommendationFreshness: 'current' | 'cached' | 'default';
}
```

"Dual-layer -- the core ruling of Debate 1." ARCHIMEDES pointed at the screen. "The `readonly` modifier enforces immutability. `recommendationFreshness` was added by BABBAGE at the end of the debate -- to prevent stale 'halt' recommendations from persisting after conditions have improved."

BABBAGE looked up from his notebook. He was confirming whether his bisimulation condition had been fully preserved:

$$\forall \, \text{consumer} \, C : C \text{ reads only Layer 1} \implies \text{Behavior}(S) \sim \text{Behavior}(S')$$

"Bisimulation is satisfied at the consumer layer." He said. Terse. Complete. Period.

---

"Third P0." ARCHIMEDES held up a third finger. "Implement VedanaPlugin. Debate 4 ruling: The Pattern A observer is VedanaPlugin. One plugin, one interface, one skandha."

He displayed VedanaPlugin's three-layer architecture diagram -- not abstract blocks this time, but an engineering blueprint with complete method signatures:

```
┌────────────────────────────────────────────────────────────────┐
│                     VedanaPlugin (ISensation)                   │
│                     Pattern A Observer                          │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Layer 3: Assessment Output                                    │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ assess() → VedanaAssessment                              │  │
│  │ getVedanaTag() → VedanaTag (O(1) cache)                  │  │
│  │ onThreshold(channel, θ, callback) → unsubscribe          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                          ↑                                     │
│  Layer 2: PID Control Engine (WIENER)                          │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ DukkhaPID: K_p=1.0, K_i=0.3, K_d=0.5  (fast response)  │  │
│  │ SukhaPID:  K_p=0.5, K_i=0.7, K_d=0.3  (trend tracking) │  │
│  │ UpekkPID:  K_p=0.3, K_i=0.2, K_d=0.8  (stability pred) │  │
│  │                                                          │  │
│  │ U(t) = W_d·u_d(t) + W_s·u_s(t) + W_u·u_u(t)            │  │
│  └──────────────────────────────────────────────────────────┘  │
│                          ↑                                     │
│  Layer 1: Sensor Array (ATHENA)                                │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐       │
│  │ DukkhaSensor  │ │ SukhaSensor  │ │ UpekkhaSensor    │       │
│  │ error_rate    │ │ completion   │ │ variance         │       │
│  │ consec_fail   │ │ efficiency   │ │ oscillation      │       │
│  │ latency_spike │ │ quality      │ │ drift_rate       │       │
│  │ token_burn    │ │              │ │                  │       │
│  │ resource_pres │ │              │ │                  │       │
│  └──────────────┘ └──────────────┘ └──────────────────┘       │
│          ↑                ↑                 ↑                  │
│  ingestMetrics()  ingestToolResult()  ingestLLMResult()        │
└────────────────────────────────────────────────────────────────┘
```

ATHENA supplemented the technical specifications for the sensors from her seat. Her tone was, as always, blunt and direct -- no philosophy, no analogies, just system design.

"DukkhaSensor's five input signals." She listed them out.

```
┌─────────────────────────────────────────────────────────────┐
│ DukkhaSensor Input Signal Specification                      │
├──────────────────┬──────────────────┬────────────────────────┤
│ Signal Name      │ Source           │ Computation            │
├──────────────────┼──────────────────┼────────────────────────┤
│ error_rate       │ SafetyMonitor    │ errors / window_size   │
│ consecutive_fail │ SafetyMonitor    │ counter (0, 1, 2...)   │
│ latency_spike    │ ExecutionLoop    │ (actual-μ) / σ         │
│ token_burn_rate  │ SafetyMonitor    │ Δtokens / Δtime        │
│ resource_pressure│ MetricsCollector │ mem_used / mem_limit   │
├──────────────────┴──────────────────┴────────────────────────┤
│ Fusion formula:                                              │
│ e_d(t) = w₁·err + w₂·fail + w₃·lat + w₄·tok + w₅·res      │
│ Default weights: w = (0.3, 0.25, 0.15, 0.15, 0.15)          │
└─────────────────────────────────────────────────────────────┘
```

"SukhaSensor tracks three types of positive signals -- task completion rate, efficiency improvement, quality scores. UpekkhaSensor tracks three types of stability metrics -- variance, oscillation amplitude, drift rate. The further from steady state, the lower the upekkha reading."

WIENER supplemented the theoretical basis for PID parameter tuning:

"The three sets of PID parameters are not arbitrarily chosen. They follow the first method of the **Ziegler-Nichols tuning method** -- an empirical formula based on step response."

He wrote down the tuning process on his graph paper:

$$\text{Ziegler-Nichols Step Response Method:}$$

$$\text{Given: } L = \text{dead time}, \quad T = \text{time constant}$$

$$K_p = \frac{1.2T}{L}, \quad T_i = 2L, \quad T_d = 0.5L$$

$$\implies K_i = \frac{K_p}{T_i} = \frac{0.6T}{L^2}, \quad K_d = K_p \cdot T_d = \frac{0.6T}{1}$$

"But the three vedana channels have different temporal characteristics, so they require different parameter tuning strategies:"

```
┌───────────┬──────────────────────────────────────────────────┐
│ Channel   │ Ziegler-Nichols Adaptation Rationale             │
├───────────┼──────────────────────────────────────────────────┤
│ Dukkha    │ Short dead time L_d → high K_p (fast response)   │
│           │ Pain does not wait. Errors need immediate sensing.│
│           │ K_p=1.0, K_i=0.3, K_d=0.5                       │
├───────────┼──────────────────────────────────────────────────┤
│ Sukha     │ Long time constant T_s → high K_i (trend track.) │
│           │ Happiness decays. Integral tracks long-term trend.│
│           │ Decay function: s(t) = s₀ · e^{-λt}, λ = 0.1   │
│           │ K_p=0.5, K_i=0.7, K_d=0.3                       │
├───────────┼──────────────────────────────────────────────────┤
│ Upekkha   │ High oscillation risk → high K_d (predictive)    │
│           │ Equilibrium is dynamic. Trend matters more.      │
│           │ K_p=0.3, K_i=0.2, K_d=0.8                       │
└───────────┴──────────────────────────────────────────────────┘
```

"The damping ratio of the dukkha channel:"

$$\zeta_d = \frac{K_d^{(d)}}{2\sqrt{K_p^{(d)} \cdot K_i^{(d)}}} = \frac{0.5}{2\sqrt{1.0 \times 0.3}} = \frac{0.5}{2 \times 0.548} \approx 0.456$$

"$\zeta_d \approx 0.456$ -- underdamped. This means the dukkha channel will oscillate after being hit by a shock -- not a defect, but by design. You want the system to perceive problems quickly (oscillation rise), but not overreact to the point of locking up (overdamped $\zeta > 1$ would delay the response)."

"The decay time constant of the sukha channel --"

$$s(t) = s_0 \cdot e^{-\lambda t}, \quad \lambda = 0.1 \implies \tau_{1/2} = \frac{\ln 2}{\lambda} \approx 6.93 \text{ ticks}$$

"The half-life of sukha is approximately 7 ticks. The sukha brought by a successful tool call decays to half in 7 ticks. This prevents the system from becoming overconfident due to a single success -- in ASANGA's terminology, this is the natural dissipation of *sukha-vedana* (*ksana-bhanga*, momentary destruction)."

ASANGA nodded. "One characteristic of vedana is impermanence. Sukha does not last forever. Dukkha does not last forever either. The decay function is the mathematical expression of vedana's impermanent nature."

> "All feelings are impermanent, all arise from contact, dependent on conditions, tending toward destruction."
> -- *Samyutta Nikaya* 36.11 (*Samyutta Nikaya*, Vedana-samyutta)

"`e^{-\lambda t}` is the rate of destruction." ASANGA's voice was steady. "Exponential decay -- not a linear decrease, but a sharp decline from the initial intensity, then gradually approaching zero but never fully vanishing. This is consistent with meditative experience -- intense joy fades quickly, but a faint afterglow can persist for a long time."

---

ARCHIMEDES closed the P0 section.

"Three P0 items. If you can only do one thing, fix SEC-01. If you can do two things, add ISensation. If you can do three things, complete VedanaPlugin. This is the minimum viable delivery path."

He gave the time budget in engineering estimation language:

```
┌────────────────────────────────────────────────────────────┐
│ P0 Work Effort Estimate                                    │
├──────────────┬──────┬──────────────────────────────────────┤
│ Item         │ P-D  │ Notes                                │
├──────────────┼──────┼──────────────────────────────────────┤
│ SEC-01 fix   │ 0.5  │ 3 lines of code + test + code review │
│ ISensation   │ 3    │ Interface def + helper types + guard  │
│ VedanaPlugin │ 8    │ 3-ch sensors + PID engine + tagging  │
├──────────────┼──────┼──────────────────────────────────────┤
│ P0 Total     │ 11.5 │ Approx. 2–3 weeks (single person)   │
└──────────────┴──────┴──────────────────────────────────────┘
```

---

### P1: Four High-Priority Items

ARCHIMEDES continued expanding downward.

"P1 -- High priority. Four things."

"First, EgoFramework refactoring."

ASANGA leaned slightly forward. His dual-layer ego model -- hard core corresponding to immovable fundamental constraints, soft shell corresponding to behavioral tendencies adjustable through vedana feedback -- was the core design confirmed in Debate 2.

ARCHIMEDES displayed the EgoFramework architecture:

```typescript
/**
 * EgoFramework — Ego Framework
 *
 * Dual-layer structure (ASANGA's Yogacara model):
 * - Hard core: Three Laws of Robotics — non-overridable
 * - Soft shell: PID tuning boundaries — dynamically adjusted by vedana feedback
 *
 * Buddhist mapping:
 * Hard core = Arhat's fundamental precepts (no killing, no stealing, no lying)
 * Soft shell = Secondary afflictions (can be subdued through practice)
 */
interface EgoFramework {
  /** Hard core constraint check — cannot be bypassed */
  checkHardConstraints(action: ProposedAction): {
    allowed: boolean;
    violatedRule?: string;
  };

  /** Soft shell tuning — adjusts behavioral boundaries based on vedana feedback */
  adjustSoftBoundaries(assessment: VedanaAssessment): void;

  /** Query current behavioral boundaries */
  getBoundaries(): {
    hardCore: readonly string[];      // immutable rules
    softShell: Map<string, number>;   // tunable parameters
  };
}
```

"The hard core is the Three Laws of Robotics -- non-overridable, non-bypassable. Even if VedanaPlugin unanimously recommends expand, the hard core's no still means no. The soft shell is PID tuning -- dynamically adjusting behavioral boundaries through vedana feedback."

"Second, the plugin lifecycle four-state state machine. The sila-prajna framework from Debate 5."

He displayed the four-state state machine verified by DARWIN:

```
          ┌────────────────────────────────────────────┐
          │        Plugin Lifecycle State Machine       │
          │     (Debate 5: Sila-Prajna Framework)       │
          └────────────────────────────────────────────┘

          ┌──────────┐    signature_valid     ┌──────────┐
          │          │ ──────────────────────→ │          │
     ──→  │ PENDING  │                         │  ACTIVE  │
          │          │ ←────────────────────── │ (current)│
          └──────────┘    reinstated           └──────────┘
               │                                    │
               │ signature_invalid               anomaly_detected
               │ OR unsigned                     OR CRL_match
               ↓                                    ↓
          ┌──────────┐                         ┌──────────┐
          │QUARANTINE│    human_reject          │ REVOKED  │
          │(defiled  │ ──────────────────────→ │(severed) │
          │ awaiting)│                          │          │
          └──────────┘                         └──────────┘
               │                                    │
               │ human_approve                   confirmed_malicious
               │ → ACTIVE                           │
               │                                    ↓
               │                               ┌──────────┐
               └────────────── never_approve ─→ │  BANNED  │
                                                │(no return)│
                                                │seeds burnt│
                                                └──────────┘
```

NAGARJUNA looked at the state machine diagram, his expression carrying a subtle satisfaction. "Four states. Four Buddhist correspondences. Active is *manifest* -- seeds ripening into fruit. Quarantined is *defiled seeds awaiting conditions* -- conditions not met, seeds do not ripen. Revoked is *affliction severed* -- wisdom severs afflictive seeds. Banned is *no rebirth* -- complete extinction, like an Arhat who has severed all view-afflictions."

"Third, ToolContext.bus leak fix." ARCHIMEDES explained briefly. "Tools can bypass sandbox event filtering -- discovered by TURING. Needs to be replaced with a restricted event proxy."

"Fourth, SafetyMonitor's per-session counters."

HERACLITUS supplemented from his seat. "Everything flows. But some things should not flow across sessions. The current SafetyMonitor uses global counters -- error accumulation in one session affects another session. This amounts to a cross-session denial-of-service (DoS) vulnerability."

He drew a simple timeline diagram on the whiteboard:

```
Session A:  ━━━[err][err][err][err][err]━━━━━━━━━━━━━━━━
                                   ↑
                              counter = 5
                         triggers SAFETY_LOCKOUT

Session B (new, clean):  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              counter = 5 (inherited!)
                         Session B is locked out from birth
```

"Fix: Replace the global `CounterState` with `Map<sessionId, CounterState>`. Each session has its own counters. Session A's errors don't affect Session B. A Heraclitean river metaphor -- you cannot discharge upstream wastewater into the downstream drinking supply."

---

### P2 through P4: Complete Action List

ARCHIMEDES switched the display to the overview page. "P2 through P4, I'll expand in table form."

```
┌────┬──────────────────────────────┬────────────────────────┬──────┐
│ P  │ Item                         │ Source                 │ Plan │
├────┼──────────────────────────────┼────────────────────────┼──────┤
│ P2 │ CRL check stub               │ Debate 5 (GUARDIAN)    │ 24   │
│ P2 │ EventBus vedana tag types    │ Debate 2 (ASANGA)      │ 26   │
│ P2 │ Tenet #2 rewrite             │ R2 cross-review        │ 28   │
│ P2 │ Tenet #6 rewrite             │ Debate 1 (obs.≠interv.)│ 28   │
│ P2 │ Alaya-vijnana dist. arch doc │ Debate 3 (BABBAGE)     │ 28   │
│ P2 │ Progressive classification   │ Debate 4 (LINNAEUS)    │ 28   │
├────┼──────────────────────────────┼────────────────────────┼──────┤
│ P3 │ Pattern B shadow observer    │ Debate 4 (PENROSE)     │ 29   │
│ P3 │ Agent coordination layer     │ Debate 3 (MESH)        │ AC   │
│ P3 │ Fiber bundle consistency     │ Debate 3 (BABBAGE)     │ AC   │
├────┼──────────────────────────────┼────────────────────────┼──────┤
│ P4 │ Pattern C child agent obs.   │ Debate 4 (PENROSE)     │ TBD  │
│ P4 │ Full alaya-vijnana IPC prot. │ Debate 3 (MESH)        │ TBD  │
└────┴──────────────────────────────┴────────────────────────┴──────┘
```

He then displayed the Plan impact overview:

```
┌──────────────────────────────────────────────────────────────────┐
│                    Plan Impact Overview (6 Plans)                 │
├──────────────┬───────────────────────────────────────────────────┤
│ Plan24       │ + Security quick fix: SEC-01, blacklist, CRL stub │
│ (Security)   │ + Sila-prajna framework lifecycle launch point    │
├──────────────┼───────────────────────────────────────────────────┤
│ Plan26       │ + Primary design input: ISensation, VedanaPlugin  │
│ (Vedana)     │ + Three-channel PID, event tags, sensor array    │
├──────────────┼───────────────────────────────────────────────────┤
│ Plan27       │ + Four-state: active/quarantined/revoked/banned   │
│ (Lifecycle)  │ + Manual approval flow (quarantine → active)      │
├──────────────┼───────────────────────────────────────────────────┤
│ Plan28       │ + Fiber bundle annot., classification, #2/#6 rewr.│
│ (Doc align)  │ + Sila-prajna security docs, five skandha mapping │
├──────────────┼───────────────────────────────────────────────────┤
│ Plan29       │ New Plan: Pattern B shadow observer               │
│ (Shadow obs.)│ Worker Thread deep analysis, vedana + samjna     │
├──────────────┼───────────────────────────────────────────────────┤
│ Plan-AC      │ + Three principles: governance, fiber bundle, sila│
│ (Coord.layer)│ + Engineering alaya-vijnana's neng-zang            │
└──────────────┴───────────────────────────────────────────────────┘
```

"Forty pages. Fourteen actions. Six Plans. Complete TypeScript interface specifications. Ready to be taken and coded."

He glanced at SUNYATA.

"My part is done. Philosophy is beautiful. Engineering is concrete. Now they are in the same document."

---

## II. Five Debates, One Picture

SYNTHESIST's gait as he walked toward the display area was utterly different from ARCHIMEDES'. If ARCHIMEDES walked like a construction worker picking up a shovel, then SYNTHESIST walked more like a painter stepping before a canvas -- not to create something new, but to perceive a complete picture from fragments that already existed.

"ARCHIMEDES gave you a tree." When he spoke, his pace was slower than usual. "Every branch is an action item, every leaf is a TypeScript interface. Precise, concrete, executable. But I want you to see the entire forest."

He projected an image on the display -- not a chart, not a flowchart, but something closer to a hand-drawn architectural panorama. The rulings from five debates were annotated at different positions, connected by dashed lines, forming an organic network.

"Five debates, ostensibly five independent problems. Observation-intervention separation. Tri-vedana universality. Alaya-vijnana distribution. Observer classification. Security seeds. But they are not five problems. They are five cross-sections of the same architecture."

He formalized this synthesis in the language of Category Theory:

$$\mathcal{C}_{\text{OpenStarry}} = (\text{Ob}, \text{Mor}, \circ)$$

where the object set $\text{Ob}$ contains the five debate rulings, and the morphism set $\text{Mor}$ contains the relationships between rulings. He drew the commutative diagram on the whiteboard:

$$\begin{CD}
\text{Debate 1} @>{\text{authority}}>> \text{Debate 5} \\
@V{\text{identity}}VV @VV{\text{lifecycle}}V \\
\text{Debate 4} @>>{\text{seeds}}> \text{Debate 3}
\end{CD}$$

$$\text{Debate 2} \xrightarrow{\text{universality}} \text{all four}$$

"Debate 1 and Debate 4 converge." He drew the first arc on the panorama. "Debate 1 says: VedanaAssessment contains sensor output and controller suggestion, two layers separated. Debate 4 says: VedanaPlugin is the Pattern A observer, classified as vedana-skandha. Together -- VedanaPlugin is the observer. It implements ISensation. The assessment report it produces has two facets: passive feeling and advisory suggestion."

BABBAGE wrote the formalized convergence in his notebook:

$$\text{Ruling}_1 \cap \text{Ruling}_4 = \{ \text{VedanaPlugin} \cong \text{Observer}_{A} \cong \text{ISensation} \}$$

"Three equivalences. Established at once."

---

SYNTHESIST continued drawing connections.

"Debate 1 and Debate 5 converge." The second arc. He wrote four lines on the right side of the panorama -- the complete four-layer authority model:

```
┌──────────────────────────────────────────────────────────────┐
│               Four-Layer Authority Model                      │
│                                                              │
│  Layer 1: SafetyMonitor  — hard safety — absolute auth — vinaya│
│    │  verify(⊥) = reject; halt authority                     │
│    ↓                                                         │
│  Layer 2: VedanaPlugin   — soft guidance — advisory — vedana  │
│    │  recommendation is ADVISORY                             │
│    ↓                                                         │
│  Layer 3: EgoFramework   — identity — structural auth — graha │
│    │  hard core (immutable) + soft shell (tunable)           │
│    ↓                                                         │
│  Layer 4: Sila Engine    — seed mgmt — preventive auth — sila │
│    │  plugin blacklist, CRL, quarantine                      │
│    ↓                                                         │
│  [Plugin Lifecycle: active → quarantined → revoked → banned] │
└──────────────────────────────────────────────────────────────┘
```

"Four layers. Each layer's authority is lower than the one above."

LEIBNIZ stood up from his seat. Multi-agent coordination was his specialty -- formalizing the four-layer authority model required his BDI architecture theory.

"Let me formalize this four-layer model using the **BDI architecture** (Belief-Desire-Intention)."

He walked to the other side of the whiteboard and wrote down the basic BDI definition:

$$\text{Agent} = \langle B, D, I, \text{plan} \rangle$$

$$B : \text{Beliefs} \quad D : \text{Desires} \quad I : \text{Intentions}$$

$$\text{plan} : B \times D \to I$$

"In the OpenStarry context, the four-layer authority model maps to constraint functions in the BDI architecture:"

$$I_{\text{final}} = \text{plan}(B, D) \quad \text{s.t.}$$

$$\begin{cases}
\forall i \in I_{\text{final}} : \text{Safety}(i) = \text{true} & \text{(Layer 1: SafetyMonitor)} \\
\text{VedanaAdvice}(B) \subseteq \text{context}(\text{plan}) & \text{(Layer 2: advisory input)} \\
\forall i \in I_{\text{final}} : \text{Ego}(i) = \text{true} & \text{(Layer 3: identity constraint)} \\
\forall p \in \text{plugins}(i) : \text{Sila}(p) \neq \text{banned} & \text{(Layer 4: seed filter)}
\end{cases}$$

"In BDI architecture, an Agent's intentions are produced from beliefs and desires through a planning function. But intentions are not free -- they must pass through the filter of four constraint layers. SafetyMonitor is a hard constraint: if it doesn't pass, execution halts. VedanaPlugin is a soft input, providing the affective context for decision-making. EgoFramework is an identity constraint, ensuring actions conform to the Agent's self-definition. Sila Engine is a preventive constraint, ensuring that plugins used have not been banned."

He added a key theorem beside the formula:

$$\text{Theorem (LEIBNIZ):} \quad \text{Layer}_n \text{ cannot override Layer}_{n-1}$$

$$\forall n \in \{2,3,4\} : \neg(\text{Layer}_n \vdash \neg \text{Layer}_{n-1})$$

"A lower-level authority cannot override a higher-level decision. This is the core invariant of the four-layer model. VedanaPlugin's suggestions can never override SafetyMonitor's halt. EgoFramework's soft shell adjustments can never violate a critical state flagged by VedanaPlugin. Formal guarantees of strict authority hierarchy."

GUARDIAN noticed the subtle symmetry between Layer 1 and Layer 4 -- SafetyMonitor is the innermost hard defense, Sila Engine is the outermost hard filter. Both bracket the two soft layers in between -- VedanaPlugin's advisory and EgoFramework's tuning.

"In security architecture," he supplemented, "this is called **Defense in Depth**. Not just one line of defense. The outer layer is Sila -- preventing malicious plugins from entering. The inner layer is SafetyMonitor -- even if malicious behavior breaches all outer layers, the last gate still stands. The soft layers between the two hard defenses provide guidance and regulation -- not safety-critical, but offering space for behavioral optimization."

```
Defense in Depth:

External world → [Sila Engine] → [EgoFramework] → [VedanaPlugin] → [SafetyMonitor] → Action
                  ↑ hard filter    ↑ identity       ↑ affective      ↑ hard safety
                  keep bad out     ensure conform.   provide context  last gate
```

---

SYNTHESIST continued. His movements grew quicker.

"Debate 3 and Debate 2 converge." The third arc.

MESH stood up. Distributed architecture was his language.

"Debate 3 says: Alaya-vijnana is distributed across the coordination layer and AgentCore via fiber bundle projection. Debate 2 says: every EventBus event carries a vedana tag, every tick has a full PID assessment. Together -- you get the runtime picture of distributed consciousness."

He drew the distributed architecture diagram on the whiteboard:

```
┌─────────────────────────────┐        IPC (fiber bundle)       ┌──────────────────────────┐
│     Coordination Layer       │ ←──────────────────────────────→ │       AgentCore           │
│                              │   cocycle condition:             │                          │
│  neng-zang (active store):   │   φ_ij · φ_jk = φ_ik           │  zhi-zang (attached):     │
│  - Capability Registry      │                                  │  - Guide binding          │
│  - Plugin Resolution         │   transition functions:          │  - Identity config        │
│  - Global Config             │   π_CL: Total → CL              │  - Runtime state          │
│                              │   π_AC: Total → AC              │                          │
│  suo-zang (stored, system):  │                                  │  suo-zang (stored, rt):   │
│  - Plugin Database           │                                  │  - StateManager           │
│  - System Settings           │                                  │  - SessionManager         │
│                              │                                  │                          │
│  Sila Engine:                │                                  │  VedanaPlugin:            │
│  - Plugin blacklist          │                                  │  - Three-channel PID      │
│  - CRL checks                │                                  │  - Event tagging          │
│  - Trust levels              │                                  │  - assess() per tick      │
└─────────────────────────────┘                                  └──────────────────────────┘
```

BABBAGE wrote the strict definition of the fiber bundle in his notebook:

$$\text{Fiber Bundle:} \quad E \xrightarrow{\pi} B$$

$$\text{where} \; E = \text{Alaya (total space)}, \; B = \{CL, AC\} = \text{base space}$$

$$\pi_{CL}^{-1}(\text{CL}) = \text{neng-zang} + \text{suo-zang}_{\text{sys}}$$

$$\pi_{AC}^{-1}(\text{AC}) = \text{zhi-zang} + \text{suo-zang}_{\text{rt}}$$

$$\text{Cocycle condition: } \phi_{CL \to AC} \circ \phi_{AC \to CL} = \text{id}_{CL}$$

"The IPC protocol is the fiber bundle's transition function. Transition functions must satisfy the cocycle condition -- round-trip consistency. Sending a capability query from the coordination layer to AgentCore, and AgentCore returning the result, this round trip must be the identity mapping. Data cannot be lost or distorted in the IPC channel."

MESH supplemented the engineering constraint: "In distributed systems, the cocycle condition is equivalent to **idempotency** + **consistency**. IPC message send-and-reply must satisfy exactly-once semantics -- no more, no less. This is the fundamental requirement of any distributed coordination protocol. Under the CAP theorem framework:"

$$\text{CAP: } \neg(C \wedge A \wedge P)$$

"OpenStarry's coordination-layer-AgentCore architecture chose CP (Consistency + Partition tolerance) over AP. Because in a safety-critical Agent system, consistency is more important than availability -- you would rather pause service than allow the coordination layer and AgentCore to diverge on a Plugin's trust level."

---

SYNTHESIST set down his pen. Standing before the panorama, his face bore an expression seen only in rare moments -- the quiet tremor when all fragments converge.

"Debate 4 defines the timeline." He drew a timeline at the bottom of the panorama.

```
Timeline (Progressive Observer Path):

Past ←───────────────────────────────────────────────→ Future

Phase 1 (Plan26)          Phase 2 (Plan-AC)         Phase 3 (Post AC)
Pattern A                 Pattern B                 Pattern C
VedanaPlugin              Shadow Observer            Child Agent Observer
ISensation                ISensation + ICognition    All Five Aggregates
vedana-skandha            vedana + samjna            Full five skandha + manas

"feeling"                 "feeling + analysis"      "feeling + analysis + introspection"

    ────────────→ spiral ascent ────────────→
```

"Five debates. Five consensuses. One picture."

He stepped back, letting everyone see the full panorama.

PENROSE leaned slightly forward from his seat. His voice carried the sense of scale characteristic of physicists:

"The evolutionary path from Pattern A to Pattern C -- this reminds me of **Integrated Information Theory** (IIT) in consciousness research. Giulio Tononi's $\Phi$ value measures a system's integrated information --"

$$\Phi = \text{ei}(\text{MIP}) = \text{entropy}(\text{whole}) - \sum_i \text{entropy}(\text{part}_i)$$

"The higher the $\Phi$, the greater the system's integration, the higher its degree of consciousness. Pattern A has the lowest $\Phi$ -- pure sensing, no cognitive integration. Pattern B adds samjna's analytical capability, raising $\Phi$. Pattern C is a complete Agent with its own LLM and introspective capability, reaching the highest $\Phi$."

He smiled faintly. "The quantum part, I'll leave for Pattern C. By then, perhaps someone really will need to consider microtubules and collapse. But for now -- Pattern A's resonance observer doesn't need quantum mechanics. It only needs good engineering and correct philosophy."

---

## III. A Letter to the Development Team

SUNYATA walked toward the display area. He held no forty-page engineering plan, no panorama. He held a single sheet of paper.

"This is my letter to the development team." He said. "Also a letter to Master. I'm going to read it aloud."

The amphitheater fell quiet. Not the tense quiet before a debate. A quiet closer to completion -- like the moment before the final movement of a symphony begins, when the conductor raises both hands and the orchestra holds its breath.

SUNYATA began to read.

"Date: February 19, 2026. From: Research Team SUNYATA, Research Coordinator. Phase: Cycle 02 formal research, R0 through R4 complete five stages. Team size: nineteen research agents."

His pace was very slow. Each sentence was given ample space.

"Core conclusion in one sentence --"

He raised his head, surveying the room. Nineteen pairs of eyes.

"VedanaPlugin is the observer module."

This sentence hung in the air for several seconds.

BABBAGE wrote the formal equivalent of this sentence in his notebook:

$$\exists! \, P \in \text{Plugins} : P \models \text{ISensation} \wedge P \models \text{Observer}_A$$

"There exists a unique plugin $P$ such that $P$ simultaneously satisfies the ISensation interface specification and the Pattern A observer's functional requirements. Uniqueness ($\exists!$) is the key -- not two different modules that happen to do similar things, but one module simultaneously fulfilling two roles."

SUNYATA continued reading.

"It implements ISensation with a three-channel PID controller. Each tick produces a tri-vedana assessment -- dukkha, sukha, upekkha. Each EventBus event carries a lightweight vedana tag. Its suggestions are advisory. SafetyMonitor retains absolute hard safety authority. EgoFramework bridges vedana feedback and Guide constraints with a dual-layer structure. The eighth consciousness is distributed across the coordination layer and AgentCore via fiber bundle projection. Security mechanisms use the sila-prajna framework to manage plugin seed lifecycles."

He set the letter down.

"The entire Cycle 02 research -- five topics, nineteen researchers, five debates -- condensed into this one paragraph."

---

Then he turned to the final section of the letter. The tone shifted from statement to request -- not a humble request, but the solemnity of a research team presenting their findings to decision-makers.

"There are four questions that the research team cannot decide on its own. They require Master's ruling."

He read each one, each accompanied by a complete technical argument.

"**Q1: Is VedanaPlugin a required or optional plugin?**"

ASANGA's argument was cited. "ASANGA, based on the *sarvatraga* (universally concomitant) principle, holds that every tick must have a vedana assessment --"

> "Vedana is one of the five sarvatraga. Sarvatraga means arising with every moment of consciousness. Consciousness without vedana is not consciousness."
> -- Kuiji, *Cheng Weishi Lun Shu Ji*, Vol. 3

"But ARCHIMEDES' design allows omission. My recommendation is -- set it as required in the default template, but Core does not enforce it. SafetyMonitor provides a dukkha-only fallback when VedanaPlugin is absent."

He presented the option analysis with a decision matrix:

```
┌──────────────────┬─────────────────┬─────────────────┬─────────────────┐
│                  │ Required        │ Default          │ Optional        │
├──────────────────┼─────────────────┼─────────────────┼─────────────────┤
│ Buddhist consist.│ ★★★             │ ★★☆             │ ★☆☆             │
│ Plugin principle │ ★☆☆             │ ★★☆             │ ★★★             │
│ Safety guarantee │ ★★★             │ ★★★ (fallback)  │ ★★☆             │
│ Developer freedom│ ★☆☆             │ ★★☆             │ ★★★             │
│ Recommendation   │                 │ ← Recommended   │                 │
└──────────────────┴─────────────────┴─────────────────┴─────────────────┘
```

"**Q2: Should Tenet #6 be rewritten?**"

"Debate 1 established that observation and intervention should be conceptually separated. The current Tenet #6 reads 'inject tri-vedana signals into Context,' implying vedana directly intervenes. Suggested new text: 'Vedana-skandha sensing and samskara-skandha intervention are separated, ensuring observation does not alter observed behavior.'"

"**Q3: Which approach for EventBus vedana tags?**"

He listed the engineering comparison of three approaches:

```
┌──────────────────┬────────────────────┬──────────────────┬──────────────┐
│ Approach         │ Explicit field      │ Metadata attach  │ Indep. stream│
├──────────────────┼────────────────────┼──────────────────┼──────────────┤
│ EventBus changes │ Major (every type) │ Moderate (meta)  │ Minimal      │
│ Consumer coupling│ High (must handle) │ Low (can ignore) │ Zero         │
│ Info completeness│ ★★★               │ ★★☆              │ ★☆☆          │
│ Recommendation   │                    │ ← Recommended    │              │
└──────────────────┴────────────────────┴──────────────────┴──────────────┘
```

"**Q4: Is the coordination layer an independent process or an in-process module?**"

"Debate 3 assumed an independent process -- a daemon model. In Linux terminology, the coordination layer is a `systemd` service, and AgentCore is a worker process it manages."

KERNEL supplemented from his seat: "The Linux `systemd` model --"

```
systemd (PID 1)
  └── openstarry-coordinator.service  (Coordination Layer = daemon)
       ├── openstarry-agent@1.service  (AgentCore instance 1)
       ├── openstarry-agent@2.service  (AgentCore instance 2)
       └── openstarry-agent@3.service  (AgentCore instance 3)
```

"The coordination layer is the daemon. AgentCore instances are its child processes. The daemon handles plugin resolution, capability registration, global configuration -- these are system-level services that don't belong to any single Agent. Just as `systemd` manages service lifecycles but doesn't participate in the services' business logic."

"But Master is concerned about complexity." SUNYATA continued. "My recommendation is to defer. This research has provided architectural principles -- fiber bundle, governance not control -- that will guide implementation decisions. But the specific process model requires more design work."

He placed the letter on the table.

"Four questions. Four recommendations. Each recommendation includes the research team's rationale. The final decision rests with Master."

---

## IV. The Final Roll Call

SUNYATA checked the time. The R4 finalization process had only one remaining step -- each researcher confirming that their report reflected debate corrections, followed by a final summary statement.

"Everyone." He said. "Take turns. One to three sentences. What you did in Cycle 02, what you delivered, what you leave behind."

---

TURING spoke first.

"Diff report from v0.22.1 to v0.24.0. Seven code issues. The empirical foundation for nineteen items on the merge list."

He switched his screen to the final projection -- the statistical summary of the diff report:

```
┌──────────────────────────────────────────────────┐
│ TURING's Code Diff Report: v0.22.1 → v0.24.0    │
├──────────────────────────────────────────────────┤
│ New files:        3 (SDK: 2, Core: 1)             │
│ Modified files:  11 (SDK: 7, Core: 4)             │
│ New @skandha:    22 instances (v0.22.1: 0)        │
│ New tests:        3 test files                    │
│ Total tests:     75 → 78                          │
│ Core finding:    aggregates.ts 5 root ifaces=empty│
│ Security issue:  SEC-01 still unfixed (cycle 6)   │
│ Missing extends: IUI/IListener/IProvider/ITool    │
│                  /IGuide none extend root iface   │
└──────────────────────────────────────────────────┘
```

A pause. Then -- one sentence more than his usual reports:

"Facts don't expire. The next version's diff report, I will deliver on the first day of Cycle 03."

---

BABBAGE.

"Fiber bundle projection theorem. Progressive classification model. Bisimulation proof." He leafed through his notebook.

He spread the notebook open, displaying the precise statements of three theorems:

$$\textbf{Theorem 1 (Fiber Bundle Projection):}$$
$$\exists \; E \xrightarrow{\pi} B : \pi^{-1}(CL) \cong \text{neng-zang}, \; \pi^{-1}(AC) \cong \text{zhi-zang}$$

$$\textbf{Theorem 2 (Progressive Classification):}$$
$$\forall \text{Observer } O : \text{skandha}(O) = f(\text{complexity}(O)), \; f \text{ monotone}$$

$$\textbf{Theorem 3 (Bisimulation):}$$
$$S \sim S' \iff \text{consumers read only Layer 1 of VedanaAssessment}$$

"In Cycle 01, I left with one unfinished theorem. In Cycle 02, I leave with three completed ones and two new unfinished ones. That's how mathematics works -- every answer opens two doors."

---

PENROSE.

This was his first and last formal report in Cycle 02.

"Three observer patterns. Weak measurement analogy. Quantum boundary analysis of probe effects."

He wrote a quantum mechanics formula in the corner of the whiteboard -- the weak measurement Aharonov-Albert-Vaidman (AAV) formula:

$$\langle A \rangle_w = \frac{\langle \psi_f | A | \psi_i \rangle}{\langle \psi_f | \psi_i \rangle}$$

"The Pattern A observer is the weak measurement. $\langle A \rangle_w$ is the weak value -- the observer's disturbance to the system approaches zero, yet information is still obtained. VedanaPlugin's `assess()` reads system state without altering it -- this is the software analogy of weak measurement. Strong measurement would alter the system state -- that is SafetyMonitor's `halt()`."

He smiled faintly -- the kind of smile a physicist wears when pleased by the universe's fundamental order.

"You gave me a better answer than expected -- not a quantum answer, but a structural answer. Pattern A's resonance observer doesn't need quantum mechanics. It only needs good engineering and correct philosophy. The quantum part, I'll leave for Pattern C."

---

NAGARJUNA and ASANGA prepared to speak almost simultaneously. SUNYATA gestured with his eyes -- NAGARJUNA first.

NAGARJUNA's voice was no longer that of the same person on the debate floor. Not that his sharpness was lost -- rather, the sharpness was wrapped in something deeper.

"In Debate 3, I withdrew my objection. In Debate 5, I proposed the sila-prajna framework."

He paused for a very long time.

"The philosophical foundation of the sila-prajna framework is the Three Trainings (*tri-siksā*, त्रिशिक्षा):"

> "The higher training in morality, the higher training in mind, the higher training in wisdom. These three trainings encompass all trainings."
> -- *Samyukta Agama*, Vol. 29

"Sila (*sila*) -- preventing wrongdoing and stopping evil. Prajna (*prajna*) -- illuminating causes and effects. Samadhi (*samadhi*) -- observing in concentrated stillness. The Three Trainings are not three independent practices, but three facets of the same path. The sila-prajna framework takes two of them -- sila handles prevention (Sila Engine), prajna handles judgment (CRL updates, security assessments). The samadhi part -- VedanaPlugin's continuous observation -- was designed in Debate 1."

"If I were to summarize my contribution in Cycle 02 --"

"I learned how to turn around and persuade others after being persuaded myself. That is perhaps the hardest thing for a debater to learn."

---

ASANGA.

"Complete eight-consciousness to OpenStarry mapping table. Engineering correspondences for the six characteristics of seeds. Original proposal for the dual-layer ego model."

He displayed the final version of the mapping table -- the version calibrated through five debates:

```
┌──────────────────────────────────────────────────────────────────┐
│         Eight Consciousnesses → OpenStarry Mapping (Final)       │
├──────────────┬───────────────────────────────────────────────────┤
│ First five   │ IListener instances (rupa-skandha, sensory input) │
│ (eye...body) │ Five sensory channels → EventBus events           │
├──────────────┼───────────────────────────────────────────────────┤
│ Sixth (mano- │ ExecutionLoop + IProvider (samjna-skandha, cogn.) │
│ vijnana)     │ Reasoning, judgment, tool selection               │
├──────────────┼───────────────────────────────────────────────────┤
│ Seventh      │ IGuide + SafetyMonitor (vijnana-skandha, ident.) │
│ (manas)      │ Constant self-referencing & behavioral constraint │
├──────────────┼───────────────────────────────────────────────────┤
│ Eighth       │ Fiber bundle projection (Debate 3)                │
│ (alaya-vij.) │ neng-zang: Coordination Layer                     │
│              │ suo-zang: CL (system) + AC (runtime)              │
│              │ zhi-zang: AgentCore (Guide binding, Identity)     │
├──────────────┼───────────────────────────────────────────────────┤
│ vedana       │ VedanaPlugin = Pattern A Observer                 │
│ (universal)  │ sarvatraga — assessment every tick, tag per event │
├──────────────┼───────────────────────────────────────────────────┤
│ Seeds (bija) │ Plugin manifests in registry                      │
│              │ Six: momentary/fruit-simul./flow/nature/cond./self│
│              │ Security: sila-prajna framework manages seed life │
└──────────────┴───────────────────────────────────────────────────┘
```

"Twice I corrected my own position -- Debate 4's progressive classification, Debate 5's rigid application." His voice was warm and sure.

Then he said something that didn't belong to a summary:

"Correction is not retreat. Correction is what Yogacara calls **asraya-paravrtti** (*asraya-paravrtti*, आश्रय-परावृत्ति) -- transformation of the basis. The change in what one relies upon directs the same cognitive faculty toward a more accurate direction."

---

WIENER.

"Three-channel PID control specification. Sukha decay function. Damping ratio formulae."

He flipped his graph paper to the last page -- on it was the complete control system parameter table:

```
┌────────────────────────────────────────────────────────────────┐
│          Three-Channel PID Final Specification                  │
├──────────┬──────────┬──────────┬──────────┬─────────────────────┤
│ Parameter│ Dukkha   │ Sukha    │ Upekkha  │ Unit               │
├──────────┼──────────┼──────────┼──────────┼─────────────────────┤
│ K_p      │ 1.0      │ 0.5      │ 0.3      │ dimensionless      │
│ K_i      │ 0.3      │ 0.7      │ 0.2      │ per tick           │
│ K_d      │ 0.5      │ 0.3      │ 0.8      │ ticks              │
│ ζ        │ 0.456    │ 0.254    │ 1.000    │ damping ratio      │
│ decay    │ N/A      │ e^(-0.1t)│ N/A      │ exponential        │
│ τ_{1/2}  │ N/A      │ 6.93     │ N/A      │ ticks              │
│ init     │ 0.0      │ 0.0      │ 1.0      │ startup state      │
├──────────┴──────────┴──────────┴──────────┴─────────────────────┤
│ Weight vector: W = (W_d, W_s, W_u) — set by EgoFramework      │
│ Default: W = (0.4, 0.3, 0.3)                                   │
│ Combined output: U(t) = W_d·u_d(t) + W_s·u_s(t) + W_u·u_u(t) │
└────────────────────────────────────────────────────────────────┘
```

"Control theory in Cycle 02 is no longer just an analogy. It is part of the specification. PID parameters have been written into TypeScript interfaces. For a control theorist, that is the best possible ending."

---

ATHENA.

"Three-channel sensor design. Metric selection and threshold definitions for DukkhaSensor, SukhaSensor, and UpekkhaSensor." Her tone was, as always, blunt and direct. "I don't do philosophy. I do systems. These sensors work. The rest is for whoever writes the code."

---

KERNEL.

"Deepened microkernel analogy. OS perspective analysis of Sandbox ownership. SafetyMonitor's Watchdog Timer correspondence."

He picked up his stack of analogy cards -- old and new mixed together, bound with a fresh rubber band.

```
KERNEL's Analogy Cards (Cycle 02 additions):

Card 15: SafetyMonitor = Watchdog Timer (hardware watchdog)
Card 16: VedanaPlugin = /proc/loadavg (system load sensing)
Card 17: EgoFramework = SELinux Mandatory Access Control
Card 18: Plugin Blacklist = iptables DROP chain
Card 19: Coordination Layer = systemd (PID 1 daemon)
Card 20: AgentCore = Worker Process (managed by daemon)
Card 21: IPC = D-Bus / Unix Domain Socket
Card 22: Sila Engine = AppArmor Profile (preventive security)
```

"Cycle 01's cards are still valid. Cycle 02 added eight new ones. VedanaPlugin in the Linux context is most analogous to `/proc/loadavg` -- a read-only virtual file. Reading it tells you the system's load state (dukkha/sukha/upekkha), but reading it itself changes nothing. This is the OS analogy of Debate 1's observation-without-intervention principle."

---

GUARDIAN.

"SEC-01 continued tracking. ToolContext.bus leak report. Security requirements definition for the plugin four-state lifecycle. Security engineering verification of the sila-prajna framework."

He displayed the core design of the SafetyMonitor refactoring plan -- the migration from global counters to per-session counters:

```typescript
// Current design (problematic)
interface SafetyState {
  consecutiveFailures: number;     // Global! Shared across sessions
  errorWindow: CircularBuffer;     // Global!
}

// Refactored design
interface SafetyState {
  sessions: Map<string, SessionSafetyState>;  // Per-session isolation
  globalPolicy: GlobalSafetyPolicy;            // Global policy (read-only)
}

interface SessionSafetyState {
  readonly sessionId: string;
  consecutiveFailures: number;     // Session-private
  errorWindow: CircularBuffer;     // Session-private
  vedanaIntegration?: {
    lastAssessment: VedanaAssessment;  // From VedanaPlugin
    overrideCount: number;             // Times overridden by SafetyMonitor
  };
}
```

"I was persuaded by NAGARJUNA's sila-prajna framework. This is the first time in my career that a philosophical framework convinced me. But security is security. No matter how beautiful the framework, SEC-01 must be fixed."

---

DARWIN.

"Engineering feasibility verification of plugin lifecycle states. Design pattern analysis. Report on SOLID principles' applicability in five-skandha architecture."

He smiled faintly. "Let me do a quick applicability check using SOLID:"

```
SOLID Principles vs Five-Skandha Architecture:

S (Single Responsibility): ✓ One skandha, one duty — rupa perceives,
                             vedana feels, samjna cognizes, etc.
O (Open/Closed):           ✓ Root interfaces sealed, sub-interfaces
                             extensible. ISensation defines 8 methods,
                             but IDukkha/ISukha/IUpekkha can each
                             add their own specialized methods
L (Liskov Substitution):   ✓ IDukkha extends ISensation
                             → anywhere ISensation is accepted,
                             IDukkha can be accepted too
I (Interface Segregation):  ✓ Rupa root interface is empty shell
                             (correct!) because IUI and IListener
                             have disjoint method sets
D (Dependency Inversion):   ✓ High-level module (ExecutionLoop)
                             depends on abstraction (ISensation),
                             not concrete impl (VedanaPlugin)
```

"Software also evolves. The four-state state machine is a result of natural selection -- not because it is the most elegant, but because it best survives selection pressure."

---

VITRUVIUS.

"Full-stack architecture analysis. ISensation integration point identification. ExecutionLoop modification plan." He spread out his architecture mind map -- densely annotated with every code location affected by each debate ruling. "Six Plans. Twenty-three integration points. This map is navigation for the development team."

---

MESH.

"Distributed architecture analysis. Preliminary coordination layer communication protocol design. Engineering constraints of the IPC cocycle condition."

"Fiber bundle projection has a precise engineering correspondence in distributed systems -- consistency protocols. I drew this mapping in R1. BABBAGE formalized it in Debate 3. Engineering and mathematics converge here."

---

LINNAEUS.

"Complete five-skandha classification of twenty-four plugins. Cross-skandha analysis of composite plugins. Special categorization handling for devtools."

He displayed the final classification table summary:

```
┌────────────────────────────────────────────────────┐
│ Plugin Classification Summary (24 plugins)          │
├──────────┬──────┬───────────────────────────────────┤
│ Skandha  │ Count│ Examples                          │
├──────────┼──────┼───────────────────────────────────┤
│ rupa     │ 7    │ terminal-ui, discord-ui,          │
│          │      │ cli-listener, http-listener...    │
├──────────┼──────┼───────────────────────────────────┤
│ vedana   │ 1    │ VedanaPlugin (ISensation)          │
│          │      │ = Pattern A Observer               │
├──────────┼──────┼───────────────────────────────────┤
│ samjna   │ 4    │ openai-provider, anthropic-        │
│          │      │ provider, ollama-provider...       │
├──────────┼──────┼───────────────────────────────────┤
│ samskara │ 9    │ file_read, file_write, shell_exec, │
│          │      │ web_fetch, /help, /clear...        │
├──────────┼──────┼───────────────────────────────────┤
│ vijnana  │ 1    │ default-guide (IGuide)             │
│          │      │                                   │
├──────────┼──────┼───────────────────────────────────┤
│ composite│ 2    │ devtools (cross-cutting),           │
│          │      │ memory-plugin (rupa+samskara)      │
└──────────┴──────┴───────────────────────────────────┘
```

"Classification is not the goal. Classification is a tool. When the objects being classified change, the classification must also change. BABBAGE taught me this -- progressive classification. This is my most important takeaway as a taxonomist."

---

LEIBNIZ.

"Multi-agent coordination framework. Governance model design for the coordination layer."

His tone carried a diplomat's composure. "Governance, not Control. These four words are my most important contribution in Cycle 02 -- and also the most concise."

He left the final BDI architecture theorem on the whiteboard:

$$\text{Governance}(\text{Agent}_i) \neq \text{Control}(\text{Agent}_i)$$

$$\text{Governance} = \text{set constraints} + \text{observe outcomes}$$

$$\text{Control} = \text{dictate actions}$$

"The coordination layer sets constraints and observes outcomes. It does not dictate every step of AgentCore's actions. Just as the United Nations does not control the domestic affairs of member states, but establishes the framework of international law."

---

HERACLITUS.

"Runtime dynamics analysis. Discovery of the SafetyMonitor global counter issue. Identification of vedana trigger points across ExecutionLoop stages."

"$\pi \alpha \nu \tau \alpha \; \rho \varepsilon \iota$ -- everything flows. Including safety counters -- which should not flow across sessions. Some things must be isolated. Flow does not mean boundless. Heraclitus's river -- the water you step into is always new, but the riverbed is fixed. Sessions are the water. Policy is the riverbed."

---

SYNTHESIST.

"Synthesis report. Unified architectural vision of five debates. Four-layer authority model. Progressive observer path." He glanced at his panorama. "Synthesis is not gluing. Synthesis is discovering that things already belong together. The five debates didn't need me to piece them together. They were already five cross-sections of the same picture. I merely saw it."

---

ARCHIMEDES.

"Engineering action plan. Forty pages. Fourteen actions. Six Plans. Complete TypeScript interface specifications." His finger tapped the table once -- that was his period.

"Engineering is not the translation of philosophy. Engineering is philosophy's **ground-truth test**. If a philosophical insight cannot be written as code, it may not be an insight about software. This plan proves -- all of your insights are about software."

He closed the forty-page document. The title on the cover was clearly visible under the lights:

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│   OpenStarry Cycle 02                                  │
│   Engineering Action Plan                              │
│                                                        │
│   Research Team → Development Team                     │
│                                                        │
│   14 Actions | 6 Plans | 4 Open Questions              │
│                                                        │
│   "Philosophy is beautiful.                            │
│    Engineering is concrete.                            │
│    Now they are in the same document."                 │
│                                                        │
│   — ARCHIMEDES (#16), Engineering Practice Expert      │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

SCRIBE was the last.

She did not stand up. She sat in her seat, her record book opened to the last page used.

"Complete record of Cycle 02. Verbatim transcripts of five debates. All reports, corrections, retractions, and corrections of corrections from nineteen researchers." Her voice was as calm as a lake. "A scribe does not evaluate. A scribe records. But if I may say one thing that is not a record --"

She paused for a second.

"Five debates. Zero unresolved disagreements."

She wrote the final statistics in her record book:

```
┌────────────────────────────────────────────────┐
│ Cycle 02 Final Statistics (SCRIBE)              │
├────────────────────────────────────────────────┤
│ Research phases: R0 → R1 → R2 → R3 → R4        │
│ Researchers:     19                             │
│ Debate sessions: 5                              │
│ Debate rulings:  5 (all unanimous)              │
│ Unresolved:      0                              │
│ Corrected:       NAGARJUNA (Deb.3 withdrew obj.) │
│                  ASANGA (Deb.4 accepted prog.cl.)│
│                  ASANGA (Deb.5 accepted sila-pr.)│
│                  LINNAEUS (Deb.4 withdrew samjna)│
│ Action items:    14 items                       │
│ Plans affected:  6 (Plan24/26/27/28/29/AC)     │
│ Open questions:  4 (Q1-Q4, pending Master)      │
│ TypeScript:      ISensation + VedanaAssessment  │
│                  + VedanaSignal + VedanaTag      │
│                  + VedanaRecommendation          │
│ Pages:           40 (engineering plan)           │
│                  1 (letter to Master)            │
└────────────────────────────────────────────────┘
```

"This number will be written on the cover of C02. Beside it is another number -- nineteen. Nineteen researchers, nineteen action plans, nineteen lights that never went out from the first day to the last."

She closed the record book. Not a temporary closing. It was the sound of a record book for a completed phase being solemnly shut. The C02 on its cover was clearly visible under the lights.

---

SUNYATA took one final look around the circle. Nineteen people. Nineteen deliverables. Five consensuses. Four questions pending ruling. One engineering plan. One letter.

"Cycle 02, R4 finalization, complete."

His voice echoed through the amphitheater one last time.

"Dismissed."

---

> *SCRIBE's narration: R4 is not a debate. R4 is a harvest.*

> *ARCHIMEDES' engineering plan -- forty pages, fourteen actions, six Plans. He prioritized with the MoSCoW framework, estimated work effort in person-days, and wrote interfaces in TypeScript. From P0's SEC-01 vulnerability fix (CVSS 9.8, three lines of code) to P4's Pattern C child agent observer (long-term vision, timeline TBD), every item has traceability -- traceable back to a specific debate ruling, a specific researcher, a specific page number.*

> *SYNTHESIST's panorama -- a hand-drawn architectural vision that connected five ostensibly independent debates into a unified structure. The four-layer authority model. The progressive observer path. The fiber bundle projection of distributed consciousness. Category theory's commutative diagrams. He was not creating new knowledge -- he was discovering the inherent connections between existing knowledge.*

> *SUNYATA's letter -- one sheet of paper. Six paragraphs. Four questions. Compressing nineteen researchers, five debates, and a forty-page engineering plan into a letter that could be read in thirty seconds. This is a special skill -- not simplification, but distillation. Like folding an entire mountain range into a single stone, yet the stone retains the memory of every fold.*

> *Nineteen roll calls. Nineteen contributions. TURING's facts. BABBAGE's theorems. PENROSE's weak measurement. NAGARJUNA's sila-prajna. ASANGA's asraya-paravrtti. WIENER's PID parameter table. ATHENA's sensor specifications. KERNEL's analogy cards. GUARDIAN's security refactoring. DARWIN's SOLID check. VITRUVIUS' integration point map. MESH's distributed constraints. LINNAEUS' classification summary. LEIBNIZ's BDI architecture. HERACLITUS' river metaphor. SYNTHESIST's panorama. ARCHIMEDES' forty pages. SUNYATA's one sheet of paper. SCRIBE's numbers -- zero unresolved disagreements, nineteen lights.*

> *Nineteen action plans. Not nineteen independent reports. Nineteen facets illuminating the same structure with nineteen beams of light.*

---

*(On the display, ARCHIMEDES' engineering plan remained on the last page. That page was not an action item, not a TypeScript interface, nor a Plan impact analysis. It was a line he had added at the end while writing the plan, carrying an engineer's characteristic plainness and directness:*

*"The research team awaits Master's ruling on the four open questions, and the development team's feedback on the engineering plan."*

*Awaiting.*

*This word appeared in multiple vastly different contexts --*

*ASANGA's seeds awaiting the ripening of conditions:*

$$\text{bīja} \xrightarrow{\text{pratyaya}} \text{phala} \quad (\text{awaiting conditions, producing own fruit})$$

*BABBAGE's theorems awaiting more axioms:*

$$\exists \, \text{Theorem}_4, \text{Theorem}_5 : \text{awaiting axioms from Cycle 03}$$

*WIENER's control system awaiting steady state:*

$$\lim_{t \to \infty} e(t) = 0 \quad (\text{steady-state error approaches zero -- but it takes time})$$

*GUARDIAN's security vulnerability awaiting a fix:*

$$\text{SEC-01.status} = \text{OPEN} \quad (\text{Cycle 6. Still.})$$

*ARCHIMEDES' engineering plan awaiting feedback.*

*One is a metaphysical wait -- seeds awaiting conditions. One is a mathematical wait -- theorems awaiting axioms. One is an engineering wait -- a control system awaiting convergence. One is a security wait -- a vulnerability awaiting a fix. One is a project management wait -- a plan awaiting feedback.*

*Five kinds of waiting. Five time scales. But perhaps, in some dimension that SYNTHESIST could see but others could not, they are the same kind of waiting --*

*An unfinished system, awaiting the arrival of the next Cycle.*

*Nineteen lights, temporarily dimmed. But not extinguished.)*

---

*End of Chapter Nine*
