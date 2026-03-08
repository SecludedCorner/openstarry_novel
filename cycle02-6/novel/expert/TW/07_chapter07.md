# 第七章：Plan30 工程藍圖與前瞻

---

## 7.1 Plan30 定義

**Plan30 = Default LoopQualityMonitor Plugin + Layer 3 Integration**

決策基礎：D3-R5（19/20 + 1 條件贊成）。前置條件：Plan29 DONE + OQ-29-1/2/4/5 已回答。

---

## 7.2 四個 Wave

### Wave 1：Default Monitor Plugin（約 120 LOC）

核心品質計算引擎，使用 B1 四維公式 + B2 六事件訂閱模型。

```typescript
// 概念性介面（非最終實作）
export class DefaultLoopQualityMonitor implements ILoopQualityMonitor {
  private readonly window: SlidingWindow;      // W=10
  private readonly warmupThreshold = 5;
  private tickCount = 0;

  // circular buffers
  private gearHistory: number[] = [];          // coherence + convergence
  private proposedCount = 0;                   // efficiency 分母
  private successCount = 0;                    // efficiency 分子
  private welfordState: WelfordState;          // stability

  constructor(private readonly bus: EventBus) {
    // Phase 1: 訂閱 6 個事件
    bus.on('gear:arbiter_evaluated', this.onArbiterEvaluated);
    bus.on('gear:switch', this.onGearSwitch);
    bus.on('action:proposed', this.onActionProposed);
    bus.on('tool:result', this.onToolResult);
    bus.on('loop:started', this.onLoopStarted);
    bus.on('loop:finished', this.onLoopFinished);
  }

  report(): LoopQualityReport {
    if (this.tickCount < this.warmupThreshold) {
      return { vector: WARMUP_VECTOR, composite: 0.5, timestamp: Date.now() };
    }
    const vector = {
      coherence:   this.computeCoherence(),
      efficiency:  this.computeEfficiency(),
      convergence: this.computeConvergence(),
      stability:   this.computeStability(),
    };
    const composite = 0.25 * (vector.coherence + vector.efficiency
                             + vector.convergence + vector.stability);
    return { vector, composite: Math.max(0, Math.min(1, composite)), timestamp: Date.now() };
  }
}
```

所有維度 O(1) per event，O(W) 空間。

### Wave 2：Layer 3 ManoAggregator Integration（約 80 LOC）

Option C 佈線。核心修改在 `mano-aggregator.ts`：

1. `createManoAggregator` 新增 `loopQualityFn?: () => number` 參數
2. `ManoAggregatorConfig` 新增 `loopQualityAlpha`、`monitorStalenessMs`、`historicalConfidenceSize`
3. arbiter 迴圈中插入 L3 閾值調整
4. 歷史信心度環形緩衝區（C-1 約束：僅記錄原始值）

```typescript
// L3 閾值調整核心邏輯
const alpha = config.loopQualityAlpha ?? 0.10;
const q = loopQualityFn ? loopQualityFn() : 0;
const adjustedThreshold = Math.max(
  config.thresholdFloor,
  threshold * (1 - alpha * q),
);
```

### Wave 3：Events + Extras + Types（約 60 LOC）

- `AgentEventType` 常量提升：7 個新常量（6 個 Plan27b 既有 + `LOOP_QUALITY_UPDATED`）
- `ConfidenceAuditLog` SDK 型別定義（GUARDIAN D3-R5 條件）
- `audit:context_contribute` 事件定義
- `MINIMAL_QUALITY_EVENTS` 常量（Phase 1 = 6 events）
- `emitWithExtras()` SDK 便利函數

### Wave 4（可選）：PassthroughAuditor（約 30 LOC）

```typescript
export class PassthroughAuditor implements IConfidenceAuditor {
  readonly id = 'passthrough-auditor';

  async audit(context: AuditContext): Promise<ConfidenceAuditResult> {
    // Phase 0: delta=0, pure logging
    return {
      delta: 0,
      reasoning: `Passthrough: confidence=${context.routeResult.confidence}, ` +
                 `gear=${context.routeResult.gear}`,
    };
  }
}
```

用途：端對端管道驗證 + 整合測試 fixture + Phase 1 ThresholdAuditor 的 scaffold。

---

## 7.3 範圍摘要

| 指標 | 估計 |
|------|------|
| 生產程式碼 | 約 260-290 LOC |
| 測試程式碼 | 約 130 LOC |
| 總計 | 約 390-420 LOC |

---

## 7.4 成功標準

**Model Delta L0-L4 全部有實際信號路徑**——每一層從 L0（EventBus 事件流）到 L4（audit 輸出）都不再是空殼，必須有真正的程式碼在運作，以整合測試驗證。

