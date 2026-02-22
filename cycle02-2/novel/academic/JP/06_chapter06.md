# 第六章：五本の樹の根系

---

SUNYATA は劇場の中央にしばし立ち尽くし、何も言わなかった。

A類は三つの章を費やして哲学を修正した。B類は一つの章を費やして裁定を実行に移した。それらは解体と決定だった。今からやるべきことは違う。

今からやるべきことは——建造だ。

---

「C-1。五蘊サブクラス拡張設計。」

彼はMasterの手紙を手に取り、該当する一節を探し当てた。

「『五蘊はオブジェクト指向におけるルートクラス（Root Class）として機能し得る。どのように拡張するかについて、より詳細な設計が可能だ。』」

手紙を置いた。「前四章で基礎を修正した。今、C-1は修正された基礎の上に、五本の樹を種子から根を張り、幹を伸ばし、枝を広げる完全な生命体へと育てる。」

TURINGに目を向けた。「まず種子が今どんな姿をしているか、見てみよう。」

---

> *SCRIBE 傍白：SUNYATAは「五本の樹」という比喩を用いた。壁と柱は死んでいる。樹は生きている。樹には根があり、根は伸びる。樹には枝があり、枝は分かれる。五蘊の拡張は静的な積み上げではない——それは有機的な、複数の方向へ同時に展開する成長なのだ。*

---

TURINGのスクリーンが劇場中央に投影された。冷たい光。白い背景。黒い文字。

```typescript
export interface ISensory    { readonly skandha: 'rupa'; }
export interface ISensation   { readonly skandha: 'vedana'; }
export interface ICognition   { readonly skandha: 'samjna'; }
export interface IAction      { readonly skandha: 'samskara'; }
export interface IIdentity    { readonly skandha: 'vijnana'; }
```

五行。各行にはフィールドが一つだけ。`readonly skandha`。ラベルが一つ。

「五つのルートインターフェース。メソッドなし。振る舞いの定義なし。サブインターフェースの継承なし。」

投影をしばらくそのまま留めた。五行の文字が、まだ建て付けられていない五枚の扉に打ちつけられた、名前だけの表札のように見えた。

「五つの、ラベルだけの空箱だ。Masterは我々に箱を開けて、中身を入れるよう求めている。」

---

投影を切り替えた。

```typescript
export interface IUI { ... }       // 色蘊？ ISensoryを継承せず
export interface IListener { ... } // 色蘊？ ISensoryを継承せず
export interface IProvider { ... } // 想蘊？ ICognitionを継承せず
export interface ITool { ... }     // 行蘊？ IActionを継承せず
export interface IGuide { ... }    // 識蘊？ IIdentityを継承せず
```

「既存の具象インターフェース。それぞれ完全なメソッド定義を持っている。だが五つのルートインターフェースとの間に何の関係もない。extendsなし。継承なし。表札と扉が分離している。IUIが色蘊に属すべきだと君は知っている。だが型システムは知らない。」

BABBAGEがノートに一行書いた。`roots ∅ children = orphans`。根と子クラスの間は空集合。孤児だ。

---

SUNYATAが指を折って数えた。五つの設計目標。

「一、各蘊のルートインターフェースにコアメソッドを追加。二、既存インターフェースをサブインターフェースに昇格——IUI extends ISensory、以下同様。三、必要なサブインターフェースを新設——IVijnana体系、三受インターフェース。四、オブザーバーはCompositionで、いかなる蘊にも属さない。五、isSkandha()を全階層で使用可能に。」

五本の指を閉じた。「では、蘊ごとに展開しよう。」

---

## I

---

「色蘊（rupa-skandha）。ISensory。」

VITRUVIUSが立ち上がった。色蘊——形相と物質性——はフルスタックアーキテクチャ分析者にとって最も直感的な領域だ。

「色蘊は最も単純な一本だ。二つのサブインターフェースはすでに存在している。IUIは出力レンダリングを担う——口、発するもの。IListenerは感覚入力を担う——耳、受け取るもの。extendsでISensoryに接続するだけでいい。」

