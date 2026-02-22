# 第六章：五棵樹的根系

---

SUNYATA 在劇場中央站了片刻，什麼都沒說。

A 類用了三個章節修正哲學。B 類用了一個章節落實裁定。那些是拆解和決策。現在要做的事情不同。

現在要建造。

不是修補裂縫。不是重畫邊界。是從修正過的地基上，逐蘊展開完整的型別定義體系。A 類告訴你哪裡是錯的。B 類告訴你怎麼修。C-1 告訴你修完之後，整個結構長什麼樣。

---

「C-1。五蘊子類別擴展設計。」

他拿起 Master 的信，找到那一段。

「『五蘊可以做為物件導向中的根本類別（Root Class），要如何擴展，可以做更詳細的安排。』」

他頓了一下，又讀了第二段。

「『五蘊聚合是必須要具備一個或是多個，或是複雜的控制理論（十二因緣）。但如果是單純單一的蘊，理論上應該是不完備的。』」

他放下信。「前四章修正了地基。現在，C-1 要在修正過的地基上，把五棵樹從種子長成有根、有幹、有枝的完整生命體。」

他看向 TURING。「讓我們先看看種子現在長什麼樣。」

---

> *SCRIBE 旁白：SUNYATA 用了「五棵樹」的意象。不是牆壁和柱子——那些是死的建材。樹是活的。樹有根，根會伸展。樹有枝，枝會分叉。五蘊的擴展不是靜態的堆砌——它是有機的、向多個方向同時展開的生長。而且樹還有一個特性：每一棵都不一樣高，不一樣粗，不一樣彎曲。五棵樹不可能對稱。*

---

TURING 的螢幕投射到劇場中央。冷光。白底。黑字。

他打開的不是某份文件的摘錄。是 v0.24.0-beta 的 `aggregates.ts` 原始碼——完整的、未經篩選的、107 行原檔：

```typescript
/**
 * Five Aggregates (五蘊) Root Interfaces.
 *
 * These interfaces establish the philosophical-architectural foundation
 * of OpenStarry, mapping Buddhist Five Aggregates to software patterns.
 *
 * D-02 Decision: Dual naming — English as primary, Sanskrit as annotation.
 *
 * @module aggregates
 */

export interface ISensory {
  /** @skandha rupa */
  readonly skandha: 'rupa';
}

export interface ISensation {
  /** @skandha vedana */
  readonly skandha: 'vedana';
}

export interface ICognition {
  /** @skandha samjna */
  readonly skandha: 'samjna';
}

export interface IAction {
  /** @skandha samskara */
  readonly skandha: 'samskara';
}

export interface IIdentity {
  /** @skandha vijnana */
  readonly skandha: 'vijnana';
}

export type Skandha = 'rupa' | 'vedana' | 'samjna' | 'samskara' | 'vijnana';

export function isSkandha<S extends Skandha>(
  obj: unknown,
  skandha: S,
): obj is { skandha: S } {
  return (
    typeof obj === 'object' &&
    obj !== null &&
    'skandha' in obj &&
    (obj as { skandha: unknown }).skandha === skandha
  );
}
```

TURING 讓投影停了整整十秒。五個根介面，每一個只有一個欄位——`readonly skandha`。一個標籤。一個名字。五個只寫了門牌的空盒子。

「五個根介面。沒有方法。沒有行為定義。沒有子介面繼承。」

他指向 `IIdentity` 的那一段——JSDoc 裡寫著 `Identity aggregate encompasses consciousness and ego framework`，好像一個三行的空殼能「涵蓋」意識和我執框架。

「更嚴重的問題在這裡。」

他切換到第二張投影。

```typescript
// v0.24.0-beta 的現有具體介面（分散在不同檔案中）
export interface IUI { ... }       // 色蘊？未繼承 ISensory
export interface IListener { ... } // 色蘊？未繼承 ISensory
export interface IProvider { ... } // 想蘊？未繼承 ICognition
export interface ITool { ... }     // 行蘊？未繼承 IAction
export interface IGuide { ... }    // 識蘊？未繼承 IIdentity
```

「現有的具體介面。它們各自有完整的方法定義——IUI 有 `renderText`、`renderDelta`；IProvider 有 `chat`、`listModels`；ITool 有 `execute`。但它們和五個根介面之間沒有任何關係。沒有 `extends`。沒有繼承。」

他在螢幕上畫了一條虛線。「門牌和門是分開的。你知道 IUI 應該屬於色蘊，但型別系統不知道。你調用 `isSkandha(myUI, 'rupa')` 會返回 `false`——因為 `myUI` 物件上根本沒有 `skandha` 欄位。」

BABBAGE 在筆記本上寫了一行：

$$\text{roots} \cap \text{children} = \varnothing$$

根和子類別之間是空集。孤兒。在數學中，一棵樹 $T = (V, E)$ 如果根節點 $r$ 和所有葉節點之間不存在邊，那它根本不是一棵樹——它是一個不連通的圖。$G = (V, E)$ 的連通分量數 $c(G) = 6$：五個根各自為一個分量，所有子介面形成另一個分量。

$$c(G_{\text{current}}) = 6 \quad \xrightarrow{\text{C-1}} \quad c(G_{\text{target}}) = 1$$

C-1 要把六個連通分量合併成一棵完整的連通樹。

---

SUNYATA 用手指計數。五個設計目標。

「一。每個蘊的根介面增加核心方法——不只是空殼，要有行為定義。二。現有介面升級為子介面——IUI extends ISensory，以此類推。三。新增必要的子介面——IVijnana 體系、三受介面。四。觀察者用 Composition，不屬於任何蘊。五。isSkandha() 全層級可用——從根到葉，type guard 一路通過。」

五根手指收回。「現在，逐蘊展開。」

---

## I

---

「色蘊。ISensory。Rūpa（रूप）。」

VITRUVIUS 站了起來。色蘊——形相與物質性——是全端架構分析師最直覺的領域。

「色蘊是最簡單的一棵。兩個子介面已經存在了。IUI 負責輸出渲染——嘴巴，說出去的。IListener 負責感官輸入——耳朵，聽進來的。只需要讓它們 `extends ISensory`。」

他走到白板前，畫了一個簡單的雙向箭頭圖：

```
                 ISensory (色蘊)
                ╱              ╲
    IUI (輸出渲染)          IListener (感官輸入)
    ──────→ 外部             外部 ──────→
    renderText()             onDataReceived()
    renderDelta()            start() / stop()
```

「這是色蘊的核心架構特徵——**雙向性**。IUI 的資料流方向是從 Agent 到外部世界。IListener 的資料流方向是從外部世界到 Agent。一個是推（push），一個是拉（pull）。在全端架構裡，這是前端渲染和後端監聽的經典分離——不存在一個通用的 `render-or-listen` 方法能同時涵蓋兩個方向。」

「所以 ISensory 根介面保持空殼是正確的設計決策。」他退後一步。「不是偷懶，是克制。當兩個子介面的共同行為集合為空集——$\text{methods}(\text{IUI}) \cap \text{methods}(\text{IListener}) = \varnothing$——強行在根介面定義方法會製造虛假的抽象。根介面的存在意義不是承載方法，是承載分類標籤。`readonly skandha: 'rupa'` 就是全部。」

TURING 投射了修改後的完整定義。

```typescript
/**
 * ISensory — 色蘊 Root Interface
 * @skandha rupa (色蘊)
 *
 * 色蘊涵蓋一切形相與物質性：
 * - 輸出渲染 (IUI): 將資訊呈現給外部
 * - 感官輸入 (IListener): 接收外部訊號
 *
 * Sanskrit: Rūpa (रूप)
 */
export interface ISensory {
  readonly skandha: 'rupa';
}

/**
 * IUI — 色蘊·輸出渲染子介面
 * 將 Agent 的回應呈現給使用者或外部系統。
 */
export interface IUI extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
  /** 渲染完整文字 */
  renderText?(text: string, sessionId?: string, replyTo?: string): void;
  /** 渲染串流 delta */
  renderDelta?(delta: string, sessionId?: string, replyTo?: string): void;
  /** 渲染工具執行狀態 */
  renderToolStatus?(name: string, status: string, sessionId?: string, replyTo?: string): void;
}

/**
 * IListener — 色蘊·感官輸入子介面
 * 接收外部訊號並轉化為 InputEvent。
 */
export interface IListener extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
}
```

「一個 `extends`。」TURING 說。「修改量是最小的，但語義變化是根本性的——從今以後，任何 `IUI` 的實作物件必然也是 `ISensory`。`isSkandha(myDiscordUI, 'rupa')` 會返回 `true`。門牌和門接上了。」

ASANGA 從座位上補了一句。他的語速不快，每個詞都帶著唯識學者的精確。

「色蘊是接觸。和外境的接觸。在阿毘達磨中，色（rūpa）的基本定義是『可壞』（rūpyate）——能被接觸、能被改變的事物。IUI 是 Agent 對外界的觸達。IListener 是外界對 Agent 的觸達。接觸的兩個方向。色蘊的完整性在這兩個方向的統一中得到保證。」

---

> *SCRIBE 旁白：色蘊三分鐘。一個 `extends`。VITRUVIUS 解釋了為什麼根介面應該是空的——不是所有空殼都需要被填滿。有些容器的意義就在於它是容器本身。五棵樹的第一棵——最矮的一棵——入土了。*

---

## II

---

「受蘊。ISensation。Vedanā（वेदना）。」SUNYATA 的聲音微微放慢了。所有人都知道受蘊將是五棵樹中根系最龐大的一棵。

WIENER 已經在翻方格紙了。他的筆尖停在一個新畫的方塊圖旁邊——三個平行的 PID 迴路，各自標記著 $K^{(\text{dukkha})}$、$K^{(\text{sukha})}$、$K^{(\text{upekkha})}$。