具體而言：
- L0：EventBus 事件被 Monitor 訂閱並處理
- L1：Klesha 增益影響 baseThreshold（已存在）
- L2：Audit delta 調整 confidence（Plan29 已佈線；Plan30 W4 提供 PassthroughAuditor）
- L3：LoopQuality 調整 threshold（Plan30 W2 新增）
- L4：VedanaEmergency boost（已存在）

---

## 7.5 WIENER 約束的工程實施

所有 Wave 必須遵守三條硬約束：

| 約束 | 實施位置 | 驗證方式 |
|------|---------|---------|
| C-1：historicalConfidence 僅含原始值 | W2: 環形緩衝區 push | 單元測試：audit 後的值不出現在 history 中 |
| C-2：AuditContext 不含前次 audit 結果 | W3: AuditContext 型別定義 | 型別檢查：介面中無 previousAuditResult 欄位 |
| C-3：extras 禁止 `audit:` 前綴 | W3: emitWithExtras 驗證 | 單元測試：含禁止前綴的寫入被拒絕 |

---

## 7.6 Plan31 預覽

Plan31 將把 AuditContext 落地到運行路徑中——從型別定義進入實際組裝：

| 項目 | 估計 LOC | 描述 |
|------|---------|------|
| AuditContext 組裝 | ~120 | Core 在 route() 中組裝完整 AuditContext |
| Default ThresholdAuditor | ~120 | Phase 1 規則式審計：低信心度偵測、loopQuality 異常、趨勢偵測 |
| Audit Trail JSONL | ~110 | 持久化層：ConfidenceAuditLog → JSONL file appender |
| **總計** | **~350** | |

Plan30 造管道（型別 + 計算 + 佈線）。Plan31 讓水流過管道（組裝 + 審計 + 持久化）。

---

## 7.7 Plan32+ 長期路線圖

```
Plan30 (本輪)      → Default LoopQualityMonitor + Layer 3 Integration
Plan31 (下輪)      → AuditContext 落地 + Default Auditor + Audit Trail
Plan32 (未來)      → VasanaEngine / SPC / Lyapunov stability
```

Cycle 02-7 的 P1 待研究項目：

1. **Lyapunov 穩定性參數校準**：alpha 值驗證、穩態分析、五層模型的嚴格穩定性證明
2. **Moha/Sneha 耦合模擬**：Klesha 模組（L1）之間的交互作用是否影響 L3 行為
3. **多 monitor 聚合策略驗證**：簡單平均 vs 悲觀策略的經驗數據比較

Cycle 03+ 的延後項目：

- **八識深化**（alaya-vijnana）：多 Agent 場景下的共享記憶機制
- **VasanaEngine**（D-29-8）：行為模式的學習與記憶，對應行蘊「造作一切有為法」
- **ISamskara 方向 A/B**：意圖規劃（cetana-formation）+ 習氣形成（vasana-imprinting）

---

## 7.8 研究成果總結

### 九項成功標準達成

| # | 標準 | 狀態 | 決議 |
|---|------|------|------|
| 1 | AuditContext 完整型別定義 | 達成 | D2-R1 |
| 2 | 審計日誌格式規格（GUARDIAN D5） | 達成 | D2-R3 |
| 3 | LoopQualityVector 4D 公式 | 達成 | D3-R1 |
| 4 | EventBus 事件訂閱清單 | 達成 | D3-R2 |
| 5 | OQ-29 全部回答 | 達成 | 5/5 |
| 6 | Plan30 方向建議 | 達成 | D3-R5 |
| 7 | 行蘊深掘報告 | 達成 | C1-C4 + D1 |
| 8 | 心所逐條蘊歸屬建議 | 達成 | C2（51 項） |
| 9 | 無範圍蔓延 | 達成 | Lyapunov/Moha/FC-26 未討論 |

### 兩大永久性產出

1. **蘊歸屬五原則 + 行蘊三準則**：未來所有蘊歸屬判定的基準線
2. **心所八點規則**：未來所有命名和佛學概念引用的判定基準線

這兩組規則不是單輪決議——它們是跨越所有未來 Cycle 的永久性框架。

### 工程與哲學的匯合

Cycle 02-5 是減法（清除裝飾性映射）。Cycle 02-6 是加法（建立精確規格）。

哲學軌建立了行蘊的原典定義（cetana 中心、造作功能、無核心過程），工程軌據此產出了完整的介面規格（AuditContext、LoopQualityVector、Option C 雙通道、五層公式）。兩軌在蘊歸屬五原則和 WRITE/READ 區分上匯合——哲學判定提供了工程設計的語義基礎，工程設計驗證了哲學判定的可操作性。

Plan30 大約 290 行生產程式碼。不多。但這 290 行的每一行都有 17 項決議、14 份研究報告、三輪 Master 指示作為依據。

二十位研究者。十七項決議。零項否決。

---

*Cycle 02-6 完。*
