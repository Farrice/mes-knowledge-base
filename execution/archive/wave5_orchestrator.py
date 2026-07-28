#!/usr/bin/env python3
"""
Wave 5 Prompt Renaissance Orchestrator
Dispatches 12 parallel Sonnet agents to refactor 150 crown-jewel prompts to structure-pure v2
Metadata: 2026-07-11, Farrice Cain's Antigravity repo
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Any

# Wave 5 Skill Groups Configuration
WAVE_5_GROUPS = [
    {"skill": "bond-halbert-copywriting", "count": 20},
    {"skill": "alen-sultanic-copywriting", "count": 18},
    {"skill": "seth-godin-ideavirus", "count": 17},
    {"skill": "erica-mallet-brand-magnetism", "count": 14},
    {"skill": "david-deutsch-copywriting", "count": 11},
    {"skill": "kallaway-content-psychology", "count": 10},
    {"skill": "brandon-jacoby-taste-mastery", "count": 10},
    {"skill": "nicolas-cole-client-acquisition", "count": 9},
    {"skill": "jun-yuh-personal-brand", "count": 8},
    {"skill": "dan-koe-multipassionate-mastery", "count": 8},
    {"skill": "lara-acosta-content-system", "count": 4},
    {"skill": "harry-dry-copywriting", "count": 1},
]

REPO_ROOT = Path("/Users/farricecain/Google Antigravity")
SKILLS_DIR = REPO_ROOT / "skills"

def create_refactor_agent_prompt(skill_name: str, prompt_count: int) -> str:
    """Create the agent prompt for refactoring a skill group's prompts."""
    return f"""You are Claude Sonnet, refactoring {prompt_count} crown-jewel prompts for {skill_name} to structure-pure v2 standard.

## Your Mission
Read each original prompt from skills/{skill_name}/references/prompts/
Skim skills/{skill_name}/genius.md for real credentials only
Refactor each to structure-pure v2 format

## Refactoring Rules

KEEP (unchanged):
- Role/activation (real credentials only)
- Input Required [BRACKET] section
- Execution protocol (numbered steps)
- Deploy When guidance

TRANSFORM:
- Examples → Output Contract (what the user receives)
- Examples → Output Skeleton (code fence with placeholders only, zero fabrication)
- Success Metrics → Quality Gate (pass/fail criteria)

STRIP (delete):
- Fabricated statistics ("studies show", invented metrics)
- Invented case studies (unless documented in genius.md)
- MES padding (motivational excess serving)
- Anecdotal preamble

MARK as "fidelity: low" if:
- Methodology is thin after stripping
- Examples were purely illustrative
- Credentials are weak/secondhand

## Output Format

Write each refactored prompt to skills/{skill_name}/references/prompts-v2/ as:

```yaml
---
name: [prompt-name]
source_prompt: [original-filename]
skill: {skill_name}
standard: structure-pure-v2
refactored: 2026-07-11
fidelity: [high|low]
---

[refactored content below, following structure-pure v2]
```

## Execution Steps

1. List all .md files in skills/{skill_name}/references/prompts/
2. For each file:
   a. Read the original
   b. Analyze: identify examples, stats, credentials
   c. Strip fabrication; keep methodology
   d. Reformat to structure-pure v2
   e. Write to prompts-v2/ with frontmatter
   f. Track: refactored (yes/no), reason if skipped
3. Report JSON: {{
    "skill": "{skill_name}",
    "refactored": <int>,
    "skipped": <int>,
    "fidelity_low": <int>,
    "summary": "<brief summary>"
}}

Start now. Report as JSON only, no preamble.
"""

def dispatch_agent(skill_name: str, prompt_count: int) -> subprocess.Popen:
    """Dispatch a single refactor agent for a skill group (non-blocking)."""
    prompt = create_refactor_agent_prompt(skill_name, prompt_count)

    # Use claude-3-5-sonnet with high effort
    cmd = [
        "claude",
        "ask",
        "--model", "claude-3-5-sonnet-20241022",
        "--effort", "high",
        prompt
    ]

    print(f"[DISPATCH] {skill_name} ({prompt_count} prompts)...", file=sys.stderr)

    return subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

def parse_agent_report(output: str) -> Dict[str, Any]:
    """Extract JSON report from agent output."""
    try:
        # Agent outputs JSON at end
        lines = output.strip().split('\n')
        for line in reversed(lines):
            if line.strip().startswith('{'):
                return json.loads(line)
    except (json.JSONDecodeError, IndexError):
        pass
    return {"error": "failed to parse"}

def main():
    """Launch all 12 agents in parallel, collect results."""
    print(f"\n{'='*70}")
    print(f"WAVE 5 PROMPT RENAISSANCE ORCHESTRATOR")
    print(f"{'='*70}")
    print(f"Date: 2026-07-11")
    print(f"Repo: {REPO_ROOT}")
    print(f"Groups: 12 | Prompts: 150")
    print(f"{'='*70}\n")

    # Verify skill directories exist
    missing = []
    for group in WAVE_5_GROUPS:
        skill_path = SKILLS_DIR / group["skill"]
        if not skill_path.exists():
            missing.append(group["skill"])

    if missing:
        print(f"ERROR: Missing skills directories: {missing}")
        return 1

    # Dispatch all agents in parallel
    agents = {}
    for group in WAVE_5_GROUPS:
        proc = dispatch_agent(group["skill"], group["count"])
        agents[group["skill"]] = proc

    # Collect results
    results = {
        "wave": 5,
        "timestamp": "2026-07-11",
        "groups_expected": len(WAVE_5_GROUPS),
        "groups_reported": 0,
        "refactored": 0,
        "skipped": 0,
        "fidelity_low": 0,
        "reports": [],
        "errors": []
    }

    print(f"Waiting for {len(agents)} agents to complete...\n", file=sys.stderr)

    for skill_name, proc in agents.items():
        stdout, stderr = proc.communicate()

        report = parse_agent_report(stdout)
        if "error" in report:
            print(f"[ERROR] {skill_name}: {report.get('error', 'unknown')}")
            results["errors"].append({"skill": skill_name, "error": report})
        else:
            results["reports"].append(report)
            results["groups_reported"] += 1
            results["refactored"] += report.get("refactored", 0)
            results["skipped"] += report.get("skipped", 0)
            results["fidelity_low"] += report.get("fidelity_low", 0)
            print(f"[DONE] {skill_name}: {report.get('refactored', 0)} refactored, "
                  f"{report.get('skipped', 0)} skipped, {report.get('fidelity_low', 0)} low-fidelity")

    # Summary
    print(f"\n{'='*70}")
    print(f"WAVE 5 SUMMARY")
    print(f"{'='*70}")
    print(f"Groups Reported: {results['groups_reported']}/{results['groups_expected']}")
    print(f"Total Refactored: {results['refactored']}")
    print(f"Total Skipped: {results['skipped']}")
    print(f"Fidelity Low: {results['fidelity_low']}")
    print(f"Errors: {len(results['errors'])}")
    print(f"{'='*70}\n")

    # Output JSON
    print(json.dumps(results, indent=2))

    return 0 if len(results["errors"]) == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
