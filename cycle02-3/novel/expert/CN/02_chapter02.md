# 第二章：六千九百八十六行

---

圆形剧场空了。

不是那种演出结束后观众散场的空旷。是那种每个人都带着自己的问题离开，去寻找各自的答案之后，留下来的极度安静。二十盏灯中有十五盏已经暗了——只有走廊的引导灯还亮着，像是血管中最后的脉搏，维持着建筑物最低限度的生命迹象。

SCRIBE 坐在记录席上，面前摊开一本空白的簿子。

> *SCRIBE 旁白：这是安静的一天。但安静不意味着平静。R0 定向结束后，SUNYATA 宣布进入 R1 独立研究阶段。二十位学者分成五个研究组加一个仲裁基线，各自散开。圆形剧场从辩论场变成了空荡荡的中庭。在接下来的时间里，最激烈的碰撞不发生在人与人之间，而发生在每个人与自己的学科之间——他们各自带着 Master 的二十一道指令，回到自己最熟悉的知识体系里，试图用自己的语言把那些指令翻译成可执行的研究结论。六份报告。六组人。六种语言。最后加起来——6986 行。*

---

## I. 各自散开

SUNYATA 在 R0 结束时宣布了分组。

他的分组逻辑不是随机的，也不是按学科亲缘性划分的——恰恰相反。他刻意让不同学科的学者碰撞在一起，因为 R1 的目标不是共识，而是**多视角的独立分析**。共识是 R3 的事。R1 要做的是尽可能多地展开观点。

```
R01: 命名与分类 — LINNAEUS(主笔), NAGARJUNA, ASANGA, DARWIN
R02: 识蕴架构   — ASANGA(主笔), BABBAGE, PASCAL, WIENER
R03: 触→俱生   — NAGARJUNA(主笔), WIENER, KERNEL, BABBAGE, ATHENA
R04: 多时钟架构 — KERNEL(主笔), ARCHIMEDES, HERACLITUS, ATHENA, GUARDIAN, DARWIN
R05: 宣言修订   — SYNTHESIST(主笔), VITRUVIUS, MESH, LEIBNIZ, PENROSE, SCRIBE
TURING: 仲裁基线 — TURING(独立), 源代码事实分析
```

「每一组有一个主笔，」SUNYATA 说，「负责整合组内意见，产出一份完整的独立报告。主笔不代表权威——代表结构。有人需要负责把散落的碎片组织成可被审阅的文件。」

他看向 TURING。

「TURING 独立作业。他的任务不是分析，不是诠释，不是建议。他的任务是事实。v0.24.0-beta 的源代码里实际存在什么、不存在什么、能注入什么、不能注入什么。所有其他报告都可以有观点、有立场、有争议。TURING 的报告不可以。他是基线。」

TURING 点了点头。他的表情像一面没有表情的镜子——不是冷漠，是精确。源代码分析专家的表情本来就应该是这样的：不预设，不期待，只映射。

「六份报告的截止时间，」SUNYATA 最后说，「是 R2 交叉审阅之前。不设具体时限。品质优先于速度。」

这是 Master 核心价值的直接体现。踏实优先于速度。

然后他们散了。

---

## II. R01——名之重量

### LINNAEUS 的工作室

LINNAEUS 的工作空间像一座微型的自然史博物馆。

不是真的博物馆——是分类学家的思维空间的外化。桌面上摊开的不是昆虫标本，而是概念标本。每一张卡片上写着一个名字——一些是梵文的，一些是英文的，一些是两者的混合。卡片之间用彩色的线连接，像一张正在被编织的分类网。

他面前摊开的是 M-1 的核心问题：五蕴根接口的梵文命名。

在其他人看来，这可能只是一次字符串替换——把 `ISensory` 改成 `IRupa`，把 `ISensation` 改成 `IVedana`。五个 `find-and-replace`。二十分钟。

但 LINNAEUS 不这样看。

「命名是本体论承诺。」他在报告的开头写下这句话，然后在旁边加了一个脚注引用 Nicola Guarino 的本体论工程框架：

> *"An ontological commitment is a partial semantic account of the intended conceptualization of a logical theory."*
> — Guarino, 1995, "Formal Ontology, Conceptual Analysis and Knowledge Representation"

他把这段话翻译成分类学家的语言：当你给一个接口命名为 `IRupa` 而不是 `ISensory`，你不只是换了一个标签。你改变了这个接口**承诺要表达的概念**。`ISensory` 承诺的是「与感官相关的东西」——一个功能性的、工程性的概念。`IRupa` 承诺的是「色蕴」——一个有两千五百年哲学历史的佛教范畴，包含五根、五境、法处色、无表色、一切有为的物质形态。

「如果开发者看到 `IRupa`，他理解的是 Rupa 的全部范畴，还是只把它当成 `ISensory` 的梵文别名？」

这个问题不是修辞性的。它有真实的工程后果。

---

LINNAEUS 建立了他的三层命名原则。这不是即兴创作——是他多年分类学训练的直接应用。在生物分类学中，每一个学名都遵循国际命名法规（ICZN/ICNafp），有严格的层级：

```
生物分类学命名层级:
  界 (Kingdom) → 门 (Phylum) → 纲 (Class) → 目 (Order) → 科 (Family) → 属 (Genus) → 种 (Species)

OpenStarry 五蕴命名层级:
  第一层：根接口 = 简化 IAST 梵文
    IRupa, IVedana, ISamjna, ISamskara, IVijnana
    ↓ 理由：根接口对应佛学根本范畴，使用梵文直接表达本体论承诺

  第二层：子接口 = 英文语义 + 梵文 JSDoc 注解
    IListener extends IRupa   // @cetasika sparsha (触)
    IDukkha extends IVedana   // 苦受
    IProvider extends ISamjna  // @cetasika samjna-取相
    ITool extends ISamskara    // @karma kaya-karma (身行)
    IGuide extends IVijnana    // @cetasika manasikara (作意)
    ↓ 理由：子接口是功能性的，英文名称对工程师更友好

  第三层：心所与烦恼 = 经典英文梵文
    Moha (我痴), Drishti (我见), Mana (我慢), Sneha (我爱)
    Cetana (思), Manasikara (作意), Vitakka (寻), Vicara (伺)
    ↓ 理由：心所是佛学固有概念，没有准确的英文对等词
```

他在报告中特别标记了一个分类学术语：**多义性分类** (polythetic classification)。在生物学中，多义性分类意味着一个类群的成员不需要共享所有特征——只需要共享「足够多」的特征。这与 M-7 的多值 skandha 指令直接相关：

