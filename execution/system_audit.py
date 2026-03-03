#!/usr/bin/env python3
"""
System Audit — Antigravity Project Health Check
Validates structural integrity of agents, skills, workflows, indexes, and scripts.
Outputs a health report to .tmp/audit-report.md
"""

import os
import re
import sys
import ast
import json
from pathlib import Path
from datetime import datetime

# Run from project root
ROOT = Path(__file__).parent.parent
AGENTS_DIR = ROOT / "agents"
SKILLS_DIR = ROOT / "skills"
WORKFLOWS_DIR = ROOT / ".agent" / "workflows"
EXECUTION_DIR = ROOT / "execution"
INVOCATION_CARDS = ROOT / "agents" / "_framework" / "invocation-cards.md"
AGENT_INDEX = ROOT / "AGENT_INDEX.md"
SKILL_INDEX = ROOT / "SKILL_INDEX.md"
OUTPUT_DIR = ROOT / ".tmp"


def extract_frontmatter(file_path):
    """Extract YAML frontmatter from a markdown file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if match:
            # Simple key-value parsing without requiring PyYAML
            fm = {}
            for line in match.group(1).split("\n"):
                if ":" in line:
                    key, _, val = line.partition(":")
                    fm[key.strip()] = val.strip().strip('"').strip("'")
            return fm, content
        return {}, content
    except Exception as e:
        return {}, f"ERROR: {e}"


def check_file_quality(filepath):
    """Basic quality checks on a markdown file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        lines = content.strip().split("\n")
        word_count = len(content.split())
        has_headings = any(l.startswith("#") for l in lines)
        return {
            "exists": True,
            "word_count": word_count,
            "line_count": len(lines),
            "has_headings": has_headings,
            "is_substantial": word_count > 50,
        }
    except Exception:
        return {"exists": False, "word_count": 0, "line_count": 0, "has_headings": False, "is_substantial": False}


def audit_agents():
    """Audit all agents in agents/ directory."""
    results = {"pass": [], "warn": [], "fail": []}
    agent_slugs = []

    for item in sorted(os.listdir(AGENTS_DIR)):
        if item.startswith("_") or item.startswith("."):
            continue
        agent_path = AGENTS_DIR / item
        if not agent_path.is_dir():
            continue

        agent_slugs.append(item)
        agent_md = agent_path / "AGENT.md"

        if not agent_md.exists():
            results["fail"].append(f"`{item}`: Missing AGENT.md")
            continue

        quality = check_file_quality(agent_md)
        fm, content = extract_frontmatter(agent_md)

        issues = []

        if not quality["is_substantial"]:
            issues.append(f"thin content ({quality['word_count']} words)")

        if not quality["has_headings"]:
            issues.append("no markdown headings")

        # Check for frontmatter (needed for index sync)
        if not fm:
            issues.append("no YAML frontmatter (index sync will miss keywords)")

        # Check for key sections
        content_lower = content.lower()
        has_identity = "identity" in content_lower or "you are" in content_lower
        has_competencies = "competenc" in content_lower or "expertise" in content_lower or "capabilities" in content_lower
        has_framework = "framework" in content_lower or "method" in content_lower or "approach" in content_lower

        if not has_identity:
            issues.append("missing identity/persona section")
        if not has_competencies:
            issues.append("missing competencies/expertise section")

        if issues:
            severity = "fail" if "Missing" in str(issues) or "thin content" in str(issues) else "warn"
            results[severity].append(f"`{item}`: {'; '.join(issues)}")
        else:
            results["pass"].append(item)

    return results, agent_slugs


