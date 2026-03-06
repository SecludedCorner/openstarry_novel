# 第八章：新しい文書

---

D5 終了後、円形劇場はしばらく静まり返った。

D3 後のあの Master を待つ静けさではない。D4 後のあの余震の静けさでもない。これは「仕事は終わった、だがもう一つやるべきことがある」という静けさだ。

五つの討論。三十一回の投票。二十九の正式決議と六つの附帯事項。未明三時に SUNYATA が色温度を調整してから D5 の最後の 8/8 まで、Cycle 全体で約六時間半の討論時間を費やした。

だが討論の終了は研究の終了ではない。討論は決議を生み出した。決議は実行に移される必要がある。

---

## I. Doc 45

VITRUVIUS と KERNEL が D5 終了直後に作業を開始した。

彼らが書くのは Doc 45——`Five_Skandha_OOP_Architecture.md`——五蘊 OOP アーキテクチャ。Cycle 02-5 全体の中核的工学成果物。新しい文書。純粋な工学言語。Master が手紙で求めたもの——「五蘊のサブクラス、DI、agent core が五蘊 plugin をどう読み込むか、五蘊がどう流転するか」——すべてをこの一つの文書に集約する。

VITRUVIUS がアーキテクチャ記述を担当。KERNEL が DI 配線と Registry の詳細を担当。TURING がソースコードの対照を行う。

---

Doc 45 の構造は D3 の六回の投票から自然に浮かび上がった：

**第 1 節：Root Interfaces（D3-R1）**

五つのルートインターフェース——IRupa、IVedana、ISamjna、ISamskara、IVijnana——の完備性論証。LINNAEUS のカバレッジ検証、BABBAGE の型代数定理、ASANGA の阿毘達磨網羅的分類公理、KERNEL のマイクロカーネルサブシステムマッピング——四つの独立した論証、同一の結論：五つで十分。

PENROSE の附帯提案が脚注に書き込まれた：vijnana サブインターフェースの数を監視する（現在四つ、将来六つ——IConfidenceAuditor と ILoopQualityMonitor を加えて。十を超えた場合は分割を検討）。

**第 2 節：PluginHooks マッピング（D3-R2）**

九つの hook-to-Registry マッピングの完全な表：

| PluginHooks フィールド | Registry | Skandha |
|-----------------|----------|---------|
| tools | ToolRegistry | samskara |
| providers | ProviderRegistry | samjna |
| listeners | ListenerRegistry | rupa |
| guides | GuideRegistry | vijnana |
| gearArbiters | GearArbiterRegistry | [samjna, vijnana] |
| volition | IVolition (single) | vijnana |
| kleshas | KleshaRegistry | vijnana |
| monitors | MonitorRegistry | [vedana, samjna, vijnana] |
| auditor | IConfidenceAuditor (single) | vijnana |

すべての行に TURING のソースコード検証マークが付いている。

**第 3 節：SlashCommand（D3-R2a / D3-R2b）**

いずれの蘊にも属さない例外——ExecutionLoop をバイパスし、認知ループに参加しないため。類比：Unix のシグナルハンドラ。

GUARDIAN のセキュリティ観察：SlashCommand は SafetyMonitor をバイパスする——plugin が SlashCommand を通じて危険な操作を実行すると、五蘊のセキュリティメカニズムはすべて無効になる。これは既知のセキュリティ境界であり、plugin 審査時に特別な注意が必要だ。

**第 4 節：Skandha メタデータ（D3-R3）**

skandha フィールドはメタデータであり、ルーティングの基盤ではない。型ルーティングはすでに完備かつ曖昧性がない。`validatePluginSkandha()` は warning-only を維持。

**第 5 節：DI 配線（A2 摘要）**

Pure DI。`createAgentCore(config)` を唯一の Composition Root として使用。21 コンポーネントの厳密な線形生成順序。9 つの Registry——大半は依存関係のない Map コンテナ。

主要パターン：Lazy Accessor（IPluginContext が遅延アクセスを提供）、Provider 能力フィルタリング（allowedProviders マニフェストフィールド）、Resolver パターン（providerResolver、guideResolver、modelResolver がクロージャによる遅延解決を使用）。