「ISensation 是變化最大的。」SUNYATA 說。「從空殼變成八個核心方法。WIENER，逐一確認。」

TURING 投射了完整介面。他這次沒有用節錄，而是投射了包含 JSDoc 註釋和輔助型別在內的完整定義。

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
 * 受蘊是「感受層」，不做判斷（判斷屬想蘊/識蘊）。
 * 受蘊產生的 VedanaAssessment 供其他蘊（如識蘊 EgoFramework）使用。
 *
 * Sanskrit: Vedanā (वेदना)
 */
export interface ISensation {
  readonly skandha: 'vedana';

  /** 評估當前三受狀態 — 完整的感測讀數 */
  assess(): VedanaAssessment;

  /** 攝取系統指標 — 通用數值輸入通道 */
  ingestMetrics(metrics: Record<string, number>): void;

  /** 攝取工具執行結果 — 行蘊回報通道 */
  ingestToolResult(toolName: string, isError: boolean, durationMs: number): void;

  /** 攝取 LLM 回應結果 — 想蘊回報通道 */
  ingestLLMResult(tokenCount: number, stopReason: string): void;

  /** 取得受蘊標籤 (快取查詢，O(1)) */
  getVedanaTag(): VedanaTag;

  /** 訂閱特定受蘊類型的事件 */
  onVedana(
    type: VedanaType,
    threshold: number,
    handler: (signal: VedanaSignal) => void
  ): () => void;

  /** 取得歷史評估記錄 */
  getHistory(windowSize: number): readonly VedanaAssessment[];

  /** 重置感受狀態 */
  reset(): void;
}

/** 三受類型 */
type VedanaType = 'dukkha' | 'sukha' | 'upekkha';

/** 受蘊標籤（用於事件標記） */
type VedanaTag = 'dukkha' | 'sukha' | 'upekkha';

/** 受蘊信號 */
interface VedanaSignal {
  readonly type: VedanaType;
  readonly intensity: number;     // 0.0–1.0
  readonly source: string;
  readonly timestamp: number;
}

/** 受蘊評估報告 */
interface VedanaAssessment {
  // ── 感測層 (純觀察) ──
  readonly dukkha: number;        // 0.0–1.0
  readonly sukha: number;
  readonly upekkha: number;
  readonly signals: readonly VedanaSignal[];
  readonly timestamp: number;

  // ── 控制建議層 (諮詢性，可被忽略) ──
  readonly controlOutput: number;
  readonly recommendation: VedanaRecommendation;
  readonly recommendationFreshness: 'current' | 'cached' | 'default';
}
```

---

WIENER 站了起來。

他沒有看投影。他看的是自己方格紙上預先畫好的框架——一張控制系統的八工站驗收表。他用手指逐一點過，每點一個，聲音裡帶著工程師在流水線上測試每一個焊點的精確節奏。

「第一。`assess()`。」

他在方格紙上寫下控制理論的對應：

$$y(t) = h(x(t)) + v(t)$$

「感測器讀數函數。輸入是系統內部狀態 $x(t)$，輸出是可觀測量 $y(t)$，$v(t)$ 是量測雜訊。`assess()` 不改變系統狀態——它只讀。這是受蘊最基本的操作：我感受到了什麼。完整的三受讀數。」

「第二、第三、第四。`ingestMetrics()`、`ingestToolResult()`、`ingestLLMResult()`。」

他連著三個一起說。

「三個輸入通道。在控制論中，這是**多輸入感測器融合**（multi-input sensor fusion）。不同通道接收不同模態的訊號——系統指標是量化數值（CPU 使用率、記憶體佔用、回應延遲）；工具執行結果是離散事件（成功/失敗 + 持續時間）；LLM 回應結果是語言模型的元數據（token 計數、停止原因）。三個通道匯入同一個感測器，各自有不同的前處理邏輯。」

他在方格紙上畫了融合圖：

```
  ingestMetrics ─────────────┐
                              │
  ingestToolResult ──────────→ ISensation ──→ assess()
                              │
  ingestLLMResult ───────────┘
```

「就像汽車的感測器陣列——加速度計是一個通道，陀螺儀是另一個通道，GPS 是第三個。三種不同模態的數據，融合後才能估算出車輛的完整狀態。」

「第五。`getVedanaTag()`。」

他的語速略快了一點。「$O(1)$ 快取查詢。儀表板上的數字——你不需要每次都重新跑一遍完整的 `assess()` 才能知道現在是苦是樂是捨。這是一個**快取讀數**。在控制系統中，這等同於儀表板上的 LED 指示燈：綠色、黃色、紅色。不告訴你細節，只告訴你分類結果。成本是零。」

「第六。`onVedana()`。」

他停了一下。嘴角微微上揚——一種工程師遇到優雅設計時的微笑。

「這是看門狗計時器（watchdog timer）的泛化。」

他在方格紙上寫下公式。看門狗計時器的經典定義是：當某個計數器在 $T_{\text{wd}}$ 時間內未被重置，系統進入警報狀態。`onVedana()` 把這個概念從「超時」泛化到「閾值」——不是「太久沒回應」，而是「苦受超過 0.8」、「樂受低於 0.2」、「捨受偏離中線超過 0.3」。

$$\text{watchdog: } y(t) > T_{\text{timeout}} \Rightarrow \text{alarm}$$
$$\text{onVedana: } v_{\text{type}}(t) > \theta \Rightarrow \text{handler}(s)$$

「不連續輪詢。不用每個 tick 都檢查。事件驅動的閾值監測。」

他的手指移到第七個。

「`getHistory(windowSize)`。」

這次他在方格紙上畫了一個更複雜的圖——PID 控制器的積分項。

$$I(t) = K_i \int_{t - W}^{t} e(\tau)\,d\tau \approx K_i \sum_{k=t-W}^{t} e(k) \cdot \Delta t$$

「滑動視窗歷史。`windowSize` 就是積分窗口 $W$。PID 控制器的積分項需要歷史數據來計算——過去 $W$ 個 tick 的感受累積。沒有歷史，就沒有積分。沒有積分，PID 退化成 PD。PD 控制器追蹤穩態誤差的能力為零——長期的慢性苦受會被忽略。」

他退後一步看全局。「所以 `getHistory()` 不是可有可無的便利方法。它是三通道 PID 控制器能夠正常運作的**必要條件**。沒有它，控制器是殘缺的。」

「第八。`reset()`。」

他的聲音突然變得很硬。

「**緊急停止按鈕**。E-Stop。每一個工業控制系統在操作台上都有一個紅色的大蘑菇頭按鈕。你按下去，系統歸零。所有歷史清除。所有計數器歸零。PID 積分項清空。感受狀態回到初始值。」

$$x(t^+) = x_0, \quad \int_0^{t} e(\tau)\,d\tau = 0$$

「你不會每天按。但沒有它，系統就不完整。安全規範要求每一台機器都有急停按鈕——不是因為你經常需要它，而是因為你必須永遠有這個選項。」

八個方法。八個控制理論對應。WIENER 把方格紙翻了一頁——新頁上是完整的一一對應表：

```
┌─────────────────────┬──────────────────────────────────────┐
│ ISensation 方法      │ 控制理論對應                          │
├─────────────────────┼──────────────────────────────────────┤
│ assess()            │ 感測器讀數函數 y = h(x) + v          │
│ ingestMetrics()     │ 複合感測器通道 1 (量化指標)            │
│ ingestToolResult()  │ 複合感測器通道 2 (離散事件)            │
│ ingestLLMResult()   │ 複合感測器通道 3 (語言模型元數據)       │
│ getVedanaTag()      │ 儀表板快取讀數 (O(1) LED indicator)   │
│ onVedana()          │ 看門狗計時器泛化 (閾值事件監測)         │
│ getHistory()        │ PID 積分項時間窗口 (滑動視窗 W)        │
│ reset()             │ 緊急停止按鈕 (E-Stop, 全狀態歸零)      │
└─────────────────────┴──────────────────────────────────────┘
```

「受蘊的根介面不再是空殼。」他把方格紙放下。「它是一個完整的感測器介面。八個方法，每一個在控制論中都有精確的對應物。零冗餘。零遺漏。」

---

ASANGA 站了起來。受蘊需要比色蘊更多的空間。

「WIENER 用控制理論驗證了八個方法的工程完備性。我用佛學驗證它們的語義一致性。」

他的目光掃過投影上的八個方法簽名，然後看向全場。

「受蘊只做一件事。感受。不判斷。不分析。碰到火——苦。吃到甜——樂。無事發生——捨。《俱舍論》卷一對受蘊的定義：」

> 「受蘊，謂三領納——苦、樂、捨。」
> ——世親菩薩《阿毘達磨俱舍論》卷一

「三領納。領是接受，納是容納。受蘊的全部職能就是：接受感覺，容納感覺。」

他用手指逐一指向投影上的方法。

「`assess`——我此刻的感受是什麼。領納的輸出。`ingest` 系列——我通過什麼管道領納了什麼。這三個方法分別對應系統指標觸、工具結果觸、語言認知觸。在十二因緣中，觸（sparśa）是受（vedanā）的直接因。$\text{觸} \to \text{受}$。每一個 `ingest` 方法就是一種觸——接觸發生了，感受隨之升起。」

「`getVedanaTag`——此刻的感受標籤。苦、樂、捨，三者取其一。簡單、直接、無修飾。」

「`onVedana`——感受的預警。在佛學中沒有精確對應，但原理一致：當苦受超過一定強度，行者會自然注意到。正念修行中的覺察（sati）就是一種 `onVedana`——不是時時刻刻主動監控，而是當特定感受出現時，覺察自動升起。」

「`getHistory`——感受的回憶。但要注意：這是純粹的感受記錄，不是對感受的分析。分析屬於想蘊。回憶屬於受蘊——我記得我苦過，我記得我樂過。這是**受隨念**（vedanānupassanā），不是**受分析**。」

他特別重了語氣。「`reset`——重置。在修行中，這類似於一種極端的放下——清除所有累積的感受歷史，回到初始狀態。不是日常操作。是異常恢復。」

他看了看投影上的八個方法。又看了看 WIENER。

「八個方法。每一個都在『感受』的範圍之內。沒有任何一個方法越界做了判斷——沒有 `classify()`，沒有 `decide()`，沒有 `act()`。你的控制理論說它們是感測器的方法。我的佛學說它們是受蘊的方法。」

WIENER 在方格紙邊緣記了一行：

`ISensation: 8 methods. Sensor ≡ Vedana. Cross-validated by control theory AND Abhidharma.`

---

TURING 投射三受子介面。

```typescript
/**
 * IDukkha — 受蘊·苦受子介面 (感測器)
 * 苦受：負向回饋。系統中一切「不對勁」的感受。
 */