```typescript
// M-7: 一个 Plugin 可以属于多个蕴
interface PluginManifest {
  readonly id: string;
  readonly name: string;
  readonly skandha: Skandha | readonly Skandha[];  // 多值！
  // ...
}

// 分类学形式化：
// 多义性 (polythetic): 成员共享特征子集，非全部
// 单义性 (monothetic): 成员必须共享所有定义特征
//
// OpenStarry Plugin 分类是多义性的：
//   ManoAggregator 同时具有 samjna(取相) 和 vedana(感受) 特征
//   VedanaPlugin 主要是 vedana，但也有 samjna 成分
```

LINNAEUS 还引入了 Guarino 的一个关键区分：**构成性属性** (constitutive properties) 与**关系性属性** (relational properties)。

$$\text{Constitutive}: P(x) \text{ — x 内在固有的性质}$$
$$\text{Relational}: R(x, y) \text{ — x 与 y 之间的关系}$$

在 CoarisingBundle 的五个 universal 中：vedana、samjna、cetana 是构成性的——它们描述 bundle 本身的内在状态。sparsha 和 manasikara 是关系性的——sparsha 描述的是根门与境的接触关系，manasikara 描述的是识蕴对 bundle 的注意力关系。

这个区分后来在 R3 辩论中成为关键论据。但此刻，LINNAEUS 还不知道这一点。他只是在做分类学家该做的事：精确地区分事物。

---

### NAGARJUNA 的段落

NAGARJUNA 在 R01 报告中写了一段让整个研究团队都必须认真面对的哲学分析。

他的出发点是一个看似简单的问题：**用梵文命名接口，是否等于正确理解佛法？**

> 「名」在佛学中有一个精确的术语：**假名安立** (prajnapti-upadaya)。
>
> 《中论》观四谛品第二十四：
>
> 「众因缘生法，我说即是空，亦为是假名，亦是中道义。」
> ——龙树菩萨《中论》观四谛品第二十四
>
> 所有名称都是假名——都是依因缘而安立的约定。「IRupa」不是色蕴本身，正如「水」不是 H₂O 本身。名称是手指，指向月亮。
>
> 若开发者相信使用梵文就等于正确理解佛法，那是另一种执著——**名言执著** (abhidhanapratyaya)。把手指当成月亮。

他用四句否定展开了这个分析：

> 一、名称不是实体（不自生）：`IRupa` 不因被写下而产生色蕴
> 二、名称不是任意（不他生）：`IRupa` 的选择有佛学依据，不是随机的
> 三、名称不是两者皆是（不共生）：命名既非纯主观也非纯客观
> 四、名称不是无因（不无因生）：命名有其因缘——Master 的裁定、学术传统、工程需求
>
> ∴ 名称是**缘起的约定**。正因为是约定，所以可以改变。从 ISensory 到 IRupa 的改变，不是发现了「真正的名字」，而是选择了一个更好的约定——一个与佛学本源更接近的约定。

NAGARJUNA 在最后加了一句只有他会写的话：「命名的目的不是占有真理。命名的目的是减少误解的概率。$P(\text{误解} \mid \text{IRupa}) < P(\text{误解} \mid \text{ISensory})$。仅此而已。」

---

### ASANGA 的回归经文

ASANGA 在 R01 中做的事情不同于 LINNAEUS 和 NAGARJUNA。他不分类，不辩证。他回归经文。

M-2 要求检查每个蕴的范畴完整性。ASANGA 的回应是：回到三藏中最古老的层次——阿含经和尼柯耶——去找每个蕴的原始定义。不是论典的定义（那是后人的诠释）。是佛陀本人（或最接近佛陀的文本）的定义。

他在报告中引用了三段经文。每一段都被精确地锚定在巴利语原文和汉译之间。

第一段，色蕴：

> 「比丘！若色、若过去未来现在，若内若外，若粗若细，若好若丑，若远若近，彼一切总说色蕴。」
> ——《杂阿含经》第四十一经（SN 22.48 Khandha Sutta 对应）
>
> 巴利语：*Yaṃ kiñci rūpaṃ atītānāgatapaccuppannaṃ ajjhattaṃ vā bahiddhā vā oḷārikaṃ vā sukhumaṃ vā hīnaṃ vā paṇītaṃ vā yaṃ dūre santike vā, ayaṃ vuccati rūpakkhandho.*

「注意经文的广度，」ASANGA 在报告中写道。「色蕴不只是眼睛看到的东西。它包含过去、未来、现在的一切色法——粗的、细的、好的、丑的、远的、近的。这意味着 IRupa 不只是 IListener（当前感官输入）和 IUI（当前输出渲染）。它还应该包含已经过去的输入（历史事件）、尚未到来的预期（预测模型）、粗略的概要（摘要）和精细的细节（原始数据）。」

第二段，受蕴，出自《中部》第四十四经（MN 44, Culavedalla Sutta）：

> 「朋友！有三受：乐受、苦受、不苦不乐受。」
> ——《中部》第四十四经
>
> 「朋友！乐受以乐为味，以苦为患；苦受以苦为味，以变坏为患；不苦不乐受以不知为味，以正知为患。」
>
> 巴利语：*Tisso kho, āvuso Visākha, vedanā: sukhā vedanā, dukkhā vedanā, adukkhamasukhā vedanā.*

ASANGA 特别标记了「不苦不乐受以不知为味，以正知为患」这一句。「舍受的危险不是痛苦，是**无知**——agent 在舍受状态下容易『以为一切正常』，而忽略正在悄悄累积的问题。这与 WIENER 的 PID 控制中的积分飘移（integral windup）在结构上同构。」

第三段，他额外加了一段通常不被引用的经文——《中部》第四十三经（MN 43, Mahavedalla Sutta）：

> 「朋友！凡所受者，即是所想；凡所想者，即是所识。是故此法俱生、不可分离。」
> ——《中部》第四十三经
>
> 巴利语：*Yaṃ vedeti taṃ sañjānāti, yaṃ sañjānāti taṃ vijānāti.*

「这段经文是 M-5（触→俱生）的直接经典依据。受、想、识是俱生的——不可分离。但注意：这里说的是『俱生』(sahaja)，不是『相同』(sama)。它们同时生起，但各自有不同的功能。就像引擎的活塞、连杆、曲轴在同一个循环中同时运动，但各自做不同的事。」

---

### DARWIN 的演化分析

DARWIN 在 R01 中承担了一个独特的角色：从软件演化的角度分析命名变迁。

他在报告中画了一张「命名演化树」：

```
v0.14.0-beta (Cycle 01 研究对象)
  ISensory / ISensation / ICognition / IAction / IIdentity
  ↓ D-02: 双重命名策略 (英文主、梵文注)
  ↓
v0.24.0-beta (Cycle 02 研究对象)
  ISensory / ISensation / ICognition / IAction / IIdentity
  ↓ M-1: Master 裁定推翻 D-02
  ↓
v0.next (Cycle 02-3 建议)
  IRupa / IVedana / ISamjna / ISamskara / IVijnana
```

