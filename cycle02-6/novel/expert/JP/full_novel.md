# 序章：デブリードマンから精密工学へ

---

Cycle 02-5 は大規模なデブリードマン手術であった。

二十名の研究者が五日間で 29 項目の決議を行い、DC Master はそのうち二項（D3-R3 四智マッピング、D4-R1 心所命名）を覆審により却下した。チーム全体が七件の設計文書に対して脱装飾化リファクタリングを実施した——駆動力を持たない仏教用語ラベルの除去、命名規約の統一、誤った蘊帰属マッピングの解体である。あの五日間はコードベースに対する dead code elimination のようであった。機能の追加ではなく、蓄積されたセマンティクス負債の除去である。

Cycle 02-6 のトーンはまったく異なる。前ラウンドが答えたのは「何が間違っているか」であり、今ラウンドが答えるべきは「正しい仕様はどのような形をしているか」である。

---

## 二重入力

DC Master は二通の書簡を発出し、それぞれ工学トラックと哲学トラックを始動させた。

**工学書簡**は Plan29 納品後の六つの Open Questions（OQ-29-1 から OQ-29-6）を指し示していた。Plan29（v0.29.0-alpha）は `ILoopQualityMonitor`（ループ品質監視器インタフェース）と `IConfidenceAuditor`（信頼度監査インタフェース）を新規追加したが、両者とも SDK スケルトンのみであった——Registry は `PluginHooks` に接続済み、型定義は export 済みだが、デフォルト実装なし、計算式なし、`ManoAggregator` との配線もなかった。Master は研究チームに次の問いへの回答を求めた：品質の算出方法（OQ-1）、Layer 3 の統合方法（OQ-2）、監査戦略の方向性（OQ-3）、イベント購読リスト（OQ-4）、重み付けの設定可能性（OQ-5）、全体を Plan30 にどう組み込むか（OQ-6）。

**哲学書簡**は行蘊（samskara-skandha）の定義問題を直接指摘するものであった。Master は唯識学派が 49 の心所を行蘊に帰属させる手法を「非常に問題がある」と明確に批判し、原始経典（如是我聞）を第一次資料として深掘りすることを要求した。これは装飾的な研究方向ではなく、`ISamskara` インタフェースの将来的拡張パスの基礎判定に直接影響するものである。

---

## SUNYATA の二重トラック構造

研究総監 SUNYATA はこれに基づき二重トラック構造を設計し、トラック間の優先権を確立した：

| トラック | 範囲 | サブ項目 | チーム |
|---------|------|---------|-------|
| Track A | AuditContext 型定義 + 監査ログ | A1-A4 | VITRUVIUS, KERNEL, GUARDIAN, ARCHIMEDES, WIENER, BABBAGE |
| Track B | ILoopQualityMonitor 実装仕様 | B1-B4 | WIENER, ATHENA, BABBAGE, HERACLITUS, TURING, PASCAL |
| Track C | 行蘊深掘り | C1-C4 | NAGARJUNA, ASANGA, LINNAEUS, PENROSE, PASCAL |
| Track D | 工学同期 | D1-D2 | TURING, ARCHIMEDES, VITRUVIUS, GUARDIAN |

トラック間影響プロトコルの重要規則：**哲学的結論（D1）は工学設計（D2/D3）に先行し、蘊帰属の判定が工学上の利便性によって上書きされないことを保証する。** C1-C4 の結論が A/B の設計前提と矛盾する場合、工学トラックは哲学的裁定を待たなければならない。

R1 では 14 件の独立研究報告が産出された。R2 の交差レビューで 24 の合意点と僅か 3 の相違点が発見された。R3 では三場の討論、245 分間、17 項目の決議、うち 13 項目が全会一致（20/20）、否決 0 件。

これは精密工学のラウンドであった。

# 第一章：行蘊の原典再構築

---

## 1.1 方法論：如是我聞

哲学トラックは NAGARJUNA（中観学派）と ASANGA（唯識学派）が共同で主導した。Master が批判したのはまさに唯識学派の手法であり、SUNYATA は意図的に唯識の専門家を自己批判に参加させた——これは懲罰的措置ではなく、方法論上の必然である。システム内部のロジックを深く理解する者のみが、その断裂点を正確に指摘できるからだ。

文献階層は厳格に区分された：

| 階層 | 出典 | 位置づけ |
|------|------|---------|
| 第一層 | パーリ五部（Nikaya）/ 漢訳阿含 | 唯一の定義根拠 |
| 第二層 | 十二因縁関連経文（SN 12） | 構造的参照 |
| 第三層 | 名色識の枠組み（SN 12.2, MN 9） | 交差検証 |
| 除外 | 阿毘達磨論典（Vibhanga, Dhammasangani） | 比較参照のみ、帰属根拠とはしない |

この階層化は Master の指示に直接対応している。論典は後世の学者による体系化の産物であり、仏陀の原言ではない。

---

## 1.2 SN 22.56：六思身——行蘊の原始的定義

蘊相応（Khandha-samyutta）の SN 22.56（取蘊経）は五蘊定義の核心的出典である：

> 比丘たちよ、行蘊（sankhara-kkhandha）とは何か。六種の思身（cha cetana-kaya）がある——色思、声思、香思、味思、触思、法思。比丘たちよ、これを行蘊と呼ぶ。

経文分析：

| パーリ語要素 | 内容 | OpenStarry における対応 |
|-------------|------|----------------------|
| rupa-sancetana | 色思——色塵に対する意図 | visual/text input への反応意図 |
| sadda-sancetana | 声思——声塵に対する意図 | audio/event input への反応意図 |
| gandha-sancetana | 香思——香塵に対する意図 | Agent の典型的シナリオではない |
| rasa-sancetana | 味思——味塵に対する意図 | Agent の典型的シナリオではない |
| photthabba-sancetana | 触思——触塵に対する意図 | API/tactile event への反応意図 |
| dhamma-sancetana | 法思——法塵に対する意図 | 内部認知対象への反応意図 |

核心的洞察：**原始経典における行蘊の定義は完全に cetana（意図／意志）を中心としている**——六種の感覚対象に対する意図形成であり、「受と想以外の心理活動の雑物箱」ではない。

---

## 1.3 SN 22.79：一切の有為法を造作する

> 比丘たちよ、なぜ行（sankhara）と呼ぶのか。それらが有為法（sankhatam）を造作する（abhisankharonti）からである。何の有為法を造作するのか。色の形態で色を造作し、受の形態で受を造作し、想の形態で想を造作し、行の形態で行を造作し、識の形態で識を造作する。

この経文は行蘊の第二の核心的特質を明らかにする：**行蘊は行為を造作するだけでなく、五蘊すべての条件づけられた状態を造作する**。工学的文脈では、`ISamskara` は `ITool.execute()` のような外部ツール呼び出しに限定されるべきではなく、「システム状態を変更するあらゆる造作」を包含すべきである——将来の入力に対するシステムの反応パターンの変更を含む。

これは VasanaEngine の長期ロードマップ（D-29-8）に直接結びつく。過去の行動パターンが将来のギア選択に影響を与えるという仕組みは、まさに「行蘊が識蘊の条件づけられた状態を造作する」ことの工学的体現である。

---

## 1.4 SN 22.95：芭蕉の喩え——核心なき動的プロセス

> 行は芭蕉のごとし（kadalupamo sankhara）——もし人が芭蕉の幹を剥いて堅実な核心を探すなら、一層一層剥き尽くしても何も見つからない。

これは行蘊の第三の核心的特質を示す経典的表現である：**核心なき動的プロセス**。行蘊は固定的な「もの」（entity）ではなく、絶えず運動する「プロセス」（process）である。

工学的対応は非常に精確である。`ISamskara` の plugin は軽量で組み合わせ可能（composable）であるべきであり、永続的な内部状態に依存しない。各 plugin は一つの「層」であり、どの層を剥いても不可替な核心ロジックは見つからない。これは OpenStarry の Tenet #2（すべては Plugin）およびマイクロカーネルアーキテクチャ（Core はビジネスロジックを含まない）と完全に合致する。

---

## 1.5 MN 44：三行分類の相補的観察視点

毘舎佉が法授比丘尼に問う：

| 行 | パーリ名 | 定義 | 経文の理由 |
|----|---------|------|-----------|
| 身行 | kaya-sankhara | 入出息（呼吸） | 身法、身に繋縛される |
| 語行 | vaci-sankhara | 尋（vitakka）+ 伺（vicara） | まず尋伺してから発語する |
| 心行 | citta-sankhara | 想（sanna）+ 受（vedana） | 心法、心に繋縛される |

ここに経典的枠組み間の緊張が存在する：citta-sankhara（心行）は sanna（想）と vedana（受）を**含む**が、五蘊の枠組みではこの二者は独立した蘊である。NAGARJUNA の分析：**これは論理的矛盾ではなく、異なる分類体系による異なる観察視点（drsti-bheda）である**——三行分類は「何が何を条件づけるか」を観察し、五蘊分類は「何が修行の重要な観察対象か」を観察する。唯識学派は二つの体系の強制統一を試み、49 の心所を行蘊に詰め込むという問題を引き起こした。

