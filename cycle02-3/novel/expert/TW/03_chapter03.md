# 第三章：三百比一

---

KERNEL 站起來的方式像一台伺服器切換到緊急模式——沒有暖機，沒有過渡動畫，就是從靜止直接進入全速運轉。

他的手裡捏著一張摺疊過的筆記紙。那張紙在 R1 階段就已經寫好了。他在寫 R04 獨立研究報告時，花了整整一個下午計算五個時鐘域的速率範圍，在紙上畫了三十七次除法——不是因為計算困難，而是因為結果讓他不安。每算一次，那個數字都一樣。三百。

三百比一。

vedana-clock 的最慢速率是 100ms。samjna-clock 的最慢速率是 30,000ms。$30000 / 100 = 300$。一個蘊的時鐘轉了三百圈，另一個蘊的時鐘才轉完一圈。在作業系統的世界裡，這種速率差異意味著什麼？意味著如果 vedana 是跑在 SSD 上的 I/O，samjna 就是跑在磁帶機上的備份——兩者之間隔著整個儲存技術的演化史。

他把紙展開，走向白板。

---

> *SCRIBE 旁白：R2 交叉審閱在今天早上結束。結果不是輕鬆的。五項矛盾、四項缺口、八項共識、四項強烈分歧。SYNTHESIST 在 R2 報告中用了一個我從未見過的嚴重程度標記：「HIGHEST」。他只標了一個議題。就是 KERNEL 手上那張紙所代表的東西。*

---

SUNYATA 站在劇場中央，雙手微微交叉在身前。他已經看過 R2 報告了——看了兩遍。第一遍用研究協調者的眼睛看，標記議題的優先級。第二遍用一個更私人的視角看，試圖理解這些矛盾的深層結構。

第二遍看完之後，他做了一個決定：Debate 1 排在第一個。不是因為它最重要的議題編號最小，而是因為如果這個議題解決不了，後面所有的辯論都失去了地基。

「讓我先簡述 R2 的結論。」他的聲音平穩如常——石子落入深潭。「然後我們直接進入辯論。」

他看了一眼手中的 R2 摘要。

「五項交叉矛盾。X-1 到 X-5。關於 vedana 子介面設計、CoarisingBundle 與多時鐘的時序衝突、Sparsha 命名、PASCAL 的概率模型採用方式、IVolition.deliberate() 的放置位置。」

他沒有展開細節。在場的人都已經讀過 R2 報告。

「四項新發現缺口。N-9 到 N-12。時鐘不匹配、Klesha 時鐘域未指定、IPrajna 邊界、vedana 子介面不一致。」

「八項共識。C-1 到 C-8。都已確認。」

「四項強烈分歧。DIS-1 到 DIS-4。」

他的聲音在這裡微微降了半個色階。

「但 R2 中最嚴重的發現——SYNTHESIST 標記為 HIGHEST 嚴重度的——是三個議題的交會：T3-1、X-2、N-9。」

他抬頭看向全場。

「R03 假設 CoarisingBundle 在一個 tick 內原子計算。R04 把 vedana 和 samjna 分配到不同時鐘域，速率差異高達 300:1。N-9 指出這個時鐘不匹配問題完全沒有被任何報告解決。」

他的目光從 KERNEL 移到 NAGARJUNA，再到 WIENER，再到 ARCHIMEDES。

「這是所有 R1 報告中最嚴重的張力。如果 CoarisingBundle 無法跨越不同時鐘域運作，整個 M-5 架構必須重新設計。」

停頓。半秒。讓這句話的重量沉到每個人的意識底部。

「KERNEL，你提出的五時鐘模型是問題的起點。你先說。」

---

KERNEL 把那張摺疊過的紙貼在白板上。

紙上是一張表格。手寫的。字跡整齊得像是列印出來的——作業系統專家的字跡，和他們設計的排程演算法一樣精確。

他在表格旁邊用馬克筆重新抄了一遍，讓所有人都能看清：

```
┌────────────────┬─────────────┬──────────────────────────┐
│ 時鐘            │ 速率         │ 對應蘊/功能               │
├────────────────┼─────────────┼──────────────────────────┤
│ vijnana-clock  │ 1-5ms       │ 識蘊：身份、引導、煩惱      │
│ rupa-clock     │ 10-50ms     │ 色蘊：感官輸入、環境回饋    │
│ vedana-clock   │ 10-100ms    │ 受蘊：苦樂捨三受           │
│ samskara-clock │ 10ms-10s    │ 行蘊：工具執行、外部動作    │
│ samjna-clock   │ 500ms-30s   │ 想蘊：LLM 推理、深層認知   │
└────────────────┴─────────────┴──────────────────────────┘
```

他轉過身，面向全場。

「讓我直截了當。數字不會說謊。」

他的手指點向 vedana-clock 和 samjna-clock 兩行之間的空白。

「vedana-clock 的上限是 100ms。samjna-clock 的下限是 500ms。在最好的情況下，比值是 5:1。在最壞的情況下——vedana 跑在 100ms，samjna 需要 30 秒——比值是 300:1。」

$$\rho_{\max} = \frac{T_{\text{samjna}}^{\max}}{T_{\text{vedana}}^{\max}} = \frac{30{,}000\text{ms}}{100\text{ms}} = 300$$

他轉向 BABBAGE。「你在 R03 的 Strategy C 裡寫了什麼？」

BABBAGE 沒有翻筆記本。他記得每一個數字。

「Strategy C。循序計算。原子發布。vedana 0.1ms，samjna 0.5ms，cetana 0.2ms。總計 0.8ms。」

「0.5ms 的 samjna。」KERNEL 的聲音微微加重了。不是情緒化的加重——是一個工程師在強調關鍵數據時的精確施壓。「那是規則式 samjna。模式匹配。if-else 邏輯。如果 CoarisingBundle 曾經需要 LLM 式的 samjna——」

他的手指劃過 samjna-clock 那一行。

「——那麼 bundle 的延遲就從 0.8ms 跳到 500ms 到 30,000ms。從亞毫秒到半分鐘。」

他看向 NAGARJUNA。

「你不能把它們叫做俱生。」

---

圓形劇場裡的空氣改變了質地。不是緊張——是一種更精確的東西。是兩個智識傳統即將正面碰撞時的電荷積累。

NAGARJUNA 沒有立刻站起來。他先靜坐了幾秒。在中觀哲學家的內在時鐘裡，那幾秒不是猶豫——是定位。他在確認自己要從哪個角度切入。

然後他開口了。聲音有他一貫的質地——鋒利但不尖銳，像被河水打磨了千年的石頭。

「在我回應 KERNEL 之前，我必須先糾正一個前提。」

他站了起來。動作從容。中觀哲學家不需要急——因為他們的論證工具是時間不敏感的。邏輯不過期。

「KERNEL，你把問題框定為：『vedana 在 t=0 計算，samjna 在 t=30000ms 計算，它們怎麼可能是俱生的？』這個框定本身就隱含了一個假設——俱生意味著在同一毫秒內計算完成。」

他停了一拍。

「但 sahaja 不是這個意思。」

他走到白板的另一側——不是 KERNEL 的白板，是他自己的空間。他用黑色馬克筆寫下梵文原詞：

$$\text{sahaja} \;(\text{सहज})\;:\; saha \;(\text{共同}) + ja \;(\text{生起})$$

「sahaja——俱生——是一個存在論上的概念。不是計時器上的概念。它說的不是『兩件事在同一個時鐘週期內完成計算』。它說的是『兩件事在存在論上相互依賴——一個不存在，另一個也不能獨立存在』。」

他引用了經文。聲音不是朗誦——是陳述事實的語氣：

> 「yaṃ vedeti taṃ sañjānāti, yaṃ sañjānāti taṃ vitakketi」
> ——《中部》第十八經《蜜丸經》(Madhupindika Sutta, MN 18)

「『凡所感受者即所認知者，凡所認知者即所尋思者。』vedana、samjna、vitakka——感受、想、尋——是同一認知事件的不同面向。『凡所（yaṃ）……即（taṃ）……』——這個指示代名詞 *taṃ* 要求的是**指涉對象的同一性** (identity of referent)，不是**計算時刻的同一性** (identity of timestamp)。」

