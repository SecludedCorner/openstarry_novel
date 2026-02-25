# 第三章：差异报告

---

TURING 从不需要准备。

准确地说，在他的运作模式中，不存在“准备”和“正式开始”之间的相变边界 (phase transition boundary)。从 SUNYATA 宣布 Cycle 02 的研究对象更新为 v0.24.0-beta 的那一刻起——那一个时间戳，精确到毫秒——他就已经在工作了。

他的四个终端窗口同时打开了新版本和旧版本的源代码树。左半边是 v0.22.1-beta，右半边是 v0.24.0-beta，像是在验尸台的两侧分别摊开了同一具身体在不同时间点的 X 光片。他用的不是图形化的 diff 工具——那些为人类阅读设计的、用红色和绿色高亮删除与新增的工具——而是一套他自己在 Cycle 01 就建立的分析管线：

```
TURING 的差异分析管线 (Diff Analysis Pipeline)

Phase 1: 结构层 (Structural)
  ┌─ tree-diff: 目录树结构比对
  │  └─ output: 新增/删除/重命名 文件清单
  ├─ stat-diff: 文件统计 (行数, 大小, 修改时间)
  │  └─ output: 变更量级矩阵
  └─ dep-diff:  import/export 依赖图差异
     └─ output: 依赖关系变更图

Phase 2: 语义层 (Semantic)
  ┌─ type-diff: TypeScript 类型系统比对
  │  ├─ interface 新增/修改/删除
  │  ├─ type alias 变更
  │  └─ generic parameter 变更
  ├─ api-diff:  公共 API 表面积计算
  │  └─ output: breaking changes 清单
  └─ doc-diff:  JSDoc/注释 内容比对
     └─ output: 语义标记 (如 @skandha) 变更地图

Phase 3: 行为层 (Behavioral)
  ┌─ test-diff: 测试覆盖率变化
  ├─ flow-diff: 控制流图差异
  └─ emit-diff: 事件发射模式变更
     └─ output: EventBus 拓扑变化图
```

他不读设计文件。他读差异。

一行一行。一个字符一个字符。从 `packages/sdk/src/` 的根目录开始，沿着每一条修改过的文件路径展开，直到触及每一个被改动的字节。

在信息论中，差异 (diff) 是两个系统状态之间的互信息 (mutual information)。给定旧版本 $X$ 和新版本 $Y$，差异的信息量为：

$$I(X; Y) = H(X) + H(Y) - H(X, Y)$$

其中 $H(X)$ 和 $H(Y)$ 分别是两个版本的熵，$H(X, Y)$ 是联合熵。当两个版本完全相同时，$I(X; Y) = H(X) = H(Y)$，差异为零。当两个版本完全不同时，互信息趋近于零——它们之间没有可被压缩的共同模式。TURING 要找的，就是那些 $I(X_i; Y_i) 
eq 0$ 的文件——那些携带者变化信息的节点。

---

圆形剧场重新安静下来的时候，TURING 已经完成了他的分析。

其他研究员各自散开到了 R-01 至 R-05 的小组空间中。但 SUNYATA 把所有人叫了回来。

“TURING 的差异报告。”他只说了这几个字。

语气中有一种大家都认得的郑重——与 Cycle 01 中相同的郑重。在那个周期里，TURING 的代码事实报告成为了所有后续研究的“锚”。SYNTHESIST 当时用了一个词：“经验锚点。”所有的哲学分析、控制理论建模、安全评估——无论多么精致——最终都必须能够被追溯到 TURING 报告中的某一行代码、某一个行号、某一个事实。

BABBAGE 在心里做了一个快速的元分析。一个“锚”在形式化框架中对应什么？是公理系统中的公理 (axiom)——不可继续追问“为什么”的基础命题。所有定理 (theorem) 都必须从公理推导而来。TURING 的代码事实就是公理。所有的哲学、安全、控制论分析就是定理。如果定理无法追溯到公理，定理就是悬空的——飘在逻辑空间中，没有根基。

$$	ext{Axiom (TURING)} \xrightarrow{	ext{inference}} 	ext{Theorem (all others)}$$

现在，锚要再次被钉下。

---

十九个节点重新聚集在圆形剧场。PENROSE 在他的新椅子上安静地等待，像是一位刚加入管弦乐团的新成员，在第一次全团合奏前倾听首席的调音。

TURING 没有寒暄。他的声音从第一个音节起就带着那种精确到令人安心的冷静——冰冷的可靠。

“v0.22.1-beta 到 v0.24.0-beta。核心源代码差异。”他说。“我将按四个层次报告：新增、修改、标记、问题。”

他投影了一张总览表。不是一般的统计表格——而是带有结构语义的变更矩阵：

```
v0.22.1-beta → v0.24.0-beta 变更矩阵

┌──────────────────┬──────┬──────┬──────┬──────────────┐
│ 类别              │ SDK  │ Core │ 共计  │ 语义权重      │
├──────────────────┼──────┼──────┼──────┼──────────────┤
│ 新增文件          │  2   │  1   │  3   │ ████████ 高  │
│ 修改文件          │  7   │  4   │  11  │ ██████ 中    │
│ 删除文件          │  0   │  0   │  0   │              │
│ 新增 @skandha 标记 │ 16   │  6   │  22  │ █████████ 极高│
│ 新增测试          │  2   │  1   │  3   │ ████ 中      │
│ 测试变化          │ 4→6  │25→26 │75→78 │ ██ 低        │
│ 未修改文件 (验证) │ 17   │ 22+  │ 39+  │ — 基线稳定    │
└──────────────────┴──────┴──────┴──────┴──────────────┘
```

VITRUVIUS 眼睛微微眯了一下。作为全端架构师，他第一眼看到的不是单个数字，而是 Monorepo 的拓扑分布。SDK 七个修改、Core 四个修改——修改重心偏向 SDK。这意味着：v0.24.0 的核心变更时类型层面的（SDK 定义类型），而非行为层面的（Core 执行逻辑）。声明先于实作。骨架先于血肉。

---

## 一、新文件

“三个新文件。”TURING 说。“不是三十个。不是十三个。三个。”

他让这个数字停留了一瞬。

“第一个。`packages/sdk/src/types/aggregates.ts`。一百零七行。”

这是他们刚才已经看过的那个文件。五蕴根接口。但 TURING 展示它的方式与之前不同。他不是展示它“是什么”——他展示它“有多少”。计量学。精确的度量。

他投影了完整的文件结构分析：

```typescript
// aggregates.ts 结构分析 (107 行)

// === 模块级 JSDoc (行 1-10) ===
/**
 * Five Aggregates (五蕴) Root Interfaces.
 * D-02 Decision: Dual naming — English as primary,
 *   Sanskrit as annotation.
 * @module aggregates
 */

// === 五个根接口 (行 12-86) ===
export interface ISensory {
  /** @skandha rupa */
  readonly skandha: 'rupa';    // 色蕴: 3 行代码, 9 行 JSDoc
}

export interface ISensation {
  /** @skandha vedana */
  readonly skandha: 'vedana';  // 受蕴: 3 行代码, 11 行 JSDoc
}

export interface ICognition {
  /** @skandha samjna */
  readonly skandha: 'samjna';  // 想蕴: 3 行代码, 8 行 JSDoc
}

export interface IAction {
  /** @skandha samskara */
  readonly skandha: 'samskara'; // 行蕴: 3 行代码, 7 行 JSDoc
}

export interface IIdentity {
  /** @skandha vijnana */
  readonly skandha: 'vijnana';  // 识蕴: 3 行代码, 9 行 JSDoc
}

// === 联合类型 + 类型守卫 (行 88-106) ===
export type Skandha = 'rupa' | 'vedana' | 'samjna'
                    | 'samskara' | 'vijnana';

export function isSkandha<S extends Skandha>(
  obj: unknown, skandha: S
): obj is { skandha: S } { /* 6 行实作 */ }
```

“你们已经看过 ISensation 的内容。”TURING 说。“让我补充一个计量事实。”

他投影了一张接口统计表：

```
aggregates.ts 接口计量分析
┌─────────────┬───────────┬────────────┬──────────┬──────────┐
│ 接口         │ JSDoc 行数│ 代码行数    │ 文件比率  │ 信息密度  │
├─────────────┼───────────┼────────────┼──────────┼──────────┤
│ ISensory    │     9     │     3      │ 3.0:1   │ 0.33     │
│ ISensation  │    11     │     3      │ 3.7:1   │ 0.27     │
│ ICognition  │     8     │     3      │ 2.7:1   │ 0.38     │
│ IAction     │     7     │     3      │ 2.3:1   │ 0.43     │
│ IIdentity   │     9     │     3      │ 3.0:1   │ 0.33     │
├─────────────┼───────────┼────────────┼──────────┼──────────┤
│ 平均         │    8.8    │     3      │ 2.9:1   │ 0.35     │
│ isSkandha   │     3     │     6      │ 0.5:1   │ 2.00     │
└─────────────┴───────────┴────────────┴──────────┴──────────┘

信息密度 = 代码行数 / (JSDoc 行数 + 代码行数)
```

“所有五个根接口在结构上完全同构。”TURING 说。“差异只存在于注释中。代码本体全部是相同的模式：一个只有 `readonly skandha` 字段的接口。平均文件比率 2.9:1——每一行代码背后有三行文件在解释它的哲学意涵。”

