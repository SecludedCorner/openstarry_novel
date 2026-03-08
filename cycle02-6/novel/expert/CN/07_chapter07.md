# 第七章：Plan30 工程蓝图与前瞻

---

## 7.1 Plan30 定义

**Plan30 = Default LoopQualityMonitor Plugin + Layer 3 Integration**

决策基础：D3-R5（19/20 + 1 条件赞成）。前置条件：Plan29 DONE + OQ-29-1/2/4/5 已回答。

---

## 7.2 四个 Wave

### Wave 1：Default Monitor Plugin（约 120 LOC）

核心品质计算引擎，使用 B1 四维公式 + B2 六事件订阅模型。

```typescript
// 概念性接口（非最终实现）
export class DefaultLoopQualityMonitor implements ILoopQualityMonitor {
  private readonly window: SlidingWindow;      // W=10
  private readonly warmupThreshold = 5;
  private tickCount = 0;

  // circular buffers
  private gearHistory: number[] = [];          // coherence + convergence
  private proposedCount = 0;                   // efficiency 分母
  private successCount = 0;                    // efficiency 分子
  private welfordState: WelfordState;          // stability

  constructor(private readonly bus: EventBus) {
    // Phase 1: 订阅 6 个事件
    bus.on('gear:arbiter_evaluated', this.onArbiterEvaluated);
    bus.on('gear:switch', this.onGearSwitch);
    bus.on('action:proposed', this.onActionProposed);
    bus.on('tool:result', this.onToolResult);
    bus.on('loop:started', this.onLoopStarted);
    bus.on('loop:finished', this.onLoopFinished);
  }

  report(): LoopQualityReport {
    if (this.tickCount < this.warmupThreshold) {
      return { vector: WARMUP_VECTOR, composite: 0.5, timestamp: Date.now() };
    }
    const vector = {
      coherence:   this.computeCoherence(),
      efficiency:  this.computeEfficiency(),
      convergence: this.computeConvergence(),
      stability:   this.computeStability(),
    };
    const composite = 0.25 * (vector.coherence + vector.efficiency
                             + vector.convergence + vector.stability);
    return { vector, composite: Math.max(0, Math.min(1, composite)), timestamp: Date.now() };
  }
}
```

所有维度 O(1) per event，O(W) 空间。

### Wave 2：Layer 3 ManoAggregator Integration（约 80 LOC）

Option C 布线。核心修改在 `mano-aggregator.ts`：

1. `createManoAggregator` 新增 `loopQualityFn?: () => number` 参数
2. `ManoAggregatorConfig` 新增 `loopQualityAlpha`、`monitorStalenessMs`、`historicalConfidenceSize`
3. arbiter 回路中插入 L3 阈值调整
4. 历史信心度环形缓冲区（C-1 约束：仅记录原始值）

```typescript
// L3 阈值调整核心逻辑
const alpha = config.loopQualityAlpha ?? 0.10;
const q = loopQualityFn ? loopQualityFn() : 0;
const adjustedThreshold = Math.max(
  config.thresholdFloor,
  threshold * (1 - alpha * q),
);
```

### Wave 3：Events + Extras + Types（约 60 LOC）

- `AgentEventType` 常量提升：7 个新常量（6 个 Plan27b 既有 + `LOOP_QUALITY_UPDATED`）
- `ConfidenceAuditLog` SDK 类型定义（GUARDIAN D3-R5 条件）
- `audit:context_contribute` 事件定义
- `MINIMAL_QUALITY_EVENTS` 常量（Phase 1 = 6 events）
- `emitWithExtras()` SDK 便利函数

### Wave 4（可选）：PassthroughAuditor（约 30 LOC）

```typescript
export class PassthroughAuditor implements IConfidenceAuditor {
  readonly id = 'passthrough-auditor';

  async audit(context: AuditContext): Promise<ConfidenceAuditResult> {
    // Phase 0: delta=0, pure logging
    return {
      delta: 0,
      reasoning: `Passthrough: confidence=${context.routeResult.confidence}, ` +
                 `gear=${context.routeResult.gear}`,
    };
  }
}
```

用途：端对端管道验证 + 整合测试 fixture + Phase 1 ThresholdAuditor 的 scaffold。

---

## 7.3 范围摘要

| 指标 | 估计 |
|------|------|
| 生产代码 | 约 260-290 LOC |
| 测试代码 | 约 130 LOC |
| 总计 | 约 390-420 LOC |

---

## 7.4 成功标准

**Model Delta L0-L4 全部有实际信号路径**——每一层从 L0（EventBus 事件流）到 L4（audit 输出）都不再是空壳，必须有真正的代码在运作，以整合测试验证。