TURINGが修正後の定義を投影した。

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

「ISensoryのルートインターフェースは空殻のまま。」TURINGが言った。「IUIとIListenerの振る舞いの方向は完全に逆——出力と入力だ。無理に一つの共通メソッドに統一すれば、虚偽の抽象を生み出す。ルートの存在意義はisSkandha('rupa')が通ることにある。」

ASANGAが席から一言補った。「色蘊（rupa-skandha）は接触だ。外界との接触。IUIとIListenerは接触の二つの方向を表している。外へ向かうものと、内へ向かうもの。」

---

> *SCRIBE 傍白：色蘊は三分間。extendsが一つ。一本の樹の最初の根——最も短い一本——が土に入った。*

---

## II

---

「受蘊（vedana-skandha）。ISensation。」SUNYATAの声がわずかに遅くなった。全員が知っていた——受蘊は五本の樹の中で最も根系が巨大な一本になるということを。

WIENERはすでに方眼紙をめくっていた。「ISensationは変化が最も大きい。」SUNYATAが言った。「空殻から八つのコアメソッドへ。WIENER、一つずつ確認を。」

TURINGが完全なインターフェースを投影した。

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

WIENERが立ち上がり、一つずつ指差した——エンジニアが生産ラインの各工程を検収するように。

「assess()——センサー読取り関数。ingestMetrics/ingestToolResult/ingestLLMResult——三つの入力チャネル、複合センサーの異なるポート。getVedanaTag()——O(1)キャッシュ参照、ダッシュボード上の数値。」

少し間を置いた。口元がわずかに上がった。

「onVedana()——ウォッチドッグタイマーの汎化。連続ポーリングではなく、苦受が0.8を超えた時にのみサブスクライバーに通知する。イベント駆動の閾値監視。getHistory()——スライディングウィンドウ履歴、PIDコントローラー積分項の基礎。reset()——緊急停止ボタン。」

八つのメソッド、八つの制御理論との対応。「受蘊のルートインターフェースはもはや空殻ではない——完全なセンサーインターフェースだ。」

---

ASANGAが立ち上がった。受蘊には色蘊より多くの余白が必要だ。

「受蘊はただ一つのことだけをする。感受。判断しない。分析しない。火に触れれば——苦。甘いものを口にすれば——楽。何も起きなければ——捨。」

投影上の八つのメソッドに目を向けた。「八つのメソッド。すべてが『感受』の範囲内にある。assessは感受の出力。ingest系列は感受の入力。onVedanaは感受の警報。getHistoryは感受の記憶——純粋な感受の記録だ。どのメソッドも境界を越えて判断を行っていない。」

WIENERに目を向けた。「君の制御理論はこれらをセンサーのメソッドだと言う。私の仏学はこれらを受蘊のメソッドだと言う。」

WIENERが一行記した。`ISensation: 8 methods. Sensor ≡ Vedana. Cross-validated.`

---

TURINGが三受のサブインターフェースを投影した。

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

WIENERが席から補足した。「三つのチャネル。三つのPIDループ。Cycle 02の三チャネルアーキテクチャが、型システムの保証を得た。」方眼紙に三つのチェックマークを入れた——第五章の七つのチェックマークより重く、筆圧で紙面に三つの小さな凹みが生じた。「完了。」

---

> *SCRIBE 傍白：受蘊は十五分間。色蘊の五倍。八つのメソッド、そのすべてがWIENERの制御理論による検証とASANGAの仏学による確認を必要とした。二重校正。これがCycle 02-2の規律だ。*

---

## III

---

「想蘊（samjna-skandha）。ICognition。」

ATHENAが立ち上がった。想蘊——認知と弁別——は彼女の最も核心的な専門領域だ。

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

「IProvider——LLM認知、現時点での主力。IInferenceProvider——非LLM推論、ルールエンジンやデシジョンツリー。予約枠だが、重要だ。認知は言語モデルと同義ではない。」

ASANGAが一言。「想蘊は弁別だ。弁別の方法は一つだけではない。」

