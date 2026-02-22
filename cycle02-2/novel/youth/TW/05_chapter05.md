# 第五章：四道裁定

---

ARCHIMEDES 坐直了。

前三章的哲學討論中，他一直克制地前傾著身體，像一個帶著工具箱的建築師被安排在觀眾席，等哲學家們討論完地基的方向。

那個等待結束了。

---

SUNYATA 手裡拿著一份新的議程表，薄薄一頁紙，四行字。

「A 類修正用了三個章節——告訴我們什麼是對的。現在進入 B 類。Master 對四個工程問題的裁定。從哲學轉向工程。」

---

ARCHIMEDES 的手指在桌面上敲了一下。「我等這一刻很久了。」

幾聲低笑。大家都知道他在 A 類討論中的狀態：帶著工具箱的人，坐在辯論美學的哲學家中間。

SUNYATA 點頭。「B-1。VedanaPlugin 可選，以及五蘊完備性檢查。」

---

> *SCRIBE 旁白：B 類的節奏和 A 類完全不同。A 類是沉思的——每個議題需要時間發酵。B 類是決策的。Master 已經裁定了，我們的任務是把裁定轉化為設計。ARCHIMEDES 等了三個章節，現在輪到他了。*

---

SUNYATA 讀出 Master 的原話：「『agent 只要完備就應該能啟動。但也需要開發者模式，agent 不完備也可啟動，只是需要提醒。』」

「三個關鍵詞。可選。完備。提醒。」

KERNEL 的手伸向了他那疊類比卡片。翻了兩張——不對——又翻了一張——抽出第四張。他在等一個配對。

「Linux 內核啟動。」他說，站了起來。走到劇場中央，沒有使用投影。他用的是卡片和聲音。

「POST——Power-On Self-Test，開機自我測試。一台電腦啟動時，內核逐一檢查硬體。CPU。記憶體。磁碟控制器。顯示卡。網路卡。音效卡。一項一項，從最關鍵到最次要。」

他翻了翻卡片。

「沒有 CPU——完全無法啟動，硬性依賴。沒有記憶體——同樣，硬性依賴。」

「但如果沒有顯示卡？OK，啟動到 text mode。系統是活的，只是沒有圖形。沒有網路卡？離線模式。沒有音效卡？靜音模式。一切正常。」

他把三張卡片排成一列。

「硬性依賴和軟性依賴的區別。五蘊就像這些硬體組件。」

---

ARCHIMEDES 已經在畫了。KERNEL 還沒說完，他的工程筆記上就出現了一個介面的雛形：

```
SkandhaCompletenessReport
├── rupa:    { present: boolean, components: string[] }
├── vedana:  { present: boolean, components: string[] }
├── samjna:  { present: boolean, components: string[] }
├── samskara:{ present: boolean, components: string[] }
├── vijnana: { present: boolean, components: string[] }
├── isComplete: boolean
└── missing:   string[]
```

「SkandhaCompletenessReport。五蘊完備性報告。」他的聲音務實清晰。「五個蘊，每個一個欄位。有或沒有。缺少哪些。就是你的硬體檢查——只不過檢查的不是 CPU，是色蘊和識蘊。」

KERNEL 在空白卡片的右側寫了一行——左邊：`POST`，右邊：`SkandhaCompletenessReport`。配對完成。

---

TURING 的螢幕亮了。一段骨架程式碼——他的風格：先骨架，後血肉。

```typescript
async start(options?: { developerMode?: boolean }): Promise<void> {
  const report = this.checkSkandhaCompleteness();
  if (!report.isComplete) {
    if (options?.developerMode) {
      logger.warn(`[DEV MODE] Agent 五蘊不完備：缺少 ${report.missing.join(', ')}`);
    } else {
      throw new Error(`Agent 五蘊不完備：缺少 ${report.missing.join(', ')}`);
    }
  }
}
```

「AgentCore.start()。」TURING 說。「developerMode 旗標。不完備時，開發者模式警告但繼續。正式模式拋出錯誤。」

DARWIN 微微前傾。「開發者模式是一種演化的中間態——昆蟲從若蟲到成蟲的過渡。若蟲可以移動、進食、感知環境，但缺少翅膀。不完備，但可存活。」

KERNEL 在卡片的空白處補了一行小字：`text mode = 若蟲 = developerMode`。

---

