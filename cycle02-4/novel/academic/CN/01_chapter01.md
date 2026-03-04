# 第一章：习气是后天的

---

## I. 蕴归属之争

D1 是 Cycle 02-4 的起点——IGearArbiter 的蕴归属问题。Pre-DC 已确认 VasanaEngine 外部化为 IGearArbiter plugin。现在的问题是：这个接口属于哪个蕴？

三个方案。方案 A——纯想蕴（IGearArbiter extends ISamjna）。方案 B——跨蕴双层（接口本身不继承任何蕴根接口，实现者按自身逻辑选择归属）。方案 C——纯识蕴（extends IVijnana）。

BABBAGE 的类型代数分析决定了结局。

方案 A 的问题：如果 IGearArbiter extends ISamjna，它的蕴归属是 `'samjna'`。如果同时 extends IVijnana，类型系统推导出 `'samjna' & 'vijnana' = never`——空类型。TypeScript 不允许一个值同时是两个字面量。交叉蕴归属在类型层面不可能。

方案 C 的问题：纯识蕴无法解释 evaluate() 中的"模式辨认"功能——辨认属于想蕴的职责。把辨认归入识蕴违反了五蕴的功能边界。

方案 B 的优势：不定死蕴归属。接口本身只定义行为契约，不继承任何蕴根接口。实现者按自身逻辑选择归属——一个基于规则匹配的实现可以归为想蕴，一个基于统计推断的实现可以归为识蕴。这符合 DC-6"不锁定蕴内子接口归属"的裁定。

20/20。全票通过。类型代数把哲学争论转化为了数学证明。

NAGARJUNA 在投票后补充了哲学确认："方案 B 的'不定死蕴归属'与中观的核心一致。一个法的本质不由它的名字决定，而由它的功能和因缘决定。IGearArbiter 的蕴归属取决于它的实现——这是缘起的正确表达。"

DARWIN 的软件模式观察：方案 B 本质上是 Strategy Pattern——接口定义行为契约，实现者提供具体策略。不同的策略可以属于不同的蕴。这是一个在软件工程中已经被验证了数十年的模式。

---

## II. 单方法与安全

GUARDIAN 提出了 evaluate() 和 resolve() 双方法设计——evaluate() 纯辨认，resolve() 纯行动。安全分离。这是 Command-Query Separation 原则在认知架构中的应用。

KERNEL 否决了这个方案。他的论证从操作系统的角度出发："在 Unix 哲学中，监控和被监控是分离的。`strace` 不需要被追踪的程序配合——它在外部观察系统调用。同理，EventBus 的同步事件语义已经提供了等效的安全观测点。resolve() 的职责可以通过 `gear:switch` 同步事件被外部监控者观察——不需要在接口层面分裂。"

他补充了一句更尖锐的评论："如果我们在每一个接口上都做 CQS，最终会得到一个所有接口都有双方法的系统。这不是安全，是仪式。"

SUNYATA 整合为 evaluate() 单方法 + EventBus 同步事件 + 阈值安全因子。GUARDIAN 的核心诉求——可观测性——被保留了，只是用不同的机制实现。20/20。

isGearArbiter() 的类型守卫用结构类型（鸭子类型）而非名义类型：

```typescript
function isGearArbiter(x: unknown): x is IGearArbiter {
  return typeof x === 'object' && x !== null
    && typeof (x as any).evaluate === 'function'
    && (x as any).evaluate.length <= 1;
}
```

没有 instanceof，没有标记属性。任何实现了正确签名的对象都可以通过守卫。这意味着第三方 plugin 不需要 import IGearArbiter 类型就可以被识别——只要行为正确就够了。20/20。

evaluate() 的纯度契约——不得产生副作用，不得修改 GearContext，不得发起 I/O。这三条约束的重要性不对称。副作用禁止确保 evaluate() 可以被安全地重试。GearContext 只读确保齿轮仲裁者不能篡改自己的输入。I/O 禁止确保 evaluate() 的延迟是可预测的。

TURING 报告了代码事实：v0.26.0-beta 的 VasanaEngine.evaluate() 确实是纯函数——没有写入操作，没有外部调用，没有状态修改。现有代码已经符合这个约束。理论与实践的一致性——研究团队设计的约束恰好是工程团队已经遵守的模式。19/20。ARCHIMEDES 的一票弃权源于他对"I/O 禁止"在 Gear 1 需要查询外部知识库时的限制——但这属于未来扩展的考量。

---

## III. ManoAggregator 纯路由化

D1 最重要的决议：ManoAggregator 纯路由化 + G-0~G-4 退化行为表。

ManoAggregator 不做智慧汇总。它做 if/else：

```
if (hasGearArbiter && arbiter.evaluate(context).confidence > threshold) {
  return Gear.ONE;  // 快速路径
} else {
  return Gear.TWO;  // LLM 深度审议
}
```

