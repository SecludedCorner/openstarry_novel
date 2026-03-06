# 第五章：名字的代价——D4 命名修正辩论

---

**时长**：~30 分钟 | **触发**：Master 审阅 | **投票**：3 项

D4 不在原始议程中。它由 Master 的一句话触发：

> **「用梵文就需要对他的定义负责。你觉得 Sati 的内容完全 match 吗？」**

## NAGARJUNA 的归谬论证

```
前提 A：Sati = 行蕴心所（佛学定义）
前提 B：SatiMonitor ≠ 行蕴（D2-R2 结论）
∴ SatiMonitor ≠ Sati
```

如果正念在佛学中必然是行蕴，而 D2 已经证明 SatiMonitor 不是行蕴——那 SatiMonitor 就不是正念。一个不是正念的元件，不应该叫 Sati。

ASANGA 确认：「如果 SatiMonitor 不是行蕴活动，那它就不是 Sati。我们自己的分类分析否定了我们自己的命名。」

## ISatiMonitor → ILoopQualityMonitor（D4-R1：13/20）

ARCHIMEDES 的提案胜出：「Loop Quality Monitor」——认知回路的品质监控器——精确描述功能，无佛学，无隐喻。

少数意见：IBehaviorQualityMonitor（GUARDIAN，4 票）、ICognitiveLoopMonitor（NAGARJUNA + ASANGA，2 票）、IQualityMonitor（SYNTHESIST，1 票）。

完整更名表：ISatiMonitor → ILoopQualityMonitor、SatiQualityVector → LoopQualityVector 等 8 项。

## IPrajna → IConfidenceAuditor（D4-R2：16/20）

NAGARJUNA：「般若是佛学中最高的认知能力——照见一切法实相的智慧。」

ASANGA：「把一个温度微调旋钮叫做核融合反应炉。」

IPrajna 的实际功能：一个方法，输入信心度，输出 `{ delta: number, reasoning: string }`，delta 限制在 [-0.05, +0.05]。这是审计——不是般若。

BABBAGE：IConfidenceAuditor 语义最精确——独立的、有限范围的、产生书面记录的二次检查。

少数意见：IThresholdCalibrator（WIENER，2 票）、ISecondaryEvaluator（HERACLITUS + PENROSE，2 票）。

## Doc 03 重新投票（D4-R3：17/20）

「Sila-Prajna Security Framework」→「Plugin Security Lifecycle」

初始投票 14/20 保留不变。Master 审阅触发重新检验——四项测试全部不通过：必要性（不需要种子理论理解 plugin 生命周期）、代码识别（实际类型用英文）、决策驱动（无 DC 确认）、定义责任（戒 ≠ 访问控制，般若 ≠ CVE 撤销）。

ASANGA 的关键区分：Doc 16 = 独立映射文件（Master 裁定保留）vs Doc 03 = 工程文件中的佛学装饰（应清理）。

## 第四项测试——定义责任（永久性标准）

> **「当使用佛学梵文术语作为代码标识符时，该组件的功能必须匹配该术语的佛学定义。如果不一致，使用工程术语。」**

补充 D1 的三项测试——即使名字通过 Test 2（代码识别），如果不通过 Test 4（定义责任），仍应更名。

影响范围：ILoopQualityMonitor 影响 6 份文件 100+ 处替换；IConfidenceAuditor 影响 5 份文件；Doc 03 重命名 + 内容清理。

---