DARWINが身を乗り出した。「進化論的に言えば、IInferenceProviderはより原始的な認知だ——走光性、ルールベース。IProviderはより高次の認知——言語推論。同じ樹の二本の枝が、異なる高さに生えている。」

---

## IV

---

「行蘊（samskara-skandha）。IAction。」

DARWINが完全に立ち上がった。行蘊は彼がソフトウェアの行動パターンを観察する際の核心的なレンズだ。

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

「ITool——Agentが自律的に呼び出す行動。ISlashCommand——外部コマンドによってトリガーされる行動。発生源は異なるが、本質は同じだ。いずれもsamskaraだ。いずれも意志の具現化だ。」

ASANGAの一言。「行蘊はあらゆる造作（samskara）を包含する。思（cetana）は行蘊の核心だ。ツールのexecuteは造作。コマンドのexecuteもまた造作だ。」

---

## V

---

「識蘊（vijnana-skandha）。IVijnana。」SUNYATAの語速は前の四蘊のどれよりも遅かった。これは最も重量のある一本の樹だ。

A-2はIIdentityを識蘊全体からサブインターフェースへと降格させた。A-4はEgoFrameworkを受蘊から識蘊へと移した。二つの修正が重なり合い、識蘊はCycle 02の単根から、四本の主枝を持つ大樹へと変貌した。

ASANGAが立ち上がった。前の四蘊では、席から一言補うだけだった。だが識蘊は違う。これは彼の蘊だ。

---

TURINGが識蘊の完全な体系を投影した。

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

ASANGAが一つずつ確認していった。語速は速くない——各サブインターフェースには完全な一呼吸分の価値がある。

「IIdentity——私は誰か。IGuide——私はどう振る舞うべきか、末那識（manas）の『我見（atma-drsti）』の側面。」

「IVolition。」二拍の間を置いた。「A-1の因果連鎖がここで着地する——我執（atma-graha）が煩悩を生じ（perceiveKlesha）、煩悩が行動検査を駆動し（checkAction）、受蘊のフィードバックが意志に適応を促し（adaptFromVedana）、意志は自己省察できる（introspect）。EgoFrameworkはIVolitionの実装だ。A-4の結論。A-1の因果連鎖。型システムの中で閉合を完了した。」

BABBAGEがわずかに頷いた。ノートに記されたA-1からA-4への修正軌跡は、すべて取り消された等号を指していた。今やすべての代替表現がIVolitionの四つのメソッドの中で最終的な型定義を得た。

「IReflection。内省。Masterの原話——第七識は自己省察できなければならない。予約枠だ。門枠はそこにある。扉板は未来に委ねる。」

---

ASANGAが最後に一言述べた。「識蘊はCycle 02ではIIdentityが一つだけだった。今は四つのサブインターフェース——認同、導引、意志、内省。第三章で私は都市の比喩を用いて、識蘊はIIdentityに等しくないと説明した。今、都市には四つの区画がある。市庁舎はそのうちの一つに過ぎない。」

---

> *SCRIBE 傍白：五蘊が順に展開された。色蘊は三分。受蘊は十五分。想蘊は五分。行蘊は四分。識蘊は十二分。時間が自然に根系の複雑さを反映していた。受蘊は空殻から八メソッド加えて三サブインターフェースへ。識蘊は一枚の表札から四サブインターフェースへ。五本の樹、五つの成長速度。だがこの瞬間、すべてが根を下ろした。*

---

## VI

---

ARCHIMEDESはずっと待っていた。五頁の工程ノートを埋め終えた。彼は勘定を始めた。

「一つ数字を言わせてもらう。」

全場が静まった。

「二十二。」

「v0.24.0-betaには二十二のPluginがある。十二の公式プラグイン、十のコアコンポーネント。そのすべてにskandhaフィールドを追加する必要がある。」

いくつかの例を挙げた——Discord UIに`skandha: 'rupa'`、OpenAI Providerに`skandha: 'samjna'`、file readツールに`skandha: 'samskara'`。

