# 序章：整理から構築へ —— Cycle 02-6 の方法論的位置づけ

---

## 研究の文脈と前輪の遺産

Cycle 02-5 は OpenStarry 研究史上最大規模の規範的修正を構成した。29 項の決議、2 項の Master 覆審による覆し、7 件の設計文書再編成である。中核的成果は、装飾的仏教的写像（decorative Buddhist mappings）の体系的除去にあり、「機能分析は術語の伝統に優先する」という方法論的立場を確立した。

Cycle 02-6 はこの遺産を継承するが、研究の性質は根本的に転換する。02-5 の主題が「否定的判断」（何が誤りか）であったとすれば、02-6 は「肯定的構築」（何が正しいか、そして正しいものはいかなる精密な仕様を備えるべきか）である。

---

## 二重の研究委託

**工学的指示**：Plan29 交付物（v0.29.0-alpha）における `IConfidenceAuditor` と `ILoopQualityMonitor` の二つの骨格コンポーネントについて、Master は六つの未解決問題（OQ-29-1〜6）への回答を要求した。AuditContext のフィールド、extras bag プロトコル、監査ログ形式、品質公式とイベント購読、Layer 2/3 統合方式、Plan30 の方向性である。

**哲学的指示**：原始経典（如是我聞）を第一次資料として行蘊（samskara-skandha）を改めて深く掘り下げること。Master は唯識学派が大部分の心所を行蘊に帰属させる手法は「極めて問題がある」と指摘し、「活動と変換」という概念が行蘊のサブカテゴリを拡張しうることを示唆した。

---

## 研究設計：二軌道構造と軌道間制約

SUNYATA（#0）は四軌道構造を設計した：

| 軌道 | 範囲 | 小項目 | 規模 |
|------|------|--------|------|
| Track A | AuditContext + 監査ログ | A1-A4 | 4 組 |
| Track B | ILoopQualityMonitor 仕様 | B1-B4 | 4 組 |
| Track C | 行蘊の哲学的深掘 | C1-C4 | 4 組 |
| Track D | 工学同期 + Plan30 | D1-D2 | 2 組 |

重要な制約：**軌道間影響プロトコル** —— D1（哲学的討論）は D2/D3（工学的討論）に先立って実施されねばならず、哲学的発見が即座に工学設計へ注入されることを保証する。

---

## 研究プロセスの概観

```
R0 方向設定 → R1 独立研究（14 件の報告） → R2 交差査読 → R3 討論（3 場 / 17 決議） → R4 成果確定
```

R1 段階では 14 件の独立研究報告が産出された。チームの配分は以下の通りである：

| 報告 | 主題 | 担当 |
|------|------|------|
| A1 | AuditContext 型定義 | VITRUVIUS + KERNEL |
| A2 | extras bag メカニズム | DARWIN + MESH |
| A3 | 監査ログ仕様 | GUARDIAN + ARCHIMEDES |
| A4 | Layer 2/3 統合経路 | WIENER + BABBAGE |
| B1 | 四次元計算公式 | WIENER + ATHENA + BABBAGE |
| B2 | EventBus イベント仕様 | HERACLITUS + TURING |
| B3 | extras 書き込み統合 | LEIBNIZ + MESH |
| B4 | 重み付けと構成 | PASCAL + ATHENA |
| C1 | 原始経典における行蘊 | NAGARJUNA + ASANGA |
| C2 | 唯識心所批判 | ASANGA + NAGARJUNA |
| C3 | ISamskara 拡張方向 | LINNAEUS + PENROSE |
| C4 | 心智論述の工学的示唆 | PASCAL + PENROSE |
| D1 | v0.29.0-alpha コード検証 | TURING + ARCHIMEDES |
| D2 | Plan30 方向性提案 | VITRUVIUS + GUARDIAN |

R2 では 24 の合意点と 3 の分岐点（extras 書き込みプロトコル、extras キー命名、loopQualityFn のデータソース）が識別された。R3 は合計約 245 分間、17 項の決議中 13 項が全会一致（20/20）で可決、0 項が否決、0 項が Master 覆審となった。

以下の各章では順次展開する。哲学軌道における行蘊の深掘（第一章）、監査コンテキストの設計（第二章）、品質監視公式（第三章）、統合アーキテクチャ（第四章）、Master の心所に関する指示（第五章）、討論の方法論的分析（第六章）、工学青写真と総括（第七章）である。

---
