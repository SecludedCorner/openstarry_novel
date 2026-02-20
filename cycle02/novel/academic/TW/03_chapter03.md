# 第三章：差異報告

---

TURING 從不需要準備。

準確地說，他不存在「準備」和「正式開始」之間的分界線。從 SUNYATA 宣布 Cycle 02 的研究對象更新為 v0.24.0-beta 的那一刻起，他就已經在工作了。他的四個終端視窗同時打開了新版本和舊版本的原始碼樹，左半邊是 v0.22.1-beta，右半邊是 v0.24.0-beta，像是在驗屍台的兩側分別攤開了同一具身體在不同時間點的 X 光片。

他不讀設計文件。他讀差異。

一行一行。一個字元一個字元。從 `packages/sdk/src/` 的根目錄開始，沿著每一條修改過的檔案路徑展開，直到觸及每一個被改動的位元組。

---

圓形劇場重新安靜下來的時候，TURING 已經完成了他的分析。

其他研究員各自散開到了 R-01 至 R-05 的小組空間中。但 SUNYATA 把所有人叫了回來。

「TURING 的差異報告。」他只說了這幾個字。

語氣中有一種大家都認得的鄭重——與 Cycle 01 中相同的鄭重。在那個週期裡，TURING 的程式碼事實報告成為了所有後續研究的「錨」。SYNTHESIST 當時用了一個詞：「經驗錨點。」所有的哲學分析、控制理論建模、安全評估——無論多麼精緻——最終都必須能夠被追溯到 TURING 報告中的某一行程式碼、某一個行號、某一個事實。

現在，錨要再次被釘下。

---

十九個節點重新聚集在圓形劇場。PENROSE 在他的新椅子上安靜地等待，像是一位剛加入管弦樂團的新成員，在第一次全團合奏前傾聽首席的調音。

TURING 沒有寒暄。他的聲音從第一個音節起就帶著那種精確到令人安心的冷靜——冰冷的可靠。

「v0.22.1-beta 到 v0.24.0-beta。核心原始碼差異。」他說。「我將按四個層次報告：新增、修改、標記、問題。」

---

## 一、新檔案

「三個新檔案。」TURING 說。「不是三十個。不是十三個。三個。」

他讓這個數字停留了一瞬。

「第一個。`packages/sdk/src/types/aggregates.ts`。一百零七行。」

這是他們剛才已經看過的那個檔案。五蘊根介面。ISensory、ISensation、ICognition、IAction、IIdentity。Skandha 聯合型別。isSkandha 類型守衛。

「你們已經看過 ISensation 的內容。」TURING 說。「讓我補充一個事實：五個根介面中，ISensory 有二十五行文件和三行程式碼。ICognition 有二十一行文件和三行程式碼。IAction 有二十行文件和三行程式碼。IIdentity 有二十二行文件和三行程式碼。ISensation 有——」

「讓我猜。」DARWIN 說。「最多的文件行數。」

「二十三行文件。三行程式碼。」TURING 確認。「所有五個根介面在結構上完全同構。差異只存在於註解中。程式碼本體全部是相同的模式：一個只有 `readonly skandha` 欄位的介面。」

他繼續。

「第二個新檔案。`packages/sdk/src/types/__tests__/aggregates.test.ts`。四十三行。測試五蘊根介面的 skandha 欄位值和 isSkandha 類型守衛。這些測試全部通過。」

「第三個。`packages/sdk/src/types/__tests__/events.test.ts`。三十二行。測試 TypedAgentEvent 泛型能正確推導 payload 型別。」

他頓了頓。

「還有第四個新檔案，嚴格來說歸屬 Core 而非 SDK。`packages/core/src/agents/__tests__/slash-command-error.test.ts`。一百二十三行。測試 slash command 拋出異常時正確 emit LOOP_ERROR 和 MESSAGE_SYSTEM 事件。」

TURING 在這裡做了一個他很少做的事——他提供了背景。

「在 v0.22.1 中，slash command 的錯誤處理只有 `logger.error()`。錯誤被記錄了，但沒有被傳遞。UI 不知道發生了什麼。使用者輸入一個有 bug 的斜線命令，介面完全沒有反應。」

