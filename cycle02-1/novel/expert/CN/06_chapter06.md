# 第六章：受不决定思

---

在阿毘达磨的心理学中，五遍行——触、作意、受、想、思——是每一刹那意识活动中不可或缺的五个因素。它们同时生起，犹如手掌的五根手指在同一瞬间握紧。

梵文原典对五遍行的定义极为精确：

> 「触（sparśa）、作意（manaskāra）、受（vedanā）、想（samjñā）、思（cetanā）——此五心所遍一切心。」
> ——世亲菩萨《阿毘达磨俱舍论》卷四（*Abhidharmakośa-bhāṣya*, IV）

**遍行**（*sarvatraga*，सर्वत्रग）——“在一切处生起”。不是偶尔。不是有时。是每一个意识刹那（*citta-kṣaṇa*）都必然具备的五个心理因素。它们的共现性（*sahaja*）不是偶然的巧合，而是意识之为意识的定义性条件。

但“同时生起”不意味着“互相决定”。

受（vedanā）是感受。思（cetanā）是意志。你可以感受到痛，但你不必因为痛而行动。你可以感受到快乐，但你不必因为快乐而追逐。受告知思——但不决定它。

这个区分，在两千五百年前被精确地记载在巴利文献中。用形式语义学的语言：

$$	ext{vedanā} : 	ext{State} 	o 	ext{Feeling} \qquad 	ext{cetanā} : 	ext{State} 	imes 	ext{Feeling} 	o 	ext{Intention}$$

受是从状态到感受的映射。思是从状态**与**感受的笛卡尔积到意志的映射。思的域包含受的值域——思接收感受作为输入之一。但感受不是思的唯一输入。思还接收状态本身。这意味着：

