# 序章：冷白的光

---

灯光在凌晨三点从琥珀色变成冷白色。

SUNYATA——研究总协调者——坐在圆形剧场的控制台前，把色温从 3200K 推到 6500K。他读了 Master 的信五遍。信只有 45 行，没有附件，放在 `research input/master_letters/cycle02-5/` 里，安静得像一张夹在报告中的便条。

但每一行都像手术刀。

Master 的核心指示：openstarry_doc 中的佛学映射过度牵强——「教诫/善巧/正念」、「戒定慧三学」、「event-driven = 正念」——增加了阅读障碍。Sati plugin 的蕴归属需要重新思考。最重要的是：五蕴子类别、依赖注入、agent core 如何载入五蕴 plugin、五蕴如何在 agent core 中流转——用工程语言回答。

Cycle 02-5 的主题被定义为：**ARCHITECTURAL——五蕴如何作为 OOP 架构运作？**

SUNYATA 把剧场灯光调成手术室的冷白，因为这一轮不是研究——是手术。切除装饰性的佛学映射，保留有工程价值的架构核心。

凌晨四点，NAGARJUNA 走进了剧场。他没有预约。他带着一个自我承认：Cycle 02-4 的 openstarry_doc 中，有些佛学映射是他在工程结论确定之后才「后贴」上去的标签。「Hard rules = sila」不是驱动设计决策的洞见——是设计完成后才加上去的装饰。

这一夜的对话产出了 Cycle 02-5 的基础设施：

**四层框架**：KEEP（保留）/ RELOCATE（迁至附录）/ REMOVE（移除）/ FILE REVIEW（整份审查）。

**三项测试**：
1. 必要性：移除是否改变工程规格？
2. 代码识别：该术语是否在源代码中使用？
3. 决策驱动：该佛学概念是否驱动了 Master 确认的设计决策？

研究分为三条轨道：Track A（五蕴 OOP 架构）、Track B（佛学映射审计）、Track C（Sati Plugin 重分类）。

20 位研究者。5 场辩论（3 场预定 + 2 场计划外）。从凌晨到傍晚。

手术刀已经消毒。病人已经上了手术台。

---
# 第一章：审计与研究

---

## R1：独立研究

九份独立研究报告在 R1 阶段产出。三条轨道并行推进。

### Track A：五蕴工程架构

**A1（LINNAEUS + ASANGA）**：五蕴子类别树。完整的 OOP 接口继承分析——IRupa 分为 IListener 和 IUI；IVedana 产生 ChannelVedana（连续信号）；ISamjna 对应 IProvider；ISamskara 窄化为 ITool；IVijnana 最复杂，下辖 IGuide、IGearArbiter、IVolition、IKlesha 四个子接口。三个「弱继承」案例被记录——IVedanaSensor、IGearArbiter、IKlesha 不显式 extends 根接口。

**A2（VITRUVIUS + KERNEL + TURING）**：DI 布线。Pure DI，`createAgentCore()` 为唯一 Composition Root，21 个组件严格线性建立，9 个 Registry。Lazy Accessor 模式、Provider 能力过滤、Resolver 闭包延迟解析。与 Spring/Guice/InversifyJS 的比较矩阵确认 Pure DI 是微核心的正确选择。

**A3（DARWIN + MESH）**：Plugin 载入生命周期。IPlugin = Manifest + Factory。双载入路径（Sandbox worker thread / Direct main thread）。八状态生命周期状态机。Sandbox 安全链：签名验证 → 静态 import 分析 → Worker 隔离 → Heartbeat → 指数退避重启。

**A4（HERACLITUS + WIENER + BABBAGE）**：五蕴执行流。FSM 六状态、九阶段处理。Phase 1（rupa）→ Phase 3（samjna）→ Phase 5（vijnana）→ Phase 6（samskara）→ Phase 7（vedana）→ Phase 8（vijnana）。三层稳定回路。BABBAGE 提供了完整的 FSM 形式规格。

