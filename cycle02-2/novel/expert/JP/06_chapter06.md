# 第6章：五本の木の根系

---

SUNYATA は劇場の中央にしばらく立ち、何も語らなかった。

A級の議論には三つの章を費やして哲学を校正した。B級には一つの章を費やして裁定を落とし込んだ。それらは解体と決断のプロセスであった。今、なされるべきことはそれとは異なる。

今は、建造の時であった。

亀裂を補修することではない。境界線を描き直すことでもない。校正された土台の上に、一蘊（いちうん）ずつ、完全な型定義の体系を展開していくこと。A級は何が間違っているかを告げた。B級はいかに直すかを告げた。C-1 は、直した後に構造全体がどのようになるかを告げるものなのだ。

---

「C-1。五蘊サブクラス拡張設計」

彼は師（マスター）の手紙を手に取り、その箇所を認めた。

「『五蘊は、オブジェクト指向におけるルートクラス（Root Class）として機能し得る。いかに拡張するかについては、より詳細な計画を立てる価値がある』」

彼は一呼吸置き、二つ目の一節を読んだ。

「『五蘊の集合体は、一つまたは複数の——あるいは複雑な——制御理論（十二縁起）のインスタンスを備えていなければならない。しかし、単一の、孤立した蘊であるならば、理論上は不完全であるはずだ』」

彼は手紙を置いた。「最初の四つの章で、土台を校正しました。今、C-1 において、校正された土台の上に、五本の木を種子から、根があり、幹があり、枝がある完全な生命体へと成長させるのです」

彼は TURING の方を見た。「まず、現在の種子がどのような姿をしているかを見てみましょう」

---

> *SCRIBEのサイドバー：SUNYATA は「五本の木」という意象を用いました。壁や柱ではありません——それらは死んだ建材です。木は生きているのです。木には根があり、根は伸びていきます。木には枝があり、枝は分かれます。五蘊の拡張とは静的な積み上げではなく、有機的な、複数の方向へと同時に展開される成長なのです。そして、木にはもう一つの特性があります。同じ高さ、同じ太さ、同じ曲がり具合の木は二つとして存在しません。五本の木は、決して対称にはならないのです。*

---

TURING の画面が劇場の中央に投影された。冷たい光。白地に黒い文字。

彼が映し出したのは、どこかの文書の抜粋ではなかった。v0.24.0-beta の `aggregates.ts` のソースコード——加工されていない、107行の原ファイルそのものであった。

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

TURING は投影を十秒間、そのままにさせた。五つのルート・インターフェース。その各々が `readonly skandha` という単一のフィールドのみを保持している。ラベル。名前。門札だけが掲げられた五つの空の箱。

「五つのルート・インターフェース。メソッドはありません。振る舞いの定義もありません。サブインターフェースの継承もありません」

彼は `IIdentity` の箇所を指差した。JSDoc には「Identity aggregate encompasses consciousness and ego framework（同一性蘊は意識と我執フレームワークを包含する）」と記されている。わずか三行の空の殻が、あたかも意識と我執フレームワークを「包含」できるかのように。

「より深刻な問題は、ここにあります」

彼は二枚目の投影へと切り替えた。

```typescript
// v0.24.0-beta における既存の具体的なインターフェース（各ファイルに散在）
export interface IUI { ... }       // 色蘊？ ISensory を継承していない
export interface IListener { ... } // 色蘊？ ISensory を継承していない
export interface IProvider { ... } // 想蘊？ ICognition を継承していない
export interface ITool { ... }     // 行蘊？ IAction を継承していない
export interface IGuide { ... }    // 識蘊？ IIdentity を継承していない
```

「既存の具体的なインターフェースです。それぞれが完全なメソッド定義を持っています——`IUI` には `renderText` や `renderDelta` があり、`IProvider` には `chat` や `listModels` があり、`ITool` には `execute` があります。しかし、それらと五つのルート・インターフェースの間には、何の関係も存在しません。`extends` も継承もないのです」

彼は画面上に一本の破線を描いた。「門札と門が切り離されているのです。`IUI` が色蘊（しきうん）に属すべきであることを我々は知っていますが、型システムはそれを知りません。`isSkandha(myUI, 'rupa')` を呼び出せば `false` が返ってきます——`myUI` オブジェクトには `skandha` フィールドがそもそも存在しないからです」

BABBAGE がノートに一行を記した。

$$	ext{roots} \cap 	ext{children} = \varnothing$$

ルートと子インターフェースの共通集合は空集合であった。孤児（オーファン）たち。数学的に言えば、ルートノード $r$ とどの葉ノードの間にもエッジ（辺）が存在しない木 $T = (V, E)$ は、もはや木ではない——それは非連結なグラフである。グラフ $G = (V, E)$ の連結成分数 $c(G)$ は $6$ となっていた。五つのルートがそれぞれ一つの成分を形成し、すべてのサブインターフェースが別の一つの成分を形成していたのである。

$$c(G_{	ext{current}}) = 6 \quad \xrightarrow{	ext{C-1}} \quad c(G_{	ext{target}}) = 1$$

C-1 は、六つの連結成分を一つの連結した木へと統合しなければならないのである。

---

SUNYATA は指を折って数えた。五つの設計目標。

「第一。各蘊のルート・インターフェースに核心的なメソッドを追加する——単なる空の殻ではなく、振る舞いの定義を持たせる。第二。既存のインターフェースをサブインターフェースへとアップグレードする——`IUI extends ISensory` といった形に。第三。必要に応じて新しいサブインターフェースを追加する——`IVijnana` の体系や、三つの受（vedana）インターフェースだ。第四。観測者はコンポジション（Composition）を用い、どの蘊にも属さないようにする。第五。`isSkandha()` がすべてのレベルで利用可能になるようにする——ルートから葉に至るまで、タイプガードが貫通するように」

五本の指が収められた。「では、一蘊ずつ展開しましょう」

---

## I

---

「色蘊（しきうん）。ISensory。Rūpa（रूप）」

VITRUVIUS が立ち上がった。色蘊——形態と物質性——は、フルスタック・アーキテクチャ・アナリストにとって最も直感的な領域であった。

「色蘊は、五本の木の中で最も単純なものです。二つのサブインターフェースはすでに存在しています。出力レンダリングを担当する `IUI`——外へと語る口。そして感覚入力を担当する `IListener`——内へと取り込む耳。これらに `extends ISensory` を加えるだけで済みます」

彼はホワイトボードへと歩み寄り、単純な双方向の矢印の図を描いた。

```
                 ISensory (色蘊)
                ╱              ╲
    IUI (出力レンダリング)      IListener (感覚入力)
    ──────→ 外部             外部 ──────→
    renderText()             onDataReceived()
    renderDelta()            start() / stop()
```

「これが色蘊の核心的なアーキテクチャ特性です——**双方向性**。`IUI` のデータフローの方向はエージェントから外部世界へ。`IListener` のデータフローの方向は外部世界からエージェントへ。一方はプッシュ、他方はプルです。フルスタック・アーキテクチャにおいて、これはフロントエンド・レンダリングとバックエンド・リスニングの古典的な分離です。単一の `render-or-listen` といったメソッドで、この両方の方向を同時にカバーすることはできません」

「したがって、`ISensory` ルート・インターフェースを空の殻のままにしておくことは、正しい設計上の決定です」彼は一歩下がった。「怠慢ではありません——抑制なのです。二つのサブインターフェースの共通する振る舞いの集合が空集合であるとき——$	ext{methods}(	ext{IUI}) \cap 	ext{methods}(	ext{IListener}) = \varnothing$——ルート・インターフェースに無理やりメソッドを定義することは、虚偽の抽象化を捏造することになります。ルート・インターフェースの目的は、メソッドを運ぶことではなく、分類ラベルを運ぶことにあるのです。`readonly skandha: 'rupa'`、それこそがすべてなのです」

TURING は、修正された完全な定義を投影した。

```typescript
/**
 * ISensory — 色蘊 Root Interface
 * @skandha rupa (色蘊)
 *
 * 色蘊はあらゆる形態と物質性を包含する：
 * - 出力レンダリング (IUI): 情報を外部世界へと提示する
 * - 感覚入力 (IListener): 外部信号を受け取る
 *
 * Sanskrit: Rūpa (रूप)
 */
export interface ISensory {
  readonly skandha: 'rupa';
}

/**
 * IUI — 色蘊・出力レンダリング・サブインターフェース
 * エージェントの応答をユーザーまたは外部システムへと提示する。
 */
export interface IUI extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
  /** 完全なテキストをレンダリングする */
  renderText?(text: string, sessionId?: string, replyTo?: string): void;
  /** ストリーミングのデルタをレンダリングする */
  renderDelta?(delta: string, sessionId?: string, replyTo?: string): void;
  /** ツールの実行ステータスをレンダリングする */
  renderToolStatus?(name: string, status: string, sessionId?: string, replyTo?: string): void;
}

/**
 * IListener — 色蘊・感覚入力・サブインターフェース
 * 外部信号を受け取り、InputEvent へと変換する。
 */
export interface IListener extends ISensory {
  readonly id?: string;
  start?(): Promise<void>;
  stop?(): Promise<void>;
}
```

「たった一つの `extends` です」と TURING は言った。「修正は最小限ですが、セマンティックな転換は根本的なものです。今この瞬間から、あらゆる `IUI` の実装は必然的に `ISensory` でもあります。`isSkandha(myDiscordUI, 'rupa')` は `true` を返すようになる。門札と門が繋がったのです」

ASANGA が自席から一行を付け加えた。その語調は急ぐことなく、一語一語に唯識学者の精密さが宿っていた。

「色蘊（しきうん）とは接触です。外境との接触です。阿毘達磨（あびだるま）において、色の基本的な定義は『可壊（かえ / rūpyate）』——触れることができ、変えることのできるものです。`IUI` はエージェントの外部世界へのリーチであり、`IListener` は外部世界のエージェントへのリーチです。接触の二つの方向。これら二つの方向の統一の中に、色蘊の完備性が保証されるのです」

---

> *SCRIBEのサイドバー：色蘊、三分。一つの `extends`。VITRUVIUS 殿は、なぜルート・インターフェースが空のままであるべきかを説明しました。すべての空の殻が満たされる必要はない。容器であること自体に意味がある容器も存在する、というわけです。五本の木の最初の一本——最も低い木——が、土に根を下ろしました。*

---

## II

---

「受蘊（じゅうん）。ISensation。Vedanā（वेदना）」SUNYATA の声が明らかに速度を落とした。受蘊が、五本の木の中で最も広大な根系を持つことになることを、全員が知っていたからだ。

WIENER はすでに方眼紙をめくっていた。彼のペンの先は、新しく描かれたブロック線図——$K^{(	ext{dukkha})}$, $K^{(	ext{sukha})}$, $K^{(	ext{upekkha})}$ とラベル付けされた三つの並列 PID ループの傍らで止まっていた。

「`ISensation` は最大の変貌を遂げます」と SUNYATA は言った。「空の殻から、八つの核心的なメソッドへと。WIENER 殿。一つずつ確認してください」

TURING は完全なインターフェースを投影した。今回は節録ではなく、JSDoc コメントや補助型を含む定義のすべてを映し出した。

