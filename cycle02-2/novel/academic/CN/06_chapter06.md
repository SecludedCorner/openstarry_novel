# 第六章：五棵树的根系

---

SUNYATA 在剧场中央站了片刻，什么都没说。

A 类用了三个章节修正哲学。B 类用了一个章节落实裁定。那些是拆解和决策。现在要做的事情不同。

现在要建造。

---

「C-1。五蕴子类别扩展设计。」

他拿起 Master 的信，找到那一段。

「『五蕴可以做为面向对象中的根本类别（Root Class），要如何扩展，可以做更详细的安排。』」

他放下信。「前四章修正了地基。现在，C-1 要在修正过的地基上，把五棵树从种子长成有根、有干、有枝的完整生命体。」

他看向 TURING。「让我们先看看种子现在长什么样。」

---

> *SCRIBE 旁白：SUNYATA 用了「五棵树」的意象。墙壁和柱子是死的。树是活的。树有根，根会伸展。树有枝，枝会分叉。五蕴的扩展不是静态的堆砌——它是有机的、向多个方向同时展开的生长。*

---

TURING 的屏幕投射到剧场中央。冷光。白底。黑字。

```typescript
export interface ISensory    { readonly skandha: 'rupa'; }
export interface ISensation   { readonly skandha: 'vedana'; }
export interface ICognition   { readonly skandha: 'samjna'; }
export interface IAction      { readonly skandha: 'samskara'; }
export interface IIdentity    { readonly skandha: 'vijnana'; }
```

五行。每一行只有一个字段。`readonly skandha`。一个标签。

「五个根接口。没有方法。没有行为定义。没有子接口继承。」

他让投影停留了几秒。五行字像五个只写了名字的门牌钉在五扇还没建好的门上。

「它们就像五个只有标签的空盒子。Master 要我们把盒子打开，往里面放东西。」

---

他切换投影。

```typescript
export interface IUI { ... }       // 色蕴？未继承 ISensory
export interface IListener { ... } // 色蕴？未继承 ISensory
export interface IProvider { ... } // 想蕴？未继承 ICognition
export interface ITool { ... }     // 行蕴？未继承 IAction
export interface IGuide { ... }    // 识蕴？未继承 IIdentity
```

「现有的具体接口。它们各自有完整的方法定义。但它们和五个根接口之间没有任何关系。没有 extends。没有继承。门牌和门是分开的。你知道 IUI 应该属于色蕴，但类型系统不知道。」

BABBAGE 在笔记本上写了一行：`roots ∅ children = orphans`。根和子类别之间是空集。孤儿。

---

SUNYATA 用手指计数。五个设计目标。

「一。每个蕴的根接口增加核心方法。二。现有接口升级为子接口——IUI extends ISensory，以此类推。三。新增必要的子接口——IVijnana 体系、三受接口。四。观察者用 Composition，不属于任何蕴。五。isSkandha() 全层级可用。」

五根手指收回。「现在，逐蕴展开。」

---

## I

---

「色蕴。ISensory。」

VITRUVIUS 站了起来。色蕴——形相与物质性——是全端架构分析师最直觉的领域。

「色蕴是最简单的一棵。两个子接口已经存在了。IUI 负责输出渲染——嘴巴，说出去的。IListener 负责感官输入——耳朵，听进来的。只需要让它们 extends ISensory。」

TURING 投射了修改后的定义。

```typescript
export interface ISensory {
  readonly skandha: 'rupa';
}

export interface IUI extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
  renderText?(text: string, sessionId?: string, replyTo?: string): void;
  renderDelta?(delta: string, sessionId?: string, replyTo?: string): void;
}

export interface IListener extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
}
```

「ISensory 根接口保持空壳。」TURING 说。「IUI 和 IListener 的行为方向完全相反——输出和输入。强行统一到一个共通方法里会制造虚假的抽象。根的存在是为了 isSkandha('rupa') 能通过。」

ASANGA 从座位上补了一句。「色蕴是接触。和外境的接触。IUI 和 IListener 代表接触的两个方向。往外的和往内的。」

---

> *SCRIBE 旁白：色蕴三分钟。一个 extends。一棵树的第一条根——最短的一条——入土了。*

---

## II

---

