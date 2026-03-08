# 第二章：审计上下文的类型设计 —— 信息充分性与反馈回路切断

---

## 2.1 问题分析：IConfidenceAuditor 的信息贫乏

Plan29 交付的 `IConfidenceAuditor` 接口存在结构性缺陷：审计函数的输入仅包含 `RouteResult`（路由结果）。审计员无法获取触发事件（sparshEvent）、仲裁器推理过程（gearEvaluation）、风险等级（riskCategory）或历史信心度序列。以决策理论术语而言，这是一个信息不对称（information asymmetry）问题。DC Master 明确指示审计员需要更多信息。

然而，扩充审计员可见信息的同时引入了控制理论风险：**正反馈回路**（positive feedback loop）。

---

## 2.2 正反馈回路的威胁模型

WIENER（#12）识别出三条潜在的正反馈路径：

1. **historicalConfidence 污染**：若历史序列包含审计后调整值，形成 `audit → confidence → history → audit` 闭合回路
2. **审计结果泄漏**：若 AuditContext 包含前次审计结果，形成确认偏误驱动的序列相关
3. **extras 后门**：若 extras bag 允许写入审计相关键值对，间接泄漏历史输出

三条路径均可导致 BIBO 不稳定：信心度值在迭代中单调增长或振荡发散。

---

## 2.3 AuditContext 类型定义 [D2-R1, 20/20]

```typescript
export interface AuditContext {
  readonly version: 1;                              // 字面量类型
  readonly sparshEvent: SparshEvent;                // 触发事件（必填）
  readonly gearEvaluation: GearEvaluation;          // 仲裁器完整推理过程
  readonly riskCategory: RiskCategory | undefined;  // 风险类别（可选）
  readonly routeResult: RouteResult;                // 审计前路由结果快照
  readonly historicalConfidence?: readonly number[]; // 环形缓冲区，预设 10
  readonly extras: ReadonlyMap<string, unknown>;     // 泛型扩展袋
}
```

核心字段由 Core 组装；historicalConfidence 为可选环形缓冲区；extras 为 ReadonlyMap，通过 `getExtra<T>(extras, key, guard)` 类型安全存取器读取。

---

## 2.4 WIENER 三约束

**C-1（历史纯净性）**：historicalConfidence 仅记录仲裁器原始信心度 $c_t^{raw}$，不含审计后调整值。

**C-2（审计结果隔离）**：AuditContext 不包含前次 ConfidenceAuditLog。每次审计信息独立。

**C-3（extras 前缀禁令）**：禁止 `audit:`、`core:`、`internal:` 前缀，防止审计结果通过 extras 泄漏。

三约束确保审计员的**因果隔离**（causal isolation）。BABBAGE（#9）的形式化验证：审计函数 $f: \mathcal{C} \times \mathcal{A} \to [-0.05, +0.05]$ 在三约束下，输入不含自身先前输出，调整量受限幅约束，信心度值域 $[0,1]$ 自然有界，系统满足 BIBO 稳定。

---

## 2.5 extras bag 协议 [D2-R2, 19/20]

| 方面 | 规格 |
|------|------|
| 写入模式 | 双事件 + SDK `emitWithExtras()` |
| 收集管道 | ManoAggregator 订阅 `audit:context_contribute` |
| 读取接口 | `getExtra<T>(extras, key, guard)` |
| 不可变性 | 浅冻结 + ReadonlyMap |
| 限制 | max 32 keys, 128 chars/key |
| 键命名 | `{category}:{name}` 格式 |

一票反对认为双事件模式增加不必要复杂性，多数认为其通用性（任何 Plugin 均可通过相同协议贡献信息）证成了设计。

---

## 2.6 ConfidenceAuditLog [D2-R3, 20/20]

完整审计轨迹类型：inputConfidence, rawDelta, clampedDelta, wasClamped, reasoning（截断 500 字符）, outputConfidence, result, auditDurationMs。主通道为 EventBus `audit:completed` 事件；JSONL 持久化排程至 Plan31。

GUARDIAN（#11）在此决议通过后正式声明："D5 的让步条件已兑现。我不再保留重新审议 $\pm 0.05$ 限幅的权利。"此声明终结了自 Cycle 02-4 以来围绕信心度调整安全性的持续争议。

---
