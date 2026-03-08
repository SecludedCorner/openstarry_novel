# Chapter Six: Three Debates -- The Precise Path from Divergence to Consensus

---

## 6.1 R2 Divergence Identification

R2 cross-review identified 24 consensus points and 3 points of divergence. All four cross-track comparison groups confirmed zero conflicts -- the philosophical track's conclusions did not affect any design assumptions in the engineering track:

| Comparison | Result |
|-----------|--------|
| C2 cetasika critique -> A1 AuditContext | 4/4 no impact |
| C4 engineering applicability -> D2 Plan30 | 4/4 no impact |
| C3 ISamskara expansion -> B1 formulas | 5/5 no impact |
| C2 cetasika critique -> skandha attribution list | 11 confirmed / 0 revised / 1 pending debate / 14 future |

All three divergences were internal to the engineering track:

1. **Extras write protocol**: A2 proposed generic event pattern vs. B3 proposed direct subscription -> Resolved in D2
2. **Extras key naming**: `loopQuality:score` vs. `loopQuality:composite` -> Unified to `loopQuality:composite` in D2
3. **loopQualityFn data source**: Whether L3 callback and extras cache should share the same source -> Resolved in D3 (dual-channel: pull + push)

---

## 6.2 D1: Formations Deep Investigation (approx. 75 minutes, 7 resolutions)

| Resolution | Content | Votes | Key Arguments |
|-----------|---------|-------|--------------|
| D1-R1 | Core definition of formations: cetana-centered, constructive function, coreless process | 20/20 | Direct citation of SN 22.56/79/95, no ambiguity |
| D1-R3 | No new ISamskara sub-interfaces; three criteria as permanent tool | 20/20 | Confirms 02-5 D3-R4, Directions A/B archived |
| D1-R4a | Cognitive sequence appendix scheduled for 02-7 P2 | 19/20 | 1 dissent argued it could be completed this round |
| D1-R4b | Four Wisdoms formally excluded | 18/20 | 2 dissenting votes argued for retention as reference; all four tests failed |
| D1-R4c | C4 comprehensive assessment table confirmed | 20/20 | -- |
| D1-R5 | "Activity and Transformation" principle; formations=WRITE, consciousness=READ | 20/20 | PENROSE's WRITE/READ distinction |
| D1-R6 | Five permanent skandha-attribution principles | 20/20 | Permanent baseline, not a single-round resolution |

D1 was the highest-consensus debate of the three -- five unanimous votes. The reason: the philosophical track's conclusions were directly grounded in original canonical citations, involving no engineering trade-off judgments, and thus leaving minimal room for divergence.

D1's conclusions required no supplementary agenda items for D2/D3 -- the cross-track influence protocol's "philosophy before engineering" rule was validated as zero-conflict in this round.

---

## 6.3 D2: AuditContext (approx. 85 minutes, 5 resolutions)

| Resolution | Content | Votes | Key Arguments |
|-----------|---------|-------|--------------|
| D2-R1 | Complete AuditContext type (sparshEvent required, history default 10 configurable) | 20/20 | A1-OQ1/2/3 all resolved |
| D2-R2 | Extras bag protocol (dual-event + SDK helper, shallow freeze, max 32 keys) | 19/20 | MESH opposed dual-event complexity; majority supported generality |
| D2-R3 | ConfidenceAuditLog (GUARDIAN D5 obligation fulfilled) | 20/20 | GUARDIAN confirmed settlement on the spot |
| D2-R4 | Layer integration Option C (L2->confidence, L3->threshold, alpha=0.10) | 20/20 | WIENER/BABBAGE stability analysis was decisive |
| D2-R5 | Three-phase auditor strategy: Phase 0 PassthroughAuditor | 20/20 | -- |

The voting process for D2-R4 is worth noting: WIENER and BABBAGE's stability analysis (Lyapunov comparison of Options A/B/C) was already presented in the R1 reports. No one challenged the analysis during R2 cross-review. By the time of the D2 debate, it passed unanimously -- the persuasive power of mathematical proof is deterministic.