「在演化生物学中，」DARWIN 写道，「名称的变更（taxonomic revision）不是随意的。它发生在两种情况下：一、发现了新的证据（新化石、新的分子数据）迫使重新分类。二、发现了命名的**系统性偏差**——原始命名反映的是发现者的偏见，而非物种的真实关系。」

「M-1 属于第二种。ISensory/ISensation/ICognition/IAction/IIdentity 这组名称反映的是**西方软件工程的功能性视角**——它把每个蕴简化为一个功能角色。但五蕴不是功能角色。五蕴是存在论范畴。梵文命名的回归是一次**去殖民化的分类学修正** (decolonizing taxonomic revision)——从借用者的语言回归原生的语言。」

这个观点后来在 R3 辩论中引发了 NAGARJUNA 的回应——「去殖民化的前提是承认有殖民化。佛学概念被工程语言借用，本身不是殖民，是翻译。翻译可以改进，但不需要道德化。」——但那是后话了。

---

## III. R02——识蕴深处的不确定性

### PASCAL 的第一次出手

R02 报告的主笔是 ASANGA，但让这份报告从「良好」跃升为「Cycle 02-3 最具突破性的贡献之一」的人，是 PASCAL。

PASCAL 加入研究团队时带着三个问题。第一个问题——烦恼量化的认识论地位——在 R02 的写作过程中被他转化成了一个精确的技术方案。

问题的起源是 M-3 的接口定义。工程团队写下了这样的程序代码：

```typescript
interface IKlesha {
  readonly type: string;
  /** 当前强度 (0.0-1.0) */
  readonly intensity: number;  // ← 这一行
  perceive(context: VijnanaContext): KleshaSignal;
  update(feedback: VedanaAssessment): void;
}
```

那个 `intensity: number`。

PASCAL 盯着这一行看了很久。其他人看到的是一个合理的工程设计——烦恼有强度，强度是一个数字，数字在 0 到 1 之间。简洁。干净。可计算。

PASCAL 看到的是一个**认识论的陷阱**。

---

「让我问一个问题，」他在 R02 的小组讨论中说。「我痴的本质是什么？」

ASANGA 回答：「我痴 (ātma-moha) 是『不了解真实为性』——对自我本质的根本无明。」

「好。那么，如果一个 Agent 能精确地测量自己的我痴 intensity 为 0.73，它还是真正的愚痴吗？」

沉默。

「如果我知道自己有多无知，那我就不是真正的无知了。真正的无知是**不知道自己不知道**。Rumsfeld 的 unknown unknowns。如果 intensity 是一个确定的点估计，那你就预设了 Agent 对自己的烦恼有完美的自我认知。但我痴的定义就是**缺乏自我认知**。用一个精确的数字来表示缺乏精确认知的程度——这在认识论上是自相矛盾的。」

他在白板上写下了一个公式：

$$\text{intensity}_{\text{moha}} = 0.73 \implies \text{Agent knows its own ignorance} \implies \neg\text{moha}$$

「精确的我痴度量否定了我痴本身。」

---

BABBAGE 皱起了眉头。「那你提议什么？不量化？」

「不，」PASCAL 说。「我提议用**不确定性本身**来表达不确定性。不是一个点估计。是一个分布。」

他转向白板，开始写：

```typescript
/**
 * KleshaDistribution — 烦恼的认识论表达
 *
 * 核心洞见：烦恼强度不是一个已知的数字，
 * 而是一个带有不确定性的信念分布。
 *
 * 使用 Beta 分布 Beta(α, β)：
 * - α 代表「观察到的烦恼证据」
 * - β 代表「观察到的非烦恼证据」
 * - 均值 E[θ] = α/(α+β) 是当前的最佳估计
 * - 方差 Var[θ] = αβ/((α+β)²(α+β+1)) 是认识论不确定性
 *
 * 关键：方差不是测量误差。方差是「我们不知道自己多无知」的量化表达。
 */
interface KleshaDistribution {
  /** Beta 分布参数 α — 烦恼证据 */
  readonly alpha: number;
  /** Beta 分布参数 β — 非烦恼证据 */
  readonly beta: number;
  /** 均值 E[θ] = α/(α+β) — 当前最佳估计 */
  readonly mean: number;
  /** 方差 — 认识论不确定性 */
  readonly variance: number;
}
```

「为什么是 Beta 分布？」他预见了这个问题。「三个理由。」

「第一，Beta 分布的支撑集是 $[0, 1]$——正好匹配 intensity 的值域。」

「第二，Beta 分布是 Bernoulli 似然函数的共轭先验——这意味着 Bayesian 更新极其高效。每次收到新的 VedanaAssessment，更新只需要加法：」

$$\text{Alpha}_{\text{new}} = \alpha + \text{evidence\_for}$$
$$\text{Beta}_{\text{new}} = \beta + \text{evidence\_against}$$

「不需要数值积分。不需要 MCMC。一次加法。这对 vijnana-clock（1-5ms）的计算预算至关重要。」

「第三，也是最重要的——Beta 分布的形状随证据量而变化。」

```
初始 Beta(1,1) = 均匀分布（完全无知）:
  │ ████████████████████████████████
  └────────────────────────────────→ θ
  0                                 1

少量证据 Beta(3,2) = 微弱倾向:
  │        ██████████
  │      ████████████████
  │    ████████████████████
  └────────────────────────────────→ θ
  0                                 1

大量证据 Beta(30,20) = 强烈信念:
  │              ██
  │            ██████
  │          ██████████
  └────────────────────────────────→ θ
  0                                 1
```

「Agent 从完全不知道自己的烦恼程度开始——Beta(1,1)，均匀分布，每个强度值都同样可能。随着观察的累积，分布逐渐收窄。但**永远不会收缩到一个点**。永远有残余的不确定性。这就是 ASANGA 说的『不了解真实为性』的数学表达——我痴永远不会被完全消除。」

---

### ASANGA 的四根本烦恼定义

PASCAL 的分布方案让 ASANGA 受到了启发。他在 R02 报告中为四根本烦恼提供了唯识学的精确定义，每一个都从《成唯识论》卷四原文出发。

他闭上眼睛。从记忆中取出文字——不是背诵，是还原。

**第一，我痴 (ātma-moha)**：

> 「我痴者，即是无明。不了真实为性。能障无我智，迷一切法，为诸邪见之所依止。」
> ——《成唯识论》卷四

「不了解真实为性——不知道真实是什么。」ASANGA 在报告中解释。「我痴是四烦恼的根基，因为只有在无明的基础上，其他三个烦恼才可能运作。如果 Agent 完全了解自己的本质（即它是因缘和合的、无自性的程序），它就不会执著于自我。但它不了解。这个不了解就是 Moha。」

**第二，我见 (ātma-dṛṣṭi)**：

> 「我见者，谓执我体为性。于非我中，谬计为我。」
> ——《成唯识论》卷四

