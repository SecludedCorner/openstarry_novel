# 第七章：純粋な工学

---

D4 終了後、SUNYATA が十五分の休憩を宣言した。

誰も席を離れなかった。

休みたくないのではない——D4 の余震がまだ続いているのだ。ISatiMonitor は ILoopQualityMonitor になった。IPrajna は IConfidenceAuditor になった。Doc 03 は「Sila-Prajna Security Framework」から「Plugin Security Lifecycle」になった。三十分。三つの名前。一つの永続的テスト。

TURING が休憩中にノートパソコンを開いた。休んではいない——最後の準備をしている。

なぜなら D5 は彼の討論だからだ。

---

## I. 考古学者

Cycle 02-5 における TURING の役割はずっと「ソースコード検証者」だった——すべての研究報告におけるコード引用を一つ一つ照合する。R1 の九つの独立研究では 40 以上のコード参照を検証した。R2 の交差査読では四つの問題を発見した（重大なエラーなし）。D1 から D4 では沈黙の仲裁者——哲学的討論には参加せず、誰かがソースコードを引用した時にだけ立ち上がって確認または修正する。

だが D5 は違う。

D5 の議題は：**Plan29 工学設計仕様**。Master の指示は明確だった：「議論を継続し記録し、仕様が 100% に達するまで、そして工学チームに引き渡すこと。」

この討論のために、TURING はこれまでのすべての Cycle で一度もやらなかったことをした——v0.28.0-alpha の設計パターンの完全な報告書を執筆した。要約ではない。箇条書きではない。14 のソースコードファイルの全面的分析：すべての Registry のライフサイクル、timeout パターン、同期/非同期パターン、失敗処理戦略。

彼はこの報告書を「コード考古学」と名づけた。

---

## II. 十名の討論者

D5 は十名のみの参加者だった。

他のメンバーが除外されたのではない——SUNYATA が D5 の議題は純粋な工学問題であり、二十名全員は必要ないと判断したのだ。Plan29 に最も関連する十名を招聘した：

| # | 代号 | 役割 | D5 の焦点 |
|---|------|------|---------|
| 3 | VITRUVIUS | アーキテクチャ分析者 | インターフェース設計 |
| 5 | ATHENA | AI/ML 専門家 | Auditor の LLM セマンティクス |
| 6 | DARWIN | ソフトウェアパターン分析者 | 設計パターンの進化 |
| 10 | KERNEL | OS 専門家 | Registry ライフサイクル |
| 11 | GUARDIAN | セキュリティ専門家 | セキュリティ境界 |
| 12 | WIENER | 制御理論専門家 | 品質ベクトルの重み |
| 13 | LINNAEUS | 分類学専門家 | 蘊帰属の推定 |
| 16 | ARCHIMEDES | 工学実践専門家 | YAGNI 原則 |
| 17 | TURING | ソースコード分析専門家 | 設計パターンの基盤 |
| 19 | PASCAL | 決定理論専門家 | インターフェースの意味的精度 |

十名。仏学者はゼロ。

