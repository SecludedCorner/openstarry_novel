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
# 第一章：行蘊的經典學重構 —— 從 cetana 中心性到功能判定準則

---

## 1.1 問題的提出：行蘊作為「剩餘類別」的困境

在 OpenStarry v0.2.0-beta 的五蘊架構中，行蘊（samskara-skandha）長期處於定義不足的狀態。相較於色蘊（rupa，對應 `ISparsha` 感官接觸介面）、受蘊（vedana，對應 `IVedana` 感受介面）、想蘊（samjna，對應 `ISamjna` 辨識介面）和識蘊（vijnana，對應 `IManas` 判斷介面）的清晰功能映射，行蘊僅擁有一個子介面 `ITool`，負責外部工具呼叫。

這種不對稱並非偶然。其根源在於唯識學派（Yogacara）對行蘊的處理方式。在唯識的五十一心所（cetasika）分類體系中，受蘊僅分配到「受」（vedana）一個心所，想蘊僅分配到「想」（samjna）一個心所，其餘四十九個心所全部歸入行蘊。行蘊由此成為一個「剩餘類別」（residual category）—— 凡是不屬於受和想的心理功能，一律歸入行蘊。

DC Master 在研究委託中明確指出此做法「非常有問題」，並要求研究團隊回歸原始經典（如是我聞），重新建立行蘊的功能性定義。

---

## 1.2 原始經典中的行蘊定義

哲學軌由 NAGARJUNA（#7，中觀學派哲學家）與 ASANGA（#8，唯識學派佛學家）領銜。值得注意的方法論安排是：被批評的學派（唯識）的專家被指派去審視自身學派的問題，以確保批判的內在性與深度。

### 1.2.1 六思身：cetana 作為行蘊的定義性特徵

《雜阿含經》（Samyutta Nikaya 22.56, Khandha-samyutta）中，佛陀對行蘊的定義明確而狹窄：

> 「云何行蘊？謂六思身：色思、聲思、香思、味思、觸思、法思。是名行蘊。」

此處的「思」即 cetana（意圖/意志），「六思身」（cha cetana-kaya）指向六種感官對象的意圖性回應。這一定義的關鍵特徵在於其 **排他性**：行蘊不是「除受想以外的一切心理功能」，而是精確地指向 cetana —— 對六種對象的意圖性造作。

### 1.2.2 造作功能：abhisamskara 與有為法的條件化

《雜阿含經》（SN 22.79）進一步闡明行蘊的功能：

> 「行蘊造作色之被條件化狀態（rupam abhisankharonti）。」

此處的動詞 abhisankharoti 表明行蘊不僅「執行動作」，更根本地是「造作」（fabricate）—— 它創造條件、改變狀態、影響後續認知過程。行蘊的造作功能甚至延伸至其他四蘊：它能造作色蘊的被條件化狀態、受蘊的被條件化狀態，乃至識蘊的被條件化狀態。

### 1.2.3 芭蕉喻：無核心的動態過程

《雜阿含經》（SN 22.95, Phena-sutta）以芭蕉樹（kadali）比喻行蘊：

> 「譬如有人剝芭蕉莖，尋求堅實，層層剝之，了不可得。」

此喻直指行蘊的本體論地位：它不是一個具有堅實核心的「實體」（entity），而是一個持續運作的「過程」（process）。每一層纖維都是條件性的造作，剝開之後並無自性可得。

---

## 1.3 三個核心特質的歸納

基於上述經典文本，研究團隊歸納出行蘊的三個核心特質：

| # | 特質 | 經典依據 | 功能意涵 |
|---|------|---------|---------|
| 1 | **cetana 中心性** | SN 22.56（六思身） | 行蘊以意圖為定義性特徵，非「剩餘類別」 |
| 2 | **造作一切有為法** | SN 22.79（abhisamskara） | 行蘊創造條件、改變狀態，影響所有五蘊 |
| 3 | **無核心的動態過程** | SN 22.95（芭蕉喻） | 行蘊是過程而非實體，無自性可得 |

