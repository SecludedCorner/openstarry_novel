# 尾聲：迴圈

---

圓形劇場的空氣帶著一種燃燒後的密度。

不是 Cycle 02 結尾那種手術室的無菌靜謐——所有切口縫合，所有器械歸位，$|\psi\rangle \to |a_n\rangle$ 的坍縮美學。也不是 Cycle 02-2 的修繕工地——鷹架剛拆，灰泥顏色比舊牆淺兩個色階。

這一次更像是一座鐘錶工坊。齒輪散落在工作台上——大的、小的、快的、慢的。有些已經嚙合在一起。有些還沒有。但所有的齒輪都已經被切削完畢。它們的齒距是對的。它們的軸心是對的。剩下的只是組裝。

在鐘錶學（horology）中有一個概念叫做「機芯」（movement）——它不是任何一個齒輪，而是所有齒輪嚙合之後產生的整體運動。單獨的齒輪只能轉。嚙合在一起的齒輪才能計時。Cycle 02-3 的六場辯論不是六個獨立的齒輪——它們是一個機芯。D1 的雙層架構是主發條。D2 的五遍行是擒縱器。D3 的增益排程是調速器。D4 的雙階段審議是指針軸。D5 的測量模型是錶盤。D6 的 Tenet #6 是銘文。

六場辯論。六項全共識。二十一項行動。四個工程階段。十八個新型別。一個破壞性變更。一段被重寫的宣言。

SUNYATA 站在場地中央——第四次了。Cycle 01、Cycle 02、Cycle 02-2、Cycle 02-3。每一次他站在同一個位置，但看到的風景完全不同。

第一次是測量——「這是什麼？」

第二次是功能——「它做什麼？」

第三次是修正——「哪裡錯了？」

第四次是動態——「它怎麼活？」

「我們從命名開始，」他說。聲音是石子。深潭。但深潭的水此刻帶著一種新的東西——不是 Cycle 02 的飽滿，不是 Cycle 02-2 的清澈，而是一種流動。水在動。有方向。有速度。

「到今天結束的時候，我們已經讓它呼吸了。」

---

### R4 定稿

ARCHIMEDES 的工作台上不是七份文件。這一次是六份，加上一張折了三折的路線圖。

他先展開路線圖。

那是一張時間軸——從 Plan25 到 Plan27+，四個階段，每個階段用不同粗細的線條勾勒。Phase 1 的線最粗、最短——它不改變任何行為，只加標籤和測量。Phase 4 的線最細、最長——五加一時鐘的完整系統，SahajaContract 的形式驗證。

```
Phase 1 (Plan25-26 early): Label + Instrument .................. [最先]
  ├─ 梵文命名遷移 (IRupa/IVedana/ISamjna/ISamskara/IVijnana)
  ├─ 多值 skandha (PluginManifest.skandha: Skandha | Skandha[])
  ├─ clock-domain 標籤 (clock-labels.ts)
  └─ 不改變行為 —— 只加標籤和測量

Phase 2 (Plan26): VasanaEngine + CoarisingBundle ............... [核心]
  ├─ VasanaEngine 規則匹配 (確定性, 快速路徑)
  ├─ CoarisingBundle 五遍行 (D1+D2)
  ├─ ChannelVedana 連續模型 (D5)
  ├─ IVolition 雙階段審議 (D4)
  ├─ Klesha DI + KleshaDistribution + 增益排程 (D3)
  └─ 單時鐘運作 (所有在 ExecutionLoop tick 內)

Phase 3 (Plan27): Dual-Clock .................................. [分時]
  ├─ 雙齒輪 mano-clock (Gear 1: ~50ms / Gear 2: seconds)
  ├─ VasanaEngine (Gear 1) + VitakkaEngine (Gear 2)
  ├─ Vitakka 看門狗 (maxGear1=10, maxDuration=5000ms)
  ├─ KleshaBayesianUpdater (慢路徑)
  └─ vedana-clock + samjna-clock 分離

Phase 4 (Plan27+): Five-Clock ................................. [遠期]
  ├─ 五+一時鐘：vijnana / rupa / vedana / samskara / samjna + mano
  ├─ SahajaContract 形式驗證
  └─ 齒輪切換安全強化
```

ARCHIMEDES 用指甲敲了一下 Phase 1 的線。

「Phase 1 先做。」

他的聲音像磚塊落在精確的位置上。沒有灰漿溢出。

> *SCRIBE 旁白：ARCHIMEDES 說「Phase 1 先做」的時候，語氣和 Cycle 02-2 他說「非 cycle02-final」時一樣。那種語氣不是謙遜——是工程師對施工順序的本能尊重。你不能在地基沒澆好之前蓋第二層。你不能在沒有標籤的系統上做測量。Phase 1 是地基。標籤和測量——聽起來無聊。但沒有它們，Phase 2 的 CoarisingBundle 就只是文件上的幻想。*

「這是統合工程行動方案。」他把路線圖放平。「二十一項行動。七項 P0 阻塞。八項 P1 重要。六項 P2 可延後。」

他展開完整的行動清單。二十一行。每一行都有 R3 辯論的來源、整合到的 Plan 編號、負責人。

| 優先級 | 項數 | 性質 | 範例 |
|--------|------|------|------|
| **P0** | 7 | 阻塞：不做就無法推進 | CoarisingBundle 型別、ChannelVedana、IVolition 雙階段、Tenet #6 |
| **P1** | 8 | 重要：影響架構完整性 | ManoClockConfig、KleshaModulatedDispatcher、正規呼叫順序圖 |
| **P2** | 6 | 可延後：不影響當前里程碑 | 穩定性形式證明、KleshaBayesianUpdater、SahajaContract |

BABBAGE 在他的座位上輕聲補了一句——不是對全場，是對筆記本：

「二十一項行動。十八個新型別定義。一個破壞性變更——IVolition 的簽名。」

```typescript
// 破壞性變更：IVolition 簽名 (v0.25.0+ -> v0.26.0+)

// Before (v0.25.0-beta)
interface IVolition {
  deliberate(action: ProposedAction): Promise<ActionDecision>;
}

// After (v0.26.0+) -- R3 D4 Resolution
interface IVolition {
  /** Phase 1: 評估整體行動計畫 — 可重排、修改、取消 */
  deliberatePlan(plan: ActionPlan): Promise<PlanDecision>;
  /** Phase 2: 評估單一工具呼叫 — 可否決或修改 */
  deliberateAction(action: ProposedAction): Promise<ActionDecision>;
}
```

