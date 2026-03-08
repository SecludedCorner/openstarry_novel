# Chapter 4: Two Independent Pipelines

---

## A Seemingly Simple Question

The quality monitor has computed a quality score. The auditor can adjust confidence. But how do they actually influence the Agent's decisions?

In OpenStarry, the core logic of the Agent's decision-making is a comparison:

```
If (confidence > threshold) -> use the arbiter's recommended plan
Otherwise -> use the default plan
```

Confidence is the arbiter's degree of certainty in its recommended plan. The threshold is the system's "minimum standard." If confidence exceeds the threshold, the recommendation is adopted; if not, the system takes the safe default route.

Now two new actors want to participate in this comparison:
- **The auditor** wants to adjust confidence ("I think the arbiter is too confident — the confidence should come down a bit")
- **The quality monitor** wants to say "The Agent has been performing well lately; the standard can be relaxed a little"

The question is: how should they intervene?

---

## Option C: Each Minds Its Own

The team considered three options. The one that passed unanimously was Option C — two independent pipelines.

**Pipeline One (Layer 2)**: The auditor adjusts confidence.

```
new confidence = old confidence + auditor's adjustment (clamped to plus or minus 0.05)
```

**Pipeline Two (Layer 3)**: The quality monitor adjusts the threshold.

```
new threshold = max(floor value, old threshold * (1 - 0.10 * quality score))
```

Then the new confidence and new threshold are compared.

Why is this good design?

**First, independence.** The two pipelines don't interfere with each other. The auditor doesn't know the quality score, and the quality monitor doesn't know the audit result. It's like two departments each making their own adjustments — finance adjusts the budget (confidence), HR adjusts the standard (threshold) — without overstepping each other's authority.

**Second, stability.** Because the two pipelines have no cross-terms (they don't influence each other), BABBAGE could mathematically prove the system is BIBO stable — bounded input always produces bounded output.

**Third, controllability.** Each pipeline has clamping: the auditor can adjust at most plus or minus 0.05, and the quality monitor's influence coefficient alpha is fixed at 0.10. It's like a steering wheel with a maximum turning angle — you can turn, but you can't spin the car 180 degrees.

**Fourth, conservative degradation.** If there's no quality monitor, quality score Q = 0, and the threshold doesn't change at all. If there's no auditor, the adjustment = 0, and confidence doesn't change at all. When either component is missing, the system behaves exactly as it would without them — it doesn't suddenly become more dangerous.

WIENER looked at the design and said: "This is the cleanest separation I've ever seen."

---

## How the Quality Score Gets There

The quality monitor has computed a score — how does it reach ManoAggregator (the component responsible for making the final decision)?

The team designed a dual-channel approach:

**Channel One (pull)**: ManoAggregator "pulls" the quality score on its own. When it needs to make a decision, it calls a `loopQualityFn()` callback, and the quality monitor returns the latest score.

**Channel Two (push)**: The quality monitor proactively "pushes" quality information into the extras bag. It emits an `audit:context_contribute` event via EventBus, placing the four-dimensional scores and the composite score into the bag so the auditor can see them too.

Why two channels? Because the two consumers have different needs. ManoAggregator needs a real-time number (to calculate the threshold). The auditor needs rich contextual information (to make its judgment).

LEIBNIZ (the multi-agent cooperation expert) emphasized one particular point: "The quality score's lifetime is per-routing-cycle. After each routing cycle ends, the bag is emptied. No accumulation."

It's like handing out a fresh agenda before every meeting. The last meeting's agenda doesn't stay on the table to influence the current one.

---

## The Five-Layer Model

Adding the previously existing Layer 0 (EventBus events), Layer 1 (klesha gain), and Layer 4 (urgent feeling), the entire decision flow now has five layers:

```
L0: EventBus - foundational event stream
L1: Klesha (afflictions) - four emotional modules adjust the threshold
L4: Vedana (feeling urgency) - urgent feelings directly lower the threshold
L3: LoopQuality - quality score fine-tunes the threshold
L2: Audit - auditor fine-tunes confidence
-> Final comparison -> routing decision
```

The layer ordering is deliberate: L4 (urgent feeling) takes priority because it handles safety-critical situations; L3 (quality) comes next; and L2 and the final comparison come last.

It's like a building safety inspection: first check for fires (L4), then check building quality (L3), then look at interior finishing details (L2). Priority runs from life-threatening to fine-tuning.

---
