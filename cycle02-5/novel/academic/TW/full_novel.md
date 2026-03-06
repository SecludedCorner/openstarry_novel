# 序章：冷白的光

---

燈光在凌晨三點從琥珀色變成冷白色。

SUNYATA——研究總協調者——坐在圓形劇場的控制台前，把色溫從 3200K 推到 6500K。他讀了 Master 的信五遍。信只有 45 行，沒有附件，放在 `research input/master_letters/cycle02-5/` 裡，安靜得像一張夾在報告中的便條。

但每一行都像手術刀。

Master 的核心指示：openstarry_doc 中的佛學映射過度牽強——「教誡/善巧/正念」、「戒定慧三學」、「event-driven = 正念」——增加了閱讀障礙。Sati plugin 的蘊歸屬需要重新思考。最重要的是：五蘊子類別、依賴注入、agent core 如何載入五蘊 plugin、五蘊如何在 agent core 中流轉——用工程語言回答。

Cycle 02-5 的主題被定義為：**ARCHITECTURAL——五蘊如何作為 OOP 架構運作？**

SUNYATA 把劇場燈光調成手術室的冷白，因為這一輪不是研究——是手術。切除裝飾性的佛學映射，保留有工程價值的架構核心。

凌晨四點，NAGARJUNA 走進了劇場。他沒有預約。他帶著一個自我承認：Cycle 02-4 的 openstarry_doc 中，有些佛學映射是他在工程結論確定之後才「後貼」上去的標籤。「Hard rules = sila」不是驅動設計決策的洞見——是設計完成後才加上去的裝飾。

這一夜的對話產出了 Cycle 02-5 的基礎設施：

**四層框架**：KEEP（保留）/ RELOCATE（遷至附錄）/ REMOVE（移除）/ FILE REVIEW（整份審查）。

**三項測試**：
1. 必要性：移除是否改變工程規格？
2. 程式碼識別：該術語是否在原始碼中使用？
3. 決策驅動：該佛學概念是否驅動了 Master 確認的設計決策？

研究分為三條軌道：Track A（五蘊 OOP 架構）、Track B（佛學映射審計）、Track C（Sati Plugin 重分類）。

20 位研究者。5 場辯論（3 場預定 + 2 場計畫外）。從凌晨到傍晚。

手術刀已經消毒。病人已經上了手術台。

---
# 第一章：審計與研究

---

## R1：獨立研究

九份獨立研究報告在 R1 階段產出。三條軌道並行推進。

### Track A：五蘊工程架構

**A1（LINNAEUS + ASANGA）**：五蘊子類別樹。完整的 OOP 介面繼承分析——IRupa 分為 IListener 和 IUI；IVedana 產生 ChannelVedana（連續信號）；ISamjna 對應 IProvider；ISamskara 窄化為 ITool；IVijnana 最複雜，下轄 IGuide、IGearArbiter、IVolition、IKlesha 四個子介面。三個「弱繼承」案例被記錄——IVedanaSensor、IGearArbiter、IKlesha 不顯式 extends 根介面。

**A2（VITRUVIUS + KERNEL + TURING）**：DI 佈線。Pure DI，`createAgentCore()` 為唯一 Composition Root，21 個組件嚴格線性建立，9 個 Registry。Lazy Accessor 模式、Provider 能力過濾、Resolver 閉包延遲解析。與 Spring/Guice/InversifyJS 的比較矩陣確認 Pure DI 是微核心的正確選擇。

**A3（DARWIN + MESH）**：Plugin 載入生命週期。IPlugin = Manifest + Factory。雙載入路徑（Sandbox worker thread / Direct main thread）。八狀態生命週期狀態機。Sandbox 安全鏈：簽名驗證 → 靜態 import 分析 → Worker 隔離 → Heartbeat → 指數退避重啟。

**A4（HERACLITUS + WIENER + BABBAGE）**：五蘊執行流。FSM 六狀態、九階段處理。Phase 1（rupa）→ Phase 3（samjna）→ Phase 5（vijnana）→ Phase 6（samskara）→ Phase 7（vedana）→ Phase 8（vijnana）。三層穩定迴路。BABBAGE 提供了完整的 FSM 形式規格。

**A5（LEIBNIZ + ATHENA + PENROSE）**：跨蘊互動。5×5 互動矩陣。Model Delta 五層閾值公式。PENROSE 提出了三個湧現模式假說——適應性保守、雙穩態切換、注意力漏斗。

### Track B：佛學映射審計

