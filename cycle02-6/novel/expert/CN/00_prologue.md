# 序章：从清创到精密工程

---

Cycle 02-5 是一次大规模清创手术。

二十位研究者在五天内做出 29 项决议，DC Master 覆议推翻其中两项（D3-R3 四智映射、D4-R1 心所命名），整个团队对七份设计文件进行去装饰化重构——移除不具驱动力的佛学标签、统一命名惯例、拆解错误的蕴归属映射。那五天像是对 codebase 进行 dead code elimination：不是增加功能，而是移除积累的语义债务。

Cycle 02-6 的调性截然不同。前一轮回答的是「什么是错的」；这一轮要回答的是「正确的规格长什么样」。

---

## 双重输入

DC Master 发出两封信件，分别触发工程轨和哲学轨。

**工程信件**指向 Plan29 交付后的六个 Open Questions（OQ-29-1 至 OQ-29-6）。Plan29（v0.29.0-alpha）新增了 `ILoopQualityMonitor`（回路品质监控器接口）和 `IConfidenceAuditor`（信心度审计接口），但两者都只有 SDK 骨架——Registry 已接入 `PluginHooks`，类型定义已 export，却没有预设实现、没有计算公式、没有与 `ManoAggregator` 的布线。Master 要求研究团队回答：品质怎么算（OQ-1）？Layer 3 怎么整合（OQ-2）？审计策略方向（OQ-3）？事件订阅清单（OQ-4）？权重可配置性（OQ-5）？整体怎么放进 Plan30（OQ-6）？

**哲学信件**直指行蕴（samskara-skandha）的定义问题。Master 明确批评唯识学派将 49 个心所归入行蕴的做法「非常有问题」，并要求以原始经典（如是我闻）为第一手依据进行深掘。这不是一个装饰性的研究方向，而是直接影响 `ISamskara` 接口未来拓展路径的基础判定。

---

## SUNYATA 的双轨架构

研究总监 SUNYATA 据此设计了双轨结构，并建立跨轨道优先权：

| 轨道 | 范畴 | 子项 | 团队 |
|------|------|------|------|
| Track A | AuditContext 类型 + 审计日志 | A1-A4 | VITRUVIUS, KERNEL, GUARDIAN, ARCHIMEDES, WIENER, BABBAGE |
| Track B | ILoopQualityMonitor 实现规格 | B1-B4 | WIENER, ATHENA, BABBAGE, HERACLITUS, TURING, PASCAL |
| Track C | 行蕴深掘 | C1-C4 | NAGARJUNA, ASANGA, LINNAEUS, PENROSE, PASCAL |
| Track D | 工程同步 | D1-D2 | TURING, ARCHIMEDES, VITRUVIUS, GUARDIAN |

跨轨道影响协议的关键规则：**哲学结论（D1）先于工程设计（D2/D3），确保蕴归属判定不被工程便利性覆盖。** 若 C1-C4 的结论与 A/B 的设计假设产生冲突，工程轨必须等待哲学裁定。

R1 产出 14 份独立研究报告。R2 交叉审阅发现 24 个共识点、仅 3 个分歧点。R3 三场辩论、245 分钟、17 项决议、13 项全票（20/20）、0 项否决。

这是一轮精密工程。
