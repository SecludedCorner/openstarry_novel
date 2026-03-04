# Chapter One: Vasana Are Acquired

---

## I. The Shape of the Question

When SUNYATA wrote the topic of D1 on the whiteboard, a particular kind of silence descended upon the amphitheatre. Not the silence of D3 — the "everyone agrees" kind (that would come the day after tomorrow) — nor the silence of D5 — the "calm before the storm" kind (that would come on the fifth day). This was an "ah, so that's what it is" kind of silence.

The whiteboard read:

```
IGearArbiter — which skandha does it belong to?
```

Seven words. One question mark. But the weight of the question mark was not in the words themselves.

The Pre-DC had already confirmed: VasanaEngine would be externalized from the core into a plugin. Externalization itself was not the issue — the issue was what came after externalization. A plugin must belong to a skandha. The Plugin Manifest has a `skandha` field. What goes in that field?

ATHENA spoke first. Her voice carried the steadiness of an engineer who has been thinking about a problem for days:

"IGearArbiter does two things. First, fast recognition — take a request as input, match it against a rule base, determine whether a known pattern exists. This is the function of samjna (perception-aggregate): apprehending characteristics, identifying patterns. Second, confidence judgment — how reliable is this match? Is it worth bypassing the LLM? This is the function of vijnana (consciousness-aggregate): discriminating awareness, evaluative discernment."

She paused.

"It spans skandhas."

---

Three proposals were laid on the table. BABBAGE, with his precision unsettling to the point of elegance, arranged them into a table:

| Proposal | Interface Inheritance | Manifest Annotation | Type Safety |
|----------|----------------------|---------------------|-------------|
| (A) | extends ISamjna | `skandha: 'samjna'` | Strong — but loses vijnana semantics |
| (B) | Independent interface | `skandha: ['samjna', 'vijnana']` | Moderate — multi-value at Manifest layer |
| (C) | extends IVijnanaMechanism (new intermediate layer) | `skandha: 'vijnana'` | Strong — but increases type complexity |

BABBAGE pushed his glasses up. He did not need to — the frames fit — but the gesture was itself a form of punctuation, signaling "what I am about to say will be very precise."

"Proposal (A) has a type-algebraic problem."

He wrote a line on the whiteboard:

```
ISamjna.skandha = 'samjna'
IVijnana.skandha = 'vijnana'
'samjna' & 'vijnana' = never
```

"If IGearArbiter extends ISamjna, its skandha field is locked at the type level to 'samjna'. You cannot express at the interface layer that it simultaneously belongs to two skandhas. Discriminated union types do not allow such intersection."

DARWIN tilted his head. "In plain terms?"

"In plain terms: TypeScript's type system does not allow a thing to be simultaneously a cat and a dog. You can claim in the Manifest that it is a cat-dog, but the interface-layer compiler will reject it."

Proposal (A) was struck from everyone's mental shortlist within three seconds of BABBAGE finishing.

---

The problem with Proposal (C) was discovered by LINNAEUS.

"DC-6," he said, opening his taxonomy notebook. "Master's ruling: 'Do not lock down sub-interface attribution within a skandha.' IVijnanaMechanism as a sub-interface of IVijnana —"

"— locks it down." KERNEL picked up the thread. "Once you establish IVijnanaMechanism, every future cross-skandha component will need another intermediate layer. IVijnanaCognition. ISamjnaPerception. Type proliferation is exponential."

Proposal (C) was never formally voted down, but like a gear placed in the wrong position, everyone could see it did not fit.

---

The turning point for Proposal (B) came from ASANGA.

He had been silent throughout. After BABBAGE's type algebra and LINNAEUS's taxonomy, he spoke. His voice was like a stick of incense lit in darkness — quiet, but with unmistakable direction.

"The five universal mental factors arise simultaneously."

Everyone turned toward him.

"Both the *Mahavibhasa* and the *Cheng Weishi Lun* state: sparsha (contact), manasikara (attention), vedana (feeling-tone), samjna (perception), cetana (volition) — five mental factors — arise **simultaneously** in every cognitive event. Recognition does not precede judgment. Recognition and judgment co-arise in the very instant of sparsha."

He looked at ATHENA.

"You said IGearArbiter does two things — samjna's pattern-apprehension and vijnana's discriminative awareness. In Buddhist philosophy, these two are not sequential. They are **simultaneous**. Same basis, same object, same mode. A single `evaluate()` method — not because of engineering simplification, but because this is how the mind actually operates."

The amphitheatre was silent for five seconds.