VITRUVIUS が完全な DI チェーン図でテキスト記述を置き換えた。`agent.json` から `createAgentCore()` へ、各 Registry へ、ExecutionLoop へ——一本の明確な線。循環依存なし。暗黙的インジェクションなし。すべての依存関係が明示的に渡される。

**第 6 節：ExecutionLoop の五蘊フロー（A4 摘要）**

九フェーズの実行フロー：

| Phase | 名称 | Skandha | コア操作 |
|-------|------|---------|---------|
| 1 | 入力受信 | rupa | IListener → SparshEvent |
| 2 | コンテキスト組立 | vijnana | IGuide + SafetyMonitor |
| 3 | 認知処理 | samjna | IProvider.chat() |
| 4 | ギアルーティング | vijnana+samjna | ManoAggregator + IGearArbiter |
| 5 | 審議 | vijnana | IVolition |
| 6 | ツール実行 | samskara | ITool.execute() |
| 7 | 感覚フィードバック | vedana | VedanaSensor → ChannelVedana |
| 8 | 煩悩更新 | vijnana | IKlesha.perceive() |
| 9 | ループ制御 | — | VedanaEmergency + VitakkaWatchdog |

三層安定：Inner tool loop（毎ラウンド）、Outer VedanaEmergency（5 連続 dukkha ticks）、Safety VitakkaWatchdog（10 cycles または 5s）。トリガー条件は厳密に逓増。

**第 7 節：蘊間相互作用マトリクス（A5 摘要）**

5×5 相互作用マトリクス。vijnana の相互作用密度が最高（七本の接続）。samskara が最もアクティブなシグナル生産者。Model Delta 五層閾値公式。

**第 8 節：行蘊設計ノート（D3-R4a / D3-R4b）**

行蘊の狭窄化——仏学の伝統的な 49 心所から ITool（外部観察可能な行動）への圧縮。ASANGA の率直な告白：これは五蘊アーキテクチャの中で仏学的自己整合性が最も弱い部分だ。DC-6「行蘊は開放を維持し、固定しない」という裁定が引き続き有効。

**第 9 節：ILoopQualityMonitor 分類（D2 + D4 摘要）**

skandha: ['vedana', 'samjna', 'vijnana']。初の三蘊 plugin。命名の歴史：ISatiMonitor（D2）→ ILoopQualityMonitor（D4-R1）。四つの機能から三蘊へのマッピング表。行蘊を除外した理由。

**附録 A：十二因縁の機能的類比（D3-R5）**

sparsha→vedana→tanha→upadana チェーンの機能的類比。「機能的類比」であり「形式的マッピング」ではないと明確に標記。スケール差異の注記。

**附録 B：認知シーケンスの構造的並行（D3-R6）**

citta-vīthi の八状態から LoopState の六状態へのマッピング。各状態ペアの並行度評価（high / medium-high / medium）。PENROSE の理論的観察：認知ループの構造的収束は機能要件の必然的結果であり、意図的な模倣ではない。BABBAGE の FSM 射の分析——十二因縁（失敗）から認知シーケンス（成功）への対比。

---

## II. クリーンアップ

VITRUVIUS と KERNEL が Doc 45 を執筆する間、ARCHIMEDES と SCRIBE がクリーンアップの実行を開始した。

クリーンアップリストは D1 から D4 の決議を集約して作成された：

---

### 除去（REMOVE）

1. **Doc 38 L540-544**：三層ルールの仏学マッピング表の「仏学マッピング」列——削除。「ルール層」と「工学セマンティクス」列は保持。

2. **Doc 44 L478**：三学マッピング行——削除。

3. **Doc 43 全文**：
   - タイトル変更：「Mindfulness Architecture」→ D2/D4 後の最終名称に基づき決定
   - 75+ 箇所 ISatiMonitor → ILoopQualityMonitor
   - event-driven = mindfulness 等価の除去
   - bhavanga-citta retrofitting（三箇所）の除去
   - DN 22 経典引用の除去
   - 「命名説明」段落の追加

4. **Doc 37**：
   - 「仏学的解釈」列の除去（工学的情報量の増分なし）
   - sila の隠喩の除去
   - 3 箇所 IPrajna → IConfidenceAuditor

