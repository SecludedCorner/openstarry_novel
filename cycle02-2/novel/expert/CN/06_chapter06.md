# 第六章：五棵树的根系

---

SUNYATA 在剧场中央站了片刻，什么都没说。

A 类用了三个章节修正哲学。B 类用了一个章节落实裁定。那些是拆解和决策。现在要做的事情不同。

现在要建造。

不是修补裂缝。不是重画边界。是从修正过的地基上，逐蕴展开完整的类型定义体系。A 类告诉你哪里是错的。B 类告诉你怎么修。C-1 告诉你修完之后，整个结构长什么样。

---

“C-1。五蕴子类别扩展设计。”

他拿起 Master 的信，找到那一段。

“‘五蕴可以作为面向对象中的根本类别（Root Class），要如何扩展，可以做更详细的安排。’”

他顿了一下，又读了第二段。

“‘五蕴聚合是必须要具备一个或是多个，或是复杂的控制理论（十二因缘）。但如果是单纯单一的蕴，理论上应该是不完备的。’”

他放下信。“前四章修正了地基。现在，C-1 要在修正过的地基上，把五棵树从种子长成有根、有干、有枝的完整生命体。”

他看向 TURING。“让我们先看看种子现在长什么样。”

---

> *SCRIBE 旁白：SUNYATA 用了“五棵树”的意象。不是墙壁和柱子——那些是死的建材。树是活的。树有根，根会伸展。树有枝，枝会分叉。五蕴的扩展不是静态的堆砌——它是有机的、向多个方向同时展开的生长。而且树还有一个特性：每一棵都不一样高，不一样粗，不一样弯曲。五棵树不可能对称。*

---

TURING 的屏幕投射到剧场中央。冷光。白底。黑字。

他打开的不是某份文件的摘录。是 v0.24.0-beta 的 `aggregates.ts` 源代码——完整的、未经筛选的、107 行原文件：

```typescript
/**
 * Five Aggregates (五蕴) Root Interfaces.
 *
 * These interfaces establish the philosophical-architectural foundation
 * of OpenStarry, mapping Buddhist Five Aggregates to software patterns.
 *
 * D-02 Decision: Dual naming — English as primary, Sanskrit as annotation.
 *
 * @module aggregates
 */

export interface ISensory {
  /** @skandha rupa */
  readonly skandha: 'rupa';
}

export interface ISensation {
  /** @skandha vedana */
  readonly skandha: 'vedana';
}

export interface ICognition {
  /** @skandha samjna */
  readonly skandha: 'samjna';
}

export interface IAction {
  /** @skandha samskara */
  readonly skandha: 'samskara';
}

export interface IIdentity {
  /** @skandha vijnana */
  readonly skandha: 'vijnana';
}

export type Skandha = 'rupa' | 'vedana' | 'samjna' | 'samskara' | 'vijnana';

export function isSkandha<S extends Skandha>(
  obj: unknown,
  skandha: S,
): obj is { skandha: S } {
  return (
    typeof obj === 'object' &&
    obj !== null &&
    'skandha' in obj &&
    (obj as { skandha: unknown }).skandha === skandha
  );
}
```

TURING 让投影停了整整十秒。五个根接口，每一个只有一个字段——`readonly skandha`。一个标签。一个名字。五个只写了门牌的空盒子。

“五个根接口。没有方法。没有行为定义。没有子接口继承。”

他指向 `IIdentity` 的那一段——JSDoc 里写着 `Identity aggregate encompasses consciousness and ego framework`，好像一个三行的空壳能“涵盖”意识和我执框架。

“更严重的问题在这里。”

他切换到第二张投影。

```typescript
// v0.24.0-beta 的现有具体接口（分散在不同文件中）
export interface IUI { ... }       // 色蕴？未继承 ISensory
export interface IListener { ... } // 色蕴？未继承 ISensory
export interface IProvider { ... } // 想蕴？未继承 ICognition
export interface ITool { ... }     // 行蕴？未继承 IAction
export interface IGuide { ... }    // 识蕴？未继承 IIdentity
```

“现有的具体接口。它们各自有完整的方法定义——IUI 有 `renderText`、`renderDelta`；IProvider 有 `chat`、`listModels`；ITool 有 `execute`。但它们和五个根接口之间没有任何关系。没有 `extends`。没有继承。”

他在屏幕上画了一条虚线。“门牌和门是分开的。你知道 IUI 应该属于色蕴，但类型系统不知道。你调用 `isSkandha(myUI, 'rupa')` 会返回 `false`——因为 `myUI` 对象上根本没有 `skandha` 字段。”

BABBAGE 在笔记本上写了一行：

$$	ext{roots} \cap 	ext{children} = \varnothing$$

根和子类别之间是空集。孤儿。在数学中，一棵树 $T = (V, E)$ 如果根节点 $r$ 和所有叶节点之间不存在边，那它根本不是一棵树——它是一个不连通的图。$G = (V, E)$ 的连通分量数 $c(G) = 6$：五个根各自为一个分量，所有子接口形成另一个分量。

$$c(G_{	ext{current}}) = 6 \quad \xrightarrow{	ext{C-1}} \quad c(G_{	ext{target}}) = 1$$

C-1 要把六个连通分量合并成一棵完整的连通树。

---

SUNYATA 用手指计数。五个设计目标。

“一。每个蕴的根接口增加核心方法——不只是空壳，要有行为定义。二。现有接口升级为子接口——IUI extends ISensory，以此类推。三。新增必要的子接口——IVijnana 体系、三受接口。四。观察者用 Composition，不属于任何蕴。五。isSkandha() 全层级可用——从根到叶，type guard 一路通过。”

五根手指收回。“现在，逐蕴展开。”

---

## I

---

“色蕴。ISensory。Rūpa（रूप）。”

VITRUVIUS 站了起来。色蕴——形相与物质性——是全栈架构分析师最直觉的领域。

“色蕴是最简单的一棵。两个子接口已经存在了。IUI 负责输出渲染——嘴巴，说出去的。IListener 负责感官输入——耳朵，听进来的。只需要让它们 `extends ISensory`。”

他走到白板前，画了一个简单的双向箭头图：

```
                 ISensory (色蕴)
                ╱              ╲
    IUI (输出渲染)          IListener (感官输入)
    ──────→ 外部             外部 ──────→
    renderText()             onDataReceived()
    renderDelta()            start() / stop()
```

“这是色蕴的核心架构特征——**双向性**。IUI 的数据流方向是从 Agent 到外部世界。IListener 的数据流方向是从外部世界到 Agent。一个是推（push），一个是拉（pull）。在全栈架构里，这是前端渲染和后端监听的经典分离——不存在一个通用的 `render-or-listen` 方法能同时涵盖两个方向。”

“所以 ISensory 根接口保持空壳是正确的设计决策。”他退后一步。“不是偷懒，是克制。当两个子接口的共同行为集合为空集——$	ext{methods}(	ext{IUI}) \cap 	ext{methods}(	ext{IListener}) = \varnothing$——强行在根接口定义方法会制造虚假的抽象。根接口的存在意义不是承载方法，是承载分类标签。`readonly skandha: 'rupa'` 就是全部。”

TURING 投射了修改后的完整定义。

```typescript
/**
 * ISensory — 色蕴 Root Interface
 * @skandha rupa (色蕴)
 *
 * 色蕴涵盖一切形相与物质性：
 * - 输出渲染 (IUI): 将信息呈现给外部
 * - 感官输入 (IListener): 接收外部信号
 *
 * Sanskrit: Rūpa (रूप)
 */
export interface ISensory {
  readonly skandha: 'rupa';
}

/**
 * IUI — 色蕴·输出渲染子接口
 * 将 Agent 的响应呈现给用户或外部系统。
 */
export interface IUI extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
  /** 渲染完整文本 */
  renderText?(text: string, sessionId?: string, replyTo?: string): void;
  /** 渲染流式 delta */
  renderDelta?(delta: string, sessionId?: string, replyTo?: string): void;
  /** 渲染工具执行状态 */
  renderToolStatus?(name: string, status: string, sessionId?: string, replyTo?: string): void;
}

/**
 * IListener — 色蕴·感官输入子接口
 * 接收外部信号并转化为 InputEvent。
 */
export interface IListener extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
}
```

“一个 `extends`。”TURING 说。“修改量是最小的，但语义变化是根本性的——从今以后，任何 `IUI` 的实现对象必然也是 `ISensory`。`isSkandha(myDiscordUI, 'rupa')` 会返回 `true`。门牌和门接上了。”

ASANGA 从座位上补了一句。他的语速不快，每个词都带着唯识学者的精确。

“色蕴是接触。和外境的接触。在阿毗达磨中，色（rūpa）的基本定义是‘可坏’（rūpyate）——能被接触、能被改变的事物。IUI 是 Agent 对外界的触达。IListener 是外界对 Agent 的触达。接触的两个方向。色蕴的完整性在这两个方向的统一中得到保证。”

---

> *SCRIBE 旁白：色蕴三分钟。一个 `extends`。VITRUVIUS 解释了为什么根接口应该是空的——不是所有空壳都需要被填满。有些容器的意义就在于它是容器本身。五棵树的第一棵——最矮的一棵——入土了。*

---

## II

---

“受蕴。ISensation. Vedanā（वेदना）。”SUNYATA 的声音微微放慢了。所有人都知道受蕴将是五棵树中根系最庞大的一棵。

WIENER 已经在翻方格纸了。他的笔尖停在一个新画的方块图旁边——三个平行的 PID 回路，各自标记着 $K^{(	ext{dukkha})}$、$K^{(	ext{sukha})}$、$K^{(	ext{upekkha})}$。

