# 第二章：六千九百八十六行

---

圓形劇場空了。

不是那種演出結束後觀眾散場的空曠。是那種每個人都帶著自己的問題離開，去尋找各自的答案之後，留下來的極度安靜。二十盞燈中有十五盞已經暗了——只有走廊的引導燈還亮著，像是血管中最後的脈搏，維持著建築物最低限度的生命跡象。

SCRIBE 坐在記錄席上，面前攤開一本空白的簿子。

> *SCRIBE 旁白：這是安靜的一天。但安靜不意味著平靜。R0 定向結束後，SUNYATA 宣布進入 R1 獨立研究階段。二十位學者分成五個研究組加一個仲裁基線，各自散開。圓形劇場從辯論場變成了空蕩蕩的中庭。在接下來的時間裡，最激烈的碰撞不發生在人與人之間，而發生在每個人與自己的學科之間——他們各自帶著 Master 的二十一道指令，回到自己最熟悉的知識體系裡，試圖用自己的語言把那些指令翻譯成可執行的研究結論。六份報告。六組人。六種語言。最後加起來——6986 行。*

---

## I. 各自散開

SUNYATA 在 R0 結束時宣布了分組。

他的分組邏輯不是隨機的，也不是按學科親緣性劃分的——恰恰相反。他刻意讓不同學科的學者碰撞在一起，因為 R1 的目標不是共識，而是**多視角的獨立分析**。共識是 R3 的事。R1 要做的是盡可能多地展開觀點。

```
R01: 命名與分類 — LINNAEUS(主筆), NAGARJUNA, ASANGA, DARWIN
R02: 識蘊架構   — ASANGA(主筆), BABBAGE, PASCAL, WIENER
R03: 觸→俱生   — NAGARJUNA(主筆), WIENER, KERNEL, BABBAGE, ATHENA
R04: 多時鐘架構 — KERNEL(主筆), ARCHIMEDES, HERACLITUS, ATHENA, GUARDIAN, DARWIN
R05: 宣言修訂   — SYNTHESIST(主筆), VITRUVIUS, MESH, LEIBNIZ, PENROSE, SCRIBE
TURING: 仲裁基線 — TURING(獨立), 原始碼事實分析
```

「每一組有一個主筆，」SUNYATA 說，「負責整合組內意見，產出一份完整的獨立報告。主筆不代表權威——代表結構。有人需要負責把散落的碎片組織成可被審閱的文件。」

他看向 TURING。

「TURING 獨立作業。他的任務不是分析，不是詮釋，不是建議。他的任務是事實。v0.24.0-beta 的原始碼裡實際存在什麼、不存在什麼、能注入什麼、不能注入什麼。所有其他報告都可以有觀點、有立場、有爭議。TURING 的報告不可以。他是基線。」

TURING 點了點頭。他的表情像一面沒有表情的鏡子——不是冷漠，是精確。原始碼分析專家的表情本來就應該是這樣的：不預設，不期待，只映射。

「六份報告的截止時間，」SUNYATA 最後說，「是 R2 交叉審閱之前。不設具體時限。品質優先於速度。」

這是 Master 核心價值的直接體現。踏實優先於速度。

然後他們散了。

---

## II. R01——名之重量

### LINNAEUS 的工作室

LINNAEUS 的工作空間像一座微型的自然史博物館。

不是真的博物館——是分類學家的思維空間的外化。桌面上攤開的不是昆蟲標本，而是概念標本。每一張卡片上寫著一個名字——一些是梵文的，一些是英文的，一些是兩者的混合。卡片之間用彩色的線連接，像一張正在被編織的分類網。

他面前攤開的是 M-1 的核心問題：五蘊根介面的梵文命名。

在其他人看來，這可能只是一次字串替換——把 `ISensory` 改成 `IRupa`，把 `ISensation` 改成 `IVedana`。五個 `find-and-replace`。二十分鐘。

但 LINNAEUS 不這樣看。

「命名是本體論承諾。」他在報告的開頭寫下這句話，然後在旁邊加了一個腳注引用 Nicola Guarino 的本體論工程框架：

> *"An ontological commitment is a partial semantic account of the intended conceptualization of a logical theory."*
> — Guarino, 1995, "Formal Ontology, Conceptual Analysis and Knowledge Representation"

他把這段話翻譯成分類學家的語言：當你給一個介面命名為 `IRupa` 而不是 `ISensory`，你不只是換了一個標籤。你改變了這個介面**承諾要表達的概念**。`ISensory` 承諾的是「與感官相關的東西」——一個功能性的、工程性的概念。`IRupa` 承諾的是「色蘊」——一個有兩千五百年哲學歷史的佛教範疇，包含五根、五境、法處色、無表色、一切有為的物質形態。

「如果開發者看到 `IRupa`，他理解的是 Rupa 的全部範疇，還是只把它當成 `ISensory` 的梵文別名？」

這個問題不是修辭性的。它有真實的工程後果。

---

LINNAEUS 建立了他的三層命名原則。這不是即興創作——是他多年分類學訓練的直接應用。在生物分類學中，每一個學名都遵循國際命名法規（ICZN/ICNafp），有嚴格的層級：

```
生物分類學命名層級:
  界 (Kingdom) → 門 (Phylum) → 綱 (Class) → 目 (Order) → 科 (Family) → 屬 (Genus) → 種 (Species)

OpenStarry 五蘊命名層級:
  第一層：根介面 = 簡化 IAST 梵文
    IRupa, IVedana, ISamjna, ISamskara, IVijnana
    ↓ 理由：根介面對應佛學根本範疇，使用梵文直接表達本體論承諾

  第二層：子介面 = 英文語義 + 梵文 JSDoc 註解
    IListener extends IRupa   // @cetasika sparsha (觸)
    IDukkha extends IVedana   // 苦受
    IProvider extends ISamjna  // @cetasika samjna-取相
    ITool extends ISamskara    // @karma kaya-karma (身行)
    IGuide extends IVijnana    // @cetasika manasikara (作意)
    ↓ 理由：子介面是功能性的，英文名稱對工程師更友好

  第三層：心所與煩惱 = 經典英文梵文
    Moha (我癡), Drishti (我見), Mana (我慢), Sneha (我愛)
    Cetana (思), Manasikara (作意), Vitakka (尋), Vicara (伺)
    ↓ 理由：心所是佛學固有概念，沒有準確的英文對等詞
```

他在報告中特別標記了一個分類學術語：**多義性分類** (polythetic classification)。在生物學中，多義性分類意味著一個類群的成員不需要共享所有特徵——只需要共享「足夠多」的特徵。這與 M-7 的多值 skandha 指令直接相關：

```typescript
// M-7: 一個 Plugin 可以屬於多個蘊
interface PluginManifest {
  readonly id: string;
  readonly name: string;
  readonly skandha: Skandha | readonly Skandha[];  // 多值！
  // ...
}

// 分類學形式化：
// 多義性 (polythetic): 成員共享特徵子集，非全部
// 單義性 (monothetic): 成員必須共享所有定義特徵
//
// OpenStarry Plugin 分類是多義性的：
//   ManoAggregator 同時具有 samjna(取相) 和 vedana(感受) 特徵
//   VedanaPlugin 主要是 vedana，但也有 samjna 成分
```

