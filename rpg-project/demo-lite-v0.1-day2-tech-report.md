# demo-lite-v0.1-day2-tech-report.md

**Day**: 2  
**目标**: 实装Ch1~Ch3关键事件，完成"必败但有收获"  
**状态**: 开发中 / 待验收

---

## 执行检查清单

### 前置条件
- [ ] 本地有RPGMaker MZ工程
- [ ] 工程路径: `___________` (请填写)
- [ ] rpg_check.py 可访问

### 步骤1: 运行检查（基线）

```bash
cd /path/to/mz-project

# 检查1: 一致性
python /path/to/rpg_check.py consistency --output day2-consistency-before.json

# 检查2: 流程
python /path/to/rpg_check.py flow --profile demo-lite --output day2-flow-before.json
```

**预期结果**: 
- consistency: 可能显示Map缺失（正常，Day2要创建）
- flow: 可能显示CONFIG_ERROR（正常，Day2要创建）

### 步骤2: 创建地图

按 `demo-lite-v0.1-day1-manual-ops.md` 创建:

- [ ] M001 宗门广场 (20x15 tiles)
- [ ] M002 宗门周边 (25x18 tiles)
- [ ] M003 古碑区域 (20x20 tiles)

### 步骤3: 填入Ch1~Ch3事件

#### Ch1 事件
- [ ] E101 开场初始化 (自动执行)
- [ ] E102 素问入门 (NPC对话)
- [ ] E104 谢临川初遇 (NPC对话)
- [ ] E201 师尊任务 (NPC对话)
- [ ] 传送点 M001→M002

#### Ch2 事件
- [ ] 传送点 M002←M001
- [ ] 传送点 M002→M003

#### Ch3 事件（核心）
- [ ] E301+E302 古碑调查
- [ ] E303 黑衣人出现
- [ ] **E304 必败战斗**（重点）
- [ ] **E305 败退获取家谱**（重点）

### 步骤4: 实装"必败但有收获"

#### 数据库设置
- [ ] 创建敌人"黑衣人"
- [ ] 创建Troop 1（2个黑衣人）
- [ ] 创建Troop Event（回合结束触发）
- [ ] 设置HP<30%或回合>=5触发败退

#### 公共事件
- [ ] Common Event 1: 黑衣人战斗
- [ ] Common Event 2: 败退获取家谱
  - [ ] 败退剧情文本
  - [ ] 获得物品"残破家谱"
  - [ ] 传送回M001

### 步骤5: 填入B的文案

按B提供的文案包填入:

- [ ] 素问入门对话
- [ ] 谢临川初遇对话
- [ ] 师尊任务对话
- [ ] 古碑解读内容（含"九劫归一"）
- [ ] 黑衣人对话
- [ ] 败退后发现家谱的描述

### 步骤6: 运行检查（验证）

```bash
# 检查1: 一致性
python /path/to/rpg_check.py consistency --output day2-consistency-after.json

# 检查2: 流程
python /path/to/rpg_check.py flow --profile demo-lite --output day2-flow-after.json
```

**预期结果**:
- consistency: `resultType: "PASS"`
- flow: `resultType: "PASS"`

### 步骤7: 5分钟测试

**测试路径**:
1. 新游戏开始
2. 与素问对话
3. 与谢临川对话
4. 与师尊对话
5. 进入M002
6. 进入M003
7. 调查古碑
8. 等待黑衣人出现
9. 战斗5回合或HP<30%
10. **败退后获得家谱**

**计时目标**: 5分钟内完成

---

## 检查报告

### consistency-before.json

```json
{
  "checkSuite": "consistency",
  "resultType": "CONFIG_ERROR",
  "error": "...",
  "timestamp": "..."
}
```

### flow-before.json

```json
{
  "checkSuite": "flow",
  "resultType": "CONFIG_ERROR",
  "error": "...",
  "timestamp": "..."
}
```

### consistency-after.json

```json
{
  "checkSuite": "consistency",
  "resultType": "PASS",
  "overallStatus": "PASS",
  "checks": [...],
  "timestamp": "..."
}
```

### flow-after.json

```json
{
  "checkSuite": "flow",
  "profile": "demo-lite",
  "resultType": "PASS",
  "overallStatus": "PASS",
  "checks": [...],
  "timestamp": "..."
}
```

---

## 已知Bug清单

### 阻断性Bug（必须修复）

| ID | 描述 | 状态 | 修复方案 |
|----|------|------|---------|
| B1 | | | |
| B2 | | | |

### 非阻断性Bug（可延后）

| ID | 描述 | 状态 | 修复方案 |
|----|------|------|---------|
| N1 | | | |
| N2 | | | |

---

## 验收确认

- [ ] 新档5分钟内可跑到"败退后拿家谱"
- [ ] consistency检查 PASS
- [ ] flow检查 PASS
- [ ] 所有报告已提交

---

**状态**: 待执行 / 待验收

**执行人**: ___________ (请填写)

**完成时间**: ___________ (请填写)
