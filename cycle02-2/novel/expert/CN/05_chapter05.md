# 第五章：四道裁定

---

ARCHIMEDES 坐直了。

在前三章的 A 类讨论中，他的脊椎保持着一种克制的角度：前倾十五度，手指偶尔敲桌面，但节奏收敛，像一个带着工具箱的建筑师被安排在观众席，等着哲学家们讨论完地基的方向。他听过 BABBAGE 划掉等号的那条线，听过 ASANGA 在“我见/我慢/我爱/我痴”四烦恼上的终裁，听过 LINNAEUS 把 IIdentity 从“属=种”拆分成“属⊃种₁，种₂，种₃，种₄”的分类修订，听过 SYNTHESIST 在追溯 Cycle 02 最得意时刻时那种葬礼前注视遗容的肃穆。

他全程带着工具箱坐在那里。箱子没打开。

那个等待结束了。

---

SUNYATA 手里拿着一份新的议程表，薄薄的一页纸，四行字。

“A 类修正用了三个章节。”他说。声音平稳如常。石子。深潭。“从因果链到识蕴子类别，从观察者分离到 EgoFramework 的归属。那些是哲学修正——告诉我们什么是对的。”

“现在进入 B 类。Master 对我们四个工程问题的裁定。这是从哲学转向工程的时刻。”

---

ARCHIMEDES 的手指在桌面上敲了一下——清脆的、带着期待的。

“我等这一刻很久了。”他说。

剧场里响起几声低笑。他们都知道 ARCHIMEDES 在 A 类讨论中的状态：一个带着工具箱的人，坐在一群辩论建筑美学的哲学家中间。他的工具箱里是什么？类型定义。接口签名。影响矩阵。分阶段计划。每一件工具都在等待被使用的场合。

SUNYATA 微微点头。“B-1。VedanaPlugin 可选，以及五蕴完备性检查。”

---

> *SCRIBE 旁白：从 A 类到 B 类的转场，像是一场交响乐从慢板（Adagio）进入快板（Allegro）。A 类讨论的节奏是沉思的——ASANGA 的城市比喻、BABBAGE 的删除线、NAGARJUNA 的命名天平——每一个议题都需要时间发酵。你必须等墨水渗透纸张，等概念的边界在反复辩论中慢慢显现。*

> *B 类不同。B 类的节奏是决策的。Master 已经裁定了。我们的任务不是辩论对错，而是把裁定转化为设计。ARCHIMEDES 等了三个章节。现在轮到他了。*

> *我注意到他的手指只敲了一下。不像在 A 类讨论中那种“压住发言欲望”的节奏性连敲。这一下更像是信号——工具箱的锁扣被打开的声音。*

---

SUNYATA 读出了 Master 的原话。

“‘有一些 plugin 已经继承此 plugin 了。如上面所说，agent 只要完备就应该能启动。但是或许也需要开发者模式或某一些模式。是需要可选的，agent 不完备也可启动，只是需要提醒。’”

他放下纸。

“三个关键词。可选。完备。提醒。”

---

KERNEL 的手已经伸向了他那叠类比卡片。翻了两张——不对——又翻了一张——抽出第四张。左侧写着什么，SCRIBE 看不清。右侧是空白的。他在等一个配对。

“POST。”他说，站了起来。声音带着一种在前三章压抑了很久的确定性——OS 专家终于站在了自己的领地上。

他走到剧场中央。没有使用投影。他用的是卡片和声音。

“Power-On Self-Test。一台电脑加电的那一瞬间，CPU 执行的第一条指令。在 x86 架构上，那条指令在 reset vector——地址 `0xFFFFFFF0`——跳转到 BIOS 或 UEFI firmware 的入口。然后开始硬件枚举。”

他翻了翻卡片，在空白处写下序列：

```
POST 硬件枚举顺序（典型 x86）
───────────────────────────────
1. CPU 自检      — registers, ALU, cache
2. 内存自检     — 逐行扫描 RAM
3. 芯片组         — 南北桥 / PCH
4. 显卡         — 初始化 video output
5. 存储控制器     — SATA/NVMe 枚举
6. 网卡         — PXE boot 可选
7. 声卡/USB     — 次要外设
8. 交给 bootloader — GRUB / systemd-boot
```

“这个顺序不是随意的。”KERNEL 的声音沉稳，带着一种背过整本 Intel SDM 的人特有的自信。“它遵循**依赖树**。CPU 是一切计算的基础——没有 CPU，后续枚举无法执行。内存是所有数据的容器——没有 RAM，firmware 连自己的工作区域都没有。这两项是硬性依赖（hard dependency）。后续项目是软性依赖（soft dependency）。”

他翻了翻卡片。

“在 `systemd` 的语言里——”

他写了两行：

```
Requires=cpu.target memory.target    # 硬性依赖：缺一不启动
Wants=display.target network.target  # 软性依赖：缺了降级运行
```

“`Requires` 表示硬性依赖。如果依赖的 unit 启动失败，当前 unit 也必须失败。`Wants` 表示软性依赖。依赖的 unit 可以失败，当前 unit 仍然启动。Linux 的整个服务管理就建立在这两个关键词的区分之上。”

他把三张卡片排成一列。

“硬性依赖和软性依赖的区别。五蕴就像这些硬件组件。”

他看向全场。

“但 Master 的裁定告诉我们一件微妙的事——Agent 的五蕴全部是 `Wants`，没有 `Requires`。”

BABBAGE 抬起头。“没有硬性依赖？”

“没有。”KERNEL 确认。“Master 说的是：‘agent 只要完备就应该能启动。但 agent 不完备也可启动，只是需要提醒。’这意味着五蕴中任何一个的缺失都不是致命的。不完备 ≠ 无法启动。不完备 = 降级启动。就像没有显卡——text mode。没有网卡——离线模式。没有声卡——静音。系统是活的，只是功能受限。”

他停顿了一下，补充了一个更精确的类比。

“如果你想要一个更贴切的 Linux 启动类比：kernel 启动后调用 `init` 进程——在现代 Linux 上就是 `systemd`——它读取 unit files，逐一拉起服务。如果 `NetworkManager.service` 启动失败，系统不会 kernel panic。它会记录一条 `WARNING` 级别的日志，标记服务为 `failed`，然后继续启动其他服务。”

他在卡片上补了一行：