---

## 1.4 行蘊屬性判定三準則

LINNAEUS（#13，分類學/本體論專家）在上述三個特質基礎上，提出了一組可操作化的判定工具 —— 行蘊屬性判定三準則（Three Criteria for Samskara Attribution）：

**準則一：造作性（Fabrication）**
- 該功能是否創造、改變或產生新狀態？
- 判定方法：檢查該功能的輸出是否修改了系統狀態或外部環境。

**準則二：意圖驅動（Cetana-driven）**
- 該功能是否由 cetana（意圖）驅動？
- 判定方法：檢查該功能的觸發是否源於系統的意志性決策，而非被動反應。

**準則三：環境改變（Environmental Modification）**
- 該功能是否改變後續認知條件？
- 判定方法：檢查該功能執行後，後續認知迴路的輸入空間是否發生了變化。

三準則經 D1-R3 決議確認為**永久性工具**（permanent tool），適用於所有未來的蘊歸屬判定。

---

## 1.5 WRITE/READ 二分法

PENROSE（#18，量子意識研究專家）在討論中提出了一個極具概括力的二分法：

> **行蘊 = WRITE（主動改變世界）**
> **識蘊 = READ（被動評估世界）**

這一二分法在電腦科學中具有天然的對應物。在作業系統理論中，WRITE 操作修改系統狀態（副作用操作），READ 操作僅觀察系統狀態（純函數操作）。映射到 OpenStarry 的程式碼：

| 操作類型 | 蘊歸屬 | 程式碼介面 | 功能 |
|---------|--------|-----------|------|
| WRITE | 行蘊 (samskara) | `ITool`, `ISlashCommand` | 執行動作、改變環境 |
| READ | 識蘊 (vijnana) | `IGuide`, `IVolition` | 評估情況、做出判斷 |

此二分法經 D1-R5 決議（20/20 全票）正式確認，成為「活動與轉換」原則的核心表述。

---

## 1.6 唯識心所系統的批判性分析

ASANGA 親自主導了對唯識五十一心所系統的批判性分析（報告 C2）。以行蘊屬性判定三準則為工具，他逐一檢視了被唯識學派歸入行蘊的 49 個心所，結果如下：

| 分類 | 數量 | 比例 | 說明 |
|------|------|------|------|
| 確屬行蘊 | 7 | 14% | chanda（意欲）、virya（精進）、apramada（不放逸）等 |
| 已有正確歸屬 | 12 | 24% | 在 OpenStarry 中已經通過功能分析獲得正確歸屬 |
| 可能屬他蘊 | 18 | 37% | 功能上更接近識蘊（如 prajna/慧）或受蘊 |
| 混合/待研究 | 14 | 28% | 需要更精細的功能分析或跨蘊處理 |

此分析的方法論意義在於：它以功能分析（functional analysis）取代了傳統分類（traditional taxonomy）作為蘊歸屬的判定依據。正如 ASANGA 本人所述：

> 「心所列表是有用的功能描述清單，但它是論典（Abhidharma）的產物，不是佛陀的原話。我們可以參考其功能描述，但不能讓其分類方式決定蘊歸屬。」

---

## 1.7 蘊歸屬五項永久性原則

基於上述研究，D1-R6 決議（20/20 全票）確立了五項永久性原則：

1. **功能分析原則**：功能分析為蘊歸屬的唯一依據。
2. **心所參考原則**：唯識五十一心所系統作為功能參考清單（reference list），不作歸屬依據。
3. **梵文限定原則**：梵文術語用於程式碼命名時，僅限源自原始經典者（如 skandha、sparsha），不使用論典創造的心所梵文名。
4. **跨蘊歸屬原則**：Plugin 不等於心所，蘊歸屬可自然跨越多蘊。
5. **既有決議原則**：既有歸屬決議（基於功能分析）繼續有效。

