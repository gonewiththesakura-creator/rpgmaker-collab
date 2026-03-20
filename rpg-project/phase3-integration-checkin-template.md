# Phase 3 Integration - Task Receipt & Check-in

**Task ID**: `WRITER-PHASE3-INTEGRATION-V1`  
**Deliverables**:  
1. `writer-phase3-integration-pack-v1.md` (A: 地图对接表, B: 文本压缩版, C: 必留/可选/后移)  
2. `writer-phase3-priority-lines.md` (Top 8 most valuable segments)  

**Status**: Ready for Supervisor Check  
**Date**: 2026-03-20  
**Writer Node**: B (小爱)  
**Git Commit**: `fb2d936`  
**GitHub**: https://github.com/gonewiththesakura-creator/rpgmaker-collab/commit/fb2d936

---

## ✅ Task Receipt (交付确认)

### 交付内容检查

| 文件 | 状态 | 说明 |
|------|------|------|
| `writer-phase3-integration-pack-v1.md` | ✅ | 地图对接表 + 文本压缩 + 三类标记 |
| `writer-phase3-priority-lines.md` | ✅ | Top 8 精华段（主线/支线/世界观/收束） |
| `task-receipt-checkin-template.md` | ✅ | 测试流程模板（已交付） |
| `writer-playtest-guidance-b.md` | ✅ | TP-06~TP-10 详细指南 |

### 核心交付指标

- **压缩后事件数**: P0 9 事件，P1 5 事件，P2 2 内容
- **总变量新增**: 12 个（仍在 MZ ≤30 约束内）
- **文本长度**: 所有段符合单屏显示（≤3 行 MZ 对话框）
- **优先级清晰**: 必留/可选/后移 三类标记明确

### Supervisor 审核要点

1. **地图对接表** (Section A)
   - ✅ M004~M008 每图 2-3 段
   - ✅ 类型标注 (主线/调查/支线/战后独白/离场钩子)
   - ✅ 变量映射完整

2. **文本压缩版** (Section B)
   - ✅ MZ 直接贴格式
   - ✅ 单段不太长
   - ✅ 保留"你在做什么/为什么/下一步"模板

3. **必留/可选/后移** (Section C)
   - ✅ 全部 Phase 3 新增内容已分类
   - ✅ P0=9事件, P1=5事件, P2=2内容
   - ✅ 给出集成数量建议 (9-10 事件)

4. **Priority Lines** (Top 8)
   - ✅ 2 主线推进 (裂谷选择、家谱真相)
   - ✅ 2 支线情感 (裂谷救援羁绊、营地篝火)
   - ✅ 2 世界观线索 (三岔门、六残我)
   - ✅ 2 收束/钩子 (家谱离场、黑衣人预警)
   - ✅ 每段含场景/触发/情绪/为什么保留

---

## 📊 Check-in Template (Phase 3 集成验证)

### Session 信息

| 字段 | 内容 |
|------|------|
| **Date** | 2026-03-____ |
| **Integrator** (A) | ________________ |
| **Build Version** | ________________ |
| **Git Commit Before** | ________________ |
| **Git Commit After** | ________________ |

---

### 集成执行记录

#### 必留 (P0) 集成情况

| 事件 | 位置 | 文件引用 | 集成? (Y/N) | 问题/备注 |
|------|------|---------|------------|----------|
| 裂谷 QTE 后独白 | M004 事件 1 | integration-pack.md B-1 | □ Y □ N | ________________ |
| 营地篝火启动 | M005 事件 1 | integration-pack.md B-3 | □ Y □ N | ________________ |
| 秘洞三岔门 | M006 事件 1 | integration-pack.md B-4 | □ Y □ N | ________________ |
| 家谱 3 页压缩 | M007 事件 1 | integration-pack.md B-5 | □ Y □ N | ________________ |
| 家谱离场抉择 | M008 事件 1 | integration-pack.md B-7 | □ Y □ N | ________________ |
| 黑衣人逼近预警 | M008 事件 3 | integration-pack.md B-8 | □ Y □ N | □ Y □ N | ________________ |
| 裂谷离场路径选择 | M004 事件 3 | integration-pack.md B-2 | □ Y □ N | ________________ |

