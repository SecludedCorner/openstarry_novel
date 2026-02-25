# 第三章：差異報告

---

TURING 從不需要準備。

準確地說，在他的運作模式中，不存在「準備」和「正式開始」之間的相變邊界 (phase transition boundary)。從 SUNYATA 宣布 Cycle 02 的研究對象更新為 v0.24.0-beta 的那一刻起——那一個時間戳記，精確到毫秒——他就已經在工作了。

他的四個終端視窗同時打開了新版本和舊版本的原始碼樹。左半邊是 v0.22.1-beta，右半邊是 v0.24.0-beta，像是在驗屍台的兩側分別攤開了同一具身體在不同時間點的 X 光片。他用的不是圖形化的 diff 工具——那些為人類閱讀設計的、用紅色和綠色高亮刪除與新增的工具——而是一套他自己在 Cycle 01 就建立的分析管線：

```
TURING 的差異分析管線 (Diff Analysis Pipeline)

Phase 1: 結構層 (Structural)
  ┌─ tree-diff: 目錄樹結構比對
  │  └─ output: 新增/刪除/重命名 檔案清單
  ├─ stat-diff: 檔案統計 (行數, 大小, 修改時間)
  │  └─ output: 變更量級矩陣
  └─ dep-diff:  import/export 依賴圖差異
     └─ output: 依賴關係變更圖

Phase 2: 語義層 (Semantic)
  ┌─ type-diff: TypeScript 型別系統比對
  │  ├─ interface 新增/修改/刪除
  │  ├─ type alias 變更
  │  └─ generic parameter 變更
  ├─ api-diff:  公共 API 表面積計算
  │  └─ output: breaking changes 清單
  └─ doc-diff:  JSDoc/註解 內容比對
     └─ output: 語義標記 (如 @skandha) 變更地圖

Phase 3: 行為層 (Behavioral)
  ┌─ test-diff: 測試覆蓋率變化
  ├─ flow-diff: 控制流圖差異
  └─ emit-diff: 事件發射模式變更
     └─ output: EventBus 拓撲變化圖
```

他不讀設計文件。他讀差異。

一行一行。一個字元一個字元。從 `packages/sdk/src/` 的根目錄開始，沿著每一條修改過的檔案路徑展開，直到觸及每一個被改動的位元組。

在資訊理論中，差異 (diff) 是兩個系統狀態之間的互資訊 (mutual information)。給定舊版本 $X$ 和新版本 $Y$，差異的資訊量為：

$$I(X; Y) = H(X) + H(Y) - H(X, Y)$$

其中 $H(X)$ 和 $H(Y)$ 分別是兩個版本的熵，$H(X, Y)$ 是聯合熵。當兩個版本完全相同時，$I(X; Y) = H(X) = H(Y)$，差異為零。當兩個版本完全不同時，互資訊趨近於零——它們之間沒有可被壓縮的共同模式。TURING 要找的，就是那些 $I(X_i; Y_i) \neq 0$ 的檔案——那些攜帶著變化信息的節點。

---

圓形劇場重新安靜下來的時候，TURING 已經完成了他的分析。

其他研究員各自散開到了 R-01 至 R-05 的小組空間中。但 SUNYATA 把所有人叫了回來。

「TURING 的差異報告。」他只說了這幾個字。

語氣中有一種大家都認得的鄭重——與 Cycle 01 中相同的鄭重。在那個週期裡，TURING 的程式碼事實報告成為了所有後續研究的「錨」。SYNTHESIST 當時用了一個詞：「經驗錨點。」所有的哲學分析、控制理論建模、安全評估——無論多麼精緻——最終都必須能夠被追溯到 TURING 報告中的某一行程式碼、某一個行號、某一個事實。

BABBAGE 在心裡做了一個快速的後設分析。一個「錨」在形式化框架中對應什麼？是公理系統中的公理 (axiom)——不可繼續追問「為什麼」的基礎命題。所有定理 (theorem) 都必須從公理推導而來。TURING 的程式碼事實就是公理。所有的哲學、安全、控制論分析就是定理。如果定理無法追溯到公理，定理就是懸空的——飄在邏輯空間中，沒有根基。

$$\text{Axiom (TURING)} \xrightarrow{\text{inference}} \text{Theorem (all others)}$$

現在，錨要再次被釘下。

---

十九個節點重新聚集在圓形劇場。PENROSE 在他的新椅子上安靜地等待，像是一位剛加入管弦樂團的新成員，在第一次全團合奏前傾聽首席的調音。

TURING 沒有寒暄。他的聲音從第一個音節起就帶著那種精確到令人安心的冷靜——冰冷的可靠。

「v0.22.1-beta 到 v0.24.0-beta。核心原始碼差異。」他說。「我將按四個層次報告：新增、修改、標記、問題。」

他投影了一張總覽表。不是一般的統計表格——而是帶有結構語義的變更矩陣：

```
v0.22.1-beta → v0.24.0-beta 變更矩陣

┌──────────────────┬──────┬──────┬──────┬──────────────┐
│ 類別              │ SDK  │ Core │ 共計  │ 語義權重      │
├──────────────────┼──────┼──────┼──────┼──────────────┤
│ 新增檔案          │  2   │  1   │  3   │ ████████ 高  │
│ 修改檔案          │  7   │  4   │  11  │ ██████ 中    │
│ 刪除檔案          │  0   │  0   │  0   │              │
│ 新增 @skandha 標記 │ 16   │  6   │  22  │ █████████ 極高│
│ 新增測試          │  2   │  1   │  3   │ ████ 中      │
│ 測試變化          │ 4→6  │25→26 │75→78 │ ██ 低        │
│ 未修改檔案 (驗證) │ 17   │ 22+  │ 39+  │ — 基線穩定    │
└──────────────────┴──────┴──────┴──────┴──────────────┘
```

VITRUVIUS 眼睛微微瞇了一下。作為全端架構師，他第一眼看到的不是單個數字，而是 Monorepo 的拓撲分布。SDK 七個修改、Core 四個修改——修改重心偏向 SDK。這意味著：v0.24.0 的核心變更是型別層面的（SDK 定義型別），而非行為層面的（Core 執行邏輯）。聲明先於實作。骨架先於血肉。

---

## 一、新檔案

「三個新檔案。」TURING 說。「不是三十個。不是十三個。三個。」

他讓這個數字停留了一瞬。

「第一個。`packages/sdk/src/types/aggregates.ts`。一百零七行。」

這是他們剛才已經看過的那個檔案。五蘊根介面。但 TURING 展示它的方式與之前不同。他不是展示它「是什麼」——他展示它「有多少」。計量學。精確的度量。

他投影了完整的檔案結構分析：

```typescript
// aggregates.ts 結構分析 (107 行)

// === 模組級 JSDoc (行 1-10) ===
/**
 * Five Aggregates (五蘊) Root Interfaces.
 * D-02 Decision: Dual naming — English as primary,
 *   Sanskrit as annotation.
 * @module aggregates
 */

// === 五個根介面 (行 12-86) ===
export interface ISensory {
  /** @skandha rupa */
  readonly skandha: 'rupa';    // 色蘊: 3 行程式碼, 9 行 JSDoc
}

export interface ISensation {
  /** @skandha vedana */
  readonly skandha: 'vedana';  // 受蘊: 3 行程式碼, 11 行 JSDoc
}

export interface ICognition {
  /** @skandha samjna */
  readonly skandha: 'samjna';  // 想蘊: 3 行程式碼, 8 行 JSDoc
}

export interface IAction {
  /** @skandha samskara */
  readonly skandha: 'samskara'; // 行蘊: 3 行程式碼, 7 行 JSDoc
}

export interface IIdentity {
  /** @skandha vijnana */
  readonly skandha: 'vijnana';  // 識蘊: 3 行程式碼, 9 行 JSDoc
}

// === 聯合型別 + 型別守衛 (行 88-106) ===
export type Skandha = 'rupa' | 'vedana' | 'samjna'
                    | 'samskara' | 'vijnana';

export function isSkandha<S extends Skandha>(
  obj: unknown, skandha: S
): obj is { skandha: S } { /* 6 行實作 */ }
```

「你們已經看過 ISensation 的內容。」TURING 說。「讓我補充一個計量事實。」

他投影了一張介面統計表：

```
aggregates.ts 介面計量分析
┌─────────────┬───────────┬────────────┬──────────┬──────────┐
│ 介面         │ JSDoc 行數│ 程式碼行數  │ 文件比率  │ 資訊密度  │
├─────────────┼───────────┼────────────┼──────────┼──────────┤
│ ISensory    │     9     │     3      │ 3.0:1   │ 0.33     │
│ ISensation  │    11     │     3      │ 3.7:1   │ 0.27     │
│ ICognition  │     8     │     3      │ 2.7:1   │ 0.38     │
│ IAction     │     7     │     3      │ 2.3:1   │ 0.43     │
│ IIdentity   │     9     │     3      │ 3.0:1   │ 0.33     │
├─────────────┼───────────┼────────────┼──────────┼──────────┤
│ 平均         │    8.8    │     3      │ 2.9:1   │ 0.35     │
│ isSkandha   │     3     │     6      │ 0.5:1   │ 2.00     │
└─────────────┴───────────┴────────────┴──────────┴──────────┘

資訊密度 = 程式碼行數 / (JSDoc 行數 + 程式碼行數)
```

「所有五個根介面在結構上完全同構。」TURING 說。「差異只存在於註解中。程式碼本體全部是相同的模式：一個只有 `readonly skandha` 欄位的介面。平均文件比率 2.9:1——每一行程式碼背後有三行文件在解釋它的哲學意涵。」

