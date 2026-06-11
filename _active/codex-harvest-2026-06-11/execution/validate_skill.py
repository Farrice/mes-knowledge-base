#!/usr/bin/env python3
"""
Validate Skill Completeness — Deterministic validation so the LLM doesn't waste tokens counting files.

Usage:
    python3 execution/validate_skill.py <skill-name>
    python3 execution/validate_skill.py <skill-name> --fix-registry
    python3 execution/validate_skill.py --all

Checks:
    1. Required files exist (SKILL.md, genius-patterns.md)
    2. Prompt files match SKILL.md's prompt table
    3. Agent directory exists with AGENT.md and memory/context.md
    4. Registered in AGENT_INDEX.md and SKILL_INDEX.md
    5. Registered in active indexes/bridge surfaces
"""

import os
import re
import sys
import argparse
from pathlib import Path
from typing import Dict, List, Tuple


BASE_PATH = Path(__file__).parent.parent
SKILLS_PATH = BASE_PATH / "skills"
AGENTS_PATH = BASE_PATH / "agents"
AGENT_INDEX = BASE_PATH / "AGENT_INDEX.md"
SKILL_INDEX = BASE_PATH / "SKILL_INDEX.md"
CODEX_MD = BASE_PATH / "CODEX.md"
CODEX_LIVE_SKILLS = BASE_PATH / ".agents" / "skills"
CODEX_COLD_SKILLS = BASE_PATH / ".agents" / "cold-skills" / "source-command-wrappers"


def source_command_name(skill_name: str) -> str | None:
    """Return the bridged slash-command name for source-command skills."""
    prefix = "source-command-"
    if skill_name.startswith(prefix):
        return skill_name.removeprefix(prefix)
    return None


def codex_command_skill_paths(skill_name: str) -> tuple[Path, Path]:
    """Return live and cold Codex command skill paths for a source-command skill."""
    return (
        CODEX_LIVE_SKILLS / skill_name / "SKILL.md",
        CODEX_COLD_SKILLS / skill_name / "SKILL.md",
    )


def codex_command_skill_status(skill_name: str) -> tuple[str, Path | None]:
    """Return live/cold/missing status for a source-command Codex skill."""
    live_path, cold_path = codex_command_skill_paths(skill_name)
    if live_path.exists():
        return "live", live_path
    if cold_path.exists():
        return "cold", cold_path
    return "missing", None


def check_skill_files(skill_name: str) -> List[Dict]:
    """Check that required skill files exist."""
    issues = []
    command_name = source_command_name(skill_name)
    if command_name:
        status, skill_file = codex_command_skill_status(skill_name)
        if status == "live":
            issues.append({"severity": "✅", "check": "Codex command skill", "detail": f"{skill_file.relative_to(BASE_PATH)} live"})
        elif status == "cold":
            issues.append({"severity": "✅", "check": "Codex command skill", "detail": f"{skill_file.relative_to(BASE_PATH)} cold-quarantined"})
        else:
            live_path, cold_path = codex_command_skill_paths(skill_name)
            issues.append({"severity": "🔴", "check": "Codex command skill", "detail": f"Missing live or cold: {live_path.relative_to(BASE_PATH)} / {cold_path.relative_to(BASE_PATH)}"})
        return issues

    skill_dir = SKILLS_PATH / skill_name

    if not skill_dir.exists():
        issues.append({"severity": "🔴", "check": "Skill directory", "detail": f"skills/{skill_name}/ does not exist"})
        return issues

    # Required files
    required = {
        "SKILL.md": skill_dir / "SKILL.md",
        "genius-patterns.md": skill_dir / "references" / "genius-patterns.md",
    }

    # Optional but expected
    optional = {
        "hidden-knowledge.md": skill_dir / "references" / "hidden-knowledge.md",
    }

    for name, path in required.items():
        if not path.exists():
            issues.append({"severity": "🔴", "check": f"Required file: {name}", "detail": f"Missing: {path.relative_to(BASE_PATH)}"})
        else:
            issues.append({"severity": "✅", "check": f"Required file: {name}", "detail": "Present"})

    for name, path in optional.items():
        if not path.exists():
            issues.append({"severity": "🟡", "check": f"Optional file: {name}", "detail": f"Missing: {path.relative_to(BASE_PATH)}"})
        else:
            issues.append({"severity": "✅", "check": f"Optional file: {name}", "detail": "Present"})

    return issues


def count_prompt_files(skill_name: str) -> Tuple[int, List[str]]:
    """Count actual prompt files in the skill's prompts directory."""
    if source_command_name(skill_name):
        return 0, []

    prompts_dir = SKILLS_PATH / skill_name / "references" / "prompts"
    if not prompts_dir.exists():
        return 0, []
    
    prompt_files = sorted([f.stem for f in prompts_dir.glob("*.md")])
    return len(prompt_files), prompt_files


