# 序章：从清理到建构 —— Cycle 02-6 的方法论定位

---

## 研究脉络与前轮遗产

Cycle 02-5 构成了 OpenStarry 研究史上规模最大的一次规范性修正。在五个研究日内，二十位跨学科研究者产出了 29 项正式决议，其中两项经 DC Master 覆议推翻（D3-R2 原始版本与 D4-R1 初始方案）。该轮研究的核心成果在于系统性地移除了装饰性佛学映射（decorative Buddhist mappings）—— 即那些仅在命名层面借用佛学术语、却不具备功能对应关系的标签。七份设计文件经历了重新命名、拆分与重组，确立了"功能分析优先于术语传统"的基本方法论立场。

Cycle 02-6 承接这一遗产，但研究性质发生了根本转变。若 02-5 的主题是"否定性判断"（什么是错的），02-6 的主题则是"肯定性建构"（什么是对的，以及对的东西应具备怎样的精确规格）。

---

## 双重研究委托

DC Master 于本轮下达了两份性质截然不同的研究委托。

**第一份委托（工程指示）** 聚焦于 Plan29 工程交付（v0.29.0-alpha）中新增的两个骨架元件：`IConfidenceAuditor`（信心度审计接口）与 `ILoopQualityMonitor`（回路品质监控接口）。Master 明确指出骨架不足以支撑工程推进，要求研究团队回答六个开放问题（OQ-29-1 至 OQ-29-6），涵盖：

1. AuditContext 应包含哪些字段？
2. extras bag 的写入与读取协议为何？
3. 审计日志（ConfidenceAuditLog）的完整格式？
4. 品质监控的计算公式与事件订阅清单？
5. Layer 2（审计）与 Layer 3（品质）如何整合进决策流程？
6. Plan30 的工程方向与范围？

**第二份委托（哲学指示）** 要求以原始经典（如是我闻）为第一手依据，重新深掘行蕴（samskara-skandha）的定义。Master 特别指出唯识学派（Yogacara）将大部分心所（cetasika）归入行蕴的做法"非常有问题"，并提示"活动与转换"（activity and transformation）的观念可用于拓展行蕴的子类别。

---

## 研究设计：双轨结构与跨轨道约束

研究总协调者 SUNYATA（#0）据此设计了四轨道结构：

| 轨道 | 范围 | 研究子项 | 团队规模 |
|------|------|---------|---------|
| Track A | AuditContext 类型 + 审计日志 | A1-A4 | 4 组 |
| Track B | ILoopQualityMonitor 实作规格 | B1-B4 | 4 组 |
| Track C | 行蕴哲学深掘 | C1-C4 | 4 组 |
| Track D | 工程同步与 Plan30 方向 | D1-D2 | 2 组 |

其中 Track A+B 构成工程轨（12 人），Track C 构成哲学轨（8 人），Track D 为桥接轨。

关键的方法论约束在于 **跨轨道影响协议**：哲学轨（Track C）的结论必须先于工程轨的最终设计完成。具体而言，D1（行蕴辩论）必须先于 D2（AuditContext 辩论）和 D3（品质监控辩论）进行，以确保哲学发现能够即时注入工程设计。

---

## 研究流程概览

本轮严格遵循标准五阶段流程：

```
R0 定向 → R1 独立研究（14 份报告） → R2 交叉审阅 → R3 辩论（3 场 / 17 决议） → R4 成果定稿
```

R1 阶段产出 14 份独立研究报告。R2 阶段完成 4 组跨轨道交叉对照与轨道内一致性检查，识别出 24 个共识点与 3 个分歧点。R3 阶段以三场辩论（D1 约 75 分钟、D2 约 85 分钟、D3 约 85 分钟，合计约 245 分钟）解决全部分歧，产出 17 项决议，其中 13 项全票通过（20/20），0 项被否决，0 项需 Master 覆议。

以下各章将依序展开哲学轨的行蕴深掘（第一章）、工程轨的审计上下文设计（第二章）、品质监控公式（第三章）、整合架构（第四章）、Master 心所指示的三轮精化（第五章）、辩论过程的方法论分析（第六章），以及最终工程蓝图（第七章）。

---
# 第一章：行蕴的经典学重构 —— 从 cetana 中心性到功能判定准则

---

## 1.1 问题的提出：行蕴作为"剩余类别"的困境

在 OpenStarry v0.2.0-beta 的五蕴架构中，行蕴（samskara-skandha）长期处于定义不足的状态。相较于色蕴（rupa，对应 `ISparsha` 感官接触接口）、受蕴（vedana，对应 `IVedana` 感受接口）、想蕴（samjna，对应 `ISamjna` 辨识接口）和识蕴（vijnana，对应 `IManas` 判断接口）的清晰功能映射，行蕴仅拥有一个子接口 `ITool`，负责外部工具调用。

这种不对称并非偶然。其根源在于唯识学派（Yogacara）对行蕴的处理方式。在唯识的五十一心所（cetasika）分类体系中，受蕴仅分配到"受"（vedana）一个心所，想蕴仅分配到"想"（samjna）一个心所，其余四十九个心所全部归入行蕴。行蕴由此成为一个"剩余类别"（residual category）—— 凡是不属于受和想的心理功能，一律归入行蕴。

DC Master 在研究委托中明确指出此做法"非常有问题"，并要求研究团队回归原始经典（如是我闻），重新建立行蕴的功能性定义。

---

## 1.2 原始经典中的行蕴定义

哲学轨由 NAGARJUNA（#7，中观学派哲学家）与 ASANGA（#8，唯识学派佛学家）领衔。值得注意的方法论安排是：被批评的学派（唯识）的专家被指派去审视自身学派的问题，以确保批判的内在性与深度。

### 1.2.1 六思身：cetana 作为行蕴的定义性特征

《杂阿含经》（Samyutta Nikaya 22.56, Khandha-samyutta）中，佛陀对行蕴的定义明确而狭窄：

> "云何行蕴？谓六思身：色思、声思、香思、味思、触思、法思。是名行蕴。"

此处的"思"即 cetana（意图/意志），"六思身"（cha cetana-kaya）指向六种感官对象的意图性回应。这一定义的关键特征在于其 **排他性**：行蕴不是"除受想以外的一切心理功能"，而是精确地指向 cetana —— 对六种对象的意图性造作。

### 1.2.2 造作功能：abhisamskara 与有为法的条件化

《杂阿含经》（SN 22.79）进一步阐明行蕴的功能：

> "行蕴造作色之被条件化状态（rupam abhisankharonti）。"

此处的动词 abhisankharoti 表明行蕴不仅"执行动作"，更根本地是"造作"（fabricate）—— 它创造条件、改变状态、影响后续认知过程。行蕴的造作功能甚至延伸至其他四蕴：它能造作色蕴的被条件化状态、受蕴的被条件化状态，乃至识蕴的被条件化状态。

### 1.2.3 芭蕉喻：无核心的动态过程

《杂阿含经》（SN 22.95, Phena-sutta）以芭蕉树（kadali）比喻行蕴：

