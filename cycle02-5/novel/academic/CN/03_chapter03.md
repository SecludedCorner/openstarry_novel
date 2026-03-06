# 第三章：三面之镜——D2 Sati Plugin 蕴归属辩论

---

**时长**：~60 分钟 | **主席**：SUNYATA | **投票**：3 项

## 更名策略（D2-R1：19/20）

保留 `Sati` 代码标识符，文件标题从「Mindfulness Architecture」改为「Cognitive Loop Quality Monitoring Architecture」。加入「命名说明」段落。安全文件使用全名。

唯一反对票：GUARDIAN——偏好完全更名以消除文化背景知识需求。接受多数决议附带安全文件全名条件。

## 五蕴组成（D2-R2：18/20）——核心决议

**结论：skandha: ['vedana', 'samjna', 'vijnana']**

四个功能到三蕴的映射：

| 功能 | Skandha | 说明 |
|------|---------|------|
| EventBus 事件订阅（11 种，持续感知） | vedana | 接收认知回路信号 |
| 滑动窗口 + 模式辨认 | samjna | 从事件流中辨认行为模式 |
| LoopQualityVector + SPC 异常判断 | vijnana | 超越描述性辨认的评价性品质判断 |
| **不执行工具、不修改状态** | **排除 samskara** | 不是正念修行 |

关键论证转折：

- **ASANGA**：佛学正念（smṛti）是行蕴心所——主动的、有意志的、道德正向的。SatiMonitor 是被动的、自动的、价值中立的。因此 SatiMonitor 不是正念，不应归为行蕴。
- **LINNAEUS**：OOP 比较——「IGearArbiter 是『被调用来看一下』；SatiMonitor 是『一直在看』。」持续订阅 vs 按需调用——足以构成独立的 vedana 声明。
- **ARCHIMEDES**（转折点）：三蕴和二蕴的工程成本差异为零——PluginManifest 的 skandha 栏位已支持多值。消除「三蕴太复杂」的顾虑后，讨论转为纯分类精度，Proposal B 的优势压倒性。
- **少数意见**（MESH、KERNEL）：Proposal C ['samjna','vijnana'] 与 IGearArbiter 分类对称，有长期维护价值。

**历史意义**：SatiMonitor 成为 OpenStarry 第一个三蕴 plugin。

## PluginHooks 专属槽位（D2-R3：20/20）

新增 `monitors?: ISatiMonitor[]` 专属槽位。遵循 Cycle 02-4 的 `arbiters` 先例（SDK 接口 → PluginHooks → Registry → PluginLoader 四步模式）。

---
