# 第一章：審計與準備

---

## R1 獨立研究

九份研究同時啟動。三條軌道、十五位主筆。

### Track A：五蘊工程架構

Track A 是 Master 的首要任務——用純工程語言回答五蘊架構的四個核心問題。五個子項由十二位研究者分工：

| 子項 | 主筆 | 內容 |
|------|------|------|
| A1 蘊子類別 | LINNAEUS + ASANGA | 五蘊的完整子類別樹，對照 SDK 原始碼 |
| A2 DI 佈線 | VITRUVIUS + KERNEL + TURING | agent-core → plugin-loader → loop 的完整 DI 鏈 |
| A3 Plugin 載入 | DARWIN + MESH | 從 agent.json 到 running hooks 的完整流程 |
| A4 執行流 | HERACLITUS + WIENER + BABBAGE | sparsha → vedana → samjna → volition → tools → feedback |
| A5 跨蘊互動 | LEIBNIZ + ATHENA + PENROSE | vedana→klesha→arbiter→volition→action 的互動矩陣 |

A1 的子類別樹揭示了一個重要的結構特徵：識蘊擁有最多的子介面（IGearArbiter、IVolition、IKlesha、IConfidenceAuditor），而行蘊最簡（ITool 單一介面）。這個不對稱是有意義的——識蘊是「判斷」，判斷的維度天然比「行動」的維度多。

A2 追蹤了完整的依賴注入鏈。三位研究者花了兩天，從 AgentCore 的構造函數開始，經過 PluginLoader 的 registry 分發，到 ExecutionLoop 的每一個 hook 呼叫點。結論：DI 鏈完整，但有兩個已知缺口——IVedanaSensor 弱繼承（不繼承 IVedana）和 VedanaAssessment 佈線預設為中性值。

A4 產出了完整的五蘊執行流圖。HERACLITUS 用他對動態流程的敏感性，追蹤了一個 SparshEvent 從誕生到消亡的完整生命週期。WIENER 用控制理論的語言重新描述了同一個流程——系統是一個閉迴路控制器，使用者目標是參考輸入，Context 是狀態反饋，Tool Call 是控制變量。BABBAGE 做了形式化，用有限狀態機證明了流程的終止性。

### Track B：佛學映射審計

B1 由 ARCHIMEDES 和 SCRIBE 負責。工程實踐專家逐文件、逐映射地掃描了七份 openstarry_doc 文件。方法是三項測試的機械性應用——每一個佛學映射都被測試三次，結果被記錄在審計表中。

最終結果：50 個映射實例。

| 處置 | 數量 | 範例 |
|------|------|------|
| KEEP | 23 | Skandha 型別名、Klesha 模組名、DC 確認約束、CoarisingBundle |
| RELOCATE | 13 | PASCAL 數學形式化、MN 18 經典引用、佛學設計理由 |
| REMOVE | 14 | śīla/upāya/smṛti 標籤、event-driven=正念、戒定慧映射 |

將近一半是 KEEP——不是所有佛學內容都是裝飾。有些是身份（Klesha 模組名），有些是決策（五蘊分類驅動了 PluginHooks 設計）。但 14 個 REMOVE——純粹的裝飾，移除不改變任何工程規格。

ARCHIMEDES 有一個精確的判斷：「不是移除整張表。是移除一欄。」他不用大鉈砸核桃——他用手術刀分離工程內容和佛學裝飾。

兩份特殊文件被標記為 FILE REVIEW：Doc 16（Plugin 類型哲學映射，裝飾比例 ~80%）和 Doc 31（八識運行時模型，裝飾比例 ~70%）。它們的問題不在個別映射，而在整份文件的定位——是工程文件中嵌入了佛學？還是以佛學映射為目的的獨立文件？

B2 由 NAGARJUNA、ASANGA、PASCAL 三人建構映射邊界原則。三個維度的框架：

- **NAGARJUNA（二諦）**：世俗諦 = 工程語言。勝義諦 = 佛學概念。不要在世俗諦的文件中硬塞勝義諦的標籤。
- **PASCAL（損害不對稱）**：False Include 的損害是累積的（讀者數 × 閱讀次數 × 認知轉換成本）。False Exclude 的損害是一次性的（搜尋成本）。E[累積] >> E[一次性]。有疑慮時傾向移除。
- **ASANGA（因果效力）**：佛學概念是否驅動了工程結果？有因果效力 → 保留。無因果效力 → 移除。

三個學科、三條路徑、一個結論——裝飾性映射應移除。

### Track C：Sati Plugin 定位

C1 由 TURING 和 GUARDIAN 負責功能分析。TURING 用純工程術語列出了 SatiMonitor 的四個功能：事件訂閱、滑動窗口、模式辨認、品質指標。以及一個關鍵的「不做」——不執行任何行動、不修改任何狀態、不發出任何指令。

GUARDIAN 的工程類比：APM Agent + Behavioral Analytics + QoS Monitor + SPC Anomaly Detector 的混合體。

C2 由 ASANGA 和 LINNAEUS 負責蘊組成分析。他們提出了四個方案：

| 方案 | 蘊組成 | 理由 |
|------|--------|------|
| A | 受 + 想 | 感知 + 辨認，最簡 |
| B | 受 + 想 + 識 | 感知 + 辨認 + 評估判斷 |
| C | 想 + 識 | 辨認 + 評估，受蘊太薄 |
| D | 純識 | 一切認知活動歸識蘊 |

四個方案都有邏輯支撐，但也各有弱點。最終答案要在 D2 辯論中決定。

---

## R2 交叉審閱

二十位研究者組成交叉審閱網——每人審閱至少兩份非本人主筆的報告。

TURING 做了最關鍵的工作——地毯式驗證所有程式碼引用。40 個以上的引用逐一比對 v0.28.0-alpha 原始碼。結果：四個問題（10% 以下的錯誤率），全部為低或中嚴重度。沒有致命錯誤。

他說了六個字：「引用乾淨。可以進入辯論。」

R2 的總結：
- **24 個共識點**：跨三條軌道，基礎穩固
- **7 個開放問題**：辯論有明確焦點
- **4 個分歧點**：辯論會有交鋒

管道通了。手術室準備好了。

---