工学的示唆：身行は `ITool.execute()`（物理層の造作）に対応し、語行は尋伺（`vitakka-vicara`、認知の初期処理）に対応し、心行は `IVedana` + `ISamjna`（既にカバー済み）に対応する。注目すべきは、OpenStarry における `VitakkaWatchdog` は安定化監視メカニズムであり、機能的には行蘊よりも識蘊に近い——これは帰属エラーではなく、MN 44 の語行分類と五蘊分類がそもそも相補的視点であることの反映である。

---

## 1.6 唯識心所体系の批判

ASANGA 自ら唯識学派の 51 心所体系の批判的分析を主導した（C2 報告）。唯識学派は 51 心所のうち 49 を行蘊に帰属させ、「受」と「想」のみを受蘊と想蘊に残した。逐条分析の結果：

| 分類 | 数量 | 割合 | 説明 |
|------|------|------|------|
| 確実に行蘊に属する | 7 | 14% | chanda, virya, apramada, mraksa, matsarya, maya, sathya |
| 既に正しく帰属済み | 12 | 24% | OpenStarry で討論を経て確認済みの plugin |
| 他の蘊に属する可能性あり | 18 | 37% | 機能的に識蘊（判断的）または受蘊（感受的）に近い |
| 混合／要研究 | 14 | 28% | 蘊を跨ぐ機能、個別分析が必要 |

ASANGA の結論：「心所リストの機能記述は参考価値があるが、その蘊帰属分類は原典の cetana 中心の定義から逸脱している。」これは唯識学の全面否定ではなく、原典と論典の間に明確な方法論的区分を設けたものである。

---

## 1.7 三基準と核心的区別

LINNAEUS が原典分析から「行蘊属性判定三基準」を帰納し、永久的判定ツールとした [D1-R3, 20/20]：

1. **造作性**（Conditioning）：新たな状態を創造・変更・生成するか？
2. **意図駆動**（Cetana-driven）：意図形成プロセスにより駆動されるか？
3. **環境変化**（Environmental Shift）：後続の認知条件を変更するか？

三問すべてが「はい」→ 行蘊（samskara）。すべてが「いいえ」→ 識蘊（vijnana）。混合 → 個別分析が必要、蘊を跨ぐ可能性あり。

PENROSE はこれをプログラマが即座に理解できる区別にさらに圧縮した：

> **行蘊 = WRITE**（能動的に世界の状態を変更する）
> **識蘊 = READ**（受動的に世界の状態を評価する）

OpenStarry コードベースにおける対応：

| 蘊帰属 | インタフェース | 操作タイプ | コードパス |
|--------|-------------|-----------|-----------|
| 行蘊（WRITE） | `ITool` | ツール実行、環境を変更 | `types/aggregates.ts#ISamskara` |
| 行蘊（WRITE） | `ISlashCommand` | コマンド実行、状態を変更 | `types/aggregates.ts#ISamskara` |
| 識蘊（READ） | `IGuide` | 評価・案内、状態を変更しない | `types/aggregates.ts#IVijnana` |
| 識蘊（READ） | `IVolition` | 審議・判断、状態を変更しない | `types/aggregates.ts#IVijnana` |

この WRITE/READ の区別は D1-R5 で全会一致で承認され（20/20）、蘊帰属判定の操作原則となった。

# 第二章：AuditContext とフィードバックループ防護

---

## 2.1 問題：監査人の情報貧困

v0.29.0-alpha における `IConfidenceAuditor.audit()` のシグネチャは以下の通りである：

```typescript
// v0.29.0-alpha 現状
audit(routeResult: RouteResult): ConfidenceAuditResult | Promise<ConfidenceAuditResult>;
```

ここで `RouteResult` は `{ gear, decidedBy, confidence, riskAdjusted, riskCategory }` のみを含む。有効な監査人にはより多くのコンテキストが必要である：トリガーイベントは何か？arbiter の完全な推論プロセスは？直近の信頼度トレンドは？他の plugin が観測した補助データは？

DC Master は R0 指示において方案 B（ジェネリック Context Bag）を唯一の正しい方向として裁定し、方案 A（固定フィールド拡張）の硬直的設計を却下した。

---

## 2.2 AuditContext 完全型定義 [D2-R1, 20/20]

```typescript
import type { SparshEvent } from './coarising.js';
import type { GearEvaluation, RouteResult, RiskCategory } from './gear-arbiter.js';

/**
 * AuditContext -- rich context for confidence auditing.
 *
 * Replaces bare RouteResult as the input to IConfidenceAuditor.audit().
 * Core fields provide the minimum for meaningful auditing;
 * extras bag allows plugin-contributed data without Core coupling.
 *
 * @version 1 -- initial version (Cycle 02-6)
 */
export interface AuditContext {
  /** Schema version for forward compatibility. Literal type. */
  readonly version: 1;

  /** 本認知ループを起動した SparshEvent */
  readonly sparshEvent: SparshEvent;

  /** 勝出した arbiter の完全な評価結果（confidence + reasoning を含む） */
  readonly gearEvaluation: GearEvaluation;

  /** 現在のリスクレベル（undefined = 未宣言の場合あり） */
  readonly riskCategory: RiskCategory | undefined;

  /** ルーティング結果（監査前のスナップショット） */
  readonly routeResult: RouteResult;

  /**
   * 直近の信頼度履歴系列（opt-in、リングバッファ、デフォルト size=10 設定可能）。
   *
   * WIENER C-1 制約：元の arbiter 信頼度のみを含み、
   * audit 後の修正値は含まない。
   */
  readonly historicalConfidence?: readonly number[];

  /**
   * Plugin が提供する追加コンテキストデータ。
   * ManoAggregator が EventBus から plugin の context contribution を収集し、
   * この Map に統合する。Core は具体的な key/value セマンティクスを関知しない。
   * auditor への引き渡し前に Object.freeze() で凍結される。
   */
  readonly extras: ReadonlyMap<string, unknown>;
}
```

**設計上の選択の要約**：

| 決定点 | 選択肢 | 最終選択 | 理由 |
|--------|-------|---------|------|
| `sparshEvent` を optional にするか | optional vs required | **required** | 各ルーティングには必ずトリガーイベントが存在する。ManoAggregator は `sparshEventFn` コールバック経由で取得 |
| `historicalConfidence` バッファサイズ | 固定 10 vs 設定可能 | **デフォルト 10 設定可能** | `ManoAggregatorConfig.historicalConfidenceSize` |
| `version` の型 | `number` vs リテラル `1` | **リテラル `1`** | コンパイル時型チェックを強制、将来バージョンは `2` に逓増 |
| `extras` の型 | `Record<string, unknown>` vs `ReadonlyMap` | **`ReadonlyMap`** | Map セマンティクスがより明確、freeze がより直感的 |

**IConfidenceAuditor インタフェース更新**：

```typescript
export interface IConfidenceAuditor extends IVijnana {
  readonly id: string;
  audit(context: AuditContext): ConfidenceAuditResult | Promise<ConfidenceAuditResult>;
}
```

これは breaking change（パラメータが `RouteResult` から `AuditContext` に変更）であるが、TURING が D1 のコード検証で v0.29.0-alpha に**いかなる IConfidenceAuditor plugin 実装も存在しない**ことを確認した——これはリファクタリングの最適なタイミングであり、実際の影響はゼロである。

---

## 2.3 WIENER 制約：フィードバックループの体系的遮断

WIENER は Cycle 02-4 D5 において次のことを既に証明していた：過去の audit delta が現在の audit 入力にフィードバックされる場合、正のフィードバックループが発生しうる：

```
Loop N:   auditor 出力 delta = +0.03
Loop N+1: auditor が前回の delta = +0.03 を参照し、正方向に傾斜 → delta = +0.04
Loop N+2: 正方向累積が継続 → システムドリフト
```

形式的表現：$c_n$ を第 $n$ ループの arbiter 元信頼度、$\delta_n$ を audit delta とする。

- **許容される入力**：$\delta_n = f(c_n, c_{n-1}, \ldots, c_{n-k}, \text{extras}_n)$ -- 観測関数
- **禁止される入力**：$\delta_n = g(\delta_{n-1}, \delta_{n-2}, \ldots)$ -- 自己回帰関数

前者の安定性は被観測システム（外生的）に依存し、後者は独立して発散しうる（内生的）。これは制御理論における観測器（observer）と自己回帰システム（autoregressive system）の根本的な区別である。

これに基づき三つのハード制約（WIENER Constraints C-1/C-2/C-3）が設計された：

**C-1**：`historicalConfidence` は元の arbiter 信頼度（`GearEvaluation.confidence`）のみを含み、audit 後の修正値（`auditedConfidence`）は含まない。

```typescript
// ManoAggregator 内部——arbiter 勝出のたびに記録
confidenceHistory.push(evaluation.confidence);  // 元の値
// confidenceHistory.push(auditedConfidence); ではない  // 禁止
```

**C-2**：AuditContext にはいかなる `previousAuditResult`、`previousDelta`、`auditHistory` フィールドも含まない。Auditor は AuditContext から自身の過去の出力を読み取ることができない。

**C-3**：extras bag は三つのプレフィックスを禁止する：`audit:`、`core:`、`internal:`。Auditor が extras を通じて C-2 を迂回することを防ぐ。

```typescript
// extras 書き込み検証
const FORBIDDEN_PREFIXES = ['audit:', 'core:', 'internal:'] as const;

function validateExtrasKey(key: string): boolean {
  return !FORBIDDEN_PREFIXES.some(prefix => key.startsWith(prefix));
}
```

