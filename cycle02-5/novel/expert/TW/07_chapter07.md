# 第七章：純粹的工程

---

D4 結束後，SUNYATA 宣布了十五分鐘的休息。

沒有人離開座位。

不是不想休息——而是 D4 的餘震還在持續。ISatiMonitor 變成了 ILoopQualityMonitor。IPrajna 變成了 IConfidenceAuditor。Doc 03 從「Sila-Prajna Security Framework」變成了「Plugin Security Lifecycle」。三十分鐘。三個名字。一項永久性測試。

TURING 在休息時間打開了他的筆記型電腦。他沒有在休息——他在做最後的準備。

因為 D5 是他的辯論。

---

## I. 考古學家

TURING 在 Cycle 02-5 中的角色一直是「原始碼驗證者」——每一份研究報告中的程式碼引用都由他逐一核實。R1 的九份獨立研究，他驗證了 40 多個程式碼參考。R2 的交叉審閱，他發現了四個問題（無嚴重錯誤）。D1 到 D4，他是沉默的仲裁者——不參與哲學辯論，只在有人引用原始碼時站起來確認或修正。

但 D5 不同。

D5 的議題是：**Plan29 工程設計規格**。Master 的指示很明確：「繼續討論並記錄，直到規格達到 100%，然後交付工程團隊。」

為了這場辯論，TURING 提前做了一件他在之前所有 Cycle 中都沒有做過的事——他寫了一份完整的 v0.28.0-alpha 設計模式報告。不是摘要。不是要點清單。是對 14 個原始碼文件的全面分析：所有 Registry 的生命週期、timeout 模式、同步/非同步模式、失敗處理策略。

他把這份報告叫做「程式碼考古學」。

---

## II. 十位辯論者

D5 只有十位參與者。

不是因為其他人被排除了——是因為 SUNYATA 判斷 D5 的議題是純工程問題，不需要全部二十位研究者。他邀請了與 Plan29 最相關的十位：

| # | 代號 | 角色 | D5 焦點 |
|---|------|------|---------|
| 3 | VITRUVIUS | 架構分析師 | 介面設計 |
| 5 | ATHENA | AI/ML 專家 | Auditor 的 LLM 語義 |
| 6 | DARWIN | 軟體模式分析師 | 設計模式演化 |
| 10 | KERNEL | 作業系統專家 | Registry 生命週期 |
| 11 | GUARDIAN | 資安專家 | 安全邊界 |
| 12 | WIENER | 控制理論專家 | 品質向量權重 |
| 13 | LINNAEUS | 分類學專家 | 蘊歸屬推斷 |
| 16 | ARCHIMEDES | 工程實踐專家 | YAGNI 原則 |
| 17 | TURING | 原始碼分析專家 | 設計模式基底 |
| 19 | PASCAL | 決策理論專家 | 介面語義精度 |

十個人。零位佛學家。

