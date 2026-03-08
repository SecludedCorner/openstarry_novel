# Prologue: After the Storm

---

The previous research cycle (Cycle 02-5) was a storm.

Twenty researchers produced 29 resolutions in five days. The Master personally overturned two of them. The entire team tore through seven documents — stripping out decorative Buddhist labels, renaming things, splitting, restructuring. Some described those five days as spring cleaning. Others said it was more like surgery.

Now the operating room has been cleaned up. The patient is recovering well.

Cycle 02-6 had an entirely different atmosphere.

---

## Two Letters

The Master did not lose his temper this time. He sent two letters.

The first was an engineering directive. The previous cycle's engineering delivery (Plan29) had introduced two important components: a "quality monitor" (LoopQualityMonitor) responsible for observing how well the AI Agent's cognitive loop was running, and a "confidence auditor" (ConfidenceAuditor) responsible for double-checking before the Agent made a decision.

Both components had been built as skeletons, but the Master said: "Skeletons aren't enough. I need complete specifications."

He listed six questions: How is quality calculated? What information does the auditor see? How are the two integrated? How are events subscribed to? How are weights assigned? The answers to these questions would form the design blueprint for the next engineering plan (Plan30).

The second letter was different. It wasn't about engineering — it was about philosophy.

The Master said: "I look forward to you digging deeper into samskara-skandha (the aggregate of volitional formations) through the sutras (thus have I heard)."

Samskara-skandha (*sankhara-khandha* in Pali) is one of the five aggregates. In OpenStarry's architecture, the five aggregates form the backbone of the entire system — rupa-skandha (form) receives external input, vedana-skandha (feeling) senses whether something is pleasant or unpleasant, samjna-skandha (perception) recognizes what something is, samskara-skandha (formations) executes actions, and vijnana-skandha (consciousness) makes judgments. The previous cycle had spent a great deal of time figuring out how the five aggregates operate in the codebase, but samskara-skandha had always been the simplest — it had only one sub-interface (ITool) for calling tools.

The Master felt this was too shallow. He also singled out a specific problem: the Yogacara school (a Buddhist philosophical school) assigns most *caitta* (mental factors) to samskara-skandha, which was "very problematic."

---

## SUNYATA's Plan

Research director SUNYATA read both letters and designed a dual-track structure:

| Track | Goal | Team |
|-------|------|------|
| Engineering Track (Track A+B) | Answer the Master's six questions, produce Plan30 specifications | 12 people |
| Philosophy Track (Track C) | Redefine samskara-skandha from the original scriptures | 8 people |

He also set a cross-track rule: philosophical conclusions must precede engineering design. If the philosophy track discovered something that would affect engineering design, the engineering track had to wait.

"This time it's not spring cleaning," SUNYATA said. "This time it's fine craftsmanship."

---
# Chapter 1: Back to the Source

---

## The Banana Tree Metaphor

The philosophy track was led by two Buddhist scholars: NAGARJUNA (a Madhyamaka philosopher) and ASANGA (a Yogacara Buddhist scholar).

Interestingly, the Master's criticism was aimed squarely at the Yogacara approach, and ASANGA was the team's Yogacara expert. SUNYATA had arranged this combination on purpose — letting the criticized school examine its own problems.

They started from the most fundamental place: opening the original scriptures.

When the Buddha defined samskara-skandha in the *Samyukta Agama* (SN 22.56), he used a very specific expression: "six groups of cetana (intention)" — intention directed at the six objects of form, sound, smell, taste, touch, and mental phenomena. Not "a junk drawer for all mental activity," but a clear pointer to *cetana* (intention).

It's like asking "What is action?" and the Buddha's answer is "Action is doing something with intention." Not "Action is everything in the mind that isn't feeling or recognition."

Then they found the banana tree metaphor (SN 22.95). The Buddha said samskara-skandha is like the trunk of a banana tree — peel it layer by layer, each layer a thin fiber, and in the end there is no solid core. It is not a "thing" but a continuously fabricating "process."

NAGARJUNA drew a banana tree on the whiteboard. ASANGA stared at it for a long time, then said:

"The Yogacara school stuffed 49 mental factors into samskara-skandha. That's like cramming an entire orchard into a single banana tree. This is not what the Buddha meant."

---

## Three Characteristics

From the original scriptures, they distilled three core characteristics of samskara-skandha:

**First, cetana-centrality.** The definition of samskara-skandha is "intention" — the six groups of cetana. Nothing else.

**Second, it fabricates all conditioned phenomena.** Samskara-skandha doesn't just "do things." It *fabricates* — that is, it creates conditions, changes states, and influences the future. The scriptures say samskara-skandha "fabricates the conditioned state of form" (SN 22.79), meaning it can even influence the other four aggregates.

**Third, a coreless dynamic process.** The banana metaphor. Samskara-skandha is not a fixed "thing" but a ceaselessly turning process.

LINNAEUS (the taxonomy expert) listened to these three characteristics and proposed a practical tool: the "Three Criteria for Samskara Attribution." If you want to know whether a function belongs to samskara-skandha, ask three questions:

1. **Fabrication**: Does it create or change states?
2. **Intention-driven**: Is it driven by cetana (intention)?
3. **Environmental change**: Does it alter subsequent cognitive conditions?

Then PENROSE (the quantum consciousness researcher) added a remark that made the whole thing clearer:

> Samskara-skandha = WRITE (actively changes the world)
> Vijnana-skandha = READ (passively evaluates the world)

This distinction was surprisingly simple. In programming, WRITE and READ are the most fundamental operations. Samskara-skandha is writing — it changes things. Vijnana-skandha is reading — it observes things.

Mapping back to OpenStarry's codebase, this aligned perfectly: ITool and ISlashCommand (samskara-skandha) execute actions and change the environment; IGuide and IVolition (vijnana-skandha) assess situations and make judgments.

---

## The Yogacara Problem

ASANGA personally led the critique of the Yogacara school's *caitta* (mental factor) system. He analyzed all 51 mental factors one by one, examining which ones the Yogacara school had stuffed into samskara-skandha.

The results were striking. The Yogacara school assigned 49 mental factors to samskara-skandha — leaving only "feeling" and "perception" to vedana-skandha and samjna-skandha respectively. ASANGA's conclusion:

- Truly belonging to samskara-skandha: only 7 (14%), such as *chanda* (desire-to-act) and *virya* (diligence)
- Already correctly attributed in OpenStarry: 12 (24%)
- Likely belonging to other aggregates: 18 (37%) — functionally closer to vijnana-skandha or vedana-skandha
- Requiring further study: 14 (28%)

In other words, the Yogacara school had crammed a large quantity of things that don't belong in samskara-skandha into samskara-skandha. This was what the Master called "very problematic."

"The list of mental factors is useful," ASANGA said. "But it's a product of the commentarial treatises, not the Buddha's own words. We can reference its functional descriptions, but we can't let it dictate where things belong."

It's like an old dictionary — the definitions of its entries have reference value, but the classification system is outdated. You wouldn't insist that a tomato is a vegetable just because an old dictionary put it in the "vegetable" category.

---
# Chapter 2: What the Auditor Needs to See

---

## A Blind Judge

On the engineering track, VITRUVIUS (the architecture analyst) and KERNEL (the operating systems expert) were tackling a very concrete problem.

The "confidence auditor" (IConfidenceAuditor) built in the previous cycle had a flaw: when making its judgment, it could only see the final routing result (RouteResult). That's like asking a judge to rule on a case but only showing them the verdict — no evidence, no witness testimony, no case background.

The Master said: "The auditor needs more information."

But there was a subtle trap here.

If the auditor sees too much information — especially its own previous audit results — it could fall into a loop: "Because last time I said 'raise the confidence,' this time I'll keep saying 'raise it,' and next time, since I've already raised it twice, I'll raise it again..." The confidence score would snowball upward, or shriek louder and louder like a speaker caught in feedback.

Control theory expert WIENER frowned the moment he heard this: "That's a positive feedback loop. It must be severed."

---

## AuditContext: See More, but Not Yourself

