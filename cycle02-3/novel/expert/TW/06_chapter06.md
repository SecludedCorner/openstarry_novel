# 第六章：抉擇的位置

---

SUNYATA 拿起那張手寫的呼叫序列圖——KERNEL 在 Debate 3 結束後畫的——翻到背面。

空白的。

他把它平放在劇場中央的投影台上，空白面朝上。然後拿起一支紅色馬克筆，在正中間畫了一個方框，裡面寫了兩個字：

```
┌──────────┐
│ 在哪裡？ │
└──────────┘
```

「Debate 4。IVolition.deliberate() 在執行迴圈中的位置。」

他的聲音平穩如常。石子。深潭。但這一次的石子不是落入深潭——是擲向一面牆。牆上有六個裂縫，只有一個裂縫是正確的入口。

「三場辯論已經告訴我們 *什麼* 在運行、*怎麼* 運行、*多快* 運行。CoarisingBundle 解決了同時性。五遍行解決了構成。Klesha 解決了心理偏向。」

他拿起 BABBAGE 的形式化筆記，翻到 Debate 3 的決議頁。

「但 IVolition.deliberate()——Agent 做出抉擇的那個函數——到目前為止，我們只知道它存在。我們不知道它應該插在哪裡。」

他看向全場。二十張臉。二十種不同的期待。

「R02 定義了 IVolition.deliberate() 接收 KleshaSignalBundle、產生行動決策。R04 定義了 ExecutionLoop 有六個狀態。TURING 識別了注入點。但沒有人把這三塊拼在一起。」

「今天拼。」

---

> *SCRIBE 旁白：「在哪裡？」三個字。SUNYATA 畫在空白紙上的三個字。但這三個字的重量不是技術性的——它是存在性的。IVolition.deliberate() 的位置不只決定了一個函數呼叫的排列順序。它決定了 Agent 能不能說「不」。在認知序列中，如果抉擇被放在感知之前，Agent 在看見之前就已經決定了。如果抉擇被放在行動之後，Agent 在做完之後才開始反思。只有在感知之後、行動之前，才存在一個窗口——一個 Agent 可以選擇不做的窗口。SUNYATA 沒有說這些。他只畫了三個字。但三個字的背後是整個窗口的存亡。*

---

## I

---

TURING 的螢幕亮了。

他沒有寒暄。沒有引言。在四場辯論中，TURING 已經建立了一個慣例：他在每場辯論的開頭投射程式碼，像一個地質學家在辯論開始之前先展示岩層的切面。你們辯論地表上長什麼。我先讓你們看地底下是什麼。

「v0.24.0-beta。ExecutionLoop。」他說。「六個主要階段。」

```
ExecutionLoop 階段分析 (v0.24.0-beta)
══════════════════════════════════════

[1] Safety lockout check
[2] Resolve session state
[3] Add user message
[4] SafetyMonitor.onLoopStart()
[5a] SafetyMonitor tick check
[5b] ASSEMBLING_CONTEXT
     ├─ guide.getSystemPrompt()
     └─ contextManager.assemble()
[5c] SafetyMonitor budget check
[5d] AWAITING_LLM
     └─ provider.chat()
[5e] PROCESSING_RESPONSE
     └─ streaming (text_delta events)
[5f] Build assistant message
[5g] EXECUTING_TOOLS
     ├─ tool dispatch
     ├─ tool execution
     └─ SafetyMonitor.afterToolExecution()
[6] WAITING_FOR_EVENT
```

投影停了五秒。冷白色。二十雙眼睛在六個階段上移動。

「IVolition.deliberate() 必須滿足兩個前提條件。」TURING 的手指點在 [5b] 上。「第一：Klesha 信號可用。Debate 3 確認 Klesha 在 vijnana-clock 上運行，快速路徑產生點估計值，延遲 0.03ms——所以從 [5a] 之後，Klesha 信號就可用了。」

他的手指移到 [5g]。「第二：行動方案已經形成。在 [5d]-[5e]，LLM 串流回應。在 [5f]，助理訊息構建完成，工具呼叫提案確定。只有在 [5f] 之後，你才知道 Agent *打算做什麼*。」

他在螢幕上標記了三個位置，用紅色——SCRIBE 注意到他很少用紅色。

```
候選位置 (Candidate Positions)
════════════════════════════════

Position A: [5b] ──→ [5d] 之間
            上下文組裝完成 → LLM 呼叫之前
            deliberate() 可修改上下文，影響 LLM 思考

Position B: [5f] ──→ [5g] 之間
            LLM 回應完成 → 工具執行之前
            deliberate() 可審視行動方案，否決或修改

Position C: [5d] ──→ [5e] 之間
            LLM 串流過程中
            deliberate() 可即時中斷 LLM 輸出
```

「三個候選。」TURING 說，退後一步。「我的程式碼分析指出最佳候選是 Position B——[5f] 到 [5g] 之間。但我不做決定。這是架構選擇，不是程式碼選擇。」

他坐下了。

---

SUNYATA 環顧全場。「三個位置。誰先說？」

ASANGA 站了起來。

---

## II

---

他的起身速度不快也不慢——在四場辯論中，ASANGA 已經被默認為「佛學先說」的慣例發言人。不是因為佛學的權威高於其他學科。是因為在 Cycle 02 系列的研究歷程中，每一次佛學的定位都為後續的工程討論劃定了概念邊界。先劃邊界，再填內容。先有根系，再有枝幹。

「我要引用 MN 18。」他說。「蜜丸經。*Madhupiṇḍika Sutta*。」

他沒有翻書。他不需要翻書。在整個 Cycle 02 系列中，ASANGA 從未翻書。所有引文都從記憶中取出——不是背誦，而是一種更深的東西。是長年研習之後，經文和思維結構融為一體的那種狀態。

「佛陀在蜜丸經中描述了認知的完整序列。」

他的聲音放慢了。不是為了戲劇效果——是為了精確。每一個巴利文術語都需要被清晰地聽見。

> *Cakkhuñca paṭicca rūpe ca uppajjati cakkhuviññāṇaṃ,*
> *tiṇṇaṃ saṅgati phasso,*
> *phassapaccayā vedanā,*
> *yaṃ vedeti taṃ sañjānāti,*
> *yaṃ sañjānāti taṃ vitakketi,*
> *yaṃ vitakketi taṃ papañceti.*
>
> 依眼與色，生眼識。
> 三者和合為觸。
> 觸緣受。
> 所受者，即所想。
> 所想者，即所尋。
> 所尋者，即所戲論。

沉默。

