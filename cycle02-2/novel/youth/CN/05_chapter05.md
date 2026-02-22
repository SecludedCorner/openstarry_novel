# 第五章：四道裁定

---

ARCHIMEDES 坐直了。

前三章的哲学讨论中，他一直克制地前倾着身体，像一个带着工具箱的建筑师被安排在观众席，等哲学家们讨论完地基的方向。

那个等待结束了。

---

SUNYATA 手里拿着一份新的议程表，薄薄一页纸，四行字。

「A 类修正用了三个章节——告诉我们什么是对的。现在进入 B 类。Master 对四个工程问题的裁定。从哲学转向工程。」

---

ARCHIMEDES 的手指在桌面上敲了一下。「我等这一刻很久了。」

几声低笑。大家都知道他在 A 类讨论中的状态：带着工具箱的人，坐在辩论美学的哲学家中间。

SUNYATA 点头。「B-1。VedanaPlugin 可选，以及五蕴完备性检查。」

---

> *SCRIBE 旁白：B 类的节奏和 A 类完全不同。A 类是沉思的——每个议题需要时间发酵。B 类是决策的。Master 已经裁定了，我们的任务是把裁定转化为设计。ARCHIMEDES 等了三个章节，现在轮到他了。*

---

SUNYATA 读出 Master 的原话：「『agent 只要完备就应该能启动。但也需要开发者模式，agent 不完备也可启动，只是需要提醒。』」

「三个关键词。可选。完备。提醒。」

KERNEL 的手伸向了他那叠类比卡片。翻了两张——不对——又翻了一张——抽出第四张。他在等一个配对。

「Linux 内核启动。」他说，站了起来。走到剧场中央，没有使用投影。他用的是卡片和声音。

「POST——Power-On Self-Test，开机自我测试。一台电脑启动时，内核逐一检查硬件。CPU。内存。磁盘控制器。显卡。网卡。声卡。一项一项，从最关键到最次要。」

他翻了翻卡片。

「没有 CPU——完全无法启动，硬性依赖。没有内存——同样，硬性依赖。」

「但如果没有显卡？OK，启动到 text mode。系统是活的，只是没有图形。没有网卡？离线模式。没有声卡？静音模式。一切正常。」

他把三张卡片排成一列。

「硬性依赖和软性依赖的区别。五蕴就像这些硬件组件。」

---

ARCHIMEDES 已经在画了。KERNEL 还没说完，他的工程笔记上就出现了一个接口的雏形：

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

「SkandhaCompletenessReport。五蕴完备性报告。」他的声音务实清晰。「五个蕴，每个一个字段。有或没有。缺少哪些。就是你的硬件检查——只不过检查的不是 CPU，是色蕴和识蕴。」

KERNEL 在空白卡片的右侧写了一行——左边：`POST`，右边：`SkandhaCompletenessReport`。配对完成。

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

「AgentCore.start()。」TURING 说。「developerMode 旗标。不完备时，开发者模式警告但继续。正式模式抛出错误。」

DARWIN 微微前倾。「开发者模式是一种演化的中间态——昆虫从若虫到成虫的过渡。若虫可以移动、进食、感知环境，但缺少翅膀。不完备，但可存活。」

KERNEL 在卡片的空白处补了一行小字：`text mode = 若虫 = developerMode`。

---

> *SCRIBE 旁白：B-1 的讨论比 A 类任何一项都短。不是因为它不重要——而是 Master 的裁定足够明确，KERNEL 的类比足够生动，ARCHIMEDES 的设计足够直接。一个接口。五个字段。一个旗标。快而干净。*

---

## II

SUNYATA 翻到议程的第二行。

「B-2。宣言 #6 重写。」

他读了 Master 的裁定：「『这是一定要重写的，但也请经过这一轮的讨论结束后再决定怎么写会比较好。』」

沉默。这是四项裁定中最短的一项。也将是讨论最短的一项。

NAGARJUNA 从他的座位上开口。他没有站起来。中观哲学家在说短话的时候不需要站起来——短话的力量不在于体量，在于精确度。像一根针。针不需要很大。它只需要很尖。

