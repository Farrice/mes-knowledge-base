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
    """How you actually fire this thing — the whole point of the listing.

    Never derive this from the file stem: the minter prefixes numbered stems, so
    `04-viral-idea-ladder` fires as `/jenny-viral-idea-ladder`. Printing the stem
    would hand back a command that does not exist.
    """
    if e["kind"] in ("command-workflow", "skill", "agent"):
        return f"/{e['id']}"
    if e.get("command"):
        return f"/{e['command']}"
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
    # "Cold" = the parent expert has NEVER appeared in the routing log. That is a
    # far stronger signal than a missing sub-workflow entry, since the log records
    # skills and top-level workflows, not individual sub-workflows.
    cands = [e for e in data["entries"]
             if e["kind"] == "skill-workflow" and not e.get("last_fired")
             and not e.get("skill_last_fired")
             and e["menu_status"] == "reachable" and e.get("has_prompts_v2")]
    cands.sort(key=lambda e: -e["mtime"])
    warm = sum(1 for e in data["entries"]
               if e["kind"] == "skill-workflow" and e.get("skill_last_fired"))
    print(f"\n{_fmt('ARSENAL — forge-grade, parent expert never routed to', BOLD)}")
    print(_fmt(f"  ({warm} sub-workflows belong to experts that ARE in rotation and are "
               f"excluded. The log records routed calls only — anything typed directly "
               f"leaves no trace, so this is a memory jog, not proof of disuse.)\n", DIM))
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


def _esc(s: str) -> str:
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;").replace('"', "&quot;"))


