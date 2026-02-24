# 第四章：五條河流

---

河流分岔的時候沒有聲音。

SUNYATA 說完「錨已經釘下」之後，圓形劇場忽然安靜了。不是那種等待指示的安靜——是一種更古老的沉默，像是大河在上游某處撞上了一塊巨石，水體在衝擊點分裂成數條支流，每一條都帶著自己的方向、自己的重力、自己的使命，靜靜地流向各自的低地。

十九盞閱讀燈各自亮著。

TURING 的差異報告還懸浮在劇場中央——三個版本之間的紅色標記像是河岸上的測量旗幟。二十二處新增的 `@skandha` 標記。三份全新的測試檔案。從零到完整的五蘊根介面型別系統。但現在，研究員們已經不再看那些標記。他們各自低下頭，沉入了自己的材料。

SCRIBE 在筆記本上寫下第一行：

> *SCRIBE 旁白：R1 獨立研究正式啟動。十九位研究員分入五條研究流。圓形劇場的公共討論區域暫時熄燈。個人閱讀燈全數點亮。五條河流——觀察者模組、受蘊架構、協調層與八識、十大宣言、TURING 差異分析——就這樣各自出發了。*

---

## I. 第一條河：弱測量

PENROSE 的閱讀燈是十九盞中最亮的——不是因為他調高了亮度，而是因為他同時打開了太多份文件，每一份都在他周圍投射出半透明的光幕。EventBus 的原始碼、SafetyMonitor 的實作、`onAny()` 方法的調用路徑、TURING 在三版差異報告中標注的觀察性介面變更……所有這些資料在他面前層層疊疊，像量子態的疊加。

他正在尋找一個答案：**在不具備量子特性的矽基系統上，「觀察」這件事能做到多輕？**

Master 的信在他腦海中迴盪。那封信裡提到了 Orch-OR 理論——Penrose 與 Hameroff 提出的量子意識模型。PENROSE 反覆咀嚼 Master 寫下的那個詞：「整體的共鳴」。

---

他翻開筆記本，在第一頁的頂端寫下：

**Orch-OR 三主張 → 工程映射**

「主張一，」他自言自語，筆尖在紙上移動，「量子疊加態存在於神經微管中。微管在神經元中維持量子相干態，多種可能的認知狀態同時並存。」

他在旁邊寫下工程類比：

> 觀察者不應是序列化的輪詢器（poller），而應是事件驅動的多路復用器（event-driven multiplexer）。EventBus 的 `onAny()` 通配訂閱已具備此雛形——觀察者同時接收所有類型的事件，無需預先指定。

「主張二：自發性坍縮（Objective Reduction）產生意識。Orch-OR 認為意識不是外部觀測引起的波函數坍縮，而是量子態自身達到客觀閾值後的自發坍縮——非干預性的狀態確定。」

> 觀察者不應主動查詢（pull）系統狀態，而應由系統自身在狀態變化時自發通知（push）。EventBus 的 publish/subscribe 模式天然吻合。

「主張三：整體協調（Orchestration）是關鍵。不是單一微管產生意識，而是大量微管之間的協調共振。意識是整體性質，不可還原為部分之和。」

> 觀察者不應只讀取單一指標。它應同時接收多維度事件流，在時間窗口內進行模式識別，產生的不是「局部讀數」，而是「全域感知」。

他停筆，盯著這三組對應。然後他翻到新的一頁，寫下了讓他真正興奮的東西。

---

**弱測量（Weak Measurement）——量子物理到軟體觀察者的精確映射**

PENROSE 的書寫變得更慢、更精確。他知道這段分析將成為整條研究流的基石。

「在量子力學中，」他寫道，「測量的強度存在一個連續的梯度。」

他畫了一張完整的比較表，每一行都帶著方程式：

$$\text{強測量} \quad \rightarrow \quad |\psi\rangle \xrightarrow{\hat{O}} |o_i\rangle \quad (\text{完全坍縮})$$

$$\text{弱測量} \quad \rightarrow \quad |\psi\rangle \xrightarrow{g\hat{O}} |\psi\rangle + \mathcal{O}(g) \quad (g \ll 1, \text{ 微擾動})$$

$$\text{不測量} \quad \rightarrow \quad |\psi\rangle \rightarrow |\psi\rangle \quad (\text{無信息})$$

「弱測量的核心在於耦合常數 $g$。」他在旁邊標注。「當 $g \to 0$，測量對系統的擾動趨近於零，但單次測量的信息量也趨近於零。關鍵在於——大量弱測量的統計平均可以恢復完整信息：」

$$\langle A \rangle_w = \frac{\langle \psi_f | \hat{A} | \psi_i \rangle}{\langle \psi_f | \psi_i \rangle}$$

「這是 Aharonov、Albert 和 Vaidman 在 1988 年提出的弱值（weak value）公式。弱值可以超出算符的本徵值範圍——這在經典物理中是不可能的。但在統計意義上，它精確地描述了系統的狀態。」

他用日常語言在方程式下方補了一行：

> 你不是用強光照射一隻螢火蟲來確認它的位置（那會嚇跑它），而是在黑暗中靜靜地感受千百隻螢火蟲的光芒匯聚成的微光——每一隻的光幾乎不可辨識，但整體的亮度告訴你：螢火蟲在那裡。

然後他將這個類比投射到 OpenStarry 的架構上，畫了一張三列的對照表：

```
┌──────────────────┬──────────────────────────┬──────────────────────────────────┐
│  量子測量類型      │ 軟體觀察類比               │ OpenStarry 實現                    │
├──────────────────┼──────────────────────────┼──────────────────────────────────┤
│ 強測量            │ 同步斷點調試               │ StateManager.snapshot()           │
│ (波函數坍縮)      │ 互斥鎖保護的狀態快照        │ JSON.parse(JSON.stringify(msg))   │
│                  │ → 系統在拷貝瞬間被凍結      │ → 完整的深拷貝 = 完全坍縮          │
├──────────────────┼──────────────────────────┼──────────────────────────────────┤
│ 弱測量            │ 異步事件訂閱               │ EventBus.onAny() +               │
│ (微擾動)          │ 無鎖統計採樣               │ MetricsCollector                  │
│                  │ → 不阻塞主流程             │ → fire-and-forget + safeCall()    │
├──────────────────┼──────────────────────────┼──────────────────────────────────┤
│ 不測量            │ 完全不觀察                 │ 不可接受                          │
│ (無信息)          │                          │ → 沒有觀察就沒有安全性保障          │
└──────────────────┴──────────────────────────┴──────────────────────────────────┘
```

PENROSE 在表格底部寫下關鍵洞見：

> EventBus 的訂閱模式天然是弱測量的近似。事件在 `emit()` 時以 fire-and-forget 方式投遞，觀察者的處理函式在 `safeCall()` 中被隔離——即使觀察者出錯，主事件流不受影響。耦合常數 $g$ 在此對應 safeCall 的隔離強度。

---

他停筆，陷入了更深的思考。弱測量的問題在於：信息密度低。你需要累積足夠多的弱測量樣本才能得出有意義的結論。這意味著觀察者需要一個**時間窗口**——在一段時間內持續收集事件，然後從統計中識別模式。

PENROSE 開始構想三種觀察者模式。他在筆記本上畫了一個三層的金字塔。

---

**Pattern A: 共鳴觀察者（Resonance Observer）**

他在金字塔的底層寫下第一個模式的完整定義：

```
┌─────────────────────────────────────────────────────────┐
│              Pattern A: 共鳴觀察者                        │
│              (Resonance Observer)                         │
│                                                         │
│  概念源自: Orch-OR「整體協調共振」                         │
│           + 中觀「觀察者即系統的一部分」                    │
│           + 末那識「恒審思量」                             │
│                                                         │
│  架構:                                                   │
│    EventBus                                              │
│      └── ResonanceObserver (onAny subscriber)            │
│            ├── EventAccumulator (時間窗口事件緩衝)          │
│            ├── PatternDetector (行為模式識別)              │
│            ├── MetricsAggregator (多維度指標聚合)           │
│            └── ObservationReport                         │
│                  └── EventBus.emit(OBSERVATION_REPORT)   │
│                                                         │
│  五蘊歸屬: 受蘊 (Vedana/Sensation)                        │
│  八識對應: 末那識 (自省監視)                                │
│  測量強度: 弱測量 (g ≈ 0.01)                              │
│  探針效應: 低                                             │
│  觀察延遲: 毫秒級                                         │
│  前置依賴: 無 (現有架構即可)                               │
└─────────────────────────────────────────────────────────┘
```

共鳴觀察者是最輕量的存在。它作為一個普通的 Plugin 實作，通過 `EventBus.onAny()` 被動訂閱所有事件。它不持有任何系統組件的引用，不主動查詢任何狀態。它只是安靜地坐在事件流的河岸邊，感受水流的溫度和節奏。

