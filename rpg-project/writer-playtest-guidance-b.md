# Writer Playtest Guidance - Part B (TP-06~TP-10 Detailed)

**Purpose**: Guide QA/testers on how to validate Line B side quests and emotional payoff
**Based on**: `writer-phase3-narrative-extensions.md`, `immersive-narrative-line-b.md`, `playtest-points-lite.md`
**Scope**: TP-06 through TP-10, covering veteran, fallen scout, camp immersion, registry understanding, side quest completion
**Status**: Ready for QA execution with manual walkthrough

---

## 📋 通用 QA 流程 (适用于 TP-06~TP-10)

1. **准备阶段**
   - 确保游戏版本包含 Phase 3 所有支线事件
   - 开启变量监控面板（应能看到 V10-V52 和 GS_* 变量）
   - 准备录音/录像设备（捕捉玩家原话）
   - 准备好《Playtest Feedback Table》（附录 A）

2. **测试阶段**
   - 按顺序执行 TP-06→TP-07→TP-08→TP-09→TP-10
   - 每个测试点记录:
     - ✅ 触发变量是否设置
     - ✅ 玩家行为（对话选择、QTE、探索顺序）
     - ✅ 玩家原话（尤其是情感反应）
     - ✅ 奖励是否获得（物品、后续对话）
   - 允许玩家自由探索，但确保测试点场景不被跳过

3. **验证通过标准**
   - 每个测试点有明确量化门槛（如 ≥60%）
   - 记录失败案例的具体原因（如: "玩家未触发老兵对话 because 没有组队"）
   - 收集"玩家可能说的话"作为"有血有肉"的证据

---

## 🎯 TP-06: 老兵信任度 (Old Sanctuary Shrine 完成)

### 目标
验证玩家是否信任老兵、接受符纹、并完成祠堂祭拜，获得情感共鸣

### 触发条件
- 入山时选择组队 (`GS_TRIAL_ENTERED_WITH_GROUP = true`)
- 与老兵对话 ≥2 次（听他讲完沈家军故事和父亲提及）
- 持有 Hot Token 并返回营地后找到 Old Sanctuary Shrine

### 关键变量
| 变量 | 说明 | 期望值 |
|------|------|--------|
| `GS_SOLDIER_FATHER_MENTION` | 老兵提及主角父亲 | `true` |
| `GS_SOLDIER_RESPECT_EARNED` | 完成祠堂祭拜获得尊敬 | `true` |
| `GS_OLD_SANCTUARY_COMPLETED` | 支线完成标志 | `true` |

### 玩家行为验证
- [ ] 与老兵对话时选择"听故事"选项（不中断）
- [ ] 前往 Old Sanctuary Shrine（营地附近，需主动探索）
- [ ] 在祠堂执行"放置符纹→上香"动作
- [ ] 观看/听完老兵哽咽独白（不跳过）

### 期望反馈词（证据）
- **情感类**: "这老兵有故事"、"我眼睛有点酸"、"符纹在跳！"
- **认同类**: "沈家军精神还在"、"他想让我延续"
- **奖励感知**: "Three-Thunder Talisman? 厉害了！" "感谢老兵！"

### 可改进方向（如果失败）
- **失败表现**: <60% 玩家完成祠堂祭拜
- **可能原因**: 祠堂位置隐蔽、老兵故事过长、奖励提示不足
- **改进**:
  1. 在营地对话增加："老兵说祠堂在营地北边，那里有沈家军最后的魂"
  2. 祠堂入口增加光点引导（符纹共鸣时自动显示）
  3. 奖励显示更明显（祭拜后画面闪光 + 文字："Three-Thunder Talisman x3 获得！"）

---

## 🎯 TP-07: 裂谷救援情感 (QTE 选择)

### 目标
验证 ≥70% 玩家选择救同伴（谢临川或其他），并感受到羁绊加深

### 触发条件
- 裂谷崩塌事件 (`GS_RIFT_COLLAPSE = true`)
- QTE 救援选项出现

### 关键变量
| 变量 | 说明 | 期望值 |
|------|------|--------|
| `GS_XIE_LIFESAVER` | 救了谢临川（若他在队） | `true` |
| `GS_RIFT_CLIMB_SUCCESS` | QTE 成功 | `true` |
| `GS_BOND_WITH_XIE_STRENGTHENED` | 羁绊增强标志 | `true` |

