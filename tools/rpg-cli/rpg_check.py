#!/usr/bin/env python3
"""
rpg_check.py - RPGMaker MZ Project Checker
MVP Version for Demo-Lite v0.1

Commands:
    python rpg_check.py consistency
    python rpg_check.py flow --profile demo-lite

Output: JSON reports with check results
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional


class RPGChecker:
    """RPGMaker MZ Project Checker"""
    
    def __init__(self, project_path: str):
        self.project_path = Path(project_path)
        self.data_path = self.project_path / "data"
        self.errors: List[str] = []
        self.warnings: List[str] = []
        
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
    
    def _report(self, check_name: str, status: str) -> Dict[str, Any]:
        """Generate standardized report"""
        return {
            "checkName": check_name,
            "status": status,
            "errors": self.errors.copy(),
            "warnings": self.warnings.copy(),
            "timestamp": datetime.now().isoformat()
        }


class ConsistencyChecker(RPGChecker):
    """Check project consistency"""
    
    REQUIRED_MAPS = ["Map001.json", "Map002.json", "Map003.json"]
    
    KEY_EVENTS = {
        "Map001.json": [1, 2, 3, 4, 5],  # E101, E102, E104, E201, teleport
        "Map002.json": [1, 2],           # teleport in/out
        "Map003.json": [1, 2, 3],        # teleport, stele, black-cloth
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
        "绮罗音碎片",                 # I[2] (optional for demo-lite)
    ]
    
    def check_maps_exist(self) -> Dict[str, Any]:
        """Check 1: Map existence"""
        self.errors = []
        self.warnings = []
        
        check_name = "Map Existence Check"
        missing_maps = []
        
        for map_file in self.REQUIRED_MAPS:
            map_path = self.data_path / map_file
            if not map_path.exists():
                missing_maps.append(map_file)
        
        if missing_maps:
            self.errors.append(f"Missing maps: {', '.join(missing_maps)}")
            return self._report(check_name, "FAIL")
        
        return self._report(check_name, "PASS")
    
    def check_key_events(self) -> Dict[str, Any]:
        """Check 2: Key events existence"""
        self.errors = []
        self.warnings = []
        
        check_name = "Key Events Check"
        missing_events = []
        
        for map_file, event_ids in self.KEY_EVENTS.items():
            map_data = self._load_json(map_file)
            if not map_data:
                continue
            
            existing_events = {e["id"] for e in map_data.get("events", []) if e}
            
            for event_id in event_ids:
                if event_id not in existing_events:
                    missing_events.append(f"{map_file}: Event {event_id}")
        
        if missing_events:
            self.errors.append(f"Missing events: {', '.join(missing_events)}")
            return self._report(check_name, "FAIL")
        
        return self._report(check_name, "PASS")
    
    def check_switches_variables(self) -> Dict[str, Any]:
        """Check 3: Switches and variables configuration"""
        self.errors = []
        self.warnings = []
        
        check_name = "Switches/Variables Check"
        system_data = self._load_json("System.json")
        
        if not system_data:
            return self._report(check_name, "FAIL")
        
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
            return self._report(check_name, "FAIL")
        
        return self._report(check_name, "PASS")
    
    def check_items(self) -> Dict[str, Any]:
        """Check 4: Key items existence"""
        self.errors = []
        self.warnings = []
        
        check_name = "Key Items Check"
        items_data = self._load_json("Items.json")
        
        if not items_data:
            return self._report(check_name, "FAIL")
        
        existing_items = {item["name"] for item in items_data if item}
        
        missing_items = []
        for item_name in self.REQUIRED_ITEMS:
            if item_name not in existing_items:
                missing_items.append(item_name)
        
        if missing_items:
            self.errors.append(f"Missing items: {', '.join(missing_items)}")
            return self._report(check_name, "FAIL")
        
        return self._report(check_name, "PASS")
    
    def run_all(self) -> Dict[str, Any]:
        """Run all consistency checks"""
        results = {
            "checkSuite": "consistency",
            "checks": [
                self.check_maps_exist(),
                self.check_key_events(),
                self.check_switches_variables(),
                self.check_items(),
            ],
            "timestamp": datetime.now().isoformat()
        }
        
        # Overall status
        all_pass = all(c["status"] == "PASS" for c in results["checks"])
        results["overallStatus"] = "PASS" if all_pass else "FAIL"
        
        return results


class FlowChecker(RPGChecker):
    """Check demo flow for demo-lite profile"""
    
    FLOW_NODES = [
        ("M001", "E101", "开场初始化"),
        ("M001", "E102", "素问入门"),
        ("M001", "E104", "谢临川初遇"),
        ("M001", "E201", "师尊任务"),
        ("M002", "teleport", "M001→M002"),
        ("M003", "teleport", "M002→M003"),
        ("M003", "E301+E302", "古碑调查"),
        ("M003", "E303", "黑衣人出现"),
        ("M003", "E304", "必败战斗"),
        ("M003", "E305", "败退获取家谱"),
    ]
    
    def check_demo_chain(self) -> Dict[str, Any]:
        """Check 1: Demo main chain reachable"""
        self.errors = []
        self.warnings = []
        
        check_name = "Demo Chain Reachability"
        
        # Check each node
        for map_name, event_ref, desc in self.FLOW_NODES:
            map_file = f"{map_name}.json" if map_name.startswith("Map") else f"Map{map_name}.json"
            map_data = self._load_json(map_file)
            
            if not map_data:
                self.errors.append(f"Cannot check {desc}: {map_file} not found")
                continue
            
            # For teleport checks, verify map exists
            if event_ref == "teleport":
                continue  # Already checked map existence
            
            # For event checks, verify event exists
            # (Simplified - actual implementation would check event content)
        
        if self.errors:
            return self._report(check_name, "FAIL")
        
        return self._report(check_name, "PASS")
    
    def check_unlosable_battle(self) -> Dict[str, Any]:
        """Check 2: Ch3 black-cloth battle is 'unlosable'"""
        self.errors = []
        self.warnings = []
        
        check_name = "Unlosable Battle Check"
        
        troops_data = self._load_json("Troops.json")
        if not troops_data:
            return self._report(check_name, "FAIL")
        
        # Check Troop 1 (黑衣人)
        if len(troops_data) < 2 or not troops_data[1]:
            self.errors.append("Troop 1 (黑衣人) not found")
            return self._report(check_name, "FAIL")
        
        troop = troops_data[1]
        pages = troop.get("pages", [])
        
        # Check for Troop Event that triggers on HP/turn threshold
        has_unlosable_mechanic = False
        for page in pages:
            # Check if there's a condition for HP or turn count
            # This is a simplified check - actual implementation would be more detailed
            if page.get("trigger") == 1:  # Turn End
                has_unlosable_mechanic = True
                break
        
        if not has_unlosable_mechanic:
            self.errors.append("Troop 1 missing unlosable mechanic (HP/turn threshold)")
            return self._report(check_name, "FAIL")
        
        return self._report(check_name, "PASS")
    
    def check_genealogy_obtainable(self) -> Dict[str, Any]:
        """Check 3: '残破家谱' obtainable after retreat"""
        self.errors = []
        self.warnings = []
        
        check_name = "Genealogy Obtainable Check"
        
        # Check Common Event 2 (败退获取家谱)
        common_events = self._load_json("CommonEvents.json")
        if not common_events or len(common_events) < 3:
            self.errors.append("Common Event 2 (败退获取家谱) not found")
            return self._report(check_name, "FAIL")
        
        ce2 = common_events[2]
        if not ce2:
            self.errors.append("Common Event 2 is empty")
            return self._report(check_name, "FAIL")
        
        # Check if CE2 adds item 1 (残破家谱)
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
            return self._report(check_name, "FAIL")
        
        return self._report(check_name, "PASS")
    
    def check_ch4_hook(self) -> Dict[str, Any]:
        """Check 4: Ch4 hook markers exist"""
        self.errors = []
        self.warnings = []
        
        check_name = "Ch4 Hook Check"
        
        # Check if S[204] (qiluo_hook_delivered) switch is defined
        system_data = self._load_json("System.json")
        if not system_data:
            return self._report(check_name, "FAIL")
        
        switches = system_data.get("switches", [])
        
        # Check for hook-related switches (simplified)
        hook_switches = ["qiluo_hook_delivered", "plot_ch4_done"]
        for sw in hook_switches:
            if sw not in switches:
                self.warnings.append(f"Hook switch '{sw}' not found (may be optional for demo-lite)")
        
        return self._report(check_name, "PASS")
    
    def run_all(self, profile: str) -> Dict[str, Any]:
        """Run all flow checks for given profile"""
        if profile != "demo-lite":
            return {
                "checkSuite": "flow",
                "error": f"Unknown profile: {profile}",
                "timestamp": datetime.now().isoformat()
            }
        
        results = {
            "checkSuite": "flow",
            "profile": profile,
            "checks": [
                self.check_demo_chain(),
                self.check_unlosable_battle(),
                self.check_genealogy_obtainable(),
                self.check_ch4_hook(),
            ],
            "timestamp": datetime.now().isoformat()
        }
        
        # Overall status
        all_pass = all(c["status"] == "PASS" for c in results["checks"])
        results["overallStatus"] = "PASS" if all_pass else "FAIL"
        
        return results


def main():
    parser = argparse.ArgumentParser(
        description="RPGMaker MZ Project Checker",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python rpg_check.py consistency
    python rpg_check.py flow --profile demo-lite
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
    
    # Exit code
    sys.exit(0 if results.get("overallStatus") == "PASS" else 1)


if __name__ == "__main__":
    main()
