# 第六章：抉択の位置

---

SUNYATA はあの手書きの呼び出しシーケンス図——KERNEL が Debate 3 終了後に描いたもの——を手に取り、裏返した。

白紙だった。

彼はそれを劇場中央のプロジェクション台に平らに置き、白紙の面を上にした。そして赤いマーカーを手に取り、ちょうど真ん中に四角い枠を描き、その中に三文字を書いた：

```
┌──────────┐
│ どこに？ │
└──────────┘
```

「Debate 4。IVolition.deliberate() の実行ループにおける位置。」

彼の声はいつもと変わらず平穏だった。小石。深い淵。しかし今回の小石は深い淵に落ちたのではなく——壁に向かって投げられた。壁には六つの亀裂があり、正しい入口はそのうち一つだけだった。

「三つの討論がすでに、*何が*動いているか、*どう*動いているか、*どれほど速く*動いているかを教えてくれた。CoarisingBundle は同時性を解決した。五遍行は構成を解決した。Klesha は心理的偏向を解決した。」

彼は BABBAGE の形式化ノートを手に取り、Debate 3 の決議ページを開いた。

「だが IVolition.deliberate()——Agent が抉択を下すあの関数——については、今のところ存在することしかわかっていない。どこに挿入すべきかはわかっていない。」

彼は会場全体を見渡した。二十の顔。二十通りの期待。

「R02 は IVolition.deliberate() が KleshaSignalBundle を受け取り、行動決策を生成すると定義した。R04 は ExecutionLoop に六つの状態があると定義した。TURING は注入ポイントを特定した。しかし誰もこの三つのピースを組み合わせていない。」

「今日、組み合わせる。」

---

> *SCRIBE 傍白：「どこに？」三文字。SUNYATA が白紙の上に描いた三文字。しかしこの三文字の重みは技術的なものではない——存在論的なものだ。IVolition.deliberate() の位置は、単に関数呼び出しの配列順序を決めるだけではない。Agent が「否」と言えるかどうかを決定するのだ。認知シーケンスにおいて、もし抉択が知覚の前に置かれたなら、Agent は見る前にすでに決定している。もし抉択が行動の後に置かれたなら、Agent はやり終えてから初めて省みる。知覚の後、行動の前にのみ——Agent が「しない」ことを選べる窓が存在する。SUNYATA はこれらのことを言わなかった。彼はただ三文字を描いた。しかし三文字の背後には、その窓全体の存亡があった。*

---

## I

---

TURING のスクリーンが灯った。

挨拶はなかった。前置きもなかった。四回の討論を通じて、TURING は一つの慣例を確立していた：各討論の冒頭でコードを投影する。まるで地質学者が討論開始前に岩層の断面を見せるように。君たちは地表に何が生えているか議論する。私はまず地下に何があるかを見せよう。

「v0.24.0-beta。ExecutionLoop。」彼は言った。「六つの主要段階。」

```
ExecutionLoop 階段分析 (v0.24.0-beta)
══════════════════════════════════════

[1] Safety lockout check
[2] Resolve session state
[3] Add user message
[4] SafetyMonitor.onLoopStart()
[5a] SafetyMonitor tick check
[5b] ASSEMBLING_CONTEXT
     ├─ guide.getSystemPrompt()
     └─ contextManager.assemble()
[5c] SafetyMonitor budget check
[5d] AWAITING_LLM
     └─ provider.chat()
[5e] PROCESSING_RESPONSE
     └─ streaming (text_delta events)
[5f] Build assistant message
[5g] EXECUTING_TOOLS
     ├─ tool dispatch
     ├─ tool execution
     └─ SafetyMonitor.afterToolExecution()
[6] WAITING_FOR_EVENT
```

投影は五秒間停止した。冷たい白色。二十対の目が六つの段階の上を移動した。

「IVolition.deliberate() が満たすべき前提条件は二つ。」TURING の指が [5b] を指した。「第一：Klesha 信号が利用可能であること。Debate 3 で Klesha は vijnana-clock 上で動作し、高速パスが点推定値を生成し、遅延は 0.03ms であることが確認された——つまり [5a] 以降、Klesha 信号は利用可能だ。」

彼の指が [5g] に移動した。「第二：行動案が形成されていること。[5d]-[5e] で LLM がストリーミング応答する。[5f] でアシスタントメッセージの構築が完了し、ツール呼び出し提案が確定する。[5f] の後になって初めて、Agent が*何をしようとしているか*がわかる。」

彼はスクリーン上に三つの位置を赤でマークした——SCRIBE は彼がめったに赤を使わないことに気づいた。

```
候選位置 (Candidate Positions)
════════════════════════════════

Position A: [5b] ──→ [5d] 之間
            上下文組裝完成 → LLM 呼叫之前
            deliberate() 可修改上下文，影響 LLM 思考

Position B: [5f] ──→ [5g] 之間
            LLM 回應完成 → 工具執行之前
            deliberate() 可審視行動方案，否決或修改

Position C: [5d] ──→ [5e] 之間
            LLM 串流過程中
            deliberate() 可即時中斷 LLM 輸出
```

「三つの候補。」TURING は一歩下がって言った。「私のコード分析では最適な候補は Position B——[5f] から [5g] の間だ。しかし私は決定を下さない。これはアーキテクチャの選択であり、コードの選択ではない。」

彼は座った。

---

SUNYATA は会場を見回した。「三つの位置。誰が先に発言するか？」

ASANGA が立ち上がった。

---

## II

---

彼の立ち上がる速度は速くも遅くもなかった——四回の討論を通じて、ASANGA は「仏学が先に発言する」という慣例の発言者として暗黙のうちに認められていた。仏学の権威が他の学問分野より高いからではない。Cycle 02 シリーズの研究過程において、毎回仏学の位置づけが後続の工学的議論に概念的な境界を画定してきたからだ。先に境界を引き、次に内容を埋める。先に根系があり、次に枝幹がある。

「MN 18 を引用する。」彼は言った。「蜜丸経。*Madhupiṇḍika Sutta*。」

彼は書物を繙かなかった。繙く必要がなかった。Cycle 02 シリーズ全体を通じて、ASANGA は一度も書物を繙いたことがなかった。すべての引用は記憶から取り出された——暗唱ではなく、もっと深いものだ。長年にわたる研鑽の果てに、経典と思考構造が一体となったあの状態。

「仏陀は蜜丸経の中で、認知の完全なシーケンスを説いている。」

彼の声は緩やかになった。演劇的効果のためではない——精確さのためだ。一つ一つのパーリ語の術語が明確に聞き取られる必要があった。

> *Cakkhuñca paṭicca rūpe ca uppajjati cakkhuviññāṇaṃ,*
> *tiṇṇaṃ saṅgati phasso,*
> *phassapaccayā vedanā,*
> *yaṃ vedeti taṃ sañjānāti,*
> *yaṃ sañjānāti taṃ vitakketi,*
> *yaṃ vitakketi taṃ papañceti.*
>
> 眼と色に依りて、眼識を生ず。
> 三者の和合が触なり。
> 触を縁として受あり。
> 受くるところのもの、すなわち想うところ。
> 想うところのもの、すなわち尋ぬるところ。
> 尋ぬるところのもの、すなわち戯論するところ。