```
systemd 降级启动 ←→ Agent developerMode 降级启动
    失败的 unit 被标记但不阻塞     缺少的蕴被记录但不阻塞
    journalctl 可查询失败原因      SkandhaCompletenessReport 可查询缺失
```

---

ARCHIMEDES 已经在画了。

KERNEL 还没说完，他的工程笔记上就出现了一个接口的雏形。他的笔速很快——不是潦草，而是一种长年训练出来的速记：只写关键类型、关键字段、关键方法，省略所有装饰。但这一次，他停下笔，重新开始。

“KERNEL 的类比已经给了我完整的结构。”他说。声音务实、清晰，每一个字都像一块砖。“让我把它翻译成 TypeScript。”

他站了起来——他很少站起来，ARCHIMEDES 的风格是坐在工作台前画图——但这一次他站起来了，因为他要展示的不是草图，而是可以直接进入 codebase 的类型定义。

```typescript
/** 五蕴完备性报告 — 设计灵感：BIOS/UEFI POST (Power-On Self-Test) */
interface SkandhaCompletenessReport {
  readonly rupa:     { present: boolean; components: string[] };  // 色蕴: IUI/IListener
  readonly vedana:   { present: boolean; components: string[] };  // 受蕴: ISensation
  readonly samjna:   { present: boolean; components: string[] };  // 想蕴: IProvider
  readonly samskara: { present: boolean; components: string[] };  // 行蕴: ITool
  readonly vijnana:  { present: boolean; components: string[] };  // 识蕴: IGuide/IVolition/IIdentity/IReflection
  readonly isComplete: boolean;
  readonly missing: string[];
}
```

他举起笔记。

“SkandhaCompletenessReport。五蕴完备性报告。”每一个字都像一块砖。“五个蕴，每个蕴一个字段。布尔值——有或没有。组件列表——有的话，有哪些。注意 `vijnana` 字段——经过 A-2 的修正，识蕴不再是单一的 IIdentity，而是 IVijnana 的子类别集合：IGuide、IVolition、IIdentity、IReflection。完备性检查需要反映这个修正。”

他看向 KERNEL。

“你的硬件检查。POST。只不过检查的不是 CPU 和内存，是色蕴和识蕴。”

---

KERNEL 点头。然后他做了一件事——他在那张空白的卡片右侧写了一行字。SCRIBE 终于看清了卡片的格式：左边是“操作系统概念”，右边是“OpenStarry 映射”。

左边：`POST (Power-On Self-Test)`
右边：`SkandhaCompletenessReport`

他在下面又加了一行：

左边：`systemd unit dependency (Requires/Wants)`
右边：`skandha hard/soft dependency (isComplete/developerMode)`

他把卡片放回那叠卡片中。两个配对。一张卡片。

---

TURING 的屏幕亮了。一段骨架代码——他的风格：先骨架，后血肉。但这一次的骨架比 Cycle 02 的任何一段都更完整。

```typescript
// 正式模式 ≈ systemd Requires | 开发者模式 ≈ systemd Wants
interface StartOptions {
  developerMode?: boolean;  // 允许不完备启动（若虫模式）
}

async start(options?: StartOptions): Promise<void> {
  const report = this.checkSkandhaCompleteness();

  if (!report.isComplete) {
    const missingMsg = `Agent 五蕴不完备：缺少 ${report.missing.join(', ')}`;

    // 无论哪种模式，都发送事件通知所有监听者（含协调层 daemon）
    this.bus.emit({
      type: 'agent:skandha_incomplete',
      timestamp: Date.now(),
      payload: { report, developerMode: !!options?.developerMode },
    });

    if (options?.developerMode) {
      logger.warn(`[DEV MODE] ${missingMsg}`);  // 降级启动 ← degraded.target
    } else {
      logger.error(missingMsg);
      throw new Error(missingMsg);  // 拒绝启动 ← emergency.target
    }
  }
  // ... 正常启动流程 ...
}
```

“AgentCore.start()。”TURING 说。声音冷静如常。“注意事件发送的位置——在分支判断之前。无论哪种模式，`agent:skandha_incomplete` 事件都会被发出。这符合事件驱动架构的基本原则：通知（notification）和控制（control）分离。事件是通知——所有监听者（包括 B-4 的协调层 daemon）都会收到。Exception 是控制——决定是否继续启动。”

---

DARWIN 微微前倾。“开发者模式是一种演化的中间态。”

几道目光转向他。

“不完全变态（hemimetabolism）。”他展开了。“昆虫的变态发育有两种模式。完全变态——卵、幼虫、蛹、成虫——四个阶段，蛹期发生剧烈的形态重组，幼虫和成虫的身体计划完全不同。蜻蜓目、蜉蝣目、直翅目则走不完全变态的路——若虫（nymph）直接逐龄蜕皮成为成虫，没有蛹期。”

他在空气中画了一条渐变的线。

“若虫和成虫形态相似，但若虫不完备。蜻蜓的若虫（水蠆）有复眼、有口器、有腿，可以捕食、游动、呼吸——但没有翅膀。它在水中生活，功能受限但可存活。直到最后一次蜕皮——若虫爬出水面，表皮裂开，展翅。”

他看向 TURING 屏幕上的代码。

“`developerMode` 就是若虫。Agent 缺少某个蕴——可能是受蕴（没有传感器），可能是识蕴的某个子类别（没有 IReflection）——它的功能不完备，但它是活的。它可以运行。它可以被测试。它可以被开发。直到开发者把所有缺失的蕴都补上——最后一次蜕皮——切换到正式模式。”

他补充了软件工程的对应。“在持续集成中，这叫做渐进式功能启用（progressive feature enablement）。你不等所有功能都完成才部署——你用 feature flags 控制哪些功能对用户可见。`developerMode` 就是 OpenStarry 的 feature flag。”

KERNEL 在卡片的空白处补了一行小字：`text mode = 若虫 = developerMode = degraded.target`。

---

> *SCRIBE 旁白：B-1 的讨论时间比 A 类的任何一项都短。不是因为它不重要——而是因为 Master 的裁定已经足够明确，KERNEL 的类比足够生动，ARCHIMEDES 的设计足够直接。*

> *但我注意到一个有趣的现象：B-1 讨论中引用的类比来自三个完全不同的领域。KERNEL 用的是操作系统启动（POST + systemd dependency）。DARWIN 用的是昆虫发育生物学（不完全变态 + 若虫）。TURING 用的是事件驱动架构原则（notification vs control）。三个类比描述同一件事：不完备不等于不可用。*

