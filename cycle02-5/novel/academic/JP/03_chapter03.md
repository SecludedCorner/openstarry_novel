# 第三章：三面の鏡——D2 Sati Plugin 蘊帰属討論

---

**所要時間**：約60 分 | **議長**：SUNYATA | **投票**：3 項

## 改名戦略（D2-R1：19/20）

`Sati` コード識別子を保留し、文書タイトルを「Mindfulness Architecture」から「Cognitive Loop Quality Monitoring Architecture」に変更する。「命名説明」段落を追加する。セキュリティ文書ではフルネームを使用する。

唯一の反対票：GUARDIAN——文化的背景知識の必要性を完全に排除するため、完全改名を選好。多数決議をセキュリティ文書フルネーム条件付きで受諾した。

## 五蘊構成（D2-R2：18/20）——核心決議

**結論：skandha: ['vedana', 'samjna', 'vijnana']**

四つの機能から三蘊へのマッピング：

| 機能 | Skandha | 説明 |
|------|---------|------|
| EventBus イベント購読（11 種、持続的知覚） | vedana | 認知ループ信号の受信 |
| スライディングウィンドウ + パターン認識 | samjna | イベントストリームからの行動パターン識別 |
| LoopQualityVector + SPC 異常判定 | vijnana | 記述的識別を超えた評価的品質判断 |
| **ツール実行なし、状態変更なし** | **samskara を除外** | 正念修行ではない |

鍵となる論証の転換点：

- **ASANGA**：仏教における正念（smṛti）は行蘊の心所——能動的、意志的、道徳的に正向きである。SatiMonitor は受動的、自動的、価値中立的である。したがって SatiMonitor は正念ではなく、行蘊に帰属させるべきではない。
- **LINNAEUS**：OOP での比較——「IGearArbiter は『呼ばれて見に行く』ものであり、SatiMonitor は『常に見ている』ものである。」持続購読 vs オンデマンド呼び出し——独立した vedana 宣言を構成するに十分である。
- **ARCHIMEDES**（転換点）：三蘊と二蘊の工学的コスト差はゼロである——PluginManifest の skandha フィールドは既に多値をサポートしている。「三蘊は複雑すぎる」という懸念を排除した後、議論は純粋な分類精度に移行し、Proposal B の優位性は圧倒的であった。
- **少数意見**（MESH、KERNEL）：Proposal C ['samjna','vijnana'] は IGearArbiter の分類と対称的であり、長期保守に価値がある。

**歴史的意義**：SatiMonitor は OpenStarry 初の三蘊 plugin となった。

## PluginHooks 専用スロット（D2-R3：20/20）

新たに `monitors?: ISatiMonitor[]` 専用スロットを追加。Cycle 02-4 の `arbiters` 先例に従う（SDK インターフェース → PluginHooks → Registry → PluginLoader の四段階パターン）。

---
