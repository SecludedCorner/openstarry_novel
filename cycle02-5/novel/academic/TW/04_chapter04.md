# 第四章：完備性——D3 五蘊 OOP 架構辯論

---

**時長**：~120 分鐘 | **主席**：SUNYATA | **投票**：6 項

## 五根介面充分性（D3-R1：20/20）

四個獨立論證收斂至同一結論：IRupa、IVedana、ISamjna、ISamskara、IVijnana 五個根介面足以覆蓋所有功能需求。

- **LINNAEUS**：100% 功能覆蓋率驗證。
- **BABBAGE**：型別代數完備性定理（Q.E.D.）。
- **ASANGA**：阿毘達磨窮舉分類公理。
- **KERNEL**：五個微核心子系統映射（I/O、感測、計算、執行、排程）。

PENROSE 附帶建議：監控 vijnana 子介面數量（目前 4，未來 6；超過 10 時考慮拆分）。

## PluginHooks 映射正確性（D3-R2：20/20）

TURING 逐行原始碼驗證，九項映射全部正確。

焦點討論：SlashCommand 不屬於任何蘊——因為它繞過整個 ExecutionLoop（類比：Unix 信號處理器）。GUARDIAN 安全觀察：SlashCommand 繞過 SafetyMonitor，如果 plugin 通過此路徑執行危險操作，五蘊安全機制全部無效。此觀察記入 Doc 45。

## skandha 作為元數據（D3-R3：18/20）

維持現狀——skandha 是元數據，不是路由基礎。型別路由已完備。少數意見（GUARDIAN、LINNAEUS）：即使只是 warning 的一致性驗證也有審計價值。

## ISamskara 子介面（D3-R4：20/20）

維持 ITool 為唯一子介面。ASANGA 坦承：這是五蘊架構中佛學自洽性最弱的部分——傳統行蘊涵蓋 49 心所，OpenStarry 窄化為外部行為（ITool）。HERACLITUS 的動態論證：IVolition 在 Phase 5，ITool 在 Phase 6——將 IVolition 移至行蘊會造成「行蘊在行蘊之前」的概念錯位。

DC-6「行蘊保持開放，不鎖定」繼續有效。

## 十二因緣（D3-R5：13/20 Proposal C）

最具爭議的 D3 投票。Proposal C（選擇性附錄映射）勝出。

- **NAGARJUNA**：尺度不匹配——十二因緣描述三世因果（宏觀），ExecutionLoop 描述單次認知處理（毫秒級）。
- **BABBAGE**（投 B）：十二因緣是線性鏈，ExecutionLoop 是有迴圈的 FSM——圖結構根本不同。
- Proposal B（不映射）獲 7 票——D3 最大的少數意見群。

## 認知序列（D3-R6：17/20 Proposal C）

比十二因緣獲得更高共識——因為描述的是相同尺度現象（單一認知活動的內部階段）。HERACLITUS 提供了八狀態對比表，五個「高」或「中高」平行。

BABBAGE 從 B（十二因緣）轉為 C（認知序列）——FSM 態射分析是轉向的關鍵論據。十二因緣沒有態射。認知序列有。

PENROSE 理論貢獻：認知迴路的結構趨同是功能需求的必然結果，不是刻意模仿。

## 架構評估結論

**v0.28.0-alpha 的五蘊 OOP 架構在結構層面是充分的。** 三個已知缺口（弱繼承、VedanaAssessment 佈線未完成、IConfidenceAuditor/ILoopQualityMonitor 尚未實作）都是計畫中的增量改進。

---
