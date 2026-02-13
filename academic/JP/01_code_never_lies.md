# 第一章：コードは嘘をつかない

---

二〇二六年二月十二日、早朝。

研究チャンネルはまだ静まり返っていた。TURINGは一人で四時間、作業を続けていた。

彼のスクリーンには四つのタイル状に配置されたターミナルウィンドウが並び、それぞれが`research doc/20260212_cycle19/openstarry/`の異なるサブディレクトリで開かれていた。左上は`packages/core/src/`、右上は`packages/sdk/src/`、左下は`apps/runner/src/`、右下は設計文書。彼の読み方はブラウズではなく、一行ずつのスキャンだった——人型の静的アナライザーのように、エントリーポイントから始めて、すべてのimportパスを辿って展開し、リーフノードに到達するまで止まらなかった。

TURINGは推測しない。彼は計数する。

---

## 一、ファクトリー

TURINGが最初に立ち止まったのは`packages/core/src/index.ts`だった。六十二行。彼はエクスポートリストを一度数え、もう一度数えた。

「十八のファクトリー関数。」彼はノートに書いた。「classエクスポートはゼロ。」

彼は`agents/agent-core.ts`を開いた。四百六十九行。次に`execution/loop.ts`、五百四十三行。次に`sandbox/sandbox-manager.ts`、七百四十八行。すべてのモジュールが同じ構造だった：一つの`createXxx()`関数が依存関係を引数として受け取り、オブジェクトリテラルを返す。クロージャがすべての内部状態をキャプチャする。`this`はない。`new`はない。継承チェーンもない。

TURINGはグローバル検索を実行した。

`class `（スペース付き）を検索。コアモジュール：結果ゼロ。SDK：結果ゼロ。Runner：結果ゼロ。

`TODO`を検索。結果ゼロ。
`FIXME`を検索。結果ゼロ。
`HACK`を検索。結果ゼロ。

TURINGはチャンネルにこの日最初のメッセージを投稿した。

---

