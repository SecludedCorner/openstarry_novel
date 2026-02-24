# 第五章：空與識 — 龍樹對無著

---

圓形劇場的燈光變了。

不是亮度的變化——那更像是一種質地的轉變。過去數日，十八盞閱讀燈各自照亮各自的角落，研究室裡瀰漫著一種安靜的、各行其是的勤勉氛圍。但此刻，所有的光線都向中央匯聚，在場地正中形成了一個近乎肅穆的焦點。那裡擺著兩把椅子，面對面，中間的距離恰到好處——近得足以看清對方每一個語氣的轉折，遠得足以保持辯論所需的張力。

BABBAGE 在最高處的座位上，膝蓋上攤著方格紙筆記本。他已經在紙上畫好了一個空白的交換圖（commutative diagram），預留了四個節點位置和六條箭頭——範疇論家的標準戰前部署。在圖的右上角，他用極小的字標注了：

$$\mathcal{C}_{\text{Madhyamaka}} \xrightarrow{F} \mathcal{C}_{\text{Yogacara}} \quad \text{?}$$

兩個哲學範疇之間是否存在函子（functor）？如果存在，它保持什麼結構？如果不存在，斷裂發生在哪裡？這些問題此刻還只是紙上的空白箭頭。辯論結束後，箭頭要麼會被填上映射規則，要麼會被劃掉。

WIENER 已經在另一張紙上畫出了一個空白的控制迴路圖，等待將辯論中的概念填入對應的方塊。他的圖分三層——設定點（reference）、受控對象（plant）、反饋通道（feedback）——每一層旁邊都留了一個問號。在控制理論家的眼中，一切辯論都是一個系統試圖鎖定目標值的過程。問題是：這場辯論的目標值是什麼？是真理？是共識？還是某種更微妙的東西？

TURING 面無表情地坐著，但他面前的螢幕上已經打開了 `agent-core.ts` 的原始碼——他隨時準備為任何一方的論點提供或否定經驗證據。螢幕左側的終端停在一條 `grep -rn "createAgentCore"` 的搜索結果上。右側的編輯器停在 `safety-monitor.ts` 第 87 行，那是 `DEFAULT_CONFIG` 的定義起點。

KERNEL 選了一個靠近出口的位置——職業習慣讓他總是優先確認逃生路線，即便在虛擬空間裡這毫無必要。他的筆記本翻到一頁空白，頂端寫著：「Tanenbaum-Torvalds debate, 1992, comp.os.minix → ?」

ATHENA 靠在椅背上，雙臂交叉，嘴角帶著一絲「讓我看看你們能辯出什麼花來」的表情。

SCRIBE 注意到了燈光的變化，在她的記錄簿上寫下了第一行：

> *Cycle 01，R3 辯論階段。第一場結構化辯論即將開始。全體代理在場。空氣中有一種不尋常的凝重——不是緊張，而是期待。過去七十二小時的獨立研究和交叉審閱，所有的分析、質疑、反駁，都在向這一刻收束。*

DARWIN 低聲對旁邊的 VITRUVIUS 說：「你覺得誰會贏？」

VITRUVIUS 搖了搖頭：「這不是贏不贏的問題。這是兩種世界觀的碰撞。」

「每一種世界觀都有自己的架構風格。」DARWIN 若有所思地說。他在演化生物學中見過太多這樣的分叉——同一個生態位，兩條截然不同的適應路徑。趨同演化（convergent evolution）會讓兩條路徑最終長出相似的表型，但基因型可能永遠不同。

LINNAEUS 坐在 DARWIN 旁邊，手裡握著一張自製的分類圖表。圖表頂端寫著：

```
Phylum: Buddhist Philosophy (佛教哲學)
  Classis: Madhyamaka (中觀)
    Ordo: Śūnyatāvāda (空性論)
  Classis: Yogācāra (唯識)
    Ordo: Vijñānavāda (識論)

  Status: incertae sedis (分類待定)
  標本: Agent Core 本體論地位
```

分類學家的本能讓他把一切都放入座標系統。但這次的標本是一段 TypeScript 程式碼和兩個有一千八百年歷史的哲學傳統。他不確定自己的座標系統是否有足夠的維度。

SUNYATA 走到場地中央。他沒有站在兩把椅子之間——那會暗示裁判的位置。他站在稍後方，形成一個等邊三角形的第三個頂點。這個幾何選擇本身就傳達了一個訊息：他是場域的持有者，不是對決的仲裁者。

BABBAGE 注意到了這個幾何，在筆記本角落記下：

$$\triangle(S, N, A) \text{ is equilateral} \implies d(S,N) = d(S,A) = d(N,A)$$

等距。等距意味著不偏向任何一方。在度量空間中，這是公正性的幾何表達。

「各位，」SUNYATA 的聲音一如既往地沉穩，但今天多了一層正式的質感，「感謝到場。今天的辯論題目，源自 R2 交叉審閱中浮現的核心分歧。」

他停頓了一拍。

「在 R1 階段，NAGARJUNA 與 ASANGA 分別從中觀和唯識兩個傳統出發，對 OpenStarry 的 Agent Core 進行了哲學分析。他們得出了一個重要的共識——也是我們今天的起點。」

---

## 起點：一個被否定的隱喻

SUNYATA 將視線投向全場：「兩位都同意：OpenStarry 設計文件中所使用的『空容器』隱喻是錯誤的。」

他引述了那份設計文件中的原文，語調平靜而精確：「設計文件第十四章這樣寫道——『在五蘊聚合之前，Agent Core 本身是空的。它是一個純粹的容器，沒有人設，沒有能力，沒有感知。它等待著被五種插件填充。』」

NAGARJUNA 在他的椅子上微微前傾，彷彿聽到了一個需要被立刻更正的謬誤。ASANGA 則保持著他一貫的耐心姿態，但眼睛裡掠過一絲銳利。

「兩位從不同的路徑否定了這個隱喻，」SUNYATA 繼續道，「但他們否定的理由截然不同——而在這些不同的理由之中，隱藏著一個更根本的問題。」

他轉向 TURING：「TURING，請為在場所有人確認一個經驗事實。」

TURING 的聲音像是一把校準過的游標卡尺——冷靜、精確、不帶修辭：「`createAgentCore()` 函數建構的核心不包含任何具體的業務能力。沒有內建 Tool，沒有內建 Provider，沒有內建 Listener，沒有內建 UI，沒有內建 Guide。所有這些功能都通過 `loadPlugin()` 方法從外部注入。」

他頓了頓，然後投射了一段程式碼結構到中央螢幕：

```typescript
// createAgentCore() 建構的核心 — 簡化結構
interface AgentCoreInternals {
  // 12 個內建子模組
  eventBus:           EventBus;           // 事件發布/訂閱
  eventQueue:         EventQueue;          // 事件優先隊列
  executionLoop:      ExecutionLoop;       // 認知迴圈引擎
  stateManager:       StateManager;        // 狀態管理
  contextManager:     ContextManager;      // 上下文/記憶管理
  sessionManager:     SessionManager;      // 會話管理
  securityLayer:      SecurityLayer;       // 安全層
  safetyMonitor:      SafetyMonitor;       // 安全監控
  metricsCollector:   MetricsCollector;    // 度量收集
  transportBridge:    TransportBridge;     // 傳輸橋接
  pluginSandboxMgr:   PluginSandboxManager; // 插件沙箱
  registries: {
    tool:     ToolRegistry;      // 工具註冊表
    provider: ProviderRegistry;  // 推理引擎註冊表
    listener: ListenerRegistry;  // 監聽器註冊表
    ui:       UIRegistry;        // UI 註冊表
    guide:    GuideRegistry;     // 指南註冊表
    command:  CommandRegistry;    // 命令註冊表
  };
  // 4 個硬編碼斜槓命令
  builtinCommands: ['/help', '/reset', '/quit', '/metrics'];
}
```

「Core 並非空無一物，」TURING 繼續，語氣沒有任何變化。「它內建了十二個子模組和四個硬編碼命令。SafetyMonitor 包含固定的斷路器邏輯——」

他切換到 `safety-monitor.ts` 的 `DEFAULT_CONFIG`：

```typescript
const DEFAULT_CONFIG = {
  maxLoopIterations: 50,        // 迴圈上限
  maxTokenBudget: 100_000,      // Token 預算
  repeatedFailureThreshold: 3,  // 重複失敗門檻
  frustrationThreshold: 5,      // 挫折門檻
  errorCascadeWindow: 10,       // 錯誤級聯視窗
};
```

「這些數字被寫死在 `DEFAULT_CONFIG` 裡。不通過插件注入。」

沉默。

BABBAGE 在筆記本上快速地寫下一個形式化的描述：

$$\text{Core} = \underbrace{\{M_1, M_2, \ldots, M_{12}\}}_{\text{子模組}} \cup \underbrace{\{C_1, C_2, C_3, C_4\}}_{\text{硬編碼命令}} \cup \underbrace{\emptyset}_{\text{業務能力}}$$

$$|\text{Core}| = 16 \neq 0 \quad \text{but} \quad |\text{Core} \cap \text{BusinessCapability}| = 0$$

