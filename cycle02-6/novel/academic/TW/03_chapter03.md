# 第三章：四維品質向量 —— 認知迴路的量化評估框架

---

## 3.1 問題定義

OpenStarry 的 AI Agent 運作於認知迴路中：sparsha → vedana → samjna → samskara → manas/vijnana → 下一輪輸入。`ILoopQualityMonitor` 需對此迴路的運作品質進行即時量化評估。品質是多維概念，單一指標不足。WIENER（#12）與 ATHENA（#5）設計了四維品質向量（LoopQualityVector），經 D3-R1（20/20）確認。

---

## 3.2 四維公式

設滑動窗口大小 $W = 10$，暖機期 $W_{warmup} = 5$。

### 3.2.1 一致性（Coherence）

$$\text{coherence} = 1 - \frac{\text{switchCount}}{W - 1}$$

衡量路由決策穩定性。高值表示 Agent 持續在同一處理模式下運作，低值表示頻繁切換。輸入事件：`gear:switch`。

### 3.2.2 效率（Efficiency）

$$\text{efficiency} = \frac{\text{success}}{\text{proposed}} \quad (\text{若 proposed} = 0, \text{則} = 1.0)$$

衡量工具呼叫成功率。退化處理：無 proposed 事件時預設 1.0。輸入事件：`action:proposed`, `tool:result`。

### 3.2.3 收斂性（Convergence）

$$\text{convergence} = \frac{\text{longestStreak}}{W}$$

衡量 Agent 是否趨近穩定狀態。與效率的區別：效率衡量「總量」，收斂性衡量「趨勢」—— 8 次成功集中在最後 8 次（收斂性 0.8）與散布在窗口各處（可能僅 0.3）意義不同。輸入事件：`gear:switch`。

### 3.2.4 穩定性（Stability）

$$\text{stability} = 1 - \min\left(1, \frac{\sigma^2}{0.25}\right)$$

衡量仲裁器信心度輸出的方差。分母 0.25 為寬鬆正規化基準。輸入事件：`gear:arbiter_evaluated`。

---

## 3.3 複合品質分數與權重

$$Q = \sum_{i=1}^{4} w_i \cdot d_i, \quad Q \in [0, 1]$$

Phase 1 等權重 $w_i = 0.25$。理論依據為 PASCAL（#19）的最大熵論證：在缺乏先驗知識的情況下，最大熵原則（Jaynes 1957）要求均勻分配權重。D3-R4（20/20）確認 Phase 1 固定等權重、Phase 2 可配置（balanced / stability-focused / efficiency-focused 三組預設）。

---

## 3.4 滑動窗口與計算複雜度

| 參數 | 值 | 理由 |
|------|-----|------|
| $W$ | 10 | 敏感度與穩健性之間的平衡 |
| $W_{warmup}$ | 5 | 暖機期避免小樣本偏差 |
| $Q_{default}$ | 0.5 | 暖機期內的中性預設值 |

所有計算 $O(1)$ per event、$O(W)$ 空間，確保品質監控不成為效能瓶頸。

---

## 3.5 EventBus 事件訂閱 [D3-R2, 20/20]

**Phase 1（6 事件）**：`gear:arbiter_evaluated`（穩定性）、`gear:switch`（一致性+收斂性）、`action:proposed`（效率）、`tool:result`（效率）、`loop:started`（窗口管理）、`loop:finished`（窗口管理）。

**Phase 2（+5 事件）**：`sparsha:contact`, `tool:error`, `tool:blocked`, `vitakka:stall`, `action:executed`。

**退化原則**（HERACLITUS #15）：「缺失是資訊，不是錯誤。」缺失事件使用安全預設值（效率 1.0、穩定性 0.5），不拋出異常。同時將散布於程式碼中的事件字串字面量統一提升為 `AgentEventType` 常量。

---