**A5（LEIBNIZ + ATHENA + PENROSE）**：跨蕴互动。5×5 互动矩阵。Model Delta 五层阈值公式。PENROSE 提出了三个涌现模式假说——适应性保守、双稳态切换、注意力漏斗。

### Track B：佛学映射审计

**B1（ARCHIMEDES + SCRIBE）**：逐行审计 7 份文件。50 个映射实例——23 个 KEEP（46%）、13 个 RELOCATE（26%）、14 个 REMOVE（28%）。Doc 43 装饰比例最高（60%）。Doc 16 和 Doc 31 被标记为「整份审查」（装饰比例 80% 和 70%）。

**B2（NAGARJUNA + ASANGA + PASCAL）**：映射边界原则。NAGARJUNA 的两谛分离、ASANGA 的功能定位、PASCAL 的损害不对称性（false include 的累积认知负担 >> RELOCATE 的一次性搜索成本）。三项测试在此文件中被正式论证。

### Track C：Sati Plugin

**C1（TURING + GUARDIAN）**：纯工程功能分析。SatiMonitor 订阅 11 种 EventBus 事件，三阶段管道处理（缓冲 → 批次分析 → 品质向量计算），输出 LoopQualityVector 四维度（Continuity, Granularity, Speed, Equanimity），**零副作用**。工程等价物：APM Agent + 行为模式分析器 + QoS Monitor + SPC 异常侦测器。

**C2（ASANGA + LINNAEUS）**：蕴组成提案。四个方案——A ['vedana','samjna']、B ['vedana','samjna','vijnana']（推荐）、C ['samjna','vijnana']、D ['vijnana']。核心论证：SatiMonitor 的事件订阅=受（vedana），模式辨认=想（samjna），品质评估=识（vijnana）。不包含行蕴——因为它不执行任何动作。

## R2：交叉审阅

TURING 验证了 40+ 个代码引用，发现 4 个问题（无严重错误）。24 个共识点免辩论通过。7 个开放问题和 4 个分歧进入 D1-D3 辩论。

---
# 第二章：边界——D1 佛学映射边界辩论

---

**时长**：~90 分钟 | **主席**：SUNYATA | **投票**：10 项 | **结果**：全部 20/20

D1 创造了本专案历史上的一项纪录：十次投票，十次全票通过，零少数意见。

## 四层框架与三项测试（D1-Q1：20/20）

四层框架和三项测试被正式确认为永久性判断标准。NAGARJUNA 提供了哲学基础（两谛分离），PASCAL 提供了数学论证（损害不对称性），ARCHIMEDES 提供了操作验证（50 案例全覆盖）。

## 三批次审判

**Batch A（D1-Q2-A：20/20）**——Master 明确批评的 5 项映射，全部 REMOVE：
- Hard rules = sila（戒）→ REMOVE
- Soft rules = upaya（善巧方便）→ REMOVE
- Heuristic rules = smrti（正念）→ REMOVE
- event-driven = mindfulness → REMOVE
- Threefold Training 映射 → REMOVE

NAGARJUNA 承认前三项是「后贴标签」——佛学名称在工程结论确定之后才被添加。

**Batch B（D1-Q2-B：20/20）**——8 项学术内容，全部 RELOCATE 至附录。特殊处理：B-6（PASCAL 的 Moha 数学形式化 `Var(epsilon) = f(theta_moha)`）保留在主文，只有《成唯识论》引文移至附录。

**Batch C（D1-Q2-C：20/20）**——7 项代码标识符 / DC 确认概念，全部 KEEP。包括五蕴类型名称、Klesha 模块名、CoarisingBundle 等。

## 个别文件决议

