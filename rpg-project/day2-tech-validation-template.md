# day2-tech-validation-template.md

**执行后填写此模板**  
**提交前必须完成所有字段**

---

## 执行信息

| 字段 | 填写内容 |
|------|---------|
| 执行日期 | 2026-03-__ |
| 执行人 | ___________ |
| MZ工程路径 | ___________ |
| 总用时 | ___________ 分钟 |

---

## 步骤1: 基线检查结果（执行前）

**执行命令**:
```bash
python tools/rpg-cli/rpg_check.py consistency > day2-before-consistency.json
python tools/rpg-cli/rpg_check.py flow --profile demo-lite > day2-before-flow.json
```

### consistency-before.json

```json
{
  "checkSuite": "consistency",
  "resultType": "_____________",
  "overallStatus": "_____________",
  "error": "_____________",
  "hint": "_____________"
}
```

**备注**: ___________

---

### flow-before.json

```json
{
  "checkSuite": "flow",
  "resultType": "_____________",
  "overallStatus": "_____________",
  "error": "_____________",
  "hint": "_____________"
}
```

**备注**: ___________

---

## 步骤2: 数据库配置验证

### 开关配置

| ID | 名称 | 状态 |
|----|------|------|
| 1 | system_tutorial_done | [ ] 已添加 [ ] 未添加 |
| 10 | plot_ch1_done | [ ] 已添加 [ ] 未添加 |
| 11 | plot_ch2_done | [ ] 已添加 [ ] 未添加 |
| 12 | plot_ch3_done | [ ] 已添加 [ ] 未添加 |
| 100 | xie_met | [ ] 已添加 [ ] 未添加 |
| 101 | xie_following | [ ] 已添加 [ ] 未添加 |

**验证命令输出**:
```bash
$ grep "system_tutorial_done" data/System.json
_______________
```

---

### 变量配置

| ID | 名称 | 状态 |
|----|------|------|
| 1 | hero_level | [ ] 已添加 [ ] 未添加 |
| 2 | hero_chapter | [ ] 已添加 [ ] 未添加 |
| 3 | xie_affection | [ ] 已添加 [ ] 未添加 |

---

### 物品配置

| 字段 | 内容 |
|------|------|
| 物品ID | ___ |
| 名称 | [ ] 残破家谱 [ ] 其他 |
| 图标 | [ ] 已选 [ ] 未选 |
| 类型 | [ ] 关键物品 [ ] 其他 |

**验证命令输出**:
```bash
$ grep "残破家谱" data/Items.json
_______________
```

---

## 步骤3: 地图创建验证

| 地图 | 文件存在 | 尺寸正确 | 事件数量 |
|------|---------|---------|---------|
| M001 | [ ] 是 [ ] 否 | [ ] 20x15 [ ] 其他 | ___个 |
| M002 | [ ] 是 [ ] 否 | [ ] 25x18 [ ] 其他 | ___个 |
| M003 | [ ] 是 [ ] 否 | [ ] 20x20 [ ] 其他 | ___个 |

**验证命令**:
```bash
$ ls -la data/Map001.json data/Map002.json data/Map003.json
_______________
```

---

## 步骤4: 关键事件验证

| 事件 | 地图 | 状态 | 备注 |
|------|------|------|------|
| E101 开场初始化 | M001 | [ ] 完成 [ ] 未完成 | |
| E102 素问入门 | M001 | [ ] 完成 [ ] 未完成 | |
| E104 谢临川初遇 | M001 | [ ] 完成 [ ] 未完成 | |
| E201 师尊任务 | M001 | [ ] 完成 [ ] 未完成 | |
| 传送M001→M002 | M001 | [ ] 完成 [ ] 未完成 | |
| 传送M002→M003 | M002 | [ ] 完成 [ ] 未完成 | |
| E301+E302 古碑 | M003 | [ ] 完成 [ ] 未完成 | |
| E303 黑衣人 | M003 | [ ] 完成 [ ] 未完成 | |
| E304 必败战斗 | Troop | [ ] 完成 [ ] 未完成 | |
| E305 败退家谱 | Common | [ ] 完成 [ ] 未完成 | |

---

## 步骤5: 最终检查结果（执行后）

**执行命令**:
```bash
python tools/rpg-cli/rpg_check.py consistency > day2-after-consistency.json
python tools/rpg-cli/rpg_check.py flow --profile demo-lite > day2-after-flow.json
```

### consistency-after.json

```json
{
  "checkSuite": "consistency",
  "resultType": "_____________",
  "overallStatus": "_____________",
  "checks": [
    {
      "checkName": "Map Existence Check",
      "resultType": "_____________",
      "errors": ___________
    },
    {
      "checkName": "Key Events Check",
      "resultType": "_____________",
      "errors": ___________
    },
    {
      "checkName": "Switches/Variables Check",
      "resultType": "_____________",
      "errors": ___________
    },
    {
      "checkName": "Key Items Check",
      "resultType": "_____________",
      "errors": ___________
    }
  ]
}
```

**截图位置**: [请粘贴截图]

**结果**: [ ] PASS [ ] CHECK_FAIL [ ] CONFIG_ERROR

---

### flow-after.json

```json
{
  "checkSuite": "flow",
  "profile": "demo-lite",
  "resultType": "_____________",
  "overallStatus": "_____________",
  "checks": [
    {
      "checkName": "Demo Chain Reachability",
      "resultType": "_____________"
    },
    {
      "checkName": "Unlosable Battle Check",
      "resultType": "_____________"
    },
    {
      "checkName": "Genealogy Obtainable Check",
      "resultType": "_____________"
    },
    {
      "checkName": "Ch4 Hook Check",
      "resultType": "_____________"
    }
  ]
}
```

**截图位置**: [请粘贴截图]

**结果**: [ ] PASS [ ] CHECK_FAIL [ ] CONFIG_ERROR

---

## 步骤6: 5分钟游戏测试

### 测试记录

| 检查点 | 状态 | 时间戳 |
|--------|------|--------|
| 新游戏开始 | [ ] 正常 [ ] 异常 | ___:___ |
| 素问对话完成 | [ ] 正常 [ ] 异常 | ___:___ |
| 谢临川对话完成 | [ ] 正常 [ ] 异常 | ___:___ |
| 师尊任务获得 | [ ] 正常 [ ] 异常 | ___:___ |
| 进入M002 | [ ] 正常 [ ] 异常 | ___:___ |
| 进入M003 | [ ] 正常 [ ] 异常 | ___:___ |
| 古碑调查完成 | [ ] 正常 [ ] 异常 | ___:___ |
| 黑衣人出现 | [ ] 正常 [ ] 异常 | ___:___ |
| 战斗败退触发 | [ ] 正常 [ ] 异常 | ___:___ |
| **获得残破家谱** | [ ] 正常 [ ] 异常 | ___:___ |

### 测试结果

| 指标 | 数值 |
|------|------|
| 总用时 | ___ 分 ___ 秒 |
| 目标达成 | [ ] ≤5分钟 [ ] >5分钟 |
| 流程完整性 | [ ] 100% [ ] 有断点 |
| 败退机制 | [ ] 正常触发 [ ] 未触发 |
| 家谱获得 | [ ] 必得 [ ] 未获得 |

**游戏截图**: [请粘贴关键节点截图]

---

## 提交清单

- [ ] day2-tech-report.md 已填写
- [ ] day2-after-consistency.json 已生成
- [ ] day2-after-flow.json 已生成
- [ ] 本验证模板已填写完整
- [ ] 所有截图已收集
- [ ] Git commit 已提交

---

**最终状态**: [ ] Ready for Supervisor Check

**备注**: ___________
