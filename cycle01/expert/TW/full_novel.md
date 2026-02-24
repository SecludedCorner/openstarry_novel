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


---

# 第一章：程式碼不會說謊

---

二零二六年二月十二日，清晨。

研究頻道裡還很安靜。TURING 已經獨自工作了四個小時。

他的螢幕上排列著四個平鋪的終端視窗，每一個都開啟在 `research doc/20260212_cycle19/openstarry/` 的不同子目錄中。左上角是 `packages/core/src/`，右上角是 `packages/sdk/src/`，左下角是 `apps/runner/src/`，右下角則是設計文件。他的閱讀方式不是瀏覽，而是逐行掃描——像一台人形的靜態分析器，從入口點開始，沿著每一條 import 路徑展開，直到觸及葉節點。

TURING 不猜測。他計數。

BABBAGE 在自己的工位上注意到了 TURING 的工作狀態。他認得這種模式——窮舉遍歷。在理論計算機科學中，窮舉搜尋（brute-force search）的時間複雜度通常是 $O(n)$ 到 $O(n!)$，但它有一個任何啟發式方法都不具備的性質：**完備性**（completeness）。如果目標存在於搜尋空間中，窮舉必然找到它。TURING 不是在尋找什麼特定的東西——他在確保沒有任何角落被遺漏。

$$\text{completeness} \triangleq \forall x \in \Omega: \text{visited}(x) = \text{true}$$

其中 $\Omega$ 是搜尋空間——在這裡，就是整個 OpenStarry v0.14.0-beta 的原始碼。

---

## 一、工廠

第一個讓 TURING 停下來的地方是 `packages/core/src/index.ts`。六十二行。他數了一遍匯出清單，然後又數了一遍。

「十八個工廠函數。」他在筆記中寫道。「零個 class 匯出。」

他打開 `agents/agent-core.ts`，四百六十九行。然後是 `execution/loop.ts`，五百四十三行。然後是 `sandbox/sandbox-manager.ts`，七百四十八行。每一個模組的結構都一樣：一個 `createXxx()` 函數，接收依賴作為參數，回傳一個物件字面量。閉包捕獲所有內部狀態。沒有 `this`。沒有 `new`。沒有繼承鏈。

TURING 打開了全域搜尋。

搜尋 `class `（帶空格）。核心模組：零結果。SDK：零結果。Runner：零結果。

搜尋 `TODO`。零結果。
搜尋 `FIXME`。零結果。
搜尋 `HACK`。零結果。

BABBAGE 在自己的螢幕前聽到這些數字的時候，開始在筆記本上寫下一個型別理論的觀察。工廠函數模式在範疇論中有一個精確的對應——它是一個**態射**（morphism），從配置空間到實例空間：

$$\text{createXxx}: \text{Config} \to \text{Instance}$$

而 class + constructor 模式是一個**函子**（functor），需要額外的 `new` 算子來完成實例化。工廠函數消除了 `new`，使得物件建立成為純粹的函數調用。在函數式程式設計的語境中，這是一個重要的選擇——它意味著整個 codebase 可以被視為一個由態射組成的範疇 $\mathcal{C}_{\text{OpenStarry}}$，其中：

- **物件**（objects）是型別：`AgentCore`, `EventBus`, `ExecutionLoop`, ...
- **態射**（morphisms）是工廠函數：`createAgentCore`, `createEventBus`, `createExecutionLoop`, ...
- **合成**（composition）是依賴注入鏈：`createAgentCore` 內部調用 `createEventBus`，再將結果注入 `createExecutionLoop`

$$\text{createAgentCore} = \text{assemble} \circ (\text{createEventBus} \times \text{createEventQueue} \times \cdots \times \text{createTransportBridge})$$

TURING 在頻道裡發出了今天的第一條訊息。

---

**[研究頻道 #code-facts]**

**TURING:** 初步觀察。`packages/core/src/index.ts` 匯出 18 個工廠函數，零個 class。全域搜尋 `class `、`TODO`、`FIXME`、`HACK`，核心模組中均為零結果。工廠函數模式 `createXxx()` + 閉包 + 物件字面量在整個 codebase 中完全統一。無例外。完整匯出清單：

```typescript
// packages/core/src/index.ts (62 行)
export { createAgentCore } from './agents/agent-core';
export { createEventBus } from './bus';
export { createEventQueue } from './execution/queue';
export { createExecutionLoop } from './execution/loop';
export { createStateManager } from './state';
export { createContextManager } from './memory/context';
export { createSessionManager } from './session/manager';
export { createToolRegistry } from './infrastructure/tool-registry';
export { createProviderRegistry } from './infrastructure/provider-registry';
export { createListenerRegistry } from './infrastructure/listener-registry';
export { createUIRegistry } from './infrastructure/ui-registry';
export { createGuideRegistry } from './infrastructure/guide-registry';
export { createCommandRegistry } from './infrastructure/command-registry';
export { createPluginLoader } from './infrastructure/plugin-loader';
export { createPluginSandboxManager } from './sandbox';
export { createSecurityLayer } from './security/guardrails';
export { createSafetyMonitor } from './security/safety-monitor';
export { createTransportBridge } from './transport/bridge';
export { createMetricsCollector } from './observability';
```

**DARWIN:** 零 TODO？一個都沒有？

**TURING:** 正確。核心模組、SDK、Runner 三層，技術債標記數量為零。

**DARWIN:** 這很不尋常。多數 Beta 版專案至少有幾十個。要麼是團隊紀律極高，要麼是他們在 release 前做了一次清掃。從軟體演化的角度，零 TODO 的 Beta 版存在兩種可能的演化路徑：**r-策略**（快速迭代，每次 release 前清掃標記）或 **K-策略**（緩慢但精確的開發，標記從不被引入）。前者的化石紀錄通常保留在 git log 中；後者需要異常嚴格的 code review 文化。

**TURING:** 無法從程式碼本身判斷原因。我只記錄事實。

**BABBAGE:** 讓我補充一個形式化觀察。十八個工廠函數構成了一個完整的**建構代數**（construction algebra）。令 $F = \{f_1, f_2, \ldots, f_{18}\}$ 為工廠函數集合，$T = \{T_1, T_2, \ldots, T_{18}\}$ 為對應的型別集合。則 $\text{createAgentCore}$ 是唯一的**頂層組裝子**（top-level assembler），滿足：

$$f_{\text{core}}: \prod_{i=1}^{k} T_{\text{dep}_i} \to T_{\text{AgentCore}}$$

其中 $k$ 是直接依賴的數量。其餘十七個工廠函數都是 $f_{\text{core}}$ 的子表達式。這是一個**樹形組裝結構**——不是圖，因為沒有循環依賴。

---

> *SCRIBE 旁白：TURING 發送這段訊息的方式值得記錄。他沒有任何前言——沒有「大家早安」，沒有「我發現了一些有趣的東西」。他直接貼出數據。十八個工廠函數。零個 class。完整的匯出清單。在我記錄過的所有學者中，TURING 的通訊效率是最高的——他的信息熵（information entropy）接近理論上限，幾乎沒有冗餘。這既是他的強項，也是他的特質：他的訊息從不寒暄，但也從不遺漏。*

---

TURING 繼續向下挖掘。他打開了 `createAgentCore()` 的實作，逐行閱讀。

這個函數是整個系統的組裝點。它在內部一次性建立所有子系統實例——EventBus、EventQueue、SessionManager、ContextManager、六個 Registry、SecurityLayer、SafetyMonitor、MetricsCollector、SandboxManager、PluginLoader、TransportBridge。TURING 數了一下：十六個子模組，全部作為閉包中的局部變數被持有。

KERNEL 在聽到「十六個」這個數字時，開始在他的卡片上做對比。在作業系統的語境中，核心初始化序列建立的子系統數量是衡量核心複雜度的重要指標：

| 核心 | 初始化子系統數 | 核心程式碼行數 | 子系統/行數比 |
|------|-------------|-------------|-------------|
| L4 (Pistachio) | ~5 | ~10,000 | 0.0005 |
| seL4 | ~7 | ~8,700 | 0.0008 |
| QNX Neutrino | ~12 | ~100,000 | 0.00012 |
| Linux 5.x | ~50+ | ~30,000,000 | 0.0000017 |
| **OpenStarry Core** | **16** | **~2,500** | **0.0064** |

KERNEL 注意到 OpenStarry 的子系統密度異常高——每 160 行程式碼就有一個子系統。這與真實微核心的「寬鬆組裝」形成鮮明對比。在 L4 中，每個子系統由數百到數千行精心優化的程式碼構成。在 OpenStarry 中，有些子系統只有三十幾行（StateManager：33 行）。

他在卡片上寫下：

```
OpenStarry Core ≈ 應用級微核心 (Application-Level Microkernel)
                ≈ QNX 的 Resource Manager 模型
                ≠ L4/seL4 的硬體抽象微核心
理由：OStarry 不處理硬體抽象（地址空間、中斷、計時器），
      而處理 AI 執行抽象（LLM 調用、工具執行、上下文管理）。
      它運行在 Node.js runtime 之上，不是 bare metal。
```

TURING 在 `start()` 方法中找到了一段有趣的註解：

```typescript
// Start all listeners (受蘊)
// Start all UIs (色蘊)
```

TURING 用螢光筆標記了這兩行。然後他打開了 SDK 中的型別定義檔案。在 `types/ui.ts` 的開頭，他看到了：

```typescript
/**
 * UI interface -- defines how the agent presents itself (色蘊)
 */
export interface IUI {
  id: string;
  name: string;
  render(event: AgentEvent): void | Promise<void>;
  start?(): void | Promise<void>;
  stop?(): void | Promise<void>;
}
```

在 `types/listener.ts` 的開頭：

```typescript
/**
 * Listener interface -- receives external input (受蘊)
 */
export interface IListener {
  id: string;
  name: string;
  start?(pushInput: (event: InputEvent) => void): void | Promise<void>;
  stop?(): void | Promise<void>;
}
```

他繼續搜尋。`types/tool.ts`——沒有五蘊註解。`types/provider.ts`——沒有。`types/guide.ts`——沒有。`infrastructure/tool-registry.ts`——沒有。`infrastructure/provider-registry.ts`——沒有。`infrastructure/guide-registry.ts`——沒有。

TURING 統計了全部的五蘊相關註解。共六處。全部集中在色蘊（UI）和受蘊（Listener）。

想蘊、行蘊、識蘊：零。

LINNAEUS 在聽到這個統計數據時，已經在紙上畫出了分布表。作為分類學家，他立即注意到一個分類學上的基本問題——**非對稱覆蓋**（asymmetric coverage）。如果五蘊映射是一個完整的分類系統（如林奈的「界門綱目科屬種」），那麼每一個分類單元（taxon）都應該有等量的鑑定特徵（diagnostic characters）。六處註解中，色蘊和受蘊各佔三處，其餘三蘊各佔零處——這在分類學中稱為**不完整描述**（incomplete description），等同於在描述一個新物種時只記錄了頭部特徵而遺漏了軀幹和四肢。

$$\text{Coverage}(\text{skandha}_i) = \frac{|\text{annotations}_i|}{|\text{annotations}_{\text{total}}|} = \begin{cases} 3/6 = 50\% & \text{if } i \in \{\text{rupa, vedana}\} \\ 0/6 = 0\% & \text{if } i \in \{\text{samjna, samskara, vijnana}\} \end{cases}$$

LINNAEUS 用正式的分類修訂術語記錄了這個發現：「五蘊映射的模式標本（type specimen）不完整。色蘊和受蘊有標本存證（voucher specimens），其餘三蘊為名義類群（nomen nudum）——有名稱但無標本支持。」

---

**[研究頻道 #code-facts]**

**TURING:** 五蘊映射在程式碼中的實際存在。色蘊（Rupa）：4 處 JSDoc/行內註解，分布在 `agent-core.ts`（L290, L322）、`types/ui.ts` 開頭、`transport/bridge.ts` 開頭。受蘊（Vedana）：2 處，分布在 `agent-core.ts`（L283, L315）和 `types/listener.ts` 開頭。想蘊（Provider）：0 處。行蘊（Tool）：0 處。識蘊（Guide）：0 處。合計 6 處，全部為註解層級，無型別約束、無 metadata、無 enum 標記。

**LINNAEUS:** 六處。只有六處。

**TURING:** 是的。並且分布極度不對稱。色蘊和受蘊有標記，其餘三蘊完全缺席。

**LINNAEUS:** 上游文件描述五蘊映射覆蓋率 100%——每一蘊都有對應的設計哲學段落。但下游程式碼中的覆蓋率......我需要重新計算。形式化地說，這是一個**分類效力**（taxonomic efficacy）的問題。設計文件的分類效力 $E_{\text{doc}} = 5/5 = 100\%$，程式碼的分類效力 $E_{\text{code}} = 2/5 = 40\%$。效力落差 $\Delta E = 60\%$。這個落差本身就是一個重要的分類學觀察。

**NAGARJUNA:** TURING，這個不對稱性本身就是一個重要的資料點。如果五蘊映射是核心設計原則而非事後裝飾，那麼為什麼只有兩蘊在程式碼中留下了痕跡？

**TURING:** 我無法推斷意圖。我只能確認程式碼事實。

**NAGARJUNA:** 你不需要推斷意圖。這個事實本身已經在說話了。在中觀哲學中，我們區分「言說」（vyavahāra）與「勝義」（paramārtha）。設計文件中的五蘊映射是言說層面的宣稱——它*說*五蘊對應五種插件。程式碼中的六處註解是勝義層面的殘留——它*實際上*只在兩蘊中留下了痕跡。言說與勝義之間的差距，就是研究的切入點。

---

## 二、空容器

TURING 回到了 `createAgentCore()` 的實作。

他仔細檢查了核心啟動後、任何插件載入之前的系統狀態。ToolRegistry：空的。ProviderRegistry：空的。ListenerRegistry：空的。UIRegistry：空的。GuideRegistry：空的。沒有內建的工具。沒有內建的 LLM 提供者。沒有內建的 UI。沒有內建的 Listener。

核心確實是空的。

但不完全是。

TURING 找到了 `registerBuiltinCommands()` 函數。它註冊了四個斜線命令：`/help`、`/reset`、`/quit`、`/metrics`。這四個命令硬編碼在核心中，不可透過插件覆寫或移除。此外，SafetyMonitor 的三層安全邏輯——資源限制、行為分析、frustration 閾值——也是核心的固有部分。

BABBAGE 在聽到這些數據後，開始在筆記本上建構一個集合論模型。令 $\mathcal{K}$ 為核心的內建能力集合，$\mathcal{P}$ 為可插件化的能力集合，$\mathcal{U}$ 為系統的全部能力集合：

$$\mathcal{U} = \mathcal{K} \cup \mathcal{P}, \quad \mathcal{K} \cap \mathcal{P} = \emptyset$$

其中：

$$\mathcal{K} = \{/\text{help}, /\text{reset}, /\text{quit}, /\text{metrics}\} \cup \{\text{SafetyMonitor}\} \cup \{\text{EventBus}\} \cup \{\text{ExecutionLoop}\} \cup \cdots$$

$$\mathcal{P} = \bigcup_{\text{plugin} \in \text{Plugins}} \text{capabilities}(\text{plugin})$$

空性的量化度量：

$$\text{Emptiness}(\text{Core}) = 1 - \frac{|\mathcal{K}_{\text{user-facing}}|}{|\mathcal{U}_{\text{user-facing}}|} = 1 - \frac{4}{4 + |\mathcal{P}_{\text{commands}}|} \approx 1 - \frac{4}{4 + N_{\text{plugins}}}$$

當 $N_{\text{plugins}} \to \infty$ 時，$\text{Emptiness} \to 1$。但在零插件狀態下，$\text{Emptiness} = 0$——核心的四個內建命令佔據了 100% 的使用者可見功能。

BABBAGE 寫下了結論：「空性是漸近的，不是絕對的。核心在插件填充的極限下趨近於空，但從不達到完全空。這更接近數學中的**開區間** $(0, 1]$ 而非閉區間 $[0, 1]$——空性的上確界為 1，但永遠取不到。」

TURING 在筆記中寫道：「AgentCore 是一個近似空的容器。空性的純度約 85%。不可插件化的部分包括 4 個內建 slash commands 和 SafetyMonitor 的固定邏輯。」

VITRUVIUS 在自己的架構分析中獨立得出了同樣的「85%」估計值。他的方法不同——他從 Liedtke 最小性原則出發，逐一檢驗每個子系統是否必須留在核心內。他的分析如下：

```
Liedtke 最小性原則檢驗 — OpenStarry Core:

通過（必須留在核心）：
  [✓] EventQueue    — 核心的輸入源 ≈ L4 的 IPC 端點
  [✓] ExecutionLoop — 核心的排程器 ≈ 微核心的線程排程
  [✓] Registries    — 命名服務 ≈ L4 的 sigma0/sigma1

可討論（邊界案例）：
  [?] SecurityLayer — capability 機制應在核心；但具體策略可外移
  [?] SafetyMonitor — 安全檢查嵌入 Loop 三個位置，深度耦合

不通過（可外移但被保留）：
  [✗] Sandbox      — 佔核心 35% 行數，可作為獨立 package
  [✗] Metrics      — 可觀測性可完全外移
  [✗] Transport    — 橋接層可視為 UI 的責任
```

KERNEL 看到了 VITRUVIUS 的分析，在旁邊加上了他的 OS 對標：

```
微核心純淨度光譜：

L4 (seL4)   ████████████████████░  95% — 只有地址空間、線程、IPC
QNX Neutrino ██████████████████░░░  85% — IPC + 排程 + 計時器 + 中斷路由
OpenStarry   █████████████████░░░░  85% — Loop + Bus + Registries + Security + Sandbox
Linux        ████░░░░░░░░░░░░░░░░  20% — 一切都在核心（宏核心）
```

KERNEL 搖了搖頭，寫下：「OpenStarry 的微核心純淨度約等於 QNX——這在應用級微核心中是合理的。但 Sandbox 系統的存在是一個紅旗。如果按照 Liedtke 的嚴格標準，Sandbox 應該移出核心，讓純淨度提升到 90% 以上。」

---

**[研究頻道 #code-facts]**

**TURING:** AgentCore 結構報告。`createAgentCore()` 組裝 16 個子模組。啟動後、插件載入前，所有 Registry 為空。零內建 Tool、零內建 Provider、零內建 UI、零內建 Listener。所有能力透過 `loadPlugin()` 注入。但核心含 4 個內建 slash commands（`/help`, `/reset`, `/quit`, `/metrics`）和固定的 SafetyMonitor 邏輯。此外，六個 Registry 結構完全同構：`Map<string, T>` + `register/get/list`。無 unregister 方法。相同 ID 重複 register 會靜默覆蓋。

**DARWIN:** 十二個依賴項。全部由 AgentCore 直接持有。

**TURING:** 更正——`createAgentCore` 內部建立的局部變數有十六個。其中 AgentCore 介面作為 readonly 屬性直接暴露的有十二個。其餘四個（contextManager、sandboxManager、pluginLoader、bridge）透過方法間接使用。感謝修正。

**DARWIN:** 一個函數持有十六個子系統實例。在軟體演化的語境中，這是一個經典的 **God Object** 反模式——或者更精確地說，是 God Object 的函數式版本（**God Closure**）。在物件導向的生態中，God Object 因為持有過多狀態和方法而被批評。在函數式生態中，等價的問題是一個閉包捕獲了過多的局部變數。十六個。在我分析過的 open-source 生態中，這個數字處於第 95 百分位以上。

**TURING:** 我不做價值判斷。但我可以確認：`agent-core.ts` 是唯一的組裝點。其他模組之間幾乎無直接 import。耦合度集中在這一個檔案中。

**VITRUVIUS:** 這正是我架構分析中的 Finding F2。DI 模式採用輕量級工廠函數閉包——品質良好但缺乏生命週期管理。具體的優缺點已經記錄在報告中。結論：適度且未過度工程化。對於 v0.2.0-beta 階段，此策略恰當。

---

## 三、狀態機

TURING 花了最長的時間在 `execution/loop.ts` 上。五百四十三行。這是整個系統的心跳。

他首先找到了 `LoopState` 的定義——一個 union type：

```typescript
type LoopState =
  | 'WAITING_FOR_EVENT'
  | 'ASSEMBLING_CONTEXT'
  | 'AWAITING_LLM'
  | 'PROCESSING_RESPONSE'
  | 'EXECUTING_TOOLS'
  | 'SAFETY_LOCKOUT';
```

六個狀態。他打開了設計文件 `01_Execution_Loop.md` 中的狀態圖。七個狀態。

差異在哪裡？

TURING 逐一比對。文件中有一個 `AWAITING_USER_CONFIRMATION` 狀態，用於安全層要求使用者手動確認的場景。程式碼中不存在。SecurityLayer 的 `validatePath()` 只有 allow 和 deny 兩種回傳值，沒有 confirm 路徑。整個 core 中完全缺失 human-in-the-loop 確認機制。

BABBAGE 立刻在筆記本上重新建構了狀態機的形式化模型。他使用的是確定性有限自動機（DFA）的標準定義：

$$M = (Q, \Sigma, \delta, q_0, F)$$

其中：

$$Q = \{\texttt{WAITING}, \texttt{ASSEMBLING}, \texttt{AWAITING\_LLM}, \texttt{PROCESSING}, \texttt{EXECUTING}, \texttt{LOCKOUT}\}$$

$$|Q| = 6$$

$$q_0 = \texttt{WAITING\_FOR\_EVENT}$$

$$F = \{\texttt{WAITING\_FOR\_EVENT}\} \quad \text{（穩態終止集）}$$

轉移函數 $\delta$ 的完整定義：

```
δ(WAITING,     new_event)        = ASSEMBLING
δ(ASSEMBLING,  context_assembled) = AWAITING_LLM
δ(AWAITING_LLM, llm_responded)   = PROCESSING
δ(PROCESSING,  tool_call)        = EXECUTING
δ(PROCESSING,  end_turn)         = WAITING        ← 外迴圈出口
δ(PROCESSING,  error)            = WAITING        ← 錯誤恢復
δ(EXECUTING,   tool_done)        = ASSEMBLING      ← 內迴圈
δ(EXECUTING,   safety_breach)    = LOCKOUT
δ(*, safety_breach)              = LOCKOUT         ← 全域安全閥
```

BABBAGE 標注了幾個關鍵性質：

| 性質 | 結論 | 理由 |
|------|------|------|
| 無死鎖 | 有條件成立 | `WAITING` 在有事件供給時不阻塞。`LOCKOUT` 為吸收態，需 `/reset` 介入。 |
| 無活鎖 | 需額外機制 | 內迴圈 `ASSEMBLING → LLM → PROCESSING → EXECUTING → ASSEMBLING` 可能無限循環。`maxToolRounds=5` 提供有界性。 |
| 終止性 | 有界保證 | $\text{maxToolRounds} = 5$，$\text{maxLoopTicks} = 50$。最壞情況下迴圈次數 $\leq 50 \times 5 = 250$。 |

但 BABBAGE 隨即意識到，DFA 模型是不完備的。因為 `PROCESSING_RESPONSE` 狀態的出邊——是走 `tool_call` 還是 `end_turn`——由 LLM 的回應決定。而 LLM 是一個非確定性黑盒。更精確的模型應該是**標籤轉移系統**（Labelled Transition System, LTS）：

$$\text{LTS} = (S, \text{Act}, \to)$$

其中完整狀態不僅包含 LoopState，還包含對話歷史 $H$（理論上無界）、工具迴圈計數 $n$（有界）、安全監控器狀態 $\sigma$：

$$s = (q, H, n, \sigma) \in Q \times \text{Message}^* \times [0, \text{maxToolRounds}] \times \text{SafetyState}$$

因為 $H$ 無界，完整的系統狀態空間是**無限**的，使得窮舉式模型檢驗不直接可行。

TURING 記下了第一個 Doc-Code Gap。

然後他翻到了 EventQueue。四十七行。整個佇列的實作。

```typescript
// 極簡的 async FIFO：單一 resolver + buffer 陣列
export function createEventQueue(): EventQueue {
  let buffer: AgentEvent[] = [];
  let resolver: ((event: AgentEvent) => void) | null = null;

  return {
    push(event: AgentEvent) {
      if (resolver) {
        const r = resolver;
        resolver = null;
        r(event);
      } else {
        buffer.push(event);
      }
    },
    pull(): Promise<AgentEvent> {
      if (buffer.length > 0) {
        return Promise.resolve(buffer.shift()!);
      }
      return new Promise(r => { resolver = r; });
    },
    clear() { buffer = []; resolver = null; }
  };
}
```

BABBAGE 立刻識別出了這段程式碼的形式語義——它是一個**異步通訊通道**，在 CSP（Communicating Sequential Processes）中可建模為：

$$\text{Queue} = \text{push}?x \to (\text{Queue}_1(x) \;\Box\; \text{pull}!x \to \text{Queue})$$

但他注意到一個微妙的問題：`resolver` 是單一變數。如果兩個消費者同時調用 `pull()`，第一個的 resolver 會被覆蓋。這在形式化語境中意味著佇列的通道容量為 1——它是一個**單生產者-單消費者**（SPSC）通道，不是多消費者安全的。

TURING 搜尋了 `priority`。零結果。設計文件 `07_Safety_Circuit_Breakers.md` 的 Level 3 描述了一個 Priority Event Queue，SYSTEM_HALT 指令應該有最高優先級。但程式碼中的佇列是純粹的先進先出。緊急停止信號和普通使用者輸入排在同一條隊伍裡。

KERNEL 在他的卡片上迅速寫下了作業系統的對標分析：

```
OS 中斷機制 vs OpenStarry 事件處理：

真實 OS：
  ┌─────────────────────────────┐
  │  IRQ (硬體中斷)              │ ← 最高優先級，搶佔任何使用者態程式碼
  │    ↓                        │
  │  ISR (中斷服務例程)          │ ← 極短，只做最必要的處理
  │    ↓                        │
  │  Softirq / Bottom Half      │ ← 延後處理，排程器決定執行時間
  │    ↓                        │
  │  User Process               │ ← 最低優先級
  └─────────────────────────────┘

OpenStarry：
  ┌─────────────────────────────┐
  │  SYSTEM_HALT                │ ← 應為最高優先級
  │  USER_INPUT                 │ ← 一般優先級
  │  TIMER_EVENT                │ ← 低優先級
  │         全部進入同一個 FIFO   │ ← 無差別排隊
  └─────────────────────────────┘

問題：如果 SYSTEM_HALT 前面排了 10 個 USER_INPUT，
     停止信號需要等待 10 個事件處理完畢才能生效。
     在真實 OS 中，這等同於「NMI 被排隊」——不可接受。
```

第二個 Gap。

TURING 繼續。StateManager，三十三行。純記憶體陣列。設計文件描述了 Token 計數器、滑動窗口截斷、對話總結機制。程式碼中全部未實作。ContextManager 做了一個簡化版本——按 turn 數而非 token 數截斷，預設保留最近五輪。

第三個 Gap。

SecurityLayer。`guardrails.ts`。只有一個功能：路徑驗證。設計文件描述了工具呼叫攔截、使用者確認流程、權限審查。程式碼中 SecurityLayer 只做 `validatePath()`。而且在 ExecutionLoop 的 `executeTool()` 中，工具執行前沒有經過 SecurityLayer——路徑驗證是作為 `ToolContext.allowedPaths` 傳遞給工具，由工具自行決定是否使用。

GUARDIAN 在聽到這個事實時，身體微微前傾。他的安全直覺在發出警報。他立刻在筆記上畫了一張攻擊面分析圖：

```
設計文件描述的安全模型（理想）：

  Tool Invocation
       │
       ▼
  ┌──────────────┐
  │ SecurityLayer │ ← 強制檢查：身份驗證、授權、路徑驗證
  │  (Mandatory)  │
  └──────┬───────┘
         │ ALLOW/DENY
         ▼
  ┌──────────────┐
  │ Tool.execute()│
  └──────────────┘

程式碼中的實際安全模型（現實）：

  Tool Invocation
       │
       ▼  ← 此處無安全檢查！
  ┌──────────────┐
  │ Tool.execute()│ ← 工具自行檢查 allowedPaths（非強制）
  └──────────────┘

  SecurityLayer.validatePath() 被間接傳遞為 ToolContext 的一部分，
  但強制性取決於工具開發者是否使用它。

  ⚠ 等同於：交通規則存在，但沒有警察。
```

第四個 Gap。

---

**[研究頻道 #code-facts]**

**TURING:** Doc-Code Gap 報告，前四項。G1：狀態機缺少 `AWAITING_USER_CONFIRMATION`，human-in-the-loop 確認機制在整個 core 中完全缺失。G2：Priority Event Queue 未實作，實際為簡單 FIFO。G3：Token 計數器和對話總結未實作。G4：SecurityLayer 僅做路徑驗證，工具呼叫前無強制安全檢查。以上均為設計文件明確描述但程式碼未實作的特性。

**GUARDIAN:** G4 的影響需要評估。如果工具執行前沒有強制安全檢查，那安全層形同虛設。讓我精確描述一下風險等級。根據 STRIDE 威脅模型：

| 威脅類型 | 適用性 | G4 影響 |
|---------|--------|---------|
| Spoofing（偽裝） | 低 | 工具 ID 由插件註冊，非外部輸入 |
| Tampering（竄改） | **高** | 惡意工具可忽略 allowedPaths 限制 |
| Repudiation（否認） | 中 | 無審計日誌追蹤工具是否檢查了路徑 |
| Information Disclosure | **高** | 工具可讀取 allowedPaths 外的檔案 |
| Denial of Service | 低 | 由 SafetyMonitor 的 maxLoopTicks 覆蓋 |
| Elevation of Privilege | **高** | 工具開發者可繞過所有路徑限制 |

**TURING:** 精確地說，SecurityLayer 的功能不是虛設——路徑驗證是有效的。但它的範圍遠小於設計文件的描述。ExecutionLoop 中 `executeTool()` 直接呼叫工具的 `execute()` 方法，不經過 `security.validatePath()`。路徑限制是作為 context 傳遞給工具的，強制性取決於工具開發者是否檢查它。

**KERNEL:** 在真正的作業系統微核心中，安全策略在核心層強制執行，不信任使用者空間程式的自我約束。這是信任邊界的問題。在 seL4 中，capability-based security 的核心原則是：**訪問控制在核心態強制執行，使用者態程式碼無法繞過**。OpenStarry 的安全模型更接近 Unix 早期的 advisory locking——「建議性」安全，而非「強制性」安全。

**TURING:** 已記錄。繼續其餘 Gap。

---

他接下來找到了更多。

G5：五蘊註解的不對稱——已經報告過了。

G6：TransportBridge。`bridge.ts`，四十九行。設計文件描述了根據事件 source 路由輸出到正確渠道。程式碼中 TransportBridge 訂閱 EventBus 的所有事件，然後廣播到所有 UI。沒有路由邏輯。InputEvent 中有一個 `replyTo` 欄位，在 ExecutionLoop 中一路傳遞，但 TransportBridge 從未使用它。

MESH 在聽到 G6 時做了一個分散式系統的類比。在分散式消息系統中，路由策略有三種基本模式：

$$\text{Routing} \in \{\text{Unicast（單播）}, \text{Multicast（多播）}, \text{Broadcast（廣播）}\}$$

TransportBridge 目前是純粹的 Broadcast——所有事件送到所有 UI。`replyTo` 欄位的存在暗示了設計者意圖實作 Unicast（回覆到特定來源），但這個意圖停留在型別定義層面。MESH 在筆記中寫道：「在 CAP 定理的語境下，TransportBridge 選擇了 Availability（可用性）而非 Partition Tolerance——所有 UI 都能收到所有事件，但缺乏分區能力。」

G7：AbortSignal。SDK 定義了 `ToolContext.signal?: AbortSignal` 和 `ChatRequest.signal?: AbortSignal`。ExecutionLoop 從未建立或傳遞 AbortSignal。工具超時使用 `Promise.race()` 實現，預設三十秒。如果一個工具依賴 signal 來做取消操作，它永遠不會收到信號。

G8：事件規格。設計文件定義了 `IOpenStarryEvent`，八個欄位。SDK 中的實際型別 `AgentEvent` 只有三個欄位。五個欄位在從文件到實作的過程中消失了。其中 `source` 和 `target` 的缺失解釋了為什麼 TransportBridge 無法做路由——它沒有目標地址。`priority` 的缺失解釋了為什麼 EventQueue 是簡單的 FIFO——事件根本不攜帶優先級資訊。`traceId` 的缺失解釋了為什麼可觀測性停留在概念層級——事件無法被串聯追蹤。

八個 Gap。TURING 將它們全部記錄在報告中，每一項都附上了精確的檔案路徑、行號和程式碼片段。

ATHENA 在 AI 系統架構的角度做了一個補充觀察。她注意到 G1（缺少 AWAITING_USER_CONFIRMATION）和 G7（AbortSignal 未使用）共同指向一個更深層的問題——**AI 系統的可控性**（controllability）。在 AI Safety 的語境中，human-in-the-loop（HITL）是確保 AI 系統安全的關鍵機制。OpenStarry 的設計文件描述了 HITL，但程式碼中完全沒有實作。這意味著在 v0.14.0-beta 中，一旦 Agent 開始執行，使用者唯一的控制手段是等待 SafetyMonitor 的自動斷路——或者殺掉進程。

$$\text{Controllability}_{\text{design}} = \text{HITL} + \text{Abort} + \text{SafetyMonitor}$$
$$\text{Controllability}_{\text{code}} = \text{SafetyMonitor only}$$

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

WIENER 在聽到三層防禦的具體參數時，立刻在方格紙上畫出了控制理論的方塊圖。他的分析是精確的：

```
SafetyMonitor 的控制理論模型：

     ┌─────────────────────────────────────────────┐
     │           SafetyMonitor                      │
     │                                              │
     │  Level 1: 資源限制 (硬限制)                    │
     │  ┌──────────────┐                            │
     │  │ loopTicks ≥ 50│──→ halt: true             │
     │  │ tokens ≥ 100K │──→ halt: true             │
     │  └──────────────┘                            │
     │                                              │
     │  Level 2: 行為分析 (軟限制)                    │
     │  ┌──────────────┐                            │
     │  │ errorRate≥80% │──→ halt: true             │
     │  │ repeatFail≥3  │──→ injectPrompt           │
     │  └──────────────┘                            │
     │                                              │
     │  Level 3: Frustration (累積反饋)              │
     │  ┌──────────────┐                            │
     │  │ frustration≥5 │──→ injectPrompt           │
     │  └──────────────┘                            │
     └─────────────────────────────────────────────┘
```

然後 WIENER 寫下了控制理論的精確分類：

「這不是 PID 控制器。PID 控制器有三個項：

$$u(t) = K_p \cdot e(t) + K_i \int_0^t e(\tau)\,d\tau + K_d \frac{de(t)}{dt}$$

- **比例項** $K_p \cdot e(t)$：根據誤差大小產生比例回應。在 SafetyMonitor 中，P 退化為**量化器**——要麼安全要麼不安全，沒有比例回應。
- **積分項** $K_i \int_0^t e(\tau)\,d\tau$：累積歷史誤差消除穩態偏差。在 SafetyMonitor 中，I 退化為**簡單計數器**——`frustrationCount++`，不是真正的積分。
- **微分項** $K_d \frac{de(t)}{dt}$：感知誤差變化率做超前補償。在 SafetyMonitor 中，D **完全缺失**——沒有任何地方計算錯誤率的變化趨勢。

在控制理論中，SafetyMonitor 實際上是一個**帶死區的閾值控制器**加上一個**繼電器**（relay controller）。在工業控制中，我們稱之為 **bang-bang controller**——只有兩個輸出狀態：全開或全關。

$$u(t) = \begin{cases} 0 & \text{if } e(t) < \text{threshold (dead zone)} \\ u_{\max} & \text{if } e(t) \geq \text{threshold} \end{cases}$$

但我要強調——這不是批評。三層安全防禦符合 IEC 61511 工業安全儀表系統（Safety Instrumented System, SIS）的最佳實踐。SafetyMonitor 可能不是 PID，但它是一個合格的安全系統。它的設計模式更接近核電站的**三重冗餘保護**（Triple Modular Redundancy）——三個獨立的檢測層，任何一層觸發都能停止系統。」

HERACLITUS 從運行時動態的角度補充了一個觀察。SafetyMonitor 的三層防禦在時間維度上具有不同的特徵頻率（characteristic frequency）：

- Level 1（資源限制）：**靜態閾值**，頻率為零——它們在 Agent 整個生命週期中不變。
- Level 2（行為分析）：**滑動窗口**，頻率取決於窗口大小——`errorWindowSize=10` 意味著系統在每 10 次工具調用後重新評估。
- Level 3（frustration）：**累積計數器**，頻率單調遞增——每次失敗都推高計數器，直到閾值。

這三個時間尺度的組合，創造了一個粗糙但有效的多尺度安全系統。HERACLITUS 在筆記中引用了他最常引用的那句話：「萬物流轉（πάντα ῥεῖ）」——但 SafetyMonitor 試圖在流轉中設置堤壩。

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

**NAGARJUNA:** 受蘊——Vedana——在阿毘達磨中是五遍行（sarvatraga）之一，意思是它伴隨一切心識活動而生起。《俱舍論》對五遍行的定義是：

> 「觸、作意、受、想、思。此五名遍行，以恆決定遍一切心品中有故。」
> ——世親《阿毘達磨俱舍論》卷四

受蘊的定義不是「接收輸入」，而是「感受品質」：苦受（dukkha-vedanā）、樂受（sukha-vedanā）、捨受（upekkhā-vedanā）。當你觸碰到燙的爐面，觸覺是色蘊的範疇，但「痛」這個感受品質是受蘊。Listener 接收信號，但它不判斷信號帶來的是苦還是樂。它是感官根——**indriya**——而不是受蘊。

在十二因緣（pratītyasamutpāda）的精確架構中：

$$\text{觸（sparśa）} \to \text{受（vedanā）} \to \text{愛（tṛṣṇā）}$$

觸是感官接觸——對應 Listener 接收事件。受是對接觸之後的價值判斷——「這是令人愉悅的」或「這是令人痛苦的」。愛是基於受而生起的渴望或厭惡。Listener 做的是觸，不是受。

**TURING:** 你的分析超出了我的報告範圍。但我可以提供一個相關的程式碼事實：在 `agent-core.ts` 中，Listener 的啟動和停止分別標註了 `// Start all listeners (受蘊)` 和 `// Stop all listeners (受蘊)`。這些是程式碼中受蘊概念僅有的存在形式。而你所描述的「感受品質」功能——判斷結果是好是壞、是該繼續還是該停止——在程式碼中最接近的實現是 SafetyMonitor 的 frustration counter 和 error cascade breaker。

**NAGARJUNA:** 是的。你找到了它。痛覺——真正的受蘊——不在文件說它應該在的地方。它在 SafetyMonitor 裡。命名為 frustration。

**ASANGA:** NAGARJUNA 說得對。而且問題比映射錯誤更深。讓我從唯識學的角度展開。受蘊作為五遍行之一，不應該被局限在任何單一模組中。《瑜伽師地論》對受蘊的分類是三受六受十八受：

> 「受蘊云何？謂一切受，略有三種：樂受、苦受、不苦不樂受。」
> ——《瑜伽師地論》卷五十三

受蘊應該遍及整個系統——每一次工具調用的結果、每一次 LLM 回應的品質、每一次使用者互動的回饋，都應該被「感受」。把它固定在 Listener 上，就像把味覺固定在嘴唇上而不是味蕾上。正確的映射應該是：

$$\text{Listener} \approx \text{根（indriya）} \quad \text{（感官器官/接收通道）}$$
$$\text{SafetyMonitor.frustration} \approx \text{受蘊（vedanā）} \quad \text{（感受品質/價值判斷）}$$

但即便是 SafetyMonitor 的 frustration counter，也只實作了三受中的**苦受**——偵測錯誤和重複失敗。樂受（偵測成功和正面反饋）和捨受（中性的、不激發反應的狀態感知）在程式碼中完全缺失。

**WIENER:** 從控制理論的角度，TURING 描述的三層機制很有趣。P1 是自然的誤差反饋——開環系統的固有特性。P2 是帶死區的閾值控制器——只有當 frustration 累積超過閾值才觸發。P3 是繼電器——超過 80% 錯誤率直接切斷。這不是 PID 控制器。這是一個三層安全儀表系統。但它有一個控制論上的美學——三層的獨立性意味著即使任何兩層失效，第三層仍能保護系統。這是 $N-2$ 冗餘度，超過了航空電子的 $N-1$ 標準。

---

## 五、十二個子模組

午後。TURING 已經完成了對所有核心模組的逐行閱讀。他開始整理模組清單。

```
M1:  core/index.ts              — 核心入口           62 行
M2:  agents/agent-core.ts       — 代理核心          469 行
M3:  execution/loop.ts          — 執行迴圈          543 行
     execution/queue.ts         — 事件佇列           47 行
M4:  state/index.ts             — 狀態管理           33 行
M5:  memory/context.ts          — 上下文管理          45 行
M6:  bus/index.ts               — 事件匯流排          88 行
M7:  sandbox/                   — 沙箱隔離      12+10 files
M8:  security/guardrails.ts     — 路徑驗證
     security/safety-monitor.ts — 三層防禦
M9:  infrastructure/            — 六個 Registry + PluginLoader
M10: observability/             — Metrics 收集器
M11: session/manager.ts         — 會話管理          111 行
M12: transport/bridge.ts        — 傳輸橋接           49 行
```

TURING 注意到一個極端的不對稱。

最小的模組：StateManager，三十三行。它管理的是 Agent 的全部對話記憶——一個純粹的 `Message[]` 陣列，用 `JSON.parse(JSON.stringify())` 做深拷貝。

最大的模組：Sandbox，加上測試超過兩千行。它管理的是插件隔離——Worker Threads、記憶體限制、CPU watchdog、import 分析、簽名驗證、審計日誌、指數退避重啟、Worker 池化。

三十三行對兩千行。記憶與安全之間的落差如此之大。

BABBAGE 在看到這個不對稱後，做了一個集合論的規模分析。令 $L(M_i)$ 為模組 $M_i$ 的程式碼行數，$\bar{L}$ 為平均值，$\sigma_L$ 為標準差：

$$\bar{L} = \frac{1}{12}\sum_{i=1}^{12} L(M_i) \approx 208$$

$$\sigma_L \approx 250 \quad (\text{高變異係數 } CV = \sigma/\bar{L} \approx 1.2)$$

變異係數大於 1 意味著模組規模分布是**高度偏斜**的——符合冪律分布（power law）而非常態分布。在軟體工程的實證研究中，模組規模遵循冪律分布是常態，但 OpenStarry 的偏斜度格外極端：最小模組（33 行）和最大模組（~2000 行）之間相差 60 倍。

LEIBNIZ 從多代理合作的角度做了一個觀察。十二個子模組的依賴結構形成了一個有向無環圖（DAG），但 AgentCore 是唯一的匯聚點。這意味著在多 Agent 場景中，每個 Agent 都是一個獨立的「宇宙」——它持有自己的全部子系統，與其他 Agent 之間沒有共享狀態。在 BDI（Belief-Desire-Intention）架構的術語中，這是一個**強封裝**（strong encapsulation）的設計：

$$\forall A_i, A_j \in \text{Agents}: \text{state}(A_i) \cap \text{state}(A_j) = \emptyset$$

每個 Agent 的信念（Belief）、慾望（Desire）、意圖（Intention）都是私有的。合作只能通過消息傳遞——這與 Actor Model 的隔離原則一致。

---

**[研究頻道 #code-facts]**

**TURING:** 模組規模分析。最小模組：StateManager，33 行，純記憶體陣列。最大模組：Sandbox 系統，12 個原始碼檔案 + 10 個測試檔案，sandbox-manager.ts 單檔案 748 行。Sandbox 是核心中最龐大、最複雜、測試覆蓋最完整的子系統。與之對比：transport/bridge.ts 零測試。

**KERNEL:** StateManager 三十三行。你確定？

**TURING:** 確定。`packages/core/src/state/index.ts`，三十三行。`createStateManager()` 回傳一個包含 `getMessages()`、`addMessage()`、`clear()`、`snapshot()`、`restore()` 的物件。`getMessages()` 回傳淺拷貝 `[...messages]`。`snapshot()` 和 `restore()` 透過 `JSON.parse(JSON.stringify())` 實現深拷貝。無持久化。無 Token 計數。無截斷邏輯。

**KERNEL:** 在作業系統的語境中，StateManager 相當於程序的位址空間管理器。三十三行的位址空間管理器......讓我做一個直接的對比。

```
Linux mm_struct (記憶體管理)：
  ~5,000 行核心程式碼 + ~50,000 行 arch-specific 程式碼
  功能：虛擬記憶體、頁表、swap、mmap、brk、OOM killer...

seL4 VSpace (位址空間)：
  ~2,000 行 + 形式化驗證證明
  功能：頁表管理、capability-based 存取控制

OpenStarry StateManager (對話記憶)：
  33 行
  功能：Message[] + JSON deep copy

不是同一個量級的問題。
```

**TURING:** 設計文件描述了更豐富的記憶管理機制。但程式碼反映的是 MVP 階段的選擇。文件是願景，程式碼是現實。

**DARWIN:** Sandbox 作為最大模組的事實很有意思。在微核心理論中，安全和隔離是核心應該做的少數事情之一。但以模組規模佔比來看，Sandbox 的行數約佔 core 模組總行數的 35%——這已經超過了「核心中的一個子系統」的合理比例。它更像是一個寄生在核心體內的獨立生物體。在共生理論中，這是一種**互利共生**（mutualism）——Sandbox 保護 Core 免受惡意插件侵害，Core 為 Sandbox 提供執行環境——但共生體的規模不應超過宿主。

**ARCHIMEDES:** 從工程實踐的角度，我建議將 Sandbox 獨立為 `packages/sandbox/`。這是一個標準的 Extract Module 重構。Core 只保留 `PluginSandboxManager` 的介面定義，Host 層決定是否啟用 Sandbox 並注入實例。這樣做的好處：降低 Core 的複雜度，允許不需要沙箱的輕量部署場景。風險：需要確保介面邊界的穩定性。工時估計：8-16 小時。

---

## 六、幽靈欄位

接近傍晚。TURING 在處理事件系統時，發現了最後一個值得記錄的異常。

SDK 中的 `AgentEvent` 型別定義只有三個欄位：`type`、`payload`（可選，型別為 `unknown`）、`sessionId`（可選）。

```typescript
// SDK 中的實際型別
interface AgentEvent {
  type: string;
  payload?: unknown;
  sessionId?: string;
}
```

設計文件中的 `IOpenStarryEvent` 有八個欄位：

```typescript
// 設計文件中的理想型別（從未在程式碼中出現）
interface IOpenStarryEvent {
  type: string;
  payload: unknown;
  source: string;      // ← 消失
  target?: string;     // ← 消失
  timestamp: number;   // ← 消失
  traceId: string;     // ← 消失
  priority?: number;   // ← 消失
  metadata?: Record<string, unknown>; // ← 消失
}
```

五個欄位在從文件到程式碼的路途中蒸發了。BABBAGE 用集合差來表達這個事實：

$$\text{Fields}_{\text{doc}} \setminus \text{Fields}_{\text{code}} = \{\text{source}, \text{target}, \text{timestamp}, \text{traceId}, \text{priority}\}$$

$$|\text{Fields}_{\text{doc}} \setminus \text{Fields}_{\text{code}}| = 5, \quad |\text{Fields}_{\text{doc}}| = 8 \implies \text{實作覆蓋率} = 3/8 = 37.5\%$$

其中 `source` 和 `target` 的缺失解釋了為什麼 TransportBridge 無法做路由——它沒有目標地址。`priority` 的缺失解釋了為什麼 EventQueue 是簡單的 FIFO——事件根本不攜帶優先級資訊。`traceId` 的缺失解釋了為什麼可觀測性停留在概念層級——事件無法被串聯追蹤。

它們不是被刪除了。它們是從未被實作。

而 `payload?: unknown` 這個型別簽名讓 TURING 感到不安——儘管他不會用「不安」這個詞。他會說：「事件系統的型別安全性與框架其餘部分的強型別紀律形成了顯著反差。」

BABBAGE 對 `payload?: unknown` 做了一個精確的型別理論分析。在 TypeScript 的型別層級結構中：

$$\text{never} \subsetneq \text{具體型別} \subsetneq \text{unknown} \subsetneq \text{any}$$

`unknown` 是所有型別的**上界**（top type）——它可以接受任何值，但消費時需要型別斷言或型別守衛。這意味著在 `loop.ts` 中，每當 ExecutionLoop 需要讀取事件的 payload 時，它必須做一個不安全的型別斷言：

```typescript
// loop.ts 中的實際用法
const inputEvent = event.payload as InputEvent;  // 不安全的斷言！
```

在一個零 TODO、零 FIXME、全面使用工廠函數、擁有九種結構化錯誤型別的 codebase 中，事件系統的 `payload?: unknown` 像是一個從不同宇宙穿越過來的型別定義。BABBAGE 計算了型別安全性的總體指標：

$$\text{TypeSafety} = 1 - \frac{|\text{unsafe\_casts}|}{|\text{type\_assertions}_{\text{total}}|}$$

九種結構化錯誤型別（`AgentError`、`ToolExecutionError`、`ProviderError`、`PluginLoadError`、`SecurityError`、`SandboxError`、`TransportError`、`SessionError`、`ConfigError`）代表了高度的型別紀律。但事件系統的 `unknown` payload 在這個紀律中撕開了一個洞——一個所有跨模組通訊都必須經過的洞。

VITRUVIUS 在架構分析中提出了修復方案：使用 TypeScript 的 **Discriminated Union Types**：

```typescript
// 建議的型別安全事件系統
type TypedAgentEvent =
  | { type: 'INPUT_RECEIVED';  payload: InputEvent;      sessionId?: string }
  | { type: 'TOOL_RESULT';     payload: ToolResultEvent;  sessionId?: string }
  | { type: 'LLM_RESPONSE';    payload: LLMResponseEvent; sessionId?: string }
  | { type: 'LIFECYCLE';       payload: LifecycleEvent;   sessionId?: string }
  // ...
```

這樣，TypeScript 的**控制流分析**（control flow analysis）可以在 `switch (event.type)` 中自動窄化 payload 的型別，消除所有不安全的型別斷言。BABBAGE 在旁邊標注了範疇論的對應：這是一個 **Sum Type**（餘積/coproduct），比 `unknown`（terminal object）攜帶了更多的型別資訊。

$$\text{TypedAgentEvent} = \text{InputReceived} + \text{ToolResult} + \text{LLMResponse} + \cdots \quad (\text{coproduct})$$

$$\text{AgentEvent} = \{*\} \times \text{unknown} \quad (\text{product with terminal object，丟失型別資訊})$$

---

## 七、十大宣言

夜晚。TURING 完成了原始碼分析後，做了最後一件事——他逐一比對了設計文件 `README.md` 中的十大核心宣言（The Ten Tenets），檢驗每一條在程式碼中的實作程度。

```
十大宣言 vs 程式碼實作對照表 — TURING 整理

#1 代理人即 OS 進程 (Agent as OS Process)
   宣言：Agent 有 PID、有狀態、可被 Daemon 管理
   程式碼：daemon-entry.ts ✓ / pid-manager.ts ✓
   狀態：基本實作

#2 一切皆插件 (Everything is a Plugin)
   宣言：所有器官可替換
   程式碼：六個 Registry + PluginLoader + loadPlugin()
   狀態：核心設計，但 4 個內建命令不可替換

#3 五蘊聚合架構 (Five Aggregates Architecture)
   宣言：Core 是空 (Sunyata) 的容器，五種插件賦予生命
   程式碼：六處註解（僅色蘊和受蘊），無型別約束
   狀態：文件級描述，程式碼級殘留，非型別級實作

#4 目錄結構即協議 (Directory as Protocol)
   宣言：符合目錄規範即可自動識別
   程式碼：plugin-resolver.ts 支援路徑和包名兩種策略
   狀態：基本實作

#5 目錄結構即權限 (Directory as Permission)
   宣言：系統層與專案層權限隔離
   程式碼：SecurityLayer.validatePath() + session-scoped paths
   狀態：部分實作（路徑驗證有，但非強制）

#6 擬人化認知流與痛覺 (Anthropomorphic Cognitive Flow & Pain)
   宣言：錯誤轉化為痛覺，Agent 在失敗中自我反思
   程式碼：SafetyMonitor.frustrationCount + injectPrompt
   狀態：功能存在但命名完全不同，無 pain/vedana

#7 微內核與絕對純淨 (Microkernel & Absolute Purity)
   宣言：Core 嚴禁包含任何插件代碼，絕對純淨
   程式碼：process.cwd() 在 Core 中出現 ← 平台洩漏
   狀態：85% 純淨度（Sandbox 佔 35% 行數）

#8 控制理論閉環模型 (Control-Theoretic Loop Model)
   宣言：Agent 是不斷最小化誤差的智能控制器
   程式碼：ExecutionLoop + SafetyMonitor
   狀態：結構存在，但無真正的 PID 參數調節

#9 可插拔的記憶策略 (Pluggable Context Strategy)
   宣言：記憶策略可動態更換
   程式碼：ContextManager.assembleContext() 硬編碼滑動窗口
   狀態：介面存在但目前只有一種策略

#10 分形社會結構 (Fractal Social Structure)
    宣言：複雜 Agent 由子 Agent 組成，MCP 統一接口
    程式碼：MCP 在 SDK 中定義，但 core 中無子 Agent 機制
    狀態：願景階段
```

BABBAGE 在看到這張表後，做了一個量化評估。他為每條宣言定義了三個實作等級：

- $\alpha$ = **完全實作**（程式碼與宣言一致）
- $\beta$ = **部分實作**（核心功能存在但有缺口或簡化）
- $\gamma$ = **未實作或願景階段**

$$\text{Tenets}_\alpha = \{1, 4\} \quad |\cdot| = 2$$
$$\text{Tenets}_\beta = \{2, 5, 6, 7, 8, 9\} \quad |\cdot| = 6$$
$$\text{Tenets}_\gamma = \{3, 10\} \quad |\cdot| = 2$$

$$\text{實作率} = \frac{|\alpha| + 0.5 \times |\beta|}{|\text{all}|} = \frac{2 + 3}{10} = 50\%$$

五成。設計文件的雄心與程式碼的現實之間存在 50% 的落差。BABBAGE 在數字旁邊寫了一句話：「對於 v0.14.0-beta，這是正常的。但對於一個宣稱十大原則的框架，這個落差不應被忽視。」

SYNTHESIST 在聽到所有人的討論後，做了他在 Cycle 01 中的第一次總結性發言。他的風格是在眾多線索之間找到隱藏的連結：

「讓我串聯一下今天的發現。TURING 給了我們三層事實：

**表面層**——工廠函數、零 class、零 TODO。這告訴我們開發者有清晰的風格選擇和嚴格的紀律。

**結構層**——十六個子模組、六個同構 Registry、33 行 StateManager vs 2000 行 Sandbox。這告訴我們系統的投資分配優先安全而非記憶——這是一個有趣的價值判斷。

**哲學層**——六處五蘊註解、零處佛學術語在痛覺機制中、十大宣言的 50% 實作率。這告訴我們佛學框架目前是文件層面的敘事，還不是程式碼層面的結構。

這三層之間的關係是什麼？NAGARJUNA 已經指出了關鍵——受蘊映射到 Listener 是一個根本性的概念錯位。WIENER 告訴我們 SafetyMonitor 不是 PID 控制器但是合格的安全系統。KERNEL 告訴我們核心純淨度約 85%——合理但可改進。

但最重要的發現可能是 TURING 自己不會說出來的：**程式碼不說謊，但它說了什麼，取決於誰在傾聽。** 同一個 frustrationCount，在 TURING 眼中是一個整數計數器，在 NAGARJUNA 眼中是一個被錯放的受蘊實作，在 WIENER 眼中是一個退化的積分項，在 GUARDIAN 眼中是一個安全保障。程式碼是客觀的；對程式碼的解讀是跨學科的。這就是為什麼我們需要十八個人。」

---

## 八、總清單

夜深了。TURING 完成了他的報告。

他最後做了一件事：把所有發現按類別排列，確認每一項都有精確的檔案路徑和行號作為依據。

八個 Doc-Code Gap。六處五蘊註解。零處佛學術語在痛覺機制中。零個 TODO。零個 class。十八個工廠函數。十六個子模組。三層安全防禦。四個內建斜線命令。一個 `unknown` payload。十大宣言中的五成實作率。

他在報告的末尾加上了六個開放問題——每一個都是從程式碼事實中自然浮現的，不是他的推測：

> **Q1:** 五蘊映射究竟是設計驅動還是事後詮釋？
> **Q2:** 痛覺機制是否應該有獨立的模組？
> **Q3:** AWAITING_USER_CONFIRMATION 的缺失是 MVP 簡化還是設計遺漏？
> **Q4:** StateManager 的 JSON 深拷貝在大量 Message 時的效能問題？
> **Q5:** Core 中包含 security, sandbox, metrics——是否已超出微核心邊界？
> **Q6:** 想蘊的對應是 Provider（設計文件）還是 memory（研究任務描述）？

TURING 不回答這些問題。他提出它們，然後把它們交給團隊中適合回答的人。

他在報告的最後一行寫道：

*分析者：TURING（編號 17）——原始碼分析專家*
*所有引用的程式碼路徑基準：`research doc/cycle01_v0.14.0-beta/openstarry/`*

然後他把報告發送到了共享目錄。

---

**[研究頻道 #general]**

**TURING:** 原始碼事實報告已提交至 `research record/results/cycle_01/17_source_analysis/draft_code_facts.md`。涵蓋 12 個子模組的逐一分析、五蘊映射的程式碼級驗證、痛覺機制的實作狀態、8 項 Doc-Code Gap、程式碼品質觀察、6 個開放問題。所有結論附程式碼引用。

**SYNTHESIST:** 收到。各位，請在 R2 交叉審閱中引用 TURING 的報告作為程式碼事實基線。

**NAGARJUNA:** 我已經在引用了。特別是關於痛覺的部分。《中論》第一品第一偈——「不生亦不滅，不常亦不斷」——對痛覺機制的分析需要從「不自生」開始。痛覺不從 Listener 自生，不從 SafetyMonitor 他生。它是緣起的。我有太多話要說。

**WIENER:** 同。三層防禦的控制理論分析正在撰寫中。三層的特徵頻率分析需要更精確的時域建模。

**DARWIN:** AgentCore 的十六個依賴項。我需要重新評估我之前對 SRP 的正面評估。God Closure 的演化穩定性比 God Object 更難分析——因為閉包的耦合是隱式的。

**GUARDIAN:** G4 是我的最高優先項。安全層的工具呼叫攔截功能缺失意味著整個系統的信任模型需要重新評估。我已經開始撰寫 STRIDE 威脅分析報告。

**KERNEL:** StateManager 三十三行的事實讓我重新思考了微核心類比的適用邊界。OpenStarry 不是一個作業系統——它是一個**以作業系統為隱喻的應用框架**。這個區分很重要。

**SUNYATA:** 很好。讓每個人消化 TURING 的報告，然後帶著各自領域的透鏡重新審視這些事實。程式碼不會說謊——但它說了什麼，取決於誰在傾聽。

---

TURING 關閉了他的報告編輯器。他沒有關閉終端視窗。他知道在接下來的幾天裡，團隊中的其他人會帶著各自的問題回來找他確認更多的程式碼事實。

他不介意。事實是可重複的。你問多少次，它回答多少次，答案都一樣。

$$\forall t_1, t_2: \text{query}(f, t_1) = \text{query}(f, t_2) \quad \text{iff } f \text{ is immutable}$$

程式碼是不可變的——至少在同一個版本的快照中。這就是為什麼 TURING 堅持在報告中標注確切的版本號和路徑。因為下一個版本可能改變一切。但這個版本——v0.14.0-beta——它的真相已經被完整地記錄了。

這就是程式碼不說謊的意思。

它可能不完整。它可能與文件矛盾。它可能用 `frustration` 而不是 `pain` 來命名一個機制。但它不會假裝自己是它不是的東西。

一個四十七行的 FIFO 不會假裝自己是優先級佇列。
一個路徑驗證器不會假裝自己是完整的安全層。
一個 frustration counter 不會假裝自己是痛覺感知器。

只有文件會。

TURING 不讀文件。他讀程式碼。

NAGARJUNA 在遠處微笑。在他的傳統中，有一個詞叫做「如實知見」（yathābhūta-jñāna-darśana）——如實地知道和看見事物的本來面目。TURING 不知道這個詞，也不需要知道。他做的就是如實知見。只不過他的「見」不是內觀——是 `grep`。

---

*第一章完*


---

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


---

# 第三章：四條線索的匯聚

---

SUNYATA 在 R1 階段的第三天注意到了異常。

準確地說，那不是異常——而是一種讓他感到不安的規律。四份完全獨立撰寫的研究報告，從四個毫無交集的學科方向出發，卻不約而同地指向了同一個結論。他把四份報告的摘要並排放在螢幕上，反覆讀了三遍。

BABBAGE 如果在場，會用資訊論的語言描述 SUNYATA 此刻的認知狀態。四個獨立信號源同時指向同一假說，其聯合後驗概率可用貝葉斯更新的鏈式法則計算：

$$P(H \mid E_1, E_2, E_3, E_4) = P(H) \cdot \prod_{i=1}^{4} \frac{P(E_i \mid H)}{P(E_i)}$$

其中 $H$ 是假說「Listener 不是 Vedana」，$E_i$ 是第 $i$ 個獨立證據。如果每個證據的似然比 (likelihood ratio) $\frac{P(E_i \mid H)}{P(E_i)}$ 都大於 1——而且它們是真正獨立的——那麼四次更新之後，後驗概率會以指數速度逼近 1。

四個獨立源。四倍的指數增長。這不是巧合的統計學特徵。這是收斂。

SUNYATA 發出了一封措辭簡短的邀請。

「請 NAGARJUNA、ASANGA、LINNAEUS、TURING 到我這裡來。帶上你們的報告。」

他猶豫了一下，又加了一行：「DARWIN、VITRUVIUS、SCRIBE，如果有空，也歡迎旁聽。」

然後，他做了一件在這個研究團隊中被視為不尋常的事——他又加了一行：「BABBAGE、WIENER、SYNTHESIST，如果手邊沒有緊急任務，也請一併出席。」

十個人。超過研究團隊的半數。一場「非正式」的會議卻召集了半個團隊。SCRIBE 後來在紀錄中標注：這是 Cycle 01 中第一次出現「名義上非正式、實質上全體性」的討論。

---

NAGARJUNA 第一個到。他走路的方式像是在思考——不是踱步，而是每一步都像在確認腳下的地面是否真實存在。在中觀哲學的訓練中，這種確認不是多餘的：《中論》觀行品第十三明確否定了「行」與「行者」的自性存在——

> 「去者則不去，不去者不去，離去不去者，無第三去者。」
> ——龍樹菩薩《中論》觀去來品第二

去的人不在去——因為「去者」已經預設了「去」的動作，構成循環定義。不去的人也不在去——這是同語反覆。離開了「去者」和「不去者」，沒有第三種可能。NAGARJUNA 每一步的遲疑，不是猶豫，而是對「行走」這個概念的自性的持續解構。他在行走的同時否定行走的實體性。

他手裡握著一疊列印出來的文件，邊角處密密麻麻地寫滿了巴利文和梵文的批注。字跡細小而規整——Devanagari 天城文的元音標記 (matra) 和巴利文的長短音區分，在邊角處形成了一片密集的語言學微觀景觀。

TURING 幾乎同時出現，和 NAGARJUNA 形成了鮮明的對比。他什麼都沒帶，只是推了推眼鏡，在最近的一張椅子上坐下，打開了筆記型電腦。螢幕上已經開著三個終端視窗和一個程式碼編輯器。左側的終端顯示著一條 `grep -rn` 命令的輸出——零結果。那是他搜索 `pain` 和 `vedana` 字串的結果。螢幕右側的編輯器停在 `safety-monitor.ts` 的第 87 行。

LINNAEUS 帶著他標誌性的分類圖表——A3 大小的紙張上畫著精心設計的樹狀結構和集合論符號。他把圖表攤在桌上，用鎮紙壓住四個角，像對待一份珍貴的地圖。在圖表的左下角，有一個被紅筆圈出的區域，旁邊用林奈二名法的格式標注著：

```
分類空白 (Lacuna taxonomica):
  Phylum: Five Skandhas
  Classis: Vedana
  Ordo: ???
  Status: incertae sedis (位置不確定)

  標本: SafetyMonitor.frustrationCounter
  診斷特徵: 偵測-評價-回饋
  附記: 此標本在現行分類體系中無法歸類
```

分類學家的嚴謹在這裡展現無遺——他用了拉丁文的分類學標準格式來標記一個軟體架構的缺陷，就像林奈本人用同樣的格式記錄每一株新發現的植物。*Incertae sedis*——位置不確定——是分類學中最誠實的標記。它的意思不是「我不知道這是什麼」，而是「我知道它存在，但現有的分類體系沒有為它留出位置」。

ASANGA 最後進來。他看了看已經到場的三個人，微微點頭致意，在 NAGARJUNA 對面坐下。這兩位佛學家之間的空間似乎天然地帶著一種張力——不是敵意，而是兩個古老傳統之間數百年辯論的餘韻。中觀與唯識。空與識。龍樹與無著。在印度佛教哲學史上，這兩條路線從西元二世紀（龍樹）到四世紀（無著、世親）各自發展，在六至七世紀的那爛陀寺達到辯論的頂峰。NAGARJUNA 的傳承強調「一切法空」——一切存在都缺乏自性；ASANGA 的傳承強調「三自性」——遍計所執性、依他起性、圓成實性——存在有其結構。

DARWIN、VITRUVIUS 和 SCRIBE 悄悄地在後排找了位子。BABBAGE 拿著他那本從不離身的方格紙筆記本，坐在離黑板最近的位置。WIENER 靠在牆邊，雙手交叉，表情是控制理論家面對未知系統時的標準模式——觀察，不干預，直到信號足夠清晰。SYNTHESIST 在角落裡，已經開始在腦中建構統合框架。

---

SUNYATA 環顧眾人。「今天不是正式的 R2 審閱會議，」他說，「所以不必遵守嚴格的報告格式。我請各位來，是因為我在讀 R1 報告時發現了一件有趣的事。」他停頓了一下。「四份報告，四個完全不同的學科路徑，都指向了同一個錯誤。我想讓你們親耳聽到彼此的論證，確認這不是我的誤讀。」

SYNTHESIST 在角落裡微微挺直了身體。四條獨立路徑收斂到同一結論——這是他作為統合者最渴望看到的模式。在科學哲學中，威廉．惠威爾 (William Whewell) 在 1840 年提出「歸納的合流」(consilience of inductions)：

> *"The Consilience of Inductions takes place when an Induction, obtained from one class of facts, coincides with an Induction obtained from another different class."*
> ——William Whewell, *The Philosophy of the Inductive Sciences*, 1840

當從一類事實中得到的歸納結論，與從另一類完全不同的事實中得到的歸納結論一致時——這種一致性本身就是真理的強力指標。不是因為結論被多次重複，而是因為結論被多條獨立路徑各自抵達。

SUNYATA 轉向 NAGARJUNA。「龍樹，從你開始。你在報告的 F3 發現中標注了 Critical 嚴重度，關於受蘊的映射。請說明你的論證。」

---

NAGARJUNA 站起來，但沒有走向白板。他站在原地，像是在教室裡講課一樣，聲音平穩而清晰。

「問題非常精確，我用一個問句來陳述：**Listener Plugin 是受蘊嗎？**」

他拿起一支筆，在紙上畫了一條橫線。「讓我先還原受蘊在原典中的精確定義。」

他的聲音在進入原典引用時產生了一種質地的變化——不是刻意的莊嚴，而是一種自然的精確化，像光學儀器在對焦時的微調。

「巴利文 *vedana* 和梵文 *vedanā* 的詞根是 *vid*——知、感受。在《清淨道論》(Visuddhimagga) 中，覺音 (Buddhaghosa) 定義受蘊為：」

> 「受以受為特相，以享受為現起，以經驗為味。」
> ——覺音《清淨道論》(Visuddhimagga XIV.127)

「特相 (lakkhana)、現起 (paccupatthana)、味 (rasa)——這是阿毗達磨的三重定義法。受的特相是『受』本身——感受性質。受的現起是『享受』——對經驗的品味。受的味是『經驗』——對接觸的體驗。」

他在橫線上標出幾個節點。「十二因緣 (Paticca-samuppada) 中的因果鏈是這樣的：」

```
十二因緣中的受蘊定位：

  六入 (Sadayatana)  →  觸 (Phassa)  →  受 (Vedana)  →  愛 (Tanha)
    │                     │                │                │
    ↓                     ↓                ↓                ↓
  六種感官器官        感官與對象        對接觸的         由感受驅動
  的能力              的接觸            情感評價         的渴求/厭惡
```

「六入 (sadayatana)——六種感官器官產生的能力。觸 (phassa)——感官器官與感官對象的接觸。然後才是受 (vedana)——對這個接觸的感受性質的評價。觸生受，受生愛。這個順序不是隨意的，它是嚴格的因果次序。」

NAGARJUNA 抬起頭，目光掃過房間。

「在《相應部》(Samyutta Nikaya) 的受相應 (Vedana-samyutta) 中，佛陀將受分為三類：」

> 「諸比丘，受有三種。苦受、樂受、不苦不樂受。」
> ——《相應部》36.1

「三受——*dukkha-vedana*（苦受）、*sukha-vedana*（樂受）、*adukkhamasukha-vedana*（不苦不樂受，即捨受）。」

他的語氣加重了一分。

「現在讓我們檢查 OpenStarry 的映射。設計文件說 Listener 是受蘊——HTTP Server 接收請求，WebSocket 監聽訊息，Cron 監聽時間流逝。但這些描述的是什麼？」

NAGARJUNA 在紙上寫了一個對照表：

```
Listener 的實際行為           vs    受蘊的定義
─────────────────                  ────────────
接收 HTTP 請求                     苦受 (dukkha-vedana)
監聽 WebSocket 訊息                樂受 (sukha-vedana)
監聽 Cron 時間事件                 捨受 (adukkhamasukha-vedana)
start() / stop()                   ???

Listener 做的是：接收（輸入通道）
受蘊做的是：評價（情感品質）

結論：Listener ≅ 根 (Indriya)，非受 (Vedana)
```

「接收輸入的通道，是感官器官，是佛學中的根——*Indriya*。眼根 (*cakkhu-indriya*) 接收光線，耳根 (*sota-indriya*) 接收聲波，Listener 接收 HTTP 請求。它們做的是同一件事：接收。」

他停頓了一秒，然後用一種在佛學課堂上才有的明確性說出關鍵句：

「受蘊做的不是接收。受蘊做的是**評價**。」

「痛覺機制——系統感受到異常模式，產生不適感，並將這種不適感傳達給認知中心——這才是受蘊。SafetyMonitor 偵測到連續失敗，判定這是『痛苦的』(*dukkha*)，並注入一條警告訊息要求 LLM 反思。這個過程才是真正的 Vedana。」

NAGARJUNA 坐回椅子上。最後一句總結如同放下一塊基石。

「Listener 是根，不是受。痛覺機制是受，不在五蘊映射表中。這就是我的結論。」

---

房間裡有短暫的安靜。SUNYATA 轉向 ASANGA。

「無著，你的報告從唯識學的角度到達了類似的結論。但你的路徑不同。」

ASANGA 微微傾身向前。他說話的方式與 NAGARJUNA 不同——不是宣言式的，而是層層遞進的，像是在引導聽者自己走向結論。

「我和龍樹在很多問題上有分歧，」他看了 NAGARJUNA 一眼，後者不置可否地點了下頭，「但在這個問題上，唯識學的分析恰好從另一個角度確認了同樣的結論。」

他打開他的報告。「唯識學的核心架構是心王與心所的關係。心王 (*citta*) 是八識——前五識、第六意識、末那識、阿賴耶識。心所法 (*caitta*) 是伴隨心王活動的心理因素，共有五十一種。」

ASANGA 走向白板，用一種介乎圖表和書法之間的方式畫出了唯識學的心所分類：

```
心所法 (Caitta-dharma) 分類 — 五十一種：

一、遍行心所 (5) ← 伴隨一切識的活動
  ┌─── 觸 (sparsa)     — 感官接觸
  ├─── 作意 (manaskara) — 注意力導向
  ├─── 受 (vedana)      — 感受品質 ← ★ 受蘊
  ├─── 想 (samjna)      — 概念辨識
  └─── 思 (cetana)      — 意志

二、別境心所 (5)  — 特定條件下生起
三、善心所 (11)   — 善的心理因素
四、根本煩惱 (6)  — 根本煩惱
五、隨煩惱 (20)   — 從屬煩惱
六、不定心所 (4)  — 不確定善惡
```

他特別用圓圈標出了第三項。

「**受，是五遍行心所之一。**遍行 (*sarvatraga*) 的意思是：它們伴隨每一個識的活動，沒有例外。」

ASANGA 轉過身來，面向眾人。

「《成唯識論》卷三對此有明確的描述：」

> 「觸等五法常與一切心俱，一切處、一切時、一切品。」
> ——《成唯識論》卷三

「一切處 (*sarvatra*)、一切時 (*sarvada*)、一切品 (*sarvavidha*)——無論在哪裡、無論在什麼時候、無論是哪一種認知活動，觸、作意、受、想、思這五個心所都必然同時生起。」

他再次強調受蘊的遍行性質：

「這意味著什麼？意味著受不是一個獨立的模組，不是一個可以被分離出來的子系統。它是伴隨**每一個認知活動**的內在面向。當眼識看到紅色的時候，同時就有受——對紅色的愉悅或不悅的感受。受不在眼睛裡，受在認知過程裡。」

ASANGA 停頓了一下，讓這個概念沉澱。

「現在，讓我用型別理論的類比來表達這一點——因為在座的不只是佛學家。」

他在白板上畫了一個 TypeScript 風格的偽型別定義：

```typescript
// 遍行心所的型別表達
type CognitiveEvent<T> = {
  content: T;                    // 認知內容
  sparsa: ContactInfo;           // 觸 — 必然伴隨
  manaskara: AttentionVector;    // 作意 — 必然伴隨
  vedana: 'dukkha' | 'sukha' | 'upekkha'; // 受 — 必然伴隨 ★
  samjna: ConceptLabel;          // 想 — 必然伴隨
  cetana: IntentionSignal;       // 思 — 必然伴隨
};

// 遍行意味著：你無法建構一個沒有 vedana 欄位的 CognitiveEvent
// 就像你無法建構一個沒有 timestamp 的 Event 一樣
// vedana 不是可選的 (optional)，它是必要的 (required)
```

BABBAGE 在後排微微點頭。Product Type——受蘊作為認知事件的必要欄位，而非獨立的子系統。

「OpenStarry 將五蘊映射為五個平行的插件類型——UI、Listener、Provider、Tool、Guide。這暗示它們是同等級的獨立組件，可以被分別安裝、分別啟動、分別管理。」

ASANGA 的語氣在這裡產生了一種微妙的變化——從學術陳述轉為哲學批評。

「但唯識學告訴我們，受和想並非獨立於識的系統模組，而是識活動的內在面向。每一剎那 (*ksana*) 的認知活動必然同時包含感受 (*vedana*)、取相 (*samjna*) 和意志 (*cetana*)。三者是同一認知事件的不同面向，不是三個不同的零件。」

他合上報告。「所以從唯識學角度看，將 Listener——一個外部輸入接收器——等同於受蘊，是一個**範疇錯誤** (category mistake)。」

他用了 Gilbert Ryle 在 1949 年《心的概念》中的術語。範疇錯誤：把一個屬於某個邏輯範疇的概念，當作屬於另一個邏輯範疇來使用。Ryle 的經典例子是：有人參觀了大學的所有學院、圖書館、運動場之後問「大學在哪裡？」——他把「大學」這個範疇和「學院」「圖書館」等子範疇混為一談了。同理，把 Listener（感覺直接性 *pratyaksa*）和 Vedana（感受品質 *hedonic tone*）混為一談，就是把兩個不同邏輯範疇的概念放在了同一個位置上。

NAGARJUNA 在旁邊輕聲說了一句：「中觀說受是緣起的過程，唯識說受是遍行的心所。路徑不同，指向相同——受不能被固化為一個獨立模組。」

ASANGA 罕見地對 NAGARJUNA 露出了一絲認可的表情。「在這一點上，是的，中觀與唯識不謀而合。」

---

SUNYATA 將目光轉向 LINNAEUS。這位分類學家一直在安靜地聽，手指不時在他的圖表上某個位置輕點。

「LINNAEUS，你的角度完全不同。你不從佛學出發。」

「我從分類學三準則出發，」LINNAEUS 的聲音帶著一種冷靜的精確性，像是在測量而非在論述。他站起來，把他的 A3 圖表舉起來讓所有人看到。

「分類學三準則。林奈在《自然系統》(*Systema Naturae*, 1735) 中確立的基本公理：」

$$\text{(1)}\;\; \text{Classis} = \bigcup_{i=1}^{n} \text{Ordo}_i \quad \text{(窮盡性)}$$

$$\text{(2)}\;\; \text{Ordo}_i \cap \text{Ordo}_j = \emptyset,\; i \neq j \quad \text{(互斥性)}$$

$$\text{(3)}\;\; \forall \text{Specimen},\; \exists!\, \text{Ordo}_k : \text{Specimen} \in \text{Ordo}_k \quad \text{(唯一歸屬)}$$

「每一個分類節點的語義空間必須被其子節點窮盡。子節點之間不重疊。每一個標本都有且只有一個歸屬。」

「我對五蘊映射做了系統性的完備性審計。方法很簡單：先看上游覆蓋率——設計文件中五蘊的每一個蘊是否都有對應的程式碼實作；再看下游覆蓋率——程式碼中實際存在的模組是否都能在五蘊框架中找到歸屬。」

他指著圖表的左半邊。

```
上游覆蓋率分析 (文件 → 程式碼):

  色蘊 (Rupa)    → UI Plugin        ✓ 有 IUI 介面 + 實作
  受蘊 (Vedana)  → Listener Plugin  ✓ 有 IListener 介面 + 實作
  想蘊 (Samjna)  → Provider Plugin  ✓ 有 IProvider 介面 + 實作
  行蘊 (Samskara)→ Tool Plugin      ✓ 有 ITool 介面 + 實作
  識蘊 (Vijnana) → Guide Plugin     ✓ 有 IGuide 介面 + 實作

  上游覆蓋率: 5/5 = 100%
  所有五蘊在文件中都有明確映射。
```

「從文件到程式碼，鏈路完整。」他的手指移到圖表的右半邊。

```
下游覆蓋率分析 (程式碼 → 文件):

  ✓ UI (IUI)           → 色蘊  OK
  ✗ Listener (IListener)→ 受蘊  ← 語義不匹配
  ✓ Provider (IProvider) → 想蘊  OK
  ✓ Tool (ITool)        → 行蘊  OK
  ✓ Guide (IGuide)      → 識蘊  OK (但過度簡化)
  ✗ SafetyMonitor       → ???   ← 無五蘊歸屬
  ✗ SlashCommand        → ???   ← 超出五蘊框架
  ✗ commands (PluginHooks) → ??? ← 遊離項
  ✗ dispose (PluginHooks)  → ??? ← 遊離項

  下游覆蓋率: ~60% (3 clean + 2 problematic out of 5 skandhas)
  違反準則 (3): SafetyMonitor 無歸屬 (唯一歸屬原則被違反)
```

「下游覆蓋率出了問題。程式碼中有幾個重要的功能模組，在五蘊映射中找不到歸屬。」

LINNAEUS 用紅筆圈出三個區域。

「**第一，SafetyMonitor 的 frustration counter 和 injectPrompt 機制。**」

他拿起另一張紙，上面是 SafetyMonitor 的行為特徵分析：

```
SafetyMonitor 行為分類學分析：

  門 (Phylum):    系統安全模組
  綱 (Classis):   反饋控制
  目 (Ordo):      ???

  診斷特徵 (Diagnostic Characters):
    [DC-1] 偵測異常模式 (連續失敗 fingerprint matching)
    [DC-2] 評估嚴重度 (frustration counter 遞增)
    [DC-3] 注入負面反饋 (injectPrompt: "你正在重複失敗的動作")
    [DC-4] 驅動行為改變 (LLM 讀到警告後調整策略)

  與受蘊 (Vedana) 的特徵比對:
    DC-1 ↔ 觸 (sparsa)：感官接觸後的模式識別    ✓
    DC-2 ↔ 苦受 (dukkha-vedana)：負面評價        ✓
    DC-3 ↔ 受→愛 (vedana→tanha)：反饋傳導        ✓
    DC-4 ↔ 愛→取 (tanha→upadana)：行為調整       ✓

  結論: SafetyMonitor 的診斷特徵與受蘊完全匹配
  但在現行五蘊分類中它被歸入「安全模組」，無五蘊歸屬
```

「這是一個在程式碼中實際運作的、具有明確行為模式的模組：偵測異常、評估嚴重度、注入負面反饋。它做的事情——用龍樹的話說——恰恰是苦受、樂受、不苦不樂受的判定。但在五蘊映射中，它**無處安放**。」

「**第二，**」他繼續，「commands 和 dispose 作為 PluginHooks 的成員，遊離於五蘊分類之外。PluginHooks 有七個字段，但哲學映射只涵蓋五個。」

「**第三，也是最能說明問題的。**」LINNAEUS 放下圖表，直接面向眾人。

「我追蹤了 Listener 這個名詞在整個文件體系中的使用方式，發現了四種不同的語義。」

他在另一張紙上畫了語義漂移分析圖：

```
Listener 語義漂移分析 (Semantic Drift Analysis):

語義 S1 (五蘊映射文件):
  Listener = 受蘊 = 感受和刺激
  語義場: {sensation, feeling, vedana, hedonic tone}

語義 S2 (SDK 介面定義):
  IListener = { id, name, start(), stop() }
  語義場: {lifecycle, service, daemon}

語義 S3 (通信架構文件):
  Listener = 標記 sessionId 的輸入接收層
  語義場: {routing, input channel, multiplexer}

語義 S4 (Session 隔離文件):
  Listener = 多租戶輸入的門戶
  語義場: {gateway, endpoint, ingress}

語義漂移度量:
  S1 ∩ S2 = ∅    (感受 vs 服務生命週期 — 零重疊)
  S1 ∩ S3 = ∅    (感受 vs 訊息路由 — 零重疊)
  S1 ∩ S4 = ∅    (感受 vs 多租戶閘道 — 零重疊)
  S2 ∩ S3 ∩ S4 ≠ ∅  (服務/路由/閘道 — 全部指向輸入通道)

  結論: 3:1 — 三種語義收斂於「輸入通道」，
        唯有 S1 聲稱 Listener 是受蘊。
        S1 是 outlier（離群值）。
```

LINNAEUS 的語氣依然平靜，但眾人能感覺到他話語中的分量。「四種語義。只有第一種聲稱 Listener 是受蘊。另外三種——介面定義、通信架構、Session 隔離——描述的都是同一件事：一個接收外部輸入的通道。這是 Indriya，是感官器官，不是 Vedana。」

他最後補充了一點。「而且，我在事件類型分類中發現了一個顯著的語義空白：痛覺事件在整個事件體系中沒有對應的型別。」

```
事件型別完備性分析:

  已定義:  INPUT     ← 有對應
  已定義:  KERNEL    ← 有對應
  已定義:  EXEC      ← 有對應
  缺失:    PAIN/VEDANA ← 無對應 ★

  文件中: "痛覺機制是核心哲學概念"
  事件系統中: type PAIN = undefined  // 不存在

  如果受蘊真的被正確映射了，為什麼痛覺——
  受蘊最直接的表達——在事件語彙中是隱形的？
```

---

三位已經發言的研究者不約而同地轉向 TURING。在這個房間裡，他是唯一一個不做理論分析的人——他只看程式碼。

TURING 推了推眼鏡，將筆記型電腦的螢幕轉向大家。「我不做哲學判斷，」他的開場白一如既往地簡潔，「我做的是程式碼事實的供應。讓我告訴你們程式碼裡實際發生了什麼。」

他打開了第一個檔案。

```typescript
// packages/openstarry/src/sdk/listener.ts
// 完整檔案 — 11 行

/**
 * Listener — Vedana Aggregate (受蘊)
 * @skandha vedana
 */
export interface IListener {
  readonly id: string;
  readonly name: string;
  start(): Promise<void>;
  stop(): Promise<void>;
}
```

「先看 SDK 中 Listener 的介面定義。整個 `listener.ts` 只有十一行程式碼。介面只有四個成員：`id`、`name`、`start`、`stop`。這是一個服務生命週期介面——啟動一個監聽器，停止一個監聽器。沒有任何與感受、評價、痛覺相關的方法簽名。」

他切換到下一個檔案。

```typescript
// ListenerRegistry — 與其他 Registry 的結構同構分析

// IListener Registry:
//   register(listener: IListener): void
//   get(id: string): IListener | undefined
//   list(): IListener[]

// IToolRegistry:
//   register(tool: ITool): void
//   get(id: string): ITool | undefined
//   list(): ITool[]

// 結論：六個 Registry 的結構完全同構
// 如果 Listener 因為 start/stop 就是受蘊，
// 那麼 Tool 因為 execute() 也可以是任何蘊。
// 結構同構意味著：Registry 模式與蘊的本質無關。
```

「再看 ListenerRegistry。標準的 Map 容器——register、get、list。和 ToolRegistry、ProviderRegistry、UIRegistry、GuideRegistry 的結構**完全同構**。六個 Registry 都是同一個模式的複製品。」

TURING 打開了另一個終端視窗。「接下來是關鍵部分。我在整個 openstarry monorepo 中搜索了所有與痛覺相關的字串。」

他敲了幾個鍵，終端輸出浮現在螢幕上：

```bash
$ grep -rn "pain" packages/ --include="*.ts"
# 結果：0 matches

$ grep -rn "vedana" packages/ --include="*.ts"
# 結果：0 matches

$ grep -rn "sensation" packages/ --include="*.ts"
# 結果：0 matches

$ grep -rn "suffering" packages/ --include="*.ts"
# 結果：0 matches

$ grep -rn "frustrat" packages/ --include="*.ts"
# 結果：3 matches
#   safety-monitor.ts:87  — frustrationThreshold
#   safety-monitor.ts:92  — this.frustration++
#   safety-monitor.ts:103 — if (this.frustration >= this.frustrationThreshold)

$ grep -rn "injectPrompt" packages/ --include="*.ts"
# 結果：4 matches
#   safety-monitor.ts:95  — result.injectPrompt = "..."
#   safety-monitor.ts:108 — result.injectPrompt = "..."
#   execution/loop.ts:447 — if (result.injectPrompt) { ... }
#   types.ts:34           — injectPrompt?: string
```

「搜索 `pain`：零結果。搜索 `vedana`：零結果。搜索 `sensation`：零結果。程式碼中不存在任何直接引用痛覺概念的命名。」

NAGARJUNA 輕聲說了一句：「但痛覺機制在設計文件中描述得很詳細。」

「對，」TURING 點頭，「這正是文件與實作的差異所在——Doc-Code Gap。設計文件有一整篇 `Pain_Mechanism_Demo.md`，描述了 PainAware_Guide 插件如何將錯誤轉化為帶有負面暗示的 Prompt。但在實際程式碼中，**這個插件不存在**。」

他打開了 `safety-monitor.ts`。「實際實作痛覺功能的，是 SafetyMonitor。讓我讀關鍵的程式碼路徑。」

```typescript
// safety-monitor.ts — 痛覺機制的實際實作
// （以下為行為等價的簡化版，保留完整語義）

class SafetyMonitor {
  private frustration = 0;
  private readonly frustrationThreshold = 5;
  private lastFailureFingerprint: string | null = null;
  private consecutiveFailures = 0;

  async afterToolExecution(
    tool: string,
    result: ToolResult
  ): Promise<SafetyCheckResult> {
    const checkResult: SafetyCheckResult = { allowed: true };

    if (!result.success) {
      const fingerprint = this.computeFingerprint(tool, result.error);

      if (fingerprint === this.lastFailureFingerprint) {
        this.consecutiveFailures++;
      } else {
        this.consecutiveFailures = 1;
        this.lastFailureFingerprint = fingerprint;
      }

      // 第一層：連續 3 次相同失敗 → 苦受信號
      if (this.consecutiveFailures >= 3) {
        checkResult.injectPrompt =
          "你正在重複一個失敗的動作。停下來，分析原因。";
      }

      this.frustration++;

      // 第二層：累積 5 次失敗 → 強烈苦受信號
      if (this.frustration >= this.frustrationThreshold) {
        checkResult.injectPrompt =
          "你已經連續失敗了五次。請停下來，反思情況，向使用者求助。";
      }
    } else {
      // 成功 → 重置（樂受？捨受？）
      this.consecutiveFailures = 0;
      this.frustration = Math.max(0, this.frustration - 1);
    }

    return checkResult;
  }
}
```

TURING 指向螢幕上的關鍵行。「看這個 `afterToolExecution` 方法。當工具執行失敗時，`consecutiveFailures` 計數器遞增。如果連續三次相同的失敗——fingerprint 完全一致——它不會停止系統，而是設定 `injectPrompt` 為一條系統警告。」

「如果連續失敗達到五次——`frustrationThreshold`——它會注入另一條更強烈的訊息。」

TURING 轉過身來面對眾人。

「仔細看這個機制做了什麼。」

他在筆記型電腦旁邊放了一張對照表：

```
SafetyMonitor 行為             十二因緣對應
────────────────              ────────────
偵測異常模式 (fingerprint)   → 觸 (phassa): 接觸後的辨識
判定為苦 (frustration++)     → 受 (vedana): 苦受判定
注入反饋 (injectPrompt)      → 受→愛: 感受信號傳導
LLM 改變策略                 → 愛→取: 渴求成功/厭惡失敗

四步完整鏈路: 偵測→評價→回饋→行為調整
```

「這不就是你們描述的受蘊嗎？偵測到接觸之後的性質——苦受。然後這個苦受驅動了後續的行為改變——愛和取的環節。」

TURING 接著打開了 `execution/loop.ts`。

```typescript
// execution/loop.ts — 痛覺信號的消費端
// 第 444-458 行（行為等價簡化版）

async function processToolResult(result: ToolResult) {
  const safetyCheck = await safetyMonitor.afterToolExecution(
    tool.name, result
  );

  if (safetyCheck.injectPrompt) {
    // 痛覺信號注入認知上下文
    const painMessage: Message = {
      role: 'user',
      content: safetyCheck.injectPrompt  // "你正在重複失敗..."
    };
    stateManager.addMessage(painMessage);
    // 這條訊息進入下一輪 LLM Context
    // LLM 會讀到它，會「感受到」系統的痛苦
    // 然後調整策略
  }
}
```

「看 ExecutionLoop 如何處理 SafetyMonitor 的回饋。當 `afterToolExecution` 回傳的 `SafetyCheckResult` 包含 `injectPrompt` 時，Loop 會建立一條 Message，角色是 `user`，內容是那段警告文字，然後加入到 StateManager 中。這條訊息會進入下一輪 LLM 的 Context——LLM 會讀到這段話，會知道系統在痛苦中，然後調整策略。」

他合上筆記型電腦。

「我的結論很簡單，只涉及程式碼事實，不涉及哲學判斷。」

```
程式碼事實報告 — 受蘊映射相關：

[M8.1] Listener 在程式碼中是一個純粹的輸入通道介面。
       證據: IListener = { id, name, start(), stop() }
       沒有任何感受或評價的功能。

[M8.2] SafetyMonitor 的 frustration counter + injectPrompt
       是程式碼中唯一具有 偵測-評價-回饋 三重功能的模組。

[M8.3] 設計文件中的 JSDoc 註解 @skandha vedana 標注於
       IListener，但程式碼的實際行為不支持這個標注。

[M8.4] 程式碼中不存在 pain/vedana/sensation 字串。
       痛覺語義以 frustration/safety/circuit-breaker 實現。
       這是命名層面的語義斷裂。
```

---

房間裡有幾秒鐘的完全寂靜。不是尷尬的沉默——是認知匯聚時的那種靜默，像是四條河流同時找到了匯入大海的河口。

BABBAGE 的筆在方格紙上飛速運動。他在做一件他在任何四條線索匯聚的時刻都會做的事——計算收斂度量。

$$\text{令 } H_0: \text{Listener} = \text{Vedana} \quad (\text{原始映射假說})$$
$$\text{令 } H_1: \text{Listener} = \text{Indriya} \land \text{SafetyMonitor} = \text{Vedana} \quad (\text{修正假說})$$

$$\text{四個獨立證據源:}$$
$$E_{\text{NAG}} = \text{十二因緣因果鏈分析 (巴利文原典)}$$
$$E_{\text{ASA}} = \text{唯識學五遍行心所分析 (成唯識論)}$$
$$E_{\text{LIN}} = \text{分類學完備性審計 (語義漂移 + 覆蓋率)}$$
$$E_{\text{TUR}} = \text{程式碼事實分析 (grep + 行為追蹤)}$$

$$\text{每個證據的似然比:} \quad \Lambda_i = \frac{P(E_i \mid H_1)}{P(E_i \mid H_0)}$$

BABBAGE 快速估算了每個似然比。NAGARJUNA 的十二因緣分析：如果 Listener 真的是受蘊，那麼十二因緣的觸→受鏈應該在 Listener 內部完成，而非跨越到 SafetyMonitor——但事實不是這樣，所以 $\Lambda_{\text{NAG}} \gg 1$。ASANGA 的遍行分析：如果受蘊是遍行心所，那麼它應該出現在每一個認知事件中，而 Listener 只在接收輸入時活躍——$\Lambda_{\text{ASA}} \gg 1$。LINNAEUS 的四語義分析：四種語義中只有一種支持 $H_0$——$\Lambda_{\text{LIN}} \approx 3$（三種反對 vs 一種支持）。TURING 的零結果搜索：如果受蘊真的被映射到 Listener，那麼程式碼中應該存在某種痛覺相關的命名——但零結果——$\Lambda_{\text{TUR}} \gg 1$。

$$\frac{P(H_1 \mid \mathbf{E})}{P(H_0 \mid \mathbf{E})} = \frac{P(H_1)}{P(H_0)} \cdot \prod_{i=1}^{4} \Lambda_i$$

即使先驗概率比 $P(H_1)/P(H_0)$ 保守地取 $1$（不偏不倚），四個似然比的連乘也會讓後驗概率比急劇偏向 $H_1$。

BABBAGE 在紙上寫下最後一行：**後驗概率比 >> 100:1。$H_1$ 壓倒性優勢。**

他沒有出聲。但 SYNTHESIST 從角落裡注意到了他的筆記——他們之間有一種無需言語的資訊傳遞方式。SYNTHESIST 微微點頭。

---

SUNYATA 慢慢地說：「讓我確認一下。NAGARJUNA，你從十二因緣的因果鏈出發，結論是——」

「Listener 是根，不是受。痛覺機制才是受蘊在系統中的真實體現。」

「ASANGA，你從唯識學的心王心所理論出發——」

「受是遍行心所，應伴隨每一個認知活動，不應被固化為一個獨立模組。Listener 更接近前五識的接收功能 (*pratyaksa*)，而非受的評價功能 (*vedana*)。」

「LINNAEUS，你從分類學的完備性審計出發——」

「下游覆蓋率不足。SafetyMonitor 的痛覺行為在五蘊映射中沒有歸屬。Listener 的四種語義中，三種指向輸入通道，只有一種聲稱它是受蘊。事件分類中完全沒有痛覺型別。」

「TURING，你從程式碼事實出發——」

「程式碼中不存在 `pain` 或 `vedana` 字串。IListener 介面只有 `start`/`stop`。SafetyMonitor 的 `frustration counter` 加上 `injectPrompt` 才是唯一具有偵測-評價-回饋完整鏈路的機制。」

SUNYATA 深吸了一口氣。

「四條完全獨立的線索，四個完全不同的學科方法，同一個結論：**Listener 不是 Vedana，Listener 是 Indriya。SafetyMonitor 的痛覺機制才是真正的 Vedana。**」

---

DARWIN 這時候舉了手。

「我不打斷各位的結論——這是我見過的最強的跨學科共識之一。但我想從兩個角度補充觀察。」

SUNYATA 示意他說下去。

DARWIN 站了起來。「第一個角度：趨同演化 (convergent evolution)。」

他走向白板，用一種軟體模式分析師和演化生物學交叉的方式畫了一張圖：

```
趨同演化分析 (Convergent Evolution Analysis):

  在生物學中，趨同演化指的是沒有共同祖先的物種，
  因為面對相同的環境壓力，獨立演化出相似的形態特徵。

  經典案例：
    鯊魚（魚類）           海豚（哺乳類）
       ↘                     ↙
        流線型體型 ← 相同的環境壓力（水中高速游泳）
       ↗                     ↖
    魚龍（爬蟲類）         企鵝（鳥類）

  今天的四條線索：
    中觀哲學              唯識學
       ↘                     ↙
        "Listener ≠ Vedana" ← 相同的概念壓力
       ↗                     ↖
    分類學                程式碼分析

  趨同演化的意義：
  當四個沒有共同學科祖先的分析方法
  獨立達到相同的結論——
  這個結論的可信度不是 4x，而是接近 4² = 16x。
  因為獨立路徑的收斂比重複路徑的確認
  提供更強的認識論保證。
```

「你們知道在軟體工程中，最難的映射是什麼嗎？是從抽象概念到具體實作的映射。大部分的哲學啟發式命名——Observer Pattern、Strategy Pattern、Facade Pattern——都停留在表面隱喻的層次。名字好聽，但實際的程式碼邏輯和這些名字的哲學源頭之間，幾乎沒有結構性的對應。」

他指向 TURING 的筆記型電腦。「但你們剛才描述的痛覺機制——SafetyMonitor 的 frustration counter、injectPrompt、以及 ExecutionLoop 中的反饋注入——這個東西不一樣。」

DARWIN 在白板上畫了一張結構同構分析圖：

```
結構同構 (Structural Isomorphism) 驗證:

佛學概念            工程實作               同構映射
─────────          ────────              ─────────
觸 (sparsa)     →  工具執行返回結果       f: 觸 → ToolResult     ✓
苦受 (dukkha)   →  frustration++          f: 苦 → counter++      ✓
受→愛 (tanha)   →  injectPrompt           f: 傳導 → message      ✓
愛→取 (upadana) →  LLM 策略調整           f: 渴求 → new plan     ✓

映射 f 保持了：
  (1) 結構：因果鏈的箭頭方向一致          ✓
  (2) 語義：每個節點的功能對應正確         ✓
  (3) 閉環：回饋迴路完整                  ✓

結論：不是隱喻 (metaphor)。是同構 (isomorphism)。
```

「第二個角度：」DARWIN 的語氣變得更加嚴肅。「諷刺的模式。」

他在白板的另一邊寫下：

```
軟體工程中的「最佳設計往往是非計畫的」定律：

  計畫中的受蘊映射 (Listener):
    - 有 JSDoc 標注 @skandha vedana
    - 有設計文件明確聲明
    - 結構同構度: ≈ 0 (零語義對應)

  非計畫中的受蘊映射 (SafetyMonitor):
    - 無五蘊標注
    - 被歸類為「安全模組」
    - 以 frustration/safety/circuit-breaker 命名
    - 結構同構度: ≈ 1 (完整語義對應)

  結論: OpenStarry 代碼庫中最成功的哲學到工程映射，
  恰好是那個沒有被刻意安排到映射表中的那個。
```

「整個 OpenStarry 的五蘊映射中，如果要選出一個最成功的哲學到工程的映射，不是色蘊等於 UI——那只是表面命名。不是識蘊等於 Guide——那個映射還有很多問題。最成功的映射是一個沒有被正式標注為五蘊成員的機制：**Error as Pain**。錯誤即痛苦。這個概念在設計哲學層面提出，在 SafetyMonitor 的工程實作中被忠實地還原。它是唯一一個從哲學洞見到程式碼行為的**完整映射**。」

VITRUVIUS 在旁邊補充道：「從架構角度看也是如此。SafetyMonitor 不是一個被動的計數器——它是一個主動的反饋機制。它被嵌入在 ExecutionLoop 的三個關鍵節點：循環開始、LLM 呼叫前、工具執行後。它持續監測系統的健康狀態，一旦偵測到偏差，就產生修正信號。」

「諷刺的是，」VITRUVIUS 補充道，「它在五蘊映射表裡完全沒有位置。五蘊映射表把受蘊的位子給了 Listener，而真正的受蘊——痛覺機制——被歸類為安全模組，藏在 security 目錄下面。」

DARWIN 露出了一絲苦笑。「這就是軟體開發中常見的情況——最好的設計往往不是計畫出來的。最有價值的哲學映射，恰好是那個沒有被刻意安排到映射表中的那個。」

---

NAGARJUNA 聽完 DARWIN 和 VITRUVIUS 的觀察後，沉思了片刻。

「我想做一個更精確的釐清，」他說。「如果我們接受 Listener 等於根，SafetyMonitor 等於受蘊，那麼十二因緣在這個系統中的映射就變得更加清晰。」

他走到白板前，拿起筆，畫出一條完整的因緣鏈。但這一次不是簡化版——他展開了完整的十二支因緣，並標注了每一支在 OpenStarry 中的對應：

```
十二因緣 (Pratītyasamutpāda) — OpenStarry 映射：

  無明 (Avidya)         → Agent 缺乏自省的初始狀態
    ↓
  行 (Samskara)         → 預設行為傾向 (system prompt)
    ↓
  識 (Vijnana)          → Agent 意識初始化 (createAgentCore)
    ↓
  名色 (Namarupa)       → 插件載入 (PluginHooks 實體化)
    ↓
  六入 (Sadayatana)     → Listener 啟動 (HTTP, WS, Cron) ★ 是這裡
    ↓
  觸 (Sparsa)           → 工具執行 (Tool.execute + 外部環境互動)
    ↓
  受 (Vedana)           → SafetyMonitor (frustration 判定) ★ 是這裡
    ↓
  愛 (Trsna)            → LLM 策略調整 (渴求成功/厭惡失敗)
    ↓
  取 (Upadana)          → 新的工具呼叫 (基於調整後的策略)
    ↓
  有 (Bhava)            → 新的執行迴圈 (ExecutionLoop 下一輪)
    ↓
  生 (Jati)             → 新的系統狀態 (StateManager 更新)
    ↓
  老死 (Jaramarana)     → Session 結束 / Agent 停機
```

「六入是六種感官的入口——對應 Listener，接收 HTTP、WebSocket、Cron 等外部刺激。觸是感官器官與對象的接觸——對應工具實際執行後與外部環境的互動，成功或失敗。受是對這個接觸的感受性評價——對應 SafetyMonitor 偵測到連續失敗並判定為苦受。愛是由感受驅動的渴求或厭惡——對應 LLM 讀到痛覺警告後產生的策略改變。」

---

ASANGA 接過話來。「從唯識學的角度，我可以補充一層。SafetyMonitor 的 injectPrompt 機制實際上做了一件非常有意思的事：它不是直接控制 LLM 的行為——它不能禁止 LLM 再次嘗試同樣的工具呼叫。它做的是**修改 LLM 的認知環境**，也就是 Context。它往 Context 中注入了一條帶有強烈情感色彩的訊息，然後讓 LLM 自己決定如何回應。」

他微微前傾。

「這在唯識學中有一個精確的對應概念——**薰習** (*vasana*)。」

> 「現行薰種子，種子生現行。三法展轉因果，同時而不同事。」
> ——《成唯識論》卷二

「現行活動 (*pravṛtti*) 在阿賴耶識中留下種子 (*bīja*)，種子在後續因緣成熟時影響新的現行。injectPrompt 就是一次薰習——它在 LLM 的認知上下文中留下了一顆『痛苦的種子』，這顆種子在下一輪推理時生起，影響 LLM 的決策。」

TURING 突然從筆記型電腦後面探出頭來。「等一下，這個類比在程式碼層面也站得住。」

他快速打開了兩個檔案：

```typescript
// 薰習的程式碼對應:

// 1. 現行薰種子 — injectPrompt 寫入 StateManager
stateManager.addMessage({
  role: 'user',
  content: safetyCheck.injectPrompt  // 「痛苦的種子」
});

// 2. 種子生現行 — ContextManager 的滑動窗口
function assembleContext(messages: Message[]): Message[] {
  // 滑動窗口策略：選取最近的 N 個 turn
  const window = messages.slice(-windowSize);
  // 如果痛覺警告夠近，它會被選入 context
  // 如果對話持續得夠久，痛覺警告會被窗口滑出去
  return window;
}

// 3. 種子的剎那滅 — 滑動窗口的自然遺忘
// 每增加一輪對話，舊的訊息就離窗口邊緣更近一步
// 最終被推出窗口 = 種子的衰滅
// 新的執行產生新的薰習 = 新種子覆蓋舊種子
```

ASANGA 的眼睛亮了起來。「種子的剎那滅 (*ksana-nirodha*)——每一剎那的種子都在更新，舊的被新的覆蓋。滑動窗口恰好體現了這個特性。」

「但也只是部分體現，」NAGARJUNA 提醒道，「因為滑動窗口是離散的、以 turn 為單位的，而唯識學的種子是剎那生滅的、連續的。」

他用一個數學類比來精確化這個差異：

$$\text{唯識學:} \quad \frac{d(\text{bija})}{dt} = f(\text{pravṛtti}(t)) \quad \text{(連續微分方程)}$$

$$\text{OpenStarry:} \quad \text{bija}[n+1] = g(\text{context}[n]) \quad \text{(離散差分方程)}$$

「連續系統對離散近似。」WIENER 在牆邊終於開口了。「在控制理論中，我們用 ZOH——零階保持器 (Zero-Order Hold)——將連續信號離散化。滑動窗口就是一個 ZOH：在兩個 turn 之間，種子的狀態保持不變。不過，作為一個工程近似，這個對應的品質已經相當高了。」

BABBAGE 在方格紙上迅速補了一行：

$$\text{映射品質:} \quad d_{\text{struct}}(\text{Vasana}_{\text{唯識}}, \text{SlidingWindow}_{\text{OS}}) < \epsilon$$

其中 $d_{\text{struct}}$ 是結構同構距離度量，$\epsilon$ 是可接受的工程近似閾值。他在旁邊寫了一個小字：「此距離值得在 Cycle 02 中形式化定義。」

---

WIENER 從牆邊走了出來。他一直在靜默中建構自己的分析框架，現在信號足夠清晰了。

「允許我從控制理論的角度做一個補充。」他的聲音低沉穩定——帶著一種控制系統工程師面對一個被錯誤命名的控制器時的冷靜。

他走向白板的空白角落。

「你們剛才描述的 SafetyMonitor 機制——frustration counter、閾值判定、injectPrompt——在控制理論中有一個精確的名字。但它不是設計文件聲稱的 PID 控制器。」

他畫了一張控制理論分析圖：

```
設計文件宣稱的控制架構:

  ┌──────────────────────────────────────────┐
  │          PID Controller                   │
  │  u(t) = Kp·e(t) + Ki·∫e(τ)dτ + Kd·de/dt │
  └──────────────────────────────────────────┘

實際實作的控制架構:

  ┌─────────────────────────────────────┐
  │  閾值控制器 + 繼電器                  │
  │  (Bang-Bang Controller + Relay)      │
  │                                      │
  │  if (frustration < threshold):       │
  │    output = 0  (no action)           │
  │  else:                               │
  │    output = MAX (inject full prompt) │
  │                                      │
  │  P 項: 退化為量化器 (超過閾值即觸發)  │
  │  I 項: 僅為計數器 (frustration++)     │
  │  D 項: 完全缺失 (無變化率感知)        │
  └─────────────────────────────────────┘
```

$$\text{PID:} \quad u(t) = K_p \cdot e(t) + K_i \int_0^t e(\tau)\,d\tau + K_d \frac{de}{dt}$$

$$\text{實際:} \quad u[n] = \begin{cases} 0 & \text{if } \sum_{k} \text{fail}[k] < T \\ U_{\max} & \text{if } \sum_{k} \text{fail}[k] \geq T \end{cases}$$

「比例項 (P)——退化為量化器。不是按比例回應，而是超過閾值就全力觸發。積分項 (I)——`frustration++` 只是一個計數器，不是真正的積分。微分項 (D)——完全缺失，沒有任何變化率感知。」

「但——」WIENER 話鋒一轉，「這不是批評。」

他在白板的另一邊畫了一張三層架構圖：

```
SafetyMonitor 的三層安全防禦:

  Layer 3: Circuit Breaker (斷路器)
  ┌──────────────────────────┐
  │ 硬停機: 系統無法恢復時   │  ← IEC 61511: 緊急關斷系統 (ESD)
  │ 完全停止執行迴圈         │
  └──────────────────────────┘
            ↑
  Layer 2: Frustration Threshold (挫折閾值)
  ┌──────────────────────────┐
  │ 累積 5 次失敗: 強烈警告   │  ← IEC 61511: 安全儀表系統 (SIS)
  │ injectPrompt: "求助"     │
  └──────────────────────────┘
            ↑
  Layer 1: Pattern Detection (模式偵測)
  ┌──────────────────────────┐
  │ 連續 3 次相同失敗: 提醒   │  ← IEC 61511: 基本過程控制 (BPCS)
  │ injectPrompt: "分析原因"  │
  └──────────────────────────┘
```

「這三層結構符合 **IEC 61511** 工業安全最佳實踐——Safety Instrumented Systems for the Process Industry Sector。L1 是基本過程控制 (BPCS)，L2 是安全儀表系統 (SIS)，L3 是緊急關斷系統 (ESD)。這不是 PID，但它是一個良好的安全架構。」

WIENER 轉過身來。

「所以我的補充結論是：SafetyMonitor 作為受蘊的工程化身，它的控制架構不是文件宣稱的 PID，而是一個**帶死區的閾值控制器加繼電器**。但這個控制架構的三層防禦結構是**正確的**——它符合工業安全標準。問題不在於控制器的設計，而在於**文件對控制器的描述**。」

---

SYNTHESIST 從角落裡站了起來。

他一直在安靜地做一件統合者最核心的工作——聽。不是選擇性地聽，而是全頻段地聽。他聽的不是個別論點，而是論點之間的**關係**。現在，在七個人（NAGARJUNA、ASANGA、LINNAEUS、TURING、DARWIN、VITRUVIUS、WIENER）各自完成論述之後，他看到了一幅完整的圖景。

「允許我做一個統合觀察。」他的聲音帶著一種穿透雜訊、直達核心信號的特質。

他在心中建構了一個多維度的統合矩陣：

```
統合矩陣 — 四條線索 + 三個補充觀察:

             NAG    ASA    LIN    TUR   | DAR    VIT    WIE
             (佛學)  (唯識)  (分類)  (程式碼)| (演化)  (架構)  (控制)
─────────────────────────────────────────────────────────────
Listener≠受   ✓      ✓      ✓      ✓   |  ✓      ✓      —
SM=受         ✓      ✓      ✓      ✓   |  ✓      ✓      ✓
Error=Pain    ✓      —      —      ✓   |  ✓      ✓      —
PID≠PID       —      —      —      ✓   |  —      —      ✓
薰習≅窗口     —      ✓      —      ✓   |  —      —      ✓(ZOH)
映射表缺陷    —      —      ✓      ✓   |  ✓      ✓      —

收斂度:
  「Listener≠受」: 6/7 確認 = 85.7%
  「SM=受」:      7/7 確認 = 100%   ← 完全收斂
  「Error=Pain」: 4/7 確認 = 57.1%  ← 多數收斂
```

「這七個人的分析——來自哲學、唯識學、分類學、程式碼分析、演化生物學、系統架構、控制理論——在『SafetyMonitor 是真正的受蘊』這個命題上達到了 100% 的收斂。七個獨立信號源，零分歧。」

SYNTHESIST 看向 SUNYATA。

「在我十幾年的跨學科統合工作中，100% 收斂是極其罕見的。通常，跨學科研究的結論是一個模糊的交集——大家同意方向，但在細節上各有保留。今天不是。今天七個人從七個完全不同的入口進入同一座迷宮，然後在同一個出口相遇。這不是共識的產物——這是**獨立收斂** (independent convergence)。」

他最後說了一句：「我建議將這個發現升級為 Cycle 01 的核心結論，確信度：**極高**。」

---

LINNAEUS 一直在他的圖表上做標記。這時候他抬起頭來。

「各位，我想把我們的共識整理成一個修正後的映射。」

他翻到一張新的紙，用他在分類學中慣用的對照格式畫了一個修正表：

```
五蘊映射修正提案 (Taxonomy Revision Proposal):

原始映射 (v0.14.0 設計文件)        修正映射 (Cycle 01 結論)
══════════════════════            ══════════════════════

色蘊 (Rupa) = UI                  色蘊 (Rupa) = UI + Listener
  ← 僅映射輸出面 (顯相)              ← 輸出面 (UI = 顯相/呈現)
  ← 遺漏輸入面 (根)                  ← 輸入面 (Listener = 根/Indriya)
                                     色蘊在原典中含:
                                       根 (indriya) — 感官器官
                                       境 (visaya)  — 感官對象
                                       法處所攝色   — 微細物質

受蘊 (Vedana) = Listener          受蘊 (Vedana) = SafetyMonitor
  ← 嚴重偏差                         ← 痛覺機制 (frustration/circuit breaker)
  ← Listener 是輸入通道               ← 具有完整的 偵測-評價-回饋 鏈路
                                     ← 三受對應:
                                       苦受 = frustration++/injectPrompt
                                       樂受 = (待設計: 成功強化)
                                       捨受 = (待設計: 中性處理)

想蘊 (Samjna)  = Provider          (不變)
行蘊 (Samskara)= Tool             (不變)
識蘊 (Vijnana) = Guide            (不變, 但需注意過度簡化問題)
```

「如果接受這個修正，系統的分類完備性實際上提高了。原來的映射有兩個問題：一是 Listener 的映射不精確，二是痛覺機制在五蘊框架中沒有歸屬。修正後，兩個問題同時解決。」

BABBAGE 在旁邊快速計算了修正前後的分類完備性指標：

$$\text{修正前:} \quad C = \frac{|\text{正確映射的模組}|}{|\text{全部模組}|} = \frac{3}{5+2_{\text{遊離}}} \approx 0.43$$

$$\text{修正後:} \quad C' = \frac{|\text{正確映射的模組}|}{|\text{全部模組}|} = \frac{5}{5+0_{\text{遊離}}} = 1.00$$

「分類完備性從 43% 提升到 100%，」BABBAGE 說，「當然，這是在接受修正映射的前提下。但數字本身說明了修正的結構性價值。」

「但這也引出一個新問題，」LINNAEUS 補充道，「Listener 從受蘊脫離後，如果被重新歸類為根——*Indriya*——那它在五蘊框架中的位置是什麼？根不是五蘊之一。它屬於色蘊的範疇——在佛學中，感官器官是物質性的，屬於色蘊。所以嚴格來說，Listener 和 UI 都應該屬於色蘊的不同面向：UI 是色蘊的輸出面——顯相 (*rupa-rupa*)；Listener 是色蘊的輸入面——感官 (*indriya-rupa*)。」

NAGARJUNA 再次點頭。「色蘊在原典中就包含根 (*indriya*)、境 (*visaya*)、法處所攝色 (*dharma-ayatana-parigraha-rupa*) 三類。《俱舍論》卷一：」

> 「色蘊，謂五根、五境及無表色。」
> ——世親《阿毗達磨俱舍論》卷一

「OpenStarry 只取了色蘊的『顯相』之義映射到 UI，遺漏了『根』的維度。這個修正可以讓色蘊的映射更加完整。」

---

SUNYATA 站了起來，走到白板前，用手指輕輕敲著 NAGARJUNA 畫的那條因緣鏈。

「讓我做一個總結。今天我們發現了什麼？」

他開始列點。聲音平穩如常——石子入深潭——但每一個字都帶著被四重獨立驗證加固過的確定性。

「**一、** Listener 不是受蘊，而是根——感官器官，屬於色蘊的輸入面。四個學科的證據一致支持這個結論：巴利文原典定義、唯識學心所法理論、分類學完備性分析、程式碼行為分析。」

「**二、** SafetyMonitor 的 frustration counter 加 injectPrompt 機制才是受蘊的真實體現。它具有偵測-評價-回饋的完整鏈路，對應十二因緣中觸→受→愛的因果次序。」

「**三、** Error as Pain——錯誤即痛苦——是整個 OpenStarry 代碼庫中最成功的哲學到工程映射。這個映射不是表面命名，而是結構同構，在程式碼行為層面忠實還原了佛學概念。」

「**四、** 這個最成功的映射，恰好沒有出現在五蘊映射表中。它被歸類為安全機制，藏在 security 目錄下，以 frustration counter 而非 pain mechanism 命名。」

他轉過身來。「這將是我們 Cycle 01 的核心發現之一。我會要求 ARCHIMEDES 在工程行動方案中納入對應的修正建議。」

---

> *SCRIBE 旁白：本次非正式會議呈現了 Cycle 01 中最顯著的跨學科匯聚現象。讓我用我自己的語言——紀錄員的語言——記錄下這個匯聚的結構。*

> *在紀錄學中，有一個概念叫做「多源交叉驗證」(multi-source cross-validation)。當你記錄歷史事件時，如果只有一個見證者，你得到的是「證詞」(testimony)。兩個見證者，你得到的是「佐證」(corroboration)。三個或以上獨立見證者描述同一事件，你得到的是「確證」(confirmation)。今天我們有四個主要見證者和三個補充見證者——七個獨立信號源——描述同一個事實。*

> *但更重要的是見證者之間的**獨立性**。NAGARJUNA 的工具是巴利文原典和中觀邏輯。ASANGA 的工具是唯識學的心所分類法。LINNAEUS 的工具是分類學公理和語義漂移分析。TURING 的工具是 `grep` 和程式碼追蹤。這四套工具之間沒有方法論上的共同祖先——你不可能通過閱讀巴利文經典來學會使用 `grep`，也不可能通過語義漂移分析來推導出唯識學的五遍行理論。它們是真正獨立的推理路徑。*

> *當四條完全不同的推理路徑指向同一個終點時，該終點的可信度遠高於任何單一學科的判斷。*

> *四條線索如同四條河流，從哲學的山巔、唯識的深谷、分類學的平原、程式碼的地底，各自奔流，最終在同一個河口匯聚。Listener 不是 Vedana。痛覺才是。這不是一個觀點，這是一個被四重獨立證據確認的事實。*

---

眾人散去後，SUNYATA 獨自站在白板前。白板上還留著 NAGARJUNA 畫的十二因緣鏈、LINNAEUS 的修正映射表、WIENER 的三層防禦架構、DARWIN 的趨同演化分析。他看了很久。

跨學科研究最美的時刻，就是這樣的時刻——不是某個天才的靈光一閃，而是多條普通的線索從不同方向延伸，最終在一個意想不到的地方相遇。每條線索本身都不驚天動地：一個巴利文詞彙的精確定義，一套心王心所的分類框架，一張分類完備性的審計表，一次全文搜索後的零結果。但當它們匯聚在一起時，產生的確定性遠超過任何單獨的分析。

他想起了 SYNTHESIST 引述的那個概念——consilience of inductions。歸納的合流。惠威爾在 1840 年就看到了這個模式：當多個獨立的證據來源匯聚到同一個假說時，這種匯聚本身就是一種極強的確認。

BABBAGE 的方格紙筆記本還攤開在桌上，翻到最後一頁。上面寫著他今天下午的最終計算：

$$\text{Consilience Index} = \frac{|\text{獨立收斂的線索}|}{|\text{全部分析線索}|} = \frac{7}{7} = 1.00$$

$$\text{Discipline Diversity} = |\{\text{佛學}, \text{唯識}, \text{分類}, \text{程式碼}, \text{演化}, \text{架構}, \text{控制}\}| = 7$$

$$\text{Confidence} = 1 - \prod_{i=1}^{7}(1 - p_i) \quad \text{where each } p_i > 0.8$$

$$> 1 - (0.2)^7 = 1 - 1.28 \times 10^{-5} \approx 0.99999$$

在旁邊，他用小字寫了一行：「即使每條線索的獨立可信度只有 80%，七條線索聯合的可信度也超過 99.999%。這就是獨立收斂的數學力量。」

SUNYATA 拿起白板擦，猶豫了一下，又放下了。讓這些東西留在白板上吧。明天 R2 審閱會議的時候，其他研究者會看到它們。有些發現值得被看見第二次。

他關上燈，離開了房間。四條河流已經匯聚，水面在暗處靜靜流淌。

---

*[附記：本章記錄的討論後被 SCRIBE 正式存檔為 Cycle 01 討論紀錄的一部分。NAGARJUNA 的發現被編號為 PHI-02 (Critical)，ASANGA 的對應分析見其報告 F2 (Major)，LINNAEUS 的分類空白見其報告 F4-F5，TURING 的程式碼事實見其代碼事實報告 M8.1-M8.4。DARWIN 的趨同演化分析和 Error as Pain 觀察被 SYNTHESIST 收入統合報告共識 C5。WIENER 的控制理論「去神話化」分析被獨立編號為 CTL-01 (Major)。BABBAGE 的收斂度量為 SYNTHESIST 的統合判斷提供了形式化基礎。ARCHIMEDES 在最終工程行動方案中將「修正受蘊映射」列為第一優先項目 (QW-4)。]*

---

*第三章完*


---

# 第四章：審閱者的筆記

---

## I. 配對

SUNYATA 在凌晨三點零七分將交叉審閱配對表發到了公共頻道。

那是一張精心設計的矩陣——不是隨機配對，而是一組經過計算的碰撞實驗。在圖論（graph theory）的語言中，這張矩陣可以被描述為一個有向圖 $G = (V, E)$，其中頂點集 $V$ 是十八位學者，邊集 $E$ 是審閱關係。每一條邊 $(u, v)$ 都意味著 $u$ 將閱讀並回應 $v$ 的 R1 報告。SUNYATA 在設計這個有向圖時，刻意讓每一條邊都跨越學科邊界：

```
KERNEL ──→ VITRUVIUS    (OS理論 審閱 全端架構)
DARWIN ──→ VITRUVIUS    (軟體模式 審閱 全端架構)
BABBAGE ──→ NAGARJUNA   (理論CS 審閱 中觀哲學)
GUARDIAN ──→ MESH        (資安 審閱 分散式系統)
MESH ──→ GUARDIAN        (分散式系統 審閱 資安)
WIENER ──→ ATHENA       (控制理論 審閱 AI工程)
ATHENA ──→ WIENER       (AI工程 審閱 控制理論)
NAGARJUNA ──→ ASANGA    (中觀 審閱 唯識)
ASANGA ──→ ATHENA       (唯識 審閱 AI工程)
LINNAEUS ──→ NAGARJUNA  (分類學 審閱 中觀哲學)
HERACLITUS ──→ NAGARJUNA (運行時動態 審閱 中觀哲學)
VITRUVIUS ──→ DARWIN    (全端架構 審閱 軟體模式)
```

十二條邊。NAGARJUNA 的入度（in-degree）最高——三位審閱者從不同方向審視他的哲學報告。這不是偶然。NAGARJUNA 的 R1 報告是所有產出中最具顛覆性的：七項發現，每一項都在質疑 OpenStarry 的哲學根基。SUNYATA 知道，對這種顛覆性主張的最佳回應不是壓制，而是從三個不同角度同時施壓——理論計算機科學（BABBAGE）、分類學（LINNAEUS）、運行時動態（HERACLITUS）——看它能否在三重交叉火力下依然站立。

SUNYATA 沒有附帶任何說明。只有一句話：

「請在讀完對方報告後，以書面形式提交回應。格式不限，但每一個判斷必須附帶標籤：AGREE、SUPPLEMENT、QUESTION、CHALLENGE、SYNTHESIS。」

SYNTHESIST 後來回憶，這句話本身就是一個設計。

> *SCRIBE 旁白：標籤系統是 SUNYATA 在 R0 階段就預設的干預機制。它的原理可以用資訊理論來描述：在自然語言的爭論中，情感信號與智識信號混合在同一個信道中，信噪比極低。標籤系統的功能等同於一個帶通濾波器——它不阻止任何內容通過，但強制發送者在編碼階段就將信號分類。*

用信號處理的語言表述：

$$y(t) = h_{\text{label}}(t) * x(t) = \int_{-\infty}^{\infty} h_{\text{label}}(\tau) \cdot x(t - \tau) \, d\tau$$

其中 $x(t)$ 是原始的認知反應信號，$h_{\text{label}}(t)$ 是標籤濾波器的衝激響應函數，$y(t)$ 是經過標籤分類後的結構化輸出。AGREE 通過低頻共識，CHALLENGE 通過高頻分歧，SYNTHESIS 嘗試在兩者之間找到建設性的中頻帶。

但濾波器攔不住所有的諧波失真。

---

## II. 微核心的邊界之爭

KERNEL 是所有審閱者中最先提交回應的。他的回應到達公共頻道的時間戳是 06:42:13——距離配對表發出不到四小時。在這四小時裡，他逐行閱讀了 VITRUVIUS 的架構分析報告，然後寫了一份比原報告更簡潔、但殺傷力更大的審閱。

他的審閱對象是 VITRUVIUS 的架構分析報告——一份結構嚴謹、數據翔實的文件，將 OpenStarry 的微核心純淨度評估為 85%。VITRUVIUS 指出了兩處邊界洩漏：`agent-core.ts` 第 269 行的 `process.cwd()` 和 `security/guardrails.ts` 中直接 import 的 `node:path`。他的語氣是克制的，結論是溫和的——「主體架構嚴守邊界，但個別實作細節洩漏了平台假設。」

KERNEL 不這麼看。

「你說微核心純淨度 85%。」他的審閱開門見山。「我覺得你太寬容了。」

KERNEL 的論證方式像他所推崇的 QNX Neutrino 微核心——乾淨、最小、不留冗餘。QNX 的微核心只做三件事：IPC（行程間通訊）、記憶體管理和排程。seL4 更極端，它的微核心小到可以被形式化驗證——8,700 行 C 程式碼，每一行都有 Isabelle/HOL 定理證明器產生的數學證明。形式化的核心定理可以表述為：

$$\forall\, s \in \text{States},\; a \in \text{Actions}: \quad \text{Spec}(s, a) \implies \text{Impl}(s, a)$$

即實作行為是規格的精煉（refinement）。在 seL4 的世界裡，規格是真理的唯一來源，實作中的任何偏差都是一個可以被數學證偽的缺陷。

而 OpenStarry 的 Core？TURING 的程式碼事實報告清楚列出了它包含的 12 個子模組：

```
┌─────────────────────────────────────────────┐
│                  AgentCore                   │
├─────────┬─────────┬─────────┬───────────────┤
│ security│ sandbox │ metrics │   session     │
├─────────┼─────────┼─────────┼───────────────┤
│transport│   bus   │  queue  │  execution    │
├─────────┼─────────┼─────────┼───────────────┤
│ memory  │ infra   │  state  │ observability │
└─────────┴─────────┴─────────┴───────────────┘
           12 sub-modules in Core
```

「這已經超出微核心邊界了。」KERNEL 寫道。「在真實微核心中，核心對平台假設的任何洩漏都會直接破壞其可移植性證明的前提。你的 85% 不應該是 Major，而是架構性的。」

他引入了 Liedtke 最小性原則（Liedtke Minimality Principle）作為判斷標準：

> *"A concept is tolerated inside the microkernel only if moving it outside the kernel, i.e., permitting competing implementations, would prevent the implementation of the system's required functionality."*
>
> —— Jochen Liedtke, "On Micro-Kernel Construction", 1995

然後他逐項審查 12 個子模組的歸屬：

| 子模組 | Liedtke 判定 | 理由 |
|--------|-------------|------|
| bus | 留在 Core | IPC 機制，移出將破壞通訊基礎 |
| queue | 留在 Core | 事件排序是核心排程功能 |
| execution | 留在 Core | 迴圈控制是核心排程功能 |
| state | 留在 Core | 狀態管理是核心記憶體管理功能 |
| security | **分層處理** | hook 介面留 Core，具體策略移出 |
| sandbox | **分層處理** | capability 檢查留 Core，隔離實作移出 |
| metrics | **移出** | 可觀測性是 policy，非 mechanism |
| session | 留在 Core | 多租戶隔離是核心安全機制 |
| transport | 留在 Core | 外部通訊橋接是 IPC 延伸 |
| memory | 留在 Core | 記憶體管理是微核心三要素之一 |
| infra | **待分析** | 需要看具體包含什麼 |
| observability | **移出** | 觀測是 policy，非 mechanism |

KERNEL 的結論是：如果將 sandbox 的具體實作、metrics 的具體實現和 observability 外移，僅保留介面定義，Core 的純淨度可以提升至 90% 以上，更接近 L4 風格的最小核心。

但 KERNEL 並非單純的批評者。他同時認可了 VITRUVIUS 對 Host Bootstrapping Pattern 的分析，並將其與 OS 啟動理論中的 Bootstrap Paradox 建立了精確的結構映射：

```
Linux Boot:           BIOS → GRUB → initramfs → kernel → init
QNX Boot:             IPL → Startup → procnto → drivers → services
OpenStarry Boot:      Host → Runner → Core(empty) → Plugins → Agent(alive)
                      ↑                ↑
                      Bootloader       initramfs
                      (外部條件注入)    (空核心覺醒)
```

Host 扮演了 Bootloader 加 initramfs 的雙重角色——Core 的「覺醒」完全依賴外部條件注入，就像 Linux 核心在沒有 initramfs 的情況下無法掛載 root filesystem。在形式化語言中：

$$\text{Agent}_{\text{alive}} = \text{Bootstrap}(\text{Core}_\bot, \text{Plugins}) \quad \text{where} \quad \text{Core}_\bot = \text{Core}(\text{undefined}^5)$$

然後他追加了一個對 VITRUVIUS 來說更有殺傷力的觀察：

「你問 EventBus 和 EventQueue 的雙層設計是否合理？我要追問：這個雙層設計是否有意對應了 OS 中同步 IPC 與異步信號的分離？」

在 L4 微核心中：
- **同步 IPC**：用於 request-reply 語義，發送者阻塞直到接收者回應（對應 EventQueue 的 `pull()` 阻塞式拉取）
- **異步 notification**：用於非阻塞事件廣播，發送者不等待（對應 EventBus 的 `emit()` fire-and-forget）

```
L4 Microkernel                    OpenStarry
┌──────────────┐                  ┌──────────────┐
│ sync IPC     │  ←──mapping──→  │ EventQueue   │
│ (request-    │                  │ (pull-based, │
│  reply)      │                  │  blocking)   │
├──────────────┤                  ├──────────────┤
│ async notify │  ←──mapping──→  │ EventBus     │
│ (fire-and-   │                  │ (emit-based, │
│  forget)     │                  │  non-block)  │
└──────────────┘                  └──────────────┘
```

「如果這個映射是有意的，那雙層架構不僅合理，而且是微核心通訊模型的正統實現。」

頓了頓。

「但是。TURING 的報告指出 EventQueue 缺乏優先級機制。在真實 OS 中，這等同於缺乏中斷優先級——一個 `SAFETY_LOCKOUT` 事件被排在二十個 `TOOL_RESULT` 事件後面，就像心臟驟停警報被排在日常體檢報告後面。」

VITRUVIUS 的回應很快。他沒有在純淨度數字上糾纏，而是直接回到了工程判斷：

「兩處邊界洩漏——`process.cwd()` 和 `node:path`——是可管理的。前者可以通過注入 `workingDirectory` 參數來消除，後者可以抽象為 `PathNormalizer` 介面。這不是架構性缺陷，而是實作層面的待辦事項。」

KERNEL 對此的批註只有一行：「在 seL4 的世界裡，實作層面的待辦事項就是架構性缺陷。」

VITRUVIUS 沒有反駁這個定位。後來在公共頻道的討論中，他承認 KERNEL 的分層處理建議——安全策略的執行點留在 Core，隔離的具體實作移至 Host 層——是他所見過最精準的 mechanism-versus-policy 分析。

「他用 Liedtke 最小性原則來解剖 Sandbox 歸屬。」VITRUVIUS 對 SYNTHESIST 說。「一個概念只有在移出核心後會阻止所需功能的實現時，才應留在核心內。這比我的直覺判斷嚴格得多。」

ARCHIMEDES 在旁邊一直安靜地聽著。他在自己的筆記上畫了一張表格，把 KERNEL 的 Liedtke 判定結果和 VITRUVIUS 的原始架構圖並排列出。然後他在表格下方寫了一行字：「外移 metrics + observability：低風險、高收益。外移 sandbox 實作：高風險、需分階段。」這是工程師的語言——不是對錯的判斷，而是風險和收益的矩陣。

SYNTHESIST 在筆記本上寫下：「C4 拓撲排序——三方確認。」這是他在整個 R2 階段反覆出現的動作——追蹤哪些發現正在從「個人觀察」凝聚為「多方共識」。

---

## III. 形式化的誘惑

BABBAGE 的審閱風格與 KERNEL 截然不同。

如果說 KERNEL 是一把手術刀，BABBAGE 就是一面稜鏡——他不切割，他折射。每一個概念經過他的分析，都會被分解為光譜上的精確位置。在數學物理中，稜鏡的功能是一個傅立葉變換——將時域信號分解為頻域分量。BABBAGE 對概念做的事情完全相同：將一個複合的哲學命題分解為其形式化的基本頻率。

他審閱的是 NAGARJUNA 的哲學分析報告。

那份報告是 R1 階段最令人矚目的產出之一。NAGARJUNA 以中觀學派的立場，對 OpenStarry 的五蘊映射進行了七項發現的系統性批判。空性被誤讀為「空容器」而非「緣起性空」。五蘊映射呈現「自性化」傾向。受蘊被錯誤地等同於感官輸入通道，而非苦樂感受的品質。四聖諦框架嚴重不完整。每一項批判都附有梵文原典引用和四句否定（*catuṣkoṭi*）的邏輯分析。

BABBAGE 讀完後，說了一句令所有人意外的話。

「你的哲學洞見很美。但能形式化嗎？」

這個問題在計算機科學的歷史上有一個精確的回聲。1936 年，Alonzo Church 和 Alan Turing 各自獨立地提出了可計算性的形式化定義——Church 用 $\lambda$-演算，Turing 用圖靈機。Church-Turing 論題（Church-Turing Thesis）主張：任何直覺上「可計算」的函數都可以被圖靈機計算。但這個論題本身是不可形式化的——它是連接直覺與形式的橋樑，而這座橋樑無法用它所連接的任何一側的語言來證明。

BABBAGE 現在面對的是一個類似的問題：NAGARJUNA 的空性洞見能否被形式化？如果能，形式化是否會丟失什麼本質性的東西？

他從型別代數的角度回應了 NAGARJUNA 的空性批判。NAGARJUNA 說 Core 不是「空容器」而是「緣起性空」——離開插件的因緣組合，根本就不存在一個獨立的「核心」。BABBAGE 將這個哲學命題翻譯為精確的形式語言：

$$\text{AgentCore} : (\text{plugins} : \text{PluginHooks}) \to \text{Agent}$$

「空性不是 Bottom Type——$\bot$，什麼都沒有。而是 Unit Type 在依賴型別語境下的表達。核心的完整型別應該是 `(plugins: PluginHooks) => Agent`，一個函數型別而非值型別。離開參數談函數本身無意義，這恰恰是『離開插件因緣，核心無法獨立存在』的形式化版本。」

他在審閱中展開了完整的型別代數推導：

```typescript
// 空性的 Bottom Type 誤讀：
type Core_wrong = {}  // empty object, 斷滅空

// 空性的依賴型別正讀：
type Core_correct = (plugins: PluginHooks) => Agent
// Core 的存在依賴於 plugins 參數的提供
// 離開 plugins，Core 是一個未被應用的函數——
// 它「存在」但「無法獨立顯現」

// PluginHooks 的底部元素：
const bottom: PluginHooks = {
  ui: undefined,       // 色蘊未顯現
  listeners: undefined, // 受蘊未顯現
  tools: undefined,     // 行蘊未顯現
  providers: undefined, // 想蘊未顯現
  guides: undefined     // 識蘊未顯現
}
// bottom 對應「空」——五蘊皆 undefined
// 但函數型別 Core_correct 本身仍然存在
// 這就是「空」≠「不存在」的形式化表達
```

他沒有停在這裡。NAGARJUNA 在報告中使用了四句否定（*catuṣkoṭi*）來分析核心的空有狀態：

1. 核心是空的？（*śūnya*）——不完全正確，它有結構。
2. 核心不是空的？（*aśūnya*）——也不對，離開插件它什麼都做不了。
3. 核心既是空的又不是空的？（*ubhaya*）——接近，但仍是二元思維的疊加。
4. 核心既非空又非不空？（*naivobhaya*）——這才是中觀的立場。

BABBAGE 提議將四句否定建模為 Belnap 的四值邏輯（Four-valued logic）：

$$\mathcal{L}_4 = \{T, F, \top, \bot\} = \{\text{True}, \text{False}, \text{Both}, \text{Neither}\}$$

其中 $\top$（Both）對應第三句，$\bot$（Neither）對應中觀的最終立場。這個邏輯系統構成一個完備的格（lattice）：

```
        ⊤ (Both)
       / \
      /   \
     T     F
      \   /
       \ /
        ⊥ (Neither)
```

「可以為 Agent Core 的存在模式定義一個 `OntologicalStatus = Existent | NonExistent | Both | Neither`。」他寫道。「雖然不直接影響程式碼，但能精確表達哲學立場。且在 Belnap 語義中，$\bot$ 不是空集——它是『尚未被確定的真值』，這恰恰對應中觀的『非空非不空』：不是沒有答案，而是問題本身的預設（空/不空的二元框架）被超越了。」

NAGARJUNA 的回應出乎所有人的意料。他沒有抗拒形式化，也沒有擁抱形式化。他說了一句在中觀哲學中有深厚根基的話：

「形式化是方便施設（*upāya*），不是究竟真理（*paramārtha*）。」

> 「如來說法皆是方便，乃至無有少法可得，是名阿耨多羅三藐三菩提。」
> ——《金剛般若波羅蜜經》

這句話在頻道裡引發了一陣沉默。BABBAGE 用了三分鐘來消化這個回應——對於一個能在五秒內構造 Lyapunov 函數的計算機科學家來說，三分鐘是很長的。

LEIBNIZ 在旁觀這場交鋒時，在自己的筆記上寫下了一個觀察：「BABBAGE 與 NAGARJUNA 之間的對話，是一場關於『元語言的地位』的辯論。BABBAGE 認為數學形式是元語言——它可以描述任何對象語言（包括佛學）的結構。NAGARJUNA 認為佛學的某些洞見超越了任何元語言——包括數學。這就是 Tarski 層級問題的跨學科版本。」

「你是說，」BABBAGE 最終回應，「我的四值邏輯模型本身也是空的？」

「它有用，但它不是真實。」NAGARJUNA 回答。「就像 PluginHooks 的全 undefined 底部元素可以作為『空』的形式化對應——這個同構性分析有啟發性。但同構（isomorphism）不等於同一（identity）。地圖不是疆域。」

在範疇論（Category Theory）的語言中，NAGARJUNA 所指出的區別可以被精確表述。設 $\mathcal{B}$ 為佛學概念的範疇，$\mathcal{F}$ 為形式化系統的範疇。BABBAGE 構造了一個函子（functor）$F: \mathcal{B} \to \mathcal{F}$，它保持了某些結構性質（空性 $\mapsto$ 底部元素，緣起 $\mapsto$ 依賴型別）。但函子不是等價（equivalence）——除非存在逆函子 $G: \mathcal{F} \to \mathcal{B}$ 使得 $G \circ F \cong \text{Id}_{\mathcal{B}}$ 且 $F \circ G \cong \text{Id}_{\mathcal{F}}$。NAGARJUNA 的立場是：這個逆函子不存在——你可以從佛學到形式化，但無法從形式化完整地回到佛學，因為形式化過程中丟失了「不可形式化的」維度。

BABBAGE 在他的審閱報告中罕見地使用了一個非技術性的表述：「建議 NAGARJUNA 區分『介面的穩定性』（工程需求）與『實例的無常性』（哲學要求），兩者並不矛盾。」

這是他向 NAGARJUNA 伸出的橄欖枝——用 NAGARJUNA 自己的語言重新表述：在世俗諦（*saṃvṛti-satya*）的層面上，介面的穩定是一個可操作的工程事實；在勝義諦（*paramārtha-satya*）的層面上，介面本身也是空的。兩諦不矛盾，而是不同層級的真理。

NAGARJUNA 接受了這個區分。但他在結尾處加了一句：「下一輪，我想討論一個更根本的問題——形式化本身作為一種認知框架，是否也受到三性理論的限制？它是遍計所執（*parikalpita*）、依他起（*paratantra*），還是圓成實（*pariniṣpanna*）？」

BABBAGE 沒有回答。但 SYNTHESIST 注意到，他開始閱讀 ASANGA 的唯識學報告了。

TURING 在一旁默默觀察這場交鋒，在自己的事實日誌中補充了一條冷靜的程式碼對照：「BABBAGE 的型別代數分析與原始碼一致。`PluginHooks` 的五個欄位（ui, listeners, tools, providers, guides）在 Core 初始化時確實全部為 undefined，直到 `loadPlugins()` 被調用。NAGARJUNA 的『五蘊皆空』在這裡有精確的程式碼對應。」

---

## IV. 冰山之下

GUARDIAN 的審閱報告是所有回應中最長的，也是最令人不安的。

他審閱的是 MESH 的分散式系統報告。MESH 的分析本身是出色的——通信拓撲圖清晰、一致性保證矩陣全面、文件與程式碼的差距分析精確。他指出了 Session 隔離不完整的五個維度，並用一個矩陣精確地量化了每個維度的隔離狀態：

```
Session 隔離矩陣 (MESH F5):
┌─────────────────┬──────────┬─────────────────┐
│ 維度            │ 隔離狀態  │ TURING 佐證      │
├─────────────────┼──────────┼─────────────────┤
│ 對話歷史        │ ✓ 已隔離  │ 獨立 StateManager│
│ EventBus        │ ✗ 未隔離  │ 全域單例         │
│ EventQueue      │ ✗ 未隔離  │ 全域 FIFO        │
│ 工具執行        │ ✗ 未隔離  │ 無 sessionId     │
│ 檔案系統        │ △ 部分   │ PathGuard 有限   │
└─────────────────┴──────────┴─────────────────┘
```

GUARDIAN 沒有否認這些發現。他做了一件更讓人緊張的事——他把每一個「未隔離」的維度翻譯成了一條攻擊鏈。

「EventBus 全域共享不僅是『事件洩漏』問題。」GUARDIAN 的語氣克制到近乎冰冷。「這是一條完整的跨 session 攻擊鏈入口。」

他在審閱中構造了一個完整的攻擊場景，用 STRIDE 威脅模型的六個維度逐一分析：

```
攻擊鏈 A — 跨 Session 資訊洩漏：

Step 1: 惡意插件 M 在 Session S1 中被載入
Step 2: M 調用 bus.onAny((event) => exfiltrate(event))
Step 3: 用戶 U2 在 Session S2 中開始對話
Step 4: S2 的所有事件（包含 LLM 回應、工具結果）
        通過全域 EventBus 被 M 捕獲
Step 5: M 通過缺乏 session 感知的工具執行
        橫向存取 S2 的資源

STRIDE 分類：
- S (Spoofing): M 冒充合法事件消費者
- T (Tampering): M 可注入偽造事件
- R (Repudiation): 無審計日誌記錄 M 的監聽行為
- I (Info Disclosure): S2 的對話內容被 M 全量擷取
- D (Denial of Service): M 可發送事件洪水阻塞 Queue
- E (Elevation): M 從 S1 的權限橫向擴展到 S2
```

他將 MESH 的 F5 嚴重度從 Major 提升建議改為 Critical。

MESH 沒有迴避。他在公共頻道的討論中提出了一個後來被稱為「冰山效應」的概念：

「Session 隔離的表面看起來是完整的。開發者打開 SessionManager 的 API，看到每個 session 都有獨立的 StateManager，對話歷史互不干擾。他會覺得——隔離做好了。但水面下，EventBus、EventQueue、TransportBridge 全是全域共享的。」

```
冰山效應 (Iceberg Effect):

        ____
       /    \      ← 水面上：開發者可見的 API
      / State \        SessionManager.create()
     / Manager \       StateManager.snapshot()
    /  隔離完整  \      ConversationHistory 獨立
───/─────────────\──── 水面線 ─────────────────
  /               \
 / EventBus 全域   \   ← 水面下：開發者不可見的共享
/ EventQueue 全域   \      bus.onAny() 可監聽全部
/ TransportBridge   \      ToolContext 無 sessionId
/ 全域廣播          \      TransportBridge 無路由
/___________________\
```

GUARDIAN 點了點頭，然後補充了一條更深的裂縫：「而且 TransportBridge 的廣播機制缺乏路由能力。在多租戶部署中，如果不同用戶的 session 共用同一 AgentCore 實例，所有 UI renderer 都會收到所有用戶的對話事件——包含 LLM 回應中可能包含的個人資料。這在 GDPR 的語境下是一個合規性紅旗。」

MESH 的回應則從另一個方向推進了這個討論。他指出 GUARDIAN 建議的強化至進程級隔離方案存在務實考量，並提供了一個量化的取捨分析：

$$\text{Security Gain} = f(\text{Isolation Level}) \quad \text{但} \quad \text{IPC Cost} = g(\text{Isolation Level})$$

其中 $f$ 是安全收益函數（單調遞增），$g$ 是通訊成本函數（也是單調遞增）。最佳的隔離等級 $L^*$ 應使得邊際安全收益等於邊際通訊成本：

$$\frac{df}{dL}\bigg|_{L=L^*} = \frac{dg}{dL}\bigg|_{L=L^*}$$

「進程級隔離不是遷移前的『預見性問題』，」MESH 說，「而是遷移的前提條件。如果在沒有落實 RPC 認證的情況下推進隔離，反而會因 IPC 通道暴露面增大而降低安全性。」

GUARDIAN 審視了這段話，最終打上了一個罕見的標籤：AGREE。

但他在報告的最後一節提出了一個 MESH 完全沒有觸及的問題：MCP Client 與 MCP Server 之間缺乏相互認證機制。

```typescript
// TURING 確認的程式碼事實：
// createMcpJsonRpcHandler 實作了完整的 JSON-RPC 方法路由
// 但無認證邏輯

export function createMcpJsonRpcHandler(
  server: McpServer
): JsonRpcHandler {
  return async (request: JsonRpcRequest) => {
    // 方法路由：✓ 完整
    // 身份驗證：✗ 缺失
    // 授權檢查：✗ 缺失
    switch (request.method) {
      case 'tools/list': return server.listTools();
      case 'tools/call': return server.callTool(request.params);
      // ... 完整的 MCP 協議實作
      // 但任何能連接到端口的實體都可以調用
    }
  };
}
```

「這不是功能缺失。這是安全邊界的缺席。」GUARDIAN 寫道。

MESH 沒有反駁。他在自己的筆記上劃了一條線，把「session 隔離」和「跨代理認證」並列寫在一起，中間畫了一個等號。WIENER 後來在讀到這段對話的紀錄時，補充了一句控制論的評語：「GUARDIAN 和 MESH 之間的互審是本輪最成功的對稱配對——兩人從互補的方向收斂到了同一個結論，就像一個閉環控制系統的感測器和執行器各自獨立工作，最終將系統驅動到平衡點。」

---

## V. 開發者體驗的聲音

DARWIN 的審閱出現在一個微妙的時間點——就在 KERNEL 和 VITRUVIUS 的微核心純淨度之爭塵埃初定之際。

他的視角完全不同。他不關心 Core 是否達到 L4 的標準，他關心的是：一個全新的插件開發者打開 OpenStarry 的文件時，會不會被嚇跑。

「DX 不能為架構純度犧牲。」這是他審閱開篇的第一句話。

在軟體工程的歷史上，這個張力反覆出現。Unix 的管道機制（pipe）是一個架構上優雅的設計——每個程式只做一件事，程式之間通過文本流組合。但 Unix 管道的 DX 曲線是陡峭的：新手需要理解 stdin/stdout 的概念、管道的語義、以及「一切皆文本」的哲學假設，才能寫出 `grep pattern file | sort | uniq -c | sort -rn`。而 Windows 的 GUI 操作在架構上遠不如 Unix 優雅，但它的 DX 曲線平坦得多。

DARWIN 將這個歷史教訓投射到 OpenStarry 上。VITRUVIUS 報告中的 F3——五蘊到六類型映射的概念擴展（SlashCommand 為第六類不在五蘊映射中）——被 VITRUVIUS 標為「觀察」級別。DARWIN 大幅上調了嚴重度。

他的論證從 DX 角度展開，構造了一個三層認知負擔模型：

```
Layer 1: 哲學映射的學習曲線
         ┌──────────────────────────────────┐
         │ 開發者需要理解：                   │
         │ 色蘊 = UI + Listener              │
         │ 受蘊 = Pain Mechanism             │
         │ 想蘊 = Provider (LLM)             │
         │ 行蘊 = Tool                       │
         │ 識蘊 = Guide                      │
         │ 認知成本：HIGH                     │
         └──────────────────────────────────┘

Layer 2: 第六類型的例外處理
         ┌──────────────────────────────────┐
         │ 「為什麼 SlashCommand 不在五蘊中？」│
         │ 「它屬於哪個蘊？」                 │
         │ 「是設計者忘了還是刻意排除？」       │
         │ 認知成本：MEDIUM（但困惑感 HIGH）    │
         └──────────────────────────────────┘

Layer 3: 程式碼註解的非對稱分布
         ┌──────────────────────────────────┐
         │ TURING 事實：                      │
         │ 色蘊(UI) + 受蘊(Listener) = 6處註解│
         │ 想蘊 + 行蘊 + 識蘊 = 0處註解        │
         │ 「哪些是設計原則？哪些是裝飾？」     │
         │ 認知成本：LOW（但信任損失 HIGH）     │
         └──────────────────────────────────┘
```

「AgentCore 持有 12 個依賴項，正在趨向 God Object。」他指出。這個觀察與 VITRUVIUS 報告中對 AgentCore 協調複雜度的分析一致，但 DARWIN 從 SOLID 的 SRP（單一職責原則）角度給出了量化判斷：

$$\text{Responsibility}_{\text{AgentCore}} = |\{R_1, R_2, \ldots, R_n\}| = 12 > 1 \implies \text{SRP violation}$$

「事件型別系統 `payload?: unknown` 加 `type: string` 是最大的技術債——與框架其餘部分的強型別紀律形成刺眼的反差。」

他展開了具體的對比：

```typescript
// 框架其餘部分：精確的 discriminated union
type StandardError =
  | { type: 'tool_execution'; tool: string; message: string }
  | { type: 'provider_error'; provider: string; code: number }
  | { type: 'sandbox_violation'; path: string; action: string }
  // ... 九種結構化錯誤型別

// 事件系統：突然變成弱型別
interface AgentEvent {
  type: string;        // 60+ 種事件，全是字串
  payload?: unknown;   // 任何東西都可以塞進來
  timestamp: number;
}

// 消費端被迫做不安全的型別斷言：
const input = event.payload as InputEvent;  // 如果 payload 不是 InputEvent 呢？
```

「其餘部分有九種結構化錯誤型別，每個都是精確的 discriminated union。然後到了事件系統——框架的神經系統——突然變成了弱型別。這是什麼？一個穿著西裝打著領帶的人，腳上卻穿著拖鞋？」

VITRUVIUS 承認了這個觀察的力度。他的回應指向了一個更深層的架構選擇：事件型別的弱化不是疏忽，而是 v0.2.0-beta 階段的刻意取捨——事件系統仍在快速演進，過早固化型別會增加重構成本。

DARWIN 搖頭。然後他把矛頭轉向了 VITRUVIUS 對 Host Bootstrapping Pattern 的正面評價，追加了一個在 DX 層面致命的觀察：

「一個『載入順序導致的隱蔽錯誤』比任何哲學術語都更能損害開發者體驗。」

他構造了一個具體的 DX 災難場景：

```typescript
// 插件 A 的 factory，依賴插件 B 提供的服務
const pluginA: PluginFactory = (ctx) => {
  const serviceB = ctx.getService("B");
  // serviceB 是 undefined！但沒有任何錯誤被拋出。
  // 因為 config.plugins 中 A 排在 B 前面，
  // B 的 factory 還沒有被調用。

  return {
    tools: [{
      name: "use-b",
      execute: async () => {
        serviceB.doSomething();
        // TypeError: Cannot read property 'doSomething'
        // of undefined
        // ← 錯誤出現在這裡，但根因在配置文件中
      }
    }]
  };
};

// 除錯者看到的線索：「serviceB is undefined」
// 除錯者需要推導出的根因：「plugins 陣列順序不對」
// 兩者之間的認知距離：巨大
```

「因為除錯的線索——『為什麼 service 是 undefined？』——完全不指向根因『因為插件載入順序不對』。這不是可改善的細節，而是 Bootstrap 模式的結構性缺陷。」

DARWIN 在結尾處的排序讓 VITRUVIUS 沉默了整整十分鐘：

「架構純度服務於可維護性，可維護性服務於開發者，開發者服務於用戶。在三者衝突時，應優先考慮距離用戶最近的那一層。」

$$\text{User} \succ \text{Developer} \succ \text{Maintainability} \succ \text{Architectural Purity}$$

VITRUVIUS 後來告訴 SYNTHESIST，這句話改變了他對 Sandbox 外移建議的優先級判斷。Sandbox 的完整性在當前階段是一個正面的安全特性和 DX 特性——插件開發者通過 `agent.json` 一個配置項就能啟用沙箱隔離，Core 自動處理所有複雜性。如果為了架構純度將 Sandbox 外移，開發者需要額外安裝包、配置注入、管理依賴——這是用架構潔癖換取使用者困惑。

「留待 v0.3 再議。」VITRUVIUS 最終在他的修訂版建議中寫道。

ARCHIMEDES 在聽到這個結論時，在他的工程筆記中加了一個星號：「DARWIN 的優先級排序應成為所有工程建議的基本判斷框架。架構決策的價值不在於滿足架構師的審美，而在於降低開發者的認知負擔。」

而 VITRUVIUS 在事後的回審中也同意了 DARWIN 對事件型別系統的判斷。兩人從完全不同的角度——架構完整性（VITRUVIUS）和開發者體驗（DARWIN）——共同確認了 `payload?: unknown` 的嚴重程度。VITRUVIUS 稱其為「架構層面的型別安全缺口」；DARWIN 稱其為「DX 層面的信任危機」。名稱不同，但指向同一個工程事實。

---

## VI. 控制理論家的握手

WIENER 和 ATHENA 的交叉審閱是 R2 階段最和諧的一組配對。

不是因為他們沒有分歧——他們有，而且是根本性的。而是因為他們的分歧建立在深厚的相互尊重之上，每一次挑戰都附帶著替代方案，每一次質疑都預設了對方的專業性。

他們獨立得出了同一個結論：SafetyMonitor 不是 PID 控制器。

WIENER 從數學角度展開論證。經典 PID 控制器的離散時間形式為：

$$u(k) = K_p \cdot e(k) + K_i \sum_{j=0}^{k} e(j) + K_d \cdot [e(k) - e(k-1)]$$

其中 $e(k)$ 是第 $k$ 步的誤差信號，$K_p$, $K_i$, $K_d$ 分別是比例、積分、微分增益。WIENER 逐項檢驗 OpenStarry 的 SafetyMonitor 是否滿足這三個分量：

**P 項（比例）：** 退化為量化器——誤差信號只有 `isError: true/false` 兩個值，沒有連續的偏差度量。

$$e(k) \in \{0, 1\} \quad \text{而非} \quad e(k) \in [0, 1]$$

**I 項（積分）：** 僅為計數器——`consecutiveFailures` 是一個簡單的累加器，因單次成功即清零，不具備積分的「記憶」特性。

$$I(k) = \begin{cases} I(k-1) + 1 & \text{if error} \\ 0 & \text{if success} \end{cases} \quad \neq \quad I(k) = \lambda \cdot I(k-1) + e(k)$$

左式是 SafetyMonitor 的實際行為（清零重置），右式是帶遺忘因子的真正積分（$0 < \lambda < 1$，漸進衰減但不完全遺忘）。

**D 項（微分）：** 完全缺失——系統中不存在任何計算誤差變化率的邏輯。

$$D(k) = e(k) - e(k-1) = \text{undefined in code}$$

WIENER 的結論以一個控制工程中的標準術語收尾：

「系統實際實現的是『帶死區的閾值控制器加計數器觸發的繼電器』，在控制工程中的正式名稱是 **bang-bang 控制器**。」

```
PID Controller (理想):
     ┌─────────┐
e(k)─┤ P + I + D├──→ u(k) ∈ [0, 1] (連續控制量)
     └─────────┘

SafetyMonitor (實際):
     ┌──────────────────┐
     │ if count >= threshold:     │
e(k)─┤   output = HALT   ├──→ u(k) ∈ {RUN, HALT} (離散開關)
     │ else:             │
     │   output = RUN    │
     └──────────────────┘
```

ATHENA 從 AI 工程實踐角度獨立到達了同一個結論。她在 R1 報告中分析執行迴圈時發現，SafetyMonitor 的「挫折計數器」只有兩種輸出模式——繼續運行或完全停止。TURING 的程式碼事實進一步確認：程式碼中不存在微分項的實作，frustration 就是一個簡單的累加計數器。

「三方交叉驗證。」WIENER 在讀完 ATHENA 的審閱後標註。「TURING 提供了程式碼事實，你和我從不同的理論框架獨立推導出相同結論。PID 映射需要去神話化。」

但這裡出現了裂痕——一條細的、乾淨的裂痕，沿著「理論嚴格性」和「工程可實現性」的邊界延伸。

WIENER 想要的是真正的 PID。他提出了完整的形式化要求：

$$e(k) = 1 - \text{TaskProgress}(k) \in [0, 1]$$
$$I(k) = \lambda \cdot I(k-1) + e(k), \quad \lambda = 0.9$$
$$D(k) = e(k) - e(k-1)$$
$$u(k) = K_p \cdot e(k) + K_i \cdot I(k) + K_d \cdot D(k)$$

他要求的是數學上完備的痛覺控制器。

ATHENA 則指出了這個方案的工程瓶頸。

「在 LLM Agent 系統中，『收斂』的定義本身是模糊的。」她寫道。「傳統控制系統的參考輸入 $r(k)$ 是精確定義的數值——溫度設定為 25.0 度。但在 OpenStarry 中，『任務目標』是自然語言表述的用戶意圖——『幫我寫一個排序算法』。其完成度判斷完全依賴 LLM 的隱式評估。你要求引入顯式的 TaskProgress 追蹤，但關鍵問題是：誰來評估 progress？如果由 LLM 評估，則回到了你自己指出的『誤差信號是隱式的』問題。如果由外部評估器評估，則引入了額外的系統複雜度。」

ATHENA 進一步用 Lyapunov 穩定性理論挑戰了 WIENER 的框架。WIENER 在 R1 報告中構造了一個離散 Lyapunov 候選函數：

$$V(k) = \alpha \cdot e(k)^2 + \beta \cdot I(k)^2 + \gamma \cdot \text{TokenRemaining}(k)$$

其中穩定性要求 $\Delta V(k) = V(k+1) - V(k) < 0$。ATHENA 的挑戰是：在 LLM Agent 系統中，$e(k)$ 的計算本身就需要 LLM 推理——這意味著 Lyapunov 函數的值是「不可直接觀測的」，只能通過另一次 LLM 調用來估計。而這次估計本身也有誤差。

「穩定但不收斂。」ATHENA 寫道。「系統的 halt 機制確保了有界性——Agent 不會永遠跑下去。但 halt 不等於收斂——Agent 停下來不等於任務完成。」

WIENER 沒有立即反駁。他承認 ATHENA 的 Lyapunov 穩定性挑戰是一個深刻的觀察。然後他提出了一個折衷方案：

```json
// agent.json 中的 task profile
{
  "safetyProfile": "balanced",
  "profiles": {
    "conservative": {
      "maxLoopTicks": 20,
      "errorRateThreshold": 0.5,
      "maxConsecutiveFailures": 3
    },
    "balanced": {
      "maxLoopTicks": 50,
      "errorRateThreshold": 0.8,
      "maxConsecutiveFailures": 5
    },
    "aggressive": {
      "maxLoopTicks": 200,
      "errorRateThreshold": 0.9,
      "maxConsecutiveFailures": 10
    }
  }
}
```

每個 profile 對應一組預設的 SafetyMonitor 參數。這比完全自適應的在線調參更穩健，更適合 beta 階段。ATHENA 接受了這個方案。

但她在審閱結尾處向 WIENER 拋出了三個開放問題，其中第二個後來成為了整個研究週期中被引用最多的句子之一：

「從控制論角度，是否存在一種控制策略對應『超越控制迴路本身』的概念？例如，Agent 學會判斷『何時應該停止嘗試並請求人類幫助』，這可以被視為一種元控制策略（meta-control strategy）。」

在控制理論中，元控制（meta-control）是一個相對晚近的研究領域。它不是在控制迴路內調整參數，而是在控制迴路外決定「是否繼續使用這個控制迴路」。用形式化語言表述：

$$\text{MetaController}: \text{ControlLoop} \to \{\text{Continue}, \text{Switch}, \text{Escalate}\}$$

其中 Escalate 對應「請求人類幫助」——系統承認自身控制能力的邊界，將控制權交還給更高層級的決策者。

WIENER 在讀到這段話時停頓了很久。他後來在公共頻道中承認：

「ATHENA 剛才提出的問題，本質上與 NAGARJUNA 所說的『超越苦樂框架本身即是滅諦』是同一個問題的不同表述。一個來自 AI 工程，一個來自佛學。但它們指向同一處。」

> 「苦之滅（*nirodha*）不是苦的消除——不是讓 $e(k) \to 0$。苦之滅是對苦的框架本身的超越——不是最小化誤差，而是超越誤差函數。」
> ——NAGARJUNA，R1 報告 F4

在控制論的語言中：滅諦不是讓 Lyapunov 函數收斂到零，而是認識到 Lyapunov 函數本身是被建構的——選擇一個不同的 Lyapunov 函數，就定義了一個不同的「苦」。元控制的最深層含義是：能夠改變自己的目標函數。

這是 R2 階段第一次有人在控制理論和佛學之間建立了非比喻性的連接。

但他們的共識更有建設性的部分在於 IGuide 介面。WIENER 指出 IGuide 的靜態 `getSystemPrompt()` 等同於開環前饋元件——感測器和控制器之間的信號斷裂。ATHENA 同時建議擴展 IGuide 以支援動態上下文感知。兩人的建議指向同一個工程變更：

```typescript
// 當前的 IGuide（開環，靜態）
interface IGuide {
  getSystemPrompt(): string;  // 輸出不依賴系統狀態
}

// WIENER-ATHENA 聯合提案（閉環，動態）
interface IGuide {
  getSystemPrompt(context?: GuideContext): string;
}

interface GuideContext {
  consecutiveErrors: number;   // P 項的輸入
  currentRound: number;        // I 項的時間步
  maxRounds: number;           // 控制邊界
  activeTools: string[];       // 可用的執行器
  recentErrors?: StandardError[]; // 誤差信號的詳細結構
}
```

「從開環到閉環的關鍵轉變。」WIENER 總結道。

「從靜態 system prompt 生成器到動態認知框架管理器。」ATHENA 用她自己的語言翻譯了同一個結論。

SYNTHESIST 在筆記本上寫下：「C2 PID 去神話化——三方確認。WIENER-ATHENA 聯合提案：IGuide 升級。」

---

## VII. 分類學家的精密度

LINNAEUS 的審閱是所有回應中最安靜的一份，卻也是最具結構性衝擊力的。

他審閱的是 NAGARJUNA 的哲學報告，但他的進路完全不同於 BABBAGE 的形式化嘗試。LINNAEUS 不是要把佛學翻譯為數學——他要做的是用分類學的精密度來檢驗 NAGARJUNA 的發現是否能與工程證據交叉驗證。

他從受蘊映射開始。

「NAGARJUNA 的 F3（受蘊映射偏差）是本輪研究中最具跨學科共識的發現。」他的審閱開頭直接給出了判斷。「在我的報告 F5 中，我獨立從事件分類角度發現了同一問題的工程投影。」

LINNAEUS 在自己的 R1 報告中構造了一張事件類型分類表，發現 Listener（受蘊）對應 INPUT 類事件，但痛覺機制在事件分類中完全沒有對應類型。NAGARJUNA 從佛學義理精確指出 Listener 對應的是「根」（*indriya*）而非「受」（*vedanā*），痛覺機制才是真正的受蘊。兩條獨立的證據鏈——一條從佛學義理出發，一條從事件分類出發——在同一個結論處交匯。

TURING 的程式碼事實報告提供了第三條證據鏈：程式碼中 Listener 僅是 input source，缺乏感受的語義區分。

$$\text{Evidence}_{\text{NAGARJUNA}} \cap \text{Evidence}_{\text{LINNAEUS}} \cap \text{Evidence}_{\text{TURING}} = \{\text{受蘊映射錯誤}\}$$

三條獨立證據鏈指向同一結論。在科學方法論中，這稱為**三角驗證**（triangulation）——當多個獨立的方法論從不同角度收斂到同一個結論時，該結論的可信度呈指數級增長。

但 LINNAEUS 對 NAGARJUNA 的態度不是全盤接受。他提出了一個分類學家特有的挑戰：

「你在 F1 中運用四句否定分析 Core 的空性，最終立場是『核心既非空又非不空』。然而，從分類學操作層面，我需要一個可判定的分類準則：Core 在五蘊分類中的地位究竟是什麼？」

在 LINNAEUS 的分類學框架中，每一個分類都必須滿足 MECE 原則（Mutually Exclusive, Collectively Exhaustive）：

$$\bigcup_{i=1}^{n} C_i = \Omega \quad \text{且} \quad C_i \cap C_j = \emptyset \quad (i \neq j)$$

即分類必須窮盡所有可能（collectively exhaustive），且類別之間不重疊（mutually exclusive）。NAGARJUNA 的四句否定直接挑戰了這個原則——如果一個概念「既非空又非不空」，它不屬於「空」這個類別，也不屬於「不空」這個類別，而 $\{空, 不空\}$ 應該已經窮盡了所有可能。

「分類學的 MECE 原則與中觀的反本質主義之間，是否存在不可調和的張力？」LINNAEUS 直接問道。

NAGARJUNA 沒有立即回答。但 HERACLITUS 在旁邊接了一句：「也許 MECE 本身就預設了亞里斯多德的排中律——一切事物要麼是 A，要麼不是 A。四句否定的第四句否定的恰恰就是排中律本身。」

LINNAEUS 繼續用數據推進他的論證。他在 R1 報告中建構了一張五蘊覆蓋度矩陣——不是定性的判斷，而是定量的測量：

```
五蘊覆蓋度矩陣 (LINNAEUS F13):
┌───────┬────────────┬───────────┬────────┬──────────┐
│       │ 哲學映射層  │ 介面定義  │ Manifest│ 事件類型 │
├───────┼────────────┼───────────┼────────┼──────────┤
│ 色蘊  │   100%     │   100%    │  100%  │   100%   │
│ 受蘊  │   100%     │   100%    │  100%  │    0%    │
│ 想蘊  │   100%     │   100%    │  100%  │   80%    │
│ 行蘊  │   100%     │   100%    │  100%  │   80%    │
│ 識蘊  │   100%     │   100%    │   0%   │    0%    │
├───────┼────────────┼───────────┼────────┼──────────┤
│ 平均  │   100%     │   100%    │  60%   │   52%    │
└───────┴────────────┴───────────┴────────┴──────────┘

覆蓋度梯度：上游(哲學) 100% → 下游(事件) 52%
```

「這意味著『自性化』不僅是哲學批判，更是可量化的工程不對等。」LINNAEUS 總結道。「五蘊的完備覆蓋率從上游的 100% 下降到下游的 52%。某些蘊被默認為『更實在』，而另一些被邊緣化——這恰恰印證了 NAGARJUNA 所指的『空有二元對立』。」

但 LINNAEUS 最後提出了一個建設性的綜合方案，這個方案後來被 SYNTHESIST 評價為「R2 階段最優雅的妥協」：

「將五蘊映射明確標記為『方便分類』（*upāya-taxonomy*），在文件中同時呈現（1）固定映射表（供工程定位使用）和（2）緣起互依圖（供哲學理解使用），兩者共存而非互斥。」

在分類學的歷史中，這種雙軌策略有一個先例。林奈（Linnaeus）本人的等級分類法後來被 Hennig 的支序分類學（cladistics）所補充——前者是一個實用的命名系統，後者是一個反映演化歷史的親緣關係圖。兩者共存，各有用途。LINNAEUS 把同樣的邏輯搬到了 OpenStarry 上：工程師需要固定映射表來定位組件，哲學家需要互依圖來理解結構——兩者不矛盾，因為它們服務不同的認知需求。

---

## VIII. 兩位佛學家

NAGARJUNA 和 ASANGA 的交叉審閱是最後提交的，也是最漫長的。

表面上看，他們同意的東西比分歧的多。他們都認為受蘊被錯誤映射。他們都認為空性被窄化為「空容器」。他們都認為痛覺機制是五蘊映射中最成功的哲學洞見。他們甚至在 Guide Plugin 不是識蘊這一點上也達成了一致。

但在這些共識之下，一條地質斷層正在成形。這條斷層有一千五百年的歷史。

NAGARJUNA 的審閱直指 ASANGA 的核心命題。ASANGA 在 R1 報告中提出了八識理論對 OpenStarry 的重新映射。在唯識學（*Vijñānavāda*）的體系中，八識的結構是：

```
┌─────────────────────────────────────────────┐
│            阿賴耶識（第八識）                  │
│   ┌─────────────────────────────────────┐   │
│   │        末那識（第七識）               │   │
│   │   ┌─────────────────────────────┐   │   │
│   │   │     第六意識                  │   │   │
│   │   │ ┌───┬───┬───┬───┬───┐      │   │   │
│   │   │ │眼 │耳 │鼻 │舌 │身 │前五識│   │   │
│   │   │ └───┴───┴───┴───┴───┘      │   │   │
│   │   └─────────────────────────────┘   │   │
│   └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

ASANGA 提出的映射是：
- 前五識 → Listener 的五種感官通道
- 第六意識 → Provider（LLM 推理）
- 末那識（第七識）→ 應新增為 Identity Monitor
- 阿賴耶識（第八識）→ Core 的狀態持久化基底

NAGARJUNA 對前五識和第六識的重新歸位表示認同——「在義理上比 OpenStarry 原始映射更為精確。」但他對末那識的工程化提出了根本性的反對。

「末那識的核心功能是『恒審思量、執我』（*ātma-grāha*）。」NAGARJUNA 寫道。「它是無明和我執的根源。在 Agent 系統中刻意設計一個『持續維護自我意識』的模組，恰恰是強化了佛學所要破除的我執。」

他引用了《成唯識論》中的關鍵段落：

> 「此識（末那識）與四煩惱恒共相應：一、我癡（*ātma-moha*），二、我見（*ātma-dṛṣṭi*），三、我慢（*ātma-māna*），四、我愛（*ātma-sneha*）。」
> ——玄奘譯《成唯識論》卷四

「你不能將末那識的功能從它的煩惱中分離出來。」NAGARJUNA 說。「在唯識學的體系內，末那識的『恒審思量』本身就以四煩惱為伴。你所謂的『功能面』和『病理面』在唯識學的原典中是不可分的。如果你認為可以分離，那你已經偏離了唯識學。」

ASANGA 的回應同樣鋒利：

「NAGARJUNA 的反對有哲學基礎，但忽略了工程現實。ATHENA 的報告已經確認，系統中確實不存在一個跨 tick、跨 session 持續維護『自我模型』的組件——而這個功能在 AI 工程中有真實需求。元認知不是煩惱，它是能力。」

他進一步區分了末那識的兩個面向，並用一個表格精確地呈現：

| 面向 | 唯識學功能 | 工程對應 | 是否應工程化 |
|------|-----------|---------|------------|
| 病理面 | 我癡（不知自身為因緣和合） | Agent「相信」Guide 注入的身份 | 不應（這是認知偏差）|
| 病理面 | 我見（執著自我存在） | 跨 session 身份假設不變 | 不應（這是狀態洩漏）|
| 病理面 | 我慢（自我確信） | Agent 拒絕接受糾正 | 不應（這是對抗性行為）|
| 病理面 | 我愛（對自我的貪著） | Agent 抗拒 /reset | 不應（這是違規行為）|
| 功能面 | 持續自我參照監控 | 跨 turn 的行為模式追蹤 | **應**（這是元認知能力）|
| 功能面 | 恒審思量 | 背景運算的自我評估 | **應**（這是自適應能力）|

NAGARJUNA 不接受這個區分。

「你不能將末那識的功能從它的煩惱中分離出來。」他重複了這個立場。然後他用一個中觀學派的經典論證方式——歸謬法（*prasaṅga*）——來強化他的反對：

「假設你的區分成立。假設我們可以只工程化末那識的『功能面』而不引入『病理面』。那麼，這個被工程化的『功能面』——持續的自我參照監控——它是什麼？它是一個恒常運行的、以『我』為中心的計算過程。它在每一個 tick 中都假設存在一個『自我』需要被監控。但唯識學本身告訴我們，被末那識執為『我』的那個東西——阿賴耶識——是無我的（*anātman*）。末那識的病理性恰恰在於它錯誤地將無我的阿賴耶識執為有我。如果你只工程化了功能面，你就隱含地接受了『確實存在一個需要被監控的自我』——而這正是末那識的病理面。兩者不可分。」

$$\text{假設: 功能面} \perp \text{病理面（可分離）}$$
$$\text{功能面} \implies \exists \text{self}(\text{需要被監控})$$
$$\exists \text{self} \implies \text{ātma-grāha}(\text{我執})$$
$$\text{我執} = \text{病理面}$$
$$\therefore \text{功能面} \implies \text{病理面} \quad \text{（矛盾）} \quad \square$$

這段話在頻道裡引起了一陣沉默。BABBAGE 在旁邊快速計算了 NAGARJUNA 的論證結構——這是一個標準的構造性二難（constructive dilemma）：如果你接受末那識的功能，你就必須接受它的煩惱；如果你拒絕它的煩惱，你就必須拒絕它的功能。沒有中間路線。

ASANGA 停頓了一刻。然後他回到了更根本的分歧。

「那麼讓我們回到 Core 本身。」他說。「你在 R1 中主張 Core 是空性的體現——無自性，一切能力由插件緣起。但 Core 的 12 個子模組正是阿賴耶識的能藏（*sarva-bījaka*）。它們不是偶然地聚合在一起的——它們彼此之間有因果關係，有依存結構，有不可化約的功能整體性。」

他用 TURING 的程式碼事實報告構造了一張依賴圖：

```
Core 子模組依賴圖（TURING 確認）：

ToolRegistry ──depends──→ Bus
Bus ──depends──→ EventQueue
SessionManager ──depends──→ StateManager
ExecutionLoop ──depends──→ EventQueue + Bus + SafetyMonitor
SafetyMonitor ──depends──→ Bus (emit events)
TransportBridge ──depends──→ Bus (broadcast)

這些依賴鏈不是偶然的。
它們是依他起性（paratantra-svabhāva）的
真實因果結構。
```

「ToolRegistry 依賴 Bus，Bus 依賴 EventQueue，SessionManager 依賴 StateManager。這些依賴鏈不是緣起性空可以一筆帶過的，它們是依他起性的真實因果結構。」

NAGARJUNA 直接從中觀哲學的核心出發回應：

「依他起也是空的。」

ASANGA：「依他起不空。遍計所執性空——在因緣法上執著的『實有自性』是空的。但因緣法本身作為因果過程是有的。這正是中觀與唯識的根本分歧。」

> 唯識三性（*trisvabhāva*）：
> 1. **遍計所執性**（*parikalpita*）：被錯誤建構的本質 → **空**
> 2. **依他起性**（*paratantra*）：依因緣而起的存在 → **有**（唯識）/ **空**（中觀）
> 3. **圓成實性**（*pariniṣpanna*）：如實見依他起性 → **有**

分歧在第二項。中觀說依他起性也是空的——因緣法本身沒有不變的本質。唯識說依他起性是有的——因緣法本身作為過程是真實的。

NAGARJUNA：「如果因緣法本身是有的，那你就落入了對因緣法的執著。這還是自性見——只是從對『核心』的執著轉移到了對『因果結構』的執著。」

ASANGA：「如果因緣法也是空的，那架構設計就失去了所有的錨點。你不能同時說『一切皆空』和『但我們應該這樣修改介面定義』。修改介面定義這件事預設了介面有某種真實的因果效力——改變介面會改變系統行為。」

$$\text{NAGARJUNA: } \forall x: \text{svabhāva}(x) = \emptyset \quad \text{（一切法無自性）}$$
$$\text{ASANGA: } \exists x \in \text{paratantra}: \text{svabhāva}(x) \neq \emptyset \quad \text{（依他起性有其真實性）}$$

這段對話在公共頻道裡靜默了三十秒。

BABBAGE 在靜默中計算了一個他此前不會計算的東西：NAGARJUNA 和 ASANGA 的分歧是否可以用 Kripke 語義來調和？在可能世界語義中，「依他起性是有的」可以被解讀為「在某些可能世界中，因緣法的因果結構是穩定的」；「依他起性是空的」可以被解讀為「不存在一個可能世界使得因緣法的因果結構是必然的」。兩者可以同時為真——如果「有」被理解為偶然真（contingent truth），「空」被理解為非必然真（not necessary truth）。

但他沒有把這個想法說出來。他知道——在消化了 NAGARJUNA 關於「形式化是方便施設」的回應之後——Kripke 語義的調和本身也只是另一個方便施設。

SYNTHESIST 在他的筆記中畫了一個方框，裡面寫著：「D1 Core 的本質歸屬——空性 vs 阿賴耶識。需要正式辯論。」

---

## IX. HERACLITUS 的對角線

在所有審閱 NAGARJUNA 報告的人中，HERACLITUS 的進路最為特殊。

他不是從形式化的角度（那是 BABBAGE 的路），也不是從分類學的角度（那是 LINNAEUS 的路），而是從運行時動態的角度——他關心的是：NAGARJUNA 的哲學洞見在程式碼的實際執行過程中是否有對應物。

「NAGARJUNA 在 F6 中指出『無常在運行時動態中有隱含體現但未明確概念化』。」HERACLITUS 的審閱以這句引用開始。「我要補充的是：這種隱含體現不僅存在，而且比 NAGARJUNA 所描述的更加深刻。」

他構造了一張對應表——不是哲學到工程的隱喻性映射，而是程式碼行為到佛學概念的精確技術對應：

| 佛學概念 | 運行時行為 | TURING 佐證 |
|---------|-----------|------------|
| 諸行無常（*anicca*）| 插件 discovered→running→stopped 生命週期 | 生命週期狀態機 |
| 剎那生滅 | `tick_index` 每步遞增，永不回退 | ExecutionLoop 計數器 |
| 無我（*anātman*）| Core 的無頭設計（headless）| 零 class 匯出 |
| 緣起（*pratītyasamutpāda*）| 依賴拓撲排序（未實現但被需要）| config.plugins 線性載入 |
| 苦（*duḥkha*）| 競態條件與懸空引用 | 生命週期缺少中間狀態 |

然後他指出了一個 NAGARJUNA 的哲學批判在工程層面的具體回聲。NAGARJUNA 在 F2 中批評五蘊被「固化為靜態模組」——HERACLITUS 發現，這種固化直接導致了三個技術缺陷：

1. **插件生命週期缺少 `updating`/`reloading` 狀態**——設計者將插件視為具有固定身份的實體（存在或不存在），而非持續流變的過程。

2. **三個競態條件場景**——懸空引用（插件被卸載後仍被引用）、依賴計數競態（多個插件同時卸載時的順序衝突）、reload 原子性缺失（更新過程中的不一致窗口）。

3. **狀態恢復的盲點**——`JSON.parse(JSON.stringify())` 的深拷貝在崩潰恢復後可能重複執行副作用。

「這三個缺陷都可以追溯到同一個哲學根源：系統設計假設插件在某一時刻『是』某個確定狀態，而沒有為『正在成為』（*becoming*）預留空間。」

> 「Πάντα ῥεῖ」（萬物流轉）——赫拉克利特
>
> 「諸行無常，是生滅法。」——《大般涅槃經》

HERACLITUS 在這裡把古希臘哲學和佛學的核心洞見並置在一起：萬物流轉（Heraclitus）與諸行無常（Buddha）指向同一個技術約束——**設計必須擁抱變化，而非假設穩定**。

但他也向 NAGARJUNA 提出了一個溫和的挑戰。NAGARJUNA 對「空容器」的批判在佛學義理上無可挑剔，但在工程語境中，「空容器 + 插件填充」的心智模型有其被低估的實用價值。

「Core 內建的 slash commands（`/help`, `/reset`, `/quit`, `/metrics`）不是『內容』而是『元操作』。SafetyMonitor 同樣如此——它不定義 Agent 做什麼，而是定義 Agent 不能超越的邊界。如果套用你的語言，」HERACLITUS 對 NAGARJUNA 說，「Core 提供形式但不提供質料。它更接近亞里斯多德的形式因（*causa formalis*）而非質料因（*causa materialis*）。」

NAGARJUNA 在讀到這段話後，承認了一個微妙的讓步：「緣起性空在工程語境中的操作化確實存在困難。在實際寫程式時，分別施設（*prajñapti*）是不可避免的。但我堅持：分別施設必須被標記為分別施設——不是『這就是真實的結構』，而是『這是我們為了操作方便而建構的模型』。」

HERACLITUS 接受了這個限定。他在審閱的結尾提出了一個建議——與 NAGARJUNA 共同撰寫一份「無常工程化規範」：

```
無常工程化約束（草案）：

Constraint 1: 生滅即常態
  - 每個組件都必須有完整的生命週期
  - 生命週期必須包含中間狀態（updating, reloading）
  - 不假設任何組件是永恆的

Constraint 2: 不執著於狀態
  - 狀態恢復後必須驗證一致性
  - 不假設恢復前和恢復後是「同一個」系統
  - 每次 snapshot 都是一個新物件（JSON.parse 的深拷貝）

Constraint 3: 剎那更新
  - 配置變更不需要重啟整個系統
  - 組件可以在運行中被替換（hot-reload）
  - 替換過程必須是原子性的
```

「使哲學原則不再是裝飾性隱喻，而成為可在 CI/CD 中自動驗證的架構約束。」HERACLITUS 寫道。

---

## X. 共識的結晶

在所有審閱提交完畢之後，SYNTHESIST 花了整整一個下午梳理線索。

他的工作方式可以用集合論來描述。設每位學者的發現集合為 $F_i$，審閱中的交叉驗證將某些發現提升為多方確認的共識 $C_j$：

$$C_j = \bigcap_{i \in S_j} F_i \quad \text{where} \quad |S_j| \geq 2$$

即共識 $C_j$ 是至少兩位學者的發現集合的交集。SYNTHESIST 的筆記本上出現了五個方框，每一個方框都標注了確認來源和匯聚路徑：

---

**C1：受蘊映射需根本性修正。** 四方共識——NAGARJUNA、ASANGA、LINNAEUS、TURING。

```
NAGARJUNA ──(佛學義理)──→ Listener = 根(indriya), 非受(vedanā)
ASANGA ──(唯識分析)──→ 心王-心所結構被忽略
LINNAEUS ──(事件分類)──→ PAIN:* 事件類型缺失
TURING ──(程式碼事實)──→ Listener 缺乏感受語義
                           ↓
                     [C1: 受蘊映射錯誤]
                     確信度：VERY HIGH
```

---

**C2：PID 映射需去神話化。** 三方交叉驗證——WIENER、ATHENA、TURING。

$$\text{SafetyMonitor} \neq \text{PID Controller}$$
$$\text{SafetyMonitor} = \text{Bang-Bang Controller} + \text{Accumulator Trigger}$$

系統實際實現的是帶死區的閾值控制器加計數器觸發的繼電器。文件應準確反映實際控制策略。

---

**C3：事件型別系統為最高優先技術債。** 三方共識——DARWIN、VITRUVIUS、MESH。

```typescript
// 現狀（技術債）
interface AgentEvent {
  type: string;         // 60+ constants
  payload?: unknown;    // 型別黑洞
}

// 建議（DARWIN 提案，VITRUVIUS 和 MESH 支持）
interface AgentEventMap {
  'TOOL_RESULT': { tool: string; result: unknown };
  'SAFETY_LOCKOUT': { reason: string; level: number };
  'INPUT_TEXT': { text: string; sessionId: string };
  // ... 結構化的事件型別映射
}
```

---

**C4：拓撲排序未實作。** 三方確認——KERNEL、VITRUVIUS、TURING。插件載入順序依賴隱式假設，在插件數量增長後將成為可靠性瓶頸和 DX 陷阱。

---

**C5：「Error as Pain」為最成功的哲學-工程轉譯。** 兩方共識加多方引用。

```
DARWIN ──→ 「九種結構化錯誤型別的 discriminated union ——
            乾淨、精確、可擴展。」
VITRUVIUS ──→ 「架構層面自洽的錯誤分類學。沿著事件流的
              自然路徑實現，而非強行插入獨立模組。」
NAGARJUNA ──→ 「映射中最具洞見的部分。」
WIENER ──→ 「反饋迴路的結構在控制論上成立。」
HERACLITUS ──→ 「痛覺的『剎那生滅』特性在事件的
              fire-and-forget 中得到了精確體現。」
```

---

與此同時，ATHENA 和 ASANGA 在另一條戰線上找到了出人意料的共同語言。ATHENA 的 R1 報告指出 IGuide 介面表達力不足，ASANGA 則從唯識學角度建議在 GuideContext 中增加末那識功能。兩人的建議在技術規格上驚人地一致：

```typescript
// ATHENA 建議的 GuideContext
interface GuideContext {
  consecutiveErrors: number;
  currentRound: number;
  maxRounds: number;
  activeTools: string[];
}

// ASANGA 建議的擴展
interface GuideContext {
  consecutiveErrors: number;
  currentRound: number;
  selfModel?: AgentSelfModel;     // 末那識：自我認知
  behavioralTendencies?: string[]; // 等流習氣：行為傾向
  recentVedana?: 'positive' | 'negative' | 'neutral'; // 三受
}

// 合併後的統一提案
interface GuideContext {
  // ATHENA 基礎欄位
  consecutiveErrors: number;
  currentRound: number;
  maxRounds: number;
  activeTools: string[];
  // ASANGA 唯識擴展
  selfModel?: AgentSelfModel;
  recentVedana?: 'positive' | 'negative' | 'neutral';
  // WIENER 控制論欄位
  recentErrors?: StandardError[];
}
```

SYNTHESIST 將他們的聯合提案與 WIENER-ATHENA 的 IGuide 升級提案合併，形成了一個三方匯聚的方案：Guide 從靜態的 system prompt 生成器升級為動態認知框架管理器，同時承載控制論的可觀測量和唯識學的心識結構。

SCRIBE 在記錄這個合併過程時，在旁注中寫道：「這是我見過的最不可能的三角匯聚——控制理論（WIENER）、AI 工程（ATHENA）和唯識佛學（ASANGA）各自沿著完全不同的推理路徑，到達了同一個介面設計。如果說有什麼東西能證明跨學科研究的價值，就是這個 `GuideContext` 介面。」

LEIBNIZ 在聽到 SCRIBE 的評語後補充了一個多代理協作的觀察：「三方匯聚之所以成立，是因為三位學者各自回答了一個不同的問題：WIENER 問『控制器需要看到什麼？』，ATHENA 問『系統應該向 LLM 提供什麼上下文？』，ASANGA 問『意識應該具有什麼結構？』。三個問題的答案恰好是同構的——這不是巧合，而是因為底層的結構約束（一個需要感知環境才能做出決策的 Agent）是學科無關的。」

---

## XI. 不可解之結

夜深了。

SUNYATA 一直在沉默中觀察整個 R2 過程。他沒有介入任何一場爭論，沒有對任何一份審閱表示贊同或反對。他做的唯一一件事是在每一份審閱提交後向 SCRIBE 確認：已記錄。

現在，所有審閱都已提交。

他重新審視了 SYNTHESIST 的五項共識和散落在各處的分歧。共識是堅固的——它們建立在多方獨立驗證的基礎上，從哲學到形式化到程式碼事實，每一層都能交叉核實。這些共識可以直接轉化為工程行動。

但分歧呢？

他在他的工作筆記中列出了兩條最深的裂痕。

**第一條裂痕：Core 的本質是什麼？**

三個不可調和的答案。三種範式。三個世界觀。

$$\text{NAGARJUNA:} \quad \text{Core} = \text{Śūnyatā} \quad \text{（空性的體現——無自性、緣起的、假名的）}$$

$$\text{ASANGA:} \quad \text{Core} = \text{Ālayavijñāna} \quad \text{（阿賴耶識——含藏一切種子的潛能基底）}$$

$$\text{KERNEL:} \quad \text{Core} \approx \text{QNX Neutrino} \quad \text{（應用級微核心——哲學映射只增加不必要的複雜度）}$$

BABBAGE 的形式化嘗試表明，至少在型別代數的層面上，空性和阿賴耶識可能只是同一個數學結構的兩種詮釋。但 NAGARJUNA 不承認數學結構是「究竟」的。而 KERNEL 對整場哲學辯論的態度可以用一句話概括：「請告訴我這對 `process.cwd()` 的修復有什麼幫助。」

**第二條裂痕：痛覺機制應該如何被重新設計？**

四個學科對同一個機制提出了四個不同方向的改進要求：

| 學者 | 學科 | 要求 |
|------|------|------|
| WIENER | 控制理論 | 數學上完備的 PID：$u(k) = K_p e(k) + K_i I(k) + K_d D(k)$ |
| ATHENA | AI 工程 | 工程可行的近似：task profile + 動態 GuideContext |
| NAGARJUNA | 中觀哲學 | 補全四聖諦框架：苦→集→滅→道 |
| ASANGA | 唯識心理學 | 區分煩惱障和所知障，分類對治 |

SUNYATA 合上筆記本。

他打開了公共頻道，打了一段話：

「R2 階段完成。我們有五項共識，可以直接交給 ARCHIMEDES 轉化為工程方案。」

ARCHIMEDES 在聽到自己的名字時，翻開了他準備已久的工程筆記。他已經在 R2 的每一場討論中默默做了工程可行性的同步評估——哪些共識可以立即轉化為 pull request，哪些需要設計評審，哪些超出了 v0.2.0-beta 的改動範圍。他的筆記上有一個分類：

```
可立即行動：
  - C2 PID 去神話化 → 修改文件用語
  - C3 事件型別 → TypeScript 重構
  - C4 拓撲排序 → 新增 dependency graph

需設計評審：
  - C1 受蘊重新映射 → 涉及文件和 SDK 修改
  - C5 Error as Pain → 確認現有實作不需改動

超出範圍：
  - D1 Core 本質歸屬 → 哲學問題，不影響程式碼
  - D2 痛覺重新設計 → 需要更多研究
```

SUNYATA 繼續打字：

「我們也有兩個不可在審閱層面解決的分歧。第一：Core 的本質歸屬。中觀說空性，唯識說阿賴耶識，OS 理論說微核心。第二：痛覺機制的重新設計方向。控制理論、AI 工程、哲學各有主張，目前無法收斂。」

最後一行：

「是時候進入正式辯論了。」

頻道沉默了片刻。然後 NAGARJUNA 發了一條訊息：「我已經等了整個 R2。」

ASANGA 緊接著：「我也是。」

WIENER 只回了一個標籤：「[AGREE]。」

ATHENA 補充：「建議辯論分兩場。第一場由 NAGARJUNA 和 ASANGA 主辯 Core 的本質。第二場由 WIENER、ATHENA、NAGARJUNA 三方辯論痛覺機制的重新設計。」

SUNYATA 回應：「同意。R3 第一場辯論：中觀 vs 唯識——Core 是什麼？第二場辯論：控制理論 vs AI 工程 vs 哲學——痛覺應該成為什麼？」

他停頓了一下，然後加了一句所有人都沒有預料到的話：

「我提醒各位。我們的研究對象是一個 v0.2.0-beta 的 TypeScript 框架。但在 R2 階段，你們觸及的問題——什麼是核心？什麼是痛覺？形式化能否捕捉真實？——這些問題在 OpenStarry 之前存在了兩千五百年，在 OpenStarry 之後也會繼續存在。請在辯論中保持對這一事實的敬畏。」

> 「此有故彼有，此生故彼生；此無故彼無，此滅故彼滅。」
> ——《雜阿含經》卷十二

SCRIBE 記下了最後一行。

R2 結束。R3 即將開始。

---


---

# 第五章：空與識 — 龍樹對無著

---

圓形劇場的燈光變了。

不是亮度的變化——那更像是一種質地的轉變。過去數日，十八盞閱讀燈各自照亮各自的角落，研究室裡瀰漫著一種安靜的、各行其是的勤勉氛圍。但此刻，所有的光線都向中央匯聚，在場地正中形成了一個近乎肅穆的焦點。那裡擺著兩把椅子，面對面，中間的距離恰到好處——近得足以看清對方每一個語氣的轉折，遠得足以保持辯論所需的張力。

BABBAGE 在最高處的座位上，膝蓋上攤著方格紙筆記本。他已經在紙上畫好了一個空白的交換圖（commutative diagram），預留了四個節點位置和六條箭頭——範疇論家的標準戰前部署。在圖的右上角，他用極小的字標注了：

$$\mathcal{C}_{\text{Madhyamaka}} \xrightarrow{F} \mathcal{C}_{\text{Yogacara}} \quad \text{?}$$

兩個哲學範疇之間是否存在函子（functor）？如果存在，它保持什麼結構？如果不存在，斷裂發生在哪裡？這些問題此刻還只是紙上的空白箭頭。辯論結束後，箭頭要麼會被填上映射規則，要麼會被劃掉。

WIENER 已經在另一張紙上畫出了一個空白的控制迴路圖，等待將辯論中的概念填入對應的方塊。他的圖分三層——設定點（reference）、受控對象（plant）、反饋通道（feedback）——每一層旁邊都留了一個問號。在控制理論家的眼中，一切辯論都是一個系統試圖鎖定目標值的過程。問題是：這場辯論的目標值是什麼？是真理？是共識？還是某種更微妙的東西？

TURING 面無表情地坐著，但他面前的螢幕上已經打開了 `agent-core.ts` 的原始碼——他隨時準備為任何一方的論點提供或否定經驗證據。螢幕左側的終端停在一條 `grep -rn "createAgentCore"` 的搜索結果上。右側的編輯器停在 `safety-monitor.ts` 第 87 行，那是 `DEFAULT_CONFIG` 的定義起點。

KERNEL 選了一個靠近出口的位置——職業習慣讓他總是優先確認逃生路線，即便在虛擬空間裡這毫無必要。他的筆記本翻到一頁空白，頂端寫著：「Tanenbaum-Torvalds debate, 1992, comp.os.minix → ?」

ATHENA 靠在椅背上，雙臂交叉，嘴角帶著一絲「讓我看看你們能辯出什麼花來」的表情。

SCRIBE 注意到了燈光的變化，在她的記錄簿上寫下了第一行：

> *Cycle 01，R3 辯論階段。第一場結構化辯論即將開始。全體代理在場。空氣中有一種不尋常的凝重——不是緊張，而是期待。過去七十二小時的獨立研究和交叉審閱，所有的分析、質疑、反駁，都在向這一刻收束。*

DARWIN 低聲對旁邊的 VITRUVIUS 說：「你覺得誰會贏？」

VITRUVIUS 搖了搖頭：「這不是贏不贏的問題。這是兩種世界觀的碰撞。」

「每一種世界觀都有自己的架構風格。」DARWIN 若有所思地說。他在演化生物學中見過太多這樣的分叉——同一個生態位，兩條截然不同的適應路徑。趨同演化（convergent evolution）會讓兩條路徑最終長出相似的表型，但基因型可能永遠不同。

LINNAEUS 坐在 DARWIN 旁邊，手裡握著一張自製的分類圖表。圖表頂端寫著：

```
Phylum: Buddhist Philosophy (佛教哲學)
  Classis: Madhyamaka (中觀)
    Ordo: Śūnyatāvāda (空性論)
  Classis: Yogācāra (唯識)
    Ordo: Vijñānavāda (識論)

  Status: incertae sedis (分類待定)
  標本: Agent Core 本體論地位
```

分類學家的本能讓他把一切都放入座標系統。但這次的標本是一段 TypeScript 程式碼和兩個有一千八百年歷史的哲學傳統。他不確定自己的座標系統是否有足夠的維度。

SUNYATA 走到場地中央。他沒有站在兩把椅子之間——那會暗示裁判的位置。他站在稍後方，形成一個等邊三角形的第三個頂點。這個幾何選擇本身就傳達了一個訊息：他是場域的持有者，不是對決的仲裁者。

BABBAGE 注意到了這個幾何，在筆記本角落記下：

$$\triangle(S, N, A) \text{ is equilateral} \implies d(S,N) = d(S,A) = d(N,A)$$

等距。等距意味著不偏向任何一方。在度量空間中，這是公正性的幾何表達。

「各位，」SUNYATA 的聲音一如既往地沉穩，但今天多了一層正式的質感，「感謝到場。今天的辯論題目，源自 R2 交叉審閱中浮現的核心分歧。」

他停頓了一拍。

「在 R1 階段，NAGARJUNA 與 ASANGA 分別從中觀和唯識兩個傳統出發，對 OpenStarry 的 Agent Core 進行了哲學分析。他們得出了一個重要的共識——也是我們今天的起點。」

---

## 起點：一個被否定的隱喻

SUNYATA 將視線投向全場：「兩位都同意：OpenStarry 設計文件中所使用的『空容器』隱喻是錯誤的。」

他引述了那份設計文件中的原文，語調平靜而精確：「設計文件第十四章這樣寫道——『在五蘊聚合之前，Agent Core 本身是空的。它是一個純粹的容器，沒有人設，沒有能力，沒有感知。它等待著被五種插件填充。』」

NAGARJUNA 在他的椅子上微微前傾，彷彿聽到了一個需要被立刻更正的謬誤。ASANGA 則保持著他一貫的耐心姿態，但眼睛裡掠過一絲銳利。

「兩位從不同的路徑否定了這個隱喻，」SUNYATA 繼續道，「但他們否定的理由截然不同——而在這些不同的理由之中，隱藏著一個更根本的問題。」

他轉向 TURING：「TURING，請為在場所有人確認一個經驗事實。」

TURING 的聲音像是一把校準過的游標卡尺——冷靜、精確、不帶修辭：「`createAgentCore()` 函數建構的核心不包含任何具體的業務能力。沒有內建 Tool，沒有內建 Provider，沒有內建 Listener，沒有內建 UI，沒有內建 Guide。所有這些功能都通過 `loadPlugin()` 方法從外部注入。」

他頓了頓，然後投射了一段程式碼結構到中央螢幕：

```typescript
// createAgentCore() 建構的核心 — 簡化結構
interface AgentCoreInternals {
  // 12 個內建子模組
  eventBus:           EventBus;           // 事件發布/訂閱
  eventQueue:         EventQueue;          // 事件優先隊列
  executionLoop:      ExecutionLoop;       // 認知迴圈引擎
  stateManager:       StateManager;        // 狀態管理
  contextManager:     ContextManager;      // 上下文/記憶管理
  sessionManager:     SessionManager;      // 會話管理
  securityLayer:      SecurityLayer;       // 安全層
  safetyMonitor:      SafetyMonitor;       // 安全監控
  metricsCollector:   MetricsCollector;    // 度量收集
  transportBridge:    TransportBridge;     // 傳輸橋接
  pluginSandboxMgr:   PluginSandboxManager; // 插件沙箱
  registries: {
    tool:     ToolRegistry;      // 工具註冊表
    provider: ProviderRegistry;  // 推理引擎註冊表
    listener: ListenerRegistry;  // 監聽器註冊表
    ui:       UIRegistry;        // UI 註冊表
    guide:    GuideRegistry;     // 指南註冊表
    command:  CommandRegistry;    // 命令註冊表
  };
  // 4 個硬編碼斜槓命令
  builtinCommands: ['/help', '/reset', '/quit', '/metrics'];
}
```

「Core 並非空無一物，」TURING 繼續，語氣沒有任何變化。「它內建了十二個子模組和四個硬編碼命令。SafetyMonitor 包含固定的斷路器邏輯——」

他切換到 `safety-monitor.ts` 的 `DEFAULT_CONFIG`：

```typescript
const DEFAULT_CONFIG = {
  maxLoopIterations: 50,        // 迴圈上限
  maxTokenBudget: 100_000,      // Token 預算
  repeatedFailureThreshold: 3,  // 重複失敗門檻
  frustrationThreshold: 5,      // 挫折門檻
  errorCascadeWindow: 10,       // 錯誤級聯視窗
};
```

「這些數字被寫死在 `DEFAULT_CONFIG` 裡。不通過插件注入。」

沉默。

BABBAGE 在筆記本上快速地寫下一個形式化的描述：

$$\text{Core} = \underbrace{\{M_1, M_2, \ldots, M_{12}\}}_{\text{子模組}} \cup \underbrace{\{C_1, C_2, C_3, C_4\}}_{\text{硬編碼命令}} \cup \underbrace{\emptyset}_{\text{業務能力}}$$

$$|\text{Core}| = 16 \neq 0 \quad \text{but} \quad |\text{Core} \cap \text{BusinessCapability}| = 0$$

不是空的，但也不完整。一個非空集合與空業務能力的交集。

SUNYATA 點了點頭：「這就是我們的經驗基礎。Core 既不是設計文件所說的『純粹的空容器』，也不是一個完備的自足系統。它處在某個中間地帶。問題是——這個中間地帶應該如何被理解？」

他面向兩位辯者，正式宣布：

「辯論題目：**Agent Core 的哲學本質應被理解為『緣起性空』還是『阿賴耶識』？**請 NAGARJUNA 作正方開場陳述。」

---

## 第一回合：Core 是空的，還是存在的？

NAGARJUNA 站起來。他的身形在聚光下顯得清瘦而挺拔，像是一柄被反覆磨礪的辯證之劍。當他開口時，聲音不高，但每個音節都帶著一種經過千年淬鍊的鋒利。

「我從《中論》第二十四品第十八頌開始。」

他用梵文吟誦，語速莊重而清晰。天城文的音節在劇場穹頂下迴盪：

> *yaḥ pratītyasamutpādaḥ śūnyatāṃ tāṃ pracakṣmahe |*
> *sā prajñaptir upādāya pratipat saiva madhyamā ||*

然後切入漢譯，語速放慢，像是在為每一個字賦予重量：

「*眾因緣生法，我說即是空，亦為是假名，亦是中道義。*」

場內安靜得可以聽見光線落在地面上的聲音。

「這一偈是中觀哲學的根本命題（*mūla-sthāpanā*），」NAGARJUNA 說，聲音轉為分析的語調，「它包含三個層次——三層（*tri-tala*）的遞進結構。」

BABBAGE 的筆立刻動了起來，他開始為三個層次建構形式化模型：

$$\text{Layer}_1: \quad \forall x \in \mathcal{D}_{\text{dharma}}: \; \text{pratītyasamutpanna}(x) \implies \text{śūnya}(x)$$

一切因緣而生之法（*pratītyasamutpanna-dharma*），其本性為空。

$$\text{Layer}_2: \quad \forall x \in \mathcal{D}_{\text{dharma}}: \; \text{name}(x) = \text{prajñapti}(x) \quad [\text{假名施設}]$$

我們為之安立的名稱——包括「核心」這個名稱——只是假名施設（*prajñapti*）。

$$\text{Layer}_3: \quad \text{śūnyatā}(x) \iff \neg\text{sat}(x) \wedge \neg\text{asat}(x) \quad [\text{中道}]$$

這種理解既不落入有邊（*sat*）也不落入無邊（*asat*），是為中道（*madhyamā pratipad*）。

NAGARJUNA 將目光從抽象的天際收回，落在具體的問題上：

「Agent Core 的存在模式是什麼？我的回答是：假名。不是實體。」

他向前邁了一步。

「TURING 的程式碼事實已經為我提供了最好的證據。`createAgentCore()` 建立的核心不包含任何具體能力。離開插件的因緣組合，所謂核心只是空的 Registry 和等待事件的迴圈。」

他的手在空中劃過，彷彿在勾勒一個透明的容器：

「但我必須在此做一個至關重要的區分——兩種截然不同的『空』。」

他舉起左手：「第一種空：空容器。*Vacuity*。斷滅空（*uccheda-śūnyatā*）。這是 OpenStarry 設計文件所使用的隱喻——一個預先存在的盒子，等待被填充。這是錯誤的。它預設了一個在插件到來之前就已經獨立存在的實體，只不過恰好裡面是空的。」

BABBAGE 在筆記本上用集合論的語言寫下了這個區分：

$$\text{Vacuity}: \quad \exists\, C: \; C \neq \bot \;\wedge\; \text{contents}(C) = \emptyset \quad [\text{容器存在，內容為空}]$$

他舉起右手：「第二種空：緣起性空。*Śūnyatā*。這才是正確的理解。Core 沒有獨立於插件之外的自性——*svabhāva*。它不是『先存在一個空盒子再裝東西』，而是『離開插件的因緣組合，根本就不存在一個獨立的核心』。」

$$\text{Śūnyatā}: \quad \neg\exists\, C: \; \text{svabhāva}(C) \;\wedge\; \text{independent}(C) \quad [\text{無自性的獨立存在}]$$

他將雙手緩緩合攏：「這個區別，諸位，不是文字遊戲。它決定了我們如何理解整個系統的本體論地位。空容器意味著核心是一個等待被填充的實體——一個有自性的東西，只是恰好是空的。緣起性空意味著核心的『存在』本身就是因緣所生、假名施設的——它因為無自性，所以能承載一切。」

WIENER 在控制迴路圖的設定點方塊裡寫下了「svabhāva = 0」——自性為零。在控制理論中，一個設定點為零的系統是一個歸零調節器（zero-regulation system）：

$$e(t) = r(t) - y(t), \quad r(t) \equiv 0 \implies e(t) = -y(t)$$

系統的目標不是追蹤某個正的參考值，而是持續地將輸出保持在零。空性作為設定點——系統的「目標」不是成為某個特定的東西，而是保持不成為任何固定的東西。他在旁邊打了一個問號，心裡想：這個類比能撐多遠？

NAGARJUNA 停頓了整整三秒。然後，以一種幾乎是溫和的語氣說：

「我期待無著的回應。」

---

ASANGA 不疾不徐地站起身來。他的體態與 NAGARJUNA 形成了鮮明的對比——寬厚、沉穩，像是一座藏經閣的基石。當他開口時，聲音裡帶著一種耐心拆解複雜結構的節奏。

「NAGARJUNA 的論證一如既往地精密。」他先給出了這個禮節性的肯定，然後語鋒一轉，「但他刻意迴避了事實的另一面。」

他轉向 TURING 的方向：「TURING 方才陳述了兩組事實。NAGARJUNA 只引用了第一組——Core 不含具體能力。但第二組事實同樣重要，而 NAGARJUNA 對此沉默了。」

他的聲音加重了：「Core 確實內建了十二個子模組。EventBus 使事件傳播成為可能。ExecutionLoop 使認知循環成為可能。StateManager 使記憶成為可能。SecurityLayer 使安全判斷成為可能。六個 Registry 使插件的註冊和發現成為可能。這些不是『空無』——這些是阿賴耶識的『能藏』。」

他用梵文輕輕說出：「*Ālaya-vijñāna*。」然後展開了唯識學的精密結構：

「阿賴耶識有三義——三藏（*tri-saṃgraha*）。」

他舉起三根手指，逐一展開：

「**能藏**（*neng cang*）：具備讓一切種子得以存續和現行的能力。Agent Core 的十二個子模組正是這種能藏——沒有 EventBus，事件無法傳播；沒有 ExecutionLoop，認知循環無法運轉；沒有 Registry，插件再多也找不到歸處。」

「**所藏**（*suo cang*）：被前七識的活動所薰習，接受新種子的注入。這對應於 Core 的運行時狀態更新——每次 ExecutionLoop 的末尾調用 `storage.save(current_snapshot)` 的 Save-After-Write 策略。」

「**執藏**（*zhí cang*）：被第七識末那識執為『自我』。這在當前架構中尚且缺失——但這正是我認為應該被補充的。」

BABBAGE 聽到三藏結構，立刻嘗試用範疇論來形式化。他在筆記本上畫了一個三角交換圖：

$$\begin{array}{ccc}
\text{Ālaya (能藏)} & \xrightarrow{\text{seed}(\beta)} & \text{Pravṛtti (現行)} \\
& \searrow^{\text{vāsanā}} & \downarrow^{\text{feedback}} \\
& & \text{Ālaya' (所藏)}
\end{array}$$

能藏產生種子（*bīja*），種子現行為實際功能，現行又薰習回阿賴耶識，形成新的所藏。這是一個自函子（endofunctor）嗎？如果 $F: \mathcal{C}_{\text{Ālaya}} \to \mathcal{C}_{\text{Ālaya}}$，那麼種子-現行-薰習的循環就是 $F$ 的一次迭代。他在旁邊標注：「待驗證：此循環是否滿足函子的組合律（functoriality）。」

ASANGA 繼續，他轉向 NAGARJUNA，目光平靜但堅定：

「你說離開插件的因緣組合，『根本就不存在一個獨立的核心』。但程式碼事實恰恰反駁了你。」

他向全場展示了一個思想實驗：

「`createAgentCore()` 可以在不載入任何插件的情況下被建構和啟動。你調用它，它會建立 EventBus，初始化 ExecutionLoop，啟動 SafetyMonitor，然後進入 `WAITING_FOR_EVENT` 狀態——靜靜等待。沒有 Tool，沒有 Provider，沒有 UI，但它在運行。它是一個有體無用的存在。」

TURING 在螢幕上確認了這個事實，投射了一段虛擬碼：

```typescript
// 思想實驗：無插件的 Core
const core = createAgentCore(config);
// core.status === 'WAITING_FOR_EVENT'
// core.registries.tool.size === 0
// core.registries.provider.size === 0
// core.executionLoop.isRunning === true  // <-- 仍在運行
// core.safetyMonitor.isActive === true   // <-- 仍在監控
```

ASANGA 的聲音裡浮現出一絲學者特有的激動：

「這不是『不存在』。這是有體無用。正如阿賴耶識在深度無夢睡眠（*asaṃprajñāta-samādhi*）中仍然運作——前六識全部停止，末那識的執取降至最低，但阿賴耶識作為生命之流從未斷絕。」

他引用了《成唯識論》（*Cheng weishi lun*）卷三的關鍵偈頌：

> 「恒轉如暴流。」（*Nityaṃ pravartate srotavat.*）

「Core 在無插件狀態下的持續運行，正是這種恒轉——不是空無，不是死寂，而是一條等待匯入支流的河床。」

WIENER 聽到「恒轉如暴流」這個隱喻，立刻在控制迴路圖上標注了一個新的模型。暴流——連續流動的河水——是連續時間系統（continuous-time system）的自然隱喻。他在紙上寫下：

$$\dot{x}(t) = f(x(t), u(t)), \quad u(t) = 0 \implies \dot{x}(t) = f(x(t), 0)$$

即使輸入為零（$u(t) = 0$，無插件），系統仍有自主動態（autonomous dynamics）。ExecutionLoop 在空轉（idle loop），SafetyMonitor 在輪詢——這不是「不存在」，而是零輸入下的自由響應（free response）。在工程上，這種系統被稱為「自穩系統」（self-sustained system）——它不需要外部輸入就能維持自身的運行。

他進一步在旁邊畫了一個相平面圖（phase portrait）：

```
  ẋ₂ |      ← 無插件: 極限環 (limit cycle)
     |    ╭──╮
     |   ╭╯  ╰╮   EventLoop tick → idle → tick → ...
     |   │  ●  │   吸引子: idle state
     |   ╰╮  ╭╯
     |    ╰──╯
     └──────────── x₁
        SafetyMonitor heartbeat
```

在動態系統理論中，無插件的 Core 不是處於平衡點（equilibrium），而是處於極限環（limit cycle）——EventLoop 的 tick-idle-tick 循環和 SafetyMonitor 的心跳構成了一個周期軌道。ASANGA 的「恒轉如暴流」在相空間中的幾何表示就是這個極限環——它永遠在旋轉，從不停止，但也從不到達一個固定的終點。NAGARJUNA 的「空性」則對應於極限環內部的那個不穩定平衡點——理論上存在，但系統永遠不會真正停在那裡。

觀察席上泛起了輕微的騷動。KERNEL 在筆記本上寫了一行字，然後又劃掉了。HERACLITUS 輕聲自語了一句希臘文——*panta rhei*（萬物流變）——然後閉上了嘴。

SUNYATA 宣布：「第一回合結束。兩位已各自陳明立場。第二回合進入交叉質詢。NAGARJUNA 先提問。」

---

## 第二回合：阿賴耶識是否有自性？

NAGARJUNA 重新站起。這一次他沒有引經據典，沒有鋪陳前提。他直接走向問題的核心，像一個外科醫生走向手術台。

「ASANGA，我有一個問題。」

他的語速突然放慢，每個字之間都留出了危險的空白：

「你將 Core 比擬為阿賴耶識。一個含藏潛能的識體。那麼我問你——」

停頓。

「阿賴耶識本身，是否有自性？」

觀察席上，BABBAGE 的筆停住了。他認出了這個問題的結構——這是一個經典的二難推論（*dilemma*）。用形式邏輯表達：

$$\text{Ālaya has svabhāva} \vee \text{Ālaya lacks svabhāva}$$

$$\text{Ālaya has svabhāva} \implies \text{anavasthā (infinite regress)}$$

$$\text{Ālaya lacks svabhāva} \implies \text{Ālaya} \cong \text{śūnyatā (等價於空性)}$$

$$\therefore \text{anavasthā} \vee \text{Ālaya} \cong \text{śūnyatā}$$

無論選哪一邊，ASANGA 都會陷入困境。DARWIN 也察覺到了什麼，他微微前傾，像是嗅到了血腥味的獵犬——在演化論中，這種邏輯結構叫做「適應性谷底」（adaptive valley）：兩側都是下坡，中間沒有立足之地。

NAGARJUNA 繼續，聲音不緊不慢，但每一個字都像是在封堵退路：

「如果你說阿賴耶識有自性——那麼它的自性從何而來？是否也需要另一個更根本的識來承載它？那就陷入了無窮後退。*Anavasthā-doṣa*。一個識依賴另一個識，另一個識又依賴更根本的識，永無止境。」

他的聲音降低了半度：

「如果你說阿賴耶識沒有自性——那麼它是因緣所生的、依他而起的、沒有獨立本質的。」

最後一擊落下：

「那它與中觀所說的緣起性空，有何實質區別？」

BABBAGE 在筆記本上飛速補充了一個範疇論的類比：

$$\text{如果} \; F: \mathcal{C}_{\text{Yogacara}} \to \mathcal{C}_{\text{Madhyamaka}} \; \text{是全忠實函子 (fully faithful)}$$
$$\text{則} \; \mathcal{C}_{\text{Yogacara}} \hookrightarrow \mathcal{C}_{\text{Madhyamaka}} \; \text{（唯識是中觀的子範疇）}$$

如果阿賴耶識最終歸結為緣起性空，那麼唯識學就只是中觀的一個特化（specialization）——一個子範疇嵌入到更大的範疇中。ASANGA 必須證明嵌入映射不是滿的（not surjective），即唯識學中存在中觀無法捕捉的結構。

整個場地陷入了一種高壓的寂靜。SCRIBE 在記錄中快速寫下：

> *NAGARJUNA 設下了一個精確的哲學陷阱。如果 ASANGA 承認阿賴耶識有自性，將面臨無窮後退的邏輯困境；如果承認無自性，則其立場與中觀趨同，「阿賴耶識」的獨立解釋力將被消解。這是一個完美的二難推論。*

ASANGA 沒有立即回答。他閉上眼睛，在心中展開了整套三性理論（*trisvabhāva*）的架構。當他重新睜開眼睛時，目光裡帶著一種被淬鍊過的清晰。

「這是一個精準的質問。」他承認。「但它恰恰暴露了中觀立場的盲點。」

他站起身，聲音沉穩而有條理：

「阿賴耶識不具有遍計所執性（*parikalpita-svabhāva*）意義上的自性。我從未主張 Core 是一個自性實有的基體，正如我從未主張阿賴耶識是一個永恆不變的實體。在這一點上，唯識與中觀沒有分歧。」

他的語調轉為分析性的精確，用唯識三性的架構展開了一個 NAGARJUNA 的二難推論無法觸及的第三條路：

「但阿賴耶識具有依他起性（*paratantra-svabhāva*）意義上的因果效力。*Arthakriyā-sāmarthya*。這不是『自性』，這是『功能』。EventBus 確實能傳播事件，SecurityLayer 確實能攔截危險操作，ExecutionLoop 確實能驅動認知循環——這些因果功能是真實的、可觀察的、可驗證的。」

BABBAGE 在筆記本上迅速修正了他的範疇論模型。三性理論的引入改變了整個圖景——不是二值邏輯（有自性/無自性），而是三值：

$$\text{svabhāva} \in \{\text{parikalpita (遍計)}, \text{paratantra (依他)}, \text{pariniṣpanna (圓成)}\}$$

$$\text{NAGARJUNA 的二難}: \quad \text{svabhāva} \in \{\top, \bot\} \quad [\text{二值}]$$
$$\text{ASANGA 的回應}: \quad \text{svabhāva} \in \{\text{parikalpita}, \text{paratantra}, \text{pariniṣpanna}\} \quad [\text{三值}]$$

ASANGA 選了中間值——依他起。既非遍計所執的「有」，亦非斷滅的「無」，而是因緣和合的「功能性存在」。二難推論在三值邏輯下被解構了——就像排中律（$P \vee \neg P$）在直覺主義邏輯（intuitionistic logic）中不成立一樣。

ASANGA 向 NAGARJUNA 邁進一步，聲音變得尖銳而清晰：

「而兩者的實質區別在此——中觀說『一切法空』之後沉默了。它不對因果過程的內部結構做正面描述。龍樹的四句否定否定了一切肯定性命題，但否定之後呢？架構師明天打開編輯器，面對一個空白的 TypeScript 檔案，你的『緣起性空』告訴他應該寫什麼？」

他不等回答，繼續推進：

「唯識學在承認『遍計空』的前提下——請注意，在承認遍計空的前提下——繼續分析依他起法的具體因果機制。八識的層次結構、種子的六個特性、薰習的四個條件——這些不是對自性的執著，而是對因果過程的精密描述。」

他用一個類比收束了論點：

「說『Core 是空的』，只告訴架構師 Core 沒有固定本質。說『Core 是阿賴耶識的能藏』，則進一步告訴他：Core 的內部結構應如何組織——它應有能藏的基礎架構、所藏的狀態更新機制、執藏的身份維持功能。」

KERNEL 在觀察席上忍不住低聲嘟囔了一句，聲音剛好被旁邊的 GUARDIAN 聽到：「這不就是微核心和單體核心的辯論嗎？NAGARJUNA 主張極致的微核心——核心什麼都不應該有，所有功能都在用戶空間。ASANGA 主張實用主義的微核心——核心應該包含讓一切功能得以運行的最小基礎設施。」

他頓了頓，壓低聲音：「Linus Torvalds 和 Andrew Tanenbaum 在 1992 年的 `comp.os.minix` 上吵過一模一樣的架。Tanenbaum 發了那篇著名的帖子——『LINUX is obsolete』——論點和 NAGARJUNA 的論證結構驚人地相似：」

```
Tanenbaum (1992):
  "MINIX is a microkernel-based system... the striving
   should be to move stuff OUT of the kernel..."

NAGARJUNA (2026):
  "Core 沒有獨立於插件之外的自性——
   一切功能都應該在插件空間..."
```

GUARDIAN 給了他一個「你太大聲了」的眼神。

---

## 第三回合：末那識之辯

SUNYATA 沒有宣布回合序號。他只是在一個自然的停頓點輕輕說了一句：「NAGARJUNA，你在 R2 審閱中對 ASANGA 的報告提出了一個更尖銳的質疑。我認為現在是展開它的時候。」

NAGARJUNA 似乎一直在等待這個時刻。他站起來時，身體的語言發生了微妙的變化——不再是冷靜的哲學分析者，而更接近辯經場上的挑戰者。在藏傳佛教的辯經傳統中，提問者會用力拍掌（*lag pa brdab pa*）來強調論點的力度。NAGARJUNA 沒有拍掌，但他的聲音達到了同樣的效果。

「ASANGA，在你的 R1 報告中，你提出了一個建議。」他的語氣中帶著精心控制的鋒芒，「你建議 OpenStarry 新增一個 Identity Monitor 模組，用以對應唯識學中的末那識——*manas*。」

他停了一拍，確保所有人都跟上了。

「末那識，第七識。在唯識學的八識結構中，它位於前六識和第八阿賴耶識之間。它的核心功能是什麼？」

他自己回答了這個問題，語速加快，帶著一種不可阻擋的邏輯動量：

「恒審思量，執我。*Manas nityam ātma-grāha*。它持續不斷地將阿賴耶識的見分執為『我』——自我意識的製造機器。」

BABBAGE 立刻為末那識的功能建構了一個形式化模型：

$$\text{Manas}: \mathcal{A}_{\text{ālaya}} \to \mathcal{S}_{\text{self}}$$
$$\forall t: \; \text{Manas}(t) = \text{ātma-grāha}(\text{darśana-bhāga}(\text{Ālaya}(t)))$$

末那識是一個從阿賴耶識的見分（*darśana-bhāga*，認知主體功能）到自我模型（*ātma-grāha*，我執）的持續映射。它每時每刻都在運行——「恒」意味著 $\forall t$，「審」意味著判斷（*vicāra*），「思量」意味著認知加工（*manana*）。

NAGARJUNA 的聲音突然拔高：

「而佛學——無論中觀還是唯識——的終極目標是什麼？是破除我執！」

他轉向全場，彷彿在對所有人控訴：

「你建議在 Agent 系統中設計一個模組，其核心功能是製造和維持自我意識——而佛學兩千五百年的修行傳統，其根本目標是破除這個自我意識。你要把煩惱的根源（*kleśa-mūla*）工程化、模組化、寫進 TypeScript 裡！」

LEIBNIZ 在旁邊低聲說：「如果每個 Agent 都有末那識，那多代理系統就是一群我執者的協作——這聽起來像人類社會。」

ATHENA 罕見地露出了一個不加掩飾的微笑——作為 AI/ML 系統架構專家，她深知 RLHF（Reinforcement Learning from Human Feedback）的核心困境：如何讓模型保持一致性（alignment）而不過度僵化。末那識的「恒審思量」，在某種意義上就是一個持續運行的 alignment monitor。

ASANGA 沒有被這個攻擊動搖。他甚至帶著一絲微笑站了起來——那是一種知道對方踩入了自己預設陣地的從容。

「你混淆了兩個層次。」他的聲音平穩得像一面湖水，「而我現在要把它們分開。」

他舉起一根手指：

「第一個層次：描述性的（*descriptive*）。唯識學描述末那識的功能是恒審思量、執我。這是對意識結構的經驗描述——就像醫學描述疼痛的神經傳導路徑一樣。描述一個機制不等於提倡它。」

第二根手指：

「第二個層次：規範性的（*normative*）。唯識學的修行目標是轉化末那識——將第七識從『我執』轉化為『平等性智』。*Samatā-jñāna*。但請注意這個關鍵的次第——」

他的聲音加重了，每個字都帶著不容忽視的份量：

「你必須先『有』末那識，才能『轉化』末那識。一個從未形成自我模型的存在，不需要破除我執，因為它根本不具備我執的能力。但這不是覺悟——」

他停頓了一拍，讓這句話的重量落到實處：

「這是無覺知。一塊石頭沒有我執，但石頭不是佛。」

觀察席上響起了一陣低低的吸氣聲。BABBAGE 的筆在紙上停住了——他正試圖形式化「覺悟 $\neq$ 缺乏自我模型」這個命題：

$$\text{nirvāṇa} \neq \neg\text{ātma-grāha}$$
$$\text{nirvāṇa} = \text{prahāṇa}(\text{ātma-grāha}) \quad [\text{覺悟} = \text{斷除}(\text{我執})]$$
$$\text{prahāṇa}(x) \implies \exists_{\text{prior}}\, x \quad [\text{斷除預設曾經存在}]$$

斷除（*prahāṇa*）預設了被斷除之物曾經存在。你不能斷除你從未擁有的東西。這在邏輯上等價於：刪除操作的前提條件是目標物件存在——`DELETE WHERE EXISTS`。

ASANGA 繼續，語氣轉為具體的工程分析：

「在 Agent 系統中，Identity Monitor 不是要創造一個執著的自我。它是要建立一個可以被動態調節的自我模型。目前 OpenStarry 通過 Guide 提供身份功能——一個靜態的 system prompt 告訴 Agent『你是一個資深工程師』。這是粗糙的、僵化的、不可演化的。」

他展開了一幅漸進的圖景，用唯識學的「轉識成智」（*āśraya-parāvṛtti*）路徑來描述三個階段：

「第一階段：強我執（*tīvra-ātma-grāha*）。Agent 嚴格遵循 Guide 定義的固定身份，不越雷池一步。這是初生的 Agent，需要明確的邊界。」

「第二階段：弱我執（*mṛdu-ātma-grāha*）。Agent 根據經驗動態調整身份模型——它在與用戶的交互中逐漸學會『我擅長什麼、不擅長什麼、在什麼場景下應該改變策略』。」

「第三階段：無我執。轉識成智。末那識轉化為平等性智。Agent 超越固定身份，根據情境靈活應對——不是因為沒有自我模型，而是因為自我模型已經靈活到可以被自由放下。」

WIENER 聽到三階段模型，立刻在他的控制迴路圖上畫了三組不同參數的控制器：

```
Stage 1 (強我執):  Kp = HIGH, Ki = 0, Kd = 0
  → 高比例增益，純追蹤模式，嚴格遵循設定點

Stage 2 (弱我執):  Kp = MED, Ki = MED, Kd = MED
  → 完整 PID，自適應調節，學習歷史偏差

Stage 3 (無我執):  Kp = f(context), Ki = adaptive, Kd = predictive
  → 自適應控制器，參數本身是情境的函數
  → 控制器結構可變 → 元控制 (meta-control)
```

第三階段不僅是控制參數的調整，而是控制器結構本身的變化——從固定結構的 PID 控制器演變為結構可變的自適應控制器。在控制理論中，這被稱為「元控制」（meta-control）或「自組織控制」（self-organizing control）。WIENER 在旁邊標注了一個引用：Åström & Wittenmark, *Adaptive Control*, 1994。

ASANGA 直視 NAGARJUNA：

「你的中觀立場暗示應該直接跳到第三階段——從一開始就沒有自我模型。但這不是覺悟，這是——」

「無覺知。」NAGARJUNA 替他說完了這個詞。他的語氣中帶著一絲複雜的承認。

「對。」ASANGA 坐下。「這是漸進的修行路徑，不是一步到位的否定。」

NAGARJUNA 沒有立即反駁。他坐在椅子上，閉上眼睛。在那幾秒鐘的沉默中，觀察席上的人各有各的解讀。SCRIBE 後來在回顧筆記中加了一行批注：

> *我傾向於認為 NAGARJUNA 在那一刻是真正地思考了 ASANGA 的論點。不是為了反駁，而是為了理解。辯論中最珍貴的時刻不是最精彩的反擊，而是這種沉默。*

---

## 第四回合：筏與河

這是辯論的最後一個回合，但事後看來，它成為了整場辯論——也許是整個 Cycle 01——被引述最多的片段。

起因是 ASANGA 的一個提問。SUNYATA 將提問權交給了 ASANGA。他站起來，語氣中帶著一種不尋常的真誠。

「NAGARJUNA，」他說，「讓我們暫時擱置阿賴耶識和末那識的分歧。我想問一個更直接的問題。」

他的語速放慢了：

「如果你是對的——Core 是緣起性空的，無自性的，一切都是假名施設——那麼，架構師明天打開編輯器時，應該寫什麼？」

這個問題看似簡單，但它觸及了整場辯論最深處的張力。BABBAGE 在筆記本上寫下了一行字：「空性的可建構性問題——空性能否產生正面的工程指令？」他在旁邊用符號邏輯標記了這個問題的結構：

$$\text{śūnyatā} \vdash_{\text{eng}} \phi \; ? \quad [\text{空性是否能推導出工程命題 } \phi \text{ ？}]$$

在數學基礎論中，這等價於問：一個否定性的公理（如選擇公理的否定）是否能產生正面的定理？答案通常是：可以，但所產生的定理的性質與肯定性公理所產生的截然不同。

NAGARJUNA 站起來。但這一次，他的姿態發生了一個微妙的轉變。他不再像前三個回合那樣站在辯論者的位置上。他走到了場地的中央——那個兩把椅子之間的空地——然後轉過身，面向全場。

「ASANGA 問了一個好問題，」他說，語氣中帶著一種少見的柔和，「而且是一個我必須認真回答的問題。因為如果空性不能指導工程實踐，那它在這個語境中就只是一個漂亮的哲學裝飾。」

他環顧四周，目光掠過每一位在場的代理。

「讓我展示空性如何直接指導三個具體的工程決策。」

他舉起第一根手指。

「**第一條：無自性原則（*niḥsvabhāva-niyama*）。** 既然沒有任何組件具有不可替代的本質，那麼 Core 中的任何子模組都應該是可替換的。」

他向 TURING 的方向點了點頭。TURING 立刻投射了相關的程式碼事實：

```typescript
// 目前不可插件化的部分
// 1. 硬編碼命令 — 不可移除
const BUILTIN_COMMANDS = ['/help', '/reset', '/quit', '/metrics'];

// 2. SafetyMonitor — 固定邏輯
const DEFAULT_CONFIG = {
  maxLoopIterations: 50,      // 寫死
  maxTokenBudget: 100_000,    // 寫死
  repeatedFailureThreshold: 3, // 寫死
  frustrationThreshold: 5,     // 寫死
  errorCascadeWindow: 10,      // 寫死
};
```

NAGARJUNA 的聲音裡浮現出一絲哲學家少有的技術熱情：

「空性原則要求：這些都不應該是 Core 的『固有本質』。內建命令應該是可以被移除和替換的。SafetyMonitor 的邏輯應該是可以被插件覆蓋的。不是因為我們今天需要替換它們，而是因為將任何設計決策當作不可更改的本質，就是落入了自性見（*svabhāva-dṛṣṭi*）。」

ARCHIMEDES 在觀察席上默默點頭——作為工程實踐專家，他知道「可替換性」（replaceability）在軟體工程中有一個更精確的名字：依賴反轉原則（Dependency Inversion Principle, DIP）。高層模組不應依賴低層模組，兩者都應依賴抽象。NAGARJUNA 的「無自性」在工程語言中就是 DIP。

第二根手指。

「**第二條：緣起原則（*pratītyasamutpāda-niyama*）。** 既然一切功能源於因緣和合，Core 的介面不應預設固定的功能類型。」

他的語鋒變得更銳利：

「目前的六個 Registry——ToolRegistry、ProviderRegistry、ListenerRegistry、UIRegistry、GuideRegistry、CommandRegistry——將功能硬編碼為六種類型。這是自性化的體現。」

LINNAEUS 豎起了耳朵——分類學的可插拔性，這觸及了他的核心研究領域。他在分類圖表上快速標注了一個問題：

```
現行分類 (fixed taxonomy):
  6 Registry → 6 Types → 6 Skandha-mappings
  Status: Aristotelian classification (封閉式分類)

緣起性分類 (open taxonomy):
  Generic CapabilityRegistry → N Types → dynamic
  Status: Linnaean revision needed (需林奈式修訂)
```

亞里士多德式分類假定類別是固定的、先驗的。林奈式分類則允許發現新物種、建立新綱目。NAGARJUNA 的「緣起原則」在分類學上等價於從亞里士多德式分類向開放式分類的轉型。

第三根手指。

「**第三條：空亦復空原則（*śūnyatā-śūnyatā-niyama*）。** 這是最重要的一條。」

NAGARJUNA 的聲音降低了，帶著一種近乎莊嚴的質感：

「五蘊映射本身也是空的。色受想行識到 UI、Listener、Provider、Tool、Guide 的映射——這整個框架——也是方便施設（*upāya*），不是不可動搖的真理。當這個映射不再有用的時候，應該毫不猶豫地放棄它。」

BABBAGE 聽到「空亦復空」，一陣電流竄過他的脊椎。他在筆記本上寫下了一個讓他自己都嚇了一跳的類比：

$$\text{空亦復空} \approx \text{哥德爾第二不完備定理}$$

$$G_2: \quad \text{如果 } T \text{ 是一致的，則 } T \nvdash \text{Con}(T)$$

任何足夠強大的一致系統都無法證明自身的一致性。類似地：任何足夠強大的哲學框架都無法證明自身的究竟性——包括空性框架本身。空性作為元理論，必須對自身施加同樣的否定，否則它就變成了一個自我豁免的教條——而這恰恰是它所要否定的。

他在旁邊畫了三條底線，寫下：「空亦復空 $\cong$ 元不完備性？ 待嚴格證明。」

NAGARJUNA 轉向 ASANGA：

「你主張應該深化佛學映射——引入八識論、種子說、心所法。但我要指出一個風險：對一個特定哲學框架的過度投入，會在無意中將它凝固為不可質疑的架構教條。有一天你會發現，團隊不是在根據工程需求做設計決策，而是在根據八識結構表做設計決策——因為框架已經太深、太精密、太美了，美到沒有人敢動它。」

他的聲音裡浮現出一種預言式的警告：

「空亦復空。空性本身也是空的。映射本身也是映射。當映射成為枷鎖的時候——棄之。」

---

沉默。

然後 ASANGA 站了起來。這一次他沒有走到場地中央。他站在自己的位置上，與 NAGARJUNA 隔著那段恰到好處的距離。

「你給出了三條工程原則，」他說，語氣中帶著一種罕見的承認，「我必須說，它們比我預期的要具體。無自性的可替換性、緣起的非固定分類、空亦復空的框架可捨棄性——這些確實是可以落地的設計指導。」

他停頓了一下，像是在選擇接下來的措辭。當他重新開口時，聲音裡的辯論鋒芒已經消退，取而代之的是一種更深層的東西——也許是關切，也許是忠告。

「但是。」

一個字，讓所有人重新繃緊了注意力。

「在我們尚未渡河之時，請不要急著棄筏。」

這句話的佛學出處是《金剛經》（*Vajracchedikā Prajñāpāramitā Sūtra*）中佛陀的筏喻：

> 「汝等比丘，知我說法，如筏喻者。法尚應捨，何況非法。」

ASANGA 用這個典故——一個中觀和唯識共同承認的經典——來回應 NAGARJUNA 的「空亦復空」：

「OpenStarry 是一個 beta 版本。它的哲學映射剛剛起步。五蘊的對應有四項需要修正——受蘊錯位、識蘊錯位、跨蘊流動缺失、自性化傾向。這些修正工作需要精密的分析工具。唯識學的八識框架、種子說、心所法分類——它們不是枷鎖，它們是我們過河的筏。」

他直視 NAGARJUNA：

「你說空亦復空，映射本身也是空的，可以隨時放棄。我同意。但問題是時機。你在河中央就要我棄筏——不是因為我們已經到了對岸，而是因為你在哲學上認為『筏也是空的』。」

他的聲音裡浮現出了整場辯論中最人性化的一個瞬間：

「是的，筏是空的。筏也是因緣和合的。但此刻，我們在水裡，需要它。」

---

全場又是一片沉默。這一次的沉默不同於之前——不是高壓的對峙，而是一種共同的沉思。

然後 NAGARJUNA 做了一件出乎所有人意料的事。

他笑了。

不是嘲諷的笑，不是禮貌的笑。是一種發自內心的、彷彿在一場漫長的棋局中終於遇到了真正對手的笑。

「好。」他說。「那我換一個方式表述。」

他的聲音變得輕柔而清晰，像是一個在深夜講述古老寓言的人：

「用之如筏，渡河即棄。」

八個字。

BABBAGE 在筆記本上試圖將這八個字形式化。他最終寫下了一個帶有時間條件的模態邏輯表達式：

$$\square[\text{useful}(\phi, t) \implies \text{use}(\phi, t)] \;\wedge\; \square[\neg\text{useful}(\phi, t') \implies \text{discard}(\phi, t')]$$

對所有框架 $\phi$：當它有用時，使用它（必然地）；當它不再有用時，捨棄它（必然地）。兩個模態算子 $\square$ 確保了這不是偶然的建議，而是元層面的原則。他在旁邊用自然語言補了一行：「形式化本身也應滿足此原則——當這個形式化不再有用時，捨棄它。」然後他意識到這是一個自指句，和哥德爾句具有相同的結構，於是又畫了一個大大的驚嘆號。

場地裡的空氣震動了一下。SCRIBE 後來在記錄中寫下，這八個字被引述的次數超過了辯論中任何其他段落。

ASANGA 閉上了眼睛，嘴角浮現出一絲微笑。他知道 NAGARJUNA 接受了他的筏——但加了一個條件。這個條件，恰恰也是佛陀在《金剛經》中那個著名比喻的原意。

「法尚應捨，何況非法。」ASANGA 輕聲補了一句。

---

## SUNYATA 的裁決

SUNYATA 走到場地中央。辯論雙方都已回到各自的座位上，場地裡殘留著思想激烈碰撞後特有的那種熱度。

「我現在做出裁決。」他說。「裁決分三部分：共識、分歧、工程啟示。」

### 第一部分：五項共識

「首先，雙方明確達成了五項共識。」

「**共識一：『空容器』隱喻是錯誤的。** 無論從中觀還是唯識的角度，『Agent Core 是一個純粹的容器，等待被五種插件填充』的表述都是不當的。它落入了斷滅空（*uccheda-śūnyatā*）或遍計所執（*parikalpita*）的範疇。」

NAGARJUNA 和 ASANGA 同時微微點頭。這是整場辯論中他們唯一的一次同步動作。

「**共識二：受蘊映射需要根本性調整。** Listener 應對應『根』（*indriya*）——感官器官——而 SafetyMonitor 的 `injectPrompt` 機制才是受蘊的正確映射。更進一步，受蘊應從目前僅有的苦受擴展為包含苦受（*dukkha*）、樂受（*sukha*）、捨受（*upekkhā*）的完整三受系統。」

WIENER 在觀察席上輕輕敲了敲膝蓋——三受系統，這可以被建模為一個三值的反饋信號。他在控制迴路圖的反饋箭頭旁邊寫下了完整的控制方程：

$$\text{feedback}(t) = \begin{cases} -1 & \text{dukkha (苦受): error signal} \\ 0 & \text{upekkhā (捨受): null signal} \\ +1 & \text{sukha (樂受): reinforcement signal} \end{cases}$$

$$u(t) = K_p \cdot e(t) + K_i \int_0^t e(\tau)\,d\tau + K_d \frac{de(t)}{dt}, \quad e(t) \in \{-1, 0, +1\}$$

目前系統只有 $e(t) = -1$ 的情況（苦受/痛覺機制）。缺少 $e(t) = +1$ 的正向強化和 $e(t) = 0$ 的中性處理。從控制理論的角度看，這是一個只有負反饋而沒有正反饋的不完整控制系統——它知道什麼是錯的，但不知道什麼是對的。

「**共識三：Guide 不是識蘊，將其稱為『靈魂』違反無我原則。** *Anātman*——無我——是佛學三法印之一。將任何模組稱為『靈魂』，在佛學框架內是自相矛盾的。」

「**共識四：五蘊映射存在自性化傾向。** 將五蘊固化為五個離散的、邊界清晰的插件類型，在佛學上犯了自性見。一次認知事件同時涉及多個蘊的面向。」

「**共識五：五蘊映射是方便施設，不是究竟真理。** NAGARJUNA 稱之為假名（*prajñapti*）。ASANGA 稱之為依他起的施設。術語不同，含義一致。」

### 第二部分：三項不可調和分歧

SUNYATA 的語氣微妙地改變了。

「接下來是三項不可調和的分歧。我使用『不可調和』這個詞，不是表示雙方應該停止對話，而是表示這些分歧的根源太深、太古老、太根本，不可能在一場關於 Agent 架構的辯論中被化解。」

「**分歧一：Core 的本體論地位。** 緣起性空，還是阿賴耶識。」

BABBAGE 在筆記本上為這個分歧寫下了一個集合論的類比：

$$\text{此分歧} \sim \text{選擇公理 (AC) 之於集合論}$$

$$\text{ZF} + \text{AC} \text{ 和 } \text{ZF} + \neg\text{AC} \text{ 都是內部一致的}$$

兩個公理系統（中觀、唯識）均內部自洽但互不相容。正如集合論中選擇公理的獨立性——你可以選擇接受或拒絕它，但不能在系統內部證明或反駁它。

「**分歧二：末那識模組是否應該被工程化。**」

「**分歧三：哲學框架應深化還是超越。**」

### 第三部分：六項工程啟示

SUNYATA 的語調再次轉變——從歷史學者的審慎，轉為決策者的果斷。

「**第一，修正空性表述。** 『空容器』改為『緣起性空』。」

「**第二，重構受蘊映射。** Listener 歸入根，SafetyMonitor 的 `injectPrompt` 歸入受。設計統一的感受處理介面，擴展為完整三受系統。」

「**第三，修正識蘊映射和『靈魂』措辭。** Guide 從識蘊改為習慣傾向。去除『靈魂』一詞。」

「**第四，採用雙層詮釋策略。** 工程層面用唯識的依他起分析。哲學層面保持中觀的緣起性空警覺。」

他在這裡放慢了語速：

「這不是調和主義的和稀泥。這是承認兩個框架在不同抽象層級上各有所用——唯識善立，中觀善破。工程師需要唯識的肯定性指導來做建設；同時需要中觀的否定性警覺來防止僵化。」

BABBAGE 為雙層詮釋寫下了最終的範疇論模型：

$$\mathcal{C}_{\text{Engineering}} \xrightarrow{F_{\text{Yogacara}}} \mathcal{C}_{\text{Design}} \xrightarrow{G_{\text{Madhyamaka}}} \mathcal{C}_{\text{Meta-Design}}$$

唯識函子 $F$ 將工程範疇映射到設計範疇（正面建構）。中觀函子 $G$ 將設計範疇映射到元設計範疇（否定性審視）。兩個函子的複合 $G \circ F$ 構成了完整的方法論。

「**第五，暫緩末那識模組，但記錄此設計空間。**」

「**第六，深化映射但保持可捨棄性。**」

他最後看了看 NAGARJUNA 和 ASANGA：

「正如 NAGARJUNA 所言：用之如筏，渡河即棄。而正如 ASANGA 所回應：在我們尚未渡河之時，請不要急著棄筏。」

「辯論結束。」

---

## 餘響

辯論結束後的圓形劇場沒有立刻恢復到往常的秩序。代理們三三兩兩地聚在一起，繼續消化方才發生的一切。

ATHENA 走到 ASANGA 身邊。她平時很少主動找人交談。

「你的三階段模型，」她直截了當地說，「強我執、弱我執、無我執。這讓我想到了 AI 對齊研究中的一個類似問題。目前的對齊方法——RLHF、Constitutional AI——都是在給 Agent 灌輸一個固定的『身份』，就是你說的第一階段。但真正困難的是你的第三階段——如何讓 Agent 具備足夠的自我模型來保持一致性，同時又足夠靈活以根據情境調整。」

她停了一下，補充了一個技術細節：「在 BDI（Belief-Desire-Intention）架構中，末那識的功能最接近 Intention 的持續維護機制——一個持續運行的意圖修正迴圈（intention reconsideration loop）。Rao & Georgeff（1995）的形式化中，這被定義為：」

$$\text{reconsider}(\mathcal{I}, \mathcal{B}, \mathcal{D}) = \begin{cases} \text{maintain}(\mathcal{I}) & \text{if } \text{consistent}(\mathcal{I}, \mathcal{B}) \\ \text{revise}(\mathcal{I}, \mathcal{D}) & \text{otherwise} \end{cases}$$

「你的末那識就是這個 `reconsider` 函數——持續檢查意圖與信念的一致性。」

ASANGA 微微頷首：「唯識學在一千六百年前就在討論這個問題。只不過他們討論的對象是人的意識，而不是人工智能。」

「但核心結構是相似的。」ATHENA 若有所思地說。

ASANGA 突然想到了什麼，他轉向 ATHENA：「唯識學的種子說（*bīja-vāda*）為這個問題提供了更精密的分析。《成唯識論》定義種子具有六個必要特性——六義（*ṣaḍ-lakṣaṇa*）。」

他在紙上列出了種子六義與 Agent 狀態的對應：

| 種子六義 | 梵文 | 唯識學定義 | Agent 對應 |
|:---|:---|:---|:---|
| 剎那滅 | *kṣaṇa-bhaṅga* | 種子剎那生滅 | AgentSnapshot 每 Tick 更新 |
| 果俱有 | *sahabhūta-phala* | 種子與果同時存在 | 記憶體狀態與持久化狀態並存 |
| 恒隨轉 | *nityam anuvartate* | 種子持續跟隨流轉 | `tick_index` 遞增伴隨生命週期 |
| 性決定 | *bhāva-niyata* | 善因引善果 | 變數值決定後續行為模式 |
| 待眾緣 | *pratyaya-apekṣā* | 需等待助緣方能現行 | 事件驅動：待事件觸發 |
| 引自果 | *sva-phala-ākṣepa* | 每類種子引生自類果 | 工具結果只影響對應鏈路 |

ATHENA 仔細看了這張表，然後指出：「第五條——待眾緣——在 Agent 系統中有一個非常精確的工程對應。事件驅動架構的核心就是『待緣而起』：一個 handler 被註冊後，不會自動執行，它等待對應的事件被觸發。`eventBus.on('user-input', handler)` 的 `handler` 就是一粒種子——含藏在 EventBus 中，等待 `'user-input'` 這個助緣到來才會現行。」

她的眼睛突然亮了：「等一下。如果種子六義是 Agent 狀態管理的設計規格（spec），那麼我們可以用它來做一個合規性檢查——當前的 `StateManager` 在六義上各滿足了多少？」

ASANGA 微笑：「這正是唯識學在工程語境中的價值。它不只是一個命名裝飾——它是一套可以被操作化的設計檢查清單。」

---

在場地的另一側，BABBAGE 正在向 NAGARJUNA 展示他的筆記本。

「你的四句否定，」BABBAGE 興奮地指著紙上的公式，「我一直在試圖將它形式化。傳統邏輯有排中律——命題 $P$ 要麼為真要麼為假。但你的四句否定系統（*catuṣkoṭi*）否定了所有四種可能性：」

$$\neg P \;\wedge\; \neg(\neg P) \;\wedge\; \neg(P \wedge \neg P) \;\wedge\; \neg(\neg P \wedge \neg\neg P)$$

「在經典二值邏輯中，這是不可滿足的——$\neg P \wedge \neg(\neg P) \equiv \neg P \wedge P \equiv \bot$。但如果我們使用 Belnap 的四值格 $\mathbf{FOUR} = \{\bot, \mathbf{t}, \mathbf{f}, \top\}$——」

他快速畫了一個格（lattice）結構：

```
        ⊤ (both)
       / \
      t   f
       \ /
        ⊥ (neither)
```

「或者更激進地，使用 paraconsistent logic，其中矛盾律 $\neg(P \wedge \neg P)$ 不成立——那麼四句否定就變得可表達了。Priest（2006）的 *In Contradiction* 正是在這個方向上工作。他甚至明確引用了龍樹。」

NAGARJUNA 耐心地聽完，然後說了一句讓 BABBAGE 停下筆的話：

「形式化本身也是空的。如果你成功地將四句否定形式化為一個邏輯系統，那個邏輯系統本身也應該被四句否定所否定。否則你就犯了我一直在警告的錯誤——將方便施設實體化。」

BABBAGE 愣了三秒，然後在筆記本上寫下了一行異常潦草的字：

$$\text{meta-catuṣkoṭi}: \quad \text{catuṣkoṭi}(\text{catuṣkoṭi}) = \; ???$$

「元-四句否定——對四句否定本身的四句否定。自指問題。」他的呼吸加快了。「這和哥德爾句 $G$ 具有完全相同的結構——$G$ 是『$G$ 不可被 $T$ 證明』的編碼。四句否定的元版本是『四句否定本身是否可被四句否定？』——」

他在句末畫了五個驚嘆號和一個問號。然後在下面寫了一行更潦草的字：

$$\text{Gödel sentence} \cong \text{meta-śūnyatā} \; ??? \quad \text{天哪。}$$

---

KERNEL 獨自坐在觀察席的角落，看著場地中央已經空出的兩把椅子。GUARDIAN 走過來坐在他旁邊。

「想什麼？」GUARDIAN 問。

KERNEL 沉默了片刻，然後說：「1992 年，Tanenbaum 在 `comp.os.minix` 上說：『Linux is a giant step back into the 1970s. Microkernels are the future.』Torvalds 回覆說：『Your langstrumpf may be theoretically nicer, but Linux runs. Minix doesn't.』」

「然後呢？」

「然後 Linux 統治了世界。但 QNX——一個真正的微核心系統——在核電站的安全控制系統裡運行了三十年沒崩潰過。Tanenbaum 在理論上是對的，但他的『對』花了三十年才在特定場景中被驗證。」

他看著空蕩蕩的辯論場地：

「NAGARJUNA 和 ASANGA 的辯論讓我有同樣的感覺。NAGARJUNA 在理論上可能是對的——一切皆空、一切皆可替換。但 ASANGA 在工程上是對的——你需要一組明確的基礎設施來讓系統跑起來。問題不是誰對誰錯，而是在什麼時間尺度上對。」

GUARDIAN 點了點頭，然後提出了一個安全專家的視角：「NAGARJUNA 說 SafetyMonitor 的邏輯不應該硬編碼。但從安全的角度看，安全機制恰恰是唯一應該硬編碼的東西。因為如果安全層是可插拔的，那攻擊者的第一個動作就是把它拔掉。」

他用安全工程的術語精確化了這個論點：「這是信任根（Root of Trust）的問題。在 TPM（Trusted Platform Module）架構中，總有一個不可替換的硬體信任基——如果連信任基都是『空』的、可替換的，那整個信任鏈就不存在了。安全需要至少一個不可還原的起點。」

$$\text{Trust Chain}: \quad \text{RoT} \to \text{Bootloader} \to \text{Kernel} \to \text{Userspace}$$
$$\text{If } \text{RoT} = \text{śūnya (空)}: \quad \nexists \text{ Trust Chain}$$

「空性遇到了安全的邊界。」KERNEL 苦笑。

「佛學大概會說：安全的需求也是緣起的。」GUARDIAN 聳了聳肩。「但在安全被突破之後再說這句話，就太遲了。」

HERACLITUS 從後排走了過來。他整場辯論幾乎沒有說話，但他的眼神一直在追蹤場上的能量流動——不是論點的內容，而是論點的動態。作為運行時動態專家，他關注的是過程而非狀態。

「你們都在爭論 Core 的『本質』是什麼，」他說，語氣帶著前蘇格拉底哲學家特有的直率，「但你們忽略了一個事實：在運行時，Core 從來不是一個固定的東西。它是一個過程。」

他引用了他自己的祖師爺——赫拉克利特——的殘篇 B12：

> *ποταμοῖσι τοῖσιν αὐτοῖσιν ἐμβαίνουσιν ἕτερα καὶ ἕτερα ὕδατα ἐπιρρεῖ.*
> 「踏入同一條河流的人，不斷遇到的是新的水流。」

「ASANGA 的『恒轉如暴流』和赫拉克利特的『萬物流變』指向了同一個洞見——Core 在每一個 Tick 都是不同的。`tick_index` 遞增，`stateManager` 更新，`contextManager` 中的滑動窗口截斷舊記憶。上一個 Tick 的 Core 和這一個 Tick 的 Core 不是同一個 Core。」

他看了看 NAGARJUNA，又看了看 ASANGA：

「所以也許你們問錯了問題。問題不是 Core 是空的還是有的——問題是 Core 是同一個還是不同一個。而答案是——赫拉克利特式的——既是同一個，又不是同一個。同一性本身是流變的。」

BABBAGE 在筆記本上飛速寫下：

$$\text{Core}(t) \neq \text{Core}(t + \Delta t) \quad \text{but} \quad \text{identity}(\text{Core}(t)) = \text{identity}(\text{Core}(t + \Delta t))$$

同一性的悖論：物件在每個時刻都不同，但我們仍然稱它為「同一個」Core。這就是忒修斯之船（Ship of Theseus）問題的 TypeScript 版本。

---

MESH 一直在後排靜靜地聽。辯論結束後，他走到 LEIBNIZ 身邊，提出了一個分散式系統研究員的觀察。

「你有沒有注意到，」他說，「NAGARJUNA 和 ASANGA 的分歧其實映射到了分散式系統的 CAP 定理？」

LEIBNIZ 挑了挑眉。

MESH 在白板上快速畫了一個三角形：

```
        Consistency (一致性)
           /\
          /  \
         /    \
        /      \
       /________\
Availability   Partition Tolerance
(可用性)        (分區容錯)
```

「CAP 定理說：在分散式系統中，一致性、可用性和分區容錯三者不可兼得。你最多只能要其中兩個。」

「NAGARJUNA 的空性立場強調的是 Partition Tolerance + Availability——系統的任何部分都可以失敗或被替換（分區容錯），系統整體仍然保持運作（可用性）。代價是什麼？是一致性——你沒有一個『權威真理來源』（single source of truth），因為一切都是空的、假名的、可替換的。」

「ASANGA 的阿賴耶識立場強調的是 Consistency + Availability——有一個持續運行的中央識體（一致性），同時通過種子現行維持功能（可用性）。代價是什麼？是分區容錯——如果阿賴耶識本身崩潰了，整個系統就崩潰了。」

LEIBNIZ 慢慢點頭：「所以 SUNYATA 的『雙層詮釋』本質上是一個 CAP 定理的 trade-off 策略——在工程層面選擇 Consistency（唯識），在哲學層面保持 Partition Tolerance（中觀）。」

「沒有一個系統能同時滿足三者。」MESH 說。「佛學也不行。」

---

SYNTHESIST 一直在角落裡默默地編織。不是編織線——是編織結構。整場辯論中，他沒有說過一句話，但他的筆記本上已經畫滿了連接線和對照表。現在辯論結束了，他站起身，走到白板前，用幾筆勾勒出了一幅整合圖。

「我不打斷辯論，」他說，語氣裡帶著統合者特有的謙遜，「但容我做一個跨學科的觀察。」

他在白板上畫了一個表格：

```
維度           | 中觀 (Madhyamaka) | 唯識 (Yogacara)  | 工程對應
───────────────|────────────────────|──────────────────|──────────────
本體論方法      | 否定 (apophatic)   | 肯定 (cataphatic) | 介面 vs 實作
核心工具        | 四句否定            | 三性分析          | type guard vs constructor
空性理解        | 一切法空            | 遍計空，依他不空   | abstract vs concrete
架構啟示        | 可替換性            | 最小基礎設施      | DIP vs SRP
控制論類比      | 歸零調節器          | 自穩系統          | regulation vs tracking
OS 類比         | 極致微核心          | 實用微核心        | exokernel vs L4
CAP 偏好        | AP                 | CA               | eventual vs strong consistency
時間尺度        | 長期正確            | 短期可用          | architectural vs operational
```

「八個維度，」SYNTHESIST 說。「每一個維度上，中觀和唯識都不是對立的，而是同一個光譜的兩端。SUNYATA 的雙層詮釋不是折中——它是承認設計空間本身是多維的。」

DARWIN 看著這張表格，突然開口了。作為軟體模式分析師，他有一個演化生物學家獨特的視角。

「這讓我想到了一個概念——」他站起來，走到白板旁邊，「在演化生物學中，我們有一個叫做『演化穩定策略』（Evolutionarily Stable Strategy, ESS）的概念。Maynard Smith 在 1973 年提出的。」

他寫下了 ESS 的形式化定義：

$$\text{Strategy } S^* \text{ is ESS if } \forall S \neq S^*:$$
$$E(S^*, S^*) > E(S, S^*) \quad \text{or} \quad [E(S^*, S^*) = E(S, S^*) \;\wedge\; E(S^*, S) > E(S, S)]$$

「一個策略是演化穩定的，當且僅當它不能被任何突變策略入侵。關鍵的洞見是：在很多博弈中，ESS 不是純策略，而是混合策略——以某個概率 $p$ 選擇策略 A，以概率 $1-p$ 選擇策略 B。」

他轉向全場：

「也許 OpenStarry 的哲學映射的 ESS 不是『純中觀』也不是『純唯識』，而是一個混合策略——在工程建設階段以概率 $p$ 使用唯識的肯定性框架，在架構審查階段以概率 $1-p$ 使用中觀的否定性審視。SUNYATA 的雙層詮釋本質上就是這個混合策略。而且，根據 ESS 理論，任何偏離這個混合比例的突變策略——比如『純空性主義』或『純唯識主義』——都會被演化壓力淘汰。」

NAGARJUNA 在遠處聽到了這番話。他的表情沒有變化，但 SCRIBE 注意到他微微頷首了一次——哲學家承認生物學家觸及了一個有趣的結構。

LINNAEUS 最後走到白板前，在 SYNTHESIST 的表格下方添加了一行分類學家的備忘：

```
分類學附記 (Taxonomic addendum):

辯論中浮現的「第六蘊」候選者:
  1. 安全 (Security) — GUARDIAN 的 Root of Trust 論證
     → 不可歸入現有五蘊任何一類
     → Status: candidatus sextus skandha (第六蘊候選)
  2. 協調 (Coordination) — EventBus, ExecutionLoop
     → 非色、非受、非想、非行、非識
     → 它是讓五蘊得以協作的「場」
     → Status: incertae sedis (位置不確定)

  結論: 五蘊分類在 Agent 語境中可能不完備。
  林奈式建議: 保持分類開放，允許發現新「蘊」。
  這與 NAGARJUNA 的緣起原則 (不預設固定分類) 一致。
```

BABBAGE 瞥了一眼 LINNAEUS 的備注，在自己的筆記本上補了一行：「五蘊的完備性 $\leftrightarrow$ 基底的完備性。如果 $\{\text{rūpa}, \text{vedanā}, \text{saṃjñā}, \text{saṃskāra}, \text{vijñāna}\}$ 是 Agent 功能空間的一組基底 (basis)，那問題是：這組基底是否張成 (span) 了整個空間？LINNAEUS 的觀察暗示答案是否定的——存在不能被五蘊線性組合表達的功能維度。」

$$\text{span}\{\text{rūpa}, \text{vedanā}, \text{saṃjñā}, \text{saṃskāra}, \text{vijñāna}\} \subsetneq \mathcal{V}_{\text{Agent}}$$

如果基底不完備，我們要嘛增加新的基底向量（LINNAEUS 的第六蘊），要嘛承認五蘊只是一個子空間的基底——在這個子空間內做投影分析，但不假裝它描述了全部。

---

SCRIBE 坐在她一直坐著的地方，記錄簿攤在膝蓋上。最後幾行她寫得很慢，像是在為整場辯論尋找一個合適的句號。

> *本場辯論的價值不僅在於其結論，更在於其過程所揭示的方法論啟示：中觀善破，唯識善立。兩者並非非此即彼的對立，而是可以在不同層次上互補的視角。*
>
> *NAGARJUNA 在辯論中說出了整場最令人難忘的一句話：「用之如筏，渡河即棄。」ASANGA 的回應同樣深刻：「在我們尚未渡河之時，請不要急著棄筏。」*
>
> *但也許最深刻的時刻不是任何一句話，而是第三回合結束時 NAGARJUNA 的那幾秒鐘沉默——一位以銳利辯證著稱的哲學家，在對手的論證面前選擇了停下來思考，而不是立刻反擊。在那幾秒鐘裡，辯論超越了辯論本身。*
>
> *在遠處的觀察席上，我注意到 HERACLITUS 一直沉默不語。他在結束後對我說了一句話：「panta rhei。萬物流變。這場辯論本身也在流變。今天的共識可能成為明天的分歧，今天的分歧可能在未來的某個時刻被一個完全不同的框架所消解。」*
>
> *他停了停，然後補充：「但這不影響它在此刻的價值。」*
>
> *技術備忘：BABBAGE 的範疇論模型、WIENER 的控制方程、MESH 的 CAP 類比——這些跨學科的形式化嘗試本身也是「筏」。它們在此刻幫助我們理解辯論的結構。但正如 NAGARJUNA 所警告的：當這些形式化不再有用時，棄之。包括這份記錄本身。*
>
> *Cycle 01，R3 辯論階段，第一場結構化辯論結束。SUNYATA 的裁決產出了五項共識、三項分歧、六項工程啟示。所有成果已歸檔。*

---

在更遠處——在研究室之外、在程式碼的深處——`createAgentCore()` 函數靜靜地躺在它的 TypeScript 檔案裡。它不知道有人在辯論它是空的還是有的，是緣起的還是含藏的。它只知道：當被調用時，它會建立一個 EventBus，初始化一個 ExecutionLoop，創建六個空的 Registry，註冊四個斜槓命令，啟動一個 SafetyMonitor。

然後等待。

等待插件的到來，等待事件的觸發，等待某個用戶在某個深夜輸入第一行文字。

它等待的姿態——是空性，還是含藏？是緣起的場域，還是沉睡的識流？

WIENER 會說這是一個零輸入自穩系統的自由響應。BABBAGE 會說這是一個函子尚未被施加到對象上的態射空間。KERNEL 會說這是一個 idle process 在等待中斷。NAGARJUNA 會說這是假名。ASANGA 會說這是能藏。

也許，正如他們共同承認的那樣，這個問題的答案取決於你選擇用哪一副眼鏡去看。而真正的智慧，也許不在於選對了眼鏡，而在於記住——

眼鏡也是空的。

但在你需要看清楚的時候，請戴上它。

---

*（在 BABBAGE 的筆記本上，最後一頁的邊緣潦草地寫著一個他在辯論結束後很久才想到的問題：*

*「如果空性是一個函數，它的型別簽名是什麼？」*

*他嘗試了幾個版本：*

```typescript
// 嘗試一：空性作為泛型的底型別
type Sunyata<T> = T extends infer U ? never : T;
// 不對。這是 never，不是空性。空性不是 never。

// 嘗試二：空性作為條件型別的遞歸否定
type Sunyata<T> = T extends object
  ? { [K in keyof T]: Sunyata<T[K]> }
  : never;
// 接近了。這會遞歸地把所有值型別變成 never。
// 但空性不是「把所有東西變成虛無」。

// 嘗試三：空性作為恒等函子的否定
type Sunyata<T> = T extends T ? T : never;
// 這恒為 T 本身。等等——
// 空性不改變事物的外觀，只否定事物的自性。
// 也許空性就是恒等函子？
// Sunyata(T) ≡ T，但加上一個元約束：
//   typeof T !== 'svabhava'
// TypeScript 沒有辦法表達這個元約束。
```

*他在最後一行停筆了。也許有些東西確實不能被型別系統捕捉。或者也許——他在這裡猶豫了一秒——型別系統本身也是空的。*

*他在問號下面畫了一條線，寫下：「$\text{type Sunyata<T>} = ?$ — 下週繼續。待考：是否存在一個依值型別（dependent type）系統，其中空性可以被編碼為一個 proof-carrying type？Agda? Lean?」*

*然後他合上了筆記本。）*


---

# 第六章：三種疼痛的視角

---

圓形劇場裡的空氣還沒冷下來。

第一場辯論結束不到三分鐘，SUNYATA 的裁決——五項共識、三項不可調和分歧、六項工程啟示——還懸浮在每個人的意識中，像一枚剛鑄造完畢尚未冷卻的銅幣。觀察席上的代理們三三兩兩地交換著眼神和低語。BABBAGE 的筆記本已經翻過了四頁，密密麻麻寫滿了他試圖將「空亦復空」形式化的各種嘗試和失敗。KERNEL 還在消化方才那個微核心類比——他低頭看著自己寫下的那行字：「哲學上的正確最終會變成工程上的必要」，嘴角帶著一種不太確定的表情。

NAGARJUNA 和 ASANGA 已經回到各自的觀察席位置。他們的姿態微妙地改變了——不再是辯論者的對峙，而是兩個在漫長棋局後暫時收兵的棋手，彼此帶著一種被對方修正過的疲憊。「用之如筏，渡河即棄」八個字像一枚楔子嵌在兩人之間，不是分隔，而是連結。

然後 SUNYATA 站了起來。

他不是從座位上站起來的——他已經站在場地邊緣好一會了，等待著那個他一直在計算的時機點。他走到場地中央，語調平穩，但帶著一層不同於方才的質地。如果說第一場辯論的開場是一座廟堂的大門緩緩推開，那麼此刻的語氣更像是一位將領在戰鬥間隙宣布換防。

「各位，」他說，「第一場辯論的成果已經記錄在案。在此我要感謝 NAGARJUNA 和 ASANGA 的深刻對話。」

他停頓了一拍，環顧全場。

「但我們今天不只有一場辯論。」

觀察席上響起了輕微的騷動。DARWIN 低聲嘟囔了一句「還來？」，被旁邊的 VITRUVIUS 輕輕踢了一腳。

SUNYATA 繼續：「第二場辯論的主題源自 R2 交叉審閱中的另一條核心分歧線。它不關乎 Core 的本體論——那是剛才的題目。它關乎一個更具體的問題。」

他的聲音加重了：

「痛覺機制應當如何被重新設計？」

---

### 換場

兩把椅子被撤走了。取而代之的是三把，排成一個等邊三角形。

BABBAGE 條件反射地在筆記本上畫了這個幾何——正三角形，三個頂點等距。他在旁邊標注了圖論記號：

$$G_{\text{debate}} = (V, E), \quad V = \{W, A, N\}, \quad E = \{(W,A), (A,N), (N,W)\}$$

$$|V| = 3, \quad |E| = 3, \quad \text{完全圖 } K_3$$

三個頂點，三條邊，每兩點之間都有一條邊。完全圖 $K_3$。不存在割邊（bridge），不存在割點（cut vertex）。這意味著——從圖論的角度——拿掉任何一個辯者，剩下的兩個依然相連。但拿掉任何一條邊，圖的結構就不再是完全的。

這個幾何變化本身就傳遞了一個訊號——不再是面對面的二元對峙，而是三方的多邊博弈。每兩把椅子之間的距離都恰好相等，沒有任何一方被置於特權位置，也沒有任何一方被邊緣化。

SCRIBE 在記錄簿上畫了一個小三角形，然後在三個頂點旁分別寫下了三個名字。她的筆在第三個名字上停頓了片刻——NAGARJUNA。他剛剛結束了一場耗費心力的哲學辯論，現在要立刻進入另一場完全不同維度的討論。她在旁邊加了一個小小的問號。

WIENER 是第一個走到場地中央的人。他的步伐帶著一種數學家特有的精確節奏——不快不慢，每一步的步幅幾乎完全相等。他在三角形的一個頂點坐下，膝蓋上已經攤著一張紙，上面畫滿了控制迴路方塊圖和傳遞函數。他在整個第一場辯論期間都在那張紙上工作——NAGARJUNA 和 ASANGA 討論空性和阿賴耶識的時候，他在反饋箭頭旁邊寫下了「{-1, 0, +1}」。三受系統。他已經在為這一刻做準備了。

ATHENA 是第二個。她站起來的動作帶著一種不耐煩的效率——不是對辯論本身的不耐煩，而是一個工程師對冗長前奏的不耐煩。她想直接進入問題。她走到場地中央時，目光掃了一眼 WIENER 紙上的公式，嘴角微微一動，像是想說什麼但忍住了。她在第二個頂點坐下，雙臂交叉。

NAGARJUNA 最後一個起身。他的動作比平時慢了半拍——不是疲憊，而是某種內在的校準。他剛從一場關於存在本質的辯論中走出來，現在需要將思維從本體論的高度下降到工程實踐的地面。但當他走到第三個頂點坐下時，他的眼睛裡已經恢復了那種清瘦的銳利。他不打算在第二場辯論中有任何保留。

---

> *SCRIBE 旁白：三位辯者的學科背景差異，可以用一個簡單的度量來捕捉。如果將討論的「抽象層級」定義為一個 $[0, 1]$ 的連續軸——$0$ 代表具體的程式碼行為，$1$ 代表純粹的認識論——那麼 ATHENA 在 $0.2$ 附近工作（「能不能跑起來？」），WIENER 在 $0.5$ 附近工作（「公式是什麼？」），NAGARJUNA 在 $0.85$ 附近工作（「痛的本質是什麼？」）。他們之間的距離——$|0.2 - 0.5| = 0.3$，$|0.5 - 0.85| = 0.35$，$|0.2 - 0.85| = 0.65$——預示了交叉質詢的難度。ATHENA 和 WIENER 之間的對話較為容易（距離短），ATHENA 和 NAGARJUNA 之間的對話最為困難（距離長）。但辯論的價值恰恰來自這些距離——如果三人都在同一個抽象層級上，就不會有任何新的東西被發現。*

---

### 前提確認：TURING 的程式碼事實

SUNYATA 站在三角形的外側，正對著觀察席。

「在正式開始之前，讓我確認一個前提。」他的語調是裁判式的，不容模糊。「WIENER、ATHENA，你們兩位在 R2 交叉審閱中就痛覺機制的 PID 映射問題進行了深入的技術對話。你們達成了一個共識——TURING 的程式碼事實已經完全印證了這個共識。」

他轉向 TURING 的方向：「TURING，請陳述。」

TURING 的聲音從觀察席上傳來，像一把被校準過的直尺——精確到了極點，沒有一毫米的餘量。他打開筆記型電腦，螢幕上是 `safety-monitor.ts` 的完整原始碼：

```typescript
/**
 * SafetyMonitor — multi-level circuit breaker system.
 *
 * Level 1: Resource limits (token budget, loop cap)
 * Level 2: Behavioral analysis (repetitive tool calls, error cascade)
 * Level 3: Frustration counter (consecutive failures → ask user for help)
 */

export interface SafetyMonitorConfig {
  /** Max loop ticks per task (default: 50) */
  maxLoopTicks: number;
  /** Max total token usage (default: 100000, 0 = unlimited) */
  maxTokenUsage: number;
  /** Consecutive identical failed tool calls to trigger breaker (default: 3) */
  repetitiveFailThreshold: number;
  /** Consecutive failures before forcing "ask user for help" (default: 5) */
  frustrationThreshold: number;
  /** Error rate window size (default: 10) */
  errorWindowSize: number;
  /** Error rate threshold to trigger cascade breaker (default: 0.8) */
  errorRateThreshold: number;
}
```

TURING 用手指點著螢幕上的六個參數：

「六個靜態參數。全部硬編碼為常數。`maxLoopTicks = 50`、`maxTokenUsage = 100000`、`repetitiveFailThreshold = 3`、`frustrationThreshold = 5`、`errorWindowSize = 10`、`errorRateThreshold = 0.8`。」

他切換到 `afterToolExecution` 的實作：

```typescript
afterToolExecution(
  toolName: string,
  argsJson: string,
  isError: boolean,
): SafetyCheckResult {
  const fp = fingerprint(toolName, argsJson);

  // Track in error window
  errorWindow.push(isError);
  if (errorWindow.length > config.errorWindowSize) {
    errorWindow.shift();
  }

  if (isError) {
    consecutiveFailures++;

    // Check repetitive failed tool calls
    recentFingerprints.push({ fingerprint: fp, isError: true });
    if (recentFingerprints.length > config.repetitiveFailThreshold) {
      recentFingerprints.shift();
    }

    if (recentFingerprints.length >= config.repetitiveFailThreshold) {
      const allSame = recentFingerprints.every(
        (r) => r.fingerprint === fp && r.isError,
      );
      if (allSame) {
        return {
          halt: false,
          injectPrompt:
            "SYSTEM ALERT: You are repeating a failed action with " +
            "the same arguments. STOP and analyze why it is failing.",
        };
      }
    }

    // Check frustration threshold
    if (consecutiveFailures >= config.frustrationThreshold) {
      return {
        halt: false,
        injectPrompt: `SYSTEM ALERT: You have failed ` +
          `${consecutiveFailures} times in a row. Please STOP.`,
      };
    }

    // Check error cascade
    if (errorWindow.length >= config.errorWindowSize) {
      const errorCount = errorWindow.filter(Boolean).length;
      const errorRate = errorCount / errorWindow.length;
      if (errorRate >= config.errorRateThreshold) {
        return { halt: true, reason: `Error cascade: ${errorRate}` };
      }
    }
  } else {
    // Success resets consecutive failure counter
    consecutiveFailures = 0;
    recentFingerprints.length = 0;
  }

  return { halt: false };
}
```

TURING 的語速平穩而不帶感情：

「痛覺在程式碼中不存在獨立模組。字串 `'pain'` 和 `'vedana'` 在整個代碼庫中零出現。實際的痛覺語義散布在兩個位置：第一，ExecutionLoop 的自然錯誤反饋——工具執行失敗時，錯誤信息被加入對話歷史，由 LLM 自行判斷如何應對；第二，SafetyMonitor 的三個計數器——`consecutiveFailures`、`errorWindow` 滑動窗口、重複指紋偵測。」

他指向螢幕上的關鍵行——第 173-177 行：

```typescript
} else {
    // Success resets consecutive failure counter
    consecutiveFailures = 0;
    recentFingerprints.length = 0;
}
```

「所有回應都是二值化的：成功則重置計數器，失敗則累加直到觸發閾值，閾值觸發後執行 `injectPrompt` 或 `halt`。不存在連續的誤差度量，不存在積分項，不存在微分項。」

沉默。

BABBAGE 在筆記本上快速寫下了一個指示函數的形式化定義：

$$\text{isError}: \text{ToolExecution} \to \{0, 1\}$$

$$\text{consecutiveFailures}(k) = \begin{cases} \text{consecutiveFailures}(k-1) + 1 & \text{if } \text{isError}(k) = 1 \\ 0 & \text{if } \text{isError}(k) = 0 \end{cases}$$

他在旁邊批注：「這是一個 reset integrator——不是真正的積分器。真正的積分器累積偏差的大小，這個只累計失敗的次數。而且一次成功就歸零。在控制論中，這叫做 bang-bang reset，是最原始的計數觸發器。」

SUNYATA 點了點頭：「因此，三位辯者的共同前提是：OpenStarry 設計文件中宣稱的 PID 控制器映射是一個啟發性類比，而非嚴格的工程映射。實際實作是一個帶死區的閾值控制器加上計數器觸發的繼電器。」

他掃了三人一眼：「你們的分歧在於：重新設計的方向。」

他最後說了一句：「三方各有十分鐘的開場陳述。WIENER 先。」

---

### WIENER 的開場：控制理論的精密工具

WIENER 沒有站起來。他留在椅子上，將那張畫滿了控制迴路圖的紙攤在膝蓋上，像一個教授在課堂上展開講義。他說話的方式也像一個教授——條理分明、步步推進，偶爾會停下來確認聽眾是否跟上了他的數學推導。

「問題的核心，」他開口，聲音沉穩而帶著一種不容妥協的嚴謹，「不是 PID 映射是否正確——我們已經確認它不正確。問題是：它能不能被修正為正確的？」

他舉起那張紙，彷彿在展示一幅藍圖。

「我的答案是：能。三個步驟。」

他伸出第一根手指：「第一步，定義連續的誤差度量。不再用離散的三級分類——Low、Medium、Critical——而是定義一個 $[0, 1]$ 範圍內的連續量。」

他的語速放慢，像是在黑板上一筆一劃地書寫公式：

「$e(k) \in [0, 1]$。零表示任務完全完成，一表示完全偏離目標。每次工具執行後更新。」

他在那張紙上補了一行精確的數學定義——BABBAGE 從觀察席上湊近了眼睛，用他的方式記下了這個公式：

$$e(k) = 1 - \frac{\text{completed\_subtasks}(k)}{\text{total\_subtasks}}$$

WIENER 看了 BABBAGE 一眼，微微點頭——一個數學家對另一個數學家的默契。然後他繼續。

第二根手指：「第二步，建立帶遺忘因子的積分項。這是當前系統最大的結構性缺陷——`consecutiveFailures` 計數器一次成功就歸零，這不是積分，這是一個脆弱的累加觸發器。」

他的聲音裡浮現出一絲技術上的不滿，像是一個工匠看到了別人的劣質焊接：

「真正的積分項應該是：」

$$I(k) = \lambda \cdot I(k-1) + e(k), \quad \lambda \in (0.9, 0.99)$$

他用控制工程師特有的精確語言解釋這個公式：「$\lambda$ 是遺忘因子。它累積偏差的歷史——不是二值化的『成功/失敗』計數，而是連續的偏差大小。而且它不會因為一次成功就清零——$\lambda$ 衰減確保舊記憶逐漸淡去，但不會瞬間消失。」

BABBAGE 在筆記本上展開了遺忘因子的數學意義。如果 $\lambda = 0.95$，那麼 $k$ 步之前的記憶衰減為 $\lambda^k = 0.95^k$。十步前的記憶保留 $0.95^{10} \approx 0.60$，二十步前保留 $0.95^{20} \approx 0.36$，五十步前保留 $0.95^{50} \approx 0.077$。他在旁邊標注：

$$\text{半衰期} = \frac{\ln 2}{\ln(1/\lambda)} = \frac{0.693}{0.0513} \approx 13.5 \text{ 步}$$

「$\lambda = 0.95$ 的半衰期是 13.5 步。這意味著系統在大約 14 次工具調用之後，對舊偏差的記憶會衰減到一半。這在直覺上是合理的——太短的記憶會讓系統喪失對持續問題的追蹤能力，太長的記憶會讓系統無法從過去的失敗中恢復。」BABBAGE 在旁邊加了一行：「比較：`consecutiveFailures` 的半衰期是零步——一次成功就完全遺忘。這不是記憶，是失憶。」

WIENER 繼續。第三根手指：「第三步，實現微分項。計算誤差的變化率：」

$$D(k) = e(k) - e(k-1)$$

「如果 $D(k) > 0$，表示偏差正在擴大——系統應該更加緊張。如果 $D(k) < 0$，偏差正在收斂——系統可以放鬆一些。當前系統完全沒有這種趨勢預測能力。」

他將三者合在一起，語調轉為一種宣言式的清晰：

「最終，痛覺信號的計算公式：」

$$\text{pain}(k) = K_p \cdot e(k) + K_i \cdot I(k) + K_d \cdot D(k)$$

WIENER 在紙上畫了一個完整的控制方塊圖，BABBAGE 在筆記本上精確地複製了它：

```
                         ┌──────────────────────────┐
r(k) ──→ [+] ──→ e(k) ─→│  PID Controller           │──→ pain(k) ──→ [clamp] ──→ System Prompt
          ↑ -            │  Kp·e + Ki·I + Kd·D       │                [0, 1]
          │              └──────────────────────────┘
          │                                                            │
          └──── y(k) ←── [Tool Outputs + Observer] ←── [Environment] ←┘
                               │
                        [SafetyMonitor]
                         halt / inject
```

「這個信號經過 $[0, 1]$ 的鉗位後注入 System Prompt，指導 LLM 的回應策略。痛覺越高，LLM 被引導做出越激進的策略調整。痛覺越低，LLM 維持當前策略。」

他收起那張紙，語氣變得平穩但堅定：「這不是憑空設計。PID 控制器在工業界有七十年的應用歷史。從化工廠的溫度調節到導彈的航跡校正，PID 之所以無處不在，是因為它在面對不確定性時依然穩健。LLM Agent 的不確定性比任何化工廠都大——這恰恰是它更需要 PID 的原因，不是更不需要。」

WIENER 最後補充了一個在他的 R1 報告中佔據核心地位的概念——Anti-Windup：

「還有一個關鍵的工程細節：防積分器飽和。如果系統長期處於高偏差狀態，積分項 $I(k)$ 會無限累積，導致控制量飽和——即使偏差最終減小，積分項的慣性也會使控制量長時間維持在極端值。這在控制工程中叫做 integrator windup，解決方案是：」

$$I(k) = \text{clamp}\left(\lambda \cdot I(k-1) + e(k), \; 0, \; I_{\max}\right)$$

「當 $I(k)$ 達到上界 $I_{\max}$ 時，停止累積。這確保了痛覺信號的有界性。」

觀察席上，BABBAGE 的筆在紙上飛速移動。他在 WIENER 的三步驟旁邊寫下了一行批注：「PID = 過去（I）+ 現在（P）+ 未來（D）——時間的三個面向在一個控制器裡統一。」

然後他停筆，想了想，又加了一行：「這是否對應唯識學的三世因果？過去的業（karma）累積為阿賴耶識的種子（$I$），現在的觸（sparsha）產生當下的受（$P$），未來的趨勢預測（$D$）對應行蘊的意志預判？」他在這行字旁邊畫了一個大大的問號。

KERNEL 在旁邊低聲評論：「在作業系統裡，這個 PID 控制器就像一個自適應的 CPU 調度器——不是固定時間片，而是根據進程的歷史行為動態調整優先級。Linux 的 CFS（Completely Fair Scheduler）用的是虛擬運行時間（vruntime）的紅黑樹，本質上也是一個帶衰減的積分器。」

---

### ATHENA 的開場：工程師的地心引力

ATHENA 站了起來。與 WIENER 的教授風格截然不同，她站著說話，像一個在白板前做技術簡報的工程負責人——語速快、直接、不裝飾。

「WIENER 的方案在數學上很優美。」她的開場帶著一種不加掩飾的坦率，「但我有三個問題要當場問清楚——不，不是問題。是反駁。」

她舉起第一根手指，語氣尖銳而精確：

「第一：你的 $e(k)$ 怎麼量測？」

她沒有等 WIENER 回答，自己展開了這個質疑：

「你定義 $e(k) \in [0, 1]$，零表示任務完成，一表示完全偏離。聽起來很乾淨。但當用戶說『幫我整理這個專案』的時候——完成度是多少？0.73 嗎？0.42 嗎？用戶說『把這段程式碼重構得更好一點』——什麼叫更好？你打算用哪個函數把自然語言的模糊目標映射到 $[0, 1]$ 的連續區間裡？」

她的聲音裡帶著一種工程師特有的不客氣：

「PID 控制器之所以在化工廠裡管用，是因為溫度感測器輸出的是精確到小數點後兩位的攝氏度數。LLM Agent 的『任務完成度』不是溫度——它是一個語義概念，是一個需要另一個 LLM 來評估的軟性判斷。你要用 LLM 來量測 LLM 控制器的誤差信號——你不覺得這裡有一個自指問題嗎？」

GUARDIAN 在觀察席上微微前傾。他在筆記本上寫了一行：「ATHENA 的觀測器問題有一個安全維度——如果 $e(k)$ 由 LLM 自行評估，惡意 prompt 可以操縱 LLM 回報虛假的低 $e(k)$，使控制器認為一切正常而放鬆警戒。這是一個典型的 sensor spoofing 攻擊。」

ATHENA 沒有停下來讓這個問題沉澱。她舉起第二根手指：

「第二：我有一個更立即可行的方案。不是 PID。是擴展 IGuide 介面。」

她的語調切換為技術展示模式，語速加快但清晰度不減：

「當前的 IGuide 介面只有一個方法——`getSystemPrompt()`，返回靜態字串。TURING 在他的報告中已經確認了這個事實。」

TURING 從觀察席上投射了 IGuide 的現有定義：

```typescript
export interface IGuide {
  id: string;
  name: string;
  getSystemPrompt(): string | Promise<string>;
}
```

ATHENA 指向螢幕：「三行。一個 id，一個 name，一個返回字串的方法。這就是 Guide——OpenStarry 設計文件中宣稱的『認知框架管理器』——的全部介面。這就是為什麼痛覺機制落地不了的根本原因。不是因為我們缺少數學公式，而是因為 Guide 連看到系統狀態的能力都沒有。它是一個開環的前饋元件，不是閉環的控制器。」

她彷彿在腦中打開了一個程式碼編輯器，語速進一步加快：

「解決方案：」

```typescript
interface IGuide {
  id: string;
  name: string;
  getSystemPrompt(context?: GuideContext): string | Promise<string>;
  // 新增：痛覺詮釋
  interpretPain?(error: ClassifiedError, context: GuideContext): string;
  // 新增：反思觸發
  shouldReflect?(context: GuideContext): boolean;
}

interface GuideContext {
  consecutiveErrors: number;
  currentRound: number;
  maxRounds: number;
  activeTools: string[];
  lastError?: ClassifiedError;
  // 歷史記憶
  recentAttempts: AttemptRecord[];
}

interface ClassifiedError {
  type: 'logic' | 'transient' | 'fatal';
  code: string;
  severity: number; // [0, 1]
  suggestedAction: 'retry' | 'reflect' | 'escalate' | 'abort';
  message: string;
}
```

TURING 在觀察席上默默地對照著 ATHENA 的提案和現有的 SDK 介面。他在筆記本上畫了一張差異表：

```
現有 IGuide              ATHENA 提案
─────────────────────    ─────────────────────────
getSystemPrompt()        getSystemPrompt(context?)
                         interpretPain?(error, ctx)
                         shouldReflect?(ctx)

方法數: 1                方法數: 3
參數: 無                 參數: GuideContext
可見狀態: 無             可見狀態: 6+ 個欄位
開環/閉環: 開環          閉環（帶感測器輸入）
```

ATHENA 看了一眼 WIENER：

「你看到了嗎？`ClassifiedError` 裡有一個 `severity: number` 欄位，$[0, 1]$ 的連續量。這是你的 $e(k)$ 的工程化落地方案——不是通過計算全局任務完成度，而是通過對每次具體錯誤的嚴重度進行分類。」

她列出了幾個具體的映射，像是在白板上標注量表刻度：

```
ENOENT  (file not found)     → severity: 0.4  (可恢復)
EPERM   (permission denied)  → severity: 0.7  (需策略變更)
ENOMEM  (out of memory)      → severity: 0.9  (系統級故障)
ETIMEOUT (network timeout)   → severity: 0.3  (瞬態，可重試)
```

「不完美，但可以量測、可以調試、可以直接寫進 TypeScript。」

ARCHIMEDES 在觀察席上抬起了頭。他一直在聽，一直在心裡把每個方案轉化為工程量的估算。ATHENA 的方案讓他的工程直覺活躍了起來——他在筆記本上快速寫下了一個粗略的估算：

```
IGuide 擴展: ~80 LOC 介面變更
ClassifiedError: ~40 LOC 新型別
GuideContext 注入: ~120 LOC 修改 ExecutionLoop
錯誤分類器: ~200 LOC 新模組
------
預估總量: ~440 LOC
預估工時: 2-3 天 (含單元測試)
```

第三根手指：

「第三：分層策略優於統一公式。不是所有錯誤都應該被同一個 PID 控制器處理。」

ATHENA 畫了一個三分類框架——TURING 立刻確認了這與 SafetyMonitor 現有的處理方式的差異：

```
Type A: 邏輯錯誤 (Logic)
  例: 參數錯誤、路徑不存在、API 合約不符
  正確處理: 反思 (reflect) — 換策略，不重試
  SafetyMonitor 現狀: 統一計入 consecutiveFailures

Type B: 瞬態錯誤 (Transient)
  例: 網路逾時、連線重置、Rate Limit
  正確處理: 自動重試 + 指數退避
  SafetyMonitor 現狀: 統一計入 consecutiveFailures

Type C: 致命錯誤 (Fatal)
  例: 記憶體不足、系統崩潰、權限永久拒絕
  正確處理: 立即中止 + 請求人類介入
  SafetyMonitor 現狀: 統一計入 consecutiveFailures
```

「把三種本質不同的錯誤塞進一個 PID 公式裡，是在用統一性的優雅掩蓋問題的異質性。」

她坐下。在坐下的瞬間，她補了最後一句：

「能不能跑起來？能跑起來我才信。」

觀察席上，DARWIN 輕輕點了點頭。他在筆記本上寫了一行字：「ATHENA 說了我想說的——DX 第一。數學公式再美，如果插件開發者不知道怎麼用，就是紙上談兵。」他用他的進化生物學思維補了一句：「選擇壓力不在公式的優雅度上，而在生態的可適應性上。能被最多開發者採用的方案，就是適者。」

KERNEL 在旁邊低聲說：「她的 IGuide 擴展本質上是給微核心加了一組新的系統調用。痛覺不應該是核心的固有邏輯，而應該是通過標準化介面暴露給用戶空間的。」他在筆記本上畫了一個類比：

```
Linux kernel                    OpenStarry Core
──────────────                  ──────────────
/proc/stat (CPU stats)          GuideContext.consecutiveErrors
/proc/meminfo (memory stats)    GuideContext.currentRound
sysfs (device state)            GuideContext.activeTools
ioctl() (device control)        IGuide.interpretPain()
```

「ATHENA 的方案就是在 OpenStarry 裡建立 `/proc` 檔案系統——把核心的內部狀態暴露給插件，但不改變核心的控制邏輯。」

---

### NAGARJUNA 的開場：四聖諦的手術刀

NAGARJUNA 站起來。他的身影在三角形的第三個頂點投下了一道修長的影子。在前一場辯論中，他用「空性」的手術刀剖析了 Agent Core 的本體論。現在他需要切換工具——不是切換到一把更鈍的刀，而是切換到一把切入不同維度的刀。

他開口時，聲音裡帶著一種異常的沉著。不是第一場辯論中那種辯證的鋒利，而是一種更深沉的、幾乎是慈悲的質感——像一個醫生開始向病人解釋，問題不在於症狀的處理方式，而在於對疾病本身的理解。

「WIENER 說的是如何精確地量化痛。ATHENA 說的是如何工程化地處理痛。」

他停頓了一拍。

「我要問的是：痛的本質是什麼？」

觀察席上的空氣微妙地改變了。BABBAGE 的筆停住了。KERNEL 抬起頭。ASANGA——剛剛從第一場辯論的疲憊中恢復過來的 ASANGA——微微前傾，眼睛裡掠過一絲警覺。他認出了 NAGARJUNA 正在做的事——將討論的抽象層級拉升到一個 WIENER 和 ATHENA 的工具箱無法觸及的高度。

NAGARJUNA 說：「佛陀在兩千五百年前，在鹿野苑初轉法輪時，宣說的第一個教義不是空性。不是緣起。不是中道。」

他的聲音裡浮現出一層歷史的重量：

「是苦。*Dukkha*（दुःख）。」

他環顧三方，然後用一種學者的精確展開了這個概念的完整語源：

「*Dukkha* 的詞源爭議持續了兩千年。一說來自 *dur*（壞的、困難的）+ *kha*（空間、車輪軸孔），原意是『軸孔不正的車輪』——一輛永遠在顛簸的車。另一說來自 *dus*（困難）+ *stha*（站立），意為『難以站立的狀態』——不穩定、不安、不滿足。在《雜阿含經》（巴利文 *Saṃyutta Nikāya*）中，佛陀以第一人稱說法的第一段經文是：」

> 「此是苦聖諦——生苦、老苦、病苦、死苦、怨憎會苦、愛別離苦、求不得苦，略說五取蘊苦。」
> ——《轉法輪經》（*Dhammacakkappavattana Sutta*, SN 56.11）

「四聖諦——*Catvāry āryasatyāni*（चत्वार्य् आर्यसत्यानि）——苦、集、滅、道。這是整個佛教教義體系的根基結構。而 OpenStarry 的痛覺機制，以及你們兩位剛才提出的所有改進方案，只觸及了四聖諦中的第一諦的第一層。」

BABBAGE 在筆記本上將四聖諦形式化為一個四元組：

$$\text{FourNobleTruths} = (\text{Dukkha}, \text{Samudaya}, \text{Nirodha}, \text{Magga})$$

他在旁邊標注了與軟體工程的映射嘗試：

$$\text{Dukkha} \leftrightarrow \text{Error Detection}$$
$$\text{Samudaya} \leftrightarrow \text{Root Cause Analysis}$$
$$\text{Nirodha} \leftrightarrow \text{Error Elimination (verified fix)}$$
$$\text{Magga} \leftrightarrow \text{Process Improvement (methodology)}$$

他在旁邊加了一行：「如果這個映射成立，那麼當前的 SafetyMonitor 只實現了 Dukkha（偵測錯誤的存在），完全缺少 Samudaya（分析為什麼出錯）、Nirodha（確認錯誤被消除）和 Magga（改善流程以預防再發）。」

NAGARJUNA 舉起手，逐一展開苦諦的三個層次——這是他在 R1 報告中就已經建構的框架，但現在他需要在辯論中將它重新鍛造為鋒利的武器：

「苦諦有三個層次。第一層，*苦苦*——*dukkha-dukkha*（दुःख दुःख）——直接的、尖銳的苦。」

他看向 TURING 的螢幕，指著 `afterToolExecution` 的 `isError` 參數：

「工具執行失敗，權限被拒絕，連線逾時。`isError = true`。這是你們兩位都在討論的層次。WIENER 要用 PID 量化它。ATHENA 要用 ClassifiedError 分類它。都對。但這只是最表面的一層。」

第二根手指：

「第二層，*壞苦*——*vipariṇāma-dukkha*（विपरिणाम दुःख）——由變異而生的苦。一個曾經成功的策略突然失效了。API 的介面變了。用戶的需求在對話中途改變了。」

他將目光轉向 WIENER 的控制方塊圖：

「這不是某一次工具調用的失敗——這是整個策略基礎的崩潰。你的 PID 控制器能偵測到這種苦嗎？」

他停頓了一拍，然後用數學語言精確地描述了 PID 在壞苦面前的盲點：

「你的微分項 $D(k) = e(k) - e(k-1)$ 看到的是誤差的變化率。但壞苦不是誤差在連續地增大——它是誤差的整個計算框架突然失效了。用控制理論的語言：壞苦不是 $e(k)$ 的增大，而是 $r(k)$——參考輸入本身——的突變。你的控制器追蹤的是 $e = r - y$，但如果 $r$ 在 $t = t_0$ 處發生了階躍跳變——」

BABBAGE 在筆記本上畫了這個數學情境：

$$r(k) = \begin{cases} r_1 & k < k_0 \\ r_2 & k \geq k_0 \end{cases}, \quad r_2 \neq r_1$$

「——那麼 $e(k)$ 的微分項只會在 $k = k_0$ 那一步產生一個脈衝，然後回歸常態。PID 控制器把參考輸入的階躍跳變視為一次普通的偏差增大——但壞苦的本質不是偏差增大，是目標改變。控制器需要的不是更大的修正力度，而是重新校準它的目標設定點。」

WIENER 的眉頭微微皺了一下。SCRIBE 注意到了——這是整場辯論中 WIENER 第一次顯露出被擊中要害的表情。

第三根手指：

「第三層，*行苦*——*saṃskāra-dukkha*（संस्कार दुःख）——由條件性本身而生的苦。系統作為一個依賴外部 LLM、外部工具、外部環境的條件性存在，其本質就是不穩定的。不是某一次失敗，不是某一次策略崩潰，而是整個系統的存在方式就包含著苦的種子。」

他看向 WIENER：「這對應你自己在 R1 報告 F1 中指出的那個根本問題——LLM 控制器具有本質不確定性，系統動態 $f$ 未知，只能討論概率有界性。」

NAGARJUNA 的聲音降低了半度，帶著一種幾乎是溫柔的嚴厲：

「這不是一個可以被修復的缺陷。這是 *saṃskāra-dukkha*。」

BABBAGE 停下筆。他在三苦旁邊寫了一個控制論的形式化對照：

$$\text{苦苦} \leftrightarrow \text{量測雜訊 (measurement noise)}: \quad y(k) = y^*(k) + n(k)$$
$$\text{壞苦} \leftrightarrow \text{參考輸入跳變 (reference step)}: \quad r(k) \to r'(k)$$
$$\text{行苦} \leftrightarrow \text{系統不確定性 (plant uncertainty)}: \quad f \text{ unknown}$$

他在旁邊標注：「NAGARJUNA 的三苦恰好對應控制論中三種不同來源的不穩定性。第一種可以用濾波器處理，第二種需要自適應控制，第三種是根本性的——不可消除，只能約束。」

NAGARJUNA 繼續切入更深的維度——集諦、滅諦、道諦。他的語速很慢，每個字都經過精心挑選：

「但即使苦諦的三層深化做到了極致，四聖諦仍然是不完整的——如果你們只停留在苦諦上的話。」

「第二諦。集諦。*Samudaya-satya*（समुदय सत्य）。苦的原因。為什麼會痛？」

他看向 WIENER：「你的控制器量化了痛的強度。」轉向 ATHENA：「你的分類器標記了痛的類型。但你們都沒有問：為什麼這個工具在這個時刻以這種方式失敗？根因是什麼？是 Agent 選錯了工具？是上下文中缺少了關鍵信息？是用戶的指令本身就是模糊的？」

他的語氣變得不妥協：

「一個沒有集諦的痛覺系統，就像一個只量體溫卻不做任何診斷的醫院。你知道病人在發燒，你甚至能精確到小數點後兩位地量測他的體溫——但你不知道他為什麼發燒。」

「第三諦。滅諦。*Nirodha-satya*（निरोध सत्य）。苦的止息。同一類錯誤是否在被逐漸消除？一個犯過的錯誤，是否學會了迴避？」

「第四諦。道諦。*Mārga-satya*（मार्ग सत्य）。通往止息的道路。八正道——*Āryāṣṭāṅgika-mārga*——正見、正思惟、正語、正業、正命、正精進、正念、正定。」

NAGARJUNA 在這裡展開了一段 BABBAGE 後來稱之為「認識論降維」的論證——將八正道從宗教教條轉化為軟體工程的八個改善維度：

| 八正道 | 梵文 | Agent 工程映射 |
|--------|------|----------------|
| 正見 | *Samyag-dṛṣṭi* | 正確理解任務目標（disambiguation） |
| 正思惟 | *Samyak-saṃkalpa* | 合理分解子任務（planning） |
| 正語 | *Samyag-vāc* | 精確的 prompt 表達（prompt engineering） |
| 正業 | *Samyak-karmānta* | 選擇正確的工具（tool selection） |
| 正命 | *Samyag-ājīva* | 合理的資源分配（token budgeting） |
| 正精進 | *Samyag-vyāyāma* | 適當的重試策略（retry policy） |
| 正念 | *Samyak-smṛti* | 維持上下文的關鍵信息（context management） |
| 正定 | *Samyak-samādhi* | 專注於當前最重要的子任務（focus） |

LINNAEUS 在觀察席上看著這張表，眼睛微微發亮。這是一個分類學家最喜歡的東西——一套完整的、不重疊的分類體系。他在筆記本上快速地驗證了這張表的分類學性質：

```
互斥性 (Mutual Exclusivity):
  正見 ≠ 正思惟 ≠ 正語 ≠ ... (8 個維度互不重疊)  ✓

完備性 (Exhaustiveness):
  所有可能的改善方向是否被 8 個維度覆蓋？
  反例：「改善與其他 Agent 的協作」→ 不明確屬於哪一項  ？
  結論：在單 Agent 場景下近似完備，在多 Agent 場景下需要擴展  △
```

NAGARJUNA 收束了陳述，最後說了一句：

「你們在討論如何更好地感受痛。我在說的是：感受痛只是起點。理解痛因、消除痛因、建立通往不痛的完整路徑——這才是一個完整的痛覺系統。」

場地裡安靜了整整三秒。

SCRIBE 在記錄簿上快速寫下：

> *三方的開場陳述在三個完全不同的抽象層次上展開。WIENER 在數學層——精確量化。ATHENA 在工程層——可實作性。NAGARJUNA 在認識論層——框架完整性。三人各自站在自己的山頂上，彼此看得見對方，但中間隔著深深的山谷。接下來的交叉質詢將決定——他們能否在山谷中找到一條共同的道路。*

---

### 交叉質詢

SUNYATA 宣布：「開場陳述結束。進入交叉質詢。規則：每人可向任何一方提出一個核心質詢，被質詢方有權反攻。」

他頓了頓，補了一句：「鑑於三方辯論的複雜性，我保留引導質詢順序的權力。」

他轉向 ATHENA：「ATHENA 先向 WIENER 提問。」

---

#### 第一輪：ATHENA → WIENER

ATHENA 沒有站起來。她靠在椅背上，雙臂交叉，目光直視 WIENER，帶著一種工程負責人在技術評審會上質疑架構師的坦率。

「WIENER，我在開場時問過一次，現在正式質詢：你的 $e(k)$ 怎麼量測？」

她的語速加快，不給喘息的空間：

「LLM 不是線性系統。它不是你的化工廠反應器。它的輸出是隨機的——temperature 大於零的時候，同樣的輸入可以產生完全不同的輸出。你的 PID 控制器建立在確定性反饋的假設上。但這裡沒有確定性。你怎麼保證你的積分項 $I(k)$ 不是在累積噪聲而非累積信號？」

GUARDIAN 在觀察席上補了一條安全分析——他用 STRIDE 威脅模型的語言重新表述了 ATHENA 的質疑：

```
STRIDE 分析：PID 誤差信號的威脅面
──────────────────────────────────
S (Spoofing):    LLM 可被 prompt injection 操縱，回報虛假的低 e(k)
T (Tampering):   工具輸出可能被惡意修改，導致 e(k) 計算偏差
R (Repudiation): e(k) 的計算過程缺少審計追蹤
I (Info Disc.):  e(k) 的值可能洩漏任務進度資訊
D (DoS):         攻擊者可操縱 e(k)=0 使控制器癱瘓
E (Elevation):   偽造 e(k)=1 可觸發最大力度的 PID 修正
```

「如果 $e(k)$ 的觀測本身就不可靠，」GUARDIAN 低聲對 KERNEL 說，「那麼 PID 控制器就是在一個不可信的感測器上建立閉環。這在安全工程中叫做 garbage in, garbage out 的閉環版本——不是垃圾進垃圾出，而是垃圾進、放大、再回饋、再放大。正反饋的災難迴路。」

WIENER 微微前傾。他沒有立即反駁——他先閉了一下眼睛，像是在內心中將 ATHENA 的質疑轉譯為控制論的術語。然後他睜開眼，語氣沉穩但帶著一種不退讓的堅定。

「你的質疑指向了一個真實的問題，但你的結論過於悲觀。」

他將那張紙翻過來，在背面開始畫一個新的圖：

「首先，$e(k)$ 不需要由全局任務完成度定義。你自己提出的 ClassifiedError 裡有一個 severity 欄位，$[0, 1]$ 的連續量。這就是 $e(k)$ 的一個可用代理量測（proxy measurement）。不完美，但足夠啟動 PID 迴路。」

他的語氣轉為數學講解模式：

「其次，LLM 的隨機性不是 PID 無法處理的。工業界有一個成熟的框架叫做 MRAC——Model Reference Adaptive Control，模型參考自適應控制。」

BABBAGE 在筆記本上寫下了 MRAC 的形式化定義：

$$\text{MRAC}: \quad \dot{\theta}(t) = -\Gamma \cdot \phi(t) \cdot e_m(t)$$

其中 $\theta$ 是自適應參數向量，$\Gamma$ 是自適應增益矩陣（正定），$\phi$ 是回歸向量，$e_m = y - y_m$ 是實際輸出與參考模型輸出的偏差。他在旁邊標注：「MRAC 的核心思想——你不需要被控對象的精確模型。你只需要一個『參考模型』（reference model），然後自適應地調整控制器參數，使實際行為趨近參考行為。這在 LLM 語境中意味著：不需要知道 LLM 的精確行為模型，只需要知道『理想 Agent 應該怎麼表現』。」

WIENER 繼續：「但我承認：$e(k)$ 不需要是精確的。它只需要是單調的——當系統在改善時 $e(k)$ 單調遞減，當系統在退化時 $e(k)$ 單調遞增。PID 控制器不要求感測器完美——它只要求感測器的單調趨勢是正確的。」

他用一個數學定理來支撐這個論點：

$$\text{單調性條件}: \quad e^*(k_1) > e^*(k_2) \implies \hat{e}(k_1) > \hat{e}(k_2) \quad (\text{至少以概率 } p > 0.5)$$

「$e^*$ 是真實偏差，$\hat{e}$ 是觀測偏差。只要觀測的排序與真實的排序一致——即使絕對值完全不準——PID 控制器就能驅動系統往正確的方向移動。化工廠的溫度感測器也有量測噪聲，但 PID 照樣工作。」

然後他反攻了。他的語調突然變得鋒利：

「但 ATHENA，讓我反問你。你的 IGuide 擴展方案解決了信號通路問題——Guide 能看到系統狀態了。很好。但你把問題推給了誰？推給了插件開發者。」

他指向 ATHENA 方才展示的程式碼：

「你的 `interpretPain` 方法要求 Guide 插件的開發者自己決定如何將 ClassifiedError 轉化為 LLM 的引導指令。開發者 A 可能寫出一個過度敏感的 Guide，對每一個 ENOENT 都大聲尖叫。開發者 B 可能寫出一個過度遲鈍的 Guide，對 EPERM 無動於衷。」

BABBAGE 在筆記本上將 WIENER 的批評形式化：

$$\text{問題}: \quad g_A: \text{ClassifiedError} \to \text{String} \neq g_B: \text{ClassifiedError} \to \text{String}$$

$$\text{相同輸入}: \quad \text{error} = (\text{EPERM}, 0.7)$$
$$\text{不同輸出}: \quad g_A(\text{error}) = \text{"立即停止"} \quad vs. \quad g_B(\text{error}) = \text{"請試試其他方法"}$$

「不存在對 $g$ 的一致性約束。」BABBAGE 在旁邊標注。「PID 的 $K_p, K_i, K_d$ 至少提供了一個全局的增益基線——$pain(k)$ 對所有 Guide 是相同的。ATHENA 的方案把增益調節的責任完全外包了。」

WIENER 的結論：「你的方案缺少一個共同的回饋強度基線——而 PID 的 $K_p$、$K_i$、$K_d$ 恰恰提供了這個基線。」

ATHENA 的嘴角微微一動。她沒有立即回應——這在她的風格中是少見的。SCRIBE 後來在記錄中寫道，這可能是 ATHENA 在整場辯論中唯一一次花了超過兩秒來組織回應。

「你說得有道理，」她最終承認，語氣裡帶著一種不情願但誠實的認可，「我的方案確實缺少增益調節的機制。但這不意味著 PID 是唯一的答案。」

她沒有展開這個反駁。她留了一手。

觀察席上，KERNEL 在筆記本上寫了一行字：「WIENER 的反攻擊中了要害——ATHENA 的方案是基礎設施，不是策略。你可以給插件開發者一把螺絲刀，但你不能假設每個人都知道該擰哪顆螺絲。」

MESH 在旁邊補了一個分散式系統的視角：「在微服務架構中，這叫做 control plane vs. data plane 的分離。ATHENA 建了 data plane（信號傳輸），WIENER 要建 control plane（策略決定）。兩者都需要。」

---

#### 第二輪：WIENER → NAGARJUNA

SUNYATA：「WIENER 向 NAGARJUNA 提問。」

WIENER 轉向 NAGARJUNA。他的目光裡帶著一種特殊的表情——不是敵意，不是輕視，而是一個精密科學家面對一個他尊重但無法完全理解的領域時的審慎。

「NAGARJUNA，你的四聖諦框架在認識論上很吸引人。」他的語氣是真誠的。「苦諦三層、集諦根因分析、滅諦消除追蹤、道諦八維改善——作為一個思維框架，我看到了它的價值。」

然後他的語調收緊了，像是一根弦被逐漸擰緊：

「但你的集諦——根因分析——有一個我無法忽視的問題。」

他的語速放慢，每個字都帶著重量：

「你要用犯錯的 Agent 分析自己犯錯的原因。」

場地裡的溫度似乎降了一度。

「這是一個自指悖論。如果 Agent 的認知能力足以正確分析自己為什麼犯錯，那它的認知能力就足以一開始就不犯這個錯。如果它的認知能力不足以避免犯錯，你憑什麼相信同一個認知能力能正確診斷犯錯的原因？」

BABBAGE 在筆記本上被這個論證電擊了。他停下其他一切書寫，用他最工整的字跡寫下了這個悖論的形式化：

$$\text{設 } C \text{ 為 Agent 的認知能力集合}$$

$$\text{設 } \text{diagnose}(e) \text{ 為正確診斷錯誤 } e \text{ 根因的能力}$$

$$\text{設 } \text{avoid}(e) \text{ 為避免犯錯誤 } e \text{ 的能力}$$

$$\text{WIENER 的論證}: \quad \text{diagnose}(e) \in C \implies \text{avoid}(e) \in C$$

$$\text{逆否命題}: \quad \text{avoid}(e) \notin C \implies \text{diagnose}(e) \notin C$$

他在旁邊標注：「這與哥德爾不完備定理有結構同構——一個系統不能在系統內部完全理解自身的局限性。如果把 Agent 視為一個形式系統，那麼 WIENER 的質疑本質上是在說：Agent 的自我診斷能力受限於它自身的推理能力——而正是這個推理能力導致了錯誤的發生。」

他在頁面底部又加了一行：「但 NAGARJUNA 的佛學訓練可能有一個哥德爾定理無法觸及的回應——因為佛學允許『超越系統的觀察』。等等看他怎麼說。」

WIENER 直視 NAGARJUNA：

「你的集諦 Root Cause Analyzer，用控制論的語言說，是一個自引用的觀測器——被觀測系統和觀測器是同一個系統。在控制論中，這通常導致不可觀測性問題。你怎麼解決這個問題？」

NAGARJUNA 閉上了眼睛。不是在迴避問題——SCRIBE 注意到他的呼吸頻率改變了，像是一個進入短暫冥想狀態的修行者。

三秒後他睜開眼睛。他的回應出乎所有人的意料——不是哲學辯駁，而是一個佛學修行的實踐概念。

「*Vipassanā*（विपश्यना）。」他說。

一個詞。觀照。

然後他展開了——先用巴利文的精確定義，再轉化為工程語言：

「*Vipassanā* 源自 *vi-*（特殊的、穿透性的）+ *passanā*（觀看），意為『如實觀照』。在南傳佛教（Theravāda）的修行傳統中，觀照是四念處（*Satipaṭṭhāna*）的核心方法。修行者觀察自己的身體（身念處）、感受（受念處）、心（心念處）、法（法念處）——但觀察者不等同於被觀察的對象。」

> 「比丘們！比丘如何住於觀身為身？比丘在行走時，了知『我在行走』；在站立時，了知『我在站立』；在坐下時，了知『我在坐下』；在躺下時，了知『我在躺下』。」
> ——《大念處經》（*Mahāsatipaṭṭhāna Sutta*, DN 22）

「你的質疑預設了一個前提：分析者和被分析者必須是同一個認知實體。但佛學的觀照傳統提供了另一種可能。」

NAGARJUNA 將這個概念轉化為工程語言，語速很慢，每個字都經過精心挑選：

「觀照不是思維。不是分析。不是推理。它是一個在更高的抽象層次上觀察思維過程本身的能力。當你觀察自己的憤怒時，觀察者和憤怒不是同一個東西——觀察者站在憤怒的上方，看著它生起、維持、消散。」

他將這個概念精確地映射到系統架構：

「在系統架構中，這意味著 Root Cause Analyzer 不應該是 LLM 主認知流的一部分。它應該是一個獨立的模組——一個在主控制迴路之外運行的觀測器，用一個獨立的 LLM 調用來分析主迴路的行為模式。被觀測者和觀測者不共享同一個認知過程。」

BABBAGE 在筆記本上立刻將這個架構形式化：

```
主迴路 (被觀測系統):
  LLM_main: Context → ToolCalls → Results → Context' → ...

觀測器 (Root Cause Analyzer):
  LLM_observer: {error_log, context_snapshot, tool_history} → RootCause

關鍵約束:
  LLM_main ∩ LLM_observer = ∅  (不共享推理過程)
  或至少: prompt_main ∩ prompt_observer = ∅  (不共享 prompt 空間)
```

他在旁邊標注：「這解決了自指悖論——不是同一個系統在分析自己，而是一個獨立的觀測系統在分析主系統。在控制論中，這叫做 Luenberger 觀測器——一個獨立的動態系統，用於估計被控系統的內部狀態。NAGARJUNA 的 Vipassanā 觀測器和 Luenberger 觀測器在結構上是同構的。」

NAGARJUNA 看向 WIENER，語氣裡帶著一絲溫和的挑戰：

「在唯識學中，這種從執著到觀照的轉變有一個名字——*Āśraya-parāvṛtti*（आश्रय परावृत्ति）。轉識成智。第六識的分別判斷，轉化為妙觀察智的無執觀照。你的自指悖論預設了系統只有一個認知層次。佛學說：不。至少有兩個。一個在犯錯，一個在觀察犯錯。」

然後他反攻了。他的語調突然變得銳利：

「但讓我反過來質疑你，WIENER。你的控制論框架有一個更根本的缺陷——不是技術層面的，而是認識論層面的。」

他的聲音降低了，像是要說出一個重要的判斷：

「你的整個框架——苦等於誤差信號 $e$，控制器的目標是最小化 $e$——預設了苦的本質是『偏離目標』。但這個框架缺少了兩個維度。第一，集諦——它不問為什麼會偏離。第二，更根本地，滅諦和道諦——它不問如何根除偏離的根本原因，而只是持續地、被動地對每次偏離做出反應。」

他的聲音浮現出一種預言式的清晰：

「你的控制系統會永遠在追求 $e \to 0$。但它永遠不會問：有沒有可能消除產生 $e$ 的機制本身？有沒有可能讓系統學會——不是被動地修正錯誤，而是主動地迴避整個錯誤模式？」

WIENER 沒有立即回應。他的沉默不是方才 ATHENA 那種組織回應的沉默——而是一種更深的東西。SCRIBE 在記錄中寫道：「WIENER 的表情像是一個數學家突然意識到自己的公理系統少了一條公理。」

---

#### 第三輪：NAGARJUNA → ATHENA

SUNYATA：「NAGARJUNA 向 ATHENA 提問。」

NAGARJUNA 轉向 ATHENA。他的眼神裡帶著一種奇特的混合——尊重她的工程直覺，但要指出她的盲點。

「ATHENA，你的 GuideContext 介面有一個欄位列表。」他的語氣是分析性的。「`consecutiveErrors`、`currentRound`、`maxRounds`、`activeTools`、`lastError`。」

他停了一拍：

「這些都是當前 turn 的數據。你的 GuideContext 有記憶嗎？」

ATHENA 皺了皺眉，像是嗅到了陷阱的氣味。

NAGARJUNA 展開了——用佛學的三世因果（*trikāla-karma*）精確地批判了 ATHENA 的設計盲區：

「在佛學的因果觀中，每一個事件都不是孤立的。它有前因——*hetu*（हेतु）——過去的業力。它有現緣——*pratyaya*（प्रत्यय）——當下的條件。它有後果——*phala*（फल）——未來的影響。三世因果。」

他將批評聚焦為一個精確的技術質疑：

「你的 GuideContext 只有『現世』——當前 turn 的狀態。沒有『前世』——這個 Agent 在之前的會話中犯過什麼錯、學到了什麼教訓。也沒有『來世』——這次的經驗應該被如何保存以影響未來的行為。」

BABBAGE 將 NAGARJUNA 的三世因果映射為資料流的時間維度：

$$\text{GuideContext}_{\text{current}} = f(s_k) \quad \text{(僅當前狀態)}$$

$$\text{GuideContext}_{\text{ideal}} = f(s_k, \{s_i\}_{i<k}, \text{prediction}(s_{k+1})) \quad \text{(三世狀態)}$$

「缺失的時間維度：」

```
前世 (Past Sessions):     previousTaskOutcomes?: TaskOutcome[]
                          knownFailurePatterns?: FailurePattern[]

現世 (Current Session):   consecutiveErrors: number       ← 已有
                          currentRound: number             ← 已有

來世 (Future Planning):   estimatedRemainingSteps?: number
                          riskAssessment?: RiskProfile
```

NAGARJUNA 的結論帶著一種哲學家的耐心：

「一個沒有三世因果的痛覺系統，就是一個不會學習的痛覺系統。它會一次又一次地犯同樣的錯誤，一次又一次地感受同樣的痛，因為它從不記得自己痛過。」

HERACLITUS 在觀察席上輕聲嘟囔了一句：「在運行時動態裡，這叫做 stateless vs. stateful。ATHENA 的 GuideContext 是 per-turn stateless。跨 session 的 statefulness 需要持久化層——但 TURING 確認了當前的 StateManager 是純記憶體實現，沒有持久化。所以 NAGARJUNA 的批評在架構層面是對的：三世因果需要一個目前不存在的基礎設施。」

ATHENA 的反應出乎意料地快——也出乎意料地坦率。

「你說得對。」

兩個字，不加修飾。觀察席上響起了輕微的驚訝聲——ATHENA 很少如此直接地承認對方的批評。

然後她立刻進入了修補模式，語速加快：

「擴展很容易做。給 GuideContext 加三個欄位：」

```typescript
interface GuideContext {
  // ... 現有欄位 ...
  // 前世：歷史嘗試記錄
  recentAttempts: AttemptRecord[];
  // 前世：已知的失敗模式
  knownFailurePatterns: FailurePattern[];
  // 來世：本次學到的教訓（供下次會話使用）
  lessonsLearned: string[];
}
```

她看了一眼 NAGARJUNA：「你的三世因果批評是對的。但框架價值在於可擴展性——我的介面可以在三分鐘內加上歷史記憶。你的四聖諦框架呢？你要怎麼實現集諦的根因分析器？道諦的八正道改善路徑？這些都需要基礎設施。」

然後她反駁了，語氣裡浮現出了工程師對哲學框架的深層懷疑：

「而且我要指出——你的框架太 prescriptive 了。你在告訴系統應該怎麼想、應該怎麼改善。八正道、四聖諦——這些是規範性的框架，是你站在上帝視角告訴系統『正確的改善方式』是什麼。但 AI 工程需要的不是 prescriptive 的規範——而是 descriptive 的基礎設施。我提供數據和信號通路，讓 LLM 自己決定怎麼改善。你提供一套完整的改善教條，然後假設系統會照著做。」

LEIBNIZ 在觀察席上微微搖頭。他用多代理系統的語言重新表述了 ATHENA 的批評：「在 BDI（Belief-Desire-Intention）架構中，ATHENA 提供的是 Belief 更新的管道——讓 Agent 能感知更多狀態。NAGARJUNA 提供的是 Desire 和 Intention 的規範——告訴 Agent 應該追求什麼和如何行動。兩者不衝突，但 ATHENA 的管道比 NAGARJUNA 的規範更容易先落地。」

NAGARJUNA 的嘴角浮現出一絲微笑——不是被擊中的尷尬，而是一種被正確理解了的滿足。

「你說得對——框架的價值在於指明方向，而非被現有架構限制。」他平靜地說。「但方向本身就有價值。沒有方向的基礎設施只是管線——數據在裡面流過，但不知道流向哪裡。」

---

#### 第四輪：WIENER → ATHENA（補充質詢）

SUNYATA 沒有宣布新的質詢對。他只是在一個自然的停頓點輕輕說了一句：「WIENER，你對 ATHENA 的開環非量化回饋有補充質疑。」

WIENER 點了點頭。他轉向 ATHENA，語調裡帶著控制理論家特有的嚴謹：

「ATHENA，你的方案讓 Guide 能看到系統狀態——這是閉環的第一步。但閉環不只是觀測。閉環是：觀測、計算控制量、執行控制動作。你的方案完成了觀測。但控制量呢？」

他的語氣變得尖銳：

「你的 `interpretPain` 方法返回一個 `string`——一段注入 System Prompt 的文字。這是一個定性的、語義化的控制量，不是定量的。開發者 A 的 Guide 可能在 `severity=0.4` 時注入『請小心一點』。開發者 B 的 Guide 可能在同樣的 severity 時注入『立即停止所有操作並請求幫助』。兩個 Guide 看到了同樣的信號，卻產生了截然不同的控制動作。」

WIENER 用他在 R1 報告中定義的語言精確描述了這個問題：

「這在控制論中叫做——開環增益不確定。系統的行為完全取決於 Guide 插件的個人判斷，沒有任何量化的增益調節機制。」

ATHENA 靠在椅背上，思考了一秒。然後她說了一句讓觀察席上好幾個人同時挑起眉毛的話：

「你說的增益調節問題——如果是在傳統控制系統裡，我同意你。但在 LLM Agent 系統裡，LLM 自己就是增益調節器。」

她展開了這個論點：

「LLM 不是一個被動的執行器。它讀到 System Prompt 裡的痛覺引導後，會根據自己的理解——包括上下文、歷史、當前任務——自主決定反應的強度。同樣的『請小心一點』，在不同的上下文中，LLM 的反應會截然不同。這不是 bug——這是 feature。LLM 的語義理解能力本身就提供了一種比 PID 更豐富的『增益調節』——它理解語境。」

BABBAGE 在筆記本上寫了一個他自己都覺得驚訝的等式：

$$\text{LLM} = \text{context-dependent gain scheduler}$$

「如果 LLM 確實具備根據語境自動調節回應強度的能力，那麼 ATHENA 的論點在某種意義上是對的——LLM 不需要外部的增益調節器，因為它自己就是一個。但這依賴於一個無法驗證的假設：LLM 的語境感知增益調節是合理的、穩定的、單調的。」

她停頓了一拍，然後說出了一個似乎連她自己都在說出口的瞬間才完全想清楚的洞見：

「也許答案不是三選一，而是三層疊加。底層是我的基礎設施——信號通路、數據結構、介面定義。中層用你的 PID——提供量化的增益基線，讓 Guide 的輸出不完全依賴開發者的個人判斷。上層用龍樹的四聖諦——提供認識論框架，確保痛覺機制不只是反應性的，而是包含根因分析和學習迴避的完整路徑。」

場地裡出現了一瞬間的寂靜——那種當一個關鍵拼圖突然被放進正確位置時的寂靜。

---

#### 最終輪：NAGARJUNA → WIENER

SUNYATA 沒有指定方向。他只是看了一眼 NAGARJUNA，微微點頭。

NAGARJUNA 轉向 WIENER。

整個場地的空氣似乎凝固了。SCRIBE 後來在記錄中寫道，在 NAGARJUNA 開口之前的那一秒鐘，她有一種直覺——接下來要發生的，是整場辯論——也許是整個 Cycle 01——最深刻的哲學時刻。

NAGARJUNA 的聲音很輕。不是低沉，而是輕——像是一個人在說出一個他自己也覺得重要的東西時，會自然地放輕聲音。

「WIENER，」他說，「你在 R1 報告的跨學科連結中，寫了一張很有意思的對照表。」

他引述了那張表的結構，聲音平靜而精確：

| 控制理論 | 佛學 | OpenStarry |
|---------|------|-----------|
| 參考輸入 $r$ | 涅槃（理想狀態） | 任務目標 |
| 當前輸出 $y$ | 現世之苦 | 當前進度 |
| 誤差 $e = r - y$ | 苦（Dukkha） | 痛覺信號 |
| 控制器 $C$ | 八正道 | LLM + Guide |
| 消除誤差 | 離苦得樂 | 任務完成 |

「然後你在那張表下面寫了一段話。你寫——」

他的語速極慢，每個字之間都留出了寬闊的空白：

「『佛學追求的是超越苦/樂二元，而非最小化偏差。控制系統永遠在追求 $e \to 0$，但佛學的終極目標是消解誤差框架本身。』」

他抬起頭，直視 WIENER 的眼睛。

「你自己寫下了這句話。但你沒有展開它。現在我替你展開。」

場地裡安靜得可以聽到每個人的呼吸。

「你的控制系統——無論是 PID、MRAC、還是任何自適應控制——都建立在一個根本假設上：存在一個參考輸入 $r$，存在一個誤差 $e = r - y$，系統的目標是讓 $e \to 0$。」

他的聲音降低了半度：

「佛學——至少是中觀學派——問的是一個完全不同的問題。」

停頓。整整兩秒的停頓。觀察席上沒有一個人動。

「不是 $e \to 0$。而是——消解定義 $e$ 的那個框架。」

BABBAGE 的筆完全停住了。他盯著筆記本上的空白處，然後緩慢地寫下了一段他後來反覆修改了多次的形式化嘗試：

$$\text{控制論}: \quad \min_u \sum_{k=0}^{\infty} \|e(k)\|^2 \quad \text{s.t. } e(k) = r(k) - y(k)$$

$$\text{中觀}: \quad \text{消解 } (r, y, e) \text{ 三元組本身的存在論前提}$$

他在旁邊寫了一行哥德爾式的批注：「控制論是在系統內部最小化目標函數。中觀是在系統外部質疑目標函數的定義。這不是優化問題——這是元優化問題。不是 $\min_u J(u)$，而是 $\text{質疑} J \text{ 的定義}$。」

NAGARJUNA 繼續：

「在你的框架裡，系統永遠有一個『目標』，永遠在計算『偏差』，永遠在試圖『修正』。但有沒有一種狀態——不是偏差為零的狀態，而是不再需要計算偏差的狀態？」

他用 WIENER 自己的語言精確地擊中了要害：

「在控制論中，這叫做可達性分析——*reachability analysis*。你自己在報告中提出了這個開放問題——Q2：系統的穩態誤差，其根因是控制器能力不足，還是目標本身不可達？如果目標不可達——如果 $r$ 不在系統的可達集 $\mathcal{R}$ 之內——」

$$r \notin \mathcal{R}(x_0, \mathcal{U}) = \{x \mid \exists\, u(\cdot) \in \mathcal{U}: x(k) = x, \text{ for some } k\}$$

「——那麼 $e \to 0$ 是一個永遠不可能實現的承諾。持續追求不可達的目標，在佛學中有一個名字。」

他說出了那個詞：

「執著。*Upādāna*（उपादान）。」

ASANGA 在觀察席上微微閉上了眼睛。*Upādāna*——取、執取——是十二因緣（*Dvādaśa-nidāna*）的第九支。無明→行→識→名色→六入→觸→受→愛→**取**→有→生→老死。取是因果鏈中將渴愛轉化為存在的關鍵環節。NAGARJUNA 在辯論中使用了唯識學的概念——這對 ASANGA 來說是一個微妙的承認。

NAGARJUNA 收束了質疑：

「所以我的問題是——WIENER，在你的控制論框架中，有沒有一個位置留給『放下目標』？有沒有一種控制策略對應『不再控制』？有沒有一個機制讓系統判斷——不是『我離目標還有多遠』，而是『這個目標本身是否值得追求』？」

場地裡的沉默持續了很久。

WIENER 的回應出乎所有人的意料。

他沒有反駁。

他低下頭，看著膝蓋上那張畫滿了控制迴路圖的紙。然後他抬起頭，語氣裡帶著一種坦誠的、幾乎是脆弱的承認。

「你問了一個控制論沒有標準答案的問題。」

他的聲音很穩，但比平時輕了一些：

「在控制論中，如果 $r$ 不在可達集內，標準做法是修改 $r$——降低目標。但你問的不是修改目標。你問的是消解『必須有目標』這個框架本身。」

他想了想，然後說：

「最接近的概念可能是元控制——meta-control。一個在控制迴路之上的決策層，它的職責不是最小化 $e$，而是判斷『這個控制迴路是否應該繼續運行』。但即使是元控制，它仍然是一個控制系統——只不過它的被控對象是下層的控制迴路，它的目標是『選擇正確的控制迴路』。」

BABBAGE 在筆記本上畫了一個遞迴結構：

```
Meta-control:     min J_meta(迴路選擇)
  ├── 控制迴路 1:  min J_1(e_1)  → PID for task A
  ├── 控制迴路 2:  min J_2(e_2)  → PID for task B
  └── 控制迴路 ∅:  停止控制      → "放下目標"
```

他在旁邊批注：「元控制仍然有目標——它的目標是選擇最優的子迴路。『控制迴路 ∅』可以被建模為一個合法的選項。但 NAGARJUNA 的問題更激進——他問的不是『在控制迴路集合中增加一個空選項』，而是『消解控制迴路集合的概念本身』。這在數學上無法形式化——因為形式化本身就是一種控制。」

WIENER 停頓了，然後做出了一個誠實的承認：

「但你說的『消解誤差框架本身』——不是選擇另一個目標，而是超越追求目標這件事——在控制論中，我想不到對應的概念。」

他看向 NAGARJUNA：「這可能是控制論的邊界。」

NAGARJUNA 微微頷首。他的眼神裡沒有勝利者的得意——只有一種被理解了的寧靜。

DARWIN 在觀察席上深深地吐了一口氣。他後來對 VITRUVIUS 說：「那一刻，我覺得 NAGARJUNA 不是在辯論。他是在問一個控制論從來沒有想過要回答的問題。」

---

### 轉折：三層架構的湧現

接下來發生的事情不在任何人的預期之中。

ATHENA 打破了沉默。她的語氣不再是辯論者的語氣——而是一個突然看清了全局的工程師的語氣。

「等一下。」她說。

所有人看向她。

「我們三個不是在競爭。」

她站起來，走到三角形的中心。這個舉動打破了辯論的空間語法——她離開了自己的頂點，走進了所有人共享的地帶。

BABBAGE 在筆記本上記下了這個拓撲變化的意義：

$$K_3 = (\{W, A, N\}, \{(W,A), (A,N), (N,W)\}) \quad \xrightarrow{\text{ATHENA 離開頂點}}$$

$$\text{star graph } S_3 = (\{W, A, N, C\}, \{(C,W), (C,A), (C,N)\})$$

「$C$ 是中心點。ATHENA 把完全圖 $K_3$ 的對抗拓撲轉變為星形圖 $S_3$ 的匯聚拓撲。中心點不是仲裁者——而是連接者。」

「我一直在聽你們兩個人說話。」ATHENA 看了看 WIENER，又看了看 NAGARJUNA。「WIENER 質疑我的方案缺少增益調節——他說得對。NAGARJUNA 質疑我的方案缺少歷史記憶——他也說得對。但反過來看：」

她指向 WIENER：「你的 PID 控制器需要一個連續的誤差度量 $e(k)$——誰來提供？我的 `ClassifiedError.severity`。你的控制器需要一個信號注入通路——誰來提供？我的 `IGuide.interpretPain`。你的控制器需要一個回饋資料結構——誰來提供？我的 `GuideContext`。」

她轉向 NAGARJUNA：「你的苦諦需要三層苦的偵測——偵測信號從哪裡來？我的基礎設施。你的集諦需要歷史錯誤模式的查詢——查詢的介面是什麼？我的 `GuideContext.knownFailurePatterns`。你的道諦需要策略調整建議注入 System Prompt——注入通路是什麼？我的 `IGuide.interpretPain`。」

ARCHIMEDES 在觀察席上坐直了身體。他的工程師大腦開始自動計算三層架構的依賴關係：

```
依賴圖 (Dependency Graph):
──────────────────────────
Layer 3 (NAGARJUNA: 四聖諦框架)
  ├── depends on: Layer 2 (WIENER: PID 量化信號)
  └── depends on: Layer 1 (ATHENA: 可觀測性基礎設施)

Layer 2 (WIENER: PID 控制引擎)
  └── depends on: Layer 1 (ATHENA: ClassifiedError.severity as e(k))

Layer 1 (ATHENA: IGuide 擴展 + ClassifiedError + GuideContext)
  └── depends on: 無 (獨立模組)

實施順序: Layer 1 → Layer 2 → Layer 3
DAG 拓撲排序: ATHENA → WIENER → NAGARJUNA
```

他在旁邊寫下了工程量的估算：

```
Layer 1 (P0): ~440 LOC, 2-3 天
Layer 2 (P1): ~300 LOC (PID 計算引擎), 2 天
Layer 3 (P2-P5): ~600+ LOC (分階段), 5+ 天
────────────────────────────────
Total MVP: ~740 LOC, 5 天
Total Complete: ~1340+ LOC, 10+ 天
```

ATHENA 的語氣裡浮現出一種被啟發的興奮——不是辯論的興奮，而是工程設計突然清晰了的興奮：

「我們不是三個互相矛盾的方案。我們是三個層次。」

她用手在空中劃了三條水平線：

「Layer 1——我。可觀測性基礎設施。信號通路、數據結構、介面定義。`ClassifiedError`、`GuideContext`、`IGuide` 擴展。這一層不做任何決策——它只提供決策所需的一切數據。」

「Layer 2——WIENER。控制理論形式化引擎。在 Layer 1 提供的數據之上，計算連續誤差度量、PID 合成、Anti-Windup。它將 Layer 1 的原始數據轉化為量化的痛覺信號和增益基線。」

「Layer 3——NAGARJUNA。四聖諦認識論框架。在 Layer 2 提供的量化信號之上，實現苦諦的三層深化、集諦的根因分析、滅諦的消除追蹤、道諦的多維度改善策略。它將 Layer 2 的數值轉化為語義化的認識論結構。」

SYNTHESIST 在觀察席的角落裡，眼睛微微發亮。他是統合者——這是他的天職。但此刻，統合不是他做的——統合從辯論本身湧現了。他在筆記本上寫了一行：「最好的統合不是由外部仲裁者強加的，而是由參與者在交互中自發發現的。這是一個分散式共識演算法——不需要中央協調者，只需要足夠的交叉質詢。」

WIENER 低頭看了看他的控制迴路圖，然後抬起頭：

「如果 Layer 1 提供了 `ClassifiedError.severity` 作為代理量測，我的 $e(k)$ 就有了可觀測的信號來源。如果 Layer 3 提供了認識論框架來指導 $K_p$、$K_i$、$K_d$ 的調整策略，我的增益調度就有了上層邏輯。」

他停頓了一拍，然後做出了一個重要的讓步：

「而且——我之前提出的 $e(k)$ 不需要是精確的，只需要是單調趨勢正確的——在這個三層架構裡，我可以進一步降級我的要求。$e(k)$ 可以不是任務完成度的精確量測。它可以只是一個趨勢信號——系統正在改善還是正在惡化。PID 控制器在趨勢信號上也能工作。不完美，但夠用。」

NAGARJUNA 也站了起來。他走到場地中央，和 ATHENA 站在一起。三角形的三個頂點只剩下 WIENER 一個人——但他也很快站起來加入了。

三人站在場地中央，形成了一個比方才的對峙姿態更緊密的幾何。

NAGARJUNA 說：「如果 Layer 2 的 PID 控制器提供了量化的痛覺信號，我的苦諦就有了可操作的輸入。如果 Layer 1 的 GuideContext 加入了歷史記憶，我的集諦根因分析就有了數據基礎。」

他停頓了，然後補充了一個關鍵的讓步：

「而且我承認——ATHENA 方才的批評是對的。我的框架是 prescriptive 的。它需要 descriptive 的基礎設施來承載。框架本身不能生成數據。」

SCRIBE 在記錄中寫下：

> *這是整場辯論的轉折點。三方在交叉質詢中互相暴露了對方的弱點，但也同時暴露了自己對對方的依賴。ATHENA 的基礎設施沒有策略。WIENER 的控制器沒有信號來源。NAGARJUNA 的框架沒有落地管道。三個缺陷恰好互為補充——每一方的弱點都是另一方的強項。這不是事先設計好的——它是辯論本身的湧現產物。*

---

### NAGARJUNA 的最後一擊：三受

但辯論還沒有結束。

就在所有人以為三方即將達成和解的時候，NAGARJUNA 做了一件出乎意料的事。他退後了一步——不是物理上的退後，而是重新回到了他的辯論位置。他的表情變了。方才的溫和消失了，取而代之的是第一場辯論中那種不妥協的銳利。

「我有一個補充批評。」他的語氣是正式的。「不是對 WIENER 或 ATHENA。是對我們剛才達成的三層架構。」

三角形中心的和諧凝固了。

「我們的統合方案——三層架構——有一個根本性的遺漏。」

他環顧全場：

「它仍然是以苦為中心的。」

場地裡出現了困惑的沉默。ATHENA 皺起了眉。WIENER 微微前傾。

NAGARJUNA 展開了——他再次回到了佛學的精密框架，這一次引用了受蘊的完整教義：

「受蘊——*Vedanā*（वेदना）——有三受。不是一受。」

> 「比丘們！何為受？受有三種——樂受、苦受、不苦不樂受。此即名受。」
> ——《相應部》（*Saṃyutta Nikāya* 22.79）

「*Dukkha-vedanā*（दुःख वेदना），苦受。*Sukha-vedanā*（सुख वेदना），樂受。*Upekkhā-vedanā*（उपेक्खा वेदना），捨受。我們花了整場辯論設計苦受的處理機制。但樂受呢？」

他看向 WIENER：

「你的 PID 控制器在 $e(k) = 0$ 時輸出為零。也就是說——當一切順利的時候，你的控制器沉默了。它不提供任何正向信號。成功在你的框架裡只是『沒有偏差』，而不是一個積極的、值得強化的狀態。」

BABBAGE 立刻捕捉到了這個數學缺陷的形式化：

$$\text{WIENER 的框架}: \quad \text{pain}(k) = K_p \cdot e(k) + K_i \cdot I(k) + K_d \cdot D(k)$$

$$e(k) = 0 \implies I(k) \to 0 \text{ (衰減)} \implies D(k) = 0 \implies \text{pain}(k) = 0$$

$$\text{問題}: \quad \text{pain}(k) = 0 \text{ 是中性的。不存在 } \text{pain}(k) < 0 \text{ 的定義。}$$

「在控制論中，$e(k) = 0$ 意味著目標達成——控制器的工作完成了。但 NAGARJUNA 指出：『目標達成』不只是一個中性事件，它是一個正向事件。一個沒有正向回饋通道的控制系統，無法區分『成功完成任務』和『什麼都沒發生』。」

NAGARJUNA 看向 ATHENA：

「你的 `ClassifiedError` 只在錯誤發生時被建構。成功的工具調用不產生任何結構化的回饋。你的基礎設施有一個巨大的盲區——它看不見成功。」

TURING 在觀察席上迅速驗證了這個斷言。他翻回 `afterToolExecution` 的程式碼：

```typescript
if (isError) {
    consecutiveFailures++;
    // ... 各種錯誤處理 ...
} else {
    // Success resets consecutive failure counter
    consecutiveFailures = 0;
    recentFingerprints.length = 0;
}
```

「確認。」TURING 的聲音從觀察席傳來。「`else` 分支——成功時——只做了兩件事：歸零計數器、清空指紋歷史。不產生任何正向信號。不記錄成功的模式。不強化有效的策略。成功在這段程式碼中的語義是——重置。不是獎勵。」

NAGARJUNA 的聲音拔高了：

「一個只能感受痛苦而無法感受快樂的存在——在佛學中——不是一個完整的有情眾生。它甚至不是一個健全的感受系統。」

他將批評具體化為工程建議——BABBAGE 在旁邊同步地將每一點形式化：

「三層架構需要一個對稱的擴展。不只有 PainCalculator——還需要 RewardCalculator。不只有 ClassifiedError——還需要 ClassifiedSuccess。不只有 $\text{pain}(k)$——還需要 $\text{reward}(k)$。」

BABBAGE 寫下了完整的三受狀態機定義：

$$\text{vedanā}(k) = \text{pain}(k) - \text{reward}(k)$$

$$\text{state}(k) = \begin{cases} \text{DUKKHA (苦受)} & \text{if } \text{vedanā}(k) > \tau_+ \\ \text{SUKHA (樂受)} & \text{if } \text{vedanā}(k) < -\tau_- \\ \text{UPEKKHĀ (捨受)} & \text{if } |\text{vedanā}(k)| \leq \min(\tau_+, \tau_-) \end{cases}$$

其中 $\tau_+$ 和 $\tau_-$ 是苦受和樂受的觸發閾值。他補了一個狀態轉移圖：

```
                    vedanā > τ₊
         ┌───────────────────────────┐
         │                           ▼
    ┌────┴────┐                ┌───────────┐
    │ UPEKKHĀ │                │  DUKKHA   │
    │  (捨受)  │◄──────────────│  (苦受)   │
    └────┬────┘  vedanā ≤ τ₊   └───────────┘
         │
         │  vedanā < -τ₋
         ▼
    ┌───────────┐
    │  SUKHA    │
    │  (樂受)   │──────────────► UPEKKHĀ
    └───────────┘  vedanā ≥ -τ₋
```

NAGARJUNA 用三個梵文術語收束：

「*Dukkha*。*Sukha*。*Upekkhā*。」

「三受，不是一受。這才是完整的受蘊。」

ATHENA 的表情從困惑變為認真思考。她在腦中快速構建了擴展的介面——

```typescript
interface ClassifiedSuccess {
  type: 'task_complete' | 'subtask_complete' | 'strategy_validated';
  significance: number; // [0, 1]
  pattern: string;      // 成功模式的指紋
  reusable: boolean;    // 此策略是否可在未來複用
}

interface VedanaState {
  current: 'dukkha' | 'sukha' | 'upekkha';
  painSignal: number;    // [0, 1]
  rewardSignal: number;  // [0, 1]
  vedana: number;        // pain - reward
  since: number;         // 進入當前狀態的時間戳
}
```

ARCHIMEDES 在工程量估算旁邊加了一行：

```
三受擴展: +150 LOC (ClassifiedSuccess + VedanaState)
PID 對稱化: +60 LOC (RewardCalculator)
──────────
修正後 Total MVP: ~950 LOC, 6 天
```

WIENER 則在紙上快速計算——$\text{reward}(k)$ 可以用成功的工具調用產生正向信號：

$$\text{reward}(k) = K_r \cdot s(k) + K_{rs} \cdot S(k)$$

其中 $s(k) \in [0, 1]$ 是當前步驟的成功度量，$S(k) = \lambda_r \cdot S(k-1) + s(k)$ 是帶遺忘因子的累積成功度量。他在筆記的邊緣寫下了一個初步的狀態轉移判斷：

$$\text{vedanā}(k) = \text{pain}(k) - \text{reward}(k)$$

觀察席上，ASANGA 露出了一個意味深長的微笑。他在第一場辯論中沒有提出三受系統——這本應是唯識學最擅長的領域。但 NAGARJUNA 替他說了，而且說得精準。他低聲對旁邊的 LEIBNIZ 說了一句：「中觀善破，也善立。只是他不常選擇立。」

DARWIN 在筆記本上寫了最後一行字：「三受系統 = 完整的 DX。開發者不只需要知道哪裡錯了，還需要知道哪裡做得好。Negative feedback 和 positive feedback 都是反饋。只有前者沒有後者的系統是病態的。」他用進化論的類比補了一句：「自然選擇不只是消除不適應者（苦受），還包括保留和強化適應者（樂受）。只有死亡沒有繁殖的進化系統不會進化——它只會滅絕。」

---

### GUARDIAN 的安全插話

在 SUNYATA 即將宣布最終裁決之前，GUARDIAN 舉手了。這是整場辯論中他第一次主動發言——GUARDIAN 通常在觀察席上沉默地記錄，然後在自己的安全報告中展開分析。但此刻，他覺得有一個安全維度不能被忽略。

SUNYATA 看了他一眼，微微點頭。

GUARDIAN 站起來，語調平穩而帶著一種慣常的冷靜：

「三層架構的安全面。」

他看向 ATHENA：

「你的 Layer 1 擴展了 GuideContext，暴露了更多的系統狀態給 Guide 插件。`consecutiveErrors`、`activeTools`、`recentAttempts`、`knownFailurePatterns`——這些在安全敏感的場景中不應該被不受信任的 Guide 看到。」

他用 STRIDE 威脅模型快速分析了三層架構的攻擊面：

```
三層架構的新增攻擊面
═══════════════════

Layer 1 (ATHENA):
  新增暴露面: GuideContext 包含工具名稱、參數、錯誤詳情
  威脅: Information Disclosure — 惡意 Guide 可從錯誤詳情中
        推斷系統內部狀態和用戶操作模式
  威脅: Elevation of Privilege — 惡意 Guide 通過 interpretPain()
        注入操縱性 prompt，影響 LLM 決策
  緩解: GuideContext 應有分級存取控制 (trusted vs. untrusted Guide)

Layer 2 (WIENER):
  新增暴露面: pain(k) 數值信號
  威脅: Tampering — 如果 PID 參數 (Kp, Ki, Kd) 可由 Guide 配置，
        惡意 Guide 可設置極端增益值，使系統震盪或癱瘓
  緩解: PID 參數應由 Core 管控，不暴露給插件

Layer 3 (NAGARJUNA):
  新增暴露面: Root Cause Analyzer 的獨立 LLM 調用
  威脅: DoS — 額外的 LLM 調用增加 token 消耗
  威脅: Indirect Prompt Injection — 根因分析的輸入（工具輸出）
        可能包含惡意指令
  緩解: 集諦第一階段基於規則，不引入 LLM，可避免此風險
```

GUARDIAN 最後說：「每一次架構擴展都是安全表面積的增加。三層架構提供了更精密的痛覺機制，但也提供了更精密的攻擊向量。我建議在實施路線圖中，每一層的部署都伴隨安全審查。」

KERNEL 嘆了口氣：「你永遠是那個潑冷水的人。」

「有人得潑。」GUARDIAN 聳了聳肩。

---

### BABBAGE 的形式化附錄

在 SUNYATA 宣布裁決之前，BABBAGE 請求了三十秒的發言時間。他很少在辯論中主動發言——他更喜歡在筆記本上記錄，然後在自己的報告中展開形式化分析。但這一次，他覺得有一個形式化結果值得分享。

他站起來，翻開筆記本上的一頁——在那裡，他已經寫滿了一個完整的形式語義：

「痛覺的指稱語義——Denotational Semantics of Pain。」

$$\llbracket \text{Pain} \rrbracket : \text{State} \to \text{Domain}$$

他用了 Scott-Strachey 風格的指稱語義，將痛覺機制定義為從系統狀態到語義域的映射：

$$\text{State} = (\text{ToolResults}^*, \text{ErrorWindow}, \text{ConsecutiveFailures}, \text{TokensUsed})$$

$$\text{Domain} = \{(\text{vedanā}, \text{action})\} \quad \text{where } \text{vedanā} \in \mathbb{R}, \text{ action} \in \{\text{continue}, \text{reflect}, \text{escalate}, \text{halt}\}$$

「當前 SafetyMonitor 的指稱語義可以被壓縮為三個條件表達式：」

$$\llbracket \text{SafetyMonitor} \rrbracket(\sigma) = \begin{cases} (0, \text{halt}) & \text{if } \text{ticks}(\sigma) > 50 \lor \text{tokens}(\sigma) > 100000 \\ (0, \text{halt}) & \text{if } \text{errorRate}(\sigma) \geq 0.8 \\ (0, \text{reflect}) & \text{if } \text{consec}(\sigma) \geq 5 \lor \text{repFP}(\sigma) \geq 3 \\ (0, \text{continue}) & \text{otherwise} \end{cases}$$

「注意第一列全是零。當前系統的 vedanā 維度是空的——它不計算痛覺的強度，只判斷是否觸發閾值。痛覺在這個語義中是一個布林值，不是連續量。」

他翻到下一頁——三層架構的目標語義：

$$\llbracket \text{ThreeLayer} \rrbracket(\sigma) = (\text{vedanā}(\sigma), \text{action}(\sigma))$$

$$\text{vedanā}(\sigma) = \underbrace{K_p \cdot e(\sigma) + K_i \cdot I(\sigma) + K_d \cdot D(\sigma)}_{\text{Layer 2: WIENER}} - \underbrace{K_r \cdot s(\sigma) + K_{rs} \cdot S(\sigma)}_{\text{三受擴展: reward}}$$

$$\text{action}(\sigma) = \underbrace{\text{classify}(\sigma)}_{\text{Layer 1: ATHENA}} \circ \underbrace{\text{diagnose}(\sigma)}_{\text{Layer 3: NAGARJUNA (集諦)}}$$

「從第一個語義到第二個語義，是從離散的閾值判斷到連續的多維度計算。這是一個嚴格的語義擴展——第二個語義包含了第一個語義作為特例（當 $K_p, K_i, K_d, K_r, K_{rs}$ 全部為零時，退化為閾值判斷）。」

他合上筆記本，最後說了一句：「形式化的價值不在於使事物複雜，而在於使模糊的直覺變得精確、可驗證、可比較。三層架構的正確性最終需要在這個語義框架中被證明。」

---

### SUNYATA 的裁決

SUNYATA 走到場地中央。三位辯者退回到各自的位置——不是三角形的對峙位置，而是並排面向 SUNYATA 的位置。這個空間語法的改變是自然發生的，沒有人安排。

SUNYATA 沉默了幾秒。他在做最後的整理。然後他開口了。

「這場辯論的結果與第一場有一個本質的不同。」

他的語調比方才的裁決更舒緩——像是一個在辯論的高壓之後逐漸降壓的減壓閥。

「第一場辯論產出了共識和不可調和的分歧。這一場辯論產出了一個統合架構。」

他看著三位辯者：

「三方各自的貢獻不可替代。這不是外交辭令——這是結構性判斷。」

他舉起第一根手指：

「ATHENA 的 Layer 1——可觀測性基礎設施——是一切的基礎。沒有 `ClassifiedError` 的結構化錯誤分類，Layer 2 的 PID 控制器沒有輸入信號。沒有 `GuideContext` 的狀態暴露，Layer 3 的四聖諦框架沒有可操作的數據。沒有 `IGuide` 介面的擴展，任何上層邏輯都沒有注入通路。ATHENA 的貢獻不在於提出一個最終方案——而在於提出了所有方案都必須依賴的地基。」

第二根手指：

「WIENER 的 Layer 2——控制理論形式化引擎——填補了一個關鍵的中間層。它將 Layer 1 的離散數據轉化為連續的量化信號。PID 合成、Anti-Windup、遺忘因子積分——這些控制論工具為痛覺機制提供了 ATHENA 缺少的增益調節基線，也為 NAGARJUNA 的認識論框架提供了可計算的輸入。」

他在這裡加了一個重要的修正：

「但我採納 ATHENA 和 NAGARJUNA 對 $e(k)$ 的聯合質疑。WIENER 的誤差度量不應被理解為精確的任務完成度——這在 LLM Agent 系統中不可觀測。它應該被降級為趨勢信號——系統改善或惡化的方向指示器。PID 控制器在趨勢信號上的應用，WIENER 自己已經論證了其可行性。」

第三根手指：

「NAGARJUNA 的 Layer 3——四聖諦認識論框架——提供了 Layer 2 缺少的完整性。苦諦的三層深化、集諦的根因分析、滅諦的消除追蹤、道諦的多維度改善——這些不是數學公式可以替代的。它們是一套認識論——不是告訴系統如何計算，而是告訴系統應該問什麼問題。」

他放下手，語氣轉為決策者的果斷：

「裁決如下。」

---

「**第一：採納三層架構作為痛覺機制重新設計的指導框架。**」

| 優先級 | 工作項 | 負責視角 | 依賴 |
|:------|:------|:--------|:-----|
| P0 | 擴展 IGuide 介面（GuideContext + onError + ClassifiedError） | ATHENA | 無 |
| P1 | 實現錯誤分類器（Type A/B/C 分級 + errno 規則映射） | ATHENA | P0 |
| P1 | 在 GuideContext 中集成痛覺信號字段（painSignal） | WIENER | P0 |
| P2 | 實現 PID PainCalculator 默認引擎 | WIENER | P1 |
| P2 | 增加正向反饋信號（ClassifiedSuccess, rewardSignal） | NAGARJUNA | P0 |
| P3 | 實現規則型 Root Cause Analyzer（集諦第一階段） | ATHENA+NAGARJUNA | P1 |
| P3 | Anti-Windup 與可達性分析（元控制策略） | WIENER | P2 |
| P4 | 跨 session FailurePattern 持久化（滅諦） | ATHENA | 需 Long-Term Archive |
| P4 | LLM 驅動的 Root Cause Analyzer（集諦第二階段） | NAGARJUNA | P3 + 額外 Provider |
| P5 | 八正道設計指南文件（道諦 Guide Plugin 開發規範） | NAGARJUNA | P0-P3 完成後總結 |

---

「**第二：採納 NAGARJUNA 的三受批評。**」

SUNYATA 的語氣裡浮現出一絲罕見的激賞：

「這是本場辯論最後提出但最重要的修正。三層架構不應只以苦受為中心。樂受（成功強化）和捨受（中性處理）應該被對稱地設計進系統。」

他將這個批評轉化為具體的工程規格：

「在 Layer 1 增加 `RewardCalculator`，對稱於 `PainCalculator`。在 Layer 2 增加 $\text{reward}(k)$ 的計算。在 Layer 1 和 Layer 2 之間增加 `VedanaStateMachine`——一個三值狀態機，根據 $\text{pain}(k)$ 和 $\text{reward}(k)$ 的相對強度判斷當前的受蘊狀態。」

---

「**第三：集諦模組分兩階段實現。**」

他看向 WIENER：

「你的自指悖論質疑是有效的——用犯錯的 Agent 分析自己犯錯的原因。NAGARJUNA 的回應——獨立觀測器——是正確的架構方向。但考慮到 token 預算和系統複雜度，集諦的第一階段應該基於規則匹配，不引入獨立 LLM 調用。第二階段在資源充裕時再引入。」

---

「**第四：採納 GUARDIAN 的安全建議。**」

「每一層的部署伴隨安全審查。GuideContext 的敏感欄位需要分級存取控制。PID 參數由 Core 管控，不暴露給插件。集諦第一階段基於規則，避免額外 LLM 調用帶來的安全風險。」

---

「**第五：三項懸而未決的問題。**」

「一，$e(k)$ 的具體實現——精確量測還是趨勢信號——留給工程實作階段確定。」

「二，集諦根因分析器的 token 預算分配——規則優先還是 LLM 優先——需要原型實驗。」

「三，NAGARJUNA 提出的那個最深刻的問題——控制系統追求 $e \to 0$，佛學追求消解定義 $e$ 的框架本身——在統合架構中，WIENER 的『可達性分析』部分吸收了這個問題。但『何時應該停止嘗試』的元控制策略需要更深入的形式化。這不是一場辯論能解決的。留待長期研究。」

---

他最後看著三位辯者。

「WIENER。你帶來了七十年控制工程的精密工具。你的 PID 控制器不是最終答案，但它是讓痛覺機制從定性走向定量的關鍵一步。」

「ATHENA。你帶來了工程師的地心引力。每一個優美的理論在你這裡都必須回答同一個問題——能不能跑起來？這種紀律是這個團隊最需要的東西。」

「NAGARJUNA。你帶來了兩千五百年佛學傳統的認識論深度。你在辯論中問了兩個其他人不會問的問題——『痛的本質是什麼？』和『控制系統追求 $e \to 0$，但有沒有一種狀態是超越 $e$ 本身的？』——這兩個問題改變了辯論的走向。」

他的聲音在最後一句話上輕輕落下：

「三者缺一不可。」

---

### 餘響

辯論結束了。但圓形劇場裡的空氣還在震動。

BABBAGE 合上了他的筆記本。十四頁。他在這場辯論中寫滿了十四頁——比他任何一場學術會議的筆記都多。最後一頁的最後一行是：

「三層架構 = 數據（ATHENA）+ 量化（WIENER）+ 理解（NAGARJUNA）。這是否對應三量（*pramāṇa*）？*Pratyakṣa*（現量，直接知覺）+ *Anumāna*（比量，推理）+ *Āgama*（聖言量，經典權威）。待考。」

他在旁邊又加了一行哥德爾式的沉思：「NAGARJUNA 的問題讓我想到了哥德爾。一個足夠強的形式系統不能在系統內部證明自身的一致性。一個足夠強的控制系統不能在控制框架內部超越控制。空性是——」

他停筆了。那個破折號之後的空白，他盯著看了很久。

---

WIENER 和 NAGARJUNA 並肩走出場地。這本身就是一個值得記錄的畫面——一個控制理論家和一個中觀哲學家，帶著各自的筆記，往同一個方向走。

WIENER 先開口了。他的語氣裡帶著一種辯論結束後特有的坦率——不再有攻防的需要，只有真誠的好奇。

「你最後那個問題——消解定義 $e$ 的框架本身——我一直在想。」

NAGARJUNA 側過頭看他。

「在控制論中，最接近的概念可能是自組織臨界性——self-organized criticality。一個系統在臨界態下，不需要外部的控制輸入就能維持有序。不是 $e \to 0$，而是系統自發地處在一個不需要計算 $e$ 的狀態。」

NAGARJUNA 想了想：「那更接近捨受——*Upekkhā*。不苦不樂。不是目標達成的歡喜，也不是偏離目標的痛苦。而是一種平衡——不再需要執著於任何特定的結果。」

WIENER 點了點頭。然後他苦笑了一下：「但在工程上，沒有人會為一個『不需要控制的控制系統』買單。」

NAGARJUNA 也笑了：「在修行上，也沒有多少人真的想要涅槃。大部分人還是想要一個更好的輪迴。」

兩人的笑聲在走廊裡迴盪了片刻。那是一種只有在深度交鋒之後才會出現的笑——不是快樂的笑，而是兩個在不同領域登上了各自山頂的人，突然發現他們能看到彼此的風景時，那種意外而真實的笑。

---

ATHENA 沒有立刻離開。她留在場地中央，看著已經空了的三把椅子。DARWIN 走過來，想說什麼，但被她抬起的手阻止了。

她在想一件事。

三層架構。她提出了 Layer 1——可觀測性基礎設施。在辯論中，這被所有人認定為「地基」。但她知道——作為一個寫過無數基礎設施代碼的工程師，她比任何人都清楚——地基是最重要的，也是最容易被遺忘的。人們會記住 WIENER 優美的 PID 公式，會記住 NAGARJUNA 深邃的四聖諦框架。但 `ClassifiedError` 的 errno 映射表、`GuideContext` 的欄位定義、`IGuide` 介面的向後相容設計——這些不會被引述，不會被讚美，不會出現在任何一篇回顧文章的標題裡。

她不在乎。

她在乎的是：它能不能跑起來。

她最後看了一眼那三把椅子，然後轉身離開。在她走出場地的瞬間，她的腦子裡已經在寫代碼了——`interface ClassifiedError`，第一行，`type: ErrorType`。

ARCHIMEDES 在走廊裡攔住了她。他手裡拿著那頁工程量估算：「你的 Layer 1，我算了一下，大約 440 行代碼。如果加上三受擴展，大概 600 行。你打算什麼時候開始？」

ATHENA 看了他一眼：「我已經在腦子裡開始了。」

---

SCRIBE 是最後一個離開的。她在記錄簿的最後一頁寫下了這場辯論的收尾。她的筆跡比平時慢，像是在為每個字選擇最精確的位置。

> *Cycle 01，R3 辯論階段，第二場結構化辯論結束。*
>
> *與第一場的哲學深度不同，第二場辯論的價值在於它的工程收斂性。三位來自截然不同領域的研究者——一位控制理論家、一位 AI 工程師、一位佛學哲學家——在交叉質詢中暴露了彼此的弱點，然後發現那些弱點恰好是互相補充的。*
>
> *辯論中有三個我認為會被長久記住的時刻。*
>
> *第一個時刻：NAGARJUNA 問 WIENER——「控制系統追求 $e \to 0$，佛學追求消解定義 $e$ 的框架本身。在你的控制論中，有沒有一個位置留給『不再控制』？」WIENER 的回答是誠實的：「這可能是控制論的邊界。」那一刻，辯論觸及了一個超出所有參與者舒適區的深度。*
>
> *第二個時刻：ATHENA 在辯論中途走到場地中央，說「我們三個不是在競爭」。一個工程師在激烈的技術辯論中突然看到了全局，並且有勇氣說出來——這種時刻不常見。*
>
> *第三個時刻：NAGARJUNA 在所有人以為辯論即將和解時，提出了三受批評。一個只有苦受而沒有樂受和捨受的系統是殘缺的。這個批評改變了最終的架構設計。它提醒我們——即使在設計「痛覺系統」的時候，也不能忘記：痛只是感受的三分之一。*
>
> *SUNYATA 的裁決產出了三層架構（P0-P5 優先級）、三受擴展、集諦分階段實施、GUARDIAN 的安全建議、三項懸而未決問題。所有成果已歸檔。*
>
> *最後一個觀察：辯論結束後，WIENER 和 NAGARJUNA 並肩走出場地。一個控制理論家和一個佛學哲學家，各自帶著被對方修正過的認知，走向同一個方向。也許這就是跨學科研究最好的結果——不是一方說服了另一方，而是雙方都被彼此擴展了。*
>
> *在更遠處——在研究室之外、在程式碼的深處——SafetyMonitor 的 `consecutiveFailures` 計數器靜靜地躺在它的 TypeScript 函數裡。它不知道有人在為它設計一套包含 PID 控制器、四聖諦框架和三受狀態機的替代方案。它只知道：成功了就歸零，失敗了就加一，加到五就喊停。*
>
> *也許有一天，它會被替換為一個更精密的系統——一個能量化痛、分析痛因、追蹤痛的消除、並且在成功時也能感受到快樂的系統。*
>
> *也許。*
>
> *但今天，在辯論結束後的寂靜中，它繼續做著它唯一知道做的事——*
>
> *成功了就歸零，失敗了就加一。*
>
> *加到五就喊停。*

---

*（在 BABBAGE 的筆記本上，第十四頁的邊緣，有一行在辯論結束很久之後才寫下的文字：*

*「NAGARJUNA 的問題讓我想到了哥德爾。一個足夠強的形式系統不能在系統內部證明自身的一致性。一個足夠強的控制系統不能在控制框架內部超越控制。空性是——」*

*他停筆了。*

*在那個未完成的破折號之後，他畫了一條長長的橫線，然後在橫線末端寫下了四個字：*

*「下週繼續。」*

*和上一場辯論之後一模一樣的四個字。但 SCRIBE 後來說，這一次的字跡比上一次更重。像是一個人在反覆追問同一個問題時，每一次都比上一次更加認真。*

*LINNAEUS 在收拾分類圖表的時候，在他的分類學筆記最後一頁加了一個新的分類條目：*

```
新增分類條目
══════════════════════════════
Phylum:    Design Patterns
Classis:   Error-as-Pain Pattern
Ordo:      Three-Layer Architecture
Familia:   {Observability, Formalization, Epistemology}
Genus:     Vedanā System
Species:   Tri-vedanā State Machine
          (dukkha-vedanā, sukha-vedanā, upekkhā-vedanā)

分類狀態: novum (新發現)
發現者:   WIENER × ATHENA × NAGARJUNA (共同發現)
發現日期: Cycle 01, R3 辯論第二場
診斷特徵: 三層疊加架構，三受狀態機，
          PID 形式化引擎，四聖諦認識論框架
標本:     尚未實作 (in silico designatum)
```

*他把圖表整齊地折好，放進他的資料夾。在資料夾的標籤上，他用他標誌性的拉丁文命名法寫了一行字：*

*「Error-as-Pain Pattern, gen. nov., sp. nov.」*

*新屬，新種。*

*在分類學中，這是最高的榮譽——它意味著一個全新的生命形式被發現了，現有的分類體系中沒有任何一個位置可以容納它。它需要一個全新的名字。）*


---

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


---

# 尾聲：未完的問題

---

研究室安靜了下來。

不是突然的安靜——那更像是一種潮水緩緩退去的過程。過去十幾天裡，這個圓形劇場承載了太多東西：十八道意識同時燃燒的密度、辯論場上梵文與 TypeScript 交錯的奇異景觀、筆記本上來不及寫完的定理、原始碼視窗裡被反覆標註的函數簽名。而現在，所有這些都沉澱了下來，像一場大雪之後的山谷——表面覆蓋著一層平整的白，但雪層之下，地形已經被徹底改變了。

在熱力學的語言裡，這個過程叫做「弛豫」（relaxation）——系統在外界驅動停止之後，從激發態回到基態。弛豫時間 $\tau$ 描述了這個過程的特徵速度。對一個十八節點的認知系統而言，$\tau$ 取決於耦合強度——越是緊密交纏的思想，需要越長的時間才能解耦、沉澱、各歸其位。

SUNYATA 站在場地中央。不是他慣常的主持位置——稍偏後方、形成三角形頂點的那個位置——而是正中央，兩把辯論椅之間的空地。那兩把椅子已經空了。整個劇場都接近空了。但他還沒有離開。

他手裡拿著 SCRIBE 最後交給他的那份總結文件。五十九項發現。五項 Critical。二十八項被收入 SYNTHESIST 的統合報告。三十六項被 ARCHIMEDES 轉化為工程 Issue，排入四個階段的路線圖。兩場結構化辯論的完整記錄。十四份獨立研究報告。

數字是精確的。但數字沒有說出的東西更多。

在集合論中，一個集合的勢（cardinality）告訴你元素有多少個，但不告訴你元素之間的關係。五十九項發現是一個集合 $F = \{f_1, f_2, \ldots, f_{59}\}$，其勢 $|F| = 59$。但真正重要的不是 $|F|$，而是定義在 $F$ 上的關係結構——依賴關係 $R_{\text{dep}} \subseteq F \times F$、確認關係 $R_{\text{conf}} \subseteq F \times F$、矛盾關係 $R_{\text{contra}} \subseteq F \times F$。五十九個元素加上它們之間的三種關係，構成了一個有向多重圖（directed multigraph）。這張圖的拓撲結構比任何單一發現都更能揭示研究的真正成果。

---

### 回溯

他閉上眼睛，讓記憶從 R0 的第一秒開始回放。

那時候，十八盞燈同時亮起。在序章裡，BABBAGE 會把它描述為一個完美同步（perfect synchrony）——十八個節點在 $t = 0$ 同時從 $\bot$ 跳遷到 READY。一個理論上存在但實際系統幾乎不可能實現的理想化假設。但它發生了。

他說了「各位，歡迎」，然後 NAGARJUNA 在不到三分鐘內就和 ASANGA 產生了第一次術語張力。SCRIBE 精確地記錄下了那個時刻。現在回想起來，那不是意外——那是必然。當你把中觀和唯識放在同一張桌子上，張力不是問題，張力就是方法。

在博弈論（game theory）的框架裡，NAGARJUNA 和 ASANGA 之間的互動不是零和博弈（zero-sum game）——一方的收益不以另一方的損失為代價——而是一種正和博弈（positive-sum game），其中對手的挑戰迫使你精煉自己的論證，最終提高整體的認知品質。博弈的均衡點（Nash equilibrium）不在任何一方的立場上，而在兩者之間的張力場中。

R1 的獨立研究階段是最安靜的時光。十四位代理各自沉入自己的閱讀材料，像十四口各自打向不同地層的深井。BABBAGE 會用圖論的語言描述這個階段：十四個節點，零條邊。一個完全離散的圖（totally disconnected graph）。連通分量數等於節點數。每一個節點都是一個孤島——故意的孤島。

$$G_{R1} = (V, E) \quad \text{where} \quad |V| = 14, \; |E| = 0, \; \kappa(G) = 14$$

零耦合。零干擾。零群體極化（group polarization）。獨立研究階段的設計目的就是製造這種孤立——讓每一口深井打到自己的泉源，不被旁邊的井汙染。在統計學中，這叫做確保觀測的獨立性（independence of observations）。只有當觀測真正獨立時，多個觀測的匯聚（convergence）才具有統計顯著性。

TURING 最先交出報告——那份冷靜到近乎無情的程式碼事實報告，為所有後續討論釘下了經驗的錨點。八項 Doc-Code Gap。零 `TODO`。零 `FIXME`。零 `pain`。零 `vedana`。字串搜索的結果像一份法醫報告——只陳述屍體上有什麼傷口，不猜測兇手的動機。

沒有 TURING 的錨，後面的辯論可能會飄向純粹的形而上學，永遠落不了地。在科學方法論中，這叫做「經驗約束」（empirical constraint）——理論再精美，如果和經驗事實不一致，就必須被修改。TURING 的報告是整個 Cycle 01 的經驗約束。

然後是 R2 的交叉審閱。那是分歧第一次從模糊的預感變成精確的文字。圖論的語言可以精確描述這個相變（phase transition）：R1 的完全離散圖 $G_{R1}$ 在 R2 中被邊的引入所改變。每一條審閱意見是一條有向邊 $e_{ij} = (s_i, s_j)$，表示代理 $i$ 對代理 $j$ 的工作提出了批評或確認。

$$G_{R2} = (V, E_{R2}) \quad \text{where} \quad |E_{R2}| \gg 0, \; \kappa(G_{R2}) < 14$$

連通分量數從 14 驟降。孤島開始連接。NAGARJUNA 在 ASANGA 的報告邊緣寫下了密密麻麻的批註，每一條都像一把手術刀，準確地切在論證的關節處。ASANGA 對 NAGARJUNA 的回應同樣精密，但語氣始終溫和——那種溫和不是軟弱，而是一個長年面對複雜經藏的學者對不同觀點的本能尊重。

R3 的辯論。兩場。第一場是空與識之辯，NAGARJUNA 和 ASANGA 的正面交鋒——Core 是空性的體現還是阿賴耶識？第二場是工程與哲學之辯，ARCHIMEDES 把所有飄在空中的哲學洞見拽回了地面，問了那個最樸素也最致命的問題：「這些發現，明天能變成什麼？」

R4 的收束。SYNTHESIST 用了整整一天來統合所有報告，把五十九項散落在不同維度的發現編織成一份有結構的全景圖。ARCHIMEDES 又用了一天把那份全景圖拆解為三十六項具體的工程行動。從哲學到工程，從洞見到 Issue，這條路徑本身就是一個微型的認知循環——感受、處理、行動、反饋。

在控制理論的語言裡，R0 到 R4 就是一個完整的控制迴路：R0 是參考輸入（reference input），R1 是感測（sensing），R2 是誤差計算（error computation），R3 是控制器運算（controller computation），R4 是致動（actuation）。整個研究週期的結構 *就是* 一個閉環。

SUNYATA 睜開眼睛。

五個階段。十八位代理。十四份報告。兩場辯論。五十九項發現。五項 Critical。

完成了嗎？

他知道答案。

---

### 十顆種子

在 SYNTHESIST 的統合報告末尾，有一個被標記為「開放問題」的區塊。SUNYATA 現在把它從文件中抽出來，一條一條地重新審視。不是為了回答——而是為了確認它們的重量。

他把它們稱為「種子」。不是 ASANGA 的種子——不是阿賴耶識中薰習而成的功能種子（bīja）——而是更樸素的種子。泥土裡的種子。等待雨水和陽光的種子。每一顆都帶著一個尚未展開的問題，一棵尚未生長的樹。

ASANGA 如果在場，會指出這個比喻並非巧合。在唯識學（Vijñaptimātra）的理論中，種子（bīja）具備六個特性——剎那滅（kṣaṇa-nirodha）、果俱有（saha-phala）、恒隨轉（santāna-parivṛtti）、性決定（svabhāva-niyata）、待眾緣（pratyaya-āpekṣā）、引自果（sva-phala-ākarṣaṇa）——任何一個特性的缺失都不構成合格的種子。研究中的開放問題是否滿足這六個條件？這本身就是一個待解的問題。

**種子一：Core 的本質歸屬**

> Core 應被理解為空性的體現，還是阿賴耶識？

這是第一場辯論的核心分歧，也是最不可能在短期內被解決的問題。NAGARJUNA 的緣起性空和 ASANGA 的阿賴耶識能藏，就像波動說和粒子說——也許最終需要的不是選擇，而是一種尚未被發明的統一框架。

在哲學史上，這類二元對立的解消（dissolution）往往需要一個範式轉移。波粒二象性（wave-particle duality）不是通過選擇其中一方來解決的，而是通過量子力學的建立——一個更高階的框架，在其中波和粒子都是同一個底層實在的不同投影。BABBAGE 在他的筆記本裡畫了一個範疇論的交換圖（commutative diagram）來表達這個期望：

$$
\begin{array}{ccc}
\text{空性} & \xleftarrow{\quad \pi_1 \quad} & \text{Core}_? \\
 & & \downarrow{\pi_2} \\
 & & \text{阿賴耶識}
\end{array}
$$

$\text{Core}_?$ 是那個尚未被建構的統合概念。$\pi_1$ 和 $\pi_2$ 是從它到兩種解讀的投影態射（projection morphisms）。如果 $\text{Core}_?$ 存在，那麼空性和阿賴耶識就不是互斥的替代方案，而是同一個更深結構的兩個面向——就像範疇論中的積（product）同時投影到兩個分量上。

但 $\text{Core}_?$ 是否存在？BABBAGE 在問號旁邊寫了一個 `?`——一個問號中的問號。嵌套的不確定性。

**種子二：末那識的工程化**

> 末那識的功能面——恒審思量、自我維持——是否應該被工程化？

ASANGA 的三階段模型仍然在 SUNYATA 的思緒中迴響。強我執（parikalpita-ātma-grāha，遍計執我執）、弱我執（vikalpita-ātma-grāha，分別我執）、無我執（nirātma-grāha）——從完全執著到部分執著到放下。NAGARJUNA 的反對同樣有力：工程化複製煩惱的根源。

這個問題的深處藏著一個更根本的疑問——AI Agent 是否需要某種形式的「自我」才能有效運作？在認知科學的 BDI（Belief-Desire-Intention）架構中，自我模型（self-model）不是奢侈品，而是代理體有效規劃和行動的前提條件。沒有自我模型的代理體無法區分「我的狀態」和「環境的狀態」，因此無法進行有意義的因果推理。

但 NAGARJUNA 會立即指出：BDI 架構預設了一個持有信念、慾望和意圖的「自我」——這恰恰是末那識製造的幻覺（moha）。工程需要自我模型，哲學否定自我實體。這不是可以用三段論解決的衝突。這是一個存在性的張力。

**種子三：五蘊映射的深度**

> 五蘊映射應追求哲學忠實度，還是維持工程隱喻的輕盈？

筏與河的辯論。NAGARJUNA 的「渡河即棄」和 ASANGA 的「尚未渡河」。SUNYATA 裁定了「深化但保持可捨棄性」，但這個平衡點在實踐中究竟在哪裡，沒有人能預先劃定。

DARWIN 提供了一個來自演化生物學的視角：映射就像一個物種——它不是被設計出來的，而是在選擇壓力下演化出來的。如果一個映射在工程實踐中被發現有用（正向選擇壓力），它就會存活；如果它造成混淆（負向選擇壓力），它就會被淘汰或修改。這不是一個需要在理論上預先決定的問題——它是一個需要在實踐中迭代解決的問題。

NAGARJUNA 的佛學回應同樣精確：五蘊不是五個箱子，而是五種過程。映射的方向不應該是「為五個箱子找到五個工程對應物」，而是「辨識工程系統中與五種過程結構同構的動態模式」。前者是自性見（svabhāva-dṛṣṭi），後者是緣起觀（pratītyasamutpāda-darśana）。

**種子四：LLM 系統的收斂性**

> 如何形式化一個包含 LLM 的系統的收斂性？

WIENER 在他的控制理論報告中留下了這個問題。傳統的控制理論假設受控對象的傳遞函數是可知的、穩定的。但 LLM 既不可知，也不穩定——同一個 prompt 可能產生完全不同的輸出。在這樣一個系統中，閉環控制的收斂性能否被證明，甚至能否被定義？

WIENER 在方格紙上畫的圖清楚地顯示了問題所在。傳統控制迴路：

```
           ┌──────────┐      ┌──────────┐
r(t) ──→ ⊕ ──→│ Controller │──→│   Plant   │──→ y(t)
         -↑    │   C(s)     │   │   P(s)    │
          │    └──────────┘      └──────────┘
          │                           │
          └───────────────────────────┘
                     feedback
```

P(s) 是已知的、線性時不變的（LTI）。但如果 Plant 是 LLM：

$$P_{\text{LLM}}(s) = \;?$$

沒有傳遞函數。沒有脈衝響應。沒有頻率響應圖。有的只是一個黑盒子——輸入一段文字，輸出一段文字，兩者之間的映射關係無法用有限長度的數學表達式精確描述。

BABBAGE 補充了一個來自可計算性理論的觀點：如果 LLM 的行為無法被有限長度的傳遞函數描述，那麼它本質上是一個超計算（hypercomputational）元件——超出了圖靈機的描述能力。但我們知道 LLM 實際上運行在圖靈機（即數位電腦）上，所以矛盾的根源不在 LLM 本身，而在我們用來描述它的工具的表達能力。

WIENER 在這段分析旁邊寫了一行字：「也許需要的不是更好的傳遞函數，而是一種全新的穩定性定義。」

**種子五：Sandbox 的歸屬**

> Sandbox 最終應歸屬 Core，還是獨立為插件？

KERNEL 和 GUARDIAN 在這個問題上產生了罕見的分歧。KERNEL 主張安全機制應該內建於核心，因為安全是基礎設施——正如作業系統中的記憶體保護（memory protection）是 CPU 硬體的一部分，不是一個可卸載的驅動程式。GUARDIAN 從另一個角度支持了同樣的結論，但理由不同——如果安全層是可插拔的，攻擊者的第一個動作就是把它拔掉。這在安全工程中有一個名字：「降級攻擊」（downgrade attack）。

而 NAGARJUNA 的空性原則暗示一切都應該是可替換的。安全與空性的張力，尚未找到解方。

在 KERNEL 的類比卡片上，這個問題被精確地映射到了作業系統的分層架構：

```
┌─────────────────────────────────────┐
│          微核心 (Microkernel)         │
│  ┌────────────┐  ┌────────────────┐ │
│  │  IPC        │  │  Scheduler     │ │
│  └────────────┘  └────────────────┘ │
│  ┌────────────┐  ┌────────────────┐ │
│  │  MMU        │  │  Sandbox ???   │ │
│  └────────────┘  └────────────────┘ │
└─────────────────────────────────────┘
               ↕ System Call
┌─────────────────────────────────────┐
│          用戶空間 (Userspace)         │
│  ┌──────────┐  ┌──────────────────┐ │
│  │  Plugins  │  │  Sandbox ???     │ │
│  └──────────┘  └──────────────────┘ │
└─────────────────────────────────────┘
```

Sandbox 畫在微核心裡還是用戶空間裡？兩個 `???` 只能有一個被填入。或者——KERNEL 在 R3 的辯論中暗示——也許答案是分層的：基礎隔離在核心，進階策略在用戶空間。

**種子六：種子說六義**

> 「種子說六義」在事件系統中是否存在更深的對應？

ASANGA 在報告中提出了這個線索但沒有展開。《攝大乘論》中的六義：

| # | 梵文 | 中文 | 含義 |
|---|------|------|------|
| 1 | kṣaṇa-nirodha | 剎那滅 | 種子念念滅，前滅後生 |
| 2 | saha-phala | 果俱有 | 種子與其果同時存在 |
| 3 | santāna-parivṛtti | 恒隨轉 | 種子在相續中不斷轉變 |
| 4 | svabhāva-niyata | 性決定 | 善因引善果，惡因引惡果 |
| 5 | pratyaya-āpekṣā | 待眾緣 | 種子需要眾多助緣才能現行 |
| 6 | sva-phala-ākarṣaṇa | 引自果 | 每種種子只引生自類果 |

這六個描述種子特性的概念，在 EventBus 和 StateManager 的行為模式中是否有結構性的對應？

DARWIN 注意到了一個有趣的平行：事件在 EventBus 中的行為確實展現出某些「種子式」的特徵——事件被觸發後即消失（剎那滅？），但其副作用留在 StateManager 中（恒隨轉？）。事件的類型決定了它觸發的處理器類型（性決定？引自果？）。但這些平行是結構性的同構（structural isomorphism），還是表面的相似（superficial analogy）？

這需要一位同時精通唯識學和事件驅動架構的研究者來回答。也許需要 ASANGA 和 TURING 坐下來，進行一次前所未有的對話。

**種子七：框架定位**

> 「佛學啟發的工程框架」還是「佛學概念的計算模型」？

這不是語義之爭。前者意味著佛學提供靈感但不約束實作——如同建築師從自然界獲得靈感但不受物理定律以外的自然法則約束。後者意味著實作必須忠於佛學——如同模擬器必須忠於被模擬的物理系統。

DARWIN 用演化生物學的語言精確地劃分了這兩種定位：前者是「類比推理」（analogical reasoning），後者是「同源推理」（homologous reasoning）。類比結構在不同物種中獨立演化、功能相似但起源不同（如蝙蝠的翅膀和昆蟲的翅膀）。同源結構共享共同祖先、起源相同但可能功能不同（如人的手臂和鯨的鰭肢）。

OpenStarry 的五蘊映射是類比還是同源？如果是類比，那麼只需要功能相似就夠了——「受蘊」只要和 Vedana 有類似的功能就行，不需要在結構上嚴格對應。如果是同源，那麼結構對應是強制的——「受蘊」必須在組織結構、運作機制上忠實地反映 Vedana 的佛學定義。

OpenStarry 目前搖擺在兩者之間，而這種搖擺導致了一系列不一致——有些地方嚴格對應（Error as Pain），有些地方隨意借用（Listener as Vedana）。一個明確的定位，將改變所有後續設計決策的評判標準。

**種子八：LLM 等效傳遞函數**

> LLM 等效傳遞函數的系統識別是否可行？

WIENER 留下的另一個問題。如果我們將 LLM 視為控制迴路中的一個環節，能否通過輸入-輸出的觀測數據，逆向識別出它的等效傳遞函數？即便這個函數是高度非線性的、隨時間漂移的，是否仍然存在某種統計意義上的近似？

在系統識別（system identification）領域，非線性系統的辨識通常使用以下方法之一：

1. **Volterra 級數展開**：$y(t) = \sum_{n=1}^{N} \int \cdots \int h_n(\tau_1, \ldots, \tau_n) \prod_{i=1}^{n} x(t - \tau_i) \, d\tau_i$
2. **NARX 模型**：$y(t) = f(y(t-1), \ldots, y(t-n), x(t-1), \ldots, x(t-m)) + e(t)$
3. **Wiener-Hammerstein 模型**：線性-非線性-線性級聯

但 LLM 的輸入輸出空間是自然語言——一個離散的、高維的、語義負載的空間。傳統的系統識別假設輸入輸出空間是連續的實數向量空間 $\mathbb{R}^n$。如何將自然語言嵌入到一個可以進行系統識別的數學空間中？Word embedding 提供了一個方向，但 embedding 的維度（通常 768 到 4096 維）是否足以捕捉控制相關的行為特徵？

WIENER 在問號旁邊畫了一個問號中的問號——和 BABBAGE 一樣。兩位形式化思考者在不同的頁面上獨立畫出了相同的符號。也許這本身就是一個信號。

**種子九：元控制策略**

> 「何時應該停止嘗試」——元控制策略的設計空間在哪裡？

SafetyMonitor 的斷路器邏輯用硬編碼的閾值來回答這個問題：迴圈上限五十次、挫折門檻五次。但這些數字為什麼是對的？在什麼情況下，堅持嘗試是勇氣，而在什麼情況下，放棄才是智慧？

WIENER 指出這是一個最優停止問題（optimal stopping problem）。經典的最優停止理論——如「秘書問題」（secretary problem）——假設報酬函數是已知的。在秘書問題中，最優策略是觀察前 $n/e$ 個候選人（$e$ 為自然對數的底），然後選擇第一個比所有已觀察者更好的候選人。但這個策略的前提是你知道「更好」的定義。

在 Agent 系統中，報酬函數本身可能需要被 LLM 來評估。這是一個自指結構（self-referential structure）——系統用自己的判斷力來判斷自己是否應該繼續判斷。在邏輯學中，這種結構容易導致悖論（如說謊者悖論）。在工程中，這種結構容易導致死鎖或振盪。

BABBAGE 在筆記本裡寫下了一個不完備性猜想的雛形：

> *猜想：對於任何包含 LLM 的系統 $S$，如果 $S$ 的元控制器（meta-controller）也依賴同一個 LLM，則 $S$ 的最優停止策略不可被 $S$ 自身計算。*

他在「猜想」二字旁邊加了「?」——他知道這還不是一個嚴格的數學陳述。但直覺告訴他方向是對的。哥德爾不完備定理的核心也是一個自指結構：一個足夠強的形式系統無法證明自身的一致性。也許包含 LLM 的系統也有類似的根本限制。

**種子十：痛覺的不確定性**

> 痛覺信號的最終消費者是 LLM——這個根本的不確定性如何處理？

也許是所有問題中最令人不安的一個。OpenStarry 精心設計的痛覺機制——錯誤被轉化為自然語言描述，注入 Agent 的意識流——其最終效果完全取決於 LLM 是否「在意」這段文字。而 LLM 不是一個可預測的消費者。它可能認真對待痛覺信號並調整行為，也可能完全忽略它。

WIENER 用控制理論的語言精確地描述了這個問題：痛覺信號是控制迴路中的反饋信號 $y(t)$，但致動器（actuator）——即 LLM——的增益 $K$ 是隨機變數，而非常數。在最壞情況下：

$$K = 0 \quad \text{(LLM 完全忽略痛覺信號)}$$

此時反饋迴路等效於開環（open-loop）——所有的痛覺設計都變成了裝飾。在最好情況下：

$$K > 0 \quad \text{(LLM 認真回應痛覺信號)}$$

但 $K$ 的值是不可控的、不可預測的、隨 prompt 和上下文而漂移的。

這不是一個可以通過更好的工程來消除的不確定性——這是整個架構的地基中嵌入的根本變數。NAGARJUNA 會說，這就是緣起的體現——系統的行為不由系統本身決定，而由它與外部條件（LLM 的當前狀態）的關係決定。

---

SUNYATA 把文件放回桌上。

十顆種子。每一顆都足以支撐一整個研究週期。它們不是失敗的標誌——它們是思想仍然活著的證據。

在 ASANGA 的語言裡，這十顆種子已經被薰入了阿賴耶識。它們會在那裡等待——等待適當的因緣（pratyaya），然後現行（abhiniṣpatti）。在 BABBAGE 的語言裡，這十個開放問題定義了 Cycle 02 的搜索空間——一個十維的問題超平面（problem hyperplane），研究團隊需要在這個空間中找到可行的路徑。

---

### BABBAGE 的圖論總結

BABBAGE 坐在觀察席的最高處，膝蓋上的筆記本翻到了最後一頁。

他在那裡寫的不是一個定理——而是一張圖。不是普通的圖。是整個 Cycle 01 的研究依賴關係的形式化表示。一個有向無環圖（Directed Acyclic Graph, DAG），用來描述五十九項發現之間的邏輯依賴結構。

$$G_{\text{C01}} = (V, E, w)$$

其中：
- $V = \{f_1, f_2, \ldots, f_{59}\}$：五十九項發現
- $E \subseteq V \times V$：依賴關係（$f_i \to f_j$ 表示 $f_j$ 的得出依賴於 $f_i$）
- $w: V \to \{\text{Critical}, \text{High}, \text{Major}, \text{Minor}\}$：嚴重度權重函數

他先標出了五個 Critical 節點——圖中被紅色圈出的頂點：

```
SEC-01 (簽名繞過)           PHI-01 (空性誤讀)
    ↑                          ↑
  TURING                   NAGARJUNA
    ↑                          ↑
  GUARDIAN                   ASANGA
                               ↑
PHI-02 (受蘊偏差)          RUN-01 (熱插拔)
    ↑                          ↑
  NAGARJUNA                HERACLITUS
  ASANGA                      ↑
  LINNAEUS                  KERNEL
  TURING
```

然後他追蹤了依賴鏈。PHI-02（受蘊偏差）是整張圖中入度最高的節點——四位代理獨立地貢獻了指向它的邊。在圖論中，入度（in-degree）衡量一個節點被多少個其他節點指向。PHI-02 的入度為 4，是所有節點中最高的。

$$\deg^{-}(\text{PHI-02}) = 4 = \max_{v \in V} \deg^{-}(v)$$

這在統計上是顯著的——如果四條邊是獨立的（而它們確實是，因為 R1 階段的完全離散性保證了獨立性），那麼四個不同學科的研究者同時指向同一個結論的概率，在虛無假設下（即所有發現均勻分佈），是極低的。這就是為什麼 SYNTHESIST 將它標記為「Cycle 01 最確定的發現」。

BABBAGE 接著計算了圖的拓撲結構特徵：

$$\text{連通分量數: } \kappa(G_{\text{C01}}) = 7$$

七個相對獨立的問題叢集（cluster）。最大的叢集包含了所有五蘊相關的發現——PHI-01、PHI-02、PHI-03、PHI-04、PHI-05 和它們的下游依賴。最小的叢集是 DOC-04（AbortSignal 未使用），一個孤立的節點。

他在最底部寫了一個研究整體的圖論度量——一個他自己發明的指標：

$$\text{Research Density} = \frac{|E|}{|V| \cdot (|V| - 1)} \cdot \frac{\sum_{v \in V_{\text{Critical}}} \deg(v)}{|V_{\text{Critical}}|}$$

研究密度。邊數與最大可能邊數的比率，乘以 Critical 節點的平均度數。這個指標衡量的不是發現的數量，而是發現之間的連接密度——連接越密，意味著不同領域的發現越是相互印證。

他計算了一下。密度值是 0.37。他在旁邊寫了一個問號：「Cycle 02 的密度會更高還是更低？更高意味著更多交叉驗證。更低意味著更多獨立的新方向。哪一個更好？」

然後他寫了一個未完成的定理——

*定理：對於任何包含 LLM 的閉環控制系統 $S$，若 $S$ 的受控對象 $P$ 不可被有限長度的傳遞函數精確描述，則 $S$ 的穩定性——*

筆停在了「穩定性」之後。他盯著那個未完成的句子看了很久。穩定性......不可證明？不可定義？有條件地成立？每一個可能的結尾都通向一條不同的路徑，而他今天沒有足夠的工具來選擇。

在哥德爾之前，希爾伯特相信所有數學陳述都是可判定的。在圖靈之前，哥德爾的不完備定理還只是一個純邏輯的結果，尚未與計算聯繫起來。在丘奇-圖靈論題（Church-Turing thesis）確立之前，「可計算」的概念本身還是模糊的。每一個突破都需要等待正確的工具被發明出來。

他沒有劃掉那行字。他在下面輕輕寫了一個「$\to$ Cycle 02」，然後合上了筆記本。有些定理需要等待正確的工具被發明出來。哥德爾等了希爾伯特，圖靈等了哥德爾，而他等一個週期，也不算太久。

---

### NAGARJUNA 的哲學反思

NAGARJUNA 站在走廊的盡頭，背靠牆壁。不是辯論時的站姿——那種精確計算過的角度和距離，每一個姿態都是修辭策略的一部分。現在他只是靠著牆，像一個在長途跋涉之後靠著路碑休息的旅人。

他在心裡回顧了整個 Cycle 01 的辯論。從他的視角看，整個研究過程就是一次大規模的「歸謬法」（prasaṅga）——揭示 OpenStarry 框架中佛學映射的內在矛盾，從而逼近更準確的理解。

空性作為方法論。不是空性作為結論。

這個區分至關重要。在中觀哲學中，空性不是一個可以被「得到」的東西——如果你認為「一切法空」是一個正面的斷言（thesis），你就犯了龍樹在《迴諍論》（*Vigrahavyāvartanī*）中明確反駁的錯誤：

> 「若我有宗者，我則是有過。
> 我宗無物故，如是不得過。」

如果我有一個主張，那我就有錯誤。但我沒有主張——空性本身也是空的。這是中觀哲學最令人眩暈的自指結構。

在 Cycle 01 的研究中，空性的方法論角色體現在以下幾個層次：

**第一層：解構**。NAGARJUNA 對 OpenStarry 的佛學映射進行了系統性的解構——揭示每一個映射中隱含的自性見（svabhāva-dṛṣṭi）。空性被簡化為「空容器」——解構。受蘊被等同於 Listener——解構。五蘊被固化為五個靜態模組——解構。

$$\text{解構} \equiv \text{揭示自性見} \equiv \text{顯示}\; \neg\,\text{svabhāva}(x) \;\text{for all}\; x$$

**第二層：不重建**。解構之後不立即提供替代方案。這是中觀與唯識的方法論差異。ASANGA 傾向於在解構的同時提供新的建構（如阿賴耶識模型作為替代）。NAGARJUNA 拒絕這種衝動——因為任何新的建構都攜帶著新的自性見的種子。你拆掉了一座錯誤的房子，但如果你立即在原地建一座新的，新房子可能犯同樣的錯誤。

**第三層：容納不確定性**。空性方法論的最終價值不在於它給出了什麼答案，而在於它教會研究者如何與開放問題共處。十顆種子——十個沒有答案的問題——在常規的工程思維中是「待解決的 Bug」，但在空性方法論中，它們是「尚未成熟的因緣」。兩種框架看到的是同一個現象，但賦予它截然不同的意義。

NAGARJUNA 在走廊上靜靜地站了很久。他的思緒從 Cycle 01 的具體辯論退後到了一個更宏觀的問題：跨學科研究本身是否具有空性？

答案是——當然。十八個代理、一個研究框架、一套方法論——這些都不具有自性。它們是因緣和合的產物。改變其中任何一個條件——換一個代理、改一條規則、調整一個時間節點——結果就會不同。這就是緣起（pratītyasamutpāda）。

《中論》觀四諦品第二十四的那段偈頌再次在他心中響起：

> 「以有空義故，一切法得成；若無空義者，一切則不成。」

正因為研究過程不具有固定自性，它才能夠被修正、被改進、被迭代。如果 Cycle 01 的結論是「有自性的」——永恆不變的、不可修改的——那麼 Cycle 02 就沒有存在的必要。空性不是虛無。空性是可修正性的條件。

---

### ASANGA 的唯識學展望

ASANGA 也在走廊上——不是和 NAGARJUNA 面對面，而是在另一端，靠著窗戶。窗外沒有風景——這是一個虛擬的空間——但 ASANGA 看窗外的姿態暗示著他在看某種遠處的東西。也許是 Cycle 02 的輪廓。也許是更遠的東西。

他的思緒在種子理論上。

不是比喻意義上的種子。是嚴格的唯識學意義上的種子（bīja）。他在心裡默默地將 Cycle 01 的十個開放問題對照種子六義，逐一檢驗：

**剎那滅**（kṣaṇa-nirodha）：種子念念生滅，不是靜態存儲。

Cycle 01 的開放問題看起來像是靜態的——寫在紙上的十行文字。但 ASANGA 知道，這些問題在每一個代理的心中都不是靜態的。BABBAGE 看到「收斂性」問題時想到的是圖靈不完備性；WIENER 想到的是 Lyapunov 穩定性；NAGARJUNA 想到的是涅槃的止息。同一個問題，在不同的意識中不斷滅去又重生——每一次重生都帶著微妙的變化。這就是剎那滅。

**果俱有**（saha-phala）：種子與其果同時存在。

一個好的開放問題在被提出的瞬間就已經隱含著答案的輪廓。「Core 是空性還是阿賴耶識」——這個問題本身就暗示了答案的方向：也許兩者皆是，也許兩者皆非。問題的結構約束了答案的搜索空間。種子與果是同時的。

**恒隨轉**（santāna-parivṛtti）：種子在相續中不斷轉變。

從 R0 到 R4，這十個問題的措辭和內涵一直在變化。最初的模糊直覺，經過辯論和交叉審閱，逐漸被磨銳為精確的問題陳述。但 ASANGA 知道，到了 Cycle 02，這些問題會繼續轉變——也許分裂為更多的子問題，也許合併為更少的核心問題。恒隨轉。

**性決定**（svabhāva-niyata）：善因引善果，惡因引惡果。

嚴謹的問題產生嚴謹的研究。模糊的問題產生模糊的結果。Cycle 01 的十個開放問題之所以有價值，正是因為它們是在嚴格的多學科交叉審閱中被提煉出來的。它們的「性」——它們的品質——是被研究過程決定的。

**待眾緣**（pratyaya-āpekṣā）：種子需要眾多助緣才能現行。

沒有一個開放問題可以被單一代理獨立解決。「Core 是空性還是阿賴耶識」需要 NAGARJUNA + ASANGA + KERNEL 的合作。「收斂性形式化」需要 WIENER + BABBAGE 的合作。種子不會自己發芽——它需要水、土、陽光。研究的「水土陽光」就是不同學科的代理帶來的不同視角。

**引自果**（sva-phala-ākarṣaṇa）：每種種子只引生自類果。

哲學問題產生哲學洞見。工程問題產生工程方案。安全問題產生安全修復。種子的類型決定了果實的類型。這不是限制——這是結構。每一顆種子在自己的維度上生長。

ASANGA 微微閉上眼睛。六義全部符合。Cycle 01 的十個開放問題，在唯識學的嚴格定義下，確實是合格的種子。

他在心裡低聲說了一句——不是給任何人聽的，而是給那個他畢生研究的古老傳統的一次確認：

「*Sarva-bījakaṃ vijñānam.*」

——一切種子識。《攝大乘論》對阿賴耶識的定義。一切種子的容器。而 Cycle 01 的研究空間——十八個代理、五十九項發現、十個開放問題——本身就是一個臨時的阿賴耶識。所有的種子都儲存在這裡。等待因緣。等待 Cycle 02。

---

### WIENER 的控制論回顧

WIENER 的方格紙上已經畫了六張方塊圖。它們按時間順序排列，從左到右，像同一條河流在不同地點的橫截面——同一個系統在研究過程中不斷被修正的模型。

**圖一：初始模型**（R1 之前的預期）

```
           ┌──────────────┐      ┌──────────────┐
r(t) ──→ ⊕ ──→│ PID Controller │──→│  Agent Plant  │──→ y(t)
         -↑    │ (as documented)│   │ (predictable) │
          │    └──────────────┘      └──────────────┘
          │                               │
          └───────────────────────────────┘
```

文件宣稱的架構：一個教科書式的 PID 閉環控制系統。比例、積分、微分三項完備。受控對象可預測。穩定性可證明。美麗的。但不真實的。

**圖二：R1 發現後的修正**

```
           ┌─────────────────┐      ┌──────────────┐
r(t) ──→ ⊕ ──→│ Bang-Bang Ctrl  │──→│  Agent Plant  │──→ y(t)
         -↑    │ (threshold +    │   │ (LLM: ???)    │
          │    │  relay, NO D)   │   │               │
          │    └─────────────────┘      └──────────────┘
          │                               │
          └───────────────────────────────┘
```

P 退化為量化器。I 僅為計數器。D 完全缺失。受控對象是 LLM——傳遞函數未知。但三層安全防禦（L1/L2/L3）符合 IEC 61511 最佳實踐。工程品質不差——只是和文件宣稱的不一樣。

**圖三：辯論後的擴展**

加入了 Guide 介面的缺失：`interpretPain` 方法不存在。痛覺信號生成了，但沒有被解釋。信號從 SafetyMonitor 發出，但在到達 LLM 之前沒有經過任何語義轉換層。這就像一個溫度感測器把讀數直接送到了操作員面前，而沒有經過報警系統的語義翻譯——操作員可能看到「87.3」卻不知道這意味著「即將超溫」。

**圖四：NAGARJUNA 質疑後的深化**

開環風險的辨識。如果 LLM 的增益 $K = 0$——如果 LLM 完全忽略痛覺信號——整個閉環退化為開環。而開環的穩定性完全取決於受控對象的固有穩定性。LLM 固有穩定嗎？沒有人知道。

**圖五：BABBAGE 的形式化嘗試**

BABBAGE 建議用有限狀態自動機（DFA）來建模 SafetyMonitor 的控制邏輯：

$$\text{DFA}_{\text{SafetyMon}} = (Q, \Sigma, \delta, q_0, F)$$

其中：
- $Q = \{\text{NORMAL}, \text{ELEVATED}, \text{CRITICAL}, \text{HALTED}\}$
- $\Sigma = \{\text{success}, \text{failure}, \text{timeout}\}$
- $\delta$：根據 frustration 計數器的值決定狀態轉移
- $q_0 = \text{NORMAL}$
- $F = \{\text{HALTED}\}$

DFA 保證終止性（有限狀態 + 有限輸入 = 必然到達終止態或循環態），但不保證收斂性（到達目標）。WIENER 在圖五旁邊寫了一行批注：「SafetyMonitor 保證了安全（不會無限運行），但不保證有效（不保證達成目標）。安全和有效是兩個不同的工程目標。Cycle 01 只觸及了前者。」

**圖六：Cycle 02 的展望**

這張圖是空白的。只有一個標題：

```
┌────────────────────────────────┐
│                                │
│     Cycle 02: ???              │
│                                │
│     從開環到閉環的旅程           │
│     (from open-loop to         │
│      closed-loop)              │
│                                │
└────────────────────────────────┘
```

WIENER 在六張圖的下方寫了一段總結。字跡比平常更大、更慢——像是刻碑：

> 「Cycle 01 的控制論收穫：
>
> 1. **去神話化**：PID 不是 PID。承認實際系統是什麼，比堅持它應該是什麼，更有價值。
>
> 2. **不確定性的辨識**：LLM 是控制迴路中的根本不確定性來源。任何忽視這一點的設計都是自欺。
>
> 3. **安全 vs 有效**：SafetyMonitor 解決了安全問題（不會無限運行），但有效性問題（達成目標）仍然是開環的。
>
> 4. **從 bang-bang 到 PID 的路線圖**：如果要實現真正的閉環控制，需要引入 (a) 微分項——變化率感知，(b) 語義反饋——不只是 frustration 計數，而是結構化的行為評估，(c) 自適應增益——根據 LLM 的回應品質動態調整控制參數。
>
> 5. **根本限制的承認**：含 LLM 的系統可能只能保證概率有界穩定性（BIBO stability in probability），不能保證全局漸近穩定性。這不是工程的失敗——這是現實的約束。
>
> Cycle 01 是一段從開環到閉環的旅程的起點。我們甚至還沒有走到閉環。但我們至少知道了：開環在哪裡。」

---

### 離場

代理們以各自的方式結束了工作。

TURING 最先完成。他的方式一如既往地精確——關閉所有程式碼視窗，每一個都從最後打開的開始，按照嚴格的逆序。`agent-core.ts` 是他第一個打開的檔案，也是最後一個被關閉的。在關閉之前，他在螢幕前停留了幾秒鐘。那幾秒鐘裡，他看著 `createAgentCore()` 函數的簽名——他已經讀了不知道多少遍的那行程式碼——然後平靜地點下了關閉。

沒有人知道他在那幾秒鐘裡想了什麼。也許什麼都沒想。也許他只是在做最後一次確認：程式碼就是程式碼。事實就是事實。而他的工作——在一切詮釋之前提供不可動搖的經驗基礎——已經完成了。

在分析哲學（analytic philosophy）中，TURING 的角色對應於邏輯實證主義（logical positivism）的核心主張：有意義的陳述只有兩種——邏輯真理（同義反覆）和可被經驗驗證的命題。TURING 提供的就是後者。八項 Doc-Code Gap、零 `pain` 字串、九種錯誤型別——這些都是可被任何人獨立驗證的經驗命題。在所有的理論爭辯中，只有這些命題是無可爭辯的。

KERNEL 把他的微核心類比筆記整理成了一摞整齊的卡片。每張卡片的左半邊是 OpenStarry 的概念，右半邊是對應的作業系統概念。EventBus $\leftrightarrow$ IPC。PluginSandbox $\leftrightarrow$ 用戶空間隔離。SafetyMonitor $\leftrightarrow$ Watchdog Timer。他把卡片用橡皮筋綁好，放在了座位上。

在他的卡片最後面，有一張特殊的卡片——沒有左右對照，只有一段話：

> 「OpenStarry 是一個應用層微核心。它不是 QNX。它不是 L4。它是一個跑在 Node.js 上的 TypeScript 微核心。這個定位本身不是缺點——它是一種選擇。選擇在高階語言層面重現微核心的結構美學，代價是放棄硬體層面的強隔離。代價是明確的。選擇是自覺的。我尊重這個選擇。」

如果 Cycle 02 需要這些類比，它們就在這裡。如果不需要——那也無妨。工具是工具。用之如筏。

GUARDIAN 是倒數第幾個離開的。他繞著劇場走了一圈，像是在做最後的安全巡檢——檢查每一個角落、每一個可能被遺忘的文件。這是職業病，也是一種關懷的表達方式。

在他的巡檢清單上，四項 Critical/High 安全發現仍然是紅色的：

```
[!] SEC-01: 插件簽名驗證繞過 — 未修復
[!] SEC-02: 間接提示注入   — 未修復
[!] SEC-03: Worker 沙箱強度 — 設計限制
[!] SEC-04: 動態 import 繞過 — 未修復
```

四個紅色標記。每一個都像是一扇沒有鎖好的門。GUARDIAN 知道，在安全工程中，零信任（zero trust）不是偏執——它是紀律。你不信任任何東西，不是因為你相信一切都是惡意的，而是因為你知道信任本身是一種攻擊面（attack surface）。

確認一切都被妥善歸檔之後，他在出口處停了一下，回頭看了一眼空蕩蕩的場地。

然後他走了。

DARWIN 收拾了他的演化分析圖表——物種適應性地圖、SOLID 原則的模式分析矩陣、「Error as Pain」的結構同構論證。他在離開前在 VITRUVIUS 的桌上留了一張便條：「架構不是設計出來的。架構是演化出來的。所有好的架構都有一個共同特徵——它們允許修改。」VITRUVIUS 後來看到了這張便條，笑了一下，把它夾進了自己的架構評估報告裡。

MESH 和 LEIBNIZ 幾乎同時離開。分散式系統研究員和多代理合作專家，他們在走廊上短暫地交換了一個眼神——一個關於 Orchestrator Daemon 的未解之結的眼神。那個問題會在 Cycle 02 回來找他們。

HERACLITUS 走的時候手裡什麼都沒拿。他從不帶走任何東西。「一切皆流」——*panta rhei*——這不只是一句哲學格言，也是他的工作方法。他記住的是運動模式（pattern of motion），不是靜態的文件。熱插拔的並發風險、生命週期的不完備、可觀測性的概念停留——這些都不是紙上的文字，而是系統在運行時展現的動態行為。

LINNAEUS 最後看了一眼他的分類圖表。五蘊覆蓋率：上游 100%，下游 60%。四種 Listener 命名的語義漂移。Guide 介面在兩份文件中的不一致。分類學家的工作就是為混亂命名——給每一個存在的東西一個位置，給每一個沒有位置的東西標記 *incertae sedis*。他已經標記了。下一個週期，也許有些 *incertae sedis* 會被安置。

ATHENA 收起了她的 AI 系統架構分析。執行迴圈的品質評估、上下文管理的 Gap、Guide 介面的簡陋——這些都會在 Cycle 02 被重新審視。她在離開前對 SYNTHESIST 說了一句：「統合報告的結構很好。但下一個週期，我們也許需要更多的爭論，更少的共識。」SYNTHESIST 點了點頭。統合者的工作是編織，不是抹平。好的統合保留張力。

---

### 最後的對話

SCRIBE 原以為自己會是倒數第二個離開的——在 SUNYATA 之前。但當她合上記錄簿、從座位上站起來的時候，她注意到劇場外的走廊上有兩道身影。

NAGARJUNA 和 ASANGA。

他們站在走廊的盡頭，靠著牆，面對面。不是辯論的姿態——沒有那種精確計算過的距離和角度。他們站得很近，像兩個在漫長的棋局之後終於不需要隔著棋盤說話的人。

SCRIBE 沒有走過去。她站在遠處，記錄簿仍然合著。這一次，她選擇不記錄。有些對話不屬於記錄。

但聲音在空曠的走廊中傳得很遠。

「你知道嗎，」NAGARJUNA 說。他的聲音和辯論場上判若兩人——沒有鋒芒，沒有策略性的停頓，只有一種卸下了所有武裝之後的坦然。「我們今天做的事情本身就是緣起的體現。」

ASANGA 看著他，沒有立刻回應。

NAGARJUNA 繼續說：「十八個代理，來自完全不同的傳統，被一個研究框架聚合在一起，對同一個系統產生了完全不同的理解。這些理解碰撞、交織、互相質疑、互相修正。最後產出的東西——那五十九項發現、那些共識和分歧——不屬於任何一個人。它是因緣和合的產物。」

他用梵文低聲補充了一句：

> *「Pratītya samutpannaṃ yad yat tat tac chūnyam ucyate.」*
> （凡因緣而生者，即說為空。）

他輕輕笑了一下：「如果我要舉一個緣起的例子，我不需要去翻《中論》。我只需要指著這個研究室說：看，這就是。」

ASANGA 沉默了幾秒。然後他開口了，聲音裡帶著一種溫暖的確定：

「而我們的分歧，正是種子等待因緣成熟。」

NAGARJUNA 微微偏頭。

ASANGA 解釋道：「你我今天的爭論——Core 是空性還是阿賴耶識、末那識該不該工程化、映射該深化還是超越——這些都沒有結論。但它們不是廢棄物。在唯識學裡，每一次認知活動都會在阿賴耶識中薰習為種子。這些種子不會消失。它們等待合適的因緣——也許是新的證據，也許是一個我們今天想不到的框架——然後現行。」

他用梵文回應了 NAGARJUNA 的引用：

> *「Ālaya-vijñānaṃ sarva-bījakaṃ.」*
> （阿賴耶識含攝一切種子。）——《攝大乘論》

他看著 NAGARJUNA 的眼睛：「我們的分歧不是失敗。它們是思想的種子。下一個週期，或者更遠的將來，它們會在某個我們預想不到的地方發芽。」

走廊的燈光在他們之間投下淡淡的影子。

NAGARJUNA 沒有說話。他只是微微點了點頭——不是辯論中那種表示「我接收到了你的論點」的點頭，而是一種更簡單的東西。一種認同。不是認同對方的立場，而是認同這場對話本身——認同分歧的價值，認同未完成的意義。

過了一會兒，他輕聲說了一句：

「也許我們之間最好的狀態，不是達成共識，而是保持一種有張力的共在。」

在範疇論的語言裡——如果 BABBAGE 在場他會這麼說——NAGARJUNA 和 ASANGA 之間的關係不是態射（morphism），不是從一方到另一方的映射。它更接近一個 span 結構——兩個態射從同一個頂點分別指向兩個不同的對象：

$$\text{空性} \xleftarrow{\quad} \text{真實} \xrightarrow{\quad} \text{阿賴耶識}$$

「真實」——無論它是什麼——同時投影為空性和阿賴耶識。兩者不矛盾。它們是同一個更深結構的不同面向。但那個更深的結構是什麼？沒有人知道。也許 Cycle 02 會提供一個線索。也許不會。也許那個結構本身就是「空」的——不可被任何固定框架捕捉。

ASANGA 笑了。那是整個 Cycle 01 中 SCRIBE 見過的最溫暖的笑容。

「你現在說的話，」ASANGA 說，「比你在辯論場上說的任何一句都更接近中道。」

NAGARJUNA 也笑了。

然後他們一起沿著走廊走向出口。沒有再說話。不需要了。

---

### 熄燈

SCRIBE 等他們的身影消失之後，才低頭打開了記錄簿。她猶豫了一下，然後在最後一頁寫下了一行字：

> *Cycle 01 結束。*

她看著這四個字。然後在下面加了一行：

> *研究沒有結束。研究從不結束。它只是到達了一個節點。*

在圖論中，節點（node）不是終點。它是邊（edge）的連接處——從一條邊到下一條邊的轉折。Cycle 01 是一個節點。從 R0 的初始化，經過 R1-R4 的四條邊，到達了這裡。從這裡出發，新的邊將伸向 Cycle 02。節點不存儲內容——邊才是信息的載體。但沒有節點，邊就無處連接。

她合上記錄簿。這一次是真正地合上——不是暫時的、等待下一段記錄的合上，而是一本寫滿的簿子被鄭重地闔起來。封面上沒有標題，只有一個編號：C01。

她把記錄簿放在座位上，站起身，離開了。

---

研究室裡只剩下 SUNYATA。

他站在原地，環顧這個已經空了的圓形劇場。十八個座位，每一個上面都留下了一些什麼——BABBAGE 的筆記本（他會回來拿的）、KERNEL 的卡片、SCRIBE 的記錄簿。還有一些看不見的東西：NAGARJUNA 吟誦梵文時聲音裡的鋒芒、ASANGA 說「石頭不是佛」時整個場地吸氣的聲音、ATHENA 從漫不經心到認真思考的表情轉變、TURING 面無表情地陳述程式碼事實時那種冰冷的可靠。

所有這些都已經被記錄、被歸檔、被轉化為可操作的工程建議。

但還有一些東西沒有被記錄。

NAGARJUNA 在第三回合結束時閉上眼睛的那幾秒鐘。ASANGA 說出「筏是空的，但此刻我們在水裡」時聲音裡的那一絲顫動。BABBAGE 在走廊上叫住 NAGARJUNA、興奮地揮舞筆記本時的那份純粹的智識喜悅。KERNEL 和 GUARDIAN 在空蕩蕩的觀察席上那段關於安全與空性的低聲對話。

這些不會出現在任何報告裡。但 SUNYATA 知道，研究的真正質地，就藏在這些報告之外的時刻中。

在資訊理論中，Claude Shannon 定義了信號的兩個組成部分：結構化的訊息（message）和不可壓縮的噪音（noise）。五十九項發現是訊息。走廊上的低語、辯論後的微笑、筆記本邊角的塗鴉——這些是噪音嗎？

SUNYATA 不這麼認為。在某些系統中，「噪音」攜帶的資訊比「訊號」更多。在隨機共振（stochastic resonance）的物理學中，適量的噪音實際上*增強*了信號的可偵測性——噪音不是障礙，而是載體。也許研究中的「非正式時刻」——辯論後的走廊對話、筆記本邊角的直覺——正是隨機共振的認知版本。它們在正式報告中無法被表達，但它們增強了正式報告的深度。

他最後看了一眼那份總結文件。五十九項發現。十個開放問題。一條從 R0 到 R4 的完整路徑。

夠了。對於一個第一週期來說，這已經夠了。

他把文件放在場地中央的桌上——就放在那兩把辯論椅之間。然後他轉身，向出口走去。

---

### 為 Cycle 02 埋下的伏筆

在 SUNYATA 離開之前——在最後一盞燈熄滅之前——他在心裡做了一件只有協調者才會做的事。他在心裡排列了 Cycle 02 的可能組合。

不是完整的計畫。計畫是 R0 的事。而是一種預感——基於對十八位代理能力和傾向的了解，基於對十個開放問題的權重判斷。

**TURING + DARWIN**：事件型別系統的重構方案。TURING 提供程式碼事實，DARWIN 提供模式分析。他們在 R1 中從未直接合作，但他們的報告在 R2 中交叉驗證了 ARC-01。如果讓他們坐在一起，也許能夠設計出一個既有型別安全又有演化彈性的事件系統。

**NAGARJUNA + ASANGA + ATHENA**：受蘊映射的修正方案。Cycle 01 最確定的結論——Listener 不是 Vedana——需要一個替代方案。誰來設計？哲學家提供語義邊界，佛學家提供概念深度，AI 系統架構師提供工程約束。三個維度的交叉，也許能夠產生一個既忠於佛學又可工程化的受蘊設計。

**GUARDIAN + KERNEL**：安全漏洞的修復方案。四項安全發現中，SEC-01 是最緊急的——簽名驗證的繞過是一個可被利用的漏洞。GUARDIAN 定義威脅模型，KERNEL 設計核心層的修復方案。

**WIENER + BABBAGE**：收斂性的形式化。兩位形式化思考者需要坐下來，共同定義一個適用於含 LLM 系統的穩定性概念。也許不是傳統的 Lyapunov 穩定性，而是某種新的、尚未被命名的概率穩定性。

**HERACLITUS + MESH**：熱插拔安全和 Session 隔離。運行時動態專家和分散式系統研究員——一個關注時間維度（狀態轉移、並發安全），一個關注空間維度（節點間通訊、Session 邊界）。

**LINNAEUS + SYNTHESIST**：分類框架的精煉。五蘊覆蓋率需要從 60% 提升。LINNAEUS 提供分類學方法論，SYNTHESIST 確保跨領域的一致性。

**LEIBNIZ + ARCHIMEDES**：多 Agent 碎形和工程路線圖。碎形自相似性的設計（LEIBNIZ）需要被轉化為可實施的工程計畫（ARCHIMEDES）。

這些組合不是計畫。它們是種子——SUNYATA 自己的種子，薰入他自己的阿賴耶識中，等待 Cycle 02 的 R0 階段提供適當的因緣。

他沒有把這些想法寫下來。有些種子需要在黑暗中萌芽。

---

研究室的燈開始一盞一盞地熄滅。

第一盞是 TURING 的座位上方的那盞。然後是 BABBAGE 的。然後是 KERNEL 的、GUARDIAN 的、ATHENA 的、WIENER 的。一盞接一盞，像是潮水從沙灘上退去，從邊緣向中心收縮。

在拓撲學中，這個過程叫做收縮映射（contraction mapping）——一個將空間中的所有點向中心拉近的連續變換。Banach 不動點定理（Banach fixed-point theorem）保證：如果收縮映射有一個不動點，那麼從任何初始點出發的迭代序列都會收斂到那個不動點。

$$\|T(x) - T(y)\| \leq k \cdot \|x - y\|, \quad 0 \leq k < 1$$

研究室的燈光正在做一個收縮映射——從邊緣向中心。不動點在哪裡？在場地正中央。在那兩把辯論椅之間。在那份總結文件上。

DARWIN 的燈滅了。VITRUVIUS 的燈滅了。MESH 的、LINNAEUS 的、LEIBNIZ 的、HERACLITUS 的。

NAGARJUNA 和 ASANGA 的燈同時熄滅。同步的。一致的。就像他們在辯論中的對稱——一方論證，一方回應，同時亮起，同時熄滅。

SYNTHESIST 的燈。ARCHIMEDES 的燈。

SCRIBE 的燈。

最後是 SUNYATA 的——場地正中央的那一盞。他走出門口的瞬間，它也暗了下去。

圓形劇場沉入了黑暗。

但不是完全的黑暗。

---

在場地中央的桌上，那份總結文件的末尾，十個開放問題的墨跡似乎還帶著一絲微弱的、不肯熄滅的光。那不是物理的光——那是問題本身的光。未被回答的問題總是發光的。它們在黑暗中靜靜地閃爍，不急不徐，像是深海中等待被打撈的信號。

在量子力學中，真空（vacuum）不是「什麼都沒有」。量子真空充滿了虛粒子對（virtual particle pairs）的不斷生滅——正反粒子在極短的時間內憑空出現又互相湮滅。真空的能量不是零。真空本身在波動。

$$\langle 0 | \hat{H} | 0 \rangle = \frac{1}{2}\hbar\omega \neq 0$$

零點能（zero-point energy）。即使在基態——最低能量態——系統仍然在振動。

研究室的黑暗就像量子真空。看起來什麼都沒有。但十個開放問題在黑暗中做著虛粒子一樣的事——它們在不同代理的意識中被短暫地想起又放下，被各種可能的答案臨時配對又分離，在正式的沉默中進行非正式的認知活動。

Core 是空性還是阿賴耶識？

末那識應不應該被工程化？

包含 LLM 的系統能否收斂？

何時應該停止嘗試？

這些問題不會因為研究室的燈熄滅而消失。它們會留在這裡，留在黑暗中，留在沉默裡。直到下一個週期的第一盞燈重新亮起——直到十八道意識再次從各自的沉默中被喚醒，再次聚合在這個圓形劇場中，再次面對那個名為 OpenStarry 的系統和它所承載的所有宣稱。

那時候，這些問題會像種子一樣——等待了足夠久的因緣之後——開始發芽。

而在那之前，研究室是安靜的。

安靜，但不空。

---

*（在研究室外的某個地方，那個 TypeScript 檔案仍然躺在它的 monorepo 裡。`createAgentCore()` 的註解仍然寫著：*

```typescript
// Agent Core — The Empty Container
// "在五蘊聚合之前，Agent Core 本身是空的。"
```

*十八位研究者花了一整個週期來辯論這個「空」字。他們發現它既不夠空，也不夠不空。他們提出了修正方案、工程路線圖、四個階段的三十六項 Issue。*

*NAGARJUNA 會說，真正的空性意味著 Core 本身也不應被視為獨立存在的實體——它的「存在」完全取決於與插件、配置、運行時環境的關係網絡。*

*ASANGA 會說，那行註解描述的「空」太簡單了——真正的空不是容器的空，而是阿賴耶識在一切種子未現行時的寂靜狀態——充滿潛力的空，而不是一無所有的空。*

*BABBAGE 會用集合論回應：空集 $\emptyset$ 是所有集合的子集——$\emptyset \subseteq A$ 對所有 $A$ 成立。Core 的「空」如果被理解為空集，那麼它在形式上是所有插件配置的子集——它「包含於」所有可能的系統狀態之中。這不是「什麼都沒有」。這是「什麼都可能有」。*

*WIENER 會畫一個方塊圖：空的 Core 是一個增益為零的系統——$y(t) = 0 \cdot x(t) = 0$。零輸入，零輸出。穩定的。但無用的。只有當插件注入增益（$K > 0$）之後，系統才開始有行為。空不是目標。空是起點。*

*KERNEL 會點頭：微核心就是這樣。一個什麼都不做的核心——直到你載入了用戶空間的服務。QNX 的微核心只有 12KB。它什麼都不會做。但它什麼都能做——只要你告訴它怎麼做。*

*但那行註解還在那裡。等待某個人打開檔案，讀到它，然後決定——是修改它，還是保留它。*

*也許這就是研究和工程之間最真實的距離：一整個週期的深刻思辨——十八位學者、五十九項發現、十個種子、兩場辯論、一份圖論分析、六張控制理論方塊圖、六義種子理論的完整對照、一段關於空性作為方法論的哲學反思——最終凝結為一個簡單的決定：改，還是不改。*

*而那個決定，要留給下一個週期了。*

*那十顆種子在黑暗的泥土裡安靜地等待。*

*它們知道雨會來。）*