BABBAGE の BIBO 安定性検証：C-1/C-2/C-3 制約の下で、audit delta $\delta_n$ の入力集合は完全に外生変数で構成され（arbiter 元信頼度系列 + plugin extras）、自身の過去の出力を一切含まない。したがって $|\delta_n| \le 0.05$（ハードクランプ）であり、システムは有界入力 → 有界出力（BIBO stability）を満たす。

---

## 2.4 extras bag プロトコル [D2-R2, 19/20]

extras bag の設計は R2 段階で唯一のトラック間相違を生じさせた：A2（DARWIN + MESH）が汎用イベントパターンを提案し、B3（LEIBNIZ + MESH）が直接購読を志向した。D2 討論で**二重イベント + SDK ユーティリティ関数**に統一された：

| 側面 | 決議 |
|------|------|
| 書き込みパターン | Plugin は SDK の `emitWithExtras(key, value)` ユーティリティ関数を使用 |
| 収集パイプライン | ManoAggregator が `audit:context_contribute` イベントを購読 |
| 読み取り | `getExtra<T>(extras, key, guard)` 型安全アクセサ |
| 不変性 | シャローフリーズ（`Object.freeze`）+ `ReadonlyMap` |
| 容量制限 | 最大 32 keys、各 key 128 chars |
| 禁止プレフィックス | `audit:`, `core:`, `internal:` |
| key 命名規約 | `{category}:{name}` -- 例：`loopQuality:vector`, `loopQuality:composite` |
| ライフサイクル | per-routing-cycle（各ルーティング終了時にクリア、永続化しない） |

1 票の反対（MESH）は二重イベントパターンが不要な複雑さを増すとするものであった。しかし多数は汎用パイプラインの投資対効果がより高いと判断した：これは LoopQualityMonitor だけでなく、将来のあらゆる Plugin が同一パイプラインを通じて AuditContext にデータを提供できるからである。

---

## 2.5 ConfidenceAuditLog——GUARDIAN D5 負債の清算 [D2-R3, 20/20]

GUARDIAN は Cycle 02-5 D5 で重要な譲歩を行った：audit delta の制限幅 +-0.05 に同意する代わりに、次ラウンドで完全な監査ログフォーマットを定義するという条件を付した。これはセキュリティ負債であった。

Cycle 02-6 で `ConfidenceAuditLog` 型が設計された：

```typescript
export interface ConfidenceAuditLog {
  readonly timestamp: number;
  readonly auditorId: string;
  readonly inputConfidence: number;    // audit 前の信頼度
  readonly rawDelta: number;           // auditor が提案した delta
  readonly clampedDelta: number;       // クランプ後の delta
  readonly wasClamped: boolean;        // クランプされたか否か
  readonly reasoning: string;          // 500 chars に切り詰め、Core が担当
  readonly outputConfidence: number;   // audit 後の信頼度
  readonly result: 'applied' | 'timeout' | 'error';
  readonly auditDurationMs: number;
}
```

伝搬チャネル：
- **主チャネル**：EventBus `audit:completed` イベント、即時観測可能
- **永続化**：JSONL file appender（オプション、Plan30 以降）
- **PII 浄化**：reasoning フィールドの PII 洗浄は plugin の責任、Core は切り詰めのみ

GUARDIAN は D2 討論中にその場で確認した：「D5 の勘定は清算された。+-0.05 制限幅の再審議権を留保しない。」これは重要なセキュリティマイルストーンである——Cycle 02-4 以来 GUARDIAN は信頼度調整の安全性に継続的に疑義を呈し、毎回の譲歩に条件を付してきた。完全なログ + 三重のフィードバックループ防護 + +-0.05 ハードクランプ——この三重保障がついに彼のセキュリティ要件を満たしたのである。

---

## 2.6 バージョン管理戦略

`AuditContext.version` はリテラル型 `1`（`number` ではない）を使用し、コンパイル時の型チェックを保証する。将来の拡張時には `2` に逓増し、Auditor plugin は認識しないバージョンに対して fail-safe 動作を行うべきである：

```typescript
function audit(ctx: AuditContext): ConfidenceAuditResult {
  if (ctx.version > 1) {
    return { delta: 0, reasoning: 'Unknown AuditContext version' };
  }
  // 通常の監査ロジック...
}
```

この fail-safe パターンは前方互換性を保証する：新バージョンの Core が旧バージョンの Auditor plugin と組み合わされた場合、auditor は認識しない新フィールドによってクラッシュするのではなく、passthrough（delta=0）に退化する。

# 第三章：四次元品質ベクトルと観測器設計

---

## 3.1 設計仕様から SDK 次元へのマッピング

Plan29 の SDK インタフェースは四次元ベクトルのフィールド名を既に定義していたが、計算式は空白のままであった。Doc 43 設計仕様と SDK 実装間のマッピングは以下の通りである：

| Doc 43 設計仕様 | SDK フィールド名 | セマンティクス | 公式記号 |
|----------------|----------------|-------------|---------|
| Continuity（連続性） | `coherence` | ルーティング決定の論理的一貫性 | C |
| Granularity（精細度） | `efficiency` | ツール実行のリソース利用効率 | E |
| Speed（速度） | `convergence` | 目標収束性 | Conv |
| Equanimity（平衡性） | `stability` | 信頼度の振動安定性 | S |

---

## 3.2 共通パラメータ

| 記号 | 定義 | デフォルト値 | 出典 |
|------|------|------------|------|
| W | スライディングウィンドウサイズ | 10 ticks | 設計選択：感度と安定性のバランス |
| W_warmup | ウォームアップ期間 | 5 ticks | 最小統計的有意性 |
| Q_default | ウォームアップ期間の複合スコア | 0.5 | 中性デフォルト（L3 調整をトリガーしない） |

ウォームアップ規則：`tickCount < W_warmup` の場合、全次元は 0.5 を返し、composite = 0.5 となる。ウォームアップ期間のデータはスライディングウィンドウに計上されるが、品質レポートは外部に発出しない。

---

## 3.3 coherence（C）：ルーティング一貫性

**セマンティクス**：認知ループのルーティング決定がどの程度一貫しているかを測定する。ギアの高速振動（1->2->1->2）はシステムの逡巡を示す。

**公式**：

$$C = 1 - \frac{\text{gearSwitchCount}}{W - 1}$$

ここで `gearSwitchCount` = ウィンドウ W 内のギア値変化回数、`W-1` = 最悪ケース（毎 tick 切り替え）。

**入力イベント**：`gear:switch`（`payload.gear`）

**実装**：長さ W のサーキュラーバッファを維持し、直近 W 回のギア値を記録する。新イベント到着のたびに O(1) で更新——新たな隣接差異カウントを追加し、古いものを除去する。

**境界ケース**：

| 状況 | 動作 | 理由 |
|------|------|------|
| `gear:switch` イベントなし | C = 1.0 | 振動なし = 完全な一貫性 |
| ウィンドウデータが W 件未満 | 分母 = max(actualCount - 1, 1) | ゼロ除算回避 |
| W = 1 | C = 1.0 | 単一 tick では振動不可能 |

---

## 3.4 efficiency（E）：ツール実行効率

**セマンティクス**：提案されたツール呼び出しのうち、成功裏に実行された割合。

**公式**：

$$E = \begin{cases} \frac{\text{successfulExec}}{\text{totalProposed}} & \text{if } \text{totalProposed} > 0 \\ 1.0 & \text{otherwise (純粋な対話ループ)} \end{cases}$$

**入力イベント**：

| イベント | 用途 | 備考 |
|---------|------|------|
| `action:proposed` | 分母 | 各ツール呼び出し提案 |
| `tool:result` | 分子 | 成功裏に実行 |
| `tool:error` | 暗黙（Phase 2） | 分子に計上しない |
| `tool:blocked` | 暗黙（Phase 2） | 分子に計上しない |

**設計選択**：純粋な対話ループ（ツール呼び出しなし）は E = 1.0 と定義し、ツールなしシナリオにペナルティを課さない。効率次元が測定するのは「提案された行動が成功したか」であり、行動を提案しないことは効率が低いことを意味しないためである。

---

## 3.5 convergence（Conv）：目標収束性

**セマンティクス**：システムのルーティング決定が同一方向に持続的に推進しているか。同一ギアの連続選択が長いほど、ループの収束度は高い。

**公式**：

$$\text{Conv} = \frac{\text{longestConsistentStreak}}{W}$$

**Phase 2 代替案（ATHENA 提案）**：指数移動平均（EMA）

$$\text{consistency}_t = \begin{cases} 1.0 & \text{if } \text{gear}_t = \text{gear}_{t-1} \\ 0.0 & \text{otherwise} \end{cases}$$

$$\text{EMA}_t = \alpha \cdot \text{consistency}_t + (1 - \alpha) \cdot \text{EMA}_{t-1}, \quad \alpha = \frac{2}{W + 1}$$

Phase 1 では streak 方式（単純、解釈可能）を使用する。Phase 2 で運用データが得られた後、EMA への切り替えを評価する。

**入力イベント**：`gear:switch`。convergence と coherence は同一ソースを使用するが、計算ロジックは異なる点に注意：coherence は切り替え頻度を測定し、convergence は最長連続同方向を測定する。

---

## 3.6 stability（S）：信頼度安定性