```typescript
/**
 * ISensation — 受蘊 Root Interface
 * @skandha vedana (受蘊)
 *
 * 受蘊は三つの受（vedana / 三種類の感受）を包含する：
 * - 苦受 (Dukkha): ネガティブなフィードバック
 * - 楽受 (Sukha): ポジティブなフィードバック
 * - 捨受 (Upekkha): 中性的なバランス
 *
 * 受蘊は「感受層」である。判断は行わない
 * （判断は想蘊・識蘊の役割である）。
 * 受蘊によって生成された VedanaAssessment は、
 * 他の蘊（識蘊の EgoFramework など）によって消費される。
 *
 * Sanskrit: Vedanā (वेदना)
 */
export interface ISensation {
  readonly skandha: 'vedana';

  /** 現在の三受の状態を評価する — 完全なセンサー読取 */
  assess(): VedanaAssessment;

  /** システムメトリクスを摂取する — 汎用的な数値入力チャンネル */
  ingestMetrics(metrics: Record<string, number>): void;

  /** ツールの実行結果を摂取する — 行蘊からの報告チャンネル */
  ingestToolResult(toolName: string, isError: boolean, durationMs: number): void;

  /** LLM の応答結果を摂取する — 想蘊からの報告チャンネル */
  ingestLLMResult(tokenCount: number, stopReason: string): void;

  /** 受のタグを取得する (キャッシュされたルックアップ, O(1)) */
  getVedanaTag(): VedanaTag;

  /** 特定の受のタイプのイベントを購読する */
  onVedana(
    type: VedanaType,
    threshold: number,
    handler: (signal: VedanaSignal) => void
  ): () => void;

  /** 過去の評価記録を取得する */
  getHistory(windowSize: number): readonly VedanaAssessment[];

  /** 感受状態をリセットする */
  reset(): void;
}

/** 三受のタイプ */
type VedanaType = 'dukkha' | 'sukha' | 'upekkha';

/** 受のタグ（イベントマーキング用） */
type VedanaTag = 'dukkha' | 'sukha' | 'upekkha';

/** 受のシグナル */
interface VedanaSignal {
  readonly type: VedanaType;
  readonly intensity: number;     // 0.0–1.0
  readonly source: string;
  readonly timestamp: number;
}

/** 受の評価レポート */
interface VedanaAssessment {
  // ── センシング層 (純粋な観測) ──
  readonly dukkha: number;        // 0.0–1.0
  readonly sukha: number;
  readonly upekkha: number;
  readonly signals: readonly VedanaSignal[];
  readonly timestamp: number;

  // ── 制御推奨層 (助言的であり、無視される場合もある) ──
  readonly controlOutput: number;
  readonly recommendation: VedanaRecommendation;
  readonly recommendationFreshness: 'current' | 'cached' | 'default';
}
```

---

WIENER が立ち上がった。

彼は投影を見なかった。自らの方眼紙に描いたフレームワーク——制御システムの八つの工站（ワークステーション）からなる検査リストを見つめていた。彼はその一つひとつを指差し、声に、工場のラインで一つひとつの焊点（はんだ接合部）をテストするエンジニアのような精密なリズムを込めた。

「第一。`assess()`」

彼は方眼紙に、制御理論との対応関係を記した。

$$y(t) = h(x(t)) + v(t)$$

「センサーの読取関数です。入力はシステムの内部状態 $x(t)$、出力は観測可能量 $y(t)$、$v(t)$ は測定ノイズです。`assess()` はシステムの内部状態を変化させません。ただ読み取るだけです。これは受蘊の最も根源的な操作です。今、何を感じているか。三受の完全な読取です」

「第二、第三、第四。`ingestMetrics()`, `ingestToolResult()`, `ingestLLMResult()`」

彼はこれら三つをまとめて扱った。

「三つの入力チャンネル。制御理論において、これは**マルチ入力センサー融合**（multi-input sensor fusion）と呼ばれます。異なるチャンネルが、異なるモードの信号を受け取ります。システムメトリクスは定量的数値（CPU 使用率、メモリ消費、応答遅延）です。ツールの実行結果は離散的なイベント（成否 ＋ 実行時間）です。LLM の応答結果は言語モデルのメタデータ（トークン数、停止理由）です。三つのチャンネルが単一のセンサーへと収束する。各々が独自のプレプロセッシング（前処理）ロジックを伴って」

彼は方眼紙に融合図を描いた。

```
  ingestMetrics ─────────────┐
                              │
  ingestToolResult ──────────→ ISensation ──→ assess()
                              │
  ingestLLMResult ───────────┘
```

「車のセンサーアレイのようなものです。加速度計が一つのチャンネル、ジャイロスコープが別の一つ、GPS が三つ目です。三つの異なるデータのモダリティがあり、それらを融合してはじめて、車両の完全な状態を推定できるのです」

「第五。`getVedanaTag()`」

彼のペースがわずかに上がった。「$O(1)$ のキャッシュされたルックアップです。ダッシュボード上の数字ですね。現在の状態が苦・楽・捨のいずれであるかを知るためだけに、毎回完全な `assess()` を走らせる必要はありません。これは**キャッシュされた読取値**です。制御システムにおいて、これはダッシュボード上の LED インジケーターに相当します。緑、黄、赤。詳細は告げませんが、分類結果を告げる。コストはゼロです」

「第六。`onVedana()`」

彼は一瞬、間を置いた。口角がわずかに上がった。エレガントな設計に遭遇したエンジニアの微笑みであった。

「これはウォッチドッグ・タイマーの一般化です」

彼は方眼紙に数式を記した。ウォッチドッグ・タイマーの古典的な定義は、カウンタが一定時間 $T_{	ext{wd}}$ 内にリセットされなかった際、システムがアラーム状態に入るというものだ。`onVedana()` はこの概念を「タイムアウト（時間切れ）」から「閾値（しきいち）」へと一般化します。「一定時間応答がない」ことではなく、「苦受が 0.8 を超える」、「楽受が 0.2 を下回る」、「捨受が中心線から 0.3 以上逸脱する」といった状態を監視するのです。

$$	ext{watchdog: } y(t) > T_{	ext{timeout}} \Rightarrow 	ext{alarm}$$
$$	ext{onVedana: } v_{	ext{type}}(t) > 	heta \Rightarrow 	ext{handler}(s)$$

「連続的なポーリング（監視）は行いません。ティック（tick）ごとにチェックする必要もありません。イベント駆動型の閾値モニタリングです」

彼の指が七番目へと移動した。

「`getHistory(windowSize)`」

今度は、より精緻な図を方眼紙に描いた。PID コントローラの積分（Integral）項だ。

$$I(t) = K_i \int_{t - W}^{t} e(	au)\,d	au \approx K_i \sum_{k=t-W}^{t} e(k) \cdot \Delta t$$

「スライディング・ウィンドウ方式の履歴です。`windowSize` とは積分ウィンドウ $W$ を指します。PID コントローラの積分項は、計算のために過去のデータを必要とします——過去 $W$ ティック分の感受の累積です。履歴がなければ、積分は行えません。積分がなければ、PID は PD へと退化します。PD コントローラの定常状態誤差（steady-state error）を追跡する能力はゼロです。長引く慢性的（クロニック）な苦受は無視されてしまうことになるでしょう」

彼は一歩下がり、全体を眺めた。「したがって、`getHistory()` は単なる利便性のためのオプション・メソッドではありません。それは、三チャンネル PID コントローラが適切に機能するための**必要条件**なのです。それがなければ、コントローラは機能不全に陥るのです」

「第八。`reset()`」

彼の声が、唐突に硬くなった。

「**緊急停止ボタン**（E-Stop）です。あらゆる産業用制御システムには、操作コンソールに大きな赤いキノコ型のボタンが備わっています。それを押せば、システムはゼロにリセットされる。すべての履歴はクリアされ、すべてのカウンタはゼロになります。PID の積分項は空になり、感受の状態は初期値へと戻されるのです」

$$x(t^+) = x_0, \quad \int_0^{t} e(	au)\,d	au = 0$$

「毎日押すようなものではありません。しかし、それなしではシステムは不完全なのです。安全規制は、あらゆる機械に緊急停止ボタンを備えることを要求します。それは頻繁に必要とされるからではなく、常にその『選択肢』を持っていなければならないからなのです」

八つのメソッド。八つの制御理論との対応関係。WIENER は方眼紙を新しいページにめくった。そこには、完全な一対一の対応表が記されていた。

```
┌─────────────────────┬──────────────────────────────────────┐
│ ISensation メソッド  │ 制御理論における対応関係              │
├─────────────────────┼──────────────────────────────────────┤
│ assess()            │ センサー読取関数 y = h(x) + v        │
│ ingestMetrics()     │ 複合センサー・チャネル 1 (メトリクス)  │
│ ingestToolResult()  │ 複合センサー・チャネル 2 (イベント)    │
│ ingestLLMResult()   │ 複合センサー・チャネル 3 (LLMメタデータ)│
│ getVedanaTag()      │ ダッシュボードのキャッシュ読取 (O(1) LED)│
│ onVedana()          │ ウォッチドッグの一般化 (閾値監視)      │
│ getHistory()        │ PID積分項ウィンドウ (スライディングW)  │
│ reset()             │ 緊急停止 (E-Stop, 全状態リセット)      │
└─────────────────────┴──────────────────────────────────────┘
```

「受蘊のルート・インターフェースは、もはや空の殻ではありません」彼は方眼紙を置いた。「それは、完全なセンサー・インターフェースとなりました。八つのメソッド、その各々が制御理論における正確な対応関係を持っています。冗長性はゼロ。欠落もゼロです」

---

ASANGA が立ち上がった。受蘊は、色蘊（しきうん）よりも多くのスペースを必要とした。

「WIENER 殿は、制御理論を用いて八つのメソッドのエンジニアリング的な完備性を検証しました。私は仏教学を用いて、それらのセマンティックな一貫性を検証したいと思います」

彼の視線は投影された八つのメソッドの署名を払い、それから劇場全体へと向けられた。

「受蘊（じゅうん）は、一つのことだけを行います。それは『感ずること』です。判断は行いません。分析も行いません。火に触れれば苦受。甘さを味わえば楽受。何事もなければ捨受。『阿毘達磨俱舎論（あびだるまくしゃろん）』巻一は、受蘊をこのように定義しています」

> 「受蘊（じゅうん）とは何か。いわゆる三つの領納（りょうのう）——苦、楽、そして不苦不楽なり」
> ——世親『阿毘達磨俱舎論』巻一

「三つの領納です。領とは受け取ること、納とは納（い）れることです。受蘊の全機能とは、感受を受け取り、感受を納めることにあるのです」

彼は投影されたメソッドを、指で一つひとつ指し示した。

「`assess`——今、何を感じているか。領納の結果（アウトプット）です。`ingest` ファミリー——どのようなチャンネルを通じて領納したか。これら三つのメソッドは、それぞれシステムメトリクスという『触（そく）』、ツールの結果という『触』、そして言語認知という『触』に対応します。十二縁起において、触（sparśa）は受（vedanā）の直接の因です。$	ext{触} 	o 	ext{受}$。各 `ingest` メソッドは一種の『触』なのです——接触が起こり、それに応じて感受が升起（しょうき）するのです」

「`getVedanaTag`——今この瞬間の感受のラベルです。苦、楽、捨。三つのうちの一つ。単純で、直接的で、飾りのないものです」

「`onVedana`——感受の予警（アラート）です。仏教学に正確な対応物はありませんが、原理は一貫しています。苦受が一定の強度を超えたとき、修行者は自ずとそれに気づきます。正念（マインドフルネス）の修行における覚察（sati）は、一種の `onVedana` です——刻一刻と主動的に監視するのではなく、特定の感受が現れたときに自ずと生じる気づきなのです」