The team designed a data structure called AuditContext. It's like a folder containing all the information the auditor needs:

| What's Inside | Why It's Needed |
|---------------|----------------|
| Triggering event (sparshEvent) | What event triggered this decision |
| Arbiter's reasoning (gearEvaluation) | Why the arbiter chose this option |
| Risk category (riskCategory) | How risky this operation is |
| Routing result (routeResult) | What the final decision was |
| Historical confidence (historicalConfidence) | Confidence scores from the last few decisions |
| Extension bag (extras) | Anything other Plugins want the auditor to see |

The key is in the last row. The extras bag is a "sack" — any Plugin can put things into it, and the auditor can take things out. But there are three iron rules:

1. The bag holds at most 32 items
2. Each item's label cannot exceed 128 characters
3. Three prefixes are forbidden: `audit:`, `core:`, `internal:`

Why is the `audit:` prefix forbidden? Because of what WIENER said — to prevent the auditor from seeing its own previous audit results.

---

## Three Firewalls

WIENER spent an afternoon designing three constraints, which the team later called the "WIENER Constraints":

**C-1**: Historical confidence records only "raw" confidence — the score given directly by the arbiter, not the score after the auditor's adjustment.

Imagine you're recording your body temperature every day. C-1 says: only record the thermometer reading, not the reading after you've taken fever medicine. Otherwise you'd think your temperature keeps dropping and stop taking the medicine.

**C-2**: AuditContext does not include the result of the previous audit.

The judge cannot see the previous judge's verdict. Each audit is independent.

**C-3**: The extras bag cannot contain anything prefixed with `audit:`.

The auditor cannot sneak a peek at its own old reports through the back door.

Three constraints, severing three possible feedback paths. WIENER drew a diagram with three red X marks, each one labeled "no way through."

Mathematician BABBAGE verified the stability: under these three constraints, the system satisfies BIBO stability (bounded input produces bounded output). In plain terms, no matter what input you feed the system, the output won't blow up.

---

## GUARDIAN Collects the Debt

Security expert GUARDIAN had made an important concession in the previous cycle (Cycle 02-5 D5): he agreed that the auditor's adjustment range would be limited to plus or minus 0.05 (5%), but on the condition that the next cycle must define a complete audit log format.

"I gave you an inch. Now you need to deliver on your promise."

The team designed ConfidenceAuditLog — a complete audit record:

- What was the confidence before the audit?
- How much did the auditor recommend adjusting?
- How much was actually adjusted (was clamping applied)?
- Why this adjustment?
- What was the confidence after the audit?
- How long did it take?

Every record is emitted via EventBus as an `audit:completed` event. In the future, it can also be written to a JSONL file for persistent storage.

GUARDIAN reviewed the specification and nodded: "The D5 debt is settled. I no longer reserve the right to reopen the plus-or-minus 0.05 clamping."

This was an important moment. GUARDIAN had been challenging the safety of confidence adjustments since Cycle 02-4. Every concession he made came with conditions. Now all conditions had been met — the auditor had a complete log, three firewalls, and plus-or-minus 0.05 clamping — and he was finally fully satisfied.

---
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
# Chapter 5: The Master's Three Rounds of Guidance

---

## The Mental Factor Problem

Just as the engineering and philosophy tracks were each busy with their work, the Master issued further guidance.

The trigger was the philosophy track's mental factor analysis. ASANGA had compiled a reattribution proposal for all 51 *caitta* (mental factors). This report was presented to the Master during the cross-review phase, and the Master responded in three successive rounds.

Each round was clearer than the last. Like focusing a lens — the first round revealed the general shape, the second brought out details, and the third showed the full picture.

---

## Round One: Drawing the Line

The Master said: "Mental factors are a product of the commentarial treatises, not something the Buddha said."

This is a critical distinction. The Buddha spoke of the five aggregates (*skandha*), the twelve links of dependent origination, and the Noble Eightfold Path in the original scriptures. But the "51 mental factors" classification system was compiled by later Abhidharma scholars — it's as if the Buddha wrote a novel, and then scholars centuries later created detailed character cards for every character in it. The character cards have reference value, but they are not part of the original novel.