def audit_skills():
    """Audit all skills in skills/ directory."""
    results = {"pass": [], "warn": [], "fail": []}
    skill_slugs = []

    for item in sorted(os.listdir(SKILLS_DIR)):
        if item.startswith("_") or item.startswith("."):
            continue
        skill_path = SKILLS_DIR / item
        if not skill_path.is_dir():
            continue

        skill_slugs.append(item)
        skill_md = skill_path / "SKILL.md"
        genius_md = skill_path / "genius.md"
        workflows_dir = skill_path / "workflows"

        issues = []

        # Check SKILL.md
        if not skill_md.exists():
            results["fail"].append(f"`{item}`: Missing SKILL.md")
            continue

        fm, content = extract_frontmatter(skill_md)
        quality = check_file_quality(skill_md)

        if not fm:
            issues.append("no YAML frontmatter")
        else:
            if not fm.get("name"):
                issues.append("frontmatter missing 'name'")
            if not fm.get("description"):
                issues.append("frontmatter missing 'description'")

        # Check genius.md
        if not genius_md.exists():
            issues.append("missing genius.md")
        else:
            genius_quality = check_file_quality(genius_md)
            if not genius_quality["is_substantial"]:
                issues.append(f"genius.md is thin ({genius_quality['word_count']} words)")

        # Check workflows
        if not workflows_dir.exists():
            issues.append("missing workflows/ directory")
        else:
            workflow_files = [f for f in os.listdir(workflows_dir) if f.endswith(".md")]
            if not workflow_files:
                issues.append("workflows/ directory is empty")
            else:
                for wf in workflow_files:
                    wf_quality = check_file_quality(workflows_dir / wf)
                    if not wf_quality["is_substantial"]:
                        issues.append(f"workflow `{wf}` is thin ({wf_quality['word_count']} words)")

        # Classify
        if issues:
            has_critical = any(x in str(issues) for x in ["Missing SKILL.md", "missing genius.md", "missing workflows/", "directory is empty"])
            severity = "fail" if has_critical else "warn"
            results[severity].append(f"`{item}`: {'; '.join(issues)}")
        else:
            results["pass"].append(item)

    return results, skill_slugs


def audit_invocation_cards(agent_slugs):
    """Check which agents have invocation cards."""
    results = {"covered": [], "missing": []}

    if not INVOCATION_CARDS.exists():
        return {"error": "invocation-cards.md not found"}

    with open(INVOCATION_CARDS, "r", encoding="utf-8") as f:
        cards_content = f.read()

    # Extract agent names from AGENT: lines
    card_agents = set()
    for match in re.finditer(r'AGENT:\s*(.+)', cards_content):
        name = match.group(1).strip().lower().replace(" ", "-")
        card_agents.add(name)

    # Also try to match by slug patterns in the content
    cards_lower = cards_content.lower()

    for slug in agent_slugs:
        # Check if agent name appears in cards (flexible matching)
        slug_parts = slug.split("-")
        name_pattern = " ".join(slug_parts)
        if name_pattern in cards_lower or slug in cards_lower:
            results["covered"].append(slug)
        else:
            results["missing"].append(slug)

    return results


def audit_indexes(agent_slugs, skill_slugs):
    """Check if indexes are populated and accurate."""
    results = {"issues": []}

    # Check AGENT_INDEX
    if AGENT_INDEX.exists():
        with open(AGENT_INDEX, "r", encoding="utf-8") as f:
            content = f.read()
        # Count rows with empty keywords
        empty_keywords = len(re.findall(r'\| \*\*.*?\*\* \|  \|', content))
        total_rows = len(re.findall(r'\| `', content))
        if empty_keywords > 0:
            results["issues"].append(f"AGENT_INDEX: {empty_keywords}/{total_rows} agents have EMPTY Domain/Keywords")

        # Check for missing agents
        indexed_slugs = set(re.findall(r'\| `([^`]+)`', content))
        missing = set(agent_slugs) - indexed_slugs
        extra = indexed_slugs - set(agent_slugs)
        if missing:
            results["issues"].append(f"AGENT_INDEX: {len(missing)} agents missing from index: {', '.join(sorted(missing)[:5])}...")
        if extra:
            results["issues"].append(f"AGENT_INDEX: {len(extra)} index entries have no agent directory")
    else:
        results["issues"].append("AGENT_INDEX.md does not exist")

    # Check SKILL_INDEX
    if SKILL_INDEX.exists():
        with open(SKILL_INDEX, "r", encoding="utf-8") as f:
            content = f.read()
        empty_keywords = len(re.findall(r'\| \*\*.*?\*\* \|  \|', content))
        total_rows = len(re.findall(r'\| `', content))
        if empty_keywords > 0:
            results["issues"].append(f"SKILL_INDEX: {empty_keywords}/{total_rows} skills have EMPTY Domain/Keywords")

        indexed_slugs = set(re.findall(r'\| `([^`]+)`', content))
        missing = set(skill_slugs) - indexed_slugs
        if missing:
            results["issues"].append(f"SKILL_INDEX: {len(missing)} skills missing from index")
    else:
        results["issues"].append("SKILL_INDEX.md does not exist")

    return results


