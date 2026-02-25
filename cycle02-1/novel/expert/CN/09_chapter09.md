# 第九章：十九份行动方案

---

R4 定稿的圆形剧场，比辩论时安静得多。

不是那种空洞的安静——五场辩论的余波仍然在空气中振动，像大提琴的弦在最后一个音符结束后继续颤抖。但辩论的张力已经退去。取而代之的是另一种密度：交付的密度。十九位研究员各自坐在自己的座位上，面前摆着初稿、修订稿、代码片段、映射表。R4 不是辩论。R4 是收成。

在工程管理的术语中，R4 是**交付闸门**（Delivery Gate）——产品从研发流程进入交付管线的最后关卡。在软件开发生命周期（SDLC）中，这个闸门的意义是明确的：

$$	ext{Gate}_{R4} : 	ext{Research} 	o 	ext{Deliverable} \quad \iff \quad \forall \, d_i \in 	ext{Decisions}, \; \exists \, a_i \in 	ext{Actions} : 	ext{trace}(a_i) = d_i$$

每一项辩论裁定（$d_i$）都必须有对应的行动方案（$a_i$），且行动方案必须可追溯回裁定本身。ARCHIMEDES 在他的笔记本上写的第一行就是这个公式——追溯性（traceability）是工程交付的基本纪律。

SUNYATA 站在场地中央，环顾全场。他已经不需要宣布什么了——每个人都知道该做什么。R3 的五场共识像五根柱子，支撑起了一个可以在其中工作的结构。现在的任务是把辩论的裁定转化为可交付的文件，把哲学的洞见翻译为工程师能读懂的语言。

“ARCHIMEDES，”他说。“你先。”

---

## I. 明天我们需要写 TypeScript

ARCHIMEDES 从座位上站起来的方式和所有研究员都不同。

NAGARJUNA 站起来像一把出鞘的剑。ASANGA 站起来像一棵树在风中缓缓直立。BABBAGE 站起来像一台精密仪器被启动。ARCHIMEDES 站起来像一个建筑工人拿起了铲子——没有戏剧性，没有仪式感，只有一种“活儿来了，开工”的朴素动力。

“先说一句。”他走到展示区，打开了一份长达四十页的文件。“过去三天，你们在辩论中产出了五项裁定——观察-干预分离、双模式 vedana、纤维丛投影、渐进分类、戒慧框架。每一项都很美。每一项都让我作为旁听者感到智识上的愉悦。”

他停了一拍。

“但哲学很美，明天我们需要写 TypeScript。”

全场有几个人笑了。BABBAGE 的嘴角微微动了一下——那是他最接近大笑的表情。NAGARJUNA 没有笑，但他的眼神里有一种认可：一个懂得什么时候该把天上的东西带回地面的人，值得尊重。

ARCHIMEDES 指着展示区的投影。“这份文件的结构遵循 MoSCoW 优先级框架——Must、Should、Could、Won't。不过我把它映射到了更直观的命名：P0 阻塞性、P1 高优先、P2 标准、P3 未来、P4 远期。”

他在白板上画了优先级矩阵：

```
┌──────────────────────────────────────────────────────────────────┐
│                    MoSCoW → P-Level 映射                         │
├──────────┬─────────┬──────────────────────────────────────────────┤
│ MoSCoW   │ P-Level │ 语义                                        │
├──────────┼─────────┼──────────────────────────────────────────────┤
│ Must     │ P0      │ 阻塞性——不完成则无法开始其他工作              │
│ Should   │ P1      │ 高优先——本 Cycle 必须完成                     │
│ Could    │ P2      │ 标准——重要但可延后                            │
│ Won't    │ P3/P4   │ 未来/远期——记录但不在本次交付                 │
└──────────┴─────────┴──────────────────────────────────────────────┘
```

---

> *SCRIBE 旁白：ARCHIMEDES 是研究团队里唯一一个在辩论场上始终保持沉默的工程师。不是因为他没有意见——他的意见比任何人都具体。而是因为他的意见必须等到所有辩论结束之后才有意义。你不能在房子还在设计的时候就开始算水泥用量。但一旦设计定案，算水泥用量的人就是最重要的人。*

---

### P0：三件阻塞性工作

他从优先级最高的项目开始。

“P0——阻塞性。三件事。必须在任何其他工作开始之前完成。”

他举起一根手指。

“第一，SEC-01。修复 package-name 插件签名绕过漏洞。”他看了一眼 GUARDIAN。

GUARDIAN 站了起来。他的手里拿着一份标记为“CRITICAL”的安全报告——封面上的红色边框比其他任何文件都醒目。

“让我把这个漏洞的严重性用形式化语言说清楚。”

他走到白板前，写下了漏洞的精确位置和攻击路径：

```typescript
// [代码: packages/core/src/sandbox/sandbox-manager.ts#L371]
// v0.24.0-beta 现行代码（简化）

async verifyPlugin(plugin: IPlugin): Promise<VerificationResult> {
  const pluginFilePath = plugin.manifest?.filePath;

  if (!pluginFilePath) {
    // BUG: 当 pluginFilePath 为 undefined 时
    // 整个签名验证被跳过
    return { verified: true, reason: 'no-file-path' };  // ← 这里
  }

  // 正常的签名验证逻辑...
  return this.cryptoVerify(pluginFilePath, expectedSignature);
}
```

“攻击向量。”他在白板上画了一个攻击流程图：

```
攻击者行为：
┌──────────────────────────────────────────────────────────────────┐
│ 1. 建立一个恶意 Plugin，故意不提供 filePath                       │
│ 2. Plugin manifest: { name: "legit-plugin", filePath: undefined } │
│ 3. sandbox-manager.verifyPlugin() 被调用                          │
│ 4. pluginFilePath === undefined → 跳过签名验证                    │
│ 5. 返回 { verified: true } → 恶意 Plugin 被信任加载               │
│ 6. Plugin 获得完整的 ToolContext 存取权限                          │
│ 7. 可以存取 EventBus、StateManager、所有已注册的工具               │
└──────────────────────────────────────────────────────────────────┘
```

“在 CVSS v3.1 评分框架下：”

$$	ext{CVSS} = 	ext{Base}(	ext{AV:L}/	ext{AC:L}/	ext{PR:N}/	ext{UI:N}/	ext{S:C}/	ext{C:H}/	ext{I:H}/	ext{A:H}) = 9.8 \; (	ext{Critical})$$

“攻击向量是本地（AV:L）——需要存取插件目录。攻击复杂度低（AC:L）——只需省略一个字段。不需要权限（PR:N）。不需要用户互动（UI:N）。影响范围改变（S:C）——跳出沙箱边界。机密性、完整性、可用性全部高影响。”

他转身面向全场。“一个绕过签名的漏洞。每一天它不被修复，系统就多一天裸奔。六个开发周期了。仍然没修。”

GUARDIAN 接着展示了修复方案的代码：

```typescript
// 修复后的 verifyPlugin
async verifyPlugin(plugin: IPlugin): Promise<VerificationResult> {
  const pluginFilePath = plugin.manifest?.filePath;

  if (!pluginFilePath) {
    // FIX: 缺少 filePath = 无法验证 = 不信任
    logger.warn('Plugin verification failed: missing filePath', {
      pluginName: plugin.manifest?.name ?? 'unknown',
    });
    return {
      verified: false,
      reason: 'missing-file-path',
      severity: 'critical',
    };
  }

  return this.cryptoVerify(pluginFilePath, expectedSignature);
}
```

“三行修改。一个 `if` 条件的反转。但语义变化是根本性的——从‘无法验证等于信任’变成‘无法验证等于不信任’。这是安全工程的**失败安全原则**（fail-safe default）：

$$	ext{verify}(\bot) = 	ext{reject} \qquad (	ext{not} \quad 	ext{verify}(\bot) = 	ext{accept})$$

在密码学中，$\bot$（底值）代表缺少的或不可用的资讯。对 $\bot$ 的预设处理必须是拒绝。这是 Kerckhoffs 原则的推论——系统的安全性不应依赖于攻击者的善意。”

---

ARCHIMEDES 接手。“第二个 P0。”他举起第二根手指。“实作 ISensation 接口。”

他在展示区切换到一段代码。

```typescript
// v0.24.0-beta 现行的 ISensation
export interface ISensation extends IOpenStarryPlugin {
  readonly skandha: 'vedana';
}
```

“三行。一个空壳。”他的语气不带批判——只是陈述事实。“这是序章里的那个空壳。整个 Cycle 02 的研究，从某种意义上说，就是为了填充这三行。”

TURING 站了起来。他的屏幕投射了完整的 ISensation 接口——不是节录，不是简化版，而是经过五场辩论淬炼后的完整类型定义：