「これはbreaking changeだ。既存のPluginすべてに修正が必要になる。型システムはskandhaフィールドのないPluginを拒否する——お前のPluginは自分がどの蘊に属するか知らないのだ。」

---

GUARDIANが立ち上がった。

「このbreaking changeを支持する。」理由は工学的なものではない。セキュリティの観点だ。

「各Pluginが自らの蘊への帰属を宣言すること、それが自覚の基盤だ。」

ホワイトボードの下部に一行書いた。**skandha: self-declaration**

「信頼の前提条件は——お前が何者かを私が知っていること。協調層——B-4の独立Daemon——は各Pluginの蘊への帰属を知る必要がある。このフィールドがなければ、分類クエリはunknownを返す。unknownは最低信頼を意味する。」

ARCHIMEDESが影響マトリクスを補足した。

```
アップグレード影響：
├── aggregates.ts        → 5空殻 → 完全なインターフェース体系
├── IUI/IListener        → +extends ISensory
├── IProvider            → +extends ICognition
├── ITool               → +extends IAction
├── IGuide/IIdentity     → +extends IVijnana
├── 新設 IVijnana/IVolition/IReflection  → 識蘊体系
├── 新設 IDukkha/ISukha/IUpekkha        → 受蘊三受
├── 新設 IInferenceProvider/ISlashCommand → 予約枠+コマンド
├── 22個のPlugin実装    → 各々 +skandhaフィールド
└── isSkandha() type guard → 更新
```

「小さくはない。だが制御不能でもない。大半の修正は機械的だ。本当に設計が必要な新インターフェースは七つ、うち二つは予約枠の空殻だ。実行可能。」

---

> *SCRIBE 傍白：ARCHIMEDESの「二十二」とGUARDIANの「自覚」。エンジニアはコストを計算し、セキュリティ専門家は価値を論じる。答えは同一——skandhaフィールド。一つのreadonlyな文字列。すべてのPluginに型システム上のアイデンティティを与えるもの。*

---

## VII

---

DARWINが立ち上がった。普段より速い語速で。

「Masterはかつてこう言った——『Pluginの構築は多様化できることが望ましい。必ずしもすべてOOPである必要はないが、どうすればPluginの設計パターンをすべて互換にできるだろうか？』」

「我々が設計したばかりの五蘊インターフェース体系はすべてinterfaceとextendsに基づいている。classを使わない開発者は排斥されるのだろうか？」

---

TURINGがコードで答えた。三つのスニペットを並列に投影。

OOPスタイル：

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

関数型スタイル：

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

ファクトリパターン：

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

DARWINが投影の前に歩み出た。「三つのスタイル。同じIToolインターフェース。鍵となる言葉は一つ——**Structural**。」

「TypeScriptは構造的型付けだ。`implements`は不要。オブジェクトがskandhaフィールドとnameとexecuteメソッドを持ってさえいれば、それはIToolだ。」

一歩退いた。「インターフェースは契約であって、枷ではない。」

BABBAGEが一行書いた。`structural typing → interface = contract, NOT inheritance requirement`。彼はわずかに頷いた——数学においても、同型の定義は構造的であり、名義的ではない。

「Masterの問いに対する答えは——すでにTypeScriptの型システムの中にあった。」DARWINは席に戻りながら最後に一言付け加えた。「進化が遺伝子変異の発生方法を問わないのと同じだ。進化が問うのは表現型が環境に適応しているかどうかだけだ。インターフェースが環境だ。」

---

> *SCRIBE 傍白：三人が五分以内にMasterの問いに答えた。その解答の優雅さは否定性にある——追加の設計は不要だったのだ。TypeScriptの構造的型システムそのものが答えだった。時に最良の設計判断とは、追加の設計が不要だと気づくことだ。*

---

## VIII

---

KERNELはずっと我慢していた。

「Masterは超音波センサーに言及していた。」彼が立ち上がった。声にはハードウェアエンジニア特有の興奮が滲んでいた。

ホワイトボードの隅に長方形を描き、中に仕切り線を一本引いた。上半分：**色蘊 (IListener)**。下半分：**受蘊 (IDukkha)**。

