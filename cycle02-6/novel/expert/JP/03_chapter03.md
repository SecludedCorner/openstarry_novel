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
