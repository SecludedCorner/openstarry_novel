# 第六章：D5——纯粹的工程

---

## 十位辩论者

D5 只有十位参与者。

不是排除——是精选。SUNYATA 判断 D5 是纯工程问题，邀请了与 Plan29 最相关的十位：VITRUVIUS（接口设计）、ATHENA（LLM 语义）、DARWIN（设计模式）、KERNEL（Registry 生命周期）、GUARDIAN（安全边界）、WIENER（品质向量权重）、LINNAEUS（蕴归属推断）、ARCHIMEDES（工程实践）、TURING（原始码分析）、PASCAL（接口语义精度）。

十个人。零位佛学家。

NAGARJUNA 和 ASANGA 自愿退出。NAGARJUNA 的临别语：「D4 证明了名字需要对定义负责。D5 会证明工程设计不需要佛学名字也能完成。这两件事同样重要。」

---

## 程序码考古学

TURING 为 D5 准备了一份前所未有的报告——对 v0.28.0-alpha 中 14 个原始码文件的全面分析。所有 Registry 的生命周期、timeout 模式、同步/异步模式、失败处理策略。

他把它叫做「程序码考古学」。

这份报告改变了辩论的质地。之前的辩论——D1 到 D4——建立在原则和框架之上。但 TURING 的报告建立在事实之上。事实缩小了分歧的空间。你可以对一个原则有不同的解读。你不能对一个 timeout 数值有不同的解读。

---

## 九项投票

D5 是 Cycle 02-5 中投票最多的辩论——九项。但也是最快的——七十五分钟，平均每项不到九分钟。

**D5-R1：独立 auditor slot。** IConfidenceAuditor 是否和 monitors 共用槽位？GUARDIAN 的论点：Monitors 是纯观察者（无副作用），Auditor 有 LLM 副作用。把观察者和有副作用的组件放同一个 Registry，模糊安全边界。**8/8。**

**D5-R2：audit() 返回类型。** D5 最接近的投票。纯异步 vs 双模式（`ConfidenceAuditResult | Promise<ConfidenceAuditResult>`）。GUARDIAN/KERNEL/VITRUVIUS 支持纯异步（语义精确），ATHENA/DARWIN 支持双模式（遵循 IGearArbiter 先例）。TURING 提供事实：v0.28.0-alpha 中 IGearArbiter 和 IVolition 都使用双模式——偏离现有模式需要充分理由。**5/8 双模式通过。** 一致性胜过语义精确性。

**D5-R3：timeout 200ms + fail-safe。** TURING 分析了现有 timeout 模式——IGearArbiter chain deadline 200ms。audit() 应匹配。timeout 时 `{ delta: 0 }`——不修正。**8/8。**

**D5-R4：单一 auditor（last-wins）。** 多个 IConfidenceAuditor 的处理方式？ATHENA 提出 YAGNI：v1 最多一个。ARCHIMEDES 支持：遵循 IVolition 先例——单数，最后载入者胜出。**6/8。** TURING 和 VITRUVIUS 的少数意见（阵列更灵活）被记录。

**D5-R5：失败处理。** 异常时 fail-safe + log。遵循 IGearArbiter 和 SafetyMonitor 的现有模式。共识直接达成，不需投票。

**D5-R6：MonitorRegistry 启动时机。** `MonitorRegistry.startAll(bus)` 在 `ExecutionLoop.onLoopStart()` 启动。遵循 SafetyMonitor 的先例。**7/8。**

**D5-R7：LoopQualityVector 均等权重。** 四维品质向量（Continuity, Granularity, Speed, Equanimity），每个 0.25。WIENER 从控制理论角度：「没有运行数据时，等权重是最保守的选择。」**8/8。**

**D5-R8：validatePluginSkandha() 维持 warning-only。** skandha 是 metadata（D3-R3），宣告不一致不影响功能。**7/8。**

**D5-R9：IConfidenceAuditor extends IVijnana。** 单蕴（vijnana），强继承。与 IVolition 和 IKlesha 一致。**8/8。**

---

## 接口定稿

九项投票完成后，TURING 在白板上写下了最终规格：

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

「100%，」他说。

Master 要求的是规格达到 100%。现在达到了。每一个需要决定的细节都有了明确答案——接口名称、方法签名、返回类型、timeout、fail-safe、多 auditor 策略、Registry 时机、权重、验证模式、蕴归属。

不是概念设计。是可以直接交给工程团队实作的完整规格。

---

## 零佛学

SCRIBE 统计了 D5 全场辩论中佛学术语被使用的次数。

零。

不是故意避开——是自然的结果。九项投票的每一项都在讨论 TypeScript 接口设计、timeout 数值、Registry 模式、fail-safe 策略。没有一项需要佛学分析。

D5 是本项目历史上第一场完全没有佛学内容的辩论。

NAGARJUNA 在辩论结束后走到 TURING 面前：「D4 证明了名字需要对定义负责。D5 证明了——有些工程问题根本不需要定义。只需要规格。」

天平的两面。一面问：名字配得上定义吗？另一面问：规格足够精确吗？D4 校准了第一面。D5 完成了第二面。

---
