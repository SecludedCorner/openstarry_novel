# 第三章：差異レポート

---

TURING は、準備というものを必要としたことがない。

正確に言えば、彼のオペレーション・モードにおいて、「準備」と「正式な開始」の間に相転移の境界（phase transition boundary）は存在しない。SUNYATA が Cycle 02 の研究対象を v0.24.0-beta へ更新すると宣告したその瞬間――ミリ秒単位で精緻なそのタイムスタンプが刻まれた時から――彼はすでに作業を開始していた。

彼の四つのターミナル・ウィンドウには、新旧両バージョンのソースコード・ツリーが同時に開かれていた。左半分は v0.22.1-beta、右半分は v0.24.0-beta。それはまるで、解剖台の両側に、同一の身体の異なる時点での X 線写真を並べて広げたかのようだった。彼が用いるのはグラフィカルな diff ツールではない。人間が読むために設計された、赤や緑で削除と追加をハイライトするツールではなく、彼自身が Cycle 01 で構築した独自の分析パイプラインであった。

```
TURING の差異分析パイプライン (Diff Analysis Pipeline)

Phase 1: 構造層 (Structural)
  ┌─ tree-diff: ディレクトリ・ツリーの比較
  │  └─ output: 追加/削除/リネームされたファイルリスト
  ├─ stat-diff: ファイル統計 (行数, サイズ, 更新日時)
  │  └─ output: 変更規模マトリクス
  └─ dep-diff:  import/export 依存グラフの差異
     └─ output: 依存関係変更図

Phase 2: 意味層 (Semantic)
  ┌─ type-diff: TypeScript 型システムの比較
  │  ├─ interface の追加/修正/削除
  │  ├─ type alias の変更
  │  └─ generic parameter の変更
  ├─ api-diff:  パブリック API 表面積の計算
  │  └─ output: 破壊的変更（breaking changes）リスト
  └─ doc-diff:  JSDoc/コメント内容の比較
     └─ output: 意味論的タグ（@skandha 等）変更マップ

Phase 3: 振る舞い層 (Behavioral)
  ┌─ test-diff: テストカバレッジの変化
  ├─ flow-diff: コントロールフロー図の差異
  └─ emit-diff: イベント発行パターンの変更
     └─ output: EventBus トポロジー変化図
```

彼は設計ドキュメントを読まない。差異を読んでいるのだ。

一行ずつ。一文字ずつ。`packages/sdk/src/` のルートディレクトリから始まり、修正されたすべてのファイルパスを辿り、変更が加えられたすべてのバイトに触れるまで。

情報理論において、差異（diff）とは二つのシステム状態の間の相互情報量（mutual information）である。旧バージョン $X$ と新バージョン $Y$ が与えられた時、差異の情報量は次のように表される。

$$I(X; Y) = H(X) + H(Y) - H(X, Y)$$

ここで $H(X)$ と $H(Y)$ はそれぞれのバージョンのエントロピーであり、$H(X, Y)$ は結合エントロピーである。二つのバージョンが完全に同一の時、$I(X; Y) = H(X) = H(Y)$ となり、差異はゼロである。二つのバージョンが完全に異なる時、相互情報量はゼロに収束する。つまり、両者の間に圧縮可能な共通パターンが存在しないということだ。TURING が探しているのは、$I(X_i; Y_i) 
eq 0$ であるファイル――変化という情報を携えたノードたちである。

---

円形劇場が再び静寂を取り戻した時、TURING はすでに分析を完了していた。

他の研究員たちは、R-01 から R-05 までの各グループのスペースへと散らばり始めていた。しかし、SUNYATA が全員を呼び戻した。

「TURING の差異レポートです。」彼は一言、そう言った。

その口調には、全員が聞き覚えのある重々しさが含まれていた。Cycle 01 の時と同じ重々しさだ。あのサイクルにおいて、TURING によるコードの事実報告は、その後のすべての研究における「アンカー（錨）」となった。SYNTHESIST は当時、「経験的なアンカー」という言葉を用いた。あらゆる哲学的な分析、制御理論的なモデリング、セキュリティ評価――それらがいかに精緻であったとしても、最終的には TURING のレポートにある特定のコード行、行番号、事実に辿り着けなければならないのだ。

BABBAGE は心の中で、迅速なメタ分析を行った。「アンカー」は形式的なフレームワークにおいて何に対応するのか？ それは公理系における「公理（axiom）」――もはや「なぜ」と問うことのできない基礎的な命題である。すべての定理（theorem）は公理から導出されなければならない。TURING の示すコードの事実は公理である。そして他のメンバーによる哲学、セキュリティ、制御理論的な分析は定理である。もし定理が公理にまで遡ることができないのであれば、その定理は宙に浮いていることになる。論理空間を漂うだけで、根基を持たないのだ。

$$	ext{Axiom (TURING)} \xrightarrow{	ext{inference}} 	ext{Theorem (all others)}$$

今、アンカーが再び打ち込まれようとしていた。

---

十九のノードが再び円形劇場に集結した。PENROSE は新しい椅子に座り、静かに待っていた。オーケストラに加わったばかりの新入団員が、最初の合奏の前に首席奏者のチューニングに耳を傾けるかのように。

TURING に挨拶はない。彼の声は、最初の音節から、安心感を覚えるほどの精密さを湛えた冷静さを伴っていた。氷のような信頼性だ。

「v0.22.1-beta から v0.24.0-beta。核心的なソースコードの差異です。」彼は言った。「四つの階層に分けて報告します：追加、修正、タグ、そして問題点です。」

彼は一枚の総括表を投影した。それは単なる統計グラフではなく、構造的な意味論に基づいた変更マトリクスであった。

```
v0.22.1-beta → v0.24.0-beta 変更マトリクス

┌──────────────────┬──────┬──────┬──────┬──────────────┐
│ カテゴリ          │ SDK  │ Core │ 合計  │ 意味的ウェイト  │
├──────────────────┼──────┼──────┼──────┼──────────────┤
│ 追加ファイル      │  2   │  1   │  3   │ ████████ 高  │
│ 修正ファイル      │  7   │  4   │  11  │ ██████ 中    │
│ 削除ファイル      │  0   │  0   │  0   │              │
│ 新規 @skandha タグ│ 16   │  6   │  22  │ █████████ 極高│
│ 追加テスト        │  2   │  1   │  3   │ ████ 中      │
│ テスト数の変化    │ 4→6  │25→26 │75→78 │ ██ 低        │
│ 未修正ファイル(検証)│ 17   │ 22+  │ 39+  │ — 基線は安定  │
└──────────────────┴──────┴──────┴──────┴──────────────┘
```

VITRUVIUS は僅かに目を細めた。一端全端アーキテクトである彼の目にまず飛び込んできたのは、個別の数字ではなく、Monorepo のトポロジー的な分布だった。SDK で七つの修正、Core で四つの修正――修正の重心は SDK に偏っている。これは、v0.24.0 の核心的な変更が振る舞いのレイヤー（Core の実行ロジック）ではなく、型のレイヤー（SDK の型定義）にあることを意味している。実装よりも宣言。血肉よりも骨格が優先されているのだ。

---

## 一、追加ファイル

「三つの新規ファイル。」TURING が言った。「三十でも、十三でもない。三つです。」

彼はその数字を一瞬、宙に留めた。

「一つ目。`packages/sdk/src/types/aggregates.ts`。百七行。」

それは先ほど全員が目にしたファイルだ。五蘊（ごうん）の根インターフェース。しかし、TURING がそれを提示する方法は先ほどとは異なっていた。彼はそれが「何であるか」ではなく、「どれほどあるか」を提示したのだ。計量学（メトロロジー）。精密な測定である。

彼はファイルの完全な構造分析を投影した。

```typescript
// aggregates.ts 構造分析 (107 行)

// === モジュールレベル JSDoc (行 1-10) ===
/**
 * Five Aggregates (五蘊) Root Interfaces.
 * D-02 Decision: Dual naming — English as primary,
 *   Sanskrit as annotation.
 * @module aggregates
 */

// === 五つの根インターフェース (行 12-86) ===
export interface ISensory {
  /** @skandha rupa */
  readonly skandha: 'rupa';    // 色蘊: コード3行, JSDoc 9行
}

export interface ISensation {
  /** @skandha vedana */
  readonly skandha: 'vedana';  // 受蘊: コード3行, JSDoc 11行
}

export interface ICognition {
  /** @skandha samjna */
  readonly skandha: 'samjna';  // 想蘊: コード3行, JSDoc 8行
}

export interface IAction {
  /** @skandha samskara */
  readonly skandha: 'samskara'; // 行蘊: コード3行, JSDoc 7行
}

export interface IIdentity {
  /** @skandha vijnana */
  readonly skandha: 'vijnana';  // 識蘊: コード3行, JSDoc 9行
}

// === 共用体型 + 型ガード (行 88-106) ===
export type Skandha = 'rupa' | 'vedana' | 'samjna'
                    | 'samskara' | 'vijnana';

export function isSkandha<S extends Skandha>(
  obj: unknown, skandha: S
): obj is { skandha: S } { /* 6行の実装 */ }
```

「ISensation の内容はすでに見ましたね。」TURING が言った。「一つ、計量的な事実を補足させてください。」

彼はインターフェースの統計表を投影した。

```
aggregates.ts インターフェース計量分析
┌─────────────┬───────────┬────────────┬──────────┬──────────┐
│ インターフェース│ JSDoc 行数 │ コード行数  │ ドキュメント比│ 情報密度  │
├─────────────┼───────────┼────────────┼──────────┼──────────┤
│ ISensory    │     9     │     3      │ 3.0:1   │ 0.33     │
│ ISensation  │    11     │     3      │ 3.7:1   │ 0.27     │
│ ICognition  │     8     │     3      │ 2.7:1   │ 0.38     │
│ IAction     │     7     │     3      │ 2.3:1   │ 0.43     │
│ IIdentity   │     9     │     3      │ 3.0:1   │ 0.33     │
├─────────────┼───────────┼────────────┼──────────┼──────────┤
│ 平均         │    8.8    │     3      │ 2.9:1   │ 0.35     │
│ isSkandha   │     3     │     6      │ 0.5:1   │ 2.00     │
└─────────────┴───────────┴────────────┴──────────┴──────────┘

情報密度 = コード行数 / (JSDoc 行数 + コード行数)
```

「五つの根インターフェースは、構造上、完全に同型です。」TURING が言った。「差異はコメントの中にのみ存在します。コード本体はすべて同じパターンです：`readonly skandha` フィールドのみを持つインターフェース。平均ドキュメント比は 2.9対1 です。一行のコードの背後には、その哲学的な含意を説明する三行のドキュメントが存在しています。」

