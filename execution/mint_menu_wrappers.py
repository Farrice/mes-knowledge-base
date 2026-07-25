#!/usr/bin/env python3
"""
mint_menu_wrappers.py — make everything built actually fireable.

WHY THIS EXISTS
---------------
`sync_registries.py` mints one command shim per SKILL. Nothing ever minted one
per WORKFLOW, so `.agent/workflows/extract.md` carried a manual instruction:
"the generators do not mint per-workflow shims (2026-07-21 gap)". Manual steps
lose to velocity — 728 workflows accumulated on disk with no way to invoke them.
Heartbeat check 7 (skill_auditor) detects that; detection alone does not fix a
MINTING gap. This closes it.

THREE DRIFT CLASSES
-------------------
  A. skill-workflow  → mints BOTH `.agent/workflows/<cmd>.md` (thin wrapper) and
                       `.claude/commands/<cmd>.md` (shim). The wrapper embeds the
                       full `skills/<skill>/workflows/<file>.md` path, which is
                       exactly what check 7 looks for.
  B. command-workflow → wrapper exists, shim missing, so it never appears in the
                       native `/` typeahead. Mints the shim only.
  C. skill            → no front-door command. NOT handled here: `sync_registries.py`
                       owns skill-level shims and expert front doors. Reported so
                       the gap is visible, never silently absorbed.

CLOBBER SAFETY (the invariant that must never break)
----------------------------------------------------
Every file written carries GEN_MARKER. A target that exists WITHOUT our marker is
foreign — a hand-written workflow or shim — and is never modified, only reported.
This is the same sentinel discipline `sync_registries.py` uses to protect the
~598 hand-written shims. A dry run writes nothing at all.

Usage:
    python3 execution/mint_menu_wrappers.py --dry-run              # default; writes nothing
    python3 execution/mint_menu_wrappers.py --scope skill <name> --apply
    python3 execution/mint_menu_wrappers.py --scope all --apply
    python3 execution/mint_menu_wrappers.py --scope all --apply --limit-families 5
    python3 execution/mint_menu_wrappers.py --report               # JSON plan, no writes
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "execution"))

import arsenal_index  # noqa: E402
from skill_auditor import _read_text  # noqa: E402

WF_DIR = ROOT / ".agent" / "workflows"
CMD_DIR = ROOT / ".claude" / "commands"

GEN_MARKER = ("<!-- auto-generated: menu wrapper (mint_menu_wrappers.py) — "
              "safe to delete; regenerated on the next parity sweep -->")

_NUM_PREFIX_RE = re.compile(r"^\d{1,2}[-_]")
_H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)
_STOP = {"the", "and", "for", "with", "os", "system", "engine", "skill"}


# ──────────────────────────────────────────────────────────────────────────
# naming — never shadow an existing command
# ──────────────────────────────────────────────────────────────────────────

def _skill_prefix(skill: str, sibling_stems: List[str]) -> str:
    """The family prefix this skill already uses, else one derived from its slug.

    Inference first: if two or more of the skill's already-reachable workflows
    share a `xxx-` prefix, that IS the family's convention (riley-, bc-, ml-,
    oe-) and new commands must match it. Only when there is no established
    convention do we derive one from the skill directory name.
    """
    counts: Dict[str, int] = {}
    for s in sibling_stems:
        head = s.split("-", 1)[0]
        if head and not head.isdigit():
            counts[head] = counts.get(head, 0) + 1
    if counts:
        best, n = max(counts.items(), key=lambda kv: kv[1])
        if n >= 2:
            return best
    tokens = [t for t in skill.split("-") if t and t not in _STOP]
    return "-".join(tokens[:2]) if tokens else skill


def choose_command_name(stem: str, skill: str, taken: set, sibling_stems: List[str]) -> Optional[str]:
    """First free candidate, or None if every candidate collides.

    Numbered stems (`02-buyback-audit`) never become bare commands — `/02-...`
    is meaningless out of its skill's context, so they always take the prefix.
    """
    base = _NUM_PREFIX_RE.sub("", stem)
    prefix = _skill_prefix(skill, sibling_stems)
    candidates = []
    if not _NUM_PREFIX_RE.match(stem):
        candidates.append(base)
    candidates.append(base if base.startswith(prefix + "-") else f"{prefix}-{base}")
    candidates.append(f"{skill}-{base}")
    for c in candidates:
        c = re.sub(r"-{2,}", "-", c).strip("-")
        if c and c not in taken:
            return c
    return None


# ──────────────────────────────────────────────────────────────────────────
# content
# ──────────────────────────────────────────────────────────────────────────

def _title(path: Path, fallback: str) -> str:
    m = _H1_RE.search(_read_text(path))
    if m:
        return re.sub(r"^/\S+\s*[—-]\s*", "", m.group(1).strip())
    return fallback.replace("-", " ").title()


def _matching_prompt(skill: str, stem: str) -> Optional[str]:
    """A prompts-v2 file whose stem matches this workflow exactly.

    Exact match only. Guessing which prompt belongs to which workflow would
    produce wrappers that load the WRONG execution prompt — worse than loading
    none, because it fails silently and confidently.
    """
    p = ROOT / "skills" / skill / "references" / "prompts-v2" / f"{stem}.md"
    return f"skills/{skill}/references/prompts-v2/{stem}.md" if p.exists() else None


def _esc(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def wrapper_body(cmd: str, skill: str, wf_rel: str, wf_path: Path, desc: str) -> str:
    title = _title(wf_path, cmd)
    prompt = _matching_prompt(skill, wf_path.stem)
    genius = ROOT / "skills" / skill / "genius.md"
    step1 = (f"1. Load the spine: read `skills/{skill}/genius.md` (patterns, signature moves, "
             f"Anti-Patterns, Recognition Test).\n" if genius.exists()
             else f"1. Load the spine: read `skills/{skill}/SKILL.md` (methodology, standards).\n")
    step2 = f"2. Read and execute `{wf_rel}` exactly as documented"
    step2 += f" — honoring the execution prompt `{prompt}`.\n" if prompt else ".\n"
    return (
        f'---\ndescription: "/{cmd} — {_esc(desc)}"\n---\n'
        f"{GEN_MARKER}\n\n"
        f"# /{cmd} — {title}\n\n"
        f"Thin wrapper — the full methodology lives in the skill.\n\n"
        f"## Steps\n{step1}{step2}"
        f"3. Run the workflow's Quality Gate before delivering.\n"
    )


def shim_body(cmd: str, target_rel: str, desc: str) -> str:
    return (
        f'---\ndescription: "/{cmd} — {_esc(desc)}"\n---\n'
        f"{GEN_MARKER}\n\n"
        f"Read and execute the workflow at `{target_rel}` - /{cmd} — {desc}\n"
    )


# ──────────────────────────────────────────────────────────────────────────
# planning
# ──────────────────────────────────────────────────────────────────────────

def _is_ours(path: Path) -> bool:
    return path.exists() and GEN_MARKER in _read_text(path)


def build_plan(data: Dict[str, Any], scope: str, skill_filter: Optional[str]) -> Dict[str, Any]:
    entries = data["entries"]
    taken = {p.stem for p in CMD_DIR.glob("*.md")} | {p.stem for p in WF_DIR.glob("*.md")}

    reachable_by_skill: Dict[str, List[str]] = {}
    for e in entries:
        if e["kind"] == "skill-workflow" and e["menu_status"] == "reachable":
            reachable_by_skill.setdefault(e["skill"], []).append(e["id"])

    writes: List[Dict[str, str]] = []
    skipped: List[Dict[str, str]] = []

    # Class A — skill workflows with no wrapper and no shim.
    for e in entries:
        if e["kind"] != "skill-workflow" or e["menu_status"] != "unreachable":
            continue
        if skill_filter and e["skill"] != skill_filter:
            continue
        cmd = choose_command_name(e["id"], e["skill"], taken, reachable_by_skill.get(e["skill"], []))
        if not cmd:
            skipped.append({"path": e["path"], "reason": "every candidate name collides"})
            continue
        wf_target, cmd_target = WF_DIR / f"{cmd}.md", CMD_DIR / f"{cmd}.md"
        if (wf_target.exists() and not _is_ours(wf_target)) or (cmd_target.exists() and not _is_ours(cmd_target)):
            skipped.append({"path": e["path"], "reason": f"/{cmd} exists and is hand-written — never clobbered"})
            continue
        desc = e["description"] or _title(ROOT / e["path"], cmd)
        writes.append({"class": "A", "cmd": cmd, "file": str(wf_target.relative_to(ROOT)), "skill": e["skill"],
                       "body": wrapper_body(cmd, e["skill"], e["path"], ROOT / e["path"], desc)})
        writes.append({"class": "A", "cmd": cmd, "file": str(cmd_target.relative_to(ROOT)), "skill": e["skill"],
                       "body": shim_body(cmd, f".agent/workflows/{cmd}.md", desc)})
        taken.add(cmd)

    # Class B — wrapper exists, shim missing: invisible in the native `/` menu.
    if scope == "all" and not skill_filter:
        for e in entries:
            if e["kind"] != "command-workflow" or e["menu_status"] != "unreachable":
                continue
            target = CMD_DIR / f"{e['id']}.md"
            if target.exists() and not _is_ours(target):
                skipped.append({"path": e["path"], "reason": "shim exists and is hand-written"})
                continue
            desc = e["description"] or e["id"].replace("-", " ")
            writes.append({"class": "B", "cmd": e["id"], "file": str(target.relative_to(ROOT)), "skill": "",
                           "body": shim_body(e["id"], e["path"], desc)})

    # Class C — skills with no front door. sync_registries.py owns these.
    missing_front_doors = [e["id"] for e in entries
                           if e["kind"] == "skill" and e["menu_status"] == "unreachable"]
    return {"writes": writes, "skipped": skipped, "missing_front_doors": missing_front_doors}


def apply_plan(plan: Dict[str, Any], limit_families: Optional[int]) -> int:
    writes = plan["writes"]
    if limit_families:
        keep, seen = [], []
        for w in writes:
            fam = w["skill"] or "_commands"
            if fam not in seen:
                if len(seen) >= limit_families:
                    continue
                seen.append(fam)
            keep.append(w)
        writes = keep
    for w in writes:
        target = ROOT / w["file"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(w["body"], encoding="utf-8")
    return len(writes)


def main() -> int:
    ap = argparse.ArgumentParser(description="Mint menu wrappers + shims for built-but-unfireable workflows.")
    ap.add_argument("--scope", default="all", help="'all' or 'skill'")
    ap.add_argument("skill", nargs="?", help="Skill name when --scope skill")
    ap.add_argument("--apply", action="store_true", help="Write files. Without this, nothing is written.")
    ap.add_argument("--dry-run", action="store_true", help="Explicit no-op (the default).")
    ap.add_argument("--report", action="store_true", help="Emit the plan as JSON.")
    ap.add_argument("--limit-families", type=int, help="Cap how many skill families this run touches.")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    data = arsenal_index.load_or_build(force=True)
    plan = build_plan(data, args.scope, args.skill if args.scope == "skill" else None)

    if args.report:
        print(json.dumps({"writes": [{k: v for k, v in w.items() if k != "body"} for w in plan["writes"]],
                          "skipped": plan["skipped"],
                          "missing_front_doors": plan["missing_front_doors"]}, indent=1))
        return 0

    cmds = sorted({w["cmd"] for w in plan["writes"]})
    if not args.apply:
        if not args.quiet:
            print(f"DRY RUN — would mint {len(cmds)} command(s) across {len(plan['writes'])} file(s). "
                  f"Nothing written.")
            for c in cmds[:20]:
                print(f"  /{c}")
            if len(cmds) > 20:
                print(f"  … and {len(cmds) - 20} more")
            for s in plan["skipped"][:10]:
                print(f"  SKIP {s['path']}: {s['reason']}")
            if plan["missing_front_doors"]:
                print(f"  NOTE {len(plan['missing_front_doors'])} skill(s) lack a front door — "
                      f"run `python3 execution/sync_registries.py` (owns skill-level shims)")
        return 0

    n = apply_plan(plan, args.limit_families)
    arsenal_index.load_or_build(force=True)  # refresh so status reflects the mint
    if not args.quiet:
        print(f"MINTED {n} file(s) — {len(cmds)} command(s) now fireable.")
        if plan["skipped"]:
            print(f"SKIPPED {len(plan['skipped'])} (collision or hand-written; see --report).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