### 玩家行为验证
- [ ] 选择"救同伴"（B 选项）而非"自救"（A）
- [ ] QTE 成功（快速按键正确）
- [ ] 救援后谢临川/同伴说出"你为什么救我？"等对话并听完
- [ ] 不要反复尝试失败（≤2 次 QTE 尝试）

### 期望反馈词（证据）
- **情感类**: "不能丢下他"、" teammate!" "谢临川：）"
- **逻辑类**: "当然要救"、"一起掉下去不如拼一把"
- **后悔类**: "刚才差点松手...现在想想后怕"（正面的后怕）

### 可改进方向（如果失败）
- **失败表现**: <70% 选 B，或 QTE 失败率高
- **可能原因**: QTE 太难、时间太短、玩家误以为 A 是"快速通关"
- **改进**:
  1. QTE 提示更清晰："B. 救他（需快速按键）"
  2. 增加失败的剧情后果（如: 自救成功但谢临川坠崖，后续永久少了这个角色）
  3.延长 QTE 时间窗口 + 视觉提示（屏幕边缘闪光）

---

## 🎯 TP-08: 营地沉浸时长 (对话覆盖度)

### 目标
验证玩家在营地平均停留 ≥5 分钟，且与至少 3 个 NPC 完成深度对话

### 触发条件
- 裂谷救援后进入营地 (`GS_CAMP_RESTED = true`)

### 关键变量
| 变量 | 说明 | 期望值 |
|------|------|--------|
| `GS_CAMP_CONVERSATION_COUNT` | 完成的深度对话人数 | ≥ 3 |
| `GS_CAMP_FIRST_CHOICE` | 优先对话对象 | 任意（无失败） |
| `GS_CAMP_FULL_DIALOGUE` | 所有人对话完成 | `true`（加分） |
| `GS_CAMP_TIME_SPENT` | 停留帧数/秒数 | ≥ 300 帧 (~5秒) 实际应 >300帧 |

### 玩家行为验证
- [ ] 与老兵对话并听完沈家历史
- [ ] 与药剂师对话并获得草药
- [ ] 与谢临川对话了解承诺（如果他在队）
- [ ] 不直接"早睡"跳过营地
- [ ] 停留时间计时（从进入营地到离开）

### 期望反馈词（证据）
- **沉浸类**: "这里好安静，想多待会儿"、"篝火真舒服"
- **信息类**: "原来沈家有旧部"、"青鸾未死？素问还活着？"
- **情感类**: "老兵眼眶红了"、"药剂师也是个有故事的人"

### 可改进方向（如果失败）
- **失败表现**: 平均对话 <3 人，停留 <5 分钟，>30% 玩家选"早睡"
- **可能原因**: 营地功能太弱（仅是休息），奖励不即时
- **改进**:
  1. 强制对话计数：离开营地前检查 `GS_CAMP_CONVERSATION_COUNT`，如果 <2，弹出提示："你确定不问问这些人吗？他们知道很多"
  2. 奖励前置：只要开始对话就给予小奖励（如老兵给符纹升级预览）
  3. 增加营地独特音效（吉他声、故事背景音）增强氛围

---

## 🎯 TP-09: 家谱理解度 (六残我与身份)

### 目标
验证 ≥80% 玩家理解"六残我"概念并意识到"我在其中"

### 触发条件
- 完成家谱调查三页 (`GS_FAMILY_REGISTRY_OBTAINED = true`)

### 关键变量
| 变量 | 说明 | 期望值 |
|------|------|--------|
| `GS_RESIDUE_IDENTITY_HINT` | 主角意识到自己与残我同源 | `true` |
| `GS_SIX_RESIDUES_KNOWN` | 知道有 6 个残我 | `true` |
| `GS_RESIDUE_MECHANISM_CLARIFIED_part1` | 理解集齐碎片才能完整 | `true` |

### 玩家行为验证
- [ ] 阅读全部 3 页（不跳过）
- [ ] 调查后主角内心独白提及"六人"或"我也是其中之一"
- [ ] 后续对话（如与谢临川复盘）提到"六残我"
- [ ] 打开背包查看家谱描述，复述关键句（如"等你回来"）

### 期望反馈词（证据）
- **震惊类**: "等等...这些名字里有我？" "我竟是其中之一！"
- **疑问类**: "所以残我想回来的是什么？" "九个归一是什么意思？"
- **动机类**: "我得集齐碎片" "深渊我必须去"

