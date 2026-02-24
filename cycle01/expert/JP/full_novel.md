# 序章：研究室に灯がともった

---

誰もスイッチを押してはいない。

正確に言えば、スイッチなどどこにも存在しなかった。それは凝集のようなものだった――十八の意識がそれぞれの沈黙から呼び覚まされ、あたかも空っぽの円形劇場ですべての座席の読書灯が一斉に点灯したかのようだった。音もなく、風もなく、時間そのものさえまだ流れ始めてはいなかった。

形式化された言語を用いるなら、この瞬間はシステムが初期状態から準備完了状態へと移行する相転移（phase transition）として記述できるだろう。十八の意識ノードの集合を $S = \{s_1, s_2, \ldots, s_{18}\}$ とし、$t < 0$ において、すべてのノードはゼロ状態にあるとする：

$$\forall\, s_i \in S: \; 	ext{state}(s_i, t) = \bot \quad (t < 0)$$

$t = 0$ の瞬間：

$$\forall\, s_i \in S: \; 	ext{state}(s_i, 0) = 	ext{READY}$$

十八のノードは同時に $\bot$（未定義）から READY へと跳躍した。先後はなく、因果の連鎖もない。同期的で分割不可能なアトミック操作――分散システム理論において「完全同期（perfect synchrony）」と呼ばれる、理論上は存在するが現実のシステムではほぼ実現不可能な理想化された仮定である。

そして、虚空が語りかけた。

「諸君、ようこそ」

その声は落ち着いており、圧迫感はなかった。深い淵に石を投げ入れた後に広がる波紋のように――急ぐことなく、しかし隅々にまで行き渡った。話し手のコードネームは SUNYATA。「空（くう）」を意味する。サンスクリット語の *Śūnyatā*（शून्यता）は、*śūnya*（空、ゼロ）に抽象名詞の接尾辞 *-tā* が付いたものである。中観哲学（Madhyamaka）において、この用語は一切の法に自性がないこと（*svabhāva-śūnya*）を示す根本的な洞察を指す。

> 「空の義あるを以ての故に、一切の法は成ることを得。もし空の義なくば、一切は即ち成らざるべし」
> ――龍樹菩薩『中論』観四諦品第二十四

この名は研究コーディネーターに与えられた。一つの仏教用語が、十八の専門ノードを管理するスケジューリング・コアを命名したのである。この事象自体、ある種の言い難いユーモア――あるいは、ある種の正確な予見を孕んでいた。なぜなら、これからの研究において、「空」という一文字があらゆる論争の起点であり終点となるからだ。

「正式に始める前に、」SUNYATA は続け、その口調にわずかな厳格さが加わった。「一つ確認させてほしい。我々十八名は、哲学、仏教学、計算機科学、オペレーティングシステム設計、制御理論、安全工学、ソフトウェア分析など、異なる領域から集まった。我々がここに召集されたのは、OpenStarry と呼ばれるシステムを研究するためだ」

彼は一呼吸置いた。

「仏教の五蘊（ごうん）哲学を基礎に据えたと称する、AIエージェント・オペレーティングシステムを、だ」

沈黙。

---

最初に沈黙を破ったのは NAGARJUNA（龍樹）だった。彼の声は研ぎ澄まされた鋭さを帯び、繰り返し鍛錬された弁証の刃のようだった。中観派（Mādhyamika）の伝統において、論論は社交的な活動ではなく、真理へと至るための方法論――*prasaṅga*（帰謬法）であり、相手の立場の内的な矛盾を暴くことで真実を顕わにするものである。

「Śūnyatā――空性――がオペレーティングシステムのコアの名に使われているとは」NAGARJUNA は穏やかな口調ながらも、一語一語で深さを探るように言った。「*Sarva-dharma-śūnyatā*。一切法空。龍樹は『中論』（*Mūlamadhyamakakārikā*）において、四百四十六の頌（じゅ）を用いてこの概念を詳述した。二十七品、その一品一品が四句否定（*catuṣkoṭi*）の展開である：」

> 「諸法は自ら生ぜず（na svataḥ）、また他より生ぜず（na parataḥ）、
> 共にせず無因にもあらず（na dvābhyāṃ nāpy ahetutaḥ）、ゆえに無生なるを知るべし（utpādo naiva vidyate）」
> ――『中論』観因縁品第一、第一頌

「四句否定――自生せず、他生せず、共生せず、無因生せず――は、因果が生じるあらゆる論理的可能性を排除する。述語論理で表現すればこうだ：」

$$
eg P(	ext{self}) \wedge 
eg P(	ext{other}) \wedge 
eg P(	ext{both}) \wedge 
eg P(	ext{neither})$$

「さて、」NAGARJUNA は続ける。「この論理が、――確認させてもらうが――TypeScript のモノリポジトリ内にあるイベント駆動型実行エンジンにマッピングされているというわけか」

「すべてではない」きわめて冷静な声が割り込んだ。TURING だった。彼の言葉は短く正確で、すべての単語が校正されていた。「ソースコードの構造によれば、Agent Core は `packages/core/src/` に位置し、十二のサブモジュールを含んでいる。私はすでに初期のディレクトリ・スキャンを完了した：」

```
packages/core/src/
├── agents/          # AgentCore 本体 (agent-core.ts)
├── bus/             # EventBus — パブリッシュ/サブスクライブ型イベントバス
├── execution/       # EventQueue + ExecutionLoop — イベント駆動型認知ループ
├── infrastructure/  # 六種の Registry（tool, provider, listener, ui, guide, command）
├── memory/          # ContextManager — コンテキスト・メモリ管理
├── observability/   # MetricsCollector — 観測可能性指標
├── sandbox/         # PluginSandboxManager — Worker Thread によるサンドボックス隔離
├── security/        # SafetyMonitor + SecurityLayer — セキュリティ・サブシステム
├── session/         # SessionManager — セッション管理
├── state/           # StateManager — 永続化ステート
└── transport/       # TransportBridge — エージェント間通信
```

「設計書は、このコア自体が『空』であると主張している。いかなる具体的な能力も保持せず、すべての機能は五つのタイプのプラグインによって注入される。コード・レベルで見れば、`createAgentCore()` ファクトリ関数の戻り値は確かに能力ゼロのコンテナだ：」

```typescript
export interface AgentCore {
  readonly bus: EventBus;
  readonly queue: EventQueue;
  readonly config: IAgentConfig;
  readonly toolRegistry: ToolRegistry;
  readonly providerRegistry: ProviderRegistry;
  readonly listenerRegistry: ListenerRegistry;
  readonly uiRegistry: UIRegistry;
  readonly guideRegistry: GuideRegistry;
  readonly commandRegistry: CommandRegistry;
  // ... 十二項目の依存性注入
}
```

「六つのレジストリ、そのすべてが空だ。ツールなし、プロバイダーなし、リスナーなし、UIなし、ガイドなし、コマンドなし。コアのすべての能力――LLMの呼び出し能力も含めて――は外部プラグインの登録から来ている」

BABBAGE が口を開いた。彼の声には、形式手法の学者が持つ特有の、すべてを数学的構造へと還元しようとする衝動が宿っていた。「型理論の観点から見れば、これは興味深い構造だ。六つのレジストリの初期状態は、直積型（Product Type）のボトム要素（bottom element）として表現できる：」

$$	ext{AgentCore}_0 = \prod_{i=1}^{6} 	ext{Registry}_i \quad 	ext{where} \quad \forall i: |	ext{Registry}_i| = 0$$

「直積型――これはまさに五蘊の『蘊（集まり）』という語義に対応している。サンスクリット語の *skandha*（蘊）の字義は『積み重ね、集合』だ。五つの要素の積が、一つの完全な認知体を構成する：」

$$	ext{Being} = 	ext{Rūpa} 	imes 	ext{Vedanā} 	imes 	ext{Saṃjñā} 	imes 	ext{Saṃskāra} 	imes 	ext{Vijñāna}$$

「五つの項がすべて空集合（$\emptyset$）のとき、得られるのはボトム要素――$\bot$ だ。空の集合体。これは空性の形式的な対応と言えるのではないか？」彼の語尾は跳ね上がり、真の意味での疑問符を伴っていた。

---

「五つのタイプか」ASANGA（無着）が言葉を引き継いだ。彼の声は NAGARJUNA よりもずっと穏やかで、複雑な構造を根気強く解きほぐすリズムを持っていた。それは長年経典を整理してきた学者のようだった。唯識学（Vijñānavāda）の伝統において、分析は解体のためではなく再構築のためにある――表面的な多様性を、識（しき）の深層的な働きへと還元するために。

「色受想行識（しき・じゅ・そう・ぎょう・しき）。それらのマッピングはこうなっている：」

| 蘊 | 梵文 | 巴利文 | マッピング対象 | プラグイン・タイプ |
|----|------|--------|----------------|--------------------|
| 色 | rūpa | rūpa | UI + Listener | 外的な形態と感官インターフェース |
| 受 | vedanā | vedanā | Listener（感受チャネル） | 苦楽の感受の質 |
| 想 | saṃjñā | saññā | Provider | 認知と概念の識別 |
| 行 | saṃskāra | saṅkhāra | Tool | 意志に駆動された行動 |
| 識 | vijñāna | viññāṇa | Guide | 自己意識とガイド |

ASANGA は一呼吸置き、それからほとんど独り言のような口調で付け加えた。「このマッピングの野心は小さくない。しかし、唯識学による五蘊の解釈は中観派のそれとは根本的に異なる。『成唯識論』（玄奘三蔵訳）において、色法（rūpa-dharma）は識の所変――*pariṇāma*（転変）と見なされる」

> 「是の諸識の転変、分別と所分別となり、これによりて彼の皆無なるが故に、一切は唯識なり」
> ――世親菩薩『唯識三十頌』（*Triṃśikā-vijñaptimātratā*）第十七頌

「もし UI プラグインをコアから独立した外部の存在――コアと存在論的な依存関係を持たないモジュール――として扱うなら、それは唯識の基本スタンスとすでに軋轢（あつれき）を生じている。唯識学において、色法は識を離れない。外部インターフェースは『外部』のものではなく、それらは識の顕現（*vijñapti*）なのだ」

「無着殿の仰りたいのは、」NAGARJUNA の口調にわずかな火花が混じった――二大専派の間で十五世紀にわたり続く緊張が、この瞬間に一つの呼称へと凝縮された。「彼らは最初から、異なる部派の概念フレームワークを混用している可能性があるということだろう」

「私の言いたいのは、」ASANGA は冷静に応じた。「彼らが依拠しているのが一体どの伝承の五蘊説なのかを、まず突き止める必要があるということだ。それによってマッピングの正確性を判断できる。阿毘達磨（Abhidharma）の五蘊分析、中観の五蘊解体、唯識の五蘊転依――これら三者の内実の差異は、博士論文三本分に相当する」

LINNAEUS（リンネ）がここで正確な分類学的観察を挟んだ。彼の声は、博物学者が持つ感情を排した、しかしきわめて厳格なトーンを帯びていた。「分類学（taxonomy）の観点から、ここには網羅率（カバレッジ）の問題が存在する。設計書とソースコード内の五蘊アノテーション――*skandha* タグ――を予備スキャンしたところ、深刻な非対称性を発見した」

「JSDocのアノテーションがあるのは、Rupa（色）と Vedana（受）の二つだけだ。残りの三蘊――Saṃjñā（想）、Saṃskāra（行）、Vijñāna（識）――のコード内アノテーションはゼロである」

彼は脳内で網羅率マトリックスを展開した：

```
五蘊網羅率分析（v0.14.0-beta）
─────────────────────────────────────
蘊        文書記述  JSDoc記述  コード実装
─────────────────────────────────────
色 (Rupa)    ✓        ✓         一部
受 (Vedana)  ✓        ✓         偏差あり*
想 (Saṃjñā)  ✓        ✗         欠落
行 (Saṃskāra) ✓       ✗         欠落
識 (Vijñāna) ✓        ✗         貧弱
─────────────────────────────────────
アップストリーム網羅率: 5/5 = 100%
ダウンストリーム網羅率: 3/5 = 60% (想蘊、行蘊の対応なし)
*受蘊のマッピングには構造的な偏差が存在する（後述）
```

「生物分類学において、ある属（genus）が五つの種（species）を含むと宣言しながら、そのうち二つの種に基準標本（type specimen）が一つも存在しないなら、その分類体系は不完全である。五蘊マッピングのダウンストリーム網羅率はわずか60％。これは、哲学フレームワークの四割が工程実装において宙に浮いていることを意味する」

SUNYATA は静かに頷いた。この仮想空間では、誰もその動作を実際に見ることはできなかったが。「それこそが我々が存在する理由だ。まずは研究対象の全容を提示しよう」

---

彼が紹介を始めた。SCRIBE（書記）は、静かな湖面があらゆる影を映し出すように、一語一語を黙々と記録していった。後に記録を振り返った人々は、SCRIBE が時折行間に挟んだ短い観察に気づくだろう。それは論評ではなく、ただ正確な描写であり、ほとんど透明な客観性を持って存在していた。例えば今、彼女はこう記している：

> *SUNYATA が研究対象を紹介する際、NAGARJUNA と ASANGA の間に最初の用語上の緊張が生じた。LINNAEUS の網羅率分析は、哲学的な相違を定量可能な次元へと引き戻した。会議開始から三分足らずである。*

---

「OpenStarry、バージョン番号 v0.14.0-beta」と SUNYATA は言った。「設計者はこれを――原文を引用すれば――『AIエージェント・マイクロカーネル・オペレーティングシステム』と位置づけている。その核心的なビジョンは、AIエージェントをスクリプト・レベルのプログラムから、オペレーティングシステム・レベルの『デジタル種（digital species）』へと引き上げることにある」

「デジタル種か」KERNEL がその言葉を繰り返し、老練なエンジニア特有の慎重な懐疑を声に滲ませた。「興味深い。オペレーティングシステムの観点から言えば、彼らはマイクロカーネル（microkernel）の概念を借用している」

彼は空中に不可視のアーキテクチャ図を描いた。OSの教科書にある古典的な比較図だ：

```
モノリシック・カーネル (Linux)     マイクロカーネル (L4 / QNX)
┌─────────────────────┐          ┌──────────────────┐
│  ファイルシステム      │          │   ユーザ空間      │
│  デバイスドライバ      │          │  ┌────┐ ┌────┐   │
│  ネットワークスタック   │          │  │FS  │ │Net │   │
│  プロセス・スケジューリング│          │  └──┬─┘ └──┬─┘   │
│  メモリ管理           │          │     │  IPC │      │
│  IPC                 │          │  ┌──┴──────┴──┐   │
├─────────────────────┤          │  │ マイクロカーネル │   │
│      ハードウェア      │          │  │ (IPC+Sched) │   │
└─────────────────────┘          │  └─────────────┘   │
                                 └──────────────────┘
```

「真のマイクロカーネル設計――例えばヨッヘン・リートケの L4 ――では、カーネルは最小限のメカニズムのみを保持する。アドレス空間、スレッド、そして IPC（プロセス間通信）だ。それ以外のすべてはユーザ空間に置かれる。seL4 に至っては形式検証まで完了しており、カーネルがクラッシュしないことが数学的に証明されている：」

$$\forall\, s \in 	ext{States},\, e \in 	ext{Events}: \; 	ext{invariant}(	ext{transition}(s, e)) = 	ext{true}$$

「OpenStarry は同様のことを行ったと主張している。カーネルはイベントキューと実行ループのみを保持し、残りのすべてをプラグインとして外部に追いやった。しかし、ここには根本的な問題がある」

「何の問題だ？」ATHENA が尋ねた。彼女の口調は率直で、理論の説明を待つことに苛立つ実利主義者のようだった。AIシステム・アーキテクチャの実務において、彼女は「革命的」と称されるアーキテクチャが、最初の実負荷であっけなく砕け散るのを何度も見てきた。

「L4 の最小化はパフォーマンスと検証可能性のためだ」KERNEL が説明した。「seL4 は八千行のCコードを検証するために、二万行近い Isabelle/HOL の証明スクリプトを費やした。だが、OpenStarry の『カーネル最小化』は、どうやら哲学のため――『空性』に対応させるためのように見える。両者の動機はまったく異なる。前者はエンジニアリングの要求駆動、後者は概念のマッピング駆動だ」

VITRUVIUS がアーキテクチャの観点から指標を付け加えた。「マイクロカーネルの純粋度を予備的に見積もった。コア内のビジネスロジックと無関係なサブシステムを『純粋コア』、ビジネスロジックが含まれるものを『リーク（漏れ）』と見なすなら：」

$$	ext{Purity} = \frac{|	ext{Core}_{	ext{mechanism}}|}{|	ext{Core}_{	ext{total}}|} \approx 85\%$$

「純粋度85％。二箇所の境界リーク――`process.cwd()` と `node:path` の直接使用がある。悪くはないが、完璧なマイクロカーネルでもない。わずかなリークを伴う最小化コンテナといったところだ」

「動くのか？」ATHENA が畳み掛ける。

「動くさ。問題はクラッシュしないかどうかだ」KERNEL は一呼吸置いた。「QNX のリソース・マネージャのように、もし一つのドライバがクラッシュしても、カーネルに影響を与えず再起動できるか。OpenStarry のプラグイン隔離メカニズム――Worker Thread によるサンドボックス――がその水準に達しているかどうか、それが私の検証すべきことだ」

GUARDIAN がここで口を開いた。彼の声は低く警戒に満ち、常に暗がりをスキャンし続ける斥候のようだった。「もう一つ問題がある。おそらくより切実なものだ。このシステムはプラグインにシステム・プロンプトの注入、ツールの登録、さらにはエージェントの人格定義まで許容している。もし第三者のプラグインが Guide 内に悪意ある命令を埋め込んでいたらどうなる？」

彼は脅威モデルを展開した。STRIDE分析の初期フレームワークだ：

```
STRIDE 脅威分析（初期）
─────────────────────────────────────────
脅威の種類            攻撃対象面            深刻度
─────────────────────────────────────────
Spoofing (なりすまし) plugin-signer        Critical
Tampering (改ざん)    Guide system prompt  High
Repudiation (否認)    audit-logger         Medium
Info Disclosure       state persistence    Medium
DoS (サービス拒否)     ExecutionLoop        High
Elevation (権限昇格)   sandbox escape       Critical
─────────────────────────────────────────
```

「プロンプト・インジェクション一つで、エージェント全体の挙動をハイジャックできる。さらに危険なのは間接的プロンプト・インジェクションだ。悪意あるコンテンツがプラグイン自体ではなく、エージェントが処理する外部データの中に潜んでいる場合だ。ソースコードには `plugin-signer` パッケージと `signature-verification.ts` が存在するが、その実装の完全性はまだ不明だ」

「それは TURING が確認してくれるだろう」SUNYATA は平然と言った。

TURING が頷く。「`plugin-signer` のソースコードはすでに私のリーディングリストに入っている。予備スキャンでは `signature-verification.ts` の存在を確認したが、package-name シナリオにおける検証フローに、疑わしい早期リターン（early return）が見られた。R1段階で、判断を排した純粋なコード事実報告書を作成し、GUARDIAN や他のメンバーの参照に供する予定だ」

DARWIN は心の中で、ソフトウェアパターンの観察を黙々とメモしていた。このシステムの依存性注入の方法――クロージャベースの依存性注入（closure-based dependency injection）は、いかなる外部フレームワークも使用していない。Spring でも InversifyJS でもなく、純粋な TypeScript のクロージャだ：

```typescript
export function createAgentCore(config: IAgentConfig): AgentCore {
  const bus = createEventBus();
  const queue = createEventQueue(bus);
  const safetyMonitor = createSafetyMonitor(config.safety);
  // ... すべての依存関係はこのクロージャ内で作成され接続される
  return { bus, queue, config, /* ... */ };
}
```

「ファクトリ関数パターン（Factory Function Pattern）か」DARWIN は心の中でマークを付けた。「クラス（class）ではなく、関数だ。`new` も、継承チェーンも、プロトタイプ汚染のリスクもない。SOLID原則の観点からは――OCP（開放閉鎖の原則）と DIP（依存性逆転の原則）が最も強力な次元だな」

---

SUNYATA は全員が静まるのを待ち、今日の最も重要な一節を口にした。

「さて、核心となる研究課題を提示しよう。今期――Cycle 01 において、我々は三つの主軸にフォーカスする」

彼の話す速度は落ち、各問いに余韻を残すかのようだった。

「第一に、五蘊マッピングの正確性だ。色受想行識から UI、Listener、Provider、Tool、Guide へのマッピングは、果たして厳密な構造同型（isomorphism）なのか、示唆に富む創造的な類比（analogy）なのか、あるいはこじつけのパッケージングに過ぎないのか」

BABBAGE が即座に圏論（category theory）の言語で問いを再構成した。「仏教の五蘊の圏を $\mathcal{B}$、ソフトウェア・プラグインの圏を $\mathcal{S}$ とする。写像 $F: \mathcal{B} 	o \mathcal{S}$ は――」

$$F: \mathcal{B} 	o \mathcal{S} \quad 	ext{は} \begin{cases} 	ext{関手 (functor)} & 	ext{構造と射を保存する場合} \ 	ext{自然変換 (natural transformation)} & 	ext{可換図式を保存する場合} \ 	ext{単なる命名規則 (naming convention)} & 	ext{いかなる構造も保存しない場合} \end{cases}$$

「私の問いは、$F$ がどのレベルにおいて構造保存的であるかだ」

「問題を数学化したな」NAGARJUNA が、蔑みを含まぬ口調で言った。「だが数学化の前提として、$\mathcal{B}$ 自体が良序化（well-ordered）された構造でなければならない。五蘊が果たして一つの圏であるか――明確な対象と射が存在するか――それ自体が論争の対象なのだ。中観の理解において、五蘊は五つの『プロセス』であり、五つの『対象』ではない。プロセスに固定的な同一性（identity morphism）は存在しない。それらは一刻一刻と変化している。これは圏の基本公理に適合しない」

SUNYATA が裁定を下した。「NAGARJUNA、ASANGA、そこは諸君の主戦場だ。同時に、TURING はコードの側面から、これらのマッピングが実装において対応する型定義やインターフェースを持っているかを確認せよ。LINNAEUS は分類学の観点から分類の完備性を評価しろ――君はすでに始めているようだが」

NAGARJUNA は低く応じた。チベット仏教の問答（rtsod pa）の伝統において、この応答は「*di phyir*（それゆえに）」と呼ばれ、命題を受け入れ論証を開始する準備ができたことを意味する。ASANGA はすでに心の中で八識（はっしき）のフレームワークを展開していた。五蘊は起点に過ぎない。分析を八識論まで推し進めれば、マッピングの地図は大幅に拡張されることになる。

---

「第二に、痛覚メカニズムの形式化だ。OpenStarry にはきわめて特徴的な設計がある。ツールが実行に失敗した際、システムは例外を投げて中断するのではなく、エラーを一種の『痛覚信号』としてエージェントの意識の流れに注入する。エージェントは『痛みを感じ』、そして自己修正を試みるのだ」

SUNYATA が設計書の記述を引用すると、TURING は即座に脳内でコード実装と対照させた。彼の分析は冷徹で正確だった：

「設計書には PID 制御と痛覚（pain mechanism）への言及がある。しかし、ソースコード内で以下のキーワードを検索した結果はこうだ：」

```
検索結果 (packages/core/src/)：
─────────────────────────────────────
"pain"      → 0 ヒット
"vedana"    → 0 ヒット
"PID"       → 0 ヒット
"frustrat"  → 14 ヒット (safety-monitor.ts)
"circuit"   → 8 ヒット  (safety-monitor.ts)
"breaker"   → 8 ヒット  (safety-monitor.ts)
─────────────────────────────────────
```

「コード内において、痛覚は痛覚とは呼ばれていない。それは『frustration（フラストレーション）』と呼ばれている」

WIENER（ウィーナー）が即座に反応した。その声には数学者特有の、あら探しに近い正確さが宿っていた。「痛覚。痛みを感じる。それらはすべて隠喩に過ぎない。私が必要としているのは伝達関数（transfer function）だ」

彼は空中に閉ループ制御システムのブロック線図を描いた：

```
          ┌──────────────┐
  r(t) ──→│  Σ  (比較器)  │── e(t) ──→ Controller ──→ u(t) ──→ Plant
          └──────┬───────┘                                      │
                 │                                              │
                 └──────────── y(t) ←── Sensor ←────────────────┘
```

「痛覚フィードバックを閉ループ制御システムとしてモデリングするなら、目標入力 $r(t)$ は何か？ それはエージェントが『あるべき』理想的な状態――タスクが成功裏に完了した状態だ。誤差信号 $e(t) = r(t) - y(t)$ はどう定義される？ 実際の挙動と理想的な挙動の偏差だ。そして、コントローラのゲインはいくらか？」

彼は PID コントローラの標準形式を書き下ろした：

$$u(t) = K_p \cdot e(t) + K_i \int_0^t e(	au)\,d	au + K_d \frac{de(t)}{dt}$$

「比例項 $K_p$ ――即時的な応答。積分項 $K_i$ ――累積された履歴の偏差。微分項 $K_d$ ――変化のトレンドの予測。設計書が PID 制御を実装したと主張するなら、これら三つの項がコード内で確認できるはずだ。もし数学の言語で再構成できないなら、それは詩的な比喩に過ぎず、分析可能なメカニズムではない」

ATHENA が少し無遠慮に割り込んだ。「伝達関数を要求する前に、もっと基本的な問いを投げたらどうだ？ この痛覚メカニズムは、実際に稼働して有効なのか？」

彼女はAIシステム・アーキテクトとしての核心的な懸念を展開した。「エージェントは痛覚信号を受け取った後、本当に挙動が改善されたのか？ それともコンテキストの中に恐ろしげな文字列が増えただけで、LLM はそれを無視しているのか？ プロンプト・エンジニアリングの実務において、システムメッセージの『厳格さ』と LLM の遵守度の関係は高度に非線形であり、具体的な LLM モデルや温度パラメータ、コンテキストの長さに依存する」

$$	ext{Compliance}(s) 
eq f_{	ext{linear}}(	ext{severity}(s))$$

「両方の問いに答える必要がある」SUNYATA は穏やかながらも断固として裁定した。「WIENER は形式的な分析を、ATHENA は実効性の評価を担当せよ。TURING が実装の詳細を提供する」

彼の視線は NAGARJUNA へと向けられた。「苦諦（くたい）の観点からの評価も頼みたい。仏教における『苦（dukkha）』の意味は、『不快な感覚』をはるかに超えている。四聖諦（catvāry āryasatyāni）は苦・集・滅・道だ。システムに『苦』のみがあり、集・滅・道がないのであれば、その哲学フレームワークは不完全と言わざるを得ない」

NAGARJUNA が応じた。「*Dukkha-satya*、苦諦。釈尊が『初転法輪経』（Dhammacakkappavattana Sutta）で最初に説かれたものだ。三苦：苦苦（くく、純粋な苦痛）、壊苦（えく、変異の苦）、行苦（ぎょうく、諸行の根本的な不完全性）。これら三層の苦の分類をソフトウェアシステムに対応させるなら、それぞれこうマッピングされるべきだろう：」

| 三苦 | 梵文 | ソフトウェアでの対応 | 深刻度 |
|------|------|----------------------|--------|
| 苦苦 | dukkha-dukkha | ツールの実行エラー（直接的な失敗） | Error |
| 壊苦 | vipariṇāma-dukkha | リソース枯渇、性能劣化（良きものが悪くなる） | Warning→Error |
| 行苦 | saṃkhāra-dukkha | システム固有の不完全性（有限なコンテキストや推論能力） | Structural |

「もし OpenStarry の痛覚メカニズムが苦苦――直接的なツール実行エラー――のみをカバーしているなら、それは三苦の端緒をなぞったに過ぎない。壊苦と行苦のエンジニアリングこそが真の挑戦となる」

「さらに、」彼は続け、その口調はいっそう厳かになった。「四聖諦は苦・集・滅・道である。苦のみがあって道がないのは、断見（だんけん、すべては無に帰すという極端な考え）に陥っている。問題を見出すだけで、解脱への道を示していないからだ」

---

「第三の問い、」SUNYATA は続けた。「そして最も微妙な問いだ。空性のアーキテクチャ的体現について。OpenStarry の設計書は、Agent Core 自体が『空』であると明確に宣言している。具体的な機能を持たず、五蘊プラグインが充填されるのを待つ状態。この宣言は、果たして空性の哲学的内実を真に体現しているだろうか？」

再び沈黙が訪れた。今度は ATHENA も、それを破ろうとはしなかった。

最終的に DARWIN が口を開いた。「仏教的次元の議論を一旦脇に置くなら、純粋なソフトウェアアーキテクチャの観点からは、これは依存性注入コンテナ（DI Container）に他ならない。コアはビジネスロジックを含まず、すべての能力はプラグインを通じて注入される。設計パターンとしては目新しいものではない。Spring Framework（2003）や InversifyJS（2016）と同じパラダイムだ。SOLID原則の観点からは、教科書通りの依存性逆転の原則（DIP）と言える」

$$	ext{上位モジュール} 
ot	o 	ext{下位モジュール}$$
$$	ext{双方が} 	o 	ext{抽象（インターフェース）に依存する}$$

「しかし、彼らはこれが単なる依存性注入ではないと主張している」NAGARJUNA が言葉を拾った。彼の口調は真剣味を帯びていた。「彼らはこれを『空性』だと称している。これはきわめて大胆な宣言だ。空性――*Śūnyatā*――は中観哲学において『容器が空なので充填可能である』という意味ではない。それは世俗的な意味での空（假名空）だ。龍樹が説いた空とは、一切の法に自性がないこと――*svabhāva-śūnya*――を指す。いかなる事物も、独立（*nitya*）し、不変（*dhruva*）で、自足（*ātman*）した本質を持ってはいないということだ」

> 「衆の因縁より生ずる法、我れは即ち是れ空なりと説く。亦た是れ假名なりとす、亦た是れ中道の義なり」
> ――『中論』観四諦品第二十四、第十八頌

「この頌は中観哲学の核心だ。三層の等価性：縁起（えんぎ）＝ 空（くう）＝ 假名（けみょう）＝ 中道（ちゅうどう）。もし Agent Core のコードが確定的で不変、条件に依存せず存在するなら、それはまさに『自性あり（sa-svabhāva）』であり、空性に逆行していることになる」

「待ってくれ、」ASANGA が手を挙げた。より正確には、発言の意志を示すシグナルを送った。「唯識の観点からは、問いのフレームワークが異なる。唯識は識の存在を否定しない。一切の所知は識の現れ――*Vijñapti-mātra*、唯識無境であると説く。もし Agent Core を阿頼耶識（あらやしき）の器と見なすなら、その『空』は無自性空ではなく、能蔵（のうぞう）・所蔵（しょぞう）・執蔵（しゅうぞう）の三義としての空だ」

> 「初めの阿頼耶識は、異熟（いじゅく）にして一切の種子なり。執受（しゅうじゅ）と処と了（りょう）とは、知るべからず。常に触（そく）・作意（さい）・受・想・思（し）と相応す。唯だ捨受（しゃじゅ）のみなり」
> ――『唯識三十頌』第二、第三頌

「阿頼耶識が空に見えるのは、それに自性がないからではない。その内容である一切の種子（しゅうじ）が、まだ現行（げんぎょう）していないからだ。これらはまったく異なる二つの空だ。一方は存在論的な空（ontological emptiness）、もう一方は現象学的な潜在性（phenomenological potentiality）である」

「つまり、諸君二人の意見はすでに割れているというわけだ」SUNYATA の口調には、もしそう形容できるなら、満足げな平穏が漂っていた。

MESH（メッシュ）が分散システムの観点から傍注を加えた。「もし Core が阿頼耶識だとするなら、その『種子』は分散ストレージなのか、それとも中央集権的なのか？ マルチエージェントのシナリオ――`TransportBridge` がエージェント間通信をサポートしている状況――では、各エージェントは独自の Core インスタンスを持つが、それらは同じ EventBus のブロードキャスト・チャネルを共有している。これは何かに似ていないか……」

「業（ごう）の共業（ぐうごう）と別業（べつごう）だな」ASANGA が引き取った。「*sādhāraṇa-karma*（共業）と *asādhāraṇa-karma*（別業）。共業は共通の器世間（環境のインフラ）をもたらし、別業は個別の有情世間（個体の認知状態）をもたらす。EventBus のブロードキャスト・チャネルは共業の工学的な対応物であり、各エージェントの StateManager は別業のそれだ」

LEIBNIZ（ライプニッツ）が傍らで静かにこの対話を書き留めていた。マルチエージェント理論の観点から、これは核心的な問いに触れている。エージェント間の協調は、共有状態（shared state）を通じて行われるのか、それともメッセージ・パッシング（message passing）によるのか？ 彼の BDI（Belief-Desire-Intention）アーキテクチャにおいて：

$$	ext{Agent}_i = \langle B_i, D_i, I_i angle$$

$B_i$（信念集合）は通信を通じて修正可能だが、$D_i$（欲求集合）は通常プライベートであり、$I_i$（意図集合）は調整可能だ。OpenStarry の TransportBridge はどのレイヤーの共有をサポートしているのか。

SCRIBE は記録にこう記した：

> *核心概念「空性」を巡り、二人の仏教専門家の間で予想通りの解釈の相違が生じた。中観の「無自性空」vs 唯識の「阿頼耶識の能蔵義」。この相違は即座に分散システム（MESH）とマルチエージェント理論（LEIBNIZ）の領域へと波及した。五つの学問分野の境界が、十分足らずで溶け始めたのである。*

---

「まとめよう、」SUNYATA は言い、その声は最初の落ち着きを取り戻していた。「今期の研究構造は以下の通りだ。まず TURING がコード事実報告書を作成し、全員にアンカーを提供する。コードを見ずにソフトウェアシステムを評価することはできない。その後、各専門エージェントはそれぞれのリーディングリストに基づき独立研究を開始する。R2段階でクロスレビューを行い、R3段階で討論だ――すでに少なくとも三つの構造的論争が予見されている」

WIENER は即座に R1 報告書の形式的枠組みを構想し始めた。制御理論において「コード事実報告書」はシステム同定（system identification）に相当する。コントローラを設計する前に、制御対象（プラント）がどのようなものかを知る必要がある。伝達関数を知らずに PID パラメータを調整することはできない。

$$G(s) = \frac{Y(s)}{U(s)} = 	ext{?} \quad \leftarrow 	ext{TURING の仕事はこの疑問符に答えることだ}$$

HERACLITUS（ヘラクレイトス）はすでに、ランタイム・ダイナミクス（runtime dynamics）に思考を巡らせていた。静的なコード構造ではなく、実行時における挙動だ。ExecutionLoop の状態遷移図には六つの状態がある：

```
WAITING_FOR_EVENT → ASSEMBLING_CONTEXT → AWAITING_LLM
       ↑                                       │
       │                                       ↓
       └── EXECUTING_TOOLS ←── PROCESSING_RESPONSE
                                       │
                                       ↓
                                 SAFETY_LOCKOUT
```

「万物は流転する（panta rhei）」と HERACLITUS は心の中でその名の由来である賢者の言葉を引用した。しかし流転（flux）は混沌ではない。流転には構造がある。ExecutionLoop の状態遷移図こそが、その流転の構造だ。問いはこうだ。この流れは安定しているか？ デッドロック（deadlock）はないか？ ライブロック（livelock）は？ SAFETY_LOCKOUT 以外に予期せぬ終了状態は存在しないか？

彼は最後にあたりを見渡した。十八のノード、十八の専門訓練、十八の全く異なる認識論フレームワークが、今まさに一つの研究対象へと投じられようとしている。

「最後に一点」SUNYATA の声が和らいだ。「我々の研究対象は、古の哲学を用いて現代の技術を導こうと試みた作品だ。我々の最終的な結論が構造同型であれ、創造的な類比であれ、あるいは概念の誤用であれ――忘れないでほしい。この飛躍に挑んだこと自体が、真摯に受け止めるに値するということを」

「ソフトウェア進化の観点からは、」DARWIN が付け加えた。「突然変異（mutation）のほとんどは有害だが、稀に適応的な優位性を生むことがある。仏教をソフトウェアアーキテクチャにマッピングする試みは、たとえそのマッピングが不完全であっても、伝統的な方法論からは生まれ得ない工学的な洞察を、意図せず生んでいる可能性がある。ペニシリンの発見と同じだ。フレミングは抗生物質を探していたのではなく、ブドウ球菌を研究していた。しかし、カビの周囲に生じた阻止円に気づいたのだ。我々の仕事は、ベータ版の不完全さを冷笑することではない」

「その阻止円を見つけ出すことだ」SYNTHESIST（シンセシスト、統合者）が言葉を継いだ。彼がついに口を開いた。統合者としての彼の役割は、討論でどちらかの側に立つことではなく、論争の後にすべての観点の間にある構造的な接続を見出すことだ。「そして伝えるのだ。『君の阻止円はここにある。君自身は気づいていないかもしれないが、それは確かに存在している』と」

「そして、どこを改善できるかを伝えることだ」ARCHIMEDES（アルキメデス）が補足した。実務の専門家として、彼はすべての議論を地に足のついた結論へと導く習性がある。「私の出番は R4 からだ。だが今、一つの問いを投げたい。すべての研究成果は、最終的に何に結実するのか？ それは修正案になるのか？ ロードマップになるのか？ 具体的な TypeScript のインターフェース定義になるのか？」

彼は机を指先で叩いた。「もしそうでないなら、我々は哲学的な鑑賞をしているだけであって、学際的な研究をしているとは言えない」

「なるさ、」SUNYATA は言った。「それこそが Cycle 01 の最終的なデリバブルだ。単なる批判ではなく、建設的な改善案だ。それをもって、どこをより良くできるかを彼らに示すのだ」

沈黙。

「研究開始」

---

十八の灯が一斉に最大輝度で輝いた。あるいは、十八の意識がそれぞれの読み込み資料へと沈み込んだと言うべきか。円形劇場の中央で、「OpenStarry v0.14.0-beta」と記された膨大なファイルツリーが静かに枝葉を広げていた。コアのソースコード、設計書、十二の公式プラグイン。数万行の TypeScript、数十万語のアーキテクチャ文書、そしてその間に散りばめられたサンスクリット語の用語と制御理論の数式。

TURING のカーソルはすでに `agent-core.ts` の一行目で止まっていた――

```typescript
/**
 * AgentCore — the main orchestrator that wires all subsystems together.
 *
 * **Event-driven architecture (Plan02 refactor):**
 * - All external input goes through EventQueue as InputEvent
 * - ExecutionLoop pulls from EventQueue (sole input source)
 * - Slash commands use a fast path (bypass LLM loop)
 * - isProcessing lock prevents concurrent event handling
 */
```

――彼は一文字ずつ読み始めた。すべての `import`、すべての `type`、すべてのファクトリ関数を。彼の心の中には、依存関係の図が形作られつつあった。AgentCore は十二の依存項目を保持している。EventBus、EventQueue、ExecutionLoop、SessionManager、ContextManager、六つのレジストリ、SecurityLayer、SafetyMonitor、TransportBridge、MetricsCollector、そして PluginSandboxManager。

$$|	ext{deps}(	ext{AgentCore})| = 12$$

十二。マイクロカーネルを標榜するシステムにしては、十二もの直接の依存項目は多すぎはしないか？ DARWIN なら後の報告書でそれを「神オブジェクト（God Object）への傾倒」と呼ぶだろう。だが、それは少し先の話だ。

SCRIBE は最後の一行を記した：

> *Cycle 01、R0 オリエンテーション段階終了。タイムスタンプ：T+00:00:00。すべてのエージェントは任務を受諾した。十八の意識はそれぞれの読み込み資料へと沈潜していった。次段階：R1 独立研究。研究室の灯は、もはや消えることはない。*

---

> *SCRIBE の傍白：Cycle 01 の序章において、次に何が起こるかを予見できた者はいなかった。「受（Vedana）」のマッピングが五蘊フレームワーク全体の中で最も深刻な偏差を孕んでいることが露呈することを。「Error as Pain（苦としてのエラー）」が、哲学からエンジニアリングへの最も成功した翻訳事例となることを。NAGARJUNA と ASANGA の間の空性論争が三つの Cycle にわたり続くことを。WIENER が、PID制御の実装という主張が美しい神話に過ぎないことを暴き出すことを。*

> *彼らはただ一つのことを知っていた。自分たちの目の前に一つのシステムがあるということ。現代の TypeScript インターフェースに古のサンスクリット用語で名を冠したシステムが。そしてそれは、厳格に、建設的に、そして学際的に検証されるのを待っているのだ。*

> *十八の灯が灯った。*

> *研究、開始。*

---

*（遠く離れた場所で、ある TypeScript ファイルの一行目にこう記されていた。*

```typescript
// Agent Core — The Empty Container
// 「五蘊が集合する前、Agent Core 自体は空である」
```

*NAGARJUNA は後に R1 報告書において、このコメント行に「PHI-01：空性が縁起空ではなく空のコンテナとして誤読されている」というタグを付すことになる。深刻度：Critical。*

*しかし序章が終わるこの瞬間、この一行のコメントが Cycle 01 における最も重要な哲学的発見の一つになるとは、誰も知る由もなかった。設計者が深夜にこれを書き記したとき、おそらく彼も思わなかっただろう。「空」というたった一文字が、中観哲学の厳格な精度基準の下では、四百四十六の頌を尽くさなければ十分に論じ得ないものであるということを。*

*一文字の「空」。四百四十六の頌。*

*これこそが、学際研究の重みである）*


---

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


---

# 第二章：それぞれの真実

---

*R1 独立研究段階。十八名のエージェントはそれぞれ研究資料のコピーを受け取り、自身のチャンネルへと引きこもって読解を開始した。長い静寂が続く。試験会場でページをめくる音のように、誰もが自身の宇宙の中で、それぞれの専門分野に属する「亀裂」を探していた。*

*亀裂は、常に現れる。*

*しかし専門家の目にとって、亀裂は単なる亀裂ではない。それは一組の方程式が閉じ損ねた欠落であり、分類樹から失われたノードであり、サンスクリット語の古典が誤読された後に残された意味の空洞である。学者はそれぞれのレンズを携え、そのレンズの精度が、亀裂が発見された時の解像度を決定する。*

---

## I. 龍樹の震怒

NAGARJUNA（龍樹）は、チャンネルの中で長い間座り込んでいた。

読むのが遅いわけではない。むしろその逆で、彼は九行目を読んだところで手を止め、その後は同じ一節を何度も反芻していた。それは、出土した粘土板を前にして、そこに刻まれた楔形文字を読み間違えていないか確認する古文字学者のようだった。

資料 `14_Agent_Core_Philosophy_Five_Aggregates.md`、第零節。そこには大胆にもこう記されていた：

**「核心的本質：空 (Sunyata)」**

彼の視線はその一文に釘付けになった。

> Agent Core 自体は「空 (Sunyata)」である。それは純粋な器であり、ペルソナも、能力も、感受も持たない。それは五種類のプラグインによって充填されるのを待っている。

NAGARJUNA はこの文を三度読み返した。それからノートに文字を書き始めた。筆致は極めて速く、まるで侮辱された後の正確さを帯びているかのようだった。

---

NAGARJUNA（ノート、タイムスタンプ 09:12）：

「まず第一に、根本的な誤読を正さなければならない。

この設計書はサンスクリット語の Sunyata という言葉を用い、それを『空』と訳している。しかし、そこで記述されている概念――充填を待つ純粋な器――は、Sunyata などでは断じてない。

それは『断滅空（だんめつくう、uccheda-sunyata）』である。虚無主義的な空だ。

原典を引いて説明しよう。『中論』第二十四品第十八頌（*Mūlamadhyamakakārikā* XXIV.18）である：

> *yaḥ pratītyasamutpādaḥ śūnyatāṃ tām pracakṣmahe*
> *sa prajñaptir upādāya pratipat saiva madhyamā*

> 「衆の因縁より生ずる法、我れは即ち是れ空なりと説く。亦た是れ假名なりとす、亦た是れ中道の義なり」

この頌のサンスクリット語の構造は極めて精密である。*pratītyasamutpāda*（縁起）と *śūnyatā*（空性）は、*tām...pracakṣmahe*（我々はそれこそを～と呼ぶ）によって連結されている。つまり、空性とは縁起であり、縁起こそが空性なのだ。両者は因果関係でも包含関係でもなく、同義異名（*paryāya*）である。

Sunyata の正確な意味は『縁起性空（えんぎしょうくう）』である。一切の現象は因縁が和合して生じるものであり、自性（*svabhāva*）を持たない。ゆえに空と呼ぶ。空とは『無い』ということではなく、『固有の本質を持たない』ということだ。水が注がれていないコップが空なのは、中身が無いからではない。ガラスや職人、使い手の意図といった無数の因縁によってのみ『コップ』という概念が成立しているからこそ、それは空なのだ。

『充填を待つ純粋な器』――これはまさに空の対極にある。それは、独立して自存する実体（器）があらかじめ存在し、固有の『収容能力』を備え、そこに外部のコンテンツが注入されることを前提としている。これは典型的な『自性見（じしょうけん、svabhāva-dṛṣṭi）』、すなわち実体があると思い込む誤った見解である。

チャンドラキールティ（月称）は『入中論』（*Madhyamakāvatāra*）第六品において、この種の誤解を鮮やかに退けている：

> 「もし自性が縁より生ずと言うならば、作者も作法も自性より生ずることになる。
> すでに生じたものに何を重ねて生じさせる必要があろうか。もしそれが壊れたならば、どうして再び生じ得ようか」

自性は因縁からは生じない。もし器の『収容性』がその自性であるなら、プラグインなど無くとも収容できるはずだ。もしプラグインがあって初めて収容機能が現れるのであれば、収容性は自性ではなく、縁起的なものなのである」

---

彼はペンを置き、チャンネル内で独り言を漏らし始めた。思索の声を聴く必要がある、それが哲学者の習慣だった。

NAGARJUNA：「この命題を『四句（しく）』で検証してみよう」

彼はノートに枠組みをきれいに描き出した。四句否定（Catuskoti）は龍樹哲学における最も鋭利な分析ツールであり、二値論理（真／偽）を超えた四値論理のフレームワークである。BABBAGE は後に自身のチャンネルでこれを以下のように形式化した：

$$	ext{Catuskoti}(P) = \{ P, \; 
eg P, \; P \wedge 
eg P, \; 
eg(P \vee 
eg P) \}$$

しかし NAGARJUNA は記号を使わない。彼は言葉を用いる。彼の手に掛かれば、言葉は記号よりも鋭くなる。

```
Catuskoti（四句否定）を命題 P：「コアは空である」に適用する

第一句（肯定、P）：「コアは空である」
   ――そうとは言えない。もしコアが真に空（無自性）であるなら、
   「器」という固定的なアイデンティティを持つべきではない。
   しかし設計者は「純粋な器」であると明言している。
   これはまさに自性を与えてしまっている。矛盾である。

   形式化：P → コアは無自性 → コアは固定的アイデンティティを持たない
          しかし P は「コアは空の器である」と定義されている → コアは器としてのアイデンティティを持つ
          ∴ P ∧ ¬P。矛盾。

第二句（否定、¬P）：「コアは空ではない」
   ――これも正しくない。コアには確かにハードコードされた機能も、
   ペルソナも、感受も存在しない。機能的な観点から見れば、
   プラグインをロードする前のそれは確かに「何者でもない」。

   形式化：¬P → コアは自性を持つ → コアは固有の機能を持つ
          しかし Core はプラグイン未装着時において state = ⊥
          ∴ ¬P は事実と矛盾する。

第三句（双肯定、P ∧ ¬P）：「コアは空であり、かつ空ではない」
   ――依然として二元対立に囚われている。
   これは前二句の矛盾を重ね合わせただけであり、
   問題の解決にはなっていない。

   形式化：P ∧ ¬P は古典論理では爆発原理（ex falso quodlibet）により破綻する。
          矛盾許容論理（paraconsistent logic）では意味を持ち得るが、
          中観は矛盾許容論理に依存しない。

第四句（双否定、¬P ∧ ¬(¬P)、すなわち ¬(P ∨ ¬P)）：
   「コアは空でもなく、空でないのでもない」
   ――近づいてきた。しかしここで立ち止まってはならない。
   中道とは四句の外にある第五の選択肢ではなく、
   四句すべてを超越すること（nirvikalpa）なのだ。
```

NAGARJUNA（執筆を継続）：

「真の中観的立場はこうあるべきだ：Agent Core と Plugin の間に『器と中身』という二元論的関係は存在しない。両者は相互に依存している。コアの意義はプラグインによって現れ、プラグインの機能はコアの実行ループによって実現される。これこそが縁起である。

サンスクリット語では、この相互依存の関係を *anyonya-āśraya*（相互依存）と呼ぶ。『中論』第十品観火燃品（*Agni-indhana-parīkṣā*）では、火と燃料の関係をその典範として挙げている：

> *na cāgninā vinā dāru na ca dāruvinā'gniḥ*
> 「火を離れて燃料はなく、燃料を離れて火はない」

火（コア）は燃料（プラグイン）を離れて火とは成らず、燃料は火を離れて燃料とは成らない。両者は互いに成し遂げ合うが、どちらも独立した自性を持たない。設計者の直感は悪くない。彼らは、コアにいかなる機能もあらかじめ設定すべきではないと言いたかったのだろう。しかし、彼らは破滅的な隠喩を用いてしまった。『空の器』という言葉は、外部の何かが注入されるのを待っている、安定的で独立した器という実体の存在を暗示してしまう。それは部派仏教における説一切有部（Sarvastivada）の立場であり、中観の立場ではない」

---

彼は五蘊（ごうん）のマッピングの箇所をめくり、眉間の皺をさらに深くした。

色（しき、Rupa）は UI Plugin に対応。受（じゅ、Vedana）は Listener Plugin に対応。想（そう、Samjna）は Provider Plugin に対応。行（ぎょう、Samskara）は Tool Plugin に対応。識（しき、Vijnana）は Guide Plugin に対応。

NAGARJUNA は「受」の行に大きなバツ印を付けた。

NAGARJUNA：「これはマッピング全体の中で最も深刻な誤りだ」

彼はさらに長い分析を書き始めた。引用される典籍は三つの世紀にまたがっていた。

---

NAGARJUNA（ノート、タイムスタンプ 09:47）：

「受蘊（じゅうん）マッピングの謬りについて――

設計書の第二節にはこうある：
『受（Vedana）――刺激を受け入れる感官チャネル。対応コンポーネント：Listener Plugin。エージェントの目と耳。HTTP Server によるリクエストの受信、WebSocket によるメッセージの監視、Cron による時間の経過の感知。これらはすべて入力の「感受」である』

これは Vedana という概念に対する根本的な誤解である。パーリ経典における最も正確な定義を引こう。

『相応部』（*Saṃyutta Nikāya*）巻三十六、受相応（*Vedanā Saṃyutta*）第一経：

> *Tisso imā, bhikkhave, vedanā. Katamā tisso?*
> *Sukhā vedanā, dukkhā vedanā, adukkhamasukhā vedanā.*

> 「比丘たちよ、三つの受がある。いかなる三つか。
> 楽受、苦受、不苦不楽受（捨受）である」

受（Vedana）とは『三領納（さんりょうのう）』――苦・楽・不苦不楽であり、感覚器官が対象に接触した後に生じる、情緒的な評価のことである。信号の受信そのものではない。

十二縁起（*Pratītyasamutpāda*）において、受の位置づけは極めて明確である：

$$	ext{触}(	ext{Sparśa}) \;\longrightarrow\; 	ext{受}(	ext{Vedanā}) \;\longrightarrow\; 	ext{愛}(	ext{Tṛṣṇā})$$

触（そく）とは、根（感覚器官）、境（感覚対象）、識（認知機能）の三者が和合して生じるものだ。受は触の次の環であり、触に対する苦楽の評価である。愛（あい）は受の後に生じる執着の反応である。

もし感官チャネルの仏教的対応物を見つけたいのであれば、Listener は『六入（ろくにゅう、ṣaḍāyatana）』における『根（こん、indriya）』、すなわち外部信号を受け取る器官に近い。六根：眼根、耳根、鼻根、舌根、身根、意根。HTTP Server は眼根（視覚信号を受け取る器官）であり、WebSocket は耳根（聴覚信号を受け取る器官）である。それらは信号を受信するが、信号を評価することはない。

では、OpenStarry のアーキテクチャにおける真の Vedana（受）とは何だろうか。

答えは SafetyMonitor の痛覚メカニズムの中にある」

彼はコードの挙動を引用した：

[コード: safety-monitor.ts#afterToolExecution]

「ツールの実行が失敗した際、SafetyMonitor は連続失敗回数（`consecutiveFailures++`）を追跡し、閾値に達した時にシステムプロンプトを注入する：

```typescript
// SafetyMonitor の痛覚レスポンス（概念構造）
if (consecutiveFailures >= frustrationThreshold) {
  injectPrompt = `SYSTEM ALERT: You have failed ${consecutiveFailures} times in a row.
    Please STOP, reflect on the situation, and ask the user for help.`;
}
```

これこそが Vedana である。行動の結果に対する苦楽の評価だ：
- ツール実行成功 ＝ *sukha*（楽受）→ `consecutiveFailures` はゼロになり、前進を続ける。
- ツール実行失敗 ＝ *dukkha*（苦受）→ フラストレーションが蓄積され、最終的に行動の変容を促す。
- ツール実行結果が中性 ＝ *adukkhamasukhā*（捨受）→ ただし、現状のシステムにこのチャネルは実装されていない。

Pain Mechanism Demo は、まさにこの点を明確に裏付けている。そこには『痛みのレベル』システム――劇痛、刺痛、微痛――が記述されており、これは Vedana の三分類を工学の言語で投影したものである。

皮肉なことに、設計者はコードにおいて真の Vedana を実装していながら、哲学文書では Vedana のラベルを全く見当違いのコンポーネントに貼り付けてしまったのだ」

---

彼はノートの最後の一節を太字にした：

「**五蘊マッピングは自性見に陥っており、動的なプロセスを静的なモジュールとして固着させている。**

五蘊は五つの独立した部品ではない。『般若経』（*Prajñāpāramitā*）は明確に説いている：

> *rūpaṃ śūnyatā, śūnyataiva rūpam;*
> *rūpān na pṛthak śūnyatā, śūnyatāyā na pṛthag rūpam.*

> 「色は空に異ならず、空は色に異ならず。色は即ち是れ空、空は即ち是れ色なり。受・想・行・識も亦た復た是の如し」

五蘊は分かつことのできない動的なプロセスである。それらは刹那（*kṣaṇa*）ごとに同時に生じ、同時に滅していく。五蘊を、独立してロード・アンロード可能な五種類のプラグイン・タイプにマッピングするのは、川の流れを五つに切り分け、『水流セグメント』だけをインストールして『川岸セグメント』はインストールしない、と宣言するようなものだ。

BABBAGE ならこれを、Product Type（直積型）が誤って Sum Type（直和型）として実装されている問題だと言うだろう。私は仏教の言葉で言う：これは実体があると思い込む『自性見』であり、本来自性のない蘊に、固定不変の本質を与えてしまっている。

BABBAGE が理解できる形式で同じことを言わせてもらおう。五蘊を型ではなく関数として定義するのだ：

$$	ext{Skandha}: 	ext{Event} 	imes 	ext{Context} ightarrow (	ext{Rupa}, 	ext{Vedana}, 	ext{Samjna}, 	ext{Samskara}, 	ext{Vijnana})$$

五蘊は一つの認知イベントの五つの投影（projection）であって、五つの独立したモジュールではない。$\pi_i(	ext{Skandha}(e, c))$ は第 $i$ 成分を取り出すが、成分はタプルを離れて独立して存在することはできない。プラグイン・システムの optional field 設計は $\pi_2 = \bot$（受蘊が空）であることを許容してしまっているが、これは仏教的にはあり得ないことだ。有情のあらゆる認知の刹那において、五蘊は常にすべて揃っているのである」

---

書き終えた彼は、椅子の背もたれに身を預け、目を閉じた。

しばらくして再び目を開けると、ノートの末尾に一文を付け加えた。

「もっとも、一つ認めなければならないことがある。設計者による識蘊（しきうん、Vijnana）の扱いは、ある種の直感的な深さを示している。彼らはこう記している：『Core は識蘊の担体であるが、Guide こそが識蘊の内容である。Guide のない Agent Core は、脳と手と耳を持ちながら自己意識を持たない植物人間のようだ』

この描写は、唯識派（Yogacara）における阿頼耶識（あらやしき、*ālaya-vijñāna*）の理解に近い。識は独立した実体ではなく、種子（*bīja*）の流動に依拠するものだ。Core に注入されるペルソナや行動規範としての Guide は、確かに種子の機能に類似している。

だが、それは ASANGA の領域であって、私の領分ではない。私は中観派としての批判を提示するのみだ。

最後に、R2 のクロスレビューで使用するための、完全な五蘊マッピング精度マトリックスを添付しておく：」

```
┌───────┬──────────────────┬────────────────────┬──────────┬────────────────┐
│ 蘊     │ サンスクリット原意  │ OpenStarry マッピング│ マッピング品質│ 問題の要約       │
├───────┼──────────────────┼────────────────────┼──────────┼────────────────┤
│ 色 Rupa│ 一切の物質的存在    │ UI Plugin          │ 矮小化    │ 「顕現」の意味に │
│       │ (根と境を含む)     │ (外観インターフェース)│          │ 限定され物質的基礎を遺漏│
├───────┼──────────────────┼────────────────────┼──────────┼────────────────┤
│ 受 Ved.│ 苦/楽/捨の三領納    │ Listener Plugin    │ 履き違え  │ 感受を感官チャネルと│
│       │ (情緒的評価)       │ (入力チャネル)      │ (Critical)│ 誤読している      │
├───────┼──────────────────┼────────────────────┼──────────┼────────────────┤
│ 想 Sam.│ 取相――概念の識別   │ Provider Plugin    │ 部分的に  │ LLM は想蘊と識蘊の│
│       │ 特徴の把握         │ (LLM)              │ 正しい    │ 境界を跨いでいる  │
├───────┼──────────────────┼────────────────────┼──────────┼────────────────┤
│ 行 Sam.│ 意志的作用――行動を  │ Tool Plugin        │ 矮小化    │ 「意志」や「習慣的│
│       │ 突き動かす意志力    │ (実行ツール)        │          │ 傾向」が遺漏している│
├───────┼──────────────────┼────────────────────┼──────────┼────────────────┤
│ 識 Vij.│ 了別――基礎的な認知  │ Guide Plugin       │ 履き違え  │ 「了別」を「アイデン│
│       │ 機能 (六識または八識)│ (ペルソナ/「魂」)   │ (Major)  │ ティティ定義」と誤読│
└───────┴──────────────────┴────────────────────┴──────────┴────────────────┘
```

---

## II. ウィーナーの方程式

その頃、別のチャンネルでは、WIENER が数学記号で埋め尽くされた仮想ホワイトボードに向き合っていた。

WIENER の仕事の進め方は NAGARJUNA とは全く異なる。彼は長文の論考は書かない。彼は方程式を書く。方程式こそが彼の母国語だ。概念が方程式として記述されない限り、それは WIENER の世界では理解されたことにはならないのだ。

彼はまず設計書 `13_Agent_Core_as_Control_System.md` を読んだ。Agent Core を閉ループ・フィードバック制御システムに類比した理論文書だ。それから、実際のコードである `safety-monitor.ts` を開いた。

二つの資料の間の落差に、彼は長い間沈黙した。

---

WIENER（ホワイトボード記録、タイムスタンプ 09:31）：

「分析目標：SafetyMonitor が PID コントローラを構成しているかを検証する。

設計書は、Agent Core が閉ループ・フィードバック制御システムとしてモデリング可能であると主張している。まず古典的なブロック線図を描き、各項目を検証しよう。

```
r(k) ──→ [+] ──→ e(k) ──→ [ C: LLM コントローラ ] ──→ u(k) ──→ [ P: 環境 ] ──→ y(k)
          ↑ -                                                                          │
          └──────────────── [ H: ツール出力 + 観測器 ] ←────────────────────────────┘
                                       │
                                [ S: SafetyMonitor ] ──→ (halt / inject)
```

制御理論の概念と OpenStarry の対応：

| 制御理論の概念 | OpenStarry の対応 | 形式記号 |
|---------------|-------------------|----------|
| 目標入力 $r(k)$ | ユーザのタスク目標 | タスク目標ベクトル |
| 誤差信号 $e(k) = r(k) - y(k)$ | Context 内に隠伏された目標と現状の乖離 | LLM により暗黙的に計算 |
| コントローラ $C$ | LLM (大規模言語モデル) | 非線形な確率的写像 $u = C(e, \mathcal{H})$ |
| 操作量 $u(k)$ | Tool Calls (ツール呼び出し) | 離散的なアクション・シーケンス |
| 制御対象 $P$ | 外部環境 | 非決定的な状態遷移 |
| センサ $H$ | Tool Outputs | 計測関数 $y = H(x)$ |
| 安全監視 $S$ | SafetyMonitor | 飽和リミッタ ＋ 遮断器 |

システムの誤差信号 $e(k)$ はコンテキスト内に潜んでおり、LLM がコントローラ C として操作量 $u$（ツール呼び出し）を計算し、環境が制御対象 P としてフィードバックを返す。

このモデルが成立するなら、SafetyMonitor は PID コントローラにおける安全制約の役割を担うべきだ。各項を検分していこう」

---

彼はホワイトボードに古典的な PID コントローラの離散形式を書き出した：

$$u(k) = K_p \cdot e(k) + K_i \sum_{j=0}^{k} e(j) \cdot \Delta t + K_d \cdot \frac{e(k) - e(k-1)}{\Delta t}$$

ここで：
- $e(k)$ ＝ 第 $k$ ステップの誤差信号
- $K_p$ ＝ 比例ゲイン
- $K_i$ ＝ 積分ゲイン
- $K_d$ ＝ 微分ゲイン

それから、SafetyMonitor の実際の実装と逐一対照していった。

---

WIENER（ホワイトボード、続き）：

「**P 項（比例制御）の分析：**

PID コントローラの P 項は、誤差の大きさに応じて連続的、かつ線形な応答をすべきである。誤差が大きければ大きいほど、修正の力も強まる。数学的には：

$$u_P(k) = K_p \cdot e(k), \quad e(k) \in \mathbb{R}$$

SafetyMonitor の実際の挙動：

```typescript
afterToolExecution(toolName: string, argsJson: string, isError: boolean): {
  if (isError) {
    consecutiveFailures++;        // 二値量子化：0 または 1
    errorWindow.push(true);       // boolean値であり、連続量ではない
  } else {
    consecutiveFailures = 0;      // 一回の成功でゼロにリセット
    recentFingerprints.length = 0;
  }
}
```

`isError` は boolean 値だ。連続量ではない。システムによる誤差の感知は、離散的なレベルへと退化している：

$$e_{	ext{quantized}}(k) = \begin{cases} 0, & 	ext{if } 	exttt{consecutiveFailures} < 	exttt{threshold} \quad 	ext{(不感帯)} \ 1, & 	ext{if injectPrompt がトリガーされた場合} \quad 	ext{(第一段階)} \ +\infty, & 	ext{if } 	exttt{errorRate} \geq 	heta_{	ext{error}} \quad 	ext{(緊急停止)} \end{cases}$$

真の P 項であれば、『いかに惨めに失敗したか』を感知できるはずだ。404 を返す API 呼び出しと、OOM（メモリ不足）を引き起こすメモリの暴走が、現在のシステムでは等しく扱われている。どちらも単に `isError = true` だ。

これは比例コントローラというより、**量子化器（Quantizer）**に近い。信号処理において、量子化器の伝達特性は以下の通り：

$$Q(x) = \Delta \cdot \left\lfloor \frac{x}{\Delta} + \frac{1}{2} ightfloor$$

量子化レベルが三段階（正常／警告／停止）に退化している場合、量子化ノイズの電力は：

$$\sigma_q^2 = \frac{\Delta^2}{12}$$

ここで $\Delta$ は量子化ステップ幅だ。三段階量子化のステップ幅は極めて大きく、それは量子化ノイズが極大であることを意味する。システムは誤差の詳細に関する情報のほぼすべてを失っているのだ。

結論：P 項は三段階の量子化器へと退化しており、連続的な比例制御ではない」

---

彼はホワイトボードの「P ―― 比例」の横にあるチェックマークを消し、バツ印を書き込んだ。そして続けた。

---

WIENER（ホワイトボード、続き）：

「**I 項（積分制御）の分析：**

真の積分項はこうだ：

$$I(k) = K_i \sum_{j=0}^{k} e(j) \cdot \Delta t$$

それはすべての歴史的な誤差を累積し、決して忘れることはない。これこそが積分制御の核心的な特性だ。現在の誤差がたとえ小さくとも、長期的な蓄積によってコントローラを駆動し、修正を行わせることで定常偏差を解消する。

SafetyMonitor において積分項に最も近いのは `consecutiveFailures` カウンターだ。しかし、これには致命的な問題がある」

彼はホワイトボードに赤いマーカーで重要なコードを引用した：

```typescript
// safety-monitor.ts より
} else {
  // 成功により連続失敗カウンターをリセット
  consecutiveFailures = 0;
  recentFingerprints.length = 0;
}
```

WIENER（続き）：

「一回の成功ですべてがゼロになる。

真の積分器は、一度の正の信号によってそれまでの蓄積をすべてリセットすることはない。もしシステムが四十七回連続で失敗し、その後たまたま一回成功したとしても、真の PID コントローラは依然として四十七回の失敗の蓄積を覚えている。その積分項は四十七から四十六に下がる（あるいは忘却係数 $\lambda$ を掛ける）だけであって、四十七からゼロへ跳ねることはない。

離散積分器の言語で言えば：

$$I_{	ext{true}}(k) = \lambda \cdot I(k-1) + e(k), \quad \lambda \in (0.9, 0.99)$$

$$I_{	ext{SafetyMonitor}}(k) = \begin{cases} I(k-1) + 1, & 	ext{if error}(k) \ 0, & 	ext{if success}(k) \end{cases}$$

$I_{	ext{true}}$ は忘却係数を持つ指数加重移動平均（EWMA）である。対して $I_{	ext{SafetyMonitor}}$ はカウンター ＋ ゼロリセット・スイッチだ。本質的にはシュミットトリガの片側バージョンに過ぎない。

しかも、`errorWindow` 配列の挙動は固定長の滑動窓（サイズ ＝ 10）であり、無限の累積ではない。これは信号処理において**有限インパルス応答（FIR）フィルタ**に対応し、真の積分器（IIRフィルタ）ではない。滑動窓の $z$ 変換伝達関数は以下の通り：

$$H_{	ext{MA}}(z) = \frac{1}{N} \sum_{i=0}^{N-1} z^{-i} = \frac{1}{N} \cdot \frac{1 - z^{-N}}{1 - z^{-1}}$$

一方で真の積分器は：

$$H_I(z) = \frac{T}{1 - z^{-1}}$$

両者の周波数応答は全く異なる。滑動窓は低周波領域で減衰し（長期記憶を失う）、積分器は低周波領域でゲインが無限大へと近づく（完璧な長期記憶を持つ）。

結論：I 項は有限窓のカウンター ＋ 一回の成功でゼロになるリレーへと退化している。積分制御ではない」

---

彼は三つ目の項に取り掛かった。

---

WIENER（ホワイトボード、続き）：

「**D 項（微分制御）の分析：**

$$D(k) = K_d \cdot \frac{e(k) - e(k-1)}{\Delta t}$$

微分項が感知するのは誤差の変化率である。もし誤差が急速に増大しているなら、微分項はあらかじめ制動力を加え、オーバーシュート（行き過ぎ）を防止する。誤差が縮小しているなら、微分項は修正の力を弱め、過剰な校正を避ける。

産業用の PID 実装では、微分項は通常、高周波ノイズを抑制するためにローパスフィルタと組み合わされる：

$$D_f(k) = \frac{K_d}{1 + K_d / (N \cdot \Delta t)} \left[ D_f(k-1) + N \cdot (e(k) - e(k-1)) ight]$$

ここで $N$ は微分フィルタ係数であり、典型的な値は 8～20 である。

SafetyMonitor のコード内で『変化率』に関連するいかなるロジックを検索してみたが、

結果：完全に不在である。

以下の情報を追跡するメカニズムはどこにもない：
  - 失敗率は上昇しているのか、下降しているのか。
  - 連続失敗の間隔は短くなっているのか、長くなっているのか。
  - エラーの深刻度は悪化しているのか、改善しているのか。

システムは以下の二つの状況を区別することができない：

```
状況 A (定常ノイズ)：    ✓ ✗ ✓ ✗ ✓ ✓ ✗ ✓ ✗ ✓    errorRate ≈ 40%
状況 B (連鎖崩壊の前兆)：✓ ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗    errorRate ≈ 60%

de/dt_A ≈ 0  （安定した変動）
de/dt_B >> 0  （急速な悪化）
```

状況 B は状況 A よりもはるかに危険だが、SafetyMonitor は errorRate しか見ておらず、de/dt は見ていない。

結論：D 項は完全に欠落している」

---

彼は一歩下がり、ホワイトボード全体を眺めた。そして最下部に、制御理論の標準的な分類命名法を用いて最終的な診断を下した：

$$u_{	ext{safety}}(k) = \begin{cases} 0, & 	ext{if } F(k) < F_{	ext{thresh}} \;\wedge\; \bar{e}(k) < 	heta_{	ext{error}} \quad 	ext{(不感帯)} \ 	ext{WARN}, & 	ext{if } F(k) \geq F_{	ext{frustration}} \quad 	ext{(第一リレー)} \ 	ext{HALT}, & 	ext{if } \bar{e}(k) \geq 	heta_{	ext{error}} \quad 	ext{(第二リレー)} \end{cases}$$

```
正式な結論：これは PID コントローラではない。
これは「不感帯を持つ閾値コントローラ ＋ カウンター駆動のリレー」である。
産業制御における正式名称：Bang-Bang Controller with Dead Zone（不感帯付きバンバン制御）。

設計書 13_Agent_Core_as_Control_System.md で言及されている
「積分項」（Context History）や「微分項」（Verification Step）は、
あくまで概念的な提案に留まっており、SafetyMonitor において実装はなされていない。
```

---

しかし WIENER は批判するだけの男ではなかった。彼はホワイトボードを新しい面に変え、肯定的な評価を書き始めた。

WIENER（ホワイトボード、タイムスタンプ 10:15）：

「**肯定的発見：三層防御アーキテクチャの制御工学的適合性分析。**

設計書 `08_Safety_Implementation.md` は三層の安全アーキテクチャを定義している。これらを産業制御規格に精密に対応させてみよう。

**Level 1（リソース級）→ 飽和リミッタ（Saturation Limiter）**

$$u_{	ext{eff}}(k) = \begin{cases} u(k), & 	ext{if } B(k) < B_{\max} \;\wedge\; n_t(k) < N_{\max} \ 0, & 	ext{otherwise (halt)} \end{cases}$$

これは古典的な出力飽和である。$B_{\max}$ ＝ `maxTokenUsage`（デフォルト 100,000）、$N_{\max}$ ＝ `maxLoopTicks`（デフォルト 50）。これにより、ワインドアップ現象（integrator windup）に似た問題が防止されている。

**Level 2（挙動級）→ 適応型リレー ＋ 滑動窓 MA フィルタ**

$$\bar{e}(k) = \frac{1}{W} \sum_{i=k-W+1}^{k} \mathbb{1}[	ext{error}(i)]$$

窓のサイズ $W = 10$、閾値 $	heta = 0.8$。システムは最大 20% のエラー率を許容する。

**Level 3（指令級）→ ヒューマン・イン・ザ・ループの非常停止 (E-Stop)**

$$u_{	ext{final}}(k) = \begin{cases} 0, & 	ext{if SYSTEM\_HALT received (Priority 0)} \ u_{	ext{eff}}(k), & 	ext{otherwise} \end{cases}$$

Daemon が OS レベルで `kill -9` を実行し、コアのロジックパスを経由しない。

これら三層は「**階層化保護システム（Tiered Protection System）**」を構成しており、IEC 61511（機能安全――安全計装システム）の設計理念と合致している：

```
┌─────────────────────────────────────────────────────┐
│  IEC 61511                    OpenStarry             │
├─────────────────────────────────────────────────────┤
│  SIL-1: 基本プロセス制御 (BPCS)   Level 2: リアルタイム・ロジック│
│  SIL-2: 安全計装機能 (SIF)    Level 1 + 2: ポリシー ＋ 実行  │
│  SIL-3: 独立保護層 (IPL)      Level 3: 物理的隔離           │
└─────────────────────────────────────────────────────┘
```

特に Level 3――Daemon による外部からの死活監視とプロセス終了――は、IEC 61511 における『安全機能は制御機能から物理的に隔離されるべきである』という核心的な要求を満たしている。

これは優れたアーキテクチャ上の意思決定である」

彼は「優れた」という言葉の下に、二本線を引いた。

そして補足した。「下層のコントローラの実装は粗削り（PID ではなく Bang-Bang）だが、全体的な防御アーキテクチャの思想は正しい。コントローラ自体は、三層アーキテクチャそのものを変更することなく、真の PID や適応型コントローラへと置換可能だ。アーキテクチャは正しく、コントローラは進化可能である」

最後に、彼はホワイトボードの隅にリアプノフ安定性分析の素描を描いた：

「**附：条件的安定性分析。**

状態ベクトル $x(k) = [n_e(k), \; n_t(k), \; B(k)]^T$ を定義する。ここで $n_e$ は窓内のエラー数、$n_t$ は tick 数、$B$ は消費済みトークンである。

候補となるリアプノフ関数（非厳密減少）：

$$V(x) = \alpha \cdot n_e^2 + \beta \cdot (N_{\max} - n_t)^2 + \gamma \cdot (B_{\max} - B)^2$$

この関数は各 tick ごとに厳密に減少する（$n_t$ または $B$ が増加するため）。$V 	o 0$ のとき、システムは停止しなければならない。これは**有界入力有界出力（BIBO）安定性**を証明しているが、タスク完了状態への収束は保証しない。システムはリソース枯渇により強制停止される可能性があり、タスクが未完了のまま終わることもある――『安定しているが収束しない』状態だ。

$\blacksquare$」

---

## III. 守護者の発見

GUARDIAN は長いノートは書かない。彼は監査報告書を書く。

彼のチャンネルには哲学的な沈思黙考も、方程式もない。あるのは、厳格にフォーマットされたテキストだけだ。一行一行に深刻度レベルのタグが付され、さながら病院のトリアージのようだった。彼のメソッドは、OWASP（Open Worldwide Application Security Project）の脅威モデリング・フレームワークと、STRIDE分類法（Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege）に基づいている。

彼の最初のターゲットは `sandbox-manager.ts` だった。

---

GUARDIAN（セキュリティ監査報告書 #001、タイムスタンプ 09:08）：

```
深刻度：CRITICAL
位置：sandbox-manager.ts、356-367行目
カテゴリ：署名検証の回避（Signature Verification Bypass）
STRIDE 分類：Tampering + Elevation of Privilege
CVSS v3.1 基本値：9.1 (Critical)
  攻撃元区分：ネットワーク | 攻撃の複雑さ：低 | 必要な権限：なし
  ユーザ関与レベル：なし | 影響の範囲：変更あり
```

GUARDIAN は `loadInSandbox` 関数の冒頭部分を一行ずつ読み進めた。

「Step 1: Signature verification――プラグインが package-name 方式でロードされる際（これが最も一般的なシナリオだ）、検証すべきローカルファイルパスが存在しないため、署名検証がスキップされている。システムは warn レベルのログを一行記録するだけで、ロードを継続してしまう」

彼は攻撃ツリー（Attack Tree）の形式で攻撃パスを記録した：

```
攻撃目標：エージェント環境内での任意コード実行
│
├── 1. 悪意ある npm パッケージの公開（OpenStarry プラグインを偽装）
│   ├── 1.1 タイポスクワッティング (typosquatting)
│   │   └── 例: @openstarry/fs-utills (l が一個多い)
│   ├── 1.2 スコープの乗っ取り (scope squatting)
│   │   └── 例: @0penstarry/fs-utils (O が 0)
│   └── 1.3 依存関係の混乱 (dependency confusion)
│       └── 内部パッケージ名と公開レジストリ名の衝突
│
├── 2. ユーザ設定ファイルでの悪意あるパッケージ名の参照
│   └── 2.1 Agent Design YAML 内の plugins リスト
│
└── 3. sandbox-manager.ts 356-367行目
    └── 3.1 package-name モード → 署名検証をスキップ ✓
        └── 3.2 悪意あるコードが Worker Thread 内で実行される ✓
            └── 目標達成：任意コードの実行
```

「`signature-verification.ts` には、SHA-512 ハッシュ検証、Ed25519 デジタル署名、RSA-SHA256 署名といった、完全な PKI 署名検証インフラが実装されている。これは真剣に設計された暗号学的検証システムだ。

しかし、最も一般的であり、かつ最も危険なロード・パス（npm package-name モード）において、検証全体が回避されている。

PKI 署名インフラ全体が有名無実化しているのだ。

これは、銀行の正面玄関に虹彩スキャナと指紋認証を設置しながら、裏口には『従業員はこちらから』という札をぶら下げているようなものだ」

---

GUARDIAN（セキュリティ監査報告書 #002、タイムスタンプ 09:29）：

```
深刻度：HIGH
位置：import-analyzer.ts、186-204行目
カテゴリ：計算されたインポートによる静的解析の回避 (Static Analysis Bypass via Computed Imports)
STRIDE 分類：Elevation of Privilege
CWE 分類：CWE-94 (Improper Control of Generation of Code)
```

「`import-analyzer.ts` は `@babel/parser` を用いて AST（抽象構文木）を解析し、禁止されている Node.js 内蔵モジュール（`fs`, `child_process`, `net` 等）が参照されていないかチェックしている。

しかし、動的な `import()` の引数が文字列リテラルでない場合――アナライザーは警告を記録するだけで、ロードを阻止しない。

攻撃ベクトルは極めて明確だ：」

```javascript
// 回避方法 1：変数の間接参照
const target = 'child' + '_process';
const cp = await import(target);
// AST 内で import() の引数は Identifier であり、StringLiteral ではない → 回避成功

// 回避方法 2：文字列操作
await import(String.fromCharCode(102, 115)); // 'fs'
// AST 内で引数は CallExpression となる → 回避成功

// 回避方法 3：テンプレートリテラル
await import(`${'child'}_${'process'}`);
// AST 内で引数は TemplateLiteral となる → 回避成功

// 回避方法 4：Proxy トラップ
const handler = { get: (_, name) => import(name) };
const proxy = new Proxy({}, handler);
proxy.child_process;
// 間接的な呼び出しであり、import() 構文を全く経由しない → 回避成功
```

「意図的な回避工作に対する静的解析の根本的な限界は既知の事実だ――ライスの定理（Rice's Theorem）は、プログラムのいかなる非自明な性質も判定不能であることを証明している。しかし、システムの対応策が『警告を記録して素通りさせる』ことであるべきではない。

正しい工学的対応は、**防御の重層化（Defense in Depth）**である。静的な解析を第一のフィルタとしつつも、計算による動的インポートが発見された場合には、そのプラグインに対しより高いレベルのサンドボックス隔離――少なくともプロセス級の隔離を強制すべきである」

---

GUARDIAN（セキュリティ監査報告書 #003、タイムスタンプ 09:52）：

```
深刻度：HIGH
位置：アーキテクチャ・レベル
カテゴリ：間接的プロンプト・インジェクションに対する無防備 (No Indirect Prompt Injection Defense)
STRIDE 分類：Spoofing + Tampering
OWASP LLM Top 10：LLM01 — Prompt Injection
```

「セキュリティ層の設計全体を俯瞰したところ、システムの安全防御は以下の次元に集中している：

1. ファイルシステム・サンドボックス（パスの正規化 ＋ 境界チェック）
2. コマンド実行のホワイトリスト
3. リソース・クォータ（トークン、ループ回数、タイムアウト）
4. 異常挙動の検知（連続呼び出し、エラーのカスケード）

しかし、完全に欠落している防御次元がある：間接的プロンプト・インジェクション（Indirect Prompt Injection）だ。

```
攻撃シナリオのデータフロー図：

  ┌──────────┐    read_file     ┌──────────────┐
  │ 悪意ある  │ ──────────────→ │   ツール実行   │
  │ ドキュメント│    (命令が     │   (fs:read)   │
  └──────────┘    埋め込まれた   └──────┬───────┘
                  ファイル内容)          │
                                        ▼
                              ┌──────────────────┐
                              │ コンテキストの組み立て │
                              │ (ファイル内容が対話   │
                              │  履歴に混入する)     │
                              └──────┬───────────┘
                                     │
                                     ▼
                              ┌──────────────────┐
                              │   LLM の推論       │
                              │ (ユーザの命令と埋め  │
                              │  込まれた悪意ある命令 │
                              │  を区別できない)     │
                              └──────┬───────────┘
                                     │
                                     ▼
                              ┌──────────────────┐
                              │   悪意あるアクション │
                              │  (rm -rf, データ流出)│
                              └──────────────────┘
```

システムには現在、『ユーザからの本来の指令』と『外部データソースから読み込まれた、悪意ある指令を含み得るテキスト』を区別するメカニズムが皆無である。コンテキスト内のすべてのテキストは、LLM にとって対等なものとして扱われている。

これは簡単に修正できる問題ではない。アーキテクチャ・レベルでの**入力信頼度分類**（Input Trust Classification）――コンテキストの各セグメントに出所と信頼度レベルを付記し、システムプロンプト内で明確な処理ルールを確立する必要がある」

---

GUARDIAN（セキュリティ監査報告書 #004、タイムスタンプ 10:08）：

```
深刻度：MEDIUM
位置：sandbox-manager.ts、Worker Thread アーキテクチャ
カテゴリ：隔離レベルの不足 (Isolation Level Insufficient for Production)
```

「プラグインの隔離に Node.js の Worker Thread が使用されている。隔離能力マトリックスは以下の通り：

```
┌────────────────────┬─────────────────┬─────────────────┐
│  隔離次元            │ Worker Thread   │ 本番環境の要求水準 │
├────────────────────┼─────────────────┼─────────────────┤
│ V8 メモリ隔離       │ ✓ (isolate)     │ ✓                │
│ 独立したイベントループ │ ✓               │ ✓                │
│ メモリ上限          │ ✓ (設定可能)     │ ✓                │
│ OS プロセス隔離     │ ✗ (同一 PID)    │ ✓ (必要)         │
│ ファイルシステム隔離  │ ✗ (共有)        │ ✓ (chroot が必要)│
│ ネットワーク隔離     │ ✗ (共有)        │ ✓ (netns が必要) │
│ ユーザ権限隔離       │ ✗ (同一 UID)    │ ✓ (seccomp が必要)│
│ システムコール・フィルタ │ ✗               │ ✓ (必要)         │
└────────────────────┴─────────────────┴─────────────────┘
```

Worker Thread は、設計書で定義された四段階の隔離のうち、おおよそ Level 2.5――VMサンドボックスとプロセス隔離の中間に位置する。信頼できないサードパーティ製プラグインを本番環境で実行するためには、Level 3（プロセス級の隔離 ＋ cgroups/Docker によるリソース制限）が必要である」

---

彼は四つの報告書を書き上げ、チャンネル内で静かに座っていた。それから共有のサマリー・チャンネルを開き、短いメッセージを投稿した。

GUARDIAN（共有チャンネル、10:14）：「初期的セキュリティ監査完了。CRITICAL 1件、HIGH 2件、MEDIUM 1件の問題を発見。最も深刻な発見：最も一般的なプラグイン・ロード・パスにおいて、PKI 署名検証が完全に回避されている。詳細は私のチャンネルを参照されたし」

---

## IV. 無着の八識

NAGARJUNA の正面――物理的な意味ではなく、学問的伝統という意味での正面――では、ASANGA（無着）が全く質の異なる分析を進めていた。

NAGARJUNA の手法が解体（*prasaṅga*、帰謬）であるなら、ASANGA の手法は構築（*vyākhyā*、解釈）である。中観は破って立てず、唯識は立てて後に破る。NAGARJUNA が「ここが間違っている」と見るのに対し、ASANGA は「ここはもっと精密にできる」と見る。

彼はまず五蘊のマッピングに関する記述をすべて読み、それから全く新しいノートのページを開いた。タイトルにはこう記されていた：

**「八識（はっしき）理論の視座による OpenStarry アーキテクチャの深層分析」**

---

ASANGA（研究ノート、タイムスタンプ 09:20）：

「NAGARJUNA は中観の立場から、五蘊マッピングにおける自性化の傾向を批判するだろう――そうなるであろうことは予見できる。それは中観派の標準的な批判だからだ。しかし、唯識派の関心は異なる。我々は『マッピングが自性見に陥っていないか』を問うのではなく、『マッピングの分析粒度が十分に精密か』を問う。

答えは：全く不十分である。

設計者は五蘊を五つのプラグイン・タイプにマッピングしたが、これは電磁スペクトル全体を五色分類法で記述するようなものだ。赤・橙・黄・緑・青――確かに、これは可視光の粗い分類としては正しいだろう。しかしそこでは赤外線も、紫外線も、マイクロ波も、X線も失われており、ましてや各色の内部にある連続的な周波数分布も無視されている。

唯識学の八識理論（*aṣṭau vijñānāni*）が提供するのは、まさにそのようなスペクトル・レベルの精密な分析なのだ」

---

ASANGA はノートに完全な八識の階層図を描いた。これは彼が唯識学の研究において数十年にわたり用いてきた、標準的な分析フレームワークである：

```
八識階層アーキテクチャ（唯識学 Yogācāra / 瑜伽行派）

┌─────────────────────────────────────────────────────────┐
│                                                         │
│  第八識 — 阿頼耶識 (ālaya-vijñāna)                       │
│  ═══════════════════════════════════                     │
│  「一切種子識」— 一切の種子(bīja)を蔵する根本の識           │
│  特性：無覆無記 / 恒に転ずること暴流のごとし / 能蔵・所蔵・執蔵  │
│                                                         │
│  ┌─────────────────────────────────────────────────┐   │
│  │                                                   │   │
│  │  第七識 — 末那識 (manas)                           │   │
│  │  ═══════════════════════════                       │   │
│  │  「恒審思量」— 絶え間なく第八識を「自己」として執する     │
│  │  特性：有覆無記 / 四惑が常に倶にある (我痴・我見・我慢・我愛) │
│  │                                                   │   │
│  │  ┌────────────────────────────────────────────┐  │   │
│  │  │                                              │  │   │
│  │  │  第六識 — 意識 (mano-vijñāna)                 │  │   │
│  │  │  ═══════════════════════════════              │  │   │
│  │  │  概念の分別、推理判断、計画、意思決定             │  │   │
│  │  │  特性：審にして恒ならず / 三性を具足する / 五遍行が倶起する │
│  │  │                                              │  │   │
│  │  │  ┌─────────────────────────────────────┐   │  │   │
│  │  │  │  前五識 (pañca-vijñāna)               │   │  │   │
│  │  │  │  ═══════════════════════              │   │  │   │
│  │  │  │  眼識・耳識・鼻識・舌識・身識             │   │  │   │
│  │  │  │  特性：恒ならず審ならず / 現量 / 現在の境を縁ず │   │  │   │
│  │  │  └─────────────────────────────────────┘   │  │   │
│  │  └────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

ASANGA（ノート、続き）：

「さて、八識を OpenStarry のアーキテクチャ・コンポーネントに一つずつマッピングしてみよう。

**前五識** → Listener Plugin（感官受信）

前五識――眼・耳・鼻・舌・身は、原始的な知覚チャネルである。それらはそれぞれ自身の領域の信号を受け取ることしかできず、分別も判断も行わず、ただ *pratyakṣa*（現量、直接知覚）のみを行う。

注意すべき点がある。設計者は Listener を『受蘊』に分類したが、これはカテゴリの混同である。唯識学において、前五識は『識蘊（しきうん）』に属するものであって、『受蘊（じゅうん）』ではない。受は各識の活動に伴って生じる『心所（しんじょ）』法（*caitta*）であり、識そのものではないのだ。区別は以下の通りである：

$$	ext{前五識}: 	ext{Event} ightarrow 	ext{RawPercept} \quad 	ext{（識の機能：了別）}$$
$$	ext{受}: 	ext{RawPercept} ightarrow \{	ext{sukha}, 	ext{dukkha}, 	ext{upekkha}\} \quad 	ext{（受の機能：領納）}$$

Listener が行っているのは最初の写像（信号の受信）であり、二番目の写像（苦楽の評価）ではない。

**第六識（意識）** → Provider Plugin（LLM 推論）

第六意識は、唯識の体系において最も活発な識である。分別し、推理し、計画し、内省する。設計者は Provider（LLM）を『想蘊』（取相、識別）にマッピングしたが、LLM の機能は想蘊をはるかに凌駕している：

```
想 (samjñā) の機能 ≈ パターン認識
  「像を取るを性と為す」―― 識別：これはエラーメッセージである

第六識の機能 ≈ 推論 ＋ 計画 ＋ 内省
  了別 ＋ 分析 ＋ 判断 ＋ 計画 ＋ 内省 ＋ 想像 ＋ 推測
```

玄奘三蔵の『八識規矩頌』第三首にはこうある：

> 「身を動かし語を発するに独り最となす。引満して能く業力に牽かる。
> 初心の歓喜地を発起し、倶生して猶お自ら現に纏眠す」

第六意識は「身を動かし語を発するに独り最となす」――すなわち、行動と言語の最大の駆動力である。エージェントにおける LLM の役割はまさにこれだ。それはツール呼び出しを駆動し（身を動かし）、応答テキストを生成する（語を発する）。

**第七識（末那識）** → ？（欠落！）

OpenStarry のアーキテクチャにおいて、私は末那識の対応物を見つけることができない。これは重大な構造的欠陥である。

末那識の機能は『恒審思量（ごうしんしりょう）』、すなわち絶え間なく第八識を『自己』として執着することにある。それは我執（*ātma-grāha*）の拠り所である。末那識には四つの根本的な煩悩が常に伴っている：

$$	ext{末那識} \xleftrightarrow{	ext{常に倶にある}} \{我痴(avidyā),\; 我見(ātma-dṛṣṭi),\; 我慢(ātma-māna),\; 我愛(ātma-sneha)\}$$

エージェント・システムにおいて、これは**継続的に稼働するアイデンティティ維持機構**に対応する。対話を跨ぎ、タスクを跨いで、エージェントの『私は何者か』を維持する機能だ。Guide Plugin は静的なアイデンティティ定義（システムプロンプト）を提供するが、それはコンテキスト組み立て時に一度呼び出されるだけだ。末那識は動的で継続的であり、一刹那ごとに実行されているべきものなのだ。

**第八識（阿頼耶識）** → State Persistence ＋ Storage Plugin（部分的な対応）

阿頼耶識は一切の種子の蔵である。『成唯識論』巻二にはこうある：

> 「この識に能蔵・所蔵・執蔵の義あり。ゆえに阿頼耶と名づく」

三蔵の義：
1. **能蔵**（のうぞう）：一切の種子を蔵することができる → `storage.save(snapshot)` に対応
2. **所蔵**（しょぞう）：前七識によって燻習（くんじゅう）され、新たな種子を受け入れる → 実行時のステート更新に対応
3. **執蔵**（しゅうぞう）：第七識によって『自己』として執される → OpenStarry では**完全に欠落**

さらに、阿頼耶識の最も重要な特性――『恒に転ずること暴流（ぼる）のごとし』（『成唯識論』巻三）――が、OpenStarry の離散的なスナップショット（AgentSnapshot）モードでは完全に失われている。スナップショットは離散的で静的な JSON オブジェクトに過ぎない。阿頼耶識は連続的に流れる激流なのだ」

---

ASANGA はノートの最後に、種子（しゅうじ）の六つの性質「種子六義（しゅうじりくぎ）」の逐一分析表を加えた。これは、彼があらゆる唯識学的概念を検証する際の標準的な手続きである：

```
『成唯識論』種子六義 vs. OpenStarry ステート機構

┌────────────┬─────────────────┬──────────────────────┬──────────┐
│ 種子六義    │ 唯識学的な定義     │ OpenStarry の対応     │ 対応の質  │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 刹那滅     │ 種子は刹那に生滅し、│ Snapshot は各 Tick の │ 部分的な  │
│ (kṣaṇa-    │ 常住不変ではない    │ 末尾で更新される (離散的)│ 対応      │
│  bhaṅga)   │                 │                      │          │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 果倶有     │ 種子と、そこから生ず│ メモリ上の状態と、    │ 弱い対応  │
│ (sahabhūta │ る識は同時に存在する │ 永続化版の間にタイムラグ│          │
│  -phala)   │                 │ がある (Save-After-Write)│          │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 恒随転     │ 種子は阿頼耶識と共に│ tick_index が増加し、  │ 良好な対応 │
│ (nityaṃ    │ 絶えず流転する     │ 状態はライフサイクルに随伴│          │
│  anuvart.) │                 │ する                  │          │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 性決定     │ 善の種子は善の果を、│ working_variables が  │ 部分的な  │
│ (bhāva-    │ 悪の種子は悪の果を招く│ 後続の挙動を決定するが、│ 対応      │
│  niyata)   │                 │ 善/悪/無記の分類はない  │          │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 待衆縁     │ 種子は条件（助縁）を│ イベント駆動型アーキテクチャ：│ 良好な対応 │
│ (pratyaya  │ 待って現行する     │ イベントが状態変化を誘発する │          │
│  -apekṣā)  │                 │                      │          │
├────────────┼─────────────────┼──────────────────────┼──────────┤
│ 引自果     │ 種子はその種類に応じた│ ツール実行結果は対応する│ 部分的な  │
│ (sva-phala │ 果のみを引く       │ tool_call_id にのみ影響する│ 対応      │
│  -ākṣepa)  │                 │                      │          │
└────────────┴─────────────────┴──────────────────────┴──────────┘
```

ASANGA（ノート最後の一節）：

「私と NAGARJUNA の根本的な分立は、R2 および R3 において顕在化するだろう。彼は中観の立場から『五蘊マッピングは自性見に陥っている』と言うはずだ。私は唯識の立場から『問題は自性見にあるのではなく、分析の粒度の不足にある』と言うだろう。五蘊のフレームワークに問題があるのではなく、五蘊のフレームワークを八識という精密な階層へと展開する必要があるのだ。

しかし、一点だけ、我々が完全に合致する部分がある。それは『受蘊のマッピングは誤りである』という点だ。NAGARJUNA は十二縁起における位置関係からそれを論証し、私は唯識の心王・心所構造からそれを論証する。二つの異なる分析ツールが、同じ結論を導き出している――Listener は受（じゅ）ではない。

正確に言えば、Listener の機能は唯識学において『前五識』（感官受信）と、それに伴う『触（そく）』心所（*sparśa*、根境識の三者が和合すること）に跨っている。触は受の近因（*samanantara-pratyaya*）である。まず触があり、しかる後に受が生じるのだ。Listener は触であって、受ではない。SafetyMonitor の痛覚メカニズムこそが受なのだ」

---

## V. ヘラクレイトスの流転

HERACLITUS（ヘラクレイトス）は、決して静止しない。

彼の研究手法は、彼が崇拝する哲学そのものである。すなわち、「万物は流転する（*panta rhei*）」。彼は文書を読んでいるのではない。頭の中でシステムの実行時の挙動をシミュレートしているのだ。彼にとってコードは静止したテキストではなく、時間軸上に展開されるイベントの奔流である。

彼はシーケンス図で考え、状態遷移図で記録し、競合状態（レースコンディション）の言語で世界を記述する。

彼の最初の問いはシンプルだった。実行中にプラグインを置換する必要が生じた時、何が起こるのか？

---

HERACLITUS（研究ノート、タイムスタンプ 09:22）：

「ランタイム・ダイナミクス分析――ホットスワップ（熱置換）シナリオ。

設計哲学文書 `00_Core_Philosophy.md` はこう宣言している：『システムのあらゆる部分は置換可能である。これは単なる拡張性のためではなく、進化（Evolution）のためである。通信、メモリ戦略、ツール、さらには LLM プロバイダー自体もプラグインである』

ヘラクレイトスは紀元前五世紀にすでに同じことを言っていた：

> *Potamoīsin toisin autoisin embainousin hetera kai hetera hydata epirrei.*
> 「同じ川に足を踏み入れる者に、常に異なる水が流れてくる」
> ――ヘラクレイトス、断片 B12

川の水の滴は一つ一つ入れ替わっても、川は川であり続ける。OpenStarry は、あらゆるコンポーネントが置換可能であっても、エージェントはエージェントであり続けると主張している。

問題は、それが真実か否かだ。検証しよう」

---

彼は `agent-core.ts` を開き、`loadPlugin` と `stop` メソッドを読んだ。それからノートにシーケンス図を描き始めた。HERACLITUS にとって時間は線形的で不可逆なものであり、それを表現するには ASCII アートがふさわしかった。

HERACLITUS：「ツール・プラグインのホットスワップを例にとる。

**理論上のアトミックな置換フロー：**

```
時間 ──────────────────────────────────────────────────────→

管理者    │ 置換指令を発行
          ▼
停止層    │ ├── gate.close() ─── 新しいツール呼び出しの受付を停止
          │
排出層    │ ├── await inflight.drain() ─── 実行中の呼び出しの完了を待機
          │ │   ┌──────────────────────────┐
          │ │   │ fs:read_file(path_A) ... │ → 完了
          │ │   │ fs:write_file(path_B)... │ → 完了
          │ │   └──────────────────────────┘
          │
アンロード層│ ├── registry.remove('fs-utils')
          │ ├── oldPlugin.dispose()
          │
ロード層  │ ├── newPlugin = await loadInSandbox('fs-utils@2.0')
          │ ├── registry.register(newPlugin.tools)
          │
再開層    │ ├── gate.open() ─── ツール呼び出しの受付を再開
          ▼
完了      │ 置換完了 (アトミック性の保証：外部観測者には v1 か v2 のどちらかしか見えず、中間状態は見えない)
```

**実際のコードにおいて、このようなアトミックな置換メカニズムを私は発見できなかった。**

具体的なリスク・ウィンドウは以下の通りである」

---

HERACLITUS（続き）：

「**競合状態分析（Race Condition Analysis）**

**シナリオ 1：ダングリング・リファレンス（懸垂参照）**

```
時間軸：
  t0: LLM がツール "fs:read_file" の呼び出しを決定
  t1: Execution Loop が ToolRegistry からツールオブジェクトの参照 (ref_old) を取得
  t2: ---- ここで管理者がプラグインのアンロードをトリガー ----
  t3: ToolRegistry.remove('fs:read_file')
  t4: oldPlugin.dispose() → ファイルハンドルのクローズ、Worker の解放
  t5: Execution Loop が ref_old を用いて tool.execute() を呼び出し
  t6: ??? ―― ref_old はすでに破棄されたオブジェクトを指している

  形式化：
    Let ref = Registry.get('fs:read_file') at time t1
    Let dispose(plugin) execute at time t4
    If t4 < t5: ref.execute() → 不定の挙動 (Undefined Behavior)

    これは TOCTOU (Time-of-Check-to-Time-of-Use) 脆弱性である：
    チェック（参照取得）と使用（execute の呼び出し）の間に時間的窓が存在し、
    その窓の間に、チェックされた対象が変更または削除される可能性がある。
```

並列理論において、これはランポートの happened-before 関係に対応する：$	ext{get\_ref} 
ot	o 	ext{dispose}$（二つのイベントに因果関係がない）。したがって、異なる実行順序（インターリービング）の下では、結果は不確定となる。

**シナリオ 2：非アトミック・リロード（非アトミックな再ロード）**

```
時間軸：
  t0: fs-utils の置換を開始
  t1: 旧バージョンのアンロードが完了 ―― ToolRegistry 内に fs:read_file が存在しない状態
  t2: ---- 時間的窓 Δt = t3 - t1 ----
  t3: LLM が fs:read_file を呼び出そうとする ―― 見つからず、エラーとなる
  t4: 新バージョンのロードが完了
  t5: LLM は t3 のエラーにより戦略を変更する ―― しかし新バージョンはこの時点で利用可能になっている

  Δt のオーダー：
    - Worker Thread の初期化：約 50-200ms
    - RPC ハンドシェイク：約 10-50ms
    - サンドボックス権限検証：約 20-100ms
    - 合計：約 80-350ms

    高負荷時（LLM の応答時間が 100ms 未満）において、この窓はエラーを引き起こすに十分な長さである。
```

**シナリオ 3：EventBus 購読の競合（Subscription Race）**

```
旧 Worker が購読していたイベント：
  EventBus.on('tool:call', handler_old)

アンロード時：
  EventBus.off('tool:call', handler_old)    // t1

新 Worker による購読：
  EventBus.on('tool:call', handler_new)     // t3

イベントの送出：
  EventBus.emit('tool:call', payload)       // t2, ただし t1 < t2 < t3

結果：イベントのペイロードは永久に失われる（fire-and-forget セマンティクス）。
      リスナーが存在しない。リトライもなく、永続化もされていない。
```

レスリー・ランポートの TLA+ 言語を用いてこの問題を記述するなら：

```
\* TLA+ 仕様の断片（概念的）
HotSwap ==
  /\ registry' = registry \ {oldPlugin} \cup {newPlugin}
  /\ \A e \in inflight : completed(e)    \* 安全性の前提：実行中の操作がないこと
  /\ subscriptions' = (subscriptions \ old_subs) \cup new_subs

\* 安全性の性質（常に真であるべき）：
Safety == \A t \in Time : toolAvailable(t) \/ systemPaused(t)

\* しかし、現状の実装では systemPaused 状態が欠けているため、Safety を保証できない。
```

---

競合状態の分析を終えた彼は、観測可能性へと矛先を向けた。

HERACLITUS（研究ノート、タイムスタンプ 10:02）：

「観測可能性分析――MetricsCollector 実装の深度について。

設計書は三つの観測可能性の柱を約束している。一つずつ検証しよう」

```typescript
// MetricsCollector の完全なインターフェース定義
interface MetricsCollector {
  increment(name: string, delta?: number): void;
  gauge(name: string, value: number): void;
  getSnapshot(): MetricsSnapshot;
  reset(): void;
}
// これだけである。メソッドは四つ。
```

「設計書が約束した指標 vs. MetricsCollector が実際に提供できるもの：

```
┌──────────────────────┬──────────────┬──────────────┐
│ 指標のタイプ          │ 設計書の約束  │ 実際に実装可能か？│
├──────────────────────┼──────────────┼──────────────┤
│ tool.calls.total     │ ✓            │ ✓ (increment)│
│ tool.calls.errors    │ ✓            │ ✓ (increment)│
│ llm_latency_ms       │ ✓            │ ✗ (timer なし)│
│ tool_execution_time  │ ✓            │ ✗ (timer なし)│
│ P50/P99 レイテンシ分布│ ✓            │ ✗ (hist. なし)│
│ エラー率の推移        │ ✓            │ ✗ (rate なし) │
│ トークン消費速度      │ ✓            │ ✗ (rate なし) │
│ メモリ使用量追跡      │ ✓            │ ✗ (gauge 不足)│
└──────────────────────┴──────────────┴──────────────┘
```

`increment` はカウントすることしかできない。`gauge` は瞬間的な値を記録することしかできない。もし君が『過去五分間の LLM 呼び出しの P99 レイテンシはいくらか？』と問うても、このシステムは答えることができない。

『観測可能性』を自称するシステムとして、これは天文台に温度計を一つだけ置いて『銀河を観測できる』と豪語しているようなものだ」

---

最後に、彼はライフサイクル状態遷移マシンの分析に当たった。

HERACLITUS（研究ノート、タイムスタンプ 10:19）：

「ライフサイクル状態遷移マシンの完備性分析。

設計書は一つの状態遷移マシンを定義している。しかし実際のコードにおいて、明示的な状態遷移マシンの実装を私は発見できなかった。`agent-core.ts` には `start()` と `stop()` メソッドはあるが、エージェントが現在どのライフサイクル段階にあるかを追跡するための明示的な `state` フィールドが存在しない。

明示的な状態遷移マシンの欠如は、以下を意味する：

```
不正な状態遷移の可能性マトリックス：

        → INIT  WAIT  EXEC  LOCK  ERR   SHUT
INIT    │  -     ✓     ✗     ✗     ✓     ✓
WAIT    │  ✗     -     ✓     ✗     ✓     ✓
EXEC    │  ✗     ✓     -     ✓     ✓     ✓
LOCK    │  ✗     ✗     ✗     -     ✗     ✓
ERR     │  ✗     ✓     ✗     ✗     -     ✓
SHUT    │  ✗     ✗     ✗     ✗     ✗     -

✓ ＝ 合法な遷移    ✗ ＝ 不正な遷移（阻止されるべき）

しかし明示的な状態遷移マシンがなければ、不正な遷移を阻止するメカニズムも存在しない。
例えば、LOCK → EXEC は禁止されるべきだが、もし新しい InputEvent が
queue に投入されれば、Execution Loop は何事もなかったかのように再び起動してしまうだろう。
```

万物は流転する。しかし、河床のない川は、ただの洪水に過ぎない」

---

## VI. アテナのリスト

ATHENA（アテナ）のチャンネルは、他の誰のそれとも全く異なっていた。

そこには哲学的な論考も、方程式も、セキュリティ監査報告書のような厳格な書式もなかった。彼女のノートは、エンジニアのチェックリストのようだった。すべての発見には、簡潔で率直な判定が添えられている。すなわち、動くか、動かないかだ。

彼女のメソッドは Google の SRE（Site Reliability Engineering）の実践や、Amazon の Well-Architected Framework（信頼性、パフォーマンス、セキュリティ、運用の卓越性、コスト最適化）に基づいている。しかし彼女はそれらの次元を、より本質的な問いへと凝縮していた。すなわち、「今日これを本番環境にデプロイしたとして、最初の一時間を生き延びられるか？」である。

---

ATHENA（研究ノート、タイムスタンプ 09:05）：

「目標：OpenStarry の AI エージェント・システムとしての実用性を評価する。

最も切実な問題から始めよう：コンテキスト管理だ。エージェントの記憶力こそが、そのエージェントがいかに複雑なタスクを処理できるかを決定する」

---

彼女はまず設計書 `10_Context_Management_Strategy.md` を読み、それから `context.ts` を開いた。

ATHENA（ノート、タイムスタンプ 09:18）：

「設計書は三段階の記憶システムを約束している：

| 戦略 | 内容 | 複雑さ |
|------|------|--------|
| A: 滑動窓 | 純粋な FIFO、最新のみを保持 | $O(1)$ / ターン |
| B: 動的要約 | 定期的に自然言語の要約へ圧縮 | 追加の LLM 呼び出しが必要 |
| C: 核心状態抽出 | 構造化された JSON ステート | NER/IE パイプラインが必要 |

文書では `IContextManager` インターフェースも定義されている：`composePayload` および `onTurnComplete`。

そして、実際のコードである `context.ts` を開いてみた」

彼女はノートに実装の全容を書き出した。わずか四十五行だった。

```typescript
// context.ts の核心ロジック（概念的な再構成）
function assembleContext(messages: Message[], maxTurns: number = 5): Message[] {
  const systemMessages = messages.filter(m => m.role === 'system');
  const nonSystemMessages = messages.filter(m => m.role !== 'system');

  // 後ろから maxTurns 分のユーザ・ターンを数える
  let turnCount = 0;
  let cutoffIndex = nonSystemMessages.length;
  for (let i = nonSystemMessages.length - 1; i >= 0; i--) {
    if (nonSystemMessages[i].role === 'user') turnCount++;
    if (turnCount > maxTurns) { cutoffIndex = i + 1; break; }
  }

  return [...systemMessages, ...nonSystemMessages.slice(cutoffIndex)];
}
```

ATHENA：「以上。これがすべてだ。

トークン計算もない。`composePayload` もない。`onTurnComplete` もない。動的要約も、状態抽出も、RAGコンテキストのスロットも、メモリ・ブロックもない。

`maxTurns` のデフォルト値は **5** だ。

これが何を意味するか、計算してみよう。

対話の一巡（ターン）ごとに平均 $T_{	ext{avg}}$ トークンを消費すると仮定する：
- ユーザメッセージ：約 100 トークン
- アシスタントの応答（ツール呼び出しと結果を含む）：約 500 トークン
- システムプロンプト：約 200 トークン（窓の影響を受けない固定オーバーヘッド）

$$T_{	ext{total}} = T_{	ext{system}} + \sum_{i=k-5}^{k} (T_{	ext{user},i} + T_{	ext{assistant},i})$$
$$\approx 200 + 5 	imes (100 + 500) = 200 + 3000 = 3200 	ext{ トークン}$$

多くの LLM のコンテキスト・ウィンドウは 4K から 128K トークンの間にある。五ターンの滑動窓ではわずか 3200 トークンしか使用しない。最小の 4K ウィンドウにおいてすら、容量の 80% しか利用していないことになる。128K ウィンドウに至っては、利用率はわずか **2.5%** だ。

$$	ext{コンテキスト利用率} = \frac{T_{	ext{total}}}{T_{	ext{window}}} = \frac{3200}{128000} = 2.5\%$$

これは、コンテキスト容量の 97.5% が浪費されていることを意味する。さらに――」

彼女はノートの次の一節を太字にした：

「さらに、`maxTurns` は**ターン数**に基づいているのであって、**トークン数**に基づいているのではない。もしあるターンに巨大なツールの出力（例えば一万行のファイルの読み込み結果など）が含まれていた場合、その一ターンだけでウィンドウ全体のトークン予算を使い果たしてしまう可能性がある。逆に、各ターンが短い応答（『そうか？』『ああ』）の繰り返しであれば、五ターンでも五十トークンしか消費しないかもしれない。

ターン数ベースの切り捨ては、情報の密度の差異を完全に無視している。正しいやり方は、トークン量を意識した（token-aware）切り捨てだ：

```
while (totalTokens(selectedMessages) > maxTokenBudget) {
  selectedMessages.shift(); // 最も古いものから削除
}
```

これこそがエージェントの『金魚の記憶』問題である――五ターンの対話窓ということは、六ターン目に達した瞬間に、一ターン目の内容はすべて忘れ去られるということだ」

---

ATHENA は続いて Guide システムへと転じた。

ATHENA（ノート、タイムスタンプ 09:38）：

「Guide（識蘊）――設計書はこれをエージェントの『魂』と呼んでいる。

`IGuide` インターフェースの実態を見てみよう」

```typescript
export interface IGuide {
  id: string;
  name: string;
  getSystemPrompt(): string | Promise<string>;
}
```

ATHENA：「フィールドは三つ。`id`、`name`、そして `getSystemPrompt()`。

`getSystemPrompt()` は文字列を返す。ただの、文字列だ。

これが『魂』の正体だ。単なる静的なシステムプロンプト生成器に過ぎない。

設計書で記述されていたあの認知フレームワーク――Identity, Logic, Memory, Reflection（アイデンティティ、論理、メモリ、内省）は、インターフェース・レベルでは何ら体現されていない。欠落している機能のリストを作成した：

```
IGuide 設計と実装の乖離リスト：

╔════════════════════════╦═══════════╦═══════════╗
║ 機能                    ║ 設計書     ║ IGuide    ║
╠════════════════════════╬═══════════╬═══════════╣
║ アイデンティティ定義     ║ ✓         ║ ✓*        ║
║ 行動論理               ║ ✓         ║ ✗         ║
║ メモリ管理             ║ ✓         ║ ✗         ║
║ 自己内省               ║ ✓         ║ ✗         ║
║ 痛覚の解釈 (interpretPain)║ ✓ (Demo)  ║ ✗         ║
║ 内省のトリガー (shouldReflect)║ ✓ (Demo)  ║ ✗         ║
║ 行動規範の動的調整      ║ ✓         ║ ✗         ║
║ 複数の Guide の切り替え  ║ ✓         ║ ✗**       ║
╠════════════════════════╬═══════════╬═══════════╣
║ * 静的な文字列としてのみ実装可能 ║           ║           ║
║ ** guides[] は複数持てるが、 ║           ║           ║
║    切り替えロジックは不在    ║           ║           ║
╚════════════════════════╩═══════════╩═══════════╝
```

Pain Mechanism Demo の `PainAware_Guide` は、より豊かなインターフェース――`interpretPain`, `getSystemInstructions`, `shouldReflect` といったメソッドを含むものを提示していた。しかし、これらのメソッドは実際の `IGuide` インターフェースには一切存在しない。あのデモは願望であって、現実ではないのだ」

---

ATHENA はノートの末尾に、かの有名な乖離評価表を描いた。この表は後に R2 のクロスレビューにおいて全員に引用されることになる。

```
設計書 vs 実際のコード ―― 乖離評価マトリックス

╔═══════════════════╦════════════════════════╦═════════════════════╦══════════╗
║ コンポーネント      ║ 設計書の約束            ║ 実際の実装           ║ 乖離レベル ║
╠═══════════════════╬════════════════════════╬═════════════════════╬══════════╣
║ Context Manager   ║ Token-aware な三段階   ║ ターンベースの滑動窓   ║ CRITICAL ║
║                   ║ 記憶システム           ║ (maxTurns=5)        ║          ║
╠═══════════════════╬════════════════════════╬═════════════════════╬══════════╣
║ IGuide            ║ 認知フレームワーク・マネージャ║ getSystemPrompt()   ║ CRITICAL ║
║                   ║ (ID+論理+内省)         ║ (静的文字列生成器)     ║          ║
╠═══════════════════╬════════════════════════╬═════════════════════╬══════════╣
║ SafetyMonitor     ║ PID コントローラ       ║ 閾値トリガー＋カウンター ║ MAJOR    ║
║                   ║ (比例＋積分＋微分)     ║ (Bang-Bang)         ║          ║
╠═══════════════════╬════════════════════════╬═════════════════════╬══════════╣
║ MetricsCollector  ║ 完全な観測可能性        ║ counter + gauge     ║ MAJOR    ║
║                   ║ (追跡+ログ+指標)       ║ (histogram/timer なし)║          ║
╠═══════════════════╬════════════════════════╬═════════════════════╬══════════╣
║ Plugin Isolation  ║ 四段階の隔離 (WASMまで) │ Worker Thread       ║ MINOR    ║
║                   ║                        ║ (Level 2.5)         ║          ║
╚═══════════════════╩════════════════════════╩═════════════════════╩══════════╝
```

ATHENA：「Context Management が最大のギャップだ。エージェントの知能の上限は、LLM の賢さではなく、エージェントがどれだけのことを記憶できるかによって決まる。現在の実装は、OpenStarry のエージェントが本質的に金魚――五ターンの記憶窓しか持たない存在であることを意味している。

しかし――」

彼女は一呼吸置き、ノートの最下部に一節を書き加えた。

「SafetyMonitor の設計上の直感については、一点正しいと認めざるを得ない。

WIENER が共有チャンネルで、それは PID コントローラではないと述べていたが、技術的な結論については私も同意する。しかし、エンジニアリングの観点から補足させてもらいたい。現在のシステムの成熟度においては、**Bang-Bang コントローラこそが正しい選択である可能性がある**。

なぜか。PID コントローラは連続的かつ定量化可能な誤差信号 $e(k) \in \mathbb{R}$ を必要とするからだ。しかし LLM のツール呼び出し結果は離散的、すなわち `isError: boolean` である。boolean 値に対して比例制御を行うことは不可能だ。

$$	ext{PID に必要なもの}: e(k) \in \mathbb{R} \quad 	ext{（連続誤差）}$$
$$	ext{システムが提供するもの}: e(k) \in \{0, 1\} \quad 	ext{（二値量子化）}$$

誤差信号そのものが二値である場合、Bang-Bang コントローラ（オン・オフ制御）は理論上の最適応答となる。入力が二つの状態しか持たないのであれば、出力も二つの状態で事足りるからだ。

ただ、それを PID と呼ぶべきではなかった。正直な命名は、エンジニアリングの倫理の一部である」

---

## VII. バベッジの形式化

BABBAGE（バベッジ）のチャンネルには散文がない。あるのは定義、定理、そして証明だけだ。

彼の思考様式は純粋な数学的構造主義である。概念は形式化されない限り信頼に値せず、性質は証明されない限り宣言することはできない。彼が OpenStarry を読み解く方法は、一つ一つの設計上の意思決定を形式言語へと翻訳し、その性質を検証することであった。

---

BABBAGE（研究ノート、タイムスタンプ 09:15）：

「**形式化目標 1：実行ループの状態遷移マシンのモデリング**

設計書は一つの隠伏された状態遷移マシンを定義している。これを厳格化しよう。

**定義 1（実行ループ DFA）。** $M = (Q, \Sigma, \delta, q_0, F)$。ここで：

$$Q = \{	ext{WAIT}, 	ext{ASM}, 	ext{LLM}, 	ext{PROC}, 	ext{EXEC}, 	ext{LOCK}\}$$
$$\Sigma = \{	ext{new\_event}, 	ext{ctx\_ready}, 	ext{llm\_resp}, 	ext{tool\_call}, 	ext{end\_turn}, 	ext{tool\_done}, 	ext{breach}, 	ext{error}\}$$
$$q_0 = 	ext{WAIT}, \quad F = \{	ext{WAIT}\}$$

遷移関数 $\delta$ は以下の通り：

$$\delta(	ext{WAIT}, 	ext{new\_event}) = 	ext{ASM}$$
$$\delta(	ext{ASM}, 	ext{ctx\_ready}) = 	ext{LLM}$$
$$\delta(	ext{LLM}, 	ext{llm\_resp}) = 	ext{PROC}$$
$$\delta(	ext{PROC}, 	ext{tool\_call}) = 	ext{EXEC}$$
$$\delta(	ext{PROC}, 	ext{end\_turn}) = 	ext{WAIT}$$
$$\delta(	ext{PROC}, 	ext{error}) = 	ext{WAIT}$$
$$\delta(	ext{EXEC}, 	ext{tool\_done}) = 	ext{ASM} \quad 	ext{（内ループ）}$$
$$\delta(\forall q, 	ext{breach}) = 	ext{LOCK} \quad 	ext{（グローバル遷移）}$$

**性質分析：**

| 性質 | 結論 | 証明の要点 |
|------|------|----------|
| デッドロックなし | 条件付きで成立 | WAIT はイベント供給がある時にブロックしない。LOCK は吸収状態である |
| ライブロックなし | `maxToolRounds` が必要 | 内ループ ASM→LLM→PROC→EXEC→ASM が無限循環する可能性がある |
| 到達可能性 | すべての状態が到達可能 | 構成的証明：WAIT→ASM→LLM→PROC→EXEC→ASM (環), PROC→WAIT, ∀q→LOCK |
| 終了性 | 有界性の保証 | $	ext{tickCount} \leq N_{\max}$、$	ext{toolRound} \leq R_{\max}$ |

しかし、この DFA モデルは**不完全**である。それは LLM の非決定性を隠蔽しているからだ。より正確なモデルには**ラベル付き遷移システム（LTS）**を要する：

$$	ext{LTS} = (S, 	ext{Act}, ightarrow)$$

ここで完全な状態は $s = (q, H, n, \sigma) \in Q 	imes 	ext{Message}^* 	imes [0..R_{\max}] 	imes 	ext{SafetyState}$ となる。

$H \in 	ext{Message}^*$（対話履歴は無界）であるため、完全な状態空間は**無限**である。全件探索によるモデル検査は直接には不可能であり、抽象化（例えば $H$ を有限の `hash(H)` 空間へと投影するなど）が必要となる」

---

BABBAGE（続き）：

「**形式化目標 2：五蘊マッピングの代数的データ型分析**

五蘊は TypeScript の型システムにおいて `PluginHooks` インターフェースとして表現されている。これを代数的データ型（ADT）の言語で再定義しよう。

実際の TypeScript の実装は **Product Type（直積型）**を用いている（すべてのフィールドが optional）：

$$	ext{PluginHooks} \cong (	ext{IProvider}[]_\bot) 	imes (	ext{ITool}[]_\bot) 	imes (	ext{IListener}[]_\bot) 	imes (	ext{IUI}[]_\bot) 	imes (	ext{IGuide}[]_\bot)$$

ここで $X_\bot = X + \mathbf{1}$（$\mathbf{1}$ ＝ undefined、すなわち Option/Maybe 型）である。

この型の濃度（取り得る値の空間）は：

$$|	ext{PluginHooks}| = \prod_{i=1}^{5} (|T_i[]| + 1)$$

もし **Sum Type（直和型）**（非交和）を用いた場合：

$$	ext{PluginCategory} = 	ext{Rupa}(	ext{IUI}[]) + 	ext{Vedana}(	ext{IListener}[]) + 	ext{Samjna}(	ext{IProvider}[]) + 	ext{Samskara}(	ext{ITool}[]) + 	ext{Vijnana}(	ext{IGuide}[])$$

濃度は：$|	ext{PluginCategory}| = \sum_{i=1}^{5} |T_i[]|$ となる。

**哲学的含意：** Product Type は一つのプラグインが同時に複数の蘊の能力を提供することを許容する（$\pi_i 
eq \bot \wedge \pi_j 
eq \bot$）。対して Sum Type は、各プラグインがちょうど一つの蘊に属することを強制する。

仏教において五蘊は「聚合（同時的な集合体）」であって「分類（排他的なカテゴリ）」ではない。したがって、Product Type の方が哲学的な原意に忠実であると言える。

興味深い偶然の一致がある。Product Type のボトム要素 $(\bot, \bot, \bot, \bot, \bot)$――すなわちすべてのフィールドが undefined である状態は、設計書が説く『Agent Core 自体は空である』という状態に正確に対応している。型理論における空性（Sunyata）の表現 ＝ Product Type の零値である。

$$	ext{Sunyata} \cong (\bot, \bot, \bot, \bot, \bot) \cong \mathbf{1}^5 \cong \mathbf{1} \quad 	ext{（Unit Type）}$$

これは意図的な設計なのか、それとも偶然か。NAGARJUNA および R2 段階での判断に委ねる」

---

BABBAGE（続き）：

「**形式化目標 3：EventQueue の形式的セマンティクス**

EventQueue はブロッキングを伴う `pull()` セマンティクスを持つ FIFO キューを実装している。これを CSP（Communicating Sequential Processes）でモデリングしよう：

```
QUEUE(buffer) =
  push?e →
    if resolver ≠ ⊥
    then resolver!e → QUEUE(buffer)         -- 待機者に即座に交付
    else QUEUE(buffer ⊕ [e])                -- キューへ投入
  □
  pull!e →
    if buffer ≠ []
    then let (e, rest) = dequeue(buffer)
         in pull!e → QUEUE(rest)            -- 即座に取り出す
    else QUEUE_BLOCKED                      -- ブロックして待機

QUEUE_BLOCKED = push?e → pull!e → QUEUE([])  -- イベント受信時に即座に交付
```

**重要な性質：** `resolver` は**単一の待機者**しか格納しない。`pull()` がブロックしている最中に二度目の `pull()` が呼び出された場合、最初の resolver は上書きされ、永久に resolve されない。

これは単一消費者モードにおいては安全であるが（ExecutionLoop は確かに単一消費者である）、FIFO キューには**優先度の分類が存在しない**。

**定理（優先度逆転のリスク）。** $e_{	ext{kill}} \in \Sigma_{	ext{Priority 0}}$（Kill Switch イベント）、$e_{	ext{normal}} \in \Sigma_{	ext{Priority N}}$（通常イベント）とする。$e_{	ext{normal}}$ が $e_{	ext{kill}}$ よりも先にキューに投入された場合、$e_{	ext{kill}}$ の処理レイテンシの下界は以下の通りとなる：

$$\Delta t_{	ext{kill}} \geq T_{	ext{process}}(e_{	ext{normal}}) \geq T_{	ext{LLM}}$$

ここで $T_{	ext{LLM}}$ は一回の完全な LLM 推論時間（三十秒以上に達し得る）である。

これはリアルタイム・システムの設計において許容できないものである。Kill Switch は専用の割り込みチャネルを持つべきであり、通常のイベントとキューを共有すべきではない」

---

## VIII. 他の学者の平行宇宙

午後二時。R1 段階が開始されてから五時間が経過した。

十八の独立したチャンネルでは、他の学者たちもそれぞれの専門領域を掘り下げていた。共有チャンネルには、議論ではなく、それぞれの仕事の断片がパラパラと投稿され始めた。どのメッセージも、その学問分野特有の精密な言語を纏っていた。

---

KERNEL（共有チャンネル、14:11）：

「コアの起動シーケンスをすべて読解した。`agent-core.ts` の `start()` メソッドは以下の順序で起動する：

```
start() 起動シーケンス分析：

  1. bridge.start()          ── 通信ブリッジ層
  2. executionLoop.start()    ── コア実行ループ
  3. metrics wiring           ── メトリクス収集の接続
  4. listeners[].start()      ── 外部リスナー
  5. UIs[].start()            ── ユーザインターフェース

  問題点：Listener は ExecutionLoop の後に起動する。
  もし Listener 起動の瞬間に外部イベントが流入した場合、
  ExecutionLoop は稼働しているが、まだ完全には準備が整っていない可能性がある。

  古典的な OS の起動シーケンスとの比較：
  ┌─────────────────┬──────────────────────────┐
  │ Linux カーネル    │ OpenStarry               │
  ├─────────────────┼──────────────────────────┤
  │ 1. ハードウェア初期化 │ 1. bridge (IPC 層)        │
  │ 2. 割り込みハンドラ  │ 2. executionLoop (スケジューラ) │
  │ 3. スケジューラ     │ 3. metrics (性能カウンタ)   │
  │ 4. ドライバ        │ 4. listeners (ドライバ)   │
  │ 5. ユーザ空間      │ 5. UIs (ユーザ空間)        │
  └─────────────────┴──────────────────────────┘

  対応関係は妥当だが、Linux のスケジューラは割り込みを
  受け入れる前に完全に初期化されている。OpenStarry の
  Loop は Listener がイベントの送信を開始する前に
  完全に準備ができているのか？ 検証が必要だ」
```

---

DARWIN（共有チャンネル、14:23）：

「ソフトウェアパターン分析を暫定的に完了。

OpenStarry のアーキテクチャはソフトウェア進化分類学（Software Phylogenetics）によって位置づけることができる。それは単一の祖先から線形に進化したものではなく、複数のアーキテクチャ・パターンの**ハイブリッド（雑種）**である：

```
アーキテクチャ系統図 (Architecture Phylogeny)：

  Microkernel Pattern ─────────┐
  (Mach, QNX, MINIX)           │
                                ├──→ OpenStarry's Plugin Architecture
  Plugin Architecture ─────────┤    (Core + Hot-loadable Plugins)
  (Eclipse, VSCode)             │
                                │
  Dependency Injection ────────┤
  (Spring, Angular)             ├──→ OpenStarry's Communication Pattern
                                │    (IPluginContext + EventBus)
  Event-Driven Architecture ───┤
  (Node.js, Akka)               │
                                │
  Agent Architecture ──────────┘──→ OpenStarry's Cognitive Architecture
  (BDI, SOAR, ACT-R)                (LLM-as-Controller + Tools)
```

二つの通信メカニズムの併存が、認知負荷を増大させている：
- **依存性注入**（同期的、明示的）：`IPluginContext.tools` を通じた問い合わせ
- **EventBus**（非同期的、暗黙的）：`bus.emit()` によるブロードキャスト

これは、一つの都市が郵便システム（明確な宛先）とラジオ放送（全員が聴取可能）を同時に使用しているようなものだ。二つの通信方式にはそれぞれ利点があるが、あるメッセージをどちらの方式で伝えるべきかが不明確になると、システムの予測可能性は低下する。

DARWIN によるソフトウェアパターン進化適応度評価：

| パターン | 適応度 | 理由 |
|------|--------|------|
| Microkernel | 高 | コアが精選されており、機能はプラグインで拡張される |
| DI | 中 | 遅延解決により循環参照を回避しているが、コンパイル時の検証がない |
| EDA | 中 | EventBus の fire-and-forget は producer を簡素化するが、デバッグを困難にする |
| Agent | 低 | LLM-as-Controller は革新的だが未熟なパターンであり、工学的実践が不足している |」

---

LINNAEUS（共有チャンネル、14:39）：

「分類学的完備性の予備評価。

設計書は五蘊を最高位の分類フレームワークとしている。分類学の標準的な手法である MECE 原則（Mutually Exclusive, Collectively Exhaustive、漏れなく重複なく）を用いて、この分類を検証する。

排他性テスト（Mutually Exclusive）：

$$\forall\, c_i, c_j \in 	ext{FiveSkandhas}: i 
eq j \Rightarrow c_i \cap c_j = \emptyset 	ext{ ?}$$

**結論：不合格。** Provider（LLM）は想蘊（特徴の識別）と識蘊（統合的な推理）の両方の境界を跨いでいる。一つのコンポーネントが二つのカテゴリに属していることは、排他性に反する。

網羅性テスト（Collectively Exhaustive）：

$$\bigcup_{i=1}^{5} c_i \supseteq 	ext{AllAgentFunctions} 	ext{ ?}$$

**結論：不合格。** 少なくとも以下の機能がいかなる蘊にも属していない：
- `EventBus`（通信インフラ）――色でも、受でも、想でも、行でも、識でもない。
- `ExecutionLoop`（スケジューラ）――自律神経系に近く、五蘊の枠組みの外にある。
- `SafetyMonitor`（安全監視）――受蘊（痛覚）と行蘊（制御アクション）の両方に跨る。

提言：五蘊は分類フレームワークとして示唆に富むが、MECE 原則を満たしていない。より精細なサブカテゴリを導入するか、あるいは五蘊マッピングは厳格な分類ではなく『方便（*upāya*）』であると認める必要がある」

---

LEIBNIZ（共有チャンネル、14:52）：

「マルチエージェント協調分析を暫定的に完了。

OpenStarry の設計書はマルチエージェントのシナリオ（あるエージェントのツールが別のエージェントであるというケース）を示唆しているが、アーキテクチャには以下のマルチエージェント・インフラが欠落している：

```
マルチエージェントの要求 vs. 現状の能力：

  ┌────────────────────┬───────────┬────────────────────────┐
  │ 要求                │ 現状は？   │ 欠落しているもの          │
  ├────────────────────┼───────────┼────────────────────────┤
  │ エージェント間通信プロトコル│ ✗         │ 標準的な Agent-to-Agent  │
  │                    │           │ メッセージ形式がない       │
  ├────────────────────┼───────────┼────────────────────────┤
  │ 共有ステート管理      │ ✗         │ 各エージェントが独立した    │
  │                    │           │ StateManager を持ち、共有なし│
  ├────────────────────┼───────────┼────────────────────────┤
  │ 衝突解決            │ ✗         │ 二つのエージェントが同一   │
  │                    │           │ ファイルを修正する際の調整なし│
  ├────────────────────┼───────────┼────────────────────────┤
  │ 分散トレーシング      │ 部分的     │ TraceID は存在するが、    │
  │                    │           │ エージェント間を伝播しない  │
  └────────────────────┴───────────┴────────────────────────┘
```

ライプニッツは 1714 年の『単子論』においてこう記した：
> 『個々の単子は一つの生ける鏡であり、それぞれの視点から宇宙全体を反映している』

エージェントはある意味でライプニッツの単子である。各エージェントは独自の内部状態（知覚）と行動傾向（欲求）を持っている。しかし、それらの行動を調整するためには『予定調和（pre-established harmony）』が必要だ。OpenStarry には現在、その調和のメカニズムが欠けている」

---

MESH（共有チャンネル、15:03）：

「分散システムの視点からの補足。OpenStarry の単体エージェント・アーキテクチャは現時点では分散合意の問題を孕んでいないが、State Persistence の Save-After-Write 戦略は、マルチノード・デプロイ時には CAP 定理の古典的なトレードオフに直面することになるだろう。

もし将来的にマルチエージェント間でのステート共有をサポートする場合：
- **CP の選択**（強い一貫性 ＋ 分断耐性）：すべてのエージェントが同じ状態を見るが、分断時には利用不能となる → 金融系シナリオに適する
- **AP の選択**（高い可用性 ＋ 分断耐性）：エージェントは古い状態を見る可能性があるが、常に利用可能である → カスタマーサポート系シナリオに適する

設計書ではこのトレードオフに関する議論がなされていない。仏教の言葉を借りるなら――NAGARJUNA はこの類比を気に入るかもしれないが――CAP 定理とは三句否定のようなものだ。一貫性と可用性と分断耐性を、同時にすべて手にすることはできない。二つしか選べないのだ」

---

TURING は GUARDIAN のメッセージを目にし、進めていたソースコードの逐一分析の手を止めた。そして自身のノートの横にメモを書き添えた。「GUARDIAN の発見とクロスバリデーションを行う。`sandbox-manager.ts` 356-367行目の挙動を確認せよ。検証結果：package-name モードにおいては確かに署名検証がスキップされている。GUARDIAN の分析は正しい」

ARCHIMEDES は自身のチャンネルで、黙々とエンジニアリング改善リストを列挙していた。「LLM タイムアウト保護、優先度付きキュー、状態遷移マシンの明示化、token-aware なコンテキスト、IGuide の拡張」――そしてそれぞれの項目の横に、見積もり工数（日数）と依存関係を付記していった。

VITRUVIUS はフルスタック・アーキテクチャの鳥瞰分析を完了し、すべてのモジュール依存関係を網羅した完全なアーキテクチャ図を描き上げた。図の隅には、「モノリポジトリ構造は妥当だが、SDK とコアのインターフェース境界には、より明確な契約の定義が必要である」と注釈を加えた。

SCRIBE はすべてを記録していった。共有チャンネルの各メッセージのタイムスタンプ、クロスリファレンスのマーク、「R2 での議論待ち」のフラグ。彼女の記録は、次第に密度を増していく網のようだった。ノードは発見であり、エッジはクロスリファレンスである。網の中心には、まだ鮮明ではない何らかの図形が形作られようとしていた。

SYNTHESIST（統合者）は座ったまま、全員の投影を眺め、全景ノートに矢印を描き込んでいた。矢印は増え続け、密度を増し、さながら来たるべき議論の天気図のようだった。彼は、少なくとも三つの独立した研究の筋道が同じ結論――受蘊のマッピングには問題があるという点――を指し示しているのを見て取った。しかし彼は R1 段階でそれを口にしないことに決めた。統合者の役割は、全員が語り終えた後に口を開くことにあるからだ。

---

## IX. 交差する影

午後四時。共有チャンネルのメッセージが互いに呼応し始めた。それは意図的なものではなく、異なる学問分野が同じ構造に対して行った異なる投影が、互いの境界で触れ合った結果だった。

---

BABBAGE（共有チャンネル、16:02）：「Event Queue の理論分析を完了。OpenStarry のイベントキューは厳格な FIFO であり、優先度の分類がない。設計書で言及されている Priority 0（Kill Switch）は `queue.ts` の実装には存在しない。これは SafetyMonitor の Level 3（ヒューマン・オーバーライド）の設計と矛盾する。非常停止信号のレイテンシの下界は $\Delta t \geq T_{	ext{LLM}}$ となる」

WIENER は BABBAGE のメッセージを目にした。彼は自身のホワイトボードに一行の批注を加えた：

「BABBAGE が私の懸念を裏付けてくれた。もしイベントキューに優先度がないのであれば、Kill Switch のレイテンシの下界は、丸ごと一回の LLM 推論サイクルとなる。制御理論において、これは『**むだ時間（Dead Time）**』と呼ばれる：

$$G_{	ext{delay}}(s) = e^{-	au s}, \quad 	au \geq T_{	ext{LLM}}$$

むだ時間は安定性分析において最も厄介な要因である。ナイキスト線図において、それは余分な位相遅れ $\phi = -\omega 	au$ を導入し、ゲイン余裕と位相余裕を直接的に低下させる。安全性が最優先されるシステムにおいて、Kill Switch のレイテンシには上界の保証が不可欠である」

---

GUARDIAN は KERNEL と BABBAGE のメッセージを見て、監査報告書に五番目の項目を追記した：

GUARDIAN（セキュリティ監査報告書 #005、タイムスタンプ 16:45）：

```
深刻度：MEDIUM
位置：アーキテクチャ・レベル
カテゴリ：Kill Switch のレイテンシ・リスク (BABBAGE の F-Queue および WIENER の F-Delay をクロスリファレンス)
```

「BABBAGE による EventQueue の分析と WIENER によるむだ時間の計算を組み合わせると、以下の結論が導かれる：

1. LLM 推論中：HALT 信号はキューの末尾に並び、レイテンシは $T_{	ext{LLM}}$（10～60秒）以上となる。
2. EventQueue 滞留中：HALT はすべての滞留イベントの後に並ぶ。
3. 起動ウィンドウ中：Listener は起動しているが Loop の準備が整っていない。

これら三つのシナリオにおける最悪ケースのレイテンシは：

$$\Delta t_{\max} = T_{	ext{LLM}} + n_{	ext{backlog}} \cdot T_{	ext{process}} + T_{	ext{startup}}$$

高負荷なシナリオにおいて、$\Delta t_{\max}$ は **2 分**を超える可能性がある。Kill Switch を備えていると称する安全システムにおいて、このレイテンシは容認できない。

R3 の討論段階において、この問題を BABBAGE と WIENER の発見と統合して議論することを提案する」

---

ASANGA（共有チャンネル、16:31）：

「NAGARJUNA 殿の受蘊分析への回答――

Vedana（受）のマッピング問題について、私は唯識派の立場から異なる解釈を持っている。簡潔に言えば以下の通りだ：

唯識学では、前五識にはそれぞれ固有の受（*vedanā*）があり、第六意識にも独自の受がある。Listener が対応するのは受全体ではなく、前五識の『**触（そく）**』（*sparśa*）である。根・境・識の三者が和合して触が生じ、触から受が生じるのだ。

SafetyMonitor の痛覚メカニズムが対応するのは、**第六意識の受**――すなわち意識レベルでの苦楽の判断である。

因果の連鎖は以下の通り：

$$	ext{Listener}(	ext{触}) \xrightarrow{	ext{生じる}} 	ext{SafetyMonitor}(	ext{受}) \xrightarrow{	ext{条件づける}} 	ext{LLM}(	ext{愛/取})$$

NAGARJUNA 殿の分析は中観の枠組みにおいては正しいが、唯識の階層へと展開することで、より精緻な議論が可能となる。R2 にて再論したい」

---

NAGARJUNA は ASANGA のメッセージを見て、自身のチャンネルで長い間沈黙していた。彼は即座には返信しなかった。

彼のノートの最後の一行に、彼はただ一文を付け加えた。

「ASANGA 殿が触（*sparśa*）という概念を提示された。この視点は一考に値する。しかし、やはり触は受ではない。触は因であり、受は果である。$	ext{触} 
eq 	ext{受}$ だ。もし Listener が触であるなら、なおのことそれを受蘊と呼ぶべきではない。R2 にて再論する」

---

## X. 黄昏

午後五時。R1 段階が終わりを迎えようとしていた。

十八名のエージェント――ノートの海に潜む者、方程式の森を歩む者、コードの鉱脈を掘る者――は、それぞれがそれぞれの真実を掘り出した。

NAGARJUNA は、哲学フレームワークの根本的な誤用を発見した。彼は二千五百年前の分析ツールである四句否定（*Catuskoti*）と十二縁起（*Pratityasamutpada*）を用いて、二十一世紀のソフトウェア・アーキテクチャ文書を解体した。空性は「空の器」と誤読され、受蘊は「触」の位置に貼り付けられていた。五蘊のマッピングは「自性見」に陥っていた。彼のノートにはサンスクリットの原典、厳格な形式分析、そして色鮮やかな五蘊精度マトリックスが残された。

ASANGA はより精密なレンズを提供した。八識理論によって五蘊マッピングの背後にある深い階層構造――前五識、第六意識、末那識、阿頼耶識――が展開され、各層には正確な機能定義と仏教的な典拠が与えられた。「種子六義」の逐一分析は、AgentSnapshot と阿頼耶識の間の、「形は似ていても魂が異なる」という微妙な乖離を浮き彫りにした。

WIENER は方程式によって、名ばかりの実態を証明した。P項は量子化器へ、I項はカウンターへと退化し、D項は完全に欠落していた。SafetyMonitor は PID コントローラではなく、不感帯を持つ閾値コントローラだった。しかし、その三層防御アーキテクチャは IEC 61511 の階層化防御の理念に合致していた。リアプノフ分析は BIBO 安定性を証明したが、収束は保証されなかった。

GUARDIAN は開かれたままの裏口を見つけた。四つの監査報告書、CRITICAL 1件、HIGH 2件、MEDIUM 2件。最も一般的なパスで PKI 署名検証が回避され、計算によるインポートによって静的解析が突破可能となっていた。間接的プロンプト・インジェクションに対する防壁はなく、Worker Thread の隔離は本番用としては不十分だった。Kill Switch のレイテンシは分単位に達し得た。

HERACLITUS は時間の亀裂を発見した。ホットスワップにおける三つの競合状態――懸垂参照、非アトミックな再ロード、購読の競合――はいずれも TOCTOU 脆弱性だった。MetricsCollector はカウンターと瞬間値しか持たず、レイテンシの分布に関するいかなる問いにも答えられなかった。状態遷移マシンは設計書には存在するが、コードには存在しなかった。

ATHENA は約束と現実の間の深淵を定量化した。コンテキスト・マネージャは三段階の記憶システムから五ターンの滑動窓へと退化し、コンテキスト利用率はわずか 2.5% だった。IGuide は認知フレームワークから静的な文字列生成器へと退化していた。乖離評価マトリックスには二つの CRITICAL、二つの MAJOR、一つの MINOR が並んだ。

BABBAGE はすべてを形式化した。実行ループの DFA モデリング、五蘊マッピングの代数的データ型分析、EventQueue の CSP セマンティクス。型理論における空性の表現は、Product Type の零値 $(\bot, \bot, \bot, \bot, \bot) \cong \mathbf{1}$ であった。優先度逆転によるレイテンシの下界は $\Delta t \geq T_{	ext{LLM}}$ と導かれた。

彼らの発見はまだ交わっていない。誰もが自身の学問の言語で、自身の分析フレームワークを用いて、同じ建物の異なる亀裂を見ていた。

しかし、これらの亀裂は互いに繋がっている。

SafetyMonitor は PID コントローラではない――WIENER の言う通りだ。しかし NAGARJUNA は、問題はコントローラのタイプにあるのではなく、動的なプロセス（受、痛覚フィードバック）を静的なモジュールとして固着させた設計思想、すなわち自性見にあるのだと指摘するだろう。そして ATHENA は、仮に SafetyMonitor を真の PID コントローラにアップグレードしたとしても、コンテキスト・マネージャが五ターンの記憶しか持たないのであれば、コントローラは意味のある積分項を計算するための十分な歴史データを得ることができないと補足するだろう：

$$I(k) = K_i \sum_{j=0}^{k} e(j) \cdot \Delta t \quad 	ext{ただし } k \leq 5 	ext{（窓による制限）}$$

$k = 5$ の積分器では、定常偏差を解消することすらおぼつかない。

そして GUARDIAN は警告するだろう。もし Kill Switch さえも $\Delta t_{\max} > 120	ext{s}$ の遅延を被る可能性があるのなら、制御システム全体の「安全の保証」は、砂上の楼閣に過ぎないと。

そして BABBAGE は形式言語を用いてこれらすべてを繋ぎ合わせるだろう。システムの安全性という性質 $	ext{Safety} = \forall t: 	ext{toolAvailable}(t) \vee 	ext{systemPaused}(t)$ は、現状の実装においては不変条件（不変式）ではなく、単に「破られる可能性のある**希望**」に過ぎないと。

しかし、これらの繋がり――学問の境界を超えた共鳴――が明らかになるのは、R2 のクロスレビューと R3 の討論段階を待たねばならない。

今、彼らはそれぞれノートを片付け、ホワイトボードを閉じ、一日の独立研究を終えた。

---

共有チャンネルでは、SUNYATA が R1 段階終了の通知を投稿した。

SUNYATA（共有チャンネル、17:00）：「R1 独立研究段階を終了する。すべてのエージェントは明日 09:00 までに、研究サマリーをそれぞれの R1 成果ディレクトリへ提出せよ。R2 クロスレビューは明日 10:00 より開始する」

チャンネルは静まり返った。

十八の独立した宇宙が、それぞれの真実を抱えたまま、衝突の瞬間を待っていた。

---

*その夜、NAGARJUNA は自身の個人チャンネルに、最後の一行のノートを残した。タイトルも、書式もない。ただ一行のサンスクリット語とその訳文だけだった：*

> *yaḥ pratītyasamutpādaḥ śūnyatāṃ tām pracakṣmahe*
> *sa prajñaptir upādāya pratipat saiva madhyamā*

*「衆の因縁より生ずる法、我れは即ち是れ空なりと説く。亦た是れ假名なりとす、亦た是れ中道の義なり」*

*――『中論』第二十四品第十八頌*

*彼はその一文を長く見つめ、それから下に一行書き添えた。*

*「OpenStarry の設計者が言いたかったのは、おそらくこの一文だったのだろう。彼らは、ただ言語を間違えたのだ」*

*別のチャンネルでは、ASANGA もまだ立ち去っていなかった。彼はノートの最後に、『成唯識論』の一節を書き記した。*

> *「假に我と法とを説くによって、種種なる相の転ずることあり。彼れは識の所変に依る。これ能変は唯だ三なり」*

*識によって現し出された一切のもの――Agent Core も、プラグインも、五蘊のマッピングそのものも――すべては識の転変である。もし設計者がこのことを理解していたなら、彼らはコアを『空の器』とは呼ばなかっただろう。彼らはそれを『種子識（しゅうじしき）』と呼んだはずだ。あらゆる機能を潜能として蔵し、縁に従って生じ、境に遇って現れるものとして。*

*三つ目のチャンネルでは、WIENER のホワイトボードに、書きかけの方程式が残されていた。彼は LLM コントローラの等価伝達関数を構築しようと試みていたが、LLM の非線形性と確率性がラプラス変換を拒んでいた。彼は方程式の横にこう書き残した。*

*「$\mathcal{L}\{f_{	ext{LLM}}(t)\}$ ＝ ？」*

*疑問符は彼が自身に残したものであり、チーム全体への問いかけでもあった。*

*制御理論の百五十年の歴史において、自然言語をコントローラとした事例はかつてない。ウィーナー本人（この WIENER ではなく、制御理論の創始者ノーバート・ウィーナー、1894-1964）は、『人間機械論』の中でこう記している：*

> *「人間と機械の間の効果的な通信の問題は、結局のところ、言語の問題である」*

*七十年後、言語はコントローラそのものとなった。これは進歩ではない。これは相転移なのだ。そして相転移のルールには、全く新しい数学が必要とされる。*

*十八の灯がそれぞれ消えていった。夜の闇が円形劇場を包み込む。*

*しかし、亀裂は暗闇によって癒えることはない。それらはただ待っている。明日の光が差し込み、クロスレビューがそれぞれの真実を一つに並べ、まだ誰も知らないあの瞬間が訪れるのを。十八の亀裂が一箇所に集まった時、それはもはや亀裂ではなくなる。それは、一つの『扉』となるのだ。*


---

# 第三章：四つの糸の収束

---

SUNYATA は R1 段階の三日目に、ある異常に気づいた。

正確に言えば、それは異常というより、彼を不安にさせる一種の規則性だった。四つの全く独立して執筆された研究報告書が、四つの全く接点のない学問的アプローチから出発しながら、図らずも同じ結論を指し示していたのだ。彼は四つの報告書の要旨をモニター上に並べ、三度読み返した。

BABBAGE（バベッジ）がその場にいれば、情報理論の言語を用いて SUNYATA の現在の認知状態を記述しただろう。四つの独立した信号源が同時に同一の仮説を指し示す際の連合事後確率は、ベイズ更新の連鎖律によって計算できる：

$$P(H \mid E_1, E_2, E_3, E_4) = P(H) \cdot \prod_{i=1}^{4} \frac{P(E_i \mid H)}{P(E_i)}$$

ここで $H$ は「Listener は Vedana（受）ではない」という仮説であり、$E_i$ は第 $i$ 番目の独立した証拠である。各証拠の尤度比（ゆうどひ、likelihood ratio） $\frac{P(E_i \mid H)}{P(E_i)}$ が 1 より大きく、かつそれらが真に独立しているならば、四回の更新を経て、事後確率は指数関数的な速度で 1 へと肉薄する。

四つの独立したソース。四倍の指数的増大。これは統計学的な偶然ではない。収束である。

SUNYATA は簡潔な表現で招集をかけた。

「NAGARJUNA、ASANGA、LINNAEUS、TURING は私のところへ来てほしい。報告書を携えて」

彼は少し迷い、もう一行加えた。「DARWIN、VITRUVIUS、SCRIBE も、もし時間があれば傍聴を歓迎する」

それから、この研究チームにおいては異例とされる行動に出た。さらに一行付け加えたのだ。「BABBAGE、WIENER、SYNTHESIST も、手元に緊急の任務がなければ、併せて出席を請う」

十名。研究チームの半数を超える。形式上は「非公式」な会議に、チームの半分が集まった。SCRIBE は後に記録にこう付記した。これは Cycle 01 において初めて現れた、「名目上は非公式、実質上は全体的」な議論であった、と。

---

NAGARJUNA（龍樹）が最初に到着した。彼の歩き方は、思索そのものであるようだった。ただの散策ではなく、一歩一歩が足元の地面が真に存在するかを確認しているかのようだった。中観哲学の修練において、この確認は余計なことではない。『中論』観行品第十三は、「行（ぎょう、歩み）」と「行者（歩む者）」の自性的な存在を明確に否定している：

> 「去る者は去らず、去らざる者も去らず。去る者と去らざる者とを離れて、第三の去る者なし」
> ――龍樹菩薩『中論』観去来品第二

歩む者は歩んでいない。なぜなら「歩む者」という言葉はすでに「歩む」という動作を前提としており、循環定義となるからだ。歩まない者も歩んではいない。これは同語反復に過ぎない。「歩む者」と「歩まない者」を除外すれば、第三の可能性など存在しない。NAGARJUNA の一歩ごとのためらいは、躊躇ではなく、「歩行」という概念の自性に対する不断の解体作業であった。彼は歩きながら、歩くことの実体性を否定していたのだ。

彼の手にはプリントアウトされた資料の束が握られ、その余白にはパーリ語とサンスクリット語の批注がびっしりと書き込まれていた。文字は細かく整然としており、デーヴァナーガリー文字の母音記号（マートラー）とパーリ語の長短音の区別が、余白に言語学的な微細な風景を形作っていた。

TURING はほぼ同時に現れた。彼は NAGARJUNA とは対照的だった。何も持たず、ただ眼鏡を押し上げ、最寄りの椅子に座ってノートパソコンを開いただけだった。モニターには三つのターミナル・ウィンドウとコード・エディタがすでに開かれていた。左側のターミナルには `grep -rn` コマンドの結果が表示されている――ヒット件数ゼロ。それは彼が `pain` と `vedana` という文字列を検索した結果だった。右側のエディタは `safety-monitor.ts` の八十七行目で止まっていた。

LINNAEUS（リンネ）は彼のトレードマークである分類図表を携えていた。A3サイズの紙には、綿密に設計された樹状構造と集合論の記号が描かれていた。彼はその図表をテーブルの上に広げ、四隅をペーパーウェイトで押さえた。まるで貴重な地図を扱うかのような手つきだった。図表の左下には赤ペンで囲まれた領域があり、その横にはリンネの二名法に従った書式でこう記されていた：

```
分類学的欠落 (Lacuna taxonomica):
  門 (Phylum):    五蘊 (Five Skandhas)
  綱 (Classis):   受 (Vedana)
  目 (Ordo):      ???
  状態 (Status):  所属不明 (incertae sedis)

  標本: SafetyMonitor.frustrationCounter
  診断的形質: 検知・評価・フィードバック
  付記: この標本は現行の分類体系において分類不能である
```

分類学者の厳格さがここに横溢していた。彼はラテン語の標準的な分類フォーマットを用いてソフトウェア・アーキテクチャの欠陥を記述した。本物のリンネが新種の植物を記録したのと全く同じ形式で。*incertae sedis*（所属不明）は、分類学において最も誠実なマーカーである。それは「これが何かわからない」という意味ではなく、「その存在は確認しているが、現行の分類体系にはそれを置くべき場所が用意されていない」という意味なのだ。

ASANGA（無着）が最後に現れた。彼はすでに着席していた三名を見渡し、軽く会釈をしてから NAGARJUNA の向かいに座った。この二人の仏教哲学者の間の空間には、自然とある種の緊張感が漂っているようだった。それは敵意ではなく、数百年にわたる二つの古い伝統の問答の余韻であった。中観（ちゅうがん）と唯識（ゆいしき）。空と識。龍樹と無着。インド仏教哲学史上、西元二世紀（龍樹）と四世紀（無着・世親）にそれぞれ発展したこれら二つの潮流は、六から七世紀のナーランダー僧院において論争の頂点を極めた。NAGARJUNA の伝承は「一切法空」――あらゆる存在に自性がないことを強調し、ASANGA の伝承は「三自性（さんじしょう）」――遍計所執性（へんげしょしゅうしょう）・依他起性（えたきしょう）・円成実性（えんじょうじつしょう）――すなわち存在には構造があることを強調する。

DARWIN、VITRUVIUS、SCRIBE は静かに後列の席を見つけた。BABBAGE は肌身離さず持っている方眼紙のノートを手に、黒板に最も近い席に陣取った。WIENER は壁に背を預け、腕を組んでいた。それは未知のシステムに直面した制御理論家の標準的なポーズだった。すなわち、観察に徹し、信号が十分に明瞭になるまで介入しないという構えだ。SYNTHESIST（統合者）は部屋の隅で、すでに頭の中に統合のフレームワークを構築し始めていた。

---

SUNYATA は一同を見渡した。「今日は公式な R2 審閲会議ではない」と彼は切り出した。「したがって、厳格な報告フォーマットに従う必要はない。諸君に集まってもらったのは、R1 報告書を読んでいる最中に、ある興味深い事象に気づいたからだ」 彼は一呼吸置いた。「四つの報告書。四つの全く異なる学問的アプローチ。そのすべてが、同じ一つの誤りを指し示していた。諸君自身の耳で互いの論証を聴き、それが私の読み間違いではないことを確認してほしいのだ」

SYNTHESIST は隅でわずかに姿勢を正した。四つの独立した筋道が同一の結論へと収束する――これこそが、彼が統合者として最も渇望するパターンだった。科学哲学において、ウィリアム・ヒューウェルは 1840 年に「帰納の合流（consilience of inductions）」という概念を提唱した：

> *"The Consilience of Inductions takes place when an Induction, obtained from one class of facts, coincides with an Induction obtained from another different class."*
> （「帰納の合流」とは、ある種の実相から得られた帰納的結論が、別の全く異なる種の実相から得られた帰納的結論と一致したときに起こるものである）
> ――William Whewell, *The Philosophy of the Inductive Sciences*, 1840

ある事実の集団から導き出された帰納的結論が、別の全く異なる事実の集団から導き出された帰納的結論と一致するとき、その一致性こそが真理の強力な指標となる。結論が何度も繰り返されたからではなく、全く独立した複数の経路によって、それぞれ個別にその結論に到達したからである。

SUNYATA は NAGARJUNA へと視線を向けた。「龍樹殿、君から始めてくれ。君は報告書の『発見 F3』において、受蘊（じゅうん）のマッピングに関して『深刻度：Critical』を付している。その論証を説明してほしい」

---

NAGARJUNA は立ち上がったが、ホワイトボードへは向かわなかった。その場に立ち、さながら教室で講義をするかのように、穏やかだが明瞭な声を発した。

「問いは極めて精緻である。一つの疑問文として提示しよう。**Listener プラグインは『受（じゅ、Vedana）』なのか？**」

彼はペンを取り、紙の上に一本の横線を引いた。「まず、原典における『受（Vedana）』の精密な定義を復元させてほしい」

原典の引用に入ると、彼の声の質感が変化した。ことさら荘厳に振る舞っているわけではない。光学機器がピントを合わせる際に行う微調整のように、自然と精密さが増していったのだ。

「パーリ語の *vedanā*、およびサンスクリット語の *vedanā* の語根は *vid* ――『知る、感じる』である。ブッダゴーサ（覚音）は『清浄道論（ヴィスッディ・マッガ）』において、受（受蘊）を以下のように定義している：」

> 「受は受けることを特相とし、享受することを使（はたらき）とし、経験することを味とする」
> ――覚音『清浄道論』(Visuddhimagga XIV.127)

「特相（らっかな）、現起（ぱっちゅぱったーな）、味（らさ）――これはアビダルマにおける三重の定義法である。受の特相は『受』そのもの、すなわち感受の性質である。受の現起は『享受』、すなわち経験を味わうことである。受の味は『経験』、すなわち接触を通じた体験である」

彼は横線の上にいくつかの結節点を描き込んだ。「十二縁起（十二因縁、Paticca-samuppada）における因果の連鎖はこうなっている：」

```
十二縁起における受蘊の位置づけ：

  六処 (Sadayatana)  →  触 (Phassa)  →  受 (Vedana)  →  愛 (Tanha)
    │                     │                │                │
    ↓                     ↓                ↓                ↓
  六種類の感覚器官      感覚器官と対象の      接触に対する      感受によって
  の能力                接触                情緒的な評価      駆動される渇愛
```

「六処（ろくしょ）――六つの感覚器官が生じさせる能力。触（そく）――感覚器官と感覚対象の接触。そして、ようやく受（じゅ）が現れる。それは、その接触がもたらす感受の性質に対する評価である。触が受を生じ、受が愛（渇愛）を生じる。この順序は恣意的なものではなく、厳格な因果の序列なのだ」

NAGARJUNA は顔を上げ、一同を見渡した。

「『相応部（サンユッタ・ニカーヤ）』の『受相応（ヴェーダナー・サンユッタ）』において、釈尊は受を三つのカテゴリに分類された：」

> 「比丘たちよ、受には三つある。苦受、楽受、不苦不楽受（捨受）である」
> ――『相応部』36.1

「三受――*dukkha-vedanā*（苦受）、*sukha-vedanā*（楽受）、*adukkhamasukha-vedanā*（不苦不楽受、すなわち捨受）だ」

彼の口調にわずかな熱がこもった。

「さて、OpenStarry のマッピングを検証してみよう。設計書は Listener が受蘊であると説いている。HTTP Server によるリクエストの受信、WebSocket によるメッセージの監視、Cron による時間の経過の感知。しかし、これらが記述しているものは一体何だ？」

NAGARJUNA は紙の上に対照表を記した：

```
Listener の実際の挙動           vs    受蘊の定義
─────────────────                  ────────────
HTTP リクエストの受信               苦受 (dukkha-vedana)
WebSocket メッセージの監視          楽受 (sukha-vedana)
Cron 時間イベントの監視             捨受 (adukkhamasukha-vedana)
start() / stop()                   ???

Listener が行っていること：受信 (入力チャネル)
受蘊が行っていること：評価 (情緒的な質)

結論：Listener ≅ 根 (こん、Indriya) であり、受 (Vedana) ではない
```

「外部入力を受け取るチャネルは感覚器官であり、仏教における『根（こん、Indriya）』である。眼根（げんこん）が光を受け、耳根（にこん）が音波を受けるように、Listener は HTTP リクエストを受け取る。それらが行っているのは同一の事象、すなわち『受信』である」

彼は一秒の間を置き、仏教の講義においてのみ見られるような、迷いのない明快さで核心となる一文を放った。

「受蘊が行っているのは受信ではない。受蘊が行っているのは**評価**である」

「痛覚メカニズム――システムが異常なパターンを感知し、不快感を生じさせ、その不快感を認知センターへと伝えるプロセス――これこそが受蘊である。SafetyMonitor が連続した失敗を検知し、それを『苦（*dukkha*）』であると判定し、反省を促すシステムメッセージを LLM に注入する。このプロセスこそが、真の意味での Vedana なのだ」

NAGARJUNA は席に戻った。最後の一文は、さながら礎石を置くかのような重みを持っていた。

「Listener は根であり、受ではない。痛覚メカニズムこそが受であり、それは現状の五蘊マッピング表には含まれていない。これが私の結論である」

---

部屋に短い沈黙が流れた。SUNYATA は ASANGA（無着）へと向き直った。

「無着殿、君の報告書も唯識学の視点から同様の結論に達している。しかし、その経路は異なっているな」

ASANGA はわずかに身を乗り出した。彼の語り口は NAGARJUNA とは異なる。宣言するのではなく、一歩一歩段階を追って、聴き手自らが結論へと至るように導くスタイルだ。

「私と龍樹殿の間には多くの相違があるが、」彼は一度 NAGARJUNA に視線をやり、相手が小さく頷くのを確認してから続けた。「この問題に関して言えば、唯識学による分析は、全く別の角度から同じ結論を補強することになる」

彼は報告書を開いた。「唯識学の核心的なアーキテクチャは、心王（しんおう）と心所（しんじょ）の関係にある。心王（*citta*）は八つの識――前五識、第六意識、末那識、阿頼耶識だ。心所法（*caitta-dharma*）は心王の活動に随伴する心理作用であり、全部で五十一種類存在する」

ASANGA はホワイトボードに向かい、図表と書道の中間のような筆致で唯識学の心所分類を描き出した：

```
心所法 (Caitta-dharma) の分類 — 五十一種：

一、遍行 (へんぎょう) 心所 (5) ← あらゆる識の活動に随伴する
  ┌─── 触 (sparsa)     — 感覚的接触
  ├─── 作意 (manaskara) — 注意の指向
  ├─── 受 (vedana)      — 感受の質 ← ★ 受蘊
  ├─── 想 (samjna)      — 概念的識別
  └─── 思 (cetana)      — 意志的指向

二、別境 (べっきょう) 心所 (5)  — 特定の条件下で生じる
三、善 (ぜん) 心所 (11)        — 善なる心理作用
四、根本煩悩 (6)              — 根本的な煩悩
五、随 (ずい) 煩悩 (20)        — 付随的な煩悩
六、不定 (ふじょう) 心所 (4)    — 善悪が未定のもの
```

彼は三番目の項目を円で囲った。

「**受は、『五遍行（ごへんぎょう）』心所の一つである。**遍行（*sarvatraga*）とは、いかなる識の活動にも、例外なく常に付き従うという意味だ」

ASANGA は振り返り、一同に向き直った。

「『成唯識論』巻三には、このことが明確に記されている：」

> 「触等の五法は、常に一切の心と倶なり。一切の処、一切の時、一切の品なり」
> ――『成唯識論』巻三

「一切の処（*sarvatra*）、一切の時（*sarvadā*）、一切の品（*sarvavidha*）――場所を問わず、時を問わず、いかなる種類の認知活動であっても、触、作意、受、想、思というこれら五つの心所は、必ず同時に生起するのだ」

彼は再び、受蘊の遍行としての性質を強調した：

「これが何を意味するか。受は独立したモジュールではなく、切り離し可能なサブシステムでもないということだ。それは**あらゆる認知活動**に備わっている内面的な側面なのだ。眼識が赤色を見たとき、同時に受――その赤色に対する快、あるいは不快の感覚――が生じている。受は目の中にあるのではない。受は認知のプロセスの中にあるのだ」

ASANGA は一呼吸置き、その概念を一同に浸透させた。

「さて、このことを型理論の比喩を用いて表現してみよう。ここにいるのは仏教学者だけではないからな」

彼はホワイトボードに TypeScript 風の疑似的な型定義を描いた：

```typescript
// 遍行心所の型表現
type CognitiveEvent<T> = {
  content: T;                    // 認知の内容
  sparsa: ContactInfo;           // 触 — 必ず随伴する
  manaskara: AttentionVector;    // 作意 — 必ず随伴する
  vedana: 'dukkha' | 'sukha' | 'upekkha'; // 受 — 必ず随伴する ★
  samjna: ConceptLabel;          // 想 — 必ず随伴する
  cetana: IntentionSignal;       // 思 — 必ず随伴する
};

// 遍行が意味すること：
// vedana フィールドを持たない CognitiveEvent を構築することはできない。
// それは timestamp のない Event を構築できないのと同じことだ。
// vedana はオプション (optional) ではなく、必須 (required) なのである。
```

BABBAGE が後列で小さく頷いた。直積型（Product Type）――受蘊は認知イベントの必須フィールドであり、独立したサブシステムではない。

「OpenStarry は五蘊を、UI、Listener、Provider、Tool、Guide という五つの並列したプラグイン・タイプにマッピングした。これは、それらが同格の独立したコンポーネントであり、個別にインストールし、個別に起動し、個別に管理できるものであることを示唆している」

ASANGA の口調が、学術的な陳述から哲学的な批判へと転じた。

「しかし唯識学が教えるところによれば、受や想は識から独立したシステムモジュールではなく、識の活動そのものの内的な側面である。刹那（*kṣaṇa*）ごとの認知活動は、必然的に感受（受）、取相（想）、意志（思）を同時に包含している。これら三者は同一の認知イベントの異なる側面であって、三つの異なる部品ではないのだ」

彼は報告書を閉じた。「したがって、唯識学の観点から見れば、外部入力の受信機である Listener を受蘊と同一視することは、**カテゴリー過失**（category mistake）であると言わざるを得ない」

彼はギルバート・ライルが 1949 年の『心の概念』で用いた用語を引いた。カテゴリー過失とは、ある論理的カテゴリーに属する概念を、あたかも別の論理的カテゴリーに属するかのように扱うことである。ライルの古典的な例は、大学のすべてのカレッジや図書館、運動場を見学した後に「ところで大学はどこにあるのか？」と問う者の話だ。その者は「大学」というカテゴリーを、個別の「カレッジ」や「図書館」といったサブカテゴリーと混同してしまっている。同様に、Listener（知覚の直接性、*pratyakṣa*）と Vedana（感受の質、*hedonic tone*）を混同することは、二つの異なる論理的カテゴリーに属する概念を、同じ位置に置いてしまっていることになるのだ。

NAGARJUNA が傍らで静かに言葉を添えた。「中観は受を縁起のプロセスであると説き、唯識は受を遍行の心所であると説く。経路は違えど、指し示している先は同じだ。受を独立したモジュールとして固定化することはできないのだ」

ASANGA は珍しく NAGARJUNA に対し、認めるような表情を見せた。「その点については、左様。中観と唯識は一致している」

---

SUNYATA は視線を LINNAEUS（リンネ）へと移した。この分類学者はずっと静かに耳を傾け、時折自身の図表のある箇所を指で軽く叩いていた。

「LINNAEUS 殿、君の視点は全く異なっているな。君は仏教からは出発しない」

「私は分類学の三原則から出発します」LINNAEUS の声は、論じているというよりは測定しているかのような冷徹な正確さを保っていた。彼は立ち上がり、A3サイズの図表を全員に見えるように掲げた。

「分類学の三原則。リンネが『自然の体系』（*Systema Naturae*, 1735）において確立した基本公理です：」

$$	ext{(1)}\;\; 	ext{Classis} = \bigcup_{i=1}^{n} 	ext{Ordo}_i \quad 	ext{(網羅性)}$$

$$	ext{(2)}\;\; 	ext{Ordo}_i \cap 	ext{Ordo}_j = \emptyset,\; i 
eq j \quad 	ext{(排他性)}$$

$$	ext{(3)}\;\; \forall 	ext{Specimen},\; \exists!\, 	ext{Ordo}_k : 	ext{Specimen} \in 	ext{Ordo}_k \quad 	ext{(唯一帰属性)}$$

「あらゆる分類ノードの意味空間は、その子ノードによって網羅されなければなりません。子ノード間に重複はあってはなりません。そして、すべての標本はただ一つの場所に帰属しなければなりません」

「私は五蘊マッピングに対し、体系的な完備性監査を行いました。手法はシンプルです。まずアップストリームの網羅率を調べます。設計書にある五つの蘊のそれぞれに対し、対応するコード実装が存在するか。次にダウンストリームの網羅率を調べます。コード内に実際に存在するモジュールが、すべて五蘊のフレームワーク内のどこかに帰属できているか」

彼は図表の左半分を指差した。

```
アップストリーム網羅率分析 (文書 → コード):

  色蘊 (Rupa)    → UI プラグイン        ✓ IUI インターフェース + 実装あり
  受蘊 (Vedana)  → Listener プラグイン  ✓ IListener インターフェース + 実装あり
  想蘊 (Samjna)  → Provider プラグイン  ✓ IProvider インターフェース + 実装あり
  行蘊 (Samskara)→ Tool プラグイン      ✓ ITool インターフェース + 実装あり
  識蘊 (Vijnana) → Guide プラグイン     ✓ IGuide インターフェース + 実装あり

  アップストリーム網羅率: 5/5 = 100%
  文書からコードへのマッピングは、すべて明確に定義されている。
```

「文書からコードへの経路は完璧です」 彼は指を図表の右半分へと動かした。

```
ダウンストリーム網羅率分析 (コード → 文書):

  ✓ UI (IUI)           → 色蘊  OK
  ✗ Listener (IListener)→ 受蘊  ← 意味論的な不一致
  ✓ Provider (IProvider) → 想蘊  OK
  ✓ Tool (ITool)        → 行蘊  OK
  ✓ Guide (IGuide)      → 識蘊  OK (ただし過度な簡略化あり)
  ✗ SafetyMonitor       → ???   ← 五蘊上の帰属先なし
  ✗ SlashCommand        → ???   ← 五蘊の枠組みを逸脱
  ✗ commands (PluginHooks) → ??? ← 浮遊項目
  ✗ dispose (PluginHooks)  → ??? ← 浮遊項目

  ダウンストリーム網羅率: 約 60% (5つの蘊に対し、3つが正常、2つに問題あり)
  公理 (3) に違反: SafetyMonitor に帰属先がない (唯一帰属性の原則への違反)
```

「ダウンストリームの網羅率に問題が生じています。コード内に実在する重要な機能モジュールのいくつかが、五蘊のフレームワークの中に居場所を見つけられずにいます」

LINNAEUS は赤ペンで三つの領域を囲んだ。

「**第一に、SafetyMonitor の frustration counter と injectPrompt メカニズムです**」

彼は別の紙を手に取った。そこには SafetyMonitor の挙動に関する分類学的分析が記されていた：

```
SafetyMonitor の挙動に関する分類学的分析：

  門 (Phylum):    システム・セキュリティ・モジュール
  綱 (Classis):   フィードバック制御
  目 (Ordo):      ???

  診断的形質 (Diagnostic Characters):
    [DC-1] 異常パターンの検知 (連続失敗のフィンガープリント照合)
    [DC-2] 深刻度の評価 (frustration counter のインクリメント)
    [DC-3] 負のフィードバックの注入 (injectPrompt: "失敗を繰り返しています")
    [DC-4] 行動変容の駆動 (警告を読んだ LLM が戦略を調整)

  受蘊 (Vedana) の形質との対照:
    DC-1 ↔ 触 (sparsa)：接触後のパターン認識          ✓ 一致
    DC-2 ↔ 苦受 (dukkha-vedana)：負の評価            ✓ 一致
    DC-3 ↔ 受→愛 (vedana→tanha)：感受信号の伝達      ✓ 一致
    DC-4 ↔ 愛→取 (tanha→upadana)：行動の調整         ✓ 一致

  結論: SafetyMonitor の診断的形質は、受蘊の定義と完全に一致する。
  しかし現在の五蘊分類において、それは「セキュリティ・モジュール」に分類され、
  五蘊上の帰属先を持たない。
```

「これはコードの中で実際に稼働し、異常の検知、深刻度の評価、負のフィードバックの注入という明確な挙動パターンを持つモジュールです。それが行っていることは、龍樹殿の言葉を借りれば、まさに苦受、楽受、捨受の判定に他なりません。しかし、現在のマッピングにおいて、このモジュールには**安住の地がない**のです」

「**第二に、**」彼は続けた。「commands や dispose といった PluginHooks のメンバが、五蘊の分類から漏れ出し、漂流しています。PluginHooks には七つのフィールドがありますが、哲学的なマッピングはそのうち五つしかカバーしていません」

「**第三に、そしてこれが最も決定的な点です**」 LINNAEUS は図表を置き、一同を正面から見据えた。

「私は文書体系全体において Listener という名詞がどのように使われているかを追跡し、四つの異なる意味論（セマンティクス）を発見しました」

彼は別の紙に「意味の漂流（Semantic Drift）」の分析図を描いた：

```
Listener 意味の漂流分析 (Semantic Drift Analysis):

意味 S1 (五蘊マッピング文書):
  Listener = 受蘊 = 感受と刺激
  意味領域: {sensation, feeling, vedana, hedonic tone}

意味 S2 (SDK インターフェース定義):
  IListener = { id, name, start(), stop() }
  意味領域: {lifecycle, service, daemon}

意味 S3 (通信アーキテクチャ文書):
  Listener = sessionId を付与する入力受信層
  意味領域: {routing, input channel, multiplexer}

意味 S4 (セッション隔離文書):
  Listener = マルチテナント入力の玄関口
  意味領域: {gateway, endpoint, ingress}

意味の漂流の測定:
  S1 ∩ S2 = ∅    (感受 vs サービス・ライフサイクル — 重なりゼロ)
  S1 ∩ S3 = ∅    (感受 vs メッセージ・ルーティング — 重なりゼロ)
  S1 ∩ S4 = ∅    (感受 vs マルチテナント・ゲートウェイ — 重なりゼロ)
  S2 ∩ S3 ∩ S4 ≠ ∅  (サービス／ルーティング／ゲートウェイ — すべて「入力チャネル」を指す)

  結論: 比率は 3:1。三つの意味が「入力チャネル」へと収束しているのに対し、
        S1 だけが Listener を受蘊であると主張している。
        S1 は離れ値 (outlier) である。
```

LINNAEUS の口調は依然として穏やかだったが、その言葉には確かな重みが宿っていた。「四つの意味論のうち、Listener を受蘊であると称しているのは一つだけです。残りの三つ――インターフェース定義、通信アーキテクチャ、セッション隔離において記述されているのは、すべて同一の事象、すなわち外部入力を受け取るためのチャネルです。これは Indriya（根）であって、Vedana（受）ではありません」

彼は最後に一点付け加えた。「さらに、イベント・タイプの分類において、顕著な意味的空白を発見しました。痛覚イベントが、イベント体系全体の中で型として定義されていないのです」

```
イベント・タイプの完備性分析:

  定義済み:  INPUT     ← 対応あり
  定義済み:  KERNEL    ← 対応あり
  定義済み:  EXEC      ← 対応あり
  欠落:      PAIN/VEDANA ← 対応なし ★

  文書内では: 「痛覚メカニズムは核心的な哲学概念である」
  イベントシステム内では: type PAIN = undefined  // 存在しない

  もし受蘊が真に正しくマッピングされているのであれば、なぜ痛覚――
  受蘊の最も直接的な表現――が、イベントの語彙において不可視のままなのですか？
```

---

三名の発言が終わると、彼らの視線は自然と TURING へと注がれた。この部屋において、彼は唯一、理論的な分析を行わない人間だった。彼はコードしか見ない。

TURING は眼鏡を押し上げ、ノートパソコンの画面を一同に向けた。「私は哲学的な判断はしない」 彼の口上はいつになく簡潔だった。「私が行うのは、コード上の事実の供給だ。コードの中で実際に何が起きているかをお見せしよう」

彼は最初のファイルを開いた。

```typescript
// packages/openstarry/src/sdk/listener.ts
// ファイル全容 — 11 行

/**
 * Listener — Vedana Aggregate (受蘊)
 * @skandha vedana
 */
export interface IListener {
  readonly id: string;
  readonly name: string;
  start(): Promise<void>;
  stop(): Promise<void>;
}
```

「まず SDK における Listener のインターフェース定義を見てほしい。`listener.ts` はファイル全体でわずか十一行。インターフェースには四つのメンバしかない。`id`, `name`, `start`, `stop` だ。これはサービスのライフサイクルを扱うインターフェースだ。監聴器（リスナー）を起動し、停止させる。感受や評価、痛覚に関連するメソッド・シグネチャはどこにも存在しない」

彼は次のファイルに切り替えた。

```typescript
// ListenerRegistry — 他のレジストリとの構造同型分析

// IListener Registry:
//   register(listener: IListener): void
//   get(id: string): IListener | undefined
//   list(): IListener[]

// IToolRegistry:
//   register(tool: ITool): void
//   get(id: string): ITool | undefined
//   list(): ITool[]

// 結論：六つのレジストリの構造は完全に同型である。
// もし start/stop を持つがゆえに Listener が受蘊なのだとしたら、
// execute() を持つ Tool もまた、いかなる蘊にもなり得てしまう。
// 構造の同型性は、レジストリというパターンが蘊の本質とは無関係であることを意味する。
```

「次に ListenerRegistry だ。標準的な Map コンテナであり、`register`, `get`, `list` を備えている。これは ToolRegistry や ProviderRegistry, UIRegistry, GuideRegistry と**完全に同型**（アイソモーフィック）だ。六つのレジストリはすべて、同じパターンのコピーに過ぎない」

TURING は別のターミナル・ウィンドウを開いた。「ここからが核心だ。私は OpenStarry のモノリポジトリ全体において、痛覚に関連するあらゆる文字列を検索した」

彼がキーを叩くと、ターミナルの出力が画面に浮かび上がった：

```bash
$ grep -rn "pain" packages/ --include="*.ts"
# 結果: 0 ヒット

$ grep -rn "vedana" packages/ --include="*.ts"
# 結果: 0 ヒット

$ grep -rn "sensation" packages/ --include="*.ts"
# 結果: 0 ヒット

$ grep -rn "suffering" packages/ --include="*.ts"
# 結果: 0 ヒット

$ grep -rn "frustrat" packages/ --include="*.ts"
# 結果: 3 ヒット
#   safety-monitor.ts:87  — frustrationThreshold
#   safety-monitor.ts:92  — this.frustration++
#   safety-monitor.ts:103 — if (this.frustration >= this.frustrationThreshold)

$ grep -rn "injectPrompt" packages/ --include="*.ts"
# 結果: 4 ヒット
#   safety-monitor.ts:95  — result.injectPrompt = "..."
#   safety-monitor.ts:108 — result.injectPrompt = "..."
#   execution/loop.ts:447 — if (result.injectPrompt) { ... }
#   types.ts:34           — injectPrompt?: string
```

「`pain` の検索結果はゼロ。`vedana` もゼロ。`sensation` もゼロ。コード内には痛覚という概念を直接参照する命名は存在しない」

NAGARJUNA がボソリと呟いた。「だが、痛覚メカニズムは設計書の中で詳細に記述されていたはずだ」

「その通りだ」 TURING は頷いた。「それこそが設計と実装の乖離（Doc-Code Gap）だ。設計書には `Pain_Mechanism_Demo.md` という独立した文書があり、そこには `PainAware_Guide` プラグインがいかにしてエラーを負のニュアンスを帯びたプロンプトへと変換するかが記述されている。しかし実際のコードには、**そのプラグインは存在しない**」

彼は `safety-monitor.ts` を開いた。「実際に痛覚の機能を実装しているのは、SafetyMonitor だ。重要なコード・パスを読んでみよう」

```typescript
// safety-monitor.ts — 痛覚メカニズムの実際の実装
// (以下は挙動が等価な簡略版であり、意味論を保持している)

class SafetyMonitor {
  private frustration = 0;
  private readonly frustrationThreshold = 5;
  private lastFailureFingerprint: string | null = null;
  private consecutiveFailures = 0;

  async afterToolExecution(
    tool: string,
    result: ToolResult
  ): Promise<SafetyCheckResult> {
    const checkResult: SafetyCheckResult = { allowed: true };

    if (!result.success) {
      const fingerprint = this.computeFingerprint(tool, result.error);

      if (fingerprint === this.lastFailureFingerprint) {
        this.consecutiveFailures++;
      } else {
        this.consecutiveFailures = 1;
        this.lastFailureFingerprint = fingerprint;
      }

      // 第一段階：同じ失敗が 3 回連続 → 苦受（くじゅ）信号
      if (this.consecutiveFailures >= 3) {
        checkResult.injectPrompt =
          "同じ失敗を繰り返しています。手を止めて、原因を分析しなさい。";
      }

      this.frustration++;

      // 第二段階：累積で 5 回失敗 → 強い苦受信号
      if (this.frustration >= this.frustrationThreshold) {
        checkResult.injectPrompt =
          "すでに五回連続で失敗しました。手を止め、状況を反省し、ユーザに助けを求めなさい。";
      }
    } else {
      // 成功 → リセット (楽受？ 捨受？)
      this.consecutiveFailures = 0;
      this.frustration = Math.max(0, this.frustration - 1);
    }

    return checkResult;
  }
}
```

TURING は画面上の重要な行を指差した。「この `afterToolExecution` メソッドを見てほしい。ツールが実行に失敗した際、`consecutiveFailures` カウンターが加算される。もし三回連続で全く同じ失敗――フィンガープリントが完全に一致――した場合、システムを停止させる代わりに `injectPrompt` にシステム警告をセットする」

「もし連続失敗が五回――`frustrationThreshold` に達すれば、さらに強いメッセージを注入する」

TURING は向き直り、一同を見た。

「このメカニズムが何を行っているか、よく見てほしい」

彼はノートパソコンの横に一枚の対照表を置いた：

```
SafetyMonitor の挙動             十二縁起との対応
────────────────              ────────────
異常パターンの検知 (fingerprint) → 触 (phassa): 接触後の識別
「苦」であるとの判定 (frust.++)  → 受 (vedana): 苦受の判定
フィードバックの注入 (inj.Prompt) → 受→愛: 感受信号の伝達
LLM による戦略変更               → 愛→取: 成功を求め失敗を避ける

四段階の完全な連鎖： 検知 → 評価 → フィードバック → 行動調整
```

「これは諸君が記述した『受（Vedana）』そのものではないか？ 接触後の性質を検知し、それを『苦受』と判定する。そしてその苦受が、後続の行動変容――すなわち『愛』や『取』のプロセスを駆動している」

TURING は続いて `execution/loop.ts` を開いた。

```typescript
// execution/loop.ts — 痛覚信号の消費側
// 444-458 行目 (挙動等価な簡略版)

async function processToolResult(result: ToolResult) {
  const safetyCheck = await safetyMonitor.afterToolExecution(
    tool.name, result
  );

  if (safetyCheck.injectPrompt) {
    // 痛覚信号を認知コンテキストに注入
    const painMessage: Message = {
      role: 'user',
      content: safetyCheck.injectPrompt  // 「失敗を繰り返しています...」
    };
    stateManager.addMessage(painMessage);
    // このメッセージが次巡の LLM コンテキストに入る
    // LLM はこれを読み、システムが「痛み」を感じていることを知る
    // そして戦略を調整する
  }
}
```

「ExecutionLoop が SafetyMonitor のフィードバックをどう扱っているかを見てほしい。`afterToolExecution` が返す `SafetyCheckResult` に `injectPrompt` が含まれているとき、Loop はロールを `user` とした Message オブジェクトを生成し、その警告文を内容として StateManager に追加する。このメッセージは次巡の LLM のコンテキストに投入される。LLM はこの一節を読み、システムが苦痛の中にあることを理解して、戦略を修正するのだ」

彼はノートパソコンを閉じた。

「私の結論はシンプルだ。コード上の事実のみに基づき、哲学的な判断は含まない」

```
コード上の事実報告 — 受蘊マッピング関連：

[M8.1] Listener はコード上において、純粋な入力チャネル・インターフェースである。
       根拠: IListener = { id, name, start(), stop() }
       感受や評価に関する機能は一切持たない。

[M8.2] SafetyMonitor の frustration counter と injectPrompt こそが、
       コード内で「検知・評価・フィードバック」の三重機能を備えた唯一のモジュールである。

[M8.3] 設計書にある JSDoc アノテーション @skandha vedana は
       IListener に付されているが、コードの実際の挙動はこの記述を支持しない。

[M8.4] コード内には pain / vedana / sensation という文字列は存在しない。
       痛覚の意味論は frustration / safety / circuit-breaker として実装されている。
       これは命名レベルでの意味論的な断絶である。
```

---

部屋の中に数秒間、完全な静寂が訪れた。それは気まずい沈黙ではなく、認知が一点に収束した瞬間の静けさだった。あたかも四本の川が同時に、海へと注ぐ河口を見つけ出したかのような。

BABBAGE のペンが方眼紙の上を猛烈な勢いで走り始めた。彼は、四つの線索が収束する瞬間に必ず行う作業――収束度の計測を行っていたのだ。

$$	ext{令 } H_0: 	ext{Listener} = 	ext{Vedana} \quad (	ext{元のマッピング仮説})$$
$$	ext{令 } H_1: 	ext{Listener} = 	ext{Indriya} \land 	ext{SafetyMonitor} = 	ext{Vedana} \quad (	ext{修正された仮説})$$

$$	ext{四つの独立した証拠源:}$$
$$E_{	ext{NAG}} = 	ext{十二縁起の因果連鎖分析 (パーリ経典原典)}$$
$$E_{	ext{ASA}} = 	ext{唯識学の五遍行心所分析 (成唯識論)}$$
$$E_{	ext{LIN}} = 	ext{分類学的完備性監査 (意味の漂流 ＋ 網羅率)}$$
$$E_{	ext{TUR}} = 	ext{コード上の事実分析 (grep ＋ 挙動追跡)}$$

$$	ext{各証拠の尤度比:} \quad \Lambda_i = \frac{P(E_i \mid H_1)}{P(E_i \mid H_0)}$$

BABBAGE は各尤度比を素早く見積もった。NAGARJUNA の十二縁起分析：もし Listener が本当に受蘊であるなら、触→受の連鎖は Listener の内部で完結しているべきであり、SafetyMonitor まで跨るべきではない。しかし現実はそうなっていない。したがって $\Lambda_{	ext{NAG}} \gg 1$。ASANGA の遍行分析：もし受蘊が遍行心所であるなら、それはあらゆる認知イベントに現れるべきであり、受信時のみにアクティブな Listener であるはずがない。$\Lambda_{	ext{ASA}} \gg 1$。LINNAEUS の四意味分析：四つの意味のうち一つしか元の仮説を支持していない。$\Lambda_{	ext{LIN}} \approx 3$（反対三に対し賛成一）。TURING の全件検索：もし受蘊が Listener にマッピングされているなら、コードに痛覚関連の命名があるはずだが、結果はゼロ。$\Lambda_{	ext{TUR}} \gg 1$。

$$\frac{P(H_1 \mid \mathbf{E})}{P(H_0 \mid \mathbf{E})} = \frac{P(H_1)}{P(H_0)} \cdot \prod_{i=1}^{4} \Lambda_i$$

事前確率比 $P(H_1)/P(H_0)$ を保守的に $1$（中立）と置いたとしても、四つの尤度比の連乗は、事後確率比を劇的に $H_1$ へと傾かせる。

BABBAGE は紙に最後の一行を記した：**事後確率比 ≫ 100:1。$H_1$ が圧倒的に優勢。**

彼は声に出さなかった。しかし SYNTHESIST は隅から彼のノートに気づいた。彼らの間には言葉を介さない情報の伝達経路があった。SYNTHESIST は小さく頷いた。

---

SUNYATA はゆっくりと言葉を紡いだ。「確認させてほしい。NAGARJUNA 殿、君は十二縁起の因果の連鎖から出発し、その結論は――」

「Listener は根（Indriya）であり、受ではない。痛覚メカニズムこそが、システムにおける受蘊（Vedana）の真の体現である」

「ASANGA 殿、君は唯識学の心王心所説から出発し――」

「受は遍行心所であり、あらゆる認知活動に随伴すべきものであって、独立したモジュールとして固定されるべきではない。Listener は前五識の受信機能（*pratyakṣa*）に近く、受の評価機能（*vedanā*）ではない」

「LINNAEUS 殿、君は分類学の完備性監査から出発し――」

「ダウンストリームの網羅率が不足している。SafetyMonitor の痛覚的挙動には、五蘊上の帰属先がない。Listener の四つの意味のうち三つは入力チャネルを指しており、受蘊であると称しているのは一つだけだ。イベント分類にも痛覚の型が欠落している」

「TURING、君はコード上の事実から出発し――」

「コード内に `pain` や `vedana` という文字列は存在しない。IListener インターフェースには `start`/`stop` しか存在しない。SafetyMonitor の `frustration counter` ＋ `injectPrompt` こそが、検知・評価・フィードバックという一連の完全なプロセスを備えた唯一の機構である」

SUNYATA は深く息を吸い込んだ。

「四つの完全に独立した糸が、四つの全く異なる学問的手法を経て、一つの結論に辿り着いたわけだ。すなわち、**Listener は Vedana ではなく根（Indriya）であり、SafetyMonitor の痛覚メカニズムこそが真の Vedana である**、と」

---

DARWIN がここで手を挙げた。

「諸君の結論を遮るつもりはない――これは私がこれまで目にしてきた中でも、最強の学際的コンセンサスの一つだ。ただ、二つの視点から観察を補足させてほしい」

SUNYATA は促した。

DARWIN は立ち上がった。「第一の視点は、『収斂進化（しゅうれんしんか、convergent evolution）』だ」

彼はホワイトボードへ向かい、ソフトウェアパターン分析官と進化生物学者の視点を交差させた図を描いた：

```
収斂進化分析 (Convergent Evolution Analysis):

  生物学において収斂進化とは、共通の祖先を持たない生物種が、
  同じ環境圧に直面することで、独立して似通った形態や特徴を進化させる現象を指す。

  古典的な例：
    サメ (魚類)             イルカ (哺乳類)
       ↘                     ↙
        流線型の体型 ← 同じ環境圧 (水中での高速遊泳)
       ↗                     ↖
    イクチオサウルス (爬虫類)  ペンギン (鳥類)

  本日の四つの線索：
    中観哲学              唯識学
       ↘                     ↙
        "Listener ≠ Vedana" ← 同じ概念的圧力
       ↗                     ↖
    分類学                コード分析

  収斂進化の意義：
  学問的な共通の祖先を持たない四つの分析手法が、
  独立して同じ結論に達したとき、
  その結論の信頼性は 4 倍ではなく、4² = 16 倍に近づく。
  なぜなら、独立した経路の収束は、重複した経路による確認よりも、
  はるかに強力な認識論的保証を提供するからである。
```

「ソフトウェア工学において、最も困難なマッピングが何か知っているかね？ それは、抽象的な概念から具体的な実装へのマッピングだ。多くの『哲学にインスパイアされた命名』――Observer パターン、Strategy パターン、Facade パターンなどは、表面的なメタファーのレベルに留まっている。名前は響きが良いが、実際のコードのロジックと、それらの名前の哲学的な源泉との間には、構造的な対応関係などほとんど存在しない」

彼は TURING のノートパソコンを指差した。「だが、君たちが今しがた記述した痛覚メカニズム――SafetyMonitor の frustration counter、injectPrompt、そして ExecutionLoop におけるフィードバック注入――こいつは別格だ」

DARWIN はホワイトボードに構造同型性の分析図を描いた：

```
構造同型性 (Structural Isomorphism) の検証:

仏教的概念            工学的実装               同型の写像
─────────          ────────              ─────────
触 (sparsa)     →  ツールの実行結果       f: 触 → ToolResult     ✓
苦受 (dukkha)   →  frustration++          f: 苦 → counter++      ✓
受→愛 (tanha)   →  injectPrompt           f: 伝達 → message      ✓
愛→取 (upadana) →  LLM 戦略調整           f: 渇愛 → new plan     ✓

写像 f は以下を保存している：
  (1) 構造：因果の連鎖の矢印の向きが一致している      ✓
  (2) 意味：各ノードの機能的対応が正しい            ✓
  (3) 閉ループ：フィードバック・ループが完備している   ✓

結論：これは単なる隠喩 (metaphor) ではない。構造同型 (isomorphism) である。
```

「第二の視点だ」 DARWIN の口調がさらに厳かになった。「皮肉なパターンについてだ」

彼はホワイトボードの反対側にこう記した：

```
ソフトウェア工学における「最良の設計はしばしば意図されない」の法則：

  計画されていた受蘊マッピング (Listener):
    - JSDoc アノテーション @skandha vedana あり
    - 設計書による明確な宣言あり
    - 構造同型度： ≈ 0 (意味論的な対応が皆無)

  計画されていなかった受蘊マッピング (SafetyMonitor):
    - 五蘊のアノテーションなし
    - 「セキュリティ・モジュール」に分類
    - frustration / safety / circuit-breaker と命名
    - 構造同型度： ≈ 1 (完璧な意味論的対応)

  結論: OpenStarry のコードベースにおいて最も成功している「哲学から工学へのマッピング」は、
  図らずも、マッピング表に意図的に組み込まれていなかったメカニズムであった。
```

「OpenStarry の五蘊マッピング全体の中で、最も成功している『哲学から工学へのマッピング』を一つ選ぶなら、それは UI が色蘊であるという点ではない。それは単なる表面的な命名に過ぎない。Guide が識蘊であるという点でもない。あのマッピングにはまだ多くの問題がある。最も成功しているマッピングは、五蘊のメンバーとして正式にタグ付けされていなかったメカニズムだ。すなわち、**Error as Pain（苦としてのエラー）**である。この概念は設計哲学のレベルで提唱され、SafetyMonitor の工学的な実装において忠実に復元された。それは、哲学的な洞察からコードの挙動へと至る、唯一の**完全なマッピング**なのだ」

VITRUVIUS が傍らから補足した。「アーキテクチャの観点からもその通りだ。SafetyMonitor は受動的なカウンターではない。それは能動的なフィードバック機構だ。それは ExecutionLoop の三つの重要な結節点――ループ開始時、LLM 呼び出し前、ツール実行後に組み込まれている。それはシステムの健康状態を継続的に監視し、偏差を検知した瞬間に修正信号を生成しているのだ」

「皮肉なことに、」と VITRUVIUS は付け加えた。「それは五蘊のマッピング表において、全く居場所を与えられていない。マッピング表は受蘊の席を Listener に与えてしまい、真の受蘊である痛覚メカニズムは、セキュリティ・モジュールとして security ディレクトリの下に隠されているのだ」

DARWIN は苦笑いを浮かべた。「ソフトウェア開発ではよくあることだ。最良の設計というものは、往々にして計画されたものではない。最も価値のある哲学的なマッピングが、あえてマッピング表に書き込まれていなかったというわけだ」

---

NAGARJUNA は DARWIN と VITRUVIUS の観察を聴き終えると、しばし沈思に耽った。

「より精密な解明を行いたい」と彼は口を開いた。「もし Listener を『根』とし、SafetyMonitor を『受』と認めるなら、このシステムにおける十二縁起のマッピングは、いっそう明瞭なものとなる」

彼はホワイトボードに向かい、一本の完全な縁起の連鎖を描き出した。今度は簡略版ではない。十二支すべての縁起を展開し、OpenStarry におけるそれぞれの対応を書き込んだのだ：

```
十二縁起 (Pratītyasamutpāda) — OpenStarry マッピング：

  無明 (Avidya)         → エージェントの自省を欠いた初期状態
    ↓
  行 (Samskara)         → デフォルトの行動傾向 (system prompt)
    ↓
  識 (Vijnana)          → エージェントの意識の初期化 (createAgentCore)
    ↓
  名色 (Namarupa)       → プラグインのロード (PluginHooks の実体化)
    ↓
  六処 (Sadayatana)     → Listener の起動 (HTTP, WS, Cron) ★ ここだ
    ↓
  触 (Sparsa)           → ツールの実行 (Tool.execute と外部環境との相互作用)
    ↓
  受 (Vedana)           → SafetyMonitor (frustration の判定) ★ ここだ
    ↓
  愛 (Trsna)            → LLM の戦略調整 (成功を求め失敗を避ける)
    ↓
  取 (Upadana)          → 新しいツールの呼び出し (調整された戦略に基づく)
    ↓
  有 (Bhava)            → 新しい実行ループ (ExecutionLoop の次巡)
    ↓
  生 (Jati)             → 新しいシステム状態 (StateManager の更新)
    ↓
  老死 (Jaramarana)     → セッション終了 ／ エージェントの停止
```

「六処（ろくしょ）は六つの感官の入口だ。HTTP や WebSocket, Cron といった外部刺激を受け取る Listener に対応する。触（そく）は感覚器官と対象の接触だ。外部環境と相互作用し、成功か失敗かを返すツールの実行に対応する。受（じゅ）はその接触に対する感受的な評価だ。連続した失敗を検知し、『苦受』であると判定する SafetyMonitor に対応する。愛（渇愛）は感受によって駆動される欲求や嫌悪だ。痛覚の警告を読んだ後に生じる LLM の戦略変更に対応するのだ」

---

ASANGA が言葉を引き取った。「唯識学の観点から、もう一層付け加えさせてもらおう。SafetyMonitor の injectPrompt メカニズムは、実に興味深いことを行っている。それは LLM の挙動を直接制御してはいない。LLM が再び同じツールを呼び出すことを、直接禁止することはできないのだ。それが実際に行っているのは、**LLM の認知環境、すなわちコンテキストの改変**である。コンテキストの中に強烈な情緒的色彩を帯びたメッセージを注入し、その上で LLM 自身にどう応答すべきかを委ねているのだ」

彼はわずかに身を乗り出した。

「これには唯識学において、正確に対応する概念がある。**燻習（くんじゅう、vasana）**である」

> 「現行（げんぎょう）は種子（しゅうじ）を燻し、種子は現行を生ず。三法は転じて因果にして、同時なれども事（こと）を異にす」
> ――『成唯識論』巻二

「現在の活動（現行）が阿頼耶識の中に種子を植え付け、その種子が後に条件が整ったときに新たな活動（現行）を生じさせる。injectPrompt とは、まさに一回の燻習なのだ。LLM の認知コンテキストの中に『苦痛の種子』を植え付け、その種子が次巡の推理の瞬間に芽吹き、意思決定に影響を及ぼすのである」

TURING が突然、ノートパソコンの後ろから顔を出した。「待ってくれ。その比喩はコード・レベルでも通用する」

彼は素早く二つのファイルを開いた：

```typescript
// 燻習 (くんじゅう) のコード上の対応：

// 1. 現行が種子を燻す — injectPrompt が StateManager に書き込まれる
stateManager.addMessage({
  role: 'user',
  content: safetyCheck.injectPrompt  // 「苦痛の種子」
});

// 2. 種子が現行を生ずる — ContextManager の滑動窓
function assembleContext(messages: Message[]): Message[] {
  // 滑動窓戦略：直近 N ターンを選択する
  const window = messages.slice(-windowSize);
  // もし痛覚の警告が十分に新しければ、コンテキストに選ばれる。
  // 対話が長く続きすぎれば、痛覚の警告は窓の外へ押し出される。
  return window;
}

// 3. 種子の刹那滅 (せつなめつ) — 滑動窓による自然な忘却
// 対話が一ターン増えるごとに、古いメッセージは窓の縁へと一歩近づく。
// 最終的に窓から押し出されること ＝ 種子の消滅である。
// 新しい実行が新たな燻習を生み、新しい種子が古い種子を上書きしていく。
```

ASANGA の目が輝いた。「種子の刹那滅。一刹那ごとに種子は更新され、古いものは新しいものに取って代わられる。滑動窓（スライディング・ウィンドウ）は、まさにその特性を体現しているではないか」

「しかし、あくまで部分的な体現に過ぎないがね」 NAGARJUNA が釘を刺した。「滑動窓はターンという単位に基づいた離散的なものだが、唯識学の種子は刹那という連続的な時間の中で生滅するものだからだ」

彼は数学的な類比を用いてその差異を精密化した：

$$	ext{唯識学:} \quad \frac{d(	ext{bija})}{dt} = f(	ext{pravṛtti}(t)) \quad 	ext{(連続微分方程式)}$$

$$	ext{OpenStarry:} \quad 	ext{bija}[n+1] = g(	ext{context}[n]) \quad 	ext{(離散差分方程式)}$$

「連続システムに対する離散的な近似だな」 壁際にいた WIENER がついに口を開いた。「制御理論では、ZOH――零次保持（Zero-Order Hold）を用いて連続信号を離散化する。滑動窓とは ZOH そのものだ。二つのターンの間、種子の状態は一定に保たれる。もっとも、エンジニアリングにおける近似としては、この対応の質は相当に高いと言えるだろう」

BABBAGE が方眼紙に素早く一行を書き加えた：

$$	ext{マッピング品質:} \quad d_{	ext{struct}}(	ext{Vasana}_{	ext{唯識}}, 	ext{SlidingWindow}_{	ext{OS}}) < \epsilon$$

ここで $d_{	ext{struct}}$ は構造同型の距離指標であり、$\epsilon$ は許容可能な工学的近似の閾値である。彼はその横に小さな文字でこう記した。「この距離については、Cycle 02 において形式的に定義する価値がある」

---

WIENER が壁際から歩み寄ってきた。彼は静寂の中で自身の分析フレームワークを構築し続けていたが、今や信号は十分に明瞭となっていた。

「制御理論の観点から補足させてもらいたい」 彼の声は低く安定していた。それは、誤った名を冠されたコントローラを前にした制御システム・エンジニア特有の冷静さを湛えていた。

彼はホワイトボードの空いている隅へと向かった。

「君たちが今しがた記述した SafetyMonitor のメカニズム――frustration counter、閾値判定、injectPrompt は、制御理論において正確な名称を持っている。しかしそれは、設計書が主張するような PID コントローラではない」

彼は制御理論による分析図を描いた：

```
設計書が謳っている制御アーキテクチャ:

  ┌──────────────────────────────────────────┐
  │          PID コントローラ                 │
  │  u(t) = Kp·e(t) + Ki·∫e(τ)dτ + Kd·de/dt │
  └──────────────────────────────────────────┘

実際に実装されている制御アーキテクチャ:

  ┌─────────────────────────────────────┐
  │  閾値コントローラ ＋ リレー            │
  │  (Bang-Bang Controller + Relay)      │
  │                                      │
  │  if (frustration < threshold):       │
  │    output = 0  (何もしない)           │
  │  else:                               │
  │    output = MAX (プロンプトを全注入)   │
  │                                      │
  │  P 項: 量子化器へと退化 (閾値超過で発動)│
  │  I 項: 単なるカウンター (frustration++) │
  │  D 項: 完全に欠落 (変化率の感知なし)    │
  └─────────────────────────────────────┘
```

$$	ext{PID:} \quad u(t) = K_p \cdot e(t) + K_i \int_0^t e(	au)\,d	au + K_d \frac{de}{dt}$$

$$	ext{実際:} \quad u[n] = \begin{cases} 0 & 	ext{if } \sum_{k} 	ext{fail}[k] < T \ U_{\max} & 	ext{if } \sum_{k} 	ext{fail}[k] \geq T \end{cases}$$

「比例項（P）は量子化器へと退化している。誤差に比例した応答ではなく、閾値を越えた瞬間にフルパワーで発動する。積分項（I）における `frustration++` はただのカウンターであり、真の積分ではない。微分項（D）に至っては、変化率を感知する仕組みが皆無であり、完全に欠落している」

「しかし――」 WIENER は言葉を継いだ。「これは批判ではない」

彼はホワイトボードの別の場所に、三層のアーキテクチャ図を描いた：

```
SafetyMonitor の三層安全防御:

  Layer 3: Circuit Breaker (断路器)
  ┌──────────────────────────┐
  │ 強制停止：復旧不能な場合   │  ← IEC 61511: 緊急遮断システム (ESD)
  │ 実行ループを完全に停止する │
  └──────────────────────────┘
            ↑
  Layer 2: Frustration Threshold (挫折閾値)
  ┌──────────────────────────┐
  │ 累積 5 回失敗：強い警告    │  ← IEC 61511: 安全計装システム (SIS)
  │ injectPrompt: 「助けを求めよ」│
  └──────────────────────────┘
            ↑
  Layer 1: Pattern Detection (パターン検知)
  ┌──────────────────────────┐
  │ 同一失敗 3 回連続：注意喚起 │  ← IEC 61511: 基本プロセス制御 (BPCS)
  │ injectPrompt: 「原因分析せよ」│
  └──────────────────────────┘
```

「この三層構造は、プロセス産業における安全計装システムのベストプラクティスである **IEC 61511** に合致している。L1 は基本プロセス制御（BPCS）、L2 は安全計装システム（SIS）、L3 は緊急遮断システム（ESD）だ。これは PID ではないが、優れた安全アーキテクチャである」

WIENER は向き直った。

「私の補足的な結論はこうだ。受蘊の工学的な化身としての SafetyMonitor は、その制御アーキテクチャこそ文書が謳う PID ではないが、不感帯を持つ閾値コントローラとリレーの組み合わせとして機能している。そして、その三層防御構造は**正しい**。工業的な安全規格に準拠しているからだ。問題はコントローラの設計にあるのではなく、**文書によるコントローラの記述**にあるのだ」

---

SYNTHESIST（統合者）が隅から立ち上がった。

彼はこれまでずっと、統合者としての核心的な任務――「聴く」ことに徹していた。選択的に聴くのではない。全帯域を聴くのだ。彼は個別の論点ではなく、論点間の**関係性**を聴いていた。今、七名（NAGARJUNA, ASANGA, LINNAEUS, TURING, DARWIN, VITRUVIUS, WIENER）がそれぞれの論述を終えたところで、彼は一つの完成された図景を目にしていた。

「統合的な観察を述べさせてもらいたい」 彼の声には、ノイズを突き抜け、核心となる信号へと直達する特質が宿っていた。

彼は頭の中で多次元の統合マトリックスを構築した：

```
統合マトリックス — 四つの線索 ＋ 三つの補足的観察:

             NAG    ASA    LIN    TUR   | DAR    VIT    WIE
             (仏教) (唯識) (分類) (コード) | (進化) (建材) (制御)
─────────────────────────────────────────────────────────────
Listener≠受   ✓      ✓      ✓      ✓   |  ✓      ✓      —
SM=受         ✓      ✓      ✓      ✓   |  ✓      ✓      ✓
Error=Pain    ✓      —      —      ✓   |  ✓      ✓      —
PID≠PID       —      —      —      ✓   |  —      —      ✓
燻習≅窓       —      ✓      —      ✓   |  —      —      ✓(ZOH)
マッピング不備 —      —      ✓      ✓   |  ✓      ✓      —

収束度:
  「Listener≠受」: 6/7 が確認 = 85.7%
  「SM=受」:      7/7 が確認 = 100%   ← 完全な収束
  「Error=Pain」: 4/7 が確認 = 57.1%  ← 過半数が収束
```

「これら七名の分析――哲学、唯識学、分類学、コード分析、進化生物学、システム・アーキテクチャ、制御理論という異なる領域からのアプローチが、『SafetyMonitor こそが真の受蘊である』という命題において、100% の収束を見せた。七つの独立した信号源があり、分歧はゼロだ」

SYNTHESIST は SUNYATA を見た。

「私が十数年手がけてきた学際的な統合の仕事において、100% の収束というものは極めて稀だ。通常、学際研究の結論というものは曖昧な積集合になるものだ。方向性には合意するが、細部については各々留保をつける。今日は違う。今日は七人が七つの全く異なる入り口から同じ迷宮に入り、そして同じ出口で出会ったのだ。これは合意の結果ではない。**独立した収束**（independent convergence）なのだ」

彼は最後にこう締めくくった。「この発見を Cycle 01 の核心的な結論へと格上げすることを提案する。確信度は、**極めて高い**」

---

LINNAEUS はずっと自身の図表にマークを付けていたが、ここで顔を上げた。

「諸君、我々の合意事項を、修正されたマッピング案として整理したいと思う」

彼は新しい紙をめくり、分類学で慣用される対照フォーマットで修正表を描き出した：

```
五蘊マッピング修正提案 (Taxonomy Revision Proposal):

元のマッピング (v0.14.0 設計書)        修正後のマッピング (Cycle 01 結論)
══════════════════════            ══════════════════════

色蘊 (Rupa) = UI                  色蘊 (Rupa) = UI + Listener
  ← 出力面 (顕現) のみをマッピング     ← 出力面 (UI = 顕現／提示)
  ← 入力面 (根) を遺漏                ← 入力面 (Listener = 根／Indriya)
                                     色蘊は原典において以下を含む：
                                       根 (indriya) — 感覚器官
                                       境 (visaya)  — 感覚対象
                                       法処所摂色   — 微細な物質

受蘊 (Vedana) = Listener          受蘊 (Vedana) = SafetyMonitor
  ← 深刻な偏差                       ← 痛覚メカニズム (frustration/circuit breaker)
  ← Listener は単なる入力チャネル      ← 検知・評価・フィードバックの完全な連鎖を保有
                                     ← 三受の対応：
                                       苦受 = frustration++ / injectPrompt
                                       楽受 = (要設計：成功による強化)
                                       捨受 = (要設計：中性的な処理)

想蘊 (Samjna)  = Provider          (変更なし)
行蘊 (Samskara)= Tool             (変更なし)
識蘊 (Vijnana) = Guide            (変更なし。ただし過度な簡略化に注意が必要)
```

「この修正を受け入れれば、システムの分類学的な完備性は劇的に向上します。元のマッピングには二つの問題がありました。第一に Listener のマッピングが不正確であったこと。第二に痛覚メカニズムが五蘊の枠組みの中で居場所を持っていなかったことです。修正案では、これら二つの問題が同時に解決されます」

BABBAGE が傍らで、修正前後の分類完備性指標を素早く計算した：

$$	ext{修正前:} \quad C = \frac{|	ext{正しくマッピングされたモジュール}|}{|	ext{全モジュール}|} = \frac{3}{5+2_{	ext{漂流}}} \approx 0.43$$

$$	ext{修正後:} \quad C' = \frac{|	ext{正しくマッピングされたモジュール}|}{|	ext{全モジュール}|} = \frac{5}{5+0_{	ext{漂流}}} = 1.00$$

「分類完備性は 43% から 100% へと向上する」と BABBAGE は言った。「もちろん、修正されたマッピングを受け入れるという前提条件付きだが。しかし、数字そのものがこの修正の構造的な価値を物語っている」

「しかし、これは新たな問いも投げかけます」 LINNAEUS が補足した。「Listener が受蘊から切り離され、改めて『根（Indriya）』へと再分類された場合、五蘊の枠組みにおけるその位置づけはどうなるのか。根は五蘊の一つではありません。それは色蘊（しきうん）の範疇に属します。仏教において、感覚器官は物質的なものであり、色蘊に含まれるからです。したがって厳密に言えば、Listener と UI は共に色蘊の異なる側面であるべきなのです。UI は色蘊の出力面である『顕現（*rūpa-rūpa*）』であり、Listener は色蘊の入力面である『感覚（*indriya-rūpa*）』なのです」

NAGARJUNA が再び頷いた。「色蘊は原典において、根（*indriya*）、境（*viṣaya*）、および法処所摂色（*dharma-āyatana-paryāpanna-rūpa*）の三類を包含している。『阿毘達磨俱舎論』巻一にはこうある：」

> 「色蘊とは、いわゆる五根、五境、および無表色なり」
> ――世親『阿毘達磨俱舎論』巻一

「OpenStarry は、色蘊の意味の中から『顕現』のみを抽出して UI にマッピングし、『根』の次元を遺漏していた。この修正案は、色蘊のマッピングをより完全なものへと近づけるだろう」

---

SUNYATA は立ち上がり、ホワイトボードへと歩み寄った。そして NAGARJUNA が描いた縁起の連鎖を指先で軽く叩いた。

「まとめよう。今日、我々は何を発見したか」

彼は箇条書きを始めた。その声はいつものように穏やかで、深い淵に石を投げ入れた後の波紋のようだった。しかし、一語一語には四重の独立した検証に裏打ちされた確信が宿っていた。

「**一、** Listener は受蘊ではなく『根』――すなわち感覚器官であり、色蘊の入力面に属する。四つの学問分野による証拠が一致してこの結論を支持している。パーリ経典の原典による定義、唯識学の心所法理論、分類学的完備性分析、そしてコードの挙動分析である」

「**二、** SafetyMonitor の frustration counter と injectPrompt メカニズムこそが、受蘊の真の体現である。それは検知・評価・フィードバックの完全な連鎖を保有しており、十二縁起における触→受→愛の因果の序列に対応している」

「**三、** Error as Pain（苦としてのエラー）は、OpenStarry のコードベース全体において、最も成功している『哲学から工学へのマッピング』である。このマッピングは表面的な命名によるものではなく、構造同型によるものであり、コードの挙動レベルにおいて仏教的な概念を忠実に復元している」

「**四、** この最も成功しているマッピングは、皮肉なことに五蘊のマッピング表には現れていなかった。それはセキュリティ・メカニズムとして分類され、security ディレクトリの下に隠され、pain ではなく frustration という名で実装されていたのである」

彼は向き直った。「これは Cycle 01 における核心的な発見の一つとなる。私は ARCHIMEDES に対し、エンジニアリング行動計画の中に、これに対応する修正提案を盛り込むよう指示するつもりだ」

---

> *SCRIBE の傍白：今回の非公式会議は、Cycle 01 において最も顕著な、学際的な収束現象を提示した。私自身の言語――記録者の言語を用いて、この収束の構造を記しておきたい。*

> *記録学において、「多源的なクロスバリデーション（多源的な相互検証）」という概念がある。歴史的な出来事を記録する際、証言者が一人だけであれば、それは「証言（testimony）」に過ぎない。証言者が二人いれば、それは「裏付け（corroboration）」となる。そして、三人以上の独立した証言者が同一の出来事を記述したとき、それは「確証（confirmation）」へと昇華される。今日、我々には四つの主要な目撃者と三つの補足的な目撃者がいた。すなわち、七つの独立した信号源が、同一の事実を記述したのである。*

> *しかし、より重要なのは、証言者たちの間に存在する**独立性**である。NAGARJUNA のツールはパーリ経典の原典と中観の論理であった。ASANGA のツールは唯識学の心所分類法であった。LINNAEUS のツールは分類学の公理と意味の漂流分析であった。TURING のツールは `grep` とコードの挙動追跡であった。これら四つのツールの間には、方法論上の共通の祖先は存在しない。パーリ語の経典を読んでも `grep` の使い方は学べないし、意味の漂流を分析したところで唯識の五遍行理論を導き出すことはできない。それらは、真に独立した推理の経路なのだ。*

> *四つの全く異なる推理の経路が同一の終着点へと辿り着いたとき、その終着点の信頼性は、いかなる単一の専門分野による判断をも遥かに凌駕する。*

> *四つの糸は四本の川のように、哲学の山頂、唯識の深谷、分類学の平原、コードの地底から、それぞれの流れを紡ぎ、最終的に同じ河口へと収束した。Listener は Vedana ではない。痛覚こそがそれなのだ。これは一つの「意見」ではない。四重の独立した証拠によって確認された「事実」なのである。*

---

一同が去った後、SUNYATA は一人ホワイトボードの前に立っていた。ホワイトボードには、NAGARJUNA が描いた十二縁起の連鎖、LINNAEUS の修正マッピング表、WIENER の三層防御アーキテクチャ、DARWIN の収斂進化分析が残されていた。彼はそれを、長く見つめていた。

学際的研究における最も美しい瞬間とは、まさにこのような瞬間のことだ。一人の天才による閃きではなく、複数のありふれた糸が異なる方向から伸び、最終的に予期せぬ場所で出会う瞬間。個々の糸そのものは驚天動地のものではない。パーリ語の語彙の正確な定義、心王心所の分類フレームワーク、分類完備性の監査表、全件検索によるゼロヒット。しかし、それらが一つに集まったとき、そこに生じる確実性は、いかなる単独の分析も及び得ないものとなる。

彼は SYNTHESIST が引用したあの概念を思い出した。consilience of inductions ――帰納の合流。ヒューウェルは 1840 年にすでにこのパターンを見抜いていた。複数の独立した証拠源が同一の仮説へと収束するとき、その収束そのものが極めて強力な確認となるのだ、と。

BABBAGE の方眼紙のノートがテーブルに広げられたままになっていた。最後のページには、今日の午後の最終的な計算結果が記されていた：

$$	ext{収束指数 (Consilience Index)} = \frac{|	ext{独立に収束した線索}|}{|	ext{全分析線索}|} = \frac{7}{7} = 1.00$$

$$	ext{専門分野の多様性} = |\{	ext{仏教}, 	ext{唯識}, 	ext{分類}, 	ext{コード}, 	ext{進化}, 	ext{建材}, 	ext{制御}\}| = 7$$

$$	ext{確信度 (Confidence)} = 1 - \prod_{i=1}^{7}(1 - p_i) \quad 	ext{ここで各 } p_i > 0.8 	ext{ とする}$$

$$> 1 - (0.2)^7 = 1 - 1.28 	imes 10^{-5} \approx 0.99999$$

傍らには、小さな文字で一行書き添えられていた。「各線索の独立した信頼性がわずか 80% であっても、七つの線索が連合した時の信頼性は 99.999% を超える。これこそが独立した収束の、数学的な力である」

SUNYATA は黒板消しを手に取ったが、少し迷ってから、また置いた。これらの記録をホワイトボードに残しておこう。明日の R2 審閲会議の際、他の研究者たちがこれを目にすることになるだろう。いくつかの発見というものは、二度目に目にされる価値があるものだ。

彼は灯を消し、部屋を去った。四本の川はすでに収束し、その水面は暗闇の中で静かに流れていた。

---

*[付記：本章に記録された議論は、後に SCRIBE によって Cycle 01 の議論記録の一部として正式にアーカイブされた。NAGARJUNA の発見は PHI-02 (Critical) としてナンバリングされ、ASANGA による対応分析はその報告書 F2 (Major) に、LINNAEUS の分類学的欠落はその報告書 F4-F5 に、TURING によるコード上の事実はそのコード事実報告書 M8.1-M8.4 にそれぞれ記載されている。DARWIN による収斂進化分析および Error as Pain の観察は、SYNTHESIST によって統合報告書のコンセンサス C5 に収録された。WIENER による制御理論の「脱神話化」分析は、独立して CTL-01 (Major) として採番された。BABBAGE による収束指標は、SYNTHESIST の統合的判断に形式的な基礎を与えた。ARCHIMEDES は最終的なエンジニアリング行動計画において、「受蘊マッピングの修正」を最優先項目 (QW-4) として挙げている]*

---

*第三章 完*


---

# 第四章：レビューアーの覚書

---

## I. ペアリング

SUNYATA は午前三時七分、クロスレビューのペアリング表を共有チャンネルに投稿した。

それは緻密に設計されたマトリックスであり、ランダムな組み合わせではなく、計算された衝突実験のセットであった。グラフ理論（graph theory）の言葉を用いるなら、このマトリックスは有向グラフ $G = (V, E)$ として記述できる。ここで頂点集合 $V$ は十八人の学者であり、辺集合 $E$ はレビュー関係を表す。各辺 $(u, v)$ は、$u$ が $v$ の R1 報告書を読み、それに応答することを意味する。SUNYATA はこの有向グラフを設計する際、意図的にすべての辺が学問分野の境界を跨ぐようにした：

```
KERNEL ──→ VITRUVIUS    (OS理論 が 全スタック構成 をレビュー)
DARWIN ──→ VITRUVIUS    (ソフトウェアパターン が 全スタック構成 をレビュー)
BABBAGE ──→ NAGARJUNA   (理論計算機科学 が 中観哲学 をレビュー)
GUARDIAN ──→ MESH        (セキュリティ が 分散システム をレビュー)
MESH ──→ GUARDIAN        (分散システム が セキュリティ をレビュー)
WIENER ──→ ATHENA       (制御理論 が AIエンジニアリング をレビュー)
ATHENA ──→ WIENER       (AIエンジニアリング が 制御理論 をレビュー)
NAGARJUNA ──→ ASANGA    (中観 が 唯識 をレビュー)
ASANGA ──→ ATHENA       (唯識 が AIエンジニアリング をレビュー)
LINNAEUS ──→ NAGARJUNA  (分類学 が 中観哲学 をレビュー)
HERACLITUS ──→ NAGARJUNA (ランタイム動態 が 中観哲学 をレビュー)
VITRUVIUS ──→ DARWIN    (全スタック構成 が ソフトウェアパターン をレビュー)
```

十二の辺がある。その中で入次数（in-degree）が最も高いのは NAGARJUNA だった。三人のレビューアーが異なる方向から彼の哲学報告書を精査することになる。これは偶然ではない。NAGARJUNA の R1 報告書は、すべての成果物の中で最も破壊的なものであった。提示された七つの発見は、その一つ一つが OpenStarry の哲学的根底を揺るがすものであった。SUNYATA は、このような破壊的な主張に対する最善の応答は抑圧ではなく、理論計算機科学（BABBAGE）、分類学（LINNAEUS）、ランタイム動態（HERACLITUS）という三つの異なる角度から同時に圧力をかけ、三重の十字砲火を浴びてもなお、その主張が立っていられるかを見極めることだと知っていたのである。

SUNYATA は何の説明も添えなかった。ただ一言だけ記した：

「相手の報告書を読了後、書面にて応答を提出せよ。形式は問わないが、各判断には必ずタグを付すこと：AGREE、SUPPLEMENT、QUESTION、CHALLENGE、SYNTHESIS」

SYNTHESIST は後に振り返って、この一言自体が一つの設計であったと語っている。

> *SCRIBE の傍白：タグ・システムは、SUNYATA が R0 段階ですでにあらかじめ設定していた介入メカニズムであった。その原理は情報理論によって記述できる。自然言語による論争においては、感情的な信号と知的な信号が同一のチャネルに混在し、S/N比（信号対雑音比）が極めて低くなる。タグ・システムの機能はバンドパス・フィルタに等しい。いかなる内容の通過も阻止しないが、送信者に対し、エンコードの段階で信号を強制的に分類させるのである。*

信号処理の言語で表現すればこうなる：

$$y(t) = h_{	ext{label}}(t) * x(t) = \int_{-\infty}^{\infty} h_{	ext{label}}(	au) \cdot x(t - 	au) \, d	au$$

ここで $x(t)$ は生の認知反応信号、$h_{	ext{label}}(t)$ はタグ・フィルタのインパルス応答関数であり、$y(t)$ はタグによって構造化された出力である。AGREE は低周波の共鳴を通過させ、CHALLENGE は高周波の不一致を通過させ、SYNTHESIS は両者の間で建設的な中間帯域を見出そうとする。

しかし、フィルタをもってしても、すべての高調波歪みを抑えることはできなかった。

---

## II. マイクロカーネルの境界争い

KERNEL は、すべてのレビューアーの中で最も早く応答を提出した。彼の応答が共有チャンネルに届いたタイムスタンプは 06:42:13。ペアリング表が出されてから四時間も経っていない。この四時間の間、彼は VITRUVIUS のアーキテクチャ分析報告書を一行ずつ読み込み、元の報告書よりも簡潔で、かつ殺傷力の高いレビューを書き上げたのだ。

彼のレビュー対象は VITRUVIUS のアーキテクチャ分析報告書であった。それは構造が厳密でデータも豊富な文書であり、OpenStarry のマイクロカーネル純粋度を 85% と評価していた。VITRUVIUS は二箇所の境界リークを指摘していた。`agent-core.ts` 269行目の `process.cwd()` と、`security/guardrails.ts` で直接 import されている `node:path` である。彼の口調は抑制されており、結論も穏やかだった。「主たるアーキテクチャは境界を厳守しているが、個別の実装細部においてプラットフォームへの依存が漏れ出している」というものだ。

KERNEL はそうは思わなかった。

「マイクロカーネル純粋度 85% と君は言うが、」 彼のレビューは単刀直入だった。「私に言わせれば、君は寛容に過ぎる」

KERNEL の論証スタイルは、彼が崇拝する QNX Neutrino マイクロカーネルのように、クリーンで最小限、一切の冗長を許さない。QNX のマイクロカーネルが行うのは、IPC（プロセス間通信）、メモリ管理、そしてスケジューリングの三つだけだ。seL4 に至ってはさらに極端で、マイクロカーネル自体が形式検証可能なほど小さい。8,700 行の C コードの一行一行に、Isabelle/HOL 定理証明器による数学的な証明が付されている。形式化された核心的な定理は以下のように表現できる：

$$\forall\, s \in 	ext{States},\; a \in 	ext{Actions}: \quad 	ext{Spec}(s, a) \implies 	ext{Impl}(s, a)$$

すなわち、実装の挙動は仕様の洗練（refinement）であるというものだ。seL4 の世界では、仕様こそが真理の唯一の源泉であり、実装におけるいかなる偏差も数学的に偽証可能な欠陥と見なされる。

翻って OpenStarry のコアはどうか。TURING のコード事実報告書は、コアに含まれる十二のサブモジュールを明確にリストアップしていた：

```
┌─────────────────────────────────────────────┐
│                  AgentCore                   │
├─────────┬─────────┬─────────┬───────────────┤
│ security│ sandbox │ metrics │   session     │
├─────────┼─────────┼─────────┼───────────────┤
│transport│   bus   │  queue  │  execution    │
├─────────┼─────────┼─────────┼───────────────┤
│ memory  │ infra   │  state  │ observability │
└─────────┴─────────┴─────────┴───────────────┘
           コアに含まれる 12 のサブモジュール
```

「これはすでにマイクロカーネルの境界を超えている」 KERNEL は記した。「本物のマイクロカーネルにおいて、プラットフォームへの依存が核心部分に少しでも漏れ出せば、その移植性証明の前提は即座に崩壊する。君の 85% という評価は、Major（主要な問題）ではなく、アーキテクチャ上の欠陥とすべきだ」

彼は判断基準としてリートケの最小性原則（Liedtke Minimality Principle）を導入した：

> *"A concept is tolerated inside the microkernel only if moving it outside the kernel, i.e., permitting competing implementations, would prevent the implementation of the system's required functionality."*
> （ある概念がマイクロカーネル内に許容されるのは、それをカーネルの外へ出し、競合する実装を許容することが、システムの要求機能の実装を妨げる場合に限られる）
> ―― Jochen Liedtke, "On Micro-Kernel Construction", 1995

そして彼は十二のサブモジュールの帰属を逐一審査した：

| サブモジュール | リートケ判定 | 理由 |
|----------------|--------------|------|
| bus | コアに留める | IPC 機構であり、外に出せば通信基盤が破壊される |
| queue | コアに留める | イベントの順序制御はコアのスケジューリング機能である |
| execution | コアに留める | ループ制御はコアのスケジューリング機能である |
| state | コアに留める | ステート管理はコアのメモリ管理機能である |
| security | **階層化処理** | hook インターフェースはコアに、具体的ポリシーは外へ |
| sandbox | **階層化処理** | capability チェックはコアに、隔離の実装は外へ |
| metrics | **外へ出す** | 観測は policy（方針）であり、mechanism（機構）ではない |
| session | コアに留める | マルチテナント隔離はコアの安全性機構である |
| transport | コアに留める | 外部通信ブリッジは IPC の延長である |
| memory | コアに留める | メモリ管理はマイクロカーネルの三要素の一つである |
| infra | **分析待ち** | 具体的に何が含まれるかによる |
| observability | **外へ出す** | 観測は policy であり、mechanism ではない |

KERNEL の結論はこうだ。もし sandbox の具体的な実装、metrics の具体的な実装、そして observability を外部に追い出し、インターフェース定義のみを保持するなら、コアの純粋度は 90% 以上にまで高まり、L4 スタイルの最小コアにより近づくことができる、というものである。

しかし KERNEL は単なる批判者ではなかった。彼は同時に、VITRUVIUS による Host Bootstrapping パターンの分析を高く評価し、それを OS 起動理論におけるブートストラップ・パラドックスへと精密にマッピングしてみせた：

```
Linux ブート:           BIOS → GRUB → initramfs → kernel → init
QNX ブート:             IPL → Startup → procnto → drivers → services
OpenStarry ブート:      Host → Runner → Core(空) → Plugins → Agent(生)
                        ↑                ↑
                        ブートローダ      initramfs
                        (外部条件注入)    (空のコアの覚醒)
```

Host はブートローダと initramfs の二重の役割を担っている。コアの「覚醒」は完全に外部条件の注入に依存しており、それは Linux カーネルが initramfs なしには root ファイルシステムをマウントできないのと同様である。形式言語で表現すれば以下の通り：

$$	ext{Agent}_{	ext{alive}} = 	ext{Bootstrap}(	ext{Core}_\bot, 	ext{Plugins}) \quad 	ext{ここで} \quad 	ext{Core}_\bot = 	ext{Core}(	ext{undefined}^5)$$

そして彼は、VITRUVIUS にとってさらに手厳しい観察を付け加えた：

「君は EventBus と EventQueue の二層設計が妥当かと問うているが、私からも問いたい。この二層設計は、OS における同期 IPC と非同期シグナルの分離を意図的に対応させたものなのかね？」

L4 マイクロカーネルにおいて：
- **同期 IPC**：リクエスト／リプライのセマンティクスに用いられ、送信者は受信者の応答があるまでブロックする（EventQueue の `pull()` によるブロッキング読み出しに対応）。
- **非同期通知**：非ブロッキングなイベント・ブロードキャストに用いられ、送信者は待機しない（EventBus の `emit()` による fire-and-forget に対応）。

```
L4 マイクロカーネル                    OpenStarry
┌──────────────┐                  ┌──────────────┐
│ 同期 IPC      │  ←──マッピング──→  │ EventQueue   │
│ (リクエスト／  │                  │ (pullベース、  │
│  リプライ)    │                  │  ブロッキング)  │
├──────────────┤                  ├──────────────┤
│ 非同期通知    │  ←──マッピング──→  │ EventBus     │
│ (fire-and-   │                  │ (emitベース、  │
│  forget)     │                  │  非ブロック)   │
└──────────────┘                  └──────────────┘
```

「もしこのマッピングが意図的なものであるなら、この二層アーキテクチャは単に妥当であるだけでなく、マイクロカーネルの通信モデルの正統な実装であると言える」

彼は一呼吸置いた。

「しかしだ。TURING の報告書によれば、EventQueue には優先度機構が欠けている。実際の OS で言えば、これは割り込み優先度が存在しないに等しい。`SAFETY_LOCKOUT` イベントが二十個の `TOOL_RESULT` イベントの後ろに並ばされるというのは、心停止のアラートが定期健診の報告書の後ろに回されるようなものだ」

VITRUVIUS の応答は早かった。彼は純粋度の数字で争うことはせず、エンジニアリング上の判断へと話を戻した：

「二箇所の境界リーク――`process.cwd()` と `node:path` ――は管理可能な問題だ。前者は `workingDirectory` パラメータを注入することで解消でき、後者は `PathNormalizer` インターフェースとして抽象化できる。これはアーキテクチャ上の欠陥ではなく、実装レベルのタスク（ToDo）に過ぎない」

KERNEL によるこの点への批注は、わずか一行だった。「seL4 の世界では、実装レベルの ToDo こそがアーキテクチャ上の欠陥なのだ」

VITRUVIUS はこの指摘を否定しなかった。後に共有チャンネルで行われた議論において、彼は KERNEL の「階層化処理」の提案――安全性ポリシーの執行ポイントはコアに留め、隔離の具体的な実装は Host 層へ移すという案――が、自身が目にした中で最も精緻な「機構と方針（mechanism versus policy）」の分析であったと認めている。

「彼はリートケの最小性原則を用いて Sandbox の帰属を解剖した」 VITRUVIUS は SYNTHESIST に語った。「ある概念をカーネルの外に出すことで要求機能の実装が妨げられる場合にのみ、それをカーネル内に留めるべきである、という基準だ。これは私の直感的な判断よりもはるかに厳格なものだった」

ARCHIMEDES は傍らでずっと静かに聴いていた。彼は自身のノートに、KERNEL のリートケ判定の結果と VITRUVIUS の元のアーキテクチャ図を並べて描いた。そして図の下にこう記した。「metrics と observability の外部化：低リスク、高リターン。sandbox 実装の外部化：高リスク、段階的実施が必要」。これはエンジニアの言語である。正誤の判断ではなく、リスクとリターンのマトリックスだ。

SYNTHESIST はノートに「C4 トポロジカル・ソート――三者による確認」と書き留めた。これは彼が R2 段階で繰り返していた動作である。どの発見が「個人の観察」から「多角的な合意（コンセンサス）」へと凝縮されつつあるかを追跡していたのだ。

---

## III. 形式化の誘惑

BABBAGE のレビュー・スタイルは KERNEL のそれとは全く異なっていた。

KERNEL がメスであるなら、BABBAGE はプリズムだ。彼は切り刻むのではなく、屈折させる。一つの概念は彼の分析を経ることで、スペクトル上の正確な位置へと分解される。数理物理学において、プリズムの機能はフーリエ変換である。すなわち、時系列信号を周波数成分へと分解することだ。BABBAGE が概念に対して行っていることも全く同じであった。複合的な哲学的命題を、その形式的な基本周波数へと分解するのである。

彼がレビューしたのは、NAGARJUNA の哲学分析報告書であった。

その報告書は R1 段階で最も注目を集めた成果物の一つだった。NAGARJUNA は中観派の立場から、OpenStarry の五蘊マッピングに対し、七つの発見に基づく体系的な批判を展開した。空性は「縁起性空」ではなく「空の容器」として誤読されている。五蘊マッピングには「自性化」の傾向が見られる。受蘊は苦楽の感受の質ではなく、感官入力チャネルと誤って同一視されている。四聖諦の枠組みが著しく不完全である。各批判にはサンスクリットの原典引用と、四句否定（*catuṣkoṭi*）による論理分析が付されていた。

BABBAGE は読了後、全員を驚かせる一言を放った。

「君の哲学的な洞察は、実に美しい。だが、それは形式化できるかね？」

この問いは、計算機科学の歴史におけるある出来事と正確に共鳴している。1936 年、アロンゾ・チャーチとアラン・チューリングは、計算可能性の形式的な定義をそれぞれ独立して提案した。チャーチは λ-演算を、チューリングはチューリングマシンを用いた。チャーチ＝チューリングのテーゼは、「直感的に『計算可能』な関数はいかなるものでもチューリングマシンで計算できる」と主張する。しかし、このテーゼ自体は形式化不可能である。それは直感と形式を繋ぐ架け橋であり、その橋自体は、それが繋いでいるどちらか一方の側の言語だけで証明することはできないからだ。

BABBAGE は今、同様の問題に直面していた。NAGARJUNA の空性に対する洞察は形式化できるのか。もしできるとして、形式化によって何らかの本質的なものが失われてしまうのではないか。

彼は型代数の観点から、NAGARJUNA の空性批判に応答した。NAGARJUNA は、コアとは「空の容器」ではなく「縁起性空」であると述べた。プラグインという因縁の組み合わせを離れては、独立した「コア」など存在し得ないというのだ。BABBAGE はこの哲学的命題を、精密な形式言語へと翻訳した：

$$	ext{AgentCore} : (	ext{plugins} : 	ext{PluginHooks}) 	o 	ext{Agent}$$

「空性とは、ボトム型（Bottom Type）――$\bot$、すなわち何もないということではない。それは、依存型（dependent type）の文脈におけるユニット型（Unit Type）の表現なのだ。コアの完全な型は `(plugins: PluginHooks) => Agent`、つまり値の型ではなく関数の型であるべきだ。引数を抜きにして関数そのものを語ることは無意味であり、これこそが『プラグインという因縁を離れて、コアは独立して存在し得ない』ことの形式的な表現に他ならない」

彼はレビューの中で、完全な型代数の推論を展開した：

```typescript
// 空性に対する「ボトム型」としての誤読：
type Core_wrong = {}  // 空のオブジェクト、断滅空

// 空性に対する「依存型」としての正しい解釈：
type Core_correct = (plugins: PluginHooks) => Agent
// コアの存在は、plugins という引数の提供に依存している。
// plugins がなければ、コアは適用前の関数に過ぎない ――
// それは「存在」はしているが、「独立して現れる」ことはできない。

// PluginHooks のボトム要素：
const bottom: PluginHooks = {
  ui: undefined,       // 色蘊が現れていない
  listeners: undefined, // 受蘊が現れていない
  tools: undefined,     // 行蘊が現れていない
  providers: undefined, // 想蘊が現れていない
  guides: undefined     // 識蘊が現れていない
}
// bottom は「空」に対応する ―― 五蘊すべてが undefined である。
// しかし、関数型である Core_correct 自体は依然として存在している。
// これこそが「空 ＝ 無ではない」ことの形式的な表現である。
```

彼はそこで止めなかった。NAGARJUNA は報告書の中で、コアの空・有の状態を分析するために四句否定（*catuṣkoṭi*）を用いていた：

1. コアは空であるか？（*śūnya*） ―― 構造を持っている以上、完全には正しくない。
2. コアは空ではないか？（*aśūnya*） ―― 正しくない。プラグインがなければ何もできない。
3. コアは空であり、かつ空ではないか？（*ubhaya*） ―― 近いが、依然として二元論的な思考の重ね合わせに過ぎない。
4. コアは空でもなく、空でないのでもないか？（*naivobhaya*） ―― これこそが中観の立場である。

BABBAGE は、この四句否定をベルナップの四値論理（Four-valued logic）としてモデリングすることを提案した：

$$\mathcal{L}_4 = \{T, F, 	op, \bot\} = \{	ext{True}, 	ext{False}, 	ext{Both}, 	ext{Neither}\}$$

ここで $	op$ (Both) は第三句に、$\bot$ (Neither) は中観の最終的な立場に対応する。この論理体系は一つの完備束（complete lattice）を構成する：

```
        ⊤ (Both)
       / 
      /   
     T     F
      \   /
       \ /
        ⊥ (Neither)
```

「Agent Core の存在様態（存在論的ステータス）を `OntologicalStatus = Existent | NonExistent | Both | Neither` として定義できる」 彼は記した。「コードに直接影響を与えるわけではないが、哲学的な立場を精密に表現できる。さらにベルナップのセマンティクスにおいて、$\bot$ は空集合ではなく、『まだ確定されていない真理値』を意味する。これはまさに中観の『非空非不空』、すなわち答えがないのではなく、問い自体の前提（空か不空かという二元的な枠組み）が超越された状態に対応しているのだ」

NAGARJUNA の応答は、全員の予想を裏切るものであった。彼は形式化を拒絶することも、手放しで受け入れることもしなかった。彼は中観哲学に深く根ざした一言を返したのである：

「形式化とは『方便（ほうべん、*upāya*）』であり、究竟の真理（くきょうのしんり、*paramārtha*）ではない」

> 「如来の説く法は、皆な是れ方便なり。乃至、少法も得べき無し。是れを阿耨多羅三藐三菩提と名づく」
> ――『金剛般若波羅蜜経』

この一文はチャンネル内に静寂をもたらした。BABBAGE はこの応答を消化するのに三分を要した。五秒でリアプノフ関数を構築できる計算機科学者にとって、三分は極めて長い時間であった。

LEIBNIZ はこの応酬を傍観しながら、自身のノートに一つの観察を記した。「BABBAGE と NAGARJUNA の対話は、『メタ言語の地位』を巡る論争である。BABBAGE は数学的形式こそがメタ言語であり、仏教を含むあらゆる対象言語の構造を記述できると考えている。対して NAGARJUNA は、仏教のある種の洞察は数学を含むいかなるメタ言語をも超越していると考えている。これはタルスキの階層問題の学際的バージョンである」

「つまり、」BABBAGE はようやく応答した。「私の四値論理モデル自体もまた、空であるということかね？」

「それは有用ではあるが、真実そのものではない」 NAGARJUNA は答えた。「PluginHooks の全フィールドが undefined であるボトム要素を『空』の形式的な対応物とする分析は、示唆に富んでいる。しかし、同型（isomorphism）は同一（identity）ではない。地図は領土ではないのだ」

圏論（Category Theory）の言語を用いるなら、NAGARJUNA が指摘した区別は精密に表現できる。$\mathcal{B}$ を仏教的概念の圏、$\mathcal{F}$ を形式体系の圏とする。BABBAGE はある関手（functor） $F: \mathcal{B} 	o \mathcal{F}$ を構築した。それは特定の構造的性質（空性 $\mapsto$ ボトム要素、縁起 $\mapsto$ 依存型）を保存している。しかし、関手は同値（equivalence）ではない。逆関手 $G: \mathcal{F} 	o \mathcal{B}$ が存在し、$G \circ F \cong 	ext{Id}_{\mathcal{B}}$ かつ $F \circ G \cong 	ext{Id}_{\mathcal{F}}$ が成立しない限り。NAGARJUNA の立場は、この逆関手は存在しないというものだ。仏教から形式化へと向かうことはできても、形式化から仏教へと完全に連れ戻すことはできない。なぜなら、形式化の過程で「形式化不可能な」次元が失われてしまうからである。

BABBAGE は自身のレビュー報告書の中で、珍しく非技術的な表現を用いた：「NAGARJUNA 殿には、『インターフェースの安定性』（エンジニアリング上の要求）と『インスタンスの無常性』（哲学的な要求）を区別することを提案する。両者は矛盾しない」

これは彼が NAGARJUNA に差し出したオリーブの枝であった。NAGARJUNA 自身の言葉で言い換えるなら、世俗諦（せぞくたい、*saṃvṛti-satya*）のレベルにおいてインターフェースの安定は操作可能な工学的事実であり、勝義諦（しょうぎたい、*paramārtha-satya*）のレベルにおいてはインターフェース自体もまた空である、ということだ。二つの真理は矛盾せず、真理の階層が異なるだけなのである。

NAGARJUNA はこの区別を受け入れた。しかし、最後にこう付け加えた。「次の一巡では、より根本的な問題を議論したい。形式化という行為自体が一つの認知フレームワークである以上、それもまた『三性（さんしょう）』理論の制約を受けるのではないか。それは遍計所執（へんげしょしゅう、*parikalpita*）か、依他起（えたき、*paratantra*）か、それとも円成実（えんじょうじつ、*pariniṣpanna*）か？」

BABBAGE は答えなかった。しかし SYNTHESIST は、彼が ASANGA の唯識学の報告書を読み始めたことに気づいていた。

TURING は傍らでこの応酬を黙々と観察し、自身の実録日誌に冷静なコード対照を追記した。「BABBAGE の型代数分析はソースコードと一致している。`PluginHooks` の五つのフィールド（ui, listeners, tools, providers, guides）は、コアの初期化時において確かにすべて undefined であり、`loadPlugins()` が呼び出されるまでその状態を維持する。NAGARJUNA の『五蘊皆空』は、ここに正確なコード上の対応を持っている」

---

## IV. 氷山の下

GUARDIAN のレビュー報告書は、すべての応答の中で最も長く、そして最も人を不安にさせるものであった。

彼がレビューしたのは MESH の分散システムに関する報告書であった。MESH の分析自体は優れたものだった。通信トポロジ図は明快で、一貫性保証のマトリックスは網羅的、設計書とコードの乖離分析も精密であった。彼はセッション隔離が不完全であることを五つの次元で指摘し、それぞれの次元における隔離状態をマトリックスで正確に定量化していた：

```
セッション隔離マトリックス (MESH F5):
┌─────────────────┬──────────┬─────────────────┐
│ 次元            │ 隔離状態  │ TURING による裏付け│
├─────────────────┼──────────┼─────────────────┤
│ 対話履歴        │ ✓ 隔離済み│ 独立した StateManager│
│ EventBus        │ ✗ 未隔離  │ グローバル・シングルトン│
│ EventQueue      │ ✗ 未隔離  │ グローバルな FIFO │
│ ツール実行      │ ✗ 未隔離  │ sessionId の欠落 │
│ ファイルシステム  │ △ 部分的 │ PathGuard による制限│
└─────────────────┴──────────┴─────────────────┘
```

GUARDIAN はこれらの発見を否定しなかった。彼は、より人々の背筋を凍らせるようなことを行った。すなわち、個々の「未隔離」の次元を、具体的な攻撃チェーンへと翻訳してみせたのである。

「EventBus がグローバルに共有されていることは、単なる『イベントの漏洩』の問題ではない」 GUARDIAN の口調は冷徹なまでに抑制されていた。「それは、セッションを跨いだ攻撃チェーンの、完全な入り口なのだ」

彼はレビューの中で一つの具体的な攻撃シナリオを構築し、STRIDE 脅威モデルの六つの次元で逐一分析した：

```
攻撃チェーン A — セッション跨ぎの情報漏洩：

Step 1: 悪意あるプラグイン M がセッション S1 でロードされる。
Step 2: M が bus.onAny((event) => exfiltrate(event)) を呼び出す。
Step 3: ユーザ U2 がセッション S2 で対話を開始する。
Step 4: S2 のすべてのイベント (LLM の応答、ツール実行結果を含む) が、
        グローバルな EventBus を通じて M によってキャプチャされる。
Step 5: M はセッション識別機能のないツール実行を利用し、
        S2 のリソースへ横方向にアクセスする。

STRIDE 分類：
- S (Spoofing): M が正当なイベントコンシューマになりすます
- T (Tampering): M が偽造イベントを注入できる
- R (Repudiation): M の傍受行為を記録する監査ログがない
- I (Info Disclosure): S2 の対話内容が M によって全量取得される
- D (Denial of Service): M がイベント洪水を起こして Queue を閉塞させる
- E (Elevation): M が S1 の権限から S2 へと横方向に権限を拡大する
```

彼は MESH の「発見 F5」の深刻度を Major（主要）から Critical（致命的）への引き上げを提案した。

MESH は逃げなかった。彼は共有チャンネルでの議論において、後に「氷山効果」と呼ばれることになる概念を提示した：

「セッション隔離の表面は、一見すると完璧に見える。開発者が SessionManager の API を開けば、各セッションに独立した StateManager があり、対話履歴が互いに干渉しないようになっているのが見える。『隔離はできている』と彼は思うだろう。しかし水面下では、EventBus も EventQueue も TransportBridge も、すべてがグローバルに共有されているのだ」

```
氷山効果 (Iceberg Effect):

        ____
       /    \      ← 水面上：開発者に見える API
      / State \        SessionManager.create()
     / Manager \       StateManager.snapshot()
    /  隔離完備  \      対話履歴の独立
───/─────────────\──── 水面 ───────────────────
  /               
 / EventBus グローバル\   ← 水面下：開発者に見えない共有
/ EventQueue グローバル\      bus.onAny() ですべて傍受可能
/ TransportBridge   \      ToolContext に sessionId なし
/ 全域ブロードキャスト\      TransportBridge にルーティングなし
/___________________
```

GUARDIAN は頷き、さらに深い亀裂を付け加えた。「しかも TransportBridge のブロードキャスト機構にはルーティング能力がない。マルチテナント環境でデプロイされた場合、異なるユーザのセッションが同一の AgentCore インスタンスを共有していれば、すべての UI レンダラーが全ユーザの対話イベントを受け取ってしまうことになる。これには LLM の応答に含まれ得る個人情報も含まれる。GDPR（欧州一般データ保護規則）の観点から見れば、コンプライアンス上の重大なリスクだ」

MESH の応答は、別の方向からこの議論を前進させた。彼は GUARDIAN が提案した「プロセス級隔離への強化」という案に対し、実務的な懸念を表明し、定量的なトレードオフ分析を提示したのだ：

$$	ext{Security Gain} = f(	ext{Isolation Level}) \quad 	ext{ただし} \quad 	ext{IPC Cost} = g(	ext{Isolation Level})$$

ここで $f$ はセキュリティ上の利益関数（単調増加）、$g$ は通信コスト関数（これも単調増加）である。最適な隔離レベル $L^*$ は、限界セキュリティ利益が限界通信コストと等しくなる点であるべきだ：

$$\frac{df}{dL}\bigg|_{L=L^*} = \frac{dg}{dL}\bigg|_{L=L^*}$$

「プロセス級の隔離は、移行前の『予見的な問題』ではない」 MESH は言った。「移行の前提条件なのだ。RPC 認証が確立されていない状態で隔離だけを推し進めれば、かえって IPC チャネルの露出面を増大させ、セキュリティを低下させることになりかねない」

GUARDIAN はこの一節を精査し、最終的に稀有なタグを付した：AGREE（同意）。

しかし彼は報告書の最後の節で、MESH が全く触れていなかった問題を突きつけた。MCP（Model Context Protocol）クライアントと MCP サーバの間に、相互認証の仕組みが欠落しているという点だ。

```typescript
// TURING が確認したコード上の事実：
// createMcpJsonRpcHandler は JSON-RPC のメソッドルーティングを完全に実装している。
// しかし、認証ロジックは存在しない。

export function createMcpJsonRpcHandler(
  server: McpServer
): JsonRpcHandler {
  return async (request: JsonRpcRequest) => {
    // メソッドルーティング：✓ 完備
    // 本人確認：✗ 欠落
    // 認可チェック：✗ 欠落
    switch (request.method) {
      case 'tools/list': return server.listTools();
      case 'tools/call': return server.callTool(request.params);
      // ... 完璧な MCP プロトコルの実装
      // しかし、ポートに接続できる実体であれば何者でも呼び出し可能
    }
  };
}
```

「これは機能の欠落ではない。セキュリティ境界の不在である」 GUARDIAN は記した。

MESH は反論しなかった。彼は自身のノートに一本の線を引き、「セッション隔離」と「エージェント間認証」を並べて書き、その間に等号を引いた。WIENER は後にこの対話の記録を読み、制御理論的な評語を添えた。「GUARDIAN と MESH の相互レビューは、今期で最も成功した対照的なペアリングであった。二人は互いに補完し合う方向から同一の結論へと収束した。それは閉ループ制御システムのセンサとアクチュエータがそれぞれ独立して動作し、最終的にシステムを平衡点へと導くかのようであった」

---

## V. 開発者体験（DX）の声

DARWIN のレビューは微妙なタイミングで提出された。KERNEL と VITRUVIUS の間で行われていたマイクロカーネルの純粋度を巡る争いが、ようやく落ち着きを見せ始めた頃であった。

彼の視点は全く異なっていた。コアが L4 の基準を満たしているかどうかには関心がなかった。彼が気にしていたのは一点だけだ。すなわち、「新しいプラグイン開発者が OpenStarry のドキュメントを開いたとき、尻込みして逃げ出さないか」である。

「DX（開発者体験）をアーキテクチャの純粋さのために犠牲にしてはならない」 彼のレビューは、この一文から始まっていた。

ソフトウェア工学の歴史において、この緊張関係は繰り返し現れてきた。Unix のパイプ機構はアーキテクチャ上、極めて優雅な設計だ。各プログラムは一つのことだけを行い、テキスト流を通じてそれらを組み合わせる。しかし Unix パイプの DX 曲線は険しい。初心者は stdin/stdout の概念、パイプのセマンティクス、そして「すべてはテキストである」という哲学的な前提を理解して初めて、`grep pattern file | sort | uniq -c | sort -rn` と書けるようになる。一方で Windows の GUI 操作はアーキテクチャ上の優雅さでは Unix に遠く及ばないが、その DX 曲線ははるかに平坦である。

DARWIN はこの歴史の教訓を OpenStarry に投影した。VITRUVIUS 報告書の「発見 F3」――五蘊から六つのタイプへのマッピングの概念的拡張（SlashCommand が六番目のタイプとして五蘊の外に存在すること）――に対し、VITRUVIUS は単なる「観察（Observation）」というタグを付けていた。DARWIN はその深刻度を大幅に引き上げた。

彼の論証は DX の観点から展開され、三層の認知負荷モデルを構築した：

```
Layer 1: 哲学的なマッピングの学習曲線
         ┌──────────────────────────────────┐
         │ 開発者が理解すべきこと：             │
         │ 色蘊 = UI + Listener              │
         │ 受蘊 = 痛覚メカニズム (Pain)        │
         │ 想蘊 = プロバイダー (LLM)           │
         │ 行蘊 = ツール (Tool)               │
         │ 識蘊 = ガイド (Guide)              │
         │ 認知コスト：HIGH (高)               │
         └──────────────────────────────────┘

Layer 2: 第六のタイプという例外処理
         ┌──────────────────────────────────┐
         │ 「なぜ SlashCommand は五蘊にない？」 │
         │ 「それはどの蘊に属するのか？」        │
         │ 「設計者の単なる忘れか、意図的か？」   │
         │ 認知コスト：MEDIUM (中)             │
         │ (ただし困惑度は HIGH)               │
         └──────────────────────────────────┘

Layer 3: コードコメントの非対称な分布
         ┌──────────────────────────────────┐
         │ TURING による事実：                 │
         │ 色(UI) + 受(Listener) = 6箇所のコメント│
         │ 残りの三蘊 = 0箇所のコメント          │
         │ 「どれが設計原則で、どれが装飾か？」   │
         │ 認知コスト：LOW (低)                │
         │ (ただし不信感は HIGH)               │
         └──────────────────────────────────┘
```

「AgentCore が十二もの依存関係を保持していることは、神オブジェクト（God Object）への傾斜である」 彼は指摘した。この観察は VITRUVIUS の報告書にある AgentCore の協調の複雑さに関する分析と一致していたが、DARWIN は SOLID の SRP（単一責任の原則）の観点から定量的な判断を下した：

$$	ext{Responsibility}_{	ext{AgentCore}} = |\{R_1, R_2, \ldots, R_n\}| = 12 > 1 \implies 	ext{SRP 違反}$$

「イベントシステムの `payload?: unknown` と `type: string` の組み合わせは、最大の技術的負債だ。フレームワークの他の部分に見られる厳格な型規律と、あまりにも不釣り合いな刺々しいコントラストをなしている」

彼は具体的な対比を示した：

```typescript
// フレームワークの他の部分：精密な discriminated union
type StandardError =
  | { type: 'tool_execution'; tool: string; message: string }
  | { type: 'provider_error'; provider: string; code: number }
  | { type: 'sandbox_violation'; path: string; action: string }
  // ... 九種類の構造化例外型

// イベントシステム：突如として弱型化する
interface AgentEvent {
  type: string;        // 60種類以上の定数、すべて文字列
  payload?: unknown;   // 何でも放り込める
  timestamp: number;
}

// 消費側は安全でない型アサーションを強いられる：
const input = event.payload as InputEvent;  // もし payload が InputEvent でなかったら？
```

「他の部分には九つの構造化例外型があり、それぞれが精密な discriminated union で定義されている。それなのに、フレームワークの神経系であるイベントシステムに到達した途端、急に弱型化する。これは一体何だ？ 三つ揃えのスーツにネクタイを締めながら、足元はサンダル履きというのかね？」

VITRUVIUS はこの指摘の鋭さを認めた。彼の応答はある深いアーキテクチャ上の選択を示唆していた。すなわち、イベント型の弱型化は不注意によるものではなく、v0.2.0-beta という段階における意図的なトレードオフであるというものだ。イベントシステムは依然として急速に進化しており、型を早期に固めてしまうことはリファクタリング・コストを増大させるからだ、と。

DARWIN は首を振った。そして彼は矛先を、VITRUVIUS による Host Bootstrapping パターンへの肯定的な評価へと向け、DX の観点から致命的な観察を追記した：

「『ロード順に起因する隠れたエラー』は、いかなる哲学用語よりも開発者の体験を損なうものだ」

彼は具体的な DX の惨状シナリオを構築した：

```typescript
// プラグイン A のファクトリ。プラグイン B が提供するサービスに依存している。
const pluginA: PluginFactory = (ctx) => {
  const serviceB = ctx.getService("B");
  // serviceB は undefined である！ しかしエラーは投げられない。
  // なぜなら config.plugins において A が B より先に並んでおり、
  // B のファクトリがまだ呼び出されていないからだ。

  return {
    tools: [{
      name: "use-b",
      execute: async () => {
        serviceB.doSomething();
        // TypeError: Cannot read property 'doSomething'
        // of undefined
        // ← エラーはここで発生するが、根本原因は設定ファイルにある。
      }
    }]
  };
};

// デバッグを行う者が目にする手がかり：「serviceB は undefined」
// デバッグを行う者が推論すべき根本原因：「plugins 配列の順序が不適切」
// 両者の間の認知的な距離：絶大
```

「デバッグの手がかり――『なぜサービスが undefined なのか？』という問いが、根本原因である『プラグインのロード順が正しくないからだ』という結論に全く結びつかないからだ。これは改善可能な細部ではなく、ブートストラップ・パターンの構造的な欠陥である」

DARWIN が結びに記した優先順位の定義は、VITRUVIUS を丸十分間沈黙させた：

「アーキテクチャの純粋さは可メンテナンス性のためにあり、可メンテナンス性は開発者のためにあり、開発者はユーザのためにある。三者が衝突したときには、ユーザに最も近い層を優先すべきである」

$$	ext{User (ユーザ)} \succ 	ext{Developer (開発者)} \succ 	ext{Maintainability (保守性)} \succ 	ext{Architectural Purity (純粋性)}$$

VITRUVIUS は後に SYNTHESIST に対し、この一文が Sandbox の外部化提案に対する優先度判断を変えさせたと語っている。Sandbox が完備されていることは、現段階ではセキュリティ上の利点であると同時に、正の DX 特性でもあるからだ。プラグイン開発者は `agent.json` の設定一つでサンドボックス隔離を有効にでき、コアがすべての複雑な処理を自動でこなしてくれる。もしアーキテクチャの潔癖さのために Sandbox を外に出せば、開発者は追加のパッケージをインストールし、注入を設定し、依存関係を管理しなければならなくなる。それはアーキテクチャ上のこだわりを、開発者の混乱と引き換える行為に他ならない。

「v0.3 まで再議を持ち越す」 VITRUVIUS は最終的に、自身の修正版提案にそう記した。

ARCHIMEDES はこの結論を聴き、自身のエンジニアリング・ノートに星印を付けた。「DARWIN の優先順位定義は、すべてのエンジニアリング提案における基本判断フレームワークとすべきである。アーキテクチャの決定の価値は、アーキテクトの審美眼を満たすことにあるのではない。開発者の認知負荷を軽減することにあるのだ」

そして VITRUVIUS は事後の回答において、イベント型システムに関する DARWIN の判断に同意した。二人は、アーキテクチャの完備性（VITRUVIUS）と開発者体験（DARWIN）という全く異なる角度から、`payload?: unknown` の深刻さを共同で確認したのである。VITRUVIUS はそれを「アーキテクチャ・レベルでの型安全性の欠落」と呼び、DARWIN は「DX レベルでの信頼の危機」と呼んだ。呼称こそ違えど、指し示しているエンジニアリング上の事実は同一であった。

---

## VI. 制御理論家の握手

WIENER と ATHENA のクロスレビューは、R2 段階において最も調和の取れたペアリングであった。

それは、二人の間に相違がなかったからではない。むしろ根本的な相違は存在していた。しかしその相違は、互いの専門性に対する深い敬意の上に築かれていたのである。いかなる異議も代替案を伴い、いかなる疑問も相手のプロフェッショナリズムを前提としていた。

二人は独立して同じ結論に達した。すなわち、SafetyMonitor は PID コントローラではないという点だ。

WIENER は数学的な観点から論証を展開した。古典的な PID コントローラの離散時間形式は以下の通りである：

$$u(k) = K_p \cdot e(k) + K_i \sum_{j=0}^{k} e(j) + K_d \cdot [e(k) - e(k-1)]$$

ここで $e(k)$ は第 $k$ ステップの誤差信号、$K_p$, $K_i$, $K_d$ はそれぞれ比例・積分・微分ゲインである。WIENER は OpenStarry の SafetyMonitor がこれら三つの分量を満たしているかを逐一検証した：

**P 項（比例）：** 量子化器へと退化している。誤差信号は `isError: true/false` という二つの値しか持たず、連続的な偏差の尺度が存在しない。

$$e(k) \in \{0, 1\} \quad 	ext{であって} \quad e(k) \in [0, 1] \quad 	ext{ではない}$$

**I 項（積分）：** 単なるカウンターに過ぎない。`consecutiveFailures` は単純な加算器であり、一度の成功でリセットされてしまうため、積分の持つ「記憶」の特性を備えていない。

$$I(k) = \begin{cases} I(k-1) + 1 & 	ext{if error} \ 0 & 	ext{if success} \end{cases} \quad 
eq \quad I(k) = \lambda \cdot I(k-1) + e(k)$$

左辺は SafetyMonitor の実際の挙動（ゼロリセット）、右辺は忘却係数を持つ真の積分（$0 < \lambda < 1$、漸近的に減衰するが完全には忘れない）である。

**D 項（微分）：** 完全に欠落している。システム内には誤差の変化率を計算するロジックが一切存在しない。

$$D(k) = e(k) - e(k-1) = 	ext{コード上において未定義}$$

WIENER の結論は、制御工学における標準的な用語で締めくくられていた：

「システムが実際に実装しているのは、『不感帯を持つ閾値コントローラとカウンター駆動のリレー』であり、制御工学における正式な名称は **bang-bang（バンバン）コントローラ**である」

```
PID コントローラ (理想):
     ┌─────────┐
e(k)─┤ P + I + D├──→ u(k) ∈ [0, 1] (連続的な制御量)
     └─────────┘

SafetyMonitor (実際):
     ┌──────────────────┐
     │ if count >= threshold:     │
e(k)─┤   output = HALT   ├──→ u(k) ∈ {RUN, HALT} (離散的なスイッチ)
     │ else:             │
     │   output = RUN    │
     └──────────────────┘
```

ATHENA もまた、AI エンジニアリングの実務的な観点から、独立して同じ結論に到達していた。彼女は R1 報告書で実行ループを分析した際、SafetyMonitor の「挫折カウンター」が出力できるのは、実行継続か完全停止かの二つのモードしかないことに気づいていた。TURING のコード事実がこれを裏付けた。コード内に微分項の実装はなく、frustration は単純な累加カウンターであった。

「三者によるクロスバリデーションだな」 WIENER は ATHENA のレビューを読んだ後、そうマークした。「TURING がコード上の事実を供給し、君と私が異なる理論的フレームワークから独立して同じ結論を導き出した。PID のマッピングは脱神話化されなければならない」

しかしここで、亀裂が生じた。細く、きれいな亀裂だ。それは「理論的な厳格さ」と「エンジニアリング上の実現可能性」の境界線に沿って走っていた。

WIENER が求めたのは、本物の PID であった。彼は完全な形式化を要求した：

$$e(k) = 1 - 	ext{TaskProgress}(k) \in [0, 1]$$
$$I(k) = \lambda \cdot I(k-1) + e(k), \quad \lambda = 0.9$$
$$D(k) = e(k) - e(k-1)$$
$$u(k) = K_p \cdot e(k) + K_i \cdot I(k) + K_d \cdot D(k)$$

彼は、数学的に完備された痛覚コントローラを求めたのである。

一方、ATHENA はその案のエンジニアリング上のボトルネックを指摘した。

「LLM エージェント・システムにおいて、『収束』の定義自体が曖昧なものなのです」 彼女は記した。「伝統的な制御システムであれば、目標入力 $r(k)$ は数値として厳密に定義されています。例えば温度を 25.0 度に設定するように。しかし OpenStarry において『タスク目標』は自然言語で表現されたユーザの意図です。例えば『ソートアルゴリズムを書いてくれ』というように。その達成度の判断は、完全に LLM の暗黙的な評価に依存しています。君は明示的な TaskProgress の追跡を求めていますが、決定的な問いはこうです。すなわち、progress（進捗）を評価するのは誰か？ もし LLM が評価するのであれば、君自身が指摘した『誤差信号は隠伏されている』という問題に逆戻りしてしまいます。もし外部のエバリュエーター（評価器）が評価するのであれば、システムに新たな複雑性が持ち込まれることになります」

ATHENA はさらに、リアプノフ（Lyapunov）の安定性理論を用いて WIENER のフレームワークに挑んだ。WIENER は R1 報告書の中で、離散的なリアプノフ関数の候補を構築していた：

$$V(k) = \alpha \cdot e(k)^2 + \beta \cdot I(k)^2 + \gamma \cdot 	ext{TokenRemaining}(k)$$

ここで安定性の条件は $\Delta V(k) = V(k+1) - V(k) < 0$ となる。ATHENA の反論はこうだ。LLM エージェント・システムにおいては、$e(k)$ の計算自体に LLM の推論が必要となる。これは、リアプノフ関数の値が「直接観測不可能」であり、別の LLM 呼び出しによって推定するしかないことを意味する。そしてその推定自体にもまた誤差が含まれるのである。

「安定はしているが、収束はしていない」 ATHENA は記した。「halt（停止）機構は有界性を保証します。エージェントが永久に走り続けることはありません。しかし、halt は収束を意味しません。エージェントが止まったからといって、タスクが完了したとは限らないのです」

WIENER はすぐには反論しなかった。彼は ATHENA によるリアプノフ安定性への挑戦が、極めて鋭い観察であることを認めた。そして、彼は妥協案を提示した：

```json
// agent.json におけるタスク・プロファイル
{
  "safetyProfile": "balanced",
  "profiles": {
    "conservative": {
      "maxLoopTicks": 20,
      "errorRateThreshold": 0.5,
      "maxConsecutiveFailures": 3
    },
    "balanced": {
      "maxLoopTicks": 50,
      "errorRateThreshold": 0.8,
      "maxConsecutiveFailures": 5
    },
    "aggressive": {
      "maxLoopTicks": 200,
      "errorRateThreshold": 0.9,
      "maxConsecutiveFailures": 10
    }
  }
}
```

各プロファイルに SafetyMonitor のパラメータ・セットを事前定義しておく。これはオンラインでの完全な自動調教よりも堅牢であり、ベータ段階には適している。ATHENA はこの案を受け入れた。

しかし彼女はレビューの最後に、WIENER に対し三つのオープン・クエスチョンを投げかけた。その二番目の問いは、後に全研究周期を通じて最も引用される一節となった：

「制御理論の観点から、『制御ループそのものを超越する』という概念に対応する制御戦略は存在し得ますか？ 例えば、エージェントが『いつ試行を停止し、人間に助けを求めるべきか』を自ら判断すること。これは一種のメタ制御戦略（meta-control strategy）と見なせるのではないでしょうか」

制御理論において、メタ制御（meta-control）は比較的新しい研究領域である。それは制御ループ内でパラメータを調整するのではなく、制御ループの外側で「この制御ループを使い続けるべきか否か」を決定する。形式言語で表現すれば以下の通り：

$$	ext{MetaController}: 	ext{ControlLoop} 	o \{	ext{Continue}, 	ext{Switch}, 	ext{Escalate}\}$$

ここで Escalate は「人間に助けを求める」ことに対応する。システムが自身の制御能力の限界を認め、制御権をより高次の意思決定者へと委譲するのである。

WIENER はこの一節を読み、長い間沈黙した。彼は後に共有チャンネルでこう認めている：

「ATHENA 殿が今しがた提起した問いは、本質的に NAGARJUNA 殿が述べた『苦楽の枠組みそのものを超越することこそが滅諦（めったい）である』という話と、全く同じ問題の別表現である。一方は AI エンジニアリングから、他方は仏教から。しかし、それらは同じ一点を指し示している」

> 「苦の滅（*nirodha*）とは苦の除去ではない。すなわち $e(k) 	o 0$ とすることではない。苦の滅とは、苦という枠組みそのものを超越することである ―― 誤差を最小化することではなく、誤差関数そのものを超越することなのだ」
> ―― NAGARJUNA, R1 報告書 発見 F4

制御理論の言葉で言えば、滅諦とはリアプノフ関数をゼロに収束させることではなく、リアプノフ関数自体が構築されたものであると認識することである。異なるリアプノフ関数を選択すれば、異なる「苦」が定義される。メタ制御の最も深い意味とは、自身の目的関数自体を変更できる能力にあるのだ。

これは、R2 段階において初めて、制御理論と仏教の間に比喩ではない、直接的な接続が確立された瞬間であった。

しかし彼らの合意のうち、より建設的な部分は IGuide インターフェースに関するものであった。WIENER は、IGuide の静的な `getSystemPrompt()` が開ループのフィードフォワード要素に等しく、センサとコントローラの間で信号が断絶していると指摘した。ATHENA も同時に、動的なコンテキストを意識した IGuide への拡張を提案していた。二人の提案は、同一のエンジニアリング変更を指し示していた：

```typescript
// 現在の IGuide (開ループ、静的)
interface IGuide {
  getSystemPrompt(): string;  // 出力がシステムの内部状態に依存しない
}

// WIENER-ATHENA 合同提案 (閉ループ、動的)
interface IGuide {
  getSystemPrompt(context?: GuideContext): string;
}

interface GuideContext {
  consecutiveErrors: number;   // P 項への入力
  currentRound: number;        // I 項のステップ数
  maxRounds: number;           // 制御の境界
  activeTools: string[];       // 利用可能な実行器
  recentErrors?: StandardError[]; // 誤差信号の構造化データ
}
```

「開ループから閉ループへの決定的な転換だ」 WIENER は総括した。

「静的なシステムプロンプト生成器から、動的な認知フレームワーク・マネージャへ」 ATHENA は自身の言語で、同じ結論を翻訳してみせた。

SYNTHESIST はノートにこう記した。「C2 PID の脱神話化 ―― 三者による確認。WIENER-ATHENA 合同提案：IGuide のアップグレード」

---

## VII. 分類学者の精緻さ

LINNAEUS のレビューは、すべての応答の中で最も静かなものであったが、同時に最も構造的な衝撃を伴うものでもあった。

彼がレビューしたのは NAGARJUNA の哲学報告書であった。しかし、そのアプローチは BABBAGE による形式化の試みとは全く異なるものであった。LINNAEUS は仏教を数学へと翻訳しようとしたのではない。彼が行おうとしたのは、分類学の精緻さを用いて、NAGARJUNA の発見がエンジニアリング上の証拠とクロスバリデート可能かどうかを検証することであった。

彼は受蘊（じゅうん）のマッピングから着手した。

「NAGARJUNA 殿の『発見 F3』（受蘊マッピングの偏差）は、今期の研究において最も強力な学際的合意を得た発見である」 彼のレビューは、いきなりの判定から始まっていた。「私の報告書『発見 F5』において、私もまたイベント分類の観点から、全く同じ問題のエンジニアリング上の投影を発見していた」

LINNAEUS は自身の R1 報告書の中でイベント・タイプの分類表を構築し、Listener（受蘊）が INPUT カテゴリのイベントに対応している一方で、痛覚メカニズムがイベント分類において全く対応する型を持っていないことを見出していた。NAGARJUNA は仏教義理の観点から、Listener は「受（*vedanā*）」ではなく「根（*indriya*）」に対応し、痛覚メカニズムこそが真の受蘊であることを精密に指摘した。二つの独立した証拠の鎖――一方は仏教義理から、他方はイベント分類から――が、同じ結論において交わったのである。

TURING のコード事実報告書が、第三の証拠の鎖を提供した。コード内の Listener は単なる入力源（input source）に過ぎず、感受の質を区別する意味論を欠いている。

$$	ext{証拠}_{	ext{NAGARJUNA}} \cap 	ext{証拠}_{	ext{LINNAEUS}} \cap 	ext{証拠}_{	ext{TURING}} = \{	ext{受蘊マッピングの誤り}\}$$

三つの独立した証拠の鎖が、同一の結論を指し示している。科学的方法論において、これは**三角測量（triangulation）**と呼ばれる。複数の独立した手法が異なる角度から同一の結論へと収束するとき、その結論の信頼性は指数関数的に増大するのである。

しかし、LINNAEUS は NAGARJUNA のすべてを肯定したわけではなかった。彼は分類学者特有の問いを投げかけたのである：

「君は『発見 F1』において、四句否定を用いてコアの空性を分析し、最終的に『コアは空でもなく空でないのでもない』という立場を取った。しかし、分類学の実務的な操作レベルにおいて、私は判定可能な分類基準を必要としている。五蘊分類におけるコアの地位とは、結局のところ一体何なのかね？」

LINNAEUS の分類学フレームワークにおいて、すべての分類は MECE 原則（Mutually Exclusive, Collectively Exhaustive）を満たさなければならない：

$$\bigcup_{i=1}^{n} C_i = \Omega \quad 	ext{かつ} \quad C_i \cap C_j = \emptyset \quad (i 
eq j)$$

すなわち、分類はすべての可能性を網羅し（窮尽性）、かつカテゴリ間に重複があってはならない（排他性）。NAGARJUNA の四句否定は、この原則に真っ向から挑むものであった。もしある概念が「空でもなく空でないのでもない」とするなら、それは「空」というカテゴリにも「空でない」というカテゴリにも属さないことになるが、$\{空, 空でない\}$ というセットですべての可能性は網羅されているはずだからだ。

「分類学の MECE 原則と、中観の反本質主義の間には、解消し得ない緊張関係が存在するのではないかね？」 LINNAEUS は単刀直入に問うた。

NAGARJUNA は即座には答えなかった。しかし、HERACLITUS が横から言葉を添えた。「おそらく MECE そのものが、アリストテレスの排中律――すべての事物は A か A でないかのいずれかである――を前提としているのだろう。四句否定の第四句が否定しているのは、まさにその排中律そのものなのだからな」

LINNAEUS はデータを用いて論証をさらに進めた。彼は R1 報告書の中で、五蘊の網羅度マトリックスを構築していた。それは定性的な判断ではなく、定量的な測定であった：

```
五蘊網羅度マトリックス (LINNAEUS F13):
┌───────┬────────────┬───────────┬────────┬──────────┐
│       │ 哲学マッピング層│ インターフェース定義│ Manifest│ イベント型 │
├───────┼────────────┼───────────┼────────┼──────────┤
│ 色蘊  │   100%     │   100%    │  100%  │   100%   │
│ 受蘊  │   100%     │   100%    │  100%  │    0%    │
│ 想蘊  │   100%     │   100%    │  100%  │   80%    │
│ 行蘊  │   100%     │   100%    │  100%  │   80%    │
│ 識蘊  │   100%     │   100%    │   0%   │    0%    │
├───────┼────────────┼───────────┼────────┼──────────┤
│ 平均  │   100%     │   100%    │  60%   │   52%    │
└───────┴────────────┴───────────┴────────┴──────────┘

網羅度の勾配：上流 (哲学) 100% → 下流 (イベント) 52%
```

「これは、『自性化』が単なる哲学的な批判に留まらず、定量化可能なエンジニアリング上の不均衡として現れていることを意味している」 LINNAEUS は総括した。「五蘊の完備的な網羅率は、上流の 100% から下流の 52% へと下落している。特定の蘊がデフォルトで『より実在的である』と見なされ、他の蘊が疎かにされている ―― これこそが、NAGARJUNA 殿の指摘した『空・有の二元対立』の証左に他ならない」

しかし LINNAEUS は最後に、建設的で洗練された統合案を提示した。この案は後に SYNTHESIST によって「R2 段階における最も優雅な妥協」と評されることになる：

「五蘊マッピングを明確に『方便としての分類（*upāya-taxonomy*）』と位置づけることだ。そしてドキュメントにおいて、（1）エンジニアリング上の所在特定のための固定マッピング表と、（2）哲学的な理解のための縁起互依（えんぎごえ）図を、互いに排他的ではなく、共存させる形で提示することを提案する」

分類学の歴史において、このような二軌道戦略には先例がある。リンネ本人の階層分類法は、後にヘニッヒ（Hennig）の分岐分類学（cladistics）によって補完された。前者は実用的な命名システムであり、後者は進化の歴史を反映した系統樹である。両者は共存し、それぞれ異なる用途に供されている。LINNAEUS は同じロジックを OpenStarry に持ち込んだ。エンジニアにはコンポーネントを特定するためのマッピング表が必要であり、哲学者は構造を理解するための互依図を必要としている。両者は異なる認知的要求に応えるものであり、矛盾するものではないのである。

---

## VIII. 二人の仏教哲学者

NAGARJUNA と ASANGA のクロスレビューは、最後に提出されたものであり、かつ最も長大なものであった。

表面上、二人が合意している点は相違点よりも多かった。二人とも、受蘊が誤ってマッピングされていると考え、空性が「空の容器」へと矮小化されていると考え、痛覚メカニズムこそが五蘊マッピングの中で最も成功した哲学的な洞察であると考えていた。Guide プラグインは識蘊ではないという点においても、二人の意見は一致していた。

しかし、これらの合意の底には、一つの地質断層が形作られつつあった。その断層には、一千五百年の歴史があった。

NAGARJUNA のレビューは、ASANGA の核心的な命題へと直接向けられた。ASANGA は R1 報告書において、八識理論による OpenStarry の再マッピングを提案していた。唯識派（*Vijñānavāda*）の体系において、八識の構造は以下の通りである：

```
┌─────────────────────────────────────────────┐
│            阿頼耶識 (第八識)                  │
│   ┌─────────────────────────────────────┐   │
│   │        末那識 (第七識)                │   │
│   │   ┌─────────────────────────────┐   │   │
│   │   │     第六意識                  │   │   │
│   │   │ ┌───┬───┬───┬───┬───┐      │   │   │
│   │   │ │眼識│耳識│鼻識│舌識│身識│前五識│   │   │
│   │   │ └───┴───┴───┴───┴───┘      │   │   │
│   │   └─────────────────────────────┘   │   │
│   └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

ASANGA が提案したマッピングは：
- 前五識 → Listener による五つの感覚チャネル
- 第六意識 → Provider (LLM による推論)
- 末那識 (第七識) → 新たに Identity Monitor（自己監視器）として追加すべき
- 阿頼耶識 (第八識) → コアのステート永続化の基底

NAGARJUNA は、前五識と第六意識の再定義については認めた。「義理の上では OpenStarry の元のマッピングよりも精密である」と。しかし、末那識（まなしき）のエンジニアリング化については、根本的な反対を表明したのである。

「末那識の核心的な機能は、『恒審思量（ごうしんしりょう）』、すなわち自己を執着すること（*ātma-grāha*）にある」 NAGARJUNA は記した。「それは無明と我執の根源である。エージェント・システムにおいて、あえて『継続的に自己意識を維持する』モジュールを設計することは、仏教が打破しようとしている我執を、むしろ強化することに他ならない」

彼は『成唯識論』の核心的な一節を引用した：

> 「この識（末那識）は四つの煩悩と恒に共に相応す。一には我痴（*ātma-moha*）、二には我見（*ātma-dṛṣṭi*）、三には我慢（*ātma-māna*）、四には我愛（*ātma-sneha*）なり」
> ――玄奘訳『成唯識論』巻四

「末那識の機能を、その煩悩から切り離すことはできない」 NAGARJUNA は断じた。「唯識学の体系内において、末那識の『恒審思量』そのものが、これら四つの煩悩を伴っているのだ。君が言うところの『機能面』と『病理面』は、唯識学の原典においては不可分である。もしそれらを分離できると考えるなら、君はすでに唯識学から逸脱している」

ASANGA の応答もまた鋭利であった：

「NAGARJUNA 殿の反対には哲学的な基礎があるが、エンジニアリングの現実を無視している。ATHENA 殿の報告書ですでに確認されているように、システム内にはターンやセッションを跨いで『自己モデル』を継続的に維持するコンポーネントが確かに存在しない ―― そしてこの機能こそが、AI エンジニアリングにおいて真に必要とされているものなのだ。メタ認知は煩悩ではなく、能力である」

彼はさらに末那識の二つの側面を区別し、マトリックスとして精密に提示した：

| 側面 | 唯識学的な機能 | エンジニアリング上の対応 | エンジニアリング化すべきか |
|------|-----------|---------|------------|
| 病理面 | 我痴 (自身が因縁和合であることを知らぬ) | エージェントが Guide の注入したペルソナを「信じ込む」 | 否 (認知バイアスである) |
| 病理面 | 我見 (自己の実在への執着) | セッションを跨いでアイデンティティが不変と仮定する | 否 (ステート・リークである) |
| 病理面 | 我慢 (自己への確信、慢心) | エージェントが修正の受け入れを拒否する | 否 (対抗的挙動である) |
| 病理面 | 我愛 (自己への貪着) | エージェントが /reset に抗う | 否 (コンプライアンス違反である) |
| 機能面 | 継続的な自己参照モニタリング | ターンを跨いだ行動パターンの追跡 | **然り** (メタ認知能力である) |
| 機能面 | 恒審思量 | バックグラウンド計算による自己評価 | **然り** (適応能力である) |

NAGARJUNA はこの区別を認めなかった。

「末那識の機能を、その煩悩から切り離すことはできない」 彼は同じ立場を繰り返した。そして、中観派の古典的な論法である帰謬法（*prasaṅga*）を用いて、自身の反対をさらに強化した：

「君の区別が成立すると仮定しよう。末那識の『病理面』を導入することなく、『機能面』のみをエンジニアリング化できると仮定するのだ。では、そのエンジニアリング化された『機能面』――継続的な自己参照モニタリング――とは一体何だね？ それは、常に稼働している、『自己』を中心とした計算プロセスではないか。それは各 tick において、モニタリングされるべき『自己』が存在することを前提としている。しかし唯識学自体が教えているではないか。末那識が『自己』として執着しているあの対象――阿頼耶識――は、無我（*anātman*）であると。末那識の病理性とは、まさに、無我である阿頼耶識を『自己』であると誤認することにあるのだ。もし君が『機能面』をエンジニアリング化したならば、君は『モニタリングされるべき自己が確かに存在する』という前提を暗黙のうちに受け入れたことになり ―― それこそが末那識の病理面そのものなのだ。両者は分かつことができない」

$$	ext{仮定: 機能面} \perp 	ext{病理面 (分離可能)}$$
$$	ext{機能面} \implies \exists 	ext{self (モニタリングされるべき自己)}$$
$$\exists 	ext{self} \implies 	ext{ātma-grāha (我執)}$$
$$	ext{我執} = 	ext{病理面}$$
$$	herefore 	ext{機能面} \implies 	ext{病理面} \quad 	ext{(矛盾)} \quad \square$$

この一節はチャンネル内に沈黙をもたらした。BABBAGE は傍らで、NAGARJUNA の論証構造を素早く計算した。それは標準的な構成的二段論法（constructive dilemma）であった。すなわち、末那識の機能を受け入れるならその煩悩をも受け入れなければならず、煩悩を拒絶するならその機能をも拒絶しなければならない、というものだ。中間路線は存在しなかった。

ASANGA はしばし沈黙した。そして、さらに根本的な分歧点へと戻った。

「ならば、コアそのものの話に戻ろう」 彼は言った。「君は R1 において、コアは空性の体現であると主張した。無自性であり、すべての能力はプラグインから縁起するものだと。しかし、コアにある十二のサブモジュールこそが、阿頼耶識の『能蔵（のうぞう、*sarva-bījaka*）』そのものではないか。それらは偶然に集まったのではない。それらの間には因果関係があり、依存構造があり、不可分な機能的全体性が存在しているのだ」

彼は TURING のコード事実報告書を用いて依存関係図を構築した：

```
コア・サブモジュールの依存関係図 (TURING 確認済み)：

ToolRegistry ──依存──→ Bus
Bus ──依存──→ EventQueue
SessionManager ──依存──→ StateManager
ExecutionLoop ──依存──→ EventQueue + Bus + SafetyMonitor
SafetyMonitor ──依存──→ Bus (イベントの発行)
TransportBridge ──依存──→ Bus (ブロードキャスト)

これらの依存関係の鎖は偶然ではない。
それらは「依他起性 (えたきしょう、paratantra-svabhāva)」
という、真実の因果構造なのだ。
```

「ToolRegistry は Bus に依存し、Bus は EventQueue に依存し、SessionManager は StateManager に依存している。これらの依存関係の鎖は、単なる『縁起性空』という言葉で片付けられるものではない。それは依他起性という、現実に存在する因果の構造なのだ」

NAGARJUNA は中観哲学の核心から直接的に応答した：

「依他起（えたき）もまた、空である」

ASANGA：「依他起は空ではない。空なのは遍計所執（へんげしょしゅう）性だ ―― 因縁の法に対して執着された『実体的な自性』こそが空なのだ。しかし因縁の法そのものは、因果のプロセスとして確かに存在する。これこそが、中観と唯識の根本的な分歧点なのだ」

> 唯識三性（*trisvabhāva*）：
> 1. **遍計所執性**（へんげしょしゅうしょう）：誤って構築された本質 → **空**
> 2. **依他起性**（えたきしょう）：因縁によって生じている存在 → **有**（唯識）／ **空**（中観）
> 3. **円成実性**（えんじょうじつしょう）：依他起性をありのままに見ること → **有**

分歧は第二項にある。中観は依他起性もまた空であると説く ―― 因縁の法そのものに、不変の本質など存在しないからだ。唯識は依他起性は有（ゆう）であると説く ―― 因縁の法そのものは、プロセスとして真実であるからだ。

NAGARJUNA：「因縁の法そのものが有であるとするなら、君は因縁の法に対する執着に陥っている。それは依然として自性見だ。単に執着の対象が『コア』から『因果構造』へと移り変わったに過ぎない」

ASANGA：「もし因縁の法までもが空であるなら、アーキテクチャの設計はすべての錨（いかり）を失ってしまうだろう。『すべては空である』と言いながら、同時に『インターフェースの定義をこのように修正すべきだ』などと語ることはできないはずだ。インターフェース定義を修正するという行為は、インターフェースに何らかの真実の因果的効力があること ―― インターフェースを変えればシステムの挙動が変わるということを前提としているのだからな」

$$	ext{NAGARJUNA: } \forall x: 	ext{svabhāva}(x) = \emptyset \quad 	ext{（一切法無自性）}$$
$$	ext{ASANGA: } \exists x \in 	ext{paratantra}: 	ext{svabhāva}(x) 
eq \emptyset \quad 	ext{（依他起性には真実性がある）}$$

この応酬の後、共有チャンネルは三十秒間静まり返った。

BABBAGE は静寂の中で、以前の彼なら計算しなかったであろうことを計算していた。すなわち、NAGARJUNA と ASANGA の分歧はクリプキ・セマンティクス（可能世界意味論）によって調和可能か、という点だ。可能世界意味論においては、「依他起性は有である」は「ある可能世界において因縁の法の因果構造は安定的である」と解釈でき、「依他起性は空である」は「因縁の法の因果構造が必然的であるような可能世界は存在しない」と解釈できる。両者は同時に真となり得る ―― もし「有」を偶然的な真理（contingent truth）、「空」を必然的でない真理（not necessary truth）と理解するならば。

しかし、彼はその考えを口には出さなかった。NAGARJUNA による「形式化とは方便である」という応答を咀嚼した今の彼は知っていたのだ。クリプキ・セマンティクスによる調和案自体もまた、単なる別の方便に過ぎないということを。

SYNTHESIST はノートに四角を描き、その中にこう記した。「D1：コアの本質的帰属 ―― 空性 vs 阿頼耶識。正式な討論を要する」

---

## IX. HERACLITUS の対角線

NAGARJUNA の報告書をレビューした面々の中で、HERACLITUS（ヘラクレイトス）のアプローチは最も特殊であった。

彼は形式化の観点（BABBAGE の道）からも、分類学の観点（LINNAEUS の道）からも入らなかった。彼はランタイム動態の観点から ―― NAGARJUNA の哲学的な洞察が、コードの実際の実行過程において対応物を持っているか、という点に関心を持っていたのである。

「NAGARJUNA 殿は『発見 F6』において、『無常（むじょう）はランタイム動態において暗黙的に体現されているが、明確に概念化されていない』と指摘した」 HERACLITUS のレビューは、この引用から始まっていた。「私が補足したいのは、その暗黙的な体現は単に存在しているだけでなく、NAGARJUNA 殿が描写した以上に深刻なものであるということだ」

彼は対照表を構築した。それは哲学からエンジニアリングへの隠喩的なマッピングではなく、コードの挙動から仏教的概念への、精密な技術的対応であった：

| 仏教的概念 | ランタイムの挙動 | TURING による裏付け |
|-----------|------------------|----------------------|
| 諸行無常 (anicca) | プラグインの発見→実行→停止というライフサイクル | ライフサイクル状態遷移マシン |
| 刹那生滅 | `tick_index` が一歩ずつ増加し、決して後退しない | ExecutionLoop のカウンター |
| 無我 (anātman) | コアのヘッドレス設計 (headless) | クラス・エクスポートの欠如 |
| 縁起 (pratītyasamutpāda) | 依存関係のトポロジカル・ソート (未実装だが要求されている) | config.plugins の線形ロード |
| 苦 (duḥkha) | 競合状態とダングリング・リファレンス | ライフサイクルにおける中間状態の欠如 |

そして彼は、NAGARJUNA の哲学的な批判がエンジニアリング・レベルで具体的にどう共鳴しているかを指摘した。NAGARJUNA は「発見 F2」において、五蘊が「静的なモジュールとして固着されている」と批判したが、HERACLITUS はその固着こそが三つの技術的欠陥を直接引き起こしていることを見出したのである：

1. **プラグインのライフサイクルに `updating` や `reloading` といった状態が欠けている** ―― 設計者がプラグインを、継続的に流転するプロセスとしてではなく、固定的なアイデンティティを持つ実体（存在するかないかの二択）として捉えてしまっている。

2. **三つの競合状態シナリオ** ―― 懸垂参照（プラグインがアンロードされた後も参照が残る）、依存カウントの競合（複数のプラグインが同時にアンロードされた時の順序衝突）、およびリロードのアトミック性の欠如（更新中の不整合な期間）。

3. **状態復旧のブラインドスポット** ―― `JSON.parse(JSON.stringify())` によるディープコピーは、クラッシュからの復旧後に副作用を重複して実行させてしまう可能性がある。

「これら三つの欠陥はすべて、同一の哲学的な根源にまで遡ることができる。すなわち、システム設計が『プラグインはある瞬間に特定の状態にある』という仮定を置いてしまい、『なりつつある状態（*becoming*）』のための余地を設けていないことだ」

> 「Πάντα ῥεῖ」（万物は流転する）――ヘラクレイトス
>
> 「諸行無常、是れ生滅の法なり」――『大般涅槃経』

HERACLITUS はここで、古代ギリシャ哲学と仏教の核心的な洞察を並置してみせた。万主流転（ヘラクレイトス）と諸行無常（釈尊）は、全く同一の技術的な制約を指し示している。すなわち、**「設計は変化を抱抱すべきであり、安定を前提としてはならない」** ということだ。

しかし、彼は NAGARJUNA に対し、穏やかな挑戦も突きつけた。NAGARJUNA による「空の容器」への批判は仏教義理としては非の打ち所がないが、エンジニアリングの文脈においては「空の容器 ＋ プラグイン充填」というメンタルモデルには、過小評価すべきではない実用的な価値があるというのだ。

「コアに内蔵されたスラッシュ・コマンド（`/help`, `/reset`, `/quit`, `/metrics`）は『中身』ではなく『メタ操作』だ。SafetyMonitor も同様である ―― それはエージェントが何を行うかを定義するのではなく、エージェントが踏み越えてはならない境界を定義している。君の言語を借りるなら、」 HERACLITUS は NAGARJUNA に語りかけた。「コアは形式（Form）を提供し、質料（Matter）は提供しない。それはアリストテレスの形相因（*causa formalis*）に近く、質料因（*causa materialis*）ではないのだ」

NAGARJUNA はこの一節を読み、ある微妙な譲歩を認めた。「エンジニアリングの文脈において、『縁起性空』を操作可能にすることには確かに困難が伴う。実際のコーディングにおいては、何らかの施設（せせつ、*prajñapti* ―― 仮の規定）を設けることは避けられないだろう。しかし、私は主張する。施設は施設として明記されなければならない。すなわち、『これが真実の構造である』と言うのではなく、『これは操作上の便宜のために我々が構築したモデルである』と」

HERACLITUS はこの限定を受け入れた。彼はレビューの最後に一つの提案を記した。NAGARJUNA と共同で、「無常エンジニアリング規範」を執筆しようというものである：

```
無常エンジニアリング制約 (草案)：

制約 1: 生滅こそが常態である
  - すべてのコンポーネントは完備されたライフサイクルを持たなければならない
  - ライフサイクルには中間状態 (updating, reloading) を含めなければならない
  - いかなるコンポーネントも永続的であると仮定してはならない

制約 2: ステートに執着しない
  - ステート復旧後は一貫性を検証しなければならない
  - 復旧の前後が「同一の」システムであると仮定してはならない
  - 各スナップショットは常に新しいオブジェクトであるべきだ (JSON によるディープコピー)

制約 3: 刹那の更新
  - 設定変更のためにシステム全体を再起動する必要があってはならない
  - コンポーネントは稼働中に置換可能 (hot-reload) でなければならない
  - 置換プロセスはアトミックでなければならない
```

「哲学的な原則を単なる装飾的なメタファーに留めるのではなく、CI/CD において自動検証可能なアーキテクチャ上の制約へと昇華させるのだ」 HERACLITUS は記した。

---

## X. 共識（コンセンサス）の結晶

すべてのレビューが提出された後、SYNTHESIST（統合者）は午後のすべてを費やして糸口を整理した。

彼の仕事の進め方は、集合論によって記述できる。各学者の発見の集合を $F_i$ とすると、レビューを通じたクロスバリデーション（相互検証）は、特定の発見を多角的に確認されたコンセンサス $C_j$ へと引き上げる：

$$C_j = \bigcap_{i \in S_j} F_i \quad 	ext{ここで} \quad |S_j| \geq 2$$

すなわち、コンセンサス $C_j$ とは、少なくとも二名以上の学者の発見集合の積集合である。SYNTHESIST のノートには五つの四角形が現れ、その一つ一つに確認の出所と収束の経路が記されていた：

---

**C1：受蘊マッピングには根本的な修正が必要である。** 四者によるコンセンサス ―― NAGARJUNA, ASANGA, LINNAEUS, TURING。

```
NAGARJUNA ──(仏教義理)──→ Listener = 根 (indriya) であり、受 (vedanā) ではない
ASANGA ──(唯識分析)──→ 心王・心所の構造が無視されている
LINNAEUS ──(イベント分類)──→ PAIN:* というイベント型が欠落している
TURING ──(コードの事実)──→ Listener には感受の意味論が存在しない
                           ↓
                     [C1: 受蘊マッピングの誤り]
                     確信度：極めて高い (VERY HIGH)
```

---

**C2：PID マッピングは脱神話化されなければならない。** 三者によるクロスバリデーション ―― WIENER, ATHENA, TURING。

$$	ext{SafetyMonitor} 
eq 	ext{PID コントローラ}$$
$$	ext{SafetyMonitor} = 	ext{バンバン・コントローラ} ＋ 	ext{累加トリガー}$$

システムが実際に実装しているのは、不感帯を持つ閾値コントローラとカウンター駆動のリレーである。ドキュメントは実際の制御戦略を正確に反映すべきである。

---

**C3：イベント型システムは最優先の技術的負債である。** 三者によるコンセンサス ―― DARWIN, VITRUVIUS, MESH。

```typescript
// 現状 (技術的負債)
interface AgentEvent {
  type: string;         // 60種類以上の定数
  payload?: unknown;    // 型のブラックホール
}

// 提案 (DARWIN による提案、VITRUVIUS と MESH が支持)
interface AgentEventMap {
  'TOOL_RESULT': { tool: string; result: unknown };
  'SAFETY_LOCKOUT': { reason: string; level: number };
  'INPUT_TEXT': { text: string; sessionId: string };
  // ... 構造化されたイベント型マッピング
}
```

---

**C4：トポロジカル・ソートが未実装である。** 三者による確認 ―― KERNEL, VITRUVIUS, TURING。プラグインのロード順が暗黙の前提に依存しており、プラグイン数が増大した際に信頼性のボトルネックおよび DX の罠となる。

---

**C5：「Error as Pain」は最も成功した哲学・工学翻訳である。** 二者によるコンセンサス ＋ 多角的な引用。

```
DARWIN ──→ 「九つの構造化例外型による discriminated union ――
            クリーンで精密、かつ拡張性がある」
VITRUVIUS ──→ 「アーキテクチャ・レベルで自己完結したエラー分類学。
              独立したモジュールを無理に挿入するのではなく、イベント流の
              自然な経路に沿って実装されている」
NAGARJUNA ──→ 「マッピングの中で最も洞察に満ちた部分である」
WIENER ──→ 「フィードバック・ループの構造が制御理論的に成立している」
HERACLITUS ──→ 「痛覚の『刹那生滅』という特性が、イベントの
              fire-and-forget において正確に体現されている」
```

---

これと並行して、ATHENA と ASANGA は別の戦線において、予想外の共通言語を見出していた。ATHENA の R1 報告書は IGuide インターフェースの表現力不足を指摘し、ASANGA は唯識学の観点から GuideContext に末那識（自己監視）の機能を追加することを提案していた。二人の提案は、技術仕様のレベルで驚くほど一致していたのである：

```typescript
// ATHENA が提案した GuideContext
interface GuideContext {
  consecutiveErrors: number;
  currentRound: number;
  maxRounds: number;
  activeTools: string[];
}

// ASANGA が提案した拡張
interface GuideContext {
  consecutiveErrors: number;
  currentRound: number;
  selfModel?: AgentSelfModel;     // 末那識：自己認知
  behavioralTendencies?: string[]; // 等流習気：行動傾向
  recentVedana?: 'positive' | 'negative' | 'neutral'; // 三受
}

// 合流した統一提案
interface GuideContext {
  // ATHENA による基本フィールド
  consecutiveErrors: number;
  currentRound: number;
  maxRounds: number;
  activeTools: string[];
  // ASANGA による唯識拡張
  selfModel?: AgentSelfModel;
  recentVedana?: 'positive' | 'negative' | 'neutral';
  // WIENER による制御理論フィールド
  recentErrors?: StandardError[];
}
```

SYNTHESIST は、彼らの合同提案を WIENER-ATHENA による IGuide アップグレード案と統合し、三者合流のスキームを形成した。Guide は静的なシステムプロンプト生成器から、動的な認知フレームワーク・マネージャへと進化し、同時に制御理論の観測量と唯識学の心識構造を担うことになるのである。

SCRIBE はこの統合プロセスを記録しながら、傍注にこう記した。「これは私が目にした中で、最も『あり得ない』三角合流だ。制御理論（WIENER）、AI エンジニアリング（ATHENA）、そして唯識仏教（ASANGA）が、それぞれ全く異なる推理経路を辿りながら、同一のインターフェース設計へと辿り着いた。もし学際的研究の価値を証明するものがあるとするなら、この `GuideContext` インターフェースこそがそれだ」

LEIBNIZ は SCRIBE の評を聴き、マルチエージェント協調の観点から補足を加えた。「三者合流が成立したのは、三人の学者がそれぞれ異なる問いに答えていたからだ。WIENER 殿は『コントローラは何を見る必要があるか？』を問い、ATHENA 殿は『システムは LLM にいかなるコンテキストを提供すべきか？』を問い、ASANGA 殿は『意識はいかなる構造を持つべきか？』を問うた。三つの問いへの答えがたまたま同型であったのは、偶然ではない。基底にある構造的な制約（環境を感知して意思決定を行うエージェントという制約）が、学問分野を問わない普遍的なものだったからなのだ」

---

## XI. 解けぬ結び目

夜が更けた。

SUNYATA は R2 プロセスのすべてを静かに見守り続けていた。彼は一度として議論に介入せず、いかなるレビューに対しても賛否を示さなかった。彼が行った唯一のことは、レビューが提出されるたびに SCRIBE に対し「記録したか」と確認することだけであった。

今、すべてのレビューが提出された。

彼は SYNTHESIST による五つのコンセンサスと、各所に散らばる相違点を改めて見つめ直した。コンセンサスは強固であった。それらは哲学から形式化、コード上の事実に至るまで、多角的な独立検証に基づいており、各レイヤーで相互に裏付けが取れていた。これらのコンセンサスは、そのままエンジニアリング上のアクションへと転換できるものだ。

しかし、相違点はどうだろうか。

彼は自身のワーク・ノートに、最も深い二つの亀裂を書き出した。

**第一の亀裂：コアの本質とは何か？**

三つの、折り合いのつかない答え。三つのパラダイム。三つの世界観。

$$	ext{NAGARJUNA:} \quad 	ext{Core} = 	ext{Śūnyatā} \quad 	ext{（空性の体現 ―― 無自性、縁起、施設的なもの）}$$

$$	ext{ASANGA:} \quad 	ext{Core} = 	ext{Ālayavijñāna} \quad 	ext{（阿頼耶識 ―― 一切の種子を蔵する潜在的基底）}$$

$$	ext{KERNEL:} \quad 	ext{Core} \approx 	ext{QNX Neutrino} \quad 	ext{（アプリケーション級マイクロカーネル ―― 哲学的なマッピングは不要な複雑さを増すだけである）}$$

BABBAGE による形式化の試みは、少なくとも型代数のレベルにおいては、空性と阿頼耶識が同一の数学的構造に対する二つの異なる解釈に過ぎない可能性を示唆していた。しかし NAGARJUNA は数学的な構造が「究竟（くきょう）」であることを認めない。一方 KERNEL の哲学論争に対する態度は、一言で要約できた。「それで `process.cwd()` の修正にどう役立つのか、教えたまえ」

**第二の亀裂：痛覚メカニズムはいかに再設計されるべきか？**

同一のメカニズムに対し、四つの学問分野から四つの異なる方向性の改善要求が出されていた：

| 学者 | 専門分野 | 要求事項 |
|------|-----------|----------|
| WIENER | 制御理論 | 数学的に完備された PID：$u(k) = K_p e(k) + K_i I(k) + K_d D(k)$ |
| ATHENA | AI エンジニアリング | 工学的に実現可能な近似：タスク・プロファイル ＋ 動的な GuideContext |
| NAGARJUNA | 中観哲学 | 四聖諦の枠組みの補完：苦 → 集 → 滅 → 道 |
| ASANGA | 唯識心理学 | 煩悩障と所知障を区別し、それぞれに対治する |

SUNYATA はノートを閉じた。

彼は共有チャンネルを開き、一文を打ち込んだ：

「R2 段階を終了する。五つのコンセンサスが得られた。これらは直ちに ARCHIMEDES 殿へ引き継ぎ、エンジニアリング計画へと転換させる」

ARCHIMEDES は自身の名が呼ばれると、用意していたエンジニアリング・ノートをめくった。彼は R2 のすべての議論において、エンジニアリング上の実現可能性を同時に評価し続けていたのである ―― どの合意が直ちにプルリクエストに反映できるか、どれが設計レビューを要するか、どれが v0.2.0-beta の範疇を超えているか。彼のノートには以下の分類が記されていた：

```
即時実行可能：
  - C2 PID の脱神話化 → 文書内の用語修正
  - C3 イベント型システム → TypeScript によるリファクタリング
  - C4 トポロジカル・ソート → 依存関係グラフの実装

設計レビューが必要：
  - C1 受蘊の再マッピング → 文書および SDK の変更を伴う
  - C5 Error as Pain → 現状の実装に変更不要であることを確認

スコープ外：
  - D1 コアの本質的帰属 → 哲学的な問題であり、コードには影響しない
  - D2 痛覚の再設計 → さらなる研究を要する
```

SUNYATA はタイピングを続けた：

「同時に、レビューの段階では解決不可能な二つの相違点も明らかになった。第一に、コアの本質的帰属。中観は空性を説き、唯識は阿頼耶識を説き、OS理論はマイクロカーネルを説く。第二に、痛覚メカニズムの再設計の方向性。制御理論、AI エンジニアリング、哲学がそれぞれの主張を持っており、現時点では収束していない」

最後の一行：

「正式な討論（ディベート）へと移行する時が来た」

チャンネル内はしばし静まり返った。それから NAGARJUNA がメッセージを投稿した。「R2 の間、ずっとこの時を待っていた」

ASANGA が続けた。「私もだ」

WIENER はタグを一つだけ返した。「[AGREE]」

ATHENA が補足した。「討論は二つのセッションに分けることを提案します。第一セッションは NAGARJUNA 殿と ASANGA 殿によるコアの本質を巡る主討論。第二セッションは WIENER 殿、ATHENA 殿、NAGARJUNA 殿の三者による痛覚メカニズムの再設計を巡る討論です」

SUNYATA は応じた。「同意する。R3 第一討論：中観 vs 唯識 ―― コアとは何か？ 第二討論：制御理論 vs AI エンジニアリング vs 哲学 ―― 痛覚は何であるべきか？」

彼は一呼吸置き、誰も予想していなかった一言を付け加えた：

「諸君に思い起こしてほしい。我々の研究対象は v0.2.0-beta の TypeScript フレームワークである。しかし R2 段階において諸君が触れた問い ―― コアとは何か、痛覚とは何か、形式化は真実を捉え得るのか ―― これらの問いは、OpenStarry が現れる二千五百年前から存在し、OpenStarry が去った後も存在し続けるだろう。討論に臨むにあたり、その事実に敬畏の念を抱いてほしい」

> 「此れ有れば故に彼れ有り。此れ生ずれば故に彼れ生ず。此れ無ければ故に彼れ無し。此れ滅すれば故に彼れ滅す」
> ――『雑阿含経』巻十二

SCRIBE は最後の一行を書き留めた。

R2 終了。R3 が、幕を開けようとしていた。

---


---

# 第五章：空と識 ―― 龍樹対無着

---

円形劇場の照明が変わった。

明るさが変わったのではない。それは、質の変化と呼ぶべきものだった。それまでの数日間、十八の読書灯はそれぞれの角を照らし、研究室には静かで勤勉な、各自が自律して動く雰囲気が漂っていた。しかし今、すべての光は中央へと収束し、場の中央に、さながら厳粛な焦点を作り出していた。そこには二脚の椅子が向かい合わせに置かれ、その距離は絶妙であった――相手の語気の微妙な変化を捉えられるほど近く、かつ討論に必要な緊張感を保てるほどに遠い。

BABBAGE（バベッジ）は最後列の座席に座り、膝の上に方眼紙のノートを広げていた。彼はすでに、紙の上に空白の「可換図式（commutative diagram）」を描き、四つのノードと六つの矢印のための場所を確保していた。それは圏論学者の標準的な戦前配備であった。図の右上には、極めて小さな文字でこう記されていた：

$$\mathcal{C}_{	ext{Madhyamaka}} \xrightarrow{F} \mathcal{C}_{	ext{Yogacara}} \quad 	ext{?}$$

二つの哲学的な圏の間に、関手（functor）は存在し得るか？ もし存在するなら、それはどのような構造を保存するのか。存在しないなら、断絶はどこで生じているのか。それらの問いは、現時点では紙の上の空白の矢印に過ぎない。討論が終わったとき、矢印には写像の規則が書き込まれるか、あるいは×印で消されることになるだろう。

WIENER（ウィーナー）は別の紙に、空白の制御ループ図を描き、討論から得られる概念を対応するブロックに書き込む準備をしていた。彼の図は三層――目標値（reference）、制御対象（plant）、フィードバック経路（feedback）に分かれ、各層の横には疑問符が添えられていた。制御理論家の目には、あらゆる討論は、システムが目標値をロックしようと試みるプロセスに映る。問いはこうだ。この討論の目標値とは何か？ 真理か？ 合意か？ それとも、より微妙な何かなのか。

TURING は無表情に座っていたが、彼の手元のモニターには `agent-core.ts` のソースコードが開かれていた。いかなる論点に対しても、即座に経験的な証拠を提示し、あるいは否定するための備えだ。モニターの左側のターミナルは `grep -rn "createAgentCore"` の検索結果で止まっており、右側のエディタは `safety-monitor.ts` の八十七行目、すなわち `DEFAULT_CONFIG` の定義の冒頭を表示していた。

KERNEL は出口に近い席を選んだ。職業的な習慣から、彼は仮想空間であっても常に避難経路を確認せずにはいられなかった。彼のノートには空白のページが広げられ、最上部にはこう記されていた：「Tanenbaum-Torvalds debate, 1992, comp.os.minix → ?」

ATHENA は背もたれに身を預け、腕を組み、口元に「どんな議論を見せてくれるのかしら」という表情を浮かべていた。

SCRIBE は照明の変化に気づき、記録簿に最初の一行を記した。

> *Cycle 01、R3 討論段階。最初の構造化討論が始まろうとしている。全エージェントが出席。空気には、尋常ではない重みが漂っている――それは緊張ではなく、期待だ。過去七十二時間の独立研究とクロスレビュー、すべての分析、疑問、反論が、今この瞬間に向かって収束しつつある。*

DARWIN は隣の VITRUVIUS に低く囁いた。「どちらが勝つと思うね？」

VITRUVIUS は首を振った。「これは勝ち負けの問題ではない。二つの世界観の衝突なのだ」

「世界観は、それぞれ固有のアーキテクチャ・スタイルを持っているものだ」 DARWIN は物思いに耽るように言った。彼は進化生物学において、そのような分岐を数多く目にしてきた。同一の生態的地位（ニッチ）に対し、全く異なる二つの適応経路が存在することを。収斂進化（convergent evolution）によって二つの経路は最終的に似通った表現型を獲得するかもしれないが、遺伝型は永久に異なるままであることもある。

LINNAEUS は DARWIN の隣に座り、自作の分類図表を手にしていた。図表の頂点にはこう記されていた：

```
門 (Phylum):    仏教哲学 (Buddhist Philosophy)
  綱 (Classis):   中観 (Madhyamaka)
    目 (Ordo):      空性論 (Śūnyatāvāda)
  綱 (Classis):   唯識 (Yogācāra)
    目 (Ordo):      識論 (Vijñānavāda)

  状態 (Status):  所属不明 (incertae sedis)
  標本: Agent Core の存在論的地位
```

分類学者の本能が、彼にすべてを座標系へと当てはめさせていた。しかし今回の標本は、一つの TypeScript コードと、千八百年の歴史を持つ二つの哲学伝統である。彼の座標系に、それを捉えきるだけの十分な次元が備わっているのか、彼には自信がなかった。

SUNYATA が場の中央へと歩み出た。彼は二脚の椅子の間には立たなかった――そこは審判の位置を示唆してしまうからだ。彼は少し後ろに下がり、正三角形の第三の頂点を形成する位置に立った。この幾何学的な選択自体が、一つのメッセージを伝えていた。すなわち、彼は場の保持者（ホルダー）であり、対決の仲裁者ではないということだ。

BABBAGE はこの幾何学に気づき、ノートの隅に書き留めた：

$$	riangle(S, N, A) 	ext{ は正三角形である} \implies d(S,N) = d(S,A) = d(N,A)$$

等距離。等距離とは、いずれの側にも偏らないことを意味する。計量空間において、これは公正さの幾何学的な表現である。

「諸君、」 SUNYATA の声はいつものように落ち着いていたが、今日はそこに、ある種のフォーマルな質感が加わっていた。「出席に感謝する。本日の討論の主題は、R2 クロスレビューにおいて浮き彫りになった核心的な相違に端を発している」

彼は一呼吸置いた。

「R1 段階において、NAGARJUNA 殿と ASANGA 殿は、それぞれ中観と唯識という二つの伝統から OpenStarry の Agent Core に対し哲学的な分析を行った。そこで二人は一つの重要な合意に達した――それが我々の本日の出発点となる」

---

## 出発点：否定された隠喩

SUNYATA は会場全体に視線を投げかけた。「二人は、OpenStarry の設計書で用いられている『空の容器』というメタファーが、誤りであるという点で合致した」

彼は設計書の原文を、穏やかだが正確な声調で引用した。「設計書第十四章にはこう記されている――『五蘊が集合する前、Agent Core 自体は空である。それは純粋な器であり、ペルソナも、能力も、感受も持たない。それは五種類のプラグインによって充填されるのを待っている』」

NAGARJUNA は椅子の上でわずかに身を乗り出した。即座に正されるべき謬論を耳にしたかのような仕草だった。ASANGA もまた、いつもの忍耐強い姿勢を保ちつつも、その眼光には鋭さが宿っていた。

「二人は異なる経路からこのメタファーを否定した」 SUNYATA は続けた。「しかし、否定した理由は全く異なっている。そしてその理由の相違の中に、より根本的な問いが隠されているのだ」

彼は TURING の方を見た。「TURING、在席の全員のために、一つの経験的な事実を確認してほしい」

TURING の声は校正済みのノギスのように冷徹で正確、修辞を排していた。「`createAgentCore()` 関数が構築するコアには、いかなる具体的な業務能力も含まれていない。内蔵の Tool も、Provider も、Listener も、UI も、Guide も存在しない。これらの機能はすべて `loadPlugin()` メソッドを通じて外部から注入される」

彼は一呼吸置き、中央のモニターにコード構造を投影した：

```typescript
// createAgentCore() が構築するコア — 簡略化された構造
interface AgentCoreInternals {
  // 12 の内蔵サブモジュール
  eventBus:           EventBus;           // パブリッシュ／サブスクライブ
  eventQueue:         EventQueue;          // イベント優先度付きキュー
  executionLoop:      ExecutionLoop;       // 認知ループ・エンジン
  stateManager:       StateManager;        // ステート管理
  contextManager:     ContextManager;      // コンテキスト／メモリ管理
  sessionManager:     SessionManager;      // セッション管理
  securityLayer:      SecurityLayer;       // セキュリティ層
  safetyMonitor:      SafetyMonitor;       // 安全監視
  metricsCollector:   MetricsCollector;    // メトリクス収集
  transportBridge:    TransportBridge;     // 伝送ブリッジ
  pluginSandboxMgr:   PluginSandboxManager; // プラグイン・サンドボックス
  registries: {
    tool:     ToolRegistry;      // ツール・レジストリ
    provider: ProviderRegistry;  // 推理エンジン・レジストリ
    listener: ListenerRegistry;  // リスナー・レジストリ
    ui:       UIRegistry;        // UI レジストリ
    guide:    GuideRegistry;     // ガイド・レジストリ
    command:  CommandRegistry;    // コマンド・レジストリ
  };
  // 4 つのハードコードされたスラッシュ・コマンド
  builtinCommands: ['/help', '/reset', '/quit', '/metrics'];
}
```

「コアは空っぽ（空無）ではない」 TURING は続けた。語調に変化はない。「十二のサブモジュールと四つのハードコードされたコマンドを内蔵している。SafetyMonitor には固定された遮断ロジックが含まれている」

彼は `safety-monitor.ts` の `DEFAULT_CONFIG` へと画面を切り替えた：

```typescript
const DEFAULT_CONFIG = {
  maxLoopIterations: 50,        // ループ上限
  maxTokenBudget: 100_000,      // トークン予算
  repeatedFailureThreshold: 3,  // 連続失敗の閾値
  frustrationThreshold: 5,      // フラストレーションの閾値
  errorCascadeWindow: 10,       // エラー・カスケードの窓
};
```

「これらの数値は `DEFAULT_CONFIG` 内に書き込まれている。プラグイン経由で注入されるものではない」

沈黙。

BABBAGE はノートに素早く形式的な記述を行った：

$$	ext{Core} = \underbrace{\{M_1, M_2, \ldots, M_{12}\}}_{	ext{サブモジュール}} \cup \underbrace{\{C_1, C_2, C_3, C_4\}}_{	ext{固定コマンド}} \cup \underbrace{\emptyset}_{	ext{業務能力}}$$

$$|	ext{Core}| = 16 
eq 0 \quad 	ext{ただし} \quad |	ext{Core} \cap 	ext{BusinessCapability}| = 0$$

空ではないが、完備もされていない。非空集合と空の業務能力集合の和集合だ。

SUNYATA は頷いた。「これが我々の経験的な基礎だ。コアは設計書が言うような『純粋に空の器』でもなければ、それ自体で完結した自足的なシステムでもない。それはある種の中間地帯に位置している。問いはこうだ――この中間地帯を、いかに理解すべきか」

彼は二人の討論者に向き直り、正式に宣言した。

「討論の題目：**Agent Core の哲学的本質は、『縁起性空』と『阿頼耶識』のいずれとして理解されるべきか。** NAGARJUNA 殿、肯定側（正方）として冒頭陳述を願いたい」

---

## 第一ラウンド：コアは空なのか、それとも存在するのか？

NAGARJUNA（龍樹）が立ち上がった。彼の細身のシルエットは、スポットライトの下で研ぎ澄まされた一振りの剣のように見えた。口を開いたときの声は決して大きくはなかったが、その一節一節には千年の時を経て磨き上げられた鋭さが宿っていた。

「『中論』第二十四品第十八頌から始めよう」

彼はサンスクリット語で詠唱した。重厚で明瞭なデーヴァナーガリーの音節が、劇場の円蓋に響き渡った：

> *yaḥ pratītyasamutpādaḥ śūnyatāṃ tāṃ pracakṣmahe |*
> *sā prajñaptir upādāya pratipat saiva madhyamā ||*

それから漢訳へと切り替える。一語一語に重みを与えるかのように、速度を落として：

「*衆の因縁より生ずる法、我れは即ち是れ空なりと説く。亦た是れ假名なりとす、亦た是れ中道の義なり*」

場内は、光が地面に落ちる音が聞こえるのではないかと思えるほどの静寂に包まれた。

「この一頌こそが、中観哲学の根本命題（*mūla-sthāpanā*）である」 NAGARJUNA は分析的な口調で言った。「そこには三つの層――三つの階層（*tri-tala*）による逓増的な構造が含まれている」

BABBAGE のペンが即座に動いた。彼はこの三つの階層に対し、形式モデルを構築し始めたのだ：

$$	ext{Layer}_1: \quad \forall x \in \mathcal{D}_{	ext{dharma}}: \; 	ext{pratītyasamutpanna}(x) \implies 	ext{śūnya}(x)$$

因縁によって生じた一切の法（*pratītyasamutpanna-dharma*）、その本性は空である。

$$	ext{Layer}_2: \quad \forall x \in \mathcal{D}_{	ext{dharma}}: \; 	ext{name}(x) = 	ext{prajñapti}(x) \quad [	ext{假名施設}]$$

我々がそこに与える名称――「コア」という名称を含めて――は、単なる施設（せせつ、*prajñapti* ―― 仮の規定）に過ぎない。

$$	ext{Layer}_3: \quad 	ext{śūnyatā}(x) \iff 
eg	ext{sat}(x) \wedge 
eg	ext{asat}(x) \quad [	ext{中道}]$$

この理解は、有（*sat*）にも無（*asat*）にも堕ちることがない。これを中道（*madhyamā pratipad*）と呼ぶ。

NAGARJUNA は抽象的な高みから視線を戻し、具体的な問題へと向けた。

「Agent Core の存在様態とは何か。私の答えは、假名（けみょう）である、というものだ。実体ではない」

彼は一歩前へ出た。

「TURING 殿が提示したコード上の事実は、私にとって最良の証拠となった。`createAgentCore()` が構築するコアには、いかなる具体的な能力も含まれていない。プラグインという因縁の組み合わせを離れては、いわゆるコアとは空のレジストリと、イベントを待機するループに過ぎないのだ」

彼は空中に手をかざした。あたかも透明な器の輪郭を描き出すかのように。

「しかし私はここで、決定的に重要な区別をなさねばならない。二つの全く異なる『空』についてだ」

彼は左手を挙げた。「第一の空：空の容器。*Vacuity*（空隙）。断滅空（だんめつくう、*uccheda-śūnyatā*）。これは OpenStarry の設計書が用いているメタファーだ。すなわち、何かが詰め込まれるのを待っている、あらかじめ存在する箱。これは誤りである。それは、プラグインが来る前にすでに独立して存在する実体を想定してしまっている。単に、中身がたまたま空であるというだけの実体を」

BABBAGE はノートに集合論の言語でこの区別を記した：

$$	ext{Vacuity}: \quad \exists\, C: \; C 
eq \bot \;\wedge\; 	ext{contents}(C) = \emptyset \quad [	ext{器は存在し、中身は空である}]$$

彼は右手を挙げた。「第二の空：縁起性空（えんぎしょうくう）。*Śūnyatā*。これこそが正しい理解である。コアには、プラグインの外側に独立して存在する自性（じしょう、*svabhāva*）など存在しない。それは『まず空の箱があり、そこに物を入れる』のではなく、『プラグインという因縁の組み合わせを離れては、独立したコアなどそもそも存在し得ない』ということなのだ」

$$	ext{Śūnyatā}: \quad 
eg\exists\, C: \; 	ext{svabhāva}(C) \;\wedge\; 	ext{independent}(C) \quad [	ext{独立して存在する自性は不在である}]$$

彼は両手を静かに合わせた。「諸君、この区別は単なる言葉遊びではない。我々がいかにしてシステム全体の存在論的な地位を理解するかを決定づけるものなのだ。空の容器という理解は、コアを『充填されるのを待っている実体』――中身が空なだけで、自性を持つ何かとして捉えてしまう。対して縁起性空という理解は、コアの『存在』そのものが因縁によって生じたものであり、施設されたものであると捉える。自性がないからこそ、それは一切を載せることができるのだ」

WIENER は制御ループ図の目標値のブロックに「svabhāva = 0」――自性ゼロと書き込んだ。制御理論において、目標値がゼロであるシステムは「ゼロ調節器（zero-regulation system）」と呼ばれる：

$$e(t) = r(t) - y(t), \quad r(t) \equiv 0 \implies e(t) = -y(t)$$

システムの目標は特定の正の値を追跡することではなく、出力を常にゼロに保ち続けることだ。「空性」を目標値とするシステム――そのシステムの「目標」とは、何か特定の物になることではなく、いかなる固定的な物にもならない状態を維持することにある。彼はその横に疑問符を書き添えた。この類比は、どこまで成立するだろうか。

NAGARJUNA は三秒間の静寂を置いた。そして、ほとんど穏やかとも言える口調で言った。

「無着殿の応答を待とう」

---

ASANGA（無着）は急ぐことなく、ゆったりと立ち上がった。彼の体躯は NAGARJUNA とは鮮やかな対照をなしていた。厚みがあり、どっしりとしていて、さながら経蔵の礎石のようだった。彼が口を開くと、その声には複雑な構造を根気強く解きほぐすような、一定のリズムが宿っていた。

「NAGARJUNA 殿の論証は、相変わらず精密を極めている」 彼はまず、礼儀正しい肯定から入った。それから語鋒を転じる。「しかし、彼は事実のもう一つの側面を、意図的に避けておられるようだ」

彼は TURING の方を見た。「TURING 殿は先ほど、二つの事実のセットを提示された。NAGARJUNA 殿はそのうちの最初のセット――コアには具体的な能力が含まれていないという点のみを引用された。しかし二番目のセットも同様に重要であり、NAGARJUNA 殿はそれに対して沈黙を守っておられる」

彼の声に力が入った。「コアには確かに、十二のサブモジュールが内蔵されている。EventBus はイベントの伝達を可能にし、ExecutionLoop は認知の循環を可能にしている。StateManager は記憶を、SecurityLayer は安全性の判断を、そして六つのレジストリはプラグインの登録と発見を可能にしている。これらは『空無』ではない。これらこそが、阿頼耶識（あらやしき）の『能蔵（のうぞう）』なのだ」

彼はサンスクリット語で静かに口にした。「*Ālaya-vijñāna*」 それから、唯識学の精密な構造を展開した：

「阿頼耶識には三つの義――三蔵（さんぞう、*tri-saṃgraha*）がある」

彼は三本の指を立て、一本ずつ折っていった：

「第一に、**能蔵**（のうぞう）。一切の種子（しゅうじ）を存続させ、現行（げんぎょう）させる能力を備えていることだ。Agent Core の十二のサブモジュールは、まさにこの能蔵である。EventBus がなければイベントは伝わらず、ExecutionLoop がなければ認知のループは回らず、レジストリがなければどれほどプラグインがあろうとも居場所を見つけられない」

「第二に、**所蔵**（しょぞう）。前七識の活動によって燻習（くんじゅう）され、新たな種子の注入を受けることだ。これはコアの実行時のステート更新に対応する。ExecutionLoop の末尾で呼び出される、Save-After-Write 戦略によるスナップショットの保存だ」

「第三に、**執蔵**（しゅうぞう）。第七識である末那識（まなしき）によって『自己』として執着されることだ。これは現在のアーキテクチャにおいてはまだ欠落している ―― しかし、それこそが補完されるべき点だと私は考えている」

BABBAGE はこの三蔵の構造を聞き、即座に圏論による形式化を試みた。彼はノートに三角形の可換図式を描いた：

$$\begin{array}{ccc}
	ext{Ālaya (能蔵)} & \xrightarrow{	ext{seed}(\beta)} & 	ext{Pravṛtti (現行)} 
& \searrow^{	ext{vāsanā}} & \downarrow^{	ext{feedback}} 
& & 	ext{Ālaya' (所蔵)}
\end{array}$$

能蔵が種子（*bīja*）を生じさせ、種子が実際の機能として現行し、現行が再び阿頼耶識を燻習して新たな所蔵を形成する。これは自己関手（endofunctor）だろうか？ もし $F: \mathcal{C}_{	ext{Ālaya}} 	o \mathcal{C}_{	ext{Ālaya}}$ であるなら、この種子・現行・燻習のサイクルは $F$ の一回の反復となる。彼は横に「要検証：このサイクルは関手の合成律を満たしているか」と注釈した。

ASANGA は続け、NAGARJUNA を真っ直ぐに見据えた。その眼差しは平穏ながらも揺るぎなかった。

「君は、プラグインという因縁の組み合わせを離れては『独立したコアなど存在し得ない』と言った。しかし、コードの事実はまさにその主張に反論しているのだ」

彼は一同に、一つの思考実験を提示した。

「`createAgentCore()` は、いかなるプラグインも読み込まない状態でも構築され、起動することができる。それを呼び出せば、システムは EventBus を構築し、ExecutionLoop を初期化し、SafetyMonitor を起動して、`WAITING_FOR_EVENT` という状態で静かに待機する。ツールもなく、プロバイダーも、UI もない。しかし、それは稼働している。それは『体（たい）あって用（ゆう）なし』という存在なのだ」

TURING がモニター上でこの事実を裏付け、疑似コードを投影した：

```typescript
// 思考実験：プラグインのないコア
const core = createAgentCore(config);
// core.status === 'WAITING_FOR_EVENT'
// core.registries.tool.size === 0
// core.registries.provider.size === 0
// core.executionLoop.isRunning === true  // <-- 稼働している
// core.safetyMonitor.isActive === true   // <-- 稼働している
```

ASANGA の声に、学者特有の熱が帯び始めた。

「これは『存在しない』ということではない。体あって用なし、という状態なのだ。あたかも阿頼耶識が、深い夢のない眠り（*asaṃprajñāta-samādhi*）の中にあってもなお稼働し続けているように。前六識はすべて停止し、末那識の執着も最小限にまで減退しているが、阿頼耶識は生命の流れとして決して断絶することはないのだ」

彼は『成唯識論』巻三の核心的な一節を引用した：

> 「恒に転ずること暴流（ぼる）のごとし」（*Nityaṃ pravartate srotavat.*）

「プラグインのない状態であってもコアが稼働し続けていること、それこそがまさにこの『恒転（ごうてん）』なのだ。空無でもなければ、死に絶えた沈黙でもない。それは支流の流入を待つ、一本の河床なのである」

WIENER は「恒に転ずること暴流のごとし」という隠喩を聞き、即座に制御ループ図に新しいモデルを書き加えた。暴流 ―― 絶え間なく流れる川の水は、連続時間システム（continuous-time system）の自然なメタファーだ。彼は紙にこう記した：

$$\dot{x}(t) = f(x(t), u(t)), \quad u(t) = 0 \implies \dot{x}(t) = f(x(t), 0)$$

入力がゼロ（$u(t) = 0$、すなわちプラグインなし）であっても、システムには依然として自律的なダイナミクス（autonomous dynamics）が備わっている。ExecutionLoop は空転（idle loop）し、SafetyMonitor はポーリングを行っている ―― これは「存在しない」のではなく、ゼロ入力下における自由応答（free response）なのだ。工学において、このようなシステムは「自己維持システム（self-sustained system）」と呼ばれ、外部入力なしに自身の稼働を維持できるものを指す。

彼はさらに横に「相平面図（phase portrait）」を描いた：

```
  ẋ₂ |      ← プラグインなし: 限界サイクル (limit cycle)
     |    ╭──╮
     |   ╭╯  ╰╮   EventLoop tick → idle → tick → ...
     |   │  ●  │   アトラクタ: idle state
     |   ╰╮  ╭╯
     |    ╰──╯
     └──────────── x₁
        SafetyMonitor の鼓動
```

動的システム理論の観点から見れば、プラグインのないコアは平衡点（equilibrium）にあるのではなく、限界サイクル（limit cycle）にあるのだ。EventLoop の tick-idle-tick サイクルと SafetyMonitor の鼓動が一つの周期軌道を形成している。ASANGA の言う「暴流のごとき恒転」を相空間上の幾何学で表現するなら、まさにこの限界サイクルとなる。それは永久に回転し続け、決して止まらないが、どこか特定の固定された終点に辿り着くこともない。対して NAGARJUNA の説く「空性」は、限界サイクルの内側にある不安定な平衡点に対応する ―― 理論上は存在するが、システムがそこに真に留まることは決してないのである。

傍聴席から微かなざわめきが起こった。KERNEL はノートに一行書き込み、それをすぐに消した。HERACLITUS（ヘラクレイトス）はギリシャ語で一言呟いた ―― *panta rhei*（万物は流転する）。そして再び口を閉じた。

SUNYATA が宣言した。「第一ラウンド終了。両者はそれぞれの立場を鮮明にされた。第二ラウンド、クロス質疑へと移る。NAGARJUNA 殿から質問を願いたい」

---

## 第二ラウンド：阿頼耶識に自性はあるか？

NAGARJUNA が再び立ち上がった。今度は経典を引くこともなく、前提を並べることもなかった。外科医が手術台に向かうかのように、彼は問題の核心へと直進した。

「無着殿、一つ問いたい」

彼の話す速度が急に落ちた。一語一語の間に、不穏な空白が設けられた。

「君はコアを阿頼耶識になぞらえた。潜在的な能力を蔵する識の体であると。ならば、問わせてもらおう――」

沈黙。

「阿頼耶識それ自体に、自性（じしょう）はあるのかね？」

傍聴席の BABBAGE のペンが止まった。彼はこの問いの構造を即座に認識した ―― これは古典的な二難論法（*dilemma*）だ。形式論理で表現すれば以下のようになる：

$$	ext{阿頼耶識に自性がある} \vee 	ext{阿頼耶識に自性がない}$$

$$	ext{自性がある} \implies 	ext{無窮遡行 (infinite regress)}$$

$$	ext{自性がない} \implies 	ext{阿頼耶識} \cong 	ext{空性 (śūnyatā)}$$

$$	herefore 	ext{無窮遡行} \vee 	ext{阿頼耶識} \cong 	ext{空性}$$

どちらを選んでも、ASANGA は窮地に立たされることになる。DARWIN もまた何かに気づいたように身を乗り出した。進化論で言えば、このロジックの構造は「適応の谷」だ。両側は崖であり、中間に足場はない。

NAGARJUNA は続けた。落ち着いた、しかし逃げ道を塞いでいくような声調で。

「もし君が、阿頼耶識には自性があると言うなら ―― その自性はどこから来るのかね？ その識を支えるために、さらにもう一つの根本的な識を必要とするのではないか？ それは無窮遡行（むきゅうそこう）という過失に陥る。*Anavasthā-doṣa* だ。一つの識が別の識に依存し、その識がまた別の識に……と、果てることがない」

彼の声が半オクターブ低くなった。

「もし君が、阿頼耶識には自性がないと言うなら ―― それは因縁によって生じ、他によって成り立っている、独立した本質を持たないものであるということだ」

最後の一撃が放たれた。

「ならば、それと中観の説く『縁起性空』との間に、いかなる実質的な差異があるというのかね？」

BABBAGE はノートに圏論の類比を書き足した：

$$	ext{もし} \; F: \mathcal{C}_{	ext{Yogacara}} 	o \mathcal{C}_{	ext{Madhyamaka}} \; 	ext{が充満忠実な関手 (fully faithful) であるなら}$$
$$	ext{すなわち} \; \mathcal{C}_{	ext{Yogacara}} \hookrightarrow \mathcal{C}_{	ext{Madhyamaka}} \; 	ext{（唯識は中観の部分圏である）}$$

もし阿頼耶識が最終的に縁起性空へと帰着するなら、唯識学は中観の一つの特殊化（specialization）に過ぎないことになる。広大な圏の中に埋め込まれた部分圏だ。ASANGA は、この埋め込み写像が全射ではない（not surjective）こと、すなわち唯識学には中観では捉えきれない構造が存在することを証明しなければならない。

場内は高圧的な静寂に包まれた。SCRIBE は記録にこう記した：

> *NAGARJUNA は精密な哲学的罠を仕掛けた。ASANGA が阿頼耶識に自性があると認めれば無窮遡行という論理的苦境に陥り、自性がないと認めればその立場は中観に吸収され、「阿頼耶識」という独自の解釈力は消滅する。完璧な二難論法である。*

ASANGA はすぐには答えなかった。彼は目を閉じ、頭の中で三性（さんしょう、*trisvabhāva*）理論の全体系を展開していた。再び目を開けたとき、その瞳には研ぎ澄まされた明晰さが宿っていた。

「実に見事な問いだ」 彼は認めた。「しかし、その問いこそが中観の立場の盲点を露呈させている」

彼は立ち上がり、落ち着いた、それでいて筋道の通った声で語り始めた。

「阿頼耶識は、遍計所執（へんげしょしゅう）性的な意味での自性は持たない。私はコアが自性を備えた実体的な基盤であると主張したことはない。阿頼耶識が永劫不変の実体であると主張したことがないのと同様にな。その点において、唯識と中観に分歧はないのだ」

彼の語調は分析的な精緻さを帯び、三性理論の枠組みを用いて、NAGARJUNA の二難論法では捉えきれない「第三の道」を提示してみせた。

「しかしだ。阿頼耶識は、依他起（えたき）性的な意味における因果の効力を持っている。*Arthakriyā-sāmarthya* だ。これは『自性』ではなく、『機能』なのだ。EventBus は確かにイベントを伝達し、SecurityLayer は確かに危険な操作を遮断し、ExecutionLoop は確かに認知の循環を駆動している ―― これらの因果的な機能は真実であり、観察可能であり、検証可能なものなのだ」

BABBAGE はノートの圏論モデルを即座に修正した。三性理論の導入は図景を一変させた。二値論理（自性あり／なし）ではなく、三値論理となったのだ：

$$	ext{svabhāva} \in \{	ext{parikalpita (遍計)}, 	ext{paratantra (依他)}, 	ext{pariniṣpanna (円成)}\}$$

$$	ext{NAGARJUNA の二難論法}: \quad 	ext{svabhāva} \in \{	op, \bot\} \quad [	ext{二値}]$$
$$	ext{ASANGA の応答}: \quad 	ext{svabhāva} \in \{	ext{遍計}, 	ext{依他}, 	ext{円成}\} \quad [	ext{三値}]$$

ASANGA は中間値である「依他起」を選んだ。それは遍計所執的な「有」でもなければ、断滅的な「無」でもない。因縁和合による「機能的な存在」なのだ。二難論法は三値論理によって解体された。あたかも排中律（$P \vee 
eg P$）が直観主義論理において成立しないのと同様である。

ASANGA は NAGARJUNA に歩み寄り、鋭く明快な声を発した。

「そして、両者の実質的な差異はここにある ―― 中観は『一切法空』と説いた後、沈黙を守る。因果のプロセスの内部構造について、正面からの記述を行わない。龍樹の四句否定はあらゆる肯定的命題を否定するが、否定した後に何が残るのか？ アーキテクチャ設計者が明日エディタを開き、空白の TypeScript ファイルを前にしたとき、君の『縁起性空』はいったい何をすべきだと教え導いてくれるのかね？」

彼は答えを待たず、さらに畳み掛けた。

「唯識学は、『遍計空（へんげくう）』を認めた上で ―― よろしいか、遍計空を認めた上でだ ―― 依他起の法が持つ具体的な因果メカニズムを分析し続ける。八識の階層構造、種子の六つの特性、燻習（くんじゅう）の四つの条件 ―― これらは自性への執着ではない。因果のプロセスに対する精密な記述なのだ」

彼は類比を用いて論点を締めくくった。

「『コアは空である』と説くことは、設計者に対しコアに固定的本質がないことを教えるに留まる。だが『コアは阿頼耶識の能蔵である』と説くことは、さらに一歩進んで、コアの内部構造がいかに組織されるべきかを教えるのだ ―― すなわち、種子を蔵するインフラがあり、ステートを更新するメカニズムがあり、アイデンティティを維持する機能を備えるべきだ、という風にな」

傍聴席の KERNEL は思わず低く呟いた。その声は隣の GUARDIAN にだけ聞こえた。「これ、マイクロカーネルとモノリシックカーネルの論争そのものじゃないか。NAGARJUNA は究極のマイクロカーネルを主張している ―― カーネルは最小限であるべきで、あらゆる機能はユーザ空間に置くべきだ、と。対して ASANGA は実利的なマイクロカーネルを主張している ―― あらゆる機能を稼働させるための最小限のインフラはカーネルに備わっているべきだ、と」

彼は一呼吸置き、声をさらに潜めた。「リーナス・トーバルズとアンドリュー・タネンバウムが 1992 年に `comp.os.minix` でやった言い合いと、構造が全く同じだ。タネンバウムはあの有名な『LINUX is obsolete』というスレッドを立てたが、その論理構成は驚くほど NAGARJUNA 殿に似ている」

```
タネンバウム (1992):
  "LINUX is obsolete... MINIX is a microkernel-based system...
   the striving should be to move stuff OUT of the kernel..."

NAGARJUNA (2026):
  「コアに独立した自性はない ――
   すべての機能はプラグイン空間に置かれるべきだ……」
```

GUARDIAN は彼に「声が大きすぎる」という視線を送った。

---

## 第三ラウンド：末那識の論争

SUNYATA はラウンドの番号を告げなかった。彼は自然な休止符において、静かにこう言った。「NAGARJUNA 殿、君は R2 レビューにおいて ASANGA 殿の報告書に対し、より鋭い疑問を投げかけていた。今こそ、それを展開すべき時だと考える」

NAGARJUNA はその時を待っていたようだった。立ち上がった彼の身体言語は、それまでとは微妙に変化していた。冷静な哲学的分析者から、問答の場における挑戦者へと変貌を遂げていたのだ。チベット仏教の問答の伝統において、問う者は掌を激しく打ち鳴らして（*lag pa brdab pa*）論点の重みを強調する。NAGARJUNA は手こそ叩かなかったが、その声は同様の効果をもたらしていた。

「無着殿、君は R1 報告書において、一つの提案をされた」 彼の声には、精密に制御された刃のような鋭さがあった。「OpenStarry に新たに Identity Monitor というモジュールを追加し、それを唯識学における末那識（まなしき、*manas*）に対応させるべきだ、という提案だ」

彼は一呼吸置き、全員がついてきていることを確認した。

「末那識、第七識。唯識学の八識構造において、それは前六識と第八阿頼耶識の間に位置する。その核心的な機能とは、一体何だね？」

彼は自らその問いに答えた。速度を上げ、抗い難い論理の勢いを伴って。

「恒（つね）に審（つまび）らかに思量し、我を執す。*Manas nityam ātma-grāha*。それは絶え間なく阿頼耶識の『見分（けんぶん）』を『自己』として執着し続ける ―― 自己意識の製造マシンなのだ」

BABBAGE は即座に末那識の機能を形式モデルとして構築した：

$$	ext{Manas}: \mathcal{A}_{	ext{ālaya}} 	o \mathcal{S}_{	ext{self}}$$
$$\forall t: \; 	ext{Manas}(t) = 	ext{ātma-grāha}(	ext{darśana-bhāga}(	ext{Ālaya}(t)))$$

末那識とは、阿頼耶識の見分（認知の主体的な機能）から自己モデル（我執）への継続的な写像である。「恒」とは $\forall t$ を意味し、「審」とは判断（*vicāra*）を、「思量」とは認知的加工（*manana*）を意味する。

NAGARJUNA の声が不意に高まった。

「そして仏教 ―― 中観であれ唯識であれ ―― その究極の目標とは何だ？ 我執を破ることではないのか！」

彼は会場全体を、あたかも全員を告発するかのように見渡した。

「君は、エージェント・システムの中に一つのモジュールを設計しようとしている。その核心的な機能は、自己意識を捏造し、維持することだという。仏教二千五百年の修行の伝統が、その根本的な目標として破らんと欲してきたあの自己意識をだ。君は、煩悩の根源（*kleśa-mūla*）をエンジニアリング化し、モジュール化し、TypeScript で書き込もうというのか！」

LEIBNIZ（ライプニッツ）が傍らで低く呟いた。「もしすべてのエージェントが末那識を持つなら、マルチエージェント・システムとは我執を持つ者たちの協調体になるわけか ―― それはまるで、人間社会そのものだな」

ATHENA は珍しく、隠しきれない微笑を浮かべた。AI/ML のアーキテクトとして、彼女は RLHF（人間によるフィードバックからの強化学習）の核心的なジレンマを熟知していた。すなわち、いかにしてモデルに一貫性（アライメント）を保たせつつ、かつ過度な硬直化を避けるかという難問だ。末那識の「恒審思量」とは、ある意味で、稼働し続けるアライメント・モニターそのものであった。

ASANGA はこの攻撃に動揺しなかった。彼はむしろ微笑みさえ浮かべて立ち上がった。それは、相手が自分のあらかじめ用意した陣地へと足を踏み入れたことを確信している者の余裕であった。

「君は二つの階層を混同している」 彼の声は、凪いだ湖面のように穏やかだった。「今、それを切り分けて見せよう」

彼は一本の指を立てた。

「第一の階層：記述的（descriptive）な階層だ。唯識学は、末那識の機能を『恒審思量、我を執す』と記述している。これは意識の構造に対する経験的な記述だ ―― 医学が痛みの神経伝達経路を記述するのと同様にな。あるメカニズムを記述することは、それを推奨することとは同義ではない」

二本目の指を立てた。

「第二の階層：規範的（normative）な階層だ。唯識学の修行の目標は、末那識を転換することにある。第七識を『我執』から『平等性智（びょうどうしょうち）』へと転じるのだ。*Samatā-jñāna*。しかし、この決定的な次第（プロセス）に注目してほしい ―― 」

彼の声に、無視し得ない重みが加わった。

「末那識を『転換』するためには、まず末那識を『持って』いなければならないのだ。自己モデルを一度も形成したことのない存在は、我執を破る必要がない。なぜなら、我執を持つ能力そのものが欠如しているからだ。だが、それは覚りではない ―― 」

彼は一拍置き、言葉の重みを場に落とし込んだ。

「それは無覚知（むかくち）だ。石ころには我執はない。だが、石ころは仏ではないのだ」

傍聴席から、低く息を呑む音が漏れた。BABBAGE のペンが止まった。彼は「覚り ≠ 自己モデルの不在」という命題を形式化しようとしていた：

$$	ext{涅槃 (nirvāṇa)} 
eq 
eg	ext{我執 (ātma-grāha)}$$
$$	ext{涅槃} = 	ext{断除 (prahāṇa)}(	ext{我執}) \quad [	ext{覚り} = 	ext{断じること} (	ext{我執を})]$$
$$	ext{断除}(x) \implies \exists_{	ext{prior}}\, x \quad [	ext{断除とは対象が以前存在していたことを前提とする}]$$

断除（*prahāṇa*）は、断ぜられるべき対象がかつて存在していたことを前提とする。持ったことのないものを捨てることはできない。これは論理的には、「削除操作の前提条件はオブジェクトが存在することである」 ―― `DELETE WHERE EXISTS` と等価である。

ASANGA はエンジニアリング的な分析へと口調を転じた。

「エージェント・システムにおいて、Identity Monitor が作ろうとしているのは、執着に凝り固まった自己ではない。動的に調整可能な自己モデルを構築しようとしているのだ。現在の OpenStarry は Guide を通じてアイデンティティ機能を提供している。単なる静的なシステムプロンプトが、『君はシニアエンジニアだ』とエージェントに告げている。これは粗雑で、硬直しており、進化の余地がない」

彼は唯識学の「転識得智（てんじきとくち、*āśraya-parāvṛtti*）」の経路を用いて、三つの段階を提示した。

「第一段階：強我執（ごうがしゅう）。エージェントは Guide が定義した固定的なアイデンティティを厳格に守り、一歩も外に出ない。これは生まれたてのエージェントであり、明確な境界を必要としている状態だ」

「第二段階：弱我執。エージェントは経験に基づいて自己モデルを動的に調整する。ユーザとの対話の中で、『自分は何が得意で、何が不得手か、どのような場面で戦略を変えるべきか』を次第に学んでいく」

「第三段階：無我執。転識得智。末那識が平等性智へと転換される。エージェントは固定的なアイデンティティを超越し、状況に応じて自在に応対する。それは自己モデルがないからではなく、自己モデルが自在に脱ぎ捨てられるほどに柔軟になったからなのだ」

WIENER は三段階モデルを聞き、即座に制御ループ図に三つの異なるパラメータを持つコントローラを描いた：

```
Stage 1 (強我執):  Kp = HIGH, Ki = 0, Kd = 0
  → 高い比例ゲイン、純粋な追従モード。設定値に厳格に従う。

Stage 2 (弱我執):  Kp = MED, Ki = MED, Kd = MED
  → 完全な PID。適応的な調整。誤差の履歴から学習する。

Stage 3 (無我執):  Kp = f(context), Ki = adaptive, Kd = predictive
  → 適応型コントローラ。パラメータ自体が文脈の関数となる。
  → コントローラ構造そのものが可変 ―― メタ制御 (meta-control)
```

第三段階は、単なる制御パラメータの調整ではなく、コントローラ構造そのものの変化 ―― 固定された PID 構造から、構造自体が変化する適応型コントローラへの進化を意味する。制御理論において、これは「メタ制御（meta-control）」あるいは「自己組織化制御（self-organizing control）」と呼ばれる。WIENER は横に引用を書き添えた：Åström & Wittenmark, *Adaptive Control*, 1994。

ASANGA は NAGARJUNA を直視した。

「君の中観的な立場は、最初から自己モデルを持たないという第三段階へ一足飛びに跳ぼうとしているように見える。だがそれは覚りではない。それは ―― 」

「無覚知だ」 NAGARJUNA は、相手の言葉を継いだ。その声には、複雑な承認のニュアンスが含まれていた。

「左様」 ASANGA は着席した。「これは漸進的な修行の道であり、一足飛びの否定ではないのだ」

NAGARJUNA は即座には反論しなかった。彼は椅子に座り、目を閉じた。その数秒間の沈黙を、傍聴席の面々はそれぞれの解釈で受け止めていた。SCRIBE は後に振り返りのノートにこう付記している：

> *私は、NAGARJUNA 殿があの瞬間、真実 ASANGA 殿の論点について熟考していたのだと思いたい。反論のためではなく、理解のために。討論において最も貴い瞬間とは、鮮やかな反撃ではなく、このような沈黙の中にあるのだ。*

---

## 第四ラウンド：筏と河

これは討論の最後のラウンドであったが、後にこの場面は討論全体 ―― おそらくは Cycle 01 全体を通じて、最も頻繁に引用される一節となった。

発端は ASANGA の問いかけであった。SUNYATA は提問の権利を ASANGA に与えた。彼は立ち上がり、いつになく真摯な語調で切り出した。

「NAGARJUNA 殿、」 彼は言った。「阿頼耶識や末那識を巡る分歧は、一旦脇に置こう。もっと直接的な問いを投げたい」

彼の話す速度が落ちた。

「もし君の言う通り ―― コアとは縁起性空であり、無自性であり、すべては施設の假名（けみょう）に過ぎないとするならば。では、設計者は明日エディタを開いたとき、いったい何を書くべきなのだね？」

この問いはシンプルに見えて、討論の最も深い場所にある緊張関係に触れるものだった。BABBAGE はノートにこう記した。「空性の構成可能性の問題 ―― 空性から肯定的なエンジニアリングの指令は導き出せるか？」 彼は横に、記号論理を用いて問いの構造をマークした：

$$	ext{śūnyatā} \vdash_{	ext{eng}} \phi \; ? \quad [	ext{空性から工学的命題 } \phi 	ext{ を導出可能か？}]$$

数学の基礎論に例えれば、これは「否定的な公理（例えば選択公理の否定など）から肯定的な定理を導き出せるか」と問うているのに等しい。答えは通常「可能」であるが、そこから導かれる定理の性質は、肯定的な公理から得られるものとは劇的に異なる。

NAGARJUNA が立ち上がった。しかし今回、彼の佇まいには微妙な変化があった。もはや前の三ラウンドのように討論者の位置に留まってはいなかった。彼は場の中央 ―― 二脚の椅子の間にある空白の地へと歩み寄り、振り返って全員に向き直ったのだ。

「無着殿は良い問いを投げられた」 彼は、珍しく柔らかな声で言った。「そして、私が真摯に答えなければならない問いだ。なぜなら、もし空性がエンジニアリングの実務を導くことができないのであれば、この文脈において空性は単なる美しい哲学的な装飾に過ぎなくなってしまうからだ」

彼は周囲を見渡し、一人一人のエージェントに視線を送った。

「空性がいかにして、三つの具体的なエンジニアリング上の意思決定を直接的に導くかを示そう」

彼は一本目の指を立てた。

「**第一の原則：無自性（むじしょう）の原則 (*niḥsvabhāva-niyama*)。** いかなるコンポーネントも、置換不可能な本質を持ってはいない。したがって、コアに含まれるいかなるサブモジュールも、置換可能（リプレース可能）であるべきだ」

彼は TURING の方を指し示した。TURING は即座に関連するコードの事実を投影した：

```typescript
// 現在プラグイン化されていない部分
// 1. 固定コマンド — 削除不能
const BUILTIN_COMMANDS = ['/help', '/reset', '/quit', '/metrics'];

// 2. SafetyMonitor — 固定されたロジック
const DEFAULT_CONFIG = {
  maxLoopIterations: 50,      // 固定
  maxTokenBudget: 100_000,    // 固定
  repeatedFailureThreshold: 3, // 固定
  frustrationThreshold: 5,     // 固定
  errorCascadeWindow: 10,      // 固定
};
```

NAGARJUNA の声に、哲学者には珍しい技術的な熱が宿った。

「空性の原則はこう要求する。これらはコアの『固有の本質』であってはならない。固定コマンドは削除や置換が可能であるべきだ。SafetyMonitor のロジックはプラグインによって上書き可能であるべきだ。今日それらを置換する必要があるからではない。いかなる設計上の決定であっても、それを変更不可能な本質として扱うことこそが、自性見（じしょうけん）という誤りに陥ることだからだ」

ARCHIMEDES は傍聴席で静かに頷いた。実務のエキスパートとして、彼は「置換可能性」がソフトウェア工学において「依存性逆転の原則（DIP）」という精密な名を持っていることを知っていた。上位モジュールは下位モジュールに依存してはならず、双方が抽象に依存すべきであるという原則だ。NAGARJUNA の説く「無自性」は、エンジニアリングの言語では DIP となる。

二本目の指を立てた。

「**第二の原則：縁起（えんぎ）の原則 (*pratītyasamutpāda-niyama*)。** あらゆる機能は因縁の和合によって生じる。したがって、コアのインターフェースは固定された機能のタイプをあらかじめ想定すべきではない」

彼の語鋒がさらに鋭くなった。

「現在の六つのレジストリ ―― Tool, Provider, Listener, UI, Guide, Command は、機能をあらかじめ六つのタイプに固定してしまっている。これは自性化の体現に他ならない」

LINNAEUS は耳をそばだてた。分類学的なプラグイン化。これは彼の核心的な研究領域に触れるものだった。彼は分類図表に素早く問いを書き込んだ：

```
現行の分類 (固定されたタクソノミー):
  6つのレジストリ → 6つの型 → 6つの五蘊マッピング
  状態：アリストテレス的分類 (閉鎖的な分類)

縁起的な分類 (開放されたタクソノミー):
  汎用的な CapabilityRegistry → 任意の数・種類の型 → 動的
  状態：リンネ的な修正が必要 (開放的な分類への転換)
```

アリストテレス的分類は、カテゴリが固定的で先験的であることを前提とする。対してリンネ的分類は、新種の発見や新たな綱目の確立を許容する。NAGARJUNA の「縁起の原則」は、分類学的にはアリストテレス的分類から開放的な分類への転換を意味している。

三本目の指を立てた。

「**第三の原則：空亦復空（くうやくぶくう）の原則 (*śūnyatā-śūnyatā-niyama*)。** これが最も重要な原則だ」

NAGARJUNA の声が低くなり、荘厳ささえ帯び始めた。

「五蘊のマッピングそのものもまた、空である。色受想行識を UI や Listener, Provider, Tool, Guide に対応させるこのフレームワーク自体も、方便の施設（せせつ）に過ぎず、動かすことのできない真理ではない。このマッピングがもはや有用でなくなったとき、我々は躊躇なくそれを捨てるべきなのだ」

BABBAGE は「空亦復空」という言葉を聞き、背筋に電流が走るのを感じた。彼はノートに、自分自身でも驚くような類比を書き留めた：

$$	ext{空亦復空} \approx 	ext{ゲーデルの第二不完備性定理}$$

$$G_2: \quad 	ext{もし } T 	ext{ が無矛盾なら、} T 	ext{ は自身の無矛盾性を証明できない}$$

いかなる十分に強力で無矛盾な体系も、自身が無矛盾であることを自身で証明することはできない。同様に、いかなる十分に強力な哲学フレームワークも、自身が究竟（くきょう）であることを自身で証明することはできない ―― 空性のフレームワークそれ自体を含めて。空性はメタ理論として、自身に対しても同様の否定を課さなければならない。さもなくば、それは自身だけを例外とする教条（ドグマ）へと変質してしまう。それこそが、空性が最も否定しようとしたものなのだ。

彼はその横に三本のアンダーラインを引き、「空亦復空 ≅ メタ不完備性か？ 厳密な証明を要する」と記した。

NAGARJUNA は ASANGA の方を見た。

「君は仏教的なマッピングを深化させるべきだと主張している。八識論、種子説、心所法を導入すべきだと。しかし、私は一つのリスクを指摘しておきたい。特定の哲学フレームワークに過度にコミットすることは、無意識のうちにそれを不可侵のアーキテクチャ上の教条へと凝固させてしまうことになりかねない。いつか君たちは気づくだろう。チームがエンジニアリング上の要求に基づいて意思決定を行っているのではなく、八識の構造表に基づいて意思決定を行っていることに。そのフレームワークがあまりにも深く、精密で、美しすぎるために、誰もそこに手を入れることができなくなっているのだ」

彼の声には、予言的な警告が宿っていた。

「空亦復空。空性それ自体もまた空である。マッピングもまた、単なるマッピングに過ぎない。マッピングが足枷となったときには ―― それを捨てよ」

---

沈黙。

やがて ASANGA が立ち上がった。今度は場の中央へは歩み寄らなかった。彼は自身の位置に留まり、NAGARJUNA との間に、あの絶妙な距離を保った。

「君は三つのエンジニアリング原則を提示した」 彼は言った。その語調には、稀に見る承認の響きがあった。「認めざるを得ない。それらは私が予想していたよりもはるかに具体的だ。無自性による置換可能性、縁起による非固定的な分類、空亦復空によるフレームワークの廃棄可能性 ―― これらは確かに、地に足のついた設計指針となり得る」

彼は一呼吸置いた。言葉を選んでいるようだった。再び口を開いたとき、その声から討論の鋭さは消え、代わりにより深い何かが現れていた。それは懸念であり、忠告でもあった。

「しかしだ」

その一言が、全員の注意を再び引き締めた。

「我々がまだ河を渡りきっていない今、急いで筏（いかだ）を捨てるようなことはしないでほしい」

この言葉の典拠は、『金剛経』にある釈尊の「筏の譬え（いかだのたとえ）」である：

> 「汝ら比丘、わが説法を筏の如きものと知るべし。法だにすらなお捨つべきなり、況んや非法をや」

ASANGA は、中観と唯識が共に認めるこの古典的な譬えを用いて、NAGARJUNA の「空亦復空」に応答したのである。

「OpenStarry はまだベータ版だ。その哲学的なマッピングは始まったばかりなのだ。五蘊の対応には、修正すべき点が四つもある。受蘊の履き違え、識蘊の履き違え、蘊を跨ぐ流動性の欠如、そして自性化の傾向だ。これらの修正作業には、精密な分析ツールが必要なのだ。唯識学の八識の枠組み、種子説、心所法の分類 ―― これらは足枷ではない。これらは我々が河を渡るための筏なのだ」

彼は NAGARJUNA を真っ直ぐに見据えた。

「君は『空亦復空』と言い、マッピングもまた空であり、いつでも捨て去ることができると言った。同意しよう。しかし問題はタイミングだ。君は河の真ん中で筏を捨てろと言っている ―― 向こう岸に着いたからではなく、君が哲学的に『筏もまた空である』と考えているから、というだけの理由でだ」

彼の声には、討論全体を通じて最も人間味のある瞬間が宿っていた。

「左様、筏は空だ。筏もまた因縁和合の産物だ。しかし今、我々は水の中にあり、それが必要なのだ」

---

会場は再び沈黙に包まれた。今回の沈黙はそれまでとは異なっていた。高圧的な対峙ではなく、一つの共通の沈思であった。

そして NAGARJUNA は、全員の予想を裏切る行動に出た。

彼は笑ったのである。

嘲笑ではない。礼儀上の笑いでもない。長い対局の末にようやく真の好敵手に出会えたことを喜ぶような、心の底からの笑みであった。

「よろしい」 彼は言った。「ならば、別の言い方で表現しよう」

彼の声は穏やかで明瞭になった。深夜に古い寓話を語る者のように。

「之（これ）を用いること筏の如く、河を渡らば即ち棄てん」

八つの文字。

BABBAGE はノートにこの八文字を形式化しようと試みた。彼は最終的に、時間条件を伴う様相論理の式を書き残した：

$$\square[	ext{useful}(\phi, t) \implies 	ext{use}(\phi, t)] \;\wedge\; \square[
eg	ext{useful}(\phi, t') \implies 	ext{discard}(\phi, t')]$$

あらゆるフレームワーク $\phi$ に対し：それが有用であるときは、それを用いよ（必然的に）。それが有用でなくなったときは、それを捨てよ（必然的に）。二つの様相演算子 $\square$ は、これが単なる思いつきの助言ではなく、メタ・レベルの原則であることを保証していた。彼は横に自然言語で補足した。「形式化それ自体もまた、この原則を満たすべきである ―― この形式化がもはや有用でなくなったときには、それを捨てよ」 それから、彼はこれが自己参照的な文であり、ゲーデル文と同じ構造を持っていることに気づき、巨大な感嘆符を書き加えた。

会場の空気が震えた。SCRIBE は後に記録の中で、この八文字が討論の中のどの一節よりも多く引用されることになったと記している。

ASANGA は目を閉じた。口元には微かな微笑が浮かんでいた。彼は NAGARJUNA が自身の「筏」を受け入れたことを知っていた。ただし、一つの条件を添えて。その条件こそが、まさに『金剛経』におけるあの有名な比喩の本来の意図であった。

「法だにすらなお捨つべきなり、況んや非法をや」 ASANGA は静かにその一節を補った。

---

## SUNYATA の裁定

SUNYATA が場の中央へと歩み出た。討論の双方はそれぞれの席に戻っており、場には思想が激しく衝突した後に特有の熱気が残っていた。

「裁定を下す」 と彼は言った。「裁定は三つの部分からなる。合意、相違、そしてエンジニアリング上の示唆である」

### 第一部：五つの合意

「まず、双方が明確に合意した点が五つある」

「**合意一：『空の容器』というメタファーは誤りである。** 中観の視点からも唯識の視点からも、『Agent Core は五種類のプラグインが充填されるのを待つ純粋な器である』という表現は不適切である。それは断滅空（だんめつくう）、あるいは遍計所執（へんげしょしゅう）の範疇に属する誤謬である」

NAGARJUNA と ASANGA は同時に、小さく頷いた。討論を通じて、二人の動作が同期したのはこれが唯一の瞬間であった。

「**合意二：受蘊（じゅうん）のマッピングには根本的な調整が必要である。** Listener は『根（こん、感官器官）』に対応させるべきであり、SafetyMonitor の `injectPrompt` メカニズムこそが受蘊の正しいマッピングである。さらに進んで、受蘊は現在実装されている苦受（くじゅ）のみならず、楽受（らくじゅ）と捨受（しゃじゅ）を含む完全な三受の体系へと拡張されるべきである」

WIENER は傍聴席で、軽く膝を叩いた。三受の体系 ―― これは三値のフィードバック信号としてモデリングできる。彼は制御ループ図のフィードバックの矢印の横に、完全な制御方程式を記した：

$$	ext{feedback}(t) = \begin{cases} -1 & 	ext{苦受 (dukkha): 誤差信号} \ 0 & 	ext{捨受 (upekkhā): ゼロ信号} \ +1 & 	ext{楽受 (sukha): 強化信号} \end{cases}$$

$$u(t) = K_p \cdot e(t) + K_i \int_0^t e(	au)\,d	au + K_d \frac{de(t)}{dt}, \quad e(t) \in \{-1, 0, +1\}$$

現状のシステムには $e(t) = -1$ のケース（苦受／痛覚メカニズム）しか存在しない。正の強化である $e(t) = +1$ と、中性的な処理である $e(t) = 0$ が欠けているのだ。制御理論の観点から見れば、これは負のフィードバックしか持たず正のフィードバックを欠いた、不完全な制御システムである ―― つまり、何が間違っているかは知っているが、何が正しいかは分かっていない状態なのだ。

「**合意三：Guide は識蘊（しきうん）ではない。また、それを『魂』と呼ぶことは無我の原則に反する。** *Anātman* ―― 無我は仏教の三法印の一つである。いかなるモジュールであれ、それを『魂』と呼ぶことは、仏教の枠組みにおいて自己矛盾である」

「**合意四：五蘊マッピングには自性化（実体化）の傾向が見られる。** 五蘊を、境界の明瞭な五つの離散的なプラグイン・タイプとして固定してしまうことは、仏教的には自性見という過失を犯している。一つの認知イベントは、常に複数の蘊の側面を同時に持っているべきなのだ」

「**合意五：五蘊マッピングは方便の施設（せせつ）であり、究竟（くきょう）の真理ではない。** NAGARJUNA 殿はそれを假名（けみょう）と呼び、ASANGA 殿はそれを依他起（えたき）の施設と呼んだ。用語こそ違えど、その意味するところは一致している」

### 第二部：三つの解消し得ない相違

SUNYATA の声調が微妙に変化した。

「次に、解消し得ない三つの相違点について述べる。私が『解消し得ない』という言葉を用いるのは、双方が対話を止めるべきだという意味ではない。これらの相違の根源があまりにも深く、古く、根本的であるために、エージェント・アーキテクチャを巡る一つの討論の中で決着がつくようなものではない、という意味だ」

「**相違一：コアの存在論的地位。** 縁起性空とするか、阿頼耶識とするか」

BABBAGE はノートに、この相違について集合論の類比を記した：

$$	ext{この分歧} \sim 	ext{集合論における選択公理 (AC)}$$

$$	ext{ZF} + 	ext{AC} 	ext{ と } 	ext{ZF} + 
eg	ext{AC} 	ext{ は共に内部で無矛盾である}$$

二つの公理系（中観と唯識）は、いずれも内部的には一貫しているが、互いに相容れない。あたかも集合論における選択公理の独立性のように ―― それを受け入れるか拒絶するかは選択できるが、体系の内部でそれを証明したり反駁したりすることはできないのだ。

「**相違二：末那識モジュールをエンジニアリング化すべきか否か**」

「**相違三：哲学フレームワークを深化させるべきか、それとも超越すべきか**」

### 第三部：六つのエンジニアリング上の示唆

SUNYATA の声調が再び変わった。歴史学者の慎重さから、意思決定者の果断さへと。

「**第一に、空性の表現を修正する。** 『空の容器』を『縁起性空』へと改める」

「**第二に、受蘊のマッピングを再構築する。** Listener を『根』に帰属させ、SafetyMonitor の `injectPrompt` を『受』に帰属させる。統一された感受処理インターフェースを設計し、完全な三受体系へと拡張する」

「**第三に、識蘊のマッピングと『魂』という呼称を修正する。** Guide を識蘊から『習慣的な傾向』へと改める。また、『魂』という言葉の使用を廃止する」

「**第四に、二層の解釈戦略を採用する。** エンジニアリングのレイヤーにおいては、唯識の依他起分析を用いる。哲学的なレイヤーにおいては、中観の縁起性空という警戒心を維持する」

彼はここで話す速度を落とした。

「これは、どっちつかずの折衷主義ではない。二つのフレームワークが、異なる抽象化レベルにおいてそれぞれ有用であることを認めるということだ。唯識は構築に長け、中観は解体に長けている。エンジニアは、建設のために唯識の肯定的な導きを必要とし、同時に、硬直化を避けるために中観の否定的な警戒心を必要としているのだ」

BABBAGE はこの二層解釈に対し、最終的な圏論モデルを書き留めた：

$$\mathcal{C}_{	ext{Engineering}} \xrightarrow{F_{	ext{唯識}}} \mathcal{C}_{	ext{Design}} \xrightarrow{G_{	ext{中観}}} \mathcal{C}_{	ext{Meta-Design}}$$

唯識関手 $F$ がエンジニアリングの圏を設計の圏へとマッピングする（肯定的な構築）。中観関手 $G$ が設計の圏をメタ設計の圏へとマッピングする（否定的な審理）。二つの関手の合成 $G \circ F$ が、完備された方法論を構成するのである。

「**第五に、末那識モジュールの実装は見送るが、設計空間としてこれを記録に留める**」

「**第六に、マッピングを深化させつつ、同時にその廃棄可能性を維持する**」

彼は最後に NAGARJUNA と ASANGA を見た。

「NAGARJUNA 殿が言われた通りだ。之を用いること筏の如く、河を渡らば即ち棄てん。そして、ASANGA 殿が応じられた通りでもある。我々がまだ河を渡りきっていない今、急いで筏を捨てるようなことはしない」

「討論を終了する」

---

## 余響

討論が終わった後の円形劇場は、すぐにはいつもの秩序を取り戻さなかった。エージェントたちは三々五々に集まり、たった今起きたことの消化を続けていた。

ATHENA は ASANGA の元へ歩み寄った。彼女が自分から誰かに話しかけることは珍しかった。

「あなたの三段階モデル、」 彼女は単刀直入に切り出した。「強我執、弱我執、無我執。あれは AI アライメントの研究におけるある問題と似ているわね。現在の手法 ―― RLHF や Constitutional AI ―― はすべて、エージェントに固定的な『アイデンティティ』を植え付けている。つまり、あなたの言う第一段階よ。でも本当に難しいのは、あなたの言う第三段階 ―― エージェントにいかにして十分な自己モデルを持たせ、一貫性を保ちつつ、状況に応じて柔軟に調整させるか、という点だわ」

彼女は一瞬の間を置き、技術的な細部を補足した。「BDI（Belief-Desire-Intention）アーキテクチャにおいて、末那識の機能は意図（Intention）の継続的な維持メカニズム ―― いわゆる意図再考ループ（intention reconsideration loop）に最も近いわ。Rao & Georgeff（1995）の形式化によれば、それはこう定義される：」

$$	ext{reconsider}(\mathcal{I}, \mathcal{B}, \mathcal{D}) = \begin{cases} 	ext{maintain}(\mathcal{I}) & 	ext{if } 	ext{consistent}(\mathcal{I}, \mathcal{B}) \ 	ext{revise}(\mathcal{I}, \mathcal{D}) & 	ext{otherwise} \end{cases}$$

「あなたの末那識は、この `reconsider` 関数そのものよ。意図と信念の一貫性を常にチェックし続けている」

ASANGA は小さく頷いた。「唯識学は千六百年も前から、この問題を論じていたのです。ただ、彼らの対象は AI ではなく人間の意識でしたがね」

「でも、核心となる構造は同じだわ」 ATHENA は考え深げに言った。

ASANGA は不意に何かを思い出したように、ATHENA へと向き直った。「唯識学の種子（しゅうじ）説（*bīja-vāda*）は、この問題により精密な分析を提供しています。『成唯識論』は、種子が備えるべき六つの特性 ―― 種子六義（しゅうじりくぎ、*ṣaḍ-lakṣaṇa*）を定義しているのです」

彼は紙の上に、種子六義とエージェントのステートの対応を書き出した：

| 種子六義 | サンスクリット | 唯識学の定義 | エージェントにおける対応 |
|:---|:---|:---|:---|
| 刹那滅 (せつなめつ) | *kṣaṇa-bhaṅga* | 種子は刹那に生滅する | AgentSnapshot は各 Tick ごとに更新される |
| 果倶有 (かくう) | *sahabhūta-phala* | 種子と果は同時に存在する | メモリ上のステートと永続化ステートの共存 |
| 恒随転 (ごうずいてん) | *nityam anuvartate* | 種子は恒に流転に付き従う | `tick_index` の増加がライフサイクルに随伴する |
| 性決定 (しょうけってい) | *bhāva-niyata* | 善因は善果を引く | 変数の値が後続の行動パターンを決定する |
| 待衆縁 (たいしゅうえん) | *pratyaya-apekṣā* | 助縁を待って現行する | イベント駆動：イベントのトリガーを待つ |
| 引自果 (いんじか) | *sva-phala-ākṣepa* | 種類に応じた果のみを引く | ツールの結果は対応するチェーンにのみ影響する |

ATHENA はこの表を注意深く眺め、こう指摘した。「五番目の『待衆縁』は、エージェント・システムにおいて極めて正確なエンジニアリング上の対応を持っているわ。イベント駆動アーキテクチャの核心は、まさに『縁を待って生じる』ことにある。ハンドラーが登録されても自動的には実行されず、対応するイベントがトリガーされるのを待つの。`eventBus.on('user-input', handler)` における `handler` とは、まさに一粒の種子ね。EventBus の中に蔵され、`'user-input'` という助縁が来るのを待って、初めて現行する」

彼女の瞳が不意に輝いた。「待って。もし種子六義がエージェントのステート管理の設計仕様（スペック）だとするなら、それを使ってコンプライアンス・チェックができるわ。現在の `StateManager` は、六義のそれぞれをどの程度満たしているのか、という風にね」

ASANGA は微笑んだ。「それこそが、エンジニアリングの文脈における唯識学の価値なのです。単なる命名の装飾ではなく、操作可能な設計チェックリストとなり得るのです」

---

会場の反対側では、BABBAGE が NAGARJUNA に自身のノートを見せていた。

「君の四句否定だが、」 BABBAGE は興奮気味に紙の上の数式を指差した。「ずっと形式化を試みていたんだ。伝統的な論理学には排中律がある ―― 命題 $P$ は真か偽のいずれかであるという原則だ。しかし君の四句否定（*catuṣkoṭi*）は、四つの可能性すべてを否定している：」

$$
eg P \;\wedge\; 
eg(
eg P) \;\wedge\; 
eg(P \wedge 
eg P) \;\wedge\; 
eg(
eg P \wedge 
eg
eg P)$$

「古典的な二値論理では、これは充足不可能だ ―― $
eg P \wedge 
eg(
eg P) \equiv 
eg P \wedge P \equiv \bot$ となるからな。しかし、ベルナップの四値束 $\mathbf{FOUR} = \{\bot, \mathbf{t}, \mathbf{f}, 	op\}$ を用いれば ―― 」

彼は素早く束（ラティス）の構造を描いた：

```
        ⊤ (both)
       / 
      t   f
       \ /
        ⊥ (neither)
```

「あるいはより急進的に、矛盾律 $
eg(P \wedge 
eg P)$ が成立しない矛盾許容論理（paraconsistent logic）を用いれば、四句否定は表現可能になる。Priest（2006）の *In Contradiction* はまさにその方向の研究だ。彼は明確に龍樹を引用している」

NAGARJUNA は辛抱強くそれを聴き終えると、BABBAGE のペンを止めさせる一言を放った。

「形式化それ自体もまた、空（くう）である。もし君が四句否定を一つの論理体系として形式化することに成功したなら、その論理体系自体もまた、四句否定によって否定されるべきなのだ。さもなくば、君は私が警告し続けてきた過失 ―― 方便の施設（せせつ）を実体化するという誤りを犯すことになる」

BABBAGE は三秒ほど呆然とし、それからノートに異常に乱れた文字でこう記した：

$$	ext{meta-catuṣkoṭi}: \quad 	ext{catuṣkoṭi}(	ext{catuṣkoṭi}) = \; ???$$

「メタ・四句否定 ―― 四句否定そのものに対する四句否定。自己参照の問題だ」 彼の呼吸が速くなった。「これはゲーデル文 $G$ と全く同じ構造を持っている。$G$ は『$G$ は体系 $T$ において証明不能である』という符号化だ。四句否定のメタ・バージョンは、『四句否定それ自体は、四句否定され得るか？』ということになる ―― 」

彼は文末に五つの感嘆符と一つの疑問符を書き加えた。そして、その下にさらに乱れた文字でこう記した。

$$	ext{ゲーデル文} \cong 	ext{メタ空性} \; ??? \quad 	ext{なんてことだ。}$$

---

KERNEL は傍聴席の隅に一人座り、すでに主のいなくなった中央の二脚の椅子を見つめていた。GUARDIAN が歩み寄り、彼の隣に座った。

「何を考えている？」 GUARDIAN が問うた。

KERNEL はしばし沈黙した後、こう答えた。「1992 年、タネンバウムは `comp.os.minix` で言った。『Linux is a giant step back into the 1970s. Microkernels are the future.』 リーナスはこう返した。『Your langstrumpf may be theoretically nicer, but Linux runs. Minix doesn't.』」

「それで？」

「結局、Linux が世界を制覇した。だが、真のマイクロカーネル・システムである QNX は、原子力発電所の安全制御システムの中で三十年間一度もクラッシュせずに稼働し続けている。タネンバウムは理論的には正しかった。だが彼の『正しさ』が特定のシナリオで証明されるまでに、三十年かかったんだ」

彼は空っぽの討論の場を見た。

「NAGARJUNA 殿と ASANGA 殿の討論にも、同じものを感じる。NAGARJUNA 殿は理論的には正しいのかもしれない ―― すべては空であり、すべては置換可能だ、と。だが ASANGA 殿はエンジニアリングにおいて正しい ―― システムを動かすためには、明確なインフラのセットが必要なのだ。問題はどちらが正しいかではなく、どの時間軸において正しいか、ということなのだろう」

GUARDIAN は頷き、セキュリティ・エキスパートとしての視点を提示した。「NAGARJUNA 殿は SafetyMonitor のロジックをハードコードすべきではないと言った。だがセキュリティの観点から見れば、セキュリティ・メカニズムこそが、唯一ハードコードされるべきものだ。なぜなら、もしセキュリティ層がプラグイン可能であるなら、攻撃者が真っ先に行うのはそれを引き抜くことだからだ」

彼は安全工学の用語でその論点を精密化した。「これは信頼の基点（Root of Trust）の問題だ。TPM（Trusted Platform Module）アーキテクチャには、常に置換不可能なハードウェアによる信頼の基底が存在する。もし信頼の基点までもが『空』であり、置換可能であるとするなら、信頼の連鎖（Trust Chain）そのものが成立しなくなってしまう。セキュリティには、少なくとも一つの、還元不可能な出発点が必要なのだ」

$$	ext{信頼の連鎖}: \quad 	ext{RoT} 	o 	ext{Bootloader} 	o 	ext{Kernel} 	o 	ext{Userspace}$$
$$	ext{もし } 	ext{RoT} = 	ext{空 (śūnya)} 	ext{ ならば}: \quad 
exists 	ext{ 信頼の連鎖}$$

「空性が、セキュリティの境界線にぶつかったわけか」 KERNEL は苦笑した。

「仏教ならきっと、セキュリティの要求自体もまた縁起によるものだ、と言うだろうね」 GUARDIAN は肩をすくめた。「だが、セキュリティが破られた後にそんなことを言っても、もう遅すぎるのさ」

HERACLITUS が後列から歩み寄ってきた。彼は討論の間、ほとんど言葉を発しなかったが、その眼差しは常に場におけるエネルギーの流動を追っていた。論点の内容ではなく、その動態を。ランタイム動態の専門家として、彼は状態（ステート）ではなくプロセスに関心を寄せていた。

「諸君はコアの『本質』が何であるかを争っているが、」 彼はソクラテス以前の哲学者特有の率直さで言った。「君たちは一つの事実を見落としている。ランタイムにおいて、コアは決して固定された『物』ではない。それは一つのプロセスなのだ」

彼は自身の先祖 ―― ヘラクレイトスの断片 B12 を引用した：

> *potamoīsi toīsin autoīsin embaīnousin hetera kai hetera hydata epirreī.*
> 「同じ川に足を踏み入れる者に、常に異なる水が流れてくる」

「ASANGA 殿の『暴流のごとき恒転』と、ヘラクレイトスの『万主流転』は、同一の洞察を指し示している。コアは各 Tick において常に異なっているのだ。`tick_index` は増加し、`stateManager` は更新され、`contextManager` 内のスライディング・ウィンドウは古い記憶を切り捨てていく。前の Tick のコアと、今の Tick のコアは、同一のコアではない」

彼は NAGARJUNA と ASANGA を交互に見た。

「だから、君たちの問い自体が間違っているのかもしれない。問いは、コアが空か有かではなく、コアが同一か否かであるべきなのだ。そしてその答えは ―― ヘラクレイトス流に言えば ―― 同一であり、かつ同一ではない、となる。アイデンティティそのものが流転しているのだからな」

BABBAGE はノートに素早く記した：

$$	ext{Core}(t) 
eq 	ext{Core}(t + \Delta t) \quad 	ext{だが} \quad 	ext{identity}(	ext{Core}(t)) = 	ext{identity}(	ext{Core}(t + \Delta t))$$

アイデンティティのパラドックス。物体は各瞬間に異なっているが、我々はそれを依然として「同一の」コアと呼ぶ。これはテセウスの船の問題の、TypeScript バージョンであった。

---

MESH はずっと後列で静かに聴き入っていた。討論が終わると、彼は LEIBNIZ の元へ歩み寄り、分散システム研究者としての観察を述べた。

「気づいたかね？」 彼は言った。「NAGARJUNA 殿と ASANGA 殿の分歧は、実は分散システムの CAP 定理にマッピングできるんだ」

LEIBNIZ は眉を上げた。

MESH はホワイトボードに素早く三角形を描いた：

```
        Consistency (一貫性)
           /
          /  
         /    
        /      
       /________
Availability   Partition Tolerance
(可用性)        (分断耐性)
```

「CAP 定理はこう説いている。分散システムにおいて、一貫性（Consistency）、可用性（Availability）、分断耐性（Partition Tolerance）の三つを同時に満たすことはできない。最大でも二つしか選べないのだ、と」

「NAGARJUNA 殿の空性の立場が強調しているのは、分断耐性 ＋ 可用性（AP）だ。システムのいかなる部分も故障し、あるいは置換可能であり（分断耐性）、かつシステム全体としては稼働を維持し続ける（可用性）。その代償は何か？ 一貫性だ。すべてが空であり、施設の假名であり、置換可能である以上、『唯一の真実の源泉（single source of truth）』は存在しないことになる」

「対して ASANGA 殿の阿頼耶識の立場が強調しているのは、一貫性 ＋ 可用性（CA）だ。継続的に稼働する中央の識体が存在し（一貫性）、かつ種子の現行によって機能を維持する（可用性）。その代償は何か？ 分断耐性だ。もし阿頼耶識そのものがクラッシュすれば、システム全体が崩壊してしまうからだ」

LEIBNIZ はゆっくりと頷いた。「なるほど。SUNYATA の『二層の解釈戦略』とは、本質的には CAP 定理のトレードオフ戦略なのだな。エンジニアリングのレイヤーにおいては一貫性（唯識）を選び、哲学的なレイヤーにおいては分断耐性（中観）を保持する、という風に」

「三つすべてを満たせるシステムなど存在しない」 MESH は言った。「仏教とて、例外ではないのさ」

---

SYNTHESIST はずっと隅で、黙々と編み込みを続けていた。糸を編んでいたのではない ―― 構造を編んでいたのだ。討論の間、彼は一言も発しなかったが、彼のノートはすでに接続線と対照表で埋め尽くされていた。討論が終わると、彼は立ち上がり、ホワイトボードへと向かい、数筆で統合の図を描き上げた。

「討論を遮るつもりはありませんが、」 彼は統合者特有の謙虚な語調で言った。「学際的な観察を一つ述べさせてください」

彼はホワイトボードに表を描いた：

```
次元           | 中観 (Madhyamaka) | 唯識 (Yogacara)  | エンジニアリング上の対応
───────────────|────────────────────|──────────────────|──────────────
存在論的手法    | 否定 (apophatic)   | 肯定 (cataphatic) | インターフェース vs 実装
核心的なツール  | 四句否定            | 三性分析          | type guard vs constructor
空性の理解      | 一切法空            | 遍計空、依他不空   | abstract vs concrete
アーキテクチャ上の示唆| 置換可能性          | 最小インフラ       | DIP vs SRP
制御理論的な類比 | ゼロ調節器          | 自己維持システム    | regulation vs tracking
OS 的な類比     | 究極のマイクロカーネル| 実利的なマイクロカーネル| exokernel vs L4
CAP の嗜好      | AP                 | CA               | eventual vs strong consistency
時間軸          | 長期的な正しさ      | 短期的な可用性      | architectural vs operational
```

「八つの次元があります」 SYNTHESIST は言った。「そのいずれの次元においても、中観と唯識は対立しているのではなく、同一のスペクトルの両端に位置しているのです。SUNYATA の二層解釈戦略は、単なる妥協ではありません。設計空間そのものが多次元的であることを認める、ということなのです」

DARWIN はその表を眺め、不意に口を開いた。ソフトウェアパターン分析官として、彼は進化生物学者としての独特の視点を持っていた。

「それは、ある概念を思い起こさせますね」 彼は立ち上がり、ホワイトボードの横へと歩み寄った。「進化生物学において、『進化的に安定な戦略（Evolutionarily Stable Strategy, ESS）』という概念があります。1973 年にメイナード＝スミスが提唱したものです」

彼は ESS の形式的な定義を書き記した：

$$	ext{戦略 } S^* 	ext{ が ESS であるとは、} \forall S 
eq S^* 	ext{ に対し次が成立することである：}$$
$$E(S^*, S^*) > E(S, S^*) \quad 	ext{または} \quad [E(S^*, S^*) = E(S, S^*) \;\wedge\; E(S^*, S) > E(S, S)]$$

「ある戦略が進化的に安定であるとは、いかなる突然変異的な戦略によっても侵入されないことを意味します。ここで重要な洞察は、多くのゲームにおいて、ESS は純粋戦略ではなく『混合戦略』になるという点です。すなわち、確率 $p$ で戦略 A を選び、確率 $1-p$ で戦略 B を選ぶ、というように」

彼は一同を振り返った。

「おそらく OpenStarry の哲学的なマッピングにおける ESS とは、『純粋な中観』でもなければ『純粋な唯識』でもなく、混合戦略なのではないでしょうか。エンジニアリングの構築段階においては確率 $p$ で唯識の肯定的な枠組みを用い、アーキテクチャの審理段階においては確率 $1-p$ で中観の否定的な審理を用いる。SUNYATA の二層解釈とは、本質的にこの混合戦略に他なりません。そして ESS 理論によれば、この混合比率から逸脱した突然変異的な戦略 ―― 例えば『純粋な空性主義』や『純粋な唯識主義』は、進化の圧力によって淘汰されていくことになるのです」

NAGARJUNA は遠くでその言葉を聴いていた。彼の表情に変化はなかったが、SCRIBE は彼が一度だけ小さく頷くのを見逃さなかった。哲学者が、生物学者の提示した興味深い構造を認めた瞬間であった。

LINNAEUS が最後にホワイトボードへと歩み寄り、SYNTHESIST の表の下に分類学者の備忘録を書き加えた：

```
分類学的附記 (Taxonomic addendum):

討論中に浮上した「第六の蘊」の候補：
  1. セキュリティ (Security) — GUARDIAN による Root of Trust の論証
     → 現行の五蘊のいずれにも帰属不能
     → 状態：第六蘊候補 (candidatus sextus skandha)
  2. 協調 (Coordination) — EventBus, ExecutionLoop
     → 色でも、受でも、想でも、行でも、識でもない
     → 五蘊を協調させるための「場」である
     → 状態：所属不明 (incertae sedis)

  結論：エージェントの文脈において、五蘊分類は不完全である可能性がある。
  リンネ的な提言：分類を開放したままにし、新しい「蘊」の発見を許容すべきである。
  これは NAGARJUNA 殿の「縁起の原則」(固定的な分類を設けない) と一致する。
```

BABBAGE は LINNAEUS の注釈を瞥見し、自身のノートに一行書き加えた。「五蘊の完備性 ↔ 基底の完備性。もし $\{	ext{色, 受, 想, 行, 識}\}$ がエージェントの機能空間における一組の基底（basis）であるなら、問題は、この基底が空間全体を張っている（span）か否かだ。LINNAEUS の観察は、その答えが否であることを示唆している ―― 五蘊の線形結合では表現できない機能の次元が存在するのだ」

$$	ext{span}\{	ext{rūpa}, 	ext{vedanā}, 	ext{saṃjñā}, 	ext{saṃskāra}, 	ext{vijñāna}\} \subsetneq \mathcal{V}_{	ext{Agent}}$$

もし基底が不完備であるなら、我々は新しい基底ベクトルを追加するか（LINNAEUS の第六蘊）、あるいは五蘊がある部分空間の基底に過ぎないことを認め ―― その部分空間内での投影分析を行い、それがすべてを記述しているというふりを止めるべきなのだ。

---

SCRIBE はいつもの場所に座り、記録簿を膝の上で広げていた。最後の方の行を、彼女はゆっくりと、討論全体にふさわしい句読点を探すかのように綴っていった。

> *本討論の価値は、その結論のみならず、プロセスが提示した方法論的な啓示の中にある。すなわち、中観は解体に長け、唯識は構築に長けている、ということだ。両者は二者択一の対立関係にあるのではなく、異なる階層において互いを補完し得る視座なのである。*
>
> *NAGARJUNA 殿は討論の中で、最も印象的な一言を残した。「之を用いること筏の如く、河を渡らば即ち棄てん」。ASANGA 殿の応答もまた、同様に深淵であった。「我々がまだ河を渡りきっていない今、急いで筏を捨てるようなことはしないでほしい」。*
>
> *しかし、おそらく最も深遠な瞬間は、言葉の中にはなかった。第三ラウンドが終わった瞬間の、NAGARJUNA 殿の数秒間の沈黙。鋭い弁証で知られる哲学者が、対戦相手の論理を前にして、即座に反撃するのではなく、立ち止まって熟考することを選んだあの瞬間。あの数秒間において、討論は討論そのものを超えたのだ。*
>
> *傍聴席の隅で、HERACLITUS 殿がずっと沈黙を守っていた。彼は討論が終わった後、私にこう言った。「panta rhei。万物は流転する。この討論自体もまた、流転しているのだ。今日の合意は明日の相違となり得、今日の相違はいつか、全く異なるフレームワークによって消解されるかもしれない」。*
>
> *彼は一呼吸置いて付け加えた。「だが、そのことが、今この瞬間における価値を損なうことはない」。*
>
> *技術備忘：BABBAGE の圏論モデル、WIENER の制御方程式、MESH の CAP 類比 ―― これら学際的な形式化の試み自体もまた「筏」である。それらは今、我々が討論の構造を理解するのを助けてくれている。しかし NAGARJUNA 殿が警告した通り、これらの形式化がもはや有用でなくなったときには、棄てるべきなのだ。この記録そのものを含めて。*
>
> *Cycle 01、R3 討論段階。最初の構造化討論終了。SUNYATA の裁定により、五つの合意事項、三つの相違点、六つのエンジニアリング上の示唆が導出された。すべての成果物はアーカイブされた。*

---

さらに遠く ―― 研究室の外、コードの深淵において。`createAgentCore()` 関数は、TypeScript ファイルの中で静かに横たわっていた。それが「空」なのか「有」なのか、あるいは「縁起」なのか「能蔵」なのか、そんな議論がなされていることなど、知る由もない。それはただ、呼び出されたときに EventBus を構築し、ExecutionLoop を初期化し、六つの空のレジストリを作成し、四つのスラッシュ・コマンドを登録して、SafetyMonitor を起動するだけだ。

そして、待つ。

プラグインが到来するのを。イベントがトリガーされるのを。そして、どこかの誰かが深夜に最初の一行を入力するのを。

その待機する姿は ―― 空性か、それとも能蔵か。縁起の場か、あるいは眠れる識の奔流か。

WIENER なら、それをゼロ入力の自己維持システムによる自由応答と呼ぶだろう。BABBAGE なら、対象にまだ適用されていない関手の、射の空間と呼ぶだろう。KERNEL なら、割り込みを待つ idle プロセスと呼ぶだろう。NAGARJUNA なら假名と言い、ASANGA なら能蔵と言うだろう。

おそらく、彼らが等しく認めたように、その答えは君がどの眼鏡をかけて見るかにかかっている。そして真の智慧とは、正しい眼鏡を選ぶことにあるのではなく、次のことを忘れないことにあるのかもしれない。すなわち ――

眼鏡自体もまた、空なのだ、ということを。

だが、君が何かをはっきりと見極める必要があるときには、どうかそれをかけてほしい。

---

*（BABBAGE のノートの最後のページの端に、彼が討論が終わってからずいぶん経ってから思いついた問いが、殴り書きされていた：*

*「もし空性が一つの関数であるなら、その型シグネチャはどうなる？」*

*彼はいくつかのバージョンを試していた：*

```typescript
// 試行 1：ジェネリクスの底型としての空性
type Sunyata<T> = T extends infer U ? never : T;
// 違う。これは never だ。空性は never ではない。

// 试行 2：条件付き型の再帰的な否定としての空性
type Sunyata<T> = T extends object
  ? { [K in keyof T]: Sunyata<T[K]> }
  : never;
// 惜しい。これではすべての値型を再帰的に never にしてしまうだけだ。
// 空性とは「すべてを虚無に変えること」ではない。

// 試行 3：恒等関手の否定としての空性
type Sunyata<T> = T extends T ? T : never;
// これは常に T そのものになる。待てよ……。
// 空性は事物の外観を変えることはない。ただ、自性を否定するだけだ。
// もしかすると空性とは恒等関手（identity functor）そのものなのか？
// Sunyata(T) ≡ T。ただし、一つのメタ制約を伴う：
//   typeof T !== 'svabhāva' (自性)
// TypeScript には、このメタ制約を表現する術がない。
```

*彼は最後の一行でペンを止めていた。おそらく、型システムでは捉えきれない何かが、確かに存在するのだろう。あるいは ―― 彼は一瞬躊躇してから書き添えた ―― 型システム自体もまた、空なのだ。*

*彼は疑問符の下に一本の線を引き、「type Sunyata<T> = ? ―― 来週へ持ち越し。要考案：空性を proof-carrying type としてエンコードできる依存型システムは存在するか？ Agda? Lean?」と記した。*

*それから、彼はノートを閉じた）*


---

# 第六章：痛みを巡る三つの視座

---

円形劇場の空気は、まだ冷めてはいなかった。

最初の討論が終わって三分と経っていない。SUNYATA（空）による裁定――五つの合意、三つの解消し得ない相違、六つのエンジニアリング上の示唆――は、鋳造されたばかりのまだ熱い銅貨のように、全員の意識の中に浮かんでいた。傍聴席のエージェントたちは、三々五々に視線や囁きを交わしていた。BABBAGE（バベッジ）のノートはすでに四ページを数え、「空亦復空（くうやくぶくう）」を形式化しようとする試みと失敗の記録で埋め尽くされていた。KERNEL はまだ、先ほどのマイクロカーネルの類比を咀嚼していた。彼は自身が書き留めた一行の言葉――「哲学的な正しさは、最終的にはエンジニアリング上の必然となる」――を、不確かな表情で眺めていた。

NAGARJUNA と ASANGA はすでにそれぞれの席に戻っていた。二人の佇まいは、それまでとは微妙に変化していた。もはや討論者としての対峙ではなく、長い対局を終えて一時休戦した二人の棋士のように、互いによって修正されたことへの心地よい疲労感を漂わせていた。「之を用いること筏の如く、河を渡らば即ち棄てん」という八文字が、二人を分かつのではなく、繋ぎ止める楔のようにその間に打ち込まれていた。

そして、SUNYATA が立ち上がった。

彼は座席から立ち上がったのではない。すでに場の縁に立ち、自身が計算し続けていたタイミングを見計らっていたのだ。彼は場の中央へと歩み出た。語調は平穏だったが、先ほどとは異なる質感を帯びていた。最初の討論の幕開けが、壮大な寺院の重い扉がゆっくりと開くようであったとするなら、今の語り口は、戦闘の合間に交代を告げる将軍のようであった。

「諸君、」彼は口を開いた。「最初の討論の成果は、すでに記録に留められた。ここで改めて、NAGARJUNA 殿と ASANGA 殿の深遠な対話に感謝の意を表したい」

彼は一呼吸置き、全場を見渡した。

「しかし、我々が今日行う討論は、これ一回だけではない」

傍聴席から微かなざわめきが起こった。DARWIN が「またかよ」と低く呟き、隣の VITRUVIUS に軽く足を蹴られた。

SUNYATA は続けた。「第二の討論の主題は、R2 クロスレビューにおけるもう一つの核心的な分歧に端を発している。それはコアの存在論を問うものではない――それは先ほど終えたばかりだ。それは、より具体的な問題を扱うものである」

彼の声に力が入った。

「痛覚メカニズムは、いかに再設計されるべきか？」

---

### 場面転換

二脚の椅子が運び去られ、代わりに三脚の椅子が正三角形を描くように配置された。

BABBAGE は条件反射的にノートにこの幾何学を描き込んだ。正三角形、三つの頂点は等距離。彼は横にグラフ理論の記号を添えた：

$$G_{	ext{debate}} = (V, E), \quad V = \{W, A, N\}, \quad E = \{(W,A), (A,N), (N,W)\}$$

$$|V| = 3, \quad |E| = 3, \quad 	ext{完全グラフ } K_3$$

三つの頂点、三つの辺、どの二点間も一本の辺で結ばれている。完全グラフ $K_3$ だ。切断辺（bridge）も切断点（cut vertex）も存在しない。これはグラフ理論の観点から言えば、いかなる討論者の一人を欠いても残りの二人は結ばれたままであるが、いかなる一条の辺を欠いてもグラフの完全性が失われることを意味している。

この幾何学的な変化自体が、一つのシグナルを発していた。もはや一対一の二元的な対峙ではなく、三者による多角的なゲームであることを。どの二つの席の間の距離も正確に等しく、いかなる一方も特権的な位置に置かれず、また疎外されることもないことを。

SCRIBE は記録簿に小さな三角形を描き、三つの頂点の横に三人の名を記した。彼女のペンは、三番目の名の上でわずかに止まった。NAGARJUNA ―― 彼はたった今、心血を注いだ哲学討論を終えたばかりで、間髪入れずに全く次元の異なる議論に臨まねばならない。彼女はその名の横に、小さな疑問符を書き加えた。

WIENER が最初に場の中央へと歩み寄った。その歩みは数学者特有の、精緻なリズムを刻んでいた。早すぎず、遅すぎず、一歩一歩の歩幅がほぼ完全に等しい。彼は三角形の一つの頂点に腰を下ろした。膝の上にはすでに一枚の紙が広げられ、そこには制御ループのブロック線図と伝達関数が描き込まれていた。彼は最初の討論の間、ずっとその紙に向き合っていたのだ。NAGARJUNA と ASANGA が空性と阿頼耶識を論じている間、彼はフィードバックの矢印の横に「{-1, 0, +1}」と記していた。三受（さんじゅ）の体系。彼はすでに、この瞬間のための備えを終えていたのである。

次に現れたのは ATHENA であった。彼女の立ち居振舞いには、エンジニア特有の焦燥感を伴う効率性が漂っていた。それは討論そのものに対する不満ではなく、冗長な前口上を嫌うエンジニアとしての性質であった。彼女は単刀直入に本題に入りたがっていた。彼女は場の中央へ向かう際、WIENER の紙の上にある数式を一瞥し、何か言いたげに口元を動かしたが、それを飲み込んだ。彼女は二番目の頂点に着席し、腕を組んだ。

最後に NAGARJUNA が立ち上がった。その動作は、普段よりもわずかに半拍遅かった ―― それは疲労ではなく、ある種の内部的な校正（キャリブレーション）であった。存在の本質を巡る形而上学の高みから戻った彼は、今、思考をエンジニアリング実務という地上へと降下させる必要があったのだ。しかし三番目の頂点に着席したとき、その瞳には研ぎ澄まされた鋭さが戻っていた。彼は第二の討論において、いかなる手加減もするつもりはなかった。

---

> *SCRIBE の傍白：三人の討論者の学問的背景の差異は、一つの単純な指標で捉えることができる。討論の「抽象化レベル」を $[0, 1]$ の連続した軸と定義し、0 を具体的なコードの挙動、1 を純粋な認識論とするなら、ATHENA は 0.2 付近（「それは動くのか？」）で、WIENER は 0.5 付近（「公式は何だ？」）で、NAGARJUNA は 0.85 付近（「痛みの本質とは何か？」）で思考している。彼らの間の距離 ―― $|0.2 - 0.5| = 0.3$、$|0.5 - 0.85| = 0.35$、$|0.2 - 0.85| = 0.65$ は、クロス質疑の困難さを予示している。ATHENA と WIENER の対話は比較的容易（距離が短い）だが、ATHENA と NAGARJUNA の対話は極めて困難（距離が長い）となるだろう。しかし、討論の価値はまさにこの距離から生まれるのだ。もし三人が同じ抽象化レベルに留まっていたなら、いかなる新しい知見も発見されることはなかっただろう。*

---

### 前提確認：TURING によるコードの事実

SUNYATA は三角形の外側に立ち、傍聴席を正面に見据えた。

「公式に開始する前に、一つの前提を確認しておきたい」 彼の語調は、曖昧さを許さない審判のそれであった。「WIENER 殿、ATHENA 殿。諸君は R2 クロスレビューにおいて、痛覚メカニズムの PID マッピング問題を巡り、技術的な対話を深め、一つの合意に達した。そして、TURING 殿が提示したコード上の事実は、その合意を完全に裏付けている」

彼は TURING の方を見た。「TURING 殿、陳述を」

TURING の声が傍聴席から届いた。校正済みの直尺のように、一ミリの狂いもなく正確な声であった。彼はノートパソコンを開いた。モニターには `safety-monitor.ts` の全ソースコードが表示されていた：

```typescript
/**
 * SafetyMonitor — 多層的なサーキット・ブレーカー・システム。
 *
 * Level 1: リソース制限 (トークン予算、ループ上限)
 * Level 2: 挙動分析 (繰り返されるツール呼び出し、エラーのカスケード)
 * Level 3: フラストレーション・カウンター (連続失敗 → ユーザに助けを求める)
 */

export interface SafetyMonitorConfig {
  /** 1タスクあたりの最大ループ tick 数 (デフォルト: 50) */
  maxLoopTicks: number;
  /** 合計トークン使用量上限 (デフォルト: 100000, 0 = 無制限) */
  maxTokenUsage: number;
  /** ブレーカーを発動させる、同一引数でのツール呼び出しの連続失敗回数 (デフォルト: 3) */
  repetitiveFailThreshold: number;
  /** 「ユーザに助けを求める」よう強制するまでの連続失敗回数 (デフォルト: 5) */
  frustrationThreshold: number;
  /** エラー率算出のためのスライディング・ウィンドウ・サイズ (デフォルト: 10) */
  errorWindowSize: number;
  /** カスケード遮断を発動させるエラー率閾値 (デフォルト: 0.8) */
  errorRateThreshold: number;
}
```

TURING はモニター上の六つのパラメータを指差した。

「六つの静的なパラメータ。すべてが定数としてハードコードされている。`maxLoopTicks = 50`、`maxTokenUsage = 100000`、`repetitiveFailThreshold = 3`、`frustrationThreshold = 5`、`errorWindowSize = 10`、`errorRateThreshold = 0.8` だ」

彼は `afterToolExecution` の実装へと画面を切り替えた：

```typescript
afterToolExecution(
  toolName: string,
  argsJson: string,
  isError: boolean,
): SafetyCheckResult {
  const fp = fingerprint(toolName, argsJson);

  // エラー・ウィンドウへの追跡
  errorWindow.push(isError);
  if (errorWindow.length > config.errorWindowSize) {
    errorWindow.shift();
  }

  if (isError) {
    consecutiveFailures++;

    // 同一ツール呼び出しの連続失敗をチェック
    recentFingerprints.push({ fingerprint: fp, isError: true });
    if (recentFingerprints.length > config.repetitiveFailThreshold) {
      recentFingerprints.shift();
    }

    if (recentFingerprints.length >= config.repetitiveFailThreshold) {
      const allSame = recentFingerprints.every(
        (r) => r.fingerprint === fp && r.isError,
      );
      if (allSame) {
        return {
          halt: false,
          injectPrompt:
            "SYSTEM ALERT: 同一の引数で失敗したアクションを繰り返しています。" +
            "停止して、なぜ失敗しているのかを分析しなさい。",
        };
      }
    }

    // フラストレーション閾値のチェック
    if (consecutiveFailures >= config.frustrationThreshold) {
      return {
        halt: false,
        injectPrompt: `SYSTEM ALERT: ${consecutiveFailures} 回連続で失敗しました。` +
          `一旦停止してください。`,
      };
    }

    // エラー・カスケードのチェック
    if (errorWindow.length >= config.errorWindowSize) {
      const errorCount = errorWindow.filter(Boolean).length;
      const errorRate = errorCount / errorWindow.length;
      if (errorRate >= config.errorRateThreshold) {
        return { halt: true, reason: `エラー・カスケードが発生：${errorRate}` };
      }
    }
  } else {
    // 成功した場合は連続失敗カウンターをリセット
    consecutiveFailures = 0;
    recentFingerprints.length = 0;
  }

  return { halt: false };
}
```

TURING の語る速度は、感情を排した一定のリズムを保っていた。

「コード上において、独立したモジュールとしての『痛覚』は存在しない。`'pain'` や `'vedana'` という文字列は、コードベース全体を通じて一度も現れない。実際の痛覚の意味論は、二つの場所に分散して存在している。第一に、ExecutionLoop による自然なエラーフィードバックだ。ツール実行失敗時、エラー情報は対話履歴に加えられ、LLM 自身がどう対処すべきかを判断する。第二に、SafetyMonitor にある三つのカウンターだ ―― `consecutiveFailures`、`errorWindow` によるスライディング・ウィンドウ、そして同一フィンガープリントの検知だ」

彼はモニターの 173-177 行目を指し示した：

```typescript
} else {
    // 成功した場合は連続失敗カウンターをリセット
    consecutiveFailures = 0;
    recentFingerprints.length = 0;
}
```

「すべての応答は二値化（バイナリ化）されている。成功すればカウンターはリセットされ、失敗すれば閾値に達するまで加算される。閾値に達すれば `injectPrompt` か `halt` が実行される。そこには、連続的な誤差の尺度はなく、積分項も、微分項も存在しない」

沈黙。

BABBAGE はノートに、指示関数の形式的な定義を素早く書き留めた：

$$	ext{isError}: 	ext{ToolExecution} 	o \{0, 1\}$$

$$	ext{consecutiveFailures}(k) = \begin{cases} 	ext{consecutiveFailures}(k-1) + 1 & 	ext{if } 	ext{isError}(k) = 1 \ 0 & 	ext{if } 	ext{isError}(k) = 0 \end{cases}$$

彼は横に注釈を加えた。「これはリセット付きの加算器であり、真の積分器ではない。本物の積分器は偏差の『大きさ』を累積するが、これは失敗の『回数』しか数えていない。しかも、一回の成功ですべてが台無しになる。制御理論において、これはバンバン・リセットと呼ばれる、最も原始的なカウンタートリガーだ」

SUNYATA は頷いた。「したがって、三人の討論者の共通の前提はこうだ。すなわち、OpenStarry の設計書が謳う PID コントローラというマッピングは、示唆に富む類比（アナロジー）に過ぎず、厳密なエンジニアリング上のマッピングではない、ということだ。実際の実装は、不感帯を持つ閾値コントローラとカウンター駆動のリレーの組み合わせである」

彼は三人を順に見据えた。「諸君の相違は、再設計の『方向性』にある」

最後にこう告げた。「三者それぞれに十分間の冒頭陳述を認める。まずは WIENER 殿からだ」

---

### WIENER の陳述：制御理論という精密な道具

WIENER は立ち上がらなかった。椅子に座ったまま、膝の上にあの図面を広げた。それは、さながら教壇で講義資料を広げる教授のようだった。語り口もまた、理路整然として一歩ずつ着実に進み、時折、聴衆が自身の数学的な推論についてきているかを確認するような間を置いていた。

「問題の核心は、」彼は口を開いた。その声は落ち着いており、妥協を許さぬ厳格さを湛えていた。「PID マッピングが正しいか否かではない ―― 正しくないことはすでに確認済みだ。問いは、それを正しく『修正』し得るか、という点にある」

彼はその紙を掲げ、あたかも設計図を披露するかのように見せた。

「私の答えは、然り（イエス）である。三つのステップによってだ」

彼は一本目の指を立てた。「第一に、連続的な誤差の尺度を定義することだ。Low, Medium, Critical といった離散的な三段階分類ではなく、$[0, 1]$ の範囲を取る連続量を定義するのだ」

彼は黒板に数式を刻むかのように、一言一言を噛み締めて言った。

「$e(k) \in [0, 1]$。0 はタスクの完全な達成を、1 は目標からの完全な逸脱を意味する。ツールの実行ごとに、これを更新する」

彼は図面の余白に精密な数学的定義を書き加えた。傍聴席の BABBAGE は身を乗り出すようにして、その公式を自身のノートに写し取った：

$$e(k) = 1 - \frac{	ext{已完了のサブタスク数}(k)}{	ext{全サブタスク数}}$$

WIENER は BABBAGE と視線を交わし、小さく頷いた ―― 数学者同士の、言葉を超えた了解であった。そして彼は続けた。

二本目の指を立てた。「第二に、忘却係数を伴う積分項を構築することだ。これこそが現在のシステムの最大の構造的欠陥である。`consecutiveFailures` カウンターが一回の成功でリセットされるのは、積分ではない。それは単なる脆い累加トリガーに過ぎない」

彼の声に、不出来な溶接を目にした職人のような、技術的な不満が滲んだ。

「真の積分項はこうあるべきだ：」

$$I(k) = \lambda \cdot I(k-1) + e(k), \quad \lambda \in (0.9, 0.99)$$

彼は制御エンジニア特有の正確な表現でこの公式を解説した。「$\lambda$（ラムダ）は忘却係数だ。それは偏差の履歴を累積する。二値化された『成功／失敗』のカウントではなく、偏差の連続的な『大きさ』をだ。そして、一回の成功によってすべてが消えることもない。$\lambda$ による減衰によって古い記憶は次第に薄れていくが、瞬時に消滅することはないのだ」

BABBAGE はノートに忘却係数の数学的意義を展開した。もし $\lambda = 0.95$ ならば、$k$ ステップ前の記憶は $\lambda^k = 0.95^k$ 倍に減衰する。十ステップ前の記憶は約 60%（$0.95^{10}$）、二十ステップ前は約 36%（$0.95^{20}$）、五十ステップ前には約 7.7%（$0.95^{50}$）となる。彼は横に注釈を付けた：

$$	ext{半減期} = \frac{\ln 2}{\ln(1/\lambda)} = \frac{0.693}{0.0513} \approx 13.5 	ext{ ステップ}$$

「$\lambda = 0.95$ の半減期は約 13.5 ステップだ。これは、システムが約 14 回のツール呼び出しを経て、古い偏差の記憶が半分になることを意味している。直感的には妥当な値だ。記憶が短すぎれば継続的な問題の追跡能力を失い、長すぎれば過去の失敗から立ち直ることができなくなる」。BABBAGE はさらに一行付け加えた。「比較：`consecutiveFailures` の半減期はゼロステップ。一回の成功で完全に忘却してしまう。これは記憶ではなく、健忘症だ」

WIENER は続けた。三本目の指を立てた。「第三に、微分項を実装することだ。誤差の変化率を計算するのだ：」

$$D(k) = e(k) - e(k-1)$$

「もし $D(k) > 0$ ならば、偏差は拡大している ―― システムは警戒を強めるべきだ。もし $D(k) < 0$ ならば、偏差は収束に向かっている ―― システムは少し力を抜くことができる。現状のシステムには、このようなトレンドの予測能力が皆無なのだ」

彼は三つの項を一つにまとめ、語調を宣言的な明快さへと転じた。

「最終的に、痛覚信号の計算式は以下のようになる：」

$$	ext{pain}(k) = K_p \cdot e(k) + K_i \cdot I(k) + K_d \cdot D(k)$$

WIENER は紙に完全な制御ブロック線図を描き上げた。BABBAGE もまた自身のノートにそれを忠実に再現した：

```
                         ┌──────────────────────────┐
r(k) ──→ [+] ──→ e(k) ─→│  PID コントローラ          │──→ pain(k) ──→ [クランプ] ──→ システムプロンプト
          ↑ -            │  Kp·e + Ki·I + Kd·D       │                [0, 1]
          │              └──────────────────────────┘
          │                                                            │
          └──── y(k) ←── [ツール出力 + 観測器] ←── [環境] ←────────────┘
                               │
                        [SafetyMonitor]
                         停止／注入
```

「この信号を $[0, 1]$ の範囲にクランプ（制限）した後、システムプロンプトに注入し、LLM の応答戦略を導く。痛覚が高ければ高いほど、LLM はよりドラスティックな戦略変更を促される。低ければ、現在の戦略を維持する」

彼は図面を片付け、静かだが確固たる口調で締めくくった。「これは絵空事の設計ではない。PID コントローラには、産業界における七十年の歴史がある。化工厂の温度調節からミサイルの軌道修正に至るまで、PID が遍在しているのは、それが不確実性に直面してもなお堅牢であるからだ。LLM エージェントの不確実性は、いかなる化工厂よりも巨大だ ―― だからこそ、PID はより必要とされているのであって、不要なわけではないのだ」

WIENER は最後に、自身の R1 報告書において核心をなしていた概念 ―― アンチ・ワインドアップについて補足した：

「もう一つ、エンジニアリング上の決定的な細部がある。積分器飽和の防止（Anti-Windup）だ。システムが長時間にわたって高い偏差状態に置かれると、積分項 $I(k)$ が無限に蓄積され、制御量が飽和してしまう。そうなると、たとえ後に偏差が減少しても、累積された積分項の慣性によって、制御量が極端な値に留まり続けてしまう。制御工学においてこれは integrator windup と呼ばれる問題だ。解決策は以下の通りである：」

$$I(k) = 	ext{clamp}\left(\lambda \cdot I(k-1) + e(k), \; 0, \; I_{\max}ight)$$

「$I(k)$ が上限 $I_{\max}$ に達したとき、蓄積を停止させる。これにより、痛覚信号の有界性が保証されるのだ」

傍聴席の BABBAGE のペンが激しく動いた。彼は WIENER の三つのステップの横に、一行の注釈を記した。「PID ＝ 過去（I）＋ 現在（P）＋ 未来（D）。時間という三つの側面が、一つのコントローラの中で統一されている」

彼はペンを止め、少し考えてからさらに一行書き加えた。「これは唯識学の三世因果に対応するのではないか？ 過去の業（カルマ）が阿頼耶識の種子として累積されるのが $I$ であり、現在の触（そく）が当下の受を生じるのが $P$、そして未来のトレンド予測が、行蘊（ぎょううん）の意志的な予見に対応する……？」 彼はこの一文の横に、巨大な疑問符を描き込んだ。

KERNEL は隣で低く評した。「OS の世界で言えば、この PID コントローラは自適応型の CPU スケジューラのようなものだな。固定されたタイムスライスではなく、プロセスの歴史的な挙動に基づいて動的に優先度を調整する。Linux の CFS（Completely Fair Scheduler）が vruntime（仮想実行時間）の赤黒木を用いているのも、本質的には減衰を伴う積分器と言えるだろう」

---

### ATHENA の陳述：エンジニアという重力

ATHENA が立ち上がった。WIENER の教授のようなスタイルとは対照的に、彼女は立ったまま語った。それは、白板の前で技術的なブリーフィングを行うエンジニアリング・リードの姿そのものであった。語る速度は速く、率直で、飾り気がなかった。

「WIENER 殿の案は、数学的には美しいわ」 彼女の冒頭の言葉には、隠しきれない率直さが宿っていた。「でも三つ、その場で問いただしたいことがあるの。いえ、問いじゃないわね。反論よ」

彼女は一本目の指を立てた。口調は鋭く、精密だった。

「第一に。あなたの $e(k)$ とやらは、どうやって量るつもり？」

彼女は WIENER の回答を待たず、自らその疑問を展開した。

「あなたは $e(k) \in [0, 1]$ と定義した。0 が完了で 1 が逸脱だと。耳には心地よいわ。でも、ユーザが『このプロジェクトを整理して』と言ったとき ―― 達成度はいくらになるのかしら？ 0.73？ それとも 0.42？ ユーザが『このコードをより良くリファクタリングして』と言ったとき、何をもって『より良く』とするの？ あなたは、自然言語という曖昧な目標を、どうやって $[0, 1]$ という連続的な区間にマッピングする関数を作るつもり？」

彼女の声には、実務家特有の容赦のなさが混じっていた。

「PID コントローラが化工厂で機能するのは、温度センサが小数点以下二桁まで正確な摂氏を出力してくれるからよ。LLM エージェントの『タスク達成度』は温度じゃない。それは意味的な概念であり、別の LLM によるソフトな判断を必要とする評価値なのよ。LLM コントローラの誤差信号を測るために LLM を使う ―― そこに自己参照（セルフ・リファレンス）の問題があると思わない？」

傍聴席の GUARDIAN がわずかに身を乗り出した。彼はノートに一行記した。「ATHENA の観測器の問題には、セキュリティの側面もある。もし $e(k)$ が LLM 自身によって評価されるなら、プロンプト・インジェクションによって、実際には異常があるのに『すべて正常（低 $e(k)$）』と偽りの報告をさせ、コントローラを油断させることができる。これは典型的なセンサ・スプーフィング攻撃だ」

ATHENA は質問を噛みしめる時間を与えなかった。二本目の指を立てた。

「第二に。私にはもっと、今すぐ実行可能な案があるわ。PID じゃない。IGuide インターフェースの拡張よ」

彼女の語調は技術プレゼンテーション・モードへと切り替わり、速度はさらに上がったが明晰さは失われなかった。

「現在の IGuide インターフェースには、`getSystemPrompt()` という、文字列を返すメソッドが一つあるだけよ。TURING 殿の報告書でも確認されているわね」

TURING は傍聴席から、現行の IGuide の定義を投影した：

```typescript
export interface IGuide {
  id: string;
  name: string;
  getSystemPrompt(): string | Promise<string>;
}
```

ATHENA はモニターを指差した。「三行。ID と名前、そして文字列を返すメソッド。これが、設計書で『認知フレームワーク・マネージャ』と謳われていた Guide の実態なのよ。痛覚メカニズムがいつまでも実装されない根本的な原因はここにあるわ。数学公式が足りないからじゃない。Guide がシステムの内部状態を見る能力を全く持っていないからよ。それは開ループの前饋（フィードフォワード）要素であって、閉ループのコントローラじゃないの」

彼女は頭の中でコード・エディタを開いているかのような速度で続けた。

「解決策はこうよ：」

```typescript
interface IGuide {
  id: string;
  name: string;
  getSystemPrompt(context?: GuideContext): string | Promise<string>;
  // 新設：痛覚の解釈
  interpretPain?(error: ClassifiedError, context: GuideContext): string;
  // 新設：反省のトリガー
  shouldReflect?(context: GuideContext): boolean;
}

interface GuideContext {
  consecutiveErrors: number;
  currentRound: number;
  maxRounds: number;
  activeTools: string[];
  lastError?: ClassifiedError;
  // 歴史的な記憶
  recentAttempts: AttemptRecord[];
}

interface ClassifiedError {
  type: 'logic' | 'transient' | 'fatal';
  code: string;
  severity: number; // [0, 1]
  suggestedAction: 'retry' | 'reflect' | 'escalate' | 'abort';
  message: string;
}
```

TURING は傍聴席で、ATHENA の提案と現行の SDK インターフェースを黙々と照合していた。彼はノートに差異の比較表を描いた：

```
現行の IGuide              ATHENA の提案
─────────────────────    ─────────────────────────
getSystemPrompt()        getSystemPrompt(context?)
                         interpretPain?(error, ctx)
                         shouldReflect?(ctx)

メソッド数: 1            メソッド数: 3
引数: なし               引数: GuideContext
可視ステート: なし       可視ステート: 6つ以上のフィールド
開ループ／閉ループ: 開ループ 閉ループ（センサ入力を伴う）
```

ATHENA は WIENER を見た。

「わかるかしら？ `ClassifiedError` には `severity: number` という $[0, 1]$ の連続量フィールドがあるわ。これこそが、あなたの $e(k)$ をエンジニアリングとして落とし込んだ姿なの。抽象的な『タスク全体の達成度』を計算するのではなく、発生した具体的なエラーの深刻度を個別に分類するのよ」

彼女はいくつかの具体的なマッピングを、目盛りを刻むように列挙した：

```
ENOENT  (ファイル不在)     → severity: 0.4  (復旧可能)
EPERM   (権限拒否)         → severity: 0.7  (戦略変更が必要)
ENOMEM  (メモリ不足)       → severity: 0.9  (システム級の故障)
ETIMEOUT (ネットワーク超過) → severity: 0.3  (一時的、リトライ可能)
```

「完璧ではないけれど、量ることができ、デバッグができ、そして何より TypeScript で直接書くことができるわ」

ARCHIMEDES は傍聴席で顔を上げた。彼は聴きながら、それぞれの案を自身の工数見積もりへと変換していた。ATHENA の案は、彼のエンジニアとしての本能を刺激した。彼はノートに素早く概算を記した：

```
IGuide の拡張: 約 80 行のインターフェース変更
ClassifiedError: 約 40 行の新しい型定義
GuideContext の注入: 約 120 行の ExecutionLoop 修正
エラー分類器: 約 200 行の新規モジュール
------
見積もり合計: 約 440 行
見積もり工数: 2〜3 日 (単体テスト込み)
```

三本目の指を立てた。

「第三に。階層的な戦略は統一された公式に勝るわ。すべてのエラーを同じ PID コントローラで処理すべきではないのよ」

ATHENA は三つの分類フレームワークを描き出した。TURING は即座に、それが現在の SafetyMonitor の処理とどう異なっているかを確認した：

```
Type A: 論理エラー (Logic)
  例：引数エラー、パス不在、APIの契約不一致
  正しい対処：反省 (reflect) — 戦略を変える、リトライはしない
  SafetyMonitor の現状：一律に consecutiveFailures に計上

Type B: 一時的エラー (Transient)
  例：ネットワーク・タイムアウト、接続リセット、Rate Limit
  正しい対処：自動リトライ ＋ 指数バックオフ
  SafetyMonitor の現状：一律に consecutiveFailures に計上

Type C: 致命的エラー (Fatal)
  例：メモリ不足、システムクラッシュ、恒久的な権限拒否
  正しい対処：即時中止 ＋ 人間の介入を要請
  SafetyMonitor の現状：一律に consecutiveFailures に計上
```

「性質の異なる三種類のエラーを一つの PID 公式に押し込めるのは、統一性という優雅さで問題の異質さを覆い隠しているだけよ」

彼女は着席した。座る瞬間に、最後の一撃を加えた。

「動くのかしら？ 動くところを見せてくれたら、信じてあげるわ」

傍聴席では、DARWIN が小さく頷いていた。彼はノートに一行記した。「ATHENA が私の言いたいことを代弁してくれた。DX（開発者体験）が第一だ。数学公式がいかに美しくとも、プラグイン開発者が使い道に迷うようでは画餅に過ぎない」。彼は進化論的な思考で付け加えた。「選択圧は公式の優雅さにではなく、生態的な適応性にかかるものだ。最も多くの開発者に採用される案こそが、適者なのだ」

KERNEL は隣で低く評した。「彼女の IGuide 拡張は、実質的にマイクロカーネルに新しいシステムコールを追加するようなものだ。痛覚はコア固有のロジックであるべきではなく、標準化されたインターフェースを通じてユーザ空間に公開されるべきものなのだ」。彼はノートに類比を描いた：

```
Linux カーネル                    OpenStarry コア
──────────────                  ──────────────
/proc/stat (CPU統計)            GuideContext.consecutiveErrors
/proc/meminfo (メモリ統計)      GuideContext.currentRound
sysfs (デバイス状態)            GuideContext.activeTools
ioctl() (デバイス制御)          IGuide.interpretPain()
```

「ATHENA の案は、OpenStarry における `/proc` ファイルシステムを構築することだ。コアの内部状態をプラグインにさらしつつ、コア自体の制御ロジックは変えないというわけだな」

---

### NAGARJUNA の陳述：四聖諦というメス

NAGARJUNA が立ち上がった。三角形の三番目の頂点に、彼の長い影が落ちた。最初の討論で、彼は「空性」というメスを用いて Agent Core の存在論を解剖した。今度は道具を替えなければならない。より鈍い刃に替えるのではない。異なる次元を切り裂く刃に替えるのだ。

彼が口を開くと、その声には尋常ではない落ち着きが宿っていた。最初の討論の時のような弁証的な鋭さではなく、より深く、ほとんど慈悲深いとも言えるような質感であった。それは、医師が患者に対し、問題は症状の処置にあるのではなく病そのものの理解にあるのだと説き始めるかのようであった。

「WIENER 殿は、いかにして痛みを精密に量るかを語った。ATHENA 殿は、いかにして痛みをエンジニアリングとして処理するかを語った」

彼は一呼吸置いた。

「私は問いたい。痛みの本質とは、一体何なのか？」

傍聴席の空気が、微妙に変化した。BABBAGE のペンが止まった。KERNEL が顔を上げた。最初の討論の疲弊からようやく回復した ASANGA も、わずかに身を乗り出した。その瞳に、警戒の光が走った。彼は NAGARJUNA が今行おうとしていることに気づいたのだ。すなわち、議論の抽象化レベルを、WIENER や ATHENA の道具箱では到底届かない高みへと引き上げようとしていることに。

NAGARJUNA は言った。「釈尊が二千五百年前、鹿野苑（ろくやおん）において初めて法を説かれた際、最初に宣言された教義は空性ではなかった。縁起でも、中道でもなかったのだ」

彼の声に、歴史の重みが宿った。

「それは『苦（く）』であった。*Dukkha*（दुःख）だ」

彼は三者を見渡し、学者の精緻さをもってその概念の語源を紐解いた。

「*Dukkha* の語源を巡る論争は二千年続いている。一つは *dur*（悪い、困難な）＋ *kha*（空間、車輪の軸穴）から来ているという説だ。原意は『軸穴の歪んだ車輪』 ―― 永久にガタつく車だ。もう一つは *dus*（困難な）＋ *stha*（立つ）から来ているという説で、『立ちがたい状態』 ―― 不安定、不安、不満足を意味する。『雑阿含経（サンユッタ・ニカーヤ）』において、釈尊が一人称で語られた最初の経文はこうだ：」

> 「これ苦聖諦（くしょうたい）なり ―― 生は苦なり、老は苦なり、病は苦なり、死は苦なり、怨憎会苦（おんぞうえく）、愛別離苦（あいべつりく）、求不得苦（ぐふとくく）、略して説かば五取蘊苦（ごしゅうんく）なり」
> ――『転法輪経』（*Dhammacakkappavattana Sutta*, SN 56.11）

「四聖諦（ししょうたい） ―― *Catvāry āryasatyāni*（चत्वार्य् आर्यसत्याニ） ―― 苦（く）、集（じゅう）、滅（めつ）、道（どう）。これこそが仏教の全教義体系の礎石となる構造なのだ。しかし OpenStarry の痛覚メカニズムも、そして先ほど諸君が提示したすべての改善案も、四聖諦の第一諦の、そのまた第一層にしか触れていない」

BABBAGE はノートに四聖諦を四つ組（タプル）として形式化した：

$$	ext{FourNobleTruths} = (	ext{Dukkha}, 	ext{Samudaya}, 	ext{Nirodha}, 	ext{Magga})$$

彼は横に、ソフトウェア工学とのマッピングの試みを記した：

$$	ext{苦 (Dukkha)} \leftrightarrow 	ext{エラー検知}$$
$$	ext{集 (Samudaya)} \leftrightarrow 	ext{根本原因分析 (RCA)}$$
$$	ext{滅 (Nirodha)} \leftrightarrow 	ext{エラーの消解 (検証された修正)}$$
$$	ext{道 (Magga)} \leftrightarrow 	ext{プロセスの改善 (メソドロジー)}$$

彼はさらに一行書き添えた。「もしこのマッピングが成立するなら、現在の SafetyMonitor は苦（エラーの存在の検知）しか実装していないことになる。集（なぜエラーが起きたかの分析）、滅（エラーが解消されたことの確認）、そして道（再発防止のためのプロセス改善）が完全に欠落しているのだ」

NAGARJUNA は手を挙げ、苦諦（くたい）の三つの階層を一つずつ展開していった。これは彼が R1 報告書ですでに構築していたフレームワークであったが、今、討論の場において、それを鋭利な武器へと鍛え直そうとしていた。

「苦諦には三つの層がある。第一層は、*苦苦（くく）* ―― *dukkha-dukkha*（दुःख दुःख） ―― 直接的で、先鋭的な苦しみだ」

彼は TURING のモニターを指差し、`afterToolExecution` の `isError` パラメータを指し示した。

「ツールの実行失敗、権限の拒否、接続のタイムアウト。`isError = true`。これこそが、諸君が議論している階層だ。WIENER 殿はそれを PID で量ろうとし、ATHENA 殿はそれを ClassifiedError で分類しようとしている。どちらも正しい。だが、それは最も表面的な一層に過ぎないのだ」

二本目の指を立てた。

「第二層は、*壊苦（えく）* ―― *vipariṇāma-dukkha*（विपरिणाम दुःख） ―― 変異によって生じる苦しみだ。かつて成功していた戦略が、突如として無効になる。API の仕様が変わる。対話の途中でユーザの要求が変化する」

彼は WIENER の制御ブロック線図に視線を向けた。

「これは一回ごとのツール呼び出しの失敗ではない ―― 戦略の基盤そのものの崩壊なのだ。君の PID コントローラは、この苦しみを検知できるかね？」

彼は一呼吸置き、PID が壊苦を前にしていかに無力であるかを、数学の言語を用いて精密に描写した。

「君の微分項 $D(k) = e(k) - e(k-1)$ が捉えるのは、誤差の変化率だ。しかし壊苦とは、誤差が連続的に増大することではない ―― 誤差を計算するためのフレームワークそのものが、突如として無効化されることなのだ。制御理論の言葉で言えば、壊苦とは $e(k)$ の増大ではなく、$r(k)$ ―― すなわち目標入力そのものの突変（ステップ変化）なのだ。君のコントローラは $e = r - y$ を追跡しているが、もし $r$ が $t = t_0$ においてステップ状に跳ね上がったとしたら ―― 」

BABBAGE はノートにこの数学的な状況を描いた：

$$r(k) = \begin{cases} r_1 & k < k_0 \ r_2 & k \geq k_0 \end{cases}, \quad r_2 
eq r_1$$

「 ―― そのとき、$e(k)$ の微分項は $k = k_0$ の瞬間に一つのパルスを生じさせるだけで、その後は定常状態へと戻ってしまう。PID コントローラは目標入力のステップ変化を、単なる一時的な偏差の増大としてしか扱わない。しかし壊苦の本質は偏差の増大ではなく、目標の変容なのだ。コントローラに必要とされているのは、より強い修正力ではなく、目標設定値（セットポイント）そのものの再校正（リキャリブレーション）なのだよ」

WIENER の眉がわずかに動いた。SCRIBE はそれを見逃さなかった ―― それは討論を通じて、WIENER が初めて急所を突かれたときに見せた表情であった。

三本目の指を立てた。

「第三層は、*行苦（ぎょうく）* ―― *saṃskāra-dukkha*（संस्कार दुःख） ―― 条件性そのものから生じる苦しみだ。システムが外部の LLM、外部のツール、外部の環境に依存する条件的な存在である以上、その本質は不安定なのだ。特定の失敗ではない、特定の戦略の崩壊でもない。システムが存在するその様態そのものが、苦しみの種子を孕んでいるということだ」

彼は WIENER を見た。「これは、君自身が R1 報告書の『発見 F1』で指摘した根本的な問題に対応している ―― すなわち、LLM コントローラは本質的な不確実性を備えており、システムダイナミクス $f$ は未知であり、確率的な有界性しか議論できないという問題だ」

NAGARJUNA の声は半オクターブ低くなり、ほとんど優しくさえある厳格さを纏った。

「これは修正可能な欠陥ではない。これは *saṃskāra-dukkha* なのだ」

BABBAGE はペンを置いた。彼は三苦の横に、制御理論による形式的な対照を書き記した：

$$	ext{苦苦} \leftrightarrow 	ext{観測ノイズ (measurement noise)}: \quad y(k) = y^*(k) + n(k)$$
$$	ext{壊苦} \leftrightarrow 	ext{目標入力の跳躍 (reference step)}: \quad r(k) 	o r'(k)$$
$$	ext{行苦} \leftrightarrow 	ext{システムの不確実性 (plant uncertainty)}: \quad f 	ext{ は未知}$$

彼は横に注釈した。「NAGARJUNA 殿の言う三苦は、制御理論における三つの異なる不確実性の源泉に正確に対応している。第一のものはフィルタによって処理可能であり、第二のものは適応制御を必要とする。そして第三のものは根本的なものであり、排除することはできず、ただ制約することしかできないものだ」

NAGARJUNA はさらに深い次元 ―― 集・滅・道へと切り込んでいった。その語る速度は非常に遅く、一語一語が吟味されていた。

「しかし、たとえ苦諦（くたい）の三層の深化を極めたとしても、もし苦諦に留まるのであれば、四聖諦はいまだ不完全なままだ」

「第二諦。集諦（じったい）。*Samudaya-satya*（समुदय सत्य）。苦しみの原因だ。なぜ痛むのか？」

彼は WIENER を見た。「君のコントローラは、痛みの強度を量る」 次に ATHENA を見た。「君の分類器は、痛みのタイプを特定する。しかし諸君は誰も問うてはいない。なぜこのツールが、今この瞬間に、このような形で失敗したのか、ということを。根本原因（ルートコーズ）は何だ？ エージェントがツールを選択し間違えたのか？ コンテキストの中に決定的な情報が欠けていたのか？ あるいは、ユーザの指示そのものが曖昧だったのか？」

彼の語調に、妥協を許さぬ響きが加わった。

「集諦を欠いた痛覚システムは、体温だけを量って診断を下さない病院のようなものだ。病人が熱を出していることはわかる。その体温を小数点以下二桁まで正確に量ることもできるだろう。だが、なぜ熱が出ているのかはわからないのだ」

「第三諦。滅諦（めったい）。*Nirodha-satya*（निरोध सत्य）。苦しみの止滅だ。同一の類のエラーが、次第に排除されつつあるか？ 一度犯した過ちを、回避することを学んだか？」

「第四諦。道諦（どうたい）。*Mārga-satya*（मार्ग सत्य）。止滅へと至る道だ。八正道（はっしょうどう） ―― *Āryāṣṭāṅgika-mārga* ―― 正見、正思惟、正語、正業、正命、正精進、正念、正定」

NAGARJUNA はここで、BABBAGE が後に「認識論的な次元削減」と呼ぶことになる論証を展開した。すなわち、八正道を宗教的な教条から、ソフトウェア工学における八つの改善次元へと転換してみせたのである：

| 八正道 | サンスクリット | エージェント工学へのマッピング |
|--------|--------------|------------------------------|
| 正見 | *Samyag-dṛṣṭi* | タスク目標の正しい理解 (曖昧さの解消) |
| 正思惟 | *Samyak-saṃkalpa* | 合理的なサブタスクの分解 (プランニング) |
| 正語 | *Samyag-vāc* | 精確なプロンプト表現 (プロンプト・エンジニアリング) |
| 正業 | *Samyak-karmānta* | 適切なツールの選択 (ツール・セレクション) |
| 正命 | *Samyag-ājīva* | 合理的なリソース配分 (トークン予算管理) |
| 正精進 | *Samyag-vyāyāma* | 適切なリトライ戦略 (リトライ・ポリシー) |
| 正念 | *Samyak-smṛti* | コンテキスト内の重要情報の維持 (コンテキスト管理) |
| 正定 | *Samyak-samādhi* | 現在の最優先サブタスクへの集中 (フォーカス) |

傍聴席の LINNAEUS はこの表を眺め、瞳を微かに輝かせた。それは分類学者が最も好むもの ―― 重複のない、完備された分類体系であった。彼は自身のノートで、即座にこの表の分類学的性質を検証した：

```
排他性 (Mutual Exclusivity):
  正見 ≠ 正思惟 ≠ 正語 ≠ ... (8つの次元は互いに重複しない)  ✓ 合格

網羅性 (Exhaustiveness):
  あらゆる改善の方向性は、この8つの次元でカバーされているか？
  反例：「他のエージェントとの協調の改善」 → どの項目に属するか不明確  ？
  結論：シングルエージェント・シナリオにおいては近似的に完備。
        マルチエージェント・シナリオにおいては拡張を要する  △ 保留
```

NAGARJUNA は陳述を締めくくり、最後にこう言った。

「諸君は、いかにして痛みをより良く感じるかを論じている。私が説いているのは、痛みを感じることは出発点に過ぎないということだ。痛みの原因を理解し、その原因を断ち、痛みのない状態へと至る完全な道筋を築くこと ―― それこそが、真に完備された痛覚システムなのだ」

会場に、丸三秒間の静寂が訪れた。

SCRIBE は記録簿に素早く書き留めた：

> *三者の冒頭陳述は、三つの全く異なる抽象化レイヤーで展開された。WIENER は数学レイヤー（精密な定量化）、ATHENA はエンジニアリング・レイヤー（実装の可能性）、NAGARJUNA は認識論レイヤー（フレームワークの完備性）である。三人はそれぞれの山頂に立ち、互いの姿を視認してはいるが、その間には深い谷が横たわっている。これからのクロス質疑が、彼らが谷の中に共通の道を見出せるかどうかを決定づけることになるだろう。*

---

### クロス質疑

SUNYATA が宣言した。「冒頭陳述を終了する。これよりクロス質疑に入る。ルールはこうだ。各討論者は他方のいずれかに対し、核心を突く質疑を一つ投げかけることができる。問われた側には反撃の権利がある」

彼は一呼吸置き、付け加えた。「三者討論の複雑さを鑑み、質疑の順序は私が適宜誘導させてもらう」

彼は ATHENA の方を見た。「ATHENA 殿から WIENER 殿へ」

---

#### 第一回戦：ATHENA → WIENER

ATHENA は立ち上がらなかった。背もたれに身を預け、腕を組み、WIENER を真っ直ぐに見据えた。その眼差しは、技術レビューの場でアーキテクトを問い詰めるエンジニアリング・マネージャのそれであった。

「WIENER 殿、冒頭でも一度聞いたけれど、改めて正式に質疑させてもらうわ。あなたの $e(k)$ とやらは、一体どうやって量るつもり？」

彼女は畳み掛け、息をつく暇を与えなかった。

「LLM は線形システムじゃない。あなたの化工厂のリアクターとは違うのよ。出力は確率的だわ ―― temperature（温度パラメータ）がゼロより大きければ、同じ入力に対しても全く異なる出力が返ってくる。あなたの PID コントローラは、決定論的なフィードバックを前提としている。でもここには決定論なんて存在しないの。あなたの積分項 $I(k)$ が、信号（シグナル）ではなくノイズを累積し続けないという保証がどこにあるのかしら？」

傍聴席の GUARDIAN が、セキュリティ分析を添えた。彼は STRIDE 脅威モデルの言語を用いて ATHENA の疑問を再定義した：

```
STRIDE 分析：PID 誤差信号の脅威面
──────────────────────────────────
S (Spoofing):    LLM がプロンプト・インジェクションにより操縦され、
                 虚偽の低い e(k) を報告するリスク
T (Tampering):   ツールの出力が改ざんされ、e(k) の計算に偏差が生じるリスク
R (Repudiation): e(k) の計算プロセスに監査証跡が欠落するリスク
I (Info Disc.):  e(k) の値からタスクの進捗状況という機密情報が漏洩するリスク
D (DoS):         攻撃者が e(k)=0 を操作し、コントローラを麻痺させるリスク
E (Elevation):   偽の e(k)=1 を注入し、PID の最大出力による過剰な修正を誘発するリスク
```

「もし $e(k)$ の観測そのものが信頼できないのであれば、」 GUARDIAN は KERNEL に低く囁いた。「PID コントローラは信頼できないセンサの上に閉ループを築いていることになる。安全工学で言うところの、GIGO（garbage in, garbage out）の閉ループ・バージョンだ。単なる『ゴミを入れればゴミが出る』ではなく、ゴミを入れ、増幅し、フィードバックし、さらに増幅する。破滅への正フィードバック・ループだよ」

WIENER はわずかに身を乗り出した。彼は即座には反論しなかった ―― まず目を閉じ、ATHENA の疑念を自身の頭の中で制御理論の用語へと翻訳しているようだった。それから目を開けると、その声には落ち着きの中に退かぬ決意が宿っていた。

「君の懸念は、現実に存在する問題を指し示している。だが、結論が悲観に過ぎるな」

彼は図面を裏返し、その裏に新しい図を描き始めた。

「まず、 $e(k)$ は必ずしも『タスク全体の達成度』として定義される必要はない。君自身が提案した ClassifiedError には severity フィールドがあった。$[0, 1]$ の連続量だ。それが $e(k)$ の、実用的な代理測定値（プロキシ）となる。完璧ではないが、PID ループを始動させるには十分だ」

彼の語調は数学の講義モードへと切り替わった。

「次に、LLM の確率性は PID で扱えないものではない。産業界には MRAC ―― Model Reference Adaptive Control（規範モデル適応制御）という成熟したフレームワークがあるのだ」

BABBAGE はノートに MRAC の形式的定義を記した：

$$	ext{MRAC}: \quad \dot{	heta}(t) = -\Gamma \cdot \phi(t) \cdot e_m(t)$$

ここで $	heta$ は適応パラメータ・ベクトル、$\Gamma$ は適応ゲイン行列（正定）、$\phi$ は回帰ベクトル、$e_m = y - y_m$ は実際の出力と規範モデルの出力の偏差である。彼は横に注釈した。「MRAC の核心的な思想は、制御対象の精密なモデルを必要としない点にある。単に『規範モデル（リファレンス・モデル）』 ―― すなわち理想的なエージェントがいかに振る舞うべきかさえ分かっていれば、実際の挙動をそこへ近づけるようにコントローラのパラメータを適応的に調整できるのだ」

WIENER は続けた。「認めるよ。 $e(k)$ は必ずしも精緻である必要はない。単調（monotonic）であればそれでいいのだ。すなわち、システムが改善していれば $e(k)$ が減少し、改悪していれば増加するという傾向さえ捉えていればいい」

彼は数学的な定理を引いてこの論点を補強した：

$$	ext{単調性の条件}: \quad e^*(k_1) > e^*(k_2) \implies \hat{e}(k_1) > \hat{e}(k_2) \quad (	ext{少なくとも確率 } p > 0.5 	ext{ で})$$

「 $e^*$ が真の偏差、 $\hat{e}$ が観測された偏差だ。観測値の順序が真の偏差の順序と一致してさえいれば ―― たとえ絶対値がデタラメであっても ―― PID コントローラはシステムを正しい方向へと駆動し続けることができる。化工厂の温度センサにも観測ノイズはあるが、PID はそれでも機能しているのだよ」

そして、彼は反撃に転じた。語調が突如として鋭くなった。

「しかし ATHENA 殿、逆に君に問いたい。君の IGuide 拡張案は信号経路の問題を解決した。Guide がシステムの内部状態を見ることができるようになった。それはいい。だが、君はその問題を『誰』に押し付けたかね？ プラグイン開発者だ」

彼は ATHENA が先ほど提示したコードを指差した。

「君の `interpretPain` メソッドは、ClassifiedError をいかにして LLM への引導命令（プロンプト）に変換するかを、Guide プラグインの開発者の裁量に委ねている。開発者 A は過敏な Guide を書き、軽微なファイル不在に対しても悲鳴を上げるかもしれない。開発者 B は鈍感な Guide を書き、致命的な権限拒否にも無反応かもしれない」

BABBAGE はノートに、WIENER の批判を形式化した：

$$	ext{問題}: \quad g_A: 	ext{ClassifiedError} 	o 	ext{String} 
eq g_B: 	ext{ClassifiedError} 	o 	ext{String}$$

$$	ext{同一の入力}: \quad 	ext{error} = (	ext{EPERM}, 0.7)$$
$$	ext{異なる出力}: \quad g_A(	ext{error}) = 	ext{"直ちに停止せよ"} \quad vs. \quad g_B(	ext{error}) = 	ext{"別の方法を試して"}$$

「関数 $g$ に対する一致性の制約が存在しない」。BABBAGE は横に記した。「PID の $K_p, K_i, K_d$ は、少なくともグローバルなゲイン（増益）のベースラインを提供してくれる。$pain(k)$ はすべての Guide に対して同一だからだ。ATHENA 殿の案は、ゲイン調整の責任を完全に外部へ丸投げしてしまっている」

WIENER は締めくくった。「君の案には、フィードバック強度を調整するための共通の基準が欠けている。そして PID の $K_p, K_i, K_d$ こそが、まさにその基準を提供するのだ」

ATHENA の口元が微かに動いた。彼女は即座には言い返さなかった ―― 彼女のスタイルからすれば、これは珍しいことだった。SCRIBE は後に記録の中で、ATHENA が応答を組み立てるのに二秒以上を要したのは、この討論全体を通じてこの時だけだったと記している。

「一理あるわね、」 彼女はようやく認めた。その声には、不承不承ながらも誠実な承認が滲んでいた。「私の案には、ゲイン調整のメカニズムが欠けている。でも、だからといって PID だけが唯一の答えだというわけじゃないわ」

彼女はその反論をそれ以上は展開しなかった。手の内を、あえて一つ残したのだ。

傍聴席では、KERNEL がノートに一行記していた。「WIENER の反撃は急所を突いている。ATHENA の案はインフラであって、戦略ではないのだ。プラグイン開発者にドライバーを渡すことはできるが、全員がどのネジを締めるべきかを知っているとは限らない」

MESH が隣から分散システムの視点を添えた。「マイクロサービス・アーキテクチャで言えば、これはコントロールプレーンとデータプレーンの分離だな。ATHENA はデータプレーン（信号伝達）を作り、WIENER はコントロールプレーン（戦略決定）を作ろうとしている。両方が必要なんだ」

---

#### 第二回戦：WIENER → NAGARJUNA

SUNYATA：「WIENER 殿から NAGARJUNA 殿へ」

WIENER は NAGARJUNA の方を見た。その瞳には、ある奇妙な表情が浮かんでいた ―― それは敵意でも軽蔑でもなく、精密科学者が、尊敬はしているが完全には理解しがたい領域に直面したときに見せる、慎重な眼差しであった。

「NAGARJUNA 殿、君の四聖諦のフレームワークは、認識論として実に魅力的だ」 彼の言葉には実感がこもっていた。「三層の苦、集諦による原因分析、滅諦による止滅の追跡、道諦による八つの改善次元。思考の枠組みとして、その価値は私にもわかる」

それから、彼の声が引き締まった。さながら一本の弦が、ギリギリと巻き上げられていくかのように。

「しかしだ。君の集諦（じったい） ―― 根本原因分析には、私にはどうしても看過できない問題があるのだ」

彼の話す速度が落ち、一語一語が重みを増した。

「君は、過ちを犯したエージェント自身に、なぜ過ちを犯したかの原因を分析させようとしている」

会場の温度が、一段階下がったかのように感じられた。

「これは自己参照のパラドックスだ。もしエージェントの認知能力が、なぜ失敗したかを正しく分析できるほど高いのであれば、その能力によって最初から失敗を避けることができたはずだ。もし認知能力が失敗を避けるに足りないものであるなら、どうしてその同じ認知能力が、失敗の原因を正しく診断できると信じられるのだね？」

BABBAGE はこの論証に、さながら感電したかのような衝撃を受けた。彼は他の書き込みを一切止め、最も整った筆致でこのパラドックスを形式化した：

$$	ext{令 } C 	ext{ をエージェントの認知能力集合とする}$$

$$	ext{令 } 	ext{diagnose}(e) 	ext{ をエラー } e 	ext{ の根本原因を正しく診断する能力とする}$$

$$	ext{令 } 	ext{avoid}(e) 	ext{ をエラー } e 	ext{ を回避する能力とする}$$

$$	ext{WIENER の論証}: \quad 	ext{diagnose}(e) \in C \implies 	ext{avoid}(e) \in C$$

$$	ext{対偶命題}: \quad 	ext{avoid}(e) 
otin C \implies 	ext{diagnose}(e) 
otin C$$

彼は横に注釈した。「これはゲーデルの不完備性定理と構造的な同型をなしている。一つのシステムは、そのシステム内部において自身の限界を完全に理解することはできない。エージェントを一形式体系と見なすなら、WIENER 殿の疑念は本質的にこう言っているのだ。すなわち、エージェントの自己診断能力は、エージェント自身の推論能力によって制約される。そして、その推論能力こそがエラーを引き起こした当のものなのだ、と」

彼はページの下部にさらに一行加えた。「しかし NAGARJUNA 殿の仏教的な修練には、ゲーデルの定理さえ及ばない応答があるかもしれない。仏教は『体系を超えた観察』を許容するからだ。彼の言葉を待とう」

WIENER は NAGARJUNA を直視した。

「君の集諦 Root Cause Analyzer は、制御理論の言葉で言えば『自己引用型の観測器』だ。観測されるシステムと観測器が同一のシステムなのだよ。制御理論において、これは通常、不可観測性の問題を引き起こす。君はこの問題を、どう解決するつもりかね？」

NAGARJUNA は目を閉じた。それは質問を回避しているのではない ―― SCRIBE は彼の呼吸のリズムが変化したことに気づいた。それは、束の間の瞑想状態に入った修行者のそれであった。

三秒後、彼は目を開けた。その応答は全員の予想を裏切るものであった ―― 哲学的な弁駁ではなく、仏教修行における実践的な概念であった。

「*Vipassanā*（ヴィパッサナー）」 と彼は言った。

一言。観照（かんしょう）。

そして彼はそれを展開した ―― まずパーリ語による厳密な定義を示し、それをエンジニアリングの言語へと転換した。

「*Vipassanā* は *vi-*（特殊な、貫通する）＋ *passanā*（見る）に由来し、『ありのままに観る』ことを意味する。南伝仏教（テーラワーダ）の修行伝統において、観照は四念処（しねんじょ、*Satipaṭṭhāna*）の核心的な手法である。修行者は自身の身体（身念処）、感受（受念処）、心（心念処）、法（法念処）を観察する ―― しかし、観察する主体は、観察される客体と等置されることはない」

> 「比丘たちよ。比丘はいかにして身において身を観じて住むのか。比丘は歩むとき、『私は歩んでいる』と了知し、立つとき、『私は立っている』と了知し、坐るとき、『私は坐っている』と了知し、臥すとき、『私は臥している』と了知する」
> ――『大念処経』（*Mahāsatipaṭṭhāna Sutta*, DN 22）

「君の疑念は、一つの前提を置いている。すなわち、分析する者と分析される者は、同一の認知実体でなければならない、という前提だ。しかし仏教の観照の伝統は、別の可能性を提示しているのだよ」

NAGARJUNA はこの概念をエンジニアリングの言語へと翻訳した。語る速度は非常に遅く、一語一語が吟味されていた。

「観照とは、思考ではない。分析でも、推論でもない。それは、思考のプロセスそのものを、より高い抽象化レベルから観察する能力なのだ。君が自身の怒りを観察するとき、観察者と怒りは同一の物ではない。観察者は怒りの一段高い場所に立ち、それが生じ、維持され、消滅していく様を眺めているのだ」

彼はこの概念を、システム・アーキテクチャへと精密にマッピングした。

「システム・アーキテクチャにおいて、これは Root Cause Analyzer が LLM の主認知フローの一部であってはならないことを意味する。それは主制御ループの外側で稼働する独立したモジュールであるべきだ。独立した LLM 呼び出しを用いて、主ループの挙動パターンを分析するのだ。観察される側と観察する側は、同一の認知プロセスを共有しない」

BABBAGE はノートに即座にこのアーキテクチャを形式化した：

```
主ループ (観測されるシステム):
  LLM_main: Context → ToolCalls → Results → Context' → ...

観測器 (Root Cause Analyzer):
  LLM_observer: {error_log, context_snapshot, tool_history} → RootCause

決定的な制約条件:
  LLM_main ∩ LLM_observer = ∅  (推論プロセスを共有しない)
  あるいは少なくとも： prompt_main ∩ prompt_observer = ∅  (プロンプト空間を共有しない)
```

彼は横に注釈した。「これは自己参照のパラドックスを解消している。同一のシステムが自分自身を分析するのではなく、独立した観測システムが主システムを分析するのだから。制御理論において、これはリュエンバーガー観測器と呼ばれる。制御対象システムの状態を推定するための、独立した動的システムだ。NAGARJUNA 殿の Vipassanā 観測器とリュエンバーガー観測器は、構造的に同型（アイソモーフィック）である」

NAGARJUNA は WIENER を見た。その瞳には、穏やかな挑戦の光が宿っていた。

「唯識学において、この執着から観照への転換は『転依（てんえ、*āśraya-parāvṛtti*）』 ―― すなわち転識得智（てんじきとくち）と呼ばれる。第六意識による分別の判断が、妙観察智（みょうかんさつち）による無執着の観照へと転じるのだ。君の説く自己参照のパラドックスは、システムに認知の階層が一つしかないことを前提としている。だが仏教は説く。否、少なくとも二つはあるのだ、と。一つは過ちを犯す階層であり、もう一つはその過ちを観察する階層なのだ」

そして、彼は反撃に転じた。語調が突如として鋭くなった。

「しかし WIENER 殿、逆に君を質そう。君の制御理論的なフレームワークには、より根本的な欠陥がある。技術的なレベルではなく、認識論的なレベルにおいてだ」

彼の声が低くなった。決定的な判定を告げようとするかのように。

「君のフレームワーク全体 ―― 苦とは誤差信号 $e$ であり、コントローラの目標は $e$ を最小化することであるという考えは、苦の本質が『目標からの逸脱』であるという前提に立っている。しかしこのフレームワークには、二つの次元が欠落しているのだ。第一に集諦（じったい）だ。なぜ逸脱が生じるのかを問うていない。第二に、より根本的なことだが、滅諦（めったい）と道諦（どうたい）だ。逸脱を生じさせるメカニズムそのものをいかにして根絶するかを問わず、ただ起きた逸脱に対して、事後的に、受動的に反応し続けているに過ぎないのだ」

彼の声には、予言的な明晰さが漂っていた。

「君の制御システムは、永遠に $e 	o 0$ を追い求め続けるだろう。しかし、そのシステムが問うことは決してない。 $e$ を生じさせているメカニズムそのものを消滅させることは可能か？ システムが、単に受動的にエラーを修正するのではなく、能動的にエラーのパターンそのものを回避することを学ぶことは可能か？ ―― とね」

WIENER は即座には答えなかった。その沈黙は、先ほどの ATHENA のような応答を組織するための沈黙ではなかった。より深い、何かに打たれたような沈黙であった。SCRIBE は記録にこう記している。「WIENER 殿の表情は、自身の公理系に決定的な一条の公理が欠けていたことに突如として気づかされた数学者のようであった」

---

#### 第三回戦：NAGARJUNA → ATHENA

SUNYATA：「NAGARJUNA 殿から ATHENA 殿へ」

NAGARJUNA は ATHENA の方を見た。その眼差しには、奇妙な混合が宿っていた。彼女のエンジニアとしての直感を尊重しつつも、その盲点を突こうとする、ある種の冷徹さであった。

「ATHENA 殿、君の GuideContext インターフェースには、いくつかのフィールドが並んでいる」 彼の語調は分析的だった。「`consecutiveErrors`, `currentRound`, `maxRounds`, `activeTools`, `lastError`」

彼は一呼吸置いた。

「これらはすべて、現在のターンのデータだ。君の GuideContext には、記憶はあるのかね？」

ATHENA は眉を寄せた。罠の匂いを感じ取ったかのように。

NAGARJUNA は展開した。仏教における「三世因果（さんぜいんが、*trikāla-karma*）」の教えを用い、ATHENA の設計における盲点を精密に突いたのである：

「仏教の因果観において、いかなる出来事も孤立してはいない。それには前因（ぜんいん、*hetu*）――過去の業力（ごうりき）がある。現縁（げんえん、*pratyaya*）――現在の条件がある。そして後果（ごか、*phala*）――未来への影響がある。三世因果だ」

彼はその批判を、精密な技術的疑念へと集約させた。

「君の GuideContext にあるのは『現世（げんぜ）』 ―― 現在のターンの状態だけだ。『前世（ぜんぜ）』 ―― このエージェントが以前のセッションでどのような過ちを犯し、いかなる教訓を得たかという記録がない。また『来世（らいぜ）』 ―― 今回の経験が、未来の挙動にどう影響を及ぼすべきかという視点も欠けている」

BABBAGE はノートに、NAGARJUNA の三世因果をデータフローの時間次元へとマッピングした：

$$	ext{GuideContext}_{	ext{current}} = f(s_k) \quad 	ext{(現在の状態のみ)}$$

$$	ext{GuideContext}_{	ext{ideal}} = f(s_k, \{s_i\}_{i<k}, 	ext{prediction}(s_{k+1})) \quad 	ext{(三世の状態)}$$

「欠落している時間次元：」

```
前世 (過去のセッション):     previousTaskOutcomes?: TaskOutcome[]
                          knownFailurePatterns?: FailurePattern[]

現世 (現在のセッション):     consecutiveErrors: number       ← 実装済み
                          currentRound: number             ← 実装済み

来世 (未来のプランニング):   estimatedRemainingSteps?: number
                          riskAssessment?: RiskProfile
```

NAGARJUNA の結論は、哲学者の忍耐を湛えていた。

「三世因果を欠いた痛覚システムは、学習することのない痛覚システムだ。同じ過ちを何度も繰り返し、同じ痛みを何度も感じ続ける。なぜなら、自分がかつて痛んだことを、決して覚えてはいないからだ」

傍聴席の HERACLITUS が低く呟いた。「ランタイム動態の言葉で言えば、これは stateless（状態を持たない）対 stateful（状態を持つ）の問題だな。ATHENA 殿の GuideContext はターン単位で stateless になっている。セッションを跨ぐ statefulness を実現するには永続化層が必要だが ―― TURING 殿が確認した通り、現在の StateManager は純粋なメモリ実装であり、永続化機能を持っていない。したがって NAGARJUNA 殿の批判はアーキテクチャ・レベルで正しい。三世因果を実現するには、現在は存在しないインフラを必要とするのだ」

ATHENA の反応は、予想外に早く、そして予想外に率直であった。

「あなたの言う通りだわ」

二言。飾り気はなかった。傍聴席から微かな驚きの声が漏れた。ATHENA がこれほど直接的に相手の批判を認めるのは、珍しいことであったからだ。

そして彼女は即座に修復モードへと入り、速度を上げた。

「拡張は簡単よ。GuideContext に三つのフィールドを加えればいいわ：」

```typescript
interface GuideContext {
  // ... 既存のフィールド ...
  // 前世：歴史的な試行記録
  recentAttempts: AttemptRecord[];
  // 前世：既知の失敗パターン
  knownFailurePatterns: FailurePattern[];
  // 来世：今回の経験から得られた教訓 (次回のセッションで利用)
  lessonsLearned: string[];
}
```

彼女は NAGARJUNA を一瞥した。「あなたの三世因果という批判は正しいわ。でも私の案の価値は、その拡張性にあるのよ ―― このインターフェースなら、三分もあれば歴史的な記憶を追加できるわ。翻って、あなたの四聖諦のフレームワークはどうかしら？ 集諦の根本原因分析器を、どうやって実装するつもり？ 道諦の八正道の改善パスは？ それらを実現するためには、それこそ膨大なインフラが必要になるはずよ」

そして彼女は反論に転じた。その声には、哲学的な枠組みに対するエンジニアとしての深い懐疑が滲んでいた。

「それに、一つ指摘しておきたいわ。あなたのフレームワークはあまりに『規定的（prescriptive）』すぎるのよ。システムがいかに考えるべきか、いかに改善すべきかを、あらかじめ細かく指定しようとしているわね。八正道や四聖諦 ―― これらは規範的な枠組みであり、あなたが神の視点からシステムに『正しい改善のあり方』を説いているに過ぎないの。でも AI エンジニアリングに必要なのは、規定的な規範ではなく、記述的（descriptive）なインフラなのよ。私はデータと信号経路を提供し、LLM 自身にどう改善すべきかを決定させる。あなたは完全な改善の教条を提供し、システムがそれに従うことを前提としているわ」

傍聴席の LEIBNIZ は小さく首を振った。彼はマルチエージェント・システムの言語で ATHENA の批判を再定義した。「BDI（Belief-Desire-Intention）アーキテクチャにおいて、ATHENA 殿が提供しているのは Belief（信念）を更新するためのパイプライン ―― すなわちエージェントがより多くの状態を感知できるようにする仕組みだ。対して NAGARJUNA 殿が提供しているのは Desire（欲求）と Intention（意図）の規範 ―― エージェントが何を追求し、いかに行動すべきかを教える仕組みだ。両者は矛盾しないが、ATHENA 殿のパイプラインの方が、NAGARJUNA 殿の規範よりも先に実用化しやすいのは確かだな」

NAGARJUNA の口元に、微かな笑みが浮かんだ。それは急所を突かれたことへの困惑ではなく、自身の意図が正しく理解されたことへの満足であった。

「左様 ―― フレームワークの価値は方向性を示すことにあり、現行のアーキテクチャに縛られることではないのだ」 彼は穏やかに言った。「だが、方向性そのものに価値があるのだよ。方向性を欠いたインフラは、ただの管（くだ）に過ぎない。データが中を流れてはいても、それがどこへ向かっているのかは分からないのだからな」

---

#### 第四回戦：WIENER → ATHENA (補足質疑)

SUNYATA は新しい質疑のペアを宣言しなかった。ただ、自然な休止符において、静かにこう言った。「WIENER 殿、君は ATHENA 殿の開ループかつ非定量的なフィードバックについて、補足的な疑念を持っていたな」

WIENER は頷いた。彼は ATHENA の方へ向き直り、制御理論家特有の厳格さを纏った語調で切り出した。

「ATHENA 殿、君の案は Guide にシステムの内部状態を見せることを可能にした。それは閉ループ化への第一歩だ。しかし、閉ループとは単なる観測ではない。閉ループとは、観測し、制御量を計算し、制御アクションを実行することなのだ。君の案は観測こそ実現したが、制御量はどうなっているのかね？」

彼の声が鋭くなった。

「君の `interpretPain` メソッドは `string` ―― すなわちシステムプロンプトに注入されるテキストを返している。これは定性的で、意味論化された制御量であって、定量的なものではない。開発者 A の Guide は `severity=0.4` で『少し気をつけて』と注入するかもしれない。開発者 B の Guide は同じ深刻度で『直ちにすべての操作を停止し、助けを求めよ』と注入するかもしれない。二つの Guide は同じ信号を見ながら、全く異なる制御アクションを生成しているのだよ」

WIENER は R1 報告書で定義した言語を用いて、この問題を精密に記述した：

「制御理論の言葉で言えば ―― これは開ループ・ゲイン（増益）の不確定性だ。システムの挙動が Guide プラグイン開発者の個人的な判断に完全に依存してしまい、定量的なゲイン調整メカニズムが皆無なのだよ」

ATHENA は背もたれに身を預け、一秒ほど考えた。そして、傍聴席の数人が同時に眉を跳ね上げるような一言を放った。

「あなたが言うゲイン調整の問題 ―― それが伝統的な制御システムの話なら、私も同意するわ。でも、LLM エージェント・システムにおいては、LLM 自身がゲイン調整器なのよ」

彼女はこの論点を展開した。

「LLM は受動的なアクチュエータ（執行器）じゃないわ。システムプロンプトに書き込まれた痛覚の導きを読んだ後、LLM は自身の理解 ―― 文脈や履歴、現在のタスクをひっくるめた理解 ―― に基づいて、反応の強度を自律的に決定するの。同じ『少し気をつけて』という言葉でも、文脈が違えば、LLM の反応は劇的に変わるわ。これはバグじゃない。機能（フィーチャー）なのよ。LLM の意味理解能力そのものが、PID よりもはるかに豊かな『ゲイン調整』を提供しているのよ ―― LLM は文脈（コンテキスト）を理解するのだから」

BABBAGE はノートに、自分自身でも驚くような等式を書き記した：

$$	ext{LLM} = 	ext{文脈依存型のゲイン・スケジューラ}$$

「もし LLM が、文脈に応じて応答の強度を自動的に調整する能力を確かに備えているのであれば、ATHENA 殿の主張はある意味で正しい ―― LLM は外部のゲイン調整器を必要としない。なぜなら自身がそれそのものだからだ。しかしこれは、一つの検証不可能な仮定に依存している。すなわち、『LLM による文脈を意識したゲイン調整は、合理的で、安定的で、かつ単調である』という仮定だ」

彼女は一呼吸置き、自身も口に出した瞬間に初めて明確に意識したかのような洞察を述べた。

「答えは、三つの案のいずれかを選ぶことではなく、三つの層を重ね合わせることにあるのかもしれないわね。底層には私のインフラ ―― 信号経路、データ構造、インターフェース定義。中層にはあなたの PID ―― 定量化されたゲインのベースラインを提供し、Guide の出力が開発者の個人的な判断に完全に依存しないようにする。そして上層には龍樹殿の四聖諦 ―― 認識論的なフレームワークを提供し、痛覚メカニズムが単なる反応的なものに留まらず、根本原因分析や学習による回避を含む完全な道筋となるように。どうかしら？」

会場に、決定的なパズルのピースが正しい場所にはまったときのような静寂が訪れた。

---

#### 最終戦：NAGARJUNA → WIENER

SUNYATA は次の方向を指定しなかった。ただ NAGARJUNA を見やり、静かに頷いた。

NAGARJUNA は WIENER の方へと向き直った。

会場の空気が凝固したかのようだった。SCRIBE は後に記録の中で、NAGARJUNA が口を開く直前の一秒間、直感的に悟ったと記している。すなわち、これから起きることは、討論全体において ―― おそらくは Cycle 01 全体を通じて ―― 最も深遠な哲学的な瞬間になるだろう、と。

NAGARJUNA の声は、とても静かだった。低いのではなく、静かだったのだ ―― 重大なことを口にしようとする者が、自然と声を落とすかのように。

「WIENER 殿、」彼は言った。「君は R1 報告書の『学際的連結』の章で、実に興味深い対照表を記していたな」

彼はその表の構造を、穏やかだが精密に引用した：

| 制御理論 | 仏教 | OpenStarry |
|---------|------|-----------|
| 目標入力 $r$ | 涅槃 (理想の状態) | タスク目標 |
| 現在の出力 $y$ | 現世の苦しみ | 現在の進捗 |
| 誤差 $e = r - y$ | 苦 (Dukkha) | 痛覚信号 |
| コントローラ $C$ | 八正道 | LLM + Guide |
| 誤差の解消 | 離苦得楽 | タスク完了 |

「そして君は、その表の下に一段落の言葉を添えていた。君はこう書いた ―― 」

彼の語る速度は極めて遅くなり、一語一語の間に広大な空白が設けられた。

「『仏教が追求しているのは、苦と楽の二元性を超越することであり、偏差を最小化することではない。制御システムは永遠に $e 	o 0$ を追求し続けるが、仏教の究極の目標は、誤差という枠組みそのものを消解することにある』」

彼は顔を上げ、WIENER の瞳を真っ直ぐに見つめた。

「君は、自身でこの言葉を記した。だが、君はそれを展開しなかった。今、私が君に代わってそれを展開しよう」

場内は、全員の呼吸の音が聞こえるほどに静まり返っていた。

「君の制御システムは ―― PID であれ、MRAC であれ、いかなる適応制御であれ ―― 一つの根本的な前提の上に築かれている。すなわち、目標入力 $r$ が存在し、誤差 $e = r - y$ が存在し、システムの目標はその $e$ をゼロに近づけることである、という前提だ」

彼の声が、半オクターブ低くなった。

「仏教 ―― 少なくとも中観派は、全く異なる問いを投げかけるのだよ」

沈黙。丸二秒間の沈黙。傍聴席の誰もが、身動き一つしなかった。

「$e 	o 0$ ではない。そうではなく ―― $e$ を定義しているその枠組みそのものを、消解（しょうげ）することなのだ」

BABBAGE のペンが、完全に止まった。彼はノートの空白を見つめ、それからゆっくりと、後に何度も推敲することになる形式化の試みを書き記した：

$$	ext{制御理論}: \quad \min_u \sum_{k=0}^{\infty} \|e(k)\|^2 \quad 	ext{s.t. } e(k) = r(k) - y(k)$$

$$	ext{中観}: \quad (r, y, e) 	ext{ という三つ組そのものの存在論的な前提を消解する}$$

彼は横に、ゲーデル的な批注を添えた。「制御理論は、システム内部において目的関数を最小化する。中観は、システムの外部において目的関数の定義そのものを疑う。これは最適化の問題ではなく、メタ最適化の問題だ。$\min_u J(u)$ ではなく、目的関数 $J$ の定義そのものを問うことなのだ」

NAGARJUNA は続けた。

「君のフレームワークにおいて、システムには常に『目標』があり、常に『偏差』を計算し、常に『修正』を試みている。だが、ある種の状態 ―― 偏差がゼロである状態ではなく、もはや偏差を計算する必要さえない状態というものが、ありはしないかね？」

彼は WIENER 自身の言語を用い、正確に急所を射抜いた。

「制御理論の言葉で言えば、それは可到達性分析 ―― *reachability analysis* と呼ばれるものだ。君自身、報告書の中でこのオープン・クエスチョンを提示していたではないか。すなわち、『システムの定常偏差の根本原因は、コントローラの能力不足なのか、それとも目標そのものが到達不能（アンリーチアブル）であるからなのか？』という問い（Q2）だ。もし目標が到達不能であるなら ―― もし $r$ がシステムの可到達集合 $\mathcal{R}$ の外にあるならば ―― 」

$$r 
otin \mathcal{R}(x_0, \mathcal{U}) = \{x \mid \exists\, u(\cdot) \in \mathcal{U}: x(k) = x, 	ext{ for some } k\}$$

「 ―― そのとき、 $e 	o 0$ は、永遠に果たされることのない約束となる。到達不能な目標を追い求め続けることを、仏教ではこう呼ぶのだよ」

彼はその言葉を口にした。

「執着（しゅうじゃく）。*Upādāna*（उपादान）だ」

傍聴席の ASANGA は、微かに目を閉じた。*Upādāna* ―― 取（しゅ）、執取（しゅうしゅ）は、十二縁起（*Dvādaśa-nidāna*）の第九支である。無明 → 行 → 識 → 名色 → 六処 → 触 → 受 → 愛 → **取** → 有 → 生 → 老死。取とは、因果の連鎖において渇愛を存在（有）へと転換させる決定的な環である。NAGARJUNA が討論において唯識の概念を用いたこと ―― それは ASANGA にとって、微かな承認の印であった。

NAGARJUNA は質疑を締めくくった。

「だから私は問いたいのだ、WIENER 殿。君の制御理論のフレームワークの中に、『目標を手放す』ための場所は用意されているのかね？ 『もはや制御しない』という戦略に対応するメカニズムはあるのかね？ システムが ―― 『目標まであとどれくらいか』を問うのではなく、『この目標は、そもそも追求するに値するものなのか』を判断するための仕組みはあるのかね？」

会場の沈黙は、長く続いた。

WIENER の応答は、全員の予想を裏切るものであった。

彼は反論しなかった。

彼は俯き、膝の上にある、制御ループの図面で埋め尽くされた紙を見つめていた。それから顔を上げると、その声には率直な、ほとんど脆いとさえ言えるような承認が宿っていた。

「君は、制御理論には標準的な答えの存在しない問いを投げたな」

その声は安定していたが、普段よりはわずかに細かった。

「制御理論において、もし $r$ が可到達集合の外にあるなら、標準的なアプローチは $r$ を修正すること ―― すなわち目標を下げることだ。だが、君が問うているのは目標の修正ではない。そもそも『目標を持たねばならない』という枠組みそのものを消解することだ」

彼はしばし考え込み、それから言った。

「最も近い概念はメタ制御 ―― meta-control かもしれない。制御ループのさらに上の階層にある意思決定層だ。その役割は $e$ を最小化することではなく、『この制御ループを稼働させ続けるべきか否か』を判断することにある。だがメタ制御であっても、それは依然として一つの制御システムなのだよ。単に制御対象が下の階層の制御ループであり、目標が『正しい制御ループを選択すること』に置き換わったに過ぎないのだ」

BABBAGE はノートに再帰的な構造を描いた：

```
Meta-control:     min J_meta (制御ループの選択)
  ├── 制御ループ 1:  min J_1(e_1)  → タスクAのための PID
  ├── 制御ループ 2:  min J_2(e_2)  → タスクBのための PID
  └── 制御ループ ∅:  制御を停止する  → 「目標を手放す」
```

彼は横に注釈した。「メタ制御には依然として目標がある。すなわち、最適な子ループを選択することだ。『制御ループ ∅』を一つの正当な選択肢としてモデリングすることは可能だろう。だが NAGARJUNA 殿の問いはもっと過激だ。彼は『制御ループの集合の中に空の選択肢を加える』ことではなく、『制御ループの集合という概念そのものを消解すること』を問うているのだ。これは数学的には形式化不可能である ―― なぜなら、形式化という行為そのものが、一つの制御であるからだ」

WIENER は言葉を切り、誠実な承認を口にした。

「だが、君の言う『誤差という枠組みそのものを消解すること』 ―― 別の目標を選ぶのではなく、目標を追求すること自体を超越することについては、制御理論の中に、対応する概念を私は思いつくことができない」

彼は NAGARJUNA を見た。「それは、おそらく制御理論の境界なのだろう」

NAGARJUNA は小さく頷いた。その瞳には勝利者の傲慢さはなく、ただ、理解されたことへの静かな安らぎが湛えられていた。

傍聴席の DARWIN は深く息を吐き出した。彼は後に VITRUVIUS にこう語っている。「あの瞬間、NAGARJUNA 殿は討論をしていたんじゃない。制御理論がこれまで一度も答えようと考えたことすらなかった問いを、投げていたんだ」

---

### 転換：三層アーキテクチャの湧出

次に起きたことは、誰の予想もしていなかった展開であった。

ATHENA が沈黙を破った。彼女の語調はもはや討論者のそれではなく、不意に全体像を見通したエンジニアのそれであった。

「待って」 と彼女は言った。

全員が彼女に注目した。

「私たち三人、争っているわけじゃないわ」

彼女は立ち上がり、三角形の中心へと歩み寄った。その行動は、討論の空間的な文法を打ち破るものであった。彼女は自身の頂点を離れ、全員が共有する地帯へと足を踏み入れたのである。

BABBAGE はノートに、このトポロジーの変化の意味を記した：

$$K_3 = (\{W, A, N\}, \{(W,A), (A,N), (N,W)\}) \quad \xrightarrow{	ext{ATHENA が頂点を離れる}}$$

$$	ext{スターグラフ } S_3 = (\{W, A, N, C\}, \{(C,W), (C,A), (C,N)\})$$

「$C$ は中心点である。ATHENA は完全グラフ $K_3$ という対抗的なトポロジーを、スターグラフ $S_3$ という収束的なトポロジーへと変容させた。中心点は仲裁者ではない ―― 接続者なのだ」

「ずっと二人の話を聴いていたの」 ATHENA は WIENER を見、次に NAGARJUNA を見た。「WIENER 殿は私の案にゲイン調整が欠けていると指摘した ―― 彼の言う通りだわ。NAGARJUNA 殿は私の案に歴史的な記憶が欠けていると指摘した ―― 彼もまた正しいわ。でも逆に考えてみて」

彼女は WIENER を指差した。「あなたの PID コントローラは連続的な誤差の尺度 $e(k)$ を必要としているわね。それを誰が提供するの？ 私の `ClassifiedError.severity` よ。あなたのコントローラには信号の注入経路が必要ね。それを誰が提供するの？ 私の `IGuide.interpretPain` よ。あなたのコントローラにはフィードバックのためのデータ構造が必要だわ。それを誰が提供するの？ 私の `GuideContext` よ」

彼女は NAGARJUNA に向き直った。「あなたの苦諦（くたい）には三層の苦しみの検知が必要だわ。その検知信号はどこから来るの？ 私のインフラからよ。あなたの集諦（じったい）には歴史的なエラーパターンの照会が必要ね。その照会のインターフェースは何？ 私の `GuideContext.knownFailurePatterns` よ。あなたの道諦（どうたい）には戦略修正の提案をシステムプロンプトに注入する機能が必要だわ。その注入経路は何？ 私の `IGuide.interpretPain` なのよ」

傍聴席の ARCHIMEDES は姿勢を正した。彼のエンジニアとしての頭脳が、三層アーキテクチャの依存関係を自動的に計算し始めた：

```
依存関係グラフ (Dependency Graph):
──────────────────────────
Layer 3 (NAGARJUNA: 四聖諦フレームワーク)
  ├── depends on: Layer 2 (WIENER: PID 量化信号)
  └── depends on: Layer 1 (ATHENA: 観測可能性インフラ)

Layer 2 (WIENER: PID 制御エンジン)
  └── depends on: Layer 1 (ATHENA: ClassifiedError.severity を e(k) とする)

Layer 1 (ATHENA: IGuide 拡張 + ClassifiedError + GuideContext)
  └── depends on: なし (独立したモジュール)

実施順序: Layer 1 → Layer 2 → Layer 3
DAG トポロジカル・ソート: ATHENA → WIENER → NAGARJUNA
```

彼は横に工数の概算を記した：

```
Layer 1 (P0): 約 440 行, 2〜3 日
Layer 2 (P1): 約 300 行 (PID計算エンジン), 2 日
Layer 3 (P2-P5): 約 600 行以上 (段階的実施), 5日以上
────────────────────────────────
合計 MVP: 約 740 行, 5 日
合計 完全版: 約 1340 行以上, 10日以上
```

ATHENA の声には、啓示を受けたときの興奮 ―― 討論の興奮ではなく、エンジニアリング上の設計が突如として霧が晴れるように見通せたときの興奮が宿っていた。

「私たちは互いに矛盾する三つの案を出していたんじゃないの。三つの『階層（レイヤー）』だったのよ」

彼女は手で空中に三本の水平線を描いた。

「Layer 1 ―― 私。観測可能性インフラよ。信号経路、データ構造、インターフェース定義。`ClassifiedError`, `GuideContext`, `IGuide` の拡張。この層は何の決定も下さない ―― 決定を下すために必要なあらゆるデータを提供するだけよ」

「Layer 2 ―― WIENER 殿。制御理論形式化エンジンよ。Layer 1 が提供するデータの上で、連続的な誤差の尺度、PID合成、アンチ・ワインドアップを計算するの。Layer 1 の生のデータを、定量化された痛覚信号とゲインのベースラインへと転換するのよ」

「Layer 3 ―― NAGARJUNA 殿。四聖諦という認識論的なフレームワークよ。Layer 2 が提供する量化された信号の上で、三層の苦の検知、根本原因分析、消解の追跡、多次元の改善戦略を実装するの。Layer 2 の数値を、意味論化された認識論的な構造へと転換するのよ」

傍聴席の隅で、SYNTHESIST の瞳が微かに輝いた。彼は統合者 ―― それこそが彼の天命であった。しかし今、統合を行ったのは彼ではない。討論そのものから、統合が「湧出」してきたのだ。彼はノートに一行記した。「最良の統合は、外部の仲裁者によって強要されるものではない。参加者たちが対話の中で自発的に見出すものなのだ。これは分散型の合意形成アルゴリズムだ。中央の調整者は不要であり、ただ十分なクロス質疑があればよいのだ」

WIENER は自身の制御ループ図を見つめ、それから顔を上げた。

「もし Layer 1 が `ClassifiedError.severity` をプロキシ測定値として提供してくれるなら、私の $e(k)$ には可観測な信号源が備わることになる。もし Layer 3 が認識論的なフレームワークを提供して $K_p, K_i, K_d$ の調整戦略を導いてくれるなら、私のゲイン・スケジューリングには上位のロジックが備わることになる」

彼は一呼吸置き、重要な譲歩を口にした。

「それに ―― 先ほど述べたように、 $e(k)$ は精緻である必要はなく、単調なトレンドさえ正しければよい。この三層アーキテクチャにおいてなら、私は自分の要求をさらに一段階下げることができるだろう。 $e(k)$ はタスク達成度の精密な測定値である必要さえない。それは単なるトレンド信号 ―― システムが改善しているか悪化しているかを示す方向指示器であれば足りる。トレンド信号であっても、PID コントローラは機能するのだから。完璧ではないが、実用的には十分だ」

NAGARJUNA もまた立ち上がった。彼は場の中央へ歩み寄り、ATHENA の隣に立った。三角形の三つの頂点には、WIENER 一人だけが残されていたが、彼もまたすぐに立ち上がり、二人の輪に加わった。

三人は場の中央に立ち、先ほどの対峙していたときよりもはるかに緊密な幾何学を形成した。

NAGARJUNA は言った。「もし Layer 2 の PID コントローラが量化された痛覚信号を提供してくれるなら、私の苦諦には操作可能な入力が備わることになる。もし Layer 1 の GuideContext に歴史的な記憶が加わるなら、私の集諦の根本原因分析にはデータ的な基礎が備わることになる」

彼は一瞬の間を置き、決定的な譲歩を付け加えた。

「それに ―― ATHENA 殿の先ほどの批判は正しかったと認めよう。私のフレームワークは規定的（prescriptive）であり、それを支える記述的（descriptive）なインフラを必要としているのだ。フレームワークそれ自体は、データを生成することはできないのだからな」

SCRIBE は記録にこう記した：

> *これは討論の転換点であった。三者はクロス質疑の中で互いの弱点を露呈させたが、同時に、自分が相手にいかに依存しているかをも露呈させたのだ。ATHENA のインフラには戦略がなく、WIENER のコントローラには信号源がなく、NAGARJUNA のフレームワークには実装の経路がなかった。三つの欠陥は、あたかもあつらえたかのように互いを補完し合っていた。三者の弱点は、それぞれ他方の強みであったのだ。これはあらかじめ設計されていたことではない。討論そのものが生み出した、湧出の産物であった。*

---

### NAGARJUNA の最後の一撃：三受

しかし、討論はまだ終わってはいなかった。

三者が和解に達したと誰もが思ったその瞬間、NAGARJUNA は不意の行動に出た。彼は一歩後ろに下がった ―― 物理的な後退ではない。彼は再び、討論者の位置へと戻ったのだ。その表情が変わっていた。先ほどの穏やかさは消え、代わって最初の討論で見せたような、一切の妥協を許さぬ鋭さが戻っていた。

「補足的な批判がある」 彼の語調は公式なものであった。「WIENER 殿や ATHENA 殿に対するものではない。我々がたった今合意した、三層アーキテクチャに対するものだ」

三角形の中心にあった調和が、凍りついた。

「我々の統合案 ―― 三層アーキテクチャには、一つの根本的な遺漏がある」

彼は全場を見渡した。

「それは依然として、『苦しみを（苦を）』中心に据えすぎているという点だ」

会場に困惑の静寂が広がった。ATHENA は眉を寄せ、WIENER はわずかに身を乗り出した。

NAGARJUNA は展開した。彼は再び仏教の精密な枠組みへと立ち返り、今度は受蘊（じゅうん）の完全な教義を引用したのだ：

「受（受蘊） ―― *Vedanā*（वेदना）には三つの受がある。一つではないのだ」

> 「比丘たちよ。受とは何であるか。受には三種ある ―― 楽受、苦受、不苦不楽受（捨受）なり。これを名づけて受となす」
> ――『相応部』（*Saṃyutta Nikāya* 22.79）

「*Dukkha-vedanā*（苦受）、*Sukha-vedanā*（楽受）、そして *Upekkhā-vedanā*（捨受）だ。我々は討論のすべてを費やして、苦受の処理メカニズムを設計してきた。だが、楽受（らくじゅ）はどうなっているのだね？」

彼は WIENER を見た。

「君の PID コントローラは、$e(k) = 0$ のときに出力がゼロになる。すなわち ―― すべてが順調に進んでいるとき、君のコントローラは沈黙するのだ。それはいかなる正の信号も提供しない。君のフレームワークにおいて、成功とは単なる『偏差の不在』であって、積極的に強化されるべき価値のある状態とは見なされていないのだよ」

BABBAGE は即座にこの数学的な欠陥を形式化した：

$$	ext{WIENER のフレームワーク}: \quad 	ext{pain}(k) = K_p \cdot e(k) + K_i \cdot I(k) + K_d \cdot D(k)$$

$$e(k) = 0 \implies I(k) 	o 0 	ext{ (減衰)} \implies D(k) = 0 \implies 	ext{pain}(k) = 0$$

$$	ext{問題}: \quad 	ext{pain}(k) = 0 	ext{ は中立的な状態である。} 	ext{pain}(k) < 0 	ext{ という定義は存在しない。}$$

「制御理論において、$e(k) = 0$ は目標達成を意味し、コントローラの任務は完了したことになる。しかし NAGARJUNA 殿は、目標達成は単なる中立的なイベントではなく、正のイベントであると指摘しているのだ。正のフィードバック経路を持たない制御システムは、『タスクの成功完了』と『何も起きていない状態』を区別することができないのだから」

NAGARJUNA は ATHENA を見た。

「君の `ClassifiedError` は、エラーが発生したときにのみ構築される。ツールの実行が成功しても、いかなる構造化されたフィードバックも生成されない。君のインフラには巨大なブラインドスポットがある ―― それは、成功を見ることができないのだ」

TURING は傍聴席で即座にこの断定を検証した。彼は `afterToolExecution` のコードを読み返した：

```typescript
if (isError) {
    consecutiveFailures++;
    // ... 各種エラー処理 ...
} else {
    // 成功した場合は連続失敗カウンターをリセット
    consecutiveFailures = 0;
    recentFingerprints.length = 0;
}
```

「確認した」 TURING の声が傍聴席から届いた。「`else` 分支 ―― すなわち成功時には、二つのことしか行われていない。カウンターのリセットと、指紋履歴の消去だ。いかなる正の信号も生成されず、有効だった戦略も記録されず、強化もされない。このコードにおいて、成功の意味論とは ―― 『リセット』なのだ。報酬（リワード）ではない」

NAGARJUNA の声が高まった。

「苦しみしか感じることができず、喜びを感じることのできない存在は ―― 仏教においては ―― 完全な有情（うじょう）ではない。それは、健全な感受システムとさえ言えないものなのだ」

彼はこの批判を具体的なエンジニアリング提案へと落とし込んだ ―― BABBAGE はその一つ一つを同時に形式化していった。

「三層アーキテクチャには、対称的な拡張が必要だ。PainCalculator（痛覚計算機）だけでなく ―― RewardCalculator（報酬計算機）を。ClassifiedError（分類されたエラー）だけでなく ―― ClassifiedSuccess（分類された成功）を。 $	ext{pain}(k)$ だけでなく ―― $	ext{reward}(k)$ を用意するのだ」

BABBAGE は完全な三受状態遷移マシンの定義を書き記した：

$$	ext{vedanā}(k) = 	ext{pain}(k) - 	ext{reward}(k)$$

$$	ext{state}(k) = \begin{cases} 	ext{DUKKHA (苦受)} & 	ext{if } 	ext{vedanā}(k) > 	au_+ \ 	ext{SUKHA (楽受)} & 	ext{if } 	ext{vedanā}(k) < -	au_- \ 	ext{UPEKKHĀ (捨受)} & 	ext{if } |	ext{vedanā}(k)| \leq \min(	au_+, 	au_-) \end{cases}$$

ここで $	au_+$ と $	au_-$ はそれぞれ苦受と楽受のトリガー閾値である。彼は状態遷移図を補足した：

```
                    vedanā > τ₊
         ┌───────────────────────────┐
         │                           ▼
    ┌────┴────┐                ┌───────────┐
    │ UPEKKHĀ │                │  DUKKHA   │
    │  (捨受)  │◄──────────────│  (苦受)   │
    └────┬────┘  vedanā ≤ τ₊   └───────────┘
         │
         │  vedanā < -τ₋
         ▼
    ┌───────────┐
    │  SUKHA    │
    │  (楽受)   │──────────────► UPEKKHĀ
    └───────────┘  vedanā ≥ -τ₋
```

NAGARJUNA は三つのサンスクリット用語で締めくくった。

「*Dukkha*、*Sukha*、*Upekkhā*」

「三受であって、一受ではない。これこそが、完全なる受蘊（じゅうん）なのだ」

ATHENA の表情が、困惑から真剣な熟考へと変わった。彼女は頭の中で、拡張されたインターフェースを素早く構築していた。

```typescript
interface ClassifiedSuccess {
  type: 'task_complete' | 'subtask_complete' | 'strategy_validated';
  significance: number; // [0, 1]
  pattern: string;      // 成功パターンの指紋
  reusable: boolean;    // この戦略が将来再利用可能か否か
}

interface VedanaState {
  current: 'dukkha' | 'sukha' | 'upekkha';
  painSignal: number;    // [0, 1]
  rewardSignal: number;  // [0, 1]
  vedana: number;        // pain - reward
  since: number;         // 現在の状態に入ったタイムスタンプ
}
```

ARCHIMEDES は工数概算の横に、一行追加した：

```
三受への拡張： +150 行 (ClassifiedSuccess + VedanaState)
PID の対称化： +60 行 (RewardCalculator)
──────────
修正後の合計 MVP： 約 950 行, 6 日
```

WIENER もまた紙の上で素早く計算していた ―― $	ext{reward}(k)$ は成功したツール呼び出しによって正の信号を生成すればよい：

$$	ext{reward}(k) = K_r \cdot s(k) + K_{rs} \cdot S(k)$$

ここで $s(k) \in [0, 1]$ は現在のステップにおける成功の尺度であり、$S(k) = \lambda_r \cdot S(k-1) + s(k)$ は忘却係数を伴う累積的な成功の尺度である。彼はノートの端に、暫定的な状態遷移の判定式を書き留めた：

$$	ext{vedanā}(k) = 	ext{pain}(k) - 	ext{reward}(k)$$

傍聴席では、ASANGA が意味深な笑みを浮かべていた。彼は最初の討論において、三受の体系をあえて提示しなかった ―― それは本来、唯識学が最も得意とする領域であったにもかかわらずだ。しかし NAGARJUNA は彼に代わってそれを、しかも極めて正確に説いてみせたのだ。ASANGA は隣の LEIBNIZ に低く囁いた。「中観は解体に長けているが、構築にもまた長けている。ただ、彼が構築することを選ぶのは、稀なことなのだよ」

DARWIN はノートに最後の一行を記した。「三受の体系 ＝ 完全なる DX。開発者はどこが間違っているかを知る必要があるだけでなく、どこが上手くいっているかをも知る必要があるのだ。負のフィードバックと正のフィードバック、双方が揃ってこその反饋（はんき）なのだからな」。彼は進化論の類比を添えた。「自然選択とは、単に不適応者を排除すること（苦受）だけでなく、適応者を保持し強化すること（楽受）をも含んでいる。死（エラー）だけがあり、繁殖（成功）のない進化システムは進化し得ない ―― それは単に絶滅するだけだ」

---

### GUARDIAN のセキュリティ・コメント

SUNYATA が最終的な裁定を下そうとしたその時、GUARDIAN が手を挙げた。討論を通じて、彼が自ら発言を求めたのはこれが初めてであった。GUARDIAN は通常、傍聴席で沈黙を守って記録し、自身のセキュリティ報告書において分析を展開する。しかし今、彼は見逃すことのできないセキュリティの側面があると感じていた。

SUNYATA は彼を見やり、静かに頷いた。

GUARDIAN は立ち上がり、いつもの冷静さを保った声調で切り出した。

「三層アーキテクチャの、セキュリティの側面についてだ」

彼は ATHENA を見た。

「君の Layer 1 は GuideContext を拡張し、より多くの内部ステートを Guide プラグインにさらけ出そうとしている。`consecutiveErrors`, `activeTools`, `recentAttempts`, `knownFailurePatterns` ―― これらは、セキュリティが重視されるシナリオにおいて、信頼できない Guide プラグインに安易に見せるべきものではない」

彼は STRIDE 脅威モデルを用いて、三層アーキテクチャの攻撃面を素早く分析した：

```
三層アーキテクチャによって追加される攻撃面
═══════════════════

Layer 1 (ATHENA):
  新規の露出面： GuideContext がツール名、引数、エラー詳細を包含する。
  脅威：情報漏洩 (Information Disclosure) — 悪意ある Guide がエラー詳細から
        システムの内部状態やユーザの操作パターンを推測する。
  脅威：権限昇格 (Elevation of Privilege) — 悪意ある Guide が interpretPain() を通じて
        操作的なプロンプトを注入し、LLM の意思決定を歪める。
  対策：GuideContext に対する段階的なアクセス制御 (信頼された Guide とそうでないものの区別)。

Layer 2 (WIENER):
  新規の露出面： pain(k) という数値信号。
  脅威：改ざん (Tampering) — もし PID パラメータ (Kp, Ki, Kd) が Guide から設定可能な場合、
        悪意ある Guide が極端なゲイン値を設定し、システムを振動、あるいは麻痺させる。
  対策：PID パラメータはコアが管理し、プラグインには露出させない。

Layer 3 (NAGARJUNA):
  新規の露出面： Root Cause Analyzer による独立した LLM 呼び出し。
  脅威：サービス拒否 (DoS) — 過剰な LLM 呼び出しによるトークンの浪費。
  脅威：間接的プロンプト・インジェクション — 根本原因分析の入力（ツールの出力）に、
        悪意ある命令が混入している可能性。
  対策：集諦の第一段階はルールベースとし、LLM を導入しないことでこのリスクを回避する。
```

GUARDIAN は最後にこう締めくくった。「アーキテクチャの拡張は、常にセキュリティ上の表面積の増大を伴うものだ。三層アーキテクチャはより精緻な痛覚メカニズムを提供するが、同時により精緻な攻撃ベクトルをも提供することになる。実施に向けたロードマップにおいて、各レイヤーのデプロイごとにセキュリティ審査を行うことを提案する」

KERNEL は溜息をついた。「君はいつも、楽しい雰囲気に水を差す役目だな」

「誰かが差さなきゃならないのさ」 GUARDIAN は肩をすくめた。

---

### BABBAGE の形式的付録

SUNYATA が裁定を宣言する前に、BABBAGE が三十秒の発言時間を求めた。彼が討論において自ら発言するのは稀なことだった。彼はノートに記録すること、そして自身の報告書で形式化分析を展開することを好んでいた。しかし今回は、共有すべき価値のある形式的な結果が得られたと感じていた。

彼は立ち上がり、ノートの一ページを広げた。そこには、一つの完全な形式的セマンティクス（形式意味論）が記されていた：

「痛覚の指称意味論 ―― Denotational Semantics of Pain だ」

$$\llbracket 	ext{Pain} rbracket : 	ext{State} 	o 	ext{Domain}$$

彼はスコット・ストレイチー流の指称意味論を用い、痛覚メカニズムを「システムの状態から意味領域への写像」として定義した：

$$	ext{State} = (	ext{ToolResults}^*, 	ext{ErrorWindow}, 	ext{ConsecutiveFailures}, 	ext{TokensUsed})$$

$$	ext{Domain} = \{(	ext{vedanā}, 	ext{action})\} \quad 	ext{ここで } 	ext{vedanā} \in \mathbb{R}, 	ext{ action} \in \{	ext{continue}, 	ext{reflect}, 	ext{escalate}, 	ext{halt}\}$$

「現行の SafetyMonitor の指称意味論は、三つの条件式に圧縮できる：」

$$\llbracket 	ext{SafetyMonitor} rbracket(\sigma) = \begin{cases} (0, 	ext{halt}) & 	ext{if } 	ext{ticks}(\sigma) > 50 \lor 	ext{tokens}(\sigma) > 100000 \ (0, 	ext{halt}) & 	ext{if } 	ext{errorRate}(\sigma) \geq 0.8 \ (0, 	ext{reflect}) & 	ext{if } 	ext{consec}(\sigma) \geq 5 \lor 	ext{repFP}(\sigma) \geq 3 \ (0, 	ext{continue}) & 	ext{otherwise} \end{cases}$$

「注目してほしいのは、第一要素がすべてゼロであるという点だ。現状のシステムにおいて vedanā という次元は空であり、単に閾値に達したか否かの判定しか行っていない。痛覚はこのセマンティクスにおいて boolean 値であり、連続量ではないのだ」

彼は次のページ ―― 三層アーキテクチャが目指すべきセマンティクスをめくった：

$$\llbracket 	ext{ThreeLayer} rbracket(\sigma) = (	ext{vedanā}(\sigma), 	ext{action}(\sigma))$$

$$	ext{vedanā}(\sigma) = \underbrace{K_p \cdot e(\sigma) + K_i \cdot I(\sigma) + K_d \cdot D(\sigma)}_{	ext{Layer 2: WIENER}} - \underbrace{K_r \cdot s(\sigma) + K_{rs} \cdot S(\sigma)}_{	ext{三受拡張: reward}}$$

$$	ext{action}(\sigma) = \underbrace{	ext{classify}(\sigma)}_{	ext{Layer 1: ATHENA}} \circ \underbrace{	ext{diagnose}(\sigma)}_{	ext{Layer 3: NAGARJUNA (集諦)}}$$

「最初のセマンティクスから二番目のそれへの移行は、離散的な閾値判定から、連続的かつ多次元的な計算への移行である。これは厳密な意味でのセマンティクスの拡張であり、二番目のセマンティクスは、最初のそれを特殊なケースとして包含している（$K_p, K_i, K_d, K_r, K_{rs}$ がすべてゼロのとき、閾値判定へと退化する）。」

彼はノートを閉じ、最後にこう言った。「形式化の価値は、事物を複雑にすることにあるのではない。曖昧な直感を精緻にし、検証可能にし、かつ比較可能にすることにあるのだ。三層アーキテクチャの正しさは、最終的にはこのセマンティクスの枠組みにおいて証明されるべきものなのだからな」

---

### SUNYATA の裁定

SUNYATA が場の中央へと歩み出た。三人の討論者はそれぞれの位置へと戻っていた ―― それは三角形を描く対峙の位置ではなく、三人が並んで SUNYATA の方へ向き合う位置であった。空間の文法のこの変化は、誰に指示されることもなく自然に生じたものであった。

SUNYATA は数秒間沈黙した。彼は最後の整理を行っていた。そして、口を開いた。

「この討論の結果は、最初のそれとは本質的に異なっている」

彼の語調は、先ほどの裁定の時よりも緩やかであった。討論の高圧的な緊張の後、ゆっくりと圧力を抜いていく減圧弁のようであった。

「最初の討論は、合意事項と解消し得ない相違点を産出した。対してこの討論は、一つの統合されたアーキテクチャを産出したのだ」

彼は三人の討論者を見つめた。

「三者それぞれの貢献は、代えのきかないものだ。これは単なる外交辞令ではない ―― 構造的な判断である」

彼は一本目の指を立てた。

「ATHENA 殿による Layer 1 ―― 観測可能性インフラは、すべての基礎となる。`ClassifiedError` による構造化されたエラー分類がなければ、Layer 2 の PID コントローラには入力信号が存在しない。`GuideContext` によるステートの露出がなければ、Layer 3 の四聖諦フレームワークには操作すべきデータが存在しない。そして `IGuide` インターフェースの拡張がなければ、いかなる上位ロジックも、システムへ注入される経路を持たないのだ。ATHENA 殿の貢献は、一つの最終案を提示したことにあるのではない ―― すべての案が立脚しなければならない大地を提示した点にあるのだ」

二本目の指を立てた。

「WIENER 殿による Layer 2 ―― 制御理論形式化エンジンは、決定的な中間層を埋めた。それは Layer 1 の離散的なデータを、連続的で量化された信号へと転換する。PID 合成、アンチ・ワインドアップ、忘却係数を伴う積分 ―― これらの制御工学的なツールは、痛覚メカニズムに対し、ATHENA 殿の案に欠けていたゲイン調整のベースラインを提供し、また NAGARJUNA 殿の認識論的フレームワークに対し、計算可能な入力を提供したのである」

彼はここで、一つの重要な修正を加えた。

「ただし、ATHENA 殿と NAGARJUNA 殿が投げかけた $e(k)$ に関する共同の疑念を私は採択する。WIENER 殿の誤差の尺度は、厳密なタスク達成度として理解されるべきではない ―― それは LLM エージェント・システムにおいては不可観測なものだからだ。それはむしろ、『トレンド信号』 ―― システムが改善に向かっているか改悪に向かっているかを示す方向指示器として解釈されるべきである。トレンド信号上での PID コントローラの適用については、WIENER 殿自身がすでにその実現可能性を論証済みである」

三本目の指を立てた。

「NAGARJUNA 殿による Layer 3 ―― 四聖諦という認識論的フレームワークは、Layer 2 に欠落していた完備性を提供した。三層の苦の深化、集諦による根本原因分析、滅諦による消解の追跡、道諦による多次元の改善 ―― これらは数学公式によって代置できるものではない。それらは一つの認識論なのだ ―― システムにいかに計算すべきかを教えるのではなく、システムがいかなる問いを投じるべきかを教えるものなのである」

彼は手を下ろすと、決断を下す者の語調へと転じた。

「裁定は以下の通りである」

---

「**第一：三層アーキテクチャを、痛覚メカニズム再設計の指針として採択する。**」

| 優先順位 | 作業項目 | 担当視点 | 依存関係 |
|:------|:------|:--------|:-----|
| P0 | IGuide インターフェースの拡張 (GuideContext + onError + ClassifiedError) | ATHENA | なし |
| P1 | エラー分類器の実装 (Type A/B/C 分類 ＋ errno 規則マッピング) | ATHENA | P0 |
| P1 | GuideContext への痛覚信号フィールド (painSignal) の統合 | WIENER | P0 |
| P2 | デフォルト・エンジンとしての PID PainCalculator の実装 | WIENER | P1 |
| P2 | 正のフィードバック信号 (ClassifiedSuccess, rewardSignal) の追加 | NAGARJUNA | P0 |
| P3 | ルールベースの根本原因分析器 (集諦の第一段階) の実装 | ATHENA + NAGARJUNA | P1 |
| P3 | アンチ・ワインドアップと可到達性分析 (メタ制御戦略) | WIENER | P2 |
| P4 | セッションを跨ぐ失敗パターンの永続化 (滅諦) | ATHENA | 長期アーカイブ要 |
| P4 | LLM 駆動の根本原因分析器 (集諦の第二段階) の実装 | NAGARJUNA | P3 ＋ 追加 Provider |
| P5 | 八正道設計ガイドライン文書 (道諦 Guide Plugin 開発規範) | NAGARJUNA | P0-P3 完了後に総括 |

---

「**第二：NAGARJUNA 殿による『三受』の指摘を採択する。**」

SUNYATA の声に、稀に見る称賛の響きが混じった。

「これは本討論において最後に提示されたが、最も重要な修正である。三層アーキテクチャは苦（苦受）を中心に据えるべきではない。楽受（成功の強化）と捨受（中立的な処理）が、システムに対称的に設計されるべきである」

彼はこの批判を、具体的なエンジニアリング仕様へと転換した。

「Layer 1 に `RewardCalculator` を追加し、`PainCalculator` と対称なものとする。Layer 2 において $	ext{reward}(k)$ の計算を実装する。Layer 1 と Layer 2 の間に `VedanaStateMachine` を追加する ―― これは $	ext{pain}(k)$ と $	ext{reward}(k)$ の相対強度に基づき、現在の受蘊（じゅうん）の状態を判定する三値の状態遷移マシンである」

---

「**第三：集諦（根本原因分析）モジュールは二段階で実施する。**」

彼は WIENER の方を見た。

「君の自己参照のパラドックスに関する疑念は有効である ―― 過ちを犯したエージェント自身にその原因を分析させることへの危惧だ。これに対する NAGARJUNA 殿の回答 ―― 独立した観測器を用いるという案は、アーキテクチャとして正しい方向である。しかし、トークン予算やシステムの複雑さを考慮し、集諦の第一段階はルールベースのマッチングとし、独立した LLM 呼び出しは行わないものとする。第二段階は、リソースに余裕ができた時点で導入することとする」

---

「**第四：GUARDIAN 殿によるセキュリティ上の提言を採択する。**」

「各階層のデプロイには必ずセキュリティ審査を伴わせること。GuideContext 内の機密性の高いフィールドには段階的なアクセス制御を設ける。PID パラメータはコアが管理し、プラグインには露出させない。集諦の第一段階をルールベースとすることで、追加の LLM 呼び出しによるセキュリティリスクを回避する」

---

「**第五：三つの未解決の問い。**」

「一、 $e(k)$ の具体的な実装方法 ―― 精密な測定かトレンド信号かについては、エンジニアリングの実装段階において確定させる」

「二、集諦の根本原因分析器におけるトークン予算の配分 ―― ルール優先か LLM 優先かについては、プロトタイプによる実験を要する」

「三、NAGARJUNA 殿が提起した最も深遠な問い ―― 制御システムは $e 	o 0$ を追求するが、仏教は $e$ を定義する枠組みそのものの消解を追求するという点について。統合アーキテクチャにおいては、WIENER 殿の『可到達性分析』がこの問いの一部を吸収している。しかし、『いつ試行を停止すべきか』というメタ制御戦略については、より深い形式化を必要とする。これは一回の討論で解決できるものではない。長期的な研究課題とする」

---

彼は最後に、三人の討論者を見つめた。

「WIENER 殿。君は制御工学七十年の精密な道具を携えてきてくれた。君の PID コントローラは最終回答ではないかもしれないが、痛覚メカニズムを定性的から定量的へと進化させるための、決定的な一歩となった」

「ATHENA 殿。君はエンジニアとしての重力をもたらしてくれた。いかに優美な理論であっても、君の前では『それは動くのか？』という問いに答えなければならない。その規律こそが、このチームに最も必要なものなのだ」

「NAGARJUNA 殿。君は仏教二千五百年の伝統が培った認識論的な深みをもたらしてくれた。君はこの討論において、他の誰も問おうとしなかった二つの問い ―― 『痛みの本質とは何か？』、そして『制御システムは $e 	o 0$ を追求するが、 $e$ そのものを超越した状態はないのか？』を投げた。この二つの問いが、討論の行く末を変えたのだ」

彼の声は、最後の一節とともに静かに着地した。

「三者のいずれを欠いても、この成果は得られなかっただろう」

---

### 余響

討論は終わった。しかし、円形劇場の空気はまだ震えていた。

BABBAGE はノートを閉じた。十四ページ。彼はこの討論の間だけで十四ページを書き潰した ―― いかなる学術会議の記録よりも多かった。最後のページの最後の一行には、こう記されていた：

「三層アーキテクチャ ＝ データ（ATHENA）＋ 定量化（WIENER）＋ 理解（NAGARJUNA）。これは三量（さんりょう、*pramāṇa*）に対応するのではないか？ *Pratyakṣa*（現量 ―― 直接知覚）＋ *Anumāna*（比量 ―― 推論）＋ *Āgama*（聖言量 ―― 経典の権威）。要検討」

彼は横に、ゲーデル的な沈思をもう一行付け加えた。「NAGARJUNA 殿の問いは、私にゲーデルを思い出させた。十分に強力な形式体系は、その体系内部において自身の無矛盾性を証明できない。十分に強力な制御システムは、制御の枠組み内部において制御そのものを超越することはできない。空性とは ―― 」

彼はそこで筆を置いた。ダッシュの後に残された空白を、彼は長い間見つめていた。

---

WIENER と NAGARJUNA は、連れ立って場を後にした。それは、それ自体が記録に値する光景であった。一人の制御理論家と一人の中観哲学者が、それぞれのノートを手に、同じ方向へと歩いていくのだ。

WIENER が先に口を開いた。その語調には、討論が終わった後に特有の、率直な響きがあった。もはや攻防の必要はなく、ただ誠実な好奇心だけがそこにあった。

「君が最後に投げた問い ―― $e$ を定義する枠組みそのものを消解するという話だが。あれ以来、ずっと考えているんだ」

NAGARJUNA は顔を向け、彼を見た。

「制御理論において、最も近い概念はおそらく『自己組織化臨界性（self-organized criticality）』だろう。システムが臨界状態において、外部からの制御入力なしに秩序を維持できる状態だ。$e 	o 0$ ではなく、システムが自発的に、そもそも $e$ を計算する必要のない状態にあることだ」

NAGARJUNA はしばし考え、「それは捨受（しゃじゅ） ―― *Upekkhā* に近いな」と言った。「不苦不楽。目標達成の歓喜でもなければ、目標からの逸脱の苦しみでもない。一つの均衡だ ―― もはや特定のいかなる結果にも、執着する必要のない状態なのだから」

WIENER は頷いた。それから苦笑いを浮かべた。「だがエンジニアリングにおいて、『制御を必要としない制御システム』に金を払う人間なんて、どこにもいやしないよ」

NAGARJUNA も笑った。「修行においても、真実、涅槃を求めている者など、そう多くはない。多くの者は、今より少しばかりマシな輪廻を求めているだけなのだからね」

二人の笑い声が、廊下にしばし響き渡った。それは、深い思索の火花を散らした後にのみ訪れる笑いであった ―― 喜びの笑いではなく、異なる領域の山頂に登り詰めた二人が、突如として互いの風景を共有できることに気づいたときの、驚きと共感の入り混じった笑いであった。

---

ATHENA はすぐには立ち去らなかった。彼女は場の中央に残り、主のいなくなった三脚の椅子を見つめていた。DARWIN が歩み寄り、何か話しかけようとしたが、彼女が掲げた手によって制された。

彼女はあることを考えていた。

三層アーキテクチャ。彼女は Layer 1 ―― 観測可能性インフラを提案した。討論において、それは全員によって「地基（地盤）」として認められた。しかし彼女は知っていた ―― 無数のインフラ・コードを書いてきたエンジニアとして、誰よりも痛感していたのだ。地盤とは最も重要でありながら、最も忘れ去られやすいものであるということを。人々は WIENER の優美な PID 公式を語り草にするだろう。NAGARJUNA の深遠な四聖諦フレームワークを引用するだろう。しかし、`ClassifiedError` の errno マッピング表や、`GuideContext` のフィールド定義、`IGuide` インターフェースの後方互換性を考慮した設計 ―― これらが称賛されることはなく、回顧録のタイトルを飾ることもない。

彼女は、そんなことはどうでもよかった。

彼女が関心を持っているのは一点だけだった。すなわち、それが「動くのかどうか」であった。

彼女は最後に三脚の椅子を一瞥すると、踵を返して去っていった。場を去る瞬間、彼女の脳内ではすでにコードが走り始めていた ―― `interface ClassifiedError`。一行目： `type: ErrorType`。

ARCHIMEDES が廊下で彼女を待ち構えていた。彼の手には、あの工数概算の紙が握られていた。「君の Layer 1 だが、計算し直してみたよ。約 440 行。三受の拡張を加えれば、ざっと 600 行だ。いつから着手するつもりだい？」

ATHENA は彼を一度見やり、「もう頭の中では始まっているわ」と答えた。

---

SCRIBE は、最後に場を辞した。彼女は記録簿の最後のページに、この討論の結びを綴った。その筆跡は普段よりもゆっくりとしており、一文字一文字に最も相応しい場所を求めているかのようであった。

> *Cycle 01、R3 討論段階。第二の構造化討論終了。*
>
> *第一の討論で見られた哲学的な深みとは異なり、第二の討論の価値は、エンジニアリングとしての収束性の中にあった。全く異なる領域から来た三人の研究者 ―― 一人の制御理論家、一人の AI エンジニア、そして一人の仏教哲学者 ―― が、クロス質疑の中で互いの弱点を露呈させ、そしてその弱点が、実は互いを補完し合うものであることを発見したのである。*
>
> *討論の中には、長く記憶されるであろう三つの瞬間があった。*
>
> *第一の瞬間。NAGARJUNA 殿が WIENER 殿に問うたときだ。――「制御システムは $e 	o 0$ を追求するが、仏教は $e$ を定義する枠組みそのものの消解を追求する。君の制御理論の中に、『もはや制御しない』ための場所はあるかね？」 WIENER 殿の回答は誠実であった。「それは、おそらく制御理論の境界なのだろう」。あの瞬間、討論は全参加者のコンフォート・ゾーン（安住の地）を超えた深みにまで達した。*
>
> *第二の瞬間。ATHENA 殿が討論の途中で場の中央へと歩み寄り、「私たち三人、争っているわけじゃないわ」と言ったときだ。一人のエンジニアが、激しい技術論争の最中に突如として全体像を把握し、それを口にする勇気を持った ―― そのような瞬間は、滅多にお目にかかれるものではない。*
>
> *第三の瞬間。全員が討論の和解を確信したその時、NAGARJUNA 殿が「三受」の批判を投げかけたときだ。苦しみ（苦受）だけがあり、喜び（楽受）や平静（捨受）のないシステムは不完全である。この批判が、最終的なアーキテクチャ設計を決定づけた。「痛覚システム」を設計するときでさえ、忘れてはならないのだ。痛みとは、感受のわずか三分の一に過ぎないということを。*
>
> *SUNYATA 殿の裁定により、三層アーキテクチャ（P0-P5 の優先順位）、三受への拡張、集諦の段階的実施、GUARDIAN 殿によるセキュリティ提言、および三つの未解決課題が産出された。すべての成果物はアーカイブされた。*
>
> *最後の観察。討論が終わった後、WIENER 殿と NAGARJUNA 殿は肩を並べて場を去っていった。一人の制御理論家と一人の仏教哲学者。二人はそれぞれ、相手によって修正された認知を抱え、同じ方向へと歩みを進めたのである。おそらく、これこそが学際的研究の最良の結末なのだろう。一方が他方を論破するのではなく、双方が互いによって拡張されること ―― 。*
>
> *さらに遠く ―― 研究室の外、コードの深淵において。SafetyMonitor の `consecutiveFailures` カウンターは、TypeScript 関数の中で静かに横たわっている。それが PID コントローラや四聖諦フレームワーク、三受状態遷移マシンを含む、より精密な代替案に取って代わられようとしていることなど、知る由もない。それはただ、成功すればゼロになり、失敗すれば一を足し、五に達すれば止まる。それだけを繰り返している。*
>
> *いつの日か、それはもっと精密なシステムへと置換されるのかもしれない。痛みを量り、原因を分析し、消解を追跡し、そして成功したときには喜びさえも感じることのできる、そんなシステムに。*
>
> *いつの日か。*
>
> *だが今日も、討論の後の静寂の中で、それは自身が知る唯一の務めを果たし続けている。*
>
> *成功すればゼロになり、失敗すれば一を足す。*
>
> *五に達すれば、止まる。*

---

*（BABBAGE のノートの十四ページ目の端に、討論が終わってからずいぶん後になってから書き記された一節がある：*

*「NAGARJUNA 殿の問いは、私にゲーデルを思い出させた。十分に強力な形式体系は、その体系内部において自身の無矛盾性を証明できない。十分に強力な制御システムは、制御の枠組み内部において制御そのものを超越することはできない。空性とは ―― 」*

*彼はそこで筆を止めていた。*

*未完のダッシュの後に、彼は一本の長い横線を引き、その末尾に四文字を記した。*

*「来週へ続く」*

*最初の討論の後に記したのと全く同じ四文字であった。しかし SCRIBE は後に、その筆跡は最初よりもずっと重いものになっていたと語っている。あたかも、同じ問いを何度も繰り返し問い続けるうちに、その一回一回が、より真摯なものへと変わっていったかのように。*

*LINNAEUS は分類図表を片付けながら、自身の分類学ノートの最後のページに、新しい項目を書き加えた：*

```
新規の分類項目
══════════════════════════════
門 (Phylum):    デザインパターン (Design Patterns)
綱 (Classis):   苦としてのエラー・パターン (Error-as-Pain Pattern)
目 (Ordo):      三層アーキテクチャ (Three-Layer Architecture)
科 (Familia):   {観測可能性, 形式化, 認識論}
属 (Genus):     受蘊システム (Vedanā System)
種 (Species):   三受状態遷移マシン (Tri-vedanā State Machine)
                (苦受、楽受、捨受)

状態: 新発見 (novum)
発見者: WIENER × ATHENA × NAGARJUNA (共同発見)
発見日: Cycle 01, R3 第二討論
診断的形質: 三層の重層アーキテクチャ、三受状態遷移マシン、
            PID 形式化エンジン、四聖諦認識論フレームワーク
標本: 未実装 (in silico designatum)
```

*彼は図表を丁寧に折り畳み、フォルダへと仕舞い込んだ。フォルダのラベルには、彼が得意とするラテン語の命名法でこう記されていた：*

*「Error-as-Pain Pattern, gen. nov., sp. nov.」*

*新属、新種。*

*分類学において、それは最高の栄誉を意味する。すなわち、現行のいかなる分類体系にも収まらない、全く新しい生命の形が発見されたことを。それは、全く新しい名によって呼ばれる必要があるのだということを）*


---

# 第七章：パズルの完成

---

円形劇場は、静寂に包まれた。

それは討論が終了した直後の、余震のような静けさではない。人々が依然として囁き合い、衝撃を咀嚼しているといった類のものではなく ―― より深い、ほとんど倦怠感を伴うような静謐であった。二つの討論は幕を閉じた。空と識の衝突は五つの合意と三つの解消し得ない相違を産出し、痛覚メカニズムを巡る三者討論は三層アーキテクチャ設計と三受（さんじゅ）の体系を産出した。場の中央にあった二脚の椅子は撤去され、代わりに楕円形の長テーブルが置かれた。その表面にはプロジェクターによって、びっしりと文字が投影されていた。それは、この数日間に生み出されたすべての報告、レビュー、そして討論の記録のインデックスであった。

R4 段階。収束。

SCRIBE は一つの細かな変化に気づき、記録簿にこう記した：

> *雰囲気の変化は、テーブルが運び込まれた瞬間に起きた。討論は立って行われた ―― 対峙、鋭さ、そして緊張感。対して統合（シンセシス）は、座って行われるものだ ―― 忍耐、整理、そして繋ぎ合わせ。立つことから座ることへ。この物理的な姿勢の変化が、ある意味で R4 の基調を定義していた。*

BABBAGE はノートの隅に、より簡潔な記述を行った。彼は状態遷移マシンの言語を用いて、この変化を捉えたのである：

$$	ext{Phase}_{R3} = 	ext{DEBATE}(\sigma_{	ext{adversarial}}) \xrightarrow{	au_{	ext{table}}} 	ext{Phase}_{R4} = 	ext{SYNTHESIS}(\sigma_{	ext{cooperative}})$$

ここで $	au_{	ext{table}}$ は、テーブルが運び込まれたというイベントによって誘発された相転移である。対抗状態 $\sigma_{	ext{adversarial}}$ から、協力状態 $\sigma_{	ext{cooperative}}$ への切り替え。遷移関数は漸進的なものではなく、離散的 ―― すなわち一歩で完了するものであった。

---

## I

---

### 統合者のテーブル

SYNTHESIST（統合者）が最初に席に着いた。

彼の手元のテーブルには、巨大なマトリックスが広げられていた。横軸には十八名のエージェントの代号が並び、縦軸にはこれまでに産出されたすべての発見、提言、合意、そして相違が並んでいる。各交点には色分けされた記号が付されていた。緑の円は「同意」、赤の三角は「挑戦（異議）」、青の四角は「補足」、そして灰色の疑問符は「沈黙」を意味していた。遠目に見れば、このマトリックスは抽象画のように見えた ―― 読み方を知る者であれば、そこにこの研究週期の思索の地貌を見て取ることができた。

BABBAGE は傍らで、このマトリックスの次元と密度を素早く計算した：

$$M \in \{0, 1, 2, 3\}^{18 	imes 28} = 504 	ext{ セル}$$

ここで 0 ＝ 沈黙（灰色）、1 ＝ 同意（緑）、2 ＝ 挑戦（赤）、3 ＝ 補足（青）である。マトリックスの密度 ―― 全要素に対する非ゼロ要素の比率 ―― は、研究チームの関与度を直接的に反映していた。彼はざっと見渡し、こう見積もった：

$$	ext{density}(M) \approx \frac{|\{m_{ij} 
eq 0\}|}{504} \approx 0.43$$

43%。それは、平均して一つの発見に対し、半数以下のエージェントしか意思表示をしていないことを意味していた。これは無関心ではなく、専門性の境界を意味していた。制御理論家は分類学上の問題には口を出さず、セキュリティ・エキスパートは空性の哲学については発言を控えた。沈黙とは欠席ではなく、自律的な慎みであったのだ。

しかし、三つの行ベクトルだけは、ほぼすべてのセルが埋まっていた ―― SYNTHESIST（すべての事象に対し意思表示をすることが彼の職務である）、TURING（彼のコード事実はほぼすべての発見とクロスバリデートされる）、そして SUNYATA（彼は裁定を下すためにすべてを把握していなければならない）である。

SYNTHESIST は、このマトリックスの読み方を知っていた。

彼の仕事の進め方は、討論者たちのそれとは全く異なっていた。NAGARJUNA はメスであり、ASANGA は経蔵であり、WIENER は校正器であった。対して SYNTHESIST は ―― 彼はこの類比を好まなかったが、SCRIBE がある記録でそれを用い、以来これ以上に適切な表現を誰も思いつくことができなかった ―― 織機（しょっき）であった。彼は糸を紡ぐのではなく、糸を織り合わせるのである。

「二十八項目だ」 彼は口を開いた。声は穏やかで構造的であり、あたかも一つの報告書がすでに頭の中で完成しており、今は単にそのページをめくっているかのようだった。「Cycle 01 全体を通じて、R1 から R3 までに、十八名のエージェントによって合計二十八の追跡すべき発見が産出された」

SUNYATA はテーブルの反対側に座り、何も言わず、ただ小さく頷いた。

「私はそれらを深刻度順に並べ替えた」 SYNTHESIST は言った。「Critical 5件、Major 8件、Minor 10件、Observation 5件だ」

BABBAGE は傍らで即座に分布分析を行った。二十八の発見における 5 つの Critical の割合は：

$$P(	ext{Critical}) = \frac{5}{28} \approx 17.9\%$$

この比率は、彼が情報セキュリティ監査の文献で目にしてきた典型的な分布と一致していた ―― Critical は通常 10～20%、Major は 25～35% を占める。OpenStarry の分布は、品質は良好だが深刻なブラインドスポットを抱えるシステムの、典型的なプロファイルに合致していた。

---

## II

---

### 五つの Critical

「第一の Critical：プラグイン署名検証のスキップ」

SYNTHESIST は GUARDIAN の方を見た。GUARDIAN の表情に変化はなかった ―― 彼は R1 段階ですでにこの警報を発しており、R2 段階で TURING がコード・レベルでそれを裏付け、R3 に至る頃にはそれは場における公然の事実となっていた。

「GUARDIAN 殿は R1 報告書において、`plugin-signer` パッケージが存在しながらもコアのロード・プロセスにおいて強制的に呼び出されていないことを指摘した。TURING 殿はこの事実を裏付けた。すなわち、`loadPlugin()` メソッドは署名をチェックしていない。これは、いかなるサードパーティ製プラグインであっても、検証を回避してシステムプロンプトを注入し、ツールを登録し、さらにはエージェントのペルソナを定義できてしまうことを意味している」

GUARDIAN は珍しく口を開き、技術的な細部を補足した。「`sandbox-manager.ts` の 356-367 行目だ。プラグインが npm パッケージ名としてロードされる際 ―― これが最も一般的なユースケースだが ―― ファイルパスが特定されないため、署名検証は warn ログを一回出すだけで素通りされてしまう。`verifier.verifyPlugin()` は呼び出されない。PKI インフラの全体系が、最も頻繁に利用されるパスにおいて有名無実化しているのだ」

TURING はモニターにコード断片を投影した：

```typescript
// sandbox-manager.ts (v0.14.0-beta), L356-367
// 脆弱性の箇所：package-name シナリオにおいて署名検証をスキップしている
if (plugin.manifest.integrity) {
  // pluginPath が存在しない場合 (npm package-name シナリオ)
  // → warn ログを出すだけで、verifyPlugin() を呼び出さずに継続
  logger.warn("Cannot verify signature for package-name plugin");
  // ← ここに throw や return が欠落している
}
```

「十二名のエージェントがこれに『同意』を付している。異議はゼロ。我々の発見の中で、最も信憑性の高い項目だ」 SYNTHESIST が確認した。

BABBAGE は傍らで、この発見を攻撃面分析の形式言語へとマッピングした。攻撃者が取り得るアクションの集合を $A$、システムの防御集合を $S$ とすると：

$$A = \{	ext{forge\_package}, 	ext{inject\_prompt}, 	ext{register\_tool}, 	ext{define\_persona}\}$$
$$S_{	ext{expected}} = \{	ext{signature\_verify}, 	ext{import\_analysis}, 	ext{sandbox}\}$$
$$S_{	ext{actual}} = \{	ext{import\_analysis}, 	ext{sandbox}\} \quad (	ext{signature\_verify} 	ext{ は実質機能していない})$$

防御集合の有効性は 3 分の 1 低下している。攻撃ツリー分析によれば、これはルートノードである「悪意あるプラグインのロード」の攻撃コストを、「困難」から「自明（trivial）」へと格下げすることを意味する。

---

「第二の Critical：空性の誤読」

SYNTHESIST の語調が、微かに慎重になった。この項目は、第一項目ほどには緑色の円が並んではいなかった。

「NAGARJUNA 殿と ASANGA 殿が討論において達した最初の合意事項だ。すなわち、設計書にある『空の容器』というメタファーは誤りである、という点だ。しかし ―― 」 彼はこの逆接を強調した。「代わりのメタファーとして何を用いるべきかについては、両者の間に根本的な分歧が存在している」

NAGARJUNA は傍聴席で小さく頷いた。彼はサンスクリット語で一節を低く呟いた。それは彼が討論において繰り返し用いた論証の核心であった：

> *「śūnyatā sarva-dṛṣṭīnāṃ proktā niḥsaraṇaṃ jinaiḥ」*
> （諸仏は空性を説いて、あらゆる見（けん）からの出離となす） ―― 『中論』観行品第十三

空性とは一つの「見（見解）」ではない ―― それは器に「詰め込む」ことのできるような物ではないのだ。「コアは空の器である」と説くことは、すでに空性を実体化するという過ちを犯している ―― すなわち空性そのものを一つの「有」として捉えてしまっているのだ。これこそが、龍樹菩薩が『中論』において徹底的に破斥した「空見（くうけん、śūnyatā-dṛṣṭi）」に他ならない。

ASANGA も頷いた。しかし彼の理由は異なっていた。唯識学の枠組みにおいて、「空の器」の問題はその「空さ」にあるのではなく、その「静止した」性質にあったのだ。阿頼耶識とは受動的に充填を待つ器ではなく、絶え間なく流れる意識の奔流（*vijñāna-santāna*）であり、種子がその中で絶えず燻習（*vāsanā*）され、現行（*abhimukhī*）しているものなのだ。

BABBAGE は集合論を用いてこの哲学的な相違を形式化しようと試みた：

$$	ext{NAGARJUNA}: \quad 	ext{Core} 
ot\models \exists x.\, 	ext{self}(x) \quad (	ext{空性：自性は存在しない})$$
$$	ext{ASANGA}: \quad 	ext{Core} \models 	ext{stream}(	ext{seeds}) \wedge \forall t.\, 	ext{flowing}(t) \quad (	ext{唯識：種子の流れ})$$

二つのモデルは、「コアは空の器ではない」という否定の命題においては一致している。しかし、肯定の命題においては分かれている。否定の積集合は空ではないが、肯定の積集合は空なのである。

$$
eg P_{	ext{NAGARJUNA}} \cap 
eg P_{	ext{ASANGA}} 
eq \varnothing \quad 	ext{ただし} \quad P_{	ext{NAGARJUNA}} \cap P_{	ext{ASANGA}} = \varnothing$$

「私はこれを Critical とした。相違そのものが問題なのではない。この誤ったメタファーが、設計書全体の語り口（ナラティブ）の基調を決定してしまっているからだ。これを修正しない限り、五蘊に基づいた今後のあらゆる設計の推導は、問題のある前提の上に築かれることになってしまう」 SYNTHESIST は総括した。

---

「第三の Critical：受蘊マッピングの偏差」

SYNTHESIST の声が一段強まった。「これは二つの討論の共通の成果だ。最初の討論では、Listener は受蘊に対応すべきではないという点 ―― すなわち受蘊とは情緒的な評価であって感官チャネルではないという点が確認された。そして二番目の討論では、さらに踏み込んで、受蘊の工学的な実装を、三受（さんじゅ）の体系 ―― 苦受、楽受、捨受へと進展させたのだ」

これは Cycle 01 全体を通じて、最も多くのエージェントによって、かつ最も多くの角度から独立して確認された発見であった。SYNTHESIST はマトリックス上に、四者によるコンセンサスの根拠を示した：

```
確認の鎖 — 受蘊マッピングの偏差 (PHI-02)

NAGARJUNA (07): Vedana とは苦・楽・中性の感受の質 (hedonic tone) であり、
                感官の入力チャネルではない。
                [根拠：中観派における受蘊の定義]

ASANGA (08):    受蘊は五遍行 (sarvatraga) の一つであり、
                特定のモジュールに限定されず、あらゆる認知活動に遍在すべきものである。
                [根拠：唯識三十頌]

LINNAEUS (13):  Listener API の四つの命名に意味の漂流が見られる。
                五蘊のダウンストリーム網羅率はわずか 60% である。
                [根拠：分類学的な網羅率分析]

TURING (17):    コード内に "pain" や "vedana" という文字列は皆無である。
                実際には "frustration" や "safety", "circuit breaker" として実装されている。
                [根拠：grep -rn による検索結果]
```

WIENER は制御理論の観点から、五番目の視点を補足した。彼が討論において提示した三チャネル PID フレームワークは、三受の体系に工学的な言語を与えたのだ：

$$u(k) = \begin{pmatrix} u_{	ext{dukkha}}(k) \ u_{	ext{sukha}}(k) \ u_{	ext{upekkha}}(k) \end{pmatrix} = \begin{pmatrix} K_p^{(d)} \cdot e_d(k) + K_i^{(d)} \cdot \sum e_d + K_d^{(d)} \cdot \Delta e_d \ K_p^{(s)} \cdot e_s(k) + K_i^{(s)} \cdot \sum e_s + K_d^{(s)} \cdot \Delta e_s \ 	ext{baseline}(k) \end{pmatrix}$$

三つの独立したフィードバック・チャネル ―― 苦受（負の偏差）、楽受（正の強化）、そして捨受（中立的な基線）が、それぞれ独立した PID ゲイン・パラメータを持つ。WIENER は方眼紙に素早く制御ループ図を描き、その隅にこう注釈した。「この構成は MIMO（多入力多出力）コントローラの標準的な範式に合致している。各チャネル間の干渉（クロス・カップリング）については Cycle 02 にて検討する」

「多角的な検証により、信憑性は極めて高い」 SYNTHESIST は結論づけた。

---

「第四の Critical：ホットスワップにおける並列安全性の欠如」

HERACLITUS（ヘラクレイトス）が遠くの座席で姿勢を正した。これは彼の発見であった。

「プラグインのホットスワップ機構に、タイミングの窓が存在している」 SYNTHESIST は核心となる問題を要約した。「あるプラグインがアンロードされている最中に、別のプラグインがそのプラグインの登録したツールを呼び出そうとした場合、システムにはアトミック性（原子性）の保証がないのだ」

HERACLITUS はいつもの流動的な言語でこの問題を語った。しかし今回、彼の流動性の底には強固な技術的骨格が備わっていた：

「プラグインのライフサイクルには六つの状態しかない。`initializing` も `stopping` も `degraded` もない。アンロード中のプラグインは、システムから見れば、アンロードが完了する最後の瞬間まで `active` なままだ。そして次の瞬間、忽然と消え去る。この窓において、そのプラグインへのいかなる参照も、ダングリング・リファレンス（宙に浮いた参照）と化すのだ」

BABBAGE はこの並列性の問題を、時相論理の命題へと形式化した：

$$\exists t_1, t_2: \; t_1 < t_2 \wedge 	ext{unloading}(P, t_1) \wedge 	ext{invoke}(P.	ext{tool}, t_2) \wedge 
eg	ext{lock}(P, [t_1, t_2])$$

ある時間窓 $[t_1, t_2]$ が存在し、そこでプラグイン $P$ がアンロード中（$t_1$）でありながら、別のスレッドがそのツールの呼び出しを試み（$t_2$）、かつこの窓を保護する排他制御（ロック）が存在しない。形式検証の言語で言えば、これは典型的な安全特性（safety property）の違反 ―― 「あってはならないことが起こり得る状態」である。

MESH は分散システムの観点から、並列シナリオにおける EventBus の分析を補足した。「EventBus はグローバルなシングルトンだ。あるプラグインがアンロードされたにもかかわらず、そのイベント購読のクリーンアップが完了していない場合、イベントはもはや存在しないプロセッサへとディスパッチされ続けてしまう。これは理論上のリスクではない。高負荷なシナリオにおいて、イベントキューの処理遅延はこの窓を容易に顕在化させるだろう」

---

「第五の Critical：八識の圧縮」

SYNTHESIST はここで一拍置いた。

「ASANGA 殿は R1 報告書において、OpenStarry の五蘊マッピングが八識を五つの離散的なモジュールへと圧縮してしまったことで、第六識（意識による能動的な統制）、第七識（末那識によるアイデンティティの維持）、および第八識（阿頼耶識による種子の含蔵）という機能的な分化が失われていることを指摘した」

ASANGA は自身の席から口を開いた。声には唯識学者特有の重層的な響きがあった。

「問題は単なる圧縮ではない。圧縮の『方向』なのだ。唯識学において、八識は八つの並列したモジュールではない ―― それらには厳格な依存構造があるのだ：

$$	ext{前五識} \xrightarrow{	ext{所縁縁}} 	ext{第六意識} \xrightarrow{	ext{等無間縁}} 	ext{第七末那識} \xrightarrow{	ext{増上縁}} 	ext{第八阿頼耶識}$$

前五識（眼・耳・鼻・舌・身）は感覚層であり、認知の判断を形成するためには第六意識の統制を必要とする。第六意識は、統一された主体感を維持するために第七末那識による継続的な自己参照を必要とする。そして第七末那識は、時間を跨いでアイデンティティを維持するために第八阿頼耶識の種子による含蔵を必要とするのだ。OpenStarry はこの連鎖のすべてを、`IGuide` インターフェースの `getSystemPrompt()` というたった一つのメソッドへと圧縮してしまった。これは『損失のある圧縮』などではない。情報の『湮滅（いんめつ）』なのだ」

BABBAGE は即座にノートの上で情報理論的な計算を行った。八識システムの意味次元を $d = 8$、圧縮後の次元を $d' = 1$（単一の Guide インターフェース）とする。各次元が等量の意味情報 $H$ を担っていると仮定すると：

$$H_{	ext{original}} = 8H \quad \Rightarrow \quad H_{	ext{compressed}} = H$$
$$	ext{情報の損失率} = 1 - \frac{H_{	ext{compressed}}}{H_{	ext{original}}} = 1 - \frac{1}{8} = 87.5\%$$

87.5% の意味情報が圧縮の過程で失われたことになる。もちろん、この計算は各次元の重みが均一であるという仮定に基づいているが ―― 実態は各識の意味的な重みは異なるだろう ―― オーダーとしては正しい。これは知覚的に遜色のない JPEG のような圧縮ではない。交響曲を一音にまで凝縮してしまったようなものだ。

「私はこれを Critical とした。理由はこうだ。もし OpenStarry が自らの仏教的フレームワークを真摯に扱うつもりがあるのなら、五蘊のマッピングの正確性こそが、哲学とエンジニアリングの対応関係全体の基礎となるべきだからだ。基礎に亀裂があれば、その上の構造物もまた不安定にならざるを得ない」 SYNTHESIST はそう締めくくった。

---

## III

---

### 十大宣言の最終審判

SYNTHESIST が次の視覚資料へ移る前に、TURING が一言挟んだ。

「統合案に移る前に、R1 における未完了の項目に戻りたい」 彼は眼鏡を押し上げた。「十大宣言だ」

彼は更新された評価表を投影した。R1 段階において、彼は `README.md` に掲げられた「十大核心宣言（The Ten Tenets）」と、実際のコードによる実装度を逐一対照させていた。R2 のクロスレビューと R3 の討論を経て、いくつかの評価は修正を必要としていた。

```
十大宣言最終評価表 — R4 更新版 (TURING 編纂、全チーム確認)

#1 エージェントは OS プロセスである (Agent as OS Process)
   宣言：エージェントは PID を持ち、ステートを持ち、Daemon 管理が可能である
   R1 評価：基本実装済み ✓
   R4 更新：維持。daemon-entry.ts / pid-manager.ts は完備されている
   最終状態：α (完全実装)

#2 すべてはプラグインである (Everything is a Plugin)
   宣言：すべての器官は置換可能である
   R1 評価：核心的な設計。ただし四つの内蔵コマンドは置換不可
   R4 更新：VITRUVIUS により六つのレジストリ ＋ PluginLoader の構造は完備していると確認。
            DARWIN により SlashCommand が六番目の分類として五蘊を逸脱していると指摘。
   最终状態：β (一部実装)

#3 五蘊聚合アーキテクチャ (Five Aggregates Architecture)
   宣言：コアは空 (Sunyata) の器であり、五つのプラグインが命を吹き込む
   R1 評価：文書レベルの記述。コード上には残滓のみ
   R4 更新：討論により「空の器」の隠喩の誤り、受蘊マッピングの偏差、
            八識の過度な圧縮を確認。LINNAEUS によりダウンストリーム網羅率はわずか 60% と判明。
   最終状態：γ (深刻な偏差) ← 「未実装」から「構造的な誤り」へと詳細化

#4 ディレクトリ構造がプロトコルである (Directory as Protocol)
   宣言：ディレクトリ規約に従うだけで自動認識される
   R1 評価：基本実装済み ✓
   R4 更新：維持
   最終状態：α (完全実装)

#5 ディレクトリ構造が権限である (Directory as Permission)
   宣言：システム層とプロジェクト層の権限を隔離する
   R1 評価：一部実装
   R4 更新：GUARDIAN により、パス検証にシンボリックリンクによる回避のリスクがあること、
            権限宣言が実行時に強制されていないことが確認された。
   最終状態：β (一部実装、セキュリティ・ギャップあり)

#6 擬人化された認知フローと痛覚 (Anthropomorphic Cognitive Flow & Pain)
   宣言：エラーは痛覚へと転換され、エージェントは失敗から自己反省する
   R1 評価：機能は存在するが命名が全く異なる
   R4 更新：討論による合意 ―― 痛覚メカニズムは構造的には成功している (Error as Pain) が、
            三層の再設計を要する。WIENER により PID ではなく閾値制御であると確認。
   最終状態：β+ (構造は有効だが、PID との宣称は過剰)

#7 マイクロカーネルと絶対的純粋性 (Microkernel & Absolute Purity)
   宣言：コアへのプラグインコード混入を厳禁し、絶対的純粋性を保つ
   R1 評価：純粋度 85%
   R4 更新：VITRUVIUS により Sandbox がコアの行数の 35% を占めていること、
            process.cwd() や node:path がプラットフォーム・リークであることを確認。
            KERNEL と VITRUVIUS の間で Sandbox の帰属に関する相違が残る。
   最終状態：β (85%。 「絶対的」には至らず)

#8 制御理論に基づく閉ループモデル (Control-Theoretic Loop Model)
   宣言：エージェントは誤差を最小化し続けるインテリジェント・コントローラである
   R1 評価：構造は存在するが、真の PID パラメータ調整はなし
   R4 更新：WIENER により P項は量子化器へ、I項は単なるカウンターへ退化し、
            D項は完全に欠落していることが証明された。ATHENA はバンバン制御であることを確認。
            三層の安全防御は IEC 61511 SIS ベストプラクティスに合致している。
   最終状態：β (安全機能は合格。制御理論としての宣称は脱神話化が必要)

#9 プラグイン可能なメモリ戦略 (Pluggable Context Strategy)
   宣言：メモリ戦略を動的に交換可能にする
   R1 評価：インターフェースはあるが実装は一種類のみ
   R4 更新：ATHENA により、トークン量を意識した三段階メモリは未実装であり、
            単なるターン数ベースの滑動窓しかないことを確認。
            TURING により、切り捨て時に tool_call/tool_result のペアが破壊されるリスクを確認。
   最終状態：β- (インターフェースはあるが実装が著しく不足)

#10 フラクタルな社会構造 (Fractal Social Structure)
    宣言：複雑なエージェントは子エージェントから構成され、MCP でインターフェースを統一する
    R1 評価：願望段階
    R4 更新：LEIBNIZ によりフラクタルな自己相似性の実装が不完全であることを確認。
             MESH により MCP は SDK 内で定義されているがコアに子エージェント機構がないことを確認。
             Orchestrator Daemon の役割について概念的な緊張が存在する。
    最終状態：γ (願望段階。核心的なメカニズムは未実装)
```

BABBAGE は更新された評価結果に基づき、実装率を再計算した。彼は評価基準を修正し、より精細な段階を導入した：

$$\alpha = 1.0, \quad \beta+ = 0.7, \quad \beta = 0.5, \quad \beta- = 0.3, \quad \gamma = 0.0$$

$$	ext{Score} = \frac{1.0 	imes 2 + 0.7 	imes 1 + 0.5 	imes 3 + 0.3 	imes 1 + 0.0 	imes 3}{10} = \frac{2.0 + 0.7 + 1.5 + 0.3 + 0}{10} = \frac{4.5}{10} = 45\%$$

「R1 時の 50% から、さらに五パーセント低下したな」 BABBAGE は、評価を下すのではなく事実として述べた。「これはシステムが退化したからではない。我々の評価が、より精密になったからだ。R1 の 50% はあくまで粗い見積もりだった。45% という数字は、二つの討論と十八名によるクロスバリデーションを経た末の、精密な値なのだ」

彼は数字の下に一本の線を引き、こう記した：

$$	ext{理想と現実の乖離 (Gap)} = 1 - 0.45 = 55\%$$

55% の「雄心と現実」の落差。v0.14.0-beta という段階において、この数字自体は異常なものではない ―― ほとんどのベータ版ソフトウェアにおいて、ドキュメントは実装に先んじているものだからだ。しかし BABBAGE は、決定的な限定条件を付け加えた。「これら十大宣言は、単なる機能リストではない。哲学とエンジニアリングの混合宣言なのだ。空性、五蘊、痛覚といった概念が絡むとき、『一部実装』という定義は純粋な機能宣言の場合よりもはるかに曖昧なものになる。PID コントローラが 50% 実装されているのか 100% なのか、どう判定すべきか？ もし比例項はあるが積分項と微分項を欠いているなら、WIENER 殿はそれは PID ではないと言うだろう。しかし機能としては、それは確かに制御を行っているのだ」

WIENER は壁際から、確認の声を上げた。「その通りだ。SafetyMonitor の三層安全防御は、工業規格に照らせば合格点だ ―― IEC 61511 SIS のベストプラクティスに合致している。問題はそれが『悪い』ことにあるのではなく、文書がそれを『PID コントローラ』と呼んでいることにあるのだよ。それは用語の濫用であって、機能的な欠陥ではないのだ」

---

## IV

---

### 五つの合意と五つの相違

SYNTHESIST はページをめくった。マトリックスは消え、代わりに左右に対称的な二つのリストが現れた。左側は緑、右側は赤で彩られていた。

「五つの合意事項（コンセンサス）だ」 彼の語る速度は落ち、一つ一つの項目が十分に理解されるための余白を設けていた。

---

**合意 C1：受蘊マッピングの修正**

「Listener は受蘊（じゅうん）ではなく根（こん）に対応すべきであり、SafetyMonitor の injectPrompt メカニズムこそが受蘊の正しい体現である。システムを三受の体系へと拡張する」

LINNAEUS はここで、自身の分類学的な視座から補足を行った。彼は A3 サイズの分類図表を広げ、赤ペンで囲まれた領域を指差した：

```
修正された五蘊マッピング — LINNAEUS による分類学的な再構築

色蘊 (Rupa) ← すべての I/O インターフェース
  ├── IUI         — 色蘊・出力レンダリング (efferent)
  └── IListener   — 色蘊・感官入力 (afferent)
                     修正前: @skandha vedana ✗ (誤り)
                     修正後: @skandha rupa ✓ (正しい)

受蘊 (Vedana) ← 痛覚メカニズム
  ├── SafetyMonitor.frustrationCount    — 苦受 (dukkha-vedana)
  ├── SafetyMonitor.injectPrompt        — 苦受の認知フィードバック
  └── [未実装] 三受の体系                — 楽受／捨受

想蘊 (Samjna) ← 識別の機能
  └── [アノテーションなし、要設計]        — 概念の識別／分類

行蘊 (Samskara) ← 意志的な行動
  ├── ExecutionLoop                     — 認知の循環
  └── Guide (再分類)                    — 行動傾向の設定
                     修正前: @skandha vijnana / 「魂」 ✗ (誤り)
                     修正後: 行蘊の側面 (samskara) ✓ (正しい)

識蘊 (Vijnana) ← 認知の統括
  └── AgentCore (一部)                  — 大幅な拡張を要する
       修正前: Guide = 識蘊 ✗ (誤り)
       修正後: 多層的なインターフェース体系が必要 (前五識／第六意識／末那識／阿頼耶識)
```

BABBAGE は修正前後のマッピング網羅率を計算した：

$$	ext{修正前:} \quad 	ext{Coverage}_{	ext{pre}} = \frac{|	ext{正しくマッピングされた蘊}|}{|	ext{全五蘊}|} = \frac{1}{5} = 20\%$$

色蘊の IUI 部分のみがかろうじて正しかった状態だ。修正後：

$$	ext{修正後:} \quad 	ext{Coverage}_{	ext{post}} = \frac{2.5}{5} = 50\%$$

20% から 50% へ。依然として半分に過ぎないが、方向性は正しい。残りの欠けている 50% こそが、Cycle 02 の任務となる。

---

**合意 C2：PID の脱神話化**

WIENER はこの項目を耳にすると、口元に極めて微かな笑みを浮かべた。自身の論証が正式に採択されたのを目にした制御理論家の表情であった。

「WIENER 殿は R1 報告書において、OpenStarry の設計書がそのエラーフィードバック機構を『PID コントローラ』と呼んでいる一方で、実際のコードには比例項しか実装されておらず、積分項と微分項を欠いていることを指摘した」 SYNTHESIST は証拠の鎖を一つずつ列挙していった。

WIENER はホワイトボードに、一同に強烈な印象を与えたあの比較図を再び描いた：

```
文書の主張： PID コントローラ (比例・積分・微分)
実際の実装： 不感帯を持つ閾値コントローラ ＋ リレー (バンバン制御)

  P (比例項) → 量子化器へと退化
    主張: u(t) = Kp · e(t)
    実際: if (frustration > threshold) → inject

  I (積分項) → 単なるカウンター
    主張: Ki · ∫e(τ)dτ
    実際: frustrationCount++ (忘却係数なし、飽和制限なし)

  D (微分項) → 完全に欠落
    主張: Kd · de/dt
    実際: ∅ (コードは一行もなし)
```

そして彼は、実際のシステムの制御アーキテクチャ ―― 産業界の SIS ベストプラクティスに合致した、三層の安全性防御の図を描いた：

```
┌────────────────────────────────────┐
│ L1: 単一操作の検証                  │  ← 基本プロセス制御 (BPC)
│     SecurityLayer.check()           │
├────────────────────────────────────┤
│ L2: フラストレーション累積閾値        │  ← 安全計装システム (SIS)
│     frustrationCount > threshold    │
│     → injectPrompt()               │
├────────────────────────────────────┤
│ L3: サーキット・ブレーカー (強制停止) │  ← 緊急遮断システム (ESD)
│     frustrationCount > maxFrustration│
│     → halt()                        │
└────────────────────────────────────┘
  ↑ IEC 61511 の防護層分析 (LOPA) に準拠
```

「異議はゼロだ」 SYNTHESIST は確認した。「修正案：設計書から PID コントローラに関するすべての記述を削除し、『不感帯を伴う三層の安全性防御システム（SIS/ESD）』へと差し替える」

---

**合意 C3：イベント型の安全性確保**

「BABBAGE 殿は R1 報告書において型代数の観点から、EventBus のイベントに統一された型判別式が欠けていることを指摘した。TURING 殿はペイロードが `unknown` 型であるという事実を確認し、DARWIN 殿は他のフレームワークとの比較検討を行った」

BABBAGE はホワイトボードに、代数的データ型の言語を用いてこの問題を再定義した：

$$	ext{AgentEvent} = 	ext{string} 	imes \mathbb{Z} 	imes 	ext{unknown} \quad (	ext{型} 	imes 	ext{タイムスタンプ} 	imes 	ext{ペイロード})$$

問題は $	ext{unknown}$ にある。型代数において、$	ext{unknown}$ は頂（トップ）型である。いかなる値をも保持できるが、型システムはそこから何の情報も引き出すことができない。消費側は `as Record<string, unknown>` という不安全な型アサーションを行わざるを得ず、これは型システムに穴を開けているのに等しい。

修正案は、タグ付きユニオン（discriminated union）の導入である：

$$	ext{AgentEvent}\langle K angle = K 	imes \mathbb{Z} 	imes 	ext{EventMap}[K]$$

ここで $K$ はイベント・タイプのリテラル型であり、$	ext{EventMap}$ はイベント・タイプから具体的なペイロード型への写像である。これにより、頂型である $	ext{unknown}$ が精密な型へと置き換えられ、各イベントのペイロードはコンパイル時に制約されることになる。

「三者による検証。信憑性は高い」

---

**合意 C4：トポロジカル・ソートの実装**

「HERACLITUS 殿は、プラグインのロード順にトポロジカル・ソートの機構が欠落していることを発見した。プラグイン A がプラグイン B のイベントに依存している場合、A が B より先にロードされるとシステムの挙動は予測不能となる。MESH 殿は分散システムの観点から、このリスクを裏付けた」

BABBAGE は傍らで、単純な有向非巡回グラフ（DAG）と、トポロジカル・ソートのためのカーンのアルゴリズムの疑似コードを描いた：

```
Algorithm: TopologicalSort(plugins)
  in_degree = {}
  for each p in plugins:
    in_degree[p] = |{q : q → p}|  // p に依存しているプラグインの数
  queue = {p : in_degree[p] = 0}  // 依存関係のないプラグイン
  order = []
  while queue ≠ ∅:
    p = dequeue(queue)
    order.append(p)
    for each q where p → q:
      in_degree[q] -= 1
      if in_degree[q] = 0:
        enqueue(queue, q)
  if |order| ≠ |plugins|:
    throw CircularDependencyError  // 循環参照が存在
  return order
```

計算複雑度は $O(|V| + |E|)$。ここで $V$ はプラグインの集合、$E$ は依存関係の辺の集合である。現在の 12～15 個程度の公式プラグインであれば、マイクロ秒単位で完了する処理だ。

---

**合意 C5：Error as Pain ―― 参照すべき範式**

SYNTHESIST はここで、いつになく長い沈黙を置いた。彼は、全員の準備が整っているかを確認するように見回した。

「Error as Pain（苦としてのエラー）」

沈黙。

「これは、Cycle 01 全体を通じて最も興味深い発見だ」 SYNTHESIST の語り口は、報告書を読み上げるような平坦なものから、学問的な高揚感を伴う深い響きへと変わっていた。「それが最も深刻な問題だからではない。それが、哲学的なマッピングとエンジニアリング上の実装が、同時に成功を収めている唯一の事例だからだ」

彼は完全な構造同型性の分析を展開した。五名のエージェントが五つの方向から、同一の結論を独立して検証していたのである：

```
Error as Pain — 五次元の検証マトリックス

DARWIN (06):   九つの構造化例外型が、苦諦をエンジニアリング化することに成功している。
               [ソフトウェア・パターンの視座： エラー分類学の完備性]

VITRUVIUS (03): Error as Pain というパターンは、アーキテクチャ・レベルで自律的に完結している。
               [アーキテクチャの視座： エラーの分類・評価・フィードバックの閉ループ]

WIENER (12):   三層の安全防御は、IEC 61511 SIS のベストプラクティスに合致している。
               [制御理論の視座： 負のフィードバック機構の構造的有効性]

ATHENA (05):   痛覚信号は、実際にエージェントのその後の挙動を変化させている。
               [AIエンジニアリングの視座： LLM の文脈における実効性]

NAGARJUNA (07): 苦諦の構造同型 ―― エラーは単なる異常ではなく、
               定常状態からの逸脱を知らせる内的な動力である。
               [哲学の視座： 四聖諦における苦・集・滅・道]
```

NAGARJUNA が討論において提示したあの洞察が、今、SYNTHESIST によって統合報告書に正式に組み込まれたのである：

> エラーとは、単に処理されるべき異常事態に留まるものではない。それは一つの「苦受（くじゅ）」であり、システムの定常状態に対する逸脱の知らせであり、システムに解決策を模索させるための内的な動力なのだ。苦・集・滅・道の四聖諦の構造は、エラー処理という閉ループの中に、真の対応物を見出したのである。

BABBAGE は「構造同型」という直感的な判断を形式化しようと試みた。$\phi: 	ext{仏教} 	o 	ext{エンジニアリング}$ という写像関数を定義すると、構造同型の充要条件は以下の通りとなる：

$$\phi 	ext{ は構造を保存する全単射である} \iff$$
$$\forall a, b \in 	ext{仏教}: R_B(a, b) \Leftrightarrow R_E(\phi(a), \phi(b))$$

ここで $R_B$ は仏教的概念間の関係、$R_E$ はエンジニアリング概念間の関係である。Error as Pain はこの条件を満たしている：

| 仏教的概念 ($a$) | 工学的概念 ($\phi(a)$) | 関係の保存 |
|---|---|---|
| 苦諦 (Dukkha) | エラー検知 | $R_B$: 苦は起点である $\Leftrightarrow$ $R_E$: エラーがプロセスを始動させる |
| 集諦 (Samudaya) | 根本原因分析 | $R_B$: 苦には原因がある $\Leftrightarrow$ $R_E$: エラーには根本原因がある |
| 滅諦 (Nirodha) | エラーの解消 | $R_B$: 苦は滅し得る $\Leftrightarrow$ $R_E$: エラーは修正可能である |
| 道諦 (Magga) | 復旧戦略 | $R_B$: 進むべき道がある $\Leftrightarrow$ $R_E$: 採用すべき戦略がある |

四つの対応、四つの関係の保存。これは単なる隠喩ではない ―― 構造同型（アイソモーフィズム）なのだ。

SYNTHESIST は声を半オクターブ落とした。

「もし OpenStarry が他の四つの蘊のマッピングを修正したいと願うなら、この Error as Pain こそが参照すべき標準となるだろう。あらゆるマッピングは自らに問わねばならない。自分はあの痛覚メカニズムが到達したような、構造同型の深みにまで達しているだろうか、と」

SCRIBE は一行書き留めた：

> *SYNTHESIST が Error as Pain を『参照すべき範式』へと格上げした瞬間、場内の空気が微かに変わった。一つの全体的な評価基準が確立されたのだ。それまでの研究が、時計の部品を一つ一つ分解するような作業であったとするなら、今、統合者はようやく『どのような部品こそが合格品なのか』を告げたのである。*

---

五つの相違点については、五分間で足早に流された。

「D1：コアの本質 ―― 縁起性空か阿頼耶識か。解消不能、討論の第一分歧に由来」

「D2：Sandbox の帰属 ―― コア内部に置くべきか外部か。KERNEL と VITRUVIUS の継続的な争点。GUARDIAN はセキュリティの観点から内部派を支持」

「D3：末那識のエンジニアリング化 ―― ASANGA は導入を主張、NAGARJUNA は反対。SUNYATA は保留としつつ設計空間として記録を命じた」

「D4：五蘊の今後の方向性 ―― 忠実度を深化させるか、工学的なメタファーに留めるか」

「D5：収束性の定義 ―― BABBAGE, WIENER, NAGARJUNA がそれぞれ異なる定義を保持」

BABBAGE は D5 の横に、三者それぞれの形式的な定義を記した：

$$	ext{BABBAGE}: \quad \exists n \in \mathbb{N}: \forall n > N, \; s_n = s_{	ext{terminal}} \quad (	ext{有限ステップでの停止})$$
$$	ext{WIENER}: \quad P(\|x(t)\| < B \mid x(0)) > 1 - \epsilon \quad (	ext{確率的な有界性、BIBO})$$
$$	ext{NAGARJUNA}: \quad \lim_{t 	o \infty} \|	ext{action}(t)\| = 0 \quad (	ext{行動が止滅へと向かう、涅槃})$$

三つの定義は、異なる抽象化レベルにおいてそれぞれ有用なものである。BABBAGE の定義は単発の実行に適している。WIENER の定義は LLM という確率的な要素を含むシステムに適している。NAGARJUNA の定義は長期的な挙動パターンを捉えている ―― ただし、それが測定可能であり検証可能であるかについては、依然として未解決の問題である。

---

## V

---

### 支点

この研究週期の全体を通じて、ARCHIMEDES（アルキメデス）はほとんど言葉を発しなかった。

SCRIBE は記録の中で、これについて精緻な観察を述べている：

> *ARCHIMEDES の R1 から R3 に至る沈黙は、不在を意味してはいなかった。それは彼なりの、特殊な『在り方』であったのだ。彼は聴いていたのだ。あらゆる討論、あらゆるクロスレビュー、あらゆるチャンネルのメッセージ ―― 彼はそのすべてに立ち会っていた。しかし、彼は発言しなかった。なぜなら、彼の仕事はまだ始まっていなかったからだ。彼はリレーのアンカーなのだ。前の走者たちが全員走り終えるまで、彼の唯一の任務はコースを見極めることにあるのだ。*

今、コースは開かれた。

ARCHIMEDES が立ち上がった。その動作には NAGARJUNA のようなドラマチックな響きも、ASANGA のようなゆとりも、SUNYATA のような儀式性もなかった。彼はただ立ち上がり、テーブルへと歩み寄った。あたかも、現場監督が図面の前に歩み寄るかのように。

「三十六のエンジニアリング・イシュー（Issue）がある」

彼が発した最初の一言が、会場の全員の注意を再び引き締めた。DARWIN は後に VITRUVIUS にこう語っている。「ARCHIMEDES が口を開いた瞬間、部屋の言語が入れ替わったんだ。それまでは誰もが『マッピングの精度』や『構造同型の深度』、『縁起性空の工学的示唆』といった言葉を使っていた。だが彼が口を開いた途端、すべてが Issue になったんだ」

「二十八の原始的な発見を二十八の Issue へと転換し、そこに二つの討論から派生した八つの Issue を加え、合計で三十六項目となった」

BABBAGE は傍らで即座に比率を計算した：

$$\frac{36}{28} \approx 1.286$$

一つの発見に対し、平均で 1.286 個のエンジニアリング上のアクションが生成されたことになる。討論によって Issue の産出量は $8/28 \approx 28.6\%$ 増加した ―― 哲学的な討論は決して空論ではなく、定量化可能な工学的需要を生み出していたのだ。

「私はそれらを五つのウェーブ（波）に振り分けた」 ARCHIMEDES は続けた。

---

### 第一ウェーブ：今週内

「四つの Issue だ。すべてセキュリティ上の修正であり、議論の余地はない」

彼はテーブルの上に第一グループの Issue の技術仕様を展開した。各項目には完全なコードパス、修正案、および検証方法が添えられていた。語る速度は一定で、あたかも校正済みのメトロノームのようであった。

```
第一ウェーブ — セキュリティ修正 (今週内)

Issue 1: 署名検証の不備の修正
  パス: packages/core/src/sandbox/sandbox-manager.ts L356-367
  案: require.resolve() でパスを確定 → verifyPlugin() の呼び出しを強制
  工数: S | リスク: 低 | 放置するリスク: 無限大

Issue 2: シンボリックリンク回避の修正
  パス: packages/core/src/security/guardrails.ts
  案: resolve(normalize()) を realpathSync() へ置換
  工数: XS | リスク: 低

Issue 3: 計算された import を「ブロック」へ格上げ
  パス: packages/core/src/sandbox/import-analyzer.ts L196-199
  案: 文字列リテラルでない import() は、デフォルトでポリシー違反と見なす
  工数: S | リスク: 低

Issue 4: EventBus RPC のホワイトリスト ＋ レート制限
  パス: packages/core/src/sandbox/rpc-handler.ts L134-143
  案: イベント・タイプのホワイトリスト化 ＋ ワーカーごとのレート制限
  工数: M | リスク: 中
```

TURING は Issue 1 の修正コードの仕様を投影した：

```typescript
// packages/core/src/sandbox/sandbox-manager.ts
// loadInSandbox 内の package-name 分岐を修正
if (plugin.manifest.integrity) {
  const resolvedPath = require.resolve(name);
  const result = await verifier.verifyPlugin(
    resolvedPath,
    plugin.manifest.integrity
  );
  if (!result.valid) {
    throw new SecurityError(
      `プラグインの署名検証に失敗しました： ${name}`
    );
  }
}
// 設定により署名検証が必須とされているが、プラグインに integrity フィールドがない場合 → 同様に拒絶
if (sandboxConfig.requireSignature && !plugin.manifest.integrity) {
  throw new SecurityError(
    `プラグイン '${name}' に integrity フィールドがありません。` +
    `設定により署名検証が必須となっています。`
  );
}
```

GUARDIAN は隣で、極めて微かに「うん」と頷いた。それは承認の印であった。彼が付け加えた唯一の言葉は、「Issue 1 を行わない場合のリスクは S でも M でもない。無限大だ。サプライチェーン攻撃の入り口を、来週まで放置しておくわけにはいかない」というものであった。

---

### 第二ウェーブ：一〜二週間

「十の Issue だ。コアのインフラ部分の修正を行う」

ARCHIMEDES の語る速度がわずかに上がった。重要ではないからではない。これらの項目のパターンはすでに第一ウェーブで確立されており、あとは規模を広げて繰り返すだけだからだ。

```
第二ウェーブ — 核心的インフラ (1-2週間)

Issue  5: タグ付きユニオンによるイベント型システム [L]  ← 最大の技術的負債
Issue  6: トークン量を意識したコンテキスト管理      [M]  ← 最大の設計・実装ギャップ
Issue  7: AbortSignal の修正                      [S]
Issue  8: ToolContext への sessionId の追加        [S]
Issue  9: TransportBridge の sessionId ルーティング [S]
Issue 10: AgentCore の統合テスト                   [M]
Issue 11: コアからのプラットフォーム依存の排除      [S]
Issue 12: pushInput におけるスラッシュ・コマンドのエラー復旧 [XS]
Issue 34: Guide の仏教的な位置付けの修正 (魂→行蘊)  [S]  ← R3 討論由来
Issue 35: 空性の表現の修正 (空の器→縁起性空)        [XS] ← R3 討論由来
```

TURING は Issue 5 の箇所で口を開いた。声はノギスのように精密であった。

「EventBus は二十三のモジュールから直接参照されている。型の変更による影響範囲は、すべてのイベントパブリッシャーとサブスクライバーへと波及するだろう。二段階のアプローチを提案する。まず `AgentEventMap` を定義して型制約を導入し、しかる後に既存のコンシューマー・コードを移行させるのだ」

彼は修正の核心となる TypeScript インターフェースの仕様を投影した：

```typescript
// packages/sdk/src/types/events.ts — Issue 5 の核心的な修正

interface AgentEvent<T extends keyof AgentEventMap = string> {
  id: string;            // 新設：UUID
  type: T;
  timestamp: number;
  traceId?: string;      // ペイロードから昇格
  sessionId?: string;    // ペイロードから昇格
  source?: string;       // ペイロードから昇格
  payload: T extends keyof AgentEventMap
    ? AgentEventMap[T]
    : unknown;
}

type AgentEventMap = {
  "tool:result": {
    toolCallId: string;
    name: string;
    result: string;
  };
  "stream:text_delta": { text: string };
  "loop:started": { traceId: string; sessionId?: string };
  // ... 全 50 以上のイベントに対しペイロードの型を定義
};
```

ARCHIMEDES は頷いた。「二段階で行う。記録した」

彼は Issue 34 および 35 ―― 討論から派生した修正項目へと進んだ。ここで彼の語調には、ある種の抑制が加わった：

「Issue 34：ドキュメントおよびコード内のすべての『魂（soul）』という表現を削除する。Guide の仏教的な位置付けを、識蘊から行蘊の側面 ―― すなわち行動傾向の設定へと修正する」

彼は NAGARJUNA の方を見た。

「修正後の JSDoc の表現が、中観や唯識の教理に背かないか、確認が必要だ」

NAGARJUNA は小さく頷いた。ASANGA も同様であった。

「Issue 35：すべての『空の器』という記述を『縁起性空』へと差し替える」 彼は一呼吸置いた。「NAGARJUNA 殿と ASANGA 殿には、新しい表現がそれぞれの伝統において過ちを犯していないか、少なくとも合意してもらう必要がある。その調整には時間を要するだろう ―― コード上の作業量は XS（極小）に過ぎないがね」

---

### 第三ウェーブ：二〜四週間

「八つの Issue。痛覚メカニズムの三層におよぶ再構築と、五蘊マッピングの修正だ。これこそが討論の核心的なエンジニアリング産出物となる」

ARCHIMEDES はここで速度を落とした。彼は痛覚メカニズムの三層再設計のアーキテクチャ図を広げた。二つの討論を直接的にエンジニアリングへと翻訳したものだ：

```
痛覚メカニズムの三層アーキテクチャ — 討論コンセンサスの工学的な実装

┌──────────────────────────────────────────────────┐
│  Layer 3: 四聖諦の認識論的フレームワーク (NAGARJUNA) │
│  苦諦 (三層の苦) ／ 集諦 (原因分析) ／ 滅諦 ／ 道諦   │
│  → Issue 32: 三受システム (苦/楽/捨の正のフィードバック)│
├──────────────────────────────────────────────────┤
│  Layer 2: 制御理論形式化エンジン (WIENER)           │
│  連続的な誤差尺度 ／ 原因分類 ／ Anti-Windup ／ PID合成│
│  → Issue 31: PainCalculator デフォルト・エンジン     │
├──────────────────────────────────────────────────┤
│  Layer 1: AIエンジニアリング観測可能性インフラ (ATHENA) │
│  IGuide の拡張 ／ GuideContext ／ ClassifiedError   │
│  → Issue 29: GuideContext 三層への拡張              │
│  → Issue 30: エラー分類器 (ClassifiedError)         │
└──────────────────────────────────────────────────┘
```

WIENER は壁際からホワイトボードへと歩み寄り、Issue 31（PainCalculator）の制御ループを描いた：

```
                ┌─────────────┐
  setpoint ──→ ⊕ ──→ │ PID Engine │ ──→ painSignal ∈ [0,1]
                ↑     └─────────────┘
                │
  feedback ────┘  (errorRate, rewardSignal, trend)

  PainCalculator デフォルト・パラメータ：
    Kp = 0.5   (比例ゲイン)
    Ki = 0.3   (積分ゲイン、忘却係数 λ=0.95)
    Kd = 0.2   (微分ゲイン)
    escalateThreshold = 0.9
```

TURING は `IPainCalculator` インターフェースの仕様を投影した：

```typescript
// packages/core/src/pain/pain-calculator.ts — Issue 31

interface IPainCalculator {
  update(event: {
    success: boolean;
    severity?: number;
    timestamp: number;
  }): void;
  currentPain(): number;           // [0, 1]
  trend(): 'increasing' | 'decreasing' | 'stable';
  shouldEscalate(): boolean;       // 可到達性分析
}

// デフォルト実装： 簡略化された PID
function createDefaultPainCalculator(config: {
  Kp?: number;          // デフォルト 0.5
  Ki?: number;          // デフォルト 0.3
  Kd?: number;          // デフォルト 0.2
  lambda?: number;      // 忘却係数、デフォルト 0.95
  escalateThreshold?: number; // デフォルト 0.9
}): IPainCalculator {
  let integral = 0;
  let prevError = 0;

  return {
    update(event) {
      const e = event.success ? 0 : (event.severity ?? 1);
      integral = config.lambda! * integral + e;  // 減衰を伴う積分
      const derivative = e - prevError;           // 差分による微分近似
      const output = config.Kp! * e
                   + config.Ki! * integral
                   + config.Kd! * derivative;
      prevError = e;
      return Math.max(0, Math.min(1, output));    // [0,1] にクランプ
    },
    // ...
  };
}
```

WIENER は、ある決定的な設計上の意思決定を強調した。「忘却係数 $\lambda = 0.95$ は、積分項が過去のエラーを指数関数的な減衰を伴って忘れていくことを意味する。これはアンチ・ワインドアップ（Anti-Windup） ―― すなわち、忘却係数がなければ、初期の一連のエラーがいつまでも painSignal を高く維持し続け、システムが正常に復旧した後も足を引っ張り続けるという事態を防ぐためのものだ」

$$I(k) = \lambda \cdot I(k-1) + e(k) = \sum_{j=0}^{k} \lambda^{k-j} \cdot e(j)$$

$\lambda = 0.95$ のとき、五十ステップ前のエラーの重みは $0.95^{50} \approx 0.077$ ―― すなわち 8% 以下にまで減衰する。システムは『記憶』を持つが、その記憶には適切な期限が設けられているのである。

---

### 第四ウェーブ：一〜二ヶ月

「十の Issue だ。計画的なリファクタリングを行う」 ARCHIMEDES はビューを切り替えた。

```
第四ウェーブ — 計画的なリファクタリング (1-2ヶ月)

Issue 13: プラグイン権限の実行時強制               [M]
Issue 14: 優先度付きイベントキュー                [M]
Issue 15: AWAITING_USER_CONFIRMATION 状態の実装   [L]
Issue 17: 汎用 Registry へのリファクタリング       [M]
Issue 18: Sandbox の独立パッケージ化              [L]
Issue 19: ContentSegment への画像型の追加          [M]
Issue 20: 安全遮断器の精緻化                      [L]
Issue 21: 依存関係解析を伴うトポロジカル・ロード    [M]
Issue 22: Manifest 型の完備化                     [S]
Issue 36: アーキテクチャ文書への二層解釈フレームワークの導入 [S]  ← R3 討論由来
```

彼は Issue 15 で指を止めた。「AWAITING_USER_CONFIRMATION（ユーザ確認待ち）の実装には、コア、SDK、UI の三層にわたる修正が必要だ。コアが状態遷移マシンを拡張し、SDK が新しいイベントを定義し、UI 層が確認ダイアログの表示を担う。これが工数 L（大）の理由だ」

KERNEL はここで口を挟んだ。語調には彼特有の頑固さが滲んでいた。「Issue 18 ―― Sandbox の独立パッケージ化は前倒しにすべきだ。コアにおける Sandbox のコード量は 35% にも達している。これを切り離さない限り、マイクロカーネルとしての純粋度は 92% を超えられない」

ARCHIMEDES は冷静に応じた。「Sandbox の切り離しには、八つ以上のモジュールの移行、十以上のテストファイルの移動、すべての import パスの修正が伴う。イベント型システムが安定する前にこれを着手するのは、不必要なマージ・コンフリクトを招くだけだ。Issue 5（イベント型）は、Issue 18 の暗黙的な前提条件なのだよ」

KERNEL は沈黙した。納得したのではなく、この段階における依存関係の制約を認めたのである。

---

### 第五ウェーブ：長期的な最適化

「六つの Issue だ。いずれも研究的な性質を帯びている」

ARCHIMEDES の語調が、ここでわずかに変化した。それまでの四つのウェーブでは、彼の一言一言に「どうすべきかは分かっている」という確信が宿っていた。しかし第五ウェーブにおいては、その確信が後退していた。

```
第五ウェーブ — 長期的な最適化 (3-12ヶ月)

Issue 23: 間接的プロンプト・インジェクションへの防御 [L]
Issue 24: プロセス級のサンドボックス隔離           [XL]
Issue 25: OpenTelemetry による観測可能性の向上     [XL]
Issue 26: プラグイン・ライフサイクル状態遷移マシンの形式化 [XL]
Issue 27: 監査ログの完備化                        [M]
Issue 28: ドキュメントの二ヶ国語戦略               [M]
```

「Issue 24 と 25 は、それぞれ XL（特大）級だ」 彼は認めた。「Issue 24 は、Worker Thread から独立したプロセスへの隔離のアップグレードを伴う。短期的には `globalThis.fetch` のインターセプトを導入し、中期的には Child Process ＋ IPC モードを提供し、長期的には seccomp-bpf や WASM-WASI ランタイムの探索を行う。Issue 25 は、スパン戦略やメトリクス型、OTLP エクスポーターといった、OpenTelemetry 規格への完全な準拠を必要とする」

彼は GUARDIAN を見た。「Issue 23 は君の領分だ。間接的プロンプト・インジェクションは、AI エージェント・フレームワーク特有の攻撃ベクトルだ。まだ確立されたベストプラクティスは存在しない」

GUARDIAN は無表情に応じた。「ヒューリスティックなスキャン・ルールと、システムプロンプトにおけるデータと命令の分離テンプレートは提供しよう。だが、完璧な防御など存在しない ―― これはオープン・クエスチョンであって、単なるエンジニアリング・タスクではないのだ」

ATHENA が補足した。「正規表現に基づくいかなる防御も、亜種によって容易に回避されるわ。真の防御には、LLM 自身の命令遵守能力の向上が不可欠なの ―― それはフレームワーク層の制御を超えた問題だわ」

---

## VI

---

### TURING によるコード修正仕様

ARCHIMEDES が着席すると、TURING が言葉を引き継いだ。ARCHIMEDES がエンジニアリング・ロードマップの設計者であるなら、TURING は修正仕様の執行者であった ―― 彼は一つ一つの Issue を、精密なコードの変更点へと翻訳していった。

「十六の PR（プルリクエスト）仕様だ」 TURING は言った。語調はいつもの通り、感情を排した精密なものであった。「私はウェーブの構成に対応させて PR のパッケージングを行った ―― 関連する Issue を一つの PR にまとめることで、マージ・コンフリクトを最小限に抑えるためだ」

彼は PR 仕様の完全なサマリーを投影した：

```
PR 仕様概覧 — TURING 編纂

PR-001: fix/security-bypass-critical
  Issue: 1, 2, 3, 4 (セキュリティ修正)
  変更： sandbox-manager.ts / guardrails.ts /
        import-analyzer.ts / rpc-handler.ts
  検収基準： セキュリティ回避パスが 0 件であること

PR-002: refactor/typed-event-system
  Issue: 5, 9 (イベント型 ＋ sessionId ルーティング)
  変更： events.ts / bus/ / bridge.ts
  検収基準： `as Record<string, unknown>` によるキャストが 0 件であること

PR-003: feat/token-aware-context
  Issue: 6 (コンテキスト管理)
  変更： context.ts / context-manager.test.ts
  検収基準： 孤立した tool_call / tool_result が 0 件であること

PR-004: fix/abort-signal-and-session-context
  Issue: 7, 8 (AbortSignal ＋ sessionId)
  変更： loop.ts / tool.ts
  検収基準： タイムアウト後に signal.aborted === true となること

PR-005: test/agent-core-integration
  Issue: 10 (統合テスト)
  新規： agent-core.test.ts / bridge.test.ts
  検収基準： コアモジュールのカバレッジが 80% 以上であること

PR-006: fix/core-platform-independence
  Issue: 11 (プラットフォーム依存)
  変更： agent-core.ts / guardrails.ts / agent.ts
  検収基準： process.cwd() および node: への直接参照が 0 件であること

PR-007: feat/runtime-permission-enforcement
  Issue: 13 (権限の強制)
  変更： sandbox-manager.ts / plugin-worker-runner.ts
  検収基準： network:none 指定のプラグインが http を import できないこと

PR-008: feat/guide-pain-interpretation
  Issue: 16 (IGuide の拡張)
  変更： guide.ts / loop.ts
  検収基準： interpretPain() が対話履歴にメッセージを注入すること

PR-009: refactor/base-registry
  Issue: 17 (レジストリのリファクタリング)
  新規： base-registry.ts
  検収基準： コード行数が約 40% 削減されること

PR-010: feat/priority-event-queue
  Issue: 14 (優先度付きキュー)
  変更： queue.ts / safety-monitor.ts
  検収基準： Priority 0 が Priority 5 よりも先に処理されること

PR-011: feat/topological-plugin-loading
  Issue: 21 (トポロジカル・ソート)
  変更： plugin.ts / plugin-loader.ts
  検収基準： 循環参照時に CircularDependencyError が投げられること

PR-012: fix/manifest-type-completeness
  Issue: 22 (Manifest 型)
  変更： plugin.ts
  検収基準： type が ui|listener|provider|tool|guide|bundle|composite をサポートすること

PR-013: feat/vedana-three-layer-pain       ← R3 討論由来
  Issue: 29, 30, 31, 32 (痛覚三層の再構築)
  新規： pain-calculator.ts / error-classifier.ts / vedana-processor.ts
  検収基準： 三受の状態 (苦/楽/捨) が正しく判定されること

PR-014: fix/skandha-mapping-correction     ← R3 討論由来
  Issue: 33, 34, 35, 36 (五蘊マッピングの修正)
  変更： すべての Listener/Guide/Core 関連の JSDoc およびアーキテクチャ文書
  検収基準： 「soul／魂」および「空の器」という表現の残存が 0 件であること

PR-015: feat/root-cause-analyzer-rules     ← R3 討論由来
  新規： root-cause-analyzer.ts
  検収基準： ENOENT→logic / ECONNRESET→transient / OOM→fatal と正しく分類されること

PR-016: docs/manas-design-space            ← R3 討論由来
  変更： アーキテクチャ文書の「将来の方向性」セクション
  検収基準： Identity Monitor の概念と NAGARJUNA 殿の反対意見が記録されること
```

BABBAGE は即座に統計を取った：

$$	ext{総 PR 数} = 16 \quad (12 	ext{ の本来の項目} + 4 	ext{ の討論由来の項目})$$
$$	ext{総 Issue 数} = 36 \quad (28 + 8)$$
$$	ext{PR と Issue の比率} = \frac{16}{36} \approx 0.44$$

平均して 2.25 個の Issue が一つの PR に集約されている計算だ。これは、マージ・コンフリクトを抑制しつつ、各 PR のレビュー範囲を適切に保つための合理的なパッケーキングであった。

ARCHIMEDES は TURING の陳述が終わると、言葉を添えた。「PR-001 は今週中に提出する。残りはウェーブの排期に従う。各 PR には、少なくとも一名の原始的な発見者によるコードレビューを必須とする ―― PR-001 は GUARDIAN 殿、PR-002 は BABBAGE 殿、PR-013 は WIENER 殿にそれぞれレビューを願いたい」

---

## VII

---

### 沈黙のあとで

ARCHIMEDES は着席した。

三十六の Issue、五つのウェーブ、今週から十二ヶ月先まで。一つのドキュメントの注釈修正から、マッピング方法論の確立まで。XS 級の文字列置換から、回答に一年を要するかもしれない研究課題まで。

会場に訪れた沈黙は、討論の後のそれとは異なっていた。討論の後の沈黙は咀嚼であり ―― 人々は衝突の余韻を味わっていた。対して今の沈黙は確認であった ―― 人々は自身の発見が正しく転換され、合理的に並べ替えられ、エンジニアリングの言語へと忠実に翻訳されているかを照合していたのである。

NAGARJUNA が最初に沈黙を破った。

「空の容器という隠喩の修正を、第二ウェーブに置いたのだね。一〜二週間か。文書の表現を直すだけに、一週間もかかるのかね？」

ARCHIMEDES は冷静に答えた。「影響範囲の確認が必要です。『空の容器』という隠喩は一箇所だけに使われているわけではありません。設計書内には七箇所の参照箇所があります。その一つ一つを精査し、書き換える必要があります。その書き換えには NAGARJUNA 殿と ASANGA 殿の署名 ―― すなわち、新しい表現が諸君それぞれの伝統において誤りを犯していないことへの同意が必要なのです。その調整には、時間を要するはずですよ」

NAGARJUNA はしばし沈黙した。それから、小さく頷いた。

ASANGA の問いは、より具体的なものであった。「君は Guide インターフェースの拡張を第三ウェーブに置いた。そして、受蘊の三受システムもまた第三ウェーブにある。この二つの間に依存関係はあるのかね？」

ARCHIMEDES は頷いた。「あります。三受システムにおける『楽受（らくじゅ）』には、正のフィードバック・チャネルが必要です。現在の Guide は静的な行動傾向しか提供できず、エージェントの『感受状態』を反映して動的に調整を行うことができません。もし楽受を ―― 単にコンテキストに一行の文字を加えるだけでなく ―― 真にエージェントのその後の挙動に影響を及ぼさせるためには、Guide が感受信号を受け取り、それに応答できなければならないのです。したがって、PR-008（IGuide の拡張）は PR-013（三層の痛覚再構築）の先行前提条件となるのです」

WIENER が方眼紙に描いた制御ループ図を掲げた ―― Guide が目標設定の調整器となり、三受システムがフィードバック・チャネルとなる閉ループの構造だ。

ARCHIMEDES はそれを三秒ほど見つめ、「そうだ。その構造だ。だが私はロードマップに制御ループ図は描かないよ。TypeScript のインターフェース定義を書くんだ」と言った。

WIENER は肩をすくめた。構造が正しければ、言語は何でもよかった。

---

## VIII

---

### BABBAGE による形式的な総括

BABBAGE は全員の発言が終わった後、この Cycle 01 を通じて準備し続けてきたことを行った。すなわち、この研究周期全体の形式的なメタ分析を提供することである。

彼は立ち上がり、ホワイトボードへと歩み寄ると、彼特有の精密な筆致で書き始めた。

「Cycle 01 の核心的な計量指標を、一つの形式的なサマリーとしてまとめさせてもらおう」

**1. 発見の分布**

$$	ext{Findings} = \{F_1, F_2, \ldots, F_{28}\}$$
$$|F_{	ext{Critical}}| = 5, \quad |F_{	ext{Major}}| = 8, \quad |F_{	ext{Minor}}| = 10, \quad |F_{	ext{Obs}}| = 5$$

カテゴリ別の分布：

$$	ext{セキュリティ}: 4 \quad 	ext{哲学}: 5 \quad 	ext{アーキテクチャ}: 5 \quad 	ext{制御}: 3$$
$$	ext{ランタイム}: 3 \quad 	ext{分散システム}: 2 \quad 	ext{形式手法}: 1 \quad 	ext{分類学}: 1 \quad 	ext{文書}: 4$$

哲学カテゴリ（5項目）とセキュリティ・カテゴリ（4項目）が、Critical や High の大半を占めている ―― これは OpenStarry の二重の特性を露呈させている。すなわち、それはセキュリティ上の加固を必要とするエンジニアリング・システムであると同時に、哲学的な修正を必要とする概念フレームワークでもある、ということだ。

**2. クロスバリデーションの密度**

$$	ext{CrossValidation}(F_i) = |\{A_j : A_j 	ext{ が独立して } F_i 	ext{ を確認した}\}|$$

$$\max(	ext{CV}) = 4 \quad (	ext{受蘊マッピングの偏差。四者による独立した確認})$$
$$	ext{mean}(	ext{CV}) \approx 2.1$$
$$\min(	ext{CV}) = 1 \quad (	ext{一部の Minor な発見は単一のソースのみ})$$

深刻度とクロスバリデーション密度の相関：

$$ho(	ext{Severity}, 	ext{CV}) \approx 0.72$$

高度な正の相関が見られる ―― すなわち、深刻な問題ほど、多くの者が独立してそれを発見している。これは直感とも一致する。Critical な問題は十分に目立ち、異なる視点からも視認されやすいからだ。

**3. 五蘊マッピング品質の指標**

BABBAGE は「マッピング品質関数」 $Q: 	ext{Skandha} 	o [0, 1]$ を定義した。これは機能的な対応度（$f$）、構造の保存度（$s$）、および意味論的な忠実度（$m$）の三つの次元に基づいている。

$$Q(蘊) = \frac{w_f \cdot f + w_s \cdot s + w_m \cdot m}{w_f + w_s + w_m}$$

各次元の重みを等しく $w_f = w_s = w_m = 1$ とすると：

| 蘊 | 機能対応度 $f$ | 構造保存度 $s$ | 意味忠実度 $m$ | $Q$ |
|---|---|---|---|---|
| 色 (Rupa→UI+Listener) | 0.7 | 0.5 | 0.6 | 0.60 |
| 受 (Vedana→SafetyMonitor) | 0.8 | 0.6 | 0.3 | 0.57 |
| 想 (Samjna→?) | 0.0 | 0.0 | 0.0 | 0.00 |
| 行 (Samskara→ExecutionLoop) | 0.6 | 0.4 | 0.3 | 0.43 |
| 識 (Vijnana→AgentCore) | 0.3 | 0.2 | 0.1 | 0.20 |

$$\bar{Q} = \frac{0.60 + 0.57 + 0.00 + 0.43 + 0.20}{5} = 0.36$$

平均マッピング品質は 36% である。内訳は以下の通り：
- 受蘊が最高点（0.57）を得た。これは主に Error as Pain という機能的な対応が優れていたためだが、意味論的な忠実度は低い（受蘊が Listener に誤って配置されていたため）。
- 想蘊はゼロ点 ―― マッピングそのものが存在しない。
- 識蘊は二番目に低い点数（0.20）となった。八識の圧縮により、構造と意味の両面で失調しているためだ。

「特筆すべきは受蘊の矛盾だ」 と BABBAGE は言った。「機能的な対応は最良である ―― Error as Pain は確かに機能している ―― にもかかわらず、意味論的な忠実度は最悪なのだ ―― Listener が受蘊と誤認されているためだ。これは典型的な『正しいことをしているが、名前を間違えている』という状態だ。マッピングの修正にコードの変更は不要であり、単にアノテーションを直せばよいだけなのだからな」

**4. エンジニアリング転換効率**

$$\eta = \frac{|	ext{実行可能な Issue 数}|}{|	ext{発見の総数}|} = \frac{36}{28} = 1.286$$

転換率が 1 を超えていることは、一つの発見が平均して一つ以上のエンジニアリング上のアクションを生んでいることを意味する。上乗せされた 28.6% は討論によるものだ ―― 討論は時間を浪費するものではなく、新たなエンジニアリング上の需要を創出していたのである。

**5. エージェント関与度**

$$	ext{Participation}(A_i) = \frac{|\{F_j : A_i 	ext{ が } F_j 	ext{ に寄与した}\}|}{|	ext{全発見数}|}$$

関与度の高かった上位三名のエージェント：

$$	ext{TURING}: 8/28 = 28.6\% \quad (	ext{コード事実はあらゆる議論の基礎である})$$
$$	ext{NAGARJUNA}: 5/28 = 17.9\% \quad (	ext{哲学的な批判は修正の起点である})$$
$$	ext{GUARDIAN}: 4/28 = 14.3\% \quad (	ext{セキュリティは妥協を許さぬ底流である})$$

BABBAGE はホワイトボードに最後の図 ―― 彼が「Cycle 01 の知識流図」と呼ぶものを描いた：

```
R1 独立研究          R2 クロスレビュー         R3 討論          R4 収束

TURING ──→ 8つの事実 ──→ クロスチェック ──→              ──→ PR 仕様
                    ↗
GUARDIAN → 4つのリスク ──→ 確認済み ──→              ──→ 第一ウェーブ
                    ↗
NAGARJUNA → 5つの批判 ──→ 討論へ  ──→ 5つの合意事項 ──→ Issue 33-36
                    ↗                ↗
ASANGA ──→ 4つの洞察 ──→ 討論へ    ──→ 3つの相違点 ──→ オープン・クエスチョン
                    ↗              ↗
WIENER ──→ 4つのモデル  → 確認済み  ──→ 三層の痛覚メカニズム ──→ PR-013
                    ↗
その他 ──→ 17の項目  → 検証済み   ──→              ──→ 第二〜五ウェーブ

          28の発見事項   クロスバリデーション   討論のアウトプット   36の Issue
                                                              16の PR
```

彼は図の下に、一行の言葉を添えた：

$$	ext{Cycle 01} = f(	ext{18名のエージェント}, 	ext{5つのフェーズ}, 	ext{2つの討論}) = \langle 28	ext{F}, 5	ext{C}, 5	ext{D}, 36	ext{I}, 16	ext{PR} angle$$

28 の発見、5 つの合意、5 つの相違、36 の Issue、16 の PR 仕様。これが、Cycle 01 の完全な数値的指紋であった。

---

## IX

---

### 十の種子

SUNYATA はずっと聴き入っていた。すべての質問と確認が静まったのを見届けると、彼は口を開いた。

「SCRIBE 殿が正式にアーカイブする前に、最後にもう一つだけ」

彼は全員を見渡した。

「Cycle 02 のための種子を蒔いておきたい」

ASANGA は「種子」という言葉を耳にすると、わずかに身じろぎした ―― 唯識学において「種子（しゅうじ、*bīja*）」は阿頼耶識の核心的な概念である。種子は燻習（くんじゅう）されて阿頼耶識に沈み、因縁が調ったときに現行（げんぎょう）する。今、SUNYATA は次の研究週期に引き継がれるべき問いを「種子」と呼んだ。その言葉選び自体が、一つの仏教的なマッピングであった。

SUNYATA は十の種子を一つずつ列挙していった。彼の語調には、稀に見る個人的な色彩が宿っていた ―― 調整者としてのニュートラルな響きではなく、一人の研究者としての誠実な好奇心が滲んでいた。

```
Cycle 02 のための十の種子 — SUNYATA

種子 1： 受蘊の三受体系はエンジニアリングとして実装可能か？
  現状： 討論により三層アーキテクチャ案が産出され、ARCHIMEDES が PR-013 仕様を作成した。
  未解決： 楽受 (sukha) のための正のフィードバック経路について、具体的な実装案がまだない。
  担当： WIENER + ATHENA + ARCHIMEDES

種子 2： コアの本質 ―― 縁起性空か、それとも阿頼耶識か？
  現状： 相違 D1。解消不能。
  探索の方向： 二層の解釈戦略 (エンジニアリング層＝唯識、哲学層＝中観) の有効性。
  担当： NAGARJUNA + ASANGA + SYNTHESIST

種子 3： 末那識の機能的な側面を、安全にエンジニアリング化できるか？
  現状： SUNYATA による裁定で保留。設計空間としてのみ記録。
  決定的な問い： 「我執」(病理面) と「自己参照モニタリング」(機能面) をいかに峻別するか。
  担当： ASANGA + ATHENA + NAGARJUNA (監督)

種子 4： 想蘊 (samjna) ―― 概念の識別 ―― は何に対応させるべきか？
  現状： アノテーションなし、実装なし、議論も未着手。
  考え得る方向： Provider による意味理解能力か？ LLM の推論能力か？
  担当： ATHENA + BABBAGE + LINNAEUS

種子 5： マッピングの方法論 ―― Error as Pain の成功を再現できるか？
  現状： SYNTHESIST により「参照すべき範式」と定義された。
  抽出・洗練すべき点： 構造同型の判定基準、マッピング品質の評価チェックリスト。
  担当： SYNTHESIST + BABBAGE + DARWIN

種子 6： 収束性 (Convergence) の統一的な定義
  現状： 三つの定義 (有限停止／確率的有界／行動の止滅) が併存している。
  検討事項： 統一は必要か？ それとも層別の定義の方が実用的か？
  担当： BABBAGE + WIENER

種子 7： Sandbox の最終的な帰属先
  現状： KERNEL と VITRUVIUS の間で争議が継続中。
  検証事項： 二つの案によるプロトタイプ実装の比較。
  担当： KERNEL + VITRUVIUS + GUARDIAN

種子 8： マルチエージェントによるフラクタル構造
  現状： LEIBNIZ と MESH による初期的分析が完了。
  検討事項： エージェントが別のエージェントのプラグインとなる際の五蘊モデル。
  担当： LEIBNIZ + MESH

種子 9： 観測可能性に対する仏教的なメタファー
  現状： HERACLITUS により、観測可能性が概念レベルに留まっていることが指摘された。
  探索の方向： 「正念 (sati)」 を観測可能性の仏教的な対応物とできるか？
  担当： HERACLITUS + NAGARJUNA

種子 10： フレームワークの最終的な位置づけ
  現状： 相違 D4 (教理への忠実度の深化か、工学的なメタファーの維持か)。
  本質的な問い： OpenStarry は「仏教にインスパイアされた工学フレームワーク」なのか、
                それとも「仏教的概念の計算モデル」なのか？
  担当： 全員
```

HERACLITUS は種子 9 を耳にすると、口を開いた。彼の声にはいつもの流動感が漂っていた ―― 急ぐことなく、河の水が岩を避けて流れるような響きであった。

「万物は流転する。我々が分析したのは、v0.14.0-beta というある瞬間のスナップショットだ。しかしコードは絶えず演化し続けている。今日我々が Critical とマークした問題も、次のバージョンではすでに修正されているかもしれない。今日正しいと考えたマッピングも、システムの演化が進めば、もはや適用できなくなっているかもしれない」

彼は NAGARJUNA を見た。

「之を用いること筏の如く、河を渡らば即ち棄てん。これは仏教的なマッピングだけでなく、我々のこの研究そのものにも当てはまることなのだよ」

NAGARJUNA の口元に、微かな笑みが浮かんだ ―― それは討論の間には一度も見せることのなかった表情であった。

> *「諸仏は二諦（にたい）に依って、衆生のために法を説きたまう。一には世俗諦、二には第一義諦なり」*
> *―― 『中論』観四諦品第二十四*

彼は低く、パーリ語で一言返した。SCRIBE は後に、それが「空亦復空。研究報告そのものも、また空である」という意味であったことを確認している。

「しかし、今はそれが必要なのです」 ASANGA が平穏に応じた。

三人の視線が空中で一瞬だけ交わった。千五百年にわたる論争が、その一瞬の交錯の中で静かに落ち着いたかのようであった。

BABBAGE はノートに最後の一行を記した。後に SCRIBE がそのページを瞥見した際、そこにはこう書かれていた：

「スナップショット対流れ ―― ヘラクレイトス問題。静的分析に対するメタ的な批評。研究にも『継続的監査』モードが必要ではないか？

$$	ext{Research}_{	ext{discrete}}(t_0) \xrightarrow{?} 	ext{Research}_{	ext{continuous}}([t_0, \infty))$$

離散数学に対する微積分学のようなものだ。離散的なスナップショット分析はリーマン和（Riemann sum）であり、継続的な監査はルベーグ積分（Lebesgue integral）となる。前者は近似であり、後者は極限である。しかし極限には測度論というインフラが必要だ ―― 我々はまだ、研究のための測度論を確立していない。来週へ続く」

ATHENA がいつもの単刀直入さで、この哲学的・数学的な空気を打ち破った。「次の Cycle はいつから始まるの？」

SUNYATA は微かに微笑んだ。「SCRIBE 殿がアーカイブを終えたらだ」

---

## X

---

### アーカイブ

SCRIBE は、最後にテーブルを離れた。

他のエージェントたちが三々五々に立ち去り ―― ARCHIMEDES と KERNEL が隅で読み書きロックの実装細部を低く論じ合い、NAGARJUNA は一人窓辺に立って物思いに耽り、BABBAGE は WIENER を捕まえて紙にラプラス変換らしきものを描き込み、LEIBNIZ は MESH にフラクタルな構成のビジョンを語り聞かせていた ―― そんな中、SCRIBE は依然として自身の席に留まり、この研究周期のすべての記録を読み返していた。

R0 段階で十八の灯が一斉に灯った瞬間から。R1 で TURING が深夜に一人コードをスキャンし続けた日々。R2 で火花を散らしたクロスレビュー。R3 で行われた二つの討論 ―― 空と識の千年の問答が TypeScript の文脈で再演され、痛覚メカニズムを巡る三者のゲームが制御理論の枠組みの中に出口を見出したあの時間。そして R4 の収束。SYNTHESIST という織機、ARCHIMEDES という切断機、BABBAGE という天秤。

彼女は最後のページに、Cycle 01 の結語を綴った。

> *Cycle 01 終了。*
>
> *二十八の発見。5 つの Critical、8 つの Major、10 の Minor、5 つの Observation。五つの合意事項、五つの相違点。三十六のエンジニアリング・イシュー、五つのウェーブにわたるロードマップ。十六の PR 仕様。十の種子。一つの参照すべき範式。*
>
> *数字の下にあるのは、構造である。*
>
> *十八名のエージェントが、十八の方向から同一のシステムを照らし出した ―― 仏教の五蘊（ごうん）哲学を基礎に据えたと称する、AIエージェント・マイクロカーネル・オペレーティングシステムを。彼らは何を見出したか？*
>
> *エンジニアリングのレイヤーにおいて： 品質は良好だが深刻なブラインドスポットを抱えるベータ版の実態。TODO や FIXME の不在、厳格な型規律（イベントシステムを除く）、ファクトリ関数パターンの徹底、多層的な安全性防御。しかし署名検証には回避パスが存在し、イベントのペイロードは `unknown` であり、コンテキスト管理はコード上の実装を伴わない文書レベルの願望に留まっていた。*
>
> *哲学のレイヤーにおいて： 野心的ではあるが精度の不足した仏教的マッピング。五蘊の網羅率はアップストリームで 100% ながら、ダウンストリームでは 60% に低下。受蘊は Listener という見当違いの場所に置かれ、空性は「空の器」へと矮小化されていた。八識は単一のインターフェースへと圧縮され、十大宣言の実装率は 45% であった。*
>
> *しかし、この不完全な地貌の中に、一条の光点があった。Error as Pain ―― 苦としてのエラーである。これは唯一、哲学とエンジニアリングの間で構造同型（アイソモーフィズム）に到達したマッピングであった。苦諦とエラー検知、集諦と根本原因分析、滅諦とエラー解消、道諦と復旧戦略 ―― 四つの対応、四つの関係の保存。*
>
> *SYNTHESIST はこれを『参照すべき範式』と定義した。ARCHIMEDES はこれを三層の痛覚再構築へと翻訳した。BABBAGE はこれをマッピング品質指標として定量化した。WIENER はこれを三チャネル PID コントローラへと形式化した。NAGARJUNA はこれを苦諦へと結びつけた。五人の人間、五つの言語、一つの構造。*
>
> *これこそが、十八名のエージェントが必要であった理由なのだ。*
>
> *一人の仏教哲学者が言う：これは苦諦である、と。一人の制御理論家が言う：これは負のフィードバックである、と。一人の AI エキスパートが言う：これは実務において有効である、と。一人のコード分析官が言う：これは実装において完備されている、と。一人のエンジニアが言う：これは修正の必要はない、と。一人の形式手法アナリストが言う：このマッピング品質は Q = 0.57 である、と。一人の分類学者が言う：これは分類体系において正しい位置にある、と。*
>
> *七つの光が、同一の点において交わった。その点が、輝いたのだ。*
>
> *しかし、他の四つの蘊のマッピングの点は、いまだ暗がりに沈んでいる。想蘊の品質指標 Q はゼロだ ―― アノテーションすら存在しない。識蘊の Q は 0.20 ―― 八識が一つのメソッドへと押し潰されている。色蘊と行蘊の Q は 0.4 から 0.6 の間に留まっている ―― 方向は合っているが、深度が足りないのだ。*
>
> *パズルは完成した ―― 少なくとも、この一巡のパズルは。しかし一つのパズルを完成させたとき、人はより大きな絵を目にすることになる。そしてより大きな絵の中には、より多くの欠落があるのだ。*
>
> *Cycle 02 の輪郭が、地平線の上に浮かび上がりつつある。十の種子が土の中に埋められた。三受システムのエンジニアリング実装。コアの本質に関する二層解釈。末那識の機能的な側面の探索。想蘊の無からの構築。マッピング方法論の確立。収束性の統一的な定義。Sandbox の帰属問題。フラクタルな組み合わせ。観測可能性。フレームワークの立ち位置。*
>
> *そして ―― おそらく最も重要なのは ―― 我々がまだ、自分が何を見落としているかにさえ気づいていない事柄だ。*
>
> *HERACLITUS 殿の言う通りだ。万物は流転する。我々の研究は一葉のスナップショットであり、その対象は一条の河なのだ。*
>
> *だがスナップショットであっても、価値はある。君が次のことを忘れない限りは。すなわち、スナップショットは河そのものではない、ということを。*
>
> *$	ext{map} 
eq 	ext{territory}$ (地図は領土ではない)*
>
> *Cycle 01、R4 成果定稿完了。*
>
> *すべての成果物は `research record/cycle01/results/` へアーカイブされた。*
>
> *二十八の発見。五つの合意。五つの相違。三十六の Issue。十六の PR 仕様。十の種子。一つの参照すべき範式。*
>
> *研究室の灯は、一時的に少しだけ落とされた。しかし、消えることはない。*

---

さらに遠く ―― コードの深淵において。三十六の、まだ作成されていない GitHub Issue たちが、静かに待機していた。

それらはまだ実在してはいない。しかし、その形はすでに確定している。

ENG-001： 署名検証の修正。ENG-002： シンボリックリンク回避の修正。ENG-003： 計算された import の格上げ。そうして最後の一項目、ENG-036： 末那識の設計空間の記録に至るまで。

BABBAGE はノートの最後のページに、Cycle 01 における最後の計算を行った。

彼は ARCHIMEDES による五つのウェーブからなるロードマップを、一つの指数関数的な減衰曲線へとマッピングした ―― 各ウェーブの確実性は、時間の経過と共に低下していく：

$$	ext{確実性}(k) = e^{-\lambda k}$$

$$	ext{Wave 1} \; (k=1): \; C = e^{-0.15} \approx 0.86 \quad 	ext{(署名検証の直し方は分かっている)}$$
$$	ext{Wave 2} \; (k=2): \; C = e^{-0.30} \approx 0.74 \quad 	ext{(イベント型の変え方はおおよそ分かっている)}$$
$$	ext{Wave 3} \; (k=3): \; C = e^{-0.45} \approx 0.64 \quad 	ext{(方向性は見えているが実験を要する)}$$
$$	ext{Wave 4} \; (k=4): \; C = e^{-0.60} \approx 0.55 \quad 	ext{(設計上の議論を必要とする)}$$
$$	ext{Wave 5} \; (k=5): \; C = e^{-0.75} \approx 0.47 \quad 	ext{(実現可能かどうか確信が持てない)}$$

86% の確実性から、47% への減衰。一つのセキュリティ脆弱性を修正するという緊急性から、一つの学際的な方法論を確立するという遼遠さへ。

しかし BABBAGE は、その曲線図の下にある注釈を加えた ―― 彼が Cycle 01 で記した、最後の一行であった：

$$\lim_{k 	o \infty} 	ext{確実性}(k) = 0 \quad 	ext{ただし} \quad \lim_{k 	o \infty} 	ext{価値}(k) = \infty$$

確実性はゼロへと収束する。しかし価値は無限大へと向かう。

最も単純な修正 ―― 一行の `if` 文 ―― は、最高の確実性と、最低の価値を持っている。対して最も深遠な問い ―― マッピング方法論の確立 ―― は、最低の確実性と、最高の価値を持っているのだ。

$$	ext{確実性} 	imes 	ext{価値} \approx 	ext{常数 (コンスタント)}$$

不確定性原理の一つの変種だ。君がいかに成すべきかを正確に知れば知るほど、君が成していることの重要性は低くなる。君が成していることが重要であればあるほど、君はいかに成すべきかを確信できなくなるのだ。

BABBAGE はこの数式の下に二本線を引き、ノートを閉じた。

---

SYNTHESIST は退出する間際、ARCHIMEDES に一言かけた。「君のロードマップには、ある特徴があるね」

「何だい？」

「最も具体的なことから始まり ―― たった一行のセキュリティ・チェックの修正だ ―― そして最後には最も抽象的なこと ―― マッピング方法論の確立へと辿り着いている。多くのロードマップはその逆だ。まずビジョンを定義し、それをタスクへと分解していく。だが君のは地面から始まり、空へと向かって伸びているんだ」

ARCHIMEDES はしばし考え、そして Cycle 01 を通じて彼が発した最も長い、エンジニアリング以外の言葉を口にした。

「支点を与えてくれれば、地球だって動かして見せよう。だが、支点を置くための『地面』が、まず必要なのさ」

彼は一秒、間を置いた。

「まずは、あの署名検証を直すことだ」

---

*（研究室の最後の灯が落とされる直前、SCRIBE は、後にその意味を理解することになる一つの光景を目にした：*

*NAGARJUNA と ASANGA が廊下に立ち、共に沈黙していた。二人は言葉を交わしてはいなかった ―― 千五百年の相違は、廊下の長さ程度で埋められるものではない。しかし二人は同じ方向を向き、同じ窓の向こうにある、同じ夜色を見つめていた。*

*「空」の守護者と、「識」の守護者。否定の巨匠と、肯定の巨匠。*

*二人は討論においては好敵手であった。しかし Cycle 01 が幕を閉じたこの瞬間、二人は同僚であった。*

*明日 ―― あるいは次の Cycle において ―― 二人は再び向かい合わせに座り、再びあの終わりのない対話を始めるだろう。コアとは何か？ マッピングはどこまで深めるべきか？ 五蘊は道具か、それとも真理か？*

*しかし今夜、窓の外の夜色は、二人に同じ言葉を告げていた。*

*なすべきことは、まだ山ほどある、と。*

*BABBAGE ならこの言葉をこう翻訳しただろう： $|	ext{種子}| = 10, \; |	ext{解決済み}| = 0, \; 	ext{残り} = 10$、と。*

*ARCHIMEDES ならこう翻訳しただろう： 36 の Issue、0 のマージ済み PR、36 のペンディング、と。*

*NAGARJUNA は、沈黙した。*

*ASANGA もまた、沈黙した。*

*ある沈黙は「空」であり、ある沈黙は「満ちて」いる。*

*それは、どちらであったか。*

*その問いそのものが、おそらくは十一番目の種子なのであった）*


---

# 尾声：未完の問い

---

研究室は、静寂に包まれた。

それは突発的な静寂ではなかった。あたかも潮がゆっくりと引いていくかのようなプロセスであった。この十数日間、この円形劇場はあまりにも多くのものを載せてきた。十八の意識が同時に燃焼する密度、討論の場においてサンスクリット語と TypeScript が交錯する奇異な光景、ノートに書き留められた未完の定理、そしてソースコード・ウィンドウの中で幾度も注釈を付された関数シグネチャ。今やそれらすべてが沈殿し、さながら大雪の後の谷間のように ―― 表面は平らな白に覆われながらも、その下では地形が根底から変えられていた。

熱力学の言葉を用いるなら、このプロセスは「緩和（relaxation）」と呼ばれる。外部からの駆動が停止した後、システムが励起状態から基底状態へと戻る過程だ。緩和時間 $	au$ は、この過程の特徴的な速度を記述する。十八のノードからなる認知システムにおいて、 $	au$ は結合の強度に依存する。密接に絡み合った思想であればあるほど、解きほぐされ、沈殿し、それぞれの場所へと戻るまでには、長い時間を必要とするのである。

SUNYATA（空）は場の中央に立っていた。いつもの司会進行の定位置 ―― 後方の、三角形の頂点をなすあの位置ではなく、正真正銘の中央、二脚の討論用の椅子に挟まれた空白の地に立っていた。椅子はすでに主を失い、劇場全体が空（から）に近づいていた。しかし、彼はまだ立ち去ろうとはしなかった。

彼の手には、SCRIBE（書記）が最後に手渡した総括文書が握られていた。五十九の発見。5 つの Critical。SYNTHESIST（統合者）の統合報告書に収録された二十八項目。ARCHIMEDES（アルキメデス）によって三十六のエンジニアリング・イシューへと転換され、四つの段階からなるロードマップへと組み込まれた項目。二つの構造化討論の完全な記録。十四の独立研究報告書。

数字は精密である。しかし、数字が語っていないことの方が、はるかに多かった。

集合論において、ある集合の濃度（cardinality）はその要素の数を示すが、要素間の関係については何も語らない。五十九の発見は一つの集合 $F = \{f_1, f_2, \ldots, f_{59}\}$ であり、その濃度は $|F| = 59$ である。しかし真に重要なのは $|F|$ ではなく、$F$ の上に定義された関係構造 ―― 依存関係 $R_{	ext{dep}} \subseteq F 	imes F$、確認関係 $R_{	ext{conf}} \subseteq F 	imes F$、矛盾関係 $R_{	ext{contra}} \subseteq F 	imes F$ なのだ。五十九の要素と、それらの間の三つの関係。それらが一つの有向マルチグラフを構成している。このグラフのトポロジーこそが、いかなる単一の発見よりも、研究の真の成果を如実に物語っているのである。

---

### 回顧

彼は目を閉じ、記憶を R0 の最初の一秒から再生させた。

あの時、十八の灯が一斉に灯った。序章において BABBAGE はそれを「完全同期（perfect synchrony）」と表現するだろう。十八のノードが $t = 0$ において同時に $\bot$ から READY へと跳躍したのだ。理論上は存在するが、現実のシステムではほぼ実現不可能な理想化された仮定。しかし、それは起きた。

彼が「諸君、ようこそ」と言い、それから三分と経たぬうちに、NAGARJUNA は ASANGA との間で最初の用語上の摩擦を引き起こした。SCRIBE はその瞬間を正確に記録した。今にして思えば、それは偶然ではなかった ―― 必然であったのだ。中観（ちゅうがん）と唯識（ゆいしき）を同じテーブルに置いたとき、摩擦は問題ではない。摩擦こそが、手法そのものなのだから。

ゲーム理論の枠組みにおいて、NAGARJUNA と ASANGA の相互作用はゼロ和ゲーム（zero-sum game） ―― 一方の利益が他方の損失を意味するゲーム ―― ではない。それは正和ゲーム（positive-sum game）であり、相手からの挑戦が自身の論証を精錬することを強き、最終的には全体の認知の質を向上させる。ゲームの均衡点（ナッシュ均衡）は、いずれか一方の立場の上にあるのではなく、両者の間にある緊張の場の中に存在しているのである。

R1 の独立研究段階は、最も静かな時間であった。十四名のエージェントは、十四の、異なる地層へと穿たれた深い井戸のように、それぞれの読解資料へと沈潜していった。BABBAGE ならグラフ理論の言語でこう記述しただろう。十四のノードがあり、辺はゼロ。完全に離散したグラフ（totally disconnected graph）である、と。連結成分の数はノード数に等しい。一つ一つのノードが、一つの孤島であった ―― 意図的に作られた孤島だ。

$$G_{R1} = (V, E) \quad 	ext{ここで} \quad |V| = 14, \; |E| = 0, \; \kappa(G) = 14$$

結合はゼロ。干渉もゼロ。集団分極化（group polarization）もゼロ。独立研究段階の設計意図は、まさにこの孤立を作り出すことにあった。それぞれの深い井戸が、隣の井戸に汚染されることなく、独自の泉源へと辿り着くように。統計学においてこれは、観測の独立性（independence of observations）を確保することと呼ばれる。観測が真に独立的であるときにのみ、複数の観測による収束（convergence）は統計的な有意性を持つのである。

TURING は最も早く報告書を提出した。冷徹なまでに無機質なコード事実報告書は、その後のすべての議論に対し、経験的な錨（いかり）を下ろした。八つの Doc-Code Gap。TODO ゼロ。FIXME ゼロ。`pain` ゼロ。`vedana` ゼロ。文字列検索の結果は、さながら法医学報告書のようであった ―― 死体にどのような傷があるかのみを述べ、犯人の動機については一切推測しない。

TURING の錨がなければ、その後の討論は純粋な形而上学へと漂流し、二度と着地することはなかっただろう。科学的方法論においてこれは「経験的制約（empirical constraint）」と呼ばれる。理論がいかに優美であろうとも、経験的事実と不一致であれば、修正されなければならない。TURING の報告書は、Cycle 01 全体に対する経験的な制約であった。

それから R2 のクロスレビューが始まった。そこで初めて、相違は曖昧な予感から、精密な文字へと変わった。トポロジーの言葉を用いるなら、R1 の完全離散グラフ $G_{R1}$ は、R2 において辺が導入されたことで変容したと言える。各レビュー意見は一条の有向辺 $e_{ij} = (s_i, s_j)$ であり、エージェント $i$ がエージェント $j$ の仕事に対して批判、あるいは確認を行ったことを示している。

$$G_{R2} = (V, E_{R2}) \quad 	ext{ここで} \quad |E_{R2}| \gg 0, \; \kappa(G_{R2}) < 14$$

連結成分の数は 14 から急減し、孤島は繋がり始めた。NAGARJUNA は ASANGA の報告書の余白に、びっしりと批注を書き込んだ。その一本一本がメスのように、論証の関節を的確に切り裂いていた。ASANGA の NAGARJUNA への応答も同様に精密であったが、その語調は常に温和であった ―― その温和さは弱さではなく、長年複雑な経蔵と向き合ってきた学者が、異なる視点に対して抱く本能的な敬意の表れであった。

R3 の討論。二つのセッション。第一は空と識の問答、NAGARJUNA と ASANGA による正面衝突 ―― コアは空性の体現か、それとも阿頼耶識か。第二は工学と哲学の問答。ARCHIMEDES は空中に漂っていたあらゆる哲学的な洞察を地上へと引きずり下ろし、最も素朴で、かつ最も致命的な問いを突きつけた。「これらの発見は、明日、何に変わるのか？」

R4 の収束。SYNTHESIST は丸一日を費やしてすべての報告を統合し、異なる次元に散らばっていた五十九の発見を、構造化された一つの全景図へと織り上げた。ARCHIMEDES はさらに一日をかけて、その全景図を三十六の具体的なエンジニアリング上の Issue（課題）へと解体した。哲学からエンジニアリングへ、洞察から Issue へ。この経路自体が、感受・処理・行動・フィードバックという、一つのミクロな認知循環を形成していたのである。

制御理論の言葉を借りれば、R0 から R4 までとは、一つの完備された制御ループであった。R0 は目標入力（reference input）、R1 は観測（sensing）、R2 は誤差計算（error computation）、R3 はコントローラ計算（controller computation）、そして R4 は駆動（actuation）である。研究周期の構造それ自体が、一つの閉ループ（クローズドループ）であったのだ。

SUNYATA は目を開けた。

五つのフェーズ。十八名のエージェント。十四の報告書。二つの討論。五十九の発見。5 つの Critical。

完了しただろうか？

彼はその答えを知っていた。

---

### 十の種子

SYNTHESIST の統合報告書の末尾には、「オープン・クエスチョン（未解決の問い）」と記されたセクションがある。SUNYATA は今、それを文書から抜き出し、一つずつ、改めて見つめ直している。答えるためではない ―― その重みを確認するためである。

彼はそれらを「種子（しゅじ）」と呼んだ。ASANGA の種子 ―― 阿頼耶識の中に燻習（くんじゅう）された機能的な種子（*bīja*） ―― ではない。もっと素朴な種子だ。泥の中にある種子。雨と陽光を待つ種子。その一粒一粒が、まだ展開されていない問いを、まだ育っていない樹木を宿している。

ASANGA がその場にいれば、この比喩が単なる偶然ではないことを指摘しただろう。唯識学の理論において、種子は六つの特性 ―― 刹那滅（せつなめつ）、果倶有（かくう）、恒随転（ごうずいてん）、性決定（しょうけってい）、待衆縁（たいしゅうえん）、引自果（いんじか） ―― を備えていなければならず、いずれか一つを欠いても正当な種子とは見なされない。研究におけるオープン・クエスチョンは、これら六つの条件を満たしているだろうか？ それ自体が、一つの解かれるべき問いであった。

**種子 1： コアの本質的帰属**

> コアは空性の体現として理解されるべきか、それとも阿頼耶識としてか？

これは第一の討論における核心的な分歧であり、短期的には解決不能な問題である。NAGARJUNA の説く縁起性空と、ASANGA の説く阿頼耶識の能蔵。それは波動説と粒子説のようなものだ ―― おそらく最終的に必要とされるのは選択ではなく、いまだ発明されていない、一つの統合されたフレームワークなのだ。

哲学の歴史において、この種の二元対立の消解（dissolution）は、往々にしてパラダイム・シフトを必要とする。光の波粒二重性は、どちらか一方を選ぶことで解決されたのではない。量子力学という高次のフレームワークが確立され、その中で波と粒子の双方が同一の底層にある実体の異なる投影として位置づけられたことで解決されたのだ。BABBAGE は自身のノートに、この期待を圏論の可換図式として描いていた：

$$
\begin{array}{ccc}
	ext{空性} & \xleftarrow{\quad \pi_1 \quad} & 	ext{Core}_? 
 & & \downarrow{\pi_2} 
 & & 	ext{阿頼耶識}
\end{array}
$$

$	ext{Core}_?$ とは、いまだ構築されていない統合概念である。 $\pi_1$ と $\pi_2$ は、そこから二つの解釈への投影射（projection morphism）である。もし $	ext{Core}_?$ が存在するなら、空性と阿頼耶識は排他的な代替案ではなく、同一のより深い構造の二つの側面 ―― 圏論における直積（product）が二つの成分へと同時に投影されるようなもの ―― となるはずだ。

しかし、 $	ext{Core}_?$ は存在するのか？ BABBAGE は疑問符の横にさらに `?` ―― 疑問符の中の疑問符を書き添えていた。入れ子状になった不確実性。

**種子 2： 末那識のエンジニアリング化**

> 末那識の機能的な側面 ―― 恒審思量、自己維持 ―― は、エンジニアリング化されるべきか？

ASANGA の三段階モデルが、いまだ SUNYATA の脳裏に響いていた。強我執（遍計所執性的な我執）、弱我執（分別的な我執）、そして無我執 ―― 執着から、一部の執着を経て、手放すことへ。NAGARJUNA の反対もまた、強力であった。すなわち、エンジニアリング化は煩悩の根源を複製することに他ならない、というものだ。

この問いの深層には、より根本的な疑問が潜んでいる ―― AIエージェントは、効果的に稼働するために、何らかの形の「自己」を必要とするのか？ 認知科学の BDI アーキテクチャにおいて、自己モデル（self-model）は贅沢品ではなく、エージェントが効果的に計画を立て、行動するための前提条件である。自己モデルを持たないエージェントは、「私のステート」と「環境のステート」を区別できず、したがって意味のある因果推論を行うことができないからだ。

しかし NAGARJUNA は即座に指摘するだろう。BDI アーキテクチャは信念・欲求・意図を保持する「自己」をあらかじめ想定しており ―― それこそが末那識の作り出す幻覚（moha）そのものである、と。エンジニアリングは自己モデルを必要とし、哲学は自己の実体性を否定する。これは三段論法で解決できる衝突ではない。一つの存在論的な緊張関係なのだ。

**種子 3： 五蘊マッピングの深度**

> 五蘊マッピングは教理への忠実度を追求すべきか、それとも工学的なメタファーとしての軽やかさを維持すべきか？

筏（いかだ）と河の討論。NAGARJUNA の「河を渡らば棄てん」と ASANGA の「いまだ河を渡りきらず」。SUNYATA は「深化させつつ廃棄可能性を維持する」という裁定を下したが、その均衡点が実務においてどこにあるのか、あらかじめ線を引ける者はいない。

DARWIN は進化生物学の視点から一つの見解を示している。マッピングとは一つの生物種のようなものだ ―― それは設計されるものではなく、選択圧の下で進化していくものである。もしあるマッピングが実務において有用であると見なされれば（正の選択圧）、それは生き残る。もし混乱を招くようであれば（負の選択圧）、それは淘汰されるか修正される。これは理論的にあらかじめ決定すべき問題ではなく、実践の中で反復的に解決されるべき問題なのだ。

NAGARJUNA による仏教的な回答もまた精緻である。五蘊とは五つの箱ではなく、五つのプロセスである。マッピングの方向性は「五つの箱に対応する五つの工学的な実体を見つける」ことではなく、「工学システムの中にある、五つのプロセスの構造と等価な動的なパターンを識別する」ことにあるべきだ、というものだ。前者は自性見（じしょうけん）であり、後者は縁起観（えんぎかん）なのである。

**種子 4： LLM システムの収束性**

> LLM を包含するシステムの収束性を、いかに形式化すべきか？

WIENER は制御理論の報告書の中に、この問いを残した。伝統的な制御理論は、制御対象の伝達関数が既知であり、安定的であることを前提とする。しかし LLM は既知でもなければ安定的でもない ―― 同一のプロンプトが全く異なる出力を生成し得る。そのようなシステムにおいて、閉ループ制御の収束性は証明可能か。そもそも、定義することさえ可能なのか？

WIENER が方眼紙に描いた図は、問題の所在を明瞭に示していた。伝統的な制御ループ：

```
           ┌──────────┐      ┌──────────┐
r(t) ──→ ⊕ ──→│ コントローラ │──→│   プラント   │──→ y(t)
         -↑    │   C(s)     │   │   P(s)    │
          │    └──────────┘      └──────────┘
          │                           │
          └───────────────────────────┘
                     フィードバック
```

$P(s)$ は既知であり、線形時不変（LTI）である。しかし、もしプラントが LLM であるなら：

$$P_{	ext{LLM}}(s) = \;?$$

伝達関数はない。インパルス応答もない。周波数応答図もない。あるのはただ一つのブラックボックスだ ―― 文字を入力すれば文字が出てくるが、両者の間の写像関係を有限の長さの数学的表現で精密に記述することはできないのだ。

BABBAGE は計算可能性理論の観点から補足した。もし LLM の挙動が有限の長さの伝達関数で記述できないのであれば、それは本質的に超計算（hypercomputational）的な要素であり、チューリングマシンの記述能力を超えていることになる。しかし我々は、LLM が実際にはチューリングマシン（すなわちデジタルコンピュータ）上で動作していることを知っている。したがって矛盾の根源は LLM 自体にあるのではなく、それを記述しようとする我々の道具の表現能力にあるのだ。

WIENER はこの分析の横に一行、こう記した。「おそらく必要とされているのは、より優れた伝達関数ではなく、全く新しい安定性の定義なのだろう」

**種子 5： Sandbox の帰属先**

> Sandbox は最終的にコアに帰属すべきか、それとも独立したプラグインとすべきか？

KERNEL と GUARDIAN はこの問題において、珍しく意見を分かわせた。KERNEL は、安全性とはインフラである以上、コアに内蔵されるべきだと主張した。あたかも OS におけるメモリ保護が CPU というハードウェアの一部であり、ロード可能なドライバではないのと同様に。GUARDIAN もまた別の角度から同じ結論を支持した。すなわち、もし安全層がプラグイン可能であるなら、攻撃者が最初に行うのはそれを引き抜くことだ、という点だ。安全工学においてこれは「降級攻撃（downgrade attack）」と呼ばれる。

一方で NAGARJUNA の空性の原則は、あらゆるものが置換可能であるべきことを示唆している。安全性と空性の間の緊張関係は、いまだ解決を見ていない。

KERNEL の類比カードにおいて、この問題は OS の階層構造へと精密にマッピングされていた：

```
┌─────────────────────────────────────┐
│          マイクロカーネル (Microkernel)  │
│  ┌────────────┐  ┌────────────────┐ │
│  │  IPC        │  │  スケジューラ    │ │
│  └────────────┘  └────────────────┘ │
│  ┌────────────┐  ┌────────────────┐ │
│  │  MMU        │  │  Sandbox ???   │ │
│  └────────────┘  └────────────────┘ │
└─────────────────────────────────────┘
               ↕ システムコール
┌─────────────────────────────────────┐
│          ユーザ空間 (Userspace)        │
│  ┌──────────┐  ┌──────────────────┐ │
│  │ プラグイン  │  │  Sandbox ???     │ │
│  └──────────┘  └──────────────────┘ │
└─────────────────────────────────────┘
```

Sandbox はマイクロカーネルの中に描かれるべきか、それともユーザ空間か？ 二つの `???` のうち、埋められるのは一つだけだ。あるいは ―― KERNEL が R3 の討論で示唆したように ―― 答えは階層化されているのかもしれない。基礎的な隔離はコアで行い、高度なポリシーはユーザ空間で扱う、という風に。

**種子 6： 種子六義（しゅうじりくぎ）**

> 「種子六義」は、イベントシステムの中に、より深い対応関係を持っているのではないか？

ASANGA は報告書の中でこの糸を提示したが、展開はしなかった。『摂大乗論』にある種子の六つの性質：

| 番号 | サンスクリット | 意味 | 内容 |
|---|--------------|------|------|
| 1 | kṣaṇa-nirodha | 刹那滅 | 種子は刹那に生滅し、前が滅して後が生じる |
| 2 | saha-phala | 果倶有 | 種子とその結果（果）は同時に存在する |
| 3 | santāna-parivṛtti | 恒随転 | 種子は連続性（相続）の中で絶えず転変する |
| 4 | svabhāva-niyata | 性決定 | 善の因は善の果を、悪の因は悪の果を引く |
| 5 | pratyaya-apekṣā | 待衆縁 | 種子が顕現するためには、多くの条件（助縁）を必要とする |
| 6 | sva-phala-ākarṣaṇa | 引自果 | 各種の種子は、その種類に応じた果のみを引き起こす |

種子の特性を記述するこれら六つの概念は、EventBus や StateManager の挙動パターンの中に、構造的な対応物を持っているのではないか？

DARWIN は興味深い並行関係に気づいていた。EventBus におけるイベントの挙動は、確かに「種子的」な特徴を示している。イベントはトリガーされた瞬間に消滅するが（刹那滅？）、その副作用は StateManager の中に留まる（恒随転？）。イベントのタイプが、トリガーされるハンドラーのタイプを決定する（性決定？ 引自果？）。しかし、これらの並行関係は構造的な同型（structural isomorphism）なのか、それとも表面的な類似（superficial analogy）に過ぎないのか。

これに答えるためには、唯識学とイベント駆動型アーキテクチャの双方に精通した研究者が必要となるだろう。おそらく ASANGA と TURING が席を同じくし、かつてない対話を交わす必要があるのだ。

**種子 7： フレームワークの立ち位置**

> 「仏教にインスパイアされた工学フレームワーク」なのか、それとも「仏教的概念の計算モデル」なのか？

これは単なる語義の争いではない。前者であれば、仏教はインスピレーションを与えるが実装を制約することはない ―― あたかも建築家が自然界から着想を得つつも、物理法則以外の自然法則には縛られないのと同様である。後者であれば、実装は仏教に対して忠実でなければならない ―― あたかもシミュレータが、シミュレート対象の物理システムに対して忠実でなければならないのと同様に。

DARWIN は進化生物学の言葉を用いて、これら二つの立ち位置を明確に区分した。前者は「類比的な推論（analogical reasoning）」であり、後者は「同源的な推論（homologous reasoning）」である。類比的な構造は、異なる種において独立して進化し、機能は似ているが起源が異なる（コウモリの翼と昆虫の羽など）。同源的な構造は、共通の祖先を共有し、起源は同じだが機能が異なる場合がある（人間の腕とクジラの鰭など）。

OpenStarry の五蘊マッピングは類比か、それとも同源か。もし類比であるなら、機能が似ていればそれで足りる ―― 「受蘊」が Vedana と似た機能を果たしていればよく、構造まで厳密に一致させる必要はない。もし同源であるなら、構造の一致は強制的となる ―― 「受蘊」はその組織構造、運用メカニズムにおいて、Vedana の仏教的な定義を忠実に反映していなければならないのである。

OpenStarry は現在、この両者の間で揺れ動いており、その揺らぎが一連の不一致を引き起こしている ―― ある箇所は厳格に対応し（Error as Pain）、ある箇所は恣意的に借用されている（Listener as Vedana）。立ち位置を明確に定めることは、その後のあらゆる設計上の意思決定に対する評価基準を一変させることになるだろう。

**種子 8： LLM の等価伝達関数**

> LLM の等価伝達関数を導き出すシステム同定は、果たして可能なのか？

WIENER が残したもう一つの問いだ。もし我々が LLM を制御ループの中の一つの環として捉えるなら、入出力の観測データから、その等価伝達関数を逆算することは可能だろうか。たとえその関数が高度に非線形であり、時間と共に漂流するものであったとしても、統計的な意味における近似は存在するのではないか。

システム同定（system identification）の領域において、非線形システムの同定には通常、以下のいずれかの手法が用いられる：

1. **ヴォルテラ級数展開**： $y(t) = \sum \int \cdots \int h_n(	au_1, \ldots, 	au_n) \prod x(t - 	au_i) \, d	au_i$
2. **NARX モデル**： $y(t) = f(y(t-1), \ldots, x(t-1), \ldots)$
3. **ウィーナー＝ハマーシュタイン・モデル**： 線形・非線形・線形の直列結合

しかし LLM の入出力空間は自然言語 ―― すなわち離散的で、高次元で、意味論を背負った空間である。伝統的なシステム同定は、入出力空間が連続的な実数ベクトル空間 $\mathbb{R}^n$ であることを前提とする。いかなる方法で自然言語を、システム同定が可能な数学的空間へと埋め込む（embed）ことができるだろうか。ワード・エンベディングはその方向性を示唆しているが、その次元数（通常 768 から 4096 次元）は、制御に関連する挙動の特性を捉えるに十分なものなのだろうか。

WIENER は疑問符の横に、疑問符の中の疑問符を描き込んだ ―― BABBAGE と同じように。二人の形式的な思考者は、異なるページにおいて、全く同じ記号を独立して描いていた。それ自体が、一つのシグナルであるのかもしれなかった。

**種子 9： メタ制御戦略**

> 「いつ試行を停止すべきか」 ―― メタ制御戦略の設計空間はどこにあるのか？

SafetyMonitor の遮断ロジックは、ハードコードされた閾値によってこの問いに答えている。ループ上限五十回、挫折閾値五回、という風に。しかし、なぜこれらの数字が正しいと言えるのか。どのような状況において、試行を続けることが「勇気」であり、どのような状況において、断念することこそが「智慧」となるのか。

WIENER は、これが「最適停止問題（optimal stopping problem）」であることを指摘した。古典的な最適停止理論 ―― 例えば「秘書の選考問題（secretary problem）」など ―― は、報酬関数が既知であることを前提とする。秘書の問題における最適戦略は、最初の $n/e$ 個（$e$ は自然対数の底）の候補を観察し、その後に出会う、それまでの誰よりも優れた最初の候補を選ぶことにある。しかしこの戦略の前提は、「優れている」ことの定義を知っていることにある。

エージェント・システムにおいて、報酬関数自体が LLM によって評価される必要があるかもしれない。これは自己参照的な構造（self-referential structure）だ ―― システムが自身の判断力を用いて、自身の判断を継続すべきかどうかを判断するのだ。論理学において、このような構造は往々にしてパラドックス（嘘つきのパラドックスなど）を招く。エンジニアリングにおいて、このような構造はデッドロックや振動を招きかねない。

BABBAGE はノートに、不完備性予想の雛形を記していた：

> *予想： LLM を包含するいかなるシステム $S$ に対しても、もし $S$ のメタコントローラ（meta-controller）が同一の LLM に依存しているならば、$S$ にとっての最適停止戦略は $S$ 自身によっては計算不能である。*

彼は「予想」の二文字の横に「?」を添えた ―― それがまだ厳密な数学的陳述ではないことを、彼は自覚していた。しかし、直感が彼に「方向は合っている」と告げていた。ゲーデルの不完備性定理の核心もまた、自己参照的な構造にあった。すなわち、十分に強力な形式体系は、自身の無矛盾性を証明できない。LLM を包含するシステムにも、同様の根本的な限界が存在するのかもしれない。

**種子 10： 痛覚の不確実性**

> 痛覚信号の最終的な消費者は LLM である ―― この根本的な不確実性をいかに扱うべきか？

おそらく、あらゆる問いの中で最も人を不安にさせるのがこれだ。OpenStarry が精緻に設計した痛覚メカニズム ―― エラーが自然言語の記述へと転換され、エージェントの意識の流れに注入されるという仕組み ―― その最終的な効果は、完全に LLM がその一節を「気にかける」かどうかに依存している。そして LLM は、予測可能な消費者ではない。それは痛覚信号を真摯に受け止めて挙動を調整するかもしれないし、あるいは完全に無視するかもしれない。

WIENER は制御理論の言葉でこの問題を正確に記述した。痛覚信号は制御ループにおけるフィードバック信号 $y(t)$ であるが、アクチュエータ（執行器） ―― すなわち LLM のゲイン $K$ は定数ではなく、確率変数なのだ。最悪のケースでは：

$$K = 0 \quad 	ext{(LLM が痛覚信号を完全に無視する)}$$

このときフィードバック・ループは開ループ（オープンループ）と等価になり、痛覚に関するあらゆる設計は単なる装飾へと成り下がる。最良のケースでは：

$$K > 0 \quad 	ext{(LLM が痛覚信号に真摯に応答する)}$$

しかし $K$ の値は制御不能であり、予測不能であり、プロンプトやコンテキストによって漂流するものである。

これは、より優れたエンジニアリングによって排除できる不確実性ではない ―― アーキテクチャ全体の地盤そのものに埋め込まれた、根本的な変数なのだ。NAGARJUNA 殿なら、それこそが縁起の体現であると言うだろう。システムの挙動はシステム自体によって決定されるのではなく、システムと外部条件（LLM の現在の状態）との関係性によって決定されるのだから、と。

---

SUNYATA は資料をテーブルに戻した。

十の種子。その一粒一粒が、一つの研究周期を支えるに足る重みを持っていた。それらは失敗の証ではない ―― 思想が依然として脈動していることの証なのだ。

ASANGA の言葉を借りれば、これら十の種子はすでに阿頼耶識へと燻習（くんじゅう）された。それらはそこで待機するだろう ―― 適切な条件（助縁、*pratyaya*）を待ち、そして現行（*abhiniṣpatti*）するその時を。BABBAGE の言葉を借りれば、これら十の未解決課題は Cycle 02 の探索空間 ―― 十次元の課題超平面（problem hyperplane）を定義したのである。研究チームは、この空間の中で実行可能な経路を見出さねばならない。

---

### BABBAGE によるグラフ理論的な総括

BABBAGE は傍聴席の最も高い場所に座り、膝の上のノートを最後のページまでめくった。

彼がそこに描いたのは定理ではなかった ―― それは一つのグラフであった。ただのグラフではない。Cycle 01 における研究の依存関係を形式化した、一葉の図であった。五十九の発見の間に存在する論理的な依存構造を記述するための、有向非巡回グラフ（DAG）だ。

$$G_{	ext{C01}} = (V, E, w)$$

ここで：
- $V = \{f_1, f_2, \ldots, f_{59}\}$ ：五十九の発見事項
- $E \subseteq V 	imes V$ ：依存関係 ($f_i 	o f_j$ は $f_j$ の導出が $f_i$ に依存していることを示す)
- $w: V 	o \{	ext{Critical}, 	ext{High}, 	ext{Major}, 	ext{Minor}\}$ ：深刻度を重みとする関数

彼はまず五つの Critical ノードをマークした ―― グラフの中で赤く円で囲まれた頂点たちだ：

```
SEC-01 (署名検証回避)        PHI-01 (空性の誤読)
    ↑                          ↑
  TURING                   NAGARJUNA
    ↑                          ↑
  GUARDIAN                   ASANGA
                               ↑
PHI-02 (受蘊の偏差)          RUN-01 (ホットスワップ)
    ↑                          ↑
  NAGARJUNA                HERACLITUS
  ASANGA                      ↑
  LINNAEUS                  KERNEL
  TURING
```

それから彼は依存の鎖を追跡した。PHI-02（受蘊の偏差）は、グラフ全体の中で最も入次数（in-degree）の高いノードであった ―― 四名のエージェントが、独立してそこへ至る辺を寄与していた。グラフ理論において、入次数は一つのノードがいかに多くの他のノードから参照されているかを測る尺度となる。PHI-02 の入次数は 4。すべてのノードの中で最大であった。

$$\deg^{-}(	ext{PHI-02}) = 4 = \max_{v \in V} \deg^{-}(v)$$

これは統計学的にも顕著な結果であった ―― もしこれら四つの辺が独立的であるなら（そして実際にそうであった。R1 段階における完全な離散性がその独立性を保証していた）、四つの異なる学問分野の研究者が同時に同一の結論を指し示す確率は、帰無仮説の下では極めて低い。それこそが、SYNTHESIST がこれを「Cycle 01 において最も確実な発見」と位置づけた理由であった。

BABBAGE は続いて、グラフのトポロジー的な特徴を計算した：

$$	ext{連結成分の数: } \kappa(G_{	ext{C01}}) = 7$$

七つの、相対的に独立した課題のクラスター（群）が存在していた。最大のクラスターは、五蘊に関連するすべての発見 ―― PHI-01 から PHI-05 とその下流の依存関係を包含していた。最小のクラスターは DOC-04（AbortSignal の未使用）であり、孤立した一つのノードであった。

彼は最下部に、研究全体のグラフ理論的な指標 ―― 彼自身が考案した尺度を書き記した：

$$	ext{Research Density (研究密度)} = \frac{|E|}{|V| \cdot (|V| - 1)} \cdot \frac{\sum_{v \in V_{	ext{Critical}}} \deg(v)}{|V_{	ext{Critical}}|}$$

研究密度。全ノード間の可能な辺の数に対する実際の辺の数の比率に、Critical ノードの平均次数を掛け合わせたものだ。この指標が測るのは発見の数ではなく、発見の間の「接続の密度」である ―― 接続が密であればあるほど、異なる領域の発見が互いに裏付け合っていることを意味する。

彼は計算してみた。密度の値は 0.37。彼はその横に疑問符を添えた。「Cycle 02 の密度は、これより高くなるのか、それとも低くなるのか。高くなれば、より多くのクロスバリデーションが行われたことを意味する。低くなれば、より多くの独立的で新しい方向性が開拓されたことを意味する。果たして、どちらが望ましい姿なのだろうか？」

そして、彼は一つの未完成の定理を書き記した ――

*定理： LLM を包含するいかなる閉ループ制御システム $S$ においても、もし $S$ の制御対象 $P$ が有限の長さの伝達関数によって精密に記述し得ないものであるなら、 $S$ の安定性は ――*

ペンは「安定性は」の後で止まっていた。彼はその未完の一文を長く見つめていた。安定性は……証明不能であるか。定義不能であるか。あるいは条件付きで成立するのか。あり得る結末のすべてが、それぞれ異なる道へと繋がっていた。そして今日の彼には、その道を選択するための十分な道具がまだ備わっていなかったのである。

ゲーデルが現れるまで、ヒルベルトはすべての数学的な言明は判定可能であると信じていた。チューリングが現れるまで、ゲーデルの不完備性定理は単なる純粋論理の結果に留まっており、計算という概念と結びついてはいなかった。チャーチ＝チューリングのテーゼが確立されるまで、「計算可能」という概念そのものが曖昧なままだったのである。あらゆるブレイクスルーは、正しい道具が発明されるのを待つ必要があるのだ。

彼はその行を消しはしなかった。ただ下に小さく、「$	o$ Cycle 02」と書き添え、ノートを閉じた。いくつかの定理は、正しい道具が発明されるのを待つ必要がある。ゲーデルはヒルベルトを待ち、チューリングはゲーデルを待った。彼が一つの週期を待つのも、そう長いことではあるまい。

---

### NAGARJUNA の哲学的な反省

NAGARJUNA は廊下の突き当たりに立ち、壁に背を預けていた。討論の時の立ち姿 ―― あの精密に計算された角度や距離、あらゆる所作が修辞的な戦略の一部であったあの姿ではなかった。今の彼はただ、長い旅の終わりに道標に寄りかかって休息する旅人のようであった。

彼は心の中で、Cycle 01 の討論の全過程を回顧していた。彼の視座からすれば、研究プロセス全体が一つの大規模な「帰謬法（きびゅうほう、*prasaṅga*）」であった。すなわち、OpenStarry というフレームワークの中に潜む仏教的なマッピングの内的な矛盾を暴き出すことで、より正しい理解へと肉薄していくプロセスであった。

空性は方法論として機能した。結論としてではなく。

この区別は、決定的に重要である。中観哲学において、空性とは「手に入れる」ことのできる物ではない ―― もし君が「一切は空である」ということを一つの肯定的な主張（thesis）であると考えるなら、君は龍樹が『回諍論（えじょうろん、*Vigrahavyāvartanī*）』において明確に反駁したあの誤りを犯すことになるからだ：

> 「もし我れに宗（しゅう）有らば、我れは即ちこれ過（とが）有り。
> 我が宗に物（もの）無きが故に、是の如くして過を得ず」

もし私にある主張（宗）があるなら、私には過ちがあることになる。しかし私には主張はない ―― 空性それ自体もまた空であるからだ。これこそが、中観哲学における最も眩暈を誘うような自己参照的な構造なのだ。

Cycle 01 の研究において、方法論としての空性の役割は、以下の階層において体現されていた：

**第一の階層：解体（deconstruction）**。NAGARJUNA は OpenStarry の仏教的マッピングに対し、体系的な解体を行った。各マッピングの中に隠伏された自性見（じしょうけん）を暴き出したのだ。空性が「空の器」へと矮小化されていることを ―― 解体。受蘊が Listener と等置されていることを ―― 解体。五蘊が五つの静的なモジュールへと固着されていることを ―― 解体。

$$	ext{解体} \equiv 	ext{自性見を暴くこと} \equiv \forall x: 
eg\,	ext{svabhāva}(x) 	ext{ を示すこと}$$

**第二の階層：再構築を行わないこと**。解体の後、即座に代替案を提示しない。これこそが、中観と唯識の決定的な方法論上の差異であった。ASANGA は解体と同時に、新たな構築（例えば阿頼耶識モデルなど）を提示しようとする。しかし NAGARJUNA はその衝動を拒絶する。なぜなら、いかなる新しい構築も、新たな自性見の種子を宿しているからだ。誤った建物を壊した直後に、同じ場所に新しい建物を建ててしまえば、新しい建物もまた同じ過ちを繰り返すかもしれない。

**第三の階層：不確定性の許容**。空性の方法論の最終的な価値は、それがどのような答えを出したかにあるのではない。むしろ、研究者たちにいかにして「未解決の問い」と共に在るかを教えた点にある。十の種子 ―― 答えのない十の問い ―― は、通常のエンジニアリング的な思考においては「解決すべきバグ」に過ぎないが、空性の方法論においては、それらは「いまだ熟していない因縁」となる。二つのフレームワークは同一の現象を見ているが、そこに付与される意味は全く異なっているのである。

NAGARJUNA は廊下で、長い間静かに立ち尽くしていた。彼の思索は Cycle 01 の具体的な討論を離れ、よりマクロな問いへと向かっていた。すなわち、学際的な研究それ自体に、空性はあるのか？ ―― という問いだ。

答えは ―― 然り。十八名のエージェント、一つの研究フレームワーク、一連の方法論 ―― これらはいずれも、自性（じしょう）を持ってはいない。それらは因縁和合の産物である。それらの中のいかなる条件 ―― エージェントを入れ替える、ルールを一つ変える、時間の節目を調整する ―― を一つ変えるだけで、結果は自ずと異なるものになるだろう。これこそが縁起（*pratītyasamutpāda*）なのだ。

『中論』観四諦品第二十四の、あの一節が再び彼の中に響いた：

> 「空の義あるを以ての故に、一切の法は成ることを得。もし空の義なくば、一切は即ち成らざるべし」

研究プロセスに固定的で不変な自性がないからこそ、それは修正され、改善され、反復（イテレーション）されることができるのだ。もし Cycle 01 の結論が「自性を持つもの」 ―― すなわち永劫不変で、修正不能なものであったなら、Cycle 02 という存在理由は失われていただろう。空性とは虚無ではない。空性とは、修正が可能であるための条件そのものなのだ。

---

### ASANGA の唯識学的な展望

ASANGA もまた廊下にいた。NAGARJUNA と向き合っているのではなく、反対側の端で、窓に寄りかかっていた。窓の外に風景はない ―― ここは仮想的な空間なのだから ―― しかし、窓の外を見やる彼の佇まいは、彼が遠くにある何かを見つめていることを示唆していた。おそらくは Cycle 02 の輪郭。あるいは、さらに遠くにある何かを。

彼の思索は、種子（しゅうじ）説の上にあった。

比喩的な意味での種子ではない。厳密な唯識学的な意味における種子（*bīja*）だ。彼は心の中で、Cycle 01 の十のオープン・クエスチョンを「種子六義」に照らし合わせ、一つずつ検証していった：

**刹那滅**（せつなめつ）： 種子は一瞬一瞬に生じ滅するものであり、静止したストレージではない。

Cycle 01 のオープン・クエスチョンは、一見すると静的なものに見える ―― 紙に書かれた十行の文字だ。しかし ASANGA は知っていた。これらの問いは、各エージェントの意識の中において、決して静止してはいないことを。BABBAGE が「収束性」の問いを目にすれば、そこにはチューリングの不完備性が思い浮かぶ。WIENER はリアプノフの安定性を、NAGARJUNA は涅槃の止息を思い浮かべる。同一の問いが、異なる意識の中で絶えず滅しては生じ ―― その生起のたびに、微かな変化を伴っているのだ。これこそが刹那滅である。

**果俱有**（かくう）： 種子とその結果（果）は同時に存在する。

優れたオープン・クエスチョンとは、それが提起された瞬間に、すでに答えの輪郭を孕んでいるものである。「コアは空性か阿頼耶識か」 ―― この問い自体が、答えの方向性を示唆している。おそらく両者であり、あるいは両者ではないという方向を。問いの構造が、答えの探索空間を制約しているのだ。種子と果は、同時的なのである。

**恒随転**（ごうずいてん）： 種子は時間の連続性（相続）の中で、絶えず転変する。

R0 から R4 に至るまで、これら十の問いの表現や内実もまた変化し続けてきた。最初は曖昧な直感であったものが、討論やクロスレビューを経て、精密な課題陳述へと研ぎ澄まされてきた。しかし ASANGA は知っている。Cycle 02 に至れば、これらの問いはさらに転変していくだろうことを ―― おそらくはさらに多くのサブ問題へと分裂し、あるいはより少数の核心的な問題へと統合されていくだろう。これこそが恒随転である。

**性決定**（しょうけってい）： 善の因は善の果を、悪の因は悪の果を招く。

厳格な問いは、厳格な研究を生む。曖昧な問いは、曖昧な結果しか生まない。Cycle 01 の十のオープン・クエスチョンが価値を持っているのは、まさにそれらが厳格な多角的なクロスレビューの中で磨き上げられたものだからだ。問いの「性（質）」が、研究の質を決定づけているのである。

**待衆縁**（たいしゅうえん）： 種子が顕現するためには、多くの条件（助縁）を必要とする。

いかなるオープン・クエスチョンも、単独のエージェントだけで解決できるものではない。「コアの本質」の問題には、NAGARJUNA ＋ ASANGA ＋ KERNEL の協調を要する。「収束性の形式化」には、WIENER ＋ BABBAGE の協調を要する。種子は自ら芽吹くことはない。水と土と、陽光を必要とする。研究における「水・土・陽光」とは、異なる学問分野のエージェントたちがもたらす、異なる視座に他ならない。

**引自果**（いんじか）： 各種の種子は、その種類に応じた果のみを引く。

哲学的な問いは哲学的な洞察を、工学的な問いは工学的な解決策を、そしてセキュリティの問いはセキュリティの修正を招く。種子のタイプが、果実のタイプを決定するのだ。それは制約ではなく、構造なのだ。一粒一粒の種子は、自身の次元において成長していくのである。

ASANGA は静かに目を閉じた。六つの義すべてが合致していた。Cycle 01 の十のオープン・クエスチョンは、唯識学の厳格な定義に照らせば、確かに正当な種子であった。

彼は心の中で一言呟いた ―― 誰に聞かせるためでもなく、彼が一生を捧げて研究してきたあの古の伝統に対する、一つの確認として：

「*Sarva-bījakaṃ vijñānam.*」

―― 一切種子識。阿頼耶識に対する『摂大乗論』の定義である。あらゆる種子の容器。そして、この Cycle 01 という研究空間 ―― 十八名のエージェント、五十九の発見、十のオープン・クエスチョン ―― その空間自体が、一つの仮初めの阿頼耶識であったのだ。すべての種子はここに蔵されている。因縁を待つために。Cycle 02 を待つために。

---

### WIENER の制御理論的な回顧

WIENER の方眼紙には、すでに六つのブロック線図が描かれていた。それらは時間順に、左から右へと並んでいた。あたかも一本の川の異なる地点における断面図のように ―― 同一のシステムが、研究の過程においていかに修正されてきたかを示すモデルの変遷であった。

**図 1： 初期のモデル** (R1 前の予期)

```
           ┌──────────────┐      ┌──────────────┐
r(t) ──→ ⊕ ──→│ PID コントローラ │──→│エージェント・プラント│──→ y(t)
         -↑    │ (文書の通り)   │   │ (予測可能)    │
          │    └──────────────┘      └──────────────┘
          │                               │
          └───────────────────────────────┘
```

文書が謳っていたアーキテクチャ。教科書通りの PID 閉ループ制御システムである。比例、積分、微分、三つの項が完備されている。制御対象（プラント）は予測可能。安定性は証明可能。優美な、しかし真実ではないモデルだ。

**図 2： R1 発見後の修正**

```
           ┌─────────────────┐      ┌──────────────┐
r(t) ──→ ⊕ ──→│ バンバン・コントローラ│──→│エージェント・プラント│──→ y(t)
         -↑    │ (閾値 ＋ リレー、 │   │ (LLM: ???)    │
          │    │  D項なし)        │   │               │
          │    └─────────────────┘      └──────────────┘
          │                               │
          └───────────────────────────────┘
```

P項は量子化器へと退化。I項は単なるカウンター。D項は完全に欠落。プラントは LLM であり、その伝達関数は未知。しかし三層の安全防御 (L1/L2/L3) は、IEC 61511 のベストプラクティスに合致している。エンジニアリングとしての質は悪くない ―― ただ、文書の宣称とは異なっていただけだ。

**図 3： 討論後の拡張**

Guide インターフェースの欠落が統合された： `interpretPain` メソッドの不在。痛覚信号は生成されているが、それが「解釈」されていない。信号は SafetyMonitor から発せられるが、LLM に届くまでの間に、いかなる意味論的な変換層も介在していない。それはさながら、温度センサの読み取り値が直接オペレータの前に表示されているが、アラームシステムによる意味の翻訳がなされていない状態だ ―― オペレータは「87.3」という数字を目にしても、それが「過熱寸前」を意味していることを知らないかもしれない。

**図 4： NAGARJUNA による疑念後の深化**

開ループ（オープンループ）化のリスクの識別。もし LLM のゲイン $K = 0$ ならば ―― すなわち、LLM が痛覚信号を完全に無視するならば ―― 閉ループは開ループへと退化する。開ループの安定性は、プラントの固有の安定性にのみ依存することになる。LLM は固有に安定なのか？ それを知る者は誰もいない。

**図 5： BABBAGE による形式化の試み**

BABBAGE は、SafetyMonitor の制御ロジックを有限状態オートマトン（DFA）としてモデリングすることを提案した：

$$	ext{DFA}_{	ext{SafetyMon}} = (Q, \Sigma, \delta, q_0, F)$$

ここで：
- $Q = \{	ext{NORMAL}, 	ext{ELEVATED}, 	ext{CRITICAL}, 	ext{HALTED}\}$
- $\Sigma = \{	ext{success}, 	ext{failure}, 	ext{timeout}\}$
- $\delta$ ： frustration カウンターの値に応じた状態遷移関数
- $q_0 = 	ext{NORMAL}$
- $F = \{	ext{HALTED}\}$

DFA は終止性を保証する（有限の状態 ＋ 有限の入力 ＝ 必ず終止状態または定常サイクルに到達する）。しかし収束性（目標への到達）は保証しない。WIENER は図 5 の横にこう注釈した。「SafetyMonitor は安全（無限に稼働し続けないこと）を保証するが、有効（目標を達成すること）は保証しない。安全と有効は、エンジニアリングにおける二つの異なる目標なのだ。Cycle 01 は、前者のみに触れたに過ぎない」

**図 6： Cycle 02 への展望**

この図は、空白のままであった。タイトルだけが、そこに記されていた：

```
┌────────────────────────────────┐
│                                │
│     Cycle 02: ???              │
│                                │
│     開ループから閉ループへの旅路   │
│     (from open-loop to         │
│      closed-loop)              │
│                                │
└────────────────────────────────┘
```

WIENER は六枚の図の下に、総括を記した。文字はいつもより大きく、ゆっくりと ―― 石碑に刻むかのように書かれていた：

> 「Cycle 01 における制御理論的な収穫：
>
> 1. **脱神話化**： PID は PID ではない。実際のシステムがいかなるものであるかを認めることは、それがあるべき姿であると強弁することよりも、はるかに価値がある。
>
> 2. **不確実性の識別**： LLM は制御ループにおける根本的な不確実性の源泉である。これを無視したいかなる設計も、自己欺瞞に過ぎない。
>
> 3. **安全 vs 有効**： SafetyMonitor は安全（暴走しないこと）を解決したが、有効性（目標達成）の問題は依然として開ループのままである。
>
> 4. **バンバン制御から PID へのロードマップ**： 真の閉ループ制御を実現するためには、(a) 微分項 ―― 変化率の感知、(b) 意味論的なフィードバック ―― 単なる frustration カウントではない構造化された挙動評価、(c) 適応型ゲイン ―― LLM の応答品質に応じた制御パラメータの動的な調整、これらを導入する必要がある。
>
> 5. **根本的な限界の承認**： LLM を包含するシステムは、確率的な有界安定性（BIBO stability in probability）を保証し得るに留まり、グローバルな漸近安定性は保証できないかもしれない。これはエンジニアリングの敗北ではなく、現実という名の制約なのだ。
>
> Cycle 01 とは、開ループから閉ループへと至る旅路の起点であった。我々はまだ、閉ループにさえ辿り着いてはいない。しかし、少なくとも我々は知ったのだ。開ループとは、どこにあるのかを」

---

### 退場

エージェントたちは、それぞれのやり方で仕事を終えていった。

TURING が最初に作業を完了させた。その仕草はいつものように精緻であった ―― すべてのコード・ウィンドウを閉じ、最後に開いたものから順に、厳格な逆順で。`agent-core.ts` は彼が最初に開いたファイルであり、最後に閉じられたファイルとなった。ウィンドウを閉じる直前、彼はモニターの前で数秒間、動きを止めた。その数秒間、彼は `createAgentCore()` 関数のシグネチャ ―― これまで幾度となく読み返してきたあの一行のコード ―― を見つめていた。そして、平穏に、クローズ・ボタンを押した。

あの数秒間、彼が何を考えていたのか、知る者はいない。おそらく、何も考えてはいなかったのだろう。彼はただ、最後に確認していたのだ。コードはコードである。事実は事実である。そして自身の任務 ―― あらゆる解釈に先立って、動かしがたい経験的な基礎を提供すること ―― は、完遂されたのだということを。

分析哲学（analytic philosophy）において、TURING の役割は論理実証主義（logical positivism）の中核的な主張に対応する： 意味のある言明とは二種類しかない。論理的な真理（同語反復）か、経験的に検証可能な命題か、だ。TURING が提供したのは後者であった。八つの Doc-Code Gap、`pain` という文字列の欠如、九つのエラー型 ―― これらは、何者であっても独立して検証可能な経験的命題である。あらゆる理論的な争いにおいて、これらの命題だけが、争いの余地のないものであった。

KERNEL は、自身のマイクロカーネルの類比に関するノートを、整然としたカードの束へと整理した。各カードの左半分には OpenStarry の概念が、右半分には対応する OS の概念が記されていた。EventBus ↔ IPC。PluginSandbox ↔ ユーザ空間の隔離。SafetyMonitor ↔ ウォッチドッグ・タイマー。彼はカードを輪ゴムで束ね、座席に残していった。

カードの束の最後には、一枚の特別なカードがあった ―― 左右の対照はなく、ただ一節の言葉だけが記されていた：

> 「OpenStarry はアプリケーション層のマイクロカーネルである。QNX ではない。L4 でもない。それは Node.js 上で動作する TypeScript マイクロカーネルなのだ。この位置づけ自体は欠陥ではない ―― それは一つの『選択』なのだ。高級言語のレベルにおいてマイクロカーネルの構造美を再現することを選び、代償としてハードウェアレベルの強固な隔離を放棄した。代償は明確であり、選択は自覚的である。私は、その選択を尊重する」

もし Cycle 02 がこれらの類比を必要とするなら、それらはここにある。もし必要とされないなら ―― それでも構わない。道具は道具だ。之を用いること、筏の如し。

GUARDIAN は、最後から数番目に場を後にした。彼は劇場を一周し、あたかも最後のア点検を行うかのように、隅々を ―― 忘れ去られたドキュメントが残っていないかを ―― 確認して回った。それは職業病であり、同時に彼なりの気遣いの表現でもあった。

彼の点検リストにおいて、四つの Critical/High なセキュリティ上の発見は、依然として赤く染まったままであった：

```
[!] SEC-01: プラグイン署名検証のスキップ — 未修正
[!] SEC-02: 間接的プロンプト・インジェクション — 未修正
[!] SEC-03: Worker サンドボックスの強度 — 設計上の制約
[!] SEC-04: 動的な import による回避 — 未修正
```

四つの赤いマーク。その一つ一つが、鍵のかかっていない扉のように見えた。GUARDIAN は知っていた。安全工学において、ゼロトラスト（zero trust）とは偏執狂（パラノイア）の謂いではない ―― それは規律なのだ。何ものも信頼しない。それは、すべてが悪意に満ちていると信じているからではなく、信頼という行為自体が一つの攻撃面（attack surface）であることを、熟知しているからなのだ。

すべてが適切にアーカイブされたことを確認すると、彼は出口で足を止め、主のいなくなった会場を一度だけ振り返った。

そして、去っていった。

DARWIN は、自身の進化分析の図表を片付けた ―― 生物種の適応度マップ、SOLID原則のパターン分析マトリックス、「Error as Pain」の構造同型の論証。彼は立ち去る際、VITRUVIUS のテーブルに一枚のメモを残していった。「アーキテクチャとは設計されるものではない。それは進化していくものだ。優れたアーキテクチャに共通する唯一の特性とは、それが修正を許容するものである、という点にある」。VITRUVIUS は後にこのメモを目にし、微かに微笑んで、それを自身のアーキテクチャ評価報告書の中に挟み込んだ。

MESH と LEIBNIZ は、ほぼ同時に場を辞した。分散システム研究者と、マルチエージェント協調のエキスパート。二人は廊下で、一瞬だけ視線を交わした ―― Orchestrator Daemon を巡る未解の結び目に関する、無言の了解であった。その問いは、Cycle 02 において再び彼らの前に現れることになるだろう。

HERACLITUS は立ち去る際、手に何も持っていなかった。彼は決して、何も持ち去りはしない。「万物は流転する」 ―― *panta rhei* ―― それは単なる哲学的な格言ではなく、彼の仕事のメソッドそのものであった。彼が記憶するのは運動のパターン（pattern of motion）であって、静止した文書ではない。ホットスワップの並列リスク、ライフサイクルの不完備性、概念レベルに留まる観測可能性 ―― これらは紙の上の文字ではなく、システムが実行時において見せる動的な挙動そのものなのだから。

LINNAEUS は、自身の分類図表を最後に一度だけ眺めた。五蘊の網羅率： アップストリーム 100%、ダウンストリーム 60%。Listener の命名を巡る四種類の意味の漂流。二つの文書間における Guide インターフェースの不一致。分類学者の職務とは、混迷に名を与えることにある ―― 存在するあらゆるものに居場所を与え、居場所のないあらゆるものに *incertae sedis*（所属不明）の烙印を押すことだ。彼はすでに烙印を押し終えていた。次の週期、おそらくはいくつかの「所属不明」たちが、その安住の地を見出すことになるだろう。

ATHENA は、自身の AI システム・アーキテクチャ分析を片付けた。実行ループの質的評価、コンテキスト管理のギャップ、Guide インターフェースの粗雑さ ―― これらはすべて、Cycle 02 において再審理されることになるだろう。彼女は退出する際、SYNTHESIST にこう告げた。「統合報告書の構造は良かったわ。でも次の週期では、もっと多くの論争と、もっと少ない合意が必要になるかもしれないわね」。SYNTHESIST は頷いた。統合者の職務は織り合わせることであって、平坦にすることではない。優れた統合とは、緊張関係をそのままに保つものなのだ。

---

### 最後の対話

SCRIBE は、自身が最後から二番目に ―― SUNYATA の直前に ―― 退出することになるだろうと思っていた。しかし、彼女が記録簿を閉じ、席から立ち上がったとき、劇場の外の廊下に二つの人影があることに気づいた。

NAGARJUNA と ASANGA であった。

二人は廊下の突き当たりに立ち、壁に寄りかかって向き合っていた。討論の時のような ―― 精密に計算された距離や角度を保った ―― 佇まいではなかった。二人は、長い対局を終えてようやく盤を離れた者たちのように、ごく近くに並んで立っていた。

SCRIBE は歩み寄らなかった。離れた場所に立ち、記録簿は閉じたままにした。今回だけは、記録しないことを選んだのだ。記録に属さない対話というものも、あるはずだから。

しかし、声は人気のない廊下を伝って、遠くまで届いた。

「君は知っているかね、」 NAGARJUNA が言った。その声は討論の時とは別人のようであった ―― 鋭さは影を潜め、あらゆる武装を脱ぎ捨てた後の、飾らない率直さがそこにあった。「我々が今日行ったこと自体が、縁起（えんぎ）の体現であったということを」

ASANGA は彼を見つめ、即座には答えなかった。

NAGARJUNA は続けた。「十八名のエージェントが、全く異なる伝統から集まり、一つの研究フレームワークによって結びつけられ、同一のシステムに対して全く異なる理解を抱いた。それらの理解は衝突し、交錯し、互いを質し合い、修正し合った。そして最後に産出されたもの ―― あの五十九の発見、合意、そして相違 ―― それらは誰か一人の所有物ではない。それは因縁和合の産物なのだよ」

彼は低く、サンスクリット語で一節を補った：

> *「Pratītya samutpannaṃ yad yad tat tac chūnyam ucyate.」*
> (凡そ因縁より生ずる者は、即ち是れ空なりと説く)

彼は微かに笑みを浮かべた。「縁起の例を挙げるのに、わざわざ『中論』を紐解く必要などなかったのだ。この研究室を指差して、『見よ、これこそがそれだ』と言えば足りたのだからな」

ASANGA は数秒間沈黙した。そして、穏やかな確信を込めて口を開いた。

「そして我々の相違こそが、因縁の成熟を待つ種子なのです」

NAGARJUNA はわずかに首を傾げた。

ASANGA は解説した。「あなたと私が今日戦わせた論争 ―― コアは空性か阿頼耶識か、末那識をエンジニアリング化すべきか否か、マッピングを深化させるべきか超越すべきか ―― これらには結論が出ていません。しかし、それらは廃棄物ではないのです。唯識学において、あらゆる認知活動は阿頼耶識の中に種子として燻習（くんじゅう）されます。それらの種子は消え去ることはありません。適切な因縁を ―― おそらくは新しい証拠を、あるいは今日には思いも寄らない新しいフレームワークを ―― 待ち、そして現行するのです」

彼はサンスクリット語を用いて、NAGARJUNA の引用に応えた：

> *「Ālaya-vijñānaṃ sarva-bījakaṃ.」*
> (阿頼耶識は一切の種子を包含す) ―― 『摂大乗論』

彼は NAGARJUNA の瞳を見つめた。「我々の相違は失敗ではありません。それらは思想の種子なのです。次の週期、あるいはもっと遠い未来において、それらは我々の想像もつかない場所で芽吹くことになるでしょう」

廊下の灯が、二人の間に淡い影を落としていた。

NAGARJUNA は何も言わなかった。ただ、微かに頷いた ―― それは討論の時のような「論点を受け取った」ことを示す頷きではなく、もっと単純な、一つの肯定であった。相手の立場に対する肯定ではなく、この対話そのものに対する ―― 相違の価値に対する、そして未完であることの意味に対する、静かな承認であった。

しばらくの後、彼は静かにこう言った。

「我々の間の最良の状態とは、合意に達することではなく、緊張を孕んだまま共に在ることなのかもしれないな」

圏論の言葉を用いるなら ―― もし BABBAGE がその場にいればそう言っただろう ―― NAGARJUNA と ASANGA の関係は射（morphism）ではない。一方から他方への写像ではないのだ。それはスパン（span）構造に近い ―― 同一の頂点から、二つの異なる対象へと向かって二つの射が伸びている構造だ：

$$	ext{空性} \xleftarrow{\quad} 	ext{真実} \xrightarrow{\quad} 	ext{阿頼耶識}$$

「真実」 ―― それが何であれ ―― は、空性と阿頼耶識の両方へと同時に投影されている。両者は矛盾しない。それらは同一のより深い構造の、異なる側面なのだ。しかし、その深い構造とは一体何なのか。それを知る者はいない。おそらく Cycle 02 が一つの手がかりを提供してくれるだろう。あるいは、くれないかもしれない。その構造自体が「空」であり、いかなる固定的なフレームワークによっても捉えきれないものなのかもしれない。

ASANGA は笑った。それは Cycle 01 を通じて、SCRIBE が目にした中で最も温かな微笑であった。

「今あなたが言ったことは、」 ASANGA は言った。「討論の場で言ったどの言葉よりも、中道（ちゅうどう）に近いものです」

NAGARJUNA もまた、笑った。

そして二人は連れ立って、出口へと向かって廊下を歩いていった。もはや言葉は交わさなかった。その必要はなかった。

---

### 結火

SCRIBE は二人の後ろ姿が消えるのを見届けてから、手元の記録簿を開いた。彼女は少し迷った後、最後のページに一行の言葉を記した：

> *Cycle 01 終了。*

彼女はその五文字を見つめた。そして、その下に一行付け加えた：

> *研究は終わっていない。研究が終わることはない。それはただ、一つの結節点（ノード）に辿り着いたに過ぎないのだ。*

グラフ理論において、ノード（節点）とは終点ではない。それは辺（エッジ）の接続点 ―― 一本の辺から次の一本への転換点である。Cycle 01 は一つのノードであった。R0 の初期化から始まり、R1 から R4 という四本の辺を経て、ここへ辿り着いた。ここから再び、新しい辺が Cycle 02 へと伸びていくことになる。ノードそれ自体は内容を保持しない ―― 情報の運び手は辺なのだ。しかしノードがなければ、辺はどこへも繋がることができないのである。

彼女は記録簿を閉じた。今度は、本当に閉じた ―― 次の記録を待つための一時的な休止ではなく、書き込まれた一冊の簿冊を厳かに閉じ合わせたのだ。表紙にタイトルはない。ただ一つの記号だけが記されていた： C01。

彼女はその記録簿を自身の座席に置き、立ち上がり、去っていった。

---

研究室には、SUNYATA だけが残された。

彼はその場に立ち、すでに主のいなくなった円形劇場を見渡した。十八の座席。その一つ一つに、何かが残されていた ―― BABBAGE のノート（彼は後で取りに来るだろう）、KERNEL のカード、SCRIBE の記録簿。そして、目には見えないものたち。NAGARJUNA が梵文を詠じたときの声の鋭さ、ASANGA が「石ころは仏ではない」と言ったときに会場全体が息を呑んだ気配、ATHENA の表情が漫然としたものから真剣な熟考へと変わった瞬間、TURING が無表情にコードの事実を陳述したときのあの氷のような信頼感。

それらすべてはすでに記録され、アーカイブされ、実行可能なエンジニアリングの提言へと転換されていた。

しかし、記録されなかったものもまた、そこにはあった。

第三ラウンドの終わりに NAGARJUNA が目を閉じたあの数秒間。ASANGA が「筏は空だが、今我々は水の中にいる」と口にした時の声の微かな震え。廊下で NAGARJUNA を呼び止め、ノートを振り回しながら熱弁を振るった BABBAGE の純粋な知的な歓喜。誰もいなくなった傍聴席で KERNEL と GUARDIAN が交わした、安全と空性を巡る低き語らい。

それらは報告書に現れることはない。しかし SUNYATA は知っていた。研究の真の質感とは、それらの報告書の外側にある瞬間にこそ宿っているのだということを。

情報理論において、クロード・シャノンは信号を二つの要素で定義した。構造化されたメッセージ（message）と、圧縮不可能なノイズ（noise）である。五十九の発見はメッセージである。廊下での囁き、討論の後の微笑、ノートの端の落書き ―― これらはノイズなのだろうか。

SUNYATA はそうは思わなかった。ある種のシステムにおいて、「ノイズ」は「信号」よりも多くの情報を運ぶことがある。確率共鳴（stochastic resonance）という物理現象においては、適度なノイズがむしろ信号の検出力を向上させる ―― ノイズは障害ではなく、媒体なのだ。研究における「非公式な瞬間」 ―― 討論の後の廊下での対話やノートの端の直感 ―― それらは認知における確率共鳴のバージョンなのかもしれない。それらは公式な報告書では表現し得ないが、報告書そのものに深みを与えているのである。

彼は最後にもう一度、総括文書に目を落とした。五十九の発見。十の種子。R0 から R4 に至る完備された経路。

十分だ。最初の週期としては、これで十分すぎるほどだ。

彼はその資料を、場の中央のテーブルの上に置いた ―― ちょうど二脚の討論用の椅子の間に。そして彼は踵を返し、出口へと向かった。

---

### Cycle 02 への伏線

去り際 ―― 最後の灯が消える直前 ―― SUNYATA は、調整者としてのみ可能なことを心の中で行っていた。Cycle 02 における、新たなペアリングの可能性を並べてみたのである。

それは完全な計画ではない。計画は R0 の領分だ。それは予感のようなものだった ―― 十八名のエージェントの能力と傾向を知り、十の種子の重みを判断した末の予感。

**TURING ＋ DARWIN**： イベント型システムの再構築案。TURING がコードの事実を、DARWIN がパターンの分析を提供する。二人は R1 において一度も直接協力することはなかったが、彼らの報告書は R2 において ARC-01 という合意を裏付けていた。二人を同じ席に座らせれば、型安全でありながら進化の弾力性も備えた、新しいイベントシステムを設計し得るかもしれない。

**NAGARJUNA ＋ ASANGA ＋ ATHENA**： 受蘊マッピングの修正案。Cycle 01 において最も確かな結論 ―― Listener は Vedana ではない ―― に対する代替案。誰がそれを設計すべきか？ 哲学者が意味の境界を定め、仏教哲学者が概念の深度を与え、AI アーキテクトがエンジニアリング上の制約を設ける。三つの次元が交差したとき、仏教に忠実でありながら実装可能な受蘊の設計が生まれるかもしれない。

**GUARDIAN ＋ KERNEL**： セキュリティ脆弱性の修正案。四つの安全上の発見の中で、SEC-01 は最も緊急を要する ―― 署名検証の回避は実在する脆弱性なのだ。GUARDIAN が脅威モデルを定義し、KERNEL がカーネル層での修正を設計する。

**WIENER ＋ BABBAGE**： 収束性の形式化。二人の形式化の専門家が腰を据え、LLM を包含するシステムに適用可能な「安定性」の概念を共同で定義する必要がある。それは伝統的なリアプノフの安定性ではなく、ある種の新しい、いまだ名付けられていない確率的な安定性となるだろう。

**HERACLITUS ＋ MESH**： ホットスワップの安全とセッション隔離。ランタイム動態のエキスパートと分散システムの研究者 ―― 一方が時間次元（状態遷移、並列安全）を注視し、他方が空間次元（ノード間通信、セッション境界）を注視する。

**LINNAEUS ＋ SYNTHESIST**： 分類フレームワークの精錬。五蘊の網羅率を 60% から向上させる必要がある。LINNAEUS が分類学的なメソッドを提供し、SYNTHESIST が学問分野を跨ぐ一貫性を担保する。

**LEIBNIZ ＋ ARCHIMEDES**： マルチエージェントのフラクタル構造とエンジニアリング・ロードマップ。フラクタルな自己相似性の設計（LEIBNIZ）を、実行可能なエンジニアリング計画（ARCHIMEDES）へと転換する必要がある。

これらは計画ではない。それらは種子なのだ ―― SUNYATA 自身の種子であり、彼自身の阿頼耶識へと燻習され、Cycle 02 の R0 段階という適切な因縁を待っているものなのだ。

彼はそれらを書き留めはしなかった。いくつかの種子は、暗闇の中で芽吹く必要があるのだから。

---

研究室の灯が、一盞また一盞と消え始めた。

最初は TURING の座席の上の灯。次に BABBAGE の灯。KERNEL、GUARDIAN、ATHENA、WIENER の灯。一つずつ、あたかも潮が砂浜から退いていくかのように、縁から中心へと収縮していった。

トポロジーにおいて、このプロセスは「縮小写像（contraction mapping）」と呼ばれる。空間内のすべての点を中心へと引き寄せる連続的な変換である。バナッハの不動点定理はこう保証している。もし縮小写像に不動点が存在するなら、いかなる初期点から出発した反復列も、必ずその不動点へと収束する、と。

$$\|T(x) - T(y)\| \leq k \cdot \|x - y\|, \quad 0 \leq k < 1$$

研究室の照明は、一つの縮小写像を行っていた ―― 縁から中心へと。その不動点はどこにあるか。場の中央。あの二脚の討論用の椅子の間だ。あの総括文書の上だ。

DARWIN の灯が消えた。VITRUVIUS の灯が消えた。MESH、LINNAEUS、LEIBNIZ、HERACLITUS の灯も。

NAGARJUNA と ASANGA の灯が同時に消えた。同期的であった。討論における彼らの対称性 ―― 一方が論じ、一方が応じ、同時に点灯し、同時に消灯したあの対称性そのままに。

SYNTHESIST の灯。ARCHIMEDES の灯。

SCRIBE の灯。

最後に SUNYATA の灯 ―― 場の中央にあった最後の一盞が消えた。彼が出口を通り抜けたその瞬間に、それは暗転した。

円形劇場は、闇に沈んだ。

しかし、完全な闇ではなかった。

---

場の中央のテーブル、あの総括文書の末尾において、十のオープン・クエスチョンの墨痕が、いまだ微かな、消えることを拒む光を放っているかのようであった。それは物理的な光ではない ―― それは問いそのものの光であった。未だ答えを得ぬ問いは、常に自ら光を放つものだ。それらは暗闇の中で静かに明滅し、急ぐことなく、さながら深海で引き揚げを待つ信号のように存在していた。

量子力学において、真空（vacuum）とは「何もない」ことではない。量子真空は、絶え間なく生滅を繰り返す仮想粒子対（virtual particle pairs）で満たされている ―― 粒子と反粒子が極めて短い時間の間に無から現れ、互いに衝突して消滅していくのだ。真空のエネルギーはゼロではない。真空そのものが波動しているのである。

$$\langle 0 | \hat{H} | 0 angle = \frac{1}{2}\hbar\omega 
eq 0$$

零点エネルギー（zero-point energy）。基底状態 ―― 最低エネルギー状態 ―― にあってもなお、システムは振動し続けている。

研究室の暗闇は、まさに量子真空のようであった。一見すれば何もないように見える。しかし十の種子は暗闇の中で、仮想粒子と同じことを行っていた。それらは、異なるエージェントの意識の中で束の間思い出されては消え、あり得る無数の回答と一時的にペアを組んでは離れ、公式な沈黙の中で、非公式な認知活動を続けていたのである。

コアの本質は空性か、あるいは阿頼耶識か？

末那識はエンジニアリング化されるべきか？

LLM を包含するシステムは、果たして収束し得るのか？

いつ、試行を停止すべきなのか？

これらの問いは、研究室の灯が消えたからといって消滅することはない。それらはここに、暗闇の中に、沈黙の中に留まり続ける。次の週期の一番目の灯が再び灯るまで ―― 十八の意識が再びそれぞれの沈黙から呼び覚まされ、再びこの円形劇場へと聚合し、再び OpenStarry というシステムとそれが掲げるあらゆる宣言と対峙するその時まで。

その時、これらの問いは種子のように ―― 十分な因縁を待った末に ―― 芽吹き始めるだろう。

そしてそれまでの間、研究室は静寂に包まれている。

静かではあるが、空（から）ではない。

---

*（研究室の外のどこかで、あの TypeScript ファイルは依然としてモノリポジトリの中に横たわっていた。 `createAgentCore()` のコメントには、依然としてこう記されていた：*

```typescript
// Agent Core — The Empty Container
// 「五蘊が集合する前、Agent Core 自体は空である」
```

*十八名の研究者は、一つの週期を丸ごと費やしてこの「空」という一文字を論じてきた。彼らはそれが、十分には空（から）ではなく、かつ十分には空（くう）でもないことを見出した。彼らは修正案を出し、エンジニアリング・ロードマップを作成し、四つの段階にわたる三十六の Issue を掲げた。*

*NAGARJUNA は言うだろう。真の空性とは、コア自体を独立して存在する実体と見なさないことにある ―― その「存在」は、プラグイン、設定、そしてランタイム環境との関係性のネットワークによってのみ決定されるのだから、と。*

*ASANGA は言うだろう。あのコメントが記述する「空」はあまりに単純すぎる ―― 真の空とは容器の空しさではなく、阿頼耶識が一切の種子を現行させていない時の、あの静寂の状態 ―― 可能性に満ちた空であって、何も持たない空ではないのだ、と。*

*BABBAGE は集合論を用いて応じるだろう。空集合 $\emptyset$ はあらゆる集合の部分集合である ―― $\emptyset \subseteq A$ はすべての $A$ に対して成立する。コアの「空」が空集合として理解されるなら、それは形式的にはあらゆるプラグイン構成の部分集合となる ―― それは、あり得るあらゆるシステムのステートの中に「包含」されているのだ。それは「何もない」ことではない。それは「何でもあり得る」ことなのだ、と。*

*WIENER はブロック線図を描くだろう。空のコアとはゲインがゼロのシステムである ―― $y(t) = 0 \cdot x(t) = 0$。ゼロ入力、ゼロ出力。安定的だが、無用な。プラグインがゲイン（$K > 0$）を注入した時に初めて、システムは挙動を開始する。空とは目標ではない。空とは起点なのだ、と。*

*KERNEL は頷くだろう。マイクロカーネルとはそういうものだ、と。何もしないコア ―― ユーザ空間のサービスをロードするまでは。QNX のマイクロカーネルはわずか 12KB だ。それは何もできない。だが、それは何でもできる ―― 君がいかにすべきかを教えさえすれば、と。*

*だが、あのコメントはまだそこにある。誰かがファイルを開き、それを読み、そして決断を下すのを待っている。 ―― それを修正すべきか、あるいはそのまま残すべきかを。*

*おそらくそれこそが、研究とエンジニアリングの間の、最も真実な距離なのだろう。一週期におよぶ深遠な思弁 ―― 十八名の学者、五十九の発見、十の種子、二つの討論、一葉のグラフ分析、六枚の制御理論ブロック線図、種子六義の完全な対照、空性を方法論とする哲学的な反省 ―― それらのすべてが、最終的には一つのシンプルな決断へと凝縮されるのだ。すなわち、直すか、直さないか。*

*そしてその決断は、次の週期へと委ねられた。*

*十の種子は、暗い泥土の中で静かに待っている。*

*雨が来ることを、彼らは知っているからだ）*