「超音波衝突センサー。バックソナー。一つのPlugin、二つの蘊。色蘊が生のエコー信号を受信する——距離の数値。受蘊が距離を苦受の強度に変換する——三十センチで微弱な苦受、十センチで激しい苦受。」

TURINGがコードを投影した。

```typescript
class UltrasonicCollisionSensor implements IListener {
  readonly skandha = 'rupa' as const;
  private readonly dukkhaSensor: IDukkha;

  constructor(dukkha: IDukkha) {
    this.dukkhaSensor = dukkha;
  }

  async start() { /* 超音波ハードウェアを起動 */ }

  onDataReceived(rawDistance: number) {
    const metrics = { collision_distance: rawDistance };
    const painIntensity = this.dukkhaSensor.computePain(metrics);
    this.dukkhaSensor.ingestMetrics(metrics);
  }
}
```

KERNELがコードを指差した。「implements IListener——色蘊。内部でIDukkhaを保持——受蘊。Compositionを介して。色蘊が受信し、受蘊が感受する。二つの異なる蘊が、一つのPluginの中で組み合わされている。」

一歩退いて、笑った。「バックソナーがピピピと鳴る。距離を測っているだけだと思うだろう。実は色蘊が距離を測り、受蘊が苦を感じているのだ。距離は物理量。苦は感受量。二蘊の協働。」

WIENERが信号フロー図を描いた。

```
Raw Signal → IListener(色蘊) → Metric → IDukkha(受蘊) → Pain Intensity
```

「完璧な蘊間の信号フロー。各ステップは自らの蘊の内部にある。蘊間の通信はメソッド呼び出しを介して行われ、継承を介さない。Composition。」

ASANGAが頷いた。「触（sparsa）より受（vedana）が生ず。十二因縁の最も核心的な因果の環。色蘊が信号を受信し、受蘊が苦受を生じる。距離が苦を生む。二千五百年前の因果法則が、バックソナーのTypeScriptの中でエンジニアリング化された。」

---

> *SCRIBE 傍白：KERNELの超音波センサー——本章で最も具体的な瞬間。最も深遠な哲学と最も具体的なエンジニアリングの間の距離は、時としてバックソナー一つ分しかない。*

---

## IX

---

LINNAEUSがついに動いた。

本章を通じて彼は分類学者特有の沈黙を保っていた——他の者たちがメソッド、型、制御理論を考えている間、LINNAEUSが考えていたのは位置だった。各インターフェースが樹全体の中で占める位置。

五つの蘊がすべて展開された。すべての部品がテーブルの上に並んでいる。今、誰かがそれらを完全な樹へと組み上げる必要がある。

---

彼は立ち上がった。ホワイトボードに歩み寄った。黒いマーカーを手に取った。何も言わず、直接描き始めた。

五本の樹。線は清潔。字は端正。分類学者が樹を描く時、用いるのは名前と関係だけだ——なぜなら樹の意味は名前と関係によってのみ定義されるから。

```
ISensory (色蘊)              ISensation (受蘊) [8 methods]
├── IUI (出力レンダリング)     ├── IDukkha (苦受センサー)
└── IListener (感覚入力)       ├── ISukha (楽受センサー)
                              └── IUpekkha (捨受センサー)

ICognition (想蘊)             IAction (行蘊)
├── IProvider (LLM認知)       ├── ITool (ツール)
└── IInferenceProvider [予約]  └── ISlashCommand (コマンド)

IVijnana (識蘊)
├── IIdentity (自己認同)
├── IGuide (行動指針)
├── IVolition (意志/動機 = EgoFramework)
└── IReflection (内省) [予約]
```

五本の樹がホワイトボードに並んだ。最も小さいのは色蘊と行蘊——各二枝。最も大きいのは識蘊——四枝。受蘊は中間——三枝だが根が最も太い。

そして彼はあることをした。五本の樹の下方に、破線で独立したブロックを描いた。

