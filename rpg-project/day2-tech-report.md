# day2-tech-report.md

**Day**: 2  
**任务**: 实装Ch1~Ch3关键事件，完成"必败但有收获"  
**交付状态**: 可直接执行的最小操作包  
**预计总工时**: 30分钟（熟练后）

---

## 假设的工程结构

```
MZ工程根目录/
├── data/
│   ├── System.json          (开关/变量定义)
│   ├── Items.json           (物品定义)
│   ├── CommonEvents.json    (公共事件)
│   ├── Troops.json          (战斗队伍)
│   ├── Map001.json          (M001宗门广场)
│   ├── Map002.json          (M002宗门周边)
│   ├── Map003.json          (M003古碑区域)
│   └── ...
├── tools/
│   └── rpg-cli/
│       └── rpg_check.py     (检查工具)
└── 工程文件.rpgproject
```

**你的MZ工程路径**: `___________` (请填写，如 `C:\RPGMaker\太玄界`)

---

## 执行步骤与预期输出

### 步骤0: 环境确认（2分钟）

**执行命令**:
```bash
cd <你的MZ工程根目录>
ls data/System.json
python --version
```

**预期输出**:
```
data/System.json  [存在]
Python 3.x.x      [3.8+]
```

**成功判定**: System.json存在，Python版本≥3.8

---

### 步骤1: 基线检查（3分钟）

**执行命令**:
```bash
cd <你的MZ工程根目录>
python tools/rpg-cli/rpg_check.py consistency --output day2-before-consistency.json
python tools/rpg-cli/rpg_check.py flow --profile demo-lite --output day2-before-flow.json
```

**预期输出**:
```json
// day2-before-consistency.json
{
  "checkSuite": "consistency",
  "resultType": "CONFIG_ERROR",
  "error": "Map001.json not found",
  "hint": "..."
}

// day2-before-flow.json
{
  "checkSuite": "flow",
  "resultType": "CONFIG_ERROR",
  "error": "..."
}
```

**成功判定**: 显示CONFIG_ERROR（正常，地图尚未创建）

---

### 步骤2: 数据库配置（5分钟）

**操作**: 在RPGMaker MZ编辑器中

**菜单路径**: 游戏 → 数据库 → 系统

**执行内容**:
1. 开关标签页，添加以下开关（ID对应）:
   - ID 1: system_tutorial_done
   - ID 10: plot_ch1_done
   - ID 11: plot_ch2_done
   - ID 12: plot_ch3_done
   - ID 100: xie_met
   - ID 101: xie_following

2. 变量标签页，添加:
   - ID 1: hero_level
   - ID 2: hero_chapter
   - ID 3: xie_affection

**预期输出**: 数据库保存成功

**验证命令**:
```bash
grep "system_tutorial_done" data/System.json
```

**成功判定**: 命令返回包含开关名称

---

### 步骤3: 创建物品（3分钟）

**菜单路径**: 游戏 → 数据库 → 物品

**执行内容**:
1. 新建物品，ID: 1
2. 名称: 残破家谱
3. 图标: 选择书卷类
4. 描述: "沈家的残破家谱，上面记载着'九劫归一'的字样..."
5. 物品类型: 关键物品

**预期输出**: 物品保存成功

**验证命令**:
```bash
grep "残破家谱" data/Items.json
```

**成功判定**: 命令返回包含物品名称

---

### 步骤4: 创建地图M001（5分钟）

**菜单路径**: 右键地图列表 → 新建

**执行内容**:
1. 名称: M001宗门广场
2. ID: 1
3. 尺寸: 宽20，高15
4. 绘制: 中央广场+边缘建筑
5. 保存

**预期输出**: Map001.json生成

**验证命令**:
```bash
ls -la data/Map001.json
```

**成功判定**: 文件存在，大小>1KB

---

### 步骤5: 创建地图M002（3分钟）

**执行内容**:
1. 名称: M002宗门周边
2. ID: 2
3. 尺寸: 宽25，高18
4. 绘制: 山路连接
5. 保存

**验证命令**:
```bash
ls -la data/Map002.json
```

---

### 步骤6: 创建地图M003（3分钟）

**执行内容**:
1. 名称: M003古碑区域
2. ID: 3
3. 尺寸: 宽20，高20
4. Tileset: Dungeon
5. 绘制: 峡谷+中央古碑区域
6. 保存

**验证命令**:
```bash
ls -la data/Map003.json
```

---

### 步骤7: 创建关键事件（10分钟）

按 `day2-tech-ops-checklist.md` 逐项创建

**核心事件清单**:
- [ ] E101 开场初始化 (M001)
- [ ] E102 素问入门 (M001)
- [ ] E104 谢临川初遇 (M001)
- [ ] E201 师尊任务 (M001)
- [ ] 传送点 M001→M002
- [ ] 传送点 M002→M003
- [ ] E301+E302 古碑调查 (M003)
- [ ] E303 黑衣人出现 (M003)
- [ ] E304 必败战斗配置
- [ ] E305 败退获取家谱

---

### 步骤8: 验证检查（3分钟）

**执行命令**:
```bash
python tools/rpg-cli/rpg_check.py consistency --output day2-after-consistency.json
python tools/rpg-cli/rpg_check.py flow --profile demo-lite --output day2-after-flow.json
```

**预期输出**:
```json
{
  "checkSuite": "consistency",
  "resultType": "PASS",
  "overallStatus": "PASS"
}

{
  "checkSuite": "flow",
  "profile": "demo-lite",
  "resultType": "PASS",
  "overallStatus": "PASS"
}
```

**成功判定**: 两个检查都显示PASS

---

### 步骤9: 5分钟游戏测试

**测试路径**:
1. 新游戏 → 开场自动播放
2. 与素问对话 → 传送
3. 与谢临川对话
4. 与师尊对话
5. 进入M002
6. 进入M003
7. 调查古碑
8. 等待黑衣人
9. 战斗5回合或HP<30%
10. **败退后获得家谱**

**计时**: 从开始到家谱入手 ≤5分钟

**成功判定**: 
- [ ] 流程无卡顿
- [ ] 败退触发正常
- [ ] 物品栏有"残破家谱"

---

## 实际执行结果（执行后填写）

### 基线检查结果
| 检查 | resultType | 备注 |
|------|-----------|------|
| consistency-before | _________ | |
| flow-before | _________ | |

### 最终检查结果
| 检查 | resultType | 备注 |
|------|-----------|------|
| consistency-after | _________ | |
| flow-after | _________ | |

### 5分钟测试结果
- 实际用时: _______ 分钟
- 败退触发: [ ] 正常 [ ] 异常
- 家谱获得: [ ] 正常 [ ] 异常

### 提交文件
- [ ] day2-after-consistency.json
- [ ] day2-after-flow.json

---

**状态**: 待执行 → 执行后填写 → Ready for Supervisor Check