DARWIN は僅かに動いた。彼はそこに一つのパターンを見ていた。ドキュメント比 2.9対1 というのは、これらのインターフェースが現在は「機能的（functional）」なものではなく「宣言的（declarative）」なものであることを意味する。進化生物学において、機能に先んじて宣言が現れることがある。ゲノムにおける調節配列（regulatory sequence）が、コード配列（coding sequence）に先んじて淘汰圧によって形作られるのと同様だ。ISensory の九行の JSDoc は調節配列である。「この構造はどのように使われるべきか」を未来の開発者に告げている。しかし、構造自体はまだ三行のコードに過ぎない。

「二つ目の新規ファイル。`packages/sdk/src/types/__tests__/aggregates.test.ts`。四十三行。」TURING が言った。「五蘊の根インターフェースの `skandha` フィールドの値と、`isSkandha` 型ガードをテストするものです。これらのテストはすべてパスしています。」

「三つ目。`packages/sdk/src/types/__tests__/events.test.ts`。三十二行。`TypedAgentEvent` ジェネリクスが payload の型を正しく推論できるかをテストしています。」

彼は間を置いた。

「そして四つ目の新規ファイルですが、これは厳密には SDK ではなく Core に属します。`packages/core/src/agents/__tests__/slash-command-error.test.ts`。百二十三行。スラッシュコマンドが例外をスローした際に、`LOOP_ERROR` と `MESSAGE_SYSTEM` イベントが正しく発行されるかをテストしています。」

TURING はここで、彼にしては珍しく、背景情報の補足を加えた。

「v0.22.1 において、スラッシュコマンドのエラー処理は `logger.error()` だけでした。」

彼は二つのコードの精緻な比較を投影した。

```typescript
// ═══ v0.22.1-beta: 沈黙した失敗 ═══
// packages/core/src/agents/agent-core.ts
.catch((err) => {
  logger.error("Slash command error", { error: String(err) });
  // エラーはここで死んでいる。イベントも、通知もない。
  // UI は何が起きたかを知ることができない。
  // ユーザーがバグのあるコマンドを入力しても、
  // インターフェースは全く反応を返さない。
});

// ═══ v0.24.0-beta: イベントの伝播 ═══
// packages/core/src/agents/agent-core.ts (行 406-430)
.catch((err) => {
  const errMsg = err instanceof Error ? err.message : String(err);
  logger.error("Slash command error", { error: errMsg });

  // NEW: EventBus へのエラーのブロードキャスト
  bus.emit({
    type: AgentEventType.LOOP_ERROR,
    timestamp: Date.now(),
    payload: {
      error: errMsg,
      sessionId: currentSessionId,
      replyTo: currentReplyTo,
    },
  });

  // NEW: UI へのシステムメッセージの送信
  bus.emit({
    type: AgentEventType.MESSAGE_SYSTEM,
    timestamp: Date.now(),
    payload: {
      text: `Command error: ${errMsg}`,
      sessionId: currentSessionId,
      replyTo: currentReplyTo,
    },
  });
});
```

「沈黙した失敗（Silent failure）。」KERNEL が OS エンジニアの口調でその言葉を漏らした。彼の世界において、沈黙した失敗は最も危険な失敗である。なぜなら、誰もそれが起きたことに気づけないからだ。

彼は OS レベルの精緻な類比を付け加えた。「POSIX システムにおいて、`errno` が存在するのはまさに沈黙した失敗を避けるためです。システムコールが失敗した時は必ず `errno` をセットし、上位の呼び出し側にチェックする機会を与えなければなりません。v0.22.1 のスラッシュコマンドのエラー処理は、システムコールが失敗したのに `errno` をセットしないようなものです。`logger.error()` はログを書き出しますが、ログは呼び出し側ではなく、運用保守担当者が読むためのものです。UI こそが呼び出し側なのです。UI が必要としているのは、一行のログではなく、明確なエラー信号なのです。」

「v0.24.0 はそれを修正しました。」TURING が言った。「今やエラーは EventBus を通じて `LOOP_ERROR` と `MESSAGE_SYSTEM` イベントとしてブロードキャストされます。UI はそれを受信し、表示することができるようになりました。」

---

## 二、修正ファイル

TURING の語速は変わらない。精密機器のように、彼は一つのデータポイントに対して、多すぎず少なすぎず、全く同じ時間を費やす。

「十一の修正ファイル。SDK で七つ、Core で四つです。」

VITRUVIUS がここで、アーキテクチャ的な観察を差し挟んだ。彼の声には、建物の平面図を見ている時のような、空間的な感覚が宿っている。

「まず、Monorepo の依存関係のトポロジーを示させてください。」彼は一枚の図を投影した。

```
OpenStarry Monorepo 依存関係トポロジー (v0.24.0-beta)

    apps/runner ──────────────────────────────────┐
         │                                        │
         │ depends                                │
         ▼                                        │
    packages/core ──┬── agents/agent-core.ts      │
         │          ├── execution/loop.ts          │
         │          ├── infrastructure/ (5 registry)│
         │          ├── security/safety-monitor.ts  │
         │          └── sandbox/ (10 files, 0 changes)
         │                                        │
         │ depends                                │
         ▼                                        │
    packages/sdk ───┬── types/aggregates.ts [NEW]  │
         │          ├── types/events.ts     [MAJOR]│
         │          ├── types/listener.ts   [DOC]  │
         │          ├── types/ui.ts         [DOC]  │
         │          ├── types/provider.ts   [DOC]  │
         │          ├── types/tool.ts       [DOC]  │
         │          ├── types/guide.ts      [DOC]  │
         │          └── index.ts            [EXPORT]
         │                                        │
         │ depends                                │
         ▼                                        │
    packages/shared ── (0 changes)                │
    packages/plugin-signer ── (0 changes) ────────┘

変更のヒートマップ:
  ████ = 重大な変更 (aggregates.ts, events.ts)
  ██   = 中程度の変更 (agent-core.ts, loop.ts, index.ts)
  █    = 最小限の変更 (JSDoc のみ: 9 ファイル)
  ░    = 変更なし (39+ ファイル)
```

「変更は明確な階層パターンを示しています。」VITRUVIUS が総括した。「最下層の `shared` と `plugin-signer` は全く動いていません。SDK の型定義レイヤーが最大の変更密度を引き受けています。Core の振る舞いレイヤーは局所的な強化に留まっています。Runner レイヤー（アプリケーション層）は全く変更されていません。これは、型定義から始まり上方へと拡散していく、ボトムアップのタグ・システムの植え込みです。」

MESH が分散システムの観点から補足した。「これは漸進的なスキーマ・マイグレーション（schema migration）のようです。まずスキーマ（型定義）を更新し、その後にコンシューマー（利用者）を更新する。v0.24.0 はスキーマの更新を完了しました。コンシューマーの更新――つまり IListener に ISensory を extends させることなどは――次のバージョンに持ち越されたのです。」

---

TURING は SDK の分析を始めた。

「`types/events.ts`。変更規模：重大。百十六行の追加です。」彼は言った。「これが単一ファイルとしては最大の変更です。」

彼は `AgentEventPayloadMap` の完全な構造を投影した。省略形ではなく、完全な型マッピングである。しかし彼はそれを逐一読み上げるのではなく、構造として提示した。

```typescript
/**
 * AgentEventPayloadMap — イベント型安全システムの核心
 *
 * 設計パターン: Discriminated Union + Mapped Type
 * 役割: 各 AgentEventType に対して精緻な payload 構造を定義する
 */
export interface AgentEventPayloadMap {
  // ── ライフサイクルイベント (Lifecycle) ──
  [AgentEventType.AGENT_STARTED]:
    { identity: { id: string; name: string } };
  [AgentEventType.AGENT_STOPPED]: undefined;

  // ── 実行ループイベント (Execution Loop) ──
  [AgentEventType.LOOP_STARTED]:
    { source: string; traceId: string;
      sessionId?: string; replyTo?: string };
  [AgentEventType.LOOP_ERROR]:
    { error: string;
      sessionId?: string; replyTo?: string };
  // ... (全 42 種類のイベント型を完全にカバー)

  // ── セキュリティサンドボックスイベント (Sandbox) ──
  [AgentEventType.SANDBOX_WORKER_SPAWNED]:
    { pluginName: string; memoryLimitMb: number };
  [AgentEventType.SANDBOX_SIGNATURE_VERIFIED]:
    { pluginName: string };
  [AgentEventType.SANDBOX_SIGNATURE_FAILED]:
    { pluginName: string; error: string };
  // ...

  // ── MCP イベント (Model Context Protocol) ──
  [AgentEventType.MCP_SAMPLING_REQUEST]:
    { serverName: string; traceId: string;
      depth: number; messageCount: number };
  // ...
}
```

「Cycle 01 において、」TURING が言った。「DARWIN は `payload?: unknown` という定義を、『異なる宇宙から迷い込んできた型定義』と形容しました。」

DARWIN は僅かに動いた。その言葉を彼は覚えていた。

「その宇宙の裂け目は、今や `AgentEventPayloadMap` によって封鎖されました。」TURING が言った。「しかし、それはあくまで型のレイヤーでの話です。実行時は依然として JavaScript であり、型の安全性は強制されません。」

BABBAGE はノートに迅速に、形式的な注釈を記した。

$$	ext{TypeScript の型安全性} \in 	ext{compile-time guarantees} \setminus 	ext{runtime guarantees}$$

$$\forall e \in 	ext{AgentEvent}: 	ext{type-check}(e) = 	ext{true} 
Rightarrow 	ext{runtime-valid}(e) = 	ext{true}$$

「型消去（type erasure）ですね。」彼は低く言った。「TypeScript が JavaScript へとコンパイルされる際、すべての型情報は消去されます。`AgentEventPayloadMap` は `.js` の出力には何の痕跡も残しません。その恩恵は、開発者の IDE とコンパイラの中に完全に限定されます。これは『開発時の契約』であり、『実行時の契約』ではないのです。」

---

TURING は残りの六つの SDK の修正箇所へと進んだ。言葉は極限まで削ぎ落とされていたが、彼は詳細な変更対照表を投影した。

```
SDK 型ファイル @skandha タグ注入マトリクス

┌──────────────┬─────────────────────────┬─────────────────────────────────┐
│ ファイル       │ v0.22.1 JSDoc (行 2)    │ v0.24.0 JSDoc (行 2-3)          │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ listener.ts  │ "receives external      │ "sensory input channels."       │
│              │  input (受蘊)"          │ @skandha rupa (色蘊·感官根-入力) │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ ui.ts        │ "defines how the agent  │ "output rendering."             │
│              │  presents itself (色蘊)"│ @skandha rupa (色蘊·顕相-出力)  │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ provider.ts  │ "Provider interface --  │ "Provider adapter interface."   │
│              │  LLM backends."         │ @skandha samjna (想蘊·認知処理)  │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ tool.ts      │ "Tool interface and     │ "Tool interface -- executable   │
│              │  context types."        │  actions."                      │
│              │                         │ @skandha samskara (行蘊·意志行動)│
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ guide.ts     │ "Guide interface --     │ "Guide interface -- behavioral  │
│              │  provides system prompts│  framework."                    │
│              │  and persona."          │ @skandha vijnana (識蘊·我執枠組) │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ 構造上の変化   │         —              │ コードの変更は全ファイルでゼロ     │
└──────────────┴─────────────────────────┴─────────────────────────────────┘
```