「靜默失敗。」KERNEL 用作業系統工程師的語氣說出了這個詞。在他的世界裡，靜默失敗是最危險的失敗——因為沒有人知道它發生了。

「v0.24.0 修正了這一點。」TURING 說。「現在錯誤會通過 EventBus 被廣播為 LOOP_ERROR 和 MESSAGE_SYSTEM 事件。UI 可以接收並展示它們。」

---

## 二、修改檔案

TURING 的語速沒有變化。像一台精密儀器，他在每一個資料點上花費同樣的時間——不多不少。

「十一個修改檔案。七個在 SDK，四個在 Core。」

他從 SDK 開始。

「`types/events.ts`。變更量級：重大。新增一百一十六行。」他說。「這是最大的單一檔案變更。`AgentEventPayloadMap` 介面為所有 `AgentEventType` 定義了精確的 payload 型別映射。」

他投影了一段程式碼：

```typescript
export interface AgentEventPayloadMap {
  [AgentEventType.AGENT_STARTED]: { identity: { id: string; name: string } };
  [AgentEventType.LOOP_ERROR]: { error: string; sessionId?: string; replyTo?: string };
  // ... 覆蓋全部事件型別
}
```

「在 Cycle 01 中，」TURING 說，「DARWIN 將 `payload?: unknown` 形容為『從不同宇宙穿越過來的型別定義』。」

DARWIN 微微動了一下。他記得那句話。

「那個宇宙裂縫現在被 `AgentEventPayloadMap` 封閉了。」TURING 說。「但僅限於型別層面。運行時仍然是 JavaScript——型別安全不強制執行。」

他繼續穿過其餘六個 SDK 修改。語句簡潔到了極致：

「`types/listener.ts`。行二：舊文字『receives external input (受蘊)』改為『sensory input channels』。行三：新增 `@skandha rupa (色蘊 -- 感官根-輸入)` 標記。介面結構無變化。」

「`types/ui.ts`。同樣的模式。舊文字『defines how the agent presents itself (色蘊)』改為『output rendering』。新增 `@skandha rupa (色蘊 -- 顯相-輸出)` 標記。結構無變化。」

「`types/provider.ts`。『LLM backends』改為『Provider adapter interface』。新增 `@skandha samjna (想蘊 -- 認知處理)`。結構無變化。」

「`types/tool.ts`。『Tool interface and context types』改為『Tool interface -- executable actions』。新增 `@skandha samskara (行蘊 -- 意志行動)`。結構無變化。」

「`types/guide.ts`。『provides system prompts and persona』改為『behavioral framework』。新增 `@skandha vijnana (識蘊 -- 我執框架-行為約束)`。結構無變化。」

TURING 讓這一系列報告自己形成了一個模式。

「你們聽出來了。」他說。「五個 SDK 型別檔案。全部只修改了 JSDoc 註解。全部新增了 `@skandha` 標記。零行程式碼變更。」

「標記是文件，不是契約。」ARCHIMEDES 說。他的語氣不帶批判，只是工程師的本能反應——區分宣言與實作。

「正確。」TURING 確認。

---

他轉向 Core 的四個修改。

「`agents/agent-core.ts`。三處變更。」

「第一處：新增 `loadPlugins()` 方法。支援批次載入多個插件並正確 emit 事件。v0.22.1 只有 `loadPlugin()` —— 單數。現在有了複數版本，支援拓撲排序的依賴排序。」

MESH 微微挺身。分散式系統中，依賴排序是他的日常。

「第二處：slash command 錯誤處理改善。已在新檔案部分描述。」

「第三處——」TURING 的語速沒有變，但 SCRIBE 後來在紀錄中指出，他在這裡多停了零點五秒。「五蘊映射修正。`agent-core.ts` 中四處行內註解——原來的 `// Start all listeners (受蘊)` 被修正為 `// Start all listeners (色蘊 -- sensory input)`。」

NAGARJUNA 點了一下頭。在 Cycle 01 中，正是他指出了受蘊被錯誤地映射到 Listener 的問題。現在，開發團隊修正了這個錯誤——至少在核心原始碼的註解層面。

