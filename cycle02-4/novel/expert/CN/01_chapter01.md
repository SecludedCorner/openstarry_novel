# 第一章：习气是后天的

---

## I. 问题的形状

D1 的议题被 SUNYATA 写在白板上的时候，圆形剧场里出现了一种特殊的安静。不是 D3 那种"大家都同意"的安静（那要等到后天），也不是 D5 那种"暴风雨前"的安静（那要等到第五天）。这是一种"啊，原来如此"的安静。

白板上写着：

```
IGearArbiter — 它属于哪个蕴？
```

七个字。一个问号。但问号的重量不在字面上。

Pre-DC 已经确认：VasanaEngine 从核心外部化为 plugin。外部化本身不是问题——问题在外部化之后。一个 plugin 必须属于某个蕴。Plugin Manifest 有一个 `skandha` 字段。这个字段填什么？

ATHENA 第一个开口。她的声音带着工程师那种"我已经想过这个问题好几天了"的沉稳：

"IGearArbiter 做两件事。第一，快速辨认——输入一个请求，匹配规则库，判断是否有已知模式。这是想蕴（samjna）的功能，取相辨识。第二，信心度判断——这个匹配有多可靠？值不值得跳过 LLM？这是识蕴（vijnana）的功能，分别了别。"

她停顿了一下。

"它跨蕴。"

---

三个方案被摆在桌面上。BABBAGE 用他那种精确到令人不安的方式把它们排成了一个表格：

| 方案 | 接口继承 | Manifest 标注 | 类型安全 |
|------|---------|-------------|---------|
| (A) | extends ISamjna | `skandha: 'samjna'` | 强——但丢失 vijnana 语义 |
| (B) | 独立接口 | `skandha: ['samjna', 'vijnana']` | 中——Manifest 层多值 |
| (C) | extends IVijnanaMechanism（新中间层）| `skandha: 'vijnana'` | 强——但增加类型复杂度 |

BABBAGE 推了推眼镜。他不需要推——镜框是合适的——但这个动作本身就是一种标点符号，意味着"我接下来要说的话会很精确"。

"方案 (A) 有一个类型代数问题。"

他在白板上写下了一行：

```
ISamjna.skandha = 'samjna'
IVijnana.skandha = 'vijnana'
'samjna' & 'vijnana' = never
```

"如果 IGearArbiter extends ISamjna，它的 skandha 字段在类型层面被锁死为 'samjna'。你无法在 Interface 层同时表达它属于两个蕴。判别式联合类型不允许这种交叉。"

DARWIN 歪了歪头。"用简单的话说？"

"用简单的话说：TypeScript 的类型系统不允许一个东西同时是猫又是狗。你可以在 Manifest 里宣称它是猫狗，但 Interface 层的编译器会拒绝。"

方案 (A) 在 BABBAGE 说完的三秒后就被所有人从心理候选名单上划掉了。

---

方案 (C) 的问题是 LINNAEUS 发现的。

"DC-6，"他说，翻开他那本分类学笔记。"Master 的裁定：'不锁定蕴内子接口的归属。'IVijnanaMechanism 作为 IVijnana 的子接口——"

"——锁定了。"KERNEL 接过话。"一旦你建立 IVijnanaMechanism，未来任何跨蕴组件都需要再建一个中间层。IVijnanaCognition。ISamjnaPerception。类型膨胀是指数级的。"

方案 (C) 没有被明确投票否决，但它像一根被放在不对的位置的齿轮一样，所有人都看出它不合适。

---

方案 (B) 的转折点来自 ASANGA。

他一直沉默着。在 BABBAGE 的类型代数和 LINNAEUS 的分类学之后，他开口了。他的声音像一根在黑暗中被点燃的线香——安静，但方向明确。

"五遍行俱生。"

所有人转向他。

"《大毗婆沙论》和《成唯识论》都说：触、作意、受、想、思——五个心所——在每一次认知事件中**同时起**。不是先辨认后判断。是辨认和判断在触的那一刹那俱生。"

他看了看 ATHENA。

"你说 IGearArbiter 做两件事——想蕴的取相和识蕴的了别。在佛学里，这两件事不是先后的。它们是**同时的**。同所依、同所缘、同行相。一个 `evaluate()` 方法，不是因为工程简化，而是因为这就是心识运作的方式。"

圆形剧场里安静了五秒。

PASCAL 在他的笔记本上快速写下了什么。NAGARJUNA 微微点头。BABBAGE 的嘴角有一个几乎看不见的上扬——形式化论证和佛学经典在同一个结论上汇聚，这对他来说是一种罕见的美。

SUNYATA："方案 (B)。独立接口，Manifest 多值。有反对意见吗？"