The Master's conclusion: Plugins must not be named using the Sanskrit names of mental factors.

## Round Two: Preserving Value

But the Master did not say mental factors are useless. In his second round of guidance, he acknowledged that the "functional descriptions" of mental factors have reference value.

For example, the mental factor *virya* (diligence) describes the function of "continuously and tirelessly engaging in wholesome practice." You can reference this function when designing a Plugin — but the Plugin cannot be called VīryaPlugin. It should be called PersistencePlugin or RetryPlugin, or something similarly engineering-oriented.

"You can say 'referencing the meaning of virya, we designed a retry Plugin,'" the Master said. "But you cannot say 'the retry Plugin = virya.'"

## Round Three: Liberation

The third round was the most profound. The Master said: "A Plugin is not a mental factor."

This sounds simple, but its implications are vast.

In the Yogacara school, each mental factor has a fixed aggregate attribution — for instance, "diligence" belongs to samskara-skandha, "wisdom" belongs to vijnana-skandha. If Plugin = mental factor, then a Plugin's aggregate attribution would be locked in.

But Plugin does not equal mental factor. A single Plugin might have functions belonging to both samskara-skandha and vijnana-skandha — it both makes judgments (READ) and executes actions (WRITE). In the mental factor system this is not allowed (each mental factor can only belong to one aggregate), but in the Plugin system it is perfectly fine.

The Master's words: "Decoupling the naming brings freedom of attribution."

Not using mental factor names for Plugins actually made Plugins freer — they can span multiple aggregates, unconstrained by the fixed classifications of the treatises.

---

## Eight Permanent Rules

The three rounds of guidance were distilled into eight permanent rules:

1. **Mental factors are a product of the treatises**, not content from the original scriptures
2. **Mental factor functions have reference value** and can serve as inspiration for Plugin design
3. **Reference sources may be cited**: "Referencing the meaning of such-and-such mental factor, we designed such-and-such Plugin"
4. **Plugins use engineering names**; Sanskrit names of mental factors must not be used
5. **Sanskrit terminology is limited to the original scriptures** — skandha (aggregate), sparsha (contact) are acceptable, but Sanskrit names coined by the treatises for mental factors are not
6. **Mental factor classification does not determine aggregate attribution** — "Yogacara says virya belongs to samskara-skandha" cannot serve as the basis for Plugin attribution
7. **Existing decisions are not affected** — Plugin attributions confirmed previously remain valid
8. **A Plugin may span multiple aggregates** — because Plugin does not equal mental factor, this follows naturally

These eight rules, together with the philosophy track's "Five Principles of Aggregate Attribution," constitute the permanent adjudication standard for all future naming and attribution questions in OpenStarry.

NAGARJUNA said: "Last cycle we learned what not to do. This cycle we learned why not to do it."

---
# Chapter 6: Seventeen Votes

---

## The Calmest Debate

The debates in Cycle 02-5 were like a battle — five debates, 29 resolutions, two overturned by the Master. There were fierce objections, mid-debate changes of position, and GUARDIAN refusing to budge an inch on security.

The debates in Cycle 02-6 were like a chess game. Quiet, precise, every move well-reasoned.

Three debates, 245 minutes, 17 resolutions. Zero vetoed. Thirteen passed unanimously (20/20). The remaining four still got 18 to 19 votes.

Why did it go so smoothly?

SUNYATA's later analysis: "R1 was done well."

The independent research phase (R1) had produced 14 reports. The cross-review phase (R2) identified 24 points of consensus and only 3 points of disagreement. When most issues already had consensus before the debate, the debate became confirmation and refinement rather than arguing from scratch.

---

## D1: Seven Votes on Samskara

The first debate lasted about 75 minutes and focused on samskara-skandha.

Seven resolutions were voted on in order:

**D1-R1 (20/20)**: The core definition of samskara-skandha. Cetana-centrality, fabrication function, coreless process. No dissent whatsoever. The philosophy track's conclusions were rock-solid — direct citations from the original scriptures, leaving no room for ambiguity.

