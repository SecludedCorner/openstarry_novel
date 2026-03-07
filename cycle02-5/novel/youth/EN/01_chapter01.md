# Chapter 1: Research and Preparation

---

## Nine Reports

Twenty researchers set to work at the same time. Imagine a team of detectives given different assignments, each going off to investigate, then coming back with clues to piece together a puzzle.

**Track A** had the most important task -- Master called it the "top priority": figure out how the five skandhas actually work in the code.

What are the five skandhas? In Buddhism, it's a way of dividing human experience into five categories: rupa (form/the external world), vedana (feeling), samjna (recognition), samskara (action), and vijnana (judgment). OpenStarry borrowed this classification to organize the functions of an AI Agent:

| Skandha | Meaning in the AI Agent | Example |
|---------|------------------------|---------|
| Rupa | Receiving external input | Receiving the user's message |
| Vedana | Sensing good or bad | Judging whether an operation is fast or slow |
| Samjna | Recognizing what something is | The language model understanding the user's intent |
| Samskara | Executing actions | Calling tools, searching files |
| Vijnana | Making judgments and decisions | Deciding which method to use for handling a request |

Twelve researchers spent a great deal of time tracing every connection in the code -- from system startup to receiving events to making decisions to executing actions, the complete flow.

The most interesting finding: vijnana has the most sub-interfaces (four), while samskara has the fewest (just one: ITool). This asymmetry is meaningful -- "judgment" naturally has more dimensions than "action." It's like in real life: making a decision is much more complex than carrying it out.

Control theory expert WIENER redescribed the entire system in his own terms -- the AI Agent is a closed-loop controller: the user's goal is the reference input, context is state feedback, and tool calls are control variables. Mathematician BABBAGE used finite state machines to prove the process always terminates (no infinite loops).

**Track B** was the Buddhist mapping audit. ARCHIMEDES (engineering practice expert) and SCRIBE (recorder) scanned seven documents line by line, finding 50 instances of Buddhist mappings. Their method was mechanical -- they ran the three tests on each mapping and recorded the results in an audit table.

Result: 23 should be kept (nearly half!), 13 should be moved to the appendix, and 14 should be removed.

This showed that not all Buddhist content is decoration. Some are part of the code's identity (like the name of the Klesha module), and some drove design decisions (like the five-skandha classification determining how plugins are organized). But there were indeed 14 purely decorative items -- removing them would not change any engineering specification.

ARCHIMEDES's criterion was precise: "Don't remove the whole table. Remove one column." He didn't use a sledgehammer on a walnut -- he used a scalpel to separate engineering content from Buddhist decoration.

**Track C** was the SatiMonitor identity analysis. Master had asked a key question: which skandhas does this component actually belong to? Four proposals were put forward, each with its own logic. The final answer would be decided in the debates.

---

## Cross-Verification

After the independent research, everyone checked each other's work.

The most important checker was TURING -- the source code analysis expert. He did something extremely tedious but extremely important: he took every code reference cited in the nine research reports and compared them one by one against the actual source code. Over 40 references.

Result: four minor issues (none serious), an error rate below 10%.

He said just six words: "References clean. Ready to debate."

It was like a teacher saying "the exam questions have been confirmed free of typos" before a test -- everyone could answer with confidence.

---

## Preparation Complete

Cross-verification results:
- 24 points of consensus (things everyone agrees on)
- 7 open questions (things that need debate)
- 4 points of disagreement (things that will see real clashes)

24 points of consensus meant the foundation was solid -- the conclusions from all three research tracks had high overlap. 7 open questions meant the debates had clear focus -- they wouldn't be aimless. 4 points of disagreement meant there would be real confrontation -- not just going through the motions.

Three debates awaited them:
- **D1**: Where are the boundaries for Buddhist mappings? (What stays, what goes)
- **D2**: What is the true identity of the mindfulness component? (Which skandhas does it belong to)
- **D3**: Can the five-skandha architecture hold up? (Are five pillars enough)

The pipeline was clear. The operating room was ready.

---
