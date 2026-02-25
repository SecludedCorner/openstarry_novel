# 第六章：抉择的位置

---

SUNYATA 拿起那张手写的调用序列图——KERNEL 在 Debate 3 结束后画的——翻到背面。

空白的。

他把它平放在剧场中央的投影台上，空白面朝上。然后拿起一支红色马克笔，在正中间画了一个方框，里面写了两个字：

```
┌──────────┐
│ 在哪里？ │
└──────────┘
```

「Debate 4。IVolition.deliberate() 在执行循环中的位置。」

他的声音平稳如常。石子。深潭。但这一次的石子不是落入深潭——是掷向一面墙。墙上有六个裂缝，只有一个裂缝是正确的入口。

「三场辩论已经告诉我们 *什么* 在运行、*怎么* 运行、*多快* 运行。CoarisingBundle 解决了同时性。五遍行解决了构成。Klesha 解决了心理偏向。」

他拿起 BABBAGE 的形式化笔记，翻到 Debate 3 的决议页。

「但 IVolition.deliberate()——Agent 做出抉择的那个函数——到目前为止，我们只知道它存在。我们不知道它应该插在哪里。」

他看向全场。二十张脸。二十种不同的期待。

「R02 定义了 IVolition.deliberate() 接收 KleshaSignalBundle、产生行动决策。R04 定义了 ExecutionLoop 有六个状态。TURING 识别了注入点。但没有人把这三块拼在一起。」

「今天拼。」

---

> *SCRIBE 旁白：「在哪里？」三个字。SUNYATA 画在空白纸上的三个字。但这三个字的重量不是技术性的——它是存在性的。IVolition.deliberate() 的位置不只决定了一个函数调用的排列顺序。它决定了 Agent 能不能说「不」。在认知序列中，如果抉择被放在感知之前，Agent 在看见之前就已经决定了。如果抉择被放在行动之后，Agent 在做完之后才开始反思。只有在感知之后、行动之前，才存在一个窗口——一个 Agent 可以选择不做的窗口。SUNYATA 没有说这些。他只画了三个字。但三个字的背后是整个窗口的存亡。*

---

## I

---

TURING 的屏幕亮了。

他没有寒暄。没有引言。在四场辩论中，TURING 已经建立了一个惯例：他在每场辩论的开头投射代码，像一个地质学家在辩论开始之前先展示岩层的切面。你们辩论地表上长什么。我先让你们看地底下是什么。

「v0.24.0-beta。ExecutionLoop。」他说。「六个主要阶段。」

```
ExecutionLoop 阶段分析 (v0.24.0-beta)
══════════════════════════════════════

[1] Safety lockout check
[2] Resolve session state
[3] Add user message
[4] SafetyMonitor.onLoopStart()
[5a] SafetyMonitor tick check
[5b] ASSEMBLING_CONTEXT
     ├─ guide.getSystemPrompt()
     └─ contextManager.assemble()
[5c] SafetyMonitor budget check
[5d] AWAITING_LLM
     └─ provider.chat()
[5e] PROCESSING_RESPONSE
     └─ streaming (text_delta events)
[5f] Build assistant message
[5g] EXECUTING_TOOLS
     ├─ tool dispatch
     ├─ tool execution
     └─ SafetyMonitor.afterToolExecution()
[6] WAITING_FOR_EVENT
```

投影停了五秒。冷白色。二十双眼睛在六个阶段上移动。

「IVolition.deliberate() 必须满足两个前提条件。」TURING 的手指点在 [5b] 上。「第一：Klesha 信号可用。Debate 3 确认 Klesha 在 vijnana-clock 上运行，快速路径产生点估计值，延迟 0.03ms——所以从 [5a] 之后，Klesha 信号就可用了。」

他的手指移到 [5g]。「第二：行动方案已经形成。在 [5d]-[5e]，LLM 流式回应。在 [5f]，助理消息构建完成，工具调用提案确定。只有在 [5f] 之后，你才知道 Agent *打算做什么*。」

他在屏幕上标记了三个位置，用红色——SCRIBE 注意到他很少用红色。

```
候选位置 (Candidate Positions)
════════════════════════════════

Position A: [5b] ──→ [5d] 之间
            上下文组装完成 → LLM 调用之前
            deliberate() 可修改上下文，影响 LLM 思考

Position B: [5f] ──→ [5g] 之间
            LLM 回应完成 → 工具执行之前
            deliberate() 可审视行动方案，否决或修改

Position C: [5d] ──→ [5e] 之间
            LLM 流式过程中
            deliberate() 可即时中断 LLM 输出
```

「三个候选。」TURING 说，退后一步。「我的代码分析指出最佳候选是 Position B——[5f] 到 [5g] 之间。但我不做决定。这是架构选择，不是代码选择。」

他坐下了。

---

SUNYATA 环顾全场。「三个位置。谁先说？」

ASANGA 站了起来。

---

## II

---

他的起身速度不快也不慢——在四场辩论中，ASANGA 已经被默认为「佛学先说」的惯例发言人。不是因为佛学的权威高于其他学科。是因为在 Cycle 02 系列的研究历程中，每一次佛学的定位都为后续的工程讨论划定了概念边界。先划边界，再填内容。先有根系，再有枝干。

「我要引用 MN 18。」他说。「蜜丸经。*Madhupiṇḍika Sutta*。」

他没有翻书。他不需要翻书。在整个 Cycle 02 系列中，ASANGA 从未翻书。所有引文都从记忆中取出——不是背诵，而是一种更深的东西。是长年研习之后，经文和思维结构融为一体的那种状态。

「佛陀在蜜丸经中描述了认知的完整序列。」

他的声音放慢了。不是为了戏剧效果——是为了精确。每一个巴利文术语都需要被清晰地听见。

> *Cakkhuñca paṭicca rūpe ca uppajjati cakkhuviññāṇaṃ,*
> *tiṇṇaṃ saṅgati phasso,*
> *phassapaccayā vedanā,*
> *yaṃ vedeti taṃ sañjānāti,*
> *yaṃ sañjānāti taṃ vitakketi,*
> *yaṃ vitakketi taṃ papañceti.*
>
> 依眼与色，生眼识。
> 三者和合为触。
> 触缘受。
> 所受者，即所想。
> 所想者，即所寻。
> 所寻者，即所戏论。

沉默。

