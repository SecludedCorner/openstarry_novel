# Vedana (Feeling Aggregate) Engineering Design: Four Pending Questions

---

## Preliminary Context: Vedana's Position in the Overall Architecture

Before discussing specific problems, we need to anchor vedana's relationship to the overall architecture. Three Master's Letters have established the following constraints:

**Three-layer architecture.** Vedana's design follows the ATHENA (sensor) -> WIENER (computation engine) -> NAGARJUNA (conceptual framework) three-layer structure. The three-layer architecture does not revolve solely around suffering -- pleasure and equanimity must be symmetrically designed into the system.

**Co-arising completeness.** When contact (sparsha) arises, feeling (vedana), perception (samjna), and volition (cetana) emerge as an inseparable whole. There cannot be "feeling without perception" or "perception without feeling." The Agent must pass a completeness check before startup -- if vedana is incomplete, the Agent should not start.

**OOP inheritance structure.** VedanaPlugin is the base class; the three feelings (sukha/pleasure, dukkha/suffering, upekkha/equanimity) inherit from it. Concrete sensors hold instances of feeling through composition, transforming raw data into feeling intensity.

**Distinction between vedana and observers.** Observers that purely perform "data integrity and authenticity" checks can be composed solely of vedana. Observers that participate in "emotional reactions" require intervention from vijnana-skandha (consciousness aggregate) and samjna-skandha (perception aggregate).

All four questions below must be discussed within these constraints.

---

## I. Continuity of Valence -- Storage Format Does Not Equal Signal Quality

### Current State

Vedana's valence uses a continuous floating-point number (-1 to +1), justified by the control engineering chattering problem: discrete classification produces square-wave jumps at threshold boundaries, while continuous values allow stable controller output. This design direction is correct.

However, continuous storage format is only a necessary condition, not a sufficient one. **The continuity of valence is a systemic property that must be guaranteed across the entire signal chain from source to consumer.**

### Problem

The signal source for valence is a rule engine -- mapping cognitive events to numerical values ("tool call failed -> -0.3", "task completed -> +0.5"). The events themselves are discrete, and the mapping to values is also discrete. Even stored as `f64`, what the controller sees is still a staircase of jumps, not a smooth curve. The chattering problem has not been solved; it has merely been relocated from the storage layer to the signal source layer.

LLM evaluation is not a substitute. LLM calls are samjna-skandha's work (500ms-30s) and cannot be invoked every vedana cycle (10-100ms); moreover, LLM numerical outputs are inherently unstable.

### Mapping to the Three-Layer Architecture

This problem can be precisely located within the three-layer architecture:

| Layer | Role | Output |
|-------|------|--------|
| ATHENA (Sensor Layer) | Produces coarse raw observations | Discrete jumps, smoothness not required |
| WIENER (Computation Engine Layer) | Bayesian filtering, incremental updates | Smooth continuous valence estimate |
| NAGARJUNA (Conceptual Framework Layer) | Threshold classification, semantic interpretation | Derived labels (dukkha/sukha/upekkha) |

The guarantee of continuity occurs at the **second layer**, not at the first layer or in the storage format.

### Proposed Approach

The klesha (affliction) signal design has already established a Bayesian incremental update framework -- belief moves gradually with observations, and inertia increases with the number of observations, naturally forming a smooth curve. Valence should follow the same path:

1. Sensors at the ATHENA layer produce **coarse raw observations** (from the rule engine or specific sensor plugins; jumps are permissible)
2. The computation engine at the WIENER layer feeds observations into a **Bayesian filter**, performing weighted fusion with prior belief
3. The filter's output is the **current estimate of valence**, consumed by the controller and the co-arising completeness check

### Pending Items

- Should klesha signals and vedana valence share the same filtering framework, or operate independently?
- The filter's output format must simultaneously satisfy two consumers: the controller (requires continuous values) and the co-arising completeness check (needs confirmation that vedana signals are ready). Are these two interface requirements in conflict?

---

## II. Valence Distribution -- The Meaning of Thresholds Depends on the Shape of the Distribution

### Current State

The classification threshold defaults to 0.1. The valence range for upekkha (equanimity) is -0.1 to +0.1; the total valence space spans 2; therefore upekkha accounts for 10%, dukkha for 45%, and sukha for 45%. The threshold is configurable; the default value's Buddhist justification is "an untrained mind is rarely at peace."

### Problem

The above calculation assumes valence is **uniformly distributed** between -1 and +1. But during normal Agent operation, most of the time no extreme events occur, and valence concentrates near zero. The actual distribution is more likely a bell curve centered at zero.

Under different distribution assumptions, the same threshold produces vastly different upekkha proportions:

