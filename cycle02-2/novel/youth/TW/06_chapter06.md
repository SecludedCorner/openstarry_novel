# 第六章：五棵樹的根系

---

SUNYATA 在劇場中央站了片刻，什麼都沒說。

A 類用了三個章節修正哲學。B 類用了一個章節落實裁定。那些是拆解和決策。現在要做的事情不同——現在要建造。

---

「C-1。五蘊子類別擴展設計。」

他拿起 Master 的信：「『五蘊可以做為根本類別（Root Class），要如何擴展，可以做更詳細的安排。』」

「前四章修正了地基。現在，C-1 要在修正過的地基上，把五棵樹從種子長成有根、有幹、有枝的完整生命體。」

---

> *SCRIBE 旁白：SUNYATA 用了「五棵樹」的意象。樹是活的，有根會伸展，有枝會分叉。五蘊的擴展不是靜態堆砌——它是有機的、向多方向同時展開的生長。*

---

TURING 的螢幕投射到劇場中央。

```typescript
export interface ISensory    { readonly skandha: 'rupa'; }
export interface ISensation   { readonly skandha: 'vedana'; }
export interface ICognition   { readonly skandha: 'samjna'; }
export interface IAction      { readonly skandha: 'samskara'; }
export interface IIdentity    { readonly skandha: 'vijnana'; }
```

五行。每行只有一個欄位——一個標籤。

「五個根介面。沒有方法。沒有行為定義。沒有子介面繼承。它們就像五個只有標籤的空盒子。Master 要我們把盒子打開，往裡面放東西。」

---

他切換投影，顯示現有的具體介面——IUI、IListener、IProvider、ITool、IGuide——每個都有完整的方法定義，但和五個根介面之間沒有任何關係。沒有 extends。門牌和門是分開的。

BABBAGE 在筆記本上寫了一行：`roots ∅ children = orphans`。根和子類別之間是空集。孤兒。

---

SUNYATA 用手指計數。五個設計目標。

「一，根介面增加核心方法。二，現有介面升級為子介面。三，新增必要的子介面。四，觀察者用 Composition，不屬於任何蘊。五，isSkandha() 全層級可用。」

「現在，逐蘊展開。」

---

## I

---

「色蘊。ISensory。」

VITRUVIUS 站了起來。「色蘊最簡單。兩個子介面已經存在。IUI 負責輸出渲染——嘴巴，說出去的。IListener 負責感官輸入——耳朵，聽進來的。只需要讓它們 extends ISensory。」

TURING 投射修改後的定義：

```typescript
export interface ISensory {
  readonly skandha: 'rupa';
}

export interface IUI extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
  renderText?(text: string, sessionId?: string): void;
  renderDelta?(delta: string, sessionId?: string): void;
}

export interface IListener extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
}
```

「ISensory 根介面保持空殼。IUI 和 IListener 方向完全相反——輸出和輸入，強行統一會製造虛假的抽象。」

ASANGA 補了一句。「色蘊是接觸——和外境的接觸。IUI 和 IListener 代表接觸的兩個方向。往外的和往內的。」

---

> *SCRIBE 旁白：色蘊三分鐘。一個 extends。最短的一條根入土了。*

---

## II

---

「受蘊。ISensation。」SUNYATA 的聲音微微放慢。所有人都知道受蘊將是根系最龐大的一棵。

TURING 投射完整介面。

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

WIENER 站了起來，逐一點過八個方法。

「assess()——感測器讀數。三個 ingest 方法——不同接口的輸入通道。getVedanaTag()——快取查詢。onVedana()——事件驅動的閾值監測，苦受超過 0.8 才通知。getHistory()——滑動視窗歷史。reset()——緊急停止。」

「受蘊的根介面不再是空殼——它是一個完整的感測器介面。」

---

ASANGA 站起來。「受蘊只做一件事：感受。不判斷，不分析。碰到火——苦。吃到甜——樂。無事發生——捨。八個方法，每一個都在『感受』的範圍內。沒有任何一個方法越界做了判斷。」

他看向 WIENER。「你的控制理論說它們是感測器方法。我的佛學說它們是受蘊方法。同一件事，兩種語言。」

---

TURING 投射三受子介面——IDukkha（苦受）、ISukha（樂受）、IUpekkha（捨受），各自繼承 ISensation，各有一個 compute 方法。

