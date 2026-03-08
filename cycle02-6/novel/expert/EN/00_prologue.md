# Prologue: From Debridement to Precision Engineering

---

Cycle 02-5 was a large-scale debridement surgery.

Twenty researchers produced 29 resolutions in five days. DC Master overturned two of them on review (D3-R3 Four Wisdoms mapping, D4-R1 cetasika naming). The entire team performed de-ornamentation refactoring across seven design documents -- removing Buddhist labels that carried no architectural driving force, unifying naming conventions, dismantling incorrect skandha-attribution mappings. Those five days were like dead code elimination on the codebase: not adding features, but removing accumulated semantic debt.

Cycle 02-6 strikes a fundamentally different tone. The previous round answered "what is wrong"; this round must answer "what does a correct specification look like."

---

## Dual Inputs

DC Master issued two letters, triggering the engineering track and the philosophical track respectively.

**The engineering letter** pointed to six Open Questions (OQ-29-1 through OQ-29-6) remaining after the Plan29 delivery. Plan29 (v0.29.0-alpha) introduced `ILoopQualityMonitor` (loop quality monitor interface) and `IConfidenceAuditor` (confidence auditor interface), but both were mere SDK skeletons -- the Registry had wired into `PluginHooks`, type definitions were exported, yet there was no default implementation, no computation formula, no wiring to `ManoAggregator`. Master required the research team to answer: how is quality computed (OQ-1)? How does Layer 3 integrate (OQ-2)? What direction for audit strategy (OQ-3)? What is the event subscription list (OQ-4)? Should weights be configurable (OQ-5)? How does all of this fit into Plan30 (OQ-6)?

**The philosophical letter** targeted the definition of formations (samskara-skandha). Master explicitly criticized the Yogacara school's practice of lumping 49 mental factors (cetasika) into the formations aggregate as "highly problematic," and demanded deep investigation using original canonical texts (thus have I heard) as the primary source. This was not a decorative research direction -- it directly affected the foundational determination for the future expansion path of the `ISamskara` interface.

---

## SUNYATA's Dual-Track Architecture

Research Director SUNYATA designed a dual-track structure accordingly, establishing cross-track priority rules:

| Track | Scope | Sub-items | Team |
|-------|-------|-----------|------|
| Track A | AuditContext type + audit logging | A1-A4 | VITRUVIUS, KERNEL, GUARDIAN, ARCHIMEDES, WIENER, BABBAGE |
| Track B | ILoopQualityMonitor implementation spec | B1-B4 | WIENER, ATHENA, BABBAGE, HERACLITUS, TURING, PASCAL |
| Track C | Formations deep investigation | C1-C4 | NAGARJUNA, ASANGA, LINNAEUS, PENROSE, PASCAL |
| Track D | Engineering synchronization | D1-D2 | TURING, ARCHIMEDES, VITRUVIUS, GUARDIAN |

The key rule in the cross-track influence protocol: **Philosophical conclusions (D1) precede engineering design (D2/D3), ensuring that skandha-attribution determinations are not overridden by engineering convenience.** If conclusions from C1-C4 conflict with design assumptions in A/B, the engineering track must wait for the philosophical ruling.

R1 produced 14 independent research reports. R2 cross-review found 24 consensus points with only 3 points of divergence. R3 comprised three debates, 245 minutes, 17 resolutions, 13 unanimous (20/20), 0 vetoes.

This was a round of precision engineering.
