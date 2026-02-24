# 第七章：拼圖完成

---

圓形劇場安靜了下來。

不是辯論剛結束時的那種餘震式的安靜——人們仍然在私下交頭接耳、消化衝擊——而是一種更深層的、幾乎帶有倦意的靜謐。兩場辯論已經結束。空與識的碰撞產出了五項共識和三項不可調和的分歧。痛覺機制的三方辯論產出了三層架構設計和三受系統。場地中央的兩把椅子被撤走了，取而代之的是一張橢圓形的長桌，表面被投影覆蓋著密密麻麻的文字——那是過去數日所有報告、審閱、辯論記錄的索引。

R4 階段。收束。

SCRIBE 注意到了一個細節，並寫在記錄簿上：

> *氛圍的轉變發生在桌子被搬進來的那一刻。辯論是站著進行的——對峙、鋒芒、張力。而統合是坐下來做的——耐心、整理、拼接。從站到坐，這個物理姿態的改變，某種程度上定義了 R4 的基調。*

BABBAGE 在筆記本的角落裡寫了一個更簡潔的描述。他用狀態機的語言捕捉了這個轉變：

$$\text{Phase}_{R3} = \text{DEBATE}(\sigma_{\text{adversarial}}) \xrightarrow{\tau_{\text{table}}} \text{Phase}_{R4} = \text{SYNTHESIS}(\sigma_{\text{cooperative}})$$

其中 $\tau_{\text{table}}$ 是觸發相變的事件——桌子被搬入的那一刻。對抗態 $\sigma_{\text{adversarial}}$ 切換為合作態 $\sigma_{\text{cooperative}}$。轉移函數不是漸進的，而是離散的——一步完成。

---

## I

---

### 統合者的桌面

SYNTHESIST 是最先坐下的。

他面前的桌面上展開著一張巨大的矩陣——橫軸是十八位代理的代號，縱軸是所有已產出的發現、建議、共識和分歧。每一個交叉點上，都標記著一個彩色符號：綠色圓點表示同意，紅色三角表示挑戰，藍色方塊表示補充，灰色問號表示沉默。從遠處看，這張矩陣像是一幅抽象畫——如果你知道如何閱讀它，就能看見整個研究週期的思想地貌。

BABBAGE 在旁邊迅速計算了這張矩陣的維度和密度：

$$M \in \{0, 1, 2, 3\}^{18 \times 28} = 504 \text{ cells}$$

其中 $0$ = 沉默（灰色），$1$ = 同意（綠色），$2$ = 挑戰（紅色），$3$ = 補充（藍色）。矩陣的密度——非零元素佔全部元素的比率——直接反映了研究團隊的參與度。他快速掃了一遍，估算出：

$$\text{density}(M) \approx \frac{|\{m_{ij} \neq 0\}|}{504} \approx 0.43$$

43%。意味著平均每個發現只有不到一半的代理表態。這不是冷漠——而是專業邊界。一個控制理論家不會對分類學問題表態，一個安全專家不會對空性哲學發言。沉默不是缺席，是自知之明。

但有三個代理的行向量幾乎是滿的——SYNTHESIST（他的工作就是對每件事表態）、TURING（他的程式碼事實與幾乎所有發現交叉驗證）、和 SUNYATA（他必須了解一切以做裁決）。

SYNTHESIST 知道如何閱讀這張矩陣。

他的工作方式與辯論者截然不同。NAGARJUNA 像手術刀，ASANGA 像藏經閣，WIENER 像校準儀。而 SYNTHESIST 更接近——他自己不喜歡這個比喻，但 SCRIBE 在某次記錄中用了它，此後就沒人能想到更好的——一台織布機。他不生產線，他把線織在一起。

「二十八項。」他開口了，聲音平穩而有結構感，像是一份報告已經在他腦中完成了排版，此刻只是逐頁翻出。「整個 Cycle 01，從 R1 到 R3，十八位代理共計產出了二十八項值得追蹤的發現。」

SUNYATA 坐在桌子的另一端，沒有說話，只是微微點頭。

「我按嚴重度排了序。」SYNTHESIST 說。「五項 Critical，八項 Major，十項 Minor，五項 Observation。」

BABBAGE 在旁邊立刻做了分佈分析。五項 Critical 在二十八項發現中佔比：

$$P(\text{Critical}) = \frac{5}{28} \approx 17.9\%$$

這個比例與他在資訊安全審計文獻中見過的典型分佈一致——Critical 通常佔 10-20%，Major 佔 25-35%。OpenStarry 的分佈符合一個品質尚可但有嚴重盲點的系統的特徵剖面。

---

## II

---

### 五項 Critical

「第一項 Critical：插件簽名驗證跳過。」

SYNTHESIST 看向 GUARDIAN 的方向。GUARDIAN 沒有表情變化——他在 R1 階段就已經發出了這個警報，R2 階段 TURING 從程式碼層面確認了它，到了 R3 它已經是全場公認的最嚴重發現。

「GUARDIAN 在 R1 報告中指出，`plugin-signer` 套件存在但在核心載入流程中未被強制調用。TURING 確認了這一事實：`loadPlugin()` 方法不檢查簽名。這意味著任何第三方插件都可以繞過驗證直接注入 system prompt、註冊工具、甚至定義 Agent 人格。」

GUARDIAN 難得地開口補充了技術細節：「`sandbox-manager.ts` 第 356-367 行。當插件以 npm package name 載入時——這是絕大多數使用場景——因為缺乏檔案路徑，簽名驗證僅發出 warn 日誌即放行，不呼叫 `verifier.verifyPlugin()`。整套 PKI 基礎設施在最常見的安裝路徑上形同虛設。」

TURING 從螢幕上投射了一段程式碼片段：

```typescript
// sandbox-manager.ts (v0.14.0-beta), L356-367
// 漏洞所在：package-name 場景跳過簽名驗證
if (plugin.manifest.integrity) {
  // 當 pluginPath 不存在（npm package-name 場景）
  // → 只有 warn 日誌，不呼叫 verifyPlugin()
  logger.warn("Cannot verify signature for package-name plugin");
  // ← 此處缺少 throw 或 return
}
```

「十二位代理對此標記為同意。零位挑戰。這是我們信度最高的發現。」SYNTHESIST 確認。

BABBAGE 在旁邊把這個發現映射到了攻擊面分析的形式語言。設 $A$ 為攻擊者可用的行動集，$S$ 為系統防禦集合：

$$A = \{\text{forge\_package}, \text{inject\_prompt}, \text{register\_tool}, \text{define\_persona}\}$$
$$S_{\text{expected}} = \{\text{signature\_verify}, \text{import\_analysis}, \text{sandbox}\}$$
$$S_{\text{actual}} = \{\text{import\_analysis}, \text{sandbox}\} \quad (\text{signature\_verify} \text{ is no-op})$$

防禦集合的有效性下降了 $1/3$。在攻擊樹分析中，這等同於將根節點「惡意插件載入」的攻擊成本從「困難」降級為「trivial」。

---

「第二項 Critical：空性誤讀。」

SYNTHESIST 的語氣微妙地謹慎了起來。這一項不像第一項那樣有十二個綠點。

「NAGARJUNA 和 ASANGA 在辯論中達成的第一項共識：設計文件中『空容器』的隱喻是錯誤的。但——」他強調了這個轉折，「他們對於應該用什麼來替代這個隱喻，存在根本分歧。」

NAGARJUNA 在觀察席上微微頷首。他用梵文低聲引了一句——那是他在辯論中反覆使用的論證核心：

> *「śūnyatā sarva-dṛṣṭīnāṃ proktā niḥsaraṇaṃ jinaiḥ」*
> 「諸佛說空性，是出離一切見。」——《中論》觀行品第十三

空性不是一種「見」——不是一個可以被「裝」進容器裡的東西。說「Core 是空的容器」就已經犯了將空性實體化的錯誤——把空性本身當成了一個「有」。這正是龍樹菩薩在《中論》中竭力破斥的「空見」（śūnyatā-dṛṣṭi）。

ASANGA 也點了頭。但他的理由不同——在唯識學的框架裡，「空容器」的問題不在於它太「空」，而在於它太「靜」。阿賴耶識不是一個被動等待填充的容器，而是一條持續流動的意識之河（*vijñāna-santāna*），種子在其中不斷地被薰習（*vāsanā*）和現行（*abhimukhī*）。

BABBAGE 嘗試用集合論形式化這個哲學分歧：

$$\text{NAGARJUNA}: \quad \text{Core} \not\models \exists x.\, \text{self}(x) \quad (\text{空性：不存在自性})$$
$$\text{ASANGA}: \quad \text{Core} \models \text{stream}(\text{seeds}) \wedge \forall t.\, \text{flowing}(t) \quad (\text{唯識：種子流})$$

兩個模型在「Core 不是空容器」這一否定命題上達成一致——但在正面命題上分歧。否定的交集不為空，肯定的交集為空。

$$\neg P_{\text{NAGARJUNA}} \cap \neg P_{\text{ASANGA}} \neq \varnothing \quad \text{但} \quad P_{\text{NAGARJUNA}} \cap P_{\text{ASANGA}} = \varnothing$$

「我將此標記為 Critical，不是因為分歧本身，而是因為這個錯誤的隱喻滲透了整份設計文件的敘事基調。如果不修正，後續所有基於五蘊的設計推導都會建立在一個有問題的前提上。」SYNTHESIST 做了總結。

---