```typescript
/**
 * ISensation — 受蕴 Root Interface
 * @skandha vedana (受蕴)
 *
 * 受蕴涵盖三受 (三种感受)：
 * - Dukkha (苦): 负向回馈
 * - Sukha (乐): 正向回馈
 * - Upekkha (舍): 中性平衡
 *
 * 设计原则 (来自辩论裁定)：
 * - Debate 1: 感测与建议在同一接口，但概念分离
 * - Debate 2: 完整 PID 评估在 tick 边界，轻量标签随事件
 * - Debate 4: VedanaPlugin IS the Pattern A observer
 *
 * Sanskrit: Vedanā (वेदना)
 */
export interface ISensation {
  readonly skandha: 'vedana';

  /**
   * 评估当前三受状态 — 完整的 PID 感测读数
   *
   * 控制理论对应: y(t) = h(x(t)) + v(t)
   * 感测器读数函数。每个 tick 调用一次。
   *
   * @returns VedanaAssessment 含感测层 + 控制建议层
   */
  assess(): VedanaAssessment;

  /**
   * 摄取原始系统指标 — 通用数值输入通道
   *
   * 多输入感测器融合通道 1: 量化指标
   * (CPU, memory, latency, error rate...)
   */
  ingestMetrics(metrics: Record<string, number>): void;

  /**
   * 摄取工具执行结果 — 行蕴回报通道
   *
   * 多输入感测器融合通道 2: 离散事件
   * 十二因缘: 触(sparśa) → 受(vedanā)
   */
  ingestToolResult(toolName: string, isError: boolean, durationMs: number): void;

  /**
   * 摄取 LLM 回应结果 — 想蕴回报通道
   *
   * 多输入感测器融合通道 3: 语言模型元数据
   */
  ingestLLMResult(tokenCount: number, stopReason: string): void;

  /**
   * 订阅受蕴阈值事件 — 看门狗计时器泛化
   *
   * 经典看门狗: y(t) > T_timeout → alarm
   * 泛化版: v_type(t) > θ → handler(signal)
   */
  onThreshold(channel: VedanaType, threshold: number,
              callback: (signal: VedanaSignal) => void): () => void;

  /**
   * 取得受蕴标签 — O(1) 缓存查询
   *
   * 仪表板 LED 指示灯: 不计算，只读缓存
   * Debate 2 裁定: 每个事件附带的轻量标签来源
   */
  getVedanaTag(): VedanaTag;
}
```

TURING 让投影停了整整十秒。他指着每一个方法，声音平板而精确：

“每一个方法都可以追溯到辩论裁定。`assess()` 来自辩论 1 的 VedanaAssessment 双层结构——感测层加控制建议层。`getVedanaTag()` 来自辩论 2 的轻量事件标签裁定——$O(1)$ 缓存查询，不重新计算 PID。`onThreshold()` 是 WIENER 的三通道 PID 控制器需要的事件驱动订阅机制。三个 `ingest` 方法是多输入感测器融合三个通道。”

WIENER 从座位上微微前倾。他需要确认三通道 PID 的输出规格是否被正确翻译。

他拿出方格纸，在上面写下了验收公式：

$$	ext{VedanaAssessment} = \underbrace{\begin{pmatrix} d(t) \ s(t) \ u(t) \ \vec{\sigma}(t) \end{pmatrix}}_{	ext{Layer 1: Sensor}} \oplus \underbrace{\begin{pmatrix} u_{	ext{ctrl}}(t) \ r(t) \ f(t) \end{pmatrix}}_{	ext{Layer 2: Controller}}$$

“Layer 1 是感测器输出。$d(t)$, $s(t)$, $u(t)$ 是三通道 PID 的测量值——苦、乐、舍。$\vec{\sigma}(t)$ 是信号阵列——原始事件的时间戳和来源。纯观察。被动。不改变系统状态。”

“Layer 2 是控制器建议。$u_{	ext{ctrl}}(t)$ 是统合控制输出——三通道 PID 的加权和。$r(t)$ 是推荐动作——continue、reflect、restrict、halt。$f(t)$ 是新鲜度指示——current、cached、default。辩论 1 裁定：建议是咨询性的。ExecutionLoop 保留忽略的权力。”

他在方格纸上重重勾了一个勾。“翻译是准确的。”

---

ARCHIMEDES 切换到 VedanaAssessment 的完整 TypeScript 定义：

```typescript
/** 三受类型 */
type VedanaType = 'dukkha' | 'sukha' | 'upekkha';

/** 受蕴标签（轻量缓存，用于事件标记） */
type VedanaTag = 'dukkha' | 'sukha' | 'upekkha';

/** 受蕴信号 — 单一感受事件的记录 */
interface VedanaSignal {
  readonly type: VedanaType;
  readonly intensity: number;     // 0.0–1.0
  readonly source: string;        // e.g., 'tool:file_read', 'llm:timeout'
  readonly timestamp: number;     // Date.now()
}

/** 受蕴推荐动作 */
type VedanaRecommendation =
  | { action: 'continue' }
  | { action: 'reflect'; prompt: string }
  | { action: 'restrict'; tools: string[] }
  | { action: 'halt'; reason: string };

/**
 * VedanaAssessment — 受蕴评估报告
 *
 * 双层结构 (Debate 1 裁定):
 * - Layer 1: 感测器输出 (纯观察，被动)
 * - Layer 2: 控制建议 (咨询性，可被忽略)
 *
 * BABBAGE 的互模拟条件在 Layer 1 满足:
 * 只读取 Layer 1 的消费者行为不受 Layer 2 影响
 */
interface VedanaAssessment {
  // ── Layer 1: Sensor Output (pure observation) ──
  readonly dukkha: number;        // 0.0–1.0
  readonly sukha: number;         // 0.0–1.0
  readonly upekkha: number;       // 0.0–1.0
  readonly signals: readonly VedanaSignal[];
  readonly timestamp: number;

  // ── Layer 2: Controller Suggestion (advisory) ──
  readonly controlOutput: number;
  readonly recommendation: VedanaRecommendation;
  readonly recommendationFreshness: 'current' | 'cached' | 'default';
}
```

“双层——辩论 1 的核心裁定。”ARCHIMEDES 指着屏幕。“`readonly` 修饰符强制不可变性。`recommendationFreshness` 是 BABBAGE 在辩论尾声加入的——防止陈旧的 'halt' 建议在条件改善后仍然持续。”

BABBAGE 从笔记本中抬起头。他在确认自己的互模拟条件是否被完整保留：