具体而言：
- L0：EventBus 事件被 Monitor 订阅并处理
- L1：Klesha 增益影响 baseThreshold（已存在）
- L2：Audit delta 调整 confidence（Plan29 已布线；Plan30 W4 提供 PassthroughAuditor）
- L3：LoopQuality 调整 threshold（Plan30 W2 新增）
- L4：VedanaEmergency boost（已存在）

---

## 7.5 WIENER 约束的工程实施

所有 Wave 必须遵守三条硬约束：

| 约束 | 实施位置 | 验证方式 |
|------|---------|---------|
| C-1：historicalConfidence 仅含原始值 | W2: 环形缓冲区 push | 单元测试：audit 后的值不出现在 history 中 |
| C-2：AuditContext 不含前次 audit 结果 | W3: AuditContext 类型定义 | 类型检查：接口中无 previousAuditResult 字段 |
| C-3：extras 禁止 `audit:` 前缀 | W3: emitWithExtras 验证 | 单元测试：含禁止前缀的写入被拒绝 |

---

## 7.6 Plan31 预览

Plan31 将把 AuditContext 落地到运行路径中——从类型定义进入实际组装：

| 项目 | 估计 LOC | 描述 |
|------|---------|------|
| AuditContext 组装 | ~120 | Core 在 route() 中组装完整 AuditContext |
| Default ThresholdAuditor | ~120 | Phase 1 规则式审计：低信心度侦测、loopQuality 异常、趋势侦测 |
| Audit Trail JSONL | ~110 | 持久化层：ConfidenceAuditLog → JSONL file appender |
| **总计** | **~350** | |

Plan30 造管道（类型 + 计算 + 布线）。Plan31 让水流过管道（组装 + 审计 + 持久化）。

---

## 7.7 Plan32+ 长期路线图

```
Plan30 (本轮)      → Default LoopQualityMonitor + Layer 3 Integration
Plan31 (下轮)      → AuditContext 落地 + Default Auditor + Audit Trail
Plan32 (未来)      → VasanaEngine / SPC / Lyapunov stability
```

Cycle 02-7 的 P1 待研究项目：

1. **Lyapunov 稳定性参数校准**：alpha 值验证、稳态分析、五层模型的严格稳定性证明
2. **Moha/Sneha 耦合模拟**：Klesha 模块（L1）之间的交互作用是否影响 L3 行为
3. **多 monitor 聚合策略验证**：简单平均 vs 悲观策略的经验数据比较

Cycle 03+ 的延后项目：

- **八识深化**（alaya-vijnana）：多 Agent 场景下的共享记忆机制
- **VasanaEngine**（D-29-8）：行为模式的学习与记忆，对应行蕴「造作一切有为法」
- **ISamskara 方向 A/B**：意图规划（cetana-formation）+ 习气形成（vasana-imprinting）

---

## 7.8 研究成果总结

### 九项成功标准达成

| # | 标准 | 状态 | 决议 |
|---|------|------|------|
| 1 | AuditContext 完整类型定义 | 达成 | D2-R1 |
| 2 | 审计日志格式规格（GUARDIAN D5） | 达成 | D2-R3 |
| 3 | LoopQualityVector 4D 公式 | 达成 | D3-R1 |
| 4 | EventBus 事件订阅清单 | 达成 | D3-R2 |
| 5 | OQ-29 全部回答 | 达成 | 5/5 |
| 6 | Plan30 方向建议 | 达成 | D3-R5 |
| 7 | 行蕴深掘报告 | 达成 | C1-C4 + D1 |
| 8 | 心所逐条蕴归属建议 | 达成 | C2（51 项） |
| 9 | 无范围蔓延 | 达成 | Lyapunov/Moha/FC-26 未讨论 |

### 两大永久性产出

1. **蕴归属五原则 + 行蕴三准则**：未来所有蕴归属判定的基准线
2. **心所八点规则**：未来所有命名和佛学概念引用的判定基准线

这两组规则不是单轮决议——它们是跨越所有未来 Cycle 的永久性框架。

### 工程与哲学的汇合

Cycle 02-5 是减法（清除装饰性映射）。Cycle 02-6 是加法（建立精确规格）。

哲学轨建立了行蕴的原典定义（cetana 中心、造作功能、无核心过程），工程轨据此产出了完整的接口规格（AuditContext、LoopQualityVector、Option C 双通道、五层公式）。两轨在蕴归属五原则和 WRITE/READ 区分上汇合——哲学判定提供了工程设计的语义基础，工程设计验证了哲学判定的可操作性。

Plan30 大约 290 行生产代码。不多。但这 290 行的每一行都有 17 项决议、14 份研究报告、三轮 Master 指示作为依据。

二十位研究者。十七项决议。零项否决。

---

*Cycle 02-6 完。*
