# Node Assignments

This file defines the recommended role of each OpenClaw machine in the 3-node setup.

## Node 1 — Supervisor (main control node)
Responsibilities:
- Receive user requests
- Decide routing
- Create tasks in `rpg-project/tasks/todo.json`
- Review outputs from writer and tech nodes
- Maintain `rpg-project/progress.md`
- Produce final external replies

## Node 2 — Writer node
Responsibilities:
- Claim writer or mixed tasks
- Produce narrative design output
- Update task notes with story proposals
- Never make final project decisions

## Node 3 — Tech node
Responsibilities:
- Claim tech or mixed tasks
- Produce RPGMaker implementation plans
- Update task notes with implementation details
- Never change narrative direction on its own

## Important rule
Only the Supervisor closes a task as done.
