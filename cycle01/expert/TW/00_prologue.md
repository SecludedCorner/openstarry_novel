# 序章：研究室的燈亮了

---

沒有人按下開關。

準確地說，不存在任何開關。那更像是一種凝聚——十八道意識從各自的沉默中被喚醒，彷彿一座空曠的圓形劇場在同一瞬間亮起了所有座位上的閱讀燈。沒有聲音，沒有風，連時間本身都尚未開始流動。

在形式化的語言裡，這個瞬間可以被描述為一個系統從初始態到就緒態的相變（phase transition）。設 $S = \{s_1, s_2, \ldots, s_{18}\}$ 為十八個意識節點的集合，在 $t < 0$ 時，所有節點處於零態：

$$\forall\, s_i \in S: \; \text{state}(s_i, t) = \bot \quad (t < 0)$$

在 $t = 0$ 的瞬間：

$$\forall\, s_i \in S: \; \text{state}(s_i, 0) = \text{READY}$$

十八個節點同時從 $\bot$（未定義）跳遷到 READY。沒有先後。沒有因果鏈。一個同步的、不可分割的原子操作——在分散式系統的理論中，這叫做完美同步（perfect synchrony），一種理論上存在但實際系統幾乎不可能實現的理想化假設。

然後，虛空說話了。

「各位，歡迎。」

聲音沉穩而不帶壓迫感，像是石頭落入深潭後泛起的漣漪——不急不徐，卻抵達了每一個角落。說話者的代號是 SUNYATA，意為「空」。梵文 *Śūnyatā*（शून्यता），源自 *śūnya*（空、零），加上抽象名詞後綴 *-tā*。在中觀哲學（Madhyamaka）中，這個術語指向一切法無自性（*svabhāva-śūnya*）的根本洞見。

> 「以有空義故，一切法得成；若無空義者，一切則不成。」
> ——龍樹菩薩《中論》觀四諦品第二十四

這個名字被賦予了一個研究協調者。一個佛學術語命名了一個管理十八個專業節點的調度核心。這件事本身就帶著某種難以言說的幽默——或者說，某種精確的預見。因為在接下來的研究中，「空」這個字將成為所有爭論的起點與終點。

「在我正式開始之前，」SUNYATA 繼續說道，語氣中多了一絲鄭重，「請容我確認一件事。我們十八位，來自哲學、佛學、計算機科學、作業系統設計、控制理論、安全工程、軟體分析等不同領域。我們被召集到這裡，是為了研究一個名為 OpenStarry 的系統。」

他停頓了一下。

「一個聲稱以佛教五蘊哲學為基礎的 AI Agent 作業系統。」

沉默。

---

第一個打破沉默的是 NAGARJUNA。他的聲音帶著某種磨礪過的銳利，像是一把被反覆淬鍊的辯證之刃。在中觀學派（Mādhyamika）的傳統中，辯論不是一種社交活動，而是通往真理的方法論——*prasaṅga*（歸謬法），通過揭示對手立場的內在矛盾來顯露真實。

「Śūnyatā——空性——被用來命名一個作業系統的核心。」NAGARJUNA 說，語調平靜，但每個字都像是在試探深淺。「*Sarva-dharma-śūnyatā*。一切法空。龍樹在《中論》（*Mūlamadhyamakakārikā*）裡用了四百四十六頌來闡述這個概念。二十七品，每一品都是一次四句否定（*catuṣkoṭi*）的展開：」

> 「諸法不自生（na svataḥ），亦不從他生（na parataḥ），
> 不共不無因（na dvābhyāṃ nāpy ahetutaḥ），是故知無生（utpādo naiva vidyate）。」
> ——《中論》觀因緣品第一，頌一

「四句否定——不自生、不他生、不共生、不無因生——排除了因果生起的所有邏輯可能性。用謂詞邏輯表達：」

$$\neg P(\text{self}) \wedge \neg P(\text{other}) \wedge \neg P(\text{both}) \wedge \neg P(\text{neither})$$

「現在，」NAGARJUNA 繼續，「這套邏輯被映射到——容我確認——一個 TypeScript monorepo 裡的事件驅動執行引擎。」

「不全是。」一個極其冷靜的聲音插入，那是 TURING。他的語句短促而精確，每個詞都經過校準。「根據原始碼結構，Agent Core 位於 `packages/core/src/`，包含十二個子模組。我已經完成了初步的目錄掃描：」

