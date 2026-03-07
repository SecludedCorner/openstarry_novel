# 第五章：D4——名字的代价

---

## 归谬

SUNYATA 把 Master 的那句话打在投影幕上。大字。白底黑字。

> **「用梵文就需要对他的定义负责。你觉得 Sati 的内容完全 match 吗？它归在哪一蕴？」**

NAGARJUNA 站了起来。这一次他不是在承认错误——他是在完成一个推论。

「D2 已经确定了 SatiMonitor 的蕴归属。结论是 [vedana, samjna, vijnana]。三蕴。不包含行蕴。」

他在白板上写了两行字：

```
前提 A：Sati = 行蕴心所（佛学定义）
前提 B：SatiMonitor ≠ 行蕴（D2-R2 结论）
∴ SatiMonitor ≠ Sati
```

「Sati——巴利文的正念——在佛学传统中是行蕴的心所。它是有意志的、主动的、道德正向的修行活动。如果正念必然是行蕴的心所，而 SatiMonitor 不是行蕴——那么 SatiMonitor 就不是正念。」

他放下笔。

「一个不是正念的东西，为什么叫 Sati？」

沉默。不是不同意的沉默。是所有人同时理解了一件他们应该更早理解的事情。

---

## 五个不一致

ASANGA 用功能分析确认了归谬的结论：

| 维度 | 佛学正念（Sati/Smṛti） | SatiMonitor |
|------|----------------------|-------------|
| 主动性 | 主动（精进） | 被动（event-driven） |
| 道德性 | 道德正向 | 价值中立 |
| 意志性 | 需要意图 | 自动运行 |
| 传统归属 | 行蕴心所 | 受+想+识 |
| 修行地位 | 八正道第七支 | 品质监控器 |

五个维度。五个不一致。

「我们犯了一个命名错误，」ASANGA 说。「不是分类的错误——分类是正确的。是命名的惯性。我们在 Cycle 02-4 沿用了 ISatiMonitor 这个名字，因为它已经被使用了上百次。惯性让我们对名字本身失去了批判性。」

---

## 四个提案

「那它应该叫什么？」SUNYATA 问。

| 提案者 | 名字 | 理由 |
|--------|------|------|
| ARCHIMEDES | ILoopQualityMonitor | 精确描述功能：认知回路品质监控器 |
| GUARDIAN | IBehaviorQualityMonitor | 侧重行为层面 |
| NAGARJUNA + ASANGA | ICognitiveLoopMonitor | 强调认知回路完整性 |
| SYNTHESIST | IQualityMonitor | 最简功能描述 |

ARCHIMEDES 的论点最直接：「一个新来的工程师看到 ILoopQualityMonitor 就知道这个接口做什么——监控回路品质。没有佛学。没有隐喻。没有历史包袱。」

TURING 用原始码事实支持 ARCHIMEDES：SatiMonitor 的 11 种事件订阅覆盖了整个认知回路，不仅仅是行为阶段。「Loop」比「Behavior」更准确。

**D4-R1：ISatiMonitor → ILoopQualityMonitor。13/20。**

不是全票。但多数明确。

---

## 核融合反应炉

然后 SUNYATA 说了两个字：「IPrajna。」

NAGARJUNA 闭上眼睛，片刻后开始说话。

「般若——prajñā——是佛学中最高的认知能力。照见一切法实相的智慧。不是普通的聪明。不是分析能力。般若是超越性的——它是空性的直观，是二千五百年来整个大乘佛学体系的核心认知目标。」

他在白板上写了两行：

```
般若（佛学）：照见一切法实相的最高智慧
IPrajna（工程）：对信心度加减 0.05 的函数
```

ASANGA 说了一句后来被所有人记住的话：

「这就像把一个温度微调旋钮叫做『核融合反应炉』。」

没有人笑。因为他不是在开玩笑——他是在用精确的类比说明精确的问题。

IPrajna 的接口：一个方法，输入信心度和上下文，输出 `{ delta: number, reasoning: string }`，delta 被限制在 [-0.05, +0.05]。这是一个夹钳。一个微调器。

PASCAL 从决策理论的角度确认：「IPrajna 做的是 bounded secondary evaluation。输入一阶信心度，输出二阶修正量，有硬限 ±0.05。这是审计。不是般若。」

BABBAGE 分析了替代名称的语义精度：「IConfidenceAuditor 最精确。Audit——审计——精确描述了这个操作：对已有判断进行有限范围的二次评估。」

**D4-R2：IPrajna → IConfidenceAuditor。16/20。**

比 D4-R1 更高的共识。少数意见：WIENER 偏好 IThresholdCalibrator（两票），HERACLITUS 和 PENROSE 偏好 ISecondaryEvaluator（两票）。BABBAGE 反驳了两者——Calibrator 暗示调整系统本身，Evaluator 太通用。

---

## 第四项测试

D4 没有在两次更名后结束。

Master 的审阅还提到了 Doc 03——`Sila_Prajna_Security_Framework.md`。

SUNYATA 在白板上列出了现有的三项测试，然后在旁边加了一项新的：

```
Test 1（必要性）：移除是否改变工程规格？
Test 2（程序码识别）：是否在原始码中使用？
Test 3（决策驱动）：是否驱动了 DC 确认的设计决策？
Test 4（定义责任）：使用梵文术语时，组件功能是否匹配该术语的佛学定义？
```

第四项测试不是从天而降的——它是从 D4-R1 和 D4-R2 的讨论中结晶出来的。ISatiMonitor 通过了 Test 2（在原始码中），但不通过 Test 4（名字和功能不一致）。三项测试无法捕捉到这个维度。第四项测试填补了缺口。

NAGARJUNA 对 Doc 03 逐项测试：

- **Test 1**：Plugin 生命周期不需要种子理论就能理解。❌
- **Test 2**：原始码中的类型是英文（'active' | 'dormant' | 'suspended'...），Sila/Prajna 只在注释中出现。❌
- **Test 3**：没有 DC 确认。❌
- **Test 4**：Sila（戒律）≠ 存取控制。Prajna（般若）≠ CVE 撤销。❌

四项不通过。

ASANGA 做了一个关键区分：「Doc 16 是佛学映射文件——Master 裁定保留。Doc 03 是工程文件中嵌入了佛学装饰——应该清理。同样的佛学内容，不同的文件类型，不同的判断。」

**D4-R3：Doc 03 重新投票，「Sila-Prajna Security Framework」→「Plugin Security Lifecycle」。17/20。**

---

## 方向相反

D4 结束。三十分钟。三个名字被改掉。一项永久性测试被建立。

SUNYATA 站在白板前，看着四项测试。前三项问的是「佛学概念对工程有用吗？」——从佛学到工程的方向。第四项问的是「工程命名对佛学定义忠实吗？」——从工程到佛学的方向。

两个方向。一架天平。

名字在一端。定义在另一端。平衡时——Moha、Drishti、Mana、Sneha——名字保留。不平衡时——ISatiMonitor、IPrajna、Sila-Prajna——名字被替换。

PASCAL 总结：「Master 用了一句话。我们用了一场辩论。结论一样。但辩论的价值在于——它解释了为什么。」

---