> "譬如有人剥芭蕉茎，寻求坚实，层层剥之，了不可得。"

此喻直指行蕴的本体论地位：它不是一个具有坚实核心的"实体"（entity），而是一个持续运作的"过程"（process）。每一层纤维都是条件性的造作，剥开之后并无自性可得。

---

## 1.3 三个核心特质的归纳

基于上述经典文本，研究团队归纳出行蕴的三个核心特质：

| # | 特质 | 经典依据 | 功能意涵 |
|---|------|---------|---------|
| 1 | **cetana 中心性** | SN 22.56（六思身） | 行蕴以意图为定义性特征，非"剩余类别" |
| 2 | **造作一切有为法** | SN 22.79（abhisamskara） | 行蕴创造条件、改变状态，影响所有五蕴 |
| 3 | **无核心的动态过程** | SN 22.95（芭蕉喻） | 行蕴是过程而非实体，无自性可得 |

---

## 1.4 行蕴属性判定三准则

LINNAEUS（#13，分类学/本体论专家）在上述三个特质基础上，提出了一组可操作化的判定工具 —— 行蕴属性判定三准则（Three Criteria for Samskara Attribution）：

**准则一：造作性（Fabrication）**
- 该功能是否创造、改变或产生新状态？
- 判定方法：检查该功能的输出是否修改了系统状态或外部环境。

**准则二：意图驱动（Cetana-driven）**
- 该功能是否由 cetana（意图）驱动？
- 判定方法：检查该功能的触发是否源于系统的意志性决策，而非被动反应。

**准则三：环境改变（Environmental Modification）**
- 该功能是否改变后续认知条件？
- 判定方法：检查该功能执行后，后续认知回路的输入空间是否发生了变化。

三准则经 D1-R3 决议确认为**永久性工具**（permanent tool），适用于所有未来的蕴归属判定。

---

## 1.5 WRITE/READ 二分法

PENROSE（#18，量子意识研究专家）在讨论中提出了一个极具概括力的二分法：

> **行蕴 = WRITE（主动改变世界）**
> **识蕴 = READ（被动评估世界）**

这一二分法在计算机科学中具有天然的对应物。在操作系统理论中，WRITE 操作修改系统状态（副作用操作），READ 操作仅观察系统状态（纯函数操作）。映射到 OpenStarry 的代码：

| 操作类型 | 蕴归属 | 代码接口 | 功能 |
|---------|--------|-----------|------|
| WRITE | 行蕴 (samskara) | `ITool`, `ISlashCommand` | 执行动作、改变环境 |
| READ | 识蕴 (vijnana) | `IGuide`, `IVolition` | 评估情况、做出判断 |

此二分法经 D1-R5 决议（20/20 全票）正式确认，成为"活动与转换"原则的核心表述。

---

## 1.6 唯识心所系统的批判性分析

ASANGA 亲自主导了对唯识五十一心所系统的批判性分析（报告 C2）。以行蕴属性判定三准则为工具，他逐一检视了被唯识学派归入行蕴的 49 个心所，结果如下：

| 分类 | 数量 | 比例 | 说明 |
|------|------|------|------|
| 确属行蕴 | 7 | 14% | chanda（意欲）、virya（精进）、apramada（不放逸）等 |
| 已有正确归属 | 12 | 24% | 在 OpenStarry 中已经通过功能分析获得正确归属 |
| 可能属他蕴 | 18 | 37% | 功能上更接近识蕴（如 prajna/慧）或受蕴 |
| 混合/待研究 | 14 | 28% | 需要更精细的功能分析或跨蕴处理 |

此分析的方法论意义在于：它以功能分析（functional analysis）取代了传统分类（traditional taxonomy）作为蕴归属的判定依据。正如 ASANGA 本人所述：

> "心所列表是有用的功能描述清单，但它是论典（Abhidharma）的产物，不是佛陀的原话。我们可以参考其功能描述，但不能让其分类方式决定蕴归属。"

---

## 1.7 蕴归属五项永久性原则

基于上述研究，D1-R6 决议（20/20 全票）确立了五项永久性原则：

1. **功能分析原则**：功能分析为蕴归属的唯一依据。
2. **心所参考原则**：唯识五十一心所系统作为功能参考清单（reference list），不作归属依据。
3. **梵文限定原则**：梵文术语用于代码命名时，仅限源自原始经典者（如 skandha、sparsha），不使用论典创造的心所梵文名。
4. **跨蕴归属原则**：Plugin 不等于心所，蕴归属可自然跨越多蕴。
5. **既有决议原则**：既有归属决议（基于功能分析）继续有效。

这五项原则与后续第五章将讨论的 Master 八点规则共同构成了 OpenStarry 未来所有命名与归属问题的永久判定框架。

---
# 第二章：审计上下文的类型设计 —— 信息充分性与反馈回路切断

---

## 2.1 问题分析：IConfidenceAuditor 的信息贫乏

Plan29 交付的 `IConfidenceAuditor` 接口存在一个结构性缺陷：审计函数的输入仅包含 `RouteResult`（路由结果），即仲裁器的最终决策输出。这意味着审计员在做出信心度调整判断时，无法获取以下关键信息：

- 触发本次决策的原始事件（sparshEvent）
- 仲裁器的推理过程与中间评估（gearEvaluation）
- 操作的风险等级（riskCategory）
- 历史信心度序列（historicalConfidence）

以决策理论的术语而言，这是一个 **信息不对称**（information asymmetry）问题：审计员被要求对决策品质做出判断，却无法接触决策的形成过程。DC Master 明确指示：审计员需要更多信息。

然而，扩充审计员可见信息的同时引入了一个控制理论风险：**正反馈回路**（positive feedback loop）。

---

## 2.2 正反馈回路的威胁模型

WIENER（#12，控制理论专家）识别出三条潜在的正反馈路径：

**路径一：historicalConfidence 污染。** 若历史信心度序列包含审计后的调整值（而非仲裁器的原始输出），审计员将在已被自身影响的数据上做出进一步调整，形成 `audit → confidence → history → audit` 的闭合回路。

**路径二：审计结果泄漏。** 若 AuditContext 包含前次审计的结果，审计员可能基于自身先前的判断做出确认偏误（confirmation bias）驱动的决策，形成 `audit_n → context_{n+1} → audit_{n+1}` 的序列相关。

**路径三：extras 后门。** 若 extras bag 允许写入审计相关的键值对，审计员可能通过扩展袋间接获取自身的历史输出。

在控制理论中，这三条路径均可导致 BIBO 不稳定（Bounded-Input Bounded-Output instability）：有界输入可能产生无界输出，即信心度值在迭代中单调增长或振荡发散。

---

## 2.3 AuditContext 类型定义

团队设计的 `AuditContext` 接口（D2-R1，20/20 全票）如下：