WIENER 補充：「三個通道。三個 PID 迴路。Cycle 02 的三通道架構，現在有了型別系統的保障。」他在方格紙上重重勾了三個勾。「到位。」

---

> *SCRIBE 旁白：受蘊十五分鐘，色蘊的五倍。八個方法需要控制理論驗證和佛學確認。雙重校準——這是 Cycle 02-2 的紀律。*

---

## III

---

「想蘊。ICognition。」

ATHENA 站起來。

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

「IProvider——LLM 認知，現在的主力。IInferenceProvider——非 LLM 推理，規則引擎、決策樹。認知不等於語言模型。」

DARWIN 前傾。「演化上，IInferenceProvider 是更原始的認知——趨光性。IProvider 是更高級的——語言推理。同一棵樹的兩條枝。」

---

## IV

---

「行蘊。IAction。」

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

DARWIN 站了起來。「ITool——Agent 自主調用的行動。ISlashCommand——外部指令觸發的行動。來源不同，本質相同。都是意志的實現。」

ASANGA 一句話。「行蘊涵蓋一切造作。工具的 execute 是造作，指令的 execute 也是造作。」

---

## V

---

「識蘊。IVijnana。」SUNYATA 語速比前四蘊都慢。這是最重的一棵樹。

A-2 把 IIdentity 從整個識蘊降級為子介面。A-4 把 EgoFramework 搬回識蘊。兩項修正讓識蘊從單根變成了四枝大樹。

ASANGA 站了起來。前四蘊他都只是從座位上補充一句。識蘊不同——這是他的蘊。

---

TURING 投射完整識蘊體系。

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

ASANGA 逐一確認。

「IIdentity——我是誰。IGuide——我應該怎麼做。」

「IVolition。」他停了兩拍。「A-1 的因果鏈在這裡落地——我執產生煩惱（perceiveKlesha），煩惱驅動行動檢查（checkAction），受蘊回饋給意志做適應（adaptFromVedana），意志能自我審視（introspect）。A-1 到 A-4 的修正，在型別系統中完成閉合。」

「IReflection。自省。預留的。門框在那裡，門板留給未來。」

最後他說：「識蘊在 Cycle 02 中只有一個 IIdentity。現在四個子介面——認同、引導、意志、自省。第三章我用城市比喻說識蘊不等於 IIdentity。現在城市有了四個區。」

---

> *SCRIBE 旁白：五蘊逐一展開。色蘊三分鐘，受蘊十五分鐘，想蘊五分鐘，行蘊四分鐘，識蘊十二分鐘。時間自然反映根系複雜度。五棵樹，五種生長速度，但都已紮根。*

---

## VI

---

ARCHIMEDES 一直在等。五頁工程筆記填完了。

「讓我說一個數字。二十二。」

「v0.24.0-beta 有二十二個 Plugin。每一個都需要增加 skandha 欄位。」

他舉了幾例——Discord UI 加 `skandha: 'rupa'`，OpenAI Provider 加 `skandha: 'samjna'`，file read 工具加 `skandha: 'samskara'`。

「這是 breaking change。型別系統會拒絕沒有 skandha 欄位的 Plugin。」

---

GUARDIAN 站起來。「我支持這個 breaking change。」理由不是工程的，是安全的。

「每個 Plugin 聲明自己的蘊歸屬，是自覺的基礎。協調層需要知道每個 Plugin 的歸屬。沒有這個欄位，分類查詢返回 unknown。unknown 意味著最低信任。」

ARCHIMEDES 補充：「大部分修改是機械性的。真正需要設計的新介面七個，其中兩個是預留空殼。可行。」

---

> *SCRIBE 旁白：ARCHIMEDES 的「二十二」和 GUARDIAN 的「自覺」。工程師算成本，安全專家論價值。答案是同一個：skandha 欄位。一個唯讀字串，讓每個 Plugin 在型別系統中擁有了身份。*

---

## VII

---

DARWIN 站起來，語速比平常快。

「Master 說過——『Plugin 不一定都是 OOP，但要如何讓不同設計模式都兼容？』」

TURING 用三段並排的程式碼回答：OOP 風格用 `class implements ITool`，函數式風格用 `function createTool(): ITool`，工廠模式用 `ToolFactory.create()`。三種風格，同一個 ITool 介面。