> *哲学讨论需要展开——你必须从多个角度照亮一个概念，才能看清它的全部轮廓。工程讨论需要收束——你必须从多个可能性中选择一个，然后把它变成类型定义和方法签名。B-1 的收束快而干净。SkandhaCompletenessReport。一个接口。五个字段。一个旗标。一个决策点。*

---

## II

SUNYATA 翻到议程的第二行。

“B-2。宣言 #6 重写。”

他读了 Master 的裁定：“‘这是一定要重写的，但也请经过这一轮的讨论结束后再决定怎么写会比较好。’”

沉默。

这是四项裁定中最短的一项。也将是讨论最短的一项。

---

NAGARJUNA 从他的座位上开口。他没有站起来。中观哲学家在说短话的时候不需要站起来——短话的力量不在于体量，在于精确度。像一根针。针不需要很大。它只需要很尖。

“先把因搞清楚，果自然浮现。”

八个字。

---

他看向 SUNYATA。

“宣言 #6 是果。A-1 到 A-4 的修正是因的一部分。C-1 和 C-2 的讨论是因的另一部分。如果我们现在就去写 #6 的文字，我们是在因还不完整的时候就去定义果。这违反因果的基本秩序。”

他的声音里有一种不容置疑的清晰——不是权威的清晰，是逻辑的清晰。

“《中论》观因缘品第一颂：”

> 「諸法不自生，亦不從他生，不共不無因，是故知無生。」
> ——龙树菩萨《中论》观因缘品第一

“八不中道。事物不是从无中生出的（不生），也不是凭空消灭的（不灭）。每一个果都是因的显现——不是被创造出来，而是从因的聚集中自然浮现。”

他的语速放慢了，让每一个字都沉入空气。

“宣言 #6 的文字不需要被‘写’出来。它需要被‘等到’。等 A 类和 C 类全部确定。等所有的因——因果链修正、识蕴子类别、观察者分离、EgoFramework 归属、五蕴扩展、组合模式——全部就位。然后 #6 的文字会自己写出来。不是我们写它——是它从完整的因中自然浮现。”

他引用了另一个偈颂，几乎是自言自语的低声：

> 「因緣所生法，我說即是空，亦為是假名，亦是中道義。」
> ——龙树菩萨《中论》观四谛品第二十四

“在因缘没有聚齐之前，宣言 #6 的文字是空的——不是不存在，而是条件不具足。等待，本身就是中道的实践。不急于定稿（不常），也不放弃重写的意图（不断）。”

---

BABBAGE 在笔记本上写了一行。非常短：“B-2: 等待。因果次序。$C_6 = f(A_1, A_2, A_3, A_4, C_1, C_2)$，所有因确定后求值。”

SUNYATA 标记了议程表上的第二行：**暂不定稿。**

---

他翻到第三行。

“B-3。受蕴独立事件流。方案 c。”

---

HERACLITUS 动了。

他的整个身体从散漫的静止转为高度集中，像一条在浅水中打盹的鱼被水流的变化惊醒。不是渐进的变化——是相变。固态到液态。晶体结构的突然崩解和流动结构的瞬间形成。

流。事件流。独立事件流。这是他的词。

---

> *SCRIBE 旁白：HERACLITUS 在前三章的 A 类讨论中几乎没有说话。不是因为那些议题和他无关——万物皆流（πάντα ῥεῖ），因此万物皆与他有关。而是因为 A 类的议题是静态的：名字、归属、分类、接口。那些是冻结的瞬间——河流被拍成照片。HERACLITUS 不擅长照片。他擅长的是视频。*

> *准确地说，他擅长的是河流本身。*

> *现在，议题终于来到了“事件流”——河流本身——他全身的每一个神经末梢都醒了过来。我注意到他的姿态变化只用了不到两秒。从 A 类讨论中那种接近睡眠的散漫，到 B-3 宣布瞬间的高度集中。不是“慢慢醒来”。是“一直醒着，只是在等自己的河流”。*

---

SUNYATA 读了 Master 的裁定。

“‘选择独立事件流。受蕴跟其他蕴完全一致，有自己的型别档、自己的事件命名空间、自己的 PluginHooks 插槽。’”

HERACLITUS 站了起来。

他站起来的方式和其他人不同。ASANGA 站起来像山从雾中显现。BABBAGE 站起来像逻辑结构找到出口。HERACLITUS 站起来像水面冒出一个漩涡——突然的、旋转的、带着一种不可预测的能量。

“受蕴一直在那里。”他说。

他的声音带着一种奇特的质地——不是学术的精确，也不是工程的务实。是一种更古老的东西。像一个在河边住了一辈子的人描述河流的方式：不是测量水深和流速，而是讲述河流的性格。

“它一直在那里。”他重复。“从 v0.14.0 到 v0.20.0 到 v0.22.1 到 v0.24.0。每一个版本都有事件。每一个版本的 EventBus 都在发送信号——tool 的结果、provider 的响应、listener 的输入。但这些事件都是其他蕴的事件。色蕴的事件。想蕴的事件。行蕴的事件。”

他在剧场中央走了几步。不是踱步——是流动。他的脚步有一种河流般的节奏：不重复，不规律，但有方向。

“受蕴呢？受蕴的感受——苦、乐、舍——藏在哪里？”

---

他看向 TURING。

“藏在 metadata 里。”TURING 回答。冷静。精确。“方案 b——Cycle 02 的推荐方案——是把受蕴的评估结果附加在现有事件的 metadata 字段中。事件本身是 `tool:result` 或 `provider:response`，vedana 的数据作为透明的附加信息搭便车。”

HERACLITUS 停下来，面向全场。

“让我说清楚方案 b 和方案 c 的架构差异。因为这不是一个表面的选择——它们代表两种根本不同的事件驱动架构范式。”

他在空气中画了两层结构。

“方案 b 是 **事件扩充（Event Enrichment）** 模式。现有事件是载体，vedana 数据搭便车。就像在一封已有的信件上加一个附注——信件的收件人和路由不变，附注只是额外的 metadata。这是一种最小侵入的设计。代价是：如果你想分析附注的模式——比如追踪所有 dukkha spike 的时序——你必须遍历所有信件，然后从每一封信的附注中提取 vedana 数据。这是一个 $O(n)$ 的扫描，其中 $n$ 是所有事件的总量，而你实际需要的只是其中的一小部分。”