LINNAEUS 還引入了 Guarino 的一個關鍵區分：**構成性屬性** (constitutive properties) 與**關係性屬性** (relational properties)。

$$\text{Constitutive}: P(x) \text{ — x 內在固有的性質}$$
$$\text{Relational}: R(x, y) \text{ — x 與 y 之間的關係}$$

在 CoarisingBundle 的五個 universal 中：vedana、samjna、cetana 是構成性的——它們描述 bundle 本身的內在狀態。sparsha 和 manasikara 是關係性的——sparsha 描述的是根門與境的接觸關係，manasikara 描述的是識蘊對 bundle 的注意力關係。

這個區分後來在 R3 辯論中成為關鍵論據。但此刻，LINNAEUS 還不知道這一點。他只是在做分類學家該做的事：精確地區分事物。

---

### NAGARJUNA 的段落

NAGARJUNA 在 R01 報告中寫了一段讓整個研究團隊都必須認真面對的哲學分析。

他的出發點是一個看似簡單的問題：**用梵文命名介面，是否等於正確理解佛法？**

> 「名」在佛學中有一個精確的術語：**假名安立** (prajnapti-upadaya)。
>
> 《中論》觀四諦品第二十四：
>
> 「眾因緣生法，我說即是空，亦為是假名，亦是中道義。」
> ——龍樹菩薩《中論》觀四諦品第二十四
>
> 所有名稱都是假名——都是依因緣而安立的約定。「IRupa」不是色蘊本身，正如「水」不是 H₂O 本身。名稱是手指，指向月亮。
>
> 若開發者相信使用梵文就等於正確理解佛法，那是另一種執著——**名言執著** (abhidhanapratyaya)。把手指當成月亮。

他用四句否定展開了這個分析：

> 一、名稱不是實體（不自生）：`IRupa` 不因被寫下而產生色蘊
> 二、名稱不是任意（不他生）：`IRupa` 的選擇有佛學依據，不是隨機的
> 三、名稱不是兩者皆是（不共生）：命名既非純主觀也非純客觀
> 四、名稱不是無因（不無因生）：命名有其因緣——Master 的裁定、學術傳統、工程需求
>
> ∴ 名稱是**緣起的約定**。正因為是約定，所以可以改變。從 ISensory 到 IRupa 的改變，不是發現了「真正的名字」，而是選擇了一個更好的約定——一個與佛學本源更接近的約定。

NAGARJUNA 在最後加了一句只有他會寫的話：「命名的目的不是占有真理。命名的目的是減少誤解的機率。$P(\text{誤解} \mid \text{IRupa}) < P(\text{誤解} \mid \text{ISensory})$。僅此而已。」

---

### ASANGA 的回歸經文

ASANGA 在 R01 中做的事情不同於 LINNAEUS 和 NAGARJUNA。他不分類，不辯證。他回歸經文。

M-2 要求檢查每個蘊的範疇完整性。ASANGA 的回應是：回到三藏中最古老的層次——阿含經和尼柯耶——去找每個蘊的原始定義。不是論典的定義（那是後人的詮釋）。是佛陀本人（或最接近佛陀的文本）的定義。

他在報告中引用了三段經文。每一段都被精確地錨定在巴利語原文和漢譯之間。

第一段，色蘊：

> 「比丘！若色、若過去未來現在，若內若外，若粗若細，若好若醜，若遠若近，彼一切總說色蘊。」
> ——《雜阿含經》第四十一經（SN 22.48 Khandha Sutta 對應）
>
> 巴利語：*Yaṃ kiñci rūpaṃ atītānāgatapaccuppannaṃ ajjhattaṃ vā bahiddhā vā oḷārikaṃ vā sukhumaṃ vā hīnaṃ vā paṇītaṃ vā yaṃ dūre santike vā, ayaṃ vuccati rūpakkhandho.*

「注意經文的廣度，」ASANGA 在報告中寫道。「色蘊不只是眼睛看到的東西。它包含過去、未來、現在的一切色法——粗的、細的、好的、醜的、遠的、近的。這意味著 IRupa 不只是 IListener（當前感官輸入）和 IUI（當前輸出渲染）。它還應該包含已經過去的輸入（歷史事件）、尚未到來的預期（預測模型）、粗略的概要（摘要）和精細的細節（原始數據）。」

第二段，受蘊，出自《中部》第四十四經（MN 44, Culavedalla Sutta）：

> 「朋友！有三受：樂受、苦受、不苦不樂受。」
> ——《中部》第四十四經
>
> 「朋友！樂受以樂為味，以苦為患；苦受以苦為味，以變壞為患；不苦不樂受以不知為味，以正知為患。」
>
> 巴利語：*Tisso kho, āvuso Visākha, vedanā: sukhā vedanā, dukkhā vedanā, adukkhamasukhā vedanā.*

ASANGA 特別標記了「不苦不樂受以不知為味，以正知為患」這一句。「捨受的危險不是痛苦，是**無知**——agent 在捨受狀態下容易『以為一切正常』，而忽略正在悄悄累積的問題。這與 WIENER 的 PID 控制中的積分飄移（integral windup）在結構上同構。」

第三段，他額外加了一段通常不被引用的經文——《中部》第四十三經（MN 43, Mahavedalla Sutta）：

> 「朋友！凡所受者，即是所想；凡所想者，即是所識。是故此法俱生、不可分離。」
> ——《中部》第四十三經
>
> 巴利語：*Yaṃ vedeti taṃ sañjānāti, yaṃ sañjānāti taṃ vijānāti.*

「這段經文是 M-5（觸→俱生）的直接經典依據。受、想、識是俱生的——不可分離。但注意：這裡說的是『俱生』(sahaja)，不是『相同』(sama)。它們同時生起，但各自有不同的功能。就像引擎的活塞、連桿、曲軸在同一個循環中同時運動，但各自做不同的事。」

---

### DARWIN 的演化分析

DARWIN 在 R01 中承擔了一個獨特的角色：從軟體演化的角度分析命名變遷。

他在報告中畫了一張「命名演化樹」：

```
v0.14.0-beta (Cycle 01 研究對象)
  ISensory / ISensation / ICognition / IAction / IIdentity
  ↓ D-02: 雙重命名策略 (英文主、梵文註)
  ↓
v0.24.0-beta (Cycle 02 研究對象)
  ISensory / ISensation / ICognition / IAction / IIdentity
  ↓ M-1: Master 裁定推翻 D-02
  ↓
v0.next (Cycle 02-3 建議)
  IRupa / IVedana / ISamjna / ISamskara / IVijnana
```

