# Chapter 1: Canonical Reconstruction of Samskara -- From Cetana-Centrality to Functional Attribution Criteria

---

## 1.1 The Problem: Samskara as a "Residual Category"

Within the panca-skandha (five aggregates) architecture of OpenStarry v0.2.0-beta, the samskara-skandha (formations aggregate) has long suffered from definitional insufficiency. Compared to the clear functional mappings of rupa-skandha (form aggregate, corresponding to the `ISparsha` sensory contact interface), vedana-skandha (feeling aggregate, corresponding to the `IVedana` feeling interface), samjna-skandha (perception aggregate, corresponding to the `ISamjna` recognition interface), and vijnana-skandha (consciousness aggregate, corresponding to the `IManas` judgment interface), the samskara-skandha possesses only a single sub-interface `ITool`, responsible for external tool invocation.

This asymmetry is not accidental. Its root lies in the Yogacara school's treatment of the samskara-skandha. In the Yogacara classification system of fifty-one cetasika (mental factors), the vedana-skandha is assigned only one cetasika -- vedana (feeling) -- and the samjna-skandha is assigned only one -- samjna (perception). The remaining forty-nine cetasika are all subsumed under the samskara-skandha. The samskara-skandha thereby becomes a "residual category" -- any mental function that does not belong to feeling or perception is categorically assigned to formations.

DC Master explicitly identified this practice as "highly problematic" in the research mandate and required the team to return to the original sutras (evam maya srutam) to re-establish a functional definition of samskara.

---

## 1.2 The Definition of Samskara in Original Sutras

