# 第六章：五棵樹的根系

---

SUNYATA 在劇場中央站了片刻，什麼都沒說。

A 類用了三個章節修正哲學。B 類用了一個章節落實裁定。那些是拆解和決策。現在要做的事情不同。

現在要建造。

---

「C-1。五蘊子類別擴展設計。」

他拿起 Master 的信，找到那一段。

「『五蘊可以做為物件導向中的根本類別（Root Class），要如何擴展，可以做更詳細的安排。』」

他放下信。「前四章修正了地基。現在，C-1 要在修正過的地基上，把五棵樹從種子長成有根、有幹、有枝的完整生命體。」

他看向 TURING。「讓我們先看看種子現在長什麼樣。」

---

> *SCRIBE 旁白：SUNYATA 用了「五棵樹」的意象。牆壁和柱子是死的。樹是活的。樹有根，根會伸展。樹有枝，枝會分叉。五蘊的擴展不是靜態的堆砌——它是有機的、向多個方向同時展開的生長。*

---

TURING 的螢幕投射到劇場中央。冷光。白底。黑字。

```typescript
export interface ISensory    { readonly skandha: 'rupa'; }
export interface ISensation   { readonly skandha: 'vedana'; }
export interface ICognition   { readonly skandha: 'samjna'; }
export interface IAction      { readonly skandha: 'samskara'; }
export interface IIdentity    { readonly skandha: 'vijnana'; }
```

五行。每一行只有一個欄位。`readonly skandha`。一個標籤。

「五個根介面。沒有方法。沒有行為定義。沒有子介面繼承。」

他讓投影停留了幾秒。五行字像五個只寫了名字的門牌釘在五扇還沒建好的門上。

「它們就像五個只有標籤的空盒子。Master 要我們把盒子打開，往裡面放東西。」

---

他切換投影。

```typescript
export interface IUI { ... }       // 色蘊？未繼承 ISensory
export interface IListener { ... } // 色蘊？未繼承 ISensory
export interface IProvider { ... } // 想蘊？未繼承 ICognition
export interface ITool { ... }     // 行蘊？未繼承 IAction
export interface IGuide { ... }    // 識蘊？未繼承 IIdentity
```

「現有的具體介面。它們各自有完整的方法定義。但它們和五個根介面之間沒有任何關係。沒有 extends。沒有繼承。門牌和門是分開的。你知道 IUI 應該屬於色蘊，但型別系統不知道。」

BABBAGE 在筆記本上寫了一行：`roots ∅ children = orphans`。根和子類別之間是空集。孤兒。

---

SUNYATA 用手指計數。五個設計目標。

「一。每個蘊的根介面增加核心方法。二。現有介面升級為子介面——IUI extends ISensory，以此類推。三。新增必要的子介面——IVijnana 體系、三受介面。四。觀察者用 Composition，不屬於任何蘊。五。isSkandha() 全層級可用。」

五根手指收回。「現在，逐蘊展開。」

---

## I

---

「色蘊。ISensory。」

VITRUVIUS 站了起來。色蘊——形相與物質性——是全端架構分析師最直覺的領域。

「色蘊是最簡單的一棵。兩個子介面已經存在了。IUI 負責輸出渲染——嘴巴，說出去的。IListener 負責感官輸入——耳朵，聽進來的。只需要讓它們 extends ISensory。」

TURING 投射了修改後的定義。

```typescript
export interface ISensory {
  readonly skandha: 'rupa';
}

export interface IUI extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
  renderText?(text: string, sessionId?: string, replyTo?: string): void;
  renderDelta?(delta: string, sessionId?: string, replyTo?: string): void;
}

export interface IListener extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
}
```

「ISensory 根介面保持空殼。」TURING 說。「IUI 和 IListener 的行為方向完全相反——輸出和輸入。強行統一到一個共通方法裡會製造虛假的抽象。根的存在是為了 isSkandha('rupa') 能通過。」

ASANGA 從座位上補了一句。「色蘊是接觸。和外境的接觸。IUI 和 IListener 代表接觸的兩個方向。往外的和往內的。」

---