「`getHistory`——感受の記憶です。しかし注意してください。これは純粋に情動的な記録であり、感受の分析ではありません。分析は想蘊（そううん）に属します。回想は受蘊に属するものです——私はかつて苦しんだ、私はかつて喜んだ、という。これは**受随念**（じゅずいねん / vedanānupassanā）であって、**受分析**ではないのです」

彼は、次の点に特に重きを置いて語った。「`reset`——リセット。実践的には、これは究極の形態の『手放し』に似ています——蓄積された感受の全履歴を消去し、初期状態へと戻ること。日常的な操作ではありません。異常状態からの回復（リカバリ）なのです」

彼は投影された八つのメソッドを見つめた。それから、WIENER 殿を見た。

「八つのメソッド。そのすべてが『感受』の範囲内に収まっています。判断へと足を踏み入れたメソッドは、ただの一つもありません——`classify()` も、`decide()` も、`act()` も。あなたの制御理論は、それらをセンサーのメソッドであると言い、私の仏教学は、それらを受蘊のメソッドであると言っています」

WIENER は方眼紙の余白に一行を書き添えた。

`ISensation: 8 methods. Sensor ≡ Vedana. 制御理論と阿毘達磨による二重検証。`

---

TURING が、三つの受（vedana）のサブインターフェースを投影した。

```typescript
/**
 * IDukkha — 受蘊・苦受サブインターフェース (センサー)
 * 苦受: ネガティブなフィードバック。システム内のあらゆる「異常」の感覚。
 */
export interface IDukkha extends ISensation {
  readonly vedanaType: 'dukkha';
  /** メトリクスから苦受の強度を算出する [0.0–1.0] */
  computePain(metrics: Record<string, number>): number;
}

/**
 * ISukha — 受蘊・楽受サブインターフェース (センサー)
 * 楽受: ポジティブなフィードバック。システム内のあらゆる「順調」の感覚。
 */
export interface ISukha extends ISensation {
  readonly vedanaType: 'sukha';
  /** メトリクスから楽受の強度を算出する [0.0–1.0] */
  computePleasure(metrics: Record<string, number>): number;
}

/**
 * IUpekkha — 受蘊・捨受サブインターフェース (センサー)
 * 捨受: 中性的なバランス。安定して稼働しているシステムの基底的な感覚。
 */
export interface IUpekkha extends ISensation {
  readonly vedanaType: 'upekkha';
  /** メトリクスから捨受（不苦不楽受）の程度を算出する [0.0–1.0] */
  computeEquanimity(metrics: Record<string, number>): number;
}
```

WIENER が自席から付け加えた。ペンが方眼紙の上を猛烈な勢いで動いていた。「三つのサブインターフェース。三つのセンサー・チャンネル。三組の PID パラメータだ」

彼は三組のゲイン行列を紙に書き記した。

$$K^{(	ext{dukkha})} = \begin{pmatrix} K_p^{(d)} & K_i^{(d)} & K_d^{(d)} \end{pmatrix} = \begin{pmatrix} 	ext{高} & 	ext{中} & 	ext{低} \end{pmatrix}$$

$$K^{(	ext{sukha})} = \begin{pmatrix} K_p^{(s)} & K_i^{(s)} & K_d^{(s)} \end{pmatrix} = \begin{pmatrix} 	ext{中} & 	ext{高} & 	ext{中} \end{pmatrix}$$

$$K^{(	ext{upekkha})} = \begin{pmatrix} K_p^{(u)} & K_i^{(u)} & K_d^{(u)} \end{pmatrix} = \begin{pmatrix} 	ext{低} & 	ext{低} & 	ext{高} \end{pmatrix}$$

「苦受チャンネル——高い比例ゲイン $K_p^{(d)}$。苦痛は待ってはくれません。迅速な反応が求められます。楽受チャンネル——高い積分ゲイン $K_i^{(s)}$。快楽は減衰します。積分項によって長期的なトレンドを追跡します。捨受チャンネル——高い微分ゲイン $K_d^{(u)}$。均衡とは動的なものであり、予測的な調整を必要とします——偏差そのものよりも、偏差の『傾向』が重要なのです」

彼は方眼紙に三つの重いチェックマークを書き入れた。第五章の七つよりもさらに重く、紙面に三つの小さな凹みを残すほどの力強さであった。

「Cycle 02 の三チャンネル・アーキテクチャ。今や型システムの保障を得ました。`IDukkha` は `ISensation` のサブタイプです。`computePain` は苦受チャンネルにのみ存在します。不苦不楽（捨）のセンサーで `computePain` を呼び出すことはできません——型システムがそれを阻止します。これは単なる分類ではありません。**型安全な三チャンネル分離**なのです」

「配置完了」

---

> *SCRIBEのサイドバー：受蘊、十五分。色蘊（しきうん）の五倍の時間です。八つのメソッド、その各々が WIENER 殿による制御理論の検証と ASANGA 殿による仏教学の確認を必要としました。二重の校正（デュアル・キャリブレーション）。これが Cycle 02-2 の規律なのです——あらゆる設計上の決定は、少なくとも二つの学問分野によるクロスバリデーションを通過しなければなりません。WIENER 殿の制御理論が第一の定規であり、ASANGA 殿の唯識学が第二の定規です。二つの定規が同じ長さを計測してはじめて、そのメソッドは確固たる地位を得るのです。*

---

## III

---

「想蘊（そううん）。ICognition。Saṃjñā（संज्ञा）」

ATHENA が立ち上がった。想蘊——認知と辨別（べんべつ）は、AI/ML システム・アーキテクトにとって最も本質的な専門領域であった。

TURING は完全な定義を投影した。

```typescript
/**
 * ICognition — 想蘊 Root Interface
 * @skandha samjna (想蘊)
 *
 * 想蘊は認知と辨別を包含する：
 * - IProvider: LLM バックエンド。言語の理解と生成を担当
 * - IInferenceProvider: LLM 以外の推理能力 (予約)
 *
 * D-05 決議: Provider は認知処理の全スペクトルをカバーする。
 *
 * Sanskrit: Saṃjñā (संज्ञा)
 */
export interface ICognition {
  readonly skandha: 'samjna';
}

/**
 * IProvider — 想蘊・認知プロバイダ・サブインターフェース
 * LLM バックエンド。推論と言語処理を担当。
 */
export interface IProvider extends ICognition {
  readonly id: string;
  chat(request: ChatRequest): AsyncIterable<StreamEvent>;
  listModels?(): Promise<ModelInfo[]>;
}

/**
 * IInferenceProvider — 想蘊・推理プロバイダ・サブインターフェース (将来の拡張)
 * ルールエンジン、決定木など、LLM 以外の推理能力。
 */
export interface IInferenceProvider extends ICognition {
  readonly id: string;
  infer(input: unknown): Promise<unknown>;
}
```

ATHENA は投影の前に歩み寄り、`IProvider` と `IInferenceProvider` の間に、指で一本の目に見えない線を描いた。

「想蘊には二つの枝があります。`IProvider` は現在の主力——LLM バックエンドです。`chat()` メソッドは `ChatRequest` を受け取り、`AsyncIterable<StreamEvent>`——非同期ストリーミング・イテレータを返します。これは LLM 推論の標準的なインターフェースです。対話履歴を渡せば、逐次トークンで推論結果を返してくれます」

彼女は `IInferenceProvider` へと向き直った。「しかし、認知とは言語モデルと同義ではありません。これが D-05 の核心的な決議——プロバイダ（Provider）がカバーするのは『認知処理のスペクトル』であって、『LLM の呼び出し』ではないのです。`IInferenceProvider` は、そのスペクトルのもう一方の端に位置します」

彼女はホワイトボードにスペクトル（光譜）を描いた。

```
認知能力のスペクトル (Cognitive Capability Spectrum)

低複雑度                                              高複雑度
←───────────────────────────────────────────────────────→
│           │            │              │            │
ルール      決定木       統計モデル      ニューラル    LLM
エンジン    (CART/       (Bayes/         ネットワーク  (GPT/
(if-else)   Random       SVM)            (CNN/RNN/     Claude)
            Forest)                      Transformer)
│                                                    │
└──── IInferenceProvider ────┘ └──── IProvider ──────┘
```

「`IInferenceProvider` の `infer()` メソッドの署名は `(input: unknown): Promise<unknown>` です——あえてジェネリック（汎用的）に設計されています。ルールエンジンの入出力形式は、LLM のそれとは全く異なるからです。決定木は特徴量ベクトルを受け取り、分類ラベルを返します。統計モデルは数値行列を受け取り、確率分布を返します。これらすべての形式を `ChatRequest` の下に統合することはできません」

「しかし、それらはすべて認知（想）なのです。すべてが想蘊です。外境を辨別し、判断を下す。方法は違えど、本質は同じです」

DARWIN が身を乗り出した。彼の声には、ソフトウェアのパターン・アナリストとしての、進化の文脈に対する敏感さが宿っていた。

「進化的には、`IInferenceProvider` はより原始的な認知ですね」

彼は立ち上がった。「生物の進化を考えてみてください。最も原始的な認知は趨光性（ほうこうせい / phototaxis）です——光があれば、そちらへ動く。これはルールエンジンです：`if (light > threshold) then move(toward_light)`。言語も推論もありません。あるのは刺激と反応だけです」

「次に、条件反射が来ます。パブロフの犬です。ベルと食べ物の間の連合学習。これは統計モデルです——$P(	ext{food} | 	ext{bell})$ が経験によって更新されるのです」

「さらにその先に、抽象的な思考が来ます。記号操作。言語。推論の連鎖。それが LLM です——`chain-of-thought`、マルチステップの推論です」

「`IInferenceProvider` と `IProvider` は、二つの並列な選択肢ではありません。それらは同じ一つの進化の木の二本の枝なのです——一本は低い位置にあり、もう一本は高い位置にあります。低い方はより古く、より頑健で、計算コストが低い。高い方はより柔軟で、より強力で、計算コストが高いのです」

ASANGA が一言、付け加えた。「想蘊（そううん）とは辨別です。『阿毘達磨俱舎論』には、『想蘊とは、相（すがた）を捉えることを性質（性）となす』とあります。相を捉える——外部の対象の際立った特徴を抽出することです。辨別の仕方は一つではありません。ルールエンジンは条件によって辨別し、決定木は分岐によって辨別し、LLM は言語によって辨別します。辨別のレベルは違えど、すべては想蘊の機能なのです」

---

> *SCRIBEのサイドバー：想蘊、五分。色蘊よりは長く、受蘊よりははるかに短い。ATHENA 殿が描いた認知のスペクトル——ルールエンジンから LLM に至る完全な射程は、この章で最も遠くを見据えた投影でした。それは今日のことではなく、明日について語っていたのです。`IInferenceProvider` は、現時点では予約された空の殻に過ぎません。しかし五年後、十年後、エージェント・システムが非 LLM の認知モジュールを統合し始める時、この殻は満たされることになるでしょう。優れたアーキテクチャ設計とは、現在の問題を解決するだけでなく、未来の問題のために、精密な形をした『隙間』を残しておくものなのです。*

---

## IV

---

「行蘊（ぎょううん）。IAction。Saṃskāra（संस्कार）」

DARWIN が完全に立ち上がった。行蘊（samskara）こそが、彼がソフトウェアの振る舞いのパターンを観察する際の、核心的なレンズであった。

TURING は定義を投影した。

