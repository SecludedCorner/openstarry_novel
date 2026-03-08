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