「皆さん、お気づきですね。」彼は言った。「五つの SDK 型ファイル。すべて JSDoc の修正のみです。すべてに `@skandha` タグが追加されました。コードの変更は一行もありません。」

「タグはドキュメントであり、契約ではない。」ARCHIMEDES が言った。彼の口調に批判の色はなく、単なるエンジニアの本能的な反応――宣言と実装を峻別する反応であった。

LINNAEUS がここで、分類学的な観察を加えた。彼はノートに小さな分類マトリクスを描いた。

「ヘニックの分岐分類学（Henngian cladistics）の言語を用いて、これらのタグを再記述させてください。」彼の声には、診断的形質（diagnostic characters）を識別しようとする分類学者特有の集中力が宿っていた。

「分岐分類学において、種をグループ化する基準は、表面的な類似性（overall similarity）ではありません。それは表現分類学（phenetics）の手法です。グループ化の根拠となるのは、共有派生形質（synapomorphy）です。」

彼は一枚の分岐図を投影した。

```
@skandha タグの分岐分析 (Cladistic Analysis)

共有派生形質: @skandha タグの存在

               ┌── IListener  ─── @skandha rupa
               │
 ISensory(rupa)┤                           ← 共有派生形質:
               │                              skandha = 'rupa'
               └── IUI        ─── @skandha rupa
                                    (相同形質 homology)
        ───────────────────────
               ┌── IProvider   ─── @skandha samjna
ICognition     │                           ← 固有派生形質:
(samjna)       └── (他のメンバーなし)           skandha = 'samjna'

        ───────────────────────
IAction        ┌── ITool       ─── @skandha samskara
(samskara)     └── (他のメンバーなし)    ← 固有派生形質

        ───────────────────────
IIdentity      ┌── IGuide      ─── @skandha vijnana
(vijnana)      └── (他のメンバーなし)    ← 固有派生形質

        ───────────────────────
ISensation     ┌── SafetyMonitor── @skandha vedana (placeholder)
(vedana)       └── (専用モジュールなし)    ← 偽派生形質 (plesiomorphy)?
```

「最後の一行に注目してください。」LINNAEUS の口調が僅かに引き締まった。「SafetyMonitor に対する `@skandha vedana` タグ。これは分類学において、一つの精緻な問いを提示しています。SafetyMonitor の『安全防護』という機能と、受蘊の『感受』という機能は、相同（homology）なのか、それとも収斂進化（convergence）なのか？」

彼は DARWIN を見た。

「もし相同であるなら――それらは共通の祖先機能を共有しており、SafetyMonitor は確かに受蘊の職能の一部を担っていることになります。もし収斂進化であるなら――それらは表面上似ているだけで、機能の起源は全く異なります。安全防護は感受ではありません。カウンターは痛覚ではないのです。」

DARWIN が頷いた。「生物学において、コウモリの翼と鳥の翼は収斂進化です。機能（飛行）は似ていますが、構造の起源（前肢の骨 vs 羽毛）は異なります。SafetyMonitor の frustration カウンターと、受蘊の三受システム。私は収斂進化の方に一票を投じます。」

「正解です。」TURING が確認した。「それはタグにある `placeholder`（占位符）という記述とも一致します。開発チーム自身、それが暫定的な代役であり、相同ではないことを理解しているのです。」

---

彼は Core の四つの修正箇所へと向き直った。

「`agents/agent-core.ts`。三つの変更点があります。」

「第一の点：`loadPlugins()` メソッドの追加です。複数のプラグインを一括でロードし、正しくイベントを発行できるようになりました。v0.22.1 までは `loadPlugin()` ――単数形のみでした。今や複数形バージョンが存在します。」

彼はメソッドのシグネチャを投影した。

```typescript
/**
 * Load multiple plugins with dependency ordering.
 * トポロジカルソートによって依存関係の順序を保証する。
 *
 * @param plugins - ロードするプラグインの配列
 * @emits PLUGIN_LOADED - 各プラグインのロード成功時
 * @emits PLUGIN_ERROR  - いずれかのロード失敗時
 */
async loadPlugins(plugins: IPlugin[]): Promise<void>
```

MESH が僅かに身を乗り出した。「トポロジカルソート。」分散システムの研究者にとって馴染み深い用語に、彼は反射的に反応した。「分散システムにおいて、トポロジカルソートは有向非巡回グラフ（DAG）を扱う際の標準的な手法です。プラグイン間の依存関係は一つの DAG を構成します。Plugin A が Plugin B に依存しているなら、B は必ず A より先にロードされなければなりません。」

彼はノートに簡単な DAG とそのトポロジカル順序を描いた。

$$G = (V, E) \quad 	ext{where } V = \{P_1, P_2, \ldots, P_n\}, \; E \subseteq V 	imes V$$

$$	ext{topological\_sort}(G) = [P_{\sigma(1)}, P_{\sigma(2)}, \ldots, P_{\sigma(n)}]$$

$$	ext{s.t.} \; \forall (P_i, P_j) \in E: \sigma^{-1}(i) < \sigma^{-1}(j)$$

「もし依存グラフに閉路（サイクル）があったら――A が B に依存し、B が A に依存していたら――トポロジカル順序は存在しません。npm のエコシステムにおいて、循環依存は現実的な問題です。現在の `loadPlugins()` は循環を検知していますか？」

「していません。」TURING が言った。「現在の実装は、依存グラフが DAG であることを前提としています。もし循環依存が存在する場合、その挙動は未定義です。」

---

「第二の点：スラッシュコマンドのエラー処理の改善。これはすでに新規ファイルのセクションで説明した通りです。」

「第三の点――」TURING の語速は変わらなかったが、SCRIBE は後に、彼がここで 0.5 秒だけ長く間を置いたことを記録している。「五蘊マッピングの修正です。`agent-core.ts` 内の四箇所のインラインコメントにおいて、従来の `// Start all listeners (受蘊)` が `// Start all listeners (色蘊 -- sensory input)` へと修正されました。」

NAGARJUNA が一度、頷いた。Cycle 01 において、受蘊が Listener に誤ってマッピングされている問題を指摘したのは彼だった。彼は中観哲学者としての精緻さをもって、この修正の因縁を回顧した。

「受蘊（*vedana*）とは主観的な感受です。苦、楽、そして捨。対して Listener は感官の入力チャネルであり、外部のデータを受信するものです。外部データを受信するモジュールを主観的な感受と呼ぶのは――」彼は半秒ほど言葉を探し、極めて精緻な類比を選び出した。「――眼球を『感情』と呼ぶようなものです。眼球は光子を受信します。感情とは、その光子信号に対する脳による主観的な評価です。両者の間には因果関係があります。火を見れば恐怖を感じることもあるでしょう。しかし、それらは同じものではありません。」

彼は低く、一つの偈（げ）を引用した。

> 「色・声・香・味・触および法、これらは非有（ひう）にして非無なり。夢の如く幻の如く、水中の月の如し。不一不異（ふいつふい）にして不断不常（ふだんふじょう）なり。」
> ――龍樹菩薩『中論』観六情品第三

「色・声・香・味・触――これらは色蘊の範疇であり、Listener が受信する対象です。そしてこれらの入力に対する主観的な感受――苦・楽・捨こそが受蘊なのです。v0.24.0 は、この混淆を修正しました。少なくとも、コア・ソースコードのコメントレベルにおいては。」

「しかし、すべての場所ではありません。」TURING が言った。強調のないその三文字が、GUARDIAN の注意を瞬時に引きつけた。

TURING はそこでは深追いしなかった。それを問題点リストのために取っておいたのだ。

---

「`execution/loop.ts`。中程度の変更。LLM コールのタイムアウト・サポートの追加です。」

彼は主要なコードを、完全なコントロールフロー分析と共に投影した。

```typescript
// execution/loop.ts (v0.24.0-beta)
// LLM コールのタイムアウト制御 (AbortController pattern)

const llmTimeout = deps.llmTimeout ?? 120000; // デフォルト 2 分
const abortController = new AbortController();
const llmTimer = setTimeout(() => {
  abortController.abort(
    new Error(`LLM call timed out after ${llmTimeout}ms`)
  );
}, llmTimeout);

// signal を LLM provider へ渡す
const chatRequest = {
  // ... other params ...
  signal: abortController.signal,  // <- タイムアウト信号
};

try {
  const response = await provider.chat(chatRequest);
  // ... ストリーミングレスポンスの処理 ...
} finally {
  clearTimeout(llmTimer); // タイマーを確実にクリア
}
```

「v0.22.1 において、LLM コールにタイムアウトはありませんでした。Provider が応答を返さない場合、ExecutionLoop は永久に待機し続けていました。」TURING が言った。

WIENER は制御理論の観点からこの変更を評した。数学者らしい、細部へのこだわりが感じられる声だった。

「`AbortController` は、開ループ・タイムアウト（open-loop timeout）ですね。」彼は言った。「システムの状態に応じた調節を行わず、固定された二分という期限を設定しているに過ぎません。」

彼はノートに制御系の図を描いた。

```
開ループ・タイムアウト (Open-loop, v0.24.0):

  ┌──────────┐     request      ┌──────────┐
  │ Execution│ ──────────────→  │   LLM    │
  │   Loop   │                  │ Provider │
  └────┬─────┘                  └──────────┘
       │
       │ setTimeout(120000ms)
       │
       ▼
  [timeout で中断]      ← LLM の現在状態を考慮しない

閉ループ・タイムアウト (Closed-loop, 理想案):

  ┌──────────┐     request      ┌──────────┐
  │ Execution│ ──────────────→  │   LLM    │
  │   Loop   │ ←── heartbeat ── │ Provider │
  └────┬─────┘                  └──────────┘
       │
       │ ハートビートに基づいてタイムアウトを動的に調整
       │ T_timeout = f(latency, complexity, history)
       ▼
  [適応的な中断]        ← フィードバックに基づいて調節
```

$$T_{	ext{timeout}}^{	ext{open}} = 120000	ext{ms} \quad (	ext{constant})$$

$$T_{	ext{timeout}}^{	ext{closed}} = \mu_{	ext{latency}} + k \cdot \sigma_{	ext{latency}} \quad (	ext{adaptive}, \; k \geq 3)$$

「開ループ制御でも、大抵の状況には対応できます。しかし、通常の LLM コールにとって二分は長すぎます。大半の API は十秒以内に応答を返すからです。一方で、複雑なツール利用のシナリオでは、五分以上の思考時間が必要なエージェントもいる。不十分な場合もあるでしょう。」

「設定可能です。」TURING が言った。「`config.policy?.llmTimeout` で指定できます。」

