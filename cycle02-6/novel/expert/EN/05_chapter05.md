# Chapter Five: Master's Cetasika Directive and Permanent Rules

---

## 5.1 Trigger: The Chain Reaction of Mental Factor Analysis

The philosophical track's C2 report (critical analysis of the Yogacara cetasika system) was presented to DC Master during R2 cross-review. ASANGA had compiled item-by-item re-attribution recommendations for all 51 mental factors -- 18 of which (37%) were judged functionally closer to the consciousness or feeling aggregates rather than formations.

Master's response was not a single ruling, but three rounds of progressive refinement. Each round sharpened the focus further.

---

## 5.2 First Round: Methodological Demarcation Between Canon and Treatise

Master's core thesis: **Mental factors (cetasika) are systematization products of treatises (Abhidharma), not content from the original suttas/agamas.**

This is not scholarly bias. The Buddha spoke in the original canon of the five aggregates, dependent origination, the Noble Eightfold Path, and the thirty-seven factors of awakening. The classification system of "51 mental factors" was the systematic compilation of later scholars (particularly Yogacara masters such as Asanga and Vasubandhu). The original texts do mention many cetasika names (such as prajna, virya, hri, apatrapya), but **organizing them into a fixed-count classification system and assigning skandha attributions** was the treatises' work.

Master's direct conclusion: **Plugin names must not use Sanskrit cetasika names.**

Engineering impact: Any plugin named with a Sanskrit cetasika term (e.g., VīryaPlugin, PrajnaPlugin) must be renamed to engineering terminology.

---

## 5.3 Second Round: Preserving Functional Reference Value

The first round could easily be misread as "cetasikas are entirely useless." Master corrected this impression in the second round: the **functional descriptions** of mental factors retain reference value.

For example, the cetasika "virya" (diligence/energy) describes the function of "persistent, unwavering commitment to wholesome states." One can reference this functional description when designing a plugin -- but the plugin must not be called VīryaPlugin; it should use an engineering name (e.g., `PersistencePlugin`, `RetryPlugin`).

Master's precise formulation: "It is acceptable to say 'we referenced the meaning of virya and designed a retry plugin.' It is not acceptable to say 'the retry plugin = virya.'"

This is the principle of "may cite, may not equate."

---

## 5.4 Third Round: Naming Decoupling Yields Attribution Freedom

The third round was the most profound. Master said: "A plugin is not a cetasika."

On the surface this seems straightforward. But its implications are structural.

In the Yogacara school, each cetasika has a fixed skandha attribution -- "virya" belongs to formations, "prajna" belongs to consciousness. If plugin = cetasika, then the plugin's skandha attribution is also locked in. But plugin != cetasika. A plugin may simultaneously have both formations and consciousness functions -- it both makes judgments (READ) and executes actions (WRITE).

Under the cetasika system this is impermissible (each cetasika belongs to exactly one skandha), but under the plugin system it is entirely legitimate. **Naming decoupling yields attribution freedom** -- not using cetasika names for plugins actually liberates plugins from the fixed classificatory constraints of treatises, allowing them to naturally span multiple aggregates.

---

## 5.5 Eight Permanent Rules

The three rounds of directives were consolidated into eight permanent rules, which together with the five skandha-attribution principles form the judgment baseline for all future naming and attribution questions:

| # | Rule | Engineering Impact |
|---|------|--------------------|
| 1 | Cetasikas are treatise products, not original canonical content | Do not use the cetasika system as the default framework for architectural design |
| 2 | Cetasika functional descriptions have reference value, suitable as plugin design inspiration | Design documents may cite cetasika functional descriptions |
| 3 | It is valid to state "referenced cetasika X's meaning to design plugin Y" | Design provenance is legitimate; equivalence claims are not |
| 4 | Plugins use engineering terminology for naming; Sanskrit cetasika names are prohibited | Hard naming convention rule |
| 5 | Sanskrit terms are limited to those from original canonical texts -- skandha, sparsha are permitted | Distinguishes canonical Sanskrit from treatise Sanskrit |
| 6 | Cetasika classifications do not serve as skandha-attribution evidence | "Yogacara says X belongs to formations" cannot serve as plugin attribution evidence |
| 7 | Existing plugin attribution decisions are unaffected | Already-confirmed attributions are not overturned by the new rules |
| 8 | Plugin != cetasika; skandha attribution may naturally span multiple aggregates | Cross-aggregate plugins are legitimate and expected |

