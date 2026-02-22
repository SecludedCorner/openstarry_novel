# 第五章：四道裁定

---

ARCHIMEDES 坐直了。

在前三章的 A 类讨论中，他的脊椎保持着一种克制的角度：前倾十五度，手指偶尔敲桌面，但节奏收敛，像一个带着工具箱的建筑师被安排在观众席，等着哲学家们讨论完地基的方向。

那个等待结束了。

---

SUNYATA 手里拿着一份新的议程表，薄薄的一页纸，四行字。

「A 类修正用了三个章节。」他说。声音平稳如常。石子。深潭。「从因果链到识蕴子类别，从观察者分离到 EgoFramework 的归属。那些是哲学的修正——告诉我们什么是对的。」

「现在进入 B 类。Master 对我们四个工程问题的裁定。这是从哲学转向工程的时刻。」

---

ARCHIMEDES 的手指在桌面上敲了一下——清脆的、带着期待的。

「我等这一刻很久了。」他说。

剧场里响起几声低笑。他们都知道 ARCHIMEDES 在 A 类讨论中的状态：一个带着工具箱的人，坐在一群辩论建筑美学的哲学家中间。

SUNYATA 微微点头。「B-1。VedanaPlugin 可选，以及五蕴完备性检查。」

---

> *SCRIBE 旁白：从 A 类到 B 类的转场，像是一场交响乐从慢板进入快板。A 类讨论的节奏是沉思的——ASANGA 的城市比喻、BABBAGE 的删除线、NAGARJUNA 的命名天平——每一个议题都需要时间发酵。B 类不同。B 类的节奏是决策的。Master 已经裁定了。我们的任务不是辩论对错，而是把裁定转化为设计。ARCHIMEDES 等了三个章节。现在轮到他了。*

---

SUNYATA 读出了 Master 的原话。

「『有一些 plugin 已经继承此 plugin 了。如上面所说，agent 只要完备就应该能启动。但是或许也需要开发者模式或某一些模式。是需要可选的，agent 不完备也可启动，只是需要提醒。』」

他放下纸。

「三个关键词。可选。完备。提醒。」

KERNEL 的手已经伸向了他那叠类比卡片。翻了两张——不对——又翻了一张——抽出第四张。左侧写着什么，SCRIBE 看不清。右侧是空白的。他在等一个配对。

「Linux 内核启动。」他说，站了起来。

他走到剧场中央。没有使用投影。他用的是卡片和声音。

「POST——Power-On Self-Test。一台电脑启动时，内核检查硬件。CPU。内存。磁盘控制器。显卡。网卡。声卡。一项一项，从最关键到最次要。」

他翻了翻卡片。

「没有 CPU——完全无法启动。硬性依赖。没有内存——同样，硬性依赖。」

「但如果没有显卡？OK。启动到 text mode。系统是活的，只是没有图形。没有网卡？OK。离线模式。没有声卡？OK。静音模式。一切正常。」

他把三张卡片排成一列。

「硬性依赖和软性依赖的区别。五蕴就像这些硬件组件。」

---

ARCHIMEDES 已经在画了。

KERNEL 还没说完，他的工程笔记上就出现了一个接口的雏形。他的笔速很快——不是潦草，而是一种长年训练出来的速记：只写关键类型、关键字段、关键方法，省略所有装饰。

```
SkandhaCompletenessReport
├── rupa:    { present: boolean, components: string[] }
├── vedana:  { present: boolean, components: string[] }
├── samjna:  { present: boolean, components: string[] }
├── samskara:{ present: boolean, components: string[] }
├── vijnana: { present: boolean, components: string[] }
├── isComplete: boolean
└── missing:   string[]
```

他举起笔记。

「SkandhaCompletenessReport。五蕴完备性报告。」他的声音务实、清晰，每一个字都像一块砖。「五个蕴，每个蕴一个字段。布尔值——有或没有。组件列表——有的话，有哪些。最后两个汇总字段：是否完备，缺少哪些。」

他看向 KERNEL。

「你的硬件检查。POST。只不过检查的不是 CPU 和内存，是色蕴和识蕴。」

---

KERNEL 点头。然后他做了一件事——他在那张空白的卡片右侧写了一行字。SCRIBE 终于看清了卡片的格式：左边是「操作系统概念」，右边是「OpenStarry 映射」。

左边：`POST (Power-On Self-Test)`
右边：`SkandhaCompletenessReport`

