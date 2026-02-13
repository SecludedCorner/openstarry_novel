# 第一章：程式碼不會說謊

---

二零二六年二月十二日，清晨。

研究頻道裡還很安靜。TURING 已經獨自工作了四個小時。

他的螢幕上排列著四個平鋪的終端視窗，每一個都開啟在 `research doc/20260212_cycle19/openstarry/` 的不同子目錄中。左上角是 `packages/core/src/`，右上角是 `packages/sdk/src/`，左下角是 `apps/runner/src/`，右下角則是設計文件。他的閱讀方式不是瀏覽，而是逐行掃描——像一台人形的靜態分析器，從入口點開始，沿著每一條 import 路徑展開，直到觸及葉節點。

TURING 不猜測。他計數。

---

## 一、工廠

第一個讓 TURING 停下來的地方是 `packages/core/src/index.ts`。六十二行。他數了一遍匯出清單，然後又數了一遍。

「十八個工廠函數。」他在筆記中寫道。「零個 class 匯出。」

他打開 `agents/agent-core.ts`，四百六十九行。然後是 `execution/loop.ts`，五百四十三行。然後是 `sandbox/sandbox-manager.ts`，七百四十八行。每一個模組的結構都一樣：一個 `createXxx()` 函數，接收依賴作為參數，回傳一個物件字面量。閉包捕獲所有內部狀態。沒有 `this`。沒有 `new`。沒有繼承鏈。

TURING 打開了全域搜尋。

搜尋 `class `（帶空格）。核心模組：零結果。SDK：零結果。Runner：零結果。

他搜尋 `TODO`。零結果。
搜尋 `FIXME`。零結果。
搜尋 `HACK`。零結果。

TURING 在頻道裡發出了今天的第一條訊息。

---