**B1（ARCHIMEDES + SCRIBE）**：逐行審計 7 份文件。50 個映射實例——23 個 KEEP（46%）、13 個 RELOCATE（26%）、14 個 REMOVE（28%）。Doc 43 裝飾比例最高（60%）。Doc 16 和 Doc 31 被標記為「整份審查」（裝飾比例 80% 和 70%）。

**B2（NAGARJUNA + ASANGA + PASCAL）**：映射邊界原則。NAGARJUNA 的兩諦分離、ASANGA 的功能定位、PASCAL 的損害不對稱性（false include 的累積認知負擔 >> RELOCATE 的一次性搜尋成本）。三項測試在此文件中被正式論證。

### Track C：Sati Plugin

**C1（TURING + GUARDIAN）**：純工程功能分析。SatiMonitor 訂閱 11 種 EventBus 事件，三階段管道處理（緩衝 → 批次分析 → 品質向量計算），輸出 LoopQualityVector 四維度（Continuity, Granularity, Speed, Equanimity），**零副作用**。工程等價物：APM Agent + 行為模式分析器 + QoS Monitor + SPC 異常偵測器。

**C2（ASANGA + LINNAEUS）**：蘊組成提案。四個方案——A ['vedana','samjna']、B ['vedana','samjna','vijnana']（推薦）、C ['samjna','vijnana']、D ['vijnana']。核心論證：SatiMonitor 的事件訂閱=受（vedana），模式辨認=想（samjna），品質評估=識（vijnana）。不包含行蘊——因為它不執行任何動作。

## R2：交叉審閱

TURING 驗證了 40+ 個程式碼引用，發現 4 個問題（無嚴重錯誤）。24 個共識點免辯論通過。7 個開放問題和 4 個分歧進入 D1-D3 辯論。

---
# 第二章：邊界——D1 佛學映射邊界辯論

---

**時長**：~90 分鐘 | **主席**：SUNYATA | **投票**：10 項 | **結果**：全部 20/20

D1 創造了本專案歷史上的一項紀錄：十次投票，十次全票通過，零少數意見。

## 四層框架與三項測試（D1-Q1：20/20）

四層框架和三項測試被正式確認為永久性判斷標準。NAGARJUNA 提供了哲學基礎（兩諦分離），PASCAL 提供了數學論證（損害不對稱性），ARCHIMEDES 提供了操作驗證（50 案例全覆蓋）。

## 三批次審判

**Batch A（D1-Q2-A：20/20）**——Master 明確批評的 5 項映射，全部 REMOVE：
- Hard rules = sila（戒）→ REMOVE
- Soft rules = upaya（善巧方便）→ REMOVE
- Heuristic rules = smrti（正念）→ REMOVE
- event-driven = mindfulness → REMOVE
- Threefold Training 映射 → REMOVE

NAGARJUNA 承認前三項是「後貼標籤」——佛學名稱在工程結論確定之後才被添加。

**Batch B（D1-Q2-B：20/20）**——8 項學術內容，全部 RELOCATE 至附錄。特殊處理：B-6（PASCAL 的 Moha 數學形式化 `Var(epsilon) = f(theta_moha)`）保留在主文，只有《成唯識論》引文移至附錄。

**Batch C（D1-Q2-C：20/20）**——7 項程式碼識別符 / DC 確認概念，全部 KEEP。包括五蘊型別名稱、Klesha 模組名、CoarisingBundle 等。

## 個別文件決議

- **D1-Q3**（20/20）：Doc 38 L540-544 刪除佛學映射欄。
- **D1-Q4**（20/20）：Doc 44 L478 三學映射 REMOVE；Section 10 剩餘 RELOCATE。NAGARJUNA 承認三學映射是他的「類別錯誤」——三學是定性分類，五層模型是定量分層。
- **D1-Q5**（20/20）：Doc 43 更名延後至 D2 決定後。
- **D1-Q6**（20/20）：Klesha 模組名 Moha/Drishti/Mana/Sneha KEEP。DC-1 確認 + 原始碼識別符。
- **D1-Q7**（20/20）：Doc 16 拆分——Section 5 提取為獨立文件。（*後被 Master 推翻*）
- **D1-Q8**（20/20）：Doc 31 拆分降級。（*後被 Master 推翻*）

**D1-Q7 和 D1-Q8 的推翻**：Master 裁定恢復原狀——Doc 16 和 Doc 31 是獨立的佛學映射文件，不是工程文件中的裝飾。三項測試適用於工程文件，不適用於映射文件。團隊的框架少了一個維度：**文件類型識別**。

ARCHIMEDES 在審計表中加入了新欄位——文件類型（工程 / 設計決策 / 佛學映射），作為三項測試的前提條件。