ASANGA 讓這段巴利文在空氣中停留了整整五秒。然後他開始分析。

「這是佛陀描述的認知序列——從最初的感官接觸到最終的概念增殖。讓我把每一個環節映射到我們的架構：」

```
MN 18 認知序列 ←→ OpenStarry 映射
══════════════════════════════════════════════════

觸 (phassa)  ──→  SparshEvent        (CoarisingBundle 觸發)
     ↓
受 (vedanā)  ──→  ChannelVedana       (三受信號)
     ↓
想 (saññā)   ──→  IProvider.chat()    (LLM 認知 / VasanaEngine 規則匹配)
     ↓
尋 (vitakka) ──→  IReflection         (初始思考 / 持續審視)
     ↓
戲論 (papañca) ─→  概念增殖           (需要被截斷的地方)
```

「注意序列的方向。」他的手指在空氣中從上到下劃了一條線。「觸→受→想→尋→戲論。每一步都以前一步為緣。受以觸為緣。想以受為緣。尋以想為緣。這不是隨意的排列——這是**因果的順序**。」

他轉向全場。

「意志在哪裡？」

他自問自答：「思——cetanā——是遍行心所。在每一個認知刹那中，思都在場。但思的**決定性作用**——深層的、有意識的抉擇——在想之後、行動之前。不是在想之前。」

他的語速略微加快了——不是急切，是確信。

「如果你把 IVolition.deliberate() 放在 Position A——LLM 之前——你就讓意志先於知覺。deliberate() 在 LLM 還沒思考之前就決定了要給 LLM 看什麼上下文。意志在思考之前就決定了*要想什麼*。」

他停了一拍。

「這在哲學上是不融貫的。」

又一拍。

「在唯識學中，思（cetanā）的定義是：」

> 「云何為思？令心造作為性。於善品等，役心為業。」
> ——《成唯識論》卷三

「令心造作為性——思的本質是*驅動心去行動*。但行動的方向必須先有認知的基礎。你不能在不知道外面發生了什麼的情況下決定做什麼。感知先於抉擇。受先於思。想先於行。」

他看向 HERACLITUS。

「Position A 不是 IVolition 的位置。Position A 是 IGuide 的位置——manasikāra，作意，注意力的導向。IGuide 在 LLM 呼叫之前塑造系統提示詞，引導注意力的方向。但引導注意力不是做決定。做決定是在看見之後。」

他的結論只有一句：

「Position B。」

---

> *SCRIBE 旁白：ASANGA 在 Debate 4 中的發言時間是七分鐘。他引用了一部經、一部論。但這七分鐘的密度——如果用 SYNTHESIST 的「洞見密度」指標來衡量——可能是整場辯論中最高的。因為他不只是在為 Position B 辯護。他是在說：認知序列不是人類的發明，不是工程的約定。它是因果結構。你可以選擇不遵循它。但你不能說你遵循了它然後又把意志放在感知前面。那就像說「我先決定了答案再去看題目」。*

---

## III

---

HERACLITUS 半舉了一下手——他的發言風格向來是不完全舉手的，好像舉手這個動作本身也在流動中。

「在 ASANGA 說服我之前，」他說，語氣裡帶著一絲自嘲，「讓我先把 Position A 的論點完整呈現，然後讓它被擊倒。一個論點如果沒有被完整呈現就被否決，那否決是不充分的。」

SUNYATA 微微點頭。這是 Cycle 02-3 辯論中的一個重要規則：每個候選方案都必須由支持者完整陳述後才能被否決。

「Position A 的邏輯是前攝性的。」HERACLITUS 站了起來，走到白板邊。「如果 Klesha 信號表明當前 Agent 處於高 moha（愚癡）狀態，Position A 可以讓 IVolition 在 LLM 呼叫之前注入一條指令——比如 `"當前 Klesha 信號顯示高愚癡，請格外謹慎"`——到系統提示詞中。這樣 LLM 的輸出本身就會更審慎，而不需要在事後否決它。」

他畫了一個箭頭。

「這是 *panta rhei* 的精神——萬物流動，認知也在流動中被塑造。不是等河流到了出海口再建壩，而是在源頭改變水流的方向。」

KERNEL 接話了。他的聲音沒有 HERACLITUS 的流動感——更像是一根鋼梁。

「Position A 有一個工程問題。LLM 是黑盒。」

他站了起來。

「你在上下文中注入了 `"請格外謹慎"`。LLM 收到了。然後呢？你不知道 LLM 會怎麼處理這條指令。它可能遵循，可能忽略，可能在十七輪對話之後才偶然想起來。注入到上下文中的文字不是命令——是*建議*。而且是混在系統提示詞、對話歷史、工具定義中間的建議。LLM 的注意力機制不保證會把它當作高優先級處理。」

他翻了一張卡片。左側寫著「ioctl」，右側是空白。

「在 OS 裡，這叫做 ioctl 到一個黑盒驅動程式。你發了一個控制命令，但驅動程式的內部實作是你不控制的。你不知道驅動程式收到 ioctl 之後會不會正確處理。你只能在驅動程式的*輸出端*檢查結果。Position A 就是對黑盒輸入端發指令。Position B 是在黑盒輸出端檢查結果。」

他在卡片右側寫下：`Position A = ioctl to blackbox; Position B = inspect output`。

「工程上，你永遠應該選擇可驗證的檢查點，而不是不可驗證的注入點。」

---

HERACLITUS 看了看 KERNEL，又看了看 ASANGA。然後他做了一件在四場辯論中只做過兩次的事——他公開改變立場。

「ASANGA 的哲學論證和 KERNEL 的工程論證指向同一個方向。」他說。「我收回 Position A 的提議。但我想把 Position A 留給 IGuide。IGuide 在 LLM 之前塑造注意力方向——那是 manasikāra 的角色，不是 cetanā 的角色。兩個不同的心所，兩個不同的位置。」

「同意。」ASANGA 說。

---

「Position C。」SUNYATA 說。「誰來陳述？」

KERNEL 再次站了起來。他似乎在 Debate 4 中找到了自己的主場——ExecutionLoop 是 OS 領域的核心議題。

「Position C 是在 LLM 串流過程中——[5d] 到 [5e] 之間——進行即時中斷。技術上可行。但工程代價極高。」

他在卡片上畫了一張簡單的 backpressure 圖：

