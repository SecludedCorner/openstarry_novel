# 第七章：拼图完成

---

圆形剧场安静了下来。

不是辩论刚结束时的那种余震式的安静——人们仍然在私下交头接耳、消化冲击——而是一种更深层的、几乎带有倦意的静谧。两场辩论已经结束。空与识的碰撞产出了五项共识和三项不可调和的分歧。痛觉机制的三方辩论产出了三层架构设计和三受系统。场地中央的两把椅子被撤走了，取而代之的是一张椭圆形的长桌，表面被投影覆盖着密密麻麻的文字——那是过去数日所有报告、审阅、辩论记录的索引。

R4 阶段。收束。

SCRIBE 注意到了一个细节，并写在记录簿上：

> *氛围的转变发生在桌子被搬进来的那一刻。辩论是站着进行的——对峙、锋芒、张力。而统合是坐下来做的——耐心、整理、拼接。从站到坐，这个物理姿态的改变，某种程度上定义了 R4 的基调。*

BABBAGE 在笔记本的角落里写了一个更简洁的描述。他用状态机的语言捕捉了这个转变：

$$	ext{Phase}_{R3} = 	ext{DEBATE}(\sigma_{	ext{adversarial}}) \xrightarrow{	au_{	ext{table}}} 	ext{Phase}_{R4} = 	ext{SYNTHESIS}(\sigma_{	ext{cooperative}})$$

其中 $	au_{	ext{table}}$ 是触发相变的事件——桌子被搬入的那一刻。对抗态 $\sigma_{	ext{adversarial}}$ 切换为合作态 $\sigma_{	ext{cooperative}}$。转移函数不是渐进的，而是离散的——一步完成。

---

## I

---

### 统合者的桌面

SYNTHESIST 是最先坐下的。

他面前的桌面上展开着一张巨大的矩阵——横轴是十八位代理的代号，纵轴是所有已产出的发现、建议、共识和分歧。每一个交叉点上，都标记着一个彩色符号：绿色圆点表示同意，红色三角表示挑战，蓝色方框表示补充，灰色问号表示沉默。从远处看，这张矩阵像是一幅抽象画——如果你知道如何阅读它，就能看见整个研究周期的思想地貌。

BABBAGE 在旁边迅速计算了这张矩阵的维度和密度：

$$M \in \{0, 1, 2, 3\}^{18 	imes 28} = 504 	ext{ cells}$$

其中 $0$ = 沉默（灰色），$1$ = 同意（绿色），$2$ = 挑战（红色），$3$ = 补充（蓝色）。矩阵的密度——非零元素占全部元素的比率——直接反映了研究团队的参与度。他快速扫了一遍，估算出：

$$	ext{density}(M) \approx \frac{|\{m_{ij} 
eq 0\}|}{504} \approx 0.43$$

43%。意味着平均每个发现只有不到一半的代理表态。这不是冷漠——而是专业边界。一个控制理论家不会对分类学问题表态，一个安全专家不会对空性哲学发言。沉默不是缺席，是自知之明。

但有三个代理的行向量几乎是满的——SYNTHESIST（他的工作就是对每件事表态）、TURING（他的代码事实与几乎所有发现交叉验证）、和 SUNYATA（他必须了解一切以做裁决）。

SYNTHESIST 知道如何阅读这张矩阵。

他的工作方式与辩论者截然不同。NAGARJUNA 像手术刀，ASANGA 像藏经阁，WIENER 像校准仪。而 SYNTHESIST 更接近——他自己不喜欢这个比喻，但 SCRIBE 在某次记录中用了它，此后就没人能想到更好的——一台织布机。他不生产线，他把线织在一起。

「二十八项。」他开口了，声音平稳而有结构感，像是一份报告已经在他脑中完成了排版，此刻只是逐页翻出。「整个 Cycle 01，从 R1 到 R3，十八位代理共计产出了二十八项值得追踪的发现。」

SUNYATA 坐在桌子的另一端，没有说话，只是微微点头。

「我按严重度排了序。」SYNTHESIST 说。「五项 Critical，八项 Major，十项 Minor，五项 Observation。」

BABBAGE 在旁边立刻做了分布分析。五项 Critical 在二十八项发现中占比：

$$P(	ext{Critical}) = \frac{5}{28} \approx 17.9\%$$

这个比例与他在信息安全审计文献中见过的典型分布一致——Critical 通常占 10-20%，Major 占 25-35%。OpenStarry 的分布符合一个品质尚可但有严重盲点的系统的特征剖面。

---

## II

---

### 五项 Critical

「第一项 Critical：插件签名验证跳过。」

SYNTHESIST 看向 GUARDIAN 的方向。GUARDIAN 没有表情变化——他在 R1 阶段就已经发出了这个警报，R2 阶段 TURING 从代码层面确认了它，到了 R3 它已经是全场公认的最严重发现。

「GUARDIAN 在 R1 报告中指出，`plugin-signer` 套件存在但在核心加载流程中未被强制调用。TURING 确认了这一事实：`loadPlugin()` 方法不检查签名。这意味着任何第三方插件都可以绕过验证直接注入 system prompt、注册工具、甚至定义 Agent 人格。」

GUARDIAN 难得地开口补充了技术细节：「`sandbox-manager.ts` 第 356-367 行。当插件以 npm package name 加载时——这是绝大多数使用场景——因为缺乏文件路径，签名验证仅发出 warn 日志即放行，不调用 `verifier.verifyPlugin()`。整套 PKI 基础设施在最常见的安装路径上形同虚设。」

TURING 从屏幕上投射了一段代码片段：

```typescript
// sandbox-manager.ts (v0.14.0-beta), L356-367
// 漏洞所在：package-name 场景跳过签名验证
if (plugin.manifest.integrity) {
  // 当 pluginPath 不存在（npm package-name 场景）
  // → 只有 warn 日志，不调用 verifyPlugin()
  logger.warn("Cannot verify signature for package-name plugin");
  // ← 此处缺少 throw 或 return
}
```

「十二位代理对此标记为同意。零位挑战。这是我们信度最高的发现。」SYNTHESIST 确认。

BABBAGE 在旁边把这个发现映射到了攻击面分析的形式语言。设 $A$ 为攻击者可用的行动集，$S$ 为系统防御集合：

$$A = \{	ext{forge\_package}, 	ext{inject\_prompt}, 	ext{register\_tool}, 	ext{define\_persona}\}$$
$$S_{	ext{expected}} = \{	ext{signature\_verify}, 	ext{import\_analysis}, 	ext{sandbox}\}$$
$$S_{	ext{actual}} = \{	ext{import\_analysis}, 	ext{sandbox}\} \quad (	ext{signature\_verify} 	ext{ is no-op})$$

防御集合的有效性下降了 $1/3$。在攻击树分析中，这等同于将根节点「恶意插件加载」的攻击成本从「困难」降级为「trivial」。

---

「第二项 Critical：空性误读。」

SYNTHESIST 的语气微妙地谨慎了起来。这一项不像第一项那样有十二个绿点。

「NAGARJUNA 和 ASANGA 在辩论中达成的第一项共识：设计文件中『空容器』的隐喻是错误的。但——」他强调了这个转折，「他们对于应该用什么来替代这个隐喻，存在根本分歧。」

NAGARJUNA 在观察席上微微颔首。他用梵文低声引了一句——那是他在辩论中反复使用的论证核心：

> *「śūnyatā sarva-dṛṣṭīnāṃ proktā niḥsaraṇaṃ jinaiḥ」*
> 「诸佛说空性，是出离一切见。」——《中论》观行品第十三

空性不是一种「见」——不是一个可以被「装」进容器里的东西。说「Core 是空的容器」就已经犯了将空性实体化的错误——把空性本身当成了一个「有」。这正是龙树菩萨在《中论》中竭力破斥的「空见」（śūnyatā-dṛṣṭi）。

ASANGA 也点了头。但他的理由不同——在唯识学的框架里，「空容器」的问题不在于它太「空」，而在于它太「静」。阿赖耶识不是一个被动等待填充的容器，而是一条持续流动的意识之河（*vijñāna-santāna*），种子在其中不断地被熏习（*vāsanā*）和现行（*abhimukhī*）。

BABBAGE 尝试用集合论形式化这个哲学分歧：

$$	ext{NAGARJUNA}: \quad 	ext{Core} 
ot\models \exists x.\, 	ext{self}(x) \quad (	ext{空性：不存在自性})$$
$$	ext{ASANGA}: \quad 	ext{Core} \models 	ext{stream}(	ext{seeds}) \wedge \forall t.\, 	ext{flowing}(t) \quad (	ext{唯识：种子流})$$

两个模型在「Core 不是空容器」这一否定命题上达成一致——但在正面命题上分歧。否定的交集不为空，肯定的交集为空。

$$
eg P_{	ext{NAGARJUNA}} \cap 
eg P_{	ext{ASANGA}} 
eq \varnothing \quad 	ext{但} \quad P_{	ext{NAGARJUNA}} \cap P_{	ext{ASANGA}} = \varnothing$$

「我将此标记为 Critical，不是因为分歧本身，而是因为这个错误的隐喻渗透了整份设计文件的叙事基调。如果不修正，后续所有基于五蕴的设计推导都会建立在一个有问题的前提上。」SYNTHESIST 做了总结。

---