```typescript
export interface AuditContext {
  readonly version: 1;                              // 字面量类型，用于未来版本迁移
  readonly sparshEvent: SparshEvent;                // 触发事件（必填）
  readonly gearEvaluation: GearEvaluation;          // 仲裁器完整推理过程
  readonly riskCategory: RiskCategory | undefined;  // 风险类别（可选）
  readonly routeResult: RouteResult;                // 审计前路由结果快照
  readonly historicalConfidence?: readonly number[]; // 环形缓冲区，预设 10，可配置
  readonly extras: ReadonlyMap<string, unknown>;     // 泛型扩展袋
}
```

设计要点：

- **核心字段由 Core 组装**：每次路由必有 sparshEvent、gearEvaluation、routeResult。
- **historicalConfidence 为可选**：环形缓冲区（ring buffer）实现，预设容量 10，可通过配置调整。
- **extras 为 ReadonlyMap**：浅冻结（shallow freeze）确保不可变性，泛型 `unknown` 值类型通过类型安全存取器（`getExtra<T>(extras, key, guard)`）读取。

---

## 2.4 WIENER 三约束：正反馈回路的系统性切断

WIENER 针对上述三条反馈路径设计了三条对应约束，团队称之为"WIENER 约束"（WIENER Constraints, C-1/C-2/C-3）：

**C-1（历史纯净性）**：`historicalConfidence` 仅记录仲裁器的原始信心度（raw arbiter confidence），不包含审计后的调整值。

形式化表述：设 $c_t^{raw}$ 为第 $t$ 轮仲裁器输出的原始信心度，$c_t^{adj}$ 为审计后的调整信心度，则：
$$\text{historicalConfidence}[t] = c_t^{raw}, \quad \forall t$$

**C-2（审计结果隔离）**：`AuditContext` 不包含前次审计的输出（`ConfidenceAuditLog`）。每次审计在信息上独立于先前审计。

**C-3（extras 前缀禁令）**：extras bag 中禁止使用以下三个前缀的键：
- `audit:` —— 防止审计结果通过 extras 泄漏
- `core:` —— 保留给 Core 内部使用
- `internal:` —— 保留给系统内部使用

三约束共同确保了审计员的 **因果隔离**（causal isolation）：审计员的输出不能以任何路径反馈成为其自身未来的输入。

---

## 2.5 BIBO 稳定性的形式化验证

BABBAGE（#9，理论计算机科学家）对 WIENER 三约束下的系统稳定性进行了形式化验证。

设审计函数为 $f: \mathcal{C} \times \mathcal{A} \to [-\delta_{max}, +\delta_{max}]$，其中 $\mathcal{C}$ 为 AuditContext 空间，$\mathcal{A}$ 为审计员内部状态空间，$\delta_{max} = 0.05$。

在 C-1/C-2/C-3 约束下：
- 审计函数 $f$ 的输入不包含自身先前的输出
- 调整量受限幅约束 $|\Delta c| \leq 0.05$
- 信心度值域 $c \in [0, 1]$ 自然有界

因此系统满足 BIBO 稳定：任意有界输入序列 $\{x_t\}_{t=1}^{\infty}$ 产生有界输出序列 $\{y_t\}_{t=1}^{\infty}$，且 $\|y\|_{\infty} \leq 1$。

---

## 2.6 extras bag 协议

extras bag 的读写协议（D2-R2，19/20）定义如下：

| 方面 | 规格 |
|------|------|
| 写入模式 | 双事件模式 + SDK `emitWithExtras()` 便利函数 |
| 收集管道 | `ManoAggregator` 订阅 `audit:context_contribute` 事件 |
| 读取接口 | `getExtra<T>(extras, key, guard)` 类型安全存取器 |
| 不可变性 | 浅冻结 + `ReadonlyMap` |
| 容量限制 | 最多 32 个键，每键最长 128 字符 |
| 禁止前缀 | `audit:`, `core:`, `internal:` |
| 键命名规范 | `{category}:{name}` 格式，如 `loopQuality:vector`, `loopQuality:composite` |

一票反对意见认为双事件模式（`loopQuality:updated` + `audit:context_contribute`）增加了不必要的复杂性，直接订阅即可。多数意见则认为双事件模式提供了通用性 —— 它不仅服务于品质监控器，任何 Plugin 均可通过相同协议向 extras bag 贡献信息。

---

## 2.7 ConfidenceAuditLog：GUARDIAN D5 条件的兑现

Cycle 02-5 的 D5 决议中，GUARDIAN（#11，资安专家）同意将审计员的调整幅度限制在 $\pm 0.05$，但附带条件：下一轮必须定义完整的审计日志格式。

D2-R3（20/20 全票）兑现了这一条件。`ConfidenceAuditLog` 类型包含以下字段：

| 字段 | 类型 | 语义 |
|------|------|------|
| `inputConfidence` | `number` | 审计前信心度 |
| `rawDelta` | `number` | 审计员建议的调整量 |
| `clampedDelta` | `number` | 限幅后的实际调整量 |
| `wasClamped` | `boolean` | 是否触发了限幅 |
| `reasoning` | `string` | 审计理由（截断 500 字符，Core 负责） |
| `outputConfidence` | `number` | 审计后信心度 |
| `result` | `RouteResult` | 最终路由结果 |
| `auditDurationMs` | `number` | 审计耗时（毫秒） |

主通道为 EventBus `audit:completed` 事件。可选的 JSONL file appender 供持久化使用（排程至 Plan31）。PII（个人可识别信息）净化由 Plugin 负责，Core 仅负责 reasoning 字段的长度截断。

GUARDIAN 在 D2-R3 通过后正式声明："D5 的让步条件已兑现。我不再保留重新审议 $\pm 0.05$ 限幅的权利。"此声明标志着自 Cycle 02-4 以来围绕信心度调整安全性的持续性争议正式终结。

---
# 第三章：四维品质向量 —— 认知回路的量化评估框架

---

## 3.1 问题定义：认知回路品质的可观测性

OpenStarry 的 AI Agent 运作于一个认知回路（cognitive loop）中：接收感官输入（sparsha）→ 形成感受（vedana）→ 辨识（samjna）→ 造作行动（samskara）→ 判断与路由（manas/vijnana）→ 接收下一轮输入。`ILoopQualityMonitor` 的设计目标是对此回路的运作品质进行即时量化评估。

核心设计挑战在于：品质是一个多维概念。单一指标（如成功率）无法捕捉回路运作的全貌。WIENER（#12）与 ATHENA（#5，AI/ML 系统架构专家）带领团队设计了一个四维品质向量（LoopQualityVector），经 D3-R1（20/20 全票）确认。

---

## 3.2 四维公式的定义与语义

设滑动窗口大小为 $W$（预设值 $W = 10$），暖机期阈值为 $W_{warmup}$（预设值 $W_{warmup} = 5$）。四个维度的计算公式如下：

### 3.2.1 一致性（Coherence）

$$\text{coherence} = 1 - \frac{\text{switchCount}}{W - 1}$$

其中 $\text{switchCount}$ 为窗口内齿轮切换（gear switch）的次数。

**语义**：衡量 Agent 的路由决策是否稳定。高一致性表示 Agent 持续在同一处理模式下运作；低一致性表示 Agent 在不同模式间频繁切换，可能表征决策混乱或任务边界模糊。

