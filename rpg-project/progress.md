# RPG Project Progress

Last updated: 2026-03-18

## Current collaboration model
- Supervisor: external speaker and project controller
- Writer: narrative execution role
- Tech: RPGMaker implementation role

## Current state
The role system has now been defined at the documentation level.
Because the current OpenClaw runtime does not support persistent thread-bound subagent sessions here, the practical implementation for now is:
- Supervisor as the only outward-facing bot
- Writer and Tech invoked as one-shot subagents per task
- Supervisor integrates outputs and responds

## Immediate next steps
1. Use the role docs in real tasks.
2. Spawn Writer one-shot subagents for narrative requests.
3. Spawn Tech one-shot subagents for implementation requests.
4. For mixed requests, call both and synthesize.
5. Upgrade to persistent role sessions later if runtime support becomes available.

## Active files
- `rpg-agents/AGENT_ROLES.md`
- `rpg-agents/ROUTING_RULES.md`
- `rpg-agents/SUPERVISOR_PROMPT.md`
- `rpg-agents/WRITER_PROMPT.md`
- `rpg-agents/TECH_PROMPT.md`
- `rpg-agents/IMPLEMENTATION_PLAN.md`
- `rpg-agents/OPENCLAW_RUNTIME_NOTES.md`
- `rpg-agents/TASK_TEMPLATES.md`
- `rpg-agents/SUPERVISOR_WORKFLOW.md`

## Notes
This is now a usable architecture, even though it is not yet the ideal persistent-session version.