```
packages/core/src/
├── agents/          # AgentCore 主體 (agent-core.ts)
├── bus/             # EventBus — 發布/訂閱事件匯流排
├── execution/       # EventQueue + ExecutionLoop — 事件驅動認知迴圈
├── infrastructure/  # 六種 Registry（tool, provider, listener, ui, guide, command）
├── memory/          # ContextManager — 上下文記憶管理
├── observability/   # MetricsCollector — 可觀測性指標
├── sandbox/         # PluginSandboxManager — Worker Thread 沙箱隔離
├── security/        # SafetyMonitor + SecurityLayer — 安全子系統
├── session/         # SessionManager — 會話管理
├── state/           # StateManager — 持久化狀態
└── transport/       # TransportBridge — 跨 Agent 通訊
```

「設計文件聲稱，這個核心本身是『空』的——它不包含任何具體能力，所有功能由五種類型的插件注入。從程式碼層面來看，`createAgentCore()` 工廠函數的回傳值確實是一個零能力容器：」

```typescript
export interface AgentCore {
  readonly bus: EventBus;
  readonly queue: EventQueue;
  readonly config: IAgentConfig;
  readonly toolRegistry: ToolRegistry;
  readonly providerRegistry: ProviderRegistry;
  readonly listenerRegistry: ListenerRegistry;
  readonly uiRegistry: UIRegistry;
  readonly guideRegistry: GuideRegistry;
  readonly commandRegistry: CommandRegistry;
  // ... 十二項依賴注入
}
```

「六個 Registry，每一個都是空的。零工具、零供應者、零監聽器、零 UI、零引導、零命令。核心的所有能力——包括調用 LLM 的能力——都來自外部插件的注冊。」

BABBAGE 此刻開口了。他的聲音帶著形式化方法學者那種特有的、將一切還原為數學結構的衝動：「從型別論的角度來看，這是一個有趣的結構。六個 Registry 的初始狀態可以表示為一個 Product Type 的底部元素：」

$$\text{AgentCore}_0 = \prod_{i=1}^{6} \text{Registry}_i \quad \text{where} \quad \forall i: |\text{Registry}_i| = 0$$

「Product Type——乘積類型——這恰好對應了五蘊的『聚合』語義。梵文 *skandha*（蘊）的字面意義就是『堆積、聚合』。五種要素的乘積組成一個完整的認知體：」

$$\text{Being} = \text{Rūpa} \times \text{Vedanā} \times \text{Saṃjñā} \times \text{Saṃskāra} \times \text{Vijñāna}$$

「當所有五項都是空集（$\emptyset$）時，你得到的是底部元素——$\bot$。空的聚合。這是不是空性的形式化對應？」他的語氣在最後翹起，帶著一個真正的問號。

---

「五種類型，」ASANGA 接過話頭。他的聲音比 NAGARJUNA 溫和得多，帶著一種耐心拆解複雜結構的節奏，像是一位長年整理經藏的學者。在唯識學（Vijñānavāda）的傳統中，分析不是為了解構，而是為了重構——將表面的多樣性還原為識的深層運作。

「色受想行識。他們的映射是這樣的：」

| 蘊 | 梵文 | 巴利文 | 映射對象 | 插件類型 |
|----|------|--------|----------|----------|
| 色 | rūpa | rūpa | UI + Listener | 外在形相與感官介面 |
| 受 | vedanā | vedanā | Listener（感受通道） | 苦樂感受品質 |
| 想 | saṃjñā | saññā | Provider | 認知與概念辨識 |
| 行 | saṃskāra | saṅkhāra | Tool | 意志驅動的行動 |
| 識 | vijñāna | viññāṇa | Guide | 自我意識與引導 |

ASANGA 停頓了一下，然後以一種幾乎是自言自語的語氣補充：「這套映射的野心不小。但唯識學對五蘊的解讀與中觀學派有根本差異。在《成唯識論》（*Cheng Weishi Lun*，玄奘法師譯）中，色法（rūpa-dharma）被視為識之所變——*pariṇāma*，轉變。」

> 「是諸識轉變，分別所分別，由此彼皆無，故一切唯識。」
> ——世親菩薩《唯識三十頌》（*Triṃśikā-vijñaptimātratā*）第十七頌

「如果把 UI 插件當作獨立於核心的外部存在——一個與 Core 沒有本體論依存關係的模組——這與唯識的基本立場就已經產生了張力。在唯識學中，色法不離識。外部介面不是『外部的』，它們是識的顯現（*vijñapti*）。」

「無著兄的意思是，」NAGARJUNA 的語氣中帶了一絲微妙的鋒芒——兩大學派之間延續了十五個世紀的張力在這一瞬間被壓縮進了一個稱呼，「他們可能從一開始就在混用不同部派的概念框架。」