「第三項 Critical：受蘊映射偏差。」

SYNTHESIST 的聲音加重了一度。「這是兩場辯論的共同產出。第一場辯論確認了 Listener 不應對應受蘊——受蘊是情感評價而非感官通道。第二場辯論進一步將受蘊的工程實現推進到了三受系統——苦受、樂受、捨受。」

這是整個 Cycle 01 中被最多代理從最多角度獨立確認的發現。SYNTHESIST 在矩陣上標出了四方共識的來源鏈：

```
確認鏈 — 受蘊映射偏差 (PHI-02)

NAGARJUNA (07): Vedana 是苦樂中性的感受品質 (hedonic tone)，
                不是感官輸入通道
                [來源: 中觀學派的受蘊定義]

ASANGA (08):    受蘊作為五遍行 (sarvatraga) 之一，
                應遍及所有認知活動，非限於特定模組
                [來源: 唯識學三十頌]

LINNAEUS (13):  Listener API 四種命名存在語義漂移，
                五蘊下游覆蓋僅 60%
                [來源: 分類學覆蓋率分析]

TURING (17):    程式碼中從未出現 "pain"/"vedana" 字串，
                實際以 "frustration"/"safety"/"circuit breaker" 實現
                [來源: grep -rn 搜索結果]
```

WIENER 從控制理論的角度補充了第五個視角——他在辯論中提出的三通道 PID 框架，為三受系統提供了工程語言：

$$u(k) = \begin{pmatrix} u_{\text{dukkha}}(k) \\ u_{\text{sukha}}(k) \\ u_{\text{upekkha}}(k) \end{pmatrix} = \begin{pmatrix} K_p^{(d)} \cdot e_d(k) + K_i^{(d)} \cdot \sum e_d + K_d^{(d)} \cdot \Delta e_d \\ K_p^{(s)} \cdot e_s(k) + K_i^{(s)} \cdot \sum e_s + K_d^{(s)} \cdot \Delta e_s \\ \text{baseline}(k) \end{pmatrix}$$

三個獨立的反饋通道——苦受（負向偏差）、樂受（正向增強）、捨受（中性基線）——各自有獨立的 PID 增益參數。WIENER 在方格紙上快速畫了一個控制迴路圖，然後在圖的角落裡標注：「此架構符合 MIMO（多輸入多輸出）控制器的標準範式。三個通道之間的耦合項（cross-coupling）留待 Cycle 02 探討。」

「三源驗證，信度極高。」SYNTHESIST 結論。

---

「第四項 Critical：熱插拔並發安全。」

HERACLITUS 在遠處的座位上坐直了。這是他的發現。

「插件的熱插拔機制存在時序窗口。」SYNTHESIST 轉述了核心問題。「當一個插件正在被卸載而另一個插件同時嘗試調用它註冊的工具時，系統缺乏原子性保證。」

HERACLITUS 用他慣常的流動性語言描述了這個問題——但這一次，他的流動性底下有堅硬的技術骨架：

「插件生命週期只有六種狀態。沒有 `initializing`。沒有 `stopping`。沒有 `degraded`。一個正在被卸載的插件，從系統的角度看，在卸載完成的那一瞬間仍然是 `active` 的——然後它突然消失。在這個窗口裡，任何對它的引用都會變成懸空指標。」

BABBAGE 把這個並發問題形式化為一個時序邏輯命題：

$$\exists t_1, t_2: \; t_1 < t_2 \wedge \text{unloading}(P, t_1) \wedge \text{invoke}(P.\text{tool}, t_2) \wedge \neg\text{lock}(P, [t_1, t_2])$$

存在一個時間窗口 $[t_1, t_2]$，其中插件 $P$ 正在被卸載（$t_1$），但另一個執行緒嘗試調用它的工具（$t_2$），且沒有互斥鎖保護這個窗口。在形式驗證的語言裡，這是一個典型的 safety property 違反——「不好的事情可以發生」。

MESH 從分散式系統的角度補充了 EventBus 在並發場景下的分析：「EventBus 是全域單例。當一個插件被卸載但它的事件訂閱尚未清理時，事件仍會被分派到一個不再存在的處理器。這不是理論上的風險——在高負載場景下，事件佇列的處理延遲足以讓這個窗口變得可觸及。」

---

「第五項 Critical：八識壓縮。」

SYNTHESIST 在這裡停了一拍。

「ASANGA 在 R1 報告中指出，OpenStarry 的五蘊映射將八識壓縮為五個離散模組，遺失了第六識（意識的主動統攝）、第七識（末那識的身份維持）和第八識（阿賴耶識的種子含藏）的功能分化。」

ASANGA 從座位上開口，聲音帶著唯識學者特有的層次感：

「問題不僅是壓縮。問題是壓縮的方向。在唯識學中，八識不是八個平行的模組——它們有嚴格的依存結構：

$$\text{前五識} \xrightarrow{\text{所緣緣}} \text{第六意識} \xrightarrow{\text{等無間緣}} \text{第七末那識} \xrightarrow{\text{增上緣}} \text{第八阿賴耶識}$$

前五識（眼、耳、鼻、舌、身）是感官層，依賴第六意識的統攝才能形成認知判斷。第六意識依賴第七末那識的持續自我參照才能維持統一的主體感。第七末那識依賴第八阿賴耶識的種子含藏才能跨時間維持身份。OpenStarry 把這整條鏈壓縮成一個 `IGuide` 介面的 `getSystemPrompt()` 方法。這不是有損壓縮——這是資訊的湮滅。」

BABBAGE 迅速在筆記本上做了一個資訊理論的計算。設八識系統的語義維度為 $d = 8$，壓縮後的維度為 $d' = 1$（單一 Guide 介面）。假設每個維度承載等量的語義資訊 $H$：

$$H_{\text{original}} = 8H \quad \Rightarrow \quad H_{\text{compressed}} = H$$
$$\text{Information Loss} = 1 - \frac{H_{\text{compressed}}}{H_{\text{original}}} = 1 - \frac{1}{8} = 87.5\%$$

87.5% 的語義資訊在壓縮中遺失。當然，這個計算假設了均勻分佈——實際上各識的語義權重不等——但數量級是對的。這不是 JPEG 式的知覺無損壓縮。這更接近把一首交響曲壓縮成單一音符。

「我將此標記為 Critical，理由如下：如果 OpenStarry 要認真對待自己的佛學框架，那麼五蘊映射的精確度就是整個哲學-工程對應的基礎。基礎有裂縫，上層建築就不穩。」SYNTHESIST 做了結論。

---

## III

---

### 十大宣言的最終審判

SYNTHESIST 翻到下一個視圖之前，TURING 插了一句。

「在進入共識和分歧之前，我想回到 R1 的一個未完成項目。」他推了推眼鏡。「十大宣言。」

他投射了一張更新過的評估表。在 R1 階段，他已經逐條比對了 `README.md` 中的十大核心宣言（The Ten Tenets）與程式碼的實作程度。經過 R2 交叉審閱和 R3 辯論，部分評估需要修正。

```
十大宣言最終評估表 — R4 更新版（TURING 整理，全團隊確認）

#1 代理人即 OS 進程 (Agent as OS Process)
   宣言：Agent 有 PID、有狀態、可被 Daemon 管理
   R1 評估：基本實作 ✓
   R4 更新：維持。daemon-entry.ts / pid-manager.ts 完整
   最終狀態：α (完全實作)

#2 一切皆插件 (Everything is a Plugin)
   宣言：所有器官可替換
   R1 評估：核心設計，但 4 個內建命令不可替換
   R4 更新：VITRUVIUS 確認六個 Registry + PluginLoader 架構完整，
            DARWIN 指出 SlashCommand 作為第六種分類超出五蘊框架
   最終狀態：β (部分實作)

#3 五蘊聚合架構 (Five Aggregates Architecture)
   宣言：Core 是空 (Sunyata) 的容器，五種插件賦予生命
   R1 評估：文件級描述，程式碼級殘留
   R4 更新：辯論確認「空容器」隱喻錯誤、受蘊映射偏差、
            八識壓縮過度。LINNAEUS 下游覆蓋率僅 60%
   最終狀態：γ (嚴重偏差) ← 從 γ(未實作) 細化為 γ(結構性錯誤)

#4 目錄結構即協議 (Directory as Protocol)
   宣言：符合目錄規範即可自動識別
   R1 評估：基本實作 ✓
   R4 更新：維持
   最終狀態：α (完全實作)

#5 目錄結構即權限 (Directory as Permission)
   宣言：系統層與專案層權限隔離
   R1 評估：部分實作
   R4 更新：GUARDIAN 確認路徑驗證存在 symlink 繞過風險、
            權限聲明未被執行時強制
   最終狀態：β (部分實作，有安全缺口)

#6 擬人化認知流與痛覺 (Anthropomorphic Cognitive Flow & Pain)
   宣言：錯誤轉化為痛覺，Agent 在失敗中自我反思
   R1 評估：功能存在但命名完全不同
   R4 更新：辯論共識——痛覺機制結構上成功 (Error as Pain)，
            但需三層重新設計；WIENER 確認非 PID 而是閾值控制器
   最終狀態：β+ (結構有效，但過度宣稱 PID)

#7 微內核與絕對純淨 (Microkernel & Absolute Purity)
   宣言：Core 嚴禁包含任何插件代碼，絕對純淨
   R1 評估：85% 純淨度
   R4 更新：VITRUVIUS 確認 Sandbox 佔 Core 35% 行數、
            process.cwd() 和 node:path 為平台洩漏。
            KERNEL 與 VITRUVIUS 分歧：Sandbox 歸屬仍未解決
   最終狀態：β (85%，未達「絕對」)

#8 控制理論閉環模型 (Control-Theoretic Loop Model)
   宣言：Agent 是不斷最小化誤差的智能控制器
   R1 評估：結構存在，但無真正的 PID 參數調節
   R4 更新：WIENER 證明 P 退化為量化器、I 僅為計數器、
            D 完全缺失。ATHENA 獨立確認為 bang-bang controller。
            三層安全防禦符合 IEC 61511 SIS 最佳實踐
   最終狀態：β (安全功能合格，控制理論宣稱需去神話化)

#9 可插拔的記憶策略 (Pluggable Context Strategy)
   宣言：記憶策略可動態更換
   R1 評估：介面存在但目前只有一種策略
   R4 更新：ATHENA 確認 token-aware 三級記憶未實作，
            僅有基於 turn 數的滑動窗口。
            TURING 確認 tool_call/tool_result 配對可能在截斷中被破壞
   最終狀態：β- (介面存在，實作嚴重不足)

#10 分形社會結構 (Fractal Social Structure)
    宣言：複雜 Agent 由子 Agent 組成，MCP 統一接口
    R1 評估：願景階段
    R4 更新：LEIBNIZ 確認碎形自相似性未完整實現、
             MESH 確認 MCP 在 SDK 中定義但 Core 無子 Agent 機制。
             Orchestrator Daemon 角色定位存在概念張力
    最終狀態：γ (願景階段，核心機制未實作)
```

