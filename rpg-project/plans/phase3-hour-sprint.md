# Phase 3 Hour Sprint

**Objective (next 1h)**
Deliver a mini second chapter slice that feels like a `real RPG`—rich maps, purposeful placement, emotional narrative with living detail, and 1~2 meaningful side paths. Focus on quality over quantity; no random clutter.

## 1. Map Suite (M004–M006)
Each map follows the 3-area/3-layer principle (main path, interaction nodes, blocking/atmosphere) with precise design intent.

| Map | Purpose | Focus | Notable Elements |
| --- | ------- | ----- | ---------------- |
| M004_HillGate | Entry to the back mountain / set up tension | Front path, a hidden shrine, overlooking ledge, gathering point | Stone gate, lantern-lined stairs, wisp-lit herbal table, NPC “Old Scout” (introduces branch).|
| M005_AncientTrail | Transition space with environmental storytelling | Narrow ravine path, ruins, vantage point archetype | Cracked bridge, broken column, mural telling of the fallen, optional loot cabin with encoded note.|
| M006_CampCliff | Cliffside camp / mini climax | Threat-friendly staging area, campfire, exit hook visual cue | Tent cluster, cresting winds, cliff-edge glow, trailing rope ladder, decision lantern guiding exit.

Details for each map include: 
- Visual focus (landmarks and light). 
- Player path (steps from start to key event). 
- Interaction nodes (NPC or investigable objects). 
- Optional branch trigger (supports one of the new side paths).

## 2. Narrative & Text (Ch2 sequence)
Write three immersive text beats: 
1. **Opening** (M004, Old Scout) – Reaffirm the mission, hint about the missing shard, include emotional tone (“Your family name is still blood-warm.”). 
2. **Midpoint** (M005, Trail mural) – Provide lore-rich exposition via environmental text + NPC aside (“We lost a patrol to that wind.”) 
3. **Cliff camp** (M006) – After reaching camp, present emotional dialog (“I thought you’d never return.”) and transition to next goal.

Include signal cues (Wind4, heartbeat, soft chime) and direct connectors to variables/switches (e.g., `SW_ROAD_SHARD_HINT`, `VAR_EMOTIONAL_STATE`). Ensure each text block is actionable in MZ events.

## 3. Side Paths
1. **Old Gate Shrine Side Path** (M004) – Investigate hidden altar by activating three lanterns (`LANTERN_LIT_1` etc.). Success grants `Shattered Sigil` (Combat token + lore snippet) and sets `SW_SHRINE_SOLVED=true`. Rewards text: “The sigil hums like a heart.”
2. **Fallen Scout Remnant** (M005) – Find abandoned journal and deliver to NPC. The NPC offers a faded map piece showing a hidden crossing (opens a minor shortcut). Triggered switch `SW_SCOUT_JOURNAL=1`. Dialogue should be human, emotional, referencing “you are still the promising child I once trained.”

Both branches have clear conditions, text, and rewards. Document the triggers, player feedback, and how they feed into the broader emotional arc.

## 4. Documentation Outputs
- `phase3-hour-sprint.md` (this doc) shared for visibility. 
- Additional deliverables to produce soon:
  * Map layouts (Map004-006) plus event IDs in `data/Map00X.json`.
  * Narrative text entries, referenced switches/variables.
  * Side path event definitions.
  * Updated `phase2-v2-exit-hook` if needed to tie into chapter 2.

## 5. Supervisory Notes
I keep the “I know what the game should feel like” promise by orchestrating each element: maps have intention, text has heart, side quests support the theme, and the whole 1-2 hour sprint is packaged for QA/Release. I'll monitor progress, gather evidence, and report back with the new assets once ready.
