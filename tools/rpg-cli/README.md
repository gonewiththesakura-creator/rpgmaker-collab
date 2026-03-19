# RPG-CLI Tools

RPGMaker MZ Project Checker - MVP Version

## Overview

Minimal checking tool for RPGMaker MZ projects, designed for the "太玄界" RPG project.

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
- Map existence (M001, M002, M003)
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
  "overallStatus": "PASS|FAIL",
  "checks": [
    {
      "checkName": "Map Existence Check",
      "status": "PASS",
      "errors": [],
      "warnings": [],
      "timestamp": "2026-03-19T10:30:00"
    }
  ],
  "timestamp": "2026-03-19T10:30:00"
}
```

## Exit Codes

- `0`: All checks passed
- `1`: One or more checks failed

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

## MVP Scope (Locked)

**Included:**
- Basic consistency checks
- Demo-lite flow validation
- JSON output
- Command-line interface

**Excluded (for now):**
- SKILL.md integration
- REPL mode
- Multi-platform support
- Full 7-phase pipeline

## Usage Examples

### Check consistency

```bash
$ python tools/rpg-cli/rpg_check.py consistency
{
  "checkSuite": "consistency",
  "overallStatus": "PASS",
  "checks": [...]
}
```

### Check flow

```bash
$ python tools/rpg-cli/rpg_check.py flow --profile demo-lite
{
  "checkSuite": "flow",
  "overallStatus": "PASS",
  "checks": [...]
}
```

### Custom project path

```bash
$ python tools/rpg-cli/rpg_check.py consistency --project-path /path/to/project
```

## Development

### Adding New Checks

1. Extend `RPGChecker` base class
2. Implement check method
3. Add to `run_all()` method
4. Update this README

### Testing

Run against a real RPGMaker MZ project:

```bash
cd /path/to/rpgmaker-project
python /path/to/rpg_check.py consistency
```

## License

Part of 太玄界 RPG Project