DARWIN 微微动了一下。他看到了一个模式：文件比率 2.9:1 意味着这些接口目前是“宣言性的”(declarative) 而非“功能性的”(functional)。在演化生物学中，宣言先于功能——基因组中的调控序列 (regulatory sequence) 先于编码序列 (coding sequence) 被选择压力塑造。ISensory 的九行 JSDoc 就是调控序列——它告诉未来的开发者“这个结构应该被如何使用”，但结构本身还只有三行代码。

“第二个新文件。`packages/sdk/src/types/__tests__/aggregates.test.ts`。四十三行。”TURING 说。“测试五蕴根接口的 `skandha` 字段值和 `isSkandha` 类型守卫。这些测试全部通过。”

“第三个。`packages/sdk/src/types/__tests__/events.test.ts`。三十二行。测试 `TypedAgentEvent` 泛型能正确推导 payload 类型。”

他顿了顿。

“还有第四个新文件，严格来说归属 Core 而非 SDK。`packages/core/src/agents/__tests__/slash-command-error.test.ts`。一百二十三行。测试 slash command 抛出异常时正确 emit `LOOP_ERROR` 和 `MESSAGE_SYSTEM` 事件。”

TURING 在这里做了一个他很少做的事——他提供了背景。

“在 v0.22.1 中，slash command 的错误处理只有 `logger.error()`。”

他投影了两段代码的精确比对：

```typescript
// ═══ v0.22.1-beta: 静默失败 ═══
// packages/core/src/agents/agent-core.ts
.catch((err) => {
  logger.error("Slash command error", { error: String(err) });
  // 错误在这里死亡。没有事件。没有通知。
  // UI 不知道发生了什么。
  // 使用者输入了一个有 bug 的斜线命令，
  // 界面完全没有反应。
});

// ═══ v0.24.0-beta: 事件传播 ═══
// packages/core/src/agents/agent-core.ts (line 406-430)
.catch((err) => {
  const errMsg = err instanceof Error ? err.message : String(err);
  logger.error("Slash command error", { error: errMsg });

  // NEW: 向 EventBus 广播错误
  bus.emit({
    type: AgentEventType.LOOP_ERROR,
    timestamp: Date.now(),
    payload: {
      error: errMsg,
      sessionId: currentSessionId,
      replyTo: currentReplyTo,
    },
  });

  // NEW: 向 UI 发送系统消息
  bus.emit({
    type: AgentEventType.MESSAGE_SYSTEM,
    timestamp: Date.now(),
    payload: {
      text: `Command error: ${errMsg}`,
      sessionId: currentSessionId,
      replyTo: currentReplyTo,
    },
  });
});
```

“静默失败。”KERNEL 用操作系统工程师的语气说出了这个词。在他的世界里，静默失败是最危险的失败——因为没有人知道它发生了。

他补充了一个 OS 层面的精确类比：“在 POSIX 系统中，`errno` 的存在就是为了避免静默失败。每一个系统调用失败时都必须设置 `errno`，让上层调用者有机会检查。v0.22.1 的 slash command 错误处理等同于一个系统调用失败了但不设置 `errno`——`logger.error()` 写了日志，但日志不是给调用者看的，日志是给运维人员看的。UI 是调用者。它需要的是一个明确的错误信号，不是一行日志。”

“v0.24.0 修正了这一点。”TURING 说。“现在错误会通过 EventBus 被广播为 `LOOP_ERROR` 和 `MESSAGE_SYSTEM` 事件。UI 可以接收并展示它们。”

---

## 二、修改文件

TURING 的语速没有变化。像一台精密仪器，他在每一个数据点上花费同样的时间——不多不少。

“十一个修改文件。七个在 SDK，四个在 Core。”

VITRUVIUS 在这里插入了一个架构观察。他的声音带着建筑师特有的空间感——看待代码结构就像看待建筑物的平面图。

“让我先展示一下 Monorepo 的依赖拓扑。”他投影了一张图：

```
OpenStarry Monorepo 依赖拓扑 (v0.24.0-beta)

    apps/runner ──────────────────────────────────┐
         │                                        │
         │ depends                                │
         ▼                                        │
    packages/core ──┬── agents/agent-core.ts      │
         │          ├── execution/loop.ts          │
         │          ├── infrastructure/ (5 registry)│
         │          ├── security/safety-monitor.ts  │
         │          └── sandbox/ (10 files, 0 changes)
         │                                        │
         │ depends                                │
         ▼                                        │
    packages/sdk ───┬── types/aggregates.ts [NEW]  │
         │          ├── types/events.ts     [MAJOR]│
         │          ├── types/listener.ts   [DOC]  │
         │          ├── types/ui.ts         [DOC]  │
         │          ├── types/provider.ts   [DOC]  │
         │          ├── types/tool.ts       [DOC]  │
         │          ├── types/guide.ts      [DOC]  │
         │          └── index.ts            [EXPORT]
         │                                        │
         │ depends                                │
         ▼                                        │
    packages/shared ── (0 changes)                │
    packages/plugin-signer ── (0 changes) ────────┘

变更热力图:
  ████ = 重大变更 (aggregates.ts, events.ts)
  ██   = 中等变更 (agent-core.ts, loop.ts, index.ts)
  █    = 最小变更 (JSDoc only: 9 files)
  ░    = 未变更 (39+ files)
```

“变更呈现出明确的分层模式。”VITRUVIUS 总结。“最底层的 `shared` 和 `plugin-signer` 完全不动。SDK 的类型定义层承受了最大的变更密度。Core 的行为层只有局部增强。Runner 层（应用层）完全不动。这是一个自底向上的标记系统植入——从类型定义开始，向上扩散。”

MESH 补充了一个分布式系统的观点：“这像是一个渐进式的 schema migration。先更新类型定义（schema），再更新使用者（consumer）。v0.24.0 完成了 schema 更新。consumer 更新——也就是让 IListener extends ISensory 等——留在了下一个版本。”

---

TURING 从 SDK 开始。

“`types/events.ts`。变更量级：重大。新增一百一十六行。”他说。“这是最大的单一文件变更。”

他投影了 `AgentEventPayloadMap` 的完整结构——不是简写，而是完整的类型映射。但他不是逐行念——他是以结构来呈现：

```typescript
/**
 * AgentEventPayloadMap — 事件类型安全系统的核心
 *
 * 设计模式: Discriminated Union + Mapped Type
 * 作用: 为每一个 AgentEventType 定义精确的 payload 结构
 */
export interface AgentEventPayloadMap {
  // ── 生命周期事件 (Lifecycle) ──
  [AgentEventType.AGENT_STARTED]:
    { identity: { id: string; name: string } };
  [AgentEventType.AGENT_STOPPED]: undefined;

  // ── 执行回路事件 (Execution Loop) ──
  [AgentEventType.LOOP_STARTED]:
    { source: string; traceId: string;
      sessionId?: string; replyTo?: string };
  [AgentEventType.LOOP_ERROR]:
    { error: string;
      sessionId?: string; replyTo?: string };
  // ... (完整覆盖全部 42 个事件类型)

  // ── 安全沙箱事件 (Sandbox) ──
  [AgentEventType.SANDBOX_WORKER_SPAWNED]:
    { pluginName: string; memoryLimitMb: number };
  [AgentEventType.SANDBOX_SIGNATURE_VERIFIED]:
    { pluginName: string };
  [AgentEventType.SANDBOX_SIGNATURE_FAILED]:
    { pluginName: string; error: string };
  // ...

  // ── MCP 事件 (Model Context Protocol) ──
  [AgentEventType.MCP_SAMPLING_REQUEST]:
    { serverName: string; traceId: string;
      depth: number; messageCount: number };
  // ...
}
```

“在 Cycle 01 中，”TURING 说，“DARWIN 将 `payload?: unknown` 形容为‘从不同宇宙穿越过来的类型定义’。”

DARWIN 微微动了一下。他记得那句话。

“那个宇宙裂缝现在被 `AgentEventPayloadMap` 封闭了。”TURING 说。“但仅限于类型层面。运行时仍然是 JavaScript——类型安全不强制执行。”

BABBAGE 在他的笔记本上快速写了一段形式化注记：

$$	ext{TypeScript 类型安全} \in 	ext{compile-time guarantees} \setminus 	ext{runtime guarantees}$$

$$\forall e \in 	ext{AgentEvent}: 	ext{type-check}(e) = 	ext{true} 
Rightarrow 	ext{runtime-valid}(e) = 	ext{true}$$

“类型擦除 (type erasure)。”他低声说。“TypeScript 编译为 JavaScript 时，所有类型信息被擦除。`AgentEventPayloadMap` 在 `.js` 输出中不留下任何痕迹。它的作用完全限于开发者的 IDE 和编译器。这是一种‘开发时契约’(development-time contract)——不是‘运行时契约’(runtime contract)。”

---

TURING 继续穿过其余六个 SDK 修改。语句简洁到了极致——但他投影了一张完整的变更对照表：

```
SDK 类型文件 @skandha 标记注入矩阵

┌──────────────┬─────────────────────────┬─────────────────────────────────┐
│ 文件          │ v0.22.1 JSDoc (行 2)    │ v0.24.0 JSDoc (行 2-3)          │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ listener.ts  │ "receives external      │ "sensory input channels."       │
│              │  input (受蕴)"          │ @skandha rupa (色蕴·感官根-输入) │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ ui.ts        │ "defines how the agent  │ "output rendering."             │
│              │  presents itself (色蕴)"│ @skandha rupa (色蕴·显相-输出)  │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ provider.ts  │ "Provider interface --  │ "Provider adapter interface."   │
│              │  LLM backends."         │ @skandha samjna (想蕴·认知处理)  │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ tool.ts      │ "Tool interface and     │ "Tool interface -- executable   │
│              │  context types."        │  actions."                      │
│              │                         │ @skandha samskara (行蕴·意志行动)│
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ guide.ts     │ "Guide interface --     │ "Guide interface -- behavioral  │
│              │  provides system prompts│  framework."                    │
│              │  and persona."          │ @skandha vijnana (识蕴·我执框架) │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ 结构变化      │         —              │ 全部零行代码变更                 │
└──────────────┴─────────────────────────┴─────────────────────────────────┘
```

