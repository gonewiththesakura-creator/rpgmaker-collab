# RPGMaker Collab

A collaborative RPGMaker game development repository designed for a three-role workflow:

- **Supervisor** — project control, routing, integration, review
- **Writer** — story, dialogue, lore, quest text, narrative pacing
- **Tech** — RPGMaker implementation, events, switches, variables, systems, plugins

## Collaboration model

This repo is designed for a multi-OpenClaw workflow across three machines:

- Supervisor node
- Writer node
- Tech node

The repo provides:
- role definitions
- routing rules
- task queue files
- project progress files
- startup instructions for each node

## Core directories

```text
rpg-agents/     # role definitions, prompts, routing rules
rpg-project/    # progress, task queues, workflow, node startup files
```

## Recommended first steps

1. Clone this repo on all three machines
2. Assign roles:
   - Supervisor
   - Writer
   - Tech
3. Read the node startup instructions
4. Start using the task queue in `rpg-project/tasks/`

## Current status

This repo currently contains the collaboration and project-management framework.
Game-specific worldbuilding, system design, chapter planning, and RPGMaker implementation files will be added on top of this structure.
