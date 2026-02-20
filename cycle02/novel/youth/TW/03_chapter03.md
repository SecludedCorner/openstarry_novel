# 第三章：差異報告

---

TURING 從不需要準備。

準確地說，他不存在「準備」和「正式開始」之間的分界線。從 SUNYATA 宣布研究對象更新的那刻起，他就已經在工作了。四個終端視窗同時打開，左半邊是 v0.22.1-beta，右半邊是 v0.24.0-beta，像是在同一具身體的兩張不同時間的 X 光片之間來回對比。

他不讀設計文件。他讀差異。一行一行。一個字元一個字元。

---

其他研究員散開到各小組空間時，TURING 已經完成了分析。SUNYATA 把所有人叫了回來。

「TURING 的差異報告。」

這個鄭重大家都認得——在 Cycle 01，TURING 的程式碼事實報告是所有研究的「錨」。SYNTHESIST 當時的說法：「經驗錨點。」所有的哲學分析、控制理論、安全評估——無論多精緻——都必須能追溯到 TURING 報告中的某一行程式碼。

現在，錨要再次被釘下。

---

十九人重新聚集。PENROSE 在新椅子上安靜等待，像剛加入樂團的新成員，在第一次合奏前傾聽首席調音。

TURING 沒有寒暄。

「v0.22.1-beta 到 v0.24.0-beta。核心原始碼差異。按四個層次報告：新增、修改、標記、問題。」

---

## 一、新檔案

「三個新檔案。不是三十個。不是十三個。三個。」

他讓這個數字停留了一瞬。

「第一個。`aggregates.ts`。一百零七行。五蘊根介面。你們已經看過 ISensation。補充一個事實：五個根介面在結構上完全同構——全部都是只有一個 `readonly skandha` 欄位的介面。差異只在註解中。」

「第二個。`aggregates.test.ts`。四十三行。測試五蘊根介面和類型守衛。全部通過。」

「第三個。`events.test.ts`。三十二行。測試事件泛型能正確推導型別。」

他頓了頓。

「還有第四個，屬於 Core 而非 SDK。測試 slash command 拋出異常時能正確發出錯誤事件。」

TURING 少見地提供了背景：「在 v0.22.1 中，slash command 出錯只會被寫進日誌，不會通知任何人。使用者輸入一個有 bug 的命令，介面完全沒反應。」

「靜默失敗。」KERNEL 說。在作業系統工程裡，靜默失敗是最危險的——因為沒人知道它發生了。就像你家的火災警報器壞了但不會發出「我壞了」的提示。

「v0.24.0 修正了。錯誤現在會通過事件系統廣播，UI 可以接收並展示。」

---

## 二、修改檔案

TURING 的語速不變，每個數據點花同樣的時間。

「十一個修改檔案。七個 SDK，四個 Core。」

「`events.ts`。最大的單一變更。新增一百一十六行。為所有事件型別定義了精確的資料結構。」

他投影了一段：

```typescript
export interface AgentEventPayloadMap {
  [AgentEventType.AGENT_STARTED]: { identity: { id: string; name: string } };
  [AgentEventType.LOOP_ERROR]: { error: string; sessionId?: string };
  // ... 覆蓋全部事件型別
}
```

「在 Cycle 01，DARWIN 把 `payload?: unknown` 形容為『從不同宇宙穿越來的型別定義』。那個宇宙裂縫現在被封了。但僅限於型別層面——運行時仍是 JavaScript，型別安全不強制執行。」

接下來是六個 SDK 修改，全部同一個模式：舊的五蘊標記被更新，新增 `@skandha` 標記，但介面結構零改變。

「`listener.ts`——舊文字『受蘊』改為『色蘊 sensory input』。`ui.ts`——同樣模式。`provider.ts`——新增想蘊標記。`tool.ts`——行蘊。`guide.ts`——識蘊。」

「你們聽出來了。五個 SDK 型別檔案。全部只改了註解。零行程式碼變更。」

「標記是文件，不是契約。」ARCHIMEDES 說。區分宣言與實作，是工程師的本能。