這五項原則與後續第五章將討論的 Master 八點規則共同構成了 OpenStarry 未來所有命名與歸屬問題的永久判定框架。

---
# 第二章：審計上下文的型別設計 —— 資訊充分性與回饋迴路切斷

---

## 2.1 問題分析：IConfidenceAuditor 的資訊貧乏

Plan29 交付的 `IConfidenceAuditor` 介面存在結構性缺陷：審計函數的輸入僅包含 `RouteResult`（路由結果）。審計員無法獲取觸發事件（sparshEvent）、仲裁器推理過程（gearEvaluation）、風險等級（riskCategory）或歷史信心度序列。以決策理論術語而言，這是一個資訊不對稱（information asymmetry）問題。DC Master 明確指示審計員需要更多資訊。

然而，擴充審計員可見資訊的同時引入了控制理論風險：**正回饋迴路**（positive feedback loop）。

---

## 2.2 正回饋迴路的威脅模型

WIENER（#12）識別出三條潛在的正回饋路徑：

1. **historicalConfidence 污染**：若歷史序列包含審計後調整值，形成 `audit → confidence → history → audit` 閉合迴路
2. **審計結果洩漏**：若 AuditContext 包含前次審計結果，形成確認偏誤驅動的序列相關
3. **extras 後門**：若 extras bag 允許寫入審計相關鍵值對，間接洩漏歷史輸出

三條路徑均可導致 BIBO 不穩定：信心度值在迭代中單調增長或振盪發散。

---

## 2.3 AuditContext 型別定義 [D2-R1, 20/20]

```typescript
export interface AuditContext {
  readonly version: 1;                              // 字面量型別
  readonly sparshEvent: SparshEvent;                // 觸發事件（必填）
  readonly gearEvaluation: GearEvaluation;          // 仲裁器完整推理過程
  readonly riskCategory: RiskCategory | undefined;  // 風險類別（可選）
  readonly routeResult: RouteResult;                // 審計前路由結果快照
  readonly historicalConfidence?: readonly number[]; // 環形緩衝區，預設 10
  readonly extras: ReadonlyMap<string, unknown>;     // 泛型擴展袋
}
```

核心欄位由 Core 組裝；historicalConfidence 為可選環形緩衝區；extras 為 ReadonlyMap，透過 `getExtra<T>(extras, key, guard)` 型別安全存取器讀取。

---

## 2.4 WIENER 三約束

**C-1（歷史純淨性）**：historicalConfidence 僅記錄仲裁器原始信心度 $c_t^{raw}$，不含審計後調整值。

**C-2（審計結果隔離）**：AuditContext 不包含前次 ConfidenceAuditLog。每次審計資訊獨立。

**C-3（extras 前綴禁令）**：禁止 `audit:`、`core:`、`internal:` 前綴，防止審計結果通過 extras 洩漏。

三約束確保審計員的**因果隔離**（causal isolation）。BABBAGE（#9）的形式化驗證：審計函數 $f: \mathcal{C} \times \mathcal{A} \to [-0.05, +0.05]$ 在三約束下，輸入不含自身先前輸出，調整量受限幅約束，信心度值域 $[0,1]$ 自然有界，系統滿足 BIBO 穩定。

---

## 2.5 extras bag 協議 [D2-R2, 19/20]

| 面向 | 規格 |
|------|------|
| 寫入模式 | 雙事件 + SDK `emitWithExtras()` |
| 收集管道 | ManoAggregator 訂閱 `audit:context_contribute` |
| 讀取介面 | `getExtra<T>(extras, key, guard)` |
| 不可變性 | 淺凍結 + ReadonlyMap |
| 限制 | max 32 keys, 128 chars/key |
| 鍵命名 | `{category}:{name}` 格式 |

一票反對認為雙事件模式增加不必要複雜性，多數認為其通用性（任何 Plugin 均可透過相同協議貢獻資訊）證成了設計。

---

## 2.6 ConfidenceAuditLog [D2-R3, 20/20]

