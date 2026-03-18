# RPG Task Schema

This file defines the JSON task format for three-machine collaboration.

## Core idea
- Supervisor writes tasks into `todo.json`
- Writer node only picks `type = writer` or `type = mixed`
- Tech node only picks `type = tech` or `type = mixed`
- Claimed tasks move to `in-progress.json`
- Finished tasks move to `done.json`

## Task object

```json
{
  "id": "task-001",
  "type": "writer | tech | mixed",
  "title": "Short title",
  "status": "todo | in-progress | done",
  "assignedTo": "supervisor | writer-node | tech-node | null",
  "createdBy": "supervisor",
  "priority": "low | medium | high",
  "description": "Detailed task description",
  "acceptance": ["Acceptance criterion 1", "Acceptance criterion 2"],
  "notes": ["optional notes"]
}
```

## Rules
- Only Supervisor creates tasks.
- Writer node should not claim `tech` tasks.
- Tech node should not claim `writer` tasks.
- `mixed` tasks require both writer and tech input before supervisor closes them.
- Do not delete tasks just because they are inconvenient; move them through queues.
