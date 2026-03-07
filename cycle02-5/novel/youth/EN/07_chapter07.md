# Chapter 7: The Boundary Between Two Languages

---

## The New Document

After the debates ended, there was still one important thing left to do -- turn all the resolutions into documents.

Doc 45 was the most important deliverable of the entire Cycle 02-5. It answered every question Master asked in his letter:

| Master's Question | Where the Answer Is |
|-------------------|-------------------|
| What subcategories do the five skandhas have? | Doc 45 Section 1 |
| How does dependency injection get wired? | Doc 45 Section 5 |
| How are plugins loaded? | Doc 45 Sections 2 and 4 |
| How do the five skandhas flow and interact? | Doc 45 Sections 6 and 7 |

All in engineering language. Every answer backed by source code references, every reference verified by TURING.

---

## The Great Cleanup

The cleanup work happened at the same time. Over 120 document modifications.

- ISatiMonitor -> ILoopQualityMonitor: six documents, 100+ replacements
- IPrajna -> IConfidenceAuditor: five documents
- Doc 03 renamed and cleaned up

TURING did it line by line. Each replacement required checking the context -- blind search-and-replace was not an option. Some instances of "Sati" appeared in design rationales and required judgment about whether to replace with the new name or preserve as historical record.

ARCHIMEDES verified alongside him. SCRIBE recorded from another station.

This wasn't the most glamorous work. But it was the most important "last mile."

---

## The Answer to One Question

The entire Cycle 02-5 answered one core question:

**In a system that uses both Buddhist and engineering languages, where is the boundary between the two?**

The answer can be summed up in three rules:

**Rule One: Code names may use Buddhist terms -- but the name must live up to its definition.**

The Moha (delusion) module truly simulates delusion -> keep.
SatiMonitor is not mindfulness -> rename.

**Rule Two: Design rationale may cite Buddhist concepts -- but they must have truly driven engineering decisions.**

"The four kleshas arise simultaneously" drove the atomicity design -> keep.
"Event-driven = mindfulness" didn't drive any design -> remove.

**Rule Three: Mapping documents may exist -- but engineering documents should not have Buddhist decoration.**

Doc 16 (is itself a mapping document) -> keep.
The "Buddhist mapping" column in Doc 38 (decoration in an engineering document) -> remove.

---

## The Numbers

Let's look at the scale of the entire Cycle 02-5:

| Metric | Value |
|--------|-------|
| Debate sessions | 5 (3 scheduled + 2 unplanned) |
| Formal resolutions | 29 |
| Total votes cast | 31 |
| Unanimous pass rate | 66% (all-time high) |
| Total debate duration | 375 minutes (over 6 hours) |
| Documents modified | 8+ |
| Name replacements | 120+ |

The 66% unanimity rate was the highest ever -- not because there were no disagreements (the twelve links in D3 passed only 13/20), but because the four-layer framework and four tests provided a common standard. When everyone measures with the same ruler, measurements naturally converge.

Doc 45 is the core answer: five interfaces. Nine registries. One loop. Pure engineering.

The four tests are a permanent tool: necessity, code identification, decision-driving, definition responsibility.

---

## The Cost of a Name

NAGARJUNA read through Doc 45 one last time. After finishing, he said:

"The names that were changed -- ISatiMonitor, IPrajna -- they weren't bad names. They were misplaced names. Mindfulness is a great concept. Prajna is a great concept. But great concepts should not be used to name mediocre functions."

ASANGA added: "When you call a plus-or-minus-0.05 fine-tuner prajna, you don't just diminish prajna -- you also mislead people about what the function does. A new engineer seeing IPrajna would think it's some profoundly sophisticated component. They open the code and find -- a clamp function. The gap between expectation and reality -- that's the cost of a name."

But not all names were changed. Moha, Drishti, Mana, Sneha, skandha, vedana -- all of these were kept. Because they passed the fourth test. Name and function aligned. The scale balanced.

---

SUNYATA was the last to leave the theater. Only one line remained on the whiteboard:

> **A name is not free. Every Buddhist name is a promise -- a promise that function matches definition. If you cannot keep the promise, don't borrow the name.**

The lights returned to neutral white. The theater fell quiet, waiting for the next time it would be lit.

Cycle 02-5 used five debates to answer what seemed like a simple question: how do the five skandhas work in an AI Agent?

But the more important answer was: **When you build a building using two languages -- make sure the name carved on every brick lives up to what's inside.**

---