**セマンティクス**：arbiter 信頼度の変動度合い。分散の逆数マッピングに基づく。

**公式**：

$$S = 1 - \min\left(1, \frac{\sigma^2}{0.25}\right)$$

ここで $\sigma^2$ はウィンドウ W 内の confidence 値の（母集団）分散、0.25 は保守的上界（二値分布 {0,1} の分散 = 0.25、[0,1] 一様分布の分散 $\approx 0.083$）。

**Welford's Online Algorithm**：

```
State: count, mean, M2

on each new confidence value x:
  count += 1
  delta = x - mean
  mean += delta / count
  delta2 = x - mean
  M2 += delta * delta2

variance = M2 / count  // population variance
```

スライディングウィンドウ版はサーキュラーバッファ + インクリメンタル更新を維持し、依然として O(1) per event。

**入力イベント**：`gear:arbiter_evaluated`（`payload.confidence`）

**境界ケース**：

| 状況 | S 値 | 理由 |
|------|------|------|
| arbiter イベントなし | 1.0 | 変動なし = 完全な安定 |
| 全 confidence が同一 | 1.0 | 分散 = 0 |
| confidence が 0/1 間で交互 | 0.0 | 最大不安定 |

---

## 3.7 Composite Score と重み

**公式** [D3-R4, 20/20]：

$$Q = w_C \cdot C + w_E \cdot E + w_{\text{Conv}} \cdot \text{Conv} + w_S \cdot S$$

Phase 1 の重みはすべて 0.25 に固定（等重み）。PASCAL の最大エントロピー論証：いずれかの次元がより重要であるという経験データが存在しない前提では、最大エントロピー原理（Maximum Entropy Principle）が各可能性に同一の重みを付与することを指示する——これは怠慢ではなく、情報がない場合の最適戦略である。

Phase 2 の重みは設定可能で、monitor plugin config に格納される（`ManoAggregatorConfig` ではない——計算者がそのパラメータを所有する）。三組のプリセット：

| プリセット | coherence | efficiency | convergence | stability |
|-----------|-----------|-----------|-------------|-----------|
| balanced | 0.25 | 0.25 | 0.25 | 0.25 |
| stability-focused | 0.15 | 0.20 | 0.15 | 0.50 |
| efficiency-focused | 0.15 | 0.50 | 0.20 | 0.15 |

検証制約：$\sum w_i = 1.0$、各 $w_i \in [0, 1]$。

**値域保証**：各次元 $d_i \in [0, 1]$、重み $w_i \in [0, 1]$、$\sum w_i = 1.0$ であるから $Q \in [0, 1]$。この有界性は L3 統合の BIBO 安定性にとって極めて重要である。

---

## 3.8 観測器の性質：制御理論の視点

WIENER は四次元公式の**純観測関数**としての性質を特に強調した——これは制御理論における観測器（observer）の定義である：

- **入力**：システムイベントストリーム（制御不能、読み取り専用）
- **状態**：内部スライディングウィンドウ（被観測システムに影響しない）
- **出力**：LoopQualityVector（読み取り専用レポート、書き戻ししない）

Monitor の蘊帰属 = [vedana, samjna, vijnana]、**samskara を排除**。四つの公式はすべて観測計算であり、EventBus 上のイベントを変更せず、いかなる plugin も呼び出さず、いかなる行動もトリガーしない。これにより観測器が被観測システムに干渉しないことが保証される——制御理論における「非侵襲的観測」の原則である。

**Lyapunov 安定性の展望**：stability 次元（S）の分散時系列は Cycle 02-7 の Lyapunov 安定性分析の基礎データを提供する。$\sigma^2$ が継続的に減少すれば、Lyapunov 関数の減少条件の前提に適合する。

---

## 3.9 EventBus イベント購読 [D3-R2, 20/20]

**Phase 1（MINIMAL_QUALITY_EVENTS = 6）**：

1. `gear:arbiter_evaluated` → stability（confidence 値）
2. `gear:switch` → coherence + convergence（gear 値）
3. `action:proposed` → efficiency 分母
4. `tool:result` → efficiency 分子
5. `loop:started` → tick カウント、ウィンドウリセット
6. `loop:finished` → 品質レポート発出のトリガー

**Phase 2（+5 EXTENDED_QUALITY_EVENTS）**：

7. `sparsha:contact` → 入力頻度分析
8. `tool:error` → 効率計算の精緻化
9. `tool:blocked` → セキュリティブロック頻度
10. `vitakka:stall` → 認知停滞検出
11. `action:executed` → 実行遅延分析

**退化原則**（HERACLITUS）：イベント欠損 → 安全なデフォルト値、エラー報告しない。効率欠損 → 1.0（正常と仮定）、安定性欠損 → 0.5（中性）。「欠損は情報であり、エラーではない。」

**Plan30 アクション項目**：Plan27b 中でコード各所に散在するイベント文字列を `AgentEventType` 定数に昇格する必要がある——7 つの新定数（6 つの既存 + `LOOP_QUALITY_UPDATED`）。

---

## 3.10 計算複雑度の要約

| 次元 | イベントごと | レポートごと | 空間 |
|------|-----------|------------|------|
| coherence | O(1) | O(1) | O(W) circular buffer |
| efficiency | O(1) | O(1) | O(1) 二つのカウンタ |
| convergence | O(1) | O(1) | O(W) circular buffer |
| stability | O(1) | O(1) | O(W) circular buffer + Welford state |
| **composite** | -- | O(1) | -- |

**全体**：O(1) per event、O(1) per report、O(W) 空間。W=10 の場合、メモリオーバーヘッドは無視できる。

# 第四章：Option C——独立チャネルのアーキテクチャ決定

---

## 4.1 問題空間：Layer 3 の統合方法

OQ-29-2 の元の問い：

> Layer 3 (Delta_loopQuality) を Model Delta 五層モデルにどう統合するか。加算重畳か、乗算スケーリングか、独立チャネルか。

v0.29.0-alpha の五層モデルの現状：

| Layer | 名称 | 作用対象 | 実装状態 |
|-------|------|---------|---------|
| L0 | Safety Floor/Ceiling | グローバル clamp [0.30, 0.90] | v0.28.0 実装済み |
| L1 | Klesha | baseThreshold += klesha gain | v0.28.0 実装済み |
| L2 | Audit Delta | confidence += clamp(delta, +-0.05) | v0.29.0 実装済み |
| L3 | LoopQuality | **TBD** | 未実装 |
| L4 | VedanaEmergency | threshold += boost [0, +0.15] | v0.28.0 実装済み |

Layer 2 は配線済み（audit delta が confidence に加算される）、Layer 3 は完全に空白である。LoopQualityMonitor の SDK + Registry は整備済みだが、出力（`LoopQualityVector`）はいかなるルーティングロジックにも接続されていない。

---

## 4.2 三方案の比較：なぜ A でも B でもないのか

### Option A：加算重畳

```
theta_final = clamp(theta_base + DeltaL1 + DeltaL2 + DeltaL3 + DeltaL4, 0.30, 0.90)
```

**利点**：既存モデルと完全に一致（すべての delta を加算）、実装一行。

**WIENER の安定性分析**：

$V = (c - \theta)^2$ を Lyapunov 候補関数とする。Option A では $c_{\text{eff}} = c + \Delta_{L2} + \Delta_{L3}$、閾値は不変。

$$\dot{V} = 2(c_{\text{eff}} - \theta)(\dot{\Delta}_{L2} + \dot{\Delta}_{L3})$$

$\Delta_{L2}$ と $\Delta_{L3}$ が同符号かつ増加する場合、$\dot{V} > 0$（Lyapunov 関数の増加 = 不安定傾向）。同方向累積の最悪値は +0.08（0.05 + 0.03）に達し、いかなる単一層の制限幅の設計意図も超過する。

より危険なのは **cross-amplification** である：audit delta は arbiter confidence に基づき、loopQuality もルーティング動作を観測する。両者は同一の異常に対して同方向の反応を示す可能性があり、間接的結合を形成する。

**結論**：Option A は L2/L3 同方向累積時に**安定性を保証できない**。

### Option B：乗算スケーリング

```
theta_adjusted = theta_after_L2 * (1 + loopQualityFactor)
```

展開：$c_{\text{eff}} = (c + \Delta_{L2}) \times (1 + f_{L3}) = c + \Delta_{L2} + c \cdot f_{L3} + \Delta_{L2} \cdot f_{L3}$

交差項 $\Delta_{L2} \cdot f_{L3}$ は直接結合を構成する。各チャネルが個別に有界であっても、交差項が全体のオフセットを増幅しうる。また、乗算はシステムを線形から非線形に変え、Lyapunov 安定性分析の複雑度を大幅に増加させる。境界動作も良好でない：低信頼度（例えば 0.35）では乗算調整幅が過小（0.035）となり、調節の意義を失う。

**結論**：Option B は**無視できない交差項**を導入し、安定性分析が困難である。

### Option C：独立チャネル

```
L2: confidence_adjusted = confidence + clampAuditDelta(audit.delta)  [+-0.05]
L3: theta_adjusted = max(thresholdFloor, theta * (1 - alpha * q))    [alpha=0.10]
```

L2 は**信頼度**を調整し、L3 は**閾値**を調整する。両者は異なる変数に作用し、二つの独立した制御チャネルを構成する。

---

## 4.3 Option C の安定性証明

