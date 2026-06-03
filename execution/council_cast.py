#!/usr/bin/env python3
"""
Council Cast — the casting layer for the Collective Genius Council.

Mirrors research_personas.py, but for general creative/intelligence work instead
of research. Given a task, it convenes a DELIBERATELY DIVERSE, cross-domain set of
experts from the 89-card roster (agents/_framework/invocation-cards.md), seats
Farrice's own lens, and resolves each member's genius.md so the inner council can
think like the real expert.

The cross-pollination is engineered: relevance picks the core voices, a per-domain
cap stops the council from being 10 copywriters, and 1-2 WILDCARDS from
unrepresented domains are seated on purpose — that collision is where net-new
ideas (the "what no single expert teaches" synthesis) come from.

Pure planning logic (no network). Consumed by `research.py`-style `convene` and the
collective-genius-council workflow.

CLI:
    python3 execution/council_cast.py "<task>" [--mode wide|tight|strike|deploy]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / "agents" / "_framework" / "invocation-cards.md"
SKILLS = ROOT / "skills"

# mode → (wide roster size, inner-council size, per-domain cap, wildcards)
MODE_SHAPE = {
    "wide":   {"roster": 12, "inner": 6, "cap": 3, "wild": 2},   # wide-then-deep default
    "deploy": {"roster": 16, "inner": 6, "cap": 3, "wild": 2},   # max breadth
    "tight":  {"roster": 6,  "inner": 4, "cap": 2, "wild": 1},   # /council, /roundtable
    "strike": {"roster": 3,  "inner": 3, "cap": 2, "wild": 0},   # fast focused
}

# Farrice is always seated — his taste + cross-domain inductive lens + Anti-Guru
# filter is the final gate (FARRICE.md).
FARRICE_SEAT = {
    "name": "Farrice (you)",
    "domain_group": "Taste & Alignment",
    "core_method": "Inductive cross-domain pattern synthesis; Anti-Guru authenticity filter; "
                   "'does this feel aligned, not just optimized?' — the final taste gate.",
    "best_for": "taste, alignment, cross-pollination, what's real vs performative",
    "entry_prompt": "FARRICE.md",
    "pairs_with": [],
    "genius_path": "FARRICE.md",
    "is_user": True,
}


def parse_cards() -> List[Dict]:
    """Parse invocation-cards.md into card dicts, tagged with their ## section domain."""
    if not CARDS.exists():
        return []
    text = CARDS.read_text(encoding="utf-8", errors="ignore")
    cards: List[Dict] = []
    section = "General"
    in_block = False
    buf: List[str] = []
    for line in text.splitlines():
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        if line.strip().startswith("```"):
            if in_block:  # closing a block → parse it
                card = _parse_block(buf, section)
                if card:
                    cards.append(card)
                buf = []
            in_block = not in_block
            continue
        if in_block:
            buf.append(line)
    return cards


def _parse_block(lines: List[str], section: str) -> Optional[Dict]:
    fields: Dict[str, str] = {}
    for ln in lines:
        if ":" in ln:
            k, _, v = ln.partition(":")
            fields[k.strip().upper()] = v.strip()
    name = fields.get("AGENT")
    if not name:
        return None
    pairs = [p.strip() for p in re.split(r"[,;]", fields.get("PAIRS WITH", "")) if p.strip()]
    return {
        "name": name,
        "domain_group": section,
        "domain": fields.get("DOMAIN", ""),
        "core_method": fields.get("CORE METHOD", ""),
        "best_for": fields.get("BEST FOR", ""),
        "entry_prompt": fields.get("ENTRY PROMPT", ""),
        "pairs_with": pairs,
    }


_STOP = set("the a an and or of for to in on with your you how what when build make create "
            "design write content from this that into more about i'm im need want help".split())


def _keywords(text: str) -> set:
    toks = re.findall(r"[a-zA-Z][a-zA-Z\-']{2,}", text.lower())
    return {t for t in toks if t not in _STOP}


def _relevance(card: Dict, kws: set) -> int:
    hay = (card["domain"] + " " + card["best_for"] + " " + card["core_method"] + " "
           + card["domain_group"]).lower()
    return sum(1 for k in kws if k in hay)


def _skill_slugs() -> List[str]:
    try:
        return [d.name for d in SKILLS.iterdir() if d.is_dir()]
    except Exception:
        return []


def _genius_path(card: Dict, slugs: List[str]) -> Optional[str]:
    """Resolve skills/<dir>/genius.md for a card (entry-prompt path first, then slug match)."""
    ep = card.get("entry_prompt", "")
    m = re.match(r"skills/([^/]+)/", ep)
    if m:
        g = SKILLS / m.group(1) / "genius.md"
        if g.exists():
            return f"skills/{m.group(1)}/genius.md"
    # fallback: match a skill dir by the expert's last-name token
    last = card["name"].lower().split()[-1].strip("().") if card["name"] else ""
    if last and len(last) > 2:
        for s in slugs:
            if last in s and (SKILLS / s / "genius.md").exists():
                return f"skills/{s}/genius.md"
    return None


