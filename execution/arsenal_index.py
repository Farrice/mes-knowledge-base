#!/usr/bin/env python3
"""
arsenal_index.py — the workflow-granularity index of everything invocable.

WHY THIS EXISTS
---------------
Nothing in the repo indexed `skills/*/workflows/*.md`. `find_skill.py` indexes
only `skills/*/SKILL.md` (371 entries); `sync_registries.py` mints one command
shim per SKILL, never per workflow. The result was one root cause with two
symptoms, measured 2026-07-25:

  1. BUILT BUT NOT FIREABLE — hundreds of workflows on disk with no wrapper and
     no shim, so they could not be invoked at all.
  2. BUILT BUT NOT REMEMBERED — no surface could answer "what do I already have
     for this task?" at workflow granularity, so assets got rebuilt.

This module is the spine that fixes both. `mint_menu_wrappers.py` reads it to
close symptom 1; `arsenal.py` reads it to close symptom 2.

REACHABILITY IS DEFINED IN EXACTLY ONE PLACE
--------------------------------------------
The `_menu_surfaces` / `_MENU_EXEMPT_RE` / `_MENU_VARIANT_RE` primitives are
IMPORTED from `skill_auditor.py` (heartbeat check 7), never re-implemented. If
this file and the auditor ever disagreed about what "reachable" means, the
minter would mint wrappers the auditor still counts as missing — an infinite
housekeeping loop. One definition, imported.

Usage:
    python3 execution/arsenal_index.py              # build (cached) + summary
    python3 execution/arsenal_index.py --rebuild    # force full rebuild
    python3 execution/arsenal_index.py stats        # counts by kind + menu status
    python3 execution/arsenal_index.py drift        # unreachable workflows, by skill
    python3 execution/arsenal_index.py drift --json # machine-readable (minter input)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "execution"))

# One definition of "menu-reachable" — imported from heartbeat check 7.
from skill_auditor import (  # noqa: E402
    _MENU_EXEMPT_RE,
    _MENU_VARIANT_RE,
    _menu_surfaces,
    _read_text,
)
# Description extraction + expert-family grouping already solved here.
from generate_slash_commands import extract_description, family_for  # noqa: E402

INDEX_PATH = ROOT / ".agent" / "arsenal-index.json"
SKILLS_DIR = ROOT / "skills"
# Vendored third-party skill systems (Simon Scrapes Skill Systems, installed
# 2026-09-02 via @scrapes/installer). Claude Code exposes .claude/skills/<name>
# natively as /<name>; Codex sees them through .agents/skills/<name> symlinks.
# Indexed here so /arsenal and the router hook surface them next to skills/.
VENDOR_SKILLS_DIR = ROOT / ".claude" / "skills"
AGENTS_DIR = ROOT / "agents"
WF_DIR = ROOT / ".agent" / "workflows"
CMD_DIR = ROOT / ".claude" / "commands"
ROUTING_PATH = ROOT / ".agent" / "routing-intelligence.json"

SCHEMA_VERSION = 1

# Status values. `exempt` is a NAMED decision (menu_exempt:/superseded), not a
# silent skip — the whole point of check 7 is that silence hid 670 workflows.
REACHABLE, UNREACHABLE, EXEMPT = "reachable", "unreachable", "exempt"

_H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.M)
# Wrappers and shims prefix their own command onto the description
# ("/foo — does a thing"). Listing that verbatim under a "/foo" column reads as
# "/foo  /foo — does a thing". Strip the echo, keep the meaning.
_SELF_PREFIX_RE = re.compile(r"^/[a-z0-9][a-z0-9-]*\s*[—:-]\s*")


# ──────────────────────────────────────────────────────────────────────────
# description
# ──────────────────────────────────────────────────────────────────────────

def _describe(path: Path) -> str:
    """Frontmatter description → first H1 → first prose sentence."""
    desc = extract_description(path)
    if desc:
        return _SELF_PREFIX_RE.sub("", desc)[:400]
    raw = _read_text(path)
    m = _H1_RE.search(raw)
    if m:
        return _SELF_PREFIX_RE.sub("", m.group(1).strip())[:400]
    for line in raw.splitlines():
        line = line.strip()
        if line and not line.startswith(("---", "#", "|", ">", "`", "<!--")):
            return line[:400]
    return ""


# ──────────────────────────────────────────────────────────────────────────
# usage evidence
# ──────────────────────────────────────────────────────────────────────────

def _last_fired() -> Dict[str, str]:
    """command/skill id -> most recent routing timestamp, from the router log.

    Best-effort: the routing log is a learning surface, not an audit trail, so a
    missing entry means "no evidence", never "never used". `arsenal --unused`
    labels it that way rather than asserting a negative.
    """
    try:
        data = json.loads(ROUTING_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}
    seen: Dict[str, str] = {}

    def note(val: Any, ts: str) -> None:
        if isinstance(val, str) and val.strip():
            name = val.strip().lstrip("@/")
            if ts > seen.get(name, ""):
                seen[name] = ts

    for rec in data.get("routing_decisions", []) or []:
        if not isinstance(rec, dict):
            continue
        ts = str(rec.get("timestamp") or rec.get("ts") or "")
        # The real schema is workflow_used + experts_deployed (a list). An earlier
        # guess at generic key names ("chosen"/"route"/"target") matched ZERO of
        # 657 records, so every asset looked unused — a broken signal is worse
        # than no signal, because it reads as a finding.
        note(rec.get("workflow_used"), ts)
        deployed = rec.get("experts_deployed")
        for item in (deployed if isinstance(deployed, list) else [deployed]):
            note(item, ts)
    return seen


# ──────────────────────────────────────────────────────────────────────────
# entry builders
# ──────────────────────────────────────────────────────────────────────────

_WF_REF_RE = re.compile(r"skills/([^/]+)/workflows/([^/`\s]+\.md)")


def _command_for_path() -> Dict[str, str]:
    """repo-relative workflow path -> the command that actually fires it.

    A workflow's file stem is NOT reliably its command name: the minter prefixes
    numbered stems (`04-viral-idea-ladder` -> `/jenny-viral-idea-ladder`) because
    `/04-…` is meaningless outside its skill. Reachability came from the wrapper's
    embedded path, so the real command has to be read back off that wrapper —
    otherwise every consumer prints an invocation that does not exist.
    """
    out: Dict[str, str] = {}
    # Both surfaces: some workflows are referenced straight from a .claude/commands
    # shim with no .agent/workflows wrapper. Scanning only WF_DIR left those with a
    # null command even though they were reachable.
    for wrapper in list(WF_DIR.glob("*.md")) + list(CMD_DIR.glob("*.md")):
        m = _WF_REF_RE.search(_read_text(wrapper))
        if m:
            out.setdefault(f"skills/{m.group(1)}/workflows/{m.group(2)}", wrapper.stem)
    return out


def _skill_workflow_entries(cmd_stems, wrapper_blob, fired) -> List[Dict[str, Any]]:
    """Every skills/<skill>/workflows/<wf>.md, with its true menu status.

    Reachability mirrors skill_auditor.heartbeat_checks check 7 exactly:
    same-stem command in .claude/commands/, OR the full repo-relative path
    referenced by some wrapper/shim.
    """
    out: List[Dict[str, Any]] = []
    by_path = _command_for_path()
    for wf in sorted(SKILLS_DIR.glob("*/workflows/*.md")):
        skill = wf.parent.parent.name
        if _MENU_VARIANT_RE.search(wf.name):
            continue  # variant/backup artifact — not a live asset
        head = _read_text(wf)[:600]
        ref = f"skills/{skill}/workflows/{wf.name}"
        if _MENU_EXEMPT_RE.search(head):
            status = EXEMPT
        else:
            status = REACHABLE if (wf.stem in cmd_stems or ref in wrapper_blob) else UNREACHABLE
        command = (wf.stem if wf.stem in cmd_stems else by_path.get(ref))
        out.append({
            "id": wf.stem,
            "command": command,
            "kind": "skill-workflow",
            "skill": skill,
            "path": str(wf.relative_to(ROOT)),
            "description": _describe(wf),
            "menu_status": status,
            "front_door": f"/{skill}" if (CMD_DIR / f"{skill}.md").exists() else None,
            "has_prompts_v2": (SKILLS_DIR / skill / "references" / "prompts-v2").is_dir(),
            "family": family_for(wf.stem) or family_for(skill),
            "last_fired": fired.get(command or wf.stem) or fired.get(wf.stem),
            # Routing logs record the SKILL/workflow that was deployed, rarely an
            # individual sub-workflow. Parent evidence separates "this expert has
            # never been deployed at all" (genuinely forgotten) from "expert is in
            # rotation, this particular sub-workflow may not be".
            "skill_last_fired": fired.get(skill),
            "mtime": wf.stat().st_mtime,
        })
    return out


def _command_workflow_entries(cmd_stems, fired) -> List[Dict[str, Any]]:
    """.agent/workflows/*.md — already the menu; reachable iff a shim exists."""
    out: List[Dict[str, Any]] = []
    for wf in sorted(WF_DIR.glob("*.md")):
        head = _read_text(wf)[:600]
        out.append({
            "id": wf.stem,
            "kind": "command-workflow",
            "skill": None,
            "path": str(wf.relative_to(ROOT)),
            "description": _describe(wf),
            "menu_status": EXEMPT if _MENU_EXEMPT_RE.search(head)
                           else (REACHABLE if wf.stem in cmd_stems else UNREACHABLE),
            "front_door": f"/{wf.stem}",
            "has_prompts_v2": False,
            "family": family_for(wf.stem),
            "last_fired": fired.get(wf.stem),
            "mtime": wf.stat().st_mtime,
        })
    return out


def _skill_front_doors() -> Dict[str, str]:
    """skill -> the command that loads its SKILL.md.

    An exact name match is NOT the only front door: many skills are fired by a
    shorter alias (`/ai-carousel` loads `ai-carousel-content-engine`, `/cos` loads
    `chief-of-staff-os`). Checking names alone reported 74 phantom gaps — and a
    gauge that cries wolf is a gauge that gets ignored.
    """
    out: Dict[str, str] = {}
    for cmd in list(CMD_DIR.glob("*.md")) + list(WF_DIR.glob("*.md")):
        for m in re.finditer(r"skills/([^/]+)/SKILL\.md", _read_text(cmd)):
            out.setdefault(m.group(1), cmd.stem)
    return out


def _skill_entries(cmd_stems, fired) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    doors = _skill_front_doors()
    for sm in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        skill = sm.parent.name
        head = _read_text(sm)[:600]
        if re.search(r"^\s*status\s*:\s*archived\b", head, re.I | re.M):
            continue  # de-indexed per directory conventions
        wfs = [w for w in (sm.parent / "workflows").glob("*.md")
               if not _MENU_VARIANT_RE.search(w.name)]
        door = skill if skill in cmd_stems else doors.get(skill)
        out.append({
            "id": skill,
            "kind": "skill",
            "skill": skill,
            "path": str(sm.relative_to(ROOT)),
            "description": _describe(sm),
            "menu_status": REACHABLE if door else UNREACHABLE,
            "front_door": f"/{door}" if door else None,
            "has_prompts_v2": (sm.parent / "references" / "prompts-v2").is_dir(),
            "family": family_for(skill),
            "workflow_count": len(wfs),
            "last_fired": fired.get(skill),
            "mtime": sm.stat().st_mtime,
        })
    return out


def _vendor_skill_entries(fired) -> List[Dict[str, Any]]:
    """Third-party skills under .claude/skills/ (Scrapes Skill Systems etc.).

    Always menu-reachable: Claude Code mounts .claude/skills/<name> as /<name>
    with no wrapper needed. Symlinks back into .agents/skills are skipped so
    the Pocock suite never double-indexes.
    """
    out: List[Dict[str, Any]] = []
    if not VENDOR_SKILLS_DIR.is_dir():
        return out
    for sm in sorted(VENDOR_SKILLS_DIR.glob("*/SKILL.md")):
        skill = sm.parent.name
        if sm.parent.is_symlink():
            continue
        head = _read_text(sm)[:600]
        if re.search(r"^\s*status\s*:\s*archived\b", head, re.I | re.M):
            continue
        out.append({
            "id": f"vendor:{skill}",
            "kind": "skill",
            "skill": skill,
            "path": str(sm.relative_to(ROOT)),
            "description": _describe(sm),
            "menu_status": REACHABLE,
            "front_door": f"/{skill}",
            "has_prompts_v2": False,
            "family": "scrapes-skill-systems",
            "workflow_count": 0,
            "vendor": "scrapes",
            "last_fired": fired.get(skill),
            "mtime": sm.stat().st_mtime,
        })
    return out