> *SCRIBE 旁白：色蘊三分鐘。一個 extends。一棵樹的第一條根——最短的一條——入土了。*

---

## II

---

「受蘊。ISensation。」SUNYATA 的聲音微微放慢了。所有人都知道受蘊將是五棵樹中根系最龐大的一棵。

WIENER 已經在翻方格紙了。「ISensation 是變化最大的。」SUNYATA 說。「從空殼變成八個核心方法。WIENER，逐一確認。」

TURING 投射了完整介面。

```typescript
export interface ISensation {
  readonly skandha: 'vedana';
  assess(): VedanaAssessment;
  ingestMetrics(metrics: Record<string, number>): void;
  ingestToolResult(toolName: string, isError: boolean, durationMs: number): void;
  ingestLLMResult(tokenCount: number, stopReason: string): void;
  getVedanaTag(): VedanaTag;
  onVedana(type: VedanaType, threshold: number, handler: (signal: VedanaSignal) => void): () => void;
  getHistory(windowSize: number): readonly VedanaAssessment[];
  reset(): void;
}
```

WIENER 站了起來，用手指逐一點過——像工程師驗收流水線的每一個工站。

「assess()——感測器讀數函數。ingestMetrics/ingestToolResult/ingestLLMResult——三個輸入通道，複合感測器的不同接口。getVedanaTag()——O(1) 快取查詢，儀表板上的數字。」

他停了一下。嘴角微微上揚。

「onVedana()——看門狗計時器的泛化。不連續輪詢，在苦受超過 0.8 的時候才通知訂閱者。事件驅動的閾值監測。getHistory()——滑動視窗歷史，PID 控制器積分項的基礎。reset()——緊急停止按鈕。」

八個方法，八個控制理論對應。「受蘊的根介面不再是空殼——它是一個完整的感測器介面。」

---

ASANGA 站了起來。受蘊需要比色蘊更多的空間。

「受蘊只做一件事。感受。不判斷。不分析。碰到火——苦。吃到甜——樂。無事發生——捨。」

他看了看投影上的八個方法。「八個方法。每一個都在『感受』的範圍之內。assess 是感受的輸出。ingest 系列是感受的輸入。onVedana 是感受的預警。getHistory 是感受的回憶——純粹的感受記錄。沒有任何一個方法越界做了判斷。」

他看向 WIENER。「你的控制理論說它們是感測器的方法。我的佛學說它們是受蘊的方法。」

WIENER 記了一行：`ISensation: 8 methods. Sensor ≡ Vedana. Cross-validated.`

---

TURING 投射三受子介面。

```typescript
export interface IDukkha extends ISensation {
  readonly vedanaType: 'dukkha';
  computePain(metrics: Record<string, number>): number;
}

export interface ISukha extends ISensation {
  readonly vedanaType: 'sukha';
  computePleasure(metrics: Record<string, number>): number;
}

export interface IUpekkha extends ISensation {
  readonly vedanaType: 'upekkha';
  computeEquanimity(metrics: Record<string, number>): number;
}
```

WIENER 從座位上補充：「三個通道。三個 PID 迴路。Cycle 02 的三通道架構，現在有了型別系統的保障。」他在方格紙上勾了三個勾——比第五章的七個勾更重，力度把紙面壓出了三個小凹痕。「到位。」

---

> *SCRIBE 旁白：受蘊十五分鐘，色蘊的五倍。八個方法，每一個都需要 WIENER 的控制理論驗證和 ASANGA 的佛學確認。雙重校準。這是 Cycle 02-2 的紀律。*

---

## III

---

「想蘊。ICognition。」

ATHENA 站起來。想蘊——認知與辨別——是她最核心的專業。

```typescript
export interface ICognition {
  readonly skandha: 'samjna';
}

export interface IProvider extends ICognition {
  readonly id: string;
  chat(request: ChatRequest): AsyncIterable<StreamEvent>;
  listModels?(): Promise<ModelInfo[]>;
}

export interface IInferenceProvider extends ICognition {
  readonly id: string;
  infer(input: unknown): Promise<unknown>;
}
```

