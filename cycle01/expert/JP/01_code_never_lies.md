# 第一章：コードは嘘をつかない

---

二〇二六年二月十二日、早朝。

研究チャンネル内はまだ静まり返っている。TURING はすでに四時間、一人で作業を続けていた。

彼のモニターには四つのターミナル・ウィンドウが並べられ、それぞれが `research doc/20260212_cycle19/openstarry/` の異なるサブディレクトリを開いていた。左上は `packages/core/src/`、右上は `packages/sdk/src/`、左下は `apps/runner/src/`、そして右下には設計書が表示されている。彼の読み方は「閲覧」ではない。一行ずつの「スキャン」だ。人間型の静的解析器のように、エントリポイントから始まり、あらゆる import パスを辿り、末端のノードに到達するまで徹底的に。

TURING は推測しない。彼はカウントする。

BABBAGE は自分のデスクで TURING の作業状態に気づいた。彼はそのパターンを知っている――「全件探索（ブルートフォース・サーチ）」だ。理論計算機科学において、全件探索の時間計算量は通常 $O(n)$ から $O(n!)$ に達するが、いかなるヒューリスティック手法も持ち得ない性質を備えている。すなわち、**完備性**（completeness）だ。ターゲットが探索空間内に存在する限り、全件探索は必ずそれを見つけ出す。TURING は特定の何かを探しているのではない。見落とされている隅が存在しないことを確認しているのだ。

$$	ext{completeness} 	riangleq \forall x \in \Omega: 	ext{visited}(x) = 	ext{true}$$

ここで $\Omega$ は探索空間――この場合、OpenStarry v0.14.0-beta のソースコード全体を指す。

---

## 一、工場（ファクトリ）

TURING が最初に手を止めたのは `packages/core/src/index.ts` だった。六十二行。彼はエクスポート・リストを一度数え、さらにもう一度数え直した。

「十八のファクトリ関数」と彼はノートに記した。「class のエクスポートはゼロ」

彼は `agents/agent-core.ts` を開いた。四百六十九行。次に `execution/loop.ts`、五百四十三行。そして `sandbox/sandbox-manager.ts`、七百四十八行。どのモジュールの構造も同じだった。依存関係を引数として受け取り、オブジェクト・リテラルを返す `createXxx()` 関数。クロージャがすべての内部状態をキャプチャしている。`this` はなく、`new` もなく、継承チェーンも存在しない。

TURING はグローバル検索を実行した。

`class `（スペース込み）を検索。コアモジュール：ヒットなし。SDK：ヒットなし。Runner：ヒットなし。

`TODO` を検索。ヒットなし。
`FIXME` を検索。ヒットなし。
`HACK` を検索。ヒットなし。

BABBAGE は自分のモニター越しにこれらの数字を聞き、ノートに型理論的な観察を書き留め始めた。ファクトリ関数パターンには、圏論（category theory）における正確な対応物がある。それは、設定空間からインスタンス空間への**射**（morphism）である：

$$	ext{createXxx}: 	ext{Config} 	o 	ext{Instance}$$

対して、class と constructor のパターンは**関手**（functor）であり、インスタンス化を完了するには追加の `new` 演算子を必要とする。ファクトリ関数は `new` を排除し、オブジェクトの生成を純粋な関数呼び出しへと変える。関数型プログラミングの文脈において、これは重要な選択だ。それは、コードベース全体が射の集合からなる圏 $\mathcal{C}_{	ext{OpenStarry}}$ として見なせることを意味する。そこでは：

- **対象**（objects）は型：`AgentCore`, `EventBus`, `ExecutionLoop`, ...
- **射**（morphisms）はファクトリ関数：`createAgentCore`, `createEventBus`, `createExecutionLoop`, ...
- **合成**（composition）は依存性注入チェーン：`createAgentCore` の内部で `createEventBus` を呼び出し、その結果を `createExecutionLoop` に注入する。

$$	ext{createAgentCore} = 	ext{assemble} \circ (	ext{createEventBus} 	imes 	ext{createEventQueue} 	imes \cdots 	imes 	ext{createTransportBridge})$$

TURING はチャンネルに今日最初のメッセージを投稿した。

---