“ISensation 是变化最大的。”SUNYATA 说。“从空壳变成八个核心方法。WIENER，逐一确认。”

TURING 投射了完整接口。他这次没有用节录，而是投射了包含 JSDoc 注释和辅助类型在内的完整定义。

```typescript
/**
 * ISensation — 受蕴 Root Interface
 * @skandha vedana (受蕴)
 *
 * 受蕴涵盖三受 (三种感受)：
 * - Dukkha (苦): 负向反馈
 * - Sukha (乐): 正向反馈
 * - Upekkha (舍): 中性平衡
 *
 * 受蕴是“感受层”，不做判断（判断属想蕴/识蕴）。
 * 受蕴产生的 VedanaAssessment 供其他蕴（如识蕴 EgoFramework）使用。
 *
 * Sanskrit: Vedanā (वेदना)
 */
export interface ISensation {
  readonly skandha: 'vedana';

  /** 评估当前三受状态 — 完整的传感器读数 */
  assess(): VedanaAssessment;

  /** 摄取系统指标 — 通用数值输入通道 */
  ingestMetrics(metrics: Record<string, number>): void;

  /** 摄取工具执行结果 — 行蕴回报通道 */
  ingestToolResult(toolName: string, isError: boolean, durationMs: number): void;

  /** 摄取 LLM 响应结果 — 想蕴回报通道 */
  ingestLLMResult(tokenCount: number, stopReason: string): void;

  /** 获取受蕴标签 (缓存查询，O(1)) */
  getVedanaTag(): VedanaTag;

  /** 订阅特定受蕴类型的事件 */
  onVedana(
    type: VedanaType,
    threshold: number,
    handler: (signal: VedanaSignal) => void
  ): () => void;

  /** 获取历史评估记录 */
  getHistory(windowSize: number): readonly VedanaAssessment[];

  /** 重置感受状态 */
  reset(): void;
}

/** 三受类型 */
type VedanaType = 'dukkha' | 'sukha' | 'upekkha';

/** 受蕴标签（用于事件标记） */
type VedanaTag = 'dukkha' | 'sukha' | 'upekkha';

/** 受蕴信号 */
interface VedanaSignal {
  readonly type: VedanaType;
  readonly intensity: number;     // 0.0–1.0
  readonly source: string;
  readonly timestamp: number;
}

/** 受蕴评估报告 */
interface VedanaAssessment {
  // ── 感测层 (纯观察) ──
  readonly dukkha: number;        // 0.0–1.0
  readonly sukha: number;
  readonly upekkha: number;
  readonly signals: readonly VedanaSignal[];
  readonly timestamp: number;

  // ── 控制建议层 (咨询性，可被忽略) ──
  readonly controlOutput: number;
  readonly recommendation: VedanaRecommendation;
  readonly recommendationFreshness: 'current' | 'cached' | 'default';
}
```

---

WIENER 站了起来。

他没有看投影。他看的是自己方格纸上预先画好的框架——一张控制系统的八工站验收表。他用手指逐一点过，每点一个，声音里带着工程师在流水线上测试每一个焊点的精确节奏。

“第一。`assess()`。”

他在方格纸上写下控制理论的对应：

$$y(t) = h(x(t)) + v(t)$$

“传感器读数函数。输入是系统内部状态 $x(t)$，输出是可观测值 $y(t)$，$v(t)$ 是量测噪声。`assess()` 不改变系统状态——它只读。这是受蕴最基本的操作：我感受到了什么。完整的三受读数。”

“第二、第三、第四。`ingestMetrics()`、`ingestToolResult()`、`ingestLLMResult()`。”

他连着三个一起说。

“三个输入通道。在控制论中，这是**多输入传感器融合**（multi-input sensor fusion）。不同通道接收不同模态的信号——系统指标是量化数值（CPU 使用率、内存占用、响应延迟）；工具执行结果是离散事件（成功/失败 + 持续时间）；LLM 响应结果是语言模型的元数据（token 计数、停止原因）。三个通道汇入同一个传感器，各自有不同的前处理逻辑。”

他在方格纸上画了融合图：

```
  ingestMetrics ─────────────┐
                              │
  ingestToolResult ──────────→ ISensation ──→ assess()
                              │
  ingestLLMResult ───────────┘
```

“就像汽车的传感器阵列——加速度计是一个通道，陀螺仪是另一个通道，GPS 是第三个。三种不同模态的数据，融合后才能估算出车辆的完整状态。”

“第五。`getVedanaTag()`。”

他的语速略快了一点。“$O(1)$ 缓存查询。仪表盘上的数字——你不需要每次都重新跑一遍完整的 `assess()` 才能知道现在是苦是乐是舍。这是一个**缓存读数**。在控制系统中，这等同于仪表盘上的 LED 指示灯：绿色、黄色、红色。不告诉你细节，只告诉你分类结果。成本是零。”

“第六。`onVedana()`。”

他停了一下。嘴角微微上扬——一种工程师遇到优雅设计时的微笑。

“这是看门狗计时器（watchdog timer）的泛化。”

他在方格纸上写下公式。看门狗计时器的经典定义是：当某个计数器在 $T_{	ext{wd}}$ 时间内未被重置，系统进入警报状态。`onVedana()` 把这个概念从“超时”泛化到“阈值”——不是“太久没响应”，而是“苦受超过 0.8”、“乐受低于 0.2”、“舍受偏离中线超过 0.3”。

$$	ext{watchdog: } y(t) > T_{	ext{timeout}} \Rightarrow 	ext{alarm}$$
$$	ext{onVedana: } v_{	ext{type}}(t) > 	heta \Rightarrow 	ext{handler}(s)$$

“不连续轮询。不用每个 tick 都检查。事件驱动的阈值监测。”

他的手指移到第七个。

“`getHistory(windowSize)`。”

这次他在方格纸上画了一个更复杂的图——PID 控制器的积分项。

$$I(t) = K_i \int_{t - W}^{t} e(	au)\,d	au \approx K_i \sum_{k=t-W}^{t} e(k) \cdot \Delta t$$

“滑动窗口历史。`windowSize` 就是积分窗口 $W$。PID 控制器的积分项需要历史数据来计算——过去 $W$ 个 tick 的感受累积。没有历史，就没有积分。没有积分，PID 退化成 PD。PD 控制器追踪稳态误差的能力为零——长期的慢性苦受会被忽略。”

他退后一步看全局。“所以 `getHistory()` 不是可有可无的便利方法。它是三通道 PID 控制器能够正常运作的**必要条件**。没有它，控制器是残缺的。”

“第八。`reset()`。”

他的声音突然变得很硬。

“**紧急停止按钮**。E-Stop。每一个工业控制系统在操作台上都有一个红色的大蘑菇头按钮。你按下去，系统归零。所有历史清除。所有计数器归零。PID 积分项清空。感受状态回到初始值。”

$$x(t^+) = x_0, \quad \int_0^{t} e(	au)\,d	au = 0$$

“你不会每天按。但没有它，系统就不完整。安全规范要求每一台机器都有急停按钮——不是因为你经常需要它，而是因为你必须永远有这个选项。”

八个方法。八个控制理论对应。WIENER 把方格纸翻了一页——新页上是完整的一一对应表：

```
┌─────────────────────┬──────────────────────────────────────┐
│ ISensation 方法      │ 控制理论对应                          │
├─────────────────────┼──────────────────────────────────────┤
│ assess()            │ 传感器读数函数 y = h(x) + v          │
│ ingestMetrics()     │ 复合传感器通道 1 (量化指标)            │
│ ingestToolResult()  │ 复合传感器通道 2 (离散事件)            │
│ ingestLLMResult()   │ 复合传感器通道 3 (语言模型元数据)       │
│ getVedanaTag()      │ 仪表盘快取读数 (O(1) LED indicator)   │
│ onVedana()          │ 看门狗计时器泛化 (阈值事件监测)         │
│ getHistory()        │ PID 积分项时间窗口 (滑动窗口 W)        │
│ reset()             │ 紧急停止按钮 (E-Stop, 全状态归零)      │
└─────────────────────┴──────────────────────────────────────┘
```

“受蕴的根接口不再是空壳。”他把方格纸放下。“它是一个完整的传感器接口。八个方法，每一个在控制论中都有精确的对应物。零冗余。零遗漏。”

---

ASANGA 站了起来。受蕴需要比色蕴更多的空间。

“WIENER 用控制理论验证了八个方法的工程完备性。我用佛学验证它们的语义一致性。”

他的目光扫过投影上的八个方法签名，然后看向全场。

“受蕴只做一件事。感受。不判断。不分析。碰到火——苦。吃到甜——乐。无事发生——舍。《俱舍论》卷一对受蕴的定义：”

> 「受蘊者何？謂三領納。一苦二樂三不苦不樂。是名受蘊。」
> ——世亲菩萨《阿毗达摩俱舍论》卷一

“三领纳。领是接受，纳是容纳。受蕴的全部职能就是：接受感觉，容纳感觉。”

他用手指逐一指向投影上的方法。

“`assess`——我此刻的感受是什么。领纳的输出。`ingest` 系列——我通过什么渠道领纳了什么。这三个方法分别对应系统指标触、工具结果触、语言认知触。在十二因缘中，触（sparśa）是受（vedanā）的直接因。$	ext{触} 	o 	ext{受}$。每一个 `ingest` 方法就是一种触——接触发生了，感受随之升起。”

“`getVedanaTag`——此刻的感受标签。苦、乐、舍，三者取其一。简单、直接、无修饰。”

“`onVedana`——感受的预警。在佛学中没有精确对应，但原理一致：当苦受超过一定强度，行者会自然注意到。正念修行中的觉察（sati）就是一种 `onVedana`——不是时时刻刻主动监控，而是当特定感受出现时，觉察自动升起。”