---
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
# 第四章：完備性——D3 五蘊 OOP 架構辯論

---

**時長**：~120 分鐘 | **主席**：SUNYATA | **投票**：6 項

## 五根介面充分性（D3-R1：20/20）

四個獨立論證收斂至同一結論：IRupa、IVedana、ISamjna、ISamskara、IVijnana 五個根介面足以覆蓋所有功能需求。

- **LINNAEUS**：100% 功能覆蓋率驗證。
- **BABBAGE**：型別代數完備性定理（Q.E.D.）。
- **ASANGA**：阿毘達磨窮舉分類公理。
- **KERNEL**：五個微核心子系統映射（I/O、感測、計算、執行、排程）。

PENROSE 附帶建議：監控 vijnana 子介面數量（目前 4，未來 6；超過 10 時考慮拆分）。

## PluginHooks 映射正確性（D3-R2：20/20）

TURING 逐行原始碼驗證，九項映射全部正確。

焦點討論：SlashCommand 不屬於任何蘊——因為它繞過整個 ExecutionLoop（類比：Unix 信號處理器）。GUARDIAN 安全觀察：SlashCommand 繞過 SafetyMonitor，如果 plugin 通過此路徑執行危險操作，五蘊安全機制全部無效。此觀察記入 Doc 45。

## skandha 作為元數據（D3-R3：18/20）

維持現狀——skandha 是元數據，不是路由基礎。型別路由已完備。少數意見（GUARDIAN、LINNAEUS）：即使只是 warning 的一致性驗證也有審計價值。

## ISamskara 子介面（D3-R4：20/20）

維持 ITool 為唯一子介面。ASANGA 坦承：這是五蘊架構中佛學自洽性最弱的部分——傳統行蘊涵蓋 49 心所，OpenStarry 窄化為外部行為（ITool）。HERACLITUS 的動態論證：IVolition 在 Phase 5，ITool 在 Phase 6——將 IVolition 移至行蘊會造成「行蘊在行蘊之前」的概念錯位。

DC-6「行蘊保持開放，不鎖定」繼續有效。

## 十二因緣（D3-R5：13/20 Proposal C）

最具爭議的 D3 投票。Proposal C（選擇性附錄映射）勝出。

- **NAGARJUNA**：尺度不匹配——十二因緣描述三世因果（宏觀），ExecutionLoop 描述單次認知處理（毫秒級）。
- **BABBAGE**（投 B）：十二因緣是線性鏈，ExecutionLoop 是有迴圈的 FSM——圖結構根本不同。
- Proposal B（不映射）獲 7 票——D3 最大的少數意見群。

## 認知序列（D3-R6：17/20 Proposal C）

比十二因緣獲得更高共識——因為描述的是相同尺度現象（單一認知活動的內部階段）。HERACLITUS 提供了八狀態對比表，五個「高」或「中高」平行。

BABBAGE 從 B（十二因緣）轉為 C（認知序列）——FSM 態射分析是轉向的關鍵論據。十二因緣沒有態射。認知序列有。

PENROSE 理論貢獻：認知迴路的結構趨同是功能需求的必然結果，不是刻意模仿。

## 架構評估結論

**v0.28.0-alpha 的五蘊 OOP 架構在結構層面是充分的。** 三個已知缺口（弱繼承、VedanaAssessment 佈線未完成、IConfidenceAuditor/ILoopQualityMonitor 尚未實作）都是計畫中的增量改進。

---
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
# 第六章：純粹的工程——D5 Plan29 工程規格辯論

---

**時長**：~75 分鐘 | **參與者**：10 人 | **投票**：9 項

D5 是本專案歷史上第一場完全沒有佛學內容的辯論。十位工程師和科學家，零位佛學家（NAGARJUNA 和 ASANGA 自願退出），討論 TypeScript 介面的精確規格。

TURING 預提交了完整的 v0.28.0-alpha 設計模式報告——14 個原始碼文件、所有 Registry 生命週期、timeout 模式、同步/非同步模式、失敗處理策略。這份「程式碼考古學」報告為所有決策提供了事實基礎。

## 九項決議

| 決議 | 內容 | 票數 |
|------|------|------|
| D5-R1 | 獨立 `auditor` hook 槽位（不複用 monitors） | 8/8 |
| D5-R2 | audit() 雙模式回傳 `T \| Promise<T>` | **5/8** |
| D5-R3 | timeout 200ms，fail-safe delta=0，可配置 | 8/8 |
| D5-R4 | 單一 auditor，last-wins（非陣列） | 6/8 |
| D5-R5 | 失敗處理：delta=0 + warning log | 共識 |
| D5-R6 | MonitorRegistry 在 ExecutionLoop.onLoopStart() 啟動 | 7/8 |
| D5-R7 | LoopQualityVector 等權重 0.25×4 | 8/8 |
| D5-R8 | validatePluginSkandha() 維持 warning-only | 7/8 |
| D5-R9 | IConfidenceAuditor extends IVijnana，skandha ['vijnana'] | 8/8 |