All three R2 divergences were resolved in D2:
- Extras write -> Unified as dual-event + SDK helper (D2-R2)
- Key naming -> Unified as `loopQuality:composite` (D2-R2 ancillary resolution)
- loopQualityFn data source -> Deferred to D3

---

## 6.4 D3: LoopQualityMonitor (approx. 85 minutes, 5 resolutions)

| Resolution | Content | Votes | Key Arguments |
|-----------|---------|-------|--------------|
| D3-R1 | Four-dimension formulas confirmed (C/E/Conv/S; W=10, warmup=5, Q_default=0.5) | 20/20 | OQ-29-1 formally answered |
| D3-R2 | EventBus subscriptions: 6 events Phase 1; AgentEventType constant promotion | 20/20 | OQ-29-4 formally answered |
| D3-R3 | Extras write: D2-R2 pipeline + loopQualityFn dual-channel; per-route lifecycle | 20/20 | Resolves R2's third divergence |
| D3-R4 | Weights Phase 1 fixed balanced 0.25x4 | 20/20 | PASCAL's maximum entropy argument |
| D3-R5 | Plan30 = Monitor + L3 + type definitions; Plan31 = Auditor + Audit Trail | 19+1 conditional | GUARDIAN conditional approval |

D3-R5 was the only resolution with a conditional approval. GUARDIAN's condition: **Plan30's Wave 3 must include the `ConfidenceAuditLog` SDK type definition; it must not be deferred to Plan31.** Rationale: the log type is the core deliverable of the D5 concession conditions, and deferral equals debt extension. The condition was accepted, and GUARDIAN switched to approval.

---

## 6.5 Three-Phase Auditor Strategy [D2-R5, 20/20]

| Phase | Corresponding Plan | Implementation | Description |
|-------|-------------------|---------------|-------------|
| Phase 0 | Plan30 (W4, optional) | PassthroughAuditor | delta=0, pure logging; validates end-to-end pipeline integrity |
| Phase 1 | Plan31 | ThresholdAuditor | Rule-based: low confidence detection, loopQuality anomaly, trend detection |
| Phase 2 | Long-term | LLM-assisted | LLM-assisted auditing |

Phase 0's PassthroughAuditor appears useless -- an auditor that adjusts nothing. But ARCHIMEDES' engineering insight: "Its value lies not in auditing, but in testing. It verifies AuditContext assembly, extras collection, audit delta clamping, ConfidenceAuditLog emission -- the entire pipeline end-to-end. Like turning on the faucet after installing the plumbing."

All phases must comply with WIENER C-1/C-2/C-3 constraints -- this is not a Phase 0-specific requirement, but a permanent constraint.

---

## 6.6 Statistical Comparison

| Metric | Cycle 02-5 | Cycle 02-6 |
|--------|-----------|-----------|
| Resolutions | 29 | 17 |
| Vetoes | 0 | 0 |
| Unanimous (20/20) | ~20 (69%) | 13 (76%) |
| Master overturns | 2 | 0 |
| Debate sessions | 5 | 3 |
| R1 reports | -- | 14 |
| R2 consensus points | -- | 24 |
| R2 divergence points | -- | 3 |

DARWIN's observation: "02-5 was a correctness debate -- what is right, what is wrong. 02-6 was a specification debate -- what does the right thing look like. The latter naturally reaches consensus more easily, because it does not involve value judgments."

SUNYATA's analysis: "R1 was done well. Fourteen reports covered the entire problem space. R2 found only 3 divergences. When most questions have consensus before the debate, the debate becomes confirmation and refinement."

The reason for zero Master overturns: the eight rules were already established during the R2 phase (Master's three rounds of refinement), and all resolutions in D1-D3 operated within the framework of the eight rules. No resolution attempted to challenge the framework itself.
