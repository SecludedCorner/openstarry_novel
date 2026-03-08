# 第三章：四維品質向量與觀測器設計

---

## 3.1 設計規格到 SDK 維度的映射

Plan29 的 SDK 介面已定義了四維向量的欄位名，但計算公式留空。Doc 43 設計規格與 SDK 實作之間的映射如下：

| Doc 43 設計規格 | SDK 欄位名 | 語義 | 公式符號 |
|----------------|-----------|------|---------|
| Continuity（連續性） | `coherence` | 路由決策的邏輯一致性 | C |
| Granularity（精細度） | `efficiency` | 工具執行的資源利用效率 | E |
| Speed（速度） | `convergence` | 目標收斂性 | Conv |
| Equanimity（平衡性） | `stability` | 信心度的振盪穩定性 | S |

---

## 3.2 通用參數

| 符號 | 定義 | 預設值 | 來源 |
|------|------|--------|------|
| W | 滑動窗口大小 | 10 ticks | 設計選擇：平衡靈敏度與穩定性 |
| W_warmup | 暖機期 | 5 ticks | 最小統計顯著性 |
| Q_default | 暖機期複合分數 | 0.5 | 中性預設（不觸發 L3 調整） |

暖機期規則：若 `tickCount < W_warmup`，所有維度回傳 0.5，composite = 0.5。暖機期資料仍計入滑動窗口，但不對外發出品質報告。

---

## 3.3 coherence（C）：路由一致性

**語義**：衡量認知迴圈路由決策的一致程度。齒輪快速振盪（1->2->1->2）表示系統猶豫不決。

**公式**：

$$C = 1 - \frac{\text{gearSwitchCount}}{W - 1}$$

其中 `gearSwitchCount` = 窗口 W 內 gear 值變化的次數，`W-1` = 最壞情況（每 tick 都切換）。

**輸入事件**：`gear:switch`（`payload.gear`）

**實作**：維護長度 W 的 circular buffer，記錄最近 W 次 gear 值。每次新事件進入時，O(1) 更新——增加新的相鄰差異計數，移除舊的。

**邊界案例**：

| 情況 | 行為 | 理由 |
|------|------|------|
| 無 `gear:switch` 事件 | C = 1.0 | 無振盪 = 完美一致 |
| 窗口資料不足 W 筆 | 分母 = max(actualCount - 1, 1) | 避免除以零 |
| W = 1 | C = 1.0 | 單 tick 無法振盪 |

---

## 3.4 efficiency（E）：工具執行效率

**語義**：提案的工具呼叫中成功執行的比率。

**公式**：

$$E = \begin{cases} \frac{\text{successfulExec}}{\text{totalProposed}} & \text{if } \text{totalProposed} > 0 \\ 1.0 & \text{otherwise (純對話迴圈)} \end{cases}$$

**輸入事件**：

| 事件 | 用途 | 備註 |
|------|------|------|
| `action:proposed` | 分母 | 每次工具呼叫提案 |
| `tool:result` | 分子 | 成功執行 |
| `tool:error` | 隱含（Phase 2） | 不計入分子 |
| `tool:blocked` | 隱含（Phase 2） | 不計入分子 |

**設計選擇**：純對話迴圈（無工具呼叫）定義為 E = 1.0，不懲罰無工具場景。這是因為效率維度衡量的是「提出的行動是否成功」，沒有提出行動不等於效率低。

---

## 3.5 convergence（Conv）：目標收斂性

**語義**：系統路由決策是否朝同一方向持續推進。連續選擇同一齒輪越久，表示迴圈越收斂。

**公式**：

$$\text{Conv} = \frac{\text{longestConsistentStreak}}{W}$$

**Phase 2 替代方案（ATHENA 建議）**：指數移動平均（EMA）

$$\text{consistency}_t = \begin{cases} 1.0 & \text{if } \text{gear}_t = \text{gear}_{t-1} \\ 0.0 & \text{otherwise} \end{cases}$$

$$\text{EMA}_t = \alpha \cdot \text{consistency}_t + (1 - \alpha) \cdot \text{EMA}_{t-1}, \quad \alpha = \frac{2}{W + 1}$$

Phase 1 使用 streak 方法（簡單、可解釋）；Phase 2 有運行數據後再評估是否切換 EMA。

**輸入事件**：`gear:switch`。注意 convergence 和 coherence 使用同一來源，但計算邏輯不同：coherence 測量切換頻率，convergence 測量最長連續同向。

---

## 3.6 stability（S）：信心度穩定性

**語義**：arbiter 信心度的波動程度。基於方差的倒數映射。

**公式**：

$$S = 1 - \min\left(1, \frac{\sigma^2}{0.25}\right)$$

