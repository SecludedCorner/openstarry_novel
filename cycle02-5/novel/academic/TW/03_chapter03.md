# 第三章：三面之鏡——D2 Sati Plugin 蘊歸屬辯論

---

**時長**：~60 分鐘 | **主席**：SUNYATA | **投票**：3 項

## 更名策略（D2-R1：19/20）

保留 `Sati` 程式碼識別符，文件標題從「Mindfulness Architecture」改為「Cognitive Loop Quality Monitoring Architecture」。加入「命名說明」段落。安全文件使用全名。

唯一反對票：GUARDIAN——偏好完全更名以消除文化背景知識需求。接受多數決議附帶安全文件全名條件。

## 五蘊組成（D2-R2：18/20）——核心決議

**結論：skandha: ['vedana', 'samjna', 'vijnana']**

四個功能到三蘊的映射：

| 功能 | Skandha | 說明 |
|------|---------|------|
| EventBus 事件訂閱（11 種，持續感知） | vedana | 接收認知迴路信號 |
| 滑動窗口 + 模式辨認 | samjna | 從事件流中辨認行為模式 |
| LoopQualityVector + SPC 異常判斷 | vijnana | 超越描述性辨認的評價性品質判斷 |
| **不執行工具、不修改狀態** | **排除 samskara** | 不是正念修行 |

關鍵論證轉折：

- **ASANGA**：佛學正念（smṛti）是行蘊心所——主動的、有意志的、道德正向的。SatiMonitor 是被動的、自動的、價值中立的。因此 SatiMonitor 不是正念，不應歸為行蘊。
- **LINNAEUS**：OOP 比較——「IGearArbiter 是『被呼叫來看一下』；SatiMonitor 是『一直在看』。」持續訂閱 vs 按需調用——足以構成獨立的 vedana 宣告。
- **ARCHIMEDES**（轉折點）：三蘊和二蘊的工程成本差異為零——PluginManifest 的 skandha 欄位已支持多值。消除「三蘊太複雜」的顧慮後，討論轉為純分類精度，Proposal B 的優勢壓倒性。
- **少數意見**（MESH、KERNEL）：Proposal C ['samjna','vijnana'] 與 IGearArbiter 分類對稱，有長期維護價值。

**歷史意義**：SatiMonitor 成為 OpenStarry 第一個三蘊 plugin。

## PluginHooks 專屬槽位（D2-R3：20/20）

新增 `monitors?: ISatiMonitor[]` 專屬槽位。遵循 Cycle 02-4 的 `arbiters` 先例（SDK 介面 → PluginHooks → Registry → PluginLoader 四步模式）。

---