**输入事件**：`gear:switch`

### 3.2.2 效率（Efficiency）

$$\text{efficiency} = \frac{\text{success}}{\text{proposed}} \quad (\text{若 proposed} = 0, \text{则} = 1.0)$$

其中 $\text{success}$ 为窗口内工具调用成功次数，$\text{proposed}$ 为工具调用提议次数。

**语义**：衡量 Agent 的动作执行成功率。效率为 1.0 表示所有提议的动作均成功执行；接近 0 表示大量动作失败，可能指向工具选择错误或环境变化。

**输入事件**：`action:proposed`, `tool:result`

**退化处理**：若无 proposed 事件，效率预设为 1.0（乐观假设：未提议动作 = 不需要动作 = 无失败）。

### 3.2.3 收敛性（Convergence）

$$\text{convergence} = \frac{\text{longestStreak}}{W}$$

其中 $\text{longestStreak}$ 为窗口内最长连续成功序列的长度。

**语义**：衡量 Agent 是否正在趋近稳定状态。高收敛性表示 Agent 已找到有效策略并持续成功；低收敛性表示成功与失败交替出现，Agent 尚未收敛到稳定行为模式。

与效率的区别在于：效率衡量"总量"，收敛性衡量"趋势"。窗口内 8 次成功若集中在最后 8 次（收敛性 = 0.8），其意义不同于散布在窗口各处（收敛性可能仅为 0.3）。

**输入事件**：`gear:switch`（同一致性）

### 3.2.4 稳定性（Stability）

$$\text{stability} = 1 - \min\left(1, \frac{\sigma^2}{0.25}\right)$$

其中 $\sigma^2$ 为窗口内信心度值的方差（variance）。分母 0.25 为理论最大方差（$[0,1]$ 区间上均匀分布的方差为 $1/12 \approx 0.083$，但取 0.25 以提供更宽松的正规化基准）。

**语义**：衡量仲裁器信心度输出的稳定性。高稳定性表示 Agent 的决策确信程度一致；低稳定性表示信心度剧烈波动，可能指向决策策略的不确定性。

**输入事件**：`gear:arbiter_evaluated`

---

## 3.3 复合品质分数

四维分数加权聚合为复合品质分数 $Q$：

$$Q = \sum_{i=1}^{4} w_i \cdot d_i, \quad Q \in [0, 1]$$

Phase 1 权重配置为等权重：$w_i = 0.25, \quad \forall i \in \{1,2,3,4\}$。

等权重选择的理论依据来自 PASCAL（#19，决策理论与概率哲学专家）的最大熵论证（maximum entropy argument）：

> 在缺乏先验知识支持任何维度具有更高重要性的情况下，最大熵原则（principle of maximum entropy）要求我们将概率质量（此处为权重）均匀分配给所有可能性。此为 Jaynes (1957) 所建立的贝叶斯推理框架的直接推论。

D3-R4（20/20 全票）确认：
- Phase 1：固定等权重 $0.25 \times 4$
- Phase 2：可配置权重，在 monitor plugin config 中定义
- 三组预设配置：balanced（均衡）、stability-focused（稳定性优先）、efficiency-focused（效率优先）

---

## 3.4 滑动窗口与暖机期

所有四维计算均在一个固定大小的滑动窗口（sliding window）中进行：

| 参数 | 值 | 理由 |
|------|-----|------|
| $W$ | 10 | 在敏感度与稳健性之间取得平衡 |
| $W_{warmup}$ | 5 | 收集到至少 5 个事件后才开始输出品质分数 |
| $Q_{default}$ | 0.5 | 暖机期内的预设品质分数（中性值） |

窗口大小的选择遵循以下考量：
- $W$ 过小（如 3-5）：对随机波动过度敏感，可能产生虚假警报
- $W$ 过大（如 50-100）：反应迟钝，Agent 已陷入困境时仍显示正常品质
- $W = 10$：提供约 2-3 个认知回路周期的历史视野，足以识别趋势而不过度延迟

暖机期的设置确保了统计显著性：在样本量不足时不做推断，避免因小样本偏差导致的错误品质评估。

---

## 3.5 计算复杂度

所有四维计算的时间复杂度为 $O(1)$ per event（每个事件到来时的增量更新），空间复杂度为 $O(W)$（仅需维护窗口大小的环形缓冲区）。

这一复杂度约束确保品质监控不会成为认知回路的性能瓶颈。

---

## 3.6 EventBus 事件订阅方案

HERACLITUS（#15，运行时动态专家）与 TURING（#17，源代码分析专家）设计了两阶段的事件订阅方案（D3-R2，20/20 全票）：

**Phase 1（6 事件，最小可行集）**：

| 事件 | 用途 |
|------|------|
| `gear:arbiter_evaluated` | 稳定性（信心度值） |
| `gear:switch` | 一致性 + 收敛性（齿轮切换） |
| `action:proposed` | 效率（提议数） |
| `tool:result` | 效率（成功数） |
| `loop:started` | 窗口管理（回路边界） |
| `loop:finished` | 窗口管理（回路边界） |

**Phase 2（+5 事件，精细化指标）**：

`sparsha:contact`, `tool:error`, `tool:blocked`, `vitakka:stall`, `action:executed`

**退化原则**（HERACLITUS 提出）：

> "缺失是信息，不是错误。"（Absence is information, not error.）

若某事件在运行时不存在（例如 Plugin 未订阅该事件），监控器不抛出异常，而是使用安全预设值：效率预设为 1.0（无失败假设），稳定性预设为 0.5（中性假设）。

同时，D3-R2 决议还包含一项重要的技术卫生措施：将散布在代码中的事件字符串字面量统一提升为 `AgentEventType` 常量，以消除拼写错误风险。

---
# 第四章：双通道整合架构 —— Layer 2/3 的正交分离设计

---

## 4.1 决策机制的形式化描述

OpenStarry 的核心路由决策可形式化为一个阈值比较：

$$\text{route} = \begin{cases} \text{arbiter\_gear} & \text{if } c > \theta \\ \text{default\_gear} & \text{otherwise} \end{cases}$$

其中 $c$ 为仲裁器（arbiter）对其推荐方案的信心度（confidence），$\theta$ 为系统阈值（threshold）。

Cycle 02-6 引入的两个新元件需要介入此决策过程：
- **IConfidenceAuditor**（Layer 2）：对 $c$ 进行微调
- **ILoopQualityMonitor**（Layer 3）：对 $\theta$ 进行微调

核心设计问题在于：如何让两者同时生效而不互相干扰？

---

## 4.2 三个候选方案

团队在 R1 阶段（报告 A4）评估了三个整合方案：

**方案 A：串联模式。** 品质分数 $Q$ 先修改阈值，然后审计员在修改后的阈值下评估信心度。两者存在序列依赖。

**方案 B：耦合模式。** 品质分数 $Q$ 同时影响信心度和阈值，审计员也同时影响信心度和阈值。两者存在交叉项。

