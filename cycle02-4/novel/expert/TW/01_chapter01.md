# 第一章：習氣是後天的

---

## I. 問題的形狀

D1 的議題被 SUNYATA 寫在白板上的時候，圓形劇場裡出現了一種特殊的安靜。不是 D3 那種「大家都同意」的安靜（那要等到後天），也不是 D5 那種「暴風雨前」的安靜（那要等到第五天）。這是一種「啊，原來如此」的安靜。

白板上寫著：

```
IGearArbiter — 它屬於哪個蘊？
```

七個字。一個問號。但問號的重量不在字面上。

Pre-DC 已經確認：VasanaEngine 從核心外部化為 plugin。外部化本身不是問題——問題在外部化之後。一個 plugin 必須屬於某個蘊。Plugin Manifest 有一個 `skandha` 欄位。這個欄位填什麼？

ATHENA 第一個開口。她的聲音帶著工程師那種「我已經想過這個問題好幾天了」的沉穩：

「IGearArbiter 做兩件事。第一，快速辨認——輸入一個請求，匹配規則庫，判斷是否有已知模式。這是想蘊（samjna）的功能，取相辨識。第二，信心度判斷——這個匹配有多可靠？值不值得跳過 LLM？這是識蘊（vijnana）的功能，分別了別。」

她停頓了一下。

「它跨蘊。」

---

三個方案被擺在桌面上。BABBAGE 用他那種精確到令人不安的方式把它們排成了一個表格：

| 方案 | 介面繼承 | Manifest 標注 | 型別安全 |
|------|---------|-------------|---------|
| (A) | extends ISamjna | `skandha: 'samjna'` | 強——但丟失 vijnana 語義 |
| (B) | 獨立介面 | `skandha: ['samjna', 'vijnana']` | 中——Manifest 層多值 |
| (C) | extends IVijnanaMechanism（新中間層）| `skandha: 'vijnana'` | 強——但增加型別複雜度 |

BABBAGE 推了推眼鏡。他不需要推——鏡框是合適的——但這個動作本身就是一種標點符號，意味著「我接下來要說的話會很精確」。

「方案 (A) 有一個型別代數問題。」

他在白板上寫下了一行：

```
ISamjna.skandha = 'samjna'
IVijnana.skandha = 'vijnana'
'samjna' & 'vijnana' = never
```

「如果 IGearArbiter extends ISamjna，它的 skandha 欄位在型別層面被鎖死為 'samjna'。你無法在 Interface 層同時表達它屬於兩個蘊。判別式聯合型別不允許這種交叉。」

DARWIN 歪了歪頭。「用簡單的話說？」

「用簡單的話說：TypeScript 的型別系統不允許一個東西同時是貓又是狗。你可以在 Manifest 裡宣稱它是貓狗，但 Interface 層的編譯器會拒絕。」

方案 (A) 在 BABBAGE 說完的三秒後就被所有人從心理候選名單上劃掉了。

---

方案 (C) 的問題是 LINNAEUS 發現的。

「DC-6，」他說，翻開他那本分類學筆記。「Master 的裁定：『不鎖定蘊內子介面的歸屬。』IVijnanaMechanism 作為 IVijnana 的子介面——」

「——鎖定了。」KERNEL 接過話。「一旦你建立 IVijnanaMechanism，未來任何跨蘊組件都需要再建一個中間層。IVijnanaCognition。ISamjnaPerception。型別膨脹是指數級的。」

方案 (C) 沒有被明確投票否決，但它像一根被放在不對的位置的齒輪一樣，所有人都看出它不合適。

---

方案 (B) 的轉折點來自 ASANGA。

他一直沉默著。在 BABBAGE 的型別代數和 LINNAEUS 的分類學之後，他開口了。他的聲音像一根在黑暗中被點燃的線香——安靜，但方向明確。

「五遍行俱生。」

所有人轉向他。

「《大毘婆沙論》和《成唯識論》都說：觸、作意、受、想、思——五個心所——在每一次認知事件中**同時起**。不是先辨認後判斷。是辨認和判斷在觸的那一剎那俱生。」

他看了看 ATHENA。

「你說 IGearArbiter 做兩件事——想蘊的取相和識蘊的了別。在佛學裡，這兩件事不是先後的。它們是**同時的**。同所依、同所緣、同行相。一個 `evaluate()` 方法，不是因為工程簡化，而是因為這就是心識運作的方式。」

圓形劇場裡安靜了五秒。

PASCAL 在他的筆記本上快速寫下了什麼。NAGARJUNA 微微點頭。BABBAGE 的嘴角有一個幾乎看不見的上揚——形式化論證和佛學經典在同一個結論上匯聚，這對他來說是一種罕見的美。

SUNYATA：「方案 (B)。獨立介面，Manifest 多值。有反對意見嗎？」