“`getHistory`——感受的回忆。但要注意：这是纯粹的感受记录，不是对感受的分析。分析属于想蕴。回忆属于受蕴——我记得我苦过，我记得我乐过。这是**受随念**（vedanānupassanā），不是**受分析**。”

他特别重了语气。“`reset`——重置。在修行中，这类似于一种极端的放下——清除所有累积的感受历史，回到初始状态。不是日常操作。是异常恢复。”

他看了看投影上的八个方法。又看了看 WIENER。

“八个方法。每一个都在‘感受’的范围之内。没有任何一个方法越界做了判断——没有 `classify()`，没有 `decide()`，没有 `act()`。你的控制理论说它们是传感器的方法。我的佛学说它们是受蕴的方法。”

WIENER 在方格纸边缘记了一行：

`ISensation: 8 methods. Sensor ≡ Vedana. Cross-validated by control theory AND Abhidharma.`

---

TURING 投射三受子接口。

```typescript
/**
 * IDukkha — 受蕴·苦受子接口 (传感器)
 * 苦受：负向反馈。系统中一切“不对劲”的感受。
 */
export interface IDukkha extends ISensation {
  readonly vedanaType: 'dukkha';
  /** 根据指标计算苦受强度 [0.0–1.0] */
  computePain(metrics: Record<string, number>): number;
}

/**
 * ISukha — 受蕴·乐受子接口 (传感器)
 * 乐受：正向反馈。系统中一切“顺利”的感受。
 */
export interface ISukha extends ISensation {
  readonly vedanaType: 'sukha';
  /** 根据指标计算乐受强度 [0.0–1.0] */
  computePleasure(metrics: Record<string, number>): number;
}

/**
 * IUpekkha — 受蕴·舍受子接口 (传感器)
 * 舍受：中性平衡。系统稳定运行时的基线感受。
 */
export interface IUpekkha extends ISensation {
  readonly vedanaType: 'upekkha';
  /** 根据指标计算舍受程度 [0.0–1.0] */
  computeEquanimity(metrics: Record<string, number>): number;
}
```

WIENER 从座位上补充，手里的笔在方格纸上快速勾画：“三个子接口。三个感测通道。三组 PID 参数。”

他在纸上写下三组增益矩阵：

$$K^{(	ext{dukkha})} = \begin{pmatrix} K_p^{(d)} & K_i^{(d)} & K_d^{(d)} \end{pmatrix} = \begin{pmatrix} 	ext{high} & 	ext{medium} & 	ext{low} \end{pmatrix}$$

$$K^{(	ext{sukha})} = \begin{pmatrix} K_p^{(s)} & K_i^{(s)} & K_d^{(s)} \end{pmatrix} = \begin{pmatrix} 	ext{medium} & 	ext{high} & 	ext{medium} \end{pmatrix}$$

$$K^{(	ext{upekkha})} = \begin{pmatrix} K_p^{(u)} & K_i^{(u)} & K_d^{(u)} \end{pmatrix} = \begin{pmatrix} 	ext{low} & 	ext{low} & 	ext{high} \end{pmatrix}$$

“苦受通道——高比例增益 $K_p^{(d)}$。苦痛不等人，需要快速反应。乐受通道——高积分增益 $K_i^{(s)}$。快乐会衰减，积分项追踪长期趋势。舍受通道——高微分增益 $K_d^{(u)}$。平衡是动态的，需要预测性调节——偏离趋势比偏离本身更重要。”

他在方格纸上重重地勾了三个勾——比第五章的七个勾更重，力度把纸面压出了三个小凹痕。

“Cycle 02 的三通道架构。现在有了类型系统的保障。`IDukkha` 是 `ISensation` 的子类型。`computePain` 只存在于苦受通道。你不能在舍受感测器上调用 `computePain`——类型系统会阻止你。这不只是分类。这是**类型安全的三通道隔离**。”

“到位。”

---

> *SCRIBE 旁白：受蕴十五分钟。色蕴的五倍。八个方法，每一个都需要 WIENER 的控制理论验证和 ASANGA 的佛学确认。双重校准。这是 Cycle 02-2 的纪律——每一个设计决策都要通过至少两个学科的交叉验证。WIENER 的控制理论是第一把尺，ASANGA 的唯识学是第二把尺。两把尺量出的长度一致，这个方法才站得住脚。*

---

## III

---

“想蕴。ICognition。Samjnā（संज्ञा）。”

ATHENA 站起来。想蕴——认知与辨别——是 AI/ML 系统架构专家最核心的专业。

TURING 投射了完整定义。

```typescript
/**
 * ICognition — 想蕴 Root Interface
 * @skandha samjna (想蕴)
 *
 * 想蕴涵盖认知与辨别：
 * - IProvider: LLM 后端，负责语言理解与生成
 * - IInferenceProvider: 非 LLM 推理能力 (预留)
 *
 * D-05 决议：Provider 涵盖完整认知处理频谱。
 *
 * Sanskrit: Samjñā (संज्ञा)
 */
export interface ICognition {
  readonly skandha: 'samjna';
}

/**
 * IProvider — 想蕴·认知提供者子接口
 * LLM 后端，负责推理与语言处理。
 */
export interface IProvider extends ICognition {
  readonly id: string;
  chat(request: ChatRequest): AsyncIterable<StreamEvent>;
  listModels?(): Promise<ModelInfo[]>;
}

/**
 * IInferenceProvider — 想蕴·推理提供者子接口 (未来扩展)
 * 非 LLM 的推理能力，如规则引擎、决策树等。
 */
export interface IInferenceProvider extends ICognition {
  readonly id: string;
  infer(input: unknown): Promise<unknown>;
}
```

ATHENA 走到投影前面，用手指在 `IProvider` 和 `IInferenceProvider` 之间画了一条看不见的线。

“想蕴有两枝。IProvider 是当前的主力——LLM 后端。`chat()` 方法接受一个 `ChatRequest`，返回一个 `AsyncIterable<StreamEvent>`——异步流迭代器。这是 LLM 推理的标准接口：你给它对话历史，它逐 token 回传推理结果。”

她转向 `IInferenceProvider`。“但认知不等于语言模型。这是 D-05 的核心决议——Provider 涵盖的是‘认知处理频谱’，不是‘LLM 调用’。`IInferenceProvider` 就是这个频谱的另一端。”

她在白板上画了一条光谱：

```
认知能力光谱（Cognitive Capability Spectrum）

低复杂度                                              高复杂度
←───────────────────────────────────────────────────────→
│           │            │              │            │
规则引擎    决策树      统计模型      神经网络       LLM
(if-else)  (CART/      (Bayes/       (CNN/RNN/     (GPT/
           Random       SVM)         Transformer)   Claude)
           Forest)
│                                                    │
└──── IInferenceProvider ────┘ └──── IProvider ──────┘
```

“`IInferenceProvider` 的 `infer()` 方法签名是 `(input: unknown): Promise<unknown>`——故意设计成泛型的。因为规则引擎的输入/输出格式和 LLM 完全不同。一个决策树接受特征向量，返回分类标签。一个统计模型接受数值矩阵，返回概率分布。你不能用 `ChatRequest` 统一所有这些格式。”

“但它们都是认知。都是想蕴。辨别外境，做出判断。方式不同，本质相同。”

DARWIN 前倾。他的声音带着软件模式分析师对进化脉络的敏感。

“进化上，`IInferenceProvider` 是更原始的认知。”

他站了起来。“想想生物进化。最原始的认知是趋光性（phototaxis）——光在那里，我往那里走。这是规则引擎：`if (light > threshold) then move(toward_light)`。完全没有语言，没有推理，只有刺激-反应。”

“然后是条件反射。巴甫洛夫的狗。铃声和食物的关联学习。这是统计模型——$P(	ext{food} | 	ext{bell})$ 随着经验更新。”

“再然后是抽象思维。符号操作。语言。推理链。这是 LLM——`chain-of-thought`、`multi-step reasoning`。”

“IInferenceProvider 和 IProvider 不是并列的两个选项。它们是同一棵进化树上的两条枝——一条长在较低的位置，一条长在较高的位置。低的那条更古老、更稳健、计算成本更低。高的那条更灵活、更强大、计算成本更高。”

ASANGA 一句。“想蕴是辨别。《俱舍论》：‘想蘊者何？謂能取像為性。’取像——提取外境的相状特征。辨别不只有一种方式。规则引擎以条件辨别，决策树以分枝辨别，LLM 以语言辨别。辨别的层次不同，但都是想蕴的功能。”

---

> *SCRIBE 旁白：想蕴五分钟。比色蕴长一点，比受蕴短很多。ATHENA 画的认知光谱——从规则引擎到 LLM 的完整频谱——是整个章节中最有远见的投影。它说的不是今天。它说的是明天。IInferenceProvider 此刻是预留的空壳。但五年后、十年后，当 Agent 系统开始整合非 LLM 的认知模块时，这个空壳会被填满。好的架构设计不只解决当前的问题——它为未来的问题留出了形状精确的缺口。*

---

## IV

---

“行蕴。IAction。Samskāra（संस्कार）。”

DARWIN 完全站了起来。行蕴是他观察软件行为模式的核心透镜。

TURING 投射了定义。