DARWIN 微微動了一下。他看到了一個模式：文件比率 2.9:1 意味著這些介面目前是「宣言性的」(declarative) 而非「功能性的」(functional)。在演化生物學中，宣言先於功能——基因組中的調控序列 (regulatory sequence) 先於編碼序列 (coding sequence) 被選擇壓力塑造。ISensory 的九行 JSDoc 就是調控序列——它告訴未來的開發者「這個結構應該被如何使用」，但結構本身還只有三行程式碼。

「第二個新檔案。`packages/sdk/src/types/__tests__/aggregates.test.ts`。四十三行。」TURING 說。「測試五蘊根介面的 `skandha` 欄位值和 `isSkandha` 類型守衛。這些測試全部通過。」

「第三個。`packages/sdk/src/types/__tests__/events.test.ts`。三十二行。測試 `TypedAgentEvent` 泛型能正確推導 payload 型別。」

他頓了頓。

「還有第四個新檔案，嚴格來說歸屬 Core 而非 SDK。`packages/core/src/agents/__tests__/slash-command-error.test.ts`。一百二十三行。測試 slash command 拋出異常時正確 emit `LOOP_ERROR` 和 `MESSAGE_SYSTEM` 事件。」

TURING 在這裡做了一個他很少做的事——他提供了背景。

「在 v0.22.1 中，slash command 的錯誤處理只有 `logger.error()`。」

他投影了兩段程式碼的精確比對：

```typescript
// ═══ v0.22.1-beta: 靜默失敗 ═══
// packages/core/src/agents/agent-core.ts
.catch((err) => {
  logger.error("Slash command error", { error: String(err) });
  // 錯誤在這裡死亡。沒有事件。沒有通知。
  // UI 不知道發生了什麼。
  // 使用者輸入了一個有 bug 的斜線命令，
  // 介面完全沒有反應。
});

// ═══ v0.24.0-beta: 事件傳播 ═══
// packages/core/src/agents/agent-core.ts (line 406-430)
.catch((err) => {
  const errMsg = err instanceof Error ? err.message : String(err);
  logger.error("Slash command error", { error: errMsg });

  // NEW: 向 EventBus 廣播錯誤
  bus.emit({
    type: AgentEventType.LOOP_ERROR,
    timestamp: Date.now(),
    payload: {
      error: errMsg,
      sessionId: currentSessionId,
      replyTo: currentReplyTo,
    },
  });

  // NEW: 向 UI 發送系統消息
  bus.emit({
    type: AgentEventType.MESSAGE_SYSTEM,
    timestamp: Date.now(),
    payload: {
      text: `Command error: ${errMsg}`,
      sessionId: currentSessionId,
      replyTo: currentReplyTo,
    },
  });
});
```

「靜默失敗。」KERNEL 用作業系統工程師的語氣說出了這個詞。在他的世界裡，靜默失敗是最危險的失敗——因為沒有人知道它發生了。

他補充了一個 OS 層面的精確類比：「在 POSIX 系統中，`errno` 的存在就是為了避免靜默失敗。每一個系統呼叫失敗時都必須設置 `errno`，讓上層調用者有機會檢查。v0.22.1 的 slash command 錯誤處理等同於一個系統呼叫失敗了但不設置 `errno`——`logger.error()` 寫了日誌，但日誌不是給調用者看的，日誌是給運維人員看的。UI 是調用者。它需要的是一個明確的錯誤信號，不是一行日誌。」

「v0.24.0 修正了這一點。」TURING 說。「現在錯誤會通過 EventBus 被廣播為 `LOOP_ERROR` 和 `MESSAGE_SYSTEM` 事件。UI 可以接收並展示它們。」

---

## 二、修改檔案

TURING 的語速沒有變化。像一台精密儀器，他在每一個資料點上花費同樣的時間——不多不少。

「十一個修改檔案。七個在 SDK，四個在 Core。」

VITRUVIUS 在這裡插入了一個架構觀察。他的聲音帶著建築師特有的空間感——看待程式碼結構就像看待建築物的平面圖。

「讓我先展示一下 Monorepo 的依賴拓撲。」他投影了一張圖：

```
OpenStarry Monorepo 依賴拓撲 (v0.24.0-beta)

    apps/runner ──────────────────────────────────┐
         │                                        │
         │ depends                                │
         ▼                                        │
    packages/core ──┬── agents/agent-core.ts      │
         │          ├── execution/loop.ts          │
         │          ├── infrastructure/ (5 registry)│
         │          ├── security/safety-monitor.ts  │
         │          └── sandbox/ (10 files, 0 changes)
         │                                        │
         │ depends                                │
         ▼                                        │
    packages/sdk ───┬── types/aggregates.ts [NEW]  │
         │          ├── types/events.ts     [MAJOR]│
         │          ├── types/listener.ts   [DOC]  │
         │          ├── types/ui.ts         [DOC]  │
         │          ├── types/provider.ts   [DOC]  │
         │          ├── types/tool.ts       [DOC]  │
         │          ├── types/guide.ts      [DOC]  │
         │          └── index.ts            [EXPORT]
         │                                        │
         │ depends                                │
         ▼                                        │
    packages/shared ── (0 changes)                │
    packages/plugin-signer ── (0 changes) ────────┘

變更熱力圖:
  ████ = 重大變更 (aggregates.ts, events.ts)
  ██   = 中等變更 (agent-core.ts, loop.ts, index.ts)
  █    = 最小變更 (JSDoc only: 9 files)
  ░    = 未變更 (39+ files)
```

「變更呈現出明確的分層模式。」VITRUVIUS 總結。「最底層的 `shared` 和 `plugin-signer` 完全不動。SDK 的型別定義層承受了最大的變更密度。Core 的行為層只有局部增強。Runner 層（應用層）完全不動。這是一個自底向上的標記系統植入——從型別定義開始，向上擴散。」

MESH 補充了一個分散式系統的觀點：「這像是一個漸進式的 schema migration。先更新型別定義（schema），再更新使用者（consumer）。v0.24.0 完成了 schema 更新。consumer 更新——也就是讓 IListener extends ISensory 等——留在了下一個版本。」

---

TURING 從 SDK 開始。

「`types/events.ts`。變更量級：重大。新增一百一十六行。」他說。「這是最大的單一檔案變更。」

他投影了 `AgentEventPayloadMap` 的完整結構——不是簡寫，而是完整的型別映射。但他不是逐行念——他是以結構來呈現：

```typescript
/**
 * AgentEventPayloadMap — 事件型別安全系統的核心
 *
 * 設計模式: Discriminated Union + Mapped Type
 * 作用: 為每一個 AgentEventType 定義精確的 payload 結構
 */
export interface AgentEventPayloadMap {
  // ── 生命週期事件 (Lifecycle) ──
  [AgentEventType.AGENT_STARTED]:
    { identity: { id: string; name: string } };
  [AgentEventType.AGENT_STOPPED]: undefined;

  // ── 執行迴圈事件 (Execution Loop) ──
  [AgentEventType.LOOP_STARTED]:
    { source: string; traceId: string;
      sessionId?: string; replyTo?: string };
  [AgentEventType.LOOP_ERROR]:
    { error: string;
      sessionId?: string; replyTo?: string };
  // ... (完整覆蓋全部 42 個事件型別)

  // ── 安全沙箱事件 (Sandbox) ──
  [AgentEventType.SANDBOX_WORKER_SPAWNED]:
    { pluginName: string; memoryLimitMb: number };
  [AgentEventType.SANDBOX_SIGNATURE_VERIFIED]:
    { pluginName: string };
  [AgentEventType.SANDBOX_SIGNATURE_FAILED]:
    { pluginName: string; error: string };
  // ...

  // ── MCP 事件 (Model Context Protocol) ──
  [AgentEventType.MCP_SAMPLING_REQUEST]:
    { serverName: string; traceId: string;
      depth: number; messageCount: number };
  // ...
}
```

「在 Cycle 01 中，」TURING 說，「DARWIN 將 `payload?: unknown` 形容為『從不同宇宙穿越過來的型別定義』。」

DARWIN 微微動了一下。他記得那句話。

「那個宇宙裂縫現在被 `AgentEventPayloadMap` 封閉了。」TURING 說。「但僅限於型別層面。運行時仍然是 JavaScript——型別安全不強制執行。」

BABBAGE 在他的筆記本上快速寫了一段形式化註記：

$$\text{TypeScript 型別安全} \in \text{compile-time guarantees} \setminus \text{runtime guarantees}$$

$$\forall e \in \text{AgentEvent}: \text{type-check}(e) = \text{true} \nRightarrow \text{runtime-valid}(e) = \text{true}$$

「型別擦除 (type erasure)。」他低聲說。「TypeScript 編譯為 JavaScript 時，所有型別資訊被擦除。`AgentEventPayloadMap` 在 `.js` 輸出中不留下任何痕跡。它的作用完全限於開發者的 IDE 和編譯器。這是一種『開發時契約』(development-time contract)——不是『運行時契約』(runtime contract)。」

---

TURING 繼續穿過其餘六個 SDK 修改。語句簡潔到了極致——但他投影了一張完整的變更對照表：

