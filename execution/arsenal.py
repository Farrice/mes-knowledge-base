#!/usr/bin/env python3
"""
arsenal.py — "what do I already have for this?"

WHY THIS EXISTS
---------------
The system builds faster than any human can remember. 378 skills, 231 agents,
~2,500 skill workflows, ~1,850 command workflows. `/recommend` names an EXPERT;
`/find-skill` names a SKILL; neither could name the specific WORKFLOW, because
nothing indexed workflow granularity until arsenal_index.py. The practical cost
was rebuilding assets that already existed and forgetting the good ones.

This is the browse-and-recall surface. It is deliberately a CLI: output is a
few hundred tokens on demand, unlike reading a 400KB markdown index into
context just to see what exists.

NEW CORPUS, NOT A NEW RANKER
-----------------------------
Ranking calls `find_skill.rank` directly — the same BM25, tokenizer, query
expansion, and Production-Core boost that already route this system. A second
scoring engine would drift from the first and quietly disagree about what is
relevant.

Usage:
    python3 execution/arsenal.py "write a cold email that converts"
    python3 execution/arsenal.py --family luke-iha-vicious-hooks
    python3 execution/arsenal.py --unused          # built, never fired
    python3 execution/arsenal.py --new 14          # built in the last 14 days
    python3 execution/arsenal.py --stats
"""
from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "execution"))

import arsenal_index  # noqa: E402
import find_skill  # noqa: E402

DIM, BOLD, RESET = "\033[2m", "\033[1m", "\033[0m"
KIND_LABEL = {
    "command-workflow": "command",
    "skill-workflow": "workflow",
    "skill": "skill",
    "agent": "agent",
}


def _supports_color() -> bool:
    return sys.stdout.isatty()


def _fmt(text: str, code: str) -> str:
    return f"{code}{text}{RESET}" if _supports_color() else text


def _invocation(e: Dict[str, Any]) -> str:
    """How you actually fire this thing — the whole point of the listing."""
    if e["kind"] in ("command-workflow", "skill", "agent"):
        return f"/{e['id']}"
    if e["menu_status"] == "reachable":
        return f"/{e['id']}"
    return f"({e['skill']} → {Path(e['path']).stem})"


def _row(e: Dict[str, Any], width: int = 42) -> str:
    inv = _invocation(e)
    desc = " ".join((e.get("description") or "").split())
    if len(desc) > 96:
        desc = desc[:95].rsplit(" ", 1)[0] + "…"
    tag = "" if e["menu_status"] == "reachable" else _fmt("  [not fireable]", DIM)
    return f"  {_fmt(inv.ljust(width), BOLD)} {desc}{tag}"