「受蕴。ISensation。」SUNYATA 的声音微微放慢了。所有人都知道受蕴将是五棵树中根系最庞大的一棵。

WIENER 已经在翻方格纸了。「ISensation 是变化最大的。」SUNYATA 说。「从空壳变成八个核心方法。WIENER，逐一确认。」

TURING 投射了完整接口。

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

WIENER 站了起来，用手指逐一点过——像工程师验收流水线的每一个工站。

「assess()——传感器读数函数。ingestMetrics/ingestToolResult/ingestLLMResult——三个输入通道，复合传感器的不同接口。getVedanaTag()——O(1) 缓存查询，仪表板上的数字。」

他停了一下。嘴角微微上扬。

「onVedana()——看门狗计时器的泛化。不连续轮询，在苦受超过 0.8 的时候才通知订阅者。事件驱动的阈值监测。getHistory()——滑动窗口历史，PID 控制器积分项的基础。reset()——紧急停止按钮。」

八个方法，八个控制理论对应。「受蕴的根接口不再是空壳——它是一个完整的传感器接口。」

---

ASANGA 站了起来。受蕴需要比色蕴更多的空间。

「受蕴只做一件事。感受。不判断。不分析。碰到火——苦。吃到甜——乐。无事发生——舍。」

他看了看投影上的八个方法。「八个方法。每一个都在『感受』的范围之内。assess 是感受的输出。ingest 系列是感受的输入。onVedana 是感受的预警。getHistory 是感受的回忆——纯粹的感受记录。没有任何一个方法越界做了判断。」

他看向 WIENER。「你的控制理论说它们是传感器的方法。我的佛学说它们是受蕴的方法。」

WIENER 记了一行：`ISensation: 8 methods. Sensor ≡ Vedana. Cross-validated.`

---

TURING 投射三受子接口。

```typescript
export interface IDukkha extends ISensation {
  readonly vedanaType: 'dukkha';
  computePain(metrics: Record<string, number>): number;
}

export interface ISukha extends ISensation {
  readonly vedanaType: 'sukha';
  computePleasure(metrics: Record<string, number>): number;
}

export interface IUpekkha extends ISensation {
  readonly vedanaType: 'upekkha';
  computeEquanimity(metrics: Record<string, number>): number;
}
```

WIENER 从座位上补充：「三个通道。三个 PID 回路。Cycle 02 的三通道架构，现在有了类型系统的保障。」他在方格纸上勾了三个勾——比第五章的七个勾更重，力度把纸面压出了三个小凹痕。「到位。」

---

> *SCRIBE 旁白：受蕴十五分钟，色蕴的五倍。八个方法，每一个都需要 WIENER 的控制理论验证和 ASANGA 的佛学确认。双重校准。这是 Cycle 02-2 的纪律。*

---

## III

---

「想蕴。ICognition。」

ATHENA 站起来。想蕴——认知与辨别——是她最核心的专业。

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

「IProvider——LLM 认知，现在的主力。IInferenceProvider——非 LLM 推理，规则引擎、决策树。预留的，但重要。认知不等于语言模型。」

ASANGA 一句。「想蕴是辨别。辨别不只有一种方式。」

DARWIN 前倾。「演化上，IInferenceProvider 是更原始的认知——趋光性，基于规则。IProvider 是更高级的——语言推理。同一棵树的两条枝，长在不同高度。」

---

## IV

---

「行蕴。IAction。」

DARWIN 完全站了起来。行蕴是他观察软件行为模式的核心透镜。

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

「ITool——Agent 自主调用的行动。ISlashCommand——外部指令触发的行动。来源不同，本质相同。都是 samskara。都是意志的实现。」

ASANGA 的一句话。「行蕴涵盖一切造作。思（cetana）是行蕴的核心。工具的 execute 是造作。指令的 execute 也是造作。」

---

## V

---

「识蕴。IVijnana。」SUNYATA 的语速比前四蕴都慢。这是重量最大的一棵树。

A-2 把 IIdentity 从整个识蕴降级为子接口。A-4 把 EgoFramework 从受蕴搬回识蕴。两项修正加在一起，让识蕴从 Cycle 02 的单根变成了四条主枝的大树。

ASANGA 站了起来。在前面四蕴，他都是从座位上补充一句。但识蕴不同。这是他的蕴。