完整審計軌跡型別：inputConfidence, rawDelta, clampedDelta, wasClamped, reasoning（截斷 500 字元）, outputConfidence, result, auditDurationMs。主通道為 EventBus `audit:completed` 事件；JSONL 持久化排程至 Plan31。

GUARDIAN（#11）在此決議通過後正式聲明：「D5 的讓步條件已兌現。我不再保留重新審議 $\pm 0.05$ 限幅的權利。」此聲明終結了自 Cycle 02-4 以來圍繞信心度調整安全性的持續爭議。

---
# 第三章：四維品質向量 —— 認知迴路的量化評估框架

---

## 3.1 問題定義

OpenStarry 的 AI Agent 運作於認知迴路中：sparsha → vedana → samjna → samskara → manas/vijnana → 下一輪輸入。`ILoopQualityMonitor` 需對此迴路的運作品質進行即時量化評估。品質是多維概念，單一指標不足。WIENER（#12）與 ATHENA（#5）設計了四維品質向量（LoopQualityVector），經 D3-R1（20/20）確認。

---

## 3.2 四維公式

設滑動窗口大小 $W = 10$，暖機期 $W_{warmup} = 5$。

### 3.2.1 一致性（Coherence）

$$\text{coherence} = 1 - \frac{\text{switchCount}}{W - 1}$$

衡量路由決策穩定性。高值表示 Agent 持續在同一處理模式下運作，低值表示頻繁切換。輸入事件：`gear:switch`。

### 3.2.2 效率（Efficiency）

$$\text{efficiency} = \frac{\text{success}}{\text{proposed}} \quad (\text{若 proposed} = 0, \text{則} = 1.0)$$

衡量工具呼叫成功率。退化處理：無 proposed 事件時預設 1.0。輸入事件：`action:proposed`, `tool:result`。

### 3.2.3 收斂性（Convergence）

$$\text{convergence} = \frac{\text{longestStreak}}{W}$$

衡量 Agent 是否趨近穩定狀態。與效率的區別：效率衡量「總量」，收斂性衡量「趨勢」—— 8 次成功集中在最後 8 次（收斂性 0.8）與散布在窗口各處（可能僅 0.3）意義不同。輸入事件：`gear:switch`。

### 3.2.4 穩定性（Stability）

$$\text{stability} = 1 - \min\left(1, \frac{\sigma^2}{0.25}\right)$$

衡量仲裁器信心度輸出的方差。分母 0.25 為寬鬆正規化基準。輸入事件：`gear:arbiter_evaluated`。

---

## 3.3 複合品質分數與權重

$$Q = \sum_{i=1}^{4} w_i \cdot d_i, \quad Q \in [0, 1]$$

Phase 1 等權重 $w_i = 0.25$。理論依據為 PASCAL（#19）的最大熵論證：在缺乏先驗知識的情況下，最大熵原則（Jaynes 1957）要求均勻分配權重。D3-R4（20/20）確認 Phase 1 固定等權重、Phase 2 可配置（balanced / stability-focused / efficiency-focused 三組預設）。

---

## 3.4 滑動窗口與計算複雜度

| 參數 | 值 | 理由 |
|------|-----|------|
| $W$ | 10 | 敏感度與穩健性之間的平衡 |
| $W_{warmup}$ | 5 | 暖機期避免小樣本偏差 |
| $Q_{default}$ | 0.5 | 暖機期內的中性預設值 |

所有計算 $O(1)$ per event、$O(W)$ 空間，確保品質監控不成為效能瓶頸。

---

## 3.5 EventBus 事件訂閱 [D3-R2, 20/20]

**Phase 1（6 事件）**：`gear:arbiter_evaluated`（穩定性）、`gear:switch`（一致性+收斂性）、`action:proposed`（效率）、`tool:result`（效率）、`loop:started`（窗口管理）、`loop:finished`（窗口管理）。

**Phase 2（+5 事件）**：`sparsha:contact`, `tool:error`, `tool:blocked`, `vitakka:stall`, `action:executed`。

