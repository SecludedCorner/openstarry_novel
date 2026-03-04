# 第三章：三和合的寧靜

---

## I. 最短的辯論

六場辯論中有長有短，有暴風雨有微風。D5 是暴風雨——一百五十分鐘，六票反對，GUARDIAN 和 ATHENA 的正面交鋒。D1 是急流——九十分鐘，九項決議，概念密度最高。D2 是一場類比的競賽——CPU、觀測器、有分心。

D3 是微風。

四十五分鐘。五項決議。全部一致通過。零爭議。

SUNYATA 事先知道會是這樣。在他的辯論準備筆記中，D3 被標注為「可能快速通過」。R1 的八份獨立報告和 R2 的八份交叉審閱在觸與作意的基本性質上完全一致——觸是事件協定，作意是 read-only 快照，觸的數學模型是布林邏輯（root AND object AND consciousness），第一版不判斷作意品質。

這就是為什麼 D3 在辯論序列調整中被提前到第二場——它的共識度高到可以在 D1 之後直接跑完，為 D4 提供「觸的事件模型已確認」的基礎。

但「沒有爭議」不等於「沒有深度」。

D3 的深度不在辯論中——在辯論之前。當所有人在 R1 和 R2 中獨立到達相同結論的時候，深度就已經完成了。D3 只是確認這個深度的存在。

---

## II. 定義性與附隨性

SUNYATA 宣布辯論開始後，先確認了五項既有共識。觸的本質。作意的本質。觸的數學模型。作意品質的延後。顯式建構的選擇。

五項。零異議。NAGARJUNA 簡短地確認了佛學基礎——觸是三和合的功能性結果，不是獨立實體，更接近協定而非事件。ASANGA 確認了作意——「作意在觸的那一刻已經確定了心的朝向。跨心念尺度的品質變化推遲到未來版本是正確的，因為這需要元認知能力。」VITRUVIUS 確認了工程可行性——SparshEvent 目前是純類型定義，零 runtime 使用，Plan27b 需要在 `processEvent()` 入口處建構它，大約 10-20 行程式碼。

然後進入第一個待決事項：SparshEvent 應攜帶哪些欄位？

---

TURING 先確認了程式碼事實。SparshEvent 在 `packages/sdk/src/types/coarising.ts` 中定義。三個欄位：`root`（根門）、`object`（外部刺激對象）、`consciousness`（認知領域識別）。沒有 `timestamp`，沒有 `sessionId`。

他順帶做了一個事實修正——R07 報告在 §4.2 中使用了 `timestamp: t₁` 這個欄位。「這是事實錯誤。SparshEvent 不存在 timestamp 欄位。R07 虛構了此欄位。」

TURING 的事實修正在 Cycle 02-4 中出現了不止一次。他在 D4 中也修正了一個虛構的 `ISensation.ingestToolResult()` 方法。這些修正很少引起戲劇性的討論——它們只是被記下來，然後辯論繼續。但每一次修正都像是從地基中取出了一塊不屬於那裡的石頭。取出後，地基反而更穩了。

---

三個選項擺在桌上。BABBAGE 排成了表格——這是他的本能，他在看到三個以上的選項時會自動產生表格的衝動。

選項 A：維持三欄位。語義純粹，只描述三和合。
選項 B：加入 timestamp。四欄位，提供時序排序。
選項 C：加入 timestamp + sessionId。五欄位，支持多 Agent 追溯。

NAGARJUNA 的分析很短。觸是根、境、識三和合——這是觸的定義。時間戳不是觸的定義要素。「但在工程脈絡中記錄『何時發生』是有用的附加資訊。從佛學角度，加不加 timestamp 不改變觸的本質。這是純工程決策。」

ASANGA 同意。「在阿毘達磨的時序分析中，『什麼時候發生』由心路過程的位置決定，不需要額外的時間標記。但工程系統不是阿毘達磨——它需要外部時鐘。佛學對此問題保持中立。」

