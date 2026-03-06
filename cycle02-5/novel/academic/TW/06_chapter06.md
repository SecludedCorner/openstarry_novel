# 第六章：純粹的工程——D5 Plan29 工程規格辯論

---

**時長**：~75 分鐘 | **參與者**：10 人 | **投票**：9 項

D5 是本專案歷史上第一場完全沒有佛學內容的辯論。十位工程師和科學家，零位佛學家（NAGARJUNA 和 ASANGA 自願退出），討論 TypeScript 介面的精確規格。

TURING 預提交了完整的 v0.28.0-alpha 設計模式報告——14 個原始碼文件、所有 Registry 生命週期、timeout 模式、同步/非同步模式、失敗處理策略。這份「程式碼考古學」報告為所有決策提供了事實基礎。

## 九項決議

| 決議 | 內容 | 票數 |
|------|------|------|
| D5-R1 | 獨立 `auditor` hook 槽位（不複用 monitors） | 8/8 |
| D5-R2 | audit() 雙模式回傳 `T \| Promise<T>` | **5/8** |
| D5-R3 | timeout 200ms，fail-safe delta=0，可配置 | 8/8 |
| D5-R4 | 單一 auditor，last-wins（非陣列） | 6/8 |
| D5-R5 | 失敗處理：delta=0 + warning log | 共識 |
| D5-R6 | MonitorRegistry 在 ExecutionLoop.onLoopStart() 啟動 | 7/8 |
| D5-R7 | LoopQualityVector 等權重 0.25×4 | 8/8 |
| D5-R8 | validatePluginSkandha() 維持 warning-only | 7/8 |
| D5-R9 | IConfidenceAuditor extends IVijnana，skandha ['vijnana'] | 8/8 |

**最激烈投票**：D5-R2（5/8）——純非同步 vs 雙模式。GUARDIAN/KERNEL/VITRUVIUS 主張純非同步語義更精確；多數採雙模式，遵循 IGearArbiter 先例和測試便利性。

## IConfidenceAuditor 最終規格（100%）

```typescript
export interface IConfidenceAuditor extends IVijnana {
  readonly id: string;
  audit(confidence: number, context: GearContext):
    ConfidenceAuditResult | Promise<ConfidenceAuditResult>;
}
export interface ConfidenceAuditResult {
  delta: number;       // clamped to [-0.05, +0.05]
  reasoning: string;   // audit trail
}
```

PluginHooks 最終形態：
```typescript
interface PluginHooks {
  // ... 既有欄位 ...
  monitors?: ILoopQualityMonitor[];   // Plan29 Wave 1
  auditor?: IConfidenceAuditor;       // Plan29 Wave 2
}
```

NAGARJUNA 在 D5 結束後的評語：「D4 證明了名字需要對定義負責。D5 證明了有些工程問題根本不需要定義——只需要規格。」

---
