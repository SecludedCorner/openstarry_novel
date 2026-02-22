# 第六章：五棵树的根系

---

SUNYATA 在剧场中央站了片刻，什么都没说。

A 类用了三个章节修正哲学。B 类用了一个章节落实裁定。那些是拆解和决策。现在要做的事情不同——现在要建造。

---

「C-1。五蕴子类别扩展设计。」

他拿起 Master 的信：「『五蕴可以做为根本类别（Root Class），要如何扩展，可以做更详细的安排。』」

「前四章修正了地基。现在，C-1 要在修正过的地基上，把五棵树从种子长成有根、有干、有枝的完整生命体。」

---

> *SCRIBE 旁白：SUNYATA 用了「五棵树」的意象。树是活的，有根会伸展，有枝会分叉。五蕴的扩展不是静态堆砌——它是有机的、向多方向同时展开的生长。*

---

TURING 的屏幕投射到剧场中央。

```typescript
export interface ISensory    { readonly skandha: 'rupa'; }
export interface ISensation   { readonly skandha: 'vedana'; }
export interface ICognition   { readonly skandha: 'samjna'; }
export interface IAction      { readonly skandha: 'samskara'; }
export interface IIdentity    { readonly skandha: 'vijnana'; }
```

五行。每行只有一个字段——一个标签。

「五个根接口。没有方法。没有行为定义。没有子接口继承。它们就像五个只有标签的空盒子。Master 要我们把盒子打开，往里面放东西。」

---

他切换投影，显示现有的具体接口——IUI、IListener、IProvider、ITool、IGuide——每个都有完整的方法定义，但和五个根接口之间没有任何关系。没有 extends。门牌和门是分开的。

BABBAGE 在笔记本上写了一行：`roots ∅ children = orphans`。根和子类别之间是空集。孤儿。

---

SUNYATA 用手指计数。五个设计目标。

「一，根接口增加核心方法。二，现有接口升级为子接口。三，新增必要的子接口。四，观察者用 Composition，不属于任何蕴。五，isSkandha() 全层级可用。」

「现在，逐蕴展开。」

---

## I

---

「色蕴。ISensory。」

VITRUVIUS 站了起来。「色蕴最简单。两个子接口已经存在。IUI 负责输出渲染——嘴巴，说出去的。IListener 负责感官输入——耳朵，听进来的。只需要让它们 extends ISensory。」

TURING 投射修改后的定义：

```typescript
export interface ISensory {
  readonly skandha: 'rupa';
}

export interface IUI extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
  renderText?(text: string, sessionId?: string): void;
  renderDelta?(delta: string, sessionId?: string): void;
}

export interface IListener extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
}
```

「ISensory 根接口保持空壳。IUI 和 IListener 方向完全相反——输出和输入，强行统一会制造虚假的抽象。」

ASANGA 补了一句。「色蕴是接触——和外境的接触。IUI 和 IListener 代表接触的两个方向。往外的和往内的。」

---

> *SCRIBE 旁白：色蕴三分钟。一个 extends。最短的一条根入土了。*

---

## II

---

「受蕴。ISensation。」SUNYATA 的声音微微放慢。所有人都知道受蕴将是根系最庞大的一棵。

TURING 投射完整接口。

```typescript
export interface ISensation {
  readonly skandha: 'vedana';
  assess(): VedanaAssessment;
  ingestMetrics(metrics: Record<string, number>): void;
  ingestToolResult(toolName: string, isError: boolean, durationMs: number): void;
  ingestLLMResult(tokenCount: number, stopReason: string): void;
  getVedanaTag(): VedanaTag;
  onVedana(type: VedanaType, threshold: number, handler: (signal: VedanaSignal) => void): () => void;
  getHistory(windowSize: number): readonly VedanaAssessment[];
  reset(): void;
}
```

WIENER 站了起来，逐一点过八个方法。

「assess()——传感器读数。三个 ingest 方法——不同接口的输入通道。getVedanaTag()——快取查询。onVedana()——事件驱动的阈值监测，苦受超过 0.8 才通知。getHistory()——滑动窗口历史。reset()——紧急停止。」

「受蕴的根接口不再是空壳——它是一个完整的传感器接口。」

---

ASANGA 站起来。「受蕴只做一件事：感受。不判断，不分析。碰到火——苦。吃到甜——乐。无事发生——舍。八个方法，每一个都在『感受』的范围内。没有任何一个方法越界做了判断。」

他看向 WIENER。「你的控制理论说它们是传感器方法。我的佛学说它们是受蕴方法。同一件事，两种语言。」

---

TURING 投射三受子接口——IDukkha（苦受）、ISukha（乐受）、IUpekkha（舍受），各自继承 ISensation，各有一个 compute 方法。

WIENER 补充：「三个通道。三个 PID 回路。Cycle 02 的三通道架构，现在有了类型系统的保障。」他在方格纸上重重勾了三个勾。「到位。」

---

> *SCRIBE 旁白：受蕴十五分钟，色蕴的五倍。八个方法需要控制理论验证和佛学确认。双重校准——这是 Cycle 02-2 的纪律。*