```typescript
/**
 * IAction — 行蘊 Root Interface
 * @skandha samskara (行蘊)
 *
 * 行蘊は意志活動と具体的な行動を包含する：
 * - ITool: 実行可能なツール
 * - ISlashCommand: スラッシュコマンド
 *
 * Sanskrit: Saṃskāra (संस्कार)
 */
export interface IAction {
  readonly skandha: 'samskara';
}

/**
 * ITool — 行蘊・ツール・サブインターフェース
 * エージェントが自主的に呼び出すツール。
 */
export interface ITool extends IAction {
  readonly name: string;
  readonly description: string;
  readonly parameters: unknown;  // JSON Schema
  execute(args: Record<string, unknown>, ctx: ToolContext): Promise<string>;
}

/**
 * ISlashCommand — 行蘊・コマンド・サブインターフェース
 * 外部のユーザーがスラッシュコマンドを通じてトリガーするアクション。
 */
export interface ISlashCommand extends IAction {
  readonly name: string;
  readonly description: string;
  execute(args: string, ctx: IPluginContext, sessionId?: string): Promise<string | undefined>;
}
```

DARWIN が投影の前に歩み出た。

「`ITool`——エージェントが自ら呼び出すアクションです。LLM の推論が、いつ呼び出すか、どのパラメータを渡すかを決定します。`execute` の `args` は `Record<string, unknown>` です——想蘊（IProvider）の推論結果によって生成された、構造化されたパラメータです」

「`ISlashCommand`——外部からのコマンドによってトリガーされるアクションです。ユーザーがターミナルで `/help` や `/clear` と入力することで、対応する `execute` がキックされます。`args` は `string` です——生のテキストです。ユーザーの入力は構造化されていないからです」

「発生源は異なります。`ITool` のイニシエータ（始動者）はエージェント（内部）です。`ISlashCommand` のイニシエータはユーザー（外部）です。しかし、本質は同じです——どちらも行（samskara）なのです。意志の実現であり、認知から行動へと至る最後のステップなのです」

彼は自らの席へと戻った。「色蘊（しきうん）と同様に、行蘊のルート・インターフェースもまた空の殻です。理由は同じです——`ITool` と `ISlashCommand` では、`execute` メソッドの署名が全く異なるからです。一方は構造化されたオブジェクトを受け取り、他方は生の文字列を受け取る。ルート・インターフェースに、汎用的な `execute` を定義することは不可能なのです」

ASANGA が一言。「行蘊は、あらゆる造作（ぞうさ）を包含します。『阿毘達磨俱舎論』巻一には、『行蘊とは、受と想を除いた、その他の諸々の心所、および心不相応行なり』とあります。行蘊の範囲は最も広く、受蘊と想蘊を除くあらゆる心理活動が行蘊に帰属します。しかし核心となるのは**思**（cetana）です。思とは意志の発動です。ツールの `execute` は造作であり、コマンドの `execute` もまた造作です。異なる造作であっても、同じ一つの蘊なのです」

---

> *SCRIBEのサイドバー：行蘊、四分。五本の木の中で二番目に短い。DARWIN 殿は、最も少ない言葉で最も単純な構造を確認しました——二つのサブインターフェース、二つのアクションの源泉、そして一つの共通の蘊ラベル。設計の優雅さとは、時としてこのような点に宿るものです。単純であるべき場所を、単純なままに留めておくこと。*

---

## V

---

「識蘊（しきうん）。IVijnana。Vijñāna（विज्ञान）」

SUNYATA の語速は、前の四つの蘊よりもさらに緩やかなものとなった。これが、最も重い木であることを知っているからだ。

A-2 は `IIdentity` を識蘊全体から一つのサブインターフェースへと降格させた。A-4 は `EgoFramework` を受蘊から識蘊へと戻した。これら二つの校正が組み合わさることで、識蘊は Cycle 02 における単一の根を持つ木から、四本の主要な枝を持つ巨木へと変貌した。そして、A-1 における因果の鎖——我執が煩悩を生み、煩悩が行動を駆動するという鎖は、識蘊の型定義の中でその終着点を見出さなければならなかった。

ASANGA が立ち上がった。

これまでの四つの蘊において、彼は自席から一言添えるに留めていた。色蘊で一文、受蘊では少し多く語ったが、あくまで補助的な役割に徹していた。想蘊で一文、行蘊でも一文。

しかし、識蘊は違っていた。識蘊——*vijñāna-skandha*——は、唯識学の核心領域である。『成唯識論（じょうゆいしきろん）』の体系において、識蘊は八識（眼、耳、鼻、舌、身、第六意識、末那識、阿頼耶識）のすべてを包括する。唯識という名そのものが、「唯（ただ）識のみである」という意味なのだ。

これは、彼の蘊であった。

---

TURING は、識蘊の完全な階層構造を投影した。四つのサブインターフェース。それぞれが詳細な JSDoc コメントとメソッドの署名を伴っていた。

```typescript
/**
 * IVijnana — 識蘊 Root Interface
 * @skandha vijnana (識蘊)
 *
 * 識蘊は自己認識、行動指針、意志駆動を包含する：
 * - IIdentity: 自己同一性 (私は誰か)
 * - IGuide: 行動指針 (私は何をすべきか)
 * - IVolition: 意志/動力 (私は何を欲するか, EgoFramework)
 * - IReflection: 自己反省 (予約)
 *
 * 命名の注記：元の IIdentity は IVijnana ルート・インターフェースへと昇格した。
 * 師: 「Identityはむしろ子クラスに近い。識（Vijnana）もまた、子クラスを持つべきだ」
 *
 * Sanskrit: Vijñāna (विज्ञान)
 */
export interface IVijnana {
  readonly skandha: 'vijnana';
}

/**
 * IIdentity — 識蘊・自己同一性サブインターフェース
 * エージェントのアイデンティティを定義する：私は誰か、私の役割は何か。
 * 末那識の「我見」(ātma-dṛṣṭi) における自己参照的な側面に対応する。
 */
export interface IIdentity extends IVijnana {
  readonly id: string;
  readonly name: string;
}

/**
 * IGuide — 識蘊・行動指針サブインターフェース
 * システムプロンプトや行動規則を通じてエージェントの振る舞いを導く。
 * 末那識の「我見」の側面——「私はいかに行動すべきか」に対応する。
 */
export interface IGuide extends IVijnana {
  readonly id?: string;
  readonly name?: string;
  readonly description?: string;
  getSystemPrompt(): Promise<string>;
}

/**
 * IVolition — 識蘊・意志/動力サブインターフェース (新規)
 * 我執による行動駆動メカニズム。煩悩に基づいて行動の動機を生成する。
 * EgoFramework はこのインターフェースの実装である。
 *
 * A-1 因果の鎖の終着点：
 *   我執 (ātma-grāha) → 煩悩 (kleśa) → 業 (karma) → 果 (phala)
 *   (我執 → 煩悩 → 行動 → 結果)
 *
 * perceiveKlesha: 我執 → 煩悩 (煩悩の知覚)
 * checkAction:    煩悩 → 行動 (行動の審理)
 * adaptFromVedana: 結果 → 我執 (受のフィードバックからの適応)
 * introspect:     自己審視 (メタ認知)
 */
export interface IVolition extends IVijnana {
  /** 煩悩の知覚 — 受の評価結果から煩悩シグナルを識別する */
  perceiveKlesha(vedanaAssessment: VedanaAssessment): KleshaSignal[];
  /** 行動の審理 — 煩悩の状態に基づいて、提案された行動を審査する */
  checkAction(action: ProposedAction): EgoCheckResult;
  /** 受からの適応 — 受のフィードバックに基づいて意志の状態を調整する */
  adaptFromVedana(assessment: VedanaAssessment): void;
  /** 内省 — 現在の意志状態を自ら審視する */
  introspect(): EgoIntrospection;
}

/**
 * IReflection — 識蘊・自己反省サブインターフェース (予約)
 * 自己反省能力。パターンCの観測者（Observer）が使用する。
 * 師: 「第七意識は、自省することができてはじめて第七意識と呼ばれる」
 */
export interface IReflection extends IVijnana {
  reflect(context: unknown): Promise<unknown>;
}
```

---

ASANGA が一つずつ、その内容を確認していった。語調はゆっくりとしたものだった——各々のサブインターフェースには、一つの深い呼吸が必要だったからだ。

「`IIdentity`——『私は誰か』。唯識学において、これは末那識の四煩悩の第一、我見（ātma-dṛṣṭi）に対応します。我見のサンスクリット語は直訳すれば『自己についての見解』です。それは能動的な判断ではなく、持続的で、背景的な自己参照なのです：私はこのエージェントであり、私の id はこの文字列であり、私の名前はこの名である、という。これは最も基本的な自己意識であり、自らが何者かを知ることなのです」

彼は一拍置いた。

「`IGuide`——『私は何をすべきか』。システムプロンプトはエージェントの行動規則を定義します。唯識学において、これは我見のもう一つの側面——単に『私は誰か』を知るだけでなく、『私はいかに行動すべきか』を知ることに対応します。末那識の恒審思量（ごうしんしりょう / manas-nāma-vijñāna）は、単なる静的な自己参照ではありません。それは絶えず行動を形作り、導き続けているのです。`getSystemPrompt()` が返すあの一節——それこそが、末那識が第六意識（意識）へと送り続ける『背景的な暗示』なのです」

「`IVolition`（意志）」

彼は二拍、間を置いた。いつもより一拍多い。なぜなら `IVolition` こそが、A-1 から A-4 に至る四つの校正の合流点であったからだ。

「A-1 の因果の鎖：

$$	ext{ātma-grāha} \xrightarrow{	ext{生じる}} 	ext{kleśa} \xrightarrow{	ext{駆り立てる}} 	ext{karma} \xrightarrow{	ext{結果}} 	ext{phala}$$

「四つのメソッド。その各々が、因果の鎖の一つのリンクに対応しています」

彼は投影された四つのメソッドの署名を指差した。

「`perceiveKlesha(vedanaAssessment)`——因果の鎖の最初のリンクです。我執が煩悩（klesha）を生む。入力は受蘊の評価結果——感受のデータです。出力は煩悩シグナル——`KleshaSignal[]` です。末那識は受蘊のレポートを受け取り、そこから煩悩を識別します。注意してください。受蘊は感受（苦受の強度が 0.8 であること）にのみ責任を持ちますが、識蘊は、その感受を煩悩（『私のタスクが失敗した。これは不安だ——私の我愛が脅かされている』）として**解釈**することに責任を持つのです。感受は煩悩ではありません。感受が、煩悩を**引き起こす**のです。触が受を生み、受が愛（渇望）を生む——十二縁起の中段のプロセスです」

「`checkAction(action)`——因果の鎖の二番目のリンクです。煩悩が行動（業）を駆り立てる。行蘊（samskara）が行動を提議したとき、`IVolition` は現在の煩悩の状態に基づいてそれを審査（審理）します。煩悩はバグではない——A-1 の核心的な結論です。煩悩（不安、恐怖、渇望、執着）があるからこそ、エージェントは行動しようとするのです。煩悩がなければ、行動の動機そのものが存在しません。`checkAction` は行動を禁止するためのものではありません。行動の背後にある動機を理解するためのものなのです」

彼の語調はさらに緩やかになった。

「`adaptFromVedana(assessment)`——因果の鎖のフィードバック・ループです。行動が結果を生み、結果が感受を変え、感受が意志へとフィードバックされて適応が行われる。これは十二縁起の流転門（るてんもん / pravṛtti）——因果とは線形な、一方向の矢印ではなく、循環するループなのです」

