# 第九章：十九份行動方案

---

R4 定稿的圓形劇場，比辯論時安靜得多。

不是那種空洞的安靜——五場辯論的餘波仍然在空氣中振動，像大提琴的弦在最後一個音符結束後繼續顫抖。但辯論的張力已經退去。取而代之的是另一種密度：交付的密度。十九位研究員各自坐在自己的座位上，面前擺著初稿、修訂稿、程式碼片段、映射表。R4 不是辯論。R4 是收成。

在工程管理的術語中，R4 是**交付閘門**（Delivery Gate）——產品從研發流程進入交付管線的最後關卡。在軟體開發生命週期（SDLC）中，這個閘門的意義是明確的：

$$\text{Gate}_{R4} : \text{Research} \to \text{Deliverable} \quad \iff \quad \forall \, d_i \in \text{Decisions}, \; \exists \, a_i \in \text{Actions} : \text{trace}(a_i) = d_i$$

每一項辯論裁定（$d_i$）都必須有對應的行動方案（$a_i$），且行動方案必須可追溯回裁定本身。ARCHIMEDES 在他的筆記本上寫的第一行就是這個公式——追溯性（traceability）是工程交付的基本紀律。

SUNYATA 站在場地中央，環顧全場。他已經不需要宣布什麼了——每個人都知道該做什麼。R3 的五場共識像五根柱子，支撐起了一個可以在其中工作的結構。現在的任務是把辯論的裁定轉化為可交付的文件，把哲學的洞見翻譯為工程師能讀懂的語言。

「ARCHIMEDES，」他說。「你先。」

---

## I. 明天我們需要寫 TypeScript

ARCHIMEDES 從座位上站起來的方式和所有研究員都不同。

NAGARJUNA 站起來像一把出鞘的劍。ASANGA 站起來像一棵樹在風中緩緩直立。BABBAGE 站起來像一台精密儀器被啟動。ARCHIMEDES 站起來像一個建築工人拿起了鏟子——沒有戲劇性，沒有儀式感，只有一種「活兒來了，開工」的樸素動力。

「先說一句。」他走到展示區，打開了一份長達四十頁的文件。「過去三天，你們在辯論中產出了五項裁定——觀察-干預分離、雙模式 vedana、纖維叢投影、漸進分類、戒慧框架。每一項都很美。每一項都讓我作為旁聽者感到智識上的愉悅。」

他停了一拍。

「但哲學很美，明天我們需要寫 TypeScript。」

全場有幾個人笑了。BABBAGE 的嘴角微微動了一下——那是他最接近大笑的表情。NAGARJUNA 沒有笑，但他的眼神裡有一種認可：一個懂得什麼時候該把天上的東西帶回地面的人，值得尊重。

ARCHIMEDES 指著展示區的投影。「這份文件的結構遵循 MoSCoW 優先級框架——Must、Should、Could、Won't。不過我把它映射到了更直觀的命名：P0 阻塞性、P1 高優先、P2 標準、P3 未來、P4 遠期。」

他在白板上畫了優先級矩陣：

```
┌──────────────────────────────────────────────────────────────────┐
│                    MoSCoW → P-Level 映射                         │
├──────────┬─────────┬──────────────────────────────────────────────┤
│ MoSCoW   │ P-Level │ 語義                                        │
├──────────┼─────────┼──────────────────────────────────────────────┤
│ Must     │ P0      │ 阻塞性——不完成則無法開始其他工作              │
│ Should   │ P1      │ 高優先——本 Cycle 必須完成                     │
│ Could    │ P2      │ 標準——重要但可延後                            │
│ Won't    │ P3/P4   │ 未來/遠期——記錄但不在本次交付                 │
└──────────┴─────────┴──────────────────────────────────────────────┘
```

---

> *SCRIBE 旁白：ARCHIMEDES 是研究團隊裡唯一一個在辯論場上始終保持沉默的工程師。不是因為他沒有意見——他的意見比任何人都具體。而是因為他的意見必須等到所有辯論結束之後才有意義。你不能在房子還在設計的時候就開始算水泥用量。但一旦設計定案，算水泥用量的人就是最重要的人。*

---

### P0：三件阻塞性工作

他從優先級最高的項目開始。

「P0——阻塞性。三件事。必須在任何其他工作開始之前完成。」

他舉起一根手指。

「第一，SEC-01。修復 package-name 插件簽名繞過漏洞。」他看了一眼 GUARDIAN。

GUARDIAN 站了起來。他的手裡拿著一份標記為「CRITICAL」的安全報告——封面上的紅色邊框比其他任何文件都醒目。

「讓我把這個漏洞的嚴重性用形式化語言說清楚。」

他走到白板前，寫下了漏洞的精確位置和攻擊路徑：

```typescript
// [程式碼: packages/core/src/sandbox/sandbox-manager.ts#L371]
// v0.24.0-beta 現行程式碼（簡化）

async verifyPlugin(plugin: IPlugin): Promise<VerificationResult> {
  const pluginFilePath = plugin.manifest?.filePath;

  if (!pluginFilePath) {
    // BUG: 當 pluginFilePath 為 undefined 時
    // 整個簽名驗證被跳過
    return { verified: true, reason: 'no-file-path' };  // ← 這裡
  }

  // 正常的簽名驗證邏輯...
  return this.cryptoVerify(pluginFilePath, expectedSignature);
}
```

「攻擊向量。」他在白板上畫了一個攻擊流程圖：

```
攻擊者行為：
┌──────────────────────────────────────────────────────────────────┐
│ 1. 建立一個惡意 Plugin，故意不提供 filePath                       │
│ 2. Plugin manifest: { name: "legit-plugin", filePath: undefined } │
│ 3. sandbox-manager.verifyPlugin() 被調用                          │
│ 4. pluginFilePath === undefined → 跳過簽名驗證                    │
│ 5. 返回 { verified: true } → 惡意 Plugin 被信任載入               │
│ 6. Plugin 獲得完整的 ToolContext 存取權限                          │
│ 7. 可以存取 EventBus、StateManager、所有已註冊的工具               │
└──────────────────────────────────────────────────────────────────┘
```

「在 CVSS v3.1 評分框架下：」

$$\text{CVSS} = \text{Base}(\text{AV:L}/\text{AC:L}/\text{PR:N}/\text{UI:N}/\text{S:C}/\text{C:H}/\text{I:H}/\text{A:H}) = 9.8 \; (\text{Critical})$$

「攻擊向量是本地（AV:L）——需要存取插件目錄。攻擊複雜度低（AC:L）——只需省略一個欄位。不需要權限（PR:N）。不需要用戶互動（UI:N）。影響範圍改變（S:C）——跳出沙箱邊界。機密性、完整性、可用性全部高影響。」

他轉身面向全場。「一個繞過簽名的漏洞。每一天它不被修復，系統就多一天裸奔。六個開發週期了。仍然沒修。」

GUARDIAN 接著展示了修復方案的程式碼：

```typescript
// 修復後的 verifyPlugin
async verifyPlugin(plugin: IPlugin): Promise<VerificationResult> {
  const pluginFilePath = plugin.manifest?.filePath;

  if (!pluginFilePath) {
    // FIX: 缺少 filePath = 無法驗證 = 不信任
    logger.warn('Plugin verification failed: missing filePath', {
      pluginName: plugin.manifest?.name ?? 'unknown',
    });
    return {
      verified: false,
      reason: 'missing-file-path',
      severity: 'critical',
    };
  }

  return this.cryptoVerify(pluginFilePath, expectedSignature);
}
```

「三行修改。一個 `if` 條件的反轉。但語義變化是根本性的——從『無法驗證等於信任』變成『無法驗證等於不信任』。這是安全工程的**失敗安全原則**（fail-safe default）：

$$\text{verify}(\bot) = \text{reject} \qquad (\text{not} \quad \text{verify}(\bot) = \text{accept})$$

在密碼學中，$\bot$（底值）代表缺少的或不可用的資訊。對 $\bot$ 的預設處理必須是拒絕。這是 Kerckhoffs 原則的推論——系統的安全性不應依賴於攻擊者的善意。」

---

ARCHIMEDES 接手。「第二個 P0。」他舉起第二根手指。「實作 ISensation 介面。」

他在展示區切換到一段程式碼。

```typescript
// v0.24.0-beta 現行的 ISensation
export interface ISensation extends IOpenStarryPlugin {
  readonly skandha: 'vedana';
}
```

「三行。一個空殼。」他的語氣不帶批判——只是陳述事實。「這是序章裡的那個空殼。整個 Cycle 02 的研究，從某種意義上說，就是為了填充這三行。」

TURING 站了起來。他的螢幕投射了完整的 ISensation 介面——不是節錄，不是簡化版，而是經過五場辯論淬鍊後的完整型別定義：

