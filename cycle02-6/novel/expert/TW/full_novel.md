# 序章：從清創到精密工程

---

Cycle 02-5 是一次大規模清創手術。

二十位研究者在五天內做出 29 項決議，DC Master 覆議推翻其中兩項（D3-R3 四智映射、D4-R1 心所命名），整個團隊對七份設計文件進行去裝飾化重構——移除不具驅動力的佛學標籤、統一命名慣例、拆解錯誤的蘊歸屬映射。那五天像是對 codebase 進行 dead code elimination：不是增加功能，而是移除積累的語義債務。

Cycle 02-6 的調性截然不同。前一輪回答的是「什麼是錯的」；這一輪要回答的是「正確的規格長什麼樣」。

---

## 雙重輸入

DC Master 發出兩封信件，分別觸發工程軌和哲學軌。

**工程信件**指向 Plan29 交付後的六個 Open Questions（OQ-29-1 至 OQ-29-6）。Plan29（v0.29.0-alpha）新增了 `ILoopQualityMonitor`（迴路品質監控器介面）和 `IConfidenceAuditor`（信心度審計介面），但兩者都只有 SDK 骨架——Registry 已接入 `PluginHooks`，型別定義已 export，卻沒有預設實作、沒有計算公式、沒有與 `ManoAggregator` 的佈線。Master 要求研究團隊回答：品質怎麼算（OQ-1）？Layer 3 怎麼整合（OQ-2）？審計策略方向（OQ-3）？事件訂閱清單（OQ-4）？權重可配置性（OQ-5）？整體怎麼放進 Plan30（OQ-6）？

**哲學信件**直指行蘊（samskara-skandha）的定義問題。Master 明確批評唯識學派將 49 個心所歸入行蘊的做法「非常有問題」，並要求以原始經典（如是我聞）為第一手依據進行深掘。這不是一個裝飾性的研究方向，而是直接影響 `ISamskara` 介面未來拓展路徑的基礎判定。

---

## SUNYATA 的雙軌架構

研究總監 SUNYATA 據此設計了雙軌結構，並建立跨軌道優先權：

| 軌道 | 範疇 | 子項 | 團隊 |
|------|------|------|------|
| Track A | AuditContext 型別 + 審計日誌 | A1-A4 | VITRUVIUS, KERNEL, GUARDIAN, ARCHIMEDES, WIENER, BABBAGE |
| Track B | ILoopQualityMonitor 實作規格 | B1-B4 | WIENER, ATHENA, BABBAGE, HERACLITUS, TURING, PASCAL |
| Track C | 行蘊深掘 | C1-C4 | NAGARJUNA, ASANGA, LINNAEUS, PENROSE, PASCAL |
| Track D | 工程同步 | D1-D2 | TURING, ARCHIMEDES, VITRUVIUS, GUARDIAN |

跨軌道影響協議的關鍵規則：**哲學結論（D1）先於工程設計（D2/D3），確保蘊歸屬判定不被工程便利性覆蓋。** 若 C1-C4 的結論與 A/B 的設計假設產生衝突，工程軌必須等待哲學裁定。

R1 產出 14 份獨立研究報告。R2 交叉審閱發現 24 個共識點、僅 3 個分歧點。R3 三場辯論、245 分鐘、17 項決議、13 項全票（20/20）、0 項否決。

這是一輪精密工程。

---

# 第一章：行蘊的原典重建

---

## 1.1 方法論：如是我聞

哲學軌由 NAGARJUNA（中觀學派）和 ASANGA（唯識學派）共同領銜。Master 批評的正是唯識學派的做法，而 SUNYATA 刻意安排唯識專家參與自我批判——這不是懲罰性安排，而是方法論上的必要：只有深諳系統內部邏輯的人才能精確指出其斷裂點。

文獻層次嚴格區分：

