# Chapter One: Vasana Are Acquired, Not Innate

---

## I. The Skandha Attribution Dispute

D1 was the starting point of Cycle 02-4 -- the skandha (aggregate) attribution of IGearArbiter. The Pre-DC had confirmed VasanaEngine's externalization into an IGearArbiter plugin. The question now was: which skandha does this interface belong to?

Three proposals. Proposal A -- pure samjna (perception) skandha (IGearArbiter extends ISamjna). Proposal B -- cross-skandha dual-layer (the interface itself inherits no skandha root interface; implementors choose attribution according to their own logic). Proposal C -- pure vijnana (consciousness) skandha (extends IVijnana).

BABBAGE's type algebra analysis decided the outcome.

The problem with Proposal A: if IGearArbiter extends ISamjna, its skandha attribution is `'samjna'`. If it also extends IVijnana, the type system derives `'samjna' & 'vijnana' = never` -- the empty type. TypeScript does not allow a value to simultaneously be two literal types. Cross-skandha attribution is impossible at the type level.

The problem with Proposal C: pure vijnana skandha cannot explain the "pattern recognition" function in evaluate() -- recognition is samjna's responsibility. Assigning recognition to vijnana violates the functional boundaries of the five skandhas.

The advantage of Proposal B: it does not lock down skandha attribution. The interface itself only defines the behavioral contract; it inherits no skandha root interface. Implementors choose attribution according to their own logic -- a rule-matching implementation can be attributed to samjna, a statistical-inference implementation can be attributed to vijnana. This aligns with DC-6's ruling: "do not lock down sub-interface attribution within a skandha."

20/20. Unanimous. Type algebra transformed a philosophical dispute into a mathematical proof.

NAGARJUNA added philosophical confirmation after the vote: "Proposal B's 'not locking down skandha attribution' is consistent with the core of Madhyamaka. A dharma's essence is not determined by its name, but by its function and dependent conditions. IGearArbiter's skandha attribution depends on its implementation -- this is the correct expression of pratityasamutpada (dependent origination)."

DARWIN's software pattern observation: Proposal B is essentially the Strategy Pattern -- the interface defines the behavioral contract, implementors provide concrete strategies. Different strategies can belong to different skandhas. This is a pattern that has been validated for decades in software engineering.

---

## II. Single Method and Safety

GUARDIAN proposed a dual-method design with evaluate() and resolve() -- evaluate() for pure recognition, resolve() for pure action. Safety separation. This was the application of the Command-Query Separation principle in a cognitive architecture.

KERNEL vetoed this proposal. His argument came from the operating system perspective: "In Unix philosophy, monitoring and the monitored are separated. `strace` does not require cooperation from the traced process -- it observes system calls externally. Likewise, EventBus's synchronous event semantics already provides equivalent safety observation points. The responsibility of resolve() can be observed by external monitors through the `gear:switch` synchronous event -- no need to split at the interface level."

He added a sharper comment: "If we apply CQS to every interface, we will end up with a system where every interface has dual methods. That is not safety -- it is ritual."

SUNYATA consolidated the decision: evaluate() as a single method + EventBus synchronous events + threshold safety factor. GUARDIAN's core demand -- observability -- was preserved, merely implemented through a different mechanism. 20/20.

The isGearArbiter() type guard uses structural typing (duck typing) rather than nominal typing:

```typescript
function isGearArbiter(x: unknown): x is IGearArbiter {
  return typeof x === 'object' && x !== null
    && typeof (x as any).evaluate === 'function'
    && (x as any).evaluate.length <= 1;
}
```

No instanceof, no tag properties. Any object implementing the correct signature can pass the guard. This means third-party plugins need not import the IGearArbiter type to be recognized -- correct behavior is sufficient. 20/20.

The purity contract for evaluate() -- must not produce side effects, must not modify GearContext, must not initiate I/O. The importance of these three constraints is asymmetric. The ban on side effects ensures evaluate() can be safely retried. The read-only GearContext ensures the gear arbiter cannot tamper with its own input. The I/O ban ensures evaluate()'s latency is predictable.

TURING reported a code fact: v0.26.0-beta's VasanaEngine.evaluate() is indeed a pure function -- no write operations, no external calls, no state modifications. Existing code already conforms to this constraint. Consistency between theory and practice -- the constraint designed by the research team happens to be the pattern already followed by the engineering team. 19/20. ARCHIMEDES's one abstention stemmed from his concern about the "I/O ban" limiting Gear 1 when it needs to query external knowledge bases -- but this belongs to future extension considerations.

---

## III. ManoAggregator Pure Routing

D1's most important resolution: ManoAggregator pure routing + G-0 through G-4 degradation behavior table.

ManoAggregator does not perform intelligent aggregation. It does if/else:

