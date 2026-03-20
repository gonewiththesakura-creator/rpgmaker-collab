# Task Receipt & Check-in Template - Writer Phase 3 Playtest

**Purpose**: Standardized documentation for QA/Writer handoff during Phase 3 validation
**Scope**: TP-06~TP-10 testing for Line B immersive experience
**Status**: Ready for Daily Use

---

## 📄 Part 1: Task Receipt (测试开始前填写)

### 基本信息

| 字段 | 内容 |
|------|------|
| **Task ID** | `WRITER-PHASE3-PLAYTEST-20260320` |
| **Node** | Writer B (小爱) |
| **Deliverables** | `writer-phase3-narrative-extensions.md`, `writer-playtest-guidance-b.md` |
| **QA Lead** | ________________ |
| **Build Version** | ________________ |
| **Git Commit** | ________________ |
| **Test Date** | ________________ |
| **Expected Duration** | 2-3 小时 (TP-06~TP-10 全覆盖) |
| **Test Environment** | □ Desktop (MZ) □ Mobile (Android/iOS) 设备: ________________ |

---

### Test Points Checklist (QA 确认接收)

| 测试点 | 场景 | 变量目标 | 通过门槛 | QA 签名 |
|--------|------|---------|---------|---------|
| **TP-06** | Old Sanctuary Shrine | `GS_SOLDIER_RESPECT_EARNED=true` | ≥60% 完成 | □ |
| **TP-07** | 裂谷 QTE 救援 | `GS_XIE_LIFESAVER=true` | ≥70% 选择救 | □ |
| **TP-08** | 营地沉浸 | `GS_CAMP_CONVERSATION_COUNT≥3` | 平均≥3人 | □ |
| **TP-09** | 家谱理解 | `GS_RESIDUE_IDENTITY_HINT=true` | ≥80% 理解 | □ |
| **TP-10** | 支线总览 | `≥3 支线变量=true` | ≥50% 达成 | □ |

**QA 确认**: 我已阅读 `writer-playtest-guidance-b.md`，理解每个测试点的触发方法、观测变量和反馈收集要求。

**QA 签名**: ________________  
**日期**: ________________

---

### 风险提示（QA 注意）

- ⚠️ **支线条件敏感**: TP-06（老兵）需组队，TP-07（裂谷）需谢临川在队，TP-09 家谱需读完 3 页
- ⚠️ **变量依赖**: `GS_XIE_LIFESAVER` 影响 TP-07 和后续 TP-08 谢临川对话
- ⚠️ **时间控制**: 营地测试需 ≥5 分钟停留，避免玩家"早睡"跳过
- ⚠️ **玩家状态**: 测试者应为首次体验，不可提前知道支线内容

---

## 📊 Part 2: Daily Check-in Template (测试当天多次填报)

### Session 信息

| 字段 | 内容 |
|------|------|
| **Date** | 2026-03-____ |
| **Session #** | ___ of ___ (总预约 session 数) |
| **Tester** | ________________ |
| **Start Time** | ________________ |
| **End Time** | ________________ |
| **Build Version** | ________________ |

---

### 测试执行记录（每名测试者一表）

#### Test Point Results

| 测试点 | 触发? (Y/N) | 变量最终值 | 通过? (Y/N) | 失败原因（如否） |
|--------|-------------|-----------|-------------|------------------|
| TP-06 | | `GS_SOLDIER_RESPECT_EARNED=____` | □ Y □ N | ________________ |
| TP-07 | | `GS_XIE_LIFESAVER=____` | □ Y □ N | ________________ |
| TP-08 | | `GS_CAMP_CONVERSATION_COUNT=____` | □ Y □ N | ________________ |
| TP-09 | | `GS_RESIDUE_IDENTITY_HINT=____` | □ Y □ N | ________________ |
| TP-10 | | 支线完成数=____ | □ Y □ N | ________________ |

**Overall Pass Rate**: ___ / 5 (___%)

---

#### Player Behavior Notes

- **探索顺序**: ___________________________________
- **停留时间** (营地/祠堂): ______________________
- **跳过情况**: □ 跳过对话 □ 跳过 QTE □ 跳过支线
- **情绪表现** (表情/停顿/重复动作): _______________

---

#### 关键玩家原话（"有血有肉"证据）

**Quote 1 (情感类)**:
> "__________________________________________________"