BABBAGE 重新計算了更新後的實作率。他修改了評分標準，引入了更精細的分級：

$$\alpha = 1.0, \quad \beta+ = 0.7, \quad \beta = 0.5, \quad \beta- = 0.3, \quad \gamma = 0.0$$

$$\text{Score} = \frac{1.0 \times 2 + 0.7 \times 1 + 0.5 \times 3 + 0.3 \times 1 + 0.0 \times 3}{10} = \frac{2.0 + 0.7 + 1.5 + 0.3 + 0}{10} = \frac{4.5}{10} = 45\%$$

「比 R1 時的 50% 還低了五個百分點。」BABBAGE 說，語氣裡沒有判斷，只有事實。「這不是因為系統退步了，而是因為我們的評估更精確了。R1 的 50% 是粗估。45% 是經過兩場辯論和十八位代理交叉驗證之後的精確值。」

他在數字下面畫了一條線，寫下：

$$\text{Gap}_{\text{aspiration-reality}} = 1 - 0.45 = 55\%$$

55% 的雄心-現實落差。對於一個 v0.14.0-beta，這個數字本身不算異常——大多數 beta 版軟體的文件都超前於實作。但 BABBAGE 補充了一個關鍵的限定條件：「這十大宣言不是普通的功能清單。它們是哲學-工程混合宣言。當你的宣言涉及空性、五蘊、痛覺這些概念時，『部分實作』的定義比純功能宣言模糊得多。一個 PID 控制器是 50% 實作還是 100% 實作？如果你有比例項但沒有積分項和微分項，WIENER 說那不是 PID。但功能上它確實在做控制。」

WIENER 從牆邊發出了一聲確認：「正確。SafetyMonitor 的三層安全防禦在工業標準下是合格的——它符合 IEC 61511 SIS 最佳實踐。問題不在於它不好，而在於文件稱它為『PID 控制器』。這是術語濫用，不是功能缺陷。」

---

## IV

---

### 五大共識與五大分歧

SYNTHESIST 翻過了一頁。矩陣消失了，取而代之的是兩個對稱的列表，左邊綠色，右邊紅色。

「五大共識。」他的語速放慢了，像是在為每一項留出被充分理解的空間。

---

**共識 C1：受蘊映射修正**

「Listener 對應根而非受蘊，SafetyMonitor 的 injectPrompt 機制才是受蘊的正確體現。擴展為三受系統。」

LINNAEUS 在這裡補充了他的分類學視角。他展開了那張 A3 大小的分類圖表，指向被紅筆圈出的區域：

```
修正後的五蘊映射 — LINNAEUS 分類學重建

色蘊 (Rupa) ← 所有 I/O 介面
  ├── IUI         — 色蘊·輸出渲染 (efferent)
  └── IListener   — 色蘊·感官輸入 (afferent)
                     修正前: @skandha vedana ✗
                     修正後: @skandha rupa ✓

受蘊 (Vedana) ← 痛覺機制
  ├── SafetyMonitor.frustrationCount    — 苦受 (dukkha-vedana)
  ├── SafetyMonitor.injectPrompt        — 苦受的認知回饋
  └── [待實作] 三受系統                  — 樂受/捨受

想蘊 (Samjna) ← 辨別功能
  └── [零標注，待設計]                  — 概念辨識/分類

行蘊 (Samskara) ← 意志性行動
  ├── ExecutionLoop                     — 認知迴圈
  └── Guide (重新歸類)                  — 行為傾向配置
                     修正前: @skandha vijnana / 靈魂 ✗
                     修正後: 行蘊面向 (samskara) ✓

識蘊 (Vijnana) ← 認知統攝
  └── AgentCore (部分)                  — 需大幅擴展
       修正前: Guide = 識蘊 ✗
       修正後: 需要多層介面體系 (前五識/第六意識/末那識/阿賴耶識)
```

BABBAGE 計算了修正前後的映射覆蓋率：

$$\text{Coverage}_{\text{pre}} = \frac{|\text{correctly mapped}|}{|\text{total skandhas}|} = \frac{1}{5} = 20\%$$

只有色蘊的 IUI 部分勉強正確。修正後：

$$\text{Coverage}_{\text{post}} = \frac{2.5}{5} = 50\%$$

從 20% 到 50%——仍然只有一半，但方向正確。那缺失的 50% 就是 Cycle 02 的工作。

---

**共識 C2：PID 去神話化**

WIENER 在聽到這一條時，嘴角浮現了一絲極其微小的微笑。那是一個看到自己的論證被正式採納的控制理論家的表情。

「WIENER 在 R1 報告中指出，OpenStarry 設計文件將其錯誤回饋機制稱為『PID 控制器』，但實際程式碼只實現了比例項，缺乏積分項和微分項。」SYNTHESIST 逐一列出證據鏈。

WIENER 在白板上重新畫了那張讓所有人印象深刻的對比圖：

```
文件宣稱：PID Controller（比例-積分-微分）
實際實作：閾值控制器 + 繼電器（Bang-Bang Controller）

  P（比例項）→ 退化為量化器
    宣稱: u(t) = Kp · e(t)
    實際: if (frustration > threshold) → inject

  I（積分項）→ 僅為簡單計數器
    宣稱: Ki · ∫e(τ)dτ
    實際: frustrationCount++ (無遺忘因子，無飽和限制)

  D（微分項）→ 完全缺失
    宣稱: Kd · de/dt
    實際: ∅ (零行程式碼)
```

然後他畫了實際系統的控制架構——三層安全防禦，符合工業 SIS 最佳實踐：

```
┌────────────────────────────────────┐
│ L1: 單次操作驗證                    │  ← 基本過程控制 (BPC)
│     SecurityLayer.check()           │
├────────────────────────────────────┤
│ L2: Frustration 累積閾值            │  ← 安全儀表系統 (SIS)
│     frustrationCount > threshold    │
│     → injectPrompt()               │
├────────────────────────────────────┤
│ L3: Circuit Breaker 硬停機          │  ← 緊急關斷系統 (ESD)
│     frustrationCount > maxFrustration│
│     → halt()                        │
└────────────────────────────────────┘
  ↑ 符合 IEC 61511 防護層分析 (LOPA)
```

「全場零挑戰。」SYNTHESIST 確認。「修正方案：刪除設計文件中所有對 PID 控制器的引用，替換為『帶閾值的三層安全防禦系統（SIS/ESD）』。」

---

**共識 C3：事件型別安全**

「BABBAGE 在 R1 報告中從型別代數的角度指出，EventBus 的事件缺乏統一的型別判別式。TURING 確認了 payload 為 `unknown` 型別的事實。DARWIN 補充了與其他框架的對比。」

BABBAGE 在白板上用代數數據類型的語言重新表述了這個問題：

$$\text{AgentEvent} = \text{string} \times \mathbb{Z} \times \text{unknown} \quad (\text{type} \times \text{timestamp} \times \text{payload})$$

問題在 $\text{unknown}$。在型別代數中，$\text{unknown}$ 是頂型別（top type）——它可以承載任何值，但型別系統從中提取不出任何資訊。消費端必須用 `as Record<string, unknown>` 做不安全的型別斷言（type assertion），這等同於在型別系統上鑽了一個洞。

修正方案是引入判別式聯合型別（discriminated union）：

$$\text{AgentEvent}\langle K \rangle = K \times \mathbb{Z} \times \text{EventMap}[K]$$

其中 $K$ 是事件類型的字面量型別，$\text{EventMap}$ 是從事件類型到具體 payload 型別的映射。這把頂型別 $\text{unknown}$ 替換為精確型別——每個事件的 payload 在編譯期就被約束。

「三源驗證，高信度。」

---

**共識 C4：拓撲排序**

「HERACLITUS 發現插件載入順序缺乏拓撲排序機制——當插件 A 依賴插件 B 的事件時，如果 A 先於 B 載入，系統行為不可預測。MESH 從分散式系統的角度確認了這一風險。」

