# 第四章：雙通道整合架構 —— Layer 2/3 的正交分離設計

---

## 4.1 決策機制的形式化描述

OpenStarry 的核心路由決策為閾值比較：若 $c > \theta$ 則採用仲裁器推薦方案，否則走預設方案。Cycle 02-6 引入 IConfidenceAuditor（Layer 2，調整 $c$）和 ILoopQualityMonitor（Layer 3，調整 $\theta$）。核心問題：如何讓兩者同時生效而不互相干擾？

---

## 4.2 三個候選方案與選擇

**方案 A（串聯）**：$Q$ 先改閾值，審計員在新閾值下評估。存在序列依賴。
**方案 B（耦合）**：$Q$ 和審計員同時影響信心度與閾值。存在交叉項。
**方案 C（正交）**：審計員僅改信心度，品質監控器僅改閾值。完全獨立。

D2-R4（20/20 全票）選擇方案 C。

---

## 4.3 方案 C 的形式化定義

**Layer 2**：$c_{adj} = c_{raw} + \text{clamp}(\Delta c, -0.05, +0.05)$

**Layer 3**：$\theta_{adj} = \max(\theta_{floor}, \; \theta_{base} \times (1 - \alpha \cdot Q))$，其中 $\alpha = 0.10$

**最終路由**：$c_{adj} > \theta_{adj}$ → arbiter\_gear，否則 default\_gear

---

## 4.4 設計優勢

**正交性**：Layer 2 僅操作 $c$，Layer 3 僅操作 $\theta$，不存在 $f(c, Q)$ 或 $g(\theta, \Delta c)$ 形式的耦合函數。兩元件可獨立開發、測試、部署。

**BIBO 穩定性**：$c_{adj}$ 受 $[0,1]$ 夾持，$\theta_{adj} \geq \theta_{floor} > 0$，無交叉項則無通道間正回饋放大路徑。

**保守退化**：無審計員則 $\Delta c = 0$；無品質監控器則 $Q = 0$。任一元件缺失時系統行為等價於該元件不存在的版本。

---

## 4.5 品質分數傳輸：Pull + Push 雙通道

| 消費者 | 需求 | 傳輸模式 |
|--------|------|---------|
| ManoAggregator（L3） | 即時數值 | Pull：`loopQualityFn()` 回調 |
| IConfidenceAuditor（L2） | 豐富背景 | Push：extras bag via `audit:context_contribute` |

Push 通道寫入 `loopQuality:vector`（四維）和 `loopQuality:composite`（$Q$）。生命週期為 per-routing-cycle，每次路由結束後 extras bag 清空（LEIBNIZ #14 強調：避免過時資訊累積）。

---

## 4.6 五層決策模型

```
L0: EventBus          -- 基礎事件流
L1: Klesha（煩惱）     -- 四個情緒模組調整閾值
L4: Vedana Emergency   -- 緊急感受直接降低閾值（安全關鍵，優先級最高）
L3: LoopQuality        -- 品質分數微調閾值（α=0.10）
L2: Audit              -- 審計員微調信心度（±0.05）
→ 最終比較: c_adj > θ_adj → 路由決策
```

Layer 順序遵循優先級遞減原則。Plan30 的成功標準：L0~L4 全部有實際信號路徑。

**邊際情境**：多監控器以簡單平均聚合（Phase 1）；監控器超過 5000ms 未更新視為過期，$Q = 0$，L3 不生效。

---
