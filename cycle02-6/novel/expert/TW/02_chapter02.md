# 第二章：AuditContext 與回饋迴路防護

---

## 2.1 問題：審計員的資訊貧乏

v0.29.0-alpha 中 `IConfidenceAuditor.audit()` 的簽名為：

```typescript
// v0.29.0-alpha 現狀
audit(routeResult: RouteResult): ConfidenceAuditResult | Promise<ConfidenceAuditResult>;
```

其中 `RouteResult` 僅包含 `{ gear, decidedBy, confidence, riskAdjusted, riskCategory }`。一個有效的審計員需要更多上下文：觸發事件是什麼？arbiter 的完整推理過程？近期信心度趨勢？其他 plugin 觀測到的輔助數據？

DC Master 在 R0 指示中裁定方案 B（泛型 Context Bag）為唯一正確方向，否決了方案 A（固定欄位擴展）的僵化設計。

---

## 2.2 AuditContext 完整型別定義 [D2-R1, 20/20]

```typescript
import type { SparshEvent } from './coarising.js';
import type { GearEvaluation, RouteResult, RiskCategory } from './gear-arbiter.js';

/**
 * AuditContext -- rich context for confidence auditing.
 *
 * Replaces bare RouteResult as the input to IConfidenceAuditor.audit().
 * Core fields provide the minimum for meaningful auditing;
 * extras bag allows plugin-contributed data without Core coupling.
 *
 * @version 1 -- initial version (Cycle 02-6)
 */
export interface AuditContext {
  /** Schema version for forward compatibility. Literal type. */
  readonly version: 1;

  /** 觸發本次認知迴圈的 SparshEvent */
  readonly sparshEvent: SparshEvent;

  /** 勝出 arbiter 的完整評估結果（含 confidence + reasoning） */
  readonly gearEvaluation: GearEvaluation;

  /** 當前風險等級（可能為 undefined = 未宣告） */
  readonly riskCategory: RiskCategory | undefined;

  /** 路由結果（審計前快照） */
  readonly routeResult: RouteResult;

  /**
   * 近期歷史信心度序列（opt-in，環形緩衝區，預設 size=10 可配置）。
   *
   * WIENER C-1 約束：僅包含原始 arbiter 信心度，
   * 不包含 audit 後的修正值。
   */
  readonly historicalConfidence?: readonly number[];

  /**
   * Plugin 貢獻的額外上下文數據。
   * ManoAggregator 從 EventBus 收集 plugin 的 context contribution，
   * 統一放入此 Map。Core 不感知具體 key/value 語義。
   * 傳入 auditor 前以 Object.freeze() 凍結。
   */
  readonly extras: ReadonlyMap<string, unknown>;
}
```

**設計抉擇摘要**：

| 決策點 | 選項 | 最終選擇 | 理由 |
|--------|------|---------|------|
| `sparshEvent` 是否 optional | optional vs required | **required** | 每次路由必有觸發事件；ManoAggregator 經由 `sparshEventFn` 回調取得 |
| `historicalConfidence` 緩衝區大小 | 固定 10 vs 可配置 | **預設 10 可配置** | `ManoAggregatorConfig.historicalConfidenceSize` |
| `version` 型別 | `number` vs 字面量 `1` | **字面量 `1`** | 強制型別檢查，未來版本遞增為 `2` |
| `extras` 型別 | `Record<string, unknown>` vs `ReadonlyMap` | **`ReadonlyMap`** | Map 語義更清晰，freeze 更直觀 |

**IConfidenceAuditor 介面更新**：

```typescript
export interface IConfidenceAuditor extends IVijnana {
  readonly id: string;
  audit(context: AuditContext): ConfidenceAuditResult | Promise<ConfidenceAuditResult>;
}
```

這是一個 breaking change（參數從 `RouteResult` 改為 `AuditContext`），但 TURING 在 D1 程式碼驗證中確認 v0.29.0-alpha **尚無任何 IConfidenceAuditor plugin 實作**——這是最佳重構時機，零實際影響。

---

## 2.3 WIENER 約束：回饋迴路的系統性切斷

WIENER 在 Cycle 02-4 D5 中已證明：若歷史 audit delta 回饋至當前 audit 輸入，可產生正反饋迴路：

```
Loop N:   auditor 輸出 delta = +0.03
Loop N+1: auditor 看到上次 delta = +0.03，傾向正向 → delta = +0.04
Loop N+2: 持續正向累積 → 系統漂移
```

形式化表述：令 $c_n$ 為第 $n$ 次迴圈的 arbiter 原始信心度，$\delta_n$ 為 audit delta。

- **允許的輸入**：$\delta_n = f(c_n, c_{n-1}, \ldots, c_{n-k}, \text{extras}_n)$ -- 觀測函數
- **禁止的輸入**：$\delta_n = g(\delta_{n-1}, \delta_{n-2}, \ldots)$ -- 自回歸函數

前者的穩定性取決於被觀測系統（外生的），後者可獨立發散（內生的）。這是控制理論中觀測器（observer）與自回歸系統（autoregressive system）的根本區別。

據此設計三條硬約束（WIENER Constraints C-1/C-2/C-3）：