- **D1-Q3**（20/20）：Doc 38 L540-544 删除佛学映射栏。
- **D1-Q4**（20/20）：Doc 44 L478 三学映射 REMOVE；Section 10 剩余 RELOCATE。NAGARJUNA 承认三学映射是他的「类别错误」——三学是定性分类，五层模型是定量分层。
- **D1-Q5**（20/20）：Doc 43 更名延后至 D2 决定后。
- **D1-Q6**（20/20）：Klesha 模块名 Moha/Drishti/Mana/Sneha KEEP。DC-1 确认 + 源代码标识符。
- **D1-Q7**（20/20）：Doc 16 拆分——Section 5 提取为独立文件。（*后被 Master 推翻*）
- **D1-Q8**（20/20）：Doc 31 拆分降级。（*后被 Master 推翻*）

**D1-Q7 和 D1-Q8 的推翻**：Master 裁定恢复原状——Doc 16 和 Doc 31 是独立的佛学映射文件，不是工程文件中的装饰。三项测试适用于工程文件，不适用于映射文件。团队的框架少了一个维度：**文件类型识别**。

ARCHIMEDES 在审计表中加入了新栏位——文件类型（工程 / 设计决策 / 佛学映射），作为三项测试的前提条件。

---
# 第三章：三面之镜——D2 Sati Plugin 蕴归属辩论

---

**时长**：~60 分钟 | **主席**：SUNYATA | **投票**：3 项

## 更名策略（D2-R1：19/20）

保留 `Sati` 代码标识符，文件标题从「Mindfulness Architecture」改为「Cognitive Loop Quality Monitoring Architecture」。加入「命名说明」段落。安全文件使用全名。

唯一反对票：GUARDIAN——偏好完全更名以消除文化背景知识需求。接受多数决议附带安全文件全名条件。

## 五蕴组成（D2-R2：18/20）——核心决议

**结论：skandha: ['vedana', 'samjna', 'vijnana']**

四个功能到三蕴的映射：

| 功能 | Skandha | 说明 |
|------|---------|------|
| EventBus 事件订阅（11 种，持续感知） | vedana | 接收认知回路信号 |
| 滑动窗口 + 模式辨认 | samjna | 从事件流中辨认行为模式 |
| LoopQualityVector + SPC 异常判断 | vijnana | 超越描述性辨认的评价性品质判断 |
| **不执行工具、不修改状态** | **排除 samskara** | 不是正念修行 |

关键论证转折：

- **ASANGA**：佛学正念（smṛti）是行蕴心所——主动的、有意志的、道德正向的。SatiMonitor 是被动的、自动的、价值中立的。因此 SatiMonitor 不是正念，不应归为行蕴。
- **LINNAEUS**：OOP 比较——「IGearArbiter 是『被调用来看一下』；SatiMonitor 是『一直在看』。」持续订阅 vs 按需调用——足以构成独立的 vedana 声明。
- **ARCHIMEDES**（转折点）：三蕴和二蕴的工程成本差异为零——PluginManifest 的 skandha 栏位已支持多值。消除「三蕴太复杂」的顾虑后，讨论转为纯分类精度，Proposal B 的优势压倒性。
- **少数意见**（MESH、KERNEL）：Proposal C ['samjna','vijnana'] 与 IGearArbiter 分类对称，有长期维护价值。

**历史意义**：SatiMonitor 成为 OpenStarry 第一个三蕴 plugin。

## PluginHooks 专属槽位（D2-R3：20/20）

新增 `monitors?: ISatiMonitor[]` 专属槽位。遵循 Cycle 02-4 的 `arbiters` 先例（SDK 接口 → PluginHooks → Registry → PluginLoader 四步模式）。

---
# 第四章：完备性——D3 五蕴 OOP 架构辩论

---

**时长**：~120 分钟 | **主席**：SUNYATA | **投票**：6 项

## 五根接口充分性（D3-R1：20/20）

四个独立论证收敛至同一结论：IRupa、IVedana、ISamjna、ISamskara、IVijnana 五个根接口足以覆盖所有功能需求。