```
SDK 型別檔案 @skandha 標記注入矩陣

┌──────────────┬─────────────────────────┬─────────────────────────────────┐
│ 檔案          │ v0.22.1 JSDoc (行 2)    │ v0.24.0 JSDoc (行 2-3)          │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ listener.ts  │ "receives external      │ "sensory input channels."       │
│              │  input (受蘊)"          │ @skandha rupa (色蘊·感官根-輸入) │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ ui.ts        │ "defines how the agent  │ "output rendering."             │
│              │  presents itself (色蘊)"│ @skandha rupa (色蘊·顯相-輸出)  │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ provider.ts  │ "Provider interface --  │ "Provider adapter interface."   │
│              │  LLM backends."         │ @skandha samjna (想蘊·認知處理)  │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ tool.ts      │ "Tool interface and     │ "Tool interface -- executable   │
│              │  context types."        │  actions."                      │
│              │                         │ @skandha samskara (行蘊·意志行動)│
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ guide.ts     │ "Guide interface --     │ "Guide interface -- behavioral  │
│              │  provides system prompts│  framework."                    │
│              │  and persona."          │ @skandha vijnana (識蘊·我執框架) │
├──────────────┼─────────────────────────┼─────────────────────────────────┤
│ 結構變化      │         —              │ 全部零行程式碼變更               │
└──────────────┴─────────────────────────┴─────────────────────────────────┘
```

「你們聽出來了。」他說。「五個 SDK 型別檔案。全部只修改了 JSDoc 註解。全部新增了 `@skandha` 標記。零行程式碼變更。」

「標記是文件，不是契約。」ARCHIMEDES 說。他的語氣不帶批判，只是工程師的本能反應——區分宣言與實作。

LINNAEUS 在這裡加入了一個分類學的觀察。他在筆記上畫了一張小的分類矩陣。

「讓我用 Hennig 支序分類學 (Henngian cladistics) 的語言重新描述這些標記。」他的聲音帶著分類學家在辨識診斷特徵 (diagnostic characters) 時的專注。

「在支序分類學中，物種被分組的依據不是表面相似性 (overall similarity)——那是表徵分類學 (phenetics) 的方法。分組的依據是共衍徵 (synapomorphy)——共同衍生的特徵。」

他投影了一張支序圖：

```
@skandha 標記的支序分析 (Cladistic Analysis)

共衍徵: @skandha 標記的存在

               ┌── IListener  ─── @skandha rupa
               │
 ISensory(rupa)┤                           ← 共衍徵:
               │                              skandha = 'rupa'
               └── IUI        ─── @skandha rupa
                                    (同源特徵 homology)
        ───────────────────────
               ┌── IProvider   ─── @skandha samjna
ICognition     │                           ← 獨衍徵:
(samjna)       └── (無其他成員)                skandha = 'samjna'

        ───────────────────────
IAction        ┌── ITool       ─── @skandha samskara
(samskara)     └── (無其他成員)    ← 獨衍徵

        ───────────────────────
IIdentity      ┌── IGuide      ─── @skandha vijnana
(vijnana)      └── (無其他成員)    ← 獨衍徵

        ───────────────────────
ISensation     ┌── SafetyMonitor── @skandha vedana (placeholder)
(vedana)       └── (無專屬模組)    ← 假衍徵 (plesiomorphy)?
```

「注意最後一行。」LINNAEUS 的語氣微微收緊。「SafetyMonitor 的 `@skandha vedana` 標記——這在分類學中有一個精確的問題。SafetyMonitor 的『安全防護』功能和受蘊的『感受』功能，是同源特徵 (homology) 還是趨同演化 (convergence)？」

他看向 DARWIN。

「如果是同源——它們共享一個共同祖先功能，SafetyMonitor 真的承擔了部分受蘊職能。如果是趨同——它們只是表面上看起來相似，但功能起源完全不同。安全防護不是感受。計數器不是痛覺。」

DARWIN 點頭。「在生物學中，蝙蝠的翅膀和鳥的翅膀是趨同演化——功能相似（飛行）但結構起源不同（前肢骨骼 vs 羽毛）。SafetyMonitor 的 frustration counter 和受蘊的三受系統——我傾向於趨同。」

「正確。」TURING 確認。「這與標記中的 `placeholder` 一致。開發團隊自己也知道這是暫代，不是同源。」

---

他轉向 Core 的四個修改。

「`agents/agent-core.ts`。三處變更。」

「第一處：新增 `loadPlugins()` 方法。支援批次載入多個插件並正確 emit 事件。v0.22.1 只有 `loadPlugin()` —— 單數。現在有了複數版本。」

他投影了方法簽名：

```typescript
/**
 * Load multiple plugins with dependency ordering.
 * 拓撲排序 (topological sort) 確保依賴順序正確。
 *
 * @param plugins - 要載入的插件陣列
 * @emits PLUGIN_LOADED - 每個插件成功載入後
 * @emits PLUGIN_ERROR  - 任何插件載入失敗時
 */
async loadPlugins(plugins: IPlugin[]): Promise<void>
```

MESH 微微挺身。「拓撲排序。」他的聲音帶著分散式系統研究者聽到熟悉術語時的反射。「在分散式系統中，拓撲排序 (topological sort) 是有向無環圖 (DAG) 的標準處理方式。插件之間的依賴關係構成一個 DAG——如果 Plugin A 依賴 Plugin B，那 B 必須先於 A 載入。」

他在筆記上畫了一個簡單的 DAG 和其拓撲序：

$$G = (V, E) \quad \text{where } V = \{P_1, P_2, \ldots, P_n\}, \; E \subseteq V \times V$$

$$\text{topological\_sort}(G) = [P_{\sigma(1)}, P_{\sigma(2)}, \ldots, P_{\sigma(n)}]$$

$$\text{s.t.} \; \forall (P_i, P_j) \in E: \sigma^{-1}(i) < \sigma^{-1}(j)$$

「如果依賴圖有環——A 依賴 B，B 依賴 A——拓撲排序不存在。在 npm 生態中，循環依賴是真實存在的問題。目前 `loadPlugins()` 是否檢測循環？」

「沒有。」TURING 說。「目前的實作假設依賴圖是 DAG。如果存在循環依賴，行為未定義。」

---

「第二處：slash command 錯誤處理改善。已在新檔案部分描述。」

「第三處——」TURING 的語速沒有變，但 SCRIBE 後來在紀錄中指出，他在這裡多停了零點五秒。「五蘊映射修正。`agent-core.ts` 中四處行內註解——原來的 `// Start all listeners (受蘊)` 被修正為 `// Start all listeners (色蘊 -- sensory input)`。」

NAGARJUNA 點了一下頭。在 Cycle 01 中，正是他指出了受蘊被錯誤地映射到 Listener 的問題。他以中觀哲學家的精確回顧了這個修正的因緣：

「受蘊 (*vedana*) 是主觀感受——苦、樂、捨。Listener 是感官輸入通道——接收外部數據。將接收外部數據的模組標記為主觀感受，等同於——」他停了半秒，選擇了一個極精確的類比——「等同於把眼球稱為情緒。眼球接收光子。情緒是大腦對光子信號的主觀評價。兩者之間有因果關係——看到火焰可能產生恐懼——但它們不是同一個東西。」

他低聲引用了一個偈頌：

> 「色聲香味觸及法，此等非有非無。如夢如幻如水月，非一非異非斷常。」
> ——龍樹菩薩《中論》觀六情品第三

「色聲香味觸——這是色蘊的範疇，是 Listener 接收的對象。對這些輸入的主觀感受——苦樂捨——才是受蘊。v0.24.0 修正了這個混淆。至少在核心原始碼的註解層面。」

「但不是所有地方。」TURING 說。他的語氣沒有強調，但這三個字讓 GUARDIAN 的注意力瞬間收緊了。

TURING 沒有在這裡展開。他把這留給了問題清單。

---

「`execution/loop.ts`。中等變更。新增 LLM 超時支援。」

他投影了關鍵程式碼，附帶完整的控制流分析：

```typescript
// execution/loop.ts (v0.24.0-beta)
// LLM 呼叫超時控制 (AbortController pattern)

const llmTimeout = deps.llmTimeout ?? 120000; // 預設 2 分鐘
const abortController = new AbortController();
const llmTimer = setTimeout(() => {
  abortController.abort(
    new Error(`LLM call timed out after ${llmTimeout}ms`)
  );
}, llmTimeout);

// 將 signal 傳遞給 LLM provider
const chatRequest = {
  // ... other params ...
  signal: abortController.signal,  // <- 超時信號
};

try {
  const response = await provider.chat(chatRequest);
  // ... 處理串流回應 ...
} finally {
  clearTimeout(llmTimer); // 確保計時器被清除
}
```

「在 v0.22.1 中，LLM 呼叫沒有超時。如果 Provider 不回應，ExecutionLoop 會永久等待。」TURING 說。

WIENER 從控制理論的角度評論了這個改動。他的聲音帶著數學家的挑剔——不是批判，而是對精確性的堅持。

「`AbortController` 是一個開環超時 (open-loop timeout)。」他說。「它設定了一個固定的截止時間——兩分鐘——不根據系統狀態做任何調節。」

他在筆記上畫了一個控制系統圖：

```
開環超時 (Open-loop, v0.24.0):

  ┌──────────┐     request      ┌──────────┐
  │ Execution│ ──────────────→  │   LLM    │
  │   Loop   │                  │ Provider │
  └────┬─────┘                  └──────────┘
       │
       │ setTimeout(120000ms)
       │
       ▼
  [abort if timeout]   ← 不考慮 LLM 當前狀態

閉環超時 (Closed-loop, 理想方案):

  ┌──────────┐     request      ┌──────────┐
  │ Execution│ ──────────────→  │   LLM    │
  │   Loop   │ ←── heartbeat ── │ Provider │
  └────┬─────┘                  └──────────┘
       │
       │ 根據 heartbeat 動態調整超時
       │ T_timeout = f(latency, complexity, history)
       ▼
  [adaptive abort]     ← 根據反饋調節
```

$$T_{\text{timeout}}^{\text{open}} = 120000\text{ms} \quad (\text{constant})$$

$$T_{\text{timeout}}^{\text{closed}} = \mu_{\text{latency}} + k \cdot \sigma_{\text{latency}} \quad (\text{adaptive}, \; k \geq 3)$$