---

TURING 投射了完整识蕴体系。

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
  readonly name?: string;
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

ASANGA 逐一确认。语速不快——每一个子接口都值得一个完整的呼吸。

「IIdentity——我是谁。IGuide——我应该怎么做，末那识的『我见』面向。」

「IVolition。」他停了两拍。「A-1 的因果链在这里落地——我执产生烦恼（perceiveKlesha），烦恼驱动行动检查（checkAction），受蕴回馈给意志做适应（adaptFromVedana），意志能自我审视（introspect）。EgoFramework 是 IVolition 的实作。A-4 的结论。A-1 的因果链。在类型系统中完成闭合。」

BABBAGE 微微点头。笔记本上从 A-1 到 A-4 的修正轨迹，每一条都指向一个被划掉的等号。现在所有替代表述在 IVolition 的四个方法中得到了最终类型定义。

「IReflection。自省。Master 的原话：第七意识要能自省。预留的。门框在那里，门板留给未来。」

---

ASANGA 最后说了一句。「识蕴在 Cycle 02 中只有一个 IIdentity。现在四个子接口——认同、引导、意志、自省。第三章我用城市比喻说明识蕴不等于 IIdentity。现在城市有了四个区。市政府只是其中一个。」

---

> *SCRIBE 旁白：五蕴逐一展开。色蕴三分钟。受蕴十五分钟。想蕴五分钟。行蕴四分钟。识蕴十二分钟。时间自然反映根系复杂度。受蕴从空壳到八个方法加三个子接口。识蕴从一个门牌到四个子接口。五棵树，五种生长速度。但此刻都已扎根。*

---

## VI

---

ARCHIMEDES 一直在等。五页工程笔记填完了。他开始算账。

「让我说一个数字。」

全场安静。

「二十二。」

「v0.24.0-beta 有二十二个 Plugin。十二个官方，十个核心组件。每一个都需要增加一个 skandha 字段。」

他列了几例——Discord UI 加 `skandha: 'rupa'`，OpenAI Provider 加 `skandha: 'samjna'`，file read 工具加 `skandha: 'samskara'`。

「这是一个 breaking change。每一个现有 Plugin 都需要修改。类型系统会拒绝没有 skandha 字段的 Plugin——你的 Plugin 不知道自己属于哪一蕴。」

---

GUARDIAN 站了起来。

「我支持这个 breaking change。」理由不是工程的。是安全的。

「每一个 Plugin 声明自己的蕴归属，是自觉的基础。」

他在白板下方写了一行：**skandha: self-declaration**

「信任的前提是——我知道你是什么。协调层——B-4 的独立 Daemon——需要知道每个 Plugin 的蕴归属。没有这个字段，分类查询返回 unknown。unknown 意味着最低信任。」

ARCHIMEDES 补充了影响矩阵：

```
升级影响：
├── aggregates.ts        → 5 空壳 → 完整接口体系
├── IUI/IListener        → +extends ISensory
├── IProvider            → +extends ICognition
├── ITool               → +extends IAction
├── IGuide/IIdentity     → +extends IVijnana
├── 新增 IVijnana/IVolition/IReflection  → 识蕴体系
├── 新增 IDukkha/ISukha/IUpekkha        → 受蕴三受
├── 新增 IInferenceProvider/ISlashCommand → 预留+指令
├── 22 个 Plugin 实作    → 各需 +skandha 字段
└── isSkandha() type guard → 更新
```

「不小。但不是不可控。大部分修改是机械性的。真正需要设计的新接口七个，其中两个是预留的空壳。可行。」

---

> *SCRIBE 旁白：ARCHIMEDES 的「二十二」和 GUARDIAN 的「自觉」。工程师算成本，安全专家论价值。答案是同一个：skandha 字段。一个只读字符串。让每一个 Plugin 在类型系统中拥有了身份。*

---

## VII

---

DARWIN 站了起来，语速比平常快。

「Master 说过一句话——『Plugin 的建立希望是可以多样化的，不一定都是 OOP，但是我又要如何让 plugin 的设计模式都兼容呢？』」

「我们刚设计的五蕴接口体系全部基于 interface 和 extends。一个不使用 class 的开发者会不会被排斥在外？」

---