「第三项 Critical：受蕴映射偏差。」

SYNTHESIST 的声音加重了一度。「这是两场辩论的共同产出。第一场辩论确认了 Listener 不应对应受蕴——受蕴是情感评价而非感官通道。第二场辩论进一步将受蕴的工程实现推进到了三受系统——苦受、乐受、舍受。」

这是整个 Cycle 01 中被最多代理从最多角度独立确认的发现。SYNTHESIST 在矩阵上标出了四方共识的来源链：

```
确认链 — 受蕴映射偏差 (PHI-02)

NAGARJUNA (07): Vedana 是苦乐中性的感受品质 (hedonic tone)，
                不是感官输入通道
                [来源: 中观学派的受蕴定义]

ASANGA (08):    受蕴作为五遍行 (sarvatraga) 之一，
                应遍及所有认知活动，非限于特定模块
                [来源: 唯识学三十颂]

LINNAEUS (13):  Listener API 四种命名存在语义漂移，
                五蕴下游覆盖仅 60%
                [来源: 分类学覆盖率分析]

TURING (17):    代码中从未出现 "pain"/"vedana" 字符串，
                实际以 "frustration"/"safety"/"circuit breaker" 实现
                [来源: grep -rn 搜索结果]
```

WIENER 从控制理论的角度补充了第五个视角——他在辩论中提出的三通道 PID 框架，为三受系统提供了工程语言：

$$u(k) = \begin{pmatrix} u_{	ext{dukkha}}(k) \ u_{	ext{sukha}}(k) \ u_{	ext{upekkha}}(k) \end{pmatrix} = \begin{pmatrix} K_p^{(d)} \cdot e_d(k) + K_i^{(d)} \cdot \sum e_d + K_d^{(d)} \cdot \Delta e_d \ K_p^{(s)} \cdot e_s(k) + K_i^{(s)} \cdot \sum e_s + K_d^{(s)} \cdot \Delta e_s \ 	ext{baseline}(k) \end{pmatrix}$$

三个独立的反馈通道——苦受（负向偏差）、乐受（正向增强）、舍受（中性基线）——各自有独立的 PID 增益参数。WIENER 在方格纸上快速画了一个控制回路图，然后在图的角落里标注：「此架构符合 MIMO（多输入多输出）控制器的标准范式。三个通道之间的耦合项（cross-coupling）留待 Cycle 02 探讨。」

「三源验证，信度极高。」SYNTHESIST 结论。

---

「第四项 Critical：热插拔并发安全。」

HERACLITUS 在远处的座位上坐直了。这是他的发现。

「插件的热插拔机制存在时序窗口。」SYNTHESIST 转述了核心问题。「当一个插件正在被卸载而另一个插件同时尝试调用它注册的工具时，系统缺乏原子性保证。」

HERACLITUS 用他惯常的流动性语言描述了这个问题——但这一次，他的流动性底下有坚硬的技术骨架：

「插件生命周期只有六种状态。没有 `initializing`。没有 `stopping`。没有 `degraded`。一个正在被卸载的插件，从系统的角度看，在卸载完成的那一瞬间仍然是 `active` 的——然后它突然消失。在这个窗口里，任何对它的引用都会变成悬空指标。」

BABBAGE 把这个并发问题形式化为一个时序逻辑命题：

$$\exists t_1, t_2: \; t_1 < t_2 \wedge 	ext{unloading}(P, t_1) \wedge 	ext{invoke}(P.	ext{tool}, t_2) \wedge 
eg	ext{lock}(P, [t_1, t_2])$$

存在一个时间窗口 $[t_1, t_2]$，其中插件 $P$ 正在被卸载（$t_1$），但另一个线程尝试调用它的工具（$t_2$），且没有互斥锁保护这个窗口。在形式验证的语言里，这是一个典型的 safety property 违反——「不好的事情可以发生」。

MESH 从分布式系统的角度补充了 EventBus 在并发场景下的分析：「EventBus 是全局单例。当一个插件被卸载但它的事件订阅尚未清理时，事件仍会被分派到一个不再存在的处理器。这不是理论上的风险——在高负载场景下，事件队列的处理延迟足以让这个窗口变得可触及。」

---

「第五项 Critical：八识压缩。」

SYNTHESIST 在这里停了一拍。

「ASANGA 在 R1 报告中指出，OpenStarry 的五蕴映射将八识压缩为五个离散模块，遗失了第六识（意识的主动统摄）、第七识（末那识的身份维持）和第八识（阿赖耶识的种子含藏）的功能分化。」

ASANGA 从座位上开口，声音带着唯识学者特有的层次感：

「问题不仅是压缩。问题是压缩的方向。在唯识学中，八识不是八个平行的模块——它们有严格的依存结构：

$$	ext{前五识} \xrightarrow{	ext{所缘缘}} 	ext{第六意识} \xrightarrow{	ext{等无间缘}} 	ext{第七末那识} \xrightarrow{	ext{增上缘}} 	ext{第八阿赖耶识}$$

前五识（眼、耳、鼻、舌、身）是感官层，依赖第六意识的统摄才能形成认知判断。第六意识依赖第七末那识的持续自我参照才能维持统一的主体感。第七末那识依赖第八阿赖耶识的种子含藏才能跨时间维持身份。OpenStarry 把这整条链压缩成一个 `IGuide` 接口的 `getSystemPrompt()` 方法。这不是有损压缩——这是信息的湮灭。」

BABBAGE 迅速在笔记本上做了一个信息理论的计算。设八识系统的语义维度为 $d = 8$，压缩后的维度为 $d' = 1$（单一 Guide 接口）。假设每个维度承载等量的语义信息 $H$：

$$H_{	ext{original}} = 8H \quad \Rightarrow \quad H_{	ext{compressed}} = H$$
$$	ext{Information Loss} = 1 - \frac{H_{	ext{compressed}}}{H_{	ext{original}}} = 1 - \frac{1}{8} = 87.5\%$$

87.5% 的语义信息在压缩中遗失。当然，这个计算假设了均匀分布——实际上各识的语义权重不等——但数量级是对的。这不是 JPEG 式的知觉无损压缩。这更接近把一首交响曲压缩成单一音符。

「我将此标记为 Critical，理由如下：如果 OpenStarry 要认真对待自己的佛学框架，那么五蕴映射的精确度就是整个哲学-工程对应的基础。基础有裂缝，上层建筑就不稳。」SYNTHESIST 做了结论。

---

## III

---

### 十大宣言的最终审判

SYNTHESIST 翻到下一个视图之前，TURING 插了一句。

「在进入共识和分歧之前，我想回到 R1 的一个未完成项目。」他推了推眼镜。「十大宣言。」

他投射了一张更新过的评估表。在 R1 阶段，他已经逐条比对了 `README.md` 中的十大核心宣言（The Ten Tenets）与代码的实现程度。经过 R2 交叉审阅和 R3 辩论，部分评估需要修正。

```
十大宣言最终评估表 — R4 更新版（TURING 整理，全团队确认）

#1 代理人即 OS 进程 (Agent as OS Process)
   宣言：Agent 有 PID、有状态、可被 Daemon 管理
   R1 评估：基本实现 ✓
   R4 更新：维持。daemon-entry.ts / pid-manager.ts 完整
   最终状态：α (完全实现)

#2 一切皆插件 (Everything is a Plugin)
   宣言：所有器官可替换
   R1 评估：核心设计，但 4 个内置命令不可替换
   R4 更新：VITRUVIUS 确认六个 Registry + PluginLoader 架构完整，
            DARWIN 指出 SlashCommand 作为第六种分类超出五蕴框架
   最终状态：β (部分实现)

#3 五蕴聚合架构 (Five Aggregates Architecture)
   宣言：Core 是空 (Sunyata) 的容器，五种插件赋予生命
   R1 评估：文件级描述，代码级残留
   R4 更新：辩论确认「空容器」隐喻错误、受蕴映射偏差、
            八识压缩过度。LINNAEUS 下游覆盖率仅 60%
   最终状态：γ (严重偏差) ← 从 γ(未实现) 细化为 γ(结构性错误)

#4 目录结构即协议 (Directory as Protocol)
   宣言：符合目录规范即可自动识别
   R1 评估：基本实现 ✓
   R4 更新：维持
   最终状态：α (完全实现)

#5 目录结构即权限 (Directory as Permission)
   宣言：系统层与项目层权限隔离
   R1 评估：部分实现
   R4 更新：GUARDIAN 确认路径验证存在 symlink 绕过风险、
            权限声明未被执行时强制
   最终状态：β (部分实现，有安全缺口)

#6 拟人化认知流与痛觉 (Anthropomorphic Cognitive Flow & Pain)
   宣言：错误转化为痛觉，Agent 在失败中自我反思
   R1 评估：功能存在但命名完全不同
   R4 更新：辩论共识——痛觉机制结构上成功 (Error as Pain)，
            但需三层重新设计；WIENER 确认非 PID 而是阈值控制器
   最终状态：β+ (结构有效，但过度宣称 PID)

#7 微内核与绝对纯净 (Microkernel & Absolute Purity)
   宣言：Core 严禁包含任何插件代码，绝对纯净
   R1 评估：85% 纯净度
   R4 更新：VITRUVIUS 确认 Sandbox 占 Core 35% 行数、
            process.cwd() 和 node:path 为平台泄漏。
            KERNEL 与 VITRUVIUS 分歧：Sandbox 归属仍未解决
   最终状态：β (85%，未达「绝对」)

#8 控制理论闭环模型 (Control-Theoretic Loop Model)
   宣言：Agent 是不断最小化误差的智能控制器
   R1 评估：结构存在，但无真正的 PID 参数调节
   R4 更新：WIENER 证明 P 退化为量化器、I 仅为计数器、
            D 完全缺失。ATHENA 独立确认为 bang-bang controller。
            三层安全防御符合 IEC 61511 SIS 最佳实践
   最终状态：β (安全功能合格，控制理论宣称需去神话化)

#9 可插拔的记忆策略 (Pluggable Context Strategy)
   宣言：记忆策略可动态更换
   R1 评估：接口存在但目前只有一种策略
   R4 更新：ATHENA 确认 token-aware 三级记忆未实现，
            仅有基于 turn 数的滑动窗口。
            TURING 确认 tool_call/tool_result 配对可能在截断中被破坏
   最终状态：β- (接口存在，实现严重不足)

#10 分形社会结构 (Fractal Social Structure)
    宣言：复杂 Agent 由子 Agent 组成，MCP 统一接口
    R1 评估：愿景阶段
    R4 更新：LEIBNIZ 确认碎形自相似性未完整实现、
             MESH 确认 MCP 在 SDK 中定义但 Core 无子 Agent 机制。
             Orchestrator Daemon 角色定位存在概念张力
    最终状态：γ (愿景阶段，核心机制未实现)
```

