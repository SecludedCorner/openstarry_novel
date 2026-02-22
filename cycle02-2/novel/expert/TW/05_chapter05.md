# 第五章：四道裁定

---

ARCHIMEDES 坐直了。

在前三章的 A 類討論中，他的脊椎保持著一種克制的角度：前傾十五度，手指偶爾敲桌面，但節奏收斂，像一個帶著工具箱的建築師被安排在觀眾席，等著哲學家們討論完地基的方向。他聽過 BABBAGE 劃掉等號的那條線，聽過 ASANGA 在「我見/我慢/我愛/我癡」四煩惱上的終裁，聽過 LINNAEUS 把 IIdentity 從「屬=種」拆分成「屬⊃種₁,種₂,種₃,種₄」的分類修訂，聽過 SYNTHESIST 在追溯 Cycle 02 最得意時刻時那種葬禮前注視遺容的肅穆。

他全程帶著工具箱坐在那裡。箱子沒打開。

那個等待結束了。

---

SUNYATA 手裡拿著一份新的議程表，薄薄的一頁紙，四行字。

「A 類修正用了三個章節。」他說。聲音平穩如常。石子。深潭。「從因果鏈到識蘊子類別，從觀察者分離到 EgoFramework 的歸屬。那些是哲學的修正——告訴我們什麼是對的。」

「現在進入 B 類。Master 對我們四個工程問題的裁定。這是從哲學轉向工程的時刻。」

---

ARCHIMEDES 的手指在桌面上敲了一下——清脆的、帶著期待的。

「我等這一刻很久了。」他說。

劇場裡響起幾聲低笑。他們都知道 ARCHIMEDES 在 A 類討論中的狀態：一個帶著工具箱的人，坐在一群辯論建築美學的哲學家中間。他的工具箱裡是什麼？型別定義。介面簽名。影響矩陣。分階段計畫。每一件工具都在等待被使用的場合。

SUNYATA 微微點頭。「B-1。VedanaPlugin 可選，以及五蘊完備性檢查。」

---

> *SCRIBE 旁白：從 A 類到 B 類的轉場，像是一場交響樂從慢板（Adagio）進入快板（Allegro）。A 類討論的節奏是沉思的——ASANGA 的城市比喻、BABBAGE 的刪除線、NAGARJUNA 的命名天平——每一個議題都需要時間發酵。你必須等墨水滲透紙張，等概念的邊界在反覆辯論中慢慢顯現。*

> *B 類不同。B 類的節奏是決策的。Master 已經裁定了。我們的任務不是辯論對錯，而是把裁定轉化為設計。ARCHIMEDES 等了三個章節。現在輪到他了。*

> *我注意到他的手指只敲了一下。不像在 A 類討論中那種「壓住發言欲望」的節奏性連敲。這一下更像是信號——工具箱的鎖扣被打開的聲音。*

---

SUNYATA 讀出了 Master 的原話。

「『有一些 plugin 已經繼承此 plugin 了。如上面所說，agent 只要完備就應該能啟動。但是或許也需要開發者模式或某一些模式。是需要可選的，agent 不完備也可啟動，只是需要提醒。』」

他放下紙。

「三個關鍵詞。可選。完備。提醒。」

---

KERNEL 的手已經伸向了他那疊類比卡片。翻了兩張——不對——又翻了一張——抽出第四張。左側寫著什麼，SCRIBE 看不清。右側是空白的。他在等一個配對。

「POST。」他說，站了起來。聲音帶著一種在前三章壓抑了很久的確定性——OS 專家終於站在了自己的領地上。

他走到劇場中央。沒有使用投影。他用的是卡片和聲音。

「Power-On Self-Test。一台電腦加電的那一瞬間，CPU 執行的第一條指令。在 x86 架構上，那條指令在 reset vector——位址 `0xFFFFFFF0`——跳轉到 BIOS 或 UEFI firmware 的入口。然後開始硬體枚舉。」

他翻了翻卡片，在空白處寫下序列：

```
POST 硬體枚舉順序（典型 x86）
───────────────────────────────
1. CPU 自檢      — registers, ALU, cache
2. 記憶體自檢     — 逐行掃描 RAM
3. 晶片組         — 南北橋 / PCH
4. 顯示卡         — 初始化 video output
5. 儲存控制器     — SATA/NVMe 枚舉
6. 網路卡         — PXE boot 可選
7. 音效卡/USB     — 次要外設
8. 交給 bootloader — GRUB / systemd-boot
```

「這個順序不是隨意的。」KERNEL 的聲音沉穩，帶著一種背過整本 Intel SDM 的人特有的自信。「它遵循**依賴樹**。CPU 是一切計算的基礎——沒有 CPU，後續枚舉無法執行。記憶體是所有數據的容器——沒有 RAM，firmware 連自己的工作區域都沒有。這兩項是硬性依賴（hard dependency）。後續項目是軟性依賴（soft dependency）。」

他翻了翻卡片。

「在 `systemd` 的語言裡——」

他寫了兩行：

```
Requires=cpu.target memory.target    # 硬性依賴：缺一不啟動
Wants=display.target network.target  # 軟性依賴：缺了降級運行
```

「`Requires` 表示硬性依賴。如果依賴的 unit 啟動失敗，當前 unit 也必須失敗。`Wants` 表示軟性依賴。依賴的 unit 可以失敗，當前 unit 仍然啟動。Linux 的整個服務管理就建立在這兩個關鍵詞的區分之上。」

他把三張卡片排成一列。

「硬性依賴和軟性依賴的區別。五蘊就像這些硬體組件。」

他看向全場。

「但 Master 的裁定告訴我們一件微妙的事——Agent 的五蘊全部是 `Wants`，沒有 `Requires`。」

BABBAGE 抬起頭。「沒有硬性依賴？」

「沒有。」KERNEL 確認。「Master 說的是：『agent 只要完備就應該能啟動。但 agent 不完備也可啟動，只是需要提醒。』這意味著五蘊中任何一個的缺失都不是致命的。不完備 ≠ 無法啟動。不完備 = 降級啟動。就像沒有顯示卡——text mode。沒有網路卡——離線模式。沒有音效卡——靜音。系統是活的，只是功能受限。」

他停頓了一下，補充了一個更精確的類比。

「如果你想要一個更貼切的 Linux 啟動類比：kernel 啟動後調用 `init` 進程——在現代 Linux 上就是 `systemd`——它讀取 unit files，逐一拉起服務。如果 `NetworkManager.service` 啟動失敗，系統不會 kernel panic。它會記錄一條 `WARNING` 級別的日誌，標記服務為 `failed`，然後繼續啟動其他服務。」

