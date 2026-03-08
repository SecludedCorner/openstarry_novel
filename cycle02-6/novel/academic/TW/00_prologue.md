# 序章：從清理到建構 —— Cycle 02-6 的方法論定位

---

## 研究脈絡與前輪遺產

Cycle 02-5 構成了 OpenStarry 研究史上規模最大的一次規範性修正：29 項決議、2 項 Master 覆議推翻、7 份設計文件重組。核心成果在於系統性移除裝飾性佛學映射（decorative Buddhist mappings），確立「功能分析優先於術語傳統」的方法論立場。

Cycle 02-6 承接此遺產，但研究性質根本轉變。若 02-5 的主題是「否定性判斷」（什麼是錯的），02-6 則是「肯定性建構」（什麼是對的，以及對的東西應具備怎樣的精確規格）。

---

## 雙重研究委託

**工程指示**：針對 Plan29 交付（v0.29.0-alpha）中 `IConfidenceAuditor` 與 `ILoopQualityMonitor` 兩個骨架元件，Master 要求回答六個開放問題（OQ-29-1~6）：AuditContext 欄位、extras bag 協議、審計日誌格式、品質公式與事件訂閱、Layer 2/3 整合方案、Plan30 方向。

**哲學指示**：以原始經典（如是我聞）為第一手依據重新深掘行蘊（samskara-skandha）。Master 指出唯識學派將大部分心所歸入行蘊的做法「非常有問題」，並提示「活動與轉換」觀念可拓展行蘊子類別。

---

## 研究設計：雙軌結構與跨軌道約束

SUNYATA（#0）設計四軌道結構：

| 軌道 | 範圍 | 子項 | 規模 |
|------|------|------|------|
| Track A | AuditContext + 審計日誌 | A1-A4 | 4 組 |
| Track B | ILoopQualityMonitor 規格 | B1-B4 | 4 組 |
| Track C | 行蘊哲學深掘 | C1-C4 | 4 組 |
| Track D | 工程同步 + Plan30 | D1-D2 | 2 組 |

關鍵約束：**跨軌道影響協議** —— D1（哲學辯論）必須先於 D2/D3（工程辯論），確保哲學發現即時注入工程設計。

---

## 研究流程概覽

```
R0 定向 → R1 獨立研究（14 份報告） → R2 交叉審閱 → R3 辯論（3 場 / 17 決議） → R4 成果定稿
```

R1 階段產出 14 份獨立研究報告，團隊分配如下：

| 報告 | 主題 | 主持 |
|------|------|------|
| A1 | AuditContext 型別定義 | VITRUVIUS + KERNEL |
| A2 | extras bag 機制 | DARWIN + MESH |
| A3 | 審計日誌規格 | GUARDIAN + ARCHIMEDES |
| A4 | Layer 2/3 整合路徑 | WIENER + BABBAGE |
| B1 | 四維計算公式 | WIENER + ATHENA + BABBAGE |
| B2 | EventBus 事件規格 | HERACLITUS + TURING |
| B3 | extras 寫入整合 | LEIBNIZ + MESH |
| B4 | 權重與配置 | PASCAL + ATHENA |
| C1 | 原始經典中的行蘊 | NAGARJUNA + ASANGA |
| C2 | 唯識心所批判 | ASANGA + NAGARJUNA |
| C3 | ISamskara 拓展方向 | LINNAEUS + PENROSE |
| C4 | 心智論述工程借鑒 | PASCAL + PENROSE |
| D1 | v0.29.0-alpha 程式碼驗證 | TURING + ARCHIMEDES |
| D2 | Plan30 方向建議 | VITRUVIUS + GUARDIAN |

R2 識別 24 個共識點、3 個分歧點（extras 寫入協議、extras key 命名、loopQualityFn 數據來源）。R3 合計 ~245 分鐘，17 項決議中 13 項全票通過（20/20），0 項否決，0 項 Master 覆議。

以下各章依序展開：哲學軌的行蘊深掘（第一章）、審計上下文設計（第二章）、品質監控公式（第三章）、整合架構（第四章）、Master 心所指示（第五章）、辯論方法論分析（第六章）、工程藍圖與總結（第七章）。

---
