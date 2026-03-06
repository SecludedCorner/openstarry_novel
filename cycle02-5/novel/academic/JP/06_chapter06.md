# 第六章：純粋な工学——D5 Plan29 工学仕様討論

---

**所要時間**：約75 分 | **参加者**：10 名 | **投票**：9 項

D5 は本プロジェクト史上初めて仏教的内容を一切含まない討論であった。十名のエンジニアと科学者、仏教学者ゼロ名（NAGARJUNA と ASANGA が自発的に退席）が、TypeScript インターフェースの精密な仕様を議論した。

TURING が完全な v0.28.0-alpha 設計パターン報告を事前提出した——14 個のソースコードファイル、全 Registry ライフサイクル、timeout パターン、同期／非同期パターン、失敗処理戦略。この「コード考古学」報告が全ての決定に事実的基盤を提供した。

## 九項の決議

| 決議 | 内容 | 票数 |
|------|------|------|
| D5-R1 | 独立した `auditor` hook スロット（monitors を再利用しない） | 8/8 |
| D5-R2 | audit() デュアルモード戻り値 `T \| Promise<T>` | **5/8** |
| D5-R3 | timeout 200ms、fail-safe delta=0、設定可能 | 8/8 |
| D5-R4 | 単一 auditor、last-wins（配列ではない） | 6/8 |
| D5-R5 | 失敗処理：delta=0 + warning log | コンセンサス |
| D5-R6 | MonitorRegistry は ExecutionLoop.onLoopStart() で起動 | 7/8 |
| D5-R7 | LoopQualityVector 等ウェイト 0.25×4 | 8/8 |
| D5-R8 | validatePluginSkandha() は warning-only を維持 | 7/8 |
| D5-R9 | IConfidenceAuditor extends IVijnana、skandha ['vijnana'] | 8/8 |

**最も激しい投票**：D5-R2（5/8）——純非同期 vs デュアルモード。GUARDIAN/KERNEL/VITRUVIUS は純非同期の方がセマンティクスが正確と主張。多数派はデュアルモードを採用し、IGearArbiter の先例とテストの利便性に従った。

## IConfidenceAuditor 最終仕様（100%）

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

PluginHooks 最終形態：
```typescript
interface PluginHooks {
  // ... 既存フィールド ...
  monitors?: ILoopQualityMonitor[];   // Plan29 Wave 1
  auditor?: IConfidenceAuditor;       // Plan29 Wave 2
}
```

NAGARJUNA は D5 終了後にこう評した：「D4 は名前が定義に対して責任を持つべきことを証明した。D5 は、ある種の工学的問題には定義すら不要であることを証明した——必要なのは仕様のみである。」

---