**退化原則**（HERACLITUS #15）：「缺失是資訊，不是錯誤。」缺失事件使用安全預設值（效率 1.0、穩定性 0.5），不拋出異常。同時將散布於程式碼中的事件字串字面量統一提升為 `AgentEventType` 常量。

---
# 第四章：雙通道整合架構 —— Layer 2/3 的正交分離設計

---

## 4.1 決策機制的形式化描述

OpenStarry 的核心路由決策為閾值比較：若 $c > \theta$ 則採用仲裁器推薦方案，否則走預設方案。Cycle 02-6 引入 IConfidenceAuditor（Layer 2，調整 $c$）和 ILoopQualityMonitor（Layer 3，調整 $\theta$）。核心問題：如何讓兩者同時生效而不互相干擾？

---

## 4.2 三個候選方案與選擇

**方案 A（串聯）**：$Q$ 先改閾值，審計員在新閾值下評估。存在序列依賴。
**方案 B（耦合）**：$Q$ 和審計員同時影響信心度與閾值。存在交叉項。
**方案 C（正交）**：審計員僅改信心度，品質監控器僅改閾值。完全獨立。

D2-R4（20/20 全票）選擇方案 C。

---

## 4.3 方案 C 的形式化定義

**Layer 2**：$c_{adj} = c_{raw} + \text{clamp}(\Delta c, -0.05, +0.05)$

**Layer 3**：$\theta_{adj} = \max(\theta_{floor}, \; \theta_{base} \times (1 - \alpha \cdot Q))$，其中 $\alpha = 0.10$

**最終路由**：$c_{adj} > \theta_{adj}$ → arbiter\_gear，否則 default\_gear

---

## 4.4 設計優勢

**正交性**：Layer 2 僅操作 $c$，Layer 3 僅操作 $\theta$，不存在 $f(c, Q)$ 或 $g(\theta, \Delta c)$ 形式的耦合函數。兩元件可獨立開發、測試、部署。

**BIBO 穩定性**：$c_{adj}$ 受 $[0,1]$ 夾持，$\theta_{adj} \geq \theta_{floor} > 0$，無交叉項則無通道間正回饋放大路徑。

**保守退化**：無審計員則 $\Delta c = 0$；無品質監控器則 $Q = 0$。任一元件缺失時系統行為等價於該元件不存在的版本。

---

## 4.5 品質分數傳輸：Pull + Push 雙通道

| 消費者 | 需求 | 傳輸模式 |
|--------|------|---------|
| ManoAggregator（L3） | 即時數值 | Pull：`loopQualityFn()` 回調 |
| IConfidenceAuditor（L2） | 豐富背景 | Push：extras bag via `audit:context_contribute` |

Push 通道寫入 `loopQuality:vector`（四維）和 `loopQuality:composite`（$Q$）。生命週期為 per-routing-cycle，每次路由結束後 extras bag 清空（LEIBNIZ #14 強調：避免過時資訊累積）。

---

## 4.6 五層決策模型

```
L0: EventBus          -- 基礎事件流
L1: Klesha（煩惱）     -- 四個情緒模組調整閾值
L4: Vedana Emergency   -- 緊急感受直接降低閾值（安全關鍵，優先級最高）
L3: LoopQuality        -- 品質分數微調閾值（α=0.10）
L2: Audit              -- 審計員微調信心度（±0.05）
→ 最終比較: c_adj > θ_adj → 路由決策
```

Layer 順序遵循優先級遞減原則。Plan30 的成功標準：L0~L4 全部有實際信號路徑。

**邊際情境**：多監控器以簡單平均聚合（Phase 1）；監控器超過 5000ms 未更新視為過期，$Q = 0$，L3 不生效。

---
# 第五章：心所命名指示的三輪精化 —— 從論典產物到命名解耦

---

## 5.1 指示的觸發脈絡