def check_agent_files(skill_name: str) -> List[Dict]:
    """Check that agent files exist for the expert."""
    issues = []

    command_name = source_command_name(skill_name)
    if command_name:
        status, codex_path = codex_command_skill_status(skill_name)
        live_path, cold_path = codex_command_skill_paths(skill_name)
        bridge_files = {
            "Workflow bridge": BASE_PATH / ".agent" / "workflows" / f"{command_name}.md",
            "Source command": BASE_PATH / ".claude" / "commands" / f"{command_name}.md",
        }
        for label, path in bridge_files.items():
            if path.exists():
                issues.append({"severity": "✅", "check": label, "detail": f"{path.relative_to(BASE_PATH)} present"})
            else:
                issues.append({"severity": "🔴", "check": label, "detail": f"Missing: {path.relative_to(BASE_PATH)}"})
        if status == "live":
            issues.append({"severity": "✅", "check": "Codex command skill", "detail": f"{codex_path.relative_to(BASE_PATH)} live"})
        elif status == "cold":
            issues.append({"severity": "✅", "check": "Codex command skill", "detail": f"{codex_path.relative_to(BASE_PATH)} cold-quarantined"})
        else:
            issues.append({"severity": "🔴", "check": "Codex command skill", "detail": f"Missing live or cold: {live_path.relative_to(BASE_PATH)} / {cold_path.relative_to(BASE_PATH)}"})
        return issues
    
    # System/non-person skills often use an exact matching agent slug.
    agent_candidates = [skill_name]

    # Derive agent name from skill name (e.g., "seena-rez-tiktok-commerce" -> "seena-rez")
    parts = skill_name.split("-")
    # Try common person/expert patterns after the exact slug.
    if len(parts) >= 2:
        agent_candidates.append(f"{parts[0]}-{parts[1]}")
    if len(parts) >= 3:
        agent_candidates.append(f"{parts[0]}-{parts[1]}-{parts[2]}")
    
    agent_found = False
    agent_name = None
    for candidate in agent_candidates:
        agent_dir = AGENTS_PATH / candidate
        if agent_dir.exists():
            agent_found = True
            agent_name = candidate
            break
    
    if not agent_found:
        issues.append({"severity": "🟡", "check": "Agent directory", "detail": f"No agent found for skill '{skill_name}' (tried: {', '.join(agent_candidates)})"})
        return issues
    
    agent_dir = AGENTS_PATH / agent_name
    
    if (agent_dir / "AGENT.md").exists():
        issues.append({"severity": "✅", "check": "AGENT.md", "detail": f"agents/{agent_name}/AGENT.md present"})
    else:
        issues.append({"severity": "🔴", "check": "AGENT.md", "detail": f"Missing: agents/{agent_name}/AGENT.md"})
    
    if (agent_dir / "memory" / "context.md").exists():
        issues.append({"severity": "✅", "check": "memory/context.md", "detail": f"agents/{agent_name}/memory/context.md present"})
    else:
        issues.append({"severity": "🟡", "check": "memory/context.md", "detail": f"Missing: agents/{agent_name}/memory/context.md"})
    
    return issues


def check_registry(skill_name: str) -> List[Dict]:
    """Check that the skill is registered in indexes."""
    issues = []
    command_name = source_command_name(skill_name)
    if command_name:
        workflow_path = BASE_PATH / ".agent" / "workflows" / f"{command_name}.md"
        source_path = BASE_PATH / ".claude" / "commands" / f"{command_name}.md"
        status, codex_path = codex_command_skill_status(skill_name)
        live_path, cold_path = codex_command_skill_paths(skill_name)

        if workflow_path.exists():
            issues.append({"severity": "✅", "check": "Command bridge", "detail": f"Registered through .agent/workflows/{command_name}.md"})
        else:
            issues.append({"severity": "🔴", "check": "Command bridge", "detail": f"Workflow .agent/workflows/{command_name}.md missing"})
        if source_path.exists():
            issues.append({"severity": "✅", "check": "Source command bridge", "detail": f".claude/commands/{command_name}.md present"})
        else:
            issues.append({"severity": "🔴", "check": "Source command bridge", "detail": f".claude/commands/{command_name}.md missing"})
        if status == "live":
            issues.append({"severity": "✅", "check": "Codex command bridge", "detail": f"{codex_path.relative_to(BASE_PATH)} live"})
        elif status == "cold":
            issues.append({"severity": "✅", "check": "Codex command bridge", "detail": f"{codex_path.relative_to(BASE_PATH)} cold-quarantined"})
        else:
            issues.append({"severity": "🔴", "check": "Codex command bridge", "detail": f"Missing live or cold: {live_path.relative_to(BASE_PATH)} / {cold_path.relative_to(BASE_PATH)}"})
        return issues
    
    # Check SKILL_INDEX.md
    if SKILL_INDEX.exists():
        content = SKILL_INDEX.read_text()
        if skill_name in content:
            issues.append({"severity": "✅", "check": "SKILL_INDEX.md", "detail": "Registered"})
        else:
            issues.append({"severity": "🔴", "check": "SKILL_INDEX.md", "detail": "NOT registered"})

    # Check AGENT_INDEX.md (look for agent slug)
    if AGENT_INDEX.exists():
        content = AGENT_INDEX.read_text()
        if skill_name in content:
            issues.append({"severity": "✅", "check": "AGENT_INDEX.md", "detail": f"Agent '{skill_name}' registered"})
            return issues

        # Derive agent slug for legacy person/expert skills.
        parts = skill_name.split("-")
        if len(parts) >= 2:
            agent_slug = f"{parts[0]}-{parts[1]}"
            if agent_slug in content:
                issues.append({"severity": "✅", "check": "AGENT_INDEX.md", "detail": f"Agent '{agent_slug}' registered"})
            else:
                issues.append({"severity": "🟡", "check": "AGENT_INDEX.md", "detail": f"Agent '{agent_slug}' not found"})
    
    return issues