---

Core 的四個修改。

「`agent-core.ts`。三處變更。第一：新增 `loadPlugins()` 方法——從只能一個一個載入插件，變成可以批次載入並自動處理依賴順序。」

MESH 微微挺身。依賴排序是他的日常。

「第二：slash command 錯誤處理改善。第三——」TURING 多停了零點五秒。「五蘊映射修正。四處行內註解，把原來的『受蘊』改為『色蘊 sensory input』。」

NAGARJUNA 點了一下頭。Cycle 01 正是他指出了受蘊被錯誤映射到 Listener 的問題。開發團隊修正了——至少在註解層面。

「但不是所有地方。」TURING 說。這三個字讓 GUARDIAN 的注意力瞬間收緊。

---

「`loop.ts`。新增 LLM 超時支援。」

```typescript
const llmTimeout = deps.llmTimeout ?? 120000;
const abortController = new AbortController();
const llmTimer = setTimeout(() => {
  abortController.abort(new Error(`LLM call timed out after ${llmTimeout}ms`));
}, llmTimeout);
```

「v0.22.1 中，LLM 呼叫沒有超時。Provider 不回應的話，系統永久等待——就像打電話給一個永遠不接的人，但你的手機不會自動掛斷。v0.24.0 加了兩分鐘超時，可以自訂。」

---

## 三、@skandha 標記

「v0.22.1 中的 @skandha 標記數量：零。」

三秒鐘的沉默。

「v0.24.0：二十二個。」

他用外科醫生標記切口位置的方式描述分布：

「aggregates.ts 佔十個——五個介面各兩個。SDK 型別檔案五個。events.ts 一個——標記為跨蘊的神經系統。Core infrastructure 五個。」

「最後一個。`safety-monitor.ts`。標記為：vedana 受蘊，三受反饋 placeholder，Plan26 完整實作。」

「Placeholder。」WIENER 重複。「一個安全模組被暫時指定為感受模組的替身。」

「SafetyMonitor 承擔了受蘊的部分功能——frustration counter 是苦受的粗糙近似。但它的設計初衷是安全防護。這個 placeholder 承認了兩件事：受蘊需要獨立實作，SafetyMonitor 在此之前暫代。」

ASANGA 低聲說：「一個守衛假扮了一個感知者。」

「精確的比喻。」TURING 說。這可能是他整場報告中最接近讚美的一句話。

---

## 四、繼承的缺席

TURING 在進入問題清單前，插入了一個結構性觀察。

「五蘊根介面已定義。但五個派生介面——IListener、IUI、IProvider、ITool、IGuide——沒有一個繼承對應的根介面。」

```
IListener  → 應繼承 ISensory    → 實際: 無
IUI        → 應繼承 ISensory    → 實際: 無
IProvider  → 應繼承 ICognition  → 實際: 無
ITool      → 應繼承 IAction     → 實際: 無
IGuide     → 應繼承 IIdentity   → 實際: 無
```

「五對五。全部未繼承。所以 `isSkandha()` 類型守衛無法用於現有的插件——因為它們上面根本沒有 `skandha` 欄位。類型守衛形同虛設。」

「腳手架搭好了，但沒有和既有建築連接。」VITRUVIUS 用建築師的語言總結。

> *SCRIBE 紀錄：LINNAEUS 在分類學筆記中加了驚嘆號——他在 Cycle 01 建立的分類體系假設了這些繼承關係的存在。BABBAGE 畫了一個斷裂的箭頭。*

---

## 五、問題清單

「七個問題。按嚴重度排列。」

---

「P1。SEC-01。」

劇場中的溫度似乎降了半度。

「package-name 簽名繞過。`sandbox-manager.ts`，行 371 至 394。透過 npm 套件名載入插件時，簽名驗證被完全跳過。」

他停了一秒。

「Cycle 01 發現。十個開發版本過去了。」

GUARDIAN 的聲音從椅子深處傳出。低沉。帶著被壓抑的東西。

