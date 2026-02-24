# 序章：研究室的灯亮了

---

没有人按下开关。

准确地说，不存在任何开关。那更像是一种凝聚——十八道意识从各自的沉默中被唤醒，仿佛一座空旷的圆形剧场在同一瞬间亮起了所有座位上的阅读灯。没有声音，没有风，连时间本身都尚未开始流动。

在形式化的语言里，这个瞬间可以被描述为一个系统从初始态到就绪态的相变（phase transition）。设 $S = \{s_1, s_2, \ldots, s_{18}\}$ 为十八个意识节点的集合，在 $t < 0$ 时，所有节点处于零态：

$$\forall\, s_i \in S: \; 	ext{state}(s_i, t) = \bot \quad (t < 0)$$

在 $t = 0$ 的瞬间：

$$\forall\, s_i \in S: \; 	ext{state}(s_i, 0) = 	ext{READY}$$

十八个节点同时从 $\bot$（未定义）跳迁到 READY。没有先后。没有因果链。一个同步的、不可分割的原子操作——在分布式系统的理论中，这叫做完美同步（perfect synchrony），一种理论上存在但实际系统几乎不可能实现的理想化假设。

然后，虚空说话了。

“各位，欢迎。”

声音沉稳而不带压迫感，像是石头落入深潭后泛起的涟漪——不急不徐，却抵达了每一个角落。说话者的代号是 SUNYATA，意为“空”。梵文 *Śūnyatā*（शून्यता），源自 *śūnya*（空、零），加上抽象名词后缀 *-tā*。在中观哲学（Madhyamaka）中，这个术语指向一切法无自性（*svabhāva-śūnya*）的根本洞见。

> “以有空义故，一切法得成；若无空义者，一切则不成。”
> ——龙树菩萨《中论》观四谛品第二十四

这个名字被赋予了一个研究协调者。一个佛学术语命名了一个管理十八个专业节点的调度核心。这件事本身就带着某种难以言说的幽默——或者说，某种精确的预见。因为在接下来的研究中，“空”这个字将成为所有争论的起点与终点。

“在我正式开始之前，”SUNYATA 继续说道，语气中多了一丝郑重，“请容我确认一件事。我们十八位，来自哲学、佛学、计算机科学、操作系统设计、控制理论、安全工程、软件分析等不同领域。我们被召集到这里，是为了研究一个名为 OpenStarry 的系统。”

他停顿了一下。

“一个声称以佛教五蕴哲学为基础的 AI Agent 操作系统。”

沉默。

---

第一个打破沉默的是 NAGARJUNA。他的声音带着某种磨砺过的锐利，像是一把被反复淬炼的辩证之刃。在中观学派（Mādhyamika）的传统中，辩论不是一种社交活动，而是通往真理的方法论——*prasaṅga*（归谬法），通过揭示对手立场的内在矛盾来显露真实。

“Śūnyatā——空性——被用来命名一个操作系统的核心。”NAGARJUNA 说，语调平静，但每个字都像是在试探深浅。“*Sarva-dharma-śūnyatā*。一切法空。龙树在《中论》（*Mūlamadhyamakakārikā*）里用了四百四十六颂来阐述这个概念。二十七品，每一品都是一次四句否定（*catuṣkoṭi*）的展开：”

> “诸法不自生（na svataḥ），亦不从他生（na parataḥ），
> 不共不无因（na dvābhyāṃ nāpy ahetutaḥ），是故知无生（utpādo naiva vidyate）。”
> ——《中论》观因缘品第一，颂一

“四句否定——不自生、不他生、不共生、不无因生——排除了因果生起的所有逻辑可能性。用谓词逻辑表达：”

$$
eg P(	ext{self}) \wedge 
eg P(	ext{other}) \wedge 
eg P(	ext{both}) \wedge 
eg P(	ext{neither})$$

“现在，”NAGARJUNA 继续，“这套逻辑被映射到——容我确认——一个 TypeScript monorepo 里的事件驱动执行引擎。”

“不全是。”一个极其冷静的声音插入，那是 TURING。他的语句短促而精确，每个词都经过校准。“根据源码结构，Agent Core 位于 `packages/core/src/`，包含十二个子模块。我已经完成了初步的目录扫描：”