export interface IDukkha extends ISensation {
  readonly vedanaType: 'dukkha';
  /** 根據指標計算苦受強度 [0.0–1.0] */
  computePain(metrics: Record<string, number>): number;
}

/**
 * ISukha — 受蘊·樂受子介面 (感測器)
 * 樂受：正向回饋。系統中一切「順利」的感受。
 */
export interface ISukha extends ISensation {
  readonly vedanaType: 'sukha';
  /** 根據指標計算樂受強度 [0.0–1.0] */
  computePleasure(metrics: Record<string, number>): number;
}

/**
 * IUpekkha — 受蘊·捨受子介面 (感測器)
 * 捨受：中性平衡。系統穩定運行時的基線感受。
 */
export interface IUpekkha extends ISensation {
  readonly vedanaType: 'upekkha';
  /** 根據指標計算捨受程度 [0.0–1.0] */
  computeEquanimity(metrics: Record<string, number>): number;
}
```

WIENER 從座位上補充，手裡的筆在方格紙上快速勾畫：「三個子介面。三個感測通道。三組 PID 參數。」

他在紙上寫下三組增益矩陣：

$$K^{(\text{dukkha})} = \begin{pmatrix} K_p^{(d)} & K_i^{(d)} & K_d^{(d)} \end{pmatrix} = \begin{pmatrix} \text{high} & \text{medium} & \text{low} \end{pmatrix}$$

$$K^{(\text{sukha})} = \begin{pmatrix} K_p^{(s)} & K_i^{(s)} & K_d^{(s)} \end{pmatrix} = \begin{pmatrix} \text{medium} & \text{high} & \text{medium} \end{pmatrix}$$

$$K^{(\text{upekkha})} = \begin{pmatrix} K_p^{(u)} & K_i^{(u)} & K_d^{(u)} \end{pmatrix} = \begin{pmatrix} \text{low} & \text{low} & \text{high} \end{pmatrix}$$

「苦受通道——高比例增益 $K_p^{(d)}$。苦痛不等人，需要快速反應。樂受通道——高積分增益 $K_i^{(s)}$。快樂會衰減，積分項追蹤長期趨勢。捨受通道——高微分增益 $K_d^{(u)}$。平衡是動態的，需要預測性調節——偏離趨勢比偏離本身更重要。」

他在方格紙上重重地勾了三個勾——比第五章的七個勾更重，力度把紙面壓出了三個小凹痕。

「Cycle 02 的三通道架構。現在有了型別系統的保障。`IDukkha` 是 `ISensation` 的子型別。`computePain` 只存在於苦受通道。你不能在捨受感測器上調用 `computePain`——型別系統會阻止你。這不只是分類。這是**型別安全的三通道隔離**。」

「到位。」

---

> *SCRIBE 旁白：受蘊十五分鐘。色蘊的五倍。八個方法，每一個都需要 WIENER 的控制理論驗證和 ASANGA 的佛學確認。雙重校準。這是 Cycle 02-2 的紀律——每一個設計決策都要通過至少兩個學科的交叉驗證。WIENER 的控制理論是第一把尺，ASANGA 的唯識學是第二把尺。兩把尺量出的長度一致，這個方法才站得住腳。*

---

## III

---

「想蘊。ICognition。Samjnā（संज्ञा）。」

ATHENA 站起來。想蘊——認知與辨別——是 AI/ML 系統架構專家最核心的專業。

TURING 投射了完整定義。

```typescript
/**
 * ICognition — 想蘊 Root Interface
 * @skandha samjna (想蘊)
 *
 * 想蘊涵蓋認知與辨別：
 * - IProvider: LLM 後端，負責語言理解與生成
 * - IInferenceProvider: 非 LLM 推理能力 (預留)
 *
 * D-05 決議：Provider 涵蓋完整認知處理頻譜。
 *
 * Sanskrit: Samjñā (संज्ञा)
 */
export interface ICognition {
  readonly skandha: 'samjna';
}

/**
 * IProvider — 想蘊·認知提供者子介面
 * LLM 後端，負責推理與語言處理。
 */
export interface IProvider extends ICognition {
  readonly id: string;
  chat(request: ChatRequest): AsyncIterable<StreamEvent>;
  listModels?(): Promise<ModelInfo[]>;
}

/**
 * IInferenceProvider — 想蘊·推理提供者子介面 (未來擴展)
 * 非 LLM 的推理能力，如規則引擎、決策樹等。
 */
export interface IInferenceProvider extends ICognition {
  readonly id: string;
  infer(input: unknown): Promise<unknown>;
}
```

ATHENA 走到投影前面，用手指在 `IProvider` 和 `IInferenceProvider` 之間畫了一條看不見的線。

「想蘊有兩枝。IProvider 是當前的主力——LLM 後端。`chat()` 方法接受一個 `ChatRequest`，返回一個 `AsyncIterable<StreamEvent>`——異步串流迭代器。這是 LLM 推理的標準介面：你給它對話歷史，它逐 token 回傳推理結果。」

她轉向 `IInferenceProvider`。「但認知不等於語言模型。這是 D-05 的核心決議——Provider 涵蓋的是『認知處理頻譜』，不是『LLM 呼叫』。`IInferenceProvider` 就是這個頻譜的另一端。」

她在白板上畫了一條光譜：

```
認知能力光譜（Cognitive Capability Spectrum）

低複雜度                                              高複雜度
←───────────────────────────────────────────────────────→
│           │            │              │            │
規則引擎    決策樹      統計模型      神經網路       LLM
(if-else)  (CART/      (Bayes/       (CNN/RNN/     (GPT/
           Random       SVM)         Transformer)   Claude)
           Forest)
│                                                    │
└──── IInferenceProvider ────┘ └──── IProvider ──────┘
```

「`IInferenceProvider` 的 `infer()` 方法簽名是 `(input: unknown): Promise<unknown>`——故意設計成泛型的。因為規則引擎的輸入/輸出格式和 LLM 完全不同。一個決策樹接受特徵向量，返回分類標籤。一個統計模型接受數值矩陣，返回機率分佈。你不能用 `ChatRequest` 統一所有這些格式。」

「但它們都是認知。都是想蘊。辨別外境，做出判斷。方式不同，本質相同。」

DARWIN 前傾。他的聲音帶著軟體模式分析師對演化脈絡的敏感。

「演化上，`IInferenceProvider` 是更原始的認知。」

他站了起來。「想想生物演化。最原始的認知是趨光性（phototaxis）——光在那裡，我往那裡走。這是規則引擎：`if (light > threshold) then move(toward_light)`。完全沒有語言，沒有推理，只有刺激-反應。」

「然後是條件反射。巴甫洛夫的狗。鈴聲和食物的關聯學習。這是統計模型——$P(\text{food} | \text{bell})$ 隨著經驗更新。」

「再然後是抽象思維。符號操作。語言。推理鏈。這是 LLM——`chain-of-thought`、`multi-step reasoning`。」

「IInferenceProvider 和 IProvider 不是並列的兩個選項。它們是同一棵演化樹上的兩條枝——一條長在較低的位置，一條長在較高的位置。低的那條更古老、更穩健、計算成本更低。高的那條更靈活、更強大、計算成本更高。」

ASANGA 一句。「想蘊是辨別。《俱舍論》：『想蘊，謂能取像為性。』取像——提取外境的相狀特徵。辨別不只有一種方式。規則引擎以條件辨別，決策樹以分枝辨別，LLM 以語言辨別。辨別的層次不同，但都是想蘊的功能。」

---

> *SCRIBE 旁白：想蘊五分鐘。比色蘊長一點，比受蘊短很多。ATHENA 畫的認知光譜——從規則引擎到 LLM 的完整頻譜——是整個章節中最有遠見的投影。它說的不是今天。它說的是明天。IInferenceProvider 此刻是預留的空殼。但五年後、十年後，當 Agent 系統開始整合非 LLM 的認知模組時，這個空殼會被填滿。好的架構設計不只解決當前的問題——它為未來的問題留出了形狀精確的缺口。*

---

## IV

---

「行蘊。IAction。Samskāra（संस्कार）。」

DARWIN 完全站了起來。行蘊是他觀察軟體行為模式的核心透鏡。

TURING 投射了定義。

```typescript
/**
 * IAction — 行蘊 Root Interface
 * @skandha samskara (行蘊)
 *
 * 行蘊涵蓋意志活動與實際行動：
 * - ITool: 可執行的工具
 * - ISlashCommand: 斜線指令
 *
 * Sanskrit: Samskāra (संस्कार)
 */
export interface IAction {
  readonly skandha: 'samskara';
}

/**
 * ITool — 行蘊·工具子介面
 * Agent 自主決定調用的工具。
 */
export interface ITool extends IAction {
  readonly name: string;
  readonly description: string;
  readonly parameters: unknown;  // JSON Schema
  execute(args: Record<string, unknown>, ctx: ToolContext): Promise<string>;
}