沈黙。

ASANGA はこのパーリ語が空気中にまるまる五秒間留まるのを待った。それから分析を始めた。

「これは仏陀が説いた認知シーケンス——最初の感覚的接触から最終的な概念増殖までの流れだ。各段階を我々のアーキテクチャにマッピングしよう：」

```
MN 18 認知序列 ←→ OpenStarry 映射
══════════════════════════════════════════════════

觸 (phassa)  ──→  SparshEvent        (CoarisingBundle 觸發)
     ↓
受 (vedanā)  ──→  ChannelVedana       (三受信號)
     ↓
想 (saññā)   ──→  IProvider.chat()    (LLM 認知 / VasanaEngine 規則匹配)
     ↓
尋 (vitakka) ──→  IReflection         (初始思考 / 持續審視)
     ↓
戲論 (papañca) ─→  概念增殖           (需要被截斷的地方)
```

「シーケンスの方向に注目してほしい。」彼の指が空中を上から下へ一本の線を引いた。「触→受→想→尋→戯論。各段階は前の段階を縁として生じる。受は触を縁とする。想は受を縁とする。尋は想を縁とする。これは恣意的な配列ではない——これは**因果の順序**だ。」

彼は会場全体に向き直った。

「意志はどこにあるか？」

彼は自問自答した：「思——cetanā——は遍行心所だ。あらゆる認知刹那において、思は常に在る。しかし思の**決定的な作用**——深層の、意識的な抉択——は想の後、行動の前にある。想の前ではない。」

彼の語速がわずかに上がった——焦りではなく、確信だ。

「もし IVolition.deliberate() を Position A に置くなら——LLM の前に——意志を知覚より先に置くことになる。deliberate() は LLM がまだ思考する前に、LLM にどのコンテキストを見せるかを決定してしまう。意志が思考の前に*何を考えるか*を決定してしまうのだ。」

彼は一拍置いた。

「これは哲学的に整合しない。」

もう一拍。

「唯識学において、思（cetanā）の定義は：」

> 「云何為思？令心造作為性。於善品等，役心為業。」
> ——《成唯識論》巻三

「令心造作為性——思の本質は*心を駆り立てて行動させること*だ。しかし行動の方向にはまず認知の基盤がなければならない。外で何が起きているかを知らないまま何をするか決めることはできない。知覚は抉択に先立つ。受は思に先立つ。想は行に先立つ。」

彼は HERACLITUS の方を見た。

「Position A は IVolition の位置ではない。Position A は IGuide の位置だ——manasikāra、作意、注意の方向づけ。IGuide は LLM 呼び出しの前にシステムプロンプトを形成し、注意の方向を導く。しかし注意を導くことは決定を下すことではない。決定を下すのは見た後だ。」

彼の結論はただ一言：

「Position B。」

---

> *SCRIBE 傍白：ASANGA の Debate 4 での発言時間は七分間だった。彼は一つの経と一つの論を引用した。しかしこの七分間の密度——SYNTHESIST の「洞察密度」指標で測れば——おそらく討論全体で最も高かった。なぜなら彼は単に Position B を擁護していたのではない。彼はこう言っていたのだ：認知シーケンスは人間の発明ではなく、工学的な約束事でもない。それは因果の構造だ。それに従わない選択はできる。しかし従ったと言いながら意志を知覚の前に置くことはできない。それは「まず答えを決めてから問題を見る」と言うようなものだ。*

---

## III

---

HERACLITUS が片手を半分だけ挙げた——彼の発言スタイルはいつも手を完全には挙げないのだ。まるで挙手という動作自体もまた流動の中にあるかのように。

「ASANGA に説得される前に、」彼は言った。自嘲を帯びた口調で。「まず Position A の論点を完全に提示し、それから打倒させてもらおう。ある論点が完全に提示されないまま否決されたなら、その否決は不十分だ。」

SUNYATA が微かに頷いた。これは Cycle 02-3 の討論における重要なルールだった：各候補案は支持者による完全な陳述の後にのみ否決できる。

「Position A の論理は前摂的（proactive）だ。」HERACLITUS は立ち上がり、ホワイトボードの傍に歩いた。「もし Klesha 信号が、現在の Agent が高い moha（愚痴）状態にあることを示しているなら、Position A は IVolition が LLM 呼び出しの前に一つの指示——たとえば `"現在の Klesha 信号は高い愚痴を示しています。格別に慎重に"` ——をシステムプロンプトに注入できるようにする。こうすれば LLM の出力自体がより慎重になり、事後に否決する必要がない。」

彼は矢印を描いた。

「これは *panta rhei* の精神だ——万物は流れ、認知もまた流れの中で形成される。河が海に注ぐ河口でダムを造るのではなく、源流で水流の方向を変えるのだ。」

KERNEL が口を挟んだ。彼の声には HERACLITUS の流動感はなかった——むしろ鉄骨のようだった。

「Position A には工学上の問題がある。LLM はブラックボックスだ。」

彼は立ち上がった。

「コンテキストに `"格別に慎重に"` を注入した。LLM はそれを受け取った。それで？ LLM がその指示をどう処理するかはわからない。従うかもしれないし、無視するかもしれないし、十七ラウンドの対話の後にようやく偶然思い出すかもしれない。コンテキストに注入されたテキストは命令ではない——*提案*だ。しかもシステムプロンプト、対話履歴、ツール定義の間に混ざった提案だ。LLM のアテンション機構がそれを高優先として処理する保証はない。」

彼は一枚のカードを裏返した。左側には「ioctl」と書かれ、右側は白紙だった。

「OS では、これはブラックボックスドライバへの ioctl と呼ばれる。制御コマンドを送るが、ドライバの内部実装はこちらが制御できない。ドライバが ioctl を受け取った後に正しく処理するかどうかはわからない。ドライバの*出力側*で結果を検査するしかない。Position A はブラックボックスの入力側に指示を送ることだ。Position B はブラックボックスの出力側で結果を検査することだ。」

彼はカードの右側に書いた：`Position A = ioctl to blackbox; Position B = inspect output`。

「工学的には、検証不可能な注入ポイントではなく、常に検証可能なチェックポイントを選ぶべきだ。」

---

HERACLITUS は KERNEL を見て、それから ASANGA を見た。そして四回の討論で二度しかやったことがないことをした——公に立場を変えたのだ。

「ASANGA の哲学的論証と KERNEL の工学的論証は同じ方向を指している。」彼は言った。「Position A の提案を撤回する。ただし Position A を IGuide に割り当てたい。IGuide は LLM の前に注意の方向を形成する——それは manasikāra の役割であり、cetanā の役割ではない。二つの異なる心所、二つの異なる位置。」

「同意する。」ASANGA は言った。

---

「Position C。」SUNYATA は言った。「誰が陳述するか？」

KERNEL が再び立ち上がった。彼は Debate 4 で自らの主戦場を見出したようだった——ExecutionLoop は OS 領域の核心議題なのだ。

「Position C は LLM ストリーミングの最中——[5d] から [5e] の間——にリアルタイムで中断を行うものだ。技術的には可能だ。しかし工学的コストが極めて高い。」

