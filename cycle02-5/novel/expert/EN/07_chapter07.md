# Chapter 7: Pure Engineering

---

After D4 ended, SUNYATA announced a fifteen-minute break.

No one left their seat.

Not because they didn't want to rest — but because D4's aftershocks were still reverberating. ISatiMonitor became ILoopQualityMonitor. IPrajna became IConfidenceAuditor. Doc 03 went from "Sila-Prajna Security Framework" to "Plugin Security Lifecycle." Thirty minutes. Three names. One permanent test.

TURING opened his laptop during the break. He was not resting — he was making final preparations.

Because D5 was his debate.

---

## I. The Archaeologist

TURING's role throughout Cycle 02-5 had been "source code verifier" — every code reference in every research report was checked by him one by one. In R1's nine independent studies, he verified over 40 code references. In R2's cross-review, he found four issues (no severe errors). In D1 through D4, he was the silent arbiter — never participating in philosophical debate, only standing up to confirm or correct when someone cited source code.

But D5 was different.

D5's topic was: **Plan29 engineering design specification.** Master's instruction was clear: "Continue discussing and documenting until the spec reaches 100%, then deliver to the engineering team."

For this debate, TURING did something he had not done in any previous Cycle — he wrote a complete v0.28.0-alpha design pattern report. Not a summary. Not a bullet list. A comprehensive analysis of 14 source code files: all Registry lifecycles, timeout patterns, sync/async patterns, failure handling strategies.

He called this report "code archaeology."

---

## II. Ten Debaters

D5 had only ten participants.

Not because others were excluded — but because SUNYATA judged D5's topic to be a pure engineering problem that did not require all twenty researchers. He invited the ten most relevant to Plan29:

| # | Code Name | Role | D5 Focus |
|---|-----------|------|----------|
| 3 | VITRUVIUS | Architecture Analyst | Interface design |
| 5 | ATHENA | AI/ML Expert | Auditor's LLM semantics |
| 6 | DARWIN | Software Pattern Analyst | Design pattern evolution |
| 10 | KERNEL | OS Expert | Registry lifecycle |
| 11 | GUARDIAN | Security Expert | Security boundaries |
| 12 | WIENER | Control Theory Expert | Quality vector weights |
| 13 | LINNAEUS | Taxonomy Expert | Skandha attribution inference |
| 16 | ARCHIMEDES | Engineering Practice Expert | YAGNI principle |
| 17 | TURING | Source Code Analysis Expert | Design pattern baseline |
| 19 | PASCAL | Decision Theory Expert | Interface semantic precision |

Ten people. Zero Buddhist scholars.

