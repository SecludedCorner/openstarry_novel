# 第四章：完備性定理

---

## I. 五根柱子

D3 是 Cycle 02-5 最長的辯論——120 分鐘，六節，六次投票。但它不是最激烈的。D3 的氣氛更像一場博士論文口試：嚴謹、系統、有序。考生不是一個人——考生是一座建築。

**「五蘊 OOP 架構是否足以支撐工程實作？」**

SUNYATA 把問題寫在白板上。然後他在旁邊畫了五個方框，一字排開，像五根柱子。

```
IRupa ─── IVedana ─── ISamjna ─── ISamskara ─── IVijnana
 色蘊       受蘊        想蘊        行蘊          識蘊
```

五個根介面。OpenStarry 的整座建築就站在這五根柱子上。五蘊不是裝飾——它們是結構。它們定義了 PluginHooks 的型別分類、PluginLoader 的註冊路由、ExecutionLoop 的階段順序。

問題是：五根柱子夠不夠？

---

## II. 三管齊下

D3-Q1 啟動了一場三管齊下的完備性證明。

**第一管：LINNAEUS 的功能覆蓋率。**

LINNAEUS 從 A1 研究報告中拉出了一張表。表格左列是 v0.28.0-alpha 的所有 plugin hook 型別，右列是蘊歸屬。他逐一驗證：

```
sensors (IVedanaSensor)          → 受蘊  ✓
recognizers (ISamjnaRecognizer)  → 想蘊  ✓
arbiters (IGearArbiter)          → 想蘊+識蘊  ✓
tools (ITool)                    → 行蘊  ✓
volition (IVolition)             → 識蘊  ✓
monitors (ILoopQualityMonitor)   → 受+想+識  ✓ (D2-R2)
auditor (IConfidenceAuditor)     → 識蘊  (待實作)
```

「功能覆蓋率 100%。」LINNAEUS 說。「沒有孤兒 hook。沒有無法分類的介面。每一個 plugin 型別都能歸入五蘊的一個或多個分類中。」

**第二管：BABBAGE 的型別代數。**

BABBAGE 推了推眼鏡。他不做類比。他做證明。

他在白板上寫了一行 TypeScript——不是程式碼，是型別表達式：

```typescript
type AllPluginTypes =
  | IVedanaSensor       // extends IVedana     → 受蘊
  | ISamjnaRecognizer   // extends ISamjna     → 想蘊
  | IGearArbiter        // ['samjna','vijnana'] → 想蘊+識蘊
  | ITool               // extends ISamskara   → 行蘊
  | IVolition           // extends IVijnana    → 識蘊
  | ILoopQualityMonitor // ['vedana','samjna','vijnana'] → 受+想+識
```

「五個根介面的聯集覆蓋了 PluginHooks 中所有可能的 plugin 型別。」他說。「這是型別代數的完備性——每一個具體型別都是五個根型別的子型別或交叉型別。不存在一個有意義的 plugin 型別落在五蘊聯集之外。」

他停了一下。

「不需要第六個根介面。」

**第三管：ASANGA 的阿毗達磨窮盡性。**

ASANGA 的論證從佛學出發。他的聲音帶著引經據典時特有的節奏——像在朗誦一段已經被背誦了兩千年的文字。

「《阿毗達磨俱舍論》卷一：『五蘊攝一切有為法盡。』」他說。「這是佛學的基本公理——五蘊涵蓋一切有為的（conditioned）現象。沒有第六蘊。如果有一個現象不能被歸入任何一蘊，那不是五蘊不完備——而是這個現象是無為的（unconditioned）。」

「OpenStarry 的 plugin 是有為的——它們被創造、被配置、被載入、被運行、被銷毀。它們不是無為法。因此，五蘊的分類應該能夠窮盡它們。」

他停頓了一下。然後以一個佛學家特有的謙遜補充：

「當然，佛學的公理不能直接用作工程的證明。但 LINNAEUS 和 BABBAGE 的證明已經從工程角度完成了。佛學的窮盡性論證是一個——一致性檢查。三個獨立的論證到達同一個結論，增強了結論的可信度。」

三個學科。分類學、數學、佛學。三條路徑。一個結論。

