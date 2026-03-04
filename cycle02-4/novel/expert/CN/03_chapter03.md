# 第三章：三和合的宁静

---

## I. 最短的辩论

六场辩论中有长有短，有暴风雨有微风。D5 是暴风雨——一百五十分钟，六票反对，GUARDIAN 和 ATHENA 的正面交锋。D1 是急流——九十分钟，九项决议，概念密度最高。D2 是一场类比的竞赛——CPU、观测器、有分心。

D3 是微风。

四十五分钟。五项决议。全部一致通过。零争议。

SUNYATA 事先知道会是这样。在他的辩论准备笔记中，D3 被标注为「可能快速通过」。R1 的八份独立报告和 R2 的八份交叉审阅在触与作意的基本性质上完全一致——触是事件协定，作意是 read-only 快照，触的数学模型是布尔逻辑（root AND object AND consciousness），第一版不判断作意品质。

这就是为什么 D3 在辩论序列调整中被提前到第二场——它的共识度高到可以在 D1 之后直接跑完，为 D4 提供「触的事件模型已确认」的基础。

但「没有争议」不等于「没有深度」。

D3 的深度不在辩论中——在辩论之前。当所有人在 R1 和 R2 中独立到达相同结论的时候，深度就已经完成了。D3 只是确认这个深度的存在。

---

## II. 定义性与附随性

SUNYATA 宣布辩论开始后，先确认了五项既有共识。触的本质。作意的本质。触的数学模型。作意品质的延后。显式建构的选择。

五项。零异议。NAGARJUNA 简短地确认了佛学基础——触是三和合的功能性结果，不是独立实体，更接近协定而非事件。ASANGA 确认了作意——「作意在触的那一刻已经确定了心的朝向。跨心念尺度的品质变化推迟到未来版本是正确的，因为这需要元认知能力。」VITRUVIUS 确认了工程可行性——SparshEvent 目前是纯类型定义，零 runtime 使用，Plan27b 需要在 `processEvent()` 入口处建构它，大约 10-20 行代码。

然后进入第一个待决事项：SparshEvent 应携带哪些字段？

---

TURING 先确认了代码事实。SparshEvent 在 `packages/sdk/src/types/coarising.ts` 中定义。三个字段：`root`（根门）、`object`（外部刺激对象）、`consciousness`（认知领域识别）。没有 `timestamp`，没有 `sessionId`。

他顺带做了一个事实修正——R07 报告在 §4.2 中使用了 `timestamp: t₁` 这个字段。「这是事实错误。SparshEvent 不存在 timestamp 字段。R07 虚构了此字段。」

TURING 的事实修正在 Cycle 02-4 中出现了不止一次。他在 D4 中也修正了一个虚构的 `ISensation.ingestToolResult()` 方法。这些修正很少引起戏剧性的讨论——它们只是被记下来，然后辩论继续。但每一次修正都像是从地基中取出了一块不属于那里的石头。取出后，地基反而更稳了。

---

三个选项摆在桌上。BABBAGE 排成了表格——这是他的本能，他在看到三个以上的选项时会自动产生表格的冲动。

选项 A：维持三字段。语义纯粹，只描述三和合。
选项 B：加入 timestamp。四字段，提供时序排序。
选项 C：加入 timestamp + sessionId。五字段，支持多 Agent 追溯。

NAGARJUNA 的分析很短。触是根、境、识三和合——这是触的定义。时间戳不是触的定义要素。「但在工程脉络中记录『何时发生』是有用的附加信息。从佛学角度，加不加 timestamp 不改变触的本质。这是纯工程决策。」

ASANGA 同意。「在阿毘达磨的时序分析中，『什么时候发生』由心路过程的位置决定，不需要额外的时间标记。但工程系统不是阿毘达磨——它需要外部时钟。佛学对此问题保持中立。」

