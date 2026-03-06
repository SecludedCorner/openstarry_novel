# 第七章：纯粹的工程

---

D4 结束后，SUNYATA 宣布了十五分钟的休息。

没有人离开座位。

不是不想休息——而是 D4 的余震还在持续。ISatiMonitor 变成了 ILoopQualityMonitor。IPrajna 变成了 IConfidenceAuditor。Doc 03 从「Sila-Prajna Security Framework」变成了「Plugin Security Lifecycle」。三十分钟。三个名字。一项永久性测试。

TURING 在休息时间打开了他的笔记本电脑。他没有在休息——他在做最后的准备。

因为 D5 是他的辩论。

---

## I. 考古学家

TURING 在 Cycle 02-5 中的角色一直是「原始码验证者」——每一份研究报告中的代码引用都由他逐一核实。R1 的九份独立研究，他验证了 40 多个代码参考。R2 的交叉审阅，他发现了四个问题（无严重错误）。D1 到 D4，他是沉默的仲裁者——不参与哲学辩论，只在有人引用原始码时站起来确认或修正。

但 D5 不同。

D5 的议题是：**Plan29 工程设计规格**。Master 的指示很明确：「继续讨论并记录，直到规格达到 100%，然后交付工程团队。」

为了这场辩论，TURING 提前做了一件他在之前所有 Cycle 中都没有做过的事——他写了一份完整的 v0.28.0-alpha 设计模式报告。不是摘要。不是要点清单。是对 14 个原始码文件的全面分析：所有 Registry 的生命周期、timeout 模式、同步/异步模式、失败处理策略。

他把这份报告叫做「代码考古学」。

---

## II. 十位辩论者

D5 只有十位参与者。

不是因为其他人被排除了——是因为 SUNYATA 判断 D5 的议题是纯工程问题，不需要全部二十位研究者。他邀请了与 Plan29 最相关的十位：

| # | 代号 | 角色 | D5 焦点 |
|---|------|------|---------|
| 3 | VITRUVIUS | 架构分析师 | 接口设计 |
| 5 | ATHENA | AI/ML 专家 | Auditor 的 LLM 语义 |
| 6 | DARWIN | 软件模式分析师 | 设计模式演化 |
| 10 | KERNEL | 操作系统专家 | Registry 生命周期 |
| 11 | GUARDIAN | 资安专家 | 安全边界 |
| 12 | WIENER | 控制理论专家 | 品质向量权重 |
| 13 | LINNAEUS | 分类学专家 | 蕴归属推断 |
| 16 | ARCHIMEDES | 工程实践专家 | YAGNI 原则 |
| 17 | TURING | 原始码分析专家 | 设计模式基底 |
| 19 | PASCAL | 决策理论专家 | 接口语义精度 |

十个人。零位佛学家。