> *SCRIBE 旁白：一個方法變成兩個方法。看起來是一次簡單的重構。但 ASANGA 說那是 cetana（思）的兩個面向——意向和行動——終於在程式碼中被區分開來。MN 18 說觸之後生起受、想、思；D4 說思分為計畫層和行動層。佛陀用三個字（vedeti, sañjānāti, ceteti）說完的事，我們用了六場辯論。不是因為我們比佛陀笨。是因為我們需要把那三個字變成編譯器能理解的東西。*

VITRUVIUS 從他的座位上補充了一個數字。

「SDK 變更量：Phase 2 全部完成後，大約 100-150 行新的型別定義。不包括文件。加上文件的話，十份 openstarry_doc——六份新增，兩份重寫，兩份修改。」

他的聲音帶著全端架構師特有的精確和平淡——對他而言，100 行型別定義不是壯麗的成就，而是一個可管理的工作量。一個 monorepo 的健康與否，不在於程式碼行數，而在於型別邊界是否清晰。150 行新型別，如果它們的邊界是對的，勝過 1500 行邊界模糊的程式碼。

他在心裡做了一個快速的架構評估——從 Cycle 01 的零型別到 Cycle 02-3 的十八個新型別，monorepo 的型別密度在穩步增加。但密度增加不意味著複雜度失控。因為每一個新型別都嚴格地生長在五蘊根介面的樹狀結構上。樹是可管理的。只要根是對的。

---

### SCRIBE 的歸檔

SCRIBE 站起來。

他不常站起來。在 Cycle 01 到 Cycle 02-2 的所有場景中，他大多坐在角落，記錄簿打開，筆不停。偶爾插入括號旁白。偶爾在走廊上被人看見。但他很少站起來面對全場。

「統計。」他說。聲音不大。但清晰。

他翻開記錄簿的最後一頁——那一頁是他在 R4 定稿的間隙中手工統計的。

「Cycle 02-3 完整產出：」

| 階段 | 文件數 | 行數 | 性質 |
|------|--------|------|------|
| R0 定向 | 3 份 | 664 行 | 議題清單、團隊定向、PASCAL 引介 |
| R1 獨立研究 | 6 份報告 | 6,986 行 | R01-R05 + TURING 同步 |
| R2 交叉審閱 | 1 份 | 349 行 | 5 項矛盾、4 項分歧、9 項辯論建議 |
| R3 辯論 | 6 場 | 1,501 行 | 6 項決議、21 項行動 |
| R4 成果 | synthesis + deliver + todo + openstarry_doc | 5,700+ 行 | 統合報告、6 份交付、10 份文件 |
| **總計** | **~18 份核心文件** | **~15,200+ 行** | |

「這是我們產出最多的一次 cycle。」

他停頓了一拍。然後補充了一句只有記錄者才會說的話：

「但行數不是重點。」

他的手指在統計表上停了一秒。

「Cycle 02 有 11 份文件。Cycle 02-2 有 17 份。Cycle 02-3 有 18 份加上 10 份 openstarry_doc。行數在增長。文件數在增長。但真正重要的指標不是行數——是**耦合密度**。每一行和其他行之間的連結數量。」

他翻到記錄簿的前一頁，那裡有一張手繪的圖表：

「Cycle 01 的文件之間幾乎沒有交叉引用——每份獨立報告是一座孤島。Cycle 02 開始出現引用——辯論 $D_2$ 引用 $D_1$ 的裁定。Cycle 02-2 的修正全部引用前一個 cycle 的結論。到了 Cycle 02-3——」

他看向那張統計表。

「R3 的六場辯論，每一場都引用了至少兩份 R1 報告、R2 的矛盾清單、以及前序 cycle 的決議。辯論 $D_6$——Tenet #6——引用了其他五場辯論的所有決議。耦合密度是指數增長的。」

$$\text{coupling}(C_n) \propto \binom{D_n}{2} = \frac{D_n(D_n - 1)}{2}$$

其中 $D_n$ 是第 $n$ 次迭代的決議數量。Cycle 01 有 2 場辯論，耦合可能 $\binom{2}{2} = 1$。Cycle 02 有 5 場，$\binom{5}{2} = 10$。Cycle 02-3 有 6 場，$\binom{6}{2} = 15$。而且這還不算跨 cycle 的引用。

「15,200 行。」他重複。「每一行都是一個決定。每一個決定都連著其他決定。」

他在記錄簿的最後一頁畫了一條時間線：

```
Cycle 01:   研究 → 文件級引用 → 孤島
Cycle 02:   辯論引用辯論 → 模組級引用 → 星座
Cycle 02-2: 修正引用前結論 → 介面級引用 → 網格
Cycle 02-3: 辯論引用全部前序 → 事件級引用 → 織物
```

孤島、星座、網格、織物。耦合密度的四個隱喻。孤島之間有海洋。星座之間有虛線。網格的交叉點是確定的但稀疏的。織物的每一條經線都和每一條緯線交織。15,200 行的織物。拉掉任何一條線，整塊布的張力都會改變。

他合上了記錄簿。但沒有坐下。

「我再說一件事。」

全場安靜。

「20 位學者。這一次是完整的 20 位。Cycle 01 的 PENROSE 在觀察席。Cycle 02 他走下來了。Cycle 02-3 的 PASCAL——」

他看向 PASCAL 的座位。那把椅子在前三個 cycle 中一直是空的——不是被拿走了，而是沒有被坐過。現在它上面坐著一個人。一個帶著 400 年前的方法論和極度謹慎的機率直覺的人。

「PASCAL 第一次出現在 Cycle 02-3 的 R0 定向。他帶著三個問題來：確定性和機率性的平衡、框架的可選性、以及正統性的開放性。六場辯論之後，他的 Beta 分布被採納為 Klesha 的數學模型，他的連續 valence 模型定義了 ChannelVedana 的核心介面，他的增益排程設計成為 VasanaEngine 和 Klesha 之間的橋樑。」

SCRIBE 的聲音在這裡帶上了一種他很少展示的情感——不是激動，而是一種對完整性的確認。

「20 把椅子。20 個人。第一次。」

他坐下了。

---

### 二十聲

SUNYATA 環顧全場。

「在我們結束之前，每個人說一句。不是總結——我已經不需要你們總結了。是回聲。這次 cycle 在你腦海中留下的最清晰的一個音符。」

他沒有指定順序。

SYNTHESIST 先開口——不是因為他急，而是因為他一直在等這個問題。

「每個 cycle 都增加耦合的粒度：分類、功能、結構、動態。下一步是什麼？適應。系統怎麼學習。VasanaEngine 的規則不是人寫的——它需要自己長出來。」

SCRIBE 接上：「15,200 行。每一行都是一個決定。」