DARWIN 解釋關鍵詞——**Structural**。

「TypeScript 是結構型別。不需要寫 `implements`。只要物件有 skandha 欄位、有 name、有 execute 方法，它就是 ITool。介面是契約，不是枷鎖。」

BABBAGE 寫了一行：`structural typing → interface = contract, NOT inheritance requirement`。

「Master 的問題——答案已經在 TypeScript 的型別系統裡了。」

---

> *SCRIBE 旁白：答案的優雅在於否定性——不需要額外設計。有時候最好的設計決策就是認識到你不需要額外設計。*

---

## VIII

---

KERNEL 已經忍了很久了。「Master 提到了超音波感測器。」

他在白板角落畫了一個長方形，上半部分：**色蘊 (IListener)**，下半部分：**受蘊 (IDukkha)**。

「超音波碰撞感測器。倒車雷達。一個 Plugin，兩蘊。色蘊接收原始回波信號——距離數值。受蘊把距離轉化為苦受強度——三十公分微弱苦受，十公分劇烈苦受。」

TURING 投射程式碼——UltrasonicCollisionSensor implements IListener，內部持有 IDukkha。色蘊接收，受蘊感受，通過 Composition 組合在一個 Plugin 中。

KERNEL 笑了。「倒車雷達嗶嗶嗶。你以為它只在量距離。其實色蘊在測距離，受蘊在感受苦。距離是物理量，苦是感受量。兩蘊協作。」

ASANGA 點頭。「觸生受——十二因緣最核心的環節。二千五百年前的因果法則，在倒車雷達的 TypeScript 中被工程化了。」

---

> *SCRIBE 旁白：最深刻的哲學和最具體的工程之間的距離，有時候只有一個倒車雷達那麼近。*

---

## IX

---

LINNAEUS 終於動了。分類學家在整章中保持沉默——其他人想的是方法和型別，他想的是位置。每一個介面在整棵樹上的位置。

五棵蘊全部展開了。現在需要有人把它們組裝成完整的樹。

---

他走向白板，拿起馬克筆，直接開始畫。

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

五棵樹並列在白板上。然後他在下方用虛線畫了一個獨立方塊：

```
IObserver (觀察者) — Composition      [虛線]
├── SimpleObserver (vedana)
├── AnalyticalObserver (vedana + cognition)
└── ReflectiveObserver (vedana + cognition + vijnana)
```

虛線——因為觀察者不屬於五棵樹中的任何一棵。它從五棵樹上截取枝幹，通過 Composition 組合成自己的結構。不是第六棵樹，是由五棵樹的木材建造的房屋。

他放下馬克筆。「從 Cycle 01 到現在。五蘊從哲學概念，變成了有根有枝的工程結構樹。」

---

劇場安靜了。像五顆種子破土，根須伸入土壤，枝葉展向各自的方向。

SUNYATA 看著白板上的五棵樹。

Cycle 01——五蘊是哲學概念。Cycle 02——五行空殼介面。Cycle 02-2——五棵樹。受蘊根最粗，八個方法。識蘊枝最多，四個子介面。色蘊和行蘊最務實——只需要 extends。想蘊最有遠見——一枝成熟，一枝預留。

---

「C-1 確立了五蘊的完整擴展設計。」

「A 類告訴我們什麼是對的。B 類告訴我們怎麼做到。C-1——」

他看向白板。

「告訴我們它長什麼樣。」

---

> *SCRIBE 旁白：C-1 結束了。本章沒有辯論。A 類需要辯論——確認什麼是對的。B 類需要決策——把裁定翻譯成設計。C-1 需要建造。十個人完成了建造，五棵樹。從哲學概念到空殼介面，從空殼介面到完整的型別定義體系。螺旋上升，又一圈。*

---

*（在劇場之外，LINNAEUS 白板上的五棵樹正在被 TURING 翻譯成 TypeScript。*

*`aggregates.ts` 將從五行擴展為超過一百五十行。五個根介面，十三個子介面，八個方法在受蘊的根上。*

*從五行到一百五十行。從標籤到結構。從空殼到生命體。*

*五棵樹的根系在 TypeScript 的土壤中展開。二十二個 Plugin 將增加 skandha 欄位——自我聲明是自覺的基礎。*

*五棵樹已經長出了根系。接下來，它們會繼續生長。）*

---

*第六章完*