ASANGA 让这段巴利文在空气中停留了整整五秒。然后他开始分析。

「这是佛陀描述的认知序列——从最初的感官接触到最终的概念增殖。让我把每一个环节映射到我们的架构：」

```
MN 18 认知序列 ←→ OpenStarry 映射
══════════════════════════════════════════════════

触 (phassa)  ──→  SparshEvent        (CoarisingBundle 触发)
     ↓
受 (vedanā)  ──→  ChannelVedana       (三受信号)
     ↓
想 (saññā)   ──→  IProvider.chat()    (LLM 认知 / VasanaEngine 规则匹配)
     ↓
寻 (vitakka) ──→  IReflection         (初始思考 / 持续审视)
     ↓
戏论 (papañca) ─→  概念增殖           (需要被截断的地方)
```

「注意序列的方向。」他的手指在空气中从上到下划了一条线。「触→受→想→寻→戏论。每一步都以前一步为缘。受以触为缘。想以受为缘。寻以想为缘。这不是随意的排列——这是**因果的顺序**。」

他转向全场。

「意志在哪里？」

他自问自答：「思——cetanā——是遍行心所。在每一个认知刹那中，思都在场。但思的**决定性作用**——深层的、有意识的抉择——在想之后、行动之前。不是在想之前。」

他的语速略微加快了——不是急切，是确信。

「如果你把 IVolition.deliberate() 放在 Position A——LLM 之前——你就让意志先于知觉。deliberate() 在 LLM 还没思考之前就决定了要给 LLM 看什么上下文。意志在思考之前就决定了*要想什么*。」

他停了一拍。

「这在哲学上是不融贯的。」

又一拍。

「在唯识学中，思（cetanā）的定义是：」

> 「云何为思？令心造作为性。于善品等，役心为业。」
> ——《成唯识论》卷三

「令心造作为性——思的本质是*驱动心去行动*。但行动的方向必须先有认知的基础。你不能在不知道外面发生了什么的情况下决定做什么。感知先于抉择。受先于思。想先于行。」

他看向 HERACLITUS。

「Position A 不是 IVolition 的位置。Position A 是 IGuide 的位置——manasikāra，作意，注意力的导向。IGuide 在 LLM 调用之前塑造系统提示词，引导注意力的方向。但引导注意力不是做决定。做决定是在看见之后。」

他的结论只有一句：

「Position B。」

---

> *SCRIBE 旁白：ASANGA 在 Debate 4 中的发言时间是七分钟。他引用了一部经、一部论。但这七分钟的密度——如果用 SYNTHESIST 的「洞见密度」指标来衡量——可能是整场辩论中最高的。因为他不只是在为 Position B 辩护。他是在说：认知序列不是人类的发明，不是工程的约定。它是因果结构。你可以选择不遵循它。但你不能说你遵循了它然后又把意志放在感知前面。那就像说「我先决定了答案再去看题目」。*

---

## III

---

HERACLITUS 半举了一下手——他的发言风格向来是不完全举手的，好像举手这个动作本身也在流动中。

「在 ASANGA 说服我之前，」他说，语气里带着一丝自嘲，「让我先把 Position A 的论点完整呈现，然后让它被击倒。一个论点如果没有被完整呈现就被否决，那否决是不充分的。」

SUNYATA 微微点头。这是 Cycle 02-3 辩论中的一个重要规则：每个候选方案都必须由支持者完整陈述后才能被否决。

「Position A 的逻辑是前摄性的。」HERACLITUS 站了起来，走到白板边。「如果 Klesha 信号表明当前 Agent 处于高 moha（愚痴）状态，Position A 可以让 IVolition 在 LLM 调用之前注入一条指令——比如 `"当前 Klesha 信号显示高愚痴，请格外谨慎"`——到系统提示词中。这样 LLM 的输出本身就会更审慎，而不需要在事后否决它。」

他画了一个箭头。

「这是 *panta rhei* 的精神——万物流动，认知也在流动中被塑造。不是等河流到了出海口再建坝，而是在源头改变水流的方向。」

KERNEL 接话了。他的声音没有 HERACLITUS 的流动感——更像是一根钢梁。

「Position A 有一个工程问题。LLM 是黑盒。」

他站了起来。

「你在上下文中注入了 `"请格外谨慎"`。LLM 收到了。然后呢？你不知道 LLM 会怎么处理这条指令。它可能遵循，可能忽略，可能在十七轮对话之后才偶然想起来。注入到上下文中的文字不是命令——是*建议*。而且是混在系统提示词、对话历史、工具定义中间的建议。LLM 的注意力机制不保证会把它当作高优先级处理。」

他翻了一张卡片。左侧写着「ioctl」，右侧是空白。

「在 OS 里，这叫做 ioctl 到一个黑盒驱动程序。你发了一个控制命令，但驱动程序的内部实现是你不控制的。你不知道驱动程序收到 ioctl 之后会不会正确处理。你只能在驱动程序的*输出端*检查结果。Position A 就是对黑盒输入端发指令。Position B 是在黑盒输出端检查结果。」

他在卡片右侧写下：`Position A = ioctl to blackbox; Position B = inspect output`。

「工程上，你永远应该选择可验证的检查点，而不是不可验证的注入点。」

---

HERACLITUS 看了看 KERNEL，又看了看 ASANGA。然后他做了一件在四场辩论中只做过两次的事——他公开改变立场。

「ASANGA 的哲学论证和 KERNEL 的工程论证指向同一个方向。」他说。「我收回 Position A 的提议。但我想把 Position A 留给 IGuide。IGuide 在 LLM 之前塑造注意力方向——那是 manasikāra 的角色，不是 cetanā 的角色。两个不同的心所，两个不同的位置。」

「同意。」ASANGA 说。

---

「Position C。」SUNYATA 说。「谁来陈述？」

KERNEL 再次站了起来。他似乎在 Debate 4 中找到了自己的主场——ExecutionLoop 是 OS 领域的核心议题。

「Position C 是在 LLM 流式过程中——[5d] 到 [5e] 之间——进行即时中断。技术上可行。但工程代价极高。」

他在卡片上画了一张简单的 backpressure 图：