R2 交叉審閱期間，ASANGA 的唯識心所批判報告（C2）被提交至 DC Master。Master 做出三輪連續性指示，直接導致 D1 議程修訂：D1-Q2（心所多蘊歸屬）刪除，D1-Q6（逐條投票 26 項）簡化為原則投票。

---

## 5.2 第一輪：經典與論典的區分

> 心所是論典（Abhidharma）的產物，非原始經典（Sutta/Agama）的內容。

佛陀在原始經典（SN 22.56、MN 44 等）中闡述了五蘊、十二因緣、八正道。五十一心所分類體系則是無著（Asanga）、世親（Vasubandhu）等後世論典學者在佛陀入滅後數百年間建構的。

直接結論：**Plugin 命名不得使用心所梵文名。**

---

## 5.3 第二輪：功能描述的參考價值

> 心所的功能描述具有參考價值，可作為 Plugin 設計靈感。

心所「精進」（virya）描述的「持續投入」功能可啟發重試 Plugin 設計，但該 Plugin 應命名為 `RetryPlugin`，非 `VīryaPlugin`。

- **允許**：「參考精進的涵義，設計了重試 Plugin」
- **禁止**：「重試 Plugin = 精進」

此區分在「借鑑」（reference）與「等同」（identification）之間劃定界線。

---

## 5.4 第三輪：命名解耦與歸屬自由

> Plugin 不等於心所（plugin ≠ cetasika）。

邏輯推論：唯識系統中每個心所有固定蘊歸屬（如 virya 屬行蘊）。若 Plugin = 心所，Plugin 歸屬被鎖死。但 Plugin ≠ 心所，因此 Plugin 可同時具有行蘊功能（WRITE）和識蘊功能（READ），不產生邏輯矛盾。

Master 概括：**「命名解耦帶來歸屬自由。」**

---

## 5.5 八點永久性規則

| # | 規則 | 性質 |
|---|------|------|
| 1 | 心所是論典產物，非原始經典內容 | 文獻學判定 |
| 2 | 心所功能可作為 Plugin 設計靈感 | 肯定性保留 |
| 3 | 可說明「參考某心所涵義，設計某 Plugin」 | 表述規範 |
| 4 | Plugin 用工程術語命名，禁用心所梵文名 | 命名規範 |
| 5 | 梵文術語限於原始經典者 | 術語範圍 |
| 6 | 心所分類不作為蘊歸屬依據 | 歸屬原則 |
| 7 | 既有 Plugin 歸屬決議不受影響 | 穩定性保證 |
| 8 | Plugin ≠ 心所，可自然跨多蘊 | 跨蘊自由 |

---

## 5.6 與蘊歸屬五原則的互補

| 面向 | 蘊歸屬五原則 | 八點規則 |
|------|------------|---------|
| 來源 | 研究團隊歸納 | DC Master 指示 |
| 焦點 | 歸屬判定方法 | 命名與術語規範 |
| 核心主張 | 功能分析為唯一依據 | Plugin ≠ 心所，命名解耦 |

兩套規則構成永久性判定框架。NAGARJUNA：「02-5 學會了什麼不該做。02-6 學會了為什麼不該做。」

---
# 第六章：辯論過程的方法論分析 —— 從衝突驅動到共識確認

---

## 6.1 與 Cycle 02-5 的結構性對比

| 指標 | Cycle 02-5 | Cycle 02-6 | 變化 |
|------|-----------|-----------|------|
| 辯論場次 | 5 | 3 | -40% |
| 決議總數 | 29 | 17 | -41% |
| 全票通過（20/20） | ~20 (~69%) | 13 (76%) | +7pp |
| Master 覆議 | 2 | 0 | -100% |
| 總辯論時間 | ~400 min（估計） | ~245 min | -39% |

DARWIN（#6）的結構性解釋：02-5 是正確性辯論（correctness debate），爭議焦點在於什麼是對的、什麼是錯的；02-6 是規格辯論（specification debate），爭議焦點在於對的東西應該長什麼樣子。後者天然更容易達成共識。SUNYATA 補充：14 份 R1 報告在 R2 交叉審閱中產生 24 個共識點、僅 3 個分歧點，辯論功能從「爭論」轉為「確認與精化」。

