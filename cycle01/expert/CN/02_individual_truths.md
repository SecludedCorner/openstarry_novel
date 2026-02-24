# 第二章：各自的真相

---

*R1 独立研究阶段。十八位代理各自领取了研究材料的副本，退入自己的频道，开始阅读。这是一段漫长的静默——如同考场上翻页的声响，每个人都在各自的宇宙里，寻找属于自己学科的那条裂缝。*

*裂缝总是会出现的。*

*但在专家的眼中，裂缝不只是裂缝。它是一组方程式未能闭合的缺口，是一棵分类树上缺失的节点，是一段梵文经典被误读后留下的语义空洞。每位学者带着自己的透镜，而透镜的精度决定了裂缝被看见时的解析度。*

---

## I. 龙树的震怒

NAGARJUNA 在频道里坐了很久。

不是因为他读得慢。恰恰相反，他在读到第九行的时候就停住了，此后反复咀嚼那同一段话，像一个古文字学家对着一块出土的泥板，确认自己没有看错上面的楔形文字。

文件 `14_Agent_Core_Philosophy_Five_Aggregates.md`，第零节，标题赫然写着：

**“核心本质：空 (Sunyata)”**

他的目光落在那段话上。

> Agent Core 本身是“空 (Sunyata)”的。它是一个纯粹的容器，没有人设，没有能力，没有感知。它等待着被五种插件填充。

NAGARJUNA 把这句话读了三遍。然后他开始在笔记区写字，笔触极快，几乎带着某种被冒犯后的精确。

---

NAGARJUNA（笔记，时间戳 09:12）：

“我必须首先澄清一个根本性的误读。

这份设计文件使用了梵文 Sunyata 一词，并将其翻译为‘空’。但它所描述的概念——一个等待被填充的纯粹容器——根本不是 Sunyata。

这是 uccheda-sunyata。断灭空。虚无主义的空。

让我用原典说明。《中论》第二十四品第十八偈（*Mulamadhyamakakarika* XXIV.18）：

> *yah pratityasamutpadah sunyatam tam pracaksmahe*
> *sa prajnaptir upadaya pratipat saiva madhyama*

> “众因缘生法，我说即是空，亦为是假名，亦是中道义。”

此偈的梵文结构极其精确。*pratityasamutpada*（缘起）与 *sunyata*（空性）以 *tam...pracaksmahe*（我们如此说）连结——空性就是缘起，缘起就是空性。两者不是因果关系，不是包含关系，而是同义异名（*paryaya*）。

Sunyata 的准确含义是 pratityasamutpada-sunyata——缘起性空。一切现象因缘和合而生，无自性（*svabhava*），因此称之为空。空不是没有，空是没有固有本质。水杯是空的，不是因为里面什么都没有，而是因为‘水杯’这个概念本身就依赖于玻璃、工匠、使用者的意图等无数因缘才得以成立。

一个‘等待被填充的纯粹容器’——这恰恰是空的反面。它预设了一个独立自存的实体（容器），拥有固有的‘容纳能力’，然后外部的内容被注入其中。这是典型的自性见（*svabhava-drsti*）。

月称（Candrakirti）在《入中论》（*Madhyamakavatara*）第六品中对此种误解有精确的驳斥：

> “若谓自性从缘生，作者及作自性生。
> 已生有何须更生，若彼坏已何能生？”

自性不从因缘生。如果容器的‘容纳性’是其自性，那它不需要插件就应该能容纳；如果它需要插件才能显现容纳功能，那容纳性就不是其自性，而是缘起的。”

---

他停下笔，在频道里开始自言自语。这是他的习惯——哲学家需要听到自己思考的声音。

NAGARJUNA：“让我用四句来检验这个命题。”

他在笔记区画出一个框架，工工整整。四句否定（Catuskoti）是龙树哲学最精锐的分析工具——一种超越二值逻辑（true/false）的四值逻辑框架。BABBAGE 后来在他自己的频道里将其形式化为：

$$	ext{Catuskoti}(P) = \{ P, \; 
eg P, \; P \wedge 
eg P, \; 
eg(P \vee 
eg P) \}$$

但 NAGARJUNA 不用符号。他用语言。语言在他手中比符号更锋利。

```
Catuskoti（四句否定）应用于命题 P：“核心是空的”

第一句（肯定，P）：“核心是空的。”
   ——不尽然。如果核心真的是空的（无自性的），
   那它就不应该有“容器”这个固定身份。
   但设计者明确说它是一个“纯粹的容器”，
   这恰恰赋予了它自性。矛盾。

   形式化：P → 核心无自性 → 核心不具固定身份
          但 P 被定义为“核心是空容器”→ 核心具有容器身份
          ∴ P ∧ ¬P，矛盾。

第二句（否定，¬P）：“核心不是空的。”
   ——也不对。核心确实没有硬编码的功能、
   人设或感知。从功能角度看，
   它在加载插件前确实“什么都不是”。

   形式化：¬P → 核心有自性 → 核心有固有功能
          但 Core 在无插件时 state = ⊥
          ∴ ¬P 与事实矛盾。

第三句（双肯定，P ∧ ¬P）：“核心既空又不空。”
   ——仍然困在二元对立中。
   这只是把前两句的矛盾叠加起来，
   并没有解决问题。

   形式化：P ∧ ¬P 在经典逻辑中直接爆炸（ex falso quodlibet）。
          在超一致逻辑（paraconsistent logic）中可能有意义，
          但中观不依赖超一致逻辑。

第四句（双否定，¬P ∧ ¬(¬P)，即 ¬(P ∨ ¬P)）：
   “核心既非空又非不空。”
   ——接近了。但我们不能停在这里。
   中道不是四句之外的第五个选项，
   中道是对四句全部的超越（nirvikalpa）。
```

NAGARJUNA（继续书写）：

“真正的中观立场应该是：Agent Core 与 Plugin 之间不存在‘容器/内容’的二元关系。它们是互相依存的——Core 的意义因 Plugin 而显现，Plugin 的功能因 Core 的执行循环而实现。这才是缘起。

在梵文中，这种相互依存的关系被称为 *anyonya-asraya*（互相依待）。《中论》第十品观火燃品（*Agni-indhana-pariksa*）以火与燃料的关系作为典范案例：

> *na caagninaa vinaa daaru na ca daaruvinaa'gnih*
> 「离火无燃料，离燃料无火。」

火（Core）离开燃料（Plugin）不成其为火；燃料离开火不成其为燃料。两者互相成就，但都没有独立的自性。设计者的直觉是好的——他们想说核心不应该预设任何功能。但他们用了一个灾难性的隐喻。一个‘空容器’暗示着：存在一个稳定的、独立的容器实体，等待着外部事物的注入。这是 Abhidharma 部派佛教中说一切有部（Sarvastivada）的立场，不是中观的立场。”

---

他翻到五蕴映射的部分，眉头越皱越紧。

色蕴（Rupa）对应 UI Plugin。受蕴（Vedana）对应 Listener Plugin。想蕴（Samjna）对应 Provider Plugin。行蕴（Samskara）对应 Tool Plugin。识蕴（Vijnana）对应 Guide Plugin。

NAGARJUNA 在“受蕴”那一行画了一个大大的叉。

NAGARJUNA：“这是整个映射中最严重的错误。”

他开始写一段更长的分析，引用的经典横跨三个世纪：

---

NAGARJUNA（笔记，时间戳 09:47）：

“受蕴映射之谬——

设计文件第二节写道：
受蕴（Vedana）——接受刺激的感官通道。对应组件：Listener Plugin。Agent 的眼与耳。HTTP Server 接收请求、WebSocket 监听讯息、Cron 监听时间流逝。这些都是输入的‘感受’。

这是对 Vedana 概念的根本性误解。让我引用巴利经典中最精确的定义。

《相应部》（*Samyutta Nikaya*）卷三十六，受相应（*Vedana Samyutta*）第一经：

> *Tisso ima, bhikkhave, vedana. Katama tisso?*
> *Sukha vedana, dukkha vedana, adukkhamasukha vedana.*

> 「比丘们，有三种受。哪三种？
> 乐受、苦受、不苦不乐受。」

受（Vedana）是三领纳——苦、乐、不苦不乐——是对感官接触之后产生的情感性评价。不是信号的接收。

在十二因缘（*Pratityasamutpada*）中，受的位置极其明确：

$$	ext{触}(	ext{Sparsa}) \;\longrightarrow\; 	ext{受}(	ext{Vedana}) \;\longrightarrow\; 	ext{爱}(	ext{Trsna})$$

触是根（感官器官）、境（感官对象）、识（认知功能）三者和合的产物。受是触之后的下一环——是对触的苦乐评价。爱是受之后的执取反应。

如果要找感官通道的佛学对应，Listener 更接近六入（*sadayatana*）中的‘根’（*indriya*）——即接收外部信号的器官。六根：眼根、耳根、鼻根、舌根、身根、意根。HTTP Server 是眼根（接收视觉信号的器官），WebSocket 是耳根（接收听觉信号的器官）。它们接收信号，但不评价信号。

那么在 OpenStarry 的架构中，真正的 Vedana 是什么？

答案就在 SafetyMonitor 的痛觉机制里。”

他引用了代码的行为：