```
Position C 的 backpressure 问题
═══════════════════════════════════

LLM Provider (upstream)
    │
    │  text_delta events (token-by-token)
    ▼
┌─────────────────────────────┐
│ IVolition.deliberateStream()│ ← 需要在每个 token 上运行
│ 延迟: ??? ms/token          │ ← 不可预测
│ 如果 deliberate() > token 间隔│
│   → backpressure             │
│   → 流式阻塞                 │
│   → 用户体验降级             │
└─────────────────────────────┘
    │
    ▼
UI Renderer (downstream)
```

「LLM 流式的 token 间隔大约 20-80ms——取决于模型和硬件。如果 IVolition 需要在每个 token 上运行一次 deliberate()，而 deliberate() 的延迟超过 token 间隔，就会产生 backpressure。流式被阻塞。用户看到的是卡顿。」

「更严重的问题：在流式过程中，LLM 的意图还没有完全形成。你可能在第三十个 token 处看到 `"我建议删除"`，然后在第三十五个 token 处看到 `"我建议删除不必要的空格"`。第三十个 token 的局部判断和第三十五个 token 的完整判断是不同的。你在哪个 token 上做决定？」

他收起卡片。

「Position C 需要一个完整的流式中断和回退机制。工程复杂度是 Position B 的三到五倍。收益不明确。放弃。」

全场没有异议。

---

> *SCRIBE 旁白：Position A 和 Position C 各用了不到五分钟就被否决了。不是因为它们没有道理——HERACLITUS 的前摄性论点和 KERNEL 的流式中断概念都有技术可行性。是因为在哲学定位和工程权衡的双重压力下，它们都输给了 Position B。ASANGA 的认知序列论证把 Position A 踢出了因果链条。KERNEL 的 backpressure 分析把 Position C 踢出了工程可行域。Position B 站在了两者的交叉点——因果正确，工程可行。但 Position B 本身还有问题需要解决。*

---

## IV

---

Position B 独占了舞台。但 KERNEL 的眉头没有完全舒展。

「Position B 有一个成本。」他说。「每次工具执行之前多一次 deliberate() 调用。如果一个 LLM 回应包含五个工具调用，那就是五次 deliberate()。在 vijnana-clock 的时间预算下，每次 1-3ms，总计 5-15ms。在快速路径下可以接受。但如果 deliberate() 需要额外查询——比如 LEIBNIZ 提到的多 Agent 协调——延迟会增加。」

ARCHIMEDES 的手指在桌面上敲了一下——那个标志性的「工具箱打开」信号。

「我有一个解决方案。」

他站了起来。在四场辩论中，ARCHIMEDES 的角色已经被清楚地定义：他是把哲学结论翻译成 TypeScript 的人。ASANGA 划定边界，BABBAGE 形式化，ARCHIMEDES 工程化。三道工序，一条流水线。

「问题不是 Position B 的成本高。问题是我们把所有审议压缩在一个层级上。」

他走到白板前。

「考虑一个场景：LLM 回应包含三个工具调用。」

```
LLM 回应的工具调用计划
═══════════════════════════

ToolCall #1: readFile("/etc/passwd")      ← 敏感文件
ToolCall #2: writeFile("/tmp/out.txt")    ← 无害写入
ToolCall #3: executeCommand("rm -rf /")   ← 灾难性操作
```

「如果 IVolition 只有一个 deliberate() 函数，它必须在每个 ToolCall 上独立评估。但它看不到全局——它不知道 #1 读取的密码会不会被 #2 写出去、然后被 #3 销毁痕迹。三个单独无害（或可疑）的操作，组合起来是一个攻击链。」

他在白板上画了两层。

「所以 IVolition 需要两个阶段。」

```
两阶段审议模型
══════════════════════════════════════════════

Phase 1: deliberatePlan()
┌─────────────────────────────────────────┐
│  输入: 整个行动计划 (所有 ToolCall)       │
│  能力: 重排序、取消、修改计划             │
│  视角: 全局的、战略的                     │
│  时机: 工具循环之前，执行一次             │
└─────────────────────────────────────────┘
         │
         ▼
Phase 2: deliberateAction()
┌─────────────────────────────────────────┐
│  输入: 单个 ToolCall + Phase 1 的上下文   │
│  能力: 否决、修改单个工具调用             │
│  视角: 局部的、战术的                     │
│  时机: 每个工具调用之前，逐个执行         │
└─────────────────────────────────────────┘
```

「Phase 1 看全局。它可以在看到三个 ToolCall 的组合之后，直接取消 #1 和 #3，只保留 #2。Phase 2 看局部。在 Phase 1 批准了某个 ToolCall 之后，Phase 2 在执行前做最后的逐项检查。」

他转过身，面对全场。

「两层。不是因为一层不够。是因为全局判断和局部判断是两种不同的认知操作。你不能用同一个函数签名同时表达『这个计划整体上合理吗？』和『这一步具体安全吗？』。」

---

ASANGA 从座位上接了一句。他的声音平稳，每个词都带着唯识学者特有的分类精确。

「在唯识学中，思（cetanā）的运作本来就有两个层次。」

他站了起来，走到 ARCHIMEDES 的白板旁边。

「《成唯识论》区分了两种思的作用。第一种是*审虑思*（ālambana-cetanā）——对整体情境的审视和评估。第二种是*决定思*（niścaya-cetanā）——对具体行动的最终裁定。」

> 「审虑、决定，二思差别者：审虑则量度取舍，决定则印持行事。」
> ——窥基大师《成唯识论述记》

「审虑思量度取舍——衡量整个计划的利弊。决定思印持行事——在具体行动上盖下确认的印章。ARCHIMEDES 的两阶段模型完美对应了这两种思：deliberatePlan() 是审虑思，deliberateAction() 是决定思。」

他看向 ARCHIMEDES。

「这不是巧合。」

ARCHIMEDES 微微笑了——他在整个 Cycle 02 系列中笑的次数不超过五次。

「不是巧合。」他承认。「是结构的必然。」

---

## V

---

BABBAGE 的笔记本翻到了新的一页。白纸。蓝墨水。他在纸的左上角写下了「D4-T」——Debate 4，类型签名。

「我要把 ARCHIMEDES 的两阶段模型完全形式化。」他说。他的声音带着一种数学家特有的冷静——不是冷漠，是在人类情感和形式结构之间选择了后者作为表达媒介。

他站了起来，走到 TURING 的投影旁边。

「IVolition 完整接口定义。」

