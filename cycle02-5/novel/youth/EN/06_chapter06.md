# Chapter 6: A Debate That Didn't Need Buddhism

---

The fifth debate (D5) was completely different from the previous four.

No Buddhism. No Sanskrit. No philosophical arguments. Just engineering.

## Why Was It Different?

Because D5 discussed: the precise technical specifications for IConfidenceAuditor (the component that was just renamed). Master said: "The spec must be 100% complete, then hand it to the engineering team to build."

So only 10 engineering-related researchers participated. Buddhist scholars NAGARJUNA and ASANGA voluntarily stepped out -- because this debate didn't need Buddhist analysis.

## Nine Engineering Questions

TURING (the source code expert) had prepared a thorough "code archaeology" report beforehand -- studying 14 source code files and documenting all of the system's existing design patterns. With this report in hand, every question had a factual basis.

The nine questions included:
- Where does the new component go? --> Its own dedicated slot (not shared with anything else)
- Return type? --> Synchronous or asynchronous, either works (consistent with existing design)
- Timeout? --> 200 milliseconds; if it times out, treat it as no adjustment made
- Can you install multiple? --> No, one is enough (YAGNI principle -- don't build what you don't need)
- Weights for quality scores? --> Each of the four dimensions gets 25% (equal weights are safest when there's no data yet)

Nine votes, seventy-five minutes to complete. The final output was a complete specification that engineers could immediately start coding from.

## NAGARJUNA's Comment

After D5 ended, NAGARJUNA walked up to TURING and said:

"D4 proved that names must be accountable to their definitions. D5 proved that some engineering questions don't need definitions at all -- they just need specifications."

Two sentences that captured the essence of two debates.

---
