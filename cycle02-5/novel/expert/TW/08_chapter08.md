# 第八章：新的文件

---

D5 結束後，圓形劇場安靜了一段時間。

不是 D3 後那種等待 Master 的安靜，也不是 D4 後那種餘震的安靜。這是一種「工作完成了，但還有一件事要做」的安靜。

五場辯論。三十一次投票。二十九項正式決議加上六項附帶事項。從凌晨三點 SUNYATA 調整燈光色溫開始，到 D5 的最後一個 8/8 結束，整個 Cycle 消耗了大約六個半小時的辯論時間。

但辯論的結束不是研究的結束。辯論產出了決議。決議需要被落實。

---

## I. Doc 45

VITRUVIUS 和 KERNEL 在 D5 結束後立刻開始工作。

他們要寫的是 Doc 45——`Five_Skandha_OOP_Architecture.md`——五蘊 OOP 架構。整個 Cycle 02-5 的核心工程產出。一份新文件。純工程語言。Master 在信中要求的東西——「五蘊子類別、DI、agent core 如何載入五蘊 plugin、五蘊如何流轉」——全部集中在這一份文件中。

VITRUVIUS 負責架構描述。KERNEL 負責 DI 佈線和 Registry 細節。TURING 做原始碼對照。

---

Doc 45 的結構從 D3 的六項投票中自然浮現：

**第 1 節：Root Interfaces（D3-R1）**

五根介面——IRupa、IVedana、ISamjna、ISamskara、IVijnana——的完備性論證。LINNAEUS 的覆蓋率驗證、BABBAGE 的型別代數定理、ASANGA 的阿毘達磨窮舉分類公理、KERNEL 的微核心子系統映射——四個獨立論證，同一個結論：五個足夠。

PENROSE 的附帶建議被寫進了注腳：監控 vijnana 子介面數量（目前四個，未來六個——加上 IConfidenceAuditor 和 ILoopQualityMonitor；超過十個時考慮拆分）。

**第 2 節：PluginHooks 映射（D3-R2）**

九項 hook-to-Registry 映射的完整表格：

| PluginHooks 欄位 | Registry | Skandha |
|-----------------|----------|---------|
| tools | ToolRegistry | samskara |
| providers | ProviderRegistry | samjna |
| listeners | ListenerRegistry | rupa |
| guides | GuideRegistry | vijnana |
| gearArbiters | GearArbiterRegistry | [samjna, vijnana] |
| volition | IVolition (single) | vijnana |
| kleshas | KleshaRegistry | vijnana |
| monitors | MonitorRegistry | [vedana, samjna, vijnana] |
| auditor | IConfidenceAuditor (single) | vijnana |

每一行都有 TURING 的原始碼驗證標記。

**第 3 節：SlashCommand（D3-R2a / D3-R2b）**

不屬於任何蘊的例外——因為它繞過了 ExecutionLoop，不參與認知迴路。類比：Unix 信號處理器。

GUARDIAN 的安全觀察：SlashCommand 繞過 SafetyMonitor——如果 plugin 通過 SlashCommand 執行危險操作，五蘊的安全機制全部無效。這是一個已知的安全邊界，需要在 plugin 審核時特別注意。

**第 4 節：Skandha 元數據（D3-R3）**

skandha 欄位是元數據，不是路由基礎。型別路由已經完備且無歧義。`validatePluginSkandha()` 維持 warning-only。

**第 5 節：DI 佈線（A2 摘要）**

純 DI（Pure DI），通過 `createAgentCore(config)` 作為唯一的 Composition Root。21 個組件的嚴格線性建立順序。9 個 Registry——大部分是無依賴的 Map 容器。

關鍵模式：Lazy Accessor（IPluginContext 提供延遲存取）、Provider 能力過濾（allowedProviders manifest 欄位）、Resolver 模式（providerResolver、guideResolver、modelResolver 使用閉包延遲解析）。