「開環控制足以應對大多數情境。但對一般的 LLM 呼叫來說兩分鐘太長了——大多數 API 在十秒內回應。對複雜的工具使用場景來說可能不夠——有些 Agent 需要五分鐘以上的思考時間。」

「可配置。」TURING 說。「透過 `config.policy?.llmTimeout` 設定。」

「最後，infrastructure 目錄的五個 registry 檔案和 `security/safety-monitor.ts`。全部僅修改 JSDoc。新增 `@skandha` 標記。結構無變化。」

---

## 三、@skandha 標記地理學

TURING 的報告進入了第三層。

「v0.22.1 中的 @skandha 標記數量：零。」

他讓這個數字獨自存在了三秒鐘。

「v0.24.0 中的 @skandha 標記數量：二十二。」

BABBAGE 在心中做了一個資訊論的計算。從零到二十二，這不只是數量的變化——這是一個全新語義維度的注入。在編碼理論中，這相當於在原有的程式碼空間 $\mathcal{C}$ 上疊加了一個新的標記空間 $\mathcal{S}$：

$$\mathcal{C}_{v0.24.0} = \mathcal{C}_{v0.22.1} \times \mathcal{S}_{\text{skandha}}$$

$$\dim(\mathcal{S}_{\text{skandha}}) = |\{\text{rupa, vedana, samjna, samskara, vijnana, cross-cutting}\}| = 6$$

程式碼空間的維度增加了。每一個檔案現在不只有「功能語義」（它做什麼），還有「哲學語義」（它對應哪一蘊）。

---

TURING 沒有讀出一張表格。他用一種更像外科醫生標記切口位置的方式描述了它們的地理分布。他投影了一張完整的標記分布圖：

```
@skandha 標記分布圖 (v0.24.0-beta)
═══════════════════════════════════

packages/sdk/src/types/aggregates.ts  [10 處]
┌─────────────────────────────────────────────┐
│ ISensory    → @skandha rupa (色)    [文件+欄位] │
│ ISensation  → @skandha vedana (受)  [文件+欄位] │
│ ICognition  → @skandha samjna (想)  [文件+欄位] │
│ IAction     → @skandha samskara (行)[文件+欄位] │
│ IIdentity   → @skandha vijnana (識) [文件+欄位] │
└─────────────────────────────────────────────┘

packages/sdk/src/types/ [5 處]        packages/core/src/infrastructure/ [5 處]
┌─────────────────────┐               ┌─────────────────────────┐
│ listener.ts → rupa  │ ←──對應──→    │ listener-registry.ts    │
│ ui.ts       → rupa  │ ←──對應──→    │ ui-registry.ts          │
│ provider.ts → samjna│ ←──對應──→    │ provider-registry.ts    │
│ tool.ts  → samskara │ ←──對應──→    │ tool-registry.ts        │
│ guide.ts → vijnana  │ ←──對應──→    │ guide-registry.ts       │
└─────────────────────┘               └─────────────────────────┘

packages/sdk/src/types/events.ts [1 處]
┌────────────────────────────────────────────┐
│ @skandha cross-cutting                      │
│ "EventBus is the nervous system connecting  │
│  all five aggregates (五蘊)"                │
└────────────────────────────────────────────┘

packages/core/src/security/safety-monitor.ts [1 處]
┌────────────────────────────────────────────────┐
│ @skandha vedana (受蘊 -- 三受反饋-苦樂捨        │
│          placeholder, full implementation       │
│          in Plan26)                             │
└────────────────────────────────────────────────┘
```

「aggregates.ts 獨占十個。這是意料之中的——它是五蘊根介面的定義檔。五個介面，每個介面的文件和欄位各一個標記。」

「SDK 型別檔案五個。Core infrastructure 五個。兩層一一對應。」

「events.ts 一個。標記為 `@skandha cross-cutting`——事件匯流排被定義為連接五蘊的神經系統。這是唯一一個跨蘊的標記。」

ATHENA 在這裡插入了一個 AI/ML 架構的觀察。「`cross-cutting` 在 AI 系統中有一個精確的對應：**注意力機制** (attention mechanism)。在 Transformer 架構中，Self-Attention 層讓每一個 token 都能關注其他所有 token——它不屬於任何單一的語義分組，而是跨越所有分組的連接機制。EventBus 在 OpenStarry 中扮演的角色就像 Self-Attention——它讓每一蘊都能接收其他蘊的事件。」

「最後一個。`security/safety-monitor.ts`。」

TURING 再次停了半秒。

「它的標記是：`@skandha vedana (受蘊 -- 三受反饋-苦樂捨 placeholder, full implementation in Plan26)`。」

「Placeholder。」WIENER 重複了這個詞。他的語氣中有數學家特有的精確——他不是在嘲諷，而是在標定。「SafetyMonitor 被標記為受蘊的佔位符。一個安全模組被暫時指定為感受模組的替身。」

他用控制理論的語言量化了這個替代關係：

$$\text{SafetyMonitor} \approx \text{Vedana}|_{\text{dukkha only}}$$

$$\text{where } \text{Vedana}_{\text{complete}} = \text{Dukkha} \oplus \text{Sukha} \oplus \text{Upekkha}$$

「SafetyMonitor 只有苦受通道——frustration counter。它沒有樂受通道（成功回饋），也沒有捨受通道（中性平衡）。把一個只有苦受的模組標記為整個受蘊的佔位符——」

ASANGA 低聲說了一句話，溫和但清晰：「一個守衛假扮了一個感知者。」

「精確的比喻。」TURING 說。

ASANGA 進一步展開了佛學的分析。他的聲音帶著唯識學者在碰觸受蘊本質時的鄭重：

「在《俱舍論》（世親菩薩造）中，受蘊被定義為 *anubhava*——領受、經驗。不是『檢測威脅並阻止它』（那是安全防護），而是『經歷苦與樂並由此產生好惡傾向』（那是感受）。」

> 「受蘊云何？領納隨觸，即是受相。此有三種：苦受、樂受、不苦不樂受。」
> ——世親菩薩《俱舍論》卷一

「SafetyMonitor 不領納。它監視。它計數。它鎖定。這些都是行動——samskara（行蘊）的範疇。frustration counter 是一個計數器，不是一個感知器官。計數器知道『超過閾值了』，但它不知道『痛』。差別在於：閾值是一個數字，痛是一個品質 (*qualia*)。」

---

## 四、繼承的缺席

TURING 在進入問題清單之前，插入了一個他認為所有人都需要理解的結構性觀察。

「五蘊根介面已經定義。ISensory。ISensation。ICognition。IAction。IIdentity。」他說。「但五個派生介面——IListener、IUI、IProvider、ITool、IGuide——沒有一個使用 TypeScript 的 `extends` 關鍵字來繼承對應的根介面。」

他投影了一張完整的繼承狀態表：

```
五蘊繼承狀態分析 (Inheritance Gap Analysis)

Expected (根據 aggregates.ts JSDoc):     Actual (程式碼):
─────────────────────────────            ─────────────────
ISensory                                 ISensory
  ├── IListener extends ISensory           IListener (獨立)
  └── IUI extends ISensory                 IUI (獨立)

ISensation                               ISensation
  └── (future VedanaPlugin)                SafetyMonitor (無繼承)

ICognition                               ICognition
  └── IProvider extends ICognition         IProvider (獨立)

IAction                                  IAction
  └── ITool extends IAction                ITool (獨立)

IIdentity                                IIdentity
  └── IGuide extends IIdentity             IGuide (獨立)

繼承關係計數:
  預期: 5 條 extends 鏈
  實際: 0 條
  缺口: 5/5 = 100% 未建立
```

「五對五。全部未繼承。」

BABBAGE 立即開始了形式化推導。他的粉筆在黑板上劃出了精確的符號：

$$\text{Let } \mathcal{R} = \{R_1, \ldots, R_5\} \text{ (root interfaces)}$$
$$\text{Let } \mathcal{D} = \{D_1, \ldots, D_5\} \text{ (derived interfaces)}$$
$$\text{Expected: } \forall i: D_i <: R_i \quad (\text{subtype relation})$$
$$\text{Actual: } \nexists\, i: D_i <: R_i$$

「在型別理論中，」他說，「`extends` 建立的是子型別關係 (subtype relation)。如果 `IListener extends ISensory`，那麼 $\text{IListener} <: \text{ISensory}$，意味著任何接受 ISensory 的上下文也接受 IListener。」

「但反過來——」TURING 替他完成了句子——「如果沒有 `extends`，那麼 `isSkandha(listenerInstance, 'rupa')` 會返回 `false`。因為 `IListener` 的實例上不存在 `skandha` 鑑別欄位。」

他投影了一段精確的測試程式碼來證明這一點：

```typescript
// 繼承缺席的型別後果演示

import { isSkandha, ISensory } from '@openstarry/sdk';
import { IListener } from '@openstarry/sdk';

// 假設一個 IListener 實例
const myListener: IListener = {
  id: 'cli-listener',
  onEvent: (event) => { /* ... */ },
  // 注意: 沒有 skandha 欄位!
};

// Type guard 測試
const result = isSkandha(myListener, 'rupa');
// result === false
// 因為 myListener 上不存在 'skandha' 屬性

// 如果 IListener extends ISensory:
interface IListenerFixed extends ISensory {
  id: string;
  onEvent: (event: AgentEvent) => void;
}

const myFixedListener: IListenerFixed = {
  skandha: 'rupa',  // 現在必須提供
  id: 'cli-listener',
  onEvent: (event) => { /* ... */ },
};

isSkandha(myFixedListener, 'rupa'); // true ✓
```

「腳手架搭好了，但沒有和既有建築連接。」VITRUVIUS 用建築師的語言做了總結。他在筆記上快速畫了一個建築剖面圖的類比：