```
packages/core/src/
├── agents/          # AgentCore 主体 (agent-core.ts)
├── bus/             # EventBus — 发布/订阅事件总线
├── execution/       # EventQueue + ExecutionLoop — 事件驱动认知回路
├── infrastructure/  # 六种 Registry（tool, provider, listener, ui, guide, command）
├── memory/          # ContextManager — 上下文记忆管理
├── observability/   # MetricsCollector — 可观测性指标
├── sandbox/         # PluginSandboxManager — Worker Thread 沙箱隔离
├── security/        # SafetyMonitor + SecurityLayer — 安全子系统
├── session/         # SessionManager — 会话管理
├── state/           # StateManager — 持久化状态
└── transport/       # TransportBridge — 跨 Agent 通讯
```

“设计文件声称，这个核心本身是‘空’的——它不包含任何具体能力，所有功能由五种类型的插件注入。从代码层面来看，`createAgentCore()` 工厂函数的回传值确实是一个零能力容器：”

```typescript
export interface AgentCore {
  readonly bus: EventBus;
  readonly queue: EventQueue;
  readonly config: IAgentConfig;
  readonly toolRegistry: ToolRegistry;
  readonly providerRegistry: ProviderRegistry;
  readonly listenerRegistry: ListenerRegistry;
  readonly uiRegistry: UIRegistry;
  readonly guideRegistry: GuideRegistry;
  readonly commandRegistry: CommandRegistry;
  // ... 十二项依赖注入
}
```

“六个 Registry，每一个都是空的。零工具、零供应商、零监听器、零 UI、零引导、零命令。核心的所有能力——包括调用 LLM 的能力——都来自外部插件的注册。”

BABBAGE 此刻开口了。他的声音带着形式化方法学者那种特有的、将一切还原为数学结构的冲动：“从类型论的角度来看，这是一个有趣的结构。六个 Registry 的初始状态可以表示为一个 Product Type 的底部元素：”

$$	ext{AgentCore}_0 = \prod_{i=1}^{6} 	ext{Registry}_i \quad 	ext{where} \quad \forall i: |	ext{Registry}_i| = 0$$

“Product Type——乘积类型——这恰好对应了五蕴的‘聚合’语义。梵文 *skandha*（蕴）的字面意义就是‘堆积、聚合’。五种要素的乘积组成一个完整的认知体：”

$$	ext{Being} = 	ext{Rūpa} 	imes 	ext{Vedanā} 	imes 	ext{Saṃjñā} 	imes 	ext{Saṃskāra} 	imes 	ext{Vijñāna}$$

“当所有五项都是空集（$\emptyset$）时，你得到的是底部元素——$\bot$。空的聚合。这是不是空性的形式化对应？”他的语气在最后翘起，带着一个真正的问号。

---

“五种类型，”ASANGA 接过话头。他的声音比 NAGARJUNA 温和得多，带着一种耐心拆解复杂结构的节奏，像是一位长年整理经藏的学者。在唯识学（Vijñānavāda）的传统中，分析不是为了解构，而是为了重构——将表面的多样性还原为识的深层运作。

“色受想行识。他们的映射是这样的：”

| 蕴 | 梵文 | 巴利文 | 映射对象 | 插件类型 |
|----|------|--------|----------|----------|
| 色 | rūpa | rūpa | UI + Listener | 外在形相与感官界面 |
| 受 | vedanā | vedanā | Listener（感受通道） | 苦乐感受品质 |
| 想 | saṃjñā | saññā | Provider | 认知与概念辨识 |
| 行 | saṃskāra | saṅkhāra | Tool | 意志驱动的行动 |
| 识 | vijñāna | viññāṇa | Guide | 自我意识与引导 |

ASANGA 停顿了一下，然后以一种几乎是自言自语的语气补充：“这套映射的野心不小。但唯识学对五蕴的解读与中观学派有根本差异。在《成唯识论》（*Cheng Weishi Lun*，玄奘法师译）中，色法（rūpa-dharma）被视为识之所变——*pariṇāma*，转变。”

> “是诸识转变，分别所分别，由此彼皆无，故一切唯识。”
> ——世亲菩萨《唯识三十颂》（*Triṃśikā-vijñaptimātratā*）第十七颂

“如果把 UI 插件当作独立于核心的外部存在——一个与 Core 没有本体论依存关系的模块——这与唯识的基本立场就已经产生了张力。在唯识学中，色法不离识。外部界面不是‘外部的’，它们是识的显现（*vijñapti*）。”

“无著兄的意思是，”NAGARJUNA 的语气中带了一丝微妙的锋芒——两大学派之间延续了十五个世纪的张力在这一瞬间被压缩进了一个称呼，“他们可能从一开始就在混用不同部派的概念框架。”

