# 第一章：审计与准备

---

## R1 独立研究

九份研究同时启动。三条轨道、十五位主笔。

### Track A：五蕴工程架构

Track A 是 Master 的首要任务——用纯工程语言回答五蕴架构的四个核心问题。五个子项由十二位研究者分工：

| 子项 | 主笔 | 内容 |
|------|------|------|
| A1 蕴子类别 | LINNAEUS + ASANGA | 五蕴的完整子类别树，对照 SDK 原始码 |
| A2 DI 布线 | VITRUVIUS + KERNEL + TURING | agent-core → plugin-loader → loop 的完整 DI 链 |
| A3 Plugin 载入 | DARWIN + MESH | 从 agent.json 到 running hooks 的完整流程 |
| A4 执行流 | HERACLITUS + WIENER + BABBAGE | sparsha → vedana → samjna → volition → tools → feedback |
| A5 跨蕴互动 | LEIBNIZ + ATHENA + PENROSE | vedana→klesha→arbiter→volition→action 的互动矩阵 |

A1 的子类别树揭示了一个重要的结构特征：识蕴拥有最多的子接口（IGearArbiter、IVolition、IKlesha、IConfidenceAuditor），而行蕴最简（ITool 单一接口）。这个不对称是有意义的——识蕴是「判断」，判断的维度天然比「行动」的维度多。

A2 追踪了完整的依赖注入链。三位研究者花了两天，从 AgentCore 的构造函数开始，经过 PluginLoader 的 registry 分发，到 ExecutionLoop 的每一个 hook 调用点。结论：DI 链完整，但有两个已知缺口——IVedanaSensor 弱继承（不继承 IVedana）和 VedanaAssessment 布线预设为中性值。

A4 产出了完整的五蕴执行流图。HERACLITUS 用他对动态流程的敏感性，追踪了一个 SparshEvent 从诞生到消亡的完整生命周期。WIENER 用控制理论的语言重新描述了同一个流程——系统是一个闭回路控制器，用户目标是参考输入，Context 是状态反馈，Tool Call 是控制变量。BABBAGE 做了形式化，用有限状态机证明了流程的终止性。

### Track B：佛学映射审计

B1 由 ARCHIMEDES 和 SCRIBE 负责。工程实践专家逐文件、逐映射地扫描了七份 openstarry_doc 文件。方法是三项测试的机械性应用——每一个佛学映射都被测试三次，结果被记录在审计表中。

最终结果：50 个映射实例。

| 处置 | 数量 | 范例 |
|------|------|------|
| KEEP | 23 | Skandha 类型名、Klesha 模组名、DC 确认约束、CoarisingBundle |
| RELOCATE | 13 | PASCAL 数学形式化、MN 18 经典引用、佛学设计理由 |
| REMOVE | 14 | śīla/upāya/smṛti 标签、event-driven=正念、戒定慧映射 |

将近一半是 KEEP——不是所有佛学内容都是装饰。有些是身份（Klesha 模组名），有些是决策（五蕴分类驱动了 PluginHooks 设计）。但 14 个 REMOVE——纯粹的装饰，移除不改变任何工程规格。

ARCHIMEDES 有一个精确的判断：「不是移除整张表。是移除一栏。」他不用大锤砸核桃——他用手术刀分离工程内容和佛学装饰。

两份特殊文件被标记为 FILE REVIEW：Doc 16（Plugin 类型哲学映射，装饰比例 ~80%）和 Doc 31（八识运行时模型，装饰比例 ~70%）。它们的问题不在个别映射，而在整份文件的定位——是工程文件中嵌入了佛学？还是以佛学映射为目的的独立文件？

B2 由 NAGARJUNA、ASANGA、PASCAL 三人建构映射边界原则。三个维度的框架：

- **NAGARJUNA（二谛）**：世俗谛 = 工程语言。胜义谛 = 佛学概念。不要在世俗谛的文件中硬塞胜义谛的标签。
- **PASCAL（损害不对称）**：False Include 的损害是累积的（读者数 × 阅读次数 × 认知转换成本）。False Exclude 的损害是一次性的（搜寻成本）。E[累积] >> E[一次性]。有疑虑时倾向移除。
- **ASANGA（因果效力）**：佛学概念是否驱动了工程结果？有因果效力 → 保留。无因果效力 → 移除。

三个学科、三条路径、一个结论——装饰性映射应移除。

### Track C：Sati Plugin 定位

C1 由 TURING 和 GUARDIAN 负责功能分析。TURING 用纯工程术语列出了 SatiMonitor 的四个功能：事件订阅、滑动窗口、模式辨认、品质指标。以及一个关键的「不做」——不执行任何行动、不修改任何状态、不发出任何指令。

GUARDIAN 的工程类比：APM Agent + Behavioral Analytics + QoS Monitor + SPC Anomaly Detector 的混合体。

C2 由 ASANGA 和 LINNAEUS 负责蕴组成分析。他们提出了四个方案：

| 方案 | 蕴组成 | 理由 |
|------|--------|------|
| A | 受 + 想 | 感知 + 辨认，最简 |
| B | 受 + 想 + 识 | 感知 + 辨认 + 评估判断 |
| C | 想 + 识 | 辨认 + 评估，受蕴太薄 |
| D | 纯识 | 一切认知活动归识蕴 |

四个方案都有逻辑支撑，但也各有弱点。最终答案要在 D2 辩论中决定。

---

## R2 交叉审阅

二十位研究者组成交叉审阅网——每人审阅至少两份非本人主笔的报告。

TURING 做了最关键的工作——地毯式验证所有程序码引用。40 个以上的引用逐一比对 v0.28.0-alpha 原始码。结果：四个问题（10% 以下的错误率），全部为低或中严重度。没有致命错误。

他说了六个字：「引用干净。可以进入辩论。」

R2 的总结：
- **24 个共识点**：跨三条轨道，基础稳固
- **7 个开放问题**：辩论有明确焦点
- **4 个分歧点**：辩论会有交锋

管道通了。手术室准备好了。

---
