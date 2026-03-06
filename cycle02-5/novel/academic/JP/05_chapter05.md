# 第五章：名前の代償——D4 命名修正討論

---

**所要時間**：約30 分 | **契機**：Master の査読 | **投票**：3 項

D4 は当初の議題にはなかった。Master の一言によって引き起こされた：

> **「梵語を使うなら、その定義に対して責任を持つ必要がある。Sati の内容が完全に match していると思うか？」**

## NAGARJUNA の帰謬論証

```
前提 A：Sati = 行蘊心所（仏教的定義）
前提 B：SatiMonitor ≠ 行蘊（D2-R2 の結論）
∴ SatiMonitor ≠ Sati
```

正念が仏教において必然的に行蘊であり、D2 で SatiMonitor が行蘊ではないことが証明されたならば——SatiMonitor は正念ではない。正念ではないコンポーネントを Sati と呼ぶべきではない。

ASANGA が確認した：「SatiMonitor が行蘊の活動でないならば、それは Sati ではない。我々自身の分類分析が我々自身の命名を否定したのである。」

## ISatiMonitor → ILoopQualityMonitor（D4-R1：13/20）

ARCHIMEDES の提案が勝利した：「Loop Quality Monitor」——認知ループの品質監視器——機能を正確に記述し、仏教用語なし、隠喩なし。

少数意見：IBehaviorQualityMonitor（GUARDIAN、4 票）、ICognitiveLoopMonitor（NAGARJUNA + ASANGA、2 票）、IQualityMonitor（SYNTHESIST、1 票）。

完全な改名表：ISatiMonitor → ILoopQualityMonitor、SatiQualityVector → LoopQualityVector 等 8 項目。

## IPrajna → IConfidenceAuditor（D4-R2：16/20）

NAGARJUNA：「般若は仏教における最高の認知能力——一切法の実相を照見する智慧である。」

ASANGA：「温度微調整つまみを核融合炉と呼ぶようなものである。」

IPrajna の実際の機能：一つのメソッド、信頼度を入力とし、`{ delta: number, reasoning: string }` を出力する。delta は [-0.05, +0.05] に制限される。これは監査であり——般若ではない。

BABBAGE：IConfidenceAuditor が意味的に最も精確である——独立した、限定範囲の、書面記録を生成する二次チェック。

少数意見：IThresholdCalibrator（WIENER、2 票）、ISecondaryEvaluator（HERACLITUS + PENROSE、2 票）。

## Doc 03 再投票（D4-R3：17/20）

「Sila-Prajna Security Framework」→「Plugin Security Lifecycle」

当初の投票 14/20 で変更なしであった。Master の査読が再検証を引き起こした——四項テストの全てに不合格：必要性（plugin ライフサイクルの理解に種子理論は不要）、コード識別（実際の型は英語を使用）、意思決定駆動（DC 確認なし）、定義責任（戒 ≠ アクセス制御、般若 ≠ CVE 撤回）。

ASANGA の鍵となる区別：Doc 16 = 独立マッピング文書（Master の裁定で保留）vs Doc 03 = 工学文書中の仏教的装飾（清掃すべき）。

## 第四のテスト——定義責任（恒久的基準）

> **「仏教梵語術語をコード識別子として使用する場合、当該コンポーネントの機能はその術語の仏教的定義に一致しなければならない。一致しない場合は、工学術語を使用する。」**

D1 の三項テストを補完する——たとえ名前が Test 2（コード識別）を通過しても、Test 4（定義責任）を通過しなければ、改名すべきである。

影響範囲：ILoopQualityMonitor は 6 件の文書で 100 箇所以上の置換に影響、IConfidenceAuditor は 5 件の文書に影響、Doc 03 は改名 + 内容清掃。

---