```
if (hasGearArbiter && arbiter.evaluate(context).confidence > threshold) {
  return Gear.ONE;  // fast path
} else {
  return Gear.TWO;  // LLM deep deliberation
}
```

Same nature as EventBus -- pure mechanism, not capability. Master's exact words during the Pre-DC phase: "Same nature as EventBus." The weight of this statement lies in demoting ManoAggregator from "core intelligence component" to "infrastructure." Infrastructure does not make decisions -- it conveys decisions.

G-0 through G-4 are five degradation levels:

| Level | Condition | Behavior |
|-------|-----------|----------|
| G-0 | No IGearArbiter plugin | Pure Gear 2 (pure LLM) |
| G-1 | Plugin load failure | Same as G-0, log error |
| G-2 | evaluate() returns low confidence | Take Gear 2 |
| G-3 | evaluate() throws exception | Take Gear 2, log exception |
| G-4 | evaluate() times out | Take Gear 2, timer triggered |

Regardless of the system's state, the Agent can operate. G-0 is the most important -- an Agent without an installed IGearArbiter is a pure Gear 2 Agent. It is still a complete, operational Agent. The ultimate test of zero built-in capabilities: unplug all plugins, and the system still lives.

20/20.

The design philosophy of the degradation behavior table deserves elaboration. In traditional software design, exception handling addresses "error conditions" -- the system strives to recover to a normal state. In G-0 through G-4, degradation is not an error -- it is another normal state of the system. A G-0 Agent and a G-4 Agent are both "normally operating Agents," differing only in capability level. This resonates with the Buddhist view: the weakening of sati (mindfulness) is not a "malfunction" -- it is "conditions changing."

VITRUVIUS confirmed from an architectural perspective: the G-0 through G-4 degradation behavior table covers all possible system states. No state of "undefined behavior" exists -- this is the fundamental requirement of a safe system.

---

## IV. Gear 1 Minimum Event Set

Three events: `gear:switch`, `action:proposed`, `action:executed`. Every Gear 1 action must emit these three synchronous events -- non-skippable, non-asynchronous.

`gear:switch` fires at the instant of gear switching -- any safety monitor can set an interceptor on this event. If the monitor deems the switch unsafe, it can block the switch during event handling. `action:proposed` fires after the action plan is generated but before execution -- this is the final veto window. An external safety module can review the action plan and decide whether to approve it. `action:executed` fires after the action completes -- providing an audit trail, letting the system record the complete history of every Gear 1 action.

The three events form a complete safety chain: prevention (gear:switch) -> review (action:proposed) -> audit (action:executed).

This was the only safety mechanism GUARDIAN successfully pushed through in D1. Although the evaluate()/resolve() dual-method was vetoed, synchronous events ensured the completeness of external safety monitoring. GUARDIAN's core demand was preserved in a different form -- this pattern would recur in D5. In every debate, GUARDIAN would propose a solution, be vetoed, then reappear in modified form. Not the stubbornness of a loser, but the professional discipline of a security engineer.

---

## V. The Structural Significance of D1

D1's nine resolutions collectively accomplished a structural transformation:

**Before**: VasanaEngine was a core component with a rule base and matching logic. ManoAggregator was an intelligent aggregator, integrating results from multiple signal sources. Gear selection logic was hardcoded in the kernel.

**After**: IGearArbiter is an optional plugin, a pure function interface. ManoAggregator is a pure router with if/else logic. Gear selection logic is externalized. Without a plugin, the system degrades to pure Gear 2 -- still fully usable. Three synchronous events ensure a complete safety observation chain.

The philosophical significance of this transformation was precisely articulated by NAGARJUNA: "An Agent without vasana is not a defective Agent -- it is a newborn Agent. Vasana are the result of posterior cultivation, not innate structure. The G-0 state is not degradation -- it is the primordial state."

ARCHIMEDES quantified the transformation's impact from an engineering perspective: VasanaEngine's externalization is projected to remove approximately 200 lines of rule-matching logic from the kernel, replacing them with approximately 15 lines of IGearArbiter interface definition and approximately 30 lines of ManoAggregator pure routing logic. The kernel's cognitive complexity drops dramatically -- from "understanding how the rule base works" to "understanding how if/else works."

MESH, although he voted against fixing Level in D2, gave unanimous support to all D1 resolutions. He later explained: "D1's direction of turning core components into plugins is correct. My objection in D2 was about Level flexibility, not about the principle of externalization."

> *SCRIBE's narration: D1's nine resolutions were completed in ninety minutes. The most important thing was not any single resolution, but a structural transformation -- VasanaEngine went from core component to plugin, ManoAggregator went from intelligent aggregator to pure router. The zero built-in capability principle was engineered into reality. BABBAGE's type algebra was the decisive weapon in this debate -- he expanded the logical consequences of every proposal to the type system level, turning choices into necessities.*

---
