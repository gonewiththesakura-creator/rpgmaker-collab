# AI_PIPELINE_V0.md

**AI Pipeline Version**: v0 (MVP)  
**Project**: 太玄界 RPG  
**Tool**: rpg_check.py  
**Date**: 2026-03-19

---

## Overview

This document defines the minimal AI-assisted checking pipeline for the RPGMaker MZ project.

**Goal**: Provide automated validation of project consistency and demo flow, enabling rapid iteration and quality assurance.

---

## Pipeline Architecture

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  RPGMaker MZ    │────▶│   rpg_check.py  │────▶│  JSON Reports   │
│   Project       │     │   (CLI Tool)    │     │  (Machine       │
│                 │     │                 │     │   Readable)     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                                              │
        │                                              ▼
        │                                       ┌─────────────────┐
        │                                       │  AI Agent /     │
        │                                       │  Supervisor     │
        │                                       │  Review         │
        │                                       └─────────────────┘
        │                                              │
        ▼                                              ▼
┌─────────────────┐                           ┌─────────────────┐
│  Manual Fix     │◀──────────────────────────│  Feedback Loop  │
│  in Editor      │                           │                 │
└─────────────────┘                           └─────────────────┘
```

---

## Stage 1: Consistency Check

**Purpose**: Verify project structure is complete and valid.

**When to Run**:
- After adding new maps
- After modifying database (switches, variables, items)
- Before committing changes

**Command**:
```bash
python tools/rpg-cli/rpg_check.py consistency
```

**Checks**:

| Check | Description | Critical |
|-------|-------------|----------|
| Map Existence | M001, M002, M003 exist | Yes |
| Key Events | Core events present in maps | Yes |
| Switches | Required switches named | Yes |
| Variables | Required variables named | Yes |
| Items | 残破家谱 and other key items exist | Yes |

**Output**: `rpg-project/reports/consistency-report.json`

**Success Criteria**:
- `overallStatus` == "PASS"
- All critical checks pass
- No errors in `errors` array

---

## Stage 2: Flow Check

**Purpose**: Verify demo flow is correctly implemented.

**When to Run**:
- After implementing events
- After modifying battle/troop configurations
- Before milestone review

**Command**:
```bash
python tools/rpg-cli/rpg_check.py flow --profile demo-lite
```

**Checks**:

| Check | Description | Critical |
|-------|-------------|----------|
| Demo Chain | Main flow nodes reachable | Yes |
| Unlosable Battle | Ch3 battle has HP/turn threshold | Yes |
| Genealogy Obtainable | 残破家谱 given after retreat | Yes |
| Ch4 Hook | Hook markers exist | No (warning) |

**Output**: `rpg-project/reports/flow-report.json`

**Success Criteria**:
- `overallStatus` == "PASS"
- All critical checks pass
- Ch4 hook may warn (optional for demo-lite)

---

## Integration with Development Workflow

### Pre-Commit Check

```bash
# Before committing changes
python tools/rpg-cli/rpg_check.py consistency

# If PASS, proceed with commit
# If FAIL, fix issues first
```

### Pre-Milestone Check

```bash
# Before milestone review
python tools/rpg-cli/rpg_check.py consistency
python tools/rpg-cli/rpg_check.py flow --profile demo-lite

# Both must PASS for milestone acceptance
```

### CI Integration (Future)

```yaml
# .github/workflows/check.yml (for future implementation)
name: RPG Check
on: [push, pull_request]
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Consistency Check
        run: python tools/rpg-cli/rpg_check.py consistency
      - name: Flow Check
        run: python tools/rpg-cli/rpg_check.py flow --profile demo-lite
```

---

## Report Interpretation

### PASS Status

```json
{
  "overallStatus": "PASS",
  "checks": [...]
}
```

**Action**: Proceed with development or commit.

### FAIL Status

```json
{
  "overallStatus": "FAIL",
  "checks": [
    {
      "status": "FAIL",
      "errors": ["Missing map: Map003.json"]
    }
  ]
}
```

**Action**: Fix listed errors, re-run check.

### Common Issues and Fixes

| Issue | Fix |
|-------|-----|
| Missing map | Create map in RPGMaker MZ |
| Missing event | Add event to map |
| Missing switch | Add switch name in System database |
| Missing item | Create item in Items database |
| Unlosable battle not configured | Add Troop Event with HP/turn threshold |

---

## Extending the Pipeline

### Adding New Checks (v1+)

1. **Identify need**: What validation is missing?
2. **Implement check**: Add method to checker class
3. **Add to suite**: Include in `run_all()` method
4. **Update docs**: Document in this file
5. **Test**: Verify against real project

### Future Profiles

- `demo-full`: Full demo checks
- `chapter-1`: Chapter 1 specific
- `release`: Pre-release validation

---

## Limitations (v0)

**Known Limitations**:
- Cannot check event content details (only existence)
- Cannot verify battle balance
- Cannot check visual/audio assets
- No automatic fix suggestions

**Workarounds**:
- Manual review for event content
- Playtesting for battle balance
- Separate asset checklist

---

## Success Metrics

**v0 Success**:
- [x] Tool runs without errors
- [x] Consistency check validates project structure
- [x] Flow check validates demo-lite profile
- [x] JSON output is machine-readable
- [x] Reports are useful for debugging

**v1+ Goals**:
- [ ] Automatic fix suggestions
- [ ] More detailed event content checks
- [ ] Integration with OpenClaw SKILL.md
- [ ] CI/CD pipeline integration

---

## Quick Reference

### Commands

```bash
# Consistency check
python tools/rpg-cli/rpg_check.py consistency

# Flow check
python tools/rpg-cli/rpg_check.py flow --profile demo-lite

# Custom project path
python tools/rpg-cli/rpg_check.py consistency --project-path /path/to/project

# Custom output
python tools/rpg-cli/rpg_check.py consistency --output /custom/path/report.json
```

### Exit Codes

- `0`: All checks passed
- `1`: One or more checks failed

### Report Locations

- Consistency: `rpg-project/reports/consistency-report.json`
- Flow: `rpg-project/reports/flow-report.json`

---

**Status**: Ready for Supervisor Check  
**Next Step**: Run against actual project, iterate based on feedback