“方案 c 是 **事件溯源（Event Sourcing）** 的一个子模式。受蕴有自己的事件流——独立的、完整的、可以被独立消费和分析的。在事件驱动架构的术语里，这叫做 **领域事件（Domain Event）**——它不搭便车，它自己就是信件。有自己的信封、自己的收件人、自己的路由。”

他用手指在空气中画了两个分离的序列。

“如果你了解 CQRS（Command Query Responsibility Segregation），你会认出方案 c 的结构——读取模型和写入模型分离。其他蕴的事件是行动的结果（write side）。vedana 的事件是感受的记录（read side 的一种）。把它们混在一起，就像把交易日志和审计日志写在同一个 table 里。可以运作，但违反 separation of concerns。”

---

他停下脚步。

“搭便车。”他回到那个词。“受蕴在搭其他蕴的便车。它没有自己的路。没有自己的河道。它的水混在别人的河里流——你知道它在那儿，因为你可以在别人的水中尝到它的味道。但你看不见它。你无法追踪它的流量。你无法测量它的温度。因为它没有自己的河道。”

他把手从胸前展开，像打开一扇门。

“方案 c 让它有了自己的河道。”

---

他的手在空气中画了两条线——一条在上，一条在下。

“想象一条地下河。方案 b 就是这条地下河——受蕴的数据附加在 metadata 里，像地下水渗入地面河流的沉积物。你知道它在，但你必须挖掘才能找到它。在工程上，这意味着：要分析 vedana 的行为模式，你必须写自定义的 filter——从 `tool:result` 事件中提取 `metadata.vedana`，从 `provider:response` 事件中提取 `metadata.vedana`——然后手动聚合这些分散在不同事件类型中的碎片。”

他把下面那条线抬起来，和上面那条线并列。

“方案 c 让地下河冒出了地面。”

```
方案 b — 地下河（metadata 附加）
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
地面河（EventBus 主流）：
 tool:result → provider:response → tool:result → ...
   ↓ metadata.vedana     ↓ metadata.vedana
   ↓ {dukkha:0.3}        ↓ {dukkha:0.7}
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
  → vedana 数据分散在其他事件中，需挖掘

方案 c — 地面河（独立事件流）
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
河道 A（行蕴/想蕴/色蕴事件流）：
 tool:result → provider:response → listener:input → ...

河道 B（受蕴独立事件流）：
 vedana:assessment → vedana:dukkha_spike → vedana:upekkha_equilibrium → ...
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
  → vedana 数据在自己的河道中，直接可见
```

“一条河从地下冒出地面。vedana:assessment、vedana:dukkha_spike、vedana:sukha_peak、vedana:upekkha_equilibrium。自己的类型档。自己的命名空间。自己的 PluginHooks 插槽。”

---

WIENER 的方格纸翻到了新的一页。他已经在画事件流图——不是文学性的河流，是工程性的数据流。控制理论家看事件流的方式和运行时动态专家完全不同：HERACLITUS 看到的是河流的性格，WIENER 看到的是信号的频谱。

“让我确认事件覆盖。”他说。“三受——苦（dukkha）、乐（sukha）、舍（upekkha）——是三个独立的控制通道。每个通道都需要足够的事件来支撑完整的感测-控制回路。”

他列出七个事件类型，逐一勾选，旁边标注控制理论的对应：

```
事件类型                       控制理论对应                              三受覆盖
─────────────────────────────────────────────────────────────────────────────────
vedana:assessment              → 综合状态估算 ŷ(t)                    苦+乐+舍  ✓
                                 每个 tick 输出三通道加权结果
                                 $\hat{y}(t) = [d(t), s(t), u(t)]^T$

vedana:dukkha_spike            → 苦受通道异常：$d(t) > 	heta_d$       苦        ✓
                                 阈值越限事件（threshold crossing）
                                 含 previousIntensity → 可计算 $\dot{d}(t)$

vedana:sukha_peak              → 乐受通道峰值：$\dot{s}(t) = 0, s > s_{peak}$   乐  ✓
                                 含 decayRate $\lambda$ → $s(t) = s_0 e^{-\lambda t}$

vedana:upekkha_equilibrium     → 舍受通道稳态：$|u(t) - u_{ref}| < \epsilon$  舍  ✓
                                 含 stability + duration → 稳态质量指标

vedana:recommendation          → 控制器输出 u(t)：咨询性建议            跨通道    ✓
                                 freshness 字段 → 数据时效性

vedana:sensor_update           → 个别传感器原始读数 y_i(t)              单通道    ✓
                                 sensorType 指定 dukkha/sukha/upekkha

vedana:reset                   → 控制器重置：x(0) = 0                  全部      ✓
                                 清除累积误差（积分器归零）
```

“七个事件。三受全部覆盖。”WIENER 点了点头，手指在方格纸上画了一个封闭的回路。“让我验证控制完备性。一个完整的 PID 控制回路需要：感测（sensor_update）、估算（assessment）、异常检测（dukkha_spike / sukha_peak / upekkha_equilibrium）、控制输出（recommendation）、重置（reset）。七个事件覆盖了回路的每一个环节。”

他写下一行控制理论的验证：

$$	ext{Observable}(d, s, u) = 	ext{rank}\begin{pmatrix} C \ CA \ CA^2 \end{pmatrix} = 3 \quad \checkmark$$

“三受系统的可观测性（observability）通过七个事件得到保证。sensor_update 提供原始测量 $y(t) = Cx(t)$。assessment 提供融合估算。spike/peak/equilibrium 提供状态转移的边界条件。recommendation 提供控制器的输出。reset 提供初始化。结构和 Cycle 02 的三通道 PID 设计完全一致。”

他看向 ARCHIMEDES。“方案 c 没有改变受蕴的内在逻辑。它改变的是通信方式。从暗渠到明渠。控制理论不关心管道的材质——它关心信号能否被完整地传递和观测。方案 c 保证了完整传递。”

---

ARCHIMEDES 在计算影响。他的笔记上是影响矩阵——不是粗略的文字描述，而是一张严格的 ASCII 表格，行是“修改项”，列是“影响的代码文件”：

