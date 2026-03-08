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