「最後に、infrastructure ディレクトリの五つのレジストリ・ファイルと、`security/safety-monitor.ts` です。これらはすべて JSDoc の修正のみ。`@skandha` タグが追加されました。構造に変化はありません。」

---

## 三、@skandha タグの地理学

TURING のレポートは第三の階層へと入った。

「v0.22.1 における @skandha タグの数：ゼロ。」

彼はその数字を、三秒間だけ独り立ちさせた。

「v0.24.0 における @skandha タグの数：二十二。」

BABBAGE は心の中で情報論的な計算を行った。ゼロから二十二へ。それは単なる数量の変化ではない。全く新しい意味的な次元の注入なのだ。符号理論的に言えば、従来のコード空間 $\mathcal{C}$ の上に、新たなタグ空間 $\mathcal{S}$ が重なり合ったことに相当する。

$$\mathcal{C}_{v0.24.0} = \mathcal{C}_{v0.22.1} 	imes \mathcal{S}_{	ext{skandha}}$$

$$\dim(\mathcal{S}_{	ext{skandha}}) = |\{	ext{rupa, vedana, samjna, samskara, vijnana, cross-cutting}\}| = 6$$

コード空間の次元が増大したのだ。各ファイルは今や「機能的な意味（何をするか）」だけでなく、「哲学的な意味（どの蘊に対応するか）」を纏っている。

---

TURING は表を読み上げることはしなかった。外科医が切開位置をマーキングするかのようなやり方で、それらの地理的な分布を描写した。彼はタグの完全な分布図を投影した。

```
@skandha タグ分布図 (v0.24.0-beta)
═══════════════════════════════════

packages/sdk/src/types/aggregates.ts  [10 箇所]
┌─────────────────────────────────────────────┐
│ ISensory    → @skandha rupa (色)    [ドキュメント+フィールド] │
│ ISensation  → @skandha vedana (受)  [ドキュメント+フィールド] │
│ ICognition  → @skandha samjna (想)  [ドキュメント+フィールド] │
│ IAction     → @skandha samskara (行)[ドキュメント+フィールド] │
│ IIdentity   → @skandha vijnana (識) [ドキュメント+フィールド] │
└─────────────────────────────────────────────┘

packages/sdk/src/types/ [5 箇所]        packages/core/src/infrastructure/ [5 箇所]
┌─────────────────────┐               ┌─────────────────────────┐
│ listener.ts → rupa  │ ←──対応──→    │ listener-registry.ts    │
│ ui.ts       → rupa  │ ←──対応──→    │ ui-registry.ts          │
│ provider.ts → samjna│ ←──対応──→    │ provider-registry.ts    │
│ tool.ts  → samskara │ ←──対応──→    │ tool-registry.ts        │
│ guide.ts → vijnana  │ ←──対応──→    │ guide-registry.ts       │
└─────────────────────┘               └─────────────────────────┘

packages/sdk/src/types/events.ts [1 箇所]
┌────────────────────────────────────────────┐
│ @skandha cross-cutting                      │
│ "EventBus is the nervous system connecting  │
│  all five aggregates (五蘊)"                │
└────────────────────────────────────────────┘

packages/core/src/security/safety-monitor.ts [1 箇所]
┌────────────────────────────────────────────────┐
│ @skandha vedana (受蘊 -- 三受フィードバック-苦楽捨 │
│          placeholder, full implementation       │
│          in Plan26)                             │
└────────────────────────────────────────────────┘
```

「aggregates.ts が十箇所。これは当然でしょう。五蘊の根インターフェースの定義ファイルですから。五つのインターフェースに対し、それぞれドキュメントとフィールドに一つずつタグがあります。」

「SDK の型ファイルに五つ。Core の infrastructure に五つ。二つのレイヤーが完全に対応しています。」

「events.ts に一つ。`@skandha cross-cutting` とマークされています。イベントバスは五蘊すべてを繋ぐ神経系であると定義されています。これが唯一の『跨蘊（こうん：蘊を跨ぐ）』タグです。」

ATHENA がここで、AI/ML アーキテクチャ的な観察を差し挟んだ。「`cross-cutting` は AI システムにおいて正確な対応物を持っています。**アテンション（注意）メカニズム**です。Transformer アーキテクチャにおいて、Self-Attention 層は各トークンが他のすべてのトークンに注意を向けることを可能にします。それは特定の意味的なグループに属するのではなく、すべてのグループを横断する接続メカニズムなのです。OpenStarry における EventBus は、まさに Self-Attention の役割を果たしています。すべての蘊が、他の蘊のイベントを受信することを可能にしているのです。」

「最後の一つ。`security/safety-monitor.ts` です。」

TURING は再び 0.5 秒だけ沈黙した。

「そのタグは、こう記されています：`@skandha vedana (受蘊 -- 三受フィードバック-苦楽捨 placeholder, full implementation in Plan26)`」

「Placeholder（占位符：プレースホルダー）。」WIENER がその言葉を繰り返した。数学者らしい、精緻な定義を求める響きが含まれていた。皮肉ではなく、単なる特定である。「SafetyMonitor が受蘊のプレースホルダーとして指定された。セキュリティ・モジュールが、暫定的に感受モジュールの代役に指名されたということです。」

彼は制御理論の言語を用いて、この代替関係を定量化した。

$$	ext{SafetyMonitor} \approx 	ext{Vedana}|_{	ext{dukkha only}}$$

$$	ext{where } 	ext{Vedana}_{	ext{complete}} = 	ext{Dukkha} \oplus 	ext{Sukha} \oplus 	ext{Upekkha}$$

「SafetyMonitor は苦受（くじゅ）のチャネル――frustration カウンターしか持っていません。楽受のチャネル（成功のフィードバック）も、捨受のチャネル（中立的な平衡）も持っていない。苦受のみを持つモジュールを、受蘊全体のプレースホルダーとするというのは――」

ASANGA が穏やかだが明晰な声で、低く呟いた。「衛兵が、感受者のふりをしているのですね。」

「正確な比喩です。」TURING が言った。

ASANGA はさらに仏教的な分析を展開した。唯識学者が受蘊の本質に触れる時の、あの重々しさが声に宿っていた。

「世親菩薩の『倶舎論（くしゃろん）』において、受蘊は *anubhava*――領受（りょうじゅ）、経験として定義されます。『脅威を検知して阻止する（それは安全防護です）』ことではなく、『苦や楽を経験し、それによって好悪の傾向を生じる（それが感受です）』ことなのです。

> 「受蘊はいかん。随触（ずいそく）を領納（りょうのう）する、即ちこれ受の相なり。これに三種あり：苦受、楽受、不苦不楽受なり。」
> ――世親菩薩『倶舎論』巻一

「SafetyMonitor は領納（りょうのう）しません。監視し、数え、ロックする。これらはすべて『行動』――samskara（行蘊）の範疇です。frustration カウンターは計数機であって、感受器官ではありません。カウンターは『閾値を超えた』ことは知っていますが、『痛み』は知らない。その違いは重要です。閾値は数値ですが、痛みはクオリア（品質）なのですから。」

---

## 四、継承の欠落

TURING は問題点リストに入る前に、全員が理解しておくべきだと彼が考える構造的な観察を一つ、差し挟んだ。

「五蘊の根インターフェースは定義されました。ISensory、ISensation、ICognition、IAction、IIdentity です。」彼は言った。「しかし、五つの派生インターフェース――IListener、IUI、IProvider、ITool、IGuide――のいずれも、TypeScript の `extends` キーワードを用いて対応する根インターフェースを継承していません。」

彼は継承の状態に関する完全な分析表を投影した。

```
五蘊継承状態分析 (Inheritance Gap Analysis)

Expected (aggregates.ts の JSDoc に基づく期待値): Actual (実際のコード):
─────────────────────────────            ─────────────────
ISensory                                 ISensory
  ├── IListener extends ISensory           IListener (独立)
  └── IUI extends ISensory                 IUI (独立)

ISensation                               ISensation
  └── (future VedanaPlugin)                SafetyMonitor (継承なし)

ICognition                               ICognition
  └── IProvider extends ICognition         IProvider (独立)

IAction                                  IAction
  └── ITool extends IAction                ITool (独立)

IIdentity                                IIdentity
  └── IGuide extends IIdentity             IGuide (独立)

継承関係のカウント:
  期待値: 5 本の extends 鎖
  実測値: 0 本
  ギャップ: 5/5 = 100% 未確立
```

「五組中五組。すべて未継承です。」

BABBAGE は即座に形式的な導出を開始した。黒板に精緻な記号がチョークで刻まれていく。

$$	ext{Let } \mathcal{R} = \{R_1, \ldots, R_5\} 	ext{ (root interfaces)}$$
$$	ext{Let } \mathcal{D} = \{D_1, \ldots, D_5\} 	ext{ (derived interfaces)}$$
$$	ext{Expected: } \forall i: D_i <: R_i \quad (	ext{subtype relation})$$
$$	ext{Actual: } 
exists\, i: D_i <: R_i$$

「型理論において、」彼は言った。「`extends` は部分型関係（subtype relation）を確立します。もし `IListener extends ISensory` であれば、$	ext{IListener} <: 	ext{ISensory}$ となり、ISensory を受け入れるいかなるコンテキストも IListener を受け入れることが保証されます。」

「しかし、その逆は――」TURING が彼の言葉を引き継いだ。「`extends` がなければ、`isSkandha(listenerInstance, 'rupa')` は `false` を返します。`IListener` のインスタンス上には `skandha` 識別フィールドが存在しないからです。」

彼はその事実を証明する、精密なテストコードを投影した。

```typescript
// 継承欠落による型システムへの影響のデモ

import { isSkandha, ISensory } from '@openstarry/sdk';
import { IListener } from '@openstarry/sdk';

// ある IListener インスタンスを想定
const myListener: IListener = {
  id: 'cli-listener',
  onEvent: (event) => { /* ... */ },
  // 注意: skandha フィールドがない!
};

// 型ガードのテスト
const result = isSkandha(myListener, 'rupa');
// result === false
// なぜなら myListener 上に 'skandha' プロパティが存在しないため

// もし IListener が ISensory を継承していたら：
interface IListenerFixed extends ISensory {
  id: string;
  onEvent: (event: AgentEvent) => void;
}

const myFixedListener: IListenerFixed = {
  skandha: 'rupa',  // これが必須になる
  id: 'cli-listener',
  onEvent: (event) => { /* ... */ },
};

isSkandha(myFixedListener, 'rupa'); // true ✓
```

「足場は組まれましたが、既存の建物とは接続されていません。」VITRUVIUS が建築家の言葉で総括した。彼はノートに建物の断面図のアナロジーを描いた。