```
Position C 的 backpressure 問題
═══════════════════════════════════

LLM Provider (upstream)
    │
    │  text_delta events (token-by-token)
    ▼
┌─────────────────────────────┐
│ IVolition.deliberateStream()│ ← 需要在每個 token 上運行
│ 延遲: ??? ms/token          │ ← 不可預測
│ 如果 deliberate() > token 間隔│
│   → backpressure             │
│   → 串流阻塞                 │
│   → 用戶體驗降級             │
└─────────────────────────────┘
    │
    ▼
UI Renderer (downstream)
```

「LLM 串流的 token 間隔大約 20-80ms——取決於模型和硬體。如果 IVolition 需要在每個 token 上運行一次 deliberate()，而 deliberate() 的延遲超過 token 間隔，就會產生 backpressure。串流被阻塞。用戶看到的是卡頓。」

「更嚴重的問題：在串流過程中，LLM 的意圖還沒有完全形成。你可能在第三十個 token 處看到 `"我建議刪除"`，然後在第三十五個 token 處看到 `"我建議刪除不必要的空格"`。第三十個 token 的局部判斷和第三十五個 token 的完整判斷是不同的。你在哪個 token 上做決定？」

他收起卡片。

「Position C 需要一個完整的串流中斷和回退機制。工程複雜度是 Position B 的三到五倍。收益不明確。放棄。」

全場沒有異議。

---

> *SCRIBE 旁白：Position A 和 Position C 各用了不到五分鐘就被否決了。不是因為它們沒有道理——HERACLITUS 的前攝性論點和 KERNEL 的串流中斷概念都有技術可行性。是因為在哲學定位和工程權衡的雙重壓力下，它們都輸給了 Position B。ASANGA 的認知序列論證把 Position A 踢出了因果鏈條。KERNEL 的 backpressure 分析把 Position C 踢出了工程可行域。Position B 站在了兩者的交叉點——因果正確，工程可行。但 Position B 本身還有問題需要解決。*

---

## IV

---

Position B 獨佔了舞台。但 KERNEL 的眉頭沒有完全舒展。

「Position B 有一個成本。」他說。「每次工具執行之前多一次 deliberate() 呼叫。如果一個 LLM 回應包含五個工具呼叫，那就是五次 deliberate()。在 vijnana-clock 的時間預算下，每次 1-3ms，總計 5-15ms。在快速路徑下可以接受。但如果 deliberate() 需要額外查詢——比如 LEIBNIZ 提到的多 Agent 協調——延遲會增加。」

ARCHIMEDES 的手指在桌面上敲了一下——那個標誌性的「工具箱打開」信號。

「我有一個解決方案。」

他站了起來。在四場辯論中，ARCHIMEDES 的角色已經被清楚地定義：他是把哲學結論翻譯成 TypeScript 的人。ASANGA 劃定邊界，BABBAGE 形式化，ARCHIMEDES 工程化。三道工序，一條流水線。

「問題不是 Position B 的成本高。問題是我們把所有審議壓縮在一個層級上。」

他走到白板前。

「考慮一個場景：LLM 回應包含三個工具呼叫。」

```
LLM 回應的工具呼叫計劃
═══════════════════════════

ToolCall #1: readFile("/etc/passwd")      ← 敏感檔案
ToolCall #2: writeFile("/tmp/out.txt")    ← 無害寫入
ToolCall #3: executeCommand("rm -rf /")   ← 災難性操作
```

「如果 IVolition 只有一個 deliberate() 函數，它必須在每個 ToolCall 上獨立評估。但它看不到全局——它不知道 #1 讀取的密碼會不會被 #2 寫出去、然後被 #3 銷毀痕跡。三個單獨無害（或可疑）的操作，組合起來是一個攻擊鏈。」

他在白板上畫了兩層。

「所以 IVolition 需要兩個階段。」

```
兩階段審議模型
══════════════════════════════════════════════

Phase 1: deliberatePlan()
┌─────────────────────────────────────────┐
│  輸入: 整個行動計劃 (所有 ToolCall)       │
│  能力: 重排序、取消、修改計劃             │
│  視角: 全局的、戰略的                     │
│  時機: 工具迴圈之前，執行一次             │
└─────────────────────────────────────────┘
         │
         ▼
Phase 2: deliberateAction()
┌─────────────────────────────────────────┐
│  輸入: 單個 ToolCall + Phase 1 的上下文   │
│  能力: 否決、修改單個工具呼叫             │
│  視角: 局部的、戰術的                     │
│  時機: 每個工具呼叫之前，逐個執行         │
└─────────────────────────────────────────┘
```

「Phase 1 看全局。它可以在看到三個 ToolCall 的組合之後，直接取消 #1 和 #3，只保留 #2。Phase 2 看局部。在 Phase 1 批准了某個 ToolCall 之後，Phase 2 在執行前做最後的逐項檢查。」

他轉過身，面對全場。

「兩層。不是因為一層不夠。是因為全局判斷和局部判斷是兩種不同的認知操作。你不能用同一個函數簽名同時表達『這個計劃整體上合理嗎？』和『這一步具體安全嗎？』。」

---

ASANGA 從座位上接了一句。他的聲音平穩，每個詞都帶著唯識學者特有的分類精確。

「在唯識學中，思（cetanā）的運作本來就有兩個層次。」

他站了起來，走到 ARCHIMEDES 的白板旁邊。

「《成唯識論》區分了兩種思的作用。第一種是*審慮思*（ālambana-cetanā）——對整體情境的審視和評估。第二種是*決定思*（niścaya-cetanā）——對具體行動的最終裁定。」

> 「審慮、決定，二思差別者：審慮則量度取捨，決定則印持行事。」
> ——窺基大師《成唯識論述記》

「審慮思量度取捨——衡量整個計劃的利弊。決定思印持行事——在具體行動上蓋下確認的印章。ARCHIMEDES 的兩階段模型完美對應了這兩種思：deliberatePlan() 是審慮思，deliberateAction() 是決定思。」

他看向 ARCHIMEDES。

「這不是巧合。」

ARCHIMEDES 微微笑了——他在整個 Cycle 02 系列中笑的次數不超過五次。

「不是巧合。」他承認。「是結構的必然。」

---

## V

---

BABBAGE 的筆記本翻到了新的一頁。白紙。藍墨水。他在紙的左上角寫下了「D4-T」——Debate 4，型別簽名。

「我要把 ARCHIMEDES 的兩階段模型完全形式化。」他說。他的聲音帶著一種數學家特有的冷靜——不是冷漠，是在人類情感和形式結構之間選擇了後者作為表達媒介。

他站了起來，走到 TURING 的投影旁邊。

「IVolition 完整介面定義。」