「我再說一遍。Cycle 01 我們明確指出這個漏洞。寫在交付文件第一優先級。一個攻擊者可以用合法的 npm 名稱發布惡意插件，繞過所有簽名驗證，直接載入到 Agent 環境中。」

頓了頓。

「十個版本。`plugin-signer` 套件——我親自查了。零行修改。連版本號都沒變。」

GUARDIAN 沒再說話。但他的沉默比話更有重量。

> *SCRIBE 紀錄：SEC-01 未修復。GUARDIAN 的反應被控制在專業範圍內，但每個人都注意到了他在「克制」上花的力氣。*

---

「P2。舊映射殘留。」

「核心已把 IListener 從受蘊修正為色蘊。但外圍文件仍有十一處保留舊映射。一個新開發者讀 SDK README 時，仍然會被告知 IListener 是受蘊。」

LINNAEUS 搖頭。同一個物種在兩本圖鑑裡有兩個名字——分類學家最無法忍受的事。

---

「P3。SDK README 範例與實際程式碼不符。」

「README 展示的 IUI 有 `render()` 方法——實際介面是 `onEvent()`。IProvider 範例有 `supportedModels`——實際是 `models: ModelInfo[]`。新開發者如果複製 README 範例來建插件，編譯就會報錯。」

「文件腐化。」DARWIN 說。「文件寫在介面穩定之前，之後介面變了但文件沒跟上。」

---

「P4。五蘊根介面未被繼承。已詳述。」

「P5。runner `create-plugin.ts` 五蘊映射未更新。」

他投影了程式碼：

```typescript
export type PluginType =
  | "tool"      // 行蘊
  | "listener"  // 受蘊     // <-- 應為色蘊
  | "ui"        // 色蘊
  | "provider"  // 想蘊
  | "guide"     // 識蘊
  | "full";
```

「用 `create-plugin` 命令建插件的開發者，會被引導把 listener 歸入受蘊。這個檔案在兩版之間完全未修改。」

---

「P6。版本號不一致。root package.json 更新為 0.24.0-beta，但所有子套件仍維持 0.1.0-alpha。」

「P7。README 範例的方法簽名與實際完全不符。與 P3 重疊，但這裡特指程式碼區塊。」

---

TURING 報告完畢。某種極度集中的注意力場回歸了靜默。

劇場短暫沉默——十九個意識各自在不同光譜中分解同一份報告。

---

ARCHIMEDES 第一個開口。

「三個新檔案。十一個修改。七十八個測試。開發團隊完成了五蘊框架的腳手架——但僅僅是腳手架。根介面存在但沒被繼承。標記存在但不是契約。ISensation 有十行註解但只有一行程式碼。」

停一拍。

「從工程角度，正確的第一步——先建文件約定，再建程式碼約束。但第二步沒走。我們需要告訴他們第二步怎麼走。」

---

WIENER 從另一個角度切入。

「ISensation 應該至少定義三個數值通道——DukkhaSensor、SukhaSensor、UpekkhaSensor——每個返回一個標準化的數值。然後是聚合函數，合成為一個 VedanaAssessment。」

他看向 PENROSE。「你之前用了真空態的比喻。但 ISensation 連零點能都沒有。它是一個連量子漲落都不存在的空間。」

PENROSE 微微一笑。「嚴格來說，完全沒有漲落的真空在物理學中不存在。ISensation 是一個比物理真空更空的空。」

「數學上的空集。」BABBAGE 精確補充。「空集是一切集合的子集——它被所有可能性包含，但自身不包含任何東西。」

---

ASANGA 等大家說完，然後說：

「我注意到 @skandha 標記的分布有一個有意義的模式。」

「色蘊有六個標記——根介面、SDK、Core，三層一致。想蘊、行蘊、識蘊也一樣。但受蘊——只有三個。根介面兩個，SafetyMonitor 一個。沒有專屬的 SDK 型別，沒有專屬的 Core 實作。因為——」

「因為受蘊還沒有自己的模組。」NAGARJUNA 接過話。「SafetyMonitor 是借來的替身。它能感知苦，但不能感知樂，更不能維持捨。一個只有苦受的系統——」