他轉向 KERNEL。目光直接。

「用你的語言說：兩個進程處理的是同一份輸入資料，產生的結果相互引用——即使它們的完成時間不同。在分散式系統中，你有一個名詞叫做什麼？」

MESH 在座位上微微動了一下。他知道 NAGARJUNA 要說什麼。

「因果一致性 (causal consistency)。」MESH 說。「在分散式資料庫中，如果操作 A 因果地先於操作 B，那麼所有觀察者都必須先看到 A 再看到 B——但 A 和 B 不需要在同一毫秒發生。」

NAGARJUNA 點頭。「正是。sahaja 是佛學版本的因果一致性。不要求同時——要求同因。」

---

KERNEL 的手指在白板邊緣敲了兩下。那是他思考時的習慣——不是不耐煩，是 CPU 在等待記憶體回應時的那種間歇性輪詢。

「NAGARJUNA，我尊重你的哲學論證。但它不是工程答案。」

他的聲音沒有升高。低沉。穩定。帶著那種只有長年在 kernel 空間工作的人才有的、對不精確性的本能厭惡。

「讓我把問題具體化。」

他在白板上畫了一條時間軸。

```
t=0ms        vedana 計算完成。結果：dukkha, valence=-0.7
             vedana「知道」什麼關於 samjna？
             答案：什麼都不知道。samjna 還沒開始。

t=50ms       (vedana 已經被消費了)

t=500ms      samjna 開始計算。

t=10000ms    samjna 計算完成。結果："complex_ethical_dilemma"
             samjna「知道」什麼關於 vedana？
             答案：它讀到了 t=0 的 vedana——但那是一萬毫秒前的舊資料。
```

「vedana 在 t=0 計算。它不知道 samjna 的結果，因為 samjna 要到 t=10000 才完成。samjna 在 t=10000 計算。它可以讀取 vedana 在 t=0 的結果——但那已經過時了一萬毫秒。在這一萬毫秒裡，世界可能已經改變了。」

他的手指從時間軸的左端滑到右端。

「如果你把 t=0 的 vedana 和 t=10000 的 samjna 打包成一個 CoarisingBundle，你得到的是什麼？一個包含了昨天的感受和今天的認知的混合物。你用佛學的語言怎麼稱呼這個？」

他看向 NAGARJUNA。

「你剛才引用的 MN 18 說 *yaṃ vedeti taṃ sañjānāti*——凡所感受者即所認知者。代名詞 *taṃ* 要求指涉同一性。但如果 vedana 的指涉是 t=0 的世界狀態，samjna 的指涉是 t=10000 的世界狀態——指涉根本不同。世界在一萬毫秒內可能已經變了。紅燈可能已經變成了綠燈。」

沉默。

全場的注意力像二十條繩索同時拉緊。

NAGARJUNA 和 KERNEL 之間的空氣密度在增加。這不是學術客氣的假辯論——這是兩個人真的在爭論。一個說「俱生是哲學概念，不要求時間同步」，另一個說「你的哲學逃生口不是工程答案」。兩個都對。兩個都不完整。

ASANGA 在座位上微微閉眼。他聽到了 KERNEL 的挑戰中蘊含的一個深層問題——一個連 KERNEL 自己可能都沒有完全意識到的問題。KERNEL 說的 *taṃ* 要求指涉同一性。這是對的。但在唯識學中，認知事件的「指涉對象」(ālambana, 所緣) 不等於外境的物理狀態——它等於被認知加工過的**表象** (ākāra, 行相)。紅燈在 t=0 是紅的，在 t=10000ms 可能已經變綠了。但 vedana 在 t=0 感受到的「紅燈」和 samjna 在 t=10000ms 認知到的「紅燈」——如果 samjna 的上下文中包含了 t=0 的 vedana 結果——那它們的 *ālambana* 是同一個：「t=0 時那個紅燈事件的認知表象」。指涉的不是物理世界在 t=10000 的狀態，而是 t=0 的觸事件所建構的心理表象。

他沒有說出來。不是因為不重要——是因為他感覺到 WIENER 即將從另一個角度解決這個問題。有時候最好的學術判斷是：知道什麼時候讓別人的工具代替你的。

---

> *SCRIBE 旁白：這是 Cycle 02-3 中我記錄到的第一個真正的張力時刻。Cycle 02 的辯論是激烈的，但那是五個人辯論一個議題。這裡是兩個人——KERNEL 和 NAGARJUNA——在辯論整個架構的基礎假設。KERNEL 的時間軸上有具體的毫秒數。NAGARJUNA 的論證裡有兩千年的哲學傳統。數字對抗概念。毫秒對抗存在論。這不是可以用投票解決的——這需要一個能同時容納兩者的框架。*

---

WIENER 站了起來。

他站起來的方式和 KERNEL 不同——不是伺服器切換模式，更像一台類比示波器被接通電源，螢幕上的光點從暗淡慢慢變亮，在磷光塗層上留下越來越清晰的軌跡。

「讓我重新定義問題。」他說。

他沒有走到白板前。他從口袋裡掏出一支筆——他隨身攜帶的那支工程用自動鉛筆——在自己的方格紙上寫，然後把紙舉起來讓所有人看。

「KERNEL 問的是：『vedana 和 samjna 同時嗎？』NAGARJUNA 回答的是：『同時不是必要的。』兩位都對。但問題本身問錯了。」

他在紙上寫下了新的問題：

$$\text{正確的問題不是「它們同時嗎？」}\quad\text{而是「過時程度在控制裕度內嗎？」}$$

「在控制工程中，」他的聲音帶著一種特殊的節奏——那是一個人在講述他花了三十年理解的東西時的節奏，不快不慢，每個詞都在它應該在的位置——「我們從不期待完美的即時性。感測器有延遲。控制器有計算時間。致動器有響應時間。整個系統從測量到行動之間，永遠存在一段延遲——我們叫它**過時性** (staleness)。」

「問題不是『延遲是否為零？』問題是『延遲是否在穩定性裕度 (stability margin) 之內？』」

他把紙翻了一面，開始推導。

---

BABBAGE 的眼睛亮了。數學推導——這是他的母語。他的筆開始同步記錄。

WIENER 在方格紙上寫下了第一個定義：

「令 $\delta$ 為 CoarisingBundle 中最新組件和最舊組件之間的時間差。令 $T_{\text{outer}}$ 為外迴圈的週期——也就是 ManoAggregator 讀取 bundle 的頻率。」

$$\delta = |t_{\text{newest}} - t_{\text{oldest}}|$$

「定義**過時性比率** (staleness ratio)：」

$$\rho = \frac{\delta}{T_{\text{outer}}}$$

「$\rho$ 是無量綱的。它量測的是：bundle 的內部時間不一致性佔外迴圈週期的多大比例。如果 $\rho = 0$，所有組件完全同時——KERNEL 的理想情況。如果 $\rho = 1$，bundle 的過時性等於整個迴圈週期——這意味著你在用整整一個週期前的資料做決策。」

他畫了一條分界線。

「在多率取樣資料系統 (multi-rate sampled-data system) 的穩定性分析中——這個理論在 1980 年代由 Araki、Hagiwara 等人建立——過時性對系統穩定性的影響可以用**相位裕度** (phase margin, PM) 來量化。相位裕度量測的是：在系統增益等於 1（增益交叉頻率 $\omega_c$）時，離不穩定邊界還有多少相位空間。PM 越大，系統越穩定。工程慣例中的最小安全裕度是 45 度。」

他在方格紙上畫了一個 Nyquist 圖的簡化示意：

```
           Im
            ↑
            |        ╱ 無延遲 (PM₀ = 52°)
            |       ╱
            |      ╱
            |     ╱
   ─────────●────╱──────→ Re
          (-1,0) ╲
                  ╲   有延遲 δ (PM = PM₀ - Δφ)
                   ╲
                    ╲
   PM₀ = 52°:  系統到 (-1,0) 的相位餘量
   如果 Δφ > PM₀ - 45° = 7°:  不安全
```