**C-1**：`historicalConfidence` 僅包含原始 arbiter 信心度（`GearEvaluation.confidence`），不包含 audit 後的修正值（`auditedConfidence`）。

```typescript
// ManoAggregator 內部——每次 arbiter 勝出後記錄
confidenceHistory.push(evaluation.confidence);  // 原始值
// 不是 confidenceHistory.push(auditedConfidence);  // 禁止
```

**C-2**：AuditContext 不包含任何 `previousAuditResult`、`previousDelta`、`auditHistory` 欄位。Auditor 無法從 AuditContext 讀取自身先前的輸出。

**C-3**：extras bag 禁止三個前綴：`audit:`、`core:`、`internal:`。防止 auditor 透過 extras 繞過 C-2。

```typescript
// extras 寫入驗證
const FORBIDDEN_PREFIXES = ['audit:', 'core:', 'internal:'] as const;

function validateExtrasKey(key: string): boolean {
  return !FORBIDDEN_PREFIXES.some(prefix => key.startsWith(prefix));
}
```

BABBAGE 的 BIBO 穩定性驗證：在 C-1/C-2/C-3 約束下，audit delta $\delta_n$ 的輸入集合完全由外生變量構成（arbiter 原始信心度序列 + plugin extras），不包含任何自身歷史輸出。因此 $|\delta_n| \le 0.05$（硬限幅），系統滿足有界輸入 → 有界輸出（BIBO stability）。

---

## 2.4 extras bag 協議 [D2-R2, 19/20]

extras bag 的設計在 R2 階段出現了唯一的跨軌道分歧：A2（DARWIN + MESH）提出通用事件模式，B3（LEIBNIZ + MESH）傾向直接訂閱。D2 辯論中統一為**雙事件 + SDK 便利函數**：

| 面向 | 決議 |
|------|------|
| 寫入模式 | Plugin 使用 SDK `emitWithExtras(key, value)` 便利函數 |
| 收集管道 | ManoAggregator 訂閱 `audit:context_contribute` 事件 |
| 讀取 | `getExtra<T>(extras, key, guard)` 型別安全存取器 |
| 不可變性 | 淺凍結（`Object.freeze`）+ `ReadonlyMap` |
| 容量限制 | 最多 32 keys，每 key 128 chars |
| 禁止前綴 | `audit:`, `core:`, `internal:` |
| key 命名慣例 | `{category}:{name}` -- 如 `loopQuality:vector`, `loopQuality:composite` |
| 生命週期 | per-routing-cycle（每次路由結束清空，不持久化） |

1 票反對（MESH）認為雙事件模式增加了不必要的複雜度。但多數認為通用管道的投資回報更高：它不只為 LoopQualityMonitor 服務，任何未來的 Plugin 都能透過同一管道向 AuditContext 貢獻數據。

---

## 2.5 ConfidenceAuditLog——GUARDIAN D5 債務清償 [D2-R3, 20/20]

GUARDIAN 在 Cycle 02-5 D5 做了一個關鍵讓步：同意 audit delta 限幅 +-0.05，條件是下一輪必須定義完整的審計日誌格式。這是一筆安全債務。

Cycle 02-6 設計了 `ConfidenceAuditLog` 型別：

```typescript
export interface ConfidenceAuditLog {
  readonly timestamp: number;
  readonly auditorId: string;
  readonly inputConfidence: number;    // audit 前的信心度
  readonly rawDelta: number;           // auditor 建議的 delta
  readonly clampedDelta: number;       // 限幅後的 delta
  readonly wasClamped: boolean;        // 是否被限幅
  readonly reasoning: string;          // 截斷至 500 chars，Core 負責
  readonly outputConfidence: number;   // audit 後的信心度
  readonly result: 'applied' | 'timeout' | 'error';
  readonly auditDurationMs: number;
}
```

傳播通道：
- **主通道**：EventBus `audit:completed` 事件，即時可觀察
- **持久化**：JSONL file appender（可選，Plan30 之後）
- **PII 淨化**：reasoning 欄位的 PII 清洗為 plugin 責任，Core 只做截斷

GUARDIAN 在 D2 辯論中當場確認：「D5 的帳清了。我不再保留重新審議 +-0.05 限幅的權利。」這是一個重要的安全里程碑——自 Cycle 02-4 以來 GUARDIAN 持續挑戰信心度調整的安全性，每次讓步都附帶條件。完整日誌 + 三條回饋迴路防護 + +-0.05 硬限幅，三重保障終於滿足了他的安全要求。

---

## 2.6 版本控制策略

`AuditContext.version` 使用字面量型別 `1`（非 `number`），確保編譯期型別檢查。未來擴展時遞增為 `2`，Auditor plugin 應對不認識的版本 fail-safe：

```typescript
function audit(ctx: AuditContext): ConfidenceAuditResult {
  if (ctx.version > 1) {
    return { delta: 0, reasoning: 'Unknown AuditContext version' };
  }
  // 正常審計邏輯...
}
```

這個 fail-safe 模式保證了向前相容性：新版 Core 搭配舊版 Auditor plugin 時，auditor 不會因不認識新欄位而崩潰，而是退化為 passthrough（delta=0）。