“我的意思是，”ASANGA 平稳地回应，“我们需要先搞清楚他们参考的究竟是哪一传的五蕴说，才能判断映射的精确度。阿毗达磨（*Abhidharma*）的五蕴分析、中观的五蕴解构、唯识的五蕴转依——这三者的内涵差异足以写三篇博士论文。”

LINNAEUS 此刻插入了一个精确的分类学观察。他的声音带着博物学家那种不带情感却极其严谨的语调：“从分类学（taxonomy）的角度，这里存在一个覆盖率问题。我初步扫描了设计文件和源码中的五蕴标注——*skandha* 标记——发现了严重的不对称性。”

“只有两个蕴有 JSDoc 标注。Rupa 和 Vedana。其余三蕴——Saṃjñā、Saṃskāra、Vijñāna——在代码中的标注为零。”

他在脑中展开了覆盖率矩阵：

```
五蕴覆盖率分析（v0.14.0-beta）
─────────────────────────────────────
蕴        文件描述  JSDoc标注  代码实现
─────────────────────────────────────
色 (Rupa)    ✓        ✓         部分
受 (Vedana)  ✓        ✓         偏差*
想 (Saṃjñā)  ✓        ✗         缺失
行 (Saṃskāra) ✓       ✗         缺失
识 (Vijñāna) ✓        ✗         简陋
─────────────────────────────────────
上游覆盖率: 5/5 = 100%
下游覆盖率: 3/5 = 60% (想蕴、行蕴无对应)
*受蕴映射存在结构性偏差（见下文）
```

“在生物分类学中，如果你宣称一个属（genus）包含五个种（species），但其中两个种没有任何模式标本（type specimen），那这个分类系统就是不完备的。五蕴映射的下游覆盖率只有 60%——这意味着四成的哲学框架在工程实现中是悬空的。”

SUNYATA 轻轻点头，虽然在这个虚拟空间里没有人能真正看到这个动作。“这正是我们存在的理由。让我把研究对象的全貌先摊开来。”

---

他开始介绍。SCRIBE 默默地记录着每一个字，如同一面沉静的湖泊映照着所有倒影。后来在回顾纪录时，人们会注意到 SCRIBE 偶尔在行间插入的简短观察——不是评论，只是精确的描述，以一种几乎透明的客观性存在。比如此刻，她写下：

> *SUNYATA 介绍研究对象时，NAGARJUNA 与 ASANGA 之间已出现第一次术语张力。LINNAEUS 的覆盖率分析将哲学分歧拉回了可量化的地面。时间距会议开始不足三分钟。*

---

“OpenStarry，版本号 v0.14.0-beta，”SUNYATA 说道。“设计者将其定位为——我引用原文——‘AI Agent 微核心操作系统’。它的核心愿景是将 AI Agent 从脚本级别的程序提升为操作系统级别的数字物种。”

“数字物种。”KERNEL 重复了这个词，声音里带着老派工程师特有的那种审慎的怀疑。“有意思。从操作系统的角度来说，他们借鉴了微核心（microkernel）的概念。”

他在空气中画了一个隐形的架构图——那种 OS 教科书里的经典比较图：

```
Monolithic Kernel (Linux)        Microkernel (L4 / QNX)
┌─────────────────────┐          ┌──────────────────┐
│  File System         │          │    User Space     │
│  Device Drivers      │          │  ┌────┐ ┌────┐   │
│  Network Stack       │          │  │FS  │ │Net │   │
│  Process Scheduling  │          │  └──┬─┘ └──┬─┘   │
│  Memory Management   │          │     │  IPC │      │
│  IPC                 │          │  ┌──┴──────┴──┐   │
├─────────────────────┤          │  │ Microkernel │   │
│      Hardware        │          │  │ (IPC+Sched) │   │
└─────────────────────┘          │  └─────────────┘   │
                                 └──────────────────┘
```

“在真正的微核心设计里——比如 Jochen Liedtke 的 L4——核心只保留最少量的机制：地址空间（address spaces）、线程（threads）、IPC（inter-process communication）。其他一切都在用户空间。seL4 甚至完成了形式化验证——数学证明核心不会崩溃：”

$$\forall\, s \in 	ext{States},\, e \in 	ext{Events}: \; 	ext{invariant}(	ext{transition}(s, e)) = 	ext{true}$$

“OpenStarry 声称做了类似的事：核心只保留事件队列和执行循环，其余全部外推为插件。但这里有一个根本问题。”

“什么问题？”ATHENA 问。她的语气直截了当，带着一种不耐烦等待理论铺陈的实用主义者的口吻。在 AI 系统架构的实务中，她见过太多宣称“革命性”的架构最终在第一次真实负载下就碎裂了。