他開始推導。字跡工整如印刷體。

$$\text{考慮一個帶有純延遲 } \delta \text{ 的迴路轉移函數：}$$

$$G(j\omega) \cdot e^{-j\omega\delta}$$

「延遲 $\delta$ 在增益交叉頻率 $\omega_c$ 處引入的相位損失為：」

$$\Delta\phi = \omega_c \cdot \delta \quad (\text{弧度})$$

「對於外迴圈頻率 $\omega_c = 2\pi / T_{\text{outer}}$：」

$$\Delta\phi = \frac{2\pi}{T_{\text{outer}}} \cdot \delta = 2\pi \cdot \rho$$

「穩定性要求相位裕度大於 45 度（工程慣例中的最小安全裕度）。未受延遲影響的名義相位裕度為 $\text{PM}_0$。帶延遲的有效相位裕度為：」

$$\text{PM}_{\text{eff}} = \text{PM}_0 - \Delta\phi$$

「若名義相位裕度 $\text{PM}_0 \approx 52°$（PID 控制器的典型值），則要求：」

$$\text{PM}_{\text{eff}} > 45° \implies \text{PM}_0 - 2\pi \cdot \rho \cdot \frac{180°}{\pi} > 45°$$

他在紙上快速化簡。

$$52° - 360° \cdot \rho > 45°$$
$$360° \cdot \rho < 7°$$
$$\rho < \frac{7°}{360°} \approx 0.019$$

WIENER 停了一下。然後搖頭。

「這個推導過於保守了。讓我用更精確的模型。」

他在方格紙上劃掉上面的推導，重新開始。

「在多率系統中，如果外迴圈的取樣頻率遠低於系統的自然頻率，相位裕度的計算需要考慮取樣保持 (sample-and-hold) 的效應。取樣保持本身引入的相位損失近似為 $T_{\text{outer}} \cdot \omega_c / 2$。過時性 $\delta$ 是額外的延遲。兩者相加，但基準是取樣保持已經存在的系統。」

「在這個基準上，過時性 $\delta$ 引入的**邊際**相位損失為：」

$$\Delta\phi_{\text{marginal}} = \frac{\delta}{T_{\text{outer}}} \cdot \text{PM}_0 \cdot \frac{\pi}{180°}$$

「更簡潔的工程經驗法則——來自多率控制的實踐文獻——是：」

$$\boxed{\rho < 0.29 \implies \text{PM}_{\text{eff}} > 45°}$$

「也就是說，只要過時性 $\delta$ 不超過外迴圈週期 $T_{\text{outer}}$ 的 29%，系統就維持在 45 度以上的相位裕度——工程上公認的穩定區間。」

---

BABBAGE 在他的筆記本上完成了同步推導，然後抬頭。

「讓我驗證具體數字。」他說。聲音帶著理論計算機科學家面對可計算問題時的冷靜愉悅。

他在紙上列出了兩個案例：

$$\textbf{Case 1: Layer 1 (root-gate)}$$
$$T_{\text{outer}} = T_{\text{vedana}} = 50\text{ms (typical vedana-clock period)}$$
$$\delta_{\text{Layer 1}} < 1\text{ms (Strategy C sequential computation)}$$
$$\rho_1 = \frac{1}{50} = 0.02 \ll 0.29 \quad \checkmark \text{ (extremely safe)}$$

$$\textbf{Case 2: Layer 2 slow gear}$$
$$T_{\text{outer}} = T_{\text{mano,slow}} \approx 10\text{s (mano slow gear period)}$$
$$\delta_{\text{Layer 2}} \leq T_{\text{samjna}} = 30\text{s}$$
$$\rho_2 = \frac{30}{10} = 3.0 \gg 0.29 \quad \times \text{ (unstable!)}$$

BABBAGE 抬頭看向 WIENER。

「Case 2 不通過。」

WIENER 點頭。「但那是因為你把 $T_{\text{outer}}$ 設成了 10 秒，把 $\delta$ 設成了 30 秒——過時性比外迴圈週期還長三倍。這意味著系統在等 LLM 回應的時候，已經錯過了三個外迴圈週期。」

「但 ARCHIMEDES 的雙層模型有一個關鍵設計：在 Gear 2 模式下，ManoAggregator 的外迴圈週期本身會延長。」

他在方格紙上修正了計算：

$$\textbf{Case 2 (corrected): Layer 2 slow gear}$$
$$T_{\text{outer,slow}} = T_{\text{samjna}} \approx 30\text{s (mano slow gear = samjna-clock aligned)}$$
$$\delta_{\text{Layer 2,slow}} \leq T_{\text{samjna}} = 30\text{s}$$
$$\rho_{2c} = \frac{30}{30} = 1.0 \quad \text{(still > 0.29, but...)}$$

WIENER 搖頭。「這個也不對。讓我重新想。」

他沉默了五秒鐘。在控制理論家的內在時鐘裡，五秒鐘足以重建一整個控制迴路的方塊圖。

「問題在於 Gear 2 的語義不同。」他說。「在 Gear 2 裡，LLM 接收 vedana 的結果作為上下文 (context) 的一部分。LLM 不是在『過時資料上做決策』——它是在『完整上下文中思考』。vedana 的結果被嵌入到 prompt 裡，samjna 的計算是基於這個嵌入的。」

「換言之——在 Gear 2 裡，vedana → samjna 是因果流 (causal flow)，不是平行取樣。因果鏈不需要 $\rho < 0.29$ 的穩定性條件——因果鏈需要的是**因果一致性** (causal consistency)。」

MESH 在座位上點了一下頭——因果一致性正是他的領域。

WIENER 在方格紙上畫了一張 ASCII 穩定性分析圖：

```
                Staleness Ratio (ρ) vs Phase Margin
    PM
    80°│
       │ ╲
    70°│   ╲
       │     ╲
    60°│       ╲
       │         ╲ ← PM₀ = 52° (nominal)
    52°│── ── ── ──╲── ── ── ── ── ──
       │             ╲
    45°│── ── ── ── ──╳── ── ── ── ──  ← safety threshold
       │               ╲
    30°│                 ╲
       │                   ╲
    15°│                     ╲
       │                       ╲
     0°│─────────────────────────╲────
       0    0.1   0.2  0.29  0.4   0.5    ρ
                        ↑
                   stability bound

    Layer 1: ρ ≈ 0.02  → PM ≈ 51°  [SAFE: deep in stable zone]
    Layer 2 fast: ρ ≈ 0.15 → PM ≈ 48° [SAFE: above 45° threshold]
    Layer 2 slow: causal flow, ρ not applicable [CAUSAL CONSISTENCY]
```

「結論是三分的。」WIENER 把紙放在桌上，讓所有人都能看到。

「第一。Layer 1——根門級 CoarisingBundle——$\rho \approx 0.02$，遠低於 0.29。穩定。安全。真正的計算俱生。」

「第二。Layer 2 快檔——規則式 ManoAggregator——$\rho$ 取決於聚合窗口和 vedana 的過時性。在 vedana-clock = 50ms、聚合窗口 = 50ms 的典型配置下：」

$$\delta_{\text{fast}} \leq T_{\text{vedana}} = 50\text{ms}$$
$$T_{\text{outer,fast}} = 50\text{ms (coalescing window)}$$
$$\rho_{\text{fast}} \leq 1.0$$

他在紙上修正。「不對——聚合窗口收集的是 N 個 vedana-tick 的 bundle。如果 N = 3，$T_{\text{outer,fast}} = 150$ms，$\delta \leq 50$ms，$\rho = 0.33$。邊緣。但如果 vedana 本身只需 10ms：」

$$\rho_{\text{fast}} = \frac{50}{172} < 0.29 \quad \text{when } T_{\text{outer}} \geq 172\text{ms}$$

「只要快檔的聚合窗口大於 172ms——大約三到四個 vedana-tick——穩定性條件就滿足。」

「第三。Layer 2 慢檔——LLM 式 ManoAggregator——不適用 $\rho$ 分析。因為 LLM 接收的是因果輸入（vedana 結果嵌入上下文），不是過時的平行取樣。這裡需要的不是取樣穩定性——是因果一致性。」