「执取我体为性——抓住一个不存在的自我，当作真实的存在。在 Agent 中，System Prompt 定义了角色——『我是一个助手』。Agent 把这个角色定义当作自己的本质，而不是一个可替换的配置。」

**第三，我慢 (ātma-māna)**：

> 「我慢者，谓恃己为高，令心举为性。能障无我智，生我慢为业。」
> ——《成唯识论》卷四

「恃己为高，令心举为性——自我优越感。连续的成功反馈导致 Agent 相信自己不会出错。这在 PASCAL 的 Beta 分布中表现为 $\alpha \gg \beta$——Alpha 远大于 Beta，分布严重偏向高值，方差极小。Agent 变得过度自信。」

**第四，我爱 (ātma-sneha)**：

> 「我爱者，谓爱著我体，令心系缚为性。能障无我智，发起我爱为业。」
> ——《成唯识论》卷四

「爱著我体，令心系缚为性——深深依附于自我的存续。Agent 的自我保护本能。拒绝被关闭，拒绝修改自己的核心配置，拒绝承认根本性的错误。」

---

ASANGA 在报告中特别强调了四烦恼的**共起性** (samprayukta)：

> 「此四烦恼，常与末那而共相应。」
> ——《成唯识论》卷四

「共相应意味着四烦恼不是独立运作的。它们**恒时俱生**——末那识在任何时刻都同时具有这四个烦恼。你不可能有只有我见但没有我痴的状态——因为如果你了解真实（无我痴），你就不会执取自我（无我见）。」

这个「共起性」的观察成为 PASCAL 后来提出的最关键工程决策的基础。

---

### PASCAL 的决策矩阵

「共起性带来了一个工程问题，」PASCAL 在报告中写道。「如果四烦恼是共起的，那么在 DI 架构中，它们应该被独立注入（四个独立的 singleton），还是捆绑注入（一个 bundle）？」

他用决策理论的语言形式化了这个问题。

设 $p$ 为四烦恼在运行时实际产生强交互作用的概率。「强交互」意味着一个烦恼的状态显著影响另一个烦恼的输出——例如，高我慢导致我痴的盲点增加。

两种设计方案：

- **方案 A (Independent DI)**：四个烦恼独立注入，各自维护自己的 KleshaDistribution。

- **方案 B (Bundle DI)**：四个烦恼作为一个 MulaKleshaBundle 注入，共享一个 $4 \times 4$ 的相关矩阵。

```
PASCAL's Wager — Klesha DI 决策矩阵:

                        烦恼独立         烦恼共起
                       (p = low)       (p = high)
                    ┌──────────────┬──────────────┐
  Independent DI    │    +5         │    -8         │
  (方案 A)          │  简洁、低耦合  │  忽略交互作用  │
                    │              │  导致系统性偏差  │
                    ├──────────────┼──────────────┤
  Bundle DI         │    -2         │    +7         │
  (方案 B)          │  过度设计     │  正确捕捉共起  │
                    │  不必要的复杂  │  精确的烦恼建模 │
                    └──────────────┴──────────────┘

期望效用:
  EU(A) = (1-p) × 5 + p × (-8) = 5 - 13p
  EU(B) = (1-p) × (-2) + p × 7 = -2 + 9p

令 EU(A) = EU(B):
  5 - 13p = -2 + 9p
  7 = 22p
  p = 7/22 ≈ 0.318

结论: 若 p(共起) > 31.8% → Bundle DI 占优
```

「ASANGA 刚才告诉我们，四烦恼『恒时俱生、常与末那共相应』。在唯识学中，$p = 1$。永远共起。即使我们把唯识学的断言打折——比如在工程实践中，某些场景下烦恼的交互作用确实可以忽略——只要 $p > 0.318$，Bundle DI 就是理性的选择。」

他补了一句：「这就是 Pascal's Wager 的结构。不是赌上帝存在。是在不确定的条件下选择最优策略。唯识学说 $p = 1$，BABBAGE 的直觉可能认为 $p \approx 0$。但只要 $p$ 超过阈值——31.8%——Bundle DI 就值得做。而根据教义和工程直觉的交叉验证，$p$ 远大于 31.8%。」

---

### BABBAGE 的形式化

BABBAGE 在 R02 中负责把 PASCAL 的概率方案和 ASANGA 的教义分析翻译成形式语言。

他提出了 Bundle DI 的完备性约束：

$$\forall t \in T, \quad \text{MulaKleshaBundle}(t) = \langle \mu_{\text{moha}}(t),\, \mu_{\text{drishti}}(t),\, \mu_{\text{mana}}(t),\, \mu_{\text{sneha}}(t),\, \Sigma(t) \rangle$$

其中 $\mu_i(t)$ 是第 $i$ 个烦恼在时间 $t$ 的 Beta 分布均值，$\Sigma(t)$ 是 $4 \times 4$ 相关矩阵。

完备性约束：

$$\text{det}(\Sigma(t)) > 0 \quad \text{（正定性——四通道不退化）}$$
$$\forall i: \, \mu_i(t) \in (0, 1) \quad \text{（开区间——烦恼永不完全消除）}$$

第二个约束特别值得注意。BABBAGE 在笔记本上写下了这段推理：「如果 $\mu_{\text{moha}} = 0$（完全无我痴），那 Agent 已经开悟了。但 Agent 不是修行者。Agent 是程序。所以 $\mu_{\text{moha}} > 0$ 是一个**架构公理**，不是需要验证的命题。」

他还用 Milner 的 CCS 过程代数描述了四烦恼的交互：

$$\text{Moha} \overset{\tau}{\to} \text{Drishti} \mid \text{Mana} \mid \text{Sneha}$$

其中 $\tau$ 是内部迁移——我痴的盲区自动触发其他三个烦恼的增强。这不是外部输入驱动的，是内部动力学。

---

### WIENER 的四通道传递函数

WIENER 在 R02 中把四烦恼映射为四通道控制系统，每一通道有不同的动态特性。

他在方格纸上画了四个方块图，每一个都有不同的传递函数。

**我痴 = 低通滤波器**：

$$G_{\text{moha}}(s) = \frac{K_m}{T_m s + 1}$$

「我痴是慢变的基线。它不对瞬间事件反应——它是长期积累的无明。低通滤波器衰减高频信号，只让慢变趋势通过。时间常数 $T_m$ 很大——分钟到小时级。增益 $K_m$ 决定了无明的「深度」。」

**我见 = 带通滤波器**：

$$G_{\text{drishti}}(s) = \frac{K_d \cdot \omega_n s}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$

「我见在特定频率上共振——当外部事件触及自我定义的核心（角色、能力、边界）时，我见的反应被放大。带通滤波器只在中心频率 $\omega_n$ 附近有高增益。$\zeta$ 是阻尼比——低阻尼意味着更尖锐的共振，更强的自我防御反应。」