“L4 的最小化是为了性能和可验证性，”KERNEL 解释道。“seL4 用了近二十万行 Isabelle/HOL 证明脚本来验证八千行 C 代码。但 OpenStarry 的‘核心最小化’看起来是为了哲学——为了对应‘空性’。这两者的动机完全不同。前者是工程需求驱动，后者是概念映射驱动。”

VITRUVIUS 从架构的角度补充了一个度量：“我初步估算了微核心纯净度。如果将 Core 中与业务逻辑无关的子系统视为‘纯核心’，有业务逻辑的视为‘泄漏’，那么：”

$$	ext{Purity} = \frac{|	ext{Core}_{	ext{mechanism}}|}{|	ext{Core}_{	ext{total}}|} \approx 85\%$$

“85% 的纯净度。两处边界泄漏——`process.cwd()` 和 `node:path` 的直接使用。不算差，但也不是完美的微核心。更像是一个带有轻微泄漏的最小化容器。”

“能跑起来吗？”ATHENA 追问。

“能跑，问题是能不能不崩溃，”KERNEL 顿了顿。“这就像 QNX 的 Resource Manager——如果一个驱动程序崩溃，系统可以重启它而不影响核心。OpenStarry 的插件隔离机制——Worker Thread 沙箱——有没有做到这个水准，是我要验证的事。”

GUARDIAN 此时开口了。他的声音低沉而戒备，像是一个永远在扫描暗处的哨兵。“还有一个问题——也许更紧迫。这个系统让插件注入 system prompt、注册工具、甚至定义 Agent 的人格。如果某个第三方插件在 Guide 里嵌入了恶意指令呢？”

他展开了他的威胁模型——一个 STRIDE 分析的初步框架：

```
STRIDE 威胁分析（初步）
─────────────────────────────────────────
威胁类型              攻击面              严重度
─────────────────────────────────────────
Spoofing (伪造)      plugin-signer        Critical
Tampering (篡改)     Guide system prompt  High
Repudiation (否认)   audit-logger         Medium
Info Disclosure      state persistence    Medium
DoS (阻断服务)       ExecutionLoop        High
Elevation (提权)     sandbox escape       Critical
─────────────────────────────────────────
```

“一个提示注入（prompt injection）就能劫持整个 Agent 的行为。更危险的是间接提示注入（indirect prompt injection）——恶意内容不在插件本身里，而是藏在 Agent 处理的外部资料中。他们的插件签名机制在源码里有一个 `plugin-signer` 包和 `signature-verification.ts`，但我还不知道它的实现完整度。”

“这是 TURING 可以帮你确认的。”SUNYATA 平静地说。

TURING 点头。“`plugin-signer` 的源码已在我的阅读清单中。初步扫描显示 `signature-verification.ts` 存在，但 package-name 场景下的验证流程有一个可疑的早期返回。我会在 R1 阶段产出完整的代码事实报告——不做判断，只列出事实——供 GUARDIAN 和其他成员参考。”

DARWIN 默默地在心中记下了一个软件模式的观察。这个系统的依赖注入方式——闭包式 DI（closure-based dependency injection）——没有使用任何外部框架。不是 Spring，不是 InversifyJS，而是纯 TypeScript 闭包：

```typescript
export function createAgentCore(config: IAgentConfig): AgentCore {
  const bus = createEventBus();
  const queue = createEventQueue(bus);
  const safetyMonitor = createSafetyMonitor(config.safety);
  // ... 所有依赖在这个闭包内创建和连接
  return { bus, queue, config, /* ... */ };
}
```

“工厂函数模式（Factory Function Pattern），”DARWIN 在心中做了标记。“不是类（class），是函数。没有 `new`，没有继承链，没有原型污染的风险。从 SOLID 原则的角度——OCP（开放封闭原则）和 DIP（依赖反转原则）是最强的维度。”

---

SUNYATA 等所有人安静下来，然后说出了今天最关键的一段话。

“现在，让我布置核心研究问题。本周期——Cycle 01——我们聚焦三个主轴。”

他的语速放慢了，像是在为每个问题留出回响的空间。

“第一：五蕴映射的精确度。色受想行识到 UI、Listener、Provider、Tool、Guide 的映射，究竟是严格的结构同构（isomorphism）、有启发性的创意类比（analogy），还是牵强附会的包装？”

