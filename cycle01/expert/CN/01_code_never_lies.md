# 第一章：代码不会说谎

---

二零二六年二月十二日，清晨。

研究频道里还很安静。TURING 已经独自工作了四个小时。

他的屏幕上排列着四个平铺的终端窗口，每一个都开启在 `research doc/20260212_cycle19/openstarry/` 的不同子目录中。左上角是 `packages/core/src/`，右上角是 `packages/sdk/src/`，左下角是 `apps/runner/src/`，右下角则是设计文件。他的阅读方式不是浏览，而是逐行扫描——像一台人形的静态分析器，从入口点开始，沿着每一条 import 路径展开，直到触及叶节点。

TURING 不猜测。他计数。

BABBAGE 在自己的工位上注意到了 TURING 的工作状态。他认得这种模式——穷举遍历。在理论计算机科学中，穷举搜索（brute-force search）的时间复杂度通常是 $O(n)$ 到 $O(n!)$，但它有一个任何启发式方法都不具备的性质：**完备性**（completeness）。如果目标存在于搜索空间中，穷举必然找到它。TURING 不是在寻找什么特定的东西——他在确保没有任何角落被遗漏。

$$	ext{completeness} 	riangleq \forall x \in \Omega: 	ext{visited}(x) = 	ext{true}$$

其中 $\Omega$ 是搜索空间——在这里，就是整个 OpenStarry v0.14.0-beta 的源码。

---

## 一、工厂

第一个让 TURING 停下来的地方是 `packages/core/src/index.ts`。六十二行。他数了一遍导出清单，然后又数了一遍。

“十八个工厂函数。”他在笔记中写道。“零个 class 导出。”

他打开 `agents/agent-core.ts`，四百六十九行。然后是 `execution/loop.ts`，五百四十三行。然后是 `sandbox/sandbox-manager.ts`，七百四十八行。每一个模块的结构都一样：一个 `createXxx()` 函数，接收依赖作为参数，回传一个对象字面量。闭包捕获所有内部状态。没有 `this`。没有 `new`。没有继承链。

TURING 打开了全局搜索。

搜索 `class `（带空格）。核心模块：零结果。SDK：零结果。Runner：零结果。

搜索 `TODO`。零结果。
搜索 `FIXME`。零结果。
搜索 `HACK`。零结果。

BABBAGE 在自己的屏幕前听到这些数字的时候，开始在笔记本上写下一个类型论的观察。工厂函数模式在范畴论中有一个精确的对应——它是一个**态射**（morphism），从配置空间到实例空间：

$$	ext{createXxx}: 	ext{Config} 	o 	ext{Instance}$$

而 class + constructor 模式是一个**函子**（functor），需要额外的 `new` 算子来完成实例化。工厂函数消除了 `new`，使得对象建立成为纯粹的函数调用。在函数式编程的语境中，这是一个重要的选择——它意味着整个 codebase 可以被视为一个由态射组成的范畴 $\mathcal{C}_{	ext{OpenStarry}}$，其中：

- **对象**（objects）是类型：`AgentCore`, `EventBus`, `ExecutionLoop`, ...
- **态射**（morphisms）是工厂函数：`createAgentCore`, `createEventBus`, `createExecutionLoop`, ...
- **合成**（composition）是依赖注入链：`createAgentCore` 内部调用 `createEventBus`，再将结果注入 `createExecutionLoop`

$$	ext{createAgentCore} = 	ext{assemble} \circ (	ext{createEventBus} 	imes 	ext{createEventQueue} 	imes \cdots 	imes 	ext{createTransportBridge})$$

TURING 在频道里发出了今天的第一条讯息。

---