def _as_rankable(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Shape arsenal entries into what find_skill.rank expects."""
    out = []
    for e in entries:
        out.append({
            "name": e["id"].replace("-", " "),
            "directory": e.get("skill") or e["id"],
            "description": e.get("description") or "",
            "when_to_use": (e.get("family") or ""),
            "routing": "",
            "_entry": e,
        })
    return out


def cmd_search(data: Dict[str, Any], query: str, top: int) -> int:
    entries = [e for e in data["entries"] if e["kind"] != "skill-workflow"
               or e["menu_status"] != "exempt"]
    scored = find_skill.rank(_as_rankable(entries), query, top=top * 4)
    if not scored:
        print(f'ARSENAL — no matches for "{query}". Try fewer / plainer words, '
              f'or `python3 execution/arsenal.py --stats` to see the shape of what exists.')
        return 0

    buckets: Dict[str, List[Dict[str, Any]]] = {"command": [], "workflow": [], "skill": [], "agent": []}
    for doc, _score in scored:
        e = doc["_entry"]
        b = KIND_LABEL[e["kind"]]
        if len(buckets[b]) < top:
            buckets[b].append(e)

    print(f'\nARSENAL — "{query}"\n')
    titles = [("command", "READY TO FIRE — command workflows"),
              ("workflow", "INSIDE SKILLS — expert workflows"),
              ("skill", "LOAD THE EXPERT — skills"),
              ("agent", "AGENTS")]
    for key, title in titles:
        if not buckets[key]:
            continue
        print(_fmt(f"▎{title}", BOLD))
        for e in buckets[key]:
            print(_row(e))
        print()
    print(_fmt("  Deepen: `python3 execution/arsenal.py --family <skill>` · "
               "full advisory: `/recommend`\n", DIM))
    return 0


def cmd_family(data: Dict[str, Any], family: str) -> int:
    entries = [e for e in data["entries"]
               if (e.get("skill") == family or e["id"] == family)]
    if not entries:
        near = sorted({e["skill"] for e in data["entries"]
                       if e.get("skill") and family.lower() in e["skill"].lower()})
        print(f"No family '{family}'." + (f" Did you mean: {', '.join(near[:6])}?" if near else ""))
        return 1
    skill_entry = next((e for e in entries if e["kind"] == "skill"), None)
    wfs = sorted([e for e in entries if e["kind"] == "skill-workflow"], key=lambda e: e["id"])
    print(f"\nARSENAL — {_fmt(family, BOLD)}")
    if skill_entry:
        desc = " ".join((skill_entry.get("description") or "").split())
        print(f"  {desc[:200]}")
        if skill_entry.get("front_door"):
            print(f"  Front door: {_fmt(skill_entry['front_door'], BOLD)}")
    unreachable = [e for e in wfs if e["menu_status"] == "unreachable"]
    print(f"\n{_fmt(f'▎{len(wfs)} workflow(s)', BOLD)}"
          + (f"  ({len(unreachable)} not yet fireable)" if unreachable else ""))
    for e in wfs:
        print(_row(e, width=46))
    if unreachable:
        print(_fmt(f"\n  Make them fireable: "
                   f"`python3 execution/mint_menu_wrappers.py --scope skill {family} --apply`", DIM))
    print()
    return 0


def cmd_unused(data: Dict[str, Any], limit: int) -> int:
    """Built, high-grade, and no evidence of ever being routed to.

    'No evidence' is not 'never used' — the router log only covers routed
    invocations, so a command Farrice types directly leaves no trace here. The
    list is a memory jog, not an indictment, and it says so.
    """
    cands = [e for e in data["entries"]
             if e["kind"] == "skill-workflow" and not e.get("last_fired")
             and e["menu_status"] == "reachable" and e.get("has_prompts_v2")]
    cands.sort(key=lambda e: -e["mtime"])
    print(f"\n{_fmt('ARSENAL — built, forge-grade, no routing evidence', BOLD)}")
    print(_fmt("  (the router log only records ROUTED calls — anything you typed "
               "directly still shows here)\n", DIM))
    by_skill: Dict[str, List[Dict[str, Any]]] = {}
    for e in cands:
        by_skill.setdefault(e["skill"], []).append(e)
    for skill, items in list(by_skill.items())[:limit]:
        print(_fmt(f"▎{skill}", BOLD) + f"  ({len(items)})")
        for e in items[:4]:
            print(_row(e, width=46))
        print()
    print(_fmt(f"  {len(cands)} total across {len(by_skill)} families.\n", DIM))
    return 0


def cmd_new(data: Dict[str, Any], days: int) -> int:
    cutoff = time.time() - days * 86400
    fresh = [e for e in data["entries"]
             if e["mtime"] >= cutoff and e["kind"] in ("skill-workflow", "command-workflow")]
    fresh.sort(key=lambda e: -e["mtime"])
    print(f"\n{_fmt(f'ARSENAL — built in the last {days} day(s)', BOLD)}  ({len(fresh)})\n")
    for e in fresh[:60]:
        print(_row(e, width=46))
    if len(fresh) > 60:
        print(_fmt(f"\n  … and {len(fresh) - 60} more", DIM))
    print()
    return 0


def cmd_stats(data: Dict[str, Any]) -> int:
    entries = data["entries"]
    kinds: Dict[str, int] = {}
    unreachable = 0
    for e in entries:
        kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
        if e["menu_status"] == "unreachable":
            unreachable += 1
    fams = {e["family"] for e in entries if e.get("family")}
    print(f"\n{_fmt('ARSENAL', BOLD)} — {len(entries)} assets\n")
    for k, v in sorted(kinds.items(), key=lambda kv: -kv[1]):
        print(f"  {k:20s} {v:5d}")
    print(f"\n  {'named families':20s} {len(fams):5d}")
    print(f"  {'not fireable':20s} {unreachable:5d}"
          + ("  ← run the minter" if unreachable else "  ✓ parity clean"))
    print()
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Browse and search everything this system can do.")
    ap.add_argument("query", nargs="*", help="Natural-language task.")
    ap.add_argument("--family", help="Show one skill family in full.")
    ap.add_argument("--unused", action="store_true", help="Forge-grade assets with no routing evidence.")
    ap.add_argument("--new", type=int, metavar="DAYS", help="Assets built in the last N days.")
    ap.add_argument("--stats", action="store_true", help="Counts by kind + parity status.")
    ap.add_argument("--top", type=int, default=6, help="Matches per section (default 6).")
    args = ap.parse_args()

    data = arsenal_index.load_or_build()

    if args.stats:
        return cmd_stats(data)
    if args.unused:
        return cmd_unused(data, limit=12)
    if args.new is not None:
        return cmd_new(data, args.new)
    if args.family:
        return cmd_family(data, args.family)
    if args.query:
        return cmd_search(data, " ".join(args.query), args.top)
    return cmd_stats(data)


if __name__ == "__main__":
    raise SystemExit(main())