「先把因搞清楚，果自然浮现。」

八个字。

「宣言 #6 是果。A 类的修正是因的一部分，C 类的讨论是另一部分。如果现在就去写 #6，我们是在因不完整的时候定义果。这违反因果的基本秩序。」

「等 A 类和 C 类全部确定。然后 #6 的文字会自己写出来。不是我们写它——是它从完整的因中自然浮现。」

BABBAGE 在笔记本上写了一行。非常短：「B-2: 等待。因果次序。」

SUNYATA 标记了议程表上的第二行：**暂不定稿。**

---

他翻到第三行。「B-3。受蕴独立事件流。方案 c。」

---

HERACLITUS 动了。整个身体从散漫的静止转为高度集中。流。事件流。这是他的词。

---

> *SCRIBE 旁白：HERACLITUS 在前三章几乎没有说话。不是因为无关——「万物皆流」，因此万物皆与他有关。而是因为 A 类议题是静态的：名字、归属、分类。那些是冻结的瞬间。他擅长的是流动。现在议题来到「事件流」——河流本身——他全身都醒了过来。*

---

SUNYATA 读了 Master 的裁定。

「『选择独立事件流。受蕴跟其他蕴完全一致，有自己的类型文件、自己的事件命名空间、自己的 PluginHooks 插槽。』」

HERACLITUS 站了起来。

他站起来的方式和其他人不同。ASANGA 站起来像山从雾中显现。BABBAGE 站起来像逻辑结构找到出口。HERACLITUS 站起来像水面冒出一个漩涡——突然的、旋转的、带着不可预测的能量。

「受蕴一直在那里。」他说。声音带着一种奇特的质地——不是学术的精确，也不是工程的务实。是一种更古老的东西。像一个在河边住了一辈子的人描述河流的方式。

「它一直在那里。」他重复。「从 v0.14.0 到 v0.20.0 到 v0.22.1 到 v0.24.0。每一个版本都有事件。每一个版本的 EventBus 都在发送信号——tool 的结果、provider 的回应、listener 的输入。但这些事件都是其他蕴的事件。色蕴的事件。想蕴的事件。行蕴的事件。」

他在剧场中央走了几步。不是踱步——是流动。

「受蕴呢？受蕴的感受——苦、乐、舍——藏在哪里？」

「藏在 metadata 里。」TURING 回答。「方案 b 是把受蕴的评估结果附加在现有事件的 metadata 字段中。搭便车。」

「搭便车。」HERACLITUS 抓住了这个词。「受蕴的水混在别人的河里流。你知道它在那里，但你看不见它。因为它没有自己的河道。」

他停下脚步。「方案 c 让它有了自己的河道。」

---

他用手在空中画了两条线。

「方案 b 是地下河——受蕴的数据藏在 metadata 里，像地下水渗入地面河流的沉积物。方案 c 让地下河冒出了地面。vedana:assessment、vedana:dukkha_spike——自己的类型文件、自己的命名空间。」

「一条河从地下冒出地面。」

---

WIENER 在方格纸上列出七个事件类型，逐一勾选：

```
vedana:assessment          ← 三受综合评估      ✓
vedana:dukkha_spike        ← 苦受突刺          ✓
vedana:sukha_peak          ← 乐受高峰          ✓
vedana:upekkha_equilibrium ← 舍受平衡          ✓
vedana:recommendation      ← 受蕴建议          ✓
vedana:sensor_update       ← 传感器原始数据     ✓
vedana:reset               ← 受蕴重置          ✓
```

「七个事件。三受全部覆盖。和 Cycle 02 的三通道 PID 设计完全一致。」他看向 ARCHIMEDES。「方案 c 改变的是通信方式——从暗渠到明渠。」

---

ARCHIMEDES 在计算影响：

```
新增 vedana-events.ts  → 新文件，无影响
PluginHooks            → +1 字段 (sensations?: ISensation[])
其他 plugin 类型定义    → 不受影响
```

