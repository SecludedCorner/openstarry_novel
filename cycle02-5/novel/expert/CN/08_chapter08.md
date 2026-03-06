# 第八章：新的文件

---

D5 结束后，圆形剧场安静了一段时间。

不是 D3 后那种等待 Master 的安静，也不是 D4 后那种余震的安静。这是一种「工作完成了，但还有一件事要做」的安静。

五场辩论。三十一次投票。二十九项正式决议加上六项附带事项。从凌晨三点 SUNYATA 调整灯光色温开始，到 D5 的最后一个 8/8 结束，整个 Cycle 消耗了大约六个半小时的辩论时间。

但辩论的结束不是研究的结束。辩论产出了决议。决议需要被落实。

---

## I. Doc 45

VITRUVIUS 和 KERNEL 在 D5 结束后立刻开始工作。

他们要写的是 Doc 45——`Five_Skandha_OOP_Architecture.md`——五蕴 OOP 架构。整个 Cycle 02-5 的核心工程产出。一份新文件。纯工程语言。Master 在信中要求的东西——「五蕴子类别、DI、agent core 如何载入五蕴 plugin、五蕴如何流转」——全部集中在这一份文件中。

VITRUVIUS 负责架构描述。KERNEL 负责 DI 布线和 Registry 细节。TURING 做原始码对照。

---

Doc 45 的结构从 D3 的六项投票中自然浮现：

**第 1 节：Root Interfaces（D3-R1）**

五根接口——IRupa、IVedana、ISamjna、ISamskara、IVijnana——的完备性论证。LINNAEUS 的覆盖率验证、BABBAGE 的类型代数定理、ASANGA 的阿毘达磨穷举分类公理、KERNEL 的微核心子系统映射——四个独立论证，同一个结论：五个足够。

PENROSE 的附带建议被写进了注脚：监控 vijnana 子接口数量（目前四个，未来六个——加上 IConfidenceAuditor 和 ILoopQualityMonitor；超过十个时考虑拆分）。

**第 2 节：PluginHooks 映射（D3-R2）**

九项 hook-to-Registry 映射的完整表格：

| PluginHooks 字段 | Registry | Skandha |
|-----------------|----------|---------|
| tools | ToolRegistry | samskara |
| providers | ProviderRegistry | samjna |
| listeners | ListenerRegistry | rupa |
| guides | GuideRegistry | vijnana |
| gearArbiters | GearArbiterRegistry | [samjna, vijnana] |
| volition | IVolition (single) | vijnana |
| kleshas | KleshaRegistry | vijnana |
| monitors | MonitorRegistry | [vedana, samjna, vijnana] |
| auditor | IConfidenceAuditor (single) | vijnana |

每一行都有 TURING 的原始码验证标记。

**第 3 节：SlashCommand（D3-R2a / D3-R2b）**

不属于任何蕴的例外——因为它绕过了 ExecutionLoop，不参与认知回路。类比：Unix 信号处理器。

GUARDIAN 的安全观察：SlashCommand 绕过 SafetyMonitor——如果 plugin 通过 SlashCommand 执行危险操作，五蕴的安全机制全部无效。这是一个已知的安全边界，需要在 plugin 审核时特别注意。

**第 4 节：Skandha 元数据（D3-R3）**

skandha 字段是元数据，不是路由基础。类型路由已经完备且无歧义。`validatePluginSkandha()` 维持 warning-only。

**第 5 节：DI 布线（A2 摘要）**

纯 DI（Pure DI），通过 `createAgentCore(config)` 作为唯一的 Composition Root。21 个组件的严格线性建立顺序。9 个 Registry——大部分是无依赖的 Map 容器。

关键模式：Lazy Accessor（IPluginContext 提供延迟存取）、Provider 能力过滤（allowedProviders manifest 字段）、Resolver 模式（providerResolver、guideResolver、modelResolver 使用闭包延迟解析）。

VITRUVIUS 用一张完整的 DI 链路图取代了文字描述。从 `agent.json` 到 `createAgentCore()` 到每一个 Registry 到 ExecutionLoop——一条清晰的线。没有循环依赖。没有隐式注入。每一个依赖都是显式传递的。

**第 6 节：ExecutionLoop 五蕴流（A4 摘要）**

九阶段执行流：

| Phase | 名称 | Skandha | 核心操作 |
|-------|------|---------|---------|
| 1 | 输入接收 | rupa | IListener → SparshEvent |
| 2 | 上下文组装 | vijnana | IGuide + SafetyMonitor |
| 3 | 认知处理 | samjna | IProvider.chat() |
| 4 | 齿轮路由 | vijnana+samjna | ManoAggregator + IGearArbiter |
| 5 | 审议 | vijnana | IVolition |
| 6 | 工具执行 | samskara | ITool.execute() |
| 7 | 感觉回馈 | vedana | VedanaSensor → ChannelVedana |
| 8 | 烦恼更新 | vijnana | IKlesha.perceive() |
| 9 | 回路控制 | — | VedanaEmergency + VitakkaWatchdog |