- **LINNAEUS**：100% 功能覆盖率验证。
- **BABBAGE**：类型代数完备性定理（Q.E.D.）。
- **ASANGA**：阿毗达磨穷举分类公理。
- **KERNEL**：五个微核心子系统映射（I/O、感测、计算、执行、调度）。

PENROSE 附带建议：监控 vijnana 子接口数量（目前 4，未来 6；超过 10 时考虑拆分）。

## PluginHooks 映射正确性（D3-R2：20/20）

TURING 逐行源代码验证，九项映射全部正确。

焦点讨论：SlashCommand 不属于任何蕴——因为它绕过整个 ExecutionLoop（类比：Unix 信号处理器）。GUARDIAN 安全观察：SlashCommand 绕过 SafetyMonitor，如果 plugin 通过此路径执行危险操作，五蕴安全机制全部无效。此观察记入 Doc 45。

## skandha 作为元数据（D3-R3：18/20）

维持现状——skandha 是元数据，不是路由基础。类型路由已完备。少数意见（GUARDIAN、LINNAEUS）：即使只是 warning 的一致性验证也有审计价值。

## ISamskara 子接口（D3-R4：20/20）

维持 ITool 为唯一子接口。ASANGA 坦承：这是五蕴架构中佛学自洽性最弱的部分——传统行蕴涵盖 49 心所，OpenStarry 窄化为外部行为（ITool）。HERACLITUS 的动态论证：IVolition 在 Phase 5，ITool 在 Phase 6——将 IVolition 移至行蕴会造成「行蕴在行蕴之前」的概念错位。

DC-6「行蕴保持开放，不锁定」继续有效。

## 十二因缘（D3-R5：13/20 Proposal C）

最具争议的 D3 投票。Proposal C（选择性附录映射）胜出。

- **NAGARJUNA**：尺度不匹配——十二因缘描述三世因果（宏观），ExecutionLoop 描述单次认知处理（毫秒级）。
- **BABBAGE**（投 B）：十二因缘是线性链，ExecutionLoop 是有回圈的 FSM——图结构根本不同。
- Proposal B（不映射）获 7 票——D3 最大的少数意见群。

## 认知序列（D3-R6：17/20 Proposal C）

比十二因缘获得更高共识——因为描述的是相同尺度现象（单一认知活动的内部阶段）。HERACLITUS 提供了八状态对比表，五个「高」或「中高」平行。

BABBAGE 从 B（十二因缘）转为 C（认知序列）——FSM 态射分析是转向的关键论据。十二因缘没有态射。认知序列有。

PENROSE 理论贡献：认知回路的结构趋同是功能需求的必然结果，不是刻意模仿。

## 架构评估结论

**v0.28.0-alpha 的五蕴 OOP 架构在结构层面是充分的。** 三个已知缺口（弱继承、VedanaAssessment 布线未完成、IConfidenceAuditor/ILoopQualityMonitor 尚未实作）都是计划中的增量改进。

---
# 第五章：名字的代价——D4 命名修正辩论

---

**时长**：~30 分钟 | **触发**：Master 审阅 | **投票**：3 项

D4 不在原始议程中。它由 Master 的一句话触发：

> **「用梵文就需要对他的定义负责。你觉得 Sati 的内容完全 match 吗？」**

## NAGARJUNA 的归谬论证

```
前提 A：Sati = 行蕴心所（佛学定义）
前提 B：SatiMonitor ≠ 行蕴（D2-R2 结论）
∴ SatiMonitor ≠ Sati
```

如果正念在佛学中必然是行蕴，而 D2 已经证明 SatiMonitor 不是行蕴——那 SatiMonitor 就不是正念。一个不是正念的元件，不应该叫 Sati。

ASANGA 确认：「如果 SatiMonitor 不是行蕴活动，那它就不是 Sati。我们自己的分类分析否定了我们自己的命名。」

## ISatiMonitor → ILoopQualityMonitor（D4-R1：13/20）

ARCHIMEDES 的提案胜出：「Loop Quality Monitor」——认知回路的品质监控器——精确描述功能，无佛学，无隐喻。