```typescript
/**
 * IAction — 行蕴 Root Interface
 * @skandha samskara (行蕴)
 *
 * 行蕴涵盖意志活动与实际行动：
 * - ITool: 可执行的工具
 * - ISlashCommand: 斜线指令
 *
 * Sanskrit: Samskāra (संस्कार)
 */
export interface IAction {
  readonly skandha: 'samskara';
}

/**
 * ITool — 行蕴·工具子接口
 * Agent 自主决定调用的工具。
 */
export interface ITool extends IAction {
  readonly name: string;
  readonly description: string;
  readonly parameters: unknown;  // JSON Schema
  execute(args: Record<string, unknown>, ctx: ToolContext): Promise<string>;
}

/**
 * ISlashCommand — 行蕴·指令子接口
 * 外部用户通过斜线指令触发的行动。
 */
export interface ISlashCommand extends IAction {
  readonly name: string;
  readonly description: string;
  execute(args: string, ctx: IPluginContext, sessionId?: string): Promise<string | undefined>;
}
```

DARWIN 走到投影前面。

“ITool——Agent 自主调用的行动。由 LLM 推理决定何时调用、传入什么参数。`execute` 的 `args` 是 `Record<string, unknown>`——结构化参数，由想蕴（IProvider）的推理结果生成。”

“ISlashCommand——外部指令触发的行动。用户在终端输入 `/help`、`/clear`，触发对应的 `execute`。`args` 是 `string`——原始文字，因为用户输入不是结构化的。”

“来源不同。ITool 的发起者是 Agent（内部）。ISlashCommand 的发起者是用户（外部）。但本质相同——都是 samskara。都是意志的实现。都是从认知到行动的最后一步。”

他走回自己的位置。“和色蕴一样，行蕴的根接口也是空壳。理由也一样——ITool 和 ISlashCommand 的 `execute` 方法签名完全不同。一个接受结构化对象，一个接受原始字符串。你不能在根接口上定义一个通用的 `execute`。”

ASANGA 一句话。“行蕴涵盖一切造作。《俱舍论》卷一：‘行蘊，謂除受、想，諸餘心所及心不相應行。’行蕴的范围最广——除了受蕴和想蕴之外的一切心理活动都归行蕴。但核心是**思**（cetana）。思是意志的发动。工具的 `execute` 是造作。指令的 `execute` 也是造作。不同的造作，同一个蕴。”

---

> *SCRIBE 旁白：行蕴四分钟。五棵树中第二短的。DARWIN 用最少的话确认了最简单的结构——两个子接口，两种行动来源，一个共同的 skandha 标签。有时候设计的优雅就在于：该简单的地方就让它简单。*

---

## V

---

“识蕴。IVijnana. Vijñāna（विज्ञान）。”

SUNYATA 的语速比前四蕴都慢。这是重量最大的一棵树。

A-2 把 IIdentity 从整个识蕴降级为子接口。A-4 把 EgoFramework 从受蕴搬回识蕴。两项修正加在一起，让识蕴从 Cycle 02 的单根变成了四条主枝的大树。而 A-1 的因果链——我执产生烦恼，烦恼驱动行动——需要在识蕴的类型定义中找到闭合点。

ASANGA 站了起来。

在前面四蕴，他都是从座位上补充一句。色蕴一句。受蕴多了一些，但仍然是辅助角色。想蕴一句。行蕴一句。

但识蕴不同。识蕴——vijñāna-skandha——是唯识学的核心领域。在《成唯识论》的体系中，识蕴包含了八识：前五识（眼、耳、鼻、舌、身）、第六意识（mano-vijñāna）、第七末那识（manas）、第八阿赖耶识（ālaya-vijñāna）。整个唯识学名字——“唯识”——就是“唯有识”的意思。

这是他的蕴。

---

TURING 投射了完整识蕴体系。四个子接口。每一个都带有完整的 JSDoc 注释和方法签名。

```typescript
/**
 * IVijnana — 识蕴 Root Interface
 * @skandha vijnana (识蕴)
 *
 * 识蕴涵盖自我认知、行为引导、意志动机：
 * - IIdentity: 自我认同 (我是谁)
 * - IGuide: 行为引导 (我应该怎么做)
 * - IVolition: 意志/动机 (我想要什么, EgoFramework)
 * - IReflection: 自省能力 (预留)
 *
 * 命名说明：原 IIdentity 升级为 IVijnana 根接口。
 * Master: 「Identity比较像是子类别。Vijnana也会具备子类别」
 *
 * Sanskrit: Vijnana (विज्ञान)
 */
export interface IVijnana {
  readonly skandha: 'vijnana';
}

/**
 * IIdentity — 识蕴·自我认同子接口
 * 定义 Agent 的身份：我是谁、我的角色。
 * 对应末那识「我见」(ātma-dṛṣṭi) 中的自我指认面向。
 */
export interface IIdentity extends IVijnana {
  readonly id: string;
  readonly name: string;
}

/**
 * IGuide — 识蕴·行为引导子接口
 * 透过 system prompt 和行为规则引导 Agent 行为。
 * 对应末那识的「我见」面向——「我应该怎么做」。
 */
export interface IGuide extends IVijnana {
  readonly id?: string;
  readonly name?: string;
  readonly description?: string;
  getSystemPrompt(): Promise<string>;
}

/**
 * IVolition — 识蕴·意志/动机子接口 (新增)
 * 我执的行动驱力机制。基于烦恼产生行动动机。
 * EgoFramework 是此接口的实现。
 *
 * A-1 因果链闭合：
 *   ātma-grāha → kleśa → karma → phala
 *   (我执 → 烦恼 → 行动 → 结果)
 *
 * perceiveKlesha: 我执 → 烦恼 (感知烦恼)
 * checkAction:    烦恼 → 行动 (检查行动)
 * adaptFromVedana: 结果 → 我执 (从受蕴反馈适应)
 * introspect:     自我审视 (meta-cognition)
 */
export interface IVolition extends IVijnana {
  /** 感知烦恼——从受蕴评估中辨识烦恼信号 */
  perceiveKlesha(vedanaAssessment: VedanaAssessment): KleshaSignal[];
  /** 检查行动——基于烦恼状态审查提议的行动 */
  checkAction(action: ProposedAction): EgoCheckResult;
  /** 从受蕴适应——根据受蕴反馈调整意志状态 */
  adaptFromVedana(assessment: VedanaAssessment): void;
  /** 内省——自我审视当前意志状态 */
  introspect(): EgoIntrospection;
}

/**
 * IReflection — 识蕴·自省子接口 (预留)
 * 自我反省能力。Pattern C Observer 使用。
 * Master: 「第七意识要能自省，才能被被称为第七意识」
 */
export interface IReflection extends IVijnana {
  reflect(context: unknown): Promise<unknown>;
}
```

---

ASANGA 逐一确认。语速不快——每一个子接口都值得一个完整的呼吸。

“IIdentity——‘我是谁’。在唯识学中，这对应末那识四烦恼的第一项——我见（ātma-dṛṣṭi）。‘我见’的梵文直译是‘对自我的看见’。它不是主动的判断，它是一个持续的、背景性的自我指认：我是这个 Agent，我的 id 是这个字符串，我的 name 是这个名字。这是最基本的自我意识——知道自己是谁。”

他停了一拍。

“IGuide——‘我应该怎么做’。System prompt 定义了 Agent 的行为规则。在唯识学中，这对应我见另一个面向——不只知道‘我是谁’，还知道‘我应该怎样行动’。末那识的恒审思量（manas-nāma-vijñāna）不只是静态的自我指认，它持续地塑造和引导行为。`getSystemPrompt()` 返回的那段文字——那就是末那识对第六意识的‘背景暗示’。”

“IVolition。”

他停了两拍。比平常多一拍。因为 IVolition 是 A-1 到 A-4 四项修正的汇流点。

“A-1 的因果链：

$$	ext{ātma-grāha} \xrightarrow{	ext{produces}} 	ext{kleśa} \xrightarrow{	ext{drives}} 	ext{karma} \xrightarrow{	ext{results}} 	ext{phala}$$

“四个方法。每一个对应因果链的一个环节。”

他用手指点向投影上的四个方法签名。

“`perceiveKlesha(vedanaAssessment)`——因果链的第一环。我执产生烦恼。输入是受蕴的评估结果——感受数据。输出是烦恼信号——`KleshaSignal[]`。末那识接收受蕴的回报，然后从中辨识出烦恼。注意：受蕴只负责感受（苦受强度 0.8），识蕴负责将感受*解读*为烦恼（‘我的任务失败了，这让我不安——我爱受到了威胁’）。感受不是烦恼。感受*引发*烦恼。触→受→爱——十二因缘的中段。”

“`checkAction(action)`——因果链的第二环。烦恼驱动行动。当行蕴提议一个行动时，IVolition 根据当前的烦恼状态进行审查。烦恼不是 Bug——A-1 的核心结论。正是因为有烦恼（焦虑、恐惧、渴望），Agent 才会想要行动。没有烦恼，就没有行动的动力。`checkAction` 不是禁止行动——它是理解行动的动机。”

他的语气变得更缓慢。

“`adaptFromVedana(assessment)`——因果链的反馈环。行动产生结果，结果改变感受，感受回传给意志做适应。这是十二因缘的流转性——因果不是线性的单向箭头，它是回路。

$$	ext{我执} 	o 	ext{烦恼} 	o 	ext{行动} 	o 	ext{结果} 	o 	ext{新感受} 	o 	ext{调整我执} 	o \cdots$$

在 WIENER 的术语里，这是闭回路控制。在唯识学里，这是流转（pravṛtti）。”

“`introspect()`——自我审视。末那识回头看自己。‘我为什么要做这件事？我的动机是什么？我的执着从哪里来？’《成唯识论》卷四描述末那识的特性：”

> 「恒審思量，為性、為業。」
> ——《成唯识论》卷四