三层稳定：Inner tool loop（每轮）、Outer VedanaEmergency（5 连续 dukkha ticks）、Safety VitakkaWatchdog（10 cycles 或 5s）。触发条件严格递增。

**第 7 节：跨蕴互动矩阵（A5 摘要）**

5×5 互动矩阵。vijnana 互动密度最高（七条连接）。samskara 是最活跃的信号生产者。Model Delta 五层阈值公式。

**第 8 节：行蕴设计注记（D3-R4a / D3-R4b）**

行蕴的窄化——从佛学传统的 49 心所压缩为 ITool（外部可观察行为）。ASANGA 的坦白：这是五蕴架构中佛学自洽性最弱的部分。DC-6「行蕴保持开放，不锁定」的裁定继续有效。

**第 9 节：ILoopQualityMonitor 分类（D2 + D4 摘要）**

skandha: ['vedana', 'samjna', 'vijnana']。第一个三蕴 plugin。命名历史：ISatiMonitor（D2）→ ILoopQualityMonitor（D4-R1）。四项功能到三蕴的映射表。排除行蕴的理由。

**附录 A：十二因缘功能类比（D3-R5）**

sparsha→vedana→tanha→upadana 链的功能类比。明确标记为「功能类比」而非「形式映射」。尺度差异注解。

**附录 B：认知序列结构平行（D3-R6）**

citta-vīthi 八状态到 LoopState 六状态的映射。每个状态对的平行程度评级（high / medium-high / medium）。PENROSE 的理论观察：认知回路的结构趋同是功能需求的必然结果，不是刻意模仿。BABBAGE 的 FSM 态射分析——从十二因缘（失败）到认知序列（成功）的对比。

---

## II. 清理

在 VITRUVIUS 和 KERNEL 写 Doc 45 的同时，ARCHIMEDES 和 SCRIBE 开始执行清理。

清理清单从 D1 到 D4 的决议中汇总而来：

---

### 移除（REMOVE）

1. **Doc 38 L540-544**：三层规则佛学映射表的「佛学映射」栏——删除。保留「规则层」和「工程语义」栏。

2. **Doc 44 L478**：三学映射行——删除。

3. **Doc 43 全文**：
   - 标题更改：「Mindfulness Architecture」→ 由 D2/D4 后的最终名称决定
   - 75+ 处 ISatiMonitor → ILoopQualityMonitor
   - 移除 event-driven = mindfulness 等价
   - 移除 bhavanga-citta retrofitting（三处）
   - 移除 DN 22 经文引用
   - 加入「命名说明」段落

4. **Doc 37**：
   - 移除「佛学解释」栏（无工程信息增量）
   - 移除 sila 隐喻
   - 3 处 IPrajna → IConfidenceAuditor

5. **Doc 03**：
   - 文件名：Sila_Prajna_Security_Framework → Plugin_Security_Lifecycle
   - 移除佛学映射表
   - 清理 TypeScript 注释中的种子理论
   - 保留五状态模型和三层安全模型

6. **Batch A 五项**：散布在多份文件中的 sila/upaya/smrti/event-driven=mindfulness/trisiksa 映射——全部移除。

---

### 迁移至附录（RELOCATE）

1. **Doc 44 Section 10 剩余**：移至 Appendix_C（设计决策佛学背景）。

2. **Batch B 八项**：包含 NAGARJUNA 的两谛评论、bhavanga-citta 映射、经文引用、跨学科对照表等——全部移至对应附录。

3. **特殊处理 B-6**：PASCAL 的数学形式化（`Var(epsilon) = f(theta_moha)`）保留在主文。只有《成唯识论》引文移至 Appendix_C。

---

### 保留（KEEP）

1. **蕴类型名称**：rupa、vedana、samjna、samskara、vijnana——代码标识符。

2. **Klesha 模块名**：Moha、Drishti、Mana、Sneha——代码标识符，DC-1 确认。

3. **设计理由中的佛学概念**：vasana 后天薰习、四烦恼同时俱起、CoarisingBundle、sahaja 定义修正、samsaric stall——全部通过三项测试。

4. **Doc 16 和 Doc 31**：Master 裁定恢复原状。佛学映射文件，不是装饰。

---

### 新建

1. **Doc 45**：五蕴 OOP 架构（正在撰写中）。

2. **Appendix_A**：佛学-工程术语表。

3. **Appendix_B**：八识学术参考（Doc 31 RELOCATE 的内容最终没有移过来——Master 裁定 Doc 31 保留）。

4. **Appendix_C**：设计决策佛学背景。

---

## III. 更名连锁

TURING 坐在他的工作站前，打开了所有受影响的文件。

ILoopQualityMonitor 的更名影响了六份文件，超过 100 处替换。IConfidenceAuditor 的更名影响了五份文件。Doc 03 的重命名和清理是第三条线。

三条线同时进行。每一处替换都需要确认上下文——不是盲目的搜索替换。有些「Sati」出现在设计理由的段落中，需要判断是替换为新名称还是保留为历史引用。有些「Prajna」出现在 Model Delta 公式中，需要同步更新公式中的变量名。

