# 第六章：五本の木の根系

---

SUNYATA は劇場の中央にしばらく立ったまま、何も言わなかった。

A 類は三つの章で哲学を修正した。B 類は一つの章で裁定を実行した。それらは解体と意思決定だった。今からやることは違う——今から建造するのだ。

---

「C-1。五蘊サブクラス拡張設計。」

彼は Master の手紙を手に取った。「『五蘊はルートクラス（Root Class）として使える。どう拡張するかについて、より詳細な設計ができる。』」

「前四章で基礎を修正した。今、C-1 では修正された基礎の上に、五本の木を種から根、幹、枝を持つ完全な生命体へと育てる。」

---

> *SCRIBE ナレーション：SUNYATA は「五本の木」というイメージを使った。木は生きている。根は伸び、枝は分かれる。五蘊の拡張は静的な積み重ねではない——有機的で、複数の方向に同時に展開する成長だ。*

---

TURING のスクリーンが劇場の中央に投影された。

```typescript
export interface ISensory    { readonly skandha: 'rupa'; }
export interface ISensation   { readonly skandha: 'vedana'; }
export interface ICognition   { readonly skandha: 'samjna'; }
export interface IAction      { readonly skandha: 'samskara'; }
export interface IIdentity    { readonly skandha: 'vijnana'; }
```

五行。各行にはフィールドが一つだけ——ラベルが一つだけ。

「五つのルートインターフェース。メソッドなし。振る舞いの定義なし。サブインターフェースの継承なし。ラベルだけが入った五つの空の箱のようなものだ。Master は我々に、その箱を開けて中身を入れるよう求めている。」

---

彼は投影を切り替え、既存の具体インターフェース——IUI、IListener、IProvider、ITool、IGuide——を表示した。それぞれ完全なメソッド定義を持っているが、五つのルートインターフェースとの間には何の関係もない。extends がない。表札とドアが分離している。

BABBAGE はノートに一行書いた。`roots ∅ children = orphans`。ルートとサブクラスの間は空集合。孤児だ。

---

SUNYATA は指で数えた。五つの設計目標。

「一、ルートインターフェースにコアメソッドを追加。二、既存インターフェースをサブインターフェースに昇格。三、必要な新しいサブインターフェースを追加。四、観察者は Composition を使い、どの蘊にも属さない。五、isSkandha() が全階層で使用可能に。」

「では、蘊ごとに展開する。」

---

## I

---

「色蘊。ISensory。」

VITRUVIUS が立ち上がった。「色蘊は最もシンプルだ。二つのサブインターフェースはすでに存在する。IUI は出力レンダリングを担当する——口、外に発するもの。IListener は感覚入力を担当する——耳、内に受け取るもの。それらに extends ISensory をつけるだけでいい。」

TURING が修正後の定義を投影した。

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

「ISensory ルートインターフェースは空のまま。IUI と IListener は方向がまったく逆——出力と入力。無理に統一すれば偽りの抽象を作ることになる。」

ASANGA が一言添えた。「色蘊は接触だ——外界との接触。IUI と IListener は接触の二つの方向を表す。外に向かうものと、内に向かうもの。」

---

> *SCRIBE ナレーション：色蘊は三分。一つの extends。最も短い根が土に入った。*

---

## II

---

「受蘊。ISensation。」SUNYATA の声がわずかに遅くなった。全員が受蘊の根系が最も大きくなることを知っていた。

TURING が完全なインターフェースを投影した。

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

WIENER が立ち上がり、八つのメソッドを一つずつ指した。

「assess()——センサー読取値。三つの ingest メソッド——異なる入力チャネル。getVedanaTag()——キャッシュ照会。onVedana()——イベント駆動の閾値監視、苦受が 0.8 を超えた時だけ通知。getHistory()——スライディングウィンドウ履歴。reset()——緊急停止。」

「受蘊のルートインターフェースはもう空殻ではない——完全なセンサーインターフェースだ。」

---

ASANGA が立ち上がった。「受蘊がやることは一つだけだ。感じること。判断もしない、分析もしない。火に触れれば——苦。甘いものを食べれば——楽。何も起きなければ——捨。八つのメソッド、そのどれもが『感じる』の範囲内にある。どのメソッドも範囲を越えて判断を行っていない。」

彼は WIENER を見た。「あなたの制御理論はそれらをセンサーメソッドだと言う。私の仏学はそれらを受蘊メソッドだと言う。同じこと、二つの言語。」

---

TURING が三受サブインターフェース——IDukkha（苦受）、ISukha（楽受）、IUpekkha（捨受）を投影した。それぞれ ISensation を継承し、それぞれに compute メソッドがある。

WIENER が補足した。「三つの通道。三つの PID ループ。Cycle 02 の三通道アーキテクチャが、型システムの保証を得た。」彼は方眼紙に力強く三つのチェックを入れた。「揃った。」

---

> *SCRIBE ナレーション：受蘊は十五分。色蘊の五倍。八つのメソッドには制御理論の検証と仏学の確認が必要だった。二重校正——これが Cycle 02-2 の規律だ。*