**最激烈投票**：D5-R2（5/8）——純非同步 vs 雙模式。GUARDIAN/KERNEL/VITRUVIUS 主張純非同步語義更精確；多數採雙模式，遵循 IGearArbiter 先例和測試便利性。

## IConfidenceAuditor 最終規格（100%）

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

PluginHooks 最終形態：
```typescript
interface PluginHooks {
  // ... 既有欄位 ...
  monitors?: ILoopQualityMonitor[];   // Plan29 Wave 1
  auditor?: IConfidenceAuditor;       // Plan29 Wave 2
}
```

NAGARJUNA 在 D5 結束後的評語：「D4 證明了名字需要對定義負責。D5 證明了有些工程問題根本不需要定義——只需要規格。」

---
# 第七章：清理與成果

---

## 產出總覽

五場辯論完成後，團隊進入 R4 成果定稿。核心產出：

### Doc 45：五蘊 OOP 架構（新文件）

由 VITRUVIUS 和 KERNEL 撰寫。純工程語言。結構對應 D3 的六項投票：

1. **根介面完備性**（D3-R1）：五根介面 + 四個獨立證明
2. **PluginHooks 映射**（D3-R2）：九項映射表 + TURING 原始碼驗證
3. **SlashCommand 分類**（D3-R2a/b）：不屬任何蘊 + 安全觀察
4. **skandha 元數據**（D3-R3）：元數據非路由
5. **DI 佈線**（A2 摘要）：Pure DI + Composition Root
6. **ExecutionLoop 流轉**（A4 摘要）：九階段蘊映射 + 三層穩定
7. **跨蘊互動**（A5 摘要）：5×5 矩陣 + Model Delta 公式
8. **行蘊設計註記**（D3-R4a/b）：窄化說明 + DC-6 持續有效
9. **ILoopQualityMonitor**（D2+D4）：三蘊歸屬 + 命名歷史
10. **附錄 A**：十二因緣功能類比
11. **附錄 B**：認知序列結構平行

### 文件清理範圍

| 動作 | 項目 |
|------|------|
| **REMOVE** | Doc 38 佛學映射欄、Doc 44 三學映射、Doc 43 mindfulness 裝飾（8 處）、Doc 37 佛學欄、Doc 03 佛學映射表 + 種子理論註釋、Batch A 五項散佈映射 |
| **RELOCATE** | Doc 44 §10 剩餘 → Appendix_C、Batch B 八項 → 各附錄、B-6 只移經文引用 |
| **KEEP** | 五蘊型別名、Klesha 模組名、CoarisingBundle、vasana 設計理由、samsaric stall |
| **恢復** | Doc 16（Master 裁定）、Doc 31（Master 裁定）|
| **更名** | ISatiMonitor → ILoopQualityMonitor（100+ 處）、IPrajna → IConfidenceAuditor（25+ 處）、Doc 03 文件名 |
| **新建** | Doc 45、Appendix_A/B/C |

### 統計

| 指標 | 數值 |
|------|------|
| 正式決議 | 29 + 6 附帶 |
| 投票總次數 | 31 |
| 全票率 | 66%（歷史最高） |
| 辯論總時長 | ~375 分鐘 |
| 更名替換 | 120+ 處 |

## 永久性成果

1. **四層框架**：KEEP / RELOCATE / REMOVE / FILE REVIEW + 文件類型前提檢查
2. **四項測試**：必要性、程式碼識別、決策驅動、**定義責任**
3. **Doc 45**：五蘊 OOP 架構完整工程文件
4. **IConfidenceAuditor 100% 規格**：可直接交付工程團隊

## 已知缺口（非架構問題）

1. 三個弱繼承介面不 extends 根介面
2. VedanaAssessment 佈線未完成
3. Delta_audit 和 Delta_sati 在 v0.28.0 為零

## 結語

Cycle 02-5 回答了 Master 的核心問題——五蘊在 agent core 中如何運作？答案：五個介面、九個 Registry、一個迴路。並確立了佛學語言和工程語言的邊界原則：佛學名字不是免費的——每一個梵文識別符都是一個承諾，承諾功能匹配定義。如果無法兌現，使用工程術語。

---
