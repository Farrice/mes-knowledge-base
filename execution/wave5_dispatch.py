#!/usr/bin/env python3
"""
Wave 5 Prompt Renaissance Dispatcher
Launches 12 parallel Sonnet agents for prompt refactoring to structure-pure v2
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Dict, Any

REPO_ROOT = Path("/Users/farricecain/Google Antigravity")
SKILLS_DIR = REPO_ROOT / "skills"

# Wave 5 skill groups
SKILLS = [
    ("bond-halbert-copywriting", 20),
    ("alen-sultanic-copywriting", 18),
    ("seth-godin-ideavirus", 17),
    ("erica-mallet-brand-magnetism", 14),
    ("david-deutsch-copywriting", 11),
    ("kallaway-content-psychology", 10),
    ("brandon-jacoby-taste-mastery", 10),
    ("nicolas-cole-client-acquisition", 9),
    ("jun-yuh-personal-brand", 8),
    ("dan-koe-multipassionate-mastery", 8),
    ("lara-acosta-content-system", 4),
    ("harry-dry-copywriting", 1),
]

def refactor_skill_group(skill_name: str, count: int) -> Dict[str, Any]:
    """
    Refactor a skill group's prompts.
    Returns: {"skill": ..., "refactored": ..., "skipped": ..., "fidelity_low": ..., "summary": ...}
    """
    skill_path = SKILLS_DIR / skill_name
    prompts_dir = skill_path / "references" / "prompts"
    prompts_v2_dir = skill_path / "references" / "prompts-v2"

    result = {
        "skill": skill_name,
        "refactored": 0,
        "skipped": 0,
        "fidelity_low": 0,
        "summary": "",
        "error": None
    }

    # Verify directories
    if not prompts_dir.exists():
        result["error"] = f"prompts directory not found: {prompts_dir}"
        return result

    # Create prompts-v2 directory
    prompts_v2_dir.mkdir(parents=True, exist_ok=True)

    # Get all prompt files
    prompt_files = sorted(prompts_dir.glob("*.md"))
    if not prompt_files:
        result["error"] = f"No prompts found in {prompts_dir}"
        return result

    # Process each prompt
    for prompt_file in prompt_files[:count]:  # Respect count limit
        try:
            with open(prompt_file, 'r') as f:
                original_content = f.read()

            # Build refactoring prompt
            refactor_prompt = f"""Refactor this prompt to structure-pure v2. Return only valid YAML with markdown, no commentary.

Original Prompt:
---
{original_content}
---

Refactoring Rules:
- KEEP: Role, Input Required, Execution steps, Deploy When
- TRANSFORM: Examples → Output Contract + Output Skeleton (code fence, placeholders only)
- STRIP: Fabricated stats, invented cases, MES padding
- Mark "fidelity: low" if methodology is thin after stripping

Output format (YAML frontmatter + markdown body):
---
name: {prompt_file.stem}
source_prompt: {prompt_file.name}
skill: {skill_name}
standard: structure-pure-v2
refactored: 2026-07-11
fidelity: high
---

[refactored content]

Return ONLY the YAML block and markdown, nothing else."""

            # Call Claude API via subprocess
            cmd = [
                "/Users/farricecain/.npm-global/bin/claude",
                "ask",
                "--model", "claude-3-5-sonnet-20241022",
                refactor_prompt
            ]

            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60
            )

            if proc.returncode == 0:
                refactored_content = proc.stdout.strip()

                # Detect fidelity-low
                is_fidelity_low = "fidelity: low" in refactored_content

                # Write to prompts-v2
                output_file = prompts_v2_dir / prompt_file.name
                with open(output_file, 'w') as f:
                    f.write(refactored_content)

                result["refactored"] += 1
                if is_fidelity_low:
                    result["fidelity_low"] += 1
            else:
                result["skipped"] += 1

        except Exception as e:
            result["skipped"] += 1

    result["summary"] = (
        f"Refactored {result['refactored']}/{len(prompt_files)} prompts; "
        f"{result['fidelity_low']} marked low-fidelity"
    )

    return result

def main():
    """Launch all 12 skills in parallel."""
    print("\n" + "="*70)
    print("WAVE 5 PROMPT RENAISSANCE ORCHESTRATOR")
    print("="*70)
    print(f"Date: 2026-07-11")
    print(f"Skills: {len(SKILLS)} | Expected Prompts: {sum(c for _, c in SKILLS)}")
    print("="*70 + "\n")

    # Parallel execution
    results = {
        "wave": 5,
        "timestamp": "2026-07-11",
        "groups_expected": len(SKILLS),
        "groups_reported": 0,
        "refactored": 0,
        "skipped": 0,
        "fidelity_low": 0,
        "reports": []
    }

    with ProcessPoolExecutor(max_workers=12) as executor:
        futures = {
            executor.submit(refactor_skill_group, skill, count): skill
            for skill, count in SKILLS
        }

        for future in as_completed(futures):
            skill = futures[future]
            try:
                report = future.result()
                results["reports"].append(report)

                if not report.get("error"):
                    results["groups_reported"] += 1
                    results["refactored"] += report["refactored"]
                    results["skipped"] += report["skipped"]
                    results["fidelity_low"] += report["fidelity_low"]

                    print(f"[✓] {skill}: {report['refactored']} refactored, "
                          f"{report['skipped']} skipped, {report['fidelity_low']} low-fidelity")
                else:
                    print(f"[✗] {skill}: {report['error']}")

            except Exception as e:
                print(f"[✗] {skill}: Exception - {e}")

    # Summary
    print("\n" + "="*70)
    print("WAVE 5 SUMMARY")
    print("="*70)
    print(f"Groups Reported: {results['groups_reported']}/{results['groups_expected']}")
    print(f"Total Refactored: {results['refactored']}")
    print(f"Total Skipped: {results['skipped']}")
    print(f"Low-Fidelity: {results['fidelity_low']}")
    print(f"Remaining in Queue: {1358 - results['refactored']}")
    print("="*70 + "\n")

    print(json.dumps(results, indent=2))

    return 0 if results["groups_reported"] == results["groups_expected"] else 1

if __name__ == "__main__":
    sys.exit(main())