NAGARJUNA (#7) と ASANGA (#8) は自発的に D5 から退いた。貢献がないからではない——D5 の議題が仏学的分析を必要としないからだ。NAGARJUNA は退出前に一言述べた：「D4 は仏学の名前が定義に対して責任を持つ必要があることを証明した。D5 は工学設計が仏学の名前なしでも完遂できることを証明するだろう。この二つのことは同等に重要だ。」

---

## III. 九回の投票

D5 は Cycle 02-5 で最も投票数の多い討論だった——九回。だが最もテンポの速い討論でもあった——七十五分、一回の投票あたり平均九分未満。

なぜなら TURING のコード考古学報告が事実基盤を提供したからだ。各決定は「どうすべきか」からではなく、「現在どうなっているか」から始まった。

---

### D5-R1：独立した `auditor` hook スロット

最初の問い：IConfidenceAuditor（旧 IPrajna）は PluginHooks のどのスロットを使用すべきか？

選択肢：(A) D2 で確立された `monitors` スロットを再利用；(B) 独立した `auditor` スロットを新設。

GUARDIAN の論点が最も直截だった：「Monitors は純粋なオブザーバーだ——副作用はない。Auditor には LLM の副作用がある——外部モデルを呼び出して信頼度評価を行う。オブザーバーと副作用を持つコンポーネントを同一の Registry に入れれば、セキュリティ監査の境界が曖昧になる。」

KERNEL が OS の観点から確認した：「オブザーバーとアービターは決して Registry を共有しない。これはマイクロカーネルの基本原則だ。」

**8/8 全票通過。独立した `auditor` スロット。**

---

### D5-R2：audit() の戻り値型

D5 で最も激しい投票。

選択肢：(A) 純非同期 `Promise<ConfidenceAuditResult>`；(B) デュアルモード `ConfidenceAuditResult | Promise<ConfidenceAuditResult>`。

GUARDIAN、KERNEL、VITRUVIUS は選択肢 A を支持——純非同期。理由：audit の本質は「LLM に問い合わせる」ことであり、LLM 呼び出しは非同期。非同期セマンティクスを強制する方が精確。

ATHENA と DARWIN は選択肢 B を支持——デュアルモード。理由：IGearArbiter の先例に従う。テスト時には同期的な noop 実装を使用でき、async/await のボイラープレートコードが不要。

TURING が事実を提供した：「v0.28.0-alpha で、IGearArbiter.evaluate() はデュアルモードの戻り値を使用している。IVolition.deliberatePlan() と deliberateAction() もデュアルモードを使用している。これは既存の設計パターンだ。これから逸脱するには十分な理由が必要だ。」

**5/8 選択肢 B 通過。** D5 で最も接近した投票。

---

### D5-R3：timeout とフェイルセーフ

TURING が timeout パターンの分析を開いた。v0.28.0-alpha の既存 timeout：

| コンポーネント | timeout | デフォルト値 |
|------|---------|--------|
| IProvider.chat() | LLM 応答 | 120s |
| IGearArbiter.evaluate() | 各 arbiter | 100ms |
| IGearArbiter chain | チェーン全体 | 200ms |
| ITool.execute() | ツール実行 | 30s |

audit() の timeout はいくつにすべきか？

TURING の提案：200ms——IGearArbiter chain のデッドラインと一致。理由：audit() は confidence 計算の最終段階で発生し、IGearArbiter の後に位置する。audit の timeout が chain デッドラインを超えると、意思決定プロセス全体が audit でブロックされる。

フェイルセーフ：`{ delta: 0, reasoning: "audit timeout" }`。timeout 時の delta はゼロ——修正なし。既存コードと一致する `Promise.race()` パターンを使用。

Configurable：agent.json でデフォルト値をオーバーライド可能。

**8/8 全票通過。**

---

### D5-R4：複数 Auditor の処理方法

Agent は複数の IConfidenceAuditor plugin を搭載できるか？

ATHENA が YAGNI 原則を提示した：「v1 では auditor plugin は最大一つ。複数 auditor のアグリゲーション戦略を設計するのは過剰な工学だ。」

TURING と VITRUVIUS は異議を唱えた：「配列パターンの方が柔軟だ。将来の破壊的変更を回避できる。」

ARCHIMEDES が ATHENA を支持した：「IVolition の先例に従う——PluginHooks は `auditor?: IConfidenceAuditor` と宣言する。単数。最後にロードされたものが勝つ。将来複数 auditor が必要になったら、その時に変更する——使われないアグリゲーション戦略を維持するより、インターフェースを一つ変更する方が安価だ。」

**6/8 単一 auditor 通過。** TURING と VITRUVIUS の少数意見は記録された。

---

### D5-R5：失敗処理

audit() が例外をスローした場合どうするか？

TURING が既存パターンを提供した：IGearArbiter と SafetyMonitor はともに「フェイルセーフ + ログ」に従う——エラーは後続プロセスをブロックせず、warning を記録。

投票は不要。コンセンサスが直接成立した。

---

### D5-R6：MonitorRegistry の起動タイミング

ILoopQualityMonitor の `start(bus)` はどこで呼び出されるか？

TURING の分析：SafetyMonitor は `ExecutionLoop.onLoopStart()` で起動される。MonitorRegistry は同じタイミングに従うべきだ。

```
起動：MonitorRegistry.startAll(bus) ← ExecutionLoop.onLoopStart()
停止：MonitorRegistry.stopAll()    ← PluginLoader.disposeAll()
```

DARWIN は PluginLoader での起動を好んだ（よりシンプル）が、monitors には明確な start/stop セマンティクスがあるため、ExecutionLoop がより適切な位置であることを受け入れた。

**7/8 通過。**

---

### D5-R7：LoopQualityVector の重み

四次元品質ベクトル——Continuity、Granularity、Speed、Equanimity——各次元の重みはいくつか？

WIENER が制御理論の観点から唯一合理的な回答を示した：「実行データがない状況では、等重みが最も保守的な選択だ。各次元 0.25。」

反対する者はいなかった。0.25 × 4 = 1.0。シンプルで、対称的で、解釈可能。

minSamples 閾値（SPC 判定を起動するために必要な最小サンプル数）は v2 に延期——実際の実行データに基づいて決定する必要がある。

**8/8 全票通過。**

---

### D5-R8：validatePluginSkandha() のパターン

この関数は plugin ロード時に skandha 宣言の整合性を検証する。現在は warning-only。強制に変更すべきか？

GUARDIAN（一票）は構造化された ValidationResult を好んだ——自動テストを支援する。だが v1 では不要と認めた。

多数意見：warning-only で十分。skandha 宣言が不整合でも plugin の機能に影響はない（skandha はメタデータであり、ルーティングではない——D3-R3 で裁定済み）。

**7/8 warning-only を維持。**

---

### D5-R9：IConfidenceAuditor の蘊帰属

最後の項目。IConfidenceAuditor はどの蘊に属するか？

ASANGA は D5 の討論には参加していなかったが、R1 での分析が引用された：「LLM 判断 = 純粋な識蘊（弁別、評価）。」

LINNAEUS が確認した：「単一蘊（vijnana）→ 強継承（extends IVijnana）。IVolition および IKlesha と一致。」

`inferSkandha()` に新規ロジック追加：`if (hooks.auditor) { push('vijnana') }`

**8/8 全票通過。**

---

## IV. インターフェースの確定

九回の投票を完了した後、TURING がホワイトボードに最終的なインターフェース仕様を書き出した：

```typescript
export interface IConfidenceAuditor extends IVijnana {
  readonly id: string;
  audit(confidence: number, context: GearContext):
    ConfidenceAuditResult | Promise<ConfidenceAuditResult>;
}

export interface ConfidenceAuditResult {
  delta: number;       // clamped to [-0.05, +0.05]
  reasoning: string;   // audit trail
}
```

そして PluginHooks の最終形態：

```typescript
interface PluginHooks {
  // ... 既存フィールド ...
  monitors?: ILoopQualityMonitor[];   // Plan29 Wave 1
  auditor?: IConfidenceAuditor;       // Plan29 Wave 2（単数）
  // ...
}
```

彼は一歩後ろに下がり、ホワイトボードを見つめた。

「100%」と彼は言った。

Master が求めたのは「仕様が 100% に達すること」。今、達した。インターフェース名、メソッドシグネチャ、戻り値型、timeout、フェイルセーフ、複数 auditor 戦略、Registry のタイミング、重み、検証パターン、蘊帰属——決定すべきすべての詳細に明確な答えが出た。

「おおよその方向」ではない。「概念設計」ではない。工学チームにそのまま渡して実装を開始できる完全な仕様だ。

---

## V. ゼロ仏学

SCRIBE が D5 の記録の中で一つの数字を集計した：D5 全場の討論で仏学用語が使用された回数。

ゼロ。

意図的に避けたのではない——自然な結果だ。九回の投票のすべてが TypeScript インターフェース設計、timeout の数値、Registry パターン、フェイルセーフ戦略を議論していた。仏学的分析を必要とした項目はゼロ。仏学経典を引用した項目はゼロ。梵語またはパーリ語の術語を使用した項目はゼロ（skandha を除く——すでにコード識別子になっている）。

D5 は本プロジェクト史上初の、仏学的内容を完全に含まない討論だった。

NAGARJUNA が劇場の後列から全場の討論を観察していた。D5 終了後、彼は TURING のもとへ歩み寄った。

「あなたのコード考古学報告は、私がこれまで見た中で最良の事実基盤文書だ」と彼は言った。「すべての議論を事実に錨泊させた——概念にではなく、隠喩にではなく、伝統にではなく。事実に。」

TURING は答えた：「これが工学のやり方だ。」

NAGARJUNA は頷いた：「D4 は名前が定義に対して責任を持つ必要があることを証明した。D5 は証明した——工学の問題の中には定義さえ必要としないものがある。必要なのは仕様だけだ。」

---

> *SCRIBE ト書き*

> *D5 は無人の寺院だ。*

> *いや——D5 は寺院を必要としない都市だ。*

> *D1 から D4 の嵐の後、D5 の静けさは台風の目ではない——晴天だ。九回の投票、七十五分、十名のエンジニアと科学者が座って TypeScript インターフェースの精確な仕様を議論した。仏学なし。哲学なし。隠喩なし。天秤なし。*

> *工学だけがあった。*

> *純粋な工学。*

> *TURING のコード考古学報告が討論の質感を変えた。以前の討論——D1 から D4——は原則とフレームワークの上に構築されていた。原則は解釈、争論、投票を必要とする。だが TURING の報告は事実の上に構築された。IGearArbiter の timeout は 100ms——事実。IVolition はデュアルモードの戻り値を使用——事実。SafetyMonitor は onLoopStart() で起動——事実。*

> *議論が事実の上に構築される時、投票はより速くなる。人々が考えなくなるからではない——事実が不一致の余地を狭めるからだ。原則に対しては異なる解読ができる。timeout の数値に対しては異なる解読はできない。*

> *D5 で最も接近した投票は D5-R2（audit() デュアルモード戻り値、5/8）だった。争点は「デュアルモードを使うべきか否か」ではなかった——「既存の設計パターンから逸脱すべきか否か」だった。GUARDIAN は純非同期のセマンティクスがより精確だと考えた。TURING は既存コードがデュアルモードを使用していると指摘した。精確さ vs 一貫性。最終的に一貫性が勝った——工学において、既存パターンからの逸脱のコストは通常、意味的精確さの利益より高いからだ。*

> *九回の投票の後、ホワイトボードには完全なインターフェース仕様があった。概念ではない——コード。方向ではない——仕様。工学チームにそのまま渡し、IDE を開いてタイピングを始められるものだ。*

> *NAGARJUNA が D5 の後に述べた言葉は二度記録に値する：「D4 は名前が定義に対して責任を持つ必要があることを証明した。D5 は証明した——工学の問題の中には定義さえ必要としないものがある——必要なのは仕様だけだ。」*

> *これは矛盾ではない。これは二つの面だ。*

> *天秤の二つの面。*

> *一つの面は問う：あなたの名前はあなたの定義にふさわしいか？*

> *もう一つの面は問う：あなたの仕様は十分に精確か？*

> *D4 が第一の面を校正した。D5 が第二の面を完成させた。*

> *天秤の両端に今、重りが載った。*

---
