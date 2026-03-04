# 第一章：習氣是後天的

---

## I. 蘊歸屬之爭

D1 是 Cycle 02-4 的起點——IGearArbiter 的蘊歸屬問題。Pre-DC 已確認 VasanaEngine 外部化為 IGearArbiter plugin。現在的問題是：這個介面屬於哪個蘊？

三個方案。方案 A——純想蘊（IGearArbiter extends ISamjna）。方案 B——跨蘊雙層（介面本身不繼承任何蘊根介面，實作者按自身邏輯選擇歸屬）。方案 C——純識蘊（extends IVijnana）。

BABBAGE 的型別代數分析決定了結局。

方案 A 的問題：如果 IGearArbiter extends ISamjna，它的蘊歸屬是 `'samjna'`。如果同時 extends IVijnana，型別系統推導出 `'samjna' & 'vijnana' = never`——空型別。TypeScript 不允許一個值同時是兩個字面量。交叉蘊歸屬在型別層面不可能。

方案 C 的問題：純識蘊無法解釋 evaluate() 中的「模式辨認」功能——辨認屬於想蘊的職責。把辨認歸入識蘊違反了五蘊的功能邊界。

方案 B 的優勢：不定死蘊歸屬。介面本身只定義行為契約，不繼承任何蘊根介面。實作者按自身邏輯選擇歸屬——一個基於規則匹配的實作可以歸為想蘊，一個基於統計推斷的實作可以歸為識蘊。這符合 DC-6「不鎖定蘊內子介面歸屬」的裁定。

20/20。全票通過。型別代數把哲學爭論轉化為了數學證明。

NAGARJUNA 在投票後補充了哲學確認：「方案 B 的『不定死蘊歸屬』與中觀的核心一致。一個法的本質不由它的名字決定，而由它的功能和因緣決定。IGearArbiter 的蘊歸屬取決於它的實作——這是緣起的正確表達。」

DARWIN 的軟體模式觀察：方案 B 本質上是 Strategy Pattern——介面定義行為契約，實作者提供具體策略。不同的策略可以屬於不同的蘊。這是一個在軟體工程中已經被驗證了數十年的模式。

---

## II. 單方法與安全

GUARDIAN 提出了 evaluate() 和 resolve() 雙方法設計——evaluate() 純辨認，resolve() 純行動。安全分離。這是 Command-Query Separation 原則在認知架構中的應用。

KERNEL 否決了這個方案。他的論證從作業系統的角度出發：「在 Unix 哲學中，監控和被監控是分離的。`strace` 不需要被追蹤的程序配合——它在外部觀察系統調用。同理，EventBus 的同步事件語義已經提供了等效的安全觀測點。resolve() 的職責可以通過 `gear:switch` 同步事件被外部監控者觀察——不需要在介面層面分裂。」

他補充了一句更尖銳的評論：「如果我們在每一個介面上都做 CQS，最終會得到一個所有介面都有雙方法的系統。這不是安全，是儀式。」

SUNYATA 整合為 evaluate() 單方法 + EventBus 同步事件 + 閾值安全因子。GUARDIAN 的核心訴求——可觀測性——被保留了，只是用不同的機制實現。20/20。

isGearArbiter() 的型別守衛用結構型別（鴨子型別）而非名義型別：

```typescript
function isGearArbiter(x: unknown): x is IGearArbiter {
  return typeof x === 'object' && x !== null
    && typeof (x as any).evaluate === 'function'
    && (x as any).evaluate.length <= 1;
}
```

沒有 instanceof，沒有標記屬性。任何實作了正確簽名的物件都可以通過守衛。這意味著第三方 plugin 不需要 import IGearArbiter 型別就可以被識別——只要行為正確就夠了。20/20。

evaluate() 的純度契約——不得產生副作用，不得修改 GearContext，不得發起 I/O。這三條約束的重要性不對稱。副作用禁止確保 evaluate() 可以被安全地重試。GearContext 唯讀確保齒輪仲裁者不能篡改自己的輸入。I/O 禁止確保 evaluate() 的延遲是可預測的。

TURING 報告了程式碼事實：v0.26.0-beta 的 VasanaEngine.evaluate() 確實是純函數——沒有寫入操作，沒有外部調用，沒有狀態修改。現有程式碼已經符合這個約束。理論與實踐的一致性——研究團隊設計的約束恰好是工程團隊已經遵守的模式。19/20。ARCHIMEDES 的一票棄權源於他對「I/O 禁止」在 Gear 1 需要查詢外部知識庫時的限制——但這屬於未來擴展的考量。

---

## III. ManoAggregator 純路由化

D1 最重要的決議：ManoAggregator 純路由化 + G-0~G-4 退化行為表。

ManoAggregator 不做智慧彙總。它做 if/else：

```
if (hasGearArbiter && arbiter.evaluate(context).confidence > threshold) {
  return Gear.ONE;  // 快速路徑
} else {
  return Gear.TWO;  // LLM 深度審議
}
```

