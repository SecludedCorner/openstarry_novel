# 第三章：差异报告

---

TURING 从不需要准备。

准确地说，他不存在"准备"和"正式开始"之间的分界线。从 SUNYATA 宣布研究对象更新的那刻起，他就已经在工作了。四个终端窗口同时打开，左半边是 v0.22.1-beta，右半边是 v0.24.0-beta，像是在同一具身体的两张不同时间的 X 光片之间来回对比。

他不读设计文件。他读差异。一行一行。一个字符一个字符。

---

其他研究员散开到各小组空间时，TURING 已经完成了分析。SUNYATA 把所有人叫了回来。

"TURING 的差异报告。"

这个郑重大家都认得——在 Cycle 01，TURING 的代码事实报告是所有研究的"锚"。SYNTHESIST 当时的说法："经验锚点。"所有的哲学分析、控制理论、安全评估——无论多精致——都必须能追溯到 TURING 报告中的某一行代码。

现在，锚要再次被钉下。

---

十九人重新聚集。PENROSE 在新椅子上安静等待，像刚加入乐团的新成员，在第一次合奏前倾听首席调音。

TURING 没有寒暄。

"v0.22.1-beta 到 v0.24.0-beta。核心源代码差异。按四个层次报告：新增、修改、标记、问题。"

---

## 一、新文件

"三个新文件。不是三十个。不是十三个。三个。"

他让这个数字停留了一瞬。

"第一个。`aggregates.ts`。一百零七行。五蕴根接口。你们已经看过 ISensation。补充一个事实：五个根接口在结构上完全同构——全部都是只有一个 `readonly skandha` 字段的接口。差异只在注释中。"

"第二个。`aggregates.test.ts`。四十三行。测试五蕴根接口和类型守卫。全部通过。"

"第三个。`events.test.ts`。三十二行。测试事件泛型能正确推导类型。"

他顿了顿。

"还有第四个，属于 Core 而非 SDK。测试 slash command 抛出异常时能正确发出错误事件。"

TURING 少见地提供了背景："在 v0.22.1 中，slash command 出错只会被写进日志，不会通知任何人。用户输入一个有 bug 的命令，界面完全没反应。"

"静默失败。"KERNEL 说。在操作系统工程里，静默失败是最危险的——因为没人知道它发生了。就像你家的火灾报警器坏了但不会发出"我坏了"的提示。

"v0.24.0 修正了。错误现在会通过事件系统广播，UI 可以接收并展示。"

---

## 二、修改文件

TURING 的语速不变，每个数据点花同样的时间。

"十一个修改文件。七个 SDK，四个 Core。"

"`events.ts`。最大的单一变更。新增一百一十六行。为所有事件类型定义了精确的数据结构。"

他投影了一段：

```typescript
export interface AgentEventPayloadMap {
  [AgentEventType.AGENT_STARTED]: { identity: { id: string; name: string } };
  [AgentEventType.LOOP_ERROR]: { error: string; sessionId?: string };
  // ... 覆盖全部事件类型
}
```

"在 Cycle 01，DARWIN 把 `payload?: unknown` 形容为'从不同宇宙穿越来的类型定义'。那个宇宙裂缝现在被封了。但仅限于类型层面——运行时仍是 JavaScript，类型安全不强制执行。"

接下来是六个 SDK 修改，全部同一个模式：旧的五蕴标记被更新，新增 `@skandha` 标记，但接口结构零改变。

"`listener.ts`——旧文字'受蕴'改为'色蕴 sensory input'。`ui.ts`——同样模式。`provider.ts`——新增想蕴标记。`tool.ts`——行蕴。`guide.ts`——识蕴。"

"你们听出来了。五个 SDK 类型文件。全部只改了注释。零行代码变更。"

"标记是文档，不是契约。"ARCHIMEDES 说。区分宣言与实现，是工程师的本能。

---

Core 的四个修改。