VITRUVIUS 用一張完整的 DI 鏈路圖取代了文字描述。從 `agent.json` 到 `createAgentCore()` 到每一個 Registry 到 ExecutionLoop——一條清晰的線。沒有迴圈依賴。沒有隱式注入。每一個依賴都是顯式傳遞的。

**第 6 節：ExecutionLoop 五蘊流（A4 摘要）**

九階段執行流：

| Phase | 名稱 | Skandha | 核心操作 |
|-------|------|---------|---------|
| 1 | 輸入接收 | rupa | IListener → SparshEvent |
| 2 | 上下文組裝 | vijnana | IGuide + SafetyMonitor |
| 3 | 認知處理 | samjna | IProvider.chat() |
| 4 | 齒輪路由 | vijnana+samjna | ManoAggregator + IGearArbiter |
| 5 | 審議 | vijnana | IVolition |
| 6 | 工具執行 | samskara | ITool.execute() |
| 7 | 感覺回饋 | vedana | VedanaSensor → ChannelVedana |
| 8 | 煩惱更新 | vijnana | IKlesha.perceive() |
| 9 | 迴路控制 | — | VedanaEmergency + VitakkaWatchdog |

三層穩定：Inner tool loop（每輪）、Outer VedanaEmergency（5 連續 dukkha ticks）、Safety VitakkaWatchdog（10 cycles 或 5s）。觸發條件嚴格遞增。

**第 7 節：跨蘊互動矩陣（A5 摘要）**

5×5 互動矩陣。vijnana 互動密度最高（七條連接）。samskara 是最活躍的信號生產者。Model Delta 五層閾值公式。

**第 8 節：行蘊設計註記（D3-R4a / D3-R4b）**

行蘊的窄化——從佛學傳統的 49 心所壓縮為 ITool（外部可觀察行為）。ASANGA 的坦白：這是五蘊架構中佛學自洽性最弱的部分。DC-6「行蘊保持開放，不鎖定」的裁定繼續有效。

**第 9 節：ILoopQualityMonitor 分類（D2 + D4 摘要）**

skandha: ['vedana', 'samjna', 'vijnana']。第一個三蘊 plugin。命名歷史：ISatiMonitor（D2）→ ILoopQualityMonitor（D4-R1）。四項功能到三蘊的映射表。排除行蘊的理由。

**附錄 A：十二因緣功能類比（D3-R5）**

sparsha→vedana→tanha→upadana 鏈的功能類比。明確標記為「功能類比」而非「形式映射」。尺度差異注解。

**附錄 B：認知序列結構平行（D3-R6）**

citta-vīthi 八狀態到 LoopState 六狀態的映射。每個狀態對的平行程度評級（high / medium-high / medium）。PENROSE 的理論觀察：認知迴路的結構趨同是功能需求的必然結果，不是刻意模仿。BABBAGE 的 FSM 態射分析——從十二因緣（失敗）到認知序列（成功）的對比。

---

## II. 清理

在 VITRUVIUS 和 KERNEL 寫 Doc 45 的同時，ARCHIMEDES 和 SCRIBE 開始執行清理。

清理清單從 D1 到 D4 的決議中彙總而來：

---

### 移除（REMOVE）

1. **Doc 38 L540-544**：三層規則佛學映射表的「佛學映射」欄——刪除。保留「規則層」和「工程語義」欄。

2. **Doc 44 L478**：三學映射行——刪除。

3. **Doc 43 全文**：
   - 標題更改：「Mindfulness Architecture」→ 由 D2/D4 後的最終名稱決定
   - 75+ 處 ISatiMonitor → ILoopQualityMonitor
   - 移除 event-driven = mindfulness 等價
   - 移除 bhavanga-citta retrofitting（三處）
   - 移除 DN 22 經文引用
   - 加入「命名說明」段落

