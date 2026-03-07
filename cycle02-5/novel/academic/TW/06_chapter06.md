# 第六章：D5——純粹的工程

---

## 十位辯論者

D5 只有十位參與者。

不是排除——是精選。SUNYATA 判斷 D5 是純工程問題，邀請了與 Plan29 最相關的十位：VITRUVIUS（介面設計）、ATHENA（LLM 語義）、DARWIN（設計模式）、KERNEL（Registry 生命週期）、GUARDIAN（安全邊界）、WIENER（品質向量權重）、LINNAEUS（蘊歸屬推斷）、ARCHIMEDES（工程實踐）、TURING（原始碼分析）、PASCAL（介面語義精度）。

十個人。零位佛學家。

NAGARJUNA 和 ASANGA 自願退出。NAGARJUNA 的臨別語：「D4 證明了名字需要對定義負責。D5 會證明工程設計不需要佛學名字也能完成。這兩件事同樣重要。」

---

## 程式碼考古學

TURING 為 D5 準備了一份前所未有的報告——對 v0.28.0-alpha 中 14 個原始碼文件的全面分析。所有 Registry 的生命週期、timeout 模式、同步/非同步模式、失敗處理策略。

他把它叫做「程式碼考古學」。

這份報告改變了辯論的質地。之前的辯論——D1 到 D4——建立在原則和框架之上。但 TURING 的報告建立在事實之上。事實縮小了分歧的空間。你可以對一個原則有不同的解讀。你不能對一個 timeout 數值有不同的解讀。

---

## 九項投票

D5 是 Cycle 02-5 中投票最多的辯論——九項。但也是最快的——七十五分鐘，平均每項不到九分鐘。

**D5-R1：獨立 auditor slot。** IConfidenceAuditor 是否和 monitors 共用槽位？GUARDIAN 的論點：Monitors 是純觀察者（無副作用），Auditor 有 LLM 副作用。把觀察者和有副作用的組件放同一個 Registry，模糊安全邊界。**8/8。**

**D5-R2：audit() 回傳類型。** D5 最接近的投票。純非同步 vs 雙模式（`ConfidenceAuditResult | Promise<ConfidenceAuditResult>`）。GUARDIAN/KERNEL/VITRUVIUS 支持純非同步（語義精確），ATHENA/DARWIN 支持雙模式（遵循 IGearArbiter 先例）。TURING 提供事實：v0.28.0-alpha 中 IGearArbiter 和 IVolition 都使用雙模式——偏離現有模式需要充分理由。**5/8 雙模式通過。** 一致性勝過語義精確性。

**D5-R3：timeout 200ms + fail-safe。** TURING 分析了現有 timeout 模式——IGearArbiter chain deadline 200ms。audit() 應匹配。timeout 時 `{ delta: 0 }`——不修正。**8/8。**

**D5-R4：單一 auditor（last-wins）。** 多個 IConfidenceAuditor 的處理方式？ATHENA 提出 YAGNI：v1 最多一個。ARCHIMEDES 支持：遵循 IVolition 先例——單數，最後載入者勝出。**6/8。** TURING 和 VITRUVIUS 的少數意見（陣列更靈活）被記錄。

**D5-R5：失敗處理。** 異常時 fail-safe + log。遵循 IGearArbiter 和 SafetyMonitor 的現有模式。共識直接達成，不需投票。

**D5-R6：MonitorRegistry 啟動時機。** `MonitorRegistry.startAll(bus)` 在 `ExecutionLoop.onLoopStart()` 啟動。遵循 SafetyMonitor 的先例。**7/8。**

**D5-R7：LoopQualityVector 均等權重。** 四維品質向量（Continuity, Granularity, Speed, Equanimity），每個 0.25。WIENER 從控制理論角度：「沒有運行數據時，等權重是最保守的選擇。」**8/8。**

**D5-R8：validatePluginSkandha() 維持 warning-only。** skandha 是 metadata（D3-R3），宣告不一致不影響功能。**7/8。**

**D5-R9：IConfidenceAuditor extends IVijnana。** 單蘊（vijnana），強繼承。與 IVolition 和 IKlesha 一致。**8/8。**

---

## 介面定稿

九項投票完成後，TURING 在白板上寫下了最終規格：

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

「100%，」他說。

Master 要求的是規格達到 100%。現在達到了。每一個需要決定的細節都有了明確答案——介面名稱、方法簽名、回傳類型、timeout、fail-safe、多 auditor 策略、Registry 時機、權重、驗證模式、蘊歸屬。

不是概念設計。是可以直接交給工程團隊實作的完整規格。

---

## 零佛學

SCRIBE 統計了 D5 全場辯論中佛學術語被使用的次數。

零。

不是故意避開——是自然的結果。九項投票的每一項都在討論 TypeScript 介面設計、timeout 數值、Registry 模式、fail-safe 策略。沒有一項需要佛學分析。

D5 是本專案歷史上第一場完全沒有佛學內容的辯論。

NAGARJUNA 在辯論結束後走到 TURING 面前：「D4 證明了名字需要對定義負責。D5 證明了——有些工程問題根本不需要定義。只需要規格。」

天平的兩面。一面問：名字配得上定義嗎？另一面問：規格足夠精確嗎？D4 校準了第一面。D5 完成了第二面。

---