| 層次 | 來源 | 地位 |
|------|------|------|
| 第一層 | 巴利五部（Nikaya）/ 漢譯阿含 | 唯一定義依據 |
| 第二層 | 十二因緣相關經文（SN 12） | 結構性參考 |
| 第三層 | 名色識架構（SN 12.2, MN 9） | 交叉驗證 |
| 排除 | 阿毘達磨論典（Vibhanga, Dhammasangani） | 僅作對比，不作歸屬依據 |

這個分層直接回應了 Master 的指示：論典是後世學者的系統化產物，不是佛陀的原話。

---

## 1.2 SN 22.56：六思身——行蘊的原始定義

蘊相應（Khandha-samyutta）的 SN 22.56（取蘊經）是五蘊定義的核心出處：

> 比丘們，什麼是行蘊（sankhara-kkhandha）？有六種思身（cha cetana-kaya）：色思、聲思、香思、味思、觸思、法思。比丘們，這就稱為行蘊。

經文分析：

| 巴利原文要素 | 內容 | OpenStarry 對應 |
|-------------|------|----------------|
| rupa-sancetana | 色思——對色塵的意圖 | 對 visual/text input 的反應意圖 |
| sadda-sancetana | 聲思——對聲塵的意圖 | 對 audio/event input 的反應意圖 |
| gandha-sancetana | 香思——對香塵的意圖 | 非 Agent 典型場景 |
| rasa-sancetana | 味思——對味塵的意圖 | 非 Agent 典型場景 |
| photthabba-sancetana | 觸思——對觸塵的意圖 | 對 API/tactile event 的反應意圖 |
| dhamma-sancetana | 法思——對法塵的意圖 | 對內部認知對象的反應意圖 |

關鍵洞見：**原始經典中行蘊的定義完全以 cetana（意圖/意志）為中心**——是六種針對感官對象的意圖形成，不是「受想以外的心理活動雜物箱」。

---

## 1.3 SN 22.79：造作一切有為法

> 比丘們，為什麼稱為行（sankhara）？因為它們造作（abhisankharonti）有為法（sankhatam）。造作什麼有為法？以色的形態造作色，以受的形態造作受，以想的形態造作想，以行的形態造作行，以識的形態造作識。

這段經文揭示了行蘊的第二個核心特質：**行蘊不僅造作行為，更造作所有五蘊的被條件化狀態**。在工程語境中，`ISamskara` 不應僅限於 `ITool.execute()` 這樣的外部工具呼叫，而應涵蓋「改變系統狀態的一切造作」——包括改變系統對未來輸入的反應模式。

這直接連結到 VasanaEngine 的長期路線圖（D-29-8）：過去的行為模式影響未來的齒輪選擇，正是「行蘊造作識蘊的被條件化狀態」的工程體現。

---

## 1.4 SN 22.95：芭蕉喻——無核心的動態過程

> 行如芭蕉（kadalupamo sankhara）——若人剝芭蕉幹，尋找堅實的核心，卻一層層剝盡，什麼也找不到。

這是行蘊第三個核心特質的經典表述：**無核心的動態過程**。行蘊不是一個固定的「東西」（entity），而是一個不斷運轉的「過程」（process）。

工程對應非常精確：`ISamskara` 的 plugin 應是輕量、可組合的（composable），不依賴持久性內部狀態。每個 plugin 都是一個「層」，剝開任何一層都不會找到不可替代的核心邏輯。這與 OpenStarry 的 Tenet #2（一切皆 Plugin）和微核心架構（Core 不包含業務邏輯）完美契合。

---

## 1.5 MN 44：三行分類的互補觀察角度

毘舍佉問法授比丘尼：

| 行 | 巴利名 | 定義 | 經文理由 |
|----|--------|------|---------|
| 身行 | kaya-sankhara | 入出息（呼吸） | 身法，繫縛於身 |
| 語行 | vaci-sankhara | 尋（vitakka）+ 伺（vicara） | 先尋伺後發語 |
| 心行 | citta-sankhara | 想（sanna）+ 受（vedana） | 心法，繫縛於心 |