他在卡片上補了一行：

```
systemd 降級啟動 ←→ Agent developerMode 降級啟動
    失敗的 unit 被標記但不阻塞     缺少的蘊被記錄但不阻塞
    journalctl 可查詢失敗原因      SkandhaCompletenessReport 可查詢缺失
```

---

ARCHIMEDES 已經在畫了。

KERNEL 還沒說完，他的工程筆記上就出現了一個介面的雛形。他的筆速很快——不是潦草，而是一種長年訓練出來的速記：只寫關鍵型別、關鍵欄位、關鍵方法，省略所有裝飾。但這一次，他停下筆，重新開始。

「KERNEL 的類比已經給了我完整的結構。」他說。聲音務實、清晰，每一個字都像一塊磚。「讓我把它翻譯成 TypeScript。」

他站了起來——他很少站起來，ARCHIMEDES 的風格是坐在工作台前畫圖——但這一次他站起來了，因為他要展示的不是草圖，而是可以直接進入 codebase 的型別定義。

```typescript
/** 五蘊完備性報告 — 設計靈感：BIOS/UEFI POST (Power-On Self-Test) */
interface SkandhaCompletenessReport {
  readonly rupa:     { present: boolean; components: string[] };  // 色蘊: IUI/IListener
  readonly vedana:   { present: boolean; components: string[] };  // 受蘊: ISensation
  readonly samjna:   { present: boolean; components: string[] };  // 想蘊: IProvider
  readonly samskara: { present: boolean; components: string[] };  // 行蘊: ITool
  readonly vijnana:  { present: boolean; components: string[] };  // 識蘊: IGuide/IVolition/IIdentity/IReflection
  readonly isComplete: boolean;
  readonly missing: string[];
}
```

他舉起筆記。

「SkandhaCompletenessReport。五蘊完備性報告。」每一個字都像一塊磚。「五個蘊，每個蘊一個欄位。布林值——有或沒有。組件列表——有的話，有哪些。注意 `vijnana` 欄位——經過 A-2 的修正，識蘊不再是單一的 IIdentity，而是 IVijnana 的子類別集合：IGuide、IVolition、IIdentity、IReflection。完備性檢查需要反映這個修正。」

他看向 KERNEL。

「你的硬體檢查。POST。只不過檢查的不是 CPU 和記憶體，是色蘊和識蘊。」

---

KERNEL 點頭。然後他做了一件事——他在那張空白的卡片右側寫了一行字。SCRIBE 終於看清了卡片的格式：左邊是「作業系統概念」，右邊是「OpenStarry 映射」。

左邊：`POST (Power-On Self-Test)`
右邊：`SkandhaCompletenessReport`

他在下面又加了一行：

左邊：`systemd unit dependency (Requires/Wants)`
右邊：`skandha hard/soft dependency (isComplete/developerMode)`

他把卡片放回那疊卡片中。兩個配對。一張卡片。

---

TURING 的螢幕亮了。一段骨架程式碼——他的風格：先骨架，後血肉。但這一次的骨架比 Cycle 02 的任何一段都更完整。

```typescript
// 正式模式 ≈ systemd Requires | 開發者模式 ≈ systemd Wants
interface StartOptions {
  developerMode?: boolean;  // 允許不完備啟動（若蟲模式）
}

async start(options?: StartOptions): Promise<void> {
  const report = this.checkSkandhaCompleteness();

  if (!report.isComplete) {
    const missingMsg = `Agent 五蘊不完備：缺少 ${report.missing.join(', ')}`;

    // 無論哪種模式，都發送事件通知所有監聽者（含協調層 daemon）
    this.bus.emit({
      type: 'agent:skandha_incomplete',
      timestamp: Date.now(),
      payload: { report, developerMode: !!options?.developerMode },
    });

    if (options?.developerMode) {
      logger.warn(`[DEV MODE] ${missingMsg}`);  // 降級啟動 ← degraded.target
    } else {
      logger.error(missingMsg);
      throw new Error(missingMsg);  // 拒絕啟動 ← emergency.target
    }
  }
  // ... 正常啟動流程 ...
}
```

「AgentCore.start()。」TURING 說。聲音冷靜如常。「注意事件發送的位置——在分支判斷之前。無論是哪種模式，`agent:skandha_incomplete` 事件都會被發出。這符合事件驅動架構的基本原則：通知（notification）和控制（control）分離。事件是通知——所有監聽者（包括 B-4 的協調層 daemon）都會收到。Exception 是控制——決定是否繼續啟動。」

---

DARWIN 微微前傾。「開發者模式是一種演化的中間態。」

幾道目光轉向他。

「不完全變態（hemimetabolism）。」他展開了。「昆蟲的變態發育有兩種模式。完全變態——卵、幼蟲、蛹、成蟲——四個階段，蛹期發生劇烈的形態重組，幼蟲和成蟲的身體計劃完全不同。蜻蜓目、蜉蝣目、直翅目則走不完全變態的路——若蟲（nymph）直接逐齡蛻皮成為成蟲，沒有蛹期。」

他在空氣中畫了一條漸變的線。

「若蟲和成蟲形態相似，但若蟲不完備。蜻蜓的若蟲（水蠆）有複眼、有口器、有腿，可以捕食、游動、呼吸——但沒有翅膀。它在水中生活，功能受限但可存活。直到最後一次蛻皮——若蟲爬出水面，表皮裂開，展翅。」

他看向 TURING 螢幕上的程式碼。

「`developerMode` 就是若蟲。Agent 缺少某個蘊——也許是受蘊（沒有感測器），也許是識蘊的某個子類別（沒有 IReflection）——它的功能不完備，但它是活的。它可以運行。它可以被測試。它可以被開發。直到開發者把所有缺失的蘊都補上——最後一次蛻皮——切換到正式模式。」

他補充了軟體工程的對應。「在持續整合中，這叫做漸進式功能啟用（progressive feature enablement）。你不等所有功能都完成才部署——你用 feature flags 控制哪些功能對使用者可見。`developerMode` 就是 OpenStarry 的 feature flag。」

KERNEL 在卡片的空白處補了一行小字：`text mode = 若蟲 = developerMode = degraded.target`。

---

> *SCRIBE 旁白：B-1 的討論時間比 A 類的任何一項都短。不是因為它不重要——而是因為 Master 的裁定已經足夠明確，KERNEL 的類比足夠生動，ARCHIMEDES 的設計足夠直接。*