---

## III

---

「想蕴。ICognition。」

ATHENA 站起来。

```typescript
export interface ICognition {
  readonly skandha: 'samjna';
}

export interface IProvider extends ICognition {
  readonly id: string;
  chat(request: ChatRequest): AsyncIterable<StreamEvent>;
  listModels?(): Promise<ModelInfo[]>;
}

export interface IInferenceProvider extends ICognition {
  readonly id: string;
  infer(input: unknown): Promise<unknown>;
}
```

「IProvider——LLM 认知，现在的主力。IInferenceProvider——非 LLM 推理，规则引擎、决策树。认知不等于语言模型。」

DARWIN 前倾。「演化上，IInferenceProvider 是更原始的认知——趋光性。IProvider 是更高级的——语言推理。同一棵树的两条枝。」

---

## IV

---

「行蕴。IAction。」

```typescript
export interface IAction {
  readonly skandha: 'samskara';
}

export interface ITool extends IAction {
  readonly name: string;
  readonly description: string;
  readonly parameters: unknown;
  execute(args: Record<string, unknown>, ctx: ToolContext): Promise<string>;
}

export interface ISlashCommand extends IAction {
  readonly name: string;
  readonly description: string;
  execute(args: string, ctx: IPluginContext, sessionId?: string): Promise<string | undefined>;
}
```

DARWIN 站了起来。「ITool——Agent 自主调用的行动。ISlashCommand——外部指令触发的行动。来源不同，本质相同。都是意志的实现。」

ASANGA 一句话。「行蕴涵盖一切造作。工具的 execute 是造作，指令的 execute 也是造作。」

---

## V

---

「识蕴。IVijnana。」SUNYATA 语速比前四蕴都慢。这是最重的一棵树。

A-2 把 IIdentity 从整个识蕴降级为子接口。A-4 把 EgoFramework 搬回识蕴。两项修正让识蕴从单根变成了四枝大树。

ASANGA 站了起来。前四蕴他都只是从座位上补充一句。识蕴不同——这是他的蕴。

---

TURING 投射完整识蕴体系。

```typescript
export interface IVijnana {
  readonly skandha: 'vijnana';
}

export interface IIdentity extends IVijnana {
  readonly id: string;
  readonly name: string;
}

export interface IGuide extends IVijnana {
  readonly id?: string;
  getSystemPrompt(): Promise<string>;
}

export interface IVolition extends IVijnana {
  perceiveKlesha(vedanaAssessment: VedanaAssessment): KleshaSignal[];
  checkAction(action: ProposedAction): EgoCheckResult;
  adaptFromVedana(assessment: VedanaAssessment): void;
  introspect(): EgoIntrospection;
}

export interface IReflection extends IVijnana {
  reflect(context: unknown): Promise<unknown>;
}
```

ASANGA 逐一确认。

「IIdentity——我是谁。IGuide——我应该怎么做。」

「IVolition。」他停了两拍。「A-1 的因果链在这里落地——我执产生烦恼（perceiveKlesha），烦恼驱动行动检查（checkAction），受蕴反馈给意志做适应（adaptFromVedana），意志能自我审视（introspect）。A-1 到 A-4 的修正，在类型系统中完成闭合。」

「IReflection。自省。预留的。门框在那里，门板留给未来。」

最后他说：「识蕴在 Cycle 02 中只有一个 IIdentity。现在四个子接口——认同、引导、意志、自省。第三章我用城市比喻说识蕴不等于 IIdentity。现在城市有了四个区。」

---

> *SCRIBE 旁白：五蕴逐一展开。色蕴三分钟，受蕴十五分钟，想蕴五分钟，行蕴四分钟，识蕴十二分钟。时间自然反映根系复杂度。五棵树，五种生长速度，但都已扎根。*

---

## VI

---

ARCHIMEDES 一直在等。五页工程笔记填完了。

「让我说一个数字。二十二。」

「v0.24.0-beta 有二十二个 Plugin。每一个都需要增加 skandha 字段。」

他举了几例——Discord UI 加 `skandha: 'rupa'`，OpenAI Provider 加 `skandha: 'samjna'`，file read 工具加 `skandha: 'samskara'`。

「这是 breaking change。类型系统会拒绝没有 skandha 字段的 Plugin。」

---

GUARDIAN 站起来。「我支持这个 breaking change。」理由不是工程的，是安全的。

「每个 Plugin 声明自己的蕴归属，是自觉的基础。协调层需要知道每个 Plugin 的归属。没有这个字段，分类查询返回 unknown。unknown 意味着最低信任。」

ARCHIMEDES 补充：「大部分修改是机械性的。真正需要设计的新接口七个，其中两个是预留空壳。可行。」

---

> *SCRIBE 旁白：ARCHIMEDES 的「二十二」和 GUARDIAN 的「自觉」。工程师算成本，安全专家论价值。答案是同一个：skandha 字段。一个只读字符串，让每个 Plugin 在类型系统中拥有了身份。*

---

## VII

---

DARWIN 站起来，语速比平常快。

「Master 说过——『Plugin 不一定都是 OOP，但要如何让不同设计模式都兼容？』」