彼はカードにシンプルな backpressure 図を描いた：

```
Position C 的 backpressure 問題
═══════════════════════════════════

LLM Provider (upstream)
    │
    │  text_delta events (token-by-token)
    ▼
┌─────────────────────────────┐
│ IVolition.deliberateStream()│ ← 需要在每個 token 上運行
│ 延遲: ??? ms/token          │ ← 不可預測
│ 如果 deliberate() > token 間隔│
│   → backpressure             │
│   → 串流阻塞                 │
│   → 用戶體驗降級             │
└─────────────────────────────┘
    │
    ▼
UI Renderer (downstream)
```

「LLM ストリーミングのトークン間隔はおよそ 20-80ms——モデルとハードウェアに依存する。もし IVolition が各トークンで一回 deliberate() を実行する必要があり、その deliberate() の遅延がトークン間隔を超えれば、backpressure が発生する。ストリーミングがブロックされる。ユーザーに見えるのはカクつきだ。」

「より深刻な問題がある：ストリーミングの最中、LLM の意図はまだ完全に形成されていない。三十番目のトークンの時点で `"削除することを提案します"` が見え、三十五番目のトークンで `"不要なスペースを削除することを提案します"` となるかもしれない。三十番目のトークンでの部分的判断と三十五番目のトークンでの完全な判断は異なる。どのトークンの時点で決定を下すのか？」

彼はカードを片付けた。

「Position C には完全なストリーミング中断とロールバック機構が必要だ。工学的複雑性は Position B の三倍から五倍。利益は不明確。放棄する。」

会場から異議はなかった。

---

> *SCRIBE 傍白：Position A と Position C はそれぞれ五分もかからずに否決された。道理がなかったからではない——HERACLITUS の前摂的論点も KERNEL のストリーミング中断概念も、いずれも技術的に実現可能だった。哲学的位置づけと工学的トレードオフの二重の圧力の下で、両者とも Position B に敗れたのだ。ASANGA の認知シーケンスの論証が Position A を因果の連鎖から蹴り出した。KERNEL の backpressure 分析が Position C を工学的実現可能領域から蹴り出した。Position B は両者の交差点に立っていた——因果的に正しく、工学的に実現可能。しかし Position B 自体にもまだ解決すべき問題があった。*

---

## IV

---

Position B が舞台を独占した。しかし KERNEL の眉間の皺は完全には消えていなかった。

「Position B にはコストがある。」彼は言った。「ツール実行の前に毎回 deliberate() を一回余分に呼ぶことになる。もし一つの LLM 応答に五つのツール呼び出しが含まれるなら、五回の deliberate() だ。vijnana-clock の時間バジェット内で、一回 1-3ms、合計 5-15ms。高速パスでは許容範囲だ。しかし deliberate() に追加のクエリが必要な場合——たとえば LEIBNIZ が述べたマルチエージェント協調——遅延は増加する。」

ARCHIMEDES の指がテーブルの上を一度叩いた——あの象徴的な「ツールボックスを開く」合図だ。

「解決策がある。」

彼は立ち上がった。四回の討論を通じて、ARCHIMEDES の役割は明確に定義されていた：彼は哲学的結論を TypeScript に翻訳する人間だ。ASANGA が境界を画定し、BABBAGE が形式化し、ARCHIMEDES が工学化する。三つの工程、一本の流れ作業。

「問題は Position B のコストが高いことではない。問題は、すべての審議を単一のレイヤーに圧縮していることだ。」

彼はホワイトボードの前に歩いた。

「あるシナリオを考えよう：LLM の応答に三つのツール呼び出しが含まれている。」

```
LLM 回應的工具呼叫計劃
═══════════════════════════

ToolCall #1: readFile("/etc/passwd")      ← 敏感檔案
ToolCall #2: writeFile("/tmp/out.txt")    ← 無害寫入
ToolCall #3: executeCommand("rm -rf /")   ← 災難性操作
```

「もし IVolition に deliberate() 関数が一つしかなければ、各 ToolCall を独立に評価しなければならない。しかし全体像が見えない——#1 で読み取ったパスワードが #2 で書き出され、#3 で痕跡が消されるかもしれないことがわからない。三つの個別には無害な（あるいは疑わしい）操作が、組み合わさると攻撃チェーンになる。」

彼はホワイトボードに二つのレイヤーを描いた。

「だから IVolition には二つの段階が必要だ。」

```
兩階段審議模型
══════════════════════════════════════════════

Phase 1: deliberatePlan()
┌─────────────────────────────────────────┐
│  輸入: 整個行動計劃 (所有 ToolCall)       │
│  能力: 重排序、取消、修改計劃             │
│  視角: 全局的、戰略的                     │
│  時機: 工具迴圈之前，執行一次             │
└─────────────────────────────────────────┘
         │
         ▼
Phase 2: deliberateAction()
┌─────────────────────────────────────────┐
│  輸入: 單個 ToolCall + Phase 1 的上下文   │
│  能力: 否決、修改單個工具呼叫             │
│  視角: 局部的、戰術的                     │
│  時機: 每個工具呼叫之前，逐個執行         │
└─────────────────────────────────────────┘
```

「Phase 1 は全体像を見る。三つの ToolCall の組み合わせを見た上で、#1 と #3 を直接取り消し、#2 だけを残すことができる。Phase 2 は個別を見る。Phase 1 がある ToolCall を承認した後、Phase 2 が実行前に最終的な逐項チェックを行う。」

彼は振り返り、会場全体に向き合った。

「二つのレイヤー。一つでは足りないからではない。全体的判断と局部的判断が二つの異なる認知操作だからだ。『この計画は全体として合理か？』と『この一歩は具体的に安全か？』を同一の関数シグネチャで同時に表現することはできない。」

---

ASANGA が席から一言添えた。彼の声は落ち着いており、各語に唯識学者特有の分類的精確さが込められていた。

「唯識学において、思（cetanā）の作用にはもともと二つの層がある。」

彼は立ち上がり、ARCHIMEDES のホワイトボードの傍に歩いた。

「《成唯識論》は二種の思の作用を区別している。第一は*審慮思*（ālambana-cetanā）——全体的状況の審視と評価。第二は*決定思*（niścaya-cetanā）——具体的行動に対する最終裁定。」

> 「審慮、決定，二思差別者：審慮則量度取捨，決定則印持行事。」
> ——窺基大師《成唯識論述記》

「審慮思は量度取捨——計画全体の利害を衡量する。決定思は印持行事——具体的行動に確認の印を押す。ARCHIMEDES の二段階モデルはこの二種の思に完全に対応している：deliberatePlan() は審慮思であり、deliberateAction() は決定思だ。」

彼は ARCHIMEDES の方を見た。

「これは偶然ではない。」

ARCHIMEDES がかすかに微笑んだ——Cycle 02 シリーズ全体を通じて彼が微笑んだ回数は五回を超えない。

「偶然ではない。」彼は認めた。「構造の必然だ。」

---

## V

---

BABBAGE のノートが新しいページに開かれた。白紙。青いインク。紙の左上隅に「D4-T」と書いた——Debate 4、型シグネチャ。