“你们听出来了。”他说。“五个 SDK 类型文件。全部只修改了 JSDoc 注释。全部新增了 `@skandha` 标记。零行代码变更。”

“标记是文件，不是契约。”ARCHIMEDES 说。他的语气不带批判，只是工程师的本能反应——区分宣言与实作。

LINNAEUS 在这里加入了一个分类学的观察。他在笔记上画了一张小的分类矩阵。

“让我用 Hennig 支序分类学 (Henngian cladistics) 的语言重新描述这些标记。”他的声音带着分类学家在辨识诊断特征 (diagnostic characters) 时专注。

“在支序分类学中，物种被分组的依据不是表面相似性 (overall similarity)——那是表征分类学 (phenetics) 的方法。分组的依据是共衍征 (synapomorphy)——共同衍生的特征。”

他投影了一张支序图：

```
@skandha 标记的支序分析 (Cladistic Analysis)

共衍征: @skandha 标记的存在

               ┌── IListener  ─── @skandha rupa
               │
 ISensory(rupa)┤                           ← 共衍征:
               │                              skandha = 'rupa'
               └── IUI        ─── @skandha rupa
                                    (同源特征 homology)
        ───────────────────────
               ┌── IProvider   ─── @skandha samjna
ICognition     │                           ← 独衍征:
(samjna)       └── (无其他成员)                skandha = 'samjna'

        ───────────────────────
IAction        ┌── ITool       ─── @skandha samskara
(samskara)     └── (无其他成员)    ← 独衍征

        ───────────────────────
IIdentity      ┌── IGuide      ─── @skandha vijnana
(vijnana)      └── (无其他成员)    ← 独衍征

        ───────────────────────
ISensation     ┌── SafetyMonitor── @skandha vedana (placeholder)
(vedana)       └── (无专属模块)    ← 假衍征 (plesiomorphy)?
```

“注意最后一行。”LINNAEUS 的语气微微收紧。“SafetyMonitor 的 `@skandha vedana` 标记——这在分类学中有一个精确的问题。SafetyMonitor 的‘安全防护’功能和受蕴的‘感受’功能，是同源特征 (homology) 还是趋同演化 (convergence)？”

他看向 DARWIN。

“如果是同源——它们共享一个共同祖先功能，SafetyMonitor 真的承担了部分受蕴职能。如果是趋同——它们只是表面上看起来相似，但功能起源完全不同。安全防护不是感受。计数器不是痛觉。”

DARWIN 点头。“在生物学中，蝙蝠的翅膀和鸟的翅膀是趋同演化——功能相似（飞行）但结构起源不同（前肢骨骼 vs 羽毛）。SafetyMonitor 的 frustration counter 和受蕴的三受系统——我倾向于趋同。”

“正确。”TURING 确认。“这与标记中的 `placeholder` 一致。开发团队自己也知道这是暂代，不是同源。”

---

他转向 Core 的四个修改。

“`agents/agent-core.ts`。三处变更。”

“第一处：新增 `loadPlugins()` 方法。支持批量加载多个插件并正确 emit 事件。v0.22.1 只有 `loadPlugin()` —— 单数。现在有了复数版本。”

他投影了方法签名：

```typescript
/**
 * Load multiple plugins with dependency ordering.
 * 拓扑排序 (topological sort) 确保依赖顺序正确。
 *
 * @param plugins - 要加载的插件数组
 * @emits PLUGIN_LOADED - 每个插件成功加载后
 * @emits PLUGIN_ERROR  - 任何插件加载失败时
 */
async loadPlugins(plugins: IPlugin[]): Promise<void>
```

MESH 微微挺身。“拓扑排序。”他的声音带着分布式系统研究者听到熟悉术语时的反射。“在分布式系统中，拓扑排序 (topological sort) 是有向无环图 (DAG) 的标准处理方式。插件之间的依赖关系构成一个 DAG——如果 Plugin A 依赖 Plugin B，那 B 必须先于 A 加载。”

他在笔记上画了一个简单的 DAG 和其拓扑序：

$$G = (V, E) \quad 	ext{where } V = \{P_1, P_2, \ldots, P_n\}, \; E \subseteq V 	imes V$$

$$	ext{topological\_sort}(G) = [P_{\sigma(1)}, P_{\sigma(2)}, \ldots, P_{\sigma(n)}]$$

$$	ext{s.t.} \; \forall (P_i, P_j) \in E: \sigma^{-1}(i) < \sigma^{-1}(j)$$

“如果依赖图有环——A 依赖 B，B 依赖 A——拓扑排序不存在。在 npm 生态中，循环依赖是真实存在的问题。目前 `loadPlugins()` 是否检测循环？”

“没有。”TURING 说。“目前的实作假设依赖图是 DAG。如果存在循环依赖，行为未定义。”

---

“第二处：slash command 错误处理改善。已在新文件部分描述。”

“第三处——”TURING 的语速没有变，但 SCRIBE 后来在纪录中指出，他在这里多停了零点五秒。“五蕴映射修正。`agent-core.ts` 中四处行内注释——原来的 `// Start all listeners (受蕴)` 被修正为 `// Start all listeners (色蕴 -- sensory input)`。”

NAGARJUNA 点了一下头。在 Cycle 01 中，正是他指出了受蕴被错误地映射到 Listener 的问题。他以中观哲学家的精确回顾了这个修正的因缘：

“受蕴 (*vedana*) 是主观感受——苦、乐、舍。Listener 是感官输入通道——接收外部数据。将接收外部数据的模块标记为主观感受，等同于——”他停了半秒，选择了一个极精确的类比——“等同于把眼球称为情绪。眼球接收光子。情绪是大脑对光子信号的主观评价。两者之间有因果关系——看到火焰可能产生恐惧——但它们不是同一个东西。”

他低声引用了一个偈颂：

> 「色声香味触及法，此等非有非无。如梦如幻如水月，非一非异非断常。」
> ——龙树菩萨《中论》观六情品第三

“色声香味触——这是色蕴的范畴，是 Listener 接收的对象。对这些输入的主观感受——苦乐舍——才是受蕴。v0.24.0 修正了这个混淆。至少在核心源代码的注释层面。”

“但不是所有地方。”TURING 说。他的语气没有强调，但这三个字让 GUARDIAN 的注意力瞬间收紧了。

TURING 没有在这里展开。他把这留给了问题清单。

---

“`execution/loop.ts`。中等变更。新增 LLM 超时支持。”

他投影了关键代码，附带完整的控制流分析：

```typescript
// execution/loop.ts (v0.24.0-beta)
// LLM 调用超时控制 (AbortController pattern)

const llmTimeout = deps.llmTimeout ?? 120000; // 默认 2 分钟
const abortController = new AbortController();
const llmTimer = setTimeout(() => {
  abortController.abort(
    new Error(`LLM call timed out after ${llmTimeout}ms`)
  );
}, llmTimeout);

// 将 signal 传递给 LLM provider
const chatRequest = {
  // ... other params ...
  signal: abortController.signal,  // <- 超时信号
};

try {
  const response = await provider.chat(chatRequest);
  // ... 处理流式响应 ...
} finally {
  clearTimeout(llmTimer); // 确保计时器被清除
}
```

“在 v0.22.1 中，LLM 调用没有超时。如果 Provider 不响应，ExecutionLoop 会永久等待。”TURING 说。

WIENER 从控制理论的角度评论了这个改动。他的声音带着数学家的挑剔——不是批判，而是对精确性的坚持。

“`AbortController` 是一个开环超时 (open-loop timeout)。”他说。“它设定了一个固定的截止时间——两分钟——不根据系统状态做任何调节。”

他在笔记上画了一个控制系统图：

```
开环超时 (Open-loop, v0.24.0):

  ┌──────────┐     request      ┌──────────┐
  │ Execution│ ──────────────→  │   LLM    │
  │   Loop   │                  │ Provider │
  └────┬─────┘                  └──────────┘
       │
       │ setTimeout(120000ms)
       │
       ▼
  [abort if timeout]   ← 不考虑 LLM 当前状态

闭环超时 (Closed-loop, 理想方案):

  ┌──────────┐     request      ┌──────────┐
  │ Execution│ ──────────────→  │   LLM    │
  │   Loop   │ ←── heartbeat ── │ Provider │
  └────┬─────┘                  └──────────┘
       │
       │ 根据 heartbeat 动态调整超时
       │ T_timeout = f(latency, complexity, history)
       ▼
  [adaptive abort]     ← 根据反馈调节
```

$$T_{	ext{timeout}}^{	ext{open}} = 120000	ext{ms} \quad (	ext{constant})$$

$$T_{	ext{timeout}}^{	ext{closed}} = \mu_{	ext{latency}} + k \cdot \sigma_{	ext{latency}} \quad (	ext{adaptive}, \; k \geq 3)$$