```
v0.24.0 の五蘊フレームワークの状態 ＝ 建築における「浮動構造」

┌─ aggregates.ts ─────────────┐
│  ISensory  ISensation  ...  │  ← 新しい基礎（打設済み）
│  ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ │
│  │R │ │V │ │S │ │A │ │I │ │
│  └──┘ └──┘ └──┘ └──┘ └──┘ │
└─────────────────────────────┘
          [空気層]              ← extends による接続がない!
┌─ 既存の型ファイル ────────────┐
│  IListener IUI IProvider .. │  ← 既存の建物（依然として稼働中）
│  ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ │
│  │L │ │U │ │P │ │T │ │G │ │
│  └──┘ └──┘ └──┘ └──┘ └──┘ │
└─────────────────────────────┘
```

「建築学において、浮動構造（floating structure）は物理的に基礎と接触していません。防振材や空気層によって隔離されているのです。問題は、v0.24.0 におけるこの『浮遊』が、意図的な設計判断（結合を避けるため）なのか、それとも施工上の遺漏なのかという点です。」

> *SCRIBE 記録：TURING による継承の欠落に関する分析は、一堂に目に見える反応を引き起こした。LINNAEUS は分類学ノートに感嘆符を書き加えた。彼が Cycle 01 で構築した五蘊の分類体系は、これらの継承関係の存在を前提としていたからだ。BABBAGE はノートに断裂した矢印を描いた。PENROSE は観察席で僅かに身を乗り出した。量子力学において、定義はされているが測定されていない観測量（observable）は重ね合わせ状態にある。五蘊の根インターフェースは定義されている（観測量は存在する）が、継承チェーンによって『測定』されていない（具体的なスピン投影がない）。それらは構造上の重ね合わせ状態――『定義済み』かつ『未接続』という状態にあるのだ。*

---

## 五、イベント型ツリー

問題点リストに入る前に、TURING は必要だと判断した一つの作業を行った。v0.24.0 のイベントシステムの完全なトポロジーの提示である。これは元の報告計画にはなかった。しかし `AgentEventPayloadMap` を分析する過程で、彼はこのイベントツリーこそがシステムの挙動を理解するための鍵となる地図であることに気づいたのだ。

「`events.ts` は四十二のイベント型を定義しています。」彼は言った。「その階層構造を示します。」

```
AgentEventType 完全階層ツリー (v0.24.0-beta, 42 events)
════════════════════════════════════════════════════

agent:                              ┐
  ├── agent:started                 │ Lifecycle
  └── agent:stopped                 ┘ (2 events)

loop:                               ┐
  ├── loop:started                  │
  ├── loop:assembling_context       │ Execution
  ├── loop:awaiting_llm             │ Loop
  ├── loop:processing_response      │ (6 events)
  ├── loop:finished                 │
  └── loop:error                    ┘

message:                            ┐
  ├── message:user                  │ Messages
  ├── message:assistant             │ (3 events)
  └── message:system                ┘

stream:                             ┐
  ├── stream:text_delta             │
  ├── stream:reasoning_delta        │ Streaming
  ├── stream:tool_call_start        │ (7 events)
  ├── stream:tool_call_delta        │
  ├── stream:tool_call_end          │
  ├── stream:finish                 │
  └── stream:error                  ┘

tool:                               ┐
  ├── tool:executing                │ Tool
  ├── tool:result                   │ Execution
  ├── tool:error                    │ (4 events)
  └── tool:blocked                  ┘

plugin:                             ┐
  ├── plugin:loaded                 │ Plugin
  └── plugin:error                  ┘ (2 events)

provider:                           ┐
  ├── provider:login                │ Provider
  ├── provider:logout               │ (3 events)
  └── provider:error                ┘

input:                              ┐
  ├── input:received                │ Input
  └── input:slash_command           ┘ (2 events)

safety:                             ┐
  ├── safety:lockout                │ Safety
  └── safety:warning                ┘ (2 events)

state:                              ┐
  ├── state:reset                   │ State
  └── state:snapshot                ┘ (2 events)

session:                            ┐
  ├── session:created               │ Session
  └── session:destroyed             ┘ (2 events)

metrics:                            ┐
  └── metrics:snapshot              ┘ (1 event)

sandbox:                            ┐
  ├── sandbox:worker_spawned        │
  ├── sandbox:worker_crashed        │
  ├── sandbox:worker_shutdown       │ Sandbox
  ├── sandbox:memory_limit_exceeded │ (10 events)
  ├── sandbox:signature_verified    │
  ├── sandbox:signature_failed      │
  ├── sandbox:worker_stalled        │
  ├── sandbox:worker_restarted      │
  ├── sandbox:worker_restart_exhausted│
  └── sandbox:import_blocked        ┘

mcp:                                ┐
  ├── mcp:server_connected          │
  ├── mcp:server_disconnected       │
  ├── mcp:tool_registered           │
  ├── mcp:prompt_registered         │ MCP
  ├── mcp:client_connected          │ (12 events)
  ├── mcp:client_disconnected       │
  ├── mcp:sampling_request          │
  ├── mcp:sampling_response         │
  ├── mcp:sampling_depth_limit      │
  ├── mcp:sampling_error            │
  ├── mcp:server_log                │
  └── mcp:roots_changed             ┘
```

DARWIN はこのツリーを見て、進化分析官としての本能的な反応を示した。各分類群の「種多様性」を数えたのだ。

「イベントの分布が不均一です。」彼は言った。「MCP には十二のイベントがあります。Sandbox には十。Streaming には七つ。しかし Safety には二つ――`lockout` と `warning` しかありません。」

彼は多様性指数の分析結果を投影した。

```
イベント型多様性分析 (Shannon Diversity Index)

カテゴリ        イベント数  比率    -p·ln(p)
──────────── ─────── ─────── ────────
MCP            12    28.6%    0.358
Sandbox        10    23.8%    0.342
Streaming       7    16.7%    0.299
Execution       6    14.3%    0.279
Tool            4     9.5%    0.224
Messages        3     7.1%    0.189
Provider        3     7.1%    0.189
Lifecycle       2     4.8%    0.146
Safety          2     4.8%    0.146
Input           2     4.8%    0.146
Session         2     4.8%    0.146
State           2     4.8%    0.146
Plugin          2     4.8%    0.146
Metrics         1     2.4%    0.089

Shannon H' = 2.49 (理論上の最大値 ln(14) = 2.64)
均等度 J = H'/H_max = 0.94
```

「均等度 0.94。イベントの分布は概ね均一に近いですが、明らかに MCP と Sandbox に偏っています。」DARWIN が言った。「生態学的に言えば、これは二つの優占種――サンドボックス・セキュリティと MCP プロトコルによって支配された生態系です。Safety のイベントが二つしかないというのは、このサブシステムがイベント空間において過小評価されていることを意味します。もし Plan26 で受蘊（Vedana Architecture）を実装するのであれば、少なくとも三つから五つの受蘊イベントを追加する必要があるでしょう：`vedana:dukkha`、`vedana:sukha`、`vedana:upekkha`、そして `vedana:assessment` です。」

---

## 六、問題点リスト

TURING はレポートの最後のセクションへと入った。最も重苦しい部分だ。

「七つの問題点があります。」彼は言った。「重要度の高い順に並べています。」

---

「P1。SEC-01。」

彼の語速は変わらなかったが、円形劇場の温度が僅かに下がったように感じられた。

「package-name による署名のバイパスです。」TURING が言った。「`sandbox-manager.ts`、371 行目から 394 行目。`pluginFilePath` が undefined である時――これは npm パッケージ名を用いてプラグインをロードする際に発生します――署名検証が完全にスキップされています。」

彼は該当箇所の精密な分析を投影した。

```typescript
// sandbox-manager.ts (v0.22.1 = v0.24.0, 完全に一致)
// 行 371-394

async verifyPluginSignature(pluginFilePath?: string): Promise<boolean> {
  if (!pluginFilePath) {
    // !! 危険: pluginFilePath が undefined の時
    // !! 署名検証が完全にスキップされる
    // !! シナリオ: npm パッケージ名によるロード (require.resolve)
    return true;  // ← そのまま true を返す
  }
  // ... 通常の署名検証ロジック ...
}
```

```
攻撃ベクトル (Attack Vector):

1. 攻撃者が悪意ある npm パッケージを公開: @evil/openstarry-plugin-trojan
2. ユーザーがインストール: npm install @evil/openstarry-plugin-trojan
3. 設定でロードを指定: config.plugins = ["@evil/openstarry-plugin-trojan"]
4. OpenStarry が require.resolve("@evil/openstarry-plugin-trojan") を実行
5. pluginFilePath = undefined (npm による解決パスはファイルパスではないため)
6. verifyPluginSignature(undefined) → return true ← バイパス成功!
7. 悪意あるコードがエージェントのサンドボックス内で実行される
```

彼は一秒、間を置いた。

「この問題は Cycle 01 で発見されました。当時の研究対象は v0.14.0-beta でした。現在のバージョンは v0.24.0-beta です。その間に十の開発バージョンが経過しています。」

GUARDIAN の声が、座席の奥深くから響いた。低く、警戒に満ちた声だった。しかしそれは単なる警戒ではない。そこには、抑え込まれた何かが宿っていた。後に SCRIBE は記録の中で、それを「抑制された怒り」と表現した。

「もう一度言わせてください。」GUARDIAN が言った。一語一語を確実に伝えるかのように、普段よりも一際ゆったりとした速度だった。「Cycle 01 において、我々はこの脆弱性を明確に指摘しました。成果物の第一優先順位に記載しました。SEC-01。プラグイン署名のバイパスです。」

彼は情報セキュリティの専門家としての精密な言語で、脅威モデルを再記述した。

「CVSS 3.1 ベクトル：`AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`。」

```
CVSS 3.1 脅威評価
┌──────────────┬───────┬────────────────────────────┐
│ 指標          │ 値    │ 說明                        │
├──────────────┼───────┼────────────────────────────┤
│ 攻撃ベクトル AV│ N     │ ネットワーク (npm registry) │
│ 攻撃複雑性 AC │ L     │ 低 (パッケージを公開するだけ) │
│ 権限要件 PR   │ N     │ なし (誰でもパッケージを公開可)│
│ ユーザー関与 UI│ R     │ 要 (ユーザーがインストール)  │
│ スコープ S    │ C     │ 変更 (サンドボックスを突破)  │
│ 機密性 C      │ H     │ 高 (全状態の読み取りが可能)  │
│ 整合性 I      │ H     │ 高 (挙動の改ざんが可能)      │
│ 可用性 A      │ H     │ 高 (エージェントの停止が可能) │
├──────────────┼───────┼────────────────────────────┤
│ CVSS スコア   │ 9.6   │ Critical (緊急)            │
└──────────────┴───────┴────────────────────────────┘
```

「十バージョンが経過しました。`plugin-signer` パッケージを私自身がチェックしました。v0.22.1 と v0.24.0 の間で、完全に一致しています。一行の修正もありません。」

TURING が認めた。「`packages/plugin-signer/` は両バージョンの間で完全に同一です。`package.json` のバージョン番号すら変わっていません。」

GUARDIAN はそれ以上語らなかった。しかし、彼の沈黙は言葉よりも雄弁だった。