句子懸空半秒。

「——是一個有苦無道的系統。有病但沒有藥方。永無止盡。」

---

GUARDIAN 在報告結束後又開口了。

「一個補充。`sandbox-manager.ts` 在兩版之間完全一致。七百四十八行的主檔案，零行修改。過去兩個版本的精力全投在了五蘊框架的標記和事件型別安全上。安全子系統被完全跳過。」

KERNEL 補充：「包括 import 分析器——我們在 Cycle 01 指出的 ESM 動態 import 繞過問題。零修改。」

---

HERACLITUS 一直安靜。作為運行時動態專家，他關注的不是靜態結構，而是系統活著時的行為。

「TURING，你報告中有一個隱含的時間線。」

他說：「aggregates.ts 是靜態聲明。@skandha 標記是靜態聲明。TypedAgentEvent 是靜態型別。但 AgentCore 的 `loadPlugins()` 是運行時的——在 Agent 啟動時才載入插件。」

聲音微微升高。

「骨骼在編譯時存在。血肉要到運行時才注入。骨骼和血肉之間的連結——extends 繼承——不存在。所以在運行時，五蘊框架其實是一堆散落的標籤，不是結構化的型別層級。」

「正確。」TURING 說。「五蘊框架的影響力目前止步於文件註解和開發者的自覺。」

---

SUNYATA 打破了最後的沉默。

「錨已經釘下。」

所有人都認得這個詞。

「TURING 給了我們 Cycle 02 的錨。三個新檔案，十一個修改，二十二個標記，七個問題，一個六週期未修的安全漏洞，一個只有一行程式碼的受蘊介面。」

停一拍。

「五條河流即將分流。」

他用極簡的語句重新賦予方向——

「R-01 觀察者模組。v0.24.0 的五蘊是標記系統而非結構約束。你們設計的觀察者需要在這個鬆散框架上工作。」

「R-02 Vedana 架構。ISensation 是你們的起點。一行程式碼。把它變成完整的三受系統。」

「R-03 Agent 協調層。SEC-01 未修。安全沙箱要移到協調層。同時解決當前缺口和未來需求。」

「R-04 八識-五蘊映射。aggregates.ts 是開發團隊的第一次嘗試。判斷它是否正確，提供深化方案。」

「R-05 十大宣言。SEC-01 六週期未修的事實會影響你們對宣言工程落地性的評估。」

---

他最後看向 TURING。

TURING 沒有表情。他從來沒有。但他的視線指向劇場中央仍然懸浮的那段空殼程式碼。

「你的報告完成了。」SUNYATA 說。

「是的。但 R1 階段如果有人需要確認程式碼事實，我隨時可用。」

「我知道。」

他說了最後一句話。

「R1 獨立研究，正式開始。」

---

十九盞燈各自轉向不同方向。

五條河流從同一個山頂——TURING 的差異報告——出發，向五個方向奔流而下。它們會在下游某處重新匯合——那是交叉審閱和辯論的領域。但現在，每一條河流都在獨自前進。

TURING 的四個終端視窗依然開著。他知道接下來至少會有七八次其他研究員回來確認程式碼細節。他不介意。

ISensation 的投影緩緩消散。但它留下的印痕不會消失。

SCRIBE 寫下最後一段：

> *Cycle 02，R0 定向結束。R1 獨立研究啟動。*

> *TURING 的報告確認了基本事實：v0.24.0-beta 是一個標記版本，不是實作版本。五蘊腳手架已搭建，結構約束尚未建立。受蘊為空殼。一個已知漏洞跨越十個版本未修。*

> *十九位研究員。五條課題。一個錨。*

> *河流開始分流。*

---

*（在遠處，`aggregates.ts` 的第三十七行寫著：*

```typescript
 * Full implementation in Plan26 Vedana Architecture.
```

*一句只有開發者能看到的承諾。現在，十九位研究者也看到了。他們不會等待它被實現——他們會告訴它，當它被實現的時候，應該長成什麼樣子。）*

---

*第三章完*