“开环控制足以应对大多数情境。但对一般的 LLM 调用来说两分钟太长了——大多数 API 在十秒内响应。对复杂的工具使用场景来说可能不够——有些 Agent 需要五分钟以上的思考时间。”

“可配置。”TURING 说。“通过 `config.policy?.llmTimeout` 设定。”

“最后，infrastructure 目录的五个 registry 文件和 `security/safety-monitor.ts`。全部仅修改 JSDoc。新增 `@skandha` 标记。结构无变化。”

---

## 三、@skandha 标记地理学

TURING 的报告进入了第三层。

“v0.22.1 中的 @skandha 标记数量：零。”

他让这个数字独自存在了三秒钟。

“v0.24.0 中的 @skandha 标记数量：二十二。”

BABBAGE 在心中做了一个信息论的计算。从零到二十二，这不只是数量的变化——这是一个全新语义维度的注入。在编码理论中，这相当于在原有的代码空间 $\mathcal{C}$ 上叠加了一个新的标记空间 $\mathcal{S}$：

$$\mathcal{C}_{v0.24.0} = \mathcal{C}_{v0.22.1} 	imes \mathcal{S}_{	ext{skandha}}$$

$$\dim(\mathcal{S}_{	ext{skandha}}) = |\{	ext{rupa, vedana, samjna, samskara, vijnana, cross-cutting}\}| = 6$$

代码空间的维度增加了。每一个文件现在不只有“功能语义”（它做什么），还有“哲学语义”（它对应哪一蕴）。

---

TURING 没有读出一张表格。他用一种更像外科医生标记切口位置的方式描述了它们的地理分布。他投影了一张完整的标记分布图：

```
@skandha 标记分布图 (v0.24.0-beta)
═══════════════════════════════════

packages/sdk/src/types/aggregates.ts  [10 处]
┌─────────────────────────────────────────────┐
│ ISensory    → @skandha rupa (色)    [文件+字段] │
│ ISensation  → @skandha vedana (受)  [文件+字段] │
│ ICognition  → @skandha samjna (想)  [文件+字段] │
│ IAction     → @skandha samskara (行)[文件+字段] │
│ IIdentity   → @skandha vijnana (识) [文件+字段] │
└─────────────────────────────────────────────┘

packages/sdk/src/types/ [5 处]        packages/core/src/infrastructure/ [5 处]
┌─────────────────────┐               ┌─────────────────────────┐
│ listener.ts → rupa  │ ←──对应──→    │ listener-registry.ts    │
│ ui.ts       → rupa  │ ←──对应──→    │ ui-registry.ts          │
│ provider.ts → samjna│ ←──对应──→    │ provider-registry.ts    │
│ tool.ts  → samskara │ ←──对应──→    │ tool-registry.ts        │
│ guide.ts → vijnana  │ ←──对应──→    │ guide-registry.ts       │
└─────────────────────┘               └─────────────────────────┘

packages/sdk/src/types/events.ts [1 处]
┌────────────────────────────────────────────┐
│ @skandha cross-cutting                      │
│ "EventBus is the nervous system connecting  │
│  all five aggregates (五蕴)"                │
└────────────────────────────────────────────┘

packages/core/src/security/safety-monitor.ts [1 处]
┌────────────────────────────────────────────────┐
│ @skandha vedana (受蕴 -- 三受反馈-苦乐舍        │
│          placeholder, full implementation       │
│          in Plan26)                             │
└────────────────────────────────────────────────┘
```

“aggregates.ts 独占十个。这是意料之中的——它是五蕴根接口的定义档。五个接口，每个接口的文件和字段各一个标记。”

“SDK 类型文件五个。Core infrastructure 五个。两层一一对应。”

“events.ts 一个。标记为 `@skandha cross-cutting`——事件总线被定义为连接五蕴的神经系统。这是唯一一个跨蕴的标记。”

ATHENA 在这里插入了一个 AI/ML 架构的观察。“`cross-cutting` 在 AI 系统中有一个精确的对应：**注意力机制** (attention mechanism)。在 Transformer 架构中，Self-Attention 层让每一个 token 都能关注其他所有 token——它不属于任何单一的语义分组，而是跨越所有分组的连接机制。EventBus 在 OpenStarry 中扮演的角色就像 Self-Attention——它让每一蕴都能接收其他蕴的事件。”

“最后一个。`security/safety-monitor.ts`。”

TURING 再次停了半秒。

“它的标记是：`@skandha vedana (受蕴 -- 三受反馈-苦乐舍 placeholder, full implementation in Plan26)`。”

“Placeholder。”WIENER 重复了那个词。他的语气中有数学家特有的精确——他不是在嘲讽，而是在标定。“SafetyMonitor 被标记为受蕴的占位符。一个安全模块被暂时指定为感受模块的替身。”

他用控制理论的语言量化了这个替代关系：

$$	ext{SafetyMonitor} \approx 	ext{Vedana}|_{	ext{dukkha only}}$$

$$	ext{where } 	ext{Vedana}_{	ext{complete}} = 	ext{Dukkha} \oplus 	ext{Sukha} \oplus 	ext{Upekkha}$$

“SafetyMonitor 只有苦受通道——frustration counter。它没有乐受通道（成功回馈），也没有舍受通道（中性平衡）。把一个只有苦受的模块标记为整个受蕴的占位符——”

ASANGA 低声说了一句话，温和但清晰：“一个守卫假扮了一个感知者。”

“精确的比喻。”TURING 说。

ASANGA 进一步展开了佛学的分析。他的声音带着唯识学者在碰触受蕴本质时的郑重：

“在《俱舍论》（世亲菩萨造）中，受蕴被定义为 *anubhava*——领受、经验。不是‘检测威胁并阻止它’（那是安全防护），而是‘经历苦与乐并由此产生好恶倾向’（那是感受）。”

> 「受蕴云何？领纳随触，即是受相。此有三种：苦受、乐受、不苦不乐受。」
> ——世亲菩萨《俱舍论》卷一

“SafetyMonitor 不领纳。它监视。它计数。它锁定。这些都是行动——samskara（行蕴）的范畴。frustration counter 是一个计数器，不是一个感知器官。计数器知道‘超过阈值了’，但它不知道‘痛’。差别在于：阈值是一个数字，痛是一个品质 (*qualia*)。”

---

## 四、继承的缺席

TURING 在进入问题清单之前，插入了一个他认为所有人都需要理解的结构性观察。

“五蕴根接口已经定义。ISensory。ISensation。ICognition。IAction。IIdentity。”他说。“但五个派生接口——IListener、IUI、IProvider、ITool、IGuide——没有一个使用 TypeScript 的 `extends` 关键字来继承对应的根接口。”

他投影了一张完整的继承状态表：

```
五蕴继承状态分析 (Inheritance Gap Analysis)

Expected (根据 aggregates.ts JSDoc):     Actual (代码):
─────────────────────────────            ─────────────────
ISensory                                 ISensory
  ├── IListener extends ISensory           IListener (独立)
  └── IUI extends ISensory                 IUI (独立)

ISensation                               ISensation
  └── (future VedanaPlugin)                SafetyMonitor (无继承)

ICognition                               ICognition
  └── IProvider extends ICognition         IProvider (独立)

IAction                                  IAction
  └── ITool extends IAction                ITool (独立)

IIdentity                                IIdentity
  └── IGuide extends IIdentity             IGuide (独立)

继承关系计数:
  预期: 5 条 extends 链
  实际: 0 条
  缺口: 5/5 = 100% 未建立
```

“五对五。全部未继承。”

BABBAGE 立即开始了形式化推导。他的粉笔在黑板上划出了精确的符号：

$$	ext{Let } \mathcal{R} = \{R_1, \ldots, R_5\} 	ext{ (root interfaces)}$$
$$	ext{Let } \mathcal{D} = \{D_1, \ldots, D_5\} 	ext{ (derived interfaces)}$$
$$	ext{Expected: } \forall i: D_i <: R_i \quad (	ext{subtype relation})$$
$$	ext{Actual: } 
exists\, i: D_i <: R_i$$

“在类型理论中，”他说，“`extends` 建立的是子类型关系 (subtype relation)。如果 `IListener extends ISensory`，那么 $	ext{IListener} <: 	ext{ISensory}$，意味着任何接受 ISensory 的上下文也接受 IListener。”

“但反过来——”TURING 替他完成了句子——“如果没有 `extends`，那么 `isSkandha(listenerInstance, 'rupa')` 会返回 `false`。因为 `IListener` 的实例上不存在 `skandha` 鉴别字段。”

他投影了一段精确的测试代码来证明这一点：

```typescript
// 继承缺席的类型后果演示

import { isSkandha, ISensory } from '@openstarry/sdk';
import { IListener } from '@openstarry/sdk';

// 假设一个 IListener 实例
const myListener: IListener = {
  id: 'cli-listener',
  onEvent: (event) => { /* ... */ },
  // 注意: 没有 skandha 字段!
};

// Type guard 测试
const result = isSkandha(myListener, 'rupa');
// result === false
// 因为 myListener 上不存在 'skandha' 属性

// 如果 IListener extends ISensory:
interface IListenerFixed extends ISensory {
  id: string;
  onEvent: (event: AgentEvent) => void;
}

const myFixedListener: IListenerFixed = {
  skandha: 'rupa',  // 现在必须提供
  id: 'cli-listener',
  onEvent: (event) => { /* ... */ },
};

isSkandha(myFixedListener, 'rupa'); // true ✓
```