```typescript
/**
 * IVolition -- 識蘊·意志子介面
 * @skandha vijnana (識蘊)
 *
 * 兩階段審議模型:
 * - Phase 1 (deliberatePlan): 審慮思 (ālambana-cetanā)
 *   全局評估，可重排/取消/修改行動計劃
 * - Phase 2 (deliberateAction): 決定思 (niścaya-cetanā)
 *   逐項審查，可否決/替換單個工具呼叫
 *
 * 時序: Position B (LLM 回應之後，工具執行之前)
 * 時鐘: vijnana-clock (1-5ms budget)
 *
 * Sanskrit: Cetanā (चेतना) -- volitional drive
 */
interface IVolition extends IVijnana {
  readonly skandha: 'vijnana';

  /**
   * Phase 1: 審慮思 -- 評估整體行動計劃
   * Time budget: 1-3ms (vijnana-clock)
   * 可重排、過濾、取消提議的行動
   */
  deliberatePlan(
    input: PlanDeliberationInput
  ): Promise<PlanDeliberationResult>;

  /**
   * Phase 2: 決定思 -- 評估單個行動
   * Time budget: 0.5-1ms per action (vijnana-clock)
   * 可否決或修改特定的工具呼叫
   */
  deliberateAction(
    input: ActionDeliberationInput
  ): Promise<ActionDeliberationResult>;
}
```

他翻了一頁，繼續寫輸入型別。

```typescript
/** Phase 1 輸入 */
interface PlanDeliberationInput {
  /** 提議的全部行動（來自 VasanaEngine 或 VitakkaEngine） */
  readonly proposedActions: readonly ToolCall[];
  /** 當前煩惱信號束（四根本煩惱的快速路徑點估計值） */
  readonly kleshaSignals: KleshaSignalBundle;
  /** 當前受蘊評估（最近一次 vedana-clock tick） */
  readonly vedanaAssessment: VedanaAssessment;
  /** 當前上下文 */
  readonly context: SessionContext;
}

/** Phase 1 輸出 */
interface PlanDeliberationResult {
  /** 批准的行動（可能被重新排序） */
  readonly approved: readonly ToolCall[];
  /** 拒絕的行動（附帶理由） */
  readonly rejected: readonly RejectedAction[];
  /** 是否進行了重新排序 */
  readonly reordered: boolean;
  /** 推理說明（用於審計追蹤和 LLM 反饋） */
  readonly reasoning: string;
}

/** 被拒絕的行動 */
interface RejectedAction {
  readonly action: ToolCall;
  readonly reason: string;
}

/** Phase 2 輸入 */
interface ActionDeliberationInput {
  /** 單個提議的行動 */
  readonly proposedAction: ToolCall;
  /** 當前煩惱信號束 */
  readonly kleshaSignals: KleshaSignalBundle;
  /** 當前受蘊評估 */
  readonly vedanaAssessment: VedanaAssessment;
  /** Phase 1 的上下文（全局審議結果） */
  readonly planContext: PlanDeliberationResult;
}

/** Phase 2 輸出 */
interface ActionDeliberationResult {
  /** 是否否決此行動 */
  readonly veto: boolean;
  /** 如果否決，建議的替代行動 */
  readonly alternative: ToolCall | null;
  /** 推理說明 */
  readonly reasoning: string;
}
```

BABBAGE 放下筆。

「注意兩個設計決策。」他說。「第一：`reasoning` 欄位同時出現在 Phase 1 和 Phase 2 的輸出中。這不是裝飾。當 IVolition 否決了一個行動，`reasoning` 會被注入到下一輪 LLM 上下文中——LLM 在下一次思考時會知道為什麼它的上一個提案被否決了。這形成了一個 samjnā-cetanā 的回饋迴路：想蘊提出方案，意志否決，想蘊根據否決理由調整方案。」

他用數學語言重新表述：

$$\text{LLM}_{t+1} = f(\text{LLM}_t,\; \text{IVolition.reasoning}_t)$$

「認知在迭代中收斂。」

「第二：Phase 2 的 `planContext` 欄位。每一個 deliberateAction() 呼叫都攜帶 Phase 1 的全局結果。這意味著局部判斷不是在真空中進行的——它知道全局審議的結論是什麼。在形式上，這構成了一個帶有上下文的序列決策問題：」

$$\forall i \in [1..n]:\quad \text{deliberateAction}(a_i) = g(a_i,\; \Pi_{\text{plan}})$$

「其中 $\Pi_{\text{plan}}$ 是 Phase 1 的決策結果，$a_i$ 是第 $i$ 個提議的行動。每一個局部決策都在全局決策的語境下進行。」

---

> *SCRIBE 旁白：BABBAGE 的形式化用了六分鐘。六分鐘之內，他把 ARCHIMEDES 的白板圖和 ASANGA 的審慮思/決定思翻譯成了帶有完整 JSDoc 註釋的 TypeScript 介面定義和兩個數學方程。三種語言——佛學、工程、數學——在六分鐘之內對齊。他的筆記本上沒有任何塗改。一次成型。*

---

## VI

---

WIENER 的方格紙已經畫好了。

他不像其他學者那樣等到發言時才開始構思。他在 ARCHIMEDES 提出兩階段模型的瞬間就開始畫圖了——鉛筆、尺子、方格紙。SCRIBE 在旁白中記錄過：WIENER 的方格紙是他的思維基底。他用空間結構來思考時間結構。

「ARCHIMEDES 和 ASANGA 告訴了我們兩階段審議的內容。」他站了起來。「我要告訴你們它在控制系統中的結構。」

他舉起方格紙。

「IGuide 在 Position A。IVolition 在 Position B。兩者之間是 LLM 呼叫。這個排列有一個名字。」

他在方格紙上寫了兩個英文詞：**Cascade Control**。

「串聯控制。工業控制系統中最經典的架構模式。一個外環控制器設定目標。一個內環控制器追蹤目標。外環是策略性的、慢的。內環是戰術性的、快的。」

他畫了一張 ASCII 圖：