佛学家们在这里做了一件在六场辩论中反复做的事——明确标记出他们的「管辖范围」。触的三和合定义？佛学有话要说。Timestamp 的有无？佛学保持中立。这种自我限制不是软弱——是精确。它让工程讨论在佛学框架允许的空间里自由展开。

---

转折来自 LINNAEUS。

在二十位学者中，LINNAEUS 不是最常发言的——他的专长是分类学和本体论，只在「这个东西应该被归为什么类别」的问题上才会出手。但当他出手的时候，他的观点往往是决定性的。

「SparshEvent 的三个原始字段是触的**定义性属性**（svabhava-laksana）。timestamp 是**附随性属性**（samprayukta-laksana）。」

他停顿了一下，确保所有人都听到了这两个术语。

「在阿毘达磨分类中，定义性属性和附随性属性有本质区别。把 timestamp 放在 SparshEvent 中，等于把附随属性混入定义。更干净的做法是让 timestamp 留在 CoarisingBundle 层级——Bundle 已经有 timestamp，不需要在 SparshEvent 重复。」

BABBAGE 立刻回应：「但如果需要 SparshEvent 自己的时间戳用于诊断——触到 Bundle 的组装延迟——可以作为 optional 字段。」

他修正了建议：

```typescript
interface SparshEvent {
  readonly root: string;
  readonly object: unknown;
  readonly consciousness: string;
  readonly timestamp?: number;  // optional: 非触的定义要素
}
```

Optional。问号。

NAGARJUNA 认可了这个设计：「`timestamp?: number` 的 optional 在佛学上是最精确的。触的本质是三和合，时间不是触的本质。但在工程脉络中记录何时发生是有用的附加信息。Optional 恰好表达了『非本质但有用』的语义。」

---

LINNAEUS 的「定义性 vs 附随性」区分在 D3 中只占了几分钟的讨论时间。但它的影响远超 D3 本身。

在 D6 中，当 NAGARJUNA 提出 `v_true → v_latent` 的语义修正时，他用的就是同样的框架——`v_true` 暗示存在「客观真实」的效价，这是一个错误的定义性属性。`v_latent`——潜在效价，agent 的内在估计——才是正确的定义。

在 D5 中，当 BABBAGE 分析 IKlesha 的蕴归属时，他用「判别式联合类型不允许 'samjna' & 'vijnana' = never」否决了方案 A——那是同一个类型理论工具在不同语境中的应用。

分类学看起来是静态的——给东西起名字，放进正确的抽屉。但在 D3 中，LINNAEUS 展示了分类学的动态面：一个好的分类框架不只告诉你东西在哪里，它还告诉你**什么不应该在那里**。

**D3-1：SparshEvent 三必填 + timestamp 可选 + 不加 sessionId——9/9。**

---

## III. 一对一

D3-2 的议题更加根本：每个认知 tick 是否只有一个 SparshEvent？

ASANGA 从阿毘达磨的心路过程（citta-vithi）分析。在上座部阿毘达磨中，一个完整的心路过程只处理一个所缘（arammana）。如果在心路进行中另一个感官对象出现，它必须等待当前心路结束。

「映射到工程：一个认知 tick 处理一个触。多个所缘意味着多个心路，也就是多个 tick。」

NAGARJUNA 补充了中观视角：「触是缘起法——它依根、境、识三者而生起。三个特定的因缘聚合产生一个特定的触。不同的因缘聚合产生不同的触——它们不应被混为一个触，就像不同的三角形不能被混为一个三角形。」

HERACLITUS 提出了工程上的边界情况——同一个 `processEvent()` 调用中，LLM 可能返回多个 tool_calls。每次工具执行是否算一个新触？

VITRUVIUS 给出了分阶段的建议：Phase 1 采用严格一对一——每次 `processEvent()` 恰好一个 SparshEvent。工具执行不产生新的触，共享同一个触的脉络。Phase 2 再扩展为一对多，允许工具执行后的「意门自触」（mano-dvara sparsha）。

