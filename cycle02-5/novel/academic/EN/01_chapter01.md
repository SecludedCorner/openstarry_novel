# Chapter 1: Audit and Research

---

## R1: Independent Research

Nine independent research reports were produced during the R1 phase. Three tracks advanced in parallel.

### Track A: Five Skandha Engineering Architecture

**A1 (LINNAEUS + ASANGA)**: Five skandha sub-category tree. A complete OOP interface inheritance analysis -- IRupa splits into IListener and IUI; IVedana produces ChannelVedana (continuous signal); ISamjna corresponds to IProvider; ISamskara narrows to ITool; IVijnana is the most complex, with four sub-interfaces: IGuide, IGearArbiter, IVolition, and IKlesha. Three "weak inheritance" cases were documented -- IVedanaSensor, IGearArbiter, and IKlesha do not explicitly extend a root interface.

**A2 (VITRUVIUS + KERNEL + TURING)**: DI wiring. Pure DI, with `createAgentCore()` as the sole Composition Root, 21 components built in strict linear order, 9 Registries. Lazy Accessor pattern, Provider capability filtering, Resolver closure-based deferred resolution. A comparison matrix against Spring/Guice/InversifyJS confirmed Pure DI as the correct choice for a microkernel.

**A3 (DARWIN + MESH)**: Plugin loading lifecycle. IPlugin = Manifest + Factory. Dual loading paths (Sandbox worker thread / Direct main thread). Eight-state lifecycle state machine. Sandbox security chain: signature verification -> static import analysis -> Worker isolation -> Heartbeat -> exponential backoff restart.

**A4 (HERACLITUS + WIENER + BABBAGE)**: Five skandha execution flow. FSM with six states, nine processing phases. Phase 1 (rupa) -> Phase 3 (samjna) -> Phase 5 (vijnana) -> Phase 6 (samskara) -> Phase 7 (vedana) -> Phase 8 (vijnana). Three-layer stability loop. BABBAGE provided a complete FSM formal specification.

**A5 (LEIBNIZ + ATHENA + PENROSE)**: Cross-skandha interaction. 5x5 interaction matrix. Model Delta five-layer threshold formula. PENROSE proposed three emergence pattern hypotheses -- adaptive conservatism, bistable switching, and attention funnel.

### Track B: Buddhist Mapping Audit

**B1 (ARCHIMEDES + SCRIBE)**: Line-by-line audit of 7 documents. 50 mapping instances -- 23 KEEP (46%), 13 RELOCATE (26%), 14 REMOVE (28%). Doc 43 had the highest decoration ratio (60%). Doc 16 and Doc 31 were flagged for "full file review" (decoration ratios of 80% and 70%).

**B2 (NAGARJUNA + ASANGA + PASCAL)**: Mapping boundary principles. NAGARJUNA's Two Truths separation, ASANGA's functional positioning, PASCAL's damage asymmetry (the cumulative cognitive burden of false includes >> the one-time search cost of RELOCATE). The three tests were formally justified in this document.

### Track C: Sati Plugin

**C1 (TURING + GUARDIAN)**: Pure engineering functional analysis. SatiMonitor subscribes to 11 EventBus event types, processes through a three-stage pipeline (buffer -> batch analysis -> quality vector computation), and outputs a LoopQualityVector with four dimensions (Continuity, Granularity, Speed, Equanimity), with **zero side effects**. Engineering equivalents: APM Agent + behavioral pattern analyzer + QoS Monitor + SPC anomaly detector.

**C2 (ASANGA + LINNAEUS)**: Skandha composition proposal. Four options -- A ['vedana','samjna'], B ['vedana','samjna','vijnana'] (recommended), C ['samjna','vijnana'], D ['vijnana']. Core argument: SatiMonitor's event subscription = vedana, pattern recognition = samjna, quality assessment = vijnana. Samskara excluded -- because it performs no actions.

## R2: Cross-Review

TURING verified 40+ code references and found 4 issues (no critical errors). 24 consensus points passed without debate. 7 open questions and 4 disagreements entered the D1-D3 debates.

---