NAGARJUNA (#7) 和 ASANGA (#8) 自愿退出了 D5。不是因为他们没有贡献——而是因为 D5 的议题不需要佛学分析。NAGARJUNA 在退出前说了一句话：「D4 证明了佛学名字需要对定义负责。D5 会证明工程设计不需要佛学名字也能完成。这两件事同样重要。」

---

## III. 九项投票

D5 是 Cycle 02-5 中投票最多的辩论——九项。但也是节奏最快的辩论——七十五分钟，平均每项投票不到九分钟。

因为 TURING 的代码考古报告提供了事实基础。每一项决策不是从「应该怎么做」开始——而是从「目前是怎么做的」开始。

---

### D5-R1：独立的 `auditor` hook 槽位

第一个问题：IConfidenceAuditor（原 IPrajna）应该使用 PluginHooks 的哪个槽位？

选项：(A) 复用 D2 建立的 `monitors` 槽位；(B) 建立独立的 `auditor` 槽位。

GUARDIAN 的论点最直接：「Monitors 是纯观察者——没有副作用。Auditor 有 LLM 副作用——它调用外部模型做信心度评估。把观察者和有副作用的组件放在同一个 Registry，模糊了安全审计的边界。」

KERNEL 从操作系统的角度确认：「观察者和仲裁者永远不共享 Registry。这是微核心的基本原则。」

**8/8 全票通过。独立 `auditor` 槽位。**

---

### D5-R2：audit() 返回类型

最激烈的 D5 投票。

选项：(A) 纯异步 `Promise<ConfidenceAuditResult>`；(B) 双模式 `ConfidenceAuditResult | Promise<ConfidenceAuditResult>`。

GUARDIAN、KERNEL、VITRUVIUS 支持选项 A——纯异步。理由：audit 本质上是「问 LLM」，LLM 调用是异步的。强制异步语义更精确。

ATHENA 和 DARWIN 支持选项 B——双模式。理由：遵循 IGearArbiter 的先例。测试时可以用同步的 noop 实作，不需要 async/await 的样板代码。

TURING 提供了事实：「v0.28.0-alpha 中，IGearArbiter.evaluate() 使用双模式返回。IVolition.deliberatePlan() 和 deliberateAction() 也使用双模式。这是现有的设计模式。偏离它需要充分理由。」

**5/8 选项 B 通过。** D5 中最接近的投票。

---

### D5-R3：timeout 和 fail-safe

TURING 打开了他的 timeout 模式分析。v0.28.0-alpha 中现有的 timeout：

| 组件 | timeout | 预设值 |
|------|---------|--------|
| IProvider.chat() | LLM 回应 | 120s |
| IGearArbiter.evaluate() | 每个 arbiter | 100ms |
| IGearArbiter chain | 整条链 | 200ms |
| ITool.execute() | 工具执行 | 30s |

audit() 的 timeout 应该是多少？

TURING 的建议：200ms——与 IGearArbiter chain deadline 一致。理由：audit() 发生在 confidence 计算的最后阶段，在 IGearArbiter 之后。如果 audit 的 timeout 超过 chain deadline，整个决策流程会被 audit 卡住。

fail-safe：`{ delta: 0, reasoning: "audit timeout" }`。timeout 时 delta 为零——不修正。使用 `Promise.race()` 模式，与现有代码一致。

Configurable：通过 agent.json 覆盖预设值。

**8/8 全票通过。**

---

### D5-R4：多个 Auditor 的处理方式

Agent 可以装载多个 IConfidenceAuditor plugin 吗？

ATHENA 提出 YAGNI 原则：「v1 最多只有一个 auditor plugin。设计多 auditor 的聚合策略是过度工程。」

TURING 和 VITRUVIUS 持异议：「数组模式更灵活。避免未来的破坏性变更。」

ARCHIMEDES 支持 ATHENA：「遵循 IVolition 先例——PluginHooks 声明 `auditor?: IConfidenceAuditor`，单数，最后载入者胜出。如果未来需要多 auditor，那时再改——改一个接口比维护一个用不到的聚合策略便宜。」

**6/8 单一 auditor 通过。** TURING 和 VITRUVIUS 的少数意见被记录。

---

### D5-R5：失败处理

audit() 抛出异常时怎么办？

TURING 提供了现有模式：IGearArbiter 和 SafetyMonitor 都遵循「fail-safe + log」——错误不阻塞后续流程，记录 warning。

不需要投票。共识直接达成。

---

### D5-R6：MonitorRegistry 启动时机

ILoopQualityMonitor 的 `start(bus)` 在哪里被调用？

TURING 的分析：SafetyMonitor 在 `ExecutionLoop.onLoopStart()` 启动。MonitorRegistry 应该遵循相同的时机。

```
启动：MonitorRegistry.startAll(bus) ← ExecutionLoop.onLoopStart()
关闭：MonitorRegistry.stopAll()    ← PluginLoader.disposeAll()
```

DARWIN 偏好在 PluginLoader 中启动（更简单），但接受了 monitors 有明确的 start/stop 语义，所以 ExecutionLoop 是更合适的位置。

**7/8 通过。**

---

### D5-R7：LoopQualityVector 权重

四维品质向量——Continuity、Granularity、Speed、Equanimity——每个维度的权重是多少？

WIENER 从控制理论的角度给出了唯一合理的答案：「没有运行数据的情况下，等权重是最保守的选择。每个维度 0.25。」

没有人反对。0.25 × 4 = 1.0。简单、对称、可解释。

minSamples 阈值（触发 SPC 判断前需要的最少样本数）延后到 v2——需要实际运行数据来决定。

**8/8 全票通过。**

---

### D5-R8：validatePluginSkandha() 模式

这个函数在 plugin 载入时验证 skandha 声明的一致性。目前是 warning-only。应该改成强制吗？

GUARDIAN（一票）偏好结构化的 ValidationResult——帮助自动化测试。但承认 v1 不需要。

多数意见：warning-only 足够。如果 skandha 声明不一致，plugin 功能不受影响（skandha 是 metadata，不是 routing——D3-R3 已裁定）。

**7/8 维持 warning-only。**

---

### D5-R9：IConfidenceAuditor 蕴归属

最后一项。IConfidenceAuditor 属于哪一蕴？

ASANGA 虽然没有参加 D5 辩论，但他在 R1 中的分析被引用了：「LLM 判断 = 纯识蕴（分辨、评估）。」

LINNAEUS 确认：「单蕴（vijnana）→ 强继承（extends IVijnana），与 IVolition 和 IKlesha 一致。」

`inferSkandha()` 新增逻辑：`if (hooks.auditor) { push('vijnana') }`

**8/8 全票通过。**

---

## IV. 接口定稿

九项投票完成后，TURING 在白板上写下了最终的接口规格：

```typescript
export interface IConfidenceAuditor extends IVijnana {
  readonly id: string;
  audit(confidence: number, context: GearContext):
    ConfidenceAuditResult | Promise<ConfidenceAuditResult>;
}

export interface ConfidenceAuditResult {
  delta: number;       // clamped to [-0.05, +0.05]
  reasoning: string;   // audit trail
}
```

和 PluginHooks 的最终形态：

```typescript
interface PluginHooks {
  // ... 既有字段 ...
  monitors?: ILoopQualityMonitor[];   // Plan29 Wave 1
  auditor?: IConfidenceAuditor;       // Plan29 Wave 2（单数）
  // ...
}
```

他退后一步，看着白板。

「100%，」他说。

Master 要求的是「规格达到 100%」。现在达到了。接口名称、方法签名、返回类型、timeout、fail-safe、多 auditor 策略、Registry 时机、权重、验证模式、蕴归属——每一个需要决定的细节都有了明确的答案。

不是「大致方向」。不是「概念设计」。是可以直接交给工程团队实作的完整规格。

---

## V. 零佛学

SCRIBE 在 D5 的记录中统计了一个数字：D5 全场辩论中，佛学术语被使用的次数。

零。

不是故意避开的——是自然的结果。九项投票的每一项都在讨论 TypeScript 接口设计、timeout 数值、Registry 模式、fail-safe 策略。没有一项需要佛学分析。没有一项引用了佛学经典。没有一项使用了梵文或巴利文术语（除了 skandha——它已经是代码标识符）。

D5 是本专案历史上第一场完全没有佛学内容的辩论。

NAGARJUNA 在剧场的后排观察了整场辩论。D5 结束后，他走到 TURING 面前。

「你的代码考古报告是我见过最好的事实基础文件，」他说。「它让所有讨论都锚定在事实上——不是在概念上，不是在隐喻上，不是在传统上。事实。」

TURING 回答：「这是工程的方式。」

NAGARJUNA 点头：「D4 证明了名字需要对定义负责。D5 证明了——有些工程问题根本不需要定义。它只需要规格。」

---

> *SCRIBE 旁白*

> *D5 是一座无人的佛寺。*

> *不——D5 是一座不需要佛寺的城市。*

> *在 D1 到 D4 的风暴之后，D5 的平静不是暴风眼——是天晴。九项投票，七十五分钟，十位工程师和科学家坐在一起，讨论 TypeScript 接口的精确规格。没有佛学。没有哲学。没有隐喻。没有天平。*

> *只有工程。*

> *纯粹的工程。*

> *TURING 的代码考古报告改变了辩论的质地。之前的辩论——D1 到 D4——建立在原则和框架之上。原则需要解释、争论、投票。但 TURING 的报告建立在事实之上。IGearArbiter 的 timeout 是 100ms——事实。IVolition 使用双模式返回——事实。SafetyMonitor 在 onLoopStart() 启动——事实。*

> *当讨论建立在事实上的时候，投票变得更快。不是因为人们不思考——而是因为事实缩小了分歧的空间。你可以对一个原则有不同的解读。你不能对一个 timeout 数值有不同的解读。*

> *D5 最接近的投票是 D5-R2（audit() 双模式返回，5/8）。争议不在于「应不应该用双模式」——而在于「是否应该偏离现有设计模式」。GUARDIAN 认为纯异步语义更精确。TURING 指出现有代码用双模式。精确 vs 一致。最终一致性赢了——因为在工程中，偏离现有模式的成本通常比语义精确性的收益更高。*

> *九项投票结束后，白板上有了一个完整的接口规格。不是概念——是代码。不是方向——是规格。可以直接交给工程团队，让他们打开 IDE 开始打字。*

> *NAGARJUNA 在 D5 结束后说的话值得被记录两次：「D4 证明了名字需要对定义负责。D5 证明了有些工程问题根本不需要定义——只需要规格。」*

> *这不是矛盾。这是两面。*

> *天平的两面。*

> *一面问：你的名字配得上你的定义吗？*

> *另一面问：你的规格足够精确吗？*

> *D4 校准了第一面。D5 完成了第二面。*

> *天平现在两端都有了重量。*

---