佛學家們在這裡做了一件在六場辯論中反覆做的事——明確標記出他們的「管轄範圍」。觸的三和合定義？佛學有話要說。Timestamp 的有無？佛學保持中立。這種自我限制不是軟弱——是精確。它讓工程討論在佛學框架允許的空間裡自由展開。

---

轉折來自 LINNAEUS。

在二十位學者中，LINNAEUS 不是最常發言的——他的專長是分類學和本體論，只在「這個東西應該被歸為什麼類別」的問題上才會出手。但當他出手的時候，他的觀點往往是決定性的。

「SparshEvent 的三個原始欄位是觸的**定義性屬性**（svabhava-laksana）。timestamp 是**附隨性屬性**（samprayukta-laksana）。」

他停頓了一下，確保所有人都聽到了這兩個術語。

「在阿毘達磨分類中，定義性屬性和附隨性屬性有本質區別。把 timestamp 放在 SparshEvent 中，等於把附隨屬性混入定義。更乾淨的做法是讓 timestamp 留在 CoarisingBundle 層級——Bundle 已經有 timestamp，不需要在 SparshEvent 重複。」

BABBAGE 立刻回應：「但如果需要 SparshEvent 自己的時間戳用於診斷——觸到 Bundle 的組裝延遲——可以作為 optional 欄位。」

他修正了建議：

```typescript
interface SparshEvent {
  readonly root: string;
  readonly object: unknown;
  readonly consciousness: string;
  readonly timestamp?: number;  // optional: 非觸的定義要素
}
```

Optional。問號。

NAGARJUNA 認可了這個設計：「`timestamp?: number` 的 optional 在佛學上是最精確的。觸的本質是三和合，時間不是觸的本質。但在工程脈絡中記錄何時發生是有用的附加資訊。Optional 恰好表達了『非本質但有用』的語義。」

---

LINNAEUS 的「定義性 vs 附隨性」區分在 D3 中只佔了幾分鐘的討論時間。但它的影響遠超 D3 本身。

在 D6 中，當 NAGARJUNA 提出 `v_true → v_latent` 的語義修正時，他用的就是同樣的框架——`v_true` 暗示存在「客觀真實」的效價，這是一個錯誤的定義性屬性。`v_latent`——潛在效價，agent 的內在估計——才是正確的定義。

在 D5 中，當 BABBAGE 分析 IKlesha 的蘊歸屬時，他用「判別式聯合型別不允許 'samjna' & 'vijnana' = never」否決了方案 A——那是同一個型別理論工具在不同語境中的應用。

分類學看起來是靜態的——給東西起名字，放進正確的抽屜。但在 D3 中，LINNAEUS 展示了分類學的動態面：一個好的分類框架不只告訴你東西在哪裡，它還告訴你**什麼不應該在那裡**。

**D3-1：SparshEvent 三必填 + timestamp 可選 + 不加 sessionId——9/9。**

---

## III. 一對一

D3-2 的議題更加根本：每個認知 tick 是否只有一個 SparshEvent？

ASANGA 從阿毘達磨的心路過程（citta-vithi）分析。在上座部阿毘達磨中，一個完整的心路過程只處理一個所緣（arammana）。如果在心路進行中另一個感官對象出現，它必須等待當前心路結束。

「映射到工程：一個認知 tick 處理一個觸。多個所緣意味著多個心路，也就是多個 tick。」

NAGARJUNA 補充了中觀視角：「觸是緣起法——它依根、境、識三者而生起。三個特定的因緣聚合產生一個特定的觸。不同的因緣聚合產生不同的觸——它們不應被混為一個觸，就像不同的三角形不能被混為一個三角形。」

HERACLITUS 提出了工程上的邊界情況——同一個 `processEvent()` 呼叫中，LLM 可能回傳多個 tool_calls。每次工具執行是否算一個新觸？

VITRUVIUS 給出了分階段的建議：Phase 1 採用嚴格一對一——每次 `processEvent()` 恰好一個 SparshEvent。工具執行不產生新的觸，共享同一個觸的脈絡。Phase 2 再擴展為一對多，允許工具執行後的「意門自觸」（mano-dvara sparsha）。

