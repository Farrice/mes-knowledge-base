#!/usr/bin/env python3
"""
Tier 3b Daily Backlog Drain — continuous auto-wiring of historical assets.

Problem solved: 1,301 wrappers contain zero contract-load language. Rather than 
rebuild them all at once (explosive), drain at ~150/day and auto-wire on a schedule.

Design:
  1. Read from backlog ledger (.agent/backlog/orphans.jsonl) — write-set from verifiers
  2. For each orphan asset (workflow, skill, agent):
     a. Re-check firing path (maybe it got wired since discovered)
     b. If still orphan: determine auto-fix (skip-if-present wrapper for workflows, etc.)
     c. Apply fix only if safe (never mutate existing, never blind-write)
     d. Log result (FIXED, SKIPPED, MANUAL_REQUIRED)
  3. Batch size: 150 assets/run
  4. Run schedule: daily 08:00 via launchd com.antigravity.backlog-drain

Exit: always 0 (audit-only, never blocks)
Writes: .agent/health/backlog-drain.json (daily results)
Reads: .agent/backlog/orphans.jsonl (write-set from verifiers)
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path("/Users/farricecain/Google Antigravity")
HEALTH_DIR = REPO_ROOT / ".agent/health"
BACKLOG_DIR = REPO_ROOT / ".agent/backlog"
OUTPUT_JSON = HEALTH_DIR / "backlog-drain.json"
ORPHANS_LEDGER = BACKLOG_DIR / "orphans.jsonl"
BATCH_SIZE = 150


class DailyBacklogDrain:
    def __init__(self):
        self.timestamp = datetime.now().isoformat()
        self.processed = []
        self.results = {
            "fixed": 0,
            "skipped": 0,
            "manual": 0,
            "error": 0
        }
        
    def _read_orphans_ledger(self):
        """Read backlog of discovered orphans"""
        orphans = []
        
        if not ORPHANS_LEDGER.exists():
            return orphans
        
        try:
            with open(ORPHANS_LEDGER) as f:
                for line in f:
                    if line.strip():
                        orphans.append(json.loads(line))
        except Exception:
            pass
        
        return orphans
    
    def _recheck_workflow_wiring(self, workflow_path):
        """Re-verify workflow — maybe it got registered since discovery"""
        workflow_name = Path(workflow_path).stem
        slash_commands = REPO_ROOT / "SLASH_COMMANDS.md"
        
        if not slash_commands.exists():
            return False
        
        try:
            with open(slash_commands) as f:
                content = f.read()
            
            patterns = [
                rf"^[/\\]{workflow_name}(?:\s|$)",
                rf"^\| `./{workflow_name}\.md`",
                rf"^\| `/{workflow_name}`",
            ]
            
            for pattern in patterns:
                if re.search(pattern, content, re.MULTILINE | re.IGNORECASE):
                    return True
        except Exception:
            pass
        
        return False
    
    def _auto_wire_workflow(self, workflow_path):
        """Auto-wire workflow: add to SLASH_COMMANDS.md if not present"""
        workflow_file = Path(workflow_path)
        workflow_name = workflow_file.stem
        slash_commands = REPO_ROOT / "SLASH_COMMANDS.md"
        
        if not slash_commands.exists():
            return "manual", "SLASH_COMMANDS.md not found"
        
        # Re-check (double-check pattern)
        if self._recheck_workflow_wiring(workflow_path):
            return "skipped", "Already wired"
        
        # Read current content
        try:
            with open(slash_commands) as f:
                content = f.read()
        except Exception as e:
            return "error", f"Failed to read SLASH_COMMANDS.md: {e}"
        
        # Check if entry already exists (safe guard)
        if workflow_name in content:
            return "skipped", "Entry exists"
        
        # Format: add to end of file before any trailing newlines
        new_entry = f"\n- `/{workflow_name}` — Auto-wired {self.timestamp[:10]}"
        
        try:
            with open(slash_commands, "a") as f:
                f.write(new_entry)
            return "fixed", f"Added /{workflow_name} to SLASH_COMMANDS.md"
        except Exception as e:
            return "error", f"Failed to write SLASH_COMMANDS.md: {e}"
    
    def process_orphan(self, orphan):
        """Process a single orphan asset"""
        file_path = orphan.get("file_path")
        file_type = orphan.get("file_type", "doc")
        
        if not file_path:
            return {"file_path": "unknown", "result": "error", "reason": "No file_path in orphan record"}
        
        # Only auto-fix workflows for now (safest)
        if file_type != "workflow":
            return {"file_path": file_path, "result": "manual", "reason": f"Auto-wire not implemented for {file_type}"}
        
        # Re-check before auto-fixing
        if self._recheck_workflow_wiring(file_path):
            result, reason = "skipped", "Re-check found wiring"
            self.results["skipped"] += 1
        else:
            # Attempt auto-wire
            result, reason = self._auto_wire_workflow(file_path)
            self.results[result] += 1
        
        return {
            "file_path": file_path,
            "file_type": file_type,
            "result": result,
            "reason": reason,
            "timestamp": self.timestamp
        }
    
    def run(self, batch_size=BATCH_SIZE):
        """Run daily drain on up to batch_size orphans"""
        orphans = self._read_orphans_ledger()

        if not orphans:
            self.processed.append({
                "status": "info",
                "message": "No orphans in backlog"
            })
        else:
            # Process up to batch_size
            for orphan in orphans[:batch_size]:
                result = self.process_orphan(orphan)
                self.processed.append(result)

        self.write_results()
        return 0
    
    def write_results(self):
        """Write daily results"""
        HEALTH_DIR.mkdir(parents=True, exist_ok=True)
        
        report = {
            "timestamp": self.timestamp,
            "summary": self.results,
            "processed_count": len(self.processed),
            "results": self.processed[-100:]  # Keep last 100 for inspection
        }
        
        with open(OUTPUT_JSON, "w") as f:
            json.dump(report, f, indent=2)


if __name__ == "__main__":
    drain = DailyBacklogDrain()
    exit(drain.run())