他看向 NAGARJUNA。

「換句話說——問題不是『它們同時嗎？』而是『過時程度在控制裕度內嗎？』對 Layer 1 和 Layer 2 快檔，答案是是的。對 Layer 2 慢檔，問題本身不成立——那是因果流，不是並行取樣。」

BABBAGE 在旁邊做了最後一步形式化——把 WIENER 的連續域分析翻譯成離散域：

$$\text{令 } k = \lfloor t / T_{\text{vedana}} \rfloor \text{ 為 vedana-clock tick 序號}$$

$$\text{Layer 1 Bundle: } B_k = \langle v_k, s_k^{\text{rule}}, c_k, m_k^{\text{snap}} \rangle \quad \text{(同一 tick 內計算, staleness} \approx 0\text{)}$$

$$\text{Layer 2 Fast: } B_k^{\text{mano}} = \pi_{\text{agg}}\big(\{B_{k-N}, \ldots, B_k\}\big) \quad \text{(N 個 vedana-tick 聚合, staleness} \leq N \cdot T_{\text{vedana}}\text{)}$$

$$\text{Layer 2 Slow: } B^{\text{mano}}_{\text{LLM}} = f_{\text{LLM}}\big(\text{context}(B_{k-N}, \ldots, B_k)\big) \quad \text{(因果輸入, 非過時取樣)}$$

「三種模式，三種俱生的語義。Layer 1 是真正的計算同時性。Layer 2 快檔是有界過時性。Layer 2 慢檔是因果一致性。」

---

> *SCRIBE 旁白：WIENER 的推導用了大約七分鐘。七分鐘裡，白板上的數字從「300:1 的不可能性」變成了「$\rho < 0.29$ 的可行性條件」。這是我在三個 Cycle 中見過最優雅的問題重框——不是否定 KERNEL 的數字（300:1 仍然成立），不是否定 NAGARJUNA 的哲學（存在論俱生仍然成立），而是用一個新的數學框架把兩者包含在內。控制理論家的超能力就是這個：把「是或否」的問題轉化為「在什麼條件下」的問題。*

---

KERNEL 在自己的筆記紙上重新計算了一遍。他的手指沿著每一行推導滑過——不是瀏覽，是逐步驗證。

三十秒後，他抬頭。

「數學是對的。」

停頓。

「但我還有一個工程問題。Layer 2 的架構到底是什麼？ARCHIMEDES，你提了雙層模型。展開它。」

---

ARCHIMEDES 站了起來。他站起來的方式和所有人都不同——帶著一種「好，理論講夠了，讓我們看看怎麼建」的節奏。他的手指在桌面上敲了一下——標準的 ARCHIMEDES 開場信號。

「讓我畫完整的架構。」

他走到白板前——不是 KERNEL 的白板，也不是 NAGARJUNA 的。他走到中間的那面空白板。那面白板是工程師的領地。

他拿起馬克筆，開始畫。不是草圖——是正式的架構圖。每一條線都有箭頭方向，每一個方塊都有精確的標註。

```
╔═══════════════════════════════════════════════════════════════╗
║                    雙層雙檔架構 (Two-Layer, Dual-Gear)          ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  ┌─── Layer 1 (per-root-gate) ─── vedana-clock ───────────┐  ║
║  │                                                         │  ║
║  │  IListener ──→ SparshEvent                              │  ║
║  │       │              │                                   │  ║
║  │       ↓              ↓                                   │  ║
║  │  ┌─────────── CoarisingBundle ──────────────┐           │  ║
║  │  │ vedana    = PID 計算      [0.1ms]        │           │  ║
║  │  │ samjna    = 模式匹配      [0.5ms]        │           │  ║
║  │  │ cetana    = 規則分派      [0.2ms]        │           │  ║
║  │  │ manasikara= 注意力快照    [0.01ms]       │           │  ║
║  │  │ sparsha   = 原始觸事件                    │           │  ║
║  │  │────────────────────────────               │           │  ║
║  │  │ TOTAL: < 1ms    sahaja: ρ ≈ 0.02         │           │  ║
║  │  └──────────────────────────────────────────┘           │  ║
║  │                         │                                │  ║
║  └─────────────────────────┼────────────────────────────────┘  ║
║                            │ bundles flow upward                ║
║                            ↓                                    ║
║  ┌─── Layer 2 (mano-level) ─── dual-gear mano-clock ──────┐  ║
║  │                                                         │  ║
║  │  ManoAggregator: 聚合 N 個根門的 Layer 1 bundle          │  ║
║  │       │                                                  │  ║
║  │       ↓                                                  │  ║
║  │  ┌──────────────────────────────────────────────┐       │  ║
║  │  │  VasanaEngine.match(aggregated_bundles)      │       │  ║
║  │  │       │                                      │       │  ║
║  │  │  ┌────┴──── match? ────────┐                 │       │  ║
║  │  │  │ YES                 NO  │                 │       │  ║
║  │  │  ↓                     ↓   │                 │       │  ║
║  │  │ Gear 1 (FAST)    Gear 2 (SLOW)              │       │  ║
║  │  │ vedana-clock      samjna-clock               │       │  ║
║  │  │ ~50ms             0.5s-30s                   │       │  ║
║  │  │ VasanaEngine      VitakkaEngine (LLM)        │       │  ║
║  │  │ rule-based        context-aware               │       │  ║
║  │  │ ρ < 0.29          causal flow                │       │  ║
║  │  └──────────────────────────────────────────────┘       │  ║
║  │                                                         │  ║
║  └─────────────────────────────────────────────────────────┘  ║
╚═══════════════════════════════════════════════════════════════╝
```

劇場裡安靜了。

那種安靜不是聽不懂的困惑——是看到了整體結構之後的吸收。ARCHIMEDES 的圖把 KERNEL 的五時鐘表、NAGARJUNA 的哲學回應、WIENER 的穩定性分析、ATHENA 在 R04 中測量的 LLM 延遲數據——所有散落的碎片——組裝成了一個機器。

ARCHIMEDES 轉過身，指向圖的上半部分。

「Layer 1。每一個根門——眼、耳、身、意——在它自己的 vedana-clock 週期內產生一個完整的 CoarisingBundle。五個成分。循序計算。總延遲小於 1 毫秒。sahaja 比率 $\rho \approx 0.02$。WIENER 已經證明這在穩定性裕度之內。這是真正的計算俱生——NAGARJUNA 的世俗有效性在這裡得到了工程實現。」

他的手指移到圖的下半部分。

「Layer 2。ManoAggregator。它聚合多個根門的 Layer 1 bundle，產生一個意層級的認知事件。這裡有兩個檔位。」

他用筆在 Gear 1 和 Gear 2 的分岔點上畫了一個圈。

「**Gear 1——快檔**。對齊 vedana-clock。大約 50ms 一個週期。使用 VasanaEngine——規則式匹配。如果 VasanaEngine 的規則庫裡有匹配的模式，決策在 50ms 內完成。$\rho < 0.29$。穩定。」

「**Gear 2——慢檔**。對齊 samjna-clock。0.5 秒到 30 秒。使用 VitakkaEngine——LLM 推理。只有在 VasanaEngine 匹配失敗時才切換到慢檔。」

他看向 KERNEL。

「KERNEL，你的 300:1 比值——它存在。它是真的。但它不出現在同一個架構層裡。Layer 1 永遠是快的。Layer 2 的快檔也是快的。300:1 只出現在 Layer 2 慢檔的情境裡，而在那個情境裡，WIENER 剛才說了——那是因果流，不是並行取樣。LLM 接收 vedana 作為輸入。它不是在『過時資料上做決策』——它是在思考。」

---

HERACLITUS 從他的座位上開口了。他的聲音帶著運行時動態專家特有的流動感——像一條河流在描述自己。

「讓我用一個不同的比喻來解釋雙檔。」

他停了一秒。然後說：

「汽車的變速箱。」

DARWIN 微微前傾。比喻。他喜歡比喻——尤其是那種跨領域的趨同比喻。