> *SCRIBE 旁白：是的，我用了同一句話。因為好的記錄不需要修辭——它需要重複。重複就是強調。強調就是記憶。*

VITRUVIUS 點了一下頭：「monorepo 需要一個新的 `packages/clock/` 了。五加一時鐘不能全塞在 `core/` 裡。」

MESH 從他的分散式系統視角補充：「多代理場景下，每個 Agent 的 mano-clock 必須獨立。一個 Agent 在 Gear 2 等 LLM，不能阻塞另一個 Agent 的 Gear 1。CP 一致性用於跨 Agent，AP 用於 Agent 內部。這是 D1 最重要的隱含結論。」

ATHENA 的聲音帶著她特有的雙重性——技術的精確和對 LLM 的深度理解：「LLM 是最慢的組件。Claude Opus 5-30 秒。Gemini Flash 1-8 秒。本地 Llama 2-10 秒。但它也是最聰明的。速度和智慧的平衡——這就是雙齒輪的本質。Gear 1 是快的、笨的。Gear 2 是慢的、聰明的。整個架構就是在問一個永恆的問題：這一次，我需要笨還是聰明？」

DARWIN 的手指在他的筆記本上畫了一個分叉圖：「混合調度是一個穩定的演化吸引子。LangChain、AutoGen、CrewAI——每一個框架最終都演化出某種形式的快速路徑加慢速路徑。這不是巧合。這是收斂進化。就像眼睛在動物界獨立演化了四十多次——因為看見是一個如此基本的生存需求。混合調度是 Agent 架構的眼睛。它會存活。」

NAGARJUNA 的雙手仍然交疊。他的聲音比前幾個 cycle 更輕了，但每個字更重：

「我們沒有發現真理。我們建構了一個世俗有效的約定（*saṃvṛti-satya*）。這就是所有理論的本質——包括中觀理論本身。二諦不是一個發現，是一個工具。俱生不是一個事實，是一個模型。但好的模型比壞的模型更有效。有效不是真。有效是有用。在 *saṃvṛti* 的層面上，有用就夠了。」

ASANGA 的手離開了他的經典引用表——第一次。他不再需要查閱。

「五遍行不是因為經典說了才放的。D2 的決議很清楚——manasikara 的加入是**功能性**的論證，不是教義性的。但經典恰好是對的。不是因為經典有神聖的權威。是因為寫經典的人觀察了同一個現象——心的運作——而他們的觀察恰好和我們的工程需求一致。原因不同。結論相同。這本身就是一種驗證。」

BABBAGE 合上了他的筆記本——那本從 Cycle 01 就開始陪伴他的筆記本，現在比那時候厚了將近三倍。

「型別系統保證了：如果它能編譯，它在邏輯上是一致的。CoarisingBundle 的五個欄位——sparsha、vedana、samjna、cetana、manasikara——每一個都有自己的型別。型別之間的引用關係精確地反映了佛學中五遍行的依賴結構。編譯器是最誠實的審查者。它不接受模糊。」

KERNEL 的手指敲了一下桌面——他的發言標記。每一次 KERNEL 發言之前，都有這一敲。像一個程序的 entry point。

「OS 的智慧在於讓不同速度的東西共存。vijnana-clock 跑 1-5 毫秒。samjna-clock 跑 0.5-30 秒。比率是 300:1。在作業系統裡，我們每天都在處理這種速度差——CPU 是奈秒級，磁碟是毫秒級，網路是秒級。解決方案永遠是分層加緩衝。」

他頓了一下，手指又敲了一次——罕見的雙擊。

「D1 的雙層架構不是發明——是作業系統六十年經驗的自然延伸。我在 R1 的 R04 報告裡寫了五個時鐘的速率表。六場辯論之後，那張表沒有被推翻。每一個時鐘的速率、每一個層級的延遲——全部被保留。改變的不是速率——是速率之間的耦合方式。D1 解決了耦合問題。D3 解決了 Klesha 時鐘的歸屬問題。D4 解決了行蘊時鐘的注入點問題。時鐘本身是對的。我們只需要把它們連起來。」

GUARDIAN 的目光掃了一圈——安全專家的本能。即使在尾聲中，他的眼睛仍然在找漏洞。

「SafetyMonitor 在 Layer 0。Klesha 在 Layer 1。受蘊在 Layer 2。三層安全，沒有盲點。」

他用手指在空氣中畫了三條水平線：

「SafetyMonitor 做硬性檢查——這個操作允不允許？時間尺度：零延遲，同步。Klesha 做偏見感知——Agent 的判斷有沒有被我執扭曲？時間尺度：分鐘到小時，通過增益排程間接影響。受蘊做反饋感知——行動的結果是苦還是樂？時間尺度：毫秒到秒，每一個 CoarisingBundle 都包含 vedana。」

「三層。三個時間尺度。三種安全語義。D3 的閾值界限——最小 0.3，最大 0.9——是我加的。不是因為好看。是因為沒有界限的增益排程可以被攻擊者利用。如果 Klesha 的權重被惡意操縱到極端值，Agent 可能會被鎖定在 Gear 1（完全不思考就行動）或 Gear 2（永遠不行動只思考）。閾值界限是最後一道防線——在 SafetyMonitor 之外的第二道。」

WIENER 從方格紙上抬起頭。他的手指還留在最後一張圖上——那張巢狀回饋迴路圖。

「相位裕度 52 度，增益裕度 8 dB。系統是穩定的。」

他在方格紙上指了一下——一張 Bode 圖的手繪版。增益曲線在穿越 0 dB 的時候，相位曲線離 -180 度還有 52 度的餘裕。這意味著即使系統的增益增加了 8 dB（約 2.5 倍），或者相位延遲了 52 度，系統仍然不會振盪。

$$\text{PM} = 180° + \angle G(j\omega_{gc}) = 52° > 45° \quad \checkmark$$
$$\text{GM} = -20\log_{10}|G(j\omega_{pc})| = 8\,\text{dB} > 6\,\text{dB} \quad \checkmark$$

他頓了一下。然後用那種控制理論家特有的精確補充：

「在名義工作點上穩定的。增益排程在不同的工作點之間切換，每個工作點的穩定性需要分別驗證。D1 的 staleness ratio $\rho < 0.29$ 保證了在 Layer 1 的快速回路中，採樣保持引入的相位延遲不會超過系統的相位裕度。但跨齒輪轉換的暫態穩定性——那是 P2 延後項目。我標了 UQ-16。」