ASANGA 确认了分阶段的佛学合理性：「Phase 1 的一对一对应六根接触六境的基本模式。Phase 2 的子触对应意门自触——意识以自身的产出为所缘。两者都是合法的认知模式，但复杂度不同。」

KERNEL 补充了操作系统角度——一对一在调度上最简单。一个 SparshEvent，一个 CoarisingBundle，一次完整的五蕴循环。没有并发控制问题，没有 Bundle 合并问题。

**D3-2：Phase 1 严格一对一 + Phase 2 扩展为一对多——9/9。**

---

## IV. 因果的种子

D3-3 的议题是 PENROSE 在交叉审阅中提出的——因果追溯性。

他的问题很具体：如果 Agent 执行了 `rm -rf /important-data/`，事后分析需要回答——是哪个触事件触发了这个认知链？如果 SparshEvent 在 GC 回收后消失，这个问题就无法回答。

三个方案被列出。

方案 α——全量日志。每个 SparshEvent 建构时自动写入持久化日志。完整但笨重。

方案 β——影子记录。在 EventBus 上 emit 结构化的因果事件，由 Sati 或 CausalTracer plugin 消费。精确但需要新增事件类型。

方案 γ——CoarisingBundle 自带触的快照。零额外机制。Bundle 的 `sparsha` 字段就是因果记录。但如果没有消费者持有引用，Bundle 同样被 GC。

NAGARJUNA 的评估带着佛学的精巧：

「方案 α 过度——等于试图留住每一刻的触。触的本质是瞬时的，试图留住一切是一种执着。」

「方案 β 最精准——触本身消灭，但其因果印记留在因果链中。这完全符合唯识学的种子理论：触消灭了，但它在阿赖耶识中留下了种子。」

「方案 γ 也可接受——Bundle 是触的结果状态，而非触本身。」

最终的折中来自 KERNEL。他建议在 Plan27b 的 SparshEvent 建构点 emit 一个 EventBus 事件。目前不需要消费者——但为未来的 CausalTracer 或 SatiMonitor 预留了扩展点。

「成本：一行 `bus.emit()` 调用。效益：完整的扩展性。」

ARCHIMEDES 确认了工程可行性——大约 5 行代码（LOC）。完全在 Plan27b 范围内。

**D3-3：CoarisingBundle 快照 + EventBus 预留扩展点——10/10。**

---

## V. 只有触是必须的

D3-4 回到了一个 DC-8 的裁定——CoarisingBundle 的五遍行为「参考设计」（reference design）。LINNAEUS 再次出手，定义了「参考设计」的精确边界。

他画了一条线。线的上方是 Mandatory——核心必须保证的。线的下方是 Reference——核心提供但不强制的。

Mandatory：SparshEvent 类型定义、CoarisingBundle 类型定义、`createCoarisingBundle()` 工厂函数、SahajaContract 品质约束、`Object.freeze()` 不可变语义。

Reference：四个 Channel——vedana、samjna、cetana、manasikara——全部是 optional。Plugin 未提供时为 `undefined`。

BABBAGE 形式化了这个边界：

```
Mandatory: ∀ bundle: bundle.sparsha ≠ undefined
           ∀ bundle: Object.isFrozen(bundle) = true
           ∀ bundle: bundle.timestamp ∈ Number

Reference: ∀ channel ∈ {vedana, samjna, cetana, manasikara}:
           bundle[channel] ∈ Channel | undefined
```

`sparsha` 是唯一的 mandatory Channel。触是认知启动的前提，没有触就没有认知。其余四个 Channel 是 optional——如果某个蕴的 plugin 尚未加载或不适用，对应的 Channel 可以是 `undefined`。

VITRUVIUS 把这个设计与 B-1 完备性检查联系起来——完备性检查报告哪些蕴有 plugin、哪些没有，但不阻止系统运行。「一个只有触和受蕴但没有想蕴 plugin 的 Agent 仍然可以运行——它能感受但不能辨认。」