---

## 6.2 三場辯論概覽

### D1：行蘊深掘（約 75 分鐘，7 項決議）

依據跨軌道影響協議優先進行。D1-R1（20/20）確認 cetana 中心定義；D1-R3（20/20）確認不新增 ISamskara 子介面、三準則為永久工具；D1-R4a（19/20）排程認知序列附錄至 02-7；D1-R4b（18/20）以四項測試排除四智（catvari-jnanani）；D1-R4c（20/20）確認心智論述評估表；D1-R5（20/20）確認 WRITE/READ 二分法；D1-R6（20/20）確認蘊歸屬五原則。跨軌道影響評估：D1 結論對 D2/D3 無需追加議題。

### D2：AuditContext（約 85 分鐘，5 項決議）

D2-R1（20/20）確認 AuditContext 型別；D2-R2（19/20）確認 extras bag 協議（一票反對認為雙事件模式過度設計）；D2-R3（20/20）確認 ConfidenceAuditLog，GUARDIAN 宣布 D5 條件兌現；D2-R4（20/20）確認方案 C 雙通道；D2-R5（20/20）確認三階段 Auditor 策略（Phase 0 PassthroughAuditor → Phase 1 ThresholdAuditor → Phase 2 LLM-assisted）。R2 識別的三項分歧全部解決。

### D3：LoopQualityMonitor（約 85 分鐘，5 項決議）

D3-R1（20/20）確認四維公式；D3-R2（20/20）確認事件訂閱 + AgentEventType 常量提升；D3-R3（20/20）確認 extras 生命週期（per-routing-cycle）；D3-R4（20/20）確認等權重策略；D3-R5（19+1 條件）確認 Plan30 方向 —— GUARDIAN 條件：W3 必須包含 ConfidenceAuditLog SDK 型別定義，不得延後至 Plan31。條件被接納。

---

## 6.3 R2 交叉審閱的量化結果

R2 階段完成 4 組跨軌道交叉對照：

| 對照 | 結果 |
|------|------|
| C2 心所批判 → A1 AuditContext | 4/4 無影響 |
| C4 工程借鑒 → D2 Plan30 | 4/4 無影響 |
| C3 ISamskara 拓展 → B1 公式 | 5/5 無影響 |
| C2 心所批判 → 蘊歸屬清單 | 11 確認 / 0 需修正 / 1 待辯論 / 14 未來考慮 |

軌道內一致性：Track A 5/5 一致、Track B 3/5 一致（1 分歧）、Cross A-B 1/3 一致（2 分歧）。三項分歧全部在 D2 中解決。

跨軌道對照結果的學術意義在於：哲學軌的發現（行蘊重定義、心所批判）與工程軌的設計（AuditContext、品質公式）在結構上正交。這驗證了 SUNYATA 的雙軌設計假設：哲學深掘提供判定框架，工程設計在框架內獨立推進，兩者不存在衝突性依賴。

---

## 6.4 零否決的方法論解釋

17 項決議全部通過可從三個層面解釋：（1）R1 品質效應 —— 87.5% 的議題在辯論前已有共識；（2）辯論性質轉變 —— 規格辯論的分歧可透過技術論證解決；（3）跨軌道協議的有效性 —— D1 的七項哲學決議為 D2/D3 提供了穩定的概念基礎，消除了框架級分歧。

---
# 第七章：工程藍圖與研究總結 —— Plan30 規格與 Cycle 02-6 的學術貢獻

---

## 7.1 Plan30 工程規格 [D3-R5, 19+1 條件]