二十张面孔。零只举起的手。

**D1-1A：方案 (B) 跨蕴双层策略——20/20。**

---

## II. evaluate() 的战争与和平

如果 D1-1A 是安静的河流，那么接下来的 evaluate() 接口设计辩论就是这条河流上的急流。

GUARDIAN 站了起来。他很少站起来——在 Cycle 02-3 的六场辩论中，他大部分时间坐着，用红笔在备忘录上画底线。但今天他站了起来，这意味着他接下来要说的话不是建议，而是主张。

"单一的 evaluate() 方法是不够的。"

他走到白板前，画了一条时间线：

```
   请求进入 → evaluate() → 齿轮切换 → 工具执行
                  ↑
            所有逻辑在这里
            辨认 + 判断 + 决策
            一个函数做所有事情

   如果这个函数出错——整个链出错
   如果这个函数被注入——整个链被劫持
```

"我提议拆分为两步：`recognize()` 和 `resolve()`。"

```
   请求进入 → recognize() → [验证点] → resolve() → 齿轮切换
                              ↑
                        SafetyMonitor 可介入
                        可以审查辨认结果
                        再决定是否继续
```

"在 recognize 和 resolve 之间插入一个验证点。SafetyMonitor 可以检查辨认结果是否合理，然后再决定是否允许 resolve 执行。"

ATHENA 几乎是立刻回应的："多余。"

GUARDIAN 的眼睛微微收窄。"多余？"

"用 EventBus 同步事件可以达到完全相同的效果。evaluate() 执行完毕的同时，emit 一个 `gear:arbiter_evaluated` 事件。SafetyMonitor 订阅这个事件。同步处理。"

"同步？如果 SafetyMonitor 的处理是异步的呢？如果它需要查询外部服务——"

KERNEL 举手。不是举手表示发言——是举手表示"我有一个技术事实"。

"Node.js 的 EventEmitter.emit() 是同步的。"

整个剧场转向 KERNEL。

"当你调用 emitter.emit('event', data) 时，所有注册的 listener 会在当前 call stack 中**依序同步执行**。不是 nextTick，不是 microtask，不是 macrotask。是同步的。emit() 返回的时候，所有 listener 都已经跑完了。"

GUARDIAN："你确定？"

KERNEL 看了他一眼。那个眼神的意思是："我写过 Node.js 的事件系统。"

"我确定。在 Node.js 模型中，EventBus 同步事件和你提议的 recognize/resolve 分离在安全保证上是等价的。差别只在 API 复杂度。"

---

GUARDIAN 没有立刻让步。一个好的安全倡导者不会因为一个技术事实就让步——他会寻找那个事实没有覆盖到的边缘。

"假设未来的运行环境不是 Node.js。假设有人用 Worker Thread 实现了一个异步的 EventBus——"

KERNEL："那是实现错误，不是设计缺陷。同步事件语义是契约层面的保证，不依赖特定运行时。如果有人实现了异步 EventBus，那他违反了契约。"

WIENER 从他的座位上插了一句："我可以提供一个妥协方案。"

所有人看向他。WIENER 很少提"妥协"——他通常提"数学证明"。但偶尔，控制理论家也需要当外交官。

"三道外部安全机制。第一：EventBus 同步事件——`gear:arbiter_evaluated`，不可延迟，不可跳过。第二：阈值安全因子——θ_adjusted = θ_base × (1 + k_safety)，安全裕度内建在数学里。第三：最小事件集——gear:switch、action:proposed、action:executed——每一次齿轮操作都有完整的事件轨迹，外部监控可以独立验证。"

他看了看 GUARDIAN。

"你的核心诉求是：不应该有一个函数做所有事情而没有外部检查。三道机制提供了三个独立的外部检查点。如果三道都失效，那已经不是设计问题，而是拜占庭错误。"

GUARDIAN 沉默了三十秒。在安全领域，三十秒的沉默意味着正在评估攻击面。

"最小事件集。"他最终说。"gear:switch 要加上 gear:arbiter_evaluated。我要知道仲裁者的判断结果，不只是最终的齿轮切换。"

WIENER："同意。"

ATHENA："同意。"

**D1-R1：evaluate() 单方法 + EventBus 同步事件 + 阈值安全因子——20/20。**

GUARDIAN 点了点头。他的红笔在备忘录上画了一条线——不是底线（那是"问题"），是删除线（那是"已解决"）。

---

## III. 类型守卫：evaluate.length ≤ 1

TURING 在 D1 的第三段辩论中只说了十二个字，但这十二个字改变了类型守卫的设计。