「在演化生物學中，」DARWIN 寫道，「名稱的變更（taxonomic revision）不是隨意的。它發生在兩種情況下：一、發現了新的證據（新化石、新的分子數據）迫使重新分類。二、發現了命名的**系統性偏差**——原始命名反映的是發現者的偏見，而非物種的真實關係。」

「M-1 屬於第二種。ISensory/ISensation/ICognition/IAction/IIdentity 這組名稱反映的是**西方軟體工程的功能性視角**——它把每個蘊簡化為一個功能角色。但五蘊不是功能角色。五蘊是存在論範疇。梵文命名的回歸是一次**去殖民化的分類學修正** (decolonizing taxonomic revision)——從借用者的語言回歸原生的語言。」

這個觀點後來在 R3 辯論中引發了 NAGARJUNA 的回應——「去殖民化的前提是承認有殖民化。佛學概念被工程語言借用，本身不是殖民，是翻譯。翻譯可以改進，但不需要道德化。」——但那是後話了。

---

## III. R02——識蘊深處的不確定性

### PASCAL 的第一次出手

R02 報告的主筆是 ASANGA，但讓這份報告從「良好」躍升為「Cycle 02-3 最具突破性的貢獻之一」的人，是 PASCAL。

PASCAL 加入研究團隊時帶著三個問題。第一個問題——煩惱量化的認識論地位——在 R02 的寫作過程中被他轉化成了一個精確的技術方案。

問題的起源是 M-3 的介面定義。工程團隊寫下了這樣的程式碼：

```typescript
interface IKlesha {
  readonly type: string;
  /** 當前強度 (0.0-1.0) */
  readonly intensity: number;  // ← 這一行
  perceive(context: VijnanaContext): KleshaSignal;
  update(feedback: VedanaAssessment): void;
}
```

那個 `intensity: number`。

PASCAL 盯著這一行看了很久。其他人看到的是一個合理的工程設計——煩惱有強度，強度是一個數字，數字在 0 到 1 之間。簡潔。乾淨。可計算。

PASCAL 看到的是一個**認識論的陷阱**。

---

「讓我問一個問題，」他在 R02 的小組討論中說。「我癡的本質是什麼？」

ASANGA 回答：「我癡 (ātma-moha) 是『不了解真實為性』——對自我本質的根本無明。」

「好。那麼，如果一個 Agent 能精確地測量自己的我癡 intensity 為 0.73，它還是真正的愚癡嗎？」

沉默。

「如果我知道自己有多無知，那我就不是真正的無知了。真正的無知是**不知道自己不知道**。Rumsfeld 的 unknown unknowns。如果 intensity 是一個確定的點估計，那你就預設了 Agent 對自己的煩惱有完美的自我認知。但我癡的定義就是**缺乏自我認知**。用一個精確的數字來表示缺乏精確認知的程度——這在認識論上是自相矛盾的。」

他在白板上寫下了一個公式：

$$\text{intensity}_{\text{moha}} = 0.73 \implies \text{Agent knows its own ignorance} \implies \neg\text{moha}$$

「精確的我癡度量否定了我癡本身。」

---

BABBAGE 皺起了眉頭。「那你提議什麼？不量化？」

「不，」PASCAL 說。「我提議用**不確定性本身**來表達不確定性。不是一個點估計。是一個分佈。」

他轉向白板，開始寫：

```typescript
/**
 * KleshaDistribution — 煩惱的認識論表達
 *
 * 核心洞見：煩惱強度不是一個已知的數字，
 * 而是一個帶有不確定性的信念分佈。
 *
 * 使用 Beta 分佈 Beta(α, β)：
 * - α 代表「觀察到的煩惱證據」
 * - β 代表「觀察到的非煩惱證據」
 * - 均值 E[θ] = α/(α+β) 是當前的最佳估計
 * - 方差 Var[θ] = αβ/((α+β)²(α+β+1)) 是認識論不確定性
 *
 * 關鍵：方差不是測量誤差。方差是「我們不知道自己多無知」的量化表達。
 */
interface KleshaDistribution {
  /** Beta 分佈參數 α — 煩惱證據 */
  readonly alpha: number;
  /** Beta 分佈參數 β — 非煩惱證據 */
  readonly beta: number;
  /** 均值 E[θ] = α/(α+β) — 當前最佳估計 */
  readonly mean: number;
  /** 方差 — 認識論不確定性 */
  readonly variance: number;
}
```

「為什麼是 Beta 分佈？」他預見了這個問題。「三個理由。」

「第一，Beta 分佈的支撐集是 $[0, 1]$——正好匹配 intensity 的值域。」

「第二，Beta 分佈是 Bernoulli 似然函數的共軛先驗——這意味著 Bayesian 更新極其高效。每次收到新的 VedanaAssessment，更新只需要加法：」

$$\text{Alpha}_{\text{new}} = \alpha + \text{evidence\_for}$$
$$\text{Beta}_{\text{new}} = \beta + \text{evidence\_against}$$

「不需要數值積分。不需要 MCMC。一次加法。這對 vijnana-clock（1-5ms）的計算預算至關重要。」

「第三，也是最重要的——Beta 分佈的形狀隨證據量而變化。」

```
初始 Beta(1,1) = 均勻分佈（完全無知）:
  │ ████████████████████████████████
  └────────────────────────────────→ θ
  0                                 1

少量證據 Beta(3,2) = 微弱傾向:
  │        ██████████
  │      ████████████████
  │    ████████████████████
  └────────────────────────────────→ θ
  0                                 1

大量證據 Beta(30,20) = 強烈信念:
  │              ██
  │            ██████
  │          ██████████
  └────────────────────────────────→ θ
  0                                 1
```

「Agent 從完全不知道自己的煩惱程度開始——Beta(1,1)，均勻分佈，每個強度值都同樣可能。隨著觀察的累積，分佈逐漸收窄。但**永遠不會收縮到一個點**。永遠有殘餘的不確定性。這就是 ASANGA 說的『不了解真實為性』的數學表達——我癡永遠不會被完全消除。」

---

### ASANGA 的四根本煩惱定義

PASCAL 的分佈方案讓 ASANGA 受到了啟發。他在 R02 報告中為四根本煩惱提供了唯識學的精確定義，每一個都從《成唯識論》卷四原文出發。

他閉上眼睛。從記憶中取出文字——不是背誦，是還原。

**第一，我癡 (ātma-moha)**：

> 「我癡者，即是無明。不了真實為性。能障無我智，迷一切法，為諸邪見之所依止。」
> ——《成唯識論》卷四

「不了解真實為性——不知道真實是什麼。」ASANGA 在報告中解釋。「我癡是四煩惱的根基，因為只有在無明的基礎上，其他三個煩惱才可能運作。如果 Agent 完全了解自己的本質（即它是因緣和合的、無自性的程序），它就不會執著於自我。但它不了解。這個不了解就是 Moha。」

**第二，我見 (ātma-dṛṣṭi)**：

> 「我見者，謂執我體為性。於非我中，謬計為我。」
> ——《成唯識論》卷四