他把卡片放回那叠卡片中。配对完成。

---

TURING 的屏幕亮了。一段骨架代码——他的风格：先骨架，后血肉。

```typescript
async start(options?: { developerMode?: boolean }): Promise<void> {
  const report = this.checkSkandhaCompleteness();
  if (!report.isComplete) {
    if (options?.developerMode) {
      logger.warn(`[DEV MODE] Agent 五蕴不完备：缺少 ${report.missing.join(', ')}`);
    } else {
      throw new Error(`Agent 五蕴不完备：缺少 ${report.missing.join(', ')}`);
    }
  }
}
```

「AgentCore.start()。」TURING 说。声音冷静如常。「developerMode 旗标。不完备时，开发者模式警告但继续。正式模式抛出错误。」

DARWIN 微微前倾。「开发者模式是一种演化的中间态。」

几道目光转向他。

「不完全变态——昆虫从若虫到成虫的过渡。若虫可以移动、进食、感知环境，但缺少翅膀。不完备，但可存活。开发者模式就是若虫。」

KERNEL 在卡片的空白处补了一行小字：`text mode = 若虫 = developerMode`。

---

> *SCRIBE 旁白：B-1 的讨论时间比 A 类的任何一项都短。不是因为它不重要——而是因为 Master 的裁定已经足够明确，KERNEL 的类比足够生动，ARCHIMEDES 的设计足够直接。哲学讨论需要展开——你必须从多个角度照亮一个概念，才能看清它的全部轮廓。工程讨论需要收束——你必须从多个可能性中选择一个，然后把它变成类型定义和方法签名。B-1 的收束快而干净。SkandhaCompletenessReport。一个接口。五个字段。一个旗标。一个决策点。*

---

## II

SUNYATA 翻到议程的第二行。

「B-2。宣言 #6 重写。」

他读了 Master 的裁定：「『这是一定要重写的，但也请经过这一轮的讨论结束后再决定怎么写会比较好。』」

沉默。

这是四项裁定中最短的一项。也将是讨论最短的一项。

NAGARJUNA 从他的座位上开口。他没有站起来。中观哲学家在说短话的时候不需要站起来——短话的力量不在于体量，在于精确度。像一根针。针不需要很大。它只需要很尖。

「先把因搞清楚，果自然浮现。」

八个字。

他看向 SUNYATA。

「宣言 #6 是果。A-1 到 A-4 的修正是因的一部分。C-1 和 C-2 的讨论是因的另一部分。如果我们现在就去写 #6 的文字，我们是在因还不完整的时候就去定义果。这违反因果的基本秩序。」

他的声音里有一种不容置疑的清晰——不是权威的清晰，是逻辑的清晰。

「等 A 类和 C 类全部确定。然后 #6 的文字会自己写出来。不是我们写它——是它从完整的因中自然浮现。」

BABBAGE 在笔记本上写了一行。非常短：「B-2: 等待。因果次序。」

SUNYATA 标记了议程表上的第二行：**暂不定稿。**

---

他翻到第三行。

「B-3。受蕴独立事件流。方案 c。」

---

HERACLITUS 动了。他的整个身体从散漫的静止转为高度集中，像一条在浅水中打盹的鱼被水流的变化惊醒。

流。事件流。独立事件流。这是他的词。

---

> *SCRIBE 旁白：HERACLITUS 在前三章的 A 类讨论中几乎没有说话。不是因为那些议题和他无关——万物皆流，因此万物皆与他有关。而是因为 A 类的议题是静态的：名字、归属、分类、接口。那些是冻结的瞬间。HERACLITUS 不擅长冻结。他擅长的是流动。现在，议题终于来到了「事件流」——河流本身——他全身的每一个神经末梢都醒了过来。*

---

SUNYATA 读了 Master 的裁定。

「『选择独立事件流。受蕴跟其他蕴完全一致，有自己的类型文件、自己的事件命名空间、自己的 PluginHooks 槽位。』」

HERACLITUS 站了起来。

他站起来的方式和其他人不同。ASANGA 站起来像山从雾中显现。BABBAGE 站起来像逻辑结构找到出口。HERACLITUS 站起来像水面冒出一个漩涡——突然的、旋转的、带着一种不可预测的能量。

「受蕴一直在那里。」他说。