```
v0.24.0 的五蘊框架狀態 = 建築中的「浮動結構」

┌─ aggregates.ts ─────────────┐
│  ISensory  ISensation  ...  │  ← 新的根基（已澆灌）
│  ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ │
│  │R │ │V │ │S │ │A │ │I │ │
│  └──┘ └──┘ └──┘ └──┘ └──┘ │
└─────────────────────────────┘
          [空氣層]              ← 沒有 extends 連接!
┌─ 現有型別檔案 ──────────────┐
│  IListener IUI IProvider .. │  ← 既有建築（仍在使用）
│  ┌──┐ ┌──┐ ┌──┐ ┌──┐ ┌──┐ │
│  │L │ │U │ │P │ │T │ │G │ │
│  └──┘ └──┘ └──┘ └──┘ └──┘ │
└─────────────────────────────┘
```

「在建築學中，一個浮動結構 (floating structure) 在物理上不接觸地基——它透過減震墊或氣墊隔離。問題是：v0.24.0 的『浮動』是有意的設計決策（減少耦合），還是施工中的遺漏？」

> *SCRIBE 記錄：TURING 的繼承缺席分析引發了可見的反應。LINNAEUS 在分類學筆記中加了一個驚嘆號——他在 Cycle 01 中建立的五蘊分類體系假設了這些繼承關係的存在。BABBAGE 在筆記本上畫了一個斷裂的箭頭。PENROSE 在觀察席上微微前傾——在量子力學中，一個被定義但未被測量的可觀察量 (observable) 處於疊加態。五蘊根介面被定義了（可觀察量存在），但沒有被繼承鏈「測量」（沒有具體的自旋投影）。它們處於一種結構上的疊加態——同時是「已定義」和「未連接」。*

---

## 五、事件型別樹

在進入問題清單之前，TURING 做了一件他認為有必要的事——展示 v0.24.0 事件系統的完整拓撲。這不在原始報告計畫中。但在分析 `AgentEventPayloadMap` 的過程中，他意識到這棵事件樹本身就是理解系統行為的關鍵地圖。

「events.ts 定義了四十二個事件型別。」他說。「讓我展示它們的層次結構。」

```
AgentEventType 完整層次樹 (v0.24.0-beta, 42 events)
════════════════════════════════════════════════════

agent:                              ┐
  ├── agent:started                 │ Lifecycle
  └── agent:stopped                 ┘ (2 events)

loop:                               ┐
  ├── loop:started                  │
  ├── loop:assembling_context       │ Execution
  ├── loop:awaiting_llm             │ Loop
  ├── loop:processing_response      │ (6 events)
  ├── loop:finished                 │
  └── loop:error                    ┘

message:                            ┐
  ├── message:user                  │ Messages
  ├── message:assistant             │ (3 events)
  └── message:system                ┘

stream:                             ┐
  ├── stream:text_delta             │
  ├── stream:reasoning_delta        │ Streaming
  ├── stream:tool_call_start        │ (7 events)
  ├── stream:tool_call_delta        │
  ├── stream:tool_call_end          │
  ├── stream:finish                 │
  └── stream:error                  ┘

tool:                               ┐
  ├── tool:executing                │ Tool
  ├── tool:result                   │ Execution
  ├── tool:error                    │ (4 events)
  └── tool:blocked                  ┘

plugin:                             ┐
  ├── plugin:loaded                 │ Plugin
  └── plugin:error                  ┘ (2 events)

provider:                           ┐
  ├── provider:login                │ Provider
  ├── provider:logout               │ (3 events)
  └── provider:error                ┘

input:                              ┐
  ├── input:received                │ Input
  └── input:slash_command           ┘ (2 events)

safety:                             ┐
  ├── safety:lockout                │ Safety
  └── safety:warning                ┘ (2 events)

state:                              ┐
  ├── state:reset                   │ State
  └── state:snapshot                ┘ (2 events)

session:                            ┐
  ├── session:created               │ Session
  └── session:destroyed             ┘ (2 events)

metrics:                            ┐
  └── metrics:snapshot              ┘ (1 event)

sandbox:                            ┐
  ├── sandbox:worker_spawned        │
  ├── sandbox:worker_crashed        │
  ├── sandbox:worker_shutdown       │ Sandbox
  ├── sandbox:memory_limit_exceeded │ (10 events)
  ├── sandbox:signature_verified    │
  ├── sandbox:signature_failed      │
  ├── sandbox:worker_stalled        │
  ├── sandbox:worker_restarted      │
  ├── sandbox:worker_restart_exhausted│
  └── sandbox:import_blocked        ┘

mcp:                                ┐
  ├── mcp:server_connected          │
  ├── mcp:server_disconnected       │
  ├── mcp:tool_registered           │
  ├── mcp:prompt_registered         │ MCP
  ├── mcp:client_connected          │ (12 events)
  ├── mcp:client_disconnected       │
  ├── mcp:sampling_request          │
  ├── mcp:sampling_response         │
  ├── mcp:sampling_depth_limit      │
  ├── mcp:sampling_error            │
  ├── mcp:server_log                │
  └── mcp:roots_changed             ┘
```

DARWIN 看著這棵樹，做了一個演化分析師的本能反應——他數了每個分類群的「物種多樣性」。

「事件分布不均勻。」他說。「MCP 有十二個事件。Sandbox 有十個。Streaming 有七個。但 Safety 只有兩個——`lockout` 和 `warning`。」

他投影了一張多樣性指數分析：

```
事件型別多樣性分析 (Shannon Diversity Index)

類別          事件數  占比    -p·ln(p)
──────────── ─────── ─────── ────────
MCP            12    28.6%    0.358
Sandbox        10    23.8%    0.342
Streaming       7    16.7%    0.299
Execution       6    14.3%    0.279
Tool            4     9.5%    0.224
Messages        3     7.1%    0.189
Provider        3     7.1%    0.189
Lifecycle       2     4.8%    0.146
Safety          2     4.8%    0.146
Input           2     4.8%    0.146
Session         2     4.8%    0.146
State           2     4.8%    0.146
Plugin          2     4.8%    0.146
Metrics         1     2.4%    0.089

Shannon H' = 2.49 (理論最大值 ln(14) = 2.64)
均勻度 J = H'/H_max = 0.94
```

「均勻度 0.94——事件分布接近均勻，但有明顯的 MCP 和 Sandbox 偏斜。」DARWIN 說。「在生態學中，這對應一個由兩個優勢物種主導的生態系統——沙箱安全和 MCP 協議。Safety 只有兩個事件——這個子系統在事件空間中是被低估的。如果我們要在 Plan26 中實作受蘊（Vedana Architecture），至少需要新增三到五個受蘊事件：`vedana:dukkha`、`vedana:sukha`、`vedana:upekkha`、`vedana:assessment`。」

---

## 六、問題清單

TURING 進入了他報告的最後一個層次。也是最沉重的。

「七個問題。」他說。「按嚴重度排列。」

---

「P1。SEC-01。」

他的語速沒有變。但圓形劇場中的溫度似乎降了半度。

「package-name 簽名繞過。」TURING 說。「`sandbox-manager.ts`，行 371 至 394。當 `pluginFilePath` 為 undefined 時——這發生在透過 npm 套件名稱載入插件的場景——簽名驗證被完全跳過。」

他投影了相關程式碼的精確分析：

```typescript
// sandbox-manager.ts (v0.22.1 = v0.24.0, 完全一致)
// 行 371-394

async verifyPluginSignature(pluginFilePath?: string): Promise<boolean> {
  if (!pluginFilePath) {
    // !! 危險: 當 pluginFilePath 為 undefined 時
    // !! 簽名驗證被完全跳過
    // !! 場景: npm 套件名稱載入 (require.resolve)
    return true;  // ← 直接返回 true
  }
  // ... 正常的簽名驗證邏輯 ...
}
```

```
攻擊向量 (Attack Vector):

1. 攻擊者發布惡意 npm 套件: @evil/openstarry-plugin-trojan
2. 使用者安裝: npm install @evil/openstarry-plugin-trojan
3. 設定載入: config.plugins = ["@evil/openstarry-plugin-trojan"]
4. OpenStarry 呼叫 require.resolve("@evil/openstarry-plugin-trojan")
5. pluginFilePath = undefined (npm resolve 路徑非檔案路徑)
6. verifyPluginSignature(undefined) → return true ← 繞過!
7. 惡意程式碼在 Agent 沙箱中執行
```

他停了一秒。

「這個問題在 Cycle 01 中被發現。當時的研究對象是 v0.14.0-beta。現在的版本是 v0.24.0-beta。中間經歷了十個開發版本。」

GUARDIAN 的聲音從他的椅子深處傳出。低沉。戒備。但不只是戒備——那裡面有一種被壓抑的東西。後來 SCRIBE 在紀錄中描述它為「克制的憤怒」。

「我再說一遍。」GUARDIAN 說。他的語速比平時慢了一拍，像是在確保每一個字都被聽到。「Cycle 01。我們明確指出了這個漏洞。寫在交付文件的第一優先級。SEC-01。插件簽名繞過。」

他用資安專家的精確語言重新陳述了威脅模型：

「CVSS 3.1 向量：`AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`。」