ASANGA 確認了分階段的佛學合理性：「Phase 1 的一對一對應六根接觸六境的基本模式。Phase 2 的子觸對應意門自觸——意識以自身的產出為所緣。兩者都是合法的認知模式，但複雜度不同。」

KERNEL 補充了作業系統角度——一對一在排程上最簡單。一個 SparshEvent，一個 CoarisingBundle，一次完整的五蘊迴圈。沒有並發控制問題，沒有 Bundle 合併問題。

**D3-2：Phase 1 嚴格一對一 + Phase 2 擴展為一對多——9/9。**

---

## IV. 因果的種子

D3-3 的議題是 PENROSE 在交叉審閱中提出的——因果追溯性。

他的問題很具體：如果 Agent 執行了 `rm -rf /important-data/`，事後分析需要回答——是哪個觸事件觸發了這個認知鏈？如果 SparshEvent 在 GC 回收後消失，這個問題就無法回答。

三個方案被列出。

方案 α——全量日誌。每個 SparshEvent 建構時自動寫入持久化日誌。完整但笨重。

方案 β——影子記錄。在 EventBus 上 emit 結構化的因果事件，由 Sati 或 CausalTracer plugin 消費。精確但需要新增事件類型。

方案 γ——CoarisingBundle 自帶觸的快照。零額外機制。Bundle 的 `sparsha` 欄位就是因果記錄。但如果沒有消費者持有引用，Bundle 同樣被 GC。

NAGARJUNA 的評估帶著佛學的精巧：

「方案 α 過度——等於試圖留住每一刻的觸。觸的本質是瞬時的，試圖留住一切是一種執著。」

「方案 β 最精準——觸本身消滅，但其因果印記留在因果鏈中。這完全符合唯識學的種子理論：觸消滅了，但它在阿賴耶識中留下了種子。」

「方案 γ 也可接受——Bundle 是觸的結果狀態，而非觸本身。」

最終的折中來自 KERNEL。他建議在 Plan27b 的 SparshEvent 建構點 emit 一個 EventBus 事件。目前不需要消費者——但為未來的 CausalTracer 或 SatiMonitor 預留了擴展點。

「成本：一行 `bus.emit()` 呼叫。效益：完整的擴展性。」

ARCHIMEDES 確認了工程可行性——大約 5 行程式碼（LOC）。完全在 Plan27b 範圍內。

**D3-3：CoarisingBundle 快照 + EventBus 預留擴展點——10/10。**

---

## V. 只有觸是必須的

D3-4 回到了一個 DC-8 的裁定——CoarisingBundle 的五遍行為「參考設計」（reference design）。LINNAEUS 再次出手，定義了「參考設計」的精確邊界。

他畫了一條線。線的上方是 Mandatory——核心必須保證的。線的下方是 Reference——核心提供但不強制的。

Mandatory：SparshEvent 型別定義、CoarisingBundle 型別定義、`createCoarisingBundle()` 工廠函數、SahajaContract 品質約束、`Object.freeze()` 不可變語義。

Reference：四個 Channel——vedana、samjna、cetana、manasikara——全部是 optional。Plugin 未提供時為 `undefined`。

BABBAGE 形式化了這個邊界：

```
Mandatory: ∀ bundle: bundle.sparsha ≠ undefined
           ∀ bundle: Object.isFrozen(bundle) = true
           ∀ bundle: bundle.timestamp ∈ Number

Reference: ∀ channel ∈ {vedana, samjna, cetana, manasikara}:
           bundle[channel] ∈ Channel | undefined
```

`sparsha` 是唯一的 mandatory Channel。觸是認知啟動的前提，沒有觸就沒有認知。其餘四個 Channel 是 optional——如果某個蘊的 plugin 尚未載入或不適用，對應的 Channel 可以是 `undefined`。

VITRUVIUS 把這個設計與 B-1 完備性檢查聯繫起來——完備性檢查報告哪些蘊有 plugin、哪些沒有，但不阻止系統運行。「一個只有觸和受蘊但沒有想蘊 plugin 的 Agent 仍然可以運行——它能感受但不能辨認。」