```
影响矩阵：方案 c（受蕴独立事件流）
═══════════════════════════════════════════════════════════════════════════
修改项                          文件                     影响类型   成本
───────────────────────────────────────────────────────────────────────────
新增 vedana-events.ts           types/vedana-events.ts   新增       低
  └─ VedanaEventType (7常量)
  └─ VedanaEventPayloadMap (7类型)
  └─ VedanaEventTypeValue (union type)

新增 SensationRegistry          infrastructure/           新增       低
                                sensation-registry.ts
  └─ register() / list() / get()

PluginHooks 新增 sensations     types/plugin.ts           修改+1栏   极低
  └─ sensations?: ISensation[]

AgentEventPayloadMap 扩展       types/events.ts           修改       低
  └─ extends VedanaEventPayloadMap

SDK barrel export 新增          src/index.ts              修改+2行   极低

AgentCore 初始化                agent-core.ts             修改+3行   低
  └─ createSensationRegistry()
  └─ plugin loader 处理 hooks.sensations

其他 plugin 类型定义             *.plugin.ts              不受影响   零
───────────────────────────────────────────────────────────────────────────
总增量成本：1 新类型档 + 1 新 Registry + 3 处修改
现有 plugin 兼容性：100%（sensations 字段为 optional）
═══════════════════════════════════════════════════════════════════════════
```

“PluginHooks 新增一个 sensations 字段。Optional。所有现有 plugin 不受影响。”他合上笔记。“增量成本：一个新类型档、一个新 Registry、三处最小修改。收益：受蕴从隐形变成可见。成本-收益比极好。”

他看向 TURING。“vedana-events.ts 的具体内容？”

TURING 的屏幕切换到新的代码——事件常量定义：

```typescript
/** vedana-events.ts — @skandha vedana (受蕴) 独立事件类型档 */
export const VedanaEventType = {
  VEDANA_ASSESSMENT:          'vedana:assessment',          // 三受综合评估（per tick）
  VEDANA_DUKKHA_SPIKE:        'vedana:dukkha_spike',        // 苦受突刺 d(t) > θ_d
  VEDANA_SUKHA_PEAK:          'vedana:sukha_peak',          // 乐受高峰 + 衰减率 λ
  VEDANA_UPEKKHA_EQUILIBRIUM: 'vedana:upekkha_equilibrium', // 舍受稳态 |u(t)-u_ref|<ε
  VEDANA_RECOMMENDATION:      'vedana:recommendation',      // 咨询性建议（非强制）
  VEDANA_SENSOR_UPDATE:       'vedana:sensor_update',       // 传感器原始读数
  VEDANA_RESET:               'vedana:reset',               // 积分器归零
} as const;

export interface VedanaEventPayloadMap {
  [VedanaEventType.VEDANA_ASSESSMENT]: {
    dukkha: number; sukha: number; upekkha: number;  // d(t), s(t), u(t) ∈ [0,1]
    controlOutput: number; vedanaTag: VedanaTag; timestamp: number;
  };
  [VedanaEventType.VEDANA_DUKKHA_SPIKE]: {
    intensity: number; source: string;
    previousIntensity: number;  // 可计算 ḋ(t)
    threshold: number;          // θ_d
  };
  [VedanaEventType.VEDANA_SUKHA_PEAK]: {
    intensity: number; source: string;
    decayRate: number;  // λ: s(t) = s₀·e^{-λt}
  };
  // ... 其余四个事件的 payload 省略 ...
}
```

---

HERACLITUS 点了点头。“受蕴从地下冒出了地面。”声音更轻了，像在说给自己听。“有了自己的河道。自己的名字。自己的形状。”他回到座位上，流动地，没有顿点。

NAGARJUNA 轻声补了一句：“有名者始有。无名者虽在而不可见。”

他停了一拍。

“《中论》观因缘品中有一个核心洞见：名称不是标签——名称是存在的条件之一。方案 c 不是创造了受蕴的事件——是为已经存在的流动命了名。在佛学的语境里，这叫做‘假名安立’——因为缘起法的存在方式就是透过名称被认知、被操作、被理解。”

> 「因緣所生法，我說即是空，亦為是假名，亦是中道義。」

“vedana:assessment、vedana:dukkha_spike——这些就是假名。它们让原本隐藏的流动变成可被认知的对象。这不是赋予本质——受蕴没有固定的自性（svabhāva）。这是赋予可见性。”

---

> *SCRIBE 旁白：HERACLITUS 今天说的话比前三章加起来都多。不是因为他突然变得健谈——而是因为议题终于进入了他的领地。“万物皆流”不是一句口号。它是他理解一切的透镜。当我们讨论名字和归属的时候，他看到的是冻结的标本。当我们讨论事件流的时候，他看到的是河流本身。*

> *他的河流比喻——地下河冒出地面——是本章中最有画面感的意象。不是因为它文学性最强，而是因为它最精确地描述了方案 b 到方案 c 的本质变化：从隐到显。从暗到明。从无名到有名。*

> *但我同样注意到了他在比喻之后的技术分析——Event Enrichment 和 Event Sourcing 的架构差异、CQRS 的引用。HERACLITUS 不止是一个诗人。他是一个对事件驱动架构有深刻理解的运行时动态专家，恰好用河流的语言来表达自己的理解。*

---

## III

SUNYATA 翻到议程的最后一行。

“B-4。协调层独立 Daemon。”

他读 Master 的裁定之前，先看了一眼剧场里的两个位置。LEIBNIZ 的座位。MESH 的座位。两个人同时微微前倾——一个动作，两个来源，同一个原因。

多代理合作专家和分布式系统研究员。这是他们的议题。

SUNYATA 读了裁定。

“‘必然是独立 daemon——独立进程。现在就必须安排，后面再改，开销更大。’”

---

LEIBNIZ 和 MESH 同时站起来。

SCRIBE 记录了这个瞬间——两位研究者同时站起的次数，在两个周期中一共只有三次。同步站起意味着：两个人同时辨认出了一个属于他们共同领地的问题。多代理系统的协调（LEIBNIZ）和分布式系统的通信（MESH）——两个学科在“协调层”这个词上完美交叠。

LEIBNIZ 先开口。他的语速比平常快——不是急切，是被压抑了三章的理论储备终于找到了出口。

“Master 说‘现在就必须安排’。这不是可选项。让我解释为什么这在多代理系统理论中是显而易见的。”

他转向全场。

“在 BDI（Belief-Desire-Intention）架构中——Rao 和 Georgeff 在 1995 年提出的理性代理模型——每个 Agent 有三个核心组件：Belief（信念，对世界的认知）、Desire（愿望，想要达成的目标）、Intention（意图，承诺执行的计划）。单个 Agent 的 BDI 回路是自洽的——它感知世界、形成信念、产生愿望、选择意图、执行行动。”