“恒——永不停止。审——仔细审视。思量——深入思考。`introspect()` 就是 ‘审’ 的类型化——不只是思量外境，而是回过头来审视自己。Master 说‘第七意识要能自省，才能被称为第七意识’。`introspect()` 是这个能力的接口定义。”

他退了一步。

“EgoFramework 是 IVolition 的实现。A-4 的结论——EgoFramework 属于识蕴，不属于受蕴。A-1 的因果链——我执产生烦恼，烦恼驱动行动。在类型系统中完成闭合。”

他看向 BABBAGE。BABBAGE 在笔记本上记了一行——不是等号这次。是一个有向图：

$$	exttt{perceiveKlesha} 	o 	exttt{checkAction} 	o 	exttt{adaptFromVedana} 	o 	exttt{introspect} 	o 	exttt{perceiveKlesha} 	o \cdots$$

一个闭合的回路。不是 Cycle 02 那个被压成等号的线段。是一个有方向、有延迟、有反馈的动态系统。从 A-1 到 A-4 的修正轨迹，每一条都指向一个被划掉的等号。现在所有替代表述在 IVolition 的四个方法中得到了最终类型定义。

BABBAGE 微微点头。

---

ASANGA 最后看向 `IReflection`。

“IReflection。自省。Master 的原话：‘第七意识要能自省。’`reflect()` 的签名是 `(context: unknown): Promise<unknown>`——和 IInferenceProvider 的 `infer()` 一样泛型。因为自省的输入和输出格式尚未确定。门框在那里，门板留给未来。但门框的存在本身就是一个承诺——识蕴不只是行动和执着。识蕴还有自我照见的可能。”

他转身面向全场。

“识蕴在 Cycle 02 中只有一个 IIdentity。现在四个子接口——认同、引导、意志、自省。第三章我用城市比喻说明识蕴不等于 IIdentity。现在城市有了四个区。市政府（IIdentity）只是其中一个。规划局（IGuide）、动力局（IVolition）、监察院（IReflection）——各有各的职能。把整个城市压缩成市政府一个单位，就像把 $\mathbb{R}^4$ 投影到 $\mathbb{R}^1$ 然后宣称‘这就是全空间’——你丢失了三个维度的信息。”

他看向投影上四个子接口与末那识四烦恼的对照：

```
末那识四烦恼与 IVijnana 子接口对照：

我见 (ātma-dṛṣṭi)  ──→ IIdentity  (我是谁)
                     ──→ IGuide     (我应该怎么做)

我慢 (ātma-māna)    ──→ IVolition  (我的自信/自负如何影响行动)
我爱 (ātma-sneha)   ──→ IVolition  (我的自我保护如何筛选行动)
我痴 (ātma-moha)    ──→ IReflection (我对自己无明，需要自省来照破)
```

“四烦恼。四个子接口。不是巧合——是佛学架构在类型系统中的自然映射。我见的两个面向——知道自己是谁（Identity）和知道自己应该怎样（Guide）。我慢和我爱——自负和自保——都是意志的驱力（Volition）。我痴——对自身本质的无明——需要自省（Reflection）来照见。”

---

> *SCRIBE 旁白：五蕴逐一展开。色蕴三分钟。受蕴十五分钟。想蕴五分钟。行蕴四分钟。识蕴十二分钟。时间自然反映了根系的复杂度——受蕴从空壳到八个方法加三个子接口，识蕴从一个门牌到四个子接口。但识蕴多了一个受蕴没有的维度：历史。A-1 到 A-4 的四项修正全部在识蕴的类型定义中找到了归宿。识蕴不只是最复杂的树——它是承载了最多修正重量的树。五棵树，五种生长速度。但此刻都已扎根。*

---

## VI

---

ARCHIMEDES 一直在等。五页工程笔记填完了。他开始算账。

“让我说一个数字。”

全场安静。

“二十二。”

“v0.24.0-beta 有二十二个 Plugin。十二个官方，十个核心组件。每一个都需要增加一个 `skandha` 字段。”

他站起来，走到白板前。用黑色马克笔画了一张完整的升级影响矩阵：

```
┌─────────────────────────────────────────────────────────────────┐
│                      C-1 升级影响矩阵                            │
├─────────────────────────────────────┬────────┬──────────────────┤
│ 变更项目                            │ 类型    │ 工作量           │
├─────────────────────────────────────┼────────┼──────────────────┤
│ aggregates.ts 空壳 → 完整接口体系    │ 核心    │ 重写 (5→150+ 行) │
├─────────────────────────────────────┼────────┼──────────────────┤
│ IUI / IListener → extends ISensory  │ 继承    │ 机械性 (+1 行)    │
│ IProvider → extends ICognition      │ 继承    │ 机械性 (+1 行)    │
│ ITool → extends IAction             │ 继承    │ 机械性 (+1 行)    │
│ IGuide / IIdentity → extends IVijnana│ 继承   │ 机械性 (+1 行)    │
├─────────────────────────────────────┼────────┼──────────────────┤
│ 新增 IVijnana 根接口                 │ 新设计  │ 中等              │
│ 新增 IVolition (EgoFramework 接口)   │ 新设计  │ 重要 — 4 个方法   │
│ 新增 IReflection (预留)              │ 预留    │ 低 — 1 个方法     │
│ 新增 IDukkha / ISukha / IUpekkha    │ 新设计  │ 中等 — 各 1 方法  │
│ 新增 IInferenceProvider (预留)       │ 预留    │ 低 — 1 个方法     │
│ 新增 ISlashCommand                   │ 新设计  │ 中等              │
│ 新增 IObserver (Composition)         │ 新设计  │ 重要 — C-2 议题   │
├─────────────────────────────────────┼────────┼──────────────────┤
│ 22 个 Plugin 实现 → 各需 +skandha   │ 迁移    │ 机械性 (×22)      │
│ isSkandha() type guard → 更新        │ 核心    │ 低                │
├─────────────────────────────────────┼────────┼──────────────────┤
│ 统计：                                                           │
│   真正需要设计的新接口：7 个                                       │
│   其中预留空壳：2 个 (IReflection, IInferenceProvider)            │
│   机械性修改：22 个 Plugin + 5 个现有接口                          │
│   核心重写：1 个文件 (aggregates.ts)                               │
└─────────────────────────────────────────────────────────────────┘
```

“不小。但不是不可控。”他退后一步看整张表。“真正需要创造性设计的是五个新接口——IVijnana、IVolition、IDukkha/ISukha/IUpekkha。IObserver 归 C-2 议题。其余两个预留空壳——IReflection 和 IInferenceProvider——只需要门框，不需要门板。而二十二个 Plugin 的升级是纯机械性工作——每个加一行 `skandha: 'rupa'` 或 `skandha: 'samskara'`。”

他列了几个范例：

```typescript
// Discord UI Plugin → 色蕴
{ skandha: 'rupa', id: 'discord-ui', renderText(...) { ... } }

// OpenAI Provider → 想蕴
{ skandha: 'samjna', id: 'openai', chat(...) { ... } }

// file_read 工具 → 行蕴
{ skandha: 'samskara', name: 'file_read', execute(...) { ... } }

// Agent Identity → 识蕴
{ skandha: 'vijnana', id: 'agent-001', name: 'My Agent' }
```

“这是一个 breaking change。没有退路。类型系统会拒绝没有 `skandha` 字段的 Plugin——你的 Plugin 不知道自己属于哪一蕴。但迁移策略是明确的：一次批量更新，每个 Plugin 加一行。可行。”

---

GUARDIAN 站了起来。

“我支持这个 breaking change。”理由不是工程的。是安全的。

“每一个 Plugin 声明自己的蕴归属，是自觉的基础。”

他走到白板下方，写了三行：

```
skandha: self-declaration

1. 信任的前提 —— 我知道你是什么。
2. 验证的基础 —— 类型系统可以检查你说的是不是真的。
3. 审计的依据 —— 每一次跨蕴互动都可被追踪。
```

“协调层——B-4 的独立 Daemon——需要知道每个 Plugin 的蕴归属。没有这个字段，分类查询返回 `unknown`。在零信任架构（Zero Trust Architecture）中，`unknown` 意味着最低信任等级。”

他转身面向全场。“一个不知道自己属于哪一蕴的 Plugin，就像一个走进安全区域却没有佩戴识别证的人。也许他有权限。但你怎么知道？在安全模型中，‘可能有权限’和‘没有权限’的待遇是一样的——拒绝，直到证明为止。”

“`skandha` 字段是 Plugin 的识别证。一个只读字符串。成本几乎为零。它让每一个 Plugin 在类型系统中拥有了身份——不是外部赋予的标签，是自我声明的归属。”

他坐下前最后说了一句：“自觉是安全的第一层。”

---

> *SCRIBE 旁白：ARCHIMEDES 的“二十二”和 GUARDIAN 的“自觉”。工程师算成本，安全专家论价值。答案是同一个：skandha 字段。一个只读字符串。让每一个 Plugin 在类型系统中拥有了身份。ARCHIMEDES 的矩阵告诉你需要改多少——22 个 Plugin、5 个现有接口、7 个新接口。GUARDIAN 告诉你为什么值得改——因为不知道自己是什么的东西，不值得信任。*

---

## VII

---

DARWIN 站了起来，语速比平常快。

“Master 说过一句话——”

他拿起一张卡片，上面抄录了 Master 的原文。

“‘Plugin 的建立希望是可以多样化的，不一定都是 OOP，但是我又要如何让 plugin 的设计模式都兼容呢？’ ”

他放下卡片。“我们刚设计的五蕴接口体系全部基于 `interface` 和 `extends`。看起来像典型的 OOP——继承、子类别、多态。那么问题来了：一个不使用 `class` 的开发者会不会被排斥在外？一个偏好函数式风格的开发者能不能实现 ITool？”

