# 第四章：Option C——獨立通道的架構決策

---

## 4.1 問題空間：Layer 3 如何整合

OQ-29-2 的原始問題：

> Layer 3 (Delta_loopQuality) 如何整合進 Model Delta 五層模型？是加法疊加、乘法縮放、還是獨立通道？

v0.29.0-alpha 的五層模型現狀：

| Layer | 名稱 | 作用對象 | 實作狀態 |
|-------|------|---------|---------|
| L0 | Safety Floor/Ceiling | 全域 clamp [0.30, 0.90] | v0.28.0 已實作 |
| L1 | Klesha | baseThreshold += klesha gain | v0.28.0 已實作 |
| L2 | Audit Delta | confidence += clamp(delta, +-0.05) | v0.29.0 已實作 |
| L3 | LoopQuality | **TBD** | 未實作 |
| L4 | VedanaEmergency | threshold += boost [0, +0.15] | v0.28.0 已實作 |

Layer 2 已佈線（audit delta 加到 confidence），Layer 3 完全空白。LoopQualityMonitor 的 SDK + Registry 已就位，但輸出（`LoopQualityVector`）未連接到任何路由邏輯。

---

## 4.2 三方案比較：為什麼不是 A 或 B

### Option A：加法疊加

```
theta_final = clamp(theta_base + DeltaL1 + DeltaL2 + DeltaL3 + DeltaL4, 0.30, 0.90)
```

**優點**：與現有模型完全一致（所有 delta 相加），實作一行。

**WIENER 的穩定性分析**：

令 $V = (c - \theta)^2$ 為 Lyapunov 候選函數。Option A 下 $c_{\text{eff}} = c + \Delta_{L2} + \Delta_{L3}$，閾值不變。

$$\dot{V} = 2(c_{\text{eff}} - \theta)(\dot{\Delta}_{L2} + \dot{\Delta}_{L3})$$

若 $\Delta_{L2}$ 和 $\Delta_{L3}$ 同號且遞增，$\dot{V} > 0$（Lyapunov 函數遞增 = 不穩定趨勢）。同向累積最壞可達 +0.08（0.05 + 0.03），超過任何單層限幅的設計意圖。

更危險的是 **cross-amplification**：audit delta 基於 arbiter confidence，loopQuality 也觀察路由行為。兩者可能對同一異常做出同向反應，形成間接耦合。

**結論**：Option A 在 L2/L3 同向累積時**無法保證穩定**。

### Option B：乘法縮放

```
theta_adjusted = theta_after_L2 * (1 + loopQualityFactor)
```

展開：$c_{\text{eff}} = (c + \Delta_{L2}) \times (1 + f_{L3}) = c + \Delta_{L2} + c \cdot f_{L3} + \Delta_{L2} \cdot f_{L3}$

交叉項 $\Delta_{L2} \cdot f_{L3}$ 構成直接耦合。即使各通道單獨有界，交叉項可放大整體偏移。另外，乘法使系統從線性變為非線性，Lyapunov 穩定性分析複雜度大幅增加。邊界行為也不佳：低信心度（如 0.35）時乘法調整幅度過小（0.035），失去調節意義。

**結論**：Option B 引入**不可忽略的交叉項**，穩定性分析困難。

### Option C：獨立通道

```
L2: confidence_adjusted = confidence + clampAuditDelta(audit.delta)  [+-0.05]
L3: theta_adjusted = max(thresholdFloor, theta * (1 - alpha * q))    [alpha=0.10]
```

L2 調整**信心度**，L3 調整**閾值**。兩者作用於不同變量，構成兩個獨立控制通道。

---

## 4.3 Option C 的穩定性證明

**控制系統建模**：

| 角色 | 元素 | 描述 |
|------|------|------|
| Plant | Agent 行為 | 齒輪選擇 → 行動品質 |
| Sensor | ILoopQualityMonitor | 觀測行為品質 |
| Controller | L3 閾值調整 | 根據品質微調通過門檻 |
| Disturbance | IConfidenceAuditor | 修正信心度估計 |

**Lyapunov 分析**：

令 $V = (c_{\text{eff}} - \theta_{\text{eff}})^2$

- 通道 1：$c_{\text{eff}} = c + \Delta_{L2}$，其中 $\Delta_{L2}$ 只依賴 arbiter 輸出
- 通道 2：$\theta_{\text{eff}} = \theta \times (1 - \alpha \cdot q)$，其中 $q$ 只依賴 EventBus 事件