**方案 C：正交模式。** 审计员仅修改信心度，品质监控器仅修改阈值。两条通道完全独立，无交叉项。

D2-R4（20/20 全票）选择方案 C。以下为详细的技术分析。

---

## 4.3 方案 C 的形式化定义

### Layer 2：信心度调整

$$c_{adj} = c_{raw} + \text{clamp}(\Delta c, -0.05, +0.05)$$

其中 $\Delta c$ 为审计员建议的调整量，$\text{clamp}$ 函数将其限制在 $[-0.05, +0.05]$ 区间内。

### Layer 3：阈值调整

$$\theta_{adj} = \max\left(\theta_{floor}, \; \theta_{base} \times (1 - \alpha \cdot Q)\right)$$

其中：
- $\theta_{base}$：基础阈值（经 Layer 1 Klesha 调整和 Layer 4 Vedana 紧急调整后的值）
- $\alpha = 0.10$：品质影响系数
- $Q \in [0, 1]$：复合品质分数
- $\theta_{floor}$：阈值下限（安全地板值，防止阈值被调至过低）

### 最终路由

$$\text{route} = \begin{cases} \text{arbiter\_gear} & \text{if } c_{adj} > \theta_{adj} \\ \text{default\_gear} & \text{otherwise} \end{cases}$$

---

## 4.4 方案 C 的设计优势分析

### 4.4.1 正交性（Orthogonality）

两条通道的作用域严格分离：Layer 2 仅操作 $c$，Layer 3 仅操作 $\theta$。不存在交叉项，即不存在 $f(c, Q)$ 或 $g(\theta, \Delta c)$ 形式的耦合函数。

此正交性的工程意义在于：两个元件可以独立开发、独立测试、独立部署。审计员的变更不影响品质监控的行为，反之亦然。

### 4.4.2 BIBO 稳定性

BABBAGE 的形式化验证：

设系统输入为 $(c_{raw}, \theta_{base}, Q)$，输出为路由决策。

- $c_{adj}$ 有界：$c_{raw} \in [0,1]$，$|\Delta c| \leq 0.05$，故 $c_{adj} \in [-0.05, 1.05]$，实际被 $[0,1]$ 夹持
- $\theta_{adj}$ 有界：$\theta_{base} \in [0,1]$，$\alpha \cdot Q \in [0, 0.10]$，故 $\theta_{adj} \geq \theta_{floor} > 0$

因此系统对任意有界输入产生有界输出，满足 BIBO 稳定。由于不存在交叉项，不存在通道间的正反馈放大路径。

### 4.4.3 可控性（Controllability）

每条通道均有明确的限幅（saturation）：
- Layer 2：$\pm 0.05$（每次路由）
- Layer 3：$\alpha = 0.10$（品质影响系数固定）

这意味着即使审计员或品质监控器的内部逻辑出现异常，其影响被严格限制在已知的范围内。

### 4.4.4 保守退化（Conservative Degradation）

- 若无审计员：$\Delta c = 0$，$c_{adj} = c_{raw}$
- 若无品质监控器：$Q = 0$，$\theta_{adj} = \theta_{base}$

任一元件缺失时，系统行为等价于该元件不存在的版本。不存在因元件缺失而导致的安全性降级。

---

## 4.5 品质分数的传输机制：Pull + Push 双通道

品质监控器产出的分数需要到达两个消费者，其需求特征不同：

| 消费者 | 需求 | 传输模式 |
|--------|------|---------|
| `ManoAggregator`（Layer 3） | 即时数值，用于阈值计算 | Pull：`loopQualityFn()` 回调 |
| `IConfidenceAuditor`（Layer 2） | 丰富背景信息，用于审计判断 | Push：extras bag via `audit:context_contribute` |

**Pull 通道**：`ManoAggregator` 在执行路由决策前，调用注入的 `loopQualityFn()` 回调函数。品质监控器返回最新的复合品质分数 $Q$。此通道的延迟为函数调用级别（microseconds）。

**Push 通道**：品质监控器通过 SDK `emitWithExtras()` 同时发出两个事件：
1. `loopQuality:updated` —— 供 `ManoAggregator` 缓存最新值
2. `audit:context_contribute` —— 将四维向量和复合分数写入 extras bag

Push 通道写入的键值对：
- `loopQuality:vector` → `{ coherence, efficiency, convergence, stability }`
- `loopQuality:composite` → $Q$

**生命周期**：per-routing-cycle。每次路由结束后，extras bag 清空。LEIBNIZ（#14）特别强调此设计的重要性：品质信息不跨路由周期累积，避免过时信息影响后续决策。一个 tick 的延迟被认为可接受，因为品质本身是历史指标而非即时指标。

---

## 4.6 五层决策模型

将 Layer 2/3 置入完整的决策流程语境中，OpenStarry 的路由决策形成一个五层模型：

```
L0: EventBus          -- 基础事件流（所有信号的传输层）
L1: Klesha（烦恼）     -- 四个情绪模块（moha, raga, dvesha, mana）调整阈值
L4: Vedana Emergency   -- 紧急感受直接降低阈值（安全关键）
L3: LoopQuality        -- 品质分数微调阈值（α=0.10）
L2: Audit              -- 审计员微调信心度（±0.05）
→ 最终比较: c_adj > θ_adj → 路由决策
```

Layer 顺序的设计遵循 **优先级递减** 原则：
- L4（Vedana Emergency）处理安全关键情境，优先级最高
- L1（Klesha）处理系统情绪状态的长期影响
- L3（LoopQuality）处理认知回路的运作品质
- L2（Audit）处理个案级别的信心度微调

此五层模型的完整性是 Plan30 的成功标准：Model Delta L0~L4 全部必须有实际信号路径，以整合测试验证。

---

## 4.7 多监控器与过期处理

方案 C 同时定义了两个边际情境的处理策略：

**多监控器聚合**：若系统中存在多个 `ILoopQualityMonitor` 实例（例如不同 Plugin 各自提供品质评估），Phase 1 采用简单平均（simple average）聚合。未来 Phase 2 可探索悲观聚合（pessimistic aggregation，取最低分）等策略。

**监控器过期**：若监控器超过 5000ms 未更新品质分数，其输出视为过期（expired），不参与聚合。过期监控器的效果等同于不存在：$Q = 0$，L3 不生效。

---
# 第五章：心所命名指示的三轮精化 —— 从论典产物到命名解耦

---

## 5.1 指示的触发脉络

在 R2 交叉审阅阶段，ASANGA 的唯识心所批判报告（C2）被提交至 DC Master 进行审阅。Master 对心所（cetasika）与 Plugin 之间的命名与归属关系做出了三轮连续性指示，每轮指示在前一轮基础上递进深化。

此三轮精化过程发生在 R2 至 R3 的过渡期间，其产出直接影响了 D1 辩论的议程修订：D1-Q2（心所多蕴归属议题）被删除，D1-Q6（逐条投票 26 项心所归属）被简化为蕴归属原则投票。

---

## 5.2 第一轮指示：经典与论典的区分

