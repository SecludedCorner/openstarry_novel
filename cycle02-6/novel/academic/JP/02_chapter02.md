# 第二章：監査コンテキストの型設計 —— 情報充足性とフィードバックループの遮断

---

## 2.1 問題分析：IConfidenceAuditor の情報貧困

Plan29 で交付された `IConfidenceAuditor` インタフェースには構造的欠陥が存在する。監査関数の入力は `RouteResult`（ルーティング結果）のみを含む。監査者はトリガイベント（sparshEvent）、仲裁器の推論過程（gearEvaluation）、リスクレベル（riskCategory）、または過去の信頼度系列を取得できない。意思決定理論の用語で言えば、これは情報の非対称性（information asymmetry）問題である。DC Master は監査者がより多くの情報を必要とすることを明確に指示した。

しかしながら、監査者に可視的な情報を拡充すると同時に、制御理論上のリスクが導入される。**正フィードバックループ**（positive feedback loop）である。

---

## 2.2 正フィードバックループの脅威モデル

WIENER（#12）は三つの潜在的正フィードバック経路を識別した：

1. **historicalConfidence 汚染**：過去の系列が監査後の調整値を含む場合、`audit → confidence → history → audit` の閉じたループが形成される
2. **監査結果の漏洩**：AuditContext が前回の監査結果を含む場合、確証バイアスに駆動される系列相関が形成される
3. **extras バックドア**：extras bag が監査関連のキー・バリューペアの書き込みを許容する場合、過去の出力が間接的に漏洩する

三つの経路はいずれも BIBO 不安定性を引き起こしうる。信頼度値が反復の中で単調増加または振動発散するのである。

---

## 2.3 AuditContext 型定義 [D2-R1, 20/20]

```typescript
export interface AuditContext {
  readonly version: 1;                              // リテラル型
  readonly sparshEvent: SparshEvent;                // トリガイベント（必須）
  readonly gearEvaluation: GearEvaluation;          // 仲裁器の完全な推論過程
  readonly riskCategory: RiskCategory | undefined;  // リスクカテゴリ（オプション）
  readonly routeResult: RouteResult;                // 監査前ルーティング結果スナップショット
  readonly historicalConfidence?: readonly number[]; // 環形バッファ、デフォルト 10
  readonly extras: ReadonlyMap<string, unknown>;     // 汎用拡張バッグ
}
```

中核フィールドは Core が組み立てる。historicalConfidence はオプションの環形バッファであり、extras は ReadonlyMap で、`getExtra<T>(extras, key, guard)` 型安全アクセサを通じて読み取る。

---

## 2.4 WIENER の三制約

**C-1（過去値の純粋性）**：historicalConfidence は仲裁器の原始信頼度 $c_t^{raw}$ のみを記録し、監査後の調整値を含まない。

**C-2（監査結果の隔離）**：AuditContext は前回の ConfidenceAuditLog を含まない。各回の監査情報は独立である。

**C-3（extras 接頭辞禁止）**：`audit:`、`core:`、`internal:` 接頭辞を禁止し、監査結果が extras を通じて漏洩することを防止する。

三制約は監査者の**因果的隔離**（causal isolation）を保証する。BABBAGE（#9）の形式的検証：監査関数 $f: \mathcal{C} \times \mathcal{A} \to [-0.05, +0.05]$ は三制約の下で、入力が自身の先行出力を含まず、調整量はリミッタ制約を受け、信頼度の値域 $[0,1]$ は自然に有界であり、システムは BIBO 安定性を満たす。

---

## 2.5 extras bag プロトコル [D2-R2, 19/20]

| 側面 | 仕様 |
|------|------|
| 書き込みモード | 二重イベント + SDK `emitWithExtras()` |
| 収集パイプライン | ManoAggregator が `audit:context_contribute` を購読 |
| 読み取りインタフェース | `getExtra<T>(extras, key, guard)` |
| 不変性 | 浅い凍結 + ReadonlyMap |
| 制限 | 最大 32 キー、128 文字/キー |
| キー命名 | `{category}:{name}` 形式 |

一票の反対は二重イベントモードが不必要な複雑性を増すと主張したが、多数はその汎用性（任意の Plugin が同一プロトコルを通じて情報を提供できること）が設計を正当化すると判断した。

---

## 2.6 ConfidenceAuditLog [D2-R3, 20/20]

完全な監査証跡の型：inputConfidence, rawDelta, clampedDelta, wasClamped, reasoning（500 文字で切り捨て）, outputConfidence, result, auditDurationMs。主要チャネルは EventBus の `audit:completed` イベントであり、JSONL 永続化は Plan31 に予定される。

GUARDIAN（#11）はこの決議の可決後、正式に声明した：「D5 の譲歩条件は履行された。私は $\pm 0.05$ リミッタの再審議権をもはや留保しない。」この声明は、Cycle 02-4 以来の信頼度調整の安全性をめぐる継続的論争を終結させた。

---