$$\dot{V} = 2(c_{\text{eff}} - \theta_{\text{eff}})(\dot{\Delta}_{L2} + \alpha \cdot \theta \cdot \dot{q})$$

因為 $\Delta_{L2}$ 不依賴 $q$，$q$ 不依賴 $\Delta_{L2}$，兩者**無交叉項**。

每個通道獨立滿足 BIBO：

- $|\Delta_{L2}| \le 0.05$（硬限幅）
- $\alpha \cdot q \in [0, 0.10]$（$\alpha = 0.10$，$q \in [0, 1]$）

**BIBO 穩定性定理（非正式）**：在 Option C 下，若 L2 和 L3 各自滿足 BIBO 穩定性，且 L2 不依賴 L3 輸出、L3 不依賴 L2 輸出，則整體系統 BIBO 穩定。

**證明草稿**：L2 和 L3 構成並聯（parallel）控制通道。並聯系統的穩定性等價於各通道獨立穩定性的聯合（parallel interconnection theorem）。各通道均有硬限幅，因此 BIBO 穩定。L0 Safety Floor/Ceiling 提供全域安全網。

**嚴格 Lyapunov 證明延後至 Cycle 02-7**（P1 Lyapunov 參數校準）。

---

## 4.4 語義對稱性

Option C 的語義區分極為清晰：

| 維度 | L2 (Audit) | L3 (LoopQuality) |
|------|-----------|-------------------|
| 作用對象 | confidence（信心度） | threshold（閾值） |
| 語義問句 | 「這個 arbiter 的判斷可靠嗎？」 | 「目前系統狀態是否適合快速路徑？」 |
| 控制理論類比 | 狀態估計器校正（state estimator correction） | 參考輸入調整（setpoint adjustment） |
| 方向 | 調整「測量值」的可信度 | 調整「通過門檻」的嚴格度 |
| 輸入來源 | AuditContext（arbiter 結果） | EventBus（monitor 觀測） |
| 數值範圍 | +-0.05 | alpha * q in [0, 0.10] |

WIENER 的評價：「這是我見過最乾淨的分離。兩個通道各自有明確的物理意義，不會互相污染。」

---

## 4.5 alpha 參數選擇

| alpha | theta=0.6 時最大調整 | 評估 |
|-------|---------------------|------|
| 0.05 | 0.57（降 0.03） | 極保守 |
| **0.10** | **0.54（降 0.06）** | **建議預設** |
| 0.15 | 0.51（降 0.09） | 激進 |
| 0.20 | 0.48（降 0.12） | 過度——可能突破 thresholdFloor |

WIENER 選擇 alpha = 0.10 的理由：

1. 最大調整約 +-6%，在人類可感知範圍內，便於調試
2. 與 L2 的 +-0.05 影響量級相當——L3 不會淹沒 L2
3. 保守起步，可根據 Simulation 數據調整

**L3 公式的語義解釋**：

| compositeLoopQuality | theta_adjusted（theta=0.6） | 含義 |
|---------------------|---------------------------|------|
| 1.0（最佳品質） | 0.54（theta * 0.9） | 系統運行穩定 → 略微放鬆閾值 → 更容易快速路徑 |
| 0.5（中等品質） | 0.57（theta * 0.95） | 中等調整 |
| 0.0（最差/無觀測） | 0.60（theta * 1.0） | 保守退化——閾值不變 |

---

## 4.6 品質分數的雙通道傳遞

品質監控器產出的分數有兩個消費者，需求不同：

| 消費者 | 需要什麼 | 通道 |
|--------|---------|------|
| ManoAggregator（L3 閾值調整） | 即時的 composite 數字 | **pull**：`loopQualityFn()` 回調 |
| IConfidenceAuditor（豐富背景） | 四維向量 + composite | **push**：extras bag via EventBus |

**Pull 通道**：`loopQualityFn` 注入 `createManoAggregator`，在 `route()` 內每次需要時同步呼叫。

```typescript
export function createManoAggregator(
  bus: EventBus,
  config: ManoAggregatorConfig,
  baseThresholdFn?: () => number,
  vedanaFn?: () => ChannelVedana,
  vedanaEmergencyConfig?: VedanaEmergencyConfig,
  auditor?: IConfidenceAuditor,
  loopQualityFn?: () => number,  // 新增：回傳 compositeLoopQuality in [0, 1]
): ManoAggregator
```