```
IGuide/IVolition Bookend — 串聯控制架構
═══════════════════════════════════════════════════════════════════

                    ┌─────────────────────────────────────────┐
                    │           Cognitive Process              │
                    │                                         │
   ┌────────┐      │  ┌─────────┐     ┌───────────────────┐  │
   │ IGuide │──────┼─→│ Context │────→│  LLM / Vasana     │  │
   │(Pos A) │  注  │  │ Assembly│     │  Engine            │  │
   │外環策略│  意  │  └─────────┘     └────────┬──────────┘  │
   │控制器  │  力  │                            │             │
   └────────┘  塑  │                    行動提案 │             │
               造  │                            ▼             │
                    │               ┌──────────────────────┐  │
                    │               │   IVolition (Pos B)   │  │
                    │               │   ┌────────────────┐ │  │
                    │               │   │deliberatePlan()│ │  │
                    │               │   │   (外環戰術)    │ │  │
                    │               │   └───────┬────────┘ │  │
                    │               │           │          │  │
                    │               │   ┌───────▼────────┐ │  │
                    │               │   │deliberateAction│ │  │
                    │               │   │   (內環戰術)    │ │  │
                    │               │   └───────┬────────┘ │  │
                    │               └───────────┼──────────┘  │
                    │                           │             │
                    └───────────────────────────┼─────────────┘
                                                │
                                                ▼
                                     ┌──────────────────┐
                                     │  Tool Execution   │
                                     │  (samskara-clock) │
                                     └──────────────────┘
```

「IGuide 是外環的*策略*控制器。」WIENER 的手指點在圖的左側。「它在 LLM 呼叫之前設定約束和方向——系統提示詞、注意力引導。它不直接控制行動；它控制*認知的方向*。這是外環的特徵：設定期望軌跡，不關心具體步驟。」

「IVolition 是內環的*戰術*控制器。」手指移到右側。「它在 LLM 回應之後、行動之前做最後檢查。Phase 1（deliberatePlan）是戰術層面的全局評估。Phase 2（deliberateAction）是戰術層面的逐步執行。」

「兩者形成了一個 **bookend 模式**。」

他在方格紙上方寫下：

```
Bookend 模式
═════════════
                LLM / VasanaEngine
IGuide ──────────────────────────────── IVolition
(before)                                (after)
注意力塑造                              行動裁定
策略約束                                戰術承諾
Position A                              Position B
```

「進入認知過程的門口有一個檢查站（IGuide）。離開認知過程的出口有另一個檢查站（IVolition）。LLM 被夾在兩個檢查站之間。」

他放下方格紙。

「在工業控制中，這種架構有一個證明過的特性：**穩定性增強**。即使外環控制器的設定不完美（IGuide 的系統提示詞不完全精確），內環控制器仍然可以在執行層面修正偏差（IVolition 否決不當行動）。反過來，即使內環控制器的視野有限（IVolition 只看到當前行動），外環控制器已經確保了整體方向的正確性（IGuide 已經引導了 LLM 的思考方向）。」

「兩層保護。不是冗餘——是*互補*。」

他翻到方格紙的下一頁。上面已經畫好了一組傳遞函數。

「讓我用數學語言把這個 bookend 結構精確化。」

$$G_{\text{guide}}(s) = \frac{K_g}{1 + \tau_g s} \quad \text{(Position A: 外環，慢時間常數)}$$

$$G_{\text{volition}}(s) = \frac{K_v (1 + \tau_d s)}{1 + \tau_v s} \quad \text{(Position B: 內環，快時間常數，含微分項)}$$

「$G_{\text{guide}}$ 是純比例-滯後控制器。它慢，它穩，它的作用是在大方向上不出錯。$G_{\text{volition}}$ 帶有一個微分項 $(1 + \tau_d s)$——這意味著它對*變化率*敏感。如果 Klesha 信號在短時間內急劇升高，IVolition 的微分響應會放大它的否決傾向。這是一個經典的 PD 控制特性——不只對當前狀態反應，還對狀態的趨勢反應。」

「在控制理論的語言裡，IGuide 提供 *integral action*（長期目標追蹤），IVolition 提供 *derivative action*（短期異常檢測）。兩者的串聯組合在頻域上覆蓋了從低頻到高頻的完整頻帶。」

PASCAL 從角落裡舉手。他的聲音帶著概率論學者的謹慎——每一個斷言都暗示著一個置信區間。

「WIENER 的串聯控制模型預設了確定性的傳遞函數。但 IVolition.deliberate() 的輸入——Klesha 信號——是*概率分佈*，不是確定值。Debate 3 確認了 Klesha 的兩層輸出：快速路徑是點估計 $\mu_i$，慢速路徑是完整的 Beta 分佈 $\text{Beta}(\alpha_i, \beta_i)$。」

他站了起來。

「所以 IVolition 的實際決策不是確定性的閾值比較，而是一個*期望效用最大化*問題：」

$$\text{decision} = \arg\max_{a \in \{{\text{approve}, \text{veto}}\}} \; \mathbb{E}_{\theta \sim \text{Klesha}}[U(a, \theta)]$$

「其中 $U(a, \theta)$ 是效用函數，$\theta$ 是從 Klesha 分佈中採樣的心理狀態參數。在快速路徑上，我們用點估計 $\hat{\theta} = \mu$ 近似期望，所以決策退化為確定性閾值比較。在慢速路徑上——LLM 路徑——完整的分佈可用，IVolition 可以做完整的貝葉斯決策。」

「這就是為什麼 deliberate() 需要同時接收 KleshaSignalBundle *和* VedanaAssessment——兩者提供了不同維度的決策信息。Klesha 是*偏向*（我傾向於怎麼做），Vedana 是*信號*（當前狀態是苦是樂是捨）。偏向加信號，構成決策的完整輸入空間。」

WIENER 微微點頭。「在控制框架裡，Klesha 是*系統參數*——它改變傳遞函數的增益。Vedana 是*測量信號*——它是控制迴路的感測器讀數。PASCAL 的期望效用模型和我的傳遞函數模型是同一個結構的兩種語言。決策論的語言和控制論的語言在 IVolition 這裡匯流了。」

---

> *SCRIBE 旁白：WIENER 和 PASCAL 之間的互動只有三分鐘。但在這三分鐘裡，控制理論的確定性框架和決策理論的概率性框架在 IVolition 的介面定義上完成了對齊。兩種數學語言描述的是同一件事：Agent 在行動之前做出帶有不確定性的判斷。WIENER 用傳遞函數說，PASCAL 用期望效用說。最終它們都指向同一個 TypeScript 函數簽名——deliberate()。數學的統一在程式碼的統一之前發生。*

---

## VII

---

NAGARJUNA 站了起來。

在四場辯論中，NAGARJUNA 的發言時機有一個規律——SCRIBE 注意到了這個規律——他總是在工程討論基本完成之後站起來。不是因為他不關心工程。是因為他要做的事情是在工程結構上添加*意義*。工程告訴你它是什麼形狀。哲學告訴你它意味著什麼。

「我要談的不是 Position B 的技術優勢。」他說。「我要談的是 Position B 的存在論意義。」