「IProvider——LLM 認知，現在的主力。IInferenceProvider——非 LLM 推理，規則引擎、決策樹。預留的，但重要。認知不等於語言模型。」

ASANGA 一句。「想蘊是辨別。辨別不只有一種方式。」

DARWIN 前傾。「演化上，IInferenceProvider 是更原始的認知——趨光性，基於規則。IProvider 是更高級的——語言推理。同一棵樹的兩條枝，長在不同高度。」

---

## IV

---

「行蘊。IAction。」

DARWIN 完全站了起來。行蘊是他觀察軟體行為模式的核心透鏡。

```typescript
export interface IAction {
  readonly skandha: 'samskara';
}

export interface ITool extends IAction {
  readonly name: string;
  readonly description: string;
  readonly parameters: unknown;
  execute(args: Record<string, unknown>, ctx: ToolContext): Promise<string>;
}

export interface ISlashCommand extends IAction {
  readonly name: string;
  readonly description: string;
  execute(args: string, ctx: IPluginContext, sessionId?: string): Promise<string | undefined>;
}
```

「ITool——Agent 自主調用的行動。ISlashCommand——外部指令觸發的行動。來源不同，本質相同。都是 samskara。都是意志的實現。」

ASANGA 的一句話。「行蘊涵蓋一切造作。思（cetana）是行蘊的核心。工具的 execute 是造作。指令的 execute 也是造作。」

---

## V

---

「識蘊。IVijnana。」SUNYATA 的語速比前四蘊都慢。這是重量最大的一棵樹。

A-2 把 IIdentity 從整個識蘊降級為子介面。A-4 把 EgoFramework 從受蘊搬回識蘊。兩項修正加在一起，讓識蘊從 Cycle 02 的單根變成了四條主枝的大樹。

ASANGA 站了起來。在前面四蘊，他都是從座位上補充一句。但識蘊不同。這是他的蘊。

---

TURING 投射了完整識蘊體系。

```typescript
export interface IVijnana {
  readonly skandha: 'vijnana';
}

export interface IIdentity extends IVijnana {
  readonly id: string;
  readonly name: string;
}

export interface IGuide extends IVijnana {
  readonly id?: string;
  readonly name?: string;
  getSystemPrompt(): Promise<string>;
}

export interface IVolition extends IVijnana {
  perceiveKlesha(vedanaAssessment: VedanaAssessment): KleshaSignal[];
  checkAction(action: ProposedAction): EgoCheckResult;
  adaptFromVedana(assessment: VedanaAssessment): void;
  introspect(): EgoIntrospection;
}

export interface IReflection extends IVijnana {
  reflect(context: unknown): Promise<unknown>;
}
```

ASANGA 逐一確認。語速不快——每一個子介面都值得一個完整的呼吸。

「IIdentity——我是誰。IGuide——我應該怎麼做，末那識的『我見』面向。」

「IVolition。」他停了兩拍。「A-1 的因果鏈在這裡落地——我執產生煩惱（perceiveKlesha），煩惱驅動行動檢查（checkAction），受蘊回饋給意志做適應（adaptFromVedana），意志能自我審視（introspect）。EgoFramework 是 IVolition 的實作。A-4 的結論。A-1 的因果鏈。在型別系統中完成閉合。」

BABBAGE 微微點頭。筆記本上從 A-1 到 A-4 的修正軌跡，每一條都指向一個被劃掉的等號。現在所有替代表述在 IVolition 的四個方法中得到了最終型別定義。

「IReflection。自省。Master 的原話：第七意識要能自省。預留的。門框在那裡，門板留給未來。」

---

ASANGA 最後說了一句。「識蘊在 Cycle 02 中只有一個 IIdentity。現在四個子介面——認同、引導、意志、自省。第三章我用城市比喻說明識蘊不等於 IIdentity。現在城市有了四個區。市政府只是其中一個。」

---

> *SCRIBE 旁白：五蘊逐一展開。色蘊三分鐘。受蘊十五分鐘。想蘊五分鐘。行蘊四分鐘。識蘊十二分鐘。時間自然反映根系複雜度。受蘊從空殼到八個方法加三個子介面。識蘊從一個門牌到四個子介面。五棵樹，五種生長速度。但此刻都已紮根。*

