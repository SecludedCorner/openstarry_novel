# 第六章：三场辩论——从分歧到共识的精确路径

---

## 6.1 R2 分歧识别

R2 交叉审阅识别了 24 个共识点和 3 个分歧点。四组跨轨道交叉对照全部确认无冲突——哲学轨的结论不影响工程轨的任何设计假设：

| 对照 | 结果 |
|------|------|
| C2 心所批判 → A1 AuditContext | 4/4 无影响 |
| C4 工程借鉴 → D2 Plan30 | 4/4 无影响 |
| C3 ISamskara 拓展 → B1 公式 | 5/5 无影响 |
| C2 心所批判 → 蕴归属清单 | 11 确认 / 0 修正 / 1 待辩 / 14 未来 |

三项分歧全部属于工程轨内部：

1. **extras 写入协议**：A2 提出通用事件模式 vs B3 提出直接订阅 → D2 解决
2. **extras key 命名**：`loopQuality:score` vs `loopQuality:composite` → D2 统一为 `loopQuality:composite`
3. **loopQualityFn 数据来源**：L3 回调 vs extras 缓存是否同源 → D3 解决（双通道：pull + push）

---

## 6.2 D1：行蕴深掘（约 75 分钟，7 项决议）

| 决议 | 内容 | 票数 | 关键论点 |
|------|------|------|---------|
| D1-R1 | 行蕴核心定义：cetana 中心、造作功能、无核心过程 | 20/20 | 直接引用 SN 22.56/79/95，无模糊空间 |
| D1-R3 | ISamskara 不新增子接口；三准则为永久工具 | 20/20 | 确认 02-5 D3-R4，A/B 方向存档 |
| D1-R4a | 认知序列 appendix 排程 02-7 P2 | 19/20 | 1 票反对认为可在本轮完成 |
| D1-R4b | 四智正式排除 | 18/20 | 2 票反对认为可保留参考；四项测试全失败 |
| D1-R4c | C4 综合评估表确认 | 20/20 | -- |
| D1-R5 | 「活动与转换」原则；行=WRITE 识=READ | 20/20 | PENROSE 的 WRITE/READ 区分 |
| D1-R6 | 蕴归属 5 项永久性原则 | 20/20 | 永久基准线，非单轮决议 |

D1 是三场辩论中共识最高的——5 项全票。原因在于哲学轨的结论直接基于原始经典引用，不涉及工程取舍（trade-off）的判断，因此分歧空间极小。

D1 结论对 D2/D3 均无需追加议题——跨轨道影响协议中的「先哲学后工程」规则在此轮验证为零冲突。

---

## 6.3 D2：AuditContext（约 85 分钟，5 项决议）

| 决议 | 内容 | 票数 | 关键论点 |
|------|------|------|---------|
| D2-R1 | AuditContext 完整类型（sparshEvent required, history 预设 10 可配置） | 20/20 | A1-OQ1/2/3 全部解决 |
| D2-R2 | extras bag 协议（双事件 + SDK helper, 浅冻结, max 32 keys） | 19/20 | MESH 反对双事件复杂度；多数支持通用性 |
| D2-R3 | ConfidenceAuditLog（GUARDIAN D5 义务兑现） | 20/20 | GUARDIAN 当场确认清账 |
| D2-R4 | Layer 整合方案 C（L2→confidence, L3→threshold, alpha=0.10） | 20/20 | WIENER/BABBAGE 稳定性分析决定性 |
| D2-R5 | Auditor 策略三阶段：Phase 0 PassthroughAuditor | 20/20 | -- |

D2-R4 的投票过程值得注意：WIENER 和 BABBAGE 的稳定性分析（Option A/B/C 的 Lyapunov 比较）在 R1 报告中已呈现。R2 交叉审阅时无人对分析提出质疑。到了 D2 辩论，全票通过——数学证明的说服力是确定性的。

R2 的三项分歧在 D2 中全部解决：
- extras 写入 → 统一为双事件 + SDK helper（D2-R2）
- key 命名 → 统一为 `loopQuality:composite`（D2-R2 附带决议）
- loopQualityFn 数据来源 → 移至 D3 处理

---

## 6.4 D3：LoopQualityMonitor（约 85 分钟，5 项决议）

| 决议 | 内容 | 票数 | 关键论点 |
|------|------|------|---------|
| D3-R1 | 4 维公式确认（C/E/Conv/S; W=10, warmup=5, Q_default=0.5） | 20/20 | OQ-29-1 正式回答 |
| D3-R2 | EventBus 订阅：6 events Phase 1; AgentEventType 常量提升 | 20/20 | OQ-29-4 正式回答 |
| D3-R3 | extras 写入：D2-R2 管道 + loopQualityFn 双通道; per-route lifecycle | 20/20 | 解决 R2 第三项分歧 |
| D3-R4 | 权重 Phase 1 固定 balanced 0.25x4 | 20/20 | PASCAL 最大熵论证 |
| D3-R5 | Plan30 = Monitor + L3 + 类型定义; Plan31 = Auditor + Audit Trail | 19+1 条件 | GUARDIAN 条件赞成 |

D3-R5 是唯一一项有条件赞成的决议。GUARDIAN 的条件：**Plan30 的 Wave 3 必须包含 `ConfidenceAuditLog` 的 SDK 类型定义，不能拖到 Plan31。** 理由：日志类型是 D5 让步条件的核心交付物，延迟等于债务延期。条件被接纳，GUARDIAN 转为赞成。

---

## 6.5 Auditor 策略三阶段 [D2-R5, 20/20]

| Phase | 对应 Plan | 实现 | 描述 |
|-------|----------|------|------|
| Phase 0 | Plan30（W4, 可选） | PassthroughAuditor | delta=0, 纯日志；验证管道端对端通畅 |
| Phase 1 | Plan31 | ThresholdAuditor | 规则式：低信心度侦测、loopQuality 异常、趋势侦测 |
| Phase 2 | 长期 | LLM-assisted | LLM 辅助审计 |

Phase 0 的 PassthroughAuditor 看似无用——一个什么都不调整的审计员。但 ARCHIMEDES 的工程洞见：「它的价值不在审计，在测试。它验证 AuditContext 组装、extras 收集、audit delta clamping、ConfidenceAuditLog 发出——整个管道端对端通畅。就像装好水管后先开水龙头。」

所有 Phase 必须遵守 WIENER C-1/C-2/C-3 约束——这不是 Phase 0 的特殊要求，而是永久性约束。

---

## 6.6 统计比较

| 指标 | Cycle 02-5 | Cycle 02-6 |
|------|-----------|-----------|
| 决议数 | 29 | 17 |
| 否决 | 0 | 0 |
| 全票（20/20） | ~20（69%） | 13（76%） |
| 师父覆议 | 2 | 0 |
| 辩论场次 | 5 | 3 |
| R1 报告数 | -- | 14 |
| R2 共识点 | -- | 24 |
| R2 分歧点 | -- | 3 |

DARWIN 的观察：「02-5 是正确性辩论——什么是对的、什么是错的。02-6 是规格辩论——对的东西长什么样子。后者天然更容易达成共识，因为不涉及价值判断。」

SUNYATA 的分析：「R1 做得好。14 份报告覆盖了所有问题空间。R2 只发现 3 个分歧。当大部分问题在辩论前就有共识，辩论就变成了确认和精化。」

零师父覆议的原因：八点规则在 R2 阶段就已确立（Master 三轮精化），D1-D3 的所有决议都在八点规则的框架内运作。没有决议试图挑战框架本身。