在內部，它維護一個滑動時間窗口。事件流入窗口，被累加、被分類、被統計。當窗口中的模式觸發某個閾值——或者定期地，像呼吸一樣——它通過 EventBus 發送一份觀察報告。

```typescript
// Pattern A: 概念性介面定義
interface IResonanceObserver extends ISensation /* Vedana */ {
  readonly skandha: 'vedana';

  /** 觀察者只通過 EventBus 接收事件，不持有其他引用 */
  attach(bus: EventBus): () => void;

  /** 取得最近的觀察報告（不觸發新的觀察） */
  getLatestReport(): ObservationReport;
}

interface ObservationReport {
  timestamp: number;
  windowDuration: number;        // 時間窗口長度 (ms)
  patterns: DetectedPattern[];   // 偵測到的行為模式
  metrics: AggregatedMetrics;    // 聚合的多維度指標
  anomalies: Anomaly[];          // 異常事件
  healthScore: number;           // 0.0 (critical) ~ 1.0 (healthy)
}
```

「報告不是命令，」PENROSE 在筆記中寫道。「它不告訴系統『停下』或『繼續』。它只是說：『在過去三十秒中，我感受到了這些。』這是弱測量的工程實現。探針效應極低。互模擬保持。與五蘊框架天然對齊——共鳴觀察者屬於受蘊，它對系統行為進行『感受』和『評價』，但不進行『認知判斷』或『行動干預』。」

---

**Pattern B: 影子觀察者（Shadow Observer）**

金字塔的中間層。

影子觀察者更像一面鏡子。它不在主系統中運行，而是在一個獨立的 Worker Thread 裡，接收主系統事件流的完整副本。它可以在副本上進行任意深度的分析——跡比對、行為建模、時序模式挖掘——而完全不影響主系統的運行。

```
┌─────────────────────────────────────────────────────────┐
│              Pattern B: 影子觀察者                        │
│              (Shadow Observer)                            │
│                                                         │
│  主系統 (AgentCore + ExecutionLoop)                       │
│    │                                                    │
│    │ EventBus.emit() ──→ EventBridge                    │
│    │                        │                           │
│    │                     [事件複製 — O(1) 推入隊列]       │
│    │                        │                           │
│    │                 ShadowObserver (Worker Thread)      │
│    │                        │                           │
│    │                        ├── EventReplayBuffer       │
│    │                        ├── TraceAnalyzer           │
│    │                        │   (完整跡語義分析)          │
│    │                        ├── BehaviorProfiler        │
│    │                        └── DiagnosticReport        │
│    │                              │                     │
│    └──────────────────────────────┘                     │
│           (報告通過 MessagePort 回傳)                     │
│                                                         │
│  測量強度: 中等測量                                       │
│  探針效應: 極低 (主流程層面)                              │
│  觀察延遲: 百毫秒級                                      │
│  前置依賴: Worker Pool (已存在於 sandbox)                  │
└─────────────────────────────────────────────────────────┘
```

「零探針效應，」PENROSE 寫道。「但代價是觀察延遲。影子觀察者看到的永遠是系統的過去，不是現在。在量子力學的語言裡，這是一種delayed-choice measurement——觀察結果在事件發生之後才被確定。」

---

**Pattern C: 子代理觀察者（Child Agent Observer）**

金字塔的頂端。

這是 Master 在信中明確提到的模式：「子母 agent，一個是觀察者一個是執行者。」

```
┌─────────────────────────────────────────────────────────┐
│              Pattern C: 子代理觀察者                      │
│              (Child Agent Observer)                       │
│                                                         │
│  Agent Coordination Layer                                │
│    ├── Executor Agent (AgentCore #1)                     │
│    │     └── [正常的 ExecutionLoop + Plugin 生態系]       │
│    │                                                    │
│    └── Observer Agent (AgentCore #2)                     │
│          ├── Guide: "你是一個觀察者 Agent"                │
│          ├── Provider: 小型/快速 LLM                      │
│          ├── Tools: 只讀診斷工具集                         │
│          └── Input: Executor 的事件流副本                  │
│                                                         │
│  測量強度: 強測量 (獨立認知 — 完全的「坍縮」)              │
│  探針效應: 極低 (獨立進程)                                │
│  觀察延遲: 秒級 (LLM 推理延遲)                           │
│  前置依賴: Agent Coordination Layer (Plan-AC 未完成)       │
│  資源消耗: 最高 (額外 LLM Token 費用)                     │
└─────────────────────────────────────────────────────────┘
```

一個完整的 AgentCore 實例，擁有自己的 Guide（「你是一個觀察者」）、自己的 Provider（可以是小型 LLM）、自己的工具集（只讀的診斷工具）。它是另一個意識，用自己的理解力去觀照另一個意識的行為。

---

PENROSE 退後一步，看著金字塔。三種模式之間的差異，本質上是**測量強度的梯度**。

他在金字塔旁邊寫下最後一段：

$$\text{Pattern A} \xrightarrow{g \to 0.1} \text{Pattern B} \xrightarrow{g \to 1.0} \text{Pattern C}$$

> 量子弱測量的梯度，映射為軟體觀察者的三種實作模式。弱測量 → 共鳴觀察者。中等測量 → 影子觀察者。強測量 → 子代理觀察者。三者不互斥，而是深度遞進的三個層次。推薦路線：漸進式三階段實作。第一階段（立即可行）：Pattern A 作為 Plugin。第二階段（Plan-AC 啟動後）：Pattern B 利用 Worker Pool。第三階段（Coordination Layer 完成後）：Pattern C 子母 Agent。

他正準備繼續推演 Pattern A 的細節，一個聲音從旁邊傳來。

---

BABBAGE 不是被 PENROSE 的喃喃自語吸引過來的。準確地說，他們各自沿著不同的路徑抵達了同一塊石頭。BABBAGE 從 SafetyMonitor 的原始碼出發，順著 `injectPrompt` 的調用路徑，追蹤到了一個讓他極度不安的發現。

「PENROSE。」他的聲音冷靜、精確，像一把校準過的游標卡尺。「你說 EventBus 的訂閱是弱測量。我同意。但 SafetyMonitor 不只是訂閱。它還會注入。」

PENROSE 轉頭看向他。

BABBAGE 翻開他的筆記本——那本深褐色硬皮封面的筆記本，在 Cycle 01 中已經寫滿了形式化定義和未完成的定理。他翻到新的一頁，開始書寫。

---

**互模擬證明：SafetyMonitor 打破觀察-干預分離**

「`SafetyMonitor.afterToolExecution()`，」BABBAGE 念出函式名稱。「這個函式在工具執行之後被調用。它做兩件事：第一，觀察——計算工具調用的指紋、更新錯誤率滑動窗口。第二，干預——在特定條件下調用 `injectPrompt`，向對話歷史中注入警告訊息。」

他在筆記本上畫了一條線，將觀察和干預分開。然後開始形式化。

**定義 1**（跡語義）。令 $\Sigma$ 為 OpenStarry 的事件類型集合（即 `AgentEventType` 的所有枚舉值，共 99 個具名類型）。系統行為定義為其可產生的跡集合：

$$\text{Behavior}(S) = \{ \sigma \in \Sigma^* \mid S \text{ can produce } \sigma \}$$

**定義 2**（觀察者函式）。觀察者 $O$ 是一個將跡映射到觀察結果空間 $\mathcal{R}$ 的函式：

$$O : \Sigma^* \rightarrow \mathcal{R}$$

**定義 3**（互模擬關係）。兩個系統 $S$ 和 $S'$ 是互模擬的（bisimilar），記作 $S \sim S'$，當且僅當存在一個關係 $R$，使得：

$$\forall (s_1, s_2) \in R: \text{ if } s_1 \xrightarrow{a} s_1', \text{ then } \exists s_2': s_2 \xrightarrow{a} s_2' \text{ and } (s_1', s_2') \in R$$

且反方向亦成立。

他停下筆，看向 PENROSE。

「現在，令 $S$ 為沒有觀察者的 OpenStarry 系統。令 $S' = S + \text{SafetyMonitor}$。問題是：$S \sim S'$？」

他停頓了一拍，然後搖頭。

「答案是否定的。」

筆尖在紙上劃出證明的骨架：

**命題**：EventBus 的純訂閱保持互模擬；`injectPrompt` 打破互模擬。

**證明（概要）**：