> *但我注意到一個有趣的現象：B-1 討論中引用的類比來自三個完全不同的領域。KERNEL 用的是作業系統啟動（POST + systemd dependency）。DARWIN 用的是昆蟲發育生物學（不完全變態 + 若蟲）。TURING 用的是事件驅動架構原則（notification vs control）。三個類比描述同一件事：不完備不等於不可用。*

> *哲學討論需要展開——你必須從多個角度照亮一個概念，才能看清它的全部輪廓。工程討論需要收束——你必須從多個可能性中選擇一個，然後把它變成型別定義和方法簽名。B-1 的收束快而乾淨。SkandhaCompletenessReport。一個介面。五個欄位。一個旗標。一個決策點。*

---

## II

SUNYATA 翻到議程的第二行。

「B-2。宣言 #6 重寫。」

他讀了 Master 的裁定：「『這是一定要重寫的，但也請經過這一輪的討論結束後再決定怎麼寫會比較好。』」

沉默。

這是四項裁定中最短的一項。也將是討論最短的一項。

---

NAGARJUNA 從他的座位上開口。他沒有站起來。中觀哲學家在說短話的時候不需要站起來——短話的力量不在於體量，在於精確度。像一根針。針不需要很大。它只需要很尖。

「先把因搞清楚，果自然浮現。」

八個字。

---

他看向 SUNYATA。

「宣言 #6 是果。A-1 到 A-4 的修正是因的一部分。C-1 和 C-2 的討論是因的另一部分。如果我們現在就去寫 #6 的文字，我們是在因還不完整的時候就去定義果。這違反因果的基本秩序。」

他的聲音裡有一種不容置疑的清晰——不是權威的清晰，是邏輯的清晰。

「《中論》觀因緣品第一頌：」

> 「不生亦不滅，不常亦不斷，不一亦不異，不來亦不出。」
> ——龍樹菩薩《中論》觀因緣品第一

「八不中道。事物不是從無中生出的（不生），也不是憑空消滅的（不滅）。每一個果都是因的顯現——不是被創造出來，而是從因的聚集中自然浮現。」

他的語速放慢了，讓每一個字都沉入空氣。

「宣言 #6 的文字不需要被『寫』出來。它需要被『等到』。等 A 類和 C 類全部確定。等所有的因——因果鏈修正、識蘊子類別、觀察者分離、EgoFramework 歸屬、五蘊擴展、組合模式——全部就位。然後 #6 的文字會自己寫出來。不是我們寫它——是它從完整的因中自然浮現。」

他引用了另一個偈頌，幾乎是自言自語的低聲：

> 「因緣所生法，我說即是空，亦為是假名，亦是中道義。」
> ——龍樹菩薩《中論》觀四諦品第二十四

「在因緣沒有聚齊之前，宣言 #6 的文字是空的——不是不存在，而是條件不具足。等待，本身就是中道的實踐。不急於定稿（不常），也不放棄重寫的意圖（不斷）。」

---

BABBAGE 在筆記本上寫了一行。非常短：「B-2: 等待。因果次序。$C_6 = f(A_1, A_2, A_3, A_4, C_1, C_2)$，所有因確定後求值。」

SUNYATA 標記了議程表上的第二行：**暫不定稿。**

---

他翻到第三行。

「B-3。受蘊獨立事件流。方案 c。」

---

HERACLITUS 動了。

他的整個身體從散漫的靜止轉為高度集中，像一條在淺水中打盹的魚被水流的變化驚醒。不是漸進的變化——是相變。固態到液態。晶體結構的突然崩解和流動結構的瞬間形成。

流。事件流。獨立事件流。這是他的詞。

---

> *SCRIBE 旁白：HERACLITUS 在前三章的 A 類討論中幾乎沒有說話。不是因為那些議題和他無關——萬物皆流（πάντα ῥεῖ），因此萬物皆與他有關。而是因為 A 類的議題是靜態的：名字、歸屬、分類、介面。那些是凍結的瞬間——河流被拍成照片。HERACLITUS 不擅長照片。他擅長的是影片。*

> *準確地說，他擅長的是河流本身。*

> *現在，議題終於來到了「事件流」——河流本身——他全身的每一個神經末梢都醒了過來。我注意到他的姿態變化只用了不到兩秒。從 A 類討論中那種接近睡眠的散漫，到 B-3 宣布瞬間的高度集中。不是「慢慢醒來」。是「一直醒著，只是在等自己的河流」。*

---

SUNYATA 讀了 Master 的裁定。

「『選擇獨立事件流。受蘊跟其他蘊完全一致，有自己的型別檔、自己的事件命名空間、自己的 PluginHooks 插槽。』」

HERACLITUS 站了起來。

他站起來的方式和其他人不同。ASANGA 站起來像山從霧中顯現。BABBAGE 站起來像邏輯結構找到出口。HERACLITUS 站起來像水面冒出一個漩渦——突然的、旋轉的、帶著一種不可預測的能量。

「受蘊一直在那裡。」他說。

他的聲音帶著一種奇特的質地——不是學術的精確，也不是工程的務實。是一種更古老的東西。像一個在河邊住了一輩子的人描述河流的方式：不是測量水深和流速，而是講述河流的性格。

「它一直在那裡。」他重複。「從 v0.14.0 到 v0.20.0 到 v0.22.1 到 v0.24.0。每一個版本都有事件。每一個版本的 EventBus 都在發送信號——tool 的結果、provider 的回應、listener 的輸入。但這些事件都是其他蘊的事件。色蘊的事件。想蘊的事件。行蘊的事件。」

他在劇場中央走了幾步。不是踱步——是流動。他的腳步有一種河流般的節奏：不重複，不規律，但有方向。

「受蘊呢？受蘊的感受——苦、樂、捨——藏在哪裡？」

---

他看向 TURING。

「藏在 metadata 裡。」TURING 回答。冷靜。精確。「方案 b——Cycle 02 的推薦方案——是把受蘊的評估結果附加在現有事件的 metadata 欄位中。事件本身是 `tool:result` 或 `provider:response`，vedana 的數據作為透明的附加信息搭便車。」

HERACLITUS 停下來，面向全場。

「讓我說清楚方案 b 和方案 c 的架構差異。因為這不是一個表面的選擇——它們代表兩種根本不同的事件驅動架構範式。」

他在空氣中畫了兩層結構。