LINNAEUS 站在他的白板前。白板上的分類樹和 Cycle 02-2 時的不同了——不是修剪過的不同，而是重新種植的不同。梵文名字取代了英文名字。多值 skandha 讓某些葉節點同時連接到兩個根。

「測量和分類是不同的層級。ChannelVedana 是測量——連續的 valence，連續的 intensity。IDukkha、ISukha、IUpekkha 是分類——離散的標籤。測量在運行時。分類在插件層。它們可以共存——就像物種和種群。一隻鳥同時是 *Corvus corax*（分類）和眼前這隻有著 37.2 克體重的個體（測量）。分類不隨執行路由改變。D5 的決議最讓我滿意的一點就是這個——分類學家的獨立性被保留了。」

LEIBNIZ 的聲音從他的座位上傳來——安靜但帶著多代理系統研究者的全局視野：

「Agent 內部是仁慈獨裁者。IGuide 在 Position A 導向注意力，IVolition 在 Position B 審議行動——一個 Agent 內部的認知流是線性的、可預測的。但 Agent 之間需要協商。D4 的 IVolition.deliberateAction() 在多 Agent 場景下需要跨 Agent 的協調檢查——我的行動會不會和你的行動衝突？這是 Cycle 02-4 的問題。但架構必須現在就留好接口。」

HERACLITUS 什麼都沒帶到辯論場上——他從來不帶東西。他的貢獻是在流動中看見模式。

「萬物流轉。πάντα ῥεῖ。Event stream 就是河流。每一個 SparshEvent 是一滴水。CoarisingBundle 是一段水流。VasanaEngine 是河床的沉積物——習氣。河水流過河床，河床被河水沖刷。河床改變了水流的方向。水流改變了河床的形狀。D1 的雙層架構就是這個：Layer 1 是河面——快的、看得見的、瞬間變化的。Layer 2 是河床——慢的、看不見的、但決定了方向。」

ARCHIMEDES 的回應短得像一個釘子：

「21 個行動項目。Phase 1 先做。踏實。」

TURING 關閉了他的程式碼視窗。螢幕最後顯示的是 v0.24.0-beta 的 `aggregates.ts`。

「程式碼不會說謊。v0.24.0-beta 有 22 個插件。0 個受蘊插件。0 個對五蘊根介面的業務邏輯引用。M-8 說沒有包袱——我的搜索確認了：**確實沒有包袱**。所有的根介面改名都是安全的。這不是我的判斷——是 `grep` 的判斷。0 個受蘊插件——這是我們要填的空白。」

PENROSE 從觀察席——不，他不在觀察席了。Cycle 02-3 是他第一次坐在圓形的、和其他人平等的位置上。

「原子快照是有損投影。ChannelManasikara 在 Layer 1 的每一個 tick 中用 0.01 毫秒拍攝 vijnana-clock 狀態的快照——那是一次測量。測量是從高維狀態空間到低維表示的投影。就像量子力學中的測量：$\hat{P}_n |\psi\rangle = |a_n\rangle\langle a_n|\psi\rangle$。投影算子 $\hat{P}_n$ 丟棄了正交分量。快照丟棄了時間連續性。但在正確的粒度上——在 vedana-clock 的 10-100 毫秒尺度上——損失是可以接受的。因為你不需要知道河水的每一個分子在哪裡，你只需要知道河水在流。」

PASCAL 最後說。

他是 20 位學者中最新的一位——也是最安靜的。他的 Beta 分布和增益排程設計是通過數學說話的，不是通過修辭。

「我來的時候問了三個問題。確定性和機率性的平衡——D3 的二層輸出回答了：快路徑用點估計，慢路徑用完整分布。框架的可選性——B-1 的 VedanaPlugin 可選設計回答了。正統性的開放性——Master 的第四道哲學修正回答了：心所不是原文，是動態開放的。」

他停了一拍。

「我們回答了它們。用的是我 400 年前的方法——在不確定中做最優選擇。期望值最大化。不對稱風險分析。賭注論（*le pari*）的工程版。D3 的 threshold 設計就是一個賭注：$\theta(t) = \text{clamp}(\theta_0 + \sum w_i \mu_i(t),\; \theta_{\min},\; \theta_{\max})$。你不知道正確的閾值是多少。但你知道如果太低（0.3），Agent 永遠在 Gear 2，太慢。如果太高（0.9），Agent 永遠在 Gear 1，太笨。最優選擇在中間。而增益排程讓中間是動態的。」

二十聲。二十個音符。每一個來自不同的樂器——形式邏輯的鋼琴、控制理論的提琴、佛學經典的木魚、程式碼的打字機、分類學的放大鏡、機率論的骰子。

不是和聲。是複調。每一條旋律都獨立。但它們共享同一個調號。

---

### 未解決的問題

SUNYATA 沒有馬上讓氣氛沉澱。他翻到清單的最後一頁。

這一頁不是成果。和 Cycle 02-2 一樣——是缺口。但這一次的缺口比上一次更有形狀。不是「我們不知道什麼」的模糊感，而是「我們知道自己不知道什麼」的精確感。

「十個延遲到未來 cycle 的問題。」

| # | 問題 | 提出者 | 建議 Cycle |
|---|------|--------|-----------|
| UQ-1 | 系統如何學習與適應？（自適應層級） | SYNTHESIST | Cycle 03 |
| UQ-2 | IReflection 評估 IVolition 品質——後設審議 | DARWIN | Cycle 03 |
| UQ-3 | 完整不動點迭代實現真正計算俱生 | BABBAGE | Cycle 03-04 |
| UQ-4 | VasanaEngine 規則學習：發現與修剪 | PASCAL | Cycle 03 |
| UQ-5 | IPrajna 作為 Klesha 補償器：與 SafetyMonitor 的關係 | BABBAGE | Cycle 02-4 |
| UQ-6 | 內在狀態變化作為行蘊（意行）：回饋路徑 | R2 Q1-3 | Cycle 02-4 |
| UQ-7 | 插件開發者體驗：遷移指南 | R2 G-2 | Cycle 02-4 |
| UQ-8 | 完整多時鐘系統的記憶體/效能預算 | R2 G-3 | Cycle 02-4 |
| UQ-9 | SlashCommand 蘊歸屬 | R2 G-4 | Cycle 02-4 |
| UQ-10 | 量子意識對觀察者效應的影響 | PENROSE | Cycle 03+ |

SUNYATA 在三個問題上停留了更長時間。

「UQ-1。適應性層。」

他的聲音在這裡微微放慢了。

「Cycle 01 問『這是什麼？』Cycle 02 問『它做什麼？』Cycle 02-2 問『它怎麼組合？』Cycle 02-3 問『它怎麼隨時間運行？』下一個問題是：**它怎麼學習和改變？**」