---

## III

---

「想蘊。ICognition。」

ATHENA が立ち上がった。

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

「IProvider——LLM 認知、現在の主力。IInferenceProvider——非 LLM 推論、ルールエンジン、デシジョンツリー。認知は言語モデルと等しくない。」

DARWIN が身を乗り出した。「進化の観点から、IInferenceProvider はより原始的な認知だ——走光性。IProvider はより高度な認知——言語推論。同じ木の二本の枝だ。」

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

DARWIN が立ち上がった。「ITool——Agent が自律的に呼び出す行動。ISlashCommand——外部コマンドがトリガーする行動。出所は異なるが、本質は同じだ。どちらも意志の実現だ。」

ASANGA が一言。「行蘊はすべての造作を含む。ツールの execute は造作であり、コマンドの execute もまた造作だ。」

---

## V

---

「識蘊。IVijnana。」SUNYATA の語速は前の四蘊のどれよりも遅かった。これは最も重い木だ。

A-2 で IIdentity を識蘊全体からサブインターフェースに格下げした。A-4 で EgoFramework を識蘊に戻した。二つの修正が識蘊を単根から四枝の大樹に変えた。

ASANGA が立ち上がった。前四蘊では席から一言補足するだけだった。識蘊は違う——これは彼の蘊だ。

---

TURING が識蘊の完全な体系を投影した。

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

ASANGA が一つずつ確認した。

「IIdentity——私は誰か。IGuide——私はどうすべきか。」

「IVolition。」彼は二拍止まった。「A-1 の因果の連鎖がここで着地する——我執が煩悩を生み（perceiveKlesha）、煩悩が行動チェックを駆動し（checkAction）、受蘊のフィードバックが意志に適応をもたらし（adaptFromVedana）、意志が自己を審視できる（introspect）。A-1 から A-4 の修正が、型システムの中で閉じた。」

「IReflection。自省。予約済みだ。ドア枠はそこにある。扉板は未来に委ねる。」

最後に彼は言った。「識蘊は Cycle 02 では IIdentity 一つだけだった。今は四つのサブインターフェース——認同、導引、意志、自省。第三章で私は都市の比喩を使って識蘊は IIdentity に等しくないと言った。今、都市は四つの区画を持った。」

---

> *SCRIBE ナレーション：五蘊が一つずつ展開された。色蘊三分、受蘊十五分、想蘊五分、行蘊四分、識蘊十二分。時間は自然に根系の複雑さを反映した。五本の木、五つの成長速度、だがすべて根を張った。*

---

## VI

---

ARCHIMEDES はずっと待っていた。五ページの工学ノートが埋まった。

「数字を一つ言おう。二十二。」

「v0.24.0-beta には二十二の Plugin がある。そのすべてに skandha フィールドを追加する必要がある。」

彼はいくつか例を挙げた——Discord UI に `skandha: 'rupa'` を追加、OpenAI Provider に `skandha: 'samjna'` を追加、file read ツールに `skandha: 'samskara'` を追加。

「これは breaking change だ。型システムは skandha フィールドのない Plugin を拒否する。」

---

GUARDIAN が立ち上がった。「この breaking change を支持する。」理由は工学的なものではなく、セキュリティ上のものだった。

「各 Plugin が自分の蘊への帰属を宣言することは、自覚の基盤だ。協調層は各 Plugin の帰属を知る必要がある。このフィールドがなければ、分類クエリは unknown を返す。unknown は最低信頼を意味する。」

ARCHIMEDES が補足した。「大部分の修正は機械的だ。本当に設計が必要な新しいインターフェースは七つで、うち二つは予約済みの空殻だ。実行可能だ。」

---

> *SCRIBE ナレーション：ARCHIMEDES の「二十二」と GUARDIAN の「自覚」。エンジニアはコストを計算し、セキュリティ専門家は価値を論じる。答えは同じだ。skandha フィールド。一つの読み取り専用文字列で、各 Plugin が型システムの中でアイデンティティを持つようになった。*

---

## VII

---

DARWIN が立ち上がった。いつもより語速が速い。

「Master はこう言った——『Plugin は必ずしもすべてが OOP とは限らないが、異なるデザインパターンをどうやって互換にするか？』」

TURING が三つの並列コードで答えた。OOP スタイルは `class implements ITool`、関数型スタイルは `function createTool(): ITool`、ファクトリパターンは `ToolFactory.create()`。三つのスタイル、同一の ITool インターフェース。

DARWIN がキーワードを説明した——**Structural**。

「TypeScript は構造的型付けだ。`implements` を書く必要はない。オブジェクトが skandha フィールド、name、execute メソッドを持っていれば、それは ITool だ。インターフェースは契約であり、枷ではない。」

BABBAGE が一行書いた。`structural typing → interface = contract, NOT inheritance requirement`。

「Master の問い——答えはすでに TypeScript の型システムの中にあった。」

---

> *SCRIBE ナレーション：答えの優雅さは否定性にある——追加の設計は必要ない。時として最良の設計判断とは、追加の設計が必要ないと認識することだ。*