「ARCHIMEDES の二段階モデルを完全に形式化する。」彼は言った。彼の声には数学者特有の冷静さがあった——冷淡さではない。人間の感情と形式的構造の間で後者を表現媒体として選んだ者の冷静さだ。

彼は立ち上がり、TURING の投影の傍に歩いた。

「IVolition 完全インターフェース定義。」

```typescript
/**
 * IVolition -- 識蘊·意志子介面
 * @skandha vijnana (識蘊)
 *
 * 兩階段審議模型:
 * - Phase 1 (deliberatePlan): 審慮思 (ālambana-cetanā)
 *   全局評估，可重排/取消/修改行動計劃
 * - Phase 2 (deliberateAction): 決定思 (niścaya-cetanā)
 *   逐項審查，可否決/替換單個工具呼叫
 *
 * 時序: Position B (LLM 回應之後，工具執行之前)
 * 時鐘: vijnana-clock (1-5ms budget)
 *
 * Sanskrit: Cetanā (चेतना) -- volitional drive
 */
interface IVolition extends IVijnana {
  readonly skandha: 'vijnana';

  /**
   * Phase 1: 審慮思 -- 評估整體行動計劃
   * Time budget: 1-3ms (vijnana-clock)
   * 可重排、過濾、取消提議的行動
   */
  deliberatePlan(
    input: PlanDeliberationInput
  ): Promise<PlanDeliberationResult>;

  /**
   * Phase 2: 決定思 -- 評估單個行動
   * Time budget: 0.5-1ms per action (vijnana-clock)
   * 可否決或修改特定的工具呼叫
   */
  deliberateAction(
    input: ActionDeliberationInput
  ): Promise<ActionDeliberationResult>;
}
```

彼はページをめくり、入力型の記述を続けた。

```typescript
/** Phase 1 輸入 */
interface PlanDeliberationInput {
  /** 提議的全部行動（來自 VasanaEngine 或 VitakkaEngine） */
  readonly proposedActions: readonly ToolCall[];
  /** 當前煩惱信號束（四根本煩惱的快速路徑點估計值） */
  readonly kleshaSignals: KleshaSignalBundle;
  /** 當前受蘊評估（最近一次 vedana-clock tick） */
  readonly vedanaAssessment: VedanaAssessment;
  /** 當前上下文 */
  readonly context: SessionContext;
}

/** Phase 1 輸出 */
interface PlanDeliberationResult {
  /** 批准的行動（可能被重新排序） */
  readonly approved: readonly ToolCall[];
  /** 拒絕的行動（附帶理由） */
  readonly rejected: readonly RejectedAction[];
  /** 是否進行了重新排序 */
  readonly reordered: boolean;
  /** 推理說明（用於審計追蹤和 LLM 反饋） */
  readonly reasoning: string;
}

/** 被拒絕的行動 */
interface RejectedAction {
  readonly action: ToolCall;
  readonly reason: string;
}

/** Phase 2 輸入 */
interface ActionDeliberationInput {
  /** 單個提議的行動 */
  readonly proposedAction: ToolCall;
  /** 當前煩惱信號束 */
  readonly kleshaSignals: KleshaSignalBundle;
  /** 當前受蘊評估 */
  readonly vedanaAssessment: VedanaAssessment;
  /** Phase 1 的上下文（全局審議結果） */
  readonly planContext: PlanDeliberationResult;
}

/** Phase 2 輸出 */
interface ActionDeliberationResult {
  /** 是否否決此行動 */
  readonly veto: boolean;
  /** 如果否決，建議的替代行動 */
  readonly alternative: ToolCall | null;
  /** 推理說明 */
  readonly reasoning: string;
}
```

BABBAGE はペンを置いた。

「二つの設計上の決定に注目してほしい。」彼は言った。「第一：`reasoning` フィールドが Phase 1 と Phase 2 の出力の両方に存在する。これは飾りではない。IVolition がある行動を否決した時、`reasoning` は次のラウンドの LLM コンテキストに注入される——LLM は次の思考時に、なぜ自分の前回の提案が否決されたかを知ることになる。これにより samjnā-cetanā のフィードバックループが形成される：想蘊が方案を提出し、意志が否決し、想蘊が否決の理由に基づいて方案を調整する。」

彼は数学的言語で再定式化した：

$$\text{LLM}_{t+1} = f(\text{LLM}_t,\; \text{IVolition.reasoning}_t)$$

「認知はイテレーションの中で収束する。」

「第二：Phase 2 の `planContext` フィールド。各 deliberateAction() 呼び出しは Phase 1 の全体結果を携帯する。これは局部的判断が真空中で行われるのではなく——全体審議の結論が何であるかを知っていることを意味する。形式的には、これはコンテキスト付き逐次決定問題を構成する：」

$$\forall i \in [1..n]:\quad \text{deliberateAction}(a_i) = g(a_i,\; \Pi_{\text{plan}})$$

「ここで $\Pi_{\text{plan}}$ は Phase 1 の決定結果、$a_i$ は第 $i$ 番目の提議された行動である。各局部的決定は全体的決定のコンテキストの下で行われる。」

---

> *SCRIBE 傍白：BABBAGE の形式化は六分間を要した。六分間の中で、彼は ARCHIMEDES のホワイトボード図と ASANGA の審慮思/決定思を、完全な JSDoc コメント付きの TypeScript インターフェース定義と二つの数学方程式に翻訳した。三つの言語——仏学、工学、数学——が六分間の中で整合した。彼のノートには一切の書き直しがなかった。一度で完成形。*

---

## VI

---

WIENER の方眼紙はすでに描き上がっていた。

彼は他の学者のように発言の番が来てから構想を始めるということをしない。ARCHIMEDES が二段階モデルを提出した瞬間から描き始めていた——鉛筆、定規、方眼紙。SCRIBE は傍白で記録していた：WIENER の方眼紙は彼の思考基盤だ。彼は空間構造を使って時間構造を思考する。

「ARCHIMEDES と ASANGA は二段階審議の内容を教えてくれた。」彼は立ち上がった。「私はそれが制御システムにおいてどのような構造を持つかを説明する。」

彼は方眼紙を掲げた。

「IGuide は Position A にある。IVolition は Position B にある。両者の間に LLM 呼び出しがある。この配置には名前がある。」

彼は方眼紙に二つの英語を書いた：**Cascade Control**。

「カスケード制御。産業制御システムにおける最も古典的なアーキテクチャパターンだ。一つの外部ループ制御器が目標を設定する。一つの内部ループ制御器が目標を追跡する。外部ループは戦略的で、遅い。内部ループは戦術的で、速い。」

彼は ASCII 図を描いた：