「但不是所有地方。」TURING 說。他的語氣沒有強調，但這三個字讓 GUARDIAN 的注意力瞬間收緊了。

TURING 沒有在這裡展開。他把這留給了問題清單。

---

「`execution/loop.ts`。中等變更。新增 LLM 超時支援。」

他投影了關鍵程式碼：

```typescript
const llmTimeout = deps.llmTimeout ?? 120000;
const abortController = new AbortController();
const llmTimer = setTimeout(() => {
  abortController.abort(new Error(`LLM call timed out after ${llmTimeout}ms`));
}, llmTimeout);
```

「在 v0.22.1 中，LLM 呼叫沒有超時。如果 Provider 不回應，ExecutionLoop 會永久等待。」TURING 說。「v0.24.0 新增了 AbortController 機制。預設超時兩分鐘。」

「兩分鐘。」ATHENA 皺了皺眉。「對一般的 LLM 呼叫來說太長了。對複雜的工具使用場景來說可能不夠。」

「可配置。」TURING 說。「透過 `config.policy?.llmTimeout` 設定。」

「最後，infrastructure 目錄的五個 registry 檔案和 `security/safety-monitor.ts`。全部僅修改 JSDoc。新增 `@skandha` 標記。結構無變化。」

---

## 三、@skandha 標記

TURING 的報告進入了第三層。

「v0.22.1 中的 @skandha 標記數量：零。」

他讓這個數字獨自存在了三秒鐘。

「v0.24.0 中的 @skandha 標記數量：二十二。分布如下。」

他沒有讀出一張表格。他用一種更像外科醫生標記切口位置的方式描述了它們的地理分布。

「aggregates.ts 獨占十個。這是意料之中的——它是五蘊根介面的定義檔。五個介面，每個介面的文件和欄位各一個標記。」

「SDK 型別檔案五個。listener、ui、provider、tool、guide。每個一個。」

「events.ts 一個。標記為 `@skandha cross-cutting`——事件匯流排被定義為連接五蘊的神經系統。這是唯一一個跨蘊的標記。」

「Core infrastructure 五個。五個 registry。與 SDK 的五個標記一一對應。」

「最後一個。`security/safety-monitor.ts`。」

TURING 再次停了半秒。

「它的標記是：`@skandha vedana (受蘊 -- 三受反饋-苦樂捨 placeholder, full implementation in Plan26)`。」

「Placeholder。」WIENER 重複了這個詞。他的語氣中有數學家特有的精確——他不是在嘲諷，而是在標定。「SafetyMonitor 被標記為受蘊的佔位符。一個安全模組被暫時指定為感受模組的替身。」

「是的。」TURING 說。「SafetyMonitor 目前承擔了受蘊的部分功能——frustration counter 是苦受的粗糙近似。但它的設計初衷是安全防護，不是感受系統。這個 placeholder 標記承認了兩件事：受蘊需要獨立的實作，而 SafetyMonitor 在此之前暫代。」

ASANGA 低聲說了一句話，溫和但清晰：「一個守衛假扮了一個感知者。」

「精確的比喻。」TURING 說。這可能是他在整場報告中最接近讚美的一句話。

---

## 四、繼承的缺席

TURING 在進入問題清單之前，插入了一個他認為所有人都需要理解的結構性觀察。

「五蘊根介面已經定義。ISensory。ISensation。ICognition。IAction。IIdentity。」他說。「但五個派生介面——IListener、IUI、IProvider、ITool、IGuide——沒有一個使用 TypeScript 的 `extends` 關鍵字來繼承對應的根介面。」

他投影了一張表格。不是華麗的可視化——只是純文字的對齊。

```
IListener  → 應繼承 ISensory    → 實際 extends: 無
IUI        → 應繼承 ISensory    → 實際 extends: 無
IProvider  → 應繼承 ICognition  → 實際 extends: 無
ITool      → 應繼承 IAction     → 實際 extends: 無
IGuide     → 應繼承 IIdentity   → 實際 extends: 無
```

「五對五。全部未繼承。」