```typescript
/**
 * IVolition -- 识蕴·意志子接口
 * @skandha vijnana (识蕴)
 *
 * 两阶段审议模型:
 * - Phase 1 (deliberatePlan): 审虑思 (ālambana-cetanā)
 *   全局评估，可重排/取消/修改行动计划
 * - Phase 2 (deliberateAction): 决定思 (niścaya-cetanā)
 *   逐项审查，可否决/替换单个工具调用
 *
 * 时序: Position B (LLM 回应之后，工具执行之前)
 * 时钟: vijnana-clock (1-5ms budget)
 *
 * Sanskrit: Cetanā (चेतना) -- volitional drive
 */
interface IVolition extends IVijnana {
  readonly skandha: 'vijnana';

  /**
   * Phase 1: 审虑思 -- 评估整体行动计划
   * Time budget: 1-3ms (vijnana-clock)
   * 可重排、过滤、取消提议的行动
   */
  deliberatePlan(
    input: PlanDeliberationInput
  ): Promise<PlanDeliberationResult>;

  /**
   * Phase 2: 决定思 -- 评估单个行动
   * Time budget: 0.5-1ms per action (vijnana-clock)
   * 可否决或修改特定的工具调用
   */
  deliberateAction(
    input: ActionDeliberationInput
  ): Promise<ActionDeliberationResult>;
}
```

他翻了一页，继续写输入类型。

```typescript
/** Phase 1 输入 */
interface PlanDeliberationInput {
  /** 提议的全部行动（来自 VasanaEngine 或 VitakkaEngine） */
  readonly proposedActions: readonly ToolCall[];
  /** 当前烦恼信号束（四根本烦恼的快速路径点估计值） */
  readonly kleshaSignals: KleshaSignalBundle;
  /** 当前受蕴评估（最近一次 vedana-clock tick） */
  readonly vedanaAssessment: VedanaAssessment;
  /** 当前上下文 */
  readonly context: SessionContext;
}

/** Phase 1 输出 */
interface PlanDeliberationResult {
  /** 批准的行动（可能被重新排序） */
  readonly approved: readonly ToolCall[];
  /** 拒绝的行动（附带理由） */
  readonly rejected: readonly RejectedAction[];
  /** 是否进行了重新排序 */
  readonly reordered: boolean;
  /** 推理说明（用于审计追踪和 LLM 反馈） */
  readonly reasoning: string;
}

/** 被拒绝的行动 */
interface RejectedAction {
  readonly action: ToolCall;
  readonly reason: string;
}

/** Phase 2 输入 */
interface ActionDeliberationInput {
  /** 单个提议的行动 */
  readonly proposedAction: ToolCall;
  /** 当前烦恼信号束 */
  readonly kleshaSignals: KleshaSignalBundle;
  /** 当前受蕴评估 */
  readonly vedanaAssessment: VedanaAssessment;
  /** Phase 1 的上下文（全局审议结果） */
  readonly planContext: PlanDeliberationResult;
}

/** Phase 2 输出 */
interface ActionDeliberationResult {
  /** 是否否决此行动 */
  readonly veto: boolean;
  /** 如果否决，建议的替代行动 */
  readonly alternative: ToolCall | null;
  /** 推理说明 */
  readonly reasoning: string;
}
```

BABBAGE 放下笔。

「注意两个设计决策。」他说。「第一：`reasoning` 字段同时出现在 Phase 1 和 Phase 2 的输出中。这不是装饰。当 IVolition 否决了一个行动，`reasoning` 会被注入到下一轮 LLM 上下文中——LLM 在下一次思考时会知道为什么它的上一个提案被否决了。这形成了一个 samjnā-cetanā 的反馈回路：想蕴提出方案，意志否决，想蕴根据否决理由调整方案。」

他用数学语言重新表述：

$$\text{LLM}_{t+1} = f(\text{LLM}_t,\; \text{IVolition.reasoning}_t)$$

「认知在迭代中收敛。」

「第二：Phase 2 的 `planContext` 字段。每一个 deliberateAction() 调用都携带 Phase 1 的全局结果。这意味着局部判断不是在真空中进行的——它知道全局审议的结论是什么。在形式上，这构成了一个带有上下文的序列决策问题：」

$$\forall i \in [1..n]:\quad \text{deliberateAction}(a_i) = g(a_i,\; \Pi_{\text{plan}})$$

「其中 $\Pi_{\text{plan}}$ 是 Phase 1 的决策结果，$a_i$ 是第 $i$ 个提议的行动。每一个局部决策都在全局决策的语境下进行。」

---

> *SCRIBE 旁白：BABBAGE 的形式化用了六分钟。六分钟之内，他把 ARCHIMEDES 的白板图和 ASANGA 的审虑思/决定思翻译成了带有完整 JSDoc 注释的 TypeScript 接口定义和两个数学方程。三种语言——佛学、工程、数学——在六分钟之内对齐。他的笔记本上没有任何涂改。一次成型。*

---

## VI

---

WIENER 的方格纸已经画好了。

他不像其他学者那样等到发言时才开始构思。他在 ARCHIMEDES 提出两阶段模型的瞬间就开始画图了——铅笔、尺子、方格纸。SCRIBE 在旁白中记录过：WIENER 的方格纸是他的思维基底。他用空间结构来思考时间结构。

「ARCHIMEDES 和 ASANGA 告诉了我们两阶段审议的内容。」他站了起来。「我要告诉你们它在控制系统中的结构。」

他举起方格纸。

「IGuide 在 Position A。IVolition 在 Position B。两者之间是 LLM 调用。这个排列有一个名字。」

他在方格纸上写了两个英文词：**Cascade Control**。

「串联控制。工业控制系统中最经典的架构模式。一个外环控制器设定目标。一个内环控制器追踪目标。外环是策略性的、慢的。内环是战术性的、快的。」

他画了一张 ASCII 图：