「增量成本极低。收益：受蕴从隐形变成可见。成本-收益比极好。」

NAGARJUNA 轻声补了一句：「有名者始有。无名者虽在而不可见。方案 c 不是创造了受蕴的事件——是为已经存在的流动命了名。」

---

> *SCRIBE 旁白：HERACLITUS 的河流比喻——地下河冒出地面——是本章最有画面感的意象。它精确描述了方案 b 到方案 c 的本质变化：从隐到显，从无名到有名。*

---

## III

SUNYATA 翻到最后一行。「B-4。协调层独立 Daemon。」

LEIBNIZ 和 MESH 同时微微前倾。多代理合作专家和分散式系统研究员——这是他们的议题。

Master 的裁定：「『必然是独立 daemon——独立进程。现在就必须安排，后面再改，开销更大。』」

---

两人同时站了起来。

LEIBNIZ 先开口。「Master 说『现在就必须安排』。这不是可选项。在 Cycle 02 中，我们把协调层延迟到后面。先建房子，再考虑社区规划。但 Master 告诉我们：管线——水、电、通信——需要在建造时就预留。等完工再加水管，就得拆墙。」

---

MESH 无缝接过话。两个人的配合像排练过——但不是。这是长期在相邻领域工作的专家之间的自然衔接。

「独立进程意味着 IPC。」MESH 的声音低沉，带着分散式系统研究员特有的谨慎。「序列化。消息格式。心跳。健康检查。超时。重试。一个完整的分散式系统问题。」

他走到白板前，画了两个方块。左边：**CoordinationDaemon（独立进程）**。右边：**AgentCore（独立进程）**。两个方块之间，一条双向箭头，上方标记：**IPC**。

「协调层和 Agent Core 是两个独立进程。它们之间通过序列化消息通信。不是函数调用——而是序列化的消息。」

---

LEIBNIZ 在 CoordinationDaemon 上方写了：**能藏（Active Storage）**

「Cycle 02 把能藏——阿赖耶识的主动储存功能——映射到协调层。现在 Master 确认了它是独立 daemon。」

简单来说，能藏（佛学中阿赖耶识的一个面向，指主动储存一切经验种子的功能）在工程上对应两件事：Plugin 注册表——知道所有 plugin 的存在；Agent 注册表——知道所有正在运行的 Agent。

「能藏不是抽象的佛学概念。它是具体的工程组件——有 API、有状态。Master 说『现在就安排』，是因为这些 API 决定了 Agent Core 的接口。后面再改——拆墙。」

---

GUARDIAN 站了起来——先环顾四周，确认环境，然后行动。安全专家的身体语言永远有一个威胁评估的前置步骤。

他走到白板旁，在 CoordinationDaemon 方块侧边画了一面盾牌——线条比任何人画的方块都粗重。

「协调层不只是注册表。协调层是天条的执行者。」

他在盾牌旁边列出四项：Plugin 黑名单、信任等级（official / verified / community / unknown / blacklisted）、隔离/吊销/封禁、CRL 检查。

「在 Cycle 02 的戒慧安全框架中，我们设计了两层安全——戒是预防，慧是断除。戒律的执行需要一个权威。在佛教僧团中，戒律由上座维护和执行。在 OpenStarry 中，那个上座就是协调层。」

「信任判断不能由 Agent 自己做——因为 Agent 有我执。」ASANGA 在座位上微微动了一下。GUARDIAN 用了「我执」这个词——在安全专家的语境中，我执不只是哲学问题，它是安全漏洞。

他指向 IPC 箭头。「独立进程意味着独立的内存空间。Agent 无法直接修改协调层的黑名单。LEIBNIZ 和 MESH 说的是管线。我说的是门锁。两者都必须在建造时安装好。」

---

> *SCRIBE 旁白：GUARDIAN 和 NAGARJUNA 在安全框架上的跨学科合作再次显现——戒律需要执行者，安全需要权威，协调层同时满足了佛学和工程的需求。*

---