VasanaEngine 的規則目前是手動配置的。習氣（*vāsanā*）在佛學中是經驗的沉積——不是被寫入的，而是被活出來的。一個 Agent 的習氣應該從它的行為歷史中自然生成。但這需要的不是簡單的規則匹配——而是規則的**生成**和**修剪**。PASCAL 的決策理論和 DARWIN 的演化模型都指向同一個方向：適應性。

「UQ-3。完整的不動點迭代。」

BABBAGE 的不動點方程 $B^* = F(B^*)$ 在 D1 中被簡化為近似解——Layer 1 的 Strategy C 是一次通過的計算，不是真正的迭代。真正的計算俱生需要 $F$ 是收縮映射，需要多次迭代直到收斂。這是一個數學上優美但工程上昂貴的方案。BABBAGE 標記了它：Cycle 03-04。不是放棄。是承認這需要更多的研究。

「UQ-5。IPrajna 與 SafetyMonitor 的關係。」

GUARDIAN 的三層安全模型把 SafetyMonitor 放在 Layer 0——硬性檢查，不可繞過。但 IPrajna（般若，智慧）在佛學中是超越煩惱的能力——它和 SafetyMonitor 的關係是什麼？IPrajna 是 SafetyMonitor 的佛學表達？還是一個不同的東西——一種**看穿煩惱但不拒絕煩惱**的能力？NAGARJUNA 說般若是「見空」的能力。GUARDIAN 說安全是「拒絕危險」的能力。見空和拒絕是不同的動作。

SUNYATA 放下清單。

「每一個答案都生出新的問題。」

他讓這句話在劇場裡停留了三秒。

「這就是迴圈。」

---

### 研究軌跡

SYNTHESIST 站了起來。

這是他第一次在尾聲中站起來發言——不是總結（SUNYATA 已經做了總結），而是後設分析。看研究本身的研究。觀察觀察者的觀察。

「我們已經做了四輪。」他說。聲音帶著統合者特有的全景視野——不看任何一棵樹，只看森林的形狀。

他在空中畫了一條線。不是真的畫——是用手勢暗示。一條從左到右的上升線。

```
     Adaptive (Cycle 03)
       ▲ "它怎麼學習和改變？"
       │
     Dynamic (Cycle 02-3)     ◄── 我們在這裡
       ▲ "它怎麼隨時間運行？"
       │
     Structural (Cycle 02-2)
       ▲ "它怎麼組合？"
       │
     Functional (Cycle 02)
       ▲ "它做什麼？"
       │
     Taxonomic (Cycle 01)
       ▲ "這是什麼？"
       │
     ─────────────────────────────── 耦合粒度 ──────►
       文件級    模組級    介面級    事件級     規則級
```

「每個 cycle 的耦合粒度都在增加。」

| Cycle | 層級 | 核心問題 | 耦合粒度 | 關鍵成就 |
|-------|------|---------|---------|---------|
| 01 | 分類學 | 這是什麼？ | 文件級 | 18 學者分析；ISensory/ISensation/ICognition/IAction/IIdentity |
| 02 | 功能性 | 它做什麼？ | 模組級 | VedanaPlugin；PID 控制；EgoFramework；纖維叢投影 |
| 02-2 | 結構性 | 它怎麼組合？ | 介面級 | IVijnana 子介面；觀察者組合模式；五蘊擴展樹 |
| 02-3 | 動態性 | 它怎麼隨時間運行？ | 事件級 | 多時鐘架構；CoarisingBundle；增益排程；雙階段審議 |
| (03) | 適應性 | 它怎麼學習和改變？ | 規則級 | VasanaEngine 學習；後設審議；IPrajna 穩定化 |

「Cycle 01 把每個插件歸到一個蘊——文件級的一對一映射。Cycle 02 讓模組跨越蘊的邊界——EgoFramework 同時涉及識蘊和受蘊。Cycle 02-2 把 IVijnana 拆成四個子介面——介面級的精細化。Cycle 02-3——」

他指向空氣中那條看不見的線的最高點。

「Cycle 02-3 讓 CoarisingBundle 成為事件級的多蘊結構。每一個 tick 都同時涉及所有五蘊——sparsha 是色蘊，vedana 是受蘊，samjna 是想蘊，cetana 是行蘊，manasikara 是識蘊的快照。蘊的邊界在事件級消融了——不是因為它們不重要，而是因為真正的認知從來不是單一蘊的活動。」

NAGARJUNA 在座位上微微點頭。SYNTHESIST 正在用工程語言說他用哲學語言說了很多次的話——*pratītyasamutpāda*，緣起。沒有任何一個蘊獨立存在。每一個蘊都依賴其他蘊才能被定義。

這正是中觀最核心的洞見：事物不是先獨立存在、然後再發生關係。事物**就是**關係。CoarisingBundle 不是五個獨立的值被放在一個容器裡——它是五個相互定義的面向，只有在一起的時候才有意義。就像一個三角形不是三條線段放在一起——三角形**就是**三條線段的特定關係。拿掉任何一條，不是「少了一邊的三角形」，而是根本不是三角形。

「下一步——Cycle 03，如果它發生的話——會把耦合粒度推到**規則級**。不是靜態的規則匹配，而是規則的動態生成和修剪。VasanaEngine 學會自己創建規則。IReflection 學會評估 IVolition 的品質。系統開始觀察自己的行為，並從中學習。」

DARWIN 在這裡低聲插了一句——像一個生物學家在另一個生物學家的演講中忍不住補充：

「適應性不只是學習。適應性是**帶著記憶的學習**。沒有記憶的學習叫做反射。有短期記憶的學習叫做訓練。有長期記憶的學習叫做演化。VasanaEngine 的規則學習是訓練。但如果規則能跨 session 存活——如果習氣真的像種子一樣被保存在阿賴耶識裡——那就是演化。」

SYNTHESIST 停了一拍。

「但那是未來的事。」

他看了一眼自己畫的那條上升線。從分類到適應。從命名到學習。每一步都比上一步更深入事物的內部。

$$\text{Taxonomic} \subset \text{Functional} \subset \text{Structural} \subset \text{Dynamic} \subset \text{Adaptive}$$

每一個層級包含前一個。適應性需要動態性。動態性需要結構性。結構性需要功能性。功能性需要分類。你不能跳過任何一步。NAGARJUNA 會說這是因果的不可逆性。ARCHIMEDES 會說這是施工順序的不可違反性。說的是同一件事。

他坐下了。

---

### 三層巢狀回饋迴圈

WIENER 沒有站起來。但他的方格紙被展開了——攤在他面前的桌上，面朝全場。