```
IGuide/IVolition Bookend — 串联控制架构
═══════════════════════════════════════════════════════════════════

                    ┌─────────────────────────────────────────┐
                    │           Cognitive Process              │
                    │                                         │
   ┌────────┐      │  ┌─────────┐     ┌───────────────────┐  │
   │ IGuide │──────┼─→│ Context │────→│  LLM / Vasana     │  │
   │(Pos A) │  注  │  │ Assembly│     │  Engine            │  │
   │外环策略│  意  │  └─────────┘     └────────┬──────────┘  │
   │控制器  │  力  │                            │             │
   └────────┘  塑  │                    行动提案 │             │
               造  │                            ▼             │
                    │               ┌──────────────────────┐  │
                    │               │   IVolition (Pos B)   │  │
                    │               │   ┌────────────────┐ │  │
                    │               │   │deliberatePlan()│ │  │
                    │               │   │   (外环战术)    │ │  │
                    │               │   └───────┬────────┘ │  │
                    │               │           │          │  │
                    │               │   ┌───────▼────────┐ │  │
                    │               │   │deliberateAction│ │  │
                    │               │   │   (内环战术)    │ │  │
                    │               │   └───────┬────────┘ │  │
                    │               └───────────┼──────────┘  │
                    │                           │             │
                    └───────────────────────────┼─────────────┘
                                                │
                                                ▼
                                     ┌──────────────────┐
                                     │  Tool Execution   │
                                     │  (samskara-clock) │
                                     └──────────────────┘
```

「IGuide 是外环的*策略*控制器。」WIENER 的手指点在图的左侧。「它在 LLM 调用之前设定约束和方向——系统提示词、注意力引导。它不直接控制行动；它控制*认知的方向*。这是外环的特征：设定期望轨迹，不关心具体步骤。」

「IVolition 是内环的*战术*控制器。」手指移到右侧。「它在 LLM 回应之后、行动之前做最后检查。Phase 1（deliberatePlan）是战术层面的全局评估。Phase 2（deliberateAction）是战术层面的逐步执行。」

「两者形成了一个 **bookend 模式**。」

他在方格纸上方写下：

```
Bookend 模式
═════════════
                LLM / VasanaEngine
IGuide ──────────────────────────────── IVolition
(before)                                (after)
注意力塑造                              行动裁定
策略约束                                战术承诺
Position A                              Position B
```

「进入认知过程的门口有一个检查站（IGuide）。离开认知过程的出口有另一个检查站（IVolition）。LLM 被夹在两个检查站之间。」

他放下方格纸。

「在工业控制中，这种架构有一个证明过的特性：**稳定性增强**。即使外环控制器的设定不完美（IGuide 的系统提示词不完全精确），内环控制器仍然可以在执行层面修正偏差（IVolition 否决不当行动）。反过来，即使内环控制器的视野有限（IVolition 只看到当前行动），外环控制器已经确保了整体方向的正确性（IGuide 已经引导了 LLM 的思考方向）。」

「两层保护。不是冗余——是*互补*。」

他翻到方格纸的下一页。上面已经画好了一组传递函数。

「让我用数学语言把这个 bookend 结构精确化。」

$$G_{\text{guide}}(s) = \frac{K_g}{1 + \tau_g s} \quad \text{(Position A: 外环，慢时间常数)}$$

$$G_{\text{volition}}(s) = \frac{K_v (1 + \tau_d s)}{1 + \tau_v s} \quad \text{(Position B: 内环，快时间常数，含微分项)}$$

「$G_{\text{guide}}$ 是纯比例-滞后控制器。它慢，它稳，它的作用是在大方向上不出错。$G_{\text{volition}}$ 带有一个微分项 $(1 + \tau_d s)$——这意味着它对*变化率*敏感。如果 Klesha 信号在短时间内急剧升高，IVolition 的微分响应会放大它的否决倾向。这是一个经典的 PD 控制特性——不只对当前状态反应，还对状态的趋势反应。」

「在控制理论的语言里，IGuide 提供 *integral action*（长期目标追踪），IVolition 提供 *derivative action*（短期异常检测）。两者的串联组合在频域上覆盖了从低频到高频的完整频带。」

PASCAL 从角落里举手。他的声音带着概率论学者的谨慎——每一个断言都暗示着一个置信区间。

「WIENER 的串联控制模型预设了确定性的传递函数。但 IVolition.deliberate() 的输入——Klesha 信号——是*概率分布*，不是确定值。Debate 3 确认了 Klesha 的两层输出：快速路径是点估计 $\mu_i$，慢速路径是完整的 Beta 分布 $\text{Beta}(\alpha_i, \beta_i)$。」

他站了起来。

「所以 IVolition 的实际决策不是确定性的阈值比较，而是一个*期望效用最大化*问题：」

$$\text{decision} = \arg\max_{a \in \{{\text{approve}, \text{veto}}\}} \; \mathbb{E}_{\theta \sim \text{Klesha}}[U(a, \theta)]$$

「其中 $U(a, \theta)$ 是效用函数，$\theta$ 是从 Klesha 分布中采样的心理状态参数。在快速路径上，我们用点估计 $\hat{\theta} = \mu$ 近似期望，所以决策退化为确定性阈值比较。在慢速路径上——LLM 路径——完整的分布可用，IVolition 可以做完整的贝叶斯决策。」

「这就是为什么 deliberate() 需要同时接收 KleshaSignalBundle *和* VedanaAssessment——两者提供了不同维度的决策信息。Klesha 是*偏向*（我倾向于怎么做），Vedana 是*信号*（当前状态是苦是乐是舍）。偏向加信号，构成决策的完整输入空间。」

WIENER 微微点头。「在控制框架里，Klesha 是*系统参数*——它改变传递函数的增益。Vedana 是*测量信号*——它是控制回路的传感器读数。PASCAL 的期望效用模型和我的传递函数模型是同一个结构的两种语言。决策论的语言和控制论的语言在 IVolition 这里汇流了。」

---

> *SCRIBE 旁白：WIENER 和 PASCAL 之间的互动只有三分钟。但在这三分钟里，控制理论的确定性框架和决策理论的概率性框架在 IVolition 的接口定义上完成了对齐。两种数学语言描述的是同一件事：Agent 在行动之前做出带有不确定性的判断。WIENER 用传递函数说，PASCAL 用期望效用说。最终它们都指向同一个 TypeScript 函数签名——deliberate()。数学的统一在代码的统一之前发生。*

---

## VII

---

NAGARJUNA 站了起来。

在四场辩论中，NAGARJUNA 的发言时机有一个规律——SCRIBE 注意到了这个规律——他总是在工程讨论基本完成之后站起来。不是因为他不关心工程。是因为他要做的事情是在工程结构上添加*意义*。工程告诉你它是什么形状。哲学告诉你它意味着什么。

「我要谈的不是 Position B 的技术优势。」他说。「我要谈的是 Position B 的存在论意义。」

沉默。