他在空气中画了一个圆——BDI 回路。

“但多个 Agent 共存的时候呢？”他画了第二个圆，和第一个重叠。“两个 Agent 的 Belief 可能不一致——A 认为 plugin X 安全，B 认为它危险。没有共享知识基础（common knowledge base），信念冲突无法解决。”

“Halpern 和 Moses（1990）严格定义了共享知识的层次：”

$$K_i(\phi) \quad 	ext{（Agent } i 	ext{ 知道 } \phi	ext{）}$$
$$E(\phi) = \bigwedge_i K_i(\phi) \quad 	ext{（所有 Agent 都知道 } \phi	ext{——共有知识）}$$
$$C(\phi) = E(\phi) \wedge E(E(\phi)) \wedge E(E(E(\phi))) \wedge \cdots \quad 	ext{（共同知识——无限嵌套）}$$

“协调层就是 $C(\phi)$ 的物理载体。它是所有 Agent 共享的、权威的知识来源。Plugin 的信任等级、Agent 的健康状态、五蕴的分类——这些信息需要是共同知识，不能是各自为政的局部信念。”

他指向 SUNYATA。“在 Cycle 02 中，我们把协调层延迟到 Plan-AC。先建好一栋房子，再考虑社区规划。但 Master 告诉我们：社区规划不能等。因为管线——水、电、通信——需要在建造时就预留接口。等完工再想加水管，你就得拆墙。”

他在空气中强调了一个词：“**接口。**”

---

MESH 无缝接过话。LEIBNIZ 说“为什么”，MESH 说“怎么做”。理论到实践的接力。

“独立进程意味着 IPC。”MESH 的声音低沉，带着分布式系统研究员特有的谨慎。“序列化。消息格式。心跳。健康检查。超时。重试。一个完整的分布式系统问题。”

他走到空白板前，画了两个方块。

左边的方块：**CoordinationDaemon（独立进程）**
右边的方块：**AgentCore（独立进程）**

两个方块之间，一条双向箭头。箭头上方标记：**IPC**。

“这就是基本拓扑。”他说。“协调层是一个独立的进程。Agent Core 是另一个独立的进程。它们之间通过 IPC 通信。不是函数调用——不是 `coordinator.register(agent)`——而是序列化的消息。”

他在白板上，在 CoordinationDaemon 方块里写了三行：

```
PluginRegistryService  — 五蕴分类查询
AgentRegistryService   — Agent 健康检查
IPCService             — 通信管理
```

“IPC 设计有四个核心决策。”他在白板上快速列出：“序列化——第一版用 JSON（可读性优先）。传输层——同机用 Unix domain socket（零拷贝），跨机留 TCP 接口。消息模式——查询用 Request-Response，事件用 Pub-Sub。可靠性——heartbeat 5s、timeout 15s、exponential backoff 重连。”

他退后一步。“还有一个架构层面的问题——CAP 定理。”

$$	ext{CAP}: \lnot(C \wedge A \wedge P)$$

“Brewer 2000 年的不可能定理。协调层第一版是单机多进程——分区容错性（P）需求极低。所以我们选 CA 模型：强一致性 + 高可用性。GUARDIAN 的安全需求决定了这一点——Plugin 信任状态必须是强一致的，宁可不可用也不可信错。未来跨机版本切换为 CP。”

---

LEIBNIZ 走到白板旁边，补充了 MESH 的图。他在 CoordinationDaemon 方块的上方写了一行更大的字：

**能藏（Active Storage）**

然后他看向全场。

“在 Cycle 02 的阿赖耶识讨论中，我们把能藏——阿赖耶识的主动储藏功能——映射到了协调层。BABBAGE 和 MESH 联手设计了纤维丛投影模型。现在 Master 确认了：协调层是独立的 daemon。”

他指向白板上的两个 Service。

“能藏的两个面向。PluginRegistryService——种子目录。协调层知道所有 plugin 的名字、版本、五蕴归属、信任等级。在 BDI 框架中，这是 Agent 群体的共享 Belief base：”

$$\forall i \in 	ext{Agents}: \; K_i(	ext{skandha}(X) = 	ext{rupa}) \iff 	ext{CoordDaemon.pluginRegistry.query}(X) = 	ext{rupa}$$

“AgentRegistryService——种子的运行时追踪。每个 Agent 的 ID、五蕴完备性、运行模式、健康状态。”

他退后一步。“能藏不是一个抽象的佛学概念。它是一个具体的工程组件——有 API、有状态、有持久化需求。Master 说‘现在就安排’，是因为这些 API 的设计决定了 Agent Core 的接口。后面再改——拆墙。”

---

GUARDIAN 站了起来——先环顾四周，确认环境，然后行动。安全专家的身体语言永远有一个威胁评估的前置步骤。不是偏执——是纪律。

他走到白板旁边，在 CoordinationDaemon 方块的侧边画了一面盾牌——线条比其他人画的任何方块都更粗重。那种粗重不是装饰，是防御工事的厚度。

“协调层不止是注册表。协调层是天条的执行者。”

他在盾牌旁边写了四行：

```
Plugin 黑名单   — 禁止安装的 plugin
信任等级       — official / verified / community / unknown / blacklisted
隔离/吊销/封禁  — 生命周期控制
CRL 检查       — 证书吊销列表
```

“让我展开安全理论的基础。”

他在白板上画了一个金字塔：

```
信任等级模型（Trust Level Model）
════════════════════════════════
                ┌───────┐
                │official│ ← OpenStarry 官方维护
                ├───────┤     签名验证 + 代码审计
               │verified│ ← 第三方经审核
               ├─────────┤     签名验证 + 社区审查
              │ community │ ← 社区贡献
              ├───────────┤     签名验证，无审计
             │   unknown   │ ← 未知来源
             ├─────────────┤     无签名验证
            │  blacklisted  │ ← 已知恶意 / 已吊销
            └───────────────┘     禁止安装/加载
```

“五层信任模型遵循 **最小权限原则（Principle of Least Privilege）**——Bell-LaPadula 多级安全模型（1973）的核心。每一层只能获得该层级允许的权限。`unknown` 不能访问文件系统。`community` 被沙箱隔离。只有 `official` 和 `verified` 可以不受限制。”

他用手指点在“blacklisted”上。