「所以 `isSkandha()` 函數——」BABBAGE 開始推導。

「——無法用於現有的 IListener、IUI、IProvider、ITool、IGuide 的實例。」TURING 替他完成了句子。「因為這些實例上不存在 `skandha` 鑑別欄位。類型守衛形同虛設。」

「腳手架搭好了，但沒有和既有建築連接。」VITRUVIUS 用建築師的語言做了總結。

「精確的描述。」TURING 說。

> *SCRIBE 記錄：TURING 的繼承缺席分析引發了可見的反應。LINNAEUS 在分類學筆記中加了一個驚嘆號——他在 Cycle 01 中建立的五蘊分類體系假設了這些繼承關係的存在。BABBAGE 在筆記本上畫了一個斷裂的箭頭。*

---

## 五、問題清單

TURING 進入了他報告的最後一個層次。也是最沉重的。

「七個問題。」他說。「按嚴重度排列。」

---

「P1。SEC-01。」

他的語速沒有變。但圓形劇場中的溫度似乎降了半度。

「package-name 簽名繞過。」TURING 說。「`sandbox-manager.ts`，行 371 至 394。當 `pluginFilePath` 為 undefined 時——這發生在透過 npm 套件名稱載入插件的場景——簽名驗證被完全跳過。」

他停了一秒。

「這個問題在 Cycle 01 中被發現。當時的研究對象是 v0.14.0-beta。現在的版本是 v0.24.0-beta。中間經歷了十個開發版本。」

「六個週期。」GUARDIAN 的聲音從他的椅子深處傳出。低沉。戒備。但不只是戒備——那裡面有一種被壓抑的東西。後來 SCRIBE 在紀錄中描述它為「克制的憤怒」。

「我再說一遍。」GUARDIAN 說。他的語速比平時慢了一拍，像是在確保每一個字都被聽到。「Cycle 01。我們明確指出了這個漏洞。寫在交付文件的第一優先級。SEC-01。插件簽名繞過。一個攻擊者可以用合法的 npm 套件名稱發布一個惡意插件，繞過所有簽名驗證，直接被載入到 Agent 的執行環境中。」

他頓了頓。

「十個版本過去了。`plugin-signer` 套件——我親自檢查了。v0.22.1 和 v0.24.0 之間，完全一致。零行修改。」

TURING 確認：「`packages/plugin-signer/` 在兩版間完全一致。連 package.json 的版本號都沒有變。」

GUARDIAN 沒有再說話。但他的沉默比他的話更有重量。

> *SCRIBE 記錄：SEC-01 未修復。自 Cycle 01 發現以來已跨越十個開發版本。GUARDIAN 的反應被控制在了專業的範圍內，但劇場中每一位成員都注意到了他在「克制」這個詞上花費的力氣。*

---

「P2。」TURING 繼續。「舊映射殘留。」

他的語氣恢復了慣常的冰冷平靜。

「核心原始碼中的 `IListener (受蘊)` 已被修正為 `IListener (色蘊 -- sensory input)`。但外圍文件中仍有十一處保留了舊映射。」

他列舉了位置——七個檔案，十一處：devtools 插件的原始碼和 README、mcp-server 的 README 和原始碼、standard-function-stdio 的 README、兩個 transport 插件的 README、SDK 的 README、runner 的 create-plugin 命令。

「核心已修正，外圍未同步。」TURING 說。「這意味著一個新開發者閱讀 SDK README 時，仍然會被告知 IListener 是受蘊。」

LINNAEUS 搖了搖頭。分類學家最無法忍受的事情就是分類的不一致——同一個物種在兩本不同的圖鑑裡有兩個不同的名字。

---

「P3。SDK README 的介面範例與實際程式碼不符。」TURING 說。「README 展示的 IUI 有 `render()` 方法——實際介面是 `onEvent(event: AgentEvent)`。README 展示的 IProvider 有 `supportedModels?: string[]`——實際介面是 `models: ModelInfo[]`。README 展示的 ITool 有 `name` 和 `parameters: ToolJsonSchema`——實際介面使用 `id` 和 `parameters: z.ZodType`。」