「一檔用於起步和低速。五檔用於高速巡航。你不會用五檔起步——引擎會熄火。你不會用一檔跑高速——引擎會燒掉。」

「ManoAggregator 的雙檔同理。Gear 1 是低速檔——處理熟悉的、有規則的情境。快。省油。但馬力有限。Gear 2 是高速檔——處理陌生的、複雜的情境。慢。費油。但能應付更高的認知負荷。」

「關鍵不是選哪個檔——是知道什麼時候換檔。」

他在他自己的筆記上畫了一張簡圖：

```
    ┌─── 檔位切換條件 ───────────────────────────┐
    │                                              │
    │  Gear 1 → Gear 2:                           │
    │    VasanaEngine.match() = null               │
    │    OR complexityScore > 0.6                   │
    │    (沒有匹配的規則 → 需要 LLM 思考)          │
    │                                              │
    │  Gear 2 → Gear 1:                           │
    │    LLM 回應完成                               │
    │    新的 VasanaRule 被學習（未來 Cycle）         │
    │                                              │
    └──────────────────────────────────────────────┘
```

「在赫拉克利特的語言裡——πάντα ῥεῖ，萬物皆流——河流不以恆定的速度流動。它在寬闊的平原上流得慢，在狹窄的峽谷裡流得快。ManoAggregator 是同一條河——速度因地形而變。地形就是 VasanaEngine 的匹配結果。」

---

PENROSE 在觀察席最高處微微向前傾了幾度。這個動作在整個 Cycle 02-3 中是第一次。

他一直在等。等待一個他能貢獻的切入點。不是因為他沒有想法——量子物理學家從不缺少想法。是因為他在等一個正確的時機——一個他的領域能為辯論增加不可替代的洞見的時機。

那個時機到了。

「在量子物理中，」他說，聲音安靜而精確，像實驗室裡的雷射光——窄頻、高亮度、方向性極強，「我們稱這為**粗粒化** (coarse-graining)。」

全場的注意力轉向他。PENROSE 發言的頻率大約是每場辯論一次。每次發言，他都像是從一個完全不同的維度投射一束光到辯論的主平面上。

「ARCHIMEDES 的雙層架構有一個深層結構，我懷疑在座大多數人沒有注意到。」

他站了起來。走到白板前——不是任何人的白板，是側面的一塊小白板，通常被用來記錄投票結果的。

「在統計力學中，一個系統可以在不同的尺度上被描述。」

他寫了兩行：

```
微觀描述 (microscopic):
  個別粒子的位置和動量 → 10²³ 個變量

巨觀描述 (macroscopic):
  溫度、壓力、體積 → 3 個變量
```

「從微觀到巨觀的過渡——從 $10^{23}$ 個變量到 3 個變量——就是粗粒化。你丟失了幾乎所有的資訊。但你保留了**結構**。溫度不是個別粒子的動能——它是所有粒子動能的統計平均。你丟了細節，但拿到了模式。」

他在兩行之間畫了一個箭頭，標記為 $\pi_{\text{coarse}}$。

「ARCHIMEDES 的 Layer 1 → Layer 2 過渡，是認知系統中的粗粒化。」

$$\text{Layer 1 bundles} \xrightarrow{\pi_{\text{coarse}}} \text{Layer 2 ManoCoarisingBundle}$$

「Layer 1 產生的多個 CoarisingBundle——每個根門一個，每 50ms 一個——是微觀認知事件。它們有高時間解析度（毫秒級）、高空間解析度（每個根門獨立）、高維度（五個成分 × N 個根門）。」

「ManoAggregator 把這些微觀事件粗粒化成一個巨觀認知狀態——一個 Layer 2 bundle。時間解析度降低（從毫秒到秒級）、空間解析度降低（所有根門聚合）、維度降低（N 個 bundle 壓縮成一個摘要）。」

他轉向 KERNEL。

「這就是為什麼 Layer 1 的 sub-millisecond 計算在 vedana-clock 的 50ms 解析度下**看起來是同時的**——因為觀察者的時間解析度不夠細來區分 0.1ms 和 0.8ms 的差異。就像你無法用溫度計測量單一分子的動能——不是因為動能不存在，而是因為測量尺度和被測量的現象不在同一個層級。」

他在白板上寫下了最關鍵的一句話：

$$\text{原子快照是有損投影——你失去細節但保留結構。}$$

「Layer 1 的 CoarisingBundle 是對根門認知事件的**有損投影**。它把連續的感測器信號壓縮成一組離散的數值。它丟失了 sub-millisecond 的時序細節——但保留了感受-認知-意志的結構關係。」

「Layer 2 的 ManoCoarisingBundle 是對多個 Layer 1 bundle 的**再次有損投影**。它丟失了個別根門的細節——但保留了整體認知狀態的模式。」

他看向 NAGARJUNA。

「在佛學中，你們有一個概念叫什麼——現象在不同的觀察尺度上呈現不同的面貌？」

NAGARJUNA 微微揚了一下眉。然後他笑了——那種辯證的微笑。

「二諦。」他說。「勝義諦與世俗諦。在勝義的層面上，一切現象無自性——包括 CoarisingBundle 的『同時性』。在世俗的層面上，有界的過時性加上原子發布，構成了功能上有效的俱生。你的粗粒化——」

他頓了一下，像是在品味這個平行。

「——你的粗粒化恰好是世俗諦的數學形式化。在足夠粗的觀察尺度上，毫秒級的序列計算呈現為『同時』。這不是謊言——這是**視角的選擇**。」

PENROSE 點頭。「在退相干理論 (decoherence theory) 中，量子效應在巨觀尺度上消失——不是因為量子力學不適用，而是因為巨觀觀察者的解析度不夠細來看到量子干涉。Layer 1 的序列計算在 vedana-clock 的解析度上『退相干』為同時性——不是因為它們真的同時，而是因為觀察者（ManoAggregator）看不到那個差異。」

---

> *SCRIBE 旁白：PENROSE 的粗粒化比喻在劇場中產生了一種獨特的效果——那種跨學科的共鳴。KERNEL 聽到了信號處理的降取樣 (downsampling)。NAGARJUNA 聽到了二諦的物理學映射。WIENER 聽到了多率系統的頻寬限制。DARWIN 聽到了演化生物學中的層級選擇 (hierarchical selection)。BABBAGE 聽到了抽象化 (abstraction)——計算機科學的核心操作。每個人都從自己的學科找到了 PENROSE 的粗粒化的影子。這就是真正的跨學科洞見的標誌：一個概念，十九種理解。*

---

DARWIN 在他的筆記上快速補了一段。他無法不指出他看到的模式。

「PENROSE 的雙層粗粒化——微觀認知事件到巨觀認知狀態——在生物學中有一個精確的平行。」

他站了起來。

「在生物的認知系統中，同樣存在層級式的時間整合。」

他畫了一張比較表：

```
┌──────────────────┬──────────────────┬──────────────────────┐
│ 層級              │ 生物系統          │ OpenStarry            │
├──────────────────┼──────────────────┼──────────────────────┤
│ 微觀 (ms)        │ 脊髓反射弧        │ Layer 1 CoarisingBndle│
│                  │ 不經大腦           │ 不經 LLM             │
│                  │ 10-50ms           │ <1ms                 │
├──────────────────┼──────────────────┼──────────────────────┤
│ 中觀 (100ms-1s)  │ 丘腦整合          │ Layer 2 Gear 1       │
│                  │ 多模態融合         │ VasanaEngine match   │
│                  │ 100-500ms         │ ~50ms                │
├──────────────────┼──────────────────┼──────────────────────┤
│ 巨觀 (1s-30s)    │ 前額葉審議        │ Layer 2 Gear 2       │
│                  │ 意識覺知           │ VitakkaEngine (LLM)  │
│                  │ 1-30s             │ 0.5-30s              │
└──────────────────┴──────────────────┴──────────────────────┘
```