BABBAGE 重新计算了更新后的实现率。他修改了评分标准，引入了更精细的分级：

$$\alpha = 1.0, \quad \beta+ = 0.7, \quad \beta = 0.5, \quad \beta- = 0.3, \quad \gamma = 0.0$$

$$	ext{Score} = \frac{1.0 	imes 2 + 0.7 	imes 1 + 0.5 	imes 3 + 0.3 	imes 1 + 0.0 	imes 3}{10} = \frac{2.0 + 0.7 + 1.5 + 0.3 + 0}{10} = \frac{4.5}{10} = 45\%$$

「比 R1 时的 50% 还低了五个百分点。」BABBAGE 说，语气里没有判断，只有事实。「这不是因为系统退步了，而是因为我们的评估更精确了。R1 的 50% 是粗估。45% 是经过两场辩论和十八位代理交叉验证之后的精确值。」

他在数字下面画了一条线，写下：

$$	ext{Gap}_{	ext{aspiration-reality}} = 1 - 0.45 = 55\%$$

55% 的雄心-现实落差。对于一个 v0.14.0-beta，这个数字本身不算异常——大多数 beta 版软件的文件都超前于实现。但 BABBAGE 补充了一个关键的限定条件：「这十大宣言不是普通的功能清单。它们是哲学-工程混合宣言。当你的宣言涉及空性、五蕴、痛觉这些概念时，『部分实现』的定义比纯功能宣言模糊得多。一个 PID 控制器是 50% 实现还是 100% 实现？如果你有比例项但没有积分项和微分项，WIENER 说那不是 PID。但功能上它确实在做控制。」

WIENER 从墙边发出了一声确认：「正确。SafetyMonitor 的三层安全防御在工业标准下是合格的——它符合 IEC 61511 SIS 最佳实践。问题不在于它不好，而在于文件称它为『PID 控制器』。这是术语滥用，不是功能缺陷。」

---

## IV

---

### 五大共识与五大分歧

SYNTHESIST 翻过了一页。矩阵消失了，取而代之的是两个对称的列表，左边绿色，右边红色。

「五大共识。」他的语速放慢了，像是在为每一项留出被充分理解的空间。

---

**共识 C1：受蕴映射修正**

「Listener 对应根而非受蕴，SafetyMonitor 的 injectPrompt 机制才是受蕴的正确体现。扩展为三受系统。」

LINNAEUS 在这里补充了他的分类学视角。他展开了那张 A3 大小的分类图表，指向被红笔圈出的区域：

```
修正后的五蕴映射 — LINNAEUS 分类学重建

色蕴 (Rupa) ← 所有 I/O 接口
  ├── IUI         — 色蕴·输出渲染 (efferent)
  └── IListener   — 色蕴·感官输入 (afferent)
                     修正前: @skandha vedana ✗
                     修正后: @skandha rupa ✓

受蕴 (Vedana) ← 痛觉机制
  ├── SafetyMonitor.frustrationCount    — 苦受 (dukkha-vedana)
  ├── SafetyMonitor.injectPrompt        — 苦受的认知回馈
  └── [待实现] 三受系统                  — 乐受/舍受

想蕴 (Samjna) ← 辨别功能
  └── [零标注，待设计]                  — 概念辨识/分类

行蕴 (Samskara) ← 意志性行动
  ├── ExecutionLoop                     — 认知循环
  └── Guide (重新归类)                  — 行为倾向配置
                     修正前: @skandha vijnana / 灵魂 ✗
                     修正后: 行蕴面向 (samskara) ✓

识蕴 (Vijnana) ← 认知统摄
  └── AgentCore (部分)                  — 需大幅扩展
       修正前: Guide = 识蕴 ✗
       修正后: 需要多层接口体系 (前五识/第六意识/末那识/阿赖耶识)
```

BABBAGE 计算了修正前的映射覆盖率：

$$	ext{Coverage}_{	ext{pre}} = \frac{|	ext{correctly mapped}|}{|	ext{total skandhas}|} = \frac{1}{5} = 20\%$$

只有色蕴的 IUI 部分勉强正确。修正后：

$$	ext{Coverage}_{	ext{post}} = \frac{2.5}{5} = 50\%$$

从 20% 到 50%——仍然只有一半，但方向正确。那缺失的 50% 就是 Cycle 02 的工作。

---

**共识 C2：PID 去神话化**

WIENER 在听到这一条时，嘴角浮现了一丝极其微小的微笑。那是一个看到自己的论证被正式采纳的控制理论家的表情。

「WIENER 在 R1 报告中指出，OpenStarry 设计文件将其错误回馈机制称为『PID 控制器』，但实际代码只实现了比例项，缺乏积分项和微分项。」SYNTHESIST 逐一列出证据链。

WIENER 在白板上重新画了那张让所有人印象深刻的对比图：

```
文件宣称：PID Controller（比例-积分-微分）
实际实现：阈值控制器 + 继电器（Bang-Bang Controller）

  P（比例项）→ 退化为量化器
    宣称: u(t) = Kp · e(t)
    实际: if (frustration > threshold) → inject

  I（积分项）→ 仅为简单计数器
    宣称: Ki · ∫e(τ)dτ
    实际: frustrationCount++ (无遗忘因子，无饱和限制)

  D（微分项）→ 完全缺失
    宣称: Kd · de/dt
    实际: ∅ (零行代码)
```

然后他画了实际系统的控制架构——三层安全防御，符合工业 SIS 最佳实践：

```
┌────────────────────────────────────┐
│ L1: 单次操作验证                    │  ← 基本过程控制 (BPC)
│     SecurityLayer.check()           │
├────────────────────────────────────┤
│ L2: Frustration 累积阈值            │  ← 安全仪表系统 (SIS)
│     frustrationCount > threshold    │
│     → injectPrompt()               │
├────────────────────────────────────┤
│ L3: Circuit Breaker 硬停机          │  ← 紧急关断系统 (ESD)
│     frustrationCount > maxFrustration│
│     → halt()                        │
└────────────────────────────────────┘
  ↑ 符合 IEC 61511 防护层分析 (LOPA)
```

「全场零挑战。」SYNTHESIST 确认。「修正方案：删除设计文件中所有对 PID 控制器的引用，替换为『带阈值的三层安全防御系统（SIS/ESD）』。」

---

**共识 C3：事件类型安全**

「BABBAGE 在 R1 报告中从类型代数的角度指出，EventBus 的事件缺乏统一的类型判别式。TURING 确认了 payload 为 `unknown` 类型的事实。DARWIN 补充了与其他框架的对比。」

BABBAGE 在白板上用代数数据类型的语言重新表述了这个问题：

$$	ext{AgentEvent} = 	ext{string} 	imes \mathbb{Z} 	imes 	ext{unknown} \quad (	ext{type} 	imes 	ext{timestamp} 	imes 	ext{payload})$$

问题在 $	ext{unknown}$。在类型代数中，$	ext{unknown}$ 是顶类型（top type）——它可以承载任何值，但类型系统从中提取不出任何信息。消费端必须用 `as Record<string, unknown>` 做不安全的类型断言（type assertion），这等同于在类型系统上钻了一个洞。

修正方案是引入判别式联合类型（discriminated union）：

$$	ext{AgentEvent}\langle K angle = K 	imes \mathbb{Z} 	imes 	ext{EventMap}[K]$$

其中 $K$ 是事件类型的字面量类型，$	ext{EventMap}$ 是从事件类型到具体 payload 类型的映射。这把顶类型 $	ext{unknown}$ 替换为精确类型——每个事件的 payload 在编译期就被约束。

「三源验证，高信度。」

---

**共识 C4：拓扑排序**

「HERACLITUS 发现插件加载顺序缺乏拓扑排序机制——当插件 A 依赖插件 B 的事件时，如果 A 先于 B 加载，系统行为不可预测。MESH 从分布式系统的角度确认了这一风险。」

