# Agent Harness Summary

## Purpose
Capture lessons from Anthropic's "Effective harnesses" post and apply them to our Phase 3 long-running flow. The key idea is to make each session self-sufficient while leaving structured progress for the next one.

## Harness Components
1. **Initializer setup**
   - On first run: create `init.sh` (tools/start script), `progress.txt` (log of work), and `feature_list.json` (step-by-step spec).
   - These files live in `/rpg-project/framework/` and are referenced by every subsequent session.

2. **Session routine**
   - Begin by running `pwd`, reading `progress.txt`, checking git log, and reviewing `feature_list.json`.
   - Run `./init.sh` once to bring the dev server or toolchain up.
   - Choose the highest-priority incomplete feature (status=false) from `feature_list.json` and work on it incrementally.
   - Before ending the session, run a basic verification (play through target flow, run `openclaw doctor`,`python rpg-cli/consistency`, etc.).
   - Commit with descriptive message and append to `progress.txt` references to what was done.

3. **Feature list format (JSON)**
   - Each entry: category, description, steps, `passes` boolean.
   - Agents only update `passes` to true when the feature passes end-to-end testing.
   - Never delete entries; adding new ones allowed but older specs stay for history.

4. **Testing discipline**
   - Integration-style tests (manual walkthrough, scripts) must run after each feature completion.
   - Capture results (pass/fail, logs) in `progress.txt` so the next agent can inspect fresh status.

## Application to TaiXuanDemo
- We maintain `phase3-progress.txt`, `phase3-feature-list.json`, and `phase3-init.sh` derived from Phase 3 requirements.
- Each session I supervise follows the harness: get bearings → pick best feature (map, event, narrative) → implement → run checks → document & commit progress.
- This makes our multi-session RPG construction reliable and traceable.

## Next steps
- Keep updating `phase3-feature-list.json` with fine-grained tasks (map design, dialogue, assets). 
- Ensure `phase3-progress.txt` logs every release candidate and test result. 
- Every agent (A, B, or me) follows the routine so that even if you rest, the project still moves toward the 1-hour playable chapter.