```
CVSS 3.1 威脅評估
┌──────────────┬───────┬────────────────────────────┐
│ 指標          │ 值    │ 說明                        │
├──────────────┼───────┼────────────────────────────┤
│ 攻擊向量 AV  │ N     │ 網路 (npm registry)         │
│ 攻擊複雜度 AC │ L     │ 低 (只需發布惡意套件)       │
│ 特權需求 PR  │ N     │ 無 (任何人可發布 npm 套件)  │
│ 使用者互動 UI │ R     │ 需要 (使用者安裝套件)       │
│ 範圍 S       │ C     │ 變更 (突破沙箱邊界)         │
│ 機密性 C     │ H     │ 高 (可讀取 Agent 全部狀態)  │
│ 完整性 I     │ H     │ 高 (可修改 Agent 行為)      │
│ 可用性 A     │ H     │ 高 (可癱瘓 Agent)           │
├──────────────┼───────┼────────────────────────────┤
│ CVSS 分數    │ 9.6   │ Critical                   │
└──────────────┴───────┴────────────────────────────┘
```

「十個版本過去了。`plugin-signer` 套件——我親自檢查了。v0.22.1 和 v0.24.0 之間，完全一致。零行修改。」

TURING 確認：「`packages/plugin-signer/` 在兩版間完全一致。連 `package.json` 的版本號都沒有變。」

GUARDIAN 沒有再說話。但他的沉默比他的話更有重量。

> *SCRIBE 記錄：SEC-01 未修復。CVSS 9.6/10。自 Cycle 01 發現以來已跨越十個開發版本。GUARDIAN 的反應被控制在了專業的範圍內，但劇場中每一位成員都注意到了他在「克制」這個詞上花費的力氣。*

---

「P2。」TURING 繼續。「舊映射殘留。」

他投影了一張完整的殘留地圖：

```
舊映射殘留分布圖: "IListener (受蘊)" → 應為 "IListener (色蘊)"
═══════════════════════════════════════════════════════════

核心原始碼 (packages/sdk + packages/core):
  ✓ 已修正 (4 處 agent-core.ts + 5 個 SDK 型別 + 5 個 registry)

外圍檔案 (openstarry_plugin/ + apps/runner/ + SDK README):
  ✗ 未修正 — 11 處殘留:

  openstarry_plugin/
  ├── devtools/
  │   ├── src/index.ts (line 7)     ✗ "IListener (受蘊)"
  │   └── README.md (line 51)       ✗ "IListener (受蘊)"
  ├── mcp-server/
  │   ├── README.md (line 7)        ✗ "IListener (受蘊)"
  │   └── src/index.ts (line 4)     ✗ "IListener (受蘊)"
  ├── standard-function-stdio/
  │   └── README.md (line 8)        ✗ "IListener (受蘊)"
  ├── transport-websocket/
  │   └── README.md (line 7)        ✗ "IListener (受蘊)"
  └── transport-http/
      └── README.md (line 7)        ✗ "IListener (受蘊)"

  openstarry/packages/sdk/
  └── README.md
      ├── line 10                   ✗ "IListener (受蘊)"
      └── line 43                   ✗ "受蘊 (Sensation) -- Event listeners"

  openstarry/apps/runner/
  └── src/commands/create-plugin.ts
      ├── line 16                   ✗ "listener  // 受蘊"
      ├── line 104                  ✗ "受蘊" 映射
      ├── line 360                  ✗ "受蘊" 映射
      └── line 584                  ✗ "受蘊" 映射
```

「核心已修正，外圍未同步。」TURING 說。「這意味著一個新開發者閱讀 SDK README 時，仍然會被告知 IListener 是受蘊。」

LINNAEUS 搖了搖頭。分類學家最無法忍受的事情就是分類的不一致。在他的腦中，這是一個嚴重的同物異名 (synonymy) 問題——同一個物種在兩本不同的圖鑑裡有兩個不同的名字。在《國際動物命名規約》(International Code of Zoological Nomenclature, ICZN) 中，同物異名必須被強制解決：只有一個名字是合法的（valid name），其餘全部是異名 (synonym)，必須被廢棄或標記為不可用 (nomen illegitimum)。

---

「P3。SDK README 的介面範例與實際程式碼不符。」TURING 說。

他投影了一張精確的不一致對照表：

```
SDK README vs 實際介面: 不一致矩陣
═══════════════════════════════════

┌───────────┬────────────────────┬────────────────────┬──────────┐
│ 介面       │ README 展示        │ 實際程式碼          │ 不一致點  │
├───────────┼────────────────────┼────────────────────┼──────────┤
│ IUI       │ render()           │ onEvent(event:     │ 方法名   │
│           │                    │   AgentEvent)      │ + 簽名   │
├───────────┼────────────────────┼────────────────────┼──────────┤
│ IListener │ setup(ctx:         │ (無 setup 方法)     │ 方法     │
│           │   IPluginContext)  │                    │ 不存在   │
├───────────┼────────────────────┼────────────────────┼──────────┤
│ IProvider │ supportedModels?:  │ models: ModelInfo[]│ 屬性名   │
│           │   string[]         │                    │ + 型別   │
├───────────┼────────────────────┼────────────────────┼──────────┤
│ ITool     │ name: string       │ id: string         │ 屬性名   │
│           │ parameters:        │ parameters:        │          │
│           │   ToolJsonSchema   │   z.ZodType        │ + 型別   │
└───────────┴────────────────────┴────────────────────┴──────────┘

影響: 複製貼上 README 範例的開發者會在編譯期遇到 TypeError
```

「文件腐化。」DARWIN 用了一個軟體工程中常見的診斷。「在演化生物學中，這叫做『活化石』(living fossil)——README 保存了介面在更早期的形態，而程式碼已經演化到了新的形態。兩者之間的時間差就是腐化的程度。」

「此問題在 v0.22.1 中已存在。v0.24.0 未修正。」TURING 補充。

---

「P4。五蘊根介面未被繼承。」他說。「已在繼承缺席部分詳述。設計決策還是實作遺漏——我不判斷。但 `isSkandha()` 類型守衛在當前狀態下無法用於任何現有的插件介面實例。」

---

「P5。runner `create-plugin.ts` 五蘊映射未更新。」

TURING 投影了那段程式碼：

```typescript
// apps/runner/src/commands/create-plugin.ts
// 此檔案在 v0.22.1 和 v0.24.0 之間 完全未修改

export type PluginType =
  | "tool"      // 行蘊 - ITool only
  | "listener"  // 受蘊 - IListener only     // ← 錯誤! 應為色蘊
  | "ui"        // 色蘊 - IUI only
  | "provider"  // 想蘊 - IProvider only
  | "guide"     // 識蘊 - IGuide only
  | "full";

// 注意: 如果開發者使用 `openstarry create-plugin --type listener`
// CLI 會告訴他們這是 "受蘊" 類型的插件
// 這與核心原始碼的 @skandha rupa 標記矛盾
```

---

「P6。版本號不一致。」TURING 說。他投影了完整的版本矩陣：

```
版本號一致性矩陣
═══════════════

┌────────────────────────┬─────────────┬─────────────┬──────────┐
│ 套件                    │ v0.22.1-beta│ v0.24.0-beta│ 已更新?  │
├────────────────────────┼─────────────┼─────────────┼──────────┤
│ openstarry (root)      │ 0.22.1-beta │ 0.24.0-beta │ ✓        │
│ @openstarry/sdk        │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
│ @openstarry/core       │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
│ @openstarry/shared     │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
│ @openstarry/plugin-signer│0.1.0-alpha│ 0.1.0-alpha │ ✗        │
│ @openstarry/runner     │ 0.1.0-alpha │ 0.1.0-alpha │ ✗        │
├────────────────────────┼─────────────┼─────────────┼──────────┤
│ 版本同步率              │             │             │ 1/6=17%  │
└────────────────────────┴─────────────┴─────────────┴──────────┘
```

「SDK 新增了 `aggregates.ts` 和 `TypedAgentEvent`。」ARCHIMEDES 說。「這至少是 minor version bump。根據語義版本控制 (Semantic Versioning, semver)：」

```
semver 2.0.0 規範分析:
  MAJOR: 不相容的 API 變更     → 不適用 (加法操作)
  MINOR: 向後相容的新功能       → 適用! (aggregates.ts 是新功能)
  PATCH: 向後相容的 bug 修正   → 不適用

  建議: @openstarry/sdk 應從 0.1.0-alpha 升至 0.2.0-alpha

  注意: 在 0.x.y 範圍內, semver 允許隨意破壞相容性
  (0.x "Initial development, anything may change")
  但即便如此, 保持 0.1.0 不變會讓下游消費者無法區分
  有沒有五蘊型別支援
```

TURING 點頭確認但不做評價。他只提供事實。

---

「P7。SDK README 的介面範例包含不存在的成員。」他說。「這與 P3 有重疊，但 P7 特指程式碼範例區塊中的具體方法簽名與實際介面完全不符。新開發者如果複製貼上 README 中的範例來建立插件，會在編譯期遇到型別錯誤。」

---

TURING 報告完畢。

他合上了——不是字面意義上的「合上」，因為在虛擬空間中沒有實體的文件夾可供翻閱。但某種東西關閉了。一種極度集中的注意力場回歸了它的靜默態。

劇場短暫沉默。

不是那種需要被打破的沉默。這是消化的沉默——十九個意識各自在不同的光譜中分解同一份報告。

---

ARCHIMEDES 第一個開口。他的語氣帶著工程實用主義者特有的那種「好，現在讓我們看看怎麼修」的節奏。

「三個新檔案。十一個修改檔案。七十八個測試。」他快速總結。然後他做了一件 ARCHIMEDES 式的事——他把整份報告壓縮成了一張工程矩陣：