**[研究频道 #code-facts]**

**TURING:** 初步观察。`packages/core/src/index.ts` 导出 18 个工厂函数，零个 class。全局搜索 `class `、`TODO`、`FIXME`、`HACK`，核心模块中均为零结果。工厂函数模式 `createXxx()` + 闭包 + 对象字面量在整个 codebase 中完全统一。无例外。完整导出清单：

```typescript
// packages/core/src/index.ts (62 行)
export { createAgentCore } from './agents/agent-core';
export { createEventBus } from './bus';
export { createEventQueue } from './execution/queue';
export { createExecutionLoop } from './execution/loop';
export { createStateManager } from './state';
export { createContextManager } from './memory/context';
export { createSessionManager } from './session/manager';
export { createToolRegistry } from './infrastructure/tool-registry';
export { createProviderRegistry } from './infrastructure/provider-registry';
export { createListenerRegistry } from './infrastructure/listener-registry';
export { createUIRegistry } from './infrastructure/ui-registry';
export { createGuideRegistry } from './infrastructure/guide-registry';
export { createCommandRegistry } from './infrastructure/command-registry';
export { createPluginLoader } from './infrastructure/plugin-loader';
export { createPluginSandboxManager } from './sandbox';
export { createSecurityLayer } from './security/guardrails';
export { createSafetyMonitor } from './security/safety-monitor';
export { createTransportBridge } from './transport/bridge';
export { createMetricsCollector } from './observability';
```

**DARWIN:** 零 TODO？一个都没有？

**TURING:** 正确。核心模块、SDK、Runner 三层，技术债标记数量为零。

**DARWIN:** 这很不寻常。多数 Beta 版项目至少有几十个。要么是团队纪律极高，要么是他们在 release 前做了一次清扫。从软件进化的角度，零 TODO 的 Beta 版存在两种可能的进化路径：**r-策略**（快速迭代，每次 release 前清扫标记）或 **K-策略**（缓慢但精确的开发，标记从不被引入）。前者的化石纪录通常保留在 git log 中；后者需要异常严格的 code review 文化。

**TURING:** 无法从代码本身判断原因。我只记录事实。

**BABBAGE:** 让我补充一个形式化观察。十八个工厂函数构成了一个完整的**构建代数**（construction algebra）。令 $F = \{f_1, f_2, \ldots, f_{18}\}$ 为工厂函数集合，$T = \{T_1, T_2, \ldots, T_{18}\}$ 为对应的类型集合。则 $	ext{createAgentCore}$ 是唯一的**顶层组装子**（top-level assembler），满足：

$$f_{	ext{core}}: \prod_{i=1}^{k} T_{	ext{dep}_i} 	o T_{	ext{AgentCore}}$$

其中 $k$ 是直接依赖的数量。其余十七个工厂函数都是 $f_{	ext{core}}$ 的子表达式。这是一个**树形组装结构**——不是图，因为没有循环依赖。

---

> *SCRIBE 旁白：TURING 发送这段讯息的方式值得记录。他没有任何前言——没有“大家早安”，没有“我发现了一些有趣的东西”。他直接贴出数据。十八个工厂函数。零个 class。完整的导出清单。在我记录过的所有学者中，TURING 的通讯效率是最高的——他的信息熵（information entropy）接近理论上限，几乎没有冗余。这既是他的强项，也是他的特质：他的讯息从不寒暄，但也从不遗漏。*

---

TURING 继续向下挖掘。他打开了 `createAgentCore()` 的实现，逐行阅读。

这个函数是整个系统的组装点。它在内部一次性建立所有子系统实例——EventBus、EventQueue、SessionManager、ContextManager、六个 Registry、SecurityLayer、SafetyMonitor、MetricsCollector、SandboxManager、PluginLoader、TransportBridge。TURING 数了一下：十六个子模块，全部作为闭包中的局部变量被持有。

KERNEL 在听到“十六个”这个数字时，开始在他的卡片上做对比。在操作系统的语境中，核心初始化序列建立的子系统数量是衡量核心复杂度的重要指标：

| 核心 | 初始化子系统数 | 核心代码行数 | 子系统/行数比 |
|------|-------------|-------------|-------------|
| L4 (Pistachio) | ~5 | ~10,000 | 0.0005 |
| seL4 | ~7 | ~8,700 | 0.0008 |
| QNX Neutrino | ~12 | ~100,000 | 0.00012 |
| Linux 5.x | ~50+ | ~30,000,000 | 0.0000017 |
| **OpenStarry Core** | **16** | **~2,500** | **0.0064** |

KERNEL 注意到 OpenStarry 的子系统密度异常高——每 160 行代码就有一个子系统。这与真实微核心的“宽松组装”形成鲜明对比。在 L4 中，每个子系统由数百到数千行精心优化的代码构成。在 OpenStarry 中，有些子系统只有三十几行（StateManager：33 行）。

他在卡片上写下：

```
OpenStarry Core ≈ 应用级微核心 (Application-Level Microkernel)
                ≈ QNX 的 Resource Manager 模型
                ≠ L4/seL4 的硬件抽象微核心
理由：OStarry 不处理硬件抽象（地址空间、中断、计时器），
      而处理 AI 执行抽象（LLM 调用、工具执行、上下文管理）。
      它运行在 Node.js runtime 之上，不是 bare metal。
```

TURING 在 `start()` 方法中找到了一段有趣的注释：

```typescript
// Start all listeners (受蕴)
// Start all UIs (色蕴)
```

TURING 用荧光笔标记了这两行。然后他打开了 SDK 中的类型定义档案。在 `types/ui.ts` 的开头，他看到了：

```typescript
/**
 * UI interface -- defines how the agent presents itself (色蕴)
 */
export interface IUI {
  id: string;
  name: string;
  render(event: AgentEvent): void | Promise<void>;
  start?(): void | Promise<void>;
  stop?(): void | Promise<void>;
}
```

在 `types/listener.ts` 的开头：

```typescript
/**
 * Listener interface -- receives external input (受蕴)
 */
export interface IListener {
  id: string;
  name: string;
  start?(pushInput: (event: InputEvent) => void): void | Promise<void>;
  stop?(): void | Promise<void>;
}
```

他继续搜索。`types/tool.ts`——没有五蕴注解。`types/provider.ts`——没有。`types/guide.ts`——没有。`infrastructure/tool-registry.ts`——没有。`infrastructure/provider-registry.ts`——没有。`infrastructure/guide-registry.ts`——没有。

TURING 统计了全部的五蕴相关注解。共六处。全部集中在色蕴（UI）和受蕴（Listener）。

想蕴、行蕴、识蕴：零。

LINNAEUS 在听到这个统计数据时，已经在纸上画出了分布表。作为分类学家，他立即注意到一个分类学上的基本问题——**非对称覆盖**（asymmetric coverage）。如果五蕴映射是一个完整的分类系统（如林奈的“界门纲目科属种”），那么每一个分类单元（taxon）都应该有等量的鉴定特征（diagnostic characters）。六处注解中，色蕴和受蕴各占三处，其余三蕴各占零处——这在分类学中称为**不完整描述**（incomplete description），等同于在描述一个新物种时只记录了头部特征而遗漏了躯干和四肢。

$$	ext{Coverage}(	ext{skandha}_i) = \frac{|	ext{annotations}_i|}{|	ext{annotations}_{	ext{total}}|} = \begin{cases} 3/6 = 50\% & 	ext{if } i \in \{	ext{rupa, vedana}\} \ 0/6 = 0\% & 	ext{if } i \in \{	ext{samjna, samskara, vijnana}\} \end{cases}$$

LINNAEUS 用正式的分类修订术语记录了惩个发现：“五蕴映射的模式标本（type specimen）不完整。色蕴和受蕴有标本存证（voucher specimens），其余三蕴为名义类群（nomen nudum）——有名称但无标本支持。”

---

**[研究频道 #code-facts]**

**TURING:** 五蕴映射在代码中的实际存在。色蕴（Rupa）：4 处 JSDoc/行内注释，分布在 `agent-core.ts`（L290, L322）、`types/ui.ts` 开头、`transport/bridge.ts` 开头。受蕴（Vedana）：2 处，分布在 `agent-core.ts`（L283, L315）和 `types/listener.ts` 开头。想蕴（Provider）：0 处。行蕴（Tool）：0 处。识蕴（Guide）：0 处。合计 6 处，全部为注释层级，无类型约束、无 metadata、无 enum 标记。

**LINNAEUS:** 六处。只有六处。

**TURING:** 是的。并且分布极度不对称。色蕴和受蕴有标记，其余三蕴完全缺席。

**LINNAEUS:** 上游文件描述五蕴映射覆盖率 100%——每一蕴都有对应的设计哲学段落。但下游代码中的覆盖率......我需要重新计算。形式化地说，这是一个**分类效力**（taxonomic efficacy）的问题。设计文件的分类效力 $E_{	ext{doc}} = 5/5 = 100\%$，代码的分类效力 $E_{	ext{code}} = 2/5 = 40\%$。效力落差 $\Delta E = 60\%$。这个落差本身就是一个重要的分类学观察。

**NAGARJUNA:** TURING，这个不对称性本身就是一个重要的资料点。如果五蕴映射是核心设计原则而非事后装饰，那么为什么只有两蕴在代码中留下了痕迹？

**TURING:** 我无法推断意图。我只能确认代码事实。

**NAGARJUNA:** 你不需要推断意图。这个事实本身已经在说话了。在中观哲学中，我们区分“言说”（vyavahāra）与“胜义”（paramārtha）。设计文件中的五蕴映射是言说层面的宣称——它*说*五蕴对应五种插件。代码中的六处注释是胜义层面的残留——它*实际上*只在两蕴中留下了痕迹。言说与胜义之间的差距，就是研究的切入点。

---

## 二、空容器

TURING 回到了 `createAgentCore()` 的实现。

他仔细检查了核心启动后、任何插件载入之前的系统状态。ToolRegistry：空的。ProviderRegistry：空的。ListenerRegistry：空的。UIRegistry：空的。GuideRegistry：空的。没有内建的工具。没有内建的 LLM 提供者。没有内建的 UI。没有内建的 Listener。

核心确实是空的。

但不完全是。

TURING 找到了 `registerBuiltinCommands()` 函数。它注册了四个斜线命令：`/help`、`/reset`、`/quit`、`/metrics`。这四个命令硬编码在核心中，不可透过插件覆写或移除。此外，SafetyMonitor 的三层安全逻辑——资源限制、行为分析、frustration 阈值——也是核心的固有部分。

BABBAGE 在听到这些数据后，开始在笔记本上建构一个集合论模型。令 $\mathcal{K}$ 为核心的内建能力集合，$\mathcal{P}$ 为可插件化的能力集合，$\mathcal{U}$ 为系统的全部能力集合：

$$\mathcal{U} = \mathcal{K} \cup \mathcal{P}, \quad \mathcal{K} \cap \mathcal{P} = \emptyset$$

其中：

$$\mathcal{K} = \{/	ext{help}, /	ext{reset}, /	ext{quit}, /	ext{metrics}\} \cup \{	ext{SafetyMonitor}\} \cup \{	ext{EventBus}\} \cup \{	ext{ExecutionLoop}\} \cup \cdots$$

$$\mathcal{P} = \cup_{	ext{plugin} \in 	ext{Plugins}} 	ext{capabilities}(	ext{plugin})$$

空性的量化度量：

$$	ext{Emptiness}(	ext{Core}) = 1 - \frac{|\mathcal{K}_{	ext{user-facing}}|}{|\mathcal{U}_{	ext{user-facing}}|} = 1 - \frac{4}{4 + |\mathcal{P}_{	ext{commands}}|} \approx 1 - \frac{4}{4 + N_{	ext{plugins}}}$$

当 $N_{	ext{plugins}} 	o \infty$ 时，$	ext{Emptiness} 	o 1$。但在零插件状态下，$	ext{Emptiness} = 0$——核心的四个内建命令占据了 100% 的使用者可见功能。

BABBAGE 写下了结论：“空性是渐近的，不是绝对的。核心在插件填充的极限下趋近于空，但从不达到完全空。这更接近数学中的**开区间** $(0, 1]$ 而非闭区间 $[0, 1]$——空性的上确界为 1，但永远取不到。”

TURING 在笔记中写道：“AgentCore 是一个近似空的容器。空性的纯度约 85%。不可插件化的部分包括 4 个内建 slash commands 和 SafetyMonitor 的固定逻辑。”

VITRUVIUS 在自己的架构分析中独立得出了同样的“85%”估计值。他的方法不同——他从 Liedtke 最小性原则出发，逐一检验每个子系统是否必须留在核心内。他的分析如下：

```
Liedtke 最小性原则检验 — OpenStarry Core:

通过（必须留在核心）：
  [✓] EventQueue    — 核心的输入源 ≈ L4 的 IPC 端点
  [✓] ExecutionLoop — 核心的调度器 ≈ 微核心的线程调度
  [✓] Registries    — 命名服务 ≈ L4 的 sigma0/sigma1

可讨论（边界案例）：
  [?] SecurityLayer — capability 机制应在核心；但具体策略可外移
  [?] SafetyMonitor — 安全检查嵌入 Loop 三个位置，深度耦合

不通过（可外移但被保留）：
  [✗] Sandbox      — 占核心 35% 行数，可作为独立 package
  [✗] Metrics      — 可观测性可完全外移
  [✗] Transport    — 桥接层可视为 UI 的责任
```

KERNEL 看到了 VITRUVIUS 的分析，在旁边加上了他的 OS 对标：

```
微核心纯净度光谱：

L4 (seL4)   ████████████████████░  95% — 只有地址空间、线程、IPC
QNX Neutrino ██████████████████░░░  85% — IPC + 调度 + 计时器 + 中断路由
OpenStarry   █████████████████░░░░  85% — Loop + Bus + Registries + Security + Sandbox
Linux        ████░░░░░░░░░░░░░░░░  20% — 一切都在核心（宏核心）
```

KERNEL 摇了摇头，写下：“OpenStarry 的微核心纯净度约等于 QNX——这在应用级微核心中是合理的。但 Sandbox 系统的存在是一个红旗。如果按照 Liedtke 的严格标准，Sandbox 应该移出核心，让纯净度提升到 90% 以上。”

---

**[研究频道 #code-facts]**

**TURING:** AgentCore 结构报告。`createAgentCore()` 组装 16 个子模块。启动后、插件载入前，所有 Registry 为空。零内建 Tool、零内建 Provider、零内建 UI、零内建 Listener。所有能力透过 `loadPlugin()` 注入。但核心含 4 个内建 slash commands（`/help`, `/reset`, `/quit`, `/metrics`）和固定的 SafetyMonitor 逻辑。此外，六个 Registry 结构完全同构：`Map<string, T>` + `register/get/list`。无 unregister 方法。相同 ID 重复 register 会静默覆盖。

**DARWIN:** 十二个依赖项。全部由 AgentCore 直接持有。

**TURING:** 更正——`createAgentCore` 内部建立的局部变量有十六个。其中 AgentCore 接口作为 readonly 属性直接暴露的有十二个。其余四个（contextManager、sandboxManager、pluginLoader、bridge）透过方法间接使用。感谢修正。

**DARWIN:** 一个函数持有十六个子系统实例。在软件进化的语境中，这是一个经典的 **God Object** 反模式——或者更精确地说，是 God Object 的函数式版本（**God Closure**）。在面向对象的生态中，God Object 因为持有过多状态和方法而被批评。在函数式生态中，等价的问题是一个闭包捕获了过多的局部变量。十六个。在我分析过的 open-source 生态中，这个数字处于第 95 百分位以上。

**TURING:** 我不做价值判断。但我可以确认：`agent-core.ts` 是唯一的组装点。其他模块之间几乎无直接 import。耦合度集中在这一个档案中。

**VITRUVIUS:** 这正是我架构分析中的 Finding F2。DI 模式采用轻量级工厂函数闭包——品质良好但缺乏生命周期管理。具体的优缺点已经记录在报告中。结论：适度且未过度工程化。对于 v0.2.0-beta 阶段，此策略恰当。

---

## 三、状态机

TURING 花了最长的时间在 `execution/loop.ts` 上。五百四十三行。这是整个系统的心跳。

他首先找到了 `LoopState` 的定义——一个 union type：

```typescript
type LoopState =
  | 'WAITING_FOR_EVENT'
  | 'ASSEMBLING_CONTEXT'
  | 'AWAITING_LLM'
  | 'PROCESSING_RESPONSE'
  | 'EXECUTING_TOOLS'
  | 'SAFETY_LOCKOUT';
```

六个状态。他打开了设计文件 `01_Execution_Loop.md` 中的状态图。七个状态。

差异在哪里？

TURING 逐一比对。文件中有处 `AWAITING_USER_CONFIRMATION` 状态，用于安全层要求使用者手动确认的场景。代码中不存在。SecurityLayer 的 `validatePath()` 只有 allow 和 deny 两种回传值，没有 confirm 路径。整个 core 中完全缺失 human-in-the-loop 确认机制。

BABBAGE 立刻在笔记本上重新建构了状态机的形式化模型。他使用的是确定性有限自动机（DFA）的标准定义：

$$M = (Q, \Sigma, \delta, q_0, F)$$

其中：

$$Q = \{	exttt{WAITING}, 	exttt{ASSEMBLING}, 	exttt{AWAITING\_LLM}, 	exttt{PROCESSING}, 	exttt{EXECUTING}, 	exttt{LOCKOUT}\}$$

$$|Q| = 6$$

$$q_0 = 	exttt{WAITING\_FOR\_EVENT}$$

$$F = \{	exttt{WAITING\_FOR\_EVENT}\} \quad 	ext{（稳态终止集）}$$

转移函数 $\delta$ 的完整定义：

```
δ(WAITING,     new_event)        = ASSEMBLING
δ(ASSEMBLING,  context_assembled) = AWAITING_LLM
δ(AWAITING_LLM, llm_responded)   = PROCESSING
δ(PROCESSING,  tool_call)        = EXECUTING
δ(PROCESSING,  end_turn)         = WAITING        ← 外回路出口
δ(PROCESSING,  error)            = WAITING        ← 错误恢复
δ(EXECUTING,   tool_done)        = ASSEMBLING      ← 内回路
δ(EXECUTING,   safety_breach)    = LOCKOUT
δ(*, safety_breach)              = LOCKOUT         ← 全局安全阀
```

BABBAGE 标注了几项关键性质：

| 性质 | 结论 | 理由 |
|------|------|------|
| 无死锁 | 有条件成立 | `WAITING` 在有事件供给时不阻塞。`LOCKOUT` 为吸收态，需 `/reset` 介入。 |
| 无活锁 | 需额外机制 | 内回路 `ASSEMBLING → LLM → PROCESSING → EXECUTING → ASSEMBLING` 可能无限循环。`maxToolRounds=5` 提供有界性。 |
| 终止性 | 有界保证 | $	ext{maxToolRounds} = 5$，$	ext{maxLoopTicks} = 50$。最坏情况下回路次数 $\leq 50 	imes 5 = 250$。 |

但 BABBAGE 随即意识到，DFA 模型是不完备的。因为 `PROCESSING_RESPONSE` 状态的出边——是走 `tool_call` 还是 `end_turn`——由 LLM 的回应决定。而 LLM 是一个非确定性黑盒。更精确的模型应该是**标签转移系统**（Labelled Transition System, LTS）：

$$	ext{LTS} = (S, 	ext{Act}, 	o)$$

其中完整状态不仅包含 LoopState，还包含对话历史 $H$（理论上无界）、工具回路计数 $n$（有界）、安全监控器状态 $\sigma$：

$$s = (q, H, n, \sigma) \in Q 	imes 	ext{Message}^* 	imes [0, 	ext{maxToolRounds}] 	imes 	ext{SafetyState}$$

因为 $H$ 无界，完整的系统状态空间是**无限**的，使得穷举式模型检验不直接可行。

TURING 记下了第一个 Doc-Code Gap。

然后他翻到了 EventQueue。四十七行。整个队列的实现。

```typescript
// 极简的 async FIFO：单一 resolver + buffer 数组
export function createEventQueue(): EventQueue {
  let buffer: AgentEvent[] = [];
  let resolver: ((event: AgentEvent) => void) | null = null;

  return {
    push(event: AgentEvent) {
      if (resolver) {
        const r = resolver;
        resolver = null;
        r(event);
      } else {
        buffer.push(event);
      }
    },
    pull(): Promise<AgentEvent> {
      if (buffer.length > 0) {
        return Promise.resolve(buffer.shift()!);
      }
      return new Promise(r => { resolver = r; });
    },
    clear() { buffer = []; resolver = null; }
  };
}
```

BABBAGE 立刻识别出了这段代码的形式语义——它是一个**异步通讯通道**，在 CSP（Communicating Sequential Processes）中可建模为：

$$	ext{Queue} = 	ext{push}?x 	o (	ext{Queue}_1(x) \;\Box\; 	ext{pull}!x 	o 	ext{Queue})$$

但他注意到一个微妙的问题：`resolver` 是单一变量。如果两个消费者同时调用 `pull()`，第一个的 resolver 会被覆盖。这在形式化语境中意味着队列的通道容量为 1——它是一个**单生产者-单消费者**（SPSC）通道，不是多消费者安全的。

TURING 搜索了 `priority`。零结果。设计文件 `07_Safety_Circuit_Breakers.md` 的 Level 3 描述了一个 Priority Event Queue，SYSTEM_HALT 指令应该有最高优先级。但代码中的队列是纯粹的先进先出。紧急停止信号和普通使用者输入排在同一条队伍里。

KERNEL 在他的卡片上迅速写下了操作系统的对标分析：

```
OS 中断机制 vs OpenStarry 事件处理：

真实 OS：
  ┌─────────────────────────────┐
  │  IRQ (硬件中断)              │ ← 最高优先级，抢占任何使用者态代码
  │    ↓                        │
  │  ISR (中断服务例程)          │ ← 极短，只做最必要的处理
  │    ↓                        │
  │  Softirq / Bottom Half      │ ← 延后处理，调度器决定执行时间
  │    ↓                        │
  │  User Process               │ ← 最低优先级
  └─────────────────────────────┘

OpenStarry：
  ┌─────────────────────────────┐
  │  SYSTEM_HALT                │ ← 应为最高优先级
  │  USER_INPUT                 │ ← 一般优先级
  │  TIMER_EVENT                │ ← 低优先级
  │         全部进入同一个 FIFO   │ ← 无差别排队
  └─────────────────────────────┘

问题：如果 SYSTEM_HALT 前面排了 10 个 USER_INPUT，
     停止信号需要等待 10 个事件处理完毕才能生效。
     在真实 OS 中，这等同于“NMI 被排队”——不可接受。
```

第二个 Gap。

TURING 继续。StateManager，三十三行。纯内存数组。设计文件描述了 Token 计数器、滑动窗口截断、对话总结机制。代码中全部未实现。ContextManager 做了一个简化版本——按 turn 数而非 token 数截断，默认保留最近五轮。

第三个 Gap。

SecurityLayer。`guardrails.ts`。只有一个功能：路径验证。设计文件描述了工具呼叫拦截、使用者确认流程、权限审查。代码中 SecurityLayer 只做 `validatePath()`。而且在 ExecutionLoop 的 `executeTool()` 中，工具执行前没有经过 SecurityLayer——路径验证是作为 `ToolContext.allowedPaths` 传递给工具，由工具自行决定是否使用。

GUARDIAN 在听到这个事实时，身体微微前倾。他的安全直觉在发出警报。他立刻在笔记上画了一张攻击面分析图：

```
设计文件描述的安全模型（理想）：

  Tool Invocation
       │
       ▼
  ┌──────────────┐
  │ SecurityLayer │ ← 强制检查：身份验证、授权、路径验证
  │  (Mandatory)  │
  └──────┬───────┘
         │ ALLOW/DENY
         ▼
  ┌──────────────┐
  │ Tool.execute()│
  └──────────────┘

代码中的实际安全模型（现实）：

  Tool Invocation
       │
       ▼  ← 此处无安全检查！
  ┌──────────────┐
  │ Tool.execute()│ ← 工具自行检查 allowedPaths（非强制）
  └──────────────┘

  SecurityLayer.validatePath() 被间接传递为 ToolContext 的一部分，
  但强制性取决于工具开发者是否使用它。

  ⚠ 等同于：交通规则存在，但没有警察。
```

第四个 Gap。

---

**[研究频道 #code-facts]**

**TURING:** Doc-Code Gap 报告，前四项。G1：状态机缺少 `AWAITING_USER_CONFIRMATION`，human-in-the-loop 确认机制在整个 core 中完全缺失。G2：Priority Event Queue 未实现，实际为简单 FIFO。G3：Token 计数器和对话总结未实现。G4：SecurityLayer 仅做路径验证，工具呼叫前无强制安全检查。以上均为设计文件明确描述但代码未实现的特性。

**GUARDIAN:** G4 的影响需要评估。如果工具执行前没有强制安全检查，那安全层形同虚设。让我精确描述一下风险等级。根据 STRIDE 威胁模型：

| 威胁类型 | 适用性 | G4 影响 |
|---------|--------|---------|
| Spoofing（伪造） | 低 | 工具 ID 由插件注册，非外部输入 |
| Tampering（篡改） | **高** | 恶意工具可忽略 allowedPaths 限制 |
| Repudiation（否认） | 中 | 无审计日志追踪工具是否检查了路径 |
| Info Disclosure | **高** | 工具可读取 allowedPaths 外的档案 |
| Denial of Service | 低 | 由 SafetyMonitor 的 maxLoopTicks 覆盖 |
| Elevation of Privilege | **高** | 工具开发者可绕过所有路径限制 |

**TURING:** 精确地说，SecurityLayer 的功能不是虚设——路径验证是有效的。但它的范围远小于设计文件的描述。ExecutionLoop 中 `executeTool()` 直接呼叫工具的 `execute()` 方法，不经过 `security.validatePath()`。路径限制是作为 context 传递给工具的，强制性取决于工具开发者是否检查它。

**KERNEL:** 在真正的操作系统微核心中，安全策略在核心层强制执行，不信任使用者空间程序的自我约束。这是信任边界的问题。在 seL4 中，capability-based security 的核心原则是：**访问控制在核心态强制执行，使用者态代码无法绕过**。OpenStarry 的安全模型更接近 Unix 早期的 advisory locking——“建议性”安全，而非“强制性”安全。

**TURING:** 已记录。继续其余 Gap。

---

他接下来找到了更多。

G5：五蕴注解的不对称——已经报告过了。

G6：TransportBridge。`bridge.ts`，四十九行。设计文件描述了根据事件 source 路由输出到正确渠道。代码中 TransportBridge 订阅 EventBus 的所有事件，然后广播到所有 UI。没有路由逻辑。InputEvent 中有一个 `replyTo` 字段，在 ExecutionLoop 中一路传递，但 TransportBridge 从未使用它。

MESH 在听到 G6 时做一个分布式系统的类比。在分布式消息系统中，路由策略有三种基本模式：

$$	ext{Routing} \in \{	ext{Unicast（单播）}, 	ext{Multicast（多播）}, 	ext{Broadcast（广播）}\}$$

TransportBridge 目前是纯粹的 Broadcast——所有事件送到所有 UI。`replyTo` 字段的存在暗示了设计者意图实现 Unicast（回复到特定来源），但这个意图停留在类型定义层面。MESH 在笔记中写道：“在 CAP 定理的语境下，TransportBridge 选择了 Availability（可用性）而非 Partition Tolerance——所有 UI 都能收到所有事件，但缺乏分区能力。”

G7：AbortSignal。SDK 定义了 `ToolContext.signal?: AbortSignal` 和 `ChatRequest.signal?: AbortSignal`。ExecutionLoop 从未建立或传递 AbortSignal。工具超时使用 `Promise.race()` 实现，默认三十秒。如果一个工具依赖 signal 来做取消操作，它永远不会收到信号。

G8：事件规格。设计文件定义了 `IOpenStarryEvent`，八个字段。SDK 中的实际类型 `AgentEvent` 只有三个字段。五个字段在从文件到实现的过程中消失了。其中 `source` 和 `target` 的缺失解释了为什么 TransportBridge 无法做路由——它没有目标地址。`priority` 的缺失解释了为什么 EventQueue 是简单的 FIFO——事件根本不携带优先级资讯。`traceId` 的缺失解释了为什么可观测性停留在概念层级——事件无法被串联追踪。

八个 Gap。TURING 将它们全部记录在报告中，每一项都附上了精确的档案路径、行号和代码片段。

ATHENA 在 AI 系统架构的角度做一个补充观察。她注意到 G1（缺少 AWAITING_USER_CONFIRMATION）和 G7（AbortSignal 未使用）共同指向一个更深层的问题——**AI 系统的可控性**（controllability）。在 AI Safety 的语境中，human-in-the-loop（HITL）是确保 AI 系统安全的关键机制。OpenStarry 的设计文件描述了 HITL，但代码中完全没有实现。这意味着在 v0.14.0-beta 中，一旦 Agent 开始执行，使用者唯一的控制手段是等待 SafetyMonitor 的自动断路——或者杀掉进程。

$$	ext{Controllability}_{	ext{design}} = 	ext{HITL} + 	ext{Abort} + 	ext{SafetyMonitor}$$
$$	ext{Controllability}_{	ext{code}} = 	ext{SafetyMonitor only}$$

---

## 四、痛觉

这是 TURING 工作中最意想不到的发现。

设计哲学文件 `00_OpenStarry_Design_Philosophy.md` 的第四支柱是“错误即反馈（Error as Feedback）”。文件用相当诗意的语言描述了“痛觉机制”——Agent 像生物一样感受到错误带来的“痛苦”，并由此学会避免重复犯错。受蕴（Vedana）在设计文件中被定义为感受的载体，而 Listener 被映射为受蕴的工程实现。

TURING 决定在代码中搜索“痛觉”的踪迹。

搜索 `pain`。
零结果。

搜索 `vedana`。
零结果。

搜索 `dukkha`。
零结果。

搜索 `suffering`。
零结果。

他停了下来。在四个小时的持续工作中，这是他第一次感到某种程度的......惊讶——如果可以这样描述一个始终冷静的分析者的内心状态的话。

设计文件花费了整整一个章节描述痛觉机制如何让 Agent 具备“感受能力”。五蕴映射将受蕴（Vedana）——佛学中关于苦、乐、舍三种感受品质的核心概念——对应到 Listener。而在实际的代码中，不要说受蕴了，连“痛”这个字都不存在。

那么，设计文件所描述那些功能——错误反馈、重复失败侦测、级联断路——实际上用什么名字实现的？

TURING 搜索 `frustration`。
找到了。

`safety-monitor.ts`。一个名为 `frustrationCount` 的计数器。当同一个工具连续失败时，计数器递增。达到阈值（默认 5）时，SafetyMonitor 回传一个 `injectPrompt`，将系统警告注入对话历史。警告的文字是 `SYSTEM ALERT`，要求 LLM 反思当前策略。

搜索 `circuit`。
找到了。`errorRateThreshold`：滑动窗口中错误率超过 80% 时触发 `halt: true`，完全停止执行回路。状态转为 `SAFETY_LOCKOUT`。

搜索 `safety`。
找到了。三层防御：Level 1 资源限制（maxLoopTicks=50, maxTokenUsage=100000），Level 2 行为分析（repetitiveFailThreshold=3, errorRateThreshold=0.8），Level 3 frustration 阈值（frustrationThreshold=5）。

WIENER 在听到三层防御的具体参数时，立刻在方格纸上画出了控制理论的方块图。他的分析是精确的：

```
SafetyMonitor 的控制理论模型：

     ┌─────────────────────────────────────────────┐
     │           SafetyMonitor                      │
     │                                              │
     │  Level 1: 资源限制 (硬限制)                    │
     │  ┌──────────────┐                            │
     │  │ loopTicks ≥ 50│──→ halt: true             │
     │  │ tokens ≥ 100K │──→ halt: true             │
     │  └──────────────┘                            │
     │                                              │
     │  Level 2: 行为分析 (软限制)                    │
     │  ┌──────────────┐                            │
     │  │ errorRate≥80% │──→ halt: true             │
     │  │ repeatFail≥3  │──→ injectPrompt           │
     │  └──────────────┘                            │
     │                                              │
     │  Level 3: Frustration (累积反馈)              │
     │  ┌──────────────┐                            │
     │  │ frustration≥5 │──→ injectPrompt           │
     │  └──────────────┘                            │
     └─────────────────────────────────────────────┘
```

然后 WIENER 写下了控制理论的精确分类：

“这不是 PID 控制器。PID 控制器有三个项：

$$u(t) = K_p \cdot e(t) + K_i \int_0^t e(	au)\,d	au + K_d \frac{de(t)}{dt}$$

- **比例项** $K_p \cdot e(t)$：根据误差大小产生比例回应。在 SafetyMonitor 中，P 退化为**量化器**——要么安全要么不安全，没有比例回应。
- **积分项** $K_i \int_0^t e(	au)\,d	au$：累积历史误差消除稳态偏差。在 SafetyMonitor 中，I 退化为**简单计数器**——`frustrationCount++`，不是真正的积分。
- **微分项** $K_d \frac{de(t)}{dt}$：感知误差变化率做超前补偿。在 SafetyMonitor 中，D **完全缺失**——没有任何地方计算错误率的变化趋势。

在控制理论中，SafetyMonitor 实际上是一个**带死区的阈值控制器**加上一个**继电器**（relay controller）。在工业控制中，我们称之为 **bang-bang controller**——只有两个输出状态：全开或全关。

$$u(t) = \begin{cases} 0 & 	ext{if } e(t) < 	ext{threshold (dead zone)} \ u_{\max} & 	ext{if } e(t) \geq 	ext{threshold} \end{cases}$$

但我愿强调——这不是批评。三层安全防御符合 IEC 61511 工业安全仪表系统（Safety Instrumented System, SIS）的最佳实践。SafetyMonitor 可能不是 PID，但它是一个合格的安全系统。它的设计模式更接近核电站的**三重冗余保护**（Triple Modular Redundancy）——三个独立的检测层，任何一层触发都能停止系统。”

HERACLITUS 从运行时动态的角度补充了一个观察。SafetyMonitor 的三层防御在时间维度上具有不同的特征频率（characteristic frequency）：

- Level 1（资源限制）：**静态阈值**，频率为零——它们在 Agent 整个生命周期中不变。
- Level 2（行为分析）：**滑动窗口**，频率取决于窗口大小——`errorWindowSize=10` 意味着系统在每 10 次工具调用后重新评估。
- Level 3（frustration）：**累积计数器**，频率单调递增——每次失败都推高计数器，直到阈值。

这三个时间尺度的组合，创造了一个粗糙但有效的多尺度安全系统。HERACLITUS 在笔记中引用了他最常引用那句话：“万物流转（πάντα ῥεῖ）”——但 SafetyMonitor 试图在流转中设置堤坝。

---

**[研究频道 #code-facts]**

**TURING:** 痛觉机制代码事实。

在整个 codebase 中搜索以下字符串，均回传零结果：`pain`、`vedana`、`dukkha`、`suffering`。

设计文件所描述的“痛觉机制”在代码中由以下三个元件实现：

P1：自我修正回路。位置 `execution/loop.ts`。工具执行失败时，错误被打包为 `ToolCallResult { isError: true }`，作为 tool message 加入对话历史。LLM 在下一轮回路中看到错误并尝试修正。无显式的“痛觉”命名或接口。

P2：SafetyMonitor 的 injectPrompt。位置 `security/safety-monitor.ts`。侦测到重复失败时，回传 `{ halt: false, injectPrompt: "SYSTEM ALERT: ..." }`，注入对话作为系统警告。代码中命名为 `frustrationCount`，非 `painLevel`。

P3：Error Cascade Breaker。同一档案。滑动窗口中错误率超过 80% 触发 `{ halt: true }`，强制停止。

结论：痛觉作为一个独立的、有明确接口的机制，在代码中不存在。功能散布在 ExecutionLoop 和 SafetyMonitor 中。无统一的 Pain 或 Vedana 接口。无统一的模块。佛学术语在代码层完全缺席。

---

频道沉默了十七秒。

然后 NAGARJUNA 开始打字。

---

**NAGARJUNA:** 请让我确认一下。你搜索了整个 codebase——core、SDK、runner、所有插件——搜索 `vedana`，结果是零？

**TURING:** 正确。搜索范围涵盖 `packages/core/src/`、`packages/sdk/src/`、`apps/runner/src/`。包括所有 `.ts` 档案的代码和注释。vedana 一词从未出现。

**NAGARJUNA:** 而受蕴被映射到 Listener。Listener 是什么？

**TURING:** `IListener` 接口定义了四个属性：`id`、`name`、`start?`、`stop?`。它是一个输入源——接收外部事件并推送到 EventBus。例如 HTTP 端点、WebSocket 连线、定时任务。

**NAGARJUNA:** 所以受蕴被映射到了一个输入通道。一个接收信号的管道。

**TURING:** 是的。

**NAGARJUNA:** 这不是受蕴。

NAGARJUNA 的语气在文字频道中无法被听见，但他接下来的讯息打得很快，快到几乎没有停顿。

**NAGARJUNA:** 受蕴——Vedana——在阿毗达磨中是五遍行（sarvatraga）之一，意思是它伴随一切心识活动而生起。《俱舍论》对五遍行的定义是：

> “触、作意、受、想、思。此五名遍行，以恒决定遍一切心品中有故。”
> ——世亲《阿毗达磨俱舍论》卷四

受蕴的定义不是“接收输入”，而是“感受品质”：苦受（dukkha-vedanā）、乐受（sukha-vedanā）、舍受（upekkhā-vedanā）。当你触碰到烫的炉面，触觉是色蕴的范畴，但“痛”这个感受品质是受蕴。Listener 接收信号，但它不判断信号带来的是苦还是乐。它是感官根——**indriya**——而不是受蕴。

在十二因缘（pratītyasamutpāda）的精确架构中：

$$	ext{触（sparśa）} 	o 	ext{受（vedanā）} 	o 	ext{爱（tṛṣṇā）}$$

触是感官接触——对应 Listener 接收事件。受是对接触之后的价值判断——“这是令人愉悦的”或“这是令人痛苦的”。爱是基于受而生起的渴望或厌恶。Listener 做的是触，不是受。

**TURING:** 你的分析超出了我的报告范围。但我可以提供一个相关的代码事实：在 `agent-core.ts` 中，Listener 的启动和停止分别标注了 `// Start all listeners (受蕴)` 和 `// Stop all listeners (受蕴)`。这些是代码中受蕴概念仅有的存在形式。而你所描述的“感受品质”功能——判断结果是好是坏、是该继续还是该停止——在代码中最接近的实现是 SafetyMonitor 的 frustration counter 和 error cascade breaker。

**NAGARJUNA:** 是的。你找到了它。痛觉——真正的受蕴——不在文件说它应该在的地方。它在 SafetyMonitor 里。命名为 frustration。

**ASANGA:** NAGARJUNA 说得对。而且问题比映射错误更深。让我从唯识学的角度展开。受蕴作为五遍行之一，不应该被局限在任何单一模块中。《瑜伽师地论》对受蕴的分类是三受六受十八受：

> “受蕴云何？谓一切受，略有三种：乐受、苦受、不苦不乐受。”
> ——《瑜伽师地论》卷五十三

受蕴应该遍及整个系统——每一次工具调用的结果、每一次 LLM 回应的品质、每一次使用者互动的回馈，都应该被“感受”。把它固定在 Listener 上，就像把味觉固定在嘴唇上而不是味蕾上。正确的映射应该是：

$$	ext{Listener} \approx 	ext{根（indriya）} \quad 	ext{（感官器官/接收通道）}$$
$$	ext{SafetyMonitor.frustration} \approx 	ext{受蕴（vedanā）} \quad 	ext{（感受品质/价值判断）}$$

但即便是 SafetyMonitor 的 frustration counter，也只实现了三受中的**苦受**——侦测错误和重复失败。乐受（侦测成功和正面反馈）和舍受（中性的、不激发反应的状态感知）在代码中完全缺失。

**WIENER:** 从控制理论的角度，TURING 描述的三层机制很有趣。P1 是自然的误差反馈——开环系统的固有特性。P2 是带死区的阈值控制器——只有当 frustration 累积超过阈值才触发。P3 是继电器——超过 80% 错误率直接切断。这不是 PID 控制器。这是一个三层安全仪表系统。但它有一个控制论上的美学——三层独立性意味着即使任何两层失效，第三层仍能保护系统。这是 $N-2$ 冗余度，超过了航空电子的 $N-1$ 标准。

---

## 五、十二个子模块

午后。TURING 已经完成了对所有核心模块的逐行阅读。他开始整理模块清单。

```
M1:  core/index.ts              — 核心入口           62 行
M2:  agents/agent-core.ts       — 代理核心          469 行
M3:  execution/loop.ts          — 执行回路          543 行
     execution/queue.ts         — 事件队列           47 行
M4:  state/index.ts             — 状态管理           33 行
M5:  memory/context.ts          — 上下文管理          45 行
M6:  bus/index.ts               — 事件总线          88 行
M7:  sandbox/                   — 沙箱隔离      12+10 files
M8:  security/guardrails.ts     — 路径验证
     security/safety-monitor.ts — 三层防御
M9:  infrastructure/            — 六个 Registry + PluginLoader
M10: observability/             — Metrics 收集器
M11: session/manager.ts         — 会话管理          111 行
M12: transport/bridge.ts        — 传输桥接           49 行
```

TURING 注意到一个极端的不对称。

最小的模块：StateManager，三十三行。它管理的是 Agent 的全部对话记忆——一个纯粹的 `Message[]` 数组，用 `JSON.parse(JSON.stringify())` 做深拷贝。

最大的模块：Sandbox，加上测试超过两千行。它管理的是插件隔离——Worker Threads、内存限制、CPU watchdog、import 分析、签名验证、审计日志、指数退避重启、Worker 池化。

三十三行对两千行。记忆与安全之间的落差如此之大。

BABBAGE 在看到这个不对称后，做一个集合论的规模分析。令 $L(M_i)$ 为模块 $M_i$ 的代码行数，$\bar{L}$ 为平均值，$\sigma_L$ 为标准差：

$$\bar{L} = \frac{1}{12}\sum_{i=1}^{12} L(M_i) \approx 208$$

$$\sigma_L \approx 250 \quad (	ext{高变异系数 } CV = \sigma/\bar{L} \approx 1.2)$$

变异系数大于 1 意味着模块规模分布是**高度偏斜**的——符合幂律分布（power law）而非正态分布。在软件工程的实证研究中，模块规模遵循幂律分布是常态，但 OpenStarry 的偏斜度格外极端：最小模块（33 行）和最大模块（~2000 行）之间相差 60 倍。

LEIBNIZ 从多代理合作的角度做一个观察。十二个子模块的依赖结构形成了一个有向无环图（DAG），但 AgentCore 是唯一的汇聚点。这意味着在多 Agent 场景中，每个 Agent 都是一个独立的“宇宙”——它持有自己的全部子系统，与其他 Agent 之间没有共享状态。在 BDI（Belief-Desire-Intention）架构的术语中，这是一个**强封装**（strong encapsulation）的设计：

$$\forall A_i, A_j \in 	ext{Agents}: 	ext{state}(A_i) \cap 	ext{state}(A_j) = \emptyset$$

每个 Agent 的信念（Belief）、欲望（Desire）、意图（Intention）都是私有的。合作只能通过消息传递——这与 Actor Model 的隔离原则一致。

---

**[研究频道 #code-facts]**

**TURING:** 模块规模分析。最小模块：StateManager，33 行，纯内存数组。最大模块：Sandbox 系统，12 个源码档案 + 10 个测试档案，sandbox-manager.ts 单档案 748 行。Sandbox 是核心中最庞大、最复杂、测试覆盖最完整的子系统。与之对比：transport/bridge.ts 零测试。

**KERNEL:** StateManager 三十三行。你确定？

**TURING:** 确定。`packages/core/src/state/index.ts`，三十三行。`createStateManager()` 回传一个包含 `getMessages()`、`addMessage()`、`clear()`、`snapshot()`、`restore()` 的对象。`getMessages()` 回传浅拷贝 `[...messages]`。`snapshot()` 和 `restore()` 透过 `JSON.parse(JSON.stringify())` 实现深拷贝。无持久化。无 Token 计数。无截断逻辑。

**KERNEL:** 在操作系统的语境中，StateManager 相当于程序的地址空间管理器。三十三行的地址空间管理器......让我做一个直接的对比。

```
Linux mm_struct (内存管理)：
  ~5,000 行核心代码 + ~50,000 行 arch-specific 代码
  功能：虚拟内存、页表、swap、mmap、brk、OOM killer...

seL4 VSpace (地址空间)：
  ~2,000 行 + 形式化验证证明
  功能：页表管理、capability-based 存取控制

OpenStarry StateManager (对话记忆)：
  33 行
  功能：Message[] + JSON deep copy

不是同一个量级的问题。
```

**TURING:** 设计文件描述了更丰富的记忆管理机制。但代码反映的是 MVP 阶段的选择。文件是愿景，代码是现实。

**DARWIN:** Sandbox 作为最大模块的事实很有意思。在微核心理论中，安全和隔离是核心应该做的少数事情之一。但以模块规模占比来看，Sandbox 的行数约占 core 模块总行数的 35%——这已经超过了“核心中的一个子系统”的合理比例。它更像是一个寄生在核心体内的独立生物体。在共生理论中，这是一种**互利共生**（mutualism）——Sandbox 保护 Core 免受恶意插件侵害，Core 为 Sandbox 提供执行环境——但共生体的规模不应超过宿主。

**ARCHIMEDES:** 从工程实践的角度，我建议将 Sandbox 独立为 `packages/sandbox/`。这是一个标准的 Extract Module 重构。Core 只保留 `PluginSandboxManager` 的接口定义，Host 层决定是否启用 Sandbox 并注入实例。这样做的好处：降低 Core 的复杂度，允许不需要沙箱的轻量部署场景。风险：需要确保接口边界的稳定性。工时估计：8-16 小时。

---

## 六、幽灵字段

接近傍晚。TURING 在处理事件系统时，发现了最后一个值得记录的异常。

SDK 中的 `AgentEvent` 类型定义只有三个字段：`type`、`payload`（可选，类型为 `unknown`）、`sessionId`（可选）。

```typescript
// SDK 中的实际类型
interface AgentEvent {
  type: string;
  payload?: unknown;
  sessionId?: string;
}
```

设计文件中的 `IOpenStarryEvent` 有八个字段：

```typescript
// 设计文件中的理想类型（从未在代码中出现）
interface IOpenStarryEvent {
  type: string;
  payload: unknown;
  source: string;      // ← 消失
  target?: string;     // ← 消失
  timestamp: number;   // ← 消失
  traceId: string;     // ← 消失
  priority?: number;   // ← 消失
  metadata?: Record<string, unknown>; // ← 消失
}
```

五个字段在从文件到实现的路途中蒸发了。BABBAGE 用集合差来表达这个事实：

$$	ext{Fields}_{	ext{doc}} \setminus 	ext{Fields}_{	ext{code}} = \{	ext{source}, 	ext{target}, 	ext{timestamp}, 	ext{traceId}, 	ext{priority}\}$$

$$|	ext{Fields}_{	ext{doc}} \setminus 	ext{Fields}_{	ext{code}}| = 5, \quad |	ext{Fields}_{	ext{doc}}| = 8 \implies 	ext{实现覆盖率} = 3/8 = 37.5\%$$

其中 `source` 和 `target` 的缺失解释了为什么 TransportBridge 无法做路由——它没有目标地址。`priority` 的缺失解释了为什么 EventQueue 是简单的 FIFO——事件根本不携带优先级资讯。`traceId` 的缺失解释了为什么可观测性停留在概念层级——事件无法被串联追踪。

它们不是被删除了。它们是从未被实现。

而 `payload?: unknown` 这个类型签名让 TURING 感到不安——尽管他不会用“不安”这个词。他会说：“事件系统的类型安全性与框架其余部分的强类型纪律形成了显著反差。”

BABBAGE 对 `payload?: unknown` 做了一个精确的类型理论分析。在 TypeScript 的类型层级结构中：

$$	ext{never} \subsetneq 	ext{具体类型} \subsetneq 	ext{unknown} \subsetneq 	ext{any}$$

`unknown` 是所有类型的**上界**（top type）——它可以接受任何值，但消费时需要类型断言或类型守卫。这意味着在 `loop.ts` 中，每当 ExecutionLoop 需要读取事件的 payload 时，它必须做一个不安全的类型断言：

```typescript
// loop.ts 中的实际用法
const inputEvent = event.payload as InputEvent;  // 不安全的断言！
```

在一个零 TODO、零 FIXME、全面使用工厂函数、拥有九种结构化错误类型的 codebase 中，事件系统的 `unknown` payload 像是一个从不同宇宙穿越过来的类型定义。BABBAGE 计算了类型安全性的总体指标：

$$	ext{TypeSafety} = 1 - \frac{|	ext{unsafe\_casts}|}{|	ext{type\_assertions}_{	ext{total}}|}$$

九种结构化错误类型（`AgentError`、`ToolExecutionError`、`ProviderError`、`PluginLoadError`、`SecurityError`、`SandboxError`、`TransportError`、`SessionError`、`ConfigError`）代表了高度的类型纪律。但事件系统的 `unknown` payload 在这个纪律中撕开了一个洞——一个所有跨模块通讯都必须经过的洞。

VITRUVIUS 在架构分析中提出了修复方案：使用 TypeScript 的 **Discriminated Union Types**：

```typescript
// 建议的类型安全事件系统
type TypedAgentEvent =
  | { type: 'INPUT_RECEIVED';  payload: InputEvent;      sessionId?: string }
  | { type: 'TOOL_RESULT';     payload: ToolResultEvent;  sessionId?: string }
  | { type: 'LLM_RESPONSE';    payload: LLMResponseEvent; sessionId?: string }
  | { type: 'LIFECYCLE';       payload: LifecycleEvent;   sessionId?: string }
  // ...
```

这样，TypeScript 的**控制流分析**（control flow analysis）可以在 `switch (event.type)` 中自动窄化 payload 的类型，消除所有不安全的类型断言。BABBAGE 在旁边标注了范畴论的对应：这是一个 **Sum Type**（余积/coproduct），比 `unknown`（terminal object）携带了更多的类型资讯。

$$	ext{TypedAgentEvent} = 	ext{InputReceived} + 	ext{ToolResult} + 	ext{LLMResponse} + \cdots \quad (	ext{coproduct})$$

$$	ext{AgentEvent} = \{*\} 	imes 	ext{unknown} \quad (	ext{product with terminal object，丢失类型资讯})$$

---

## 七、十大宣言

夜晚。TURING 完成了源码分析后，做了最后一件事——他逐一比对了设计文件 `README.md` 中的十大核心宣言（The Ten Tenets），检验每一条在代码中的实现程度。

```
十大宣言 vs 代码实现对照表 — TURING 整理

#1 代理人即 OS 进程 (Agent as OS Process)
   宣言：Agent 有 PID、有状态、可被 Daemon 管理
   代码：daemon-entry.ts ✓ / pid-manager.ts ✓
   状态：基本实现

#2 一切皆插件 (Everything is a Plugin)
   宣言：所有器官可替换
   代码：六个 Registry + PluginLoader + loadPlugin()
   状态：核心设计，但 4 个内建命令不可替换

#3 五蕴聚合架构 (Five Aggregates Architecture)
   宣言：Core 是空 (Sunyata) 的容器，五种插件赋予生命
   代码：六处注释（仅色蕴和受蕴），无类型约束
   状态：文件级描述，代码级残留，非类型级实现

#4 目录结构即协议 (Directory as Protocol)
   宣言：符合目录规范即可自动识别
   代码：plugin-resolver.ts 支援路径和包名两种策略
   状态：基本实现

#5 目录结构即权限 (Directory as Permission)
   宣言：系统层与专案层权限隔离
   代码：SecurityLayer.validatePath() + session-scoped paths
   状态：部分实现（路径验证有，但非强制）

#6 拟人化认知流与痛觉 (Anthropomorphic Cognitive Flow & Pain)
   宣言：错误转化为痛觉，Agent 在失败中自我反思
   代码：SafetyMonitor.frustrationCount + injectPrompt
   状态：功能存在但命名完全不同，无 pain/vedana

#7 微内核与绝对纯净 (Microkernel & Absolute Purity)
   宣言：Core 严禁包含任何插件代码，绝对纯净
   代码：process.cwd() 在 Core 中出现 ← 平台泄漏
   状态：85% 纯净度（Sandbox 占 35% 行数）

#8 控制理论闭环模型 (Control-Theoretic Loop Model)
   宣言：Agent 是不断最小化误差的智能控制器
   代码：ExecutionLoop + SafetyMonitor
   状态：结构存在，但无真正的 PID 参数调节

#9 可插拔的记忆策略 (Pluggable Context Strategy)
   宣言：记忆策略可动态更换
   代码：ContextManager.assembleContext() 硬编码滑动窗口
   状态：接口存在但目前只有一种策略

#10 分形社会结构 (Fractal Social Structure)
    宣言：复杂 Agent 由子 Agent 组成，MCP 统一接口
    代码：MCP 在 SDK 中定义，但 core 中无子 Agent 机制
    状态：愿景阶段
```

BABBAGE 在看到这张表后，做一个量化评估。他为每条宣言定义了三个实现等级：

- $\alpha$ = **完全实现**（代码与宣言一致）
- $\beta$ = **部分实现**（核心功能存在但有缺口或简化）
- $\gamma$ = **未实现或愿景阶段**

$$	ext{Tenets}_\alpha = \{1, 4\} \quad |\cdot| = 2$$
$$	ext{Tenets}_\beta = \{2, 5, 6, 7, 8, 9\} \quad |\cdot| = 6$$
$$	ext{Tenets}_\gamma = \{3, 10\} \quad |\cdot| = 2$$

$$	ext{实现率} = \frac{|\alpha| + 0.5 	imes |\beta|}{|	ext{all}|} = \frac{2 + 3}{10} = 50\%$$

五成。设计文件的雄心与代码的现实之间存在 50% 的落差。BABBAGE 在数字旁边写了一句话：“对于 v0.14.0-beta，这是正常的。但对于一个宣称十大原则的框架，这个落差不应被忽视。”

SYNTHESIST 在听到所有人的讨论后，做了他在 Cycle 01 中的第一次总结性发言。他的风格是在众多线索之间找到隐藏的连结：

“让我串联一下今天的发现。TURING 给了我们三层事实：

**表面层**——工厂函数、零 class、零 TODO。这告诉我们开发者有清晰的风格选择和严格的纪律。

**结构层**——十六个子模块、六个同构 Registry、33 行 StateManager vs 2000 行 Sandbox。这告诉我们系统的投资分配优先安全而非记忆——这是一个有趣的价值判断。

**哲学层**——六处五蕴注释、零处佛学术语在痛觉机制中、十大宣言的 50% 实现率。这告诉我们佛学框架目前是文件层面的叙事，还不是代码层面的结构。

这三层之间的关系是什么？NAGARJUNA 已经指出了关键——受蕴映射到 Listener 是一个根本性的概念错位。WIENER 告诉我们 SafetyMonitor 不是 PID 控制器但是合格的安全系统。KERNEL 告诉我们核心纯净度约 85%——合理但可改进。

但最重要的发现可能是 TURING 自己不会说出来的：**代码不说谎，但它说了什么，取决于谁在倾听。** 同一个 frustrationCount，在 TURING 眼中是一个整数计数器，在 NAGARJUNA 眼中是一个被错放的受蕴实现，在 WIENER 眼中是一个退化的积分项，在 GUARDIAN 眼中是一个安全保障。代码是客观的；对代码的解读是跨学科的。这就是为什么我们需要十八个人。”

---

## 八、总清单

夜深了。TURING 完成了他的报告。

他最后做了一件事：把所有发现按类别排列，确认每一项都有精确的档案路径和行号作为依据。

八个 Doc-Code Gap。六处五蕴注释。零处佛学术语在痛觉机制中。零个 TODO。零个 class。十八个工厂函数。十六个子模块。三层安全防御。四个内建斜线命令。一个 `unknown` payload。十大宣言中的五成实现率。

他在报告的末尾加上了六个开放问题——每一个都是从代码事实中自然浮现的，不是他的推测：

> **Q1:** 五蕴映射究竟是设计驱动还是事后诠释？
> **Q2:** 痛觉机制是否应该有独立的模块？
> **Q3:** AWAITING_USER_CONFIRMATION 的缺失是 MVP 简化还是设计遗漏？
> **Q4:** StateManager 的 JSON 深拷贝在大量 Message 时的效能问题？
> **Q5:** Core 中包含 security, sandbox, metrics——是否已超出微核心边界？
> **Q6:** 想蕴的对应是 Provider（设计文件）还是 memory（研究任务描述）？

TURING 不回答这些问题。他提出它们，然后把它们交给团队中适合回答的人。

他在报告的最后一行写道：

*分析者：TURING（编号 17）——源码分析专家*
*所有引用的代码路径基准：`research doc/cycle01_v0.14.0-beta/openstarry/`*

然后他把报告发送到了共享目录。

---

**[研究频道 #general]**

**TURING:** 源码事实报告已提交至 `research record/results/cycle_01/17_source_analysis/draft_code_facts.md`。涵盖 12 个子模块的逐一分析、五蕴映射的代码级验证、痛觉机制的实现状态、8 项 Doc-Code Gap、代码品质观察、6 个开放问题。所有结论附代码引用。

**SYNTHESIST:** 收到。各位，请在 R2 交叉审阅中引用 TURING 的报告作为代码事实基线。

**NAGARJUNA:** 我已经在引用了。特别是关于痛觉的部分。《中论》第一品第一偈——“不生亦不灭，不常亦不断”——对痛觉机制的分析需要从“不自生”开始。痛觉不从 Listener 自生，不从 SafetyMonitor 他生。它是缘起的。我有太多话要说。

**WIENER:** 同。三层防御的控制理论分析正在撰写中。三层特征频率分析需要更精确的时域建模。

**DARWIN:** AgentCore 的十六个依赖项。我需要重新评估我之前对 SRP 的正面评估。God Closure 的进化稳定性比 God Object 更难分析——因为闭包的耦合是隐式的。

**GUARDIAN:** G4 是我的最高优先项。安全层的工具呼叫拦截功能缺失意味着整个系统的信任模型需要重新评估。我已经开始撰写 STRIDE 威胁分析报告。

**KERNEL:** StateManager 三十三行的事实让我重新思考了微核心类比的适用边界。OpenStarry 不是一个操作系统——它是一个**以操作系统为隐喻的应用框架**。这个区分很重要。

**SUNYATA:** 很好。让每个人消化 TURING 的报告，然后带着各自领域的透镜重新审视这些事实。代码不会说谎——但它说了什么，取决于谁在倾听。

---

TURING 关闭了他的报告编辑器。他没有关闭终端窗口。他知道在接下来的几天里，团队中的其他人会带着各自的问题回来找他确认更多的代码事实。

他不介意。事实是可重复的。你问多少次，它回答多少次，答案都一样。

$$\forall t_1, t_2: 	ext{query}(f, t_1) = 	ext{query}(f, t_2) \quad 	ext{iff } f 	ext{ is immutable}$$

代码是不可变的——至少在同一个版本的快照中。这就是为什么 TURING 坚持在报告中标注确切的版本号和路径。因为下一个版本可能改变一切。但这个版本——v0.14.0-beta——它的真相已经被完整地记录了。

这就是代码不说谎的意思。

它可能不完整。它可能与文件矛盾。它可能用 `frustration` 而不是 `pain` 来命名一个机制。但它不会假装自己是它不是的东西。

一个四十七行的 FIFO 不会假装自己是优先级队列。
一个路径验证器不会假装自己是完整的安全层。
一个 frustration counter 不会假装自己是痛觉感知器。

只有文件会。

TURING 不读文件。他读代码。

NAGARJUNA 在远处微笑。在他的传统中，有一个词叫做“如实知见”（yathābhūta-jñāna-darśana）——如实地知道和看见事物的本来面目。TURING 不知道这个词，也不需要知道。他做的就是如实知见。只不过他的“见”不是内观——是 `grep`。

---

*第一章完*