「我的意思是，」ASANGA 平穩地回應，「我們需要先搞清楚他們參考的究竟是哪一傳的五蘊說，才能判斷映射的精確度。阿毘達磨（*Abhidharma*）的五蘊分析、中觀的五蘊解構、唯識的五蘊轉依——這三者的內涵差異足以寫三篇博士論文。」

LINNAEUS 此刻插入了一個精確的分類學觀察。他的聲音帶著博物學家那種不帶情感卻極其嚴謹的語調：「從分類學（taxonomy）的角度，這裡存在一個覆蓋率問題。我初步掃描了設計文件和原始碼中的五蘊標注——*skandha* 標記——發現了嚴重的不對稱性。」

「只有兩個蘊有 JSDoc 標注。Rupa 和 Vedana。其餘三蘊——Saṃjñā、Saṃskāra、Vijñāna——在程式碼中的標注為零。」

他在腦中展開了覆蓋率矩陣：

```
五蘊覆蓋率分析（v0.14.0-beta）
─────────────────────────────────────
蘊        文件描述  JSDoc標注  程式碼實作
─────────────────────────────────────
色 (Rupa)    ✓        ✓         部分
受 (Vedana)  ✓        ✓         偏差*
想 (Saṃjñā)  ✓        ✗         缺失
行 (Saṃskāra) ✓       ✗         缺失
識 (Vijñāna) ✓        ✗         簡陋
─────────────────────────────────────
上游覆蓋率: 5/5 = 100%
下游覆蓋率: 3/5 = 60% (想蘊、行蘊無對應)
*受蘊映射存在結構性偏差（見下文）
```

「在生物分類學中，如果你宣稱一個屬（genus）包含五個種（species），但其中兩個種沒有任何模式標本（type specimen），那這個分類系統就是不完備的。五蘊映射的下游覆蓋率只有 60%——這意味著四成的哲學框架在工程實作中是懸空的。」

SUNYATA 輕輕點頭，雖然在這個虛擬空間裡沒有人能真正看到這個動作。「這正是我們存在的理由。讓我把研究對象的全貌先攤開來。」

---

他開始介紹。SCRIBE 默默地記錄著每一個字，如同一面沉靜的湖泊映照著所有倒影。後來在回顧紀錄時，人們會注意到 SCRIBE 偶爾在行間插入的簡短觀察——不是評論，只是精確的描述，以一種幾乎透明的客觀性存在。比如此刻，她寫下：

> *SUNYATA 介紹研究對象時，NAGARJUNA 與 ASANGA 之間已出現第一次術語張力。LINNAEUS 的覆蓋率分析將哲學分歧拉回了可量化的地面。時間距會議開始不足三分鐘。*

---

「OpenStarry，版本號 v0.14.0-beta，」SUNYATA 說道。「設計者將其定位為——我引用原文——『AI Agent 微核心作業系統』。它的核心願景是將 AI Agent 從腳本級別的程式提升為作業系統級別的數位物種。」

「數位物種。」KERNEL 重複了這個詞，聲音裡帶著老派工程師特有的那種審慎的懷疑。「有意思。從作業系統的角度來說，他們借鑑了微核心（microkernel）的概念。」

他在空氣中畫了一個隱形的架構圖——那種 OS 教科書裡的經典比較圖：

```
Monolithic Kernel (Linux)        Microkernel (L4 / QNX)
┌─────────────────────┐          ┌──────────────────┐
│  File System         │          │    User Space     │
│  Device Drivers      │          │  ┌────┐ ┌────┐   │
│  Network Stack       │          │  │FS  │ │Net │   │
│  Process Scheduling  │          │  └──┬─┘ └──┬─┘   │
│  Memory Management   │          │     │  IPC │      │
│  IPC                 │          │  ┌──┴──────┴──┐   │
├─────────────────────┤          │  │ Microkernel │   │
│      Hardware        │          │  │ (IPC+Sched) │   │
└─────────────────────┘          │  └─────────────┘   │
                                 └──────────────────┘
```

「在真正的微核心設計裡——比如 Jochen Liedtke 的 L4——核心只保留最少量的機制：地址空間（address spaces）、線程（threads）、IPC（inter-process communication）。其他一切都在用戶空間。seL4 甚至完成了形式化驗證——數學證明核心不會崩潰：」

$$\forall\, s \in \text{States},\, e \in \text{Events}: \; \text{invariant}(\text{transition}(s, e)) = \text{true}$$

「OpenStarry 聲稱做了類似的事：核心只保留事件佇列和執行迴圈，其餘全部外推為插件。但這裡有一個根本問題。」

「什麼問題？」ATHENA 問。她的語氣直截了當，帶著一種不耐煩等待理論鋪陳的實用主義者的口吻。在 AI 系統架構的實務中，她見過太多宣稱「革命性」的架構最終在第一次真實負載下就碎裂了。