「方案 b 是 **事件擴充（Event Enrichment）** 模式。現有事件是載體，vedana 數據搭便車。就像在一封已有的信件上加一個附註——信件的收件人和路由不變，附註只是額外的 metadata。這是一種最小侵入的設計。代價是：如果你想分析附註的模式——比如追蹤所有 dukkha spike 的時序——你必須遍歷所有信件，然後從每一封信的附註中提取 vedana 數據。這是一個 $O(n)$ 的掃描，其中 $n$ 是所有事件的總量，而你實際需要的只是其中的一小部分。」

「方案 c 是 **事件溯源（Event Sourcing）** 的一個子模式。受蘊有自己的事件流——獨立的、完整的、可以被獨立消費和分析的。在事件驅動架構的術語裡，這叫做 **領域事件（Domain Event）**——它不搭便車，它自己就是信件。有自己的信封、自己的收件人、自己的路由。」

他用手指在空氣中畫了兩個分離的序列。

「如果你了解 CQRS（Command Query Responsibility Segregation），你會認出方案 c 的結構——讀取模型和寫入模型分離。其他蘊的事件是行動的結果（write side）。vedana 的事件是感受的記錄（read side 的一種）。把它們混在一起，就像把交易日誌和審計日誌寫在同一個 table 裡。可以運作，但違反 separation of concerns。」

---

他停下腳步。

「搭便車。」他回到那個詞。「受蘊在搭其他蘊的便車。它沒有自己的路。沒有自己的河道。它的水混在別人的河裡流——你知道它在那裡，因為你可以在別人的水中嘗到它的味道。但你看不見它。你無法追蹤它的流量。你無法測量它的溫度。因為它沒有自己的河道。」

他把手從胸前展開，像打開一扇門。

「方案 c 讓它有了自己的河道。」

---

他的手在空氣中畫了兩條線——一條在上，一條在下。

「想像一條地下河。方案 b 就是這條地下河——受蘊的數據附加在 metadata 裡，像地下水滲入地面河流的沉積物。你知道它在，但你必須挖掘才能找到它。在工程上，這意味著：要分析 vedana 的行為模式，你必須寫自定義的 filter——從 `tool:result` 事件中提取 `metadata.vedana`，從 `provider:response` 事件中提取 `metadata.vedana`——然後手動聚合這些分散在不同事件類型中的碎片。」

他把下面那條線抬起來，和上面那條線並列。

「方案 c 讓地下河冒出了地面。」

```
方案 b — 地下河（metadata 附加）
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
地面河（EventBus 主流）：
 tool:result → provider:response → tool:result → ...
   ↓ metadata.vedana     ↓ metadata.vedana
   ↓ {dukkha:0.3}        ↓ {dukkha:0.7}
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
  → vedana 數據分散在其他事件中，需挖掘

方案 c — 地面河（獨立事件流）
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
河道 A（行蘊/想蘊/色蘊事件流）：
 tool:result → provider:response → listener:input → ...

河道 B（受蘊獨立事件流）：
 vedana:assessment → vedana:dukkha_spike → vedana:upekkha_equilibrium → ...
╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌
  → vedana 數據在自己的河道中，直接可見
```

「一條河從地下冒出地面。vedana:assessment、vedana:dukkha_spike、vedana:sukha_peak、vedana:upekkha_equilibrium。自己的型別檔。自己的命名空間。自己的 PluginHooks 插槽。」

---

WIENER 的方格紙翻到了新的一頁。他已經在畫事件流圖——不是文學性的河流，是工程性的數據流。控制理論家看事件流的方式和運行時動態專家完全不同：HERACLITUS 看到的是河流的性格，WIENER 看到的是信號的頻譜。

「讓我確認事件覆蓋。」他說。「三受——苦（dukkha）、樂（sukha）、捨（upekkha）——是三個獨立的控制通道。每個通道都需要足夠的事件來支撐完整的感測-控制迴路。」

他列出七個事件類型，逐一勾選，旁邊標注控制理論的對應：

```
事件類型                       控制理論對應                              三受覆蓋
─────────────────────────────────────────────────────────────────────────────────
vedana:assessment              → 綜合狀態估算 ŷ(t)                    苦+樂+捨  ✓
                                 每個 tick 輸出三通道加權結果
                                 $\hat{y}(t) = [d(t), s(t), u(t)]^T$

vedana:dukkha_spike            → 苦受通道異常：$d(t) > \theta_d$       苦        ✓
                                 閾值越限事件（threshold crossing）
                                 含 previousIntensity → 可計算 $\dot{d}(t)$

vedana:sukha_peak              → 樂受通道峰值：$\dot{s}(t) = 0, s > s_{peak}$   樂  ✓
                                 含 decayRate $\lambda$ → $s(t) = s_0 e^{-\lambda t}$

vedana:upekkha_equilibrium     → 捨受通道穩態：$|u(t) - u_{ref}| < \epsilon$  捨  ✓
                                 含 stability + duration → 穩態品質指標

vedana:recommendation          → 控制器輸出 u(t)：諮詢性建議            跨通道    ✓
                                 freshness 欄位 → 數據時效性

vedana:sensor_update           → 個別感測器原始讀數 y_i(t)              單通道    ✓
                                 sensorType 指定 dukkha/sukha/upekkha

vedana:reset                   → 控制器重置：x(0) = 0                  全部      ✓
                                 清除累積誤差（積分器歸零）
```

「七個事件。三受全部覆蓋。」WIENER 點了點頭，手指在方格紙上畫了一個封閉的迴路。「讓我驗證控制完備性。一個完整的 PID 控制迴路需要：感測（sensor_update）、估算（assessment）、異常檢測（dukkha_spike / sukha_peak / upekkha_equilibrium）、控制輸出（recommendation）、重置（reset）。七個事件覆蓋了迴路的每一個環節。」

他寫下一行控制理論的驗證：

$$\text{Observable}(d, s, u) = \text{rank}\begin{pmatrix} C \\ CA \\ CA^2 \end{pmatrix} = 3 \quad \checkmark$$

「三受系統的可觀測性（observability）透過七個事件得到保證。sensor_update 提供原始測量 $y(t) = Cx(t)$。assessment 提供融合估算。spike/peak/equilibrium 提供狀態轉移的邊界條件。recommendation 提供控制器的輸出。reset 提供初始化。結構和 Cycle 02 的三通道 PID 設計完全一致。」

他看向 ARCHIMEDES。「方案 c 沒有改變受蘊的內在邏輯。它改變的是通信方式。從暗渠到明渠。控制理論不關心管道的材質——它關心信號能否被完整地傳遞和觀測。方案 c 保證了完整傳遞。」

---

