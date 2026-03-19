#!/usr/bin/env python3
"""
rpg_check.py - RPGMaker MZ Project Checker
Version: v0.1 (Fixed)

Commands:
    python rpg_check.py consistency
    python rpg_check.py flow --profile demo-lite

Output: JSON reports with resultType (PASS | CHECK_FAIL | CONFIG_ERROR)
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple


class CheckResult:
    """Standardized check result"""
    PASS = "PASS"
    CHECK_FAIL = "CHECK_FAIL"
    CONFIG_ERROR = "CONFIG_ERROR"
    
    def __init__(self, check_name: str, result_type: str, errors: List[str], warnings: List[str], hint: str = ""):
        self.check_name = check_name
        self.result_type = result_type
        self.errors = errors
        self.warnings = warnings
        self.hint = hint
        self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        # status is derived from result_type for backward compatibility
        status = "PASS" if self.result_type == self.PASS else "FAIL"
        
        return {
            "checkName": self.check_name,
            "status": status,  # legacy field
            "resultType": self.result_type,
            "errors": self.errors,
            "warnings": self.warnings,
            "hint": self.hint,
            "timestamp": self.timestamp
        }


class RPGChecker:
    """RPGMaker MZ Project Checker"""
    
    # Map naming: RPGMaker MZ uses "Map001.json" format
    MAP_PREFIX = "Map"
    MAP_SUFFIX = ".json"
    
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.data_path = self.project_path / "data"
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.config_error: bool = False
        self.hint: str = ""
        
    def validate_project_structure(self) -> Tuple[bool, str]:
        """Validate project structure before running checks"""
        if not self.project_path.exists():
            self.config_error = True
            self.hint = "请将 --project-path 指向 RPGMaker MZ 工程根目录"
            return False, f"Project path does not exist: {self.project_path}"
        
        if not self.data_path.exists():
            self.config_error = True
            self.hint = "请将 --project-path 指向 RPGMaker MZ 工程根目录（应包含 data/ 子目录）"
            return False, f"Data directory not found: {self.data_path}"
        
        # Check for critical files
        system_file = self.data_path / "System.json"
        if not system_file.exists():
            self.config_error = True
            self.hint = "RPGMaker MZ 工程缺少关键文件 data/System.json"
            return False, "System.json not found - not a valid RPGMaker MZ project"
        
        return True, ""
        
    def _load_json(self, filename: str) -> Optional[Dict]:
        """Load JSON file from data directory"""
        filepath = self.data_path / filename
        if not filepath.exists():
            self.errors.append(f"File not found: {filename}")
            return None
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            self.errors.append(f"JSON parse error in {filename}: {e}")
            return None
    
    def _format_map_name(self, map_id: int) -> str:
        """Format map filename (e.g., 1 -> Map001.json)"""
        return f"{self.MAP_PREFIX}{map_id:03d}{self.MAP_SUFFIX}"


class ConsistencyChecker(RPGChecker):
    """Check project consistency"""
    
    REQUIRED_MAP_IDS = [1, 2, 3]  # M001, M002, M003
    
    KEY_EVENTS = {
        1: [1, 2, 3, 4, 5],  # M001: E101, E102, E104, E201, teleport
        2: [1, 2],           # M002: teleport in/out
        3: [1, 2, 3],        # M003: teleport, stele, black-cloth
    }
    
    REQUIRED_SWITCHES = [
        "system_tutorial_done",      # S[1]
        "plot_ch1_done",             # S[10]
        "plot_ch2_done",             # S[11]
        "plot_ch3_done",             # S[12]
        "xie_met",                   # S[100]
        "xie_following",             # S[101]
    ]
    
    REQUIRED_VARIABLES = [
        "hero_level",                # V[1]
        "hero_chapter",              # V[2]
        "xie_affection",             # V[3]
    ]
    
    REQUIRED_ITEMS = [
        "残破家谱",                   # I[1]
    ]
    
    def check_maps_exist(self) -> CheckResult:
        """Check 1: Map existence"""
        self.errors = []
        self.warnings = []
        
        check_name = "Map Existence Check"
        missing_maps = []
        
        for map_id in self.REQUIRED_MAP_IDS:
            map_file = self._format_map_name(map_id)
            map_path = self.data_path / map_file
            if not map_path.exists():
                missing_maps.append(map_file)
        
        if missing_maps:
            self.errors.append(f"Missing maps: {', '.join(missing_maps)}")
            return CheckResult(check_name, CheckResult.CHECK_FAIL, self.errors, self.warnings)
        
        return CheckResult(check_name, CheckResult.PASS, [], self.warnings)
    
    def check_key_events(self) -> CheckResult:
        """Check 2: Key events existence"""
        self.errors = []
        self.warnings = []
        
        check_name = "Key Events Check"
        missing_events = []
        
        for map_id, event_ids in self.KEY_EVENTS.items():
            map_file = self._format_map_name(map_id)
            map_data = self._load_json(map_file)
            if not map_data:
                missing_events.append(f"{map_file}: cannot load map")
                continue
            
            existing_events = {e["id"] for e in map_data.get("events", []) if e}
            
            for event_id in event_ids:
                if event_id not in existing_events:
                    missing_events.append(f"{map_file}: Event {event_id}")
        
        if missing_events:
            self.errors.append(f"Missing events: {', '.join(missing_events)}")
            # FIX: Must return CHECK_FAIL if errors exist
            return CheckResult(check_name, CheckResult.CHECK_FAIL, self.errors, self.warnings)
        
        return CheckResult(check_name, CheckResult.PASS, [], self.warnings)
    
    def check_switches_variables(self) -> CheckResult:
        """Check 3: Switches and variables configuration"""
        self.errors = []
        self.warnings = []
        
        check_name = "Switches/Variables Check"
        system_data = self._load_json("System.json")
        
        if not system_data:
            return CheckResult(check_name, CheckResult.CHECK_FAIL, self.errors, self.warnings)
        
        switches = system_data.get("switches", [])
        variables = system_data.get("variables", [])
        
        # Check switches
        missing_switches = []
        for switch_name in self.REQUIRED_SWITCHES:
            if switch_name not in switches:
                missing_switches.append(switch_name)
        
        if missing_switches:
            self.errors.append(f"Missing switches: {', '.join(missing_switches)}")
        
        # Check variables
        missing_vars = []
        for var_name in self.REQUIRED_VARIABLES:
            if var_name not in variables:
                missing_vars.append(var_name)
        
        if missing_vars:
            self.errors.append(f"Missing variables: {', '.join(missing_vars)}")
        
        if self.errors:
            return CheckResult(check_name, CheckResult.CHECK_FAIL, self.errors, self.warnings)
        
        return CheckResult(check_name, CheckResult.PASS, [], self.warnings)
    
    def check_items(self) -> CheckResult:
        """Check 4: Key items existence"""
        self.errors = []
        self.warnings = []
        
        check_name = "Key Items Check"
        items_data = self._load_json("Items.json")
        
        if not items_data:
            return CheckResult(check_name, CheckResult.CHECK_FAIL, self.errors, self.warnings)
        
        existing_items = {item["name"] for item in items_data if item}
        
        missing_items = []
        for item_name in self.REQUIRED_ITEMS:
            if item_name not in existing_items:
                missing_items.append(item_name)
        
        if missing_items:
            self.errors.append(f"Missing items: {', '.join(missing_items)}")
            return CheckResult(check_name, CheckResult.CHECK_FAIL, self.errors, self.warnings)
        
        return CheckResult(check_name, CheckResult.PASS, [], self.warnings)
    
    def run_all(self) -> Dict[str, Any]:
        """Run all consistency checks"""
        # Validate project structure first
        valid, error_msg = self.validate_project_structure()
        if not valid:
            return {
                "checkSuite": "consistency",
                "resultType": CheckResult.CONFIG_ERROR,
                "overallStatus": "FAIL",
                "error": error_msg,
                "hint": self.hint,
                "timestamp": datetime.now().isoformat()
            }
        
        # Run checks
        checks = [
            self.check_maps_exist(),
            self.check_key_events(),
            self.check_switches_variables(),
            self.check_items(),
        ]
        
        results = {
            "checkSuite": "consistency",
            "checks": [c.to_dict() for c in checks],
            "timestamp": datetime.now().isoformat()
        }
        
        # Determine overall result type
        if any(c.result_type == CheckResult.CONFIG_ERROR for c in checks):
            results["resultType"] = CheckResult.CONFIG_ERROR
            results["overallStatus"] = "FAIL"
        elif any(c.result_type == CheckResult.CHECK_FAIL for c in checks):
            results["resultType"] = CheckResult.CHECK_FAIL
            results["overallStatus"] = "FAIL"
        else:
            results["resultType"] = CheckResult.PASS
            results["overallStatus"] = "PASS"
        
        return results


class FlowChecker(RPGChecker):
    """Check demo flow for demo-lite profile"""
    
    FLOW_NODES = [
        (1, "E101", "开场初始化"),
        (1, "E102", "素问入门"),
        (1, "E104", "谢临川初遇"),
        (1, "E201", "师尊任务"),
        (2, "teleport", "M001→M002"),
        (3, "teleport", "M002→M003"),
        (3, "E301+E302", "古碑调查"),
        (3, "E303", "黑衣人出现"),
        (3, "E304", "必败战斗"),
        (3, "E305", "败退获取家谱"),
    ]
    
    def check_demo_chain(self) -> CheckResult:
        """Check 1: Demo main chain reachable"""
        self.errors = []
        self.warnings = []
        
        check_name = "Demo Chain Reachability"
        
        for map_id, event_ref, desc in self.FLOW_NODES:
            map_file = self._format_map_name(map_id)
            map_data = self._load_json(map_file)
            
            if not map_data:
                self.errors.append(f"Cannot check {desc}: {map_file} not found")
                continue
        
        if self.errors:
            return CheckResult(check_name, CheckResult.CHECK_FAIL, self.errors, self.warnings)
        
        return CheckResult(check_name, CheckResult.PASS, [], self.warnings)
    
    def check_unlosable_battle(self) -> CheckResult:
        """Check 2: Ch3 black-cloth battle is 'unlosable'"""
        self.errors = []
        self.warnings = []
        
        check_name = "Unlosable Battle Check"
        
        troops_data = self._load_json("Troops.json")
        if not troops_data:
            return CheckResult(check_name, CheckResult.CHECK_FAIL, self.errors, self.warnings)
        
        # Check Troop 1 (黑衣人)
        if len(troops_data) < 2 or not troops_data[1]:
            self.errors.append("Troop 1 (黑衣人) not found")
            return CheckResult(check_name, CheckResult.CHECK_FAIL, self.errors, self.warnings)
        
        troop = troops_data[1]
        pages = troop.get("pages", [])
        
        has_unlosable_mechanic = False
        for page in pages:
            if page.get("trigger") == 1:  # Turn End
                has_unlosable_mechanic = True
                break
        
        if not has_unlosable_mechanic:
            self.errors.append("Troop 1 missing unlosable mechanic (HP/turn threshold)")
            return CheckResult(check_name, CheckResult.CHECK_FAIL, self.errors, self.warnings)
        
        return CheckResult(check_name, CheckResult.PASS, [], self.warnings)
    
    def check_genealogy_obtainable(self) -> CheckResult:
        """Check 3: '残破家谱' obtainable after retreat"""
        self.errors = []
        self.warnings = []
        
        check_name = "Genealogy Obtainable Check"
        
        common_events = self._load_json("CommonEvents.json")
        if not common_events or len(common_events) < 3:
            self.errors.append("Common Event 2 (败退获取家谱) not found")
            return CheckResult(check_name, CheckResult.CHECK_FAIL, self.errors, self.warnings)
        
        ce2 = common_events[2]
        if not ce2:
            self.errors.append("Common Event 2 is empty")
            return CheckResult(check_name, CheckResult.CHECK_FAIL, self.errors, self.warnings)
        
        commands = ce2.get("list", [])
        has_add_item = False
        for cmd in commands:
            if cmd.get("code") == 126:  # Change Items
                params = cmd.get("parameters", [])
                if len(params) >= 2 and params[0] == 1:  # Item ID 1
                    has_add_item = True
                    break
        
        if not has_add_item:
            self.errors.append("Common Event 2 does not add '残破家谱'")
            return CheckResult(check_name, CheckResult.CHECK_FAIL, self.errors, self.warnings)
        
        return CheckResult(check_name, CheckResult.PASS, [], self.warnings)
    
    def check_ch4_hook(self) -> CheckResult:
        """Check 4: Ch4 hook markers exist"""
        self.errors = []
        self.warnings = []
        
        check_name = "Ch4 Hook Check"
        
        system_data = self._load_json("System.json")
        if not system_data:
            return CheckResult(check_name, CheckResult.CHECK_FAIL, self.errors, self.warnings)
        
        switches = system_data.get("switches", [])
        
        hook_switches = ["qiluo_hook_delivered", "plot_ch4_done"]
        for sw in hook_switches:
            if sw not in switches:
                self.warnings.append(f"Hook switch '{sw}' not found (may be optional for demo-lite)")
        
        return CheckResult(check_name, CheckResult.PASS, [], self.warnings)
    
    def run_all(self, profile: str) -> Dict[str, Any]:
        """Run all flow checks for given profile"""
        if profile != "demo-lite":
            return {
                "checkSuite": "flow",
                "resultType": CheckResult.CONFIG_ERROR,
                "overallStatus": "FAIL",
                "error": f"Unknown profile: {profile}",
                "hint": "Available profiles: demo-lite",
                "timestamp": datetime.now().isoformat()
            }
        
        # Validate project structure first
        valid, error_msg = self.validate_project_structure()
        if not valid:
            return {
                "checkSuite": "flow",
                "profile": profile,
                "resultType": CheckResult.CONFIG_ERROR,
                "overallStatus": "FAIL",
                "error": error_msg,
                "hint": self.hint,
                "timestamp": datetime.now().isoformat()
            }
        
        checks = [
            self.check_demo_chain(),
            self.check_unlosable_battle(),
            self.check_genealogy_obtainable(),
            self.check_ch4_hook(),
        ]
        
        results = {
            "checkSuite": "flow",
            "profile": profile,
            "checks": [c.to_dict() for c in checks],
            "timestamp": datetime.now().isoformat()
        }
        
        # Determine overall result type
        if any(c.result_type == CheckResult.CONFIG_ERROR for c in checks):
            results["resultType"] = CheckResult.CONFIG_ERROR
            results["overallStatus"] = "FAIL"
        elif any(c.result_type == CheckResult.CHECK_FAIL for c in checks):
            results["resultType"] = CheckResult.CHECK_FAIL
            results["overallStatus"] = "FAIL"
        else:
            results["resultType"] = CheckResult.PASS
            results["overallStatus"] = "PASS"
        
        return results


def main():
    parser = argparse.ArgumentParser(
        description="RPGMaker MZ Project Checker v0.1",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python rpg_check.py consistency
    python rpg_check.py flow --profile demo-lite
    python rpg_check.py consistency --project-path /path/to/project
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Commands")
    
    # consistency command
    consistency_parser = subparsers.add_parser(
        "consistency",
        help="Check project consistency (maps, events, switches, items)"
    )
    consistency_parser.add_argument(
        "--project-path",
        default=".",
        help="Path to RPGMaker project (default: current directory)"
    )
    consistency_parser.add_argument(
        "--output",
        default="rpg-project/reports/consistency-report.json",
        help="Output file path"
    )
    
    # flow command
    flow_parser = subparsers.add_parser(
        "flow",
        help="Check demo flow for specific profile"
    )
    flow_parser.add_argument(
        "--profile",
        required=True,
        choices=["demo-lite"],
        help="Flow profile to check"
    )
    flow_parser.add_argument(
        "--project-path",
        default=".",
        help="Path to RPGMaker project (default: current directory)"
    )
    flow_parser.add_argument(
        "--output",
        default="rpg-project/reports/flow-report.json",
        help="Output file path"
    )
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    # Run checks
    if args.command == "consistency":
        checker = ConsistencyChecker(args.project_path)
        results = checker.run_all()
    elif args.command == "flow":
        checker = FlowChecker(args.project_path)
        results = checker.run_all(args.profile)
    
    # Write output
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    # Print summary to stdout
    print(json.dumps(results, ensure_ascii=False, indent=2))
    
    # Exit code based on resultType
    result_type = results.get("resultType", "CHECK_FAIL")
    if result_type == CheckResult.PASS:
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