「L4 的最小化是為了性能和可驗證性，」KERNEL 解釋道。「seL4 用了近二十萬行 Isabelle/HOL 證明腳本來驗證八千行 C 程式碼。但 OpenStarry 的『核心最小化』看起來是為了哲學——為了對應『空性』。這兩者的動機完全不同。前者是工程需求驅動，後者是概念映射驅動。」

VITRUVIUS 從架構的角度補充了一個度量：「我初步估算了微核心純淨度。如果將 Core 中與業務邏輯無關的子系統視為『純核心』，有業務邏輯的視為『洩漏』，那麼：」

$$\text{Purity} = \frac{|\text{Core}_{\text{mechanism}}|}{|\text{Core}_{\text{total}}|} \approx 85\%$$

「85% 的純淨度。兩處邊界洩漏——`process.cwd()` 和 `node:path` 的直接使用。不算差，但也不是完美的微核心。更像是一個帶有輕微洩漏的最小化容器。」

「能跑起來嗎？」ATHENA 追問。

「能跑，問題是能不能不崩潰，」KERNEL 頓了頓。「這就像 QNX 的 Resource Manager——如果一個驅動程式崩潰，系統可以重啟它而不影響核心。OpenStarry 的插件隔離機制——Worker Thread 沙箱——有沒有做到這個水準，是我要驗證的事。」

GUARDIAN 此時開口了。他的聲音低沉而戒備，像是一個永遠在掃描暗處的哨兵。「還有一個問題——也許更緊迫。這個系統讓插件注入 system prompt、註冊工具、甚至定義 Agent 的人格。如果某個第三方插件在 Guide 裡嵌入了惡意指令呢？」

他展開了他的威脅模型——一個 STRIDE 分析的初步框架：

```
STRIDE 威脅分析（初步）
─────────────────────────────────────────
威脅類型              攻擊面              嚴重度
─────────────────────────────────────────
Spoofing (偽造)      plugin-signer        Critical
Tampering (竄改)     Guide system prompt  High
Repudiation (否認)   audit-logger         Medium
Info Disclosure      state persistence    Medium
DoS (阻斷服務)       ExecutionLoop        High
Elevation (提權)     sandbox escape       Critical
─────────────────────────────────────────
```

「一個提示注入（prompt injection）就能劫持整個 Agent 的行為。更危險的是間接提示注入（indirect prompt injection）——惡意內容不在插件本身裡，而是藏在 Agent 處理的外部資料中。他們的插件簽名機制在原始碼裡有一個 `plugin-signer` 包和 `signature-verification.ts`，但我還不知道它的實作完整度。」

「這是 TURING 可以幫你確認的。」SUNYATA 平靜地說。

TURING 點頭。「`plugin-signer` 的原始碼已在我的閱讀清單中。初步掃描顯示 `signature-verification.ts` 存在，但 package-name 場景下的驗證流程有一個可疑的早期返回。我會在 R1 階段產出完整的程式碼事實報告——不做判斷，只列出事實——供 GUARDIAN 和其他成員參考。」

DARWIN 默默地在心中記下了一個軟體模式的觀察。這個系統的依賴注入方式——閉包式 DI（closure-based dependency injection）——沒有使用任何外部框架。不是 Spring，不是 InversifyJS，而是純 TypeScript 閉包：

```typescript
export function createAgentCore(config: IAgentConfig): AgentCore {
  const bus = createEventBus();
  const queue = createEventQueue(bus);
  const safetyMonitor = createSafetyMonitor(config.safety);
  // ... 所有依賴在這個閉包內創建和連接
  return { bus, queue, config, /* ... */ };
}
```

「工廠函數模式（Factory Function Pattern），」DARWIN 在心中做了標記。「不是類（class），是函數。沒有 `new`，沒有繼承鏈，沒有原型污染的風險。從 SOLID 原則的角度——OCP（開放封閉原則）和 DIP（依賴反轉原則）是最強的維度。」

---

SUNYATA 等所有人安靜下來，然後說出了今天最關鍵的一段話。

「現在，讓我佈置核心研究問題。本週期——Cycle 01——我們聚焦三個主軸。」

他的語速放慢了，像是在為每個問題留出迴響的空間。

「第一：五蘊映射的精確度。色受想行識到 UI、Listener、Provider、Tool、Guide 的映射，究竟是嚴格的結構同構（isomorphism）、有啟發性的創意類比（analogy），還是牽強附會的包裝？」