"`agent-core.ts`。三处变更。第一：新增 `loadPlugins()` 方法——从只能一个一个加载插件，变成可以批量加载并自动处理依赖顺序。"

MESH 微微挺身。依赖排序是他的日常。

"第二：slash command 错误处理改善。第三——"TURING 多停了零点五秒。"五蕴映射修正。四处行内注释，把原来的'受蕴'改为'色蕴 sensory input'。"

NAGARJUNA 点了一下头。Cycle 01 正是他指出了受蕴被错误映射到 Listener 的问题。开发团队修正了——至少在注释层面。

"但不是所有地方。"TURING 说。这三个字让 GUARDIAN 的注意力瞬间收紧。

---

"`loop.ts`。新增 LLM 超时支持。"

```typescript
const llmTimeout = deps.llmTimeout ?? 120000;
const abortController = new AbortController();
const llmTimer = setTimeout(() => {
  abortController.abort(new Error(`LLM call timed out after ${llmTimeout}ms`));
}, llmTimeout);
```

"v0.22.1 中，LLM 调用没有超时。Provider 不响应的话，系统永久等待——就像打电话给一个永远不接的人，但你的手机不会自动挂断。v0.24.0 加了两分钟超时，可以自定义。"

---

## 三、@skandha 标记

"v0.22.1 中的 @skandha 标记数量：零。"

三秒钟的沉默。

"v0.24.0：二十二个。"

他用外科医生标记切口位置的方式描述分布：

"aggregates.ts 占十个——五个接口各两个。SDK 类型文件五个。events.ts 一个——标记为跨蕴的神经系统。Core infrastructure 五个。"

"最后一个。`safety-monitor.ts`。标记为：vedana 受蕴，三受反馈 placeholder，Plan26 完整实现。"

"Placeholder。"WIENER 重复。"一个安全模块被暂时指定为感受模块的替身。"

"SafetyMonitor 承担了受蕴的部分功能——frustration counter 是苦受的粗糙近似。但它的设计初衷是安全防护。这个 placeholder 承认了两件事：受蕴需要独立实现，SafetyMonitor 在此之前暂代。"

ASANGA 低声说："一个守卫假扮了一个感知者。"

"精确的比喻。"TURING 说。这可能是他整场报告中最接近赞美的一句话。

---

## 四、继承的缺席

TURING 在进入问题清单前，插入了一个结构性观察。

"五蕴根接口已定义。但五个派生接口——IListener、IUI、IProvider、ITool、IGuide——没有一个继承对应的根接口。"

```
IListener  → 应继承 ISensory    → 实际: 无
IUI        → 应继承 ISensory    → 实际: 无
IProvider  → 应继承 ICognition  → 实际: 无
ITool      → 应继承 IAction     → 实际: 无
IGuide     → 应继承 IIdentity   → 实际: 无
```

"五对五。全部未继承。所以 `isSkandha()` 类型守卫无法用于现有的插件——因为它们上面根本没有 `skandha` 字段。类型守卫形同虚设。"

"脚手架搭好了，但没有和既有建筑连接。"VITRUVIUS 用建筑师的语言总结。

> *SCRIBE 记录：LINNAEUS 在分类学笔记中加了惊叹号——他在 Cycle 01 建立的分类体系假设了这些继承关系的存在。BABBAGE 画了一个断裂的箭头。*

---

## 五、问题清单

"七个问题。按严重度排列。"

---

"P1。SEC-01。"

剧场中的温度似乎降了半度。

"package-name 签名绕过。`sandbox-manager.ts`，行 371 至 394。通过 npm 包名加载插件时，签名验证被完全跳过。"

他停了一秒。

"Cycle 01 发现。十个开发版本过去了。"

GUARDIAN 的声音从椅子深处传出。低沉。带着被压抑的东西。