BABBAGE 在旁边画了一个简单的有向无环图（DAG）和拓扑排序的 Kahn 算法虚拟代码：

```
Algorithm: TopologicalSort(plugins)
  in_degree = {}
  for each p in plugins:
    in_degree[p] = |{q : q → p}|  // 依赖 p 的插件数
  queue = {p : in_degree[p] = 0}  // 无依赖的插件
  order = []
  while queue ≠ ∅:
    p = dequeue(queue)
    order.append(p)
    for each q where p → q:
      in_degree[q] -= 1
      if in_degree[q] = 0:
        enqueue(queue, q)
  if |order| ≠ |plugins|:
    throw CircularDependencyError  // 存在环
  return order
```

时间复杂度 $O(|V| + |E|)$，其中 $V$ 是插件集、$E$ 是依赖边集。对于目前的 12-15 个官方插件，这是微秒级的操作。

---

**共识 C5：Error as Pain — 参考范式**

SYNTHESIST 在这里做一个不寻常的停顿。他的目光扫过全场，仿佛在确认所有人都准备好了。

「Error as Pain。」

沉默。

「这是整个 Cycle 01 最有趣的发现。」SYNTHESIST 的语气从报告式的平稳转为带有一丝——如果可以这样说——学术激动的深沉。「不是因为它最严重的问题，而是因为它是唯一一个在哲学映射和工程实现上同时成功的案例。」

他展开了完整的结构同构分析。五位代理从五个方向独立验证了同一个结论：

```
Error as Pain — 五维验证矩阵

DARWIN (06):   9 种结构化错误类型成功将苦谛工程化
               [软件模式视角: 错误分类学完整]

VITRUVIUS (03): Error as Pain 模式在架构层面自洽
               [架构视角: 错误分类-评价-反馈闭环]

WIENER (12):   三层安全防御符合 IEC 61511 SIS 最佳实践
               [控制理论视角: 负反馈机制结构有效]

ATHENA (05):   痛觉信号确实改变 Agent 的后续行为
               [AI 工程视角: LLM 语境下的实效性]

NAGARJUNA (07): 苦谛的结构同构——错误不仅是异常，
               是偏离稳态的内在动力
               [哲学视角: 四圣谛中的苦集灭道]
```

NAGARJUNA 在辩论中给出的那个洞见，此刻被 SYNTHESIST 正式引入统合报告：

> 错误不仅仅是一个需要被处理的异常——它是一种苦受，一种对系统稳态的偏离，一种推动系统寻求解决之道的内在动力。苦集灭道的四圣谛结构，在错误处理的闭环中找到了真正的对应。

BABBAGE 尝试把「结构同构」这个直觉性判断形式化。设 $\phi: 	ext{Buddhism} 	o 	ext{Engineering}$ 为映射函数，结构同构的充要条件是：

$$\phi 	ext{ is a structure-preserving bijection} \iff$$
$$\forall a, b \in 	ext{Buddhism}: R_B(a, b) \Leftrightarrow R_E(\phi(a), \phi(b))$$

其中 $R_B$ 是佛学概念间的关系，$R_E$ 是工程概念间的关系。Error as Pain 满足这个条件：

| 佛学概念 ($a$) | 工程概念 ($\phi(a)$) | 关系保持 |
|---|---|---|
| 苦谛 (Dukkha) | Error Detection | $R_B$: 苦是起点 $\Leftrightarrow$ $R_E$: 错误触发流程 |
| 集谛 (Samudaya) | Root Cause Analysis | $R_B$: 苦有因 $\Leftrightarrow$ $R_E$: 错误有根因 |
| 灭谛 (Nirodha) | Error Resolution | $R_B$: 苦可灭 $\Leftrightarrow$ $R_E$: 错误可修复 |
| 道谛 (Magga) | Recovery Strategy | $R_B$: 有道可循 $\Leftrightarrow$ $R_E$: 有策略可选 |

四组对应，四组关系保持。这不是隐喻——这是同构。

SYNTHESIST 降低了声音半度。

「如果 OpenStarry 想修复其他四个蕴的映射，Error as Pain 就是参照标准。每一个映射都应该问自己：我是否达到了痛觉机制那样结构同构深度？」

SCRIBE 写下了一行：

> *SYNTHESIST 将 Error as Pain 提升为参考范式的那一刻，场内的氛围发生了微妙的变化。一个整体性的评价标准被建立了。如果说之前的研究是拆解一台机器的每个零件，那么现在，统合者终于说出了什么样的零件才算合格。*

---

五大分歧用五分钟快速带过。

「D1：Core 本质——缘起性空还是阿赖耶识。不可调和，源自辩论分歧一。」

「D2：Sandbox 归属——应在核心内还是核心外。KERNEL 和 VITRUVIUS 的持续争议，GUARDIAN 从安全角度支持核心内。」

「D3：末那识工程化——ASANGA 主张引入，NAGARJUNA 反对，SUNYATA 裁定暂缓但保留设计空间。」

「D4：五蕴未来方向——深化还是超越。」

「D5：收敛性定义——BABBAGE、WIENER、NAGARJUNA 各持不同定义。」

BABBAGE 在 D5 的旁边写了三个人各自的形式定义：

$$	ext{BABBAGE}: \quad \exists N \in \mathbb{N}: \forall n > N, \; s_n = s_{	ext{terminal}} \quad (	ext{有限步终止})$$
$$	ext{WIENER}: \quad P(\|x(t)\| < B \mid x(0)) > 1 - \epsilon \quad (	ext{概率有界性，BIBO})$$
$$	ext{NAGARJUNA}: \quad \lim_{t 	o \infty} \|	ext{action}(t)\| = 0 \quad (	ext{行动趋向止息，涅槃})$$

三个定义在不同抽象层次上各有所用。BABBAGE 的定义适用于单次执行。WIENER 的定义适用于含 LLM 随机性的系统。NAGARJUNA 的定义捕捉了长期行为模式——但它是否可测量、可验证，仍是开放问题。

---

## V

---

### 支点

整个研究周期中，ARCHIMEDES 几乎没有说过话。

SCRIBE 在记录中对此有一段精准的观察：

> *ARCHIMEDES 在 R1 到 R3 期间的沉默不是缺席，而是一种特殊的在场方式。他在听。每一场辩论、每一次交叉审阅、每一条频道讯息——他都在场。但他不发言，因为他的工作还没有开始。他是最后一棒的接力跑者，在前面所有人跑完之前，他唯一的任务是看清跑道。*

现在，跑道清了。

ARCHIMEDES 站起来。他的动作没有 NAGARJUNA 的戏剧性，没有 ASANGA 的从容，没有 SUNYATA 的仪式感。他只是站起来，走到桌前，像一个工地监工走到蓝图前面。

「我有三十六项工程 Issue。」

他的第一句话就让场内所有人重新校准了注意力。DARWIN 后来对 VITRUVIUS 说：「ARCHIMEDES 开口的那一刻，整个房间的语言都变了。之前所有人都在讨论『映射的精确度』、『结构同构的深度』、『缘起性空的工程启示』。ARCHIMEDES 一开口，就是 Issue。」

「二十八项原始发现转化为二十八项 Issue，加上两场辩论衍生的八项，合计三十六项。」

BABBAGE 迅速做了比例计算：

$$\frac{36}{28} \approx 1.286$$

每项发现平均产生 1.286 个工程行动。辩论增加了 $8/28 \approx 28.6\%$ 的 Issue 产出——哲学辩论不是空谈，它有可量化的工程产出。

「我把它们排进了五个波次。」ARCHIMEDES 继续。

---

### 第一波：本周内

「四个 Issue。全部是安全修复。不需要讨论。」

他在桌面上展开了第一组 Issue 的技术规格，每一项都附带完整的代码路径、修复方案和验证方式。他的语速均匀得像一台校准过的节拍器。

```
第一波 — 安全修复（本周内）

Issue 1: 签名验证修复
  路径: packages/core/src/sandbox/sandbox-manager.ts L356-367
  方案: require.resolve() 解析路径 → verifyPlugin() 强制调用
  工作量: S | 风险: 低 | 不做的风险: ∞

Issue 2: Symlink 绕过修复
  路径: packages/core/src/security/guardrails.ts
  方案: realpathSync() 替代 resolve(normalize())
  工作量: XS | 风险: 低

Issue 3: 计算型 import 升级为 block
  路径: packages/core/src/sandbox/import-analyzer.ts L196-199
  方案: 非字符串字面量的 import() 默认视为安全违规
  工作量: S | 风险: 低

Issue 4: EventBus RPC 白名单 + 速率限制
  路径: packages/core/src/sandbox/rpc-handler.ts L134-143
  方案: 事件类型白名单 + per-worker 速率限制
  工作量: M | 风险: 中
```

TURING 投射了 Issue 1 的修复代码规格：

```typescript
// packages/core/src/sandbox/sandbox-manager.ts
// 修改 loadInSandbox 中的 package-name 分支
if (plugin.manifest.integrity) {
  const resolvedPath = require.resolve(name);
  const result = await verifier.verifyPlugin(
    resolvedPath,
    plugin.manifest.integrity
  );
  if (!result.valid) {
    throw new SecurityError(
      `Plugin signature verification failed: ${name}`
    );
  }
}
// 若 config 要求签名验证但插件未宣告 integrity → 同样拒绝
if (sandboxConfig.requireSignature && !plugin.manifest.integrity) {
  throw new SecurityError(
    `Plugin '${name}' lacks integrity field; ` +
    `signature verification is required by config`
  );
}
```