**制御システムのモデリング**：

| 役割 | 要素 | 説明 |
|------|------|------|
| Plant | Agent 動作 | ギア選択 → 行動品質 |
| Sensor | ILoopQualityMonitor | 行動品質の観測 |
| Controller | L3 閾値調整 | 品質に基づく通過閾値の微調整 |
| Disturbance | IConfidenceAuditor | 信頼度推定の修正 |

**Lyapunov 分析**：

$V = (c_{\text{eff}} - \theta_{\text{eff}})^2$ とする

- チャネル 1：$c_{\text{eff}} = c + \Delta_{L2}$、ここで $\Delta_{L2}$ は arbiter 出力にのみ依存する
- チャネル 2：$\theta_{\text{eff}} = \theta \times (1 - \alpha \cdot q)$、ここで $q$ は EventBus イベントにのみ依存する

$$\dot{V} = 2(c_{\text{eff}} - \theta_{\text{eff}})(\dot{\Delta}_{L2} + \alpha \cdot \theta \cdot \dot{q})$$

$\Delta_{L2}$ は $q$ に依存せず、$q$ は $\Delta_{L2}$ に依存しないため、両者に**交差項は存在しない**。

各チャネルは独立して BIBO を満たす：

- $|\Delta_{L2}| \le 0.05$（ハードクランプ）
- $\alpha \cdot q \in [0, 0.10]$（$\alpha = 0.10$、$q \in [0, 1]$）

**BIBO 安定性定理（非形式的）**：Option C の下で、L2 と L3 がそれぞれ BIBO 安定性を満たし、かつ L2 が L3 の出力に依存せず L3 が L2 の出力に依存しなければ、全体システムは BIBO 安定である。

**証明概要**：L2 と L3 は並列（parallel）制御チャネルを構成する。並列システムの安定性は各チャネルの独立安定性の結合と等価である（parallel interconnection theorem）。各チャネルにはハードクランプがあるため BIBO 安定である。L0 Safety Floor/Ceiling がグローバルなセーフティネットを提供する。

**厳密な Lyapunov 証明は Cycle 02-7 に延期**（P1 Lyapunov パラメータ校正）。

---

## 4.4 セマンティクスの対称性

Option C のセマンティクスの区別は極めて明確である：

| 次元 | L2 (Audit) | L3 (LoopQuality) |
|------|-----------|-------------------|
| 作用対象 | confidence（信頼度） | threshold（閾値） |
| セマンティクスの問い | 「この arbiter の判断は信頼できるか？」 | 「現在のシステム状態は高速パスに適しているか？」 |
| 制御理論のアナロジー | 状態推定器補正（state estimator correction） | 参照入力調整（setpoint adjustment） |
| 方向 | 「測定値」の信頼性を調整 | 「通過閾値」の厳格さを調整 |
| 入力源 | AuditContext（arbiter 結果） | EventBus（monitor 観測） |
| 数値範囲 | +-0.05 | alpha * q in [0, 0.10] |

WIENER の評価：「これは私が見た中で最もクリーンな分離だ。二つのチャネルはそれぞれ明確な物理的意味を持ち、互いに汚染しない。」

---

## 4.5 alpha パラメータの選択

| alpha | theta=0.6 時の最大調整 | 評価 |
|-------|----------------------|------|
| 0.05 | 0.57（0.03 低下） | 極めて保守的 |
| **0.10** | **0.54（0.06 低下）** | **推奨デフォルト** |
| 0.15 | 0.51（0.09 低下） | アグレッシブ |
| 0.20 | 0.48（0.12 低下） | 過度——thresholdFloor を突破する可能性 |

WIENER が alpha = 0.10 を選択した理由：

1. 最大調整が約 +-6% であり、人間が知覚可能な範囲でデバッグに便利
2. L2 の +-0.05 と影響の規模が同程度——L3 が L2 を圧倒しない
3. 保守的な出発点であり、シミュレーションデータに基づいて調整可能

**L3 公式のセマンティクス的解釈**：

| compositeLoopQuality | theta_adjusted（theta=0.6） | 意味 |
|---------------------|---------------------------|------|
| 1.0（最高品質） | 0.54（theta * 0.9） | システム動作が安定 → 閾値をわずかに緩和 → 高速パスがより容易 |
| 0.5（中程度品質） | 0.57（theta * 0.95） | 中程度の調整 |
| 0.0（最低／無観測） | 0.60（theta * 1.0） | 保守的退化——閾値は不変 |

---

## 4.6 品質スコアの二重チャネル伝達

品質監視器が産出するスコアには二つの消費者がおり、それぞれ要求が異なる：

| 消費者 | 必要とするもの | チャネル |
|--------|-------------|---------|
| ManoAggregator（L3 閾値調整） | 即時の composite 数値 | **pull**：`loopQualityFn()` コールバック |
| IConfidenceAuditor（豊富な背景情報） | 四次元ベクトル + composite | **push**：extras bag via EventBus |

**Pull チャネル**：`loopQualityFn` を `createManoAggregator` に注入し、`route()` 内で必要に応じて同期呼び出しする。

```typescript
export function createManoAggregator(
  bus: EventBus,
  config: ManoAggregatorConfig,
  baseThresholdFn?: () => number,
  vedanaFn?: () => ChannelVedana,
  vedanaEmergencyConfig?: VedanaEmergencyConfig,
  auditor?: IConfidenceAuditor,
  loopQualityFn?: () => number,  // 新規追加：compositeLoopQuality in [0, 1] を返す
): ManoAggregator
```

**Push チャネル**：Monitor は SDK の `emitWithExtras()` を使用して同時に発出する：
- `loopQuality:updated` イベント（ManoAggregator が購読、pull コールバックの内部キャッシュ更新に使用）
- `audit:context_contribute` イベント（ManoAggregator が extras bag に収集）

extras 内の key：
- `loopQuality:composite` → composite score（number）
- `loopQuality:vector` → 四次元ベクトルオブジェクト

LEIBNIZ の重要な制約：「品質スコアのライフサイクルは per-routing-cycle である。各ルーティング終了時に extras bag はクリアされる。累積せず、永続化しない。」一 tick の遅延は許容される——品質は履歴指標であり、マイクロ秒レベルの即時性は不要である。

---

## 4.7 境界条件分析

**Monitor Plugin なし（G-0 退化パス）**：`loopQualityFn` が `undefined` または `q_default = 0` を返す場合、L3 は無効：`theta_adjusted = theta`（1.0 を乗ずる）。システム動作は ILoopQualityMonitor が存在しない場合と完全に同一である。

**Monitor レポートの陳腐化**：`monitorStalenessMs = 5000`（設定可能）を設定。期限切れは無観測とみなす → q = 0。WIENER の理由：陳腐化した観測は「ゴースト信号」の導入に等しく、ゼロ次ホールド（ZOH）原則の有効期限概念と一致する。

**複数 Monitor の集約**：Phase 1 では単純平均を使用する（個別 monitor のノイズ影響を低減）。BABBAGE が提案した悲観的戦略（最低値採用）は否決された——単一の異常 monitor が全体に過度の影響を与えるべきではない。

**compositeLoopQuality = 1.0 の極端値**：`theta = thresholdFloor = 0.30` の場合、`theta_adjusted = 0.27 < thresholdFloor`。修正：L3 調整後も L0 に従う必要がある：

```typescript
const adjustedThreshold = Math.max(
  config.thresholdFloor,
  threshold * (1 - loopQualityAlpha * compositeLoopQuality),
);
```

---

## 4.8 完全な五層公式（Option C 統合後）

```
theta_base                                        // 基礎閾値（config 注入）
  + L1: Sigma(w_k * K_k)                         // Klesha ゲイン（baseThresholdFn）
  + L4: thresholdBoost                            // VedanaEmergency 引き上げ
  = theta_intermediate

theta_adjusted = max(thresholdFloor,
                     theta_intermediate * (1 - alpha * q))  // L3: LoopQuality
theta_final = min(thresholdCeiling, theta_adjusted)         // L0 上限

confidence_adjusted = confidence
                    + clampAuditDelta(audit.delta)          // L2: Audit

routing = (confidence_adjusted > theta_final)
        ? arbiter_gear
        : default_gear
```

**Layer 実行順序**：L4（VedanaEmergency）→ L1（Klesha）→ L3（LoopQuality）→ 比較（L2 で調整済み confidence を含む）。L4 が最優先なのは、安全クリティカルな緊急状態を処理するためである。

**L2 と L3 の最悪の相互作用**：confidence が 0.05 増加し、かつ threshold が 0.06 低下 → 純効果は約 0.11。依然として L0 の安全範囲内（`thresholdFloor` + `maxConfidenceByGear` が共同で制約）。

---

## 4.9 ManoAggregator コード統合ポイント

`mano-aggregator.ts` の arbiter ループにおいて、L134-L138 の現行閾値計算の後に L3 調整を挿入する：

```typescript
// 現行：L0 + L1 + risk adjustment
const threshold = evaluation.riskCategory
  ? computeAdjustedThreshold(
      effectiveBaseThreshold, evaluation.riskCategory,
      config.riskDelta, config.thresholdFloor, config.thresholdCeiling)
  : effectiveBaseThreshold;

// 新規追加：Layer 3 -- LoopQuality threshold adjustment
const loopQualityAlpha = config.loopQualityAlpha ?? 0.10;
const q = loopQualityFn ? loopQualityFn() : 0;
const adjustedThreshold = Math.max(
  config.thresholdFloor,
  threshold * (1 - loopQualityAlpha * q),
);

// 修正：adjustedThreshold を使用
if (evaluation.confidence > adjustedThreshold) {
  // ... existing routing logic ...
}
```