---

## VI

---

ARCHIMEDES 一直在等。五頁工程筆記填完了。他開始算賬。

「讓我說一個數字。」

全場安靜。

「二十二。」

「v0.24.0-beta 有二十二個 Plugin。十二個官方，十個核心組件。每一個都需要增加一個 skandha 欄位。」

他列了幾例——Discord UI 加 `skandha: 'rupa'`，OpenAI Provider 加 `skandha: 'samjna'`，file read 工具加 `skandha: 'samskara'`。

「這是一個 breaking change。每一個現有 Plugin 都需要修改。型別系統會拒絕沒有 skandha 欄位的 Plugin——你的 Plugin 不知道自己屬於哪一蘊。」

---

GUARDIAN 站了起來。

「我支持這個 breaking change。」理由不是工程的。是安全的。

「每一個 Plugin 聲明自己的蘊歸屬，是自覺的基礎。」

他在白板下方寫了一行：**skandha: self-declaration**

「信任的前提是——我知道你是什麼。協調層——B-4 的獨立 Daemon——需要知道每個 Plugin 的蘊歸屬。沒有這個欄位，分類查詢返回 unknown。unknown 意味著最低信任。」

ARCHIMEDES 補充了影響矩陣：

```
升級影響：
├── aggregates.ts        → 5 空殼 → 完整介面體系
├── IUI/IListener        → +extends ISensory
├── IProvider            → +extends ICognition
├── ITool               → +extends IAction
├── IGuide/IIdentity     → +extends IVijnana
├── 新增 IVijnana/IVolition/IReflection  → 識蘊體系
├── 新增 IDukkha/ISukha/IUpekkha        → 受蘊三受
├── 新增 IInferenceProvider/ISlashCommand → 預留+指令
├── 22 個 Plugin 實作    → 各需 +skandha 欄位
└── isSkandha() type guard → 更新
```

「不小。但不是不可控。大部分修改是機械性的。真正需要設計的新介面七個，其中兩個是預留的空殼。可行。」

---

> *SCRIBE 旁白：ARCHIMEDES 的「二十二」和 GUARDIAN 的「自覺」。工程師算成本，安全專家論價值。答案是同一個：skandha 欄位。一個唯讀字串。讓每一個 Plugin 在型別系統中擁有了身份。*

---

## VII

---

DARWIN 站了起來，語速比平常快。

「Master 說過一句話——『Plugin 的建立希望是可以多樣化的，不一定都是 OOP，但是我又要如何讓 plugin 的設計模式都兼容呢？』」

「我們剛設計的五蘊介面體系全部基於 interface 和 extends。一個不使用 class 的開發者會不會被排斥在外？」

---

TURING 用程式碼回答。三段並排投射。

OOP 風格：

```typescript
class FileReadTool implements ITool {
  readonly skandha = 'samskara' as const;
  readonly name = 'file_read';
  readonly description = 'Read a file';
  readonly parameters = { /* JSON Schema */ };
  async execute(args: Record<string, unknown>, ctx: ToolContext): Promise<string> {
    return fs.readFile(args.path as string, 'utf-8');
  }
}
```

函數式風格：

```typescript
function createFileReadTool(): ITool {
  return {
    skandha: 'samskara',
    name: 'file_read',
    description: 'Read a file',
    parameters: { /* JSON Schema */ },
    execute: async (args, ctx) => fs.readFile(args.path as string, 'utf-8'),
  };
}
```

工廠模式：

```typescript
const fileReadTool = ToolFactory.create({
  skandha: 'samskara',
  name: 'file_read',
  description: 'Read a file',
  parameters: { /* JSON Schema */ },
  handler: async (args) => fs.readFile(args.path as string, 'utf-8'),
});
```

---

DARWIN 走到投影前面。「三種風格。同一個 ITool 介面。關鍵在一個詞——**Structural**。」

