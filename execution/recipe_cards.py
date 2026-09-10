#!/usr/bin/env python3
"""recipe_cards.py — the recipe card library (directives/recipe-card-standard.md).

Born 2026-09-09 from Nate B Jones's manager-loop video: a recipe card names a
real job, sketches its lanes, says what to ask for, what the manager handles
alone, when it comes back, and what to do when work breaks. Cards are LIVING
docs at recipes/<job-slug>.md — no date in the filename, updated in place.

Usage:
  python3 execution/recipe_cards.py list
  python3 execution/recipe_cards.py show <slug>
  python3 execution/recipe_cards.py match "<raw ask>" [--top 3] [--json]
  python3 execution/recipe_cards.py new <slug> --name "<Job name>" --family <F>
  python3 execution/recipe_cards.py parse <slug> --json      # lanes + sections (job_board.py uses this)
  python3 execution/recipe_cards.py lint [slug]              # exit 1 on a broken card

Deterministic, stdlib only, identical under Claude Code and Codex. Nothing here
blocks anything — lint reports, the manager decides.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECIPES = ROOT / "recipes"
FAMILIES = ("client-content", "harvest-research", "revenue-launch", "harness")
REQUIRED_SECTIONS = (
    "The job", "Sub-jobs / lanes", "Ask me first", "Handles alone", "Comes back when",
    "Needs approval", "Needs", "When it breaks", "Done means", "Ratchet log",
)
LANE_RE = re.compile(
    r"^-\s+(?P<id>L\d+[a-z]?)\s+(?P<name>[^—\-]+?)\s+[—-]\s+(?P<desc>.*?)"
    r"(?:\s*\[(?P<tag>parallel|after:\s*[^\]]+)\])?\s*$")
STOP = set("the a an and or of to in for on with into from by is are be this that it as at "
           "your my our his her their i you we they me us them then once after before "
           "every each one two three".split())


# ── parsing ───────────────────────────────────────────────────────────────
def card_path(slug: str) -> Path:
    return RECIPES / f"{slug}.md"


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm = {}
    for line in parts[1].splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            v = v.split("#", 1)[0].strip()
            fm[k.strip()] = v
    return fm, parts[2]


def sections(body: str) -> dict:
    out, cur = {}, None
    for line in body.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            cur = m.group(1).strip()
            out[cur] = []
        elif cur is not None:
            out[cur].append(line)
    return {k: "\n".join(v).strip() for k, v in out.items()}


def parse_lanes(block: str) -> list[dict]:
    lanes = []
    for line in block.splitlines():
        m = LANE_RE.match(line.strip())
        if not m:
            continue
        tag = (m.group("tag") or "parallel").strip()
        after = []
        if tag.startswith("after:"):
            after = [x.strip() for x in tag[6:].split(",") if x.strip()]
        lanes.append({
            "id": m.group("id"), "name": m.group("name").strip(),
            "desc": m.group("desc").strip(), "after": after,
        })
    return lanes


def parse(slug: str) -> dict:
    p = card_path(slug)
    text = p.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    secs = sections(body)
    return {
        "slug": slug, "path": str(p.relative_to(ROOT)), "frontmatter": fm,
        "sections": secs, "lanes": parse_lanes(secs.get("Sub-jobs / lanes", "")),
    }


def all_slugs() -> list[str]:
    if not RECIPES.exists():
        return []
    return sorted(p.stem for p in RECIPES.glob("*.md") if not p.name.startswith("_"))


# ── matching ──────────────────────────────────────────────────────────────
def _terms(text: str) -> list[str]:
    return [w for w in re.findall(r"[a-z][a-z0-9\-]{2,}", text.lower()) if w not in STOP]


def match(ask: str, top: int = 3) -> list[dict]:
    q = set(_terms(ask))
    if not q:
        return []
    scored = []
    for slug in all_slugs():
        try:
            card = parse(slug)
        except Exception:
            continue
        fm, secs = card["frontmatter"], card["sections"]
        heavy = " ".join([slug.replace("-", " "), fm.get("name", ""), fm.get("family", ""),
                          secs.get("The job", "")])
        light = " ".join([secs.get("Sub-jobs / lanes", ""), secs.get("Done means", "")])
        ht, lt = set(_terms(heavy)), set(_terms(light))
        score = 3 * len(q & ht) + len(q & lt)
        # slug words count double again — the job name is the strongest signal
        score += 2 * len(q & set(slug.split("-")))
        if score:
            scored.append({"slug": slug, "name": fm.get("name", slug), "score": score,
                           "family": fm.get("family", "")})
    scored.sort(key=lambda r: (-r["score"], r["slug"]))
    return scored[:top]


# Match floor (2026-09-10 scar): the Coach Cooz job matched the Poppy card on a
# score of 14 and ran Poppy lanes on a website audit. Calibrated on this library:
# right matches score 13-28 and lead the runner-up 3x+ (triage 13/4, Poppy 28/5,
# harvest 26/2, MyBPM 15/2) or sit high beside a true sibling (Jen weekly 20/12);
# the wrong one scored 11-14 with a runner-up close behind (11/7, 14/10, 6/5).
# A weak match is a forge signal, never a plan.
MATCH_STRONG = 15      # at or above: confident on score alone
MATCH_FLOOR = 10       # below: weak no matter what
MATCH_MARGIN = 2.0     # between: confident only when the top leads the runner-up by this


def verdict(rows: list[dict]) -> dict:
    """{'confident': bool, 'reason': str, 'slug': top or None}."""
    if not rows:
        return {"confident": False, "reason": "no card scored", "slug": None}
    top = rows[0]
    second = rows[1]["score"] if len(rows) > 1 else 0
    sc = top["score"]
    if sc >= MATCH_STRONG:
        return {"confident": True, "slug": top["slug"], "reason": f"score {sc} is at or above {MATCH_STRONG}"}
    if sc < MATCH_FLOOR:
        return {"confident": False, "slug": top["slug"], "reason": f"top score {sc} is under the floor {MATCH_FLOOR}"}
    if second and sc < MATCH_MARGIN * second:
        return {"confident": False, "slug": top["slug"],
                "reason": f"top score {sc} does not lead the runner-up ({second}) by {MATCH_MARGIN:g}x"}
    return {"confident": True, "slug": top["slug"], "reason": f"score {sc} leads the runner-up ({second}) by {MATCH_MARGIN:g}x+"}


# ── lint ──────────────────────────────────────────────────────────────────
def lint(slug: str) -> list[str]:
    errs = []
    p = card_path(slug)
    if not p.exists():
        return [f"{slug}: missing {p}"]
    card = parse(slug)
    fm = card["frontmatter"]
    if fm.get("job") != slug:
        errs.append(f"{slug}: frontmatter job '{fm.get('job')}' != filename")
    if fm.get("family") not in FAMILIES:
        errs.append(f"{slug}: family '{fm.get('family')}' not in {FAMILIES}")
    if fm.get("tier_default") not in ("T1", "T2"):
        errs.append(f"{slug}: tier_default must be T1|T2")
    if not re.fullmatch(r"\d+", fm.get("runs", "")):
        errs.append(f"{slug}: runs must be an integer")
    for s in REQUIRED_SECTIONS:
        if s not in card["sections"]:
            errs.append(f"{slug}: missing section '## {s}'")
    lanes = card["lanes"]
    if not lanes:
        errs.append(f"{slug}: no parseable lanes (format: '- L1 name — desc [parallel|after: L1]')")
    ids = {l["id"] for l in lanes}
    for l in lanes:
        for a in l["after"]:
            if a not in ids:
                errs.append(f"{slug}: lane {l['id']} depends on unknown lane {a}")
    body = p.read_text(encoding="utf-8")
    if len(body.splitlines()) > 140:
        errs.append(f"{slug}: {len(body.splitlines())} lines — a card fits on one page (≤140)")
    return errs


# ── new ───────────────────────────────────────────────────────────────────
TEMPLATE = """---
job: {slug}
name: {name}
family: {family}
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
One sentence: the outcome, in Farrice's words.

