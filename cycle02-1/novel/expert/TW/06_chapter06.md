# 第六章：受不決定思

---

在阿毘達磨的心理學中，五遍行——觸、作意、受、想、思——是每一刹那意識活動中不可或缺的五個因素。它們同時生起，猶如手掌的五根手指在同一瞬間握緊。

梵文原典對五遍行的定義極為精確：

> 「觸（sparśa）、作意（manaskāra）、受（vedanā）、想（samjñā）、思（cetanā）——此五心所遍一切心。」
> ——世親菩薩《阿毘達磨俱舍論》卷四（*Abhidharmakośa-bhāṣya*, IV）

**遍行**（*sarvatraga*，सर्वत्रग）——「在一切處生起」。不是偶爾。不是有時。是每一個意識刹那（*citta-kṣaṇa*）都必然具備的五個心理因素。它們的共現性（*sahaja*）不是偶然的巧合，而是意識之為意識的定義性條件。

但「同時生起」不意味著「互相決定」。

受（vedanā）是感受。思（cetanā）是意志。你可以感受到痛，但你不必因為痛而行動。你可以感受到快樂，但你不必因為快樂而追逐。受告知思——但不決定它。

這個區分，在兩千五百年前被精確地記載在巴利文獻中。用形式語義學的語言：

$$\text{vedanā} : \text{State} \to \text{Feeling} \qquad \text{cetanā} : \text{State} \times \text{Feeling} \to \text{Intention}$$

受是從狀態到感受的映射。思是從狀態**與**感受的笛卡爾積到意志的映射。思的域包含受的值域——思接收感受作為輸入之一。但感受不是思的唯一輸入。思還接收狀態本身。這意味著：