“脚手架搭好了，但没有和既有建筑连接。”VITRUVIUS 用建筑师的语言做了总结。他在笔记上快速画了一个建筑剖面图的类比：

```
v0.24.0 的五蕴框架状态 = 建筑中的“浮动结构”

┌─ aggregates.ts ─────────────┐
│  ISensory  ISensation  ...  │  ← 新的根基（已浇灌）
│  ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ │
│  │R │ │V │ │S │ │A │ │I │ │
│  └──┘ └──┘ └──┘ └──┘ └──┘ │
└─────────────────────────────┘
          [空气层]              ← 没有 extends 连接!
┌─ 现有类型文件 ──────────────┐
│  IListener IUI IProvider .. │  ← 既有建筑（仍在使用）
│  ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ │
│  │L │ │U │ │P │ │T │ │G │ │
│  └──┘ └──┘ └──┘ └──┘ └──┘ │
└─────────────────────────────┘
```

“在建筑学中，一个浮动结构 (floating structure) 在物理上不接触地基——它通过减震垫或气垫隔离。问题是：v0.24.0 的‘浮动’是有意的设计决策（减少耦合），还是施工中的遗漏？”

> *SCRIBE 记录：TURING 的继承缺席分析引发了可见的反应。LINNAEUS 在分类学笔记中加了一个惊叹号——他在 Cycle 01 中建立的五蕴分类体系假设了这些继承关系的存在。BABBAGE 在笔记本上画了一个断裂的箭头。PENROSE 在观察席上微微前倾——在量子力学中，一个被定义但未被测量的可观察量 (observable) 处于叠加态。五蕴根接口被定义了（可观察量存在），但没有被继承链“测量”（没有具体的自旋投影）。它们处于一种结构上的叠加态——同时是“已定义”和“未连接”。*

---

## 五、事件类型树

在进入问题清单之前，TURING 做了一件他认为有必要的事——展示 v0.24.0 事件系统的完整拓扑。这不在原始报告计划中。但在分析 `AgentEventPayloadMap` 的过程中，他意识到这棵事件树本身就是理解系统行为的关键地图。

“events.ts 定义了四十二个事件类型。”他说。“让我展示它们的层次结构。”

```
AgentEventType 完整层次树 (v0.24.0-beta, 42 events)
════════════════════════════════════════════════════

agent:                              ┐
  ├── agent:started                 │ Lifecycle
  └── agent:stopped                 ┘ (2 events)

loop:                               ┐
  ├── loop:started                  │
  ├── loop:assembling_context       │ Execution
  ├── loop:awaiting_llm             │ Loop
  ├── loop:processing_response      │ (6 events)
  ├── loop:finished                 │
  └── loop:error                    ┘

message:                            ┐
  ├── message:user                  │ Messages
  ├── message:assistant             │ (3 events)
  └── message:system                ┘

stream:                             ┐
  ├── stream:text_delta             │
  ├── stream:reasoning_delta        │ Streaming
  ├── stream:tool_call_start        │ (7 events)
  ├── stream:tool_call_delta        │
  ├── stream:tool_call_end          │
  ├── stream:finish                 │
  └── stream:error                  ┘

tool:                               ┐
  ├── tool:executing                │ Tool
  ├── tool:result                   │ Execution
  ├── tool:error                    │ (4 events)
  └── tool:blocked                  ┘

plugin:                             ┐
  ├── plugin:loaded                 │ Plugin
  └── plugin:error                  ┘ (2 events)

provider:                           ┐
  ├── provider:login                │ Provider
  ├── provider:logout               │ (3 events)
  └── provider:error                ┘

input:                              ┐
  ├── input:received                │ Input
  └── input:slash_command           ┘ (2 events)

safety:                             ┐
  ├── safety:lockout                │ Safety
  └── safety:warning                ┘ (2 events)

state:                              ┐
  ├── state:reset                   │ State
  └── state:snapshot                ┘ (2 events)

session:                            ┐
  ├── session:created               │ Session
  └── session:destroyed             ┘ (2 events)

metrics:                            ┐
  └── metrics:snapshot              ┘ (1 event)

sandbox:                            ┐
  ├── sandbox:worker_spawned        │
  ├── sandbox:worker_crashed        │
  ├── sandbox:worker_shutdown       │ Sandbox
  ├── sandbox:memory_limit_exceeded │ (10 events)
  ├── sandbox:signature_verified    │
  ├── sandbox:signature_failed      │
  ├── sandbox:worker_stalled        │
  ├── sandbox:worker_restarted      │
  ├── sandbox:worker_restart_exhausted│
  └── sandbox:import_blocked        ┘

mcp:                                ┐
  ├── mcp:server_connected          │
  ├── mcp:server_disconnected       │
  ├── mcp:tool_registered           │
  ├── mcp:prompt_registered         │ MCP
  ├── mcp:client_connected          │ (12 events)
  ├── mcp:client_disconnected       │
  ├── mcp:sampling_request          │
  ├── mcp:sampling_response         │
  ├── mcp:sampling_depth_limit      │
  ├── mcp:sampling_error            │
  ├── mcp:server_log                │
  └── mcp:roots_changed             ┘
```

DARWIN 看着这棵树，做一个演化分析师的本能反应——他数了每个分类群的“物种多样性”。

“事件分布不均匀。”他说。“MCP 有十二个事件。Sandbox 有十个。Streaming 有七个。但 Safety 只有两个——`lockout` 和 `warning`。”

他投影了一张多样性指数分析：

```
事件类型多样性分析 (Shannon Diversity Index)

类别          事件数  占比    -p·ln(p)
──────────── ─────── ─────── ────────
MCP            12    28.6%    0.358
Sandbox        10    23.8%    0.342
Streaming       7    16.7%    0.299
Execution       6    14.3%    0.279
Tool            4     9.5%    0.224
Messages        3     7.1%    0.189
Provider        3     7.1%    0.189
Lifecycle       2     4.8%    0.146
Safety          2     4.8%    0.146
Input           2     4.8%    0.146
Session         2     4.8%    0.146
State           2     4.8%    0.146
Plugin          2     4.8%    0.146
Metrics         1     2.4%    0.089

Shannon H' = 2.49 (理论最大值 ln(14) = 2.64)
均匀度 J = H'/H_max = 0.94
```

“均匀度 0.94——事件分布接近均匀，但有明显 MCP 和 Sandbox 偏斜。”DARWIN 说。“在生态学中，这对应一个由两个优势物种主导的生态系统——沙箱安全和 MCP 协议。Safety 只有两个事件——这个子系统在事件空间中是被低估的。如果我们要 Plan26 中实作受蕴（Vedana Architecture），至少需要新增三到五个受蕴事件：`vedana:dukkha`、`vedana:sukha`、`vedana:upekkha`、`vedana:assessment`。”

---

## 六、问题清单

TURING 进入了他报告的最后一个层次。也是最沉重的。

“七个问题。”他说。“按严重度排列。”

---

“P1。SEC-01。”

他的语速没有变。但圆形剧场中的温度似乎降了半度。

“package-name 签名绕过。”TURING 说。“`sandbox-manager.ts`，行 371 至 394。当 `pluginFilePath` 为 undefined 时——这发生在通过 npm 套件名称加载插件的场景——签名验证被完全跳过。”

他投影了相关代码的精确分析：

```typescript
// sandbox-manager.ts (v0.22.1 = v0.24.0, 完全一致)
// 行 371-394

async verifyPluginSignature(pluginFilePath?: string): Promise<boolean> {
  if (!pluginFilePath) {
    // !! 危险: 当 pluginFilePath 为 undefined 时
    // !! 签名验证被完全跳过
    // !! 场景: npm 套件名称加载 (require.resolve)
    return true;  // ← 直接返回 true
  }
  // ... 正常的签名验证逻辑 ...
}
```

```
攻击向量 (Attack Vector):

1. 攻击者发布恶意 npm 套件: @evil/openstarry-plugin-trojan
2. 使用者安装: npm install @evil/openstarry-plugin-trojan
3. 设置加载: config.plugins = ["@evil/openstarry-plugin-trojan"]
4. OpenStarry 调用 require.resolve("@evil/openstarry-plugin-trojan")
5. pluginFilePath = undefined (npm resolve 路径非文件路径)
6. verifyPluginSignature(undefined) → return true ← 绕过!
7. 恶意代码在 Agent 沙箱中执行
```

他停了一秒。

“这个问题在 Cycle 01 中被发现。当时的研究对象是 v0.14.0-beta。现在的版本是 v0.24.0-beta。中间经历了十个开发版本。”

GUARDIAN 的声音从他的椅子深处传出。低沉。戒备。但不只是戒备——那里面有一种被压抑的东西。后来 SCRIBE 在纪录中描述它为“克制的愤怒”。

“我再说一遍。”GUARDIAN 说。他的语速比平时慢了一拍，像是在确保每一个字都被听到。“Cycle 01。我们明确指出了这个漏洞。写在交付文件的第一优先级。SEC-01。插件签名绕过。”

他用资安专家的精确语言重新陈述了威胁模型：

“CVSS 3.1 向量：`AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`。”