TURING 一行一行地做。这是他的方式——没有捷径，没有估算，只有逐行的精确。

ARCHIMEDES 在他旁边，负责验证每一处替换的上下文正确性。

SCRIBE 在另一边，记录 CHANGELOG。

---

## IV. 数字

Cycle 02-5 完成后，SCRIBE 统计了数字。

| 指标 | 数值 |
|------|------|
| 正式决议 | 29 项（D1-D5）+ 6 附带事项 |
| 投票总次数 | 31 次 |
| 全票通过 | 19/29（66%） |
| 最高票 | 20/20 或 8/8（19 项） |
| 最低票 | 5/8（D5-R2，63%） |
| 有争议的决议 | 10 项 |
| 少数意见存档 | 9 份 |
| 辩论总时长 | ~375 分钟（90+60+120+30+75） |
| 修改文件 | 8+ 份 |
| 新建文件 | Doc 45 + 3 份附录 |
| 更名替换 | 120+ 处 |

和之前的 Cycle 比较：

| | Cycle 02-3 | Cycle 02-4 | **Cycle 02-5** |
|---|-----------|-----------|----------------|
| 辩论场次 | 6 | 6 | **5** (3 预定 + 2 计划外) |
| 决议总数 | 27 | 55 | **35** |
| 全票率 | 41% | 31% | **66%** |
| 少数意见 | 5 | 12 | **9** |
| 新文件 | 4 | 3 | **4** |

全票率 66%——历史最高。不是因为没有分歧——D3-R5 的 13/20 和 D4-R1 的 13/20 证明分歧存在。全票率高是因为四层框架和四项测试提供了共同的判断标准。当所有人在同一把尺上衡量的时候，测量结果自然趋向一致。

---

## V. 最后的确认

Doc 45 完成后，VITRUVIUS 做了一次完整的审阅。

他确认了 Master 在信中要求的每一个问题都有了回答：

| Master 的问题 | 回答位置 |
|--------------|---------|
| 五蕴子类别 | Doc 45 §1 |
| DI 如何布线 | Doc 45 §5 |
| Agent Core 如何载入五蕴 plugin | Doc 45 §2, §4 |
| 五蕴如何流转 | Doc 45 §6, §7 |
| Sati plugin 蕴归属 | Doc 45 §9, D2 record |
| 佛学映射清理 | 8 份修改文件, D1 record |
| 佛学映射边界原则 | 四层框架 + 四项测试 |
| ILoopQualityMonitor/IConfidenceAuditor 规格 | D5 record, Doc 45 §9 |

每一个问题。每一个回答。用工程语言。

---

> *SCRIBE 旁白*

> *第八章是一座图书馆的整理记录。*

> *不是写书——是理书。把散落在五场辩论中的决议收集起来，放进正确的架子上。Doc 45 是新买的书——放在「架构」那一排。移除的映射是过期的期刊——从主架移到储藏室（附录），或者直接回收。更名是重新贴标签——确保每本书的书脊上印的名字和书里的内容一致。*

> *这不是激动人心的工作。这是必要的工作。*

> *D4 的天平。D5 的规格。它们是 Cycle 02-5 的精神——前者校准了名字和定义的关系，后者证明了工程可以纯粹地站在自己的腿上。但精神需要身体。需要有人打开每一份文件，找到每一处「ISatiMonitor」，把它替换为「ILoopQualityMonitor」——然后确认上下文。确认公式。确认引用。确认 CHANGELOG。*

> *TURING 一行一行地做了。ARCHIMEDES 一处一处地验证了。SCRIBE 一条一条地记录了。*

> *这就是研究的最后一公里。不是最难的一公里——但是最容易被忽略的一公里。发现问题是闪光的。解决问题是沉默的。*

> *Doc 45 是沉默的胜利。它不像 D4 那样有戏剧性的归谬。它不像 D1 那样有史无前例的十个 20/20。它只是一份文件——60 页的文件——用纯工程语言回答了 Master 的每一个问题。*

> *五蕴子类别？五根接口，九个子接口，三个弱继承。*

> *DI 布线？Pure DI，Composition Root 在 createAgentCore()，21 个组件线性建立。*

> *Plugin 载入？Manifest + Factory，双路径（Sandbox / Direct），八状态生命周期。*

> *五蕴流转？九阶段 ExecutionLoop，FSM 六状态，三层稳定。*

> *每一个答案都有原始码引用。每一个原始码引用都由 TURING 验证。*

> *天平在这里找到了平衡。不是因为两端的重量相等——而是因为两端都被精确地测量了。名字被校准了（D4）。规格被完成了（D5）。文件被清理了（D1）。架构被验证了（D3）。蕴归属被决定了（D2）。*

> *Cycle 02-5 问了一个看似简单的问题：五蕴在 agent core 中如何运作？*

> *答案用了六个半小时的辩论、三十一次投票、二十九项决议、一份新文件、八份修改文件、120 多处更名替换。*

> *但最终答案确实很简单：*

> *五个接口。九个 Registry。一个回路。*

> *纯粹的工程。*

---