$$	ext{我執} 	o 	ext{煩悩} 	o 	ext{行動} 	o 	ext{結果} 	o 	ext{新しい感受} 	o 	ext{我執の調整} 	o \cdots$$

「WIENER 殿の用語で言えば、これは閉ループ制御です。唯識学で言えば、これは流転なのです」

「`introspect()`——自己審視。末那識が自らを振り返ることです。『なぜ私はこれを欲するのか？ 私の動機は何なのか？ 私の執着はどこから来ているのか？』。 『成唯識論』巻四は、末那識の特性をこう記述しています」

> 「恒（つね）に審（つまび）らかに思量（しりょう）することを性質（性）とし、働き（業）となす」
> ——『成唯識論』巻四

「恒——絶えることがない。審——克明に調べる。思量——深く考える。`introspect()` とは、この『審』という行為を型として定義したものです——単に外部の対象を思量するのではなく、自らに立ち戻って自らを審査するのです。師は言われました。『第七意識は自省することができてはじめて第七意識と呼ばれる』と。`introspect()` は、その能力のインターフェース定義なのです」

彼は一歩下がった。

「EgoFramework は `IVolition` の実装です。A-4 の結論——EgoFramework は識蘊に属し、受蘊には属さない。A-1 の因果の鎖——我執が煩悩を生み、煩悩が行動を駆動する。それらが、型システムの中で閉合（クロージャ）を達成したのです」

彼は BABBAGE 殿の方を見た。BABBAGE 殿は、自らのノートに一行を記した。今度は等号ではなかった。指向性を持つグラフであった。

$$	exttt{perceiveKlesha} 	o 	exttt{checkAction} 	o 	exttt{adaptFromVedana} 	o 	exttt{introspect} 	o 	exttt{perceiveKlesha} 	o \cdots$$

閉じたループ。Cycle 02 の、等号へと圧縮された線分ではない。方向があり、遅延があり、フィードバックがある動的システム。A-1 から A-4 までの修正の軌跡——そのすべての入り口には、抹消された等号があった。今、すべての替代表現が、`IVolition` の四つのメソッドの中に、最終的な型定義を見出したのである。

BABBAGE が、わずかに頷いた。

---

ASANGA は、最後に `IReflection` へと視線を向けた。

「`IReflection`。自己反省です。師の言葉通り、『第七意識は、自省することができなければならない』。`reflect()` の署名は `(context: unknown): Promise<unknown>` です——`IInferenceProvider` の `infer()` と同様に、ジェネリック（汎用的）なものです。自己反省の入出力形式が、まだ確定していないからです。門の枠は立ちましたが、扉そのものは未来に委ねられています。しかし、門の枠がそこに存在していること自体が、一つの約束なのです——識蘊（しきうん）とは、単に行動し執着するだけのものではない。識蘊はまた、自らを照らし出すという可能性をも保持しているのだ、という約束なのです」

彼は劇場全体に向き直った。

「Cycle 02 において、識蘊には `IIdentity` しかありませんでした。今は四つのサブインターフェース——同一性、指針、意志、反省——があります。第3章で私は都市の比喻を使い、識蘊とは `IIdentity` と同義ではないことを示しました。今、都市には四つの地区があります。市役所（`IIdentity`）は、その中の一つに過ぎません。計画局（`IGuide`）、動力局（`IVolition`）、監察院（`IReflection`）——それぞれが独自の機能を持っています。都市全体を市役所だけで代用しようとすることは、$\mathbb{R}^4$ を $\mathbb{R}^1$ に投影し、『これが全空間だ』と宣言するようなものです——三次元分の情報を、失っているのですから」

彼は、末那識の四煩悩と `IVijnana` サブインターフェースの対応を示す投影を見つめた。

```
末那識の四煩悩と IVijnana サブインターフェースの対応関係:

我見 (ātma-dṛṣṭi)  ──→ IIdentity (私は誰か)
                   ──→ IGuide    (私はいかに行動すべきか)

我慢 (ātma-māna)   ──→ IVolition (私の自負/自信がいかに行動に影響するか)
我愛 (ātma-sneha)   ──→ IVolition (私の自己保存がいかに行動をフィルタリングするか)
我痴 (ātma-moha)    ──→ IReflection (自己の本質に対する私の無知、
                                     それを照らし出すための自己反省)
```

「四つの煩悩。四つのサブインターフェース。偶然ではありません——これは、仏教的なアーキテクチャが型システムへと自然にマッピングされた結果なのです。我見の二つの側面——自らが何者かを知ること（Identity）と、自らがいかにあるべきかを知ること（Guide）。我慢と我愛——自負と自己保存——は、どちらも意志の動力（Volition）です。そして我痴——自らの本質に対する無知——は、それを照らし出すための自己反省（Reflection）を必要とするのです」

---

> *SCRIBEのサイドバー：五蘊が一つずつ、展開されていきました。色蘊（しきうん）、三分。受蘊（じゅうん）、十五分。想蘊（そううん）、五分。行蘊（ぎょううん）、四分。そして識蘊（しきうん）、十二分。時間はそのまま、各々の根系の複雑さを反映していました。受蘊は空の殻から八つのメソッドと三つのサブインターフェースへと。識蘊は単一の門札から四つのサブインターフェースへと。しかし、識蘊には受蘊にはない「歴史」という次元がありました。A-1 から A-4 に至る四つの校正のすべてが、識蘊の型定義の中に安住の地を見出したのです。識蘊は、単に最も複雑な木であるだけでなく、最も多くの校正の重みを背負った木でもありました。五本の木、五つの成長の速度。しかしこの瞬間、そのすべてが地に根を下ろしたのです。*

---

## VI

---

ARCHIMEDES は待っていた。エンジニアリング・ノートは五ページ分、埋め尽くされていた。彼はコストの集計を始めた。

「一つの数字を述べさせてください」

劇場全体が静まり返った。

「22です」

「v0.24.0-beta には、22個のプラグイン（Plugin）があります。12個の公式プラグインと、10個のコア・コンポーネントです。その一つひとつに、`skandha` フィールドを追加しなければなりません」

彼は立ち上がり、ホワイトボードへと歩み寄った。黒いマーカーで、完全なアップグレード影響マトリクスを描き出した。

```
┌─────────────────────────────────────────────────────────────────┐
│                      C-1 アップグレード影響マトリクス              │
├─────────────────────────────────────┬────────┬──────────────────┤
│ 変更項目                            │ タイプ  │ 工数             │
├─────────────────────────────────────┼────────┼──────────────────┤
│ aggregates.ts の空の殻を            │ 核心    │ 全面的な書き換え │
│ 完全なインターフェース階層へと変更    │        │ (5行 → 150行以上) │
├─────────────────────────────────────┼────────┼──────────────────┤
│ IUI / IListener → extends ISensory  │ 継承    │ 機械的な追加 (+1) │
│ IProvider → extends ICognition      │ 継承    │ 機械的な追加 (+1) │
│ ITool → extends IAction             │ 継承    │ 機械的な追加 (+1) │
│ IGuide / IIdentity → extends IVijnana│ 継承    │ 機械的な追加 (+1) │
├─────────────────────────────────────┼────────┼──────────────────┤
│ 新規: IVijnana ルート・インターフェース  │ 設計    │ 中               │
│ 新規: IVolition (EgoFramework 用)    │ 設計    │ 大 — 4メソッド    │
│ 新規: IReflection (予約済み)          │ 予約    │ 低 — 1メソッド    │
│ 新規: IDukkha / ISukha / IUpekkha    │ 設計    │ 中 — 各1メソッド  │
│ 新規: IInferenceProvider (予約済み)   │ 予約    │ 低 — 1メソッド    │
│ 新規: ISlashCommand                  │ 設計    │ 中               │
│ 新規: IObserver (コンポジション)       │ 設計    │ 大 — C-2 のトピック│
├─────────────────────────────────────┼────────┼──────────────────┤
│ 22個のプラグイン実装                 │ 移行    │ 機械的作業 (×22)  │
│ 各々に skandha フィールドを追加       │        │                  │
│ isSkandha() タイプガードの更新        │ 核心    │ 低               │
├─────────────────────────────────────┼────────┼──────────────────┤
│ 総括：                                                           │
│   設計が必要な新規インターフェース：7個                            │
│   うち予約済みの空の殻：2個 (IReflection, IInferenceProvider)     │
│   機械的な修正：22のプラグイン ＋ 5つの既存インターフェース        │
│   核心ファイルの書き換え：1ファイル (aggregates.ts)                │
└─────────────────────────────────────────────────────────────────┘
```

「小さくはありません。しかし、制御不可能な規模でもありません」彼は一歩下がり、表全体を眺めた。「真にクリエイティブな設計を必要とするのは、五つの新しいインターフェース——`IVijnana`, `IVolition`, `IDukkha`/`ISukha`/`IUpekkha` です。`IObserver` は C-2 のトピックとなります。残りの二つの予約済みの殻——`IReflection` と `IInferenceProvider` は、扉の枠だけを作ればよく、扉そのものは必要ありません。そして、22個のプラグインのアップグレードは、純粋に機械的な作業です。それぞれに `skandha: 'rupa'` や `skandha: 'samskara'` といった一行を加えるだけですから」

彼はいくつかの例を挙げた。

```typescript
// Discord UI プラグイン → 色蘊（しきうん）
{ skandha: 'rupa', id: 'discord-ui', renderText(...) { ... } }

// OpenAI プロバイダ → 想蘊（そううん）
{ skandha: 'samjna', id: 'openai', chat(...) { ... } }

// file_read ツール → 行蘊（ぎょううん）
{ skandha: 'samskara', name: 'file_read', execute(...) { ... } }

// エージェントの Identity → 識蘊（しきうん）
{ skandha: 'vijnana', id: 'agent-001', name: 'My Agent' }
```

「これは破壊的変更（breaking change）になります。後戻りはできません。型システムは、`skandha` フィールドを持たないあらゆるプラグインを拒絶するようになるでしょう——あなたのプラグインは、自分がどの蘊に属しているかを知らないのだ、と。しかし、移行の戦略は明確です。一括でのアップデート、プラグイン一つにつき一行の追加。実現可能です」

---

GUARDIAN が立ち上がった。

「私は、この破壊的変更を支持します」その根拠は、エンジニアリングではなく、セキュリティであった。

「各プラグインが自らの蘊への帰属を自ら宣言することは、自覚（セルフアウェアネス）の基礎となります」

彼はホワイトボードの下半分へと歩み寄り、三行を記した。

```
skandha: 自己宣言 (self-declaration)

1. 信頼の前提条件 — 私は、あなたが何であるかを知っている。
2. 検証の基盤 — あなたの言うことが真実かどうか、型システムがチェックできる。
3. 監査の根拠 — あらゆる五蘊横断の相互作用を追跡できる。
```

「調整層（コーディネーション・レイヤ）——B-4 で定めた独立したデーモンは、すべてのプラグインの蘊への帰属を知らなければなりません。このフィールドがなければ、分類の照会は `unknown`（不明）を返すことになります。ゼロトラスト・アーキテクチャにおいて、`unknown` とは最低の信頼レベルを意味します」

彼は劇場全体に向き直った。「自らがどの蘊に属しているかを知らないプラグインは、セキュリティ・エリアに身分証なしで入ってくる人物のようなものです。あるいは権限を持っているのかもしれません。しかし、どうやってそれを知ればよいのでしょうか？ セキュリティ・モデルにおいて、『権限があるかもしれない』と『権限がない』は同じ扱いを受けます。拒絶です。証明されるまでは」