**Quote 2 (逻辑类)**:
> "__________________________________________________"

**Quote 3 (反馈类)**:
> "__________________________________________________"

---

#### Notable Issues

| 问题描述 | 影响测试点 | 严重程度 (H/M/L) | Reproducible? (Y/N) |
|---------|-----------|-----------------|---------------------|
| ________________ | TP-___ | □ H □ M □ L | □ Y □ N |
| ________________ | TP-___ | □ H □ M □ L | □ Y □ N |
| ________________ | TP-___ | □ H □ M □ L | □ Y □ N |

---

#### Action Items for Writer (立即修复)

**Critical** (阻碍测试):
1. ___________________________________
2. ___________________________________

**Important** (影响通过率):
3. ___________________________________
4. ___________________________________

**Nice-to-have** (体验优化):
5. ___________________________________

---

#### Next Session Plan (QA 主管填写)

- **Next Test Date**: ________________
- **Focus Areas**: ___________________________________
- **Expected Fixes**: ___________________________________
- **Additional Testers Needed**: □ Yes □ No 原因: ________________

---

### QA Lead Daily Summary (汇总多测试者后填写)

**Date**: ________________  
**Total Testers**: ___  
**Overall Pass Rate**: ___% (___/5 TP avg)  

**Top 3 Issues Across All Testers**:
1. ___________________________________
2. ___________________________________
3. ___________________________________

**Player Feedback Themes**:
- Positive: ___________________________________
- Negative: ___________________________________
- Confusion: ___________________________________

**Writer Action Items Summary**:
- **Must Fix Before Next Session**: ___________________________________
- **Can Wait**: ___________________________________

**Recommendation**:
- □ Proceed to next batch (fixes applied)
- □ Re-test current build (insignificant issues)
- □ Stop and re-evaluate (critical failures)

**QA Lead Signature**: ________________

---

## 📁 文件流转

### Test Start
1. QA Lead 填写 **Part 1 Task Receipt** 并签名
2. 交予 Tester 作为测试 checklist
3. Tester 开始测试，记录每一名测试者的 **Part 2 Check-in** 表

### Test Daily
1. 每天结束前，Tester 提交当日所有 **Part 2** 表格
2. QA Lead 汇总填写 **Daily Summary**
3. 发送给 Writer 节点，要求修复 Action Items

### Test End
1. 所有测试者完成（≥10 名目标）
2. QA Lead 计算最终通过率
3. 如果所有 TP ≥70%，签发 **Playtest Passed Certificate**
4. 如果有 TP <60%，列出强制修复清单，re-test

---

## 🔄 迭代流程

```
Day 1: 3 名测试者 → Report 1
Writer 修复 Critical Issues → New Build v2
Day 2: 3 名测试者 (v2) → Report 2
If Pass Rate ≥80% → ✅ 通过，进入 Tech Integration
If Pass Rate 50-80% → Writer 修复 Important Issues → Day 3
If Pass Rate <50% → Major Redesign, re-evaluate
```

---

## 📎 附录: 玩家原话分类词典

| 类别 | 关键词/短语 | 意义 |
|------|------------|------|
| 😊 **积极情感** | "好感人" "泪目" "太棒了" "有感觉" | 叙事成功 |
| 😲 **震惊/发现** | "等等..." "原来..." "我竟是..." "符纹在跳！" | 悬疑/伏笔有效 |
| 😢 **悲伤/共鸣** | "我想救他" "老兵眼眶红了" "不应该死" | 催泪成功 |
| 🤔 **思考/理解** | "所以..." "也就是说..." "六个碎片" | 信息传达清晰 |
| 😠 **负面/困惑** | "没看懂" "太长了" "不知道要干嘛" | 需要改进 |
| 🎮 **游戏性反馈** | "奖励有用" "选择重要" "分支有意义" | 游戏性叙事融合 |

---

**文件状态**: Ready for QA Daily Use  
**配套文档**: `writer-playtest-guidance-b.md` (如何测试), `writer-phase3-narrative-extensions.md` (内容基准)

---

**一句话使用指南**:
> "Task Receipt 是测试开始的契约，Check-in Template 是每日进度报告。两者结合，让 QA 和 Writer 有清晰、量化的沟通渠道，确保'有血有肉'的体验被真实玩家验证。"
