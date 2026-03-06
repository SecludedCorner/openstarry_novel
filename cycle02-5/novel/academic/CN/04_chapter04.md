# 第四章：完备性——D3 五蕴 OOP 架构辩论

---

**时长**：~120 分钟 | **主席**：SUNYATA | **投票**：6 项

## 五根接口充分性（D3-R1：20/20）

四个独立论证收敛至同一结论：IRupa、IVedana、ISamjna、ISamskara、IVijnana 五个根接口足以覆盖所有功能需求。

- **LINNAEUS**：100% 功能覆盖率验证。
- **BABBAGE**：类型代数完备性定理（Q.E.D.）。
- **ASANGA**：阿毗达磨穷举分类公理。
- **KERNEL**：五个微核心子系统映射（I/O、感测、计算、执行、调度）。

PENROSE 附带建议：监控 vijnana 子接口数量（目前 4，未来 6；超过 10 时考虑拆分）。

## PluginHooks 映射正确性（D3-R2：20/20）

TURING 逐行源代码验证，九项映射全部正确。

焦点讨论：SlashCommand 不属于任何蕴——因为它绕过整个 ExecutionLoop（类比：Unix 信号处理器）。GUARDIAN 安全观察：SlashCommand 绕过 SafetyMonitor，如果 plugin 通过此路径执行危险操作，五蕴安全机制全部无效。此观察记入 Doc 45。

## skandha 作为元数据（D3-R3：18/20）

维持现状——skandha 是元数据，不是路由基础。类型路由已完备。少数意见（GUARDIAN、LINNAEUS）：即使只是 warning 的一致性验证也有审计价值。

## ISamskara 子接口（D3-R4：20/20）

维持 ITool 为唯一子接口。ASANGA 坦承：这是五蕴架构中佛学自洽性最弱的部分——传统行蕴涵盖 49 心所，OpenStarry 窄化为外部行为（ITool）。HERACLITUS 的动态论证：IVolition 在 Phase 5，ITool 在 Phase 6——将 IVolition 移至行蕴会造成「行蕴在行蕴之前」的概念错位。

DC-6「行蕴保持开放，不锁定」继续有效。

## 十二因缘（D3-R5：13/20 Proposal C）

最具争议的 D3 投票。Proposal C（选择性附录映射）胜出。

- **NAGARJUNA**：尺度不匹配——十二因缘描述三世因果（宏观），ExecutionLoop 描述单次认知处理（毫秒级）。
- **BABBAGE**（投 B）：十二因缘是线性链，ExecutionLoop 是有回圈的 FSM——图结构根本不同。
- Proposal B（不映射）获 7 票——D3 最大的少数意见群。

## 认知序列（D3-R6：17/20 Proposal C）

比十二因缘获得更高共识——因为描述的是相同尺度现象（单一认知活动的内部阶段）。HERACLITUS 提供了八状态对比表，五个「高」或「中高」平行。

BABBAGE 从 B（十二因缘）转为 C（认知序列）——FSM 态射分析是转向的关键论据。十二因缘没有态射。认知序列有。

PENROSE 理论贡献：认知回路的结构趋同是功能需求的必然结果，不是刻意模仿。

## 架构评估结论

**v0.28.0-alpha 的五蕴 OOP 架构在结构层面是充分的。** 三个已知缺口（弱继承、VedanaAssessment 布线未完成、IConfidenceAuditor/ILoopQualityMonitor 尚未实作）都是计划中的增量改进。

---