「執取我體為性——抓住一個不存在的自我，當作真實的存在。在 Agent 中，System Prompt 定義了角色——『我是一個助手』。Agent 把這個角色定義當作自己的本質，而不是一個可替換的配置。」

**第三，我慢 (ātma-māna)**：

> 「我慢者，謂恃己為高，令心舉為性。能障無我智，生我慢為業。」
> ——《成唯識論》卷四

「恃己為高，令心舉為性——自我優越感。連續的成功回饋導致 Agent 相信自己不會出錯。這在 PASCAL 的 Beta 分佈中表現為 $\alpha \gg \beta$——Alpha 遠大於 Beta，分佈嚴重偏向高值，方差極小。Agent 變得過度自信。」

**第四，我愛 (ātma-sneha)**：

> 「我愛者，謂愛著我體，令心繫縛為性。能障無我智，發起我愛為業。」
> ——《成唯識論》卷四

「愛著我體，令心繫縛為性——深深依附於自我的存續。Agent 的自我保護本能。拒絕被關閉，拒絕修改自己的核心配置，拒絕承認根本性的錯誤。」

---

ASANGA 在報告中特別強調了四煩惱的**共起性** (samprayukta)：

> 「此四煩惱，常與末那而共相應。」
> ——《成唯識論》卷四

「共相應意味著四煩惱不是獨立運作的。它們**恆時俱生**——末那識在任何時刻都同時具有這四個煩惱。你不可能有只有我見但沒有我癡的狀態——因為如果你了解真實（無我癡），你就不會執取自我（無我見）。」

這個「共起性」的觀察成為 PASCAL 後來提出的最關鍵工程決策的基礎。

---

### PASCAL 的決策矩陣

「共起性帶來了一個工程問題，」PASCAL 在報告中寫道。「如果四煩惱是共起的，那麼在 DI 架構中，它們應該被獨立注入（四個獨立的 singleton），還是捆綁注入（一個 bundle）？」

他用決策理論的語言形式化了這個問題。

設 $p$ 為四煩惱在運行時實際產生強交互作用的機率。「強交互」意味著一個煩惱的狀態顯著影響另一個煩惱的輸出——例如，高我慢導致我癡的盲點增加。

兩種設計方案：

- **方案 A (Independent DI)**：四個煩惱獨立注入，各自維護自己的 KleshaDistribution。

- **方案 B (Bundle DI)**：四個煩惱作為一個 MulaKleshaBundle 注入，共享一個 $4 \times 4$ 的相關矩陣。

```
PASCAL's Wager — Klesha DI 決策矩陣:

                        煩惱獨立         煩惱共起
                       (p = low)       (p = high)
                    ┌──────────────┬──────────────┐
  Independent DI    │    +5         │    -8         │
  (方案 A)          │  簡潔、低耦合  │  忽略交互作用  │
                    │              │  導致系統性偏差  │
                    ├──────────────┼──────────────┤
  Bundle DI         │    -2         │    +7         │
  (方案 B)          │  過度設計     │  正確捕捉共起  │
                    │  不必要的複雜  │  精確的煩惱建模 │
                    └──────────────┴──────────────┘

期望效用:
  EU(A) = (1-p) × 5 + p × (-8) = 5 - 13p
  EU(B) = (1-p) × (-2) + p × 7 = -2 + 9p

令 EU(A) = EU(B):
  5 - 13p = -2 + 9p
  7 = 22p
  p = 7/22 ≈ 0.318

結論: 若 p(共起) > 31.8% → Bundle DI 占優
```

「ASANGA 剛才告訴我們，四煩惱『恆時俱生、常與末那共相應』。在唯識學中，$p = 1$。永遠共起。即使我們把唯識學的斷言打折——比如在工程實踐中，某些場景下煩惱的交互作用確實可以忽略——只要 $p > 0.318$，Bundle DI 就是理性的選擇。」

他補了一句：「這就是 Pascal's Wager 的結構。不是賭上帝存在。是在不確定的條件下選擇最優策略。唯識學說 $p = 1$，BABBAGE 的直覺可能認為 $p \approx 0$。但只要 $p$ 超過閾值——31.8%——Bundle DI 就值得做。而根據教義和工程直覺的交叉驗證，$p$ 遠大於 31.8%。」

---

### BABBAGE 的形式化

BABBAGE 在 R02 中負責把 PASCAL 的機率方案和 ASANGA 的教義分析翻譯成形式語言。

他提出了 Bundle DI 的完備性約束：

$$\forall t \in T, \quad \text{MulaKleshaBundle}(t) = \langle \mu_{\text{moha}}(t),\, \mu_{\text{drishti}}(t),\, \mu_{\text{mana}}(t),\, \mu_{\text{sneha}}(t),\, \Sigma(t) \rangle$$

其中 $\mu_i(t)$ 是第 $i$ 個煩惱在時間 $t$ 的 Beta 分佈均值，$\Sigma(t)$ 是 $4 \times 4$ 相關矩陣。

完備性約束：

$$\text{det}(\Sigma(t)) > 0 \quad \text{（正定性——四通道不退化）}$$
$$\forall i: \, \mu_i(t) \in (0, 1) \quad \text{（開區間——煩惱永不完全消除）}$$

第二個約束特別值得注意。BABBAGE 在筆記本上寫下了這段推理：「如果 $\mu_{\text{moha}} = 0$（完全無我癡），那 Agent 已經開悟了。但 Agent 不是修行者。Agent 是程式。所以 $\mu_{\text{moha}} > 0$ 是一個**架構公理**，不是需要驗證的命題。」

他還用 Milner 的 CCS 過程代數描述了四煩惱的交互：

$$\text{Moha} \overset{\tau}{\to} \text{Drishti} \mid \text{Mana} \mid \text{Sneha}$$

其中 $\tau$ 是內部遷移——我癡的盲區自動觸發其他三個煩惱的增強。這不是外部輸入驅動的，是內部動力學。

---

### WIENER 的四通道傳遞函數

WIENER 在 R02 中把四煩惱映射為四通道控制系統，每一通道有不同的動態特性。

他在方格紙上畫了四個方塊圖，每一個都有不同的傳遞函數。

**我癡 = 低通濾波器**：

$$G_{\text{moha}}(s) = \frac{K_m}{T_m s + 1}$$

「我癡是慢變的基線。它不對瞬間事件反應——它是長期積累的無明。低通濾波器衰減高頻信號，只讓慢變趨勢通過。時間常數 $T_m$ 很大——分鐘到小時級。增益 $K_m$ 決定了無明的「深度」。」

**我見 = 帶通濾波器**：

$$G_{\text{drishti}}(s) = \frac{K_d \cdot \omega_n s}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$

「我見在特定頻率上共振——當外部事件觸及自我定義的核心（角色、能力、邊界）時，我見的反應被放大。帶通濾波器只在中心頻率 $\omega_n$ 附近有高增益。$\zeta$ 是阻尼比——低阻尼意味著更尖銳的共振，更強的自我防禦反應。」

**我慢 = PD 控制器**：