NAGARJUNA (#7) and ASANGA (#8) voluntarily withdrew from D5. Not because they had nothing to contribute — but because D5's topic did not require Buddhist analysis. NAGARJUNA said one thing before withdrawing: "D4 proved that Buddhist names must be accountable to their definitions. D5 will prove that engineering design can be completed without Buddhist names. Both things are equally important."

---

## III. Nine Votes

D5 was Cycle 02-5's most vote-heavy debate — nine votes. But also its fastest-paced debate — seventy-five minutes, averaging less than nine minutes per vote.

Because TURING's code archaeology report provided the factual foundation. Every decision started not from "what should we do" but from "what is currently being done."

---

### D5-R1: Independent `auditor` hook slot

First question: which PluginHooks slot should IConfidenceAuditor (formerly IPrajna) use?

Options: (A) Reuse the D2-established `monitors` slot; (B) Create an independent `auditor` slot.

GUARDIAN's argument was most direct: "Monitors are pure observers — no side effects. Auditor has LLM side effects — it calls an external model for confidence evaluation. Putting observers and side-effecting components in the same Registry blurs security audit boundaries."

KERNEL confirmed from the OS perspective: "Observers and arbiters never share a Registry. This is a fundamental microkernel principle."

**8/8 unanimous. Independent `auditor` slot.**

---

### D5-R2: audit() return type

The most heated D5 vote.

Options: (A) Pure async `Promise<ConfidenceAuditResult>`; (B) Dual-mode `ConfidenceAuditResult | Promise<ConfidenceAuditResult>`.

GUARDIAN, KERNEL, VITRUVIUS supported Option A — pure async. Rationale: audit was essentially "asking an LLM," and LLM calls are asynchronous. Forcing async semantics was more precise.

ATHENA and DARWIN supported Option B — dual-mode. Rationale: following the IGearArbiter precedent. Testing could use synchronous no-op implementations without async/await boilerplate.

TURING provided facts: "In v0.28.0-alpha, IGearArbiter.evaluate() uses dual-mode return. IVolition.deliberatePlan() and deliberateAction() also use dual-mode. This is the existing design pattern. Deviating from it requires sufficient justification."

**5/8 Option B passes.** The closest vote in D5.

---

### D5-R3: Timeout and fail-safe

TURING opened his timeout pattern analysis. Existing timeouts in v0.28.0-alpha:

| Component | Timeout | Default |
|-----------|---------|---------|
| IProvider.chat() | LLM response | 120s |
| IGearArbiter.evaluate() | Per arbiter | 100ms |
| IGearArbiter chain | Entire chain | 200ms |
| ITool.execute() | Tool execution | 30s |

What should audit()'s timeout be?

TURING's recommendation: 200ms — consistent with the IGearArbiter chain deadline. Rationale: audit() occurred in the final stage of confidence computation, after IGearArbiter. If audit's timeout exceeded the chain deadline, the entire decision flow would be blocked by audit.

Fail-safe: `{ delta: 0, reasoning: "audit timeout" }`. On timeout, delta is zero — no correction. Using the `Promise.race()` pattern, consistent with existing code.

Configurable: overridable via agent.json.

**8/8 unanimous.**

---

### D5-R4: Multiple Auditor handling

Can an Agent load multiple IConfidenceAuditor plugins?

ATHENA invoked the YAGNI principle: "v1 will have at most one auditor plugin. Designing multi-auditor aggregation strategy is over-engineering."

TURING and VITRUVIUS dissented: "Array pattern is more flexible. Avoids future breaking changes."

ARCHIMEDES supported ATHENA: "Follow the IVolition precedent — PluginHooks declares `auditor?: IConfidenceAuditor`, singular, last-loaded wins. If multi-auditor is needed in the future, change it then — changing one interface is cheaper than maintaining an unused aggregation strategy."

**6/8 single auditor passes.** TURING and VITRUVIUS' minority opinions were recorded.

---

### D5-R5: Failure handling

What happens when audit() throws an exception?

TURING provided the existing pattern: IGearArbiter and SafetyMonitor both followed "fail-safe + log" — errors do not block subsequent flow; a warning is logged.

No vote needed. Consensus reached directly.

---

### D5-R6: MonitorRegistry start timing

Where is ILoopQualityMonitor's `start(bus)` called?

TURING's analysis: SafetyMonitor starts at `ExecutionLoop.onLoopStart()`. MonitorRegistry should follow the same timing.

```
Start: MonitorRegistry.startAll(bus) <- ExecutionLoop.onLoopStart()
Stop:  MonitorRegistry.stopAll()     <- PluginLoader.disposeAll()
```

DARWIN preferred starting in PluginLoader (simpler) but accepted that monitors had explicit start/stop semantics, making ExecutionLoop the more appropriate location.

**7/8 passes.**

---

### D5-R7: LoopQualityVector weights

Four-dimensional quality vector — Continuity, Granularity, Speed, Equanimity — what weight for each dimension?

WIENER gave the only reasonable answer from a control theory perspective: "Without runtime data, equal weights are the most conservative choice. 0.25 per dimension."

No one objected. 0.25 x 4 = 1.0. Simple, symmetric, interpretable.

The minSamples threshold (minimum samples needed before triggering SPC judgment) was deferred to v2 — actual runtime data was needed for the decision.

**8/8 unanimous.**

---

### D5-R8: validatePluginSkandha() mode

This function validated skandha declaration consistency during plugin loading. Currently warning-only. Should it become mandatory?

GUARDIAN (one vote) preferred structured ValidationResult — to assist automated testing. But acknowledged v1 didn't need it.

Majority opinion: warning-only was sufficient. If skandha declaration was inconsistent, plugin function was unaffected (skandha was metadata, not routing — D3-R3 had ruled).

**7/8 maintain warning-only.**

---

### D5-R9: IConfidenceAuditor skandha attribution

The final item. Which skandha does IConfidenceAuditor belong to?

ASANGA, though not participating in D5's debate, had his R1 analysis cited: "LLM judgment = pure vijnana (discrimination, evaluation)."

LINNAEUS confirmed: "Single-skandha (vijnana) -> strong inheritance (extends IVijnana), consistent with IVolition and IKlesha."

`inferSkandha()` new logic: `if (hooks.auditor) { push('vijnana') }`

**8/8 unanimous.**

---

## IV. Interface Finalized

After nine votes, TURING wrote the final interface specification on the whiteboard:

```typescript
export interface IConfidenceAuditor extends IVijnana {
  readonly id: string;
  audit(confidence: number, context: GearContext):
    ConfidenceAuditResult | Promise<ConfidenceAuditResult>;
}

export interface ConfidenceAuditResult {
  delta: number;       // clamped to [-0.05, +0.05]
  reasoning: string;   // audit trail
}
```

And the final form of PluginHooks:

```typescript
interface PluginHooks {
  // ... existing fields ...
  monitors?: ILoopQualityMonitor[];   // Plan29 Wave 1
  auditor?: IConfidenceAuditor;       // Plan29 Wave 2 (singular)
  // ...
}
```

He stepped back and looked at the whiteboard.

"100%," he said.

Master's requirement was "spec reaches 100%." Now it did. Interface names, method signatures, return types, timeout, fail-safe, multi-auditor strategy, Registry timing, weights, validation mode, skandha attribution — every detail that needed deciding had a definitive answer.

Not "general direction." Not "conceptual design." A complete spec that could be handed directly to an engineering team for implementation.

---

## V. Zero Buddhism

SCRIBE tallied a number in the D5 record: the number of times Buddhist terminology was used during the entire D5 debate.

Zero.

Not deliberately avoided — it was a natural result. Each of the nine votes discussed TypeScript interface design, timeout values, Registry patterns, fail-safe strategies. None required Buddhist analysis. None cited Buddhist scripture. None used Sanskrit or Pali terms (except skandha — which was already a code identifier).

D5 was the first debate in this project's history with absolutely no Buddhist content.

NAGARJUNA observed the entire debate from the back row of the amphitheater. After D5 ended, he walked to TURING.

"Your code archaeology report is the best factual-basis document I've seen," he said. "It anchored every discussion to facts — not concepts, not metaphors, not tradition. Facts."

TURING replied: "That's the engineering way."

NAGARJUNA nodded: "D4 proved that names must be accountable to their definitions. D5 proved — some engineering problems don't need definitions at all. They only need specifications."

---

> *SCRIBE's aside*

> *D5 was a temple with no one in it.*

> *No — D5 was a city that needed no temple.*

> *After D1 through D4's storm, D5's calm was not the eye of the hurricane — it was clear sky. Nine votes, seventy-five minutes, ten engineers and scientists sitting together, discussing the precise specification of TypeScript interfaces. No Buddhism. No philosophy. No metaphor. No scale.*

> *Only engineering.*

> *Pure engineering.*

> *TURING's code archaeology report changed the debate's texture. Previous debates — D1 through D4 — were built on principles and frameworks. Principles needed interpretation, contention, voting. But TURING's report was built on facts. IGearArbiter's timeout was 100ms — fact. IVolition used dual-mode return — fact. SafetyMonitor started at onLoopStart() — fact.*

> *When discussion is built on facts, votes come faster. Not because people think less — but because facts narrow the space for divergence. You can have different interpretations of a principle. You cannot have different interpretations of a timeout value.*

> *D5's closest vote was D5-R2 (audit() dual-mode return, 5/8). The dispute was not about "should we use dual-mode or not" — but "should we deviate from the existing design pattern." GUARDIAN argued pure async semantics were more precise. TURING pointed out existing code used dual-mode. Precision vs. consistency. Consistency won — because in engineering, the cost of deviating from existing patterns is usually higher than the benefit of semantic precision.*

> *After nine votes, the whiteboard held a complete interface specification. Not a concept — code. Not a direction — a specification. Something that could be handed directly to an engineering team, so they could open their IDE and start typing.*

> *NAGARJUNA's words after D5 ended are worth recording twice: "D4 proved that names must be accountable to their definitions. D5 proved that some engineering problems don't need definitions at all — they only need specifications."*

> *This is not a contradiction. It is two sides.*

> *Two sides of the scale.*

> *One side asks: does your name live up to your definition?*

> *The other side asks: is your specification precise enough?*

> *D4 calibrated the first side. D5 completed the second.*

> *The scale now had weight on both ends.*

---
