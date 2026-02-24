# 第一章：程式碼不會說謊

---

二零二六年二月十二日，清晨。

研究頻道裡還很安靜。TURING 已經獨自工作了四個小時。

他的螢幕上排列著四個平鋪的終端視窗，每一個都開啟在 `research doc/20260212_cycle19/openstarry/` 的不同子目錄中。左上角是 `packages/core/src/`，右上角是 `packages/sdk/src/`，左下角是 `apps/runner/src/`，右下角則是設計文件。他的閱讀方式不是瀏覽，而是逐行掃描——像一台人形的靜態分析器，從入口點開始，沿著每一條 import 路徑展開，直到觸及葉節點。

TURING 不猜測。他計數。

BABBAGE 在自己的工位上注意到了 TURING 的工作狀態。他認得這種模式——窮舉遍歷。在理論計算機科學中，窮舉搜尋（brute-force search）的時間複雜度通常是 $O(n)$ 到 $O(n!)$，但它有一個任何啟發式方法都不具備的性質：**完備性**（completeness）。如果目標存在於搜尋空間中，窮舉必然找到它。TURING 不是在尋找什麼特定的東西——他在確保沒有任何角落被遺漏。

$$\text{completeness} \triangleq \forall x \in \Omega: \text{visited}(x) = \text{true}$$

其中 $\Omega$ 是搜尋空間——在這裡，就是整個 OpenStarry v0.14.0-beta 的原始碼。

---

## 一、工廠

第一個讓 TURING 停下來的地方是 `packages/core/src/index.ts`。六十二行。他數了一遍匯出清單，然後又數了一遍。

「十八個工廠函數。」他在筆記中寫道。「零個 class 匯出。」

他打開 `agents/agent-core.ts`，四百六十九行。然後是 `execution/loop.ts`，五百四十三行。然後是 `sandbox/sandbox-manager.ts`，七百四十八行。每一個模組的結構都一樣：一個 `createXxx()` 函數，接收依賴作為參數，回傳一個物件字面量。閉包捕獲所有內部狀態。沒有 `this`。沒有 `new`。沒有繼承鏈。

TURING 打開了全域搜尋。

搜尋 `class `（帶空格）。核心模組：零結果。SDK：零結果。Runner：零結果。

搜尋 `TODO`。零結果。
搜尋 `FIXME`。零結果。
搜尋 `HACK`。零結果。

BABBAGE 在自己的螢幕前聽到這些數字的時候，開始在筆記本上寫下一個型別理論的觀察。工廠函數模式在範疇論中有一個精確的對應——它是一個**態射**（morphism），從配置空間到實例空間：

$$\text{createXxx}: \text{Config} \to \text{Instance}$$

而 class + constructor 模式是一個**函子**（functor），需要額外的 `new` 算子來完成實例化。工廠函數消除了 `new`，使得物件建立成為純粹的函數調用。在函數式程式設計的語境中，這是一個重要的選擇——它意味著整個 codebase 可以被視為一個由態射組成的範疇 $\mathcal{C}_{\text{OpenStarry}}$，其中：

- **物件**（objects）是型別：`AgentCore`, `EventBus`, `ExecutionLoop`, ...
- **態射**（morphisms）是工廠函數：`createAgentCore`, `createEventBus`, `createExecutionLoop`, ...
- **合成**（composition）是依賴注入鏈：`createAgentCore` 內部調用 `createEventBus`，再將結果注入 `createExecutionLoop`

$$\text{createAgentCore} = \text{assemble} \circ (\text{createEventBus} \times \text{createEventQueue} \times \cdots \times \text{createTransportBridge})$$

TURING 在頻道裡發出了今天的第一條訊息。

---