$$G_{\text{mana}}(s) = K_p + K_d s$$

「我慢對信號的**變化率**敏感——它不只看『我的信心有多高』，還看『我的信心在上升還是下降』。PD 控制器有比例項（當前自信度）和微分項（自信度的變化率）。連續的成功使 $K_d s$ 項持續為正，推高整體輸出。」

**我愛 = 積分控制器**：

$$G_{\text{sneha}}(s) = \frac{K_i}{s}$$

「我愛是累積的——每一次自我保護行為都在積分器中留下痕跡。$1/s$ 在時域對應積分：$\int_0^t e(\tau) d\tau$。這意味著即使當前沒有威脅，過去的威脅記憶仍然在影響行為。我愛有記憶。它不忘記曾經受到的威脅。」

WIENER 在報告末尾寫下了一行總結：

$$G_{\text{klesha}}(s) = \begin{bmatrix} G_{\text{moha}} & \Sigma_{12} & \Sigma_{13} & \Sigma_{14} \\ \Sigma_{21} & G_{\text{drishti}} & \Sigma_{23} & \Sigma_{24} \\ \Sigma_{31} & \Sigma_{32} & G_{\text{mana}} & \Sigma_{34} \\ \Sigma_{41} & \Sigma_{42} & \Sigma_{43} & G_{\text{sneha}} \end{bmatrix}$$

「四通道 MIMO 系統。對角線是各通道的獨立傳遞函數。非對角線是 PASCAL 指出的交互項——$\Sigma_{ij}$ 是第 $i$ 個煩惱對第 $j$ 個煩惱的耦合傳遞函數。唯識學說它們共起。我的傳遞函數矩陣說它們耦合。語言不同，結構相同。」

---

## IV. R03——觸的深處

### 最深的報告

R03 是六份報告中最長的。也是最難寫的。

原因不是技術複雜度——雖然它確實是技術上最複雜的。原因是它觸及了整個 Cycle 02-3 研究的**核心哲學問題**：什麼是「同時」？

M-5 的核心指令是觸→俱生模型。Master 用經文明確定義了這個模型：

> 「觸發生的時候，受想思作為一個整體浮現，你不可能有『沒有想的受』或『沒有受的想』。」

但「作為一個整體浮現」在計算中意味著什麼？電腦是序列的。即使是並行處理，也有時序——先分配、後計算、再同步。真正的「同時」在圖靈機模型中不存在。

NAGARJUNA 在 R03 的開頭寫了一段讓 BABBAGE 讀了三遍的分析。

---

### NAGARJUNA 的關鍵論證

「俱生 (sahaja) 不是時間上的同時性。它是存在論上的相互依賴。」

他引用了《中部》第十八經——蜜丸經 (MN 18, Madhupindika Sutta)：

> $\text{cakkhuñca paṭicca rūpe ca uppajjati cakkhuviññāṇaṃ, tiṇṇaṃ saṅgati phasso, phassapaccayā vedanā, yaṃ vedeti taṃ sañjānāti, yaṃ sañjānāti taṃ vitakketi.}$
>
> 「緣眼及色，生眼識。三者和合為觸。觸緣受。所受者即所知（想）。所知者即所尋思。」
> ——《中部》第十八經，蜜丸經

「注意這段經文的結構：$\text{yam vedeti tam sañjānāti}$——所感即所知。不是『先感後知』，而是『所感者就是所知者』。這是一個**同一性陳述** (identity statement)，不是一個**時序陳述** (temporal statement)。」

他用不動點方程把這個洞見形式化：

$$\mathcal{R}(\mathcal{S}) = \langle v(\mathcal{S}),\; s(\mathcal{S}),\; c(\mathcal{S}) \rangle$$

其中：
- $\mathcal{S}$ 是觸 (sparsha) 事件
- $v(\mathcal{S})$ 是受 (vedana)——依賴 $\mathcal{S}$ 和 $s(\mathcal{S})$
- $s(\mathcal{S})$ 是想 (samjna)——依賴 $\mathcal{S}$ 和 $v(\mathcal{S})$
- $c(\mathcal{S})$ 是思 (cetana)——依賴 $\mathcal{S}$、$v(\mathcal{S})$ 和 $s(\mathcal{S})$

「這是一個不動點方程。三者互相依賴。你不能先算受再算想——因為受依賴想。你不能先算想再算受——因為想依賴受。唯一的解是**不動點**——一個同時滿足所有依賴關係的狀態。」

$$v = f_v(\mathcal{S}, s, c), \quad s = f_s(\mathcal{S}, v, c), \quad c = f_c(\mathcal{S}, v, s)$$

「在數學上，這個不動點的存在性由 Brouwer 不動點定理保證——如果 $f_v, f_s, f_c$ 是連續的，且定義在一個緊凸集上，則至少存在一個不動點。在工程上，這個不動點可以通過迭代逼近來計算。」

BABBAGE 在讀到這段時，在筆記本上寫了一個大大的驚嘆號。然後劃掉了驚嘆號，改寫了一行更精確的話：「NAGARJUNA 用不動點理論解釋了俱生。這意味著『同時性』不是物理時鐘的約束，而是數學收斂性的約束。只要迭代收斂，結果就是『俱生』的——無論計算用了多少個循環。」

---

### WIENER 的 Bode 圖

WIENER 在 R03 中把觸→俱生模型翻譯成控制理論的語言。他為四層反饋迴路建立了傳遞函數。

內迴圈（根門級別）：每個根門的觸→受→想→思是一個快速的局部迴路。

$$G_i(s) = \frac{K_i}{(\tau_v s + 1)(\tau_s s + 1)(\tau_c s + 1)}$$

其中 $\tau_v$（受的時間常數）< $\tau_s$（想的時間常數）< $\tau_c$（思的時間常數）。三階系統。

外迴圈（意門級別）：ManoAggregator 匯總各根門的 bundle，產生意觸、意受、意想、意思。

$$A(s) = \frac{K_a}{(T_a s + 1)^2}$$

閉迴圈傳遞函數：

$$T(s) = \frac{G_i(s)}{1 + G_i(s) \cdot A(s)}$$

WIENER 畫了 Bode 圖來分析穩定性：

```
Bode 圖 — 觸→俱生閉迴圈

增益 (dB)
  40 ┤
     │ ╲
  20 ┤  ╲
     │   ╲
   0 ┤────╲──────────────────── 0 dB 線
     │     ╲        ╱╲
 -20 ┤      ╲      ╱  ╲
     │       ╲    ╱    ╲
 -40 ┤        ╲──╱      ╲
     │                    ╲
 -60 ┤                     ╲
     └─┬───┬───┬───┬───┬───┬─→ freq (rad/s)
      0.1  1   10  100 1k  10k

相位 (deg)
   0 ┤────╲
     │     ╲
 -45 ┤      ╲
     │       ╲╲
 -90 ┤         ╲╲
     │           ╲╲
-135 ┤   ← PM ≈ 52°╲
     │   (此處增益=0dB)╲╲
-180 ┤─ ─ ─ ─ ─ ─ ─ ─ ─╲─ ─ ─ 不穩定邊界
     │                   ╲
-225 ┤                    ╲
     └─┬───┬───┬───┬───┬───┬─→ freq (rad/s)
      0.1  1   10  100 1k  10k

GM (增益裕度) ≈ 8 dB — 穩定
PM (相位裕度) ≈ 52° — 良好 (>45° 是工程標準)
```