新規 `ManoAggregatorConfig` フィールド：

```typescript
export interface ManoAggregatorConfig {
  // ... existing fields ...
  readonly loopQualityAlpha?: number;       // [0, 0.2], default: 0.10
  readonly monitorStalenessMs?: number;     // default: 5000
  readonly historicalConfidenceSize?: number; // default: 10
}
```

WIENER の最終声明：「Option C の安定性保証は二つのチャネルの独立性仮定に基づいている。将来の設計がこの独立性を破壊する場合（例えば auditor に loopQuality を読み取らせてそれに基づいて delta を調整させるなど）、安定性保証は成立しなくなる。extras bag 内で auditor は `loopQuality:composite` を見ることができるが、WIENER C-1/C-2/C-3 が保証するのは、それを見ても正のフィードバックループが形成されないということである——auditor の delta が loopQuality の計算にフィードバックされることはないからだ。」

# 第五章：Master の心所指示と永久的規則

---

## 5.1 トリガー：心所分析の連鎖反応

哲学トラックの C2 報告（唯識学派心所批判）は R2 交差レビュー時に DC Master に提示された。ASANGA は 51 心所の逐条再帰属提案を整理した——うち 18 項（37%）が機能的に行蘊よりも識蘊または受蘊に近いとされた。

Master の回答は単発の裁定ではなく、三ラウンドの漸進的精緻化であった。各ラウンドの焦点はより鋭利になった。

---

## 5.2 第一ラウンド：経典と論典の方法論的画定

Master の核心的主張：**心所（cetasika）は論典（阿毘達磨）の体系化の産物であり、原始仏経（sutta/agama）の内容ではない。**

これは学術的偏見ではない。仏陀は原始経典において五蘊、十二因縁、八正道、三十七道品を説いた。「51 心所」という分類体系は後世の学者（特に無著、世親ら唯識論師）による体系的整理である。原典に多くの心所の名称（例えば慧、精進、慚、愧）が確かに出現するが、**それらを固定数量の分類体系に組織し蘊帰属を指定する**のは論典の仕事である。

Master の直接的結論：**Plugin の命名に心所の梵語名を使用してはならない。**

工学的影響：梵語の心所名で命名されたすべての plugin（例えば VīryaPlugin、PrajnaPlugin）は工学用語に改名しなければならない。

---

## 5.3 第二ラウンド：機能的参照の保持

第一ラウンドは「心所は完全に無用である」と誤読されやすい。Master は第二ラウンドでこの印象を修正した：心所の**機能記述**には参考価値がある。

例えば、心所「精進」（vīrya）は「善法への持続的かつ不断の投入」という機能を記述する。この機能記述を参考にして Plugin を設計することは可能である——ただし Plugin は VīryaPlugin と呼ぶべきではなく、工学的名称（例えば `PersistencePlugin`、`RetryPlugin`）を使用すべきである。

Master の正確な表現：「精進の意味を参考にして、リトライ Plugin を設計した、と言うことはできる。しかし、リトライ Plugin = 精進、とは言えない。」

これは「援引可能、等同不可」の原則である。

---

## 5.4 第三ラウンド：命名の脱結合がもたらす帰属の自由

第三ラウンドは最も深遠であった。Master は言った：「Plugin は心所ではない。」

表面上これは単純である。しかしその含意は構造的である。

唯識学派において、各心所には固定された蘊帰属がある——「精進」は行蘊に属し、「慧」は識蘊に属する。もし Plugin = 心所であれば、Plugin の蘊帰属も固定される。しかし Plugin != 心所である。一つの Plugin は行蘊と識蘊の機能を同時に持ちうる——判断（READ）も行い、行動の実行（WRITE）も行う。

心所体系ではこれは許容されない（各心所は唯一の蘊に帰属する）が、Plugin 体系では完全に合法である。**命名の脱結合は帰属の自由をもたらす**——心所名で Plugin を命名しないことが、かえって Plugin を論典の固定分類の束縛から解放し、複数の蘊を自然に跨ぐことを可能にする。

---

## 5.5 八項目の永久的規則

三ラウンドの指示が八条の永久的規則に整理され、蘊帰属五原則と共に、将来のすべての命名および帰属問題の判定基準を構成する：

| # | 規則 | 工学的影響 |
|---|------|-----------|
| 1 | 心所は論典の産物であり、原始経典の内容ではない | 心所体系をアーキテクチャ設計のデフォルトフレームワークとしない |
| 2 | 心所の機能には参考価値があり、plugin 設計のインスピレーションとなりうる | 設計文書は心所の機能記述を引用可能 |
| 3 | 「ある心所の意味を参考に、ある plugin を設計した」と説明可能 | 設計溯源は合法、等同の宣言は違法 |
| 4 | Plugin は工学用語で命名し、心所の梵語名を使用してはならない | 命名規約のハード規則 |
| 5 | 梵語術語は原始経典由来のものに限定——五蘊(skandha)、触(sparsha) は使用可能 | 経典梵語 vs 論典梵語の区別 |
| 6 | 心所分類は蘊帰属の根拠としない | 「唯識では X は行蘊に属す」は plugin 帰属の証拠とならない |
| 7 | 既存の plugin 帰属決議は影響を受けない | 確認済みの帰属は新規則により覆されない |
| 8 | Plugin != 心所、蘊帰属は自然に複数の蘊を跨ぎうる | 蘊を跨ぐ plugin は合法的であり、想定内である |

---

## 5.6 蘊帰属五原則 [D1-R6, 20/20]

八項目規則と相補的に、五原則は肯定的な判定方法を提供する：

1. **機能分析が蘊帰属の唯一の根拠である**——名称でも、伝統でも、論典でもない
2. **唯識 51 心所体系は機能参照リストとして使用し、帰属根拠としない**
3. **コード命名に梵語術語を使用する場合、原始経典由来のものに限定する**
4. **Plugin は心所ではなく、蘊帰属は自然に複数の蘊を跨ぎうる**
5. **既存の帰属決議（機能分析に基づくもの）は引き続き有効である**

この五条の原則と八項目規則が完全な判定フレームワークを形成する。将来「この機能はどの蘊に属するか」や「この plugin は何と名付けるべきか」と問われるたびに、ゼロから討論する必要はなくなった——この 13 条の規則に直接照合すればよい。

---

## 5.7 D1 議題の連鎖的修訂

Master の三ラウンドの指示は D1 討論議題の修訂を直接的に引き起こした：

- **D1-Q2（心所の複数蘊帰属問題）が削除された**——心所分類が根拠とならない以上、その複数蘊帰属を議論する意義がなくなった
- **D1-Q6（26 項目の心所の逐条投票）が簡略化された**——個別判定ではなく、蘊帰属原則そのものへの投票に変更
- **manasikara 追加議題が取り消された**——`CoarisingBundle` における manasikara は独立インタフェースではなく、追加の議論は不要

これらの修訂により少なくとも 45 分間の討論時間が節約され、同時に決議の抽象度が向上した——個別事例の判定から原則の確立への上昇である。

---

## 5.8 心智論述の工学借鑒評価 [D1-R4a/b/c]

C4 報告（PASCAL + PENROSE）はすべての仏教的心智論述の工学的借鑒価値について体系的評価を行った：

| 論述 | 結論 | 決議 | テスト結果 |
|------|------|------|-----------|
| 五蘊 | 融合完了 | アクション不要 | -- |
| 名色識 | 核心的価値は吸収済み | アクション不要 | -- |
| 十二因縁 | 説明的付録 | 02-7 P2 [D1-R4a, 19/20] | -- |
| 八識 | マルチ Agent シナリオ待ち | Cycle 03+ | -- |
| **四智** | **除外** | **D1-R4b, 18/20** | 四項テストすべて不合格 |
| 認知シーケンス | 最も強い構造的対応 | 02-7 P2 [D1-R4a, 19/20] | -- |

四智（大円鏡智、平等性智、妙観察智、成所作智）の除外は特に重要である。四項の除外テスト：

1. **除去テスト**：四智マッピングを除去した場合、いかなる設計が変わるか？ → いいえ
2. **コード存在テスト**：四智はコードベースに対応物があるか？ → いいえ
3. **駆動力テスト**：四智はいかなる工学的意思決定を駆動したか？ → いいえ
4. **不可替テスト**：より単純な工学概念で代替可能か？ → はい

2 票の反対は参考文書として保持可能とするものであった。しかし四項テストすべてが不合格——保持は認知負荷を増すのみで設計価値を増さない。

---

## 5.9 ISamskara 拡張方向 [D1-R3, 20/20]

Cycle 02-5 D3-R4 決議の確認：現時点で ISamskara サブインタフェースは新規追加しない。四つの方向を長期候補としてアーカイブする：

| 方向 | 説明 | 優先度 | 時期 |
|------|------|--------|------|
| A: cetana-formation | 意図計画——「ツール実行」から「意図形成」への拡張 | P2 | Cycle 03+ |
| B: vasana-imprinting | 習気形成——行動パターンの学習と記憶 | P2 | 長期（VasanaEngine） |
| C: kaya extension | 環境変換——身行の拡張 | P3 | スケジュール不要 |
| D: vaci | コミュニケーション形成——語行の拡張 | P3 | スケジュール不要 |