---

## 5.6 Five Skandha-Attribution Principles [D1-R6, 20/20]

Complementing the eight rules, the five principles provide a positive determination method:

1. **Functional analysis is the sole basis for skandha attribution** -- not names, not tradition, not treatises
2. **The Yogacara 51-cetasika system serves as a functional reference list, not an attribution authority**
3. **Sanskrit terms used in code naming are limited to those originating from the original canon**
4. **Plugin != cetasika; skandha attribution may naturally span multiple aggregates**
5. **Existing attribution decisions (based on functional analysis) remain valid**

These five principles plus the eight rules form a complete determination framework. In the future, whenever someone asks "which skandha does this function belong to" or "what should this plugin be named," there is no need to debate from scratch -- simply consult these 13 rules.

---

## 5.7 Cascading Revisions to the D1 Agenda

Master's three rounds of directives directly led to revisions of the D1 debate agenda:

- **D1-Q2 (cetasika multi-aggregate attribution problem) was deleted** -- since cetasika classifications are not used as a basis, debating their multi-aggregate attribution loses its purpose
- **D1-Q6 (item-by-item vote on 26 cetasikas) was simplified** -- changed to voting on the attribution principles themselves, not case-by-case determinations
- **The manasikara supplementary agenda item was canceled** -- `CoarisingBundle` does not include manasikara as an independent interface, requiring no further discussion

These revisions saved at least 45 minutes of debate time while elevating the abstraction level of the resolutions -- from case-by-case rulings to principle establishment.

---

## 5.8 Engineering Applicability Assessment of Buddhist Mind Theories [D1-R4a/b/c]

The C4 report (PASCAL + PENROSE) conducted a systematic assessment of the engineering applicability of all Buddhist mind theories:

| Theory | Conclusion | Resolution | Test Results |
|--------|-----------|------------|-------------|
| Five Aggregates | Already fully integrated | No action needed | -- |
| Nama-rupa-vinnana | Core value already absorbed | No action needed | -- |
| Dependent Origination | Explanatory appendix | 02-7 P2 [D1-R4a, 19/20] | -- |
| Eight Consciousnesses | Awaiting multi-Agent scenarios | Cycle 03+ | -- |
| **Four Wisdoms** | **Excluded** | **D1-R4b, 18/20** | All four tests failed |
| Cognitive Sequence | Strongest structural correspondence | 02-7 P2 [D1-R4a, 19/20] | -- |

The exclusion of the Four Wisdoms (adarsa-jnana, samata-jnana, pratyaveksana-jnana, krtyanusthana-jnana) was particularly significant. Four exclusion tests:

1. **Removal test**: Does removing the Four Wisdoms mapping change any design? -> No
2. **Code existence test**: Do the Four Wisdoms have counterparts in the codebase? -> No
3. **Driving force test**: Did the Four Wisdoms drive any engineering decision? -> No
4. **Irreplaceability test**: Is there a simpler engineering concept that can substitute? -> Yes

2 dissenting votes argued they could be retained as reference material. But all four tests failed -- retaining them would only increase cognitive load without adding design value.

---

## 5.9 ISamskara Expansion Directions [D1-R3, 20/20]

Confirmed the Cycle 02-5 D3-R4 resolution: no new ISamskara sub-interfaces at this time. Four directions are archived as long-term candidates:

| Direction | Description | Priority | Timeline |
|-----------|-------------|----------|----------|
| A: cetana-formation | Intention planning -- expanding from "execute tool" to "form intention" | P2 | Cycle 03+ |
| B: vasana-imprinting | Habit formation -- learning and memory of behavioral patterns | P2 | Long-term (VasanaEngine) |
| C: kaya extension | Environmental transformation -- extension of bodily formation | P3 | No scheduling needed |
| D: vaci | Communication formation -- extension of verbal formation | P3 | No scheduling needed |

Directions A and B directly relate to the canonical analysis: cetana-formation corresponds to SN 22.56's six classes of volition (the intention-formation process), and vasana-imprinting corresponds to SN 22.79's "constructing all conditioned phenomena" (behavior shaping future conditions). Direction B's VasanaEngine is already scheduled in D-29-8 as a long-term roadmap item.

NAGARJUNA's summary: "Last round we learned what not to do. This round we learned why not to do it."