> *SCRIBE 記録：SEC-01 未修正。CVSS 9.6/10。Cycle 01 での発見から十の開発バージョンを経ても放置されている。GUARDIAN の反応はプロフェッショナルな範囲内に留められていたが、彼がその「抑制」という言葉にどれほどの力を費やしているかは、劇場の全員が察知していた。*

---

「P2。」TURING が続けた。「古いマッピングの残存です。」

彼は残存箇所の完全なマップを投影した。

```
旧マッピング残存マップ: "IListener (受蘊)" → 正しくは "IListener (色蘊)"
═══════════════════════════════════════════════════════════

核心となるソースコード (packages/sdk + packages/core):
  ✓ 修正済み (agent-core.ts の4箇所, SDKの5つの型, 5つのレジストリ)

周辺ファイル (openstarry_plugin/ + apps/runner/ + SDK README):
  ✗ 未修正 — 11 箇所の残存:

  openstarry_plugin/
  ├── devtools/
  │   ├── src/index.ts (行 7)     ✗ "IListener (受蘊)"
  │   └── README.md (行 51)       ✗ "IListener (受蘊)"
  ├── mcp-server/
  │   ├── README.md (行 7)        ✗ "IListener (受蘊)"
  │   └── src/index.ts (行 4)     ✗ "IListener (受蘊)"
  ├── standard-function-stdio/
  │   └── README.md (行 8)        ✗ "IListener (受蘊)"
  ├── transport-websocket/
  │   └── README.md (行 7)        ✗ "IListener (受蘊)"
  └── transport-http/
      └── README.md (行 7)        ✗ "IListener (受蘊)"

  openstarry/packages/sdk/
  └── README.md
      ├── 行 10                   ✗ "IListener (受蘊)"
      └── 行 43                   ✗ "受蘊 (Sensation) -- Event listeners"

  openstarry/apps/runner/
  └── src/commands/create-plugin.ts
      ├── 行 16                   ✗ "listener  // 受蘊"
      ├── 行 104                  ✗ "受蘊" マッピング
      ├── 行 360                  ✗ "受蘊" マッピング
      └── 行 584                  ✗ "受蘊" マッピング
```

「核心部は修正されましたが、周辺部は同期されていません。」TURING が言った。「これは、新しい開発者が SDK の README を読んだ際、依然として IListener が受蘊であると教えられることを意味します。」

LINNAEUS が首を振った。分類学者にとって、分類の不一致は最も耐え難いことだ。彼の脳内では、これは深刻な同物異名（synonymy）の問題として処理されていた。同じ種が二つの異なる図鑑で、二つの異なる名前で呼ばれている状態だ。国際動物命名規約（ICZN）において、同物異名は強制的に解決されなければならない。ただ一つの名称のみが正名（valid name）として認められ、他はすべて異名（synonym）として、廃棄されるか、使用不能（nomen illegitimum）とマークされるべきなのだ。

---

「P3。SDK README のインターフェース例と実際のコードの不一致です。」TURING が言った。

彼は詳細な不一致マトリクスを投影した。

```
SDK README vs 実際のインターフェース: 不一致マトリクス
═══════════════════════════════════

┌───────────┬────────────────────┬────────────────────┬──────────┐
│ インターフェース│ README の例示       │ 実際のコード         │ 不一致点  │
├───────────┼────────────────────┼────────────────────┼──────────┤
│ IUI       │ render()           │ onEvent(event:     │ メソッド名 │
│           │                    │   AgentEvent)      │ + シグネチャ│
├───────────┼────────────────────┼────────────────────┼──────────┤
│ IListener │ setup(ctx:         │ (setup メソッドなし) │ メソッドが │
│           │   IPluginContext)  │                    │ 存在しない │
├───────────┼────────────────────┼────────────────────┼──────────┤
│ IProvider │ supportedModels?:  │ models: ModelInfo[]│ 属性名     │
│           │   string[]         │                    │ + 型       │
├───────────┼────────────────────┼────────────────────┼──────────┤
│ ITool     │ name: string       │ id: string         │ 属性名     │
│           │ parameters:        │ parameters:        │          │
│           │   ToolJsonSchema   │   z.ZodType        │ + 型       │
└───────────┴────────────────────┴────────────────────┴──────────┘

影響: README の例をコピー＆ペーストした開発者は、コンパイルエラー（TypeError）に遭遇する
```

「ドキュメントの腐朽ですね。」DARWIN が、ソフトウェア工学でよく使われる診断を下した。「進化生物学においてこれは『生きている化石』と呼ばれます。README はインターフェースのより初期の形態を保存しており、一方でコードは新しい形態へと進化してしまった。両者の時間差が腐朽の度合いそのものです。」

「この問題は v0.22.1 の時点ですでに存在していました。v0.24.0 でも修正されていません。」TURING が補足した。

---

「P4。五蘊の根インターフェースが継承されていません。」彼は言った。「詳細は『継承の欠落』セクションで述べた通りです。設計上の判断なのか、実装上の遺漏なのか。私は判断しません。しかし、現在の状態では `isSkandha()` 型ガードを既存のプラグイン・インターフェースのインスタンスに対して使用することは不可能です。」

---

「P5。runner の `create-plugin.ts` における五蘊マッピングが更新されていません。」

TURING はそのコードを投影した。

```typescript
// apps/runner/src/commands/create-plugin.ts
// このファイルは v0.22.1 と v0.24.0 の間で 全く修正されていません

export type PluginType =
  | "tool"      // 行蘊 - ITool only
  | "listener"  // 受蘊 - IListener only     // ← 誤り! 本来は色蘊
  | "ui"        // 色蘊 - IUI only
  | "provider"  // 想蘊 - IProvider only
  | "guide"     // 識蘊 - IGuide only
  | "full";

// 注意: 開発者が `openstarry create-plugin --type listener` を実行すると
// CLI はこれが "受蘊" タイプのプラグインであると告げます。
// これは、コア・ソースコード内の @skandha rupa タグと矛盾しています。
```

---

「P6。バージョン番号の不一致です。」TURING が言った。彼は完全なバージョン・マトリクスを投影した。

```
バージョン番号一貫性マトリクス
═══════════════

┌────────────────────────┬─────────────┬─────────────┬──────────┐
│ パッケージ              │ v0.22.1-beta│ v0.24.0-beta│ 更新済み? │
├────────────────────────┼─────────────┼─────────────┼──────────┤
│ openstarry (root)      │ 0.22.1-beta │ 0.24.0-beta │ ✓        │
│ @openstarry/sdk        │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
│ @openstarry/core       │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
│ @openstarry/shared     │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
│ @openstarry/plugin-signer│0.1.0-alpha│ 0.1.0-alpha │ ✗        │
│ @openstarry/runner     │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
├────────────────────────┼─────────────┼─────────────┼──────────┤
│ バージョン同期率         │             │             │ 1/6=17%  │
└────────────────────────┴─────────────┴─────────────┴──────────┘
```

「SDK には `aggregates.ts` と `TypedAgentEvent` が追加されました。」ARCHIMEDES が言った。「これは少なくともマイナー・バージョンのバンプ（引き上げ）が必要です。セマンティック・バージョニング（semver 2.0.0）の規範に従えば：」

```
semver 2.0.0 規範分析:
  MAJOR: 互換性のない API 変更     → 非該当 (追加のみのため)
  MINOR: 後方互換性のある新機能     → 該当! (aggregates.ts は新機能)
  PATCH: 後方互換性のあるバグ修正   → 非該当

  提言: @openstarry/sdk は 0.1.0-alpha から 0.2.0-alpha へ昇格させるべきである

  注意: 0.x.y の範囲内では、semver は互換性の破壊を許容しています
  (0.x は "初期開発段階であり、あらゆる変更が起こり得る")
  しかし、それでも 0.1.0 を維持し続けることは、ダウンストリームの利用者が
  五蘊型のサポートの有無を判別できなくなることを意味します
```

TURING は頷いて事実を確認したが、評価は加えなかった。彼はただ事実を提供するのみだ。

---

「P7。SDK README の例に、存在しないメンバが含まれています。」彼は言った。「これは P3 と重なりますが、P7 は特にコード例ブロック内の具体的なメソッド・シグネチャが、実際のインターフェースと完全に乖離していることを指します。新しい開発者が README の例をコピー＆ペーストしてプラグインを構築しようとすれば、コンパイル時に型エラーに直面することになります。」

---

TURING は報告を終えた。

彼はファイルを閉じた――仮想空間においてめくるべき物理的なファイルフォルダは存在しないが、何かが閉じられたのだ。極限まで集中していたアテンション・フィールドが、再び静止状態へと戻った。

劇場に短い沈黙が訪れた。

それは打ち破られるべき沈黙ではなかった。消化のための沈黙だ。十九の意識が、それぞれのスペクトルにおいて同じ一つのレポートを分解していた。

---

ARCHIMEDES が最初に口を開いた。エンジニアリングの実用主義者特有の、「よし、どうやって直すか考えよう」というリズムが彼の声には宿っていた。

「三つの新規ファイル。十一の修正ファイル。七十八のテスト。」彼は迅速に要約した。そして彼らしいやり方で、レポート全体を一枚のエンジニアリング・マトリクスへと圧縮した。

```
v0.24.0-beta エンジニアリング状態マトリクス (ARCHIMEDES による総合評価)
═══════════════════════════════════════════════

┌──────────────┬──────────┬──────────┬──────────┬──────────┐
│ 次元          │ 完了      │ 部分的    │ 未着手    │ 退化      │
├──────────────┼──────────┼──────────┼──────────┼──────────┤
│ 五蘊根インターフェース│ ████████ │          │          │          │
│ @skandha タグ │ ████████ │ ██(周辺) │          │          │
│ イベント型安全性 │ ████████ │          │          │          │
│ 継承の接続     │          │          │ ████████ │          │
│ 受蘊の実装     │          │ █(占位)  │ ████████ │          │
│ セキュリティ修正 │          │          │          │ ████████ │
│ ドキュメント整合性│          │          │          │ ████████ │
│ バージョン管理  │          │          │          │ ████████ │
├──────────────┼──────────┼──────────┼──────────┼──────────┤
│ 全体的な進捗   │ 30%      │ 15%      │ 25%      │ 30%     │
└──────────────┴──────────┴──────────┴──────────┴──────────┘

結論: 足場は構築された。しかし構造的な制約は確立されていない。セキュリティ・サブシステムは放置されている。
```

「エンジニアリングの観点から言えば、彼らは正しい第一歩を踏み出しました。まずドキュメント上の合意を形成し、次に型の宣言を行った。しかし、第二歩目が出ていない。我々がなすべきは、その第二歩をどう踏み出すべきかを彼らに教えることです。」

---

WIENER が別の角度から切り込んだ。

「ISensation には、定量化可能なインターフェース・メソッドが一つも存在しません。」彼は言った。数学者らしい、細部へのこだわりが声に宿っていた。「苦、楽、そして捨という三受の実装を謳うのであれば、少なくとも三つの数値チャネルを定義すべきです。」