**Push 通道**：Monitor 使用 SDK `emitWithExtras()` 同時發出：
- `loopQuality:updated` 事件（ManoAggregator 訂閱，用於 pull 回調的內部快取更新）
- `audit:context_contribute` 事件（ManoAggregator 收集進 extras bag）

extras 中的 key：
- `loopQuality:composite` → composite score（number）
- `loopQuality:vector` → 四維向量物件

LEIBNIZ 的關鍵約束：「品質分數的生命週期是 per-routing-cycle。每次路由結束，extras bag 清空。不累積、不持久化。」延遲一 tick 可接受——品質是歷史指標，不需要即時到微秒級。

---

## 4.7 邊界條件分析

**無 Monitor Plugin（G-0 退化路徑）**：`loopQualityFn` 回傳 `undefined` 或 `q_default = 0`，L3 不生效：`theta_adjusted = theta`（乘以 1.0）。系統行為與沒有 ILoopQualityMonitor 時完全相同。

**Monitor 報告過時**：設定 `monitorStalenessMs = 5000`（可配置）。過期則視為無觀測 → q = 0。WIENER 的理由：過時觀測等於引入「幽靈信號」，與零階保持（ZOH）原則的有效期限概念一致。

**多 Monitor 聚合**：Phase 1 使用簡單平均（降低個別 monitor 的噪聲影響）。BABBAGE 提出的悲觀策略（取最低）被否決——單一異常 monitor 不應過度影響整體。

**compositeLoopQuality = 1.0 極端值**：若 `theta = thresholdFloor = 0.30`，`theta_adjusted = 0.27 < thresholdFloor`。修正：L3 調整後仍需遵守 L0：

```typescript
const adjustedThreshold = Math.max(
  config.thresholdFloor,
  threshold * (1 - loopQualityAlpha * compositeLoopQuality),
);
```

---

## 4.8 完整五層公式（Option C 整合後）

```
theta_base                                        // 基礎閾值（config 注入）
  + L1: Sigma(w_k * K_k)                         // Klesha 增益（baseThresholdFn）
  + L4: thresholdBoost                            // VedanaEmergency 提升
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

**Layer 執行順序**：L4（VedanaEmergency）→ L1（Klesha）→ L3（LoopQuality）→ 比較（含 L2-adjusted confidence）。L4 優先因為它處理安全關鍵的緊急狀態。

**L2 與 L3 的最壞交互**：confidence 增加 0.05 且 threshold 降低 0.06 → 淨效果約 0.11。仍在 L0 安全範圍內（`thresholdFloor` + `maxConfidenceByGear` 共同約束）。

---

## 4.9 ManoAggregator 程式碼整合點

在 `mano-aggregator.ts` 的 arbiter 迴圈中，L134-L138 現行閾值計算後插入 L3 調整：

```typescript
// 現行：L0 + L1 + risk adjustment
const threshold = evaluation.riskCategory
  ? computeAdjustedThreshold(
      effectiveBaseThreshold, evaluation.riskCategory,
      config.riskDelta, config.thresholdFloor, config.thresholdCeiling)
  : effectiveBaseThreshold;

// 新增：Layer 3 -- LoopQuality threshold adjustment
const loopQualityAlpha = config.loopQualityAlpha ?? 0.10;
const q = loopQualityFn ? loopQualityFn() : 0;
const adjustedThreshold = Math.max(
  config.thresholdFloor,
  threshold * (1 - loopQualityAlpha * q),
);

// 修改：使用 adjustedThreshold
if (evaluation.confidence > adjustedThreshold) {
  // ... existing routing logic ...
}
```

新增 `ManoAggregatorConfig` 欄位：

```typescript
export interface ManoAggregatorConfig {
  // ... existing fields ...
  readonly loopQualityAlpha?: number;       // [0, 0.2], default: 0.10
  readonly monitorStalenessMs?: number;     // default: 5000
  readonly historicalConfidenceSize?: number; // default: 10
}
```

WIENER 的最終聲明：「Option C 的穩定性保證基於兩通道獨立性假設。若未來設計破壞此獨立性（如讓 auditor 讀取 loopQuality 並據此調整 delta），穩定性保證不再成立。extras bag 中 auditor 可以看到 `loopQuality:composite`，但 WIENER C-1/C-2/C-3 確保了即使看到也不會形成正反饋迴路——因為 auditor 的 delta 不會回饋到 loopQuality 的計算中。」