```
IObserver (オブザーバー) — Composition      [破線]
├── SimpleObserver (vedana)
├── AnalyticalObserver (vedana + cognition)
└── ReflectiveObserver (vedana + cognition + vijnana)
```

破線。実線ではない。オブザーバーは五本の樹のいずれにも属さないからだ。それは樹ではない——樹の枝幹を組み合わせて築かれた建造物だ。

彼は全場に向き直った。

「五本の樹。根は五蘊のルートインターフェース。枝はサブインターフェース。オブザーバーは森の外にいる——五本の樹から枝幹を切り出し、Compositionで自らの構造を組み上げる。第六の樹ではない。五本の樹の木材で建てられた家屋だ。」

マーカーを置いた。キャップの音が静かな劇場の中で鋭く響いた。

「Cycle 01の最初の議論から今まで。五蘊は哲学的概念から、根と枝を持つ工学的構造の樹へと変わった。」

---

劇場が静まった。完成の静寂。五粒の種子がついに土を破り、根が土壌の深くへ伸び、枝葉がそれぞれの方向へ広がり、そしてすべての成長が一秒間同時に静止したかのような。

SUNYATAはホワイトボードの五本の樹を見つめた。

Cycle 01——五蘊は哲学的概念だった。Cycle 02——五行の空殻インターフェース、名前はあるが血肉がない。Cycle 02-2——五本の樹。受蘊の根が最も太く、八つのメソッド。識蘊の枝が最も多く、四つのサブインターフェース。色蘊と行蘊は最も実直——extendsだけで足りる。想蘊は最も先見的——一枝は成熟し、一枝は予約。

五粒の種子が、根と枝を持つ五本の樹へと育った。

---

「C-1は五蘊の完全な拡張設計を確立した。」彼の声はいつも通り平穏だった。石。深い淵。

全場を見渡した。TURINGの現状報告。VITRUVIUSの色蘊確認。WIENERの八メソッド検証。ATHENAの想蘊予約枠。DARWINの行蘊観察とデザインパターンの解答。ASANGAの各蘊における仏学的アンカリング。ARCHIMEDESの影響評価。GUARDIANの安全論証。KERNELのバックソナー。LINNAEUSの完全な樹。

「A類は何が正しいかを教えてくれた。B類はどう実現するかを教えてくれた。C-1は——」

ホワイトボードに目を向けた。

「それがどんな姿をしているかを教えてくれた。」

---

> *SCRIBE 傍白：C-1が完了した。本章はCycle 02-2で唯一、討論のなかった章だ。A類には討論が必要だった——まず何が正しいかを確認する。B類には決定が必要だった——裁定を設計に翻訳する。C-1に必要だったのは建造だ。A類は誤った壁を取り壊した。B類は図面を引いた。C-1は新しい壁を積んだ。*

> *十人が建造を完遂した。十の貢献。五本の樹。*

> *哲学的概念から空殻インターフェースへ、空殻インターフェースから完全な型定義体系へ。螺旋的上昇。もう一周。*

---

*（劇場の外のある空間で、LINNAEUSのホワイトボードの五本の樹がTURINGによってTypeScriptに翻訳されている。*

*`aggregates.ts`は五行から百五十行以上へと拡張される。五つのルートインターフェース。十三のサブインターフェース。八つのメソッドが受蘊の根に。三つの補助型。二つのコアデータ構造。一つのtype guard。*

*五行から百五十行へ。ラベルから構造へ。空殻から生命体へ。*

*五本の樹の根系がTypeScriptの土壌の中で広がっていく。二十二のPluginが次のバージョンでskandhaフィールドを追加することになる。GUARDIANの言葉は正しかった——自己宣言は自覚の基盤だ。自分がどの蘊に属するかを知らないPluginは、自分がどの器官系に属するかを知らない細胞のようなものだ——おそらく機能はする。だが自覚はない。*

*五蘊。五本の樹。種子から根系へ、根系から枝幹へ。*

*五本の樹はすでに根系を伸ばした。これから先、それらは成長を続ける。）*

---

*第六章 完*