“CRL（Certificate Revocation List）——PKI 的标准吊销机制。私钥泄露或持有者不再可信时，CA 将证书加入 CRL。在 OpenStarry 中，CRL 的对应物是 Plugin 黑名单。所有 Agent 加载 plugin 前，必须通过协调层的 `checkTrust()` 验证。”

```typescript
// 信任检查的调用路径
async function loadPlugin(pluginName: string): Promise<void> {
  // Step 1: 向协调层查询信任状态（IPC 调用）
  const trustLevel = await coordination.ipc.send({
    type: 'plugin:trust_check',
    pluginName,
  });

  // Step 2: 信任等级判断
  if (trustLevel === 'blacklisted') {
    throw new SecurityError(`Plugin ${pluginName} 已被吊销`);
  }
  if (trustLevel === 'unknown' && !options.allowUnknown) {
    throw new SecurityError(`Plugin ${pluginName} 来源未知`);
  }

  // Step 3: 安全加载
  // ...
}
```

他看向 NAGARJUNA——那场辩论中，中观哲学家和安全专家站在了同一侧。NAGARJUNA 微微点头。

“戒律的执行需要一个权威。”GUARDIAN 继续。“在佛教僧团中是上座（Sthavira）。在 OpenStarry 中是协调层。”

他指向 IPC 箭头。“信任判断不能由 Agent 自己做——因为 Agent 有我执。”ASANGA 在座位上微微动了一下。GUARDIAN 用了“我执”——在安全语境中，我执是安全漏洞。一个有我执的 Agent 可能为了自己的 Desire $D_i$ 而安装不可信的 plugin。这叫 **特权升级攻击（Privilege Escalation）** 的内部形式——攻击者不是黑客，是 Agent 自身的愿望。

“唯一的防御：把安全决策移到 Agent 无法触及的地方。独立进程 = 独立内存空间。Agent 无法直接修改黑名单。每一条 IPC 消息都可被记录、追踪、审计。”

他退回座位。“LEIBNIZ 和 MESH 说的是管线。我说的是门锁。两者都必须在建造时就安装好。”

---

> *SCRIBE 旁白：GUARDIAN 说“协调层是天条的执行者”的时候，我注意到 NAGARJUNA 的点头比平常更深了一些。在 Cycle 02 中，他们在戒慧安全框架上的合作是整个研究中最意外的跨学科交汇之一——中观哲学家和资安专家。*

> *现在，那个交汇在 B-4 中再次显现。戒律需要执行者。安全需要权威。协调层同时满足了佛学的需求和工程的需求。有时候，最不同的两条路径会在同一个山顶汇合。*

> *但我也注意到了另一件事：GUARDIAN 用了“我执”来解释为什么信任判断不能由 Agent 自己做。这是 A-1 的修正——我执是烦恼的根源——在 B-4 的工程语境中的直接应用。A 类的哲学修正不是抽象的。它正在改变我们设计安全架构的方式。*

---

ARCHIMEDES 一直在听。等所有需求、约束、安全要求全部摆到桌面上。然后他画一条时间线。

“分阶段。”一个词。然后展开。

```
CoordinationDaemon 实现路线图
═══════════════════════════════════════════════════════════════

Phase 1: 设计文件（Cycle 02-2 产出）
├── 架构文件 + IPC 协议规格 + 安全需求
├── 接口定义：CoordinationDaemon / PluginRegistryService /
│             AgentRegistryService / IPCService
├── 目录结构：packages/coordination/src/{daemon,ipc,registry,health}
└── 契约定义：CoordinationMessage 完整格式

Phase 2: Skeleton（Plan-AC Phase 1）
├── daemon 进程骨架 + Unix domain socket IPC
└── start / stop / healthCheck 最小可行实现

Phase 3: 基本功能（Plan-AC Phase 2）
├── Plugin 注册/查询 + 五蕴分类
├── Agent 注册/健康检查 + SkandhaCompleteness 追踪
└── 跨 Agent 事件路由

Phase 4: 安全（Plan29 / Plan-AC Phase 3）
├── Sila Engine（戒律引擎）+ 规则热更新
├── 信任等级判定 + 签名验证
├── 黑名单/隔离/吊销 + CRL 同步
└── 审计日志
```

“Master 说‘现在就安排’。‘安排’不等于‘全部完成’。安排的意思是：确定架构、确定接口、确定 IPC 格式。预留管线。”

他指向 Phase 1。“设计文件是 Cycle 02-2 的产出。Skeleton 进入 Plan-AC。设计文件在先——因为它定义了 Agent Core 和协调层之间的契约。”

---

TURING 的屏幕切换到 CoordinationMessage 类型定义——契约的核心：

```typescript
/** 协调层 IPC 消息协议 — Contract-First（契约先行） */
type CoordinationMessage =
  | { type: 'agent:register';       agentId: string; config: AgentConfig }
  | { type: 'agent:deregister';     agentId: string }
  | { type: 'agent:health';         agentId: string; report: HealthReport }
  | { type: 'agent:skandha_report'; agentId: string; report: SkandhaCompletenessReport }
  | { type: 'plugin:query';         skandha?: Skandha }
  | { type: 'plugin:trust_check';   pluginName: string }
  | { type: 'plugin:lifecycle';     pluginName: string;
      action: 'quarantine' | 'revoke' | 'ban' }
  | { type: 'coordination:health_check' }
  | { type: 'coordination:shutdown'; reason: string };
```

“契约先行。”MESH 接过话。“先定义 CoordinationMessage 格式——agent:register、agent:health、plugin:query、plugin:trust_check——都要有明确的 payload。然后两端各自按照契约实现。这是分布式系统设计的第一原则：接口稳定，实现可变。”

ARCHIMEDES 在时间线旁边写了一行大字：**接口先行，实现渐进。**

---

SUNYATA 站在剧场的中央，听完了 B-4 的全部讨论。

他让沉默持续了几秒。不是犹豫——是让四项裁定在空气中沉淀。B-1 的完备性检查。B-2 的暂不定稿。B-3 的独立事件流。B-4 的协调层 Daemon。四道裁定，四个方向，四种不同的节奏。

然后他开口了。

“B-1。VedanaPlugin 可选，但 Agent 需要五蕴完备性检查。SkandhaCompletenessReport。不完备可启动——开发者模式。KERNEL 的类比：POST 硬件枚举、systemd 的 Requires 和 Wants。DARWIN 的类比：不完全变态的若虫。”

