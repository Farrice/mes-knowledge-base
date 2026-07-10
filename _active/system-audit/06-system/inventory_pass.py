#!/usr/bin/env python3
"""One-off inventory: classify each .agent/workflows/*.md as substantive / router-functional / router-broken / empty,
   and check registration in SLASH_COMMANDS.md and SKILL_INDEX.md.

   This fills the gap that system_audit.py leaves: it counts words in the router file alone,
   so functional router stubs get flagged as "thin content" failures. The router pattern is intentional —
   we just need to verify the target exists with substance.

   Output: _active/system-audit/06-system/workflow-coverage-2026-05-05.md
"""
import os, re, sys
from pathlib import Path

ROOT = Path("/Users/farricecain/Google Antigravity")
WF_DIR = ROOT / ".agent/workflows"
SLASH_REG = ROOT / "SLASH_COMMANDS.md"
SKILL_REG = ROOT / "SKILL_INDEX.md"
OUT = ROOT / "_active/system-audit/06-system/workflow-coverage-2026-05-05.md"

LOAD_RE = re.compile(r"(?:Load:|Execute:)\s*(skills/[^\s`)]+\.md)", re.IGNORECASE)
SKILL_PATH_RE = re.compile(r"skills/[\w\-]+/(?:workflows/[\w\-]+\.md|SKILL\.md|genius\.md)")

slash_text = SLASH_REG.read_text(errors="ignore") if SLASH_REG.exists() else ""
skill_text = SKILL_REG.read_text(errors="ignore") if SKILL_REG.exists() else ""

results = []
for wf in sorted(WF_DIR.glob("*.md")):
    name = wf.stem
    try:
        content = wf.read_text(errors="ignore")
    except Exception as e:
        results.append((name, "READ-ERROR", str(e), False, False))
        continue

    word_count = len(content.split())
    line_count = len(content.splitlines())

    # Find skill workflow target(s) referenced in the router stub
    targets = LOAD_RE.findall(content)
    # Also pick up any skill path mentions
    targets += [m.group(0) for m in SKILL_PATH_RE.finditer(content)]
    targets = list(set(targets))  # dedupe

    # Classify
    if word_count == 0:
        status = "EMPTY"
        detail = "0 words — broken stub"
    elif word_count >= 200:
        # Substantive on its own
        status = "SUBSTANTIVE"
        detail = f"{word_count} words, {line_count} lines"
    elif targets:
        # Router stub — verify target exists with substance
        valid_targets = []
        broken_targets = []
        for t in targets:
            tp = ROOT / t
            if tp.exists():
                t_words = len(tp.read_text(errors="ignore").split())
                if t_words >= 200:
                    valid_targets.append((str(t), t_words))
                else:
                    broken_targets.append((str(t), f"target only {t_words} words"))
            else:
                broken_targets.append((str(t), "target file missing"))
        if valid_targets:
            status = "ROUTER-OK"
            detail = f"{word_count}w router → {valid_targets[0][0]} ({valid_targets[0][1]}w)"
        else:
            status = "ROUTER-BROKEN"
            detail = f"{word_count}w router; broken targets: {broken_targets}"
    else:
        # Thin content with no router target — actually thin
        status = "THIN-NO-ROUTER"
        detail = f"{word_count}w, no skill target referenced"

    # Registration check
    in_slash = name in slash_text or f"/{name}" in slash_text
    in_skill = name in skill_text

    results.append((name, status, detail, in_slash, in_skill))

# Tally
from collections import Counter
status_counts = Counter(r[1] for r in results)
unreg_in_slash = [r for r in results if not r[3]]
unreg_in_skill = [r for r in results if not r[4]]