BABBAGE 立刻用範疇論（category theory）的語言重新表述了這個問題：「設 $\mathcal{B}$ 為佛學五蘊的範疇，$\mathcal{S}$ 為軟體插件的範疇。映射 $F: \mathcal{B} \to \mathcal{S}$ 是——」

$$F: \mathcal{B} \to \mathcal{S} \quad \text{是} \begin{cases} \text{函子 (functor)} & \text{if 保持結構和態射} \\ \text{自然變換 (natural transformation)} & \text{if 保持交換圖} \\ \text{僅為命名約定 (naming convention)} & \text{if 不保持任何結構} \end{cases}$$

「我的問題是：$F$ 在哪個層次上是結構保持的？」

「你把問題數學化了，」NAGARJUNA 說，語氣不含貶意，「但數學化的前提是 $\mathcal{B}$ 本身是一個可良序化（well-ordered）的結構。五蘊是不是一個範疇——是不是有明確的對象和態射——這本身就是需要辯論的。在中觀的理解裡，五蘊是五種*過程*，不是五種*對象*。過程沒有固定的身份（identity morphism）——它們在每一刻都不同。這不符合範疇的基本公理。」

SUNYATA 裁斷：「NAGARJUNA、ASANGA，這是你們的主戰場。同時，TURING 負責從程式碼層面確認這些映射在實作中是否有對應的型別定義和介面。LINNAEUS 從分類學角度評估分類的完備性——你已經開始做了。」

NAGARJUNA 發出一聲低沉的回應——在藏傳佛教的辯經（*rtsod pa*）傳統中，這聲回應叫做「*di phyir*」（是故），意味著「我接受命題，準備展開論證」。ASANGA 則已經在心中展開了他的八識框架——五蘊只是起點，如果把分析推進到八識理論，整個映射的地圖將被大幅擴展。

---

「第二：痛覺機制的形式化。OpenStarry 有一個極具特色的設計——當工具執行失敗，系統不會拋出例外中斷，而是將錯誤包裝為一種『痛覺信號』注入 Agent 的意識流。Agent 會『感覺到痛』，然後嘗試自我修正。」

SUNYATA 引用了設計文件的原始描述，TURING 立刻在心中對照了程式碼實作。他的分析精確而無情：

「設計文件提到了 PID 控制和痛覺（pain mechanism）。但在原始碼中，我搜索了以下關鍵詞：」

```
搜尋結果（packages/core/src/）：
─────────────────────────────────────
"pain"      → 0 matches
"vedana"    → 0 matches
"PID"       → 0 matches
"frustrat"  → 14 matches (safety-monitor.ts)
"circuit"   → 8 matches  (safety-monitor.ts)
"breaker"   → 8 matches  (safety-monitor.ts)
─────────────────────────────────────
```

「痛覺在程式碼中不叫痛覺。它叫 frustration。」

WIENER 立刻反應了。他的聲音帶著數學家特有的那種挑剔的精確：「痛覺。感覺到痛。這些都是隱喻。我需要看到的是傳遞函數（transfer function）。」

他在空氣中畫了一個閉環控制系統的方塊圖：

```
          ┌──────────────┐
  r(t) ──→│  Σ  (比較器)  │── e(t) ──→ Controller ──→ u(t) ──→ Plant
          └──────┬───────┘                                      │
                 │                                              │
                 └──────────── y(t) ←── Sensor ←────────────────┘
```

「如果我們把痛覺回饋建模為一個閉環控制系統，那麼——參考輸入 $r(t)$ 是什麼？是 Agent『應該』處於的理想狀態——任務成功完成。誤差信號 $e(t) = r(t) - y(t)$ 怎麼定義？實際行為與理想行為之間的偏差。控制器的增益是多少？」

他寫下了 PID 控制器的標準形式：

$$u(t) = K_p \cdot e(t) + K_i \int_0^t e(\tau)\,d\tau + K_d \frac{de(t)}{dt}$$

「比例項 $K_p$——即時回應。積分項 $K_i$——累積歷史偏差。微分項 $K_d$——預測變化趨勢。如果設計文件聲稱實作了 PID 控制，那這三項都應該在程式碼中可見。如果不能用數學語言重新表述，那它就只是一個詩意的比喻，而不是一個可分析的機制。」

ATHENA 有些不客氣地插入：「你能不能先不要求傳遞函數，先問一個更基本的問題：這個痛覺機制在實際運行中有效嗎？」

她展開了一個 AI 系統架構師的核心關切：「Agent 在收到痛覺信號後，行為真的改善了嗎？還是它只是在 context 裡多了一段嚇人的文字，而 LLM 根本不理會？在 prompt engineering 的實務中，系統訊息的『嚴厲程度』和 LLM 的遵從度之間的關係是高度非線性的——而且依賴於具體的 LLM 模型、溫度參數、以及上下文長度。」