---

## VIII

---

KERNEL はずっと我慢していた。「Master は超音波センサーに言及した。」

彼はホワイトボードの隅に長方形を描いた。上半分：**色蘊 (IListener)**、下半分：**受蘊 (IDukkha)**。

「超音波衝突センサー。バック駐車レーダー。一つの Plugin、二蘊。色蘊が生のエコー信号を受信する——距離の数値。受蘊が距離を苦受の強度に変換する——三十センチは微弱な苦受、十センチは激しい苦受。」

TURING がコードを投影した——UltrasonicCollisionSensor implements IListener、内部に IDukkha を保持。色蘊が受信し、受蘊が感じ取り、Composition で一つの Plugin に組み合わさる。

KERNEL が笑った。「バック駐車レーダーのピピピピ。距離を測っているだけだと思っていただろう。実は色蘊が距離を測り、受蘊が苦を感じているのだ。距離は物理量、苦は感受量。二蘊の協働だ。」

ASANGA がうなずいた。「触より受を生ず——十二因縁の最も核心的な環節だ。二千五百年前の因果の法則が、バック駐車レーダーの TypeScript の中で工学化された。」

---

> *SCRIBE ナレーション：最も深遠な哲学と最も具体的な工学の間の距離は、時としてバック駐車レーダー一つ分でしかない。*

---

## IX

---

LINNAEUS がついに動いた。分類学者は本章を通じて沈黙を保っていた——他の人々がメソッドと型を考えている間、彼が考えていたのは位置だ。全体の木における各インターフェースの位置。

五つの蘊がすべて展開された。今、誰かがそれらを完全な木に組み上げる必要がある。

---

彼はホワイトボードに歩み寄り、マーカーを手に取り、そのまま描き始めた。

```
ISensory (色蘊)              ISensation (受蘊) [8 methods]
├── IUI (出力レンダリング)      ├── IDukkha (苦受センサー)
└── IListener (感覚入力)       ├── ISukha (楽受センサー)
                              └── IUpekkha (捨受センサー)

ICognition (想蘊)             IAction (行蘊)
├── IProvider (LLM 認知)      ├── ITool (ツール)
└── IInferenceProvider [予約]  └── ISlashCommand (コマンド)

IVijnana (識蘊)
├── IIdentity (自己認同)
├── IGuide (行動導引)
├── IVolition (意志/動機 = EgoFramework)
└── IReflection (自省) [予約]
```

五本の木がホワイトボードに並んだ。そして彼は下方に破線で独立した四角を描いた。

```
IObserver (観察者) — Composition      [破線]
├── SimpleObserver (vedana)
├── AnalyticalObserver (vedana + cognition)
└── ReflectiveObserver (vedana + cognition + vijnana)
```

破線——なぜなら観察者は五本の木のどれにも属さないからだ。五本の木から枝を切り出し、Composition で自らの構造に組み合わせる。六本目の木ではなく、五本の木の木材で建てられた家だ。

彼はマーカーを置いた。「Cycle 01 から今まで。五蘊は哲学的概念から、根と枝を持つ工学的構造の木に変わった。」

---

劇場が静まった。五つの種子が地を破り、根が土壌に伸び、枝葉がそれぞれの方向に広がるように。

SUNYATA はホワイトボードの五本の木を見つめた。

Cycle 01——五蘊は哲学的概念だった。Cycle 02——五行の空殻インターフェース。Cycle 02-2——五本の木。受蘊の根が最も太く、八つのメソッド。識蘊の枝が最も多く、四つのサブインターフェース。色蘊と行蘊は最も実務的——extends するだけでよかった。想蘊は最も先見性があった——一枝は成熟し、一枝は予約。

---

「C-1 は五蘊の完全な拡張設計を確立した。」

「A 類は教えてくれた。何が正しいかを。B 類は教えてくれた。どう実現するかを。C-1 は——」

彼はホワイトボードを見た。

「それがどんな姿をしているかを教えてくれた。」

---

> *SCRIBE ナレーション：C-1 が終わった。本章に討論はない。A 類には討論が必要だった——何が正しいかを確認するために。B 類には意思決定が必要だった——裁定を設計に翻訳するために。C-1 には建造が必要だった。十人が建造を完成させた。五本の木。哲学的概念から空殻インターフェースへ、空殻インターフェースから完全な型定義体系へ。螺旋上昇、もう一周。*

---

*（劇場の外で、LINNAEUS がホワイトボードに描いた五本の木を TURING が TypeScript に翻訳していた。*

*`aggregates.ts` は五行から百五十行以上に拡張される。五つのルートインターフェース、十三のサブインターフェース、受蘊の根に八つのメソッド。*

*五行から百五十行へ。ラベルから構造へ。空殻から生命体へ。*

*五本の木の根系が TypeScript の土壌で広がっている。二十二の Plugin が skandha フィールドを追加する——自己申告は自覚の基盤だ。*

*五本の木はすでに根系を張った。これから、成長は続く。）*

---

*第六章 了*