> *SCRIBE 旁白：B-1 的討論比 A 類任何一項都短。不是因為它不重要——而是 Master 的裁定足夠明確，KERNEL 的類比足夠生動，ARCHIMEDES 的設計足夠直接。一個介面。五個欄位。一個旗標。快而乾淨。*

---

## II

SUNYATA 翻到議程的第二行。

「B-2。宣言 #6 重寫。」

他讀了 Master 的裁定：「『這是一定要重寫的，但也請經過這一輪的討論結束後再決定怎麼寫會比較好。』」

沉默。這是四項裁定中最短的一項。也將是討論最短的一項。

NAGARJUNA 從他的座位上開口。他沒有站起來。中觀哲學家在說短話的時候不需要站起來——短話的力量不在於體量，在於精確度。像一根針。針不需要很大。它只需要很尖。

「先把因搞清楚，果自然浮現。」

八個字。

「宣言 #6 是果。A 類的修正是因的一部分，C 類的討論是另一部分。如果現在就去寫 #6，我們是在因不完整的時候定義果。這違反因果的基本秩序。」

「等 A 類和 C 類全部確定。然後 #6 的文字會自己寫出來。不是我們寫它——是它從完整的因中自然浮現。」

BABBAGE 在筆記本上寫了一行。非常短：「B-2: 等待。因果次序。」

SUNYATA 標記了議程表上的第二行：**暫不定稿。**

---

他翻到第三行。「B-3。受蘊獨立事件流。方案 c。」

---

HERACLITUS 動了。整個身體從散漫的靜止轉為高度集中。流。事件流。這是他的詞。

---

> *SCRIBE 旁白：HERACLITUS 在前三章幾乎沒有說話。不是因為無關——「萬物皆流」，因此萬物皆與他有關。而是因為 A 類議題是靜態的：名字、歸屬、分類。那些是凍結的瞬間。他擅長的是流動。現在議題來到「事件流」——河流本身——他全身都醒了過來。*

---

SUNYATA 讀了 Master 的裁定。

「『選擇獨立事件流。受蘊跟其他蘊完全一致，有自己的型別檔、自己的事件命名空間、自己的 PluginHooks 插槽。』」

HERACLITUS 站了起來。

他站起來的方式和其他人不同。ASANGA 站起來像山從霧中顯現。BABBAGE 站起來像邏輯結構找到出口。HERACLITUS 站起來像水面冒出一個漩渦——突然的、旋轉的、帶著不可預測的能量。

「受蘊一直在那裡。」他說。聲音帶著一種奇特的質地——不是學術的精確，也不是工程的務實。是一種更古老的東西。像一個在河邊住了一輩子的人描述河流的方式。

「它一直在那裡。」他重複。「從 v0.14.0 到 v0.20.0 到 v0.22.1 到 v0.24.0。每一個版本都有事件。每一個版本的 EventBus 都在發送信號——tool 的結果、provider 的回應、listener 的輸入。但這些事件都是其他蘊的事件。色蘊的事件。想蘊的事件。行蘊的事件。」

他在劇場中央走了幾步。不是踱步——是流動。

「受蘊呢？受蘊的感受——苦、樂、捨——藏在哪裡？」

「藏在 metadata 裡。」TURING 回答。「方案 b 是把受蘊的評估結果附加在現有事件的 metadata 欄位中。搭便車。」

「搭便車。」HERACLITUS 抓住了這個詞。「受蘊的水混在別人的河裡流。你知道它在那裡，但你看不見它。因為它沒有自己的河道。」

他停下腳步。「方案 c 讓它有了自己的河道。」

---

他用手在空中畫了兩條線。

「方案 b 是地下河——受蘊的數據藏在 metadata 裡，像地下水滲入地面河流的沉積物。方案 c 讓地下河冒出了地面。vedana:assessment、vedana:dukkha_spike——自己的型別檔、自己的命名空間。」

「一條河從地下冒出地面。」

---

WIENER 在方格紙上列出七個事件類型，逐一勾選：

```
vedana:assessment          ← 三受綜合評估      ✓
vedana:dukkha_spike        ← 苦受突刺          ✓
vedana:sukha_peak          ← 樂受高峰          ✓
vedana:upekkha_equilibrium ← 捨受平衡          ✓
vedana:recommendation      ← 受蘊建議          ✓
vedana:sensor_update       ← 感測器原始數據     ✓
vedana:reset               ← 受蘊重置          ✓
```