# Write report
lines = []
lines.append(f"# Workflow Coverage Report")
lines.append(f"**Generated**: 2026-05-05")
lines.append(f"**Total workflows**: {len(results)}")
lines.append("")
lines.append("## Status Distribution")
lines.append("")
lines.append("| Status | Count | Meaning |")
lines.append("|---|---|---|")
lines.append(f"| SUBSTANTIVE | {status_counts['SUBSTANTIVE']} | Rich content in router file (≥200 words) — works as-is |")
lines.append(f"| ROUTER-OK | {status_counts['ROUTER-OK']} | Thin router → substantive skill workflow target |")
lines.append(f"| ROUTER-BROKEN | {status_counts['ROUTER-BROKEN']} | Router with missing/thin skill target — actually broken |")
lines.append(f"| THIN-NO-ROUTER | {status_counts['THIN-NO-ROUTER']} | Thin content, no router target — actually broken |")
lines.append(f"| EMPTY | {status_counts['EMPTY']} | Zero-word file — actually broken |")
lines.append(f"| READ-ERROR | {status_counts.get('READ-ERROR', 0)} | Couldn't read |")
lines.append("")
total_broken = status_counts['ROUTER-BROKEN'] + status_counts['THIN-NO-ROUTER'] + status_counts['EMPTY']
total_working = status_counts['SUBSTANTIVE'] + status_counts['ROUTER-OK']
lines.append(f"**Working: {total_working} / {len(results)}** ({total_working*100//len(results)}%)")
lines.append(f"**Actually broken: {total_broken} / {len(results)}** ({total_broken*100//len(results)}%)")
lines.append("")
lines.append(f"## Registration Gaps")
lines.append(f"- Not in SLASH_COMMANDS.md: **{len(unreg_in_slash)}**")
lines.append(f"- Not in SKILL_INDEX.md: **{len(unreg_in_skill)}**")
lines.append("")
lines.append("## C — Truly Broken (need fix or removal)")
lines.append("")
lines.append("| Workflow | Status | Detail |")
lines.append("|---|---|---|")
for name, status, detail, _, _ in results:
    if status in ("EMPTY", "ROUTER-BROKEN", "THIN-NO-ROUTER", "READ-ERROR"):
        lines.append(f"| `{name}` | {status} | {detail[:100]} |")
lines.append("")
lines.append("## B — Functional but Unregistered (need backfill in indexes)")
lines.append("")
lines.append("Working workflows missing from BOTH indexes:")
lines.append("")
lines.append("| Workflow | Status |")
lines.append("|---|---|")
both_unreg = [r for r in results if r[1] in ("SUBSTANTIVE", "ROUTER-OK") and not r[3] and not r[4]]
for name, status, detail, _, _ in both_unreg[:80]:
    lines.append(f"| `{name}` | {status} |")
lines.append("")
lines.append(f"... ({len(both_unreg)} total)")
lines.append("")
lines.append("## A — Production Ready (Substantive + Registered Sample)")
lines.append("")
ready = [r for r in results if r[1] in ("SUBSTANTIVE", "ROUTER-OK") and r[3] and r[4]]
lines.append(f"Total: **{len(ready)}** workflows registered in both indexes with working content")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## Perception Engineering Product Path (the 12 + Georgi cluster)")
lines.append("")
lines.append("| Workflow | Status | In SLASH | In SKILL_INDEX |")
lines.append("|---|---|---|---|")
perception_set = [
    "perception-dopamine-engine", "insight-perception-sprint", "positioning-perception-siege",
    "addictive-perception-content", "consumer-perception-alchemy", "perception-dominance-campaign",
    "blind-spot-social-engine", "behavioral-copy-audit", "reverse-benchmarking-audit",
    "perception-metric-reframe", "asymmetric-bet-evaluator", "conspiratorial-reframe-engine",
    "georgi-copy", "georgi-hook", "georgi-mechanism", "georgi-curiosity-loop",
    "georgi-paradox", "georgi-emotion-map", "georgi-nostalgia", "georgi-post-purchase",
    "georgi-social", "georgi-audit",
]
for name, status, detail, in_slash, in_skill in results:
    if name in perception_set:
        lines.append(f"| `{name}` | {status} | {'✅' if in_slash else '❌'} | {'✅' if in_skill else '❌'} |")

OUT.write_text("\n".join(lines))
print(f"Report written to: {OUT}")
print(f"Total: {len(results)} | Working: {total_working} | Broken: {total_broken}")
print(f"Unregistered in SLASH_COMMANDS.md: {len(unreg_in_slash)}")
print(f"Unregistered in SKILL_INDEX.md: {len(unreg_in_skill)}")