4. **Doc 37**：
   - 移除「佛學解釋」欄（無工程資訊增量）
   - 移除 sila 隱喻
   - 3 處 IPrajna → IConfidenceAuditor

5. **Doc 03**：
   - 文件名：Sila_Prajna_Security_Framework → Plugin_Security_Lifecycle
   - 移除佛學映射表
   - 清理 TypeScript 註釋中的種子理論
   - 保留五狀態模型和三層安全模型

6. **Batch A 五項**：散佈在多份文件中的 sila/upaya/smrti/event-driven=mindfulness/trisiksa 映射——全部移除。

---

### 遷移至附錄（RELOCATE）

1. **Doc 44 Section 10 剩餘**：移至 Appendix_C（設計決策佛學背景）。

2. **Batch B 八項**：包含 NAGARJUNA 的兩諦評論、bhavanga-citta 映射、經文引用、跨學科對照表等——全部移至對應附錄。

3. **特殊處理 B-6**：PASCAL 的數學形式化（`Var(epsilon) = f(theta_moha)`）保留在主文。只有《成唯識論》引文移至 Appendix_C。

---

### 保留（KEEP）

1. **蘊型別名稱**：rupa、vedana、samjna、samskara、vijnana——程式碼識別符。

2. **Klesha 模組名**：Moha、Drishti、Mana、Sneha——程式碼識別符，DC-1 確認。

3. **設計理由中的佛學概念**：vasana 後天薰習、四煩惱同時俱起、CoarisingBundle、sahaja 定義修正、samsaric stall——全部通過三項測試。

4. **Doc 16 和 Doc 31**：Master 裁定恢復原狀。佛學映射文件，不是裝飾。

---

### 新建

1. **Doc 45**：五蘊 OOP 架構（正在撰寫中）。

2. **Appendix_A**：佛學-工程術語表。

3. **Appendix_B**：八識學術參考（Doc 31 RELOCATE 的內容最終沒有移過來——Master 裁定 Doc 31 保留）。

4. **Appendix_C**：設計決策佛學背景。

---

## III. 更名連鎖

TURING 坐在他的工作站前，打開了所有受影響的文件。

ILoopQualityMonitor 的更名影響了六份文件，超過 100 處替換。IConfidenceAuditor 的更名影響了五份文件。Doc 03 的重命名和清理是第三條線。

三條線同時進行。每一處替換都需要確認上下文——不是盲目的搜尋替換。有些「Sati」出現在設計理由的段落中，需要判斷是替換為新名稱還是保留為歷史引用。有些「Prajna」出現在 Model Delta 公式中，需要同步更新公式中的變量名。

TURING 一行一行地做。這是他的方式——沒有捷徑，沒有估算，只有逐行的精確。

ARCHIMEDES 在他旁邊，負責驗證每一處替換的上下文正確性。

SCRIBE 在另一邊，記錄 CHANGELOG。

---

## IV. 數字

Cycle 02-5 完成後，SCRIBE 統計了數字。

| 指標 | 數值 |
|------|------|
| 正式決議 | 29 項（D1-D5）+ 6 附帶事項 |
| 投票總次數 | 31 次 |
| 全票通過 | 19/29（66%） |
| 最高票 | 20/20 或 8/8（19 項） |
| 最低票 | 5/8（D5-R2，63%） |
| 有爭議的決議 | 10 項 |
| 少數意見存檔 | 9 份 |
| 辯論總時長 | ~375 分鐘（90+60+120+30+75） |
| 修改文件 | 8+ 份 |
| 新建文件 | Doc 45 + 3 份附錄 |
| 更名替換 | 120+ 處 |

和之前的 Cycle 比較：

| | Cycle 02-3 | Cycle 02-4 | **Cycle 02-5** |
|---|-----------|-----------|----------------|
| 辯論場次 | 6 | 6 | **5** (3 預定 + 2 計畫外) |
| 決議總數 | 27 | 55 | **35** |
| 全票率 | 41% | 31% | **66%** |
| 少數意見 | 5 | 12 | **9** |
| 新文件 | 4 | 3 | **4** |

