# Chapter 6: D5 -- A Debate Without Buddhism

---

## Ten People, Zero Buddhist Scholars

D5 was a special debate.

Only ten participants -- and no Buddhist scholars. NAGARJUNA and ASANGA voluntarily stepped out. NAGARJUNA's parting words were interesting: "D4 proved that names must be accountable to their definitions. D5 will prove that engineering design can be completed without Buddhist names. Both of these things are equally important."

D5's topic was a purely engineering question: take the interfaces renamed in D4 and design them into complete, executable specifications. Master's requirement was "get the specification to 100%, then hand it off to the engineering team."

---

## Code Archaeology

TURING prepared a special report for D5 -- he analyzed every design pattern across 14 source code files. What is each timeout set to? How does each Registry work? What happens when each one fails?

He called this report "code archaeology."

This report changed the way the debate worked. Previous debates were built on "principles" -- and principles can be interpreted differently. But TURING's report was built on "facts" -- and facts only have one version.

---

## Nine Decisions

D5 made nine votes in seventy-five minutes. It moved quickly -- because every item had a factual foundation.

The most important decisions:

**IConfidenceAuditor gets its own dedicated slot.** Not shared with monitors. Reason: monitors only observe (no side effects), while auditors call AI models (has side effects). Observers and side-effect-producing components shouldn't be mixed together. Passed unanimously.

**Return type uses dual mode.** Can be either synchronous or asynchronous. This was D5's closest vote -- 5 to 3. The disagreement wasn't about "is dual mode good or not," but about "should we break the existing design pattern." In the end, "consistency" won -- because in engineering, staying consistent with existing code is usually more important than chasing perfection.

**Timeout: 200 milliseconds.** If the audit doesn't respond within 200 milliseconds, skip it (don't modify the confidence score). Consistent with the existing gear arbiter. Passed unanimously.

**Only one auditor allowed.** No complicated multi-auditor aggregation strategies. Following the YAGNI principle -- You Ain't Gonna Need It (don't build what you don't need yet). Passed 6 to 2.

**Equal weights.** The quality vector's four dimensions -- continuity, granularity, speed, and balance -- each at 0.25. Control theory expert WIENER said: "When you have no runtime data, equal weights are the most conservative choice." Passed unanimously.

---

## The Final Specification

After nine votes, TURING wrote the final interface on the whiteboard:

```typescript
export interface IConfidenceAuditor extends IVijnana {
  readonly id: string;
  audit(confidence: number, context: GearContext):
    ConfidenceAuditResult | Promise<ConfidenceAuditResult>;
}

export interface ConfidenceAuditResult {
  delta: number;       // clamped to [-0.05, +0.05]
  reasoning: string;   // audit log
}
```

"100%," he said.

This was not a concept design. This was a complete specification that an engineer could open their code editor and start implementing right away.

---

## Zero Buddhism

Recorder SCRIBE tallied the number of times Buddhist terms were used in the entire D5 debate.

Zero.

D5 was the first debate in this project's history with absolutely no Buddhist content. Not deliberately avoided -- it was a natural result. When you're discussing timeout values and failure handling strategies, you don't need to cite any Buddhist scriptures.

NAGARJUNA came over after the debate ended and said: "D4 proved that names must be accountable to their definitions. D5 proved -- some engineering problems don't need definitions at all. They just need specifications."

This isn't contradictory -- it's two sides of the same scale. One side asks, "Does your name live up to its definition?" The other asks, "Is your specification precise enough?" D4 calibrated the first side. D5 completed the second.

Both sides are needed. Neither can be missing.

---