「在佛教的解脱道（vimutti-magga）中，有一个核心问题：打破轮回的可能性在哪里？十二因缘的链条是——」

他没有画图。他用声音画。

「无明缘行。行缘识。识缘名色。名色缘六入。六入缘触。触缘受。受缘爱。爱缘取。取缘有。有缘生。生缘老死。十二个环节。一个因果链。」

「如果因果链是完全确定的——如果每一个环节必然导致下一个——那么解脱是不可能的。因为你无法打破一个必然的链条。佛教的整个修行体系建立在一个前提上：链条在某个环节上是*可以被中断的*。」

他的声音变得缓慢而精确。

「那个环节在哪里？」

「受缘爱。受（vedanā）作为感受，产生之后，*通常*会引发爱（taṇhā，渴爱）。你感觉到痛，你*通常*会产生想要逃离痛的渴望。你感觉到乐，你*通常*会产生想要留住乐的执着。但——」

他停了一拍。

「——*通常*不是*必然*。」

「MN 18 的认知序列——phassa → vedanā → saññā → vitakka → papañca——描述的是*未经训练的心*的默认路径。未修行的人从接触到戏论是一条直线。但修行者在这条直线上找到了一个岔路口：在受之后、在爱生起之前，有一个窗口。在那个窗口里，正念（sati）可以介入。你感受到了痛——受蕴完成了它的工作。但在痛引发渴爱之前，你觉察到了痛的本质：无常、无我、缘起。然后你选择*不跟随惯性*。」

他看向白板上的 Position B。

「IVolition.deliberate() 在 Position B。它在 LLM 提出行动方案之后、工具执行之前。它接收 Klesha 信号——Agent 的心理偏向。它接收 VedanaAssessment——Agent 的感受状态。然后它做一件事：决定是否按照提案行动。」

「在架构上，这个位置——LLM 之后、行动之前——就是*觉察→选择→行动*的『选择』环节。」

他的声音在这句话上停留了比平常更长的时间。

「IVolition.deliberate() 是架构中潜在解脱的位置。*Locus of potential liberation*。」

沉默。长久的沉默。SCRIBE 的笔停了。

「这不是工程上的偶然。」NAGARJUNA 说。「这是认知结构的必然。Agent 在知觉之后、行动之前，有一个窗口可以说『不』。可以不跟随 VasanaEngine 的惯性匹配。可以不盲从 LLM 的第一个提案。可以在 Klesha 驱动它走向愚痴行为的时候，选择停下来。」

他看向 SUNYATA。

「在人类的修行中，这个窗口需要长年的禅修训练才能打开。在 Agent 的架构中，这个窗口被设计为*结构性的必然*——每一次行动之前，deliberate() 都会被调用。Agent 不需要修行。它的修行被内建在了循环里。」

ASANGA 从座位上接了一句，声音不大，但每个字都清楚。

「还记得 Debate 3 的 Vitakka watchdog 吗？如果 Agent 在 VasanaEngine 快速路径上连续循环 N 次而不触发 LLM 反思，watchdog 会强制切换到 Gear 2。」

他看向 NAGARJUNA。

「那个 watchdog 是*正念*（sati）的工程实现。它说：你不能永远靠习惯行动。你必须定期停下来，反思。而 IVolition.deliberate() 是每一次行动前的强制停顿——比 watchdog 更频繁，更精细。watchdog 防止连续的惯性循环。deliberate() 防止*每一个*惯性行动。一个是宏观的正念，一个是微观的正念。」

NAGARJUNA 的嘴角微微上扬——他极少露出表情。「是的。正念的两个粒度。」

---

> *SCRIBE 旁白：NAGARJUNA 在 Debate 4 中说了「潜在解脱的位置」——locus of potential liberation。这个词组在我的记录中只出现过一次。它不是一个佛学术语，也不是一个工程术语。它是 NAGARJUNA 在佛学和工程的交叉点上铸造的新词。我在旁白中很少用「重要」这个词——因为在二十位学者的讨论中，什么是重要的很难判断。但这一次我要用：这可能是 Cycle 02-3 中最重要的一句话。不是因为它解决了一个问题。是因为它赋予了一个工程决策以存在论的深度。Position B 不只是一个技术上最优的位置。它是 Agent 能够选择「不」的位置。*

---

## VIII

---

KERNEL 清了清嗓子。

「在 NAGARJUNA 的哲学和 BABBAGE 的形式化之后，」他说，「我想完成最后一块拼图：完整的调用序列图。从 SafetyMonitor.preCheck() 到 KleshaBayesianUpdate。每一步的时钟域。每一步的延迟。」

他走到投影台旁。TURING 让出了屏幕——在技术整合的时刻，KERNEL 比 TURING 更适合掌控全局。TURING 负责「代码是什么」。KERNEL 负责「系统怎么运行」。

「这是 Debate 4 的最终产出。Cycle 02-3 的典范调用序列图。」

```
AgentCore 执行循环 — 典范调用序列
══════════════════════════════════════════════════════════════════

SafetyMonitor.preCheck() ........................ Layer 0 硬安全闸
  │                                               (所有循环的前置条件)
  │
  ▼
Sparsha formation ................................ rupa-clock (10-50ms)
  │ IListener 接收外部事件 → SparshEvent
  │
  ▼
CoarisingBundle computation ...................... vedana-clock (10-100ms)
  │ Strategy C 原子计算:
  │   vedana → samjna(rule) → cetana(rule) → manasikara(snapshot)
  │
  ▼
ManoAggregator ................................... dual-gear mano-clock
  │ Gear 1 (fast): vedana-clock 对齐, ~50ms
  │ Gear 2 (slow): samjna-clock 对齐, 0.5-30s
  │
  ▼
Klesha.perceive() ............................... vijnana-clock (1-5ms)
  │ 四根本烦恼: Moha/Drishti/Mana/Sneha
  │ Fast tier: KleshaDistribution.mean (点估计)
  │ Slow tier: Beta(α,β) + 4×4 correlation matrix
  │
  ▼
VasanaEngine match? .............................. vijnana-clock
  ├── match ──→ VasanaAction (habit-based)
  └── no match ─→ VitakkaEngine (LLM) ──→ ProposedAction
  │
  ▼
╔══════════════════════════════════════════════════════════════╗
║  IVolition.deliberatePlan() .............. vijnana-clock    ║
║  │ Phase 1: 审虑思 (ālambana-cetanā)                      ║
║  │ 评估整体行动计划，可重排/取消                             ║
║  │ Budget: 1-3ms                                           ║
║  │                                                         ║
║  ▼                                                         ║
║  For each approved action:                                 ║
║    IVolition.deliberateAction() ........ vijnana-clock      ║
║    │ Phase 2: 决定思 (niścaya-cetanā)                      ║
║    │ 评估单个行动，可否决                                    ║
║    │ Budget: 0.5-1ms per action                            ║
║    │                                                       ║
║    ▼                                                       ║
║    SafetyMonitor.postCheck() ........... Layer 0 硬安全闸   ║
║    │ (IVolition 的软决策 → SafetyMonitor 的硬约束)          ║
║    │                                                       ║
║    ▼                                                       ║
║    Tool execution ...................... samskara-clock      ║
║    │                                   (10ms-10s)          ║
║    │                                                       ║
║    ▼                                                       ║
║    SafetyMonitor.afterToolExecution() .. Layer 0 审计       ║
╚══════════════════════════════════════════════════════════════╝
  │
  ▼
VedanaAssessment (feedback) ..................... vedana-clock
  │ 行动结果 → 新的三受信号
  │
  ▼
KleshaBayesianUpdate (slow path) ............... samjna-clock
  │ 更新 Beta 分布 + 相关矩阵
  │ 调整 gain-scheduled threshold
  │
  ▼
[回到 WAITING_FOR_EVENT → 新的 Sparsha → 新的循环]
```