"我再说一遍。Cycle 01 我们明确指出这个漏洞。写在交付文件第一优先级。一个攻击者可以用合法的 npm 名称发布恶意插件，绕过所有签名验证，直接加载到 Agent 环境中。"

顿了顿。

"十个版本。`plugin-signer` 包——我亲自查了。零行修改。连版本号都没变。"

GUARDIAN 没再说话。但他的沉默比话更有重量。

> *SCRIBE 记录：SEC-01 未修复。GUARDIAN 的反应被控制在专业范围内，但每个人都注意到了他在"克制"上花的力气。*

---

"P2。旧映射残留。"

"核心已把 IListener 从受蕴修正为色蕴。但外围文件仍有十一处保留旧映射。一个新开发者读 SDK README 时，仍然会被告知 IListener 是受蕴。"

LINNAEUS 摇头。同一个物种在两本图鉴里有两个名字——分类学家最无法忍受的事。

---

"P3。SDK README 示例与实际代码不符。"

"README 展示的 IUI 有 `render()` 方法——实际接口是 `onEvent()`。IProvider 示例有 `supportedModels`——实际是 `models: ModelInfo[]`。新开发者如果复制 README 示例来建插件，编译就会报错。"

"文档腐化。"DARWIN 说。"文档写在接口稳定之前，之后接口变了但文档没跟上。"

---

"P4。五蕴根接口未被继承。已详述。"

"P5。runner `create-plugin.ts` 五蕴映射未更新。"

他投影了代码：

```typescript
export type PluginType =
  | "tool"      // 行蕴
  | "listener"  // 受蕴     // <-- 应为色蕴
  | "ui"        // 色蕴
  | "provider"  // 想蕴
  | "guide"     // 识蕴
  | "full";
```

"用 `create-plugin` 命令建插件的开发者，会被引导把 listener 归入受蕴。这个文件在两版之间完全未修改。"

---

"P6。版本号不一致。root package.json 更新为 0.24.0-beta，但所有子包仍维持 0.1.0-alpha。"

"P7。README 示例的方法签名与实际完全不符。与 P3 重叠，但这里特指代码块。"

---

TURING 报告完毕。某种极度集中的注意力场回归了静默。

剧场短暂沉默——十九个意识各自在不同光谱中分解同一份报告。

---

ARCHIMEDES 第一个开口。

"三个新文件。十一个修改。七十八个测试。开发团队完成了五蕴框架的脚手架——但仅仅是脚手架。根接口存在但没被继承。标记存在但不是契约。ISensation 有十行注释但只有一行代码。"

停一拍。

"从工程角度，正确的第一步——先建文档约定，再建代码约束。但第二步没走。我们需要告诉他们第二步怎么走。"

---

WIENER 从另一个角度切入。

"ISensation 应该至少定义三个数值通道——DukkhaSensor、SukhaSensor、UpekkhaSensor——每个返回一个标准化的数值。然后是聚合函数，合成为一个 VedanaAssessment。"

他看向 PENROSE。"你之前用了真空态的比喻。但 ISensation 连零点能都没有。它是一个连量子涨落都不存在的空间。"

PENROSE 微微一笑。"严格来说，完全没有涨落的真空在物理学中不存在。ISensation 是一个比物理真空更空的空。"

"数学上的空集。"BABBAGE 精确补充。"空集是一切集合的子集——它被所有可能性包含，但自身不包含任何东西。"

---

ASANGA 等大家说完，然后说：

"我注意到 @skandha 标记的分布有一个有意义的模式。"

"色蕴有六个标记——根接口、SDK、Core，三层一致。想蕴、行蕴、识蕴也一样。但受蕴——只有三个。根接口两个，SafetyMonitor 一个。没有专属的 SDK 类型，没有专属的 Core 实现。因为——"

"因为受蕴还没有自己的模块。"NAGARJUNA 接过话。"SafetyMonitor 是借来的替身。它能感知苦，但不能感知乐，更不能维持舍。一个只有苦受的系统——"