少数意见：IBehaviorQualityMonitor（GUARDIAN，4 票）、ICognitiveLoopMonitor（NAGARJUNA + ASANGA，2 票）、IQualityMonitor（SYNTHESIST，1 票）。

完整更名表：ISatiMonitor → ILoopQualityMonitor、SatiQualityVector → LoopQualityVector 等 8 项。

## IPrajna → IConfidenceAuditor（D4-R2：16/20）

NAGARJUNA：「般若是佛学中最高的认知能力——照见一切法实相的智慧。」

ASANGA：「把一个温度微调旋钮叫做核融合反应炉。」

IPrajna 的实际功能：一个方法，输入信心度，输出 `{ delta: number, reasoning: string }`，delta 限制在 [-0.05, +0.05]。这是审计——不是般若。

BABBAGE：IConfidenceAuditor 语义最精确——独立的、有限范围的、产生书面记录的二次检查。

少数意见：IThresholdCalibrator（WIENER，2 票）、ISecondaryEvaluator（HERACLITUS + PENROSE，2 票）。

## Doc 03 重新投票（D4-R3：17/20）

「Sila-Prajna Security Framework」→「Plugin Security Lifecycle」

初始投票 14/20 保留不变。Master 审阅触发重新检验——四项测试全部不通过：必要性（不需要种子理论理解 plugin 生命周期）、代码识别（实际类型用英文）、决策驱动（无 DC 确认）、定义责任（戒 ≠ 访问控制，般若 ≠ CVE 撤销）。

ASANGA 的关键区分：Doc 16 = 独立映射文件（Master 裁定保留）vs Doc 03 = 工程文件中的佛学装饰（应清理）。

## 第四项测试——定义责任（永久性标准）

> **「当使用佛学梵文术语作为代码标识符时，该组件的功能必须匹配该术语的佛学定义。如果不一致，使用工程术语。」**

补充 D1 的三项测试——即使名字通过 Test 2（代码识别），如果不通过 Test 4（定义责任），仍应更名。

影响范围：ILoopQualityMonitor 影响 6 份文件 100+ 处替换；IConfidenceAuditor 影响 5 份文件；Doc 03 重命名 + 内容清理。

---
# 第六章：纯粹的工程——D5 Plan29 工程规格辩论

---

**时长**：~75 分钟 | **参与者**：10 人 | **投票**：9 项

D5 是本专案历史上第一场完全没有佛学内容的辩论。十位工程师和科学家，零位佛学家（NAGARJUNA 和 ASANGA 自愿退出），讨论 TypeScript 接口的精确规格。

TURING 预提交了完整的 v0.28.0-alpha 设计模式报告——14 个源代码文件、所有 Registry 生命周期、timeout 模式、同步/异步模式、失败处理策略。这份「代码考古学」报告为所有决策提供了事实基础。

## 九项决议

| 决议 | 内容 | 票数 |
|------|------|------|
| D5-R1 | 独立 `auditor` hook 槽位（不复用 monitors） | 8/8 |
| D5-R2 | audit() 双模式回传 `T \| Promise<T>` | **5/8** |
| D5-R3 | timeout 200ms，fail-safe delta=0，可配置 | 8/8 |
| D5-R4 | 单一 auditor，last-wins（非数组） | 6/8 |
| D5-R5 | 失败处理：delta=0 + warning log | 共识 |
| D5-R6 | MonitorRegistry 在 ExecutionLoop.onLoopStart() 启动 | 7/8 |
| D5-R7 | LoopQualityVector 等权重 0.25×4 | 8/8 |
| D5-R8 | validatePluginSkandha() 维持 warning-only | 7/8 |
| D5-R9 | IConfidenceAuditor extends IVijnana，skandha ['vijnana'] | 8/8 |

**最激烈投票**：D5-R2（5/8）——纯异步 vs 双模式。GUARDIAN/KERNEL/VITRUVIUS 主张纯异步语义更精确；多数采双模式，遵循 IGearArbiter 先例和测试便利性。