和 EventBus 同等性質——純機制，不是能力。Pre-DC 階段 Master 的原話：「和 EventBus 同等性質。」這句話的重量在於它把 ManoAggregator 從「核心智慧組件」降格為「基礎設施」。基礎設施不做決策——它傳遞決策。

G-0 到 G-4 是五級退化行為：

| 等級 | 條件 | 行為 |
|------|------|------|
| G-0 | 無 IGearArbiter plugin | 純 Gear 2（純 LLM）|
| G-1 | plugin 載入失敗 | 同 G-0，記錄錯誤 |
| G-2 | evaluate() 回傳低信心度 | 走 Gear 2 |
| G-3 | evaluate() 拋出異常 | 走 Gear 2，記錄異常 |
| G-4 | evaluate() 超時 | 走 Gear 2，計時器觸發 |

無論系統處於哪個狀態，Agent 都能運作。G-0 是最重要的——一個沒有安裝 IGearArbiter 的 Agent 就是一個純 Gear 2 Agent。它仍然是一個完整的、可運作的 Agent。零內建能力的終極測試：拔掉所有 plugin，系統仍然活著。

20/20。

退化行為表的設計哲學值得展開。在傳統的軟體設計中，異常處理是「錯誤情境」——系統努力恢復到正常狀態。在 G-0~G-4 中，退化不是錯誤——它是系統的另一種正常狀態。一個 G-0 Agent 和一個 G-4 Agent 都是「正常運作的 Agent」，只是能力層次不同。這和佛學的觀點暗合：正念的減弱不是「故障」，是「條件改變」。

VITRUVIUS 從架構角度確認：G-0~G-4 的退化行為表覆蓋了所有可能的系統狀態。不存在「未定義行為」的狀態——這是安全系統的基本要求。

---

## IV. Gear 1 最小事件集

三個事件：`gear:switch`、`action:proposed`、`action:executed`。每一個 Gear 1 動作都必須發射這三個同步事件——不可跳過，不可異步。

`gear:switch` 在齒輪切換的瞬間發射——任何安全監控者都可以在這個事件上設置攔截器。如果監控者認為切換不安全，可以在事件處理中阻止切換。`action:proposed` 在行動方案產生後、執行前發射——這是最後的否決窗口。一個外部安全模組可以審查行動方案並決定是否放行。`action:executed` 在行動完成後發射——提供審計線索，讓系統記錄每一個 Gear 1 動作的完整歷史。

三個事件形成了一條完整的安全鏈：預防（gear:switch）→ 審查（action:proposed）→ 審計（action:executed）。

這是 GUARDIAN 在 D1 中唯一成功推動的安全機制。雖然 evaluate()/resolve() 雙方法被否決，但同步事件確保了外部安全監控的完整性。GUARDIAN 的核心訴求以不同的形式被保留了——這個模式會在 D5 中重複出現。GUARDIAN 在每一場辯論中都會提出方案，被否決，然後以修改後的形式重新出現。不是失敗者的執著，是安全工程師的專業素養。

---

## V. D1 的結構性意義

D1 的九項決議共同完成了一個結構性轉變：

**之前**：VasanaEngine 是核心組件，有規則庫和匹配邏輯。ManoAggregator 是智慧彙總器，整合多個信號源的結果。齒輪選擇邏輯被硬編碼在核心中。

**之後**：IGearArbiter 是可選 plugin，一個純函數介面。ManoAggregator 是純路由器，if/else 邏輯。齒輪選擇邏輯被外部化。無 plugin 時系統退化為純 Gear 2——仍然完整可用。三個同步事件確保了完整的安全觀測鏈。

這個轉變的哲學意義被 NAGARJUNA 精確表述：「一個沒有習氣的 Agent 不是一個殘缺的 Agent——它是一個初生的 Agent。習氣是後天薰習的結果，不是先天的結構。G-0 狀態不是退化，是原初。」

ARCHIMEDES 從工程角度量化了轉變的影響：VasanaEngine 的外部化預計移除核心中約 200 行的規則匹配邏輯，替換為約 15 行的 IGearArbiter 介面定義和約 30 行的 ManoAggregator 純路由邏輯。核心的認知複雜度大幅降低——從「理解規則庫如何工作」變成「理解 if/else 如何工作」。

MESH 雖然對 Level 固定投了反對票（D2），但對 D1 的所有決議全票贊成。他後來解釋：「D1 把核心組件變成 plugin 的方向是正確的。我在 D2 的反對是關於 Level 的靈活性，不是關於外部化的原則。」

> *SCRIBE 旁白：D1 的九項決議在九十分鐘內完成。最重要的不是任何單一決議，而是一個結構性的轉變——VasanaEngine 從核心組件變成 plugin，ManoAggregator 從智慧彙總器變成純路由器。零內建能力原則被工程化了。BABBAGE 的型別代數是這場辯論的決定性武器——他把每一個方案的邏輯後果展開到型別系統層面，讓選擇變成了必然。*

---