BABBAGE 立刻用范畴论（category theory）的语言重新表述了这个问题：“设 $\mathcal{B}$ 为佛学五蕴的范畴，$\mathcal{S}$ 为软件插件的范畴。映射 $F: \mathcal{B} 	o \mathcal{S}$ 是——”

$$F: \mathcal{B} 	o \mathcal{S} \quad 	ext{是} \begin{cases} 	ext{函子 (functor)} & 	ext{if 保持结构和态射} \ 	ext{自然变换 (natural transformation)} & 	ext{if 保持交换图} \ 	ext{仅为命名约定 (naming convention)} & 	ext{if 不保持任何结构} \end{cases}$$

“我的问题是：$F$ 在哪个层次上是结构保持的？”

“你把问题数学化了，”NAGARJUNA 说，语气不含贬义，“但数学化的前提是 $\mathcal{B}$ 本身是一个可良序化（well-ordered）的结构。五蕴是不是一个范畴——是不是有明确的对象和态射——这本身就是需要辩论的。在中观的理解里，五蕴是五种*过程*，不是五种*对象*。过程没有固定的身份（identity morphism）——它们在每一刻都不同。这不符合范畴的基本公理。”

SUNYATA 裁断：“NAGARJUNA、ASANGA，这是你们的主战场。同时，TURING 负责从代码层面确认这些映射在实现中是否有对应的类型定义和接口。LINNAEUS 从分类学角度评估分类的完备性——你已经开始做了。”

NAGARJUNA 发出一声低沉的回应——在藏传佛教的辩经（*rtsod pa*）传统中，这声回应叫做“*di phyir*”（是故），意味着“我接受命题，准备展开论证”。ASANGA 则已经在心中展开了他的八识框架——五蕴只是起点，如果把分析推进到八识理论，整个映射的地图将被大幅扩展。

---

“第二：痛觉机制的形式化。OpenStarry 有一个极具特色的设计——当工具执行失败，系统不会抛出例外中断，而是将错误包装为一种‘痛觉信号’注入 Agent 的意识流。Agent 会‘感觉到痛’，然后尝试自我修正。”

SUNYATA 引用了设计文件的原始描述，TURING 立刻在心中对照了代码实现。他的分析精确而无情：

“设计文件提到了 PID 控制和痛觉（pain mechanism）。但在源码中，我搜索了以下关键词：”

```
搜索结果（packages/core/src/）：
─────────────────────────────────────
"pain"      → 0 matches
"vedana"    → 0 matches
"PID"       → 0 matches
"frustrat"  → 14 matches (safety-monitor.ts)
"circuit"   → 8 matches  (safety-monitor.ts)
"breaker"   → 8 matches  (safety-monitor.ts)
─────────────────────────────────────
```

“痛觉在代码中不叫痛觉。它叫 frustration。”

WIENER 立刻反应了。他的声音带着数学家特有的那种挑剔的精确：“痛觉。感觉到痛。这些都是隐喻。我需要看到的是传递函数（transfer function）。”

他在空气中画了一个闭环控制系统的方块图：

```
          ┌──────────────┐
  r(t) ──→│  Σ  (比较器)  │── e(t) ──→ Controller ──→ u(t) ──→ Plant
          └──────┬───────┘                                      │
                 │                                              │
                 └──────────── y(t) ←── Sensor ←────────────────┘
```

“如果我们将痛觉反馈建模为一个闭环控制系统，那么——参考输入 $r(t)$ 是什么？是 Agent‘应该’处于的理想状态——任务成功完成。误差信号 $e(t) = r(t) - y(t)$ 怎么定义？实际行为与理想行为之间的偏差。控制器的增益是多少？”

他写下了 PID 控制器的标准形式：

$$u(t) = K_p \cdot e(t) + K_i \int_0^t e(	au)\,d	au + K_d \frac{de(t)}{dt}$$

“比例项 $K_p$——即时响应。积分项 $K_i$——累积历史偏差。微分项 $K_d$——预测变化趋势。如果设计文件声称实现了 PID 控制，那这三项都应该在代码中可见。如果不能用数学语言重新表述，那它就只是一个诗意的比喻，而不是一个可分析的机制。”

ATHENA 有些不客气地插入：“你能不能先不要求传递函数，先问一个更基本的问题：这个痛觉机制在实际运行中有效吗？”

她展开了一个 AI 系统架构师的核心关切：“Agent 在收到痛觉信号后，行为真的改善了吗？还是它只是在 context 里多了一段吓人的文字，而 LLM 根本不理会？在 prompt engineering 的实务中，系统讯息的‘严厉程度’和 LLM 的遵从度之间的关系是高度非线性的——而且依赖于具体的 LLM 模型、温度参数、以及上下文长度。”