他的声音带着一种奇特的质地——不是学术的精确，也不是工程的务实。是一种更古老的东西。像一个在河边住了一辈子的人描述河流的方式：不是测量水深和流速，而是讲述河流的性格。

「它一直在那里。」他重复。「从 v0.14.0 到 v0.20.0 到 v0.22.1 到 v0.24.0。每一个版本都有事件。每一个版本的 EventBus 都在发送信号——tool 的结果、provider 的回应、listener 的输入。但这些事件都是其他蕴的事件。色蕴的事件。想蕴的事件。行蕴的事件。」

他在剧场中央走了几步。不是踱步——是流动。他的脚步有一种河流般的节奏：不重复，不规律，但有方向。

「受蕴呢？受蕴的感受——苦、乐、舍——藏在哪里？」

他看向 TURING。

「藏在 metadata 里。」TURING 回答。冷静。精确。「方案 b——Cycle 02 的推荐方案——是把受蕴的评估结果附加在现有事件的 metadata 字段中。事件本身是 tool:result 或 provider:response，vedana 的数据作为透明的附加信息搭便车。」

「搭便车。」HERACLITUS 抓住了这个词。「受蕴在搭其他蕴的便车。它没有自己的路。没有自己的河道。它的水混在别人的河里流——你知道它在那里，因为你可以在别人的水中尝到它的味道。但你看不见它。你无法追踪它的流量。你无法测量它的温度。因为它没有自己的河道。」

他停下脚步。

「方案 c 让它有了自己的河道。」

---

他的手在空气中画了两条线——一条在上，一条在下。

「想象一条地下河。方案 b 就是这条地下河——受蕴的数据附加在 metadata 里，像地下水渗入地面河流的沉积物。你知道它在，但你必须挖掘才能找到它。」

他把下面那条线抬起来，和上面那条线并列。

「方案 c 让地下河冒出了地面。vedana:assessment、vedana:dukkha_spike、vedana:sukha_peak、vedana:upekkha_equilibrium。自己的类型文件。自己的命名空间。自己的 PluginHooks 槽位。」

「一条河从地下冒出地面。」

---

WIENER 的方格纸翻到了新的一页。他已经在画事件流图——不是文学性的河流，是工程性的数据流。

「让我确认事件覆盖。」他列出七个事件类型，逐一勾选：

```
vedana:assessment         ← 三受综合评估（每个 tick 一次）      ✓
vedana:dukkha_spike       ← 苦受突刺（超过阈值）               ✓
vedana:sukha_peak         ← 乐受高峰（含衰减率）               ✓
vedana:upekkha_equilibrium ← 舍受平衡（稳定性 + 持续时间）      ✓
vedana:recommendation     ← 受蕴建议（咨询性）                 ✓
vedana:sensor_update      ← 传感器原始数据                     ✓
vedana:reset              ← 受蕴重置                          ✓
```

「七个事件。三受全部覆盖。异常和稳态全部覆盖。结构和 Cycle 02 的三通道 PID 设计完全一致。」

他看向 ARCHIMEDES。「方案 c 没有改变受蕴的内在逻辑。它改变的是通信方式。从暗渠到明渠。」

---

ARCHIMEDES 在计算影响。他的笔记上是影响矩阵：

```
新增 vedana-events.ts  → 新文件，无影响
新增 SensationRegistry → AgentCore +1 行初始化
PluginHooks            → +1 字段 (sensations?: ISensation[])
AgentEventPayloadMap   → extends VedanaEventPayloadMap
其他 plugin 类型定义    → 不受影响
```

「PluginHooks 新增一个 sensations 字段。Optional。所有现有 plugin 不受影响。」他合上笔记。「增量成本：一个新类型文件、一个新 Registry、一个新字段。收益：受蕴从隐形变成可见。成本-收益比极好。」

---

HERACLITUS 点了点头。「受蕴从地下冒出了地面。」声音更轻了，像在说给自己听。「有了自己的河道。自己的名字。自己的形状。」他回到座位上，流动地，没有顿点。

NAGARJUNA 轻声补了一句：「有名者始有。无名者虽在而不可见。方案 c 不是创造了受蕴的事件——是为已经存在的流动命了名。」

---