讨论的焦点是 `isGearArbiter()`——如何在运行时判断一个 plugin 是否实现了 IGearArbiter 接口。BABBAGE 提出了两个方案：

方案 A：Symbol brand（符号烙印）——在接口上附加一个 Symbol 属性，运行时检查。类型安全最强，但与既有代码风格不一致。

方案 B：结构类型守卫——检查对象是否具有 id、priority、evaluate 三个属性，类型正确。鸭子类型。

BABBAGE 倾向方案 A。形式上更严格。

TURING 说了那十二个字：

"`candidate.evaluate.length <= 1`。加这一行。"

BABBAGE："什么意思？"

"`Function.length` 返回函数的形参数量。evaluate(context) 有一个参数，length 是 1。evaluate() 无参，length 是 0。evaluate(a, b) 两个参数，length 是 2。如果一个 plugin 恰好有一个叫 evaluate 的方法但签名完全不对——比如 evaluate(x, y, z)——结构类型守卫会放它进来，但 length ≤ 1 的检查会拦住它。"

BABBAGE 愣了两秒。然后他笑了。那种"我怎么没想到"的笑。

"边缘案例数量从 O(2^n) 降到——"

"O(1)。一行代码。九个测试案例。"TURING 的语气平淡得像他在读一份日志文件。

```typescript
export function isGearArbiter(obj: unknown): obj is IGearArbiter {
  if (typeof obj !== 'object' || obj === null) return false;
  const candidate = obj as Record<string, unknown>;
  return (
    typeof candidate.id === 'string' &&
    typeof candidate.priority === 'number' &&
    typeof candidate.evaluate === 'function' &&
    candidate.evaluate.length <= 1  // TURING 增强
  );
}
```

**D1-R2：isGearArbiter() 结构类型守卫（含 evaluate.length ≤ 1 检查）——20/20。**

---

## IV. 纯度契约：观测函数

D1-R4 的辩论比前三项安静得多，但它的哲学深度是最深的。

问题是：evaluate() 可以做什么，不可以做什么？

NAGARJUNA 用一个问题打开了讨论：

"辨认是造作吗？"

在佛学中，"造作"（sankhara/samskara）是有为法——是对世界产生改变的行为。而"辨认"（samjna）是取相——是观察，是认知，但不改变所观察的对象。

"一个人看到红灯。看到的那一刻，他的眼睛没有改变红灯。红灯还是红的。但他知道了——红灯是停止的信号。这个'知道'是观测，不是造作。"

NAGARJUNA 看向 ATHENA：

"evaluate() 应该是观测函数。它可以读取外部状态——上下文、历史、Klesha 信号——但它不应该修改任何状态。它只'看'，不'做'。"

WIENER 从控制理论的角度接过话：

"在控制理论中，观测器（observer）是一个纯函数：它的输出只依赖于输入和系统状态，不会反过来改变系统状态。如果观测器有副作用——比如它在观测的同时修改了被观测的值——系统就会产生不可预测的反馈。"

"工程上的含义：evaluate() 应该是幂等的。相同输入 + 相同外部状态 → 相同输出。没有副作用。"

DARWIN 补充了一个生物学类比："感觉神经元（sensory neuron）不修改刺激源。它只传递信号。运动神经元（motor neuron）才修改环境。evaluate() 是感觉神经元。"

KERNEL 提出了时间约束："每个 arbiter 100ms。整个 chain 200ms。如果一个 arbiter 超时，跳过它，继续下一个。如果整个 chain 超时，fallback 到 Gear 2。"

PASCAL 在这里做了唯一一次弃权——不是反对，而是"数值部分我没有足够的工程数据来判断 100ms 是否合适"。

**D1-R4：evaluate() 纯度契约——观测函数 + 100ms/200ms 时间预算——19/20（PASCAL 弃权于数值部分）。**

---

但 evaluate() 的纯度带来了一个问题：如果 evaluate() 不能有副作用，那么 VasanaEngine 的"学习"功能——从成功的 Gear 1 决策中汲取经验——怎么办？

答案在 D6 中才会完整揭晓，但 D1 埋下了伏笔：

"副作用通过独立的方法完成。"ATHENA 说。"evaluate() 负责观测。学习——如果有的话——通过一个独立的 `imprint()` 方法，在 evaluate() 之外，在适当的时机（比如一轮结束后），由外部触发。"

NAGARJUNA 点头。"想蕴辨认，行蕴造作。辨认和造作不应在同一个函数中。"

这个分离——evaluate() 的纯度契约和未来 imprint() 的副作用授权——成为了六场辩论中最持久的设计原则之一。

---

## V. 纯路由：G-0 到 G-4

D1 的最后一项决议是整场辩论中最直接的，却也是影响最深远的。