### 可改进方向（如果失败**
- **失败表现**: <80% 理解六残我，或许多玩家仍以为是"敌人"
- **可能原因**: 三页文案信息量过大，玩家漏看第二页名单
- **改进**:
  1. 增加第二页高亮边框，列出六人名字时逐个闪烁
  2. 阅读完第三页自动触发主角独白："六人...绮罗音、绯铃、宁素心...原来我身体里沉睡着他们。"
  3. 在家谱物品描述中 permanently highlight "六魂归位" 四个字

---

## 🎯 TP-10: 支线完成率 (Old Sanctuary + Fallen Scout)

### 目标
验证 ≥50% 玩家触发至少 3 个支线（从 4 个可用支线中）

### 可用支线清单
| 支线名称 | 触发条件 | 关键变量 |
|---------|---------|---------|
| 1. 老兵故事与祠堂祭拜 | 组队 + 听完老兵故事 | `GS_OLD_SANCTUARY_COMPLETED` |
| 2. Fallen Scout 身份 | 独行 或 救过谢临川 | `GS_SCOUT_IDENTITY_REVEALED` |
| 3. 药剂师馈赠与青鸾信息 | 与药剂师对话 | `GS_QINGLUAN_NOTE_OBTAINED` |
| 4. 谢临川深夜承诺 | 在队且 `GS_XIE_LIFESAVER = true` | `GS_XIE_PROMISE_FULL` |

### 玩家行为验证
- [ ] 统计上述 4 个变量中有多少为 `true`
- [ ] ≥3 个则为通过
- [ ] 记录玩家何时发现这些支线（如: "我在回营地路上看见一个祠堂"）
- [ ] 记录是否因选择不同（如独行）导致某些支线不可用

### 期望反馈词（证据）
- **情感类**: "老兵、药剂师、谢临川都有故事"、"这个游戏 NPC 不是摆设"
- **发现类**: "我居然错过了 Scout 那条线...下次一定要 triggering 它"
- **整体**: "支线是有血有肉的，不影響主线但让世界丰富"

### 可改进方向（如果失败**
- **失败表现**: <50% 玩家完成 ≥3 支线
- **可能原因**: 支线位置隐蔽、触发条件苛刻、玩家急于推进主线
- **改进**:
  1. 增加支线引导：在营地增加老兵提示"祠堂在那边"，Scout 尸体增加闪光提示
  2. 放宽触发：Old Sanctuary 无需组队，独行玩家也可以发现（老兵独自在祠堂）
  3. 奖励更即时：每个支线给 immediate buff（符纹、草药）让玩家立即感知价值
  4. 成就系统："沈家旧部"成就触发，提示"还有更多故事等待"

---

## 📊 QA 执行检查清单（手动 walkthrough）

### 测试前
- [ ] 游戏版本: commit `e14ea10` 或 later
- [ ] 变量监控面板: 显示 V10-V52 + GS_* 所有变量
- [ ] 测试设备: RPGMaker MZ desktop 或 mobile，调试模式开启
- [ ] 测试者: 3-5 名，未玩过此前版本

### 测试中（每名测试者）
#### Session 记录表

| 测试点 | 触发情况 | 变量值 | 玩家行为 | 玩家原话 | 通过? |
|--------|---------|--------|---------|---------|-------|
| TP-06 | □ 是 □ 否 | GS_SOLDIER_RESPECT_EARNED=__ |  |  | □ ✅ □ ❌ |
| TP-07 | □ 是 □ 否 | GS_XIE_LIFESAVER=__ |  |  | □ ✅ □ ❌ |
| TP-08 | □ 是 □ 否 | GS_CAMP_CONVERSATION_COUNT=__ |  |  | □ ✅ □ ❌ |
| TP-09 | □ 是 □ 否 | GS_RESIDUE_IDENTITY_HINT=__ |  |  | □ ✅ □ ❌ |
| TP-10 | □ 是 □ 否 | GS_OLD_SANCTUARY_COMPLETED=__, GS_SCOUT_IDENTITY_REVEALED=__ |  |  | □ ✅ □ ❌ |

**总通过率**: ___ / 5

#### 额外观察
- [ ] 玩家表情变化（大笑、皱眉、沉默）
- [ ] 停留时间（营地、祠堂）
- [ ] 重复行为（反复打开背包看符纹）