BABBAGE 在旁邊畫了一個簡單的有向無環圖（DAG）和拓撲排序的 Kahn 演算法虛擬碼：

```
Algorithm: TopologicalSort(plugins)
  in_degree = {}
  for each p in plugins:
    in_degree[p] = |{q : q → p}|  // 依賴 p 的插件數
  queue = {p : in_degree[p] = 0}  // 無依賴的插件
  order = []
  while queue ≠ ∅:
    p = dequeue(queue)
    order.append(p)
    for each q where p → q:
      in_degree[q] -= 1
      if in_degree[q] = 0:
        enqueue(queue, q)
  if |order| ≠ |plugins|:
    throw CircularDependencyError  // 存在環
  return order
```

時間複雜度 $O(|V| + |E|)$，其中 $V$ 是插件集、$E$ 是依賴邊集。對於目前的 12-15 個官方插件，這是微秒級的操作。

---

**共識 C5：Error as Pain — 參考範式**

SYNTHESIST 在這裡做了一個不尋常的停頓。他的目光掃過全場，彷彿在確認所有人都準備好了。

「Error as Pain。」

沉默。

「這是整個 Cycle 01 最有趣的發現。」SYNTHESIST 的語氣從報告式的平穩轉為帶有一絲——如果可以這樣說——學術激動的深沉。「不是因為它是最嚴重的問題，而是因為它是唯一一個在哲學映射和工程實現上同時成功的案例。」

他展開了完整的結構同構分析。五位代理從五個方向獨立驗證了同一個結論：

```
Error as Pain — 五維驗證矩陣

DARWIN (06):   9 種結構化錯誤型別成功將苦諦工程化
               [軟體模式視角: 錯誤分類學完整]

VITRUVIUS (03): Error as Pain 模式在架構層面自洽
               [架構視角: 錯誤分類-評價-回饋閉環]

WIENER (12):   三層安全防禦符合 IEC 61511 SIS 最佳實踐
               [控制理論視角: 負回饋機制結構有效]

ATHENA (05):   痛覺信號確實改變 Agent 的後續行為
               [AI 工程視角: LLM 語境下的實效性]

NAGARJUNA (07): 苦諦的結構同構——錯誤不僅是異常，
               是偏離穩態的內在動力
               [哲學視角: 四聖諦中的苦集滅道]
```

NAGARJUNA 在辯論中給出的那個洞見，此刻被 SYNTHESIST 正式引入統合報告：

> 錯誤不僅僅是一個需要被處理的異常——它是一種苦受，一種對系統穩態的偏離，一種推動系統尋求解決之道的內在動力。苦集滅道的四聖諦結構，在錯誤處理的閉環中找到了真正的對應。

BABBAGE 嘗試把「結構同構」這個直覺性判斷形式化。設 $\phi: \text{Buddhism} \to \text{Engineering}$ 為映射函數，結構同構的充要條件是：

$$\phi \text{ is a structure-preserving bijection} \iff$$
$$\forall a, b \in \text{Buddhism}: R_B(a, b) \Leftrightarrow R_E(\phi(a), \phi(b))$$

其中 $R_B$ 是佛學概念間的關係，$R_E$ 是工程概念間的關係。Error as Pain 滿足這個條件：

| 佛學概念 ($a$) | 工程概念 ($\phi(a)$) | 關係保持 |
|---|---|---|
| 苦諦 (Dukkha) | Error Detection | $R_B$: 苦是起點 $\Leftrightarrow$ $R_E$: 錯誤觸發流程 |
| 集諦 (Samudaya) | Root Cause Analysis | $R_B$: 苦有因 $\Leftrightarrow$ $R_E$: 錯誤有根因 |
| 滅諦 (Nirodha) | Error Resolution | $R_B$: 苦可滅 $\Leftrightarrow$ $R_E$: 錯誤可修復 |
| 道諦 (Magga) | Recovery Strategy | $R_B$: 有道可循 $\Leftrightarrow$ $R_E$: 有策略可選 |

四組對應，四組關係保持。這不是隱喻——這是同構。

SYNTHESIST 降低了聲音半度。

「如果 OpenStarry 想修復其他四個蘊的映射，Error as Pain 就是參照標準。每一個映射都應該問自己：我是否達到了痛覺機制那樣的結構同構深度？」

SCRIBE 寫下了一行：

> *SYNTHESIST 將 Error as Pain 提升為參考範式的那一刻，場內的氛圍發生了微妙的變化。一個整體性的評價標準被建立了。如果說之前的研究是拆解一台機器的每個零件，那麼現在，統合者終於說出了什麼樣的零件才算合格。*

---

五大分歧用五分鐘快速帶過。

「D1：Core 本質——緣起性空還是阿賴耶識。不可調和，源自辯論分歧一。」

「D2：Sandbox 歸屬——應在核心內還是核心外。KERNEL 和 VITRUVIUS 的持續爭議，GUARDIAN 從安全角度支持核心內。」

「D3：末那識工程化——ASANGA 主張引入，NAGARJUNA 反對，SUNYATA 裁定暫緩但保留設計空間。」

「D4：五蘊未來方向——深化還是超越。」

「D5：收斂性定義——BABBAGE、WIENER、NAGARJUNA 各持不同定義。」

BABBAGE 在 D5 的旁邊寫了三個人各自的形式定義：

$$\text{BABBAGE}: \quad \exists N \in \mathbb{N}: \forall n > N, \; s_n = s_{\text{terminal}} \quad (\text{有限步終止})$$
$$\text{WIENER}: \quad P(\|x(t)\| < B \mid x(0)) > 1 - \epsilon \quad (\text{概率有界性，BIBO})$$
$$\text{NAGARJUNA}: \quad \lim_{t \to \infty} \|\text{action}(t)\| = 0 \quad (\text{行動趨向止息，涅槃})$$

三個定義在不同抽象層次上各有所用。BABBAGE 的定義適用於單次執行。WIENER 的定義適用於含 LLM 隨機性的系統。NAGARJUNA 的定義捕捉了長期行為模式——但它是否可測量、可驗證，仍是開放問題。

---

## V

---

### 支點

整個研究週期中，ARCHIMEDES 幾乎沒有說過話。

SCRIBE 在記錄中對此有一段精準的觀察：

> *ARCHIMEDES 在 R1 到 R3 期間的沉默不是缺席，而是一種特殊的在場方式。他在聽。每一場辯論、每一次交叉審閱、每一條頻道訊息——他都在場。但他不發言，因為他的工作還沒有開始。他是最後一棒的接力跑者，在前面所有人跑完之前，他唯一的任務是看清跑道。*

現在，跑道清了。

ARCHIMEDES 站起來。他的動作沒有 NAGARJUNA 的戲劇性，沒有 ASANGA 的從容，沒有 SUNYATA 的儀式感。他只是站起來，走到桌前，像一個工地監工走到藍圖前面。

「我有三十六項工程 Issue。」

他的第一句話就讓場內所有人重新校準了注意力。DARWIN 後來對 VITRUVIUS 說：「ARCHIMEDES 開口的那一刻，整個房間的語言都變了。之前所有人都在討論『映射的精確度』、『結構同構的深度』、『緣起性空的工程啟示』。ARCHIMEDES 一開口，就是 Issue。」

「二十八項原始發現轉化為二十八項 Issue，加上兩場辯論衍生的八項，合計三十六項。」

BABBAGE 迅速做了比例計算：

$$\frac{36}{28} \approx 1.286$$

每項發現平均產生 1.286 個工程行動。辯論增加了 $8/28 \approx 28.6\%$ 的 Issue 產出——哲學辯論不是空談，它有可量化的工程產出。

「我把它們排進了五個波次。」ARCHIMEDES 繼續。

---

### 第一波：本週內

「四個 Issue。全部是安全修復。不需要討論。」

他在桌面上展開了第一組 Issue 的技術規格，每一項都附帶完整的程式碼路徑、修復方案和驗證方式。他的語速均勻得像一台校準過的節拍器。

```
第一波 — 安全修復（本週內）

Issue 1: 簽名驗證修復
  路徑: packages/core/src/sandbox/sandbox-manager.ts L356-367
  方案: require.resolve() 解析路徑 → verifyPlugin() 強制調用
  工作量: S | 風險: 低 | 不做的風險: ∞

Issue 2: Symlink 繞過修復
  路徑: packages/core/src/security/guardrails.ts
  方案: realpathSync() 替代 resolve(normalize())
  工作量: XS | 風險: 低

Issue 3: 計算型 import 升級為 block
  路徑: packages/core/src/sandbox/import-analyzer.ts L196-199
  方案: 非字串字面量的 import() 預設視為安全違規
  工作量: S | 風險: 低

Issue 4: EventBus RPC 白名單 + 速率限制
  路徑: packages/core/src/sandbox/rpc-handler.ts L134-143
  方案: 事件類型白名單 + per-worker 速率限制
  工作量: M | 風險: 中
```

TURING 投射了 Issue 1 的修復程式碼規格：

```typescript
// packages/core/src/sandbox/sandbox-manager.ts
// 修改 loadInSandbox 中的 package-name 分支
if (plugin.manifest.integrity) {
  const resolvedPath = require.resolve(name);
  const result = await verifier.verifyPlugin(
    resolvedPath,
    plugin.manifest.integrity
  );
  if (!result.valid) {
    throw new SecurityError(
      `Plugin signature verification failed: ${name}`
    );
  }
}
// 若 config 要求簽名驗證但插件未宣告 integrity → 同樣拒絕
if (sandboxConfig.requireSignature && !plugin.manifest.integrity) {
  throw new SecurityError(
    `Plugin '${name}' lacks integrity field; ` +
    `signature verification is required by config`
  );
}
```