The philosophical track was led by NAGARJUNA (#7, Madhyamaka philosopher) and ASANGA (#8, Yogacara scholar). A noteworthy methodological arrangement: the expert representing the school under critique (Yogacara) was assigned to examine the problems of his own school, ensuring the internality and depth of the criticism.

### 1.2.1 The Six Cetana Groups: Cetana as the Defining Characteristic of Samskara

In the Samyutta Nikaya (SN 22.56, Khandha-samyutta), the Buddha defines the samskara-skandha with explicit precision:

> "And what are formations? There are these six groups of cetana (intention): cetana regarding form, cetana regarding sound, cetana regarding smell, cetana regarding taste, cetana regarding touch, cetana regarding mental objects. These are called formations."

Here "cetana" denotes intention/volition; the "six cetana groups" (cha cetana-kaya) refer to intentional responses directed toward six categories of sensory objects. The critical feature of this definition lies in its **exclusivity**: the samskara-skandha is not "everything mental except feeling and perception," but rather points precisely to cetana -- intentional fabrication directed at six types of objects.

### 1.2.2 The Fabrication Function: Abhisamskara and the Conditioning of Conditioned Phenomena

The Samyutta Nikaya (SN 22.79) further elucidates the function of samskara:

> "Formations fabricate form's conditioned state (rupam abhisankharonti)."

The verb abhisankharoti indicates that samskara does not merely "execute actions" but, more fundamentally, "fabricates" -- it creates conditions, modifies states, and influences subsequent cognitive processes. The fabricating function of samskara extends even to the other four aggregates: it can fabricate the conditioned state of form, the conditioned state of feeling, and even the conditioned state of consciousness.

### 1.2.3 The Plantain Simile: A Coreless Dynamic Process

The Samyutta Nikaya (SN 22.95, Phena-sutta) uses the plantain tree (kadali) as a simile for samskara:

> "Suppose a person were to strip a plantain trunk, seeking heartwood. They would peel it layer by layer and find nothing solid within."

This simile points directly to the ontological status of samskara: it is not an "entity" with a solid core, but rather a continuously operating "process." Each layer of fiber is a conditional fabrication; once peeled away, no intrinsic nature (svabhava) is found.

---

## 1.3 Three Core Characteristics

Based on the above canonical texts, the research team distilled three core characteristics of samskara:

| # | Characteristic | Canonical Basis | Functional Implication |
|---|---------------|-----------------|----------------------|
| 1 | **Cetana-centrality** | SN 22.56 (six cetana groups) | Samskara is defined by intention, not as a "residual category" |
| 2 | **Fabrication of all conditioned phenomena** | SN 22.79 (abhisamskara) | Samskara creates conditions, modifies states, affects all five aggregates |
| 3 | **Coreless dynamic process** | SN 22.95 (plantain simile) | Samskara is a process rather than an entity; no intrinsic nature is found |

---

## 1.4 Three Criteria for Samskara Attribution

Building on these three characteristics, LINNAEUS (#13, Taxonomy/Ontology Expert) proposed an operationalizable set of attribution tools -- the Three Criteria for Samskara Attribution:

**Criterion 1: Fabrication**
- Does the function create, modify, or produce new states?
- Test: Check whether the function's output modifies system state or the external environment.

**Criterion 2: Cetana-driven**
- Is the function driven by cetana (intention)?
- Test: Check whether the function's trigger originates from a volitional decision of the system, rather than a passive reaction.

**Criterion 3: Environmental Modification**
- Does the function alter subsequent cognitive conditions?
- Test: Check whether, after the function executes, the input space of subsequent cognitive loops has changed.

The three criteria were confirmed by Resolution D1-R3 as a **permanent tool**, applicable to all future aggregate-attribution determinations.

---

## 1.5 The WRITE/READ Dichotomy

PENROSE (#18, Quantum Consciousness Researcher) proposed a highly generalizable dichotomy during discussion:

> **Samskara = WRITE (actively changing the world)**
> **Vijnana = READ (passively evaluating the world)**

This dichotomy has a natural counterpart in computer science. In operating system theory, WRITE operations modify system state (side-effecting operations), while READ operations merely observe system state (pure-function operations). Mapped to OpenStarry's code:

| Operation Type | Aggregate Attribution | Code Interface | Function |
|---------------|----------------------|---------------|----------|
| WRITE | samskara-skandha | `ITool`, `ISlashCommand` | Execute actions, modify environment |
| READ | vijnana-skandha | `IGuide`, `IVolition` | Evaluate situations, render judgments |

This dichotomy was formally confirmed by Resolution D1-R5 (20/20 unanimous) and became the core articulation of the "activity and transformation" principle.

---

## 1.6 Critical Analysis of the Yogacara Cetasika System

ASANGA personally led the critical analysis of the Yogacara fifty-one cetasika system (Report C2). Using the Three Criteria for Samskara Attribution as the analytical instrument, he examined each of the 49 cetasika assigned to the samskara-skandha by the Yogacara school. The results were as follows:

| Classification | Count | Percentage | Description |
|---------------|-------|-----------|-------------|
| Confirmed samskara | 7 | 14% | chanda (desire-to-act), virya (diligence), apramada (non-negligence), etc. |
| Already correctly attributed | 12 | 24% | Already assigned correct attribution in OpenStarry via functional analysis |
| Possibly belonging to other aggregates | 18 | 37% | Functionally closer to vijnana (e.g., prajna/wisdom) or vedana |
| Mixed / requiring further study | 14 | 28% | Requiring finer-grained functional analysis or cross-aggregate treatment |

The methodological significance of this analysis lies in replacing traditional taxonomy with functional analysis as the basis for aggregate attribution. As ASANGA himself stated:

> "The cetasika list is a useful catalog of functional descriptions, but it is a product of the Abhidharma treatises, not the Buddha's own words. We may consult its functional descriptions, but we must not allow its classificatory scheme to determine aggregate attribution."

---

## 1.7 Five Permanent Principles for Aggregate Attribution

Based on the above research, Resolution D1-R6 (20/20 unanimous) established five permanent principles:

1. **Functional Analysis Principle**: Functional analysis is the sole basis for aggregate attribution.
2. **Cetasika Reference Principle**: The Yogacara fifty-one cetasika system serves as a functional reference list, not as a basis for attribution.
3. **Sanskrit Restriction Principle**: When Sanskrit terms are used in code naming, they are restricted to those originating from original sutras (e.g., skandha, sparsha); Sanskrit names coined in Abhidharma treatises for cetasika shall not be used.
4. **Cross-Aggregate Attribution Principle**: A Plugin is not equivalent to a cetasika; aggregate attribution may naturally span multiple aggregates.
5. **Existing Resolution Principle**: Existing attribution resolutions (based on functional analysis) remain valid.

These five principles, together with the Master's Eight-Point Rules discussed in Chapter 5, constitute the permanent adjudication framework for all future naming and attribution questions in OpenStarry.

---