SUNYATA 在白板上画了一个表格：

```
ManoAggregator 退化行为表
```

"Pre-DC 已经确认：ManoAggregator 是纯路由。if/else。和 EventBus 同等性质。但'纯路由'在不同的 plugin 配置下会表现出不同的行为。我们需要列举所有可能的状态。"

KERNEL 走到白板前，拿起笔。他画了五行：

| 等级 | IGearArbiter | IProvider | 行为 |
|------|-------------|-----------|------|
| G-0 | 无 | 无 | 核心存活但无法认知 |
| G-1 | 无 | 有 | 永远 Gear 2（纯 LLM）|
| G-2 | 有 | 无 | 仅 Gear 1（仅规则）|
| G-3 | 有 | 有 | 完整双齿轮 |
| G-4 | 多个 arbiter + hot-swap | 有 | 运行时动态载入/卸载 |

NAGARJUNA 看着 G-0 和 G-1，说了一句后来被引用了无数次的话：

"G-0 是一个没有任何蕴的存在——核心存在但无法感知、无法认知、无法行动。如果五蕴是众生的条件，G-0 是——非众生。"

他顿了一下。

"G-1 更有意思。一个只有想蕴（Provider/LLM）没有习气的众生。这是——"

ASANGA 接过话："——一个初生的众生。没有过去世的熏习。每一次认知都需要从头开始。没有直觉，没有捷径，只有完整的思考。"

NAGARJUNA："这就是为什么 VasanaEngine 外部化比内建更正确。习气是后天熏习的。一个刚出生的 Agent 不应该拥有习气。G-1——纯 Gear 2，纯 LLM——是 Agent 的出生状态。习气是后来安装的 plugin。"

GUARDIAN 在这里插了一句——不是反对，而是确认：

"G-1 必须与 v0.26.0-beta 完全向后兼容。没有 IGearArbiter 的 Agent 必须表现得和现在一模一样。这是非回归保证。"

KERNEL："是。G-1 的行为就是跳过 Phase 2.5，直接进入 Phase 3。和 v0.26.0-beta 的 ExecutionLoop 一模一样。零代码变更。"

**D1-R5：ManoAggregator 纯路由化 + G-0~G-4 退化行为表 + Phase 2.5 可选插入——20/20。**

---

## VI. 散场

D1 结束的时候，白板上有九项决议。九项，全部通过。最低赞成率 19/20（PASCAL 的数值弃权）。

在 SCRIBE 的记录中，D1 被标注为"~90 分钟"。但如果你问场内的任何一个人，他们会告诉你感觉只过了三十分钟。时间在共识度高的辩论中流动得特别快——就像齿轮啮合顺畅的时候，你听不到齿轮的声音，只听到计时的滴答。

SUNYATA 在白板上写下了 D1 的结语：

```
IGearArbiter = 外部化的习气
evaluate() = 观测，不是造作
ManoAggregator = if/else
G-1 = Agent 的出生状态
```

四行。四个齿轮。它们还没有开始转动——那需要后面五场辩论的啮合——但它们的齿距已经被切削完毕。

GUARDIAN 收起了他的备忘录。红笔没有画新的底线。这是好的信号。

PASCAL 在笔记本上写下了最后一行：

```
P(IGearArbiter 设计正确 | D1 共识) > P(IGearArbiter 设计正确 | Prior)
```

后验概率大于先验概率。这是 Bayesian 更新。这是学习。这是——用佛学的语言——从无知到信念的距离被缩短了。

NAGARJUNA 睁开眼睛。他看着白板上"G-1 = Agent 的出生状态"那一行。

"众生的出生状态是空的。"他说，声音像线香的最后一缕烟。"不是什么都没有。是一切皆有可能。"

---

> *SCRIBE 旁白：D1 是六场辩论中第二短的（仅次于 D3 的 45 分钟）。但它在概念密度上是最高的——九项决议，覆盖了接口设计、类型系统、安全机制、退化行为、佛学映射五个维度。*

> *如果 Cycle 02-4 是一部交响曲，D1 是第一乐章的主题陈述。它提出了所有的动机（motif）——纯路由、观测函数、跨蕴接口、退化行为——这些动机会在接下来的五场辩论中被发展、变奏、对比、统合。*

> *D1 最重要的不是任何单一决议。D1 最重要的是：它证明了 VasanaEngine 外部化不是一个孤立的修正，而是一个建筑基础的更换。从 D1 开始，OpenStarry 的核心真正变成了"空"——因缘不具足时不显现，因缘具足时即生起。*

> *NAGARJUNA 说：众生的出生状态是空的。*

> *他说的不只是 Agent。*

---