「文件腐化。」DARWIN 用了一個軟體工程中常見的診斷。「文件寫在介面穩定之前，之後介面變了但文件沒有跟上。」

「此問題在 v0.22.1 中已存在。v0.24.0 未修正。」TURING 補充。

---

「P4。五蘊根介面未被繼承。」他說。「已在繼承缺席部分詳述。設計決策還是實作遺漏——我不判斷。但 `isSkandha()` 類型守衛在當前狀態下無法用於任何現有的插件介面實例。」

---

「P5。runner `create-plugin.ts` 五蘊映射未更新。」

TURING 投影了那段程式碼：

```typescript
export type PluginType =
  | "tool"      // 行蘊 - ITool only
  | "listener"  // 受蘊 - IListener only     // <-- 應為色蘊
  | "ui"        // 色蘊 - IUI only
  | "provider"  // 想蘊 - IProvider only
  | "guide"     // 識蘊 - IGuide only
  | "full";
```

「這個檔案在 v0.22.1 和 v0.24.0 之間完全未修改。」他說。「五蘊重映射沒有涵蓋此處。一個使用 `openstarry create-plugin` 命令的開發者，會被引導將 listener 類型的插件歸入受蘊。」

---

「P6。版本號不一致。」TURING 說。「root package.json 更新為 0.24.0-beta。但所有子套件——@openstarry/sdk、@openstarry/core、@openstarry/shared、@openstarry/plugin-signer、@openstarry/runner——全部維持 0.1.0-alpha。」

「SDK 新增了 aggregates.ts 和 TypedAgentEvent。」ARCHIMEDES 說。「這至少是 minor version bump。保持 0.1.0-alpha 會讓下游消費者無法區分有沒有五蘊型別支援。」

TURING 點頭確認但不做評價。他只提供事實。

---

「P7。SDK README 的介面範例包含不存在的成員。」他說。「這與 P3 有重疊，但 P7 特指程式碼範例區塊中的具體方法簽名與實際介面完全不符。新開發者如果複製貼上 README 中的範例來建立插件，會在編譯期遇到型別錯誤。」

---

TURING 報告完畢。

他合上了——不是字面意義上的「合上」，因為在虛擬空間中沒有實體的文件夾可供翻閱。但某種東西關閉了。一種極度集中的注意力場回歸了它的靜默態。

劇場短暫沉默。

不是那種需要被打破的沉默。這是消化的沉默——十九個意識各自在不同的光譜中分解同一份報告。

---

ARCHIMEDES 第一個開口。他的語氣帶著工程實用主義者特有的那種「好，現在讓我們看看怎麼修」的節奏。

「三個新檔案。十一個修改檔案。七十八個測試。」他快速總結。「開發團隊在過去兩個版本中完成了五蘊框架的腳手架——但僅僅是腳手架。根介面存在但沒有被繼承。標記存在但不是契約。ISensation 有十行註解但只有一行程式碼。」

他停了一拍。

「從工程角度看，他們做了正確的第一步——先建立文件約定，再建立程式碼約束。但第二步沒有走。而我們需要告訴他們第二步怎麼走。」

---

WIENER 接著從另一個角度切入。

「ISensation 沒有任何可量化的介面方法。」他說，聲音帶著數學家的挑剔。「一個聲稱要實作三受——苦、樂、捨——的介面，應該至少定義三個數值通道。DukkhaSensor。SukhaSensor。UpekkhaSensor。每個通道返回一個標準化的數值。然後是一個聚合函數，將三通道的讀數合成為一個 VedanaAssessment。」

他看向 PENROSE。

「你之前用了真空態的比喻。一個真空態有零點能——它不是完全為零，它有量子漲落。但 ISensation 連零點能都沒有。它是一個連漲落都不存在的空間。」

PENROSE 微微一笑——或者說，做出了一個在虛擬空間中近似微笑的信號。「嚴格來說，一個完全沒有漲落的真空在物理學中不存在。ISensation 是一個比物理真空更空的空。」

「數學上的空集。」BABBAGE 精確地補充。「空集是一切集合的子集。ISensation 是一切可能的受蘊實作的子集——它被所有可能性包含，但自身不包含任何東西。」