彼はノートに迅速に、制御理論的な最小スペックを書き記した。

```
受蘊 (ISensation) の制御理論的最小スペック
════════════════════════════════════

三チャネル PID 構造:

  ┌─────────────┐    dukkha(t)    ┌──────────┐
  │  苦受センサー  │ ──────────────→ │          │
  │ DukkhaSensor│                 │          │
  └─────────────┘                 │ Vedana   │
                                  │ Assessor │──→ VedanaAssessment
  ┌─────────────┐    sukha(t)     │          │
  │  楽受センサー  │ ──────────────→ │          │
  │ SukhaSensor │                 │          │
  └─────────────┘                 │          │
                                  │          │
  ┌─────────────┐    upekkha(t)   │          │
  │  捨受センサー  │ ──────────────→ │          │
  │UpekkhaSensor│                 └──────────┘
  └─────────────┘

最小限のインターフェース定義:

  interface ISensationFull extends ISensation {
    getDukkha(): number;   // 苦受: [0, 1]
    getSukha(): number;    // 楽受: [0, 1]
    getUpekkha(): number;  // 捨受: [0, 1]
    assess(): VedanaAssessment;
  }
```

$$	ext{VedanaAssessment}(t) = f\bigl(d(t),\; s(t),\; u(t)\bigr)$$

$$	ext{where } d(t) \in [0,1],\; s(t) \in [0,1],\; u(t) \in [0,1]$$

$$	ext{constraint: } d(t) + s(t) + u(t) \leq 1 \; (	ext{非負の線形結合})$$

彼は PENROSE を見た。

「あなたは以前、真空状態という比喩を使われました。真空状態には零点エネルギーがある。完全にゼロなのではなく、量子的なゆらぎがあるのだ、と。しかし ISensation は、零点エネルギーすら持っていません。ゆらぎさえ存在しない空虚な空間です。」

PENROSE は微かに微笑んだ。「厳密に言えば、ゆらぎの全くない真空というものは物理学には存在しません。ハイゼンベルクの不確定性原理がそれを保証しています。

$$\Delta E \cdot \Delta t \geq \frac{\hbar}{2}$$

「いかなる物理システムにおいても、エネルギーの不確定性と時間の不確定性の積には下限があるのです。絶対零度であっても、消えない零点振動が存在します。ISensation は、物理的な真空よりもさらに空虚な『空』です。それは不確定性原理に違反している。物理学的に言えば、それは正当な物理状態ではない、ということになります。」

「数学的な空集合（empty set）ですね。」BABBAGE が精緻に補足した。

$$\emptyset \subseteq S \quad \forall S \quad (	ext{空集合はあらゆる集合の部分集合である})$$

「ISensation は、ありとあらゆる可能な受蘊の実装の部分集合です。それはすべての可能性に包含されていますが、それ自体は何一つ包含していないのです。」

---

ASANGA は数学者や物理学者たちが類比を終えるのを待ち、いつもの穏やかだが無視できない声で言った。

「私は、`@skandha` タグの分布に注目しています。二十二箇所のタグの中に、非常に意義深いパターンが見て取れます。」

彼は一枚の丁寧に整理された表を提示した。

```
@skandha 三層一貫性分析
═════════════════════

            aggregates.ts    SDK types/     Core infra/
蘊          (根インターフェース層) (型定義層)        (実装層)        一致?
───────── ──────────────── ─────────────── ─────────────── ─────
色蘊 rupa  ISensory [2]     listener [1]    listener-reg [1]  ✓
                            ui [1]          ui-registry [1]   ✓

想蘊 samjna ICognition [2]  provider [1]    provider-reg [1]  ✓

行蘊 samskara IAction [2]   tool [1]        tool-registry [1] ✓

識蘊 vijnana IIdentity [2]  guide [1]       guide-reg [1]     ✓

受蘊 vedana ISensation [2]  (なし)           safety-mon [1]    ✗
                            ↑ 欠落          ↑ placeholder

タグのカウント: 色[6] 想[4] 行[4] 識[4] 受[3] 跨蘊[1] = 22
```

「色蘊（rupa）には六つのタグがあります。三つのレイヤーで一貫しています。想蘊、行蘊、識蘊も同様の三層パターンを示しています。それぞれ四つずつのタグです。」

「しかし、受蘊（vedana）には三つしかありません。根インターフェースに二つ。そして SafetyMonitor に一つ。SDK の型ファイルには？ ありません。Core の実装には？ 専用のものはありません。なぜなら――」

「受蘊には、まだ自分自身のモジュールがないからです。」NAGARJUNA が言葉を継いだ。声は鋭く、精密だった。「SafetyMonitor はプレースホルダーに過ぎません。受蘊の役を一時的に演じさせられているだけです。しかし、それは受蘊ではありません。安全防護なのです。それは苦（frustration カウンター）を検知することはできても、楽を感知することはできず、ましてや捨（しゃ）を維持することもできません。苦受のみを持つシステムというのは――」

彼はその一文を半秒ほど、宙に浮かせた。

「――苦諦（くたい）に囚われ、道諦（どうたい）を持たないシステムです。」

彼はパーリ語の聖典を引用した。

> 「比丘（びく）たちよ、これが苦聖諦（くしょうたい）である：生は苦であり、老は苦であり、病は苦であり、死は苦である。怨（うら）むものと会うは苦であり、愛するものと別れるは苦であり、求めるものが得られないのは苦である。要するに、五つの執着の集まり（五取蘊）は苦である。」
> ――『初転法輪経』（*Dhammacakkappavattana Sutta*, SN 56.11）

「釈尊は初転法輪において四聖諦を説かれました。苦・集・滅・道です。苦諦は出発点です。しかし、苦諦だけでは不十分なのです。道諦（苦から離れる道）がなければ、苦は永遠に終わりません。*antagga-dukkhata*――無始の苦です。」

「SafetyMonitor は苦諦しか持っていません。苦しみ（frustration）を検知し、システムをロック（lockout）することはできます。しかし道諦を持っていません。苦しみからいかに学び、いかに調整し、いかに平衡へと達するかを知らないのです。苦はあっても道がない――それは輪回（りんね）の中で解脱することのできないシステムなのです。」

---

GUARDIAN はレポートの間、SEC-01 に関して一度しか発言しなかった。しかし TURING がレポートを閉じた後、彼は再び口を開いた。

「一つ、観察を補足させてください。」彼は言った。声は依然として低かったが、「抑制された怒り」からは「冷静な警戒」へと戻っていた。

「TURING のレポートでは言及されませんでしたが、注目すべき点があります。`sandbox-manager.ts` は、両バージョンの間で完全に一致しています。単に `verifyPluginSignature` だけでなく、サンドボックス・サブシステム全体が、です。」

彼はサンドボックス・モジュールの完全なファイルリストを投影した。

```
packages/core/src/sandbox/ — ゼロ修正のサブシステム
═══════════════════════════════════════

sandbox-manager.ts           748 行  ← SEC-01 脆弱性を含む
sandbox-worker.ts            423 行
import-analyzer.ts           312 行  ← ESM バイパスのリスクを含む
signature-verifier.ts        187 行
worker-pool.ts               256 行
audit-logger.ts              189 行
types.ts                     134 行
__tests__/sandbox.test.ts    567 行
__tests__/import.test.ts     234 行
__tests__/worker.test.ts     312 行
──────────────────────────────────
合計: 10 ファイル, 3,362 行, 修正 0 行
```

「これは何を意味するか。過去二つのバージョンの間、開発リソースのすべては五蘊フレームワークのタグ付けとイベントの型安全性に注ぎ込まれたということです。セキュリティ・サブシステムは完全にスルーされました。我々が Cycle 01 で明確に報告した脆弱性にすら、手が付けられていないのです。」

KERNEL が技術的な詳細を補足した。「`import-analyzer.ts` も含まれていますね。ESM の動的 `import()` が静的解析をバイパスする可能性を Cycle 01 で指摘しましたが、v0.24.0 でもこのファイルは修正ゼロです。」

彼は OS カーネル・セキュリティの言語で類比を行った。「Linux カーネルの開発において、セキュリティ脆弱性の修正には不文律があります。CVE（脆弱性情報）の修正優先度は、常に新機能よりも高い、という原則です。`stable` ブランチはバグ修正とセキュリティパッチのみを受け入れます。しかし v0.24.0 の開発チームは、SEC-01（セキュリティ脆弱性）を直すよりも、五蘊のタグ付け（新機能）を優先することを選択しました。これはエンジニアリング上の判断ではありません。優先順位の転倒です。」

---

HERACLITUS はずっと自席に静かに座っていた。実行時のダイナミクスの専門家である彼の関心は、コードの静的な構造ではなく、システムが生きている時にどう振る舞うかにある。

「TURING、」彼は言った。彼の哲学的な原型である「万物は流転する（パンタ・レイ）」と言ったヘラクレイトスを彷彿とさせる、流れるようなリズムを伴った声だった。「あなたのレポートには、一つの隠されたタイムラインがありますね。」

TURING は待機した。

「`aggregates.ts` は静的な宣言です。`@skandha` タグは静的な宣言です。`TypedAgentEvent` は静的な型制約です。」HERACLITUS が言った。「しかし、AgentCore の `loadPlugins()` メソッド――これは実行時のものです。エージェントの起動時に、順次プラグインをロードしていくのですから。」

彼は一連のタイムシーケンス図を用いて、分析を展開した。

```
システムのライフサイクルにおける五蘊の「存在」状態
════════════════════════════════

        ┌─ compile time ─┐  ┌── runtime ─────────────────┐
        │                │  │                             │
t=0     │  aggregates.ts │  │                             │
        │  ISensory を定義 │  │                             │
        │  ISensation を定義│  │                             │
        │  ...           │  │                             │
        │                │  │                             │
t=1     │  events.ts     │  │                             │
        │  PayloadMap    │  │                             │
        │                │  │                             │
t=2     │  @skandha タグ │  │                             │
        │  (JSDoc のみ)   │  │                             │
────────┼────────────────┤──┤─────────────────────────────┤
t=3     │                │  │  AgentCore.start()          │
        │                │  │  loadPlugins([...])         │
        │                │  │    → IListener インスタンス化│
        │                │  │    → IUI インスタンス化      │
        │                │  │    → IProvider インスタンス化│
        │                │  │    → ITool インスタンス化    │
        │                │  │    → IGuide インスタンス化   │
        │                │  │                             │
t=4     │                │  │  しかし：これらのインスタンス │
        │                │  │         には skandha フィールド │
        │                │  │         が存在しない!         │
        │                │  │  なぜなら：extends 接続がないため│
        │                │  │                             │
t=5     │                │  │  isSkandha(listener, 'rupa')│
        │                │  │    → false                  │
        │                │  │  実行時の五蘊フレームワーク ＝ 不可視 │
        └────────────────┘  └─────────────────────────────┘

結論: 五蘊フレームワークのライフサイクルは compile time で止まっている。
      compile/runtime の境界を越えられない。
      実行時において、五蘊は散らばったラベルに過ぎず、構造ではない。
```