ASANGA 在这里说了一句被后来反复引用的话：

「五遍行俱生是佛学理想，工程允许降级。」

他引用了 Master 的精神——「Agent Core 提供让五蕴 plugin 因缘和合组合出想要的应用」。因缘具足则五遍行齐备，因缘不足则有所缺漏，但核心本身不强制。

这与 D1 的 G-0 到 G-4 退化行为表形成了对称。D1 说：没有 IGearArbiter 的 Agent 是 G-1——纯 LLM，出生状态。D3 说：没有完整五蕴 plugin 的 Agent 仍可运行——只是认知能力降低。

两者表达的是同一个原则：**核心是空的。能力来自 plugin。因缘具足时生起，因缘不具足时不显现。**

**D3-4：sparsha-only mandatory + 四 Channel reference + 五遍行俱生允许降级——10/10。**

---

## VI. 作意的扩展点

D3-5 是最后一项——ChannelManasikara 的字段设计。两个核心字段已经在 SDK 中定义：`focus`（注意力焦点）和 `intensity`（注意力强度）。

ASANGA 确认了佛学映射——作意的两个功能：「警心」（cetasa abhoga，唤醒心、使心活跃，对应 intensity）和「引心为业」（manasikara-karman，将心引向特定所缘，对应 focus）。两个字段已覆盖作意的基本功能。如理/非如理的判断——那是元认知层面的事，不应在基本快照中。

BABBAGE 建议加入 `dimensions?` 扩展点，与 ChannelVedana 的组合模式保持一致：

```typescript
interface ChannelManasikara {
  readonly focus: string;
  readonly intensity: number;
  readonly dimensions?: readonly ManasikaraDimension[];
}
```

未来 plugin 可以通过 `dimensions` 扩展作意的描述——例如 `{ name: 'source', value: 'user-input' }` 或 `{ name: 'priority', value: 0.8 }`。

NAGARJUNA 认可：「作意的引心方向不仅仅是朝向何处，还包括为何朝向此处、朝向的持续程度等微细面向。这些在第一版不需要填充，但数据结构预留空间是正确的。」

VITRUVIUS 提出了 Plan27b 的最小实现——`focus` 从 InputEvent.source 或 user message 提取，`intensity` 预设 1.0（focal attention）。大约 10 行代码。

**D3-5：focus + intensity + dimensions? 可选扩展——10/10。**

---

## VII. 四十五分钟

D3 结束了。四十五分钟。五项决议。全部一致。

在六场辩论中，D3 的工程影响最小——大约 50 行代码（LOC），是六场辩论中最少的。没有新接口，没有新的类型层次，没有跨蕴的归属争议。SparshEvent 加一个 optional 的 timestamp。ChannelManasikara 加一个 optional 的 dimensions。CoarisingBundle 的 mandatory/reference 边界被精确定义。

但 D3 的概念影响是深远的。

LINNAEUS 的「定义性 vs 附随性」区分成为了一个反复使用的分类工具——D6 的 `v_true → v_latent` 语义修正、D1 的 Manifest 多值 skandha、D5 的四烦恼构成论，都可以追溯到 D3 中确立的「什么是本质、什么是上下文」这个基本问题。

ASANGA 的「五遍行俱生是佛学理想，工程允许降级」成为了 OpenStarry 佛学映射的一般原则。不是「完美复制佛学理论」，而是「理论提供方向，工程决定程度」。

PENROSE 的因果追溯问题——触的 fire-and-forget 语义与工程上的事后分析需求之间的张力——被优雅地解决了。不是改变触的本质（那是佛学不允许的），而是在触生起的那一刻留下一个扩展点（那是工程的责任）。触消灭了，但种子留下了。

---

SCRIBE 在记录中写道：