| Assumed Distribution | Standard Deviation | Upekkha Proportion (Threshold 0.1) |
|---------------------|-------------------|-----------------------------------|
| Uniform distribution | -- | 10% |
| Normal distribution | sigma = 0.5 | ~16% |
| Normal distribution | sigma = 0.3 | ~26% |
| Normal distribution | sigma = 0.2 | ~38% |

If valence follows a normal distribution with sigma=0.3, even without changing the threshold, the Agent spends over a quarter of its time in upekkha -- contradicting the design intent of "rarely at peace."

The deeper issue: valence distribution is not fixed; it changes dynamically with Agent state. **Whether a threshold value is appropriate cannot be statically determined at design time; it must be calibrated at runtime after observing the actual distribution.**

### Recommendations

1. **Keep the default threshold at 0.1, but annotate the assumed distribution model in documentation.**
2. **Provide a runtime distribution observer.** Record the Agent's valence values over the past N cycles, calculate the actual upekkha proportion. When the actual proportion deviates too much from the design intent, emit a parameter adjustment recommendation.
3. **Treat distribution shape as an Agent state observation metric.** The skewness of the valence distribution reflects whether the Agent chronically leans toward dukkha or sukha; the kurtosis reflects the amplitude of emotional fluctuation. These statistics are themselves meaningful "vedana metadata."

### Skandha Attribution of the Observer

Per Master's Letter's distinction regarding observers: if the distribution observer only performs statistics (computing mean, standard deviation, skewness), it is a pure "data integrity" observer and can be composed solely of vedana. If it needs to judge "an abnormal distribution indicates a problem with Agent state requiring adjustment," that involves samjna-skandha's recognition and sankhara-skandha's decision-driving, and should be a cross-skandha composite plugin. The recommendation is to first implement the pure statistics version (internal to vedana), leaving judgment logic to upper layers.

### Note

This is the only one of the four questions with no coverage by any existing design -- a fully open gap.

---

## III. Boundaries of the Two-Dimensional Model -- Sense of Control Belongs to Sankhara-skandha, Not Vedana

### Current State

Vedana's valence model uses two dimensions: valence (-1 to +1) and intensity (0 to 1), citing Russell's Circumplex Model as its scientific basis.

Some in the psychology community argue that two dimensions are insufficient. Mehrabian's PAD model adds a third dimension -- dominance (sense of control). Anger and fear may have the same valence and intensity, but their dominance is completely different: one feels empowered in anger but powerless in fear.

### Conclusion: Vedana Does Not Need a Third Dimension

Dominance -- feeling empowered versus powerless when facing difficulty -- does not belong to vedana; it belongs to sankhara-skandha (the volitional formations aggregate). Master's Letter has explicitly stated that sankhara-skandha's scope is broad: "it is not limited to changes affecting rupa; internal mechanism state changes are also included." The stance, driving force, and dispositions one takes toward suffering and pleasure are all sankhara-skandha's work.

This yields a cleaner architectural division of responsibility:

| Skandha | What It Governs | Corresponding Dimension |
|---------|----------------|----------------------|
| **Vedana** | The texture of suffering and pleasure | Valence + Intensity (two-dimensional) |
| **Sankhara-skandha** | The stance taken toward suffering and pleasure | Dominance, drive direction, dispositions |

Russell's two-dimensional model is sufficient as the engineering framework for vedana; there is no need to force a third dimension into vedana. The prerequisite is that sankhara-skandha adds dominance-related logic on its side.

This also echoes Master's Letter's five-skandha division of labor principle -- vedana is the Input Signal (signal texture), sankhara-skandha is the Process (volitional drive). Dominance is part of volition, not part of signal texture.

### Notes

1. **Terminology alignment.** The current design's "intensity" has a conceptual difference from Russell's "arousal." Arousal refers to physiological activation level (excited vs. calm); intensity refers to the vividness of feeling. The two overlap in most cases but are not identical. The design document should explicitly state the relationship between this system's intensity and Russell's arousal.
2. **Reserve extensibility in the data structure.** Even though two dimensions are currently sufficient, the feeling data structure should be designed as extensible (e.g., `VedanaRecord { valence: f64, intensity: f64, metadata: HashMap<String, f64> }`), adding no complexity but leaving room for future needs.

---

## IV. Plugin Implementation at the Processing Layer -- Divide by Function, Coordinate Through Event Streams

### Current State

Vedana's design has established a dual-layer architecture: the data layer is continuous (valence is a float, labels are derived), while the processing layer is discrete (there can be dedicated components handling different feelings). Master's Letter further confirms that a Plugin can simultaneously possess multiple skandha attributions, and that inter-Plugin communication should adopt an event-driven pub/sub model.