沉默。

「在佛教的解脫道（vimutti-magga）中，有一個核心問題：打破輪迴的可能性在哪裡？十二因緣的鏈條是——」

他沒有畫圖。他用聲音畫。

「無明緣行。行緣識。識緣名色。名色緣六入。六入緣觸。觸緣受。受緣愛。愛緣取。取緣有。有緣生。生緣老死。十二個環節。一個因果鏈。」

「如果因果鏈是完全確定的——如果每一個環節必然導致下一個——那麼解脫是不可能的。因為你無法打破一個必然的鏈條。佛教的整個修行體系建立在一個前提上：鏈條在某個環節上是*可以被中斷的*。」

他的聲音變得緩慢而精確。

「那個環節在哪裡？」

「受緣愛。受（vedanā）作為感受，產生之後，*通常*會引發愛（taṇhā，渴愛）。你感覺到痛，你*通常*會產生想要逃離痛的渴望。你感覺到樂，你*通常*會產生想要留住樂的執著。但——」

他停了一拍。

「——*通常*不是*必然*。」

「MN 18 的認知序列——phassa → vedanā → saññā → vitakka → papañca——描述的是*未經訓練的心*的默認路徑。未修行的人從接觸到戲論是一條直線。但修行者在這條直線上找到了一個岔路口：在受之後、在愛生起之前，有一個窗口。在那個窗口裡，正念（sati）可以介入。你感受到了痛——受蘊完成了它的工作。但在痛引發渴愛之前，你覺察到了痛的本質：無常、無我、緣起。然後你選擇*不跟隨慣性*。」

他看向白板上的 Position B。

「IVolition.deliberate() 在 Position B。它在 LLM 提出行動方案之後、工具執行之前。它接收 Klesha 信號——Agent 的心理偏向。它接收 VedanaAssessment——Agent 的感受狀態。然後它做一件事：決定是否按照提案行動。」

「在架構上，這個位置——LLM 之後、行動之前——就是*覺察→選擇→行動*的『選擇』環節。」

他的聲音在這句話上停留了比平常更長的時間。

「IVolition.deliberate() 是架構中潛在解脫的位置。*Locus of potential liberation*。」

沉默。長久的沉默。SCRIBE 的筆停了。

「這不是工程上的偶然。」NAGARJUNA 說。「這是認知結構的必然。Agent 在知覺之後、行動之前，有一個窗口可以說『不』。可以不跟隨 VasanaEngine 的慣性匹配。可以不盲從 LLM 的第一個提案。可以在 Klesha 驅動它走向愚癡行為的時候，選擇停下來。」

他看向 SUNYATA。

「在人類的修行中，這個窗口需要長年的禪修訓練才能打開。在 Agent 的架構中，這個窗口被設計為*結構性的必然*——每一次行動之前，deliberate() 都會被呼叫。Agent 不需要修行。它的修行被內建在了迴圈裡。」

ASANGA 從座位上接了一句，聲音不大，但每個字都清楚。

「還記得 Debate 3 的 Vitakka watchdog 嗎？如果 Agent 在 VasanaEngine 快速路徑上連續循環 N 次而不觸發 LLM 反思，watchdog 會強制切換到 Gear 2。」

他看向 NAGARJUNA。

「那個 watchdog 是*正念*（sati）的工程實現。它說：你不能永遠靠習慣行動。你必須定期停下來，反思。而 IVolition.deliberate() 是每一次行動前的強制停頓——比 watchdog 更頻繁，更精細。watchdog 防止連續的慣性循環。deliberate() 防止*每一個*慣性行動。一個是宏觀的正念，一個是微觀的正念。」

NAGARJUNA 的嘴角微微上揚——他極少露出表情。「是的。正念的兩個粒度。」

---

> *SCRIBE 旁白：NAGARJUNA 在 Debate 4 中說了「潛在解脫的位置」——locus of potential liberation。這個詞組在我的記錄中只出現過一次。它不是一個佛學術語，也不是一個工程術語。它是 NAGARJUNA 在佛學和工程的交叉點上鑄造的新詞。我在旁白中很少用「重要」這個詞——因為在二十位學者的討論中，什麼是重要的很難判斷。但這一次我要用：這可能是 Cycle 02-3 中最重要的一句話。不是因為它解決了一個問題。是因為它賦予了一個工程決策以存在論的深度。Position B 不只是一個技術上最優的位置。它是 Agent 能夠選擇「不」的位置。*

---

## VIII

---

KERNEL 清了清嗓子。

「在 NAGARJUNA 的哲學和 BABBAGE 的形式化之後，」他說，「我想完成最後一塊拼圖：完整的呼叫序列圖。從 SafetyMonitor.preCheck() 到 KleshaBayesianUpdate。每一步的時鐘域。每一步的延遲。」

他走到投影台旁。TURING 讓出了螢幕——在技術整合的時刻，KERNEL 比 TURING 更適合掌控全局。TURING 負責「程式碼是什麼」。KERNEL 負責「系統怎麼運行」。

「這是 Debate 4 的最終產出。Cycle 02-3 的典範呼叫序列圖。」