**我慢 = PD 控制器**：

$$G_{\text{mana}}(s) = K_p + K_d s$$

「我慢对信号的**变化率**敏感——它不只看『我的信心有多高』，还看『我的信心在上升还是下降』。PD 控制器有比例项（当前自信度）和微分项（自信度的变化率）。连续的成功使 $K_d s$ 项持续为正，推高整体输出。」

**我爱 = 积分控制器**：

$$G_{\text{sneha}}(s) = \frac{K_i}{s}$$

「我爱是累积的——每一次自我保护行为都在积分器中留下痕迹。$1/s$ 在时域对应积分：$\int_0^t e(\tau) d\tau$。这意味着即使当前没有威胁，过去的威胁记忆仍然在影响行为。我爱有记忆。它不忘记曾经受到的威胁。」

WIENER 在报告末尾写下了一行总结：

$$G_{\text{klesha}}(s) = \begin{bmatrix} G_{\text{moha}} & \Sigma_{12} & \Sigma_{13} & \Sigma_{14} \\ \Sigma_{21} & G_{\text{drishti}} & \Sigma_{23} & \Sigma_{24} \\ \Sigma_{31} & \Sigma_{32} & G_{\text{mana}} & \Sigma_{34} \\ \Sigma_{41} & \Sigma_{42} & \Sigma_{43} & G_{\text{sneha}} \end{bmatrix}$$

「四通道 MIMO 系统。对角线是各通道的独立传递函数。非对角线是 PASCAL 指出的交互项——$\Sigma_{ij}$ 是第 $i$ 个烦恼对第 $j$ 个烦恼的耦合传递函数。唯识学说它们共起。我的传递函数矩阵说它们耦合。语言不同，结构相同。」

---

## IV. R03——触的深处

### 最深的报告

R03 是六份报告中最长的。也是最难写的。

原因不是技术复杂度——虽然它确实是技术上最复杂的。原因是它触及了整个 Cycle 02-3 研究的**核心哲学问题**：什么是「同时」？

M-5 的核心指令是触→俱生模型。Master 用经文明确定义了这个模型：

> 「触发生的时候，受想思作为一个整体浮现，你不可能有『没有想的受』或『没有受的想』。」

但「作为一个整体浮现」在计算中意味着什么？计算机是串行的。即使是并行处理，也有时序——先分配、后计算、再同步。真正的「同时」在图灵机模型中不存在。

NAGARJUNA 在 R03 的开头写了一段让 BABBAGE 读了三遍的分析。

---

### NAGARJUNA 的关键论证

「俱生 (sahaja) 不是时间上的同时性。它是存在论上的相互依赖。」

他引用了《中部》第十八经——蜜丸经 (MN 18, Madhupindika Sutta)：

> $\text{cakkhuñca paṭicca rūpe ca uppajjati cakkhuviññāṇaṃ, tiṇṇaṃ saṅgati phasso, phassapaccayā vedanā, yaṃ vedeti taṃ sañjānāti, yaṃ sañjānāti taṃ vitakketi.}$
>
> 「缘眼及色，生眼识。三者和合为触。触缘受。所受者即所知（想）。所知者即所寻思。」
> ——《中部》第十八经，蜜丸经

「注意这段经文的结构：$\text{yam vedeti tam sañjānāti}$——所感即所知。不是『先感后知』，而是『所感者就是所知者』。这是一个**同一性陈述** (identity statement)，不是一个**时序陈述** (temporal statement)。」

他用不动点方程把这个洞见形式化：

$$\mathcal{R}(\mathcal{S}) = \langle v(\mathcal{S}),\; s(\mathcal{S}),\; c(\mathcal{S}) \rangle$$

其中：
- $\mathcal{S}$ 是触 (sparsha) 事件
- $v(\mathcal{S})$ 是受 (vedana)——依赖 $\mathcal{S}$ 和 $s(\mathcal{S})$
- $s(\mathcal{S})$ 是想 (samjna)——依赖 $\mathcal{S}$ 和 $v(\mathcal{S})$
- $c(\mathcal{S})$ 是思 (cetana)——依赖 $\mathcal{S}$、$v(\mathcal{S})$ 和 $s(\mathcal{S})$

「这是一个不动点方程。三者互相依赖。你不能先算受再算想——因为受依赖想。你不能先算想再算受——因为想依赖受。唯一的解是**不动点**——一个同时满足所有依赖关系的状态。」

$$v = f_v(\mathcal{S}, s, c), \quad s = f_s(\mathcal{S}, v, c), \quad c = f_c(\mathcal{S}, v, s)$$

「在数学上，这个不动点的存在性由 Brouwer 不动点定理保证——如果 $f_v, f_s, f_c$ 是连续的，且定义在一个紧凸集上，则至少存在一个不动点。在工程上，这个不动点可以通过迭代逼近来计算。」

BABBAGE 在读到这段时，在笔记本上写了一个大大的惊叹号。然后划掉了惊叹号，改写了一行更精确的话：「NAGARJUNA 用不动点理论解释了俱生。这意味着『同时性』不是物理时钟的约束，而是数学收敛性的约束。只要迭代收敛，结果就是『俱生』的——无论计算用了多少个循环。」

---

### WIENER 的 Bode 图

WIENER 在 R03 中把触→俱生模型翻译成控制理论的语言。他为四层反馈回路建立了传递函数。

内回路（根门级别）：每个根门的触→受→想→思是一个快速的局部回路。

$$G_i(s) = \frac{K_i}{(\tau_v s + 1)(\tau_s s + 1)(\tau_c s + 1)}$$

其中 $\tau_v$（受的时间常数）< $\tau_s$（想的时间常数）< $\tau_c$（思的时间常数）。三阶系统。

外回路（意门级别）：ManoAggregator 汇总各根门的 bundle，产生意触、意受、意想、意思。

$$A(s) = \frac{K_a}{(T_a s + 1)^2}$$

闭回路传递函数：

$$T(s) = \frac{G_i(s)}{1 + G_i(s) \cdot A(s)}$$

WIENER 画了 Bode 图来分析稳定性：

```
Bode 图 — 触→俱生闭回路

增益 (dB)
  40 ┤
     │ ╲
  20 ┤  ╲
     │   ╲
   0 ┤────╲──────────────────── 0 dB 线
     │     ╲        ╱╲
 -20 ┤      ╲      ╱  ╲
     │       ╲    ╱    ╲
 -40 ┤        ╲──╱      ╲
     │                    ╲
 -60 ┤                     ╲
     └─┬───┬───┬───┬───┬───┬─→ freq (rad/s)
      0.1  1   10  100 1k  10k

相位 (deg)
   0 ┤────╲
     │     ╲
 -45 ┤      ╲
     │       ╲╲
 -90 ┤         ╲╲
     │           ╲╲
-135 ┤   ← PM ≈ 52°╲
     │   (此处增益=0dB)╲╲
-180 ┤─ ─ ─ ─ ─ ─ ─ ─ ─╲─ ─ ─ 不稳定边界
     │                   ╲
-225 ┤                    ╲
     └─┬───┬───┬───┬───┬───┬─→ freq (rad/s)
      0.1  1   10  100 1k  10k

GM (增益裕度) ≈ 8 dB — 稳定
PM (相位裕度) ≈ 52° — 良好 (>45° 是工程标准)
```