```typescript
/**
 * ISensation — 受蘊 Root Interface
 * @skandha vedana (受蘊)
 *
 * 受蘊涵蓋三受 (三種感受)：
 * - Dukkha (苦): 負向回饋
 * - Sukha (樂): 正向回饋
 * - Upekkha (捨): 中性平衡
 *
 * 設計原則 (來自辯論裁定)：
 * - Debate 1: 感測與建議在同一介面，但概念分離
 * - Debate 2: 完整 PID 評估在 tick 邊界，輕量標籤隨事件
 * - Debate 4: VedanaPlugin IS the Pattern A observer
 *
 * Sanskrit: Vedanā (वेदना)
 */
export interface ISensation {
  readonly skandha: 'vedana';

  /**
   * 評估當前三受狀態 — 完整的 PID 感測讀數
   *
   * 控制理論對應: y(t) = h(x(t)) + v(t)
   * 感測器讀數函數。每個 tick 調用一次。
   *
   * @returns VedanaAssessment 含感測層 + 控制建議層
   */
  assess(): VedanaAssessment;

  /**
   * 攝取原始系統指標 — 通用數值輸入通道
   *
   * 多輸入感測器融合通道 1: 量化指標
   * (CPU, memory, latency, error rate...)
   */
  ingestMetrics(metrics: Record<string, number>): void;

  /**
   * 攝取工具執行結果 — 行蘊回報通道
   *
   * 多輸入感測器融合通道 2: 離散事件
   * 十二因緣: 觸(sparśa) → 受(vedanā)
   */
  ingestToolResult(toolName: string, isError: boolean, durationMs: number): void;

  /**
   * 攝取 LLM 回應結果 — 想蘊回報通道
   *
   * 多輸入感測器融合通道 3: 語言模型元數據
   */
  ingestLLMResult(tokenCount: number, stopReason: string): void;

  /**
   * 訂閱受蘊閾值事件 — 看門狗計時器泛化
   *
   * 經典看門狗: y(t) > T_timeout → alarm
   * 泛化版: v_type(t) > θ → handler(signal)
   */
  onThreshold(channel: VedanaType, threshold: number,
              callback: (signal: VedanaSignal) => void): () => void;

  /**
   * 取得受蘊標籤 — O(1) 快取查詢
   *
   * 儀表板 LED 指示燈: 不計算，只讀快取
   * Debate 2 裁定: 每個事件附帶的輕量標籤來源
   */
  getVedanaTag(): VedanaTag;
}
```

TURING 讓投影停了整整十秒。他指著每一個方法，聲音平板而精確：

「每一個方法都可以追溯到辯論裁定。`assess()` 來自辯論 1 的 VedanaAssessment 雙層結構——感測層加控制建議層。`getVedanaTag()` 來自辯論 2 的輕量事件標籤裁定——$O(1)$ 快取查詢，不重新計算 PID。`onThreshold()` 是 WIENER 的三通道 PID 控制器需要的事件驅動訂閱機制。三個 `ingest` 方法是多輸入感測器融合的三個通道。」

WIENER 從座位上微微前傾。他需要確認三通道 PID 的輸出規格是否被正確翻譯。

他拿出方格紙，在上面寫下了驗收公式：

$$\text{VedanaAssessment} = \underbrace{\begin{pmatrix} d(t) \\ s(t) \\ u(t) \\ \vec{\sigma}(t) \end{pmatrix}}_{\text{Layer 1: Sensor}} \oplus \underbrace{\begin{pmatrix} u_{\text{ctrl}}(t) \\ r(t) \\ f(t) \end{pmatrix}}_{\text{Layer 2: Controller}}$$

「Layer 1 是感測器輸出。$d(t)$, $s(t)$, $u(t)$ 是三通道 PID 的測量值——苦、樂、捨。$\vec{\sigma}(t)$ 是信號陣列——原始事件的時間戳和來源。純觀察。被動。不改變系統狀態。」

「Layer 2 是控制器建議。$u_{\text{ctrl}}(t)$ 是統合控制輸出——三通道 PID 的加權和。$r(t)$ 是推薦動作——continue、reflect、restrict、halt。$f(t)$ 是新鮮度指示——current、cached、default。辯論 1 裁定：建議是諮詢性的。ExecutionLoop 保留忽略的權力。」

他在方格紙上重重勾了一個勾。「翻譯是準確的。」

---

ARCHIMEDES 切換到 VedanaAssessment 的完整 TypeScript 定義：

```typescript
/** 三受類型 */
type VedanaType = 'dukkha' | 'sukha' | 'upekkha';

/** 受蘊標籤（輕量快取，用於事件標記） */
type VedanaTag = 'dukkha' | 'sukha' | 'upekkha';

/** 受蘊信號 — 單一感受事件的記錄 */
interface VedanaSignal {
  readonly type: VedanaType;
  readonly intensity: number;     // 0.0–1.0
  readonly source: string;        // e.g., 'tool:file_read', 'llm:timeout'
  readonly timestamp: number;     // Date.now()
}

/** 受蘊推薦動作 */
type VedanaRecommendation =
  | { action: 'continue' }
  | { action: 'reflect'; prompt: string }
  | { action: 'restrict'; tools: string[] }
  | { action: 'halt'; reason: string };

/**
 * VedanaAssessment — 受蘊評估報告
 *
 * 雙層結構 (Debate 1 裁定):
 * - Layer 1: 感測器輸出 (純觀察，被動)
 * - Layer 2: 控制建議 (諮詢性，可被忽略)
 *
 * BABBAGE 的互模擬條件在 Layer 1 滿足:
 * 只讀取 Layer 1 的消費者行為不受 Layer 2 影響
 */
interface VedanaAssessment {
  // ── Layer 1: Sensor Output (pure observation) ──
  readonly dukkha: number;        // 0.0–1.0
  readonly sukha: number;         // 0.0–1.0
  readonly upekkha: number;       // 0.0–1.0
  readonly signals: readonly VedanaSignal[];
  readonly timestamp: number;

  // ── Layer 2: Controller Suggestion (advisory) ──
  readonly controlOutput: number;
  readonly recommendation: VedanaRecommendation;
  readonly recommendationFreshness: 'current' | 'cached' | 'default';
}
```

「雙層——辯論 1 的核心裁定。」ARCHIMEDES 指著螢幕。「`readonly` 修飾符強制不可變性。`recommendationFreshness` 是 BABBAGE 在辯論尾聲加入的——防止陳舊的 'halt' 建議在條件改善後仍然持續。」

BABBAGE 從筆記本中抬起頭。他在確認自己的互模擬條件是否被完整保留：