Master 的第一轮指示建立了一个根本性的文献学区分：

> 心所是论典（Abhidharma）的产物，非原始经典（Sutta/Agama）的内容。

此区分的学术依据如下：佛陀在原始经典（如《杂阿含经》SN 22.56、《中部》MN 44 等）中阐述了五蕴（panca-skandha）、十二因缘（pratityasamutpada）、八正道（arya-astangika-marga）等核心教义架构。然而，系统化的五十一心所分类体系是后世论典学者（主要为无著/Asanga 与世亲/Vasubandhu 的唯识学派，以及说一切有部/Sarvastivada 的七十五法体系）在佛陀入灭后数百年间逐步建构的。

Master 由此得出的直接结论：**Plugin 的命名不得使用心所的梵文名称。**

---

## 5.3 第二轮指示：功能描述的参考价值

第二轮指示在第一轮的否定性判断基础上，补充了肯定性判断：

> 心所的功能描述具有参考价值，可作为 Plugin 设计的灵感来源。

此指示承认了论典学术传统的贡献。例如，心所"精进"（virya）描述了"持续不懈地投入善法"的功能特征。此功能描述可以启发一个负责重试逻辑的 Plugin 设计 —— 但该 Plugin 应命名为 `PersistencePlugin` 或 `RetryPlugin`，而非 `VīryaPlugin`。

Master 给出的表述规范：

- **允许**："参考精进（virya）的涵义，设计了重试 Plugin"
- **禁止**："重试 Plugin = 精进"

此区分的方法论意义在于：它在"借鉴"（reference）与"等同"（identification）之间划定了明确界线。前者保留了跨传统对话的可能性，后者则会导致不当的概念锁定。

---

## 5.4 第三轮指示：命名解耦与归属自由

第三轮指示是最具系统性影响的。Master 明确宣告：

> Plugin 不等于心所（plugin ≠ cetasika）。

此宣告的逻辑推论如下：

**前提一**：在唯识心所系统中，每个心所具有固定的蕴归属 —— 例如"精进"（virya）固定属于行蕴，"慧"（prajna）固定属于识蕴（在某些分类中）。

**前提二**：若 Plugin = 心所，则 Plugin 的蕴归属亦被心所系统的固定归属所决定。

**前提三**：但 Plugin ≠ 心所。

**结论**：Plugin 的蕴归属不受心所系统的固定归属约束。一个 Plugin 可以同时具有行蕴功能（WRITE —— 执行动作、改变环境）和识蕴功能（READ —— 评估情况、做出判断），而不产生任何逻辑矛盾。

Master 以一句话概括此结论的系统性意义：

> "命名解耦带来归属自由。"（Naming decoupling brings attribution freedom.）

---

## 5.5 八点永久性规则

三轮指示经整理后形成八条永久性规则，经团队确认并纳入永久性规范框架：

| # | 规则 | 性质 |
|---|------|------|
| 1 | 心所是论典产物，非原始经典内容 | 文献学判定 |
| 2 | 心所的功能描述具有参考价值，可作为 Plugin 设计灵感 | 肯定性保留 |
| 3 | 可说明参考来源："参考某某心所的涵义，设计某某 Plugin" | 表述规范 |
| 4 | Plugin 必须使用工程术语命名，不得使用心所梵文名 | 命名规范 |
| 5 | 梵文术语限于原始经典者（skandha、sparsha 等） | 术语范围 |
| 6 | 心所分类不作为蕴归属依据 | 归属原则 |
| 7 | 既有 Plugin 归属决议（基于功能分析）不受影响 | 稳定性保证 |
| 8 | Plugin ≠ 心所，蕴归属可自然跨多蕴 | 跨蕴自由 |

---

## 5.6 与蕴归属五原则的互补关系

八点规则与第一章所述的蕴归属五项永久性原则（D1-R6）形成互补结构：

| 方面 | 蕴归属五原则 | 八点规则 |
|------|------------|---------|
| 来源 | 研究团队归纳 | DC Master 指示 |
| 焦点 | 归属判定方法 | 命名与术语规范 |
| 核心主张 | 功能分析为唯一依据 | Plugin ≠ 心所，命名解耦 |

两套规则共同构成了 OpenStarry 未来所有命名与归属问题的完整判定框架。其效力为永久性（permanent），不因特定研究周期的结束而失效。

正如 NAGARJUNA 所言："Cycle 02-5 我们学会了什么不该做（移除装饰性映射）。Cycle 02-6 我们学会了为什么不该做（论典归属不等于功能归属）。"

---

## 5.7 对 D1 议程的影响

Master 心所指示直接导致了 D1 辩论议程的三项修订：

1. **D1-Q2（心所多蕴归属）删除**：既然心所分类不作为归属依据，讨论心所的多蕴归属问题失去意义。
2. **D1-Q6（逐条投票 26 项心所归属）简化**：不再逐条投票个别心所的归属，改为投票确认蕴归属原则本身。
3. **manasikara（作意）追加议题取消**：manasikara 在 `CoarisingBundle` 中已有处理，非独立接口，无需额外讨论。

这些议程修订体现了 Master 指示的方法论影响：它将讨论从"个案判定"层面提升到"原则建立"层面，大幅提高了辩论效率。

---
# 第六章：辩论过程的方法论分析 —— 从冲突驱动到共识确认

---

## 6.1 与 Cycle 02-5 的结构性对比

Cycle 02-5 与 02-6 的辩论过程呈现出显著的结构性差异：

| 指标 | Cycle 02-5 | Cycle 02-6 | 变化 |
|------|-----------|-----------|------|
| 辩论场次 | 5 | 3 | -40% |
| 决议总数 | 29 | 17 | -41% |
| 全票通过（20/20） | ~20 (~69%) | 13 (76%) | +7pp |
| 否决数 | 0 | 0 | -- |
| Master 覆议 | 2 | 0 | -100% |
| 总辩论时间 | ~400 min（估计） | ~245 min | -39% |

DARWIN（#6，软件模式分析师）对此差异提出了一个结构性解释：

> "Cycle 02-5 是正确性辩论（correctness debate）—— 争议焦点在于什么是对的、什么是错的。Cycle 02-6 是规格辩论（specification debate）—— 争议焦点在于对的东西应该长什么样子。后者天然更容易达成共识，因为不涉及价值判断，而是工程规格的精确化。"

SUNYATA 的补充分析指向 R1（独立研究）阶段的品质：14 份独立研究报告在 R2 交叉审阅中产生了 24 个共识点，仅 3 个分歧点。当 87.5% 的议题在辩论前已有共识，辩论的功能从"从零开始的争论"转变为"共识的确认与精化"。

---

## 6.2 D1：行蕴深掘辩论（约 75 分钟，7 项决议）

D1 是本轮的哲学辩论，依据跨轨道影响协议优先于 D2/D3 进行。

### D1-R1（20/20）：行蕴核心定义