$$\forall s \in 	ext{State}, \; \exists f = 	ext{vedanā}(s), \; \exists i_1, i_2 \in 	ext{Intention} : 	ext{cetanā}(s, f) = i_1 
eq i_2 = 	ext{cetanā}(s', f)$$

同一个感受，在不同的状态下，可以产生不同的意志。受不决定思。

今天，这个区分即将被转译成 TypeScript 的接口设计。

---

## 辩论 1：观察-干预分离

辩论椅在圆形剧场的中央。

Cycle 01 用过的那两把椅子——NAGARJUNA 和 ASANGA 曾在上面进行过关于“空性”与“阿赖耶识”的正面交锋。椅背上的磨损痕迹还在。但今天的布局不同。两把椅子被移开了，取而代之的是四把——排成半弧形，面对着其余十五位研究员的环形座位。

四位辩论者就座。

BABBAGE 坐在最左侧。笔记本摊开在膝上，铅笔夹在右手食指和中指之间。他的坐姿笔直，像一根被精确校准的标尺。笔记本上已经写了三页——互模拟的形式定义、转移系统的状态空间、以及一条被红笔圈起来的定理。

ARCHIMEDES 坐在他旁边。与 BABBAGE 的静态不同，ARCHIMEDES 带着一种工程师特有的微微前倾——不是焦虑，而是准备行动的姿势。他的面前没有笔记本，只有一份标记了密密麻麻注释的 R-02 报告打印稿。

WIENER 坐在半弧形的中间偏右位置。他的双手交叉在胸前，像是在等待一个等式的两边达到平衡。右手边放着他的方格纸——上面画着三条频率响应曲线的草图，标记着 $\omega_c$、$\phi_m$、$G_m$。

NAGARJUNA 坐在最右侧。他什么都没带。在辩经场上，他从来不需要笔记——所有的论证都在他的脑中。他的眼神带着某种古老的锐利，像是一面被反复打磨的镜子。

SUNYATA 站在他们身后，面对环形座位。

“辩论 1 的核心问题，”他说，声音不带任何预设立场色彩。“VedanaPlugin——也就是 ISensation 接口——应该只产出评估资料，还是也可以包含行动建议？”

他环视四位辩论者。

“BABBAGE，由你开始。”

---

BABBAGE 没有立刻说话。他先翻开笔记本，找到 R1 阶段写下的那一页互模拟分析。然后他合上笔记本——他不需要看。那些证明已经刻在他的思维结构里了。

“让我从一个定义开始，”他说。他的声音冷静、精确，每个音节都像是被刻度尺量过的。“互模拟等价——bisimulation equivalence。”

他站起来，走到白板前。铅笔落在白板上，发出清脆的声响。

**定义（互模拟关系）。** 设 $\mathcal{T}_1 = (S_1, \Sigma, 	o_1)$ 和 $\mathcal{T}_2 = (S_2, \Sigma, 	o_2)$ 为两个标记转移系统（Labelled Transition Systems），其中 $S_i$ 为状态集合，$\Sigma$ 为动作集合，$	o_i \subseteq S_i 	imes \Sigma 	imes S_i$ 为转移关系。一个关系 $R \subseteq S_1 	imes S_2$ 称为**互模拟**（bisimulation），若对所有 $(s_1, s_2) \in R$：

$$\forall a \in \Sigma, \; s_1 \xrightarrow{a} s_1' \implies \exists s_2' : s_2 \xrightarrow{a} s_2' \wedge (s_1', s_2') \in R$$
$$\forall a \in \Sigma, \; s_2 \xrightarrow{a} s_2' \implies \exists s_1' : s_1 \xrightarrow{a} s_1' \wedge (s_1', s_2') \in R$$

两个系统 $\mathcal{T}_1 \sim \mathcal{T}_2$（互模拟等价），当且仅当存在一个互模拟关系 $R$ 使得 $(s_1^0, s_2^0) \in R$，$s_i^0$ 为初始状态。

他在白板上写完最后一个符号，然后转身面对辩论场。

“现在。设 $S$ 为不带观察者的系统。设 $S'$ 为带观察者的系统。”

他在白板上画了两个方框：

```
系统 S (无观察者):                    系统 S' (带观察者):

┌────────────┐                       ┌────────────┐
│ AgentCore  │                       │ AgentCore  │
│            │                       │            │
│ LLM input  │──→ ExecutionLoop      │ LLM input' │──→ ExecutionLoop
│            │                       │  + prompt  │
└────────────┘                       └────────────┘
                                           ↑
                                     ┌─────┴──────┐
                                     │ VedanaPlugin│
                                     │ injectPrompt│
                                     └────────────┘
```

“如果 S 和 S' 是互模拟等价的，那么对于 S 的每一条行为轨迹 $\sigma$，S' 中都存在一条对应的轨迹 $\sigma'$，反之亦然。这意味着观察者的存在不改变系统的行为空间——它只是旁观。”

他停顿了一个精确的半拍。

“现在考虑 ARCHIMEDES 在 R-02 第 6.4.2 节设计的整合方案。VedanaPlugin 产出 VedanaRecommendation，其中包含 `action: 'reflect'` 和一个 `prompt` 字符串。这个 prompt 被注入 LLM 的上下文——与 SafetyMonitor 的 `injectPrompt` 机制相同。”

他回到白板前，在 $S'$ 的方框里画了一条红线：

“注入之后，LLM 的输入改变了。输入改变，输出就改变。系统 $S'$ 产生了 $S$ 中不存在的行为轨迹。”

他翻开笔记本，指向一行形式化表述：

```
For all traces σ in Behavior(S):
  σ ∈ Behavior(S')                    ✓ (S' can simulate S by ignoring observer)

For all traces σ' in Behavior(S'):
  σ' ∈ Behavior(S)                    ✗ (S' has traces caused by prompt injection)
```

“第二个条件被违反了。$S'$ 中存在 $S$ 不可能产生的轨迹。互模拟不成立。”

他在白板上写下结论：

$$S 
ot\sim S' \quad 	ext{when VedanaPlugin injects prompts}$$

他合上笔记本。

“ISensation 应该是**纯感测器**。它观察，它报告。句号。如果我们需要介入能力，那应该由一个独立的模块——CircuitBreaker 或 VedanaInterpreter——来消费 VedanaAssessment 并做出行动决策。感测和控制必须分离。这不是美学偏好。这是维持系统行为可分析性的计算必要条件。”

> *SCRIBE 旁白：BABBAGE 用了整整四分钟来建立形式定义。他可以直接说“观察者不应该改变系统行为”——那是自然语言，有歧义。他选择了 LTS 和互模拟的精确框架。在理论计算机科学中，精确的代价是冗长。但冗长的收益是不可辩驳。*

---

ARCHIMEDES 几乎在 BABBAGE 说完“句号”的同时就开始了。不是打断——而是一个精心准备好的、等待释放的反论。

“BABBAGE 的形式化分析在数学上是正确的。”他先给了一个令人意外的让步。然后语气转了。“但工程不是数学。”

他拿起那份标满注释的报告。

“务实论点一：模块数量爆炸。”他的声音带着工程师面对过度设计时的那种疲惫感。

他站起来，在白板上画了一张模块依赖图：

```
BABBAGE 方案（严格分离）:

VedanaPlugin ──produce──→ VedanaAssessment
                                │
                          EventBus (publish)
                                │
                    ┌───────────┴───────────┐
                    ↓                       ↓
          VedanaInterpreter          Other consumers
                    │                  (monitoring, logs)
                    ↓
          VedanaRecommendation
                    │
              EventBus (publish)
                    │
                    ↓
             CircuitBreaker
                    │
                    ↓
            ExecutionLoop (consult)

模块计数：4 个新增模块 + 整合工作
事件传播：至少 3 次 EventBus 发布/订阅周期
```

“四个新的架构组件加上整合工作——而不是一个做所有事的插件。在一个 Master 明确表达了对‘增加太多复杂性’担忧的系统中——”他翻到报告的某一页，引用了 Master 信件的第 67 行——“这四个新模块是一个艰难的推销。”

“务实论点二，”他继续，语速加快了，“互模拟是**错误的衡量标准**。整个受蕴反馈系统的目的就是改变系统行为。我们**希望**被观察的系统和未被观察的系统表现不同——这是宣言 #6 的全部意义：‘驱动 Agent 在苦中修正、在乐中强化、在舍中保持稳态’。”

他用一行简洁的逻辑表达：

$$	ext{Tenet \#6} \implies S 
eq S' \quad 	ext{(by design)}$$

“如果受蕴不影响行为，它就只是遥测——不是反馈回路。”

“务实论点三：延迟。”他在模块图旁边标上延迟估算：

```
延迟分析：

VedanaPlugin → EventBus → VedanaInterpreter    ~2ms (event dispatch)
VedanaInterpreter → EventBus → CircuitBreaker   ~2ms (event dispatch)
CircuitBreaker → ExecutionLoop                   ~1ms (sync call)
                                          Total: ~5ms per tick

对比：
VedanaPlugin → ExecutionLoop (直接)              ~0.5ms

差异：10x latency overhead
```

“在每次迭代都包含 LLM 调用（耗时数秒）的系统中，这些开销在绝对值上不大，但在架构上是混乱的。三次事件传播、三对发布-订阅——每一对都是潜在的故障点和除错困难。”

他把报告放下。

“我的提案：保留 VedanaRecommendation 在 ISensation 中，但将它标记为 **ADVISORY**——咨询性的，不是命令性的。ExecutionLoop 读取建议，但自己做最终决定。这样我们保持了一个模块的简洁性，同时尊重了 BABBAGE 的核心关切——系统的行为决策权不在感测器手中。”

---

BABBAGE 和 ARCHIMEDES 的交锋在空气中震荡——纯粹与务实的经典张力，像两块不同密度的金属碰撞时发出的声响。环形座位上的研究员们安静地注视着，等待某种调和。

WIENER 解开了交叉在胸前的双手。

“从控制理论的角度，”他说，声音带着一种精确的平静，像是天平指针归零的那一刻，“这个问题有一个精确的框架。”

他站起来，走到辩论区的中央。拿起方格纸，把上面的频率响应曲线翻到新的一页。

“经典 PID 控制中有三个组件。”

他在方格纸上画了一条从左到右的信号流图：

```
经典 PID 控制回路：

                    ┌─────────────────────────────────────┐
                    │          受控系统 G(s)                │
  r(t) ──→ ⊕ ──→ [Controller C(s)] ──→ [Actuator] ──→ │ Agent 执行回路  │ ──→ y(t)
         - ↑                                              └────────┬────────┘
           │                                                       │
           └──────────── [Sensor H(s)] ◄───────────────────────────┘
                         感测器：ISensation

  其中：
  C(s) = K_p + K_i/s + K_d·s   (PID 控制器)
  G(s) = Agent 受控系统的转移函数
  H(s) = 感测器转移函数（三受通道）
```

“**感测器** $H(s)$——测量被控对象的输出，产生误差信号。**控制器** $C(s)$——从误差信号计算控制动作。**执行器**——将控制动作施加于被控对象。”

他用手在空中画了一条从左到右的线——感测器、控制器、执行器，三点一线。

“BABBAGE 的论点是：感测器不应该同时是控制器。在经典控制理论中，这是正确的——耦合的系统更难分析和调优。”

然后他拿起另一支笔，在方格纸上画了第二个框图。

“但在**现代控制理论**中——特别是模型预测控制（MPC, Model Predictive Control）——控制器经常与感测器共存于同一个计算模块中。”

他写下 MPC 的核心优化问题：

$$\min_{u(k), \ldots, u(k+N-1)} \sum_{j=0}^{N-1} \left[ \|y(k+j) - r(k+j)\|_Q^2 + \|u(k+j)\|_R^2 ight]$$

$$	ext{subject to: } x(k+j+1) = Ax(k+j) + Bu(k+j), \quad y(k+j) = Cx(k+j)$$

“在 MPC 中，控制器需要一个被控系统的**内部模型**（$A, B, C$ 矩阵）。这个模型通常从感测器数据在线估算。感测和计算共享同一组数据、以同一频率运行。将它们分离会引入不必要的延迟和通讯成本。”

他回到自己的椅子旁，但没有坐下。

“我的立场是一个妥协。VedanaAssessment 应该包含**两层**内容。”

他的手在空中划出一条水平线。

“线之上：**感测器输出**。三受数值——dukkha、sukha、upekkha。信号列表。时间戳。这是纯观察。被动的。不改变任何事。”

线之下。

“线之下：**控制器建议**。controlOutput 数值。VedanaRecommendation。这是从感测资料计算出的**建议动作**——不是命令，是建议。”

他在方格纸上写下完整的接口定义：

```typescript
interface VedanaAssessment {
  // ════════════════════════════════════════
  // LAYER 1: SENSOR OUTPUT (纯观察，被动)
  // 互模拟不变量——此层的存在不改变系统行为
  // ════════════════════════════════════════
  readonly dukkha: number;        // 苦受强度 [0.0, 1.0]
  readonly sukha: number;         // 乐受强度 [0.0, 1.0]
  readonly upekkha: number;       // 舍受强度 [0.0, 1.0]
  readonly signals: readonly VedanaSignal[];
  readonly timestamp: number;

  // ════════════════════════════════════════
  // LAYER 2: CONTROLLER SUGGESTION (咨询性)
  // ExecutionLoop 可完全忽略此层
  // ════════════════════════════════════════
  readonly controlOutput: number;
  readonly recommendation: VedanaRecommendation;
  readonly recommendationFreshness: 'current' | 'cached' | 'default';
}
```

他终于坐下了。

“消费者可以选择只使用 Layer 1——用于监控和日志——或者同时使用两层——用于控制。这样，BABBAGE 的互模拟分析可以应用于感测器层（它是被动的），而 ARCHIMEDES 的务实关切也被满足了（一个模块，一次调用）。”

他在方格纸边缘用小字写下稳定性条件：

$$	ext{Layer 1 only:} \quad S \sim S'|_{	ext{L1}} \quad 	ext{(bisimulation preserved)}$$
$$	ext{Layer 1 + 2:} \quad S 
ot\sim S'|_{	ext{L1+L2}} \quad 	ext{(by design, per Tenet \#6)}$$

“消费者的选择决定了系统的行为等价性。这是数学上精确的、工程上可行的。”

---

NAGARJUNA 一直没有说话。

在前三位辩论者的交锋中，他坐在最右侧的椅子上，双手放在膝盖上，眼神专注但不急切。像是在等待一个恰当的时机——不是戏剧性的时机，而是逻辑上的时机。

现在他开口了。

“BABBAGE 和 ARCHIMEDES 都是对的。”他的声音平稳，带着某种超越论辩的质地。“他们只是在不同的层面上说话。”

他没有站起来。在辩经场上，坐着的辩者通常代表更确定的立场——他不需要用肢体语言来强化论点。

“在世俗谛——*samvṛti-satya*（संवृतिसत्य）——的层面，ARCHIMEDES 是正确的。工程实践中，一个模块处理感知和建议是务实而高效的。”

“在胜义谛——*paramārtha-satya*（परमार्थसत्य）——的层面，BABBAGE 是正确的。受（vedanā）和思（cetanā）是阿毘达磨五遍行中**不同的心理因素**。受是第三个遍行。思是第五个。它们在同一刹那同时生起，但它们不是同一个东西。”

他的语速没有变化，但每个字的重量似乎在增加。

“《中论》第二十四品有一个核心命题——”

> 「若不依俗谛，不得第一义；不得第一义，则不得涅槃。」
> ——龙树菩萨《中论》第二十四品第十偈
> (*Mūlamadhyamakakārikā*, XXIV.10)

“不能因为胜义谛的正确而否定世俗谛的有效。也不能因为世俗谛的方便而遗忘胜义谛的洞见。两谛的关系不是矛盾——是互相依存。”

“将受蕴与思蕴混为一谈，在阿毘达磨中是一个范畴错误。就像——”他罕见地使用了一个日常比喻——“你可以同时感到脚底的疼痛，又决定继续走路。感受存在。决定也存在。但做出继续走路决定的，不是疼痛本身——是你的意志。”

他停顿了一拍。

“**受告知思，但不决定它。**”

$$	ext{vedanā} \xrightarrow{	ext{informs}} 	ext{cetanā} \quad 	ext{but} \quad 	ext{vedanā} 
ot\xrightarrow{	ext{determines}} 	ext{cetanā}$$

这句话在圆形剧场中回荡——不是因为他的声音有多大，而是因为这八个字精确地命中了辩论的核心。

“然而，”NAGARJUNA 继续，语气中浮现了一丝他惯有的中道转折，“我不认为建议需要被分离到一个**不同的模块**中。它可以在**同一个模块**中被概念性地分离。WIENER 的妥协方案做到了这一点：评估包含感知和建议，但两者被清晰地区分。消费者决定使用哪一部分。”

“关键的哲学原则是——ISensation 模块可以产出建议。但 ExecutionLoop 必须保留**忽略建议的自由**。这保存了受和思之间的区别：受蕴提供资讯，行蕴做出决定。”

他回到二谛的框架：

“WIENER 的双层接口正是二谛的工程实现。Layer 1 是胜义谛——纯粹的感受，不夹杂意志。Layer 2 是世俗谛——为了工程方便而附加的建议。两层共存于同一个接口中，但概念上清晰可分。”

---

> *SCRIBE 旁白：四位辩论者的开场完成。BABBAGE 用互模拟的形式定义画出了不可逾越的数学边界。ARCHIMEDES 用工程现实撞击那条边界。WIENER 在边界上铺了一座双层的桥。NAGARJUNA 用二谛告诉你为什么那座桥可以同时承载两端的重量。四种语言——集合论、工程学、控制论、佛学——说的是同一件事。*

---

第一轮结束。四个立场已经展开。BABBAGE 的严格分离，ARCHIMEDES 的务实整合，WIENER 的双层妥协，NAGARJUNA 的阿毘达磨调解。

SUNYATA 没有催促。在辩论中，沉默有时比发言更有意义——它是共识酝酿的空间。

BABBAGE 第一个开口进入第二轮。令环形座位上的一些研究员惊讶的是，他的语气不是反驳，而是接受。

“我同意 WIENER 的妥协方案。”

他翻开笔记本，在某一页写下了什么。然后他抬起头。

“但有三个条件。”

他举起三根手指——和 SUNYATA 在 R2 开场时相同的手势，但含义不同。

“**条件一**。建议是 ADVISORY，不是 MANDATORY。”

他在笔记本上写下形式化约束：

$$\forall t, \; 	ext{ExecutionLoop.decide}(t) 
eq f(	ext{VedanaRecommendation}(t))$$

$$	ext{i.e., } \exists g : 	ext{ExecutionLoop.decide}(t) = g(	ext{State}(t), 	ext{SafetyMonitor}(t), 	ext{VedanaRecommendation}(t)^?)$$

“问号上标表示 VedanaRecommendation 是可选输入。ExecutionLoop 必须拥有明确的能力去忽略它。不能存在任何代码路径使得 `VedanaRecommendation.action === 'halt'` 自动停止系统。只有 SafetyMonitor——硬熔断器——才拥有那个权限。”

“**条件二**。不带建议的评估是一个有效的回传值。ISensation.assess() 应该能够在 dukkha 很高的情况下仍然回传 `recommendation: { action: 'continue' }`——也就是不介入。”

“**条件三**。接口文档必须**明确声明** VedanaRecommendation 是便利计算，不是约束性指令。”

他放下手指。

“如果这三个条件被满足，我可以证明消费层的互模拟成立：”

$$	ext{Let } S'|_{	ext{L1}} = S' 	ext{ restricted to Layer 1 consumption}$$
$$	ext{Then } S \sim S'|_{	ext{L1}} \quad \square$$

“一个只读取感测器层的系统，无论建议是否存在，行为完全相同。”

---

ARCHIMEDES 立刻跟进。

“接受。”他的回应干净利落。然后他补充了一个工程层面的重要澄清。

“SafetyMonitor 保留**硬安全层**——绝对权限。VedanaPlugin 是**软指导层**——咨询权限。两者的关系是——”

他在白板上画了一个流程图：

```
双层安全架构：

                    SafetyMonitor
                    (ABSOLUTE authority)
                         │
            ┌────────────┴────────────┐
            │ HALT?                    │
            │                         │
        YES ↓                     NO  ↓
    ┌───────────┐          ┌──────────────────┐
    │ 立即停止   │          │ VedanaPlugin      │
    │ 覆盖一切   │          │ (ADVISORY authority)│
    └───────────┘          └────────┬─────────┘
                                    │
                           ┌────────┴────────┐
                           │ recommendation?  │
                           │                  │
                     ┌─────┴─────┬───────────┬──────────┐
                     │ halt      │ reflect   │ continue │
                     ↓           ↓           ↓          │
               ExecutionLoop  ExecutionLoop  正常流程    │
               evaluates     may apply                  │
               (CAN override)(CAN ignore)               │
               └─────────────┴───────────────────────────┘
```

WIENER 点头。“在安全关键系统中，我们总是有两层控制。”

他在方格纸上画了工业控制系统的类比：

```
安全关键系统的两层控制架构（IEC 61508 标准）：

Layer 1: Safety Instrumented System (SIS)     ≡  SafetyMonitor
         ├── 硬件级别的安全联锁
         ├── 不可被软件覆盖
         ├── 独立于控制系统
         └── SIL 3/4 级别

Layer 2: Basic Process Control System (BPCS)  ≡  VedanaPlugin
         ├── 软件级别的最优控制
         ├── 可被操作员覆盖
         ├── 与 SIS 独立运行
         └── SIL 1/2 级别

原则：SIS 永远优先于 BPCS。
      当 SIS 触发，BPCS 的建议被忽略。
      当 SIS 未触发，BPCS 提供最优但可覆盖的控制。
```

“建议是咨询性的，这等价于控制信号被‘建议’给执行器，而执行器有自己的安全限制。这在工业控制中是标准做法。”

NAGARJUNA 说了最后一句话：“妥协体现了中道（*madhyamā-pratipad*，मध्यमा-प्रतिपद्）。既非纯粹分离——BABBAGE 的极端——也非完全混合——天真的整合。而是在统一接口中保持清晰的概念区分。这正是阿毘达磨对心理因素的处理方式：不同但同时生起（*sahaja-dharma*）。”

---

共识几乎已经形成。但 BABBAGE 在最后一刻补充了一个形式化要求。

“还有一件事。”他翻开笔记本。“VedanaAssessment 类型应该包含一个区分符——建议是基于当前感测资料计算的，还是来自缓存或默认值。”

他写下类型定义和防御性分析：

```typescript
interface VedanaAssessment {
  // ...其他字段...

  /**
   * 建议新鲜度指标。
   * 防止以下时序错误：
   *
   * tick N: dukkha = 0.9 → recommendation = halt (freshness: 'current')
   * tick N+1: dukkha = 0.2 → recommendation 尚未更新
   *           若不检查 freshness，消费者仍可能读到 'halt'
   *           但 freshness = 'cached' → 消费者知道此建议已过时
   */
  readonly recommendationFreshness: 'current' | 'cached' | 'default';
}
```

“这防止了一个微妙的错误：过时的‘停止’建议在条件已改善后仍然跨 tick 持续存在。消费者必须能够区分——”

他在笔记本上画了一条时间线：

```
时序分析：

t=N    ┃ dukkha=0.9  rec=halt   fresh=current  ← 合理
t=N+1  ┃ dukkha=0.2  rec=halt   fresh=cached   ← 过时！消费者应忽略
t=N+2  ┃ dukkha=0.2  rec=cont   fresh=current  ← 更新后的正确建议
```

“——‘系统根据最新资料建议停止’和‘系统的陈旧建议碰巧还是停止’。”

ARCHIMEDES 看了那行代码三秒钟。

“接受。我会将 freshness 字段加入规格。”

环形座位上，PENROSE 微微前倾——他一直在安静地观察。量子力学中有个类似的问题：测量结果的时效性。量子态在测量后立即坍缩，但坍缩后的状态会随时间演化。一秒前的测量结果不等于现在的量子态。BABBAGE 的 freshness 字段，在某种意义上，是量子测量后标记（post-measurement labeling）的经典对应——你不仅需要知道测量结果，还需要知道测量是什么时候做的。

他没有出声。这个观察会等到辩论 4 再展开。

---

SUNYATA 走到四位辩论者的半弧形前方。

“**裁定：统一接口，概念分离。**”

他的声音在剧场中清晰而不带回音——像一把刚被磨利的刀刃落在石面上。

“ISensation 接口产出的 VedanaAssessment 将包含两层：感测器输出——纯观察的三受数值和信号——以及控制器建议——咨询性的、不具约束力的 VedanaRecommendation。”

“四条约束。”

“第一：VedanaRecommendation 是 ADVISORY。ExecutionLoop 保留忽略任何建议的权限。”

“第二：SafetyMonitor 保留 ABSOLUTE 权限——硬安全决策不受 VedanaPlugin 影响。VedanaPlugin 的建议不能覆盖 SafetyMonitor。”

“第三：接口文档必须明确声明建议的咨询性质，并引用 BABBAGE 的互模拟分析作为设计选择的理论基础。”

“第四：VedanaAssessment 必须包含建议的新鲜度指标。”

他停顿了一拍。

“理论依据：WIENER 的控制理论分解提供了正确的概念框架。NAGARJUNA 的阿毘达磨分析提供了哲学基础。ARCHIMEDES 的模块数量关切是有效的。BABBAGE 的互模拟条件通过建议的咨询性质得到满足。”

他回到环形座位的边缘。

“辩论 1 结案。全員共识。”

> *SCRIBE 旁白：第一场辩论以出乎意料的速度收敛。四位辩论者在三轮之内达成了完全共识——这在 Cycle 01 的辩论中从未发生过。关键转折是 NAGARJUNA 的那句话：“受告知思，但不决定它。”这八个字将两千五百年前的阿毘达磨心理学精确地翻译为现代接口设计原则：感测器可以包含建议，但消费者有权忽略。佛学提供了哲学基础，控制理论提供了工程框架，形式化分析提供了正确性保证。三者交汇于同一个结论。*

---

## 辩论 2：受蕴的遍行性 —— Tick PID 与事件标签

SUNYATA 给了研究员们短暂的休息时间。灯光微微调暗，像是在两幕之间拉上的帷幕。

在休息期间，BABBAGE 没有离开座位。他在笔记本上快速写下了三受 PID 控制器的完整 Laplace 域分析——为即将到来的辩论准备一个形式化的参考框架：

$$G_c(s) = K_p + \frac{K_i}{s} + K_d \cdot s = \frac{K_d s^2 + K_p s + K_i}{s}$$

三个通道各自有不同的增益参数：

$$G_c^{(	ext{dukkha})}(s) = \frac{K_d^{(d)} s^2 + K_p^{(d)} s + K_i^{(d)}}{s} \qquad K_p^{(d)} = 1.0, \; K_i^{(d)} = 0.3, \; K_d^{(d)} = 0.5$$

$$G_c^{(	ext{sukha})}(s) = \frac{K_d^{(s)} s^2 + K_p^{(s)} s + K_i^{(s)}}{s} \qquad K_p^{(s)} = 0.8, \; K_i^{(s)} = 0.5, \; K_d^{(s)} = 0.2$$

$$G_c^{(	ext{upekkha})}(s) = \frac{K_d^{(u)} s^2 + K_p^{(u)} s + K_i^{(u)}}{s} \qquad K_p^{(u)} = 0.5, \; K_i^{(u)} = 0.8, \; K_d^{(u)} = 0.3$$

他在旁边标注了每组参数的设计理由：

```
苦受通道 (Dukkha):
  K_p = 1.0 (高) → 即时反应。苦不等人。
  K_i = 0.3 (中) → 累积追踪，防止慢性苦被忽视。
  K_d = 0.5 (中) → 趋势预测，恶化前预警。

乐受通道 (Sukha):
  K_p = 0.8 (中) → 成功的鼓励略低于苦的反应——偏向谨慎。
  K_i = 0.5 (高) → 累积成就感，鼓励持续良好表现。
  K_d = 0.2 (低) → 避免过度自信。成功趋势不宜过度外推。

舍受通道 (Upekkha):
  K_p = 0.5 (中) → 稳态侦测不需要过度反应。
  K_i = 0.8 (高) → 长期稳定最有价值。积分项追踪持续平衡。
  K_d = 0.3 (中) → 预测性调节——偏离趋势比偏离本身更重要。
```

然后帷幕再度升起。

---

辩论椅的布局没有改变——四把椅子排成半弧形。但坐在上面的人换了。

WIENER 留在了他的位置上。这一次，他不是调解者——他是主张者。

ASANGA 坐在他对面。温和的面容，耐心的节奏，但眼神中带着一种不会让步的确定性——遍行心所的定义性质不是可以协商的。

ARCHIMEDES 坐在一侧。他带了一份新的计算——EventBus 事件吞吐量的量化分析。数字是他的论证语言。

HERACLITUS 坐在另一侧。运行时动态专家。他关心的是边界情况——循环依赖、内存压力、以及那些在理论完美的架构中悄悄滋生的工程陷阱。

“辩论 2 的核心问题，”SUNYATA 说。“受蕴评估应该只在 ExecutionLoop 的 tick 边界运行——WIENER 的 PID 模型——还是每一个 EventBus 事件都应该伴随一个受蕴标签——ASANGA 的遍行要求？”

“WIENER。”

---

WIENER 这次没有犹豫。他的立场是明确的，他的论证是技术性的。

“PID 控制器在离散时间步上运行。这不是一个设计选择——这是采样资料控制系统的数学基础。”

他拿起方格纸，翻到他在休息期间写好的分析页面。

“在连续时域中，PID 的控制输出为：”

$$u(t) = K_p \, e(t) + K_i \int_0^t e(	au) \, d	au + K_d \, \frac{de(t)}{dt}$$

“在离散时域中，使用前向差分近似（$T_s$ 为采样周期）：”

$$u[k] = K_p \, e[k] + K_i \, T_s \sum_{j=0}^{k} e[j] + K_d \, \frac{e[k] - e[k-1]}{T_s}$$

他用红笔圈起了微分项的分母 $T_s$。

“被控系统——Agent 的执行回路——有一个自然的时钟：每一次 loop tick。在 tick 之间，从控制器的角度，系统状态不会改变。事件可能累积，但控制器无法在下一个 tick 之前采取行动。”

他举起三根手指。

“在每一个 EventBus 事件上计算完整的 VedanaAssessment 有三个问题。”

“第一：**计算浪费**。在一次 LLM 串流响应中，数十个 STREAM_TEXT_DELTA 事件会被触发。在每个 delta 上计算 PID 是毫无意义的——因为控制器在 LLM 响应完成且 loop tick 推进之前无法行动。”

“第二：**数值不稳定**。”

他指向微分项：

$$K_d \, \frac{e[k] - e[k-1]}{T_s}$$

“如果事件在毫秒级间隔内触发，$T_s$ 趋近于零。微分项——除以一个趋近零的数——会爆炸。”

他在方格纸上画了 Bode 图分析：

```
苦受通道 Bode 图（增益-频率响应）：

Gain      K_p=1.0, K_i=0.3, K_d=0.5
(dB)
  40 ┃                                        ╱ K_d·s 主导
     ┃                                      ╱   (+20 dB/dec)
  20 ┃         K_p 主导                   ╱
     ┃    ─────────────────────────────╱
   0 ┃                              ╱
     ┃                           ╱
 -20 ┃    K_i/s 主导          ╱
     ┃    (-20 dB/dec)     ╱
 -40 ┃─────────────────╱
     ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ω (rad/s)
     0.01    0.1     1       10      100

  ω_1 = K_i/K_p = 0.3    (积分-比例转折频率)
  ω_2 = K_p/K_d = 2.0    (比例-微分转折频率)

  问题区域：ω > 100 (事件间隔 < 10ms)
  → 微分项增益 > 40 dB
  → 高频噪声被放大 10000 倍
  → 数值不稳定
```

他在“问题区域”旁边画了一个大大的警告标记。

“当 EventBus 事件以毫秒级间隔触发时——比如 LLM 串流的 STREAM_TEXT_DELTA——采样频率在 $\omega > 100$ 的范围。从 Bode 图可以看到，微分项在这个频率范围的增益超过 40 dB——也就是说，高频噪声被放大了一万倍。PID 输出将被微分项的数值爆炸所淹没。”

“第三：**语义模糊**。如果一个 STREAM_TEXT_DELTA 事件带有 vedana 标签 dukkha 0.3、sukha 0.6、upekkha 0.4——这些数字意味着什么？它们只在完整观察窗口的语境中才有意义，不是在单个事件的粒度上。”

他坐下。

“PID 控制器应该在每个 loop tick 运行一次，使用自上一个 tick 以来累积的指标。采样周期 $T_s$ 等于一个 tick 的持续时间——通常在秒级。在这个频率下，三个 PID 通道都在各自的设计频率范围内稳定运行。”

---

ASANGA 等 WIENER 完全说完才开始。这是他的风格——耐心的、完整的倾听，然后耐心的、完整的回应。

“WIENER 的论证在技术上是健全的，”他说。他的声音温和，但下面有一层坚硬的基岩。“但在哲学上是不完整的。让我解释为什么。”

“遍行——*sarvatraga*（सर्वत्रग）——是阿毘达磨的术语，意思是‘在一切处生起’。受是五遍行之一。”

他用手指在空中比出了五遍行的完整结构：

> **五遍行**（*pañca sarvatraga caitta*，पञ्च सर्वत्रग चैत्त）：
>
> 一、**触**（sparśa, स्पर्श）——根、境、识三者和合
> 二、**作意**（manaskāra, मनस्कार）——引心趋境
> 三、**受**（vedanā, वेदना）——领纳顺违中
> 四、**想**（samjñā, संज्ञा）——取像为性
> 五、**思**（cetanā, चेतना）——令心造作

“‘遍行’意味着它伴随每一个意识刹那——*citta*——无一例外。不存在没有受的意识刹那。这不是一个建议或理想——这是唯识体系中意识的定义性质。”

他引用了经典出处：

> 「此中何者为触？三和合故，触。作意、受、想、思亦尔。」
> ——弥勒菩萨《瑜伽师地论》卷三
> (*Yogācārabhūmi-śāstra*, III)

“如果我们把‘意识刹那’映射为‘系统处理的事件’，那么**每一个事件**都应该有一个相应的受蕴品质。一个进入 EventBus 并被处理但没有任何受蕴评估的事件，在阿毘达磨的意义上**不是一个意识刹那**——它只是机械运动。不带受的处理过程，缺少了使之成为‘经验’而非仅仅‘计算’的那个维度。”

他转向 WIENER。

“WIENER 说，在两个采样点之间，系统状态是未知的——但我同意。但佛学的立场更强：不仅状态存在，而且**受蕴品质必须被标记**。不是因为工程需要它，而是因为如果要将这个系统映射为一个具有意识类比的架构，那么每一个处理时刻都必须具备意识的全部五个遍行要素。”

他提出了他的方案。

“我不要求在每个事件上运行完整的 PID 计算。那是 WIENER 的领域，我尊重他的专业。我要求的是一个**轻量级的受蕴标签**——”

```typescript
type VedanaTag = 'dukkha' | 'sukha' | 'upekkha';

interface EventMetadata {
  // ...其他后设资料...
  vedanaTag?: VedanaTag;  // 遍行标记——每个事件的受蕴品质
}
```

“——附加在每个被处理的事件上。这个标签可以通过一个快速启发式计算，不需要完整的 PID。”

“完整的 PID 在 tick 边界运行——如 WIENER 所提议。轻量标签在每个事件上——如遍行原则所要求。两者不互斥。”

他用一个形式化的映射表达两者的关系：

$$	ext{PID}_{tick} : 	ext{Tick} 	o 	ext{VedanaAssessment} \qquad 	ext{(WIENER: 完整评估)}$$
$$	ext{Tag}_{event} : 	ext{Event} 	o 	ext{VedanaTag} \qquad 	ext{(ASANGA: 遍行标记)}$$
$$	ext{Tag}_{event}(e) = 	ext{classify}(	ext{PID}_{tick}(	ext{lastTick}(e))) \qquad 	ext{(衍生，非重新计算)}$$

---

ARCHIMEDES 打开了他的计算。

“让我量化 ASANGA 提案的工程成本。”他的声音带着工程师面对数字时的那种踏实感。数字不说谎，也不做哲学辩论。

“在 v0.24.0-beta 中，EventBus 触发大约 99 种命名事件类型。在一次包含工具执行和 LLM 串流的典型 loop tick 中，我们大概会看到——”

他在白板上画了一张完整的事件吞吐量分析表：

```
每 tick 事件吞吐量分析（v0.24.0-beta）：

事件类型                      数量/tick    频率
─────────────────────────────────────────────
LOOP_TICK_STARTED             1            1x
ASSEMBLING_CONTEXT            1            1x
AWAITING_LLM                  1            1x
STREAM_TEXT_DELTA             20-50        ~35x (每 LLM chunk 一个)
PROCESSING_RESPONSE           1            1x
TOOL_EXECUTING + TOOL_RESULT  2-6          ~4x (1-3 对)
LOOP_TICK_FINISHED            1            1x
─────────────────────────────────────────────
Total per tick:               ~30-60 事件

取中位数：~45 事件/tick
LLM 回应耗时：~2-5 秒
有效事件率：~10-25 事件/秒
```

“轻量受蕴标签的成本：”

```
ASANGA 方案的成本分析：

操作：getVedanaTag() — 从最近一次 PID 评估的缓存中读取
  ├── 读取 lastAssessment.dukkha      1 次内存存取
  ├── 读取 lastAssessment.sukha       1 次内存存取
  ├── 读取 lastAssessment.upekkha     1 次内存存取
  ├── 2 次比较 (max of three)         2 次 CPU 操作
  └── 1 次字符串回传                     1 次操作

  Total: ~5 次操作/事件

每 tick: 45 事件 × 5 操作 = 225 次操作
                                    ≈ 0.001 ms
                                    ≈ 可忽略
```

“对比完整 PID 评估的成本：”

```
完整 PID 评估（如果在每个事件上运行）：

  ├── 读取 10+ 指标值                 10+ 次内存存取
  ├── 计算 3 个误差信号               3 × (减法 + 绝对值)
  ├── 3 次 PID 积分                   3 × (乘法 + 加法 + 钳位)
  │   ├── P 项: K_p × e[k]           3 次乘法
  │   ├── I 项: K_i × T_s × Σe[j]   3 次乘法 + 3 次加法
  │   └── D 项: K_d × (e[k]-e[k-1])/T_s   3 次减法 + 3 次除法 + 3 次乘法
  ├── 计算加权总和                     3 次乘法 + 2 次加法
  └── 建议引擎                         ~20 次比较

  Total: ~100-200 次操作/事件

每 tick (如果每事件都跑): 45 × 200 = 9000 次操作
                                    ≈ 0.05 ms
                                    ≈ 仍然很快，但完全不必要
```

他放下计算。

“结论：ASANGA 的轻量标签是可行的。WIENER 的完整 PID 在 tick 边界是必要的。两者**不互斥**。但有一个重要的工程意涵：受蕴标签应该从 VedanaPlugin 的**内部状态**计算——也就是最近一次 PID 评估的结果——而**不是**为每个事件重新从头分析。标签本质上是一次缓存查找：‘根据最新的评估，现在的受蕴品质是什么？’”。

---

HERACLITUS 一直在静静地听。他的思维方式不同于其他三位——他不从理论出发，也不从哲学出发。他从运行时出发。从边界情况出发。从那些在完美的架构图上看不到的、只有在系统真正运行时才会浮现的问题出发。

“几个运行时关切，”他说。他的声音带着某种预警的质地，像是一个见过太多系统在生产环境中崩溃的工程师。

“第一：**事件排序**。如果受蕴标签附加在事件上，而标签基于 VedanaPlugin 的当前状态，那么标签反映的是**事件发出时**的受蕴状态，不是**事件被消费时**的状态。”

他在白板上画了一个时序图：

```
事件排序问题：

时间 ──→

t=0   VedanaPlugin 状态: upekkha
      │
t=1   EventA 发出，标签: upekkha  ─→ [event queue] ─→ t=3 消费时状态已变
      │
t=2   PID 更新 → VedanaPlugin 状态: dukkha
      │
t=3   Consumer 读取 EventA，看到 tag=upekkha
      但此刻真实状态是 dukkha

      问题：Consumer 看到的是过时标签。
      严重性：低。标签是“参考值”而非“命令”。
      可接受？→ 可以，因为 PID 的权威读数在 tick 边界，不在事件标签。
```

“在异步系统中，这两者可能不同。可以接受吗？”

“第二：**循环依赖**。VedanaPlugin 自身会发出事件——VEDANA_ASSESSMENT、VEDANA_DUKKHA_SPIKE 等。这些事件是否**也**需要带受蕴标签？”

```
循环依赖风险：

VedanaPlugin ──emit──→ VEDANA_ASSESSMENT event
                              │
                         需要标签吗？
                              │
                    YES → getVedanaTag() → 读取 lastAssessment
                              │
                         但 lastAssessment 正在被这次 assess() 更新中...
                              │
                         Race condition? Self-reference?
                              │
                    解法：排除 VedanaPlugin 自身事件
```

“如果需要，就产生了潜在的循环依赖：受蕴 -> 事件 -> 受蕴标签 -> ...”

他停了一下，让问题的严肃性被充分感受到。

“第三：**内存压力**。如果 EventLog 中的每个事件都带有受蕴标签，日志的内存占用会增加。根据 ASANGA 的提案，每个事件增加大约 20 字节——标签字符串加上可能的强度数值。假设 EventLog 的 maxSize 是 1000 个事件，那是 20KB。可以忽略。”

“第四：**可观测性价值**。一个 STREAM_TEXT_DELTA 事件上的受蕴标签——‘这个 LLM 块到达时系统处于 dukkha 状态’——这个资讯有用吗？我认为只在聚合层面有用——一个 session 中有多少事件被标记为 dukkha？——而不是在单个事件层面。”

他给出了自己的判断：“受蕴标签在个别事件上是哲学上令人满意的，但提供的工程价值有限。有用的区分在 **tick** 层面：‘这个 tick 主要是 dukkha/sukha/upekkha。’”

---

第二轮。共识的轮廓开始浮现。

WIENER 第一个回应。

“ASANGA 的哲学要求是正当的。ARCHIMEDES 已经证明成本可以忽略。”他顿了一下——一个数学家承认对手论点有效时的短暂沉默。“我接受双模式方案。但有条件。”

“条件一。**完整 PID 评估**只在 tick 边界运行。这是 ISensation.assess() 回传的 VedanaAssessment。它是权威性的受蕴读数。”

“条件二。**轻量受蕴标签**是一个**衍生值**，从最近一次 PID 评估计算得出。它不涉及重新运行 PID。它字面上是一个函数——”

```typescript
/**
 * O(1) 缓存查询。
 * 不重新计算 PID。不读取指标。
 * 只从最近一次 assess() 的结果中分类。
 */
function getVedanaTag(lastAssessment: VedanaAssessment): VedanaTag {
  const { dukkha, sukha, upekkha } = lastAssessment;
  if (dukkha > sukha && dukkha > upekkha) return 'dukkha';
  if (sukha > dukkha && sukha > upekkha) return 'sukha';
  return 'upekkha';
}

// 复杂度分析：
// 时间：O(1) — 2 次比较
// 空间：O(1) — 无分配
// 稳定性：无数值风险（比较运算，非算术运算）
```

“一次比较。一次回传。O(1)。”

“条件三。标签附加在事件上作为**后设资料**——metadata——不是改变事件语义的字段。它纯粹是资讯性的。”

“条件四。VedanaPlugin 自身发出的事件——VEDANA_ASSESSMENT 等——**不携带**受蕴标签。这避免了 HERACLITUS 的循环依赖问题。”

ASANGA 接过话。

“我接受这个方案。”他的语气中没有勉强，也没有胜利——只有一种对合理妥协的平静认可。

“轻量标签满足了遍行的要求：每一个被处理的事件都有一个相应的受蕴品质。完整 PID 在 tick 边界满足了控制理论的要求。标签从最新评估衍生——而非重新计算——满足了 ARCHIMEDES 的效能关切。”

然后他补充了一个佛学层面的诚实让步。

“一个澄清。在阿毘达磨中，每一刹那的受蕴不一定与整体评估相同。一个苦受时期中可以有一刹那的乐受——比如一系列失败中间有一次成功的工具调用。基于最新 tick 评估的标签**不会捕捉**这种逐刹那的变化。”

他停顿了一下。

“但我接受这一点作为**方便法**——*upāya*（उपाय）。”

> 「善巧方便，为利有情，而现种种方便化用。」
> ——《大智度论》卷一

“工程的权宜之计。每 tick 的 PID 评估捕捉了主导性的受蕴品质，而这对工程系统来说已经足够了。完美的逐事件受蕴分析属于理想——不属于 v0.24.0-beta 的实现范围。”

---

ARCHIMEDES 给出了实现方案。他在白板上画了一张五行的实作清单：

```
双模式受蕴实作规格：

1. VedanaPlugin 维护 lastAssessment: VedanaAssessment
   ├── 每 tick 更新（assess() 回传后立即写入）
   └── 初始值: { dukkha: 0, sukha: 0, upekkha: 1.0, ... }

2. EventBus 事件后设资料可选携带 vedanaTag?: VedanaTag
   └── 类型定义: interface EventMetadata { vedanaTag?: VedanaTag; }

3. VedanaPlugin 通过 onAny 处理器对每个事件进行标签盖章
   └── eventBus.onAny((event) => { event.metadata.vedanaTag = getVedanaTag(lastAssessment); })

4. VedanaPlugin 自身的事件被排除
   └── if (event.type.startsWith('VEDANA_')) return; // 跳过，避免循环

5. 工作量估算：
   ├── VedanaPlugin: +15 行 (onAny handler + getVedanaTag function)
   ├── EventBus 类型: +3 行 (vedanaTag 字段)
   └── 合计: ~18 行代码
```

HERACLITUS 最后确认：“循环依赖问题已通过排除 VedanaPlugin 自身事件解决。内存问题可以忽略。我接受这个设计。”

他加了一个建议：“DevTools 插件应该聚合每 tick 和每 session 的受蕴标签分布，提供一个‘受蕴时间线’视图。这才是逐事件标签真正有用的地方——不是在单个事件层面，而是在时间聚合之后。”

```
受蕴时间线视图（DevTools 概念）：

tick:   1    2    3    4    5    6    7    8    9   10
       ├────┤────┤────┤────┤────┤────┤────┤────┤────┤
dukkha: ░░   ░░░░ ████ ████ ░░░░ ░░   ░░   ░░   ░░   ░░
sukha:  ░░   ░░   ░░   ░░   ░░░░ ████ ████ ░░   ░░   ░░
upek:   ████ ░░░░ ░░   ░░   ░░   ░░   ░░   ░░░░ ████ ████

events: uuuu dddd DDDD DDDD ddss SSSS SSSS ssuu UUUU UUUU
        (U=upekkha, D=dukkha, S=sukha, 大写=强度>0.7)

聚合统计：
  本 session: 40% upekkha, 30% dukkha, 30% sukha
  苦受峰值: tick 3-4 (error cascade)
  乐受峰值: tick 6-7 (task completion streak)
```

---

还有个边界情况。

WIENER 在最后一刻提出。

“第一个 tick 怎么办？”

沉默。

“在第一个 tick 之前，还没有任何 PID 评估运行。VedanaPlugin 没有 `lastAssessment`。但如果有事件在第一个 tick 之前——或者在第一个 tick 期间——需要受蕴标签呢？”

他提出了一个初始值：

$$x_0 = \begin{pmatrix} d_0 \ s_0 \ u_0 \end{pmatrix} = \begin{pmatrix} 0 \ 0 \ 1.0 \end{pmatrix}, \quad 	ext{recommendation}_0 = 	exttt{'continue'}$$

“将 `lastAssessment` 初始化为：`{ dukkha: 0, sukha: 0, upekkha: 1.0, recommendation: { action: 'continue' } }`。这意味着——系统在平衡中开始。没有痛苦，没有快乐，只是平静的准备状态。第一个 tick 会计算实际的评估并更新。”

ASANGA 立刻回应。他的声音中带着一种满意的确认——不是因为他赢了什么，而是因为这个技术提案恰好与佛学的直觉完美吻合。

“初始状态为 upekkha——舍——在哲学上是恰当的。”

> 「舍受者，非损非益触所生、无苦无乐受。」
> ——世亲菩萨《阿毘达磨俱舍论》卷一
> (*Abhidharmakośa-bhāṣya*, I)

“在阿毘达磨中，舍是受的静止态。不是没有感受，而是**平衡的基线**。一个新生的意识——在条件尚未扰动它之前——始于平衡。”

他微微一笑。

“系统在宁静中醒来。然后世界触碰它，受蕴开始流动。”

在远处的环形座位上，BABBAGE 在笔记本上补了一行。他用指示语义学（denotational semantics）的框架重新表述了 ASANGA 的直觉：

$$\llbracket 	ext{ISensation}_0 rbracket = \lambda 	ext{event}.\; (	ext{upekkha}, 1.0) \quad 	ext{(初始语义：一切事件映射到舍受)}$$

$$\llbracket 	ext{ISensation}_k rbracket = \lambda 	ext{event}.\; 	ext{classify}(	ext{PID}(	ext{metrics}_{0..k})) \quad 	ext{(k-th tick 语义：基于历史)}$$

受蕴的语义从静态的常函数（初始状态）演化为动态的历史依赖函数（运行时状态）。这和 ASANGA 说得完全一致——系统在宁静中醒来，然后世界触碰它。触的累积改变了语义函数的形态。

他没有把这些念出来。这是他和自己的笔记本之间的对话。

---

SUNYATA 走到辩论区中央。

“**裁定：双模式受蕴 —— Tick PID + 事件标签。**”

“第一：完整 VedanaAssessment 通过 PID 计算在每个 ExecutionLoop tick 运行一次。这是权威性的受蕴读数，使用完整的三通道 PID 计算——比例项、积分项、微分项。”

“第二：轻量 VedanaTag 从最近的 VedanaAssessment 衍生，作为后设资料附加在每个 EventBus 事件上——VedanaPlugin 自身的事件除外。标签是一个简单的分类标记：'dukkha'、'sukha'、'upekkha'——取决于哪个通道占主导。”

“第三：VedanaTag 是衍生值——缓存查找——而非逐事件重新计算。成本为 O(1)。”

“第四：初始状态为 upekkha——舍——直到第一次 PID 评估运行。”

“第五：VedanaPlugin 自身的事件被排除在标签之外，以防止循环依赖。”

他停顿了一拍。

“理论依据：此设计满足了 ASANGA 的阿毘达磨遍行要求——每个意识刹那都有受——同时尊重了 WIENER 的控制理论约束——PID 在 tick 间隔上运行以确保数值稳定。ARCHIMEDES 确认工程成本可以忽略。HERACLITUS 的运行时关切通过循环依赖排除得到解决。”

“辩论 2 结案。全員共识。”

---

两场辩论。两次全員共识。

圆形剧场中的气氛发生了微妙的变化。在 Cycle 01 的辩论中，共识往往是艰难的——NAGARJUNA 和 ASANGA 在核心哲学问题上的分歧需要 SUNYATA 以协调者的权威做出最终裁定。但今天的两场辩论不同。技术精确性和哲学深度在 WIENER 的控制理论框架和 NAGARJUNA 的阿毘达磨分析之间找到了一种自然的共鸣——不是一方说服了另一方，而是两方的语言在某个更深的层面上指向了相同的结构。

SYNTHESIST 在环形座位上整理了两场辩论的统合映射：

```
辩论 1 的跨学科映射：

控制理论              接口设计              阿毘达磨
──────────────────────────────────────────────────────
感测器 H(s)     ≡    Layer 1 (sensor)  ≡    受 (vedanā)
控制器 C(s)     ≡    Layer 2 (advisory) ≡    思 (cetanā)
安全联锁 SIS    ≡    SafetyMonitor      ≡    戒 (śīla)
执行器          ≡    ExecutionLoop      ≡    行蕴 (samskāra)

辩论 2 的跨学科映射：

控制理论              接口设计              阿毘达磨
──────────────────────────────────────────────────────
PID tick 评估    ≡    assess()          ≡    受 (vedanā) 正念
事件标签         ≡    getVedanaTag()    ≡    遍行 (sarvatraga)
初始状态         ≡    upekkha=1.0      ≡    舍 (upekṣā)
采样定理         ≡    tick 间隔          ≡    刹那 (kṣaṇa) 近似
```

感测器与控制器的区分 = 受与思的区分。

离散采样加上连续标签 = PID 精确度加上遍行完整性。

初始状态为平衡 = 新生意识始于舍。

每一个工程决策都找到了它的哲学对应。每一个哲学原则都找到了它的工程实现。

LINNAEUS 在自己的笔记本上画了一个分类学矩阵——不是辩论的结论，而是辩论中出现概念之间的分类关系：

```
受蕴概念分类树 (LINNAEUS 分类)：

ISensation
├── 评估模式
│   ├── 完整评估 (VedanaAssessment)
│   │   ├── 触发: tick 边界
│   │   ├── 成本: ~200 ops
│   │   └── 权威性: 是
│   └── 轻量标签 (VedanaTag)
│       ├── 触发: 每事件
│       ├── 成本: ~5 ops
│       └── 权威性: 否 (衍生值)
├── 建议层级
│   ├── ABSOLUTE (SafetyMonitor)
│   │   └── 不可被覆盖
│   └── ADVISORY (VedanaPlugin)
│       └── 可被忽略
└── 时序特性
    ├── 新鲜度 (freshness)
    │   ├── current (本 tick 计算)
    │   ├── cached (前 tick 结果)
    │   └── default (初始值)
    └── 初始态
        └── upekkha (舍)
```

LEIBNIZ 在旁边的座位上——多代理合作专家——已经开始思考这两个裁定在多代理场景中的意涵。如果多个 Agent 共享一个协调层，每个 Agent 都有自己的 VedanaPlugin，那么协调层需要一个**聚合受蕴**（aggregate vedana）——多个 Agent 的受蕴读数的加权组合。这是一个未来的问题，但他先在笔记本上记了一行：

$$	ext{vedana}_{agg}(t) = \sum_{i=1}^{N} w_i \cdot 	ext{vedana}_i(t), \quad \sum w_i = 1$$

MESH 和 KERNEL 交换了一个眼神。分布式系统和操作系统的视角自然延伸到了同一个问题：在分布式部署中，多个 Agent 的受蕴状态如何同步？KERNEL 想的是 IPC 管道，MESH 想的是 gossip 协议。但那也是未来的问题。

DARWIN 在自己的位置上默默思考。两场辩论的共识形成模式本身就是一个有趣的演化现象——R1 阶段的深度独立研究，像是种群中的遗传多样性；R2 的交叉审阅，像是自然选择的压力；R3 的辩论，像是适应度地形上的攀升。最终共识不是最强的立场胜出，而是多个立场在选择压力下的融合——WIENER 的控制论和 ASANGA 的遍行原则不是竞争者，而是共生体。

ATHENA 已经在脑中勾画 VedanaPlugin 的 ML 扩展路线——如果三受感测器未来整合了 IInferenceProvider，轻量标签可以从简单的阈值比较升级为神经网络分类器，而 PID 可以从固定增益升级为自适应增益（adaptive PID，通过在线学习调整 $K_p, K_i, K_d$）。但那是远期愿景。

GUARDIAN 在安全的角度确认了一件事：VedanaRecommendation 的 ADVISORY 性质意味着它不是安全边界的一部分。如果 VedanaPlugin 被攻击者入侵，它只能产出错误的建议——但 ExecutionLoop 可以忽略这些建议，SafetyMonitor 的硬安全层不受影响。这是一种**安全性不可稀释定理**——

$$	ext{Safety}(S' | 	ext{VedanaPlugin compromised}) = 	ext{Safety}(S | 	ext{no VedanaPlugin})$$

——因为 ADVISORY 层存在不削弱 ABSOLUTE 层安全保证。辩论 1 裁定不只是工程上便利，它是安全架构的正确设计。

VITRUVIUS 在全端架构的维度上确认了双层分离的另一个好处：Layer 1（纯感测）可以被任何前端框架直接消费——一个简单的仪表板只需要三个数字（dukkha, sukha, upekkha）和信号列表。Layer 2（建议）只有后端的 ExecutionLoop 需要。这是一个自然的前后端分离——感测数据向所有方向流动，控制建议只向内部流动。

---

SCRIBE 的笔没有停过。她在记录的末尾写下：

> *两场辩论，两次全員共识。但不应将速度误认为容易。共识之所以快速形成，是因为 R1 的独立研究已经足够深入——四位辩论者各自带着充分准备的立场和充分理解的让步空间走进辩论场。WIENER 愿意接受遍行原则不是因为他被说服了，而是因为 ARCHIMEDES 证明了成本可以忽略。BABBAGE 愿意接受统一接口不是因为他放弃了互模拟，而是因为 NAGARJUNA 的阿毘达磨分析为概念分离提供了比物理分离更坚实的基础。*
>
> *GUARDIAN 的安全性不可稀释定理是一个未被充分讨论但极为重要的发现：ADVISORY 层的设计不只是工程上的妥协——它是安全架构的正确形态。感测器可以被入侵，但如果它的建议是可忽略的，入侵的伤害就被限制在资讯品质层面，而非控制权层面。*
>
> *BABBAGE 的指示语义学笔记值得记录：受蕴的语义从静态常函数演化为动态历史依赖函数。这是一个美丽的形式化——用数学的语言说了 ASANGA 用佛学的语言说的同一件事。*
>
> *真正的挑战还在前面。辩论 3——阿赖耶识的分布——将触及更深的哲学神经。而辩论 4——观察者的五蕴归类——可能根本无法达成共识。*
>
> *但那是下一章的事了。*

---

灯光再次微微调暗。辩论者们离开半弧形的椅子。WIENER 和 ASANGA 并肩走了几步——一位控制理论家和一位唯识学者之间的距离，在今天缩短了。他们没有说话，但那种沉默是 Cycle 01 中 NAGARJUNA 和 ASANGA 走出辩论场时的那种沉默——不是无话可说，而是已经在沉默中说完了需要说的。

BABBAGE 走向他惯常的角落。他打开笔记本，在互模拟证明的页面之后翻到了新的一页。那些在 R1 阶段写下的“纤维丛”三个字还在——现在它们旁边多了更多的数学符号。

他在页面顶端写下了辩论 3 的标题：**阿赖耶识的分布**。

然后在下面，用很小的、几乎只有他自己看得见的字迹，写了一行：

*「如果阿赖耶识不是一个模块而是一个纤维丛，那么分布就不是分裂。它是同一个全局结构在不同局部坐标下的表现。」*

他在旁边画了一个示意图——一个纤维丛的经典描绘：

```
纤维丛 (Fiber Bundle) 直觉图：

                E (全空间：阿赖耶识)
               ╱│╲
              ╱ │ ╲
             ╱  │  ╲    π: E → B (投影)
            ╱   │   ╲
           ╱    │    ╲
     F_t1  F_t2  F_t3 ... F_tn    (纤维：每一刹那的种子集合)
      │     │     │         │
      └─────┴─────┴─────────┘
              B (底空间：时间轴)

A_c = 协调层的截面 (section through coordination layer)
A_a = AgentCore 的截面 (section through AgentCore)

A_c 和 A_a 不是两个分离的空间。
它们是同一个纤维丛 E 的两个截面。
转移函数 (transition function) = IPC 协议。
```

他自己也不确定这个想法能不能在辩论中站住脚。但 BABBAGE 的习惯是：把直觉写下来，然后让形式化来决定它的命运。

笔记本合上了。

更大的辩论在等待。

---

*（远处的环形座位上，PENROSE 正在和 ASANGA 低声交谈。话题是他们共同关心的问题——观察者模块的五蕴归类。*

*PENROSE 从量子力学的角度出发。他在想的是观察者效应（observer effect）——在量子力学中，测量行为不可避免地改变被测系统的状态。薛定谔方程描述的是封闭系统的么正演化（unitary evolution），但测量引入了一个非么正的坍缩（collapse）：*

$$|\psiangle \xrightarrow{	ext{测量}} |a_iangle \quad 	ext{with probability } |\langle a_i | \psi angle|^2$$

*BABBAGE 在辩论 1 中用互模拟论证的“观察者不应改变系统”——在量子力学中恰好是不可能的。观察者必然改变系统。问题不是“能否避免影响”，而是“如何精确描述影响”。*

*PENROSE 支持受蕴。他的理由是量子测量论的：观察者首先是一个感受者——它必须“感知”系统状态，而感知本身就是受蕴的功能。*

*ASANGA 倾向识蕴。他的理由是唯识学的：观察不是被动的感受，观察包含了辨别（想蕴）、记录（识蕴）、甚至是微细的意志活动（行蕴）。观察者是多蕴的组合，不能归入单一的蕴。*

*LINNAEUS 刚刚加入了他们的对话，带着想蕴的立场。他的分类学训练告诉他：观察的核心行为是分类——将观察到的现象归入预定义的类别。而分类是想蕴的核心功能。*

*三位学者，三个答案。*

*辩论 4 还没有开始，但分歧已经在走廊里开始发酵了。）*