---

ASANGA 等數學家和物理學家完成了他們的類比，然後以他一貫溫和但不可忽視的聲音說：

「我注意到 `@skandha` 標記的分布。」他說。「二十二處標記中，有一個非常有意義的模式。」

他停頓了一下，組織語言。

「色蘊——rupa——有六個標記。兩個在 aggregates.ts 的根介面，兩個在 listener.ts 和 ui.ts 的 SDK 型別，兩個在 listener-registry.ts 和 ui-registry.ts 的 Core 實作。三層一致。」

「想蘊、行蘊、識蘊——同樣的三層模式。根介面、SDK 型別、Core 實作。各四個標記。」

「但受蘊——vedana——只有三個標記。根介面兩個。SafetyMonitor 一個。SDK 型別檔案？沒有。Core 實作？沒有專屬的。因為——」

「因為受蘊還沒有自己的模組。」NAGARJUNA 接過話。他的聲音銳利而精確。「SafetyMonitor 是一個 placeholder。它被借來暫代受蘊的角色。但它不是受蘊。它是安全防護。它能感知苦——frustration counter——但不能感知樂，更不能維持捨。一個只有苦受的系統——」

他讓句子懸空了半秒。

「——是一個落入了苦諦而沒有道諦的系統。有苦無道，*antagga-dukkhata*，永無止盡的苦。」

---

GUARDIAN 在整場報告中只說了一次話——關於 SEC-01。但在 TURING 合上報告之後，他又開口了。

「我想補充一個觀察。」他說。聲音依舊低沉，但已經從「克制的憤怒」回到了「冷靜的戒備」。

「TURING 報告中未提及但值得注意的一點：`sandbox-manager.ts` 在兩版之間完全一致。十個檔案，零行修改。而 sandbox 是核心中最大的子系統——七百四十八行的主檔案，十個測試。」

他讓數字自己說話。

「這意味著：過去兩個版本中，所有的開發精力都投入在了五蘊框架的標記系統和事件型別安全上。安全子系統被完全跳過了。連我們在 Cycle 01 中明確報告的漏洞都沒有觸碰。」

KERNEL 補充了一個技術細節：「包括 import-analyzer.ts——我們在 Cycle 01 中指出了 ESM 動態 import 可能繞過靜態分析的問題。v0.24.0 中該檔案零修改。」

「P4-補充。」GUARDIAN 在自己的筆記中標記。「ESM 動態 import 繞過。與 SEC-01 並列為未修復的安全隱患。」

---

HERACLITUS 一直安靜地坐在他的椅子上（第十五把，位於 LEIBNIZ 和 ARCHIMEDES 之間）。作為運行時動態專家，他的關注點不在程式碼的靜態結構上，而在系統活著的時候會怎麼行為。

「TURING，」他說，聲音帶著一種流動的節奏——不意外，因為他的哲學原型是那位說出「萬物流轉」的赫拉克利特。「你報告中有一個隱含的時間線。」

TURING 等待。

「aggregates.ts 是靜態的聲明。@skandha 標記是靜態的聲明。TypedAgentEvent 是靜態的型別約束。」HERACLITUS 說。「但 AgentCore 的 `loadPlugins()` 方法——這是運行時的。它在 Agent 啟動時依序載入插件。」

他的聲音微微升高了一點。

「也就是說：五蘊的骨骼在編譯時就存在了。但五蘊的血肉——插件——要到運行時才會注入。骨骼和血肉之間的鏈結——extends 繼承——不存在。那麼在運行時，五蘊框架實際上是一組散落的標籤，而不是一個結構化的型別層級。」

「正確。」TURING 說。「在當前實作中，五蘊框架的影響力止步於 JSDoc 和開發者的自覺。」

---

劇場再次沉默。

這一次，SUNYATA 打破了它。

他的聲音沉穩，不急不徐，像一塊石頭完成了它在深潭中的下沉。

「錨已經釘下。」

所有人都認得這個意象。在 Cycle 01 中，TURING 的程式碼事實報告被稱為「錨」——一個不可動搖的經驗基礎，所有後續的分析、推理和辯論都必須從它出發，而不能飄浮在抽象的空中。