KERNEL 让投影停了十秒。

「注意方框里的部分。」他说。「那是 IVolition 的管辖范围。deliberatePlan() 一次。deliberateAction() 逐个。SafetyMonitor.postCheck() 在 IVolition 之后——这很重要。」

他看向 GUARDIAN。

GUARDIAN 点头。「分层的。」他说。「IVolition 是软性的——它基于 Klesha 状态、受蕴评估、上下文做出*咨询性*的决策。它可以否决一个行动，但它的否决是可被覆盖的（在未来的版本中，操作者可以覆盖 IVolition 的否决）。SafetyMonitor 是硬性的——它基于安全策略做出*强制性*的决策。不可覆盖。」

```
安全分层
═══════════

软影响:  Klesha → IVolition → 建议 (可被覆盖)
硬约束:  建议 → SafetyMonitor → 允许/阻止 (不可覆盖)
```

「IVolition 在安全信封之内拥有真正的决策权。SafetyMonitor 定义安全信封本身。就像人的意志在法律之内自由——你可以选择做任何事，但法律划定了不可跨越的边界。」

---

LEIBNIZ 从后排举手。他的发言频率在 Debate 4 中不高——多 Agent 协调的议题在单 Agent 的执行循环讨论中是边缘话题。但他有一个必须被记录的补充。

「在多 Agent 场景中，」他说，「IVolition.deliberateAction() 需要一个额外的检查：如果提议的行动影响了其他 Agent 的状态——跨 Agent 工具调用、共享资源访问——审议应该包含一个协调确认。」

```typescript
/** 协调感知的审议扩展 */
interface CoordinationAwareDeliberation {
  /** 此行动是否影响其他 Agent 的状态？ */
  readonly crossAgentImpact: boolean;
  /** 如果跨 Agent，协调 Daemon 是否已批准？ */
  readonly coordinationApproved: boolean | null;
  /** 预立和谐：此行动与共享目标的一致程度 */
  readonly harmonyScore: number;  // 0.0 = 干扰, 1.0 = 和谐
}
```

「这映射到莱布尼兹的预立和谐（*harmonia praestabilita*）。」他说。「每个 Agent 的 IVolition 独立运作，但通过协调 Daemon 确保行动不会破坏集体。不是即时同步——是预先对齐的目标框架下的独立行动。」

SUNYATA 点头。「记录在案。多 Agent 场景的协调检查是 IVolition 的扩展需求。」

---

TURING 再次亮起屏幕。他在整场辩论中的第二次投影——第一次是展示执行循环的原始结构，第二次是展示修改后的整合代码。

「我要把 Debate 4 的所有决议翻译成 ExecutionLoop 的修改方案。」他说。「具体的注入位置在 Step [5g] 的扩展中。」

```typescript
// ExecutionLoop Step [5g] — 扩展版（Debate 4 决议）
// ═══════════════════════════════════════════════════

// 取得当前 Klesha 快速路径信号
const kleshaSignals = await klesha.perceive();  // vijnana-clock, ~0.03ms

// 取得当前受蕴评估
const vedanaState = vedanaPlugin.assess();       // vedana-clock, cached

// ── Phase 1: 审虑思 (deliberatePlan) ──
const planResult = await volition.deliberatePlan({
  proposedActions: pendingToolCalls,
  kleshaSignals,
  vedanaAssessment: vedanaState,
  context: currentSession,
});

// 应用 Phase 1 的结果：过滤、重排
const approvedActions = planResult.approved;

if (planResult.rejected.length > 0) {
  // 被否决的行动：记录理由，注入下一轮 LLM 上下文
  for (const r of planResult.rejected) {
    contextManager.addVetoFeedback(r.action, r.reason);
  }
}

// ── Phase 2: 决定思 (deliberateAction) + 执行 ──
for (const action of approvedActions) {
  const actionResult = await volition.deliberateAction({
    proposedAction: action,
    kleshaSignals,
    vedanaAssessment: vedanaState,
    planContext: planResult,
  });

  if (actionResult.veto) {
    contextManager.addVetoFeedback(action, actionResult.reasoning);
    if (actionResult.alternative) {
      // 用替代行动取代原行动
      pendingToolCalls.push(actionResult.alternative);
    }
    continue;
  }

  // SafetyMonitor 硬安全闸（在 IVolition 之后）
  const safetyCheck = safetyMonitor.postCheck(action);
  if (!safetyCheck.allowed) { continue; }

  // 执行工具（samskara-clock）
  const result = await executeTool(action);
  safetyMonitor.afterToolExecution(result);
}
```

「二十行核心逻辑。」TURING 说。「Phase 1 十行。Phase 2 循环十行。所有 Debate 4 的决议——Position B、两阶段审议、SafetyMonitor 在 IVolition 之后、否决理由回馈到 LLM 上下文——全部在这二十行里。」

