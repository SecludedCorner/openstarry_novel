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
