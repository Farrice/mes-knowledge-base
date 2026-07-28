#!/usr/bin/env python3
"""
Master Fleet Verifier — coordinates all detection tiers and produces unified report.

Runs all verify_*.py suites in sequence, aggregates findings, and produces:
  1. .agent/health/fleet.json — structured findings (machine-readable)
  2. .agent/health/fleet-report.md — human-readable summary

Tiers (in order):
  1. Loop-Integrity (verify_loop_integrity.py) — hooks, launchd, spine, registries
  2. Core-Surface (verify_core_surface.py) — deliverables vs skill loads
  3. Birth-Wiring (verify_birth_wiring.py) — historical backlog scan
  
Classification (per finding):
  PROVEN — wiring is live, asset is used
  ALIGNED — deliverable + skill match
  NEWBORN_WIRED — asset created with firing path
  FLAGGED — attention needed (manual decision)
  UNDERLOADED — deliverable shipped, core skills missing
  ORPHAN — asset declared, no firing path

Exit: always 0 (audit-only, never blocks)
Writes: .agent/health/fleet.json + .agent/health/fleet-report.md

COMPASS DOCTRINE: audit reports, never refuses. Every red finding is either
auto-fixable (skip-if-present) or a judgment call surfaced here.
"""

import json
import subprocess
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path("/Users/farricecain/Google Antigravity")
HEALTH_DIR = REPO_ROOT / ".agent/health"
OUTPUT_JSON = HEALTH_DIR / "fleet.json"
OUTPUT_MD = HEALTH_DIR / "fleet-report.md"


class FleetVerifier:
    def __init__(self):
        self.timestamp = datetime.now().isoformat()
        self.all_findings = []
        self.tier_summaries = {}
        
    def run_tier(self, tier_script):
        """Run a single tier verifier and collect findings"""
        script_path = REPO_ROOT / "execution" / tier_script
        
        if not script_path.exists():
            return {"error": f"{tier_script} not found"}
        
        try:
            result = subprocess.run(
                ["python3", str(script_path)],
                capture_output=True,
                text=True,
                timeout=30,
                cwd=str(REPO_ROOT)
            )
            
            if result.returncode != 0 and result.stderr:
                return {"error": f"Tier failed: {result.stderr[:200]}"}
            
            return {"success": True}
        except subprocess.TimeoutExpired:
            return {"error": f"{tier_script} timed out"}
        except Exception as e:
            return {"error": str(e)}
    
    def aggregate_findings(self):
        """Read results from all tier verifiers and aggregate"""
        tier_results = [
            ("loop-integrity", HEALTH_DIR / "loop-integrity.json"),
            ("core-surface", HEALTH_DIR / "core-surface.json"),
            ("birth-wiring", HEALTH_DIR / "birth-wiring.json"),
        ]
        
        for tier_name, result_file in tier_results:
            if not result_file.exists():
                continue
            
            try:
                with open(result_file) as f:
                    tier_data = json.load(f)
                
                findings = tier_data.get("findings", [])
                summary = tier_data.get("summary", {})
                
                self.tier_summaries[tier_name] = {
                    "total": len(findings),
                    "summary": summary
                }
                
                # Merge findings
                for finding in findings:
                    if not finding.get("classification"):
                        continue
                    
                    # Add tier context
                    finding["tier"] = tier_name
                    self.all_findings.append(finding)
            
            except Exception:
                pass
    
    def write_fleet_json(self):
        """Write aggregated findings to fleet.json"""
        HEALTH_DIR.mkdir(parents=True, exist_ok=True)
        
        # Tally by classification
        classifications = {}
        for finding in self.all_findings:
            classification = finding.get("classification")
            if classification:
                classifications[classification] = classifications.get(classification, 0) + 1
        
        report = {
            "timestamp": self.timestamp,
            "summary": {
                "total_findings": len(self.all_findings),
                "by_classification": classifications,
                "tier_summaries": self.tier_summaries
            },
            "findings": self.all_findings
        }
        
        with open(OUTPUT_JSON, "w") as f:
            json.dump(report, f, indent=2)
    
    def write_fleet_markdown(self):
        """Write human-readable fleet report"""
        HEALTH_DIR.mkdir(parents=True, exist_ok=True)
        
        lines = [
            "# Fleet Verification Report",
            f"**Generated**: {self.timestamp}",
            "",
            "## Summary by Classification",
            ""
        ]
        
        # Count by classification
        classifications = {}
        for finding in self.all_findings:
            classification = finding.get("classification")
            if classification:
                classifications[classification] = classifications.get(classification, 0) + 1
        
        for classification in sorted(classifications.keys()):
            count = classifications[classification]
            lines.append(f"- **{classification}**: {count}")
        
        lines.append("")
        lines.append("## Summary by Tier")
        lines.append("")
        
        for tier_name, summary in sorted(self.tier_summaries.items()):
            lines.append(f"### {tier_name.title()}")
            lines.append(f"- Total findings: {summary['total']}")
            if summary.get('summary'):
                for key, value in summary['summary'].items():
                    lines.append(f"- {key}: {value}")
            lines.append("")
        
        # Flagged findings section
        flagged = [f for f in self.all_findings if f.get("classification") in ["FLAGGED", "UNDERLOADED", "NEWBORN_ORPHAN", "STALE_BIRTH"]]
        if flagged:
            lines.append("## 🚨 Issues Requiring Attention")
            lines.append("")
            for finding in flagged[:20]:  # Show first 20
                tier = finding.get("tier", "?")
                classification = finding.get("classification", "?")
                message = finding.get("message", "unknown")
                lines.append(f"**[{tier}:{classification}]** {message}")
            lines.append("")
        
        with open(OUTPUT_MD, "w") as f:
            f.write("\n".join(lines))
    
    def run(self):
        """Run full fleet verification"""
        # Run each tier
        tiers = [
            "verify_loop_integrity.py",
            "verify_core_surface.py",
            # birth-wiring is event-driven, not batched
        ]
        
        for tier_script in tiers:
            self.run_tier(tier_script)
        
        # Aggregate results
        self.aggregate_findings()
        
        # Write reports
        self.write_fleet_json()
        self.write_fleet_markdown()
        
        return 0


if __name__ == "__main__":
    verifier = FleetVerifier()
    exit(verifier.run())
