#!/usr/bin/env python3
"""verify_born_intent_drift.py — born-intent contracts + weekly drift diff.

Born 2026-07-21 (Farrice decision, /go-v3 session): every asset we build
(skills, workflows, prompts, agents) carries an intent anchor — its
description/identity line. Self-improvement loops are only recursive when
changes to those anchors are DELIBERATE; silent anchor drift is how assets
walk away from the intent of their creation (the failure class that rotted
30 fleet verifiers before 2026-07-21).

Mechanism (same review-then-bless pattern as platform_compiler.py):
  - Baseline: .agent/health/born-intent-baseline.json  {asset: sha1(anchor)}
  - New assets are auto-adopted into the baseline (born = first seen).
  - CHANGED or DELETED anchors vs baseline => exit 1 with a named list.
    Deliberate change? Review, then re-bless:  --bless
  - Rides the Sunday verify_fleet train (execution/verify_*.py glob) and the
    routine-health exception channel — drift lands in /cos, never silently.

Usage:
  python3 execution/verify_born_intent_drift.py          # check (fleet mode)
  python3 execution/verify_born_intent_drift.py --bless  # accept current state
"""

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASELINE = ROOT / ".agent" / "health" / "born-intent-baseline.json"


def _frontmatter_desc(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")[:4000]
    except OSError:
        return ""
    m = re.search(r"^description:\s*[\"']?(.+?)[\"']?\s*$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    m = re.search(r"^name:\s*[\"']?(.+?)[\"']?\s*$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def _agent_identity(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")[:4000]
    except OSError:
        return ""
    m = re.search(r"\*\*Who You Are\*\*:\s*(.+)", text)
    if m:
        return m.group(1).strip()[:300]
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def collect_anchors() -> dict:
    anchors = {}
    for sk in sorted((ROOT / "skills").glob("*/SKILL.md")):
        anchors[f"skill:{sk.parent.name}"] = _frontmatter_desc(sk)
    for wf in sorted((ROOT / ".agent" / "workflows").glob("*.md")):
        anchors[f"workflow:{wf.stem}"] = _frontmatter_desc(wf)
    for pr in sorted((ROOT / "skills").glob("*/references/prompts-v2/*.md")):
        anchors[f"prompt:{pr.parent.parent.parent.name}/{pr.stem}"] = _frontmatter_desc(pr)
    for ag in sorted((ROOT / "agents").glob("*/AGENT.md")):
        anchors[f"agent:{ag.parent.name}"] = _agent_identity(ag)
    return {k: hashlib.sha1(v.encode()).hexdigest()[:16] for k, v in anchors.items() if v}


def main() -> int:
    bless = "--bless" in sys.argv
    current = collect_anchors()
    BASELINE.parent.mkdir(parents=True, exist_ok=True)

    if bless or not BASELINE.exists():
        BASELINE.write_text(json.dumps(current, indent=0, sort_keys=True) + "\n")
        print(f"BLESSED — {len(current)} born-intent anchors baselined -> {BASELINE.relative_to(ROOT)}")
        return 0

    baseline = json.loads(BASELINE.read_text())
    changed = sorted(k for k in current if k in baseline and current[k] != baseline[k])
    deleted = sorted(k for k in baseline if k not in current)
    born = sorted(k for k in current if k not in baseline)

    # Adopt newborns silently (born = first seen); persist so next run is stable.
    if born:
        baseline.update({k: current[k] for k in born})
        # Drop deleted only when the run passes — deletions must be reviewed first.
        if not changed and not deleted:
            BASELINE.write_text(json.dumps(baseline, indent=0, sort_keys=True) + "\n")

    print(f"born-intent: {len(current)} anchors | {len(born)} newborn (adopted) | "
          f"{len(changed)} changed | {len(deleted)} deleted")
    if changed or deleted:
        for k in changed[:20]:
            print(f"  DRIFT {k} — intent anchor changed since bless")
        for k in deleted[:20]:
            print(f"  GONE  {k} — asset deleted (or renamed) since bless")
        if len(changed) + len(deleted) > 40:
            print(f"  ... +{len(changed)+len(deleted)-40} more")
        print("Deliberate? Review the diffs, then: python3 execution/verify_born_intent_drift.py --bless")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
