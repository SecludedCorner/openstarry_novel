# Chapter 4: Dual-Channel Integration Architecture -- Orthogonal Separation Design for Layers 2/3

---

## 4.1 Formal Description of the Decision Mechanism

OpenStarry's core routing decision is a threshold comparison: if $c > \theta$, the arbiter's recommended plan is adopted; otherwise, the default plan is used. Cycle 02-6 introduces IConfidenceAuditor (Layer 2, adjusting $c$) and ILoopQualityMonitor (Layer 3, adjusting $\theta$). The central question: how to make both effective simultaneously without mutual interference?

---

## 4.2 Three Candidate Schemes and Selection

**Scheme A (Serial)**: $Q$ first modifies the threshold, then the auditor evaluates under the new threshold. Sequential dependency exists.
**Scheme B (Coupled)**: $Q$ and the auditor simultaneously affect both confidence and threshold. Cross-terms exist.
**Scheme C (Orthogonal)**: The auditor modifies only confidence; the quality monitor modifies only the threshold. Fully independent.

Resolution D2-R4 (20/20 unanimous) selected Scheme C.

---

## 4.3 Formal Definition of Scheme C

**Layer 2**: $c_{adj} = c_{raw} + \text{clamp}(\Delta c, -0.05, +0.05)$

**Layer 3**: $\theta_{adj} = \max(\theta_{floor}, \; \theta_{base} \times (1 - \alpha \cdot Q))$, where $\alpha = 0.10$

**Final routing**: $c_{adj} > \theta_{adj}$ -> arbiter\_gear; otherwise default\_gear

---

## 4.4 Design Advantages

**Orthogonality**: Layer 2 operates solely on $c$; Layer 3 operates solely on $\theta$. No coupling functions of the form $f(c, Q)$ or $g(\theta, \Delta c)$ exist. The two components can be developed, tested, and deployed independently.

**BIBO stability**: $c_{adj}$ is clamped to $[0,1]$; $\theta_{adj} \geq \theta_{floor} > 0$. The absence of cross-terms eliminates inter-channel positive feedback amplification paths.

**Conservative degradation**: Without an auditor, $\Delta c = 0$; without a quality monitor, $Q = 0$. When either component is absent, system behavior is equivalent to the version where that component does not exist.

---

## 4.5 Quality Score Transmission: Pull + Push Dual Channel

| Consumer | Requirement | Transmission Mode |
|----------|------------|-------------------|
| ManoAggregator (L3) | Real-time numeric value | Pull: `loopQualityFn()` callback |
| IConfidenceAuditor (L2) | Rich context | Push: extras bag via `audit:context_contribute` |

The Push channel writes `loopQuality:vector` (four-dimensional) and `loopQuality:composite` ($Q$). The lifecycle is per-routing-cycle; the extras bag is cleared after each routing cycle completes (LEIBNIZ #14 emphasized: avoid accumulation of stale information).

---

## 4.6 Five-Layer Decision Model

```
L0: EventBus          -- foundational event stream
L1: Klesha             -- four emotion modules adjusting threshold
L4: Vedana Emergency   -- emergency feeling directly lowers threshold (safety-critical, highest priority)
L3: LoopQuality        -- quality score fine-tunes threshold (alpha=0.10)
L2: Audit              -- auditor fine-tunes confidence (+-0.05)
-> Final comparison: c_adj > theta_adj -> routing decision
```

Layer ordering follows the principle of decreasing priority. The success criterion for Plan30: L0 through L4 all have actual signal paths.

**Edge cases**: Multiple monitors are aggregated by simple averaging (Phase 1); a monitor that has not updated for more than 5000ms is treated as expired, $Q = 0$, and L3 does not take effect.

---
