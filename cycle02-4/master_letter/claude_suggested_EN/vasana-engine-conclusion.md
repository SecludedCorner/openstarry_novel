# VasanaEngine Architecture -- Problem Analysis and Conclusion

## Original Design (Before Revision)

In the original conception, Agent cognition had two fixed speeds:

- **Gear 1 (Fast)**: VasanaEngine rule engine, ~50ms, handling previously seen patterns
- **Gear 2 (Slow)**: VitakkaEngine calling LLM, several seconds, handling complex situations

The vijnana-skandha (consciousness aggregate) decides which path to take based on matching confidence. Both Engines resided inside the ManoAggregator core.

The following analysis is based on this original conception. The final conclusion is: both Engines should be moved out of the core, and the number of gears should not be determined by architecture but by plugin composition.

---

## Three Structural Problems

### Problem One: Fast Gear Cannot Truly Skip Understanding

For VasanaEngine to match natural language input to rules, that matching step itself constitutes semantic understanding. Keyword matching is too fragile ("What time is it" vs. "What's the time now" vs. "Could you tell me the time"), while embedding matching already introduces a model. The premise of "no LLM consultation, completion in tens of milliseconds" does not hold -- the boundary between fast and slow gears is blurry.

From a Buddhist perspective, this is actually correct: even intuitive reactions driven by vasana (habitual tendencies) only occur after the conjunction (sparsha/contact) of sense faculty, object, and consciousness. There is no shortcut that completely bypasses consciousness.

### Problem Two: 70-80% Fast Gear Coverage Does Not Hold in a General Framework

The tasks users bring to an AI Agent are mostly there precisely because they are not simple. Patterns that can be exhaustively enumerated by rules are very limited in open-ended natural language scenarios; the actual ratio is likely reversed (20-30% fast gear, 70-80% slow gear). If the fast gear only covers a minority of scenarios, the return on investment of maintaining the rule base becomes questionable.

Furthermore, vasana (habitual tendencies) in Yogacara philosophy are seeds that are continuously altered through experiential conditioning -- they are not hardcoded if-then rules. If VasanaEngine lacks a learning mechanism that automatically distills new rules from slow gear results, it is merely a static lookup table and does not live up to its name.

### Problem Three: The Switching Decision Is Binary, but Confidence Is Continuous

The design mentions "matching confidence" as a continuous value from 0 to 1, but the architecture only has a binary switch (match/no match) with no handling of the gray zone. At confidence 0.6, taking the fast gear might execute the wrong action, while taking the slow gear wastes the rule engine's value. More critically, who should set the threshold -- getting the time wrong is inconsequential, but deleting a file incorrectly is catastrophic. Different scenarios and risk levels require different thresholds.

### Common Root Cause

All three problems point to the same thing: **forcing a continuous, understanding-dependent, dynamic cognitive process into a discrete, understanding-free, static binary switch.**

---

## The Fourth Problem: Contradiction with the Zero Built-in Capability Principle

All components currently in the OpenStarry core are pure mechanisms -- EventBus (routing), ServiceRegistry (registration), PluginLoader (loading), ExecutionLoop (scheduling) -- containing no domain knowledge whatsoever.

VasanaEngine breaks this pattern: it has a rule base (knowledge), matching logic (semantic judgment), and confidence scoring (decision-making). **It is not a mechanism; it is a capability.** Placing it in the core violates the "zero built-in capability" principle.

---

## Solution: Separate Mechanism from Capability

### Core Principle

The root of the contradiction lies in conflating the gear-switching "mechanism" with the VasanaEngine "capability." They should be separated.

### Final Architecture

```
ManoAggregator (Core = Pure Mechanism)
  |
  +-- IGearArbiter plugin chain (0 to N, optional)
  |     Query each registered IGearArbiter in sequence
  |     The first one whose confidence exceeds the threshold has its result adopted
  |     All below threshold -> fallback to IProvider
  |     None installed -> always go to IProvider
  |
  +-- IProvider plugin slot (fallback)
  |     Interface already exists; LLM capability comes from a plugin
  |     None installed -> Agent cannot reason (but core does not break)
  |
  +-- Threshold modulation: Klesha (existing mechanism)
```

**The core retains only:** query the IGearArbiter chain in order; if any exceeds the threshold, use it; otherwise call IProvider. This is a middleware chain pattern, identical to EventBus routing -- pure mechanism, no knowledge. The number of gears depends entirely on how many IGearArbiter plugins are installed.

### Handling of VitakkaEngine

VitakkaEngine's "capability" is not its own -- it merely assembles context and calls the IProvider plugin as a pipeline, equivalent in nature to EventBus dispatching events. But for thorough cleanliness, it should not exist as an independent component in the core either; it is simply a path through which the core calls existing plugins. Neither Engine should be in the core; only the routing mechanism belongs there.

### Degradation Behavior Under Different Plugin Combinations

The number of gears is not determined by architecture but by what plugins users install according to their scenario:

| Plugin Combination | Behavior | Applicable Scenario |
|-------------------|----------|-------------------|
| Multiple IGearArbiter + IProvider | Multi-gear waterfall fallback, full operation | High-precision scenarios |
| One IGearArbiter + IProvider | Classic dual-speed operation | Customer service bots, etc. |
| IProvider only | Everything goes through LLM, no fast path | Research-type Agents |
| IGearArbiter only | Can only handle rule-matched cases, cannot reason | Embedded IoT |
| None | Core survives but cannot cognize | -- |

---

## Buddhist Consistency

This decomposition is more correct from a Buddhist standpoint:

- Vasana (habitual tendencies) in Yogacara philosophy are **habitual patterns conditioned through posterior experience**, not innate capabilities of consciousness
- A sentient being with no vasana whatsoever still possesses complete cognitive capacity (vijnana); it simply has to cognize everything afresh
- Embedding VasanaEngine into the core = asserting that "vasana is an innate structure of consciousness" -- this does not hold in Yogacara philosophy

Therefore:

- An Agent without VasanaEngine plugins = a newborn being with no vasana, requiring deep deliberation for everything
- An Agent with VasanaEngine plugins = an experienced being capable of intuitive responses to familiar situations
- VasanaEngine rules accumulating over time = the process of vasana conditioning

Different beings have different depths of vasana -- some operate almost entirely on intuition, others deliberate over everything. This is not a difference in the structure of consciousness but in the accumulation of experience. The core (the fundamental structure of consciousness) is the same; what differs is which plugins are installed (what vasana has been accumulated).

---

## Additional Recommendations

1. **Enable VasanaEngine to learn**: Patterns processed by IProvider should automatically distill into new IGearArbiter rules, genuinely corresponding to the concept of "conditioning" (vasana)
2. **Introduce risk-aware dynamic thresholds**: Switching decisions should consider not only confidence but also the risk level of the operation; high-risk operations should prefer routing through IProvider