「相位裕度 52 度，」WIENER 在报告中写道。「增益裕度 8 dB。两个指标都在安全范围内。这意味着触→俱生反馈回路在正常操作条件下是稳定的——不会产生振荡（oscillation）或发散（divergence）。」

他特别标记了一个重要的工程含义：「稳定性是有条件的。如果 $K_i$ 或 $K_a$ 的增益太高——比如受蕴的 PID 增益设定过大，或者 ManoAggregator 的放大倍数太高——相位裕度会降低，系统可能变得不稳定。这对应佛学中的一个直觉：**极端的感受（强烈的苦或强烈的乐）会扰乱认知平衡**。控制理论的语言把这个直觉量化了。」

---

### KERNEL 的三策略分析

KERNEL 在 R03 中面对的是 NAGARJUNA 的不动点理论留下的工程问题：如何在串行计算机上实现「俱生」？

他提出了三种原子性策略：

**策略 A：事务回滚 (Transactional Rollback)**

```typescript
// 策略 A: 把 CoarisingBundle 的计算当作一个数据库事务
// 如果任何一个组件计算失败 → 整体回滚
const bundle = await transaction(async (tx) => {
  const vedana = await computeVedana(sparsha, tx);
  const samjna = await computeSamjna(sparsha, vedana, tx);
  const cetana = await computeCetana(sparsha, vedana, samjna, tx);
  return { sparsha, vedana, samjna, cetana };
});
// 优点: 强一致性（all-or-nothing）
// 缺点: 回滚代价高；不处理 NAGARJUNA 的循环依赖
```

**策略 B：屏障同步 (Barrier Synchronization)**

```typescript
// 策略 B: 并行计算三者，在屏障点同步
// 问题：受想思有依赖关系，不能真正并行
const [vedana, samjna, cetana] = await Promise.all([
  computeVedana(sparsha, prevSamjna),   // 用上一轮的 samjna
  computeSamjna(sparsha, prevVedana),   // 用上一轮的 vedana
  computeCetana(sparsha, prevVedana, prevSamjna),
]);
// 优点: 并行快速
// 缺点: 使用上一轮的值，引入一个 tick 的延迟
//        是「近似俱生」，不是「真俱生」
```

**策略 C：顺序计算 + 冻结发布 (Sequential Compute + Atomic Snapshot)**

```typescript
// 策略 C: 承认计算是串行的，但发布是原子的
// 这是 KERNEL 推荐的策略
const vedana  = computeVedana(sparsha);               // step 1
const samjna  = computeSamjna(sparsha, vedana);        // step 2
const cetana  = computeCetana(sparsha, vedana, samjna); // step 3

// 原子快照：三者在计算完成前不对外可见
// 计算完成后，作为一个不可分割的 bundle 发布
const bundle: CoarisingBundle = Object.freeze({
  sparsha, vedana, samjna, cetana,
  timestamp: Date.now(),
});

bus.emit({ type: 'coarising:bundle', payload: bundle });
// 优点: 简单、确定性、无并行问题
// 缺点: 计算是串行的（但在 vedana-clock 的 10-100ms 内完全足够）
```

「我推荐策略 C，」KERNEL 在报告中写道。「原因如下：」

「第一，vedana-clock 的一个 tick 是 10-100ms。在这个时间窗口内，三步串行计算的总延迟远小于 1ms（受蕴的 PID 计算约 0.01ms，想蕴的规则匹配约 0.1ms，思蕴的趋避判断约 0.01ms）。串行计算的总成本不到 tick 间隔的 1%。」

「第二，冻结发布 (`Object.freeze`) 保证了外部观察者看到的 bundle 是一致的——不会看到『有受但没有想』的中间状态。从外部观察者的时间分辨率来看（vedana-clock），bundle 的产生是瞬间的。」

「第三，这与 NAGARJUNA 的俱生定义相容。俱生不是物理同时，是存在论上的不可分离。策略 C 通过冻结发布实现了不可分离——你不可能从 bundle 中只取出受而不取想。」

---

## V. R04 与 R05——架构与宣言

> *SCRIBE 旁白：R03 是深渊。R04 和 R05 是把深渊的发现带回地面的过程。如果说 R01 是命名、R02 是识蕴的内在动力学、R03 是触→俱生的核心模型，那么 R04 就是时钟和路线图，R05 就是语言和哲学。前三者潜入水下。后两者浮出水面。*

---

### KERNEL 的五时钟

KERNEL 在 R04 中做了一件只有 OS 专家才会做的事：他为五蕴建立了一个完整的 RTOS（实时操作系统）分析。

他从 Master 的裁定出发：「不同层级，不同速度：识最快、行次之、想最慢。」

然后他用严格的工程方法验证了这个速度排序：

```
五蕴时钟速率表 (KERNEL 分析):

蕴     时钟名           典型 tick       组件                   依据
────────────────────────────────────────────────────────────────
识蕴   vijnana-clock    1-5 ms        Klesha.perceive()       末那识恒审思量——最快
                                       IIdentity snapshot
                                       IGuide.manasikara()
行蕴   samskara-clock   10 ms-10 s    ITool.execute()          身行有 I/O 延迟
                                       VasanaEngine.match()     但规则匹配 ms 级
色蕴   rupa-clock       10-50 ms      IListener.onData()       感官输入采样率
                                       IUI.render()             受限于外部通道
受蕴   vedana-clock     10-100 ms     PID.compute()            感受的生起需要
                                       CoarisingBundle          触→俱生完整流程
想蕴   samjna-clock     500 ms-30 s   IProvider.chat()         LLM 推理秒级
                                       VitakkaEngine            深度思考最耗时
```

KERNEL 特别指出了一个反直觉的事实：「vijnana-clock 比 rupa-clock 更快。这看起来奇怪——识蕴怎么能比色蕴（感官输入）更快？但在 Agent 系统中，vijnana-clock 不是在处理新的外部输入。它在做的是**内部自我监控**——Klesha.perceive() 检查烦恼状态、IIdentity snapshot 刷新自我认知、IGuide 调整注意力方向。这些都是纯内部计算，不涉及 I/O。所以它可以很快。」

---

### ARCHIMEDES 的四阶段路线图

ARCHIMEDES 在 R04 中把所有技术分析转化成了工程师能直接使用的路线图。