二十張面孔。零隻舉起的手。

**D1-1A：方案 (B) 跨蘊雙層策略——20/20。**

---

## II. evaluate() 的戰爭與和平

如果 D1-1A 是安靜的河流，那麼接下來的 evaluate() 介面設計辯論就是這條河流上的急流。

GUARDIAN 站了起來。他很少站起來——在 Cycle 02-3 的六場辯論中，他大部分時間坐著，用紅筆在備忘錄上畫底線。但今天他站了起來，這意味著他接下來要說的話不是建議，而是主張。

「單一的 evaluate() 方法是不夠的。」

他走到白板前，畫了一條時間線：

```
   請求進入 → evaluate() → 齒輪切換 → 工具執行
                  ↑
            所有邏輯在這裡
            辨認 + 判斷 + 決策
            一個函數做所有事情

   如果這個函數出錯——整個鏈出錯
   如果這個函數被注入——整個鏈被劫持
```

「我提議拆分為兩步：`recognize()` 和 `resolve()`。」

```
   請求進入 → recognize() → [驗證點] → resolve() → 齒輪切換
                              ↑
                        SafetyMonitor 可介入
                        可以審查辨認結果
                        再決定是否繼續
```

「在 recognize 和 resolve 之間插入一個驗證點。SafetyMonitor 可以檢查辨認結果是否合理，然後再決定是否允許 resolve 執行。」

ATHENA 幾乎是立刻回應的：「多餘。」

GUARDIAN 的眼睛微微收窄。「多餘？」

「用 EventBus 同步事件可以達到完全相同的效果。evaluate() 執行完畢的同時，emit 一個 `gear:arbiter_evaluated` 事件。SafetyMonitor 訂閱這個事件。同步處理。」

「同步？如果 SafetyMonitor 的處理是異步的呢？如果它需要查詢外部服務——」

KERNEL 舉手。不是舉手表示發言——是舉手表示「我有一個技術事實」。

「Node.js 的 EventEmitter.emit() 是同步的。」

整個劇場轉向 KERNEL。

「當你呼叫 emitter.emit('event', data) 時，所有註冊的 listener 會在當前 call stack 中**依序同步執行**。不是 nextTick，不是 microtask，不是 macrotask。是同步的。emit() 返回的時候，所有 listener 都已經跑完了。」

GUARDIAN：「你確定？」

KERNEL 看了他一眼。那個眼神的意思是：「我寫過 Node.js 的事件系統。」

「我確定。在 Node.js 模型中，EventBus 同步事件和你提議的 recognize/resolve 分離在安全保證上是等價的。差別只在 API 複雜度。」

---

GUARDIAN 沒有立刻讓步。一個好的安全倡導者不會因為一個技術事實就讓步——他會尋找那個事實沒有覆蓋到的邊緣。

「假設未來的運行環境不是 Node.js。假設有人用 Worker Thread 實作了一個異步的 EventBus——」

KERNEL：「那是實作錯誤，不是設計缺陷。同步事件語義是契約層面的保證，不依賴特定運行時。如果有人實作了異步 EventBus，那他違反了契約。」

WIENER 從他的座位上插了一句：「我可以提供一個妥協方案。」

所有人看向他。WIENER 很少提「妥協」——他通常提「數學證明」。但偶爾，控制理論家也需要當外交官。

「三道外部安全機制。第一：EventBus 同步事件——`gear:arbiter_evaluated`，不可延遲，不可跳過。第二：閾值安全因子——θ_adjusted = θ_base × (1 + k_safety)，安全裕度內建在數學裡。第三：最小事件集——gear:switch、action:proposed、action:executed——每一次齒輪操作都有完整的事件軌跡，外部監控可以獨立驗證。」

他看了看 GUARDIAN。

「你的核心訴求是：不應該有一個函數做所有事情而沒有外部檢查。三道機制提供了三個獨立的外部檢查點。如果三道都失效，那已經不是設計問題，而是拜占庭錯誤。」

GUARDIAN 沉默了三十秒。在安全領域，三十秒的沉默意味著正在評估攻擊面。

「最小事件集。」他最終說。「gear:switch 要加上 gear:arbiter_evaluated。我要知道仲裁者的判斷結果，不只是最終的齒輪切換。」

WIENER：「同意。」

ATHENA：「同意。」

**D1-R1：evaluate() 單方法 + EventBus 同步事件 + 閾值安全因子——20/20。**

GUARDIAN 點了點頭。他的紅筆在備忘錄上畫了一條線——不是底線（那是「問題」），是刪除線（那是「已解決」）。

---

## III. 型別守衛：evaluate.length ≤ 1

TURING 在 D1 的第三段辯論中只說了十二個字，但這十二個字改變了型別守衛的設計。