這裡存在一個經典框架間的張力：citta-sankhara（心行）**包含** sanna（想）和 vedana（受），但在五蘊框架中這兩者是獨立的蘊。NAGARJUNA 的分析：**這不是邏輯矛盾，而是不同分類系統的不同觀察角度（drsti-bheda）**——三行分類觀察「什麼條件化什麼」，五蘊分類觀察「什麼是修行的關鍵觀察對象」。唯識學派試圖強制統一兩個系統，導致了 49 心所塞進行蘊的問題。

工程啟示：身行對應 `ITool.execute()`（物理層造作），語行對應尋伺（`vitakka-vicara`，認知初始處理），心行對應 `IVedana` + `ISamjna`（已覆蓋）。值得注意的是，`VitakkaWatchdog` 在 OpenStarry 中是穩定化監控機制，功能上更接近識蘊而非行蘊——這不是歸屬錯誤，而是 MN 44 的語行分類與五蘊分類本就是互補視角。

---

## 1.6 唯識心所系統的批判

ASANGA 親自主導了對唯識學派 51 心所系統的批判性分析（C2 報告）。唯識學派將 51 心所中的 49 個歸入行蘊——僅留「受」和「想」給受蘊和想蘊。逐條分析結果：

| 分類 | 數量 | 比例 | 說明 |
|------|------|------|------|
| 確屬行蘊 | 7 | 14% | chanda, virya, apramada, mraksa, matsarya, maya, sathya |
| 已有正確歸屬 | 12 | 24% | 已在 OpenStarry 中經辯論確認的 plugin |
| 可能屬他蘊 | 18 | 37% | 功能上更接近識蘊（判斷性）或受蘊（感受性） |
| 混合/待研究 | 14 | 28% | 跨蘊功能，需逐案分析 |

ASANGA 的結論：「心所列表的功能描述有參考價值，但其蘊歸屬分類已偏離原典的 cetana 中心定義。」這不是全面否定唯識學——而是在原典與論典之間做出了清晰的方法論區分。

---

## 1.7 三準則與核心區分

LINNAEUS 從原典分析中歸納出「行蘊屬性判定三準則」，作為永久性判定工具 [D1-R3, 20/20]：

1. **造作性**（Conditioning）：是否創造/改變/產生新狀態？
2. **意圖驅動**（Cetana-driven）：是否由意圖形成過程驅動？
3. **環境改變**（Environmental Shift）：是否改變後續認知條件？

三個問題全部為「是」→ 行蘊（samskara）；全部為「否」→ 識蘊（vijnana）；混合 → 需逐案分析，可能跨蘊。

PENROSE 將此進一步壓縮為一個程式設計者立即能理解的區分：

> **行蘊 = WRITE**（主動改變世界的狀態）
> **識蘊 = READ**（被動評估世界的狀態）

在 OpenStarry codebase 中的對應：

| 蘊歸屬 | 介面 | 操作類型 | 程式碼路徑 |
|--------|------|---------|-----------|
| 行蘊（WRITE） | `ITool` | 工具執行，改變環境 | `types/aggregates.ts#ISamskara` |
| 行蘊（WRITE） | `ISlashCommand` | 指令執行，改變狀態 | `types/aggregates.ts#ISamskara` |
| 識蘊（READ） | `IGuide` | 評估引導，不改變狀態 | `types/aggregates.ts#IVijnana` |
| 識蘊（READ） | `IVolition` | 審議判斷，不改變狀態 | `types/aggregates.ts#IVijnana` |

這個 WRITE/READ 區分被 D1-R5 全票確認（20/20），成為蘊歸屬判定的操作性原則。

---

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

---

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

---

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

---

# 第五章：Master 的心所指示與永久性規則

---

## 5.1 觸發：心所分析的連鎖反應