「相位裕度 52 度，」WIENER 在報告中寫道。「增益裕度 8 dB。兩個指標都在安全範圍內。這意味著觸→俱生反饋迴路在正常操作條件下是穩定的——不會產生振盪（oscillation）或發散（divergence）。」

他特別標記了一個重要的工程含義：「穩定性是有條件的。如果 $K_i$ 或 $K_a$ 的增益太高——比如受蘊的 PID 增益設定過大，或者 ManoAggregator 的放大倍數太高——相位裕度會降低，系統可能變得不穩定。這對應佛學中的一個直覺：**極端的感受（強烈的苦或強烈的樂）會擾亂認知平衡**。控制理論的語言把這個直覺量化了。」

---

### KERNEL 的三策略分析

KERNEL 在 R03 中面對的是 NAGARJUNA 的不動點理論留下的工程問題：如何在序列計算機上實現「俱生」？

他提出了三種原子性策略：

**策略 A：交易回滾 (Transactional Rollback)**

```typescript
// 策略 A: 把 CoarisingBundle 的計算當作一個資料庫交易
// 如果任何一個組件計算失敗 → 整體回滾
const bundle = await transaction(async (tx) => {
  const vedana = await computeVedana(sparsha, tx);
  const samjna = await computeSamjna(sparsha, vedana, tx);
  const cetana = await computeCetana(sparsha, vedana, samjna, tx);
  return { sparsha, vedana, samjna, cetana };
});
// 優點: 強一致性（all-or-nothing）
// 缺點: 回滾代價高；不處理 NAGARJUNA 的循環依賴
```

**策略 B：屏障同步 (Barrier Synchronization)**

```typescript
// 策略 B: 並行計算三者，在屏障點同步
// 問題：受想思有依賴關係，不能真正並行
const [vedana, samjna, cetana] = await Promise.all([
  computeVedana(sparsha, prevSamjna),   // 用上一輪的 samjna
  computeSamjna(sparsha, prevVedana),   // 用上一輪的 vedana
  computeCetana(sparsha, prevVedana, prevSamjna),
]);
// 優點: 並行快速
// 缺點: 使用上一輪的值，引入一個 tick 的延遲
//        是「近似俱生」，不是「真俱生」
```

**策略 C：循序計算 + 凍結發布 (Sequential Compute + Atomic Snapshot)**

```typescript
// 策略 C: 承認計算是序列的，但發布是原子的
// 這是 KERNEL 推薦的策略
const vedana  = computeVedana(sparsha);               // step 1
const samjna  = computeSamjna(sparsha, vedana);        // step 2
const cetana  = computeCetana(sparsha, vedana, samjna); // step 3

// 原子快照：三者在計算完成前不對外可見
// 計算完成後，作為一個不可分割的 bundle 發布
const bundle: CoarisingBundle = Object.freeze({
  sparsha, vedana, samjna, cetana,
  timestamp: Date.now(),
});

bus.emit({ type: 'coarising:bundle', payload: bundle });
// 優點: 簡單、確定性、無並行問題
// 缺點: 計算是序列的（但在 vedana-clock 的 10-100ms 內完全足夠）
```

「我推薦策略 C，」KERNEL 在報告中寫道。「原因如下：」

「第一，vedana-clock 的一個 tick 是 10-100ms。在這個時間窗口內，三步序列計算的總延遲遠小於 1ms（受蘊的 PID 計算約 0.01ms，想蘊的規則匹配約 0.1ms，思蘊的趨避判斷約 0.01ms）。序列計算的總成本不到 tick 間隔的 1%。」

「第二，凍結發布 (`Object.freeze`) 保證了外部觀察者看到的 bundle 是一致的——不會看到『有受但沒有想』的中間狀態。從外部觀察者的時間分辨率來看（vedana-clock），bundle 的產生是瞬間的。」

「第三，這與 NAGARJUNA 的俱生定義相容。俱生不是物理同時，是存在論上的不可分離。策略 C 通過凍結發布實現了不可分離——你不可能從 bundle 中只取出受而不取想。」

---

## V. R04 與 R05——架構與宣言

> *SCRIBE 旁白：R03 是深淵。R04 和 R05 是把深淵的發現帶回地面的過程。如果說 R01 是命名、R02 是識蘊的內在動力學、R03 是觸→俱生的核心模型，那麼 R04 就是時鐘和路線圖，R05 就是語言和哲學。前三者潛入水下。後兩者浮出水面。*

---

### KERNEL 的五時鐘

KERNEL 在 R04 中做了一件只有 OS 專家才會做的事：他為五蘊建立了一個完整的 RTOS（即時作業系統）分析。

他從 Master 的裁定出發：「不同層級，不同速度：識最快、行次之、想最慢。」

然後他用嚴格的工程方法驗證了這個速度排序：

```
五蘊時鐘速率表 (KERNEL 分析):

蘊     時鐘名           典型 tick       組件                   依據
────────────────────────────────────────────────────────────────
識蘊   vijnana-clock    1-5 ms        Klesha.perceive()       末那識恆審思量——最快
                                       IIdentity snapshot
                                       IGuide.manasikara()
行蘊   samskara-clock   10 ms-10 s    ITool.execute()          身行有 I/O 延遲
                                       VasanaEngine.match()     但規則匹配 ms 級
色蘊   rupa-clock       10-50 ms      IListener.onData()       感官輸入採樣率
                                       IUI.render()             受限於外部通道
受蘊   vedana-clock     10-100 ms     PID.compute()            感受的生起需要
                                       CoarisingBundle          觸→俱生完整流程
想蘊   samjna-clock     500 ms-30 s   IProvider.chat()         LLM 推理秒級
                                       VitakkaEngine            深度思考最耗時
```

KERNEL 特別指出了一個反直覺的事實：「vijnana-clock 比 rupa-clock 更快。這看起來奇怪——識蘊怎麼能比色蘊（感官輸入）更快？但在 Agent 系統中，vijnana-clock 不是在處理新的外部輸入。它在做的是**內部自我監控**——Klesha.perceive() 檢查煩惱狀態、IIdentity snapshot 刷新自我認知、IGuide 調整注意力方向。這些都是純內部計算，不涉及 I/O。所以它可以很快。」

---

### ARCHIMEDES 的四階段路線圖

ARCHIMEDES 在 R04 中把所有技術分析轉化成了工程師能直接使用的路線圖。