TURING 用三段并排的代码回答：OOP 风格用 `class implements ITool`，函数式风格用 `function createTool(): ITool`，工厂模式用 `ToolFactory.create()`。三种风格，同一个 ITool 接口。

DARWIN 解释关键词——**Structural**。

「TypeScript 是结构类型。不需要写 `implements`。只要对象有 skandha 字段、有 name、有 execute 方法，它就是 ITool。接口是契约，不是枷锁。」

BABBAGE 写了一行：`structural typing → interface = contract, NOT inheritance requirement`。

「Master 的问题——答案已经在 TypeScript 的类型系统里了。」

---

> *SCRIBE 旁白：答案的优雅在于否定性——不需要额外设计。有时候最好的设计决策就是认识到你不需要额外设计。*

---

## VIII

---

KERNEL 已经忍了很久了。「Master 提到了超声波传感器。」

他在白板角落画了一个长方形，上半部分：**色蕴 (IListener)**，下半部分：**受蕴 (IDukkha)**。

「超声波碰撞传感器。倒车雷达。一个 Plugin，两蕴。色蕴接收原始回波信号——距离数值。受蕴把距离转化为苦受强度——三十公分微弱苦受，十公分剧烈苦受。」

TURING 投射代码——UltrasonicCollisionSensor implements IListener，内部持有 IDukkha。色蕴接收，受蕴感受，通过 Composition 组合在一个 Plugin 中。

KERNEL 笑了。「倒车雷达嘀嘀嘀。你以为它只在量距离。其实色蕴在测距离，受蕴在感受苦。距离是物理量，苦是感受量。两蕴协作。」

ASANGA 点头。「触生受——十二因缘最核心的环节。二千五百年前的因果法则，在倒车雷达的 TypeScript 中被工程化了。」

---

> *SCRIBE 旁白：最深刻的哲学和最具体的工程之间的距离，有时候只有一个倒车雷达那么近。*

---

## IX

---

LINNAEUS 终于动了。分类学家在整章中保持沉默——其他人想的是方法和类型，他想的是位置。每一个接口在整棵树上的位置。

五棵蕴全部展开了。现在需要有人把它们组装成完整的树。

---

他走向白板，拿起马克笔，直接开始画。

```
ISensory (色蕴)              ISensation (受蕴) [8 methods]
├── IUI (输出渲染)            ├── IDukkha (苦受传感器)
└── IListener (感官输入)       ├── ISukha (乐受传感器)
                              └── IUpekkha (舍受传感器)

ICognition (想蕴)             IAction (行蕴)
├── IProvider (LLM 认知)      ├── ITool (工具)
└── IInferenceProvider [预留]  └── ISlashCommand (指令)

IVijnana (识蕴)
├── IIdentity (自我认同)
├── IGuide (行为引导)
├── IVolition (意志/动机 = EgoFramework)
└── IReflection (自省) [预留]
```

五棵树并列在白板上。然后他在下方用虚线画了一个独立方块：

```
IObserver (观察者) — Composition      [虚线]
├── SimpleObserver (vedana)
├── AnalyticalObserver (vedana + cognition)
└── ReflectiveObserver (vedana + cognition + vijnana)
```

虚线——因为观察者不属于五棵树中的任何一棵。它从五棵树上截取枝干，通过 Composition 组合成自己的结构。不是第六棵树，是由五棵树的木材建造的房屋。

他放下马克笔。「从 Cycle 01 到现在。五蕴从哲学概念，变成了有根有枝的工程结构树。」

---

剧场安静了。像五颗种子破土，根须伸入土壤，枝叶展向各自的方向。

SUNYATA 看着白板上的五棵树。

Cycle 01——五蕴是哲学概念。Cycle 02——五行空壳接口。Cycle 02-2——五棵树。受蕴根最粗，八个方法。识蕴枝最多，四个子接口。色蕴和行蕴最务实——只需要 extends。想蕴最有远见——一枝成熟，一枝预留。

---

「C-1 确立了五蕴的完整扩展设计。」

「A 类告诉我们什么是对的。B 类告诉我们怎么做到。C-1——」

他看向白板。

「告诉我们它长什么样。」

---

> *SCRIBE 旁白：C-1 结束了。本章没有辩论。A 类需要辩论——确认什么是对的。B 类需要决策——把裁定翻译成设计。C-1 需要建造。十个人完成了建造，五棵树。从哲学概念到空壳接口，从空壳接口到完整的类型定义体系。螺旋上升，又一圈。*

---

*（在剧场之外，LINNAEUS 白板上的五棵树正在被 TURING 翻译成 TypeScript。*

*`aggregates.ts` 将从五行扩展为超过一百五十行。五个根接口，十三个子接口，八个方法在受蕴的根上。*

*从五行到一百五十行。从标签到结构。从空壳到生命体。*

*五棵树的根系在 TypeScript 的土壤中展开。二十二个 Plugin 将增加 skandha 字段——自我声明是自觉的基础。*

*五棵树已经长出了根系。接下来，它们会继续生长。）*

---

*第六章完*