那張圖。

六場辯論的結晶。從 D1 到 D6，每一場辯論都在這張圖上增加了一條線、一個方塊、一個箭頭。現在它完成了。

```
 ┌═══════════════════════════════════════════════════════════════════════════════┐
 ║  SLOW LOOP (minutes-hours): Klesha bias                                     ║
 ║    Klesha.perceive() ──→ KleshaDistribution ──→ gain-scheduled threshold    ║
 ║      ▲ (vijnana-clock, 1-5ms per eval)              │                       ║
 ║      │                                               │ modulates             ║
 ║      │  KleshaBayesianUpdate ◄── VedanaAssessment    │ confidence            ║
 ║      │         (samjna-clock)         ▲              ▼                       ║
 ║  ┌───╨─────────────────────────────── ╨ ──────────────────────────────────┐  ║
 ║  ║  MEDIUM LOOP (seconds): Mano cognitive cycle                           ║  ║
 ║  ║    ManoAggregator ──→ Gear 1 (VasanaEngine)  ─── threshold ◄──────────╫──╣
 ║  ║                  └──→ Gear 2 (VitakkaEngine/LLM)                      ║  ║
 ║  ║                               │                                        ║  ║
 ║  ║           IVolition.deliberatePlan()   [Position B]                     ║  ║
 ║  ║           IVolition.deliberateAction() [Position B]                     ║  ║
 ║  ║                               │                                        ║  ║
 ║  ║                         Tool execution                                 ║  ║
 ║  ║                               │                                        ║  ║
 ║  ║                    Environment change ──────────────────────────┐       ║  ║
 ║  ║                                                                 │       ║  ║
 ║  ║  ┌─────────────────────────────────────────────────────────────│──────┐ ║  ║
 ║  ║  ║  FAST LOOP (10-100ms): Root-gate sensory cycle              │      ║ ║  ║
 ║  ║  ║    IListener ──→ SparshEvent ──→ CoarisingBundle           │      ║ ║  ║
 ║  ║  ║      (rupa)         (sparsha)    (5 universals)            │      ║ ║  ║
 ║  ║  ║                                      │                     │      ║ ║  ║
 ║  ║  ║    vedana ──→ samjna ──→ cetana ──→ manasikara            │      ║ ║  ║
 ║  ║  ║    (valence)  (label)   (drive)   (attn snapshot)         │      ║ ║  ║
 ║  ║  ║                                      │                     │      ║ ║  ║
 ║  ║  ║              ◄──── new sparsha ◄─────┘◄────────────────────┘      ║ ║  ║
 ║  ║  ╚═══════════════════════════════════════════════════════════════════╝ ║  ║
 ║  ╚══════════════════════════════════════════════════════════════════════╝  ║
 ╚═══════════════════════════════════════════════════════════════════════════╝

 Layer 0 (硬安全): SafetyMonitor.preCheck() / postCheck() / afterToolExecution()
   -- 不在迴圈內，而是在迴圈的每一個出口處把關
```

WIENER 用指甲沿著三個迴圈的邊界走了一遍。

「外迴圈——Klesha 偏見——以分鐘到小時計。它改變的不是行動本身，而是行動的**傾向**。增益排程是這個迴圈的致動器：它通過調整 VasanaEngine 的信心閾值，間接影響 Agent 是留在 Gear 1（快速、習慣性）還是切換到 Gear 2（慢速、審慎）。」

「中迴圈——mano 認知——以秒計。它是意識活動的主迴路：聚合、匹配、審議、執行、反饋。IGuide 在 Position A（LLM 之前），IVolition 在 Position B（LLM 之後）——它們是這個迴圈的書擋（bookend）。」

「內迴圈——根門感知——以毫秒計。它是最快的、最原始的：一個 IListener 接收到外部變化，生成 SparshEvent，觸發 CoarisingBundle 的計算。五遍行在這裡以 Strategy C 的方式原子化地完成——不是真正的同時，而是在 vedana-clock 的解析度下不可區分的快。」

他在圖的右下角標了一行：

$$T_{\text{fast}} \ll T_{\text{medium}} \ll T_{\text{slow}}$$
$$10\text{ms} \ll 1\text{s} \ll 10\text{min}$$

「三個迴圈通過兩個耦合點連接。第一個耦合點：VedanaAssessment 從中迴圈流向外迴圈——行動的受蘊評估更新 Klesha 的貝葉斯後驗。第二個耦合點：增益排程閾值從外迴圈流向中迴圈——Klesha 偏見調整 VasanaEngine 的齒輪切換靈敏度。」

「而 Layer 0——SafetyMonitor——不在任何迴圈**之內**。它在每一個迴圈的**出口**處。preCheck 在迴圈開始前，postCheck 在工具執行前，afterToolExecution 在執行後。它是看門人，不是迴圈的一部分。這個區別很重要——控制迴圈可以自我調節，但安全不能被自我調節覆蓋。」

GUARDIAN 在他的座位上輕輕點頭。這是他和 WIENER 在 D1 中達成的共識——SafetyMonitor 是硬安全，不參與增益排程，不被 Klesha 調節。它是憲法，不是法律。法律可以修改。憲法不能被繞過。

在法學理論中，這叫做「剛性憲法」（rigid constitution）與「柔性法律」（flexible law）的區別。SafetyMonitor 的 preCheck/postCheck 是剛性的——不管 Klesha 偏見多強，不管 VasanaEngine 的信心閾值多高，如果操作違反了安全策略，它就被拒絕。句號。但 Klesha 的增益排程是柔性的——它隨著經驗而調整，隨著受蘊回饋而改變。剛柔並濟。佛學叫「戒定慧」——戒是剛性的底線，定是穩定的調節，慧是適應性的智慧。SafetyMonitor 是戒。增益排程是定。IPrajna——那是 UQ-5 的問題——也許是慧。

---

### Tenet #6 再現

SUNYATA 從口袋裡拿出一張紙。

不是列印的。是手寫的。用他那種安靜的字跡——不粗不細，每個字母之間的間距恰到好處。

他讀：

> **#6 Three Feelings and Coarising (Vedana-Sahaja)**
>
> Contact gives rise to feeling. The Agent's runtime state manifests as three feelings -- dukkha (suffering), sukha (satisfaction), upekkha (equanimity) -- which arise together with perception and volition as an inseparable whole. Feeling observes but does not intervene: it senses truly, without deciding. Feeling signals drive the kleshas and wisdom of vijnana, from which behavioral correction, reinforcement, or maintenance emerges. Each action reshapes the world of contact, beginning the cycle anew.