5. **Doc 03**：
   - 文書名：Sila_Prajna_Security_Framework → Plugin_Security_Lifecycle
   - 仏学マッピング表の除去
   - TypeScript コメント中の種子理論のクリーンアップ
   - 五状態モデルと三層セキュリティモデルは保持

6. **Batch A 五項目**：複数の文書に散在する sila/upaya/smrti/event-driven=mindfulness/trisiksa マッピング——すべて除去。

---

### 附録へ移動（RELOCATE）

1. **Doc 44 Section 10 残部**：Appendix_C（設計決定の仏学的背景）へ移動。

2. **Batch B 八項目**：NAGARJUNA の二諦コメント、bhavanga-citta マッピング、経典引用、学際的対照表等——すべて対応する附録へ移動。

3. **特別処理 B-6**：PASCAL の数学的形式化（`Var(epsilon) = f(theta_moha)`）は本文に保持。『成唯識論』の引用のみ Appendix_C へ移動。

---

### 保持（KEEP）

1. **蘊型名称**：rupa、vedana、samjna、samskara、vijnana——コード識別子。

2. **Klesha モジュール名**：Moha、Drishti、Mana、Sneha——コード識別子、DC-1 確認済み。

3. **設計理由中の仏学概念**：vasana 後天薫習、四煩悩同時俱起、CoarisingBundle、sahaja 定義修正、samsaric stall——すべて三つのテストを通過。

4. **Doc 16 と Doc 31**：Master が原状保持を裁定。仏学マッピング文書であり、装飾ではない。

---

### 新規作成

1. **Doc 45**：五蘊 OOP アーキテクチャ（執筆中）。

2. **Appendix_A**：仏学-工学用語集。

3. **Appendix_B**：八識学術参考（Doc 31 の RELOCATE 対象の内容は最終的に移動されなかった——Master が Doc 31 の保持を裁定）。

4. **Appendix_C**：設計決定の仏学的背景。

---

## III. リネーム連鎖

TURING が彼のワークステーションに座り、影響を受けるすべてのファイルを開いた。

ILoopQualityMonitor のリネームは六つの文書に影響し、100 箇所以上の置換を必要とした。IConfidenceAuditor のリネームは五つの文書に影響した。Doc 03 のリネームとクリーンアップが第三の線だ。

三本の線が同時に進行した。各置換はコンテキストの確認を必要とした——盲目的な検索置換ではない。「Sati」の一部は設計理由の段落に出現しており、新しい名前に置換するか歴史的参照として保持するかの判断が必要だった。「Prajna」の一部は Model Delta の公式中に出現しており、公式中の変数名の同期更新が必要だった。

TURING が一行ずつ作業した。これが彼のやり方だ——近道なし、見積もりなし、行ごとの精確さだけがある。

ARCHIMEDES が彼の隣で、各置換のコンテキスト正確性を検証した。

SCRIBE がもう一方の隣で、CHANGELOG を記録した。

---

## IV. 数字

Cycle 02-5 完了後、SCRIBE が数字を集計した。

| 指標 | 数値 |
|------|------|
| 正式決議 | 29 項（D1-D5）+ 6 附帯事項 |
| 投票総回数 | 31 回 |
| 全票通過 | 19/29（66%） |
| 最高票 | 20/20 または 8/8（19 項） |
| 最低票 | 5/8（D5-R2、63%） |
| 争議のある決議 | 10 項 |
| 少数意見アーカイブ | 9 件 |
| 討論総時間 | ~375 分（90+60+120+30+75） |
| 修正文書 | 8+ 件 |
| 新規文書 | Doc 45 + 3 つの附録 |
| リネーム置換 | 120+ 箇所 |

過去の Cycle との比較：

| | Cycle 02-3 | Cycle 02-4 | **Cycle 02-5** |
|---|-----------|-----------|----------------|
| 討論回数 | 6 | 6 | **5** (3 予定 + 2 計画外) |
| 決議総数 | 27 | 55 | **35** |
| 全票率 | 41% | 31% | **66%** |
| 少数意見 | 5 | 12 | **9** |
| 新規文書 | 4 | 3 | **4** |