ASANGA 在這裡說了一句被後來反覆引用的話：

「五遍行俱生是佛學理想，工程允許降級。」

他引用了 Master 的精神——「Agent Core 提供讓五蘊 plugin 因緣和合組合出想要的應用」。因緣具足則五遍行齊備，因緣不足則有所缺漏，但核心本身不強制。

這與 D1 的 G-0 到 G-4 退化行為表形成了對稱。D1 說：沒有 IGearArbiter 的 Agent 是 G-1——純 LLM，出生狀態。D3 說：沒有完整五蘊 plugin 的 Agent 仍可運行——只是認知能力降低。

兩者表達的是同一個原則：**核心是空的。能力來自 plugin。因緣具足時生起，因緣不具足時不顯現。**

**D3-4：sparsha-only mandatory + 四 Channel reference + 五遍行俱生允許降級——10/10。**

---

## VI. 作意的擴展點

D3-5 是最後一項——ChannelManasikara 的欄位設計。兩個核心欄位已經在 SDK 中定義：`focus`（注意力焦點）和 `intensity`（注意力強度）。

ASANGA 確認了佛學映射——作意的兩個功能：「警心」（cetasa abhoga，喚醒心、使心活躍，對應 intensity）和「引心為業」（manasikara-karman，將心引向特定所緣，對應 focus）。兩個欄位已覆蓋作意的基本功能。如理/非如理的判斷——那是元認知層面的事，不應在基本快照中。

BABBAGE 建議加入 `dimensions?` 擴展點，與 ChannelVedana 的組合模式保持一致：

```typescript
interface ChannelManasikara {
  readonly focus: string;
  readonly intensity: number;
  readonly dimensions?: readonly ManasikaraDimension[];
}
```

未來 plugin 可以通過 `dimensions` 擴展作意的描述——例如 `{ name: 'source', value: 'user-input' }` 或 `{ name: 'priority', value: 0.8 }`。

NAGARJUNA 認可：「作意的引心方向不僅僅是朝向何處，還包括為何朝向此處、朝向的持續程度等微細面向。這些在第一版不需要填充，但資料結構預留空間是正確的。」

VITRUVIUS 提出了 Plan27b 的最小實作——`focus` 從 InputEvent.source 或 user message 提取，`intensity` 預設 1.0（focal attention）。大約 10 行程式碼。

**D3-5：focus + intensity + dimensions? 可選擴展——10/10。**

---

## VII. 四十五分鐘

D3 結束了。四十五分鐘。五項決議。全部一致。

在六場辯論中，D3 的工程影響最小——大約 50 行程式碼（LOC），是六場辯論中最少的。沒有新介面，沒有新的型別層次，沒有跨蘊的歸屬爭議。SparshEvent 加一個 optional 的 timestamp。ChannelManasikara 加一個 optional 的 dimensions。CoarisingBundle 的 mandatory/reference 邊界被精確定義。

但 D3 的概念影響是深遠的。

LINNAEUS 的「定義性 vs 附隨性」區分成為了一個反覆使用的分類工具——D6 的 `v_true → v_latent` 語義修正、D1 的 Manifest 多值 skandha、D5 的四煩惱構成論，都可以追溯到 D3 中確立的「什麼是本質、什麼是上下文」這個基本問題。

ASANGA 的「五遍行俱生是佛學理想，工程允許降級」成為了 OpenStarry 佛學映射的一般原則。不是「完美複製佛學理論」，而是「理論提供方向，工程決定程度」。

PENROSE 的因果追溯問題——觸的 fire-and-forget 語義與工程上的事後分析需求之間的張力——被優雅地解決了。不是改變觸的本質（那是佛學不允許的），而是在觸生起的那一刻留下一個擴展點（那是工程的責任）。觸消滅了，但種子留下了。

---

SCRIBE 在記錄中寫道：