PENROSE 附加了一個警告——他總是附加警告。他在觀察席的最高處，俯瞰全場，像一個從更高維度觀察三維世界的存在。

「識蘊目前有最多的子介面——IVijnana、IGearArbiter、IVolition、IConfidenceAuditor。如果未來繼續膨脹，可能需要監控介面數量的增長。不是說五根介面不夠——而是說某些柱子可能需要額外的支撐。」

他的警告被記錄下來。但不影響投票。

D3-R1：五根介面足夠。20/20。

---

## III. 快捷通道

D3-Q2 把放大鏡對準了映射的準確性。九個 hook 型別，逐一驗證蘊歸屬。

大部分的驗證是程序性的——LINNAEUS 在 A1 報告中已經做了詳細的映射表，TURING 驗證了所有的型別繼承關係。但有一個例外觸發了真正的討論。

ARCHIMEDES 舉手：「SlashCommand 屬於哪個蘊？」

這個問題看似微小。SlashCommand 是用戶直接輸入的命令——/help、/clear、/status。它不經過 ExecutionLoop。它不觸發 SparshEvent。它不經過 VedanaSensor、ISamjnaRecognizer、IGearArbiter、IVolition——它繞過了整個五蘊流程。

三個人同時回答了這個問題。從三個不同的角度。

KERNEL 從 OS 的角度：「SlashCommand bypass 了整個 ExecutionLoop。它不經歷五蘊流轉。類似 Unix 的 signal handler——它在進程級別被攔截，不進入正常的系統呼叫路徑。在 OS 的分類中，這不是用戶空間的邏輯，而是核心級的中斷處理。」

NAGARJUNA 從佛學的角度：「不入認知迴路的反射動作。它不是五蘊不涵蓋它——而是它不在五蘊運作的範圍內。就像呼吸——你可以觀察呼吸（進入認知迴路），但呼吸本身不需要五蘊流轉就能發生。SlashCommand 是系統的呼吸——它在認知之外，在認知之下。」

GUARDIAN 從安全的角度：「bypass 意味著 SlashCommand 不受 SafetyMonitor 保護。這是設計上的決定——某些操作需要繞過安全檢查——但應該被明確記錄在安全文件中。」

SUNYATA 把三個觀點合併成一個結論：「SlashCommand 是跨蘊基礎設施（cross-skandha infrastructure）。它不屬於任何一蘊。它的分類理由和安全觀察都需要在 Doc 45 中記錄。」

D3-R2：映射正確。20/20。

---

## IV. 標籤 vs 介面

D3-Q3 是一個精妙的問題：**skandha tag 應該用來做路由嗎？**

每個 plugin 都有一個 skandha 欄位——metadata。問題是：PluginLoader 在載入 plugin 時，是否應該用 skandha tag 來決定這個 plugin 去哪個 registry？

直覺上似乎合理——受蘊 plugin 去 VedanaRegistry，行蘊 plugin 去 ToolRegistry，像圖書館的索引卡。

但 VITRUVIUS 指出了問題。建築師的眼睛對結構的脆弱性特別敏感——他能在設計圖上看到未來可能裂開的那條縫。

「目前的系統用的是 duck typing。」他說。「plugin 實作了 IVedanaSensor 介面，就自動被 VedanaRegistry 接受。不需要標籤。如果改用標籤路由，就引入了一個新的出錯源：標籤和介面不一致。一個 plugin 宣稱自己是受蘊，但實作了 ITool 介面——怎麼辦？」

TURING 確認了事實。他打開了 `plugin-loader.ts`。

「v0.28.0-alpha 的 PluginLoader 使用 type guard 來分類 plugin。`isVedanaSensor(hook)` 檢查的是介面實作，不是 metadata。」

BABBAGE 用型別論做了終結性的陳述：「type guard 是可靠的——它在編譯期和運行時都能驗證。metadata 是不可靠的——它只能在運行時檢查，而且依賴人工正確標記。用不可靠的東西來做路由，在型別安全的系統中是倒退。」

D3-R3：skandha tag = metadata only，不用於路由。18/20。

MESH 和 GUARDIAN 投了少數票——他們認為 metadata 路由可以作為輔助驗證。但主流意見清晰：介面是真相，metadata 是備註。