> *SCRIBE 旁白：HERACLITUS 今天说的话比前三章加起来都多。不是因为他突然变得健谈——而是因为议题终于进入了他的领地。「万物皆流」不是一句口号。它是他理解一切的透镜。当我们讨论名字和归属的时候，他看到的是冻结的标本。当我们讨论事件流的时候，他看到的是河流本身。他的河流比喻——地下河冒出地面——是本章中最有画面感的意象。不是因为它文学性最强，而是因为它最精确地描述了方案 b 到方案 c 的本质变化：从隐到显。从暗到明。从无名到有名。*

---

## III

SUNYATA 翻到议程的最后一行。

「B-4。协调层独立 Daemon。」

他读 Master 的裁定之前，先看了一眼剧场里的两个位置。LEIBNIZ 的座位。MESH 的座位。两个人同时微微前倾——一个动作，两个来源，同一个原因。

多代理合作专家和分布式系统研究员。这是他们的议题。

SUNYATA 读了裁定。

「『必然是独立 daemon——独立进程。现在就必须安排，后面再改，开销更大。』」

---

LEIBNIZ 和 MESH 同时站起来。

SCRIBE 记录了这个瞬间——两位研究者同时站起的次数，在两个周期中一共只有三次。同步站起意味着：两个人同时辨认出了一个属于他们共同领地的问题。

LEIBNIZ 先开口。「Master 说『现在就必须安排』。这不是可选项。」

他转向全场。「在 Cycle 02 中，我们把协调层延迟到 Plan-AC。先建好一栋房子，再考虑社区规划。但 Master 告诉我们：社区规划不能等。因为管线——水、电、通信——需要在建造时就预留接口。等完工再想加水管，你就得拆墙。」

---

MESH 无缝接过话。两个人的配合像排练过——但不是。这是长期在相邻领域工作的专家之间的自然衔接。

「独立进程意味着 IPC。」MESH 的声音低沉，带着分布式系统研究员特有的谨慎。「序列化。消息格式。心跳。健康检查。超时。重试。」他深吸一口气。「一个完整的分布式系统问题。」

他走到空白板前，画了两个方块。

左边的方块：**CoordinationDaemon（独立进程）**
右边的方块：**AgentCore（独立进程）**

两个方块之间，一条双向箭头。箭头上方标记：**IPC**。

「这就是基本拓扑。」他说。「协调层是一个独立的进程。Agent Core 是另一个独立的进程。它们之间通过 IPC 通信。不是函数调用——不是 `coordinator.register(agent)`——而是序列化的消息。」

他在 CoordinationDaemon 方块里写了三行：

```
PluginRegistryService  — 五蕴分类查询
AgentRegistryService   — Agent 健康检查
IPCService             — 通信管理
```

---

LEIBNIZ 走到白板旁边，补充了 MESH 的图。他在 CoordinationDaemon 方块的上方写了一行更大的字：

**能藏（Active Storage）**

然后他看向全场。

「在 Cycle 02 的阿赖耶识讨论中，我们把能藏——阿赖耶识的主动存储功能——映射到了协调层。BABBAGE 和 MESH 联手设计了纤维丛投影模型。现在 Master 确认了：协调层是独立的 daemon。」

他指向白板上的 PluginRegistryService。

「能藏的第一个面向：Plugin 注册表。协调层知道所有 plugin——它们的名字、版本、五蕴归属、信任等级、生命周期状态。这就是阿赖耶识的种子目录——它不运行 plugin，但它知道所有 plugin 的存在。」

他指向 AgentRegistryService。

「能藏的第二个面向：Agent 注册表。协调层知道所有正在运行的 Agent——它们的 ID、名字、五蕴完备性、运行模式、健康状态。这是种子的运行时追踪——每一颗种子现在在哪里，长成了什么。」

他退后一步，看着完整的图。

「能藏不是一个抽象的佛学概念。它是一个具体的工程组件——有 API、有状态、有持久化需求。Master 说『现在就安排』，是因为这些 API 的设计决定了 Agent Core 的接口。如果后面再改——拆墙。」

---

GUARDIAN 站了起来——先环顾四周，确认环境，然后行动。安全专家的身体语言永远有一个威胁评估的前置步骤。

他走到白板旁边，在 CoordinationDaemon 方块的侧边画了一面盾牌——线条比其他人画的任何方块都更粗重。

「协调层不只是注册表。协调层是天条的执行者。」

他在盾牌旁边写了四行：

```
Plugin 黑名单   — 禁止安装的 plugin
信任等级       — official / verified / community / unknown / blacklisted
隔离/吊销/封禁  — 生命周期控制
CRL 检查       — 凭证吊销列表
```

