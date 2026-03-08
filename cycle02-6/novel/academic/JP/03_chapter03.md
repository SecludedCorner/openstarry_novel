# 第三章：四次元品質ベクトル —— 認知ループの定量的評価枠組み

---

## 3.1 問題の定義

OpenStarry の AI Agent は認知ループにおいて動作する：sparsha → vedana → samjna → samskara → manas/vijnana → 次のサイクルの入力。`ILoopQualityMonitor` はこのループの動作品質をリアルタイムで定量的に評価する必要がある。品質は多次元の概念であり、単一指標では不十分である。WIENER（#12）と ATHENA（#5）が四次元品質ベクトル（LoopQualityVector）を設計し、D3-R1（20/20）で確認された。

---

## 3.2 四次元公式

滑動窓サイズ $W = 10$、ウォームアップ期間 $W_{warmup} = 5$ とする。

### 3.2.1 一貫性（Coherence）

$$\text{coherence} = 1 - \frac{\text{switchCount}}{W - 1}$$

ルーティング決定の安定性を測定する。高い値は Agent が同一の処理モードで継続的に動作していることを示し、低い値は頻繁な切り替えを示す。入力イベント：`gear:switch`。

### 3.2.2 効率性（Efficiency）

$$\text{efficiency} = \frac{\text{success}}{\text{proposed}} \quad (\text{proposed} = 0 \text{ の場合} = 1.0)$$

ツール呼び出しの成功率を測定する。退化処理：proposed イベントがない場合はデフォルト 1.0。入力イベント：`action:proposed`, `tool:result`。

### 3.2.3 収束性（Convergence）

$$\text{convergence} = \frac{\text{longestStreak}}{W}$$

Agent が安定状態に収束しつつあるか否かを測定する。効率性との違い：効率性は「総量」を測定し、収束性は「傾向」を測定する —— 8 回の成功が直近 8 回に集中する場合（収束性 0.8）と窓全体に分散する場合（おそらく 0.3 にすぎない）とでは意味が異なる。入力イベント：`gear:switch`。

### 3.2.4 安定性（Stability）

$$\text{stability} = 1 - \min\left(1, \frac{\sigma^2}{0.25}\right)$$

仲裁器の信頼度出力の分散を測定する。分母 0.25 は緩やかな正規化基準である。入力イベント：`gear:arbiter_evaluated`。

---

## 3.3 複合品質スコアと重み

$$Q = \sum_{i=1}^{4} w_i \cdot d_i, \quad Q \in [0, 1]$$

Phase 1 では等重み $w_i = 0.25$ とする。理論的根拠は PASCAL（#19）の最大エントロピー論証にある。事前知識が欠如する状況において、最大エントロピー原理（Jaynes 1957）は重みの均等配分を要請する。D3-R4（20/20）は Phase 1 の固定等重み、Phase 2 の設定可能性（balanced / stability-focused / efficiency-focused の三組のプリセット）を確認した。

---

## 3.4 滑動窓と計算量

| パラメータ | 値 | 理由 |
|-----------|-----|------|
| $W$ | 10 | 感度とロバスト性の間のバランス |
| $W_{warmup}$ | 5 | ウォームアップ期間による小標本バイアスの回避 |
| $Q_{default}$ | 0.5 | ウォームアップ期間中の中立的デフォルト値 |

すべての計算は $O(1)$ per event、$O(W)$ 空間であり、品質監視がパフォーマンスのボトルネックとならないことを保証する。

---

## 3.5 EventBus イベント購読 [D3-R2, 20/20]

**Phase 1（6 イベント）**：`gear:arbiter_evaluated`（安定性）、`gear:switch`（一貫性＋収束性）、`action:proposed`（効率性）、`tool:result`（効率性）、`loop:started`（窓管理）、`loop:finished`（窓管理）。

**Phase 2（+5 イベント）**：`sparsha:contact`, `tool:error`, `tool:blocked`, `vitakka:stall`, `action:executed`。

**退化原則**（HERACLITUS #15）：「欠如は情報であり、エラーではない。」欠如イベントは安全なデフォルト値（効率性 1.0、安定性 0.5）を使用し、例外を投げない。同時に、コード中に散在するイベント文字列リテラルを統一的に `AgentEventType` 定数へ昇格させる。

---