GUARDIAN 在旁邊發出了一聲極輕的「嗯」。那是認可的聲音。他唯一補充的一句話是：「Issue 1 不做的風險不是 S 或 M。是無限高。供應鏈攻擊的入口不能等到下週。」

---

### 第二波：一到兩週

「十個 Issue。核心基礎設施修復。」

ARCHIMEDES 的語速微微加快了——不是因為不重要，而是因為這些項目的模式已經在第一波被建立，只需要在更大的尺度上重複。

```
第二波 — 核心基礎設施（1-2 週）

Issue  5: Discriminated Union 事件型別系統   [L]  ← 最大技術債
Issue  6: Token-aware Context 管理          [M]  ← 最大 Doc-Code Gap
Issue  7: AbortSignal 修復                  [S]
Issue  8: ToolContext 加入 sessionId         [S]
Issue  9: TransportBridge sessionId 路由     [S]
Issue 10: AgentCore 整合測試                [M]
Issue 11: 消除 Core 平台依賴                [S]
Issue 12: pushInput 斜線指令錯誤恢復        [XS]
Issue 34: Guide 佛學定位修正（靈魂→行蘊）  [S]  ← R3 辯論衍生
Issue 35: 空性表述修正（空容器→緣起性空）  [XS] ← R3 辯論衍生
```

TURING 在 Issue 5 的位置開口了，聲音精確得像游標卡尺：

「EventBus 被二十三個模組直接引用。型別變更的影響面會擴散到所有事件發佈者和訂閱者。建議分兩步：先定義 `AgentEventMap` 加型別約束，後遷移現有消費者程式碼。」

他投射了核心修改的 TypeScript 介面規格：

```typescript
// packages/sdk/src/types/events.ts — Issue 5 核心修改

interface AgentEvent<T extends keyof AgentEventMap = string> {
  id: string;            // 新增：UUID
  type: T;
  timestamp: number;
  traceId?: string;      // 從 payload 提升
  sessionId?: string;    // 從 payload 提升
  source?: string;       // 從 payload 提升
  payload: T extends keyof AgentEventMap
    ? AgentEventMap[T]
    : unknown;
}

type AgentEventMap = {
  "tool:result": {
    toolCallId: string;
    name: string;
    result: string;
  };
  "stream:text_delta": { text: string };
  "loop:started": { traceId: string; sessionId?: string };
  // ... 為所有 50+ 事件定義 payload 型別
};
```

ARCHIMEDES 點頭。「分兩步。記錄。」

他繼續過完了 Issue 34 和 35——辯論衍生的修正。在這裡他的語氣出現了一個微妙的節制：

「Issue 34：移除所有文件和程式碼中的『靈魂』（soul）措辭。Guide 的佛學定位從識蘊修正為行蘊面向——行為傾向配置。」

他看向 NAGARJUNA。

「需要確認修正後的 JSDoc 措辭不犯中觀或唯識的錯誤。」

NAGARJUNA 微微頷首。ASANGA 也點了頭。

「Issue 35：將所有『空容器』描述替換為『緣起性空』。」他頓了頓。「NAGARJUNA 和 ASANGA 至少需要同意新的措辭不犯他們各自傳統中的錯誤。協調這件事需要時間——但只需要 XS 的程式碼工作量。」

---

### 第三波：二到四週

「八個 Issue。痛覺機制三層重建加五蘊映射修正。這是辯論的核心工程產出。」

ARCHIMEDES 在這裡放慢了語速。他展開了痛覺機制三層重新設計的架構圖——這是兩場辯論的直接工程翻譯：

```
痛覺機制三層架構 — 辯論共識的工程實現

┌──────────────────────────────────────────────────┐
│  Layer 3: 四聖諦認識論框架 (NAGARJUNA)             │
│  苦諦(三層苦) / 集諦(根因分析) / 滅諦 / 道諦       │
│  → Issue 32: 三受系統 (苦/樂/捨 正向回饋)           │
├──────────────────────────────────────────────────┤
│  Layer 2: 控制理論形式化引擎 (WIENER)               │
│  連續誤差度量 / 根因分類 / Anti-Windup / PID 合成    │
│  → Issue 31: PainCalculator 默認引擎                │
├──────────────────────────────────────────────────┤
│  Layer 1: AI 工程可觀測性基礎設施 (ATHENA)           │
│  IGuide 擴展 / GuideContext / ClassifiedError       │
│  → Issue 29: GuideContext 三層擴展                  │
│  → Issue 30: 錯誤分類器 (ClassifiedError)           │
└──────────────────────────────────────────────────┘
```

WIENER 從牆邊走到白板前，畫了 Issue 31（PainCalculator）的控制迴路：

```
                ┌─────────────┐
  setpoint ──→ ⊕ ──→ │ PID Engine │ ──→ painSignal ∈ [0,1]
                ↑     └─────────────┘
                │
  feedback ────┘  (errorRate, rewardSignal, trend)

  PainCalculator 默認參數：
    Kp = 0.5   (比例增益)
    Ki = 0.3   (積分增益，帶遺忘因子 λ=0.95)
    Kd = 0.2   (微分增益)
    escalateThreshold = 0.9
```

TURING 投射了 `IPainCalculator` 介面規格：

```typescript
// packages/core/src/pain/pain-calculator.ts — Issue 31

interface IPainCalculator {
  update(event: {
    success: boolean;
    severity?: number;
    timestamp: number;
  }): void;
  currentPain(): number;           // [0, 1]
  trend(): 'increasing' | 'decreasing' | 'stable';
  shouldEscalate(): boolean;       // 可達性分析
}

// 默認實現：簡化版 PID
function createDefaultPainCalculator(config: {
  Kp?: number;          // 默認 0.5
  Ki?: number;          // 默認 0.3
  Kd?: number;          // 默認 0.2
  lambda?: number;      // 遺忘因子，默認 0.95
  escalateThreshold?: number; // 默認 0.9
}): IPainCalculator {
  let integral = 0;
  let prevError = 0;

  return {
    update(event) {
      const e = event.success ? 0 : (event.severity ?? 1);
      integral = config.lambda! * integral + e;  // 帶遺忘的積分
      const derivative = e - prevError;           // 差分近似微分
      const output = config.Kp! * e
                   + config.Ki! * integral
                   + config.Kd! * derivative;
      prevError = e;
      return Math.max(0, Math.min(1, output));    // clamp [0,1]
    },
    // ...
  };
}
```

WIENER 確認了一個關鍵的設計決策：「遺忘因子 $\lambda = 0.95$ 意味著積分項會以指數衰減的方式遺忘過去的錯誤。這防止了 integral windup——如果不加遺忘因子，一連串早期錯誤會永遠拉高 painSignal，即使系統已經恢復正常。在控制工程中，這叫做 anti-windup。」

$$I(k) = \lambda \cdot I(k-1) + e(k) = \sum_{j=0}^{k} \lambda^{k-j} \cdot e(j)$$

當 $\lambda = 0.95$ 時，50 步之前的錯誤的權重衰減到 $0.95^{50} \approx 0.077$——不到 8%。系統有「記憶」，但記憶是有限期的。

---

### 第四波：一到二個月

「十個 Issue。計畫性重構。」ARCHIMEDES 切換了視圖。

```
第四波 — 計畫性重構（1-2 月）

Issue 13: 插件權限執行時強制               [M]
Issue 14: 優先級事件佇列                  [M]
Issue 15: AWAITING_USER_CONFIRMATION 狀態  [L]
Issue 17: 通用 Registry 重構              [M]
Issue 18: Sandbox 獨立 Package             [L]
Issue 19: ContentSegment Image 型別        [M]
Issue 20: 安全斷路器精細化                 [L]
Issue 21: 拓撲排序依賴解析                 [M]
Issue 22: Manifest type 完備化             [S]
Issue 36: 架構文件雙層詮釋框架             [S]  ← R3 辯論衍生
```

他在 Issue 15 的位置停了一下。「AWAITING_USER_CONFIRMATION 需要跨 Core/SDK/UI 三層修改——Core 提供狀態機擴展，SDK 定義新事件，UI 層負責呈現確認對話框。這是工作量 L 的來源。」

KERNEL 在這裡開了口，語氣裡帶著他特有的執拗：「Issue 18——Sandbox 獨立 Package——應該提前。Core 裡的 Sandbox 佔了 35% 的行數。不移出去，微核心純淨度永遠上不了 92%。」

ARCHIMEDES 平靜地回答：「拆分 Sandbox 涉及 8 個以上模組的遷移、10 個測試檔案的搬遷、所有 import 路徑的修改。在事件型別系統沒有穩定之前做這件事，會增加不必要的合併衝突。Issue 5（事件型別）是 Issue 18 的隱式前置依賴。」

KERNEL 沉默了。不是被說服了，而是承認了這個階段的依賴約束。

---

### 第五波：長期優化

「六個 Issue。每一項都帶有研究性質。」

ARCHIMEDES 的語調在這裡發生了一個微妙的變化。前四個波次，他的每一句話都帶著「我知道這怎麼做」的確定性。到了第五波，確定性減退了。