def audit_workflows():
    """Audit slash command workflows."""
    results = {"pass": [], "warn": [], "fail": []}

    if not WORKFLOWS_DIR.exists():
        return {"fail": [".agent/workflows/ directory missing"]}

    for item in sorted(os.listdir(WORKFLOWS_DIR)):
        if not item.endswith(".md"):
            continue
        wf_path = WORKFLOWS_DIR / item
        quality = check_file_quality(wf_path)

        if not quality["is_substantial"]:
            results["fail"].append(f"`{item}`: thin content ({quality['word_count']} words)")
        elif quality["word_count"] < 100:
            results["warn"].append(f"`{item}`: short ({quality['word_count']} words)")
        else:
            results["pass"].append(item)

    return results


def audit_execution_scripts():
    """Check Python scripts for valid syntax."""
    results = {"pass": [], "fail": []}

    for item in sorted(os.listdir(EXECUTION_DIR)):
        if not item.endswith(".py"):
            continue
        script_path = EXECUTION_DIR / item
        try:
            with open(script_path, "r", encoding="utf-8") as f:
                source = f.read()
            ast.parse(source)
            results["pass"].append(item)
        except SyntaxError as e:
            results["fail"].append(f"`{item}`: Syntax error at line {e.lineno}: {e.msg}")

    return results


def audit_agent_skill_alignment(agent_slugs, skill_slugs):
    """Check if agents have corresponding skills and vice versa."""
    results = {"agents_without_skills": [], "skills_without_agents": [], "aligned": []}

    for agent in agent_slugs:
        matching_skills = [s for s in skill_slugs if agent in s]
        if matching_skills:
            results["aligned"].append(f"`{agent}` → {', '.join(f'`{s}`' for s in matching_skills)}")
        else:
            results["agents_without_skills"].append(agent)

    # Skills that don't map to any agent (utility/framework skills)
    agent_set = set(agent_slugs)
    for skill in skill_slugs:
        has_agent = any(agent in skill for agent in agent_set)
        if not has_agent:
            results["skills_without_agents"].append(skill)

    return results


