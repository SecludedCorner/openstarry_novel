# Chapter 5: The Cost of a Name -- D4 Naming Correction Debate

---

**Duration**: ~30 minutes | **Trigger**: Master review | **Votes**: 3 items

D4 was not on the original agenda. It was triggered by a single sentence from Master:

> **"If you use Sanskrit, you must take responsibility for its definition. Do you think Sati's content is a complete match?"**

## NAGARJUNA's Reductio ad Absurdum

```
Premise A: Sati = samskara mental factor (Buddhist definition)
Premise B: SatiMonitor != samskara (D2-R2 conclusion)
 :. SatiMonitor != Sati
```

If mindfulness is necessarily samskara in Buddhism, and D2 has already proven that SatiMonitor is not samskara -- then SatiMonitor is not mindfulness. A component that is not mindfulness should not be called Sati.

ASANGA confirmed: "If SatiMonitor is not a samskara activity, then it is not Sati. Our own classificatory analysis negates our own naming."

## ISatiMonitor -> ILoopQualityMonitor (D4-R1: 13/20)

ARCHIMEDES's proposal prevailed: "Loop Quality Monitor" -- a quality monitor for the cognitive loop -- precisely describes the function, no Buddhism, no metaphor.

Minority opinions: IBehaviorQualityMonitor (GUARDIAN, 4 votes), ICognitiveLoopMonitor (NAGARJUNA + ASANGA, 2 votes), IQualityMonitor (SYNTHESIST, 1 vote).

Complete renaming table: ISatiMonitor -> ILoopQualityMonitor, SatiQualityVector -> LoopQualityVector, and 8 items total.

## IPrajna -> IConfidenceAuditor (D4-R2: 16/20)

NAGARJUNA: "Prajna is the highest cognitive capacity in Buddhism -- the wisdom that illuminates the true nature of all dharmas."

ASANGA: "It is like calling a temperature fine-tuning knob a nuclear fusion reactor."

IPrajna's actual function: one method, inputs a confidence score, outputs `{ delta: number, reasoning: string }`, with delta clamped to [-0.05, +0.05]. This is auditing -- not prajna.

BABBAGE: IConfidenceAuditor is the most semantically precise -- an independent, limited-scope, documented secondary check.

Minority opinions: IThresholdCalibrator (WIENER, 2 votes), ISecondaryEvaluator (HERACLITUS + PENROSE, 2 votes).

## Doc 03 Re-Vote (D4-R3: 17/20)

"Sila-Prajna Security Framework" -> "Plugin Security Lifecycle"

Initial vote of 14/20 to keep unchanged. Master review triggered re-examination -- all four tests failed: Necessity (no need for seed theory to understand plugin lifecycle), Code identification (actual types use English), Decision-driven (no DC confirmation), Definition responsibility (sila != access control, prajna != CVE revocation).

ASANGA's key distinction: Doc 16 = standalone mapping document (Master ruled to keep) vs Doc 03 = Buddhist decoration in an engineering document (should be cleaned up).

## The Fourth Test -- Definition Responsibility (Permanent Standard)

> **"When using Buddhist Sanskrit terms as code identifiers, the component's functionality must match the term's Buddhist definition. If inconsistent, use engineering terminology."**

Supplements D1's three tests -- even if a name passes Test 2 (code identification), if it fails Test 4 (definition responsibility), it should still be renamed.

Scope of impact: ILoopQualityMonitor affects 6 documents with 100+ replacements; IConfidenceAuditor affects 5 documents; Doc 03 renamed + content cleanup.

---