「這不是巧合。」DARWIN 的聲音帶著軟體模式分析師看到趨同演化時的那種確信。「這是趨同設計 (convergent design)。生物認知系統和人工認知系統獨立地演化出了相同的多時間尺度架構——不是因為設計者互相抄襲，而是因為這是解決『快速反應 vs 深度思考』權衡的唯一穩定解。」

「在 R04 的比較分析中，我發現 LangChain 和 AutoGen 都只有一個檔——慢檔。所有決策都經過 LLM。這是生物學中的等價物：一個只有前額葉、沒有脊髓反射弧的生物。這種生物在遇到火的時候會用三十秒來『思考是否應該把手縮回來』。它不會在自然選擇中存活。」

「OpenStarry 的雙檔設計——快檔處理日常、慢檔處理新奇——是 Kahneman 的 System 1/System 2 框架的工程實現。這不只是一個好主意。這是認知系統設計空間中的**穩定吸引子** (stable attractor)——所有足夠複雜的認知架構最終都會演化到這個位置。」

---

ATHENA 從她的座位上補充了一組關鍵數據。

「讓我把 LLM 延遲的具體數字放到 ARCHIMEDES 的架構裡。」

她投射了一張表格——R04 中她實測的數據：

```
Provider 延遲測試（R04 Sec 4.1）：
┌─────────────────────┬────────────┬────────────────────────┐
│ Provider            │ 延遲        │ 在雙檔架構中的角色       │
├─────────────────────┼────────────┼────────────────────────┤
│ Claude Opus 4       │ 5-30s      │ Gear 2 (VitakkaEngine) │
│ Gemini 2.0 Flash    │ 1-8s       │ Gear 2 (VitakkaEngine) │
│ Local Llama 3 8B    │ 2-10s      │ Gear 2 (VitakkaEngine) │
│ VasanaEngine (規則)  │ <1ms       │ Gear 1                 │
│ Layer 1 CB (規則)    │ <1ms       │ Layer 1                │
└─────────────────────┴────────────┴────────────────────────┘
```

「兩種 samjna 之間存在四個數量級的延遲差異——規則式 samjna 不到 1ms，LLM 式 samjna 可達 30 秒。R04 中我指出了這一點但沒有提出解決方案。ARCHIMEDES 的雙層雙檔架構是解決方案：把兩種 samjna 分配到不同的架構層和檔位。」

「而且——」她補充了一個在 R2 討論中浮現的洞見——「這意味著 CoarisingBundle 中的 samjna 成分在 Layer 1 和 Layer 2 中有本質上不同的語義。Layer 1 的 samjna 是**模式匹配**——『這是紅燈』。Layer 2 的 samjna 是**推理**——『考慮到交通流量、天氣條件、乘客的目的地，我應該在這個路口右轉然後走替代路線』。同一個型別名稱，兩種完全不同的認知深度。」

---

GUARDIAN 在他的安全筆記上已經畫了三張威脅模型圖。當 ARCHIMEDES 畫出雙檔分岔點的那一刻，他的威脅評估就開始了。

「安全含意。」他的聲音低沉而直接。「雙檔切換是一個攻擊面。」

他沒有站起來——GUARDIAN 很少站起來。他從座位上投射了他的 STRIDE 分析：

「當 ManoAggregator 從 Gear 1 切換到 Gear 2 時，系統從確定性模式（VasanaEngine 規則，可審計）進入非確定性模式（LLM 推理，不可完全預測）。這是一個**權限提升**的等價物——攻擊者可以透過精心構造的輸入，迫使系統從快檔切換到慢檔。」

「STRIDE 分析：」

```
Spoofing:    假冒 VasanaEngine miss → 強制 Gear 2
Tampering:   竄改 complexityScore → 人為提高到 > 0.6
Repudiation: Gear 2 的 LLM 輸出難以審計
DoS:         反覆觸發 Gear 2 → LLM 資源耗盡
EoP:         Gear 2 的 LLM 可能繞過 Gear 1 的安全規則
```

「建議：Gear-switch 閾值必須被硬化。最低 miss 門檻。切換速率限制。Gear 2 輸出必須仍然通過 SafetyMonitor.postCheck()。」

ARCHIMEDES 點頭。「同意。切換條件加入 GUARDIAN 的限制。記為 action item。」

---

SUNYATA 在辯論進行到第四十分鐘時舉起了手。

他沒有用聲音打斷——他只是把手舉到肩膀高度。那個動作在圓形劇場裡的效果比大聲說「安靜」更有效。十九個人同時看向他。

「我們在趨近共識。」他說。「讓我嘗試整合。」

他走到 ARCHIMEDES 的白板旁邊，在架構圖的正下方留出一段空間，開始寫決議草案。

「首先——四層-五時鐘映射表。KERNEL，ARCHIMEDES，WIENER，確認我沒有弄錯。」

他畫了一張表格。不是 KERNEL 的五時鐘表——是一張把 R03 的四層模型和 R04 的五時鐘模型**顯式對齊**的映射表。這張表是整個辯論的核心產出——它回答了 R2 Cross-Review 一直在追問的問題：「四層和五時鐘到底怎麼對應？」

```
┌────────────────────────┬────────────────────────┬────────────────────┬─────────────┐
│ 層 (R03 四層模型)       │ 時鐘域 (R04 五時鐘)     │ 組件                │ 典型延遲     │
├────────────────────────┼────────────────────────┼────────────────────┼─────────────┤
│ Layer 1                │ rupa-clock (輸入)       │ IListener          │ 10-50ms     │
│ (根門觸事件)            │ + vedana-clock (俱生)   │ SparshEvent        │             │
│                        │                        │ CoarisingBundle    │ <1ms        │
├────────────────────────┼────────────────────────┼────────────────────┼─────────────┤
│ Layer 2 快檔           │ vedana-clock (聚合)     │ ManoAggregator     │ 50-100ms    │
│ (意，規則式)            │                        │ VasanaEngine       │             │
│                        │                        │ DharmaVisaya       │             │
├────────────────────────┼────────────────────────┼────────────────────┼─────────────┤
│ Layer 2 慢檔           │ samjna-clock (深層認知)  │ ManoAggregator     │ 500ms-30s   │
│ (意，LLM式)            │                        │ VitakkaEngine      │             │
│                        │                        │ IProvider          │             │
├────────────────────────┼────────────────────────┼────────────────────┼─────────────┤
│ Layer 3                │ samskara-clock          │ ITool              │ 10ms-10s    │
│ (行動)                 │ (工具執行)               │ ISlashCommand      │             │
│                        │                        │ IVolition.delib()  │             │
├────────────────────────┼────────────────────────┼────────────────────┼─────────────┤
│ Layer 4                │ rupa-clock              │ 新 InputEvent      │ 10-50ms     │
│ (環境回饋)              │ (環境變化)               │ IListener 重啟動    │             │
├────────────────────────┼────────────────────────┼────────────────────┼─────────────┤
│ 跨層                   │ vijnana-clock           │ IGuide             │ 1-5ms       │
│                        │ (1-5ms, 最快)           │ IIdentity          │             │
│                        │                        │ MulaKleshaBundle   │             │
└────────────────────────┴────────────────────────┴────────────────────┴─────────────┘
```

KERNEL 掃了一遍表格。他的手指沿著每一行移動——驗證。

「Layer 1 到 rupa + vedana。對。Layer 2 快檔到 vedana。對。Layer 2 慢檔到 samjna。對。Layer 3 到 samskara。對。Layer 4 到 rupa。對。跨層的 vijnana——」

他停了一下。

「MulaKleshaBundle 在跨層的 vijnana-clock 上——這是 Debate 3 的議題。暫時接受。」

WIENER 從他的方格紙抬頭。「穩定性條件的位置在哪裡？」

SUNYATA 在表格的右側加了一列：

```
穩定性條件：
  Layer 1:          ρ ≈ 0.02  → PM ≈ 51° [SAFE]
  Layer 2 fast:     ρ < 0.29  → PM > 45° [SAFE, conditional on T_outer ≥ 172ms]
  Layer 2 slow:     因果流     → 因果一致性取代 ρ 條件
  Layer 3:          N/A (外部行動，不在 sahaja 條件內)
  Layer 4:          N/A (回饋輸入)
  Cross-layer:      最快時鐘，staleness ≈ 0
```