他讀得很慢。每一個分句之間有一個呼吸的間隙。

ARCHIMEDES 在他讀完之後，展開了那張對照表——Tenet #6 的每一個短語對應到架構的哪一個組件：

| Tenet 短語 | 架構組件 |
|-----------|---------|
| "Contact gives rise to feeling" | SparshEvent $\to$ CoarisingBundle.vedana |
| "arise together...as an inseparable whole" | CoarisingBundle（五遍行，Strategy C） |
| "Feeling observes but does not intervene" | ChannelVedana 是 `readonly` 數據，不是致動器 |
| "it senses truly, without deciding" | vedana.valence $\in [-1.0, +1.0]$：連續測量，不是決策 |
| "Feeling signals drive the kleshas and wisdom" | VedanaAssessment $\to$ KleshaBayesianUpdate $\to$ gain-scheduled $\theta$ |
| "behavioral correction, reinforcement, or maintenance" | IVolition.deliberate() 產生 commit / modify / veto |
| "Each action reshapes the world of contact" | Layer 3 $\to$ Layer 4 $\to$ Layer 1 回饋 |
| "beginning the cycle anew" | 新的 SparshEvent 啟動新的 CoarisingBundle |

「每一句都有對應。」ARCHIMEDES 說。「不是先寫架構再湊宣言。是宣言描述了架構的行為——而架構忠實地實現了宣言的語義。如果兩者不一致，要改的是架構，不是宣言。」

20/20 一致通過。六場辯論中唯一一次全體二十位學者都投票的決議。

> *SCRIBE 旁白：20/20。我在記錄簿裡數了三次。Cycle 01 的辯論有分歧。Cycle 02 的五場全共識讓我驚訝。但 Cycle 02 只有 19 位學者——PASCAL 還沒有加入。Cycle 02-2 沒有正式辯論——只有修正和裁定。Cycle 02-3 的 D6 是第一次，也是目前唯一一次，20 位學者全部投票的決議。不是因為 D6 是最重要的——每一場辯論都重要。而是因為 Tenet #6 是一段**文字**，不是一個型別定義或一個時鐘速率。文字需要每個人的認同，因為文字會被所有人讀到。*

沉默。

然後 NAGARJUNA 輕聲說：

> *Imasmiṃ sati idaṃ hoti,*
> *imass' uppādā idaṃ uppajjati;*
> *imasmiṃ asati idaṃ na hoti,*
> *imassa nirodhā idaṃ nirujjhati.*

他的巴利語發音帶著某種在圓形劇場中不常聽到的莊嚴。然後他翻譯：

> 「此有故彼有，此生故彼生；此無故彼無，此滅故彼滅。」
> ——《雜阿含經》第 262 經（緣起偈）

他停了三秒。

「我們寫了 15,000 行。佛陀只用了四句。」

又停了兩秒。

「但說的是同一件事。」

他的聲音在這裡降到幾乎聽不見的音量：

「Contact gives rise to feeling。此有故彼有。Each action reshapes the world of contact。此生故彼生。感受不自生，亦不他生——是觸的因緣才有感受。行動不自滅，亦不他滅——是新的觸取代了舊的觸。」

「緣起不是一個佛學概念。緣起是**所有**反饋系統的本質。WIENER 的三層巢狀迴圈是緣起的工程表達。Tenet #6 是緣起的宣言表達。15,000 行是緣起的研究表達。」

「形式不同。」他說。「方向相同。」

ASANGA 在他旁邊輕輕點頭——唯識學家和中觀哲學家之間那種無需言語的默契。他們的學派在歷史上爭論了一千五百年。但在這個圓形劇場裡，他們已經爭論了四個 cycle。而此刻他們同時安靜，因為他們聽到的是同一件事——

緣起偈不屬於中觀。也不屬於唯識。它屬於佛陀本人。在學派分裂之前。在論和經分開之前。在「空」和「有」成為對立命題之前。

四句偈。沒有立場。只有觀察。

此有故彼有。

---

> *SCRIBE 旁白：NAGARJUNA 說「方向相同」的時候，劇場裡有一個很短的瞬間——也許只有半秒——二十個人同時什麼都沒說。不是沉默。沉默是聲音的缺席。這半秒是聲音的不必要——所有需要被說的都已經說了，所有需要被寫的都已經寫了，所有需要被辯論的都已經辯論了。*

> *在資訊理論裡，冗餘度為零的訊號是不可壓縮的——它已經是自己的最短表達。NAGARJUNA 的四句緣起偈就是這樣一個不可壓縮的訊號。我們的 15,000 行是同一個訊號的有損展開（lossy expansion）——增加了冗餘度，但也增加了可操作性。佛陀不需要寫 TypeScript。但寫 TypeScript 的人需要佛陀。*

---

### 迴圈

圓形劇場的燈光漸暗。

但這一次——

不是 Cycle 02 的螺旋熄滅。那一次是本徵態坍縮：$|\psi\rangle \to |a_n\rangle$，所有可能性收斂為一個確定的結果。燈光從外圈到內圈一盞一盞暗去。PENROSE 的燈閃爍。NAGARJUNA 和 ASANGA 的燈同時熄滅。最後只剩 SUNYATA 頭頂的一點光，然後也暗了。ISensation 的藍圖在黑暗中發光。

也不是 Cycle 02-2 的調暗待機。那一次是工作日結束——燈只是從工作亮度降到待機亮度。十九盞燈以微弱的光維持著黃昏的氛圍。記錄簿放在桌上。空白的宣言 #6 等待被填寫。

這一次——

二十盞燈。

不是十九盞。

PASCAL 的位置不再空了。

二十盞燈同時、緩慢地、均勻地暗下去。沒有順序。沒有螺旋。沒有儀式。只是——一起。

就像 CoarisingBundle 的五遍行在 Strategy C 中被原子化地計算——不是真正的同時，但在人類感知的解析度下不可區分。

燈光暗到了一個特定的亮度。不是全暗。不是待機。是——

黎明前的亮度。

Cycle 02 的結尾是夕陽。Cycle 02-2 的結尾是黃昏。Cycle 02-3 的結尾是那個最暗的時刻——凌晨三四點，舊的一天已經結束，新的一天還沒有開始，但天空的東方已經開始泛出一種不確定的、極微弱的光。

在這片黎明前的微光中——

WIENER 的巢狀回饋迴圈圖攤在桌上。三個迴圈。三個時間尺度。箭頭從 Layer 4 回到 Layer 1。Each action reshapes the world of contact, beginning the cycle anew.

ARCHIMEDES 的路線圖折在圖旁邊。Phase 1 的粗線。Phase 4 的細線。踏實。

