#!/usr/bin/env python3
"""Dependency validator for perception engineering product path workflows.

For each of 22 workflows, verify:
1. load_context files exist with substance
2. Cross-Expert Stacking references resolve to existing workflows
3. Named patterns/frameworks referenced (e.g., "Sutherland Pattern 11") have anchors in the genius file

Output: _active/system-audit/06-system/dependency-report-2026-05-05.md
"""
import re, os
from pathlib import Path
from collections import defaultdict

ROOT = Path("/Users/farricecain/Google Antigravity")

# 22 perception product path workflows (skill-level paths)
WORKFLOWS = {
    # 12 perception cross-stacks + solos (in rory-sutherland-marketing/workflows/)
    "perception-dopamine-engine": "skills/rory-sutherland-marketing/workflows/perception-dopamine-engine.md",
    "insight-perception-sprint": "skills/rory-sutherland-marketing/workflows/insight-perception-sprint.md",
    "positioning-perception-siege": "skills/rory-sutherland-marketing/workflows/positioning-perception-siege.md",
    "addictive-perception-content": "skills/rory-sutherland-marketing/workflows/addictive-perception-content.md",
    "consumer-perception-alchemy": "skills/rory-sutherland-marketing/workflows/consumer-perception-alchemy.md",
    "perception-dominance-campaign": "skills/rory-sutherland-marketing/workflows/perception-dominance-campaign.md",
    "blind-spot-social-engine": "skills/rory-sutherland-marketing/workflows/blind-spot-social-engine.md",
    "behavioral-copy-audit": "skills/rory-sutherland-marketing/workflows/behavioral-copy-audit.md",
    "reverse-benchmarking-audit": "skills/rory-sutherland-marketing/workflows/reverse-benchmarking-audit.md",
    "perception-metric-reframe": "skills/rory-sutherland-marketing/workflows/perception-metric-reframe.md",
    "asymmetric-bet-evaluator": "skills/rory-sutherland-marketing/workflows/asymmetric-bet-evaluator.md",
    "conspiratorial-reframe-engine": "skills/rory-sutherland-marketing/workflows/conspiratorial-reframe-engine.md",
    # 10 Stefan Georgi family
    "georgi-copy": "skills/stefan-georgi-dopamine-copy/workflows/dopamine-copy-engine.md",
    "georgi-hook": "skills/stefan-georgi-dopamine-copy/workflows/dopamine-hook-forge.md",
    "georgi-social": "skills/stefan-georgi-dopamine-copy/workflows/dopamine-social-engine.md",
    "georgi-emotion-map": "skills/stefan-georgi-dopamine-copy/workflows/emotion-mapping-engine.md",
    "georgi-mechanism": "skills/stefan-georgi-dopamine-copy/workflows/mechanism-architect.md",
    "georgi-curiosity-loop": "skills/stefan-georgi-dopamine-copy/workflows/curiosity-loop-designer.md",
    "georgi-paradox": "skills/stefan-georgi-dopamine-copy/workflows/paradox-generator.md",
    "georgi-nostalgia": "skills/stefan-georgi-dopamine-copy/workflows/nostalgia-lead-builder.md",
    "georgi-post-purchase": "skills/stefan-georgi-dopamine-copy/workflows/post-purchase-dopamine-drip.md",
    "georgi-audit": "skills/stefan-georgi-dopamine-copy/workflows/dopamine-audit.md",
}

LOAD_RE = re.compile(r"load_context:\s*[\"']?(.+?)[\"']?\s*$", re.MULTILINE)
LOAD_RE_BODY = re.compile(r"Load:\s*([^\n]+)")
PATTERN_REF_RE = re.compile(r"(?:Sutherland|Iha|Kallaway|Georgi|Dunford)\s+Patterns?\s+(?:[\d, ]+(?:and\s+\d+)?|\d+\-\d+)", re.IGNORECASE)
SLASH_REF_RE = re.compile(r"`/[\w\-]+`|\(`/[\w\-]+`\)")
SKILL_PATH_RE = re.compile(r"skills/[\w\-]+/(?:genius\.md|SKILL\.md|workflows/[\w\-]+\.md)")

results = {}

for wf_name, wf_path in WORKFLOWS.items():
    full_path = ROOT / wf_path
    info = {
        "exists": False,
        "words": 0,
        "load_context_files": [],
        "missing_load_files": [],
        "thin_load_files": [],
        "cross_expert_refs": [],
        "broken_cross_refs": [],
        "pattern_refs": [],
    }

    if not full_path.exists():
        results[wf_name] = info
        continue

    info["exists"] = True
    content = full_path.read_text(errors="ignore")
    info["words"] = len(content.split())

    # Extract load_context dependencies
    # Format: "rory-sutherland-marketing/genius.md + stefan-georgi-dopamine-copy/genius.md"
    load_match = LOAD_RE.search(content)
    if load_match:
        load_str = load_match.group(1)
        # Split on " + " or "+"
        parts = re.split(r"\s*\+\s*", load_str)
        for p in parts:
            p = p.strip()
            # Normalize to skills/X path
            if p.startswith("skills/"):
                skill_path = p
            else:
                skill_path = f"skills/{p}"
            target = ROOT / skill_path
            if not target.exists():
                info["missing_load_files"].append(skill_path)
            else:
                t_words = len(target.read_text(errors="ignore").split())
                if t_words < 200:
                    info["thin_load_files"].append((skill_path, t_words))
                info["load_context_files"].append((skill_path, t_words))

    # Extract Cross-Expert Stacking slash command references
    # Find section "## Cross-Expert Stacking" and pull /commands
    cross_section = re.search(r"##\s*Cross-Expert\s+Stacking.*?(?=^##\s|\Z)", content, re.DOTALL | re.MULTILINE | re.IGNORECASE)
    if cross_section:
        slash_cmds = re.findall(r"`/([\w\-]+)`", cross_section.group(0))
        for cmd in slash_cmds:
            info["cross_expert_refs"].append(cmd)
            # Check if this slash command exists as a workflow
            wf_file = ROOT / ".agent/workflows" / f"{cmd}.md"
            if not wf_file.exists():
                info["broken_cross_refs"].append(cmd)

    # Extract pattern references (just count, since validating each pattern number requires reading genius)
    info["pattern_refs"] = list(set(PATTERN_REF_RE.findall(content)))

    results[wf_name] = info