哲學軌的 C2 報告（唯識學派心所批判）在 R2 交叉審閱時被呈給 DC Master。ASANGA 整理了 51 心所的逐條重新歸屬建議——其中 18 項（37%）被認為功能上更接近識蘊或受蘊，而非行蘊。

Master 的回應不是單次裁定，而是三輪漸進精化。每一輪的焦點更加銳利。

---

## 5.2 第一輪：經典與論典的方法論劃界

Master 的核心主張：**心所（cetasika）是論典（阿毘達磨）的系統化產物，不是原始佛經（sutta/agama）的內容。**

這不是學術偏見。佛陀在原始經典中說了五蘊、十二因緣、八正道、三十七道品。「51 心所」這個分類系統是後世學者（特別是無著、世親等唯識論師）的系統化整理。原典中確實出現了許多心所的名稱（如慧、精進、慚、愧），但**將它們組織為固定數量的分類系統並指定蘊歸屬**是論典的工作。

Master 的直接結論：**Plugin 的命名不能使用心所的梵文名字。**

工程影響：任何以梵文心所名命名的 plugin（如 VīryaPlugin、PrajnaPlugin）必須改為工程術語。

---

## 5.3 第二輪：功能參考的保留

第一輪容易被誤讀為「心所完全無用」。Master 在第二輪中修正了這個印象：心所的**功能描述**有參考價值。

例如，心所「精進」（vīrya）描述了「持續不懈地投入善法」的功能。可以參考這個功能描述來設計一個 Plugin——但 Plugin 不能叫 VīryaPlugin，而應使用工程名稱（如 `PersistencePlugin`、`RetryPlugin`）。

Master 的精確表述：「可以說『參考精進的涵義，設計了重試 Plugin』。但不能說『重試 Plugin = 精進』。」

這是「可援引、不可等同」的原則。

---

## 5.4 第三輪：命名解耦帶來歸屬自由

第三輪是最深刻的。Master 說：「Plugin 不等於心所。」

表面上這很簡單。但含義是結構性的。

在唯識學派中，每個心所有固定的蘊歸屬——「精進」屬行蘊，「慧」屬識蘊。如果 Plugin = 心所，那 Plugin 的蘊歸屬也被鎖死。但 Plugin != 心所。一個 Plugin 可能同時有行蘊和識蘊的功能——它既做判斷（READ），又執行動作（WRITE）。

在心所系統中這是不允許的（每個心所歸屬唯一蘊），但在 Plugin 系統中完全合法。**命名解耦帶來歸屬自由**——不用心所名字命名 Plugin，反而讓 Plugin 擺脫了論典的固定分類束縛，可以自然地跨越多個蘊。

---

## 5.5 八點永久性規則

三輪指示被整理成八條永久規則，與蘊歸屬五原則共同構成所有未來命名和歸屬問題的判定基準：

| # | 規則 | 工程影響 |
|---|------|---------|
| 1 | 心所是論典產物，非原始經典內容 | 不以心所系統作為架構設計的預設框架 |
| 2 | 心所功能有參考價值，可作 plugin 設計靈感 | 設計文件可引用心所的功能描述 |
| 3 | 可說明「參考某心所涵義，設計某 plugin」 | 設計溯源合法，等同宣稱非法 |
| 4 | Plugin 使用工程術語命名，不得用心所梵文名 | 命名慣例硬規則 |
| 5 | 梵文術語限於原始經典者——五蘊(skandha)、觸(sparsha) 可用 | 區分經典梵文 vs 論典梵文 |
| 6 | 心所分類不作為蘊歸屬依據 | 「唯識說 X 屬行蘊」不能作為 plugin 歸屬證據 |
| 7 | 既有 plugin 歸屬決議不受影響 | 已確認的歸屬不因新規則翻案 |
| 8 | Plugin != 心所，蘊歸屬可自然跨多蘊 | 跨蘊 plugin 是合法的、預期的 |

---

