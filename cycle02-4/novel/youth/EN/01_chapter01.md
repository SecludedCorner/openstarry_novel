# Chapter One: A Car Without an Engine Can Still Drive

---

## Who Does the Gear Arbiter Belong To?

The first debate (D1) posed a very specific question: which of the five skandha does the new interface IGearArbiter belong to?

The five skandha (aggregates) are this system's five major modules -- rupa (form/sensation), vedana (feeling), samjna (perception), samskara (volition/formation), and vijnana (consciousness). Every interface must belong to one skandha. So which one gets the new gear arbiter?

Three proposals were on the table.

Proposal A: it belongs to samjna (the skandha responsible for perception). Proposal C: it belongs to vijnana (the skandha responsible for consciousness). Proposal B: don't lock it down -- let the implementer decide.

BABBAGE used his favorite tool -- type algebra -- to turn this question into a math problem.

"Suppose IGearArbiter inherits interfaces from both samjna and vijnana. Samjna's tag is 'samjna'; vijnana's tag is 'vijnana'. In TypeScript, a single value cannot be two different strings at the same time. 'samjna' AND 'vijnana' = never. Empty set. Does not exist."

It's like you can't be both an apple and an orange at the same time. The type system won't allow it.

BABBAGE's proof took just three lines. But those three lines made nineteen people nod simultaneously -- because math doesn't need you to believe. It needs you to check. Anyone could verify those three lines themselves. The conclusion depends not on trust, but on logic.

So both Proposal A and Proposal C had problems -- they locked in the affiliation. Proposal B leaves affiliation open, letting implementers choose based on their own logic. A rule-matching implementation could declare itself samjna; a statistical-inference implementation could declare itself vijnana.

20/20. Unanimous. The first perfect-score resolution of Cycle 02-4.

NAGARJUNA added the philosophical angle: "Proposal B aligns with the core of Madhyamaka philosophy. The nature of a dharma is not determined by its name, but by its function and conditions." In plain language: you aren't who you are because of your name -- you are who you are because of what you do.

---

## One Method Is Enough

GUARDIAN wanted two methods -- evaluate() (pure judgment) and resolve() (pure action). Security separation.

KERNEL shook his head. He's an operating systems expert -- he'd seen too many interfaces bloated in the name of "security separation."

"Not needed. EventBus's synchronous events already provide observation points. Every gear switch emits an event that any safety monitor can intercept. No need to add another door to the interface."

He added: "If every interface does this kind of separation, eventually every interface in the system has dual methods. That's not security; that's ritual."

The final design: a single evaluate() method, plus three synchronous events -- `gear:switch` (when gears switch), `action:proposed` (after an action plan is generated), `action:executed` (after an action completes). Three events forming a complete security chain: prevention, review, audit.

GUARDIAN's proposal was rejected, but his core concern -- "I need to be able to observe what's happening" -- was preserved in a different form. Three events = three windows. Through these three windows, GUARDIAN can see everything. He doesn't need his own door.

This pattern recurred throughout later debates: GUARDIAN proposes a security measure, it gets rejected, then his core concern reappears in modified form. Not a loser's stubbornness -- a security engineer's professional discipline. A good security designer isn't someone who blocks everything. It's someone who ensures "even if I'm overruled, the risk I worried about is still covered."

---

## Pull Out All the Plugins

D1's most important resolution: ManoAggregator becomes a pure router.

The old ManoAggregator was like a traffic controller -- gathering signals from all directions, making comprehensive judgments. Now it's a traffic light: if an IGearArbiter exists and its confidence is high enough, green light (take Gear 1, the fast path); otherwise, red light (take Gear 2, let the LLM think carefully).

This change looks small -- from "intelligent judgment" to "simple judgment." But it means the kernel no longer contains any "capabilities." The kernel only forwards. All capabilities live in plugins.

Five levels of degradation behavior:

| State | What happened | What the system does |
|-------|--------------|---------------------|
| G-0 | No plugins installed | Pure LLM mode |
| G-1 | Plugin is broken | Same as above, log error |
| G-2 | Plugin isn't very sure | Use LLM |
| G-3 | Plugin threw an error | Use LLM, log anomaly |
| G-4 | Plugin is too slow | Use LLM, timeout switch |

G-0 is the most important one -- an Agent with zero plugins installed is simply a pure LLM Agent. It still works. Like a car without a navigation system -- you can still drive; you just have to read road signs at every intersection. Nobody would call a car without navigation a "broken car." It's just a more basic car.

NAGARJUNA offered a precise statement from the Buddhist perspective: "G-0 is not degradation. G-0 is the primordial state. An Agent without vasana is not deficient -- it is newborn."

The ultimate test of zero built-in capabilities: pull out all plugins, and the system still lives. 20/20.

The Gear 1 fast path still requires a minimal set of events -- `gear:switch` and `action:proposed`. Without these two events, the fast path is a highway with no traffic lights. Too dangerous. GUARDIAN pointed this out immediately. KERNEL agreed.

One more detail: the evaluate() method has a strict "purity contract" -- no side effects, no mutating inputs, no I/O. In plain language: evaluate() can only look, not touch. It can tell you "I think we should take the fast path," but it can't act on its own.

TURING searched the existing codebase -- good news: the existing VasanaEngine.evaluate() already satisfies this constraint. Theory and practice are consistent.

> *SCRIBE's narration: D1 took ninety minutes. Nine resolutions. The most important thing wasn't any single resolution -- it was a shift in mindset. The engine was extracted. The kernel became lighter, simpler, cleaner. Like tidying a room -- the things that truly matter become easier to find.*

---