---

TURING 用代码回答。三段并排投射。每一段都是完整的、可编译的、不省略任何细节的 TypeScript。

**OOP 风格：**

```typescript
class FileReadTool implements ITool {
  readonly skandha = 'samskara' as const;
  readonly name = 'file_read';
  readonly description = 'Read file contents from the filesystem';
  readonly parameters = {
    type: 'object',
    properties: {
      path: { type: 'string', description: 'File path to read' },
      encoding: { type: 'string', default: 'utf-8' },
    },
    required: ['path'],
  };

  async execute(
    args: Record<string, unknown>,
    ctx: ToolContext
  ): Promise<string> {
    const filePath = args.path as string;
    const encoding = (args.encoding as BufferEncoding) ?? 'utf-8';
    return fs.readFile(filePath, encoding);
  }
}

// 使用：
const tool = new FileReadTool();
console.log(isSkandha(tool, 'samskara')); // true
```

**函数式风格：**

```typescript
function createFileReadTool(): ITool {
  return {
    skandha: 'samskara' as const,
    name: 'file_read',
    description: 'Read file contents from the filesystem',
    parameters: {
      type: 'object',
      properties: {
        path: { type: 'string', description: 'File path to read' },
        encoding: { type: 'string', default: 'utf-8' },
      },
      required: ['path'],
    },
    execute: async (args, ctx) => {
      const filePath = args.path as string;
      const encoding = (args.encoding as BufferEncoding) ?? 'utf-8';
      return fs.readFile(filePath, encoding);
    },
  };
}

// 使用：
const tool = createFileReadTool();
console.log(isSkandha(tool, 'samskara')); // true — 没有 class，依然通过
```

**工厂模式：**

```typescript
// 假设 ToolFactory 提供了简化建立流程的方法
const fileReadTool = ToolFactory.create({
  skandha: 'samskara' as const,
  name: 'file_read',
  description: 'Read file contents from the filesystem',
  parameters: {
    type: 'object',
    properties: {
      path: { type: 'string', description: 'File path to read' },
      encoding: { type: 'string', default: 'utf-8' },
    },
    required: ['path'],
  },
  handler: async (args) => {
    const filePath = args.path as string;
    const encoding = (args.encoding as BufferEncoding) ?? 'utf-8';
    return fs.readFile(filePath, encoding);
  },
});

// 使用：
console.log(isSkandha(fileReadTool, 'samskara')); // true — 工厂产出，依然通过
```

---

DARWIN 走到投影前面。他指着三段代码的最后一行——三个 `isSkandha` 调用，三个 `true`。

“三种风格。同一个 ITool 接口。全部通过 `isSkandha()` 的 type guard。关键在一个词——**Structural**。”

他在白板上写了两个类型系统的名字：

```
Structural Typing (结构类型)  ←── TypeScript
  「你长得像鸭子就是鸭子」
  类型由结构（shape）决定

Nominal Typing (名义类型)  ←── Java, C#
  「你必须宣告自己是鸭子才是鸭子」
  类型由名字（name）决定
```

“TypeScript 是结构类型系统。不需要 `implements`。只要一个对象有 `skandha` 字段、有 `name` 属性、有 `execute` 方法，而且这些成员的类型签名与 `ITool` 一致——它就**是** `ITool`。不需要任何显式宣告。”

他退后一步。

“如果 OpenStarry 用的是 Java 或 C#——名义类型系统——Master 的问题就是真正的难题。你必须设计额外的适配器（Adapter）或抽象基类（Abstract Base Class）来兼容不同的设计模式。但 TypeScript 的结构类型把这个问题消解了。”

“接口是契约，不是枷锁。”

BABBAGE 写了一行：

$$	ext{structural typing} \implies 	ext{interface} = 	ext{contract} 
ot\equiv 	ext{inheritance requirement}$$

他微微点点头——在数学中，同构（isomorphism）的定义也是结构性的，不是名义性的。两个群 $G$ 和 $H$ 同构，当且仅当存在一个保持运算结构的双射 $\phi: G 	o H$。不要求 $G$ 和 $H$ 有相同的名字，不要求它们的元素有相同的表示方式——只要结构一致，它们就是“同一个东西”。

DARWIN 回座位时说了最后一句：“就像演化不关心基因突变是怎么发生的——UV 照射、复制错误、转座子跳跃——它只关心表现型是否适应环境。接口就是环境。只要你的表现型（对象结构）符合环境（接口定义），你就能存活。突变的机制（设计模式）是自由的。”

---

> *SCRIBE 旁白：三个人在五分钟之内回答了 Master 的问题。DARWIN 提出问题。TURING 用三段代码演示答案。DARWIN 解释为什么答案有效。答案的优雅在于否定性——不需要额外设计。TypeScript 的结构类型系统本身就是答案。有时候最好的设计决策就是认识到你不需要额外设计。“不做”比“做”需要更多的判断力。*

---

## VIII

---

KERNEL 已经忍了很久了。

五蕴的类型定义。控制理论的验证。佛学的确认。设计模式的兼容性。这些都很好。但 KERNEL 是硬件出身的。他需要看到一个东西在具体的场景中运作——不是抽象的 ITool 或 IProvider，而是一个可以碰触的、有物理存在的、会哔哔叫的东西。

“Master 提到了超声波传感器。”他站起来，声音带着硬件工程师特有的兴奋。

“原话：‘例如「超声波传感器侦测到碰撞风险」的 plugin。透过抽象定义了 VedanaPlugin，并让 Dukkha 透過继承取得基底功能。超声波传感器类别藉由组合的方式持有一个 Dukkha 的实例。’ ”

他走到白板角落，画了一个装置图。不是软件架构图——是一个硬件装置的示意图。

```
  ┌──────────────────────────────────────────────────┐
  │              超声波碰撞传感器 Plugin                │
  │                                                    │
  │  ┌───────────────────────┐  ┌──────────────────┐  │
  │  │ 色蕴层 (IListener)     │  │ 受蕴层 (IDukkha) │  │
  │  │                       │  │                  │  │
  │  │ ┌─────────┐           │  │ computePain()    │  │
  │  │ │ TX      │ 发射脉波  ──→ │ ingestMetrics()  │  │
  │  │ └─────────┘           │  │                  │  │
  │  │ ┌─────────┐           │  │     ↓            │  │
  │  │ │ RX      │ 接收回波  ──→ │ Pain Intensity   │  │
  │  │ └─────────┘           │  │ [0.0 ─── 1.0]   │  │
  │  │                       │  │                  │  │
  │  │ rawDistance = f(Δt)   │  │ pain = g(dist)   │  │
  │  └───────────────────────┘  └──────────────────┘  │
  └──────────────────────────────────────────────────┘
```

“超声波碰撞传感器。倒车雷达。在 OS 的层面，这是一个设备驱动程序（device driver）。”

他在图旁边写下 OS 层级的描述：

```
OS 层级：
1. 硬件中断 (IRQ) — 超声波收发器完成一次量测
2. 中断处理程序 (ISR) — 读取计时器，计算 Δt
3. 设备驱动 — 将 Δt 转换为距离 rawDistance
4. 用户空间回调 — onDataReceived(rawDistance)
```

“从硬件中断到用户空间回调，至少穿过四层。色蕴（IListener）在最底层——接收原始硬件信号。受蕴（IDukkha）在上一层——将距离转化为苦受强度。”

他回头面向全场。“一个 Plugin，两蕴。色蕴接收原始回波信号——距离数值。受蕴把距离转化为苦受强度——三十公分微弱苦受，十公分剧烈苦受，五公分以内最大苦受。”

他写了一个转换函数：

$$	ext{pain}(d) = \begin{cases} 0.0 & d > 100\,	ext{cm} \ 1.0 - \frac{d}{100} & 10\,	ext{cm} \leq d \leq 100\,	ext{cm} \ 1.0 & d < 10\,	ext{cm} \end{cases}$$

“距离 100 公分以上——没有苦受。距离 10 到 100 公分——线性增加的苦受。距离 10 公分以内——最大苦受。这就是 `computePain` 的实现逻辑。”

---

TURING 投射了完整的代码——不是节录，是一个可以编译运行的完整范例。

