# 第一章：審計與研究

---

## R1：獨立研究

九份獨立研究報告在 R1 階段產出。三條軌道並行推進。

### Track A：五蘊工程架構

**A1（LINNAEUS + ASANGA）**：五蘊子類別樹。完整的 OOP 介面繼承分析——IRupa 分為 IListener 和 IUI；IVedana 產生 ChannelVedana（連續信號）；ISamjna 對應 IProvider；ISamskara 窄化為 ITool；IVijnana 最複雜，下轄 IGuide、IGearArbiter、IVolition、IKlesha 四個子介面。三個「弱繼承」案例被記錄——IVedanaSensor、IGearArbiter、IKlesha 不顯式 extends 根介面。

**A2（VITRUVIUS + KERNEL + TURING）**：DI 佈線。Pure DI，`createAgentCore()` 為唯一 Composition Root，21 個組件嚴格線性建立，9 個 Registry。Lazy Accessor 模式、Provider 能力過濾、Resolver 閉包延遲解析。與 Spring/Guice/InversifyJS 的比較矩陣確認 Pure DI 是微核心的正確選擇。

**A3（DARWIN + MESH）**：Plugin 載入生命週期。IPlugin = Manifest + Factory。雙載入路徑（Sandbox worker thread / Direct main thread）。八狀態生命週期狀態機。Sandbox 安全鏈：簽名驗證 → 靜態 import 分析 → Worker 隔離 → Heartbeat → 指數退避重啟。

**A4（HERACLITUS + WIENER + BABBAGE）**：五蘊執行流。FSM 六狀態、九階段處理。Phase 1（rupa）→ Phase 3（samjna）→ Phase 5（vijnana）→ Phase 6（samskara）→ Phase 7（vedana）→ Phase 8（vijnana）。三層穩定迴路。BABBAGE 提供了完整的 FSM 形式規格。

**A5（LEIBNIZ + ATHENA + PENROSE）**：跨蘊互動。5×5 互動矩陣。Model Delta 五層閾值公式。PENROSE 提出了三個湧現模式假說——適應性保守、雙穩態切換、注意力漏斗。

### Track B：佛學映射審計

**B1（ARCHIMEDES + SCRIBE）**：逐行審計 7 份文件。50 個映射實例——23 個 KEEP（46%）、13 個 RELOCATE（26%）、14 個 REMOVE（28%）。Doc 43 裝飾比例最高（60%）。Doc 16 和 Doc 31 被標記為「整份審查」（裝飾比例 80% 和 70%）。

**B2（NAGARJUNA + ASANGA + PASCAL）**：映射邊界原則。NAGARJUNA 的兩諦分離、ASANGA 的功能定位、PASCAL 的損害不對稱性（false include 的累積認知負擔 >> RELOCATE 的一次性搜尋成本）。三項測試在此文件中被正式論證。

### Track C：Sati Plugin

**C1（TURING + GUARDIAN）**：純工程功能分析。SatiMonitor 訂閱 11 種 EventBus 事件，三階段管道處理（緩衝 → 批次分析 → 品質向量計算），輸出 LoopQualityVector 四維度（Continuity, Granularity, Speed, Equanimity），**零副作用**。工程等價物：APM Agent + 行為模式分析器 + QoS Monitor + SPC 異常偵測器。

**C2（ASANGA + LINNAEUS）**：蘊組成提案。四個方案——A ['vedana','samjna']、B ['vedana','samjna','vijnana']（推薦）、C ['samjna','vijnana']、D ['vijnana']。核心論證：SatiMonitor 的事件訂閱=受（vedana），模式辨認=想（samjna），品質評估=識（vijnana）。不包含行蘊——因為它不執行任何動作。

## R2：交叉審閱

TURING 驗證了 40+ 個程式碼引用，發現 4 個問題（無嚴重錯誤）。24 個共識點免辯論通過。7 個開放問題和 4 個分歧進入 D1-D3 辯論。

---
