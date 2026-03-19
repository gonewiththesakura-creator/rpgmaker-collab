# RPG-CLI Tools v0.1

RPGMaker MZ Project Checker - Fixed Version

## Overview

Minimal checking tool for RPGMaker MZ projects, designed for the "太玄界" RPG project.

**Version**: v0.1 (Fixed)  
**Changes**: Map naming unified, resultType added, CONFIG_ERROR handling

## Installation

No installation required. Just ensure Python 3.8+ is available.

```bash
cd tools/rpg-cli
python rpg_check.py --help
```

## Commands

### 1. Consistency Check

Verify project structure and required assets:

```bash
python rpg_check.py consistency
```

**Checks:**
- Map existence (Map001.json, Map002.json, Map003.json)
- Key events existence
- Switches/variables configuration
- Key items existence (残破家谱, etc.)

**Output:** `rpg-project/reports/consistency-report.json`

### 2. Flow Check

Verify demo flow for specific profile:

```bash
python rpg_check.py flow --profile demo-lite
```

**Checks:**
- Demo main chain reachability
- Ch3 unlosable battle configuration
- Genealogy item obtainable after retreat
- Ch4 hook markers

**Output:** `rpg-project/reports/flow-report.json`

## Output Format

All checks output JSON with the following structure:

```json
{
  "checkSuite": "consistency",
  "resultType": "PASS",
  "overallStatus": "PASS",
  "checks": [
    {
      "checkName": "Map Existence Check",
      "status": "PASS",
      "resultType": "PASS",
      "errors": [],
      "warnings": [],
      "hint": "",
      "timestamp": "2026-03-19T10:30:00"
    }
  ],
  "timestamp": "2026-03-19T10:30:00"
}
```

### Result Types

| resultType | Meaning | Exit Code |
|-----------|---------|-----------|
| `PASS` | All checks passed | 0 |
| `CHECK_FAIL` | Data exists but check failed | 1 |
| `CONFIG_ERROR` | Project structure invalid | 1 |

### Error Handling

**CONFIG_ERROR with hint:**

```json
{
  "checkSuite": "consistency",
  "resultType": "CONFIG_ERROR",
  "overallStatus": "FAIL",
  "error": "Data directory not found",
  "hint": "请将 --project-path 指向 RPGMaker MZ 工程根目录（应包含 data/ 子目录）",
  "timestamp": "2026-03-19T10:30:00"
}
```

## Map Naming Convention

This tool uses RPGMaker MZ standard naming:

- Map 1 → `Map001.json`
- Map 2 → `Map002.json`
- Map 3 → `Map003.json`

**Note**: The tool only recognizes this format. Do not use `M001.json` or `MapM001.json`.

## Project Structure

```
rpgmaker-collab/
├── tools/
│   └── rpg-cli/
│       ├── rpg_check.py      # Main checker
│       └── README.md         # This file
└── rpg-project/
    └── reports/              # Output directory
        ├── consistency-report.json
        └── flow-report.json
```

## Usage Examples

### Check consistency (current directory)

```bash
$ python tools/rpg-cli/rpg_check.py consistency
{
  "checkSuite": "consistency",
  "resultType": "PASS",
  "overallStatus": "PASS",
  "checks": [...]
}
```

### Check flow

```bash
$ python tools/rpg-cli/rpg_check.py flow --profile demo-lite
{
  "checkSuite": "flow",
  "resultType": "PASS",
  "overallStatus": "PASS",
  "checks": [...]
}
```

### Custom project path

```bash
$ python tools/rpg-cli/rpg_check.py consistency --project-path /path/to/project
```

### CONFIG_ERROR example (wrong path)

```bash
$ python tools/rpg-cli/rpg_check.py consistency --project-path /wrong/path
{
  "checkSuite": "consistency",
  "resultType": "CONFIG_ERROR",
  "overallStatus": "FAIL",
  "error": "Data directory not found: /wrong/path/data",
  "hint": "请将 --project-path 指向 RPGMaker MZ 工程根目录（应包含 data/ 子目录）",
  "timestamp": "2026-03-19T10:30:00"
}
```

## MVP Scope (Locked)

**Included:**
- Basic consistency checks
- Demo-lite flow validation
- JSON output with resultType
- CONFIG_ERROR handling with hints
- Command-line interface

**Excluded (for now):**
- SKILL.md integration
- REPL mode
- Multi-platform support
- Full 7-phase pipeline

## Exit Codes

- `0`: PASS (all checks passed)
- `1`: CHECK_FAIL or CONFIG_ERROR

## Development

### Adding New Checks

1. Extend `RPGChecker` base class
2. Return `CheckResult` with proper `resultType`
3. Add to `run_all()` method
4. Update this README

### Testing

Run against a real RPGMaker MZ project:

```bash
cd /path/to/rpgmaker-project
python /path/to/rpg_check.py consistency
```

## Changelog

### v0.1 (Fixed)
- Fixed: Map naming unified to `Map001.json` format
- Fixed: PASS/FAIL logic - errors now correctly result in CHECK_FAIL
- Added: CONFIG_ERROR result type for project structure issues
- Added: `hint` field for configuration error guidance
- Added: `resultType` field in all outputs

### v0.0 (Initial)
- Basic consistency checks
- Flow checks for demo-lite
- JSON output

## License

Part of 太玄界 RPG Project