def _agent_entries(cmd_stems, fired) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for am in sorted(AGENTS_DIR.glob("*/AGENT.md")):
        agent = am.parent.name
        out.append({
            "id": agent,
            "kind": "agent",
            "skill": None,
            "path": str(am.relative_to(ROOT)),
            "description": _describe(am),
            "menu_status": REACHABLE if agent in cmd_stems else UNREACHABLE,
            "front_door": f"/{agent}" if agent in cmd_stems else None,
            "has_prompts_v2": False,
            "family": family_for(agent),
            "last_fired": fired.get(agent),
            "mtime": am.stat().st_mtime,
        })
    return out


# ──────────────────────────────────────────────────────────────────────────
# build / cache
# ──────────────────────────────────────────────────────────────────────────

def build_index() -> Dict[str, Any]:
    cmd_stems, wrapper_blob = _menu_surfaces()
    fired = _last_fired()
    entries: List[Dict[str, Any]] = []
    entries += _skill_workflow_entries(cmd_stems, wrapper_blob, fired)
    entries += _command_workflow_entries(cmd_stems, fired)
    entries += _skill_entries(cmd_stems, fired)
    entries += _agent_entries(cmd_stems, fired)
    entries += _vendor_skill_entries(fired)
    return {"schema_version": SCHEMA_VERSION, "entries": entries}


