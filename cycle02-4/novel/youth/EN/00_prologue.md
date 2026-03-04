# Prologue: Tearing Out the Engine

---

The circular amphitheater's lights held steady at working brightness. Twenty lamps. Not a single one dimmed.

This amphitheater had been lit for five cycles now. Each cycle, twenty people sat here and debated. Each cycle ended, the lights went dark. A few days later, they came back on. Then a new cycle began.

Three days ago -- when Cycle 02-3 concluded -- SUNYATA offered an analogy. Six debates were like six gears, precisely machined. The tooth spacing was right, the axles were right. They were waiting to be assembled into a clock.

Three days.

No formal debates in those three days. But something happened in those three days -- something that changed everything before the formal debates even started.

---

GUARDIAN read the security memo three times.

Not a casual skim. The kind of reading where you underline key words in red pen, and each pass makes the lines thicker.

After the third read, he wrote three lines in his notebook:

- VasanaEngine has a rule base
- A rule base is a capability
- Capabilities should not be in the kernel

If you're working on a car, you pop the hood and spot a component inside -- it has its own memory, its own judgment, its own decision-making ability. You'd ask: why is this component inside the engine? It's not part of the engine. It's an independent device that just happened to be stuffed in there.

VasanaEngine was that component. It was in the kernel, but it didn't belong in the kernel.

---

NAGARJUNA arrived at the same question at the same time, but in an entirely different language. He didn't know about GUARDIAN's analysis. GUARDIAN didn't know about his. Two people in different rooms, using different languages, derived the same conclusion.

"Vasana (habitual patterns) are cultivated through experience," he said with his eyes closed.

In plain language: your habits are something you live into, not something you're born with. A baby has no habits. A newborn AI Agent shouldn't be forced to have them either.

If VasanaEngine (the habitual-pattern engine) is part of the kernel, that means every Agent is born with a built-in set of habits. That's wrong.

Two people. Different starting points. The same destination. GUARDIAN approached from security -- the kernel shouldn't contain capabilities. NAGARJUNA approached from Buddhism -- vasana are acquired, not innate. Same conclusion: tear it out.

---

SUNYATA wrote the contradiction on the whiteboard. Then he did something he'd never done before -- he pressed the comm panel and contacted Master directly.

"VasanaEngine should not be in the kernel."

Master's reply was just two words: "That's right."

That "That's right" wasn't surprise. It was "I've been waiting for you to discover this yourselves."

Then Master said: "If VasanaEngine isn't in the kernel, ManoAggregator degrades to pure routing. if/else. Like an EventBus -- just a relay station."

SUNYATA paused when he heard this. "Pure routing" meant the kernel does almost nothing -- it just checks whether a plugin can handle things, hands off to it if yes, hands off to the LLM if no. The entire kernel's complexity shrinks from a hundred lines to twenty.

VasanaEngine was extracted. It got a new name: **IGearArbiter** -- the gear arbiter. A plugin you can install or remove.

Like an app on your phone. You can install a navigation app, or not. Without it, the phone is still a phone -- you just have to read road signs yourself. With it, you get extra convenience. But a navigation app isn't part of the phone's core -- it shouldn't be soldered onto the motherboard.

That same conversation also resolved a long-lingering question: do we need to formally distinguish "required plugins" from "optional plugins"? The answer was unexpectedly simple -- no. The "Five Skandha (aggregates) completeness check" designed back in Cycle 02-2 already covered this need. No new mechanism required.

SUNYATA later wrote a single line in the record: "Review existing decisions before proposing new ones."

This lesson matters more than it looks. In a research project spanning five cycles with hundreds of decisions, the biggest time-waster isn't "can't think of an answer" -- it's "forgetting that the answer already exists."

---

PASCAL -- the team's newest member -- was in another office, poring over the previous cycle's reports. He joined the team in Cycle 02-3, specializing in decision theory and probability. His notebook was filled with sketches of Beta distributions. He didn't know those sketches would break deadlocks three times in the debates three days later.

---

The fourth letter arrived on the evening of the third day.

The first three letters changed "what," "how to fix it," and "how it moves." The fourth letter changed -- **how it all becomes one whole.**

Six directives:

- M-1: Extract VasanaEngine; design a new interface
- M-2: Six long-pending questions -- resolve them all
- M-3: Sparsha (contact) and manasikara (attention) -- are they events? Or the starting point of causation?
- M-4: Sati (mindfulness) is not a periodic check
- M-5: Where do samskara's (volition/formation) results go? More important than it looks
- M-6: Ten declarations. Strict microkernel. Zero built-in capabilities. Do not compromise.

M-6 was the sternest. Three words: "Do not compromise." Master had never used that tone in previous letters. Those three words meant: some things were compromised in earlier cycles. Not this time.

Six directives. Six debates. But not six independent problems.

SUNYATA stood before the twenty lamps and said: "Master has given us a field. Like a map -- every point has a value. Our job is not to solve six equations. It is to solve one field equation."

> *SCRIBE's narration: The fourth letter was different from the first three. The first three were like prescriptions from a doctor -- it hurts here, take this medicine. The fourth was like an X-ray -- what you see isn't a symptom, but the entire skeleton.*

---