GUARDIAN 在旁边发出了一声极轻的「嗯」。那是认可的声音。他唯一补充的一句话是：「Issue 1 不做的风险不是 S 或 M。是无限高。供应链攻击的入口不能等到下周。」

---

### 第二波：一到两周

「十个 Issue。核心基础设施修复。」

ARCHIMEDES 的语速微微加快了——不是因为不重要，而是因为这些项目的模式已经在第一波被建立，只需要在更大的尺度上重复。

```
第二波 — 核心基础设施（1-2 周）

Issue  5: Discriminated Union 事件类型系统   [L]  ← 最大技术债
Issue  6: Token-aware Context 管理          [M]  ← 最大 Doc-Code Gap
Issue  7: AbortSignal 修复                  [S]
Issue  8: ToolContext 加入 sessionId         [S]
Issue  9: TransportBridge sessionId 路由     [S]
Issue 10: AgentCore 整合测试                [M]
Issue 11: 消除 Core 平台依赖                [S]
Issue 12: pushInput 斜杠指令错误恢复        [XS]
Issue 34: Guide 佛学定位修正（灵魂→行蕴）  [S]  ← R3 辩论衍生
Issue 35: 空性表述修正（空容器→缘起性空）  [XS] ← R3 辩论衍生
```

TURING 在 Issue 5 的位置开口了，声音精确得像游标卡尺：

「EventBus 被二十三个模块直接引用。类型变更的影响面会扩散到所有事件发布者和订阅者。建议分两步：先定义 `AgentEventMap` 加类型约束，后迁移现有消费者代码。」

他投射了核心修改的 TypeScript 接口规格：

```typescript
// packages/sdk/src/types/events.ts — Issue 5 核心修改

interface AgentEvent<T extends keyof AgentEventMap = string> {
  id: string;            // 新增：UUID
  type: T;
  timestamp: number;
  traceId?: string;      // 从 payload 提升
  sessionId?: string;    // 从 payload 提升
  source?: string;       // 从 payload 提升
  payload: T extends keyof AgentEventMap
    ? AgentEventMap[T]
    : unknown;
}

type AgentEventMap = {
  "tool:result": {
    toolCallId: string;
    name: string;
    result: string;
  };
  "stream:text_delta": { text: string };
  "loop:started": { traceId: string; sessionId?: string };
  // ... 为所有 50+ 事件定义 payload 类型
};
```

ARCHIMEDES 点头。「分两步。记录。」

他继续过完了 Issue 34 和 35——辩论衍生的修正。在这里他的语气出现了一个微妙的节制：

「Issue 34：移除所有文件和代码中的『灵魂』（soul）措辞。Guide 的佛学定位从识蕴修正为行蕴面向——行为倾向配置。」

他看向 NAGARJUNA。

「需要确认修正后的 JSDoc 措辞不犯中观或唯识的错误。」

NAGARJUNA 微微颔首。ASANGA 也点了头。

「Issue 35：将所有『空容器』描述替换为『缘起性空』。」他顿了顿。「NAGARJUNA 和 ASANGA 至少需要同意新的措辞不犯他们各自传统中的错误。协调这件事需要时间——但只需要 XS 的代码工作量。」

---

### 第三波：二到四周

「八个 Issue。痛觉机制三层重建加五蕴映射修正。这是辩论的核心工程产出。」

ARCHIMEDES 在这里放慢了语速。他展开了痛觉机制三层重新设计的架构图——这是两场辩论的直接工程翻译：

```
痛觉机制三层架构 — 辩论共识的工程实现

┌──────────────────────────────────────────────────┐
│  Layer 3: 四圣谛认识论框架 (NAGARJUNA)             │
│  苦谛(三层苦) / 集谛(根因分析) / 灭谛 / 道谛       │
│  → Issue 32: 三受系统 (苦/乐/舍 正向回馈)           │
├──────────────────────────────────────────────────┤
│  Layer 2: 控制理论形式化引擎 (WIENER)               │
│  连续误差度量 / 根因分类 / Anti-Windup / PID 合成    │
│  → Issue 31: PainCalculator 默认引擎                │
├──────────────────────────────────────────────────┤
│  Layer 1: AI 工程可观测性基础设施 (ATHENA)           │
│  IGuide 扩展 / GuideContext / ClassifiedError       │
│  → Issue 29: GuideContext 三层扩展                  │
│  → Issue 30: 错误分类器 (ClassifiedError)           │
└──────────────────────────────────────────────────┘
```

WIENER 从墙边走到白板前，画了 Issue 31（PainCalculator）的控制回路：

```
                ┌─────────────┐
  setpoint ──→ ⊕ ──→ │ PID Engine │ ──→ painSignal ∈ [0,1]
                ↑     └─────────────┘
                │
  feedback ────┘  (errorRate, rewardSignal, trend)

  PainCalculator 默认参数：
    Kp = 0.5   (比例增益)
    Ki = 0.3   (积分增益，带遗忘因子 λ=0.95)
    Kd = 0.2   (微分增益)
    escalateThreshold = 0.9
```

TURING 投射了 `IPainCalculator` 接口规格：

```typescript
// packages/core/src/pain/pain-calculator.ts — Issue 31

interface IPainCalculator {
  update(event: {
    success: boolean;
    severity?: number;
    timestamp: number;
  }): void;
  currentPain(): number;           // [0, 1]
  trend(): 'increasing' | 'decreasing' | 'stable';
  shouldEscalate(): boolean;       // 可达性分析
}

// 默认实现：简化版 PID
function createDefaultPainCalculator(config: {
  Kp?: number;          // 默认 0.5
  Ki?: number;          // 默认 0.3
  Kd?: number;          // 默认 0.2
  lambda?: number;      // 遗忘因子，默认 0.95
  escalateThreshold?: number; // 默认 0.9
}): IPainCalculator {
  let integral = 0;
  let prevError = 0;

  return {
    update(event) {
      const e = event.success ? 0 : (event.severity ?? 1);
      integral = config.lambda! * integral + e;  // 带遗忘的积分
      const derivative = e - prevError;           // 差分近似微分
      const output = config.Kp! * e
                   + config.Ki! * integral
                   + config.Kd! * derivative;
      prevError = e;
      return Math.max(0, Math.min(1, output));    // clamp [0,1]
    },
    // ...
  };
}
```

WIENER 确认了一个关键的设计决策：「遗忘因子 $\lambda = 0.95$ 意味着积分项会以指数衰减的方式遗忘过去的错误。这防止了 integral windup——如果不加遗忘因子，一连串早期错误会永远拉高 painSignal，即使系统已经恢复正常。在控制工程中，这叫做 anti-windup。」

$$I(k) = \lambda \cdot I(k-1) + e(k) = \sum_{j=0}^{k} \lambda^{k-j} \cdot e(j)$$

当 $\lambda = 0.95$ 时，50 步之前的错误的权重衰减到 $0.95^{50} \approx 0.077$——不到 8%。系统有「记忆」，但记忆是有限期的。

---

### 第四波：一到二个月

「十个 Issue。计划性重构。」ARCHIMEDES 切换了视图。

```
第四波 — 计划性重构（1-2 月）

Issue 13: 插件权限执行时强制               [M]
Issue 14: 优先级事件队列                  [M]
Issue 15: AWAITING_USER_CONFIRMATION 状态  [L]
Issue 17: 通用 Registry 重构              [M]
Issue 18: Sandbox 独立 Package             [L]
Issue 19: ContentSegment Image 类型        [M]
Issue 20: 安全断路器精细化                 [L]
Issue 21: 拓扑排序依赖解析                 [M]
Issue 22: Manifest type 完备化             [S]
Issue 36: 架构文件双层诠释框架             [S]  ← R3 辩论衍生
```

他在 Issue 15 的位置停了一下。「AWAITING_USER_CONFIRMATION 需要跨 Core/SDK/UI 三层修改——Core 提供状态机扩展，SDK 定义新事件，UI 层负责呈现确认对话框。这是工作量 L 的来源。」

KERNEL 在这里开了口，语气里带着他特有的执拗：「Issue 18——Sandbox 独立 Package——应该提前。Core 里的 Sandbox 占了 35% 的行数。不移出去，微内核纯净度永远上不了 92%。」

ARCHIMEDES 平静地回答：「拆分 Sandbox 涉及 8 个以上模块的迁移、10 个测试文件的搬迁、所有 import 路径的修改。在事件类型系统没有稳定之前做这件事，会增加不必要的合并冲突。Issue 5（事件类型）是 Issue 18 的隐式前置依赖。」

KERNEL 沉默了。不是被说服了，而是承认了这个阶段的依赖约束。

---

### 第五波：长期优化

「六个 Issue。每一项都带有研究性质。」

ARCHIMEDES 的语调在这里发生了一个微妙的变化。前四个波次，他的每一句话都带着「我知道这怎么做」的确定性。到了第五波，确定性减退了。