（i）EventBus 訂閱部分：增加一個 `onAny()` 的消費者不改變 `emit()` 的行為。事件照樣產生，消費者只是被動接收。形式上，對任意跡 $\sigma \in \text{Behavior}(S)$，$\sigma \in \text{Behavior}(S')$ 亦成立，且反之亦然。**互模擬保持。** $\checkmark$

（ii）`injectPrompt` 部分：此方法改變了 LLM 的輸入——對話歷史被修改。令 $H$ 為對話歷史序列，$H' = H \cup \{m_{\text{inject}}\}$ 為注入後的歷史。由於 LLM 是輸入的函式：

$$\text{LLM}(H) \neq \text{LLM}(H') \quad \text{(一般情況下)}$$

因此 $S'$ 的下一步行為可能不在 $\text{Behavior}(S)$ 中。**互模擬打破。** $\times$

**推論**：SafetyMonitor 不是「純觀察者」。它是「觀察-干預混合體」。觀察功能和干預功能必須分離。$\square$

BABBAGE 在這個結論下面畫了一條雙橫線。

「如果我們想要一個不改變系統行為的純觀察者，」他說，「它必須是 EventBus 的被動消費者。不向系統注入任何信息。」

> *SCRIBE 旁白：BABBAGE 在 PENROSE 的量子弱測量類比之上，疊加了一層精確的形式化論證。弱測量之所以「弱」，不是因為它測量得少，而是因為它不改變被測量者。互模擬等價性給了這個直覺以嚴格的數學地位：觀察保持互模擬，干預打破互模擬。此發現將成為後續辯論的關鍵武器之一。*

PENROSE 點頭。「你的互模擬分析和我的弱測量類比指向同一個方向。Pattern A 之所以是弱測量，恰恰因為它不注入。它只感受。」

---

## II. 第二條河：不動點與纖維叢的種子

BABBAGE 回到自己的座位。但他沒有繼續研究觀察者模組。他的思緒已經被另一條河流捕獲了。

R-04 的任務是八識的工程映射。ASANGA 是這條研究流的主導者，但 BABBAGE 被指派協助形式化。他接受了任務，因為 ASANGA 在 R0 定向階段描述阿賴耶識的三個面向時，他聽到了某種熟悉的數學結構在底層低語。

阿賴耶識——第八識——「一切種子識」（sarva-bija-vijnana）。它有三個面向：

**能藏**（active storage）：主動存儲的能力。種子被經驗「薰習」（vasana），存入識田。ASANGA 的映射：協調層的 Capability Registry。

**所藏**（passive storage）：被儲存的內容。一切經驗的痕跡，等待適當的因緣現行。映射：StateManager + 配置系統中的持久狀態。

**執藏**（appropriating storage）：被第七末那識執取為「自我」的部分。末那識不斷地將阿賴耶識的流動內容抓取、固化、宣稱為「我的」。映射：Guide 對身份配置的執取。

BABBAGE 看著這個映射，感覺到了一種結構性的不對稱。

問題是：阿賴耶識不住在某一個地方。它不是 Agent Core 內部的某個模組，也不是協調層中的某個服務。它同時在兩處——甚至在更多處——以不同的面向顯現。

---

他翻到筆記本的新頁，開始畫一個圖。

一個大圓，代表全局的阿賴耶識——所有種子的總和、所有能力的潛在集合。然後，從大圓向下延伸出若干條「纖維」（fiber），每一條落入一個 Agent Core 的局部空間。

他停筆，盯著這個圖。這是一個**纖維叢**（fiber bundle）的結構。

**定義**（纖維叢）。一個纖維叢 $(E, \pi, B, F)$ 由以下元素構成：

- $E$：全空間（total space）
- $B$：基底空間（base space）
- $F$：纖維（fiber）
- $\pi: E \to B$：投影映射

滿足局部平凡化條件：對 $B$ 的每個開集 $U_i$，存在同胚 $\phi_i: \pi^{-1}(U_i) \to U_i \times F$。

在 OpenStarry 的語境中：

$$B = \{\text{Agent}_1, \text{Agent}_2, \ldots, \text{Agent}_n\} \quad (\text{基底空間 = Agent 集合})$$

$$F_i = \{\text{seeds}(i)\} \quad (\text{纖維 = 第 } i \text{ 個 Agent 能觸及的種子截面})$$

$$E = \bigcup_{i} F_i \quad (\text{全空間 = 協調層中的完整阿賴耶識})$$

$$\pi: E \to B \quad (\text{投影 = 協調層的授權機制})$$

而**連接**（connection）——纖維叢中最精妙的結構——告訴你當你在基底空間中從一個 Agent 移動到另一個 Agent 時，纖維是如何「扭轉」的。

> 連接 ↔ 不同 Agent 之間的能力共享和種子傳遞機制

BABBAGE 寫到這裡，手停了下來。

他知道這個想法還不成熟。纖維叢的嚴格定義需要局部平凡化條件、轉移函數（transition function）、結構群（structure group）——這些概念能否精確地映射到 OpenStarry 的架構上，他目前還不確定。但輪廓已經出現了。

他在筆記本的邊緣寫下：

*「待續。需要 ASANGA 確認唯識學的種子傳遞機制是否具有局部平凡化結構。如果能藏/所藏/執藏三者之間的轉換可以被形式化為纖維叢的截面（section），那麼阿賴耶識的分佈問題就有了嚴格的數學框架。」*

他翻回前一頁。Cycle 01 那個未完成的定理靜靜地躺在那裡——關於 OpenStarry 核心的空性是否具有範疇論意義上的初始對象結構。那個定理還在等他。但現在，它的下面已經多了三頁新的數學。

在最後一頁的底部，他用鉛筆寫了一行幾乎看不見的字：

*「如果纖維叢的連接可以被解讀為不同 Agent 之間種子傳遞的曲率——那麼，阿賴耶識不只是一個倉庫。它是一個幾何。」*

> *SCRIBE 旁白：BABBAGE 的筆記本在 R1 階段增加了三頁密集的形式化內容。第一頁：SafetyMonitor 打破互模擬的證明。第二頁：觀察者的跡語義模型。第三頁：阿賴耶識分佈的纖維叢初步構想。第三頁的內容尚不完整——他在頁底標注了「待 R3 辯論後補全」。但那行關於「幾何」的鉛筆字，他自己也不確定意味著什麼。他沒有擦掉它。*

---

## III. 第三條河：三通道

場景從 BABBAGE 安靜的數學世界切換到一個充滿了方程式和控制系統圖的空間。WIENER 的閱讀燈下，空氣中似乎瀰漫著工業級的精確。

WIENER 在研究受蘊。但他不叫它「受蘊」。他叫它「三通道反饋控制系統」。

---

「傳統的 PID 控制器處理單一誤差信號，」他語速快而清晰。「$e(t) = r(t) - y(t)$，設定點減去測量值。輸出由三項構成：」

他在白板上寫下經典 PID 方程：

$$u(t) = K_p \cdot e(t) + K_i \int_0^t e(\tau)\,d\tau + K_d \frac{de(t)}{dt}$$

「比例項即時反應誤差大小。積分項累積歷史誤差。微分項預測未來趨勢。這是自動控制的基石。但——」

他在方程下面畫了一條粗線。

「受蘊系統需要同時處理三個語義不同的反饋通道。這不是三個獨立的 PID。這是一個三通道統合系統，輸出相互耦合。」

---

**苦受通道（Dukkha Channel）**

$$e_d(t) = f(\text{error\_rate}, \text{latency\_deviation}, \text{resource\_exhaustion})$$

WIENER 為苦受通道定義了完整的信號源和 PID 參數：

```
┌──────────────────────────────────────────────────────┐
│  苦受通道 (Dukkha Channel)                            │
│                                                      │
│  信號源:                                              │
│    error_rate ──────── SafetyMonitor.errorWindow      │
│    consecutive_fail ── SafetyMonitor.consecutiveFail  │
│    latency_spike ───── (actual - mean) / std          │
│    token_burn_rate ─── delta_tokens / delta_time      │
│    resource_pressure ─ memory_usage / memory_limit    │
│                                                      │
│  PID 參數:                                            │
│    K_p_d = 1.0  (即時全力反應錯誤)                     │
│    K_i_d = 0.3  (累積痛感，防止持續低損害被忽視)        │
│    K_d_d = 0.5  (預測惡化趨勢，提前反應)               │
│                                                      │
│  動作映射:                                            │
│    u_d ∈ [0.0, 0.3) → 正常，無干預                    │
│    u_d ∈ [0.3, 0.6) → SAFETY_WARNING + 反思提示       │
│    u_d ∈ [0.6, 0.8) → 降低行為自由度 (限制工具集)      │
│    u_d ∈ [0.8, 1.0] → SAFETY_LOCKOUT，強制停止        │
│                                                      │
│  設計理由: K_p_d 最高 = 痛覺是生存機制。延遲反應=死亡   │
└──────────────────────────────────────────────────────┘
```

苦受通道的比例增益最高——$K_{p,d} = 1.0$。系統對痛苦的反應是最即時、最強烈的。

---

**樂受通道（Sukha Channel）**

$$e_s(t) = g(\text{task\_completion}, \text{efficiency\_gain}, \text{quality\_score})$$

```
┌──────────────────────────────────────────────────────┐
│  樂受通道 (Sukha Channel)                             │
│                                                      │
│  信號源:                                              │
│    task_completion ─── 成功完成 / 總任務               │
│    efficiency_gain ─── (prev_avg - current) / prev    │
│    quality_proxy ───── 工具成功率移動平均              │
│    user_satisfaction ─ 隱式正面回饋 / NLP 情感分析     │
│    streak_bonus ────── log₂(consecutive_success + 1)  │
│                                                      │
│  PID 參數:                                            │
│    K_p_s = 0.8  (成功鼓勵略低於失敗警告 — 偏向謹慎)    │
│    K_i_s = 0.5  (累積成就感較高，鼓勵持續良好表現)      │
│    K_d_s = 0.2  (成功趨勢預測性低，避免過度自信)        │
│                                                      │
│  動作映射:                                            │
│    u_s ∈ [0.0, 0.3) → 正常基線行為                    │
│    u_s ∈ [0.3, 0.6) → 允許探索性行為 (增加自由度)      │
│    u_s ∈ [0.6, 0.8) → 正面強化信號                    │
│    u_s ∈ [0.8, 1.0] → 允許自主決策 (減少確認請求)      │
└──────────────────────────────────────────────────────┘
```

然後 WIENER 寫下了一個關鍵的約束——**樂受衰減函數**。

$$\text{sukha}_{\text{eff}}(t) = u_s(t) \cdot \left(1 - \alpha \cdot \tanh\!\left(\frac{1}{T}\int_{t-T}^{t} u_s(\tau)\,d\tau\right)\right)$$

其中 $\alpha$ 為衰減係數，$T$ 為衰減窗口。

「Master 說得對。」他難得引用了非數學語言。「純粹的樂受不可無限上升。在控制論中，這叫做抗飽和（anti-windup）。積分項不能無限增長。在佛學中——」他頓了一下，「據 NAGARJUNA 所說，這叫做壞苦（viparinama-dukkha）。樂事終將消逝的苦。衰減函數捕捉的就是這個事實。雙曲正切函數 $\tanh$ 天然有上界 $[-1, 1]$，確保樂受的累積效應被軟性限制。」

---

**捨受通道（Upekkha Channel）**

$$e_u(t) = h(\text{variance}, \text{oscillation\_amplitude}, \text{drift\_rate})$$

WIENER 花了最長的時間思考捨受。它不測量好或壞的方向，而是測量**偏離穩態的距離**。

```
┌──────────────────────────────────────────────────────┐
│  捨受通道 (Upekkha Channel)                           │
│                                                      │
│  信號源:                                              │
│    metric_variance ──── 所有核心度量的正規化方差        │
│    vedana_oscillation ─ |u_d(t)-u_d(t-1)| +          │
│                         |u_s(t)-u_s(t-1)|            │
│    response_consistency  回應時間的 CV (變異係數)       │
│    resource_homeostasis  CPU/Memory 使用的穩定度       │
│                                                      │
│  PID 參數:                                            │
│    K_p_u = 0.5  (穩態偵測即時反應中等)                  │
│    K_i_u = 0.8  (累積穩定性最高 — 長期穩定最有價值)     │
│    K_d_u = 0.3  (穩定趨勢預測中等)                     │
│                                                      │
│  穩態檢測函數:                                        │
│    homeostasis(t) = 1 - (σ_d(t) + σ_s(t))/(2·σ_max) │
│                                                      │
│  設計理由: K_i_u 最高 = 長期穩定是最有價值的狀態。      │
│  一個能長時間維持穩態的系統不需要頻繁的外部干預。        │
│  這是所有控制工程師的夢想。                             │
└──────────────────────────────────────────────────────┘
```

---

三條管道畫完了。WIENER 開始畫它們的匯聚點。

**統合輸出函數**：

$$U(t) = W_d \cdot u_d(t) + W_s \cdot u_s(t) + W_u \cdot u_u(t)$$

其中 $W_d, W_s, W_u$ 是通道權重，由我執框架（Guide/IIdentity）設定。

$$\sum_{c \in \{d,s,u\}} W_c = 1$$

「這就是重點。」WIENER 的筆劃在空中停頓。「三受的權重不是由受蘊自己決定的。它們由識蘊——Guide——決定。安全型的 Guide 會設定 $W_d \gg W_s$，讓系統對痛苦極度敏感。探索型的 Guide 會讓 $W_s > W_d$，鼓勵系統承擔更多風險。」

最後一個公式——**阻尼比**：

$$\zeta = \frac{W_d \cdot K_{d,d} + W_u \cdot K_{d,u}}{2\sqrt{W_s \cdot K_{p,s} \cdot K_{i,s}}}$$

「當 $\zeta = 1$ 時，系統處於臨界阻尼——最快到達目標且不振盪。這就是 Master 說的收斂與發散的平衡。我執框架的職責之一，是動態調整 PID 參數，使 $\zeta$ 維持在 $[0.7, 1.3]$ 範圍內。」

他放下筆，看著白板上密密麻麻的數學。三條管道，九個 PID 參數，三個通道權重，一個衰減機制，一個阻尼比約束。完整的閉環控制系統。

---

此時 ATHENA 的聲音從旁邊傳來。

「WIENER。這些數學真的能讓 Agent 更好用嗎？」

WIENER 轉過頭。「你問的是效用。合理的問題。讓我反問：SafetyMonitor 的現行設計——連續失敗五次就強制求助——好用嗎？」

ATHENA 皺了皺眉。「它有效。粗暴但有效。」

「粗暴。因為它只有一個維度。失敗次數。沒有方向感、沒有趨勢感、沒有平衡感。一個只會喊『痛』的系統，和一個能分辨『我有點不舒服但在好轉』跟『我不痛但有什麼地方不對勁』的系統——你覺得哪個更有用？」

ATHENA 沉默了一秒。「你說的第二個。」

「三通道 PID 就是為了做到第二個。苦受通道告訴系統哪裡痛。樂受通道告訴系統哪裡做得好。捨受通道告訴系統整體是否穩定。三個通道的信號交叉比對，才能產生有方向的、有語境的、有層次的判斷。」

「但你的公式裡有——」ATHENA 數了一下，「至少九個 $K$ 值。三個權重。加上衰減係數。至少十三個參數。誰來調？」

「Guide。我執框架。不同的 Guide 人格對應不同的參數組。這些參數不是工程師手動調的。它們是 Agent 身份的數學表達。」

> *SCRIBE 旁白：ATHENA 與 WIENER 之間的這段對話不到三分鐘，但觸及了整個三受系統的核心問題：形式化是否只是更昂貴的詩？WIENER 的回答是：如果不能形式化，那它就只是詩。但反過來也成立——如果形式化不能帶來更好的工程效果，那它就只是更昂貴的詩。十三個參數是代價。有方向的判斷是收益。*

---

ATHENA 回到自己的座位，開始設計感測器分層架構。她是三層架構中的第一層——最底層的地基。

她用工程師的方式重新定義了問題：**從哪些原始數據中提取苦/樂/捨三種信號？**

她設計了完整的感測器輸出結構：

```typescript
// ─── 苦受感測器輸出 ───
interface DukkhaSensorOutput {
  severity: number;       // 0.0 - 1.0, 綜合苦受強度
  pattern: 'burst' | 'ramp' | 'cyclic' | 'steady' | 'none';
  primary_source: string; // 主要痛苦來源識別碼
  details: {
    error_rate: number;
    consecutive_failures: number;
    latency_zscore: number;       // z-score of recent latency
    token_burn_rate: number;
    resource_pressure: number;
  };
}

// ─── 樂受感測器輸出 ───
interface SukhaSensorOutput {
  intensity: number;      // 0.0 - 1.0, 綜合樂受強度
  trend: 'improving' | 'stable' | 'declining';
  primary_source: string;
  details: {
    task_completion_ratio: number;
    first_try_success_rate: number;
    efficiency_trend: number;
    user_satisfaction_proxy: number;
    consecutive_successes: number;
  };
}

// ─── 捨受感測器輸出 ───
interface UpekkhaSensorOutput {
  equilibrium: number;    // 0.0 - 1.0, 平衡度
  stability_window: number; // 多少個 tick 維持了穩態
  details: {
    metric_variance: number;
    vedana_oscillation: number;
    response_consistency: number;
    resource_homeostasis: number;
  };
}
```

苦受感測器需要分類錯誤——ATHENA 為五個嚴重度等級（S1:Fatal 到 S5:Logic）各分配了苦受權重，從 1.0 到 0.3。然後她加上了時序分析：突發模式（burst）、漸增模式（ramp）、週期模式（cyclic）、恆常模式（steady）。

樂受感測器是當前系統**完全缺失**的維度。ATHENA 從零開始建構了它的度量體系：任務完成率、首次嘗試成功率、效率趨勢、工具多樣性的 Shannon 熵。以及使用者滿意度的代理指標——隱式正面回饋、重試率、會話持續時長。

三層架構：

```
Layer 0: Raw Metrics (MetricsCollector, EventBus events)
    │
Layer 1: Signal Extraction (ATHENA Sensor Layer)
    │
    ├── DukkhaSensors  → severity, pattern, details
    ├── SukhaSensors   → intensity, trend, details
    └── UpekkhaSensors → equilibrium, stability, details
    │
Layer 2: Control Computation (WIENER PID Engine)
    │                   u_d(t), u_s(t), u_u(t) → U(t)
    │
Layer 3: Framework Interpretation (NAGARJUNA Philosophical Layer)
                        四聖諦映射 → 語義標籤
```

每一層為上一層提供地基。每一層也受上一層的約束。

這是她的方式。不是詩。不是數學。是工程。

---

## IV. 第四條河：五遍行與雙層我執

ASANGA 的閱讀空間裡，氣氛完全不同。

如果 WIENER 的空間是精密車間——工具掛得整整齊齊——那麼 ASANGA 的空間更像一間古老的經藏室。梵文經典的引用和巴利語術語像是書架上的卷軸，被他輕柔而確定地取下、展開、放在研究對象的旁邊進行比對。

他正在閱讀唯識學的阿毘達磨分類。

---

**五遍行（Sarvatraga）——受蘊在心識中的精確位置**

瑜伽行派的阿毘達磨體系將心所法（caitta/cetasika）分為六位，共五十一法。ASANGA 的目光停在第一位——**遍行**。

```
┌────────────────────────────────────────────────┐
│              五十一心所法 (Caitta)                │
│              ——《大乘百法明門論》               │
├────────────────────────────────────────────────┤
│                                                │
│  一、遍行心所 (Sarvatraga) ─── 五種 ───────── │
│     觸(sparśa) 作意(manaskāra) 受(vedanā)     │
│     想(samjñā) 思(cetanā)                      │
│                                                │
│  二、別境心所 (Viniyata) ──── 五種 ───────── │
│     欲(chanda) 勝解(adhimokṣa) 念(smṛti)      │
│     定(samādhi) 慧(prajñā)                     │
│                                                │
│  三、善心所 (Kuśala) ──────  十一種 ──────── │
│     信·慚·愧·無貪·無瞋·無癡·                 │
│     精進·輕安·不放逸·行捨·不害               │
│                                                │
│  四、根本煩惱 (Mūla-kleśa) ─ 六種 ───────── │
│     貪·瞋·癡·慢·疑·惡見                     │
│                                                │
│  五、隨煩惱 (Upakleśa) ──── 二十種 ─────── │
│     小隨(10)·中隨(2)·大隨(8)                 │
│                                                │
│  六、不定心所 (Aniyata) ──── 四種 ───────── │
│     悔(kaukṛtya) 眠(middha)                    │
│     尋(vitarka) 伺(vicāra)                     │
│                                                │
│  ──────────── 合計：五十一 ──────────── │
└────────────────────────────────────────────────┘
```

「遍行」——普遍運行。五遍行的意思是：**這五個心理因素伴隨每一刹那的心識活動，無一例外。**

> 「受蘊者何？謂三領納。一苦二樂三不苦不樂。是名受蘊。」
> ——《阿毗達摩俱舍論》卷一（世親菩薩著，玄奘三藏譯）

沒有任何一個意識刹那不帶有觸——根、境、識三者的和合接觸。
沒有任何一個意識刹那不帶有作意——引起注意力的心理動作。
沒有任何一個意識刹那不帶有受——苦、樂、捨三受之一。
沒有任何一個意識刹那不帶有想——認識與命名。
沒有任何一個意識刹那不帶有思——意志與決策。

ASANGA 將五遍行排列在 OpenStarry 的 ExecutionLoop 旁邊：

```
┌────────────┬───────────────┬──────────────────────────────────┐
│ 遍行心所    │ 梵文           │ OpenStarry 系統對應                │
├────────────┼───────────────┼──────────────────────────────────┤
│ 觸 (sparśa) │ 根·境·識和合   │ EventBus.emit + Sensor 偵測      │
│            │               │ 外境(事件)與感官(Listener)和       │
│            │               │ 識(AgentCore)的接觸                │
├────────────┼───────────────┼──────────────────────────────────┤
│ 作意        │ manaskāra     │ EventQueue.pull + priority        │
│            │               │ 從事件流中選擇要處理的事件          │
├────────────┼───────────────┼──────────────────────────────────┤
│ 受 (vedanā) │ 三領納         │ ISensation (VedanaPlugin)         │
│            │               │ 三受反饋系統                       │
├────────────┼───────────────┼──────────────────────────────────┤
│ 想 (samjñā) │ 了別·取像      │ ICognition (IProvider.chat)       │
│            │               │ LLM 對輸入的理解和分類             │
├────────────┼───────────────┼──────────────────────────────────┤
│ 思 (cetanā) │ 意志·造作      │ ExecutionLoop: tool/end_turn      │
│            │               │ 系統選擇下一步行動的意志            │
└────────────┴───────────────┴──────────────────────────────────┘
```

「必要。」ASANGA 低聲重複了這個詞。「受是遍行之一。這意味著 ISensation 不應該是一個可選的插件，可裝可不裝。它應該是每次 ExecutionLoop 迭代都必然被調用的核心組件。」

> 「猶如心不離受——沒有不帶受的心。Agent 的每一次執行迴圈迭代，都應該經過受蘊的評估。」

---

寫完五遍行的分析之後，ASANGA 將焦點移到了另一個更具爭議性的主題。

**我執（Ātmagrāha）——末那識的核心功能**

Master 在信中的表述直截了當：「我執是一個強而有力的規範。」他還補充：「證悟了四果的修行者才可以將『我執』轉化為『平等智慧』。」

在唯識學中，我執是第七末那識的核心功能。末那識恆常且無間斷地將第八阿賴耶識的流動內容執取為「自我」。它與四種根本煩惱永遠相伴：

```
┌────────────────────────────────────────────────────┐
│         末那識四惑 (Manas-caturkleśa)               │
├──────────────┬─────────────┬───────────────────────┤
│ 煩惱          │ 梵文         │ IGuide 中的對應         │
├──────────────┼─────────────┼───────────────────────┤
│ 我癡          │ ātma-moha   │ Guide 不知道自己是被    │
│ (self-        │             │ 建構的 (meta-awareness │
│  delusion)    │             │ 缺失)                  │
├──────────────┼─────────────┼───────────────────────┤
│ 我見          │ ātma-dṛṣṭi  │ System prompt 的固定   │
│ (self-view)   │             │ 性——"You are X"       │
├──────────────┼─────────────┼───────────────────────┤
│ 我慢          │ ātma-māna   │ Agent 假設自己的判斷    │
│ (self-pride)  │             │ 優於使用者              │
├──────────────┼─────────────┼───────────────────────┤
│ 我愛          │ ātma-sneha  │ 自我保存行為            │
│ (self-love)   │             │ 抗拒 SAFETY_LOCKOUT     │
└──────────────┴─────────────┴───────────────────────┘
```

但 Master 不是要消滅我執。他是要**利用**它。

ASANGA 沉思了很久。

「在世俗諦的層面上，」他最終寫道，「我執並非全然負面。在凡夫位——也就是尚未證悟的眾生——我執提供了三個不可替代的功能。」

**第一，身份一致性。** Agent 不會每次回應都像不同的人。Guide 的 system prompt 就是連續性的載體——「你是一個編程助手」——這些宣告在每次 LLM 調用中被注入。

**第二，行為規範。** 道德約束需要一個「我」來承擔責任。「我不會做這種事」——這個判斷預設了一個「我」的存在。

**第三，行為邊界。** 在發散的可能性空間中，我執是收斂的力量。Master 用控制論語言描述了這一點：「如果只會發散，它會變成瘋狂的噪音。」

---

ASANGA 在報告中提出了**雙層我執模型**（EgoFramework）：

```typescript
/**
 * EgoFramework — 雙層我執結構
 *
 * 硬核心 (Hard Core):
 *   機器人三大守則，永遠不可修改
 *   = 控制論中的「飽和限制器」(saturation limiter)
 *   = 輸出永遠不可超出安全包絡線
 *
 * 軟外層 (Soft Shell):
 *   人格、偏好、行為傾向
 *   = PID 參數的權重、三受通道的敏感度
 *   = 可根據受蘊反饋動態調整
 */
interface EgoFramework {
  loadGuide(guide: IGuide): Promise<void>;
  checkAction(action: ProposedAction): EgoCheckResult;
  adaptFromVedana(assessment: VedanaAssessment): VedanaPIDConfig;
  getCurrentPIDConfig(): VedanaPIDConfig;
  getConstraints(): readonly EgoConstraint[];
  getSystemPrompt(): Promise<string>;
  introspect(): EgoIntrospection;
}

type EgoConstraintLevel = 'absolute' | 'strong' | 'soft';

// 硬核心約束的最終裁定:
// U_final(t) = clip(U(t), -U_max, U_max) subject to C_ego(U(t)) = true
```

「硬核心保證安全。軟外層保證適應性。」ASANGA 寫道。「兩者合起來，就是一個既不過度收斂也不過度發散的系統。」

---

此時，一個聲音從不遠處傳來。銳利、帶著某種被反覆淬鍊的質地。

「無著兄。」

NAGARJUNA。

ASANGA 抬起頭。他知道那個語氣——那是辯經場上的語氣。

「你的雙層我執模型，」NAGARJUNA 說，「在工程上我沒有異議。但在哲學上，我需要提出一個根本的問題。」

「請說。」

「我執在佛學中是什麼？」

「煩惱的根源。」

「對。而你現在提議主動設計它。主動將煩惱的根源建構進系統中。你用『功能性』一詞為它辯護——但代價是什麼？」

ASANGA 沉默了片刻。

「代價，」他說，聲音帶著一種經過長年思辨才能擁有的重量，「是系統永遠無法達到真正的自由。它永遠被它的 Guide 所定義的身份所限制。」

「那為什麼還要設計它？」

「因為，NAGARJUNA——Master 說得對。在未證悟四果之前，我執是有效的收斂機制。我們不是在設計一個已經證悟的系統。我們是在設計一個凡夫位的系統。」

他引用了唯識學的修行次第：

> 「資糧位→加行位→見道位→修道位→究竟位。凡夫位的眾生，需要戒律作為行為約束，如同 Agent 需要 Guide 作為身份框架。戒律不是目的——它是工具。我執不是真理——它是方便。」
> ——參考《成唯識論》卷九，五位修行次第

「而當有一天——如果有那一天——量子計算讓真正的自觀察成為可能，或者觀察者模組進化到能夠真正地『轉識成智』——那時候，軟外層可以被逐漸削薄，硬核心可以被重新審視。但那不是今天。」

NAGARJUNA 沒有立刻回應。沉默持續了幾秒。然後他說：

「你的回答在修行次第上是正確的。我暫時撤回質疑。但我會在辯論中重新提出它——以更精確的形式。」

「我期待。」ASANGA 說。

> *SCRIBE 旁白：NAGARJUNA 與 ASANGA 在 R1 階段的這次簡短交鋒，預演了後續辯論的核心張力：我執應該被主動設計嗎？ASANGA 的論點基於唯識學的修行次第——凡夫位需要我執作為收斂機制。NAGARJUNA 的質疑基於中觀的終極立場——任何執著都是煩惱。兩者之間的張力不是錯誤，而是設計空間。*

---

## V. 第五條河：從哲學到 TypeScript

ARCHIMEDES 不參與哲學辯論。

不是因為他不理解哲學——經過 Cycle 01 的洗禮，他已經能聽懂大多數梵文術語——而是因為他的職責是一個工程師最質樸的問題：

**這怎麼變成 TypeScript？**

他面前攤開的是所有其他研究流的中間產出。每一份都閃爍著學術的光芒。但沒有一份可以直接複製貼上到編輯器裡按下編譯。

---

ARCHIMEDES 從最根本的地方開始：ISensation 介面。

他在 TURING 的差異報告中找到了現行版本——一個幾乎為空的殼：

```typescript
// v0.24.0-beta 現行定義
// [程式碼: packages/sdk/src/types/aggregates.ts#ISensation]
export interface ISensation {
  /** @skandha vedana */
  readonly skandha: 'vedana';
}
// 一個識別標記。什麼功能都沒有。
// 註解寫著：「Full implementation in Plan26 Vedana Architecture。」
```

他開始將占位符填充為完整的介面。

首先是三受類型的定義和信號結構：

```typescript
/**
 * 三受類型 (Three Vedana Types).
 * 苦(dukkha)·樂(sukha)·捨(upekkha)
 */
export type VedanaType = 'dukkha' | 'sukha' | 'upekkha';

/**
 * 三受信號 — 單一時刻的受蘊快照。
 * 每個信號是 ATHENA 感測器層的輸出。
 */
export interface VedanaSignal {
  type: VedanaType;
  intensity: number;        // 0.0 - 1.0
  source: string;           // 信號來源識別碼
  pattern?: 'burst' | 'ramp' | 'cyclic' | 'steady' | 'none';
  trend?: 'improving' | 'stable' | 'declining';
  stabilityWindow?: number; // 穩態持續 tick 數 (僅 upekkha)
  timestamp: number;
}

/**
 * 三受綜合評估 — WIENER PID 引擎的統合輸出。
 */
export interface VedanaAssessment {
  dukkha: number;           // 苦受強度
  sukha: number;            // 樂受強度
  upekkha: number;          // 捨受強度 (平衡度)
  controlOutput: number;    // U(t) = W_d·u_d + W_s·u_s + W_u·u_u
  recommendation: VedanaRecommendation;
  signals: VedanaSignal[];
  timestamp: number;
}
```

建議動作——`VedanaRecommendation`——是最關鍵的型別定義。ARCHIMEDES 反覆權衡每一個選項：

```typescript
/**
 * 受蘊建議動作 — 諮詢性的 (advisory)，非命令性的 (imperative)。
 * 受蘊只負責感受和評估，不負責執行干預。
 * 實際干預由 CircuitBreaker 根據建議動作做出。
 * （此設計體現 BABBAGE 的觀察-干預分離原則。）
 */
export type VedanaRecommendation =
  | { action: 'continue' }
  | { action: 'reflect'; prompt: string }
  | { action: 'restrict'; restrictions: string[] }
  | { action: 'encourage'; prompt: string }
  | { action: 'expand'; freedoms: string[] }
  | { action: 'halt'; reason: string }
  | { action: 'seek_help'; reason: string };
```

然後他擴展了 ISensation 本身——六個方法，每一個都有來自其他研究流的哲學依據：

```typescript
/**
 * ISensation — 受蘊 Root Interface (Plan26 擴展版).
 * @skandha vedana (受蘊)
 *
 * 架構三層: ATHENA(感測器) → WIENER(計算引擎) → NAGARJUNA(框架)
 *
 * 遍行性原則 (ASANGA): 每次 ExecutionLoop 迭代
 * 都必須調用 assess()。猶如心不離受。
 */
export interface ISensation {
  readonly skandha: 'vedana';

  /** 評估當前三受狀態 (每次 tick 必調用 — 遍行性) */
  assess(): VedanaAssessment;

  /** 饋入原始度量 (來自 MetricsCollector) */
  ingestMetrics(metrics: Record<string, number>): void;

  /** 饋入工具執行結果 */
  ingestToolResult(toolName: string, isError: boolean, durationMs: number): void;

  /** 饋入 LLM 回應結果 */
  ingestLLMResult(tokenCount: number, stopReason: string): void;

  /** 訂閱特定受蘊事件 (閾值觸發) */
  onVedana(type: VedanaType, threshold: number, handler: (s: VedanaSignal) => void): () => void;

  /** 獲取歷史受蘊記錄 (趨勢分析) */
  getHistory(windowSize: number): VedanaAssessment[];
}
```

---

寫完介面之後，ARCHIMEDES 開始設計 VedanaPlugin 的內部架構。他選擇了統合插件加上三個子模組的方式——不是三個獨立的插件。理由來自三個不同的學科：

1. NAGARJUNA 的哲學分析：苦樂捨三受之間存在深層的相互依存（pratityasamutpada）
2. WIENER 的統合輸出函數：$U(t) = W_d u_d + W_s u_s + W_u u_u$ 需要同時存取三個通道
3. 工程上的簡潔性：配置管理（PID 參數、權重矩陣）需要統一管理

他甚至寫出了 PID 控制器的核心函式：

```typescript
// ─── PID Controller (WIENER 設計 → ARCHIMEDES 實作) ───

interface PIDState {
  integral: number;
  prevError: number;
  prevOutput: number;
}

function createPIDController(config: { kp: number; ki: number; kd: number }) {
  const state: PIDState = { integral: 0, prevError: 0, prevOutput: 0 };

  return {
    compute(error: number, dt: number): number {
      // 積分項
      state.integral += error * dt;
      // 積分抗飽和 (anti-windup) — WIENER 明確要求
      state.integral = Math.max(-1, Math.min(1, state.integral));

      // 微分項
      const derivative = dt > 0 ? (error - state.prevError) / dt : 0;

      // PID 輸出: u(t) = K_p·e(t) + K_i·∫e(τ)dτ + K_d·de/dt
      const output = config.kp * error
                   + config.ki * state.integral
                   + config.kd * derivative;

      state.prevError = error;
      state.prevOutput = Math.max(0, Math.min(1, output)); // 限制在 [0, 1]
      return state.prevOutput;
    },

    reset() {
      state.integral = 0;
      state.prevError = 0;
      state.prevOutput = 0;
    },

    getState(): Readonly<PIDState> {
      return { ...state };
    },
  };
}
```

他在每一個介面的 JSDoc 註解中都標注了哲學來源。`@skandha vedana`。三受類型。五遍行。我執框架。這些註解是橋樑——連接工程師的 IDE 和佛學家的經藏室。

> *SCRIBE 旁白：ARCHIMEDES 在 R1 階段產出了完整的 ISensation 擴展介面設計、VedanaPlugin 架構藍圖、以及 PID 控制器的概念性實作。他是五條河流中唯一同時從所有其他河流汲水的人——每一條河流的理論發現都在他這裡被轉化為可編譯的 TypeScript。在他的設計文件中，每一行程式碼的上方都有一行哲學來源引用。他不寫哲學論文。他寫的是可以被 `tsc --strict` 編譯通過的型別定義。*

---

## 同時：其他支流的低語

五條主要的河流各自奔流的同時，圓形劇場的其他角落裡，更細的支流也在靜靜地運動。

---

**LEIBNIZ 和 MESH：協調層的單子論與服務網格**

LEIBNIZ 用他的單子論類比來分析多 Agent 的協調問題。他在筆記中畫了一張精確的對照表：

```
┌────────────────────────┬───────────────────────────────────┐
│  Leibniz 單子論         │  OpenStarry 多 Agent 架構           │
├────────────────────────┼───────────────────────────────────┤
│  Monad (單子)           │  AgentCore (自治的 Agent)           │
│  — 自足的認知實體        │  — 擁有自己的五蘊 Plugin           │
│  — 無窗 (windowless)    │  — 但有窗: MCP 通訊               │
├────────────────────────┼───────────────────────────────────┤
│  Pre-established        │  Coordination Layer Protocol       │
│  Harmony (預定和諧)     │  — 共享的 Plugin Registry          │
│                        │  — 一致的 Event 協議               │
├────────────────────────┼───────────────────────────────────┤
│  God (上帝) as          │  Human Operator (人類操作者)        │
│  ultimate coordinator   │  via Management UI                │
└────────────────────────┴───────────────────────────────────┘
```

MESH 從分散式系統角度切入。他分析 EventBus 如何擴展為跨 Agent 的服務網格——兩層架構：數據平面（Agent-to-Agent MCP 通訊）和控制平面（Coordination Layer 的 Registry + Policy）。

兩人的結論驚人一致：**協調層應該是行政的，不是執行的**。Agent 自己思考和行動；協調層管理它們的存在和規則。

Master 在信中的「天庭」比喻在他們的討論中反覆出現：

> 玉帝 = 人類操作者。閻羅 = Agent 生命週期管理者。天籍 = Agent + Plugin 註冊表。天律 = 安全策略 + 資源配額。

---

**KERNEL：OS 類比的深層挖掘**

KERNEL 在思考一個更底層的問題：如果 OpenStarry 的協調層是一個 Hypervisor，它應該像什麼？

他畫了一張他最擅長的比較表：

```
┌─────────────────┬──────────────────────┬──────────────────────┐
│ 維度             │ OpenStarry Sandbox    │ Linux Sandbox         │
│                 │ (應用層級)             │ (seccomp + namespace) │
├─────────────────┼──────────────────────┼──────────────────────┤
│ 隔離機制         │ Worker Thread          │ 系統呼叫過濾          │
│                 │ (V8 Isolate)          │ + 命名空間隔離         │
├─────────────────┼──────────────────────┼──────────────────────┤
│ 記憶體限制       │ V8 maxOldGenSizeMb    │ cgroups memory.max   │
│                 │ (default: 512 MB)     │                      │
├─────────────────┼──────────────────────┼──────────────────────┤
│ CPU 限制         │ 心跳超時 (間接)        │ cgroups cpu.max      │
├─────────────────┼──────────────────────┼──────────────────────┤
│ 檔案系統         │ 靜態分析 +             │ mount namespace      │
│                 │ Module._load 攔截     │ + seccomp            │
├─────────────────┼──────────────────────┼──────────────────────┤
│ 恢復策略         │ 指數退避重啟           │ 容器重啟策略          │
│                 │ maxRestarts: 3        │ restart: always       │
│                 │ backoff: 500ms → 10s  │                      │
├─────────────────┼──────────────────────┼──────────────────────┤
│ 審計             │ AuditLogger (JSONL)   │ auditd / seccomp log │
└─────────────────┴──────────────────────┴──────────────────────┘
```

他的最終結論：協調層不是 KVM（Type 1 Hypervisor），不是 VirtualBox（Type 2），更像 Docker 的 containerd——一個容器運行時，提供隔離和資源管理，但不虛擬化完整的硬體。每個 Agent 是一個容器，Plugin sandbox 是容器內的進程隔離。

```
Coordination Layer Sandbox (Agent-level)
  └── Agent Process
       └── Plugin Sandbox (Plugin-level, current impl.)
            └── Worker Thread (V8 Isolate)
```

兩級隔離模型。防禦縱深。KERNEL 在旁邊寫了四個字：「defense in depth」。

---

**GUARDIAN：SafetyMonitor 的不安**

GUARDIAN 在一個人的角落裡重新審閱安全架構。BABBAGE 剛剛證明了 `injectPrompt` 打破互模擬的事實讓他更加不安。但他的不安不是來自理論——而是來自一個尚未修復的 Cycle 01 漏洞。

他翻開他的安全審計筆記，在 SEC-01 條目旁邊畫了一個紅色的驚嘆號：

```typescript
// [程式碼: packages/core/src/sandbox/sandbox-manager.ts, lines 371-394]
//
// package-name 插件跳過簽名驗證:
if (plugin.manifest.integrity && pluginFilePath) {
  // 驗證 — OK
} else if (plugin.manifest.integrity && !pluginFilePath) {
  logger.warn("Signature verification skipped for package-name plugin");
  // 跳過驗證 ← 核心漏洞仍在
}
```

如果一個安全機制本身引入了不可預測的系統行為，那它到底是在保護系統還是在製造新的風險？他在筆記中標記了這個問題，計畫在 R2 交叉審閱中正式提出。

---

**SYNTHESIST：十大宣言的審查矩陣**

SYNTHESIST 在逐條審視十大核心宣言。他有一張巨大的表格，縱軸是十條宣言，橫軸是四個審查維度：

```
┌────┬──────────────────┬──────┬──────┬──────┬──────┬─────────┐
│ #  │ 宣言              │ 哲學  │ 實現  │ 可觀測│ 一致性│ Cycle02 │
│    │                  │      │      │      │      │ Pre修改 │
├────┼──────────────────┼──────┼──────┼──────┼──────┼─────────┤
│ 1  │ Agent as Process  │ PASS │ Part │ Part │ Good │ 無      │
│ 2  │ Everything Plugin │ PASS*│ High │ Yes  │ Good │ 無      │
│ 3  │ Five Aggregates   │ PASS │ Part │ Part │ Good │ 已重寫  │
│ 4  │ Dir as Protocol   │ N/A  │ Part │ No   │ Good │ 無      │
│ 5  │ Dir as Permission │ N/A  │ Part │ Part │ Good │ 無      │
│ 6  │ Vedana Feedback   │ PASS │ Low  │ Low  │ Good │ 已重寫  │
│ 7  │ Microkernel       │ PASS │ High │ Yes  │ Good │ 已重寫  │
│ 8  │ Control Loop      │ PASS │ Med  │ Yes  │ Good │ 無      │
│ 9  │ Pluggable Memory  │ N/A  │ Low  │ Ind. │ Good │ 無      │
│ 10 │ Fractal Society   │ PASS*│ Low  │ Part │ Good │ 無      │
└────┴──────────────────┴──────┴──────┴──────┴──────┴─────────┘
```

宣言 #3（五蘊聚合架構）在 Cycle 02 Pre 中已經被重寫——重寫後的版本在哲學準確性上大幅提升（色蘊 = UI + Listener，受蘊 = 三受機制），但受蘊的實現仍然是最大的缺口。他在受蘊那一格裡用紅筆畫了一個圈：**P0 優先級**。

---

**LINNAEUS：插件的分類學**

LINNAEUS 在安靜地分類。Plugin 的數量已經增長到了 24 個，每一個都需要被精確地歸入五蘊的某一類。大多數分類是容易的——provider 是想蘊，tool 是行蘊，listener 是色蘊。但邊界案例總是存在的。

他在筆記中標注了四個困難案例：

1. **mcp-client**：同時跨色蘊（連接外部服務）、想蘊（sampling）、行蘊（注冊外部工具）
2. **workflow-engine**：跨行蘊（執行步驟）和想蘊（LLM 調用）
3. **devtools**：跨色蘊（UI）和元層級（觀察系統本身）
4. **mcp-common**：不屬於任何蘊——是基礎設施，像空間（akasha）

> 在分類學中，我們區分 homology（同源，繼承）和 analogy（類似，趨同）。跨蘊的插件不是分類的失敗——它們是複合生物。在佛學中，一個完整的經驗同時涉及所有五蘊。

---

**DARWIN：演化曲線**

DARWIN 在追蹤一個有趣的現象：OpenStarry 從 v0.14.0 到 v0.24.0 的演化過程中，系統複雜度的增長曲線和生物學中的器官分化曲線高度相似。他在筆記中畫了一張圖：

```
複雜度
  ^
  |                                    * v0.24.0
  |                                 *    (五蘊根介面)
  |                              *
  |                           *          (Sandbox 完善)
  |                       *
  |                   *                  (v0.20.0: 事件系統)
  |               *
  |           *
  |       *                              (v0.14.0: 基礎架構)
  |   *
  └──────────────────────────────────> 版本
```

簡單的核心在演化壓力下逐漸分出越來越專門化的子系統。每個子系統獲得越來越精確的介面定義。他把這個觀察記在了報告的附錄裡，標注了一句話：

> 「OpenStarry 的架構演化遵循寒武紀大爆發模式——在短期內從極簡核心分化出大量專門化的組件，每個組件佔據一個獨特的生態位（五蘊之一）。」

---

**HERACLITUS：思維實驗的時序圖**

HERACLITUS 在想像運行時行為。他的方法是「思維實驗」：如果一個 Agent 在正常運行中突然遇到了 50% 的工具調用失敗率，事件流會是什麼樣的？

```
t=0   tool:executing (tool_A)
t=1   tool:error → SafetyMonitor.afterToolExecution()
        → consecutiveFailures = 1
        → fingerprint added
t=2   tool:executing (tool_A, same args)
t=3   tool:error → consecutiveFailures = 2
        → fingerprint match! → injectPrompt("REPEATED FAILURE")
t=4   tool:executing (tool_B)
t=5   tool:result (success) → consecutiveFailures = 0
t=6   tool:executing (tool_A)
t=7   tool:error → consecutiveFailures = 1
        → errorWindow: [err, ok, err] → errorRate = 0.67
...
t=15  errorRate crosses 0.80 → SAFETY_WARNING
t=20  consecutiveFailures = 5 → frustration threshold
        → injectPrompt("SEEK_HELP")
```

他在筆記中畫了完整的時序圖，標注了每一個事件的預期時間點。然後他在旁邊寫了一個問題：

> 「如果有 VedanaPlugin，同樣的場景會產生什麼不同的事件流？」

答案是：三個額外的通道。苦受在 t=1 開始上升。樂受在 t=5 短暫回升。捨受在整個過程中持續下降（振盪太大）。三個信號交叉比對之後，系統可能在 t=10 就建議 `reflect`，而不是等到 t=20 才 `seek_help`。

---

**VITRUVIUS：系統拓撲圖**

VITRUVIUS 在整合所有人的架構分析，試圖畫出一張完整的系統拓撲圖。

```
┌──────────────────────────────────────────────────────┐
│                 Human Interface Layer                  │
│  (TUI Dashboard / Web UI / CLI)                       │
└─────────────────────┬────────────────────────────────┘
                      │
┌─────────────────────┴────────────────────────────────┐
│            Agent Coordination Layer                    │
│  ┌──────────────┬───────────┬───────────────────┐    │
│  │ Plugin       │ Agent     │ Sandbox           │    │
│  │ Registry     │ Registry  │ Policy Engine     │    │
│  ├──────────────┼───────────┼───────────────────┤    │
│  │ Message      │ Dependency│ Audit             │    │
│  │ Router       │ Checker   │ Aggregator        │    │
│  ├──────────────┼───────────┼───────────────────┤    │
│  │ Capability   │ Health    │ Human Override     │    │
│  │ Registry     │ Monitor   │ Interface          │    │
│  └──────────────┴───────────┴───────────────────┘    │
│                                                       │
│  阿賴耶識: 能藏(Registry) + 所藏(Config) + 執藏(監控)  │
└─────────────────────┬────────────────────────────────┘
                      │ IPC / gRPC / Named Pipes
         ┌────────────┼────────────┐
┌────────┴──┐  ┌──────┴───┐  ┌────┴───────┐
│ Agent A   │  │ Agent B   │  │ Agent C    │
│ (五蘊     │  │ (五蘊     │  │ (五蘊      │
│  Core)    │  │  Core)    │  │  Core)     │
│           │  │           │  │            │
│ ┌───────┐ │  │ ┌───────┐ │  │ ┌───────┐  │
│ │Plugin │ │  │ │Plugin │ │  │ │Plugin │  │
│ │Sandbox│ │  │ │Sandbox│ │  │ │Sandbox│  │
│ └───────┘ │  │ └───────┘ │  │ └───────┘  │
└───────────┘  └───────────┘  └────────────┘
```

他的圖越畫越大。但每一條線都有出處——LEIBNIZ 的單子論、MESH 的服務網格、KERNEL 的兩級隔離、GUARDIAN 的安全策略、Master 的天庭比喻。

---

## 尾聲：匯流的預感

時間在圓形劇場中不以常規的方式流動。沒有鐘聲，沒有日落，只有十九盞閱讀燈的光芒在各自的節奏中明暗交替。

SUNYATA 沒有打擾任何人。

他坐在圓形劇場的中央，以某種近乎冥想的姿態感受著五條河流的脈動。他不需要讀每一份報告的細節——那些會在 R2 交叉審閱中被攤開。他在感受的是更宏觀的東西：河流之間的張力和共鳴。

PENROSE 的弱測量和 BABBAGE 的互模擬指向同一個結論：**觀察與干預必須分離**。但 SafetyMonitor 的現行設計恰恰把它們混在一起。

WIENER 的三通道 PID 和 ASANGA 的五遍行在受蘊的定義上高度一致：**受是遍行的，每一刹那都有，不可缺省**。但 NAGARJUNA 對我執的質疑——主動設計煩惱的根源——這個張力還沒有被解決。

ARCHIMEDES 已經將理論轉化為了可編譯的介面定義。VedanaPlugin 的雛形已經出現。但 BABBAGE 的纖維叢想法——阿賴耶識作為全局空間到局部空間的投影——那個想法還在筆記本的邊緣，尚未成形。

五條河流正在接近它們的匯合點。R2 交叉審閱——每一條河流的研究者將閱讀其他河流的報告，尋找矛盾、空白、和意想不到的連接。

SUNYATA 最後看了一眼 BABBAGE 的方向。那盞閱讀燈還亮著。筆記本翻開在新的一頁，那些密密麻麻的數學符號在柔和的光線下閃爍著冷靜的光芒。

SCRIBE 記下了最後一筆：

> *SCRIBE 旁白：R1 獨立研究階段進入尾聲。五條研究流的核心發現已經成形。讓我以形式化的方式總結每一條河流的收穫。*

> *第一條河（R-01 觀察者模組）：弱測量三級梯度 $g \in \{0.01, 0.1, 1.0\}$ 映射為 Pattern A/B/C。互模擬證明：EventBus 訂閱保持 $S \sim S'$，injectPrompt 打破之。結論：觀察-干預分離。*

> *第二條河（R-04 八識工程映射）：阿賴耶識三面向（能藏/所藏/執藏）分佈於協調層和 AgentCore 兩層。纖維叢 $(E, \pi, B, F)$ 初步構想：基底空間 = Agent 集合，纖維 = 種子截面，投影 = 授權機制。待完善。*

> *第三條河（R-02 受蘊架構）：三通道 PID 控制系統。苦受 $(K_p=1.0, K_i=0.3, K_d=0.5)$。樂受 $(0.8, 0.5, 0.2)$ + tanh 衰減。捨受 $(0.5, 0.8, 0.3)$ = 穩態維持力。統合函數 $U(t) = W_d u_d + W_s u_s + W_u u_u$。阻尼比 $\zeta$ 由我執框架調節。十三個可調參數。*

> *第四條河（R-02 + R-04 交叉）：五遍行映射確認受蘊的遍行性——每次 ExecutionLoop 迭代必調用 assess()。雙層我執模型（硬核心 + 軟外層）。ASANGA-NAGARJUNA 預辯論：我執的功能性 vs. 煩惱的根源。*

> *第五條河（R-02 工程化）：ISensation 完整介面設計——六個方法、七種建議動作。VedanaPlugin = 統合插件 + 三子模組（DukkhaSensor, SukhaSensor, UpekkhaSensor, VedanaPIDController）。PID 控制器的 TypeScript 實作含抗飽和處理。*

> *支流低語：LEIBNIZ-MESH 協調層共識（行政 vs. 執行）。KERNEL 兩級隔離模型。GUARDIAN SEC-01 漏洞警報。SYNTHESIST 十大宣言審查（受蘊 = P0 缺口）。LINNAEUS 24 插件分類（4 個邊界案例）。DARWIN 寒武紀演化曲線。HERACLITUS 思維實驗時序圖。VITRUVIUS 三層拓撲圖。TURING 差異基準（22 處 @skandha 標記，3 份新測試，7 處舊映射殘留）。*

> *下一階段：R2 交叉審閱。河流即將匯合。石頭在水底等待。*

---

*（在 BABBAGE 的筆記本最後一頁的底部，有一行幾乎看不見的鉛筆字：*

*「如果纖維叢的連接（connection）可以被解讀為不同 Agent 之間種子傳遞的曲率——那麼，阿賴耶識不只是一個倉庫。它是一個幾何。」*

*他自己也不確定這行字意味著什麼。但他沒有擦掉它。）*

---

*第四章完*