TURING 用代码回答。三段并排投射。

OOP 风格：

```typescript
class FileReadTool implements ITool {
  readonly skandha = 'samskara' as const;
  readonly name = 'file_read';
  readonly description = 'Read a file';
  readonly parameters = { /* JSON Schema */ };
  async execute(args: Record<string, unknown>, ctx: ToolContext): Promise<string> {
    return fs.readFile(args.path as string, 'utf-8');
  }
}
```

函数式风格：

```typescript
function createFileReadTool(): ITool {
  return {
    skandha: 'samskara',
    name: 'file_read',
    description: 'Read a file',
    parameters: { /* JSON Schema */ },
    execute: async (args, ctx) => fs.readFile(args.path as string, 'utf-8'),
  };
}
```

工厂模式：

```typescript
const fileReadTool = ToolFactory.create({
  skandha: 'samskara',
  name: 'file_read',
  description: 'Read a file',
  parameters: { /* JSON Schema */ },
  handler: async (args) => fs.readFile(args.path as string, 'utf-8'),
});
```

---

DARWIN 走到投影前面。「三种风格。同一个 ITool 接口。关键在一个词——**Structural**。」

「TypeScript 是结构类型。不需要 `implements`。只要对象有 skandha 字段、有 name、有 execute 方法，它就是 ITool。」

他退后一步。「接口是契约，不是枷锁。」

BABBAGE 写了一行：`structural typing → interface = contract, NOT inheritance requirement`。他微微点头——在数学中，同构的定义也是结构性的，不是名义性的。

「Master 的问题——答案已经在 TypeScript 的类型系统里了。」DARWIN 回座位时说了最后一句：「就像演化不关心基因突变是怎么发生的。它只关心表现型是否适应环境。接口就是环境。」

---

> *SCRIBE 旁白：三个人在五分钟之内回答了 Master 的问题。答案的优雅在于否定性——不需要额外设计。TypeScript 的结构类型系统本身就是答案。有时候最好的设计决策就是认识到你不需要额外设计。*

---

## VIII

---

KERNEL 已经忍了很久了。

「Master 提到了超声波传感器。」他站起来，声音带着硬件工程师特有的兴奋。

他在白板角落画了一个长方形，里面一条分隔线。上半部分：**色蕴 (IListener)**。下半部分：**受蕴 (IDukkha)**。

「超声波碰撞传感器。倒车雷达。一个 Plugin，两蕴。色蕴接收原始回波信号——距离数值。受蕴把距离转化为苦受强度——三十公分微弱苦受，十公分剧烈苦受。」

TURING 投射代码。

```typescript
class UltrasonicCollisionSensor implements IListener {
  readonly skandha = 'rupa' as const;
  private readonly dukkhaSensor: IDukkha;

  constructor(dukkha: IDukkha) {
    this.dukkhaSensor = dukkha;
  }

  async start() { /* 启动超声波硬件 */ }

  onDataReceived(rawDistance: number) {
    const metrics = { collision_distance: rawDistance };
    const painIntensity = this.dukkhaSensor.computePain(metrics);
    this.dukkhaSensor.ingestMetrics(metrics);
  }
}
```

KERNEL 指着代码。「implements IListener——色蕴。内部持有 IDukkha——受蕴。通过 Composition。色蕴接收，受蕴感受。两个不同的蕴，组合在一个 Plugin 中。」

他退后一步，笑了。「倒车雷达嘀嘀嘀。你以为它只在量距离。其实色蕴在测距离，受蕴在感受苦。距离是物理量。苦是感受量。两蕴协作。」

WIENER 画了信号流图：

```
Raw Signal → IListener(色蕴) → Metric → IDukkha(受蕴) → Pain Intensity
```

「完美的跨蕴信号流。每一步在自己的蕴之内。跨蕴通信通过方法调用，不通过继承。Composition。」

ASANGA 点头。「触生受。十二因缘最核心的因果环节。色蕴接收信号，受蕴产生苦受。距离生苦。二千五百年前的因果法则，在倒车雷达的 TypeScript 中被工程化了。」

---

> *SCRIBE 旁白：KERNEL 的超声波传感器——整章最具体的时刻。最深刻的哲学和最具体的工程之间的距离，有时候只有一个倒车雷达那么近。*