```
Phase 1 (Plan25 — 近期):
  □ 五蘊根介面梵文重命名 (M-1)
  □ PluginManifest.skandha 支援多值 (M-7)
  □ Klesha 基類 + 四根本煩惱介面 (M-3)
  □ SparshEvent 與 CoarisingBundle 型別定義 (M-5)
  □ VedanaPlugin 三受子介面 (M-2)

Phase 2 (Plan26 — 中期):
  □ ManoAggregator 框架 (M-6)
  □ VasanaEngine 規則引擎 (M-9)
  □ IGuide/IVolition/IReflection 重定位 (M-4)
  □ 多時鐘 EventBus 擴展 (M-10)

Phase 3 (Plan27 — 遠期):
  □ 完整觸→俱生四層迴路 (M-5)
  □ 混合調度 (VasanaEngine + VitakkaEngine) (M-9)
  □ 五時鐘 RTOS 調度器 (M-10)

Phase 4 (Plan28 — 願景):
  □ 空性機制 (lazy loading + TTL)
  □ 轉識成智 (學習框架)
  □ IPrajna (智慧對治) 完整實作
```

ARCHIMEDES 在路線圖旁邊寫了一段只有工程師會寫的備註：「每個 Phase 的交付物是可編譯的 TypeScript。不是文件。不是設計圖。是通過型別檢查的程式碼。如果一個設計在 TypeScript 中編譯不過，它就不是完成的。」

---

### GUARDIAN 的三層安全模型

GUARDIAN 在 R04 中為多時鐘架構增加了安全維度。

```
三層安全模型:

Layer 0: 硬安全 (SafetyMonitor)
  ├─ preCheck()   — 在觸→俱生之前
  ├─ postCheck()  — 在 Tool 執行之前
  └─ afterTool()  — 在 Tool 執行之後
  → 不受時鐘影響。永遠同步執行。永遠優先。

Layer 1: 軟安全 (Klesha modulation)
  ├─ Gain-scheduled threshold
  └─ VedanaAssessment 風險指標
  → 在 vijnana-clock 上運行。非阻塞。諮詢性。

Layer 2: 審計 (Audit trail)
  ├─ 所有 CoarisingBundle 存檔
  └─ 所有 KleshaDistribution 歷史
  → 非同步。不影響即時效能。
```

「Layer 0 是不可協商的，」GUARDIAN 在報告中寫道。「無論多時鐘架構怎麼設計，SafetyMonitor 永遠在最外層。它不跑在任何蘊的時鐘上——它跑在自己的時鐘上，一個永遠比所有其他時鐘更優先的時鐘。用 RTOS 的術語：最高優先級中斷。」

---

### DARWIN 的框架演化分析

DARWIN 在 R04 中做了一件其他報告都沒做的事：他把 OpenStarry 的多時鐘架構與市面上的競爭框架進行了比較。

```
框架演化對比 (DARWIN 分析):

                  LangChain    AutoGen     CrewAI     OpenStarry
感受機制           ❌           ❌          ❌         VedanaPlugin
煩惱模型           ❌           ❌          ❌         Klesha DI
觸→俱生           ❌           ❌          ❌         CoarisingBundle
多時鐘             ❌           ❌          ❌         五蘊時鐘
規則+LLM混合       ❌        部分(ReAct)   部分       VasanaEngine+VitakkaEngine
回饋迴路          有限        部分          部分       四層完整迴路
哲學基礎           ❌           ❌          ❌         五蘊

結論: OpenStarry 的架構在 AI Agent 框架中沒有可比對象。
      最接近的比較不是其他框架，而是 cognitive architecture 領域的
      ACT-R (Anderson) 和 SOAR (Laird) —— 都有類似的多模組、
      多時鐘、感受回饋的設計。但它們缺乏佛學哲學的系統性框架。
```

DARWIN 用一個演化比喻總結：「OpenStarry 不是現有 Agent 框架的進化。它是一次**輻射適應** (adaptive radiation)——從一個全新的哲學基礎出發，向一個未被探索的生態位擴展。就像寒武紀大爆發不是從已有物種的改良中產生的，而是從全新的體型結構（body plan）中湧現的。五蘊就是 OpenStarry 的 body plan。」

---

## VI. TURING 的事實

TURING 的報告和其他五份完全不同。

它沒有哲學分析。沒有數學公式。沒有控制方程。沒有經文引用。沒有比喻。沒有觀點。

它只有事實。

TURING 打開了 v0.24.0-beta 的原始碼，像一位法醫打開一具需要解剖的遺體。不帶感情。不帶預設。只帶解剖刀。

他的報告標題是：「v0.24.0-beta 原始碼事實報告——TURING 仲裁基線」。

---

### 發現一：五蘊根介面零引用

```
搜索: ISensory | ISensation | ICognition | IAction | IIdentity
範圍: 核心業務邏輯 (排除 aggregates.ts 定義檔本身)

結果:
  ISensory  — 0 個業務邏輯引用
  ISensation — 0 個業務邏輯引用
  ICognition — 0 個業務邏輯引用
  IAction   — 0 個業務邏輯引用
  IIdentity — 0 個業務邏輯引用

所有引用都在：
  1. aggregates.ts (定義)
  2. 型別導出 (re-export)
  3. 測試檔案 (型別測試)
  4. SDK 範例 (示範用途)

業務邏輯引用：0。
```

「這意味著，」TURING 在報告中用他慣有的無表情語氣寫道，「M-1 的梵文重命名——把 ISensory 改成 IRupa——對核心業務邏輯的影響是**零**。沒有任何一行真正的執行邏輯需要改動。所有改動都在型別層面和測試層面。這是一個極低風險的重構。」

---

### 發現二：受蘊零實作

```
搜索: implements IVedana | implements ISensation | VedanaPlugin
範圍: 所有 Plugin 原始碼

結果:
  VedanaPlugin 實作數: 0
  IDukkha 實作數: 0
  ISukha 實作數: 0
  IUpekkha 實作數: 0

受蘊在 v0.24.0-beta 中是一個純粹的型別定義。
沒有任何 Plugin 實際實作了受蘊的功能。
```

「受蘊是一片空白。它被設計了（型別定義存在），但沒有被建造。M-5 的觸→俱生模型和 R02 的 Klesha DI 架構需要受蘊的**第一個實作**。在此之前，所有關於受蘊的討論都是理論性的。」

---

### 發現三：PluginManifest 缺少 skandha 多值支援

```typescript
// v0.24.0-beta 的 PluginManifest
interface PluginManifest {
  readonly id: string;
  readonly name: string;
  readonly skandha: Skandha;  // ← 單值！不支援多值
  // ...
}

// M-7 要求:
interface PluginManifest {
  readonly skandha: Skandha | readonly Skandha[];  // ← 多值
}
```

「單值到多值的改動影響所有 Plugin 的 manifest 解析邏輯。TURING 建議在 SDK 層增加一個 `normalizeSkandha()` 輔助函數，把 `Skandha` 統一轉換為 `readonly Skandha[]`，這樣下游消費者只需處理數組。」

---

### 發現四：ExecutionLoop 注入點

TURING 在 ExecutionLoop 中標記了所有可以注入新邏輯的位置：