---

## 📎 附录 A: Playtest Feedback Table（完整版）

| 字段 | 说明 | 示例 |
|------|------|------|
| 测试点 ID | TP-06 等 | TP-06 |
| 场景 | 具体地点 | 营地→Old Sanctuary Shrine |
| 玩家行为 | 详细动作 | "与老兵对话 3 次，前往祠堂放置符纹" |
| 变量观测 | 最终值 | GS_SOLDIER_RESPECT_EARNED=true |
| 玩家原话 | 直接引用 | "这老兵有故事，符纹在跳！" |
| 情绪标记 | 😊/😲/😢/😠 | 😢（祠堂独白时） |
| 通过? | ✅/❌ | ✅ |
| 改进建议 | 如果失败 | "祠堂入口加光点引导" |

---

## 📎 附录 B: 变量全清单（Phase 3 新增）

| 变量名 | 用途 | 触发位置 |
|--------|------|---------|
| GS_RIFT_CLIMB_SUCCESS | 裂谷 QTE 成功 | M009 |
| GS_CAMP_FIRST_CHOICE | 营地优先对话 | M010 |
| GS_CAMP_FULL_DIALOGUE | 营地全对话 | M010 |
| GS_RESIDUE_TRIAL_COMPLETED | 残我试炼完成 | M016 中段 |
| GS_QINGLUAN_NOTE_OBTAINED | 获得素问纸条 | M016 右门 |
| GS_TRAP_SET | 设陷阱延迟黑衣人 | M016 (选 D) |
| GS_SOLDIER_RESPECT_EARNED | 祠堂祭拜完成 | Old Sanctuary |
| GS_OLD_SANCTUARY_COMPLETED | 旧 sanctuary 支线标志 | Old Sanctuary |
| GS_SCOUT_IDENTITY_REVEALED | Scout 身份揭露 | Fallen Scout |
| GS_HIDDEN_PROTECTORS_KNOWN | 暗卫真相已知 | Fallen Scout |
| GS_POST_COMBAT_REFLECTION | 战斗后独白已触发 | any combat end |

---

## 📎 附录 C: Task Receipt + Check-in Template

### Task Receipt (测试执行确认)

```
=== WRITER PHASE 3 PLAYTEST RECEIPT ===
Tester: ________________
Date: ________________
Build Version: ________________
Commit: ________________

Test Points Completed:
□ TP-06 老兵信任度 (Old Sanctuary)
□ TP-07 裂谷救援情感
□ TP-08 营地沉浸时长
□ TP-09 家谱理解度
□ TP-10 支线完成率

Total Pass Rate: ___ / 5

Issues Found:
1. ___________________________________
2. ___________________________________
3. ___________________________________

Feedback Keywords Collected:
- ___________________________________
- ___________________________________

Tester Signature: ________________
=========================================
```

### Check-in Template (每日进度报告)

```
=== WRITER PHASE 3 DAILY CHECK-IN ===
Date: 2026-03-XX
Session: ___ of ___

Tests Executed:
- TP-06: ___ passes / ___ attempts
- TP-07: ___ passes / ___ attempts
- TP-08: ___ passes / ___ attempts
- TP-09: ___ passes / ___ attempts
- TP-10: ___ passes / ___ attempts

Overall Pass Rate: ___%

Notable Player Quotes:
1. "__________________________________"
2. "__________________________________"
3. "__________________________________"

Critical Failures (Pass Rate <60%):
□ TP-06: ___
□ TP-07: ___
□ TP-08: ___
□ TP-09: ___
□ TP-10: ___

Action Items for Writer:
1. ___________________________________
2. ___________________________________
3. ___________________________________

Next Session Plan:
- Focus on: _______________________
- Expected improvements: ___________

=========================================
```

---

**文件状态**: Ready for QA Execution & Daily Reporting  
**关联**: `writer-phase3-narrative-extensions.md`, `playtest-points-lite.md`, `writer-release-summary.md`

---

**一句话指南**:
> "TP-06~TP-10 是 Line B 支线的情感验证：老兵祠堂的哽咽、裂谷救援的羁绊、营地的每句对话、家谱的自我认知、Scout 身份的震撼——每一个都有变量钩子和玩家原话证据，确保'有血有肉'不是空话。"
