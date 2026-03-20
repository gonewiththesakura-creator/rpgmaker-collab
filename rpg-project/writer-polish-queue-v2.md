# Writer Polish Queue v2 - 待反馈后填充

**Status**: Empty queue - waiting for QA / owner playtest results  
**Purpose**: Prioritized list of text segments needing polish based on real feedback  
**Trigger**: After `writer-playtest-feedback-capture.md` data collection completes

---

## 📋 队列结构说明

Each entry will contain:

| 字段 | 说明 |
|------|------|
| **优先级** | P0 (必须) / P1 (重要) / P2 ( nicer-to-have) |
| **段落ID** | 对应 polish 文件中的 📖 编号 |
| **场景** | Mxxx 事件位置 |
| **问题类型** | 不自然 / 情绪不足 / 节奏拖 / 收束弱 / 理解障碍 |
| **玩家反馈证据** | 来自 feedback capture 的原话 |
| **当前文案** | 引用 polish v1 版本 |
| **精修方向** | 待定（根据反馈填写） |
| **预计复杂度** | 低 / 中 / 高（变量/音效依赖） |

---

## 📭 当前队列（空）

> 暂无条目。待 Playtest TP-06~TP-10 数据返回后填充。

---

## 📊 预计填充时间复杂度

- **数据收集**: Playtest 1-3 天（取决于测试者数量）
- **分析**: 1 天（汇总 feedback-capture.md）
- **队列构建**: 0.5 天（填写本文件）
- **Polishing**: 1-2 天（执行 v2 精修）

**Total**: 预计 3-5 天 after playtest completion

---

## 🔄 工作流程

1. ✅ **完成**: Phase 3 Polish Lines v1 (delivered)
2. ⏳ **等待**: A 完成 Integration v1.2 → QA Playtest (TP-06~TP-10)
3. ⏳ **收集**: `writer-playtest-feedback-capture.md` 填满数据
4. ⏳ **分析**: Supervisor / Writer 分析失败点
5. ⏳ **填充**: 本队列文件按优先级填入问题段落
6. ⏳ **执行**: Writer 产出 `writer-phase3-polish-lines-v2.md`
7. ⏳ **验证**: A 替换，QA 回归测试

---

## 🎯 预期可能的问题（预判，非最终）

Based on common playtest patterns, these segments might need polish:

| 段落ID | 场景 | 预判风险 |
|--------|------|---------|
| 📖 4-6 | 家谱三页 | 信息量过大，玩家可能跳过 |
| 📖 7 | 离场抉择 | 选项不够吸引，玩家随意选 |
| 📖 8 | 黑衣人预警 | 紧张感不足，玩家反应平淡 |
| 📖 2 | 营地篝火 | 对话顺序导致信息碎片化 |
| 📖 10 | 谢临川对话 | 神秘感过强，玩家困惑 |

**注意**: 以上仅为预判，实际以真实反馈为准。现在不修改。

---

## 📝 最终交付物（待产出）

- ✅ `writer-phase3-polish-lines-v2.md`（精修版）
- ✅ `writer-playtest-feedback-analysis.md`（反馈分析摘要）
- ✅ Updated `writer-playtest-feedback-capture.md`（汇总数据）
- 🔄  commit hash + GitHub link

---

**状态**: EMPTY QUEUE - STANDBY  
**规则**: 无真实反馈，不凭空精修