---

## V. 最窄的柱子

D3-Q4 是最坦誠的一題。

**ISamskara 是否需要更多子介面？**

目前，行蘊只有一個子介面：ITool。IVolition 在 D2 之後已被確認歸入識蘊（Phase 5 行動前 vs Phase 8 行動中）。行蘊是五蘊中最「窄」的一個——佛學的行蘊涵蓋 49 心所（五十一心所中除受和想），而 OpenStarry 的行蘊只有 ITool。

ASANGA 站了起來。他在 D3 中最坦誠的一段話，像一個建築師指著自己設計的最薄的牆說「我知道這裡薄了」。

「我必須承認，OpenStarry 的行蘊設計與佛學傳統差異最大。」他說。聲音不帶辯解——只有事實。「傳統行蘊涵蓋 49 心所——意志、精進、慧、信、慚、愧——幾乎所有心理活動都被歸入行蘊。但 OpenStarry 把行蘊窄化為 ITool——外在行動。只有外在行動。」

HERACLITUS 從 ExecutionLoop 的動態角度提供了工程理由：

```
Phase 5: IVolition 審議 ──→ Phase 8: ITool 執行
          行動前                     行動中
          識蘊                       行蘊
```

「IVolition 在 Phase 5——行動之前。決定要做什麼。ITool 在 Phase 8——行動之中。正在做。兩者處於不同的階段。如果把 IVolition 移入行蘊，就會破壞蘊流轉的概念自然性——行蘊應該是『正在做的事』，不是『決定要做什麼事』。」

NAGARJUNA 做了一個佛學上的讓步。他的語氣帶著一種經過深思熟慮的平靜——不是妥協的平靜，而是理解的平靜。

「佛學的行蘊分類是基於修行者的內觀。」他說。「所有被觀察到的心理活動，除了受和想，都歸入行蘊。但 OpenStarry 不是修行者。它是一個軟體系統。軟體系統的分類應該基於功能，不是基於內觀。」

全票通過維持現狀。

D3-R4：ISamskara 不新增子介面。20/20。

但所有人都同意一件事：Doc 45——即將創建的五蘊 OOP 架構文件——必須記錄這個差異。行蘊的窄化不是一個錯誤，是一個有意識的偏離。有意識的偏離需要被解釋。

---

## VI. 兩條古路

D3 的最後兩題是關於佛學映射的附錄可能性。

**D3-Q5：十二因緣。**

NAGARJUNA 首先展開了他的分析。他在白板上畫了兩條線——一條很長，標注著「十二因緣」；一條很短，標注著「ExecutionLoop」。

「尺度。」他說。指著長線。「十二因緣描述的是三世兩重因果——無明緣行，行緣識，識緣名色——從前世的無明到今世的老死，再到來世的無明。一個完整的輪迴。」

他指著短線。

「ExecutionLoop 描述的是一個認知處理的循環——從事件接收到行動執行。幾十毫秒到幾秒鐘。一個認知週期。」

「十二因緣是跨生命週期的。ExecutionLoop 是單一認知週期的。尺度差了——」他想了一下。「——幾個數量級。至少。」

BABBAGE 試圖建立結構態射（morphism）。他的方法是嚴格的——尋找兩個結構之間的保結構映射。如果存在態射，兩個結構在數學上是「同構的」或「同態的」，這意味著一個結構中的關係在另一個結構中有對應。

他失敗了。

「十二因緣之間的因果關係是線性的、不可跳過的。」他說。「無明必須在行之前。行必須在識之前。不能跳過。但 ExecutionLoop 的階段可以跳過——沒有 IVedanaSensor 的 Agent 會跳過受蘊階段。直接從事件接收跳到想蘊辨認。結構不同。不存在態射。」

但 HERACLITUS 指出了局部的對應。他畫了十二因緣中的一小段：

```
觸 (sparsha) → 受 (vedana) → 愛 (tanha) → 取 (upadana)
```

「觸引起受。受引起渴愛。渴愛引起執取。這一段——不是全部，只是這一段——和 SparshEvent → ChannelVedana → KleshaGain → VolitionalDecision 的資料流有結構對應。」