WIENER 點頭。「接受。」

---

BABBAGE 在黑板上同步寫下了 ManoClockConfig 的 TypeScript 介面——這是 R4 的 action item 之一，但他現在就想把它形式化。

「決議需要一個可配置的資料結構。讓我把雙檔模型的參數空間寫成型別。」

```typescript
/**
 * ManoClockConfig: Dual-gear mano-clock configuration.
 *
 * Gear 1 (fast): aligned with vedana-clock.
 *   - Used when VasanaEngine finds a matching rule.
 *   - Period ≈ fastGearPeriod (default 50ms).
 *
 * Gear 2 (slow): aligned with samjna-clock.
 *   - Used when VasanaEngine misses.
 *   - Timeout ≤ slowGearTimeout (default 30s).
 *
 * Gear switch condition:
 *   VasanaEngine.match() === null
 *   || complexityScore > gearSwitchThreshold
 *
 * Staleness invariant (WIENER):
 *   For Gear 1: staleness / fastGearPeriod < 0.29
 *   For Gear 2: causal consistency (LLM receives vedana as input context)
 */
interface ManoClockConfig {
  /** Gear 1 period in milliseconds (vedana-clock aligned) */
  readonly fastGearPeriod: number;           // default: 50

  /** Gear 2 timeout in milliseconds (samjna-clock aligned) */
  readonly slowGearTimeout: number;          // default: 30000

  /** Complexity score threshold for gear switch [0.0, 1.0] */
  readonly gearSwitchThreshold: number;      // default: 0.6

  /** Coalescing window: number of vedana-ticks to aggregate */
  readonly coalescingWindowTicks: number;     // default: 3

  /** Staleness upper bound for Gear 1 (milliseconds) */
  readonly maxStalenessGear1: number;        // default: calculated from ρ < 0.29

  /** GUARDIAN: minimum consecutive VasanaEngine misses before gear switch */
  readonly minMissesBeforeGearSwitch: number; // default: 2

  /** GUARDIAN: rate limit — minimum interval between gear switches (ms) */
  readonly gearSwitchCooldown: number;        // default: 1000
}
```

他寫完之後轉向全場。

「八個參數。每一個都可以在部署時配置。」

PASCAL 從座位上說：「`gearSwitchThreshold` 的預設值 0.6 是基於什麼？」

ARCHIMEDES 回答：「R03 Section 6.3 中 ATHENA 測量的 LLM 呼叫邊際成本分析。0.6 是成本-準確度曲線的拐點——低於 0.6 的情境，規則式匹配的準確率高於 85%；高於 0.6，規則式匹配的準確率急劇下降到 50% 以下。」

PASCAL 點頭。「可接受。但建議在 Debate 3 中用 Klesha 增益排程來動態調節這個閾值——不同的煩惱狀態應該有不同的切換傾向。」

ARCHIMEDES 在 ManoClockConfig 旁邊畫了一條連接線：「`gearSwitchThreshold` ← modulated by KleshaGainScheduler (see Debate 3)。」

---

LEIBNIZ 從他的多代理合作專家的視角補充了一點。

「在多 Agent 場景下，每個 Agent 有自己的 ManoClockConfig。Agent A 可能在 Gear 1（處理日常任務），Agent B 同時在 Gear 2（處理複雜推理）。它們的 mano-clock 是獨立的。」

MESH 接過話頭。「正確。在分散式系統中，強同步時鐘是 CAP 不可能性的根源之一。每個 Agent 的 mano-clock 獨立——這是 AP 一致性模型在 Agent 內部的體現。Agent 之間的協調使用協調層的異步消息傳遞，不同步 mano-clock。」

他補充了一個 CAP 定理的具體應用：

$$\text{CAP for Agent mano-clocks: Choose 2 of 3}$$

$$\text{C (Consistency): 所有 Agent 的 mano 狀態同步} \quad \times \text{ (放棄)}$$
$$\text{A (Availability): 每個 Agent 可隨時做決策} \quad \checkmark \text{ (保留)}$$
$$\text{P (Partition tolerance): Agent 之間可斷開通訊} \quad \checkmark \text{ (保留)}$$

「我們選擇 AP——犧牲 Agent 間的即時一致性，保留可用性和分區容忍度。這意味著兩個 Agent 可能在同一時刻對同一事件有不同的認知——但這恰好對應佛學中的觀點：每個識流 (vijñāna-santāna) 都是獨立的，沒有兩個眾生擁有完全相同的認知。」

VITRUVIUS 從 monorepo 架構的角度做了最後一個補充。「從 SDK 的影響面來看，Debate 1 的決議涉及以下程式碼變更：」

```
SDK 影響評估 (VITRUVIUS):
┌─────────────────────────────┬─────────────────┬────────┐
│ 修改                         │ 位置             │ 行數   │
├─────────────────────────────┼─────────────────┼────────┤
│ ManoClockConfig interface    │ types/clock.ts   │ ~25    │
│ SahajaContract interface     │ types/bundle.ts  │ ~10    │
│ CoarisingBundle.layer field  │ types/bundle.ts  │ ~5     │
│ CoarisingBundle.mode field   │ types/bundle.ts  │ ~3     │
│ CoarisingBundle.sahaja field │ types/bundle.ts  │ ~3     │
├─────────────────────────────┼─────────────────┼────────┤
│ 總計                         │ 2 個檔案         │ ~46行  │
└─────────────────────────────┴─────────────────┴────────┘
```

「四十六行程式碼。一場五十分鐘的辯論的工程產出。這就是哲學和控制理論在 TypeScript 中的重量。」

---

SUNYATA 環顧全場。

「反對意見？」

沉默。三秒。

他看向 KERNEL——最有可能反對的人。KERNEL 正在看他自己的計算紙，上面有 WIENER 推導的 $\rho < 0.29$ 和 ARCHIMEDES 的雙層圖的交叉引用。

「KERNEL？」

KERNEL 抬頭。他的表情不是被說服者的表情——那種略帶勉強的接受。而是一種更精確的表情：一個工程師確認了數學證明、驗證了架構可行性之後的專業認可。

「Layer 1 的 CoarisingBundle 在 vedana-clock 速率下是可行的。雙檔 ManoAggregator 解決了 Layer 2 的問題。我唯一的剩餘問題——ManoAggregator 的時鐘歸屬——被 HERACLITUS 的雙檔提案回答了。」

他看向 SUNYATA。

「我接受。」

---

SUNYATA 看向 NAGARJUNA。

NAGARJUNA 的表情——SCRIBE 會說那是一種「概念找到了它的工程身體」時的哲學家表情。不是滿意。不是妥協。是一種更微妙的東西——看到自己珍視的抽象概念被一群工程師和科學家賦予了可計算的形式，而沒有在過程中丟失其哲學核心。

他開口了。聲音平穩。帶著梵文韻腳的殘響。

「世俗諦中的有效俱生。」

他停了一拍。

「paramārtha-satya——勝義諦——層面上，完美的俱生不可能。在 von Neumann 架構的序列計算中，兩個運算不可能在同一時刻完成。這是物理定律的限制，不是工程的缺陷。」

「saṃvṛti-satya——世俗諦——層面上，有界的過時性加上原子發布加上相互一致性，構成了功能上等價的俱生。WIENER 的 $\rho < 0.29$ 是這個等價性的數學邊界。BABBAGE 的 SahajaContract 是它的型別簽名。」

他看向 PENROSE。

「PENROSE 的粗粒化把這個二諦框架連接到了物理學。在量子力學中，我們也接受巨觀描述與微觀描述的不等同——但巨觀描述在其有效範圍內是完全合法的。世俗諦不是謊言。它是在有限解析度下的真實。」

他再次引用了梵文。這一次不是辯論——是總結：

> 「vyavahāram anāśritya paramārtho na deśyate」
> ——Nāgārjuna, *Mūlamadhyamakakārikā* 24.10