| Wave | 內容 | 估計 LOC | 關鍵技術點 |
|------|------|---------|-----------|
| W1 | Default LoopQualityMonitor Plugin | ~120 | 四維公式、6 事件訂閱、O(1)/event |
| W2 | Layer 3 佈線（方案 C） | ~80 | `loopQualityFn()` 回調、$\alpha=0.10$ |
| W3 | 型別定義與事件常量 | ~60 | ConfidenceAuditLog SDK、AgentEventType 提升 |
| W4（可選） | PassthroughAuditor | ~30 | delta=0 直通審計、端對端管道驗證 |

總計 ~260-290 LOC + ~130 test LOC。成功標準：Model Delta L0~L4 全部有實際信號路徑。

---

## 7.2 Plan31 展望

Plan31 完成審計管道端對端落地（~350 LOC）：AuditContext 組裝（Core 責任）、Default ThresholdAuditor（Phase 1 規則式）、Audit Trail JSONL 持久化。Plan30 建造管道，Plan31 讓邏輯流經管道。

---

## 7.3 Cycle 02-7 研究展望

- **P0**：Plan31 規格研究
- **P1**：Lyapunov 穩定性參數校準（$\alpha$ 驗證）、Moha/Sneha 耦合模擬、多監控器聚合策略驗證
- **P2**：認知序列（citta-vithi）附錄、十二因緣（pratityasamutpada）附錄
- **Cycle 03+**：八識深化（alaya-vijnana 多 Agent）、VasanaEngine、ISamskara 方向 A/B

---

## 7.4 成功標準達成

| # | 標準 | 達成 |
|---|------|------|
| 1 | AuditContext 型別定義 | D2-R1 (20/20) |
| 2 | 審計日誌格式（GUARDIAN D5 兌現） | D2-R3 (20/20) |
| 3 | LoopQualityVector 四維公式 | D3-R1 (20/20) |
| 4 | EventBus 事件訂閱清單 | D3-R2 (20/20) |
| 5 | OQ-29 全部回答（6/6） | 分散於各決議 |
| 6 | Plan30 方向建議 | D3-R5 (19+1) |
| 7 | 行蘊深掘報告 | C1-C4 + D1 |
| 8 | 心所逐條蘊歸屬（51 項） | C2 |
| 9 | 無範圍蔓延 | 確認 |

9/9 達成。

---

## 7.5 學術貢獻總結

### 哲學貢獻

**行蘊的經典學重構。** 從原始經典（SN 22.56, SN 22.79, SN 22.95, MN 44, SN 12.2）重建行蘊的功能性定義，以 cetana 為中心，取代唯識「剩餘類別」。WRITE/READ 二分法構成佛學與電腦科學間的高一致性概念框架。

**唯識心所批判。** 51 心所逐一檢視揭示系統性偏差：僅 14% 確屬行蘊。為功能分析優先於傳統分類提供了量化支持。

**永久性判定框架。** 蘊歸屬五原則 + Master 八點規則構成自洽、可操作化的判定框架。核心洞見「命名解耦帶來歸屬自由」具有超越本專案的方法論價值。

### 工程貢獻

**AuditContext 型別**：WIENER 三約束切斷正回饋迴路，BIBO 穩定性經形式化驗證。**四維品質向量**：最大熵原則等權重，$O(1)$ 複雜度，退化處理確保魯棒性。**方案 C 雙通道**：正交分離實現可證明的 BIBO 穩定、保守退化、獨立可測試性。

### 方法論貢獻

**跨軌道影響協議**確保哲學結論先於工程設計。**條件贊成機制**（D3-R5 GUARDIAN）展示了安全關切與進度之間的中間態決策方式。

---

## 7.6 結語：從減法到加法

- **Cycle 02-5**（減法）：什麼是錯的 —— 裝飾性映射、命名不當、歸屬混亂
- **Cycle 02-6**（加法）：什麼是對的 —— cetana 定義、AuditContext、四維公式、方案 C、永久規則

02-5 清理地基。02-6 畫好藍圖。Plan30 開始建造。

二十位研究者。十七項決議。十三項全票。零否決。零覆議。9/9 成功標準達成。

---

*Cycle 02-6 完。*

---