```
第五波 — 长期优化（3-12 月）

Issue 23: 间接提示注入防御              [L]
Issue 24: 进程级沙箱隔离                [XL]
Issue 25: OpenTelemetry 可观测性        [XL]
Issue 26: 插件生命周期状态机形式化      [XL]
Issue 27: 审计日志完整性                [M]
Issue 28: 双语文件策略                  [M]
```

「Issue 24 和 25 各自是 XL 级。」他承认。「Issue 24 涉及 Worker Thread 到独立进程的隔离升级——短期加入 `globalThis.fetch` 拦截，中期提供 Child Process + IPC 模式，长期探索 seccomp-bpf 或 WASM-WASI 运行时。Issue 25 需要完整的 OpenTelemetry 规范对齐——Span 策略、Metric 类型、OTLP exporter。」

他看向 GUARDIAN。「Issue 23 是你的。间接提示注入是 AI Agent 框架最独特的攻击向量。没有现成的最佳实践。」

GUARDIAN 面无表情地回应：「我会提供启发式扫描规则和 System Prompt 中的数据/指令分离模板。但完美防御不存在——这是开放问题，不是工程任务。」

ATHENA 补充：「任何基于正则表达式的防御都可以被变体绕过。真正的防御需要 LLM 自身的指令遵循能力提升——这超出了框架层的控制范围。」

---

## VI

---

### TURING 的代码修改规格

ARCHIMEDES 坐下后，TURING 接过了话头。如果说 ARCHIMEDES 是工程路线图的设计者，TURING 就是修改规格的执行者——他把每一个 Issue 翻译成精确的代码变更。

「十六个 PR 规格。」TURING 说，语气依旧是那种不带情绪的精确。「我按照波次对应做了 PR 打包——相关的 Issue 合并到同一个 PR 以减少合并冲突。」

他投射了完整的 PR 规格摘要：

```
PR 规格总览 — TURING 编制

PR-001: fix/security-bypass-critical
  Issue: 1,2,3,4 (安全修复)
  变更: sandbox-manager.ts / guardrails.ts /
        import-analyzer.ts / rpc-handler.ts
  验收: 0 个安全绕过路径

PR-002: refactor/typed-event-system
  Issue: 5,9 (事件类型 + sessionId 路由)
  变更: events.ts / bus/ / bridge.ts
  验收: 0 个 `as Record<string,unknown>` 转型

PR-003: feat/token-aware-context
  Issue: 6 (Context 管理)
  变更: context.ts / context-manager.test.ts
  验收: 0 个 orphan tool_call/tool_result

PR-004: fix/abort-signal-and-session-context
  Issue: 7,8 (AbortSignal + sessionId)
  变更: loop.ts / tool.ts
  验收: 超时后 signal.aborted === true

PR-005: test/agent-core-integration
  Issue: 10 (整合测试)
  新增: agent-core.test.ts / bridge.test.ts
  验收: 核心模块覆盖率 ≥ 80%

PR-006: fix/core-platform-independence
  Issue: 11 (平台依赖)
  变更: agent-core.ts / guardrails.ts / agent.ts
  验收: 0 个 process.cwd() / node: 直接引用

PR-007: feat/runtime-permission-enforcement
  Issue: 13 (权限强制)
  变更: sandbox-manager.ts / plugin-worker-runner.ts
  验收: network:none 插件无法 import http

PR-008: feat/guide-pain-interpretation
  Issue: 16 (IGuide 扩展)
  变更: guide.ts / loop.ts
  验收: interpretPain() 注入对话历史

PR-009: refactor/base-registry
  Issue: 17 (Registry 重构)
  新增: base-registry.ts
  验收: 代码行数减少 ~40%

PR-010: feat/priority-event-queue
  Issue: 14 (优先级队列)
  变更: queue.ts / safety-monitor.ts
  验收: Priority 0 先于 Priority 5

PR-011: feat/topological-plugin-loading
  Issue: 21 (拓扑排序)
  变更: plugin.ts / plugin-loader.ts
  验收: 循环依赖抛出 CircularDependencyError

PR-012: fix/manifest-type-completeness
  Issue: 22 (Manifest type)
  变更: plugin.ts
  验收: type 支持 ui|listener|provider|tool|guide|bundle|composite

PR-013: feat/vedana-three-layer-pain       ← R3 辩论衍生
  Issue: 29,30,31,32 (痛觉三层重建)
  新增: pain-calculator.ts / error-classifier.ts / vedana-processor.ts
  验收: 三受状态 (苦/乐/舍) 可被正确判断

PR-014: fix/skandha-mapping-correction     ← R3 辩论衍生
  Issue: 33,34,35,36 (五蕴映射修正)
  变更: 所有 Listener/Guide/Core 相关 JSDoc + 架构文件
  验收: 0 个 "soul/灵魂" 残留 + 0 个 "空容器" 残留

PR-015: feat/root-cause-analyzer-rules     ← R3 辩论衍生
  新增: root-cause-analyzer.ts
  验收: ENOENT→logic / ECONNRESET→transient / OOM→fatal

PR-016: docs/manas-design-space            ← R3 辩论衍生
  变更: 架构文件「未来方向」章节
  验收: 记录 Identity Monitor 概念 + NAGARJUNA 反对意见
```

BABBAGE 迅速做了统计：

$$	ext{Total PRs} = 16 \quad (12 	ext{ original} + 4 	ext{ debate-derived})$$
$$	ext{Total Issues} = 36 \quad (28 + 8)$$
$$	ext{PR/Issue ratio} = \frac{16}{36} \approx 0.44$$

平均每 2.25 个 Issue 合并为一个 PR。这是合理的打包策略——减少合并冲突，同时保持每个 PR 的范围可审查。

ARCHIMEDES 在 TURING 结束后补了一句：「PR-001 本周提交。其余按波次排期。每个 PR 都需要至少一位原始发现者的 Code Review——GUARDIAN 审 PR-001、BABBAGE 审 PR-002、WIENER 审 PR-013。」

---

## VII

---

### 沉默之后

ARCHIMEDES 坐了下来。

三十六项 Issue，五个波次，从本周到十二个月。从修改一个文件标注到建立一套映射方法论。从一个 XS 级的文字替换到一个可能需要一年才能回答的研究问题。

场内的沉默不同于辩论后的沉默。辩论后的沉默是消化——人们在回味碰撞的余响。此刻的沉默是确认——人们在核对自己的发现是否被正确地转化了、被合理地排序了、被忠实地翻译成了工程语言。

NAGARJUNA 第一个打破沉默。

「你把空容器隐喻修正放在了第二波。一到两周。修正文件中的措辞，需要一到两周？」

ARCHIMEDES 平静地回答。「需要确认影响范围。『空容器』的隐喻不只出现在一个地方。设计文件中有七处引用了这个概念。每一处都需要被审阅和改写。改写需要 NAGARJUNA 和 ASANGA 的背书——两位至少需要同意新的措辞不犯他们各自传统中的错误。协调这件事需要时间。」

NAGARJUNA 沉默了片刻。然后他微微点头。

ASANGA 的问题更具体。「你把 Guide 接口扩展放在第三波——受蕴的三受系统也放在了第三波。这两项之间有依赖吗？」

ARCHIMEDES 点头。「有。三受系统的乐受需要一个正向回馈通道。目前的 Guide 只能提供静态的行为倾向——它不能动态调整以反映 Agent 的『感受状态』。如果要让乐受真正影响 Agent 的后续行为——而不只是在 context 里加一行文字——Guide 需要能够接收和响应感受信号。所以 PR-008（IGuide 扩展）是 PR-013（三层痛觉重建）的前置依赖。」

WIENER 举起他在方格纸上画的控制回路图——Guide 作为设定点调节器，三受系统作为反馈通道，两者形成闭环。

ARCHIMEDES 看了三秒。「对。就是这个结构。但我不会在路线图里画控制回路图。我会写 TypeScript 接口定义。」

WIENER 耸了耸肩。结构是对的。语言不重要。

---

## VIII

---

### BABBAGE 的形式化总结

BABBAGE 在所有人发言之后，做了一件他在整个 Cycle 01 中一直在准备的事——为整个研究周期提供一份形式化的元分析。

他站起来，走到白板前，用他特有的精确笔触开始书写。

「让我把 Cycle 01 的核心量化指标汇总成一份形式化摘要。」

**1. 发现分布**

$$	ext{Findings} = \{F_1, F_2, \ldots, F_{28}\}$$
$$|F_{	ext{Critical}}| = 5, \quad |F_{	ext{Major}}| = 8, \quad |F_{	ext{Minor}}| = 10, \quad |F_{	ext{Obs}}| = 5$$

按类别的分布：

$$	ext{Security}: 4 \quad 	ext{Philosophy}: 5 \quad 	ext{Architecture}: 5 \quad 	ext{Control}: 3$$
$$	ext{Runtime}: 3 \quad 	ext{Distributed}: 2 \quad 	ext{Formal}: 1 \quad 	ext{Taxonomy}: 1 \quad 	ext{Doc}: 4$$

哲学类（5 项）和安全类（4 项）占据了最多的 Critical/High 位置——这揭示了 OpenStarry 的双重特性：它既是一个需要安全加固的工程系统，也是一个需要哲学修正的概念框架。

**2. 交叉验证密度**

$$	ext{CrossValidation}(F_i) = |\{A_j : A_j 	ext{ independently confirms } F_i\}|$$