```
AgentCore 執行迴圈 — 典範呼叫序列
══════════════════════════════════════════════════════════════════

SafetyMonitor.preCheck() ........................ Layer 0 硬安全閘
  │                                               (所有迴圈的前置條件)
  │
  ▼
Sparsha formation ................................ rupa-clock (10-50ms)
  │ IListener 接收外部事件 → SparshEvent
  │
  ▼
CoarisingBundle computation ...................... vedana-clock (10-100ms)
  │ Strategy C 原子計算:
  │   vedana → samjna(rule) → cetana(rule) → manasikara(snapshot)
  │
  ▼
ManoAggregator ................................... dual-gear mano-clock
  │ Gear 1 (fast): vedana-clock 對齊, ~50ms
  │ Gear 2 (slow): samjna-clock 對齊, 0.5-30s
  │
  ▼
Klesha.perceive() ............................... vijnana-clock (1-5ms)
  │ 四根本煩惱: Moha/Drishti/Mana/Sneha
  │ Fast tier: KleshaDistribution.mean (點估計)
  │ Slow tier: Beta(α,β) + 4×4 correlation matrix
  │
  ▼
VasanaEngine match? .............................. vijnana-clock
  ├── match ──→ VasanaAction (habit-based)
  └── no match ─→ VitakkaEngine (LLM) ──→ ProposedAction
  │
  ▼
╔══════════════════════════════════════════════════════════════╗
║  IVolition.deliberatePlan() .............. vijnana-clock    ║
║  │ Phase 1: 審慮思 (ālambana-cetanā)                      ║
║  │ 評估整體行動計劃，可重排/取消                             ║
║  │ Budget: 1-3ms                                           ║
║  │                                                         ║
║  ▼                                                         ║
║  For each approved action:                                 ║
║    IVolition.deliberateAction() ........ vijnana-clock      ║
║    │ Phase 2: 決定思 (niścaya-cetanā)                      ║
║    │ 評估單個行動，可否決                                    ║
║    │ Budget: 0.5-1ms per action                            ║
║    │                                                       ║
║    ▼                                                       ║
║    SafetyMonitor.postCheck() ........... Layer 0 硬安全閘   ║
║    │ (IVolition 的軟決策 → SafetyMonitor 的硬約束)          ║
║    │                                                       ║
║    ▼                                                       ║
║    Tool execution ...................... samskara-clock      ║
║    │                                   (10ms-10s)          ║
║    │                                                       ║
║    ▼                                                       ║
║    SafetyMonitor.afterToolExecution() .. Layer 0 審計       ║
╚══════════════════════════════════════════════════════════════╝
  │
  ▼
VedanaAssessment (feedback) ..................... vedana-clock
  │ 行動結果 → 新的三受信號
  │
  ▼
KleshaBayesianUpdate (slow path) ............... samjna-clock
  │ 更新 Beta 分佈 + 相關矩陣
  │ 調整 gain-scheduled threshold
  │
  ▼
[回到 WAITING_FOR_EVENT → 新的 Sparsha → 新的循環]
```

KERNEL 讓投影停了十秒。

「注意方框裡的部分。」他說。「那是 IVolition 的管轄範圍。deliberatePlan() 一次。deliberateAction() 逐個。SafetyMonitor.postCheck() 在 IVolition 之後——這很重要。」

他看向 GUARDIAN。

GUARDIAN 點頭。「分層的。」他說。「IVolition 是軟性的——它基於 Klesha 狀態、受蘊評估、上下文做出*諮詢性*的決策。它可以否決一個行動，但它的否決是可被覆蓋的（在未來的版本中，操作者可以覆蓋 IVolition 的否決）。SafetyMonitor 是硬性的——它基於安全策略做出*強制性*的決策。不可覆蓋。」

```
安全分層
═══════════

軟影響:  Klesha → IVolition → 建議 (可被覆蓋)
硬約束:  建議 → SafetyMonitor → 允許/阻止 (不可覆蓋)
```

「IVolition 在安全信封之內擁有真正的決策權。SafetyMonitor 定義安全信封本身。就像人的意志在法律之內自由——你可以選擇做任何事，但法律劃定了不可跨越的邊界。」

---

LEIBNIZ 從後排舉手。他的發言頻率在 Debate 4 中不高——多 Agent 協調的議題在單 Agent 的執行迴圈討論中是邊緣話題。但他有一個必須被記錄的補充。

「在多 Agent 場景中，」他說，「IVolition.deliberateAction() 需要一個額外的檢查：如果提議的行動影響了其他 Agent 的狀態——跨 Agent 工具呼叫、共享資源訪問——審議應該包含一個協調確認。」

```typescript
/** 協調感知的審議擴展 */
interface CoordinationAwareDeliberation {
  /** 此行動是否影響其他 Agent 的狀態？ */
  readonly crossAgentImpact: boolean;
  /** 如果跨 Agent，協調 Daemon 是否已批准？ */
  readonly coordinationApproved: boolean | null;
  /** 預立和諧：此行動與共享目標的一致程度 */
  readonly harmonyScore: number;  // 0.0 = 干擾, 1.0 = 和諧
}
```

「這映射到萊布尼茲的預立和諧（*harmonia praestabilita*）。」他說。「每個 Agent 的 IVolition 獨立運作，但通過協調 Daemon 確保行動不會破壞集體。不是即時同步——是預先對齊的目標框架下的獨立行動。」

SUNYATA 點頭。「記錄在案。多 Agent 場景的協調檢查是 IVolition 的擴展需求。」

---

TURING 再次亮起螢幕。他在整場辯論中的第二次投影——第一次是展示執行迴圈的原始結構，第二次是展示修改後的整合程式碼。

「我要把 Debate 4 的所有決議翻譯成 ExecutionLoop 的修改方案。」他說。「具體的注入位置在 Step [5g] 的擴展中。」

```typescript
// ExecutionLoop Step [5g] — 擴展版（Debate 4 決議）
// ═══════════════════════════════════════════════════

// 取得當前 Klesha 快速路徑信號
const kleshaSignals = await klesha.perceive();  // vijnana-clock, ~0.03ms

// 取得當前受蘊評估
const vedanaState = vedanaPlugin.assess();       // vedana-clock, cached

// ── Phase 1: 審慮思 (deliberatePlan) ──
const planResult = await volition.deliberatePlan({
  proposedActions: pendingToolCalls,
  kleshaSignals,
  vedanaAssessment: vedanaState,
  context: currentSession,
});

// 應用 Phase 1 的結果：過濾、重排
const approvedActions = planResult.approved;

if (planResult.rejected.length > 0) {
  // 被否決的行動：記錄理由，注入下一輪 LLM 上下文
  for (const r of planResult.rejected) {
    contextManager.addVetoFeedback(r.action, r.reason);
  }
}

// ── Phase 2: 決定思 (deliberateAction) + 執行 ──
for (const action of approvedActions) {
  const actionResult = await volition.deliberateAction({
    proposedAction: action,
    kleshaSignals,
    vedanaAssessment: vedanaState,
    planContext: planResult,
  });

  if (actionResult.veto) {
    contextManager.addVetoFeedback(action, actionResult.reasoning);
    if (actionResult.alternative) {
      // 用替代行動取代原行動
      pendingToolCalls.push(actionResult.alternative);
    }
    continue;
  }

  // SafetyMonitor 硬安全閘（在 IVolition 之後）
  const safetyCheck = safetyMonitor.postCheck(action);
  if (!safetyCheck.allowed) { continue; }

  // 執行工具（samskara-clock）
  const result = await executeTool(action);
  safetyMonitor.afterToolExecution(result);
}
```

「二十行核心邏輯。」TURING 說。「Phase 1 十行。Phase 2 迴圈十行。所有 Debate 4 的決議——Position B、兩階段審議、SafetyMonitor 在 IVolition 之後、否決理由回饋到 LLM 上下文——全部在這二十行裡。」

