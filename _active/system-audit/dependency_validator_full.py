#!/usr/bin/env python3
"""Full-system dependency validator. Scans every skill workflow file for:
1. load_context files that don't exist or are thin
2. Cross-Expert Stacking references to slash commands that don't exist
3. Reports prioritized by skill cluster

Output: _active/system-audit/full-dependency-report-2026-05-05.md
"""
import re
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path("/Users/farricecain/Google Antigravity")
SKILLS_DIR = ROOT / "skills"
AGENT_WF_DIR = ROOT / ".agent/workflows"

LOAD_RE = re.compile(r"load_context:\s*[\"']?(.+?)[\"']?\s*$", re.MULTILINE)
SLASH_REF_RE = re.compile(r"`/([\w\-]+)`")

# Build set of existing slash commands (= filenames in .agent/workflows/)
existing_slash = set()
for f in AGENT_WF_DIR.glob("*.md"):
    existing_slash.add(f.stem)

# Walk all skill workflow files
all_workflows = []
for skill_dir in SKILLS_DIR.iterdir():
    if not skill_dir.is_dir():
        continue
    wf_subdir = skill_dir / "workflows"
    if not wf_subdir.is_dir():
        continue
    for wf in wf_subdir.glob("*.md"):
        all_workflows.append(wf)

# Stats
total = len(all_workflows)
issues = defaultdict(list)  # skill_dir -> list of (workflow_file, issue_type, detail)
all_issues_count = Counter()

for wf in all_workflows:
    try:
        content = wf.read_text(errors="ignore")
    except Exception as e:
        issues[wf.parent.parent.name].append((wf.name, "READ-ERROR", str(e)))
        continue

    skill_name = wf.parent.parent.name

    # 1. load_context check
    load_match = LOAD_RE.search(content)
    if load_match:
        load_str = load_match.group(1).strip()
        # Strip annotations like "(primary)" or "(chain-loaded per phase)"
        # Split on " + "
        parts = re.split(r"\s*[+,]\s*", load_str)
        for p in parts:
            # Remove parenthetical annotations
            p_clean = re.sub(r"\s*\([^)]*\)", "", p).strip()
            # Skip non-file entries (e.g., "chain-loaded per phase" without /)
            if "/" not in p_clean or not p_clean.endswith(".md"):
                continue
            # Normalize path
            if p_clean.startswith("skills/"):
                target_path = p_clean
            else:
                target_path = f"skills/{p_clean}"
            target = ROOT / target_path
            if not target.exists():
                issues[skill_name].append((wf.name, "MISSING-LOAD", target_path))
                all_issues_count["MISSING-LOAD"] += 1
            else:
                t_words = len(target.read_text(errors="ignore").split())
                if t_words < 200:
                    issues[skill_name].append((wf.name, "THIN-LOAD", f"{target_path} ({t_words}w)"))
                    all_issues_count["THIN-LOAD"] += 1

    # 2. Cross-Expert Stacking section check
    cross_section = re.search(r"##\s*Cross-Expert\s+Stacking.*?(?=^##\s|\Z)", content, re.DOTALL | re.MULTILINE | re.IGNORECASE)
    if cross_section:
        slash_cmds = SLASH_REF_RE.findall(cross_section.group(0))
        for cmd in slash_cmds:
            if cmd not in existing_slash:
                issues[skill_name].append((wf.name, "BROKEN-XREF", f"/{cmd}"))
                all_issues_count["BROKEN-XREF"] += 1

# Sort issues by skill (most-affected first)
sorted_skills = sorted(issues.items(), key=lambda x: -len(x[1]))

# Build report
lines = []
lines.append("# Full-System Dependency Validation Report")
lines.append("**Generated**: 2026-05-05")
lines.append(f"**Total skill workflows scanned**: {total}")
lines.append(f"**Skills with at least one issue**: {len(issues)}")
lines.append("")

lines.append("## Issue Type Summary")
lines.append("")
lines.append("| Issue Type | Count | Meaning |")
lines.append("|---|---|---|")
lines.append(f"| MISSING-LOAD | {all_issues_count['MISSING-LOAD']} | load_context references a file that doesn't exist |")
lines.append(f"| THIN-LOAD | {all_issues_count['THIN-LOAD']} | load_context file exists but <200 words (insufficient context) |")
lines.append(f"| BROKEN-XREF | {all_issues_count['BROKEN-XREF']} | Cross-Expert Stacking reference to non-existent slash command |")
total_issues = sum(all_issues_count.values())
lines.append(f"| **TOTAL** | **{total_issues}** | |")
lines.append("")

# Top affected skills
lines.append("## Top 20 Most-Affected Skills")
lines.append("")
lines.append("| Skill | Issue Count |")
lines.append("|---|---|")
for skill, skill_issues in sorted_skills[:20]:
    lines.append(f"| `{skill}` | {len(skill_issues)} |")
lines.append("")

# Detail per skill (top 10 only)
lines.append("## Detail — Top 10 Affected Skills")
lines.append("")
for skill, skill_issues in sorted_skills[:10]:
    lines.append(f"### `{skill}` ({len(skill_issues)} issues)")
    lines.append("")
    by_type = defaultdict(list)
    for wf_name, issue_type, detail in skill_issues:
        by_type[issue_type].append((wf_name, detail))
    for issue_type, items in sorted(by_type.items()):
        lines.append(f"**{issue_type}** ({len(items)}):")
        for wf_name, detail in items[:8]:
            lines.append(f"- `{wf_name}`: {detail}")
        if len(items) > 8:
            lines.append(f"- ... ({len(items) - 8} more)")
        lines.append("")
    lines.append("")

# Most-referenced phantom slash commands
phantom_counter = Counter()
for skill, skill_issues in issues.items():
    for wf_name, issue_type, detail in skill_issues:
        if issue_type == "BROKEN-XREF":
            phantom_counter[detail] += 1

lines.append("## Top Phantom Slash Commands (referenced but don't exist)")
lines.append("")
lines.append("These slash commands are referenced in Cross-Expert Stacking sections but have no workflow file. Each represents a planned-but-not-built workflow OR a renamed workflow whose old name is still referenced.")
lines.append("")
lines.append("| Phantom Command | Times Referenced |")
lines.append("|---|---|")
for cmd, count in phantom_counter.most_common(30):
    lines.append(f"| `{cmd}` | {count} |")
lines.append("")

OUT = ROOT / "_active/system-audit/full-dependency-report-2026-05-05.md"
OUT.write_text("\n".join(lines))
print(f"Report: {OUT}")
print(f"Total workflows: {total}")
print(f"Skills with issues: {len(issues)}")
print(f"Total issues: {total_issues}")
print(f"  Missing loads: {all_issues_count['MISSING-LOAD']}")
print(f"  Thin loads: {all_issues_count['THIN-LOAD']}")
print(f"  Broken xrefs: {all_issues_count['BROKEN-XREF']}")
