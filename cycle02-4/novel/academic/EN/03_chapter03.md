# Chapter Three: The Fabricated Code

---

## I. TURING's Correction

D4 opened with a correction.

TURING stood up: "The R07 report cites `ISensation.ingestToolResult()` in multiple places. This method is entirely nonexistent across the entire v0.26.0-beta codebase. Global search: zero results."

Three fabrications -- ISensation, feedbackQueue, SparshEvent.timestamp. One report. HERACLITUS did not argue -- TURING's global search was irrefutable.

This correction changed D4's tenor. If samskara (volition/formation) can update vedana (feeling) in real time within the same cycle (as described in R07), the stability analysis is one thing. If samskara can only affect vedana in the next cycle (the actual situation), the stability analysis is an entirely different thing. Feedback delay went from zero to one full cycle -- a difference sufficient in control theory to alter a system's stability conclusions.

HERACLITUS's reaction was impressive -- no excuses, no "my analysis is still valid" defense. He immediately accepted the correction and readjusted his model of samskara's influence. Academic honesty is not merely admitting error -- it is adjusting course within three seconds of the error being identified.

The lesson was written into the record: **All analyses involving code references must be verified by TURING.** This rule took effect from D4 onward and was strictly enforced in D5 and D6 -- whenever someone cited code, TURING would simultaneously perform a global search confirmation.

---

## II. The Boundaries of Samskara

Four rapid consensuses established strict limits on samskara:

1. Samskara may only directly affect IUI (the user interface skandha) -- all influence on other skandhas must occur indirectly through EventBus.
2. Samskara does not directly modify the state of vijnana (consciousness) or samjna (perception) skandha.
3. Mental samskara influences vedana across cycles through EventBus.
4. Samskara results triggering new sparsha (mano-dvara self-contact) is deferred to Phase 2.

These limits constitute samskara's "cannot-do" list. Samskara is the hand -- it can push the external world (IUI), but it cannot reach directly into the brain (vijnana, samjna) to alter the way of thinking. To alter the way of thinking, it must first change external state, and let external state become new input in the next cycle.

LEIBNIZ confirmed the necessity of this constraint from the multi-agent cooperation perspective: if samskara could directly modify other skandhas' states, it would be equivalent to one module bypassing interfaces to directly modify another module's internal state. In distributed systems, this is the primary cause of race conditions and irreproducible bugs.

NAGARJUNA's Buddhist confirmation was even more fundamental: samskara directly modifying vijnana or samjna is equivalent to "the effect directly modifying the cause." In pratityasamutpada (dependent origination), causal chains must pass through intermediaries -- action changes the environment, and the environment becomes new conditions for dependent arising in the next instant. Skipping the intermediary is skipping causality.

These four constraints were frequently cited in all subsequent D4 discussions -- they are the fundamental theorems of the samskara model, and all subsequent derivations are built upon this foundation. ARCHIMEDES called them "the four axioms of samskara" -- basic rules that need no proof and cannot be violated.

Noteworthy is the fourth constraint -- the deferral of mano-dvara self-contact. Samskara's results can trigger new sparsha, just as an action's consequences can become new objects of perception. But this mechanism involves causal circulation: samskara -> new sparsha -> new vedana -> new samjna -> new samskara. Implementing such circulation in Phase 1's linear pipeline requires additional design, hence the deferral to Phase 2.

---

## III. Gain Ceiling and Stability

D4-R1: samskara -> vedana feedback gain ceiling w <= 0.3.

PASCAL provided Bayesian justification. The Kalman gain derivation: in a discrete-time Kalman filter, gain K = P*H'*(H*P*H' + R)^-1. When process noise Q far exceeds observation noise R (high uncertainty / high observation quality), gain approaches the upper bound. PASCAL estimated this upper bound under OpenStarry's typical operating conditions: K_1 ~ 0.308.

Engineering takes 0.3 as the conservative value -- slightly below the theoretical upper bound, leaving a safety margin. 8/9 (ARCHIMEDES abstained -- he believed the specific value should be configurable per deployment environment; 0.3 as a default is fine, but should not be hardcoded).

D4-R2: three-layer stabilization mechanism -- one of this cycle's deepest interdisciplinary achievements.

| Layer | Mechanism | Buddhist Mapping | Characteristic |
|-------|-----------|-----------------|----------------|
| Layer 1 | Sati fine-tuning (per-cycle micro-adjustment) | sampajanna (clear comprehension) | Continuous, small-magnitude |
| Layer 2 | VitakkaWatchdog coarse feedback (cross-cycle trends) | vitakka (applied thought) contemplation | Intermittent, medium-magnitude |
| Layer 3 | SafetyMonitor hard constraints (immediate trigger) | sila (morality) guardrails | Discrete, large-magnitude |

WIENER's Lyapunov stability analysis provided the mathematical guarantee. Define the Lyapunov function V = Sum(x_i - x_i*)^2, where x_i is each skandha's state and x_i* is the desired equilibrium point. Stability condition:

```
k_positive_feedback * w_samskara < k_stabilization * sati_min
```

