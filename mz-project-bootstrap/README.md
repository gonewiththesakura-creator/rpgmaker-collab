# MZ Project Bootstrap (for 太玄界 Demo-Lite)

> 说明：当前仓库不包含真实 RPGMaker MZ 工程文件（无 `Game.rmmzproject`）。
> 本目录用于把“空白 MZ 工程”快速对齐到本项目的 demo-lite 流程。

## 目标
把你本地新建的空白 MZ 工程接入本仓库的执行体系：
- 剧本/技术任务文件
- day1/day2 操作手册
- 自动检查工具 `rpg_check.py`

## 你需要准备
在 RPGMaker MZ 中新建一个空白工程（任意名字），并确认工程目录包含：
- `Game.rmmzproject`
- `data/`
- `img/`
- `audio/`

## 快速接入步骤
1. 新建空白工程后，记住工程目录路径（例如 `/home/zero/Games/TaiXuan`）。
2. 运行检查工具（先看配置是否可识别）：
   ```bash
   python /home/zero/.openclaw/workspace/rpgmaker-collab/tools/rpg-cli/rpg_check.py consistency --project-path /home/zero/Games/TaiXuan
   ```
3. 按以下文档执行事件/地图搭建：
   - `rpg-project/demo-lite-v0.1-day1-manual-ops.md`
   - `rpg-project/day2-tech-ops-checklist.md`
4. 执行前后检查并保存报告：
   ```bash
   cd /home/zero/Games/TaiXuan
   python /home/zero/.openclaw/workspace/rpgmaker-collab/tools/rpg-cli/rpg_check.py consistency --project-path . > day2-before-consistency.json
   python /home/zero/.openclaw/workspace/rpgmaker-collab/tools/rpg-cli/rpg_check.py flow --profile demo-lite --project-path . > day2-before-flow.json

   # 按文档完成搭建后再跑
   python /home/zero/.openclaw/workspace/rpgmaker-collab/tools/rpg-cli/rpg_check.py consistency --project-path . > day2-after-consistency.json
   python /home/zero/.openclaw/workspace/rpgmaker-collab/tools/rpg-cli/rpg_check.py flow --profile demo-lite --project-path . > day2-after-flow.json
   ```

## 结果回传
将 4 份报告 + 试玩反馈交给监督节点：
- day2-before-consistency.json
- day2-before-flow.json
- day2-after-consistency.json
- day2-after-flow.json

## 后续
当基础 demo 跑通后，再进入：
- 占位素材替换
- 地图氛围精修
- 文案节奏迭代
