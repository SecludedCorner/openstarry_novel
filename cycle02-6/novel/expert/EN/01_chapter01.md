# Chapter One: Canonical Reconstruction of Formations

---

## 1.1 Methodology: Thus Have I Heard

The philosophical track was co-led by NAGARJUNA (Madhyamaka school) and ASANGA (Yogacara school). It was precisely the Yogacara approach that Master had criticized, and SUNYATA deliberately assigned the Yogacara specialist to participate in self-critique -- not as a punitive arrangement, but as a methodological necessity: only someone deeply versed in a system's internal logic can precisely identify its fracture points.

The textual hierarchy was strictly delineated:

| Level | Source | Status |
|-------|--------|--------|
| Primary | Pali Nikayas / Chinese Agamas | Sole definitional authority |
| Secondary | Dependent origination suttas (SN 12) | Structural reference |
| Tertiary | Nama-rupa-vinnana framework (SN 12.2, MN 9) | Cross-validation |
| Excluded | Abhidhamma treatises (Vibhanga, Dhammasangani) | Comparison only, not for attribution |

This stratification directly responded to Master's directive: treatises are systematization products of later scholars, not the Buddha's original words.

---

## 1.2 SN 22.56: The Six Classes of Volition -- The Original Definition of Formations

The Khandha-samyutta's SN 22.56 (Upadana Sutta) is the core source for the definition of the five aggregates:

> Monks, what are formations (sankhara-kkhandha)? There are six classes of volition (cha cetana-kaya): volition regarding forms, volition regarding sounds, volition regarding odors, volition regarding tastes, volition regarding tactile objects, volition regarding mental objects. Monks, this is called formations.

Textual analysis:

| Pali Term | Content | OpenStarry Correspondence |
|-----------|---------|--------------------------|
| rupa-sancetana | Form-volition -- intention toward visual objects | Reactive intention toward visual/text input |
| sadda-sancetana | Sound-volition -- intention toward auditory objects | Reactive intention toward audio/event input |
| gandha-sancetana | Odor-volition -- intention toward olfactory objects | Not typical for Agent scenarios |
| rasa-sancetana | Taste-volition -- intention toward gustatory objects | Not typical for Agent scenarios |
| photthabba-sancetana | Touch-volition -- intention toward tactile objects | Reactive intention toward API/tactile events |
| dhamma-sancetana | Mental-object-volition -- intention toward mental objects | Reactive intention toward internal cognitive objects |

Key insight: **In the original canonical texts, the definition of formations is entirely centered on cetana (intention/volition)** -- it describes six types of intention-formation directed at sense objects, not a "miscellaneous bin for mental activities other than feeling and perception."

---

## 1.3 SN 22.79: Constructing All Conditioned Phenomena

> Monks, why are they called formations (sankhara)? Because they construct (abhisankharonti) conditioned phenomena (sankhatam). What conditioned phenomena do they construct? They construct form as form, feeling as feeling, perception as perception, formations as formations, consciousness as consciousness.

This passage reveals a second core characteristic of formations: **Formations not only construct actions but also construct the conditioned states of all five aggregates.** In engineering terms, `ISamskara` should not be limited to external tool calls like `ITool.execute()`, but should encompass "all constructive activity that changes system state" -- including altering how the system responds to future inputs.

This directly connects to VasanaEngine's long-term roadmap (D-29-8): past behavioral patterns influencing future gear selection is precisely the engineering embodiment of "formations constructing the conditioned state of consciousness."

---

## 1.4 SN 22.95: The Plantain Simile -- A Coreless Dynamic Process

> Formations are like a plantain trunk (kadalupamo sankhara) -- if a person peels a plantain trunk seeking a solid core, they peel layer after layer and find nothing at all.

This is the classic expression of the third core characteristic of formations: **a coreless dynamic process**. Formations are not a fixed "entity" but a continuously operating "process."

The engineering correspondence is remarkably precise: `ISamskara` plugins should be lightweight and composable, not dependent on persistent internal state. Each plugin is a "layer" -- peeling away any one layer never reveals an irreplaceable core logic. This aligns perfectly with OpenStarry's Tenet #2 (Everything is a Plugin) and the microkernel architecture (Core contains no business logic).

---

## 1.5 MN 44: The Three Types of Formations as Complementary Perspectives

