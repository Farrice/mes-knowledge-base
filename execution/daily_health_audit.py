#!/usr/bin/env python3
"""daily_health_audit.py — Daily health ratchet (runs ~150 assets/day to full backlog in ~1 month).

Combines Tier 1 (loop-integrity) and Tier 2 (core-surface) audits to gradually
verify all declared wiring and all skill/workflow registry entries.

Tiers:
  Tier 1: System-level wiring (hooks, launchd, spine, commands)
          - verify_loop_integrity.py (always runs, fixed cost)
  Tier 2: Session ledgers + core-surface alignment
          - verify_core_surface.py (always runs, incremental per session)
  Tier 3: Asset-level inventory checks (future)
          - Batch process: skills, workflows, directives, etc.
          - Run ~150 assets/day to cover ~1,200 skills in 8 days, ~990 workflows in 7 days

Exit: always 0 (audit-only, never blocks)
Writes: .agent/health/daily-audit.json
Scheduled: daily via launchd com.antigravity.daily-health-audit (06:00 AM)

Design: runs fast system checks (Tier 1) always. Tier 2 incremental. Tier 3 future.
"""

import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
HEALTH_DIR = REPO_ROOT / ".agent/health"
OUTPUT_JSON = HEALTH_DIR / "daily-audit.json"
AUDIT_STATE = HEALTH_DIR / "daily-audit-state.json"


class DailyHealthAudit:
    """Orchestrates daily health checks across all tiers."""

    def __init__(self):
        self.timestamp = datetime.now().isoformat()
        self.findings = []
        self.state = self._load_state()

    def _load_state(self):
        """Load audit progress state (last asset checked, etc.)"""
        if AUDIT_STATE.exists():
            try:
                return json.loads(AUDIT_STATE.read_text())
            except Exception:
                pass
        return {
            "last_run": None,
            "assets_checked_total": 0,
            "last_asset_batch": 0,
            "tier1_pass": False,
            "tier2_pass": False,
        }

    def _save_state(self):
        """Persist audit progress state"""
        HEALTH_DIR.mkdir(parents=True, exist_ok=True)
        AUDIT_STATE.write_text(json.dumps(self.state, indent=2))

    def run_tier1_loop_integrity(self):
        """Run Tier 1: System-level wiring checks (loop-integrity)."""
        try:
            result = subprocess.run(
                [sys.executable, str(REPO_ROOT / "execution/verify_loop_integrity.py")],
                capture_output=True,
                text=True,
                timeout=30,
            )

            # Tier 1 exit code: 0 = pass, >0 = findings found (but not failing)
            self.state["tier1_pass"] = result.returncode == 0

            self.findings.append({
                "tier": 1,
                "name": "loop_integrity",
                "status": "pass" if result.returncode == 0 else "findings",
                "exit_code": result.returncode,
                "output": result.stdout[:500] if result.stdout else "",
            })
            return result.returncode == 0
        except Exception as e:
            self.findings.append({
                "tier": 1,
                "name": "loop_integrity",
                "status": "error",
                "message": str(e),
            })
            return False

    def run_tier2_core_surface(self):
        """Run Tier 2: Skill load vs deliverable surface checks."""
        try:
            result = subprocess.run(
                [sys.executable, str(REPO_ROOT / "execution/verify_core_surface.py")],
                capture_output=True,
                text=True,
                timeout=30,
            )

            self.state["tier2_pass"] = result.returncode == 0

            self.findings.append({
                "tier": 2,
                "name": "core_surface",
                "status": "pass" if result.returncode == 0 else "findings",
                "exit_code": result.returncode,
                "output": result.stdout[:500] if result.stdout else "",
            })
            return result.returncode == 0
        except Exception as e:
            self.findings.append({
                "tier": 2,
                "name": "core_surface",
                "status": "error",
                "message": str(e),
            })
            return False

    def write_report(self):
        """Write daily audit results to .agent/health/daily-audit.json"""
        HEALTH_DIR.mkdir(parents=True, exist_ok=True)

        report = {
            "timestamp": self.timestamp,
            "state": self.state,
            "tiers_run": [1, 2],  # Future: extend to 3
            "findings": self.findings,
            "next_run": "Tomorrow 06:00 (scheduled via launchd)",
        }

        with open(OUTPUT_JSON, "w") as f:
            json.dump(report, f, indent=2)

        self.state["last_run"] = self.timestamp
        self._save_state()

    def run(self):
        """Execute daily audit (Tier 1 + 2)."""
        tier1_pass = self.run_tier1_loop_integrity()
        tier2_pass = self.run_tier2_core_surface()

        self.write_report()

        # Exit 0 (never block), but report findings
        return 0


def main():
    audit = DailyHealthAudit()
    exit_code = audit.run()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