def _sources_fingerprint() -> tuple:
    """(count, newest mtime) across every indexed source + both menu surfaces.

    Cheap staleness probe in the spirit of find_skill.load_or_build_index —
    the menu surfaces are included because minting a wrapper changes an entry's
    status without touching the workflow file itself.
    """
    paths = (list(SKILLS_DIR.glob("*/workflows/*.md")) + list(WF_DIR.glob("*.md"))
             + list(SKILLS_DIR.glob("*/SKILL.md")) + list(AGENTS_DIR.glob("*/AGENT.md"))
             + list(VENDOR_SKILLS_DIR.glob("*/SKILL.md"))
             + list(CMD_DIR.glob("*.md")))
    newest = 0.0
    for p in paths:
        try:
            newest = max(newest, p.stat().st_mtime)
        except OSError:
            continue
    return len(paths), round(newest, 3)


def load_or_build(force: bool = False) -> Dict[str, Any]:
    if not force and INDEX_PATH.exists():
        try:
            cached = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        except Exception:
            cached = None
        if (cached and cached.get("schema_version") == SCHEMA_VERSION
                and tuple(cached.get("fingerprint", [])) == _sources_fingerprint()):
            return cached
    data = build_index()
    data["fingerprint"] = list(_sources_fingerprint())
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(data, indent=1), encoding="utf-8")
    return data