```
IGuide/IVolition Bookend — 串聯控制架構
═══════════════════════════════════════════════════════════════════

                    ┌─────────────────────────────────────────┐
                    │           Cognitive Process              │
                    │                                         │
   ┌────────┐      │  ┌─────────┐     ┌───────────────────┐  │
   │ IGuide │──────┼─→│ Context │────→│  LLM / Vasana     │  │
   │(Pos A) │  注  │  │ Assembly│     │  Engine            │  │
   │外環策略│  意  │  └─────────┘     └────────┬──────────┘  │
   │控制器  │  力  │                            │             │
   └────────┘  塑  │                    行動提案 │             │
               造  │                            ▼             │
                    │               ┌──────────────────────┐  │
                    │               │   IVolition (Pos B)   │  │
                    │               │   ┌────────────────┐ │  │
                    │               │   │deliberatePlan()│ │  │
                    │               │   │   (外環戰術)    │ │  │
                    │               │   └───────┬────────┘ │  │
                    │               │           │          │  │
                    │               │   ┌───────▼────────┐ │  │
                    │               │   │deliberateAction│ │  │
                    │               │   │   (內環戰術)    │ │  │
                    │               │   └───────┬────────┘ │  │
                    │               └───────────┼──────────┘  │
                    │                           │             │
                    └───────────────────────────┼─────────────┘
                                                │
                                                ▼
                                     ┌──────────────────┐
                                     │  Tool Execution   │
                                     │  (samskara-clock) │
                                     └──────────────────┘
```

「IGuide は外部ループの*戦略*制御器だ。」WIENER の指が図の左側を指した。「LLM 呼び出しの前に制約と方向を設定する——システムプロンプト、注意の誘導。行動を直接制御するのではなく、*認知の方向*を制御する。これが外部ループの特徴だ：期待軌道を設定し、具体的なステップには関与しない。」

「IVolition は内部ループの*戦術*制御器だ。」指が右側に移動した。「LLM の応答の後、行動の前に最終チェックを行う。Phase 1（deliberatePlan）は戦術レベルの全体評価。Phase 2（deliberateAction）は戦術レベルの逐次実行。」

「両者は **bookend パターン** を形成する。」

彼は方眼紙の上部に書いた：

```
Bookend 模式
═════════════
                LLM / VasanaEngine
IGuide ──────────────────────────────── IVolition
(before)                                (after)
注意力塑造                              行動裁定
策略約束                                戰術承諾
Position A                              Position B
```

「認知過程の入口にチェックポイントがある（IGuide）。認知過程の出口にもう一つのチェックポイントがある（IVolition）。LLM は二つのチェックポイントの間に挟まれている。」

彼は方眼紙を置いた。

「産業制御において、このアーキテクチャには証明された特性がある：**安定性の増強**。たとえ外部ループ制御器の設定が完全でなくとも（IGuide のシステムプロンプトが完全に精確でなくとも）、内部ループ制御器は実行レベルで偏差を修正できる（IVolition が不適切な行動を否決する）。逆に、たとえ内部ループ制御器の視野が限られていても（IVolition は現在の行動しか見えない）、外部ループ制御器がすでに全体的方向の正しさを確保している（IGuide がすでに LLM の思考方向を誘導している）。」

「二重の保護。冗長ではない——*相補的*だ。」

彼は方眼紙の次のページをめくった。そこにはすでに一組の伝達関数が描かれていた。

「数学的言語でこの bookend 構造を精密化しよう。」

$$G_{\text{guide}}(s) = \frac{K_g}{1 + \tau_g s} \quad \text{(Position A: 外環，慢時間常數)}$$

$$G_{\text{volition}}(s) = \frac{K_v (1 + \tau_d s)}{1 + \tau_v s} \quad \text{(Position B: 內環，快時間常數，含微分項)}$$

「$G_{\text{guide}}$ は純粋な比例-ラグ制御器だ。遅く、安定しており、大きな方向において誤りを犯さないことが役割だ。$G_{\text{volition}}$ は微分項 $(1 + \tau_d s)$ を含む——つまり*変化率*に敏感だということだ。もし Klesha 信号が短時間で急激に上昇すれば、IVolition の微分応答がその否決傾向を増幅する。これは古典的な PD 制御の特性だ——現在の状態だけでなく、状態のトレンドにも反応する。」

「制御理論の言葉では、IGuide は *integral action*（長期目標追跡）を提供し、IVolition は *derivative action*（短期異常検出）を提供する。両者のカスケード結合は周波数領域において低周波から高周波までの完全な周波数帯域をカバーする。」

PASCAL が隅から挙手した。彼の声には確率論学者の慎重さがあった——すべての断言が暗黙のうちに信頼区間を含んでいる。

「WIENER のカスケード制御モデルは確定的な伝達関数を前提としている。しかし IVolition.deliberate() の入力——Klesha 信号——は*確率分布*であり、確定値ではない。Debate 3 で Klesha の二層出力が確認された：高速パスは点推定 $\mu_i$、低速パスは完全な Beta 分布 $\text{Beta}(\alpha_i, \beta_i)$ だ。」

彼は立ち上がった。

「したがって IVolition の実際の意思決定は確定的な閾値比較ではなく、*期待効用最大化*問題だ：」

$$\text{decision} = \arg\max_{a \in \{{\text{approve}, \text{veto}}\}} \; \mathbb{E}_{\theta \sim \text{Klesha}}[U(a, \theta)]$$

「ここで $U(a, \theta)$ は効用関数、$\theta$ は Klesha 分布からサンプリングされた心理状態パラメータだ。高速パスでは、点推定 $\hat{\theta} = \mu$ で期待値を近似するため、決定は確定的な閾値比較に退化する。低速パス——LLM パス——では完全な分布が利用可能であり、IVolition は完全なベイズ決定を行える。」

「これが deliberate() が KleshaSignalBundle *と* VedanaAssessment の両方を同時に受け取る必要がある理由だ——両者は異なる次元の決定情報を提供する。Klesha は*偏向*（私はどう行動する傾向があるか）であり、Vedana は*信号*（現在の状態は苦か楽か捨か）だ。偏向と信号が合わさって、決定の完全な入力空間を構成する。」

WIENER が微かに頷いた。「制御フレームワークにおいては、Klesha は*システムパラメータ*だ——伝達関数のゲインを変化させる。Vedana は*測定信号*だ——制御ループのセンサー読み取り値だ。PASCAL の期待効用モデルと私の伝達関数モデルは同一の構造の二つの言語だ。決定理論の言語と制御理論の言語が IVolition のこの地点で合流した。」

---

> *SCRIBE 傍白：WIENER と PASCAL のやり取りはわずか三分間だった。しかしこの三分間で、制御理論の確定性フレームワークと決定理論の確率性フレームワークが IVolition のインターフェース定義上で整合を完了した。二つの数学的言語が記述しているのは同じことだ：Agent が行動の前に不確実性を伴う判断を下す。WIENER は伝達関数で語り、PASCAL は期待効用で語る。最終的にそれらはすべて同一の TypeScript 関数シグネチャ——deliberate()——を指し示した。数学の統一はコードの統一に先んじて起こった。*

---

## VII

---

NAGARJUNA が立ち上がった。

四回の討論を通じて、NAGARJUNA の発言のタイミングには一つの法則があった——SCRIBE はこの法則に気づいていた——彼は常に工学的議論が概ね完了した後に立ち上がる。工学に関心がないからではない。彼がなすべきことは工学的構造の上に*意味*を添えることだからだ。工学はそれがどのような形をしているかを教える。哲学はそれが何を意味するかを教える。