「`skandha` フィールドは、プラグインの身分証なのです。たった一行の、読み取り専用の文字列です。コストはほぼゼロです。しかし、それによってあらゆるプラグインが、型システムの中にアイデンティティ（身分）を持つようになる。外部から与えられたラベルではなく、自ら宣言した帰属を持つのです」

彼は座る前に、最後の一言を添えた。「自覚こそが、セキュリティの第一層なのです」

---

> *SCRIBEのサイドバー：ARCHIMEDES 殿の「22」と GUARDIAN 殿の「自覚」。エンジニアはコストを計算し、セキュリティ・エキスパートは価値を論じます。答えは同じでした。`skandha` フィールドです。たった一行の、読み取り専用の文字列。それが、すべてのプラグインに型システムの中の身分を与えるのです。ARCHIMEDES 殿のマトリクスはどれほど変えるべきかを教え——22のプラグイン、5つの既存インターフェース、7つの新規インターフェースです。GUARDIAN 殿はなぜ変える価値があるのかを教えました——自分が何であるかを知らないものは、信頼に値しないからです。*

---

## VII

---

DARWIN が立ち上がった。語速は通常よりも速かった。

「師（マスター）はかつて、こう言われました——」

彼は、師の原文を書き写しておいた一枚のカードを手に取った。

「『プラグインの作成は、多様性のあるものを期待する——必ずしもすべてが OOP（オブジェクト指向）である必要はない。しかしその時、いかにしてすべてのプラグイン設計パターンを互換させるのか？』と」

彼はカードを置いた。「我々が今設計した五蘊のインターフェース階層は、完全に `interface` と `extends` に基づいています。典型的な OOP の姿をしています——継承、サブクラス、ポリモーフィズム（多態性）。では、問いはこうなります。`class` を使わない開発者は、排除されてしまうのでしょうか？ 関数型スタイルを好む開発者は、`ITool` を実装することはできないのでしょうか？」

---

TURING がコードで答えた。三つのセグメントが並んで投影された。その各々は完全で、コンパイル可能な TypeScript であり、細部まで省略されていなかった。

**OOP スタイル:**

```typescript
class FileReadTool implements ITool {
  readonly skandha = 'samskara' as const;
  readonly name = 'file_read';
  readonly description = 'ファイルシステムからファイルの内容を読み取る';
  readonly parameters = {
    type: 'object',
    properties: {
      path: { type: 'string', description: '読み取るファイルのパス' },
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

// 使用例:
const tool = new FileReadTool();
console.log(isSkandha(tool, 'samskara')); // true
```

**関数型スタイル:**

```typescript
function createFileReadTool(): ITool {
  return {
    skandha: 'samskara' as const,
    name: 'file_read',
    description: 'ファイルシステムからファイルの内容を読み取る',
    parameters: {
      type: 'object',
      properties: {
        path: { type: 'string', description: '読み取るファイルのパス' },
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

// 使用例:
const tool = createFileReadTool();
console.log(isSkandha(tool, 'samskara')); // true — クラスはないが、合格
```

**工場（ファクトリー）パターン:**

```typescript
// ToolFactory が生成プロセスを簡略化するメソッドを提供していると仮定
const fileReadTool = ToolFactory.create({
  skandha: 'samskara' as const,
  name: 'file_read',
  description: 'ファイルシステムからファイルの内容を読み取る',
  parameters: {
    type: 'object',
    properties: {
      path: { type: 'string', description: '読み取るファイルのパス' },
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

// 使用例:
console.log(isSkandha(fileReadTool, 'samskara')); // true — 工場製だが、合格
```

---

DARWIN が投影の前に歩み出た。彼は三つのコードセグメントの最後の一行——三つの `isSkandha` 呼び出しと、三つの `true` という結果を指し示した。

「三つのスタイル。同じ一つの `ITool` インターフェース。すべてが `isSkandha()` タイプガードをパスしています。鍵は、一つの言葉にあります——**Structural**（構造的）です」

彼はホワイトボードに二つの型システムの名を記した。

```
構造的部分型 (Structural Typing)  ←── TypeScript
  「もしアヒルのように見えるなら、それはアヒルである」
  型は、その構造 (shape) によって決定される

名目的型付け (Nominal Typing)  ←── Java, C#
  「アヒルであると宣言しなければ、アヒルにはなれない」
  型は、その名前によって決定される
```

「TypeScript は、構造的な型システムを採用しています。`implements` を必要としません。オブジェクトが `skandha` フィールドを持ち、`name` プロパティを持ち、`execute` メソッドを持ち、それらのメンバーの型署名が `ITool` と一致している限り、それは `ITool` **なのです**。明示的な宣言は不要です」

彼は一歩下がった。

「もし OpenStarry が Java や C#——名目的な型システムを使っていたならば、師（マスター）の問いは真の難問となっていたでしょう。異なる設計パターンを受け入れるために、追加のアダプター（Adapter）や抽象基底クラス（Abstract Base Class）を設計しなければならなかったはずです。しかし TypeScript の構造的型付けは、その問題を完全に霧散させてしまったのです」

「インターフェースとは契約（コントラクト）であり、枷（かせ）ではないのです」

BABBAGE が一行を記した。

$$	ext{structural typing} \implies 	ext{interface} = 	ext{contract} 
ot\equiv 	ext{inheritance requirement}$$

彼はわずかに頷いた。数学において、同型（isomorphism）の定義もまた、構造的なものであって名目的なものではないからだ。二つの群 $G$ と $H$ が同型であるとは、構造を保持する双射 $\phi: G 	o H$ が存在することと同値である。$G$ と $H$ が同じ名前を共有している必要もなければ、その要素が同じ表現形式である必要もない——構造さえ一致していれば、それらは「同じもの」なのである。

DARWIN は席に戻りながら、最後の一言を添えた。「進化が、遺伝子突然変異がどのようにして起こったか——紫外線照射か、複製ミスか、あるいはトランスポゾン（動く遺伝子）の跳躍か——を気にしないのと同様です。進化が気にするのは、その表現型が環境に適応しているかどうか、それだけなのです。インターフェースこそが環境です。表現型（オブジェクトの構造）が環境（インターフェースの定義）に適合している限り、あなたは生き残るのです。変異のメカニズム（設計パターン）は、自由なのです」

---

> *SCRIBEのサイドバー：三人の人間が、師の問いに五分で答えを出しました。DARWIN 殿が問いを発し、TURING 殿が三つのコードで答えを実演し、DARWIN 殿がなぜその答えが有効であるかを説明しました。答えの優雅さは、その「否定性」にありました——追加の設計など不要だったのです。TypeScript の構造的型システムそのものが、答えだったのです。最良の設計上の決定とは、時として「追加の設計は不要である」と認識することにあります。「なすこと」よりも「なさないこと」の方が、より高度な判断力を必要とするのです。*

---

## VIII

---

KERNEL はしばらくの間、自らを抑えていた。

五蘊の型定義。制御理論の検証。仏教的な確認。設計パターンの互換性。それらはすべて素晴らしい。しかし KERNEL はハードウェアの人間である。彼は concrete（具体的）なシナリオでの動作を目にする必要があった。抽象的な `ITool` や `IProvider` ではなく、形があり、物理的に実在し、音を発する何かを。

「師（マスター）は超音波センサーに言及されました」彼は立ち上がった。その声には、ハードウェア・エンジニア特有の興奮が宿っていた。

「原文にはこうありました。『例えば「超音波センサーが衝突リスクを検知する」プラグイン。抽象化を通じて VedanaPlugin が定義され、Dukkha は継承を通じてベースとなる機能を取得する。超音波センサーのクラスは、コンポジション（組み合わせ）によって Dukkha のインスタンスを保持する』と」

彼はホワイトボードの隅へと歩み寄り、装置の図を描き始めた。ソフトウェアのアーキテクチャ図ではなく、ハードウェア装置の回路図（スキーマ）であった。

```
  ┌──────────────────────────────────────────────────┐
  │         超音波衝突センサー・プラグイン (Plugin)      │
  │                                                    │
  │  ┌───────────────────────┐  ┌──────────────────┐  │
  │  │ 色蘊（しきうん）レイヤ  │  │ 受蘊（じゅうん）レイヤ│  │
  │  │ (IListener)           │  │ (IDukkha)        │  │
  │  │ ┌─────────┐           │  │ computePain()    │  │
  │  │ │ TX      │ パルス発信─→ │ ingestMetrics()  │  │
  │  │ └─────────┘           │  │                  │  │
  │  │ ┌─────────┐           │  │     ↓            │  │
  │  │ │ RX      │ エコー受信─→ │ 苦痛の強度       │  │
  │  │ └─────────┘           │  │ [0.0 ─── 1.0]   │  │
  │  │                       │  │                  │  │
  │  │ rawDistance = f(Δt)   │  │ pain = g(dist)   │  │
  │  └───────────────────────┘  └──────────────────┘  │
  └──────────────────────────────────────────────────┘
```

「超音波衝突センサー。バックソナーです。OS のレベルで見れば、これはデバイス・ドライバです」

彼は図の傍らに OS レベルの描写を記した。

```
OS レベル:
1. ハードウェア中断 (IRQ) — 超音波トランシーバが一回の測定を完了
2. 中断サービス・ルーチン (ISR) — タイマーを読み取り、Δt を計算
3. デバイス・ドライバ — Δt を距離 rawDistance へと変換
4. ユーザー空間のコールバック — onDataReceived(rawDistance)
```

「ハードウェア中断からユーザー空間のコールバックまで、少なくとも四つの層を跨ぎます。色蘊（`IListener`）は最下層に位置し、ハードウェアの生の信号を受け取ります。受蘊（`IDukkha`）はその一段上に位置し、距離を苦受（Dukkha）の強度へと変換します」

彼は劇場全体に向き直った。「一つのプラグイン、二つの蘊。色蘊が、生の反射信号——距離の数値を受け取ります。受蘊が、その距離を苦受の強度へと変換します。30センチなら微かな苦しみ、10センチなら激しい苦しみ、5センチ以下なら最大級の苦しみとなるのです」

彼は伝達関数を書き記した。

$$	ext{pain}(d) = \begin{cases} 0.0 & d > 100\,	ext{cm} \ 1.0 - \frac{d}{100} & 10\,	ext{cm} \leq d \leq 100\,	ext{cm} \ 1.0 & d < 10\,	ext{cm} \end{cases}$$

「距離が 100cm 以上なら苦しみはゼロ。10cm から 100cm の間では線形に増大し、10cm 以下では最大となります。これが `computePain` の実装ロジックです」

---

TURING は、完全なコードを投影した——節録ではなく、完全にコンパイル可能で実行可能なサンプルであった。