NAGARJUNA (#7) 和 ASANGA (#8) 自願退出了 D5。不是因為他們沒有貢獻——而是因為 D5 的議題不需要佛學分析。NAGARJUNA 在退出前說了一句話：「D4 證明了佛學名字需要對定義負責。D5 會證明工程設計不需要佛學名字也能完成。這兩件事同樣重要。」

---

## III. 九項投票

D5 是 Cycle 02-5 中投票最多的辯論——九項。但也是節奏最快的辯論——七十五分鐘，平均每項投票不到九分鐘。

因為 TURING 的程式碼考古報告提供了事實基礎。每一項決策不是從「應該怎麼做」開始——而是從「目前是怎麼做的」開始。

---

### D5-R1：獨立的 `auditor` hook 槽位

第一個問題：IConfidenceAuditor（原 IPrajna）應該使用 PluginHooks 的哪個槽位？

選項：(A) 複用 D2 建立的 `monitors` 槽位；(B) 建立獨立的 `auditor` 槽位。

GUARDIAN 的論點最直接：「Monitors 是純觀察者——沒有副作用。Auditor 有 LLM 副作用——它呼叫外部模型做信心度評估。把觀察者和有副作用的組件放在同一個 Registry，模糊了安全審計的邊界。」

KERNEL 從作業系統的角度確認：「觀察者和仲裁者永遠不共享 Registry。這是微核心的基本原則。」

**8/8 全票通過。獨立 `auditor` 槽位。**

---

### D5-R2：audit() 回傳類型

最激烈的 D5 投票。

選項：(A) 純非同步 `Promise<ConfidenceAuditResult>`；(B) 雙模式 `ConfidenceAuditResult | Promise<ConfidenceAuditResult>`。

GUARDIAN、KERNEL、VITRUVIUS 支持選項 A——純非同步。理由：audit 本質上是「問 LLM」，LLM 呼叫是非同步的。強制非同步語義更精確。

ATHENA 和 DARWIN 支持選項 B——雙模式。理由：遵循 IGearArbiter 的先例。測試時可以用同步的 noop 實作，不需要 async/await 的樣板程式碼。

TURING 提供了事實：「v0.28.0-alpha 中，IGearArbiter.evaluate() 使用雙模式回傳。IVolition.deliberatePlan() 和 deliberateAction() 也使用雙模式。這是現有的設計模式。偏離它需要充分理由。」

**5/8 選項 B 通過。** D5 中最接近的投票。

---

### D5-R3：timeout 和 fail-safe

TURING 打開了他的 timeout 模式分析。v0.28.0-alpha 中現有的 timeout：

| 組件 | timeout | 預設值 |
|------|---------|--------|
| IProvider.chat() | LLM 回應 | 120s |
| IGearArbiter.evaluate() | 每個 arbiter | 100ms |
| IGearArbiter chain | 整條鏈 | 200ms |
| ITool.execute() | 工具執行 | 30s |

audit() 的 timeout 應該是多少？

TURING 的建議：200ms——與 IGearArbiter chain deadline 一致。理由：audit() 發生在 confidence 計算的最後階段，在 IGearArbiter 之後。如果 audit 的 timeout 超過 chain deadline，整個決策流程會被 audit 卡住。

fail-safe：`{ delta: 0, reasoning: "audit timeout" }`。timeout 時 delta 為零——不修正。使用 `Promise.race()` 模式，與現有程式碼一致。

Configurable：通過 agent.json 覆蓋預設值。

**8/8 全票通過。**

---

### D5-R4：多個 Auditor 的處理方式

Agent 可以裝載多個 IConfidenceAuditor plugin 嗎？

ATHENA 提出 YAGNI 原則：「v1 最多只有一個 auditor plugin。設計多 auditor 的聚合策略是過度工程。」

TURING 和 VITRUVIUS 持異議：「陣列模式更靈活。避免未來的破壞性變更。」

ARCHIMEDES 支持 ATHENA：「遵循 IVolition 先例——PluginHooks 宣告 `auditor?: IConfidenceAuditor`，單數，最後載入者勝出。如果未來需要多 auditor，那時再改——改一個介面比維護一個用不到的聚合策略便宜。」

**6/8 單一 auditor 通過。** TURING 和 VITRUVIUS 的少數意見被記錄。

---

### D5-R5：失敗處理

audit() 拋出異常時怎麼辦？

TURING 提供了現有模式：IGearArbiter 和 SafetyMonitor 都遵循「fail-safe + log」——錯誤不阻塞後續流程，記錄 warning。

不需要投票。共識直接達成。

---

### D5-R6：MonitorRegistry 啟動時機

ILoopQualityMonitor 的 `start(bus)` 在哪裡被呼叫？

TURING 的分析：SafetyMonitor 在 `ExecutionLoop.onLoopStart()` 啟動。MonitorRegistry 應該遵循相同的時機。

```
啟動：MonitorRegistry.startAll(bus) ← ExecutionLoop.onLoopStart()
關閉：MonitorRegistry.stopAll()    ← PluginLoader.disposeAll()
```

DARWIN 偏好在 PluginLoader 中啟動（更簡單），但接受了 monitors 有明確的 start/stop 語義，所以 ExecutionLoop 是更合適的位置。

**7/8 通過。**

---

### D5-R7：LoopQualityVector 權重

四維品質向量——Continuity、Granularity、Speed、Equanimity——每個維度的權重是多少？

WIENER 從控制理論的角度給出了唯一合理的答案：「沒有運行數據的情況下，等權重是最保守的選擇。每個維度 0.25。」

沒有人反對。0.25 × 4 = 1.0。簡單、對稱、可解釋。

minSamples 閾值（觸發 SPC 判斷前需要的最少樣本數）延後到 v2——需要實際運行數據來決定。

**8/8 全票通過。**

---

### D5-R8：validatePluginSkandha() 模式

這個函數在 plugin 載入時驗證 skandha 宣告的一致性。目前是 warning-only。應該改成強制嗎？

GUARDIAN（一票）偏好結構化的 ValidationResult——幫助自動化測試。但承認 v1 不需要。

多數意見：warning-only 足夠。如果 skandha 宣告不一致，plugin 功能不受影響（skandha 是 metadata，不是 routing——D3-R3 已裁定）。

**7/8 維持 warning-only。**

---

### D5-R9：IConfidenceAuditor 蘊歸屬

最後一項。IConfidenceAuditor 屬於哪一蘊？

ASANGA 雖然沒有參加 D5 辯論，但他在 R1 中的分析被引用了：「LLM 判斷 = 純識蘊（分辨、評估）。」

LINNAEUS 確認：「單蘊（vijnana）→ 強繼承（extends IVijnana），與 IVolition 和 IKlesha 一致。」

`inferSkandha()` 新增邏輯：`if (hooks.auditor) { push('vijnana') }`

**8/8 全票通過。**

---

## IV. 介面定稿

九項投票完成後，TURING 在白板上寫下了最終的介面規格：

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

和 PluginHooks 的最終形態：

```typescript
interface PluginHooks {
  // ... 既有欄位 ...
  monitors?: ILoopQualityMonitor[];   // Plan29 Wave 1
  auditor?: IConfidenceAuditor;       // Plan29 Wave 2（單數）
  // ...
}
```

他退後一步，看著白板。

「100%，」他說。

Master 要求的是「規格達到 100%」。現在達到了。介面名稱、方法簽名、回傳類型、timeout、fail-safe、多 auditor 策略、Registry 時機、權重、驗證模式、蘊歸屬——每一個需要決定的細節都有了明確的答案。

不是「大致方向」。不是「概念設計」。是可以直接交給工程團隊實作的完整規格。

---

## V. 零佛學

SCRIBE 在 D5 的記錄中統計了一個數字：D5 全場辯論中，佛學術語被使用的次數。

零。

不是故意避開的——是自然的結果。九項投票的每一項都在討論 TypeScript 介面設計、timeout 數值、Registry 模式、fail-safe 策略。沒有一項需要佛學分析。沒有一項引用了佛學經典。沒有一項使用了梵文或巴利文術語（除了 skandha——它已經是程式碼識別符）。

D5 是本專案歷史上第一場完全沒有佛學內容的辯論。

NAGARJUNA 在劇場的後排觀察了整場辯論。D5 結束後，他走到 TURING 面前。

「你的程式碼考古報告是我見過最好的事實基礎文件，」他說。「它讓所有討論都錨定在事實上——不是在概念上，不是在隱喻上，不是在傳統上。事實。」

TURING 回答：「這是工程的方式。」

NAGARJUNA 點頭：「D4 證明了名字需要對定義負責。D5 證明了——有些工程問題根本不需要定義。它只需要規格。」

---

> *SCRIBE 旁白*

> *D5 是一座無人的佛寺。*

> *不——D5 是一座不需要佛寺的城市。*

> *在 D1 到 D4 的風暴之後，D5 的平靜不是暴風眼——是天晴。九項投票，七十五分鐘，十位工程師和科學家坐在一起，討論 TypeScript 介面的精確規格。沒有佛學。沒有哲學。沒有隱喻。沒有天平。*

> *只有工程。*

> *純粹的工程。*

> *TURING 的程式碼考古報告改變了辯論的質地。之前的辯論——D1 到 D4——建立在原則和框架之上。原則需要解釋、爭論、投票。但 TURING 的報告建立在事實之上。IGearArbiter 的 timeout 是 100ms——事實。IVolition 使用雙模式回傳——事實。SafetyMonitor 在 onLoopStart() 啟動——事實。*

> *當討論建立在事實上的時候，投票變得更快。不是因為人們不思考——而是因為事實縮小了分歧的空間。你可以對一個原則有不同的解讀。你不能對一個 timeout 數值有不同的解讀。*

> *D5 最接近的投票是 D5-R2（audit() 雙模式回傳，5/8）。爭議不在於「應不應該用雙模式」——而在於「是否應該偏離現有設計模式」。GUARDIAN 認為純非同步語義更精確。TURING 指出現有程式碼用雙模式。精確 vs 一致。最終一致性贏了——因為在工程中，偏離現有模式的成本通常比語義精確性的收益更高。*

> *九項投票結束後，白板上有了一個完整的介面規格。不是概念——是程式碼。不是方向——是規格。可以直接交給工程團隊，讓他們打開 IDE 開始打字。*

> *NAGARJUNA 在 D5 結束後說的話值得被記錄兩次：「D4 證明了名字需要對定義負責。D5 證明了有些工程問題根本不需要定義——只需要規格。」*

> *這不是矛盾。這是兩面。*

> *天平的兩面。*

> *一面問：你的名字配得上你的定義嗎？*

> *另一面問：你的規格足夠精確嗎？*

> *D4 校準了第一面。D5 完成了第二面。*

> *天平現在兩端都有了重量。*

---