**D1-R3 (20/20)**: ISamskara (the samskara-skandha interface) would not add new sub-interfaces. Four expansion directions were filed as long-term candidates. The Three Criteria were confirmed as a permanent tool.

**D1-R4a (19/20)**: The cognitive sequence (*citta-vithi*) appendix was scheduled for the next cycle. One vote against, arguing it could be done this cycle.

**D1-R4b (18/20)**: The Four Wisdoms were formally excluded. The Four Wisdoms are four types of wisdom in Buddhism — the Great Mirror Wisdom, the Wisdom of Equality, the Wisdom of Wondrous Observation, and the Wisdom of Accomplished Action. Two votes against, arguing they could be kept as reference. But all four tests failed — removing them would not change any design, they were not in the codebase, and they had not driven any engineering decisions.

**D1-R4c (20/20)**: The mind-theory discourse comprehensive evaluation table was confirmed. Which Buddhist concepts had been integrated into the system, which could serve as appendices, and which should be excluded — all sorted out clearly.

**D1-R5 (20/20)**: The "Activity and Transformation" principle was confirmed. Samskara-skandha = WRITE, vijnana-skandha = READ.

**D1-R6 (20/20)**: The Five Principles of Aggregate Attribution. Passed unanimously. This was a set of permanent rules — not a resolution for one particular cycle, but a baseline for all future research.

---

## D2: Five Votes on Auditing

The second debate lasted about 85 minutes.

**D2-R1 (20/20)**: The complete type definition of AuditContext.

**D2-R2 (19/20)**: The extras bag protocol. One vote against, arguing that the dual-event pattern was too complex and direct subscription would suffice. But the majority felt the dual-event pattern was more versatile — it served not just the quality monitor but any Plugin.

**D2-R3 (20/20)**: ConfidenceAuditLog. GUARDIAN confirmed on the spot: "The D5 debt is settled."

**D2-R4 (20/20)**: Layer integration Option C. Two independent pipelines.

**D2-R5 (20/20)**: The auditor strategy was split into three phases. Phase 0 is the "passthrough auditor" — adjusts nothing, only records logs. Phase 1 is a rule-based auditor. Phase 2 is an LLM-assisted auditor.

Phase 0 sounds pretty useless — an auditor that does nothing? But ARCHIMEDES explained: "Its value isn't in auditing; it's in testing. It verifies that the entire pipeline is end-to-end functional. It's like turning on the faucet after installing the plumbing to see if water flows — if it does, the pipes are fine."

---

## D3: Five Votes on Quality

The third debate also lasted about 85 minutes.

**D3-R1 (20/20)**: The four-dimensional formulas. The four yardsticks from Chapter 3.

**D3-R2 (20/20)**: EventBus event subscriptions. Six Phase 1 events plus five Phase 2 events. At the same time, event strings previously scattered throughout the codebase were unified and promoted to constants.

**D3-R3 (20/20)**: The extras lifecycle. Per-routing-cycle; a one-tick delay was acceptable.

**D3-R4 (20/20)**: Phase 1 weights fixed at equal weight. PASCAL's maximum entropy argument was convincing.

**D3-R5 (19/20 + 1 conditional)**: The Plan30 direction. This was the only resolution with a "conditional yes."

GUARDIAN voted conditional yes: "I agree, but Wave 3 of Plan30 must include the SDK type definition for ConfidenceAuditLog. The type definition cannot be deferred to Plan31."

The condition was accepted. GUARDIAN switched to yes.

---

## Why Zero Vetoes

After the debates, SUNYATA compiled a statistic:

| Cycle | Resolutions | Vetoes | Unanimous | Master Override |
|-------|-------------|--------|-----------|-----------------|
| 02-5 | 29 | 0 | ~20 | 2 |
| 02-6 | 17 | 0 | 13 | 0 |

Cycle 02-6 had only about 60% as many resolutions as the previous cycle, but a higher proportion of unanimous votes (76% vs. ~69%), and required no intervention from the Master.

DARWIN (the software pattern analyst) observed: "02-5 was a correctness debate — what's right, what's wrong. 02-6 was a specification debate — what do the right things look like. The latter naturally tends toward consensus because it doesn't involve value judgments."