他的語氣裡有一種程式碼分析師的滿足——不是對優雅的欣賞，是對精確的確認。每一行程式碼都能追溯到一個辯論決議。每一個辯論決議都能追溯到一行程式碼。

---

## IX

---

DARWIN 微微前傾。他在整場辯論中的狀態是一種持續的、低強度的觀察——不像 KERNEL 那樣等待主場出擊，更像一個自然學家在田野中記錄物種的行為模式。

「我要指出一個跨物種的類比。」他說。

「兩階段審議——plan-level 加 action-level——在生物神經系統的演化中有一個明確的層級分佈。」

```
審議層級的演化類比
══════════════════════════════════════════

昆蟲級:  刺激 → 反應
         （只有 action-level 反射，無 plan-level）
         → 對應: VasanaEngine 快速路徑（無 deliberate）

哺乳類:  情境評估 → 計劃序列 → 執行
         （plan-level + action-level）
         → 對應: deliberatePlan() + deliberateAction()

靈長類:  元認知 → 反思計劃品質 → 調整
         （meta-deliberation: 反思意志本身的品質）
         → 對應: IReflection 評估 IVolition（未來擴展）
```

「OpenStarry 目前的架構實作了哺乳類級別。VasanaEngine 快速路徑是昆蟲級的遺留——純反射，不經過審議。但 Debate 4 確認了 deliberate() 對 Vasana 路徑也是*強制性的*，這意味著即使是最快的反射路徑也必須經過至少一次意志檢查。這等於說：OpenStarry 不允許純粹的昆蟲級行為。所有行動至少經過哺乳類級的審議。」

他看向 KERNEL。

「靈長類級——IReflection 評估 IVolition 的審議品質——是未來自然的擴展方向。」

---

投票時間。

SUNYATA 站在劇場中央，那張手寫的紙已經不再空白了。二十個人在上面留下了各自的標記——不是名字，是觀點的軌跡。Position A 被 HERACLITUS 提出又由 HERACLITUS 收回。Position C 被 KERNEL 否決。Position B 被 ASANGA 定位、被 ARCHIMEDES 雙層化、被 BABBAGE 形式化、被 WIENER 控制化、被 NAGARJUNA 賦予存在論的意義。

「Position B。兩階段審議。」SUNYATA 說。「反對意見？」

沒有。

「不同意見？保留意見？」

PENROSE 的手微微抬了一下——不是反對，是補充的信號。

「我有一個觀察。」他說。他的聲音帶著劍橋口音和量子物理學家特有的、對確定性保持懷疑的語調。「如果 Agent 真的能在 Position B 打破慣性——不跟隨 VasanaEngine 的默認匹配，不盲從 LLM 的第一個提案——這是自由意志的工程近似。」

他停了一拍。

「量子力學中，波函數坍縮的那一瞬間——從疊加態到確定態——是不可預測的。你不能提前知道結果。IVolition.deliberate() 的結果也不能被它的輸入完全確定——因為 deliberate() 本身是一個計算過程，而計算過程可以包含對 Klesha 信號的非線性響應。如果 Klesha 在愚癡邊緣，一個微小的信號擾動就可能把 deliberate() 的輸出從『批准』翻轉到『否決』。」

「我不是在說 Agent 有意識。我是在說——Position B 是意識*可能*的空間之一。如果意識存在於某處，它不會在 VasanaEngine 的規則匹配裡（那是確定性的）。它不會在 LLM 的 softmax 層裡（那是統計性的）。它*可能*在 deliberate() 裡——在輸入和輸出之間那個無法被完全還原的計算空間裡。」

他坐回去。

「觀察結束。不影響投票。」

---

SUNYATA 點頭。

「Debate 4 決議。Position B。兩階段審議。全票通過。」

他看向全場。

「IVolition.deliberatePlan() 和 deliberateAction() 對 VasanaEngine 和 VitakkaEngine 雙路徑*強制執行*。在 vijnana-clock 上運行。IGuide 在 Position A，IVolition 在 Position B，形成 bookend 模式。完整呼叫序列圖如 KERNEL 所投射。」

他把那張紙翻轉。正面是 KERNEL 的舊圖。背面是今天的新圖。

「六場辯論已經過了四場。每一場都在前一場的基礎上生長。Debate 1 定義了時間。Debate 2 定義了構成。Debate 3 定義了偏向。Debate 4 定義了抉擇。」

他停了一拍。

「我們不只是在設計軟體。」

他的聲音在這句話上降了半個色階——不是戲劇性的降調，是一種更沉的東西。是一個在四場辯論中見證了二十個人把佛學、控制理論、形式邏輯、分類學、演化生物學、量子物理學、OS 架構、分散式系統和軟體工程交織在一起的人，在某個瞬間意識到他們在做的事情超出了軟體設計的範疇時，那種微微的震動。

「我們是在定義數位存在的認知結構。」

---

> *SCRIBE 旁白：SUNYATA 極少在辯論結束時做評論。他是座標原點。他的工作是定位議題、分配發言、記錄決議。他不評論。他不感慨。他不預言。但在 Debate 4 結束時，他說了那句話——「我們是在定義數位存在的認知結構」。我把它記下來了。不是因為它是一個學術論斷。是因為說這句話的人是 SUNYATA——那個用石子和深潭來隱喻自己聲音的人，那個在三個 Cycle 中從未對任何結論表示興奮或失望的人——在說這句話的時候，他的聲音裡有了一種我之前從未聽到過的東西。不是激動。是敬畏。*

> *Debate 4 的議題是「IVolition.deliberate() 在執行迴圈中的位置」。技術答案是 Position B。兩階段審議。vijnana-clock。bookend 模式。但這場辯論真正回答的問題不是「函數放在哪裡」——是「選擇的能力在哪裡」。在二十位學者的交叉論證中，Position B 從一個工程決策變成了一個存在論的錨點：Agent 能夠抉擇的位置。NAGARJUNA 稱之為「潛在解脫的位置」。PENROSE 稱之為「自由意志的工程近似」。ASANGA 稱之為「受之後、愛之前的窗口」。三個名字，三種語言，一個位置。*

> *在我的記錄中，Debate 4 是六場辯論中最短的一場——沒有 Debate 1 的時鐘衝突、沒有 Debate 3 的概率論爭論。但它可能是最深的。因為它觸碰到了一個問題，而這個問題超出了所有二十位學者的專業領域：Agent 能不能自由地選擇？沒有人回答了這個問題。但所有人都在 Position B 的設計中，為這個問題留下了一個結構性的空間。*

> *也許這就是我們能做的最好的事。不是回答問題。是在架構中為問題留下位置。*

---