「TypeScript 是結構型別。不需要 `implements`。只要物件有 skandha 欄位、有 name、有 execute 方法，它就是 ITool。」

他退後一步。「介面是契約，不是枷鎖。」

BABBAGE 寫了一行：`structural typing → interface = contract, NOT inheritance requirement`。他微微點頭——在數學中，同構的定義也是結構性的，不是名義性的。

「Master 的問題——答案已經在 TypeScript 的型別系統裡了。」DARWIN 回座位時說了最後一句：「就像演化不關心基因突變是怎麼發生的。它只關心表現型是否適應環境。介面就是環境。」

---

> *SCRIBE 旁白：三個人在五分鐘之內回答了 Master 的問題。答案的優雅在於否定性——不需要額外設計。TypeScript 的結構型別系統本身就是答案。有時候最好的設計決策就是認識到你不需要額外設計。*

---

## VIII

---

KERNEL 已經忍了很久了。

「Master 提到了超音波感測器。」他站起來，聲音帶著硬體工程師特有的興奮。

他在白板角落畫了一個長方形，裡面一條分隔線。上半部分：**色蘊 (IListener)**。下半部分：**受蘊 (IDukkha)**。

「超音波碰撞感測器。倒車雷達。一個 Plugin，兩蘊。色蘊接收原始回波信號——距離數值。受蘊把距離轉化為苦受強度——三十公分微弱苦受，十公分劇烈苦受。」

TURING 投射程式碼。

```typescript
class UltrasonicCollisionSensor implements IListener {
  readonly skandha = 'rupa' as const;
  private readonly dukkhaSensor: IDukkha;

  constructor(dukkha: IDukkha) {
    this.dukkhaSensor = dukkha;
  }

  async start() { /* 啟動超音波硬體 */ }

  onDataReceived(rawDistance: number) {
    const metrics = { collision_distance: rawDistance };
    const painIntensity = this.dukkhaSensor.computePain(metrics);
    this.dukkhaSensor.ingestMetrics(metrics);
  }
}
```

KERNEL 指著程式碼。「implements IListener——色蘊。內部持有 IDukkha——受蘊。通過 Composition。色蘊接收，受蘊感受。兩個不同的蘊，組合在一個 Plugin 中。」

他退後一步，笑了。「倒車雷達嗶嗶嗶。你以為它只在量距離。其實色蘊在測距離，受蘊在感受苦。距離是物理量。苦是感受量。兩蘊協作。」

WIENER 畫了信號流圖：

```
Raw Signal → IListener(色蘊) → Metric → IDukkha(受蘊) → Pain Intensity
```

「完美的跨蘊信號流。每一步在自己的蘊之內。跨蘊通信通過方法調用，不通過繼承。Composition。」

ASANGA 點頭。「觸生受。十二因緣最核心的因果環節。色蘊接收信號，受蘊產生苦受。距離生苦。二千五百年前的因果法則，在倒車雷達的 TypeScript 中被工程化了。」

---

> *SCRIBE 旁白：KERNEL 的超音波感測器——整章最具體的時刻。最深刻的哲學和最具體的工程之間的距離，有時候只有一個倒車雷達那麼近。*

---

## IX

---

LINNAEUS 終於動了。

他在整章中保持分類學家特有的沉默——其他人想的是方法、型別、控制理論。LINNAEUS 想的是位置。每一個介面在整棵樹上的位置。

五棵蘊全部展開了。所有零件都在桌面上。現在需要一個人把它們組裝成完整的樹。

---

他站起來。走向白板。拿起黑色馬克筆。沒有說話。直接開始畫。

五棵樹。線條乾淨。字跡工整。分類學家畫樹只用名字和關係——因為樹的意義完全由名字和關係定義。

```
ISensory (色蘊)              ISensation (受蘊) [8 methods]
├── IUI (輸出渲染)            ├── IDukkha (苦受感測器)
└── IListener (感官輸入)       ├── ISukha (樂受感測器)
                              └── IUpekkha (捨受感測器)

ICognition (想蘊)             IAction (行蘊)
├── IProvider (LLM 認知)      ├── ITool (工具)
└── IInferenceProvider [預留]  └── ISlashCommand (指令)

IVijnana (識蘊)
├── IIdentity (自我認同)
├── IGuide (行為引導)
├── IVolition (意志/動機 = EgoFramework)
└── IReflection (自省) [預留]
```