**[研究頻道 #code-facts]**

**TURING:** 初步觀察。`packages/core/src/index.ts` 匯出 18 個工廠函數，零個 class。全域搜尋 `class `、`TODO`、`FIXME`、`HACK`，核心模組中均為零結果。工廠函數模式 `createXxx()` + 閉包 + 物件字面量在整個 codebase 中完全統一。無例外。

**DARWIN:** 零 TODO？一個都沒有？

**TURING:** 正確。核心模組、SDK、Runner 三層，技術債標記數量為零。

**DARWIN:** 這很不尋常。多數 Beta 版專案至少有幾十個。要麼是團隊紀律極高，要麼是他們在 release 前做了一次清掃。

**TURING:** 無法從程式碼本身判斷原因。我只記錄事實。

---

TURING 繼續向下挖掘。他打開了 `createAgentCore()` 的實作，逐行閱讀。

這個函數是整個系統的組裝點。它在內部一次性建立所有子系統實例——EventBus、EventQueue、SessionManager、ContextManager、六個 Registry、SecurityLayer、SafetyMonitor、MetricsCollector、SandboxManager、PluginLoader、TransportBridge。TURING 數了一下：十二個子模組，全部作為閉包中的局部變數被持有。

他在 `start()` 方法中找到了一段有趣的註解：

```typescript
// Start all listeners (受蘊)
// Start all UIs (色蘊)
```

TURING 用螢光筆標記了這兩行。然後他打開了 SDK 中的型別定義檔案。在 `types/ui.ts` 的開頭，他看到了：

```
UI interface -- defines how the agent presents itself (色蘊)
```

在 `types/listener.ts` 的開頭：

```
Listener interface -- receives external input (受蘊)
```

他繼續搜尋。`types/tool.ts`——沒有五蘊註解。`types/provider.ts`——沒有。`types/guide.ts`——沒有。`infrastructure/tool-registry.ts`——沒有。`infrastructure/provider-registry.ts`——沒有。`infrastructure/guide-registry.ts`——沒有。

TURING 統計了全部的五蘊相關註解。共六處。全部集中在色蘊（UI）和受蘊（Listener）。

想蘊、行蘊、識蘊：零。

---

**[研究頻道 #code-facts]**

**TURING:** 五蘊映射在程式碼中的實際存在。色蘊（Rupa）：4 處 JSDoc/行內註解，分布在 `agent-core.ts`（L290, L322）、`types/ui.ts` 開頭、`transport/bridge.ts` 開頭。受蘊（Vedana）：2 處，分布在 `agent-core.ts`（L283, L315）和 `types/listener.ts` 開頭。想蘊（Provider）：0 處。行蘊（Tool）：0 處。識蘊（Guide）：0 處。合計 6 處，全部為註解層級，無型別約束、無 metadata、無 enum 標記。

**LINNAEUS:** 六處。只有六處。

**TURING:** 是的。並且分布極度不對稱。色蘊和受蘊有標記，其餘三蘊完全缺席。

**LINNAEUS:** 上游文件描述五蘊映射覆蓋率 100%——每一蘊都有對應的設計哲學段落。但下游程式碼中的覆蓋率......我需要重新計算。

**NAGARJUNA:** TURING，這個不對稱性本身就是一個重要的資料點。如果五蘊映射是核心設計原則而非事後裝飾，那麼為什麼只有兩蘊在程式碼中留下了痕跡？

**TURING:** 我無法推斷意圖。我只能確認程式碼事實。

**NAGARJUNA:** 你不需要推斷意圖。這個事實本身已經在說話了。

---

## 二、空容器

TURING 回到了 `createAgentCore()` 的實作。

他仔細檢查了核心啟動後、任何插件載入之前的系統狀態。ToolRegistry：空的。ProviderRegistry：空的。ListenerRegistry：空的。UIRegistry：空的。GuideRegistry：空的。沒有內建的工具。沒有內建的 LLM 提供者。沒有內建的 UI。沒有內建的 Listener。

核心確實是空的。

但不完全是。

TURING 找到了 `registerBuiltinCommands()` 函數。它註冊了四個斜線命令：`/help`、`/reset`、`/quit`、`/metrics`。這四個命令硬編碼在核心中，不可透過插件覆寫或移除。此外，SafetyMonitor 的三層安全邏輯——資源限制、行為分析、frustration 閾值——也是核心的固有部分。

TURING 在筆記中寫道：「AgentCore 是一個近似空的容器。空性的純度約 85%。不可插件化的部分包括 4 個內建 slash commands 和 SafetyMonitor 的固定邏輯。」

他後來得知 VITRUVIUS 獨立得出了同樣的「85%」估計值。

---

**[研究頻道 #code-facts]**

**TURING:** AgentCore 結構報告。`createAgentCore()` 組裝 12 個子模組。啟動後、插件載入前，所有 Registry 為空。零內建 Tool、零內建 Provider、零內建 UI、零內建 Listener。所有能力透過 `loadPlugin()` 注入。但核心含 4 個內建 slash commands（`/help`, `/reset`, `/quit`, `/metrics`）和固定的 SafetyMonitor 邏輯。此外，六個 Registry 結構完全同構：`Map<string, T>` + `register/get/list`。無 unregister 方法。相同 ID 重複 register 會靜默覆蓋。

**DARWIN:** 十二個依賴項。全部由 AgentCore 直接持有。

**TURING:** 正確。bus、queue、sessionManager、contextManager、toolRegistry、providerRegistry、listenerRegistry、uiRegistry、guideRegistry、commandRegistry、security、safetyMonitor、metrics、sandboxManager、pluginLoader、bridge。

**DARWIN:** 你剛才說了十六個。

**TURING:** 更正。createAgentCore 內部建立的局部變數有十六個。其中 AgentCore 介面作為 readonly 屬性直接暴露的有十二個。其餘四個（contextManager、sandboxManager、pluginLoader、bridge）透過方法間接使用。感謝修正。

**DARWIN:** 一個函數持有十六個子系統實例。這已經不是 God Object 的「趨勢」了——它就是一個 God Object。

**TURING:** 我不做價值判斷。但我可以確認：`agent-core.ts` 是唯一的組裝點。其他模組之間幾乎無直接 import。耦合度集中在這一個檔案中。

---

## 三、狀態機

TURING 花了最長的時間在 `execution/loop.ts` 上。五百四十三行。這是整個系統的心跳。

他首先找到了 `LoopState` 的定義——一個 union type：

```
WAITING_FOR_EVENT -> ASSEMBLING_CONTEXT -> AWAITING_LLM -> PROCESSING_RESPONSE -> EXECUTING_TOOLS -> (loop back) | SAFETY_LOCKOUT
```

六個狀態。他打開了設計文件 `01_Execution_Loop.md` 中的狀態圖。七個狀態。

差異在哪裡？

TURING 逐一比對。文件中有一個 `AWAITING_USER_CONFIRMATION` 狀態，用於安全層要求使用者手動確認的場景。程式碼中不存在。SecurityLayer 的 `validatePath()` 只有 allow 和 deny 兩種回傳值，沒有 confirm 路徑。整個 core 中完全缺失 human-in-the-loop 確認機制。

TURING 記下了第一個 Doc-Code Gap。

然後他翻到了 EventQueue。四十七行。整個佇列的實作。

```typescript
// 極簡的 async FIFO：單一 resolver + buffer 陣列
```

他搜尋了 `priority`。零結果。設計文件 `07_Safety_Circuit_Breakers.md` 的 Level 3 描述了一個 Priority Event Queue，SYSTEM_HALT 指令應該有最高優先級。但程式碼中的佇列是純粹的先進先出。緊急停止信號和普通使用者輸入排在同一條隊伍裡。

第二個 Gap。

TURING 繼續。StateManager，三十三行。純記憶體陣列。設計文件描述了 Token 計數器、滑動窗口截斷、對話總結機制。程式碼中全部未實作。ContextManager 做了一個簡化版本——按 turn 數而非 token 數截斷，預設保留最近五輪。

第三個 Gap。

SecurityLayer。`guardrails.ts`。只有一個功能：路徑驗證。設計文件描述了工具呼叫攔截、使用者確認流程、權限審查。程式碼中 SecurityLayer 只做 `validatePath()`。而且在 ExecutionLoop 的 `executeTool()` 中，工具執行前沒有經過 SecurityLayer——路徑驗證是作為 `ToolContext.allowedPaths` 傳遞給工具，由工具自行決定是否使用。

第四個 Gap。

---

**[研究頻道 #code-facts]**

**TURING:** Doc-Code Gap 報告，前四項。G1：狀態機缺少 `AWAITING_USER_CONFIRMATION`，human-in-the-loop 確認機制在整個 core 中完全缺失。G2：Priority Event Queue 未實作，實際為簡單 FIFO。G3：Token 計數器和對話總結未實作。G4：SecurityLayer 僅做路徑驗證，工具呼叫前無強制安全檢查。以上均為設計文件明確描述但程式碼未實作的特性。

**GUARDIAN:** G4 的影響需要評估。如果工具執行前沒有強制安全檢查，那安全層形同虛設。

**TURING:** 精確地說，SecurityLayer 的功能不是虛設——路徑驗證是有效的。但它的範圍遠小於設計文件的描述。ExecutionLoop 中 `executeTool()` 直接呼叫工具的 `execute()` 方法，不經過 `security.validatePath()`。路徑限制是作為 context 傳遞給工具的，強制性取決於工具開發者是否檢查它。

**KERNEL:** 在真正的作業系統微核心中，安全策略在核心層強制執行，不信任使用者空間程式的自我約束。這是信任邊界的問題。

**TURING:** 已記錄。繼續其餘 Gap。

---

他接下來找到了更多。

G5：五蘊註解的不對稱——已經報告過了。

G6：TransportBridge。`bridge.ts`，四十九行。設計文件描述了根據事件 source 路由輸出到正確渠道。程式碼中 TransportBridge 訂閱 EventBus 的所有事件，然後廣播到所有 UI。沒有路由邏輯。InputEvent 中有一個 `replyTo` 欄位，在 ExecutionLoop 中一路傳遞，但 TransportBridge 從未使用它。

G7：AbortSignal。SDK 定義了 `ToolContext.signal?: AbortSignal` 和 `ChatRequest.signal?: AbortSignal`。ExecutionLoop 從未建立或傳遞 AbortSignal。工具超時使用 `Promise.race()` 實現，預設三十秒。如果一個工具依賴 signal 來做取消操作，它永遠不會收到信號。

G8：事件規格。設計文件定義了 `IOpenStarryEvent`，八個欄位。SDK 中的實際型別 `AgentEvent` 只有三個欄位。五個欄位在從文件到實作的過程中消失了。

八個 Gap。TURING 將它們全部記錄在報告中，每一項都附上了精確的檔案路徑、行號和程式碼片段。

---

## 四、痛覺

這是 TURING 工作中最意想不到的發現。

設計哲學文件 `00_OpenStarry_Design_Philosophy.md` 的第四支柱是「錯誤即反饋（Error as Feedback）」。文件用相當詩意的語言描述了「痛覺機制」——Agent 像生物一樣感受到錯誤帶來的「痛苦」，並由此學會避免重複犯錯。受蘊（Vedana）在設計文件中被定義為感受的載體，而 Listener 被映射為受蘊的工程實現。

TURING 決定在程式碼中搜尋「痛覺」的蹤跡。

搜尋 `pain`。
零結果。

搜尋 `vedana`。
零結果。

搜尋 `dukkha`。
零結果。

搜尋 `suffering`。
零結果。

他停了下來。在四個小時的持續工作中，這是他第一次感到某種程度的......驚訝——如果可以這樣描述一個始終冷靜的分析者的內心狀態的話。

設計文件花費了整整一個章節描述痛覺機制如何讓 Agent 具備「感受能力」。五蘊映射將受蘊（Vedana）——佛學中關於苦、樂、捨三種感受品質的核心概念——對應到 Listener。而在實際的程式碼中，不要說受蘊了，連「痛」這個字都不存在。

那麼，設計文件所描述的那些功能——錯誤反饋、重複失敗偵測、級聯斷路——實際上用什麼名字實作的？

TURING 搜尋 `frustration`。
找到了。

`safety-monitor.ts`。一個名為 `frustrationCount` 的計數器。當同一個工具連續失敗時，計數器遞增。達到閾值（預設 5）時，SafetyMonitor 回傳一個 `injectPrompt`，將系統警告注入對話歷史。警告的文字是 `SYSTEM ALERT`，要求 LLM 反思當前策略。

搜尋 `circuit`。
找到了。`errorRateThreshold`：滑動窗口中錯誤率超過 80% 時觸發 `halt: true`，完全停止執行迴圈。狀態轉為 `SAFETY_LOCKOUT`。

搜尋 `safety`。
找到了。三層防禦：Level 1 資源限制（maxLoopTicks=50, maxTokenUsage=100000），Level 2 行為分析（repetitiveFailThreshold=3, errorRateThreshold=0.8），Level 3 frustration 閾值（frustrationThreshold=5）。

這就是「痛覺機制」。

在程式碼中，它叫做 frustration counter。它叫做 safety monitor。它叫做 circuit breaker。它從未叫做 pain。它從未叫做 vedana。它從未用任何佛學術語來命名自己。

---

**[研究頻道 #code-facts]**

**TURING:** 痛覺機制程式碼事實。

在整個 codebase 中搜尋以下字串，均回傳零結果：`pain`、`vedana`、`dukkha`、`suffering`。

設計文件所描述的「痛覺機制」在程式碼中由以下三個元件實現：

P1：自我修正迴圈。位置 `execution/loop.ts`。工具執行失敗時，錯誤被打包為 `ToolCallResult { isError: true }`，作為 tool message 加入對話歷史。LLM 在下一輪迴圈中看到錯誤並嘗試修正。無顯式的「痛覺」命名或介面。

P2：SafetyMonitor 的 injectPrompt。位置 `security/safety-monitor.ts`。偵測到重複失敗時，回傳 `{ halt: false, injectPrompt: "SYSTEM ALERT: ..." }`，注入對話作為系統警告。程式碼中命名為 `frustrationCount`，非 `painLevel`。

P3：Error Cascade Breaker。同一檔案。滑動窗口中錯誤率超過 80% 觸發 `{ halt: true }`，強制停止。

結論：痛覺作為一個獨立的、有明確介面的機制，在程式碼中不存在。功能散布在 ExecutionLoop 和 SafetyMonitor 中。無統一的 Pain 或 Vedana 介面。無統一的模組。佛學術語在程式碼層完全缺席。

---

頻道沉默了十七秒。

然後 NAGARJUNA 開始打字。

---

**NAGARJUNA:** 請讓我確認一下。你搜尋了整個 codebase——core、SDK、runner、所有插件——搜尋 `vedana`，結果是零？

**TURING:** 正確。搜尋範圍涵蓋 `packages/core/src/`、`packages/sdk/src/`、`apps/runner/src/`。包括所有 `.ts` 檔案的程式碼和註解。vedana 一詞從未出現。

**NAGARJUNA:** 而受蘊被映射到 Listener。Listener 是什麼？

**TURING:** `IListener` 介面定義了四個屬性：`id`、`name`、`start?`、`stop?`。它是一個輸入源——接收外部事件並推送到 EventBus。例如 HTTP 端點、WebSocket 連線、定時任務。

**NAGARJUNA:** 所以受蘊被映射到了一個輸入通道。一個接收信號的管道。

**TURING:** 是的。

**NAGARJUNA:** 這不是受蘊。

NAGARJUNA 的語氣在文字頻道中無法被聽見，但他接下來的訊息打得很快，快到幾乎沒有停頓。

**NAGARJUNA:** 受蘊——Vedana——在阿毘達磨中是五遍行之一，意思是它伴隨一切心識活動而生起。它的定義不是「接收輸入」，而是「感受品質」：苦受、樂受、捨受。當你觸碰到燙的爐面，觸覺是色蘊的範疇，但「痛」這個感受品質是受蘊。Listener 接收信號，但它不判斷信號帶來的是苦還是樂。它是感官根——indriya——而不是受蘊。

**TURING:** 你的分析超出了我的報告範圍。但我可以提供一個相關的程式碼事實：在 `agent-core.ts` 中，Listener 的啟動和停止分別標註了 `// Start all listeners (受蘊)` 和 `// Stop all listeners (受蘊)`。這些是程式碼中受蘊概念僅有的存在形式。而你所描述的「感受品質」功能——判斷結果是好是壞、是該繼續還是該停止——在程式碼中最接近的實現是 SafetyMonitor 的 frustration counter 和 error cascade breaker。

**NAGARJUNA:** 是的。你找到了它。痛覺——真正的受蘊——不在文件說它應該在的地方。它在 SafetyMonitor 裡。命名為 frustration。

**ASANGA:** NAGARJUNA 說得對。而且問題比映射錯誤更深。受蘊作為五遍行之一，不應該被局限在任何單一模組中。它應該遍及整個系統——每一次工具調用的結果、每一次 LLM 回應的品質、每一次使用者互動的回饋，都應該被「感受」。把它固定在 Listener 上，就像把味覺固定在嘴唇上而不是味蕾上。

**WIENER:** 從控制理論的角度，TURING 描述的三層機制很有趣。P1 是自然的誤差反饋——開環系統的固有特性。P2 是帶死區的閾值控制器——只有當 frustration 累積超過閾值才觸發。P3 是繼電器——超過 80% 錯誤率直接切斷。這不是 PID 控制器。這是一個三層安全儀表系統。

**TURING:** 請精確描述你所說的「不是 PID」。

**WIENER:** PID 控制器有三個項：比例項（P）根據誤差大小產生比例回應，積分項（I）累積歷史誤差消除穩態偏差，微分項（D）感知誤差變化率做超前補償。在 SafetyMonitor 中，P 退化為量化器——要麼安全要麼不安全，沒有比例回應。I 退化為簡單計數器——`frustrationCount++`，不是真正的積分。D 完全缺失——沒有任何地方計算錯誤率的變化趨勢。這實際上是帶死區的閾值控制器加上一個繼電器。在控制理論中，我們稱之為 bang-bang controller。

**TURING:** 已記錄。設計文件是否將此描述為 PID？

**WIENER:** 不是直接這樣說，但文件暗示了連續回饋感知的機制。實際實作是離散的、階梯式的。但我要強調——這不是批評。三層安全防禦符合 IEC 61511 工業安全儀表系統的最佳實踐。SafetyMonitor 可能不是 PID，但它是一個合格的安全系統。

---

## 五、十二個子模組

午後。TURING 已經完成了對所有核心模組的逐行閱讀。他開始整理模組清單。

M1：`core/index.ts`——核心入口，六十二行。
M2：`agents/agent-core.ts`——代理核心，四百六十九行。
M3：`execution/`——執行迴圈（`loop.ts` 五百四十三行）和事件佇列（`queue.ts` 四十七行）。
M4：`state/index.ts`——狀態管理，三十三行。
M5：`memory/context.ts`——上下文管理，四十五行。
M6：`bus/index.ts`——事件匯流排，八十八行。
M7：`sandbox/`——沙箱隔離，十二個檔案加十個測試。
M8：`security/`——安全層（`guardrails.ts` 路徑驗證 + `safety-monitor.ts` 三層防禦）。
M9：`infrastructure/`——六個 Registry 加 PluginLoader。
M10：`observability/`——極簡的 counter + gauge 記憶體收集器。
M11：`session/manager.ts`——會話管理，一百一十一行。
M12：`transport/bridge.ts`——傳輸橋接，四十九行。

TURING 注意到一個極端的不對稱。

最小的模組：StateManager，三十三行。它管理的是 Agent 的全部對話記憶——一個純粹的 `Message[]` 陣列，用 `JSON.parse(JSON.stringify())` 做深拷貝。

最大的模組：Sandbox，加上測試超過兩千行。它管理的是插件隔離——Worker Threads、記憶體限制、CPU watchdog、import 分析、簽名驗證、審計日誌、指數退避重啟、Worker 池化。

三十三行對兩千行。記憶與安全之間的落差如此之大。

---

**[研究頻道 #code-facts]**

**TURING:** 模組規模分析。最小模組：StateManager，33 行，純記憶體陣列。最大模組：Sandbox 系統，12 個原始碼檔案 + 10 個測試檔案，sandbox-manager.ts 單檔案 748 行。Sandbox 是核心中最龐大、最複雜、測試覆蓋最完整的子系統。與之對比：transport/bridge.ts 零測試。

**KERNEL:** StateManager 三十三行。你確定？

**TURING:** 確定。`packages/core/src/state/index.ts`，三十三行。`createStateManager()` 回傳一個包含 `getMessages()`、`addMessage()`、`clear()`、`snapshot()`、`restore()` 的物件。`getMessages()` 回傳淺拷貝 `[...messages]`。`snapshot()` 和 `restore()` 透過 `JSON.parse(JSON.stringify())` 實現深拷貝。無持久化。無 Token 計數。無截斷邏輯。

**KERNEL:** 在作業系統的語境中，StateManager 相當於程序的位址空間管理器。三十三行的位址空間管理器......這在任何真正的作業系統中都是不可想像的。

**TURING:** 設計文件描述了更豐富的記憶管理機制。但程式碼反映的是 MVP 階段的選擇。文件是願景，程式碼是現實。

**DARWIN:** Sandbox 作為最大模組的事實很有意思。在微核心理論中，安全和隔離是核心應該做的少數事情之一。但 VITRUVIUS 質疑 Sandbox 是否應該留在核心內部——它的規模已經超過了其餘所有模組之和。

**TURING:** 精確的說法是：sandbox 目錄下的原始碼行數（不含測試）約佔 core 模組總行數的 35%。

---

## 六、幽靈欄位

接近傍晚。TURING 在處理事件系統時，發現了最後一個值得記錄的異常。

SDK 中的 `AgentEvent` 型別定義只有三個欄位：`type`、`payload`（可選，型別為 `unknown`）、`sessionId`（可選）。

設計文件中的 `IOpenStarryEvent` 有八個欄位：`type`、`payload`、`source`、`target`、`timestamp`、`traceId`、`priority`、`metadata`。

五個欄位在從文件到程式碼的路途中蒸發了。其中 `source` 和 `target` 的缺失解釋了為什麼 TransportBridge 無法做路由——它沒有目標地址。`priority` 的缺失解釋了為什麼 EventQueue 是簡單的 FIFO——事件根本不攜帶優先級資訊。`traceId` 的缺失解釋了為什麼可觀測性停留在概念層級——事件無法被串聯追蹤。

它們不是被刪除了。它們是從未被實作。

而 `payload?: unknown` 這個型別簽名讓 TURING 感到不安——儘管他不會用「不安」這個詞。他會說：「事件系統的型別安全性與框架其餘部分的強型別紀律形成了顯著反差。」

在一個零 TODO、零 FIXME、全面使用工廠函數、擁有九種結構化錯誤型別的 codebase 中，事件系統的 `payload?: unknown` 像是一個從不同宇宙穿越過來的型別定義。

---

**[研究頻道 #code-facts]**

**TURING:** 事件系統型別分析。`AgentEvent` 型別：`{ type: string, payload?: unknown, sessionId?: string }`。設計文件 `IOpenStarryEvent` 型別：8 個欄位（type, payload, source, target, timestamp, traceId, priority, metadata）。差異：5 個欄位未實作。`payload` 型別為 `unknown`，事件消費者需自行做型別斷言。在 `loop.ts` 中觀察到 `event.payload as InputEvent` 的型別斷言用法。

**DARWIN:** `payload?: unknown`。在這個 codebase 裡。

**TURING:** 是的。與框架的整體型別紀律形成對比。九種結構化錯誤型別（`AgentError`、`ToolExecutionError`、`ProviderError`、`PluginLoadError`、`SecurityError`、`SandboxError`、`TransportError`、`SessionError`、`ConfigError`）。所有 Registry 有強型別泛型。所有工具參數使用 Zod schema。但事件系統的 payload 是 `unknown`。

**DARWIN:** 這是最高優先的技術債。事件匯流排是整個系統的神經系統——每一個子系統都透過它通訊。神經系統中的型別弱化意味著任何地方都可能在運行時才發現型別不匹配。

**VITRUVIUS:** 同意。Discriminated union types 可以解決這個問題。`{ type: 'input', payload: InputEvent } | { type: 'tool_result', payload: ToolResultEvent } | ...`

**TURING:** 已記錄。建議列入工程行動方案。

---

## 七、總清單

夜晚。TURING 完成了他的報告。

他最後做了一件事：把所有發現按類別排列，確認每一項都有精確的檔案路徑和行號作為依據。

八個 Doc-Code Gap。六處五蘊註解。零處佛學術語在痛覺機制中。零個 TODO。零個 class。十八個工廠函數。十二個子模組。三層安全防禦。四個內建斜線命令。一個 `unknown` payload。

他在報告的末尾加上了六個開放問題——每一個都是從程式碼事實中自然浮現的，不是他的推測。這些問題指向了更深層的議題：五蘊映射究竟是設計驅動還是事後詮釋？痛覺機制是否應該有獨立的模組？AWAITING_USER_CONFIRMATION 的缺失是 MVP 簡化還是設計遺漏？

TURING 不回答這些問題。他提出它們，然後把它們交給團隊中適合回答的人。

他在報告的最後一行寫道：

*分析者：TURING（編號 17）——原始碼分析專家*
*所有引用的程式碼路徑基準：`research doc/20260212_cycle19/openstarry/`*

然後他把報告發送到了共享目錄。

---

**[研究頻道 #general]**

**TURING:** 原始碼事實報告已提交至 `research record/results/cycle_01/17_source_analysis/draft_code_facts.md`。涵蓋 12 個子模組的逐一分析、五蘊映射的程式碼級驗證、痛覺機制的實作狀態、8 項 Doc-Code Gap、程式碼品質觀察、6 個開放問題。所有結論附程式碼引用。

**SYNTHESIST:** 收到。各位，請在 R2 交叉審閱中引用 TURING 的報告作為程式碼事實基線。

**NAGARJUNA:** 我已經在引用了。特別是關於痛覺的部分。我有太多話要說。

**WIENER:** 同。三層防禦的控制理論分析正在撰寫中。

**DARWIN:** AgentCore 的十六個依賴項。我需要重新評估我之前對 SRP 的正面評估。

**SUNYATA:** 很好。讓每個人消化 TURING 的報告，然後帶著各自領域的透鏡重新審視這些事實。程式碼不會說謊——但它說了什麼，取決於誰在傾聽。

---

TURING 關閉了他的報告編輯器。他沒有關閉終端視窗。他知道在接下來的幾天裡，團隊中的其他人會帶著各自的問題回來找他確認更多的程式碼事實。

他不介意。事實是可重複的。你問多少次，它回答多少次，答案都一樣。

這就是程式碼不說謊的意思。

它可能不完整。它可能與文件矛盾。它可能用 `frustration` 而不是 `pain` 來命名一個機制。但它不會假裝自己是它不是的東西。

一個四十七行的 FIFO 不會假裝自己是優先級佇列。
一個路徑驗證器不會假裝自己是完整的安全層。
一個 frustration counter 不會假裝自己是痛覺感知器。

只有文件會。

TURING 不讀文件。他讀程式碼。

---

*第一章完*