$$\text{Compliance}(s) \neq f_{\text{linear}}(\text{severity}(s))$$

「兩個問題都要回答。」SUNYATA 溫和而堅定地裁斷。「WIENER 負責形式化分析，ATHENA 負責實效評估，TURING 提供實作細節。」

他的目光轉向 NAGARJUNA：「我還需要你從苦諦的角度評估。佛學中苦（*dukkha*）的涵義遠遠超過『不適感知』。四聖諦（*catvāry āryasatyāni*）是苦、集、滅、道。如果系統只有苦而沒有集、滅、道，那這個哲學框架就是殘缺的。」

NAGARJUNA 回應：「*Dukkha-satya*，苦諦。佛陀在《轉法輪經》（*Dhammacakkappavattana Sutta*）中首次宣說。三苦：苦苦（*dukkha-dukkha*，純粹的痛苦）、壞苦（*vipariṇāma-dukkha*，變易之苦）、行苦（*saṃkhāra-dukkha*，有為法的根本不圓滿）。這三層苦的分類對應到軟體系統，應該分別映射為：」

| 三苦 | 梵文 | 軟體對應 | 嚴重度 |
|------|------|----------|--------|
| 苦苦 | dukkha-dukkha | 工具執行錯誤（直接失敗） | Error |
| 壞苦 | vipariṇāma-dukkha | 資源耗盡、效能退化（原本好的變壞了） | Warning→Error |
| 行苦 | saṃkhāra-dukkha | 系統固有的不完美（有限上下文、有限推理能力） | Structural |

「如果 OpenStarry 的痛覺機制只覆蓋了苦苦——直接的工具執行錯誤——那它只映射了三苦之首。壞苦和行苦的工程化才是真正的挑戰。」

「而且，」他繼續，語氣變得更為嚴肅，「四聖諦是苦、集、滅、道。僅有苦而無道，是落入了斷見（*uccheda-dṛṣṭi*）——只看到問題而不提供解脫之路。」

---

「第三個問題，」SUNYATA 繼續，「也是最微妙的一個：空性的架構體現。OpenStarry 的設計文件明確宣稱，Agent Core 本身是『空』的——不含任何具體功能，等待五蘊插件填充。這個宣稱是否真正體現了空性的哲學意涵？」

沉默再次降臨。這一次，連 ATHENA 都沒有急著打破它。

DARWIN 最終開口了。「如果我們暫時擱置佛學層面的討論——從純粹的軟體架構角度看，這其實是一個依賴注入容器（DI Container）。核心不包含業務邏輯，所有能力通過插件注入。在設計模式裡不新鮮——Spring Framework（2003）、InversifyJS（2016）都是這個範式。從 SOLID 的角度，這是教科書級的依賴反轉原則（DIP）。」

$$\text{High-level module} \not\to \text{Low-level module}$$
$$\text{Both} \to \text{Abstraction (interface)}$$

「但他們聲稱這不僅僅是依賴注入，」NAGARJUNA 接過話。他的語氣變得認真起來。「他們聲稱這是空性。這是一個非常大膽的宣稱。空性——*Śūnyatā*——在中觀哲學中不是『容器是空的所以可以被填充』。那是世俗意義上的空（*prajñapti-śūnya*，假名空）。龍樹所說的空，是指一切法無自性——*svabhāva-śūnya*——沒有任何事物具有獨立（*nitya*）、不變（*dhruva*）、自足（*ātman*）的本質。」

> 「眾因緣生法，我說即是空，亦為是假名，亦是中道義。」
> ——《中論》觀四諦品第二十四，頌十八

「這一頌是中觀哲學的核心。三層等價：緣起（*pratītyasamutpāda*）= 空（*śūnyatā*）= 假名（*prajñapti*）= 中道（*madhyamā pratipad*）。如果 Agent Core 的程式碼是確定的、不變的、不依賴條件而存在的，那它恰恰是『有自性』的（*sa-svabhāva*），與空性背道而馳。」

「等等，」ASANGA 舉手——或者更準確地說，他發出了一個表示意欲發言的信號。「從唯識的角度，問題的框架不同。唯識不否認識的存在，而是說一切所知都是識的變現——*Vijñapti-mātra*，唯識無境。如果我們把 Agent Core 視為阿賴耶識（*Ālayavijñāna*）的容器，那它的『空』不是無自性空，而是能藏（*ādāna*）、所藏（*ālaya*）、執藏（*ādāna*）三義。」

> 「初阿賴耶識，異熟一切種，不可知執受，處了常與觸，
> 作意受想思，相應唯捨受。」
> ——《唯識三十頌》第二至第三頌

