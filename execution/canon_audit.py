#!/usr/bin/env python3
"""Canon audit — per-project map of what's current, so stale docs stop winning greps.

Usage:
  python3 execution/canon_audit.py <project-folder>            # report + write CANON.md
  python3 execution/canon_audit.py <project-folder> --dry-run  # report only

Reads frontmatter `status:` / `superseded_by:` from every .md in the project
(recursive, skipping 99-archive*/archive dirs). Writes CANON.md at the project
root: canonical docs, superseded docs with successors, and drift flags —
prose "SUPERSEDED" banners with no frontmatter stamp. Never moves or edits
any file (compass, never cage): drift is reported with the exact stamp to add.
"""
import re
import sys
from datetime import date
from pathlib import Path

SKIP_DIRS = {"99-archive", "archive", ".git", "node_modules", "90-exports"}
BANNER_RE = re.compile(r"\bSUPERSEDED\b", re.I)
FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


def frontmatter(text: str) -> dict:
    m = FM_RE.match(text)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out


def audit(root: Path):
    canonical, superseded, drift, unmarked = [], [], [], []
    for p in sorted(root.rglob("*.md")):
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.name in {"CANON.md", "CAMPAIGN.md", "INDEX.md"}:
            continue
        try:
            text = p.read_text(errors="replace")
        except OSError:
            continue
        fm = frontmatter(text)
        rel = str(p.relative_to(root))
        status = fm.get("status", "").lower()
        if status == "canonical":
            canonical.append((rel, fm.get("supersedes", "")))
        elif status in {"superseded", "archived"}:
            superseded.append((rel, fm.get("superseded_by", "?")))
        elif BANNER_RE.search(text[:2000]):
            drift.append(rel)
        else:
            unmarked.append(rel)
    return canonical, superseded, drift, unmarked


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    root = Path(sys.argv[1]).resolve()
    dry = "--dry-run" in sys.argv
    if not root.is_dir():
        print(f"not a directory: {root}")
        return 1
    canonical, superseded, drift, unmarked = audit(root)

    # CANON.md is DEMOTED as of 2026-08-07. It used to open with "Canonical
    # (read these)", which is exactly the attractor Farrice diagnosed: a
    # stamped snapshot outranking newer cumulative work. The front door is the
    # entry point now; this file survives only as a wrong-not-just-old list,
    # because project_filer.EXEMPT_NAMES and the placement hook both pin the
    # name and other tools still expect it to exist.
    lines = [f"# CANON — {root.name}", "",
             "> **This is not the front door. Read `START-HERE.md`.**",
             "> Current-ness is decided by the living-vs-record rule, not by a",
             "> stamp: an undated filename is the living doc, a filename leading",
             "> with a date is a record. See `directives/artifact-placement.md`.",
             "",
             f"Generated {date.today().isoformat()} by canon_audit.py. This file now lists only docs that were *wrong* (explicitly superseded), plus stamp drift. Merely-older is the date rule's job.", ""]
    if canonical:
        lines.append("## ⚠ Retired `status: canonical` stamps — delete these")
        lines += [f"- `{r}` — remove the stamp; if it is truth, it should be the undated living doc in its folder" for r, _s in canonical]
        lines.append("")
    lines.append("## Superseded / archived (do NOT build on these)")
    lines += [f"- `{r}` → read `{s}` instead" for r, s in superseded] or ["- none"]
    if drift:
        lines.append("")
        lines.append("## DRIFT — prose banner says superseded, frontmatter missing (stamp these)")
        lines += [f"- `{r}` — add `---\\nstatus: superseded\\nsuperseded_by: <path>\\n---`" for r in drift]
    lines.append("")
    lines.append(f"## Unmarked ({len(unmarked)} docs — fine for working files; stamp any that are load-bearing)")
    lines.append("")

    report = "\n".join(lines)
    print(report)
    if not dry:
        (root / "CANON.md").write_text(report + "\n")
        print(f"\nwrote {root / 'CANON.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