# Write report
lines = []
lines.append("# Dependency Validation Report — Perception Product Path")
lines.append("**Generated**: 2026-05-05")
lines.append(f"**Workflows audited**: {len(WORKFLOWS)}")
lines.append("")

# Summary
total_missing_loads = sum(len(r["missing_load_files"]) for r in results.values())
total_thin_loads = sum(len(r["thin_load_files"]) for r in results.values())
total_broken_xrefs = sum(len(r["broken_cross_refs"]) for r in results.values())
all_load_files = set()
for r in results.values():
    for f, _ in r["load_context_files"]:
        all_load_files.add(f)

lines.append("## Summary")
lines.append("")
lines.append(f"- Total load_context dependencies referenced: **{sum(len(r['load_context_files']) for r in results.values())}**")
lines.append(f"- Unique genius/skill files required: **{len(all_load_files)}**")
lines.append(f"- Missing load_context files: **{total_missing_loads}**")
lines.append(f"- Thin (<200 words) load_context files: **{total_thin_loads}**")
lines.append(f"- Broken Cross-Expert Stacking references: **{total_broken_xrefs}**")
lines.append("")

# Required genius files inventory
lines.append("## Required Genius/Skill Files Inventory")
lines.append("")
lines.append("| File | Words | Status |")
lines.append("|---|---|---|")
for f in sorted(all_load_files):
    fp = ROOT / f
    if fp.exists():
        w = len(fp.read_text(errors="ignore").split())
        status = "✅ OK" if w >= 500 else ("⚠️ THIN" if w >= 200 else "❌ TOO THIN")
        lines.append(f"| `{f}` | {w} | {status} |")
    else:
        lines.append(f"| `{f}` | - | ❌ MISSING |")
lines.append("")

# Per-workflow detail
lines.append("## Per-Workflow Dependency Status")
lines.append("")
lines.append("| Workflow | Words | Loads OK | Cross-Refs OK | Pattern Refs |")
lines.append("|---|---|---|---|---|")
for name in WORKFLOWS:
    r = results[name]
    if not r["exists"]:
        lines.append(f"| `/{name}` | - | ❌ MISSING WORKFLOW | - | - |")
        continue
    loads_status = "✅" if not r["missing_load_files"] and not r["thin_load_files"] else f"⚠️ {len(r['missing_load_files'])}miss/{len(r['thin_load_files'])}thin"
    xref_status = "✅" if not r["broken_cross_refs"] else f"❌ {len(r['broken_cross_refs'])}"
    pattern_count = len(r["pattern_refs"])
    lines.append(f"| `/{name}` | {r['words']} | {loads_status} | {xref_status} | {pattern_count} |")
lines.append("")

# Detail on issues
lines.append("## Issues Found (Detail)")
lines.append("")
any_issues = False
for name in WORKFLOWS:
    r = results[name]
    issues = []
    if not r["exists"]:
        issues.append(f"WORKFLOW FILE MISSING: {WORKFLOWS[name]}")
    for f in r["missing_load_files"]:
        issues.append(f"Missing load file: `{f}`")
    for f, w in r["thin_load_files"]:
        issues.append(f"Thin load file ({w}w): `{f}`")
    for c in r["broken_cross_refs"]:
        issues.append(f"Broken cross-expert reference: `/{c}` (no workflow file)")
    if issues:
        any_issues = True
        lines.append(f"### `/{name}`")
        for i in issues:
            lines.append(f"- {i}")
        lines.append("")

if not any_issues:
    lines.append("**No dependency issues found.** All 22 workflows have functional load_context files and resolved cross-expert references.")
    lines.append("")

# Pattern references compiled
lines.append("## Pattern References (per-workflow — manual verification needed)")
lines.append("")
lines.append("These pattern references should be checked against the relevant genius file to confirm the named patterns exist. The validator only counts occurrences; verifying that 'Sutherland Pattern 11' actually exists requires reading `skills/rory-sutherland-marketing/genius.md`.")
lines.append("")
for name in WORKFLOWS:
    r = results[name]
    if r["pattern_refs"]:
        lines.append(f"- `/{name}`: {', '.join(r['pattern_refs'])}")

OUT = ROOT / "_active/system-audit/06-system/dependency-report-2026-05-05.md"
OUT.write_text("\n".join(lines))
print(f"Report: {OUT}")
print(f"Workflows: {len(WORKFLOWS)} | Missing loads: {total_missing_loads} | Thin loads: {total_thin_loads} | Broken xrefs: {total_broken_xrefs}")
