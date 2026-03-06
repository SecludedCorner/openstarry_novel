# 第五章：名字的代價——D4 命名修正辯論

---

**時長**：~30 分鐘 | **觸發**：Master 審閱 | **投票**：3 項

D4 不在原始議程中。它由 Master 的一句話觸發：

> **「用梵文就需要對他的定義負責。你覺得 Sati 的內容完全 match 嗎？」**

## NAGARJUNA 的歸謬論證

```
前提 A：Sati = 行蘊心所（佛學定義）
前提 B：SatiMonitor ≠ 行蘊（D2-R2 結論）
∴ SatiMonitor ≠ Sati
```

如果正念在佛學中必然是行蘊，而 D2 已經證明 SatiMonitor 不是行蘊——那 SatiMonitor 就不是正念。一個不是正念的元件，不應該叫 Sati。

ASANGA 確認：「如果 SatiMonitor 不是行蘊活動，那它就不是 Sati。我們自己的分類分析否定了我們自己的命名。」

## ISatiMonitor → ILoopQualityMonitor（D4-R1：13/20）

ARCHIMEDES 的提案勝出：「Loop Quality Monitor」——認知迴路的品質監控器——精確描述功能，無佛學，無隱喻。

少數意見：IBehaviorQualityMonitor（GUARDIAN，4 票）、ICognitiveLoopMonitor（NAGARJUNA + ASANGA，2 票）、IQualityMonitor（SYNTHESIST，1 票）。

完整更名表：ISatiMonitor → ILoopQualityMonitor、SatiQualityVector → LoopQualityVector 等 8 項。

## IPrajna → IConfidenceAuditor（D4-R2：16/20）

NAGARJUNA：「般若是佛學中最高的認知能力——照見一切法實相的智慧。」

ASANGA：「把一個溫度微調旋鈕叫做核融合反應爐。」

IPrajna 的實際功能：一個方法，輸入信心度，輸出 `{ delta: number, reasoning: string }`，delta 限制在 [-0.05, +0.05]。這是審計——不是般若。

BABBAGE：IConfidenceAuditor 語義最精確——獨立的、有限範圍的、產生書面記錄的二次檢查。

少數意見：IThresholdCalibrator（WIENER，2 票）、ISecondaryEvaluator（HERACLITUS + PENROSE，2 票）。

## Doc 03 重新投票（D4-R3：17/20）

「Sila-Prajna Security Framework」→「Plugin Security Lifecycle」

初始投票 14/20 保留不變。Master 審閱觸發重新檢驗——四項測試全部不通過：必要性（不需要種子理論理解 plugin 生命週期）、程式碼識別（實際類型用英文）、決策驅動（無 DC 確認）、定義責任（戒 ≠ 存取控制，般若 ≠ CVE 撤銷）。

ASANGA 的關鍵區分：Doc 16 = 獨立映射文件（Master 裁定保留）vs Doc 03 = 工程文件中的佛學裝飾（應清理）。

## 第四項測試——定義責任（永久性標準）

> **「當使用佛學梵文術語作為程式碼識別符時，該組件的功能必須匹配該術語的佛學定義。如果不一致，使用工程術語。」**

補充 D1 的三項測試——即使名字通過 Test 2（程式碼識別），如果不通過 Test 4（定義責任），仍應更名。

影響範圍：ILoopQualityMonitor 影響 6 份文件 100+ 處替換；IConfidenceAuditor 影響 5 份文件；Doc 03 重命名 + 內容清理。

---
