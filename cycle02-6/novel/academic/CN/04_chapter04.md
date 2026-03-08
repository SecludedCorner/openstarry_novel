# 第四章：双通道整合架构 —— Layer 2/3 的正交分离设计

---

## 4.1 决策机制的形式化描述

OpenStarry 的核心路由决策为阈值比较：若 $c > \theta$ 则采用仲裁器推荐方案，否则走预设方案。Cycle 02-6 引入 IConfidenceAuditor（Layer 2，调整 $c$）和 ILoopQualityMonitor（Layer 3，调整 $\theta$）。核心问题：如何让两者同时生效而不互相干扰？

---

## 4.2 三个候选方案与选择

**方案 A（串联）**：$Q$ 先改阈值，审计员在新阈值下评估。存在序列依赖。
**方案 B（耦合）**：$Q$ 和审计员同时影响信心度与阈值。存在交叉项。
**方案 C（正交）**：审计员仅改信心度，品质监控器仅改阈值。完全独立。

D2-R4（20/20 全票）选择方案 C。

---

## 4.3 方案 C 的形式化定义

**Layer 2**：$c_{adj} = c_{raw} + \text{clamp}(\Delta c, -0.05, +0.05)$

**Layer 3**：$\theta_{adj} = \max(\theta_{floor}, \; \theta_{base} \times (1 - \alpha \cdot Q))$，其中 $\alpha = 0.10$

**最终路由**：$c_{adj} > \theta_{adj}$ → arbiter\_gear，否则 default\_gear

---

## 4.4 设计优势

**正交性**：Layer 2 仅操作 $c$，Layer 3 仅操作 $\theta$，不存在 $f(c, Q)$ 或 $g(\theta, \Delta c)$ 形式的耦合函数。两元件可独立开发、测试、部署。

**BIBO 稳定性**：$c_{adj}$ 受 $[0,1]$ 夹持，$\theta_{adj} \geq \theta_{floor} > 0$，无交叉项则无通道间正反馈放大路径。

**保守退化**：无审计员则 $\Delta c = 0$；无品质监控器则 $Q = 0$。任一元件缺失时系统行为等价于该元件不存在的版本。

---

## 4.5 品质分数传输：Pull + Push 双通道

| 消费者 | 需求 | 传输模式 |
|--------|------|---------|
| ManoAggregator（L3） | 即时数值 | Pull：`loopQualityFn()` 回调 |
| IConfidenceAuditor（L2） | 丰富背景 | Push：extras bag via `audit:context_contribute` |

Push 通道写入 `loopQuality:vector`（四维）和 `loopQuality:composite`（$Q$）。生命周期为 per-routing-cycle，每次路由结束后 extras bag 清空（LEIBNIZ #14 强调：避免过时信息累积）。

---

## 4.6 五层决策模型

```
L0: EventBus          -- 基础事件流
L1: Klesha（烦恼）     -- 四个情绪模块调整阈值
L4: Vedana Emergency   -- 紧急感受直接降低阈值（安全关键，优先级最高）
L3: LoopQuality        -- 品质分数微调阈值（α=0.10）
L2: Audit              -- 审计员微调信心度（±0.05）
→ 最终比较: c_adj > θ_adj → 路由决策
```

Layer 顺序遵循优先级递减原则。Plan30 的成功标准：L0~L4 全部有实际信号路径。

**边际情境**：多监控器以简单平均聚合（Phase 1）；监控器超过 5000ms 未更新视为过期，$Q = 0$，L3 不生效。

---