def validate_skill(skill_name: str) -> None:
    """Run all validation checks on a skill."""
    print(f"\n🔍 Validating: {skill_name}")
    print("=" * 60)

    all_issues = []
    
    # 1. Skill files
    print("\n📁 Skill Files:")
    file_issues = check_skill_files(skill_name)
    all_issues.extend(file_issues)
    for issue in file_issues:
        print(f"  {issue['severity']} {issue['check']}: {issue['detail']}")
    
    # 2. Prompt files
    print("\n📝 Prompts:")
    count, prompts = count_prompt_files(skill_name)
    print(f"  📊 Found {count} prompt file(s)")
    for p in prompts:
        print(f"    - {p}")
    
    # 3. Agent files
    print("\n👤 Agent:")
    agent_issues = check_agent_files(skill_name)
    all_issues.extend(agent_issues)
    for issue in agent_issues:
        print(f"  {issue['severity']} {issue['check']}: {issue['detail']}")
    
    # 4. Registry
    print("\n📋 Registration:")
    reg_issues = check_registry(skill_name)
    all_issues.extend(reg_issues)
    for issue in reg_issues:
        print(f"  {issue['severity']} {issue['check']}: {issue['detail']}")
    
    # Summary
    print("\n" + "=" * 60)
    critical = len([i for i in all_issues if i['severity'] == '🔴'])
    warnings = len([i for i in all_issues if i['severity'] == '🟡'])
    passed = len([i for i in all_issues if i['severity'] == '✅'])
    
    print(f"📊 Results: {passed} passed, {warnings} warnings, {critical} critical")
    
    if critical == 0 and warnings == 0:
        print("✅ Skill is fully valid!")
    elif critical == 0:
        print("⚠️  Skill works but has minor gaps")
    else:
        print("❌ Skill has critical issues that need fixing")


def list_all_skills() -> List[str]:
    """List all skill directories."""
    if not SKILLS_PATH.exists():
        return []
    return sorted([
        d.name for d in SKILLS_PATH.iterdir() 
        if d.is_dir() and not d.name.startswith("_") and not d.name.startswith(".")
    ])


def main():
    parser = argparse.ArgumentParser(description="Validate skill completeness")
    parser.add_argument("skill_name", nargs="?", help="Name of the skill to validate")
    parser.add_argument("--all", action="store_true", help="Validate all skills")
    parser.add_argument("--summary", action="store_true", help="Show only summary for --all mode")
    
    args = parser.parse_args()
    
    if args.all:
        skills = list_all_skills()
        print(f"\n🔍 Validating all {len(skills)} skills...\n")
        
        results = {}
        for skill in skills:
            if args.summary:
                # Quick check
                file_issues = check_skill_files(skill)
                count, _ = count_prompt_files(skill)
                reg_issues = check_registry(skill)
                all_issues = file_issues + reg_issues
                critical = len([i for i in all_issues if i['severity'] == '🔴'])
                warnings = len([i for i in all_issues if i['severity'] == '🟡'])
                status = "✅" if critical == 0 and warnings == 0 else ("⚠️ " if critical == 0 else "❌")
                results[skill] = {"status": status, "prompts": count, "critical": critical, "warnings": warnings}
            else:
                validate_skill(skill)
                print()
        
        if args.summary:
            print(f"{'Skill':<45} {'Status':<6} {'Prompts':<8} {'Issues'}")
            print("-" * 75)
            for skill, info in results.items():
                issue_str = ""
                if info['critical'] > 0:
                    issue_str += f"{info['critical']} critical"
                if info['warnings'] > 0:
                    issue_str += f"{', ' if issue_str else ''}{info['warnings']} warnings"
                if not issue_str:
                    issue_str = "—"
                print(f"{skill:<45} {info['status']:<6} {info['prompts']:<8} {issue_str}")
    
    elif args.skill_name:
        validate_skill(args.skill_name)
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