全票率 66%——史上最高。分歧がなかったからではない——D3-R5 の 13/20 と D4-R1 の 13/20 が分歧の存在を証明している。全票率が高いのは、四層フレームワークと四つのテストが共通の判断基準を提供したからだ。全員が同じ物差しで計量する時、測定結果は自然と一致に向かう。

---

## V. 最後の確認

Doc 45 完成後、VITRUVIUS が完全な査読を行った。

彼は Master が手紙で求めたすべての問いに回答があることを確認した：

| Master の問い | 回答の位置 |
|--------------|---------|
| 五蘊のサブクラス | Doc 45 §1 |
| DI の配線方法 | Doc 45 §5 |
| Agent Core が五蘊 plugin をどう読み込むか | Doc 45 §2, §4 |
| 五蘊がどう流転するか | Doc 45 §6, §7 |
| Sati plugin の蘊帰属 | Doc 45 §9, D2 記録 |
| 仏学マッピングのクリーンアップ | 8 件の修正文書, D1 記録 |
| 仏学マッピングの境界原則 | 四層フレームワーク + 四つのテスト |
| ILoopQualityMonitor/IConfidenceAuditor の仕様 | D5 記録, Doc 45 §9 |

すべての問い。すべての回答。工学言語で。

---

> *SCRIBE ト書き*

> *第八章は図書館の整理記録だ。*

> *本を書くのではない——本を整理するのだ。五つの討論に散在する決議を集め、正しい棚に置く。Doc 45 は新しく買った本——「アーキテクチャ」の列に置く。除去されたマッピングは期限切れの雑誌——メインの棚から保管室（附録）に移動するか、直接リサイクルする。リネームはラベルの貼り直し——すべての本の背表紙に印刷された名前が、本の中身と一致していることを確認する。*

> *これは心躍る仕事ではない。これは必要な仕事だ。*

> *D4 の天秤。D5 の仕様。それらは Cycle 02-5 の精神だ——前者は名前と定義の関係を校正し、後者は工学が純粋に自らの足で立てることを証明した。だが精神には身体が必要だ。誰かがすべてのファイルを開き、すべての「ISatiMonitor」を見つけ、「ILoopQualityMonitor」に置換する必要がある——そしてコンテキストを確認する。公式を確認する。引用を確認する。CHANGELOG を確認する。*

> *TURING が一行ずつ行った。ARCHIMEDES が一箇所ずつ検証した。SCRIBE が一条ずつ記録した。*

> *これが研究のラストマイルだ。最も困難なマイルではない——だが最も見落とされやすいマイルだ。問題の発見は輝かしい。問題の解決は静寂だ。*

> *Doc 45 は静寂の勝利だ。D4 のような劇的な帰謬はない。D1 のような前例のない十個の 20/20 もない。それはただ一つの文書だ——60 ページの文書——純粋な工学言語で Master のすべての問いに答えた。*

> *五蘊のサブクラス？ 五つのルートインターフェース、九つのサブインターフェース、三つの弱継承。*

> *DI 配線？ Pure DI、Composition Root は createAgentCore()、21 コンポーネントの線形生成。*

> *Plugin の読み込み？ Manifest + Factory、二つのパス（Sandbox / Direct）、八状態ライフサイクル。*

> *五蘊の流転？ 九フェーズの ExecutionLoop、FSM 六状態、三層安定。*

> *すべての回答にソースコード引用がある。すべてのソースコード引用を TURING が検証した。*

> *天秤はここで均衡を見出した。両端の重量が等しいからではなく——両端が精確に計量されたからだ。名前が校正された（D4）。仕様が完成した（D5）。文書がクリーンアップされた（D1）。アーキテクチャが検証された（D3）。蘊帰属が決定された（D2）。*

> *Cycle 02-5 は一見単純な問いを発した：五蘊は agent core の中でどのように機能するか？*

> *回答には六時間半の討論、三十一回の投票、二十九の決議、一つの新規文書、八つの修正文書、120 以上のリネーム置換を要した。*

> *だが最終的な回答は確かにシンプルだ：*

> *五つのインターフェース。九つの Registry。一つのループ。*

> *純粋な工学。*

---