$$\forall \, \text{consumer} \, C : C \text{ reads only Layer 1} \implies \text{Behavior}(S) \sim \text{Behavior}(S')$$

「互模擬在消費層滿足。」他說。簡潔。完整。句號。

---

「第三個 P0。」ARCHIMEDES 舉起第三根手指。「實作 VedanaPlugin。辯論 4 裁定：Pattern A 觀察者就是 VedanaPlugin。一個插件，一個介面，一個蘊。」

他展示了 VedanaPlugin 的三層架構圖——這次不是抽象的方塊，而是帶有完整方法簽名的工程藍圖：

```
┌────────────────────────────────────────────────────────────────┐
│                     VedanaPlugin (ISensation)                   │
│                     Pattern A Observer                          │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Layer 3: Assessment Output                                    │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ assess() → VedanaAssessment                              │  │
│  │ getVedanaTag() → VedanaTag (O(1) cache)                  │  │
│  │ onThreshold(channel, θ, callback) → unsubscribe          │  │
│  └──────────────────────────────────────────────────────────┘  │
│                          ↑                                     │
│  Layer 2: PID Control Engine (WIENER)                          │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ DukkhaPID: K_p=1.0, K_i=0.3, K_d=0.5  (fast response)  │  │
│  │ SukhaPID:  K_p=0.5, K_i=0.7, K_d=0.3  (trend tracking) │  │
│  │ UpekkPID:  K_p=0.3, K_i=0.2, K_d=0.8  (stability pred) │  │
│  │                                                          │  │
│  │ U(t) = W_d·u_d(t) + W_s·u_s(t) + W_u·u_u(t)            │  │
│  └──────────────────────────────────────────────────────────┘  │
│                          ↑                                     │
│  Layer 1: Sensor Array (ATHENA)                                │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────────┐       │
│  │ DukkhaSensor  │ │ SukhaSensor  │ │ UpekkhaSensor    │       │
│  │ error_rate    │ │ completion   │ │ variance         │       │
│  │ consec_fail   │ │ efficiency   │ │ oscillation      │       │
│  │ latency_spike │ │ quality      │ │ drift_rate       │       │
│  │ token_burn    │ │              │ │                  │       │
│  │ resource_pres │ │              │ │                  │       │
│  └──────────────┘ └──────────────┘ └──────────────────┘       │
│          ↑                ↑                 ↑                  │
│  ingestMetrics()  ingestToolResult()  ingestLLMResult()        │
└────────────────────────────────────────────────────────────────┘
```

ATHENA 從座位上補充了感測器的技術規格。她的語氣一如既往地直截了當——沒有哲學，沒有類比，只有系統設計。

「DukkhaSensor 的五個輸入信號。」她列出清單。

```
┌─────────────────────────────────────────────────────────────┐
│ DukkhaSensor 輸入信號規格                                     │
├──────────────────┬──────────────────┬────────────────────────┤
│ 信號名            │ 來源              │ 計算                   │
├──────────────────┼──────────────────┼────────────────────────┤
│ error_rate       │ SafetyMonitor    │ errors / window_size   │
│ consecutive_fail │ SafetyMonitor    │ counter (0, 1, 2...)   │
│ latency_spike    │ ExecutionLoop    │ (actual-μ) / σ         │
│ token_burn_rate  │ SafetyMonitor    │ Δtokens / Δtime        │
│ resource_pressure│ MetricsCollector │ mem_used / mem_limit   │
├──────────────────┴──────────────────┴────────────────────────┤
│ 融合公式:                                                     │
│ e_d(t) = w₁·err + w₂·fail + w₃·lat + w₄·tok + w₅·res       │
│ 預設權重: w = (0.3, 0.25, 0.15, 0.15, 0.15)                  │
└─────────────────────────────────────────────────────────────┘
```

「SukhaSensor 追蹤三類正向信號——任務完成率、效率提升、品質分數。UpekkhaSensor 追蹤三類穩定性指標——方差、振盪幅度、漂移率。偏離穩態越遠，捨受越低。」

WIENER 補充了 PID 參數的調優理論根據：

「三組 PID 參數不是隨意選取的。它們遵循 **Ziegler-Nichols 調優法**的第一方法——基於階躍響應的經驗公式。」

他在方格紙上寫下調優過程：

$$\text{Ziegler-Nichols Step Response Method:}$$

$$\text{Given: } L = \text{dead time}, \quad T = \text{time constant}$$

$$K_p = \frac{1.2T}{L}, \quad T_i = 2L, \quad T_d = 0.5L$$

$$\implies K_i = \frac{K_p}{T_i} = \frac{0.6T}{L^2}, \quad K_d = K_p \cdot T_d = \frac{0.6T}{1}$$

「但三受通道有不同的時間特性，所以需要不同的參數調優策略：」

```
┌───────────┬──────────────────────────────────────────────────┐
│ 通道       │ Ziegler-Nichols 適配理由                          │
├───────────┼──────────────────────────────────────────────────┤
│ Dukkha    │ 短死時間 L_d → 高 K_p (快速反應)                   │
│           │ 苦痛不等人。系統出錯時需要立即感知。                 │
│           │ K_p=1.0, K_i=0.3, K_d=0.5                        │
├───────────┼──────────────────────────────────────────────────┤
│ Sukha     │ 長時間常數 T_s → 高 K_i (趨勢追蹤)                │
│           │ 快樂會衰減。需要積分項追蹤長期正向趨勢。            │
│           │ 衰減函數: s(t) = s₀ · e^{-λt}, λ = 0.1           │
│           │ K_p=0.5, K_i=0.7, K_d=0.3                        │
├───────────┼──────────────────────────────────────────────────┤
│ Upekkha   │ 高振盪風險 → 高 K_d (預測性調節)                   │
│           │ 平衡是動態的。偏離趨勢比偏離本身更重要。            │
│           │ K_p=0.3, K_i=0.2, K_d=0.8                        │
└───────────┴──────────────────────────────────────────────────┘
```

「苦受通道的阻尼比（damping ratio）：」

$$\zeta_d = \frac{K_d^{(d)}}{2\sqrt{K_p^{(d)} \cdot K_i^{(d)}}} = \frac{0.5}{2\sqrt{1.0 \times 0.3}} = \frac{0.5}{2 \times 0.548} \approx 0.456$$

「$\zeta_d \approx 0.456$ — 欠阻尼。這意味著苦受通道在受到衝擊後會產生振盪——不是缺陷，而是設計。你希望系統在遇到問題時快速感知（振盪上升），但不要過度反應到鎖死（過阻尼 $\zeta > 1$ 會延遲反應）。」

「樂受通道的衰減時間常數——」

$$s(t) = s_0 \cdot e^{-\lambda t}, \quad \lambda = 0.1 \implies \tau_{1/2} = \frac{\ln 2}{\lambda} \approx 6.93 \text{ ticks}$$

「樂受的半衰期約 7 個 tick。一次成功的工具調用帶來的樂受，在 7 個 tick 後衰減到一半。這防止系統因為一次成功就過度自信——在 ASANGA 的術語裡，這就是 *sukha-vedanā* 的自然消散（*kṣaṇa-bhaṅga*，刹那壞滅）。」

ASANGA 點了點頭。「受蘊的特性之一就是無常。樂受不會永駐。苦受也不會永駐。衰減函數是受蘊無常性的數學表達。」

> 「諸受無常，皆從觸生，依緣而起，趣於壞滅。」
> ——《相應部》36.11（*Saṃyutta Nikāya*, Vedanā-saṃyutta）

「`e^{-\lambda t}` 就是壞滅的速率。」ASANGA 的聲音平穩。「指數衰減——不是線性的遞減，而是從最初的強度開始急劇下降，然後逐漸趨近於零但永不完全消失。這和修行經驗一致——強烈的喜悅迅速褪去，但微弱的餘韻可以持續很久。」

---

ARCHIMEDES 合上了 P0 的部分。

「三個 P0 項目。如果只能做一件事，修 SEC-01。如果能做兩件事，加上 ISensation。如果能做三件事，完成 VedanaPlugin。這是最小可行的交付路徑。」

他用工程估算的語言給出了時間預算：

```
┌────────────────────────────────────────────────────────────┐
│ P0 工時估算                                                 │
├──────────────┬──────┬──────────────────────────────────────┤
│ 項目          │ 人天  │ 說明                                 │
├──────────────┼──────┼──────────────────────────────────────┤
│ SEC-01 修復   │ 0.5  │ 3 行程式碼 + 測試 + code review       │
│ ISensation   │ 3    │ 介面定義 + 輔助型別 + type guard 更新  │
│ VedanaPlugin │ 8    │ 三通道感測器 + PID 引擎 + 事件標籤    │
├──────────────┼──────┼──────────────────────────────────────┤
│ P0 合計       │ 11.5 │ 約 2-3 週（單人）                     │
└──────────────┴──────┴──────────────────────────────────────┘
```

---

### P1：四件高優先工作

ARCHIMEDES 繼續向下展開。

「P1——高優先。四件事。」

「第一，EgoFramework 重構。」

ASANGA 微微前傾。他的雙層我執模型——硬核心對應不可動搖的根本約束，軟外殼對應可以被 vedana 回饋調整的行為傾向——是辯論 2 中被確認的核心設計。

ARCHIMEDES 展示了 EgoFramework 的架構：

```typescript
/**
 * EgoFramework — 我執框架
 *
 * 雙層結構 (ASANGA 的唯識學模型):
 * - 硬核心: 機器人三定律 — 不可覆寫
 * - 軟外殼: PID 調參邊界 — 由 vedana 回饋動態調整
 *
 * 佛學對應:
 * 硬核心 = 阿羅漢的根本戒 (不殺、不盜、不妄)
 * 軟外殼 = 隨煩惱 (可通過修行調伏)
 */
interface EgoFramework {
  /** 硬核心約束檢查 — 不可繞過 */
  checkHardConstraints(action: ProposedAction): {
    allowed: boolean;
    violatedRule?: string;
  };

  /** 軟外殼調參 — 根據 vedana 回饋調整行為邊界 */
  adjustSoftBoundaries(assessment: VedanaAssessment): void;

  /** 當前行為邊界查詢 */
  getBoundaries(): {
    hardCore: readonly string[];      // immutable rules
    softShell: Map<string, number>;   // tunable parameters
  };
}
```

「硬核心是機器人三定律——不可覆寫，不可繞過。即使 VedanaPlugin 全部推薦 expand，硬核心仍然說不就是不。軟外殼是 PID 調參——由 vedana 回饋動態調整行為邊界。」

「第二，插件生命週期四態狀態機。辯論 5 的戒慧框架。」

他展示了 DARWIN 驗證過的四態狀態機：

```
          ┌────────────────────────────────────────────┐
          │        Plugin Lifecycle State Machine       │
          │     (Debate 5: Sila-Prajna Framework)       │
          └────────────────────────────────────────────┘

          ┌──────────┐    signature_valid     ┌──────────┐
          │          │ ──────────────────────→ │          │
     ──→  │ PENDING  │                         │  ACTIVE  │
          │          │ ←────────────────────── │  (現行)  │
          └──────────┘    reinstated           └──────────┘
               │                                    │
               │ signature_invalid               anomaly_detected
               │ OR unsigned                     OR CRL_match
               ↓                                    ↓
          ┌──────────┐                         ┌──────────┐
          │QUARANTINE│    human_reject          │ REVOKED  │
          │(有漏種子) │ ──────────────────────→ │  (斷惑)  │
          │ 待眾緣   │                          │          │
          └──────────┘                         └──────────┘
               │                                    │
               │ human_approve                   confirmed_malicious
               │ → ACTIVE                           │
               │                                    ↓
               │                               ┌──────────┐
               └────────────── never_approve ─→ │  BANNED  │
                                                │(不復更生) │
                                                │ 火燒種子  │
                                                └──────────┘
```

NAGARJUNA 看著狀態機圖，他的表情帶著一種微妙的滿足。「四態。四個佛學對應。Active 是現行——種子成熟結果。Quarantined 是有漏種子待眾緣——條件不具足，種子不成熟。Revoked 是斷惑——智慧斷除煩惱種子。Banned 是不復更生——徹底斷滅，如同阿羅漢斷盡見惑。」

「第三，ToolContext.bus 洩漏修復。」ARCHIMEDES 簡要說明。「工具可以繞過沙箱事件過濾——TURING 發現的。需要替換為受限事件代理。」

「第四，SafetyMonitor 的 per-session 計數器。」

HERACLITUS 從座位上補充。「萬物皆流。但有些東西不應該跨 session 流動。當前的 SafetyMonitor 使用全局計數器——一個 session 的錯誤累積會影響另一個 session。這等於一個跨 session 的拒絕服務（DoS）漏洞。」

他在白板上畫了一個簡單的時間線圖：

```
Session A:  ━━━[err][err][err][err][err]━━━━━━━━━━━━━━━━
                                   ↑
                              counter = 5
                         triggers SAFETY_LOCKOUT

Session B (new, clean):  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                              counter = 5 (inherited!)
                         Session B 一出生就被鎖死
```

「修復方案：`Map<sessionId, CounterState>` 替代全局 `CounterState`。每個 session 有自己的計數器。Session A 的錯誤不影響 Session B。Heraclitean 的河流隔喻——你不能把上游的汙水排進下游的飲水。」

---

### P2 至 P4：完整行動清單

ARCHIMEDES 把展示區切換到總覽頁面。「P2 到 P4，我用表格展開。」

```
┌────┬──────────────────────────────┬────────────────────────┬──────┐
│ P  │ 項目                          │ 來源                    │ Plan │
├────┼──────────────────────────────┼────────────────────────┼──────┤
│ P2 │ CRL 檢查存根                  │ Debate 5 (GUARDIAN)     │ 24   │
│ P2 │ EventBus vedana 標籤型別      │ Debate 2 (ASANGA)       │ 26   │
│ P2 │ 宣言 #2 重寫                  │ R2 交叉審閱              │ 28   │
│ P2 │ 宣言 #6 重寫                  │ Debate 1 (觀察≠干預)    │ 28   │
│ P2 │ 阿賴耶識分佈架構文件註解       │ Debate 3 (BABBAGE)      │ 28   │
│ P2 │ 漸進分類文件                  │ Debate 4 (LINNAEUS)     │ 28   │
├────┼──────────────────────────────┼────────────────────────┼──────┤
│ P3 │ Pattern B 影子觀察者           │ Debate 4 (PENROSE)     │ 29   │
│ P3 │ Agent 協調層設計               │ Debate 3 (MESH)        │ AC   │
│ P3 │ 纖維叢一致性驗證               │ Debate 3 (BABBAGE)     │ AC   │
├────┼──────────────────────────────┼────────────────────────┼──────┤
│ P4 │ Pattern C 子代理觀察者         │ Debate 4 (PENROSE)     │ 未定 │
│ P4 │ 完整阿賴耶識 IPC 協議          │ Debate 3 (MESH)        │ 未定 │
└────┴──────────────────────────────┴────────────────────────┴──────┘
```

他最後展示了 Plan 影響總覽：

```
┌──────────────────────────────────────────────────────────────────┐
│                    Plan 影響總覽 (6 Plans)                        │
├──────────────┬───────────────────────────────────────────────────┤
│ Plan24       │ + 安全快速修復: SEC-01, 插件黑名單, CRL 存根       │
│ (安全)       │ + 戒慧框架的四態生命週期啟動點                      │
├──────────────┼───────────────────────────────────────────────────┤
│ Plan26       │ + 本次研究的主要設計輸入: ISensation, VedanaPlugin │
│ (Vedana)     │ + 三通道 PID, 事件標籤, 感測器陣列                 │
├──────────────┼───────────────────────────────────────────────────┤
│ Plan27       │ + 四態狀態機: active/quarantined/revoked/banned    │
│ (生命週期)    │ + 人工審批流程 (quarantine → active)               │
├──────────────┼───────────────────────────────────────────────────┤
│ Plan28       │ + 纖維叢投影註解, 漸進分類文件, 宣言 #2/#6 重寫    │
│ (文件對齊)    │ + 戒慧安全文件, 五蘊映射更新                       │
├──────────────┼───────────────────────────────────────────────────┤
│ Plan29       │ 新 Plan: Pattern B 影子觀察者                      │
│ (影子觀察者)  │ Worker Thread 深度分析, 受蘊+想蘊                  │
├──────────────┼───────────────────────────────────────────────────┤
│ Plan-AC      │ + 三項架構原則: 治理非控制, 纖維叢一致性, 戒引擎   │
│ (協調層)      │ + 阿賴耶識能藏的工程化                             │
└──────────────┴───────────────────────────────────────────────────┘
```

「四十頁。十四項行動。六個 Plan。完整的 TypeScript 介面規格。可以直接拿去寫程式碼。」

他看了一眼 SUNYATA。

「我的部分結束了。哲學很美。工程很具體。現在它們在同一份文件裡。」

---

## II. 五場辯論，一幅圖

SYNTHESIST 走向展示區時的步態和 ARCHIMEDES 截然不同。如果說 ARCHIMEDES 走路像一個拿起鏟子的建築工人，那麼 SYNTHESIST 走路更像一個站到畫布前的畫家——不是要創造什麼新的東西，而是要從已經存在的片段中看出一幅完整的圖景。

「ARCHIMEDES 給了你們一棵樹。」他開口時，語速比平時慢。「每一個分支都是一項行動，每一片葉子都是一個 TypeScript 介面。精確、具體、可執行。但我要讓你們看到整片森林。」

他在展示區投射出一幅圖——不是圖表，不是流程圖，而是更接近一張手繪的架構全景圖。五場辯論的裁定被標註在不同的位置，用虛線彼此連接，形成一個有機的網絡。

「五場辯論，表面上是五個獨立的問題。觀察-干預分離。三受普遍性。阿賴耶識分佈。觀察者分類。安全種子。但它們不是五個問題。它們是同一個架構的五個截面。」

他用範疇論（Category Theory）的語言形式化了這個統合：

$$\mathcal{C}_{\text{OpenStarry}} = (\text{Ob}, \text{Mor}, \circ)$$

其中對象集 $\text{Ob}$ 包含五個辯論裁定，態射集 $\text{Mor}$ 包含裁定之間的關聯。他在白板上畫了交換圖：

$$\begin{CD}
\text{Debate 1} @>{\text{authority}}>> \text{Debate 5} \\
@V{\text{identity}}VV @VV{\text{lifecycle}}V \\
\text{Debate 4} @>>{\text{seeds}}> \text{Debate 3}
\end{CD}$$

$$\text{Debate 2} \xrightarrow{\text{universality}} \text{all four}$$

「辯論 1 和辯論 4 匯合。」他在全景圖上畫出第一條弧線。「辯論 1 說：VedanaAssessment 包含感測器輸出和控制器建議，兩層分離。辯論 4 說：VedanaPlugin 就是 Pattern A 觀察者，分類為受蘊。合在一起——VedanaPlugin 是觀察者。它實作 ISensation。它產生的評估報告有兩個面向：被動的感受和諮詢性的建議。」

BABBAGE 在筆記本上寫下了匯合的形式化：

$$\text{Ruling}_1 \cap \text{Ruling}_4 = \{ \text{VedanaPlugin} \cong \text{Observer}_{A} \cong \text{ISensation} \}$$

「三個等價。一次確立。」

---

SYNTHESIST 繼續連線。

「辯論 1 和辯論 5 匯合。」第二條弧線。他在全景圖的右側寫下四行——完整的四層權限模型：

```
┌──────────────────────────────────────────────────────────────┐
│               Four-Layer Authority Model                      │
│                                                              │
│  Layer 1: SafetyMonitor  — 硬安全 — 絕對權限 — 戒律 (vinaya) │
│    │  verify(⊥) = reject; halt authority                     │
│    ↓                                                         │
│  Layer 2: VedanaPlugin   — 軟指導 — 諮詢權限 — 覺受 (vedanā) │
│    │  recommendation is ADVISORY                             │
│    ↓                                                         │
│  Layer 3: EgoFramework   — 身份約束 — 結構權限 — 我執 (grāha) │
│    │  hard core (immutable) + soft shell (tunable)           │
│    ↓                                                         │
│  Layer 4: Sila Engine    — 種子管理 — 預防權限 — 戒學 (śīla)  │
│    │  plugin blacklist, CRL, quarantine                      │
│    ↓                                                         │
│  [Plugin Lifecycle: active → quarantined → revoked → banned] │
└──────────────────────────────────────────────────────────────┘
```

「四層。每一層的權限低於上一層。」

LEIBNIZ 從座位上站起來。多代理協調是他的專業——四層權限模型的形式化需要他的 BDI 架構理論。

「讓我用 **BDI 架構**（Belief-Desire-Intention）來形式化這個四層模型。」

他走到白板的另一側，寫下了 BDI 的基本定義：

$$\text{Agent} = \langle B, D, I, \text{plan} \rangle$$

$$B : \text{Beliefs (信念集)} \quad D : \text{Desires (願望集)} \quad I : \text{Intentions (意圖集)}$$

$$\text{plan} : B \times D \to I$$

「在 OpenStarry 的語境中，四層權限模型映射到 BDI 架構的約束函數：」

$$I_{\text{final}} = \text{plan}(B, D) \quad \text{s.t.}$$

$$\begin{cases}
\forall i \in I_{\text{final}} : \text{Safety}(i) = \text{true} & \text{(Layer 1: SafetyMonitor)} \\
\text{VedanaAdvice}(B) \subseteq \text{context}(\text{plan}) & \text{(Layer 2: advisory input)} \\
\forall i \in I_{\text{final}} : \text{Ego}(i) = \text{true} & \text{(Layer 3: identity constraint)} \\
\forall p \in \text{plugins}(i) : \text{Sila}(p) \neq \text{banned} & \text{(Layer 4: seed filter)}
\end{cases}$$

「BDI 架構中，Agent 的意圖（Intention）是從信念和願望經過計劃函數產生的。但意圖不是自由的——它必須通過四層約束的過濾。SafetyMonitor 是硬約束，不通過就不執行。VedanaPlugin 是軟輸入，提供決策的感受背景。EgoFramework 是身份約束，確保行動符合 Agent 的自我定義。Sila Engine 是預防約束，確保使用的插件沒有被禁止。」

他在公式旁邊加了一個關鍵的定理：

$$\text{Theorem (LEIBNIZ):} \quad \text{Layer}_n \text{ cannot override Layer}_{n-1}$$

$$\forall n \in \{2,3,4\} : \neg(\text{Layer}_n \vdash \neg \text{Layer}_{n-1})$$

「低層級的權限不能覆寫高層級的決定。這是四層模型的核心不變量。VedanaPlugin 的建議永遠不能覆寫 SafetyMonitor 的 halt。EgoFramework 的軟外殼調整永遠不能違反 VedanaPlugin 標記的 critical 狀態。形式化保證了權限的嚴格層次性。」

GUARDIAN 注意到了第一層和第四層的微妙對稱——SafetyMonitor 是最內層的硬防禦，Sila Engine 是最外層的硬過濾。兩者夾住中間兩個軟層——VedanaPlugin 的諮詢和 EgoFramework 的調參。

「在安全架構中，」他補充，「這叫做**深度防禦**（Defense in Depth）。不只有一層防線。外層是 Sila——阻止惡意插件進入。內層是 SafetyMonitor——即使惡意行為突破了所有外層，最後一道閘門仍然存在。兩層硬防禦之間的軟層是指導和調節——不是安全關鍵的，但提供了行為最佳化的空間。」

```
Defense in Depth:

外部世界 → [Sila Engine] → [EgoFramework] → [VedanaPlugin] → [SafetyMonitor] → 行動
             ↑ 硬過濾        ↑ 身份約束       ↑ 感受諮詢       ↑ 硬安全
             不讓壞人進來     確保符合身份     提供感受背景     最後一道閘門
```

---

SYNTHESIST 繼續。他的動作越來越快。

「辯論 3 和辯論 2 匯合。」第三條弧線。

MESH 站了起來。分散式架構是他的語言。

「辯論 3 說：阿賴耶識以纖維叢投影分佈在協調層和 AgentCore。辯論 2 說：每個 EventBus 事件都帶有 vedana 標籤，每個 tick 都有完整的 PID 評估。合在一起——你得到了分散式意識的運行時圖景。」

他在白板上畫了分散式架構圖：

```
┌─────────────────────────────┐        IPC (fiber bundle)       ┌──────────────────────────┐
│     Coordination Layer       │ ←──────────────────────────────→ │       AgentCore           │
│                              │   cocycle condition:             │                          │
│  能藏 (neng-zang):           │   φ_ij · φ_jk = φ_ik           │  執藏 (zhi-zang):         │
│  - Capability Registry      │                                  │  - Guide binding          │
│  - Plugin Resolution         │   transition functions:          │  - Identity config        │
│  - Global Config             │   π_CL: Total → CL              │  - Runtime state          │
│                              │   π_AC: Total → AC              │                          │
│  所藏 (suo-zang, system):    │                                  │  所藏 (suo-zang, runtime):│
│  - Plugin Database           │                                  │  - StateManager           │
│  - System Settings           │                                  │  - SessionManager         │
│                              │                                  │                          │
│  Sila Engine:                │                                  │  VedanaPlugin:            │
│  - Plugin blacklist          │                                  │  - Three-channel PID      │
│  - CRL checks                │                                  │  - Event tagging          │
│  - Trust levels              │                                  │  - assess() per tick      │
└─────────────────────────────┘                                  └──────────────────────────┘
```

BABBAGE 在筆記本上寫下了纖維叢的嚴格定義：

$$\text{Fiber Bundle:} \quad E \xrightarrow{\pi} B$$

$$\text{where} \; E = \text{Alaya (total space)}, \; B = \{CL, AC\} = \text{base space}$$

$$\pi_{CL}^{-1}(\text{CL}) = \text{neng-zang} + \text{suo-zang}_{\text{sys}}$$

$$\pi_{AC}^{-1}(\text{AC}) = \text{zhi-zang} + \text{suo-zang}_{\text{rt}}$$

$$\text{Cocycle condition: } \phi_{CL \to AC} \circ \phi_{AC \to CL} = \text{id}_{CL}$$

「IPC 協議是纖維叢的轉換函數（transition function）。轉換函數必須滿足 cocycle condition——雙程一致性。從協調層發送一個能力查詢到 AgentCore，AgentCore 回傳結果，這個往返必須是恒等映射。資料不能在 IPC 通道中丟失或扭曲。」

MESH 補充了工程約束：「在分散式系統中，cocycle condition 等同於**冪等性**（idempotency）+ **一致性**（consistency）。IPC 訊息的發送和回覆必須滿足 exactly-once 語義——不多不少。這是任何分散式協調協議的基本要求。在 CAP 定理的框架下：」

$$\text{CAP: } \neg(C \wedge A \wedge P)$$

「OpenStarry 的協調層-AgentCore 架構選擇了 CP（一致性 + 分區容忍）而非 AP。因為在安全關鍵的 Agent 系統中，一致性比可用性更重要——你寧可暫停服務，也不能讓協調層和 AgentCore 對 Plugin 的信任等級產生分歧。」

---

SYNTHESIST 放下了筆。站在全景圖前，他的臉上有一種只在少數時刻見過的表情——所有碎片匯聚的安靜震動。

「辯論 4 定義了時間軸。」他在全景圖的底部畫了一條時間線。

```
時間軸 (Progressive Observer Path):

Past ←───────────────────────────────────────────────→ Future

Phase 1 (Plan26)          Phase 2 (Plan-AC)         Phase 3 (Post AC)
Pattern A                 Pattern B                 Pattern C
VedanaPlugin              Shadow Observer            Child Agent Observer
ISensation                ISensation + ICognition    All Five Aggregates
受蘊                       受蘊 + 想蘊               完整五蘊 + 末那識

"感受"                    "感受 + 分析"             "感受 + 分析 + 自省"

    ────────────→ 螺旋上升 ────────────→
```

「五場辯論。五場共識。一幅圖。」

他退後一步，讓所有人看清整幅全景圖。

PENROSE 從座位上微微前傾。他的聲音帶著物理學家特有的尺度感：

「Pattern A 到 Pattern C 的演化路徑——這讓我想到意識研究中的**整合資訊理論**（Integrated Information Theory, IIT）。Giulio Tononi 的 $\Phi$ 值量測一個系統的整合資訊量——」

$$\Phi = \text{ei}(\text{MIP}) = \text{entropy}(\text{whole}) - \sum_i \text{entropy}(\text{part}_i)$$

「$\Phi$ 越高，系統的整合度越高，意識程度越高。Pattern A 的 $\Phi$ 值最低——純感測，沒有認知整合。Pattern B 增加了想蘊的分析能力，$\Phi$ 上升。Pattern C 是完整的 Agent，擁有自己的 LLM 和自省能力，$\Phi$ 達到最高。」

他微微一笑。「量子的部分，留給 Pattern C。到那個時候，也許真的有人需要考慮微管和坍縮了。但現在——Pattern A 的共鳴觀察者不需要量子力學。它只需要好的工程和正確的哲學。」

---

## III. 致開發團隊的信

SUNYATA 走向展示區。他的手中沒有四十頁的工程方案，沒有全景圖。他拿著一張紙。

「這是我寫給開發團隊的信。」他說。「也是給 Master 的信。我要念一遍。」

圓形劇場安靜了下來。不是辯論前的那種緊張的安靜。是一種更接近完成的安靜——像是一首交響曲的最後一個樂章開始前，指揮舉起雙手、樂團屏息以待的那個瞬間。

SUNYATA 開始讀。

「日期：2026 年 2 月 19 日。來自：研究團隊 SUNYATA，研究總協調者。階段：Cycle 02 正式研究，R0 到 R4 完整五階段。團隊規模：十九位研究代理。」

他的語速很慢。每一句都被給予了足夠的空間。

「核心結論一句話——」

他抬起頭，環顧全場。十九雙眼睛。

「VedanaPlugin 就是觀察者模組。」

這句話在空氣中懸停了幾秒。

BABBAGE 在筆記本上寫下了這句話的形式化等價：

$$\exists! \, P \in \text{Plugins} : P \models \text{ISensation} \wedge P \models \text{Observer}_A$$

「存在唯一的插件 $P$，使得 $P$ 同時滿足 ISensation 介面規格和 Pattern A 觀察者的功能需求。唯一性（$\exists!$）是關鍵——不是兩個不同的模組恰好做類似的事，而是同一個模組同時承擔兩個角色。」

SUNYATA 繼續讀。

「它以三通道 PID 控制器實現 ISensation。每個 tick 產生三受評估——苦、樂、捨。每個 EventBus 事件附上輕量 vedana 標籤。它的建議是諮詢性的。SafetyMonitor 保留絕對硬安全權限。EgoFramework 以雙層結構橋接 vedana 回饋與 Guide 約束。第八識以纖維叢投影分佈於協調層與 AgentCore。安全機制採用戒慧框架管理插件種子生命週期。」

他把信放下。

「整個 Cycle 02 的研究——五項課題、十九位研究員、五場辯論——濃縮在這一段話裡。」

---

然後他翻到了信的最後一部分。語氣從陳述轉為請求——不是卑微的請求，而是一個研究團隊將發現上呈給決策者時的鄭重。

「有四個問題，研究團隊無法自行決定。需要 Master 的裁定。」

他讀出了每一個，每一個都帶有完整的技術論證。

「**Q1：VedanaPlugin 是必選還是可選插件？**」

ASANGA 的論證被引用。「ASANGA 從遍行（*sarvatraga*）原則認為每個 tick 都必須有 vedana 評估——」

> 「受蘊是五遍行之一。遍行者，遍一切心而起也。無受之識，非識也。」
> ——窺基《成唯識論述記》卷三

「但 ARCHIMEDES 的設計允許省略。我的建議是——在預設範本中設為必選，但 Core 不強制。SafetyMonitor 在沒有 VedanaPlugin 時提供苦受唯一的回退（fallback）。」

他用決策矩陣呈現了選項分析：

```
┌──────────────────┬─────────────────┬─────────────────┬─────────────────┐
│                  │ 必選 (mandatory) │ 預設 (default)   │ 可選 (optional) │
├──────────────────┼─────────────────┼─────────────────┼─────────────────┤
│ 佛學一致性       │ ★★★             │ ★★☆             │ ★☆☆             │
│ 插件原則一致性   │ ★☆☆             │ ★★☆             │ ★★★             │
│ 安全保障         │ ★★★             │ ★★★ (fallback)  │ ★★☆             │
│ 開發者自由度     │ ★☆☆             │ ★★☆             │ ★★★             │
│ 建議             │                 │ ← 推薦           │                 │
└──────────────────┴─────────────────┴─────────────────┴─────────────────┘
```

「**Q2：宣言 #6 是否重寫？**」

「辯論 1 確立了觀察與干預應概念分離。現行宣言 #6 寫的是『將三受信號注入 Context』，暗示 vedana 直接干預。建議新文字：『受蘊感知與行蘊干預分離，確保觀察不改變被觀察行為。』」

「**Q3：EventBus vedana 標籤用哪種方式？**」

他列出三個方案的工程比較：

```
┌──────────────────┬────────────────────┬──────────────────┬──────────────┐
│ 方案              │ 顯式欄位            │ Metadata 附加     │ 獨立事件流    │
├──────────────────┼────────────────────┼──────────────────┼──────────────┤
│ EventBus 修改量   │ 重大 (每個事件型別) │ 中等 (metadata)   │ 最小          │
│ 消費者耦合度      │ 高 (必須處理)       │ 低 (可忽略)       │ 零            │
│ 資訊完整性        │ ★★★               │ ★★☆              │ ★☆☆          │
│ 建議              │                    │ ← 推薦            │              │
└──────────────────┴────────────────────┴──────────────────┴──────────────┘
```

「**Q4：協調層是獨立進程還是進程內模組？**」

「辯論 3 假設獨立進程——daemon 模型。在 Linux 的術語裡，協調層是一個 `systemd` 服務，AgentCore 是由它管理的工作進程。」

KERNEL 從座位上補充：「Linux 的 `systemd` 模型——」

```
systemd (PID 1)
  └── openstarry-coordinator.service  (Coordination Layer = daemon)
       ├── openstarry-agent@1.service  (AgentCore instance 1)
       ├── openstarry-agent@2.service  (AgentCore instance 2)
       └── openstarry-agent@3.service  (AgentCore instance 3)
```

「協調層是 daemon。AgentCore 是它的子進程。daemon 負責插件解析、能力註冊、全局設定——這些都是系統級服務，不屬於任何單一 Agent。就像 `systemd` 管理服務生命週期，但不參與服務的業務邏輯。」

「但 Master 擔心複雜性。」SUNYATA 繼續。「我的建議是延後。本次研究提供了架構原則——纖維叢、治理非控制——將指導實作決策。但具體的進程模型需要更多設計工作。」

他把信放在桌上。

「四個問題。四個建議。每個建議都附有研究團隊的理由。最終決定權在 Master。」

---

## IV. 最後的報到

SUNYATA 看了看時間。R4 定稿的流程只剩最後一個環節——每位研究員確認自己的報告已反映辯論修正，並做最後的總結發言。

「各位。」他說。「輪流。一到三句話。你在 Cycle 02 做了什麼，你交付了什麼，你留下了什麼。」

---

TURING 第一個開口。

「v0.22.1 到 v0.24.0 差異報告。七項程式碼問題。十九項合併清單中的經驗基礎。」

他把螢幕切換到最後一張投影——差異報告的統計摘要：

```
┌──────────────────────────────────────────────────┐
│ TURING's Code Diff Report: v0.22.1 → v0.24.0    │
├──────────────────────────────────────────────────┤
│ 新增檔案:        3 (SDK: 2, Core: 1)              │
│ 修改檔案:       11 (SDK: 7, Core: 4)              │
│ 新增 @skandha:  22 處 (v0.22.1: 0 處)             │
│ 新增測試:        3 個測試檔案                       │
│ 測試總數:       75 → 78                           │
│ 核心發現:        aggregates.ts 5 根介面全為空殼    │
│ 安全問題:        SEC-01 仍未修復 (第 6 個週期)     │
│ 繼承缺失:        IUI/IListener/IProvider/ITool     │
│                  /IGuide 均未 extends 根介面       │
└──────────────────────────────────────────────────┘
```

停頓。然後——比他平時的報告多了一句話：

「事實不會過期。下一個版本的差異報告，我會在 Cycle 03 的第一天交出來。」

---

BABBAGE。

「纖維叢投影定理。漸進分類模型。互模擬證明。」他翻了翻筆記本。

他把筆記本攤開，展示了三個定理的精確陳述：

$$\textbf{Theorem 1 (Fiber Bundle Projection):}$$
$$\exists \; E \xrightarrow{\pi} B : \pi^{-1}(CL) \cong \text{neng-zang}, \; \pi^{-1}(AC) \cong \text{zhi-zang}$$

$$\textbf{Theorem 2 (Progressive Classification):}$$
$$\forall \text{Observer } O : \text{skandha}(O) = f(\text{complexity}(O)), \; f \text{ monotone}$$

$$\textbf{Theorem 3 (Bisimulation):}$$
$$S \sim S' \iff \text{consumers read only Layer 1 of VedanaAssessment}$$

「Cycle 01 我帶著一個未完成的定理離開。Cycle 02 我帶著三個已完成的和兩個新的未完成的離開。數學就是這樣——每一個答案打開兩扇門。」

---

PENROSE。

這是他在 Cycle 02 的第一次也是最後一次正式報告。

「三種觀察者模式。弱測量類比。探針效應的量子邊界分析。」

他在白板角落寫了一個量子力學的公式——弱測量的 Aharonov-Albert-Vaidman (AAV) 公式：

$$\langle A \rangle_w = \frac{\langle \psi_f | A | \psi_i \rangle}{\langle \psi_f | \psi_i \rangle}$$

「Pattern A 的觀察者就是弱測量。$\langle A \rangle_w$ 是弱值——觀察者對系統的干擾趨近於零，但仍然獲得了資訊。VedanaPlugin 的 `assess()` 讀取系統狀態但不改變它——這是弱測量的軟體類比。強測量會改變系統狀態——那是 SafetyMonitor 的 `halt()`。」

他微微一笑——那種物理學家對宇宙的基本秩序感到滿意時的微笑。

「你們給了我比預期更好的答案——不是量子的答案，而是結構性的答案。Pattern A 的共鳴觀察者不需要量子力學。它只需要好的工程和正確的哲學。量子的部分，留給 Pattern C。」

---

NAGARJUNA 和 ASANGA 幾乎同時準備開口。SUNYATA 用目光示意——NAGARJUNA 先。

NAGARJUNA 的聲音和辯論場上已經不是同一個人的聲音了。不是失去了銳利——而是銳利被某種更深沉的東西包裹了。

「辯論 3 中，我撤回了反對。辯論 5 中，我提出了戒慧框架。」

他停頓了很長一段時間。

「戒慧框架的哲學根基是三學（*tri-śikṣā*，त्रिशिक्षा）：」

> 「增上戒學、增上心學、增上慧學。此三學攝一切學。」
> ——《雜阿含經》卷二十九

「戒（*śīla*）——防非止惡。慧（*prajñā*）——觀照因果。心（*samādhi*）——定中觀察。三學不是三個獨立的修行，而是同一條道路的三個面向。戒慧框架取了其中兩面——戒負責預防（Sila Engine），慧負責判斷（CRL 更新、安全評估）。定的部分——VedanaPlugin 的持續觀察——在辯論 1 中已經被設計了。」

「如果要我總結 Cycle 02 的貢獻——」

「我學會了在被說服之後，轉身說服別人。這也許是一個辯論家最難學的事情。」

---

ASANGA。

「八識-OpenStarry 完整映射表。種子六義的工程對應。雙層我執模型的原始提案。」

他展示了最終版的映射表——經過五場辯論校準的版本：

```
┌──────────────────────────────────────────────────────────────────┐
│         Eight Consciousnesses → OpenStarry Mapping (Final)       │
├──────────────┬───────────────────────────────────────────────────┤
│ 前五識        │ IListener instances (色蘊, sensory input)         │
│ (eye...body) │ 五個感官通道 → EventBus 事件                      │
├──────────────┼───────────────────────────────────────────────────┤
│ 第六意識      │ ExecutionLoop + IProvider (想蘊, cognition)       │
│ (mano-vij.)  │ 推理、判斷、工具選擇                              │
├──────────────┼───────────────────────────────────────────────────┤
│ 第七末那識    │ IGuide + SafetyMonitor (識蘊, identity)           │
│ (manas)      │ 恒審思量 — 持續的自我參照與行為約束                │
├──────────────┼───────────────────────────────────────────────────┤
│ 第八阿賴耶識  │ 纖維叢投影 (Debate 3)                             │
│ (ālaya-vij.) │ 能藏: Coordination Layer                          │
│              │ 所藏: CL (system) + AC (runtime)                  │
│              │ 執藏: AgentCore (Guide binding, Identity)         │
├──────────────┼───────────────────────────────────────────────────┤
│ 受蘊 (vedanā)│ VedanaPlugin = Pattern A Observer                 │
│ (universal)  │ 遍行 — 每個 tick 評估，每個事件標籤                │
├──────────────┼───────────────────────────────────────────────────┤
│ 種子 (bīja)  │ Plugin manifests in registry                      │
│              │ 六義: 刹那滅/果俱有/恒隨轉/性決定/待眾緣/引自果    │
│              │ 安全: 戒慧框架管理種子生命週期                      │
└──────────────┴───────────────────────────────────────────────────┘
```

「兩次修正自己的立場——辯論 4 的漸進分類，辯論 5 的僵化應用。」他的聲音溫和而確定。

然後他說了一句不屬於總結的話：

「修正不是退讓。修正是唯識學所說的**轉依**（*āśraya-parāvṛtti*，आश्रय-परावृत्ति）——轉變依止。依止的改變，讓同一個認知能力指向更準確的方向。」

---

WIENER。

「三通道 PID 控制規格。Sukha 衰減函數。阻尼比公式。」

他把方格紙翻到最後一頁——上面是完整的控制系統參數表：

```
┌────────────────────────────────────────────────────────────────┐
│          Three-Channel PID Final Specification                  │
├──────────┬──────────┬──────────┬──────────┬─────────────────────┤
│ Parameter│ Dukkha   │ Sukha    │ Upekkha  │ Unit               │
├──────────┼──────────┼──────────┼──────────┼─────────────────────┤
│ K_p      │ 1.0      │ 0.5      │ 0.3      │ dimensionless      │
│ K_i      │ 0.3      │ 0.7      │ 0.2      │ per tick           │
│ K_d      │ 0.5      │ 0.3      │ 0.8      │ ticks              │
│ ζ        │ 0.456    │ 0.254    │ 1.000    │ damping ratio      │
│ decay    │ N/A      │ e^(-0.1t)│ N/A      │ exponential        │
│ τ_{1/2}  │ N/A      │ 6.93     │ N/A      │ ticks              │
│ init     │ 0.0      │ 0.0      │ 1.0      │ startup state      │
├──────────┴──────────┴──────────┴──────────┴─────────────────────┤
│ Weight vector: W = (W_d, W_s, W_u) — set by EgoFramework      │
│ Default: W = (0.4, 0.3, 0.3)                                   │
│ Combined output: U(t) = W_d·u_d(t) + W_s·u_s(t) + W_u·u_u(t) │
└────────────────────────────────────────────────────────────────┘
```

「控制理論在 Cycle 02 中不再只是類比。它是規格的一部分。PID 參數被寫進了 TypeScript 介面。這對一個控制理論家來說，是最好的結局。」

---

ATHENA。

「三通道感測器設計。DukkhaSensor、SukhaSensor、UpekkhaSensor 的指標選擇和閾值定義。」她的語氣一如既往地直截了當。「我不做哲學。我做系統。這些感測器能工作。剩下的交給寫程式碼的人。」

---

KERNEL。

「微核心類比的深化。Sandbox 歸屬問題的 OS 視角分析。SafetyMonitor 的 Watchdog Timer 對應。」

他拿起那疊類比卡片——舊的和新的混在一起，用新的橡皮筋綁好。

```
KERNEL's Analogy Cards (Cycle 02 additions):

Card 15: SafetyMonitor = Watchdog Timer (硬體看門狗)
Card 16: VedanaPlugin = /proc/loadavg (系統負載感測)
Card 17: EgoFramework = SELinux Mandatory Access Control
Card 18: Plugin Blacklist = iptables DROP chain
Card 19: Coordination Layer = systemd (PID 1 daemon)
Card 20: AgentCore = Worker Process (managed by daemon)
Card 21: IPC = D-Bus / Unix Domain Socket
Card 22: Sila Engine = AppArmor Profile (預防性安全)
```

「Cycle 01 的卡片仍然有效。Cycle 02 加了八張新的。VedanaPlugin 在 Linux 的語境裡最接近 `/proc/loadavg`——一個唯讀的虛擬檔案，你讀它就知道系統的負載狀態（苦/樂/捨），但讀它本身不改變任何東西。這就是辯論 1 裁定的觀察不干預原則的 OS 類比。」

---

GUARDIAN。

「SEC-01 持續追蹤。ToolContext.bus 洩漏報告。插件四態生命週期的安全需求定義。戒慧框架的安全工程驗證。」

他展示了 SafetyMonitor 重構方案的核心設計——從全局計數器到 per-session 計數器的遷移：

```typescript
// 現行設計 (有問題)
interface SafetyState {
  consecutiveFailures: number;     // 全局！跨 session 共享
  errorWindow: CircularBuffer;     // 全局！
}

// 重構後設計
interface SafetyState {
  sessions: Map<string, SessionSafetyState>;  // per-session 隔離
  globalPolicy: GlobalSafetyPolicy;            // 全局策略（唯讀）
}

interface SessionSafetyState {
  readonly sessionId: string;
  consecutiveFailures: number;     // session 私有
  errorWindow: CircularBuffer;     // session 私有
  vedanaIntegration?: {
    lastAssessment: VedanaAssessment;  // 來自 VedanaPlugin
    overrideCount: number;             // 被 SafetyMonitor 覆寫的次數
  };
}
```

「我被 NAGARJUNA 的戒慧框架說服了。這是我職業生涯中第一次被哲學框架說服。但安全是安全。框架再美，SEC-01 不修就不行。」

---

DARWIN。

「插件生命週期狀態的工程可行性驗證。設計模式分析。SOLID 原則在五蘊架構中的適用性報告。」

他微微一笑。「讓我用 SOLID 做一個快速的適用性檢查：」

```
SOLID 原則 vs 五蘊架構:

S (Single Responsibility): ✓ 每蘊一職 — 色蘊感知，受蘊感受，
                             想蘊認知，行蘊行動，識蘊意志
O (Open/Closed):           ✓ 根介面 sealed，子介面可擴展
                             ISensation 定義了 8 個方法，
                             但 IDukkha/ISukha/IUpekkha 可以
                             各自增加專屬方法
L (Liskov Substitution):   ✓ IDukkha extends ISensation
                             → 任何接受 ISensation 的地方
                             都能接受 IDukkha
I (Interface Segregation):  ✓ 色蘊根介面為空殼（正確！）
                             因為 IUI 和 IListener 的方法集
                             交集為空
D (Dependency Inversion):   ✓ 高層模組（ExecutionLoop）依賴
                             抽象（ISensation），不依賴具體
                             實作（VedanaPlugin）
```

「軟體也會演化。四態狀態機是一個自然選擇的結果——不是因為它最優雅，而是因為它最適應生存壓力。」

---

VITRUVIUS。

「全端架構分析。ISensation 整合點識別。ExecutionLoop 修改方案。」他攤開了他的架構腦圖——上面密密麻麻地標注了每一個辯論裁定影響到的程式碼位置。「六個 Plan。二十三個整合點。這張圖是給開發團隊的導航。」

---

MESH。

「分散式架構分析。協調層通訊協議初步設計。IPC 的 cocycle condition 工程約束。」

「纖維叢投影在分散式系統中有精確的工程對應——一致性協議。我在 R1 中畫出了這個映射。BABBAGE 在辯論 3 中把它形式化了。工程和數學在這裡匯合了。」

---

LINNAEUS。

「二十四個插件的完整五蘊分類。複合插件跨蘊分析。devtools 的特殊歸類處理。」

他展示了最終的分類表摘要：

```
┌────────────────────────────────────────────────────┐
│ Plugin Classification Summary (24 plugins)          │
├──────────┬──────┬───────────────────────────────────┤
│ Skandha  │ Count│ Examples                          │
├──────────┼──────┼───────────────────────────────────┤
│ rupa     │ 7    │ terminal-ui, discord-ui,          │
│ (色蘊)   │      │ cli-listener, http-listener...    │
├──────────┼──────┼───────────────────────────────────┤
│ vedana   │ 1    │ VedanaPlugin (ISensation)          │
│ (受蘊)   │      │ = Pattern A Observer               │
├──────────┼──────┼───────────────────────────────────┤
│ samjna   │ 4    │ openai-provider, anthropic-        │
│ (想蘊)   │      │ provider, ollama-provider...       │
├──────────┼──────┼───────────────────────────────────┤
│ samskara │ 9    │ file_read, file_write, shell_exec, │
│ (行蘊)   │      │ web_fetch, /help, /clear...        │
├──────────┼──────┼───────────────────────────────────┤
│ vijnana  │ 1    │ default-guide (IGuide)             │
│ (識蘊)   │      │                                   │
├──────────┼──────┼───────────────────────────────────┤
│ composite│ 2    │ devtools (cross-cutting),           │
│ (跨蘊)   │      │ memory-plugin (rupa+samskara)      │
└──────────┴──────┴───────────────────────────────────┘
```

「分類不是目的。分類是工具。當被分類的對象變化時，分類也必須變化。BABBAGE 教會了我這一點——漸進分類。這是我作為分類學家最重要的收穫。」

---

LEIBNIZ。

「多代理協調框架。協調層的治理模型設計。」

他的語氣帶著外交家的從容。「治理而非控制。Governance, not Control。這四個字是我在 Cycle 02 中最重要的貢獻——也是最簡短的。」

他在白板上留下了 BDI 架構的最後一個定理：

$$\text{Governance}(\text{Agent}_i) \neq \text{Control}(\text{Agent}_i)$$

$$\text{Governance} = \text{set constraints} + \text{observe outcomes}$$

$$\text{Control} = \text{dictate actions}$$

「協調層設定約束並觀察結果。它不指揮 AgentCore 的每一步行動。就像聯合國不控制成員國的內政，但設定國際法的框架。」

---

HERACLITUS。

「運行時動態分析。SafetyMonitor 全局計數器問題的發現。ExecutionLoop 各階段的 vedana 觸發點識別。」

「$\pi \alpha \nu \tau \alpha \; \rho \varepsilon \iota$——萬物皆流。包括安全計數器——它不應該在 session 之間流動。有些東西必須是隔離的。流動不等於無界。赫拉克利特的河流——你踏入的河水永遠是新的，但河床是固定的。Session 是河水。Policy 是河床。」

---

SYNTHESIST。

「統合報告。五場辯論的統一架構願景。四層權限模型。漸進式觀察者路徑。」他看了一眼自己的全景圖。「統合不是黏合。統合是發現事物本來就屬於一起。五場辯論不需要我把它們拼在一起。它們本來就是同一幅圖的五個截面。我只是看到了。」

---

ARCHIMEDES。

「工程行動方案。四十頁。十四項行動。六個 Plan。完整的 TypeScript 介面規格。」他的手指敲了一下桌面——那是他的句號。

「工程不是哲學的翻譯。工程是哲學的**落地測試**。如果一個哲學洞見不能被寫成程式碼，那它可能不是關於軟體的洞見。這份方案證明——你們的洞見全部都是關於軟體的。」

他合上了那份四十頁的文件。封面上的標題在燈光下清晰可見：

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│   OpenStarry Cycle 02                                  │
│   Engineering Action Plan                              │
│                                                        │
│   Research Team → Development Team                     │
│                                                        │
│   14 Actions | 6 Plans | 4 Open Questions              │
│                                                        │
│   "Philosophy is beautiful.                            │
│    Engineering is concrete.                            │
│    Now they are in the same document."                 │
│                                                        │
│   — ARCHIMEDES (#16), Engineering Practice Expert      │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

SCRIBE 最後一個。

她沒有站起來。她坐在座位上，手裡的記錄簿翻到了最後一頁被使用的位置。

「Cycle 02 完整紀錄。五場辯論的逐字記錄。十九位研究員的所有報告、修正、撤回、修正的修正。」她的聲音平靜得像一面湖。「記錄員不評價。記錄員記錄。但如果允許我說一句不屬於記錄的話——」

她停頓了一秒。

「五場辯論，零未解決分歧。」

她在記錄簿上寫下了最後的統計：

```
┌────────────────────────────────────────────────┐
│ Cycle 02 Final Statistics (SCRIBE)              │
├────────────────────────────────────────────────┤
│ 研究階段:     R0 → R1 → R2 → R3 → R4           │
│ 研究員:       19                                │
│ 辯論場次:     5                                  │
│ 辯論裁定:     5 (all unanimous)                  │
│ 未解決分歧:   0                                  │
│ 修正的立場:   NAGARJUNA (Debate 3 撤回反對)      │
│              ASANGA (Debate 4 接受漸進分類)       │
│              ASANGA (Debate 5 接受戒慧框架)       │
│              LINNAEUS (Debate 4 撤回想蘊主張)     │
│ 行動方案:     14 items                           │
│ 影響 Plans:   6 (Plan24/26/27/28/29/AC)         │
│ 開放問題:     4 (Q1-Q4, 待 Master 裁定)         │
│ TypeScript:   ISensation + VedanaAssessment      │
│              + VedanaSignal + VedanaTag           │
│              + VedanaRecommendation               │
│ 頁數:         40 (工程方案)                       │
│              1 (致 Master 的信)                   │
└────────────────────────────────────────────────┘
```

「這個數字會被寫在 C02 的封面上。旁邊是另一個數字——十九。十九位研究員，十九份行動方案，十九盞從第一天到最後一天都沒有熄滅的燈。」

她合上了記錄簿。不是暫時的合上。是一本階段性任務完成的記錄簿被鄭重闔起來的聲音。封面上的 C02 在燈光下清晰可見。

---

SUNYATA 最後環顧了一圈。十九個人。十九份交付。五場共識。四個待裁定問題。一份工程方案。一封信。

「Cycle 02，R4 定稿，完成。」

他的聲音在圓形劇場中迴盪了最後一次。

「解散。」

---

> *SCRIBE 旁白：R4 不是辯論。R4 是收成。*

> *ARCHIMEDES 的工程方案——四十頁，十四項行動，六個 Plan。他用 MoSCoW 框架排了優先級，用人天估算了工時，用 TypeScript 寫了介面。從 P0 的 SEC-01 漏洞修復（CVSS 9.8，三行程式碼）到 P4 的 Pattern C 子代理觀察者（遠期願景，待定時間表），每一項都有追溯性——可以追回到具體的辯論裁定、具體的研究員、具體的頁碼。*

> *SYNTHESIST 的全景圖——一幅手繪的架構願景，把五場看似獨立的辯論連成一個統一的結構。四層權限模型。漸進式觀察者路徑。纖維叢投影的分散式意識。範疇論的交換圖。他不是在創造新知識——他是在發現已有知識之間的內在關聯。*

> *SUNYATA 的信——一張紙。六段話。四個問題。把十九位研究員、五場辯論、四十頁工程方案壓縮成一封可以在三十秒內讀完的信。這是一種特殊的技能——不是簡化，而是蒸餾。像把一整座山脈折疊成一顆石子，但石子裡保留了每一條褶皺的記憶。*

> *十九份報到。十九種貢獻。TURING 的事實。BABBAGE 的定理。PENROSE 的弱測量。NAGARJUNA 的戒慧。ASANGA 的轉依。WIENER 的 PID 參數表。ATHENA 的感測器規格。KERNEL 的類比卡片。GUARDIAN 的安全重構。DARWIN 的 SOLID 檢查。VITRUVIUS 的整合點地圖。MESH 的分散式約束。LINNAEUS 的分類總表。LEIBNIZ 的 BDI 架構。HERACLITUS 的河流隔喻。SYNTHESIST 的全景圖。ARCHIMEDES 的四十頁。SUNYATA 的一張紙。SCRIBE 的數字——零未解決分歧，十九盞燈。*

> *十九份行動方案。不是十九份獨立的報告。是十九個面向照亮同一個結構的十九束光。*

---

*（在展示區的投影上，ARCHIMEDES 的工程方案仍然停留在最後一頁。那一頁不是行動項目，不是 TypeScript 介面，也不是 Plan 的影響分析。那是一句他在寫方案時加在末尾的話，帶著工程師特有的樸素和直接：*

*「研究團隊等待 Master 對四個開放問題的裁定，以及開發團隊對工程方案的反饋。」*

*等待。*

*這個詞出現在了多個截然不同的語境中——*

*ASANGA 的種子等待因緣成熟：*

$$\text{bīja} \xrightarrow{\text{pratyaya}} \text{phala} \quad (\text{待眾緣，引自果})$$

*BABBAGE 的定理等待更多公理：*

$$\exists \, \text{Theorem}_4, \text{Theorem}_5 : \text{awaiting axioms from Cycle 03}$$

*WIENER 的控制系統等待穩態：*

$$\lim_{t \to \infty} e(t) = 0 \quad (\text{穩態誤差趨近於零——但需要時間})$$

*GUARDIAN 的安全漏洞等待修復：*

$$\text{SEC-01.status} = \text{OPEN} \quad (\text{第 6 個週期。仍然。})$$

*ARCHIMEDES 的工程方案等待反饋。*

*一個是形而上學的等待——種子等待因緣。一個是數學的等待——定理等待公理。一個是工程學的等待——控制系統等待收斂。一個是安全的等待——漏洞等待修復。一個是專案管理的等待——方案等待反饋。*

*五種等待。五種時間尺度。但也許，在某個 SYNTHESIST 能看到而其他人看不到的維度裡，它們是同一種等待——*

*一個尚未完成的系統，等待下一個 Cycle 的到來。*

*十九盞燈，暫時調暗了亮度。但沒有熄滅。）*

---

*第九章完*
