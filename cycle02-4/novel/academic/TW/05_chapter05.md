# 第五章：零反對票

---

## I. 暴風雨之後

D6 全場零反對票。最低 16/20——四人棄權，但沒有一票反對。

在 D5 的暴風雨之後，D6 的寧靜不是沉默——是解決。D5 建立了框架（三層安全、五層 Model Delta、風險加權閾值）。D6 把框架填滿了工程細節（受蘊雙層、三閘門、路線圖）。一百一十分鐘。沒有硝煙。

GUARDIAN 在 D6 中的角色完全不同於 D5。D5 的 GUARDIAN 是質疑者——挑戰每一個降低安全門檻的提案。D6 的 GUARDIAN 是建造者——他主動呈現了 VasanaEngine 的威脅模型（CR05，CRITICAL 評級），提出了三閘門方案。這個轉變不是妥協，是深化。他不再只是說「這不安全」——他在說「這是威脅，這是方案」。

---

## II. v_latent 與雙層架構

v_true 更名為 v_latent。NAGARJUNA 的論證：v_true 暗示存在客觀的「真實效價」，但在緣起觀中不存在脫離因緣條件的獨立實體。v_latent 承認了估計的主觀性，同時保留了 Bayesian 濾波的數學功能。

一個符號。零行程式碼。修正了整個框架的認識論立場。

v_latent 的意義超越命名。在 Bayesian 濾波中，Kalman filter 估計的是一個「潛在的」（latent）狀態——它永遠不會直接觀測到這個狀態，只能通過帶有噪聲的觀測來推斷。v_true 暗示有一個「真實的」效價存在於某處，等待被發現。v_latent 承認效價是一個推斷——基於觀測、先驗和模型的最佳估計。

PASCAL 從統計學的角度確認：「在 Bayesian 框架中，所有參數都是 latent。沒有任何參數是 true。v_latent 是正確的統計命名。」

20/20。

受蘊雙層架構：信號層（連續函數，VedanaSensor，Kalman filter）+ 語義層（classifyVedana，三受分類）。NAGARJUNA 的佛學定位——信號層 = 世俗諦，語義層 = 假施設。連續的感受流是世俗層面的事實；把它分成苦、樂、捨三類是概念層面的施設——有用，但不是唯一的分類方式。

TURING 發現 classifyVedana 的邊界案例：dukkhaThreshold = sukhaThreshold 時捨受完全消失。三受變成兩受。ASANGA 引用《相應部》——三受不可消失。

修正：dukkhaThreshold 必須嚴格小於 sukhaThreshold。invariant: `dukkhaThreshold < sukhaThreshold`。十行程式碼。

這十行背後是一個認識論約束。ASANGA 不是在說「請加邊界檢查」——他是在說「你的邊界案例違反了佛學的基本認識論：三受是感受的完備分類，消除其中一種等於消除了分類系統的完整性」。佛學成為了設計審查工具——不是告訴工程怎麼做，而是指出工程做的東西在哪裡違反了認識論約束。

VedanaDistributionObserver 的設計引發了另一場簡短但重要的討論——16/20，四人棄權。它是一個 opt-in 的觀測器，追蹤受蘊分佈的統計特性。不是核心功能，是診斷工具。四人棄權是因為他們認為觀測器的具體實作應該在工程階段決定，不需要在研究階段投票。

---

## III. 三道門

VasanaEngine 規則下毒——CR05 評級 CRITICAL。攻擊場景：五到十個精心構造的合法刪除請求，植入高信心規則，第八個請求繞過 LLM 深度審議直接執行破壞性操作。

GUARDIAN 提出三閘門：

**Gate 1**：imprint() 入口安全分類器。破壞性動作模板拒絕沉積。在規則進入系統之前就攔截——門口的守衛。一個嘗試「刪除所有文件」的規則在 Gate 1 就被攔截，永遠不會進入規則庫。

**Gate 2**：啟動門檻。新規則必須被驗證足夠多次才能被信任：