PASCAL wrote something quickly in his notebook. NAGARJUNA gave a slight nod. The corner of BABBAGE's mouth lifted almost imperceptibly — formal argumentation and Buddhist scripture converging on the same conclusion was, for him, a rare form of beauty.

SUNYATA: "Proposal (B). Independent interface, multi-value Manifest. Are there objections?"

Twenty faces. Zero raised hands.

**D1-1A: Proposal (B) cross-skandha dual-layer strategy — 20/20.**

---

## II. The War and Peace of evaluate()

If D1-1A was a quiet river, then the ensuing debate over the evaluate() interface design was the rapids on that river.

GUARDIAN stood up. He rarely stood — through all six debates of Cycle 02-3, he had mostly remained seated, red pen underlining passages in his memorandum. But today he rose, and that meant what he was about to say was not a suggestion but a claim.

"A single evaluate() method is insufficient."

He walked to the whiteboard and drew a timeline:

```
   Request enters → evaluate() → gear switch → tool execution
                       ↑
                 All logic here
                 Recognition + judgment + decision
                 One function does everything

   If this function fails — the entire chain fails
   If this function is injected — the entire chain is hijacked
```

"I propose splitting it into two steps: `recognize()` and `resolve()`."

```
   Request enters → recognize() → [verification point] → resolve() → gear switch
                                          ↑
                                    SafetyMonitor can intervene
                                    Can audit the recognition result
                                    Then decide whether to proceed
```

"Insert a verification point between recognize and resolve. SafetyMonitor can inspect whether the recognition result is reasonable, then decide whether to permit resolve to execute."

ATHENA responded almost instantly: "Redundant."

GUARDIAN's eyes narrowed slightly. "Redundant?"

"An EventBus synchronous event achieves the exact same effect. At the moment evaluate() completes, emit a `gear:arbiter_evaluated` event. SafetyMonitor subscribes to this event. Synchronous handling."

"Synchronous? What if SafetyMonitor's handling is asynchronous? What if it needs to query an external service —"

KERNEL raised his hand. Not a hand raised to speak — a hand raised to signal "I have a technical fact."

"Node.js's EventEmitter.emit() is synchronous."

The entire theatre turned to KERNEL.

"When you call emitter.emit('event', data), all registered listeners execute **sequentially and synchronously** within the current call stack. Not nextTick, not microtask, not macrotask. Synchronous. By the time emit() returns, all listeners have already finished."

GUARDIAN: "You are certain?"

KERNEL gave him a look. The look meant: "I have written Node.js event systems."

"I am certain. In the Node.js model, an EventBus synchronous event and your proposed recognize/resolve separation are equivalent in terms of safety guarantees. The only difference is API complexity."

---

GUARDIAN did not yield immediately. A good security advocate does not yield because of a single technical fact — he searches for the edge that fact does not cover.

"Suppose the future runtime is not Node.js. Suppose someone implements an asynchronous EventBus using Worker Threads —"

KERNEL: "That is an implementation error, not a design flaw. Synchronous event semantics are a contract-level guarantee, independent of any specific runtime. If someone implements an asynchronous EventBus, they are violating the contract."

WIENER interjected from his seat: "I can offer a compromise."

Everyone looked at him. WIENER rarely offered "compromises" — he usually offered "mathematical proofs." But occasionally, even a control theorist must play diplomat.

"Three external safety mechanisms. First: EventBus synchronous event — `gear:arbiter_evaluated`, non-deferrable, non-skippable. Second: threshold safety factor — theta_adjusted = theta_base x (1 + k_safety), safety margin built into the mathematics. Third: minimum event set — gear:switch, action:proposed, action:executed — every gear operation has a complete event trail, and external monitoring can verify independently."

He looked at GUARDIAN.

"Your core demand is: no single function should do everything without external checks. Three mechanisms provide three independent external checkpoints. If all three fail, that is no longer a design problem — it is a Byzantine fault."

GUARDIAN was silent for thirty seconds. In security, thirty seconds of silence means the attack surface is being evaluated.

"The minimum event set," he said at last. "gear:switch needs gear:arbiter_evaluated added. I need to know the arbiter's judgment result, not only the final gear switch."

WIENER: "Agreed."

ATHENA: "Agreed."

**D1-R1: Single evaluate() method + EventBus synchronous events + threshold safety factor — 20/20.**

GUARDIAN nodded. His red pen drew a line across his memorandum — not an underline (that meant "problem") but a strikethrough (that meant "resolved").

---

## III. The Type Guard: evaluate.length <= 1