确认三个核心特质：cetana 中心性（SN 22.56）、造作功能（SN 22.79）、无核心过程（SN 22.95）。无反对意见。哲学轨的经典学研究过于扎实，直接引用原始经典文本，未留下可辩论的模糊空间。

### D1-R3（20/20）：ISamskara 拓展方向

确认不新增子接口（延续 02-5 D3-R4 的 20/20 全票决议）。四个拓展方向存档为长期候选：

| 方向 | 描述 | 优先级 | 时程 |
|------|------|--------|------|
| A | 意图规划（cetana-formation） | P2 | Cycle 03+ |
| B | 习气形成（vasana-imprinting） | P2 | 长期 |
| C | 环境转换（kaya extension） | P3 | 无需排程 |
| D | 沟通形成（vaci） | P3 | 无需排程 |

行蕴属性判定三准则确认为永久性工具。

### D1-R4a（19/20）：认知序列附录

认知序列（citta-vithi）附录排程至 Cycle 02-7（P2 优先级）。一票反对认为可在本轮完成，但多数认为当前周期的工程任务优先。

### D1-R4b（18/20）：四智排除

四智（catvari-jnanani）—— 大圆镜智（adarsa-jnana）、平等性智（samata-jnana）、妙观察智（pratyaveksana-jnana）、成所作智（krtyanusthana-jnana）—— 正式排除出架构映射候选。

排除依据为四项测试（均失败）：
1. 移除四智映射不改变任何现有设计
2. 四智不出现在代码中
3. 四智未驱动任何工程决策
4. 四智不对应任何已有接口

两票反对认为四智可保留作为附录参考，但多数认为排除更为干净。

### D1-R4c（20/20）：心智论述综合评估表

确认 C4 报告的评估结论：

| 论述 | 状态 | 后续行动 |
|------|------|---------|
| 五蕴（panca-skandha） | 已完成融入 | 无需行动 |
| 名色识（nama-rupa-vijnana） | 核心价值已吸收 | 无需行动 |
| 十二因缘（pratityasamutpada） | 解释性附录候选 | 02-7 P2 |
| 八识（asta-vijnana） | 待多 Agent 场景 | Cycle 03+ |
| 四智（catvari-jnanani） | 排除 | D1-R4b |
| 认知序列（citta-vithi） | 最强结构对应 | 02-7 P2 |

### D1-R5（20/20）：活动与转换原则

确认 WRITE/READ 二分法。行蕴 = WRITE（主动改变）、识蕴 = READ（被动评估）。三准则同步确认。

### D1-R6（20/20）：蕴归属五项永久性原则

全票通过。详见第一章 1.7 节。

**跨轨道影响评估**：D1 结论对 D2/D3 均无需追加议题。哲学发现与工程设计正交。

---

## 6.3 D2：AuditContext 辩论（约 85 分钟，5 项决议）

### D2-R1（20/20）：AuditContext 接口

确认完整类型定义（详见第二章 2.3 节）。sparshEvent 为 required，historicalConfidence 预设 10 可配置。

### D2-R2（19/20）：extras bag 协议

确认双事件模式 + SDK helper + key 标准化 + 浅冻结 + max 32 keys。一票反对认为双事件模式过度设计。

此为 R2 阶段识别的三项分歧之一（extras 写入协议：A2 通用事件 vs B3 直接订阅），在辩论中正式解决。

### D2-R3（20/20）：ConfidenceAuditLog

确认完整审计日志类型。GUARDIAN 当场宣布 D5 让步条件兑现（详见第二章 2.7 节）。

### D2-R4（20/20）：Layer 整合方案 C

确认双通道正交设计（详见第四章）。R2 阶段的第二项分歧（extras key 命名）与第三项分歧（loopQualityFn 数据来源）在此决议中一并解决。

### D2-R5（20/20）：Auditor 策略三阶段

确认分阶段实施方案：

| Phase | 实作 | 功能 | 时程 |
|-------|------|------|------|
| Phase 0 | `PassthroughAuditor` | delta=0，纯日志记录 | Plan30（可选） |
| Phase 1 | `ThresholdAuditor` | 规则式信心度调整 | Plan31 |
| Phase 2 | LLM-assisted Auditor | LLM 辅助审计 | 长期 |

ARCHIMEDES（#16，工程实践专家）对 Phase 0 的价值论述：PassthroughAuditor 的功能不在于审计本身（它不做任何调整），而在于端对端管道验证 —— 它证明从 AuditContext 组装、到审计函数调用、到 ConfidenceAuditLog 记录的完整管道是通畅的。

---

## 6.4 D3：LoopQualityMonitor 辩论（约 85 分钟，5 项决议）

### D3-R1（20/20）：四维公式

确认一致性、效率、收敛性、稳定性四维公式（详见第三章 3.2 节）。$W=10$，$W_{warmup}=5$，$Q_{default}=0.5$。

### D3-R2（20/20）：EventBus 事件订阅

确认 Phase 1 六事件 + Phase 2 五事件 + AgentEventType 常量提升（详见第三章 3.6 节）。

### D3-R3（20/20）：extras 写入生命周期

确认 D2-R2 通用管道 + loopQualityFn 双通道。per-routing-cycle 生命周期，一 tick 延迟可接受。Phase 1 多监控器采用 last-emitted-wins 策略。

### D3-R4（20/20）：权重策略

确认 Phase 1 固定等权重 $0.25 \times 4$。PASCAL 的最大熵论证（详见第三章 3.3 节）获得全票支持。

### D3-R5（19/20 + 1 条件赞成）：Plan30 方向

此为本轮唯一一项包含"条件赞成"（conditional approval）的决议。

GUARDIAN 的条件："Plan30 的 Wave 3 必须包含 ConfidenceAuditLog 的 SDK 类型定义。此类型定义不得延后至 Plan31。"

条件被团队接纳。GUARDIAN 转为赞成。

此条件的背景在于 GUARDIAN 对安全相关类型定义的持续关注：审计日志的类型定义是安全基础设施的一部分，应尽早固化，不应与具体审计逻辑的实作绑定。

---

## 6.5 零否决的方法论解释

17 项决议全部通过（0 否决）的结果可从三个层面解释：

**第一，R1 品质效应。** 14 份独立研究报告的品质使得 R2 交叉审阅仅识别出 3 个分歧点。辩论开始时，大部分问题已有共识基础。

**第二，辩论性质转变。** 从正确性辩论（02-5）到规格辩论（02-6），分歧空间缩小。规格辩论的分歧通常可通过技术论证解决，而非价值判断。

**第三，跨轨道协议的有效性。** 哲学轨（D1）先于工程轨（D2/D3）完成，确保了框架性问题在具体设计之前已经定案。D1 的七项决议为 D2/D3 提供了稳定的概念基础，消除了潜在的框架级分歧。

---
# 第七章：工程蓝图与研究总结 —— Plan30 规格与 Cycle 02-6 的学术贡献

---

## 7.1 Plan30 工程规格

十七项决议定案后，VITRUVIUS（#3，全端架构分析师）与 ARCHIMEDES（#16）将所有规格整理为 Plan30 —— 下一步工程实作的完整设计蓝图。D3-R5（19/20 + 1 条件赞成）确认了以下四波次结构：