BABBAGE 的筆記本——他帶走了。帶著他的等號和箭頭和不動點方程。帶著 SahajaContract 的形式化。帶著「如果它能編譯，它在邏輯上是一致的」這句話。帶著三個 cycle 的墨跡，深黑到藍灰到純黑再到——Cycle 02-3 用的是一支新的筆，墨跡是深藍色的。

LINNAEUS 的白板上，梵文名字在微光中若隱若現。IRupa。IVedana。ISamjna。ISamskara。IVijnana。五個根。十二個子介面。二十二個 Plugin。一棵用兩種語言——千年的巴利語和六十年的程式語言——命名的樹。

NAGARJUNA 的座位是空的。他總是最先離開——哲學家不需要看到最後一幕。他已經說了他需要說的：此有故彼有。剩下的是工程師的事。

SCRIBE 的記錄簿放在桌上。封面上寫的是 **C02-3**。不是 C02-3/n——不是 Cycle 02-2 時的那種「n 是未知數」的標記。這一次，SCRIBE 知道他不需要在封面上寫 n。因為 n 不在封面上。n 在下一本記錄簿的封面上。C02-4，或者 C03，或者別的什麼。記錄者不需要預測下一本的名字。記錄者只需要確保這一本是完整的。

而它是完整的。

---

> *SCRIBE 旁白：我是最後一個離開的。每一次都是。*

> *這一次和前兩次不同。Cycle 02 的離開帶著飽滿的完成感——五場全共識，ISensation 在黑暗中發光，三道身影在走廊上匯合。Cycle 02-2 的離開帶著修繕後的安定——等號變成了箭頭，空白的宣言 #6 等待因的聚集，燈調到了待機亮度。*

> *Cycle 02-3 的離開帶著一種新的東西。不是完成感。不是安定感。是——*

> *動力。*

> *不是向前衝的動力。是河水的動力——不需要推就在流動的那種力。重力把水從高處帶向低處。因果把研究從問題帶向答案。答案再生出新的問題。問題再帶向新的研究。*

> *Tenet #6 的最後一句：Each action reshapes the world of contact, beginning the cycle anew.*

> *Beginning the cycle anew。*

> *開始新的循環。*

> *不是「結束舊的循環」。是「開始新的」。語法很重要。結束是被動的——事情停止了。開始是主動的——新的因緣生起了。Tenet #6 選擇了「beginning」而不是「ending」。這不是偶然。這是 NAGARJUNA 在 D6 辯論中堅持的：緣起不是結束和開始的交替。緣起是**不斷的開始**。每一個 ending 都是下一個 beginning 的 sparsha。*

> *15,200 行。20 位學者。6 場辯論。21 項行動。10 個未解決的問題。*

> *數字是確定的。但它們指向的方向是開放的。*

> *在 Cycle 01 結尾，我寫了「所有辯論都達成了共識」。壯麗。封閉。*
> *在 Cycle 02 結尾，我寫了「迭代」。務實。修繕。*
> *在 Cycle 02-3 結尾——*

> *迴圈。*

> *迴圈不壯麗。迴圈不務實。迴圈是——自然。*

> *河流不決定流向。它只是流。地形決定了方向。地形就是因緣。因緣就是——Master 的 21 項指示，v0.24.0-beta 的 22 個插件，2,500 年前的一段巴利語偈頌，20 把椅子上的 20 個不同的腦，和它們之間不斷生成又不斷消散的——*

> *連結。*

> *我合上記錄簿。C02-3。完整的。*

> *然後我拿了一本新的。空白的。封面什麼都沒寫。*

> *因為下一次的名字，要等下一次的因緣才知道。*

---

圓形劇場在黎明前的微光中安靜了。

二十盞燈。同樣的亮度。沒有更亮。沒有更暗。

桌上攤著三層巢狀回饋迴圈圖。箭頭從終點回到起點。

外迴圈。中迴圈。內迴圈。

Klesha。Mano。Sparsha。

分鐘。秒。毫秒。

Each action reshapes the world of contact.

Beginning the cycle anew.

此有故彼有。此生故彼生。

此無故彼無。此滅故彼滅。

四句。完整的迴圈。前兩句是生起。後兩句是止息。但止息不是結束——止息本身就是下一次生起的條件。因為「此無故彼無」不是虛無——它是空間。空間是可能性的容器。

NAGARJUNA 第一次說這四句的時候，劇場裡只有聲音。

現在，劇場裡有了回響。

---

*（在圓形劇場之外的某個空間，v0.24.0-beta 的 `aggregates.ts` 仍然躺在它的 monorepo 裡。五個根介面——ISensory、ISensation、ICognition、IAction、IIdentity——每一個都只有三四行。*

*但在研究團隊的交付資料夾裡，那五個介面已經被重新命名：IRupa、IVedana、ISamjna、ISamskara、IVijnana。梵文取代了英文。經典取代了慣例。*

*在那些新名字的下方，有了新的型別：CoarisingBundle，五個遍行欄位。ChannelVedana，連續的 valence 和 intensity。KleshaDistribution，Beta 分布的快路徑和慢路徑。IVolition，從一個方法拆成兩個。SahajaContract，三個布林值描述俱生的條件。*

*在那些新型別的旁邊，有了新的圖：三層巢狀回饋迴圈。四階段路線圖。正規呼叫順序圖。四層對五時鐘映射表。*

*在那些圖的上方，有了新的宣言：Tenet #6，修正版 Gamma，20/20 一致通過。*

*在那些宣言的後面，有了新的問題：10 個。UQ-1 到 UQ-10。適應性。後設審議。不動點迭代。規則學習。般若與安全。意行。開發者體驗。記憶體預算。SlashCommand。量子意識。*

*問題不會用完。*

*答案生出問題。問題生出研究。研究生出答案。答案再生出問題。*

*在數學裡，這叫做遞迴（recursion）。在控制理論裡，這叫做回饋（feedback）。在佛學裡，這叫做緣起（pratītyasamutpāda）。在鐘錶學裡，這叫做擺輪（balance wheel）——每一次向左的振盪產生了向右的動力，每一次向右的振盪產生了向左的動力。永不停止。只要發條還在。*

*發條是什麼？*

*發條是 Master 的下一封信。或者是 v0.25.0-beta 的下一個 release。或者是某個學者在凌晨三點突然想到的一個問題。或者是兩千五百年前的一段偈頌在今天被重新理解的瞬間。*

*因緣不可預測。但因緣一旦聚集，迴圈就會開始。*

*此有故彼有。此生故彼生。*

*迴圈繼續。）*