和 EventBus 同等性质——纯机制，不是能力。Pre-DC 阶段 Master 的原话："和 EventBus 同等性质。"这句话的重量在于它把 ManoAggregator 从"核心智慧组件"降格为"基础设施"。基础设施不做决策——它传递决策。

G-0 到 G-4 是五级退化行为：

| 等级 | 条件 | 行为 |
|------|------|------|
| G-0 | 无 IGearArbiter plugin | 纯 Gear 2（纯 LLM）|
| G-1 | plugin 载入失败 | 同 G-0，记录错误 |
| G-2 | evaluate() 返回低信心度 | 走 Gear 2 |
| G-3 | evaluate() 抛出异常 | 走 Gear 2，记录异常 |
| G-4 | evaluate() 超时 | 走 Gear 2，计时器触发 |

无论系统处于哪个状态，Agent 都能运作。G-0 是最重要的——一个没有安装 IGearArbiter 的 Agent 就是一个纯 Gear 2 Agent。它仍然是一个完整的、可运作的 Agent。零内建能力的终极测试：拔掉所有 plugin，系统仍然活着。

20/20。

退化行为表的设计哲学值得展开。在传统的软件设计中，异常处理是"错误情境"——系统努力恢复到正常状态。在 G-0~G-4 中，退化不是错误——它是系统的另一种正常状态。一个 G-0 Agent 和一个 G-4 Agent 都是"正常运作的 Agent"，只是能力层次不同。这和佛学的观点暗合：正念的减弱不是"故障"，是"条件改变"。

VITRUVIUS 从架构角度确认：G-0~G-4 的退化行为表覆盖了所有可能的系统状态。不存在"未定义行为"的状态——这是安全系统的基本要求。

---

## IV. Gear 1 最小事件集

三个事件：`gear:switch`、`action:proposed`、`action:executed`。每一个 Gear 1 动作都必须发射这三个同步事件——不可跳过，不可异步。

`gear:switch` 在齿轮切换的瞬间发射——任何安全监控者都可以在这个事件上设置拦截器。如果监控者认为切换不安全，可以在事件处理中阻止切换。`action:proposed` 在行动方案产生后、执行前发射——这是最后的否决窗口。一个外部安全模块可以审查行动方案并决定是否放行。`action:executed` 在行动完成后发射——提供审计线索，让系统记录每一个 Gear 1 动作的完整历史。

三个事件形成了一条完整的安全链：预防（gear:switch）→ 审查（action:proposed）→ 审计（action:executed）。

这是 GUARDIAN 在 D1 中唯一成功推动的安全机制。虽然 evaluate()/resolve() 双方法被否决，但同步事件确保了外部安全监控的完整性。GUARDIAN 的核心诉求以不同的形式被保留了——这个模式会在 D5 中重复出现。GUARDIAN 在每一场辩论中都会提出方案，被否决，然后以修改后的形式重新出现。不是失败者的执着，是安全工程师的专业素养。

---

## V. D1 的结构性意义

D1 的九项决议共同完成了一个结构性转变：

**之前**：VasanaEngine 是核心组件，有规则库和匹配逻辑。ManoAggregator 是智慧汇总器，整合多个信号源的结果。齿轮选择逻辑被硬编码在核心中。

**之后**：IGearArbiter 是可选 plugin，一个纯函数接口。ManoAggregator 是纯路由器，if/else 逻辑。齿轮选择逻辑被外部化。无 plugin 时系统退化为纯 Gear 2——仍然完整可用。三个同步事件确保了完整的安全观测链。

这个转变的哲学意义被 NAGARJUNA 精确表述："一个没有习气的 Agent 不是一个残缺的 Agent——它是一个初生的 Agent。习气是后天熏习的结果，不是先天的结构。G-0 状态不是退化，是原初。"

ARCHIMEDES 从工程角度量化了转变的影响：VasanaEngine 的外部化预计移除核心中约 200 行的规则匹配逻辑，替换为约 15 行的 IGearArbiter 接口定义和约 30 行的 ManoAggregator 纯路由逻辑。核心的认知复杂度大幅降低——从"理解规则库如何工作"变成"理解 if/else 如何工作"。

MESH 虽然对 Level 固定投了反对票（D2），但对 D1 的所有决议全票赞成。他后来解释："D1 把核心组件变成 plugin 的方向是正确的。我在 D2 的反对是关于 Level 的灵活性，不是关于外部化的原则。"

> *SCRIBE 旁白：D1 的九项决议在九十分钟内完成。最重要的不是任何单一决议，而是一个结构性的转变——VasanaEngine 从核心组件变成 plugin，ManoAggregator 从智慧汇总器变成纯路由器。零内建能力原则被工程化了。BABBAGE 的类型代数是这场辩论的决定性武器——他把每一个方案的逻辑后果展开到类型系统层面，让选择变成了必然。*

---