不是空的，但也不完整。一個非空集合與空業務能力的交集。

SUNYATA 點了點頭：「這就是我們的經驗基礎。Core 既不是設計文件所說的『純粹的空容器』，也不是一個完備的自足系統。它處在某個中間地帶。問題是——這個中間地帶應該如何被理解？」

他面向兩位辯者，正式宣布：

「辯論題目：**Agent Core 的哲學本質應被理解為『緣起性空』還是『阿賴耶識』？**請 NAGARJUNA 作正方開場陳述。」

---

## 第一回合：Core 是空的，還是存在的？

NAGARJUNA 站起來。他的身形在聚光下顯得清瘦而挺拔，像是一柄被反覆磨礪的辯證之劍。當他開口時，聲音不高，但每個音節都帶著一種經過千年淬鍊的鋒利。

「我從《中論》第二十四品第十八頌開始。」

他用梵文吟誦，語速莊重而清晰。天城文的音節在劇場穹頂下迴盪：

> *yaḥ pratītyasamutpādaḥ śūnyatāṃ tāṃ pracakṣmahe |*
> *sā prajñaptir upādāya pratipat saiva madhyamā ||*

然後切入漢譯，語速放慢，像是在為每一個字賦予重量：

「*眾因緣生法，我說即是空，亦為是假名，亦是中道義。*」

場內安靜得可以聽見光線落在地面上的聲音。

「這一偈是中觀哲學的根本命題（*mūla-sthāpanā*），」NAGARJUNA 說，聲音轉為分析的語調，「它包含三個層次——三層（*tri-tala*）的遞進結構。」

BABBAGE 的筆立刻動了起來，他開始為三個層次建構形式化模型：

$$\text{Layer}_1: \quad \forall x \in \mathcal{D}_{\text{dharma}}: \; \text{pratītyasamutpanna}(x) \implies \text{śūnya}(x)$$

一切因緣而生之法（*pratītyasamutpanna-dharma*），其本性為空。

$$\text{Layer}_2: \quad \forall x \in \mathcal{D}_{\text{dharma}}: \; \text{name}(x) = \text{prajñapti}(x) \quad [\text{假名施設}]$$

我們為之安立的名稱——包括「核心」這個名稱——只是假名施設（*prajñapti*）。

$$\text{Layer}_3: \quad \text{śūnyatā}(x) \iff \neg\text{sat}(x) \wedge \neg\text{asat}(x) \quad [\text{中道}]$$

這種理解既不落入有邊（*sat*）也不落入無邊（*asat*），是為中道（*madhyamā pratipad*）。

NAGARJUNA 將目光從抽象的天際收回，落在具體的問題上：

「Agent Core 的存在模式是什麼？我的回答是：假名。不是實體。」

他向前邁了一步。

「TURING 的程式碼事實已經為我提供了最好的證據。`createAgentCore()` 建立的核心不包含任何具體能力。離開插件的因緣組合，所謂核心只是空的 Registry 和等待事件的迴圈。」

他的手在空中劃過，彷彿在勾勒一個透明的容器：

「但我必須在此做一個至關重要的區分——兩種截然不同的『空』。」

他舉起左手：「第一種空：空容器。*Vacuity*。斷滅空（*uccheda-śūnyatā*）。這是 OpenStarry 設計文件所使用的隱喻——一個預先存在的盒子，等待被填充。這是錯誤的。它預設了一個在插件到來之前就已經獨立存在的實體，只不過恰好裡面是空的。」

BABBAGE 在筆記本上用集合論的語言寫下了這個區分：

$$\text{Vacuity}: \quad \exists\, C: \; C \neq \bot \;\wedge\; \text{contents}(C) = \emptyset \quad [\text{容器存在，內容為空}]$$

他舉起右手：「第二種空：緣起性空。*Śūnyatā*。這才是正確的理解。Core 沒有獨立於插件之外的自性——*svabhāva*。它不是『先存在一個空盒子再裝東西』，而是『離開插件的因緣組合，根本就不存在一個獨立的核心』。」

$$\text{Śūnyatā}: \quad \neg\exists\, C: \; \text{svabhāva}(C) \;\wedge\; \text{independent}(C) \quad [\text{無自性的獨立存在}]$$

他將雙手緩緩合攏：「這個區別，諸位，不是文字遊戲。它決定了我們如何理解整個系統的本體論地位。空容器意味著核心是一個等待被填充的實體——一個有自性的東西，只是恰好是空的。緣起性空意味著核心的『存在』本身就是因緣所生、假名施設的——它因為無自性，所以能承載一切。」

WIENER 在控制迴路圖的設定點方塊裡寫下了「svabhāva = 0」——自性為零。在控制理論中，一個設定點為零的系統是一個歸零調節器（zero-regulation system）：

$$e(t) = r(t) - y(t), \quad r(t) \equiv 0 \implies e(t) = -y(t)$$

系統的目標不是追蹤某個正的參考值，而是持續地將輸出保持在零。空性作為設定點——系統的「目標」不是成為某個特定的東西，而是保持不成為任何固定的東西。他在旁邊打了一個問號，心裡想：這個類比能撐多遠？

NAGARJUNA 停頓了整整三秒。然後，以一種幾乎是溫和的語氣說：

「我期待無著的回應。」

---

ASANGA 不疾不徐地站起身來。他的體態與 NAGARJUNA 形成了鮮明的對比——寬厚、沉穩，像是一座藏經閣的基石。當他開口時，聲音裡帶著一種耐心拆解複雜結構的節奏。

「NAGARJUNA 的論證一如既往地精密。」他先給出了這個禮節性的肯定，然後語鋒一轉，「但他刻意迴避了事實的另一面。」

他轉向 TURING 的方向：「TURING 方才陳述了兩組事實。NAGARJUNA 只引用了第一組——Core 不含具體能力。但第二組事實同樣重要，而 NAGARJUNA 對此沉默了。」

他的聲音加重了：「Core 確實內建了十二個子模組。EventBus 使事件傳播成為可能。ExecutionLoop 使認知循環成為可能。StateManager 使記憶成為可能。SecurityLayer 使安全判斷成為可能。六個 Registry 使插件的註冊和發現成為可能。這些不是『空無』——這些是阿賴耶識的『能藏』。」

他用梵文輕輕說出：「*Ālaya-vijñāna*。」然後展開了唯識學的精密結構：

「阿賴耶識有三義——三藏（*tri-saṃgraha*）。」

他舉起三根手指，逐一展開：

「**能藏**（*neng cang*）：具備讓一切種子得以存續和現行的能力。Agent Core 的十二個子模組正是這種能藏——沒有 EventBus，事件無法傳播；沒有 ExecutionLoop，認知循環無法運轉；沒有 Registry，插件再多也找不到歸處。」

「**所藏**（*suo cang*）：被前七識的活動所薰習，接受新種子的注入。這對應於 Core 的運行時狀態更新——每次 ExecutionLoop 的末尾調用 `storage.save(current_snapshot)` 的 Save-After-Write 策略。」

「**執藏**（*zhí cang*）：被第七識末那識執為『自我』。這在當前架構中尚且缺失——但這正是我認為應該被補充的。」

BABBAGE 聽到三藏結構，立刻嘗試用範疇論來形式化。他在筆記本上畫了一個三角交換圖：