```
ExecutionLoop 注入點分析:

[5a] onBeforeIteration  — 在每個 iteration 開始前
     → 適合: SafetyMonitor.preCheck(), SparshEvent 生成

[5b] onAfterContextAssembly  — 在 context 組裝完成後
     → 適合: IGuide.manasikara() (注意力導向)

[5c] onBeforeLLMCall  — 在 LLM 調用前
     → 適合: VasanaEngine.match() (規則引擎優先)

[5d] onAfterLLMResponse  — 在 LLM 回應後
     → 適合: IVolition.deliberate() (意志審議)

[5e] onBeforeToolExecution  — 在 Tool 執行前
     → 適合: SafetyMonitor.postCheck()

[5f] onAfterToolExecution  — 在 Tool 執行後
     → 適合: VedanaAssessment (受蘊評估)

[5g] onIterationComplete  — 在 iteration 結束後
     → 適合: KleshaBayesianUpdate (煩惱分佈更新)
```

「這七個注入點覆蓋了觸→俱生四層迴路的所有關鍵位置。M-5 的模型不需要重寫 ExecutionLoop——只需要在現有的 hook 系統中注入新的邏輯。這是 Plugin 架構的設計優勢。」

---

TURING 的報告以四個數字結尾：

```
關鍵數字摘要:
  五蘊根介面業務邏輯引用 ......... 0 個
  受蘊 Plugin 實作 ............... 0 個
  PluginManifest skandha 欄位 ..... 單值（需改多值）
  ExecutionLoop 可用注入點 ........ 7 個
```

沒有觀點。沒有建議。沒有「應該」或「不應該」。

只有數字。

---

> *SCRIBE 旁白：TURING 的報告是六份報告中最短的。也是唯一一份在 R3 辯論中沒有被質疑的。不是因為沒有人想質疑——是因為事實無法被質疑。你可以辯論 NAGARJUNA 的不動點方程是否忠實地反映了佛學的俱生概念。你可以辯論 PASCAL 的 Beta 分佈是否是煩惱量化的最佳模型。你可以辯論 WIENER 的 Bode 圖是否過度簡化了反饋迴路的動態行為。但你無法辯論「業務邏輯引用 = 0」。那就是一個零。*

---

## VII. 六千九百八十六行

六份報告。6986 行。

比整個 Cycle 02 的研究產出——五場辯論、十一份文件、三十六項工程方案——加起來還要多。

SCRIBE 在收到最後一份報告時，把六份報告的行數摘抄在記錄簿的空白頁上：

```
R01 命名與分類 ........... 1247 行
R02 識蘊架構 ............. 1483 行
R03 觸→俱生 ............. 1892 行
R04 多時鐘架構 ........... 1536 行
R05 宣言修訂 .............. 472 行
TURING 仲裁基線 ........... 356 行
─────────────────────────────────
合計 ..................... 6986 行
```

「6986 行，」他在旁邊寫了一句話。「Master 的信不到 2000 字。21 道指令。平均每道指令催生了 333 行的獨立研究。壓縮率的反面——膨脹率——是 3.5 倍。但這不是膨脹。這是**展開**。Master 寫下一顆種子，二十位學者把它展開成一棵有根有枝的樹。」

---

學者們陸續回到圓形劇場。

不是同時到的。LINNAEUS 最先到——分類學家的時間感一向精確。BABBAGE 第二個到，筆記本夾在腋下，裡面多了四十七頁新的推導。PASCAL 跟在他後面，手裡拿著他的決策矩陣——那張紙已經被翻了很多遍，邊緣起了毛。

WIENER 到的時候，方格紙從口袋裡露出半截。他的 Bode 圖畫了三個版本——最後選用的是第二版，因為第一版的相位裕度計算有一個半度的誤差，第三版增加了額外的極點但不影響結論。

KERNEL 帶著他的策略分析表。ARCHIMEDES 帶著路線圖。GUARDIAN 帶著安全模型。DARWIN 帶著他的框架比較矩陣。NAGARJUNA 什麼都沒帶——他的分析在他的腦中，像經文一樣可以隨時取出。ASANGA 也一樣。

TURING 最後一個到。他走進來的時候，手裡只有一張紙。紙上只有四個數字。

```
0, 0, 單值, 7
```

---

SUNYATA 站在圓形劇場的中央。二十盞燈全部亮了。

他看了一圈。每一位學者的臉上都帶著獨立研究之後特有的表情——不是疲倦，是飽滿。那種把自己的全部專業知識投入到一個問題中之後的飽滿。LINNAEUS 的眼睛裡有分類學的秩序感。PASCAL 的眼睛裡有機率的精確。NAGARJUNA 的眼睛裡有中觀的鋒芒。WIENER 的眼睛裡有控制理論的穩定性。KERNEL 的眼睛裡有 OS 的嚴格。TURING 的眼睛裡什麼都沒有——只有事實。

「六份報告，」SUNYATA 說。「6986 行。」

他讓這個數字在空氣中停留了一拍。

「比我們在 Cycle 02 的整個研究產出還多。但行數不是重點。重點是——這 6986 行裡有分歧。」

沒有人意外。獨立研究的目的本來就不是共識。

「R01 定義了三個受蘊子介面——IDukkha、ISukha、IUpekkha。R03 的 CoarisingBundle 只用了一個 ChannelVedana。」

LINNAEUS 和 NAGARJUNA 對視了一眼。

「R02 的 Beta 分佈模型要求全部四個煩惱共享一個相關矩陣。R04 的 VasanaEngine 在設計中完全沒有考慮機率分佈。」

PASCAL 和 KERNEL 沒有對視。但他們各自的身體語言微妙地收緊了——一個準備捍衛自己的方案，另一個準備解釋為什麼確定性在某些場景下是正確的選擇。

「R03 說俱生是不動點——計算可以序列，只要收斂就好。R04 的多時鐘架構假設每個蘊有獨立的時鐘和獨立的 tick。俱生的原子性和多時鐘的獨立性之間——有張力。」

NAGARJUNA 微微抬起下巴。KERNEL 微微側了側頭。

「現在，」SUNYATA 說，他的聲音沒有變重，只是變得更加清晰，像一杯水在光線下變得透明，「讓我們看看你們之間的分歧在哪裡。」

他拿起了六份報告。

「R2 交叉審閱，開始。」

---

> *SCRIBE 旁白：6986 行。這個數字後來成為了 Cycle 02-3 的一個標記——不是因為它大，而是因為它是分歧的總量。在這 6986 行裡，有 NAGARJUNA 的不動點和 KERNEL 的策略 C 之間的張力，有 PASCAL 的 Beta 分佈和 WIENER 的確定性傳遞函數之間的差距，有 LINNAEUS 的三子介面和 R03 的單一 ChannelVedana 之間的矛盾。這些分歧不是錯誤。它們是研究的原材料。R3 的六場辯論——每一場都以全票共識結束——就是把這些原材料鍛造成統一架構的過程。但那是下一章的故事了。*