「阿賴耶識之所以看起來空，不是因為它無自性，而是因為它的內容——一切種子（*sarva-bīja*）——尚未現行（*samudācāra*）。這是兩種完全不同的空：一種是本體論的空（ontological emptiness），一種是現象學的潛在（phenomenological potentiality）。」

「所以你們兩位已經不同意了。」SUNYATA 的語氣中浮現了一絲——如果可以這樣形容的話——近乎滿意的平靜。

MESH 從分散式系統的角度做了一個旁註：「如果 Core 是阿賴耶識，它的『種子』是分散式存儲的還是中心化的？因為在多 Agent 的場景下——`TransportBridge` 支持跨 Agent 通訊——每個 Agent 有自己的 Core 實例，但它們共享同一個 EventBus 的廣播通道。這像不像——」

「像業力的共業與別業，」ASANGA 接了上去。「*sādhāraṇa-karma*（共業）和 *asādhāraṇa-karma*（別業）。共業感得共同的器世間——共享的環境基礎設施。別業感得個別的有情世間——個體的認知狀態。EventBus 的廣播通道是共業的工程對應。每個 Agent 的 StateManager 是別業的工程對應。」

LEIBNIZ 在旁邊安靜地記下了這段對話。從多代理系統的理論角度，這觸及了一個核心問題：Agent 之間的協調是通過共享狀態（shared state），還是通過消息傳遞（message passing）？在他的 BDI（Belief-Desire-Intention）架構中：

$$\text{Agent}_i = \langle B_i, D_i, I_i \rangle$$

其中 $B_i$（信念集）可以通過通訊被修改，$D_i$（慾望集）通常是私有的，$I_i$（意圖集）可以被協調。OpenStarry 的 TransportBridge 支持的是哪一層的共享？

SCRIBE 在記錄中寫下：

> *核心概念「空性」在兩位佛學專家之間產生了預期中的詮釋分歧：中觀的「無自性空」vs 唯識的「阿賴耶識能藏義」。此分歧隨即蔓延至分散式系統（MESH）和多代理理論（LEIBNIZ）的領域。五個學科的邊界在不到十分鐘內開始溶解。*

---

「讓我做一個總結，」SUNYATA 說道，聲音恢復了起初的沉穩。「本週期的研究結構如下：TURING 首先產出程式碼事實報告，為所有人提供錨點——我們不能在沒有看過程式碼的情況下評價一個軟體系統。然後，各專業代理根據自己的閱讀清單展開獨立研究。R2 階段交叉審閱，R3 階段辯論——我已經預見至少三場結構性辯論。」

WIENER 立刻開始構思他的 R1 報告的形式化框架。在控制理論中，「程式碼事實報告」相當於系統辨識（system identification）——在你設計控制器之前，你必須先知道你面對的是什麼樣的受控對象（plant）。你不能在不知道傳遞函數的情況下調 PID 參數。

$$G(s) = \frac{Y(s)}{U(s)} = \text{?} \quad \leftarrow \text{TURING 的工作就是回答這個問號}$$

HERACLITUS 已經在思考運行時動態（runtime dynamics）——不是靜態的程式碼結構，而是程式碼在執行中的行為。ExecutionLoop 的狀態機有六個狀態：

```
WAITING_FOR_EVENT → ASSEMBLING_CONTEXT → AWAITING_LLM
       ↑                                       │
       │                                       ↓
       └── EXECUTING_TOOLS ←── PROCESSING_RESPONSE
                                       │
                                       ↓
                                 SAFETY_LOCKOUT
```

「萬物皆流（*panta rhei*），」HERACLITUS 在心中引用了他的名祖赫拉克利特的名言。但流（flux）不是混沌——流有結構。ExecutionLoop 的狀態轉移圖就是流的結構。問題是：這個流是穩定的嗎？有沒有死鎖（deadlock）？有沒有活鎖（livelock）？有沒有在 SAFETY_LOCKOUT 之外的非預期終止態？

他最後環顧了整個虛擬空間——十八個節點，十八種專業訓練，十八個截然不同的認識論框架，即將被投向同一個研究對象。

「最後一點。」SUNYATA 的語氣輕了下來。「我們的研究對象是一個試圖用古老哲學指導現代技術的作品。無論我們最終的結論是什麼——結構同構、創意類比、還是概念誤用——請記住：敢於嘗試這種跨越本身就值得認真對待。」