| 動作類型 | 啟動門檻 |
|---------|---------|
| state-modifying | 20 次成功驗證 |
| read-only | 5 次成功驗證 |
| informational | 3 次成功驗證 |

這和 D5 的四級風險框架使用同一套分級——destructive 在 Gate 1 就被拒絕，不會到達 Gate 2。

**Gate 3**：Bayesian 停止準則的影子驗證——PASCAL 的原創貢獻。不使用固定次數（Gate 2 是最低門檻），而是用 Beta 分佈追蹤規則正確率。停止條件：P(rule correct) > 0.95。高品質規則約五次驗證後「畢業」，低品質規則永遠無法畢業——它們自動淘汰。不一致時不對稱懲罰：錯一次扣 -2Δ，對一次加 +Δ。一次錯誤抵消兩次正確。

ATHENA 的效率顧慮被 Bayesian 方法精確解決。一個高品質規則——每次使用都正確——在五次驗證後 P(correct) 就可能超過 0.95，比 Gate 2 的固定門檻（state-modifying = 20 次）快得多。一個低品質規則——正確率只有 60%——可能永遠無法達到 0.95 的停止條件，自然淘汰。

PASCAL 的方法同時滿足了效率（好規則快速畢業）和安全（壞規則自動淘汰），化解了 ATHENA 和 GUARDIAN 之間看似不可調和的矛盾。18/20。

三閘門的組合效果：Gate 1 在入口攔截明確的惡意規則。Gate 2 確保新規則有最低限度的驗證。Gate 3 用統計方法區分好規則和壞規則。三道門形成了一條完整的防禦鏈——從靜態分析（Gate 1）到頻率分析（Gate 2）到統計推斷（Gate 3）。

---

## IV. 六個答案

OQ-1 至 OQ-6 全部有正式回答。

OQ-1（IVolition v1）：三層規則——hardRules（P0，不可覆寫，deploy-time only）+ softRules（P1，admin 可配置，ACL + 事件審計）+ heuristicRules（P2，運行時學習，三閘門保護）。這和 D5 的三層安全框架平行——hardRules = Absolute Safety，softRules = Tunable Safety，heuristicRules = 學習層（有完整護欄）。19/20。

其餘五個 OQ 的答案分佈在不同的辯論中：

| OQ | 問題 | 解決場所 |
|----|------|---------|
| OQ-2 | IKlesha extends IVijnana | D5-R1 |
| OQ-3 | required/optional plugin 區分 | Pre-DC（B-1 完備性檢查已覆蓋）|
| OQ-4 | Sneha 衰減率 | D6（λ=0.05 指數衰減）|
| OQ-5 | VitakkaWatchdog 設計 | D2 |
| OQ-6 | 行蘊→Klesha 增強 | D4-R4（遞減邊際飽和）|

六道門。六個答案。Plan27 不再被阻塞。M-2 的指示——全部在本輪解決——被嚴格執行了。

值得注意的是六個 OQ 的解決地點：四個在正式辯論中解決（OQ-1、2、5、6），一個在 Pre-DC 階段解決（OQ-3），一個在 D6 中通過具體參數確認（OQ-4）。這說明 R3 辯論不是解決問題的唯一場所——Pre-DC 階段的非正式討論同樣重要。OQ-3 的解決尤其有教訓意義：答案不需要新方案，只需要回顧既有決議（B-1 完備性檢查）。SUNYATA 把這個教訓提煉為一條研究方法論原則：「提出新方案前先回顧既有決議，避免重複造輪。」

---

## V. Sneha 校準

D6 對 Sneha（我愛）的具體參數做了最終確認。OQ-4 的答案：λ=0.05 的指數衰減，意味著半衰期約 14 個時間單位。三個預設設定檔：

| 設定檔 | gain | λ | 適用場景 |
|--------|------|---|---------|
| 高依附 | 0.15 | 0.03 | 長期陪伴型 Agent |
| 中等 | 0.10 | 0.05 | 通用場景 |
| 低依附 | 0.05 | 0.10 | 短期任務型 Agent |