## Sub-jobs / lanes
- L1 First lane — what it produces [parallel]
- L2 Second lane — what it produces [after: L1]

## Ask me first
- Q: … · look first: <path>

## Handles alone
none

## Comes back when
none

## Needs approval
none

## Needs
none

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| source missing | search, mark UNCONFIRMED | never invent |

## Done means
Verifiable receipts.

## Ratchet log
- none yet
"""


def cmd_new(a):
    p = card_path(a.slug)
    if p.exists() and not a.force:
        print(f"exists: {p} (use --force to overwrite)")
        return 1
    RECIPES.mkdir(exist_ok=True)
    p.write_text(TEMPLATE.format(slug=a.slug, name=a.name, family=a.family), encoding="utf-8")
    print(f"created {p.relative_to(ROOT)} — fill it from the workflows that already run the job")
    return 0


def cmd_list(a):
    rows = []
    for slug in all_slugs():
        try:
            fm = parse(slug)["frontmatter"]
        except Exception as exc:
            rows.append(f"  {slug:<34} (unparseable: {exc.__class__.__name__})")
            continue
        rows.append(f"  {slug:<34} {fm.get('family', ''):<17} runs={fm.get('runs', '?'):<3} "
                    f"ratchet={fm.get('last_ratchet', '?')}  {fm.get('name', '')}")
    print(f"RECIPES ({len(rows)}) — recipes/<slug>.md · standard: directives/recipe-card-standard.md")
    print("\n".join(rows) if rows else "  none — recipe_cards.py new <slug> --name … --family …")
    return 0


def cmd_show(a):
    p = card_path(a.slug)
    if not p.exists():
        print(f"no recipe '{a.slug}' — recipe_cards.py list")
        return 1
    print(p.read_text(encoding="utf-8"))
    return 0


def cmd_match(a):
    rows = match(a.ask, top=a.top)
    v = verdict(rows)
    if a.json:
        print(json.dumps({"rows": rows, "verdict": v}, indent=2))
        return 0
    if not rows:
        print("RECIPE MATCH: none — WEAK MATCH: forge one (recipe-card-forge) and save it to recipes/")
        return 0
    print("RECIPE MATCH (highest first):")
    for r in rows:
        print(f"  {r['slug']:<34} score={r['score']:<3} {r['family']:<17} {r['name']}")
    if v["confident"]:
        print(f"CONFIDENT MATCH — {v['slug']} ({v['reason']})")
    else:
        print(f"WEAK MATCH — {v['reason']}. Do not run {v['slug']}'s lanes on this ask: forge a card "
              f"(recipe-card-forge), save it to recipes/, and show it in the JOB PLAN.")
    return 0


def cmd_parse(a):
    card = parse(a.slug)
    if a.json:
        print(json.dumps(card, indent=2))
    else:
        for l in card["lanes"]:
            dep = f"after {','.join(l['after'])}" if l["after"] else "parallel"
            print(f"  {l['id']:<4} {l['name']:<28} [{dep}]  {l['desc'][:70]}")
    return 0


def cmd_lint(a):
    slugs = [a.slug] if a.slug else all_slugs()
    errs = []
    for s in slugs:
        errs += lint(s)
    if errs:
        print("RECIPE LINT — problems:")
        print("\n".join("  " + e for e in errs))
        return 1
    print(f"RECIPE LINT — {len(slugs)} card(s) clean")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Recipe card library")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list").set_defaults(fn=cmd_list)
    s = sub.add_parser("show"); s.add_argument("slug"); s.set_defaults(fn=cmd_show)
    s = sub.add_parser("match"); s.add_argument("ask"); s.add_argument("--top", type=int, default=3)
    s.add_argument("--json", action="store_true"); s.set_defaults(fn=cmd_match)
    s = sub.add_parser("new"); s.add_argument("slug"); s.add_argument("--name", required=True)
    s.add_argument("--family", required=True, choices=FAMILIES)
    s.add_argument("--force", action="store_true"); s.set_defaults(fn=cmd_new)
    s = sub.add_parser("parse"); s.add_argument("slug"); s.add_argument("--json", action="store_true")
    s.set_defaults(fn=cmd_parse)
    s = sub.add_parser("lint"); s.add_argument("slug", nargs="?"); s.set_defaults(fn=cmd_lint)
    a = ap.parse_args(argv)
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