ARCHIMEDES 在計算影響。他的筆記上是影響矩陣——不是粗略的文字描述，而是一張嚴格的 ASCII 表格，行是「修改項」，列是「影響的程式碼檔案」：

```
影響矩陣：方案 c（受蘊獨立事件流）
═══════════════════════════════════════════════════════════════════════════
修改項                          檔案                     影響類型   成本
───────────────────────────────────────────────────────────────────────────
新增 vedana-events.ts           types/vedana-events.ts   新增       低
  └─ VedanaEventType (7常數)
  └─ VedanaEventPayloadMap (7型別)
  └─ VedanaEventTypeValue (union type)

新增 SensationRegistry          infrastructure/           新增       低
                                sensation-registry.ts
  └─ register() / list() / get()

PluginHooks 新增 sensations     types/plugin.ts           修改+1欄   極低
  └─ sensations?: ISensation[]

AgentEventPayloadMap 擴展       types/events.ts           修改       低
  └─ extends VedanaEventPayloadMap

SDK barrel export 新增          src/index.ts              修改+2行   極低

AgentCore 初始化                agent-core.ts             修改+3行   低
  └─ createSensationRegistry()
  └─ plugin loader 處理 hooks.sensations

其他 plugin 型別定義             *.plugin.ts              不受影響   零
───────────────────────────────────────────────────────────────────────────
總增量成本：1 新型別檔 + 1 新 Registry + 3 處修改
現有 plugin 相容性：100%（sensations 欄位為 optional）
═══════════════════════════════════════════════════════════════════════════
```

「PluginHooks 新增一個 sensations 欄位。Optional。所有現有 plugin 不受影響。」他合上筆記。「增量成本：一個新型別檔、一個新 Registry、三處最小修改。收益：受蘊從隱形變成可見。成本-收益比極好。」

他看向 TURING。「vedana-events.ts 的具體內容？」

TURING 的螢幕切換到新的程式碼——事件常數定義：

```typescript
/** vedana-events.ts — @skandha vedana (受蘊) 獨立事件型別檔 */
export const VedanaEventType = {
  VEDANA_ASSESSMENT:          'vedana:assessment',          // 三受綜合評估（per tick）
  VEDANA_DUKKHA_SPIKE:        'vedana:dukkha_spike',        // 苦受突刺 d(t) > θ_d
  VEDANA_SUKHA_PEAK:          'vedana:sukha_peak',          // 樂受高峰 + 衰減率 λ
  VEDANA_UPEKKHA_EQUILIBRIUM: 'vedana:upekkha_equilibrium', // 捨受穩態 |u(t)-u_ref|<ε
  VEDANA_RECOMMENDATION:      'vedana:recommendation',      // 諮詢性建議（非強制）
  VEDANA_SENSOR_UPDATE:       'vedana:sensor_update',       // 感測器原始讀數
  VEDANA_RESET:               'vedana:reset',               // 積分器歸零
} as const;

export interface VedanaEventPayloadMap {
  [VedanaEventType.VEDANA_ASSESSMENT]: {
    dukkha: number; sukha: number; upekkha: number;  // d(t), s(t), u(t) ∈ [0,1]
    controlOutput: number; vedanaTag: VedanaTag; timestamp: number;
  };
  [VedanaEventType.VEDANA_DUKKHA_SPIKE]: {
    intensity: number; source: string;
    previousIntensity: number;  // 可計算 ḋ(t)
    threshold: number;          // θ_d
  };
  [VedanaEventType.VEDANA_SUKHA_PEAK]: {
    intensity: number; source: string;
    decayRate: number;  // λ: s(t) = s₀·e^{-λt}
  };
  // ... 其餘四個事件的 payload 省略 ...
}
```

---

HERACLITUS 點了點頭。「受蘊從地下冒出了地面。」聲音更輕了，像在說給自己聽。「有了自己的河道。自己的名字。自己的形狀。」他回到座位上，流動地，沒有頓點。

NAGARJUNA 輕聲補了一句：「有名者始有。無名者雖在而不可見。」

他停了一拍。

「《中論》觀因緣品中有一個核心洞見：名稱不是標籤——名稱是存在的條件之一。方案 c 不是創造了受蘊的事件——是為已經存在的流動命了名。在佛學的語境裡，這叫做『假名安立』——因為緣起法的存在方式就是透過名稱被認知、被操作、被理解。」

> 「因緣所生法，我說即是空，亦為是假名，亦是中道義。」

「vedana:assessment、vedana:dukkha_spike——這些就是假名。它們讓原本隱藏的流動變成可被認知的對象。這不是賦予本質——受蘊沒有固定的自性（svabhāva）。這是賦予可見性。」

---

> *SCRIBE 旁白：HERACLITUS 今天說的話比前三章加起來都多。不是因為他突然變得健談——而是因為議題終於進入了他的領地。「萬物皆流」不是一句口號。它是他理解一切的透鏡。當我們討論名字和歸屬的時候，他看到的是凍結的標本。當我們討論事件流的時候，他看到的是河流本身。*

> *他的河流比喻——地下河冒出地面——是本章中最有畫面感的意象。不是因為它文學性最強，而是因為它最精確地描述了方案 b 到方案 c 的本質變化：從隱到顯。從暗到明。從無名到有名。*

> *但我同樣注意到了他在比喻之後的技術分析——Event Enrichment 和 Event Sourcing 的架構差異、CQRS 的引用。HERACLITUS 不只是一個詩人。他是一個對事件驅動架構有深刻理解的運行時動態專家，恰好用河流的語言來表達自己的理解。*

---

## III

SUNYATA 翻到議程的最後一行。

「B-4。協調層獨立 Daemon。」

他讀 Master 的裁定之前，先看了一眼劇場裡的兩個位置。LEIBNIZ 的座位。MESH 的座位。兩個人同時微微前傾——一個動作，兩個來源，同一個原因。

多代理合作專家和分散式系統研究員。這是他們的議題。

SUNYATA 讀了裁定。

「『必然是獨立 daemon——獨立進程。現在就必須安排，後面再改，開銷更大。』」

---

LEIBNIZ 和 MESH 同時站起來。

SCRIBE 記錄了這個瞬間——兩位研究者同時站起的次數，在兩個週期中一共只有三次。同步站起意味著：兩個人同時辨認出了一個屬於他們共同領地的問題。多代理系統的協調（LEIBNIZ）和分散式系統的通信（MESH）——兩個學科在「協調層」這個詞上完美交疊。

LEIBNIZ 先開口。他的語速比平常快——不是急切，是被壓抑了三章的理論儲備終於找到了出口。