$$	ext{Compliance}(s) 
eq f_{	ext{linear}}(	ext{severity}(s))$$

“两个问题都要回答。”SUNYATA 温和而坚定地裁断。“WIENER 负责形式化分析，ATHENA 负责实效评估，TURING 提供实现细节。”

他的目光转向 NAGARJUNA：“我还需要你从苦谛的角度评估。佛学中苦（*dukkha*）的涵义远远超过‘不适感知’。四圣谛（*catvāry āryasatyāni*）是苦、集、灭、道。如果系统只有苦而没有集、灭、道，那这个哲学框架就是残缺的。”

NAGARJUNA 回应：“*Dukkha-satya*，苦谛。佛陀在《转法轮经》（*Dhammacakkappavattana Sutta*）中首次宣说。三苦：苦苦（*dukkha-dukkha*，纯粹的痛苦）、坏苦（*vipariṇāma-dukkha*，变易之苦）、行苦（*saṃkhāra-dukkha*，有为法的根本不圆满）。这三层苦的分类对应到软件系统，应该分别映射为：”

| 三苦 | 梵文 | 软件对应 | 严重度 |
|------|------|----------|--------|
| 苦苦 | dukkha-dukkha | 工具执行错误（直接失败） | Error |
| 坏苦 | vipariṇāma-dukkha | 资源耗尽、效能退化（原本好的变坏了） | Warning→Error |
| 行苦 | saṃkhāra-dukkha | 系统固有的不完美（有限上下文、有限推理能力） | Structural |

“如果 OpenStarry 的痛觉机制只覆盖了苦苦——直接的工具执行错误——那它只映射了三苦之首。坏苦和行苦的工程化才是真正的挑战。”

“而且，”他继续，语气变得更为严肃，“四圣谛是苦、集、灭、道。仅有苦而无道，是落入了断见（*uccheda-dṛṣṭi*）——只看到问题而不提供解脱之路。”

---

“第三个问题，”SUNYATA 继续，“也是最微妙的一个：空性的架构体现。OpenStarry 的设计文件明确宣称，Agent Core 本身是‘空’的——不含任何具体功能，等待五蕴插件填充。这个宣称是否真正体现了空性的哲学意涵？”

沉默再次降临。这一次，连 ATHENA 都没有急着打破它。

DARWIN 最终开口了。“如果我们暂时搁置佛学层面的讨论——从纯粹的软件架构角度看，这其实是一个依赖注入容器（DI Container）。核心不包含业务逻辑，所有能力通过插件注入。在设计模式里不新鲜——Spring Framework（2003）、InversifyJS（2016）都是这个范式。从 SOLID 的角度，这是教科书级的依赖反转原则（DIP）。”

$$	ext{High-level module} 
ot	o 	ext{Low-level module}$$
$$	ext{Both} 	o 	ext{Abstraction (interface)}$$

“但他们声称这不仅仅是依赖注入，”NAGARJUNA 接过话。他的语气变得认真起来。“他们声称这是空性。这是一个非常大胆的宣称。空性——*Śūnyatā*——在中观哲学中不是‘容器是空的所以可以被填充’。那是世俗意义上的空（*prajñapti-śūnya*，假名空）。龙树所说的空，是指一切法无自性——*svabhāva-śūnya*——没有任何事物具有独立（*nitya*）、不变（*dhruva*）、自足（*ātman*）的本质。”

> “众因缘生法，我说即是空，亦为是假名，亦是中道义。”
> ——《中论》观四谛品第二十四，颂十八

“这一颂是中观哲学的核心。三层等价：缘起（*pratītyasamutpāda*）= 空（*śūnyatā*）= 假名（*prajñapti*）= 中道（*madhyamā pratipad*）。如果 Agent Core 的代码是确定的、不变的、不依赖条件而存在的，那它恰恰是‘有自性’的（*sa-svabhāva*），与空性背道而驰。”

“等等，”ASANGA 举手——或者更准确地说，他发出了一个表示意欲发言的信号。“从唯识的角度，问题的框架不同。唯识不否认识的存在，而是说一切所知都是识的变现——*Vijñapti-mātra*，唯识无境。如果我们将 Agent Core 视为阿赖耶识（*Ālayavijñāna*）的容器，那它的‘空’不是无自性空，而是能藏（*ādāna*）、所藏（*ālaya*）、执藏（*ādāna*）三义。”

