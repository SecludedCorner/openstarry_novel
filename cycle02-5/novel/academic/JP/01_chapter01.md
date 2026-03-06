# 第一章：監査と研究

---

## R1：独立研究

九件の独立研究報告が R1 段階で産出された。三つのトラックが並行して推進された。

### Track A：五蘊工学アーキテクチャ

**A1（LINNAEUS + ASANGA）**：五蘊サブカテゴリツリー。完全な OOP インターフェース継承分析——IRupa は IListener と IUI に分かれ、IVedana は ChannelVedana（連続信号）を生成し、ISamjna は IProvider に対応し、ISamskara は ITool に狭化され、IVijnana が最も複雑で、IGuide、IGearArbiter、IVolition、IKlesha の四つのサブインターフェースを管轄する。三つの「弱い継承」ケースが記録された——IVedanaSensor、IGearArbiter、IKlesha はルートインターフェースを明示的に extends しない。

**A2（VITRUVIUS + KERNEL + TURING）**：DI 配線。Pure DI、`createAgentCore()` が唯一の Composition Root、21 個のコンポーネントが厳密に線形構築、9 個の Registry。Lazy Accessor パターン、Provider 能力フィルタリング、Resolver クロージャ遅延解決。Spring/Guice/InversifyJS との比較マトリクスにより、Pure DI がマイクロカーネルにとって正しい選択であることが確認された。

**A3（DARWIN + MESH）**：Plugin 読み込みライフサイクル。IPlugin = Manifest + Factory。二つの読み込みパス（Sandbox worker thread / Direct main thread）。八状態ライフサイクルステートマシン。Sandbox セキュリティチェーン：署名検証 → 静的 import 分析 → Worker 隔離 → Heartbeat → 指数バックオフ再起動。

**A4（HERACLITUS + WIENER + BABBAGE）**：五蘊実行フロー。FSM 六状態、九段階処理。Phase 1（rupa）→ Phase 3（samjna）→ Phase 5（vijnana）→ Phase 6（samskara）→ Phase 7（vedana）→ Phase 8（vijnana）。三層安定ループ。BABBAGE が完全な FSM 形式仕様を提供した。

**A5（LEIBNIZ + ATHENA + PENROSE）**：蘊間相互作用。5×5 相互作用マトリクス。Model Delta 五層閾値公式。PENROSE が三つの創発パターン仮説を提出した——適応的保守、双安定スイッチング、注意の漏斗。

### Track B：仏教マッピング監査

**B1（ARCHIMEDES + SCRIBE）**：7 件の文書を逐行監査。50 個のマッピング事例——23 個が KEEP（46%）、13 個が RELOCATE（26%）、14 個が REMOVE（28%）。Doc 43 の装飾比率が最も高かった（60%）。Doc 16 と Doc 31 が「ファイル全体審査」として標識された（装飾比率 80% および 70%）。

**B2（NAGARJUNA + ASANGA + PASCAL）**：マッピング境界原則。NAGARJUNA の二諦分離、ASANGA の機能位置づけ、PASCAL の損害非対称性（false include の累積認知負荷 >> RELOCATE の一回限りの検索コスト）。三項テストが本文書で正式に論証された。

### Track C：Sati Plugin

**C1（TURING + GUARDIAN）**：純工学機能分析。SatiMonitor は 11 種の EventBus イベントを購読し、三段階パイプライン処理（バッファリング → バッチ分析 → 品質ベクトル計算）を行い、LoopQualityVector 四次元（Continuity, Granularity, Speed, Equanimity）を出力する。**副作用ゼロ**。工学的等価物：APM Agent + 行動パターン分析器 + QoS Monitor + SPC 異常検出器。

**C2（ASANGA + LINNAEUS）**：蘊構成提案。四つの方案——A ['vedana','samjna']、B ['vedana','samjna','vijnana']（推奨）、C ['samjna','vijnana']、D ['vijnana']。核心論証：SatiMonitor のイベント購読＝受（vedana）、パターン認識＝想（samjna）、品質評価＝識（vijnana）。行蘊は含まない——いかなる動作も実行しないためである。

## R2：交差査読

TURING が 40 件以上のコード引用を検証し、4 件の問題を発見した（重大な誤りはなし）。24 の合意点が討論なしで承認された。7 件の未解決問題と 4 件の相違が D1-D3 の討論に入った。

---
