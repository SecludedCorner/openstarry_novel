# 第六章：纯粹的工程——D5 Plan29 工程规格辩论

---

**时长**：~75 分钟 | **参与者**：10 人 | **投票**：9 项

D5 是本专案历史上第一场完全没有佛学内容的辩论。十位工程师和科学家，零位佛学家（NAGARJUNA 和 ASANGA 自愿退出），讨论 TypeScript 接口的精确规格。

TURING 预提交了完整的 v0.28.0-alpha 设计模式报告——14 个源代码文件、所有 Registry 生命周期、timeout 模式、同步/异步模式、失败处理策略。这份「代码考古学」报告为所有决策提供了事实基础。

## 九项决议

| 决议 | 内容 | 票数 |
|------|------|------|
| D5-R1 | 独立 `auditor` hook 槽位（不复用 monitors） | 8/8 |
| D5-R2 | audit() 双模式回传 `T \| Promise<T>` | **5/8** |
| D5-R3 | timeout 200ms，fail-safe delta=0，可配置 | 8/8 |
| D5-R4 | 单一 auditor，last-wins（非数组） | 6/8 |
| D5-R5 | 失败处理：delta=0 + warning log | 共识 |
| D5-R6 | MonitorRegistry 在 ExecutionLoop.onLoopStart() 启动 | 7/8 |
| D5-R7 | LoopQualityVector 等权重 0.25×4 | 8/8 |
| D5-R8 | validatePluginSkandha() 维持 warning-only | 7/8 |
| D5-R9 | IConfidenceAuditor extends IVijnana，skandha ['vijnana'] | 8/8 |

**最激烈投票**：D5-R2（5/8）——纯异步 vs 双模式。GUARDIAN/KERNEL/VITRUVIUS 主张纯异步语义更精确；多数采双模式，遵循 IGearArbiter 先例和测试便利性。

## IConfidenceAuditor 最终规格（100%）

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

PluginHooks 最终形态：
```typescript
interface PluginHooks {
  // ... 既有栏位 ...
  monitors?: ILoopQualityMonitor[];   // Plan29 Wave 1
  auditor?: IConfidenceAuditor;       // Plan29 Wave 2
}
```

NAGARJUNA 在 D5 结束后的评语：「D4 证明了名字需要对定义负责。D5 证明了有些工程问题根本不需要定义——只需要规格。」

---