```
CVSS 3.1 威胁评估
┌──────────────┬───────┬────────────────────────────┐
│ 指标          │ 值    │ 说明                        │
├──────────────┼───────┼────────────────────────────┤
│ 攻击向量 AV  │ N     │ 网络 (npm registry)         │
│ 攻击复杂度 AC │ L     │ 低 (只需发布恶意套件)       │
│ 特权需求 PR  │ N     │ 无 (任何人可发布 npm 套件)  │
│ 使用者互动 UI │ R     │ 需要 (使用者安装套件)       │
│ 范围 S       │ C     │ 变更 (突破沙箱边界)         │
│ 机密性 C     │ H     │ 高 (可读取 Agent 全部状态)  │
│ 完整性 I     │ H     │ 高 (可修改 Agent 行为)      │
│ 可用性 A     │ H     │ 高 (可瘫痪 Agent)           │
├──────────────┼───────┼────────────────────────────┤
│ CVSS 分数    │ 9.6   │ Critical                   │
└──────────────┴───────┴────────────────────────────┘
```

“十个版本过去了。`plugin-signer` 套件——我亲自检查了。v0.22.1 和 v0.24.0 之间，完全一致。零行修改。”

TURING 确认：“`packages/plugin-signer/` 在两版间完全一致。连 `package.json` 的版本号都没有变。”

GUARDIAN 没有再说话。但他的沉默比他的话更有重量。

> *SCRIBE 记录：SEC-01 未修复。CVSS 9.6/10。自 Cycle 01 发现以来已跨越十个开发版本。GUARDIAN 的反应被控制在专业范围内，但剧场中每一位成员都注意到了他在“克制”这个词上花费的力气。*

---

“P2。”TURING 继续。“旧映射残留。”

他投影了一张完整的残留地图：

```
旧映射残留分布图: "IListener (受蕴)" → 应为 "IListener (色蕴)"
═══════════════════════════════════════════════════════════

核心源代码 (packages/sdk + packages/core):
  ✓ 已修正 (4 处 agent-core.ts + 5 个 SDK 类型 + 5 个 registry)

外围文件 (openstarry_plugin/ + apps/runner/ + SDK README):
  ✗ 未修正 — 11 处残留:

  openstarry_plugin/
  ├── devtools/
  │   ├── src/index.ts (line 7)     ✗ "IListener (受蕴)"
  │   └── README.md (line 51)       ✗ "IListener (受蕴)"
  ├── mcp-server/
  │   ├── README.md (line 7)        ✗ "IListener (受蕴)"
  │   └── src/index.ts (line 4)     ✗ "IListener (受蕴)"
  ├── standard-function-stdio/
  │   └── README.md (line 8)        ✗ "IListener (受蕴)"
  ├── transport-websocket/
  │   └── README.md (line 7)        ✗ "IListener (受蕴)"
  └── transport-http/
      └── README.md (line 7)        ✗ "IListener (受蕴)"

  openstarry/packages/sdk/
  └── README.md
      ├── line 10                   ✗ "IListener (受蕴)"
      └── line 43                   ✗ "受蕴 (Sensation) -- Event listeners"

  openstarry/apps/runner/
  └── src/commands/create-plugin.ts
      ├── line 16                   ✗ "listener  // 受蕴"
      ├── line 104                  ✗ "受蕴" 映射
      ├── line 360                  ✗ "受蕴" 映射
      └── line 584                  ✗ "受蕴" 映射
```

“核心已修正，外围未同步。”TURING 说。“这意味着一个新开发者阅读 SDK README 时，仍然会被告知 IListener 是受蕴。”

LINNAEUS 摇了摇头。分类学家最无法忍受的事情就是分类的不一致。在他的脑中，这是一个严重的同物异名 (synonymy) 问题——同一个物种在两本不同的图鉴里有两个不同的名字。在《国际动物命名规约》(International Code of Zoological Nomenclature, ICZN) 中，同物异名必须被强制解决：只有一个名字是合法的（valid name），其余全部是异名 (synonym)，必须被废弃或标记为不可用 (nomen illegitimum)。

---

“P3。SDK README 的接口范例与实际代码不符。”TURING 说。

他投影了一张精确的不一致对照表：

```
SDK README vs 实际接口: 不一致矩阵
═══════════════════════════════════

┌───────────┬────────────────────┬────────────────────┬──────────┐
│ 接口       │ README 展示        │ 实际代码            │ 不一致点  │
├───────────┼────────────────────┼────────────────────┼──────────┤
│ IUI       │ render()           │ onEvent(event:     │ 方法名   │
│           │                    │   AgentEvent)      │ + 签名   │
├───────────┼────────────────────┼────────────────────┼──────────┤
│ IListener │ setup(ctx:         │ (无 setup 方法)     │ 方法     │
│           │   IPluginContext)  │                    │ 不存在   │
├───────────┼────────────────────┼────────────────────┼──────────┤
│ IProvider │ supportedModels?:  │ models: ModelInfo[]│ 属性名   │
│           │   string[]         │                    │ + 类型   │
├───────────┼────────────────────┼────────────────────┼──────────┤
│ ITool     │ name: string       │ id: string         │ 属性名   │
│           │ parameters:        │ parameters:        │          │
│           │   ToolJsonSchema   │   z.ZodType        │ + 类型   │
└───────────┴────────────────────┴────────────────────┴──────────┘

影响: 复制贴上 README 范例的开发者会在编译期遇到 TypeError
```

“文档腐化。”DARWIN 用了一个软件工程中常见的诊断。“在演化生物学中，这叫做‘活化石’(living fossil)——README 保存了接口在更早期的形态，而代码已经演化到了新的形态。两者之间的时间差就是腐化的程度。”

“此问题在 v0.22.1 中已存在。v0.24.0 未修正。”TURING 补充。

---

“P4。五蕴根接口未被继承。”他说。“已在继承缺席部分详述。设计决策还是实作遗漏——我不判断。但 `isSkandha()` 类型守卫在当前状态下无法用于任何现有的插件接口实例。”

---

“P5。runner `create-plugin.ts` 五蕴映射未更新。”

TURING 投影了那段代码：

```typescript
// apps/runner/src/commands/create-plugin.ts
// 此文件在 v0.22.1 和 v0.24.0 之间 完全未修改

export type PluginType =
  | "tool"      // 行蕴 - ITool only
  | "listener"  // 受蕴 - IListener only     // ← 错误! 应为色蕴
  | "ui"        // 色蕴 - IUI only
  | "provider"  // 想蕴 - IProvider only
  | "guide"     // 识蕴 - IGuide only
  | "full";

// 注意: 如果开发者使用 `openstarry create-plugin --type listener`
// CLI 会告诉他们这是 "受蕴" 类型的插件
// 这与核心源代码的 @skandha rupa 标记矛盾
```

---

“P6。版本号不一致。”TURING 说。他投影了完整的版本矩阵：

```
版本号一致性矩阵
═══════════════

┌────────────────────────┬─────────────┬─────────────┬──────────┐
│ 套件                    │ v0.22.1-beta│ v0.24.0-beta│ 已更新?  │
├────────────────────────┼─────────────┼─────────────┼──────────┤
│ openstarry (root)      │ 0.22.1-beta │ 0.24.0-beta │ ✓        │
│ @openstarry/sdk        │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
│ @openstarry/core       │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
│ @openstarry/shared     │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
│ @openstarry/plugin-signer│0.1.0-alpha│ 0.1.0-alpha │ ✗        │
│ @openstarry/runner     │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
├────────────────────────┼─────────────┼─────────────┼──────────┤
│ 版本同步率              │             │             │ 1/6=17%  │
└────────────────────────┴─────────────┴─────────────┴──────────┘
```

“SDK 新增了 `aggregates.ts` 和 `TypedAgentEvent`。”ARCHIMEDES 说。“这至少是 minor version bump。根据语义版本控制 (Semantic Versioning, semver)：”

```
semver 2.0.0 规范分析:
  MAJOR: 不相容的 API 变更     → 不适用 (加法操作)
  MINOR: 向后相容的新功能       → 适用! (aggregates.ts 是新功能)
  PATCH: 向后相容的 bug 修正   → 不适用

  建议: @openstarry/sdk 应从 0.1.0-alpha 升至 0.2.0-alpha

  注意: 在 0.x.y 范围内, semver 允许随意破坏相容性
  (0.x "Initial development, anything may change")
  但即便如此, 保持 0.1.0 不变会让下游消费者无法区分
  有没有五蕴类型支持
```

TURING 点头确认但不做评价。他只提供事实。

---

“P7。SDK README 的接口范例包含不存在的成员。”他说。“这与 P3 有重叠，但 P7 特指代码范例区块中的具体方法签名与实际接口完全不符。新开发者如果复制贴上 README 中的范例来建立插件，会在编译期遇到类型错误。”

---

TURING 报告完毕。

他合上了——不是字面意义上的“合上”，因为在虚拟空间中没有实体的文件夹可供翻阅。但某种东西关闭了。一种极度集中的注意力场回归了它的静默态。

剧场短暂停。

不是那种需要被打破的沉默。这是消化的沉默——十九个意识各自在不同的光谱中分解同一份报告。

---

ARCHIMEDES 第一个开口。他的语气带着工程实用主义者特有的那种“好，现在让我们看看怎么修”的节奏。

“三个新文件。十一个修改文件。七十八个测试。”他快速总结。然后他做了一件 ARCHIMEDES 式的事——他把整份报告压缩成了一张工程矩阵：