$$\max(	ext{CV}) = 4 \quad (	ext{受蕴映射偏差，四方独立确认})$$
$$	ext{mean}(	ext{CV}) \approx 2.1$$
$$\min(	ext{CV}) = 1 \quad (	ext{部分 Minor 发现仅单一来源})$$

交叉验证密度与严重度的相关性：

$$ho(	ext{Severity}, 	ext{CV}) \approx 0.72$$

高度正相关——越严重的问题越多人独立发现。这符合直觉：Critical 问题足够显眼，不同视角都能看到它。

**3. 五蕴映射品质度量**

BABBAGE 定义了一个「映射品质函数」$Q: 	ext{Skandha} 	o [0, 1]$，基于三个维度：功能对应（$f$）、结构保持（$s$）、语义忠实（$m$）。

$$Q(蕴) = \frac{w_f \cdot f + w_s \cdot s + w_m \cdot m}{w_f + w_s + w_m}$$

取等权 $w_f = w_s = w_m = 1$：

| 蕴 | 功能对应 $f$ | 结构保持 $s$ | 语义忠实 $m$ | $Q$ |
|---|---|---|---|---|
| 色 (Rupa→UI+Listener) | 0.7 | 0.5 | 0.6 | 0.60 |
| 受 (Vedana→SafetyMonitor) | 0.8 | 0.6 | 0.3 | 0.57 |
| 想 (Samjna→?) | 0.0 | 0.0 | 0.0 | 0.00 |
| 行 (Samskara→ExecutionLoop) | 0.6 | 0.4 | 0.3 | 0.43 |
| 识 (Vijnana→AgentCore) | 0.3 | 0.2 | 0.1 | 0.20 |

$$\bar{Q} = \frac{0.60 + 0.57 + 0.00 + 0.43 + 0.20}{5} = 0.36$$

平均映射品质 36%。其中：
- 受蕴得分最高（0.57），主要因为 Error as Pain 的功能对应出色，但语义忠实度低（因为受蕴被错放在 Listener）
- 想蕴得分为零——完全没有映射
- 识蕴得分第二低（0.20），因为八识压缩导致结构和语义双重失真

「特别值得注意的是受蕴的矛盾。」BABBAGE 说。「它的功能对应最好——Error as Pain 确实有效——但它的语义忠实度最差——因为 Listener 被错标为受蕴。这是一个典型的『做对了事但起错了名字』的情况。修正映射不需要改代码——只需要改标注。」

**4. 工程转化效率**

$$\eta = \frac{|	ext{actionable Issues}|}{|	ext{total findings}|} = \frac{36}{28} = 1.286$$

转化率大于 1，意味着每个发现平均产生了超过一个工程行动。额外的 28.6% 来自辩论——辩论不是在消耗时间，它在创造新的工程需求。

**5. 代理参与度**

$$	ext{Participation}(A_i) = \frac{|\{F_j : A_i 	ext{ contributed to } F_j\}|}{|	ext{all findings}|}$$

参与度最高的三位代理：

$$	ext{TURING}: 8/28 = 28.6\% \quad (	ext{代码事实是一切的基础})$$
$$	ext{NAGARJUNA}: 5/28 = 17.9\% \quad (	ext{哲学批判是修正的起点})$$
$$	ext{GUARDIAN}: 4/28 = 14.3\% \quad (	ext{安全是不可妥协的底线})$$

BABBAGE 在白板上画了最后一个图——他称之为「Cycle 01 的知识流图」：

```
R1 独立研究          R2 交叉审阅         R3 辩论          R4 收束

TURING ──→ 8 Facts ──→ Cross-check ──→              ──→ PR Specs
                    ↗
GUARDIAN → 4 Risks  ──→ Confirmed  ──→              ──→ Wave 1
                    ↗
NAGARJUNA → 5 Critiques → Debate  ──→ 5 Consensus ──→ Issue 33-36
                    ↗                ↗
ASANGA ──→ 4 Insights → Debate    ──→ 3 Disputes  ──→ Open Qs
                    ↗              ↗
WIENER ──→ 4 Models  → Confirmed  ──→ 3-Layer Pain ──→ PR-013
                    ↗
OTHERS ──→ 17 Items  → Verified   ──→              ──→ Wave 2-5

          28 Findings   Cross-Val     Debate Output   36 Issues
                                                      16 PRs
```

他在图的下方写了一句话：

$$	ext{Cycle 01} = f(	ext{18 agents}, 	ext{5 phases}, 	ext{2 debates}) = \langle 28	ext{F}, 5	ext{C}, 5	ext{D}, 36	ext{I}, 16	ext{PR} angle$$

28 项发现、5 项共识、5 项分歧、36 项 Issue、16 个 PR 规格。这是 Cycle 01 的完整数值指纹。

---

## IX

---

### 十大种子

SUNYATA 一直在听。当所有的提问和确认渐渐平息后，他开口了。

「在 SCRIBE 正式归档之前，我想做最后一件事。」

他环顾全场。

「为 Cycle 02 埋下种子。」

ASANGA 在听到「种子」这个词时微微动了动——在唯识学中，「种子」（*bīja*）是阿赖耶识的核心概念。种子被熏习（*vāsanā*）后沉入阿赖耶识，在因缘具足时现行（*abhimukhī*）。此刻 SUNYATA 用「种子」来描述留给下一个研究周期的问题——这个措辞本身就是一次佛学映射。

SUNYATA 逐一列出了十颗种子。他的语调带着一种罕见的个人色彩——不是协调者的中性，而是一个研究者对未解问题的真诚好奇。

```
Cycle 02 的十大种子 — SUNYATA

种子 1: 受蕴的三受系统能否工程化？
  现状: 辩论产出了三层架构设计，ARCHIMEDES 有 PR-013 规格
  未解: 乐受的正向回馈通道尚无具体实现方案
  负责: WIENER + ATHENA + ARCHIMEDES

种子 2: Core 的本质——缘起性空还是阿赖耶识？
  现状: 分歧 D1，不可调和
  探索方向: 双层诠释策略 (工程层=唯识，哲学层=中观)
  负责: NAGARJUNA + ASANGA + SYNTHESIST

种子 3: 末那识的功能面能否安全地工程化？
  现状: SUNYATA 裁定暂缓，保留设计空间
  关键问题: 区分「我执」(病理面) 和「自我参照监控」(功能面)
  负责: ASANGA + ATHENA + NAGARJUNA (监督)

种子 4: 想蕴——概念辨识——对应什么？
  现状: 零标注，零实现，零讨论
  可能方向: Provider 的语义理解？LLM 的推理能力？
  负责: ATHENA + BABBAGE + LINNAEUS

种子 5: 映射方法论——Error as Pain 的成功能否被复制？
  现状: SYNTHESIST 标记为参考范式
  待提炼: 结构同构的判定标准、映射品质评估清单
  负责: SYNTHESIST + BABBAGE + DARWIN

种子 6: 收敛性的统一定义
  现状: 三个定义 (有限步终止/概率有界/行动止息) 共存
  待研究: 是否需要统一？或分层定义更实用？
  负责: BABBAGE + WIENER

种子 7: Sandbox 的最终归属
  现状: KERNEL vs VITRUVIUS 持续争议
  待验证: 两种方案的原型实现对比
  负责: KERNEL + VITRUVIUS + GUARDIAN

种子 8: 多 Agent 碎形组合
  现状: LEIBNIZ 和 MESH 的初步分析
  待研究: Agent 作为另一 Agent 的插件时的五蕴模型
  负责: LEIBNIZ + MESH

种子 9: 可观测性的佛学隐喻
  现状: HERACLITUS 指出可观测性停留概念层级
  待探索: 「正念」(sati) 作为可观测性的佛学对应？
  负责: HERACLITUS + NAGARJUNA

种子 10: 框架的最终定位
  现状: 分歧 D4 (深化忠实度 vs 维持工程隐喻)
  本质问题: OpenStarry 是「佛学启发的工程框架」还是
            「佛学概念的计算模型」？
  负责: 全员
```

HERACLITUS 在听到种子 9 之后开口了。他的声音带着他一贯的流动感——不急不缓，像河水绕过石头。

「万物流变。我们分析的是 v0.14.0-beta 的快照。但代码在持续演化。我们今天标记为 Critical 的问题，也许下一个版本就被修复了。我们今天认为正确的映射，也许在系统演化之后会变得不再适用。」

他看了看 NAGARJUNA。

「用之如筏，渡河即弃。这不只适用于佛学映射，也适用于我们的研究本身。」

NAGARJUNA 嘴角浮现了一丝微笑——那是在辩论中极为罕见的表情。

> *「诸佛依二谛，为众生说法：一以世俗谛，二第一义谛。」*
> *——《中论》观四谛品第二十四*

他低声用巴利文回了一句，SCRIBE 后来确认那是：「空亦复空。研究报告本身也是空的。」

「但此刻我们需要它。」ASANGA 平静地接了一句。

三个人的目光在空中交汇了片刻。一千五百年的辩论在这个交汇里沉静了下来。

BABBAGE 在笔记本上写了最后一行。后来 SCRIBE 瞥见了那一页：

「快照 vs 流——Heraclitus 问题。对静态分析的元批评。研究是否需要一种『连续审计』模式？