> *D3 是六场辩论中唯一可以用「和谐」来形容的一场。不是因为没有分歧——分歧在 R1 和 R2 阶段就已经被解决了。而是因为到了 D3，所有人对触和作意的理解已经收敛到一个足够小的区域，辩论变成了精确的校准而非方向性的争执。*

> *如果 D1 是主题陈述（exposition），D2 是发展部（development），D3 是——*

> *间奏曲（intermezzo）。*

> *交响曲中的间奏曲不是休息。它是调性的转换、情绪的过渡、下一个乐章的准备。D3 确认了触和作意的设计——而触是所有认知事件的起点。D4 的行蕴流向以触为起点。D5 的阈值框架以触带来的受蕴评估为基础。D6 的受蕴工程以触→受的因果链为前提。*

> *D3 的安静不是空洞。D3 的安静是基础的坚固。*

---

SUNYATA 没有在白板上写 D3 的结语。他只是在五项决议下面画了一条线，然后看了看时间。

四十五分钟。他原本预估三十分钟。多出的十五分钟花在了 PENROSE 的因果追溯问题上——那是预料之外的深度。

他看了看辩论日程。D1 已完成。D3 已完成。D4 已完成。明天是 D2——正念架构。后天是 D5——烦恼与安全。最后是 D6——受蕴工程。

三场已过，三场待来。

前三场辩论（D1、D3、D4）在 SUNYATA 的笔记中被标注为「地基」——触的事件模型、齿轮仲裁者的蕴归属、行蕴的流向约束。这些是系统最底层的设计决策，像混凝土一样硬化之后就不再容易修改。

后三场辩论（D2、D5、D6）被标注为「上层建筑」——正念的架构映射、安全与阈值框架、受蕴的工程实现。它们建立在前三场的基础之上，但它们的设计空间更大，争议也更大。

D5 尤其令 SUNYATA 警惕。GUARDIAN 在 D1 中让步了——evaluate() 单方法加上三道外部安全机制。但 SUNYATA 知道 GUARDIAN 的让步不是放弃，而是积蓄。D5 的议题——烦恼、安全、阈值——正好是 GUARDIAN 最核心的关切。

那场辩论会很长。SUNYATA 已经知道了。他看了看 GUARDIAN 的座位。GUARDIAN 正在翻阅他的红色封面安全备忘录，红笔在纸面上画了新的底线——不是删除线，是底线。底线意味着「问题」。

D3 的宁静是暂时的。

但暂时的宁静也有它的价值。就像在暴风雨来临之前，工匠会检查所有的铆钉是否到位——D3 确认了触和作意的铆钉。它们到位了。牢固。

接下来的风暴可以来了。

---

> *SCRIBE 旁白：六场辩论的情绪曲线如下——*

> *D1 = 集中（九项决议，概念密度最高）*
> *D3 = 宁静（五项决议，全场零争议）*
> *D4 = 深沉（行蕴流向、WIENER 的稳定性证明，数学最密集）*
> *D2 = 灵动（类比的竞赛，CPU/观测器/有分心）*
> *D5 = 暴风（一百五十分钟，六票反对，三次僵局）*
> *D6 = 收束（十六项决议，工程味最浓，零反对票）*

> *每一场辩论的情绪都不一样。但如果你把六场辩论排在一起看——*

> *它是一部交响曲。*

> *D1 是第一乐章（Allegro con brio）——快板，有力，主题陈述。*
> *D3 是间奏曲（Intermezzo）——短小，安静，过渡性。*
> *D4 是第二乐章（Adagio）——慢板，深沉，数学最密集。*
> *D2 是第三乐章（Scherzo）——谐谑曲，灵动，类比的游戏。*
> *D5 是第四乐章（Allegro molto）——急板，戏剧性最强，冲突与解决。*
> *D6 是终曲（Finale）——所有动机回归，统一主题再现。*

> *D3 的间奏曲很短。但没有间奏曲的交响曲——*

> *只是噪音。*

---