Visakha asked the bhikkhuni Dhammadinna:

| Formation | Pali Name | Definition | Canonical Reasoning |
|-----------|-----------|------------|-------------------|
| Bodily formation | kaya-sankhara | In-and-out breathing | A bodily phenomenon, bound to the body |
| Verbal formation | vaci-sankhara | Initial application (vitakka) + sustained application (vicara) | One first applies and sustains thought, then speaks |
| Mental formation | citta-sankhara | Perception (sanna) + feeling (vedana) | Mental phenomena, bound to the mind |

Here a tension exists between canonical frameworks: citta-sankhara (mental formation) **includes** sanna (perception) and vedana (feeling), yet in the five-aggregate framework these two are independent aggregates. NAGARJUNA's analysis: **This is not a logical contradiction, but different observation angles (drsti-bheda) of different classification systems** -- the three-formation classification observes "what conditions what," while the five-aggregate classification observes "what are the key objects of contemplative practice." The Yogacara school's attempt to forcibly unify the two systems led to the problem of cramming 49 mental factors into formations.

Engineering implication: Bodily formation corresponds to `ITool.execute()` (physical-layer construction), verbal formation corresponds to initial-and-sustained application (`vitakka-vicara`, initial cognitive processing), and mental formation corresponds to `IVedana` + `ISamjna` (already covered). Notably, `VitakkaWatchdog` in OpenStarry is a stabilization monitoring mechanism, functionally closer to consciousness than to formations -- this is not a misattribution, but rather a consequence of MN 44's verbal-formation classification and the five-aggregate classification being inherently complementary perspectives.

---

## 1.6 Critique of the Yogacara Mental Factor System

ASANGA personally led a critical analysis of the Yogacara school's 51-cetasika system (Report C2). The Yogacara school assigns 49 of 51 mental factors to formations -- leaving only "feeling" and "perception" for the feeling and perception aggregates. The item-by-item analysis yielded:

| Category | Count | Proportion | Description |
|----------|-------|------------|-------------|
| Genuinely formations | 7 | 14% | chanda, virya, apramada, mraksa, matsarya, maya, sathya |
| Already correctly attributed | 12 | 24% | Plugins already confirmed through debate in OpenStarry |
| Possibly other aggregates | 18 | 37% | Functionally closer to consciousness (judgment) or feeling (affective) |
| Mixed / requires further study | 14 | 28% | Cross-aggregate functions, requiring case-by-case analysis |

ASANGA's conclusion: "The functional descriptions in the mental factor list have reference value, but their skandha-attribution classifications have deviated from the canonical cetana-centered definition." This is not a wholesale rejection of Yogacara -- rather, it draws a clear methodological distinction between canonical texts and treatises.

---

## 1.7 Three Criteria and the Core Distinction

LINNAEUS distilled from the canonical analysis the "Three Criteria for Formations Attribution," established as a permanent determination tool [D1-R3, 20/20]:

1. **Conditioning**: Does it create / change / produce new states?
2. **Cetana-driven**: Is it driven by the intention-formation process?
3. **Environmental Shift**: Does it alter subsequent cognitive conditions?

All three "yes" -> formations (samskara); all three "no" -> consciousness (vijnana); mixed -> requires case-by-case analysis, possibly cross-aggregate.

PENROSE further compressed this into a distinction immediately graspable by any programmer:

> **Formations = WRITE** (actively changing the world's state)
> **Consciousness = READ** (passively evaluating the world's state)

Correspondence in the OpenStarry codebase:

| Skandha Attribution | Interface | Operation Type | Code Path |
|--------------------|-----------|---------------|-----------|
| Formations (WRITE) | `ITool` | Tool execution, changes environment | `types/aggregates.ts#ISamskara` |
| Formations (WRITE) | `ISlashCommand` | Command execution, changes state | `types/aggregates.ts#ISamskara` |
| Consciousness (READ) | `IGuide` | Evaluative guidance, no state change | `types/aggregates.ts#IVijnana` |
| Consciousness (READ) | `IVolition` | Deliberative judgment, no state change | `types/aggregates.ts#IVijnana` |

This WRITE/READ distinction was unanimously confirmed by D1-R5 (20/20), becoming the operational principle for skandha attribution.