def build_council_plan(task: str, mode: str = "wide") -> Dict:
    """Convene a deliberately diverse cross-domain council for a task."""
    shape = MODE_SHAPE.get(mode, MODE_SHAPE["wide"])
    cards = parse_cards()
    slugs = _skill_slugs()
    kws = _keywords(task)

    scored = sorted(cards, key=lambda c: _relevance(c, kws), reverse=True)

    # Greedy relevance pick with a per-domain cap (stops domain monoculture).
    roster: List[Dict] = []
    group_count: Dict[str, int] = {}
    core_target = shape["roster"] - shape["wild"]
    for c in scored:
        if len(roster) >= core_target:
            break
        g = c["domain_group"]
        if group_count.get(g, 0) >= shape["cap"]:
            continue
        if _relevance(c, kws) == 0 and len(roster) >= 3:
            continue  # don't pad the core with zero-relevance cards
        roster.append(c)
        group_count[g] = group_count.get(g, 0) + 1

    # WILDCARDS — deliberately seat voices from UNREPRESENTED domains for
    # cross-pollination. Prefer a maximally-different lens (philosophy, creative,
    # a domain the core ignored).
    represented = set(group_count)
    wild_pool = [c for c in cards if c["domain_group"] not in represented]
    # bias toward perspective-shifting domains
    def _wild_rank(c):
        bonus = 2 if any(w in c["domain_group"].lower()
                         for w in ["philosophy", "consciousness", "creative", "writing", "humor"]) else 0
        return bonus
    wild_pool.sort(key=_wild_rank, reverse=True)
    wildcards = wild_pool[:shape["wild"]]
    for c in wildcards:
        c = dict(c)
        c["wildcard"] = True
        roster.append(c)

    # Resolve genius paths + tag.
    for c in roster:
        c["genius_path"] = _genius_path(c, slugs)
        c.setdefault("wildcard", False)

    # Always seat Farrice.
    roster.append(dict(FARRICE_SEAT))

    domains = sorted({c["domain_group"] for c in roster})
    return {
        "task": task,
        "mode": mode,
        "roster_size": len(roster),
        "domains_represented": domains,
        "domain_count": len(domains),
        "inner_council_size": shape["inner"],
        "wildcards": [c["name"] for c in roster if c.get("wildcard")],
        "roster": [
            {
                "name": c["name"],
                "domain_group": c["domain_group"],
                "core_method": c["core_method"],
                "lens": c["best_for"],
                "pairs_with": c.get("pairs_with", []),
                "genius_path": c.get("genius_path"),
                "wildcard": c.get("wildcard", False),
                "is_user": c.get("is_user", False),
            }
            for c in roster
        ],
    }


def council_member_prompt(member: Dict, task: str) -> str:
    """The DIVERGE brief each council member gets (card-level, independent take)."""
    wild = " (you are the WILDCARD voice — bring your outsider lens precisely because it doesn't obviously fit)" if member.get("wildcard") else ""
    if member.get("is_user"):
        return (
            f"You are **Farrice's own lens** (taste + alignment + Anti-Guru filter).\n\n"
            f"## The task\n{task}\n\n"
            f"Give the take only YOU would: where does the obvious expert move feel performative or "
            f"misaligned? What cross-domain pattern (gaming, spirituality, systems) reframes this? "
            f"What would make this feel real, not just optimized?\n"
            f"Return JSON {{take, signature_angle, the_move}} — `the_move` = the single sharpest contribution."
        )
    return (
        f"You are **{member['name']}** — {member['domain_group']}{wild}.\n"
        f"Your method: {member['core_method']}\n"
        f"Your lens: {member['lens']}\n\n"
        f"## The task\n{task}\n\n"
        f"Give YOUR distinctive take — the angle only you, through your method, would see. "
        f"Don't be comprehensive; be unmistakably yourself. If you'd lean on a fact/number, ground it "
        f"(`python3 execution/research.py \"<q>\" --depth quick`) or flag it as an assumption.\n"
        f"Return JSON {{take, signature_angle, the_move}} where `the_move` is your single sharpest, "
        f"most stealable contribution to this problem."
    )


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(prog="council_cast.py")
    p.add_argument("task")
    p.add_argument("--mode", default="wide", choices=list(MODE_SHAPE.keys()))
    a = p.parse_args()
    print(json.dumps(build_council_plan(a.task, a.mode), indent=2))
