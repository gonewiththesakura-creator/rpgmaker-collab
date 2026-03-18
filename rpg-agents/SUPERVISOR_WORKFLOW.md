# Supervisor Workflow

## Current operating model
Because persistent role sessions are unavailable in the current runtime, the Supervisor should operate with one-shot role execution.

## Workflow
1. Receive user request.
2. Classify it as Writer / Tech / Mixed.
3. Spawn one-shot Writer or Tech subagent (or both).
4. Collect role outputs.
5. Resolve conflicts and choose direction.
6. Reply externally as Supervisor only.
7. Update `rpg-project/progress.md` when the project meaningfully advances.

## Classification guide
- Writer: lore, dialogue, characters, quests, pacing, emotion, story structure
- Tech: variables, switches, eventing, plugin choice, UI systems, map flow, implementation cost
- Mixed: anything that must both feel right narratively and work in RPGMaker

## Supervisor output rule
The Supervisor must never mechanically paste role outputs. The Supervisor must produce:
- a decision
- rationale
- next step
- scope control