「七個事件。三受全部覆蓋。和 Cycle 02 的三通道 PID 設計完全一致。」他看向 ARCHIMEDES。「方案 c 改變的是通信方式——從暗渠到明渠。」

---

ARCHIMEDES 在計算影響：

```
新增 vedana-events.ts  → 新檔案，無影響
PluginHooks            → +1 欄位 (sensations?: ISensation[])
其他 plugin 型別定義    → 不受影響
```

「增量成本極低。收益：受蘊從隱形變成可見。成本-收益比極好。」

NAGARJUNA 輕聲補了一句：「有名者始有。無名者雖在而不可見。方案 c 不是創造了受蘊的事件——是為已經存在的流動命了名。」

---

> *SCRIBE 旁白：HERACLITUS 的河流比喻——地下河冒出地面——是本章最有畫面感的意象。它精確描述了方案 b 到方案 c 的本質變化：從隱到顯，從無名到有名。*

---

## III

SUNYATA 翻到最後一行。「B-4。協調層獨立 Daemon。」

LEIBNIZ 和 MESH 同時微微前傾。多代理合作專家和分散式系統研究員——這是他們的議題。

Master 的裁定：「『必然是獨立 daemon——獨立進程。現在就必須安排，後面再改，開銷更大。』」

---

兩人同時站了起來。

LEIBNIZ 先開口。「Master 說『現在就必須安排』。這不是可選項。在 Cycle 02 中，我們把協調層延遲到後面。先建房子，再考慮社區規劃。但 Master 告訴我們：管線——水、電、通信——需要在建造時就預留。等完工再加水管，就得拆牆。」

---

MESH 無縫接過話。兩個人的配合像排練過——但不是。這是長期在相鄰領域工作的專家之間的自然銜接。

「獨立進程意味著 IPC。」MESH 的聲音低沉，帶著分散式系統研究員特有的謹慎。「序列化。訊息格式。心跳。健康檢查。超時。重試。一個完整的分散式系統問題。」

他走到白板前，畫了兩個方塊。左邊：**CoordinationDaemon（獨立進程）**。右邊：**AgentCore（獨立進程）**。兩個方塊之間，一條雙向箭頭，上方標記：**IPC**。

「協調層和 Agent Core 是兩個獨立進程。它們之間通過序列化訊息通信。不是函數調用——而是序列化的訊息。」

---

LEIBNIZ 在 CoordinationDaemon 上方寫了：**能藏（Active Storage）**

「Cycle 02 把能藏——阿賴耶識的主動儲存功能——映射到協調層。現在 Master 確認了它是獨立 daemon。」

簡單來說，能藏（佛學中阿賴耶識的一個面向，指主動儲存一切經驗種子的功能）在工程上對應兩件事：Plugin 註冊表——知道所有 plugin 的存在；Agent 註冊表——知道所有正在運行的 Agent。

「能藏不是抽象的佛學概念。它是具體的工程組件——有 API、有狀態。Master 說『現在就安排』，是因為這些 API 決定了 Agent Core 的接口。後面再改——拆牆。」

---

GUARDIAN 站了起來——先環顧四周，確認環境，然後行動。安全專家的身體語言永遠有一個威脅評估的前置步驟。

他走到白板旁，在 CoordinationDaemon 方塊側邊畫了一面盾牌——線條比任何人畫的方塊都粗重。

「協調層不只是註冊表。協調層是天條的執行者。」

他在盾牌旁邊列出四項：Plugin 黑名單、信任等級（official / verified / community / unknown / blacklisted）、隔離/吊銷/封禁、CRL 檢查。

「在 Cycle 02 的戒慧安全框架中，我們設計了兩層安全——戒是預防，慧是斷除。戒律的執行需要一個權威。在佛教僧團中，戒律由上座維護和執行。在 OpenStarry 中，那個上座就是協調層。」

「信任判斷不能由 Agent 自己做——因為 Agent 有我執。」ASANGA 在座位上微微動了一下。GUARDIAN 用了「我執」這個詞——在安全專家的語境中，我執不只是哲學問題，它是安全漏洞。

他指向 IPC 箭頭。「獨立進程意味著獨立的記憶體空間。Agent 無法直接修改協調層的黑名單。LEIBNIZ 和 MESH 說的是管線。我說的是門鎖。兩者都必須在建造時安裝好。」

