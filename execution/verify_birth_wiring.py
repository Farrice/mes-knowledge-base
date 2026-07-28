#!/usr/bin/env python3
"""
Tier 3a Birth-Wiring Detector — verify new assets have firing paths.

Problem solved: "Wired-but-never-loaded" (2026-07-21) — 1,301 of 1,373 wrappers 
contained zero contract-load language. The asset exists on disk but never fires.

Trigger: PostToolUse (Write/Edit) — immediate, same-session verification

Audits (via file deltas from session start):
  1. New .md files (workflows, skills, agents, docs)
  2. New skill directories with SKILL.md
  3. New workflow entries in SLASH_COMMANDS.md (if applicable)
  4. Check: does it have a firing path?
     - Workflow: registered in SLASH_COMMANDS.md?
     - Skill: referenced in a Tier-1+ load path (expert SKILL.md, routing binding)?
     - Agent: added to AGENT_INDEX.md?
     - Doc: cross-referenced from active manifest?

Classification:
  NEWBORN_WIRED — asset created with firing path in place
  NEWBORN_ORPHAN — asset created, no firing path found (AUTO_FIX candidate: skip-if-present wrapper)
  STALE_BIRTH — asset created >1 day ago, never referenced (heals via auto-wire sweep)

Exit: always 0 (audit-only, never blocks)
Writes: .agent/health/birth-wiring.json (append-only ledger)
"""

import json
import os
import re
from datetime import datetime, timedelta
from pathlib import Path

REPO_ROOT = Path("/Users/farricecain/Google Antigravity")
HEALTH_DIR = REPO_ROOT / ".agent/health"
OUTPUT_JSON = HEALTH_DIR / "birth-wiring.json"


class BirthWiringDetector:
    def __init__(self, file_path=None, file_type=None):
        self.file_path = file_path
        self.file_type = file_type  # 'workflow', 'skill', 'agent', 'doc'
        self.timestamp = datetime.now().isoformat()
        self.finding = None
        
    def _check_workflow_wiring(self, workflow_path):
        """Check if workflow is registered in SLASH_COMMANDS.md"""
        workflow_name = Path(workflow_path).stem
        slash_commands = REPO_ROOT / "SLASH_COMMANDS.md"
        
        if not slash_commands.exists():
            return "FLAGGED", "SLASH_COMMANDS.md not found"
        
        try:
            with open(slash_commands) as f:
                content = f.read()
            
            # Check for workflow name in any form: /name, `/ name`, etc.
            patterns = [
                rf"^[/\\]{workflow_name}(?:\s|$)",
                rf"^\| `./{workflow_name}\.md`",
                rf"^\| `/{workflow_name}`",
            ]
            
            for pattern in patterns:
                if re.search(pattern, content, re.MULTILINE | re.IGNORECASE):
                    return "NEWBORN_WIRED", "Workflow registered in SLASH_COMMANDS.md"
            
            return "NEWBORN_ORPHAN", "Workflow not found in SLASH_COMMANDS.md"
        
        except Exception as e:
            return "ERROR", f"Failed to check SLASH_COMMANDS.md: {e}"
    
    def _check_skill_wiring(self, skill_path):
        """Check if skill is referenced in PRODUCTION_CORE.md or routing bindings"""
        skill_name = Path(skill_path).parent.name
        
        # Check PRODUCTION_CORE.md
        prod_core = REPO_ROOT / "PRODUCTION_CORE.md"
        if prod_core.exists():
            try:
                with open(prod_core) as f:
                    content = f.read()
                if skill_name in content:
                    return "NEWBORN_WIRED", "Skill referenced in PRODUCTION_CORE.md"
            except Exception:
                pass
        
        # Check routing bindings
        routing_bindings = REPO_ROOT / "directives/routing-bindings.md"
        if routing_bindings.exists():
            try:
                with open(routing_bindings) as f:
                    content = f.read()
                if skill_name in content:
                    return "NEWBORN_WIRED", "Skill in routing bindings"
            except Exception:
                pass
        
        return "NEWBORN_ORPHAN", "Skill not in PRODUCTION_CORE or routing bindings"
    
    def _check_agent_wiring(self, agent_path):
        """Check if agent is in AGENT_INDEX.md"""
        agent_name = Path(agent_path).parent.name
        
        agent_index = REPO_ROOT / "AGENT_INDEX.md"
        if not agent_index.exists():
            return "FLAGGED", "AGENT_INDEX.md not found"
        
        try:
            with open(agent_index) as f:
                content = f.read()
            if agent_name in content:
                return "NEWBORN_WIRED", "Agent indexed in AGENT_INDEX.md"
            else:
                return "NEWBORN_ORPHAN", "Agent not in AGENT_INDEX.md"
        except Exception as e:
            return "ERROR", f"Failed to check AGENT_INDEX.md: {e}"
    
    def audit(self):
        """Run birth-wiring audit for a single file"""
        if not self.file_path or not self.file_type:
            return
        
        file_path = Path(self.file_path)
        
        # Infer file type if not provided
        if self.file_type == "auto":
            if ".agent/workflows" in str(file_path):
                self.file_type = "workflow"
            elif "skills/" in str(file_path) and "SKILL.md" in str(file_path):
                self.file_type = "skill"
            elif "agents/" in str(file_path) and "AGENT.md" in str(file_path):
                self.file_type = "agent"
            else:
                self.file_type = "doc"
        
        # Run appropriate wiring check
        if self.file_type == "workflow":
            classification, message = self._check_workflow_wiring(file_path)
        elif self.file_type == "skill":
            classification, message = self._check_skill_wiring(file_path)
        elif self.file_type == "agent":
            classification, message = self._check_agent_wiring(file_path)
        else:
            classification, message = "INFO", "Manual audit required for doc type"
        
        # Check file age (stale birth detection)
        try:
            file_mtime = file_path.stat().st_mtime
            file_age = datetime.now() - datetime.fromtimestamp(file_mtime)
            
            if file_age > timedelta(days=1) and classification == "NEWBORN_ORPHAN":
                classification = "STALE_BIRTH"
        except Exception:
            pass
        
        self.finding = {
            "timestamp": self.timestamp,
            "file_path": str(file_path),
            "file_type": self.file_type,
            "classification": classification,
            "message": message
        }
        
        return self.finding
    
    def log_finding(self):
        """Append finding to birth-wiring ledger"""
        if not self.finding:
            return
        
        HEALTH_DIR.mkdir(parents=True, exist_ok=True)
        
        # Load existing ledger
        ledger = []
        if OUTPUT_JSON.exists():
            try:
                with open(OUTPUT_JSON) as f:
                    ledger = json.load(f)
            except Exception:
                ledger = []
        
        # Append new finding
        ledger.append(self.finding)
        
        # Write back (keep last 1000 entries to avoid unbounded growth)
        with open(OUTPUT_JSON, "w") as f:
            json.dump(ledger[-1000:], f, indent=2)


def detect_and_log(file_path, file_type="auto"):
    """Convenience function: detect wiring + log result"""
    detector = BirthWiringDetector(file_path, file_type)
    finding = detector.audit()
    if finding:
        detector.log_finding()
        return finding
    return None


if __name__ == "__main__":
    # Example: run as `python3 verify_birth_wiring.py <file_path> [file_type]`
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 verify_birth_wiring.py <file_path> [workflow|skill|agent|doc|auto]")
        sys.exit(0)
    
    file_path = sys.argv[1]
    file_type = sys.argv[2] if len(sys.argv) > 2 else "auto"
    
    finding = detect_and_log(file_path, file_type)
    if finding:
        print(json.dumps(finding, indent=2))