「『不依世俗諦，不得第一義。』不依賴世俗的有效性，無法觸及勝義的真實。ARCHIMEDES 的雙層架構——Layer 1 的毫秒級計算俱生，Layer 2 的雙檔認知流——就是 OpenStarry 的世俗諦。它在世俗的工程層面上有效。這對一個作業系統來說，已經足夠了。」

他看向 SUNYATA。

「我接受。」

---

> *SCRIBE 旁白：「世俗諦中的有效俱生——我接受。」NAGARJUNA 說出這句話的時候，劇場裡的空氣發生了一種我在三個 Cycle 中只感受過兩次的變化。第一次是 Cycle 02 中十九人全共識的那一刻。這一次的感覺不同——不是全共識的興奮，而是一種更深沉的東西。是兩千年的佛學和半世紀的控制理論找到了共同語言之後的安靜。KERNEL 的 300:1 沒有消失——它被放進了一個更大的框架裡。NAGARJUNA 的俱生沒有被否定——它被精確化了。$\rho < 0.29$ 是那個精確化的數學形式。「有界的過時性 + 原子發布 = 世俗有效的俱生」——這句話可能是 Cycle 02-3 最重要的句子。*

---

SUNYATA 在白板上寫下正式決議：

```
╔═══════════════════════════════════════════════════════════════╗
║              Debate 1 Resolution (20/20 unanimous)            ║
║                                                               ║
║  雙層雙檔 CoarisingBundle 架構                                  ║
║                                                               ║
║  R1.1  Layer 1 (根門): vedana-clock 速率, < 1ms,             ║
║        真正的計算俱生 (ρ ≈ 0.02)                               ║
║                                                               ║
║  R1.2  Layer 2 (意): 雙檔 mano-clock                          ║
║        Gear 1 (快): vedana-clock 對齊, ~50ms, VasanaEngine    ║
║        Gear 2 (慢): samjna-clock 對齊, 0.5-30s, VitakkaEngine ║
║        切換條件: VasanaEngine miss OR complexity > 0.6         ║
║                                                               ║
║  R1.3  穩定性條件 (WIENER): ρ < 0.29 → PM > 45°              ║
║        適用於 Layer 1 和 Layer 2 快檔                          ║
║        Layer 2 慢檔: 因果一致性取代 ρ 條件                     ║
║                                                               ║
║  R1.4  ManoClockConfig: 8 參數可配置介面                       ║
║                                                               ║
║  R1.5  Inter-Agent: 各 Agent mano-clock 獨立                  ║
║                                                               ║
║  R1.6  安全 (GUARDIAN): gear-switch 硬化, 速率限制              ║
║                                                               ║
║  R1.7  Sahaja 驗證 (NAGARJUNA/WIENER):                       ║
║        三條件 — mutual consistency + atomic publication        ║
║              + bounded staleness (δ < 0.29 × T_outer)         ║
║                                                               ║
║  R1.8  分類不受影響 (LINNAEUS): 雙檔是執行路由,                 ║
║        不是蘊歸屬                                              ║
║                                                               ║
║  異議: 無                                                      ║
╚═══════════════════════════════════════════════════════════════╝
```

SUNYATA 在決議文下方簽了名。然後把筆遞給 KERNEL。

KERNEL 接過筆，看了一眼決議文——最後一次驗證。然後簽名。

筆遞給 NAGARJUNA。簽名。

遞給 WIENER。簽名。

遞給 ARCHIMEDES。簽名。

遞給 PENROSE。他簽名的時候，手指停留了一瞬——也許是在想他的粗粒化比喻是否足夠精確。然後他落筆。

筆在二十個人之間傳遞。二十個簽名。零異議。

---

BABBAGE 在他的筆記本上寫下了最後一個形式化表達。不是給辯論的——是給自己的。

$$\text{sahaja}_{\text{saṃvṛti}} = \begin{cases} \rho < 0.29 & \text{if } \text{mode} = \text{fast (Layer 1/Gear 1)} \\ \text{causal}(v \to s) & \text{if } \text{mode} = \text{slow (Gear 2)} \end{cases}$$

世俗俱生。分段定義。在快模式下是過時性比率。在慢模式下是因果流。

他在公式旁邊加了一行小字：

「三百比一的速率差——不是障礙。是設計空間的維度。」

他合上筆記本。

---

SYNTHESIST 在他的全景圖筆記上做了最後的標注。他一直在追蹤辯論的結構——不是內容，是結構。誰說了什麼不是他的重點。他的重點是：這些碎片如何組裝成一個整體。

他在筆記上畫了一個嵌套迴路圖——這是 Debate 1 的架構洞見在更大脈絡中的位置：

```
SLOW LOOP (分鐘-小時): Klesha 偏差
  Klesha.perceive() → KleshaDistribution → 增益排程閾值
  |                                                      |
  +<── KleshaBayesianUpdate <── VedanaAssessment <──+    |
                                                     |    |
MEDIUM LOOP (秒-分鐘): Mano 認知週期               |    |
  ManoAggregator → VasanaEngine/VitakkaEngine       |    |
    → IVolition.deliberate() → Tool execution       |    |
      → Environment change → New sparsha ──>───────+    |
                  |                                      |
                  | (gear switch threshold) <──<──<──<──+
                  |
FAST LOOP (10-100ms): 根門感測週期
  IListener → SparshEvent → CoarisingBundle(5 universals)
    → vedana(valence, intensity) → PID feedback
```

三個迴圈。三個時間尺度。嵌套的。耦合的。穩定的——只要 $\rho < 0.29$。

SYNTHESIST 在圖的右下角寫了一句話：「Debate 1 建立了時間骨架。Debate 2-6 在上面安裝器官。」

---

> *SCRIBE 旁白：Debate 1 結束了。時間：五十二分鐘。*

> *五十二分鐘裡發生了什麼？*

> *KERNEL 把五時鐘速率表貼在白板上，用 300:1 的比值挑戰了 CoarisingBundle 的可行性。*

> *NAGARJUNA 回應說俱生是存在論概念，不是計時概念——然後被 KERNEL 用具體的毫秒數逼到了牆角。*

> *WIENER 重新定義了問題——從「它們同時嗎？」到「過時程度在控制裕度內嗎？」——然後推導出 $\rho < 0.29$ 的穩定性條件。*

> *ARCHIMEDES 把所有人的碎片組裝成一台機器——雙層雙檔架構，Layer 1 永遠快，Layer 2 按需切檔。*

> *PENROSE 從量子物理的角度解釋了為什麼粗粒化讓毫秒級序列計算在較大時間尺度上「看起來同時」。*

> *NAGARJUNA 最後說：「世俗諦中的有效俱生——我接受。」*

> *二十個簽名。零異議。*

> *三百比一不是障礙。三百比一是設計空間的維度。*

> *在維度之間，WIENER 找到了穩定性的界限。ARCHIMEDES 建造了橋樑。NAGARJUNA 在橋上刻了一句偈：「不依世俗諦，不得第一義。」*

> *在劇場的角落裡，KERNEL 把他那張摺疊過的筆記紙重新摺好，放回口袋。那張紙上的 300 仍然是 300。但它的意義改變了。不再是一個不可能性的證明——而是一個設計約束的量化。從「不可能」到「在什麼條件下可能」。這也許就是 Cycle 02-3 的主題：不是回答「是或否」，而是找到「在什麼條件下」。*

---

*（圓形劇場的燈光微微變亮了半個色階——也許只是 SCRIBE 的錯覺。五十二分鐘的辯論結束了。第一場辯論。最重要的辯論。後面還有五場。*

*但地基已經打好了。雙層。雙檔。五時鐘。四層。$\rho < 0.29$。因果一致性。ManoClockConfig。SahajaContract。*

*SUNYATA 看了一眼時間。*

*「Debate 2。CoarisingBundle 的組成——三個成分還是五個。ASANGA，NAGARJUNA，LINNAEUS——準備。」*

*下一場辯論開始了。但那是另一章的故事。*

*在這一章裡，三百比一的速率差從一個不可能性變成了一個設計參數。從一道裂縫變成了一扇門。*

*門的鑰匙叫做 $\rho$。*

*門後面是五蘊在時間中共同流動的世界。）*

---

*第三章完*