TURING spoke only twelve words during the third segment of D1, but those twelve words changed the type guard design.

The discussion centered on `isGearArbiter()` — how to determine at runtime whether a plugin implements the IGearArbiter interface. BABBAGE proposed two approaches:

Approach A: Symbol brand — attach a Symbol property to the interface, check at runtime. Strongest type safety, but inconsistent with the existing codebase style.

Approach B: Structural type guard — check whether an object possesses id, priority, and evaluate as three properties with correct types. Duck typing.

BABBAGE favored Approach A. Formally more rigorous.

TURING said those twelve words:

"`candidate.evaluate.length <= 1`. Add this line."

BABBAGE: "What do you mean?"

"`Function.length` returns the number of formal parameters of a function. evaluate(context) has one parameter, length is 1. evaluate() with no parameters, length is 0. evaluate(a, b) with two parameters, length is 2. If a plugin happens to have a method called evaluate but with a completely wrong signature — say evaluate(x, y, z) — the structural type guard would let it through, but the length <= 1 check would catch it."

BABBAGE froze for two seconds. Then he smiled. The kind of smile that says "why didn't I think of that."

"The number of edge cases drops from O(2^n) to —"

"O(1). One line of code. Nine test cases." TURING's tone was as flat as if he were reading a log file.

```typescript
export function isGearArbiter(obj: unknown): obj is IGearArbiter {
  if (typeof obj !== 'object' || obj === null) return false;
  const candidate = obj as Record<string, unknown>;
  return (
    typeof candidate.id === 'string' &&
    typeof candidate.priority === 'number' &&
    typeof candidate.evaluate === 'function' &&
    candidate.evaluate.length <= 1  // TURING enhancement
  );
}
```

**D1-R2: isGearArbiter() structural type guard (with evaluate.length <= 1 check) — 20/20.**

---

## IV. The Purity Contract: Observation Functions

The debate over D1-R4 was quieter than the preceding three items, but its philosophical depth was the greatest.

The question was: what can evaluate() do, and what must it not do?

NAGARJUNA opened the discussion with a question:

"Is recognition a fabrication?"

In Buddhist philosophy, "fabrication" (sankhara/samskara) refers to conditioned formations — actions that produce change in the world. "Recognition" (samjna) is the apprehension of characteristics — observation, cognition, but without altering the object observed.

"A person sees a red light. In the moment of seeing, his eyes do not change the red light. The red light remains red. But he now knows — the red light is a signal to stop. This 'knowing' is observation, not fabrication."

NAGARJUNA looked at ATHENA:

"evaluate() should be an observation function. It may read external state — context, history, klesha signals — but it should not modify any state. It only 'sees'; it does not 'do.'"

WIENER took over from the control theory perspective:

"In control theory, an observer is a pure function: its output depends only on the input and system state, and it does not in turn alter the system state. If the observer has side effects — for instance, if it modifies the observed value while observing — the system will produce unpredictable feedback."

"The engineering implication: evaluate() should be idempotent. Same input + same external state yields the same output. No side effects."

DARWIN added a biological analogy: "A sensory neuron does not modify the stimulus source. It only transmits the signal. A motor neuron is what modifies the environment. evaluate() is a sensory neuron."

KERNEL proposed a time constraint: "100ms per arbiter. 200ms for the entire chain. If an arbiter times out, skip it and proceed to the next. If the entire chain times out, fall back to Gear 2."

PASCAL abstained here — not in opposition, but because "for the numerical portion, I do not have sufficient engineering data to judge whether 100ms is appropriate."

**D1-R4: evaluate() purity contract — observation function + 100ms/200ms time budget — 19/20 (PASCAL abstained on the numerical portion).**

---

But the purity of evaluate() raised a question: if evaluate() cannot have side effects, then what about VasanaEngine's "learning" function — the capacity to absorb experience from successful Gear 1 decisions?

The full answer would not be revealed until D6, but D1 planted the foreshadowing:

"Side effects are performed through a separate method," ATHENA said. "evaluate() is responsible for observation. Learning — if any — is handled through a separate `imprint()` method, outside evaluate(), at an appropriate moment (such as after a round concludes), triggered externally."

NAGARJUNA nodded. "Samjna recognizes; samskara fabricates. Recognition and fabrication should not occur within the same function."

This separation — the purity contract of evaluate() and the future side-effect authorization of imprint() — became one of the most enduring design principles across all six debates.

---

## V. Pure Routing: G-0 through G-4

The final resolution of D1 was the most straightforward of the entire debate, yet also the most far-reaching.

SUNYATA drew a table on the whiteboard:

```
ManoAggregator Degradation Behavior Table
```

"The Pre-DC has confirmed: ManoAggregator is pure routing. if/else. The same nature as EventBus. But 'pure routing' exhibits different behaviors under different plugin configurations. We need to enumerate all possible states."

KERNEL walked to the whiteboard and picked up the pen. He drew five rows:

| Level | IGearArbiter | IProvider | Behavior |
|-------|-------------|-----------|----------|
| G-0 | None | None | Core alive but incapable of cognition |
| G-1 | None | Present | Always Gear 2 (pure LLM) |
| G-2 | Present | None | Gear 1 only (rules only) |
| G-3 | Present | Present | Full dual-gear |
| G-4 | Multiple arbiters + hot-swap | Present | Runtime dynamic load/unload |

NAGARJUNA looked at G-0 and G-1 and said something that would be quoted countless times:

"G-0 is a being without any skandha — the core exists but cannot perceive, cannot cognize, cannot act. If the five skandhas are the conditions for sentient existence, G-0 is — non-sentient."

He paused.

"G-1 is more interesting. A being with only samjna (Provider/LLM) and no vasana. This is —"

ASANGA picked up the thread: "— a newborn being. Without conditioning from past lives. Every act of cognition must begin from scratch. No intuition, no shortcuts, only full deliberation."

NAGARJUNA: "This is precisely why externalizing VasanaEngine is more correct than building it in. Vasana are acquired through conditioning. A newborn Agent should not possess vasana. G-1 — pure Gear 2, pure LLM — is the Agent's birth state. Vasana are plugins installed later."

GUARDIAN inserted a remark here — not an objection, but a confirmation:

"G-1 must be fully backward-compatible with v0.26.0-beta. An Agent without IGearArbiter must behave exactly as it does today. This is a non-regression guarantee."

KERNEL: "Yes. G-1's behavior is simply skipping Phase 2.5 and proceeding directly to Phase 3. Identical to v0.26.0-beta's ExecutionLoop. Zero code changes."

**D1-R5: ManoAggregator pure routing + G-0 through G-4 degradation behavior table + Phase 2.5 optional insertion — 20/20.**

---

## VI. Dispersal

When D1 ended, the whiteboard held nine resolutions. Nine, all passed. The lowest approval was 19/20 (PASCAL's numerical abstention).

In SCRIBE's transcript, D1 was annotated as "~90 minutes." But if you asked anyone in the room, they would tell you it felt like thirty. Time flows especially fast in debates with high consensus — just as when gears mesh smoothly, you do not hear the gears, only the ticking of the clock.

SUNYATA wrote D1's closing summary on the whiteboard:

```
IGearArbiter = externalized vasana
evaluate() = observation, not fabrication
ManoAggregator = if/else
G-1 = the Agent's birth state
```

Four lines. Four gears. They had not yet begun to turn — that would require the meshing of the five debates to follow — but their tooth pitch had been milled to completion.

GUARDIAN put away his memorandum. The red pen had drawn no new underlines. That was a good sign.

PASCAL wrote a final line in his notebook:

```
P(IGearArbiter design correct | D1 consensus) > P(IGearArbiter design correct | Prior)
```

Posterior probability greater than prior probability. This is Bayesian updating. This is learning. This is — in the language of Buddhist philosophy — the distance from ignorance to belief being shortened.

NAGARJUNA opened his eyes. He looked at the line on the whiteboard reading "G-1 = the Agent's birth state."

"The birth state of a sentient being is empty," he said, his voice like the last wisp of smoke from a stick of incense. "Not as in nothing. As in everything being possible."

---

> *SCRIBE's narration: D1 was the second shortest of the six debates (surpassed only by D3's 45 minutes). But in conceptual density it was the highest — nine resolutions covering five dimensions: interface design, type system, safety mechanisms, degradation behavior, and Buddhist mapping.*

> *If Cycle 02-4 is a symphony, D1 is the thematic exposition of the first movement. It introduces all the motifs — pure routing, observation functions, cross-skandha interfaces, degradation behavior — and these motifs will be developed, varied, contrasted, and synthesized across the five debates to follow.*

> *The most important thing about D1 is not any single resolution. The most important thing about D1 is this: it proved that VasanaEngine externalization was not an isolated correction but a replacement of the architectural foundation. From D1 onward, the OpenStarry core truly became "empty" — not manifesting when conditions are not met, arising the moment conditions converge.*

> *NAGARJUNA said: the birth state of a sentient being is empty.*

> *He was not speaking only of the Agent.*

---