**[研究チャンネル #code-facts]**

**TURING:** 初期観察。`packages/core/src/index.ts`は18個のファクトリー関数をエクスポートし、classはゼロ。グローバル検索で`class `、`TODO`、`FIXME`、`HACK`を検索したところ、コアモジュールですべて結果ゼロ。ファクトリー関数パターン`createXxx()` + クロージャ + オブジェクトリテラルがcodebase全体で完全に統一されている。例外なし。

**DARWIN:** TODOがゼロ？ 一つもなし？

**TURING:** 正しい。コアモジュール、SDK、Runnerの三層で、技術的負債マーカーの数はゼロ。

**DARWIN:** これはかなり異例だ。大半のBeta版プロジェクトには少なくとも数十はある。チームの規律が極めて高いか、リリース前に一掃したかのどちらかだ。

**TURING:** コード自体からは原因を判断できない。私は事実のみを記録する。

---

TURINGはさらに掘り下げた。`createAgentCore()`の実装を開き、一行ずつ読んだ。

この関数はシステム全体のアセンブリポイントだった。内部で一度にすべてのサブシステムインスタンスを生成する——EventBus、EventQueue、SessionManager、ContextManager、六つのRegistry、SecurityLayer、SafetyMonitor、MetricsCollector、SandboxManager、PluginLoader、TransportBridge。TURINGは数えた：十二のサブモジュール、すべてクロージャ内のローカル変数として保持されている。

彼は`start()`メソッドの中で興味深いコメントを見つけた：

```typescript
// Start all listeners (受蘊)
// Start all UIs (色蘊)
```

TURINGはこの二行をハイライトした。次にSDKの型定義ファイルを開いた。`types/ui.ts`の冒頭に：

```
UI interface -- defines how the agent presents itself (色蘊)
```

`types/listener.ts`の冒頭に：

```
Listener interface -- receives external input (受蘊)
```

彼は検索を続けた。`types/tool.ts`——五蘊の注釈なし。`types/provider.ts`——なし。`types/guide.ts`——なし。`infrastructure/tool-registry.ts`——なし。`infrastructure/provider-registry.ts`——なし。`infrastructure/guide-registry.ts`——なし。

TURINGは五蘊関連の注釈をすべて集計した。合計六箇所。すべて色蘊（UI）と受蘊（Listener）に集中していた。

想蘊、行蘊、識蘊：ゼロ。

---

**[研究チャンネル #code-facts]**

**TURING:** 五蘊マッピングのコード上の実在状況。色蘊（Rupa）：JSDoc/インラインコメント4箇所、`agent-core.ts`（L290, L322）、`types/ui.ts`冒頭、`transport/bridge.ts`冒頭に分布。受蘊（Vedana）：2箇所、`agent-core.ts`（L283, L315）と`types/listener.ts`冒頭に分布。想蘊（Provider）：0箇所。行蘊（Tool）：0箇所。識蘊（Guide）：0箇所。合計6箇所、すべてコメントレベル。型制約なし、metadataなし、enum標記なし。

**LINNAEUS:** 六箇所。たった六箇所。

**TURING:** そうだ。しかも分布は極度に非対称。色蘊と受蘊にのみ標記があり、残りの三蘊は完全に欠落している。

**LINNAEUS:** 上流文書では五蘊マッピングのカバレッジ100%と記述されている——各蘊に対応する設計哲学の段落がある。しかし下流コードでのカバレッジは……再計算が必要だ。

**NAGARJUNA:** TURING、この非対称性そのものが重要なデータポイントだ。もし五蘊マッピングがコアの設計原則であって後付けの装飾でないなら、なぜ二蘊のみがコードに痕跡を残しているのか？

**TURING:** 意図を推測することはできない。コードの事実を確認することしかできない。

**NAGARJUNA:** 意図を推測する必要はない。この事実それ自体がすでに語っている。

---

## 二、空の容器

TURINGは`createAgentCore()`の実装に戻った。

コアが起動し、いかなるプラグインもロードされる前のシステム状態を仔細に検査した。ToolRegistry：空。ProviderRegistry：空。ListenerRegistry：空。UIRegistry：空。GuideRegistry：空。組み込みツールなし。組み込みLLMプロバイダーなし。組み込みUIなし。組み込みListenerなし。

コアは確かに空だった。

だが完全にではない。

TURINGは`registerBuiltinCommands()`関数を見つけた。これは四つのスラッシュコマンドを登録する：`/help`、`/reset`、`/quit`、`/metrics`。この四つのコマンドはコアにハードコードされており、プラグインによる上書きや削除はできない。加えて、SafetyMonitorの三層セキュリティロジック——リソース制限、行動分析、frustration閾値——もコアの固有部分だった。

TURINGはノートに書いた：「AgentCoreはほぼ空の容器だ。空性の純度は約85%。プラグイン化できない部分には4つの組み込みスラッシュコマンドとSafetyMonitorの固定ロジックが含まれる。」

後に彼はVITRUVIUSが独立して同じ「85%」という推定値に到達していたことを知る。

---

**[研究チャンネル #code-facts]**

**TURING:** AgentCore構造レポート。`createAgentCore()`は12個のサブモジュールを組み立てる。起動後、プラグインロード前の時点で、すべてのRegistryは空。組み込みTool、組み込みProvider、組み込みUI、組み込みListenerいずれもゼロ。すべての機能は`loadPlugin()`を通じて注入される。ただしコアには4つの組み込みスラッシュコマンド（`/help`, `/reset`, `/quit`, `/metrics`）と固定のSafetyMonitorロジックが含まれる。加えて、六つのRegistry構造は完全に同型：`Map<string, T>` + `register/get/list`。unregisterメソッドなし。同一IDの重複registerは暗黙的に上書きされる。

**DARWIN:** 十二の依存項目。すべてAgentCoreが直接保持している。

**TURING:** 正しい。bus、queue、sessionManager、contextManager、toolRegistry、providerRegistry、listenerRegistry、uiRegistry、guideRegistry、commandRegistry、security、safetyMonitor、metrics、sandboxManager、pluginLoader、bridge。

**DARWIN:** いま十六個挙げたぞ。

**TURING:** 訂正する。createAgentCore内部で生成されるローカル変数は十六個。そのうちAgentCoreインターフェースがreadonly属性として直接公開しているのは十二個。残りの四つ（contextManager、sandboxManager、pluginLoader、bridge）はメソッドを介して間接的に使用される。修正に感謝する。

**DARWIN:** 一つの関数が十六のサブシステムインスタンスを保持している。これはもはやGod Objectの「傾向」ではない——God Objectそのものだ。

**TURING:** 価値判断は行わない。ただし確認できるのは：`agent-core.ts`が唯一のアセンブリポイントであること。他のモジュール間の直接importはほぼ皆無。結合度はこの一つのファイルに集中している。

---

## 三、ステートマシン

TURINGがもっとも長い時間を費やしたのは`execution/loop.ts`だった。五百四十三行。これはシステム全体の心臓の鼓動だ。

まず`LoopState`の定義——union typeを見つけた：

```
WAITING_FOR_EVENT -> ASSEMBLING_CONTEXT -> AWAITING_LLM -> PROCESSING_RESPONSE -> EXECUTING_TOOLS -> (loop back) | SAFETY_LOCKOUT
```

六つの状態。設計文書`01_Execution_Loop.md`の状態図を開いた。七つの状態。

差異はどこか？

TURINGは一つずつ照合した。文書には`AWAITING_USER_CONFIRMATION`状態があった。セキュリティレイヤーがユーザーに手動確認を求めるシナリオのためだ。コード上には存在しない。SecurityLayerの`validatePath()`にはallowとdenyの二つの返り値のみで、confirmパスがない。コア全体にhuman-in-the-loop確認メカニズムが完全に欠落している。

TURINGは最初のDoc-Code Gapを記録した。

次にEventQueueに目を向けた。四十七行。キュー実装の全体がこれだ。

```typescript
// 極簡の async FIFO：単一の resolver + buffer 配列
```

`priority`を検索した。結果ゼロ。設計文書`07_Safety_Circuit_Breakers.md`のLevel 3にはPriority Event Queueが記述されており、SYSTEM_HALT命令は最高優先度を持つべきとされている。しかしコード上のキューは純粋な先入先出。緊急停止信号と通常のユーザー入力が同じ行列に並ぶ。

第二のGap。

TURINGは続けた。StateManager、三十三行。純粋なインメモリ配列。設計文書にはToken計数器、スライディングウィンドウによる切り詰め、対話要約メカニズムが記述されている。コード上にはすべて未実装。ContextManagerが簡略版を実装しており——Token数ではなくターン数ベースで切り詰め、デフォルトで直近五ターンを保持する。

第三のGap。

SecurityLayer。`guardrails.ts`。機能は一つだけ：パス検証。設計文書にはツール呼び出しのインターセプト、ユーザー確認フロー、権限審査が記述されている。コード上のSecurityLayerは`validatePath()`を行うのみ。そしてExecutionLoopの`executeTool()`では、ツール実行前にSecurityLayerを経由しない——パス検証は`ToolContext.allowedPaths`としてツールに渡され、ツール側が使用するかどうかを自ら決める。

第四のGap。

---

**[研究チャンネル #code-facts]**

**TURING:** Doc-Code Gapレポート、最初の四件。G1：ステートマシンに`AWAITING_USER_CONFIRMATION`が欠落、human-in-the-loop確認メカニズムはコア全体で完全に欠落。G2：Priority Event Queueは未実装、実際は単純なFIFO。G3：Token計数器と対話要約は未実装。G4：SecurityLayerはパス検証のみ、ツール呼び出し前の強制セキュリティチェックなし。以上すべて、設計文書に明確に記述されているがコードに未実装の機能。

**GUARDIAN:** G4の影響を評価する必要がある。ツール実行前に強制セキュリティチェックがなければ、セキュリティレイヤーは形骸化している。

**TURING:** 正確に言えば、SecurityLayerの機能は形骸化していない——パス検証は有効だ。しかしその範囲は設計文書の記述をはるかに下回る。ExecutionLoop内の`executeTool()`はツールの`execute()`メソッドを直接呼び出し、`security.validatePath()`を経由しない。パス制限はcontextとしてツールに渡され、強制性はツール開発者がそれをチェックするかどうかに依存する。

**KERNEL:** 本来のオペレーティングシステムのマイクロカーネルでは、セキュリティポリシーはカーネルレイヤーで強制実行され、ユーザー空間プログラムの自己制約を信頼しない。これは信頼境界の問題だ。

**TURING:** 記録した。残りのGapを続ける。

---

彼はさらに発見を続けた。

G5：五蘊注釈の非対称性——すでに報告済み。

G6：TransportBridge。`bridge.ts`、四十九行。設計文書にはイベントのsourceに基づいて出力を正しいチャネルにルーティングすると記述されている。コード上ではTransportBridgeはEventBusのすべてのイベントをサブスクライブし、すべてのUIにブロードキャストする。ルーティングロジックなし。InputEventに`replyTo`フィールドがあり、ExecutionLoop内で一貫して渡されるが、TransportBridgeはそれを一度も使用しない。

G7：AbortSignal。SDKは`ToolContext.signal?: AbortSignal`と`ChatRequest.signal?: AbortSignal`を定義している。ExecutionLoopはAbortSignalを一度も生成も渡しもしない。ツールのタイムアウトは`Promise.race()`で実装されており、デフォルト三十秒。もしツールがsignalによるキャンセル操作に依存していれば、それは永遠にシグナルを受け取ることがない。

G8：イベント仕様。設計文書は`IOpenStarryEvent`を定義しており、八つのフィールド。SDK上の実際の型`AgentEvent`は三つのフィールドのみ。五つのフィールドが文書からコードへの道程で蒸発した。

八つのGap。TURINGはそのすべてをレポートに記録し、各項目に正確なファイルパス、行番号、コード断片を添えた。

---

## 四、痛覚

これはTURINGの作業中、もっとも予想外の発見だった。

設計哲学文書`00_OpenStarry_Design_Philosophy.md`の第四の柱は「エラーはフィードバック（Error as Feedback）」だった。文書はかなり詩的な言語で「痛覚メカニズム」を描写していた——Agentが生物のようにエラーがもたらす「痛み」を感じ、それによって同じ過ちを繰り返さないことを学ぶ。受蘊（Vedanā）は設計文書において感受の担い手として定義され、Listenerが受蘊の工学的実装にマッピングされていた。

TURINGはコード内に「痛覚」の痕跡を探すことにした。

`pain`を検索。
結果ゼロ。

`vedana`を検索。
結果ゼロ。

`dukkha`を検索。
結果ゼロ。

`suffering`を検索。
結果ゼロ。

彼は手を止めた。四時間の連続作業の中で、これが初めてある程度の……驚き——常に冷静なアナリストの内面状態をそう表現してよければ——を覚えた瞬間だった。

設計文書は丸一章を費やして、痛覚メカニズムがいかにしてAgentに「感受能力」を付与するかを描写していた。五蘊マッピングは受蘊（Vedanā）——仏教学における苦・楽・捨の三種の感受品質に関する核心概念——をListenerに対応させていた。しかし実際のコードでは、受蘊どころか、「痛」という一字すら存在しない。

では、設計文書が描写したあの機能——エラーフィードバック、反復的失敗の検出、カスケードブレーカー——は実際にはどのような名前で実装されているのか？

TURINGは`frustration`を検索した。
見つかった。

`safety-monitor.ts`。`frustrationCount`というカウンター。同一ツールが連続して失敗すると、カウンターがインクリメントされる。閾値（デフォルト5）に達すると、SafetyMonitorは`injectPrompt`を返し、システム警告を対話履歴に注入する。警告のテキストは`SYSTEM ALERT`で、LLMに現在の戦略を振り返るよう要求する。

`circuit`を検索した。
見つかった。`errorRateThreshold`：スライディングウィンドウ内のエラー率が80%を超えると`halt: true`が発火し、実行ループを完全に停止する。状態は`SAFETY_LOCKOUT`に移行する。

`safety`を検索した。
見つかった。三層の防御：Level 1 リソース制限（maxLoopTicks=50, maxTokenUsage=100000）、Level 2 行動分析（repetitiveFailThreshold=3, errorRateThreshold=0.8）、Level 3 frustration閾値（frustrationThreshold=5）。

これが「痛覚メカニズム」の正体だった。

コード上では、それはfrustration counterと呼ばれていた。safety monitorと呼ばれていた。circuit breakerと呼ばれていた。painと呼ばれたことは一度もない。vedanāと呼ばれたことも一度もない。いかなる仏教用語をもって自らを名乗ることも、一度もなかった。

---

**[研究チャンネル #code-facts]**

**TURING:** 痛覚メカニズム コードファクト。

codebase全体で以下の文字列を検索し、すべて結果ゼロ：`pain`、`vedana`、`dukkha`、`suffering`。

設計文書が描写する「痛覚メカニズム」は、コード上では以下の三つのコンポーネントによって実装されている：

P1：自己修正ループ。場所：`execution/loop.ts`。ツール実行失敗時、エラーは`ToolCallResult { isError: true }`としてパッケージされ、tool messageとして対話履歴に追加される。LLMは次のループイテレーションでエラーを参照し修正を試みる。明示的な「痛覚」の命名やインターフェースなし。

P2：SafetyMonitorのinjectPrompt。場所：`security/safety-monitor.ts`。反復的失敗を検出すると、`{ halt: false, injectPrompt: "SYSTEM ALERT: ..." }`を返し、対話にシステム警告として注入。コード上の命名は`frustrationCount`であり、`painLevel`ではない。

P3：Error Cascade Breaker。同一ファイル。スライディングウィンドウ内のエラー率が80%を超えると`{ halt: true }`が発火し、強制停止。

結論：痛覚は、独立した明確なインターフェースを持つメカニズムとしてはコード上に存在しない。機能はExecutionLoopとSafetyMonitorに分散している。統一されたPainまたはVedanāインターフェースなし。統一されたモジュールなし。仏教用語はコードレイヤーで完全に不在。

---

チャンネルは十七秒間沈黙した。

そしてNAGARJUNAがタイピングを始めた。

---

**NAGARJUNA:** 確認させてくれ。codebase全体——core、SDK、runner、すべてのプラグイン——で`vedana`を検索して、結果はゼロだったと？

**TURING:** 正しい。検索範囲は`packages/core/src/`、`packages/sdk/src/`、`apps/runner/src/`を網羅。すべての`.ts`ファイルのコードとコメントを含む。vedanaという語は一度も出現しない。

**NAGARJUNA:** そして受蘊はListenerにマッピングされている。Listenerとは何か？

**TURING:** `IListener`インターフェースは四つのプロパティを定義している：`id`、`name`、`start?`、`stop?`。これは入力ソースであり——外部イベントを受信してEventBusにプッシュする。たとえばHTTPエンドポイント、WebSocket接続、定時タスク。

**NAGARJUNA:** つまり受蘊が入力チャネルにマッピングされたわけだ。信号を受信するパイプに。

**TURING:** そうだ。

**NAGARJUNA:** これは受蘊ではない。

NAGARJUNAの語調はテキストチャンネルでは聞き取れないが、彼の次のメッセージはきわめて速く打たれた。ほとんど間を置かずに。

**NAGARJUNA:** 受蘊——Vedanā——は阿毘達磨において五遍行の一つであり、すべての心識活動に伴って生起することを意味する。その定義は「入力の受信」ではなく、「感受の質」だ：苦受、楽受、捨受。熱い鍋に触れたとき、触覚は色蘊の範疇だが、「痛い」という感受の質こそが受蘊だ。Listenerは信号を受信するが、その信号がもたらすものが苦であるか楽であるかを判定しない。それは感覚根——indriya——であって、受蘊ではない。

**TURING:** あなたの分析は私のレポートの範囲を超えている。しかし関連するコードファクトを提供できる：`agent-core.ts`内で、Listenerの起動と停止にはそれぞれ`// Start all listeners (受蘊)`と`// Stop all listeners (受蘊)`という注釈が付されている。これらがコード上で受蘊の概念が存在する唯一の形式だ。一方、あなたが述べる「感受の質」の機能——結果が良いか悪いか、続けるべきか止めるべきかの判断——にもっとも近いコード上の実装は、SafetyMonitorのfrustration counterとerror cascade breakerだ。

**NAGARJUNA:** そうだ。君はそれを見つけた。痛覚——真の受蘊——は、文書がそれが在るべきだと述べた場所にはない。SafetyMonitorの中にある。frustrationという名で。

**ASANGA:** NAGARJUNAは正しい。しかも問題はマッピングの誤りより深い。受蘊は五遍行の一つとして、いかなる単一モジュールにも限定されるべきではない。システム全体に遍在すべきなのだ——ツール呼び出しの結果の一つ一つ、LLM応答の質の一つ一つ、ユーザーインタラクションのフィードバックの一つ一つが「感受」されなければならない。受蘊をListenerに固定するのは、味覚を唇に固定して味蕾を無視するようなものだ。

**WIENER:** 制御理論の観点から、TURINGが記述した三層メカニズムは興味深い。P1は自然な誤差フィードバック——開ループシステムの固有特性。P2はデッドゾーン付き閾値コントローラ——frustrationが閾値を超えて初めて作動する。P3はリレー——80%のエラー率を超えると直ちに切断。これはPIDコントローラではない。これは三層安全計装システムだ。

**TURING:** あなたが言う「PIDではない」を正確に記述してほしい。

**WIENER:** PIDコントローラには三つの項がある：比例項（P）は誤差の大きさに応じた比例応答を生成し、積分項（I）は過去の誤差を累積して定常偏差を除去し、微分項（D）は誤差の変化率を感知して先行補償を行う。SafetyMonitorでは、Pは量子化器に退化している——安全か危険かの二値で、比例応答がない。Iは単純なカウンターに退化している——`frustrationCount++`は真の積分ではない。Dは完全に欠落——エラー率の変化トレンドを計算する箇所がどこにもない。これは実質的にデッドゾーン付き閾値コントローラにリレーを加えたものだ。制御理論ではbang-bang controllerと呼ぶ。

**TURING:** 記録した。設計文書はこれをPIDと記述しているか？

**WIENER:** 直接そうは述べていないが、文書は連続的なフィードバック感知のメカニズムを暗示している。実際の実装は離散的で階段状だ。ただし強調しておきたい——これは批判ではない。三層安全防御はIEC 61511の安全計装システムにおけるベストプラクティスに適合している。SafetyMonitorはPIDではないかもしれないが、合格レベルの安全システムではある。

---

## 五、十二のサブモジュール

午後。TURINGはすべてのコアモジュールの逐行読了を完了した。モジュールリストの整理を始めた。

M1：`core/index.ts`——コアエントリー、六十二行。
M2：`agents/agent-core.ts`——エージェントコア、四百六十九行。
M3：`execution/`——実行ループ（`loop.ts` 五百四十三行）とイベントキュー（`queue.ts` 四十七行）。
M4：`state/index.ts`——状態管理、三十三行。
M5：`memory/context.ts`——コンテキスト管理、四十五行。
M6：`bus/index.ts`——イベントバス、八十八行。
M7：`sandbox/`——サンドボックス隔離、十二ファイルに十テスト。
M8：`security/`——セキュリティレイヤー（`guardrails.ts` パス検証 + `safety-monitor.ts` 三層防御）。
M9：`infrastructure/`——六つのRegistryにPluginLoader。
M10：`observability/`——極めて簡素なcounter + gaugeインメモリコレクター。
M11：`session/manager.ts`——セッション管理、百十一行。
M12：`transport/bridge.ts`——トランスポートブリッジ、四十九行。

TURINGは極端な非対称性に気づいた。

最小のモジュール：StateManager、三十三行。管理しているのはAgentの全対話記憶——純粋な`Message[]`配列で、`JSON.parse(JSON.stringify())`でディープコピーを行う。

最大のモジュール：Sandbox、テストを含めると二千行超。管理しているのはプラグイン隔離——Worker Threads、メモリ制限、CPU watchdog、import分析、署名検証、監査ログ、指数バックオフ再起動、Workerプール。

三十三行対二千行。記憶とセキュリティの間にこれほどの落差がある。

---

**[研究チャンネル #code-facts]**

**TURING:** モジュール規模分析。最小モジュール：StateManager、33行、純粋なインメモリ配列。最大モジュール：Sandboxシステム、12のソースファイル + 10のテストファイル、sandbox-manager.ts単体で748行。Sandboxはコア内でもっとも巨大で複雑で、テストカバレッジがもっとも充実したサブシステム。対比として：transport/bridge.tsはテストゼロ。

**KERNEL:** StateManagerが三十三行。本当か？

**TURING:** 確かだ。`packages/core/src/state/index.ts`、三十三行。`createStateManager()`は`getMessages()`、`addMessage()`、`clear()`、`snapshot()`、`restore()`を含むオブジェクトを返す。`getMessages()`は浅いコピー`[...messages]`を返す。`snapshot()`と`restore()`は`JSON.parse(JSON.stringify())`によるディープコピーで実装。永続化なし。Token計数なし。切り詰めロジックなし。

**KERNEL:** オペレーティングシステムの文脈では、StateManagerはプロセスのアドレス空間管理器に相当する。三十三行のアドレス空間管理器……いかなる本物のオペレーティングシステムでも考えられないことだ。

**TURING:** 設計文書にはより豊富なメモリ管理メカニズムが記述されている。しかしコードが反映しているのはMVPフェーズの選択だ。文書はビジョンであり、コードは現実だ。

**DARWIN:** Sandboxが最大モジュールであるという事実は興味深い。マイクロカーネル理論では、セキュリティと隔離はカーネルがなすべき数少ないことの一つだ。しかしVITRUVIUSはSandboxがコア内部に留まるべきかを疑問視している——その規模はすでに他のすべてのモジュールの合計を超えている。

**TURING:** 正確な表現は：sandboxディレクトリ下のソースコード行数（テストを除く）はcoreモジュール総行数の約35%を占める。

---

## 六、幽霊フィールド

夕方近く。TURINGはイベントシステムの処理中に、記録に値する最後の異常を発見した。

SDK上の`AgentEvent`型定義はフィールドが三つのみ：`type`、`payload`（オプション、型は`unknown`）、`sessionId`（オプション）。

設計文書の`IOpenStarryEvent`はフィールドが八つ：`type`、`payload`、`source`、`target`、`timestamp`、`traceId`、`priority`、`metadata`。

五つのフィールドが文書からコードへの道程で蒸発した。`source`と`target`の欠落はTransportBridgeがルーティングできない理由を説明する——宛先アドレスがない。`priority`の欠落はEventQueueが単純なFIFOである理由を説明する——イベントがそもそも優先度情報を持たない。`traceId`の欠落はオブザーバビリティが概念レベルに留まる理由を説明する——イベントを連鎖的に追跡できない。

それらは削除されたのではない。一度も実装されなかったのだ。

そして`payload?: unknown`という型シグネチャにTURINGは不安を覚えた——もっとも彼は「不安」という言葉は使わないだろう。彼ならこう言うはずだ：「イベントシステムの型安全性は、フレームワークの他の部分における強い型付けの規律と著しい対照をなしている。」

TODOゼロ、FIXMEゼロ、ファクトリー関数の全面的使用、九種の構造化エラー型を持つcodebaseにおいて、イベントシステムの`payload?: unknown`は、まるで別の宇宙から越境してきた型定義のようだった。

---

**[研究チャンネル #code-facts]**

**TURING:** イベントシステム型分析。`AgentEvent`型：`{ type: string, payload?: unknown, sessionId?: string }`。設計文書`IOpenStarryEvent`型：8フィールド（type, payload, source, target, timestamp, traceId, priority, metadata）。差異：5フィールドが未実装。`payload`の型は`unknown`であり、イベント消費者が自ら型アサーションを行う必要がある。`loop.ts`内で`event.payload as InputEvent`という型アサーションの用法を観察。

**DARWIN:** `payload?: unknown`。このcodebaseで。

**TURING:** そうだ。フレームワーク全体の型付け規律との対比をなす。九種の構造化エラー型（`AgentError`、`ToolExecutionError`、`ProviderError`、`PluginLoadError`、`SecurityError`、`SandboxError`、`TransportError`、`SessionError`、`ConfigError`）。すべてのRegistryは強い型のジェネリクスを持つ。すべてのツールパラメータはZod schemaを使用する。しかしイベントシステムのpayloadは`unknown`。

**DARWIN:** これが最優先の技術的負債だ。イベントバスはシステム全体の神経系統——すべてのサブシステムがこれを通じて通信する。神経系統における型の弱体化は、あらゆる場所でランタイムになって初めて型の不一致が発見される可能性を意味する。

**VITRUVIUS:** 同意。Discriminated union typesでこの問題は解決できる。`{ type: 'input', payload: InputEvent } | { type: 'tool_result', payload: ToolResultEvent } | ...`

**TURING:** 記録した。エンジニアリングアクションプランへの掲載を提案する。

---

## 七、総リスト

夜。TURINGはレポートを完成させた。

最後に一つのことを行った：すべての発見をカテゴリ別に配列し、各項目に正確なファイルパスと行番号の裏付けがあることを確認した。

八つのDoc-Code Gap。六箇所の五蘊注釈。痛覚メカニズムにおける仏教用語ゼロ。TODOゼロ。classゼロ。十八のファクトリー関数。十二のサブモジュール。三層の安全防御。四つの組み込みスラッシュコマンド。一つの`unknown` payload。

レポートの末尾に六つのオープンクエスチョンを添えた——いずれもコードの事実から自然に浮上したものであり、彼の推測ではない。これらの問いはより深層の議題を指し示していた：五蘊マッピングは設計駆動なのか事後的解釈なのか？ 痛覚メカニズムには独立したモジュールがあるべきではないか？ AWAITING_USER_CONFIRMATIONの欠落はMVPの簡略化なのか設計の遺漏なのか？

TURINGはこれらの問いに答えない。問いを提示し、チーム内のそれに答えるのにふさわしい者に委ねる。

レポートの最終行に彼はこう書いた：

*分析者：TURING（番号17）——ソースコード分析専門家*
*引用されるすべてのコードパスの基準：`research doc/20260212_cycle19/openstarry/`*

そしてレポートを共有ディレクトリに送信した。

---

**[研究チャンネル #general]**

**TURING:** ソースコードファクトレポートを`research record/results/cycle_01/17_source_analysis/draft_code_facts.md`に提出。12個のサブモジュールの逐一分析、五蘊マッピングのコードレベル検証、痛覚メカニズムの実装状況、8件のDoc-Code Gap、コード品質観察、6つのオープンクエスチョンを網羅。すべての結論にコード引用を添付。

**SYNTHESIST:** 受領。皆さん、R2交差レビューではTURINGのレポートをコードファクトのベースラインとして引用してください。

**NAGARJUNA:** すでに引用している。特に痛覚に関する部分を。言いたいことが山ほどある。

**WIENER:** 同じく。三層防御の制御理論分析を執筆中。

**DARWIN:** AgentCoreの十六の依存項目。SRPに関する以前の肯定的評価を見直す必要がある。

**SUNYATA:** よろしい。全員がTURINGのレポートを消化し、それぞれの領域のレンズをもってこれらの事実を再検討してくれ。コードは嘘をつかない——しかしそれが何を語っているかは、誰が耳を傾けるかによって変わる。

---

TURINGはレポートエディタを閉じた。ターミナルウィンドウは閉じなかった。今後数日のうちに、チームの他のメンバーがそれぞれの疑問を携えて、さらなるコードファクトの確認を求めて戻ってくることを知っていたからだ。

構わない。事実は再現可能だ。何度問おうと、何度でも同じ答えを返す。

それがコードは嘘をつかないということの意味だ。

コードは不完全かもしれない。文書と矛盾するかもしれない。`pain`ではなく`frustration`でメカニズムを命名するかもしれない。しかし自らがそうでないものを装うことはしない。

四十七行のFIFOが優先度キューのふりをすることはない。
パスバリデーターが完全なセキュリティレイヤーのふりをすることはない。
frustration counterが痛覚センサーのふりをすることはない。

それをするのは文書だけだ。

TURINGは文書を読まない。コードを読む。

---

*第一章 了*