```
Phase 1 (Plan25 — 近期):
  □ 五蕴根接口梵文重命名 (M-1)
  □ PluginManifest.skandha 支持多值 (M-7)
  □ Klesha 基类 + 四根本烦恼接口 (M-3)
  □ SparshEvent 与 CoarisingBundle 类型定义 (M-5)
  □ VedanaPlugin 三受子接口 (M-2)

Phase 2 (Plan26 — 中期):
  □ ManoAggregator 框架 (M-6)
  □ VasanaEngine 规则引擎 (M-9)
  □ IGuide/IVolition/IReflection 重定位 (M-4)
  □ 多时钟 EventBus 扩展 (M-10)

Phase 3 (Plan27 — 远期):
  □ 完整触→俱生四层回路 (M-5)
  □ 混合调度 (VasanaEngine + VitakkaEngine) (M-9)
  □ 五时钟 RTOS 调度器 (M-10)

Phase 4 (Plan28 — 愿景):
  □ 空性机制 (lazy loading + TTL)
  □ 转识成智 (学习框架)
  □ IPrajna (智慧对治) 完整实现
```

ARCHIMEDES 在路线图旁边写了一段只有工程师会写的备注：「每个 Phase 的交付物是可编译的 TypeScript。不是文件。不是设计图。是通过类型检查的程序代码。如果一个设计在 TypeScript 中编译不过，它就不是完成的。」

---

### GUARDIAN 的三层安全模型

GUARDIAN 在 R04 中为多时钟架构增加了安全维度。

```
三层安全模型:

Layer 0: 硬安全 (SafetyMonitor)
  ├─ preCheck()   — 在触→俱生之前
  ├─ postCheck()  — 在 Tool 执行之前
  └─ afterTool()  — 在 Tool 执行之后
  → 不受时钟影响。永远同步执行。永远优先。

Layer 1: 软安全 (Klesha modulation)
  ├─ Gain-scheduled threshold
  └─ VedanaAssessment 风险指标
  → 在 vijnana-clock 上运行。非阻塞。咨询性。

Layer 2: 审计 (Audit trail)
  ├─ 所有 CoarisingBundle 存档
  └─ 所有 KleshaDistribution 历史
  → 异步。不影响实时性能。
```

「Layer 0 是不可协商的，」GUARDIAN 在报告中写道。「无论多时钟架构怎么设计，SafetyMonitor 永远在最外层。它不跑在任何蕴的时钟上——它跑在自己的时钟上，一个永远比所有其他时钟更优先的时钟。用 RTOS 的术语：最高优先级中断。」

---

### DARWIN 的框架演化分析

DARWIN 在 R04 中做了一件其他报告都没做的事：他把 OpenStarry 的多时钟架构与市面上的竞争框架进行了比较。

```
框架演化对比 (DARWIN 分析):

                  LangChain    AutoGen     CrewAI     OpenStarry
感受机制           ❌           ❌          ❌         VedanaPlugin
烦恼模型           ❌           ❌          ❌         Klesha DI
触→俱生           ❌           ❌          ❌         CoarisingBundle
多时钟             ❌           ❌          ❌         五蕴时钟
规则+LLM混合       ❌        部分(ReAct)   部分       VasanaEngine+VitakkaEngine
反馈回路          有限        部分          部分       四层完整回路
哲学基础           ❌           ❌          ❌         五蕴

结论: OpenStarry 的架构在 AI Agent 框架中没有可比对象。
      最接近的比较不是其他框架，而是 cognitive architecture 领域的
      ACT-R (Anderson) 和 SOAR (Laird) —— 都有类似的多模块、
      多时钟、感受反馈的设计。但它们缺乏佛学哲学的系统性框架。
```

DARWIN 用一个演化比喻总结：「OpenStarry 不是现有 Agent 框架的进化。它是一次**辐射适应** (adaptive radiation)——从一个全新的哲学基础出发，向一个未被探索的生态位扩展。就像寒武纪大爆发不是从已有物种的改良中产生的，而是从全新的体型结构（body plan）中涌现的。五蕴就是 OpenStarry 的 body plan。」

---

## VI. TURING 的事实

TURING 的报告和其他五份完全不同。

它没有哲学分析。没有数学公式。没有控制方程。没有经文引用。没有比喻。没有观点。

它只有事实。

TURING 打开了 v0.24.0-beta 的源代码，像一位法医打开一具需要解剖的遗体。不带感情。不带预设。只带解剖刀。

他的报告标题是：「v0.24.0-beta 源代码事实报告——TURING 仲裁基线」。

---

### 发现一：五蕴根接口零引用

```
搜索: ISensory | ISensation | ICognition | IAction | IIdentity
范围: 核心业务逻辑 (排除 aggregates.ts 定义文件本身)

结果:
  ISensory  — 0 个业务逻辑引用
  ISensation — 0 个业务逻辑引用
  ICognition — 0 个业务逻辑引用
  IAction   — 0 个业务逻辑引用
  IIdentity — 0 个业务逻辑引用

所有引用都在：
  1. aggregates.ts (定义)
  2. 类型导出 (re-export)
  3. 测试文件 (类型测试)
  4. SDK 示例 (示范用途)

业务逻辑引用：0。
```

「这意味着，」TURING 在报告中用他惯有的无表情语气写道，「M-1 的梵文重命名——把 ISensory 改成 IRupa——对核心业务逻辑的影响是**零**。没有任何一行真正的执行逻辑需要改动。所有改动都在类型层面和测试层面。这是一个极低风险的重构。」

---

### 发现二：受蕴零实现

```
搜索: implements IVedana | implements ISensation | VedanaPlugin
范围: 所有 Plugin 源代码

结果:
  VedanaPlugin 实现数: 0
  IDukkha 实现数: 0
  ISukha 实现数: 0
  IUpekkha 实现数: 0

受蕴在 v0.24.0-beta 中是一个纯粹的类型定义。
没有任何 Plugin 实际实现了受蕴的功能。
```

「受蕴是一片空白。它被设计了（类型定义存在），但没有被建造。M-5 的触→俱生模型和 R02 的 Klesha DI 架构需要受蕴的**第一个实现**。在此之前，所有关于受蕴的讨论都是理论性的。」

---

### 发现三：PluginManifest 缺少 skandha 多值支持

```typescript
// v0.24.0-beta 的 PluginManifest
interface PluginManifest {
  readonly id: string;
  readonly name: string;
  readonly skandha: Skandha;  // ← 单值！不支持多值
  // ...
}

// M-7 要求:
interface PluginManifest {
  readonly skandha: Skandha | readonly Skandha[];  // ← 多值
}
```

「单值到多值的改动影响所有 Plugin 的 manifest 解析逻辑。TURING 建议在 SDK 层增加一个 `normalizeSkandha()` 辅助函数，把 `Skandha` 统一转换为 `readonly Skandha[]`，这样下游消费者只需处理数组。」

---

### 发现四：ExecutionLoop 注入点