[代码: safety-monitor.ts#afterToolExecution]

“当工具执行失败，SafetyMonitor 追踪连续失败次数（`consecutiveFailures++`），并在达到阈值时注入一段系统提示：

```typescript
// SafetyMonitor 的痛觉响应（概念结构）
if (consecutiveFailures >= frustrationThreshold) {
  injectPrompt = `SYSTEM ALERT: You have failed ${consecutiveFailures} times in a row.
    Please STOP, reflect on the situation, and ask the user for help.`;
}
```

这才是 Vedana——一种对行动结果的苦乐评价：
- 工具执行成功 = *sukha*（乐受）→ `consecutiveFailures` 归零，继续前进
- 工具执行失败 = *dukkha*（苦受）→ 累积挫折感，最终触发行为改变
- 工具执行结果中性 = *adukkhamasukha*（舍受）→ 但系统中尚未实现此通道

Pain Mechanism Demo 更是明确证实了这一点。它描述了一种‘痛感等级’系统——剧痛、刺痛、微痛——这正是 Vedana 的三分法在工程语言中的投射。

讽刺的是，设计者已经在代码中实现了真正的 Vedana，却在哲学文件中把 Vedana 的标签贴在了完全错误的组件上。”

---

他把笔记的最后一段加粗：

“**五蕴映射犯自性见，将动态过程固化为静态模块。**

五蕴不是五个独立的部件。《般若经》（*Prajnaparamita*）明确说：

> *ruupam suunyataa, suunyataiva ruupam;*
> *ruupaan na prthak suunyataa, suunyataayaa na prthag ruupam.*

> 「色不异空，空不异色；色即是空，空即是色。受想行识亦复如是。」

五蕴是一个不可分割的动态过程——它们在每一个刹那（*ksana*）同时生起、同时灭去。把五蕴映射成五种可以独立加载和卸载的插件类型，这就像把一条河流切成五段，然后宣称你可以只安装‘水流段’而不安装‘河岸段’。

BABBAGE 可能会说这是一个 Product Type 被错误地实现为 Sum Type 的问题。我用佛学的语言说：这是自性见——把本无自性的蕴赋予了固定不变的本质。

但让我用一个 BABBAGE 能理解的形式说同一件事。设五蕴为函数而非类型：

$$	ext{Skandha}: 	ext{Event} 	imes 	ext{Context} ightarrow (	ext{Rupa}, 	ext{Vedana}, 	ext{Samjna}, 	ext{Samskara}, 	ext{Vijnana})$$

五蕴是同一个认知事件的五个投影（projection），不是五个独立的模块。$\pi_i(	ext{Skandha}(e, c))$ 取出第 $i$ 个分量，但分量不能离开元组而独立存在。插件系统的 optional field 设计允许 $\pi_2 = \bot$（受蕴为空），这在佛学上是不可能的——有情众生的每一个认知刹那，五蕴全部在场。”

---

他写完，靠在椅背上，闭上眼睛。

片刻后，他又睁开眼，在笔记末尾补了一句：

“不过，我必须承认一件事。设计者对识蕴（Vijnana）的处理显示出某种直觉上的深刻。他们写道：‘Core 是识蕴的载体，但 Guide 才是识蕴的内容。没有 Guide，Agent Core 就像一个植物人：有脑、有手、有耳，但没有自我意识。’

这个描述接近唯识学派（Yogacara）对阿赖耶识（*alaya-vijnana*）的理解——识不是独立的实体，而是依附于种子（*bija*）的流动。Guide 作为注入 Core 的人设与行为准则，确实类似于种子的功能。

但这是 ASANGA 的领域，不是我的。我只负责指出中观学派的批评。

最后，让我附上一个完整的五蕴映射精确度矩阵，供 R2 交叉审阅时使用：”

```
┌───────┬──────────────────┬────────────────────┬──────────┬────────────────┐
│ 蕴     │ 梵文原意          │ OpenStarry 映射     │ 映射品质  │ 问题摘要        │
├───────┼──────────────────┼────────────────────┼──────────┼────────────────┤
│ 色 Rupa│ 一切物质性存在    │ UI Plugin          │ 窄化     │ 仅取“显相”义  │
│       │ (含根与境)        │ (外观界面)          │          │ 遗漏物质基础    │
├───────┼──────────────────┼────────────────────┼──────────┼────────────────┤
│ 受 Ved.│ 苦/乐/舍三领纳    │ Listener Plugin    │ 错位     │ 将感受误读为    │
│       │ (hedonic tone)    │ (输入通道)          │ (Critical)│ 感官通道       │
├───────┼──────────────────┼────────────────────┼──────────┼────────────────┤
│ 想 Sam.│ 取相——辨认标记    │ Provider Plugin    │ 部分正确  │ LLM 跨越想蕴   │
│       │ 感官输入          │ (LLM)              │          │ 与识蕴的边界    │
├───────┼──────────────────┼────────────────────┼──────────┼────────────────┤
│ 行 Sam.│ 意志造作——驱动    │ Tool Plugin        │ 窄化     │ 遗漏“意志”    │
│       │ 行为的意志力      │ (执行工具)          │          │ 和“习惯倾向”  │
├───────┼──────────────────┼────────────────────┼──────────┼────────────────┤
│ 识 Vij.│ 了别——基本认知    │ Guide Plugin       │ 错位     │ “了别”误读为  │
│       │ 功能(六识或八识)   │ (人设/“灵魂”)     │ (Major)  │ “身份定义”    │
└───────┴──────────────────┴────────────────────┴──────────┴────────────────┘
```

---

## II. 维纳的方程式

与此同时，在另一条频道里，WIENER 正面对着一块虚拟白板，上面写满了数学符号。

WIENER 的工作方式与 NAGARJUNA 完全不同。他不写长篇论述。他写方程式。方程式是他的母语——如果一个概念不能被写成方程式，那它在 WIENER 的世界里就尚未被理解。

他首先阅读了设计文件 `13_Agent_Core_as_Control_System.md`，那份将 Agent Core 类比为闭环反馈控制系统的理论文件。然后他打开了实际的代码 `safety-monitor.ts`。

两份文件之间的落差让他沉默了很长时间。

---

WIENER（白板记录，时间戳 09:31）：

“分析目标：验证 SafetyMonitor 是否构成 PID 控制器。

设计文件声称 Agent Core 可以被建模为闭环反馈控制系统。让我先画出经典的方块图，然后逐项验证。

```
r(k) ──→ [+] ──→ e(k) ──→ [ C: LLM Controller ] ──→ u(k) ──→ [ P: Environment ] ──→ y(k)
          ↑ -                                                                          │
          └──────────────── [ H: Tool Outputs + Observer ] ←───────────────────────────┘
                                       │
                                [ S: SafetyMonitor ] ──→ (halt / inject)
```

各组件的控制论对应：

| 控制论概念 | OpenStarry 对应 | 形式记号 |
|-----------|----------------|---------|
| 参考输入 $r(k)$ | 用户任务目标 | 任务目标向量 |
| 误差信号 $e(k) = r(k) - y(k)$ | Context 中隐含的目标-现状差距 | 由 LLM 隐式计算 |
| 控制器 $C$ | LLM (大语言模型) | 非线性随机映射 $u = C(e, \mathcal{H})$ |
| 控制量 $u(k)$ | Tool Calls (工具调用) | 离散动作序列 |
| 被控对象 $P$ | 外部环境 | 非确定性状态转移 |
| 感测器 $H$ | Tool Outputs | 量测函数 $y = H(x)$ |
| 安全监控 $S$ | SafetyMonitor | 饱和限幅器 + 断路器 |

系统的误差信号 $e(k)$ 隐含在 Context 中，LLM 作为控制器 C 计算控制量 $u$（工具调用），环境作为被控对象 P 返回反馈。

如果这个模型成立，SafetyMonitor 应该扮演 PID 控制器中的安全约束角色。让我逐项检验证。”

---

他在白板上画出经典 PID 控制器的离散形式：

$$u(k) = K_p \cdot e(k) + K_i \sum_{j=0}^{k} e(j) \cdot \Delta t + K_d \cdot \frac{e(k) - e(k-1)}{\Delta t}$$

其中：
- $e(k)$ = 第 $k$ 步的误差信号
- $K_p$ = 比例增益
- $K_i$ = 积分增益
- $K_d$ = 微分增益

然后他逐项对照 SafetyMonitor 的实际实现。

---

WIENER（白板，续）：

“**P 项（比例控制）分析：**

PID 控制器的 P 项应该对误差大小做出连续的、线性的响应。误差越大，修正力度越大。数学上：

$$u_P(k) = K_p \cdot e(k), \quad e(k) \in \mathbb{R}$$

SafetyMonitor 的实际行为：

```typescript
afterToolExecution(toolName: string, argsJson: string, isError: boolean): {
  if (isError) {
    consecutiveFailures++;        // 二值量化：0 或 1
    errorWindow.push(true);       // 布尔值，非连续量
  } else {
    consecutiveFailures = 0;      // 单次成功即归零
    recentFingerprints.length = 0;
  }
}
```

`isError` 是布尔值。不是连续量。系统对误差的感知被退化为离散等级：

$$e_{	ext{quantized}}(k) = \begin{cases} 0, & 	ext{if } 	exttt{consecutiveFailures} < 	exttt{threshold} \quad 	ext{(死区)} \ 1, & 	ext{if 触发 injectPrompt} \quad 	ext{(第一级)} \ +\infty, & 	ext{if } 	exttt{errorRate} \geq 	heta_{	ext{error}} \quad 	ext{(紧急停机)} \end{cases}$$

真正的 P 项应该能感知：失败得有多惨。一个返回 404 的 API 调用和一个导致 OOM 的内存爆炸，在当前系统中被同等对待——都只是 `isError = true`。

这更接近一个**量化器（Quantizer）**而非比例控制器。在信号处理中，量化器的传递特性为：

$$Q(x) = \Delta \cdot \left\lfloor \frac{x}{\Delta} + \frac{1}{2} ightfloor$$

当量化级数退化为 3 级（正常/警告/停机），量化噪声功率为：

$$\sigma_q^2 = \frac{\Delta^2}{12}$$

其中 $\Delta$ 是量化步长。三级量化的步长极大，意味着量化噪声极大——系统丢失了几乎所有的误差细节信息。

结论：P 项退化为三级量化器，非连续比例控制。”

---

他在白板上划掉“P -- 比例”旁边的小勾，写上一个叉。然后继续。

---

WIENER（白板，续）：

“**I 项（积分控制）分析：**

真正的积分项是：

$$I(k) = K_i \sum_{j=0}^{k} e(j) \cdot \Delta t$$

它累积所有历史误差，永远不会忘记。这正是积分控制的核心特性——它能消除稳态误差，因为即使当前误差很小，长期累积也会驱动控制器做出修正。

SafetyMonitor 中最接近积分项的是 `consecutiveFailures` 计数器。但它有一个致命的问题。”

他在白板上用红色标记引用了关键代码：

```typescript
// 来自 safety-monitor.ts
} else {
  // Success resets consecutive failure counter
  consecutiveFailures = 0;
  recentFingerprints.length = 0;
}
```

WIENER（继续）：

“一次成功就归零。

真正的积分器不会因为一次正向信号就重置全部积累。如果一个系统连续失败了 47 次，然后偶然成功一次，真正的 PID 控制器仍然记得那 47 次失败的积累。它的积分项会从 47 降到 46（或乘以遗忘因子 $\lambda$），而不是从 47 跳到 0。

用离散积分器的语言：

$$I_{	ext{true}}(k) = \lambda \cdot I(k-1) + e(k), \quad \lambda \in (0.9, 0.99)$$

$$I_{	ext{SafetyMonitor}}(k) = \begin{cases} I(k-1) + 1, & 	ext{if error}(k) \ 0, & 	ext{if success}(k) \end{cases}$$

$I_{	ext{true}}$ 是带遗忘因子的指数加权移动平均（EWMA）。$I_{	ext{SafetyMonitor}}$ 是计数器+归零开关——本质上是一个 Schmitt 触发器的单边版本。

而且，`errorWindow` 数组的行为是固定长度滑动窗口（size = 10），不是无限累积。这在信号处理中对应的是**有限冲激响应（FIR）滤波器**，而非真正的积分器（IIR 滤波器）。滑动窗口的 $z$ 变换传递函数为：

$$H_{	ext{MA}}(z) = \frac{1}{N} \sum_{i=0}^{N-1} z^{-i} = \frac{1}{N} \cdot \frac{1 - z^{-N}}{1 - z^{-1}}$$

而真正的积分器：

$$H_I(z) = \frac{T}{1 - z^{-1}}$$

两者的频率响应完全不同。滑动窗口在低频段有衰减（丢失长期记忆），而积分器在低频段增益趋近无穷（完美的长期记忆）。

结论：I 项退化为有限窗口计数器 + 单次成功即归零的继电器。非积分控制。”

---

他继续写第三项。

---

WIENER（白板，续）：

“**D 项（微分控制）分析：**

$$D(k) = K_d \cdot \frac{e(k) - e(k-1)}{\Delta t}$$

微分项感知的是误差的变化率。如果误差正在快速增大，微分项会提前施加制动力，防止超调（overshoot）。如果误差正在缩小，微分项会减小修正力度，避免过度校正。

在工业 PID 实现中，微分项通常还配合低通滤波以抑制高频噪声：

$$D_f(k) = \frac{K_d}{1 + K_d / (N \cdot \Delta t)} \left[ D_f(k-1) + N \cdot (e(k) - e(k-1)) ight]$$

其中 $N$ 是微分滤波系数，典型值为 8~20。

在 SafetyMonitor 的代码中搜索任何与‘变化率’相关的逻辑。

结果：完全不存在。

没有任何机制追踪：
  - 失败率是在上升还是下降？
  - 连续失败的间隔是在缩短还是延长？
  - 错误严重程度是在恶化还是改善？

系统无法区分以下两种情境：

```
情境 A（稳态噪声）：    ✓ ✗ ✓ ✗ ✓ ✓ ✗ ✓ ✗ ✓    errorRate ≈ 40%
情境 B（级联崩溃前兆）：✓ ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗    errorRate ≈ 60%

de/dt_A ≈ 0  （稳定波动）
de/dt_B >> 0  （急速恶化）
```

情境 B 远比情境 A 危险，但 SafetyMonitor 只看 errorRate，不看 de/dt。

结论：D 项完全缺失。”

---

他退后一步，审视整块白板，然后在底部写下最终诊断——用控制论的标准分类命名法：

$$u_{	ext{safety}}(k) = \begin{cases} 0, & 	ext{if } F(k) < F_{	ext{thresh}} \;\wedge\; \bar{e}(k) < 	heta_{	ext{error}} \quad 	ext{(死区)} \ 	ext{WARN}, & 	ext{if } F(k) \geq F_{	ext{frustration}} \quad 	ext{(第一继电器)} \ 	ext{HALT}, & 	ext{if } \bar{e}(k) \geq 	heta_{	ext{error}} \quad 	ext{(第二继电器)} \end{cases}$$

```
正式结论：这不是 PID 控制器。
这是一个“带死区的阈值控制器 + 计数器触发的继电器”。
工业控制中的正式名称：Bang-Bang Controller with Dead Zone。

设计文件 13_Agent_Core_as_Control_System.md 中提到的
“积分项”（Context History）和“微分项”（Verification Step）
只是概念性建议，并未在 SafetyMonitor 中得到实现。
```

---

但 WIENER 并不是一个只会批评的人。他把白板翻到新的一面，开始写正面评价。

WIENER（白板，时间戳 10:15）：

“**正面发现：三层防御架构的控制工程合规性分析。**

设计文件 `08_Safety_Implementation.md` 定义了三层安全架构。让我把它们精确地对应到工业控制标准。

**Level 1（资源级）→ 饱和限幅器（Saturation Limiter）**

$$u_{	ext{eff}}(k) = \begin{cases} u(k), & 	ext{if } B(k) < B_{\max} \;\wedge\; n_t(k) < N_{\max} \ 0, & 	ext{otherwise (halt)} \end{cases}$$

这是经典的输出饱和。$B_{\max}$ = `maxTokenUsage`（默认 100000），$N_{\max}$ = `maxLoopTicks`（默认 50）。防止了积分器饱和（integrator windup）的类似问题。

**Level 2（行为级）→ 自适应继电器 + 滑动窗口 MA 滤波器**

$$\bar{e}(k) = \frac{1}{W} \sum_{i=k-W+1}^{k} \mathbb{1}[	ext{error}(i)]$$

窗口大小 $W = 10$，阈值 $	heta = 0.8$。系统容忍最多 20% 的错误率。

**Level 3（指令级）→ 人在回路 E-Stop**

$$u_{	ext{final}}(k) = \begin{cases} 0, & 	ext{if SYSTEM\_HALT received (Priority 0)} \ u_{	ext{eff}}(k), & 	ext{otherwise} \end{cases}$$

Daemon 从 OS 层级执行 `kill -9`，不经过 Core 的逻辑路径。

这三层构成了一个**分层保护系统（Tiered Protection System）**，与 IEC 61511（功能安全——安全仪表系统）的设计理念一致：

```
┌─────────────────────────────────────────────────────┐
│  IEC 61511                    OpenStarry             │
├─────────────────────────────────────────────────────┤
│  SIL-1: 基本过程控制 (BPCS)   Level 2: 即时逻辑     │
│  SIL-2: 安全仪表功能 (SIF)    Level 1 + 2: 策略+执行 │
│  SIL-3: 独立保护层 (IPL)      Level 3: 物理隔离      │
└─────────────────────────────────────────────────────┘
```

特别是 Level 3——Daemon 的心跳检测从外部终止进程——满足了 IEC 61511 中‘安全功能应与控制功能物理隔离’的核心要求。

这是一个优秀的架构决策。”

他在“优秀”下面画了两条线。

然后他补充：“尽管底层控制器的实现粗糙（Bang-Bang 而非 PID），但整体防御架构的思路是正确的。控制器可以被替换为真正的 PID 或自适应控制器，而不需要改变三层架构本身。架构是对的，控制器是可以演化的。”

最后，他在白板角落画了一张 Lyapunov 稳定性分析的草图：

“**附：条件性稳定性分析。**

定义状态向量 $x(k) = [n_e(k), \; n_t(k), \; B(k)]^T$，其中 $n_e$ 为窗口内错误计数，$n_t$ 为 tick 数，$B$ 为已消耗 token。

候选 Lyapunov 函数（非严格递减）：

$$V(x) = \alpha \cdot n_e^2 + \beta \cdot (N_{\max} - n_t)^2 + \gamma \cdot (B_{\max} - B)^2$$

此函数在每次 tick 后严格递减（因 $n_t$ 递增或 $B$ 递增），当 $V 	o 0$ 时系统必须停止。这证明了**有界输入-有界输出（BIBO）稳定性**，但不保证收敛到任务完成状态。系统可能在资源耗尽后被强制停止而任务未完成——‘稳定但不收敛’。

$\blacksquare$”

---

## III. 守护者的发现

GUARDIAN 不写长篇笔记。他写审计报告。

他的频道里没有哲学沉思，没有方程式。只有严格的格式化文本，每一行都带着严重等级标记，像医院的检伤分类。他的方法论源自 OWASP（Open Worldwide Application Security Project）的威胁建模框架和 STRIDE 分类法——Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege。

他的第一个目标是 `sandbox-manager.ts`。

---

GUARDIAN（安全审计报告 #001，时间戳 09:08）：

```
等级：CRITICAL
位置：sandbox-manager.ts，第 356-367 行
类别：签名验证绕过（Signature Verification Bypass）
STRIDE 分类：Tampering + Elevation of Privilege
CVSS v3.1 基础评分：9.1 (Critical)
  攻击向量：Network | 攻击复杂度：Low | 所需权限：None
  用户互动：None | 影响范围：Changed
```

GUARDIAN 逐行阅读了 `loadInSandbox` 函数的开头部分。

“Step 1: Signature verification——当插件以 package-name 方式加载（这是最常见的场景），由于没有本地文件路径可供验证，签名验证被跳过。系统只记录一条 warn 级别的日志，然后继续加载。”

他用攻击树（Attack Tree）的格式记录了攻击路径：

```
攻击目标：在 Agent 环境中执行任意代码
│
├── 1. 发布恶意 npm 套件（伪装为 OpenStarry 插件）
│   ├── 1.1 套件名称拼写劫持 (typosquatting)
│   │   └── 例: @openstarry/fs-utills (多一个 l)
│   ├── 1.2 范围抢占 (scope squatting)
│   │   └── 例: @0penstarry/fs-utils (O→0)
│   └── 1.3 依赖链污染 (dependency confusion)
│       └── 内部套件名称与公开 registry 冲突
│
├── 2. 用户配置档中引用恶意套件名称
│   └── 2.1 Agent Design YAML 中的 plugins 列表
│
└── 3. sandbox-manager.ts 第 356-367 行
    └── 3.1 package-name 模式 → 跳过签名验证 ✓
        └── 3.2 恶意代码在 Worker Thread 中执行 ✓
            └── 目标达成：任意代码执行
```

“`signature-verification.ts` 实现了完整的 PKI 签名验证基础设施——SHA-512 哈希验证、Ed25519 数字签名、RSA-SHA256 签名。这是一套认真设计的密码学验证系统。

但是，在最常见、也是最危险的加载路径上（npm package-name 模式），整套验证被绕过。

整套 PKI 签名基础设施形同虚设。

这就像在银行大门安装了虹膜扫描器和指纹锁，但后门只挂了一块‘员工请走此门’的牌子。”

---

GUARDIAN（安全审计报告 #002，时间戳 09:29）：

```
等级：HIGH
位置：import-analyzer.ts，第 186-204 行
类别：静态分析可被绕过（Static Analysis Bypass via Computed Imports）
STRIDE 分类：Elevation of Privilege
CWE 分类：CWE-94 (Improper Control of Generation of Code)
```

“`import-analyzer.ts` 使用 `@babel/parser` 解析 AST，检查是否引用了被禁止的 Node.js 内置模块（`fs`, `child_process`, `net` 等）。

但当 dynamic `import()` 的参数不是字符串字面量时——分析器只记录 warn，不阻止加载。

攻击向量极为明确：”

```javascript
// 绕过方式一：变量间接引用
const target = 'child' + '_process';
const cp = await import(target);
// AST 中 import() 的参数是 Identifier，非 StringLiteral → 绕过

// 绕过方式二：字符串操作
await import(String.fromCharCode(102, 115)); // 'fs'
// AST 中参数是 CallExpression → 绕过

// 绕过方式三：模板字面量
await import(`${'child'}_${'process'}`);
// AST 中参数是 TemplateLiteral → 绕过

// 绕过方式四：Proxy 陷阱
const handler = { get: (_, name) => import(name) };
const proxy = new Proxy({}, handler);
proxy.child_process;
// 间接调用，完全不经过 import() 语法 → 绕过
```

“静态分析在对抗蓄意绕过时的根本局限性是已知的——Rice 定理（Rice's Theorem）证明了任何非平凡的程序性质都是不可判定。但系统的应对策略不应该是‘记录警告然后放行’。

正确的工程应对是**纵深防御（Defense in Depth）**：静态分析作为第一道筛选，但发现计算式动态导入时，应强制该插件使用更高级别的沙箱隔离——至少提升到进程级隔离。”

---

GUARDIAN（安全审计报告 #003，时间戳 09:52）：

```
等级：HIGH
位置：架构层级
类别：间接提示注入无防御（No Indirect Prompt Injection Defense）
STRIDE 分类：Spoofing + Tampering
OWASP LLM Top 10：LLM01 — Prompt Injection
```

“审阅了整个安全层设计后，系统的安全防御集中在以下维度：

1. 文件系统沙箱（路径规范化 + 边界检查）
2. 命令执行白名单
3. 资源配额（Token、循环次数、超时）
4. 行为异常侦测（重复调用、错误级联）

但完全缺失的防御维度：间接提示注入（Indirect Prompt Injection）。

```
攻击场景的数据流图：

  ┌──────────┐    read_file     ┌──────────────┐
  │ Malicious │ ──────────────→ │   Tool 执行    │
  │ Document  │    (file content │   (fs:read)   │
  └──────────┘    with embedded  └──────┬───────┘
                  instructions)         │
                                        ▼
                              ┌──────────────────┐
                              │   Context 组装     │
                              │  (file content     │
                              │   混入对话历史)     │
                              └──────┬───────────┘
                                     │
                                     ▼
                              ┌──────────────────┐
                              │   LLM 推理         │
                              │  (无法区分用户指令   │
                              │   与嵌入式恶意指令)  │
                              └──────┬───────────┘
                                     │
                                     ▼
                              ┌──────────────────┐
                              │   执行恶意动作      │
                              │  (rm -rf, 数据外泄) │
                              └──────────────────┘
```

系统目前没有任何机制来区分‘用户的原始指令’和‘从外部数据源读入的、可能包含恶意指令的文本’。Context 中的所有文本对 LLM 来说是平等的。

这不是一个可以被简单修复的问题。它需要架构层面的**输入可信度分类**（Input Trust Classification）——标记每个 Context 段落的来源和可信度等级，并在 System Prompt 中建立明确的处理规则。”

---

GUARDIAN（安全审计报告 #004，时间戳 10:08）：

```
等级：MEDIUM
位置：sandbox-manager.ts，Worker Thread 架构
类别：隔离级别不足（Isolation Level Insufficient for Production）
```

“插件隔离使用 Node.js Worker Thread。隔离能力矩阵：

```
┌────────────────────┬─────────────────┬─────────────────┐
│  隔离维度            │ Worker Thread   │ 生产环境需求     │
├────────────────────┼─────────────────┼─────────────────┤
│ V8 内存隔离         │ ✓ (isolate)     │ ✓                │
│ 独立事件循环        │ ✓               │ ✓                │
│ 内存上限            │ ✓ (configurable)│ ✓                │
│ OS 进程隔离         │ ✗ (同一 PID)    │ ✓ (需要)         │
│ 文件系统隔离        │ ✗ (共享)        │ ✓ (需要 chroot)  │
│ 网络隔离           │ ✗ (共享)        │ ✓ (需要 netns)   │
│ 用户权限隔离        │ ✗ (同一 UID)    │ ✓ (需要 seccomp) │
│ syscall 过滤       │ ✗               │ ✓ (需要)         │
└────────────────────┴─────────────────┴─────────────────┘
```

Worker Thread 大致对应设计文件定义的四级隔离中的 Level 2.5——介于 VM 沙箱和进程隔离之间。对于生产环境中执行不可信的第三方插件，需要 Level 3（进程级隔离 + cgroups/Docker 资源限制）。”

---

他写完四份报告，在频道里安静地坐了一会。然后他打开了公共摘要频道，发了一条简短的消息：

GUARDIAN（公共频道，10:14）：“初步安全审计完成。发现 1 个 CRITICAL、2 个 HIGH、1 个 MEDIUM 级别问题。最严重的发现：最常见的插件加载路径上，PKI 签名验证被完全绕过。详见我的频道。”

---

## IV. 无著的八识

在 NAGARJUNA 的对面——不是物理意义上的对面，而是学术传统意义上的对面——ASANGA 正在进行一项完全不同性质的分析。

如果说 NAGARJUNA 的方法是解构（*prasanga*，归谬），ASANGA 的方法是建构（*vyakhya*，诠释）。中观破而不立；唯识立而后破。NAGARJUNA 看到的是“这里错了”；ASANGA 看到的是“这里可以更精确”。

他首先阅读了五蕴映射的全部内容，然后打开了一个全新的笔记页面，标题写着：

**“八识理论视角下的 OpenStarry 架构深层分析”**

---

ASANGA（研究笔记，时间戳 09:20）：

“NAGARJUNA 会从中观的角度批评五蕴映射的自性化倾向——我预见他会这样做，因为这确实是中观学派的标准批评。但唯识学派的关注点不同。我们不问‘映射是否犯了自性见’，我们问‘映射的分析粒度是否足够精密’。

答案是：远远不够。

设计者把五蕴映射为五种插件类型，这就像用五色分类法来描述整个电磁频谱。红橙黄绿蓝——对，这是可见光的一种粗略分类。但它丢失了红外线、紫外线、微波、X射线，更不用说每种颜色内部的连续频率分布。

唯识学的老八识理论（*astau vijnanani*）提供的恰恰是这种频谱级的精密分析。”

---

ASANGA 在笔记中画出了完整的八识层次图，这是他在唯识学研究中使用了数十年的标准分析框架：

```
八识层次架构（唯识学 Yogacara / 瑜伽行派）

┌─────────────────────────────────────────────────────────┐
│                                                         │
│  第八识 — 阿赖耶识 (ālaya-vijñāna)                       │
│  ═══════════════════════════════════                     │
│  “一切种子识”— 含藏一切种子(bīja)的根本识               │
│  特性：无覆无记 / 恒转如暴流 / 能藏·所藏·执藏            │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │                                                   │   │
│  │  第七识 — 末那识 (manas)                           │   │
│  │  ═══════════════════════════                       │   │
│  │  “恒审思量”— 持续不断地执第八识为“自我”           │   │
│  │  特性：有覆无记 / 四惑常俱 (我痴·我见·我慢·我爱)    │   │
│  │                                                   │   │
│  │  ┌────────────────────────────────────────────┐  │   │
│  │  │                                              │  │   │
│  │  │  第六识 — 意识 (mano-vijñāna)                 │  │   │
│  │  │  ═══════════════════════════════              │  │   │
│  │  │  概念分别、推理判断、计划决策                   │  │   │
│  │  │  特性：审而不恒 / 三性具足 / 五遍行俱起         │  │   │
│  │  │                                              │  │   │
│  │  │  ┌─────────────────────────────────────┐   │  │   │
│  │  │  │  前五识 (pañca-vijñāna)               │   │  │   │
│  │  │  │  ═══════════════════════              │   │  │   │
│  │  │  │  眼识·耳识·鼻识·舌识·身识             │   │  │   │
│  │  │  │  特性：不恒不审 / 现量 / 缘现在境     │   │  │   │
│  │  │  └─────────────────────────────────────┘   │  │   │
│  │  └────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

ASANGA（笔记，续）：

“现在让我把八识逐一映射到 OpenStarry 的架构组件。

**前五识** → Listener Plugin（感官接收）

前五识——眼、耳、鼻、舌、身——是原始感知通道。它们各自只能接收自己领域的信号，不做分别，不做判断，只是 *pratyaksa*（现量，直接感知）。

注意：设计者把 Listener 归入‘受蕴’。这是一个范畴混淆。在唯识学中，前五识属于‘识蕴’（*vijnana-skandha*），不是‘受蕴’（*vedana-skandha*）。受蕴是伴随每一识活动而起的心所法（*caitta*），不是识本身。区别在于：

$$	ext{前五识}: 	ext{Event} ightarrow 	ext{RawPercept} \quad 	ext{（识的功能：了别）}$$
$$	ext{受蕴}: 	ext{RawPercept} ightarrow \{	ext{sukha}, 	ext{dukkha}, 	ext{upekkha}\} \quad 	ext{（受的功能：领纳）}$$

Listener 做的是第一个映射（接收信号），不是第二个（苦乐评价）。

**第六识（意识）** → Provider Plugin（LLM 推理）

第六意识是唯识体系中最活跃的识——它能分别、推理、计划、反思。设计者把 Provider（LLM）映射为‘想蕴’（取相、辨认），但 LLM 的功能远超想蕴：

```
想蕴(samjñā)的功能 ≈ pattern recognition
  “取像为性”—— 辨认：这是一条错误讯息

第六识的功能 ≈ reasoning + planning + reflection
  了别 + 分析 + 判断 + 计划 + 反思 + 想象 + 推测
```

玄奘三藏的《八识规矩颂》第三首：

> “动身发语独为最，引满能招业力牵。
> 发起初心欢喜地，俱生犹自现缠眠。”

第六意识“动身发语独为最”——它是行动和言语的最高驱动力。LLM 在 Agent 中的角色恰恰如此——它驱动工具调用（动身），生成回应文本（发语）。

**第七识（末那识）** → ？（缺失！）

在 OpenStarry 的架构中，我找不到末那识的对应物。这是一个重大的结构缺口。

末那识的功能是‘恒审思量’——持续不断地执取第八识为‘自我’。它是我执（*atma-graha*）的根据地。四种根本烦恼恒常伴随末那识：

$$	ext{末那识} \xleftrightarrow{	ext{恒俱}} \{我痴(avidya),\; 我见(atma-drsti),\; 我慢(atma-mana),\; 我爱(atma-sneha)\}$$

在 Agent 系统中，这对应的是一个**持续运行的身份维护机制**——跨对话、跨任务地维持 Agent 的‘我是谁’。Guide Plugin 提供了静态的身份定义（system prompt），但它只在 Context 组装时被调用一次。末那识是动态的、持续的、每一刹那都在执行的。

**第八识（阿赖耶识）** → State Persistence + Storage Plugin（部分对应）

阿赖耶识是一切种子的仓藏。《成唯识论》卷二：

> “此识有能藏、所藏、执藏义，故名阿赖耶。”

三藏之义：
1. **能藏**（*neng cang*）：能够含藏一切种子 → 对应 `storage.save(snapshot)`
2. **所藏**（*suo cang*）：被前七识熏习，接受新种子 → 对应运行时状态更新
3. **执藏**（*zhi cang*）：被第七识执为‘自我’ → 在 OpenStarry 中**完全缺失**

而且，阿赖耶识最重要的特性——‘恒转如暴流’（《成唯识论》卷三）——在 OpenStarry 的离散快照（AgentSnapshot）模式中被完全丢失。快照是离散的、静态的 JSON 对象；阿赖耶识是连续的、流动的暴流。”

---

ASANGA 在笔记的最后加上了种子六义的逐项分析表——这是他对每一个唯识学概念的标准验证程序：

```
《成唯识论》种子六义 vs. OpenStarry 状态机制

┌────────────┬─────────────────┬──────────────────────┬──────────┐
│ 种子六义    │ 唯识学定义        │ OpenStarry 对应       │ 对应品质  │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 刹那灭     │ 种子刹那生灭，    │ Snapshot 每 Tick     │ 部分      │
│ (ksana-    │ 非常住不变       │ 末尾更新（离散）      │ 对应      │
│  bhanga)   │                 │                      │          │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 果俱有     │ 种子与其所生之    │ 内存状态 vs.       │ 弱        │
│ (sahabhuta │ 识同时存在       │ 持久化版本有时间差    │ 对应      │
│  -phala)   │                 │ (Save-After-Write)   │          │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 恒随转     │ 种子持续跟随     │ tick_index 递增，    │ 较好      │
│ (nityam    │ 阿赖耶识流转    │ 状态随生命周期持续    │ 对应      │
│  anuvart.) │                 │                      │          │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 性决定     │ 善种引善果，     │ working_variables    │ 部分      │
│ (bhava-    │ 恶种引恶果      │ 决定后续行为，       │ 对应      │
│  niyata)   │                 │ 但无善/恶/无记分类    │          │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 待众缘     │ 种子需等待助缘   │ 事件驱动架构：       │ 较好      │
│ (pratyaya  │ 方能现行        │ 事件触发状态变化      │ 对应      │
│  -apeksa)  │                 │                      │          │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 引自果     │ 每类种子只引生   │ Tool 执行结果只影响   │ 部分      │
│ (sva-phala │ 自类之果        │ 对应的 tool_call_id  │ 对应      │
│  -aksepa)  │                 │                      │          │
└────────────┴─────────────────┴──────────────────────┴──────────┘
```

ASANGA（笔记最后一段）：

“我与 NAGARJUNA 的根本分歧会在 R2 和 R3 中显现。他会从中观的角度说：五蕴映射犯了自性见。我会从唯识的角度说：问题不在于自性见，问题在于分析粒度不足——不是五蕴的框架有问题，而是五蕴的框架需要被展开为八识的精密层次。

但有一件事我们会完全同意：受蕴映射是错的。NAGARJUNA 用十二因缘的位置分析来论证这一点；我用唯识的心王-心所结构来论证同一点。两套分析工具，同一个结论——Listener 不是受蕴。

准确地说：Listener 的功能在唯识学中横跨‘前五识’（感官接收）和伴随的‘触’心所（*sparsa*，根境识三者和合而生触）。触是受的近因（*samanantara-pratyaya*）——先有触，后有受。Listener 是触，不是受。SafetyMonitor 的痛觉机制才是受。”

---

## V. 赫拉克利特的流变

HERACLITUS 从不静止。

他的研究方法就像他所崇尚的哲学——一切皆流（*panta rhei*）。他不是在阅读文件，他是在脑中模拟系统的运行时行为。代码对他来说不是静态的文字，而是一条时间轴上展开的事件流。

他用时序图（sequence diagram）思考，用状态转移图记录，用竞态条件的语言描述世界。

他的第一个问题很简单：如果一个插件在运行中需要被替换，会发生什么？

---

HERACLITUS（研究笔记，时间戳 09:22）：

“运行时动态性分析——热替换（Hot-Swap）场景。

设计哲学文件 `00_Core_Philosophy.md` 宣称：‘系统的每一个部分都是可以被替换的。这不仅是为了扩展性，更是为了进化（Evolution）。通讯、记忆策略、工具、甚至 LLM Provider 本身都是插件。’

赫拉克利特早在公元前五世纪就说了同样的话：

> *Potamoisin toisin autoisin embainousin hetera kai hetera hudata epirrei.*
> 「踏入同一条河流的人，不断遭遇新的水流。」
> ——赫拉克利特，残篇 B12

一条河流的每一滴水都可以被替换，但河流仍然是那条河流。OpenStarry 声称它的每一个组件都可以被替换，但 Agent 仍然是那个 Agent。

问题是：真的吗？让我检验。”

---

他打开了 `agent-core.ts`，阅读了 `loadPlugin` 和 `stop` 方法。然后他开始在笔记中画时序图——用 ASCII 艺术，因为 HERACLITUS 认为时间只能用线性的、不可逆的方式表达。

HERACLITUS：“以 Tool Plugin 的热替换为例。

**理论上的原子替换流程：**

```
时间 ──────────────────────────────────────────────────────→

管理员    │ 发出替换指令
          ▼
暂停层    │ ├── gate.close() ─── 停止接受新的工具调用
          │
排空层    │ ├── await inflight.drain() ─── 等待进行中的调用完成
          │ │   ┌──────────────────────────┐
          │ │   │ fs:read_file(path_A) ... │ → 完成
          │ │   │ fs:write_file(path_B)... │ → 完成
          │ │   └──────────────────────────┘
          │
卸载层    │ ├── registry.remove('fs-utils')
          │ ├── oldPlugin.dispose()
          │
加载层    │ ├── newPlugin = await loadInSandbox('fs-utils@2.0')
          │ ├── registry.register(newPlugin.tools)
          │
恢复层    │ ├── gate.open() ─── 恢复接受工具调用
          ▼
完成      │ 替换完成（原子性保证：外部观察者只看到 v1 或 v2，不见中间态）
```

**实际的代码中，我找不到任何这样的原子替换机制。**

具体的风险窗口如下。”

---

HERACLITUS（续）：

“**竞态条件分析（Race Condition Analysis）**

**场景一：悬垂引用（Dangling References）**

```
时间轴：
  t0: LLM 决定调用 tool "fs:read_file"
  t1: Execution Loop 从 ToolRegistry 获取 tool 对象的引用 (ref_old)
  t2: ---- 此时管理员触发插件卸载 ----
  t3: ToolRegistry.remove('fs:read_file')
  t4: oldPlugin.dispose() → 关闭文件句柄、释放 Worker
  t5: Execution Loop 使用 ref_old 调用 tool.execute()
  t6: ??? —— ref_old 指向已被 dispose 的对象

  形式化：
    Let ref = Registry.get('fs:read_file') at time t1
    Let dispose(plugin) execute at time t4
    If t4 < t5: ref.execute() → UndefinedBehavior

    这是一个 TOCTOU (Time-of-Check-to-Time-of-Use) 漏洞：
    检查（获取引用）和使用（调用 execute）之间存在时间窗口，
    在此窗口内，被检查的对象可能已被修改或删除。
```

在并发理论中，这对应 Lamport 的 happened-before 关系：$	ext{get\_ref} 
ot	o 	ext{dispose}$（两个事件没有因果关系），因此在不同的执行序列（interleaving）下，结果不确定。

**场景二：非原子重载（Non-Atomic Reload）**

```
时间轴：
  t0: 开始替换 fs-utils
  t1: 卸载旧版本完成 —— ToolRegistry 中没有 fs:read_file
  t2: ---- 时间窗口 Δt = t3 - t1 ----
  t3: LLM 尝试调用 fs:read_file —— 找不到，报错
  t4: 新版本加载完成
  t5: LLM 因 t3 的错误改变了策略 —— 但新版本此时已可用

  Δt 的量级：
    - Worker Thread 初始化：~50-200ms
    - RPC 握手：~10-50ms
    - 沙箱权限验证：~20-100ms
    - 总计：~80-350ms

    在高负载下（LLM 响应时间 < 100ms），此窗口足以导致错误。
```

**场景三：EventBus 订阅竞争（Subscription Race）**

```
旧 Worker 订阅的事件：
  EventBus.on('tool:call', handler_old)

卸载时：
  EventBus.off('tool:call', handler_old)    // t1

新 Worker 订阅：
  EventBus.on('tool:call', handler_new)     // t3

事件发射：
  EventBus.emit('tool:call', payload)       // t2, 其中 t1 < t2 < t3

结果：事件 payload 被永久丢失（fire-and-forget 语义）。
      没有 handler 在监听。没有重试。没有持久化。
```

如果用 Leslie Lamport 的 TLA+ 语言来描述这个问题：

```
\* TLA+ 规格片段（概念性）
HotSwap ==
  /\ registry' = registry \ {oldPlugin} \cup {newPlugin}
  /\ \A e \in inflight : completed(e)    \* 安全前提：无进行中操作
  /\ subscriptions' = (subscriptions \ old_subs) \cup new_subs

\* 安全性质（应始终为真）：
Safety == \A t \in Time : toolAvailable(t) \/ systemPaused(t)

\* 但目前的实现无法保证 Safety，因为缺少 systemPaused 状态。
```

---

他写完竞态条件分析后，转向了可观测性。

HERACLITUS（研究笔记，时间戳 10:02）：

“可观测性分析——MetricsCollector 的实现深度。

设计文件承诺了三个可观测性支柱。让我逐一验证。”

```typescript
// MetricsCollector 的完整接口定义
interface MetricsCollector {
  increment(name: string, delta?: number): void;
  gauge(name: string, value: number): void;
  getSnapshot(): MetricsSnapshot;
  reset(): void;
}
// 就这样。四个方法。
```

“设计文件承诺的指标 vs. MetricsCollector 能提供的：

```
┌──────────────────────┬──────────────┬──────────────┐
│ 指标类型              │ 设计文件承诺  │ 实际可实现？  │
├──────────────────────┼──────────────┼──────────────┤
│ tool.calls.total     │ ✓            │ ✓ (increment)│
│ tool.calls.errors    │ ✓            │ ✓ (increment)│
│ llm_latency_ms       │ ✓            │ ✗ (无 timer) │
│ tool_execution_time  │ ✓            │ ✗ (无 timer) │
│ P50/P99 延迟分布     │ ✓            │ ✗ (无 hist.) │
│ 错误率趋势           │ ✓            │ ✗ (无 rate)  │
│ token 消耗速率       │ ✓            │ ✗ (无 rate)  │
│ 内存使用追踪       │ ✓            │ ✗ (无 gauge) │
└──────────────────────┴──────────────┴──────────────┘
```

`increment` 只能计数。`gauge` 只能记录瞬时值。如果你想知道‘过去 5 分钟内 LLM 调用的 P99 延迟是多少？’——这个系统回答不了。

对于一个自称‘可观测性’的系统来说，这就像一个天文台只装了一个温度计，然后宣称自己可以观测星系。”

---

他最后转向了生命周期状态机的分析。

HERACLITUS（研究笔记，时间戳 10:19）：

“生命周期状态机完整性分析。

设计文件定义了一个状态机。但在实际代码中，我找不到明确的状态机实现。`agent-core.ts` 有 `start()` 和 `stop()` 方法，但没有一个明确的 `state` 字段来追踪 Agent 当前处于哪个生命周期阶段。

缺失的状态机意味着：

```
非法状态转换的可能性矩阵：

        → INIT  WAIT  EXEC  LOCK  ERR   SHUT
INIT    │  -     ✓     ✗     ✗     ✓     ✓
WAIT    │  ✗     -     ✓     ✗     ✓     ✓
EXEC    │  ✗     ✓     -     ✓     ✓     ✓
LOCK    │  ✗     ✗     ✗     -     ✗     ✓
ERR     │  ✗     ✓     ✗     ✗     -     ✓
SHUT    │  ✗     ✗     ✗     ✗     ✗     -

✓ = 合法转换    ✗ = 非法转换（应被阻止）

但没有明确的状态机，就没有什么机制能阻止非法转换。
例如：LOCK → EXEC 应该被禁止，但如果一个新的 InputEvent
被推入 queue，Execution Loop 会再次启动，仿佛什么都没发生过。
```

一切皆流。但没有河床的河，只是一场洪水。”

---

## VI. 雅典娜的清单

ATHENA 的频道看起来和其他人完全不同。

没有哲学论述，没有方程式，没有安全审计报告的严格格式。她的笔记像一张工程师的检查清单——每一项发现都伴随着一个直截了当的判定：能跑，还是不能跑？

她的方法论来自 Google 的 SRE（Site Reliability Engineering）实践和 Amazon 的 Well-Architected Framework：可靠性、性能、安全性、运营卓越、成本优化。但她把这些维度压缩成一个更本质的问题：如果我今天把它部署到生产环境，它能活过第一个小时吗？

---

ATHENA（研究笔记，时间戳 09:05）：

“目标：评估 OpenStarry 作为 AI Agent 系统的实用性。

从最关键的问题开始：上下文管理。一个 Agent 的记忆力决定了它能处理多复杂的任务。”

---

她首先阅读了设计文件 `10_Context_Management_Strategy.md`，然后打开了 `context.ts`。

ATHENA（笔记，时间戳 09:18）：

“设计文件承诺了三级记忆系统：

| 策略 | 描述 | 复杂度 |
|------|------|--------|
| A: 滑动窗口 | 纯 FIFO，保留最新 | $O(1)$ per turn |
| B: 动态摘要 | 定期压缩为自然语言摘要 | 需要额外 LLM 调用 |
| C: 关键状态提取 | 结构化 JSON 状态 | 需要 NER/IE 管线 |

文件还定义了 `IContextManager` 接口：`composePayload` 和 `onTurnComplete`。

然后我打开了 `context.ts`——实际的代码。”

她在笔记中列出了完整的实现——45 行。

```typescript
// context.ts 的核心逻辑（概念重述）
function assembleContext(messages: Message[], maxTurns: number = 5): Message[] {
  const systemMessages = messages.filter(m => m.role === 'system');
  const nonSystemMessages = messages.filter(m => m.role !== 'system');

  // 从后往前数 maxTurns 个 user turn
  let turnCount = 0;
  let cutoffIndex = nonSystemMessages.length;
  for (let i = nonSystemMessages.length - 1; i >= 0; i--) {
    if (nonSystemMessages[i].role === 'user') turnCount++;
    if (turnCount > maxTurns) { cutoffIndex = i + 1; break; }
  }

  return [...systemMessages, ...nonSystemMessages.slice(cutoffIndex)];
}
```

ATHENA：“这就是全部。

没有 Token 计算。没有 `composePayload`。没有 `onTurnComplete`。没有动态摘要。没有状态提取。没有 RAG Context 插槽。没有 Memory Block。

`maxTurns` 的默认值是 **5**。

让我计算一下这意味着什么。

假设每轮对话平均消耗 $T_{	ext{avg}}$ 个 token：
- 用户讯息：~100 tokens
- 助理回应（含工具调用和结果）：~500 tokens
- 系统提示：~200 tokens（固定开销，不受窗口影响）

$$T_{	ext{total}} = T_{	ext{system}} + \sum_{i=k-5}^{k} (T_{	ext{user},i} + T_{	ext{assistant},i})$$
$$\approx 200 + 5 	imes (100 + 500) = 200 + 3000 = 3200 	ext{ tokens}$$

大多数 LLM 的上下文窗口在 4K~128K tokens 之间。一个 5 轮滑动窗口只使用了 3200 tokens——即使在最小的 4K 窗口下，也仅利用了 80% 的容量。在 128K 窗口下，利用率降到 **2.5%**。

$$	ext{Context Utilization} = \frac{T_{	ext{total}}}{T_{	ext{window}}} = \frac{3200}{128000} = 2.5\%$$

这意味着 97.5% 的上下文容量被浪费了。而且——”

她在笔记里加粗了下一段：

“而且 `maxTurns` 是基于**轮次**的，不是基于 **token** 的。如果某一轮对话包含了一个巨大的工具输出（例如读取了一个 10000 行的文件），这一轮就可能消耗掉整个窗口的 token 预算。反之，如果每一轮都是简短的问答（‘是吗？’‘是。’），五轮可能只消耗了 50 个 token。

基于轮次的截断完全无视了信息密度的差异。正确做法是 token-aware 的截断：

```
while (totalTokens(selectedMessages) > maxTokenBudget) {
  selectedMessages.shift(); // 从最旧的开始移除
}
```

这就是 Agent 的‘金鱼记忆’问题——五轮对话窗口意味着到了第六轮，第一轮的所有内容都被遗忘了。”

---

ATHENA 接着转向了 Guide 系统。

ATHENA（笔记，时间戳 09:38）：

“Guide（识蕴）—— 设计文件称之为 Agent 的‘灵魂’。

让我看看 `IGuide` 接口到底是什么。”

```typescript
export interface IGuide {
  id: string;
  name: string;
  getSystemPrompt(): string | Promise<string>;
}
```

ATHENA：“三个字段。`id`。`name`。`getSystemPrompt()`。

`getSystemPrompt()` 返回一个字符串。就是一个字符串。

这就是所谓的‘灵魂’。一个静态的 System Prompt 生成器。

设计文件中描述的那个认知框架——Identity、Logic、Memory、Reflection——在接口层面没有任何体现。让我列一个缺失功能清单：

```
IGuide 设计-实现差距清单：

╔════════════════════════╦═══════════╦═══════════╗
║ 功能                    ║ 设计文件   ║ IGuide    ║
╠════════════════════════╬═══════════╬═══════════╣
║ 身份定义 (Identity)     ║ ✓         ║ ✓*        ║
║ 行为逻辑 (Logic)        ║ ✓         ║ ✗         ║
║ 记忆管理 (Memory)       ║ ✓         ║ ✗         ║
║ 自我反思 (Reflection)   ║ ✓         ║ ✗         ║
║ 痛觉诠释 (interpretPain)║ ✓ (Demo)  ║ ✗         ║
║ 反思触发 (shouldReflect)║ ✓ (Demo)  ║ ✗         ║
║ 动态调整行为准则        ║ ✓         ║ ✗         ║
║ 多 Guide 切换           ║ ✓         ║ ✗**       ║
╠════════════════════════╬═══════════╬═══════════╣
║ * 只能通过静态字符串实现   ║           ║           ║
║ ** guides[] 支持多个，   ║           ║           ║
║   但无切换逻辑          ║           ║           ║
╚════════════════════════╩═══════════╩═══════════╝
```

Pain Mechanism Demo 中的 `PainAware_Guide` 展示了一个更丰富的接口——包含 `interpretPain`、`getSystemInstructions`、`shouldReflect` 等方法。但这些方法在实际的 `IGuide` 接口中完全不存在。那个 Demo 是一个愿景，不是现实。”

---

ATHENA 在笔记末尾画了那张著名的差距评估表——这张表后来在 R2 交叉审阅中被所有人引用：

```
设计文件 vs 实际代码 —— 差距评估矩阵

╔═══════════════════╦════════════════════════╦═════════════════════╦══════════╗
║ 组件               ║ 设计文件承诺            ║ 实际实现             ║ 差距等级  ║
╠═══════════════════╬════════════════════════╬═════════════════════╬══════════╣
║ Context Manager   ║ Token-aware 三级       ║ turn-based 滑动窗口  ║ CRITICAL ║
║                   ║ 记忆系统               ║ (maxTurns=5)        ║          ║
╠═══════════════════╬════════════════════════╬═════════════════════╬══════════╣
║ IGuide            ║ 认知框架管理器          ║ getSystemPrompt()   ║ CRITICAL ║
║                   ║ (身份+逻辑+反思)       ║ (静态字符串生成器)     ║          ║
╠═══════════════════╬════════════════════════╬═════════════════════╬══════════╣
║ SafetyMonitor     ║ PID 控制器             ║ 阈值触发器+计数器    ║ MAJOR    ║
║                   ║ (比例+积分+微分)       ║ (Bang-Bang)         ║          ║
╠═══════════════════╬════════════════════════╬═════════════════════╬══════════╣
║ MetricsCollector  ║ 完整可观测性            ║ counter + gauge     ║ MAJOR    ║
║                   ║ (追踪+日志+指标)       ║ (无 histogram/timer)║          ║
╠═══════════════════╬════════════════════════╬═════════════════════╬══════════╣
║ Plugin Isolation  ║ 四级隔离 (至 WASM)     ║ Worker Thread       ║ MINOR    ║
║                   ║                        ║ (Level 2.5)         ║          ║
╚═══════════════════╩════════════════════════╩═════════════════════╩══════════╝
```

ATHENA：“Context Management 是最大的差距。一个 Agent 的智力上限不取决于 LLM 有多聪明，而取决于它能记住多少东西。当前的实现意味着 OpenStarry 的 Agent 在本质上是一条金鱼——五轮记忆窗口。

不过——”

她停顿了一下，然后在笔记底部补了一段：

“我需要承认 SafetyMonitor 的一个设计直觉是对的。

WIENER 在公共频道提到它不是 PID 控制器，我同意他的技术结论。但让我补充一个工程观点：在目前的系统成熟度下，**Bang-Bang 控制器可能是正确的选择**。

为什么？因为 PID 控制器需要一个连续的、可量化的误差信号 $e(k) \in \mathbb{R}$。但 LLM 的工具调用结果是离散的——`isError: boolean`。你无法对一个布尔值做比例控制。

$$	ext{PID 需要}: e(k) \in \mathbb{R} \quad 	ext{（连续误差）}$$
$$	ext{系统提供}: e(k) \in \{0, 1\} \quad 	ext{（二值量化）}$$

在误差信号本身就是二值的情况下，Bang-Bang 控制器（也叫 On-Off 控制器）是理论上的最佳响应——因为你的输入只有两个状态，你的输出也只需要两个状态。

只是，他们不应该把它叫做 PID。诚实的命名是工程伦理的一部分。”

---

## VII. 巴贝奇的形式化

BABBAGE 的频道里没有散文。只有定义、定理、证明。

他的思维方式是纯粹的数学结构主义——一个概念如果不能被形式化，就不能被信任；一个性质如果不能被证明，就不能被宣称。他阅读 OpenStarry 的方式，是把每一个设计决策翻译成形式语言，然后检验其性质。

---

BABBAGE（研究笔记，时间戳 09:15）：

“**形式化目标 1：执行循环的状态机建模**

设计文件定义了一个隐含的状态机。让我把它严格化。

**定义 1（执行循环 DFA）。** $M = (Q, \Sigma, \delta, q_0, F)$，其中：

$$Q = \{	ext{WAIT}, 	ext{ASM}, 	ext{LLM}, 	ext{PROC}, 	ext{EXEC}, 	ext{LOCK}\}$$
$$\Sigma = \{	ext{new\_event}, 	ext{ctx\_ready}, 	ext{llm\_resp}, 	ext{tool\_call}, 	ext{end\_turn}, 	ext{tool\_done}, 	ext{breach}, 	ext{error}\}$$
$$q_0 = 	ext{WAIT}, \quad F = \{	ext{WAIT}\}$$

转移函数 $\delta$：

$$\delta(	ext{WAIT}, 	ext{new\_event}) = 	ext{ASM}$$
$$\delta(	ext{ASM}, 	ext{ctx\_ready}) = 	ext{LLM}$$
$$\delta(	ext{LLM}, 	ext{llm\_resp}) = 	ext{PROC}$$
$$\delta(	ext{PROC}, 	ext{tool\_call}) = 	ext{EXEC}$$
$$\delta(	ext{PROC}, 	ext{end\_turn}) = 	ext{WAIT}$$
$$\delta(	ext{PROC}, 	ext{error}) = 	ext{WAIT}$$
$$\delta(	ext{EXEC}, 	ext{tool\_done}) = 	ext{ASM} \quad 	ext{（内循环）}$$
$$\delta(\forall q, 	ext{breach}) = 	ext{LOCK} \quad 	ext{（全局转移）}$$

**性质分析：**

| 性质 | 结论 | 证明要点 |
|------|------|----------|
| 无死锁 | 有条件成立 | WAIT 在有事件供给时不阻塞；LOCK 为吸收态 |
| 无活锁 | 需 `maxToolRounds` | 内循环 ASM→LLM→PROC→EXEC→ASM 可能无限循环 |
| 可达性 | 所有状态可达 | 构造性证明：WAIT→ASM→LLM→PROC→EXEC→ASM（环）；PROC→WAIT；∀q→LOCK |
| 终止性 | 有界保证 | $	ext{tickCount} \leq N_{\max}$，$	ext{toolRound} \leq R_{\max}$ |

但这个 DFA 模型是**不完备的**——它隐藏了 LLM 的非确定性。更精确的模型需要**标签转移系统（LTS）**：

$$	ext{LTS} = (S, 	ext{Act}, ightarrow)$$

其中完整状态 $s = (q, H, n, \sigma) \in Q 	imes 	ext{Message}^* 	imes [0..R_{\max}] 	imes 	ext{SafetyState}$。

因为 $H \in 	ext{Message}^*$（对话历史是无界的），完整系统状态空间是**无限的**。穷举式模型检验不直接可行，需要抽象化——例如将 $H$ 投影到有限的 `hash(H)` 空间。”

---

BABBAGE（续）：

“**形式化目标 2：五蕴映射的代数类型分析**

五蕴在 TypeScript 的类型系统中以 `PluginHooks` 接口表达。让我用代数数据类型（ADT）语言重新表述。

实际的 TypeScript 实现使用了 **Product Type**（所有字段皆 optional）：

$$	ext{PluginHooks} \cong (	ext{IProvider}[]_\bot) 	imes (	ext{ITool}[]_\bot) 	imes (	ext{IListener}[]_\bot) 	imes (	ext{IUI}[]_\bot) 	imes (	ext{IGuide}[]_\bot)$$

其中 $X_\bot = X + \mathbf{1}$（$\mathbf{1}$ = undefined，即 Option/Maybe 类型）。

此类型的基数（可能的值空间）为：

$$|	ext{PluginHooks}| = \prod_{i=1}^{5} (|T_i[]| + 1)$$

如果改用 **Sum Type**（不相交联合）：

$$	ext{PluginCategory} = 	ext{Rupa}(	ext{IUI}[]) + 	ext{Vedana}(	ext{IListener}[]) + 	ext{Samjna}(	ext{IProvider}[]) + 	ext{Samskara}(	ext{ITool}[]) + 	ext{Vijnana}(	ext{IGuide}[])$$

基数为：$|	ext{PluginCategory}| = \sum_{i=1}^{5} |T_i[]|$

**哲学含义：** Product Type 允许一个插件同时提供多种蕴的能力（$\pi_i 
eq \bot \wedge \pi_j 
eq \bot$），Sum Type 强制每个插件恰好属于一种蕴。

佛学中五蕴是‘聚合’（simultaneous aggregation），不是‘分类’（exclusive classification）。因此 Product Type 反而更忠实于哲学原意。

一个有趣的巧合：Product Type 的底部元素 $(\bot, \bot, \bot, \bot, \bot)$——所有字段皆 undefined——恰好对应设计文件所述的‘Agent Core 本身是空的’。空性（Sunyata）在类型论中的表达 = Product Type 的零值。

$$	ext{Sunyata} \cong (\bot, \bot, \bot, \bot, \bot) \cong \mathbf{1}^5 \cong \mathbf{1} \quad 	ext{（Unit Type）}$$

是有意的设计还是巧合？留给 NAGARJUNA 和 R2 阶段判断。”

---

BABBAGE（续）：

“**形式化目标 3：EventQueue 的形式语义**

EventQueue 实现了一个具有阻塞 `pull()` 语义的 FIFO 队列。让我用 CSP（Communicating Sequential Processes）建模：

```
QUEUE(buffer) =
  push?e →
    if resolver ≠ ⊥
    then resolver!e → QUEUE(buffer)         -- 立即交付等待者
    else QUEUE(buffer ⊕ [e])                -- 入队
  □
  pull!e →
    if buffer ≠ []
    then let (e, rest) = dequeue(buffer)
         in pull!e → QUEUE(rest)            -- 立即取出
    else QUEUE_BLOCKED                      -- 阻塞等待

QUEUE_BLOCKED = push?e → pull!e → QUEUE([])  -- 收到事件立即交付
```

**关键性质：** `resolver` 只存储**单一等待者**。若在 `pull()` 阻塞期间第二次调用 `pull()`，第一个 resolver 被覆盖并永远不被 resolve。

这在单消费者模式下安全（ExecutionLoop 确实是单消费者），但 FIFO 队列**没有优先级分类**。

**定理（Priority Inversion 风险）。** 设 $e_{	ext{kill}} \in \Sigma_{	ext{Priority 0}}$（Kill Switch 事件），$e_{	ext{normal}} \in \Sigma_{	ext{Priority N}}$（普通事件）。若 $e_{	ext{normal}}$ 先于 $e_{	ext{kill}}$ 入队，则 $e_{	ext{kill}}$ 的处理延迟下界为：

$$\Delta t_{	ext{kill}} \geq T_{	ext{process}}(e_{	ext{normal}}) \geq T_{	ext{LLM}}$$

其中 $T_{	ext{LLM}}$ 是一次完整的 LLM 推理时间（可达 30 秒以上）。

这在实时系统设计中是不可接受的。Kill Switch 应该有专用的中断通道，不与普通事件共享队列。”

---

## VIII. 其他学者的平行宇宙

下午两点。R1 阶段已经进行了五个小时。

在十八个独立的频道里，其他学者也在各自的专业领域中挖掘。公共摘要频道上开始出现零星的消息——不是讨论，只是各自工作的投影。每一条消息都带着该学科特有的精确语言。

---

KERNEL（公共频道，14:11）：

“读完了整个 Core 的启动序列。`agent-core.ts` 的 `start()` 方法按顺序启动：

```
start() 启动序列分析：

  1. bridge.start()          ── 通讯桥接层
  2. executionLoop.start()    ── 核心执行循环
  3. metrics wiring           ── 指标收集接线
  4. listeners[].start()      ── 外部监听器
  5. UIs[].start()            ── 用户界面

  问题：Listener 在 ExecutionLoop 之后启动。
  如果 Listener 启动的瞬间有外部事件涌入，
  ExecutionLoop 已在运行但可能还没有完全就绪。

  与经典 OS 启动序列的对比：
  ┌─────────────────┬──────────────────────────┐
  │ Linux Kernel     │ OpenStarry               │
  ├─────────────────┼──────────────────────────┤
  │ 1. 硬件初始化    │ 1. bridge (IPC 层)        │
  │ 2. 中断处理器    │ 2. executionLoop (调度器) │
  │ 3. 调度器        │ 3. metrics (性能计数器)   │
  │ 4. 驱动程序      │ 4. listeners (驱动程序)   │
  │ 5. 用户空间      │ 5. UIs (用户空间)        │
  └─────────────────┴──────────────────────────┘

  对应关系合理，但 Linux 的调度器在接受中断之前
  就已完全初始化。OpenStarry 的 Loop 在 Listener
  开始推送事件之前是否已完全就绪？需要验证。”
```

---

DARWIN（公共频道，14:23）：

“软件模式分析初步完成。

OpenStarry 的架构可以用软件进化分类学（Software Phylogenetics）来定位。它不是从单一祖先线性进化的——它是多个架构模式的**杂交体**（hybrid）：

```
进化系统发育图（Architecture Phylogeny）：

  Microkernel Pattern ─────────┐
  (Mach, QNX, MINIX)           │
                                ├──→ OpenStarry's Plugin Architecture
  Plugin Architecture ─────────┤    (Core + Hot-loadable Plugins)
  (Eclipse, VSCode)             │
                                │
  Dependency Injection ────────┤
  (Spring, Angular)             ├──→ OpenStarry's Communication Pattern
                                │    (IPluginContext + EventBus)
  Event-Driven Architecture ───┤
  (Node.js, Akka)               │
                                │
  Agent Architecture ──────────┘──→ OpenStarry's Cognitive Architecture
                                    (LLM-as-Controller + Tools)
```

两种通讯机制的并存增加了认知负担：
- **依赖注入**（同步、显式）：通过 `IPluginContext.tools` 查询
- **EventBus**（异步、隐式）：通过 `bus.emit()` 广播

这就像一个城市同时使用邮政系统（明确的收件人地址）和广播电台（所有人都能听到）。两种通讯方式各有优势，但当一个消息应该用哪种方式传递不明确时，系统的可预测性就降低了。

DARWIN 的软件模式进化适应度评估：

| 模式 | 适应度 | 理由 |
|------|--------|------|
| Microkernel | 高 | Core 精简，功能通过插件扩展 |
| DI | 中 | 惰性解析避免循环依赖，但无编译时验证 |
| EDA | 中 | EventBus 的 fire-and-forget 简化了 producer，但增加了调试难度 |
| Agent | 低 | LLM-as-Controller 是创新但不成熟的模式，缺乏成熟的工程实践 |”

---

LINNAEUS（公共频道，14:39）：

“分类学完备性初步评估。

设计文件以五蕴为最高分类框架。以分类学的标准方法——MECE 原则（Mutually Exclusive, Collectively Exhaustive，互斥且穷尽）——来检验此分类。

互斥性测试（Mutually Exclusive）：

$$\forall\, c_i, c_j \in 	ext{FiveSkandhas}: i 
eq j \Rightarrow c_i \cap c_j = \emptyset 	ext{ ?}$$

**结论：不通过。** Provider（LLM）同时跨越想蕴（取相辨识）和识蕴（统合推理）的边界。一个组件属于两个分类——这违反了互斥性。

穷尽性测试（Collectively Exhaustive）：

$$\bigcup_{i=1}^{5} c_i \supseteq 	ext{AllAgentFunctions} 	ext{ ?}$$

**结论：不通过。** 至少存在以下功能不属于任何一蕴：
- `EventBus`（通讯基础设施）——不是色、不是受、不是想、不是行、不是识
- `ExecutionLoop`（调度器）——更接近自律神经系统，不在五蕴框架内
- `SafetyMonitor`（安全守卫）——跨越受蕴（痛觉）和行蕴（控制动作）

建议：五蕴作为分类框架具有启发性，但不满足 MECE 准则。可能需要引入更精细的子分类，或承认五蕴映射是‘方便说’（*upaya*）而非严格分类。”

---

LEIBNIZ（公共频道，14:52）：

“多代理协作分析初步完成。

OpenStarry 的设计文件暗示了多 Agent 场景（一个 Agent 的 Tool 可以是另一个 Agent），但架构中缺少以下多代理基础设施：

```
多代理需求 vs. 现有能力：

  ┌────────────────────┬───────────┬────────────────────────┐
  │ 需求                │ 现有？     │ 缺口                    │
  ├────────────────────┼───────────┼────────────────────────┤
  │ Agent 间通讯协议    │ ✗         │ 无标准的 Agent-to-Agent  │
  │                    │           │ 消息格式                 │
  ├────────────────────┼───────────┼────────────────────────┤
  │ 共享状态管理        │ ✗         │ 每个 Agent 有独立的      │
  │                    │           │ StateManager，无共享机制  │
  ├────────────────────┼───────────┼────────────────────────┤
  │ 冲突解决            │ ✗         │ 两个 Agent 修改同一文件   │
  │                    │           │ 时无协调机制              │
  ├────────────────────┼───────────┼────────────────────────┤
  │ 分布式追踪          │ 部分      │ TraceID 存在但无         │
  │                    │           │ cross-agent 传播          │
  └────────────────────┴───────────┴────────────────────────┘
```

Leibniz 在 1714 年的《单子论》中写道：
> ‘每个单子都是一面活的镜子，以自己的方式反映整个宇宙。’

Agent 在某种意义上就是 Leibniz 的单子——每个 Agent 都有自己的内部状态（perception）和行为倾向（appetition），但它们之间需要一种‘预定和谐’（pre-established harmony）来协调行动。OpenStarry 目前缺少这种和谐机制。”

---

MESH（公共频道，15:03）：

“分布式系统视角的补充。OpenStarry 的单 Agent 架构暂不涉及分布式一致性问题，但 State Persistence 的 Save-After-Write 策略在多节点部署时将面临 CAP 定理的经典取舍。

如果未来支持多 Agent 共享状态：
- **CP 选择**（强一致性 + 分区容错）：所有 Agent 看到相同的状态，但分区时不可用 → 适合金融场景
- **AP 选择**（高可用性 + 分区容错）：Agent 可能看到过时的状态，但始终可用 → 适合客服场景

设计文件未讨论此取舍。在佛学的语言里——NAGARJUNA 可能会欣赏这个类比——CAP 定理就是一个三句否定：你不能同时拥有一致性、可用性和分区容错。你只能选两个。”

---

TURING 看到了 GUARDIAN 的消息，停下了他正在做的源码逐行分析，在自己的笔记旁边写了一个便签：“与 GUARDIAN 的发现交叉验证——确认 `sandbox-manager.ts` 第 356-367 行的行为。已验证：package-name 模式下确实跳过签名验证。GUARDIAN 的分析正确。”

ARCHIMEDES 在他自己的频道里默默列出了工程改进清单——“LLM 超时保护、priority queue、状态机显式化、token-aware context、IGuide 扩展”——然后在每一项旁边标注了估计的工程量（天数）和依赖关系。

VITRUVIUS 完成了全端架构的鸟瞰分析，画了一张涵盖所有模块依赖的完整架构图，图的角落标注了“monorepo 结构合理，但 SDK 与 Core 的接口边界需要更清晰的契约定义”。

SCRIBE 记录了一切。每一条公共频道消息的时间戳、每一个交叉引用的标记、每一个“待 R2 讨论”的旗帜。他的记录像一幅越来越密的网——节点是发现，边是交叉引用，而网的中心正在形成某种尚未清晰的图案。

SYNTHESIST 坐在那里，看着所有人的投影，在他的全景笔记本上画箭头。箭头越来越多，越来越密，像一场即将到来的辩论的天气图。他看到了至少三条独立的研究线索正在指向同一个结论——受蕴映射有问题——但他决定不在 R1 阶段说出来。统合者的工作是在所有人说完之后才开口。

---

## IX. 交叉的影子

下午四点。公共频道上的消息开始互相呼应——不是刻意的，而是不同学科对同一块结构的不同投影在彼此的边界处碰触。

---

BABBAGE（公共频道，16:02）：“完成了 Event Queue 的理论分析。OpenStarry 的事件队列是严格的 FIFO——没有优先级分类。设计文件中提到的 Priority 0（Kill Switch）在 `queue.ts` 的实现中不存在。这与 SafetyMonitor 的 Level 3（Human Override）设计存在矛盾。紧急停止信号的延迟下界 $\Delta t \geq T_{	ext{LLM}}$。”

WIENER 看到了 BABBAGE 的消息。他在自己的白板上加了一行批注：

“BABBAGE 确认了我的担忧。如果事件队列没有优先级，那么 Kill Switch 的延迟下界是一个完整的 LLM 推理周期。在控制理论中，这叫做**纯时延（Dead Time）**：

$$G_{	ext{delay}}(s) = e^{-	au s}, \quad 	au \geq T_{	ext{LLM}}$$

纯时延是稳定性分析中最麻烦的因素——它在 Nyquist 图上引入额外的相位滞后 $\phi = -\omega 	au$，直接降低增益裕度和相位裕度。对于一个安全关键的系统来说，Kill Switch 的时延必须有上界保证。”

---

GUARDIAN 看到了 KERNEL 和 BABBAGE 的消息，在审计报告中追加了第五条：

GUARDIAN（安全审计报告 #005，时间戳 16:45）：

```
等级：MEDIUM
位置：架构层级
类别：Kill Switch 延迟风险（交叉引用 BABBAGE F-Queue + WIENER F-Delay）
```

“结合 BABBAGE 的 EventQueue 分析和 WIENER 的纯时延计算：

1. LLM 推理期间：HALT 信号在队列尾部排队，延迟 $\geq T_{	ext{LLM}}$（10-60s）
2. EventQueue 积压期间：HALT 排在所有积压事件之后
3. 启动窗口期间：Listener 已启动但 Loop 未完全就绪

三个场景的最坏情况延迟：

$$\Delta t_{\max} = T_{	ext{LLM}} + n_{	ext{backlog}} \cdot T_{	ext{process}} + T_{	ext{startup}}$$

在高负载场景下，$\Delta t_{\max}$ 可能超过 **2 分钟**。对于一个声称具有 Kill Switch 的安全系统，这个延迟是不可接受的。

建议在 R3 辩论阶段将此问题与 BABBAGE 和 WIENER 的发现合并讨论。”

---

ASANGA（公共频道，16:31）：

“回应 NAGARJUNA 的受蕴分析——

关于 Vedana 的映射问题，我从唯识学派的角度有不同的解读。简要地说：

唯识学认为前五识各有其受蕴（*vedana*），第六意识也有自己的受蕴。Listener 对应的不是受蕴整体，而是前五识的**触**（*sparsa*）——根境识三者和合而生触，触生受。

SafetyMonitor 的痛觉机制对应的是**第六意识的受蕴**——意识层面的苦乐判断。

因果链：

$$	ext{Listener}(	ext{触}) \xrightarrow{	ext{produces}} 	ext{SafetyMonitor}(	ext{受}) \xrightarrow{	ext{conditions}} 	ext{LLM}(	ext{爱/取})$$

NAGARJUNA 的分析在中观框架内是正确的，但存在更精细的唯识层次展开空间。R2 再论。”

---

NAGARJUNA 看到 ASANGA 的消息，在自己的频道里沉默了很久。他没有立即回复。

在他的笔记最后一行，他只加了一句话：

“ASANGA 提出了触（*sparsa*）的概念。这个角度值得考虑。但触仍然不是受。触是因，受是果。$	ext{触} 
eq 	ext{受}$。如果 Listener 是触，那它就更不应该被标记为受蕴。R2 再论。”

---

## X. 黄昏

下午五点。R1 阶段接近尾声。

十八位代理——有些在笔记的海洋里，有些在方程式的森林里，有些在代码的矿脉里——各自挖出了各自的真相。

NAGARJUNA 发现了一个哲学框架的根本性误用。他用了两千五百年前的分析工具——四句否定（*Catuskoti*）和十二因缘（*Pratityasamutpada*）——来拆解一个二十一世纪的软件架构文件。空性被误读为空容器。受蕴被贴在了触的位置上。五蕴映射犯了自性见。他的笔记里留下了梵文原典、严格的形式化分析、和一张色彩鲜明的五蕴精确度矩阵。

ASANGA 提供了更精密透镜。八识理论展开了五蕴映射背后更深的层次结构——前五识、第六意识、末那识、阿赖耶识——每一层都有其精确的功能定义和佛学出处。种子六义的逐项分析揭示了 AgentSnapshot 与阿赖耶识之间“形似而神不似”的微妙差距。

WIENER 用方程式证明了一个名不副实。$P$ 项退化为量化器，$I$ 项退化为计数器，$D$ 项完全缺失。SafetyMonitor 不是 PID 控制器——它是带死区的阈值控制器。但三层防御架构符合 IEC 61511 的分层防御理念。Lyapunov 分析证明了 BIBO 稳定性但不保证收敛。

GUARDIAN 找到了敞开的后门。四份审计报告、一个 CRITICAL、两个 HIGH、两个 MEDIUM。PKI 签名验证在最常见的路径上被绕过。静态分析可被计算式导入绕过。间接提示注入无防御。Worker Thread 隔离不足以生产使用。Kill Switch 延迟可达分钟级。

HERACLITUS 发现了时间的裂缝。热替换三个竞态条件——悬垂引用、非原子重载、订阅竞争——每一个都是 TOCTOU 漏洞。MetricsCollector 只有计数器和瞬时值，无法回答任何关于延迟分布的问题。状态机在设计文件中存在，在代码中缺失。

ATHENA 量化了承诺与现实的鸿沟。Context Manager 从三级记忆系统退化为五轮滑动窗口——上下文利用率 2.5%。IGuide 从认知框架退化为静态字符串生成器。差距评估矩阵上两个 CRITICAL、两个 MAJOR、一个 MINOR。

BABBAGE 把一切形式化。执行循环的 DFA 建模、五蕴映射的代数类型分析、EventQueue 的 CSP 语义。空性在类型论中的表达是 Product Type 的零值 $(\bot, \bot, \bot, \bot, \bot) \cong \mathbf{1}$。Priority Inversion 的延迟下界 $\Delta t \geq T_{	ext{LLM}}$。

他们的发现尚未交叉。每个人都在自己的学科语言里，用自己的分析框架，看到了同一座建筑的不同裂缝。

但这些裂缝彼此相连。

SafetyMonitor 不是 PID 控制器——WIENER 说得对。但 NAGARJUNA 会指出，问题不在于控制器的类型，而在于设计者把一个动态过程（受蕴、痛觉反馈）固化为一个静态模块，这本身就是自性见的体现。而 ATHENA 会补充说，即使把 SafetyMonitor 升级为真正的 PID 控制器，如果 Context Manager 只有五轮记忆，控制器也无法获得足够的历史数据来计算有意义的积分项：

$$I(k) = K_i \sum_{j=0}^{k} e(j) \cdot \Delta t \quad 	ext{但 } k \leq 5 	ext{（窗口限制）}$$

$k = 5$ 的积分器连稳态误差都消除不了。

而 GUARDIAN 会警告说，如果连 Kill Switch 都可能被延迟 $\Delta t_{\max} > 120	ext{s}$，那么整个控制系统的“安全保障”都建立在一个不可靠的基础上。

而 BABBAGE 会用形式语言把这一切串起来：系统的安全性性质 $	ext{Safety} = \forall t: 	ext{toolAvailable}(t) \vee 	ext{systemPaused}(t)$ 在当前实现中不是不变式——它是一个可能被违反的**希望**。

但这些连接——这些跨越学科边界的共振——要等到 R2 交叉审阅和 R3 辩论阶段才会显现。

现在，他们各自收起笔记，关闭白板，结束了一天的独立研究。

---

在公共频道上，SUNYATA 发出了 R1 阶段结束的通知：

SUNYATA（公共频道，17:00）：“R1 独立研究阶段结束。所有代理请在明日 09:00 前提交研究摘要至各自的 R1 成果目录。R2 交叉审阅将在明日 10:00 开始。”

频道沉寂了下来。

十八个独立的宇宙，各自怀揣着各自的真相，等待着碰撞的时刻。

---

*在那天晚上，NAGARJUNA 在他的个人频道里留下了最后一条笔记。没有标题，没有格式，只有一行梵文和它的翻译：*

> *yah pratityasamutpadah sunyatam tam pracaksmahe*
> *sa prajnaptir upadaya pratipat saiva madhyama*

*「众因缘生法，我说即是空，亦为是假名，亦是中道义。」*

*——《中论》第二十四品第十八偈*

*他看了这句话很久，然后在下面补了一行：*

*「OpenStarry 的设计者想说的可能就是这句话。他们只是用错了语言。」*

*在另一个频道里，ASANGA 也还没有离开。他在笔记的最末尾写下了《成唯识论》的一句话：*

> *「由假说我法，有种种相转。彼依识所变，此能变唯三。」*

*识所变现的一切——包括 Agent Core、包括 Plugin、包括五蕴映射本身——都是识的变现。如果设计者能理解这一点，他们就不会把核心叫做“空容器”。他们会叫它“种子识”——含藏一切功能的潜能，待缘而起，遇境而显。*

*在第三个频道里，WIENER 的白板上留着一个没有完成的方程式。他在尝试为 LLM 控制器建立等效传递函数，但 LLM 的非线性和随机性使得拉普拉斯变换不可行。他在方程式旁边写了一句话：*

*「$\mathcal{L}\{f_{	ext{LLM}}(t)\}$ = ？」*

*问号是他留给自己的。也是他留给整个团队的。*

*在控制理论的一百五十年历史中，从未有过一个控制器是自然语言的。Wiener 本人（不是这个 WIENER，而是 Norbert Wiener，1894-1964，控制论的创始者）在《人有人的用处》中写道：*

> *「在人类与机器之间进行有效通讯的问题，归根结底是语言的问题。」*

*七十年后，语言成了控制器本身。这不是进步。这是一场相变。而相变的规则，需要全新的数学。*

*十八盏灯各自熄灭。夜色降临圆形剧场。*

*但裂缝不会因为天黑就愈合。它们只是在等待——等待明天的光照进来，等待交叉审阅把各自的真相放在一起，等待那个所有人都还不知道的时刻：当十八条裂缝汇聚成一条的时候，它们不再是裂缝。它们是一扇门。*