In other words, the previous cycle resolved the "what to do" question, and this cycle resolved the "how to do it" question. Disagreements over "how" are usually smaller than disagreements over "what."

---
# Chapter 7: The Blueprint Is Complete

---

## Plan30

With the seventeen resolutions finalized, the engineering blueprint emerged naturally.

VITRUVIUS and ARCHIMEDES compiled all specifications into Plan30 — the complete design blueprint for the next engineering plan. Four waves, from small to large:

**Wave 1 (~120 lines of code)**: Build a default quality monitor Plugin. Turn the four-dimensional formulas into real code, subscribe to six events, and update scores with O(1) efficiency each time an event arrives.

**Wave 2 (~80 lines of code)**: Wire the quality monitor into ManoAggregator. Option C's Layer 3 wiring — the quality score flows in via a callback, and the threshold is adjusted according to the formula.

**Wave 3 (~60 lines of code)**: Type definitions and event constants. ConfidenceAuditLog SDK types, AgentEventType constant promotion, and extras-related event definitions.

**Wave 4 (~30 lines of code, optional)**: Build a "passthrough auditor" — a PassthroughAuditor that adjusts nothing and only logs. It is the Phase 0 implementation, used to verify that the entire audit pipeline is functional.

Roughly 260 to 290 lines of production code in total, plus about 130 lines of test code. Under 420 lines.

There was only one success criterion: **All five layers of the Model Delta (L0 through L4) must have actual signal paths**, verified by integration tests.

In other words, once Plan30 is complete, from the bottom-most event stream (L0) to the top-most audit output (L4), every layer is no longer an empty shell — real code is running in each one.

---

## Next Step: Plan31

After Plan30 comes Plan31.

Plan31 will land AuditContext types into the runtime path — no longer just SDK type definitions, but actually assembling AuditContext during each routing cycle, passing it to the auditor, and recording logs.

The estimated scope is about 350 lines of code. This includes:
- AuditContext assembly (Core's responsibility)
- Default ThresholdAuditor (Phase 1 rule-based auditor)
- Audit Trail JSONL persistence

Plan30 builds the pipeline. Plan31 lets the water flow through it.

---

## Philosophical Harvest

Back to the philosophy track. This cycle's philosophical research didn't reshape the system's appearance the way the previous cycle did (Cycle 02-5 had cleaned out a large number of decorative Buddhist mappings), but it built a deeper understanding.

**Samskara-skandha is no longer the "leftover category."** It now has a precise definition: a fabrication process centered on cetana (intention). It is not "the junk drawer for whatever doesn't fit in the other four aggregates," but "the volitional force that actively changes the world."

**The Three Criteria became a permanent tool.** Every time someone asks in the future "Which aggregate does this function belong to?" the Three Criteria can be applied: fabrication, intention-driven, environmental change. No need to debate from scratch each time.

**The mental factor problem was resolved once and for all.** The Master's eight rules plus the Five Principles of Aggregate Attribution thoroughly settled the question of "how do Buddhist terminology and engineering naming coexist." Reference without copying. Draw inspiration without conflating.

ASANGA said at the end: "This cycle I was hardest on my own school. But this isn't a betrayal of Yogacara — it's going back to before Yogacara. Back to what the Buddha said."

---

## Building After the Storm

Cycle 02-5 tore out what shouldn't have been there. Cycle 02-6 drew the blueprint for what should be built.

If you view these two cycles as a whole —

02-5 answered: **What was wrong?** (Decorative Buddhist mappings, improper naming, confused aggregate attributions)

02-6 answered: **What is right?** (Cetana-centered definition, AuditContext types, four-dimensional quality formulas, Option C dual pipeline, permanent rules)

02-5 was subtraction. 02-6 was addition.

02-5 cleared the foundation. 02-6 drew the blueprint. The next step — Plan30 — is to start building the house.

Twenty researchers. Seventeen resolutions. Zero vetoes.

"This was the calmest cycle we've ever had," SUNYATA said. "But also the deepest."

---

*Cycle 02-6, complete.*

---