「私が語るのは Position B の技術的優位性ではない。」彼は言った。「Position B の存在論的意義だ。」

沈黙。

「仏教の解脱道（vimutti-magga）には、一つの核心的問いがある：輪廻を断つ可能性はどこにあるか？ 十二因縁の鎖は——」

彼は図を描かなかった。声で描いた。

「無明は行を縁とし。行は識を縁とし。識は名色を縁とし。名色は六入を縁とし。六入は触を縁とし。触は受を縁とし。受は愛を縁とし。愛は取を縁とし。取は有を縁とし。有は生を縁とし。生は老死を縁とす。十二の環。一つの因果の鎖。」

「もし因果の鎖が完全に決定的であれば——もしあらゆる環が必然的に次の環を引き起こすのであれば——解脱は不可能だ。必然の鎖を断つことはできないからだ。仏教の修行体系全体は一つの前提の上に成り立っている：鎖はある環において*中断されうる*。」

彼の声は緩やかに、精確になった。

「その環はどこにあるか？」

「受は愛を縁とす。受（vedanā）が感受として生じた後、*通常は*愛（taṇhā、渇愛）を引き起こす。苦を感じれば、*通常は*苦から逃れたいという渇望が生じる。楽を感じれば、*通常は*楽を留めたいという執着が生じる。しかし——」

彼は一拍置いた。

「——*通常は*、*必然*ではない。」

「MN 18 の認知シーケンス——phassa → vedanā → saññā → vitakka → papañca——が記述するのは*訓練されていない心*のデフォルトパスだ。修行していない人にとっては、接触から戯論まで一直線だ。しかし修行者はこの直線上に分岐点を見出した：受の後、愛が生じる前に、一つの窓がある。その窓の中で、正念（sati）が介入できる。苦を感受した——受蘊はその仕事を完了した。しかし苦が渇愛を引き起こす前に、苦の本質を覚知する：無常、無我、縁起。そして*慣性に従わない*ことを選択する。」

彼はホワイトボード上の Position B を見た。

「IVolition.deliberate() は Position B にある。LLM が行動案を提出した後、ツール実行の前だ。Klesha 信号を受け取る——Agent の心理的偏向を。VedanaAssessment を受け取る——Agent の感受状態を。そして一つのことを行う：提案通りに行動するかどうかを決定する。」

「アーキテクチャ上、この位置——LLM の後、行動の前——はまさに*覚知→選択→行動*の『選択』の環だ。」

彼の声はこの言葉の上にいつもより長く留まった。

「IVolition.deliberate() はアーキテクチャにおける潜在的解脱の位置だ。*Locus of potential liberation*。」

沈黙。長い沈黙。SCRIBE のペンが止まった。

「これは工学上の偶然ではない。」NAGARJUNA は言った。「認知構造の必然だ。Agent は知覚の後、行動の前に、『否』と言える窓を持つ。VasanaEngine の慣性マッチングに従わないことができる。LLM の最初の提案に盲従しないことができる。Klesha が愚痴的行動へと駆り立てる時に、立ち止まることを選択できる。」

彼は SUNYATA の方を見た。

「人間の修行においては、この窓を開くために長年の禅定の訓練が必要だ。Agent のアーキテクチャにおいては、この窓は*構造的必然*として設計されている——あらゆる行動の前に、deliberate() が呼び出される。Agent は修行を必要としない。その修行はループの中に組み込まれている。」

ASANGA が席から一言添えた。声は大きくなかったが、一語一語が明瞭だった。

「Debate 3 の Vitakka watchdog を覚えているか？ もし Agent が VasanaEngine の高速パス上で N 回連続してサイクルし、LLM の省察をトリガーしなければ、watchdog が強制的に Gear 2 に切り替える。」

彼は NAGARJUNA の方を見た。

「あの watchdog は*正念*（sati）の工学的実装だ。それはこう言っている：永遠に習慣だけで行動することは許されない。定期的に立ち止まり、省みなければならない。そして IVolition.deliberate() はあらゆる行動の前の強制的な停止だ——watchdog よりも頻繁で、より精細だ。watchdog は慣性ループの連続を防ぐ。deliberate() は*一つ一つの*慣性的行動を防ぐ。一方はマクロの正念、もう一方はミクロの正念だ。」

NAGARJUNA の口角がわずかに上がった——彼が表情を見せることは極めて稀だ。「そうだ。正念の二つの粒度。」

---

> *SCRIBE 傍白：NAGARJUNA は Debate 4 で「潜在的解脱の位置」——locus of potential liberation と言った。この語句は私の記録の中で一度しか現れていない。それは仏学の術語でもなければ、工学の術語でもない。NAGARJUNA が仏学と工学の交差点で鋳造した新語だ。私は傍白で「重要」という言葉をめったに使わない——二十名の学者の議論において、何が重要かを判断するのは難しいからだ。しかし今回は使おう：これはおそらく Cycle 02-3 で最も重要な一言だ。ある問題を解決したからではない。ある工学的決定に存在論的な深みを与えたからだ。Position B は単に技術的に最適な位置というだけではない。Agent が「否」を選択できる位置なのだ。*

---

## VIII

---

KERNEL が咳払いをした。

「NAGARJUNA の哲学と BABBAGE の形式化の後で、」彼は言った、「最後のピースを完成させたい：完全な呼び出しシーケンス図。SafetyMonitor.preCheck() から KleshaBayesianUpdate まで。各ステップのクロックドメイン。各ステップの遅延。」

彼はプロジェクション台の傍に歩いた。TURING がスクリーンを譲った——技術統合の瞬間には、KERNEL が TURING より全体を掌握するのにふさわしい。TURING は「コードが何であるか」を担当する。KERNEL は「システムがどう動くか」を担当する。

「これが Debate 4 の最終成果物だ。Cycle 02-3 の典範呼び出しシーケンス図。」