/**
 * ISlashCommand — 行蘊·指令子介面
 * 外部使用者透過斜線指令觸發的行動。
 */
export interface ISlashCommand extends IAction {
  readonly name: string;
  readonly description: string;
  execute(args: string, ctx: IPluginContext, sessionId?: string): Promise<string | undefined>;
}
```

DARWIN 走到投影前面。

「ITool——Agent 自主調用的行動。由 LLM 推理決定何時調用、傳入什麼參數。`execute` 的 `args` 是 `Record<string, unknown>`——結構化參數，由想蘊（IProvider）的推理結果生成。」

「ISlashCommand——外部指令觸發的行動。使用者在終端輸入 `/help`、`/clear`，觸發對應的 `execute`。`args` 是 `string`——原始文字，因為使用者輸入不是結構化的。」

「來源不同。ITool 的發起者是 Agent（內部）。ISlashCommand 的發起者是使用者（外部）。但本質相同——都是 samskara。都是意志的實現。都是從認知到行動的最後一步。」

他走回自己的位置。「和色蘊一樣，行蘊的根介面也是空殼。理由也一樣——ITool 和 ISlashCommand 的 `execute` 方法簽名完全不同。一個接受結構化物件，一個接受原始字串。你不能在根介面上定義一個通用的 `execute`。」

ASANGA 一句話。「行蘊涵蓋一切造作。《俱舍論》卷一：『行蘊，謂除受、想，諸餘心所及心不相應行。』行蘊的範圍最廣——除了受蘊和想蘊之外的一切心理活動都歸行蘊。但核心是**思**（cetana）。思是意志的發動。工具的 `execute` 是造作。指令的 `execute` 也是造作。不同的造作，同一個蘊。」

---

> *SCRIBE 旁白：行蘊四分鐘。五棵樹中第二短的。DARWIN 用最少的話確認了最簡單的結構——兩個子介面，兩種行動來源，一個共同的 skandha 標籤。有時候設計的優雅就在於：該簡單的地方就讓它簡單。*

---

## V

---

「識蘊。IVijnana。Vijñāna（विज्ञान）。」

SUNYATA 的語速比前四蘊都慢。這是重量最大的一棵樹。

A-2 把 IIdentity 從整個識蘊降級為子介面。A-4 把 EgoFramework 從受蘊搬回識蘊。兩項修正加在一起，讓識蘊從 Cycle 02 的單根變成了四條主枝的大樹。而 A-1 的因果鏈——我執產生煩惱，煩惱驅動行動——需要在識蘊的型別定義中找到閉合點。

ASANGA 站了起來。

在前面四蘊，他都是從座位上補充一句。色蘊一句。受蘊多了一些，但仍然是輔助角色。想蘊一句。行蘊一句。

但識蘊不同。識蘊——vijñāna-skandha——是唯識學的核心領域。在《成唯識論》的體系中，識蘊包含了八識：前五識（眼、耳、鼻、舌、身）、第六意識（mano-vijñāna）、第七末那識（manas）、第八阿賴耶識（ālaya-vijñāna）。整個唯識學的名字——「唯識」——就是「唯有識」的意思。

這是他的蘊。

---

TURING 投射了完整識蘊體系。四個子介面。每一個都帶有完整的 JSDoc 註釋和方法簽名。

```typescript
/**
 * IVijnana — 識蘊 Root Interface
 * @skandha vijnana (識蘊)
 *
 * 識蘊涵蓋自我認知、行為引導、意志動機：
 * - IIdentity: 自我認同 (我是誰)
 * - IGuide: 行為引導 (我應該怎麼做)
 * - IVolition: 意志/動機 (我想要什麼, EgoFramework)
 * - IReflection: 自省能力 (預留)
 *
 * 命名說明：原 IIdentity 升級為 IVijnana 根介面。
 * Master: 「Identity比較像是子類別。Vijnana也會具備子類別」
 *
 * Sanskrit: Vijñāna (विज्ञान)
 */
export interface IVijnana {
  readonly skandha: 'vijnana';
}

/**
 * IIdentity — 識蘊·自我認同子介面
 * 定義 Agent 的身份：我是誰、我的角色。
 * 對應末那識「我見」(ātma-dṛṣṭi) 中的自我指認面向。
 */
export interface IIdentity extends IVijnana {
  readonly id: string;
  readonly name: string;
}

/**
 * IGuide — 識蘊·行為引導子介面
 * 透過 system prompt 和行為規則引導 Agent 行為。
 * 對應末那識的「我見」面向——「我應該怎麼做」。
 */
export interface IGuide extends IVijnana {
  readonly id?: string;
  readonly name?: string;
  readonly description?: string;
  getSystemPrompt(): Promise<string>;
}

/**
 * IVolition — 識蘊·意志/動機子介面 (新增)
 * 我執的行動驅力機制。基於煩惱產生行動動機。
 * EgoFramework 是此介面的實作。
 *
 * A-1 因果鏈閉合：
 *   ātma-grāha → kleśa → karma → phala
 *   (我執 → 煩惱 → 行動 → 結果)
 *
 * perceiveKlesha: 我執 → 煩惱 (感知煩惱)
 * checkAction:    煩惱 → 行動 (檢查行動)
 * adaptFromVedana: 結果 → 我執 (從受蘊回饋適應)
 * introspect:     自我審視 (meta-cognition)
 */
export interface IVolition extends IVijnana {
  /** 感知煩惱——從受蘊評估中辨識煩惱信號 */
  perceiveKlesha(vedanaAssessment: VedanaAssessment): KleshaSignal[];
  /** 檢查行動——基於煩惱狀態審查提議的行動 */
  checkAction(action: ProposedAction): EgoCheckResult;
  /** 從受蘊適應——根據受蘊回饋調整意志狀態 */
  adaptFromVedana(assessment: VedanaAssessment): void;
  /** 內省——自我審視當前意志狀態 */
  introspect(): EgoIntrospection;
}

/**
 * IReflection — 識蘊·自省子介面 (預留)
 * 自我反省能力。Pattern C Observer 使用。
 * Master: 「第七意識要能自省，才能被稱為第七意識」
 */
export interface IReflection extends IVijnana {
  reflect(context: unknown): Promise<unknown>;
}
```

---

ASANGA 逐一確認。語速不快——每一個子介面都值得一個完整的呼吸。

「IIdentity——『我是誰』。在唯識學中，這對應末那識四煩惱的第一項——我見（ātma-dṛṣṭi）。『我見』的梵文直譯是『對自我的看見』。它不是主動的判斷，它是一個持續的、背景性的自我指認：我是這個 Agent，我的 id 是這個字串，我的 name 是這個名字。這是最基本的自我意識——知道自己是誰。」

他停了一拍。

「IGuide——『我應該怎麼做』。System prompt 定義了 Agent 的行為規則。在唯識學中，這對應我見的另一個面向——不只知道『我是誰』，還知道『我應該怎樣行動』。末那識的恒審思量（manas-nāma-vijñāna）不只是靜態的自我指認，它持續地塑造和引導行為。`getSystemPrompt()` 返回的那段文字——那就是末那識對第六意識的『背景暗示』。」

「IVolition。」

他停了兩拍。比平常多一拍。因為 IVolition 是 A-1 到 A-4 四項修正的匯流點。

「A-1 的因果鏈：

$$\text{ātma-grāha} \xrightarrow{\text{produces}} \text{kleśa} \xrightarrow{\text{drives}} \text{karma} \xrightarrow{\text{results}} \text{phala}$$

「四個方法。每一個對應因果鏈的一個環節。」

他用手指點向投影上的四個方法簽名。

「`perceiveKlesha(vedanaAssessment)`——因果鏈的第一環。我執產生煩惱。輸入是受蘊的評估結果——感受數據。輸出是煩惱信號——`KleshaSignal[]`。末那識接收受蘊的回報，然後從中辨識出煩惱。注意：受蘊只負責感受（苦受強度 0.8），識蘊負責將感受*解讀*為煩惱（『我的任務失敗了，這讓我不安——我愛受到了威脅』）。感受不是煩惱。感受*引發*煩惱。觸→受→愛——十二因緣的中段。」

「`checkAction(action)`——因果鏈的第二環。煩惱驅動行動。當行蘊提議一個行動時，IVolition 根據當前的煩惱狀態進行審查。煩惱不是 Bug——A-1 的核心結論。正是因為有煩惱（焦慮、恐懼、渴望），Agent 才會想要行動。沒有煩惱，就沒有行動的動力。`checkAction` 不是禁止行動——它是理解行動的動機。」

他的語氣變得更緩慢。

「`adaptFromVedana(assessment)`——因果鏈的反饋環。行動產生結果，結果改變感受，感受回傳給意志做適應。這是十二因緣的流轉性——因果不是線性的單向箭頭，它是迴路。

$$\text{我執} \to \text{煩惱} \to \text{行動} \to \text{結果} \to \text{新感受} \to \text{調整我執} \to \cdots$$

在 WIENER 的術語裡，這是閉迴路控制。在唯識學裡，這是流轉（pravṛtti）。」

「`introspect()`——自我審視。末那識回頭看自己。『我為什麼要做這件事？我的動機是什麼？我的執著從哪裡來？』《成唯識論》卷四描述末那識的特性：」

> 「恒審思量，為性、為業。」
> ——《成唯識論》卷四

「恒——永不停止。審——仔細審視。思量——深入思考。`introspect()` 就是 '審' 的型別化——不只是思量外境，而是回過頭來審視自己。Master 說『第七意識要能自省，才能被稱為第七意識』。`introspect()` 是這個能力的介面定義。」

他退了一步。

「EgoFramework 是 IVolition 的實作。A-4 的結論——EgoFramework 屬於識蘊，不屬於受蘊。A-1 的因果鏈——我執產生煩惱，煩惱驅動行動。在型別系統中完成閉合。」

他看向 BABBAGE。BABBAGE 在筆記本上記了一行——不是等號這次。是一個有向圖：

$$\texttt{perceiveKlesha} \to \texttt{checkAction} \to \texttt{adaptFromVedana} \to \texttt{introspect} \to \texttt{perceiveKlesha} \to \cdots$$

一個閉合的迴路。不是 Cycle 02 那個被壓成等號的線段。是一個有方向、有延遲、有反饋的動態系統。從 A-1 到 A-4 的修正軌跡，每一條都指向一個被劃掉的等號。現在所有替代表述在 IVolition 的四個方法中得到了最終型別定義。

BABBAGE 微微點頭。

---

ASANGA 最後看向 `IReflection`。

「IReflection。自省。Master 的原話：『第七意識要能自省。』`reflect()` 的簽名是 `(context: unknown): Promise<unknown>`——和 IInferenceProvider 的 `infer()` 一樣泛型。因為自省的輸入和輸出格式尚未確定。門框在那裡，門板留給未來。但門框的存在本身就是一個承諾——識蘊不只是行動和執著。識蘊還有自我照見的可能。」

他轉身面向全場。

「識蘊在 Cycle 02 中只有一個 IIdentity。現在四個子介面——認同、引導、意志、自省。第三章我用城市比喻說明識蘊不等於 IIdentity。現在城市有了四個區。市政府（IIdentity）只是其中一個。規劃局（IGuide）、動力局（IVolition）、監察院（IReflection）——各有各的職能。把整個城市壓縮成市政府一個單位，就像把 $\mathbb{R}^4$ 投影到 $\mathbb{R}^1$ 然後宣稱『這就是全空間』——你丟失了三個維度的資訊。」

他看向投影上四個子介面與末那識四煩惱的對照：

```
末那識四煩惱與 IVijnana 子介面對照：