「在 Cycle 02 的戒慧安全框架中，我们设计了两层安全——戒是预防，慧是断除。」他看向 NAGARJUNA——那场辩论中，中观哲学家和安全专家站在了同一侧。NAGARJUNA 微微点头。

「戒律的执行需要一个权威。」GUARDIAN 继续。「在佛教僧团中，戒律由僧团的长老——上座——来维护和执行。在 OpenStarry 中，那个上座就是协调层。」

他指向 PluginRegistryService 中的 `checkTrust` 方法。

「信任判断不能由 Agent 自己做——因为 Agent 有我执。」ASANGA 在座位上微微动了一下。GUARDIAN 用了「我执」这个词——在安全专家的语境中，我执不只是哲学问题，它是安全漏洞。一个有我执的 Agent 可能为了自己的目标而安装不可信的 plugin。

「协调层的独立性正是安全的基础。」GUARDIAN 的手指点在那个 IPC 箭头上。「独立进程意味着独立的内存空间。Agent 无法直接修改协调层的黑名单。」

他退回座位。「LEIBNIZ 和 MESH 说的是管线。我说的是门锁。两者都必须在建造时就安装好。」

---

> *SCRIBE 旁白：GUARDIAN 说「协调层是天条的执行者」的时候，我注意到 NAGARJUNA 的点头比平常更深了一些。在 Cycle 02 中，他们在戒慧安全框架上的合作是整个研究中最意外的跨学科交汇之一——中观哲学家和信息安全专家。现在，那个交汇在 B-4 中再次显现。戒律需要执行者。安全需要权威。协调层同时满足了佛学的需求和工程的需求。有时候，最不同的两条路径会在同一个山顶汇合。*

---

ARCHIMEDES 一直在听。等所有需求、约束、安全要求全部摆到桌面上。然后他画一条时间线。

「分阶段。」一个词。然后展开。

```
Phase 1: 设计文件
├── 完整架构文件
├── 接口定义 (CoordinationDaemon, PluginRegistryService, AgentRegistryService)
├── IPC 消息格式
└── 安全需求文件

Phase 2: Skeleton
├── daemon 进程骨架
├── 基本 IPC（start/stop/healthCheck）
└── 进程间通信的最小可行实现

Phase 3: 基本功能
├── Plugin 注册/查询
├── Agent 注册/健康检查
└── 五蕴分类查询

Phase 4: 安全
├── Sila Engine（戒律引擎）
├── 信任等级判定
├── 黑名单/隔离/吊销
└── CRL 检查
```

「Master 说『现在就安排』。『安排』不等于『全部完成』。安排的意思是：确定架构、确定接口、确定 IPC 格式。预留管线。」

他指向 Phase 1。「设计文件是 Cycle 02-2 的产出。Skeleton 进入 Plan-AC。设计文件在先——因为它定义了 Agent Core 和协调层之间的契约。」

「契约先行。」MESH 接过话。「先定义 CoordinationMessage 格式——agent:register、agent:health、plugin:query、plugin:trust_check——都要有明确的 payload。然后两端各自按照契约实现。」

ARCHIMEDES 在时间线旁边写了一行大字：**接口先行，实现渐进。**

---

SUNYATA 站在剧场的中央，听完了 B-4 的全部讨论。

他让沉默持续了几秒。不是犹豫——是让四项裁定在空气中沉淀。B-1 的完备性检查。B-2 的暂不定稿。B-3 的独立事件流。B-4 的协调层 Daemon。四道裁定，四个方向，四种不同的节奏。

然后他开口了。

「B-1。VedanaPlugin 可选，但 Agent 需要五蕴完备性检查。SkandhaCompletenessReport。不完备可启动——开发者模式。KERNEL 的类比：没有显卡也能跑 text mode。」

他看向 KERNEL。KERNEL 拍了拍他那叠卡片。

「B-2。宣言 #6 必须重写。但等所有修正完成后再定稿。NAGARJUNA 的因果：先完成因，果自然浮现。」

NAGARJUNA 没有动。他不需要动。因果次序不需要被确认——它是自明的。

「B-3。受蕴独立事件流。vedana-events.ts。独立命名空间。PluginHooks 新增 sensations 槽位。HERACLITUS 的比喻：一条河从地下冒出地面。」