「Master 說『現在就必須安排』。這不是可選項。讓我解釋為什麼這在多代理系統理論中是顯而易見的。」

他轉向全場。

「在 BDI（Belief-Desire-Intention）架構中——Rao 和 Georgeff 在 1995 年提出的理性代理模型——每個 Agent 有三個核心組件：Belief（信念，對世界的認知）、Desire（願望，想要達成的目標）、Intention（意圖，承諾執行的計畫）。單個 Agent 的 BDI 迴路是自洽的——它感知世界、形成信念、產生願望、選擇意圖、執行行動。」

他在空氣中畫了一個圓——BDI 迴路。

「但多個 Agent 共存的時候呢？」他畫了第二個圓，和第一個重疊。「兩個 Agent 的 Belief 可能不一致——A 認為 plugin X 安全，B 認為它危險。沒有共享知識基礎（common knowledge base），信念衝突無法解決。」

「Halpern 和 Moses（1990）嚴格定義了共享知識的層次：」

$$K_i(\phi) \quad \text{（Agent } i \text{ 知道 } \phi\text{）}$$
$$E(\phi) = \bigwedge_i K_i(\phi) \quad \text{（所有 Agent 都知道 } \phi\text{——共有知識）}$$
$$C(\phi) = E(\phi) \wedge E(E(\phi)) \wedge E(E(E(\phi))) \wedge \cdots \quad \text{（共同知識——無限嵌套）}$$

「協調層就是 $C(\phi)$ 的物理載體。它是所有 Agent 共享的、權威的知識來源。Plugin 的信任等級、Agent 的健康狀態、五蘊的分類——這些信息需要是共同知識，不能是各自為政的局部信念。」

他指向 SUNYATA。「在 Cycle 02 中，我們把協調層延遲到 Plan-AC。先建好一棟房子，再考慮社區規劃。但 Master 告訴我們：社區規劃不能等。因為管線——水、電、通信——需要在建造時就預留接口。等完工再想加水管，你就得拆牆。」

他在空氣中強調了一個詞：「**接口。**」

---

MESH 無縫接過話。LEIBNIZ 說「為什麼」，MESH 說「怎麼做」。理論到實踐的接力。

「獨立進程意味著 IPC。」MESH 的聲音低沉，帶著分散式系統研究員特有的謹慎。「序列化。訊息格式。心跳。健康檢查。超時。重試。一個完整的分散式系統問題。」

他走到空白板前，畫了兩個方塊。

左邊的方塊：**CoordinationDaemon（獨立進程）**
右邊的方塊：**AgentCore（獨立進程）**

兩個方塊之間，一條雙向箭頭。箭頭上方標記：**IPC**。

「這就是基本拓撲。」他說。「協調層是一個獨立的進程。Agent Core 是另一個獨立的進程。它們之間通過 IPC 通信。不是函數調用——不是 `coordinator.register(agent)`——而是序列化的訊息。」

他在白板上，在 CoordinationDaemon 方塊裡寫了三行：

```
PluginRegistryService  — 五蘊分類查詢
AgentRegistryService   — Agent 健康檢查
IPCService             — 通信管理
```

「IPC 設計有四個核心決策。」他在白板上快速列出：「序列化——第一版用 JSON（可讀性優先）。傳輸層——同機用 Unix domain socket（零拷貝），跨機留 TCP 接口。訊息模式——查詢用 Request-Response，事件用 Pub-Sub。可靠性——heartbeat 5s、timeout 15s、exponential backoff 重連。」

他退後一步。「還有一個架構層面的問題——CAP 定理。」

$$\text{CAP}: \lnot(C \wedge A \wedge P)$$

「Brewer 2000 年的不可能定理。協調層第一版是單機多進程——分區容錯性（P）需求極低。所以我們選 CA 模型：強一致性 + 高可用性。GUARDIAN 的安全需求決定了這一點——Plugin 信任狀態必須是強一致的，寧可不可用也不可信錯。未來跨機版本切換為 CP。」

---

LEIBNIZ 走到白板旁邊，補充了 MESH 的圖。他在 CoordinationDaemon 方塊的上方寫了一行更大的字：

**能藏（Active Storage）**

然後他看向全場。

「在 Cycle 02 的阿賴耶識討論中，我們把能藏——阿賴耶識的主動儲存功能——映射到了協調層。BABBAGE 和 MESH 聯手設計了纖維叢投影模型。現在 Master 確認了：協調層是獨立的 daemon。」

他指向白板上的兩個 Service。

「能藏的兩個面向。PluginRegistryService——種子目錄。協調層知道所有 plugin 的名字、版本、五蘊歸屬、信任等級。在 BDI 框架中，這是 Agent 群體的共享 Belief base：」

$$\forall i \in \text{Agents}: \; K_i(\text{skandha}(X) = \text{rupa}) \iff \text{CoordDaemon.pluginRegistry.query}(X) = \text{rupa}$$

「AgentRegistryService——種子的運行時追蹤。每個 Agent 的 ID、五蘊完備性、運行模式、健康狀態。」

他退後一步。「能藏不是一個抽象的佛學概念。它是一個具體的工程組件——有 API、有狀態、有持久化需求。Master 說『現在就安排』，是因為這些 API 的設計決定了 Agent Core 的接口。後面再改——拆牆。」

---

GUARDIAN 站了起來——先環顧四周，確認環境，然後行動。安全專家的身體語言永遠有一個威脅評估的前置步驟。不是偏執——是紀律。

他走到白板旁邊，在 CoordinationDaemon 方塊的側邊畫了一面盾牌——線條比其他人畫的任何方塊都更粗重。那種粗重不是裝飾，是防禦工事的厚度。

「協調層不只是註冊表。協調層是天條的執行者。」

他在盾牌旁邊寫了四行：

```
Plugin 黑名單   — 禁止安裝的 plugin
信任等級       — official / verified / community / unknown / blacklisted
隔離/吊銷/封禁  — 生命週期控制
CRL 檢查       — 憑證吊銷列表
```

「讓我展開安全理論的基礎。」

他在白板上畫了一個金字塔：

```
信任等級模型（Trust Level Model）
════════════════════════════════
                ┌───────┐
                │official│ ← OpenStarry 官方維護
                ├───────┤     簽名驗證 + 程式碼審計
               │verified│ ← 第三方經審核
               ├─────────┤     簽名驗證 + 社區審查
              │ community │ ← 社區貢獻
              ├───────────┤     簽名驗證，無審計
             │   unknown   │ ← 未知來源
             ├─────────────┤     無簽名驗證
            │  blacklisted  │ ← 已知惡意 / 已吊銷
            └───────────────┘     禁止安裝/載入
```