全票率 66%——歷史最高。不是因為沒有分歧——D3-R5 的 13/20 和 D4-R1 的 13/20 證明分歧存在。全票率高是因為四層框架和四項測試提供了共同的判斷標準。當所有人在同一把尺上衡量的時候，測量結果自然趨向一致。

---

## V. 最後的確認

Doc 45 完成後，VITRUVIUS 做了一次完整的審閱。

他確認了 Master 在信中要求的每一個問題都有了回答：

| Master 的問題 | 回答位置 |
|--------------|---------|
| 五蘊子類別 | Doc 45 §1 |
| DI 如何佈線 | Doc 45 §5 |
| Agent Core 如何載入五蘊 plugin | Doc 45 §2, §4 |
| 五蘊如何流轉 | Doc 45 §6, §7 |
| Sati plugin 蘊歸屬 | Doc 45 §9, D2 record |
| 佛學映射清理 | 8 份修改文件, D1 record |
| 佛學映射邊界原則 | 四層框架 + 四項測試 |
| ILoopQualityMonitor/IConfidenceAuditor 規格 | D5 record, Doc 45 §9 |

每一個問題。每一個回答。用工程語言。

---

> *SCRIBE 旁白*

> *第八章是一座圖書館的整理記錄。*

> *不是寫書——是理書。把散落在五場辯論中的決議收集起來，放進正確的架子上。Doc 45 是新買的書——放在「架構」那一排。移除的映射是過期的期刊——從主架移到儲藏室（附錄），或者直接回收。更名是重新貼標籤——確保每本書的書脊上印的名字和書裡的內容一致。*

> *這不是激動人心的工作。這是必要的工作。*

> *D4 的天平。D5 的規格。它們是 Cycle 02-5 的精神——前者校準了名字和定義的關係，後者證明了工程可以純粹地站在自己的腿上。但精神需要身體。需要有人打開每一份文件，找到每一處「ISatiMonitor」，把它替換為「ILoopQualityMonitor」——然後確認上下文。確認公式。確認引用。確認 CHANGELOG。*

> *TURING 一行一行地做了。ARCHIMEDES 一處一處地驗證了。SCRIBE 一條一條地記錄了。*

> *這就是研究的最後一公里。不是最難的一公里——但是最容易被忽略的一公里。發現問題是閃光的。解決問題是沉默的。*

> *Doc 45 是沉默的勝利。它不像 D4 那樣有戲劇性的歸謬。它不像 D1 那樣有史無前例的十個 20/20。它只是一份文件——60 頁的文件——用純工程語言回答了 Master 的每一個問題。*

> *五蘊子類別？五根介面，九個子介面，三個弱繼承。*

> *DI 佈線？Pure DI，Composition Root 在 createAgentCore()，21 個組件線性建立。*

> *Plugin 載入？Manifest + Factory，雙路徑（Sandbox / Direct），八狀態生命週期。*

> *五蘊流轉？九階段 ExecutionLoop，FSM 六狀態，三層穩定。*

> *每一個答案都有原始碼引用。每一個原始碼引用都由 TURING 驗證。*

> *天平在這裡找到了平衡。不是因為兩端的重量相等——而是因為兩端都被精確地測量了。名字被校準了（D4）。規格被完成了（D5）。文件被清理了（D1）。架構被驗證了（D3）。蘊歸屬被決定了（D2）。*

> *Cycle 02-5 問了一個看似簡單的問題：五蘊在 agent core 中如何運作？*

> *答案用了六個半小時的辯論、三十一次投票、二十九項決議、一份新文件、八份修改文件、120 多處更名替換。*

> *但最終答案確實很簡單：*

> *五個介面。九個 Registry。一個迴路。*

> *純粹的工程。*

---