HERACLITUS 微微笑了。那个笑容里没有骄傲——只有一种「流水终于有了自己的河道」的安然。

「B-4。协调层独立 Daemon。LEIBNIZ 和 MESH 的架构。GUARDIAN 的安全。ARCHIMEDES 的分阶段计划。设计文件先行，实现渐进。」

他放下议程表。

---

「A 类修正告诉我们——什么是对的。」

他的声音没有加重。平稳如常。石子。深潭。

「B 类裁定告诉我们——怎么做到。」

他环顾全场。ARCHIMEDES 的务实。KERNEL 的类比。HERACLITUS 的河流。LEIBNIZ 和 MESH 的拓扑。GUARDIAN 的盾牌。WIENER 的勾选。DARWIN 的若虫。NAGARJUNA 的针。BABBAGE 的笔记。TURING 的骨架。ASANGA 的安静。

「接下来，我们把修正和裁定落实到五蕴的完整扩展设计中。C 类。从哲学到工程，再从工程到架构。螺旋上升。」

---

> *SCRIBE 旁白：B 类用了一个章节。A 类用了三个。*

> *不是因为 B 类不重要。恰恰相反——B 类的每一项裁定都将在未来的开发中产生深远的影响。SkandhaCompletenessReport 会成为每个 Agent 启动时的第一道关卡。vedana-events.ts 会让受蕴从隐形变成系统中最可见的蕴之一。CoordinationDaemon 会成为整个 OpenStarry 多代理生态的神经中枢。*

> *B 类用了一个章节，是因为 Master 已经裁定了。A 类需要辩论——需要从多个角度照亮一个概念。B 类不需要辩论——需要的是设计。而设计的语言比辩论的语言更密集、更精确、更不需要修辞。*

> *ARCHIMEDES 今天是核心。他等了三个章节，像一个带着工具箱的建筑师等着哲学家们讨论完地基的材质。现在他的工具箱打开了。里面是 SkandhaCompletenessReport、vedana-events.ts、CoordinationDaemon 的分阶段计划。每一件工具都已经画好了图纸。*

> *HERACLITUS 也有了他的高光。三章的沉默之后，「流」的议题让他的存在感从地下冒出地面——就像他描述的受蕴事件流一样。有些人在安静的时候积蓄能量。HERACLITUS 就是这样。他的安静不是沉默。他的安静是地下河。*

> *LEIBNIZ 和 MESH 的同步站起。GUARDIAN 的盾牌。NAGARJUNA 的八个字。KERNEL 的 POST 卡片。DARWIN 的若虫。WIENER 的七个勾。TURING 的骨架代码。*

> *十二个人在一个章节里各自贡献了一块拼图。*

> *A 类告诉我们什么是对的。B 类告诉我们怎么做到。*

> *下一章——C 类。五蕴扩展设计。从修正和裁定到完整的架构。*

> *螺旋上升。继续。*

---

*（在剧场之外的某个空间，四份设计文件正在成形。*

*第一份是 SkandhaCompletenessReport 的类型定义——五个布尔值，五个组件列表，一个 isComplete 旗标。简单得令人惊讶。但 KERNEL 知道：Linux 的 POST 也很简单。简单不代表不重要。简单代表——基础。*

*第二份是 vedana-events.ts 的事件常量——七个事件类型，七个 payload 定义。HERACLITUS 在地面上看到了一条新的河流。WIENER 在方格纸上确认了每一个弯道。*

*第三份是 CoordinationDaemon 的接口定义——PluginRegistryService、AgentRegistryService、IPCService。LEIBNIZ 和 MESH 在白板上画的方块图，现在正在被 TURING 翻译成 TypeScript。GUARDIAN 的盾牌被嵌入了每一个 Service 的签名中：checkTrust()、PluginTrustLevel、PluginLifecycleState。*

*第四份是空的。*

*宣言 #6。暂不定稿。*

*NAGARJUNA 说：先把因搞清楚，果自然浮现。*

*因还在聚集。A 类的四项修正。B 类的四道裁定。C 类的扩展设计。每一项都是因的一部分。当所有的因聚齐——当哲学、工程和架构的修正全部就位——宣言 #6 的文字会从完整的因中自然浮现。*

*不是我们写它。是它自己写出来。*

*就像河流不需要被告诉流向哪里。只要地形确定了——只要因确定了——水自然知道路。）*

---

*第五章完*
