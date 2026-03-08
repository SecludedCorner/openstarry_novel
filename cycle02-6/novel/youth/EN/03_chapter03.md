# Chapter 3: Quality in Four Dimensions

---

## How Do You Know If the AI Is Doing Well?

Imagine you're tutoring a student in math. How do you tell if they're learning well?

You can't just look at their accuracy — maybe they're just lucky guesses. You'd want to know more: Is their method consistent? Do they keep switching strategies? Are they getting better over time or just spinning their wheels?

OpenStarry's quality monitor (LoopQualityMonitor) faces the same problem. It needs to evaluate the AI Agent's cognitive loop — the Agent receives a message, thinks, makes a decision, executes, then receives the next message — and assess how well that cycle is running.

WIENER and ATHENA (the AI/ML expert) led the team in designing four dimensions:

---

## Four Yardsticks

**Yardstick One: Coherence**

Formula: `1 - switch count / (window size - 1)`

If the Agent keeps operating in the same "gear" (processing mode) — as opposed to constantly shifting gears like a driver who can't decide — that indicates it knows what it's doing. If it keeps jumping between different gears, it might be lost.

Imagine someone cooking. They pick up the spatula, put it down, pick up the knife, put it down, pick up the spatula again — they probably don't know what they're doing. But if they hold the spatula steadily and stir-fry the whole dish, they clearly know their goal.

**Yardstick Two: Efficiency**

Formula: `successes / attempts`

How many actions did the Agent propose? How many succeeded? If the Agent made 10 tool calls and 8 succeeded, efficiency is 0.8.

This is the most intuitive yardstick. Just like a test score.

**Yardstick Three: Convergence**

Formula: `longest consecutive successes / window size`

Is the Agent getting better over time? If it recently succeeded 8 times in a row (with a window size of 10), convergence is 0.8. This means the Agent has found the right direction and is making steady progress.

Think of a student doing practice problems — if they got 8 out of the last 10 right and those 8 were consecutive, that says more about mastery than getting 8 right scattered across the 10.

**Yardstick Four: Stability**

Formula: `1 - min(1, variance / 0.25)`

Is the Agent's confidence score stable? If the confidence is roughly the same each time it makes a decision (low variance), stability is high. If confidence swings wildly — 0.9 this time, 0.3 next time, then 0.8 — the system may not be very stable.

Imagine asking someone "Are you sure?" If they consistently say "I'm about 80% sure," they're stable. If they say "90%!" one moment and "20%..." the next, you'd worry they're just guessing.

---

## The Sliding Window

All four yardsticks are calculated within a "sliding window" of 10 events.

Why 10? Because a window that's too small would overreact to random fluctuations (one failure triggers panic), while a window that's too large would be too sluggish (the Agent is already in trouble but the monitor hasn't noticed). Ten is a balance point.

Moreover, until at least 5 events have been collected, the monitor won't emit any quality scores. This is called the "warm-up period" — like warming up an engine before driving, to avoid making bad judgments on insufficient data.

The four dimensions are each weighted at 0.25 (equal weight), and their sum produces a composite quality score Q between 0 and 1.

Why equal weight? Because there is currently no data to support any one dimension being more important than the others. PASCAL (the decision theory expert) said: "In the absence of evidence, the maximum entropy principle tells us: give each possibility equal weight." Start running, collect data, then adjust later.

---

## Six Ears

The monitor needs to "listen" to events on EventBus to calculate quality. HERACLITUS (the runtime dynamics expert) and TURING planned a two-phase listening strategy:

Phase 1 listens to only 6 event types — just enough to calculate the four dimensions. Like having six ears, each responsible for listening to a different sound.

Phase 2 adds 5 more event types for calculating finer-grained quality metrics.

Why two phases? Because more events means more resource consumption. Start with the fewest ears needed to be "good enough," then see if more are needed.

What if a certain event happens not to exist? The monitor won't crash. It uses safe defaults — for example, efficiency defaults to 1.0 (assuming everything is fine), and stability defaults to 0.5 (neither good nor bad).

HERACLITUS's principle: "Absence is information, not error."

---