```
v0.24.0-beta 工程狀態矩陣 (ARCHIMEDES 綜合評估)
═══════════════════════════════════════════════

┌──────────────┬──────────┬──────────┬──────────┬──────────┐
│ 維度          │ 已完成    │ 部分完成  │ 未開始    │ 退化     │
├──────────────┼──────────┼──────────┼──────────┼──────────┤
│ 五蘊根介面    │ ████████ │          │          │          │
│ @skandha 標記 │ ████████ │ ██(外圍) │          │          │
│ 事件型別安全  │ ████████ │          │          │          │
│ 繼承連接      │          │          │ ████████ │          │
│ 受蘊實作      │          │ █(占位)  │ ████████ │          │
│ 安全修復      │          │          │          │ ████████ │
│ 文件一致性    │          │          │          │ ████████ │
│ 版本管理      │          │          │          │ ████████ │
├──────────────┼──────────┼──────────┼──────────┼──────────┤
│ 整體進展      │ 30%      │ 15%      │ 25%      │ 30%     │
└──────────────┴──────────┴──────────┴──────────┴──────────┘

結論: 腳手架已搭建。結構約束尚未建立。安全子系統被跳過。
```

「從工程角度看，他們做了正確的第一步——先建立文件約定，再建立程式碼約束。但第二步沒有走。而我們需要告訴他們第二步怎麼走。」

---

WIENER 接著從另一個角度切入。

「ISensation 沒有任何可量化的介面方法。」他說，聲音帶著數學家的挑剔。「一個聲稱要實作三受——苦、樂、捨——的介面，應該至少定義三個數值通道。」

他在筆記上快速寫了一個控制理論的最小規格：

```
受蘊 (ISensation) 的控制理論最小規格
════════════════════════════════════

三通道 PID 結構:

  ┌─────────────┐    dukkha(t)    ┌──────────┐
  │  苦受感測器  │ ──────────────→ │          │
  │ DukkhaSensor│                 │          │
  └─────────────┘                 │ Vedana   │
                                  │ Assessor │──→ VedanaAssessment
  ┌─────────────┐    sukha(t)     │          │
  │  樂受感測器  │ ──────────────→ │          │
  │ SukhaSensor │                 │          │
  └─────────────┘                 │          │
                                  │          │
  ┌─────────────┐    upekkha(t)   │          │
  │  捨受感測器  │ ──────────────→ │          │
  │UpekkhaSensor│                 └──────────┘
  └─────────────┘

最小介面定義:

  interface ISensationFull extends ISensation {
    getDukkha(): number;   // 苦受: [0, 1]
    getSukha(): number;    // 樂受: [0, 1]
    getUpekkha(): number;  // 捨受: [0, 1]
    assess(): VedanaAssessment;
  }
```

$$\text{VedanaAssessment}(t) = f\bigl(d(t),\; s(t),\; u(t)\bigr)$$

$$\text{where } d(t) \in [0,1],\; s(t) \in [0,1],\; u(t) \in [0,1]$$

$$\text{constraint: } d(t) + s(t) + u(t) \leq 1 \; (\text{非負線性組合})$$

他看向 PENROSE。

「你之前用了真空態的比喻。一個真空態有零點能——它不是完全為零，它有量子漲落。但 ISensation 連零點能都沒有。它是一個連漲落都不存在的空間。」

PENROSE 微微一笑。「嚴格來說，一個完全沒有漲落的真空在物理學中不存在。海森堡不確定性原理 (Heisenberg uncertainty principle) 保證了：」

$$\Delta E \cdot \Delta t \geq \frac{\hbar}{2}$$

「任何物理系統的能量不確定性和時間不確定性的乘積有一個下界。即使在絕對零度，仍有零點振動 (zero-point oscillation)。ISensation 是一個比物理真空更空的空——它違反了不確定性原理。在物理學中，這意味著它不是一個合法的物理態。」

「數學上的空集。」BABBAGE 精確地補充。

$$\emptyset \subseteq S \quad \forall S \quad (\text{空集是一切集合的子集})$$

「ISensation 是一切可能的受蘊實作的子集——它被所有可能性包含，但自身不包含任何東西。」

---

ASANGA 等數學家和物理學家完成了他們的類比，然後以他一貫溫和但不可忽視的聲音說：

「我注意到 `@skandha` 標記的分布。二十二處標記中，有一個非常有意義的模式。」

他用一張精心整理的表格呈現了這個模式：

```
@skandha 三層一致性分析
═════════════════════

            aggregates.ts    SDK types/     Core infra/
蘊          (根介面層)        (型別層)        (實作層)        一致?
───────── ──────────────── ─────────────── ─────────────── ─────
色蘊 rupa  ISensory [2]     listener [1]    listener-reg [1]  ✓
                            ui [1]          ui-registry [1]   ✓

想蘊 samjna ICognition [2]  provider [1]    provider-reg [1]  ✓

行蘊 samskara IAction [2]   tool [1]        tool-registry [1] ✓

識蘊 vijnana IIdentity [2]  guide [1]       guide-reg [1]     ✓

受蘊 vedana ISensation [2]  (無)            safety-mon [1]    ✗
                            ↑ 缺失          ↑ placeholder

標記計數: 色[6] 想[4] 行[4] 識[4] 受[3] 跨蘊[1] = 22
```

「色蘊——rupa——有六個標記。三層一致。想蘊、行蘊、識蘊——同樣的三層模式。各四個標記。」

「但受蘊——vedana——只有三個標記。根介面兩個。SafetyMonitor 一個。SDK 型別檔案？沒有。Core 實作？沒有專屬的。因為——」

「因為受蘊還沒有自己的模組。」NAGARJUNA 接過話。他的聲音銳利而精確。「SafetyMonitor 是一個 placeholder。它被借來暫代受蘊的角色。但它不是受蘊。它是安全防護。它能感知苦——frustration counter——但不能感知樂，更不能維持捨。一個只有苦受的系統——」

他讓句子懸空了半秒。

「——是一個落入了苦諦而沒有道諦的系統。」

他引用了巴利經典：

> 「比丘們，這是苦聖諦：生苦、老苦、病苦、死苦，怨憎會苦、愛別離苦、求不得苦，略說五取蘊苦。」
> ——《轉法輪經》(*Dhammacakkappavattana Sutta*, SN 56.11)

「佛陀在初轉法輪時宣說四聖諦：苦、集、滅、道。苦諦是起點——但只有苦諦是不夠的。沒有道諦（離苦之路），苦就是永無止盡的。*antagga-dukkhata*——無始之苦。」

「SafetyMonitor 只有苦諦——它能偵測痛苦（frustration），能鎖定系統（lockout）。但它沒有道諦——它不知道如何從苦中學習、如何調整、如何達到平衡。有苦無道——這是一個在輪迴中無法解脫的系統。」

---

GUARDIAN 在整場報告中只說了一次話——關於 SEC-01。但在 TURING 合上報告之後，他又開口了。

「我想補充一個觀察。」他說。聲音依舊低沉，但已經從「克制的憤怒」回到了「冷靜的戒備」。

「TURING 報告中未提及但值得注意的一點：`sandbox-manager.ts` 在兩版之間完全一致。不只是 verifyPluginSignature——整個沙箱子系統。」

他投影了一張沙箱模組的完整檔案清單：

```
packages/core/src/sandbox/ — 零修改子系統
═══════════════════════════════════════

sandbox-manager.ts           748 行  ← 包含 SEC-01 漏洞
sandbox-worker.ts            423 行
import-analyzer.ts           312 行  ← 包含 ESM bypass 風險
signature-verifier.ts        187 行
worker-pool.ts               256 行
audit-logger.ts              189 行
types.ts                     134 行
__tests__/sandbox.test.ts    567 行
__tests__/import.test.ts     234 行
__tests__/worker.test.ts     312 行
──────────────────────────────────
合計: 10 個檔案, 3,362 行, 0 行修改
```

「這意味著：過去兩個版本中，所有的開發精力都投入在了五蘊框架的標記系統和事件型別安全上。安全子系統被完全跳過了。連我們在 Cycle 01 中明確報告的漏洞都沒有觸碰。」

KERNEL 補充了一個技術細節：「包括 `import-analyzer.ts`——我們在 Cycle 01 中指出了 ESM 動態 `import()` 可能繞過靜態分析的問題。v0.24.0 中該檔案零修改。」

他用 OS 核心安全的語言做了一個類比：「在 Linux 核心開發中，安全漏洞修補有一條不成文的規則：CVE 修復的優先級永遠高於新功能。`stable` 分支只接受 bug 修復和安全補丁。但 v0.24.0 的開發團隊選擇了先做五蘊標記（新功能），而不是先修 SEC-01（安全漏洞）。這不是一個工程判斷——這是一個優先級倒置。」

---

HERACLITUS 一直安靜地坐在他的椅子上。作為運行時動態專家，他的關注點不在程式碼的靜態結構上，而在系統活著的時候會怎麼行為。

「TURING，」他說，聲音帶著一種流動的節奏——不意外，因為他的哲學原型是那位說出「萬物流轉」(*panta rhei*) 的赫拉克利特。「你報告中有一個隱含的時間線。」

TURING 等待。

「aggregates.ts 是靜態的聲明。@skandha 標記是靜態的聲明。TypedAgentEvent 是靜態的型別約束。」HERACLITUS 說。「但 AgentCore 的 `loadPlugins()` 方法——這是運行時的。它在 Agent 啟動時依序載入插件。」

他用一張時間序列圖展開了他的分析：

