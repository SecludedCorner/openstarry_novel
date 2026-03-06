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