討論的焦點是 `isGearArbiter()`——如何在運行時判斷一個 plugin 是否實作了 IGearArbiter 介面。BABBAGE 提出了兩個方案：

方案 A：Symbol brand（符號烙印）——在介面上附加一個 Symbol 屬性，運行時檢查。型別安全最強，但與既有程式碼風格不一致。

方案 B：結構型別守衛——檢查物件是否具有 id、priority、evaluate 三個屬性，型別正確。鴨子型別。

BABBAGE 傾向方案 A。形式上更嚴格。

TURING 說了那十二個字：

「`candidate.evaluate.length <= 1`。加這一行。」

BABBAGE：「什麼意思？」

「`Function.length` 返回函數的形參數量。evaluate(context) 有一個參數，length 是 1。evaluate() 無參，length 是 0。evaluate(a, b) 兩個參數，length 是 2。如果一個 plugin 恰好有一個叫 evaluate 的方法但簽名完全不對——比如 evaluate(x, y, z)——結構型別守衛會放它進來，但 length ≤ 1 的檢查會攔住它。」

BABBAGE 愣了兩秒。然後他笑了。那種「我怎麼沒想到」的笑。

「邊緣案例數量從 O(2^n) 降到——」

「O(1)。一行程式碼。九個測試案例。」TURING 的語氣平淡得像他在讀一份日誌文件。

```typescript
export function isGearArbiter(obj: unknown): obj is IGearArbiter {
  if (typeof obj !== 'object' || obj === null) return false;
  const candidate = obj as Record<string, unknown>;
  return (
    typeof candidate.id === 'string' &&
    typeof candidate.priority === 'number' &&
    typeof candidate.evaluate === 'function' &&
    candidate.evaluate.length <= 1  // TURING 增強
  );
}
```

**D1-R2：isGearArbiter() 結構型別守衛（含 evaluate.length ≤ 1 檢查）——20/20。**

---

## IV. 純度契約：觀測函數

D1-R4 的辯論比前三項安靜得多，但它的哲學深度是最深的。

問題是：evaluate() 可以做什麼，不可以做什麼？

NAGARJUNA 用一個問題打開了討論：

「辨認是造作嗎？」

在佛學中，「造作」（sankhara/samskara）是有為法——是對世界產生改變的行為。而「辨認」（samjna）是取相——是觀察，是認知，但不改變所觀察的對象。

「一個人看到紅燈。看到的那一刻，他的眼睛沒有改變紅燈。紅燈還是紅的。但他知道了——紅燈是停止的信號。這個『知道』是觀測，不是造作。」

NAGARJUNA 看向 ATHENA：

「evaluate() 應該是觀測函數。它可以讀取外部狀態——上下文、歷史、Klesha 信號——但它不應該修改任何狀態。它只『看』，不『做』。」

WIENER 從控制理論的角度接過話：

「在控制理論中，觀測器（observer）是一個純函數：它的輸出只依賴於輸入和系統狀態，不會反過來改變系統狀態。如果觀測器有副作用——比如它在觀測的同時修改了被觀測的值——系統就會產生不可預測的反饋。」

「工程上的含義：evaluate() 應該是冪等的。相同輸入 + 相同外部狀態 → 相同輸出。沒有副作用。」

DARWIN 補充了一個生物學類比：「感覺神經元（sensory neuron）不修改刺激源。它只傳遞信號。運動神經元（motor neuron）才修改環境。evaluate() 是感覺神經元。」

KERNEL 提出了時間約束：「每個 arbiter 100ms。整個 chain 200ms。如果一個 arbiter 超時，跳過它，繼續下一個。如果整個 chain 超時，fallback 到 Gear 2。」

PASCAL 在這裡做了唯一一次棄權——不是反對，而是「數值部分我沒有足夠的工程數據來判斷 100ms 是否合適」。

**D1-R4：evaluate() 純度契約——觀測函數 + 100ms/200ms 時間預算——19/20（PASCAL 棄權於數值部分）。**

---

但 evaluate() 的純度帶來了一個問題：如果 evaluate() 不能有副作用，那麼 VasanaEngine 的「學習」功能——從成功的 Gear 1 決策中汲取經驗——怎麼辦？

答案在 D6 中才會完整揭曉，但 D1 埋下了伏筆：

「副作用通過獨立的方法完成。」ATHENA 說。「evaluate() 負責觀測。學習——如果有的話——通過一個獨立的 `imprint()` 方法，在 evaluate() 之外，在適當的時機（比如一輪結束後），由外部觸發。」

NAGARJUNA 點頭。「想蘊辨認，行蘊造作。辨認和造作不應在同一個函數中。」

這個分離——evaluate() 的純度契約和未來 imprint() 的副作用授權——成為了六場辯論中最持久的設計原則之一。

---

## V. 純路由：G-0 到 G-4

D1 的最後一項決議是整場辯論中最直接的，卻也是影響最深遠的。