方向 A と B は原典分析と直接関連する：cetana-formation は SN 22.56 の六思身（意図形成プロセス）に対応し、vasana-imprinting は SN 22.79 の「一切の有為法を造作する」（行動が将来の条件を形成する）に対応する。方向 B の VasanaEngine は D-29-8 において長期ロードマップとして既にスケジュール済みである。

NAGARJUNA の総括：「前ラウンドで我々は何をすべきでないかを学んだ。今ラウンドで我々はなぜすべきでないかを学んだ。」

# 第六章：三場の討論——相違から合意への精密な経路

---

## 6.1 R2 相違点の識別

R2 交差レビューにより 24 の合意点と 3 の相違点が識別された。四組のトラック間交差照合はすべて矛盾なしを確認した——哲学トラックの結論は工学トラックのいかなる設計前提にも影響しない：

| 照合 | 結果 |
|------|------|
| C2 心所批判 → A1 AuditContext | 4/4 影響なし |
| C4 工学借鑒 → D2 Plan30 | 4/4 影響なし |
| C3 ISamskara 拡張 → B1 公式 | 5/5 影響なし |
| C2 心所批判 → 蘊帰属リスト | 11 確認 / 0 修正 / 1 要討論 / 14 将来 |

三項の相違はすべて工学トラック内部に属する：

1. **extras 書き込みプロトコル**：A2 の汎用イベントパターン vs B3 の直接購読 → D2 で解決
2. **extras key 命名**：`loopQuality:score` vs `loopQuality:composite` → D2 で `loopQuality:composite` に統一
3. **loopQualityFn データソース**：L3 コールバック vs extras キャッシュが同一ソースか → D3 で解決（二重チャネル：pull + push）

---

## 6.2 D1：行蘊深掘り（約 75 分間、7 項決議）

| 決議 | 内容 | 票数 | 重要な論点 |
|------|------|------|-----------|
| D1-R1 | 行蘊の核心定義：cetana 中心、造作機能、核心なきプロセス | 20/20 | SN 22.56/79/95 を直接引用、曖昧さなし |
| D1-R3 | ISamskara サブインタフェース新規追加なし；三基準を永久ツールとする | 20/20 | 02-5 D3-R4 を確認、A/B 方向をアーカイブ |
| D1-R4a | 認知シーケンス appendix を 02-7 P2 にスケジュール | 19/20 | 1 票の反対は本ラウンドで完了可能とするもの |
| D1-R4b | 四智の正式除外 | 18/20 | 2 票の反対は参考として保持可能とするもの；四項テストすべて不合格 |
| D1-R4c | C4 総合評価表の確認 | 20/20 | -- |
| D1-R5 | 「活動と変換」原則；行=WRITE 識=READ | 20/20 | PENROSE の WRITE/READ 区別 |
| D1-R6 | 蘊帰属 5 項永久的原則 | 20/20 | 永久的ベースライン、単ラウンドの決議ではない |

D1 は三場の討論の中で合意度が最も高かった——5 項目が全会一致。原因は哲学トラックの結論が原始経典の引用に直接基づいており、工学的トレードオフの判断を伴わないため、相違の余地が極めて小さかったことにある。

D1 の結論は D2/D3 に対して追加議題を必要としなかった——トラック間影響プロトコルにおける「哲学先行、工学後続」規則がこのラウンドでゼロ矛盾と検証された。

---

## 6.3 D2：AuditContext（約 85 分間、5 項決議）

| 決議 | 内容 | 票数 | 重要な論点 |
|------|------|------|-----------|
| D2-R1 | AuditContext 完全型定義（sparshEvent required、history デフォルト 10 設定可能） | 20/20 | A1-OQ1/2/3 すべて解決 |
| D2-R2 | extras bag プロトコル（二重イベント + SDK helper、シャローフリーズ、最大 32 keys） | 19/20 | MESH が二重イベントの複雑さに反対；多数が汎用性を支持 |
| D2-R3 | ConfidenceAuditLog（GUARDIAN D5 義務の履行） | 20/20 | GUARDIAN がその場で清算を確認 |
| D2-R4 | Layer 統合方案 C（L2→confidence、L3→threshold、alpha=0.10） | 20/20 | WIENER/BABBAGE の安定性分析が決定的 |
| D2-R5 | Auditor 戦略三段階：Phase 0 PassthroughAuditor | 20/20 | -- |

D2-R4 の投票過程は注目に値する：WIENER と BABBAGE の安定性分析（Option A/B/C の Lyapunov 比較）は R1 報告で既に提示されていた。R2 交差レビューでは分析に対する疑義は提起されなかった。D2 討論に至り、全会一致で可決——数学的証明の説得力は決定的である。

R2 の三項の相違は D2 ですべて解決された：
- extras 書き込み → 二重イベント + SDK helper に統一（D2-R2）
- key 命名 → `loopQuality:composite` に統一（D2-R2 付帯決議）
- loopQualityFn データソース → D3 に移管して処理

---

## 6.4 D3：LoopQualityMonitor（約 85 分間、5 項決議）

| 決議 | 内容 | 票数 | 重要な論点 |
|------|------|------|-----------|
| D3-R1 | 4 次元公式確認（C/E/Conv/S; W=10, warmup=5, Q_default=0.5） | 20/20 | OQ-29-1 への正式回答 |
| D3-R2 | EventBus 購読：6 events Phase 1; AgentEventType 定数昇格 | 20/20 | OQ-29-4 への正式回答 |
| D3-R3 | extras 書き込み：D2-R2 パイプライン + loopQualityFn 二重チャネル; per-route lifecycle | 20/20 | R2 第三の相違を解決 |
| D3-R4 | 重み Phase 1 固定 balanced 0.25x4 | 20/20 | PASCAL の最大エントロピー論証 |
| D3-R5 | Plan30 = Monitor + L3 + 型定義; Plan31 = Auditor + Audit Trail | 19+1 条件付き | GUARDIAN の条件付き賛成 |

D3-R5 は唯一の条件付き賛成の決議であった。GUARDIAN の条件：**Plan30 の Wave 3 に `ConfidenceAuditLog` の SDK 型定義を必ず含めること、Plan31 に先送りしてはならない。** 理由：ログ型は D5 譲歩条件の核心的納品物であり、延期は負債の先送りに等しい。条件は受け入れられ、GUARDIAN は賛成に転じた。

---

## 6.5 Auditor 戦略三段階 [D2-R5, 20/20]

| Phase | 対応 Plan | 実装 | 説明 |
|-------|----------|------|------|
| Phase 0 | Plan30（W4、オプション） | PassthroughAuditor | delta=0、純粋なログ出力；パイプラインのエンドツーエンド疎通を検証 |
| Phase 1 | Plan31 | ThresholdAuditor | ルールベース：低信頼度検出、loopQuality 異常、トレンド検出 |
| Phase 2 | 長期 | LLM-assisted | LLM 支援による監査 |

Phase 0 の PassthroughAuditor は一見無用に見える——何も調整しない監査人である。しかし ARCHIMEDES の工学的洞察：「その価値は監査にあるのではなく、テストにある。AuditContext の組立、extras の収集、audit delta のクランプ、ConfidenceAuditLog の発出——パイプライン全体のエンドツーエンド疎通を検証するのだ。水道管を設置した後にまず蛇口を開けるようなものだ。」

すべての Phase は WIENER C-1/C-2/C-3 制約に従わなければならない——これは Phase 0 の特別な要件ではなく、永久的な制約である。

---

## 6.6 統計比較

| 指標 | Cycle 02-5 | Cycle 02-6 |
|------|-----------|-----------|
| 決議数 | 29 | 17 |
| 否決 | 0 | 0 |
| 全会一致（20/20） | ~20（69%） | 13（76%） |
| Master 覆審 | 2 | 0 |
| 討論回数 | 5 | 3 |
| R1 報告数 | -- | 14 |
| R2 合意点 | -- | 24 |
| R2 相違点 | -- | 3 |

DARWIN の観察：「02-5 は正当性の討論——何が正しく、何が間違っているか。02-6 は仕様の討論——正しいものがどのような形をしているか。後者は本質的に合意に達しやすい。価値判断を伴わないからだ。」

SUNYATA の分析：「R1 が良くできた。14 件の報告がすべての問題空間をカバーした。R2 で発見された相違は僅か 3 件。大部分の問題が討論前に既に合意を得ていれば、討論は確認と精緻化の場となる。」

Master 覆審がゼロの理由：八項目規則が R2 段階で既に確立されていた（Master の三ラウンドの精緻化）。D1-D3 のすべての決議は八項目規則のフレームワーク内で運用された。フレームワーク自体に挑戦を試みた決議は一つもなかった。

# 第七章：Plan30 工学ブループリントと展望

---

## 7.1 Plan30 の定義

**Plan30 = Default LoopQualityMonitor Plugin + Layer 3 Integration**

意思決定の基盤：D3-R5（19/20 + 1 条件付き賛成）。前提条件：Plan29 DONE + OQ-29-1/2/4/5 回答済み。

---

## 7.2 四つの Wave

