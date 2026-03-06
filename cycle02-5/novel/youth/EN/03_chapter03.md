# Chapter 3: What Exactly Is SatiMonitor?

---

The second debate (D2) had to answer Master's question: which of the Five Skandhas make up the SatiMonitor component?

## First, Figure Out What It Does

SatiMonitor does four things:
1. **Subscribes to events** -- connects to the system's event stream, continuously receiving 11 different signals
2. **Remembers history** -- uses a "sliding window" to record what happened recently
3. **Recognizes patterns** -- spots things like "this behavior is repeating" or "this pattern isn't normal"
4. **Calculates quality scores** -- produces four scores (continuity, granularity, speed, balance)

What's important is what it **doesn't** do: it doesn't execute any actions, doesn't modify any state, doesn't switch any gears. It's like an ECG machine in a hospital -- it only observes, it doesn't treat.

## Four Proposals

| Proposal | Skandha Combination | Supporting Reason |
|----------|-------------------|------------------|
| A | Vedana + Samjna | Only looks at observation and recognition |
| **B** | **Vedana + Samjna + Vijnana** | **Observation + recognition + judgment, complete** |
| C | Samjna + Vijnana | Ignores the observation part |
| D | Vijnana only | Too oversimplified |

## The Turning Point

At the start of the debate, some worried that "a three-skandha plugin is too complex." But ARCHIMEDES did the math -- going from two skandhas to three only requires adding one array element, roughly a 4-line code difference.

Once this worry was eliminated, the discussion became purely about "whether the classification is accurate." The precision of three skandhas overwhelmingly beat two.

Final vote: **Proposal B (Vedana + Samjna + Vijnana) 18 votes, Proposal C 2 votes.**

SatiMonitor became OpenStarry's first "three-skandha plugin."

## Why Not Include Samskara?

Because "sati" (mindfulness) in Buddhism belongs to samskara -- it is an active, intentional practice activity. But SatiMonitor is passive, automatic quality monitoring. It's not "practicing mindfulness" -- it's just "observing."

This distinction later became very important. In the next chapter, Master would question the entire naming system because of it.

---