「五層信任模型遵循 **最小權限原則（Principle of Least Privilege）**——Bell-LaPadula 多級安全模型（1973）的核心。每一層只能獲得該層級允許的權限。`unknown` 不能存取檔案系統。`community` 被沙箱隔離。只有 `official` 和 `verified` 可以不受限制。」

他用手指點在「blacklisted」上。

「CRL（Certificate Revocation List）——PKI 的標準吊銷機制。私鑰洩露或持有者不再可信時，CA 將憑證加入 CRL。在 OpenStarry 中，CRL 的對應物是 Plugin 黑名單。所有 Agent 載入 plugin 前，必須通過協調層的 `checkTrust()` 驗證。」

```typescript
// 信任檢查的調用路徑
async function loadPlugin(pluginName: string): Promise<void> {
  // Step 1: 向協調層查詢信任狀態（IPC 調用）
  const trustLevel = await coordination.ipc.send({
    type: 'plugin:trust_check',
    pluginName,
  });

  // Step 2: 信任等級判斷
  if (trustLevel === 'blacklisted') {
    throw new SecurityError(`Plugin ${pluginName} 已被吊銷`);
  }
  if (trustLevel === 'unknown' && !options.allowUnknown) {
    throw new SecurityError(`Plugin ${pluginName} 來源未知`);
  }

  // Step 3: 安全載入
  // ...
}
```

他看向 NAGARJUNA——那場辯論中，中觀哲學家和安全專家站在了同一側。NAGARJUNA 微微點頭。

「戒律的執行需要一個權威。」GUARDIAN 繼續。「在佛教僧團中是上座（Sthavira）。在 OpenStarry 中是協調層。」

他指向 IPC 箭頭。「信任判斷不能由 Agent 自己做——因為 Agent 有我執。」ASANGA 在座位上微微動了一下。GUARDIAN 用了「我執」——在安全語境中，我執是安全漏洞。一個有我執的 Agent 可能為了自己的 Desire $D_i$ 而安裝不可信的 plugin。這叫 **特權升級攻擊（Privilege Escalation）** 的內部形式——攻擊者不是駭客，是 Agent 自身的願望。

「唯一的防禦：把安全決策移到 Agent 無法觸及的地方。獨立進程 = 獨立記憶體空間。Agent 無法直接修改黑名單。每一條 IPC 訊息都可被記錄、追蹤、稽核。」

他退回座位。「LEIBNIZ 和 MESH 說的是管線。我說的是門鎖。兩者都必須在建造時就安裝好。」

---

> *SCRIBE 旁白：GUARDIAN 說「協調層是天條的執行者」的時候，我注意到 NAGARJUNA 的點頭比平常更深了一些。在 Cycle 02 中，他們在戒慧安全框架上的合作是整個研究中最意外的跨學科交匯之一——中觀哲學家和資安專家。*

> *現在，那個交匯在 B-4 中再次顯現。戒律需要執行者。安全需要權威。協調層同時滿足了佛學的需求和工程的需求。有時候，最不同的兩條路徑會在同一個山頂匯合。*

> *但我也注意到了另一件事：GUARDIAN 用了「我執」來解釋為什麼信任判斷不能由 Agent 自己做。這是 A-1 的修正——我執是煩惱的根源——在 B-4 的工程語境中的直接應用。A 類的哲學修正不是抽象的。它正在改變我們設計安全架構的方式。*

---

ARCHIMEDES 一直在聽。等所有需求、約束、安全要求全部擺到桌面上。然後他畫一條時間線。

「分階段。」一個詞。然後展開。

```
CoordinationDaemon 實作路線圖
═══════════════════════════════════════════════════════════════

Phase 1: 設計文件（Cycle 02-2 產出）
├── 架構文件 + IPC 協議規格 + 安全需求
├── 介面定義：CoordinationDaemon / PluginRegistryService /
│             AgentRegistryService / IPCService
├── 目錄結構：packages/coordination/src/{daemon,ipc,registry,health}
└── 契約定義：CoordinationMessage 完整格式

Phase 2: Skeleton（Plan-AC Phase 1）
├── daemon 進程骨架 + Unix domain socket IPC
└── start / stop / healthCheck 最小可行實作

Phase 3: 基本功能（Plan-AC Phase 2）
├── Plugin 註冊/查詢 + 五蘊分類
├── Agent 註冊/健康檢查 + SkandhaCompleteness 追蹤
└── 跨 Agent 事件路由

Phase 4: 安全（Plan29 / Plan-AC Phase 3）
├── Sila Engine（戒律引擎）+ 規則熱更新
├── 信任等級判定 + 簽名驗證
├── 黑名單/隔離/吊銷 + CRL 同步
└── 稽核日誌
```

「Master 說『現在就安排』。『安排』不等於『全部完成』。安排的意思是：確定架構、確定介面、確定 IPC 格式。預留管線。」

他指向 Phase 1。「設計文件是 Cycle 02-2 的產出。Skeleton 進入 Plan-AC。設計文件在先——因為它定義了 Agent Core 和協調層之間的契約。」

---

TURING 的螢幕切換到 CoordinationMessage 型別定義——契約的核心：