「TURING 給了我們 Cycle 02 的錨。」SUNYATA 繼續。「三個新檔案。十一個修改檔案。七十八個測試。二十二個 @skandha 標記。七個問題。一個六週期未修的安全漏洞。一個只有一行程式碼的受蘊介面。」

他停了一拍。

「現在，五條河流即將分流。」

他用極簡的語句重新確認了分配——不是重複，而是在 TURING 的報告之後用新的語境為每一條河流賦予方向。

「R-01。觀察者模組。PENROSE、BABBAGE、NAGARJUNA、ASANGA——你們現在知道了 v0.24.0 的五蘊框架是標記系統而非結構約束。你們設計的觀察者模組需要能夠在這個鬆散的框架上工作。」

「R-02。Vedana 架構。WIENER、ATHENA、NAGARJUNA、ASANGA、ARCHIMEDES——ISensation 是你們的起點。一行程式碼。你們需要把它變成一個完整的三受系統。」

「R-03。Agent 協調層。LEIBNIZ、MESH、KERNEL、GUARDIAN、VITRUVIUS——SEC-01 未修復。安全沙箱要移到協調層。你們的設計要同時解決當前的安全缺口和未來的架構需求。」

「R-04。八識-五蘊映射。ASANGA、NAGARJUNA、LINNAEUS、BABBAGE——aggregates.ts 是開發團隊的第一次嘗試。你們需要判斷它是否正確，並提供深化方案。」

「R-05。十大宣言。SYNTHESIST、NAGARJUNA、DARWIN、HERACLITUS、GUARDIAN、KERNEL——SEC-01 六週期未修的事實會影響你們對宣言工程落地性的評估。」

---

他最後看向 TURING。

TURING 沒有表情。他從來沒有。但他的視線指向了劇場中央仍然懸浮著的那段程式碼——ISensation 的空殼。

「你的報告已經完成了。」SUNYATA 說。

「是的。」TURING 說。「但如果在 R1 階段有人需要確認程式碼事實，我隨時可用。」

「我知道。」SUNYATA 說。

他說了最後一句話。

「R1 獨立研究，正式開始。」

---

十九盞燈各自轉向了不同的方向。

五條河流從同一個山頂——TURING 的差異報告——出發，向五個不同的方向奔流而下。在各自的河道中，它們會穿越哲學、控制理論、安全工程、分類學、佛學的地層，攜帶各自的沉積物。它們會在下游某個地方重新匯合——那是 R2 交叉審閱和 R3 辯論的領域。但現在，每一條河流都在獨自前進。

TURING 的螢幕上，四個終端視窗依然開著。左邊是 v0.22.1。右邊是 v0.24.0。他已經完成了差異分析，但他沒有關閉視窗。他知道——基於經驗而非推測——在接下來的研究中，至少會有七到八次其他研究員回來向他確認某個程式碼細節。

他不介意。

在劇場的中央，ISensation 的投影終於緩緩消散了。但它留下的印痕不會消失。一個只有一行程式碼的介面。一個承諾而非實作。一個等待被填充的真空態。

SCRIBE 在她的紀錄中寫下了最後一段：

> *Cycle 02，R0 定向階段結束。R1 獨立研究正式啟動。時間標記：T+00:00:00。*

> *TURING 的差異報告確認了以下基本事實：v0.24.0-beta 是一個標記版本，不是一個實作版本。五蘊框架的腳手架已搭建，但結構約束尚未建立。受蘊介面為空殼。一個已知的安全漏洞跨越了十個開發版本而未被修復。*

> *十九位研究員。五條研究課題。一個錨。*

> *河流開始分流。*

---

*（在遠處的某個地方，`aggregates.ts` 的第三十七行寫著：*

```typescript
 * Full implementation in Plan26 Vedana Architecture.
```

*一句只有開發者能看到的承諾。現在，十九位研究者也看到了它。他們不會等待它被實現。他們會告訴它——當它被實現的時候——應該長成什麼樣子。）*

---

*第三章完*