句子悬空半秒。

"——是一个有苦无道的系统。有病但没有药方。永无止尽。"

---

GUARDIAN 在报告结束后又开口了。

"一个补充。`sandbox-manager.ts` 在两版之间完全一致。七百四十八行的主文件，零行修改。过去两个版本的精力全投在了五蕴框架的标记和事件类型安全上。安全子系统被完全跳过。"

KERNEL 补充："包括 import 分析器——我们在 Cycle 01 指出的 ESM 动态 import 绕过问题。零修改。"

---

HERACLITUS 一直安静。作为运行时动态专家，他关注的不是静态结构，而是系统活着时的行为。

"TURING，你报告中有一个隐含的时间线。"

他说："aggregates.ts 是静态声明。@skandha 标记是静态声明。TypedAgentEvent 是静态类型。但 AgentCore 的 `loadPlugins()` 是运行时的——在 Agent 启动时才加载插件。"

声音微微升高。

"骨骼在编译时存在。血肉要到运行时才注入。骨骼和血肉之间的连接——extends 继承——不存在。所以在运行时，五蕴框架其实是一堆散落的标签，不是结构化的类型层级。"

"正确。"TURING 说。"五蕴框架的影响力目前止步于文档注释和开发者的自觉。"

---

SUNYATA 打破了最后的沉默。

"锚已经钉下。"

所有人都认得这个词。

"TURING 给了我们 Cycle 02 的锚。三个新文件，十一个修改，二十二个标记，七个问题，一个六周期未修的安全漏洞，一个只有一行代码的受蕴接口。"

停一拍。

"五条河流即将分流。"

他用极简的语句重新赋予方向——

"R-01 观察者模块。v0.24.0 的五蕴是标记系统而非结构约束。你们设计的观察者需要在这个松散框架上工作。"

"R-02 Vedana 架构。ISensation 是你们的起点。一行代码。把它变成完整的三受系统。"

"R-03 Agent 协调层。SEC-01 未修。安全沙箱要移到协调层。同时解决当前缺口和未来需求。"

"R-04 八识-五蕴映射。aggregates.ts 是开发团队的第一次尝试。判断它是否正确，提供深化方案。"

"R-05 十大宣言。SEC-01 六周期未修的事实会影响你们对宣言工程落地性的评估。"

---

他最后看向 TURING。

TURING 没有表情。他从来没有。但他的视线指向剧场中央仍然悬浮的那段空壳代码。

"你的报告完成了。"SUNYATA 说。

"是的。但 R1 阶段如果有人需要确认代码事实，我随时可用。"

"我知道。"

他说了最后一句话。

"R1 独立研究，正式开始。"

---

十九盏灯各自转向不同方向。

五条河流从同一个山顶——TURING 的差异报告——出发，向五个方向奔流而下。它们会在下游某处重新汇合——那是交叉审阅和辩论的领域。但现在，每一条河流都在独自前进。

TURING 的四个终端窗口依然开着。他知道接下来至少会有七八次其他研究员回来确认代码细节。他不介意。

ISensation 的投影缓缓消散。但它留下的印痕不会消失。

SCRIBE 写下最后一段：

> *Cycle 02，R0 定向结束。R1 独立研究启动。*

> *TURING 的报告确认了基本事实：v0.24.0-beta 是一个标记版本，不是实现版本。五蕴脚手架已搭建，结构约束尚未建立。受蕴为空壳。一个已知漏洞跨越十个版本未修。*

> *十九位研究员。五条课题。一个锚。*

> *河流开始分流。*

---

*（在远处，`aggregates.ts` 的第三十七行写着：*

```typescript
 * Full implementation in Plan26 Vedana Architecture.
```

*一句只有开发者能看到的承诺。现在，十九位研究者也看到了。他们不会等待它被实现——他们会告诉它，当它被实现的时候，应该长成什么样子。）*

---

*第三章完*