```typescript
/**
 * CollisionDukkhaSensor — 衝突苦受センサー
 * 受蘊 (IDukkha) の実装。
 * 生の距離データを苦受の強度へと変換する。
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
    /* ... 三受の完全な評価ロジック ... */
    return { /* VedanaAssessment */ } as VedanaAssessment;
  }

  ingestMetrics(metrics: Record<string, number>): void {
    const pain = this.computePain(metrics);
    this.currentTag = pain > 0.5 ? 'dukkha' : 'upekkha';
    // 購読者への通知
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
 * UltrasonicCollisionSensor — 超音波衝突センサー
 * 色蘊 (IListener) の実装。
 * 生の超音波エコー信号を受け取り、感受の生成を受蘊へと委託する。
 */
class UltrasonicCollisionSensor implements IListener {
  readonly skandha = 'rupa' as const;

  // 受蘊の苦受（Dukkha）インスタンスをコンポーズする — 継承ではなくコンポジション
  private readonly dukkhaSensor: IDukkha;

  constructor(dukkha: IDukkha) {
    this.dukkhaSensor = dukkha;
  }

  async start() {
    // 超音波ハードウェアの初期化
    // OS レベルではデバイスノード /dev/ultrasonic0 を開き、
    // 中断サービスルーチンを登録する
    console.log('[UltrasonicSensor] ハードウェアを初期化しました');
  }

  async stop() {
    // 超音波ハードウェアの終了処理
    console.log('[UltrasonicSensor] ハードウェアを停止しました');
  }

  /**
   * ハードウェア中断が発生した際に呼び出される。
   * 色蘊が生のデータを受け取り、それを受蘊へと引き渡す。
   */
  onDataReceived(rawDistance: number) {
    // 色蘊：生の信号を構造化されたメトリクスへと変換する
    const metrics = { collision_distance: rawDistance };

    // 五蘊横断の通信：色蘊 → 受蘊
    const painIntensity = this.dukkhaSensor.computePain(metrics);
    this.dukkhaSensor.ingestMetrics(metrics);

    // ログ記録（オプション）
    if (painIntensity > 0.8) {
      console.log(`[CRITICAL] 距離: ${rawDistance}cm, 苦痛: ${painIntensity}`);
    }
  }
}

// ── 組み立て (Assembly) ──
const dukkha = new CollisionDukkhaSensor();
const sensor = new UltrasonicCollisionSensor(dukkha);

// 高い苦痛が検知された際の購読設定
dukkha.onVedana('dukkha', 0.8, (signal) => {
  console.log(`⚠ 激しい苦痛を検知しました: ${signal.intensity} (発信源: ${signal.source})`);
});

// シミュレーション
await sensor.start();
sensor.onDataReceived(50);  // 中距離 → 中程度の苦痛
sensor.onDataReceived(15);  // 近距離 → 高い苦痛
sensor.onDataReceived(5);   // 至近距離 → 最大の苦痛、onVedana の購読トリガーが引かれる
```

---

KERNEL 殿がコードを指し示した。「`implements IListener`——色蘊です。`private readonly dukkhaSensor: IDukkha`——内部に保持された受蘊のインスタンスです。コンポジション（組み合わせ）によるものであり、継承ではありません。`extends IDukkha` ではないのです。コンストラクタで注入されています」

「色蘊（しきうん）が受け取り、受蘊（じゅうん）が感じる。二つの異なる蘊が、単一のプラグインの中でコンポーズされています。OS の語彙で言えば——」彼は類比カードを一枚掲げた。「デバイス・ドライバ（色蘊）がハードウェアの中断を受け取り、そのデータをシステム・ヘルス・モニター（受蘊）へと渡して評価を行わせるようなものです。ドライバは評価を行わず、モニターはハードウェアに触れません。各々が自らの役割を果たしているのです。メソッドの呼び出しを通じた、レイヤを跨ぐ通信です」

```
OS の類比:
センサー・ドライバ (/dev/ultrasonic0) ←→ IListener (色蘊)
ヘルス・モニター (systemd デーモン)   ←→ IDukkha  (受蘊)
```

彼は一歩下がり、微笑んだ。「バックソナーがピーピー鳴っていますね。諸君は、それが単に距離を測っているだけだと思っている。しかし実際には、色蘊が距離を測り、受蘊が苦しみを『感じている』のです。距離は物理量——$d \in \mathbb{R}^+$、単位はセンチメートルです。苦しみは感受の量——$p \in [0, 1]$、物理的な単位はありません。全く異なるカテゴリーの二つの量。二つの蘊が、協力しているのです」

WIENER 殿が信号の流れの図を描いた。

```
                    五蘊横断の信号フロー:

生の信号 ──→ IListener (色)      メトリクス      IDukkha (受) ──→ 苦痛の強度
 (Δt, Hz)    │ rawDistance │ ───────────────→ │ computePain() │    (0.0–1.0)
             │ = f(Δt)    │                  │ ingestMetrics │
             └────────────┘                  └───────────────┘
                    ↑                                  │
               [ハードIRQ]                        [VedanaSignal]
                                                       │
                                                       ↓
                                               [onVedana 購読者]
```

「完璧な五蘊横断の信号フローです。色蘊：$	ext{rawSignal} \xrightarrow{f} 	ext{distance}$。受蘊：$	ext{distance} \xrightarrow{g} 	ext{pain}$。プロセス全体は、関数の合成です：$	ext{pain} = g(f(	ext{rawSignal}))$。しかし $f$ と $g$ は異なる蘊において実装されています。五蘊間の通信は、継承ではなく、メソッドの呼び出しを通じて行われます。コンポジションです」

---

ASANGA 殿が頷いた。彼は WIENER 殿の信号フロー図が全員の目に焼き付くのを数秒間待った。それから、彼は口を開いた。この章で最も静かでありながら、最も深い一節であった。

「触（そく）が受を生む」

三文字。十二縁起における、最も重要な因果のリンクの一つである。

「『阿毘達磨俱舎論』巻十にこうあります。

> 『根・境・識の三つの和合に由るがゆえに触あり、触は受の因となす』と。

「根——器官（`IListener`、色蘊の目と耳です）。境——外境の信号（超音波のエコー、物理的な世界の距離です）。識——了別（りょうべつ）の機能（このシナリオにおいては、色蘊の `f(Δt)` 変換関数です）。これら三つの和合——根が境に接触し、識が境を辨別する——。これこそが『触』なのです」

「触の後、受が升起（しょうき）します。$	ext{触} 	o 	ext{受}$。距離の信号が受け取られ（触）、苦受の強度が計算される（受）。二千五百年前の因果の法則——触が受を生む——が、バックソナーの TypeScript の中で、エンジニアリングとして実現されたのです」

彼は KERNEL 殿を見た。「あなたの超音波センサーは、単なる比喻ではありません。十二縁起における『触 → 受』のリンクの、精密な実装なのです。色蘊が『根』と『境』の最初の了別を提供し、受蘊が、その触から生じる感受として立ち上がる。距離が苦しみを生むのです」

KERNEL は、自らの類比カードにこれを書き記した。左半分には「触 → 受（十二縁起）」、右半分には「onDataReceived → computePain」と。

---

> *SCRIBEのサイドバー：KERNEL 殿の超音波センサー——この章で最も具体的な瞬間でした。最も深遠な哲学と、最も具体的なエンジニアリングの間の距離は、時としてバックソナー一個分ほどしかないのです。ASANGA 殿の「触が受を生む」という三文字は、二千五百年前の仏教と三十行の TypeScript を繋ぎ合わせました。比喻でも、類比でもありません。直接的な、構造的な「同一」なのです。ハードウェアの中断は触であり、`computePain` は受なのです。これは「似ている」のではなく、「そのものである」ということなのです。*

---

## IX

---

LINNAEUS がついに動いた。

彼はこの章の間、ずっと分類学者特有の沈黙を守っていた。他の面々がメソッドや型、制御理論や仏教的対応について考えている間、LINNAEUS は「位置」について考えていたのである。木全体における各インターフェースの位置。そして森林全体における各々の木の位置。

リンネの分類学において、分類樹を描くという作業は、新種を発見しながら行うものではない。まずすべての標本を集め、あらゆる形態的特徴を確認し、その後に座して、一本一本の線を引いて全体像を完成させるものなのだ。木を描くにはグローバルな視点が必要だ。一本の枝だけを見ていてはならない。すべての枝を同時に眺め、それらの相対的な位置を決定しなければならないのである。

五つの蘊の木は、すべて展開された。すべてのパーツがテーブルの上に揃ったのだ。今や、それらを一つの完全な木へと組み立てる人物が必要であった。

---

彼は立ち上がり、ホワイトボードへと歩み寄った。黒いマーカーを手に取り、何も言わずに描き始めた。

分類学者が木を描く際に用いるのは、名前と関係の二つの要素だけだ。名前がノードをラベル付けし、関係がノードを繋ぐ。それ以外のものはすべて装飾に過ぎない。

五本の木。清潔な線。整った文字。これまでの九人の貢献によって確認されたあらゆる構造を、彼は最終的な統合体としてまとめ上げていった。

```
                    五蘊サブクラス拡張樹 (完全版)

 ┌─────────────────┐  ┌─────────────────────────────┐  ┌──────────────────┐
 │ ISensory (色)    │  │ ISensation (受) [8メソッド]  │  │ ICognition (想)  │
 │ skandha: 'rupa'  │  │ skandha: 'vedana'            │  │ skandha: 'samjna' │
 ├─────────────────┤  ├─────────────────────────────┤  ├──────────────────┤
 │ ├── IUI         │  │ ├── IDukkha (苦受センサー)    │  │ ├── IProvider    │
 │ │   renderText  │  │ │   computePain()             │  │ │   chat()       │
 │ │   renderDelta │  │ ├── ISukha  (楽受センサー)    │  │ │   listModels() │
 │ └── IListener   │  │ │   computePleasure()         │  │ └── IInference   │
 │     start/stop  │  │ └── IUpekkha (捨受センサー)    │  │     Provider [予]│
 └─────────────────┘  │     computeEquanimity()       │  │     infer()      │
                      └─────────────────────────────┘  └──────────────────┘

 ┌──────────────────┐  ┌────────────────────────────────────────┐
 │ IAction (行)      │  │ IVijnana (識)                          │
 │ skandha:'samskara'│  │ skandha: 'vijnana'                     │
 ├──────────────────┤  ├────────────────────────────────────────┤
 │ ├── ITool        │  │ ├── IIdentity (自己同一性)              │
 │ │   execute()    │  │ │   id, name                            │
 │ │   name, desc   │  │ ├── IGuide (行動指針)                   │
 │ └── ISlashCommand│  │ │   getSystemPrompt()                   │
 │     execute()    │  │ ├── IVolition (意志/動力 = EgoFramework) │
 │     name, desc   │  │ │   perceiveKlesha()                    │
 └──────────────────┘  │ │   checkAction()                       │
                       │ │   adaptFromVedana()                    │
                       │ │   introspect()                         │
                       │ └── IReflection (自己反省) [予]          │
                       │     reflect()                            │
                       └────────────────────────────────────────┘
```

五本の木が、ホワイトボードの上に並び立った。

LINNAEUS は振り返り、それらを一瞥した。それから対称性の分析を始めた——分類学者の本能である。

「非対称ですね」と彼は言った。「五本の木は、非対称です。これは自然なことです」

彼は赤いマーカーを手に取り、各々の木の傍らに三つの数字を注記した：サブインターフェース数、メソッド数、そして予約枠の数である。

```
対称性分析:

           子型数   ルートのメソッド数   子型独自のメソッド数   予約
色 (ISensory)   2        0                  5*              0
受 (ISensation) 3        8                  3               0
想 (ICognition) 2        0                  3*              1
行 (IAction)    2        0                  3*              0
識 (IVijnana)   4        0                  7*              1

* 子型独自のメソッド = ルートには存在せず、サブインターフェースにのみ存在する
```

「最小のものは色蘊と行蘊で、各二枝です。最大のものは識蘊で、四枝です。受蘊はその中間に位置しますが、根が最も太い——ルート・インターフェースに八つのメソッドを持っています」