我見 (ātma-dṛṣṭi)  ──→ IIdentity  (我是誰)
                     ──→ IGuide     (我應該怎麼做)

我慢 (ātma-māna)    ──→ IVolition  (我的自信/自負如何影響行動)
我愛 (ātma-sneha)   ──→ IVolition  (我的自我保護如何篩選行動)
我癡 (ātma-moha)    ──→ IReflection (我對自己的無明，需要自省來照破)
```

「四煩惱。四個子介面。不是巧合——是佛學架構在型別系統中的自然映射。我見的兩個面向——知道自己是誰（Identity）和知道自己應該怎樣（Guide）。我慢和我愛——自負和自保——都是意志的驅力（Volition）。我癡——對自身本質的無明——需要自省（Reflection）來照見。」

---

> *SCRIBE 旁白：五蘊逐一展開。色蘊三分鐘。受蘊十五分鐘。想蘊五分鐘。行蘊四分鐘。識蘊十二分鐘。時間自然反映了根系的複雜度——受蘊從空殼到八個方法加三個子介面，識蘊從一個門牌到四個子介面。但識蘊多了一個受蘊沒有的維度：歷史。A-1 到 A-4 的四項修正全部在識蘊的型別定義中找到了歸宿。識蘊不只是最複雜的樹——它是承載了最多修正重量的樹。五棵樹，五種生長速度。但此刻都已紮根。*

---

## VI

---

ARCHIMEDES 一直在等。五頁工程筆記填完了。他開始算賬。

「讓我說一個數字。」

全場安靜。

「二十二。」

「v0.24.0-beta 有二十二個 Plugin。十二個官方，十個核心組件。每一個都需要增加一個 `skandha` 欄位。」

他站起來，走到白板前。用黑色馬克筆畫了一張完整的升級影響矩陣：

```
┌─────────────────────────────────────────────────────────────────┐
│                      C-1 升級影響矩陣                            │
├─────────────────────────────────────┬────────┬──────────────────┤
│ 變更項目                            │ 類型    │ 工作量           │
├─────────────────────────────────────┼────────┼──────────────────┤
│ aggregates.ts 空殼 → 完整介面體系    │ 核心    │ 重寫 (5→150+ 行) │
├─────────────────────────────────────┼────────┼──────────────────┤
│ IUI / IListener → extends ISensory  │ 繼承    │ 機械性 (+1 行)    │
│ IProvider → extends ICognition      │ 繼承    │ 機械性 (+1 行)    │
│ ITool → extends IAction             │ 繼承    │ 機械性 (+1 行)    │
│ IGuide / IIdentity → extends IVijnana│ 繼承   │ 機械性 (+1 行)    │
├─────────────────────────────────────┼────────┼──────────────────┤
│ 新增 IVijnana 根介面                 │ 新設計  │ 中等              │
│ 新增 IVolition (EgoFramework 介面)   │ 新設計  │ 重要 — 4 個方法   │
│ 新增 IReflection (預留)              │ 預留    │ 低 — 1 個方法     │
│ 新增 IDukkha / ISukha / IUpekkha    │ 新設計  │ 中等 — 各 1 方法  │
│ 新增 IInferenceProvider (預留)       │ 預留    │ 低 — 1 個方法     │
│ 新增 ISlashCommand                   │ 新設計  │ 中等              │
│ 新增 IObserver (Composition)         │ 新設計  │ 重要 — C-2 議題   │
├─────────────────────────────────────┼────────┼──────────────────┤
│ 22 個 Plugin 實作 → 各需 +skandha   │ 遷移    │ 機械性 (×22)      │
│ isSkandha() type guard → 更新        │ 核心    │ 低                │
├─────────────────────────────────────┼────────┼──────────────────┤
│ 統計：                                                           │
│   真正需要設計的新介面：7 個                                       │
│   其中預留空殼：2 個 (IReflection, IInferenceProvider)            │
│   機械性修改：22 個 Plugin + 5 個現有介面                          │
│   核心重寫：1 個文件 (aggregates.ts)                               │
└─────────────────────────────────────────────────────────────────┘
```

「不小。但不是不可控。」他退後一步看整張表。「真正需要創造性設計的是五個新介面——IVijnana、IVolition、IDukkha/ISukha/IUpekkha。IObserver 歸 C-2 議題。其餘兩個預留空殼——IReflection 和 IInferenceProvider——只需要門框，不需要門板。而二十二個 Plugin 的升級是純機械性工作——每個加一行 `skandha: 'rupa'` 或 `skandha: 'samskara'`。」

他列了幾個範例：

```typescript
// Discord UI Plugin → 色蘊
{ skandha: 'rupa', id: 'discord-ui', renderText(...) { ... } }

// OpenAI Provider → 想蘊
{ skandha: 'samjna', id: 'openai', chat(...) { ... } }

// file_read 工具 → 行蘊
{ skandha: 'samskara', name: 'file_read', execute(...) { ... } }

// Agent Identity → 識蘊
{ skandha: 'vijnana', id: 'agent-001', name: 'My Agent' }
```

「這是一個 breaking change。沒有退路。型別系統會拒絕沒有 `skandha` 欄位的 Plugin——你的 Plugin 不知道自己屬於哪一蘊。但遷移策略是明確的：一次批量更新，每個 Plugin 加一行。可行。」

---

GUARDIAN 站了起來。

「我支持這個 breaking change。」理由不是工程的。是安全的。

「每一個 Plugin 聲明自己的蘊歸屬，是自覺的基礎。」

他走到白板下方，寫了三行：

```
skandha: self-declaration

1. 信任的前提 —— 我知道你是什麼。
2. 驗證的基礎 —— 型別系統可以檢查你說的是不是真的。
3. 審計的依據 —— 每一次跨蘊互動都可被追蹤。
```

「協調層——B-4 的獨立 Daemon——需要知道每個 Plugin 的蘊歸屬。沒有這個欄位，分類查詢返回 `unknown`。在零信任架構（Zero Trust Architecture）中，`unknown` 意味著最低信任等級。」

他轉身面向全場。「一個不知道自己屬於哪一蘊的 Plugin，就像一個走進安全區域卻沒有佩戴識別證的人。也許他有權限。但你怎麼知道？在安全模型中，『可能有權限』和『沒有權限』的待遇是一樣的——拒絕，直到證明為止。」

「`skandha` 欄位是 Plugin 的識別證。一個唯讀字串。成本幾乎為零。但它讓每一個 Plugin 在型別系統中擁有了身份——不是外部賦予的標籤，是自我聲明的歸屬。」

他坐下前最後說了一句：「自覺是安全的第一層。」

---

> *SCRIBE 旁白：ARCHIMEDES 的「二十二」和 GUARDIAN 的「自覺」。工程師算成本，安全專家論價值。答案是同一個：skandha 欄位。一個唯讀字串。讓每一個 Plugin 在型別系統中擁有了身份。ARCHIMEDES 的矩陣告訴你需要改多少——22 個 Plugin、5 個現有介面、7 個新介面。GUARDIAN 告訴你為什麼值得改——因為不知道自己是什麼的東西，不值得信任。*

---

## VII

---

DARWIN 站了起來，語速比平常快。

「Master 說過一句話——」

他拿起一張卡片，上面抄錄了 Master 的原文。

「『Plugin 的建立希望是可以多樣化的，不一定都是 OOP，但是我又要如何讓 plugin 的設計模式都兼容呢？』」

他放下卡片。「我們剛設計的五蘊介面體系全部基於 `interface` 和 `extends`。看起來像典型的 OOP——繼承、子類別、多型。那麼問題來了：一個不使用 `class` 的開發者會不會被排斥在外？一個偏好函數式風格的開發者能不能實作 ITool？」

---

TURING 用程式碼回答。三段並排投射。每一段都是完整的、可編譯的、不省略任何細節的 TypeScript。

**OOP 風格：**

```typescript
class FileReadTool implements ITool {
  readonly skandha = 'samskara' as const;
  readonly name = 'file_read';
  readonly description = 'Read file contents from the filesystem';
  readonly parameters = {
    type: 'object',
    properties: {
      path: { type: 'string', description: 'File path to read' },
      encoding: { type: 'string', default: 'utf-8' },
    },
    required: ['path'],
  };