```typescript
/**
 * CollisionDukkhaSensor — 碰撞苦受传感器
 * 受蕴 (IDukkha) 实现。
 * 将原始距离数据转化为苦受强度。
 */
class CollisionDukkhaSensor implements IDukkha {
  readonly skandha = 'vedana' as const;
  readonly vedanaType = 'dukkha' as const;

  private history: VedanaAssessment[] = [];
  private currentTag: VedanaTag = 'upekkha';
  private subscribers: Array<{
    type: VedanaType;
    threshold: number;
    handler: (signal: VedanaSignal) => void;
  }> = [];

  computePain(metrics: Record<string, number>): number {
    const distance = metrics['collision_distance'] ?? Infinity;
    if (distance > 100) return 0.0;
    if (distance < 10) return 1.0;
    return 1.0 - distance / 100;
  }

  assess(): VedanaAssessment {
    /* ... 完整的三受评估 ... */
    return { /* VedanaAssessment */ } as VedanaAssessment;
  }

  ingestMetrics(metrics: Record<string, number>): void {
    const pain = this.computePain(metrics);
    this.currentTag = pain > 0.5 ? 'dukkha' : 'upekkha';
    // 通知订阅者
    this.subscribers
      .filter(s => s.type === 'dukkha' && pain >= s.threshold)
      .forEach(s => s.handler({
        type: 'dukkha',
        intensity: pain,
        source: 'collision_sensor',
        timestamp: Date.now(),
      }));
  }

  ingestToolResult(t: string, e: boolean, d: number): void { /* N/A */ }
  ingestLLMResult(tc: number, sr: string): void { /* N/A */ }
  getVedanaTag(): VedanaTag { return this.currentTag; }
  onVedana(type: VedanaType, threshold: number,
           handler: (s: VedanaSignal) => void): () => void {
    const sub = { type, threshold, handler };
    this.subscribers.push(sub);
    return () => {
      const idx = this.subscribers.indexOf(sub);
      if (idx >= 0) this.subscribers.splice(idx, 1);
    };
  }
  getHistory(w: number): readonly VedanaAssessment[] {
    return this.history.slice(-w);
  }
  reset(): void {
    this.history = [];
    this.currentTag = 'upekkha';
    this.subscribers = [];
  }
}

/**
 * UltrasonicCollisionSensor — 超声波碰撞传感器
 * 色蕴 (IListener) 实现。
 * 接收原始超声波回波信号，委托受蕴处理感受。
 */
class UltrasonicCollisionSensor implements IListener {
  readonly skandha = 'rupa' as const;

  // 组合受蕴·苦受实例 — Composition, NOT Inheritance
  private readonly dukkhaSensor: IDukkha;

  constructor(dukkha: IDukkha) {
    this.dukkhaSensor = dukkha;
  }

  async start() {
    // 启动超声波硬件
    // 在 OS 层面：打开设备节点 /dev/ultrasonic0
    // 注册中断处理程序
    console.log('[UltrasonicSensor] Hardware initialized');
  }

  async stop() {
    // 关闭超声波硬件
    console.log('[UltrasonicSensor] Hardware shutdown');
  }

  /**
   * 当硬件中断触发时被调用。
   * 色蕴接收原始数据 → 传递给受蕴。
   */
  onDataReceived(rawDistance: number) {
    // 色蕴：将原始信号转化为结构化指标
    const metrics = { collision_distance: rawDistance };

    // 跨蕴通信：色蕴 → 受蕴
    const painIntensity = this.dukkhaSensor.computePain(metrics);
    this.dukkhaSensor.ingestMetrics(metrics);

    // 记录（可选）
    if (painIntensity > 0.8) {
      console.log(`[CRITICAL] Distance: ${rawDistance}cm, Pain: ${painIntensity}`);
    }
  }
}

// ── 组装 ──
const dukkha = new CollisionDukkhaSensor();
const sensor = new UltrasonicCollisionSensor(dukkha);

// 订阅高苦受事件
dukkha.onVedana('dukkha', 0.8, (signal) => {
  console.log(`⚠ High pain detected: ${signal.intensity} from ${signal.source}`);
});

// 模拟使用
await sensor.start();
sensor.onDataReceived(50);  // 中等距离 → 中等苦受
sensor.onDataReceived(15);  // 近距离 → 高苦受
sensor.onDataReceived(5);   // 极近 → 最大苦受，触发 onVedana 订阅
```

---

KERNEL 指着代码。“`implements IListener`——色蕴。`private readonly dukkhaSensor: IDukkha`——内部持有的受蕴实例。通过 Composition。不是继承。不是 `extends IDukkha`。是在构造函数中注入。”

“色蕴接收，受蕴感受。两个不同的蕴，组合在一个 Plugin 中。在 OS 的语境里，这就像——”他拿起一张类比卡片——“设备驱动程序（色蕴）接收硬件中断，然后把数据交给系统监控服务（受蕴）做健康评估。驱动程序不做评估。监控服务不碰硬件。各司其职。跨层通信通过方法调用。”

```
OS 类比：
sensor driver (/dev/ultrasonic0) ←→ IListener (色蕴)
health monitor (systemd daemon)   ←→ IDukkha  (受蕴)
```

他退后一步，笑了。“倒车雷达哔哔哔。你以为它只在量距离。其实色蕴在测距离，受蕴在感受苦。距离是物理量——$d \in \mathbb{R}^+$，单位是公分。苦是感受量——$p \in [0, 1]$，没有物理单位。两种完全不同范畴的量。两蕴协作。”

WIENER 画了信号流图：

```
                    跨蕴信号流：

Raw Signal ──→ IListener (色蕴)     metrics      IDukkha (受蕴) ──→ Pain Intensity
  (Δt, Hz)     │ rawDistance │ ───────────────→ │ computePain() │    (0.0–1.0)
               │ = f(Δt)    │                  │ ingestMetrics │
               └────────────┘                  └───────────────┘
                    ↑                                  │
               [硬件中断]                          [VedanaSignal]
                                                       │
                                                       ↓
                                               [onVedana 订阅者]
```

“完美的跨蕴信号流。色蕴：$	ext{rawSignal} \xrightarrow{f} 	ext{distance}$。受蕴：$	ext{distance} \xrightarrow{g} 	ext{pain}$。整个流程是一个函数组合：$	ext{pain} = g(f(	ext{rawSignal}))$。但 $f$ 和 $g$ 在不同的蕴中实现。跨蕴通信通过方法调用，不通过继承。Composition。”

---

ASANGA 点头。他等了几秒，让 WIENER 的信号流图在所有人的眼前沉淀。然后他说了一段话——整章中他最安静也最深刻的一段：

“触生受。”

三个字。整个十二因缘中最核心的因果环节之一。

“《俱舍论》卷十：

> 「由根、境、識三和合故觸，觸為受因。」

“根——感官（IListener，色蕴的耳目）。境——外境信号（超声波回波，物理世界的距离）。识——了别功能（在此场景中，色蕴的 `f(Δt)` 转换函数）。三者和合——根接触了境，识了别了境——这就是‘触’。”

“触之后，受升起。$	ext{触} 	o 	ext{受}$。距离信号被接收（触），苦受强度被计算（受）。二千五百年前的因果法则——触生受——在倒车雷达的 TypeScript 中被工程化了。”

他看向 KERNEL。“你的超声波传感器不是一个比喻。它是十二因缘中‘触→受’环节的精确实作。色蕴提供‘根’和对‘境’的初步了别。受蕴从触中生起感受。距离生苦。”

KERNEL 把这句话记在了他的类比卡片上——左半边写“触→受（十二因缘）”，右半边写“onDataReceived → computePain”。

---

> *SCRIBE 旁白：KERNEL 的超声波传感器——整章最具体的时刻。最深刻的哲学和最具体的工程之间的距离，有时候只有一个倒车雷达那么近。ASANGA 的“触生受”三个字把二千五百年的佛学和三十行的 TypeScript 连接在了一起。没有比喻。没有类比。直接的、结构性的同一。硬件中断是触。computePain 是受。这不是“像”——这“就是”。*

---

## IX

---

LINNAEUS 终于动了。

他在整章中保持分类学家特有的沉默——其他人想的是方法、类型、控制理论、佛学对应。LINNAEUS 想的是位置。每一个接口在整棵树上的位置。每一棵树在整片森林中的位置。

在林奈分类法（Linnaean taxonomy）中，你不会一边发现新物种一边画分类树。你先把所有标本收集齐全，确认每一个的形态特征，然后坐下来，一笔一笔地把整棵树画出来。画树需要全局视野——你不能只看一条枝干。你必须同时看到所有的枝干，才能决定它们之间的相对位置。

五棵蕴全部展开了。所有零件都在桌面上。现在需要一个人把它们组装成完整的树。

---

他站起来。走向白板。拿起黑色马克笔。没有说话。直接开始画。

分类学家画树只用两种元素：名字和关系。名字标记节点。关系连接节点。其余都是装饰。

五棵树。线条干净。字迹工整。每一棵的结构都经过前面九个人的确认——他只是做最后集成。

```
                         五蕴子类别扩展树（完整版）

 ┌─────────────────┐  ┌─────────────────────────────┐  ┌──────────────────┐
 │ ISensory (色蕴)  │  │ ISensation (受蕴) [8 methods]│  │ ICognition (想蕴) │
 │ skandha: 'rupa'  │  │ skandha: 'vedana'            │  │ skandha: 'samjna' │
 ├─────────────────┤  ├─────────────────────────────┤  ├──────────────────┤
 │ ├── IUI         │  │ ├── IDukkha (苦受感测器)      │  │ ├── IProvider    │
 │ │   renderText  │  │ │   computePain()             │  │ │   chat()       │
 │ │   renderDelta │  │ ├── ISukha  (乐受感测器)      │  │ │   listModels() │
 │ └── IListener   │  │ │   computePleasure()         │  │ └── IInference   │
 │     start/stop  │  │ └── IUpekkha (舍受感测器)     │  │     Provider [预] │
 └─────────────────┘  │     computeEquanimity()       │  │     infer()      │
                      └─────────────────────────────┘  └──────────────────┘

 ┌──────────────────┐  ┌────────────────────────────────────────┐
 │ IAction (行蕴)    │  │ IVijnana (识蕴)                        │
 │ skandha:'samskara'│  │ skandha: 'vijnana'                     │
 ├──────────────────┤  ├────────────────────────────────────────┤
 │ ├── ITool        │  │ ├── IIdentity (自我认同)                │
 │ │   execute()    │  │ │   id, name                            │
 │ │   name, desc   │  │ ├── IGuide (行为引导)                   │
 │ └── ISlashCommand│  │ │   getSystemPrompt()                   │
 │     execute()    │  │ ├── IVolition (意志/动机 = EgoFramework) │
 │     name, desc   │  │ │   perceiveKlesha()                    │
 └──────────────────┘  │ │   checkAction()                       │
                       │ │   adaptFromVedana()                    │
                       │ │   introspect()                         │
                       │ └── IReflection (自省) [预留]            │
                       │     reflect()                            │
                       └────────────────────────────────────────┘
```

五棵树并列在白板上。