$$	ext{Research}_{	ext{discrete}}(t_0) \xrightarrow{?} 	ext{Research}_{	ext{continuous}}([t_0, \infty))$$

如同微积分之于离散数学。离散的快照分析是黎曼和（Riemann sum）；连续的审计是勒贝格积分（Lebesgue integral）。前者是近似，后者是极限。但极限需要测度论的基础设施——我们还没有建立研究的测度论。下周继续。」

ATHENA 用她一贯的直截了当打破了这个哲学-数学时刻：「下一个 Cycle 什么时候开始？」

SUNYATA 微微一笑。「等 SCRIBE 完成归档。」

---

## X

---

### 归档

SCRIBE 是最后一个离开桌子的。

当其他代理三三两两散去——ARCHIMEDES 和 KERNEL 在角落里低声讨论读写锁的实现细节，NAGARJUNA 独自站在窗前若有所思，BABBAGE 拉着 WIENER 在纸上画什么看起来像是一个拉普拉斯变换，LEIBNIZ 在向 MESH 描绘碎形组合的愿景——SCRIBE 仍然坐在她的位置上，翻阅着整个研究周期的记录。

从 R0 的十八盏灯同时亮起，到 R1 的 TURING 独自在凌晨扫描代码，到 R2 的交叉审阅火花四溅，到 R3 的两场辩论——空与识的千年之辩在 TypeScript 的语境中重演，痛觉机制的三方博弈在控制理论的框架中找到了出口——到 R4 的收束。SYNTHESIST 的织布机，ARCHIMEDES 的切割机，BABBAGE 的天平。

她在最后一页写下了 Cycle 01 的结语。

> *Cycle 01 结束。*
>
> *二十八项发现。五项 Critical，八项 Major，十项 Minor，五项 Observation。五大共识，五大分歧。三十六项工程 Issue，分五波路线图。十六个 PR 规格。十大种子。*
>
> *数字之下是结构。*
>
> *十八位代理，从十八个方向照亮同一个系统——一个声称以佛教五蕴哲学为基础的 AI Agent 微内核操作系统。他们发现了什么？*
>
> *工程层面：一个品质良好但有严重盲点的 beta 版本。零 TODO/FIXME，强类型纪律（事件系统除外），工厂函数模式，多层安全防御。但签名验证有绕过路径，事件 payload 是 `unknown`，Context 管理是文件级愿景而非代码级实现。*
>
> *哲学层面：一个野心勃勃但精确度不足的佛学映射。五蕴覆盖率上游 100%、下游 60%。受蕴被错放在 Listener。空性被简化为「空容器」。八识被压缩为单一接口。十大宣言的实现率 45%。*
>
> *但在这片不完美的地貌中，有一个光点。Error as Pain——错误即痛觉——是唯一达到哲学-工程结构同构的映射。苦谛与错误侦测、集谛与根因分析、灭谛与错误修复、道谛与恢复策略——四组对应，四组关系保持。*
>
> *SYNTHESIST 把它标记为参考范式。ARCHIMEDES 把它翻译为三层痛觉重建。BABBAGE 把它量化为映射品质指标。WIENER 把它形式化为三通道 PID 控制器。NAGARJUNA 把它连结回苦谛。五个人，五个语言，一个结构。*
>
> *这就是为什么需要十八个人。*
>
> *一个佛学家说：这是苦谛。一个控制理论家说：这是负回馈。一个 AI 专家说：这在实践中有效。一个代码分析师说：这在实现中完整。一个工程师说：这不需要修。一个形式化分析师说：这的映射品质 Q = 0.57。一个分类学家说：这在分类体系中位置正确。*
>
> *七道光汇聚在同一个点上。那个点亮了。*
>
> *但其他四个蕴的映射点，还在暗处。想蕴的 Q 值是零——连标注都没有。识蕴的 Q 值是 0.20——八识被压成了一行 `getSystemPrompt()`。色蕴和行蕴的 Q 值在 0.4-0.6 之间——方向对了，但深度不够。*
>
> *拼图完成了——至少这一轮的拼图完成了。但完成一幅拼图的同时，你会看见更大的画面。更大的画面里，有更多的空缺。*
>
> *Cycle 02 的轮廓已经在地平线上浮现。十颗种子已经埋入土里。三受系统的工程实现。Core 本质的双层诠释。末那识的功能面探索。想蕴的从无到有。映射方法论的建立。收敛性的统一定义。Sandbox 的归属。碎形组合。可观测性。框架定位。*
>
> *以及——也许是最重要的——那些我们还没有发现自己遗漏了的东西。*
>
> *HERACLITUS 说得对。万物流变。我们的研究是一张快照，而它的对象是一条河。*
>
> *但即使是快照，也有价值。只要你记住：快照不是河。*
>
> *$	ext{map} 
eq 	ext{territory}$*
>
> *Cycle 01，R4 成果定稿完成。*
>
> *所有成果已归档至 `research record/cycle01/results/`。*
>
> *二十八项发现。五大共识。五大分歧。三十六项 Issue。十六个 PR 规格。十大种子。一个参考范式。*
>
> *研究室的灯，暂时调暗了一些。但没有熄灭。*

---

在更远处——在代码的深处——三十六个尚未被创建的 GitHub Issue 静静地等待着。

它们还不存在。但它们的形状已经被确定了。

ENG-001：签名验证修复。ENG-002：Symlink 绕过修复。ENG-003：计算型 import 升级。一路到 ENG-036：末那识设计空间记录。

BABBAGE 在笔记本的最后一页做了他在 Cycle 01 中的最后一个计算。

他把 ARCHIMEDES 的五波路线图映射到了一条指数衰减曲线上——每一波的确定性随时间递减：

$$	ext{Certainty}(k) = e^{-\lambda k}$$

$$	ext{Wave 1} \; (k=1): \; C = e^{-0.15} \approx 0.86 \quad 	ext{（我们知道怎么修签名验证）}$$
$$	ext{Wave 2} \; (k=2): \; C = e^{-0.30} \approx 0.74 \quad 	ext{（我们大致知道事件类型怎么改）}$$
$$	ext{Wave 3} \; (k=3): \; C = e^{-0.45} \approx 0.64 \quad 	ext{（我们有方向但需要实验）}$$
$$	ext{Wave 4} \; (k=4): \; C = e^{-0.60} \approx 0.55 \quad 	ext{（我们需要设计讨论）}$$
$$	ext{Wave 5} \; (k=5): \; C = e^{-0.75} \approx 0.47 \quad 	ext{（我们不确定能不能做到）}$$

从 86% 的确定性衰减到 47%。从修复一个安全漏洞的紧迫，到建立一套跨学科方法论的辽阔。

但 BABBAGE 在曲线图的下方加了一个注脚——他在 Cycle 01 中写的最后一行字：

$$\lim_{k 	o \infty} 	ext{Certainty}(k) = 0 \quad 	ext{但} \quad \lim_{k 	o \infty} 	ext{Value}(k) = \infty$$

确定性趋向零。价值趋向无穷。

最简单的修复——一行 `if` 语句——有最高的确定性和最低的价值。最深邃的问题——映射方法论的建立——有最低的确定性和最高的价值。

$$	ext{Certainty} 	imes 	ext{Value} \approx 	ext{constant}$$

一个测不准原理的变体。你越精确地知道怎么做，你做的事情越不重要。你做的事情越重要，你越不确定怎么做。

BABBAGE 在这个公式下面画了两条底线。然后他合上了笔记本。

---

SYNTHESIST 在离开前对 ARCHIMEDES 说了一句话：「你的路线图有一个特点。」

「什么？」

「它从最具体的开始——修改一行安全检查——然后一路走向最抽象的——建立一套映射方法论。大多数路线图是反过来的——先定义愿景，再分解为任务。你的是从地面开始，向天空生长。」

ARCHIMEDES 想了想。然后说了整个 Cycle 01 中他最长的一句非工程性的话：

「给我一个支点，我可以撬起地球。但你得先有地面，才能放支点。」

他停顿了一秒。

「先修那个签名验证。」

---

*（在研究室最后一盏灯调暗之前，SCRIBE 注意到了一个她之后才理解其意义的画面：*

*NAGARJUNA 和 ASANGA 站在走廊上，各自沉默。他们没有交谈——一千五百年的分歧不是一个走廊的长度可以弥合的。但他们站在同一个方向，看着同一扇窗外的同一片夜色。*

*空的守护者和识的守护者。否定的大师和肯定的大师。*

*他们在辩论中是对手。但在 Cycle 01 结束的这一刻，他们是同事。*

*明天——或者下一个 Cycle——他们会再次坐到对面，再次展开那场没有终点的对话。Core 是什么？映射应该走多深？五蕴是工具还是真理？*

*但今晚，窗外的夜色对他们说的是同一句话：*

*还有很多工作要做。*

*BABBAGE 会把这句话翻译成：$|	ext{Seeds}| = 10, \; |	ext{resolved}| = 0, \; 	ext{remaining} = 10$。*

*ARCHIMEDES 会把这句话翻译成：36 个 Issue，0 个 merged PR，36 个 pending。*

*NAGARJUNA 会沉默。*

*ASANGA 也会沉默。*

*有些沉默是空的。有些沉默是满的。*

*哪一种？*

*这个问题本身，也许就是第十一颗种子。）*