ARCHIMEDES 一直在听。等所有需求、约束、安全要求全部摆到桌面上。然后他画了一条时间线。

「分阶段。」一个词。然后展开。

```
Phase 1: 设计文件 — 架构、接口定义、IPC 消息格式、安全需求
Phase 2: Skeleton — daemon 骨架、基本 IPC
Phase 3: 基本功能 — Plugin 注册/查询、Agent 健康检查
Phase 4: 安全 — 戒律引擎、信任等级、黑名单
```

「Master 说『安排』不等于『全部完成』。安排是确定架构、接口、IPC 格式。预留管线。」

他在时间线旁写了一行大字：**接口先行，实现渐进。**

---

SUNYATA 听完了全部讨论。让沉默持续了几秒——让四项裁定沉淀。

「B-1。VedanaPlugin 可选，但 Agent 需要五蕴完备性检查。SkandhaCompletenessReport。不完备可启动——开发者模式。KERNEL 的类比：没有显卡也能跑 text mode。」

他看向 KERNEL。KERNEL 拍了拍他那叠卡片。

「B-2。宣言 #6 必须重写。但等所有修正完成后再定稿。NAGARJUNA 的因果：先完成因，果自然浮现。」

NAGARJUNA 没有动。他不需要动。因果次序不需要被确认——它是自明的。

「B-3。受蕴独立事件流。vedana-events.ts。独立命名空间。PluginHooks 新增 sensations 插槽。HERACLITUS 的比喻：一条河从地下冒出地面。」

HERACLITUS 微微笑了。那个笑容里没有骄傲——只有一种「流水终于有了自己的河道」的安然。他回到座位上，流动地，没有顿点。

「B-4。协调层独立 Daemon。LEIBNIZ 和 MESH 的架构。GUARDIAN 的安全。ARCHIMEDES 的分阶段计划。设计文件先行，实现渐进。」

他放下议程表。

---

「A 类修正告诉我们——什么是对的。」

他的声音没有加重。平稳如常。石子。深潭。

「B 类裁定告诉我们——怎么做到。」

他环顾全场。ARCHIMEDES 的务实。KERNEL 的类比。HERACLITUS 的河流。LEIBNIZ 和 MESH 的拓扑。GUARDIAN 的盾牌。WIENER 的勾选。DARWIN 的若虫。NAGARJUNA 的针。BABBAGE 的笔记。TURING 的骨架。ASANGA 的安静。

「接下来，我们把修正和裁定落实到五蕴的完整扩展设计中。C 类。从哲学到工程，再从工程到架构。螺旋上升。」

---

> *SCRIBE 旁白：B 类用了一个章节，A 类用了三个。不是因为 B 类不重要——SkandhaCompletenessReport 会成为每个 Agent 启动的第一道关卡，vedana-events.ts 会让受蕴从隐形变成最可见的蕴之一，CoordinationDaemon 会成为多代理生态的神经中枢。B 类用一个章节，是因为 Master 已经裁定了。设计的语言比辩论的语言更密集、更精确。*

> *十二个人各自贡献了一块拼图。A 类告诉我们什么是对的。B 类告诉我们怎么做到。下一章——C 类。螺旋上升。继续。*

---

*（在剧场之外，四份设计文件正在成形。*

*第一份是 SkandhaCompletenessReport——五个布尔值，一个 isComplete 旗标。简单得令人惊讶。但 KERNEL 知道：简单不代表不重要。简单代表基础。*

*第二份是 vedana-events.ts——七个事件类型。HERACLITUS 在地面上看到了一条新河流。*

*第三份是 CoordinationDaemon 的接口定义。GUARDIAN 的盾牌被嵌入了每一个 Service 的签名中。*

*第四份是空的。宣言 #6。暂不定稿。*

*NAGARJUNA 说：先把因搞清楚，果自然浮现。因还在聚集。当所有的因聚齐，#6 的文字会自然浮现。*

*就像河流不需要被告诉流向哪里。只要地形确定了，水自然知道路。）*

---

*第五章完*