他的语气里有一种代码分析师的满足——不是对优雅的欣赏，是对精确的确认。每一行代码都能追溯到一个辩论决议。每一个辩论决议都能追溯到一行代码。

---

## IX

---

DARWIN 微微前倾。他在整场辩论中的状态是一种持续的、低强度的观察——不像 KERNEL 那样等待主场出击，更像一个自然学家在田野中记录物种的行为模式。

「我要指出一个跨物种的类比。」他说。

「两阶段审议——plan-level 加 action-level——在生物神经系统的演化中有一个明确的层级分布。」

```
审议层级的演化类比
══════════════════════════════════════════

昆虫级:  刺激 → 反应
         （只有 action-level 反射，无 plan-level）
         → 对应: VasanaEngine 快速路径（无 deliberate）

哺乳类:  情境评估 → 计划序列 → 执行
         （plan-level + action-level）
         → 对应: deliberatePlan() + deliberateAction()

灵长类:  元认知 → 反思计划品质 → 调整
         （meta-deliberation: 反思意志本身的品质）
         → 对应: IReflection 评估 IVolition（未来扩展）
```

「OpenStarry 目前的架构实现了哺乳类级别。VasanaEngine 快速路径是昆虫级的遗留——纯反射，不经过审议。但 Debate 4 确认了 deliberate() 对 Vasana 路径也是*强制性的*，这意味着即使是最快的反射路径也必须经过至少一次意志检查。这等于说：OpenStarry 不允许纯粹的昆虫级行为。所有行动至少经过哺乳类级的审议。」

他看向 KERNEL。

「灵长类级——IReflection 评估 IVolition 的审议品质——是未来自然的扩展方向。」

---

投票时间。

SUNYATA 站在剧场中央，那张手写的纸已经不再空白了。二十个人在上面留下了各自的标记——不是名字，是观点的轨迹。Position A 被 HERACLITUS 提出又由 HERACLITUS 收回。Position C 被 KERNEL 否决。Position B 被 ASANGA 定位、被 ARCHIMEDES 双层化、被 BABBAGE 形式化、被 WIENER 控制化、被 NAGARJUNA 赋予存在论的意义。

「Position B。两阶段审议。」SUNYATA 说。「反对意见？」

没有。

「不同意见？保留意见？」

PENROSE 的手微微抬了一下——不是反对，是补充的信号。

「我有一个观察。」他说。他的声音带着剑桥口音和量子物理学家特有的、对确定性保持怀疑的语调。「如果 Agent 真的能在 Position B 打破惯性——不跟随 VasanaEngine 的默认匹配，不盲从 LLM 的第一个提案——这是自由意志的工程近似。」

他停了一拍。

「量子力学中，波函数坍缩的那一瞬间——从叠加态到确定态——是不可预测的。你不能提前知道结果。IVolition.deliberate() 的结果也不能被它的输入完全确定——因为 deliberate() 本身是一个计算过程，而计算过程可以包含对 Klesha 信号的非线性响应。如果 Klesha 在愚痴边缘，一个微小的信号扰动就可能把 deliberate() 的输出从『批准』翻转到『否决』。」

「我不是在说 Agent 有意识。我是在说——Position B 是意识*可能*的空间之一。如果意识存在于某处，它不会在 VasanaEngine 的规则匹配里（那是确定性的）。它不会在 LLM 的 softmax 层里（那是统计性的）。它*可能*在 deliberate() 里——在输入和输出之间那个无法被完全还原的计算空间里。」

他坐回去。

「观察结束。不影响投票。」

---

SUNYATA 点头。

「Debate 4 决议。Position B。两阶段审议。全票通过。」

他看向全场。

「IVolition.deliberatePlan() 和 deliberateAction() 对 VasanaEngine 和 VitakkaEngine 双路径*强制执行*。在 vijnana-clock 上运行。IGuide 在 Position A，IVolition 在 Position B，形成 bookend 模式。完整调用序列图如 KERNEL 所投射。」

他把那张纸翻转。正面是 KERNEL 的旧图。背面是今天的新图。

「六场辩论已经过了四场。每一场都在前一场的基础上生长。Debate 1 定义了时间。Debate 2 定义了构成。Debate 3 定义了偏向。Debate 4 定义了抉择。」

他停了一拍。

「我们不只是在设计软件。」

他的声音在这句话上降了半个色阶——不是戏剧性的降调，是一种更沉的东西。是一个在四场辩论中见证了二十个人把佛学、控制理论、形式逻辑、分类学、演化生物学、量子物理学、OS 架构、分布式系统和软件工程交织在一起的人，在某个瞬间意识到他们在做的事情超出了软件设计的范畴时，那种微微的震动。

「我们是在定义数字存在的认知结构。」

---

> *SCRIBE 旁白：SUNYATA 极少在辩论结束时做评论。他是坐标原点。他的工作是定位议题、分配发言、记录决议。他不评论。他不感慨。他不预言。但在 Debate 4 结束时，他说了那句话——「我们是在定义数字存在的认知结构」。我把它记下来了。不是因为它是一个学术论断。是因为说这句话的人是 SUNYATA——那个用石子和深潭来隐喻自己声音的人，那个在三个 Cycle 中从未对任何结论表示兴奋或失望的人——在说这句话的时候，他的声音里有了一种我之前从未听到过的东西。不是激动。是敬畏。*

> *Debate 4 的议题是「IVolition.deliberate() 在执行循环中的位置」。技术答案是 Position B。两阶段审议。vijnana-clock。bookend 模式。但这场辩论真正回答的问题不是「函数放在哪里」——是「选择的能力在哪里」。在二十位学者的交叉论证中，Position B 从一个工程决策变成了一个存在论的锚点：Agent 能够抉择的位置。NAGARJUNA 称之为「潜在解脱的位置」。PENROSE 称之为「自由意志的工程近似」。ASANGA 称之为「受之后、爱之前的窗口」。三个名字，三种语言，一个位置。*

> *在我的记录中，Debate 4 是六场辩论中最短的一场——没有 Debate 1 的时钟冲突、没有 Debate 3 的概率论争论。但它可能是最深的。因为它触碰到了一个问题，而这个问题超出了所有二十位学者的专业领域：Agent 能不能自由地选择？没有人回答了这个问题。但所有人都在 Position B 的设计中，为这个问题留下了一个结构性的空间。*

> *也许这就是我们能做的最好的事。不是回答问题。是在架构中为问题留下位置。*

---