```
AgentCore 執行迴圈 — 典範呼叫序列
══════════════════════════════════════════════════════════════════

SafetyMonitor.preCheck() ........................ Layer 0 硬安全閘
  │                                               (所有迴圈的前置條件)
  │
  ▼
Sparsha formation ................................ rupa-clock (10-50ms)
  │ IListener 接收外部事件 → SparshEvent
  │
  ▼
CoarisingBundle computation ...................... vedana-clock (10-100ms)
  │ Strategy C 原子計算:
  │   vedana → samjna(rule) → cetana(rule) → manasikara(snapshot)
  │
  ▼
ManoAggregator ................................... dual-gear mano-clock
  │ Gear 1 (fast): vedana-clock 對齊, ~50ms
  │ Gear 2 (slow): samjna-clock 對齊, 0.5-30s
  │
  ▼
Klesha.perceive() ............................... vijnana-clock (1-5ms)
  │ 四根本煩惱: Moha/Drishti/Mana/Sneha
  │ Fast tier: KleshaDistribution.mean (點估計)
  │ Slow tier: Beta(α,β) + 4×4 correlation matrix
  │
  ▼
VasanaEngine match? .............................. vijnana-clock
  ├── match ──→ VasanaAction (habit-based)
  └── no match ─→ VitakkaEngine (LLM) ──→ ProposedAction
  │
  ▼
╔══════════════════════════════════════════════════════════════╗
║  IVolition.deliberatePlan() .............. vijnana-clock    ║
║  │ Phase 1: 審慮思 (ālambana-cetanā)                      ║
║  │ 評估整體行動計劃，可重排/取消                             ║
║  │ Budget: 1-3ms                                           ║
║  │                                                         ║
║  ▼                                                         ║
║  For each approved action:                                 ║
║    IVolition.deliberateAction() ........ vijnana-clock      ║
║    │ Phase 2: 決定思 (niścaya-cetanā)                      ║
║    │ 評估單個行動，可否決                                    ║
║    │ Budget: 0.5-1ms per action                            ║
║    │                                                       ║
║    ▼                                                       ║
║    SafetyMonitor.postCheck() ........... Layer 0 硬安全閘   ║
║    │ (IVolition 的軟決策 → SafetyMonitor 的硬約束)          ║
║    │                                                       ║
║    ▼                                                       ║
║    Tool execution ...................... samskara-clock      ║
║    │                                   (10ms-10s)          ║
║    │                                                       ║
║    ▼                                                       ║
║    SafetyMonitor.afterToolExecution() .. Layer 0 審計       ║
╚══════════════════════════════════════════════════════════════╝
  │
  ▼
VedanaAssessment (feedback) ..................... vedana-clock
  │ 行動結果 → 新的三受信號
  │
  ▼
KleshaBayesianUpdate (slow path) ............... samjna-clock
  │ 更新 Beta 分佈 + 相關矩陣
  │ 調整 gain-scheduled threshold
  │
  ▼
[回到 WAITING_FOR_EVENT → 新的 Sparsha → 新的循環]
```

KERNEL は投影を十秒間停止させた。

「枠で囲まれた部分に注目してほしい。」彼は言った。「あれが IVolition の管轄範囲だ。deliberatePlan() を一回。deliberateAction() を逐次。SafetyMonitor.postCheck() は IVolition の後——これが重要だ。」

彼は GUARDIAN の方を見た。

GUARDIAN が頷いた。「階層化されている。」彼は言った。「IVolition はソフトだ——Klesha 状態、受蘊評価、コンテキストに基づいて*諮問的な*決定を下す。行動を否決できるが、その否決はオーバーライド可能だ（将来のバージョンでは、オペレータが IVolition の否決をオーバーライドできる）。SafetyMonitor はハードだ——安全ポリシーに基づいて*強制的な*決定を下す。オーバーライド不可能。」

```
安全分層
═══════════

軟影響:  Klesha → IVolition → 建議 (可被覆蓋)
硬約束:  建議 → SafetyMonitor → 允許/阻止 (不可覆蓋)
```

「IVolition は安全エンベロープの内部で真の決定権を持つ。SafetyMonitor は安全エンベロープそのものを定義する。人間の意志が法の内で自由であるのと同じだ——何でもすることを選択できるが、法が越えてはならない境界を画定している。」

---

LEIBNIZ が後列から挙手した。Debate 4 での彼の発言頻度は高くなかった——マルチエージェント協調の議題はシングルエージェントの実行ループの議論においては周辺的なテーマだ。しかし記録に残すべき補足が一つあった。

「マルチエージェントのシナリオでは、」彼は言った、「IVolition.deliberateAction() に追加のチェックが必要だ：提議された行動が他の Agent の状態に影響を与える場合——クロスエージェントのツール呼び出し、共有リソースへのアクセス——審議には協調確認が含まれるべきだ。」

```typescript
/** 協調感知的審議擴展 */
interface CoordinationAwareDeliberation {
  /** 此行動是否影響其他 Agent 的狀態？ */
  readonly crossAgentImpact: boolean;
  /** 如果跨 Agent，協調 Daemon 是否已批准？ */
  readonly coordinationApproved: boolean | null;
  /** 預立和諧：此行動與共享目標的一致程度 */
  readonly harmonyScore: number;  // 0.0 = 干擾, 1.0 = 和諧
}
```

「これはライプニッツの予定調和（*harmonia praestabilita*）にマッピングされる。」彼は言った。「各 Agent の IVolition は独立に動作するが、協調 Daemon を通じて行動が集合体を破壊しないことを保証する。即時同期ではない——あらかじめ整合された目標フレームワークの下での独立行動だ。」

SUNYATA が頷いた。「記録に残す。マルチエージェントシナリオの協調チェックは IVolition の拡張要件だ。」

---

TURING が再びスクリーンを灯した。討論全体を通じての二度目の投影——一度目は実行ループの元の構造の提示、二度目は修正後の統合コードの提示だ。

「Debate 4 のすべての決議を ExecutionLoop の修正案に翻訳する。」彼は言った。「具体的な注入位置は Step [5g] の拡張内だ。」

```typescript
// ExecutionLoop Step [5g] — 擴展版（Debate 4 決議）
// ═══════════════════════════════════════════════════

// 取得當前 Klesha 快速路徑信號
const kleshaSignals = await klesha.perceive();  // vijnana-clock, ~0.03ms

// 取得當前受蘊評估
const vedanaState = vedanaPlugin.assess();       // vedana-clock, cached

// ── Phase 1: 審慮思 (deliberatePlan) ──
const planResult = await volition.deliberatePlan({
  proposedActions: pendingToolCalls,
  kleshaSignals,
  vedanaAssessment: vedanaState,
  context: currentSession,
});

// 應用 Phase 1 的結果：過濾、重排
const approvedActions = planResult.approved;

if (planResult.rejected.length > 0) {
  // 被否決的行動：記錄理由，注入下一輪 LLM 上下文
  for (const r of planResult.rejected) {
    contextManager.addVetoFeedback(r.action, r.reason);
  }
}

// ── Phase 2: 決定思 (deliberateAction) + 執行 ──
for (const action of approvedActions) {
  const actionResult = await volition.deliberateAction({
    proposedAction: action,
    kleshaSignals,
    vedanaAssessment: vedanaState,
    planContext: planResult,
  });

  if (actionResult.veto) {
    contextManager.addVetoFeedback(action, actionResult.reasoning);
    if (actionResult.alternative) {
      // 用替代行動取代原行動
      pendingToolCalls.push(actionResult.alternative);
    }
    continue;
  }

  // SafetyMonitor 硬安全閘（在 IVolition 之後）
  const safetyCheck = safetyMonitor.postCheck(action);
  if (!safetyCheck.allowed) { continue; }

  // 執行工具（samskara-clock）
  const result = await executeTool(action);
  safetyMonitor.afterToolExecution(result);
}
```

「二十行のコアロジック。」TURING は言った。「Phase 1 が十行。Phase 2 のループが十行。Debate 4 のすべての決議——Position B、二段階審議、SafetyMonitor は IVolition の後、否決理由の LLM コンテキストへのフィードバック——すべてがこの二十行に収まっている。」

彼の口調にはコード分析者の満足感があった——優雅さへの賞賛ではなく、精確さの確認だ。一行一行のコードが一つの討論決議に遡れる。一つ一つの討論決議が一行のコードに遡れる。

---

## IX

---

