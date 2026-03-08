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