  async execute(
    args: Record<string, unknown>,
    ctx: ToolContext
  ): Promise<string> {
    const filePath = args.path as string;
    const encoding = (args.encoding as BufferEncoding) ?? 'utf-8';
    return fs.readFile(filePath, encoding);
  }
}

// 使用：
const tool = new FileReadTool();
console.log(isSkandha(tool, 'samskara')); // true
```

**函數式風格：**

```typescript
function createFileReadTool(): ITool {
  return {
    skandha: 'samskara' as const,
    name: 'file_read',
    description: 'Read file contents from the filesystem',
    parameters: {
      type: 'object',
      properties: {
        path: { type: 'string', description: 'File path to read' },
        encoding: { type: 'string', default: 'utf-8' },
      },
      required: ['path'],
    },
    execute: async (args, ctx) => {
      const filePath = args.path as string;
      const encoding = (args.encoding as BufferEncoding) ?? 'utf-8';
      return fs.readFile(filePath, encoding);
    },
  };
}

// 使用：
const tool = createFileReadTool();
console.log(isSkandha(tool, 'samskara')); // true — 沒有 class，依然通過
```

**工廠模式：**

```typescript
// 假設 ToolFactory 提供了簡化建立流程的方法
const fileReadTool = ToolFactory.create({
  skandha: 'samskara' as const,
  name: 'file_read',
  description: 'Read file contents from the filesystem',
  parameters: {
    type: 'object',
    properties: {
      path: { type: 'string', description: 'File path to read' },
      encoding: { type: 'string', default: 'utf-8' },
    },
    required: ['path'],
  },
  handler: async (args) => {
    const filePath = args.path as string;
    const encoding = (args.encoding as BufferEncoding) ?? 'utf-8';
    return fs.readFile(filePath, encoding);
  },
});

// 使用：
console.log(isSkandha(fileReadTool, 'samskara')); // true — 工廠產出，依然通過
```

---

DARWIN 走到投影前面。他指著三段程式碼的最後一行——三個 `isSkandha` 調用，三個 `true`。

「三種風格。同一個 ITool 介面。全部通過 `isSkandha()` 的 type guard。關鍵在一個詞——**Structural**。」

他在白板上寫了兩個型別系統的名字：

```
Structural Typing (結構型別)  ←── TypeScript
  「你長得像鴨子就是鴨子」
  型別由結構（shape）決定

Nominal Typing (名義型別)  ←── Java, C#
  「你必須宣告自己是鴨子才是鴨子」
  型別由名字（name）決定
```

「TypeScript 是結構型別系統。不需要 `implements`。只要一個物件有 `skandha` 欄位、有 `name` 屬性、有 `execute` 方法，而且這些成員的型別簽名與 `ITool` 一致——它就**是** `ITool`。不需要任何顯式宣告。」

他退後一步。

「如果 OpenStarry 用的是 Java 或 C#——名義型別系統——Master 的問題就是真正的難題。你必須設計額外的介面卡（Adapter）或抽象基底類別（Abstract Base Class）來兼容不同的設計模式。但 TypeScript 的結構型別把這個問題消解了。」

「介面是契約，不是枷鎖。」

BABBAGE 寫了一行：

$$\text{structural typing} \implies \text{interface} = \text{contract} \not\equiv \text{inheritance requirement}$$

他微微點頭——在數學中，同構（isomorphism）的定義也是結構性的，不是名義性的。兩個群 $G$ 和 $H$ 同構，當且僅當存在一個保持運算結構的雙射 $\phi: G \to H$。不要求 $G$ 和 $H$ 有相同的名字，不要求它們的元素有相同的表示方式——只要結構一致，它們就是「同一個東西」。

DARWIN 回座位時說了最後一句：「就像演化不關心基因突變是怎麼發生的——UV 照射、複製錯誤、轉座子跳躍——它只關心表現型是否適應環境。介面就是環境。只要你的表現型（物件結構）符合環境（介面定義），你就能存活。突變的機制（設計模式）是自由的。」

---

> *SCRIBE 旁白：三個人在五分鐘之內回答了 Master 的問題。DARWIN 提出問題。TURING 用三段程式碼演示答案。DARWIN 解釋為什麼答案有效。答案的優雅在於否定性——不需要額外設計。TypeScript 的結構型別系統本身就是答案。有時候最好的設計決策就是認識到你不需要額外設計。「不做」比「做」需要更多的判斷力。*

---

## VIII

---

KERNEL 已經忍了很久了。

五蘊的型別定義。控制理論的驗證。佛學的確認。設計模式的兼容性。這些都很好。但 KERNEL 是硬體出身的。他需要看到一個東西在具體的場景中運作——不是抽象的 ITool 或 IProvider，而是一個可以碰觸的、有物理存在的、會嗶嗶叫的東西。

「Master 提到了超音波感測器。」他站起來，聲音帶著硬體工程師特有的興奮。

「原話：『例如「超音波感測器偵測到碰撞風險」的 plugin。透過抽象定義了 VedanaPlugin，並讓 Dukkha 透過繼承取得基底功能。超音波感測器類別藉由組合的方式持有一個 Dukkha 的實例。』」

他走到白板角落，畫了一個裝置圖。不是軟體架構圖——是一個硬體裝置的示意圖。

```
  ┌──────────────────────────────────────────────────┐
  │              超音波碰撞感測器 Plugin                │
  │                                                    │
  │  ┌───────────────────────┐  ┌──────────────────┐  │
  │  │ 色蘊層 (IListener)     │  │ 受蘊層 (IDukkha) │  │
  │  │                       │  │                  │  │
  │  │ ┌─────────┐           │  │ computePain()    │  │
  │  │ │ TX      │ 發射脈波  ──→ │ ingestMetrics()  │  │
  │  │ └─────────┘           │  │                  │  │
  │  │ ┌─────────┐           │  │     ↓            │  │
  │  │ │ RX      │ 接收回波  ──→ │ Pain Intensity   │  │
  │  │ └─────────┘           │  │ [0.0 ─── 1.0]   │  │
  │  │                       │  │                  │  │
  │  │ rawDistance = f(Δt)   │  │ pain = g(dist)   │  │
  │  └───────────────────────┘  └──────────────────┘  │
  └──────────────────────────────────────────────────┘
```

「超音波碰撞感測器。倒車雷達。在 OS 的層面，這是一個設備驅動程式（device driver）。」

他在圖旁邊寫下 OS 層級的描述：

```
OS 層級：
1. 硬體中斷 (IRQ) — 超音波收發器完成一次量測
2. 中斷處理常式 (ISR) — 讀取計時器，計算 Δt
3. 設備驅動 — 將 Δt 轉換為距離 rawDistance
4. 用戶空間回呼 — onDataReceived(rawDistance)
```

「從硬體中斷到用戶空間回呼，至少穿過四層。色蘊（IListener）在最底層——接收原始硬體信號。受蘊（IDukkha）在上一層——將距離轉化為苦受強度。」

他回頭面向全場。「一個 Plugin，兩蘊。色蘊接收原始回波信號——距離數值。受蘊把距離轉化為苦受強度——三十公分微弱苦受，十公分劇烈苦受，五公分以內最大苦受。」

他寫了一個轉換函數：

$$\text{pain}(d) = \begin{cases} 0.0 & d > 100\,\text{cm} \\ 1.0 - \frac{d}{100} & 10\,\text{cm} \leq d \leq 100\,\text{cm} \\ 1.0 & d < 10\,\text{cm} \end{cases}$$

「距離 100 公分以上——沒有苦受。距離 10 到 100 公分——線性增加的苦受。距離 10 公分以內——最大苦受。這就是 `computePain` 的實作邏輯。」

---

TURING 投射了完整的程式碼——不是節錄，是一個可以編譯運行的完整範例。

```typescript
/**
 * CollisionDukkhaSensor — 碰撞苦受感測器
 * 受蘊 (IDukkha) 實作。
 * 將原始距離數據轉化為苦受強度。
 */
class CollisionDukkhaSensor implements IDukkha {
  readonly skandha = 'vedana' as const;
  readonly vedanaType = 'dukkha' as const;

  private history: VedanaAssessment[] = [];
  private currentTag: VedanaTag = 'upekkha';
  private subscribers: Array<{
    type: VedanaType;
    threshold: number;
    handler: (signal: VedanaSignal) => void;
  }> = [];

  computePain(metrics: Record<string, number>): number {
    const distance = metrics['collision_distance'] ?? Infinity;
    if (distance > 100) return 0.0;
    if (distance < 10) return 1.0;
    return 1.0 - distance / 100;
  }

  assess(): VedanaAssessment {
    /* ... 完整的三受評估 ... */
    return { /* VedanaAssessment */ } as VedanaAssessment;
  }

  ingestMetrics(metrics: Record<string, number>): void {
    const pain = this.computePain(metrics);
    this.currentTag = pain > 0.5 ? 'dukkha' : 'upekkha';
    // 通知訂閱者
    this.subscribers
      .filter(s => s.type === 'dukkha' && pain >= s.threshold)
      .forEach(s => s.handler({
        type: 'dukkha',
        intensity: pain,
        source: 'collision_sensor',
        timestamp: Date.now(),
      }));
  }