> *D3 是六場辯論中唯一可以用「和諧」來形容的一場。不是因為沒有分歧——分歧在 R1 和 R2 階段就已經被解決了。而是因為到了 D3，所有人對觸和作意的理解已經收斂到一個足夠小的區域，辯論變成了精確的校準而非方向性的爭執。*

> *如果 D1 是主題陳述（exposition），D2 是發展部（development），D3 是——*

> *間奏曲（intermezzo）。*

> *交響曲中的間奏曲不是休息。它是調性的轉換、情緒的過渡、下一個樂章的準備。D3 確認了觸和作意的設計——而觸是所有認知事件的起點。D4 的行蘊流向以觸為起點。D5 的閾值框架以觸帶來的受蘊評估為基礎。D6 的受蘊工程以觸→受的因果鏈為前提。*

> *D3 的安靜不是空洞。D3 的安靜是基礎的堅固。*

---

SUNYATA 沒有在白板上寫 D3 的結語。他只是在五項決議下面畫了一條線，然後看了看時間。

四十五分鐘。他原本預估三十分鐘。多出的十五分鐘花在了 PENROSE 的因果追溯問題上——那是預料之外的深度。

他看了看辯論日程。D1 已完成。D3 已完成。D4 已完成。明天是 D2——正念架構。後天是 D5——煩惱與安全。最後是 D6——受蘊工程。

三場已過，三場待來。

前三場辯論（D1、D3、D4）在 SUNYATA 的筆記中被標注為「地基」——觸的事件模型、齒輪仲裁者的蘊歸屬、行蘊的流向約束。這些是系統最底層的設計決策，像混凝土一樣硬化之後就不再容易修改。

後三場辯論（D2、D5、D6）被標注為「上層建築」——正念的架構映射、安全與閾值框架、受蘊的工程實作。它們建立在前三場的基礎之上，但它們的設計空間更大，爭議也更大。

D5 尤其令 SUNYATA 警惕。GUARDIAN 在 D1 中讓步了——evaluate() 單方法加上三道外部安全機制。但 SUNYATA 知道 GUARDIAN 的讓步不是放棄，而是積蓄。D5 的議題——煩惱、安全、閾值——正好是 GUARDIAN 最核心的關切。

那場辯論會很長。SUNYATA 已經知道了。他看了看 GUARDIAN 的座位。GUARDIAN 正在翻閱他的紅色封面安全備忘錄，紅筆在紙面上畫了新的底線——不是刪除線，是底線。底線意味著「問題」。

D3 的寧靜是暫時的。

但暫時的寧靜也有它的價值。就像在暴風雨來臨之前，工匠會檢查所有的鉚釘是否到位——D3 確認了觸和作意的鉚釘。它們到位了。牢固。

接下來的風暴可以來了。

---

> *SCRIBE 旁白：六場辯論的情緒曲線如下——*

> *D1 = 集中（九項決議，概念密度最高）*
> *D3 = 寧靜（五項決議，全場零爭議）*
> *D4 = 深沉（行蘊流向、WIENER 的穩定性證明，數學最密集）*
> *D2 = 靈動（類比的競賽，CPU/觀測器/有分心）*
> *D5 = 暴風（一百五十分鐘，六票反對，三次僵局）*
> *D6 = 收束（十六項決議，工程味最濃，零反對票）*

> *每一場辯論的情緒都不一樣。但如果你把六場辯論排在一起看——*

> *它是一部交響曲。*

> *D1 是第一樂章（Allegro con brio）——快板，有力，主題陳述。*
> *D3 是間奏曲（Intermezzo）——短小，安靜，過渡性。*
> *D4 是第二樂章（Adagio）——慢板，深沉，數學最密集。*
> *D2 是第三樂章（Scherzo）——諧謔曲，靈動，類比的遊戲。*
> *D5 是第四樂章（Allegro molto）——急板，戲劇性最強，衝突與解決。*
> *D6 是終曲（Finale）——所有動機回歸，統一主題再現。*

> *D3 的間奏曲很短。但沒有間奏曲的交響曲——*

> *只是噪音。*

---