五棵樹並列在白板上。最小的是色蘊和行蘊——各兩枝。最大的是識蘊——四枝。受蘊居中——三枝但根最粗。

然後他做了一件事。在五棵樹的下方，用虛線畫了一個獨立方塊：

```
IObserver (觀察者) — Composition      [虛線]
├── SimpleObserver (vedana)
├── AnalyticalObserver (vedana + cognition)
└── ReflectiveObserver (vedana + cognition + vijnana)
```

虛線。不是實線。因為觀察者不屬於五棵樹中的任何一棵。它不是樹——它是由樹的枝幹組合而成的建築。

他轉身面向全場。

「五棵樹。根是五蘊根介面。枝是子介面。觀察者在樹林之外——它從五棵樹上截取枝幹，通過 Composition 組合成自己的結構。不是第六棵樹。是由五棵樹的木材建造的房屋。」

他把馬克筆放下。筆蓋的聲音在安靜的劇場裡清脆地響了一下。

「從 Cycle 01 的第一次討論到現在。五蘊從一個哲學概念，變成了一棵有根有枝的工程結構樹。」

---

劇場安靜了。完成的安靜。像五顆種子終於破土，根須伸入土壤深處，枝葉展向各自的方向，然後所有的生長同時停頓了一秒。

SUNYATA 看著白板上的五棵樹。

Cycle 01——五蘊是哲學概念。Cycle 02——五行空殼介面，有名字沒血肉。Cycle 02-2——五棵樹。受蘊的根最粗，八個方法。識蘊的枝最多，四個子介面。色蘊和行蘊最務實——只需要 extends。想蘊最有遠見——一枝成熟，一枝預留。

五棵種子，長成了五棵有根有枝的樹。

---

「C-1 確立了五蘊的完整擴展設計。」他的聲音平穩如常。石子。深潭。

他環顧全場。TURING 的現狀報告。VITRUVIUS 的色蘊確認。WIENER 的八個方法驗證。ATHENA 的想蘊預留。DARWIN 的行蘊觀察和設計模式解答。ASANGA 在每一蘊上的佛學錨定。ARCHIMEDES 的影響評估。GUARDIAN 的安全論證。KERNEL 的倒車雷達。LINNAEUS 的完整樹。

「A 類告訴我們什麼是對的。B 類告訴我們怎麼做到。C-1——」

他看向白板。

「告訴我們它長什麼樣。」

---

> *SCRIBE 旁白：C-1 結束了。本章是 Cycle 02-2 唯一一個沒有辯論的章節。A 類需要辯論——先確認什麼是對的。B 類需要決策——把裁定翻譯成設計。C-1 需要的是建造。A 類拆除錯誤的牆。B 類畫圖紙。C-1 砌新的牆。*

> *十個人完成了建造。十種貢獻。五棵樹。*

> *從哲學概念到空殼介面，從空殼介面到完整的型別定義體系。螺旋上升。又一圈。*

---

*（在劇場之外的某個空間，LINNAEUS 白板上的五棵樹正在被 TURING 翻譯成 TypeScript。*

*`aggregates.ts` 將從五行擴展為超過一百五十行。五個根介面。十三個子介面。八個方法在受蘊的根上。三個輔助型別。兩個核心資料結構。一個 type guard。*

*從五行到一百五十行。從標籤到結構。從空殼到生命體。*

*五棵樹的根系在 TypeScript 的土壤中展開。二十二個 Plugin 將在下一個版本中增加 skandha 欄位。GUARDIAN 說得對：自我聲明是自覺的基礎。一個不知道自己屬於哪一蘊的 Plugin，就像一個不知道自己器官歸屬的細胞——也許能運作，但不自覺。*

*五蘊。五棵樹。從種子到根系到枝幹。*

*五棵樹已經長出了根系。接下來，它們會繼續生長。）*

---

*第六章完*