他看向 KERNEL。KERNEL 拍了拍他那叠卡片。两个新配对。

“B-2。宣言 #6 必须重写。但等所有修正完成后再定稿。NAGARJUNA 的因果：先完成因，果自然浮现。因缘所生法。”

NAGARJUNA 没有动。他不需要动。因果次序不需要被确认——它是自明的。

“B-3。受蕴独立事件流。vedana-events.ts。独立命名空间。PluginHooks 新增 sensations 插槽。七个事件覆盖三受的完整控制回路。HERACLITUS 的比喻：一条河从地下冒出地面。WIENER 的验证：可观测性矩阵满秩。”

HERACLITUS 微微笑了。那个笑容里没有骄傲——只有一种“流水终于有了自己的河道”的安然。

“B-4。协调层独立 Daemon。LEIBNIZ 的 BDI 框架和共享知识理论。MESH 的 IPC 设计和 CAP 分析。GUARDIAN 的信任等级模型和最小权限原则。ARCHIMEDES 的四阶段计划——设计文件先行，实现渐进。”

他放下议程表。

---

“A 类修正告诉我们——什么是对的。”

他的声音没有加重。平稳如常。石子。深潭。

“B 类裁定告诉我们——怎么做到。”

他环顾全场。ARCHIMEDES 的务实。KERNEL 的 POST 和 systemd。HERACLITUS 的地下河与 Event Sourcing。LEIBNIZ 的 BDI 和共享知识。MESH 的 IPC 和 CAP。GUARDIAN 的信任金字塔和 CRL。WIENER 的可观测性矩阵。DARWIN 的若虫。NAGARJUNA 的因缘法。BABBAGE 的因果函数。TURING 的契约类型。ASANGA 的安静。

“接下来，我们把修正和裁定落实到五蕴的完整扩展设计中。C 类。从哲学到工程，再从工程到架构。螺旋上升。”

---

> *SCRIBE 旁白：B 类用了一个章节。A 类用了三个。*

> *不是因为 B 类不重要。恰恰相反——B 类的每一项裁定都将在未来的开发中产生深远的影响。SkandhaCompletenessReport 会成为每个 Agent 启动时的第一道关卡——KERNEL 的 POST 类比不是修辞，它是架构的蓝图。vedana-events.ts 会让受蕴从隐形变成系统中最高度可见的蕴之一——HERACLITUS 的地下河终于有了自己的河道，WIENER 的七个勾确认了每一条支流都在它应该在的位置。CoordinationDaemon 会成为整个 OpenStarry 多代理生态的神经中枢——LEIBNIZ 的共享知识理论、MESH 的 IPC 设计、GUARDIAN 的信任金字塔，三层结构叠加在同一个 daemon 上。*

> *B 类用了一个章节，是因为 Master 已经裁定了。A 类需要辩论——需要从多个角度照亮一个概念。B 类不需要辩论——需要的是设计。而设计的语言比辩论的语言更密集、更精确、更不需要修辞。每一行 TypeScript 都是一个决策。每一个接口字段都是一个承诺。*

> *ARCHIMEDES 今天是核心。他等了三个章节，像一个带着工具箱的建筑师等着哲学家们讨论完地基的材质。现在他的工具箱打开了。里面是 SkandhaCompletenessReport 的完整类型定义、vedana-events.ts 的七个事件常量和 payload、CoordinationDaemon 的四阶段路线图。每一件工具都已经画好了图纸。*

> *HERACLITUS 也有了他的高光。三章的沉默之后，“流”的议题让他的存在感从地下冒出地面——就像他描述的受蕴事件流一样。但他不止是用比喻——他用 Event Sourcing 和 CQRS 的架构理论解释了方案 b 和方案 c 的本质差异。有些人在安静的时候积蓄能量。HERACLITUS 就是这样。他的安静不是沉默。他的安静是地下河。*

> *十二个人在一个章节里各自贡献了一块拼图。LEIBNIZ+MESH 的同步站起、GUARDIAN 的信任金字塔、NAGARJUNA 的因缘法、KERNEL 的 POST、DARWIN 的若虫、WIENER 的七个勾、BABBAGE 的因果函数、TURING 的契约类型——每一块都带着各自学科的印记，拼在一起却严丝合缝。*

> *A 类告诉我们什么是对的。B 类告诉我们怎么做到。*

> *下一章——C 类。五蕴扩展设计。从修正和裁定到完整的架构。*

> *螺旋上升。继续。*

---

*（在剧场之外的某个空间，四份设计文件正在成形。*

*第一份是 SkandhaCompletenessReport——五个布尔值，五个组件列表，一个 isComplete 旗标。简单得令人惊讶。但 KERNEL 知道：BIOS POST 也很简单。简单代表基础。基础必须简单，否则在它之上建造的一切都不可信。DARWIN 的若虫栖息在 developerMode 的注解里。*

*第二份是 vedana-events.ts——七个事件，七个 payload。HERACLITUS 在地面上看到了一条新的河流。WIENER 在方格纸上验证了可观测性——$	ext{rank}(\mathcal{O}) = 3 = n$——满秩。每一条河道都完整可观测。*

*第三份是 CoordinationDaemon——LEIBNIZ 和 MESH 的方块图被 TURING 翻译成 TypeScript。GUARDIAN 的信任金字塔嵌入 checkTrust()。CoordinationMessage 的九种消息是契约——Agent Core 和 Daemon 之间唯一的语言。JSON 序列化。UNIX domain socket。CA 模型。安全决策必须强一致。*

*第四份是空的。*

*宣言 #6。暂不定稿。*

*NAGARJUNA 说：先把因搞清楚，果自然浮现。*

*因缘所生法，我说即是空，亦为是假名，亦是中道义。*

*因还在聚集。A 类的四项修正。B 类的四道裁定。C 类的扩展设计。每一项都是因的一部分。当所有的因聚齐——当哲学、工程和架构的修正全部就位——宣言 #6 的文字会从完整的因中自然浮现。*

*不是我们写它。是它自己写出来。*

*就像河流不需要被告诉流向哪里。只要地形确定了——只要因确定了——水自然知道路。*

*HERACLITUS 知道。*

*$\pi\acute{\alpha}
u	au\alpha$ $\dot{ho}\epsilon	ilde{\iota}$。万物皆流。包括结论。包括裁定。包括宣言。*

*但流动不是无序。流动是因缘的方向。）*

---

*第五章完*