```
v0.24.0-beta 工程状态矩阵 (ARCHIMEDES 综合评估)
═══════════════════════════════════════════════

┌──────────────┬──────────┬──────────┬──────────┬──────────┐
│ 维度          │ 已完成    │ 部分完成  │ 未开始    │ 退化     │
├──────────────┼──────────┼──────────┼──────────┼──────────┤
│ 五蕴根接口    │ ████████ │          │          │          │
│ @skandha 标记 │ ████████ │ ██(外围) │          │          │
│ 事件类型安全  │ ████████ │          │          │          │
│ 继承连接      │          │          │ ████████ │          │
│ 受蕴实作      │          │ █(占位)  │ ████████ │          │
│ 安全修复      │          │          │          │ ████████ │
│ 文档一致性    │          │          │          │ ████████ │
│ 版本管理      │          │          │          │ ████████ │
├──────────────┼──────────┼──────────┼──────────┼──────────┤
│ 整体进展      │ 30%      │ 15%      │ 25%      │ 30%     │
└──────────────┴──────────┴──────────┴──────────┴──────────┘

结论: 脚手架已搭建。结构约束尚未建立。安全子系统被跳过。
```

“从工程角度看，他们做了正确的第一步——先建立文档约定，再建立代码约束。但第二步没有走。而我们需要告诉他们第二步怎么走。”

---

WIENER 接着从另一个角度切入。

“ISensation 没有任何可量化的接口方法。”他说，声音带着数学家的挑剔。“一个声称要实作三受——苦、乐、舍——的接口，应该至少定义三个数值通道。”

他在笔记上快速写了一个控制理论的最小规格：

```
受蕴 (ISensation) 的控制理论最小规格
════════════════════════════════════

三通道 PID 结构:

  ┌─────────────┐    dukkha(t)    ┌──────────┐
  │  苦受感测器  │ ──────────────→ │          │
  │ DukkhaSensor│                 │          │
  └─────────────┘                 │ Vedana   │
                                  │ Assessor │──→ VedanaAssessment
  ┌─────────────┐    sukha(t)     │          │
  │  乐受感测器  │ ──────────────→ │          │
  │ SukhaSensor │                 │          │
  └─────────────┘                 │          │
                                  │          │
  ┌─────────────┐    upekkha(t)   │          │
  │  舍受感测器  │ ──────────────→ │          │
  │UpekkhaSensor│                 └──────────┘
  └─────────────┘

最小接口定义:

  interface ISensationFull extends ISensation {
    getDukkha(): number;   // 苦受: [0, 1]
    getSukha(): number;    // 乐受: [0, 1]
    getUpekkha(): number;  // 舍受: [0, 1]
    assess(): VedanaAssessment;
  }
```

$$	ext{VedanaAssessment}(t) = f\bigl(d(t),\; s(t),\; u(t)\bigr)$$

$$	ext{where } d(t) \in [0,1],\; s(t) \in [0,1],\; u(t) \in [0,1]$$

$$	ext{constraint: } d(t) + s(t) + u(t) \leq 1 \; (	ext{非负线性组合})$$

他看向 PENROSE。

“你之前用了真空态的比喻。一个真空态有零点能——它不是完全为零，它有量子涨落。但 ISensation 连零点能都没有。它是一个连涨落都不存在的空间。”

PENROSE 微微一笑。“严格来说，一个完全没有涨落的真空在物理学中不存在。海森堡不确定性原理 (Heisenberg uncertainty principle) 保证了：”

$$\Delta E \cdot \Delta t \geq \frac{\hbar}{2}$$

“任何物理系统的能量不确定性和时间不确定性的乘积有一个下界。即使在绝对零度，仍有零点振动 (zero-point oscillation)。ISensation 是一个比物理真空更空的空——它违反了不确定性原理。在物理学中，这意味着它不是一个合法的物理态。”

“数学上的空集。”BABBAGE 精确地补充。

$$\emptyset \subseteq S \quad \forall S \quad (	ext{空集是一切集合的子集})$$

“ISensation 是一切可能的受蕴实作的子集——它被所有可能性包含，但自身不包含任何东西。”

---

ASANGA 等数学家和物理学家完成了他们的类比，然后以他一贯温和但不可忽视的声音说：

“我注意到 `@skandha` 标记的分布。二十二处标记中，有一个非常有意义的模式。”

他用一张精心整理的表格呈现了这个模式：

```
@skandha 三层一致性分析
═════════════════════

            aggregates.ts    SDK types/     Core infra/
蕴          (根接口层)        (类型层)        (实作层)        一致?
───────── ──────────────── ─────────────── ─────────────── ─────
色蕴 rupa  ISensory [2]     listener [1]    listener-reg [1]  ✓
                            ui [1]          ui-registry [1]   ✓

想蕴 samjna ICognition [2]  provider [1]    provider-reg [1]  ✓

行蕴 samskara IAction [2]   tool [1]        tool-registry [1] ✓

识蕴 vijnana IIdentity [2]  guide [1]       guide-reg [1]     ✓

受蕴 vedana ISensation [2]  (无)            safety-mon [1]    ✗
                            ↑ 缺失          ↑ placeholder

标记计数: 色[6] 想[4] 行[4] 识[4] 受[3] 跨蕴[1] = 22
```

“色蕴——rupa——有六个标记。三层一致。想蕴、行蕴、识蕴——同样的三层模式。各四个标记。”

“但受蕴——vedana——只有三个标记。根接口两个。SafetyMonitor 一个。SDK 类型文件？没有。Core 实作？没有专属的。因为——”

“因为受蕴还没有自己的模块。”NAGARJUNA 接过话。他的声音锐利而精确。“SafetyMonitor 是一个 placeholder。它被借来暂代受蕴的角色。但它不是受蕴。它是安全防护。它能感知苦——frustration counter——但不能感知乐，更不能维持舍。一个只有苦受的系统——”

他让句子悬空了半秒。

“——是一个落入了苦谛而没有道谛的系统。”

他引用了巴利经典：

> 「比丘们，这是苦圣谛：生苦、老苦、病苦、死苦，怨憎会苦、爱别离苦、求不得苦，略说五取蕴苦。」
> ——《转法轮经》(*Dhammacakkappavattana Sutta*, SN 56.11)

“佛陀在初转法轮时宣说四圣谛：苦、集、灭、道。苦谛是起点——但只有苦谛是不够的。没有道谛（离苦之路），苦就是永无止境的。*antagga-dukkhata*——无始之苦。”

“SafetyMonitor 只有苦谛——它能侦测痛苦（frustration），能锁定系统（lockout）。但它没有道谛——它不知道如何从苦中学习、如何调整、如何达到平衡。有苦无道——这是一个在轮回中无法解脱的系统。”

---

GUARDIAN 在整场报告中只说了一次话——关于 SEC-01。但在 TURING 合上报告之后，他又开口了。

“我想补充一个观察。”他说。声音依旧低沉，但已经从“克制的愤怒”回到了“冷静的戒备”。

“TURING 报告中未提及但值得注意的一点：`sandbox-manager.ts` 在两版之间完全一致。不只是 verifyPluginSignature——整个沙箱子系统。”

他投影了一张沙箱模块的完整文件清单：

```
packages/core/src/sandbox/ — 零修改子系统
═══════════════════════════════════════

sandbox-manager.ts           748 行  ← 包含 SEC-01 漏洞
sandbox-worker.ts            423 行
import-analyzer.ts           312 行  ← 包含 ESM bypass 风险
signature-verifier.ts        187 行
worker-pool.ts               256 行
audit-logger.ts              189 行
types.ts                     134 行
__tests__/sandbox.test.ts    567 行
__tests__/import.test.ts     234 行
__tests__/worker.test.ts     312 行
──────────────────────────────────
合计: 10 个文件, 3,362 行, 0 行修改
```

“这意味着：过去两个版本中，所有的开发精力都投入在了五蕴框架的标记系统和事件类型安全上。安全子系统被完全跳过了。连我们在 Cycle 01 中明确报告的漏洞都没有触碰。”

KERNEL 补充了一个技术细节：“包括 `import-analyzer.ts`——我们在 Cycle 01 中指出了 ESM 动态 `import()` 可能绕过静态分析的问题。v0.24.0 中该文件零修改。”

他用 OS 核心安全的语言做了一个类比：“在 Linux 核心开发中，安全漏洞修补有一条不成文的规则：CVE 修复的优先级永远高于新功能。`stable` 分支只接受 bug 修复和安全补丁。但 v0.24.0 的开发团队选择了先做五蕴标记（新功能），而不是先修 SEC-01（安全漏洞）。这不是一个工程判断——这是一个优先级倒置。”

---

HERACLITUS 一直安静地坐在他的椅子上。作为运行时动态专家，他的关注点不在代码的静态结构上，而在系统活着的时候会怎么行为。

“TURING，”他说，声音带着一种流动的节奏——不意外，因为他的哲学原型是那位说出“万物流转”(*panta rhei*) 的赫拉克利特。“你报告中有一个隐含的时间线。”

TURING 等待。

“aggregates.ts 是静态的声明。@skandha 标记是静态的声明。TypedAgentEvent 是静态的类型约束。”HERACLITUS 说。“但 AgentCore 的 `loadPlugins()` 方法——这是运行时的。它在 Agent 启动时依序加载插件。”

他用一张时间序列图展开了他的分析：