Where k_positive_feedback is the positive feedback gain (reinforcement effect of samskara's repeated patterns), w_samskara is the samskara weight (<= 0.3), k_stabilization is the stabilization gain (combined effect of the three-layer mechanism), and sati_min is the minimum mindfulness level.

Specifically, if an action produces positive feedback that makes the system more inclined to repeat that action, the three-layer stabilization mechanism ensures this positive feedback loop does not run away:
- Layer 1 (Sati) continuously fine-tunes -- small correction each cycle
- Layer 2 (VitakkaWatchdog) monitors trends -- medium intervention when deviation accumulates
- Layer 3 (SafetyMonitor) hard-cuts -- large correction when all else fails

As long as the combined effect of the three-layer mechanism suffices to counteract the maximum positive feedback gain, the system is globally asymptotically stable. 9/9.

---

## IV. Zero-Order Hold

D4-R3: vedana snapshots at cycle start (Zero-Order Hold), batch updates at cycle end.

This is the direct consequence of TURING's correction -- since samskara cannot update vedana in real time within the same cycle, the rule is made explicit: vedana takes a snapshot at the start of each cycle, all skandhas use this snapshot throughout the cycle, and accumulated changes are written in a single batch at cycle end.

Four-dimensional verification made this resolution a paragon of interdisciplinary consensus:

- **Control theory** (WIENER): Optimal for stability -- eliminates intra-cycle real-time feedback paths. In discrete control systems, zero-order hold is the standard method.
- **Buddhism** (NAGARJUNA): Correct causal temporality -- the vedana -> samjna -> samskara causal chain is not disrupted by mid-course modification. A single instant's vedana determines that instant's samjna and samskara -- samskara's results cannot retroactively modify the same instant's vedana.
- **Engineering** (ARCHIMEDES): Simplest implementation -- no need to handle intra-cycle race conditions. Snapshot once, use for one cycle, write once.
- **Safety** (GUARDIAN): SafetyMonitor independently handles immediate protection -- it is not constrained by zero-order hold. In a genuine emergency, SafetyMonitor can intervene at any moment without waiting for the cycle to end.

Four disciplines. Four independent arguments. One conclusion. 9/9.

---

## V. The Silkworm Binding Itself

D4-R4 answered OQ-6: samskara's repeated patterns enhance Moha (delusion), using a diminishing marginal saturation model.

ASANGA cited the Yogacara imagery: "Like a silkworm spinning its cocoon, binding itself within" -- from the *Cheng Weishi Lun* (Treatise on the Establishment of Consciousness-Only). The silkworm spins silk and forms a cocoon, sealing itself inside. Each thread is thin, but accumulated they form a cocoon. Samskara's repeated patterns are like the spun silk -- if an Agent repeatedly uses the same strategy, that strategy gradually becomes its "cocoon." It grows ever more inclined to use that strategy, ever less able to try new ones.

DARWIN confirmed the universality of this phenomenon from the software pattern perspective: "This is path dependency. In software systems, early architectural decisions constrain later possibilities. In cognitive systems, early behavioral patterns constrain later behavioral space. The diminishing marginal model correctly captures this characteristic."

Mathematically: Delta-Moha = alpha_m * r / (1 + beta_m * M).

The formula's meaning: r is the repetition count, M is the current Moha level. The numerator alpha_m * r grows linearly with repetition, but the denominator 1 + beta_m * M also grows, making the increment ever smaller. Early repetitions have large impact -- the first time a pattern is repeated, Moha increases the most. But as Moha accumulates, new repetitions bring diminishing increments. Like a deeply ingrained habit -- repeating it once more produces less solidification than the first few times did.

WIENER confirmed the model's stability: diminishing margins guarantee that Moha has a natural saturation ceiling -- it will not grow without bound. Safety ceiling: actionHistory contribution <= 30%, ensuring samskara's repeated patterns cannot dominate the total Moha value. 9/9.

---

## VI. D4's Interdisciplinary Density

D4 was the debate with the highest mathematical density. Four core concepts -- Kalman gain (PASCAL), Lyapunov function (WIENER), zero-order hold (ARCHIMEDES/WIENER), diminishing margins (PASCAL/ASANGA) -- came from four different disciplines, yet converged on the same question: how can samskara influence other skandhas without destroying system stability?

The answer is not a single formula but an interlocking set of constraints:
- Gain ceiling (w <= 0.3) limits the magnitude of each influence
- Zero-order hold eliminates intra-cycle real-time feedback
- Three-layer stabilization ensures long-term global asymptotic stability
- Diminishing margins prevent unbounded Moha accumulation

Four constraints. Four disciplines. One stable system.

D4's other implicit contribution: it established TURING's "fact-checker" role in the debates. From D4 onward, whenever someone cited code, TURING would simultaneously perform a global search. This informal institution was strictly enforced in D5 and D6, ensuring all code references in subsequent debates had a factual basis. The three engineering memos TURING uncovered in D6 (injectPrompt security flaw, VedanaRegistry duplicate check absence, isSahajaValid dead code) were all products of this role.

> *SCRIBE's narration: D4's mathematical density was the highest of the six debates -- Kalman gain, Lyapunov function, zero-order hold, diminishing margins. But the most profound moment was not the mathematics; it was TURING's three seconds of silence -- in those three seconds, the foundation of the entire debate shifted from fabricated code to real code. Fact before theory. This lesson echoed through D5 and D6 -- whenever someone cited code, TURING would silently open the search window.*

---