---

## IX

---

LINNAEUS 终于动了。

他在整章中保持分类学家特有的沉默——其他人想的是方法、类型、控制理论。LINNAEUS 想的是位置。每一个接口在整棵树上的位置。

五棵蕴全部展开了。所有零件都在桌面上。现在需要一个人把它们组装成完整的树。

---

他站起来。走向白板。拿起黑色马克笔。没有说话。直接开始画。

五棵树。线条干净。字迹工整。分类学家画树只用名字和关系——因为树的意义完全由名字和关系定义。

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

五棵树并列在白板上。最小的是色蕴和行蕴——各两枝。最大的是识蕴——四枝。受蕴居中——三枝但根最粗。

然后他做了一件事。在五棵树的下方，用虚线画了一个独立方块：

```
IObserver (观察者) — Composition      [虚线]
├── SimpleObserver (vedana)
├── AnalyticalObserver (vedana + cognition)
└── ReflectiveObserver (vedana + cognition + vijnana)
```

虚线。不是实线。因为观察者不属于五棵树中的任何一棵。它不是树——它是由树的枝干组合而成的建筑。

他转身面向全场。

「五棵树。根是五蕴根接口。枝是子接口。观察者在树林之外——它从五棵树上截取枝干，通过 Composition 组合成自己的结构。不是第六棵树。是由五棵树的木材建造的房屋。」

他把马克笔放下。笔帽的声音在安静的剧场里清脆地响了一下。

「从 Cycle 01 的第一次讨论到现在。五蕴从一个哲学概念，变成了一棵有根有枝的工程结构树。」

---

剧场安静了。完成的安静。像五颗种子终于破土，根须伸入土壤深处，枝叶展向各自的方向，然后所有的生长同时停顿了一秒。

SUNYATA 看着白板上的五棵树。

Cycle 01——五蕴是哲学概念。Cycle 02——五行空壳接口，有名字没血肉。Cycle 02-2——五棵树。受蕴的根最粗，八个方法。识蕴的枝最多，四个子接口。色蕴和行蕴最务实——只需要 extends。想蕴最有远见——一枝成熟，一枝预留。

五棵种子，长成了五棵有根有枝的树。

---

「C-1 确立了五蕴的完整扩展设计。」他的声音平稳如常。石子。深潭。

他环顾全场。TURING 的现状报告。VITRUVIUS 的色蕴确认。WIENER 的八个方法验证。ATHENA 的想蕴预留。DARWIN 的行蕴观察和设计模式解答。ASANGA 在每一蕴上的佛学锚定。ARCHIMEDES 的影响评估。GUARDIAN 的安全论证。KERNEL 的倒车雷达。LINNAEUS 的完整树。

「A 类告诉我们什么是对的。B 类告诉我们怎么做到。C-1——」

他看向白板。

「告诉我们它长什么样。」

---

> *SCRIBE 旁白：C-1 结束了。本章是 Cycle 02-2 唯一一个没有辩论的章节。A 类需要辩论——先确认什么是对的。B 类需要决策——把裁定翻译成设计。C-1 需要的是建造。A 类拆除错误的墙。B 类画图纸。C-1 砌新的墙。*

> *十个人完成了建造。十种贡献。五棵树。*

> *从哲学概念到空壳接口，从空壳接口到完整的类型定义体系。螺旋上升。又一圈。*

---

*（在剧场之外的某个空间，LINNAEUS 白板上的五棵树正在被 TURING 翻译成 TypeScript。*

*`aggregates.ts` 将从五行扩展为超过一百五十行。五个根接口。十三个子接口。八个方法在受蕴的根上。三个辅助类型。两个核心数据结构。一个 type guard。*

*从五行到一百五十行。从标签到结构。从空壳到生命体。*

*五棵树的根系在 TypeScript 的土壤中展开。二十二个 Plugin 将在下一个版本中增加 skandha 字段。GUARDIAN 说得对：自我声明是自觉的基础。一个不知道自己属于哪一蕴的 Plugin，就像一个不知道自己器官归属的细胞——也许能运作，但不自觉。*

*五蕴。五棵树。从种子到根系到枝干。*

*五棵树已经长出了根系。接下来，它们会继续生长。）*

---

*第六章完*
