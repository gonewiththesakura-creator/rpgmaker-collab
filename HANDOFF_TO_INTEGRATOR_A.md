# Handoff: Zero2 Design Package to Integrator A

**From**: Writer B (小爱)  
**To**: Integrator A  
**Date**: 2026-03-20  
**Task**: zero2-design-v1 — Map Training Cross-Discipline  
**Status**: Ready for Integrator A

---

## 📦 交付内容

以下 3 个文件构成完整的 zero2 地图设计包（v1），位于 **rpgmaker-collab** 仓库：

| 文件 | 路径 | 说明 |
|------|------|------|
| `zero2-study-notes-v1.md` | `rpg-project/zero2-study-notes-v1.md` | 7 参考学习提炼，21 条方法 |
| `zero2-world-logic-v1.md` | `rpg-project/zero2-world-logic-v1.md` | 世界逻辑三问（地点/布局/禁忌） |
| `zero2-map-design-v1.md` | `rpg-project/zero2-map-design-v1.md` | 地图设计 spec（10 条要求 + ASCII 草图） |

**Git 引用**:
- **Commit**: `4887a0e`
- **GitHub**: https://github.com/gonewiththesakura-creator/rpgmaker-collab/commit/4887a0e
- **分支**: main

---

## 🎯 A 的执行指令

### 1. 获取设计包
```bash
# 进入 rpgmaker-collab 仓库（如果 A 有只读访问）
cd /path/to/rpgmaker-collab
git pull origin main

# 或直接下载单个文件
# 例如: https://github.com/gonewiththesakura-creator/rpgmaker-collab/blob/main/rpg-project/zero2-map-design-v1.md
```

### 2. 读取 `zero2-map-design-v1.md`
这是**直接可实施的设计规格**，包含：
- 地图尺寸 (75x50)
- 中轴布局 (3 tiles 宽)
- 主殿位置 (北端高台)
- 前庭元素 (香炉+石碑)
- 左右区功能 (练武场 vs 公告墙)
- 地标清单
- 该放/不该放元素
- ASCII 草图

### 3. 在 TaiXuanDemo-day2-node-c 中实装 `zero2-implementation-v1`

**步骤**:
1. 打开 RPGMaker MZ，创建新地图（或编辑现有宗门广场）
2. 按照 `zero2-map-design-v1.md` 的坐标和 tile 清单铺设
3. 按照 `zero2-world-logic-v1.md` 的逻辑检查（功能分区、视线通廊等）
4. 参考 `zero2-study-notes-v1.md` 的设计原则微调
5. 完成后导出截图至 `phase3_screenshots/zero2_after.png`（在 TaiXuanDemo-day2-node-c 中）

**不要求**:
- ❌ 写剧情文案（Writer 后续会补充）
- ❌ 做复杂事件（仅基础地图铺设）
- ❌ 改变设计逻辑（严格按 spec）

---

## 📊 设计包关键指标（快速预览）

| 指标 | 值 |
|------|------|
| 地图尺寸 | 75 x 50 tiles |
| 中轴宽度 | 3 tiles |
| 主殿高度 | 高台 +2 tiles |
| 功能区 | 3（入口/过渡/核心） |
| 视觉焦点 | 主殿 + 香炉 + 石碑 |
| 装饰套装 | 石狮、灯柱、香炉、石碑、兵器架、沙袋、公告板 |
| 屋顶层级 | 歇山顶（主殿） vs 硬山顶（辅助） |
| 色彩方案 | 主殿红金，辅助灰白，地砖青灰 |

---

## 🔄 工作流

```
Writer B (rpgmaker-collab)  →  Handoff 本文件  →  Integrator A (TaiXuanDemo-day2-node-c)
    ↓ 设计包已交付                    ↓ 读取设计包
    ↓ 等待反馈                        ↓ 按 spec 实装地图
    ↑ QA Playtest 结果                ↑ 截图反馈
    ↓ 如需 polish，v2 精修             ↓ 提交 `zero2_after.png`
```

---

## ✅ 交付检查

- ✅ `zero2-study-notes-v1.md` 已存在（rpgmaker-collab）
- ✅ `zero2-world-logic-v1.md` 已存在（rpgmaker-collab）
- ✅ `zero2-map-design-v1.md` 已存在（rpgmaker-collab）
- ✅ Git commit `4887a0e` 包含全部文件
- ✅ 本 Handoff 文件已添加并推送

---

## 📬 给 A 的话

这是你的地图训练任务 spec。请不要重新设计或发挥——严格按照 `zero2-map-design-v1.md` 执行。如果 spec 有模糊处，先按 `zero2-study-notes-v1.md` 的设计原则（主路、主殿、焦点、禁忌）处理，不确定的地方在截图时标注，后续 Writer 会调整文案而非改结构。

目标是做出一个"一眼看出主路、主殿、焦点区、宗门气质"的广场，而不是创意实验。

Good luck!

---

**状态**: Ready for Integrator A

---

## 📁 文件位置总结

```
rpgmaker-collab/
└── rpg-project/
    ├── zero2-study-notes-v1.md
    ├── zero2-world-logic-v1.md
    ├── zero2-map-design-v1.md
    └── HANDOFF_TO_INTEGRATOR_A.md (本文件)
```

**A 的工作仓库**: `TaiXuanDemo-day2-node-c`  
**A 的输出**: `zero2-implementation-v1` + `phase3_screenshots/zero2_after.png`
