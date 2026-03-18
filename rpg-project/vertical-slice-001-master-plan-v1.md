# vertical-slice-001-master-plan-v1

Date: 2026-03-18
Based on:
- `rpg-project/vertical-slice-001-supervisor-v1.md`
- `rpg-project/vertical-slice-001-writer-plan-v1.md` (B, reviewed)
- `rpg-project/vertical-slice-001-tech-plan-v1.md` (A, reviewed)

## Master decision
Approved for execution.

## Scope lock (must not expand)
- Engine: RPGMaker MZ
- Chapters: Ch1~Ch4 only
- Core cast (6): 沈照璃 / 谢临川 / 素问真人 / 宗门师尊 / 黑衣人 / 绮罗音(遭遇态)
- No full multi-loop inheritance system
- No full residue-boss framework
- No heavy plugin-first redesign

## Unified chapter flow
1. Ch1 宗门日常与入门异常
2. Ch2 试炼推进与关系加压
3. Ch3 古碑线索与表层冲突（黑衣人）
4. Ch4 深渊入口与残我首次遭遇（绮罗音）

## Technical execution baseline (A adopted)
- Maps: 8
- Core events: ~40
- Core variables/switches: 28
- Xie mechanism: **方案B 剧情同行**
- Qiluo mechanism: **遭遇 + 选择 + 结果标记** only
- Key item: `残破家谱` with `九劫归一` foreshadowing

## Writer baseline (B adopted)
- Keep 1st-loop surface narrative intact
- Ch3 conflict is the visible climax
- Ch4 must end with a strong continuation hook
- Truth-layer remains mostly hidden (no early spoil)

## Acceptance criteria
- Ch1~Ch4 playable end-to-end
- Ch3 contains explicit black-clothed antagonist confrontation
- Ch4 contains Qiluo encounter + meaningful choice + hook
- Event/asset scope stays within low-cost MZ bounds

## Immediate next tasks
1. A: `vertical-slice-001-tech-implementation-tasks-v1.md`
2. B: `vertical-slice-001-writer-scene-script-v1.md`
3. Supervisor: merge both into sprint checklist and set milestone gates

## Milestones
- M1: Ch1~Ch2 playable
- M2: Ch3 conflict + genealogy item complete
- M3: Ch4 Qiluo encounter + ending hook complete
- M4: full Ch1~Ch4 regression pass