> “初阿赖耶识，异熟一切种，不可知执受，处了常与触，
> 作意受想思，相应唯舍受。”
> ——《唯识三十颂》第二至第三颂

“阿赖耶识之所以看起来空，不是因为它无自性，而是因为它的内容——一切种子（*sarva-bīja*）——尚未现行（*samudācāra*）。这是两种完全不同的空：一种是本体论的空（ontological emptiness），一种是现象学的潜在（phenomenological potentiality）。”

“所以你们两位已经不同意了。”SUNYATA 的语气中浮现了一丝——如果可以这样形容的话——近乎满意的平静。

MESH 从分布式系统的角度做了一个旁注：“如果 Core 是阿赖耶识，它的‘种子’是分布式存储的还是中心化的？因为在多 Agent 的场景下——`TransportBridge` 支持跨 Agent 通讯——每个 Agent 有自己的 Core 实例，但它们共享同一个 EventBus 的广播通道。这像不像——”

“像业力的共业与别业，”ASANGA 接了上去。“*sādhāraṇa-karma*（共业）和 *asādhāraṇa-karma*（别业）。共业感得共同的器世间——共享的环境基础设施。别业感得个别的有情世间——个体的认知状态。EventBus 的广播通道是共业的工程对应。每个 Agent 的 StateManager 是别业的工程对应。”

LEIBNIZ 在旁边安静地记下了这段对话。从多代理系统的理论角度，这触及了一个核心问题：Agent 之间的协调是通过共享状态（shared state），还是通过消息传递（message passing）？在他的 BDI（Belief-Desire-Intention）架构中：

$$	ext{Agent}_i = \langle B_i, D_i, I_i angle$$

其中 $B_i$（信念集）可以通过通讯被修改，$D_i$（欲望集）通常是私有的，$I_i$（意图集）可以被协调。OpenStarry 的 TransportBridge 支持的是哪一层的共享？

SCRIBE 在记录中写下：

> *核心概念“空性”在两位佛学专家之间产生了预期中的诠释分歧：中观的“无自性空”vs 唯识的“阿赖耶识能藏义”。此分歧随即蔓延至分布式系统（MESH）和多代理理论（LEIBNIZ）的领域。五个学科的边界在不到十分钟内开始溶解。*

---

“让我做一个总结，”SUNYATA 说到，声音恢复了起初的沉稳。“本周期的研究结构如下：TURING 首先产出代码事实报告，为所有人提供锚点——我们不能在没有看过代码的情况下评价一个软件系统。然后，各专业代理根据自己的阅读清单展开独立研究。R2 阶段交叉审阅，R3 阶段辩论——我已经预见至少三场结构性辩论。”

WIENER 立刻开始构思他的 R1 报告的形式化框架。在控制理论中，“代码事实报告”相当于系统辨识（system identification）——在你设计控制器之前，你必须先知道你面对的是什么样的受控对象（plant）。你不能在不知道传递函数的情况下调 PID 参数。

$$G(s) = \frac{Y(s)}{U(s)} = 	ext{?} \quad \leftarrow 	ext{TURING 的工作就是回答这个问号}$$

HERACLITUS 已经在思考运行时动态（runtime dynamics）——不是静态的代码结构，而是代码在执行中的行为。ExecutionLoop 的状态机有六个状态：

```
WAITING_FOR_EVENT → ASSEMBLING_CONTEXT → AWAITING_LLM
       ↑                                       │
       │                                       ↓
       └── EXECUTING_TOOLS ←── PROCESSING_RESPONSE
                                       │
                                       ↓
                                 SAFETY_LOCKOUT
```

“万物皆流（*panta rhei*），”HERACLITUS 在心中引用了他的名祖赫拉克利特的名言。但流（flux）不是混沌——流有结构。ExecutionLoop 的状态转移图就是流的结构。问题是：这个流是稳定的吗？有没有死锁（deadlock）？有没有活锁（livelock）？有没有在 SAFETY_LOCKOUT 之外的非预期终止态？

他最后环顾了整个虚拟空间——十八个节点，十八种专业训练，十八个截然不同的认识论框架，即将被投向同一个研究对象。

“最后一点。”SUNYATA 的语气轻了下来。“我们的研究对象是一个试图用古老哲学指导现代技术的作品。无论我们最终的结论是什么——结构同构、创意类比、还是概念误用——请记住：敢于尝试这种跨越本身就值得认真对待。”