def cmd_board(data: Dict[str, Any]) -> int:
    """Write the always-open visual arsenal — every command, filterable.

    Design tokens mirror pulse_dashboard.py so the two consoles read as one
    system. Entirely self-contained (no external CSS/JS/fonts) so it publishes
    as an Artifact under a strict CSP.
    """
    entries = [e for e in data["entries"] if e["menu_status"] != "exempt"]
    fams: Dict[str, List[Dict[str, Any]]] = {}
    for e in entries:
        if e["kind"] == "skill-workflow":
            fams.setdefault(e["skill"], []).append(e)
    standalone = sorted([e for e in entries if e["kind"] == "command-workflow"],
                        key=lambda e: e["id"])
    agents = sorted([e for e in entries if e["kind"] == "agent"], key=lambda e: e["id"])

    def card(title: str, front: str, items: List[Dict[str, Any]]) -> str:
        rows = "".join(
            f'<li><code>{_esc(_invocation(i))}</code>'
            f'<span>{_esc(" ".join((i.get("description") or "").split())[:150])}</span></li>'
            for i in sorted(items, key=lambda x: x["id"]))
        head = f'<h3>{_esc(title)} <em>{len(items)}</em></h3>'
        if front:
            head += f'<p class="front">front door <code>{_esc(front)}</code></p>'
        return f'<section class="fam" data-text="{_esc(title.lower())}">{head}<ul>{rows}</ul></section>'

    blocks = []
    for skill in sorted(fams):
        skill_entry = next((e for e in entries if e["kind"] == "skill" and e["id"] == skill), None)
        blocks.append(card(skill, (skill_entry or {}).get("front_door") or "", fams[skill]))
    if standalone:
        blocks.append(card("Standalone command workflows", "", standalone))
    if agents:
        blocks.append(card("Agents", "", agents))

    total = sum(len(v) for v in fams.values()) + len(standalone) + len(agents)
    html = f"""<title>Arsenal — Antigravity</title>
<style>
:root {{ --ground:#f7f7f9; --panel:#fff; --ink:#1c1e28; --muted:#6a6d80; --line:#e3e4ec; --accent:#4c5bd4; }}
@media (prefers-color-scheme: dark) {{
  :root {{ --ground:#12141d; --panel:#191c28; --ink:#e8e9f0; --muted:#8b8fa8; --line:#272b3b; --accent:#8b97ff; }} }}
:root[data-theme="dark"] {{ --ground:#12141d; --panel:#191c28; --ink:#e8e9f0; --muted:#8b8fa8; --line:#272b3b; --accent:#8b97ff; }}
:root[data-theme="light"] {{ --ground:#f7f7f9; --panel:#fff; --ink:#1c1e28; --muted:#6a6d80; --line:#e3e4ec; --accent:#4c5bd4; }}
body {{ background:var(--ground); color:var(--ink); font:15px/1.5 ui-sans-serif,-apple-system,system-ui,sans-serif;
       margin:0; padding:28px 20px 60px; }}
.wrap {{ max-width:1100px; margin:0 auto; }}
h1 {{ font-size:22px; margin:0 0 4px; }}
.sub {{ color:var(--muted); margin:0 0 20px; font-size:14px; }}
#q {{ width:100%; padding:12px 14px; font-size:15px; border-radius:8px; border:1px solid var(--line);
      background:var(--panel); color:var(--ink); margin-bottom:22px; box-sizing:border-box; }}
#q:focus {{ outline:2px solid var(--accent); outline-offset:1px; }}
.fam {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:14px 18px; margin-bottom:14px; }}
.fam h3 {{ font-size:15px; margin:0 0 2px; }}
.fam h3 em {{ font-style:normal; color:var(--muted); font-weight:400; font-size:13px; }}
.front {{ margin:0 0 8px; font-size:12px; color:var(--muted); }}
ul {{ list-style:none; margin:0; padding:0; }}
li {{ display:flex; gap:12px; padding:3px 0; border-top:1px solid var(--line); font-size:13.5px; }}
li:first-child {{ border-top:none; }}
li code {{ color:var(--accent); font-weight:600; flex:0 0 300px; word-break:break-all; }}
li span {{ color:var(--muted); }}
@media (max-width:720px) {{ li {{ flex-direction:column; gap:1px; }} li code {{ flex:none; }} }}
.hide {{ display:none; }}
</style>
<div class="wrap">
<h1>Arsenal</h1>
<p class="sub">{total} fireable assets across {len(fams)} skill families ·
generated by <code>execution/arsenal.py --board</code> · everything here fires from the <code>/</code> menu</p>
<input id="q" type="search" placeholder="Filter — type a command, a family, or words from a description…" autofocus>
{''.join(blocks)}
</div>
<script>
const q=document.getElementById('q');
const fams=[...document.querySelectorAll('.fam')].map(f=>({{el:f,txt:f.innerText.toLowerCase()}}));
q.addEventListener('input',()=>{{
  const t=q.value.trim().toLowerCase();
  for(const f of fams){{
    if(!t){{ f.el.classList.remove('hide'); f.el.querySelectorAll('li').forEach(li=>li.classList.remove('hide')); continue; }}
    const hit=f.txt.includes(t);
    f.el.classList.toggle('hide',!hit);
    if(hit) f.el.querySelectorAll('li').forEach(li=>
      li.classList.toggle('hide', !li.innerText.toLowerCase().includes(t) && !f.el.querySelector('h3').innerText.toLowerCase().includes(t)));
  }}
}});
</script>
"""
    out = ROOT / ".agent" / "pulse" / "arsenal-board.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)} — {total} assets, {len(fams)} families "
          f"({len(html)//1024}KB). Publish it with the Artifact tool.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Browse and search everything this system can do.")
    ap.add_argument("query", nargs="*", help="Natural-language task.")
    ap.add_argument("--family", help="Show one skill family in full.")
    ap.add_argument("--unused", action="store_true", help="Forge-grade assets with no routing evidence.")
    ap.add_argument("--new", type=int, metavar="DAYS", help="Assets built in the last N days.")
    ap.add_argument("--stats", action="store_true", help="Counts by kind + parity status.")
    ap.add_argument("--board", action="store_true",
                    help="Write the filterable HTML arsenal console to .agent/pulse/arsenal-board.html.")
    ap.add_argument("--top", type=int, default=6, help="Matches per section (default 6).")
    args = ap.parse_args()

    data = arsenal_index.load_or_build()

    if args.board:
        return cmd_board(data)
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