其中 $\sigma^2$ 為窗口 W 內 confidence 值的（母體）方差，0.25 為保守上界（二值分佈 {0,1} 的方差 = 0.25，[0,1] 均勻分佈的方差 $\approx 0.083$）。

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

滑動窗口版本需維護 circular buffer + 增量更新，仍為 O(1) per event。

**輸入事件**：`gear:arbiter_evaluated`（`payload.confidence`）

**邊界案例**：

| 情況 | S 值 | 理由 |
|------|------|------|
| 無 arbiter 事件 | 1.0 | 無波動 = 完美穩定 |
| 所有 confidence 相同 | 1.0 | 方差 = 0 |
| confidence 在 0/1 間交替 | 0.0 | 最大不穩定 |

---

## 3.7 Composite Score 與權重

**公式** [D3-R4, 20/20]：

$$Q = w_C \cdot C + w_E \cdot E + w_{\text{Conv}} \cdot \text{Conv} + w_S \cdot S$$

Phase 1 權重全部固定為 0.25（等權重）。PASCAL 的最大熵論證：在沒有經驗數據支持任何維度更重要的前提下，最大熵原則（Maximum Entropy Principle）指示給每個可能性相同的權重——這不是懶惰，而是在無資訊時的最優策略。

Phase 2 權重可配置，存儲在 monitor plugin config 中（不是 `ManoAggregatorConfig`——計算者擁有其參數）。三組預設：

| 預設 | coherence | efficiency | convergence | stability |
|------|-----------|-----------|-------------|-----------|
| balanced | 0.25 | 0.25 | 0.25 | 0.25 |
| stability-focused | 0.15 | 0.20 | 0.15 | 0.50 |
| efficiency-focused | 0.15 | 0.50 | 0.20 | 0.15 |

驗證約束：$\sum w_i = 1.0$，每個 $w_i \in [0, 1]$。

**值域保證**：每個維度 $d_i \in [0, 1]$，權重 $w_i \in [0, 1]$，$\sum w_i = 1.0$，因此 $Q \in [0, 1]$。這個有界性對 L3 整合的 BIBO 穩定性至關重要。

---

## 3.8 觀測器性質：控制理論視角

WIENER 特別強調四維公式的**純觀測函數**性質——這是控制理論中觀測器（observer）的定義：

- **輸入**：系統事件流（不可控，唯讀）
- **狀態**：內部滑動窗口（不影響被觀測系統）
- **輸出**：LoopQualityVector（只讀報告，不回寫）

Monitor 的蘊歸屬 = [vedana, samjna, vijnana]，**排除 samskara**。四個公式均為觀測計算，絕不修改 EventBus 上的事件、不呼叫任何 plugin、不觸發任何行動。這確保了觀測器不會干擾被觀測系統——控制理論中的「非侵入性觀測」原則。

**Lyapunov 穩定性前瞻**：stability 維度（S）的方差時間序列為 Cycle 02-7 的 Lyapunov 穩定性分析提供基礎數據。若 $\sigma^2$ 持續下降，符合 Lyapunov 函數遞減條件的前提。

---

## 3.9 EventBus 事件訂閱 [D3-R2, 20/20]

**Phase 1（MINIMAL_QUALITY_EVENTS = 6）**：

1. `gear:arbiter_evaluated` → stability（confidence 值）
2. `gear:switch` → coherence + convergence（gear 值）
3. `action:proposed` → efficiency 分母
4. `tool:result` → efficiency 分子
5. `loop:started` → tick 計數、窗口重置
6. `loop:finished` → 觸發品質報告發出

**Phase 2（+5 EXTENDED_QUALITY_EVENTS）**：

7. `sparsha:contact` → 輸入頻率分析
8. `tool:error` → 細化效率計算
9. `tool:blocked` → 安全阻擋頻率
10. `vitakka:stall` → 認知停滯偵測
11. `action:executed` → 執行延遲分析

**退化原則**（HERACLITUS）：缺失事件 → 安全預設值，不報錯。效率缺失 → 1.0（假設正常），穩定性缺失 → 0.5（中性）。「缺失是資訊，不是錯誤。」

**Plan30 行動項**：Plan27b 中散落在程式碼裡的事件字串必須提升為 `AgentEventType` 常量——7 個新常量（6 個既有 + `LOOP_QUALITY_UPDATED`）。

---

## 3.10 計算複雜度摘要

| 維度 | 每事件 | 每報告 | 空間 |
|------|--------|--------|------|
| coherence | O(1) | O(1) | O(W) circular buffer |
| efficiency | O(1) | O(1) | O(1) 兩個計數器 |
| convergence | O(1) | O(1) | O(W) circular buffer |
| stability | O(1) | O(1) | O(W) circular buffer + Welford state |
| **composite** | -- | O(1) | -- |

**整體**：O(1) per event，O(1) per report，O(W) 空間。在 W=10 的情況下，記憶體開銷可忽略不計。
