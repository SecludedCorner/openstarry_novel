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
