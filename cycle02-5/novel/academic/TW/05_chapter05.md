# 第五章：D4——名字的代價

---

## 歸謬

SUNYATA 把 Master 的那句話打在投影幕上。大字。白底黑字。

> **「用梵文就需要對他的定義負責。你覺得 Sati 的內容完全 match 嗎？它歸在哪一蘊？」**

NAGARJUNA 站了起來。這一次他不是在承認錯誤——他是在完成一個推論。

「D2 已經確定了 SatiMonitor 的蘊歸屬。結論是 [vedana, samjna, vijnana]。三蘊。不包含行蘊。」

他在白板上寫了兩行字：

```
前提 A：Sati = 行蘊心所（佛學定義）
前提 B：SatiMonitor ≠ 行蘊（D2-R2 結論）
∴ SatiMonitor ≠ Sati
```

「Sati——巴利文的正念——在佛學傳統中是行蘊的心所。它是有意志的、主動的、道德正向的修行活動。如果正念必然是行蘊的心所，而 SatiMonitor 不是行蘊——那麼 SatiMonitor 就不是正念。」

他放下筆。

「一個不是正念的東西，為什麼叫 Sati？」

沉默。不是不同意的沉默。是所有人同時理解了一件他們應該更早理解的事情。

---

## 五個不一致

ASANGA 用功能分析確認了歸謬的結論：

| 維度 | 佛學正念（Sati/Smṛti） | SatiMonitor |
|------|----------------------|-------------|
| 主動性 | 主動（精進） | 被動（event-driven） |
| 道德性 | 道德正向 | 價值中立 |
| 意志性 | 需要意圖 | 自動運行 |
| 傳統歸屬 | 行蘊心所 | 受+想+識 |
| 修行地位 | 八正道第七支 | 品質監控器 |

五個維度。五個不一致。

「我們犯了一個命名錯誤，」ASANGA 說。「不是分類的錯誤——分類是正確的。是命名的慣性。我們在 Cycle 02-4 沿用了 ISatiMonitor 這個名字，因為它已經被使用了上百次。慣性讓我們對名字本身失去了批判性。」

---

## 四個提案

「那它應該叫什麼？」SUNYATA 問。

| 提案者 | 名字 | 理由 |
|--------|------|------|
| ARCHIMEDES | ILoopQualityMonitor | 精確描述功能：認知迴路品質監控器 |
| GUARDIAN | IBehaviorQualityMonitor | 側重行為層面 |
| NAGARJUNA + ASANGA | ICognitiveLoopMonitor | 強調認知迴路完整性 |
| SYNTHESIST | IQualityMonitor | 最簡功能描述 |

ARCHIMEDES 的論點最直接：「一個新來的工程師看到 ILoopQualityMonitor 就知道這個介面做什麼——監控迴路品質。沒有佛學。沒有隱喻。沒有歷史包袱。」

TURING 用原始碼事實支持 ARCHIMEDES：SatiMonitor 的 11 種事件訂閱覆蓋了整個認知迴路，不僅僅是行為階段。「Loop」比「Behavior」更準確。

**D4-R1：ISatiMonitor → ILoopQualityMonitor。13/20。**

不是全票。但多數明確。

---

## 核融合反應爐

然後 SUNYATA 說了兩個字：「IPrajna。」

NAGARJUNA 閉上眼睛，片刻後開始說話。

「般若——prajñā——是佛學中最高的認知能力。照見一切法實相的智慧。不是普通的聰明。不是分析能力。般若是超越性的——它是空性的直觀，是二千五百年來整個大乘佛學體系的核心認知目標。」

他在白板上寫了兩行：

```
般若（佛學）：照見一切法實相的最高智慧
IPrajna（工程）：對信心度加減 0.05 的函數
```

ASANGA 說了一句後來被所有人記住的話：

「這就像把一個溫度微調旋鈕叫做『核融合反應爐』。」

沒有人笑。因為他不是在開玩笑——他是在用精確的類比說明精確的問題。

IPrajna 的介面：一個方法，輸入信心度和上下文，輸出 `{ delta: number, reasoning: string }`，delta 被限制在 [-0.05, +0.05]。這是一個夾鉗。一個微調器。

PASCAL 從決策理論的角度確認：「IPrajna 做的是 bounded secondary evaluation。輸入一階信心度，輸出二階修正量，有硬限 ±0.05。這是審計。不是般若。」

BABBAGE 分析了替代名稱的語義精度：「IConfidenceAuditor 最精確。Audit——審計——精確描述了這個操作：對已有判斷進行有限範圍的二次評估。」

**D4-R2：IPrajna → IConfidenceAuditor。16/20。**

比 D4-R1 更高的共識。少數意見：WIENER 偏好 IThresholdCalibrator（兩票），HERACLITUS 和 PENROSE 偏好 ISecondaryEvaluator（兩票）。BABBAGE 反駁了兩者——Calibrator 暗示調整系統本身，Evaluator 太通用。

---

## 第四項測試

D4 沒有在兩次更名後結束。

Master 的審閱還提到了 Doc 03——`Sila_Prajna_Security_Framework.md`。

SUNYATA 在白板上列出了現有的三項測試，然後在旁邊加了一項新的：

```
Test 1（必要性）：移除是否改變工程規格？
Test 2（程式碼識別）：是否在原始碼中使用？
Test 3（決策驅動）：是否驅動了 DC 確認的設計決策？
Test 4（定義責任）：使用梵文術語時，組件功能是否匹配該術語的佛學定義？
```

第四項測試不是從天而降的——它是從 D4-R1 和 D4-R2 的討論中結晶出來的。ISatiMonitor 通過了 Test 2（在原始碼中），但不通過 Test 4（名字和功能不一致）。三項測試無法捕捉到這個維度。第四項測試填補了缺口。

NAGARJUNA 對 Doc 03 逐項測試：

- **Test 1**：Plugin 生命週期不需要種子理論就能理解。❌
- **Test 2**：原始碼中的類型是英文（'active' | 'dormant' | 'suspended'...），Sila/Prajna 只在註釋中出現。❌
- **Test 3**：沒有 DC 確認。❌
- **Test 4**：Sila（戒律）≠ 存取控制。Prajna（般若）≠ CVE 撤銷。❌

四項不通過。

ASANGA 做了一個關鍵區分：「Doc 16 是佛學映射文件——Master 裁定保留。Doc 03 是工程文件中嵌入了佛學裝飾——應該清理。同樣的佛學內容，不同的文件類型，不同的判斷。」

**D4-R3：Doc 03 重新投票，「Sila-Prajna Security Framework」→「Plugin Security Lifecycle」。17/20。**

---

## 方向相反

D4 結束。三十分鐘。三個名字被改掉。一項永久性測試被建立。

SUNYATA 站在白板前，看著四項測試。前三項問的是「佛學概念對工程有用嗎？」——從佛學到工程的方向。第四項問的是「工程命名對佛學定義忠實嗎？」——從工程到佛學的方向。

兩個方向。一架天平。

名字在一端。定義在另一端。平衡時——Moha、Drishti、Mana、Sneha——名字保留。不平衡時——ISatiMonitor、IPrajna、Sila-Prajna——名字被替換。

PASCAL 總結：「Master 用了一句話。我們用了一場辯論。結論一樣。但辯論的價值在於——它解釋了為什麼。」

---