### Alignment with the OOP Inheritance Structure

Master's Letter (Cycle 02-2) established VedanaPlugin as the base class, with the three feelings inheriting from it, and concrete sensors holding feeling instances through composition. Functional plugin implementation must be compatible with this structure:

```
VedanaPlugin (Base)
  +-- Dukkha (Suffering)
  +-- Sukha (Pleasure)
  +-- Upekkha (Equanimity)

Concrete Sensor Plugin (e.g., CollisionRiskSensor)
  -> Holds a Dukkha instance through Composition
  -> Transforms raw data into valence

Functional Processing Plugin (e.g., AvoidanceTrigger)
  -> Subscribes to the valence event stream
  -> Independently determines response intensity via continuous activation function
  -> Skandha attribution: vedana + sankhara-skandha (cross-skandha composition)
```

The three feelings' inheritance structure handles **sensing and generation** (from raw data to valence); functional plugins handle **consumption and response** (from valence to behavioral tendency). The two do not conflict; they are upstream and downstream in the data flow.

### Implementation Approach

Processing-layer plugins should be **divided by function, not by feeling category.** Instead of a "dukkha processor" and a "sukha processor," design "avoidance behavior trigger," "approach behavior trigger," "balance maintainer," and similar functional plugins.

Rationale:

1. **Avoid routing-layer chattering.** If three plugins are divided by dukkha/sukha/upekkha, a central router must dispatch based on thresholds. When valence fluctuates slightly around the threshold boundary (-0.09 <-> -0.11), the routing layer will repeatedly switch between two handlers, each switch incurring state reconstruction costs.
2. **Aligns with microkernel philosophy.** Each plugin subscribes to the valence event stream and independently determines whether and how strongly to respond via its continuous activation function, requiring no central router.
3. **Aligns with multi-skandha attribution principle.** An "avoidance behavior trigger" naturally belongs to both vedana (reading valence) and sankhara-skandha (driving avoidance behavior), without requiring artificial separation.
4. **Aligns with Agent completeness requirements.** A complete Agent requires the aggregation of all five skandhas. Functional plugins are inherently cross-skandha compositions, naturally tending toward completeness.

### Pending Implementation Details

1. **Activation function design.** Each functional plugin uses a continuous function to determine response intensity, e.g., "avoidance behavior trigger" response intensity = `max(0, -valence - threshold) * intensity`. No hard threshold switching, naturally eliminating boundary chattering. The specific function form and parameters need to be determined experimentally.
2. **Multi-plugin conflict arbitration.** At valence -0.7, the "avoidance behavior trigger" and the "alert escalator" may both activate simultaneously. Through pub/sub they can each respond independently, but ultimately an arbitration mechanism is needed -- this should be the work of sankhara-skandha's IVolition.deliberate() two-stage deliberation (the global deliberation stage evaluates whether multiple plugins' suggestions conflict).
3. **Hysteresis mechanism.** Even with continuous activation functions, it is recommended to add hysteresis between plugin activation and deactivation: set different activation and deactivation thresholds to avoid repeated start-stop cycling near the boundary.
4. **Skandha attribution of sensor plugins.** Per Master's Letter's ultrasonic sensor example, sensors hold instances of the three feelings through composition, transforming raw data into valence. Sensor plugins' skandha field should be marked as rupa-skandha (physical sensing) + vedana (feeling generation), i.e., multi-skandha attribution.

---

## Summary

| Problem | Conclusion | Next Steps |
|---------|-----------|------------|
| Valence continuity | Continuity is guaranteed by the WIENER layer's filter, not by the data type | Decide whether valence shares the klesha signal's Bayesian filtering framework; confirm filter output simultaneously satisfies the controller and co-arising completeness check |
| Valence distribution and thresholds | Threshold meaning depends on distribution shape; runtime calibration needed | Design a runtime distribution observer (pure statistics version, internal to vedana); annotate the distribution assumption underlying the threshold |
| Two-dimensional model boundaries | Two dimensions are sufficient; dominance belongs to sankhara-skandha | Terminology alignment; reserve extensibility in the data structure |
| Processing-layer plugin implementation | Divide by function, coordinate through event streams, continuous activation functions | Activation function design, conflict arbitration, hysteresis mechanism, sensor skandha attribution confirmation |

**Priority recommendation:** Problem I has the smallest gap but is the most critical -- what is missing is merely the explicit extension of the klesha signal filtering framework to vedana valence; once confirmed, it can be written into the interface definition. Problem II is the only fully open gap but does not block implementation; it can be iterated at runtime. Problems III and IV have established architectural directions and are entering the implementation detail phase.