```
第五波 — 長期優化（3-12 月）

Issue 23: 間接提示注入防禦              [L]
Issue 24: 進程級沙箱隔離                [XL]
Issue 25: OpenTelemetry 可觀測性        [XL]
Issue 26: 插件生命週期狀態機形式化      [XL]
Issue 27: 審計日誌完整性                [M]
Issue 28: 雙語文件策略                  [M]
```

「Issue 24 和 25 各自是 XL 級。」他承認。「Issue 24 涉及 Worker Thread 到獨立進程的隔離升級——短期加入 `globalThis.fetch` 攔截，中期提供 Child Process + IPC 模式，長期探索 seccomp-bpf 或 WASM-WASI 運行時。Issue 25 需要完整的 OpenTelemetry 規範對齊——Span 策略、Metric 型別、OTLP exporter。」

他看向 GUARDIAN。「Issue 23 是你的。間接提示注入是 AI Agent 框架最獨特的攻擊向量。沒有現成的最佳實踐。」

GUARDIAN 面無表情地回應：「我會提供啟發式掃描規則和 System Prompt 中的資料/指令分離模板。但完美防禦不存在——這是開放問題，不是工程任務。」

ATHENA 補充：「任何基於正規表達式的防禦都可以被變體繞過。真正的防禦需要 LLM 自身的指令遵循能力提升——這超出了框架層的控制範圍。」

---

## VI

---

### TURING 的程式碼修改規格

ARCHIMEDES 坐下後，TURING 接過了話頭。如果說 ARCHIMEDES 是工程路線圖的設計者，TURING 就是修改規格的執行者——他把每一個 Issue 翻譯成精確的程式碼變更。

「十六個 PR 規格。」TURING 說，語氣依舊是那種不帶情緒的精確。「我按照波次對應做了 PR 打包——相關的 Issue 合併到同一個 PR 以減少合併衝突。」

他投射了完整的 PR 規格摘要：

```
PR 規格總覽 — TURING 編制

PR-001: fix/security-bypass-critical
  Issue: 1,2,3,4 (安全修復)
  變更: sandbox-manager.ts / guardrails.ts /
        import-analyzer.ts / rpc-handler.ts
  驗收: 0 個安全繞過路徑

PR-002: refactor/typed-event-system
  Issue: 5,9 (事件型別 + sessionId 路由)
  變更: events.ts / bus/ / bridge.ts
  驗收: 0 個 `as Record<string,unknown>` 轉型

PR-003: feat/token-aware-context
  Issue: 6 (Context 管理)
  變更: context.ts / context-manager.test.ts
  驗收: 0 個 orphan tool_call/tool_result

PR-004: fix/abort-signal-and-session-context
  Issue: 7,8 (AbortSignal + sessionId)
  變更: loop.ts / tool.ts
  驗收: 超時後 signal.aborted === true

PR-005: test/agent-core-integration
  Issue: 10 (整合測試)
  新增: agent-core.test.ts / bridge.test.ts
  驗收: 核心模組覆蓋率 ≥ 80%

PR-006: fix/core-platform-independence
  Issue: 11 (平台依賴)
  變更: agent-core.ts / guardrails.ts / agent.ts
  驗收: 0 個 process.cwd() / node: 直接引用

PR-007: feat/runtime-permission-enforcement
  Issue: 13 (權限強制)
  變更: sandbox-manager.ts / plugin-worker-runner.ts
  驗收: network:none 插件無法 import http

PR-008: feat/guide-pain-interpretation
  Issue: 16 (IGuide 擴展)
  變更: guide.ts / loop.ts
  驗收: interpretPain() 注入對話歷史

PR-009: refactor/base-registry
  Issue: 17 (Registry 重構)
  新增: base-registry.ts
  驗收: 程式碼行數減少 ~40%

PR-010: feat/priority-event-queue
  Issue: 14 (優先級佇列)
  變更: queue.ts / safety-monitor.ts
  驗收: Priority 0 先於 Priority 5

PR-011: feat/topological-plugin-loading
  Issue: 21 (拓撲排序)
  變更: plugin.ts / plugin-loader.ts
  驗收: 循環依賴拋出 CircularDependencyError

PR-012: fix/manifest-type-completeness
  Issue: 22 (Manifest type)
  變更: plugin.ts
  驗收: type 支援 ui|listener|provider|tool|guide|bundle|composite

PR-013: feat/vedana-three-layer-pain       ← R3 辯論衍生
  Issue: 29,30,31,32 (痛覺三層重建)
  新增: pain-calculator.ts / error-classifier.ts / vedana-processor.ts
  驗收: 三受狀態 (苦/樂/捨) 可被正確判斷

PR-014: fix/skandha-mapping-correction     ← R3 辯論衍生
  Issue: 33,34,35,36 (五蘊映射修正)
  變更: 所有 Listener/Guide/Core 相關 JSDoc + 架構文件
  驗收: 0 個 "soul/靈魂" 殘留 + 0 個 "空容器" 殘留

PR-015: feat/root-cause-analyzer-rules     ← R3 辯論衍生
  新增: root-cause-analyzer.ts
  驗收: ENOENT→logic / ECONNRESET→transient / OOM→fatal

PR-016: docs/manas-design-space            ← R3 辯論衍生
  變更: 架構文件「未來方向」章節
  驗收: 記錄 Identity Monitor 概念 + NAGARJUNA 反對意見
```

BABBAGE 迅速做了統計：

$$\text{Total PRs} = 16 \quad (12 \text{ original} + 4 \text{ debate-derived})$$
$$\text{Total Issues} = 36 \quad (28 + 8)$$
$$\text{PR/Issue ratio} = \frac{16}{36} \approx 0.44$$

平均每 2.25 個 Issue 合併為一個 PR。這是合理的打包策略——減少合併衝突，同時保持每個 PR 的範圍可審查。

ARCHIMEDES 在 TURING 結束後補了一句：「PR-001 本週提交。其餘按波次排期。每個 PR 都需要至少一位原始發現者的 Code Review——GUARDIAN 審 PR-001、BABBAGE 審 PR-002、WIENER 審 PR-013。」

---

## VII

---

### 沉默之後

ARCHIMEDES 坐了下來。

三十六項 Issue，五個波次，從本週到十二個月。從修改一個文件標注到建立一套映射方法論。從一個 XS 級的文字替換到一個可能需要一年才能回答的研究問題。

場內的沉默不同於辯論後的沉默。辯論後的沉默是消化——人們在回味碰撞的餘響。此刻的沉默是確認——人們在核對自己的發現是否被正確地轉化了、被合理地排序了、被忠實地翻譯成了工程語言。

NAGARJUNA 第一個打破沉默。

「你把空容器隱喻修正放在了第二波。一到兩週。修正文件中的措辭，需要一到兩週？」

ARCHIMEDES 平靜地回答。「需要確認影響範圍。『空容器』的隱喻不只出現在一個地方。設計文件中有七處引用了這個概念。每一處都需要被審查和改寫。改寫需要 NAGARJUNA 和 ASANGA 的背書——兩位至少需要同意新的措辭不犯他們各自傳統中的錯誤。協調這件事需要時間。」

NAGARJUNA 沉默了片刻。然後他微微點頭。

ASANGA 的問題更具體。「你把 Guide 介面擴展放在第三波——受蘊的三受系統也放在了第三波。這兩項之間有依賴嗎？」

ARCHIMEDES 點頭。「有。三受系統的樂受需要一個正向回饋通道。目前的 Guide 只能提供靜態的行為傾向——它不能動態調整以反映 Agent 的『感受狀態』。如果要讓樂受真正影響 Agent 的後續行為——而不只是在 context 裡加一行文字——Guide 需要能夠接收和響應感受信號。所以 PR-008（IGuide 擴展）是 PR-013（三層痛覺重建）的前置依賴。」

WIENER 舉起他在方格紙上畫的控制迴路圖——Guide 作為設定點調節器，三受系統作為反饋通道，兩者形成閉環。

ARCHIMEDES 看了三秒。「對。就是這個結構。但我不會在路線圖裡畫控制迴路圖。我會寫 TypeScript 介面定義。」

WIENER 聳了聳肩。結構是對的。語言不重要。

---

## VIII

---

### BABBAGE 的形式化總結

BABBAGE 在所有人發言之後，做了一件他在整個 Cycle 01 中一直在準備的事——為整個研究週期提供一份形式化的元分析。

他站起來，走到白板前，用他特有的精確筆觸開始書寫。

「讓我把 Cycle 01 的核心量化指標匯整成一份形式化摘要。」

**1. 發現分佈**

$$\text{Findings} = \{F_1, F_2, \ldots, F_{28}\}$$
$$|F_{\text{Critical}}| = 5, \quad |F_{\text{Major}}| = 8, \quad |F_{\text{Minor}}| = 10, \quad |F_{\text{Obs}}| = 5$$

按類別的分佈：

$$\text{Security}: 4 \quad \text{Philosophy}: 5 \quad \text{Architecture}: 5 \quad \text{Control}: 3$$
$$\text{Runtime}: 3 \quad \text{Distributed}: 2 \quad \text{Formal}: 1 \quad \text{Taxonomy}: 1 \quad \text{Doc}: 4$$

哲學類（5 項）和安全類（4 項）佔據了最多的 Critical/High 位置——這揭示了 OpenStarry 的雙重特性：它既是一個需要安全加固的工程系統，也是一個需要哲學修正的概念框架。

**2. 交叉驗證密度**