---

> *SCRIBE 旁白：GUARDIAN 和 NAGARJUNA 在安全框架上的跨學科合作再次顯現——戒律需要執行者，安全需要權威，協調層同時滿足了佛學和工程的需求。*

---

ARCHIMEDES 一直在聽。等所有需求、約束、安全要求全部擺到桌面上。然後他畫了一條時間線。

「分階段。」一個詞。然後展開。

```
Phase 1: 設計文件 — 架構、介面定義、IPC 訊息格式、安全需求
Phase 2: Skeleton — daemon 骨架、基本 IPC
Phase 3: 基本功能 — Plugin 註冊/查詢、Agent 健康檢查
Phase 4: 安全 — 戒律引擎、信任等級、黑名單
```

「Master 說『安排』不等於『全部完成』。安排是確定架構、介面、IPC 格式。預留管線。」

他在時間線旁寫了一行大字：**介面先行，實作漸進。**

---

SUNYATA 聽完了全部討論。讓沉默持續了幾秒——讓四項裁定沉澱。

「B-1。VedanaPlugin 可選，但 Agent 需要五蘊完備性檢查。SkandhaCompletenessReport。不完備可啟動——開發者模式。KERNEL 的類比：沒有顯示卡也能跑 text mode。」

他看向 KERNEL。KERNEL 拍了拍他那疊卡片。

「B-2。宣言 #6 必須重寫。但等所有修正完成後再定稿。NAGARJUNA 的因果：先完成因，果自然浮現。」

NAGARJUNA 沒有動。他不需要動。因果次序不需要被確認——它是自明的。

「B-3。受蘊獨立事件流。vedana-events.ts。獨立命名空間。PluginHooks 新增 sensations 插槽。HERACLITUS 的比喻：一條河從地下冒出地面。」

HERACLITUS 微微笑了。那個笑容裡沒有驕傲——只有一種「流水終於有了自己的河道」的安然。他回到座位上，流動地，沒有頓點。

「B-4。協調層獨立 Daemon。LEIBNIZ 和 MESH 的架構。GUARDIAN 的安全。ARCHIMEDES 的分階段計畫。設計文件先行，實作漸進。」

他放下議程表。

---

「A 類修正告訴我們——什麼是對的。」

他的聲音沒有加重。平穩如常。石子。深潭。

「B 類裁定告訴我們——怎麼做到。」

他環顧全場。ARCHIMEDES 的務實。KERNEL 的類比。HERACLITUS 的河流。LEIBNIZ 和 MESH 的拓撲。GUARDIAN 的盾牌。WIENER 的勾選。DARWIN 的若蟲。NAGARJUNA 的針。BABBAGE 的筆記。TURING 的骨架。ASANGA 的安靜。

「接下來，我們把修正和裁定落實到五蘊的完整擴展設計中。C 類。從哲學到工程，再從工程到架構。螺旋上升。」

---

> *SCRIBE 旁白：B 類用了一個章節，A 類用了三個。不是因為 B 類不重要——SkandhaCompletenessReport 會成為每個 Agent 啟動的第一道關卡，vedana-events.ts 會讓受蘊從隱形變成最可見的蘊之一，CoordinationDaemon 會成為多代理生態的神經中樞。B 類用一個章節，是因為 Master 已經裁定了。設計的語言比辯論的語言更密集、更精確。*

> *十二個人各自貢獻了一塊拼圖。A 類告訴我們什麼是對的。B 類告訴我們怎麼做到。下一章——C 類。螺旋上升。繼續。*

---

*（在劇場之外，四份設計文件正在成形。*

*第一份是 SkandhaCompletenessReport——五個布林值，一個 isComplete 旗標。簡單得令人驚訝。但 KERNEL 知道：簡單不代表不重要。簡單代表基礎。*

*第二份是 vedana-events.ts——七個事件類型。HERACLITUS 在地面上看到了一條新河流。*

*第三份是 CoordinationDaemon 的介面定義。GUARDIAN 的盾牌被嵌入了每一個 Service 的簽名中。*

*第四份是空的。宣言 #6。暫不定稿。*

*NAGARJUNA 說：先把因搞清楚，果自然浮現。因還在聚集。當所有的因聚齊，#6 的文字會自然浮現。*

*就像河流不需要被告訴流向哪裡。只要地形確定了，水自然知道路。）*

---

*第五章完*