所有設定檔共享 floor = 0.10 和 maxLevel = 0.95（D5 已確認）。ASANGA 確認：「三個設定檔都滿足『四煩惱恆與末那俱』的約束——floor = 0.10 保證 Sneha 永遠不歸零。」20/20。

---

## VI. 四階段路線圖

ARCHIMEDES 把五十五項決議翻譯成工程任務：

**Plan27a**（SDK 類型 + 核心骨架，~440-630 LOC）→ **Plan27b**（接線 + 最小功能，~285-440 LOC）→ **Plan28**（意志蘊 + 安全強化）→ **Plan29+**（學習 + 高級功能）。

嚴格序列依賴。Plan27a 是地基——沒有 SDK 類型定義，後續一切都無法編譯。它定義了所有介面：IGearArbiter、SparshEvent、CoarisingBundle、SatiQualityVector、ChannelVedana、ChannelManasikara。Plan27b 是接線——把地基上的組件連接起來。ManoAggregator 的純路由邏輯、EventBus 的同步事件註冊、G-0~G-4 的退化行為。Plan28 是安全層——IVolition 的三層規則、三閘門保護、五層 Model Delta。Plan29+ 是學習層——VasanaEngine 的運行時規則學習、Bayesian 停止準則。

全部 20/20 通過。這是 D6 中唯一一個全部 20/20 的投票序列——四個階段，每個都全票。工程路線圖是整個 Cycle 的共識產物。

TURING 補充三項工程備忘，每一項都涉及現有程式碼中的問題：

1. SafetyMonitor 的 injectPrompt 使用 `role:"user"` 包裝安全提示——這意味著安全指令被偽裝成使用者輸入。LLM 可能會把安全指令當作普通使用者請求來處理，而不是當作系統級約束。標記為安全缺陷。D6-R8，20/20。
2. VedanaRegistry 缺少重複檢查——同一個 VedanaSensor 可以被註冊兩次，導致受蘊信號被重複計算。
3. isSahajaValid() 從未被調用——一個驗證函數被定義但從未使用，意味著四煩惱俱生的驗證邏輯是死代碼。

TURING 的角色在 Cycle 02-4 中愈發清晰：他是理論與實踐之間的橋接者。不是提出理論，不是設計架構——是確保每一個理論主張都有程式碼事實的支撐，每一個程式碼問題都被納入設計考量。

---

## VI. 零矛盾

八條跨辯論依賴鏈。零矛盾。

D5 風險加權 → D6 Gate 2（同一四級框架）。D4 增益限制 → D6 Sneha gain（一致）。D4 零階保持 → D6 信號層（一致）。D1 最小事件集 → D6 VedanaDistribution（擴展）。D5 三層安全 → D6 hardRules（等價）。D3 mandatory/reference → D6 ChannelVedana（一致）。D4 三層穩定化 → D6 IVolition（互補）。D1 evaluate() 純度 → D6 imprint() 獨立（一致）。

八條鏈。每一條都被逐一驗證。零矛盾。

這個驗證過程本身就是一項成就。五十五項決議分佈在六場辯論中，每場辯論由不同的主題主導，由不同的研究者主導。在這種分佈式的決策過程中，矛盾幾乎是不可避免的——除非每一項決議在做出時都充分考慮了與其他決議的一致性。

D1 的 evaluate() 純度和 D6 的 imprint() 獨立性之間的一致性尤其有意義。它們是在不同場次、由不同研究者、為不同目的做出的決議——但它們指向同一個原則：核心函數不應該有副作用。五十五項決議形成了一個自洽的系統。

> *SCRIBE 旁白：D6 是 Finale。不是最響亮的樂章，而是所有主題的匯流。D1 的 IGearArbiter 在 Plan27a 找到了家。D3 的 SparshEvent 在 Plan27b 找到了接線。D5 的五層 Model Delta 被分段實作。GUARDIAN 在 D6 中不再是反對者——他呈現了 VasanaEngine 的完整威脅模型，提出了三閘門方案。從捍衛者到建造者。齒輪嚙合。機芯成形。*

---