def generate_report():
    """Run all audits and generate report."""
    print("Running Antigravity System Audit...\n")

    # Run audits
    agent_results, agent_slugs = audit_agents()
    skill_results, skill_slugs = audit_skills()
    card_results = audit_invocation_cards(agent_slugs)
    index_results = audit_indexes(agent_slugs, skill_slugs)
    workflow_results = audit_workflows()
    script_results = audit_execution_scripts()
    alignment_results = audit_agent_skill_alignment(agent_slugs, skill_slugs)

    # Build report
    report = []
    report.append(f"# Antigravity System Audit Report")
    report.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("")

    # Summary
    report.append("## Summary")
    report.append("")
    total_pass = len(agent_results["pass"]) + len(skill_results["pass"])
    total_warn = len(agent_results["warn"]) + len(skill_results["warn"])
    total_fail = len(agent_results["fail"]) + len(skill_results["fail"])
    report.append(f"| Category | Pass | Warn | Fail |")
    report.append(f"|----------|------|------|------|")
    report.append(f"| Agents ({len(agent_slugs)}) | {len(agent_results['pass'])} | {len(agent_results['warn'])} | {len(agent_results['fail'])} |")
    report.append(f"| Skills ({len(skill_slugs)}) | {len(skill_results['pass'])} | {len(skill_results['warn'])} | {len(skill_results['fail'])} |")
    report.append(f"| Workflows | {len(workflow_results.get('pass', []))} | {len(workflow_results.get('warn', []))} | {len(workflow_results.get('fail', []))} |")
    report.append(f"| Execution Scripts | {len(script_results['pass'])} | 0 | {len(script_results['fail'])} |")
    report.append("")

    # Agents
    report.append("## Agents")
    report.append("")
    if agent_results["fail"]:
        report.append("### Failures")
        for item in agent_results["fail"]:
            report.append(f"- {item}")
        report.append("")
    if agent_results["warn"]:
        report.append("### Warnings")
        for item in agent_results["warn"]:
            report.append(f"- {item}")
        report.append("")
    report.append(f"**{len(agent_results['pass'])}/{len(agent_slugs)} agents pass structural checks.**")
    report.append("")

    # Skills
    report.append("## Skills")
    report.append("")
    if skill_results["fail"]:
        report.append("### Failures")
        for item in skill_results["fail"]:
            report.append(f"- {item}")
        report.append("")
    if skill_results["warn"]:
        report.append("### Warnings")
        for item in skill_results["warn"]:
            report.append(f"- {item}")
        report.append("")
    report.append(f"**{len(skill_results['pass'])}/{len(skill_slugs)} skills pass structural checks.**")
    report.append("")

    # Invocation Cards
    report.append("## Invocation Cards Coverage")
    report.append("")
    if isinstance(card_results, dict) and "error" not in card_results:
        report.append(f"- **Covered**: {len(card_results['covered'])}/{len(agent_slugs)} agents")
        report.append(f"- **Missing cards**: {len(card_results['missing'])} agents")
        if card_results["missing"]:
            report.append("")
            report.append("**Agents without invocation cards:**")
            for slug in card_results["missing"]:
                report.append(f"- `{slug}`")
    report.append("")

    # Indexes
    report.append("## Index Health")
    report.append("")
    if index_results["issues"]:
        for issue in index_results["issues"]:
            report.append(f"- **{issue}**")
    else:
        report.append("All indexes are in sync.")
    report.append("")

    # Workflows
    report.append("## Slash Command Workflows")
    report.append("")
    if workflow_results.get("fail"):
        report.append("### Failures")
        for item in workflow_results["fail"]:
            report.append(f"- {item}")
        report.append("")
    if workflow_results.get("warn"):
        report.append("### Warnings")
        for item in workflow_results["warn"]:
            report.append(f"- {item}")
        report.append("")
    report.append(f"**{len(workflow_results.get('pass', []))} workflows pass checks.**")
    report.append("")

    # Execution Scripts
    report.append("## Execution Scripts")
    report.append("")
    if script_results["fail"]:
        for item in script_results["fail"]:
            report.append(f"- FAIL: {item}")
    report.append(f"**{len(script_results['pass'])}/{len(script_results['pass']) + len(script_results['fail'])} scripts have valid syntax.**")
    report.append("")

    # Agent-Skill Alignment
    report.append("## Agent-Skill Alignment")
    report.append("")
    report.append(f"- **Aligned pairs**: {len(alignment_results['aligned'])}")
    report.append(f"- **Agents without matching skills**: {len(alignment_results['agents_without_skills'])}")
    report.append(f"- **Standalone skills (no matching agent)**: {len(alignment_results['skills_without_agents'])}")
    report.append("")
    if alignment_results["agents_without_skills"]:
        report.append("**Agents with no corresponding skill:**")
        for slug in alignment_results["agents_without_skills"]:
            report.append(f"- `{slug}`")
        report.append("")
    if alignment_results["skills_without_agents"]:
        report.append("**Standalone/utility skills (no agent):**")
        for slug in alignment_results["skills_without_agents"]:
            report.append(f"- `{slug}`")
        report.append("")

    # Critical Findings
    report.append("---")
    report.append("")
    report.append("## Critical Findings & Recommended Actions")
    report.append("")

    findings = []
    if index_results["issues"]:
        findings.append("**INDEX GAP**: Agent and skill indexes have empty Domain/Keywords columns — routing system cannot discover experts by topic. Fix: enhance `sync_registries.py` to extract keywords from file content.")

    if isinstance(card_results, dict) and "missing" in card_results and len(card_results.get("missing", [])) > 20:
        findings.append(f"**CARD GAP**: {len(card_results['missing'])} agents lack invocation cards — Tier 0 routing skips them entirely. Fix: generate cards for uncovered agents.")

    agent_no_fm = len(agent_results["warn"]) + len(agent_results["fail"])
    if agent_no_fm > 0:
        findings.append(f"**AGENT METADATA**: {agent_no_fm} agents have structural warnings/failures. Most common: missing YAML frontmatter needed by sync_registries.py.")

    if not findings:
        findings.append("No critical issues found.")

    for f in findings:
        report.append(f"1. {f}")

    report.append("")

    # Write report
    OUTPUT_DIR.mkdir(exist_ok=True)
    output_path = OUTPUT_DIR / "audit-report.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report))

    print(f"Audit complete. Report saved to: {output_path}")
    print(f"\nQuick summary:")
    print(f"  Agents:    {len(agent_results['pass'])} pass / {len(agent_results['warn'])} warn / {len(agent_results['fail'])} fail")
    print(f"  Skills:    {len(skill_results['pass'])} pass / {len(skill_results['warn'])} warn / {len(skill_results['fail'])} fail")
    print(f"  Workflows: {len(workflow_results.get('pass', []))} pass / {len(workflow_results.get('warn', []))} warn / {len(workflow_results.get('fail', []))} fail")
    print(f"  Scripts:   {len(script_results['pass'])} pass / {len(script_results['fail'])} fail")
    if isinstance(card_results, dict) and "missing" in card_results:
        print(f"  Cards:     {len(card_results['covered'])} covered / {len(card_results['missing'])} missing")


if __name__ == "__main__":
    generate_report()