| Wave | 内容 | 估计代码量 | 关键技术点 |
|------|------|------------|-----------|
| W1 | Default LoopQualityMonitor Plugin | ~120 LOC | 四维公式实作、6 事件订阅、O(1)/event 增量更新 |
| W2 | Layer 3 布线（方案 C） | ~80 LOC | `loopQualityFn()` 回调注入、$\theta_{adj}$ 计算、$\alpha=0.10$ |
| W3 | 类型定义与事件常量 | ~60 LOC | `ConfidenceAuditLog` SDK 类型、`AgentEventType` 常量提升、extras 事件定义 |
| W4（可选） | PassthroughAuditor | ~30 LOC | delta=0 直通审计、纯日志记录、端对端管道验证 |

**总计**：~260-290 行生产代码 + ~130 行测试代码，合计不超过 420 行。

**成功标准**：Model Delta 五层（L0~L4）全部具有实际信号路径，以整合测试验证。具体而言，Plan30 完成后：
- L0（EventBus）：品质监控器订阅的 6 个事件均有实际发出方
- L1（Klesha）：既有，不在 Plan30 范围内
- L3（LoopQuality）：`loopQualityFn()` 回调已接入 `ManoAggregator`
- L2（Audit）：`ConfidenceAuditLog` 类型已定义，`PassthroughAuditor`（若 W4 实施）验证管道通畅
- L4（Vedana Emergency）：既有，不在 Plan30 范围内

---

## 7.2 Plan31 展望

Plan30 之后的下一步工程计划 Plan31 将完成审计管道的端对端落地：

| 元件 | 内容 | 估计代码量 |
|------|------|------------|
| AuditContext 组装 | Core 在每次路由时组装完整 AuditContext | ~120 LOC |
| Default ThresholdAuditor | Phase 1 规则式审计员（非 delta=0 的直通审计） | ~100 LOC |
| Audit Trail JSONL | 审计日志的 JSONL 文件持久化 | ~130 LOC |

总计约 350 行代码。Plan30 建造管道基础设施，Plan31 让审计逻辑真正流经管道。

---

## 7.3 Cycle 02-7 研究展望

### P0 延续项
- Plan31 规格研究与工程交付追踪

### P1 待研究
- **Lyapunov 稳定性参数校准**：$\alpha$ 值的理论验证与稳态分析
- **Moha/Sneha 耦合模拟**：烦恼模块间的交互影响
- **多监控器聚合策略验证**：简单平均 vs 悲观聚合的比较分析

### P2 附录
- 认知序列（citta-vithi）附录 → Doc 01
- 十二因缘（pratityasamutpada）附录

### 延后至 Cycle 03+
- 八识深化（alaya-vijnana 在多 Agent 场景中的应用）
- VasanaEngine（D-29-8 决议的长期实作）
- ISamskara 方向 A/B（意图规划 / 习气形成子接口）

---

## 7.4 成功标准达成状态

Cycle 02-6 设定了 9 项成功标准，全部达成：

| # | 标准 | 达成决议 |
|---|------|---------|
| 1 | AuditContext 完整类型定义 | D2-R1 (20/20) |
| 2 | 审计日志格式规格（GUARDIAN D5 条件兑现） | D2-R3 (20/20) |
| 3 | LoopQualityVector 四维公式 | D3-R1 (20/20) |
| 4 | EventBus 事件订阅清单 | D3-R2 (20/20) |
| 5 | OQ-29 全部回答（6/6） | 分散于各决议 |
| 6 | Plan30 方向建议 | D3-R5 (19+1) |
| 7 | 行蕴深掘报告 | C1-C4 + D1 |
| 8 | 心所逐条蕴归属建议（51 项） | C2 |
| 9 | 无范围蔓延（scope creep） | Lyapunov/Moha/FC-26 均未讨论 |

---

## 7.5 Cycle 02-6 的学术贡献总结

### 7.5.1 哲学贡献

**行蕴的经典学重构。** 本轮研究从原始经典（SN 22.56, SN 22.79, SN 22.95, MN 44, SN 12.2）重新建立了行蕴的功能性定义，以 cetana（意图/意志）为中心，取代了唯识学派的"剩余类别"处理方式。三个核心特质（cetana 中心性、造作功能、无核心过程）和 WRITE/READ 二分法构成了一个在佛学与计算机科学之间具有高度一致性的概念框架。

**唯识心所系统的批判性分析。** ASANGA 对 51 个心所的逐一检视揭示了唯识归属方案的系统性偏差：仅 14% 的被归入行蕴之心所在功能分析下确属行蕴。此分析为功能分析优先于传统分类的方法论立场提供了量化支持。

**永久性判定框架的建立。** 蕴归属五原则与 Master 八点规则共同构成了一个自洽的、可操作化的判定框架，适用于 OpenStarry 未来所有的命名与归属问题。此框架的核心洞见 —— "命名解耦带来归属自由"—— 具有超越 OpenStarry 项目本身的方法论价值：在任何跨传统（佛学 / 计算机科学）的概念映射中，保持命名的独立性是避免概念锁定的关键。

### 7.5.2 工程贡献

**AuditContext 类型设计。** 解决了审计员信息贫乏问题的同时，通过 WIENER 三约束系统性地切断了正反馈回路。BIBO 稳定性的形式化验证为设计提供了控制理论的理论保证。

**四维品质向量。** 以最大熵原则为理论依据的等权重四维公式，在 $O(1)$ 计算复杂度下提供了认知回路品质的多维度量化评估。退化处理（缺失事件 → 安全预设值）确保了系统的鲁棒性。

**方案 C 双通道架构。** Layer 2（信心度调整）与 Layer 3（阈值调整）的正交分离设计，实现了可证明的 BIBO 稳定性、保守退化、独立可测试性，以及与既有 Layer 0/1/4 的无缝整合。

### 7.5.3 方法论贡献

**跨轨道影响协议。** 哲学结论先于工程设计的约束确保了概念框架的稳定性，避免了工程决策在不稳定的哲学基础上进行。

**条件赞成机制。** D3-R5 中 GUARDIAN 的条件赞成展示了一种在完全赞成与完全反对之间的中间态决策机制，使得安全关切可以在不阻塞整体进度的情况下获得具体的承诺。

---

## 7.6 结语：从减法到加法

若以一个对偶结构概括 Cycle 02-5 与 02-6 的关系：

- **Cycle 02-5**（减法）：回答"什么是错的？"—— 装饰性佛学映射、命名不当、蕴归属混乱
- **Cycle 02-6**（加法）：回答"什么是对的？"—— cetana 中心定义、AuditContext 类型、四维品质公式、方案 C 双通道、永久性规则

02-5 清理了地基。02-6 画好了蓝图。Plan30 将开始建造。

二十位研究者。三场辩论。十七项决议。十三项全票通过。零项否决。零项 Master 覆议。

9/9 成功标准达成。

---

*Cycle 02-6 完。*

---