## 5.6 蘊歸屬五原則 [D1-R6, 20/20]

與八點規則互補，五原則提供了正面的判定方法：

1. **功能分析為蘊歸屬的唯一依據**——不是名稱、不是傳統、不是論典
2. **唯識 51 心所系統作為功能參考清單，不作歸屬依據**
3. **梵文術語用於程式碼命名時，僅限源自原始經典者**
4. **Plugin 不等於心所，蘊歸屬可自然跨越多蘊**
5. **既有歸屬決議（基於功能分析）繼續有效**

這五條原則加上八點規則，形成了一套完整的判定框架。未來每次有人問「這個功能屬於哪個蘊」或「這個 plugin 該叫什麼名字」，不再需要從頭辯論——直接對照這 13 條規則即可。

---

## 5.7 D1 議程的連鎖修訂

Master 的三輪指示直接導致了 D1 辯論議程的修訂：

- **D1-Q2（心所多蘊歸屬問題）被刪除**——心所分類既然不作為依據，討論其多蘊歸屬就失去意義
- **D1-Q6（逐條投票 26 項心所）被簡化**——改為投票蘊歸屬原則本身，而非逐條判定
- **manasikara 追加議題被取消**——`CoarisingBundle` 中 manasikara 不是獨立介面，無需額外討論

這些修訂節省了至少 45 分鐘的辯論時間，同時提高了決議的抽象層次——從個案判定上升到原則確立。

---

## 5.8 心智論述工程借鑒評估 [D1-R4a/b/c]

C4 報告（PASCAL + PENROSE）對所有佛學心智論述的工程借鑒價值做了系統性評估：

| 論述 | 結論 | 決議 | 測試結果 |
|------|------|------|---------|
| 五蘊 | 已完成融入 | 無需行動 | -- |
| 名色識 | 核心價值已吸收 | 無需行動 | -- |
| 十二因緣 | 解釋性附錄 | 02-7 P2 [D1-R4a, 19/20] | -- |
| 八識 | 待多 Agent 場景 | Cycle 03+ | -- |
| **四智** | **排除** | **D1-R4b, 18/20** | 四項測試全失敗 |
| 認知序列 | 最強結構對應 | 02-7 P2 [D1-R4a, 19/20] | -- |

四智（大圓鏡智、平等性智、妙觀察智、成所作智）的排除尤為重要。四項排除測試：

1. **移除測試**：移除四智映射是否改變任何設計？ → 否
2. **程式碼存在測試**：四智在 codebase 中有對應嗎？ → 否
3. **驅動力測試**：四智驅動了任何工程決策嗎？ → 否
4. **不可替代測試**：是否有更簡單的工程概念可替代？ → 是

2 票反對認為可保留做參考文件。但四項測試全部失敗——保留只會增加認知負擔而不增加設計價值。

---

## 5.9 ISamskara 拓展方向 [D1-R3, 20/20]

確認 Cycle 02-5 D3-R4 決議：目前不新增 ISamskara 子介面。四個方向存檔為長期候選：

| 方向 | 描述 | 優先級 | 時程 |
|------|------|--------|------|
| A: cetana-formation | 意圖規劃——從「執行工具」擴展到「形成意圖」 | P2 | Cycle 03+ |
| B: vasana-imprinting | 習氣形成——行為模式的學習與記憶 | P2 | 長期（VasanaEngine） |
| C: kaya extension | 環境轉換——身行的擴展 | P3 | 無需排程 |
| D: vaci | 溝通形成——語行的擴展 | P3 | 無需排程 |

方向 A 和 B 與原典分析直接相關：cetana-formation 對應 SN 22.56 的六思身（意圖形成過程），vasana-imprinting 對應 SN 22.79 的「造作一切有為法」（行為塑造未來條件）。方向 B 的 VasanaEngine 已在 D-29-8 中排程為長期路線圖。

