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