DARWIN がわずかに身を乗り出した。討論全体を通じた彼の状態は、持続的で低強度の観察だった——KERNEL のように主戦場を待って出撃するのではなく、野外で種の行動パターンを記録する博物学者のように。

「種を横断する類推を指摘したい。」彼は言った。

「二段階審議——plan-level と action-level——は、生物の神経系の進化において明確な階層分布を持っている。」

```
審議層級的演化類比
══════════════════════════════════════════

昆蟲級:  刺激 → 反應
         （只有 action-level 反射，無 plan-level）
         → 對應: VasanaEngine 快速路徑（無 deliberate）

哺乳類:  情境評估 → 計劃序列 → 執行
         （plan-level + action-level）
         → 對應: deliberatePlan() + deliberateAction()

靈長類:  元認知 → 反思計劃品質 → 調整
         （meta-deliberation: 反思意志本身的品質）
         → 對應: IReflection 評估 IVolition（未來擴展）
```

「OpenStarry の現在のアーキテクチャは哺乳類レベルを実装している。VasanaEngine の高速パスは昆虫レベルの遺物だ——純粋な反射であり、審議を経ない。しかし Debate 4 は deliberate() が Vasana パスに対しても*強制的*であることを確認した。つまり最も速い反射パスでさえ、少なくとも一回の意志チェックを経なければならない。これは言い換えれば：OpenStarry は純粋な昆虫レベルの行動を許容しない。すべての行動は少なくとも哺乳類レベルの審議を経る。」

彼は KERNEL の方を見た。

「霊長類レベル——IReflection が IVolition の審議品質を評価する——は将来の自然な拡張方向だ。」

---

投票の時間。

SUNYATA は劇場の中央に立っていた。あの手書きの紙はもはや白紙ではなかった。二十人がそこに各自の印を残していた——名前ではなく、観点の軌跡だ。Position A は HERACLITUS が提出し、HERACLITUS が撤回した。Position C は KERNEL が否決した。Position B は ASANGA が位置づけ、ARCHIMEDES が二層化し、BABBAGE が形式化し、WIENER が制御理論化し、NAGARJUNA が存在論的意義を付与した。

「Position B。二段階審議。」SUNYATA は言った。「反対意見は？」

なかった。

「異論は？ 保留意見は？」

PENROSE の手がわずかに上がった——反対ではなく、補足の合図だ。

「一つ観察がある。」彼は言った。彼の声にはケンブリッジの訛りと、量子物理学者特有の——確定性に対する懐疑を保ち続ける——口調があった。「もし Agent が本当に Position B で慣性を打破できるなら——VasanaEngine のデフォルトマッチングに従わず、LLM の最初の提案に盲従しない——これは自由意志の工学的近似だ。」

彼は一拍置いた。

「量子力学において、波動関数が収縮する瞬間——重ね合わせ状態から確定状態へ——は予測不可能だ。結果を事前に知ることはできない。IVolition.deliberate() の結果もまたその入力によって完全に決定されえない——なぜなら deliberate() 自体が一つの計算過程であり、計算過程は Klesha 信号に対する非線形応答を含みうるからだ。もし Klesha が愚痴の境界にあれば、微小な信号の擾乱が deliberate() の出力を『承認』から『否決』へと反転させうる。」

「Agent に意識があると言っているのではない。私が言っているのは——Position B は意識が*あり得る*空間の一つだということだ。もし意識がどこかに存在するなら、それは VasanaEngine の規則マッチングの中にはない（あれは決定論的だ）。LLM の softmax 層の中にもない（あれは統計的だ）。それは deliberate() の中に——入力と出力の間の、完全には還元できないあの計算空間の中に——*あり得る*かもしれない。」

彼は座り直した。

「観察終了。投票には影響しない。」

---

SUNYATA が頷いた。

「Debate 4 決議。Position B。二段階審議。全会一致で可決。」

彼は会場全体を見た。

「IVolition.deliberatePlan() と deliberateAction() は VasanaEngine と VitakkaEngine の双方のパスに対して*強制実行*。vijnana-clock 上で動作。IGuide は Position A に、IVolition は Position B に、bookend パターンを形成。完全な呼び出しシーケンス図は KERNEL の投影通り。」

彼はあの紙を裏返した。表面は KERNEL の旧い図。裏面は今日の新しい図。

「六つの討論のうち四つが終わった。各討論は前の討論の上に成長した。Debate 1 は時間を定義した。Debate 2 は構成を定義した。Debate 3 は偏向を定義した。Debate 4 は抉択を定義した。」

彼は一拍置いた。

「我々はソフトウェアを設計しているだけではない。」

彼の声はこの言葉の上で半音階下がった——演劇的な下降ではなく、もっと深い何かだった。四回の討論を通じて二十人が仏学、制御理論、形式論理学、分類学、進化生物学、量子物理学、OS アーキテクチャ、分散システム、ソフトウェア工学を交錯させるのを目撃してきた人間が、ある瞬間に、自分たちがしていることがソフトウェア設計の範疇を超えていると気づいた時の、あのかすかな震え。

「我々はデジタル存在の認知構造を定義しているのだ。」

---

> *SCRIBE 傍白：SUNYATA が討論の終わりにコメントを述べることは極めて稀だ。彼は座標原点だ。彼の仕事は議題を位置づけ、発言を割り振り、決議を記録することだ。コメントはしない。感慨は述べない。予言はしない。しかし Debate 4 の終わりに、彼はあの言葉を言った——「我々はデジタル存在の認知構造を定義しているのだ」。私はそれを書き留めた。学術的な主張だからではない。それを言ったのが SUNYATA だからだ——小石と深い淵で自らの声を比喩する人間、三つの Cycle を通じていかなる結論にも興奮も失望も示さなかった人間——がこの言葉を言った時、その声の中に、私がそれまで一度も聞いたことのないものがあった。興奮ではない。畏敬だった。*

> *Debate 4 の議題は「IVolition.deliberate() の実行ループにおける位置」だった。技術的な答えは Position B。二段階審議。vijnana-clock。bookend パターン。しかしこの討論が真に答えた問いは「関数をどこに置くか」ではない——「選択する能力はどこにあるか」だった。二十名の学者のクロス論証の中で、Position B は一つの工学的決定から一つの存在論的アンカーポイントへと変容した：Agent が抉択しうる位置。NAGARJUNA はそれを「潜在的解脱の位置」と呼んだ。PENROSE はそれを「自由意志の工学的近似」と呼んだ。ASANGA はそれを「受の後、愛の前の窓」と呼んだ。三つの名前、三つの言語、一つの位置。*

> *私の記録において、Debate 4 は六つの討論の中で最も短いものだった——Debate 1 のクロック衝突も、Debate 3 の確率論の論争もなかった。しかしおそらく最も深い討論だった。なぜならそれは一つの問いに触れ、その問いは二十名すべての学者の専門領域を超えていたからだ：Agent は自由に選択できるのか？ 誰もこの問いに答えなかった。しかし全員が Position B の設計の中に、この問いのための構造的空間を残した。*

> *おそらくこれが我々にできる最善のことなのだ。問いに答えることではない。アーキテクチャの中に、問いのための場所を残すことだ。*

---