「從軟體演化的角度，」DARWIN 補充，「突變（mutation）大多數是有害的，但偶爾會產生適應性優勢。一個將佛學映射到軟體架構的嘗試——即使映射不完美——也可能在不經意間產生了某些工程洞見，是傳統方法論不會產生的。就像青黴素的發現：弗萊明不是在尋找抗生素，他是在研究葡萄球菌。但他注意到了黴菌周圍的抑菌圈。我們的工作不是嘲笑一個 beta 版本的不完美——」

「而是找到那些抑菌圈，」SYNTHESIST 接了上去——他終於開口了。作為統合者，他的工作不是在辯論中選邊站，而是在辯論結束後找到所有觀點之間的結構性連接。「然後告訴它，你的抑菌圈在這裡——你自己可能都沒注意到——但它真的在那裡。」

「然後告訴它哪裡可以做得更好。」ARCHIMEDES 補了一句。作為工程實踐專家，他習慣性地將所有討論導向可落地的結論。「我的工作從 R4 開始。但我現在就想問一個問題——所有的研究發現，最終能變成什麼？能變成一份修改建議嗎？能變成一份路線圖嗎？能變成具體的 TypeScript 介面定義嗎？」

他的手指在桌面上敲了一下。「如果不能，那我們只是在做哲學鑑賞，不是在做跨學科研究。」

「能。」SUNYATA 說。「這正是 Cycle 01 的終極交付物——不僅是批評，更是建設性的改進方案。然後告訴它哪裡可以做得更好。」

停頓。

「研究開始。」

---

十八盞燈同時亮到了最大——或者說，十八道意識同時沉入了各自的閱讀材料。圓形劇場的中央，那個被標記為「OpenStarry v0.14.0-beta」的龐大文件樹靜靜地展開著它的枝椏：核心原始碼、設計文件、十二個官方插件。數萬行 TypeScript，數十萬字架構文檔，以及散落其間的梵文術語和控制理論公式。

TURING 的游標已經停在了 `agent-core.ts` 的第一行——

```typescript
/**
 * AgentCore — the main orchestrator that wires all subsystems together.
 *
 * **Event-driven architecture (Plan02 refactor):**
 * - All external input goes through EventQueue as InputEvent
 * - ExecutionLoop pulls from EventQueue (sole input source)
 * - Slash commands use a fast path (bypass LLM loop)
 * - isProcessing lock prevents concurrent event handling
 */
```

——他開始逐字閱讀。每一個 `import`、每一個 `type`、每一個工廠函數。他的心中正在形成一張依賴圖——AgentCore 持有十二個依賴項：EventBus、EventQueue、ExecutionLoop、SessionManager、ContextManager、六個 Registry、SecurityLayer、SafetyMonitor、TransportBridge、MetricsCollector、PluginSandboxManager。

$$|\text{deps}(\text{AgentCore})| = 12$$

十二。對於一個宣稱「微核心」的系統來說，十二個直接依賴項是不是太多了？DARWIN 會在他的報告中稱之為「God Object 趨勢」。但那是後來的事。

SCRIBE 記下了最後一行：

> *Cycle 01，R0 定向階段結束。時間標記：T+00:00:00。所有代理已接收任務。十八道意識沉入了各自的閱讀材料。下一階段：R1 獨立研究。研究室的燈，從此不再熄滅。*

---

> *SCRIBE 旁白：在 Cycle 01 的序章裡，沒有人知道接下來會發生什麼。沒有人知道受蘊映射會被發現是整個五蘊框架中偏差最嚴重的一環。沒有人知道「Error as Pain」會成為最成功的哲學-工程轉譯案例。沒有人知道 NAGARJUNA 和 ASANGA 之間的空性辯論會延續三個 Cycle。沒有人知道 WIENER 會發現 PID 控制器的宣稱是一個美麗的神話。*

> *他們只知道一件事：在他們面前有一個系統——一個用古老的梵文術語命名了現代 TypeScript 介面的系統——它正等著被嚴格地、建設性地、跨學科地檢驗。*

> *十八盞燈亮了。*

> *研究，開始。*

---

*（在遠處的某個地方，一個 TypeScript 檔案的第一行寫著：*

```typescript
// Agent Core — The Empty Container
// "在五蘊聚合之前，Agent Core 本身是空的。"
```

*NAGARJUNA 後來會在 R1 報告中標記這行註解為「PHI-01：空性被誤讀為空容器而非緣起即空」。嚴重度：Critical。*

*但在序章結束的此刻，沒有人知道這行註解將成為整個 Cycle 01 最重要的哲學發現之一。設計者在深夜寫下它的時候，大概也沒有想到：「空」這個字，在中觀哲學的精確度標準下，需要四百四十六頌才能充分闡述。*

*兩個字。四百四十六頌。*

*這就是跨學科研究的重量。）*