def drift(data: Dict[str, Any]) -> Dict[str, List[str]]:
    """Unreachable SKILL workflows grouped by skill — the minter's work-list."""
    out: Dict[str, List[str]] = {}
    for e in data["entries"]:
        if e["kind"] == "skill-workflow" and e["menu_status"] == UNREACHABLE:
            out.setdefault(e["skill"], []).append(e["id"])
    return dict(sorted(out.items(), key=lambda kv: -len(kv[1])))


# ──────────────────────────────────────────────────────────────────────────
# CLI
# ──────────────────────────────────────────────────────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(description="Arsenal index — every invocable asset, at workflow granularity.")
    ap.add_argument("command", nargs="?", default="build", choices=["build", "stats", "drift"])
    ap.add_argument("--rebuild", action="store_true", help="Force a full rebuild, ignoring the cache.")
    ap.add_argument("--json", action="store_true", help="Machine-readable output.")
    args = ap.parse_args()

    data = load_or_build(force=args.rebuild or args.command != "build")
    entries = data["entries"]

    if args.command == "drift":
        d = drift(data)
        total = sum(len(v) for v in d.values())
        if args.json:
            print(json.dumps({"total": total, "by_skill": d}, indent=1))
            return 0
        print(f"UNREACHABLE: {total} workflow(s) across {len(d)} skill(s)")
        for skill, wfs in list(d.items())[:25]:
            print(f"  {skill:48s} {len(wfs):3d}  e.g. {', '.join(wfs[:3])}")
        if len(d) > 25:
            print(f"  … and {len(d) - 25} more skill(s) — use --json for the full list")
        return 0

    kinds: Dict[str, int] = {}
    status: Dict[str, int] = {}
    for e in entries:
        kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
        status[e["menu_status"]] = status.get(e["menu_status"], 0) + 1
    if args.json:
        print(json.dumps({"total": len(entries), "kinds": kinds, "menu_status": status}, indent=1))
        return 0
    print(f"ARSENAL INDEX — {len(entries)} entries  →  {INDEX_PATH.relative_to(ROOT)}")
    for k, v in sorted(kinds.items(), key=lambda kv: -kv[1]):
        print(f"  {k:20s} {v:5d}")
    print("  " + "─" * 26)
    for k, v in sorted(status.items(), key=lambda kv: -kv[1]):
        print(f"  {k:20s} {v:5d}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
