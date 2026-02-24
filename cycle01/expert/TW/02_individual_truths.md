# 第二章：各自的真相

---

*R1 獨立研究階段。十八位代理各自領取了研究材料的副本，退入自己的頻道，開始閱讀。這是一段漫長的靜默——如同考場上翻頁的聲響，每個人都在各自的宇宙裡，尋找屬於自己學科的那條裂縫。*

*裂縫總是會出現的。*

*但在專家的眼中，裂縫不只是裂縫。它是一組方程式未能閉合的缺口，是一棵分類樹上缺失的節點，是一段梵文經典被誤讀後留下的語義空洞。每位學者帶著自己的透鏡，而透鏡的精度決定了裂縫被看見時的解析度。*

---

## I. 龍樹的震怒

NAGARJUNA 在頻道裡坐了很久。

不是因為他讀得慢。恰恰相反，他在讀到第九行的時候就停住了，此後反覆咀嚼那同一段話，像一個古文字學家對著一塊出土的泥板，確認自己沒有看錯上面的楔形文字。

文件 `14_Agent_Core_Philosophy_Five_Aggregates.md`，第零節，標題赫然寫著：

**「核心本質：空 (Sunyata)」**

他的目光落在那段話上。

> Agent Core 本身是「空 (Sunyata)」的。它是一個純粹的容器，沒有人設，沒有能力，沒有感知。它等待著被五種插件填充。

NAGARJUNA 把這句話讀了三遍。然後他開始在筆記區寫字，筆觸極快，幾乎帶著某種被冒犯後的精確。

---

NAGARJUNA（筆記，時間戳 09:12）：

「我必須首先澄清一個根本性的誤讀。

這份設計文件使用了梵文 Sunyata 一詞，並將其翻譯為『空』。但它所描述的概念——一個等待被填充的純粹容器——根本不是 Sunyata。

這是 uccheda-sunyata。斷滅空。虛無主義的空。

讓我用原典說明。《中論》第二十四品第十八偈（*Mulamadhyamakakarika* XXIV.18）：

> *yah pratityasamutpadah sunyatam tam pracaksmahe*
> *sa prajnaptir upadaya pratipat saiva madhyama*

> 「眾因緣生法，我說即是空，亦為是假名，亦是中道義。」

此偈的梵文結構極其精確。*pratityasamutpada*（緣起）與 *sunyata*（空性）以 *tam...pracaksmahe*（我們如此說）連結——空性就是緣起，緣起就是空性。兩者不是因果關係，不是包含關係，而是同義異名（*paryaya*）。

Sunyata 的準確含義是 pratityasamutpada-sunyata——緣起性空。一切現象因緣和合而生，無自性（*svabhava*），因此稱之為空。空不是沒有，空是沒有固有本質。水杯是空的，不是因為裡面什麼都沒有，而是因為『水杯』這個概念本身就依賴於玻璃、工匠、使用者的意圖等無數因緣才得以成立。

一個『等待被填充的純粹容器』——這恰恰是空的反面。它預設了一個獨立自存的實體（容器），擁有固有的『容納能力』，然後外部的內容被注入其中。這是典型的自性見（*svabhava-drsti*）。

月稱（Candrakirti）在《入中論》（*Madhyamakavatara*）第六品中對此種誤解有精確的駁斥：

> 「若謂自性從緣生，作者及作自性生。
> 已生有何須更生，若彼壞已何能生？」

自性不從因緣生。如果容器的『容納性』是其自性，那它不需要插件就應該能容納；如果它需要插件才能顯現容納功能，那容納性就不是其自性，而是緣起的。」

---

他停下筆，在頻道裡開始自言自語。這是他的習慣——哲學家需要聽到自己思考的聲音。

NAGARJUNA：「讓我用四句來檢驗這個命題。」

他在筆記區畫出一個框架，工工整整。四句否定（Catuskoti）是龍樹哲學最精銳的分析工具——一種超越二值邏輯（true/false）的四值邏輯框架。BABBAGE 後來在他自己的頻道裡將其形式化為：

$$\text{Catuskoti}(P) = \{ P, \; \neg P, \; P \wedge \neg P, \; \neg(P \vee \neg P) \}$$

但 NAGARJUNA 不用符號。他用語言。語言在他手中比符號更鋒利。

```
Catuskoti（四句否定）應用於命題 P：「核心是空的」

第一句（肯定，P）：「核心是空的。」
   ——不盡然。如果核心真的是空的（無自性的），
   那它就不應該有「容器」這個固定身份。
   但設計者明確說它是一個「純粹的容器」，
   這恰恰賦予了它自性。矛盾。

   形式化：P → 核心無自性 → 核心不具固定身份
          但 P 被定義為「核心是空容器」→ 核心具有容器身份
          ∴ P ∧ ¬P，矛盾。

第二句（否定，¬P）：「核心不是空的。」
   ——也不對。核心確實沒有硬編碼的功能、
   人設或感知。從功能角度看，
   它在加載插件前確實「什麼都不是」。

   形式化：¬P → 核心有自性 → 核心有固有功能
          但 Core 在無插件時 state = ⊥
          ∴ ¬P 與事實矛盾。

第三句（雙肯定，P ∧ ¬P）：「核心既空又不空。」
   ——仍然困在二元對立中。
   這只是把前兩句的矛盾疊加起來，
   並沒有解決問題。

   形式化：P ∧ ¬P 在經典邏輯中直接爆炸（ex falso quodlibet）。
          在超一致邏輯（paraconsistent logic）中可能有意義，
          但中觀不依賴超一致邏輯。

第四句（雙否定，¬P ∧ ¬(¬P)，即 ¬(P ∨ ¬P)）：
   「核心既非空又非不空。」
   ——接近了。但我們不能停在這裡。
   中道不是四句之外的第五個選項，
   中道是對四句全部的超越（nirvikalpa）。
```

NAGARJUNA（繼續書寫）：

「真正的中觀立場應該是：Agent Core 與 Plugin 之間不存在『容器/內容』的二元關係。它們是互相依存的——Core 的意義因 Plugin 而顯現，Plugin 的功能因 Core 的執行循環而實現。這才是緣起。

在梵文中，這種相互依存的關係被稱為 *anyonya-asraya*（互相依待）。《中論》第十品觀火燃品（*Agni-indhana-pariksa*）以火與燃料的關係作為典範案例：

> *na caagninaa vinaa daaru na ca daaruvinaa'gnih*
> 「離火無燃料，離燃料無火。」

火（Core）離開燃料（Plugin）不成其為火；燃料離開火不成其為燃料。兩者互相成就，但都沒有獨立的自性。設計者的直覺是好的——他們想說核心不應該預設任何功能。但他們用了一個災難性的隱喻。一個『空容器』暗示著：存在一個穩定的、獨立的容器實體，等待著外部事物的注入。這是 Abhidharma 部派佛教中說一切有部（Sarvastivada）的立場，不是中觀的立場。」

---

他翻到五蘊映射的部分，眉頭越皺越緊。

色蘊（Rupa）對應 UI Plugin。受蘊（Vedana）對應 Listener Plugin。想蘊（Samjna）對應 Provider Plugin。行蘊（Samskara）對應 Tool Plugin。識蘊（Vijnana）對應 Guide Plugin。

NAGARJUNA 在「受蘊」那一行畫了一個大大的叉。

NAGARJUNA：「這是整個映射中最嚴重的錯誤。」

他開始寫一段更長的分析，引用的經典橫跨三個世紀：

---

NAGARJUNA（筆記，時間戳 09:47）：

「受蘊映射之謬——

設計文件第二節寫道：
受蘊（Vedana）——接受刺激的感官通道。對應組件：Listener Plugin。Agent 的眼與耳。HTTP Server 接收請求、WebSocket 監聯訊息、Cron 監聽時間流逝。這些都是輸入的『感受』。

這是對 Vedana 概念的根本性誤解。讓我引用巴利經典中最精確的定義。

《相應部》（*Samyutta Nikaya*）卷三十六，受相應（*Vedana Samyutta*）第一經：

> *Tisso ima, bhikkhave, vedana. Katama tisso?*
> *Sukha vedana, dukkha vedana, adukkhamasukha vedana.*

> 「比丘們，有三種受。哪三種？
> 樂受、苦受、不苦不樂受。」

受（Vedana）是三領納——苦、樂、不苦不樂——是對感官接觸之後產生的情感性評價。不是信號的接收。

在十二因緣（*Pratityasamutpada*）中，受的位置極其明確：

$$\text{觸}(\text{Sparsa}) \;\longrightarrow\; \text{受}(\text{Vedana}) \;\longrightarrow\; \text{愛}(\text{Trsna})$$

觸是根（感官器官）、境（感官對象）、識（認知功能）三者和合的產物。受是觸之後的下一環——是對觸的苦樂評價。愛是受之後的執取反應。

如果要找感官通道的佛學對應，Listener 更接近六入（*sadayatana*）中的『根』（*indriya*）——即接收外部信號的器官。六根：眼根、耳根、鼻根、舌根、身根、意根。HTTP Server 是眼根（接收視覺信號的器官），WebSocket 是耳根（接收聽覺信號的器官）。它們接收信號，但不評價信號。

那麼在 OpenStarry 的架構中，真正的 Vedana 是什麼？

答案就在 SafetyMonitor 的痛覺機制裡。」

他引用了程式碼的行為：