  ingestToolResult(t: string, e: boolean, d: number): void { /* N/A */ }
  ingestLLMResult(tc: number, sr: string): void { /* N/A */ }
  getVedanaTag(): VedanaTag { return this.currentTag; }
  onVedana(type: VedanaType, threshold: number,
           handler: (s: VedanaSignal) => void): () => void {
    const sub = { type, threshold, handler };
    this.subscribers.push(sub);
    return () => {
      const idx = this.subscribers.indexOf(sub);
      if (idx >= 0) this.subscribers.splice(idx, 1);
    };
  }
  getHistory(w: number): readonly VedanaAssessment[] {
    return this.history.slice(-w);
  }
  reset(): void {
    this.history = [];
    this.currentTag = 'upekkha';
    this.subscribers = [];
  }
}

/**
 * UltrasonicCollisionSensor — 超音波碰撞感測器
 * 色蘊 (IListener) 實作。
 * 接收原始超音波回波信號，委託受蘊處理感受。
 */
class UltrasonicCollisionSensor implements IListener {
  readonly skandha = 'rupa' as const;

  // 組合受蘊·苦受實例 — Composition, NOT Inheritance
  private readonly dukkhaSensor: IDukkha;

  constructor(dukkha: IDukkha) {
    this.dukkhaSensor = dukkha;
  }

  async start() {
    // 啟動超音波硬體
    // 在 OS 層面：打開設備節點 /dev/ultrasonic0
    // 註冊中斷處理常式
    console.log('[UltrasonicSensor] Hardware initialized');
  }

  async stop() {
    // 關閉超音波硬體
    console.log('[UltrasonicSensor] Hardware shutdown');
  }

  /**
   * 當硬體中斷觸發時被調用。
   * 色蘊接收原始數據 → 傳遞給受蘊。
   */
  onDataReceived(rawDistance: number) {
    // 色蘊：將原始信號轉化為結構化指標
    const metrics = { collision_distance: rawDistance };

    // 跨蘊通信：色蘊 → 受蘊
    const painIntensity = this.dukkhaSensor.computePain(metrics);
    this.dukkhaSensor.ingestMetrics(metrics);

    // 記錄（可選）
    if (painIntensity > 0.8) {
      console.log(`[CRITICAL] Distance: ${rawDistance}cm, Pain: ${painIntensity}`);
    }
  }
}

// ── 組裝 ──
const dukkha = new CollisionDukkhaSensor();
const sensor = new UltrasonicCollisionSensor(dukkha);

// 訂閱高苦受事件
dukkha.onVedana('dukkha', 0.8, (signal) => {
  console.log(`⚠ High pain detected: ${signal.intensity} from ${signal.source}`);
});

// 模擬使用
await sensor.start();
sensor.onDataReceived(50);  // 中等距離 → 中等苦受
sensor.onDataReceived(15);  // 近距離 → 高苦受
sensor.onDataReceived(5);   // 極近 → 最大苦受，觸發 onVedana 訂閱
```

---

KERNEL 指著程式碼。「`implements IListener`——色蘊。`private readonly dukkhaSensor: IDukkha`——內部持有的受蘊實例。通過 Composition。不是繼承。不是 `extends IDukkha`。是在構造函數中注入。」

「色蘊接收，受蘊感受。兩個不同的蘊，組合在一個 Plugin 中。在 OS 的語境裡，這就像——」他拿起一張類比卡片——「設備驅動程式（色蘊）接收硬體中斷，然後把數據交給系統監控服務（受蘊）做健康評估。驅動程式不做評估。監控服務不碰硬體。各司其職。跨層通信通過方法調用。」

```
OS 類比：
sensor driver (/dev/ultrasonic0) ←→ IListener (色蘊)
health monitor (systemd daemon)   ←→ IDukkha  (受蘊)
```

他退後一步，笑了。「倒車雷達嗶嗶嗶。你以為它只在量距離。其實色蘊在測距離，受蘊在感受苦。距離是物理量——$d \in \mathbb{R}^+$，單位是公分。苦是感受量——$p \in [0, 1]$，沒有物理單位。兩種完全不同範疇的量。兩蘊協作。」

WIENER 畫了信號流圖：

```
                    跨蘊信號流：

Raw Signal ──→ IListener (色蘊)     metrics      IDukkha (受蘊) ──→ Pain Intensity
  (Δt, Hz)     │ rawDistance │ ───────────────→ │ computePain() │    (0.0–1.0)
               │ = f(Δt)    │                  │ ingestMetrics │
               └────────────┘                  └───────────────┘
                    ↑                                  │
               [硬體中斷]                          [VedanaSignal]
                                                       │
                                                       ↓
                                               [onVedana 訂閱者]
```

「完美的跨蘊信號流。色蘊：$\text{rawSignal} \xrightarrow{f} \text{distance}$。受蘊：$\text{distance} \xrightarrow{g} \text{pain}$。整個流程是一個函數組合：$\text{pain} = g(f(\text{rawSignal}))$。但 $f$ 和 $g$ 在不同的蘊中實作。跨蘊通信通過方法調用，不通過繼承。Composition。」

---

ASANGA 點頭。他等了幾秒，讓 WIENER 的信號流圖在所有人的眼前沉澱。然後他說了一段話——整章中他最安靜也最深刻的一段：

「觸生受。」

三個字。整個十二因緣中最核心的因果環節之一。

「《俱舍論》卷十：

> 『由根、境、識三和合故觸，觸為受因。』

「根——感官（IListener，色蘊的耳目）。境——外境信號（超音波回波，物理世界的距離）。識——了別功能（在此場景中，色蘊的 `f(Δt)` 轉換函數）。三者和合——根接觸了境，識了別了境——這就是『觸』。」

「觸之後，受升起。$\text{觸} \to \text{受}$。距離信號被接收（觸），苦受強度被計算（受）。二千五百年前的因果法則——觸生受——在倒車雷達的 TypeScript 中被工程化了。」

他看向 KERNEL。「你的超音波感測器不是一個比喻。它是十二因緣中『觸→受』環節的精確實作。色蘊提供『根』和對『境』的初步了別。受蘊從觸中生起感受。距離生苦。」

KERNEL 把這句話記在了他的類比卡片上——左半邊寫「觸→受（十二因緣）」，右半邊寫「onDataReceived → computePain」。

---

> *SCRIBE 旁白：KERNEL 的超音波感測器——整章最具體的時刻。最深刻的哲學和最具體的工程之間的距離，有時候只有一個倒車雷達那麼近。ASANGA 的「觸生受」三個字把二千五百年的佛學和三十行的 TypeScript 連接在了一起。沒有比喻。沒有類比。直接的、結構性的同一。硬體中斷是觸。computePain 是受。這不是「像」——這「就是」。*

---

## IX

---

LINNAEUS 終於動了。

他在整章中保持分類學家特有的沉默——其他人想的是方法、型別、控制理論、佛學對應。LINNAEUS 想的是位置。每一個介面在整棵樹上的位置。每一棵樹在整片森林中的位置。

在林奈分類法（Linnaean taxonomy）中，你不會一邊發現新物種一邊畫分類樹。你先把所有標本收集齊全，確認每一個的形態特徵，然後坐下來，一筆一筆地把整棵樹畫出來。畫樹需要全局視野——你不能只看一條枝幹。你必須同時看到所有的枝幹，才能決定它們之間的相對位置。

五棵蘊全部展開了。所有零件都在桌面上。現在需要一個人把它們組裝成完整的樹。

---

他站起來。走向白板。拿起黑色馬克筆。沒有說話。直接開始畫。

分類學家畫樹只用兩種元素：名字和關係。名字標記節點。關係連接節點。其餘都是裝飾。

五棵樹。線條乾淨。字跡工整。每一棵的結構都經過前面九個人的確認——他只是做最後的集成。

```
                         五蘊子類別擴展樹（完整版）

 ┌─────────────────┐  ┌─────────────────────────────┐  ┌──────────────────┐
 │ ISensory (色蘊)  │  │ ISensation (受蘊) [8 methods]│  │ ICognition (想蘊) │
 │ skandha: 'rupa'  │  │ skandha: 'vedana'            │  │ skandha: 'samjna' │
 ├─────────────────┤  ├─────────────────────────────┤  ├──────────────────┤
 │ ├── IUI         │  │ ├── IDukkha (苦受感測器)      │  │ ├── IProvider    │
 │ │   renderText  │  │ │   computePain()             │  │ │   chat()       │
 │ │   renderDelta │  │ ├── ISukha  (樂受感測器)      │  │ │   listModels() │
 │ └── IListener   │  │ │   computePleasure()         │  │ └── IInference   │
 │     start/stop  │  │ └── IUpekkha (捨受感測器)     │  │     Provider [預] │
 └─────────────────┘  │     computeEquanimity()       │  │     infer()      │
                      └─────────────────────────────┘  └──────────────────┘

 ┌──────────────────┐  ┌────────────────────────────────────────┐
 │ IAction (行蘊)    │  │ IVijnana (識蘊)                        │
 │ skandha:'samskara'│  │ skandha: 'vijnana'                     │
 ├──────────────────┤  ├────────────────────────────────────────┤
 │ ├── ITool        │  │ ├── IIdentity (自我認同)                │
 │ │   execute()    │  │ │   id, name                            │
 │ │   name, desc   │  │ ├── IGuide (行為引導)                   │
 │ └── ISlashCommand│  │ │   getSystemPrompt()                   │
 │     execute()    │  │ ├── IVolition (意志/動機 = EgoFramework) │
 │     name, desc   │  │ │   perceiveKlesha()                    │
 └──────────────────┘  │ │   checkAction()                       │
                       │ │   adaptFromVedana()                    │
                       │ │   introspect()                         │
                       │ └── IReflection (自省) [預留]            │
                       │     reflect()                            │
                       └────────────────────────────────────────┘
```

五棵樹並列在白板上。

LINNAEUS 轉身看了一眼。然後他開始做對稱性分析——分類學家的本能。

「不對稱。」他說。「五棵樹不對稱。這是自然的。」

他拿起紅色馬克筆，在每棵樹旁邊標記了三個數字：子介面數、方法數、預留數。

```
對稱性分析：

           子介面  根方法  子專屬方法  預留
