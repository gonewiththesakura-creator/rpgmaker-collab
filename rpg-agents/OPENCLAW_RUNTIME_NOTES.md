# OpenClaw Runtime Notes for RPG Agent Collaboration

## Current limitation
In the current OpenClaw runtime, persistent subagent sessions are not available because:
- `mode="session"` requires `thread=true`
- current channel/runtime does not expose the thread-bound spawning hook needed for persistent subagent sessions

## Practical implication
The ideal architecture is:
- Supervisor as the external speaker
- Persistent Writer session
- Persistent Tech session

However, **right now the executable version must use one-shot subagents** rather than persistent thread-bound sessions.

## Current workable architecture
- Supervisor = main Telegram/OpenClaw assistant
- Writer = spawned one-shot subagent using WRITER_PROMPT.md
- Tech = spawned one-shot subagent using TECH_PROMPT.md
- Supervisor integrates both outputs and replies externally

## Upgrade path later
When runtime supports persistent session spawning:
1. Create `writer-rpg-agent` as a true session
2. Create `tech-rpg-agent` as a true session
3. Reuse them with `sessions_send`
4. Keep Supervisor as the only outward-facing bot

## Conclusion
The design is valid. The current runtime just constrains the implementation to one-shot role agents for now.
