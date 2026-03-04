# Chapter Three: Fictitious Code

---

## Three Seconds of Silence

The fourth debate (D4) didn't open with a proposal. It opened with a correction.

TURING -- the source code analysis expert -- stood up. He normally doesn't say much. But when he speaks, everyone listens. Because every sentence he utters is backed by `grep` search results.

"Report R07 references a method called `ISensation.ingestToolResult()`. I searched the entire codebase. This method does not exist."

Three fabrications -- ISensation, feedbackQueue, SparshEvent.timestamp. All written in the same report. All cited as fact. Like a paper citing three books that don't exist.

HERACLITUS didn't argue. A global search is irrefutable. You claim a method exists in the code; TURING searched; it's not there. Facts are facts.

HERACLITUS's response was impressive -- no excuses, no "but my analytical logic is still correct." He accepted the correction immediately.

Three seconds of silence. Those three seconds changed the entire tone of the debate.

Why? Because that report assumed samskara could update vedana in real time within "the same cycle." But in reality, samskara can only affect vedana in "the next cycle." This difference -- real-time versus next-cycle -- is enough in control theory to change whether the conclusion is that the system is stable or unstable.

The lesson was recorded: **All analyses citing code must be verified by TURING.**

PENROSE later wrote in the record: "TURING wasn't humiliating HERACLITUS. He was reminding everyone -- we too easily treat things we've imagined as real. When you've built a perfect model in your head, you forget to check whether reality matches your model."

---

## The Hand Cannot Directly Alter the Brain

If fictitious code can lead to wrong conclusions, then correct conclusions must be built on real code. D4 started from the correction, then rebuilt all analyses on the corrected foundation.

Four rules for samskara:

1. Samskara can only directly affect the user interface -- pressing buttons, sending messages, performing actions.
2. Effects on other skandha must occur indirectly through the EventBus.
3. It cannot directly modify the state of vijnana or samjna.
4. Mano-dvara sparsha (mind-door contact -- action results triggering new perception) is deferred to Phase 2.

A human analogy: the hand (samskara) can push things and grab things (affect the outside world). But the hand cannot reach directly into the brain to change your thoughts. If you want to change a thought, you have to do something first (like read a book), then let that action become new input in the next moment.

LEIBNIZ confirmed this boundary from a multi-agent perspective: "Samskara is the interface between the system and the outside world, not a side door within the system. If samskara could bypass the EventBus and directly modify vijnana, then safety monitoring becomes decoration -- because there'd be a path that bypasses all checkpoints."

The fourth rule -- mano-dvara sparsha -- is the most interesting. An Agent does something (samskara), and the result of that action becomes new perceptual input (sparsha), triggering a new processing cycle. This is causal circularity. Handled poorly, it leads to infinite recursion. Deferred to Phase 2.

---

## Three Layers of Stabilization

If an action produces good results, the system becomes more inclined to repeat that action. Repetition produces more good results. Good results reinforce the inclination. This is positive feedback -- like a microphone facing a speaker, the sound getting louder and louder until it screams.

How do you prevent it? Three-layer mechanism:

| Layer | What it does | What it's like |
|-------|-------------|---------------|
| Layer 1 (Sati) | Fine-tune each cycle | Co-pilot gently reminding |
| Layer 2 (Contemplation) | Cross-cycle trend monitoring | Traffic officer observing at an intersection |
| Layer 3 (Safety) | Hard constraints | Guardrails -- hitting them hurts, but you won't go off the cliff |

WIENER proved mathematically: as long as the combined force of the three layers exceeds the force of positive feedback, the system won't spiral out of control. Like a bridge -- as long as the support force exceeds the weight, the bridge won't collapse.

Specifically, w (the gain cap) cannot exceed 0.3. Why 0.3? WIENER derived it using the Kalman gain formula -- above 0.3, the system can oscillate in worst-case scenarios. Below 0.3, the three-layer mechanism guarantees stability.

There was also an important resolution: vedana's "zero-order hold."

Vedana takes a snapshot at the beginning of each cycle. All skandha use this snapshot throughout the cycle. Changes are written back all at once when the cycle ends.

Why? Four reasons. Control theory: eliminates intra-loop real-time feedback, more stable. Buddhism: the vedana -> samjna -> samskara causal chain isn't disrupted mid-process. Engineering: simplest implementation -- no race conditions to handle. Safety: SafetyMonitor is exempt from this constraint -- in true emergencies it can intervene at any time.

Using a photography analogy: vedana presses the shutter once at the start of each cycle. This photo doesn't change during the entire cycle. All skandha see the same photo -- no one sees a different picture because they looked at a different time. Only when the cycle ends does the photo get replaced.

20/20. Arguments from four disciplines all converged on the same design. This kind of cross-disciplinary consistency is rare.

---

## The Silkworm's Own Cocoon

ASANGA invoked an ancient image: "Like a silkworm spinning silk, binding itself in its own cocoon."

A silkworm spins silk to make a cocoon. Each strand is so fine you can barely see it. But strand after strand, they accumulate into a cocoon -- sealing itself inside. You don't notice the weight of any single strand, until one day you realize you can't move.

Samskara's repetitive patterns are like those strands of silk. An Agent that repeatedly uses the same strategy will find that strategy becoming its cocoon.

The mathematical model captures this property: early repetitions have large effects (the first strand changes the most), but as they accumulate, each new repetition changes less and less (the cocoon is already thick; one more strand is barely noticeable). Safety cap: repetitive patterns contribute at most 30% of the influence. Same as the earlier gain cap (w <= 0.3) -- 0.3 is a safety line. Cross it, and the system starts becoming unstable.

NAGARJUNA smiled: "Buddhism has known this for a long time. Vasana can influence you, but they cannot control you. 0.3 is the mathematical expression of a Buddhist intuition."

> *SCRIBE's narration: D4 had the highest mathematical density of all six debates. But the most profound moment wasn't any formula -- it was TURING's three seconds of silence. In those three seconds, the entire debate's foundation shifted from fictitious code to real code. Facts before theory.*

---