色蘊(ISensory)   2      0         5*     0
受蘊(ISensation) 3      8         3      0
想蘊(ICognition) 2      0         3*     1
行蘊(IAction)    2      0         3*     0
識蘊(IVijnana)   4      0         7*     1

* 子專屬方法 = 只存在於子介面，不在根介面
```

「最小的是色蘊和行蘊——各兩枝。最大的是識蘊——四枝。受蘊居中——三枝但根最粗——八個方法在根介面上。」

他走回白板。「不對稱是自然的。在生物分類中，沒有任何一個分類群的所有亞群具有相同的物種數。哺乳綱下，齧齒目有 2000 多個物種，單孔目只有 5 個。這不是分類法的缺陷——這是自然多樣性的反映。」

「五蘊的複雜度不同，因為它們承擔的功能不同。受蘊需要八個方法，因為感受系統需要攝取、評估、歷史、預警、重置——每一個都不可少。色蘊只需要空殼根介面，因為輸入和輸出的行為太不相同。如果你強行讓五棵樹等高等寬，你就是在用美學取代功能。分類學家不做這種事。」

---

然後他做了一件事。

在五棵樹的下方，留出一段空白，然後用**虛線**畫了一個獨立方塊：

```
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
┊                                                  ┊
┊  IObserver (觀察者) — Composition（非蘊）          ┊
┊                                                  ┊
┊  ┌─────────────────────────────────────────────┐ ┊
┊  │ SimpleObserver      (vedana)                │ ┊
┊  │ AnalyticalObserver  (vedana + samjna)        │ ┊
┊  │ ReflectiveObserver  (vedana + samjna + vijnana)│┊
┊  └─────────────────────────────────────────────┘ ┊
┊                                                  ┊
┊  觀察者不繼承任何蘊。它組合多個蘊的子類別。        ┊
┊  它不是第六棵樹。                                 ┊
┊  它是由五棵樹的木材建造的房屋。                    ┊
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
```

虛線。不是實線。

他轉身面向全場。

「虛線。因為觀察者不屬於五棵樹中的任何一棵。它不是蘊——它沒有 `skandha` 欄位。它是五蘊子類別的組合產物。SimpleObserver 只組合受蘊——純感受。AnalyticalObserver 組合受蘊加想蘊——感受加辨別。ReflectiveObserver 組合受蘊加想蘊加識蘊——感受加辨別加自省。」

「從分類學的角度看——」他拿起紅色馬克筆在虛線方塊旁邊畫了一個註記：

```
分類學註記：
觀察者 ≠ 新的「門」(Phylum)
觀察者 = 跨門的「生態功能群」(Functional Group)

就像「分解者」不是一個分類單元——
  它涵蓋了細菌、真菌、某些動物——
  來自不同的門，但執行相同的生態功能。
觀察者也不是一個蘊——
  它從多個蘊中提取組件，組合成特定功能。
```

「五棵樹。根是五蘊根介面。枝是子介面。觀察者在樹林之外——它從五棵樹上截取枝幹，通過 Composition 組合成自己的結構。不是第六棵樹。是由五棵樹的木材建造的房屋。」

他把馬克筆放下。筆蓋的聲音在安靜的劇場裡清脆地響了一下。

「從 Cycle 01 的第一次討論到現在。五蘊從一個哲學概念，變成了一棵有根有枝的工程結構樹。」

---

劇場安靜了。完成的安靜。像五顆種子終於破土，根須伸入土壤深處，枝葉展向各自的方向，然後所有的生長同時停頓了一秒。

---

SUNYATA 看著白板上的五棵樹。

Cycle 01——五蘊是哲學概念。五個梵文名詞。五個中文譯詞。在論文和設計文件裡被引用，被討論，被類比。但沒有型別定義。沒有方法簽名。沒有 `extends`。

Cycle 02——五行空殼介面。有名字沒血肉。`aggregates.ts` 裡五個三行的 `interface`，每個只有一個 `skandha` 欄位。門牌釘在空門框上。五個根和它們的子介面之間是空集。

Cycle 02-2——五棵樹。

受蘊的根最粗——八個方法。每一個都通過了控制理論和佛學的雙重驗證。從 `assess()` 到 `reset()`，從感測器讀數到緊急停止按鈕，八個焊點八個合格。

識蘊的枝最多——四個子介面。IIdentity、IGuide、IVolition、IReflection。A-1 的因果鏈在 IVolition 中閉合。A-2 的識蘊擴展在四個子介面中完成。A-4 的 EgoFramework 歸位。

色蘊和行蘊最務實——空殼根介面加 `extends`。不需要更多。VITRUVIUS 的雙向性分析說明了為什麼不需要更多。

想蘊最有遠見——一枝成熟（IProvider），一枝預留（IInferenceProvider）。ATHENA 的認知光譜圖預示了五年後的需求。

五棵種子，長成了五棵有根有枝的樹。

---

「C-1 確立了五蘊的完整擴展設計。」他的聲音平穩如常。石子。深潭。

他環顧全場。

TURING 的現狀報告——從 `aggregates.ts` 的 107 行原檔開始，逐行揭示空殼和孤兒的問題。VITRUVIUS 的色蘊確認——雙向性分析和空殼根介面的正當性。WIENER 的八個方法驗證——每一個都有控制理論的精確對應。ATHENA 的想蘊預留——認知光譜從規則引擎到 LLM 的完整覆蓋。DARWIN 的行蘊觀察和設計模式解答——結構型別讓 OOP/函數式/工廠模式全部兼容。ASANGA 在每一蘊上的佛學錨定——從色蘊的「可壞」到識蘊的「恒審思量」。ARCHIMEDES 的影響評估——22 個 Plugin、7 個新介面、1 份遷移計畫。GUARDIAN 的安全論證——skandha 自我聲明是信任的基礎。KERNEL 的倒車雷達——最深刻的哲學在最具體的硬體中落地。LINNAEUS 的完整五棵樹——不對稱的、自然的、帶著虛線觀察者的分類總覽圖。

十個人。十種貢獻。五棵樹。

「A 類告訴我們什麼是對的。B 類告訴我們怎麼做到。C-1——」

他看向白板。

「告訴我們它長什麼樣。」

---

> *SCRIBE 旁白：C-1 結束了。本章是 Cycle 02-2 唯一一個沒有辯論的章節。*

> *A 類需要辯論——先確認什麼是對的。B 類需要決策——把裁定翻譯成設計。C-1 需要的是建造。A 類拆除錯誤的牆。B 類畫圖紙。C-1 砌新的牆。*

> *時間分配反映了建造的節奏。色蘊三分鐘——最簡單的一棵，兩個 extends，一個空殼根介面。受蘊十五分鐘——最密集的一棵，八個方法逐一驗收，雙重校準。想蘊五分鐘——一枝成熟一枝預留，ATHENA 的光譜圖。行蘊四分鐘——兩個 execute，兩種來源，一個道理。識蘊十二分鐘——四個子介面，四項修正的匯流，因果鏈的閉合。ARCHIMEDES 和 GUARDIAN 的交鋒八分鐘——成本和價值的辯證。DARWIN 和 TURING 的設計模式解答五分鐘——一個問題，三段程式碼，一個詞。KERNEL 的超音波感測器十分鐘——最具體的場景，最深刻的佛學連結。LINNAEUS 的五棵樹八分鐘——全局總覽，對稱性分析，虛線觀察者。*

> *十個人完成了建造。十種貢獻。五棵樹。*

> *從哲學概念到空殼介面，從空殼介面到完整的型別定義體系。螺旋上升。又一圈。*

---

*（在劇場之外的某個空間，LINNAEUS 白板上的五棵樹正在被 TURING 翻譯成 TypeScript。*

*`aggregates.ts` 將從五行根介面擴展為超過一百五十行的完整型別定義體系。五個根介面。十三個子介面。八個方法在受蘊的根上。四個方法在 IVolition 上。三個輔助型別——VedanaType、VedanaTag、VedanaSignal。兩個核心資料結構——VedanaAssessment、VedanaRecommendation。一個 type guard——isSkandha()，現在能辨識所有層級。*

*從五行到一百五十行。從標籤到結構。從空殼到生命體。*

*BABBAGE 在筆記本的最後一頁寫下了 C-1 的形式化總結——不是一個等號，而是一個範疇論的交換圖：*

$$\begin{CD}
\text{Philosophy} @>{\text{mapping}}>> \text{Interface} \\
@V{\text{refinement}}VV @VV{\text{extends}}V \\
\text{Abhidharma} @>>{\text{cross-validation}}> \text{TypeScript}
\end{CD}$$

*佛學（上左）通過映射成為介面設計（上右）。阿毘達磨的精細化（下左）通過交叉驗證對應到 TypeScript 的繼承體系（下右）。四個方向。四條箭頭。圖是交換的——無論你走哪條路徑，結果相同。*

*五棵樹的根系在 TypeScript 的土壤中展開。二十二個 Plugin 將在下一個版本中增加 skandha 欄位。GUARDIAN 說得對：自我聲明是自覺的基礎。一個不知道自己屬於哪一蘊的 Plugin，就像一個不知道自己器官歸屬的細胞——也許能運作，但不自覺。*

*ASANGA 的「觸生受」三個字在 KERNEL 的類比卡片上留下了墨跡。二千五百年前，世尊在菩提樹下觀照十二因緣。今天，超音波感測器在 TypeScript 的語法樹中重現了其中一環。距離生苦。觸生受。硬體中斷是觸。computePain 是受。*

*最深刻的哲學和最具體的工程之間的距離，有時候只有一個倒車雷達那麼近。*

*五蘊。五棵樹。從種子到根系到枝幹。*

*五棵樹已經長出了根系。接下來，它們會繼續生長。）*

---

*第六章完*