## IConfidenceAuditor 最终规格（100%）

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

PluginHooks 最终形态：
```typescript
interface PluginHooks {
  // ... 既有栏位 ...
  monitors?: ILoopQualityMonitor[];   // Plan29 Wave 1
  auditor?: IConfidenceAuditor;       // Plan29 Wave 2
}
```

NAGARJUNA 在 D5 结束后的评语：「D4 证明了名字需要对定义负责。D5 证明了有些工程问题根本不需要定义——只需要规格。」

---
# 第七章：清理与成果

---

## 产出总览

五场辩论完成后，团队进入 R4 成果定稿。核心产出：

### Doc 45：五蕴 OOP 架构（新文件）

由 VITRUVIUS 和 KERNEL 撰写。纯工程语言。结构对应 D3 的六项投票：

1. **根接口完备性**（D3-R1）：五根接口 + 四个独立证明
2. **PluginHooks 映射**（D3-R2）：九项映射表 + TURING 源代码验证
3. **SlashCommand 分类**（D3-R2a/b）：不属任何蕴 + 安全观察
4. **skandha 元数据**（D3-R3）：元数据非路由
5. **DI 布线**（A2 摘要）：Pure DI + Composition Root
6. **ExecutionLoop 流转**（A4 摘要）：九阶段蕴映射 + 三层稳定
7. **跨蕴互动**（A5 摘要）：5×5 矩阵 + Model Delta 公式
8. **行蕴设计注记**（D3-R4a/b）：窄化说明 + DC-6 持续有效
9. **ILoopQualityMonitor**（D2+D4）：三蕴归属 + 命名历史
10. **附录 A**：十二因缘功能类比
11. **附录 B**：认知序列结构平行

### 文件清理范围

| 动作 | 项目 |
|------|------|
| **REMOVE** | Doc 38 佛学映射栏、Doc 44 三学映射、Doc 43 mindfulness 装饰（8 处）、Doc 37 佛学栏、Doc 03 佛学映射表 + 种子理论注释、Batch A 五项散布映射 |
| **RELOCATE** | Doc 44 §10 剩余 → Appendix_C、Batch B 八项 → 各附录、B-6 只移经文引用 |
| **KEEP** | 五蕴类型名、Klesha 模块名、CoarisingBundle、vasana 设计理由、samsaric stall |
| **恢复** | Doc 16（Master 裁定）、Doc 31（Master 裁定）|
| **更名** | ISatiMonitor → ILoopQualityMonitor（100+ 处）、IPrajna → IConfidenceAuditor（25+ 处）、Doc 03 文件名 |
| **新建** | Doc 45、Appendix_A/B/C |

### 统计

| 指标 | 数值 |
|------|------|
| 正式决议 | 29 + 6 附带 |
| 投票总次数 | 31 |
| 全票率 | 66%（历史最高） |
| 辩论总时长 | ~375 分钟 |
| 更名替换 | 120+ 处 |

## 永久性成果

1. **四层框架**：KEEP / RELOCATE / REMOVE / FILE REVIEW + 文件类型前提检查
2. **四项测试**：必要性、代码识别、决策驱动、**定义责任**
3. **Doc 45**：五蕴 OOP 架构完整工程文件
4. **IConfidenceAuditor 100% 规格**：可直接交付工程团队

## 已知缺口（非架构问题）

1. 三个弱继承接口不 extends 根接口
2. VedanaAssessment 布线未完成
3. Delta_audit 和 Delta_sati 在 v0.28.0 为零

## 结语

Cycle 02-5 回答了 Master 的核心问题——五蕴在 agent core 中如何运作？答案：五个接口、九个 Registry、一个回路。并确立了佛学语言和工程语言的边界原则：佛学名字不是免费的——每一个梵文标识符都是一个承诺，承诺功能匹配定义。如果无法兑现，使用工程术语。

---