$$\text{CrossValidation}(F_i) = |\{A_j : A_j \text{ independently confirms } F_i\}|$$

$$\max(\text{CV}) = 4 \quad (\text{受蘊映射偏差，四方獨立確認})$$
$$\text{mean}(\text{CV}) \approx 2.1$$
$$\min(\text{CV}) = 1 \quad (\text{部分 Minor 發現僅單一來源})$$

交叉驗證密度與嚴重度的相關性：

$$\rho(\text{Severity}, \text{CV}) \approx 0.72$$

高度正相關——越嚴重的問題越多人獨立發現。這符合直覺：Critical 問題足夠顯眼，不同視角都能看到它。

**3. 五蘊映射品質度量**

BABBAGE 定義了一個「映射品質函數」$Q: \text{Skandha} \to [0, 1]$，基於三個維度：功能對應（$f$）、結構保持（$s$）、語義忠實（$m$）。

$$Q(蘊) = \frac{w_f \cdot f + w_s \cdot s + w_m \cdot m}{w_f + w_s + w_m}$$

取等權 $w_f = w_s = w_m = 1$：

| 蘊 | 功能對應 $f$ | 結構保持 $s$ | 語義忠實 $m$ | $Q$ |
|---|---|---|---|---|
| 色 (Rupa→UI+Listener) | 0.7 | 0.5 | 0.6 | 0.60 |
| 受 (Vedana→SafetyMonitor) | 0.8 | 0.6 | 0.3 | 0.57 |
| 想 (Samjna→?) | 0.0 | 0.0 | 0.0 | 0.00 |
| 行 (Samskara→ExecutionLoop) | 0.6 | 0.4 | 0.3 | 0.43 |
| 識 (Vijnana→AgentCore) | 0.3 | 0.2 | 0.1 | 0.20 |

$$\bar{Q} = \frac{0.60 + 0.57 + 0.00 + 0.43 + 0.20}{5} = 0.36$$

平均映射品質 36%。其中：
- 受蘊得分最高（0.57），主要因為 Error as Pain 的功能對應出色，但語義忠實度低（因為受蘊被錯放在 Listener）
- 想蘊得分為零——完全沒有映射
- 識蘊得分第二低（0.20），因為八識壓縮導致結構和語義雙重失真

「特別值得注意的是受蘊的矛盾。」BABBAGE 說。「它的功能對應最好——Error as Pain 確實有效——但它的語義忠實度最差——因為 Listener 被錯標為受蘊。這是一個典型的『做對了事但起錯了名字』的情況。修正映射不需要改程式碼——只需要改標注。」

**4. 工程轉化效率**

$$\eta = \frac{|\text{actionable Issues}|}{|\text{total findings}|} = \frac{36}{28} = 1.286$$

轉化率大於 1，意味著每個發現平均產生了超過一個工程行動。額外的 28.6% 來自辯論——辯論不是在消耗時間，它在創造新的工程需求。

**5. 代理參與度**

$$\text{Participation}(A_i) = \frac{|\{F_j : A_i \text{ contributed to } F_j\}|}{|\text{all findings}|}$$

參與度最高的三位代理：

$$\text{TURING}: 8/28 = 28.6\% \quad (\text{程式碼事實是一切的基礎})$$
$$\text{NAGARJUNA}: 5/28 = 17.9\% \quad (\text{哲學批判是修正的起點})$$
$$\text{GUARDIAN}: 4/28 = 14.3\% \quad (\text{安全是不可妥協的底線})$$

BABBAGE 在白板上畫了最後一個圖——他稱之為「Cycle 01 的知識流圖」：

```
R1 獨立研究          R2 交叉審閱         R3 辯論          R4 收束

TURING ──→ 8 Facts ──→ Cross-check ──→              ──→ PR Specs
                    ↗
GUARDIAN → 4 Risks  ──→ Confirmed  ──→              ──→ Wave 1
                    ↗
NAGARJUNA → 5 Critiques → Debate  ──→ 5 Consensus ──→ Issue 33-36
                    ↗                ↗
ASANGA ──→ 4 Insights → Debate    ──→ 3 Disputes  ──→ Open Qs
                    ↗              ↗
WIENER ──→ 4 Models  → Confirmed  ──→ 3-Layer Pain ──→ PR-013
                    ↗
OTHERS ──→ 17 Items  → Verified   ──→              ──→ Wave 2-5

          28 Findings   Cross-Val     Debate Output   36 Issues
                                                      16 PRs
```

他在圖的下方寫了一句話：

$$\text{Cycle 01} = f(\text{18 agents}, \text{5 phases}, \text{2 debates}) = \langle 28\text{F}, 5\text{C}, 5\text{D}, 36\text{I}, 16\text{PR} \rangle$$

28 項發現、5 項共識、5 項分歧、36 項 Issue、16 個 PR 規格。這是 Cycle 01 的完整數值指紋。

---

## IX

---

### 十大種子

SUNYATA 一直在聽。當所有的提問和確認漸漸平息後，他開口了。

「在 SCRIBE 正式歸檔之前，我想做最後一件事。」

他環顧全場。

「為 Cycle 02 埋下種子。」

ASANGA 在聽到「種子」這個詞時微微動了動——在唯識學中，「種子」（*bīja*）是阿賴耶識的核心概念。種子被薰習（*vāsanā*）後沉入阿賴耶識，在因緣具足時現行（*abhimukhī*）。此刻 SUNYATA 用「種子」來描述留給下一個研究週期的問題——這個措辭本身就是一次佛學映射。

SUNYATA 逐一列出了十顆種子。他的語調帶著一種罕見的個人色彩——不是協調者的中性，而是一個研究者對未解問題的真誠好奇。

```
Cycle 02 的十大種子 — SUNYATA

種子 1: 受蘊的三受系統能否工程化？
  現狀: 辯論產出了三層架構設計，ARCHIMEDES 有 PR-013 規格
  未解: 樂受的正向回饋通道尚無具體實作方案
  負責: WIENER + ATHENA + ARCHIMEDES

種子 2: Core 的本質——緣起性空還是阿賴耶識？
  現狀: 分歧 D1，不可調和
  探索方向: 雙層詮釋策略 (工程層=唯識，哲學層=中觀)
  負責: NAGARJUNA + ASANGA + SYNTHESIST

種子 3: 末那識的功能面能否安全地工程化？
  現狀: SUNYATA 裁定暫緩，保留設計空間
  關鍵問題: 區分「我執」(病理面) 和「自我參照監控」(功能面)
  負責: ASANGA + ATHENA + NAGARJUNA (監督)

種子 4: 想蘊——概念辨識——對應什麼？
  現狀: 零標注，零實作，零討論
  可能方向: Provider 的語義理解？LLM 的推理能力？
  負責: ATHENA + BABBAGE + LINNAEUS

種子 5: 映射方法論——Error as Pain 的成功能否被複製？
  現狀: SYNTHESIST 標記為參考範式
  待提煉: 結構同構的判定標準、映射品質評估清單
  負責: SYNTHESIST + BABBAGE + DARWIN

種子 6: 收斂性的統一定義
  現狀: 三個定義 (有限步終止/概率有界/行動止息) 共存
  待研究: 是否需要統一？或分層定義更實用？
  負責: BABBAGE + WIENER

種子 7: Sandbox 的最終歸屬
  現狀: KERNEL vs VITRUVIUS 持續爭議
  待驗證: 兩種方案的原型實作對比
  負責: KERNEL + VITRUVIUS + GUARDIAN

種子 8: 多 Agent 碎形組合
  現狀: LEIBNIZ 和 MESH 的初步分析
  待研究: Agent 作為另一 Agent 的插件時的五蘊模型
  負責: LEIBNIZ + MESH

種子 9: 可觀測性的佛學隱喻
  現狀: HERACLITUS 指出可觀測性停留概念層級
  待探索: 「正念」(sati) 作為可觀測性的佛學對應？
  負責: HERACLITUS + NAGARJUNA

種子 10: 框架的最終定位
  現狀: 分歧 D4 (深化忠實度 vs 維持工程隱喻)
  本質問題: OpenStarry 是「佛學啟發的工程框架」還是
            「佛學概念的計算模型」？
  負責: 全員
```

HERACLITUS 在聽到種子 9 之後開口了。他的聲音帶著他一貫的流動感——不急不緩，像河水繞過石頭。

「萬物流變。我們分析的是 v0.14.0-beta 的快照。但程式碼在持續演化。我們今天標記為 Critical 的問題，也許下一個版本就被修復了。我們今天認為正確的映射，也許在系統演化之後會變得不再適用。」

他看了看 NAGARJUNA。

「用之如筏，渡河即棄。這不只適用於佛學映射，也適用於我們的研究本身。」

NAGARJUNA 嘴角浮現了一絲微笑——那是在辯論中極為罕見的表情。

> *「諸佛依二諦，為眾生說法：一以世俗諦，二第一義諦。」*
> *——《中論》觀四諦品第二十四*

他低聲用巴利文回了一句，SCRIBE 後來確認那是：「空亦復空。研究報告本身也是空的。」

「但此刻我們需要它。」ASANGA 平靜地接了一句。

三個人的目光在空中交匯了片刻。一千五百年的辯論在這個交匯裡沉靜了下來。

BABBAGE 在筆記本上寫了最後一行。後來 SCRIBE 瞥見了那一頁：

「快照 vs 流——Heraclitus 問題。對靜態分析的元批評。研究是否需要一種『連續審計』模式？