NAGARJUNA 的總結：「上一輪我們學會了什麼不該做。這一輪我們學會了為什麼不該做。」

---

# 第六章：三場辯論——從分歧到共識的精確路徑

---

## 6.1 R2 分歧識別

R2 交叉審閱識別了 24 個共識點和 3 個分歧點。四組跨軌道交叉對照全部確認無衝突——哲學軌的結論不影響工程軌的任何設計假設：

| 對照 | 結果 |
|------|------|
| C2 心所批判 → A1 AuditContext | 4/4 無影響 |
| C4 工程借鑒 → D2 Plan30 | 4/4 無影響 |
| C3 ISamskara 拓展 → B1 公式 | 5/5 無影響 |
| C2 心所批判 → 蘊歸屬清單 | 11 確認 / 0 修正 / 1 待辯 / 14 未來 |

三項分歧全部屬於工程軌內部：

1. **extras 寫入協議**：A2 提出通用事件模式 vs B3 提出直接訂閱 → D2 解決
2. **extras key 命名**：`loopQuality:score` vs `loopQuality:composite` → D2 統一為 `loopQuality:composite`
3. **loopQualityFn 數據來源**：L3 回調 vs extras 快取是否同源 → D3 解決（雙通道：pull + push）

---

## 6.2 D1：行蘊深掘（約 75 分鐘，7 項決議）

| 決議 | 內容 | 票數 | 關鍵論點 |
|------|------|------|---------|
| D1-R1 | 行蘊核心定義：cetana 中心、造作功能、無核心過程 | 20/20 | 直接引用 SN 22.56/79/95，無模糊空間 |
| D1-R3 | ISamskara 不新增子介面；三準則為永久工具 | 20/20 | 確認 02-5 D3-R4，A/B 方向存檔 |
| D1-R4a | 認知序列 appendix 排程 02-7 P2 | 19/20 | 1 票反對認為可在本輪完成 |
| D1-R4b | 四智正式排除 | 18/20 | 2 票反對認為可保留參考；四項測試全失敗 |
| D1-R4c | C4 綜合評估表確認 | 20/20 | -- |
| D1-R5 | 「活動與轉換」原則；行=WRITE 識=READ | 20/20 | PENROSE 的 WRITE/READ 區分 |
| D1-R6 | 蘊歸屬 5 項永久性原則 | 20/20 | 永久基準線，非單輪決議 |

D1 是三場辯論中共識最高的——5 項全票。原因在於哲學軌的結論直接基於原始經典引用，不涉及工程取捨（trade-off）的判斷，因此分歧空間極小。

D1 結論對 D2/D3 均無需追加議題——跨軌道影響協議中的「先哲學後工程」規則在此輪驗證為零衝突。

---

## 6.3 D2：AuditContext（約 85 分鐘，5 項決議）

| 決議 | 內容 | 票數 | 關鍵論點 |
|------|------|------|---------|
| D2-R1 | AuditContext 完整型別（sparshEvent required, history 預設 10 可配置） | 20/20 | A1-OQ1/2/3 全部解決 |
| D2-R2 | extras bag 協議（雙事件 + SDK helper, 淺凍結, max 32 keys） | 19/20 | MESH 反對雙事件複雜度；多數支持通用性 |
| D2-R3 | ConfidenceAuditLog（GUARDIAN D5 義務兌現） | 20/20 | GUARDIAN 當場確認清帳 |
| D2-R4 | Layer 整合方案 C（L2→confidence, L3→threshold, alpha=0.10） | 20/20 | WIENER/BABBAGE 穩定性分析決定性 |
| D2-R5 | Auditor 策略三階段：Phase 0 PassthroughAuditor | 20/20 | -- |

D2-R4 的投票過程值得注意：WIENER 和 BABBAGE 的穩定性分析（Option A/B/C 的 Lyapunov 比較）在 R1 報告中已呈現。R2 交叉審閱時無人對分析提出質疑。到了 D2 辯論，全票通過——數學證明的說服力是確定性的。