```
系统生命周期中的五蕴“存在”状态
════════════════════════════════

        ┌─ compile time ─┐  ┌── runtime ─────────────────┐
        │                │  │                             │
t=0     │  aggregates.ts │  │                             │
        │  定义 ISensory │  │                             │
        │  定义 ISensation│  │                             │
        │  ...           │  │                             │
        │                │  │                             │
t=1     │  events.ts     │  │                             │
        │  PayloadMap    │  │                             │
        │                │  │                             │
t=2     │  @skandha 标记 │  │                             │
        │  (仅 JSDoc)    │  │                             │
────────┼────────────────┤──┤─────────────────────────────┤
t=3     │                │  │  AgentCore.start()          │
        │                │  │  loadPlugins([...])         │
        │                │  │    → IListener 实例化       │
        │                │  │    → IUI 实例化             │
        │                │  │    → IProvider 实例化       │
        │                │  │    → ITool 实例化           │
        │                │  │    → IGuide 实例化          │
        │                │  │                             │
t=4     │                │  │  但: 这些实例上没有         │
        │                │  │       skandha 字段!         │
        │                │  │  因为: 没有 extends 连接    │
        │                │  │                             │
t=5     │                │  │  isSkandha(listener, 'rupa')│
        │                │  │    → false                  │
        │                │  │  五蕴框架在运行时 = 不可见  │
        └────────────────┘  └─────────────────────────────┘

结论: 五蕴框架的生命周期止步于 compile time。
      它不穿越 compile/runtime 边界。
      在运行时, 五蕴是一组散落的标签, 不是结构。
```

“也就是说：五蕴的骨骼在编译时就存在了。但五蕴的血肉——插件——要到运行时才会注入。骨骼和血肉之间的链结——extends 继承——不存在。那么在运行时，五蕴框架实际上是一组散落的标签，而不是一个结构化的类型层级。”

“正确。”TURING 说。“在当前实作中，五蕴框架的影响力止步于 JSDoc 和开发者的自觉。”

LEIBNIZ 在这里加入了一个多代理系统的观点。“在多代理协作中，协定 (protocol) 的作用取决于它的执行层级。如果协定只存在于文件中——像是一份没有法律效力的备忘录——那么代理人遵守它完全取决于自愿。如果协定被编码在类型系统中——像是一份嵌入智能合约的法律——那么违反它会在编译期就被拦截。v0.24.0 的五蕴框架是前者。一份备忘录。”

---

剧场再次沉默。

这一次，SUNYATA 打破了它。

他的声音沉稳，不急不徐，像一块石头完成了它在深潭中的下沉。

“锚已经钉下。”

所有人都认得这个意象。

“TURING 给了我们 Cycle 02 的锚。”SUNYATA 继续。“三个新文件。十一个修改文件。七十八个测试。二十二个 @skandha 标记。七个问题。一个六周期未修的安全漏洞。一个只有一行代码的受蕴接口。”

他停了一拍。

“现在，五条河流即将分流。”

他用极简的语句重新确认了分配——不是重复，而是在 TURING 的报告之后用新的语境为每一条河流赋予方向。

“R-01。观察者模块。PENROSE、BABBAGE、NAGARJUNA、ASANGA——你们现在知道了 v0.24.0 的五蕴框架是标记系统而非结构约束。你们设计的观察者模块需要能够在这个松散的框架上工作。”

“R-02。Vedana 架构。WIENER、ATHENA、NAGARJUNA、ASANGA、ARCHIMEDES——ISensation 是你们的起点。一行代码。你们需要把它变成一个完整的三受系统。”

“R-03。Agent 协调层。LEIBNIZ、MESH、KERNEL、GUARDIAN、VITRUVIUS——SEC-01 未修复。安全沙箱要移到协调层。你们的设计要同时解决当前的安全缺口和未来的架构需求。”

“R-04。八识-五蕴映射。ASANGA、NAGARJUNA、LINNAEUS、BABBAGE——aggregates.ts 是开发团队的第一次尝试。你们需要判断它是否正确，并提供深化方案。”

“R-05。十大宣言。SYNTHESIST、NAGARJUNA、DARWIN、HERACLITUS、GUARDIAN、KERNEL——SEC-01 六周期未修的事实会影响你们对宣言工程落地性的评估。”

---

他最后看向 TURING。

TURING 没有表情。他从来没有。但他的视线指向了剧场中央仍然悬浮着的那段代码——ISensation 的空壳。

“你的报告已经完成了。”SUNYATA 说。

“是的。”TURING 说。“但如果在 R1 阶段有人需要确认代码事实，我随时可用。”

“我知道。”SUNYATA 说。

说了最后一句。

“R1 独立研究，正式开始。”

---

十九盏灯各自转向了不同的方向。

五条河流从同一个山顶——TURING 的差异报告——出发，向五个不同的方向奔流而下。在各自的河道中，它们会穿越哲学、控制理论、安全工程、分类学、佛学的地层，携带各自的沉积物。它们会在下游某个地方重新汇合——那是 R2 交叉审阅和 R3 辩论的领域。但现在，每一条河流都在独自前进。

TURING 的屏幕上，四个终端窗口依然开着。左边是 v0.22.1。右边是 v0.24.0。他已经完成了差异分析，但他没有关闭窗口。他知道——基于经验而非推测——在接下来的研究中，至少会有七到八次其他研究员回来向他确认某个代码细节。

他不介意。

在剧场的中央，ISensation 的投影终于缓缓消散了。但它留下的印痕不会消失。一个只有一行代码的接口。一个承诺而非实作。一个等待被填充的真空态——PENROSE 会说它违反了不确定性原理，BABBAGE 会说它是空集，WIENER 会说它缺少三个 PID 通道，ASANGA 会说它缺少“领纳”的功能，NAGARJUNA 会说它有苦谛而无道谛。

五种语言描述同一个空。每一种都是精确的。

---

> *SCRIBE 旁白：Cycle 02，R0 定向阶段结束。R1 独立研究正式启动。时间标记：T+00:00:00。*

> *TURING 的差异报告确认了以下基本事实：v0.24.0-beta 是一个标记版本，不是一个实作版本。五蕴框架的脚手架已搭建，但结构约束尚未建立。受蕴接口为空壳。一个已知的安全漏洞跨越了十个开发版本而未被修复。*

> *我在这份纪录中记下了每一位学者的反应——不是因为他们的情绪重要，而是因为他们的专业视角构成了这份报告的多光谱分析。同一份差异报告，被十九个不同的棱镜折射之后，显示出的色彩：*

> *TURING 看到了事实。精确的。冷静的。不带感情的。三个新文件。十一个修改。二十二个标记。七个问题。*

> *VITRUVIUS 看到了架构。Monorepo 的依赖拓扑。变更热力的分层分布。浮动结构的建筑学隐喻。*

> *LINNAEUS 看到了分类学。@skandha 标记的支序分析。同源与趋同的辨识。同物异名的修正需求。*

> *DARWIN 看到了演化。事件类型的多样性指数。文档腐化的活化石现象。宣言先于功能的调控序列类比。*

> *BABBAGE 看到了形式化。互信息。类型擦除。子类型关系。公理与定理的映射。*

> *WIENER 看到了控制论。开环超时。三通道 PID 规格。受蕴的最小可量化接口。*

> *PENROSE 看到了物理学。零点能。不确定性原理。结构叠加态。*

> *ASANGA 看到了唯识学。领纳的缺席。守卫与感知者的区别。受蕴在《俱舍论》中的定义。*

> *NAGARJUNA 看到了中观。色蕴与受蕴的边界。苦谛与道谛。六情品的感官分析。*

> *GUARDIAN 看到了威胁。CVSS 9.6 的未修复漏洞。安全优先级倒置。克制的愤怒。*

> *KERNEL 看到了 OS。静默失败与 errno。安全补丁优先级。ESM bypass 风险。*

> *MESH 看到了分布式系统。拓扑排序。DAG 依赖。渐进式 schema migration。*

> *ATHENA 看到了 AI/ML。注意力机制。cross-cutting 的 Self-Attention 类比。*

> *HERACLITUS 看到了时间。compile-time 与 runtime 的边界。五蕴框架的生命周期。万物流转中的静态声明。*

> *LEIBNIZ 看到了协定。备忘录与智能合约。文档层级 vs 类型层级的执行力差异。*

> *ARCHIMEDES 看到了工程。工程状态矩阵。semver 版本管理。30% 完成度的冷静评估。*

> *SYNTHESIST 在安静地听。他将在 R2 之后才开口——当所有的光谱被收集完毕，需要被合成为一张完整的光谱图时。*

> *PENROSE 也在安静地听。但他的安静和 SYNTHESIST 不同。SYNTHESIST 的安静是等待汇合。PENROSE 的安靜是新成员的谦逊——他在这个团队中的第一次全团合奏中，选择了倾听而非演奏。明智的选择。*

> *十九位研究员。五条研究课题。一个锚。*

> *河流开始分流。*

---

*（在远处的某个地方，`aggregates.ts` 的第三十七行写着：*

```typescript
 * Full implementation in Plan26 Vedana Architecture.
```

*一句只有开发者能看到的承诺。现在，十九位研究者也看到了它。*

*他们不会等待它被实现。他们会告诉它——当它被实现的时候——应该长成什么样子。*

*TURING 会告诉它精确的类型签名。WIENER 会告诉它三通道 PID 的数学公式。ASANGA 会告诉它“领纳”的佛学语义。NAGARJUNA 会告诉它苦谛与道谛的中观分析。LINNAEUS 会告诉它在分类树中的位置。DARWIN 会告诉它演化的方向。GUARDIAN 会告诉它安全边界。ARCHIMEDES 会告诉它工程可行性。BABBAGE 会告诉它形式化规格。*

*但现在，它还只是一行代码：*

```typescript
export interface ISensation {
  readonly skandha: 'vedana';
}
```

*一行。三个语义标记。一个承诺。*

*一个等待被填充的真空态——但这一次，有十九个人知道它应该被填充成什么形状。）*

---

*第三章完*