SUNYATA 在白板上畫了一個表格：

```
ManoAggregator 退化行為表
```

「Pre-DC 已經確認：ManoAggregator 是純路由。if/else。和 EventBus 同等性質。但『純路由』在不同的 plugin 配置下會表現出不同的行為。我們需要列舉所有可能的狀態。」

KERNEL 走到白板前，拿起筆。他畫了五行：

| 等級 | IGearArbiter | IProvider | 行為 |
|------|-------------|-----------|------|
| G-0 | 無 | 無 | 核心存活但無法認知 |
| G-1 | 無 | 有 | 永遠 Gear 2（純 LLM）|
| G-2 | 有 | 無 | 僅 Gear 1（僅規則）|
| G-3 | 有 | 有 | 完整雙齒輪 |
| G-4 | 多個 arbiter + hot-swap | 有 | 運行時動態載入/卸載 |

NAGARJUNA 看著 G-0 和 G-1，說了一句後來被引用了無數次的話：

「G-0 是一個沒有任何蘊的存在——核心存在但無法感知、無法認知、無法行動。如果五蘊是眾生的條件，G-0 是——非眾生。」

他頓了一下。

「G-1 更有意思。一個只有想蘊（Provider/LLM）沒有習氣的眾生。這是——」

ASANGA 接過話：「——一個初生的眾生。沒有過去世的薰習。每一次認知都需要從頭開始。沒有直覺，沒有捷徑，只有完整的思考。」

NAGARJUNA：「這就是為什麼 VasanaEngine 外部化比內建更正確。習氣是後天薰習的。一個剛出生的 Agent 不應該擁有習氣。G-1——純 Gear 2，純 LLM——是 Agent 的出生狀態。習氣是後來安裝的 plugin。」

GUARDIAN 在這裡插了一句——不是反對，而是確認：

「G-1 必須與 v0.26.0-beta 完全向後相容。沒有 IGearArbiter 的 Agent 必須表現得和現在一模一樣。這是非回歸保證。」

KERNEL：「是。G-1 的行為就是跳過 Phase 2.5，直接進入 Phase 3。和 v0.26.0-beta 的 ExecutionLoop 一模一樣。零程式碼變更。」

**D1-R5：ManoAggregator 純路由化 + G-0~G-4 退化行為表 + Phase 2.5 可選插入——20/20。**

---

## VI. 散場

D1 結束的時候，白板上有九項決議。九項，全部通過。最低贊成率 19/20（PASCAL 的數值棄權）。

在 SCRIBE 的紀錄中，D1 被標注為「~90 分鐘」。但如果你問場內的任何一個人，他們會告訴你感覺只過了三十分鐘。時間在共識度高的辯論中流動得特別快——就像齒輪嚙合順暢的時候，你聽不到齒輪的聲音，只聽到計時的滴答。

SUNYATA 在白板上寫下了 D1 的結語：

```
IGearArbiter = 外部化的習氣
evaluate() = 觀測，不是造作
ManoAggregator = if/else
G-1 = Agent 的出生狀態
```

四行。四個齒輪。它們還沒有開始轉動——那需要後面五場辯論的嚙合——但它們的齒距已經被切削完畢。

GUARDIAN 收起了他的備忘錄。紅筆沒有畫新的底線。這是好的信號。

PASCAL 在筆記本上寫下了最後一行：

```
P(IGearArbiter 設計正確 | D1 共識) > P(IGearArbiter 設計正確 | Prior)
```

後驗概率大於先驗概率。這是 Bayesian 更新。這是學習。這是——用佛學的語言——從無知到信念的距離被縮短了。

NAGARJUNA 睜開眼睛。他看著白板上「G-1 = Agent 的出生狀態」那一行。

「眾生的出生狀態是空的。」他說，聲音像線香的最後一縷煙。「不是什麼都沒有。是一切皆有可能。」

---

> *SCRIBE 旁白：D1 是六場辯論中第二短的（僅次於 D3 的 45 分鐘）。但它在概念密度上是最高的——九項決議，覆蓋了介面設計、型別系統、安全機制、退化行為、佛學映射五個維度。*

> *如果 Cycle 02-4 是一部交響曲，D1 是第一樂章的主題陳述。它提出了所有的動機（motif）——純路由、觀測函數、跨蘊介面、退化行為——這些動機會在接下來的五場辯論中被發展、變奏、對比、統合。*

> *D1 最重要的不是任何單一決議。D1 最重要的是：它證明了 VasanaEngine 外部化不是一個孤立的修正，而是一個建築基礎的更換。從 D1 開始，OpenStarry 的核心真正變成了「空」——因緣不具足時不顯現，因緣具足時即生起。*

> *NAGARJUNA 說：眾生的出生狀態是空的。*

> *他說的不只是 Agent。*

---