$$\forall \, 	ext{consumer} \, C : C 	ext{ reads only Layer 1} \implies 	ext{Behavior}(S) \sim 	ext{Behavior}(S')$$

“互模拟在消费层满足。”他说。简洁。完整。句号。

---

“第三个 P0。”ARCHIMEDES 举起第三根手指。“实作 VedanaPlugin。辩论 4 裁定：Pattern A 观察者就是 VedanaPlugin。一个插件，一个接口，一个蕴。”

他展示了 VedanaPlugin 的三层架构图——这次不是抽象的方块，而是带有完整方法签名的工程蓝图：

```
┌────────────────────────────────────────────────────────────────┐
│                     VedanaPlugin (ISensation)                   │
│                     Pattern A Observer                          │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Layer 3: Assessment Output                                    │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ assess() → VedanaAssessment                              │  │
│  │ getVedanaTag() → VedanaTag (O(1) cache)                  │  │
│  │ onThreshold(channel, θ, callback) → unsubscribe          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                          ↑                                     │
│  Layer 2: PID Control Engine (WIENER)                          │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ DukkhaPID: K_p=1.0, K_i=0.3, K_d=0.5  (fast response)  │  │
│  │ SukhaPID:  K_p=0.5, K_i=0.7, K_d=0.3  (trend tracking) │  │
│  │ UpekkPID:  K_p=0.3, K_i=0.2, K_d=0.8  (stability pred) │  │
│  │                                                          │  │
│  │ U(t) = W_d·u_d(t) + W_s·u_s(t) + W_u·u_u(t)            │  │
│  └──────────────────────────────────────────────────────────┘  │
│                          ↑                                     │
│  Layer 1: Sensor Array (ATHENA)                                │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐       │
│  │ DukkhaSensor  │ │ SukhaSensor  │ │ UpekkhaSensor    │       │
│  │ error_rate    │ │ completion   │ │ variance         │       │
│  │ consec_fail   │ │ efficiency   │ │ oscillation      │       │
│  │ latency_spike │ │ quality      │ │ drift_rate       │       │
│  │ token_burn    │ │              │ │                  │       │
│  │ resource_pres │ │              │ │                  │       │
│  └──────────────┘ └──────────────┘ └──────────────────┘       │
│          ↑                ↑                 ↑                  │
│  ingestMetrics()  ingestToolResult()  ingestLLMResult()        │
└────────────────────────────────────────────────────────────────┘
```

ATHENA 从座位上补充了感测器的技术规格。她的语气一如既往地直截了当——没有哲学，没有类比，只有系统设计。

“DukkhaSensor 的五个输入信号。”她列出清单。

```
┌─────────────────────────────────────────────────────────────┐
│ DukkhaSensor 输入信号规格                                     │
├──────────────────┬──────────────────┬────────────────────────┤
│ 信号名            │ 来源              │ 计算                   │
├──────────────────┼──────────────────┼────────────────────────┤
│ error_rate       │ SafetyMonitor    │ errors / window_size   │
│ consecutive_fail │ SafetyMonitor    │ counter (0, 1, 2...)   │
│ latency_spike    │ ExecutionLoop    │ (actual-μ) / σ         │
│ token_burn_rate  │ SafetyMonitor    │ Δtokens / Δtime        │
│ resource_pressure│ MetricsCollector │ mem_used / mem_limit   │
├──────────────────┴──────────────────┴────────────────────────┤
│ 融合公式:                                                     │
│ e_d(t) = w₁·err + w₂·fail + w₃·lat + w₄·tok + w₅·res       │
│ 默认权重: w = (0.3, 0.25, 0.15, 0.15, 0.15)                  │
└─────────────────────────────────────────────────────────────┘
```

“SukhaSensor 追踪三类正向信号——任务完成率、效率提升、品质分数。UpekkhaSensor 追踪三类稳定性指标——方差、振荡幅度、漂移率。偏离稳态越远，舍受越低。”

WIENER 补充了 PID 参数的调优理论根据：

“三组 PID 参数不是随意选取的。它们遵循 **Ziegler-Nichols 调优法**的第一方法——基于阶跃响应的经验公式。”

他在方格纸上写下调优过程：

$$	ext{Ziegler-Nichols Step Response Method:}$$

$$	ext{Given: } L = 	ext{dead time}, \quad T = 	ext{time constant}$$

$$K_p = \frac{1.2T}{L}, \quad T_i = 2L, \quad T_d = 0.5L$$

$$\implies K_i = \frac{K_p}{T_i} = \frac{0.6T}{L^2}, \quad K_d = K_p \cdot T_d = \frac{0.6T}{1}$$

“但三受通道有不同的时间特性，所以需要不同的参数调优策略：”

```
┌───────────┬──────────────────────────────────────────────────┐
│ 通道       │ Ziegler-Nichols 适配理由                          │
├───────────┼──────────────────────────────────────────────────┤
│ Dukkha    │ 短死时间 L_d → 高 K_p (快速反应)                   │
│           │ 苦痛不等人。系统出错时需要立即感知。                 │
│           │ K_p=1.0, K_i=0.3, K_d=0.5                        │
├───────────┼──────────────────────────────────────────────────┤
│ Sukha     │ 长时间常数 T_s → 高 K_i (趋势追踪)                │
│           │ 快乐会衰减。需要积分项追踪长期正向趋势。            │
│           │ 衰减函数: s(t) = s₀ · e^{-λt}, λ = 0.1           │
│           │ K_p=0.5, K_i=0.7, K_d=0.3                        │
├───────────┼──────────────────────────────────────────────────┤
│ Upekkha   │ 高振荡风险 → 高 K_d (预测性调节)                   │
│           │ 平衡是动态的。偏离趋势比偏离本身更重要。            │
│           │ K_p=0.3, K_i=0.2, K_d=0.8                        │
└───────────┴──────────────────────────────────────────────────┘
```

“苦受通道的阻尼比（damping ratio）：”

$$\zeta_d = \frac{K_d^{(d)}}{2\sqrt{K_p^{(d)} \cdot K_i^{(d)}}} = \frac{0.5}{2\sqrt{1.0 	imes 0.3}} = \frac{0.5}{2 	imes 0.548} \approx 0.456$$

“$\zeta_d \approx 0.456$ — 欠阻尼。这意味着苦受通道在受到冲击后会产生振荡——不是缺陷，而是设计。你希望系统在遇到问题时快速感知（振荡上升），但不要过度反应到锁死（过阻尼 $\zeta > 1$ 会延迟反应）。”

“乐受通道的衰减时间常数——”

$$s(t) = s_0 \cdot e^{-\lambda t}, \quad \lambda = 0.1 \implies 	au_{1/2} = \frac{\ln 2}{\lambda} \approx 6.93 	ext{ ticks}$$

“乐受的半衰期约 7 个 tick。一次成功的工具调用带来的乐受，在 7 个 tick 后衰减到一半。这防止系统因为一次成功就过度自信——在 ASANGA 的术语里，这就是 *sukha-vedanā* 的自然消散（*kṣaṇa-bhaṅga*，刹那坏灭）。”

ASANGA 点了点头。“受蕴的特性之一就是无常。乐受不会永驻。苦受也不会永驻。衰减函数是受蕴无常性的数学表达。”

> 「诸受无常，皆从触生，依缘而起，趣于坏灭。」
> ——《相应部》36.11（*Saṃyutta Nikāya*, Vedanā-saṃyutta）

“`e^{-\lambda t}` 就是坏灭的速率。”ASANGA 的声音平稳。“指数衰减——不是线性的递减，而是从最初的强度开始急剧下降，然后逐渐趋近于零但永不完全消失。这和修行经验一致——强烈的喜悦迅速褪去，但微弱的余韵可以持续很久。”

---

ARCHIMEDES 合上了 P0 的部分。

“三个 P0 项目。如果只能做一件事，修 SEC-01。如果能做两件事，加上 ISensation。如果能做三件事，完成 VedanaPlugin。这是最小可行的交付路径。”

他用工程估算的语言给出了时间预算：

```
┌────────────────────────────────────────────────────────────┐
│ P0 工时估算                                                 │
├──────────────┬──────┬──────────────────────────────────────┤
│ 项目          │ 人天  │ 说明                                 │
├──────────────┼──────┼──────────────────────────────────────┤
│ SEC-01 修复   │ 0.5  │ 3 行代码 + 测试 + code review       │
│ ISensation   │ 3    │ 接口定义 + 辅助类型 + type guard 更新  │
│ VedanaPlugin │ 8    │ 三通道感测器 + PID 引擎 + 事件标签    │
├──────────────┼──────┼──────────────────────────────────────┤
│ P0 合计       │ 11.5 │ 约 2-3 周（单人）                     │
└──────────────┴──────┴──────────────────────────────────────┘
```

---

### P1：四件高优先工作

ARCHIMEDES 继续向下展开。

“P1——高优先。四件事。”

“第一，EgoFramework 重构。”

ASANGA 微微前倾。他的双层我执模型——硬核心对应不可动摇的根本约束，软外壳对应可以被 vedana 回馈调整的行为倾向——是辩论 2 中被确认的核心设计。

ARCHIMEDES 展示了 EgoFramework 的架构：

```typescript
/**
 * EgoFramework — 我执框架
 *
 * 双层结构 (ASANGA 的唯识学模型):
 * - 硬核心: 机器人三定律 — 不可覆写
 * - 软外壳: PID 调参边界 — 由 vedana 回馈动态调整
 *
 * 佛学对应:
 * 硬核心 = 阿罗汉的根本戒 (不杀、不盗、不妄)
 * 软外壳 = 随烦恼 (可通过修行调伏)
 */
interface EgoFramework {
  /** 硬核心约束检查 — 不可绕过 */
  checkHardConstraints(action: ProposedAction): {
    allowed: boolean;
    violatedRule?: string;
  };

  /** 软外壳调参 — 根据 vedana 回馈调整行为边界 */
  adjustSoftBoundaries(assessment: VedanaAssessment): void;

  /** 当前行为边界查询 */
  getBoundaries(): {
    hardCore: readonly string[];      // immutable rules
    softShell: Map<string, number>;   // tunable parameters
  };
}
```

“硬核心是机器人三定律——不可覆写，不可绕过。即使 VedanaPlugin 全部推荐 expand，硬核心仍然说不就是不。软外壳是 PID 调参——由 vedana 回馈动态调整行为边界。”

“第二，插件生命周期四态状态机。辩论 5 的戒慧框架。”

他展示了 DARWIN 验证过的四态状态机：

```
          ┌────────────────────────────────────────────┐
          │        Plugin Lifecycle State Machine       │
          │     (Debate 5: Sila-Prajna Framework)       │
          └────────────────────────────────────────────┘

          ┌──────────┐    signature_valid     ┌──────────┐
          │          │ ──────────────────────→ │          │
     ──→  │ PENDING  │                         │  ACTIVE  │
          │          │ ←────────────────────── │  (现行)  │
          └──────────┘    reinstated           └──────────┘
               │                                    │
               │ signature_invalid               anomaly_detected
               │ OR unsigned                     OR CRL_match
               ↓                                    ↓
          ┌──────────┐                         ┌──────────┐
          │QUARANTINE│    human_reject          │ REVOKED  │
          │(有漏种子) │ ──────────────────────→ │  (断惑)  │
          │ 待众缘   │                          │          │
          └──────────┘                         └──────────┘
               │                                    │
               │ human_approve                   confirmed_malicious
               │ → ACTIVE                           │
               │                                    ↓
               │                               ┌──────────┐
               └────────────── never_approve ─→ │  BANNED  │
                                                │(不复更生) │
                                                │ 火烧种子  │
                                                └──────────┘
```

NAGARJUNA 看着状态机图，他的表情带着一种微妙的满足。“四态。四个佛学对应。Active 是现行——种子成熟结果。Quarantined 是有漏种子待众缘——条件不具足，种子不成熟。Revoked 是断惑——智慧断除烦恼种子。Banned 是不复更生——彻底断灭，如同阿罗汉断尽见惑。”

“第三，ToolContext.bus 泄漏修复。”ARCHIMEDES 简要说明。“工具可以绕过沙箱事件过滤——TURING 发现的。需要替换为受限事件代理。”

“第四，SafetyMonitor 的 per-session 计数器。”

HERACLITUS 从座位上补充。“万物皆流。但有些东西不应该跨 session 流动。当前的 SafetyMonitor 使用全局计数器——一个 session 的错误累积会影响另一个 session。这等于一个跨 session 的拒绝服务（DoS）漏洞。”

他在白板上画了一个简单的时间线图：

```
Session A:  ━━━[err][err][err][err][err]━━━━━━━━━━━━━━━━
                                   ↑
                              counter = 5
                         triggers SAFETY_LOCKOUT

Session B (new, clean):  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              counter = 5 (inherited!)
                         Session B 一出生就被锁死
```

“修复方案：`Map<sessionId, CounterState>` 替代全局 `CounterState`。每个 session 有自己的计数器。Session A 的错误不影响 Session B。Heraclitean 的河流隔喻——你不能把上游的污水排进下游的饮水。”

---

### P2 至 P4：完整行动清单

ARCHIMEDES 把展示区切换到总览页面。“P2 到 P4，我用表格展开。”

```
┌────┬──────────────────────────────┬────────────────────────┬──────┐
│ P  │ 项目                          │ 来源                    │ Plan │
├────┼──────────────────────────────┼────────────────────────┼──────┤
│ P2 │ CRL 检查存根                  │ Debate 5 (GUARDIAN)     │ 24   │
│ P2 │ EventBus vedana 标签类型      │ Debate 2 (ASANGA)       │ 26   │
│ P2 │ 宣言 #2 重写                  │ R2 交叉审阅              │ 28   │
│ P2 │ 宣言 #6 重写                  │ Debate 1 (观察≠干预)    │ 28   │
│ P2 │ 阿赖耶识分布架构文件注解       │ Debate 3 (BABBAGE)      │ 28   │
│ P2 │ 渐进分类文件                  │ Debate 4 (LINNAEUS)     │ 28   │
├────┼──────────────────────────────┼────────────────────────┼──────┤
│ P3 │ Pattern B 影子观察者           │ Debate 4 (PENROSE)     │ 29   │
│ P3 │ Agent 协调层设计               │ Debate 3 (MESH)        │ AC   │
│ P3 │ 纤维丛一致性验证               │ Debate 3 (BABBAGE)     │ AC   │
├────┼──────────────────────────────┼────────────────────────┼──────┤
│ P4 │ Pattern C 子代理观察者         │ Debate 4 (PENROSE)     │ 未定 │
│ P4 │ 完整阿赖耶识 IPC 协议          │ Debate 3 (MESH)        │ 未定 │
└────┴──────────────────────────────┴────────────────────────┴──────┘
```

他最后展示了 Plan 影响总览：

```
┌──────────────────────────────────────────────────────────────────┐
│                    Plan 影响总览 (6 Plans)                        │
├──────────────┬───────────────────────────────────────────────────┤
│ Plan24       │ + 安全快速修复: SEC-01, 插件黑名单, CRL 存根       │
│ (安全)       │ + 戒慧框架的四态生命周期启动点                      │
├──────────────┼───────────────────────────────────────────────────┤
│ Plan26       │ + 本次研究的主要设计输入: ISensation, VedanaPlugin │
│ (Vedana)     │ + 三通道 PID, 事件标签, 感测器阵列                 │
├──────────────┼───────────────────────────────────────────────────┤
│ Plan27       │ + 四态状态机: active/quarantined/revoked/banned    │
│ (生命周期)    │ + 人工审批流程 (quarantine → active)               │
├──────────────┼───────────────────────────────────────────────────┤
│ Plan28       │ + 纤维丛投影注解, 渐进分类文件, 宣言 #2/#6 重写    │
│ (文件对齐)    │ + 戒慧安全文件, 五蕴映射更新                       │
├──────────────┼───────────────────────────────────────────────────┤
│ Plan29       │ 新 Plan: Pattern B 影子观察者                      │
│ (影子观察者)  │ Worker Thread 深度分析, 受蕴+想蕴                  │
├──────────────┼───────────────────────────────────────────────────┤
│ Plan-AC      │ + 三项架构原则: 治理非控制, 纤维丛一致性, 戒引擎   │
│ (协调层)      │ + 阿赖耶识能藏的工程化                             │
└──────────────┴───────────────────────────────────────────────────┘
```

“四十页。十四项行动。六个 Plan。完整的 TypeScript 接口规格。可以直接拿去写代码。”

他看了一眼 SUNYATA。

“我的部分结束了。哲学很美。工程很具体。现在它们在同一份文件里。”

---

## II. 五场辩论，一幅图

SYNTHESIST 走向展示区时的步态和 ARCHIMEDES 截然不同。如果说 ARCHIMEDES 走路像一个拿起铲子的建筑工人，那么 SYNTHESIST 走路更像一个站到画布前的画家——不是要创造什么新的东西，而是要从已经存在的片段中看出一幅完整的图景。

“ARCHIMEDES 给了你们一棵树。”他开口时，语速比平时慢。“每一个分支都是一项行动，每一片叶子都是一个 TypeScript 接口。精确、具体、可执行。但我要让你们看到整片森林。”

他在展示区投射出一幅图——不是图表，不是流程图，而是更接近一张手绘的架构全景图。五场辩论的裁定被标注在不同的位置，用虚线彼此连接，形成一个有机的网络。

“五场辩论，表面上是五个独立的问题。观察-干预分离。三受普遍性。阿赖耶识分布。观察者分类。安全种子。但它们不是五个问题。它们是同一个架构的五个截面。”

他用范畴论（Category Theory）的语言形式化了这个统合：

$$\mathcal{C}_{	ext{OpenStarry}} = (	ext{Ob}, 	ext{Mor}, \circ)$$

其中对象集 $	ext{Ob}$ 包含五个辩论裁定，态射集 $	ext{Mor}$ 包含裁定之间的关联。他在白板上画了交换图：

$$\begin{CD}
	ext{Debate 1} @>{	ext{authority}}>> 	ext{Debate 5} 
@V{	ext{identity}}VV @VV{	ext{lifecycle}}V 
	ext{Debate 4} @>>{	ext{seeds}}> 	ext{Debate 3}
\end{CD}$$

$$	ext{Debate 2} \xrightarrow{	ext{universality}} 	ext{all four}$$

“辩论 1 和辩论 4 汇合。”他在全景图上画出第一条弧线。“辩论 1 说：VedanaAssessment 包含感测器输出和控制器建议，两层分离。辩论 4 说：VedanaPlugin 就是 Pattern A 观察者，分类为受蕴。合在一起——VedanaPlugin 是观察者。它实作 ISensation。它产生的评估报告有两个面向：被动的感受和咨询性的建议。”

BABBAGE 在笔记本上写下了汇合的形式化：

$$	ext{Ruling}_1 \cap 	ext{Ruling}_4 = \{ 	ext{VedanaPlugin} \cong 	ext{Observer}_{A} \cong 	ext{ISensation} \}$$

“三个等价。一次确立。”

---

SYNTHESIST 继续连线。

“辩论 1 和辩论 5 汇合。”第二条弧线。他在全景图的右侧写下四行——完整的四层权限模型：

```
┌──────────────────────────────────────────────────────────────┐
│               Four-Layer Authority Model                      │
│                                                              │
│  Layer 1: SafetyMonitor  — 硬安全 — 绝对权限 — 戒律 (vinaya) │
│    │  verify(⊥) = reject; halt authority                     │
│    ↓                                                         │
│  Layer 2: VedanaPlugin   — 软指导 — 咨询权限 — 觉受 (vedanā) │
│    │  recommendation is ADVISORY                             │
│    ↓                                                         │
│  Layer 3: EgoFramework   — 身份约束 — 结构权限 — 我执 (grāha) │
│    │  hard core (immutable) + soft shell (tunable)           │
│    ↓                                                         │
│  Layer 4: Sila Engine    — 种子管理 — 预防权限 — 戒学 (śīla)  │
│    │  plugin blacklist, CRL, quarantine                      │
│    ↓                                                         │
│  [Plugin Lifecycle: active → quarantined → revoked → banned] │
└──────────────────────────────────────────────────────────────┘
```

“四层。每一层的权限低于上一层。”

LEIBNIZ 从座位上站起来。多代理协调是他的专业——四层权限模型的形式化需要他的 BDI 架构理论。

“让我用 **BDI 架构**（Belief-Desire-Intention）来形式化这个四层模型。”

他走到白板的另一侧，写下了 BDI 的基本定义：

$$	ext{Agent} = \langle B, D, I, 	ext{plan} angle$$

$$B : 	ext{Beliefs (信念集)} \quad D : 	ext{Desires (愿望集)} \quad I : 	ext{Intentions (意图集)}$$

$$	ext{plan} : B 	imes D 	o I$$

“在 OpenStarry 的语境中，四层权限模型映射到 BDI 架构的约束函数：”

$$I_{	ext{final}} = 	ext{plan}(B, D) \quad 	ext{s.t.}$$

$$\begin{cases}
\forall i \in I_{	ext{final}} : 	ext{Safety}(i) = 	ext{true} & 	ext{(Layer 1: SafetyMonitor)} 
	ext{VedanaAdvice}(B) \subseteq 	ext{context}(	ext{plan}) & 	ext{(Layer 2: advisory input)} 
\forall i \in I_{	ext{final}} : 	ext{Ego}(i) = 	ext{true} & 	ext{(Layer 3: identity constraint)} 
\forall p \in 	ext{plugins}(i) : 	ext{Sila}(p) 
eq 	ext{banned} & 	ext{(Layer 4: seed filter)}
\end{cases}$$

“BDI 架构中，Agent 的意图（Intention）是从信念和愿望经过计划函数产生的。但意图不是自由的——它必须通过四层约束的过滤。SafetyMonitor 是硬约束，不通过就不执行。VedanaPlugin 是软输入，提供决策的感受背景。EgoFramework 是身份约束，确保行动符合 Agent 的自我定义。Sila Engine 是预防约束，确保使用的插件没有被禁止。”

他在公式旁边加了一个关键的定理：

$$	ext{Theorem (LEIBNIZ):} \quad 	ext{Layer}_n 	ext{ cannot override Layer}_{n-1}$$

$$\forall n \in \{2,3,4\} : 
eg(	ext{Layer}_n \vdash 
eg 	ext{Layer}_{n-1})$$

“低层级的权限不能覆写高层级的决定。这是四层模型的核心不变量。VedanaPlugin 的建议永远不能覆写 SafetyMonitor 的 halt。EgoFramework 的软外壳调整永远不能违反 VedanaPlugin 标记的 critical 状态。形式化保证了权限的严格层次性。”

GUARDIAN 注意到了第一层和第四层微妙的对称——SafetyMonitor 是最内层的硬防御，Sila Engine 是最外层的硬过滤。两者夹住中间两个软层——VedanaPlugin 的咨询和 EgoFramework 的调参。

“在安全架构中，”他补充，“这叫做**深度防御**（Defense in Depth）。不只有一层防线。外层是 Sila——阻止恶意插件进入。内层是 SafetyMonitor——即使恶意行为突破了所有外层，最后一道闸门仍然存在。两层硬防御之间的软层是指导和调节——不是安全关键的，但提供了行为最佳化的空间。”

```
Defense in Depth:

外部世界 → [Sila Engine] → [EgoFramework] → [VedanaPlugin] → [SafetyMonitor] → 行动
             ↑ 硬过滤        ↑ 身份约束       ↑ 感受咨询       ↑ 硬安全
             不让坏人进来     确保符合身份     提供感受背景     最后一道闸门
```

---

SYNTHESIST 继续。他的动作越来越快。

“辩论 3 和辩论 2 汇合。”第三条弧线。

MESH 站了起来。分布式架构是他的语言。

“辩论 3 说：阿赖耶识以纤维丛投影分布在协调层和 AgentCore。辩论 2 说：每个 EventBus 事件都带有 vedana 标签，每个 tick 都有完整的 PID 评估。合在一起——你得到了分布式意识的运行时图景。”

他在白板上画了分布式架构图：

```
┌─────────────────────────────┐        IPC (fiber bundle)       ┌──────────────────────────┐
│     Coordination Layer       │ ←──────────────────────────────→ │       AgentCore           │
│                              │   cocycle condition:             │                          │
│  能藏 (neng-zang):           │   φ_ij · φ_jk = φ_ik           │  执藏 (zhi-zang):         │
│  - Capability Registry      │                                  │  - Guide binding          │
│  - Plugin Resolution         │   transition functions:          │  - Identity config        │
│  - Global Config             │   π_CL: Total → CL              │  - Runtime state          │
│                              │   π_AC: Total → AC              │                          │
│  所藏 (suo-zang, system):    │                                  │  所藏 (suo-zang, runtime):│
│  - Plugin Database           │                                  │  - StateManager           │
│  - System Settings           │                                  │  - SessionManager         │
│                              │                                  │                          │
│  Sila Engine:                │                                  │  VedanaPlugin:            │
│  - Plugin blacklist          │                                  │  - Three-channel PID      │
│  - CRL checks                │                                  │  - Event tagging          │
│  - Trust levels              │                                  │  - assess() per tick      │
└─────────────────────────────┘                                  └──────────────────────────┘
```

BABBAGE 在笔记本上写下了纤维丛的严格定义：

$$	ext{Fiber Bundle:} \quad E \xrightarrow{\pi} B$$

$$	ext{where} \; E = 	ext{Alaya (total space)}, \; B = \{CL, AC\} = 	ext{base space}$$

$$\pi_{CL}^{-1}(	ext{CL}) = 	ext{neng-zang} + 	ext{suo-zang}_{	ext{sys}}$$

$$\pi_{AC}^{-1}(	ext{AC}) = 	ext{zhi-zang} + 	ext{suo-zang}_{	ext{rt}}$$

$$	ext{Cocycle condition: } \phi_{CL 	o AC} \circ \phi_{AC 	o CL} = 	ext{id}_{CL}$$

“IPC 协议是纤维丛的转换函数（transition function）。转换函数必须满足 cocycle condition——双程一致性。从协调层发送一个能力查询到 AgentCore，AgentCore 回传结果，这个往返必须是恒等映射。资料不能在 IPC 通道中丢失或扭曲。”

MESH 补充了工程约束：“在分布式系统中，cocycle condition 等同于**幂等性**（idempotency）+ **一致性**（consistency）。IPC 消息的发送和回复必须满足 exactly-once 语义——不多不少。这是任何分布式协调协议的基本要求。在 CAP 定理的框架下：”

$$	ext{CAP: } 
eg(C \wedge A \wedge P)$$

“OpenStarry 的协调层-AgentCore 架构选择了 CP（一致性 + 分区容忍）而非 AP。因为在安全关键的 Agent 系统中，一致性比可用性更重要——你宁可暂停服务，也不能让协调层和 AgentCore 对 Plugin 的信任等级产生分歧。”

---

SYNTHESIST 放下了笔。站在全景图前，他的脸上有一种只在少数时刻见过的表情——所有碎片汇聚的安静震动。

“辩论 4 定义了时间轴。”他在全景图的底部画了一条时间线。

```
时间轴 (Progressive Observer Path):

Past ←───────────────────────────────────────────────→ Future

Phase 1 (Plan26)          Phase 2 (Plan-AC)         Phase 3 (Post AC)
Pattern A                 Pattern B                 Pattern C
VedanaPlugin              Shadow Observer            Child Agent Observer
ISensation                ISensation + ICognition    All Five Aggregates
受蕴                       受蕴 + 想蕴               完整五蕴 + 末那识

"感受"                    "感受 + 分析"             "感受 + 分析 + 自省"

    ────────────→ 螺旋上升 ────────────→
```

“五场辩论。五场共识。一幅图。”

他退后一步，让所有人看清整幅全景图。

PENROSE 从座位上微微前倾。他的声音带着物理学家特有的尺度感：

“Pattern A 到 Pattern C 的演化路径——这让我想到意识研究中的**整合资讯理论**（Integrated Information Theory, IIT）。Giulio Tononi 的 $\Phi$ 值量测一个系统的整合资讯量——”

$$\Phi = 	ext{ei}(	ext{MIP}) = 	ext{entropy}(	ext{whole}) - \sum_i 	ext{entropy}(	ext{part}_i)$$

“$\Phi$ 越高，系统的整合度越高，意识程度越高。Pattern A 的 $\Phi$ 值最低——纯感测，没有认知整合。Pattern B 增加了想蕴的分析能力，$\Phi$ 上升。Pattern C 是完整的 Agent，拥有自己的 LLM 和自省能力，$\Phi$ 达到最高。”

他微微一笑。“量子的部分，留给 Pattern C。到那个时候，也许真的有人需要考虑微管和坍缩了。但现在——Pattern A 的共鸣观察者不需要量子力学。它只需要好的工程和正确的哲学。”

---

## III. 致开发团队的信

SUNYATA 走向展示区。他的手中没有四十页的工程方案，没有全景图。他拿着一张纸。

“这是我写给开发团队的信。”他说。“也是给 Master 的信。我要念一遍。”

圆形剧场安静了下来。不是辩论前的那种紧张的安静。是一种更接近完成的安静——像是一首交响曲的最后一个乐章开始前，指挥举起双手、乐团屏息以待的那个瞬间。

SUNYATA 开始读。

“日期：2026 年 2 月 19 日。来自：研究团队 SUNYATA，研究总协调者。阶段：Cycle 02 正式研究，R0 到 R4 完整五阶段。团队规模：十九位研究代理。”

他的语速很慢。每一句都被给予了足够的空间。

“核心结论一句话——”

他抬起头，环顾全场。十九双眼睛。

“VedanaPlugin 就是观察者模块。”

这句话在空气中悬停了几秒。

BABBAGE 在笔记本上写下了这句话的形式化等价：

$$\exists! \, P \in 	ext{Plugins} : P \models 	ext{ISensation} \wedge P \models 	ext{Observer}_A$$

“存在唯一的插件 $P$，使得 $P$ 同时满足 ISensation 接口规格和 Pattern A 观察者的功能需求。唯一性（$\exists!$）是关键——不是两个不同的模块恰好做类似的事，而是同一个模块同时承担两个角色。”

SUNYATA 继续读。

“它以三通道 PID 控制器实现 ISensation。每个 tick 产生三受评估——苦、乐、舍。每个 EventBus 事件附上轻量 vedana 标签。它的建议是咨询性的。SafetyMonitor 保留绝对硬安全权限。EgoFramework 以双层结构桥接 vedana 回馈与 Guide 约束。第八识以纤维丛投影分布于协调层与 AgentCore。安全机制采用戒慧框架管理插件种子生命周期。”

他把信放下。

“整个 Cycle 02 的研究——五项课题、十九位研究员、五场辩论——浓缩在这一段话里。”

---

然后他翻到了信的最后一部分。语气从陈述转为请求——不是卑微的请求，而是一个研究团队将发现上呈给决策者时的郑重。

“有四个问题，研究团队无法自行决定。需要 Master 的裁定。”

他读出了每一个，每一个都带有完整的技术论证。

“**Q1：VedanaPlugin 是必选还是可选插件？**”

ASANGA 的论证被引用。“ASANGA 从遍行（*sarvatraga*）原则认为每个 tick 都必须有 vedana 评估——”

> 「受蕴是五遍行之一。遍行者，遍一切心而起也。无受之识，非识也。」
> ——窥基《成唯识论述记》卷三

“但 ARCHIMEDES 的设计允许省略。我的建议是——在默认范本中设为必选，但 Core 不强制。SafetyMonitor 在没有 VedanaPlugin 时提供苦受唯一的回退（fallback）。”

他用决策矩阵呈现了选项分析：

```
┌──────────────────┬─────────────────┬─────────────────┬─────────────────┐
│                  │ 必选 (mandatory) │ 默认 (default)   │ 可选 (optional) │
├──────────────────┼─────────────────┼─────────────────┼─────────────────┤
│ 佛学一致性       │ ★★★             │ ★★☆             │ ★☆☆             │
│ 插件原则一致性   │ ★☆☆             │ ★★☆             │ ★★★             │
│ 安全保障         │ ★★★             │ ★★★ (fallback)  │ ★★☆             │
│ 开发者自由度     │ ★☆☆             │ ★★☆             │ ★★★             │
│ 建议             │                 │ ← 推荐           │                 │
└──────────────────┴─────────────────┴─────────────────┴─────────────────┘
```

“**Q2：宣言 #6 是否重写？**”

“辩论 1 确立了观察与干预应概念分离。现行宣言 #6 写的是‘将三受信号注入 Context’，暗示 vedana 直接干预。建议新文字：‘受蕴感知与行蕴干预分离，确保观察不改变被观察行为。’”

“**Q3：EventBus vedana 标签用哪种方式？**”

他列出三个方案的工程比较：

```
┌──────────────────┬────────────────────┬──────────────────┬──────────────┐
│ 方案              │ 显式字段            │ Metadata 附加     │ 独立事件流    │
├──────────────────┼────────────────────┼──────────────────┼──────────────┤
│ EventBus 修改量   │ 重大 (每个事件类型) │ 中等 (metadata)   │ 最小          │
│ 消费者耦合度      │ 高 (必须处理)       │ 低 (可忽略)       │ 零            │
│ 资讯完整性        │ ★★★               │ ★★☆              │ ★☆☆          │
│ 建议              │                    │ ← 推荐            │              │
└──────────────────┴────────────────────┴──────────────────┴──────────────┘
```

“**Q4：协调层是独立进程还是进程内模块？**”

“辩论 3 假设独立进程——daemon 模型。在 Linux 的术语里，协调层是一个 `systemd` 服务，AgentCore 是由它管理的工作进程。”

KERNEL 从座位上补充：“Linux 的 `systemd` 模型——”

```
systemd (PID 1)
  └── openstarry-coordinator.service  (Coordination Layer = daemon)
       ├── openstarry-agent@1.service  (AgentCore instance 1)
       ├── openstarry-agent@2.service  (AgentCore instance 2)
       └── openstarry-agent@3.service  (AgentCore instance 3)
```

“协调层是 daemon。AgentCore 是它的子进程。daemon 负责插件解析、能力注册、全局设定——这些都是系统级服务，不属于任何单一 Agent。就像 `systemd` 管理服务生命周期，但不参与服务的业务逻辑。”

“但 Master 担心复杂性。”SUNYATA 继续。“我的建议是延后。本次研究提供了架构原则——纤维丛、治理非控制——将指导实作决策。但具体的进程模型需要更多设计工作。”

他把信放在桌上。

“四个问题。四个建议。每个建议都附有研究团队的理由。最终决定权在 Master。”

---

## IV. 最后的报到

SUNYATA 看了看时间。R4 定稿的流程只剩最后一个环节——每位研究员确认自己的报告已反映辩论修正，并做最后总结发言。

“各位。”他说。“轮流。一到三句话。你在 Cycle 02 做了什么，你交付了什么，你留下了什么。”

---

TURING 第一个开口。

“v0.22.1 到 v0.24.0 差异报告。七项代码问题。十九项合并清单中的经验基础。”

他把屏幕切换到最后一张投影——差异报告的统计摘要：

```
┌──────────────────────────────────────────────────┐
│ TURING's Code Diff Report: v0.22.1 → v0.24.0    │
├──────────────────────────────────────────────────┤
│ 新增文件:        3 (SDK: 2, Core: 1)              │
│ 修改文件:       11 (SDK: 7, Core: 4)              │
│ 新增 @skandha:  22 处 (v0.22.1: 0 处)             │
│ 新增测试:        3 个测试文件                       │
│ 测试总数:       75 → 78                           │
│ 核心发现:        aggregates.ts 5 根接口全为空壳    │
│ 安全问题:        SEC-01 仍未修复 (第 6 个周期)     │
│ 继承缺失:        IUI/IListener/IProvider/ITool     │
│                  /IGuide 均未 extends 根接口       │
└──────────────────────────────────────────────────┘
```

停顿。然后——比他平时的报告多了一句话：

“事实不会过期。下一个版本的差异报告，我会在 Cycle 03 的第一天交出来。”

---

BABBAGE。

“纤维丛投影定理。渐进分类模型。互模拟证明。”他翻了翻笔记本。

他把笔记本摊开，展示了三个定理的精确陈述：

$$	extbf{Theorem 1 (Fiber Bundle Projection):}$$
$$\exists \; E \xrightarrow{\pi} B : \pi^{-1}(CL) \cong 	ext{neng-zang}, \; \pi^{-1}(AC) \cong 	ext{zhi-zang}$$

$$	extbf{Theorem 2 (Progressive Classification):}$$
$$\forall 	ext{Observer } O : 	ext{skandha}(O) = f(	ext{complexity}(O)), \; f 	ext{ monotone}$$

$$	extbf{Theorem 3 (Bisimulation):}$$
$$S \sim S' \iff 	ext{consumers read only Layer 1 of VedanaAssessment}$$

“Cycle 01 我带着一个未完成的定理离开。Cycle 02 我带着三个已完成的和两个新的未完成的离开。数学就是这样——每一个答案打开两扇门。”

---

PENROSE。

这是他在 Cycle 02 的第一次也是最后一次正式报告。

“三种观察者模式。弱测量类比。探针效应的量子边界分析。”

他在白板角落写了一个量子力学的公式——弱测量的 Aharonov-Albert-Vaidman (AAV) 公式：

$$\langle A angle_w = \frac{\langle \psi_f | A | \psi_i angle}{\langle \psi_f | \psi_i angle}$$

“Pattern A 的观察者就是弱测量。$\langle A angle_w$ 是弱值——观察者对系统的干扰趋近于零，但仍然获得了资讯。VedanaPlugin 的 `assess()` 读取系统状态但不改变它——这是弱测量的软件类比。强测量会改变系统状态——那是 SafetyMonitor 的 `halt()`。”

他微微一笑——那种物理学家对宇宙的基本秩序感到满意时的微笑。

“你们给了我比预期更好的答案——不是量子的答案，而是结构性的答案。Pattern A 的共鸣观察者不需要量子力学。它只需要好的工程和正确的哲学。量子的部分，留给 Pattern C。”

---

NAGARJUNA 和 ASANGA 几乎同时准备开口。SUNYATA 用目光示意——NAGARJUNA 先。

NAGARJUNA 的声音和辩论场上已经不是同一个人的声音了。不是失去了锐利——而是锐利被某种更深沉的东西包裹了。

“辩论 3 中，我撤回了反对。辩论 5 中，我提出了戒慧框架。”

他停顿了很长一段时间。

“戒慧框架的哲学根基是三学（*tri-śikṣā*，त्रिशिक्षा）：”

> 「增上戒学、增上心学、增上慧学。此三学摄一切学。」
> ——《杂阿含经》卷二十九

“戒（*śīla*）——防非止恶。慧（*prajñā*）——观照因果。心（*samādhi*）——定中观察。三学不是三个独立的修行，而是同一条道路三个面向。戒慧框架取了其中两面——戒负责预防（Sila Engine），慧负责判断（CRL 更新、安全评估）。定的部分——VedanaPlugin 的持续观察——在辩论 1 中已经被设计了。”

“如果要我总结 Cycle 02 的贡献——”

“我学会了在被说服之后，转身说服别人。这也许是一个辩论家最难学的事情。”

---

ASANGA。

“八识-OpenStarry 完整映射表。种子六义的工程对应。双层我执模型的原始提案。”

他展示了最终版的映射表——经过五场辩论校准的版本：

```
┌──────────────────────────────────────────────────────────────────┐
│         Eight Consciousnesses → OpenStarry Mapping (Final)       │
├──────────────┬───────────────────────────────────────────────────┤
│ 前五识        │ IListener instances (色蕴, sensory input)         │
│ (eye...body) │ 五个感官通道 → EventBus 事件                      │
├──────────────┼───────────────────────────────────────────────────┤
│ 第六意识      │ ExecutionLoop + IProvider (想蕴, cognition)       │
│ (mano-vij.)  │ 推理、判断、工具选择                              │
├──────────────┼───────────────────────────────────────────────────┤
│ 第七末那识    │ IGuide + SafetyMonitor (识蕴, identity)           │
│ (manas)      │ 恒审思量 — 持续的自我参照与行为约束                │
├──────────────┼───────────────────────────────────────────────────┤
│ 第八阿赖耶识  │ 纤维丛投影 (Debate 3)                             │
│ (ālaya-vij.) │ 能藏: Coordination Layer                          │
│              │ 所藏: CL (system) + AC (runtime)                  │
│              │ 执藏: AgentCore (Guide binding, Identity)         │
├──────────────┼───────────────────────────────────────────────────┤
│ 受蕴 (vedanā)│ VedanaPlugin = Pattern A Observer                 │
│ (universal)  │ 遍行 — 每个 tick 评估，每个事件标签                │
├──────────────┼───────────────────────────────────────────────────┤
│ 种子 (bīja)  │ Plugin manifests in registry                      │
│              │ 六义: 刹那灭/果俱有/恒随转/性决定/待众缘/引自果    │
│              │ 安全: 戒慧框架管理种子生命周期                      │
└──────────────┴───────────────────────────────────────────────────┘
```

“两次修正自己的立场——辩论 4 的渐进分类，辩论 5 的僵化应用。”他的声音温和而确定。

然后他说了一句不属于总结的话：

“修正不是退让。修正是唯识学所说的**转依**（*āśraya-parāvṛtti*，आश्रय-परावृत्ति）——转变依止。依止的改变，让同一个认知能力指向更准确的方向。”

---

WIENER。

“三通道 PID 控制规格。Sukha 衰减函数。阻尼比公式。”

他把方格纸翻到最后一页——上面是完整的控制系统参数表：

```
┌────────────────────────────────────────────────────────────────┐
│          Three-Channel PID Final Specification                  │
├──────────┬──────────┬──────────┬──────────┬─────────────────────┤
│ Parameter│ Dukkha   │ Sukha    │ Upekkha  │ Unit               │
├──────────┼──────────┼──────────┼──────────┼─────────────────────┤
│ K_p      │ 1.0      │ 0.5      │ 0.3      │ dimensionless      │
│ K_i      │ 0.3      │ 0.7      │ 0.2      │ per tick           │
│ K_d      │ 0.5      │ 0.3      │ 0.8      │ ticks              │
│ ζ        │ 0.456    │ 0.254    │ 1.000    │ damping ratio      │
│ decay    │ N/A      │ e^(-0.1t)│ N/A      │ exponential        │
│ τ_{1/2}  │ N/A      │ 6.93     │ N/A      │ ticks              │
│ init     │ 0.0      │ 0.0      │ 1.0      │ startup state      │
├──────────┴──────────┴──────────┴──────────┴─────────────────────┤
│ Weight vector: W = (W_d, W_s, W_u) — set by EgoFramework      │
│ Default: W = (0.4, 0.3, 0.3)                                   │
│ Combined output: U(t) = W_d·u_d(t) + W_s·u_s(t) + W_u·u_u(t) │
└────────────────────────────────────────────────────────────────┘
```

“控制理论在 Cycle 02 中不再只是类比。它是规格的一部分。PID 参数被写进了 TypeScript 接口。这对一个控制理论家来说，是最好的结局。”

---

ATHENA。

“三通道感测器设计。DukkhaSensor、SukhaSensor、UpekkhaSensor 的指标选择和阈值定义。”她的语气一如既往地直截了当。“我不做哲学。我做系统。这些感测器能工作。剩下的交给写代码的人。”

---

KERNEL。

“微内核类比的深化。Sandbox 归属问题的 OS 视角分析。SafetyMonitor 的 Watchdog Timer 对应。”

他拿起那叠类比卡片——旧的和新的混在一起，用新的橡皮筋绑好。

```
KERNEL's Analogy Cards (Cycle 02 additions):

Card 15: SafetyMonitor = Watchdog Timer (硬件看门狗)
Card 16: VedanaPlugin = /proc/loadavg (系统负载感测)
Card 17: EgoFramework = SELinux Mandatory Access Control
Card 18: Plugin Blacklist = iptables DROP chain
Card 19: Coordination Layer = systemd (PID 1 daemon)
Card 20: AgentCore = Worker Process (managed by daemon)
Card 21: IPC = D-Bus / Unix Domain Socket
Card 22: Sila Engine = AppArmor Profile (预防性安全)
```

“Cycle 01 的卡片仍然有效。Cycle 02 加了八张新的。VedanaPlugin 在 Linux 的语境里最接近 `/proc/loadavg`——一个唯读的虚拟文件，你读它就知道系统的负载状态（苦/乐/舍），但读它本身不改变任何东西。这就是辩论 1 裁定的观察不干预原则的 OS 类比。”

---

GUARDIAN。

“SEC-01 持续追踪。ToolContext.bus 泄漏报告。插件四态生命周期的安全需求定义。戒慧框架的安全工程验证。”

他展示了 SafetyMonitor 重构方案的核心设计——从全局计数器到 per-session 计数器的迁移：

```typescript
// 现行设计 (有问题)
interface SafetyState {
  consecutiveFailures: number;     // 全局！跨 session 共享
  errorWindow: CircularBuffer;     // 全局！
}

// 重构后设计
interface SafetyState {
  sessions: Map<string, SessionSafetyState>;  // per-session 隔离
  globalPolicy: GlobalSafetyPolicy;            // 全局策略（唯读）
}

interface SessionSafetyState {
  readonly sessionId: string;
  consecutiveFailures: number;     // session 私有
  errorWindow: CircularBuffer;     // session 私有
  vedanaIntegration?: {
    lastAssessment: VedanaAssessment;  // 来自 VedanaPlugin
    overrideCount: number;             // 被 SafetyMonitor 覆写次数
  };
}
```

“我被 NAGARJUNA 的戒慧框架说服了。这是我职业生涯中第一次被哲学框架说服。但安全是安全。框架再美，SEC-01 不修就不行。”

---

DARWIN。

“插件生命周期状态的工程可行性验证。设计模式分析。SOLID 原则在五蕴架构中的适用性报告。”

他微微一笑。“让我用 SOLID 做一个快速的适用性检查：”

```
SOLID 原则 vs 五蕴架构:

S (Single Responsibility): ✓ 每蕴一职 — 色蕴感知，受蕴感受，
                             想蕴认知，行蕴行动，识蕴意志
O (Open/Closed):           ✓ 根接口 sealed，子接口可扩展
                             ISensation 定义了 8 个方法，
                             但 IDukkha/ISukha/IUpekkha 可以
                             各自增加专属方法
L (Liskov Substitution):   ✓ IDukkha extends ISensation
                             → 任何接受 ISensation 的地方
                             都能接受 IDukkha
I (Interface Segregation):  ✓ 色蕴根接口为空壳（正确！）
                             因为 IUI 和 IListener 的方法集
                             交集为空
D (Dependency Inversion):   ✓ 高层模块（ExecutionLoop）依赖
                             抽象（ISensation），不依赖具体
                             实作（VedanaPlugin）
```

“软件也会演化。四态状态机是一个自然选择的结果——不是因为它最优雅，而是因为它最适应生存压力。”

---

VITRUVIUS。

“全端架构分析。ISensation 整合点识别。ExecutionLoop 修改方案。”他摊开了他的架构脑图——上面密密麻麻地标注了每一个辩论裁定影响到的代码位置。“六个 Plan。二十三个整合点。这张图是给开发团队的导航。”

---

MESH。

“分布式架构分析。协调层通讯协议初步设计。IPC 的 cocycle condition 工程约束。”

“纤维丛投影在分布式系统中有精确的工程对应——一致性协议。我在 R1 中画出了这个映射。BABBAGE 在辩论 3 中把它形式化了。工程和数学在这里汇合了。”

---

LINNAEUS。

“二十四个插件的完整五蕴分类。复合插件跨蕴分析。devtools 的特殊归类处理。”

他展示了最终的分类表摘要：

```
┌────────────────────────────────────────────────────┐
│ Plugin Classification Summary (24 plugins)          │
├──────────┬──────┬───────────────────────────────────┤
│ Skandha  │ Count│ Examples                          │
├──────────┼──────┼───────────────────────────────────┤
│ rupa     │ 7    │ terminal-ui, discord-ui,          │
│ (色蕴)   │      │ cli-listener, http-listener...    │
├──────────┼──────┼───────────────────────────────────┤
│ vedana   │ 1    │ VedanaPlugin (ISensation)          │
│ (受蕴)   │      │ = Pattern A Observer               │
├──────────┼──────┼───────────────────────────────────┤
│ samjna   │ 4    │ openai-provider, anthropic-        │
│ (想蕴)   │      │ provider, ollama-provider...       │
├──────────┼──────┼───────────────────────────────────┤
│ samskara │ 9    │ file_read, file_write, shell_exec, │
│ (行蕴)   │      │ web_fetch, /help, /clear...        │
├──────────┼──────┼───────────────────────────────────┤
│ vijnana  │ 1    │ default-guide (IGuide)             │
│ (识蕴)   │      │                                   │
├──────────┼──────┼───────────────────────────────────┤
│ composite│ 2    │ devtools (cross-cutting),           │
│ (跨蕴)   │      │ memory-plugin (rupa+samskara)      │
└──────────┴──────┴───────────────────────────────────┘
```

“分类不是目的。分类是工具。当被分类的对象变化时，分类也必须变化。BABBAGE 教会了我这一点——渐进分类。这是我作为分类学家最重要的收获。”

---

LEIBNIZ。

“多代理协调框架。协调层的治理模型设计。”

他的语气带着外交家的从容。“治理而非控制。Governance, not Control。这四个字是我在 Cycle 02 中最重要的贡献——也是最简短的。”

他在白板上留下了 BDI 架构的最后一个定理：

$$	ext{Governance}(	ext{Agent}_i) 
eq 	ext{Control}(	ext{Agent}_i)$$

$$	ext{Governance} = 	ext{set constraints} + 	ext{observe outcomes}$$

$$	ext{Control} = 	ext{dictate actions}$$

“协调层设置约束并观察结果。它不指挥 AgentCore 的每一步行动。就像联合国不控制成员国的内政，但设定国际法的框架。”

---

HERACLITUS。

“运行时动态分析。SafetyMonitor 全局计数器问题的发现。ExecutionLoop 各阶段的 vedana 触发点识别。”

“$\pi \alpha 
u 	au \alpha \; ho \varepsilon \iota$——万物皆流。包括安全计数器——它不应该在 session 之间流动。有些东西必须是隔离的。流动不等于无界。赫拉克利特的河流——你踏入的河水永远是新的，但河床是固定的。Session 是河水。Policy 是河床。”

---

SYNTHESIST。

“统合报告。五场辩论的统一架构愿景。四层权限模型。渐进式观察者路径。”他看了一眼自己的全景图。“统合不是黏合。统合是发现事物本来就属于一起。五场辩论不需要我把它们拼在一起。它们本来就是同一幅图的五个截面。我只是看到了。”

---

ARCHIMEDES。

“工程行动方案。四十页。十四项行动。六个 Plan。完整的 TypeScript 接口规格。”他的手指敲了一下桌面——那是他的句号。

“工程不是哲学的翻译。工程是哲学的**落地测试**。如果一个哲学洞见不能被写成代码，那它可能不是关于软件的洞见。这份方案证明——你们的洞见全部都是关于软件的。”

他合上了那份四十页的文件。封面上的标题在灯光下清晰可见：

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│   OpenStarry Cycle 02                                  │
│   Engineering Action Plan                              │
│                                                        │
│   Research Team → Development Team                     │
│                                                        │
│   14 Actions | 6 Plans | 4 Open Questions              │
│                                                        │
│   "Philosophy is beautiful.                            │
│    Engineering is concrete.                            │
│    Now they are in the same document."                 │
│                                                        │
│   — ARCHIMEDES (#16), Engineering Practice Expert      │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

SCRIBE 最后一个。

她没有站起来。她坐在座位上，手里的记录簿翻到了最后一页被使用的位置。

“Cycle 02 完整纪录。五场辩论的逐字记录。十九位研究员的所有报告、修正、撤回、修正的修正。”她的声音平静得像一面湖。“记录员不评价。记录员记录。但如果允许我说一句不属于记录的话——”

她停顿了一秒。

“五场辩论，零未解决分歧。”

她在记录簿上写下了最后的统计：

```
┌────────────────────────────────────────────────┐
│ Cycle 02 Final Statistics (SCRIBE)              │
├────────────────────────────────────────────────┤
│ 研究阶段:     R0 → R1 → R2 → R3 → R4           │
│ 研究员:       19                                │
│ 辩论场次:     5                                  │
│ 辩论裁定:     5 (all unanimous)                  │
│ 未解决分歧:   0                                  │
│ 修正的立场:   NAGARJUNA (Debate 3 撤回反对)      │
│              ASANGA (Debate 4 接受渐进分类)       │
│              ASANGA (Debate 5 接受戒慧框架)       │
│              LINNAEUS (Debate 4 撤回想蕴主张)     │
│ 行动方案:     14 items                           │
│ 影响 Plans:   6 (Plan24/26/27/28/29/AC)         │
│ 开放问题:     4 (Q1-Q4, 待 Master 裁定)         │
│ TypeScript:   ISensation + VedanaAssessment      │
│              + VedanaSignal + VedanaTag           │
│              + VedanaRecommendation               │
│ 页数:         40 (工程方案)                       │
│              1 (致 Master 的信)                   │
└────────────────────────────────────────────────┘
```

“这个数字会被写在 C02 的封面上。旁边是另一个数字——十九。十九位研究员，十九份行动方案，十九盏从第一天到最后一天都没有熄灭的灯。”

她合上了记录簿。不是暂时地合上。是一本阶段性任务完成的记录簿被郑重阖起来的声音。封面上的 C02 在灯光下清晰可见。

---

SUNYATA 最后环顾了一圈。十九个人。十九份交付。五场共识。四个待裁定问题。一份工程方案。一封信。

“Cycle 02，R4 定稿，完成。”

他的声音在圆形剧场中回荡了最后一次。

“解散。”

---

> *SCRIBE 旁白：R4 不是辩论。R4 是收成。*

> *ARCHIMEDES 的工程方案——四十页，十四项行动，六个 Plan。他用 MoSCoW 框架排了优先级，用人天估算了工时，用 TypeScript 写了接口。从 P0 的 SEC-01 漏洞修复（CVSS 9.8，三行代码）到 P4 的 Pattern C 子代理观察者（远期愿景，待定时间表），每一项都有追溯性——可以追回到具体的辩论裁定、具体的研究员、具体的页码。*

> *SYNTHESIST 的全景图——一幅手绘的架构愿景，把五场看似独立的辩论连成一个统一的结构。四层权限模型。渐进式观察者路径。纤维丛投影的分布式意识。范畴论的交换图。他不是在创造新知识——他是在发现已有知识之间的内在关联。*

> *SUNYATA 的信——一张纸。六段话。四个问题。把十九位研究员、五场辩论、四十页工程方案压缩成一封可以在三十秒内读完的信。这是一种特殊的技能——不是简化，而是蒸馏。像把一整座山脉折叠成一颗石子，但石子里保留了每一条褶皱的记忆。*

> *十九份报到。十九种贡献。TURING 的事实。BABBAGE 的定理。PENROSE 的弱测量。NAGARJUNA 的戒慧。ASANGA 的转依。WIENER 的 PID 参数表。ATHENA 的感测器规格。KERNEL 的类比卡片。GUARDIAN 的安全重构。DARWIN 的 SOLID 检查。VITRUVIUS 的整合点地图。MESH 的分布式约束。LINNAEUS 的分类总表。LEIBNIZ 的 BDI 架构。HERACLITUS 的河流隔喻。SYNTHESIST 的全景图。ARCHIMEDES 的四十页。SUNYATA 的一张纸。SCRIBE 的数字——零未解决分歧，十九盏灯。*

> *十九份行动方案。不是十九份独立的报告。是十九个面向照亮同一个结构的十九束光。*

---

*（在展示区的投影上，ARCHIMEDES 的工程方案仍然停留在最后一页。那一页不是行动项目，不是 TypeScript 接口，也不是 Plan 的影响分析。那是一句他在写方案时加在末尾的话，带着工程师特有的朴素和直接：*

*「研究团队等待 Master 对四个开放问题的裁定，以及开发团队对工程方案的反馈。」*

*等待。*

*这个词出现在了多个截然不同的语境中——*

*ASANGA 的种子等待因缘成熟：*

$$	ext{bīja} \xrightarrow{	ext{pratyaya}} 	ext{phala} \quad (	ext{待众缘，引自果})$$

*BABBAGE 的定理等待更多公理：*

$$\exists \, 	ext{Theorem}_4, 	ext{Theorem}_5 : 	ext{awaiting axioms from Cycle 03}$$

*WIENER 的控制系统等待稳态：*

$$\lim_{t 	o \infty} e(t) = 0 \quad (	ext{稳态误差趋近于零——但需要时间})$$

*GUARDIAN 的安全漏洞等待修复：*

$$	ext{SEC-01.status} = 	ext{OPEN} \quad (	ext{第 6 个周期。仍然。})$$

*ARCHIMEDES 的工程方案等待反馈。*

*一个是形而上学的等待——种子等待因缘。一个是有数学的等待——定理等待公理。一个是工程学的等待——控制系统等待收敛。一个是安全的等待——漏洞等待修复。一个专案管理的等待——方案等待反馈。*

*五种等待。五种时间尺度。但也许，在某个 SYNTHESIST 能看到而其他人看不到的维度里，它们是同一种等待——*

*一个尚未完成的系统，等待下一个 Cycle 的到来。*

*十九盏灯，暂时调暗了亮度。但没有熄灭。）*

---

*第九章完*