R2 的三項分歧在 D2 中全部解決：
- extras 寫入 → 統一為雙事件 + SDK helper（D2-R2）
- key 命名 → 統一為 `loopQuality:composite`（D2-R2 附帶決議）
- loopQualityFn 數據來源 → 移至 D3 處理

---

## 6.4 D3：LoopQualityMonitor（約 85 分鐘，5 項決議）

| 決議 | 內容 | 票數 | 關鍵論點 |
|------|------|------|---------|
| D3-R1 | 4 維公式確認（C/E/Conv/S; W=10, warmup=5, Q_default=0.5） | 20/20 | OQ-29-1 正式回答 |
| D3-R2 | EventBus 訂閱：6 events Phase 1; AgentEventType 常量提升 | 20/20 | OQ-29-4 正式回答 |
| D3-R3 | extras 寫入：D2-R2 管道 + loopQualityFn 雙通道; per-route lifecycle | 20/20 | 解決 R2 第三項分歧 |
| D3-R4 | 權重 Phase 1 固定 balanced 0.25x4 | 20/20 | PASCAL 最大熵論證 |
| D3-R5 | Plan30 = Monitor + L3 + 型別定義; Plan31 = Auditor + Audit Trail | 19+1 條件 | GUARDIAN 條件贊成 |

D3-R5 是唯一一項有條件贊成的決議。GUARDIAN 的條件：**Plan30 的 Wave 3 必須包含 `ConfidenceAuditLog` 的 SDK 型別定義，不能拖到 Plan31。** 理由：日誌型別是 D5 讓步條件的核心交付物，延遲等於債務延期。條件被接納，GUARDIAN 轉為贊成。

---

## 6.5 Auditor 策略三階段 [D2-R5, 20/20]

| Phase | 對應 Plan | 實作 | 描述 |
|-------|----------|------|------|
| Phase 0 | Plan30（W4, 可選） | PassthroughAuditor | delta=0, 純日誌；驗證管道端對端通暢 |
| Phase 1 | Plan31 | ThresholdAuditor | 規則式：低信心度偵測、loopQuality 異常、趨勢偵測 |
| Phase 2 | 長期 | LLM-assisted | LLM 輔助審計 |

Phase 0 的 PassthroughAuditor 看似無用——一個什麼都不調整的審計員。但 ARCHIMEDES 的工程洞見：「它的價值不在審計，在測試。它驗證 AuditContext 組裝、extras 收集、audit delta clamping、ConfidenceAuditLog 發出——整個管道端對端通暢。就像裝好水管後先開水龍頭。」

所有 Phase 必須遵守 WIENER C-1/C-2/C-3 約束——這不是 Phase 0 的特殊要求，而是永久性約束。

---

## 6.6 統計比較

| 指標 | Cycle 02-5 | Cycle 02-6 |
|------|-----------|-----------|
| 決議數 | 29 | 17 |
| 否決 | 0 | 0 |
| 全票（20/20） | ~20（69%） | 13（76%） |
| 師父覆議 | 2 | 0 |
| 辯論場次 | 5 | 3 |
| R1 報告數 | -- | 14 |
| R2 共識點 | -- | 24 |
| R2 分歧點 | -- | 3 |

DARWIN 的觀察：「02-5 是正確性辯論——什麼是對的、什麼是錯的。02-6 是規格辯論——對的東西長什麼樣子。後者天然更容易達成共識，因為不涉及價值判斷。」

SUNYATA 的分析：「R1 做得好。14 份報告覆蓋了所有問題空間。R2 只發現 3 個分歧。當大部分問題在辯論前就有共識，辯論就變成了確認和精化。」

零師父覆議的原因：八點規則在 R2 階段就已確立（Master 三輪精化），D1-D3 的所有決議都在八點規則的框架內運作。沒有決議試圖挑戰框架本身。

---

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