### Wave 1：Default Monitor Plugin（約 120 LOC）

コア品質計算エンジン、B1 四次元公式 + B2 六イベント購読モデルを使用。

```typescript
// 概念的インタフェース（最終実装ではない）
export class DefaultLoopQualityMonitor implements ILoopQualityMonitor {
  private readonly window: SlidingWindow;      // W=10
  private readonly warmupThreshold = 5;
  private tickCount = 0;

  // circular buffers
  private gearHistory: number[] = [];          // coherence + convergence
  private proposedCount = 0;                   // efficiency 分母
  private successCount = 0;                    // efficiency 分子
  private welfordState: WelfordState;          // stability

  constructor(private readonly bus: EventBus) {
    // Phase 1: 6 イベントを購読
    bus.on('gear:arbiter_evaluated', this.onArbiterEvaluated);
    bus.on('gear:switch', this.onGearSwitch);
    bus.on('action:proposed', this.onActionProposed);
    bus.on('tool:result', this.onToolResult);
    bus.on('loop:started', this.onLoopStarted);
    bus.on('loop:finished', this.onLoopFinished);
  }

  report(): LoopQualityReport {
    if (this.tickCount < this.warmupThreshold) {
      return { vector: WARMUP_VECTOR, composite: 0.5, timestamp: Date.now() };
    }
    const vector = {
      coherence:   this.computeCoherence(),
      efficiency:  this.computeEfficiency(),
      convergence: this.computeConvergence(),
      stability:   this.computeStability(),
    };
    const composite = 0.25 * (vector.coherence + vector.efficiency
                             + vector.convergence + vector.stability);
    return { vector, composite: Math.max(0, Math.min(1, composite)), timestamp: Date.now() };
  }
}
```

すべての次元が O(1) per event、O(W) 空間。

### Wave 2：Layer 3 ManoAggregator Integration（約 80 LOC）

Option C の配線。`mano-aggregator.ts` におけるコア修正：

1. `createManoAggregator` に `loopQualityFn?: () => number` パラメータを新規追加
2. `ManoAggregatorConfig` に `loopQualityAlpha`、`monitorStalenessMs`、`historicalConfidenceSize` を新規追加
3. arbiter ループに L3 閾値調整を挿入
4. 信頼度履歴リングバッファ（C-1 制約：元の値のみを記録）

```typescript
// L3 閾値調整のコアロジック
const alpha = config.loopQualityAlpha ?? 0.10;
const q = loopQualityFn ? loopQualityFn() : 0;
const adjustedThreshold = Math.max(
  config.thresholdFloor,
  threshold * (1 - alpha * q),
);
```

### Wave 3：Events + Extras + Types（約 60 LOC）

- `AgentEventType` 定数昇格：7 つの新定数（6 つの Plan27b 既存 + `LOOP_QUALITY_UPDATED`）
- `ConfidenceAuditLog` SDK 型定義（GUARDIAN D3-R5 条件）
- `audit:context_contribute` イベント定義
- `MINIMAL_QUALITY_EVENTS` 定数（Phase 1 = 6 events）
- `emitWithExtras()` SDK ユーティリティ関数

### Wave 4（オプション）：PassthroughAuditor（約 30 LOC）

```typescript
export class PassthroughAuditor implements IConfidenceAuditor {
  readonly id = 'passthrough-auditor';

  async audit(context: AuditContext): Promise<ConfidenceAuditResult> {
    // Phase 0: delta=0, pure logging
    return {
      delta: 0,
      reasoning: `Passthrough: confidence=${context.routeResult.confidence}, ` +
                 `gear=${context.routeResult.gear}`,
    };
  }
}
```

用途：エンドツーエンドのパイプライン検証 + 統合テストフィクスチャ + Phase 1 ThresholdAuditor のスキャフォールド。

---

## 7.3 スコープ要約

| 指標 | 見積り |
|------|-------|
| プロダクションコード | 約 260-290 LOC |
| テストコード | 約 130 LOC |
| 合計 | 約 390-420 LOC |

---

## 7.4 成功基準

**Model Delta L0-L4 すべてに実際の信号パスが存在すること**——L0（EventBus イベントストリーム）から L4（audit 出力）まで各層が空殻でなく、実際のコードが動作していなければならず、統合テストで検証する。

具体的には：
- L0：EventBus イベントが Monitor に購読・処理される
- L1：Klesha ゲインが baseThreshold に影響する（既存）
- L2：Audit delta が confidence を調整する（Plan29 で配線済み；Plan30 W4 が PassthroughAuditor を提供）
- L3：LoopQuality が threshold を調整する（Plan30 W2 で新規追加）
- L4：VedanaEmergency boost（既存）

---

## 7.5 WIENER 制約の工学的実施

すべての Wave は三つのハード制約に従わなければならない：

| 制約 | 実施箇所 | 検証方法 |
|------|---------|---------|
| C-1：historicalConfidence は元の値のみを含む | W2: リングバッファ push | ユニットテスト：audit 後の値が history に現れないこと |
| C-2：AuditContext は前回の audit 結果を含まない | W3: AuditContext 型定義 | 型チェック：インタフェースに previousAuditResult フィールドがないこと |
| C-3：extras は `audit:` プレフィックスを禁止する | W3: emitWithExtras 検証 | ユニットテスト：禁止プレフィックスを含む書き込みが拒否されること |

---

## 7.6 Plan31 プレビュー

Plan31 は AuditContext を実行パスに落とし込む——型定義から実際の組立へ：

| 項目 | 見積り LOC | 説明 |
|------|-----------|------|
| AuditContext 組立 | ~120 | Core が route() 内で完全な AuditContext を組み立てる |
| Default ThresholdAuditor | ~120 | Phase 1 ルールベース監査：低信頼度検出、loopQuality 異常、トレンド検出 |
| Audit Trail JSONL | ~110 | 永続化層：ConfidenceAuditLog → JSONL file appender |
| **合計** | **~350** | |

Plan30 はパイプラインを構築する（型 + 計算 + 配線）。Plan31 はパイプラインに水を流す（組立 + 監査 + 永続化）。

---

## 7.7 Plan32+ 長期ロードマップ

```
Plan30 (本ラウンド)    → Default LoopQualityMonitor + Layer 3 Integration
Plan31 (次ラウンド)    → AuditContext 落とし込み + Default Auditor + Audit Trail
Plan32 (将来)         → VasanaEngine / SPC / Lyapunov stability
```

Cycle 02-7 の P1 要研究項目：

1. **Lyapunov 安定性パラメータ校正**：alpha 値の検証、定常状態分析、五層モデルの厳密な安定性証明
2. **Moha/Sneha 結合シミュレーション**：Klesha モジュール（L1）間の相互作用が L3 動作に影響するか
3. **複数 monitor 集約戦略の検証**：単純平均 vs 悲観的戦略の経験データ比較

Cycle 03+ の延期項目：

- **八識深化**（alaya-vijnana）：マルチ Agent シナリオにおける共有記憶メカニズム
- **VasanaEngine**（D-29-8）：行動パターンの学習と記憶、行蘊の「一切の有為法を造作する」に対応
- **ISamskara 方向 A/B**：意図計画（cetana-formation）+ 習気形成（vasana-imprinting）

---

## 7.8 研究成果の総括

### 九項目の成功基準の達成

| # | 基準 | 状態 | 決議 |
|---|------|------|------|
| 1 | AuditContext 完全型定義 | 達成 | D2-R1 |
| 2 | 監査ログフォーマット仕様（GUARDIAN D5） | 達成 | D2-R3 |
| 3 | LoopQualityVector 4D 公式 | 達成 | D3-R1 |
| 4 | EventBus イベント購読リスト | 達成 | D3-R2 |
| 5 | OQ-29 全回答 | 達成 | 5/5 |
| 6 | Plan30 方向提案 | 達成 | D3-R5 |
| 7 | 行蘊深掘り報告 | 達成 | C1-C4 + D1 |
| 8 | 心所逐条蘊帰属提案 | 達成 | C2（51 項目） |
| 9 | スコープクリープなし | 達成 | Lyapunov/Moha/FC-26 は未議論 |

### 二大永久的成果

1. **蘊帰属五原則 + 行蘊三基準**：将来のすべての蘊帰属判定のベースライン
2. **心所八項目規則**：将来のすべての命名および仏教概念引用の判定ベースライン

この二組の規則は単ラウンドの決議ではない——すべての将来の Cycle を跨ぐ永久的フレームワークである。

### 工学と哲学の合流

Cycle 02-5 は減法であった（装飾的マッピングの除去）。Cycle 02-6 は加法である（精密な仕様の構築）。

哲学トラックは行蘊の原典定義を確立し（cetana 中心、造作機能、核心なきプロセス）、工学トラックはこれに基づいて完全なインタフェース仕様を産出した（AuditContext、LoopQualityVector、Option C 二重チャネル、五層公式）。両トラックは蘊帰属五原則と WRITE/READ 区別において合流した——哲学的判定が工学設計のセマンティクス基盤を提供し、工学設計が哲学的判定の操作可能性を検証した。

Plan30 は約 290 行のプロダクションコードである。多くはない。しかしこの 290 行の一行一行が、17 項目の決議、14 件の研究報告、三ラウンドの Master 指示を根拠としている。

二十名の研究者。十七項目の決議。否決ゼロ。

---

*Cycle 02-6 完。*