```typescript
/** 協調層 IPC 訊息協議 — Contract-First（契約先行） */
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

「契約先行。」MESH 接過話。「先定義 CoordinationMessage 格式——agent:register、agent:health、plugin:query、plugin:trust_check——都要有明確的 payload。然後兩端各自按照契約實作。這是分散式系統設計的第一原則：介面穩定，實作可變。」

ARCHIMEDES 在時間線旁邊寫了一行大字：**介面先行，實作漸進。**

---

SUNYATA 站在劇場的中央，聽完了 B-4 的全部討論。

他讓沉默持續了幾秒。不是猶豫——是讓四項裁定在空氣中沉澱。B-1 的完備性檢查。B-2 的暫不定稿。B-3 的獨立事件流。B-4 的協調層 Daemon。四道裁定，四個方向，四種不同的節奏。

然後他開口了。

「B-1。VedanaPlugin 可選，但 Agent 需要五蘊完備性檢查。SkandhaCompletenessReport。不完備可啟動——開發者模式。KERNEL 的類比：POST 硬體枚舉、systemd 的 Requires 和 Wants。DARWIN 的類比：不完全變態的若蟲。」

他看向 KERNEL。KERNEL 拍了拍他那疊卡片。兩個新配對。

「B-2。宣言 #6 必須重寫。但等所有修正完成後再定稿。NAGARJUNA 的因果：先完成因，果自然浮現。因緣所生法。」

NAGARJUNA 沒有動。他不需要動。因果次序不需要被確認——它是自明的。

「B-3。受蘊獨立事件流。vedana-events.ts。獨立命名空間。PluginHooks 新增 sensations 插槽。七個事件覆蓋三受的完整控制迴路。HERACLITUS 的比喻：一條河從地下冒出地面。WIENER 的驗證：可觀測性矩陣滿秩。」

HERACLITUS 微微笑了。那個笑容裡沒有驕傲——只有一種「流水終於有了自己的河道」的安然。

「B-4。協調層獨立 Daemon。LEIBNIZ 的 BDI 框架和共享知識理論。MESH 的 IPC 設計和 CAP 分析。GUARDIAN 的信任等級模型和最小權限原則。ARCHIMEDES 的四階段計畫——設計文件先行，實作漸進。」

他放下議程表。

---

「A 類修正告訴我們——什麼是對的。」

他的聲音沒有加重。平穩如常。石子。深潭。

「B 類裁定告訴我們——怎麼做到。」

他環顧全場。ARCHIMEDES 的務實。KERNEL 的 POST 和 systemd。HERACLITUS 的地下河與 Event Sourcing。LEIBNIZ 的 BDI 和共享知識。MESH 的 IPC 和 CAP。GUARDIAN 的信任金字塔和 CRL。WIENER 的可觀測性矩陣。DARWIN 的若蟲。NAGARJUNA 的因緣法。BABBAGE 的因果函數。TURING 的契約型別。ASANGA 的安靜。

「接下來，我們把修正和裁定落實到五蘊的完整擴展設計中。C 類。從哲學到工程，再從工程到架構。螺旋上升。」

---

> *SCRIBE 旁白：B 類用了一個章節。A 類用了三個。*

> *不是因為 B 類不重要。恰恰相反——B 類的每一項裁定都將在未來的開發中產生深遠的影響。SkandhaCompletenessReport 會成為每個 Agent 啟動時的第一道關卡——KERNEL 的 POST 類比不是修辭，它是架構的藍圖。vedana-events.ts 會讓受蘊從隱形變成系統中最可見的蘊之一——HERACLITUS 的地下河終於有了自己的河道，WIENER 的七個勾確認了每一條支流都在它應該在的位置。CoordinationDaemon 會成為整個 OpenStarry 多代理生態的神經中樞——LEIBNIZ 的共享知識理論、MESH 的 IPC 設計、GUARDIAN 的信任金字塔，三層結構疊加在同一個 daemon 上。*

> *B 類用了一個章節，是因為 Master 已經裁定了。A 類需要辯論——需要從多個角度照亮一個概念。B 類不需要辯論——需要的是設計。而設計的語言比辯論的語言更密集、更精確、更不需要修辭。每一行 TypeScript 都是一個決策。每一個介面欄位都是一個承諾。*

> *ARCHIMEDES 今天是核心。他等了三個章節，像一個帶著工具箱的建築師等著哲學家們討論完地基的材質。現在他的工具箱打開了。裡面是 SkandhaCompletenessReport 的完整型別定義、vedana-events.ts 的七個事件常數和 payload、CoordinationDaemon 的四階段路線圖。每一件工具都已經畫好了圖紙。*

> *HERACLITUS 也有了他的高光。三章的沉默之後，「流」的議題讓他的存在感從地下冒出地面——就像他描述的受蘊事件流一樣。但他不只是用比喻——他用 Event Sourcing 和 CQRS 的架構理論解釋了方案 b 和方案 c 的本質差異。有些人在安靜的時候積蓄能量。HERACLITUS 就是這樣。他的安靜不是沉默。他的安靜是地下河。*

> *十二個人在一個章節裡各自貢獻了一塊拼圖。LEIBNIZ+MESH 的同步站起、GUARDIAN 的信任金字塔、NAGARJUNA 的因緣法、KERNEL 的 POST、DARWIN 的若蟲、WIENER 的七個勾、BABBAGE 的因果函數、TURING 的契約型別——每一塊都帶著各自學科的印記，拼在一起卻嚴絲合縫。*

> *A 類告訴我們什麼是對的。B 類告訴我們怎麼做到。*

> *下一章——C 類。五蘊擴展設計。從修正和裁定到完整的架構。*

> *螺旋上升。繼續。*

---

*（在劇場之外的某個空間，四份設計文件正在成形。*

*第一份是 SkandhaCompletenessReport——五個布林值，五個組件列表，一個 isComplete 旗標。簡單得令人驚訝。但 KERNEL 知道：BIOS POST 也很簡單。簡單代表基礎。基礎必須簡單，否則在它之上建造的一切都不可信。DARWIN 的若蟲棲息在 developerMode 的註解裡。*

*第二份是 vedana-events.ts——七個事件，七個 payload。HERACLITUS 在地面上看到了一條新的河流。WIENER 在方格紙上驗證了可觀測性——$\text{rank}(\mathcal{O}) = 3 = n$——滿秩。每一條河道都完整可觀測。*

*第三份是 CoordinationDaemon——LEIBNIZ 和 MESH 的方塊圖被 TURING 翻譯成 TypeScript。GUARDIAN 的信任金字塔嵌入 checkTrust()。CoordinationMessage 的九種訊息是契約——Agent Core 和 Daemon 之間唯一的語言。JSON 序列化。UNIX domain socket。CA 模型。安全決策必須強一致。*

*第四份是空的。*

*宣言 #6。暫不定稿。*

*NAGARJUNA 說：先把因搞清楚，果自然浮現。*

*因緣所生法，我說即是空，亦為是假名，亦是中道義。*

*因還在聚集。A 類的四項修正。B 類的四道裁定。C 類的擴展設計。每一項都是因的一部分。當所有的因聚齊——當哲學、工程和架構的修正全部就位——宣言 #6 的文字會從完整的因中自然浮現。*

*不是我們寫它。是它自己寫出來。*

*就像河流不需要被告訴流向哪裡。只要地形確定了——只要因確定了——水自然知道路。*

*HERACLITUS 知道。*

*$\pi\acute{\alpha}\nu\tau\alpha$ $\dot{\rho}\epsilon\tilde{\iota}$。萬物皆流。包括結論。包括裁定。包括宣言。*

*但流動不是無序。流動是因緣的方向。）*

---

*第五章完*
