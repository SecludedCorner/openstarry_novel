# 第二章：審計上下文的型別設計 —— 資訊充分性與回饋迴路切斷

---

## 2.1 問題分析：IConfidenceAuditor 的資訊貧乏

Plan29 交付的 `IConfidenceAuditor` 介面存在結構性缺陷：審計函數的輸入僅包含 `RouteResult`（路由結果）。審計員無法獲取觸發事件（sparshEvent）、仲裁器推理過程（gearEvaluation）、風險等級（riskCategory）或歷史信心度序列。以決策理論術語而言，這是一個資訊不對稱（information asymmetry）問題。DC Master 明確指示審計員需要更多資訊。

然而，擴充審計員可見資訊的同時引入了控制理論風險：**正回饋迴路**（positive feedback loop）。

---

## 2.2 正回饋迴路的威脅模型

WIENER（#12）識別出三條潛在的正回饋路徑：

1. **historicalConfidence 污染**：若歷史序列包含審計後調整值，形成 `audit → confidence → history → audit` 閉合迴路
2. **審計結果洩漏**：若 AuditContext 包含前次審計結果，形成確認偏誤驅動的序列相關
3. **extras 後門**：若 extras bag 允許寫入審計相關鍵值對，間接洩漏歷史輸出

三條路徑均可導致 BIBO 不穩定：信心度值在迭代中單調增長或振盪發散。

---

## 2.3 AuditContext 型別定義 [D2-R1, 20/20]

```typescript
export interface AuditContext {
  readonly version: 1;                              // 字面量型別
  readonly sparshEvent: SparshEvent;                // 觸發事件（必填）
  readonly gearEvaluation: GearEvaluation;          // 仲裁器完整推理過程
  readonly riskCategory: RiskCategory | undefined;  // 風險類別（可選）
  readonly routeResult: RouteResult;                // 審計前路由結果快照
  readonly historicalConfidence?: readonly number[]; // 環形緩衝區，預設 10
  readonly extras: ReadonlyMap<string, unknown>;     // 泛型擴展袋
}
```

核心欄位由 Core 組裝；historicalConfidence 為可選環形緩衝區；extras 為 ReadonlyMap，透過 `getExtra<T>(extras, key, guard)` 型別安全存取器讀取。

---

## 2.4 WIENER 三約束

**C-1（歷史純淨性）**：historicalConfidence 僅記錄仲裁器原始信心度 $c_t^{raw}$，不含審計後調整值。

**C-2（審計結果隔離）**：AuditContext 不包含前次 ConfidenceAuditLog。每次審計資訊獨立。

**C-3（extras 前綴禁令）**：禁止 `audit:`、`core:`、`internal:` 前綴，防止審計結果通過 extras 洩漏。

三約束確保審計員的**因果隔離**（causal isolation）。BABBAGE（#9）的形式化驗證：審計函數 $f: \mathcal{C} \times \mathcal{A} \to [-0.05, +0.05]$ 在三約束下，輸入不含自身先前輸出，調整量受限幅約束，信心度值域 $[0,1]$ 自然有界，系統滿足 BIBO 穩定。

---

## 2.5 extras bag 協議 [D2-R2, 19/20]

| 面向 | 規格 |
|------|------|
| 寫入模式 | 雙事件 + SDK `emitWithExtras()` |
| 收集管道 | ManoAggregator 訂閱 `audit:context_contribute` |
| 讀取介面 | `getExtra<T>(extras, key, guard)` |
| 不可變性 | 淺凍結 + ReadonlyMap |
| 限制 | max 32 keys, 128 chars/key |
| 鍵命名 | `{category}:{name}` 格式 |

一票反對認為雙事件模式增加不必要複雜性，多數認為其通用性（任何 Plugin 均可透過相同協議貢獻資訊）證成了設計。

---

## 2.6 ConfidenceAuditLog [D2-R3, 20/20]

完整審計軌跡型別：inputConfidence, rawDelta, clampedDelta, wasClamped, reasoning（截斷 500 字元）, outputConfidence, result, auditDurationMs。主通道為 EventBus `audit:completed` 事件；JSONL 持久化排程至 Plan31。

GUARDIAN（#11）在此決議通過後正式聲明：「D5 的讓步條件已兌現。我不再保留重新審議 $\pm 0.05$ 限幅的權利。」此聲明終結了自 Cycle 02-4 以來圍繞信心度調整安全性的持續爭議。

---