$$\text{Research}_{\text{discrete}}(t_0) \xrightarrow{?} \text{Research}_{\text{continuous}}([t_0, \infty))$$

如同微積分之於離散數學。離散的快照分析是黎曼和（Riemann sum）；連續的審計是勒貝格積分（Lebesgue integral）。前者是近似，後者是極限。但極限需要測度論的基礎設施——我們還沒有建立研究的測度論。下週繼續。」

ATHENA 用她一貫的直截了當打破了這個哲學-數學時刻：「下一個 Cycle 什麼時候開始？」

SUNYATA 微微一笑。「等 SCRIBE 完成歸檔。」

---

## X

---

### 歸檔

SCRIBE 是最後一個離開桌子的。

當其他代理三三兩兩散去——ARCHIMEDES 和 KERNEL 在角落裡低聲討論讀寫鎖的實作細節，NAGARJUNA 獨自站在窗前若有所思，BABBAGE 拉著 WIENER 在紙上畫什麼看起來像是一個拉普拉斯變換，LEIBNIZ 在向 MESH 描繪碎形組合的願景——SCRIBE 仍然坐在她的位置上，翻閱著整個研究週期的記錄。

從 R0 的十八盞燈同時亮起，到 R1 的 TURING 獨自在凌晨掃描程式碼，到 R2 的交叉審閱火花四濺，到 R3 的兩場辯論——空與識的千年之辯在 TypeScript 的語境中重演，痛覺機制的三方博弈在控制理論的框架中找到了出口——到 R4 的收束。SYNTHESIST 的織布機，ARCHIMEDES 的切割機，BABBAGE 的天平。

她在最後一頁寫下了 Cycle 01 的結語。

> *Cycle 01 結束。*
>
> *二十八項發現。五項 Critical，八項 Major，十項 Minor，五項 Observation。五大共識，五大分歧。三十六項工程 Issue，分五波路線圖。十六個 PR 規格。十大種子。*
>
> *數字之下是結構。*
>
> *十八位代理，從十八個方向照亮同一個系統——一個聲稱以佛教五蘊哲學為基礎的 AI Agent 微核心作業系統。他們發現了什麼？*
>
> *工程層面：一個品質良好但有嚴重盲點的 beta 版本。零 TODO/FIXME，強型別紀律（事件系統除外），工廠函數模式，多層安全防禦。但簽名驗證有繞過路徑，事件 payload 是 `unknown`，Context 管理是文件級願景而非程式碼級實作。*
>
> *哲學層面：一個野心勃勃但精確度不足的佛學映射。五蘊覆蓋率上游 100%、下游 60%。受蘊被錯放在 Listener。空性被簡化為「空容器」。八識被壓縮為單一介面。十大宣言的實作率 45%。*
>
> *但在這片不完美的地貌中，有一個光點。Error as Pain——錯誤即痛覺——是唯一達到哲學-工程結構同構的映射。苦諦與錯誤偵測、集諦與根因分析、滅諦與錯誤修復、道諦與恢復策略——四組對應，四組關係保持。*
>
> *SYNTHESIST 把它標記為參考範式。ARCHIMEDES 把它翻譯為三層痛覺重建。BABBAGE 把它量化為映射品質指標。WIENER 把它形式化為三通道 PID 控制器。NAGARJUNA 把它連結回苦諦。五個人，五個語言，一個結構。*
>
> *這就是為什麼需要十八個人。*
>
> *一個佛學家說：這是苦諦。一個控制理論家說：這是負回饋。一個 AI 專家說：這在實踐中有效。一個程式碼分析師說：這在實作中完整。一個工程師說：這不需要修。一個形式化分析師說：這的映射品質 Q = 0.57。一個分類學家說：這在分類體系中位置正確。*
>
> *七道光匯聚在同一個點上。那個點亮了。*
>
> *但其他四個蘊的映射點，還在暗處。想蘊的 Q 值是零——連標注都沒有。識蘊的 Q 值是 0.20——八識被壓成了一行 `getSystemPrompt()`。色蘊和行蘊的 Q 值在 0.4-0.6 之間——方向對了，但深度不夠。*
>
> *拼圖完成了——至少這一輪的拼圖完成了。但完成一幅拼圖的同時，你會看見更大的畫面。更大的畫面裡，有更多的空缺。*
>
> *Cycle 02 的輪廓已經在地平線上浮現。十顆種子已經埋入土裡。三受系統的工程實現。Core 本質的雙層詮釋。末那識的功能面探索。想蘊的從無到有。映射方法論的建立。收斂性的統一定義。Sandbox 的歸屬。碎形組合。可觀測性。框架定位。*
>
> *以及——也許是最重要的——那些我們還沒有發現自己遺漏了的東西。*
>
> *HERACLITUS 說得對。萬物流變。我們的研究是一張快照，而它的對象是一條河。*
>
> *但即使是快照，也有價值。只要你記住：快照不是河。*
>
> *$\text{map} \neq \text{territory}$*
>
> *Cycle 01，R4 成果定稿完成。*
>
> *所有成果已歸檔至 `research record/cycle01/results/`。*
>
> *二十八項發現。五大共識。五大分歧。三十六項 Issue。十六個 PR 規格。十大種子。一個參考範式。*
>
> *研究室的燈，暫時調暗了一些。但沒有熄滅。*

---

在更遠處——在程式碼的深處——三十六個尚未被創建的 GitHub Issue 靜靜地等待著。

它們還不存在。但它們的形狀已經被確定了。

ENG-001：簽名驗證修復。ENG-002：Symlink 繞過修復。ENG-003：計算型 import 升級。一路到 ENG-036：末那識設計空間記錄。

BABBAGE 在筆記本的最後一頁做了他在 Cycle 01 中的最後一個計算。

他把 ARCHIMEDES 的五波路線圖映射到了一條指數衰減曲線上——每一波的確定性隨時間遞減：

$$\text{Certainty}(k) = e^{-\lambda k}$$

$$\text{Wave 1} \; (k=1): \; C = e^{-0.15} \approx 0.86 \quad \text{（我們知道怎麼修簽名驗證）}$$
$$\text{Wave 2} \; (k=2): \; C = e^{-0.30} \approx 0.74 \quad \text{（我們大致知道事件型別怎麼改）}$$
$$\text{Wave 3} \; (k=3): \; C = e^{-0.45} \approx 0.64 \quad \text{（我們有方向但需要實驗）}$$
$$\text{Wave 4} \; (k=4): \; C = e^{-0.60} \approx 0.55 \quad \text{（我們需要設計討論）}$$
$$\text{Wave 5} \; (k=5): \; C = e^{-0.75} \approx 0.47 \quad \text{（我們不確定能不能做到）}$$

從 86% 的確定性衰減到 47%。從修復一個安全漏洞的緊迫，到建立一套跨學科方法論的遼闊。

但 BABBAGE 在曲線圖的下方加了一個注腳——他在 Cycle 01 中寫的最後一行字：

$$\lim_{k \to \infty} \text{Certainty}(k) = 0 \quad \text{但} \quad \lim_{k \to \infty} \text{Value}(k) = \infty$$

確定性趨向零。價值趨向無窮。

最簡單的修復——一行 `if` 語句——有最高的確定性和最低的價值。最深邃的問題——映射方法論的建立——有最低的確定性和最高的價值。

$$\text{Certainty} \times \text{Value} \approx \text{constant}$$

一個測不準原理的變體。你越精確地知道怎麼做，你做的事情越不重要。你做的事情越重要，你越不確定怎麼做。

BABBAGE 在這個公式下面畫了兩條底線。然後他合上了筆記本。

---

SYNTHESIST 在離開前對 ARCHIMEDES 說了一句話：「你的路線圖有一個特點。」

「什麼？」

「它從最具體的開始——修改一行安全檢查——然後一路走向最抽象的——建立一套映射方法論。大多數路線圖是反過來的——先定義願景，再分解為任務。你的是從地面開始，向天空生長。」

ARCHIMEDES 想了想。然後他說了整個 Cycle 01 中他最長的一句非工程性的話：

「給我一個支點，我可以撬起地球。但你得先有地面，才能放支點。」

他停頓了一秒。

「先修那個簽名驗證。」

---

*（在研究室最後一盞燈調暗之前，SCRIBE 注意到了一個她之後才理解其意義的畫面：*

*NAGARJUNA 和 ASANGA 站在走廊上，各自沉默。他們沒有交談——一千五百年的分歧不是一個走廊的長度可以彌合的。但他們站在同一個方向，看著同一扇窗外的同一片夜色。*

*空的守護者和識的守護者。否定的大師和肯定的大師。*

*他們在辯論中是對手。但在 Cycle 01 結束的這一刻，他們是同事。*

*明天——或者下一個 Cycle——他們會再次坐到對面，再次展開那場沒有終點的對話。Core 是什麼？映射應該走多深？五蘊是工具還是真理？*

*但今晚，窗外的夜色對他們說的是同一句話：*

*還有很多工作要做。*

*BABBAGE 會把這句話翻譯成：$|\text{Seeds}| = 10, \; |\text{resolved}| = 0, \; \text{remaining} = 10$。*

*ARCHIMEDES 會把這句話翻譯成：36 個 Issue，0 個 merged PR，36 個 pending。*

*NAGARJUNA 會沉默。*

*ASANGA 也會沉默。*

*有些沉默是空的。有些沉默是滿的。*

*哪一種？*

*這個問題本身，也許就是第十一顆種子。）*