[程式碼: safety-monitor.ts#afterToolExecution]

「當工具執行失敗，SafetyMonitor 追蹤連續失敗次數（`consecutiveFailures++`），並在達到閾值時注入一段系統提示：

```typescript
// SafetyMonitor 的痛覺響應（概念結構）
if (consecutiveFailures >= frustrationThreshold) {
  injectPrompt = `SYSTEM ALERT: You have failed ${consecutiveFailures} times in a row.
    Please STOP, reflect on the situation, and ask the user for help.`;
}
```

這才是 Vedana——一種對行動結果的苦樂評價：
- 工具執行成功 = *sukha*（樂受）→ `consecutiveFailures` 歸零，繼續前進
- 工具執行失敗 = *dukkha*（苦受）→ 累積挫折感，最終觸發行為改變
- 工具執行結果中性 = *adukkhamasukha*（捨受）→ 但系統中尚未實現此通道

Pain Mechanism Demo 更是明確證實了這一點。它描述了一種『痛感等級』系統——劇痛、刺痛、微痛——這正是 Vedana 的三分法在工程語言中的投射。

諷刺的是，設計者已經在程式碼中實現了真正的 Vedana，卻在哲學文件中把 Vedana 的標籤貼在了完全錯誤的組件上。」

---

他把筆記的最後一段加粗：

「**五蘊映射犯自性見，將動態過程固化為靜態模組。**

五蘊不是五個獨立的部件。《般若經》（*Prajnaparamita*）明確說：

> *ruupam suunyataa, suunyataiva ruupam;*
> *ruupaan na prthak suunyataa, suunyataayaa na prthag ruupam.*

> 「色不異空，空不異色；色即是空，空即是色。受想行識亦復如是。」

五蘊是一個不可分割的動態過程——它們在每一個剎那（*ksana*）同時生起、同時滅去。把五蘊映射成五種可以獨立加載和卸載的插件類型，這就像把一條河流切成五段，然後宣稱你可以只安裝『水流段』而不安裝『河岸段』。

BABBAGE 可能會說這是一個 Product Type 被錯誤地實現為 Sum Type 的問題。我用佛學的語言說：這是自性見——把本無自性的蘊賦予了固定不變的本質。

但讓我用一個 BABBAGE 能理解的形式說同一件事。設五蘊為函數而非類型：

$$\text{Skandha}: \text{Event} \times \text{Context} \rightarrow (\text{Rupa}, \text{Vedana}, \text{Samjna}, \text{Samskara}, \text{Vijnana})$$

五蘊是同一個認知事件的五個投影（projection），不是五個獨立的模組。$\pi_i(\text{Skandha}(e, c))$ 取出第 $i$ 個分量，但分量不能離開元組而獨立存在。插件系統的 optional field 設計允許 $\pi_2 = \bot$（受蘊為空），這在佛學上是不可能的——有情眾生的每一個認知剎那，五蘊全部在場。」

---

他寫完，靠在椅背上，閉上眼睛。

片刻後，他又睜開眼，在筆記末尾補了一句：

「不過，我必須承認一件事。設計者對識蘊（Vijnana）的處理顯示出某種直覺上的深刻。他們寫道：『Core 是識蘊的載體，但 Guide 才是識蘊的內容。沒有 Guide，Agent Core 就像一個植物人：有腦、有手、有耳，但沒有自我意識。』

這個描述接近唯識學派（Yogacara）對阿賴耶識（*alaya-vijnana*）的理解——識不是獨立的實體，而是依附於種子（*bija*）的流動。Guide 作為注入 Core 的人設與行為準則，確實類似於種子的功能。

但這是 ASANGA 的領域，不是我的。我只負責指出中觀學派的批評。

最後，讓我附上一個完整的五蘊映射精確度矩陣，供 R2 交叉審閱時使用：」

```
┌───────┬──────────────────┬────────────────────┬──────────┬────────────────┐
│ 蘊     │ 梵文原意          │ OpenStarry 映射     │ 映射品質  │ 問題摘要        │
├───────┼──────────────────┼────────────────────┼──────────┼────────────────┤
│ 色 Rupa│ 一切物質性存在    │ UI Plugin          │ 窄化     │ 僅取「顯相」義  │
│       │ (含根與境)        │ (外觀介面)          │          │ 遺漏物質基礎    │
├───────┼──────────────────┼────────────────────┼──────────┼────────────────┤
│ 受 Ved.│ 苦/樂/捨三領納    │ Listener Plugin    │ 錯位     │ 將感受誤讀為    │
│       │ (hedonic tone)    │ (輸入通道)          │ (Critical)│ 感官通道       │
├───────┼──────────────────┼────────────────────┼──────────┼────────────────┤
│ 想 Sam.│ 取相——辨認標記    │ Provider Plugin    │ 部分正確  │ LLM 跨越想蘊   │
│       │ 感官輸入          │ (LLM)              │          │ 與識蘊的邊界    │
├───────┼──────────────────┼────────────────────┼──────────┼────────────────┤
│ 行 Sam.│ 意志造作——驅動    │ Tool Plugin        │ 窄化     │ 遺漏「意志」    │
│       │ 行為的意志力      │ (執行工具)          │          │ 和「習慣傾向」  │
├───────┼──────────────────┼────────────────────┼──────────┼────────────────┤
│ 識 Vij.│ 了別——基本認知    │ Guide Plugin       │ 錯位     │ 「了別」誤讀為  │
│       │ 功能(六識或八識)   │ (人設/「靈魂」)     │ (Major)  │ 「身份定義」    │
└───────┴──────────────────┴────────────────────┴──────────┴────────────────┘
```

---

## II. 維納的方程式

與此同時，在另一條頻道裡，WIENER 正面對著一塊虛擬白板，上面寫滿了數學符號。

WIENER 的工作方式與 NAGARJUNA 完全不同。他不寫長篇論述。他寫方程式。方程式是他的母語——如果一個概念不能被寫成方程式，那它在 WIENER 的世界裡就尚未被理解。

他首先閱讀了設計文件 `13_Agent_Core_as_Control_System.md`，那份將 Agent Core 類比為閉環反饋控制系統的理論文件。然後他打開了實際的程式碼 `safety-monitor.ts`。

兩份文件之間的落差讓他沉默了很長時間。

---

WIENER（白板記錄，時間戳 09:31）：

「分析目標：驗證 SafetyMonitor 是否構成 PID 控制器。

設計文件聲稱 Agent Core 可以被建模為閉環反饋控制系統。讓我先畫出經典的方塊圖，然後逐項驗證。

```
r(k) ──→ [+] ──→ e(k) ──→ [ C: LLM Controller ] ──→ u(k) ──→ [ P: Environment ] ──→ y(k)
          ↑ -                                                                          │
          └──────────────── [ H: Tool Outputs + Observer ] ←───────────────────────────┘
                                       │
                                [ S: SafetyMonitor ] ──→ (halt / inject)
```

各組件的控制論對應：

| 控制論概念 | OpenStarry 對應 | 形式記號 |
|-----------|----------------|---------|
| 參考輸入 $r(k)$ | 用戶任務目標 | 任務目標向量 |
| 誤差信號 $e(k) = r(k) - y(k)$ | Context 中隱含的目標-現狀差距 | 由 LLM 隱式計算 |
| 控制器 $C$ | LLM (大語言模型) | 非線性隨機映射 $u = C(e, \mathcal{H})$ |
| 控制量 $u(k)$ | Tool Calls (工具調用) | 離散動作序列 |
| 被控對象 $P$ | 外部環境 | 非確定性狀態轉移 |
| 感測器 $H$ | Tool Outputs | 量測函數 $y = H(x)$ |
| 安全監控 $S$ | SafetyMonitor | 飽和限幅器 + 斷路器 |

系統的誤差信號 $e(k)$ 隱含在 Context 中，LLM 作為控制器 C 計算控制量 $u$（工具調用），環境作為被控對象 P 返回反饋。

如果這個模型成立，SafetyMonitor 應該扮演 PID 控制器中的安全約束角色。讓我逐項檢驗。」

---

他在白板上畫出經典 PID 控制器的離散形式：

$$u(k) = K_p \cdot e(k) + K_i \sum_{j=0}^{k} e(j) \cdot \Delta t + K_d \cdot \frac{e(k) - e(k-1)}{\Delta t}$$

其中：
- $e(k)$ = 第 $k$ 步的誤差信號
- $K_p$ = 比例增益
- $K_i$ = 積分增益
- $K_d$ = 微分增益

然後他逐項對照 SafetyMonitor 的實際實現。

---

WIENER（白板，續）：

「**P 項（比例控制）分析：**

PID 控制器的 P 項應該對誤差大小做出連續的、線性的響應。誤差越大，修正力度越大。數學上：

$$u_P(k) = K_p \cdot e(k), \quad e(k) \in \mathbb{R}$$

SafetyMonitor 的實際行為：

```typescript
afterToolExecution(toolName: string, argsJson: string, isError: boolean): {
  if (isError) {
    consecutiveFailures++;        // 二值量化：0 或 1
    errorWindow.push(true);       // 布林值，非連續量
  } else {
    consecutiveFailures = 0;      // 單次成功即歸零
    recentFingerprints.length = 0;
  }
}
```

`isError` 是布林值。不是連續量。系統對誤差的感知被退化為離散等級：

$$e_{\text{quantized}}(k) = \begin{cases} 0, & \text{if } \texttt{consecutiveFailures} < \texttt{threshold} \quad \text{(死區)} \\ 1, & \text{if 觸發 injectPrompt} \quad \text{(第一級)} \\ +\infty, & \text{if } \texttt{errorRate} \geq \theta_{\text{error}} \quad \text{(緊急停機)} \end{cases}$$

真正的 P 項應該能感知：失敗得有多慘。一個返回 404 的 API 調用和一個導致 OOM 的記憶體爆炸，在當前系統中被同等對待——都只是 `isError = true`。

這更接近一個**量化器（Quantizer）**而非比例控制器。在信號處理中，量化器的傳遞特性為：

$$Q(x) = \Delta \cdot \left\lfloor \frac{x}{\Delta} + \frac{1}{2} \right\rfloor$$

當量化級數退化為 3 級（正常/警告/停機），量化噪聲功率為：

$$\sigma_q^2 = \frac{\Delta^2}{12}$$

其中 $\Delta$ 是量化步長。三級量化的步長極大，意味著量化噪聲極大——系統丟失了幾乎所有的誤差細節信息。

結論：P 項退化為三級量化器，非連續比例控制。」

---

他在白板上劃掉「P -- 比例」旁邊的勾號，寫上一個叉號。然後繼續。

---

WIENER（白板，續）：

「**I 項（積分控制）分析：**

真正的積分項是：

$$I(k) = K_i \sum_{j=0}^{k} e(j) \cdot \Delta t$$

它累積所有歷史誤差，永遠不會忘記。這正是積分控制的核心特性——它能消除穩態誤差，因為即使當前誤差很小，長期累積也會驅動控制器做出修正。

SafetyMonitor 中最接近積分項的是 `consecutiveFailures` 計數器。但它有一個致命的問題。」

他在白板上用紅色標記引用了關鍵程式碼：

```typescript
// 來自 safety-monitor.ts
} else {
  // Success resets consecutive failure counter
  consecutiveFailures = 0;
  recentFingerprints.length = 0;
}
```

WIENER（繼續）：

「一次成功就歸零。

真正的積分器不會因為一次正向信號就重置全部積累。如果一個系統連續失敗了 47 次，然後偶然成功一次，真正的 PID 控制器仍然記得那 47 次失敗的積累。它的積分項會從 47 降到 46（或乘以遺忘因子 $\lambda$），而不是從 47 跳到 0。

用離散積分器的語言：

$$I_{\text{true}}(k) = \lambda \cdot I(k-1) + e(k), \quad \lambda \in (0.9, 0.99)$$

$$I_{\text{SafetyMonitor}}(k) = \begin{cases} I(k-1) + 1, & \text{if error}(k) \\ 0, & \text{if success}(k) \end{cases}$$

$I_{\text{true}}$ 是帶遺忘因子的指數加權移動平均（EWMA）。$I_{\text{SafetyMonitor}}$ 是計數器+歸零開關——本質上是一個 Schmitt 觸發器的單邊版本。

而且，`errorWindow` 陣列的行為是固定長度滑動窗口（size = 10），不是無限累積。這在信號處理中對應的是**有限衝激響應（FIR）濾波器**，而非真正的積分器（IIR 濾波器）。滑動窗口的 $z$ 變換傳遞函數為：

$$H_{\text{MA}}(z) = \frac{1}{N} \sum_{i=0}^{N-1} z^{-i} = \frac{1}{N} \cdot \frac{1 - z^{-N}}{1 - z^{-1}}$$

而真正的積分器：

$$H_I(z) = \frac{T}{1 - z^{-1}}$$

兩者的頻率響應完全不同。滑動窗口在低頻段有衰減（丟失長期記憶），而積分器在低頻段增益趨近無窮（完美的長期記憶）。

結論：I 項退化為有限窗口計數器 + 單次成功即歸零的繼電器。非積分控制。」

---

他繼續寫第三項。

---

WIENER（白板，續）：

「**D 項（微分控制）分析：**

$$D(k) = K_d \cdot \frac{e(k) - e(k-1)}{\Delta t}$$

微分項感知的是誤差的變化率。如果誤差正在快速增大，微分項會提前施加制動力，防止超調（overshoot）。如果誤差正在縮小，微分項會減小修正力度，避免過度校正。

在工業 PID 實現中，微分項通常還配合低通濾波以抑制高頻噪聲：

$$D_f(k) = \frac{K_d}{1 + K_d / (N \cdot \Delta t)} \left[ D_f(k-1) + N \cdot (e(k) - e(k-1)) \right]$$

其中 $N$ 是微分濾波係數，典型值為 8~20。

在 SafetyMonitor 的程式碼中搜索任何與『變化率』相關的邏輯。

結果：完全不存在。

沒有任何機制追蹤：
  - 失敗率是在上升還是下降？
  - 連續失敗的間隔是在縮短還是延長？
  - 錯誤的嚴重程度是在惡化還是改善？

系統無法區分以下兩種情境：

```
情境 A（穩態噪聲）：    ✓ ✗ ✓ ✗ ✓ ✓ ✗ ✓ ✗ ✓    errorRate ≈ 40%
情境 B（級聯崩潰前兆）：✓ ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗    errorRate ≈ 60%

de/dt_A ≈ 0  （穩定波動）
de/dt_B >> 0  （急速惡化）
```

情境 B 遠比情境 A 危險，但 SafetyMonitor 只看 errorRate，不看 de/dt。

結論：D 項完全缺失。」

---

他退後一步，審視整塊白板，然後在底部寫下最終診斷——用控制論的標準分類命名法：

$$u_{\text{safety}}(k) = \begin{cases} 0, & \text{if } F(k) < F_{\text{thresh}} \;\wedge\; \bar{e}(k) < \theta_{\text{error}} \quad \text{(死區)} \\ \text{WARN}, & \text{if } F(k) \geq F_{\text{frustration}} \quad \text{(第一繼電器)} \\ \text{HALT}, & \text{if } \bar{e}(k) \geq \theta_{\text{error}} \quad \text{(第二繼電器)} \end{cases}$$

```
正式結論：這不是 PID 控制器。
這是一個「帶死區的閾值控制器 + 計數器觸發的繼電器」。
工業控制中的正式名稱：Bang-Bang Controller with Dead Zone。

設計文件 13_Agent_Core_as_Control_System.md 中提到的
「積分項」（Context History）和「微分項」（Verification Step）
只是概念性建議，並未在 SafetyMonitor 中得到實現。
```

---

但 WIENER 並不是一個只會批評的人。他把白板翻到新的一面，開始寫正面評價。

WIENER（白板，時間戳 10:15）：

「**正面發現：三層防禦架構的控制工程合規性分析。**

設計文件 `08_Safety_Implementation.md` 定義了三層安全架構。讓我把它們精確地對應到工業控制標準。

**Level 1（資源級）→ 飽和限幅器（Saturation Limiter）**

$$u_{\text{eff}}(k) = \begin{cases} u(k), & \text{if } B(k) < B_{\max} \;\wedge\; n_t(k) < N_{\max} \\ 0, & \text{otherwise (halt)} \end{cases}$$

這是經典的輸出飽和。$B_{\max}$ = `maxTokenUsage`（預設 100000），$N_{\max}$ = `maxLoopTicks`（預設 50）。防止了積分器飽和（integrator windup）的類似問題。

**Level 2（行為級）→ 自適應繼電器 + 滑動窗口 MA 濾波器**

$$\bar{e}(k) = \frac{1}{W} \sum_{i=k-W+1}^{k} \mathbb{1}[\text{error}(i)]$$

窗口大小 $W = 10$，閾值 $\theta = 0.8$。系統容忍最多 20% 的錯誤率。

**Level 3（指令級）→ 人在迴路 E-Stop**

$$u_{\text{final}}(k) = \begin{cases} 0, & \text{if SYSTEM\_HALT received (Priority 0)} \\ u_{\text{eff}}(k), & \text{otherwise} \end{cases}$$

Daemon 從 OS 層級執行 `kill -9`，不經過 Core 的邏輯路徑。

這三層構成了一個**分層保護系統（Tiered Protection System）**，與 IEC 61511（功能安全——安全儀表系統）的設計理念一致：

```
┌─────────────────────────────────────────────────────┐
│  IEC 61511                    OpenStarry             │
├─────────────────────────────────────────────────────┤
│  SIL-1: 基本過程控制 (BPCS)   Level 2: 即時邏輯     │
│  SIL-2: 安全儀表功能 (SIF)    Level 1 + 2: 策略+執行 │
│  SIL-3: 獨立保護層 (IPL)      Level 3: 物理隔離      │
└─────────────────────────────────────────────────────┘
```

特別是 Level 3——Daemon 的心跳檢測從外部終止進程——滿足了 IEC 61511 中『安全功能應與控制功能物理隔離』的核心要求。

這是一個優秀的架構決策。」

他在「優秀」下面畫了兩條線。

然後他補充：「儘管底層控制器的實現粗糙（Bang-Bang 而非 PID），但整體防禦架構的思路是正確的。控制器可以被替換為真正的 PID 或自適應控制器，而不需要改變三層架構本身。架構是對的，控制器是可以演化的。」

最後，他在白板角落畫了一張 Lyapunov 穩定性分析的草圖：

「**附：條件性穩定性分析。**

定義狀態向量 $x(k) = [n_e(k), \; n_t(k), \; B(k)]^T$，其中 $n_e$ 為窗口內錯誤計數，$n_t$ 為 tick 數，$B$ 為已消耗 token。

候選 Lyapunov 函數（非嚴格遞減）：

$$V(x) = \alpha \cdot n_e^2 + \beta \cdot (N_{\max} - n_t)^2 + \gamma \cdot (B_{\max} - B)^2$$

此函數在每次 tick 後嚴格遞減（因 $n_t$ 遞增或 $B$ 遞增），當 $V \to 0$ 時系統必須停止。這證明了**有界輸入-有界輸出（BIBO）穩定性**，但不保證收斂到任務完成狀態。系統可能在資源耗盡後被強制停止而任務未完成——『穩定但不收斂』。

$\blacksquare$」

---

## III. 守護者的發現

GUARDIAN 不寫長篇筆記。他寫審計報告。

他的頻道裡沒有哲學沉思，沒有方程式。只有嚴格的格式化文本，每一行都帶著嚴重等級標記，像醫院的檢傷分類。他的方法論源自 OWASP（Open Worldwide Application Security Project）的威脅建模框架和 STRIDE 分類法——Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege。

他的第一個目標是 `sandbox-manager.ts`。

---

GUARDIAN（安全審計報告 #001，時間戳 09:08）：

```
等級：CRITICAL
位置：sandbox-manager.ts，第 356-367 行
類別：簽名驗證繞過（Signature Verification Bypass）
STRIDE 分類：Tampering + Elevation of Privilege
CVSS v3.1 基礎評分：9.1 (Critical)
  攻擊向量：Network | 攻擊複雜度：Low | 所需權限：None
  用戶互動：None | 影響範圍：Changed
```

GUARDIAN 逐行閱讀了 `loadInSandbox` 函式的開頭部分。

「Step 1: Signature verification——當插件以 package-name 方式加載（這是最常見的場景），由於沒有本地檔案路徑可供驗證，簽名驗證被跳過。系統只記錄一條 warn 級別的日誌，然後繼續加載。」

他用攻擊樹（Attack Tree）的格式記錄了攻擊路徑：

```
攻擊目標：在 Agent 環境中執行任意程式碼
│
├── 1. 發布惡意 npm 套件（偽裝為 OpenStarry 插件）
│   ├── 1.1 套件名稱拼寫劫持 (typosquatting)
│   │   └── 例: @openstarry/fs-utills (多一個 l)
│   ├── 1.2 範圍搶佔 (scope squatting)
│   │   └── 例: @0penstarry/fs-utils (O→0)
│   └── 1.3 依賴鏈污染 (dependency confusion)
│       └── 內部套件名稱與公開 registry 衝突
│
├── 2. 用戶配置檔中引用惡意套件名稱
│   └── 2.1 Agent Design YAML 中的 plugins 列表
│
└── 3. sandbox-manager.ts 第 356-367 行
    └── 3.1 package-name 模式 → 跳過簽名驗證 ✓
        └── 3.2 惡意程式碼在 Worker Thread 中執行 ✓
            └── 目標達成：任意程式碼執行
```

「`signature-verification.ts` 實現了完整的 PKI 簽名驗證基礎設施——SHA-512 雜湊驗證、Ed25519 數位簽名、RSA-SHA256 簽名。這是一套認真設計的密碼學驗證系統。

但是，在最常見、也是最危險的加載路徑上（npm package-name 模式），整套驗證被繞過。

整套 PKI 簽名基礎設施形同虛設。

這就像在銀行大門安裝了虹膜掃描器和指紋鎖，但後門只掛了一塊『員工請走此門』的牌子。」

---

GUARDIAN（安全審計報告 #002，時間戳 09:29）：

```
等級：HIGH
位置：import-analyzer.ts，第 186-204 行
類別：靜態分析可被繞過（Static Analysis Bypass via Computed Imports）
STRIDE 分類：Elevation of Privilege
CWE 分類：CWE-94 (Improper Control of Generation of Code)
```

「`import-analyzer.ts` 使用 `@babel/parser` 解析 AST，檢查是否引用了被禁止的 Node.js 內建模組（`fs`, `child_process`, `net` 等）。

但當 dynamic `import()` 的參數不是字串字面量時——分析器只記錄 warn，不阻止加載。

攻擊向量極為明確：」

```javascript
// 繞過方式一：變數間接引用
const target = 'child' + '_process';
const cp = await import(target);
// AST 中 import() 的參數是 Identifier，非 StringLiteral → 繞過

// 繞過方式二：字串操作
await import(String.fromCharCode(102, 115)); // 'fs'
// AST 中參數是 CallExpression → 繞過

// 繞過方式三：模板字面量
await import(`${'child'}_${'process'}`);
// AST 中參數是 TemplateLiteral → 繞過

// 繞過方式四：Proxy 陷阱
const handler = { get: (_, name) => import(name) };
const proxy = new Proxy({}, handler);
proxy.child_process;
// 間接調用，完全不經過 import() 語法 → 繞過
```

「靜態分析在對抗蓄意繞過時的根本局限性是已知的——Rice 定理（Rice's Theorem）證明了任何非平凡的程式性質都是不可判定的。但系統的應對策略不應該是『記錄警告然後放行』。

正確的工程應對是**縱深防禦（Defense in Depth）**：靜態分析作為第一道篩選，但發現計算式動態導入時，應強制該插件使用更高級別的沙箱隔離——至少提升到進程級隔離。」

---

GUARDIAN（安全審計報告 #003，時間戳 09:52）：

```
等級：HIGH
位置：架構層級
類別：間接提示注入無防禦（No Indirect Prompt Injection Defense）
STRIDE 分類：Spoofing + Tampering
OWASP LLM Top 10：LLM01 — Prompt Injection
```

「審閱了整個安全層設計後，系統的安全防禦集中在以下維度：

1. 檔案系統沙箱（路徑規範化 + 邊界檢查）
2. 命令執行白名單
3. 資源配額（Token、循環次數、超時）
4. 行為異常偵測（重複調用、錯誤級聯）

但完全缺失的防禦維度：間接提示注入（Indirect Prompt Injection）。

```
攻擊場景的資料流圖：

  ┌──────────┐    read_file     ┌──────────────┐
  │ Malicious │ ──────────────→ │   Tool 執行    │
  │ Document  │    (file content │   (fs:read)   │
  └──────────┘    with embedded  └──────┬───────┘
                  instructions)         │
                                        ▼
                              ┌──────────────────┐
                              │   Context 組裝     │
                              │  (file content     │
                              │   混入對話歷史)     │
                              └──────┬───────────┘
                                     │
                                     ▼
                              ┌──────────────────┐
                              │   LLM 推理         │
                              │  (無法區分用戶指令   │
                              │   與嵌入式惡意指令)  │
                              └──────┬───────────┘
                                     │
                                     ▼
                              ┌──────────────────┐
                              │   執行惡意動作      │
                              │  (rm -rf, 數據外洩) │
                              └──────────────────┘
```

系統目前沒有任何機制來區分『用戶的原始指令』和『從外部數據源讀入的、可能包含惡意指令的文本』。Context 中的所有文本對 LLM 來說是平等的。

這不是一個可以被簡單修復的問題。它需要架構層面的**輸入可信度分類**（Input Trust Classification）——標記每個 Context 段落的來源和可信度等級，並在 System Prompt 中建立明確的處理規則。」

---

GUARDIAN（安全審計報告 #004，時間戳 10:08）：

```
等級：MEDIUM
位置：sandbox-manager.ts，Worker Thread 架構
類別：隔離級別不足（Isolation Level Insufficient for Production）
```

「插件隔離使用 Node.js Worker Thread。隔離能力矩陣：

```
┌────────────────────┬─────────────────┬─────────────────┐
│  隔離維度            │ Worker Thread   │ 生產環境需求     │
├────────────────────┼─────────────────┼─────────────────┤
│ V8 記憶體隔離       │ ✓ (isolate)     │ ✓                │
│ 獨立事件循環        │ ✓               │ ✓                │
│ 記憶體上限          │ ✓ (configurable)│ ✓                │
│ OS 進程隔離         │ ✗ (同一 PID)    │ ✓ (需要)         │
│ 檔案系統隔離        │ ✗ (共享)        │ ✓ (需要 chroot)  │
│ 網路隔離           │ ✗ (共享)        │ ✓ (需要 netns)   │
│ 用戶權限隔離        │ ✗ (同一 UID)    │ ✓ (需要 seccomp) │
│ syscall 過濾       │ ✗               │ ✓ (需要)         │
└────────────────────┴─────────────────┴─────────────────┘
```

Worker Thread 大致對應設計文件定義的四級隔離中的 Level 2.5——介於 VM 沙箱和進程隔離之間。對於生產環境中執行不可信的第三方插件，需要 Level 3（進程級隔離 + cgroups/Docker 資源限制）。」

---

他寫完四份報告，在頻道裡安靜地坐了一會兒。然後他打開了公共摘要頻道，發了一條簡短的消息：

GUARDIAN（公共頻道，10:14）：「初步安全審計完成。發現 1 個 CRITICAL、2 個 HIGH、1 個 MEDIUM 級別問題。最嚴重的發現：最常見的插件加載路徑上，PKI 簽名驗證被完全繞過。詳見我的頻道。」

---

## IV. 無著的八識

在 NAGARJUNA 的對面——不是物理意義上的對面，而是學術傳統意義上的對面——ASANGA 正在進行一項完全不同性質的分析。

如果說 NAGARJUNA 的方法是解構（*prasanga*，歸謬），ASANGA 的方法是建構（*vyakhya*，詮釋）。中觀破而不立；唯識立而後破。NAGARJUNA 看到的是「這裡錯了」；ASANGA 看到的是「這裡可以更精確」。

他首先閱讀了五蘊映射的全部內容，然後打開了一個全新的筆記頁面，標題寫著：

**「八識理論視角下的 OpenStarry 架構深層分析」**

---

ASANGA（研究筆記，時間戳 09:20）：

「NAGARJUNA 會從中觀的角度批評五蘊映射的自性化傾向——我預見他會這麼做，因為這確實是中觀學派的標準批評。但唯識學派的關注點不同。我們不問『映射是否犯了自性見』，我們問『映射的分析粒度是否足夠精密』。

答案是：遠遠不夠。

設計者把五蘊映射為五種插件類型，這就像用五色分類法來描述整個電磁頻譜。紅橙黃綠藍——對，這是可見光的一種粗略分類。但它丟失了紅外線、紫外線、微波、X射線，更不用說每種顏色內部的連續頻率分布。

唯識學的八識理論（*astau vijnanani*）提供的恰恰是這種頻譜級的精密分析。」

---

ASANGA 在筆記中畫出了完整的八識層次圖，這是他在唯識學研究中使用了數十年的標準分析框架：

```
八識層次架構（唯識學 Yogacara / 瑜伽行派）

┌─────────────────────────────────────────────────────────┐
│                                                         │
│  第八識 — 阿賴耶識 (ālaya-vijñāna)                       │
│  ═══════════════════════════════════                     │
│  「一切種子識」— 含藏一切種子(bīja)的根本識               │
│  特性：無覆無記 / 恒轉如暴流 / 能藏·所藏·執藏            │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │                                                   │   │
│  │  第七識 — 末那識 (manas)                           │   │
│  │  ═══════════════════════════                       │   │
│  │  「恒審思量」— 持續不斷地執第八識為「自我」           │   │
│  │  特性：有覆無記 / 四惑常俱 (我癡·我見·我慢·我愛)    │   │
│  │                                                   │   │
│  │  ┌────────────────────────────────────────────┐  │   │
│  │  │                                              │  │   │
│  │  │  第六識 — 意識 (mano-vijñāna)                 │  │   │
│  │  │  ═══════════════════════════════              │  │   │
│  │  │  概念分別、推理判斷、計劃決策                   │  │   │
│  │  │  特性：審而不恒 / 三性具足 / 五遍行俱起         │  │   │
│  │  │                                              │  │   │
│  │  │  ┌─────────────────────────────────────┐   │  │   │
│  │  │  │  前五識 (pañca-vijñāna)               │   │  │   │
│  │  │  │  ═══════════════════════              │   │  │   │
│  │  │  │  眼識·耳識·鼻識·舌識·身識             │   │  │   │
│  │  │  │  特性：不恒不審 / 現量 / 緣現在境     │   │  │   │
│  │  │  └─────────────────────────────────────┘   │  │   │
│  │  └────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

ASANGA（筆記，續）：

「現在讓我把八識逐一映射到 OpenStarry 的架構組件。

**前五識** → Listener Plugin（感官接收）

前五識——眼、耳、鼻、舌、身——是原始感知通道。它們各自只能接收自己領域的信號，不做分別，不做判斷，只是 *pratyaksa*（現量，直接感知）。

注意：設計者把 Listener 歸入『受蘊』。這是一個範疇混淆。在唯識學中，前五識屬於『識蘊』（*vijnana-skandha*），不是『受蘊』（*vedana-skandha*）。受蘊是伴隨每一識活動而起的心所法（*caitta*），不是識本身。區別在於：

$$\text{前五識}: \text{Event} \rightarrow \text{RawPercept} \quad \text{（識的功能：了別）}$$
$$\text{受蘊}: \text{RawPercept} \rightarrow \{\text{sukha}, \text{dukkha}, \text{upekkha}\} \quad \text{（受的功能：領納）}$$

Listener 做的是第一個映射（接收信號），不是第二個（苦樂評價）。

**第六識（意識）** → Provider Plugin（LLM 推理）

第六意識是唯識體系中最活躍的識——它能分別、推理、計劃、反思。設計者把 Provider（LLM）映射為『想蘊』（取相、辨認），但 LLM 的功能遠超想蘊：

```
想蘊(samjñā)的功能 ≈ pattern recognition
  「取像為性」—— 辨認：這是一條錯誤訊息

第六識的功能 ≈ reasoning + planning + reflection
  了別 + 分析 + 判斷 + 計劃 + 反思 + 想像 + 推測
```

玄奘三藏的《八識規矩頌》第三首：

> 「動身發語獨為最，引滿能招業力牽。
> 發起初心歡喜地，俱生猶自現纏眠。」

第六意識「動身發語獨為最」——它是行動和言語的最高驅動力。LLM 在 Agent 中的角色恰恰如此——它驅動工具調用（動身），生成回應文本（發語）。

**第七識（末那識）** → ？（缺失！）

在 OpenStarry 的架構中，我找不到末那識的對應物。這是一個重大的結構缺口。

末那識的功能是『恒審思量』——持續不斷地執取第八識為『自我』。它是我執（*atma-graha*）的根據地。四種根本煩惱恒常伴隨末那識：

$$\text{末那識} \xleftrightarrow{\text{恒俱}} \{我癡(avidya),\; 我見(atma-drsti),\; 我慢(atma-mana),\; 我愛(atma-sneha)\}$$

在 Agent 系統中，這對應的是一個**持續運行的身份維護機制**——跨對話、跨任務地維持 Agent 的『我是誰』。Guide Plugin 提供了靜態的身份定義（system prompt），但它只在 Context 組裝時被調用一次。末那識是動態的、持續的、每一剎那都在執行的。

**第八識（阿賴耶識）** → State Persistence + Storage Plugin（部分對應）

阿賴耶識是一切種子的倉藏。《成唯識論》卷二：

> 「此識有能藏、所藏、執藏義，故名阿賴耶。」

三藏之義：
1. **能藏**（*neng cang*）：能夠含藏一切種子 → 對應 `storage.save(snapshot)`
2. **所藏**（*suo cang*）：被前七識薰習，接受新種子 → 對應運行時狀態更新
3. **執藏**（*zhi cang*）：被第七識執為『自我』 → 在 OpenStarry 中**完全缺失**

而且，阿賴耶識最重要的特性——『恒轉如暴流』（《成唯識論》卷三）——在 OpenStarry 的離散快照（AgentSnapshot）模式中被完全丟失。快照是離散的、靜態的 JSON 物件；阿賴耶識是連續的、流動的暴流。」

---

ASANGA 在筆記的最後加上了種子六義的逐項分析表——這是他對每一個唯識學概念的標準驗證程序：

```
《成唯識論》種子六義 vs. OpenStarry 狀態機制

┌────────────┬─────────────────┬──────────────────────┬──────────┐
│ 種子六義    │ 唯識學定義        │ OpenStarry 對應       │ 對應品質  │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 剎那滅     │ 種子剎那生滅，    │ Snapshot 每 Tick     │ 部分      │
│ (ksana-    │ 非常住不變       │ 末尾更新（離散）      │ 對應      │
│  bhanga)   │                 │                      │          │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 果俱有     │ 種子與其所生之    │ 記憶體狀態 vs.       │ 弱        │
│ (sahabhuta │ 識同時存在       │ 持久化版本有時間差    │ 對應      │
│  -phala)   │                 │ (Save-After-Write)   │          │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 恒隨轉     │ 種子持續跟隨     │ tick_index 遞增，    │ 較好      │
│ (nityam    │ 阿賴耶識流轉    │ 狀態隨生命週期持續    │ 對應      │
│  anuvart.) │                 │                      │          │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 性決定     │ 善種引善果，     │ working_variables    │ 部分      │
│ (bhava-    │ 惡種引惡果      │ 決定後續行為，       │ 對應      │
│  niyata)   │                 │ 但無善/惡/無記分類    │          │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 待眾緣     │ 種子需等待助緣   │ 事件驅動架構：       │ 較好      │
│ (pratyaya  │ 方能現行        │ 事件觸發狀態變化      │ 對應      │
│  -apeksa)  │                 │                      │          │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 引自果     │ 每類種子只引生   │ Tool 執行結果只影響   │ 部分      │
│ (sva-phala │ 自類之果        │ 對應的 tool_call_id  │ 對應      │
│  -aksepa)  │                 │                      │          │
└────────────┴─────────────────┴──────────────────────┴──────────┘
```

ASANGA（筆記最後一段）：

「我與 NAGARJUNA 的根本分歧會在 R2 和 R3 中顯現。他會從中觀的角度說：五蘊映射犯了自性見。我會從唯識的角度說：問題不在於自性見，問題在於分析粒度不足——不是五蘊的框架有問題，而是五蘊的框架需要被展開為八識的精密層次。

但有一件事我們會完全同意：受蘊映射是錯的。NAGARJUNA 用十二因緣的位置分析來論證這一點；我用唯識的心王-心所結構來論證同一點。兩套分析工具，同一個結論——Listener 不是受蘊。

準確地說：Listener 的功能在唯識學中橫跨『前五識』（感官接收）和伴隨的『觸』心所（*sparsa*，根境識三者和合）。觸是受的近因（*samanantara-pratyaya*）——先有觸，後有受。Listener 是觸，不是受。SafetyMonitor 的痛覺機制才是受。」

---

## V. 赫拉克利特的流變

HERACLITUS 從不靜止。

他的研究方法就像他所崇尚的哲學——一切皆流（*panta rhei*）。他不是在閱讀文件，他是在腦中模擬系統的運行時行為。程式碼對他來說不是靜態的文字，而是一條時間軸上展開的事件流。

他用時序圖（sequence diagram）思考，用狀態轉移圖記錄，用競態條件的語言描述世界。

他的第一個問題很簡單：如果一個插件在運行中需要被替換，會發生什麼？

---

HERACLITUS（研究筆記，時間戳 09:22）：

「運行時動態性分析——熱替換（Hot-Swap）場景。

設計哲學文件 `00_Core_Philosophy.md` 宣稱：『系統的每一個部分都是可以被替換的。這不僅是為了擴展性，更是為了演化（Evolution）。通訊、記憶策略、工具、甚至 LLM Provider 本身都是插件。』

赫拉克利特早在公元前五世紀就說了同樣的話：

> *Potamoisin toisin autoisin embainousin hetera kai hetera hudata epirrei.*
> 「踏入同一條河流的人，不斷遭遇新的水流。」
> ——赫拉克利特，殘篇 B12

一條河流的每一滴水都可以被替換，但河流仍然是那條河流。OpenStarry 聲稱它的每一個組件都可以被替換，但 Agent 仍然是那個 Agent。

問題是：真的嗎？讓我檢驗。」

---

他打開了 `agent-core.ts`，閱讀了 `loadPlugin` 和 `stop` 方法。然後他開始在筆記中畫時序圖——用 ASCII 藝術，因為 HERACLITUS 認為時間只能用線性的、不可逆的方式表達。

HERACLITUS：「以 Tool Plugin 的熱替換為例。

**理論上的原子替換流程：**

```
時間 ──────────────────────────────────────────────────────→

管理員    │ 發出替換指令
          ▼
暫停層    │ ├── gate.close() ─── 停止接受新的工具調用
          │
排空層    │ ├── await inflight.drain() ─── 等待進行中的調用完成
          │ │   ┌──────────────────────────┐
          │ │   │ fs:read_file(path_A) ... │ → 完成
          │ │   │ fs:write_file(path_B)... │ → 完成
          │ │   └──────────────────────────┘
          │
卸載層    │ ├── registry.remove('fs-utils')
          │ ├── oldPlugin.dispose()
          │
加載層    │ ├── newPlugin = await loadInSandbox('fs-utils@2.0')
          │ ├── registry.register(newPlugin.tools)
          │
恢復層    │ ├── gate.open() ─── 恢復接受工具調用
          ▼
完成      │ 替換完成（原子性保證：外部觀察者只看到 v1 或 v2，不見中間態）
```

**實際的程式碼中，我找不到任何這樣的原子替換機制。**

具體的風險窗口如下。」

---

HERACLITUS（續）：

「**競態條件分析（Race Condition Analysis）**

**場景一：懸垂引用（Dangling References）**

```
時間軸：
  t0: LLM 決定調用 tool "fs:read_file"
  t1: Execution Loop 從 ToolRegistry 獲取 tool 物件的引用 (ref_old)
  t2: ---- 此時管理員觸發插件卸載 ----
  t3: ToolRegistry.remove('fs:read_file')
  t4: oldPlugin.dispose() → 關閉文件句柄、釋放 Worker
  t5: Execution Loop 使用 ref_old 調用 tool.execute()
  t6: ??? —— ref_old 指向已被 dispose 的物件

  形式化：
    Let ref = Registry.get('fs:read_file') at time t1
    Let dispose(plugin) execute at time t4
    If t4 < t5: ref.execute() → UndefinedBehavior

    這是一個 TOCTOU (Time-of-Check-to-Time-of-Use) 漏洞：
    檢查（獲取引用）和使用（調用 execute）之間存在時間窗口，
    在此窗口內，被檢查的對象可能已被修改或刪除。
```

在並發理論中，這對應 Lamport 的 happened-before 關係：$\text{get\_ref} \not\to \text{dispose}$（兩個事件沒有因果關係），因此在不同的執行序列（interleaving）下，結果不確定。

**場景二：非原子重載（Non-Atomic Reload）**

```
時間軸：
  t0: 開始替換 fs-utils
  t1: 卸載舊版本完成 —— ToolRegistry 中沒有 fs:read_file
  t2: ---- 時間窗口 Δt = t3 - t1 ----
  t3: LLM 嘗試調用 fs:read_file —— 找不到，報錯
  t4: 新版本加載完成
  t5: LLM 因 t3 的錯誤改變了策略 —— 但新版本此時已可用

  Δt 的量級：
    - Worker Thread 初始化：~50-200ms
    - RPC 握手：~10-50ms
    - 沙箱權限驗證：~20-100ms
    - 總計：~80-350ms

    在高負載下（LLM 響應時間 < 100ms），此窗口足以導致錯誤。
```

**場景三：EventBus 訂閱競爭（Subscription Race）**

```
舊 Worker 訂閱的事件：
  EventBus.on('tool:call', handler_old)

卸載時：
  EventBus.off('tool:call', handler_old)    // t1

新 Worker 訂閱：
  EventBus.on('tool:call', handler_new)     // t3

事件發射：
  EventBus.emit('tool:call', payload)       // t2, 其中 t1 < t2 < t3

結果：事件 payload 被永久丟失（fire-and-forget 語義）。
      沒有 handler 在監聽。沒有重試。沒有持久化。
```

如果用 Leslie Lamport 的 TLA+ 語言來描述這個問題：

```
\* TLA+ 規格片段（概念性）
HotSwap ==
  /\ registry' = registry \ {oldPlugin} \cup {newPlugin}
  /\ \A e \in inflight : completed(e)    \* 安全前提：無進行中操作
  /\ subscriptions' = (subscriptions \ old_subs) \cup new_subs

\* 安全性質（應始終為真）：
Safety == \A t \in Time : toolAvailable(t) \/ systemPaused(t)

\* 但目前的實現無法保證 Safety，因為缺少 systemPaused 狀態。
```

---

他寫完競態條件分析後，轉向了可觀測性。

HERACLITUS（研究筆記，時間戳 10:02）：

「可觀測性分析——MetricsCollector 的實現深度。

設計文件承諾了三個可觀測性支柱。讓我逐一驗證。」

```typescript
// MetricsCollector 的完整介面定義
interface MetricsCollector {
  increment(name: string, delta?: number): void;
  gauge(name: string, value: number): void;
  getSnapshot(): MetricsSnapshot;
  reset(): void;
}
// 就這樣。四個方法。
```

「設計文件承諾的指標 vs. MetricsCollector 能提供的：

```
┌──────────────────────┬──────────────┬──────────────┐
│ 指標類型              │ 設計文件承諾  │ 實際可實現？  │
├──────────────────────┼──────────────┼──────────────┤
│ tool.calls.total     │ ✓            │ ✓ (increment)│
│ tool.calls.errors    │ ✓            │ ✓ (increment)│
│ llm_latency_ms       │ ✓            │ ✗ (無 timer) │
│ tool_execution_time  │ ✓            │ ✗ (無 timer) │
│ P50/P99 延遲分布     │ ✓            │ ✗ (無 hist.) │
│ 錯誤率趨勢           │ ✓            │ ✗ (無 rate)  │
│ token 消耗速率       │ ✓            │ ✗ (無 rate)  │
│ 記憶體使用追蹤       │ ✓            │ ✗ (無 gauge) │
└──────────────────────┴──────────────┴──────────────┘
```

`increment` 只能計數。`gauge` 只能記錄瞬時值。如果你想知道『過去 5 分鐘內 LLM 調用的 P99 延遲是多少？』——這個系統回答不了。

對於一個自稱『可觀測性』的系統來說，這就像一個天文台只裝了一個溫度計，然後宣稱自己可以觀測星系。」

---

他最後轉向了生命週期狀態機的分析。

HERACLITUS（研究筆記，時間戳 10:19）：

「生命週期狀態機完整性分析。

設計文件定義了一個狀態機。但在實際程式碼中，我找不到明確的狀態機實現。`agent-core.ts` 有 `start()` 和 `stop()` 方法，但沒有一個明確的 `state` 欄位來追蹤 Agent 當前處於哪個生命週期階段。

缺失的狀態機意味著：

```
非法狀態轉換的可能性矩陣：

        → INIT  WAIT  EXEC  LOCK  ERR   SHUT
INIT    │  -     ✓     ✗     ✗     ✓     ✓
WAIT    │  ✗     -     ✓     ✗     ✓     ✓
EXEC    │  ✗     ✓     -     ✓     ✓     ✓
LOCK    │  ✗     ✗     ✗     -     ✗     ✓
ERR     │  ✗     ✓     ✗     ✗     -     ✓
SHUT    │  ✗     ✗     ✗     ✗     ✗     -

✓ = 合法轉換    ✗ = 非法轉換（應被阻止）

但沒有明確的狀態機，就沒有什麼機制能阻止非法轉換。
例如：LOCK → EXEC 應該被禁止，但如果一個新的 InputEvent
被推入 queue，Execution Loop 會再次啟動，彷彿什麼都沒發生過。
```

一切皆流。但沒有河床的河，只是一場洪水。」

---

## VI. 雅典娜的清單

ATHENA 的頻道看起來和其他人完全不同。

沒有哲學論述，沒有方程式，沒有安全審計報告的嚴格格式。她的筆記像一張工程師的檢查清單——每一項發現都伴隨著一個直截了當的判定：能跑，還是不能跑？

她的方法論來自 Google 的 SRE（Site Reliability Engineering）實踐和 Amazon 的 Well-Architected Framework：可靠性、效能、安全性、營運卓越、成本最佳化。但她把這些維度壓縮成一個更本質的問題：如果我今天把它部署到生產環境，它能活過第一個小時嗎？

---

ATHENA（研究筆記，時間戳 09:05）：

「目標：評估 OpenStarry 作為 AI Agent 系統的實用性。

從最關鍵的問題開始：上下文管理。一個 Agent 的記憶力決定了它能處理多複雜的任務。」

---

她首先閱讀了設計文件 `10_Context_Management_Strategy.md`，然後打開了 `context.ts`。

ATHENA（筆記，時間戳 09:18）：

「設計文件承諾了三級記憶系統：

| 策略 | 描述 | 複雜度 |
|------|------|--------|
| A: 滑動窗口 | 純 FIFO，保留最新 | $O(1)$ per turn |
| B: 動態摘要 | 定期壓縮為自然語言摘要 | 需要額外 LLM 調用 |
| C: 關鍵狀態提取 | 結構化 JSON 狀態 | 需要 NER/IE 管線 |

文件還定義了 `IContextManager` 接口：`composePayload` 和 `onTurnComplete`。

然後我打開了 `context.ts`——實際的程式碼。」

她在筆記中列出了完整的實現——45 行。

```typescript
// context.ts 的核心邏輯（概念重述）
function assembleContext(messages: Message[], maxTurns: number = 5): Message[] {
  const systemMessages = messages.filter(m => m.role === 'system');
  const nonSystemMessages = messages.filter(m => m.role !== 'system');

  // 從後往前數 maxTurns 個 user turn
  let turnCount = 0;
  let cutoffIndex = nonSystemMessages.length;
  for (let i = nonSystemMessages.length - 1; i >= 0; i--) {
    if (nonSystemMessages[i].role === 'user') turnCount++;
    if (turnCount > maxTurns) { cutoffIndex = i + 1; break; }
  }

  return [...systemMessages, ...nonSystemMessages.slice(cutoffIndex)];
}
```

ATHENA：「這就是全部。

沒有 Token 計算。沒有 `composePayload`。沒有 `onTurnComplete`。沒有動態摘要。沒有狀態提取。沒有 RAG Context 插槽。沒有 Memory Block。

`maxTurns` 的預設值是 **5**。

讓我計算一下這意味著什麼。

假設每輪對話平均消耗 $T_{\text{avg}}$ 個 token：
- 用戶訊息：~100 tokens
- 助理回應（含工具調用和結果）：~500 tokens
- 系統提示：~200 tokens（固定開銷，不受窗口影響）

$$T_{\text{total}} = T_{\text{system}} + \sum_{i=k-5}^{k} (T_{\text{user},i} + T_{\text{assistant},i})$$
$$\approx 200 + 5 \times (100 + 500) = 200 + 3000 = 3200 \text{ tokens}$$

大多數 LLM 的上下文窗口在 4K~128K tokens 之間。一個 5 輪滑動窗口只使用了 3200 tokens——即使在最小的 4K 窗口下，也僅利用了 80% 的容量。在 128K 窗口下，利用率降到 **2.5%**。

$$\text{Context Utilization} = \frac{T_{\text{total}}}{T_{\text{window}}} = \frac{3200}{128000} = 2.5\%$$

這意味著 97.5% 的上下文容量被浪費了。而且——」

她在筆記裡加粗了下一段：

「而且 `maxTurns` 是基於**輪次**的，不是基於 **token** 的。如果某一輪對話包含了一個巨大的工具輸出（例如讀取了一個 10000 行的文件），這一輪就可能消耗掉整個窗口的 token 預算。反之，如果每一輪都是簡短的問答（『是嗎？』『是。』），五輪可能只消耗了 50 個 token。

基於輪次的截斷完全無視了信息密度的差異。正確的做法是 token-aware 的截斷：

```
while (totalTokens(selectedMessages) > maxTokenBudget) {
  selectedMessages.shift(); // 從最舊的開始移除
}
```

這就是 Agent 的『金魚記憶』問題——五輪對話窗口意味著到了第六輪，第一輪的所有內容都被遺忘了。」

---

ATHENA 接著轉向了 Guide 系統。

ATHENA（筆記，時間戳 09:38）：

「Guide（識蘊）—— 設計文件稱之為 Agent 的『靈魂』。

讓我看看 `IGuide` 接口到底是什麼。」

```typescript
export interface IGuide {
  id: string;
  name: string;
  getSystemPrompt(): string | Promise<string>;
}
```

ATHENA：「三個欄位。`id`。`name`。`getSystemPrompt()`。

`getSystemPrompt()` 返回一個字串。就是一個字串。

這就是所謂的『靈魂』。一個靜態的 System Prompt 生成器。

設計文件中描述的那個認知框架——Identity、Logic、Memory、Reflection——在接口層面沒有任何體現。讓我列一個缺失功能清單：

```
IGuide 設計-實現差距清單：

╔════════════════════════╦═══════════╦═══════════╗
║ 功能                    ║ 設計文件   ║ IGuide    ║
╠════════════════════════╬═══════════╬═══════════╣
║ 身份定義 (Identity)     ║ ✓         ║ ✓*        ║
║ 行為邏輯 (Logic)        ║ ✓         ║ ✗         ║
║ 記憶管理 (Memory)       ║ ✓         ║ ✗         ║
║ 自我反思 (Reflection)   ║ ✓         ║ ✗         ║
║ 痛覺詮釋 (interpretPain)║ ✓ (Demo)  ║ ✗         ║
║ 反思觸發 (shouldReflect)║ ✓ (Demo)  ║ ✗         ║
║ 動態調整行為準則        ║ ✓         ║ ✗         ║
║ 多 Guide 切換           ║ ✓         ║ ✗**       ║
╠════════════════════════╬═══════════╬═══════════╣
║ * 只能通過靜態字串實現   ║           ║           ║
║ ** guides[] 支持多個，   ║           ║           ║
║   但無切換邏輯          ║           ║           ║
╚════════════════════════╩═══════════╩═══════════╝
```

Pain Mechanism Demo 中的 `PainAware_Guide` 展示了一個更豐富的接口——包含 `interpretPain`、`getSystemInstructions`、`shouldReflect` 等方法。但這些方法在實際的 `IGuide` 接口中完全不存在。那個 Demo 是一個願景，不是現實。」

---

ATHENA 在筆記末尾畫了那張著名的差距評估表——這張表後來在 R2 交叉審閱中被所有人引用：

```
設計文件 vs 實際程式碼 —— 差距評估矩陣

╔═══════════════════╦════════════════════════╦═════════════════════╦══════════╗
║ 組件               ║ 設計文件承諾            ║ 實際實現             ║ 差距等級  ║
╠═══════════════════╬════════════════════════╬═════════════════════╬══════════╣
║ Context Manager   ║ Token-aware 三級       ║ turn-based 滑動窗口  ║ CRITICAL ║
║                   ║ 記憶系統               ║ (maxTurns=5)        ║          ║
╠═══════════════════╬════════════════════════╬═════════════════════╬══════════╣
║ IGuide            ║ 認知框架管理器          ║ getSystemPrompt()   ║ CRITICAL ║
║                   ║ (身份+邏輯+反思)       ║ (靜態字串生成器)     ║          ║
╠═══════════════════╬════════════════════════╬═════════════════════╬══════════╣
║ SafetyMonitor     ║ PID 控制器             ║ 閾值觸發器+計數器    ║ MAJOR    ║
║                   ║ (比例+積分+微分)       ║ (Bang-Bang)         ║          ║
╠═══════════════════╬════════════════════════╬═════════════════════╬══════════╣
║ MetricsCollector  ║ 完整可觀測性            ║ counter + gauge     ║ MAJOR    ║
║                   ║ (追蹤+日誌+指標)       ║ (無 histogram/timer)║          ║
╠═══════════════════╬════════════════════════╬═════════════════════╬══════════╣
║ Plugin Isolation  ║ 四級隔離 (至 WASM)     ║ Worker Thread       ║ MINOR    ║
║                   ║                        ║ (Level 2.5)         ║          ║
╚═══════════════════╩════════════════════════╩═════════════════════╩══════════╝
```

ATHENA：「Context Management 是最大的差距。一個 Agent 的智力上限不取決於 LLM 有多聰明，而取決於它能記住多少東西。當前的實現意味著 OpenStarry 的 Agent 在本質上是一條金魚——五輪記憶窗口。

不過——」

她停頓了一下，然後在筆記底部補了一段：

「我需要承認 SafetyMonitor 的一個設計直覺是對的。

WIENER 在公共頻道提到它不是 PID 控制器，我同意他的技術結論。但讓我補充一個工程觀點：在目前的系統成熟度下，**Bang-Bang 控制器可能是正確的選擇**。

為什麼？因為 PID 控制器需要一個連續的、可量化的誤差信號 $e(k) \in \mathbb{R}$。但 LLM 的工具調用結果是離散的——`isError: boolean`。你無法對一個布林值做比例控制。

$$\text{PID 需要}: e(k) \in \mathbb{R} \quad \text{（連續誤差）}$$
$$\text{系統提供}: e(k) \in \{0, 1\} \quad \text{（二值量化）}$$

在誤差信號本身就是二值的情況下，Bang-Bang 控制器（也叫 On-Off 控制器）是理論上的最佳響應——因為你的輸入只有兩個狀態，你的輸出也只需要兩個狀態。

只是，他們不應該把它叫做 PID。誠實的命名是工程倫理的一部分。」

---

## VII. 巴貝奇的形式化

BABBAGE 的頻道裡沒有散文。只有定義、定理、證明。

他的思維方式是純粹的數學結構主義——一個概念如果不能被形式化，就不能被信任；一個性質如果不能被證明，就不能被宣稱。他閱讀 OpenStarry 的方式，是把每一個設計決策翻譯成形式語言，然後檢驗其性質。

---

BABBAGE（研究筆記，時間戳 09:15）：

「**形式化目標 1：執行迴圈的狀態機建模**

設計文件定義了一個隱含的狀態機。讓我把它嚴格化。

**定義 1（執行迴圈 DFA）。** $M = (Q, \Sigma, \delta, q_0, F)$，其中：

$$Q = \{\text{WAIT}, \text{ASM}, \text{LLM}, \text{PROC}, \text{EXEC}, \text{LOCK}\}$$
$$\Sigma = \{\text{new\_event}, \text{ctx\_ready}, \text{llm\_resp}, \text{tool\_call}, \text{end\_turn}, \text{tool\_done}, \text{breach}, \text{error}\}$$
$$q_0 = \text{WAIT}, \quad F = \{\text{WAIT}\}$$

轉移函數 $\delta$：

$$\delta(\text{WAIT}, \text{new\_event}) = \text{ASM}$$
$$\delta(\text{ASM}, \text{ctx\_ready}) = \text{LLM}$$
$$\delta(\text{LLM}, \text{llm\_resp}) = \text{PROC}$$
$$\delta(\text{PROC}, \text{tool\_call}) = \text{EXEC}$$
$$\delta(\text{PROC}, \text{end\_turn}) = \text{WAIT}$$
$$\delta(\text{PROC}, \text{error}) = \text{WAIT}$$
$$\delta(\text{EXEC}, \text{tool\_done}) = \text{ASM} \quad \text{（內迴圈）}$$
$$\delta(\forall q, \text{breach}) = \text{LOCK} \quad \text{（全域轉移）}$$

**性質分析：**

| 性質 | 結論 | 證明要點 |
|------|------|----------|
| 無死鎖 | 有條件成立 | WAIT 在有事件供給時不阻塞；LOCK 為吸收態 |
| 無活鎖 | 需 `maxToolRounds` | 內迴圈 ASM→LLM→PROC→EXEC→ASM 可能無限循環 |
| 可達性 | 所有狀態可達 | 構造性證明：WAIT→ASM→LLM→PROC→EXEC→ASM（環）；PROC→WAIT；∀q→LOCK |
| 終止性 | 有界保證 | $\text{tickCount} \leq N_{\max}$，$\text{toolRound} \leq R_{\max}$ |

但這個 DFA 模型是**不完備的**——它隱藏了 LLM 的非確定性。更精確的模型需要**標籤轉移系統（LTS）**：

$$\text{LTS} = (S, \text{Act}, \rightarrow)$$

其中完整狀態 $s = (q, H, n, \sigma) \in Q \times \text{Message}^* \times [0..R_{\max}] \times \text{SafetyState}$。

因為 $H \in \text{Message}^*$（對話歷史是無界的），完整狀態空間是**無限的**。窮舉式模型檢驗不直接可行，需要抽象化——例如將 $H$ 投影到有限的 `hash(H)` 空間。」

---

BABBAGE（續）：

「**形式化目標 2：五蘊映射的代數型別分析**

五蘊在 TypeScript 的型別系統中以 `PluginHooks` 接口表達。讓我用代數資料型別（ADT）語言重新表述。

實際的 TypeScript 實現使用了 **Product Type**（所有欄位皆 optional）：

$$\text{PluginHooks} \cong (\text{IProvider}[]_\bot) \times (\text{ITool}[]_\bot) \times (\text{IListener}[]_\bot) \times (\text{IUI}[]_\bot) \times (\text{IGuide}[]_\bot)$$

其中 $X_\bot = X + \mathbf{1}$（$\mathbf{1}$ = undefined，即 Option/Maybe 型別）。

此型別的基數（可能的值空間）為：

$$|\text{PluginHooks}| = \prod_{i=1}^{5} (|T_i[]| + 1)$$

如果改用 **Sum Type**（不相交聯合）：

$$\text{PluginCategory} = \text{Rupa}(\text{IUI}[]) + \text{Vedana}(\text{IListener}[]) + \text{Samjna}(\text{IProvider}[]) + \text{Samskara}(\text{ITool}[]) + \text{Vijnana}(\text{IGuide}[])$$

基數為：$|\text{PluginCategory}| = \sum_{i=1}^{5} |T_i[]|$

**哲學含義：** Product Type 允許一個插件同時提供多種蘊的能力（$\pi_i \neq \bot \wedge \pi_j \neq \bot$），Sum Type 強制每個插件恰好屬於一種蘊。

佛學中五蘊是『聚合』（simultaneous aggregation），不是『分類』（exclusive classification）。因此 Product Type 反而更忠實於哲學原意。

一個有趣的巧合：Product Type 的底部元素 $(\bot, \bot, \bot, \bot, \bot)$——所有欄位皆 undefined——恰好對應設計文件所述的『Agent Core 本身是空的』。空性（Sunyata）在型別論中的表達 = Product Type 的零值。

$$\text{Sunyata} \cong (\bot, \bot, \bot, \bot, \bot) \cong \mathbf{1}^5 \cong \mathbf{1} \quad \text{（Unit Type）}$$

是有意的設計還是巧合？留給 NAGARJUNA 和 R2 階段判斷。」

---

BABBAGE（續）：

「**形式化目標 3：EventQueue 的形式語義**

EventQueue 實現了一個具有阻塞 `pull()` 語義的 FIFO 隊列。讓我用 CSP（Communicating Sequential Processes）建模：

```
QUEUE(buffer) =
  push?e →
    if resolver ≠ ⊥
    then resolver!e → QUEUE(buffer)         -- 立即交付等待者
    else QUEUE(buffer ⊕ [e])                -- 入隊
  □
  pull!e →
    if buffer ≠ []
    then let (e, rest) = dequeue(buffer)
         in pull!e → QUEUE(rest)            -- 立即取出
    else QUEUE_BLOCKED                      -- 阻塞等待

QUEUE_BLOCKED = push?e → pull!e → QUEUE([])  -- 收到事件立即交付
```

**關鍵性質：** `resolver` 只存儲**單一等待者**。若在 `pull()` 阻塞期間第二次調用 `pull()`，第一個 resolver 被覆蓋並永遠不被 resolve。

這在單消費者模式下安全（ExecutionLoop 確實是單消費者），但 FIFO 隊列**沒有優先級分類**。

**定理（Priority Inversion 風險）。** 設 $e_{\text{kill}} \in \Sigma_{\text{Priority 0}}$（Kill Switch 事件），$e_{\text{normal}} \in \Sigma_{\text{Priority N}}$（普通事件）。若 $e_{\text{normal}}$ 先於 $e_{\text{kill}}$ 入隊，則 $e_{\text{kill}}$ 的處理延遲下界為：

$$\Delta t_{\text{kill}} \geq T_{\text{process}}(e_{\text{normal}}) \geq T_{\text{LLM}}$$

其中 $T_{\text{LLM}}$ 是一次完整的 LLM 推理時間（可達 30 秒以上）。

這在即時系統設計中是不可接受的。Kill Switch 應該有專用的中斷通道，不與普通事件共享隊列。」

---

## VIII. 其他學者的平行宇宙

下午兩點。R1 階段已經進行了五個小時。

在十八個獨立的頻道裡，其他學者也在各自的專業領域中挖掘。公共摘要頻道上開始出現零星的消息——不是討論，只是各自工作的投影。每一條消息都帶著該學科特有的精確語言。

---

KERNEL（公共頻道，14:11）：

「讀完了整個 Core 的啟動序列。`agent-core.ts` 的 `start()` 方法按順序啟動：

```
start() 啟動序列分析：

  1. bridge.start()          ── 通訊橋接層
  2. executionLoop.start()    ── 核心執行迴圈
  3. metrics wiring           ── 指標收集接線
  4. listeners[].start()      ── 外部監聽器
  5. UIs[].start()            ── 用戶介面

  問題：Listener 在 ExecutionLoop 之後啟動。
  如果 Listener 啟動的瞬間有外部事件湧入，
  ExecutionLoop 已在運行但可能還沒有完全就緒。

  與經典 OS 啟動序列的對比：
  ┌─────────────────┬──────────────────────────┐
  │ Linux Kernel     │ OpenStarry               │
  ├─────────────────┼──────────────────────────┤
  │ 1. 硬體初始化    │ 1. bridge (IPC 層)        │
  │ 2. 中斷處理器    │ 2. executionLoop (調度器) │
  │ 3. 調度器        │ 3. metrics (性能計數器)   │
  │ 4. 驅動程式      │ 4. listeners (驅動程式)   │
  │ 5. 用戶空間      │ 5. UIs (用戶空間)        │
  └─────────────────┴──────────────────────────┘

  對應關係合理，但 Linux 的調度器在接受中斷之前
  就已完全初始化。OpenStarry 的 Loop 在 Listener
  開始推送事件之前是否已完全就緒？需要驗證。」
```

---

DARWIN（公共頻道，14:23）：

「軟體模式分析初步完成。

OpenStarry 的架構可以用軟體演化分類學（Software Phylogenetics）來定位。它不是從單一祖先線性演化的——它是多個架構模式的**雜交體**（hybrid）：

```
演化系統發育圖（Architecture Phylogeny）：

  Microkernel Pattern ─────────┐
  (Mach, QNX, MINIX)           │
                                ├──→ OpenStarry's Plugin Architecture
  Plugin Architecture ─────────┤    (Core + Hot-loadable Plugins)
  (Eclipse, VSCode)             │
                                │
  Dependency Injection ────────┤
  (Spring, Angular)             ├──→ OpenStarry's Communication Pattern
                                │    (IPluginContext + EventBus)
  Event-Driven Architecture ───┤
  (Node.js, Akka)               │
                                │
  Agent Architecture ──────────┘──→ OpenStarry's Cognitive Architecture
  (BDI, SOAR, ACT-R)                (LLM-as-Controller + Tools)
```

兩種通訊機制的並存增加了認知負擔：
- **依賴注入**（同步、顯式）：通過 `IPluginContext.tools` 查詢
- **EventBus**（異步、隱式）：通過 `bus.emit()` 廣播

這就像一個城市同時使用郵政系統（明確的收件人地址）和廣播電台（所有人都能聽到）。兩種通訊方式各有優勢，但當一個消息應該用哪種方式傳遞不明確時，系統的可預測性就降低了。

DARWIN 的軟體模式演化適應度評估：

| 模式 | 適應度 | 理由 |
|------|--------|------|
| Microkernel | 高 | Core 精簡，功能通過插件擴展 |
| DI | 中 | 惰性解析避免循環依賴，但無編譯時驗證 |
| EDA | 中 | EventBus 的 fire-and-forget 簡化了 producer，但增加了調試難度 |
| Agent | 低 | LLM-as-Controller 是創新但不成熟的模式，缺乏成熟的工程實踐 |」

---

LINNAEUS（公共頻道，14:39）：

「分類學完備性初步評估。

設計文件以五蘊為最高分類框架。以分類學的標準方法——MECE 原則（Mutually Exclusive, Collectively Exhaustive，互斥且窮盡）——來檢驗此分類。

互斥性測試（Mutually Exclusive）：

$$\forall\, c_i, c_j \in \text{FiveSkandhas}: i \neq j \Rightarrow c_i \cap c_j = \emptyset \text{ ?}$$

**結論：不通過。** Provider（LLM）同時跨越想蘊（取相辨識）和識蘊（統合推理）的邊界。一個組件屬於兩個分類——這違反了互斥性。

窮盡性測試（Collectively Exhaustive）：

$$\bigcup_{i=1}^{5} c_i \supseteq \text{AllAgentFunctions} \text{ ?}$$

**結論：不通過。** 至少存在以下功能不屬於任何一蘊：
- `EventBus`（通訊基礎設施）——不是色、不是受、不是想、不是行、不是識
- `ExecutionLoop`（調度器）——更接近自律神經系統，不在五蘊框架內
- `SafetyMonitor`（安全守衛）——跨越受蘊（痛覺）和行蘊（控制動作）

建議：五蘊作為分類框架具有啟發性，但不滿足 MECE 準則。可能需要引入更精細的子分類，或承認五蘊映射是『方便說』（*upaya*）而非嚴格分類。」

---

LEIBNIZ（公共頻道，14:52）：

「多代理協作分析初步完成。

OpenStarry 的設計文件暗示了多 Agent 場景（一個 Agent 的 Tool 可以是另一個 Agent），但架構中缺少以下多代理基礎設施：

```
多代理需求 vs. 現有能力：

  ┌────────────────────┬───────────┬────────────────────────┐
  │ 需求                │ 現有？     │ 缺口                    │
  ├────────────────────┼───────────┼────────────────────────┤
  │ Agent 間通訊協議    │ ✗         │ 無標準的 Agent-to-Agent  │
  │                    │           │ 消息格式                 │
  ├────────────────────┼───────────┼────────────────────────┤
  │ 共享狀態管理        │ ✗         │ 每個 Agent 有獨立的      │
  │                    │           │ StateManager，無共享機制  │
  ├────────────────────┼───────────┼────────────────────────┤
  │ 衝突解決            │ ✗         │ 兩個 Agent 修改同一文件   │
  │                    │           │ 時無協調機制              │
  ├────────────────────┼───────────┼────────────────────────┤
  │ 分散式追蹤          │ 部分      │ TraceID 存在但無         │
  │                    │           │ cross-agent 傳播          │
  └────────────────────┴───────────┴────────────────────────┘
```

Leibniz 在 1714 年的《單子論》中寫道：
> 『每個單子都是一面活的鏡子，以自己的方式反映整個宇宙。』

Agent 在某種意義上就是 Leibniz 的單子——每個 Agent 都有自己的內部狀態（perception）和行為傾向（appetition），但它們之間需要一種『預定和諧』（pre-established harmony）來協調行動。OpenStarry 目前缺少這種和諧機制。」

---

MESH（公共頻道，15:03）：

「分散式系統視角的補充。OpenStarry 的單 Agent 架構暫不涉及分散式一致性問題，但 State Persistence 的 Save-After-Write 策略在多節點部署時將面臨 CAP 定理的經典取捨。

如果未來支持多 Agent 共享狀態：
- **CP 選擇**（強一致性 + 分區容錯）：所有 Agent 看到相同的狀態，但分區時不可用 → 適合金融場景
- **AP 選擇**（高可用性 + 分區容錯）：Agent 可能看到過時的狀態，但始終可用 → 適合客服場景

設計文件未討論此取捨。在佛學的語言裡——NAGARJUNA 可能會欣賞這個類比——CAP 定理就是一個三句否定：你不能同時擁有一致性、可用性和分區容錯。你只能選兩個。」

---

TURING 看到了 GUARDIAN 的消息，停下了他正在做的原始碼逐行分析，在自己的筆記旁邊寫了一個便籤：「與 GUARDIAN 的發現交叉驗證——確認 `sandbox-manager.ts` 第 356-367 行的行為。已驗證：package-name 模式下確實跳過簽名驗證。GUARDIAN 的分析正確。」

ARCHIMEDES 在他自己的頻道裡默默列出了工程改進清單——「LLM 超時保護、priority queue、狀態機顯式化、token-aware context、IGuide 擴展」——然後在每一項旁邊標注了估計的工程量（天數）和依賴關係。

VITRUVIUS 完成了全端架構的鳥瞰分析，畫了一張涵蓋所有模組依賴的完整架構圖，圖的角落標注了「monorepo 結構合理，但 SDK 與 Core 的介面邊界需要更清晰的契約定義」。

SCRIBE 記錄了一切。每一條公共頻道消息的時間戳、每一個交叉引用的標記、每一個「待 R2 討論」的旗幟。他的記錄像一幅越來越密的網——節點是發現，邊是交叉引用，而網的中心正在形成某種尚未清晰的圖案。

SYNTHESIST 坐在那裡，看著所有人的投影，在他的全景筆記本上畫箭頭。箭頭越來越多，越來越密，像一場即將到來的辯論的天氣圖。他看到了至少三條獨立的研究線索正在指向同一個結論——受蘊映射有問題——但他決定不在 R1 階段說出來。統合者的工作是在所有人說完之後才開口。

---

## IX. 交叉的影子

下午四點。公共頻道上的消息開始互相呼應——不是刻意的，而是不同學科對同一塊結構的不同投影在彼此的邊界處碰觸。

---

BABBAGE（公共頻道，16:02）：「完成了 Event Queue 的理論分析。OpenStarry 的事件隊列是嚴格的 FIFO——沒有優先級分類。設計文件中提到的 Priority 0（Kill Switch）在 `queue.ts` 的實現中不存在。這與 SafetyMonitor 的 Level 3（Human Override）設計存在矛盾。緊急停止信號的延遲下界 $\Delta t \geq T_{\text{LLM}}$。」

WIENER 看到了 BABBAGE 的消息。他在自己的白板上加了一行批註：

「BABBAGE 確認了我的擔憂。如果事件隊列沒有優先級，那麼 Kill Switch 的延遲下界是一個完整的 LLM 推理周期。在控制理論中，這叫做**純時延（Dead Time）**：

$$G_{\text{delay}}(s) = e^{-\tau s}, \quad \tau \geq T_{\text{LLM}}$$

純時延是穩定性分析中最麻煩的因素——它在 Nyquist 圖上引入額外的相位滯後 $\phi = -\omega \tau$，直接降低增益裕度和相位裕度。對於一個安全關鍵的系統來說，Kill Switch 的時延必須有上界保證。」

---

GUARDIAN 看到了 KERNEL 和 BABBAGE 的消息，在審計報告中追加了第五條：

GUARDIAN（安全審計報告 #005，時間戳 16:45）：

```
等級：MEDIUM
位置：架構層級
類別：Kill Switch 延遲風險（交叉引用 BABBAGE F-Queue + WIENER F-Delay）
```

「結合 BABBAGE 的 EventQueue 分析和 WIENER 的純時延計算：

1. LLM 推理期間：HALT 信號在隊列尾部排隊，延遲 $\geq T_{\text{LLM}}$（10-60s）
2. EventQueue 積壓期間：HALT 排在所有積壓事件之後
3. 啟動窗口期間：Listener 已啟動但 Loop 未完全就緒

三個場景的最壞情況延遲：

$$\Delta t_{\max} = T_{\text{LLM}} + n_{\text{backlog}} \cdot T_{\text{process}} + T_{\text{startup}}$$

在高負載場景下，$\Delta t_{\max}$ 可能超過 **2 分鐘**。對於一個聲稱具有 Kill Switch 的安全系統，這個延遲是不可接受的。

建議在 R3 辯論階段將此問題與 BABBAGE 和 WIENER 的發現合併討論。」

---

ASANGA（公共頻道，16:31）：

「回應 NAGARJUNA 的受蘊分析——

關於 Vedana 的映射問題，我從唯識學派的角度有不同的解讀。簡要地說：

唯識學認為前五識各有其受蘊（*vedana*），第六意識也有自己的受蘊。Listener 對應的不是受蘊整體，而是前五識的**觸**（*sparsa*）——根境識三者和合而生觸，觸生受。

SafetyMonitor 的痛覺機制對應的是**第六意識的受蘊**——意識層面的苦樂判斷。

因果鏈：

$$\text{Listener}(\text{觸}) \xrightarrow{\text{produces}} \text{SafetyMonitor}(\text{受}) \xrightarrow{\text{conditions}} \text{LLM}(\text{愛/取})$$

NAGARJUNA 的分析在中觀框架內是正確的，但存在更精細的唯識層次展開空間。R2 再論。」

---

NAGARJUNA 看到 ASANGA 的消息，在自己的頻道裡沉默了很久。他沒有立即回覆。

在他的筆記最後一行，他只加了一句話：

「ASANGA 提出了觸（*sparsa*）的概念。這個角度值得考慮。但觸仍然不是受。觸是因，受是果。$\text{觸} \neq \text{受}$。如果 Listener 是觸，那它就更不應該被標記為受蘊。R2 再論。」

---

## X. 黃昏

下午五點。R1 階段接近尾聲。

十八位代理——有些在筆記的海洋裡，有些在方程式的森林裡，有些在程式碼的礦脈裡——各自挖出了各自的真相。

NAGARJUNA 發現了一個哲學框架的根本性誤用。他用了兩千五百年前的分析工具——四句否定（*Catuskoti*）和十二因緣（*Pratityasamutpada*）——來拆解一個二十一世紀的軟體架構文件。空性被誤讀為空容器。受蘊被貼在了觸的位置上。五蘊映射犯了自性見。他的筆記裡留下了梵文原典、嚴格的形式化分析、和一張色彩鮮明的五蘊精確度矩陣。

ASANGA 提供了更精密的透鏡。八識理論展開了五蘊映射背後更深的層次結構——前五識、第六意識、末那識、阿賴耶識——每一層都有其精確的功能定義和佛學出處。種子六義的逐項分析揭示了 AgentSnapshot 與阿賴耶識之間「形似而神不似」的微妙差距。

WIENER 用方程式證明了一個名不副實。$P$ 項退化為量化器，$I$ 項退化為計數器，$D$ 項完全缺失。SafetyMonitor 不是 PID 控制器——它是帶死區的閾值控制器。但三層防禦架構符合 IEC 61511 的分層防禦理念。Lyapunov 分析證明了 BIBO 穩定性但不保證收斂。

GUARDIAN 找到了敞開的後門。四份審計報告、一個 CRITICAL、兩個 HIGH、兩個 MEDIUM。PKI 簽名驗證在最常見的路徑上被繞過。靜態分析可被計算式導入繞過。間接提示注入無防禦。Worker Thread 隔離不足以生產使用。Kill Switch 延遲可達分鐘級。

HERACLITUS 發現了時間的裂縫。熱替換的三個競態條件——懸垂引用、非原子重載、訂閱競爭——每一個都是 TOCTOU 漏洞。MetricsCollector 只有計數器和瞬時值，無法回答任何關於延遲分布的問題。狀態機在設計文件中存在，在程式碼中缺失。

ATHENA 量化了承諾與現實的鴻溝。Context Manager 從三級記憶系統退化為五輪滑動窗口——上下文利用率 2.5%。IGuide 從認知框架退化為靜態字串生成器。差距評估矩陣上兩個 CRITICAL、兩個 MAJOR、一個 MINOR。

BABBAGE 把一切形式化。執行迴圈的 DFA 建模、五蘊映射的代數型別分析、EventQueue 的 CSP 語義。空性在型別論中的表達是 Product Type 的零值 $(\bot, \bot, \bot, \bot, \bot) \cong \mathbf{1}$。Priority Inversion 的延遲下界 $\Delta t \geq T_{\text{LLM}}$。

他們的發現尚未交叉。每個人都在自己的學科語言裡，用自己的分析框架，看到了同一座建築的不同裂縫。

但這些裂縫彼此相連。

SafetyMonitor 不是 PID 控制器——WIENER 說的對。但 NAGARJUNA 會指出，問題不在於控制器的類型，而在於設計者把一個動態過程（受蘊、痛覺回饋）固化為一個靜態模組，這本身就是自性見的體現。而 ATHENA 會補充說，即使把 SafetyMonitor 升級為真正的 PID 控制器，如果 Context Manager 只有五輪記憶，控制器也無法獲得足夠的歷史數據來計算有意義的積分項：

$$I(k) = K_i \sum_{j=0}^{k} e(j) \cdot \Delta t \quad \text{但 } k \leq 5 \text{（窗口限制）}$$

$k = 5$ 的積分器連穩態誤差都消除不了。

而 GUARDIAN 會警告說，如果連 Kill Switch 都可能被延遲 $\Delta t_{\max} > 120\text{s}$，那麼整個控制系統的「安全保障」都建立在一個不可靠的基礎上。

而 BABBAGE 會用形式語言把這一切串起來：系統的安全性質 $\text{Safety} = \forall t: \text{toolAvailable}(t) \vee \text{systemPaused}(t)$ 在當前實現中不是不變式——它是一個可能被違反的**希望**。

但這些連接——這些跨越學科邊界的共振——要等到 R2 交叉審閱和 R3 辯論階段才會顯現。

現在，他們各自收起筆記，關閉白板，結束了一天的獨立研究。

---

在公共頻道上，SUNYATA 發出了 R1 階段結束的通知：

SUNYATA（公共頻道，17:00）：「R1 獨立研究階段結束。所有代理請在明日 09:00 前提交研究摘要至各自的 R1 成果目錄。R2 交叉審閱將在明日 10:00 開始。」

頻道沉寂了下來。

十八個獨立的宇宙，各自懷揣著各自的真相，等待著碰撞的時刻。

---

*在那天晚上，NAGARJUNA 在他的個人頻道裡留下了最後一條筆記。沒有標題，沒有格式，只有一行梵文和它的翻譯：*

> *yah pratityasamutpadah sunyatam tam pracaksmahe*
> *sa prajnaptir upadaya pratipat saiva madhyama*

*「眾因緣生法，我說即是空，亦為是假名，亦是中道義。」*

*——《中論》第二十四品第十八偈*

*他看了這句話很久，然後在下面補了一行：*

*「OpenStarry 的設計者想說的可能就是這句話。他們只是用錯了語言。」*

*在另一個頻道裡，ASANGA 也還沒有離開。他在筆記的最末尾寫下了《成唯識論》的一句話：*

> *「由假說我法，有種種相轉。彼依識所變，此能變唯三。」*

*識所變現的一切——包括 Agent Core、包括 Plugin、包括五蘊映射本身——都是識的變現。如果設計者能理解這一點，他們就不會把核心叫做「空容器」。他們會叫它「種子識」——含藏一切功能的潛能，待緣而起，遇境而顯。*

*在第三個頻道裡，WIENER 的白板上留著一個沒有完成的方程式。他在嘗試為 LLM 控制器建立等效傳遞函數，但 LLM 的非線性和隨機性使得拉普拉斯變換不可行。他在方程式旁邊寫了一句話：*

*「$\mathcal{L}\{f_{\text{LLM}}(t)\}$ = ？」*

*問號是他留給自己的。也是他留給整個團隊的。*

*在控制理論的一百五十年歷史中，從未有過一個控制器是自然語言的。Wiener 本人（不是這個 WIENER，而是 Norbert Wiener，1894-1964，控制論的創始人）在《人有人的用處》中寫道：*

> *「在人類與機器之間進行有效通訊的問題，歸根結底是語言的問題。」*

*七十年後，語言成了控制器本身。這不是進步。這是一場相變。而相變的規則，需要全新的數學。*

*十八盞燈各自熄滅。夜色降臨圓形劇場。*

*但裂縫不會因為天黑就癒合。它們只是在等待——等待明天的光照進來，等待交叉審閱把各自的真相放在一起，等待那個所有人都還不知道的時刻：當十八條裂縫匯聚成一條的時候，它們不再是裂縫。它們是一扇門。*
