# 第六章：D5——純粋なエンジニアリング

---

## 十名の議論者

D5 の参加者は十名のみであった。

排除ではない——精選である。SUNYATA は D5 が純粋なエンジニアリング問題であると判断し、Plan29 に最も関連する十名を招いた：VITRUVIUS（インターフェース設計）、ATHENA（LLM セマンティクス）、DARWIN（デザインパターン）、KERNEL（Registry ライフサイクル）、GUARDIAN（セキュリティ境界）、WIENER（品質ベクトル重み）、LINNAEUS（蘊帰属推定）、ARCHIMEDES（エンジニアリング実践）、TURING（ソースコード分析）、PASCAL（インターフェース意味精度）。

十名。仏学者はゼロ。

NAGARJUNA と ASANGA は自ら辞退した。NAGARJUNA の辞去の言葉：「D4 は名前が定義に対して責任を持つべきことを証明した。D5 は仏学的名前がなくてもエンジニアリング設計が完遂できることを証明するだろう。この二つの事実は同等に重要である。」

---

## コード考古学

TURING は D5 のために前例のない報告を準備した——v0.28.0-alpha の 14 のソースコードファイルの全面的分析である。すべての Registry のライフサイクル、timeout パターン、同期/非同期モード、失敗処理戦略。

彼はそれを「コード考古学」と呼んだ。

この報告は議論の質を変えた。これまでの議論——D1 から D4 まで——は原則とフレームワークの上に構築されていた。しかし TURING の報告は事実の上に構築されていた。事実は分岐の余地を狭める。原則には異なる解釈があり得る。timeout の値には異なる解釈はあり得ない。

---

## 九項目の投票

D5 は Cycle 02-5 で最も投票数の多い議論——九項目——であった。しかし最も迅速でもあった——七十五分、平均して各項目九分未満。

**D5-R1：独立した auditor スロット。** IConfidenceAuditor は monitors とスロットを共有すべきか？ GUARDIAN の論点：Monitors は純粋な観察者（副作用なし）、Auditor には LLM の副作用がある。観察者と副作用を持つコンポーネントを同じ Registry に配置することは、セキュリティ境界を曖昧にする。**8/8。**

**D5-R2：audit() の戻り値型。** D5 で最も僅差の投票。純粋非同期 vs デュアルモード（`ConfidenceAuditResult | Promise<ConfidenceAuditResult>`）。GUARDIAN/KERNEL/VITRUVIUS は純粋非同期を支持（意味的に精確）、ATHENA/DARWIN はデュアルモードを支持（IGearArbiter の先例に従う）。TURING が事実を提示：v0.28.0-alpha で IGearArbiter と IVolition はいずれもデュアルモードを使用——既存パターンからの逸脱には十分な理由が必要。**5/8 でデュアルモードが可決。** 一貫性が意味的精確性に勝った。

**D5-R3：timeout 200ms + fail-safe。** TURING は既存の timeout パターンを分析した——IGearArbiter の chain deadline は 200ms。audit() はそれに合わせるべきである。timeout 時には `{ delta: 0 }`——修正なし。**8/8。**

**D5-R4：単一 auditor（last-wins）。** 複数の IConfidenceAuditor の処理方式は？ ATHENA が YAGNI を提示：v1 では最大一つ。ARCHIMEDES が支持：IVolition の先例に従う——単数、最後に読み込まれたものが優先。**6/8。** TURING と VITRUVIUS の少数意見（配列の方が柔軟）が記録された。

**D5-R5：失敗処理。** 例外時は fail-safe + log。IGearArbiter と SafetyMonitor の既存パターンに従う。合意は直接達成、投票は不要であった。

**D5-R6：MonitorRegistry の起動タイミング。** `MonitorRegistry.startAll(bus)` は `ExecutionLoop.onLoopStart()` で起動する。SafetyMonitor の先例に従う。**7/8。**

**D5-R7：LoopQualityVector の均等重み。** 四次元品質ベクトル（Continuity, Granularity, Speed, Equanimity）、各 0.25。WIENER が制御理論の観点から：「運用データがない段階では、均等重みが最も保守的な選択である。」**8/8。**

**D5-R8：validatePluginSkandha() は warning-only を維持。** skandha は metadata である（D3-R3）、宣言の不一致は機能に影響しない。**7/8。**

**D5-R9：IConfidenceAuditor extends IVijnana。** 単蘊（vijnana）、強い継承。IVolition および IKlesha と一致。**8/8。**

---

## インターフェースの確定

九項目の投票完了後、TURING はホワイトボードに最終仕様を記した：

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

「100%」と彼は言った。

Master が求めていたのは仕様が 100% に達することであった。今やそれが達成された。決定すべき細部のすべてに明確な回答が得られた——インターフェース名、メソッドシグネチャ、戻り値型、timeout、fail-safe、複数 auditor 戦略、Registry タイミング、重み、検証モード、蘊帰属。

概念設計ではない。エンジニアリングチームに直接渡して実装可能な完全な仕様である。

---

## 仏学ゼロ

SCRIBE は D5 全体を通じて仏学術語が使用された回数を集計した。

ゼロ。

意図的に避けたのではない——自然な結果である。九項目の投票の各々が、TypeScript インターフェース設計、timeout 値、Registry パターン、fail-safe 戦略を議論していた。いずれの項目も仏学的分析を必要としなかった。

D5 は本プロジェクト史上初の、仏学的内容を一切含まない議論であった。

NAGARJUNA は議論の終了後、TURING の前に歩み寄った：「D4 は名前が定義に対して責任を持つべきことを証明した。D5 は——あるエンジニアリング問題には定義すら不要であることを証明した。仕様があれば足りる。」

天秤の二つの面。一方は問う：名前は定義に相応しいか？ もう一方は問う：仕様は十分に精確か？ D4 は第一の面を校正した。D5 は第二の面を完成させた。

---