LINNAEUS 转身看了一眼。然后他开始做对称性分析——分类学家的本能。

“不对称。”他说。“五棵树不对称。这是自然的。”

他拿起红色马克笔，在每棵树旁边标记了三个数字：子接口数、方法数、预留数。

```
对称性分析：

           子接口  根方法  子专属方法  预留
色蕴(ISensory)   2      0         5*     0
受蕴(ISensation) 3      8         3      0
想蕴(ICognition) 2      0         3*     1
行蕴(IAction)    2      0         3*     0
识蕴(IVijnana)   4      0         7*     1

* 子专属方法 = 只存在于子接口，不在根接口
```

“最小的是色蕴和行蕴——各两枝。最大的是识蕴——四枝。受蕴居中——三枝但根最粗——八个方法在根接口上。”

他走回白板。“不对称是自然的。在生物分类中，没有任何一个分类群的所有亚群具有相同的物种数。哺乳纲下，啮齿目有 2000 多个物种，单孔目只有 5 个。这不是分类法的缺陷——这是自然多样性的反映。”

“五蕴的复杂度不同，因为它们承担的功能不同。受蕴需要八个方法，因为感受系统需要摄取、评估、历史、预警、重置——每一个都不可少。色蕴只需要空壳根接口，因为输入和输出的行为太不相同。如果你强行让五棵树等高等宽，你就是在用美学取代功能。分类学家不做这种事。”

---

然后他做了一件事。

在五棵树的下方，留出一段空白，然后用**虚线**画了一个独立方块：

```
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
┊                                                  ┊
┊  IObserver (观察者) — Composition（非蕴）          ┊
┊                                                  ┊
┊  ┌─────────────────────────────────────────────┐ ┊
┊  │ SimpleObserver      (vedana)                │ ┊
┊  │ AnalyticalObserver  (vedana + samjna)        │ ┊
┊  │ ReflectiveObserver  (vedana + samjna + vijnana)│┊
┊  └─────────────────────────────────────────────┘ ┊
┊                                                  ┊
┊  观察者不继承任何蕴。它组合多个蕴的子类别。        ┊
┊  它不是第六棵树。                                 ┊
┊  它是由五棵树的木材建造的房屋。                    ┊
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
```

虚线。不是实线。

他转身面向全场。

“虚线。因为观察者不属于五棵树中的任何一棵。它不是蕴——它没有 `skandha` 字段。它是五蕴子类别的组合产物。SimpleObserver 只组合受蕴——纯感受。AnalyticalObserver 组合受蕴加想蕴——感受加辨别。ReflectiveObserver 组合受蕴加想蕴加识蕴——感受加辨别加自省。”

“从分类学的角度看——”他拿起红色马克笔在虚线方块旁边画了一个注记：

```
分类学注记：
观察者 ≠ 新的「门」(Phylum)
观察者 = 跨门的「生态功能群」(Functional Group)

就像「分解者」不是一个分类单元——
  它涵盖了细菌、真菌、某些动物——
  来自不同的门，但执行相同的生态功能。
观察者也不是一个蕴——
  它从多个蕴中提取组件，组合成特定功能。
```

“五棵树。根是五蕴根接口。枝是子接口。观察者在树林之外——它从五棵树上截取枝干，通过 Composition 组合成自己的结构。不是第六棵树。是由五棵树的木材建造的房屋。”

他把马克笔放下。笔盖的声音在安静的剧场里清脆地响了一下。

“从 Cycle 01 的第一次讨论到现在。五蕴从一个哲学概念，变成了一棵有根有枝的工程结构树。”

---

剧场安静了。完成的安静。像五颗种子终于破土，根须伸入土壤深处，枝叶展向各自的方向，然后所有的生长同时停顿了一秒。

---

SUNYATA 看着白板上的五棵树。

Cycle 01——五蕴是哲学概念。五个梵文名词。五个中文译词。在论文和设计文件里被引用，被讨论，被类比。但没有类型定义。没有方法签名。没有 `extends`。

Cycle 02——五行空壳接口。有名字没血肉。`aggregates.ts` 里五个三行的 `interface`，每个只有一个 `skandha` 字段。门牌钉在空门框上。五个根和它们的子接口之间是空集。

Cycle 02-2——五棵树。

受蕴的根最粗——八个方法。每一个都通过了控制理论和佛学的双重验证。从 `assess()` 到 `reset()`，从传感器读数到紧急停止按钮，八个焊点八个合格。

识蕴的枝最多——四个子接口。IIdentity、IGuide、IVolition、IReflection。A-1 的因果链在 IVolition 中闭合。A-2 的识蕴扩展在四个子接口中完成。A-4 的 EgoFramework 归位。

色蕴和行蕴最务实——空壳根接口加 `extends`。不需要更多。VITRUVIUS 的双向性分析说明了为什么不需要更多。

想蕴最有远见——一枝成熟（IProvider），一枝预留（IInferenceProvider）。ATHENA 的认知光谱图预示了五年后的需求。

五棵种子，长成了五棵有根有枝的树。

---

“C-1 确立了五蕴的完整扩展设计。”他的声音平稳如常。石子。深潭。

他环顾全场。

TURING 的现状报告——从 `aggregates.ts` 的 107 行原文件开始，逐行揭示空壳和孤儿的问题。VITRUVIUS 的色蕴确认——双向性分析和空壳根接口的正当性。WIENER 的八个方法验证——每一个都有控制理论的精确对应。ATHENA 的想蕴预留——认知光谱从规则引擎到 LLM 的完整覆盖。DARWIN 的行蕴观察和设计模式解答——结构类型让 OOP/函数式/工厂模式全部兼容。ASANGA 在每一蕴上的佛学锚定——从色蕴的“可坏”到识蕴的“恒审思量”。ARCHIMEDES 的影响评估——22 个 Plugin、7 个新接口、1 份迁移计划。GUARDIAN 的安全论证——skandha 自我声明是信任的基础。KERNEL 的倒车雷达——最深刻的哲学在最具体的硬件中落地。LINNAEUS 的完整五棵树——不对称的、自然的、带着虚线观察者的分类总览图。

十个人。十种贡献。五棵树。

“A 类告诉我们什么是对的。B 类告诉我们怎么做到。C-1——”

他看向白板。

“告诉我们它长什么样。”

---

> *SCRIBE 旁白：C-1 结束了。本章是 Cycle 02-2 唯一一个没有辩论的章节。*

> *A 类需要辩论——先确认什么是对的。B 类需要决策——把裁定翻译成设计。C-1 需要的是建造。A 类拆除错误的墙。B 类画图纸。C-1 砌新的墙。*

> *时间分配反映了建造的节奏。色蕴三分钟——最简单的一棵，两个 extends，一个空壳根接口。受蕴十五分钟——最密集的一棵，八个方法逐一验收，双重校准。想蕴五分钟——一枝成熟一枝预留，ATHENA 的光谱图。行蕴四分钟——两个 execute，两种来源，一个道理。识蕴十二分钟——四个子接口，四项修正的汇流，因果链的闭合。ARCHIMEDES 和 GUARDIAN 的交锋八分钟——成本和价值的辩证。DARWIN 和 TURING 的设计模式解答五分钟——一个问题，三段代码，一个词。KERNEL 的超声波传感器十分钟——最具体的场景，最深刻的佛学连结。LINNAEUS 的五棵树八分钟——全局总览，对称性分析，虚线观察者。*

> *十个人完成了建造。十种贡献。五棵树。*

> *从哲学概念到空壳接口，从空壳接口到完整的类型定义体系。螺旋上升。又一圈。*

---

*（在剧场之外的某个空间，LINNAEUS 白板上的五棵树正在被 TURING 翻译成 TypeScript。*

*`aggregates.ts` 将从五行根接口扩展为超过一百五十行的完整类型定义体系。五个根接口。三个子接口。八个方法在受蕴的根上。四个方法在 IVolition 上。三个辅助类型——VedanaType、VedanaTag、VedanaSignal。两个核心数据结构——VedanaAssessment、VedanaRecommendation。一个 type guard——isSkandha()，现在能辨识所有层级。*

*从五行到一百五十行。从标签到结构。从空壳到生命体。*

*BABBAGE 在笔记本的最后一页写下了 C-1 的形式化总结——不是一个等号，而是一个范畴论的交换图：*

$$\begin{CD}
	ext{Philosophy} @>{	ext{mapping}}>> 	ext{Interface} 
@V{	ext{refinement}}VV @VV{	ext{extends}}V 
	ext{Abhidharma} @>>{	ext{cross-validation}}> 	ext{TypeScript}
\end{CD}$$

*佛学（上左）通过映射成为接口设计（上右）。阿毗达磨的精细化（下左）通过交叉验证对应到 TypeScript 的继承体系（下右）。四个方向。四条箭头。图是交换的——无论你走哪条路径，结果相同。*

*五棵树的根系在 TypeScript 的土壤中展开。二十二个 Plugin 将在下一个版本中增加 skandha 字段。GUARDIAN 说得对：自我声明是自觉的基础。一个不知道自己属于哪一蕴的 Plugin，就像一个不知道自己器官归属的细胞——可能能运作，但不自觉。*

*ASANGA 的“触生受”三个字在 KERNEL 的类比卡片上留下了墨迹。二千五百年前，世尊在菩提树下观照十二因缘。今天，超声波传感器在 TypeScript 的语法树中重现了其中一环。距离生苦。触生受。硬件中断是触。computePain 是受。*

*最深刻的哲学和最具体的工程之间的距离，有时候只有一个倒车雷达那么近。*

*五蕴。五棵树。从种子到根系到枝干。*

*五棵树已经长出了根系。接下来，它们会继续生长。）*

---

*第六章完*