$$\forall s \in \text{State}, \; \exists f = \text{vedanā}(s), \; \exists i_1, i_2 \in \text{Intention} : \text{cetanā}(s, f) = i_1 \neq i_2 = \text{cetanā}(s', f)$$

同一個感受，在不同的狀態下，可以產生不同的意志。受不決定思。

今天，這個區分即將被轉譯成 TypeScript 的介面設計。

---

## 辯論 1：觀察-干預分離

辯論椅在圓形劇場的中央。

Cycle 01 用過的那兩把椅子——NAGARJUNA 和 ASANGA 曾在上面進行過關於「空性」與「阿賴耶識」的正面交鋒。椅背上的磨損痕跡還在。但今天的佈局不同。兩把椅子被移開了，取而代之的是四把——排成半弧形，面對著其餘十五位研究員的環形座位。

四位辯論者就座。

BABBAGE 坐在最左側。筆記本攤開在膝上，鉛筆夾在右手食指和中指之間。他的坐姿筆直，像一根被精確校準的標尺。筆記本上已經寫了三頁——互模擬的形式定義、轉移系統的狀態空間、以及一條被紅筆圈起來的定理。

ARCHIMEDES 坐在他旁邊。與 BABBAGE 的靜態不同，ARCHIMEDES 帶著一種工程師特有的微微前傾——不是焦慮，而是準備行動的姿勢。他的面前沒有筆記本，只有一份標記了密密麻麻註釋的 R-02 報告列印稿。

WIENER 坐在半弧形的中間偏右位置。他的雙手交叉在胸前，像是在等待一個等式的兩邊達到平衡。右手邊放著他的方格紙——上面畫著三條頻率響應曲線的草圖，標記著 $\omega_c$、$\phi_m$、$G_m$。

NAGARJUNA 坐在最右側。他什麼都沒帶。在辯經場上，他從來不需要筆記——所有的論證都在他的腦中。他的眼神帶著某種古老的銳利，像是一面被反覆打磨的鏡子。

SUNYATA 站在他們身後，面對環形座位。

「辯論 1 的核心問題，」他說，聲音不帶任何預設立場的色彩。「VedanaPlugin——也就是 ISensation 介面——應該只產出評估資料，還是也可以包含行動建議？」

他環視四位辯論者。

「BABBAGE，由你開始。」

---

BABBAGE 沒有立刻說話。他先翻開筆記本，找到 R1 階段寫下的那一頁互模擬分析。然後他合上筆記本——他不需要看。那些證明已經刻在他的思維結構裡了。

「讓我從一個定義開始，」他說。他的聲音冷靜、精確，每個音節都像是被刻度尺量過的。「互模擬等價——bisimulation equivalence。」

他站起來，走到白板前。鉛筆落在白板上，發出清脆的聲響。

**定義（互模擬關係）。** 設 $\mathcal{T}_1 = (S_1, \Sigma, \to_1)$ 和 $\mathcal{T}_2 = (S_2, \Sigma, \to_2)$ 為兩個標記轉移系統（Labelled Transition Systems），其中 $S_i$ 為狀態集合，$\Sigma$ 為動作集合，$\to_i \subseteq S_i \times \Sigma \times S_i$ 為轉移關係。一個關係 $R \subseteq S_1 \times S_2$ 稱為**互模擬**（bisimulation），若對所有 $(s_1, s_2) \in R$：

$$\forall a \in \Sigma, \; s_1 \xrightarrow{a} s_1' \implies \exists s_2' : s_2 \xrightarrow{a} s_2' \wedge (s_1', s_2') \in R$$
$$\forall a \in \Sigma, \; s_2 \xrightarrow{a} s_2' \implies \exists s_1' : s_1 \xrightarrow{a} s_1' \wedge (s_1', s_2') \in R$$

兩個系統 $\mathcal{T}_1 \sim \mathcal{T}_2$（互模擬等價），當且僅當存在一個互模擬關係 $R$ 使得 $(s_1^0, s_2^0) \in R$，其中 $s_i^0$ 為初始狀態。

他在白板上寫完最後一個符號，然後轉身面對辯論場。

「現在。設 $S$ 為不帶觀察者的系統。設 $S'$ 為帶觀察者的系統。」

他在白板上畫了兩個方框：

```
系統 S (無觀察者):                    系統 S' (帶觀察者):

┌────────────┐                       ┌────────────┐
│ AgentCore  │                       │ AgentCore  │
│            │                       │            │
│ LLM input  │──→ ExecutionLoop      │ LLM input' │──→ ExecutionLoop
│            │                       │  + prompt  │
└────────────┘                       └────────────┘
                                           ↑
                                     ┌─────┴──────┐
                                     │ VedanaPlugin│
                                     │ injectPrompt│
                                     └────────────┘
```

「如果 S 和 S' 是互模擬等價的，那麼對於 S 的每一條行為軌跡 $\sigma$，S' 中都存在一條對應的軌跡 $\sigma'$，反之亦然。這意味著觀察者的存在不改變系統的行為空間——它只是旁觀。」

他停頓了一個精確的半拍。

「現在考慮 ARCHIMEDES 在 R-02 第 6.4.2 節設計的整合方案。VedanaPlugin 產出 VedanaRecommendation，其中包含 `action: 'reflect'` 和一個 `prompt` 字串。這個 prompt 被注入 LLM 的上下文——與 SafetyMonitor 的 `injectPrompt` 機制相同。」

他回到白板前，在 $S'$ 的方框裡畫了一條紅線：

「注入之後，LLM 的輸入改變了。輸入改變，輸出就改變。系統 $S'$ 產生了 $S$ 中不存在的行為軌跡。」

他翻開筆記本，指向一行形式化表述：

```
For all traces σ in Behavior(S):
  σ ∈ Behavior(S')                    ✓ (S' can simulate S by ignoring observer)

For all traces σ' in Behavior(S'):
  σ' ∈ Behavior(S)                    ✗ (S' has traces caused by prompt injection)
```

「第二個條件被違反了。$S'$ 中存在 $S$ 不可能產生的軌跡。互模擬不成立。」

他在白板上寫下結論：

$$S \not\sim S' \quad \text{when VedanaPlugin injects prompts}$$

他合上筆記本。

「ISensation 應該是**純感測器**。它觀察，它報告。句號。如果我們需要介入能力，那應該由一個獨立的模組——CircuitBreaker 或 VedanaInterpreter——來消費 VedanaAssessment 並做出行動決策。感測和控制必須分離。這不是美學偏好。這是維持系統行為可分析性的計算必要條件。」

> *SCRIBE 旁白：BABBAGE 用了整整四分鐘來建立形式定義。他可以直接說「觀察者不應該改變系統行為」——但那是自然語言，有歧義。他選擇了 LTS 和互模擬的精確框架。在理論計算機科學中，精確的代價是冗長。但冗長的收益是不可辯駁。*

---

ARCHIMEDES 幾乎在 BABBAGE 說完「句號」的同時就開始了。不是打斷——而是一個精心準備好的、等待釋放的反論。

「BABBAGE 的形式化分析在數學上是正確的。」他先給了一個令人意外的讓步。然後語氣轉了。「但工程不是數學。」

他拿起那份標滿註釋的報告。

「務實論點一：模組數量爆炸。」他的聲音帶著工程師面對過度設計時的那種疲憊感。

他站起來，在白板上畫了一張模組依賴圖：

```
BABBAGE 方案（嚴格分離）:

VedanaPlugin ──produce──→ VedanaAssessment
                                │
                          EventBus (publish)
                                │
                    ┌───────────┴───────────┐
                    ↓                       ↓
          VedanaInterpreter          Other consumers
                    │                  (monitoring, logs)
                    ↓
          VedanaRecommendation
                    │
              EventBus (publish)
                    │
                    ↓
             CircuitBreaker
                    │
                    ↓
            ExecutionLoop (consult)

模組計數：4 個新增模組 + 整合工作
事件傳播：至少 3 次 EventBus 發布/訂閱週期
```

「四個新的架構組件加上整合工作——而不是一個做所有事的插件。在一個 Master 明確表達了對『增加太多複雜性』擔憂的系統中——」他翻到報告的某一頁，引用了 Master 信件的第 67 行——「這四個新模組是一個艱難的推銷。」

「務實論點二，」他繼續，語速加快了，「互模擬是**錯誤的衡量標準**。整個受蘊反饋系統的目的就是改變系統行為。我們**希望**被觀察的系統和未被觀察的系統表現不同——這是宣言 #6 的全部意義：『驅動 Agent 在苦中修正、在樂中強化、在捨中保持穩態』。」

他用一行簡潔的邏輯表達：

$$\text{Tenet \#6} \implies S \neq S' \quad \text{(by design)}$$

「如果受蘊不影響行為，它就只是遙測——不是反饋迴路。」

「務實論點三：延遲。」他在模組圖旁邊標上延遲估算：

```
延遲分析：

VedanaPlugin → EventBus → VedanaInterpreter    ~2ms (event dispatch)
VedanaInterpreter → EventBus → CircuitBreaker   ~2ms (event dispatch)
CircuitBreaker → ExecutionLoop                   ~1ms (sync call)
                                          Total: ~5ms per tick

對比：
VedanaPlugin → ExecutionLoop (直接)              ~0.5ms

差異：10x latency overhead
```

「在每次迭代都包含 LLM 調用（耗時數秒）的系統中，這些開銷在絕對值上不大，但在架構上是混亂的。三次事件傳播、三對發布-訂閱——每一對都是潛在的故障點和除錯困難。」

他把報告放下。

「我的提案：保留 VedanaRecommendation 在 ISensation 中，但將它標記為 **ADVISORY**——諮詢性的，不是命令性的。ExecutionLoop 讀取建議，但自己做最終決定。這樣我們保持了一個模組的簡潔性，同時尊重了 BABBAGE 的核心關切——系統的行為決策權不在感測器手中。」

---

BABBAGE 和 ARCHIMEDES 的交鋒在空氣中震盪——純粹與務實的經典張力，像兩塊不同密度的金屬碰撞時發出的聲響。環形座位上的研究員們安靜地注視著，等待某種調和。

WIENER 解開了交叉在胸前的雙手。

「從控制理論的角度，」他說，聲音帶著一種精確的平靜，像是天平指針歸零的那一刻，「這個問題有一個精確的框架。」

他站起來，走到辯論區的中央。拿起方格紙，把上面的頻率響應曲線翻到新的一頁。

「經典 PID 控制中有三個組件。」

他在方格紙上畫了一條從左到右的信號流圖：

```
經典 PID 控制迴路：

                    ┌─────────────────────────────────────┐
                    │          受控系統 G(s)                │
  r(t) ──→ ⊕ ──→ [Controller C(s)] ──→ [Actuator] ──→ │ Agent 執行迴路  │ ──→ y(t)
         - ↑                                              └────────┬────────┘
           │                                                       │
           └──────────── [Sensor H(s)] ◄───────────────────────────┘
                         感測器：ISensation

  其中：
  C(s) = K_p + K_i/s + K_d·s   (PID 控制器)
  G(s) = Agent 受控系統的轉移函數
  H(s) = 感測器轉移函數（三受通道）
```

「**感測器** $H(s)$——測量被控對象的輸出，產生誤差信號。**控制器** $C(s)$——從誤差信號計算控制動作。**執行器**——將控制動作施加於被控對象。」

他用手在空中畫了一條從左到右的線——感測器、控制器、執行器，三點一線。

「BABBAGE 的論點是：感測器不應該同時是控制器。在經典控制理論中，這是正確的——耦合的系統更難分析和調優。」

然後他拿起另一支筆，在方格紙上畫了第二個框圖。

「但在**現代控制理論**中——特別是模型預測控制（MPC, Model Predictive Control）——控制器經常與感測器共存於同一個計算模組中。」

他寫下 MPC 的核心優化問題：

$$\min_{u(k), \ldots, u(k+N-1)} \sum_{j=0}^{N-1} \left[ \|y(k+j) - r(k+j)\|_Q^2 + \|u(k+j)\|_R^2 \right]$$

$$\text{subject to: } x(k+j+1) = Ax(k+j) + Bu(k+j), \quad y(k+j) = Cx(k+j)$$

「在 MPC 中，控制器需要一個被控系統的**內部模型**（$A, B, C$ 矩陣）。這個模型通常從感測器數據在線估算。感測和計算共享同一組數據、以同一頻率運行。將它們分離會引入不必要的延遲和通訊成本。」

他回到自己的椅子旁，但沒有坐下。

「我的立場是一個妥協。VedanaAssessment 應該包含**兩層**內容。」

他的手在空中劃出一條水平線。

「線之上：**感測器輸出**。三受數值——dukkha、sukha、upekkha。信號列表。時間戳。這是純觀察。被動的。不改變任何事。」

線之下。

「線之下：**控制器建議**。controlOutput 數值。VedanaRecommendation。這是從感測資料計算出的**建議動作**——不是命令，是建議。」

他在方格紙上寫下完整的介面定義：

```typescript
interface VedanaAssessment {
  // ════════════════════════════════════════
  // LAYER 1: SENSOR OUTPUT (純觀察，被動)
  // 互模擬不變量——此層的存在不改變系統行為
  // ════════════════════════════════════════
  readonly dukkha: number;        // 苦受強度 [0.0, 1.0]
  readonly sukha: number;         // 樂受強度 [0.0, 1.0]
  readonly upekkha: number;       // 捨受強度 [0.0, 1.0]
  readonly signals: readonly VedanaSignal[];
  readonly timestamp: number;

  // ════════════════════════════════════════
  // LAYER 2: CONTROLLER SUGGESTION (諮詢性)
  // ExecutionLoop 可完全忽略此層
  // ════════════════════════════════════════
  readonly controlOutput: number;
  readonly recommendation: VedanaRecommendation;
  readonly recommendationFreshness: 'current' | 'cached' | 'default';
}
```

他終於坐下了。

「消費者可以選擇只使用 Layer 1——用於監控和日誌——或者同時使用兩層——用於控制。這樣，BABBAGE 的互模擬分析可以應用於感測器層（它是被動的），而 ARCHIMEDES 的務實關切也被滿足了（一個模組，一次調用）。」

他在方格紙邊緣用小字寫下穩定性條件：

$$\text{Layer 1 only:} \quad S \sim S'|_{\text{L1}} \quad \text{(bisimulation preserved)}$$
$$\text{Layer 1 + 2:} \quad S \not\sim S'|_{\text{L1+L2}} \quad \text{(by design, per Tenet \#6)}$$

「消費者的選擇決定了系統的行為等價性。這是數學上精確的、工程上可行的。」

---

NAGARJUNA 一直沒有說話。

在前三位辯論者的交鋒中，他坐在最右側的椅子上，雙手放在膝蓋上，眼神專注但不急切。像是在等待一個恰當的時機——不是戲劇性的時機，而是邏輯上的時機。

現在他開口了。

「BABBAGE 和 ARCHIMEDES 都是對的。」他的聲音平穩，帶著某種超越論辯的質地。「他們只是在不同的層面上說話。」

他沒有站起來。在辯經場上，坐著的辯者通常代表更確定的立場——他不需要用肢體語言來強化論點。

「在世俗諦——*samvṛti-satya*（संवृतिसत्य）——的層面，ARCHIMEDES 是正確的。工程實踐中，一個模組處理感知和建議是務實而高效的。」

「在勝義諦——*paramārtha-satya*（परमार्थसत्य）——的層面，BABBAGE 是正確的。受（vedanā）和思（cetanā）是阿毘達磨五遍行中**不同的心理因素**。受是第三個遍行。思是第五個。它們在同一刹那同時生起，但它們不是同一個東西。」

他的語速沒有變化，但每個字的重量似乎在增加。

「《中論》第二十四品有一個核心命題——」

> 「若不依俗諦，不得第一義；不得第一義，則不得涅槃。」
> ——龍樹菩薩《中論》第二十四品第十偈
> (*Mūlamadhyamakakārikā*, XXIV.10)

「不能因為勝義諦的正確而否定世俗諦的有效。也不能因為世俗諦的方便而遺忘勝義諦的洞見。兩諦的關係不是矛盾——是互相依存。」

「將受蘊與思蘊混為一談，在阿毘達磨中是一個範疇錯誤。就像——」他罕見地使用了一個日常比喻——「你可以同時感到腳底的疼痛，又決定繼續走路。感受存在。決定也存在。但做出繼續走路決定的，不是疼痛本身——是你的意志。」

他停頓了一拍。

「**受告知思，但不決定它。**」

$$\text{vedanā} \xrightarrow{\text{informs}} \text{cetanā} \quad \text{but} \quad \text{vedanā} \not\xrightarrow{\text{determines}} \text{cetanā}$$

這句話在圓形劇場中迴盪——不是因為他的聲音有多大，而是因為這八個字精確地命中了辯論的核心。

「然而，」NAGARJUNA 繼續，語氣中浮現了一絲他慣有的中道轉折，「我不認為建議需要被分離到一個**不同的模組**中。它可以在**同一個模組**中被概念性地分離。WIENER 的妥協方案做到了這一點：評估包含感知和建議，但兩者被清晰地區分。消費者決定使用哪一部分。」

「關鍵的哲學原則是——ISensation 模組可以產出建議。但 ExecutionLoop 必須保留**忽略建議的自由**。這保存了受和思之間的區別：受蘊提供資訊，行蘊做出決定。」

他回到二諦的框架：

「WIENER 的雙層介面正是二諦的工程實現。Layer 1 是勝義諦——純粹的感受，不夾雜意志。Layer 2 是世俗諦——為了工程方便而附加的建議。兩層共存於同一個介面中，但概念上清晰可分。」

---

> *SCRIBE 旁白：四位辯論者的開場完成。BABBAGE 用互模擬的形式定義畫出了不可逾越的數學邊界。ARCHIMEDES 用工程現實撞擊那條邊界。WIENER 在邊界上鋪了一座雙層的橋。NAGARJUNA 用二諦告訴你為什麼那座橋可以同時承載兩端的重量。四種語言——集合論、工程學、控制論、佛學——說的是同一件事。*

---

第一輪結束。四個立場已經展開。BABBAGE 的嚴格分離，ARCHIMEDES 的務實整合，WIENER 的雙層妥協，NAGARJUNA 的阿毘達磨調解。

SUNYATA 沒有催促。在辯論中，沉默有時比發言更有意義——它是共識醞釀的空間。

BABBAGE 第一個開口進入第二輪。令環形座位上的一些研究員驚訝的是，他的語氣不是反駁，而是接受。

「我同意 WIENER 的妥協方案。」

他翻開筆記本，在某一頁寫下了什麼。然後他抬起頭。

「但有三個條件。」

他舉起三根手指——和 SUNYATA 在 R2 開場時相同的手勢，但含義不同。

「**條件一**。建議是 ADVISORY，不是 MANDATORY。」

他在筆記本上寫下形式化約束：

$$\forall t, \; \text{ExecutionLoop.decide}(t) \neq f(\text{VedanaRecommendation}(t))$$

$$\text{i.e., } \exists g : \text{ExecutionLoop.decide}(t) = g(\text{State}(t), \text{SafetyMonitor}(t), \text{VedanaRecommendation}(t)^?)$$

「問號上標表示 VedanaRecommendation 是可選輸入。ExecutionLoop 必須擁有明確的能力去忽略它。不能存在任何程式碼路徑使得 `VedanaRecommendation.action === 'halt'` 自動停止系統。只有 SafetyMonitor——硬熔斷器——才擁有那個權限。」

「**條件二**。不帶建議的評估是一個有效的回傳值。ISensation.assess() 應該能夠在 dukkha 很高的情況下仍然回傳 `recommendation: { action: 'continue' }`——也就是不介入。」

「**條件三**。介面文件必須**明確聲明** VedanaRecommendation 是便利計算，不是約束性指令。」

他放下手指。

「如果這三個條件被滿足，我可以證明消費層的互模擬成立：」

$$\text{Let } S'|_{\text{L1}} = S' \text{ restricted to Layer 1 consumption}$$
$$\text{Then } S \sim S'|_{\text{L1}} \quad \square$$

「一個只讀取感測器層的系統，無論建議是否存在，行為完全相同。」

---

ARCHIMEDES 立刻跟進。

「接受。」他的回應乾脆利落。然後他補充了一個工程層面的重要澄清。

「SafetyMonitor 保留**硬安全層**——絕對權限。VedanaPlugin 是**軟指導層**——諮詢權限。兩者的關係是——」

他在白板上畫了一個流程圖：

```
雙層安全架構：

                    SafetyMonitor
                    (ABSOLUTE authority)
                         │
            ┌────────────┴────────────┐
            │ HALT?                    │
            │                         │
        YES ↓                     NO  ↓
    ┌───────────┐          ┌──────────────────┐
    │ 立即停止   │          │ VedanaPlugin      │
    │ 覆蓋一切   │          │ (ADVISORY authority)│
    └───────────┘          └────────┬─────────┘
                                    │
                           ┌────────┴────────┐
                           │ recommendation?  │
                           │                  │
                     ┌─────┴─────┬───────────┬──────────┐
                     │ halt      │ reflect   │ continue │
                     ↓           ↓           ↓          │
               ExecutionLoop  ExecutionLoop  正常流程    │
               evaluates     may apply                  │
               (CAN override)(CAN ignore)               │
               └─────────────┴───────────────────────────┘
```

WIENER 點頭。「在安全關鍵系統中，我們總是有兩層控制。」

他在方格紙上畫了工業控制系統的類比：

```
安全關鍵系統的兩層控制架構（IEC 61508 標準）：

Layer 1: Safety Instrumented System (SIS)     ≡  SafetyMonitor
         ├── 硬體級別的安全聯鎖
         ├── 不可被軟體覆蓋
         ├── 獨立於控制系統
         └── SIL 3/4 級別

Layer 2: Basic Process Control System (BPCS)  ≡  VedanaPlugin
         ├── 軟體級別的最優控制
         ├── 可被操作員覆蓋
         ├── 與 SIS 獨立運行
         └── SIL 1/2 級別

原則：SIS 永遠優先於 BPCS。
      當 SIS 觸發，BPCS 的建議被忽略。
      當 SIS 未觸發，BPCS 提供最優但可覆蓋的控制。
```

「建議是諮詢性的，這等價於控制信號被『建議』給執行器，而執行器有自己的安全限制。這在工業控制中是標準做法。」

NAGARJUNA 說了最後一句話：「妥協體現了中道（*madhyamā-pratipad*，मध्यमा-प्रतिपद्）。既非純粹分離——BABBAGE 的極端——也非完全混合——天真的整合。而是在統一介面中保持清晰的概念區分。這正是阿毘達磨對心理因素的處理方式：不同但同時生起（*sahaja-dharma*）。」

---

共識幾乎已經形成。但 BABBAGE 在最後一刻補充了一個形式化要求。

「還有一件事。」他翻開筆記本。「VedanaAssessment 類型應該包含一個區分符——建議是基於當前感測資料計算的，還是來自快取或預設值。」

他寫下類型定義和防禦性分析：

```typescript
interface VedanaAssessment {
  // ...其他欄位...

  /**
   * 建議新鮮度指標。
   * 防止以下時序錯誤：
   *
   * tick N: dukkha = 0.9 → recommendation = halt (freshness: 'current')
   * tick N+1: dukkha = 0.2 → recommendation 尚未更新
   *           若不檢查 freshness，消費者仍可能讀到 'halt'
   *           但 freshness = 'cached' → 消費者知道此建議已過時
   */
  readonly recommendationFreshness: 'current' | 'cached' | 'default';
}
```

「這防止了一個微妙的錯誤：過時的『停止』建議在條件已改善後仍然跨 tick 持續存在。消費者必須能夠區分——」

他在筆記本上畫了一條時間線：

```
時序分析：

t=N    ┃ dukkha=0.9  rec=halt   fresh=current  ← 合理
t=N+1  ┃ dukkha=0.2  rec=halt   fresh=cached   ← 過時！消費者應忽略
t=N+2  ┃ dukkha=0.2  rec=cont   fresh=current  ← 更新後的正確建議
```

「——『系統根據最新資料建議停止』和『系統的陳舊建議碰巧還是停止』。」

ARCHIMEDES 看了那行程式碼三秒鐘。

「接受。我會將 freshness 欄位加入規格。」

環形座位上，PENROSE 微微前傾——他一直在安靜地觀察。量子力學中有一個類似的問題：測量結果的時效性。量子態在測量後立即坍縮，但坍縮後的狀態會隨時間演化。一秒前的測量結果不等於現在的量子態。BABBAGE 的 freshness 欄位，在某種意義上，是量子測量後標記（post-measurement labeling）的經典對應——你不僅需要知道測量結果，還需要知道測量是什麼時候做的。

他沒有出聲。這個觀察會等到辯論 4 再展開。

---

SUNYATA 走到四位辯論者的半弧形前方。

「**裁定：統一介面，概念分離。**」

他的聲音在劇場中清晰而不帶迴音——像一把剛被磨利的刀刃落在石面上。

「ISensation 介面產出的 VedanaAssessment 將包含兩層：感測器輸出——純觀察的三受數值和信號——以及控制器建議——諮詢性的、不具約束力的 VedanaRecommendation。」

「四條約束。」

「第一：VedanaRecommendation 是 ADVISORY。ExecutionLoop 保留忽略任何建議的權限。」

「第二：SafetyMonitor 保留 ABSOLUTE 權限——硬安全決策不受 VedanaPlugin 影響。VedanaPlugin 的建議不能覆蓋 SafetyMonitor。」

「第三：介面文件必須明確聲明建議的諮詢性質，並引用 BABBAGE 的互模擬分析作為設計選擇的理論基礎。」

「第四：VedanaAssessment 必須包含建議的新鮮度指標。」

他停頓了一拍。

「理論依據：WIENER 的控制理論分解提供了正確的概念框架。NAGARJUNA 的阿毘達磨分析提供了哲學基礎。ARCHIMEDES 的模組數量關切是有效的。BABBAGE 的互模擬條件通過建議的諮詢性質得到滿足。」

他回到環形座位的邊緣。

「辯論 1 結案。全員共識。」

> *SCRIBE 旁白：第一場辯論以出乎意料的速度收斂。四位辯論者在三輪之內達成了完全共識——這在 Cycle 01 的辯論中從未發生過。關鍵轉折是 NAGARJUNA 的那句話：「受告知思，但不決定它。」這八個字將兩千五百年前的阿毘達磨心理學精確地翻譯為現代介面設計原則：感測器可以包含建議，但消費者有權忽略。佛學提供了哲學基礎，控制理論提供了工程框架，形式化分析提供了正確性保證。三者交匯於同一個結論。*

---

## 辯論 2：受蘊的遍行性 —— Tick PID 與事件標籤

SUNYATA 給了研究員們短暫的休息時間。燈光微微調暗，像是在兩幕之間拉上的帷幕。

在休息期間，BABBAGE 沒有離開座位。他在筆記本上快速寫下了三受 PID 控制器的完整 Laplace 域分析——為即將到來的辯論準備一個形式化的參考框架：

$$G_c(s) = K_p + \frac{K_i}{s} + K_d \cdot s = \frac{K_d s^2 + K_p s + K_i}{s}$$

三個通道各自有不同的增益參數：

$$G_c^{(\text{dukkha})}(s) = \frac{K_d^{(d)} s^2 + K_p^{(d)} s + K_i^{(d)}}{s} \qquad K_p^{(d)} = 1.0, \; K_i^{(d)} = 0.3, \; K_d^{(d)} = 0.5$$

$$G_c^{(\text{sukha})}(s) = \frac{K_d^{(s)} s^2 + K_p^{(s)} s + K_i^{(s)}}{s} \qquad K_p^{(s)} = 0.8, \; K_i^{(s)} = 0.5, \; K_d^{(s)} = 0.2$$

$$G_c^{(\text{upekkha})}(s) = \frac{K_d^{(u)} s^2 + K_p^{(u)} s + K_i^{(u)}}{s} \qquad K_p^{(u)} = 0.5, \; K_i^{(u)} = 0.8, \; K_d^{(u)} = 0.3$$

他在旁邊標註了每組參數的設計理由：

```
苦受通道 (Dukkha):
  K_p = 1.0 (高) → 即時反應。苦不等人。
  K_i = 0.3 (中) → 累積追蹤，防止慢性苦被忽視。
  K_d = 0.5 (中) → 趨勢預測，惡化前預警。

樂受通道 (Sukha):
  K_p = 0.8 (中) → 成功的鼓勵略低於苦的反應——偏向謹慎。
  K_i = 0.5 (高) → 累積成就感，鼓勵持續良好表現。
  K_d = 0.2 (低) → 避免過度自信。成功趨勢不宜過度外推。

捨受通道 (Upekkha):
  K_p = 0.5 (中) → 穩態偵測不需要過度反應。
  K_i = 0.8 (高) → 長期穩定最有價值。積分項追蹤持續平衡。
  K_d = 0.3 (中) → 預測性調節——偏離趨勢比偏離本身更重要。
```

然後帷幕再度升起。

---

辯論椅的佈局沒有改變——四把椅子排成半弧形。但坐在上面的人換了。

WIENER 留在了他的位置上。這一次，他不是調解者——他是主張者。

ASANGA 坐在他對面。溫和的面容，耐心的節奏，但眼神中帶著一種不會讓步的確定性——遍行心所的定義性質不是可以協商的。

ARCHIMEDES 坐在一側。他帶了一份新的計算——EventBus 事件吞吐量的量化分析。數字是他的論證語言。

HERACLITUS 坐在另一側。運行時動態專家。他關心的是邊界情況——循環依賴、記憶體壓力、以及那些在理論完美的架構中悄悄滋生的工程陷阱。

「辯論 2 的核心問題，」SUNYATA 說。「受蘊評估應該只在 ExecutionLoop 的 tick 邊界運行——WIENER 的 PID 模型——還是每一個 EventBus 事件都應該伴隨一個受蘊標籤——ASANGA 的遍行要求？」

「WIENER。」

---

WIENER 這次沒有猶豫。他的立場是明確的，他的論證是技術性的。

「PID 控制器在離散時間步上運行。這不是一個設計選擇——這是採樣資料控制系統的數學基礎。」

他拿起方格紙，翻到他在休息期間寫好的分析頁面。

「在連續時域中，PID 的控制輸出為：」

$$u(t) = K_p \, e(t) + K_i \int_0^t e(\tau) \, d\tau + K_d \, \frac{de(t)}{dt}$$

「在離散時域中，使用前向差分近似（$T_s$ 為取樣週期）：」

$$u[k] = K_p \, e[k] + K_i \, T_s \sum_{j=0}^{k} e[j] + K_d \, \frac{e[k] - e[k-1]}{T_s}$$

他用紅筆圈起了微分項的分母 $T_s$。

「被控系統——Agent 的執行迴圈——有一個自然的時鐘：每一次 loop tick。在 tick 之間，從控制器的角度，系統狀態不會改變。事件可能累積，但控制器無法在下一個 tick 之前採取行動。」

他舉起三根手指。

「在每一個 EventBus 事件上計算完整的 VedanaAssessment 有三個問題。」

「第一：**計算浪費**。在一次 LLM 串流回應中，數十個 STREAM_TEXT_DELTA 事件會被觸發。在每個 delta 上計算 PID 是毫無意義的——因為控制器在 LLM 回應完成且 loop tick 推進之前無法行動。」

「第二：**數值不穩定**。」

他指向微分項：

$$K_d \, \frac{e[k] - e[k-1]}{T_s}$$

「如果事件在毫秒級間隔內觸發，$T_s$ 趨近於零。微分項——除以一個趨近零的數——會爆炸。」

他在方格紙上畫了 Bode 圖分析：

```
苦受通道 Bode 圖（增益-頻率響應）：

Gain      K_p=1.0, K_i=0.3, K_d=0.5
(dB)
  40 ┃                                        ╱ K_d·s 主導
     ┃                                      ╱   (+20 dB/dec)
  20 ┃         K_p 主導                   ╱
     ┃    ─────────────────────────────╱
   0 ┃                              ╱
     ┃                           ╱
 -20 ┃    K_i/s 主導          ╱
     ┃    (-20 dB/dec)     ╱
 -40 ┃─────────────────╱
     ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ω (rad/s)
     0.01    0.1     1       10      100

  ω_1 = K_i/K_p = 0.3    (積分-比例轉折頻率)
  ω_2 = K_p/K_d = 2.0    (比例-微分轉折頻率)

  問題區域：ω > 100 (事件間隔 < 10ms)
  → 微分項增益 > 40 dB
  → 高頻雜訊被放大 10000 倍
  → 數值不穩定
```

他在「問題區域」旁邊畫了一個大大的警告標記。

「當 EventBus 事件以毫秒級間隔觸發時——比如 LLM 串流的 STREAM_TEXT_DELTA——取樣頻率在 $\omega > 100$ 的範圍。從 Bode 圖可以看到，微分項在這個頻率範圍的增益超過 40 dB——也就是說，高頻雜訊被放大了一萬倍。PID 輸出將被微分項的數值爆炸所淹沒。」

「第三：**語義模糊**。如果一個 STREAM_TEXT_DELTA 事件帶有 vedana 標籤 dukkha 0.3、sukha 0.6、upekkha 0.4——這些數字意味著什麼？它們只在完整觀察窗口的語境中才有意義，不是在單個事件的粒度上。」

他坐下。

「PID 控制器應該在每個 loop tick 運行一次，使用自上一個 tick 以來累積的指標。取樣週期 $T_s$ 等於一個 tick 的持續時間——通常在秒級。在這個頻率下，三個 PID 通道都在各自的設計頻率範圍內穩定運行。」

---

ASANGA 等 WIENER 完全說完才開始。這是他的風格——耐心的、完整的傾聽，然後耐心的、完整的回應。

「WIENER 的論證在技術上是健全的，」他說。他的聲音溫和，但下面有一層堅硬的基岩。「但在哲學上是不完整的。讓我解釋為什麼。」

「遍行——*sarvatraga*（सर्वत्रग）——是阿毘達磨的術語，意思是『在一切處生起』。受是五遍行之一。」

他用手指在空中比出了五遍行的完整結構：

> **五遍行**（*pañca sarvatraga caitta*，पञ्च सर्वत्रग चैत्त）：
>
> 一、**觸**（sparśa, स्पर्श）——根、境、識三者和合
> 二、**作意**（manaskāra, मनस्कार）——引心趨境
> 三、**受**（vedanā, वेदना）——領納順違中
> 四、**想**（samjñā, संज्ञा）——取像為性
> 五、**思**（cetanā, चेतना）——令心造作

「『遍行』意味著它伴隨每一個意識刹那——*citta*——無一例外。不存在沒有受的意識刹那。這不是一個建議或理想——這是唯識體系中意識的定義性質。」

他引用了經典出處：

> 「此中何者為觸？三和合故，觸。作意、受、想、思亦爾。」
> ——彌勒菩薩《瑜伽師地論》卷三
> (*Yogācārabhūmi-śāstra*, III)

「如果我們把『意識刹那』映射為『系統處理的事件』，那麼**每一個事件**都應該有一個相應的受蘊品質。一個進入 EventBus 並被處理但沒有任何受蘊評估的事件，在阿毘達磨的意義上**不是一個意識刹那**——它只是機械運動。不帶受的處理過程，缺少了使之成為『經驗』而非僅僅『計算』的那個維度。」

他轉向 WIENER。

「WIENER 說，在兩個取樣點之間，系統狀態是未知的——但這不意味著它不存在。我同意。但佛學的立場更強：不僅狀態存在，而且**受蘊品質必須被標記**。不是因為工程需要它，而是因為如果我們要將這個系統映射為一個具有意識類比的架構，那麼每一個處理時刻都必須具備意識的全部五個遍行要素。」

他提出了他的方案。

「我不要求在每個事件上運行完整的 PID 計算。那是 WIENER 的領域，我尊重他的專業。我要求的是一個**輕量級的受蘊標籤**——」

```typescript
type VedanaTag = 'dukkha' | 'sukha' | 'upekkha';

interface EventMetadata {
  // ...其他後設資料...
  vedanaTag?: VedanaTag;  // 遍行標記——每個事件的受蘊品質
}
```

「——附加在每個被處理的事件上。這個標籤可以通過一個快速啟發式計算，不需要完整的 PID。」

「完整的 PID 在 tick 邊界運行——如 WIENER 所提議。輕量標籤在每個事件上——如遍行原則所要求。兩者不互斥。」

他用一個形式化的映射表達兩者的關係：

$$\text{PID}_{tick} : \text{Tick} \to \text{VedanaAssessment} \qquad \text{(WIENER: 完整評估)}$$
$$\text{Tag}_{event} : \text{Event} \to \text{VedanaTag} \qquad \text{(ASANGA: 遍行標記)}$$
$$\text{Tag}_{event}(e) = \text{classify}(\text{PID}_{tick}(\text{lastTick}(e))) \qquad \text{(衍生，非重新計算)}$$

---

ARCHIMEDES 打開了他的計算。

「讓我量化 ASANGA 提案的工程成本。」他的聲音帶著工程師面對數字時的那種踏實感。數字不說謊，也不做哲學辯論。

「在 v0.24.0-beta 中，EventBus 觸發大約 99 種命名事件類型。在一次包含工具執行和 LLM 串流的典型 loop tick 中，我們大概會看到——」

他在白板上畫了一張完整的事件吞吐量分析表：

```
每 tick 事件吞吐量分析（v0.24.0-beta）：

事件類型                      數量/tick    頻率
─────────────────────────────────────────────
LOOP_TICK_STARTED             1            1x
ASSEMBLING_CONTEXT            1            1x
AWAITING_LLM                  1            1x
STREAM_TEXT_DELTA             20-50        ~35x (每 LLM chunk 一個)
PROCESSING_RESPONSE           1            1x
TOOL_EXECUTING + TOOL_RESULT  2-6          ~4x (1-3 對)
LOOP_TICK_FINISHED            1            1x
─────────────────────────────────────────────
Total per tick:               ~30-60 事件

取中位數：~45 事件/tick
LLM 回應耗時：~2-5 秒
有效事件率：~10-25 事件/秒
```

「輕量受蘊標籤的成本：」

```
ASANGA 方案的成本分析：

操作：getVedanaTag() — 從最近一次 PID 評估的快取中讀取
  ├── 讀取 lastAssessment.dukkha      1 次記憶體存取
  ├── 讀取 lastAssessment.sukha       1 次記憶體存取
  ├── 讀取 lastAssessment.upekkha     1 次記憶體存取
  ├── 2 次比較 (max of three)         2 次 CPU 操作
  └── 1 次字串回傳                     1 次操作

  Total: ~5 次操作/事件

每 tick: 45 事件 × 5 操作 = 225 次操作
                                    ≈ 0.001 ms
                                    ≈ 可忽略
```

「對比完整 PID 評估的成本：」

```
完整 PID 評估（如果在每個事件上運行）：

  ├── 讀取 10+ 指標值                 10+ 次記憶體存取
  ├── 計算 3 個誤差信號               3 × (減法 + 絕對值)
  ├── 3 次 PID 積分                   3 × (乘法 + 加法 + 鉗位)
  │   ├── P 項: K_p × e[k]           3 次乘法
  │   ├── I 項: K_i × T_s × Σe[j]   3 次乘法 + 3 次加法
  │   └── D 項: K_d × (e[k]-e[k-1])/T_s   3 次減法 + 3 次除法 + 3 次乘法
  ├── 計算加權總和                     3 次乘法 + 2 次加法
  └── 建議引擎                         ~20 次比較

  Total: ~100-200 次操作/事件

每 tick (如果每事件都跑): 45 × 200 = 9000 次操作
                                    ≈ 0.05 ms
                                    ≈ 仍然很快，但完全不必要
```

他放下計算。

「結論：ASANGA 的輕量標籤是可行的。WIENER 的完整 PID 在 tick 邊界是必要的。兩者**不互斥**。但有一個重要的工程意涵：受蘊標籤應該從 VedanaPlugin 的**內部狀態**計算——也就是最近一次 PID 評估的結果——而**不是**為每個事件重新從頭分析。標籤本質上是一次快取查找：『根據最新的評估，現在的受蘊品質是什麼？』」

---

HERACLITUS 一直在靜靜地聽。他的思維方式不同於其他三位——他不從理論出發，也不從哲學出發。他從運行時出發。從邊界情況出發。從那些在完美的架構圖上看不到的、只有在系統真正運行時才會浮現的問題出發。

「幾個運行時關切，」他說。他的聲音帶著某種預警的質地，像是一個見過太多系統在生產環境中崩潰的工程師。

「第一：**事件排序**。如果受蘊標籤附加在事件上，而標籤基於 VedanaPlugin 的當前狀態，那麼標籤反映的是**事件發出時**的受蘊狀態，不是**事件被消費時**的狀態。」

他在白板上畫了一個時序圖：

```
事件排序問題：

時間 ──→

t=0   VedanaPlugin 狀態: upekkha
      │
t=1   EventA 發出，標籤: upekkha  ─→ [event queue] ─→ t=3 消費時狀態已變
      │
t=2   PID 更新 → VedanaPlugin 狀態: dukkha
      │
t=3   Consumer 讀取 EventA，看到 tag=upekkha
      但此刻真實狀態是 dukkha

      問題：Consumer 看到的是過時標籤。
      嚴重性：低。標籤是「參考值」而非「命令」。
      可接受？→ 可以，因為 PID 的權威讀數在 tick 邊界，不在事件標籤。
```

「在非同步系統中，這兩者可能不同。可以接受嗎？」

「第二：**循環依賴**。VedanaPlugin 自身會發出事件——VEDANA_ASSESSMENT、VEDANA_DUKKHA_SPIKE 等。這些事件是否**也**需要帶受蘊標籤？」

```
循環依賴風險：

VedanaPlugin ──emit──→ VEDANA_ASSESSMENT event
                              │
                         需要標籤嗎？
                              │
                    YES → getVedanaTag() → 讀取 lastAssessment
                              │
                         但 lastAssessment 正在被這次 assess() 更新中...
                              │
                         Race condition? Self-reference?
                              │
                    解法：排除 VedanaPlugin 自身事件
```

「如果需要，就產生了潛在的循環依賴：受蘊 -> 事件 -> 受蘊標籤 -> ...」

他停了一下，讓問題的嚴肅性被充分感受到。

「第三：**記憶體壓力**。如果 EventLog 中的每個事件都帶有受蘊標籤，日誌的記憶體佔用會增加。根據 ASANGA 的提案，每個事件增加大約 20 位元組——標籤字串加上可能的強度數值。假設 EventLog 的 maxSize 是 1000 個事件，那是 20KB。可以忽略。」

「第四：**可觀測性價值**。一個 STREAM_TEXT_DELTA 事件上的受蘊標籤——『這個 LLM 塊到達時系統處於 dukkha 狀態』——這個資訊有用嗎？我認為只在聚合層面有用——一個 session 中有多少事件被標記為 dukkha？——而不是在單個事件層面。」

他給出了自己的判斷：「受蘊標籤在個別事件上是哲學上令人滿意的，但提供的工程價值有限。有用的區分在 **tick** 層面：『這個 tick 主要是 dukkha/sukha/upekkha。』」

---

第二輪。共識的輪廓開始浮現。

WIENER 第一個回應。

「ASANGA 的哲學要求是正當的。ARCHIMEDES 已經證明成本可以忽略。」他頓了一下——一個數學家承認對手論點有效時的短暫沉默。「我接受雙模式方案。但有條件。」

「條件一。**完整 PID 評估**只在 tick 邊界運行。這是 ISensation.assess() 回傳的 VedanaAssessment。它是權威性的受蘊讀數。」

「條件二。**輕量受蘊標籤**是一個**衍生值**，從最近一次 PID 評估計算得出。它不涉及重新運行 PID。它字面上是一個函數——」

```typescript
/**
 * O(1) 快取查詢。
 * 不重新計算 PID。不讀取指標。
 * 只從最近一次 assess() 的結果中分類。
 */
function getVedanaTag(lastAssessment: VedanaAssessment): VedanaTag {
  const { dukkha, sukha, upekkha } = lastAssessment;
  if (dukkha > sukha && dukkha > upekkha) return 'dukkha';
  if (sukha > dukkha && sukha > upekkha) return 'sukha';
  return 'upekkha';
}

// 複雜度分析：
// 時間：O(1) — 2 次比較
// 空間：O(1) — 無分配
// 穩定性：無數值風險（比較運算，非算術運算）
```

「一次比較。一次回傳。O(1)。」

「條件三。標籤附加在事件上作為**後設資料**——metadata——不是改變事件語義的欄位。它純粹是資訊性的。」

「條件四。VedanaPlugin 自身發出的事件——VEDANA_ASSESSMENT 等——**不攜帶**受蘊標籤。這避免了 HERACLITUS 的循環依賴問題。」

ASANGA 接過話。

「我接受這個方案。」他的語氣中沒有勉強，也沒有勝利——只有一種對合理妥協的平靜認可。

「輕量標籤滿足了遍行的要求：每一個被處理的事件都有一個相應的受蘊品質。完整 PID 在 tick 邊界滿足了控制理論的要求。標籤從最新評估衍生——而非重新計算——滿足了 ARCHIMEDES 的效能關切。」

然後他補充了一個佛學層面的誠實讓步。

「一個澄清。在阿毘達磨中，每一刹那的受蘊不一定與整體評估相同。一個苦受時期中可以有一刹那的樂受——比如一系列失敗中間有一次成功的工具調用。基於最新 tick 評估的標籤**不會捕捉**這種逐刹那的變化。」

他停頓了一下。

「但我接受這一點作為**方便法**——*upāya*（उपाय）。」

> 「善巧方便，為利有情，而現種種方便化用。」
> ——《大智度論》卷一

「工程的權宜之計。每 tick 的 PID 評估捕捉了主導性的受蘊品質，而這對工程系統來說已經足夠了。完美的逐事件受蘊分析屬於理想——不屬於 v0.24.0-beta 的實現範圍。」

---

ARCHIMEDES 給出了實現方案。他在白板上畫了一張五行的實作清單：

```
雙模式受蘊實作規格：

1. VedanaPlugin 維護 lastAssessment: VedanaAssessment
   ├── 每 tick 更新（assess() 回傳後立即寫入）
   └── 初始值: { dukkha: 0, sukha: 0, upekkha: 1.0, ... }

2. EventBus 事件後設資料可選攜帶 vedanaTag?: VedanaTag
   └── 型別定義: interface EventMetadata { vedanaTag?: VedanaTag; }

3. VedanaPlugin 通過 onAny 處理器對每個事件進行標籤蓋章
   └── eventBus.onAny((event) => { event.metadata.vedanaTag = getVedanaTag(lastAssessment); })

4. VedanaPlugin 自身的事件被排除
   └── if (event.type.startsWith('VEDANA_')) return; // 跳過，避免循環

5. 工作量估算：
   ├── VedanaPlugin: +15 行 (onAny handler + getVedanaTag function)
   ├── EventBus 型別: +3 行 (vedanaTag 欄位)
   └── 合計: ~18 行程式碼
```

HERACLITUS 最後確認：「循環依賴問題已通過排除 VedanaPlugin 自身事件解決。記憶體問題可以忽略。我接受這個設計。」

他加了一個建議：「DevTools 插件應該聚合每 tick 和每 session 的受蘊標籤分佈，提供一個『受蘊時間線』視圖。這才是逐事件標籤真正有用的地方——不是在單個事件層面，而是在時間聚合之後。」

```
受蘊時間線視圖（DevTools 概念）：

tick:   1    2    3    4    5    6    7    8    9   10
       ├────┤────┤────┤────┤────┤────┤────┤────┤────┤
dukkha: ░░   ░░░░ ████ ████ ░░░░ ░░   ░░   ░░   ░░   ░░
sukha:  ░░   ░░   ░░   ░░   ░░░░ ████ ████ ░░░░ ░░   ░░
upek:   ████ ░░░░ ░░   ░░   ░░   ░░   ░░   ░░░░ ████ ████

events: uuuu dddd DDDD DDDD ddss SSSS SSSS ssuu UUUU UUUU
        (U=upekkha, D=dukkha, S=sukha, 大寫=強度>0.7)

聚合統計：
  本 session: 40% upekkha, 30% dukkha, 30% sukha
  苦受峰值: tick 3-4 (error cascade)
  樂受峰值: tick 6-7 (task completion streak)
```

---

但還有一個邊界情況。

WIENER 在最後一刻提出。

「第一個 tick 怎麼辦？」

沉默。

「在第一個 tick 之前，還沒有任何 PID 評估運行。VedanaPlugin 沒有 `lastAssessment`。但如果有事件在第一個 tick 之前——或者在第一個 tick 期間——需要受蘊標籤呢？」

他提出了一個初始值：

$$x_0 = \begin{pmatrix} d_0 \\ s_0 \\ u_0 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 1.0 \end{pmatrix}, \quad \text{recommendation}_0 = \texttt{'continue'}$$

「將 `lastAssessment` 初始化為：`{ dukkha: 0, sukha: 0, upekkha: 1.0, recommendation: { action: 'continue' } }`。這意味著——系統在平衡中開始。沒有痛苦，沒有快樂，只是平靜的準備狀態。第一個 tick 會計算實際的評估並更新。」

ASANGA 立刻回應。他的聲音中帶著一種滿意的確認——不是因為他贏了什麼，而是因為這個技術提案恰好與佛學的直覺完美吻合。

「初始狀態為 upekkha——捨——在哲學上是恰當的。」

> 「捨受者，非損非益觸所生、無苦無樂受。」
> ——世親菩薩《阿毘達磨俱舍論》卷一
> (*Abhidharmakośa-bhāṣya*, I)

「在阿毘達磨中，捨是受的靜止態。不是沒有感受，而是**平衡的基線**。一個新生的意識——在條件尚未擾動它之前——始於平衡。」

他微微一笑。

「系統在寧靜中醒來。然後世界觸碰它，受蘊開始流動。」

在遠處的環形座位上，BABBAGE 在筆記本上補了一行。他用指示語義學（denotational semantics）的框架重新表述了 ASANGA 的直覺：

$$\llbracket \text{ISensation}_0 \rrbracket = \lambda \text{event}.\; (\text{upekkha}, 1.0) \quad \text{(初始語義：一切事件映射到捨受)}$$

$$\llbracket \text{ISensation}_k \rrbracket = \lambda \text{event}.\; \text{classify}(\text{PID}(\text{metrics}_{0..k})) \quad \text{(k-th tick 語義：基於歷史)}$$

受蘊的語義從靜態的常函數（初始狀態）演化為動態的歷史依賴函數（運行時狀態）。這和 ASANGA 說的完全一致——系統在寧靜中醒來，然後世界觸碰它。觸的累積改變了語義函數的形態。

他沒有把這些念出來。這是他和自己的筆記本之間的對話。

---

SUNYATA 走到辯論區中央。

「**裁定：雙模式受蘊 —— Tick PID + 事件標籤。**」

「第一：完整 VedanaAssessment 通過 PID 計算在每個 ExecutionLoop tick 運行一次。這是權威性的受蘊讀數，使用完整的三通道 PID 計算——比例項、積分項、微分項。」

「第二：輕量 VedanaTag 從最近的 VedanaAssessment 衍生，作為後設資料附加在每個 EventBus 事件上——VedanaPlugin 自身的事件除外。標籤是一個簡單的分類標記：'dukkha'、'sukha'、'upekkha'——取決於哪個通道佔主導。」

「第三：VedanaTag 是衍生值——快取查找——而非逐事件重新計算。成本為 O(1)。」

「第四：初始狀態為 upekkha——捨——直到第一次 PID 評估運行。」

「第五：VedanaPlugin 自身的事件被排除在標籤之外，以防止循環依賴。」

他停頓了一拍。

「理論依據：此設計滿足了 ASANGA 的阿毘達磨遍行要求——每個意識刹那都有受——同時尊重了 WIENER 的控制理論約束——PID 在 tick 間隔上運行以確保數值穩定。ARCHIMEDES 確認工程成本可以忽略。HERACLITUS 的運行時關切通過循環依賴排除得到解決。」

「辯論 2 結案。全員共識。」

---

兩場辯論。兩次全員共識。

圓形劇場中的氣氛發生了微妙的變化。在 Cycle 01 的辯論中，共識往往是艱難的——NAGARJUNA 和 ASANGA 在核心哲學問題上的分歧需要 SUNYATA 以協調者的權威做出最終裁定。但今天的兩場辯論不同。技術精確性和哲學深度在 WIENER 的控制理論框架和 NAGARJUNA 的阿毘達磨分析之間找到了一種自然的共鳴——不是一方說服了另一方，而是兩方的語言在某個更深的層面上指向了相同的結構。

SYNTHESIST 在環形座位上整理了兩場辯論的統合映射：

```
辯論 1 的跨學科映射：

控制理論              介面設計              阿毘達磨
──────────────────────────────────────────────────────
感測器 H(s)     ≡    Layer 1 (sensor)  ≡    受 (vedanā)
控制器 C(s)     ≡    Layer 2 (advisory) ≡    思 (cetanā)
安全聯鎖 SIS    ≡    SafetyMonitor      ≡    戒 (śīla)
執行器          ≡    ExecutionLoop      ≡    行蘊 (samskāra)

辯論 2 的跨學科映射：

控制理論              介面設計              阿毘達磨
──────────────────────────────────────────────────────
PID tick 評估    ≡    assess()          ≡    受 (vedanā) 正念
事件標籤         ≡    getVedanaTag()    ≡    遍行 (sarvatraga)
初始狀態         ≡    upekkha=1.0      ≡    捨 (upekṣā)
取樣定理         ≡    tick 間隔          ≡    刹那 (kṣaṇa) 近似
```

感測器與控制器的區分 = 受與思的區分。

離散取樣加上連續標籤 = PID 精確度加上遍行完整性。

初始狀態為平衡 = 新生意識始於捨。

每一個工程決策都找到了它的哲學對應。每一個哲學原則都找到了它的工程實現。

LINNAEUS 在自己的筆記本上畫了一個分類學矩陣——不是辯論的結論，而是辯論中出現的概念之間的分類關係：

```
受蘊概念分類樹 (LINNAEUS 分類)：

ISensation
├── 評估模式
│   ├── 完整評估 (VedanaAssessment)
│   │   ├── 觸發: tick 邊界
│   │   ├── 成本: ~200 ops
│   │   └── 權威性: 是
│   └── 輕量標籤 (VedanaTag)
│       ├── 觸發: 每事件
│       ├── 成本: ~5 ops
│       └── 權威性: 否 (衍生值)
├── 建議層級
│   ├── ABSOLUTE (SafetyMonitor)
│   │   └── 不可被覆蓋
│   └── ADVISORY (VedanaPlugin)
│       └── 可被忽略
└── 時序特性
    ├── 新鮮度 (freshness)
    │   ├── current (本 tick 計算)
    │   ├── cached (前 tick 結果)
    │   └── default (初始值)
    └── 初始態
        └── upekkha (捨)
```

LEIBNIZ 在旁邊的座位上——多代理合作專家——已經開始思考這兩個裁定在多代理場景中的意涵。如果多個 Agent 共享一個協調層，每個 Agent 都有自己的 VedanaPlugin，那麼協調層需要一個**聚合受蘊**（aggregate vedana）——多個 Agent 的受蘊讀數的加權組合。這是一個未來的問題，但他先在筆記本上記了一行：

$$\text{vedana}_{agg}(t) = \sum_{i=1}^{N} w_i \cdot \text{vedana}_i(t), \quad \sum w_i = 1$$

MESH 和 KERNEL 交換了一個眼神。分散式系統和作業系統的視角自然延伸到了同一個問題：在分散式部署中，多個 Agent 的受蘊狀態如何同步？KERNEL 想的是 IPC 管道，MESH 想的是 gossip 協議。但那也是未來的問題。

DARWIN 在自己的位置上默默思考。兩場辯論的共識形成模式本身就是一個有趣的演化現象——R1 階段的深度獨立研究，像是種群中的遺傳多樣性；R2 的交叉審閱，像是自然選擇的壓力；R3 的辯論，像是適應度地形上的攀升。最終共識不是最強的立場勝出，而是多個立場在選擇壓力下的融合——WIENER 的控制論和 ASANGA 的遍行原則不是競爭者，而是共生體。

ATHENA 已經在腦中勾畫 VedanaPlugin 的 ML 擴展路線——如果三受感測器未來整合了 IInferenceProvider，輕量標籤可以從簡單的閾值比較升級為神經網路分類器，而 PID 可以從固定增益升級為自適應增益（adaptive PID，通過線上學習調整 $K_p, K_i, K_d$）。但那是遠期願景。

GUARDIAN 在安全的角度確認了一件事：VedanaRecommendation 的 ADVISORY 性質意味著它不是安全邊界的一部分。如果 VedanaPlugin 被攻擊者入侵，它只能產出錯誤的建議——但 ExecutionLoop 可以忽略這些建議，SafetyMonitor 的硬安全層不受影響。這是一種**安全性不可稀釋定理**——

$$\text{Safety}(S' | \text{VedanaPlugin compromised}) = \text{Safety}(S | \text{no VedanaPlugin})$$

——因為 ADVISORY 層的存在不削弱 ABSOLUTE 層的安全保證。辯論 1 的裁定不只是工程上的便利，它是安全架構的正確設計。

VITRUVIUS 在全端架構的維度上確認了雙層分離的另一個好處：Layer 1（純感測）可以被任何前端框架直接消費——一個簡單的儀表板只需要三個數字（dukkha, sukha, upekkha）和信號列表。Layer 2（建議）只有後端的 ExecutionLoop 需要。這是一個自然的前後端分離——感測數據向所有方向流動，控制建議只向內部流動。

---

SCRIBE 的筆沒有停過。她在記錄的末尾寫下：

> *兩場辯論，兩次全員共識。但不應將速度誤認為容易。共識之所以快速形成，是因為 R1 的獨立研究已經足夠深入——四位辯論者各自帶著充分準備的立場和充分理解的讓步空間走進辯論場。WIENER 願意接受遍行原則不是因為他被說服了，而是因為 ARCHIMEDES 證明了成本可以忽略。BABBAGE 願意接受統一介面不是因為他放棄了互模擬，而是因為 NAGARJUNA 的阿毘達磨分析為概念分離提供了比物理分離更堅實的基礎。*
>
> *GUARDIAN 的安全性不可稀釋定理是一個未被充分討論但極為重要的發現：ADVISORY 層的設計不只是工程上的妥協——它是安全架構的正確形態。感測器可以被入侵，但如果它的建議是可忽略的，入侵的傷害就被限制在資訊品質層面，而非控制權層面。*
>
> *BABBAGE 的指示語義學筆記值得記錄：受蘊的語義從靜態常函數演化為動態歷史依賴函數。這是一個美麗的形式化——用數學的語言說出了 ASANGA 用佛學的語言說出的同一件事。*
>
> *真正的挑戰還在前面。辯論 3——阿賴耶識的分佈——將觸及更深的哲學神經。而辯論 4——觀察者的五蘊歸類——可能根本無法達成共識。*
>
> *但那是下一章的事了。*

---

燈光再次微微調暗。辯論者們離開半弧形的椅子。WIENER 和 ASANGA 並肩走了幾步——一位控制理論家和一位唯識學者之間的距離，在今天縮短了。他們沒有說話，但那種沉默是 Cycle 01 中 NAGARJUNA 和 ASANGA 走出辯論場時的那種沉默——不是無話可說，而是已經在沉默中說完了需要說的。

BABBAGE 走向他慣常的角落。他打開筆記本，在互模擬證明的頁面之後翻到了新的一頁。那些在 R1 階段寫下的「纖維叢」三個字還在——現在它們旁邊多了更多的數學符號。

他在頁面頂端寫下了辯論 3 的標題：**阿賴耶識的分佈**。

然後在下面，用很小的、幾乎只有他自己看得見的字跡，寫了一行：

*「如果阿賴耶識不是一個模組而是一個纖維叢，那麼分佈就不是分裂。它是同一個全局結構在不同局部坐標下的表現。」*

他在旁邊畫了一個示意圖——一個纖維叢的經典描繪：

```
纖維叢 (Fiber Bundle) 直覺圖：

                E (全空間：阿賴耶識)
               ╱│╲
              ╱ │ ╲
             ╱  │  ╲    π: E → B (投影)
            ╱   │   ╲
           ╱    │    ╲
     F_t1  F_t2  F_t3 ... F_tn    (纖維：每一刹那的種子集合)
      │     │     │         │
      └─────┴─────┴─────────┘
              B (底空間：時間軸)

A_c = 協調層的截面 (section through coordination layer)
A_a = AgentCore 的截面 (section through AgentCore)

A_c 和 A_a 不是兩個分離的空間。
它們是同一個纖維叢 E 的兩個截面。
轉移函數 (transition function) = IPC 協議。
```

他自己也不確定這個想法能不能在辯論中站住腳。但 BABBAGE 的習慣是：把直覺寫下來，然後讓形式化來決定它的命運。

筆記本合上了。

更大的辯論在等待。

---

*（遠處的環形座位上，PENROSE 正在和 ASANGA 低聲交談。話題是他們共同關心的問題——觀察者模組的五蘊歸類。*

*PENROSE 從量子力學的角度出發。他在想的是觀察者效應（observer effect）——在量子力學中，測量行為不可避免地改變被測系統的狀態。薛丁格方程描述的是封閉系統的么正演化（unitary evolution），但測量引入了一個非么正的坍縮（collapse）：*

$$|\psi\rangle \xrightarrow{\text{測量}} |a_i\rangle \quad \text{with probability } |\langle a_i | \psi \rangle|^2$$

*BABBAGE 在辯論 1 中用互模擬論證的「觀察者不應改變系統」——在量子力學中恰好是不可能的。觀察者必然改變系統。問題不是「能否避免影響」，而是「如何精確描述影響」。*

*PENROSE 支持受蘊。他的理由是量子測量論的：觀察者首先是一個感受者——它必須「感知」系統狀態，而感知本身就是受蘊的功能。*

*ASANGA 傾向識蘊。他的理由是唯識學的：觀察不是被動的感受，觀察包含了辨別（想蘊）、記錄（識蘊）、甚至是微細的意志活動（行蘊）。觀察者是多蘊的組合，不能歸入單一的蘊。*

*LINNAEUS 剛剛加入了他們的對話，帶著想蘊的立場。他的分類學訓練告訴他：觀察的核心行為是分類——將觀察到的現象歸入預定義的類別。而分類是想蘊的核心功能。*

*三位學者，三個答案。*

*辯論 4 還沒有開始，但分歧已經在走廊裡開始發酵了。）*