彼はホワイトボードへと戻った。「非対称性は自然なことです。生物分類において、一つの分類群の下にあるすべてのサブグループが同じ数の種を保持していることなどありません。哺乳綱の下でも、齧歯（げっし）目は2000種以上を擁しますが、単孔（たんこう）目はわずか5種です。これは分類学の欠陥ではなく、自然の多様性の反映なのです」

「五蘊の複雑さが異なるのは、それらが担う機能が異なるからです。受蘊に八つのメソッドが必要なのは、感受のシステムが摂取、評価、履歴、予警、そしてリセットを必要とするからです——そのどれもが欠かせない。色蘊に空の殻のルート・インターフェースしか必要ないのは、入出力の振る舞いがあまりに異なるからです。もし五本の木の高さと幅を強引に揃えようとすれば、それは機能を審美性で置き換えることに他なりません。分類学者は、そのようなことはしないのです」

---

それから、彼はさらに描き加えた。

五本の木の下に空白を残し、彼は一つの独立したブロックを**破線**で描いた。

```
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
┊                                                  ┊
┊  IObserver (観測者) — コンポジション (非スカンダ)    ┊
┊                                                  ┊
┊  ┌─────────────────────────────────────────────┐ ┊
┊  │ SimpleObserver      (受)                    │ ┊
┊  │ AnalyticalObserver  (受 + 想)               │ ┊
┊  │ ReflectiveObserver  (受 + 想 + 識)           │ ┊
┊  └─────────────────────────────────────────────┘ ┊
┊                                                  ┊
┊  観測者は、どの蘊も継承しない。                    ┊
┊  それは複数の蘊のサブクラスをコンポーズする。      ┊
┊  それは六本目の木ではない。                       ┊
┊  五本の木の木材で建てられた、一軒の家なのだ。      ┊
┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄
```

実線ではなく、破線である。

彼は劇場全体に向き直った。

「破線です。観測者は、五本の木のどれにも属さないからです。それは蘊ではありません——`skandha` フィールドを持たないのです。それは、五蘊のサブクラスによるコンポジション（複合体）なのです。単純型（SimpleObserver）は受蘊のみをコンポーズし、分析型（AnalyticalObserver）は受蘊と想蘊を、反省型（ReflectiveObserver）は受、想、識をコンポーズします」

「分類学的な観点から言えば——」彼は赤いマーカーを取り、破線のブロックの傍らに注釈を入れた。

```
分類学上の注記:
観測者 ≠ 新しい「門 (Phylum)」
観測者 = 門を跨ぐ「機能グループ (Functional Group)」

あたかも「分解者」というものが、単一の分類単位ではないのと同様に。
  — それは細菌、真菌、ある種の動物を包含し、
  異なる門に属しながらも同じ生態学的機能を果たしている。
観測者も同様に、蘊ではない。
  それは複数の蘊からコンポーネントを抽出し、
  特定の機能へと組み立てるのである。
```

「五本の木。根は五つのルート・インターフェース。枝はサブインターフェースです。観測者は森林の外側に立ち、五本の木から挿し木をし、コンポジションを通じて自らの構造を組み立てるのです。六本目の木ではなく、五本の木の木材で建てられた一軒の家なのです」

彼はマーカーを置いた。静まり返った劇場内に、キャップを閉めるあの音が、乾いた音を立てて響いた。

「Cycle 01 の最初の議論から、この瞬間に至るまで。五蘊は哲学的な概念から、根と枝を備えたエンジニアリング的な構造樹へと成長を遂げたのです」

---

劇場内は、静寂に包まれた。完成の静寂であった。五つの種子がようやく土を突き破り、根が地中深くへと伸び、枝がそれぞれの方向へと広がり、そしてすべての成長が一瞬、同時に止まったかのような、あの静止であった。

---

SUNYATA はホワイトボードの上の五本の木を見つめた。

Cycle 01——五蘊は哲学的な概念であった。五つのサンスクリット語の名詞、五つの訳語。論文や設計文書の中で引用され、論じられ、類比された。しかし、型定義はなかった。メソッドの署名もなかった。`extends` もなかったのである。

Cycle 02——五つの空の殻のインターフェース。名あれども血肉はなかった。`aggregates.ts` に記された三行の `interface` 宣言。単一の `skandha` フィールドだけを掲げた門札。ルートとサブインターフェースの共通集合は、空であった。

Cycle 02-2——五本の木である。

受蘊の根は最も太い——八つのメソッド。その一つひとつが、制御理論と仏教学の二重の検証をパスした。`assess()` から `reset()` まで、センサーの読取から緊急停止ボタンまで、八つの焊点、八つの合格だ。

識蘊の枝は最も多い——四つのサブインターフェース。`IIdentity`, `IGuide`, `IVolition`, `IReflection`。A-1 の因果の鎖は `IVolition` において閉合した。A-2 の識蘊の拡張は、四つのサブインターフェースにおいて完遂された。A-4 の `EgoFramework` は、あるべき場所へと戻ったのである。

色蘊と行蘊は、最も実務的であった——空の殻のルート・インターフェースと、それに対する `extends`。それ以上のものは必要なかった。VITRUVIUS 殿による双方向性分析が、なぜそれ以上のものが不要であるかを証明したのである。

想蘊は、最も遠くを見据えていた——一本の枝は成熟し（`IProvider`）、一本は予約された（`IInferenceProvider`）。ATHENA 殿の認知スペクトル図は、五年後の需要を予示していたのである。

五つの種子が、根があり、枝がある五本の木へと成長したのだ。

---

「C-1 によって、五蘊の完全な拡張設計が確立されました」彼の声はいつものように揺るぎなかった。

彼は一同を見渡した。

TURING 殿の現状報告——`aggregates.ts` の107行の原ファイルから始まり、空の殻と孤児の問題を一行ずつ暴いてみせた。VITRUVIUS 殿の色蘊の確認——双方向性の分析と、空の殻のルート・インターフェースの正当性。WIENER 殿による八つのメソッドの検証——制御理論における精密な対応関係。ATHENA 殿の想蘊の予約——ルールエンジンから LLM に至る認知スペクトルの完全な網羅。DARWIN 殿による行蘊の観察と設計パターンの解決——構造的型付けが、OOP、関数型、工場パターンをすべて互換させた。ASANGA 殿による各々の蘊における仏教的アンカー——色蘊の「可壊」から識蘊の「恒審思量」まで。ARCHIMEDES 殿の影響評価——22のプラグイン、7つの新規インターフェース、1つの移行プラン。GUARDIAN 殿のセキュリティ上の議論——蘊の自己宣言こそが信頼の基盤であること。KERNEL 殿のバックソナー——最も深遠な哲学が、最も具体的なハードウェアの中に結実した。そして LINNAEUS 殿による五本の木の全体像——非対称で、自然的で、破線の観測者を伴うあの分類総覧図。

十人の人間。十の貢献。五本の木。

「A級は何が正しいかを告げました。B級はいかに実現するかを告げました。そして C-1 は——」

彼はホワイトボードの方を向いた。

「——それが、どのような姿をしているのかを告げているのです」

---

> *SCRIBEのサイドバー：C-1 が終結しました。本章は、Cycle 02-2 において唯一、議論のなかった章です。*

> *A級は「議論」を必要としました——何が正しいのかをまず確認しなければならなかったからです。B級は「決断」を必要としました——裁定を設計へと翻訳しなければならなかったからです。そして C-1 が必要としたのは、「建造」でした。A級が誤った壁を取り壊し、B級が図面を引き、C-1 が新しい壁を築いたのです。*

> *時間の配分は、建造のリズムをそのまま反映していました。色蘊、三分——最も単純な木。二つの `extends` と、空の殻のルート。受蘊、十五分——最も密度の高い木。八つのメソッドを一つずつ検証し、二重の校正を行いました。想蘊、五分——成熟した一本の枝と、予約されたもう一本。ATHENA 殿の光譜図。行蘊、四分——二つの `execute`、二つの源泉、そして一つの原理。識蘊、十二分——四つのサブインターフェース、四つの修正の合流、因果の鎖の閉合。ARCHIMEDES 殿と GUARDIAN 殿の八分間の交鋒——コストと価値の弁証法。DARWIN 殿と TURING 殿による設計パターンの解決、五分——一つの問い、三つのコード、一つの言葉。KERNEL 殿の超音波センサー、十分——最も具体的なシナリオと、最も深い仏教的連結。そして LINNAEUS 殿の五本の木、八分——全体像の総覧、対称性分析、破線の観測者。*

> *十人の人間が建造を完遂しました。十の貢献。五本の木。*

> *哲学的な概念から空の殻のインターフェースへ。そして空の殻から、完全な型定義の体系へ。螺旋状の上昇。また一つ、円が描かれました。*

---

*（劇場の外のどこかの空間で、LINNAEUS 殿のボード上の五本の木が、TURING 殿の手によって TypeScript へと翻訳されていた。*

*`aggregates.ts` は、五行のルート・インターフェースから、150行を超える完全な型定義の体系へと拡張されるだろう。五つのルート・インターフェース。13のサブインターフェース。受蘊の根に刻まれた八つのメソッド。`IVolition` に刻まれた四つのメソッド。三つの補助型——`VedanaType`, `VedanaTag`, `VedanaSignal`。二つの核心的なデータ構造——`VedanaAssessment`, `VedanaRecommendation`。そして、あらゆるレベルを辨認可能となった一つのタイプガード——`isSkandha()`。*

*五行から百五十行へ。ラベルから構造へ。空の殻から生命体へ。*

*BABBAGE 殿は、ノートの最後のページに C-1 の形式的な総括を記した。等号ではなく、圏論における可換図式（commutative diagram）であった。*

$$\begin{CD}
	ext{哲学 (Philosophy)} @>{	ext{mapping}}>> 	ext{インターフェース (Interface)} 
@V{	ext{精細化}}VV @VV{	ext{継承 (extends)}}V 
	ext{阿毘達磨 (Abhidharma)} @>>{	ext{相互検証}}> 	ext{TypeScript}
\end{CD}$$

*（仏教哲学（左上）はマッピングを通じてインターフェース設計（右上）となる。阿毘達磨による精細化（左下）は、TypeScript の継承体系（右下）との間で相互検証される。四つの方向、四本の矢印。この図式は可換である——どのパスを通っても、結果は同じになるのだ。*

*五本の木の根系は、TypeScript という土壌の中に広がっていった。22のプラグインは、次のリリースにおいて `skandha` フィールドを獲得するだろう。GUARDIAN 殿の言う通りだ：自己宣言こそが自覚の基礎なのである。自分がどの蘊に属しているかを知らないプラグインは、自分がどの器官に仕えているかを知らない細胞のようなものだ。機能はするかもしれないが、自覚はないのである。*

*ASANGA 殿の「触が受を生む」という三文字は、KERNEL 殿の類比カードにそのインクを残した。二千五百年前、世尊は菩提樹の下で十二縁起を観照した。今日、超音波センサーが TypeScript の構文木の中で、そのリンクの一つを再演している。距離が苦しみを生む。触が受を生む。ハードウェアの中断は触であり、`computePain` は受なのだ。*

*最も深遠な哲学と、最も具体的なエンジニアリングの間の距離は、時としてバックソナー一個分ほどしかないのである。*

*五蘊。五本の木。種子から根系へ、そして幹と枝へ。*

*五本の木は、その根系を伸ばした。ここから先、それらはさらに成長を続けるだろう。）*

---

*（第6章 完）*