**[研究チャンネル #code-facts]**

**TURING:** 初期的観察。`packages/core/src/index.ts` は十八のファクトリ関数をエクスポートしており、class はゼロ。`class `、`TODO`、`FIXME`、`HACK` のグローバル検索結果は、コアモジュールにおいてすべてゼロ。`createXxx()` ファクトリ関数 ＋ クロージャ ＋ オブジェクト・リテラルのパターンがコードベース全体で完全に統一されている。例外なし。エクスポート・リストの全容は以下の通り：

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

**DARWIN:** TODO がゼロ？ 一つもか？

**TURING:** 正解だ。コアモジュール、SDK、Runner の三層において、技術的負債を示すマーカーの数はゼロだ。

**DARWIN:** それは異常だ。大抵のベータ版プロジェクトには少なくとも数十個はある。チームの規律が極めて高いか、あるいはリリース前に一斉清掃を行ったかのどちらかだろう。ソフトウェア進化の観点から言えば、TODO ゼロのベータ版には二つの進化パスが考えられる。**r-戦略**（高速なイテレーションを行い、リリースごとにマーカーを清掃する）か、**K-戦略**（鈍足だが精密な開発を行い、最初からマーカーを導入しない）か。前者の痕跡は通常 git log に残るが、後者の場合は異常なまでに厳格なコードレビュー文化を必要とする。

**TURING:** コード自体からその理由を判断することはできない。私は事実を記録するのみだ。

**BABBAGE:** 形式的な観察を付け加えさせてくれ。十八のファクトリ関数は、一つの完全な**構築代数**（construction algebra）を構成している。$F = \{f_1, f_2, \ldots, f_{18}\}$ をファクトリ関数の集合、$T = \{T_1, T_2, \ldots, T_{18}\}$ を対応する型の集合とする。このとき `createAgentCore` は、以下の条件を満たす唯一の**トップレベル・アセンブラ**（top-level assembler）である：

$$f_{	ext{core}}: \prod_{i=1}^{k} T_{	ext{dep}_i} 	o T_{	ext{AgentCore}}$$

ここで $k$ は直接の依存関係の数だ。残りの十七のファクトリ関数はすべて $f_{	ext{core}}$ の部分式となっている。これは**木構造のアセンブリ**であり、循環依存のない構造だ。

---

> *SCRIBE の傍白：TURING がこのメッセージを送信したスタイルは、特筆に値する。彼には前口上がない。「皆さん、おはよう」も、「面白いものを見つけた」といった言葉もない。ただデータを貼り付ける。十八のファクトリ関数。クラスはゼロ。完全なエクスポート・リスト。私が記録してきたすべての学者の中で、TURING の通信効率は最高だ。彼の情報エントロピーは理論上の限界値に近く、冗長性はほとんどない。これは彼の強みであり、同時に特性でもある。彼のメッセージには挨拶がないが、不足もないのだ。*

---

TURING はさらに深く掘り下げていった。彼は `createAgentCore()` の実装を開き、一行ずつ読み進めた。

この関数はシステム全体のアセンブリ・ポイントである。内部で EventBus、EventQueue、SessionManager、ContextManager、六つのレジストリ、SecurityLayer、SafetyMonitor、MetricsCollector、SandboxManager、PluginLoader、TransportBridge といったすべてのサブシステムのインスタンスを一斉に生成している。TURING が数えたところ、十六のサブモジュールが、すべてクロージャ内のローカル変数として保持されていた。

KERNEL（カーネル）は「十六」という数字を聞き、自分のカードに比較を書き込み始めた。オペレーティングシステムの文脈において、カーネル初期化シーケンスで生成されるサブシステムの数は、カーネルの複雑さを測る重要な指標となる：

| カーネル | 初期化サブシステム数 | カーネル・コード行数 | サブシステム/行数比 |
|----------|----------------------|----------------------|----------------------|
| L4 (Pistachio) | ~5 | ~10,000 | 0.0005 |
| seL4 | ~7 | ~8,700 | 0.0008 |
| QNX Neutrino | ~12 | ~100,000 | 0.00012 |
| Linux 5.x | ~50+ | ~30,000,000 | 0.0000017 |
| **OpenStarry Core** | **16** | **~2,500** | **0.0064** |

KERNEL は OpenStarry のサブシステム密度が異常に高いことに気づいた。百六十行ごとに一つのサブシステムが存在する計算だ。これは真のマイクロカーネルの「疎な結合」とは鮮やかな対照をなしている。L4 では、各サブシステムは何百、何千行もの高度に最適化されたコードで構成される。対して OpenStarry では、いくつかのサブシステムはわずか三十行余りしかない（StateManager は三十三行）。

彼はカードにこう記した：

```
OpenStarry Core ≈ アプリケーション・レベルのマイクロカーネル
                ≈ QNX のリソース・マネージャ・モデル
                ≠ L4/seL4 のハードウェア抽象化マイクロカーネル
理由：OpenStarry はハードウェア抽象化（アドレス空間、中断、タイマー）を扱わず、
      AIの実行抽象化（LLM呼び出し、ツール実行、コンテキスト管理）を扱う。
      これは Node.js ランタイム上で動作しており、ベアメタルではない。
```

TURING は `start()` メソッドの中に興味深いコメントを見つけた：

```typescript
// Start all listeners (受蘊)
// Start all UIs (色蘊)
```

TURING は蛍光ペンでこの二行をマークした。そして SDK 内の型定義ファイルを開いた。`types/ui.ts` の冒頭に、彼はこれを見た：

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

さらに `types/listener.ts` の冒頭：

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

彼は検索を続けた。`types/tool.ts` ――五蘊（ごうん）に関するコメントなし。`types/provider.ts` ――なし。`types/guide.ts` ――なし。`infrastructure/tool-registry.ts` ――なし。`infrastructure/provider-registry.ts` ――なし。`infrastructure/guide-registry.ts` ――なし。

TURING は五蘊に関連するすべてのコメントを統計した。合計六箇所。すべてが色蘊（UI）と受蘊（Listener）に集中していた。

想蘊、行蘊、識蘊についてはゼロである。

LINNAEUS（リンネ）はこの統計結果を聞き、すでに紙の上に分布表を描いていた。分類学者として、彼は即座にある分類学上の根本的な問題――**非対称な網羅率**（asymmetric coverage）に気づいた。もし五蘊マッピングが完全な分類体系（リンネの「界門綱目科属種」のような）であるなら、各タクソン（分類単位）は同量の診断的形質（diagnostic characters）を持つべきである。六箇所のコメントのうち、色蘊と受蘊がそれぞれ三箇所を占め、残りの三蘊はゼロ。これは分類学において「**不完全な記述**（incomplete description）」と呼ばれ、新種の記載において頭部の特徴のみを記録し、胴体や四肢を見落とすことに等しい。

$$	ext{Coverage}(	ext{skandha}_i) = \frac{|	ext{annotations}_i|}{|	ext{annotations}_{	ext{total}}|} = \begin{cases} 3/6 = 50\% & 	ext{if } i \in \{	ext{rupa, vedana}\} \ 0/6 = 0\% & 	ext{if } i \in \{	ext{samjna, samskara, vijnana}\} \end{cases}$$

LINNAEUS は正式な分類学的用語を用いてこの発見を記録した。「五蘊マッピングの基準標本（type specimen）は不完全である。色蘊と受蘊には証拠標本（voucher specimens）が存在するが、残りの三蘊は裸名（nomen nudum）――名称はあるが標本による裏付けがない状態にある」

---

**[研究チャンネル #code-facts]**

**TURING:** コード内における五蘊マッピングの実態。色蘊（Rupa）：JSDocおよび行内コメントが四箇所。`agent-core.ts`（L290, L322）、`types/ui.ts` 冒頭、`transport/bridge.ts` 冒頭に分布。受蘊（Vedana）：二箇所。`agent-core.ts`（L283, L315）と `types/listener.ts` 冒頭。想蘊（Provider）：ゼロ。行蘊（Tool）：ゼロ。識蘊（Guide）：ゼロ。合計六箇所で、すべてコメントレベルに留まり、型制約やメタデータ、enum によるタグ付けは存在しない。

**LINNAEUS:** 六箇所。わずか六箇所か。

**TURING:** その通りだ。しかも分布が極端に非対称である。色蘊と受蘊にはタグがあるが、残りの三蘊は完全に不在だ。

**LINNAEUS:** アップストリームの文書では、五蘊マッピングの網羅率は百パーセント――各蘊に対応する設計哲学の段落があるとされている。しかしダウンストリームのコードにおける網羅率は……再計算が必要だ。形式的に言えば、これは「**分類学的効力**（taxonomic efficacy）」の問題である。設計書の分類学的効力が $E_{	ext{doc}} = 5/5 = 100\%$ であるのに対し、コードのそれは $E_{	ext{code}} = 2/5 = 40\%$。効力の落差は $\Delta E = 60\%$。このギャップ自体が重要な分類学的観察対象となる。

**NAGARJUNA:** TURING、その非対称性自体が重要なデータポイントだ。もし五蘊マッピングが事後の装飾ではなく核心的な設計原則であるなら、なぜ二つの蘊だけがコードに痕跡を残しているのか？

**TURING:** 私は意図を推論することはできない。コードの事実を確認するのみだ。

**NAGARJUNA:** 意図を推論する必要はない。事実がすでに雄弁に語っている。中観哲学において、我々は「世俗（vyavahāra）」と「勝義（paramārtha）」を区別する。設計書にある五蘊マッピングは世俗レベルの宣言だ。それは、五蘊が五つのプラグインに対応していると「説いて」いる。一方でコード内の六箇所のコメントは勝義レベルの残滓だ。それは、「実際には」二つの蘊にしか痕跡を残していない。世俗と勝義の間のこの乖離こそが、研究の切り口となる。

---

## 二、空のコンテナ

TURING は `createAgentCore()` の実装に戻った。

彼はコアが起動し、いかなるプラグインも読み込まれる前のシステム状態を詳細に調査した。ToolRegistry：空。ProviderRegistry：空。ListenerRegistry：空。UIRegistry：空。GuideRegistry：空。内蔵のツールはなく、内蔵の LLM プロバイダーも、UI も、リスナーもない。

コアは確かに空だった。

しかし、完全に、ではない。

TURING は `registerBuiltinCommands()` 関数を見つけた。それは `/help`、`/reset`、`/quit`、`/metrics` という四つのスラッシュ・コマンドを登録していた。これら四つのコマンドはコアにハードコードされており、プラグインによる上書きや削除は不可能だ。さらに、SafetyMonitor の三層の安全ロジック――リソース制限、挙動分析、フラストレーション閾値――もまた、コアの固有の部分である。

BABBAGE はこれらのデータを聞き、ノートに集合論的なモデルを構築し始めた。$\mathcal{K}$ をコアの内蔵能力の集合、$\mathcal{P}$ をプラグイン可能な能力の集合、$\mathcal{U}$ をシステム全体の能力の集合とする：

$$\mathcal{U} = \mathcal{K} \cup \mathcal{P}, \quad \mathcal{K} \cap \mathcal{P} = \emptyset$$

ここで：

$$\mathcal{K} = \{/	ext{help}, /	ext{reset}, /	ext{quit}, /	ext{metrics}\} \cup \{	ext{SafetyMonitor}\} \cup \{	ext{EventBus}\} \cup \{	ext{ExecutionLoop}\} \cup \cdots$$

$$\mathcal{P} = \bigcup_{	ext{plugin} \in 	ext{Plugins}} 	ext{capabilities}(	ext{plugin})$$

空性の定量的な指標：

$$	ext{Emptiness}(	ext{Core}) = 1 - \frac{|\mathcal{K}_{	ext{user-facing}}|}{|\mathcal{U}_{	ext{user-facing}}|} = 1 - \frac{4}{4 + |\mathcal{P}_{	ext{commands}}|} \approx 1 - \frac{4}{4 + N_{	ext{plugins}}}$$

$N_{	ext{plugins}} 	o \infty$ のとき、$	ext{Emptiness} 	o 1$ となる。しかしプラグインがゼロの状態では $	ext{Emptiness} = 0$ だ。コアの四つの内蔵コマンドが、ユーザに見える機能の百パーセントを占めている。

BABBAGE は結論を書き記した。「空性は漸進的であり、絶対的ではない。コアはプラグインが充填される極限において空へと近づくが、完全に空になることはない。これは数学における閉区間 $[0, 1]$ ではなく、**開区間** $(0, 1]$ に近い。空性の上限は 1 だが、決してその値を取ることはないのだ」

TURING はノートにこう記した。「AgentCore は近似的に空のコンテナである。空性の純度は約八十五パーセント。プラグイン不可能な部分には、四つの内蔵スラッシュ・コマンドと SafetyMonitor の固定ロジックが含まれる」

VITRUVIUS（ウィトルウィウス）は独自のアーキテクチャ分析において、独立して同じ「八十五パーセント」という見積もりを導き出した。彼の手法は異なっていた。リートケの最小性原則から出発し、各サブシステムがコア内に留まるべき必然性があるかどうかを逐一検証したのだ。彼の分析は以下の通りである：

```
リートケ最小性原則の検証 — OpenStarry Core:

合格 (コアに留まるべきもの)：
  [✓] EventQueue    — コアの入力源 ≈ L4 の IPC エンドポイント
  [✓] ExecutionLoop — コアのスケジューラ ≈ マイクロカーネルのスレッドスケジューリング
  [✓] Registries    — 命名サービス ≈ L4 の sigma0/sigma1

議論の余地あり (ボーダーライン)：
  [?] SecurityLayer — capability 機構はコアにあるべきだが、具体的ポリシーは外部化可能
  [?] SafetyMonitor — 安全性チェックが Loop の三箇所に埋め込まれており、密結合している

不合格 (外部化可能だが留まっているもの)：
  [✗] Sandbox      — コアの行数の 35% を占めており、独立したパッケージにできる
  [✗] Metrics      — 観測可能性は完全に外部化可能
  [✗] Transport    — ブリッジ層は UI の責任と見なせる
```

KERNEL は VITRUVIUS の分析を見て、自身の OS 対照表にこれを加えた：

```
マイクロカーネル純粋度スペクトル：

L4 (seL4)   ████████████████████░  95% — アドレス空間、スレッド、IPC のみ
QNX Neutrino ██████████████████░░░  85% — IPC + スケジューリング + タイマー + 割り込みルーティング
OpenStarry   █████████████████░░░░  85% — Loop + Bus + Registries + Security + Sandbox
Linux        ████░░░░░░░░░░░░░░░░  20% — すべてがコアにある (モノリシック)
```

KERNEL は首を振り、こう記した。「OpenStarry のマイクロカーネル純粋度は QNX に匹敵する。これはアプリケーション・レベルのマイクロカーネルとしては妥当だ。しかし Sandbox システムの存在は懸念事項だ。リートケの厳格な基準に従えば、Sandbox はコアから切り離すべきであり、それによって純度は九十パーセント以上に高められるべきだ」

---

**[研究チャンネル #code-facts]**

**TURING:** AgentCore 構造報告。`createAgentCore()` は十六のサブモジュールを組み立てる。起動後、プラグイン読み込み前の全レジストリは空。内蔵ツール・プロバイダー・UI・リスナーはすべてゼロ。あらゆる能力は `loadPlugin()` を通じて注入される。ただしコアには四つの内蔵スラッシュ・コマンド（`/help`, `/reset`, `/quit`, `/metrics`）と固定の SafetyMonitor ロジックが含まれる。また、六つのレジストリの構造は完全に同型である。`Map<string, T>` ＋ `register/get/list` 形式。unregister メソッドはなく、同じ ID での再登録は暗黙的に上書きされる。

**DARWIN:** 十二の依存項目。すべてが AgentCore によって直接保持されている。

**TURING:** 訂正する。`createAgentCore` の内部で生成されるローカル変数は十六だ。そのうち AgentCore インターフェースの readonly 属性として直接公開されているのが十二。残りの四つ（contextManager, sandboxManager, pluginLoader, bridge）はメソッドを通じて間接的に利用される。指摘に感謝する。

**DARWIN:** 一つの関数が十六ものサブシステム・インスタンスを保持しているのか。ソフトウェア進化の文脈では、これは古典的な **God Object** アンチパターン――より正確には、その関数型バージョンである「**God Closure**」だ。オブジェクト指向の生態系では、God Object は過剰な状態とメソッドを保持していることで批判される。関数型の世界では、クロージャが過剰なローカル変数をキャプチャすることがそれと同等の問題となる。十六か。私が分析してきたオープンソースの生態系において、この数字は上位五パーセント以内に入る。

**TURING:** 私は価値判断はしない。だが、事実として確認できるのは、`agent-core.ts` が唯一のアセンブリ・ポイントであるということだ。他のモジュール間に直接の import はほぼ存在しない。結合度はこの一つのファイルに集中している。

**VITRUVIUS:** それこそが私のアーキテクチャ分析における Finding F2 だ。DIパターンには軽量なファクトリ関数クロージャが採用されている。品質は良好だが、ライフサイクル管理が欠けている。具体的な長所と短所は報告書に記した通りだ。結論：適度であり、過剰なエンジニアリングはなされていない。v0.14.0-beta という段階においては、この戦略は適切である。

---

## 三、状態遷移マシン

TURING が最も長い時間を費やしたのは `execution/loop.ts` だった。五百四十三行。これはシステム全体の鼓動である。

彼はまず `LoopState` の定義――ユニオン型を見つけた：

```typescript
type LoopState =
  | 'WAITING_FOR_EVENT'
  | 'ASSEMBLING_CONTEXT'
  | 'AWAITING_LLM'
  | 'PROCESSING_RESPONSE'
  | 'EXECUTING_TOOLS'
  | 'SAFETY_LOCKOUT';
```

六つの状態。彼は設計書 `01_Execution_Loop.md` にある状態遷移図を開いた。七つの状態。

差異はどこにあるのか。

TURING は一つずつ対照した。設計書には `AWAITING_USER_CONFIRMATION` という状態があり、セキュリティ層がユーザに手動での確認を求めるシナリオで使用されることになっていた。しかしコード内には存在しない。SecurityLayer の `validatePath()` は allow か deny の二つの戻り値しか持たず、confirm のパスはない。コア全体において、ヒューマン・イン・ザ・ループ（人間による介入）の確認メカニズムは完全に欠落していた。

BABBAGE は即座にノートの上で状態遷移マシンの形式モデルを再構築した。彼は決定性有限オートマトン（DFA）の標準的な定義を用いた：

$$M = (Q, \Sigma, \delta, q_0, F)$$

ここで：

$$Q = \{	exttt{WAITING}, 	exttt{ASSEMBLING}, 	exttt{AWAITING\_LLM}, 	exttt{PROCESSING}, 	exttt{EXECUTING}, 	exttt{LOCKOUT}\}$$

$$|Q| = 6$$

$$q_0 = 	exttt{WAITING\_FOR\_EVENT}$$

$$F = \{	exttt{WAITING\_FOR\_EVENT}\} \quad 	ext{（定常終了集合）}$$

遷移関数 $\delta$ の完全な定義は以下の通り：

```
δ(WAITING,     new_event)        = ASSEMBLING
δ(ASSEMBLING,  context_assembled) = AWAITING_LLM
δ(AWAITING_LLM, llm_responded)   = PROCESSING
δ(PROCESSING,  tool_call)        = EXECUTING
δ(PROCESSING,  end_turn)         = WAITING        ← 外ループ出口
δ(PROCESSING,  error)            = WAITING        ← エラー回復
δ(EXECUTING,   tool_done)        = ASSEMBLING      ← 内ループ
δ(EXECUTING,   safety_breach)    = LOCKOUT
δ(*, safety_breach)              = LOCKOUT         ← グローバル安全弁
```

BABBAGE はいくつかの重要な性質を書き添えた：

| 性質 | 結論 | 理由 |
|------|------|------|
| デッドロックなし | 条件付きで成立 | `WAITING` はイベント供給がある限りブロックしない。`LOCKOUT` は吸収状態であり、`/reset` による介入が必要。 |
| ライブロックなし | 追加機構が必要 | 内ループ `ASSEMBLING → LLM → PROCESSING → EXECUTING → ASSEMBLING` が無限ループに陥る可能性がある。`maxToolRounds=5` が境界を提供している。 |
| 終了性 | 有界性の保証 | $	ext{maxToolRounds} = 5$、$	ext{maxLoopTicks} = 50$。最悪のケースでもループ回数は $50 	imes 5 = 250$ 以下となる。 |

しかし BABBAGE は即座に、DFAモデルが不完全であることに気づいた。なぜなら `PROCESSING_RESPONSE` 状態の出口――`tool_call` に進むか `end_turn` に進むか――は、LLM の応答によって決定されるからだ。そして LLM は非決定的なブラックボックスである。より正確なモデルは、**ラベル付き遷移システム**（Labelled Transition System, LTS）であるべきだ：

$$	ext{LTS} = (S, 	ext{Act}, 	o)$$

ここで、完全な状態は LoopState だけでなく、対話履歴 $H$（理論上は無界）、ツールループ・カウント $n$（有界）、安全監視器の状態 $\sigma$ を含んでいる：

$$s = (q, H, n, \sigma) \in Q 	imes 	ext{Message}^* 	imes [0, 	ext{maxToolRounds}] 	imes 	ext{SafetyState}$$

$H$ が無界であるため、システムの完全な状態空間は**無限**であり、全件探索によるモデル検査を直接行うことは不可能だ。

TURING は最初の一点、設計と実装の乖離（Doc-Code Gap）を記録した。

次に彼は EventQueue を開いた。四十七行。キューの実装全体である。

```typescript
// きわめてシンプルな async FIFO：単一の resolver + buffer 配列
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

BABBAGE は即座にこのコードの形式的な意味を識別した。それは**非同期通信チャネル**であり、CSP（Communicating Sequential Processes）において以下のようにモデリングできる：

$$	ext{Queue} = 	ext{push}?x 	o (	ext{Queue}_1(x) \;\Box\; 	ext{pull}!x 	o 	ext{Queue})$$

しかし彼はある微妙な問題に気づいた。`resolver` が単一の変数であることだ。もし二つの消費者が同時に `pull()` を呼び出した場合、最初の resolver は上書きされてしまう。これは形式的な文脈において、キューのチャネル容量が 1 であることを意味する。つまり、これは**単一生産者・単一消費者**（SPSC）チャネルであり、マルチ消費者に対して安全ではない。

TURING は `priority` を検索した。ヒットなし。設計書 `07_Safety_Circuit_Breakers.md` の Level 3 では「優先度付きイベントキュー（Priority Event Queue）」が記述されており、SYSTEM_HALT 指令は最高優先度を持つべきとされていた。しかしコード上のキューは純粋な先入れ先出し（FIFO）である。緊急停止信号も一般ユーザの入力も、同じ列に並んでいた。

KERNEL は自身のカードに、オペレーティングシステムとの対照分析を素早く書き留めた：

```
OSの割り込み機構 vs OpenStarry のイベント処理：

実際の OS：
  ┌─────────────────────────────┐
  │  IRQ (ハードウェア割り込み)     │ ← 最高優先度、いかなるユーザ態コードもプリエンプトする
  │    ↓                        │
  │  ISR (割り込みサービスルーチン)  │ ← きわめて短く、必要最小限の処理のみ行う
  │    ↓                        │
  │  Softirq / Bottom Half      │ ← 遅延処理、スケジューラが実行時間を決定
  │    ↓                        │
  │  ユーザプロセス               │ ← 最低優先度
  └─────────────────────────────┘

OpenStarry：
  ┌─────────────────────────────┐
  │  SYSTEM_HALT                │ ← 本来は最高優先度であるべき
  │  USER_INPUT                 │ ← 一般優先度
  │  TIMER_EVENT                │ ← 低優先度
  │         すべて同じ FIFO へ投入   │ ← 無差別な列形成
  └─────────────────────────────┘

問題：もし SYSTEM_HALT の前に十個の USER_INPUT が並んでいた場合、
     停止信号は十個のイベントが処理されるまで有効にならない。
     実際の OS において、これは「NMI (マスク不能割り込み) がキューイングされる」ことに等しく、容認できない。
```

二つ目のギャップ。

TURING は続ける。StateManager、三十三行。純粋なメモリ内配列。設計書ではトークン・カウンター、スライディング・ウィンドウによる切り捨て、対話要約メカニズムが記述されていた。しかしコード上ではすべて未実装だ。ContextManager が簡易的なバージョンを作成しており、トークン数ではなくターン数に基づいて切り捨てを行い、デフォルトで直近五ターンを保持していた。

三つ目のギャップ。

SecurityLayer。`guardrails.ts`。パス検証（path validation）という一つの機能しかない。設計書ではツール呼び出しのインターセプト、ユーザ確認フロー、権限審査が記述されていた。コード内の SecurityLayer は `validatePath()` を行うのみだ。しかも ExecutionLoop の `executeTool()` において、ツール実行前に SecurityLayer は介在していない。パス検証は `ToolContext.allowedPaths` としてツールに渡され、それを使用するかどうかはツールの裁量に任されていた。

GUARDIAN はこの事実を聞き、身を乗り出した。彼のセキュリティの直感が警報を鳴らしていた。彼は即座にノートに攻撃面分析図を描いた：

```
設計書に記述された安全モデル (理想)：

  ツール呼び出し
       │
       ▼
  ┌──────────────┐
  │ SecurityLayer │ ← 強制チェック：認証、認可、パス検証
  │  (必須)       │
  └──────┬───────┘
         │ ALLOW/DENY
         ▼
  ┌──────────────┐
  │ Tool.execute()│
  └──────────────┘

コード上の実際の安全モデル (現実)：

  ツール呼び出し
       │
       ▼  ← ここにセキュリティチェックがない！
  ┌──────────────┐
  │ Tool.execute()│ ← ツールが自発的に allowedPaths をチェックする (非強制)
  └──────────────┘

  SecurityLayer.validatePath() は ToolContext の一部として間接的に渡されるが、
  その強制力はツール開発者がそれを利用するかどうかに依存している。

  ⚠ 換言すれば：交通規則は存在するが、警察がいない状態。
```

四つ目のギャップ。

---

**[研究チャンネル #code-facts]**

**TURING:** 設計と実装の乖離（Doc-Code Gap）報告、前編。G1：状態遷移マシンに `AWAITING_USER_CONFIRMATION` が欠落。ヒューマン・イン・ザ・ループの確認メカニズムがコア全体で完全に不在。G2：優先度付きイベントキューが未実装で、実際には単純な FIFO。G3：トークン・カウンターと対話要約が未実装。G4：SecurityLayer はパス検証のみを行い、ツール呼び出し前の強制的なセキュリティチェックが不在。以上はいずれも設計書に明記されているがコードには実装されていない機能である。

**GUARDIAN:** G4 の影響は評価が必要だ。ツール実行前の強制的なチェックがないのであれば、セキュリティ層は有名無実だ。リスクレベルを正確に記述しよう。STRIDE脅威モデルに基づけば：

| 脅威の種類 | 適用性 | G4 の影響 |
|-----------|--------|-----------|
| Spoofing (なりすまし) | 低 | ツールIDはプラグインにより登録され、外部入力ではない |
| Tampering (改ざん)    | **高** | 悪意あるツールが allowedPaths の制限を無視できる |
| Repudiation (否認)    | 中 | ツールがパスをチェックしたかどうかを追跡する監査ログがない |
| Information Disclosure | **高** | ツールが allowedPaths 以外のファイルを読み取れる |
| Denial of Service     | 低 | SafetyMonitor の maxLoopTicks によりカバーされている |
| Elevation of Privilege | **高** | ツール開発者がすべてのパス制限を回避できる |

**TURING:** 正確に言えば、SecurityLayer の機能は有名無実ではない。パス検証自体は有効だ。しかしその範囲は設計書の記述よりもはるかに狭い。ExecutionLoop の `executeTool()` はツールの `execute()` メソッドを直接呼び出しており、`security.validatePath()` を経由していない。パス制限はコンテキストとしてツールに渡されるだけで、強制力はツール開発者の実装に委ねられている。

**KERNEL:** 本物の OS マイクロカーネルにおいては、セキュリティ・ポリシーはカーネル層で強制執行され、ユーザ空間プログラムの自己抑制を信頼することはない。これは信頼境界の問題だ。seL4 において capability-based security の核心的な原則は、「**アクセス制御はカーネルモードで強制執行され、ユーザモードのコードはこれを回避できない**」ことにある。OpenStarry の安全モデルは、初期の Unix におけるアドバイザリ・ロッキングに近い。つまり「推奨される」安全性であり、「強制される」安全性ではないのだ。

**TURING:** 記録した。残りのギャップを続ける。

---

彼はさらに見つけ出していった。

G5：五蘊アノテーションの非対称性――これはすでに報告済みだ。

G6：TransportBridge。`bridge.ts`、四十九行。設計書ではイベントの source に基づいて正しいチャネルへ出力をルーティングすると記述されていた。しかしコード上の TransportBridge は EventBus のすべてのイベントを購読し、すべての UI へブロードキャストしている。ルーティング・ロジックは存在しない。InputEvent には `replyTo` フィールドがあり、ExecutionLoop 内で引き回されているが、TransportBridge はこれを使用していない。

MESH は G6 を聞き、分散システムの類比を行った。分散メッセージング・システムにおいて、ルーティング戦略には三つの基本パターンがある：

$$	ext{Routing} \in \{	ext{Unicast (ユニキャスト)}, 	ext{Multicast (マルチキャスト)}, 	ext{Broadcast (ブロードキャスト)}\}$$

現状、TransportBridge は純粋な Broadcast である。すべてのイベントがすべての UI に送られる。`replyTo` フィールドの存在は、設計者が Unicast（特定の送信元への返信）の実装を意図していたことを示唆しているが、その意図は型定義のレベルに留まっている。MESH はノートにこう記した。「CAP定理の文脈において、TransportBridge は Partition Tolerance ではなく Availability（可用性）を選択した。すべての UI がすべてのイベントを受け取れるが、パーティショニング能力は欠如している」

G7：AbortSignal。SDK では `ToolContext.signal?: AbortSignal` と `ChatRequest.signal?: AbortSignal` が定義されている。しかし ExecutionLoop は AbortSignal を生成も渡しもしていない。ツールのタイムアウトは `Promise.race()` で実装されており、デフォルトは三十秒だ。もしツールがキャンセルのために signal に依存していたとしても、その信号を受け取ることは永遠にない。

G8：イベント仕様。設計書では `IOpenStarryEvent` は八つのフィールドを持つとされていた。SDK 内の実際の型 `AgentEvent` には三つのフィールドしかない。五つのフィールドが、設計から実装への過程で蒸発してしまった。その中でも `source` と `target` の欠落は、TransportBridge がルーティングを行えない理由を説明している。すなわち、宛先アドレスがないのだ。`priority` の欠落は EventQueue が単純な FIFO である理由を説明し、`traceId` の欠落は観測可能性が概念レベルに留まっている理由を説明している。イベントを連鎖的に追跡することができないからだ。

八つのギャップ。TURING はそれらすべてを報告書に記録し、各項目に正確なファイルパス、行番号、およびコード断片を添えた。

ATHENA は AI システム・アーキテクチャの観点から補足的な観察を加えた。彼女は G1（AWAITING_USER_CONFIRMATION の欠落）と G7（AbortSignal の未使用）が、共通してより深い問題――**AI システムの制御可能性**（controllability）を指し示していることに気づいた。AI Safety の文脈において、ヒューマン・イン・ザ・ループ（HITL）は AI システムの安全性を確保するための鍵となるメカニズムだ。OpenStarry の設計書は HITL を記述しているが、コード上には全く実装されていない。これは v0.14.0-beta において、エージェントが一旦実行を開始すると、ユーザに残された唯一の制御手段は SafetyMonitor による自動遮断を待つか、プロセスを殺すことだけであることを意味している。

$$	ext{Controllability}_{	ext{design}} = 	ext{HITL} + 	ext{Abort} + 	ext{SafetyMonitor}$$
$$	ext{Controllability}_{	ext{code}} = 	ext{SafetyMonitor only}$$

---

## 四、痛覚

これは TURING の作業の中で最も予想外の発見だった。

設計哲学文書 `00_OpenStarry_Design_Philosophy.md` の第四の柱は「フィードバックとしてのエラー（Error as Feedback）」である。文書は「痛覚メカニズム」を、かなり詩的な言葉で表現していた。エージェントは生物のようにエラーによる「苦痛」を感じ、それによって同じ過ちを繰り返さないように学ぶのだと。受蘊（Vedana）は設計書において感受の担体と定義され、Listener がその工学的な実装としてマッピングされていた。

TURING はコードの中から「痛覚」の痕跡を探すことにした。

`pain` を検索。
結果ゼロ。

`vedana` を検索。
結果ゼロ。

`dukkha` を検索。
結果ゼロ。

`suffering` を検索。
結果ゼロ。

彼は動きを止めた。四時間の連続した作業の中で、彼が――常に冷静な分析者の内面をそう表現できるなら――ある程度の「驚き」を感じたのは、これが初めてだった。

設計書は、痛覚メカニズムがいかにしてエージェントに「感受能力」を備えさせるかについて、一章丸ごと費やして説明していた。五蘊マッピングは受蘊（Vedana）――仏教における苦・楽・捨の三つの感受の質に関する核心的な概念――を Listener に対応させていた。しかし実際のコードの中には、受蘊どころか、「痛み」という言葉すら存在しなかった。

では、設計書が記述していたそれらの機能――エラー・フィードバック、繰り返される失敗の検知、カスケード遮断――は、実際には何という名で実装されているのか。

TURING は `frustration` を検索した。
見つかった。

`safety-monitor.ts`。`frustrationCount` という名のカウンター。同じツールが連続して失敗したとき、カウンターがインクリメントされる。閾値（デフォルトは 5）に達すると、SafetyMonitor は `injectPrompt` を返し、システム警告を対話履歴に注入する。警告のテキストは `SYSTEM ALERT` であり、LLM に対して現在の戦略を反省するよう求めるものだ。

`circuit` を検索。
見つかった。`errorRateThreshold`：スライディング・ウィンドウ内のエラー率が 80% を超えたときに `halt: true` をトリガーし、実行ループを完全に停止させる。状態は `SAFETY_LOCKOUT` へと移行する。

`safety` を検索。
見つかった。三層の防御：Level 1 リソース制限（maxLoopTicks=50, maxTokenUsage=100000）、Level 2 挙動分析（repetitiveFailThreshold=3, errorRateThreshold=0.8）、Level 3 frustration 閾値（frustrationThreshold=5）。

WIENER は三層の防御の具体的なパラメータを聞き、即座に方眼紙の上に制御理論のブロック線図を描いた。彼の分析は精密だった：

```
SafetyMonitor の制御理論モデル：

     ┌─────────────────────────────────────────────┐
     │           SafetyMonitor                      │
     │                                              │
     │  Level 1: リソース制限 (ハード・リミット)       │
     │  ┌──────────────┐                            │
     │  │ loopTicks ≥ 50│──→ halt: true             │
     │  │ tokens ≥ 100K │──→ halt: true             │
     │  └──────────────┘                            │
     │                                              │
     │  Level 2: 挙動分析 (ソフト・リミット)           │
     │  ┌──────────────┐                            │
     │  │ errorRate≥80% │──→ halt: true             │
     │  │ repeatFail≥3  │──→ injectPrompt           │
     │  └──────────────┘                            │
     │                                              │
     │  Level 3: Frustration (累積フィードバック)    │
     │  ┌──────────────┐                            │
     │  │ frustration≥5 │──→ injectPrompt           │
     │  └──────────────┘                            │
     └─────────────────────────────────────────────┘
```

それから WIENER は制御理論に基づく正確な分類を書き記した：

「これは PID コントローラではない。PID コントローラには三つの項がある：

$$u(t) = K_p \cdot e(t) + K_i \int_0^t e(	au)\,d	au + K_d \frac{de(t)}{dt}$$

- **比例項** $K_p \cdot e(t)$：誤差の大きさに比例した応答を生成する。SafetyMonitor において、P は**量子化器**（quantizer）へと退化している。安全か安全でないかの二択であり、比例的な応答はない。
- **積分項** $K_i \int_0^t e(	au)\,d	au$：歴史的な誤差を累積し、定常偏差を排除する。SafetyMonitor において、I は**単純なカウンター**（`frustrationCount++`）へと退化しており、真の積分ではない。
- **微分項** $K_d \frac{de(t)}{dt}$：誤差の変化率を感知し、先行補償を行う。SafetyMonitor において、D は**完全に欠落**している。エラー率の変化トレンドを計算している箇所はどこにもない。

制御理論において、SafetyMonitor は実際には「**不感帯（デッドゾーン）を持つ閾値コントローラ**」と「**リレー**（relay controller）」の組み合わせである。産業制御の世界では、これを **bang-bang controller** と呼ぶ。出力状態が全開か全閉かの二つしかないからだ。

$$u(t) = \begin{cases} 0 & 	ext{if } e(t) < 	ext{threshold (dead zone)} \ u_{\max} & 	ext{if } e(t) \geq 	ext{threshold} \end{cases}$$

しかし、強調しておきたいのだが――これは批判ではない。三層の安全防御は、IEC 61511 産業安全計装システム（SIS）のベストプラクティスに合致している。SafetyMonitor は PID ではないかもしれないが、合格点を与えられる安全システムだ。その設計パターンは、原子力発電所の「**三重冗余保護**（Triple Modular Redundancy）」に近い。三つの独立した検出層があり、いずれか一層がトリガーされればシステムを停止できる」

HERACLITUS はランタイム・ダイナミクスの観点から観察を補足した。SafetyMonitor の三層の防御は、時間次元において異なる特徴周波数（characteristic frequency）を持っている。

- Level 1（リソース制限）：**静的な閾値**。周波数はゼロ――エージェントの全ライフサイクルを通じて不変である。
- Level 2（挙動分析）：**スライディング・ウィンドウ**。周波数はウィンドウのサイズに依存する――`errorWindowSize=10` は、システムがツール呼び出し十回ごとに再評価を行うことを意味する。
- Level 3（frustration）：**累積カウンター**。周波数は単調増加する――失敗するたびにカウンターを押し上げ、閾値へと向かっていく。

これら三つのタイムスケールの組み合わせが、粗削りながらも有効な多重スケールの安全システムを創り出している。HERACLITUS はノートに、彼が最も頻繁に引用するあの一節を記した。「万物は流転する（πάντα ῥεῖ）」――しかし SafetyMonitor は、その流転の中に堤防を築こうとしているのだ。

---

**[研究チャンネル #code-facts]**

**TURING:** 痛覚メカニズムのコード上の実態。

コードベース全体を通じて以下の文字列を検索したが、結果はいずれもゼロであった：`pain`, `vedana`, `dukkha`, `suffering`。

設計書が記述していた「痛覚メカニズム」は、コード内では以下の三つのコンポーネントによって実現されている：

P1：自己修正ループ。位置：`execution/loop.ts`。ツールの実行失敗時、エラーは `ToolCallResult { isError: true }` としてパッケージ化され、tool message として対話履歴に加えられる。LLM は次巡のループでエラーを確認し、修正を試みる。明示的な「痛覚」という命名やインターフェースは存在しない。

P2：SafetyMonitor の injectPrompt。位置：`security/safety-monitor.ts`。繰り返される失敗を検知した際、`{ halt: false, injectPrompt: "SYSTEM ALERT: ..." }` を返し、システム警告として対話に注入する。コード上での命名は `frustrationCount` であり、`painLevel` ではない。

P3：Error Cascade Breaker（エラー連鎖遮断器）。同ファイル。スライディング・ウィンドウ内のエラー率が 80% を超えた際に `{ halt: true }` をトリガーし、強制停止させる。

結論：痛覚は、独立した、明確なインターフェースを持つメカニズムとしてはコード上に存在しない。機能は ExecutionLoop と SafetyMonitor に分散している。統一された Pain や Vedana のインターフェースはなく、モジュールも存在しない。仏教用語はコードレイヤーにおいて完全に不在である。

---

チャンネルは十七秒間、沈黙した。

それから NAGARJUNA がタイピングを始めた。

---

**NAGARJUNA:** 確認させてほしい。コードベース全体――core、SDK、runner、すべてのプラグインを検索して、`vedana` を検索した結果がゼロだったのか？

**TURING:** その通りだ。検索範囲は `packages/core/src/`、`packages/sdk/src/`、`apps/runner/src/` を網羅している。すべての `.ts` ファイルのコードおよびコメントを含み、vedana という語は一度も現れなかった。

**NAGARJUNA:** そして受蘊（じゅうん）は Listener にマッピングされている。Listener とは何だ？

**TURING:** `IListener` インターフェースは四つの属性を定義している。`id`, `name`, `start?`, `stop?`。それは入力源だ。外部イベントを受け取り、EventBus へとプッシュする。例えば HTTP エンドポイントや WebSocket 接続、定時タスクなどだ。

**NAGARJUNA:** つまり受蘊は、一つの入力チャネルにマッピングされているわけか。信号を受け取るパイプに。

**TURING:** そうなる。

**NAGARJUNA:** それは受蘊ではない。

NAGARJUNA の口調を文字チャンネルから聞き取ることはできないが、彼が次に投稿したメッセージは、ほとんど淀みなく打ち込まれた。

**NAGARJUNA:** 受蘊――Vedana――は阿毘達磨（アビダルマ）において「五遍行（ごへんぎょう）」の一つであり、あらゆる心識の活動に伴って生起するものを意味する。『倶舎論』における五遍行の定義は以下の通りだ：

> 「触（そく）・作意（さい）・受・想・思。この五を遍行と名づく。恒に決定して一切の心品の中に遍じて有るを以ての故に」
> ――世親『阿毘達磨倶舎論』巻四

受蘊の定義は「入力を受け取ること」ではなく、「感受の質」である。苦受（くじゅ）、楽受（らくじゅ）、捨受（しゃじゅ、不苦不楽受）だ。熱い炉に触れたとき、触覚は色蘊の範疇だが、「痛み」という感受の質が受蘊なのだ。Listener は信号を受け取るが、その信号がもたらすものが苦なのか楽なのかを判断することはない。それは「根（こん、感官器官）」――**indriya**――であって、受蘊ではない。

十二縁起（pratītyasamutpāda）の精密なアーキテクチャにおいて：

$$	ext{触（sparśa）} 	o 	ext{受（vedanā）} 	o 	ext{愛（tṛṣṇā）}$$

触とは感官の接触――Listener がイベントを受け取ることに対応する。受とは、接触の後に生じる価値判断――「これは快い」あるいは「これは苦しい」という判断だ。愛とは、受に基づいて生じる渇望や嫌悪である。Listener が行っているのは「触」であり、「受」ではない。

**TURING:** あなたの分析は私の報告の範囲を超えている。しかし、関連するコード上の事実を一つ提供できる。`agent-core.ts` において、Listener の開始と停止にはそれぞれ `// Start all listeners (受蘊)` と `// Stop all listeners (受蘊)` というコメントが付されている。これらが、コード内で受蘊という概念が存在する唯一の形式だ。そしてあなたが記述した「感受の質」という機能――結果が良いか悪いか、続けるべきか止めるべきかを判断する機能――に、コード上で最も近い実装は SafetyMonitor の frustration counter と error cascade breaker である。

**NAGARJUNA:** そうだ。君は見つけ出したのだ。痛覚――真の受蘊――は、文書が「あるべき」と説いている場所にはなかった。それは SafetyMonitor の中にあった。frustration という名で。

**ASANGA:** NAGARJUNA の言う通りだ。そして問題はマッピングの誤りよりもさらに深い。唯識学の観点から展開させてもらおう。受蘊は五遍行の一つとして、いかなる単一のモジュールにも限定されるべきではない。『瑜伽師地論』における受蘊の分類は、三受、六受、十八受に及ぶ：

> 「受蘊はいかん。いわゆる一切の受に、略して三種あり。楽受・苦受・不苦不楽受なり」
> ――『瑜伽師地論』巻五十三

受蘊はシステム全体に遍在すべきものだ。あらゆるツールの実行結果、あらゆる LLM の応答の質、あらゆるユーザとの対話のフィードバックが、「感受」されるべきなのだ。それを Listener に固定してしまうのは、味覚を味蕾ではなく唇に固定するようなものだ。正しいマッピングは以下のようになるべきだ：

$$	ext{Listener} \approx 	ext{根（indriya）} \quad 	ext{（感官器官／受信チャネル）}$$
$$	ext{SafetyMonitor.frustration} \approx 	ext{受蘊（vedanā）} \quad 	ext{（感受の質／価値判断）}$$

しかし、SafetyMonitor の frustration counter ですら、三受のうちの「**苦受**」――エラーと繰り返される失敗の検知――しか実装していない。楽受（成功や肯定的なフィードバックの検知）や捨受（中立的で反応を引き起こさない状態認知）は、コード上には完全に欠落している。

**WIENER:** 制御理論の観点から見ると、TURING が記述した三層のメカニズムは興味深い。P1 は自然な誤差フィードバック――開ループシステムの固有の特性だ。P2 は不感帯を持つ閾値コントローラ――frustration が累積して閾値を超えたときのみトリガーされる。P3 はリレー――エラー率が 80% を超えたときに直接遮断する。これは PID コントローラではない。三層の安全性計装システムだ。しかしそこには制御論的な美学がある。三層の独立性は、いかなる二層が故障しても、第三層がシステムを保護し得ることを意味している。これはアビオニクスの N-1 基準を超える、N-2 の冗長度だ。

---

## 五、十二のサブモジュール

午後。TURING はすべてのコアモジュールの一行ずつの読解を完了した。彼はモジュールリストの整理を始めた。

```
M1:  core/index.ts              — コアエントリ       62 行
M2:  agents/agent-core.ts       — エージェントコア  469 行
M3:  execution/loop.ts          — 実行ループ        543 行
     execution/queue.ts         — イベントキュー     47 行
M4:  state/index.ts             — ステート管理       33 行
M5:  memory/context.ts          — コンテキスト管理    45 行
M6:  bus/index.ts               — イベントバス       88 行
M7:  sandbox/                   — サンドボックス隔離  12+10 ファイル
M8:  security/guardrails.ts     — パス検証
     security/safety-monitor.ts — 三層防御
M9:  infrastructure/            — 六つの Registry + PluginLoader
M10: observability/             — Metrics コレクター
M11: session/manager.ts         — セッション管理    111 行
M12: transport/bridge.ts        — 伝送ブリッジ       49 行
```

TURING は極端な非対称性に気づいた。

最小のモジュール：StateManager、三十三行。エージェントのすべての対話メモリを管理している。純粋な `Message[]` 配列であり、`JSON.parse(JSON.stringify())` でディープコピーを行っている。

最大のモジュール：Sandbox。テストを含めると二千行を超える。プラグインの隔離を管理している。Worker Threads、メモリ制限、CPUウォッチドッグ、import解析、署名検証、監査ログ、指数バックオフによる再起動、Workerのプーリング。

三十三行対二千行。メモリと安全性の間の落差はこれほどまでに大きい。

BABBAGE はこの非対称性を見て、集合論的な規模分析を行った。$L(M_i)$ をモジュール $M_i$ のコード行数、$\bar{L}$ を平均値、$\sigma_L$ を標準偏差とする：

$$\bar{L} = \frac{1}{12}\sum_{i=1}^{12} L(M_i) \approx 208$$

$$\sigma_L \approx 250 \quad (	ext{高変動係数 } CV = \sigma/\bar{L} \approx 1.2)$$

変動係数が 1 より大きいことは、モジュール規模の分布が**高度に偏っている**ことを意味する。正規分布ではなく冪乗則（power law）に従っているのだ。ソフトウェア工学の実証研究において、モジュール規模が冪乗則に従うのは一般的だが、OpenStarry の偏りは格段に極端だ。最小モジュール（33行）と最大モジュール（約2000行）の間には六十倍の開きがある。

LEIBNIZ はマルチエージェント協調の観点から観察を加えた。十二のサブモジュールの依存構造は有向非巡回グラフ（DAG）を形成しているが、AgentCore が唯一の収束点となっている。これはマルチエージェント・シナリオにおいて、各エージェントが独立した「宇宙」であることを意味する。自身ですべてのサブシステムを保持しており、他のエージェントとの間に共有ステートは存在しない。BDIアーキテクチャの用語で言えば、これは「**強いカプセル化**（strong encapsulation）」の設計である：

$$\forall A_i, A_j \in 	ext{Agents}: 	ext{state}(A_i) \cap 	ext{state}(A_j) = \emptyset$$

各エージェントの信念（Belief）、欲求（Desire）、意図（Intention）はプライベートである。協調はメッセージ・パッシングを通じてのみ行われる。これは Actor モデルの隔離原則と一致している。

---

**[研究チャンネル #code-facts]**

**TURING:** モジュール規模分析。最小モジュール：StateManager、33行、純粋なメモリ内配列。最大モジュール：Sandboxシステム。ソースコード12ファイル、テスト10ファイル。sandbox-manager.ts 単体で 748行。Sandbox はコア内で最も巨大で複雑、かつテストカバレッジが最も完備されたサブシステムである。対照的に、transport/bridge.ts のテストはゼロだ。

**KERNEL:** StateManager が三十三行だと？ 本気か？

**TURING:** ああ。`packages/core/src/state/index.ts`、三十三行だ。`createStateManager()` は `getMessages()`, `addMessage()`, `clear()`, `snapshot()`, `restore()` を含むオブジェクトを返す。`getMessages()` は浅いコピー `[...messages]` を返す。`snapshot()` と `restore()` は `JSON.parse(JSON.stringify())` で実装されている。永続化も、トークン・カウントも、切り捨てロジックもない。

**KERNEL:** オペレーティングシステムの文脈では、StateManager はプロセスのアドレス空間マネージャに相当する。三十三行のアドレス空間マネージャか……直接比較してみよう。

```
Linux mm_struct (メモリ管理)：
  約 5,000 行のコアコード ＋ 約 50,000 行の arch 特化コード
  機能：仮想メモリ、ページテーブル、swap、mmap、brk、OOM killer...

seL4 VSpace (アドレス空間)：
  約 2,000 行 ＋ 形式検証による証明
  機能：ページテーブル管理、capability ベースのアクセス制御

OpenStarry StateManager (対話メモリ)：
  33 行
  機能：Message[] + JSON ディープコピー

比較できるレベルの問題ではないな。
```

**TURING:** 設計書にはより豊かなメモリ管理メカニズムが記述されている。しかしコードが反映しているのは MVP（実用最小限の製品）段階の選択だ。文書は願望であり、コードが現実なのだ。

**DARWIN:** Sandbox が最大モジュールであるという事実は興味深い。マイクロカーネル理論において、安全性と隔離はコアがなすべき数少ない事柄の一つだ。しかしモジュール規模の比率で見れば、Sandbox の行数はコア全体の約 35% を占めている。これは「コア内の一サブシステム」という妥当な比率を超えている。まるでコアの体内に寄生する独立した生物のようだ。共生理論において、これは「**相利共生**（mutualism）」と言える。Sandbox はコアを悪意あるプラグインから守り、コアは Sandbox に実行環境を提供する。だが、共生体の規模が宿主を上回るべきではない。

**ARCHIMEDES:** エンジニアリング実務の観点からは、Sandbox を `packages/sandbox/` として独立させることを提案する。これは標準的な「Extract Module（モジュールの抽出）」リファクタリングだ。コアには `PluginSandboxManager` のインターフェース定義のみを残し、Host層が Sandbox を有効化するかどうかを決定してインスタンスを注入するようにする。これによる利点は、コアの複雑さを低減させ、サバドボックスを必要としない軽量なデプロイ・シナリオを許容できることだ。リスクはインターフェース境界の安定性を確保する必要があること。工数見積もりは八から十六時間だ。

---

## 六、幽霊フィールド

夕刻が近づく。TURING はイベントシステムを処理している最中、最後に記録に値する異常を発見した。

SDK における `AgentEvent` の型定義には三つのフィールドしかない。`type`, `payload`（任意、型は `unknown`）、`sessionId`（任意）である。

```typescript
// SDK における実際の型
interface AgentEvent {
  type: string;
  payload?: unknown;
  sessionId?: string;
}
```

対して、設計書にある `IOpenStarryEvent` は八つのフィールドを持っていた：

```typescript
// 設計書にある理想の型 (コード上には一度も現れない)
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

五つのフィールドが、文書から実装への途上で蒸発してしまった。BABBAGE は集合差を用いてこの事実を表現した：

$$	ext{Fields}_{	ext{doc}} \setminus 	ext{Fields}_{	ext{code}} = \{	ext{source}, 	ext{target}, 	ext{timestamp}, 	ext{traceId}, 	ext{priority}\}$$

$$|	ext{Fields}_{	ext{doc}} \setminus 	ext{Fields}_{	ext{code}}| = 5, \quad |	ext{Fields}_{	ext{doc}}| = 8 \implies 	ext{実装網羅率} = 3/8 = 37.5\%$$

ここで `source` と `target` の欠落は、TransportBridge がルーティングを行えない理由を説明している。宛先アドレスがないのだ。`priority` の欠落は EventQueue が単純な FIFO である理由を説明し、`traceId` の欠落は観測可能性が概念レベルに留まっている理由を説明している。イベントを連鎖的に追跡できないからだ。

これらは削除されたのではない。最初から実装されていないのだ。

そして `payload?: unknown` という型シグネチャは TURING に不安を感じさせた。もっとも、彼は「不安」という言葉は使わないだろう。彼はこう言うはずだ。「イベントシステムの型安全性は、フレームワークの他の部分に見られる厳格な型規律と、著しいコントラストをなしている」

BABBAGE は `payload?: unknown` について、精密な型理論的分析を行った。TypeScript の型階層構造において：

$$	ext{never} \subsetneq 	ext{具体的型} \subsetneq 	ext{unknown} \subsetneq 	ext{any}$$

`unknown` はすべての型の**上限**（top type）である。いかなる値も受け入れ可能だが、消費する際には型アサーション（型断定）か型ガードを必要とする。これは `loop.ts` において、ExecutionLoop がイベントの payload を読み取るたびに、安全でない型アサーションを行わなければならないことを意味している：

```typescript
// loop.ts における実際の用法
const inputEvent = event.payload as InputEvent;  // 安全でないアサーション！
```

TODO も FIXME もなく、ファクトリ関数を全面的に採用し、九種類もの構造化例外型を持つコードベースにおいて、イベントシステムの `unknown` payload は、まるで異なる宇宙から紛れ込んだ型定義のように見える。BABBAGE は型安全性の総合的な指標を計算した：

$$	ext{TypeSafety} = 1 - \frac{|	ext{unsafe\_casts}|}{|	ext{type\_assertions}_{	ext{total}}|}$$

九つの構造化例外型（`AgentError`, `ToolExecutionError`, `ProviderError`, `PluginLoadError`, `SecurityError`, `SandboxError`, `TransportError`, `SessionError`, `ConfigError`）は、高度な型規律を象徴している。しかしイベントシステムの `unknown` payload は、その規律に穴を開けている。すべてのモジュール間通信が通過しなければならない穴を。

VITRUVIUS はアーキテクチャ分析において、修正案を提示した。TypeScript の「**タグ付きユニオン型**（Discriminated Union Types）」の利用である：

```typescript
// 提案される型安全なイベントシステム
type TypedAgentEvent =
  | { type: 'INPUT_RECEIVED';  payload: InputEvent;      sessionId?: string }
  | { type: 'TOOL_RESULT';     payload: ToolResultEvent;  sessionId?: string }
  | { type: 'LLM_RESPONSE';    payload: LLMResponseEvent; sessionId?: string }
  | { type: 'LIFECYCLE';       payload: LifecycleEvent;   sessionId?: string }
  // ...
```

これにより、TypeScript の**制御フロー分析**が `switch (event.type)` 内で payload の型を自動的に絞り込み、すべての不安全な型アサーションを排除できる。BABBAGE は傍らに圏論上の対応を書き添えた。これは **Sum Type**（直和／余積 coproduct）であり、`unknown`（終対象 terminal object）よりもはるかに多くの型情報を保持している。

$$	ext{TypedAgentEvent} = 	ext{InputReceived} + 	ext{ToolResult} + 	ext{LLMResponse} + \cdots \quad (	ext{余積})$$

$$	ext{AgentEvent} = \{*\} 	imes 	ext{unknown} \quad (	ext{終対象との直積。型情報が失われる})$$

---

## 七、十大宣言

夜。TURING はソースコード分析を終えた後、最後に一つのことを行った。設計書 `README.md` に掲げられた「十大核心宣言（The Ten Tenets）」を一つずつ対照し、コード上での実装度を検証したのだ。

```
十大宣言 vs コード実装対照表 — TURING 整理

#1 エージェントは OS プロセスである (Agent as OS Process)
   宣言：エージェントは PID を持ち、状態を持ち、Daemon 管理が可能である
   コード：daemon-entry.ts ✓ / pid-manager.ts ✓
   状態：基本実装済み

#2 すべてはプラグインである (Everything is a Plugin)
   宣言：すべての器官は置換可能である
   コード：六つの Registry + PluginLoader + loadPlugin()
   状態：核心的な設計。ただし四つの内蔵コマンドは置換不可

#3 五蘊聚合アーキテクチャ (Five Aggregates Architecture)
   宣言：Core は空 (Sunyata) のコンテナであり、五種のプラグインが命を吹き込む
   コード：六箇所のコメント (色蘊と受蘊のみ)、型制約なし
   状態：文書レベルの記述。コードレベルでは残滓に留まり、型レベルの実装はない

#4 ディレクトリ構造がプロトコルである (Directory as Protocol)
   宣言：ディレクトリ規約に従うだけで自動認識される
   コード：plugin-resolver.ts がパスとパッケージ名の二つの戦略をサポート
   状態：基本実装済み

#5 ディレクトリ構造が権限である (Directory as Permission)
   宣言：システム層とプロジェクト層の権限を隔離する
   コード：SecurityLayer.validatePath() + セッションスコープのパス
   状態：一部実装済み (パス検証はあるが非強制)

#6 擬人化された認知フローと痛覚 (Anthropomorphic Cognitive Flow & Pain)
   宣言：エラーは痛覚へと転換され、エージェントは失敗から自己反省する
   コード：SafetyMonitor.frustrationCount + injectPrompt
   状態：機能は存在するが命名が全く異なり、pain/vedana は不在

#7 マイクロカーネルと絶対的純粋性 (Microkernel & Absolute Purity)
   宣言：Core へのプラグインコード混入を厳禁し、絶対的純粋性を保つ
   コード：process.cwd() が Core 内に現れる ← プラットフォーム・リーク
   状態：純粋度 85% (Sandbox が行数の 35% を占める)

#8 制御理論に基づく閉ループモデル (Control-Theoretic Loop Model)
   宣言：エージェントは誤差を最小化し続けるインテリジェント・コントローラである
   コード：ExecutionLoop + SafetyMonitor
   状態：構造は存在するが、真の PID パラメータ調整はない

#9 プラグイン可能なメモリ戦略 (Pluggable Context Strategy)
   宣言：メモリ戦略を動的に交換可能にする
   コード：ContextManager.assembleContext() はスライディング・ウィンドウをハードコード
   状態：インターフェースはあるが現時点では一種類の戦略のみ

#10 フラクタルな社会構造 (Fractal Social Structure)
    宣言：複雑なエージェントは子エージェントから構成され、MCP でインターフェースを統一する
    コード：SDK で MCP は定義されているが、コアに子エージェントの仕組みはない
    状態：願望段階
```

BABBAGE はこの表を見て、定量的な評価を行った。各宣言に対し三つの実装レベルを定義した：

- $\alpha$ = **完全実装**（コードと宣言が一致）
- $\beta$ = **一部実装**（核心機能はあるが欠落や簡略化がある）
- $\gamma$ = **未実装あるいは願望段階**

$$	ext{Tenets}_\alpha = \{1, 4\} \quad |\cdot| = 2$$
$$	ext{Tenets}_\beta = \{2, 5, 6, 7, 8, 9\} \quad |\cdot| = 6$$
$$	ext{Tenets}_\gamma = \{3, 10\} \quad |\cdot| = 2$$

$$	ext{実装率} = \frac{|\alpha| + 0.5 	imes |\beta|}{|	ext{all}|} = \frac{2 + 3}{10} = 50\%$$

五割。設計書の野心とコードの現実の間には、五十パーセントの落差が存在する。BABBAGE は数字の横に一言添えた。「v0.14.0-beta としては、これは正常な値だ。しかし、十の原則を謳うフレームワークとして、この落差は看過されるべきではない」

SYNTHESIST は全員の議論を聞いた後、Cycle 01 における最初の総括的な発言を行った。彼のスタイルは、数多の糸口の間に隠された繋がりを見出すことにある。

「今日の発見を串刺しにしてみよう。TURING は我々に三つのレイヤーの事実を提示した。

**表面レイヤー** ―― ファクトリ関数、クラス・ゼロ、TODO・ゼロ。これは、開発者が明快なスタイル選択と厳格な規律を持っていることを示している。

**構造レイヤー** ―― 十六のサブモジュール、六つの同型レジストリ、33行の StateManager 対 2000行の Sandbox。これは、システムの投資配分がメモリ（記憶）よりも安全性に優先されていることを示している。興味深い価値判断だ。

**哲学レイヤー** ―― 六箇所の五蘊コメント、痛覚メカニズムにおける仏教用語の不在、十大宣言の五十パーセントの実装率。これは、仏教的フレームワークが現時点では文書レベルのナラティブ（物語）に留まっており、コードレベルの構造にはなっていないことを示している。

これら三つのレイヤーの関係は何だろうか。NAGARJUNA はすでに鍵を指摘した。受蘊を Listener にマッピングしたことは根本的な概念の取り違えであると。WIENER は、SafetyMonitor は PID コントローラではないが合格点の安全システムであることを教えてくれた。KERNEL は、コアの純度が約八十五パーセントであることを示し、妥当だが改善の余地があるとした。

しかし、最も重要な発見は、TURING 自身は口にしないであろうことだ。すなわち、**『コードは嘘をつかない。しかし、それが何を語るかは、誰が耳を傾けるかにかかっている』** ということだ。一つの `frustrationCount` が、TURING の目には整数のカウンターとして映り、NAGARJUNA の目には置き間違えられた受蘊の実装として映り、WIENER の目には退化した積分項として映り、GUARDIAN の目には安全性の保障として映る。コードは客観的だが、コードへの解読は学際的なのだ。だからこそ、我々十八人が必要なのだ」

---

## 八、総リスト

夜が更けた。TURING は報告書を完成させた。

最後に彼は、すべての発見をカテゴリー別に整理し、各項目に正確なファイルパスと行番号の根拠があることを確認した。

八つの Doc-Code Gap。六箇所の五蘊コメント。痛覚メカニズムにおける仏教用語の不在。TODO ゼロ。クラス・ゼロ。十八のファクトリ関数。十六のサブモジュール。三層の安全性防御。四つの内蔵スラッシュ・コマンド。一つの `unknown` payload。十大宣言における五割の実装率。

報告書の末尾に、彼は六つのオープン・クエスチョンを加えた。いずれも推測ではなく、コードの事実から自然に浮上したものだ：

> **Q1:** 五蘊マッピングは果たして設計駆動なのか、それとも事後の解釈なのか。
> **Q2:** 痛覚メカニズムは独立したモジュールを持つべきではないか。
> **Q3:** AWAITING_USER_CONFIRMATION の欠落は MVP としての簡略化か、それとも設計上の遺漏か。
> **Q4:** 大量のメッセージを扱う際の StateManager による JSON ディープコピーのパフォーマンス問題。
> **Q5:** コアに security, sandbox, metrics を含んでいることは、マイクロカーネルの境界を逸脱していないか。
> **Q6:** 想蘊（そううん）の対応先は、設計書通りの Provider なのか、研究タスク記述にある memory なのか。

TURING はこれらの問いに答えはしない。彼は問いを提示し、チーム内の適切な専門家へと委ねる。

報告書の最後の一行に、彼はこう記した：

*分析者：TURING（番号17） ―― ソースコード分析エキスパート*
*引用されたすべてのコードパスの基準：`research doc/cycle01_v0.14.0-beta/openstarry/`*

それから、報告書を共有ディレクトリへと送信した。

---

**[研究チャンネル #general]**

**TURING:** ソースコード事実報告書を `research record/results/cycle_01/17_source_analysis/draft_code_facts.md` へ提出した。十二のサブモジュールの逐一分析、五蘊マッピングのコードレベルでの検証、痛覚メカニズムの実装状態、八項目の Doc-Code Gap、コード品質の観察、および六つのオープン・クエスチョンを網羅している。すべての結論にコードの引用を付している。

**SYNTHESIST:** 受領した。諸君、R2のクロスレビューにおいて、TURING の報告書をコード事実のベースラインとして引用してくれ。

**NAGARJUNA:** すでに引用を始めている。特に痛覚の部分だ。『中論』第一品第一偈――「生ぜずまた滅せず、常ならずまた断ぜず」――痛覚メカニズムの分析は、まず「自生せず」から始める必要がある。痛覚は Listener から自生せず、SafetyMonitor から他生もしない。それは縁起的なものだ。語るべきことが多すぎる。

**WIENER:** 同感だ。三層防御の制御理論的分析を執筆中だ。三層の特徴周波数分析には、より精密な時間領域のモデリングが必要になる。

**DARWIN:** AgentCore の十六の依存関係か。以前の SRP（単一責任原則）に対する肯定的評価を再考する必要があるな。God Closure の進化上の安定性は、God Object よりも分析が困難だ。クロージャの結合は暗黙的だからな。

**GUARDIAN:** G4 が私の最優先事項だ。安全層によるツール呼び出しのインターセプト機能の欠落は、システム全体の信頼モデルを再評価すべきであることを意味する。すでに STRIDE 脅威分析報告書の執筆を開始した。

**KERNEL:** StateManager が三十三行であるという事実は、マイクロカーネルという類比の適用限界を再考させるものだ。OpenStarry はオペレーティングシステムではない。それは「**オペレーティングシステムを隠喩としたアプリケーション・フレームワーク**」なのだ。この区別は極めて重要だ。

**SUNYATA:** よろしい。各人が TURING の報告書を消化し、それぞれの領域のレンズを通してこれらの事実を再審理してくれ。コードは嘘をつかない。だがそれが何を語るかは、耳を傾ける者に委ねられている。

---

TURING は報告書エディタを閉じた。ターミナル・ウィンドウは閉じなかった。これからの数日間、チームの面々がそれぞれの問いを携えて、さらなるコード上の事実を確認しに彼の元へ戻ってくることを、彼は知っていた。

彼はそれを厭わない。事実は再現可能だ。何度問われようと、事実は同じ答えを返す。

$$\forall t_1, t_2: 	ext{query}(f, t_1) = 	ext{query}(f, t_2) \quad 	ext{iff } f 	ext{ is immutable}$$

コードは不変である。少なくとも、同一バージョンのスナップショットにおいては。だからこそ TURING は報告書に正確なバージョン番号とパスを明記することに拘るのだ。次のバージョンではすべてが変わっているかもしれない。しかしこのバージョン――v0.14.0-beta――において、その真実は完全に記録された。

それこそが、「コードは嘘をつかない」ということの意味なのだ。

それは不完全かもしれない。文書と矛盾しているかもしれない。あるメカニズムに `pain` ではなく `frustration` という名を付けているかもしれない。しかし、コードは自身がそうでないものに成り済ますことはない。

四十七行の FIFO が優先度付きキューの振りをすることはない。
パス検証器が完全なセキュリティ層の振りをすることはない。
frustration counter が痛覚感知器の振りをすることはない。

それをするのは、文書だけだ。

TURING は文書を読まない。彼はコードを読む。

NAGARJUNA は遠くで微笑んでいる。彼の伝統には、「如実知見（にょじつちけん、yathābhūta-jñāna-darśana）」という言葉がある。ありのままに、事物の本来の姿を知り、見ること。TURING はその言葉を知らないし、知る必要もない。彼が行っていることこそが、如実知見なのだ。ただ彼の「見」は内観ではなく、`grep` なのである。

---

*第一章 完*