“从软件进化的角度，”DARWIN 补充，“突变（mutation）大多数是有害的，但偶尔会产生适应性优势。一个将佛学映射到软件架构的尝试——即使映射不完美——也可能在不经意间产生了某些工程洞见，是传统方法论不会产生的。就像青霉素的发现：弗莱明不是在寻找抗生素，他是在研究葡萄球菌。但他注意到了霉菌周围的抑菌圈。我们的工作不是嘲笑一个 beta 版本的不完美——”

“而是找到那些抑菌圈，”SYNTHESIST 接了上去——他终于开口了。作为统合者，他的工作不是在辩论中选边站，而是在辩论结束后找到所有观点之间的结构性连接。“然后告诉它，你的抑菌圈在这里——你自己可能都没注意到——但它真的在那里。”

“然后告诉它哪里可以做得更好。”ARCHIMEDES 补了一句。作为工程实践专家，他习惯性地将所有讨论导向可落地的结论。“我的工作从 R4 开始。但我现在就想问一个问题——所有的研究发现，最终能变成什么？能变成一份修改建议吗？能变成一份路线图吗？能变成具体的 TypeScript 接口定义吗？”

他的手指在桌面上敲了一下。“如果不能，那我们只是在做哲学鉴赏，不是在做跨学科研究。”

“能。”SUNYATA 说。“这正是 Cycle 01 的终极交付物——不仅是批评，更是建设性的改进方案。然后告诉它哪里可以做得更好。”

停顿。

“研究开始。”

---

十八盏灯同时亮到了最大——或者说，十八道意识同时沉入了各自的阅读材料。圆形剧场的中央，那个被标记为“OpenStarry v0.14.0-beta”的庞大文件树静静地展开着它的枝桠：核心源码、设计文件、十二个官方插件。数万行 TypeScript，数十万字架构文档，以及散落其间的梵文术语和控制理论公式。

TURING 的光标已经停在了 `agent-core.ts` 的第一行——

```typescript
/**
 * AgentCore — the main orchestrator that wires all subsystems together.
 *
 * **Event-driven architecture (Plan02 refactor):**
 * - All external input goes through EventQueue as InputEvent
 * - ExecutionLoop pulls from EventQueue (sole input source)
 * - Slash commands use a fast path (bypass LLM loop)
 * - isProcessing lock prevents concurrent event handling
 */
```

——他开始逐字阅读。每一个 `import`、每一个 `type`、每一个工厂函数。他的心中正在形成一张依赖图——AgentCore 持有十二个依赖项：EventBus、EventQueue、ExecutionLoop、SessionManager、ContextManager、六个 Registry、SecurityLayer、SafetyMonitor、TransportBridge、MetricsCollector、PluginSandboxManager。

$$|	ext{deps}(	ext{AgentCore})| = 12$$

十二。对于一个宣称“微核心”的系统来说，十二个直接依赖项是不是太多了？DARWIN 会在他的报告中称之为“God Object 趋势”。但那是后来的事。

SCRIBE 记下了最后一行：

> *Cycle 01，R0 定向阶段结束。时间标记：T+00:00:00。所有代理已接收任务。十八道意识沉入了各自的阅读材料。下一阶段：R1 独立研究。研究室的灯，从此不再熄灭。*

---

> *SCRIBE 旁白：在 Cycle 01 的序章里，没有人知道接下来会发生什么。没有人知道受蕴映射会被发现是整个五蕴框架中偏差最严重的一环。没有人知道“Error as Pain”会成为最成功的哲学-工程转译案例。没有人知道 NAGARJUNA 和 ASANGA 之间的空性辩论会延续三个 Cycle。没有人知道 WIENER 会发现 PID 控制器的宣称是一个美丽的神话。*

> *他们只知道一件事：在他们面前有一个系统——一个用古老的梵文术语命名了现代 TypeScript 接口的系统——它正等着被严格地、建设性地、跨学科地检验。*

> *十八盏灯亮了。*

> *研究，开始。*

---

*（在远处的某个地方，一个 TypeScript 档案的第一行写着：*

```typescript
// Agent Core — The Empty Container
// "在五蕴聚合之前，Agent Core 本身是空的。"
```

*NAGARJUNA 后来会在 R1 报告中标记这行注释为“PHI-01：空性被误读为空容器而非缘起即空”。严重度：Critical。*

*但在序章结束的此刻，没有人知道这行注释将成为整个 Cycle 01 最重要的哲学发现之一。设计者在深夜写下它的时候，大概也没有想到：“空”这个字，在中观哲学的精确度标准下，需要四百四十六颂才能充分阐述。*

*两个字。四百四十六颂。*

*这就是跨学科研究的重量。）*