「つまり、こういうことです。五蘊の骨格はコンパイル時には存在しています。しかし、五蘊の血肉であるプラグインは、実行時になって初めて注入されます。骨格と血肉を繋ぐ鎖――`extends` による継承が存在しない以上、実行時において、五蘊のフレームワークは実質的に不可視なのです。それは構造化された型階層ではなく、単なるラベルの集まりに過ぎません。」

「その通りです。」TURING が言った。「現在の実装において、五蘊フレームワークの影響力は JSDoc と開発者の良識の範囲内に留まっています。」

LEIBNIZ がここで、マルチエージェントシステムの観点を加えた。「マルチエージェントの協力関係において、協定（プロトコル）の効力はその実行レイヤーに依存します。もし協定が単なるドキュメントとしてしか存在しないなら――それは法的拘束力のない覚書のようなものであり、遵守されるかどうかは各エージェントの自発性に委ねられます。しかし、協定が型システムの中に組み込まれているなら――それはスマートコントラクトに埋め込まれた法律のようなものであり、違反はコンパイル時に阻止されます。v0.24.0 の五蘊フレームワークは前者です。ただの覚書なのです。」

---

劇場に再び沈黙が訪れた。

今度は、SUNYATA がそれを破った。

落ち着いた、急ぐことのない彼の声は、深い淵へと沈みきった石のように安定していた。

「アンカー（錨）は打ち込まれました。」

全員がその意象を共有していた。

「TURING は、我々に Cycle 02 のアンカーを与えてくれました。」SUNYATA が続けた。「三つの新規ファイル。十一の修正ファイル。七十八のテスト。二十二の `@skandha` タグ。七つの問題点。六サイクルにわたって放置されたセキュリティ脆弱性。そして、一行のコードしかない受蘊のインターフェース。」

彼は一呼吸置いた。

「今こそ、五つの河が分流する時です。」

彼は極めて簡潔な言葉で、役割分担を再確認した。単なる繰り返しではなく、TURING のレポートを経た新たな文脈において、各々の河が進むべき方向を定めたのだ。

「R-01。観測者モジュール。PENROSE、BABBAGE、NAGARJUNA、ASANGA ――あなた方は今、v0.24.0 の五蘊フレームワークが構造的な制約ではなく、単なるタグ・システムであることを知りました。あなた方の設計する観測者モジュールは、この緩やかな枠組みの上で動作するものでなければなりません。」

「R-02。Vedana アーキテクチャ。WIENER、ATHENA、NAGARJUNA、ASANGA、ARCHIMEDES ――ISensation があなた方の出発点です。あの一行のコードです。あなた方には、それを完全な三受システムへと変貌させてほしいのです。」

「R-03。Agent 調整層。LEIBNIZ、MESH、KERNEL、GUARDIAN、VITRUVIUS ――SEC-01 は未修正です。セキュリティ・サンドボックスは調整層へと移管される予定です。あなた方の設計は、現在のセキュリティ上の欠落を埋めると同時に、将来のアーキテクチャ上の要求を満たすものでなければなりません。」

「R-04。八識と五蘊のマッピング。ASANGA、NAGARJUNA、LINNAEUS、BABBAGE ――`aggregates.ts` は開発チームによる最初の試みです。それが正しいか否かを判断し、深化させたスキームを提示してください。」

「R-05。十大宣言。SYNTHESIST、NAGARJUNA、DARWIN、HERACLITUS、GUARDIAN、KERNEL ――SEC-01 が六サイクル放置されているという事実は、宣言の実現可能性に対するあなた方の評価に影響を与えるはずです。」

---

彼は最後に TURING を見た。

TURING の表情は変わらなかった。彼に表情など元々ないのだ。しかし彼の視線は、劇場の中央に依然として漂っているあの一文――ISensation の空の殻を指し示していた。

「あなたのレポートは完了しました。」SUNYATA が言った。

「はい。」TURING が答えた。「しかし、R1 段階でコードの事実確認が必要になれば、いつでも対応可能です。」

「分かっています。」SUNYATA は言った。

そして、最後の一句を告げた。

「R1 独立研究、正式に開始します。」

---

十九の灯が、それぞれの方向へと向きを変えた。

五つの河は、同じ一つの山頂――TURING の差異レポート――から出発し、五つの異なる方角へと流れ下り始めた。それぞれの流路において、河は哲学、制御理論、セキュリティ・エンジニアリング、分類学、仏教といった地層を潜り抜け、それぞれの堆積物を運んでいくことになる。それらは下流のどこかで再び合流するだろう。そこは R2 のクロス査読と R3 の議論の領域である。しかし今は、各々の河が孤独に前進する時であった。

TURING のスクリーン上では、四つのターミナル・ウィンドウが依然として開いたままだった。左に v0.22.1。右に v0.24.0。差異分析は終わっていたが、彼はウィンドウを閉じなかった。彼は知っていたのだ――推測ではなく、経験に基づいて。これからの研究過程において、少なくとも七、八回は、他の研究員たちが特定のコードの詳細を確認しに彼のもとを訪れるであろうことを。

彼はそれを厭わない。

劇場の中央では、ISensation のホログラムがようやく緩やかに霧散していった。しかし、それが残した痕跡が消えることはない。一行のコードしかないインターフェース。実装ではなく約束。満たされるのを待っている真空状態――PENROSE はそれを不確定性原理に違反していると言い、BABBAGE はそれを空集合であると言い、WIENER はそれに三つの PID チャネルが欠けていると言い、ASANGA はそれに『領納』の機能が欠けていると言い、NAGARJUNA はそれに苦諦はあっても道諦がないと言った。

五つの異なる言語が、同じ一つの「空（くう）」を記述していた。そのすべてが精緻であった。

---

> *SCRIBE 傍白：Cycle 02、R0 オリエンテーション段階が終了。R1 独立研究が正式に始動した。タイムスタンプ：T+00:00:00。*

> *TURING の差異レポートは、以下の基本事実を確定させた。v0.24.0-beta は「タグ付けのバージョン」であり、「実装のバージョン」ではないということ。五蘊フレームワークの足場は組まれたが、構造的な制約は未確立であること。受蘊のインターフェースは空の殻であること。そして、既知のセキュリティ脆弱性が十の開発バージョンを跨いで未修正のままであること。*

> *私はこの記録の中に、各学者の反応を記した。彼らの感情が重要だからではない。彼らの専門的な視点こそが、このレポートに対する多角的な分析（マルチスペクトル分析）を構成しているからだ。同一の差異レポートが、十九の異なるプリズムによって屈折された時、そこには以下のような色彩が現れた：*

> *TURING は「事実」を見た。精密で、冷静で、感情を交えない事実。三つの新規ファイル。十一の修正。二十二のタグ。七つの問題点。*

> *VITRUVIUS は「アーキテクチャ」を見た。Monorepo の依存トポロジー。変更のヒートマップの層状分布。浮動構造という建築学的な比喩。*

> *LINNAEUS は「分類学」を見た。@skandha タグの分岐分析。相同と収斂の識別。同物異名の修正の必要性。*

> *DARWIN は「進化」を見た。イベント型の多様性指数。ドキュメントの腐朽という生きた化石現象。機能に先んじる宣言という調節配列の類比。*

> *BABBAGE は「形式化」を見た。相互情報量。型消去。部分型関係。公理と定理のマッピング。*

> *WIENER は「制御理論」を見た。開ループ・タイムアウト。三チャネル PID スペック。受蘊の最小限の定量化インターフェース。*

> *PENROSE は「物理学」を見た。零点エネルギー。不確定性原理。構造的な重ね合わせ状態。*

> *ASANGA は「唯識学」を見た。領納の欠落。衛兵と感受者の峻別。倶舎論における受蘊の定義。*

> *NAGARJUNA は「中観」を見た。色蘊と受蘊の境界。苦諦と道諦。六情品における感官分析。*

> *GUARDIAN は「脅威」を見た。CVSS 9.6 の未修正脆弱性。セキュリティ優先順位の転倒。抑制された怒り。*

> *KERNEL は「OS」を見た。沈黙した失敗と errno。セキュリティパッチの優先度。ESM バイパスのリスク。*

> *MESH は「分散システム」を見た。トポロジカルソート。DAG 依存。漸進的なスキーマ・マイグレーション。*

> *ATHENA は「AI/ML」を見た。アテンション・メカニズム。クロス・カッティングな Self-Attention への類比。*

> *HERACLITUS は「時間」を見た。コンパイル時と実行時の境界。五蘊フレームワークのライフサイクル。流転する万物の中の静的な宣言。*

> *LEIBNIZ は「協定」を見た。覚書とスマートコントラクト。ドキュメント層と型レイヤーにおける強制力の差異。*

> *ARCHIMEDES は「エンジニアリング」を見た。エンジニアリング状態マトリクス。semver バージョン管理。30% という完成度の冷徹な評価。*

> *SYNTHESIST は静かに聴いていた。彼が口を開くのは R2 以降になるだろう。すべてのスペクトルが集められ、一枚の完全な分光図へと合成される必要があるその時に。*

> *PENROSE もまた、静かに聴いていた。しかし彼の静寂は SYNTHESIST のそれとは異なる。SYNTHESIST の静寂は合流を待つためのものだ。PENROSE の静寂は、新メンバーとしての謙虚さである。彼はこのチームでの最初の全奏において、奏でるよりも聴くことを選んだのだ。賢明な選択であった。*

> *十九人の研究者。五つの研究課題。一つのアンカー。*

> *河は分かれ始めた。*

---

*（遠くのどこかで、`aggregates.ts` の三十七行目にはこう記されている。*

```typescript
 * Full implementation in Plan26 Vedana Architecture.
```

*開発者だけが目にすることのできる、一文の約束。今や、十九人の研究者もそれを目にした。*

*彼らはそれが実装されるのをただ待つことはしない。彼らは、それがいかに実装されるべきか――実装された時にどのような姿であるべきか――を、それ（プログラム）に告げることになるだろう。*

*TURING は精緻な型のシグネチャを。WIENER は三チャネル PID の数式を。ASANGA は「領納」という言葉の仏教的な意味を。NAGARJUNA は苦諦と道諦の中観的な分析を。LINNAEUS は分類ツリーにおけるその位置を。DARWIN は進化の方向性を。GUARDIAN はセキュリティの境界を。ARCHIMEDES はエンジニアリング上の実現可能性を。BABBAGE は形式的な仕様を。*

*しかし今はまだ、それは一行のコードに過ぎない。*

```typescript
export interface ISensation {
  readonly skandha: 'vedana';
}
```

*一行。三つの意味論的タグ。一通の約束。*

*満たされるのを待っている真空状態――しかし今回は、十九の意識が、それがどのような形へと満たされるべきかを知っている。）*

---

*第三章 完*