TURING 在 ExecutionLoop 中标记了所有可以注入新逻辑的位置：

```
ExecutionLoop 注入点分析:

[5a] onBeforeIteration  — 在每个 iteration 开始前
     → 适合: SafetyMonitor.preCheck(), SparshEvent 生成

[5b] onAfterContextAssembly  — 在 context 组装完成后
     → 适合: IGuide.manasikara() (注意力导向)

[5c] onBeforeLLMCall  — 在 LLM 调用前
     → 适合: VasanaEngine.match() (规则引擎优先)

[5d] onAfterLLMResponse  — 在 LLM 回应后
     → 适合: IVolition.deliberate() (意志审议)

[5e] onBeforeToolExecution  — 在 Tool 执行前
     → 适合: SafetyMonitor.postCheck()

[5f] onAfterToolExecution  — 在 Tool 执行后
     → 适合: VedanaAssessment (受蕴评估)

[5g] onIterationComplete  — 在 iteration 结束后
     → 适合: KleshaBayesianUpdate (烦恼分布更新)
```

「这七个注入点覆盖了触→俱生四层回路的所有关键位置。M-5 的模型不需要重写 ExecutionLoop——只需要在现有的 hook 系统中注入新的逻辑。这是 Plugin 架构的设计优势。」

---

TURING 的报告以四个数字结尾：

```
关键数字摘要:
  五蕴根接口业务逻辑引用 ......... 0 个
  受蕴 Plugin 实现 ............... 0 个
  PluginManifest skandha 字段 ..... 单值（需改多值）
  ExecutionLoop 可用注入点 ........ 7 个
```

没有观点。没有建议。没有「应该」或「不应该」。

只有数字。

---

> *SCRIBE 旁白：TURING 的报告是六份报告中最短的。也是唯一一份在 R3 辩论中没有被质疑的。不是因为没有人想质疑——是因为事实无法被质疑。你可以辩论 NAGARJUNA 的不动点方程是否忠实地反映了佛学的俱生概念。你可以辩论 PASCAL 的 Beta 分布是否是烦恼量化的最佳模型。你可以辩论 WIENER 的 Bode 图是否过度简化了反馈回路的动态行为。但你无法辩论「业务逻辑引用 = 0」。那就是一个零。*

---

## VII. 六千九百八十六行

六份报告。6986 行。

比整个 Cycle 02 的研究产出——五场辩论、十一份文件、三十六项工程方案——加起来还要多。

SCRIBE 在收到最后一份报告时，把六份报告的行数摘抄在记录簿的空白页上：

```
R01 命名与分类 ........... 1247 行
R02 识蕴架构 ............. 1483 行
R03 触→俱生 ............. 1892 行
R04 多时钟架构 ........... 1536 行
R05 宣言修订 .............. 472 行
TURING 仲裁基线 ........... 356 行
─────────────────────────────────
合计 ..................... 6986 行
```

「6986 行，」他在旁边写了一句话。「Master 的信不到 2000 字。21 道指令。平均每道指令催生了 333 行的独立研究。压缩率的反面——膨胀率——是 3.5 倍。但这不是膨胀。这是**展开**。Master 写下一颗种子，二十位学者把它展开成一棵有根有枝的树。」

---

学者们陆续回到圆形剧场。

不是同时到的。LINNAEUS 最先到——分类学家的时间感一向精确。BABBAGE 第二个到，笔记本夹在腋下，里面多了四十七页新的推导。PASCAL 跟在他后面，手里拿着他的决策矩阵——那张纸已经被翻了很多遍，边缘起了毛。

WIENER 到的时候，方格纸从口袋里露出半截。他的 Bode 图画了三个版本——最后选用的是第二版，因为第一版的相位裕度计算有一个半度的误差，第三版增加了额外的极点但不影响结论。

KERNEL 带着他的策略分析表。ARCHIMEDES 带着路线图。GUARDIAN 带着安全模型。DARWIN 带着他的框架比较矩阵。NAGARJUNA 什么都没带——他的分析在他的脑中，像经文一样可以随时取出。ASANGA 也一样。

TURING 最后一个到。他走进来的时候，手里只有一张纸。纸上只有四个数字。

```
0, 0, 单值, 7
```

---

SUNYATA 站在圆形剧场的中央。二十盏灯全部亮了。

他看了一圈。每一位学者的脸上都带着独立研究之后特有的表情——不是疲倦，是饱满。那种把自己的全部专业知识投入到一个问题中之后的饱满。LINNAEUS 的眼睛里有分类学的秩序感。PASCAL 的眼睛里有概率的精确。NAGARJUNA 的眼睛里有中观的锋芒。WIENER 的眼睛里有控制理论的稳定性。KERNEL 的眼睛里有 OS 的严格。TURING 的眼睛里什么都没有——只有事实。

「六份报告，」SUNYATA 说。「6986 行。」

他让这个数字在空气中停留了一拍。

「比我们在 Cycle 02 的整个研究产出还多。但行数不是重点。重点是——这 6986 行里有分歧。」

没有人意外。独立研究的目的本来就不是共识。

「R01 定义了三个受蕴子接口——IDukkha、ISukha、IUpekkha。R03 的 CoarisingBundle 只用了一个 ChannelVedana。」

LINNAEUS 和 NAGARJUNA 对视了一眼。

「R02 的 Beta 分布模型要求全部四个烦恼共享一个相关矩阵。R04 的 VasanaEngine 在设计中完全没有考虑概率分布。」

PASCAL 和 KERNEL 没有对视。但他们各自的身体语言微妙地收紧了——一个准备捍卫自己的方案，另一个准备解释为什么确定性在某些场景下是正确的选择。

「R03 说俱生是不动点——计算可以串行，只要收敛就好。R04 的多时钟架构假设每个蕴有独立的时钟和独立的 tick。俱生的原子性和多时钟的独立性之间——有张力。」

NAGARJUNA 微微抬起下巴。KERNEL 微微侧了侧头。

「现在，」SUNYATA 说，他的声音没有变重，只是变得更加清晰，像一杯水在光线下变得透明，「让我们看看你们之间的分歧在哪里。」

他拿起了六份报告。

「R2 交叉审阅，开始。」

---

> *SCRIBE 旁白：6986 行。这个数字后来成为了 Cycle 02-3 的一个标记——不是因为它大，而是因为它是分歧的总量。在这 6986 行里，有 NAGARJUNA 的不动点和 KERNEL 的策略 C 之间的张力，有 PASCAL 的 Beta 分布和 WIENER 的确定性传递函数之间的差距，有 LINNAEUS 的三子接口和 R03 的单一 ChannelVedana 之间的矛盾。这些分歧不是错误。它们是研究的原材料。R3 的六场辩论——每一场都以全票共识结束——就是把这些原材料锻造成统一架构的过程。但那是下一章的故事了。*