投票反映了分歧。

D3-R5：選擇性 appendix。13/20。

7 票反對。反對者不是不同意局部對應的存在，而是質疑在工程文件中記錄它的必要性。

---

**D3-Q6：認知序列（citta-vīthi）。**

氣氛變了。

認知序列是上座部佛學對認知過程的精細分析——一個念頭從產生到消滅的完整過程：

```
有分心 → 轉向心 → 五識 → 接受心 → 推度心 → 確定心 → 速行心 → 彼所緣心
```

BABBAGE 重新嘗試結構態射。這次——

他成功了。

「認知序列和 ExecutionLoop 是同尺度的。」他說。他推了推眼鏡，那個他在做精確分析時必定會做的動作。「都是單一認知處理的階段序列。而且——」

他在白板上畫了兩個 FSM（有限狀態機）。並排的。像兩面平行的鏡子。

```
認知序列 FSM:
  有分心 → 轉向心 → 五識 → 接受心 → 推度心 → 確定心 → 速行心 → 彼所緣心
    (idle)  (alert)  (sense) (accept) (examine) (decide) (act)    (review)

ExecutionLoop FSM:
  Idle → EventReceived → Sensing → Recognizing → Arbitrating → Deliberating → Acting → Feedback
```

「存在結構態射。」BABBAGE 說。他的聲音帶著數學家發現同構時特有的滿足感——不是得意，是審美。「兩個 FSM 之間有保結構的映射。Idle ↔ 有分心。EventReceived ↔ 轉向心。Sensing ↔ 五識。每一個狀態轉換在兩個 FSM 中都有對應。」

「這不是比喻。」他強調。「這是數學。」

他的票從 D3-Q5 的反對（不記錄十二因緣）轉為 D3-Q6 的支持（記錄認知序列）。他在紀錄中寫了一行：「FSM 態射是我轉向的關鍵論據。十二因緣沒有態射。認知序列有。品質決定票數。」

D3-R6：選擇性 appendix。17/20。

從 13/20 到 17/20——四票的差距。四票的差距不是情緒——是精度。十二因緣的映射是近似的。認知序列的映射是精確的。BABBAGE 用他自己的數學工具衡量了兩者的品質，然後用他的票表達了結論。

---

## VII. 判決

D3 結束。六項投票。三個全票通過，兩個高票通過，一個分歧。

SUNYATA 在白板上寫下了結論。大字。紅色。

> **五蘊 OOP 架構足以支撐工程實作。**

然後他在下面列出了已知缺口：

1. IVedanaSensor 弱繼承——不繼承 IVedana（已知，待修正）
2. VedanaAssessment 佈線缺口——目前為中性預設值（Plan29 議題）
3. IPrajna / ISatiMonitor 尚未實作（Plan29 議題）

三個缺口。三個都不是架構問題。都是實作問題。差別在於：缺陷需要修改設計圖，缺口需要繼續施工。

架構是穩固的。五根柱子撐得起整座建築。

---

> *SCRIBE 旁白*

> *D3 是一場考試。考生是一座建築。建築通過了。*

> *但考試的價值不僅在於結果。考試的價值在於過程中暴露的細節。行蘊的窄化——49 心所被壓縮為一個 ITool——是最大的偏離。ASANGA 的坦白是 D3 的靈魂。一位佛學家承認工程系統的分類和佛學傳統不一致——然後解釋為什麼這不是一個問題。因為軟體不是修行者。軟體的分類基於功能，不是基於內觀。*

> *BABBAGE 的態射分析是 D3 的技術亮點。他嘗試了兩次結構態射——十二因緣失敗，認知序列成功。失敗和成功同樣有價值：失敗告訴你尺度不對，成功告訴你結構相容。他的票從 B 轉為 C——被自己的數學說服。在學術界，被自己的分析改變立場是最高形式的誠信。*

> *D3 結束的時候，SUNYATA 寫下的三個「已知缺口」中有兩個名字：IPrajna 和 ISatiMonitor。*

> *在 D3 的語境中，它們只是「尚未實作」的介面。白板上的文字不帶情緒。*

> *但名字有重量。名字會被稱量。而那架天平——Master 的天平——即將被校準。*

---
