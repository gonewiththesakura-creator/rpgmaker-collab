# 3-Node Collaboration Workflow

## Goal
Coordinate three OpenClaw instances as:
- Supervisor
- Writer
- Tech

## Workflow
1. Supervisor receives a request.
2. Supervisor classifies the task:
   - writer
   - tech
   - mixed
3. Supervisor creates a task in `tasks/todo.json`.
4. Writer or Tech node claims task by moving it to `tasks/in-progress.json` and setting `assignedTo`.
5. The node writes its output into task `notes` or companion files.
6. If mixed, both nodes contribute.
7. Supervisor reviews outputs.
8. Supervisor either:
   - sends task back for revision, or
   - moves it to `tasks/done.json`
9. Supervisor updates `progress.md`.

## Practical implementation notes
- In the current environment, this can begin as a manual/shared-file protocol.
- Later, it can be upgraded to automatic polling or API-based task claiming.
- Git commits should be used to preserve task history and roll back bad changes.