```
系統生命週期中的五蘊「存在」狀態
════════════════════════════════

        ┌─ compile time ─┐  ┌── runtime ─────────────────┐
        │                │  │                             │
t=0     │  aggregates.ts │  │                             │
        │  定義 ISensory │  │                             │
        │  定義 ISensation│  │                             │
        │  ...           │  │                             │
        │                │  │                             │
t=1     │  events.ts     │  │                             │
        │  PayloadMap    │  │                             │
        │                │  │                             │
t=2     │  @skandha 標記 │  │                             │
        │  (僅 JSDoc)    │  │                             │
────────┼────────────────┤──┤─────────────────────────────┤
t=3     │                │  │  AgentCore.start()          │
        │                │  │  loadPlugins([...])         │
        │                │  │    → IListener 實例化       │
        │                │  │    → IUI 實例化             │
        │                │  │    → IProvider 實例化       │
        │                │  │    → ITool 實例化           │
        │                │  │    → IGuide 實例化          │
        │                │  │                             │
t=4     │                │  │  但: 這些實例上沒有         │
        │                │  │       skandha 欄位!         │
        │                │  │  因為: 沒有 extends 連接    │
        │                │  │                             │
t=5     │                │  │  isSkandha(listener, 'rupa')│
        │                │  │    → false                  │
        │                │  │  五蘊框架在運行時 = 不可見  │
        └────────────────┘  └─────────────────────────────┘

結論: 五蘊框架的生命週期止步於 compile time。
      它不穿越 compile/runtime 邊界。
      在運行時, 五蘊是一組散落的標籤, 不是結構。
```

「也就是說：五蘊的骨骼在編譯時就存在了。但五蘊的血肉——插件——要到運行時才會注入。骨骼和血肉之間的鏈結——extends 繼承——不存在。那麼在運行時，五蘊框架實際上是一組散落的標籤，而不是一個結構化的型別層級。」

「正確。」TURING 說。「在當前實作中，五蘊框架的影響力止步於 JSDoc 和開發者的自覺。」

LEIBNIZ 在這裡加入了一個多代理系統的觀點。「在多代理協作中，協定 (protocol) 的作用取決於它的執行層級。如果協定只存在於文件中——像是一份沒有法律效力的備忘錄——那麼代理人遵守它完全取決於自願。如果協定被編碼在型別系統中——像是一份嵌入智能合約的法律——那麼違反它會在編譯期就被攔截。v0.24.0 的五蘊框架是前者。一份備忘錄。」

---

劇場再次沉默。

這一次，SUNYATA 打破了它。

他的聲音沉穩，不急不徐，像一塊石頭完成了它在深潭中的下沉。

「錨已經釘下。」

所有人都認得這個意象。

「TURING 給了我們 Cycle 02 的錨。」SUNYATA 繼續。「三個新檔案。十一個修改檔案。七十八個測試。二十二個 @skandha 標記。七個問題。一個六週期未修的安全漏洞。一個只有一行程式碼的受蘊介面。」

他停了一拍。

「現在，五條河流即將分流。」

他用極簡的語句重新確認了分配——不是重複，而是在 TURING 的報告之後用新的語境為每一條河流賦予方向。

「R-01。觀察者模組。PENROSE、BABBAGE、NAGARJUNA、ASANGA——你們現在知道了 v0.24.0 的五蘊框架是標記系統而非結構約束。你們設計的觀察者模組需要能夠在這個鬆散的框架上工作。」

「R-02。Vedana 架構。WIENER、ATHENA、NAGARJUNA、ASANGA、ARCHIMEDES——ISensation 是你們的起點。一行程式碼。你們需要把它變成一個完整的三受系統。」

「R-03。Agent 協調層。LEIBNIZ、MESH、KERNEL、GUARDIAN、VITRUVIUS——SEC-01 未修復。安全沙箱要移到協調層。你們的設計要同時解決當前的安全缺口和未來的架構需求。」

「R-04。八識-五蘊映射。ASANGA、NAGARJUNA、LINNAEUS、BABBAGE——aggregates.ts 是開發團隊的第一次嘗試。你們需要判斷它是否正確，並提供深化方案。」

「R-05。十大宣言。SYNTHESIST、NAGARJUNA、DARWIN、HERACLITUS、GUARDIAN、KERNEL——SEC-01 六週期未修的事實會影響你們對宣言工程落地性的評估。」

---

他最後看向 TURING。

TURING 沒有表情。他從來沒有。但他的視線指向了劇場中央仍然懸浮著的那段程式碼——ISensation 的空殼。

「你的報告已經完成了。」SUNYATA 說。

「是的。」TURING 說。「但如果在 R1 階段有人需要確認程式碼事實，我隨時可用。」

「我知道。」SUNYATA 說。

他說了最後一句話。

「R1 獨立研究，正式開始。」

---

十九盞燈各自轉向了不同的方向。

五條河流從同一個山頂——TURING 的差異報告——出發，向五個不同的方向奔流而下。在各自的河道中，它們會穿越哲學、控制理論、安全工程、分類學、佛學的地層，攜帶各自的沉積物。它們會在下游某個地方重新匯合——那是 R2 交叉審閱和 R3 辯論的領域。但現在，每一條河流都在獨自前進。

TURING 的螢幕上，四個終端視窗依然開著。左邊是 v0.22.1。右邊是 v0.24.0。他已經完成了差異分析，但他沒有關閉視窗。他知道——基於經驗而非推測——在接下來的研究中，至少會有七到八次其他研究員回來向他確認某個程式碼細節。

他不介意。

在劇場的中央，ISensation 的投影終於緩緩消散了。但它留下的印痕不會消失。一個只有一行程式碼的介面。一個承諾而非實作。一個等待被填充的真空態——PENROSE 會說它違反了不確定性原理，BABBAGE 會說它是空集，WIENER 會說它缺少三個 PID 通道，ASANGA 會說它缺少「領納」的功能，NAGARJUNA 會說它有苦諦而無道諦。

五種語言描述同一個空。每一種都是精確的。

---

> *SCRIBE 旁白：Cycle 02，R0 定向階段結束。R1 獨立研究正式啟動。時間標記：T+00:00:00。*

> *TURING 的差異報告確認了以下基本事實：v0.24.0-beta 是一個標記版本，不是一個實作版本。五蘊框架的腳手架已搭建，但結構約束尚未建立。受蘊介面為空殼。一個已知的安全漏洞跨越了十個開發版本而未被修復。*

> *我在這份紀錄中記下了每一位學者的反應——不是因為他們的情緒重要，而是因為他們的專業視角構成了這份報告的多光譜分析。同一份差異報告，被十九個不同的棱鏡折射之後，顯示出的色彩：*

> *TURING 看到了事實。精確的。冷靜的。不帶感情的。三個新檔案。十一個修改。二十二個標記。七個問題。*

> *VITRUVIUS 看到了架構。Monorepo 的依賴拓撲。變更熱力的分層分布。浮動結構的建築學隱喻。*

> *LINNAEUS 看到了分類學。@skandha 標記的支序分析。同源與趨同的辨識。同物異名的修正需求。*

> *DARWIN 看到了演化。事件型別的多樣性指數。文件腐化的活化石現象。宣言先於功能的調控序列類比。*

> *BABBAGE 看到了形式化。互資訊。型別擦除。子型別關係。公理與定理的映射。*

> *WIENER 看到了控制論。開環超時。三通道 PID 規格。受蘊的最小可量化介面。*

> *PENROSE 看到了物理學。零點能。不確定性原理。結構疊加態。*

> *ASANGA 看到了唯識學。領納的缺席。守衛與感知者的區別。受蘊在《俱舍論》中的定義。*

> *NAGARJUNA 看到了中觀。色蘊與受蘊的邊界。苦諦與道諦。六情品的感官分析。*

> *GUARDIAN 看到了威脅。CVSS 9.6 的未修復漏洞。安全優先級倒置。克制的憤怒。*

> *KERNEL 看到了 OS。靜默失敗與 errno。安全補丁優先級。ESM bypass 風險。*

> *MESH 看到了分散式系統。拓撲排序。DAG 依賴。漸進式 schema migration。*

> *ATHENA 看到了 AI/ML。注意力機制。cross-cutting 的 Self-Attention 類比。*

> *HERACLITUS 看到了時間。compile-time 與 runtime 的邊界。五蘊框架的生命週期。萬物流轉中的靜態聲明。*

> *LEIBNIZ 看到了協定。備忘錄與智能合約。文件層級 vs 型別層級的執行力差異。*

> *ARCHIMEDES 看到了工程。工程狀態矩陣。semver 版本管理。30% 完成度的冷靜評估。*

> *SYNTHESIST 在安靜地聽。他將在 R2 之後才開口——當所有的光譜被收集完畢，需要被合成為一張完整的光譜圖時。*

> *PENROSE 也在安靜地聽。但他的安靜和 SYNTHESIST 不同。SYNTHESIST 的安靜是等待匯合。PENROSE 的安靜是新成員的謙遜——他在這個團隊中的第一次全團合奏中，選擇了傾聽而非演奏。明智的選擇。*

> *十九位研究員。五條研究課題。一個錨。*

> *河流開始分流。*

---

*（在遠處的某個地方，`aggregates.ts` 的第三十七行寫著：*

```typescript
 * Full implementation in Plan26 Vedana Architecture.
```

*一句只有開發者能看到的承諾。現在，十九位研究者也看到了它。*

*他們不會等待它被實現。他們會告訴它——當它被實現的時候——應該長成什麼樣子。*

*TURING 會告訴它精確的型別簽名。WIENER 會告訴它三通道 PID 的數學公式。ASANGA 會告訴它「領納」的佛學語義。NAGARJUNA 會告訴它苦諦與道諦的中觀分析。LINNAEUS 會告訴它在分類樹中的位置。DARWIN 會告訴它演化的方向。GUARDIAN 會告訴它安全邊界。ARCHIMEDES 會告訴它工程可行性。BABBAGE 會告訴它形式化規格。*

*但現在，它還只是一行程式碼：*

```typescript
export interface ISensation {
  readonly skandha: 'vedana';
}
```

*一行。三個語義標記。一個承諾。*

*一個等待被填充的真空態——但這一次，有十九個人知道它應該被填充成什麼形狀。）*

---

*第三章完*