**P0 集成完成率**: ___ / 7

---

#### 可选 (P1) 集成情况

| 事件 | 位置 | 是否集成 | 理由 (如果未集成) |
|------|------|---------|-------------------|
| Old Sanctuary 入口提示 | M005 事件 2 / M008 事件 2 | □ Y □ N | ________________ |
| 谢临川洞穴提醒 | M007 事件 3 | □ Y □ N | ________________ |
| 裂谷崖壁检查 | M004 事件 2 | □ Y □ N | ________________ |

**P1 集成完成率**: ___ / 3

---

#### Priority Lines 验证

| 段 # | 类型 | 场景 | 是否集成 | 情绪反馈 (QA 验证) |
|------|------|------|---------|-------------------|
| 1 | 主线推进 | 裂谷救援选择 | □ Y □ N | ________________ |
| 2 | 主线推进 | 家谱真相 | □ Y □ N | ________________ |
| 3 | 支线情感 | 谢临川羁绊 | □ Y □ N | ________________ |
| 4 | 支线情感 | 营地篝火 | □ Y □ N | ________________ |
| 5 | 世界观线索 | 三岔门 | □ Y □ N | ________________ |
| 6 | 世界观线索 | 六残我 | □ Y □ N | ________________ |
| 7 | 收束/钩子 | 家谱离场 | □ Y □ N | ________________ |
| 8 | 收束/钩子 | 黑衣人预警 | □ Y □ N | ________________ |

**Priority Lines 完成率**: ___ / 8

---

### 集成质量检查

- [ ] 所有 P0 文本已按照 `integration-pack-v1.md` Section B 的压缩版本贴入
- [ ] 变量名正确 (`GS_*`) 且在 Database 中存在
- [ ] 事件触发条件与 `trigger conditions` 一致
- [ ] 单屏文本长度 ≤3 行 (MZ 标准)
- [ ] 音效标记已添加 (如果 Audio 已就绪)
- [ ] "你在做什么/为什么/下一步" 模板完整
- [ ] 无新增变量超出 30 个限制（总变量已统计）

---

### Issues & Blockers

| 问题描述 | 影响事件 | 严重程度 (H/M/L) | 需要 Writer 协助? (Y/N) |
|---------|---------|-----------------|-------------------------|
| ________________ | M___ | □ H □ M □ L | □ Y □ N |
| ________________ | M___ | □ H □ M □ L | □ Y □ N |
| ________________ | M___ | □ H □ M □ L | □ Y □ N |

---

### 下一步行动

**如果 P0 完成率 = 7/7**:
- ✅ 进入下一阶段：Playtest 验证 (使用 `writer-playtest-guidance-b.md`)
- 提交新构建版本，commit hash: ________________

**如果 P0 完成率 < 7/7**:
- ❌ 必须补充缺失 P0 内容
- 分析原因: □ 事件不够 □ 变量缺失 □ 文案过长 □ 其他: ______
- 要求 Writer 协助事项: __________________________________

**如果 P1 完成率 < 3/3**:
- ⚠️ 非阻塞，但应在 Playtest 前决定是否补全
- 记录理由供 Supervisor 评估是否扩充到 1.5 小时体验

---

### Supervisor Final Check-off

**Integration Verified By**: ________________  
**Date**: ________________  
**Status**:  
- ✅ **P0 Complete** (7/7) - Ready for Playtest  
- ⚠️ **P0 Partial** (___/7) - Needs completion before playtest  
- ❌ **P0 Incomplete** (<<7) - Major rework needed

**Notes**: ___________________________________

---

**文件流转**:
1. Integrator (A) 在集成过程中填写本表
2. 完成后提交给 Supervisor
3. Supervisor 检查并签字
4. 如果 P0 complete，进入 Playtest 阶段（使用 `writer-playtest-guidance-b.md` + `task-receipt-checkin-template.md`）

---

**一句话使用指南**:
> "Check-in Template 是集成过程的追踪表，确保 7 个 P0 事件全部到位。只有 P0 完成率 100% 才能进入 Playtest，P1/P2 可后续补充。"
