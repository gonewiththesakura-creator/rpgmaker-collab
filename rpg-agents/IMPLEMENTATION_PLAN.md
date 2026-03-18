# Implementation Plan - Supervisor + Writer + Tech

## 目标
在 Telegram 群里只保留一个“监督”机器人对外发言，后台由“剧本”和“技术”两个执行角色协作完成 RPGMaker 项目任务。

---

## 第一阶段：最小可行实现

### 对外
- 群里只有监督机器人响应
- 群里需要 @ 监督 才触发

### 对内
- 剧本 agent：负责叙事与文案
- 技术 agent：负责 RPGMaker 实现与系统设计

### 初始路由规则
- 剧情 / 世界观 / 对话 / 人设 → 剧本
- 插件 / 开关 / 变量 / 事件 / 地图 / UI → 技术
- 混合任务 → 同时调用剧本 + 技术，监督整合

---

## 第二阶段：固定角色 Session

建议为以下角色建立长期 session：
- supervisor-main（主会话 / 群入口）
- writer-rpg-agent
- tech-rpg-agent

这样角色会有连续上下文，而不是每次临时从零开始。

---

## 第三阶段：项目记忆与进度

建议补充：
- `rpg-project/progress.md`
- `rpg-project/feature-list.json`
- `rpg-project/world-bible.md`
- `rpg-project/tech-architecture.md`

其中：
- 剧本主要维护世界观、剧情结构类文档
- 技术主要维护实现结构类文档
- 监督维护进度与优先级

---

## 监督实际运行流程

1. 接收群消息
2. 判断任务类型
3. 调用 writer / tech
4. 审核并整合结果
5. 输出最终回复
6. 必要时更新项目文档

---

## 注意事项

- 不要让 writer 和 tech 直接在群里对话
- 不要让执行角色自己拍板项目方向
- 不要让混合任务只由单一角色回答
- 所有最终对外意见必须经过监督整合