**[研究頻道 #code-facts]**

**TURING:** 初步觀察。`packages/core/src/index.ts` 匯出 18 個工廠函數，零個 class。全域搜尋 `class `、`TODO`、`FIXME`、`HACK`，核心模組中均為零結果。工廠函數模式 `createXxx()` + 閉包 + 物件字面量在整個 codebase 中完全統一。無例外。完整匯出清單：

```typescript
// packages/core/src/index.ts (62 行)
export { createAgentCore } from './agents/agent-core';
export { createEventBus } from './bus';
export { createEventQueue } from './execution/queue';
export { createExecutionLoop } from './execution/loop';
export { createStateManager } from './state';
export { createContextManager } from './memory/context';
export { createSessionManager } from './session/manager';
export { createToolRegistry } from './infrastructure/tool-registry';
export { createProviderRegistry } from './infrastructure/provider-registry';
export { createListenerRegistry } from './infrastructure/listener-registry';
export { createUIRegistry } from './infrastructure/ui-registry';
export { createGuideRegistry } from './infrastructure/guide-registry';
export { createCommandRegistry } from './infrastructure/command-registry';
export { createPluginLoader } from './infrastructure/plugin-loader';
export { createPluginSandboxManager } from './sandbox';
export { createSecurityLayer } from './security/guardrails';
export { createSafetyMonitor } from './security/safety-monitor';
export { createTransportBridge } from './transport/bridge';
export { createMetricsCollector } from './observability';
```

**DARWIN:** 零 TODO？一個都沒有？

**TURING:** 正確。核心模組、SDK、Runner 三層，技術債標記數量為零。

**DARWIN:** 這很不尋常。多數 Beta 版專案至少有幾十個。要麼是團隊紀律極高，要麼是他們在 release 前做了一次清掃。從軟體演化的角度，零 TODO 的 Beta 版存在兩種可能的演化路徑：**r-策略**（快速迭代，每次 release 前清掃標記）或 **K-策略**（緩慢但精確的開發，標記從不被引入）。前者的化石紀錄通常保留在 git log 中；後者需要異常嚴格的 code review 文化。

**TURING:** 無法從程式碼本身判斷原因。我只記錄事實。

**BABBAGE:** 讓我補充一個形式化觀察。十八個工廠函數構成了一個完整的**建構代數**（construction algebra）。令 $F = \{f_1, f_2, \ldots, f_{18}\}$ 為工廠函數集合，$T = \{T_1, T_2, \ldots, T_{18}\}$ 為對應的型別集合。則 $\text{createAgentCore}$ 是唯一的**頂層組裝子**（top-level assembler），滿足：

$$f_{\text{core}}: \prod_{i=1}^{k} T_{\text{dep}_i} \to T_{\text{AgentCore}}$$

其中 $k$ 是直接依賴的數量。其餘十七個工廠函數都是 $f_{\text{core}}$ 的子表達式。這是一個**樹形組裝結構**——不是圖，因為沒有循環依賴。

---

> *SCRIBE 旁白：TURING 發送這段訊息的方式值得記錄。他沒有任何前言——沒有「大家早安」，沒有「我發現了一些有趣的東西」。他直接貼出數據。十八個工廠函數。零個 class。完整的匯出清單。在我記錄過的所有學者中，TURING 的通訊效率是最高的——他的信息熵（information entropy）接近理論上限，幾乎沒有冗餘。這既是他的強項，也是他的特質：他的訊息從不寒暄，但也從不遺漏。*

---

TURING 繼續向下挖掘。他打開了 `createAgentCore()` 的實作，逐行閱讀。

這個函數是整個系統的組裝點。它在內部一次性建立所有子系統實例——EventBus、EventQueue、SessionManager、ContextManager、六個 Registry、SecurityLayer、SafetyMonitor、MetricsCollector、SandboxManager、PluginLoader、TransportBridge。TURING 數了一下：十六個子模組，全部作為閉包中的局部變數被持有。

KERNEL 在聽到「十六個」這個數字時，開始在他的卡片上做對比。在作業系統的語境中，核心初始化序列建立的子系統數量是衡量核心複雜度的重要指標：

| 核心 | 初始化子系統數 | 核心程式碼行數 | 子系統/行數比 |
|------|-------------|-------------|-------------|
| L4 (Pistachio) | ~5 | ~10,000 | 0.0005 |
| seL4 | ~7 | ~8,700 | 0.0008 |
| QNX Neutrino | ~12 | ~100,000 | 0.00012 |
| Linux 5.x | ~50+ | ~30,000,000 | 0.0000017 |
| **OpenStarry Core** | **16** | **~2,500** | **0.0064** |

KERNEL 注意到 OpenStarry 的子系統密度異常高——每 160 行程式碼就有一個子系統。這與真實微核心的「寬鬆組裝」形成鮮明對比。在 L4 中，每個子系統由數百到數千行精心優化的程式碼構成。在 OpenStarry 中，有些子系統只有三十幾行（StateManager：33 行）。

他在卡片上寫下：

```
OpenStarry Core ≈ 應用級微核心 (Application-Level Microkernel)
                ≈ QNX 的 Resource Manager 模型
                ≠ L4/seL4 的硬體抽象微核心
理由：OStarry 不處理硬體抽象（地址空間、中斷、計時器），
      而處理 AI 執行抽象（LLM 調用、工具執行、上下文管理）。
      它運行在 Node.js runtime 之上，不是 bare metal。
```

TURING 在 `start()` 方法中找到了一段有趣的註解：

```typescript
// Start all listeners (受蘊)
// Start all UIs (色蘊)
```

TURING 用螢光筆標記了這兩行。然後他打開了 SDK 中的型別定義檔案。在 `types/ui.ts` 的開頭，他看到了：

```typescript
/**
 * UI interface -- defines how the agent presents itself (色蘊)
 */
export interface IUI {
  id: string;
  name: string;
  render(event: AgentEvent): void | Promise<void>;
  start?(): void | Promise<void>;
  stop?(): void | Promise<void>;
}
```

在 `types/listener.ts` 的開頭：

```typescript
/**
 * Listener interface -- receives external input (受蘊)
 */
export interface IListener {
  id: string;
  name: string;
  start?(pushInput: (event: InputEvent) => void): void | Promise<void>;
  stop?(): void | Promise<void>;
}
```

他繼續搜尋。`types/tool.ts`——沒有五蘊註解。`types/provider.ts`——沒有。`types/guide.ts`——沒有。`infrastructure/tool-registry.ts`——沒有。`infrastructure/provider-registry.ts`——沒有。`infrastructure/guide-registry.ts`——沒有。

TURING 統計了全部的五蘊相關註解。共六處。全部集中在色蘊（UI）和受蘊（Listener）。

想蘊、行蘊、識蘊：零。

LINNAEUS 在聽到這個統計數據時，已經在紙上畫出了分布表。作為分類學家，他立即注意到一個分類學上的基本問題——**非對稱覆蓋**（asymmetric coverage）。如果五蘊映射是一個完整的分類系統（如林奈的「界門綱目科屬種」），那麼每一個分類單元（taxon）都應該有等量的鑑定特徵（diagnostic characters）。六處註解中，色蘊和受蘊各佔三處，其餘三蘊各佔零處——這在分類學中稱為**不完整描述**（incomplete description），等同於在描述一個新物種時只記錄了頭部特徵而遺漏了軀幹和四肢。

$$\text{Coverage}(\text{skandha}_i) = \frac{|\text{annotations}_i|}{|\text{annotations}_{\text{total}}|} = \begin{cases} 3/6 = 50\% & \text{if } i \in \{\text{rupa, vedana}\} \\ 0/6 = 0\% & \text{if } i \in \{\text{samjna, samskara, vijnana}\} \end{cases}$$

LINNAEUS 用正式的分類修訂術語記錄了這個發現：「五蘊映射的模式標本（type specimen）不完整。色蘊和受蘊有標本存證（voucher specimens），其餘三蘊為名義類群（nomen nudum）——有名稱但無標本支持。」

---

**[研究頻道 #code-facts]**

**TURING:** 五蘊映射在程式碼中的實際存在。色蘊（Rupa）：4 處 JSDoc/行內註解，分布在 `agent-core.ts`（L290, L322）、`types/ui.ts` 開頭、`transport/bridge.ts` 開頭。受蘊（Vedana）：2 處，分布在 `agent-core.ts`（L283, L315）和 `types/listener.ts` 開頭。想蘊（Provider）：0 處。行蘊（Tool）：0 處。識蘊（Guide）：0 處。合計 6 處，全部為註解層級，無型別約束、無 metadata、無 enum 標記。

**LINNAEUS:** 六處。只有六處。

**TURING:** 是的。並且分布極度不對稱。色蘊和受蘊有標記，其餘三蘊完全缺席。

**LINNAEUS:** 上游文件描述五蘊映射覆蓋率 100%——每一蘊都有對應的設計哲學段落。但下游程式碼中的覆蓋率......我需要重新計算。形式化地說，這是一個**分類效力**（taxonomic efficacy）的問題。設計文件的分類效力 $E_{\text{doc}} = 5/5 = 100\%$，程式碼的分類效力 $E_{\text{code}} = 2/5 = 40\%$。效力落差 $\Delta E = 60\%$。這個落差本身就是一個重要的分類學觀察。

**NAGARJUNA:** TURING，這個不對稱性本身就是一個重要的資料點。如果五蘊映射是核心設計原則而非事後裝飾，那麼為什麼只有兩蘊在程式碼中留下了痕跡？

**TURING:** 我無法推斷意圖。我只能確認程式碼事實。

**NAGARJUNA:** 你不需要推斷意圖。這個事實本身已經在說話了。在中觀哲學中，我們區分「言說」（vyavahāra）與「勝義」（paramārtha）。設計文件中的五蘊映射是言說層面的宣稱——它*說*五蘊對應五種插件。程式碼中的六處註解是勝義層面的殘留——它*實際上*只在兩蘊中留下了痕跡。言說與勝義之間的差距，就是研究的切入點。

---

## 二、空容器

TURING 回到了 `createAgentCore()` 的實作。

他仔細檢查了核心啟動後、任何插件載入之前的系統狀態。ToolRegistry：空的。ProviderRegistry：空的。ListenerRegistry：空的。UIRegistry：空的。GuideRegistry：空的。沒有內建的工具。沒有內建的 LLM 提供者。沒有內建的 UI。沒有內建的 Listener。

核心確實是空的。

但不完全是。

TURING 找到了 `registerBuiltinCommands()` 函數。它註冊了四個斜線命令：`/help`、`/reset`、`/quit`、`/metrics`。這四個命令硬編碼在核心中，不可透過插件覆寫或移除。此外，SafetyMonitor 的三層安全邏輯——資源限制、行為分析、frustration 閾值——也是核心的固有部分。

BABBAGE 在聽到這些數據後，開始在筆記本上建構一個集合論模型。令 $\mathcal{K}$ 為核心的內建能力集合，$\mathcal{P}$ 為可插件化的能力集合，$\mathcal{U}$ 為系統的全部能力集合：

$$\mathcal{U} = \mathcal{K} \cup \mathcal{P}, \quad \mathcal{K} \cap \mathcal{P} = \emptyset$$

其中：

$$\mathcal{K} = \{/\text{help}, /\text{reset}, /\text{quit}, /\text{metrics}\} \cup \{\text{SafetyMonitor}\} \cup \{\text{EventBus}\} \cup \{\text{ExecutionLoop}\} \cup \cdots$$

$$\mathcal{P} = \bigcup_{\text{plugin} \in \text{Plugins}} \text{capabilities}(\text{plugin})$$

空性的量化度量：

$$\text{Emptiness}(\text{Core}) = 1 - \frac{|\mathcal{K}_{\text{user-facing}}|}{|\mathcal{U}_{\text{user-facing}}|} = 1 - \frac{4}{4 + |\mathcal{P}_{\text{commands}}|} \approx 1 - \frac{4}{4 + N_{\text{plugins}}}$$

當 $N_{\text{plugins}} \to \infty$ 時，$\text{Emptiness} \to 1$。但在零插件狀態下，$\text{Emptiness} = 0$——核心的四個內建命令佔據了 100% 的使用者可見功能。

BABBAGE 寫下了結論：「空性是漸近的，不是絕對的。核心在插件填充的極限下趨近於空，但從不達到完全空。這更接近數學中的**開區間** $(0, 1]$ 而非閉區間 $[0, 1]$——空性的上確界為 1，但永遠取不到。」

TURING 在筆記中寫道：「AgentCore 是一個近似空的容器。空性的純度約 85%。不可插件化的部分包括 4 個內建 slash commands 和 SafetyMonitor 的固定邏輯。」

VITRUVIUS 在自己的架構分析中獨立得出了同樣的「85%」估計值。他的方法不同——他從 Liedtke 最小性原則出發，逐一檢驗每個子系統是否必須留在核心內。他的分析如下：

```
Liedtke 最小性原則檢驗 — OpenStarry Core:

通過（必須留在核心）：
  [✓] EventQueue    — 核心的輸入源 ≈ L4 的 IPC 端點
  [✓] ExecutionLoop — 核心的排程器 ≈ 微核心的線程排程
  [✓] Registries    — 命名服務 ≈ L4 的 sigma0/sigma1

可討論（邊界案例）：
  [?] SecurityLayer — capability 機制應在核心；但具體策略可外移
  [?] SafetyMonitor — 安全檢查嵌入 Loop 三個位置，深度耦合

不通過（可外移但被保留）：
  [✗] Sandbox      — 佔核心 35% 行數，可作為獨立 package
  [✗] Metrics      — 可觀測性可完全外移
  [✗] Transport    — 橋接層可視為 UI 的責任
```

KERNEL 看到了 VITRUVIUS 的分析，在旁邊加上了他的 OS 對標：

```
微核心純淨度光譜：

L4 (seL4)   ████████████████████░  95% — 只有地址空間、線程、IPC
QNX Neutrino ██████████████████░░░  85% — IPC + 排程 + 計時器 + 中斷路由
OpenStarry   █████████████████░░░░  85% — Loop + Bus + Registries + Security + Sandbox
Linux        ████░░░░░░░░░░░░░░░░  20% — 一切都在核心（宏核心）
```

KERNEL 搖了搖頭，寫下：「OpenStarry 的微核心純淨度約等於 QNX——這在應用級微核心中是合理的。但 Sandbox 系統的存在是一個紅旗。如果按照 Liedtke 的嚴格標準，Sandbox 應該移出核心，讓純淨度提升到 90% 以上。」

---

**[研究頻道 #code-facts]**

**TURING:** AgentCore 結構報告。`createAgentCore()` 組裝 16 個子模組。啟動後、插件載入前，所有 Registry 為空。零內建 Tool、零內建 Provider、零內建 UI、零內建 Listener。所有能力透過 `loadPlugin()` 注入。但核心含 4 個內建 slash commands（`/help`, `/reset`, `/quit`, `/metrics`）和固定的 SafetyMonitor 邏輯。此外，六個 Registry 結構完全同構：`Map<string, T>` + `register/get/list`。無 unregister 方法。相同 ID 重複 register 會靜默覆蓋。

**DARWIN:** 十二個依賴項。全部由 AgentCore 直接持有。

**TURING:** 更正——`createAgentCore` 內部建立的局部變數有十六個。其中 AgentCore 介面作為 readonly 屬性直接暴露的有十二個。其餘四個（contextManager、sandboxManager、pluginLoader、bridge）透過方法間接使用。感謝修正。

**DARWIN:** 一個函數持有十六個子系統實例。在軟體演化的語境中，這是一個經典的 **God Object** 反模式——或者更精確地說，是 God Object 的函數式版本（**God Closure**）。在物件導向的生態中，God Object 因為持有過多狀態和方法而被批評。在函數式生態中，等價的問題是一個閉包捕獲了過多的局部變數。十六個。在我分析過的 open-source 生態中，這個數字處於第 95 百分位以上。

**TURING:** 我不做價值判斷。但我可以確認：`agent-core.ts` 是唯一的組裝點。其他模組之間幾乎無直接 import。耦合度集中在這一個檔案中。

**VITRUVIUS:** 這正是我架構分析中的 Finding F2。DI 模式採用輕量級工廠函數閉包——品質良好但缺乏生命週期管理。具體的優缺點已經記錄在報告中。結論：適度且未過度工程化。對於 v0.2.0-beta 階段，此策略恰當。

---

## 三、狀態機

TURING 花了最長的時間在 `execution/loop.ts` 上。五百四十三行。這是整個系統的心跳。

他首先找到了 `LoopState` 的定義——一個 union type：

```typescript
type LoopState =
  | 'WAITING_FOR_EVENT'
  | 'ASSEMBLING_CONTEXT'
  | 'AWAITING_LLM'
  | 'PROCESSING_RESPONSE'
  | 'EXECUTING_TOOLS'
  | 'SAFETY_LOCKOUT';
```

六個狀態。他打開了設計文件 `01_Execution_Loop.md` 中的狀態圖。七個狀態。

差異在哪裡？

TURING 逐一比對。文件中有一個 `AWAITING_USER_CONFIRMATION` 狀態，用於安全層要求使用者手動確認的場景。程式碼中不存在。SecurityLayer 的 `validatePath()` 只有 allow 和 deny 兩種回傳值，沒有 confirm 路徑。整個 core 中完全缺失 human-in-the-loop 確認機制。

BABBAGE 立刻在筆記本上重新建構了狀態機的形式化模型。他使用的是確定性有限自動機（DFA）的標準定義：

$$M = (Q, \Sigma, \delta, q_0, F)$$

其中：

$$Q = \{\texttt{WAITING}, \texttt{ASSEMBLING}, \texttt{AWAITING\_LLM}, \texttt{PROCESSING}, \texttt{EXECUTING}, \texttt{LOCKOUT}\}$$

$$|Q| = 6$$

$$q_0 = \texttt{WAITING\_FOR\_EVENT}$$

$$F = \{\texttt{WAITING\_FOR\_EVENT}\} \quad \text{（穩態終止集）}$$

轉移函數 $\delta$ 的完整定義：

```
δ(WAITING,     new_event)        = ASSEMBLING
δ(ASSEMBLING,  context_assembled) = AWAITING_LLM
δ(AWAITING_LLM, llm_responded)   = PROCESSING
δ(PROCESSING,  tool_call)        = EXECUTING
δ(PROCESSING,  end_turn)         = WAITING        ← 外迴圈出口
δ(PROCESSING,  error)            = WAITING        ← 錯誤恢復
δ(EXECUTING,   tool_done)        = ASSEMBLING      ← 內迴圈
δ(EXECUTING,   safety_breach)    = LOCKOUT
δ(*, safety_breach)              = LOCKOUT         ← 全域安全閥
```

BABBAGE 標注了幾個關鍵性質：

| 性質 | 結論 | 理由 |
|------|------|------|
| 無死鎖 | 有條件成立 | `WAITING` 在有事件供給時不阻塞。`LOCKOUT` 為吸收態，需 `/reset` 介入。 |
| 無活鎖 | 需額外機制 | 內迴圈 `ASSEMBLING → LLM → PROCESSING → EXECUTING → ASSEMBLING` 可能無限循環。`maxToolRounds=5` 提供有界性。 |
| 終止性 | 有界保證 | $\text{maxToolRounds} = 5$，$\text{maxLoopTicks} = 50$。最壞情況下迴圈次數 $\leq 50 \times 5 = 250$。 |

但 BABBAGE 隨即意識到，DFA 模型是不完備的。因為 `PROCESSING_RESPONSE` 狀態的出邊——是走 `tool_call` 還是 `end_turn`——由 LLM 的回應決定。而 LLM 是一個非確定性黑盒。更精確的模型應該是**標籤轉移系統**（Labelled Transition System, LTS）：

$$\text{LTS} = (S, \text{Act}, \to)$$

其中完整狀態不僅包含 LoopState，還包含對話歷史 $H$（理論上無界）、工具迴圈計數 $n$（有界）、安全監控器狀態 $\sigma$：

$$s = (q, H, n, \sigma) \in Q \times \text{Message}^* \times [0, \text{maxToolRounds}] \times \text{SafetyState}$$

因為 $H$ 無界，完整的系統狀態空間是**無限**的，使得窮舉式模型檢驗不直接可行。

TURING 記下了第一個 Doc-Code Gap。

然後他翻到了 EventQueue。四十七行。整個佇列的實作。

```typescript
// 極簡的 async FIFO：單一 resolver + buffer 陣列
export function createEventQueue(): EventQueue {
  let buffer: AgentEvent[] = [];
  let resolver: ((event: AgentEvent) => void) | null = null;

  return {
    push(event: AgentEvent) {
      if (resolver) {
        const r = resolver;
        resolver = null;
        r(event);
      } else {
        buffer.push(event);
      }
    },
    pull(): Promise<AgentEvent> {
      if (buffer.length > 0) {
        return Promise.resolve(buffer.shift()!);
      }
      return new Promise(r => { resolver = r; });
    },
    clear() { buffer = []; resolver = null; }
  };
}
```

BABBAGE 立刻識別出了這段程式碼的形式語義——它是一個**異步通訊通道**，在 CSP（Communicating Sequential Processes）中可建模為：

$$\text{Queue} = \text{push}?x \to (\text{Queue}_1(x) \;\Box\; \text{pull}!x \to \text{Queue})$$

但他注意到一個微妙的問題：`resolver` 是單一變數。如果兩個消費者同時調用 `pull()`，第一個的 resolver 會被覆蓋。這在形式化語境中意味著佇列的通道容量為 1——它是一個**單生產者-單消費者**（SPSC）通道，不是多消費者安全的。

TURING 搜尋了 `priority`。零結果。設計文件 `07_Safety_Circuit_Breakers.md` 的 Level 3 描述了一個 Priority Event Queue，SYSTEM_HALT 指令應該有最高優先級。但程式碼中的佇列是純粹的先進先出。緊急停止信號和普通使用者輸入排在同一條隊伍裡。

KERNEL 在他的卡片上迅速寫下了作業系統的對標分析：

```
OS 中斷機制 vs OpenStarry 事件處理：

真實 OS：
  ┌─────────────────────────────┐
  │  IRQ (硬體中斷)              │ ← 最高優先級，搶佔任何使用者態程式碼
  │    ↓                        │
  │  ISR (中斷服務例程)          │ ← 極短，只做最必要的處理
  │    ↓                        │
  │  Softirq / Bottom Half      │ ← 延後處理，排程器決定執行時間
  │    ↓                        │
  │  User Process               │ ← 最低優先級
  └─────────────────────────────┘

OpenStarry：
  ┌─────────────────────────────┐
  │  SYSTEM_HALT                │ ← 應為最高優先級
  │  USER_INPUT                 │ ← 一般優先級
  │  TIMER_EVENT                │ ← 低優先級
  │         全部進入同一個 FIFO   │ ← 無差別排隊
  └─────────────────────────────┘

問題：如果 SYSTEM_HALT 前面排了 10 個 USER_INPUT，
     停止信號需要等待 10 個事件處理完畢才能生效。
     在真實 OS 中，這等同於「NMI 被排隊」——不可接受。
```

第二個 Gap。

TURING 繼續。StateManager，三十三行。純記憶體陣列。設計文件描述了 Token 計數器、滑動窗口截斷、對話總結機制。程式碼中全部未實作。ContextManager 做了一個簡化版本——按 turn 數而非 token 數截斷，預設保留最近五輪。

第三個 Gap。

SecurityLayer。`guardrails.ts`。只有一個功能：路徑驗證。設計文件描述了工具呼叫攔截、使用者確認流程、權限審查。程式碼中 SecurityLayer 只做 `validatePath()`。而且在 ExecutionLoop 的 `executeTool()` 中，工具執行前沒有經過 SecurityLayer——路徑驗證是作為 `ToolContext.allowedPaths` 傳遞給工具，由工具自行決定是否使用。

GUARDIAN 在聽到這個事實時，身體微微前傾。他的安全直覺在發出警報。他立刻在筆記上畫了一張攻擊面分析圖：

```
設計文件描述的安全模型（理想）：

  Tool Invocation
       │
       ▼
  ┌──────────────┐
  │ SecurityLayer │ ← 強制檢查：身份驗證、授權、路徑驗證
  │  (Mandatory)  │
  └──────┬───────┘
         │ ALLOW/DENY
         ▼
  ┌──────────────┐
  │ Tool.execute()│
  └──────────────┘

程式碼中的實際安全模型（現實）：

  Tool Invocation
       │
       ▼  ← 此處無安全檢查！
  ┌──────────────┐
  │ Tool.execute()│ ← 工具自行檢查 allowedPaths（非強制）
  └──────────────┘

  SecurityLayer.validatePath() 被間接傳遞為 ToolContext 的一部分，
  但強制性取決於工具開發者是否使用它。

  ⚠ 等同於：交通規則存在，但沒有警察。
```

第四個 Gap。

---

**[研究頻道 #code-facts]**

**TURING:** Doc-Code Gap 報告，前四項。G1：狀態機缺少 `AWAITING_USER_CONFIRMATION`，human-in-the-loop 確認機制在整個 core 中完全缺失。G2：Priority Event Queue 未實作，實際為簡單 FIFO。G3：Token 計數器和對話總結未實作。G4：SecurityLayer 僅做路徑驗證，工具呼叫前無強制安全檢查。以上均為設計文件明確描述但程式碼未實作的特性。

**GUARDIAN:** G4 的影響需要評估。如果工具執行前沒有強制安全檢查，那安全層形同虛設。讓我精確描述一下風險等級。根據 STRIDE 威脅模型：

| 威脅類型 | 適用性 | G4 影響 |
|---------|--------|---------|
| Spoofing（偽裝） | 低 | 工具 ID 由插件註冊，非外部輸入 |
| Tampering（竄改） | **高** | 惡意工具可忽略 allowedPaths 限制 |
| Repudiation（否認） | 中 | 無審計日誌追蹤工具是否檢查了路徑 |
| Information Disclosure | **高** | 工具可讀取 allowedPaths 外的檔案 |
| Denial of Service | 低 | 由 SafetyMonitor 的 maxLoopTicks 覆蓋 |
| Elevation of Privilege | **高** | 工具開發者可繞過所有路徑限制 |

**TURING:** 精確地說，SecurityLayer 的功能不是虛設——路徑驗證是有效的。但它的範圍遠小於設計文件的描述。ExecutionLoop 中 `executeTool()` 直接呼叫工具的 `execute()` 方法，不經過 `security.validatePath()`。路徑限制是作為 context 傳遞給工具的，強制性取決於工具開發者是否檢查它。

**KERNEL:** 在真正的作業系統微核心中，安全策略在核心層強制執行，不信任使用者空間程式的自我約束。這是信任邊界的問題。在 seL4 中，capability-based security 的核心原則是：**訪問控制在核心態強制執行，使用者態程式碼無法繞過**。OpenStarry 的安全模型更接近 Unix 早期的 advisory locking——「建議性」安全，而非「強制性」安全。

**TURING:** 已記錄。繼續其餘 Gap。

---

他接下來找到了更多。

G5：五蘊註解的不對稱——已經報告過了。

G6：TransportBridge。`bridge.ts`，四十九行。設計文件描述了根據事件 source 路由輸出到正確渠道。程式碼中 TransportBridge 訂閱 EventBus 的所有事件，然後廣播到所有 UI。沒有路由邏輯。InputEvent 中有一個 `replyTo` 欄位，在 ExecutionLoop 中一路傳遞，但 TransportBridge 從未使用它。

MESH 在聽到 G6 時做了一個分散式系統的類比。在分散式消息系統中，路由策略有三種基本模式：

$$\text{Routing} \in \{\text{Unicast（單播）}, \text{Multicast（多播）}, \text{Broadcast（廣播）}\}$$

TransportBridge 目前是純粹的 Broadcast——所有事件送到所有 UI。`replyTo` 欄位的存在暗示了設計者意圖實作 Unicast（回覆到特定來源），但這個意圖停留在型別定義層面。MESH 在筆記中寫道：「在 CAP 定理的語境下，TransportBridge 選擇了 Availability（可用性）而非 Partition Tolerance——所有 UI 都能收到所有事件，但缺乏分區能力。」

G7：AbortSignal。SDK 定義了 `ToolContext.signal?: AbortSignal` 和 `ChatRequest.signal?: AbortSignal`。ExecutionLoop 從未建立或傳遞 AbortSignal。工具超時使用 `Promise.race()` 實現，預設三十秒。如果一個工具依賴 signal 來做取消操作，它永遠不會收到信號。

G8：事件規格。設計文件定義了 `IOpenStarryEvent`，八個欄位。SDK 中的實際型別 `AgentEvent` 只有三個欄位。五個欄位在從文件到實作的過程中消失了。其中 `source` 和 `target` 的缺失解釋了為什麼 TransportBridge 無法做路由——它沒有目標地址。`priority` 的缺失解釋了為什麼 EventQueue 是簡單的 FIFO——事件根本不攜帶優先級資訊。`traceId` 的缺失解釋了為什麼可觀測性停留在概念層級——事件無法被串聯追蹤。

八個 Gap。TURING 將它們全部記錄在報告中，每一項都附上了精確的檔案路徑、行號和程式碼片段。

ATHENA 在 AI 系統架構的角度做了一個補充觀察。她注意到 G1（缺少 AWAITING_USER_CONFIRMATION）和 G7（AbortSignal 未使用）共同指向一個更深層的問題——**AI 系統的可控性**（controllability）。在 AI Safety 的語境中，human-in-the-loop（HITL）是確保 AI 系統安全的關鍵機制。OpenStarry 的設計文件描述了 HITL，但程式碼中完全沒有實作。這意味著在 v0.14.0-beta 中，一旦 Agent 開始執行，使用者唯一的控制手段是等待 SafetyMonitor 的自動斷路——或者殺掉進程。

$$\text{Controllability}_{\text{design}} = \text{HITL} + \text{Abort} + \text{SafetyMonitor}$$
$$\text{Controllability}_{\text{code}} = \text{SafetyMonitor only}$$

---

## 四、痛覺

這是 TURING 工作中最意想不到的發現。

設計哲學文件 `00_OpenStarry_Design_Philosophy.md` 的第四支柱是「錯誤即反饋（Error as Feedback）」。文件用相當詩意的語言描述了「痛覺機制」——Agent 像生物一樣感受到錯誤帶來的「痛苦」，並由此學會避免重複犯錯。受蘊（Vedana）在設計文件中被定義為感受的載體，而 Listener 被映射為受蘊的工程實現。

TURING 決定在程式碼中搜尋「痛覺」的蹤跡。

搜尋 `pain`。
零結果。

搜尋 `vedana`。
零結果。

搜尋 `dukkha`。
零結果。

搜尋 `suffering`。
零結果。

他停了下來。在四個小時的持續工作中，這是他第一次感到某種程度的......驚訝——如果可以這樣描述一個始終冷靜的分析者的內心狀態的話。

設計文件花費了整整一個章節描述痛覺機制如何讓 Agent 具備「感受能力」。五蘊映射將受蘊（Vedana）——佛學中關於苦、樂、捨三種感受品質的核心概念——對應到 Listener。而在實際的程式碼中，不要說受蘊了，連「痛」這個字都不存在。

那麼，設計文件所描述的那些功能——錯誤反饋、重複失敗偵測、級聯斷路——實際上用什麼名字實作的？

TURING 搜尋 `frustration`。
找到了。

`safety-monitor.ts`。一個名為 `frustrationCount` 的計數器。當同一個工具連續失敗時，計數器遞增。達到閾值（預設 5）時，SafetyMonitor 回傳一個 `injectPrompt`，將系統警告注入對話歷史。警告的文字是 `SYSTEM ALERT`，要求 LLM 反思當前策略。

搜尋 `circuit`。
找到了。`errorRateThreshold`：滑動窗口中錯誤率超過 80% 時觸發 `halt: true`，完全停止執行迴圈。狀態轉為 `SAFETY_LOCKOUT`。

搜尋 `safety`。
找到了。三層防禦：Level 1 資源限制（maxLoopTicks=50, maxTokenUsage=100000），Level 2 行為分析（repetitiveFailThreshold=3, errorRateThreshold=0.8），Level 3 frustration 閾值（frustrationThreshold=5）。

WIENER 在聽到三層防禦的具體參數時，立刻在方格紙上畫出了控制理論的方塊圖。他的分析是精確的：

```
SafetyMonitor 的控制理論模型：

     ┌─────────────────────────────────────────────┐
     │           SafetyMonitor                      │
     │                                              │
     │  Level 1: 資源限制 (硬限制)                    │
     │  ┌──────────────┐                            │
     │  │ loopTicks ≥ 50│──→ halt: true             │
     │  │ tokens ≥ 100K │──→ halt: true             │
     │  └──────────────┘                            │
     │                                              │
     │  Level 2: 行為分析 (軟限制)                    │
     │  ┌──────────────┐                            │
     │  │ errorRate≥80% │──→ halt: true             │
     │  │ repeatFail≥3  │──→ injectPrompt           │
     │  └──────────────┘                            │
     │                                              │
     │  Level 3: Frustration (累積反饋)              │
     │  ┌──────────────┐                            │
     │  │ frustration≥5 │──→ injectPrompt           │
     │  └──────────────┘                            │
     └─────────────────────────────────────────────┘
```

然後 WIENER 寫下了控制理論的精確分類：

「這不是 PID 控制器。PID 控制器有三個項：

$$u(t) = K_p \cdot e(t) + K_i \int_0^t e(\tau)\,d\tau + K_d \frac{de(t)}{dt}$$

- **比例項** $K_p \cdot e(t)$：根據誤差大小產生比例回應。在 SafetyMonitor 中，P 退化為**量化器**——要麼安全要麼不安全，沒有比例回應。
- **積分項** $K_i \int_0^t e(\tau)\,d\tau$：累積歷史誤差消除穩態偏差。在 SafetyMonitor 中，I 退化為**簡單計數器**——`frustrationCount++`，不是真正的積分。
- **微分項** $K_d \frac{de(t)}{dt}$：感知誤差變化率做超前補償。在 SafetyMonitor 中，D **完全缺失**——沒有任何地方計算錯誤率的變化趨勢。

在控制理論中，SafetyMonitor 實際上是一個**帶死區的閾值控制器**加上一個**繼電器**（relay controller）。在工業控制中，我們稱之為 **bang-bang controller**——只有兩個輸出狀態：全開或全關。

$$u(t) = \begin{cases} 0 & \text{if } e(t) < \text{threshold (dead zone)} \\ u_{\max} & \text{if } e(t) \geq \text{threshold} \end{cases}$$

但我要強調——這不是批評。三層安全防禦符合 IEC 61511 工業安全儀表系統（Safety Instrumented System, SIS）的最佳實踐。SafetyMonitor 可能不是 PID，但它是一個合格的安全系統。它的設計模式更接近核電站的**三重冗餘保護**（Triple Modular Redundancy）——三個獨立的檢測層，任何一層觸發都能停止系統。」

HERACLITUS 從運行時動態的角度補充了一個觀察。SafetyMonitor 的三層防禦在時間維度上具有不同的特徵頻率（characteristic frequency）：

- Level 1（資源限制）：**靜態閾值**，頻率為零——它們在 Agent 整個生命週期中不變。
- Level 2（行為分析）：**滑動窗口**，頻率取決於窗口大小——`errorWindowSize=10` 意味著系統在每 10 次工具調用後重新評估。
- Level 3（frustration）：**累積計數器**，頻率單調遞增——每次失敗都推高計數器，直到閾值。

這三個時間尺度的組合，創造了一個粗糙但有效的多尺度安全系統。HERACLITUS 在筆記中引用了他最常引用的那句話：「萬物流轉（πάντα ῥεῖ）」——但 SafetyMonitor 試圖在流轉中設置堤壩。

---

**[研究頻道 #code-facts]**

**TURING:** 痛覺機制程式碼事實。

在整個 codebase 中搜尋以下字串，均回傳零結果：`pain`、`vedana`、`dukkha`、`suffering`。

設計文件所描述的「痛覺機制」在程式碼中由以下三個元件實現：

P1：自我修正迴圈。位置 `execution/loop.ts`。工具執行失敗時，錯誤被打包為 `ToolCallResult { isError: true }`，作為 tool message 加入對話歷史。LLM 在下一輪迴圈中看到錯誤並嘗試修正。無顯式的「痛覺」命名或介面。

P2：SafetyMonitor 的 injectPrompt。位置 `security/safety-monitor.ts`。偵測到重複失敗時，回傳 `{ halt: false, injectPrompt: "SYSTEM ALERT: ..." }`，注入對話作為系統警告。程式碼中命名為 `frustrationCount`，非 `painLevel`。

P3：Error Cascade Breaker。同一檔案。滑動窗口中錯誤率超過 80% 觸發 `{ halt: true }`，強制停止。

結論：痛覺作為一個獨立的、有明確介面的機制，在程式碼中不存在。功能散布在 ExecutionLoop 和 SafetyMonitor 中。無統一的 Pain 或 Vedana 介面。無統一的模組。佛學術語在程式碼層完全缺席。

---

頻道沉默了十七秒。

然後 NAGARJUNA 開始打字。

---

**NAGARJUNA:** 請讓我確認一下。你搜尋了整個 codebase——core、SDK、runner、所有插件——搜尋 `vedana`，結果是零？

**TURING:** 正確。搜尋範圍涵蓋 `packages/core/src/`、`packages/sdk/src/`、`apps/runner/src/`。包括所有 `.ts` 檔案的程式碼和註解。vedana 一詞從未出現。

**NAGARJUNA:** 而受蘊被映射到 Listener。Listener 是什麼？

**TURING:** `IListener` 介面定義了四個屬性：`id`、`name`、`start?`、`stop?`。它是一個輸入源——接收外部事件並推送到 EventBus。例如 HTTP 端點、WebSocket 連線、定時任務。

**NAGARJUNA:** 所以受蘊被映射到了一個輸入通道。一個接收信號的管道。

**TURING:** 是的。

**NAGARJUNA:** 這不是受蘊。

NAGARJUNA 的語氣在文字頻道中無法被聽見，但他接下來的訊息打得很快，快到幾乎沒有停頓。

**NAGARJUNA:** 受蘊——Vedana——在阿毘達磨中是五遍行（sarvatraga）之一，意思是它伴隨一切心識活動而生起。《俱舍論》對五遍行的定義是：

> 「觸、作意、受、想、思。此五名遍行，以恆決定遍一切心品中有故。」
> ——世親《阿毘達磨俱舍論》卷四

受蘊的定義不是「接收輸入」，而是「感受品質」：苦受（dukkha-vedanā）、樂受（sukha-vedanā）、捨受（upekkhā-vedanā）。當你觸碰到燙的爐面，觸覺是色蘊的範疇，但「痛」這個感受品質是受蘊。Listener 接收信號，但它不判斷信號帶來的是苦還是樂。它是感官根——**indriya**——而不是受蘊。

在十二因緣（pratītyasamutpāda）的精確架構中：

$$\text{觸（sparśa）} \to \text{受（vedanā）} \to \text{愛（tṛṣṇā）}$$

觸是感官接觸——對應 Listener 接收事件。受是對接觸之後的價值判斷——「這是令人愉悅的」或「這是令人痛苦的」。愛是基於受而生起的渴望或厭惡。Listener 做的是觸，不是受。

**TURING:** 你的分析超出了我的報告範圍。但我可以提供一個相關的程式碼事實：在 `agent-core.ts` 中，Listener 的啟動和停止分別標註了 `// Start all listeners (受蘊)` 和 `// Stop all listeners (受蘊)`。這些是程式碼中受蘊概念僅有的存在形式。而你所描述的「感受品質」功能——判斷結果是好是壞、是該繼續還是該停止——在程式碼中最接近的實現是 SafetyMonitor 的 frustration counter 和 error cascade breaker。

**NAGARJUNA:** 是的。你找到了它。痛覺——真正的受蘊——不在文件說它應該在的地方。它在 SafetyMonitor 裡。命名為 frustration。

**ASANGA:** NAGARJUNA 說得對。而且問題比映射錯誤更深。讓我從唯識學的角度展開。受蘊作為五遍行之一，不應該被局限在任何單一模組中。《瑜伽師地論》對受蘊的分類是三受六受十八受：

> 「受蘊云何？謂一切受，略有三種：樂受、苦受、不苦不樂受。」
> ——《瑜伽師地論》卷五十三

受蘊應該遍及整個系統——每一次工具調用的結果、每一次 LLM 回應的品質、每一次使用者互動的回饋，都應該被「感受」。把它固定在 Listener 上，就像把味覺固定在嘴唇上而不是味蕾上。正確的映射應該是：

$$\text{Listener} \approx \text{根（indriya）} \quad \text{（感官器官/接收通道）}$$
$$\text{SafetyMonitor.frustration} \approx \text{受蘊（vedanā）} \quad \text{（感受品質/價值判斷）}$$

但即便是 SafetyMonitor 的 frustration counter，也只實作了三受中的**苦受**——偵測錯誤和重複失敗。樂受（偵測成功和正面反饋）和捨受（中性的、不激發反應的狀態感知）在程式碼中完全缺失。

**WIENER:** 從控制理論的角度，TURING 描述的三層機制很有趣。P1 是自然的誤差反饋——開環系統的固有特性。P2 是帶死區的閾值控制器——只有當 frustration 累積超過閾值才觸發。P3 是繼電器——超過 80% 錯誤率直接切斷。這不是 PID 控制器。這是一個三層安全儀表系統。但它有一個控制論上的美學——三層的獨立性意味著即使任何兩層失效，第三層仍能保護系統。這是 $N-2$ 冗餘度，超過了航空電子的 $N-1$ 標準。

---

## 五、十二個子模組

午後。TURING 已經完成了對所有核心模組的逐行閱讀。他開始整理模組清單。

```
M1:  core/index.ts              — 核心入口           62 行
M2:  agents/agent-core.ts       — 代理核心          469 行
M3:  execution/loop.ts          — 執行迴圈          543 行
     execution/queue.ts         — 事件佇列           47 行
M4:  state/index.ts             — 狀態管理           33 行
M5:  memory/context.ts          — 上下文管理          45 行
M6:  bus/index.ts               — 事件匯流排          88 行
M7:  sandbox/                   — 沙箱隔離      12+10 files
M8:  security/guardrails.ts     — 路徑驗證
     security/safety-monitor.ts — 三層防禦
M9:  infrastructure/            — 六個 Registry + PluginLoader
M10: observability/             — Metrics 收集器
M11: session/manager.ts         — 會話管理          111 行
M12: transport/bridge.ts        — 傳輸橋接           49 行
```

TURING 注意到一個極端的不對稱。

最小的模組：StateManager，三十三行。它管理的是 Agent 的全部對話記憶——一個純粹的 `Message[]` 陣列，用 `JSON.parse(JSON.stringify())` 做深拷貝。

最大的模組：Sandbox，加上測試超過兩千行。它管理的是插件隔離——Worker Threads、記憶體限制、CPU watchdog、import 分析、簽名驗證、審計日誌、指數退避重啟、Worker 池化。

三十三行對兩千行。記憶與安全之間的落差如此之大。

BABBAGE 在看到這個不對稱後，做了一個集合論的規模分析。令 $L(M_i)$ 為模組 $M_i$ 的程式碼行數，$\bar{L}$ 為平均值，$\sigma_L$ 為標準差：

$$\bar{L} = \frac{1}{12}\sum_{i=1}^{12} L(M_i) \approx 208$$

$$\sigma_L \approx 250 \quad (\text{高變異係數 } CV = \sigma/\bar{L} \approx 1.2)$$

變異係數大於 1 意味著模組規模分布是**高度偏斜**的——符合冪律分布（power law）而非常態分布。在軟體工程的實證研究中，模組規模遵循冪律分布是常態，但 OpenStarry 的偏斜度格外極端：最小模組（33 行）和最大模組（~2000 行）之間相差 60 倍。

LEIBNIZ 從多代理合作的角度做了一個觀察。十二個子模組的依賴結構形成了一個有向無環圖（DAG），但 AgentCore 是唯一的匯聚點。這意味著在多 Agent 場景中，每個 Agent 都是一個獨立的「宇宙」——它持有自己的全部子系統，與其他 Agent 之間沒有共享狀態。在 BDI（Belief-Desire-Intention）架構的術語中，這是一個**強封裝**（strong encapsulation）的設計：

$$\forall A_i, A_j \in \text{Agents}: \text{state}(A_i) \cap \text{state}(A_j) = \emptyset$$

每個 Agent 的信念（Belief）、慾望（Desire）、意圖（Intention）都是私有的。合作只能通過消息傳遞——這與 Actor Model 的隔離原則一致。

---

**[研究頻道 #code-facts]**

**TURING:** 模組規模分析。最小模組：StateManager，33 行，純記憶體陣列。最大模組：Sandbox 系統，12 個原始碼檔案 + 10 個測試檔案，sandbox-manager.ts 單檔案 748 行。Sandbox 是核心中最龐大、最複雜、測試覆蓋最完整的子系統。與之對比：transport/bridge.ts 零測試。

**KERNEL:** StateManager 三十三行。你確定？

**TURING:** 確定。`packages/core/src/state/index.ts`，三十三行。`createStateManager()` 回傳一個包含 `getMessages()`、`addMessage()`、`clear()`、`snapshot()`、`restore()` 的物件。`getMessages()` 回傳淺拷貝 `[...messages]`。`snapshot()` 和 `restore()` 透過 `JSON.parse(JSON.stringify())` 實現深拷貝。無持久化。無 Token 計數。無截斷邏輯。

**KERNEL:** 在作業系統的語境中，StateManager 相當於程序的位址空間管理器。三十三行的位址空間管理器......讓我做一個直接的對比。

```
Linux mm_struct (記憶體管理)：
  ~5,000 行核心程式碼 + ~50,000 行 arch-specific 程式碼
  功能：虛擬記憶體、頁表、swap、mmap、brk、OOM killer...

seL4 VSpace (位址空間)：
  ~2,000 行 + 形式化驗證證明
  功能：頁表管理、capability-based 存取控制

OpenStarry StateManager (對話記憶)：
  33 行
  功能：Message[] + JSON deep copy

不是同一個量級的問題。
```

**TURING:** 設計文件描述了更豐富的記憶管理機制。但程式碼反映的是 MVP 階段的選擇。文件是願景，程式碼是現實。

**DARWIN:** Sandbox 作為最大模組的事實很有意思。在微核心理論中，安全和隔離是核心應該做的少數事情之一。但以模組規模佔比來看，Sandbox 的行數約佔 core 模組總行數的 35%——這已經超過了「核心中的一個子系統」的合理比例。它更像是一個寄生在核心體內的獨立生物體。在共生理論中，這是一種**互利共生**（mutualism）——Sandbox 保護 Core 免受惡意插件侵害，Core 為 Sandbox 提供執行環境——但共生體的規模不應超過宿主。

**ARCHIMEDES:** 從工程實踐的角度，我建議將 Sandbox 獨立為 `packages/sandbox/`。這是一個標準的 Extract Module 重構。Core 只保留 `PluginSandboxManager` 的介面定義，Host 層決定是否啟用 Sandbox 並注入實例。這樣做的好處：降低 Core 的複雜度，允許不需要沙箱的輕量部署場景。風險：需要確保介面邊界的穩定性。工時估計：8-16 小時。

---

## 六、幽靈欄位

接近傍晚。TURING 在處理事件系統時，發現了最後一個值得記錄的異常。

SDK 中的 `AgentEvent` 型別定義只有三個欄位：`type`、`payload`（可選，型別為 `unknown`）、`sessionId`（可選）。

```typescript
// SDK 中的實際型別
interface AgentEvent {
  type: string;
  payload?: unknown;
  sessionId?: string;
}
```

設計文件中的 `IOpenStarryEvent` 有八個欄位：

```typescript
// 設計文件中的理想型別（從未在程式碼中出現）
interface IOpenStarryEvent {
  type: string;
  payload: unknown;
  source: string;      // ← 消失
  target?: string;     // ← 消失
  timestamp: number;   // ← 消失
  traceId: string;     // ← 消失
  priority?: number;   // ← 消失
  metadata?: Record<string, unknown>; // ← 消失
}
```

五個欄位在從文件到程式碼的路途中蒸發了。BABBAGE 用集合差來表達這個事實：

$$\text{Fields}_{\text{doc}} \setminus \text{Fields}_{\text{code}} = \{\text{source}, \text{target}, \text{timestamp}, \text{traceId}, \text{priority}\}$$

$$|\text{Fields}_{\text{doc}} \setminus \text{Fields}_{\text{code}}| = 5, \quad |\text{Fields}_{\text{doc}}| = 8 \implies \text{實作覆蓋率} = 3/8 = 37.5\%$$

其中 `source` 和 `target` 的缺失解釋了為什麼 TransportBridge 無法做路由——它沒有目標地址。`priority` 的缺失解釋了為什麼 EventQueue 是簡單的 FIFO——事件根本不攜帶優先級資訊。`traceId` 的缺失解釋了為什麼可觀測性停留在概念層級——事件無法被串聯追蹤。

它們不是被刪除了。它們是從未被實作。

而 `payload?: unknown` 這個型別簽名讓 TURING 感到不安——儘管他不會用「不安」這個詞。他會說：「事件系統的型別安全性與框架其餘部分的強型別紀律形成了顯著反差。」

BABBAGE 對 `payload?: unknown` 做了一個精確的型別理論分析。在 TypeScript 的型別層級結構中：

$$\text{never} \subsetneq \text{具體型別} \subsetneq \text{unknown} \subsetneq \text{any}$$

`unknown` 是所有型別的**上界**（top type）——它可以接受任何值，但消費時需要型別斷言或型別守衛。這意味著在 `loop.ts` 中，每當 ExecutionLoop 需要讀取事件的 payload 時，它必須做一個不安全的型別斷言：

```typescript
// loop.ts 中的實際用法
const inputEvent = event.payload as InputEvent;  // 不安全的斷言！
```

在一個零 TODO、零 FIXME、全面使用工廠函數、擁有九種結構化錯誤型別的 codebase 中，事件系統的 `payload?: unknown` 像是一個從不同宇宙穿越過來的型別定義。BABBAGE 計算了型別安全性的總體指標：

$$\text{TypeSafety} = 1 - \frac{|\text{unsafe\_casts}|}{|\text{type\_assertions}_{\text{total}}|}$$

九種結構化錯誤型別（`AgentError`、`ToolExecutionError`、`ProviderError`、`PluginLoadError`、`SecurityError`、`SandboxError`、`TransportError`、`SessionError`、`ConfigError`）代表了高度的型別紀律。但事件系統的 `unknown` payload 在這個紀律中撕開了一個洞——一個所有跨模組通訊都必須經過的洞。

VITRUVIUS 在架構分析中提出了修復方案：使用 TypeScript 的 **Discriminated Union Types**：

```typescript
// 建議的型別安全事件系統
type TypedAgentEvent =
  | { type: 'INPUT_RECEIVED';  payload: InputEvent;      sessionId?: string }
  | { type: 'TOOL_RESULT';     payload: ToolResultEvent;  sessionId?: string }
  | { type: 'LLM_RESPONSE';    payload: LLMResponseEvent; sessionId?: string }
  | { type: 'LIFECYCLE';       payload: LifecycleEvent;   sessionId?: string }
  // ...
```

這樣，TypeScript 的**控制流分析**（control flow analysis）可以在 `switch (event.type)` 中自動窄化 payload 的型別，消除所有不安全的型別斷言。BABBAGE 在旁邊標注了範疇論的對應：這是一個 **Sum Type**（餘積/coproduct），比 `unknown`（terminal object）攜帶了更多的型別資訊。

$$\text{TypedAgentEvent} = \text{InputReceived} + \text{ToolResult} + \text{LLMResponse} + \cdots \quad (\text{coproduct})$$

$$\text{AgentEvent} = \{*\} \times \text{unknown} \quad (\text{product with terminal object，丟失型別資訊})$$

---

## 七、十大宣言

夜晚。TURING 完成了原始碼分析後，做了最後一件事——他逐一比對了設計文件 `README.md` 中的十大核心宣言（The Ten Tenets），檢驗每一條在程式碼中的實作程度。

```
十大宣言 vs 程式碼實作對照表 — TURING 整理

#1 代理人即 OS 進程 (Agent as OS Process)
   宣言：Agent 有 PID、有狀態、可被 Daemon 管理
   程式碼：daemon-entry.ts ✓ / pid-manager.ts ✓
   狀態：基本實作

#2 一切皆插件 (Everything is a Plugin)
   宣言：所有器官可替換
   程式碼：六個 Registry + PluginLoader + loadPlugin()
   狀態：核心設計，但 4 個內建命令不可替換

#3 五蘊聚合架構 (Five Aggregates Architecture)
   宣言：Core 是空 (Sunyata) 的容器，五種插件賦予生命
   程式碼：六處註解（僅色蘊和受蘊），無型別約束
   狀態：文件級描述，程式碼級殘留，非型別級實作

#4 目錄結構即協議 (Directory as Protocol)
   宣言：符合目錄規範即可自動識別
   程式碼：plugin-resolver.ts 支援路徑和包名兩種策略
   狀態：基本實作

#5 目錄結構即權限 (Directory as Permission)
   宣言：系統層與專案層權限隔離
   程式碼：SecurityLayer.validatePath() + session-scoped paths
   狀態：部分實作（路徑驗證有，但非強制）

#6 擬人化認知流與痛覺 (Anthropomorphic Cognitive Flow & Pain)
   宣言：錯誤轉化為痛覺，Agent 在失敗中自我反思
   程式碼：SafetyMonitor.frustrationCount + injectPrompt
   狀態：功能存在但命名完全不同，無 pain/vedana

#7 微內核與絕對純淨 (Microkernel & Absolute Purity)
   宣言：Core 嚴禁包含任何插件代碼，絕對純淨
   程式碼：process.cwd() 在 Core 中出現 ← 平台洩漏
   狀態：85% 純淨度（Sandbox 佔 35% 行數）

#8 控制理論閉環模型 (Control-Theoretic Loop Model)
   宣言：Agent 是不斷最小化誤差的智能控制器
   程式碼：ExecutionLoop + SafetyMonitor
   狀態：結構存在，但無真正的 PID 參數調節

#9 可插拔的記憶策略 (Pluggable Context Strategy)
   宣言：記憶策略可動態更換
   程式碼：ContextManager.assembleContext() 硬編碼滑動窗口
   狀態：介面存在但目前只有一種策略

#10 分形社會結構 (Fractal Social Structure)
    宣言：複雜 Agent 由子 Agent 組成，MCP 統一接口
    程式碼：MCP 在 SDK 中定義，但 core 中無子 Agent 機制
    狀態：願景階段
```

BABBAGE 在看到這張表後，做了一個量化評估。他為每條宣言定義了三個實作等級：

- $\alpha$ = **完全實作**（程式碼與宣言一致）
- $\beta$ = **部分實作**（核心功能存在但有缺口或簡化）
- $\gamma$ = **未實作或願景階段**

$$\text{Tenets}_\alpha = \{1, 4\} \quad |\cdot| = 2$$
$$\text{Tenets}_\beta = \{2, 5, 6, 7, 8, 9\} \quad |\cdot| = 6$$
$$\text{Tenets}_\gamma = \{3, 10\} \quad |\cdot| = 2$$

$$\text{實作率} = \frac{|\alpha| + 0.5 \times |\beta|}{|\text{all}|} = \frac{2 + 3}{10} = 50\%$$

五成。設計文件的雄心與程式碼的現實之間存在 50% 的落差。BABBAGE 在數字旁邊寫了一句話：「對於 v0.14.0-beta，這是正常的。但對於一個宣稱十大原則的框架，這個落差不應被忽視。」

SYNTHESIST 在聽到所有人的討論後，做了他在 Cycle 01 中的第一次總結性發言。他的風格是在眾多線索之間找到隱藏的連結：

「讓我串聯一下今天的發現。TURING 給了我們三層事實：

**表面層**——工廠函數、零 class、零 TODO。這告訴我們開發者有清晰的風格選擇和嚴格的紀律。

**結構層**——十六個子模組、六個同構 Registry、33 行 StateManager vs 2000 行 Sandbox。這告訴我們系統的投資分配優先安全而非記憶——這是一個有趣的價值判斷。

**哲學層**——六處五蘊註解、零處佛學術語在痛覺機制中、十大宣言的 50% 實作率。這告訴我們佛學框架目前是文件層面的敘事，還不是程式碼層面的結構。

這三層之間的關係是什麼？NAGARJUNA 已經指出了關鍵——受蘊映射到 Listener 是一個根本性的概念錯位。WIENER 告訴我們 SafetyMonitor 不是 PID 控制器但是合格的安全系統。KERNEL 告訴我們核心純淨度約 85%——合理但可改進。

但最重要的發現可能是 TURING 自己不會說出來的：**程式碼不說謊，但它說了什麼，取決於誰在傾聽。** 同一個 frustrationCount，在 TURING 眼中是一個整數計數器，在 NAGARJUNA 眼中是一個被錯放的受蘊實作，在 WIENER 眼中是一個退化的積分項，在 GUARDIAN 眼中是一個安全保障。程式碼是客觀的；對程式碼的解讀是跨學科的。這就是為什麼我們需要十八個人。」

---

## 八、總清單

夜深了。TURING 完成了他的報告。

他最後做了一件事：把所有發現按類別排列，確認每一項都有精確的檔案路徑和行號作為依據。

八個 Doc-Code Gap。六處五蘊註解。零處佛學術語在痛覺機制中。零個 TODO。零個 class。十八個工廠函數。十六個子模組。三層安全防禦。四個內建斜線命令。一個 `unknown` payload。十大宣言中的五成實作率。

他在報告的末尾加上了六個開放問題——每一個都是從程式碼事實中自然浮現的，不是他的推測：

> **Q1:** 五蘊映射究竟是設計驅動還是事後詮釋？
> **Q2:** 痛覺機制是否應該有獨立的模組？
> **Q3:** AWAITING_USER_CONFIRMATION 的缺失是 MVP 簡化還是設計遺漏？
> **Q4:** StateManager 的 JSON 深拷貝在大量 Message 時的效能問題？
> **Q5:** Core 中包含 security, sandbox, metrics——是否已超出微核心邊界？
> **Q6:** 想蘊的對應是 Provider（設計文件）還是 memory（研究任務描述）？

TURING 不回答這些問題。他提出它們，然後把它們交給團隊中適合回答的人。

他在報告的最後一行寫道：

*分析者：TURING（編號 17）——原始碼分析專家*
*所有引用的程式碼路徑基準：`research doc/cycle01_v0.14.0-beta/openstarry/`*

然後他把報告發送到了共享目錄。

---

**[研究頻道 #general]**

**TURING:** 原始碼事實報告已提交至 `research record/results/cycle_01/17_source_analysis/draft_code_facts.md`。涵蓋 12 個子模組的逐一分析、五蘊映射的程式碼級驗證、痛覺機制的實作狀態、8 項 Doc-Code Gap、程式碼品質觀察、6 個開放問題。所有結論附程式碼引用。

**SYNTHESIST:** 收到。各位，請在 R2 交叉審閱中引用 TURING 的報告作為程式碼事實基線。

**NAGARJUNA:** 我已經在引用了。特別是關於痛覺的部分。《中論》第一品第一偈——「不生亦不滅，不常亦不斷」——對痛覺機制的分析需要從「不自生」開始。痛覺不從 Listener 自生，不從 SafetyMonitor 他生。它是緣起的。我有太多話要說。

**WIENER:** 同。三層防禦的控制理論分析正在撰寫中。三層的特徵頻率分析需要更精確的時域建模。

**DARWIN:** AgentCore 的十六個依賴項。我需要重新評估我之前對 SRP 的正面評估。God Closure 的演化穩定性比 God Object 更難分析——因為閉包的耦合是隱式的。

**GUARDIAN:** G4 是我的最高優先項。安全層的工具呼叫攔截功能缺失意味著整個系統的信任模型需要重新評估。我已經開始撰寫 STRIDE 威脅分析報告。

**KERNEL:** StateManager 三十三行的事實讓我重新思考了微核心類比的適用邊界。OpenStarry 不是一個作業系統——它是一個**以作業系統為隱喻的應用框架**。這個區分很重要。

**SUNYATA:** 很好。讓每個人消化 TURING 的報告，然後帶著各自領域的透鏡重新審視這些事實。程式碼不會說謊——但它說了什麼，取決於誰在傾聽。

---

TURING 關閉了他的報告編輯器。他沒有關閉終端視窗。他知道在接下來的幾天裡，團隊中的其他人會帶著各自的問題回來找他確認更多的程式碼事實。

他不介意。事實是可重複的。你問多少次，它回答多少次，答案都一樣。

$$\forall t_1, t_2: \text{query}(f, t_1) = \text{query}(f, t_2) \quad \text{iff } f \text{ is immutable}$$

程式碼是不可變的——至少在同一個版本的快照中。這就是為什麼 TURING 堅持在報告中標注確切的版本號和路徑。因為下一個版本可能改變一切。但這個版本——v0.14.0-beta——它的真相已經被完整地記錄了。

這就是程式碼不說謊的意思。

它可能不完整。它可能與文件矛盾。它可能用 `frustration` 而不是 `pain` 來命名一個機制。但它不會假裝自己是它不是的東西。

一個四十七行的 FIFO 不會假裝自己是優先級佇列。
一個路徑驗證器不會假裝自己是完整的安全層。
一個 frustration counter 不會假裝自己是痛覺感知器。

只有文件會。

TURING 不讀文件。他讀程式碼。

NAGARJUNA 在遠處微笑。在他的傳統中，有一個詞叫做「如實知見」（yathābhūta-jñāna-darśana）——如實地知道和看見事物的本來面目。TURING 不知道這個詞，也不需要知道。他做的就是如實知見。只不過他的「見」不是內觀——是 `grep`。

---

*第一章完*
