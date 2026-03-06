# Chapter 3: A Three-Faced Mirror -- D2 Sati Plugin Skandha Classification Debate

---

**Duration**: ~60 minutes | **Chair**: SUNYATA | **Votes**: 3 items

## Renaming Strategy (D2-R1: 19/20)

Retain `Sati` as the code identifier; change the document title from "Mindfulness Architecture" to "Cognitive Loop Quality Monitoring Architecture." Add a "naming note" paragraph. Security documents use the full name.

Sole dissenting vote: GUARDIAN -- preferred complete renaming to eliminate the need for cultural background knowledge. Accepted the majority decision with the security document full-name condition.

## Five Skandha Composition (D2-R2: 18/20) -- Core Resolution

**Conclusion: skandha: ['vedana', 'samjna', 'vijnana']**

Four functions mapped to three skandhas:

| Function | Skandha | Description |
|----------|---------|-------------|
| EventBus event subscription (11 types, continuous perception) | vedana | Receives cognitive loop signals |
| Sliding window + pattern recognition | samjna | Identifies behavioral patterns from event streams |
| LoopQualityVector + SPC anomaly determination | vijnana | Evaluative quality judgment beyond descriptive recognition |
| **Executes no tools, modifies no state** | **Excludes samskara** | Not mindfulness practice |

Key argumentative turning points:

- **ASANGA**: Buddhist mindfulness (smrti) is a samskara mental factor -- active, intentional, morally positive. SatiMonitor is passive, automatic, and value-neutral. Therefore SatiMonitor is not mindfulness and should not be classified as samskara.
- **LINNAEUS**: OOP comparison -- "IGearArbiter is 'called upon to take a look'; SatiMonitor is 'always watching.'" Continuous subscription vs on-demand invocation -- sufficient to constitute an independent vedana declaration.
- **ARCHIMEDES** (turning point): The engineering cost difference between three-skandha and two-skandha is zero -- the PluginManifest's skandha field already supports multiple values. Once the concern of "three skandhas is too complex" was eliminated, discussion shifted to pure classificatory precision, where Proposal B's advantages were overwhelming.
- **Minority opinion** (MESH, KERNEL): Proposal C ['samjna','vijnana'] is symmetrical with the IGearArbiter classification and has long-term maintenance value.

**Historical significance**: SatiMonitor became OpenStarry's first three-skandha plugin.

## PluginHooks Dedicated Slot (D2-R3: 20/20)

Added `monitors?: ISatiMonitor[]` dedicated slot. Following the Cycle 02-4 `arbiters` precedent (SDK interface -> PluginHooks -> Registry -> PluginLoader four-step pattern).

---