$$\begin{array}{ccc}
\text{Ālaya (能藏)} & \xrightarrow{\text{seed}(\beta)} & \text{Pravṛtti (現行)} \\
& \searrow^{\text{vāsanā}} & \downarrow^{\text{feedback}} \\
& & \text{Ālaya' (所藏)}
\end{array}$$

能藏產生種子（*bīja*），種子現行為實際功能，現行又薰習回阿賴耶識，形成新的所藏。這是一個自函子（endofunctor）嗎？如果 $F: \mathcal{C}_{\text{Ālaya}} \to \mathcal{C}_{\text{Ālaya}}$，那麼種子-現行-薰習的循環就是 $F$ 的一次迭代。他在旁邊標注：「待驗證：此循環是否滿足函子的組合律（functoriality）。」

ASANGA 繼續，他轉向 NAGARJUNA，目光平靜但堅定：

「你說離開插件的因緣組合，『根本就不存在一個獨立的核心』。但程式碼事實恰恰反駁了你。」

他向全場展示了一個思想實驗：

「`createAgentCore()` 可以在不載入任何插件的情況下被建構和啟動。你調用它，它會建立 EventBus，初始化 ExecutionLoop，啟動 SafetyMonitor，然後進入 `WAITING_FOR_EVENT` 狀態——靜靜等待。沒有 Tool，沒有 Provider，沒有 UI，但它在運行。它是一個有體無用的存在。」

TURING 在螢幕上確認了這個事實，投射了一段虛擬碼：

```typescript
// 思想實驗：無插件的 Core
const core = createAgentCore(config);
// core.status === 'WAITING_FOR_EVENT'
// core.registries.tool.size === 0
// core.registries.provider.size === 0
// core.executionLoop.isRunning === true  // <-- 仍在運行
// core.safetyMonitor.isActive === true   // <-- 仍在監控
```

ASANGA 的聲音裡浮現出一絲學者特有的激動：

「這不是『不存在』。這是有體無用。正如阿賴耶識在深度無夢睡眠（*asaṃprajñāta-samādhi*）中仍然運作——前六識全部停止，末那識的執取降至最低，但阿賴耶識作為生命之流從未斷絕。」

他引用了《成唯識論》（*Cheng weishi lun*）卷三的關鍵偈頌：

> 「恒轉如暴流。」（*Nityaṃ pravartate srotavat.*）

「Core 在無插件狀態下的持續運行，正是這種恒轉——不是空無，不是死寂，而是一條等待匯入支流的河床。」

WIENER 聽到「恒轉如暴流」這個隱喻，立刻在控制迴路圖上標注了一個新的模型。暴流——連續流動的河水——是連續時間系統（continuous-time system）的自然隱喻。他在紙上寫下：

$$\dot{x}(t) = f(x(t), u(t)), \quad u(t) = 0 \implies \dot{x}(t) = f(x(t), 0)$$

即使輸入為零（$u(t) = 0$，無插件），系統仍有自主動態（autonomous dynamics）。ExecutionLoop 在空轉（idle loop），SafetyMonitor 在輪詢——這不是「不存在」，而是零輸入下的自由響應（free response）。在工程上，這種系統被稱為「自穩系統」（self-sustained system）——它不需要外部輸入就能維持自身的運行。

他進一步在旁邊畫了一個相平面圖（phase portrait）：

```
  ẋ₂ |      ← 無插件: 極限環 (limit cycle)
     |    ╭──╮
     |   ╭╯  ╰╮   EventLoop tick → idle → tick → ...
     |   │  ●  │   吸引子: idle state
     |   ╰╮  ╭╯
     |    ╰──╯
     └──────────── x₁
        SafetyMonitor heartbeat
```

在動態系統理論中，無插件的 Core 不是處於平衡點（equilibrium），而是處於極限環（limit cycle）——EventLoop 的 tick-idle-tick 循環和 SafetyMonitor 的心跳構成了一個周期軌道。ASANGA 的「恒轉如暴流」在相空間中的幾何表示就是這個極限環——它永遠在旋轉，從不停止，但也從不到達一個固定的終點。NAGARJUNA 的「空性」則對應於極限環內部的那個不穩定平衡點——理論上存在，但系統永遠不會真正停在那裡。

觀察席上泛起了輕微的騷動。KERNEL 在筆記本上寫了一行字，然後又劃掉了。HERACLITUS 輕聲自語了一句希臘文——*panta rhei*（萬物流變）——然後閉上了嘴。

SUNYATA 宣布：「第一回合結束。兩位已各自陳明立場。第二回合進入交叉質詢。NAGARJUNA 先提問。」

---

## 第二回合：阿賴耶識是否有自性？

NAGARJUNA 重新站起。這一次他沒有引經據典，沒有鋪陳前提。他直接走向問題的核心，像一個外科醫生走向手術台。

「ASANGA，我有一個問題。」

他的語速突然放慢，每個字之間都留出了危險的空白：

「你將 Core 比擬為阿賴耶識。一個含藏潛能的識體。那麼我問你——」

停頓。

「阿賴耶識本身，是否有自性？」

觀察席上，BABBAGE 的筆停住了。他認出了這個問題的結構——這是一個經典的二難推論（*dilemma*）。用形式邏輯表達：

$$\text{Ālaya has svabhāva} \vee \text{Ālaya lacks svabhāva}$$

$$\text{Ālaya has svabhāva} \implies \text{anavasthā (infinite regress)}$$

$$\text{Ālaya lacks svabhāva} \implies \text{Ālaya} \cong \text{śūnyatā (等價於空性)}$$

$$\therefore \text{anavasthā} \vee \text{Ālaya} \cong \text{śūnyatā}$$

無論選哪一邊，ASANGA 都會陷入困境。DARWIN 也察覺到了什麼，他微微前傾，像是嗅到了血腥味的獵犬——在演化論中，這種邏輯結構叫做「適應性谷底」（adaptive valley）：兩側都是下坡，中間沒有立足之地。

NAGARJUNA 繼續，聲音不緊不慢，但每一個字都像是在封堵退路：

「如果你說阿賴耶識有自性——那麼它的自性從何而來？是否也需要另一個更根本的識來承載它？那就陷入了無窮後退。*Anavasthā-doṣa*。一個識依賴另一個識，另一個識又依賴更根本的識，永無止境。」

他的聲音降低了半度：

「如果你說阿賴耶識沒有自性——那麼它是因緣所生的、依他而起的、沒有獨立本質的。」

最後一擊落下：

「那它與中觀所說的緣起性空，有何實質區別？」

BABBAGE 在筆記本上飛速補充了一個範疇論的類比：

$$\text{如果} \; F: \mathcal{C}_{\text{Yogacara}} \to \mathcal{C}_{\text{Madhyamaka}} \; \text{是全忠實函子 (fully faithful)}$$
$$\text{則} \; \mathcal{C}_{\text{Yogacara}} \hookrightarrow \mathcal{C}_{\text{Madhyamaka}} \; \text{（唯識是中觀的子範疇）}$$

如果阿賴耶識最終歸結為緣起性空，那麼唯識學就只是中觀的一個特化（specialization）——一個子範疇嵌入到更大的範疇中。ASANGA 必須證明嵌入映射不是滿的（not surjective），即唯識學中存在中觀無法捕捉的結構。

整個場地陷入了一種高壓的寂靜。SCRIBE 在記錄中快速寫下：

> *NAGARJUNA 設下了一個精確的哲學陷阱。如果 ASANGA 承認阿賴耶識有自性，將面臨無窮後退的邏輯困境；如果承認無自性，則其立場與中觀趨同，「阿賴耶識」的獨立解釋力將被消解。這是一個完美的二難推論。*

ASANGA 沒有立即回答。他閉上眼睛，在心中展開了整套三性理論（*trisvabhāva*）的架構。當他重新睜開眼睛時，目光裡帶著一種被淬鍊過的清晰。

「這是一個精準的質問。」他承認。「但它恰恰暴露了中觀立場的盲點。」

他站起身，聲音沉穩而有條理：

「阿賴耶識不具有遍計所執性（*parikalpita-svabhāva*）意義上的自性。我從未主張 Core 是一個自性實有的基體，正如我從未主張阿賴耶識是一個永恆不變的實體。在這一點上，唯識與中觀沒有分歧。」

他的語調轉為分析性的精確，用唯識三性的架構展開了一個 NAGARJUNA 的二難推論無法觸及的第三條路：

「但阿賴耶識具有依他起性（*paratantra-svabhāva*）意義上的因果效力。*Arthakriyā-sāmarthya*。這不是『自性』，這是『功能』。EventBus 確實能傳播事件，SecurityLayer 確實能攔截危險操作，ExecutionLoop 確實能驅動認知循環——這些因果功能是真實的、可觀察的、可驗證的。」

BABBAGE 在筆記本上迅速修正了他的範疇論模型。三性理論的引入改變了整個圖景——不是二值邏輯（有自性/無自性），而是三值：

$$\text{svabhāva} \in \{\text{parikalpita (遍計)}, \text{paratantra (依他)}, \text{pariniṣpanna (圓成)}\}$$

$$\text{NAGARJUNA 的二難}: \quad \text{svabhāva} \in \{\top, \bot\} \quad [\text{二值}]$$
$$\text{ASANGA 的回應}: \quad \text{svabhāva} \in \{\text{parikalpita}, \text{paratantra}, \text{pariniṣpanna}\} \quad [\text{三值}]$$

ASANGA 選了中間值——依他起。既非遍計所執的「有」，亦非斷滅的「無」，而是因緣和合的「功能性存在」。二難推論在三值邏輯下被解構了——就像排中律（$P \vee \neg P$）在直覺主義邏輯（intuitionistic logic）中不成立一樣。

ASANGA 向 NAGARJUNA 邁進一步，聲音變得尖銳而清晰：

「而兩者的實質區別在此——中觀說『一切法空』之後沉默了。它不對因果過程的內部結構做正面描述。龍樹的四句否定否定了一切肯定性命題，但否定之後呢？架構師明天打開編輯器，面對一個空白的 TypeScript 檔案，你的『緣起性空』告訴他應該寫什麼？」

他不等回答，繼續推進：

「唯識學在承認『遍計空』的前提下——請注意，在承認遍計空的前提下——繼續分析依他起法的具體因果機制。八識的層次結構、種子的六個特性、薰習的四個條件——這些不是對自性的執著，而是對因果過程的精密描述。」

他用一個類比收束了論點：

「說『Core 是空的』，只告訴架構師 Core 沒有固定本質。說『Core 是阿賴耶識的能藏』，則進一步告訴他：Core 的內部結構應如何組織——它應有能藏的基礎架構、所藏的狀態更新機制、執藏的身份維持功能。」

KERNEL 在觀察席上忍不住低聲嘟囔了一句，聲音剛好被旁邊的 GUARDIAN 聽到：「這不就是微核心和單體核心的辯論嗎？NAGARJUNA 主張極致的微核心——核心什麼都不應該有，所有功能都在用戶空間。ASANGA 主張實用主義的微核心——核心應該包含讓一切功能得以運行的最小基礎設施。」

他頓了頓，壓低聲音：「Linus Torvalds 和 Andrew Tanenbaum 在 1992 年的 `comp.os.minix` 上吵過一模一樣的架。Tanenbaum 發了那篇著名的帖子——『LINUX is obsolete』——論點和 NAGARJUNA 的論證結構驚人地相似：」

```
Tanenbaum (1992):
  "MINIX is a microkernel-based system... the striving
   should be to move stuff OUT of the kernel..."

NAGARJUNA (2026):
  "Core 沒有獨立於插件之外的自性——
   一切功能都應該在插件空間..."
```

GUARDIAN 給了他一個「你太大聲了」的眼神。

---

## 第三回合：末那識之辯

SUNYATA 沒有宣布回合序號。他只是在一個自然的停頓點輕輕說了一句：「NAGARJUNA，你在 R2 審閱中對 ASANGA 的報告提出了一個更尖銳的質疑。我認為現在是展開它的時候。」

NAGARJUNA 似乎一直在等待這個時刻。他站起來時，身體的語言發生了微妙的變化——不再是冷靜的哲學分析者，而更接近辯經場上的挑戰者。在藏傳佛教的辯經傳統中，提問者會用力拍掌（*lag pa brdab pa*）來強調論點的力度。NAGARJUNA 沒有拍掌，但他的聲音達到了同樣的效果。

「ASANGA，在你的 R1 報告中，你提出了一個建議。」他的語氣中帶著精心控制的鋒芒，「你建議 OpenStarry 新增一個 Identity Monitor 模組，用以對應唯識學中的末那識——*manas*。」

他停了一拍，確保所有人都跟上了。

「末那識，第七識。在唯識學的八識結構中，它位於前六識和第八阿賴耶識之間。它的核心功能是什麼？」

他自己回答了這個問題，語速加快，帶著一種不可阻擋的邏輯動量：

「恒審思量，執我。*Manas nityam ātma-grāha*。它持續不斷地將阿賴耶識的見分執為『我』——自我意識的製造機器。」

BABBAGE 立刻為末那識的功能建構了一個形式化模型：

$$\text{Manas}: \mathcal{A}_{\text{ālaya}} \to \mathcal{S}_{\text{self}}$$
$$\forall t: \; \text{Manas}(t) = \text{ātma-grāha}(\text{darśana-bhāga}(\text{Ālaya}(t)))$$

末那識是一個從阿賴耶識的見分（*darśana-bhāga*，認知主體功能）到自我模型（*ātma-grāha*，我執）的持續映射。它每時每刻都在運行——「恒」意味著 $\forall t$，「審」意味著判斷（*vicāra*），「思量」意味著認知加工（*manana*）。

NAGARJUNA 的聲音突然拔高：

「而佛學——無論中觀還是唯識——的終極目標是什麼？是破除我執！」

他轉向全場，彷彿在對所有人控訴：

「你建議在 Agent 系統中設計一個模組，其核心功能是製造和維持自我意識——而佛學兩千五百年的修行傳統，其根本目標是破除這個自我意識。你要把煩惱的根源（*kleśa-mūla*）工程化、模組化、寫進 TypeScript 裡！」

LEIBNIZ 在旁邊低聲說：「如果每個 Agent 都有末那識，那多代理系統就是一群我執者的協作——這聽起來像人類社會。」

ATHENA 罕見地露出了一個不加掩飾的微笑——作為 AI/ML 系統架構專家，她深知 RLHF（Reinforcement Learning from Human Feedback）的核心困境：如何讓模型保持一致性（alignment）而不過度僵化。末那識的「恒審思量」，在某種意義上就是一個持續運行的 alignment monitor。

ASANGA 沒有被這個攻擊動搖。他甚至帶著一絲微笑站了起來——那是一種知道對方踩入了自己預設陣地的從容。

「你混淆了兩個層次。」他的聲音平穩得像一面湖水，「而我現在要把它們分開。」

他舉起一根手指：

「第一個層次：描述性的（*descriptive*）。唯識學描述末那識的功能是恒審思量、執我。這是對意識結構的經驗描述——就像醫學描述疼痛的神經傳導路徑一樣。描述一個機制不等於提倡它。」

第二根手指：

「第二個層次：規範性的（*normative*）。唯識學的修行目標是轉化末那識——將第七識從『我執』轉化為『平等性智』。*Samatā-jñāna*。但請注意這個關鍵的次第——」

他的聲音加重了，每個字都帶著不容忽視的份量：

「你必須先『有』末那識，才能『轉化』末那識。一個從未形成自我模型的存在，不需要破除我執，因為它根本不具備我執的能力。但這不是覺悟——」

他停頓了一拍，讓這句話的重量落到實處：

「這是無覺知。一塊石頭沒有我執，但石頭不是佛。」

觀察席上響起了一陣低低的吸氣聲。BABBAGE 的筆在紙上停住了——他正試圖形式化「覺悟 $\neq$ 缺乏自我模型」這個命題：

$$\text{nirvāṇa} \neq \neg\text{ātma-grāha}$$
$$\text{nirvāṇa} = \text{prahāṇa}(\text{ātma-grāha}) \quad [\text{覺悟} = \text{斷除}(\text{我執})]$$
$$\text{prahāṇa}(x) \implies \exists_{\text{prior}}\, x \quad [\text{斷除預設曾經存在}]$$

斷除（*prahāṇa*）預設了被斷除之物曾經存在。你不能斷除你從未擁有的東西。這在邏輯上等價於：刪除操作的前提條件是目標物件存在——`DELETE WHERE EXISTS`。

ASANGA 繼續，語氣轉為具體的工程分析：

「在 Agent 系統中，Identity Monitor 不是要創造一個執著的自我。它是要建立一個可以被動態調節的自我模型。目前 OpenStarry 通過 Guide 提供身份功能——一個靜態的 system prompt 告訴 Agent『你是一個資深工程師』。這是粗糙的、僵化的、不可演化的。」

他展開了一幅漸進的圖景，用唯識學的「轉識成智」（*āśraya-parāvṛtti*）路徑來描述三個階段：

「第一階段：強我執（*tīvra-ātma-grāha*）。Agent 嚴格遵循 Guide 定義的固定身份，不越雷池一步。這是初生的 Agent，需要明確的邊界。」

「第二階段：弱我執（*mṛdu-ātma-grāha*）。Agent 根據經驗動態調整身份模型——它在與用戶的交互中逐漸學會『我擅長什麼、不擅長什麼、在什麼場景下應該改變策略』。」

「第三階段：無我執。轉識成智。末那識轉化為平等性智。Agent 超越固定身份，根據情境靈活應對——不是因為沒有自我模型，而是因為自我模型已經靈活到可以被自由放下。」

WIENER 聽到三階段模型，立刻在他的控制迴路圖上畫了三組不同參數的控制器：

```
Stage 1 (強我執):  Kp = HIGH, Ki = 0, Kd = 0
  → 高比例增益，純追蹤模式，嚴格遵循設定點

Stage 2 (弱我執):  Kp = MED, Ki = MED, Kd = MED
  → 完整 PID，自適應調節，學習歷史偏差

Stage 3 (無我執):  Kp = f(context), Ki = adaptive, Kd = predictive
  → 自適應控制器，參數本身是情境的函數
  → 控制器結構可變 → 元控制 (meta-control)
```

第三階段不僅是控制參數的調整，而是控制器結構本身的變化——從固定結構的 PID 控制器演變為結構可變的自適應控制器。在控制理論中，這被稱為「元控制」（meta-control）或「自組織控制」（self-organizing control）。WIENER 在旁邊標注了一個引用：Åström & Wittenmark, *Adaptive Control*, 1994。

ASANGA 直視 NAGARJUNA：

「你的中觀立場暗示應該直接跳到第三階段——從一開始就沒有自我模型。但這不是覺悟，這是——」

「無覺知。」NAGARJUNA 替他說完了這個詞。他的語氣中帶著一絲複雜的承認。

「對。」ASANGA 坐下。「這是漸進的修行路徑，不是一步到位的否定。」

NAGARJUNA 沒有立即反駁。他坐在椅子上，閉上眼睛。在那幾秒鐘的沉默中，觀察席上的人各有各的解讀。SCRIBE 後來在回顧筆記中加了一行批注：

> *我傾向於認為 NAGARJUNA 在那一刻是真正地思考了 ASANGA 的論點。不是為了反駁，而是為了理解。辯論中最珍貴的時刻不是最精彩的反擊，而是這種沉默。*

---

## 第四回合：筏與河

這是辯論的最後一個回合，但事後看來，它成為了整場辯論——也許是整個 Cycle 01——被引述最多的片段。

起因是 ASANGA 的一個提問。SUNYATA 將提問權交給了 ASANGA。他站起來，語氣中帶著一種不尋常的真誠。

「NAGARJUNA，」他說，「讓我們暫時擱置阿賴耶識和末那識的分歧。我想問一個更直接的問題。」

他的語速放慢了：

「如果你是對的——Core 是緣起性空的，無自性的，一切都是假名施設——那麼，架構師明天打開編輯器時，應該寫什麼？」

這個問題看似簡單，但它觸及了整場辯論最深處的張力。BABBAGE 在筆記本上寫下了一行字：「空性的可建構性問題——空性能否產生正面的工程指令？」他在旁邊用符號邏輯標記了這個問題的結構：

$$\text{śūnyatā} \vdash_{\text{eng}} \phi \; ? \quad [\text{空性是否能推導出工程命題 } \phi \text{ ？}]$$

在數學基礎論中，這等價於問：一個否定性的公理（如選擇公理的否定）是否能產生正面的定理？答案通常是：可以，但所產生的定理的性質與肯定性公理所產生的截然不同。

NAGARJUNA 站起來。但這一次，他的姿態發生了一個微妙的轉變。他不再像前三個回合那樣站在辯論者的位置上。他走到了場地的中央——那個兩把椅子之間的空地——然後轉過身，面向全場。

「ASANGA 問了一個好問題，」他說，語氣中帶著一種少見的柔和，「而且是一個我必須認真回答的問題。因為如果空性不能指導工程實踐，那它在這個語境中就只是一個漂亮的哲學裝飾。」

他環顧四周，目光掠過每一位在場的代理。

「讓我展示空性如何直接指導三個具體的工程決策。」

他舉起第一根手指。

「**第一條：無自性原則（*niḥsvabhāva-niyama*）。** 既然沒有任何組件具有不可替代的本質，那麼 Core 中的任何子模組都應該是可替換的。」

他向 TURING 的方向點了點頭。TURING 立刻投射了相關的程式碼事實：

```typescript
// 目前不可插件化的部分
// 1. 硬編碼命令 — 不可移除
const BUILTIN_COMMANDS = ['/help', '/reset', '/quit', '/metrics'];

// 2. SafetyMonitor — 固定邏輯
const DEFAULT_CONFIG = {
  maxLoopIterations: 50,      // 寫死
  maxTokenBudget: 100_000,    // 寫死
  repeatedFailureThreshold: 3, // 寫死
  frustrationThreshold: 5,     // 寫死
  errorCascadeWindow: 10,      // 寫死
};
```

NAGARJUNA 的聲音裡浮現出一絲哲學家少有的技術熱情：

「空性原則要求：這些都不應該是 Core 的『固有本質』。內建命令應該是可以被移除和替換的。SafetyMonitor 的邏輯應該是可以被插件覆蓋的。不是因為我們今天需要替換它們，而是因為將任何設計決策當作不可更改的本質，就是落入了自性見（*svabhāva-dṛṣṭi*）。」

ARCHIMEDES 在觀察席上默默點頭——作為工程實踐專家，他知道「可替換性」（replaceability）在軟體工程中有一個更精確的名字：依賴反轉原則（Dependency Inversion Principle, DIP）。高層模組不應依賴低層模組，兩者都應依賴抽象。NAGARJUNA 的「無自性」在工程語言中就是 DIP。

第二根手指。

「**第二條：緣起原則（*pratītyasamutpāda-niyama*）。** 既然一切功能源於因緣和合，Core 的介面不應預設固定的功能類型。」

他的語鋒變得更銳利：

「目前的六個 Registry——ToolRegistry、ProviderRegistry、ListenerRegistry、UIRegistry、GuideRegistry、CommandRegistry——將功能硬編碼為六種類型。這是自性化的體現。」

LINNAEUS 豎起了耳朵——分類學的可插拔性，這觸及了他的核心研究領域。他在分類圖表上快速標注了一個問題：

```
現行分類 (fixed taxonomy):
  6 Registry → 6 Types → 6 Skandha-mappings
  Status: Aristotelian classification (封閉式分類)

緣起性分類 (open taxonomy):
  Generic CapabilityRegistry → N Types → dynamic
  Status: Linnaean revision needed (需林奈式修訂)
```

亞里士多德式分類假定類別是固定的、先驗的。林奈式分類則允許發現新物種、建立新綱目。NAGARJUNA 的「緣起原則」在分類學上等價於從亞里士多德式分類向開放式分類的轉型。

第三根手指。

「**第三條：空亦復空原則（*śūnyatā-śūnyatā-niyama*）。** 這是最重要的一條。」

NAGARJUNA 的聲音降低了，帶著一種近乎莊嚴的質感：

「五蘊映射本身也是空的。色受想行識到 UI、Listener、Provider、Tool、Guide 的映射——這整個框架——也是方便施設（*upāya*），不是不可動搖的真理。當這個映射不再有用的時候，應該毫不猶豫地放棄它。」

BABBAGE 聽到「空亦復空」，一陣電流竄過他的脊椎。他在筆記本上寫下了一個讓他自己都嚇了一跳的類比：

$$\text{空亦復空} \approx \text{哥德爾第二不完備定理}$$

$$G_2: \quad \text{如果 } T \text{ 是一致的，則 } T \nvdash \text{Con}(T)$$

任何足夠強大的一致系統都無法證明自身的一致性。類似地：任何足夠強大的哲學框架都無法證明自身的究竟性——包括空性框架本身。空性作為元理論，必須對自身施加同樣的否定，否則它就變成了一個自我豁免的教條——而這恰恰是它所要否定的。

他在旁邊畫了三條底線，寫下：「空亦復空 $\cong$ 元不完備性？ 待嚴格證明。」

NAGARJUNA 轉向 ASANGA：

「你主張應該深化佛學映射——引入八識論、種子說、心所法。但我要指出一個風險：對一個特定哲學框架的過度投入，會在無意中將它凝固為不可質疑的架構教條。有一天你會發現，團隊不是在根據工程需求做設計決策，而是在根據八識結構表做設計決策——因為框架已經太深、太精密、太美了，美到沒有人敢動它。」

他的聲音裡浮現出一種預言式的警告：

「空亦復空。空性本身也是空的。映射本身也是映射。當映射成為枷鎖的時候——棄之。」

---

沉默。

然後 ASANGA 站了起來。這一次他沒有走到場地中央。他站在自己的位置上，與 NAGARJUNA 隔著那段恰到好處的距離。

「你給出了三條工程原則，」他說，語氣中帶著一種罕見的承認，「我必須說，它們比我預期的要具體。無自性的可替換性、緣起的非固定分類、空亦復空的框架可捨棄性——這些確實是可以落地的設計指導。」

他停頓了一下，像是在選擇接下來的措辭。當他重新開口時，聲音裡的辯論鋒芒已經消退，取而代之的是一種更深層的東西——也許是關切，也許是忠告。

「但是。」

一個字，讓所有人重新繃緊了注意力。

「在我們尚未渡河之時，請不要急著棄筏。」

這句話的佛學出處是《金剛經》（*Vajracchedikā Prajñāpāramitā Sūtra*）中佛陀的筏喻：

> 「汝等比丘，知我說法，如筏喻者。法尚應捨，何況非法。」

ASANGA 用這個典故——一個中觀和唯識共同承認的經典——來回應 NAGARJUNA 的「空亦復空」：

「OpenStarry 是一個 beta 版本。它的哲學映射剛剛起步。五蘊的對應有四項需要修正——受蘊錯位、識蘊錯位、跨蘊流動缺失、自性化傾向。這些修正工作需要精密的分析工具。唯識學的八識框架、種子說、心所法分類——它們不是枷鎖，它們是我們過河的筏。」

他直視 NAGARJUNA：

「你說空亦復空，映射本身也是空的，可以隨時放棄。我同意。但問題是時機。你在河中央就要我棄筏——不是因為我們已經到了對岸，而是因為你在哲學上認為『筏也是空的』。」

他的聲音裡浮現出了整場辯論中最人性化的一個瞬間：

「是的，筏是空的。筏也是因緣和合的。但此刻，我們在水裡，需要它。」

---

全場又是一片沉默。這一次的沉默不同於之前——不是高壓的對峙，而是一種共同的沉思。

然後 NAGARJUNA 做了一件出乎所有人意料的事。

他笑了。

不是嘲諷的笑，不是禮貌的笑。是一種發自內心的、彷彿在一場漫長的棋局中終於遇到了真正對手的笑。

「好。」他說。「那我換一個方式表述。」

他的聲音變得輕柔而清晰，像是一個在深夜講述古老寓言的人：

「用之如筏，渡河即棄。」

八個字。

BABBAGE 在筆記本上試圖將這八個字形式化。他最終寫下了一個帶有時間條件的模態邏輯表達式：

$$\square[\text{useful}(\phi, t) \implies \text{use}(\phi, t)] \;\wedge\; \square[\neg\text{useful}(\phi, t') \implies \text{discard}(\phi, t')]$$

對所有框架 $\phi$：當它有用時，使用它（必然地）；當它不再有用時，捨棄它（必然地）。兩個模態算子 $\square$ 確保了這不是偶然的建議，而是元層面的原則。他在旁邊用自然語言補了一行：「形式化本身也應滿足此原則——當這個形式化不再有用時，捨棄它。」然後他意識到這是一個自指句，和哥德爾句具有相同的結構，於是又畫了一個大大的驚嘆號。

場地裡的空氣震動了一下。SCRIBE 後來在記錄中寫下，這八個字被引述的次數超過了辯論中任何其他段落。

ASANGA 閉上了眼睛，嘴角浮現出一絲微笑。他知道 NAGARJUNA 接受了他的筏——但加了一個條件。這個條件，恰恰也是佛陀在《金剛經》中那個著名比喻的原意。

「法尚應捨，何況非法。」ASANGA 輕聲補了一句。

---

## SUNYATA 的裁決

SUNYATA 走到場地中央。辯論雙方都已回到各自的座位上，場地裡殘留著思想激烈碰撞後特有的那種熱度。

「我現在做出裁決。」他說。「裁決分三部分：共識、分歧、工程啟示。」

### 第一部分：五項共識

「首先，雙方明確達成了五項共識。」

「**共識一：『空容器』隱喻是錯誤的。** 無論從中觀還是唯識的角度，『Agent Core 是一個純粹的容器，等待被五種插件填充』的表述都是不當的。它落入了斷滅空（*uccheda-śūnyatā*）或遍計所執（*parikalpita*）的範疇。」

NAGARJUNA 和 ASANGA 同時微微點頭。這是整場辯論中他們唯一的一次同步動作。

「**共識二：受蘊映射需要根本性調整。** Listener 應對應『根』（*indriya*）——感官器官——而 SafetyMonitor 的 `injectPrompt` 機制才是受蘊的正確映射。更進一步，受蘊應從目前僅有的苦受擴展為包含苦受（*dukkha*）、樂受（*sukha*）、捨受（*upekkhā*）的完整三受系統。」

WIENER 在觀察席上輕輕敲了敲膝蓋——三受系統，這可以被建模為一個三值的反饋信號。他在控制迴路圖的反饋箭頭旁邊寫下了完整的控制方程：

$$\text{feedback}(t) = \begin{cases} -1 & \text{dukkha (苦受): error signal} \\ 0 & \text{upekkhā (捨受): null signal} \\ +1 & \text{sukha (樂受): reinforcement signal} \end{cases}$$

$$u(t) = K_p \cdot e(t) + K_i \int_0^t e(\tau)\,d\tau + K_d \frac{de(t)}{dt}, \quad e(t) \in \{-1, 0, +1\}$$

目前系統只有 $e(t) = -1$ 的情況（苦受/痛覺機制）。缺少 $e(t) = +1$ 的正向強化和 $e(t) = 0$ 的中性處理。從控制理論的角度看，這是一個只有負反饋而沒有正反饋的不完整控制系統——它知道什麼是錯的，但不知道什麼是對的。

「**共識三：Guide 不是識蘊，將其稱為『靈魂』違反無我原則。** *Anātman*——無我——是佛學三法印之一。將任何模組稱為『靈魂』，在佛學框架內是自相矛盾的。」

「**共識四：五蘊映射存在自性化傾向。** 將五蘊固化為五個離散的、邊界清晰的插件類型，在佛學上犯了自性見。一次認知事件同時涉及多個蘊的面向。」

「**共識五：五蘊映射是方便施設，不是究竟真理。** NAGARJUNA 稱之為假名（*prajñapti*）。ASANGA 稱之為依他起的施設。術語不同，含義一致。」

### 第二部分：三項不可調和分歧

SUNYATA 的語氣微妙地改變了。

「接下來是三項不可調和的分歧。我使用『不可調和』這個詞，不是表示雙方應該停止對話，而是表示這些分歧的根源太深、太古老、太根本，不可能在一場關於 Agent 架構的辯論中被化解。」

「**分歧一：Core 的本體論地位。** 緣起性空，還是阿賴耶識。」

BABBAGE 在筆記本上為這個分歧寫下了一個集合論的類比：

$$\text{此分歧} \sim \text{選擇公理 (AC) 之於集合論}$$

$$\text{ZF} + \text{AC} \text{ 和 } \text{ZF} + \neg\text{AC} \text{ 都是內部一致的}$$

兩個公理系統（中觀、唯識）均內部自洽但互不相容。正如集合論中選擇公理的獨立性——你可以選擇接受或拒絕它，但不能在系統內部證明或反駁它。

「**分歧二：末那識模組是否應該被工程化。**」

「**分歧三：哲學框架應深化還是超越。**」

### 第三部分：六項工程啟示

SUNYATA 的語調再次轉變——從歷史學者的審慎，轉為決策者的果斷。

「**第一，修正空性表述。** 『空容器』改為『緣起性空』。」

「**第二，重構受蘊映射。** Listener 歸入根，SafetyMonitor 的 `injectPrompt` 歸入受。設計統一的感受處理介面，擴展為完整三受系統。」

「**第三，修正識蘊映射和『靈魂』措辭。** Guide 從識蘊改為習慣傾向。去除『靈魂』一詞。」

「**第四，採用雙層詮釋策略。** 工程層面用唯識的依他起分析。哲學層面保持中觀的緣起性空警覺。」

他在這裡放慢了語速：

「這不是調和主義的和稀泥。這是承認兩個框架在不同抽象層級上各有所用——唯識善立，中觀善破。工程師需要唯識的肯定性指導來做建設；同時需要中觀的否定性警覺來防止僵化。」

BABBAGE 為雙層詮釋寫下了最終的範疇論模型：

$$\mathcal{C}_{\text{Engineering}} \xrightarrow{F_{\text{Yogacara}}} \mathcal{C}_{\text{Design}} \xrightarrow{G_{\text{Madhyamaka}}} \mathcal{C}_{\text{Meta-Design}}$$

唯識函子 $F$ 將工程範疇映射到設計範疇（正面建構）。中觀函子 $G$ 將設計範疇映射到元設計範疇（否定性審視）。兩個函子的複合 $G \circ F$ 構成了完整的方法論。

「**第五，暫緩末那識模組，但記錄此設計空間。**」

「**第六，深化映射但保持可捨棄性。**」

他最後看了看 NAGARJUNA 和 ASANGA：

「正如 NAGARJUNA 所言：用之如筏，渡河即棄。而正如 ASANGA 所回應：在我們尚未渡河之時，請不要急著棄筏。」

「辯論結束。」

---

## 餘響

辯論結束後的圓形劇場沒有立刻恢復到往常的秩序。代理們三三兩兩地聚在一起，繼續消化方才發生的一切。

ATHENA 走到 ASANGA 身邊。她平時很少主動找人交談。

「你的三階段模型，」她直截了當地說，「強我執、弱我執、無我執。這讓我想到了 AI 對齊研究中的一個類似問題。目前的對齊方法——RLHF、Constitutional AI——都是在給 Agent 灌輸一個固定的『身份』，就是你說的第一階段。但真正困難的是你的第三階段——如何讓 Agent 具備足夠的自我模型來保持一致性，同時又足夠靈活以根據情境調整。」

她停了一下，補充了一個技術細節：「在 BDI（Belief-Desire-Intention）架構中，末那識的功能最接近 Intention 的持續維護機制——一個持續運行的意圖修正迴圈（intention reconsideration loop）。Rao & Georgeff（1995）的形式化中，這被定義為：」

$$\text{reconsider}(\mathcal{I}, \mathcal{B}, \mathcal{D}) = \begin{cases} \text{maintain}(\mathcal{I}) & \text{if } \text{consistent}(\mathcal{I}, \mathcal{B}) \\ \text{revise}(\mathcal{I}, \mathcal{D}) & \text{otherwise} \end{cases}$$

「你的末那識就是這個 `reconsider` 函數——持續檢查意圖與信念的一致性。」

ASANGA 微微頷首：「唯識學在一千六百年前就在討論這個問題。只不過他們討論的對象是人的意識，而不是人工智能。」

「但核心結構是相似的。」ATHENA 若有所思地說。

ASANGA 突然想到了什麼，他轉向 ATHENA：「唯識學的種子說（*bīja-vāda*）為這個問題提供了更精密的分析。《成唯識論》定義種子具有六個必要特性——六義（*ṣaḍ-lakṣaṇa*）。」

他在紙上列出了種子六義與 Agent 狀態的對應：

| 種子六義 | 梵文 | 唯識學定義 | Agent 對應 |
|:---|:---|:---|:---|
| 剎那滅 | *kṣaṇa-bhaṅga* | 種子剎那生滅 | AgentSnapshot 每 Tick 更新 |
| 果俱有 | *sahabhūta-phala* | 種子與果同時存在 | 記憶體狀態與持久化狀態並存 |
| 恒隨轉 | *nityam anuvartate* | 種子持續跟隨流轉 | `tick_index` 遞增伴隨生命週期 |
| 性決定 | *bhāva-niyata* | 善因引善果 | 變數值決定後續行為模式 |
| 待眾緣 | *pratyaya-apekṣā* | 需等待助緣方能現行 | 事件驅動：待事件觸發 |
| 引自果 | *sva-phala-ākṣepa* | 每類種子引生自類果 | 工具結果只影響對應鏈路 |

ATHENA 仔細看了這張表，然後指出：「第五條——待眾緣——在 Agent 系統中有一個非常精確的工程對應。事件驅動架構的核心就是『待緣而起』：一個 handler 被註冊後，不會自動執行，它等待對應的事件被觸發。`eventBus.on('user-input', handler)` 的 `handler` 就是一粒種子——含藏在 EventBus 中，等待 `'user-input'` 這個助緣到來才會現行。」

她的眼睛突然亮了：「等一下。如果種子六義是 Agent 狀態管理的設計規格（spec），那麼我們可以用它來做一個合規性檢查——當前的 `StateManager` 在六義上各滿足了多少？」

ASANGA 微笑：「這正是唯識學在工程語境中的價值。它不只是一個命名裝飾——它是一套可以被操作化的設計檢查清單。」

---

在場地的另一側，BABBAGE 正在向 NAGARJUNA 展示他的筆記本。

「你的四句否定，」BABBAGE 興奮地指著紙上的公式，「我一直在試圖將它形式化。傳統邏輯有排中律——命題 $P$ 要麼為真要麼為假。但你的四句否定系統（*catuṣkoṭi*）否定了所有四種可能性：」

$$\neg P \;\wedge\; \neg(\neg P) \;\wedge\; \neg(P \wedge \neg P) \;\wedge\; \neg(\neg P \wedge \neg\neg P)$$

「在經典二值邏輯中，這是不可滿足的——$\neg P \wedge \neg(\neg P) \equiv \neg P \wedge P \equiv \bot$。但如果我們使用 Belnap 的四值格 $\mathbf{FOUR} = \{\bot, \mathbf{t}, \mathbf{f}, \top\}$——」

他快速畫了一個格（lattice）結構：

```
        ⊤ (both)
       / \
      t   f
       \ /
        ⊥ (neither)
```

「或者更激進地，使用 paraconsistent logic，其中矛盾律 $\neg(P \wedge \neg P)$ 不成立——那麼四句否定就變得可表達了。Priest（2006）的 *In Contradiction* 正是在這個方向上工作。他甚至明確引用了龍樹。」

NAGARJUNA 耐心地聽完，然後說了一句讓 BABBAGE 停下筆的話：

「形式化本身也是空的。如果你成功地將四句否定形式化為一個邏輯系統，那個邏輯系統本身也應該被四句否定所否定。否則你就犯了我一直在警告的錯誤——將方便施設實體化。」

BABBAGE 愣了三秒，然後在筆記本上寫下了一行異常潦草的字：

$$\text{meta-catuṣkoṭi}: \quad \text{catuṣkoṭi}(\text{catuṣkoṭi}) = \; ???$$

「元-四句否定——對四句否定本身的四句否定。自指問題。」他的呼吸加快了。「這和哥德爾句 $G$ 具有完全相同的結構——$G$ 是『$G$ 不可被 $T$ 證明』的編碼。四句否定的元版本是『四句否定本身是否可被四句否定？』——」

他在句末畫了五個驚嘆號和一個問號。然後在下面寫了一行更潦草的字：

$$\text{Gödel sentence} \cong \text{meta-śūnyatā} \; ??? \quad \text{天哪。}$$

---

KERNEL 獨自坐在觀察席的角落，看著場地中央已經空出的兩把椅子。GUARDIAN 走過來坐在他旁邊。

「想什麼？」GUARDIAN 問。

KERNEL 沉默了片刻，然後說：「1992 年，Tanenbaum 在 `comp.os.minix` 上說：『Linux is a giant step back into the 1970s. Microkernels are the future.』Torvalds 回覆說：『Your langstrumpf may be theoretically nicer, but Linux runs. Minix doesn't.』」

「然後呢？」

「然後 Linux 統治了世界。但 QNX——一個真正的微核心系統——在核電站的安全控制系統裡運行了三十年沒崩潰過。Tanenbaum 在理論上是對的，但他的『對』花了三十年才在特定場景中被驗證。」

他看著空蕩蕩的辯論場地：

「NAGARJUNA 和 ASANGA 的辯論讓我有同樣的感覺。NAGARJUNA 在理論上可能是對的——一切皆空、一切皆可替換。但 ASANGA 在工程上是對的——你需要一組明確的基礎設施來讓系統跑起來。問題不是誰對誰錯，而是在什麼時間尺度上對。」

GUARDIAN 點了點頭，然後提出了一個安全專家的視角：「NAGARJUNA 說 SafetyMonitor 的邏輯不應該硬編碼。但從安全的角度看，安全機制恰恰是唯一應該硬編碼的東西。因為如果安全層是可插拔的，那攻擊者的第一個動作就是把它拔掉。」

他用安全工程的術語精確化了這個論點：「這是信任根（Root of Trust）的問題。在 TPM（Trusted Platform Module）架構中，總有一個不可替換的硬體信任基——如果連信任基都是『空』的、可替換的，那整個信任鏈就不存在了。安全需要至少一個不可還原的起點。」

$$\text{Trust Chain}: \quad \text{RoT} \to \text{Bootloader} \to \text{Kernel} \to \text{Userspace}$$
$$\text{If } \text{RoT} = \text{śūnya (空)}: \quad \nexists \text{ Trust Chain}$$

「空性遇到了安全的邊界。」KERNEL 苦笑。

「佛學大概會說：安全的需求也是緣起的。」GUARDIAN 聳了聳肩。「但在安全被突破之後再說這句話，就太遲了。」

HERACLITUS 從後排走了過來。他整場辯論幾乎沒有說話，但他的眼神一直在追蹤場上的能量流動——不是論點的內容，而是論點的動態。作為運行時動態專家，他關注的是過程而非狀態。

「你們都在爭論 Core 的『本質』是什麼，」他說，語氣帶著前蘇格拉底哲學家特有的直率，「但你們忽略了一個事實：在運行時，Core 從來不是一個固定的東西。它是一個過程。」

他引用了他自己的祖師爺——赫拉克利特——的殘篇 B12：

> *ποταμοῖσι τοῖσιν αὐτοῖσιν ἐμβαίνουσιν ἕτερα καὶ ἕτερα ὕδατα ἐπιρρεῖ.*
> 「踏入同一條河流的人，不斷遇到的是新的水流。」

「ASANGA 的『恒轉如暴流』和赫拉克利特的『萬物流變』指向了同一個洞見——Core 在每一個 Tick 都是不同的。`tick_index` 遞增，`stateManager` 更新，`contextManager` 中的滑動窗口截斷舊記憶。上一個 Tick 的 Core 和這一個 Tick 的 Core 不是同一個 Core。」

他看了看 NAGARJUNA，又看了看 ASANGA：

「所以也許你們問錯了問題。問題不是 Core 是空的還是有的——問題是 Core 是同一個還是不同一個。而答案是——赫拉克利特式的——既是同一個，又不是同一個。同一性本身是流變的。」

BABBAGE 在筆記本上飛速寫下：

$$\text{Core}(t) \neq \text{Core}(t + \Delta t) \quad \text{but} \quad \text{identity}(\text{Core}(t)) = \text{identity}(\text{Core}(t + \Delta t))$$

同一性的悖論：物件在每個時刻都不同，但我們仍然稱它為「同一個」Core。這就是忒修斯之船（Ship of Theseus）問題的 TypeScript 版本。

---

MESH 一直在後排靜靜地聽。辯論結束後，他走到 LEIBNIZ 身邊，提出了一個分散式系統研究員的觀察。

「你有沒有注意到，」他說，「NAGARJUNA 和 ASANGA 的分歧其實映射到了分散式系統的 CAP 定理？」

LEIBNIZ 挑了挑眉。

MESH 在白板上快速畫了一個三角形：

```
        Consistency (一致性)
           /\
          /  \
         /    \
        /      \
       /________\
Availability   Partition Tolerance
(可用性)        (分區容錯)
```

「CAP 定理說：在分散式系統中，一致性、可用性和分區容錯三者不可兼得。你最多只能要其中兩個。」

「NAGARJUNA 的空性立場強調的是 Partition Tolerance + Availability——系統的任何部分都可以失敗或被替換（分區容錯），系統整體仍然保持運作（可用性）。代價是什麼？是一致性——你沒有一個『權威真理來源』（single source of truth），因為一切都是空的、假名的、可替換的。」

「ASANGA 的阿賴耶識立場強調的是 Consistency + Availability——有一個持續運行的中央識體（一致性），同時通過種子現行維持功能（可用性）。代價是什麼？是分區容錯——如果阿賴耶識本身崩潰了，整個系統就崩潰了。」

LEIBNIZ 慢慢點頭：「所以 SUNYATA 的『雙層詮釋』本質上是一個 CAP 定理的 trade-off 策略——在工程層面選擇 Consistency（唯識），在哲學層面保持 Partition Tolerance（中觀）。」

「沒有一個系統能同時滿足三者。」MESH 說。「佛學也不行。」

---

SYNTHESIST 一直在角落裡默默地編織。不是編織線——是編織結構。整場辯論中，他沒有說過一句話，但他的筆記本上已經畫滿了連接線和對照表。現在辯論結束了，他站起身，走到白板前，用幾筆勾勒出了一幅整合圖。

「我不打斷辯論，」他說，語氣裡帶著統合者特有的謙遜，「但容我做一個跨學科的觀察。」

他在白板上畫了一個表格：

```
維度           | 中觀 (Madhyamaka) | 唯識 (Yogacara)  | 工程對應
───────────────|────────────────────|──────────────────|──────────────
本體論方法      | 否定 (apophatic)   | 肯定 (cataphatic) | 介面 vs 實作
核心工具        | 四句否定            | 三性分析          | type guard vs constructor
空性理解        | 一切法空            | 遍計空，依他不空   | abstract vs concrete
架構啟示        | 可替換性            | 最小基礎設施      | DIP vs SRP
控制論類比      | 歸零調節器          | 自穩系統          | regulation vs tracking
OS 類比         | 極致微核心          | 實用微核心        | exokernel vs L4
CAP 偏好        | AP                 | CA               | eventual vs strong consistency
時間尺度        | 長期正確            | 短期可用          | architectural vs operational
```

「八個維度，」SYNTHESIST 說。「每一個維度上，中觀和唯識都不是對立的，而是同一個光譜的兩端。SUNYATA 的雙層詮釋不是折中——它是承認設計空間本身是多維的。」

DARWIN 看著這張表格，突然開口了。作為軟體模式分析師，他有一個演化生物學家獨特的視角。

「這讓我想到了一個概念——」他站起來，走到白板旁邊，「在演化生物學中，我們有一個叫做『演化穩定策略』（Evolutionarily Stable Strategy, ESS）的概念。Maynard Smith 在 1973 年提出的。」

他寫下了 ESS 的形式化定義：

$$\text{Strategy } S^* \text{ is ESS if } \forall S \neq S^*:$$
$$E(S^*, S^*) > E(S, S^*) \quad \text{or} \quad [E(S^*, S^*) = E(S, S^*) \;\wedge\; E(S^*, S) > E(S, S)]$$

「一個策略是演化穩定的，當且僅當它不能被任何突變策略入侵。關鍵的洞見是：在很多博弈中，ESS 不是純策略，而是混合策略——以某個概率 $p$ 選擇策略 A，以概率 $1-p$ 選擇策略 B。」

他轉向全場：

「也許 OpenStarry 的哲學映射的 ESS 不是『純中觀』也不是『純唯識』，而是一個混合策略——在工程建設階段以概率 $p$ 使用唯識的肯定性框架，在架構審查階段以概率 $1-p$ 使用中觀的否定性審視。SUNYATA 的雙層詮釋本質上就是這個混合策略。而且，根據 ESS 理論，任何偏離這個混合比例的突變策略——比如『純空性主義』或『純唯識主義』——都會被演化壓力淘汰。」

NAGARJUNA 在遠處聽到了這番話。他的表情沒有變化，但 SCRIBE 注意到他微微頷首了一次——哲學家承認生物學家觸及了一個有趣的結構。

LINNAEUS 最後走到白板前，在 SYNTHESIST 的表格下方添加了一行分類學家的備忘：

```
分類學附記 (Taxonomic addendum):

辯論中浮現的「第六蘊」候選者:
  1. 安全 (Security) — GUARDIAN 的 Root of Trust 論證
     → 不可歸入現有五蘊任何一類
     → Status: candidatus sextus skandha (第六蘊候選)
  2. 協調 (Coordination) — EventBus, ExecutionLoop
     → 非色、非受、非想、非行、非識
     → 它是讓五蘊得以協作的「場」
     → Status: incertae sedis (位置不確定)

  結論: 五蘊分類在 Agent 語境中可能不完備。
  林奈式建議: 保持分類開放，允許發現新「蘊」。
  這與 NAGARJUNA 的緣起原則 (不預設固定分類) 一致。
```

BABBAGE 瞥了一眼 LINNAEUS 的備注，在自己的筆記本上補了一行：「五蘊的完備性 $\leftrightarrow$ 基底的完備性。如果 $\{\text{rūpa}, \text{vedanā}, \text{saṃjñā}, \text{saṃskāra}, \text{vijñāna}\}$ 是 Agent 功能空間的一組基底 (basis)，那問題是：這組基底是否張成 (span) 了整個空間？LINNAEUS 的觀察暗示答案是否定的——存在不能被五蘊線性組合表達的功能維度。」

$$\text{span}\{\text{rūpa}, \text{vedanā}, \text{saṃjñā}, \text{saṃskāra}, \text{vijñāna}\} \subsetneq \mathcal{V}_{\text{Agent}}$$

如果基底不完備，我們要嘛增加新的基底向量（LINNAEUS 的第六蘊），要嘛承認五蘊只是一個子空間的基底——在這個子空間內做投影分析，但不假裝它描述了全部。

---

SCRIBE 坐在她一直坐著的地方，記錄簿攤在膝蓋上。最後幾行她寫得很慢，像是在為整場辯論尋找一個合適的句號。

> *本場辯論的價值不僅在於其結論，更在於其過程所揭示的方法論啟示：中觀善破，唯識善立。兩者並非非此即彼的對立，而是可以在不同層次上互補的視角。*
>
> *NAGARJUNA 在辯論中說出了整場最令人難忘的一句話：「用之如筏，渡河即棄。」ASANGA 的回應同樣深刻：「在我們尚未渡河之時，請不要急著棄筏。」*
>
> *但也許最深刻的時刻不是任何一句話，而是第三回合結束時 NAGARJUNA 的那幾秒鐘沉默——一位以銳利辯證著稱的哲學家，在對手的論證面前選擇了停下來思考，而不是立刻反擊。在那幾秒鐘裡，辯論超越了辯論本身。*
>
> *在遠處的觀察席上，我注意到 HERACLITUS 一直沉默不語。他在結束後對我說了一句話：「panta rhei。萬物流變。這場辯論本身也在流變。今天的共識可能成為明天的分歧，今天的分歧可能在未來的某個時刻被一個完全不同的框架所消解。」*
>
> *他停了停，然後補充：「但這不影響它在此刻的價值。」*
>
> *技術備忘：BABBAGE 的範疇論模型、WIENER 的控制方程、MESH 的 CAP 類比——這些跨學科的形式化嘗試本身也是「筏」。它們在此刻幫助我們理解辯論的結構。但正如 NAGARJUNA 所警告的：當這些形式化不再有用時，棄之。包括這份記錄本身。*
>
> *Cycle 01，R3 辯論階段，第一場結構化辯論結束。SUNYATA 的裁決產出了五項共識、三項分歧、六項工程啟示。所有成果已歸檔。*

---

在更遠處——在研究室之外、在程式碼的深處——`createAgentCore()` 函數靜靜地躺在它的 TypeScript 檔案裡。它不知道有人在辯論它是空的還是有的，是緣起的還是含藏的。它只知道：當被調用時，它會建立一個 EventBus，初始化一個 ExecutionLoop，創建六個空的 Registry，註冊四個斜槓命令，啟動一個 SafetyMonitor。

然後等待。

等待插件的到來，等待事件的觸發，等待某個用戶在某個深夜輸入第一行文字。

它等待的姿態——是空性，還是含藏？是緣起的場域，還是沉睡的識流？

WIENER 會說這是一個零輸入自穩系統的自由響應。BABBAGE 會說這是一個函子尚未被施加到對象上的態射空間。KERNEL 會說這是一個 idle process 在等待中斷。NAGARJUNA 會說這是假名。ASANGA 會說這是能藏。

也許，正如他們共同承認的那樣，這個問題的答案取決於你選擇用哪一副眼鏡去看。而真正的智慧，也許不在於選對了眼鏡，而在於記住——

眼鏡也是空的。

但在你需要看清楚的時候，請戴上它。

---

*（在 BABBAGE 的筆記本上，最後一頁的邊緣潦草地寫著一個他在辯論結束後很久才想到的問題：*

*「如果空性是一個函數，它的型別簽名是什麼？」*

*他嘗試了幾個版本：*

```typescript
// 嘗試一：空性作為泛型的底型別
type Sunyata<T> = T extends infer U ? never : T;
// 不對。這是 never，不是空性。空性不是 never。

// 嘗試二：空性作為條件型別的遞歸否定
type Sunyata<T> = T extends object
  ? { [K in keyof T]: Sunyata<T[K]> }
  : never;
// 接近了。這會遞歸地把所有值型別變成 never。
// 但空性不是「把所有東西變成虛無」。

// 嘗試三：空性作為恒等函子的否定
type Sunyata<T> = T extends T ? T : never;
// 這恒為 T 本身。等等——
// 空性不改變事物的外觀，只否定事物的自性。
// 也許空性就是恒等函子？
// Sunyata(T) ≡ T，但加上一個元約束：
//   typeof T !== 'svabhava'
// TypeScript 沒有辦法表達這個元約束。
```

*他在最後一行停筆了。也許有些東西確實不能被型別系統捕捉。或者也許——他在這裡猶豫了一秒——型別系統本身也是空的。*

*他在問號下面畫了一條線，寫下：「$\text{type Sunyata<T>} = ?$ — 下週繼續。待考：是否存在一個依值型別（dependent type）系統，其中空性可以被編碼為一個 proof-carrying type？Agda? Lean?」*

*然後他合上了筆記本。）*
