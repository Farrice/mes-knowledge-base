#!/usr/bin/env python3
"""
Panel Cast — the hybrid casting layer for the Expert Assembly OS (/assemble).

Extends council_cast.py (imported, never modified) with the one thing the council
caster can't do: KNOW when the roster is thin. Given a task + its required domains,
it computes a per-domain coverage report against the invocation-card roster, seats
real extracted experts where coverage is strong, and emits BESPOKE SLOTS — orders
to synthesize a composite world-class persona — where coverage is thin or absent.

This is the wire between council_cast.py (roster selection) and the McClain
persona-forge logic (persona invention), so /assemble can field a world-class
panel for ANY domain, not just the ~227 extracted experts.

Pure planning logic (no network). Consumed by expert-assembly.workflow.js and the
/assemble manual runbook.

CLI:
    python3 execution/panel_cast.py "<task>" [--domains "a,b,c"] [--mode panel]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, List

sys.path.insert(0, str(Path(__file__).resolve().parent))
from council_cast import (  # noqa: E402
    FARRICE_SEAT,
    _genius_path,
    _keywords,
    _relevance,
    _skill_slugs,
    parse_cards,
)

# panel: the /assemble shape — 3-5 seats total (roster + bespoke), Farrice extra.
PANEL_SHAPE = {
    "panel": {"min_seats": 3, "max_seats": 5, "cap": 2},
}

# Governor bounded slots (expert-composition-governor.md), in assignment order.
# Farrice is always the FUNCTION OWNER on top of these.
GOVERNOR_SLOTS = ["Spine", "Mechanism", "Differentiator", "Craft", "Risk Gate"]

# Coverage thresholds: a card must hit at least this many of a domain's keywords
# AND at least this fraction of them to count as STRONG coverage.
STRONG_MIN_HITS = 2
STRONG_MIN_RATIO = 0.5


def coverage_report(cards: List[Dict], domains: List[str]) -> List[Dict]:
    """Per required domain: best roster card, its score, and strong/thin/absent."""
    report = []
    for d in domains:
        kws = _keywords(d)
        if not kws:
            report.append({"domain": d, "status": "absent", "best_card": None,
                           "best_score": 0, "keyword_count": 0})
            continue
        best, best_score = None, 0
        for c in cards:
            s = _relevance(c, kws)
            if s > best_score:
                best, best_score = c, s
        ratio = best_score / len(kws)
        # Short domains (1 usable keyword) can never hit STRONG_MIN_HITS — scale it.
        if best_score >= min(STRONG_MIN_HITS, len(kws)) and ratio >= STRONG_MIN_RATIO:
            status = "strong"
        elif best_score >= 1:
            status = "thin"
        else:
            status = "absent"
        report.append({
            "domain": d,
            "status": status,
            "best_card": best["name"] if best else None,
            "best_score": best_score,
            "keyword_count": len(kws),
        })
    return report


def build_panel_plan(task: str, domains: List[str], mode: str = "panel") -> Dict:
    """Cast a hybrid panel: roster seats for strong domains, bespoke slots for thin ones."""
    shape = PANEL_SHAPE.get(mode, PANEL_SHAPE["panel"])
    cards = parse_cards()
    slugs = _skill_slugs()
    task_kws = _keywords(task)
    domains = [d.strip() for d in domains if d.strip()] or [task]

    coverage = coverage_report(cards, domains)

    roster: List[Dict] = []
    bespoke_slots: List[Dict] = []
    seated_names: set = set()
    group_count: Dict[str, int] = {}

    # 1) One seat per required domain: roster card if strong, bespoke slot otherwise.
    for cov in coverage:
        if len(roster) + len(bespoke_slots) >= shape["max_seats"]:
            break
        if cov["status"] == "strong":
            card = next((c for c in cards if c["name"] == cov["best_card"]), None)
            if card and card["name"] not in seated_names \
                    and group_count.get(card["domain_group"], 0) < shape["cap"]:
                c = dict(card)
                c["bespoke"] = False
                c["covers_domain"] = cov["domain"]
                roster.append(c)
                seated_names.add(c["name"])
                group_count[c["domain_group"]] = group_count.get(c["domain_group"], 0) + 1
                continue
        why = (f"best roster match '{cov['best_card']}' scored "
               f"{cov['best_score']}/{cov['keyword_count']} domain keywords"
               if cov["best_card"] else "no roster card matched this domain at all")
        bespoke_slots.append({"domain_needed": cov["domain"], "why_thin": why})

    # 2) Fill remaining seats to min_seats with the top TASK-relevant roster cards
    #    (relevance >= 2 so we never recreate the zero-relevance padding problem).
    if len(roster) + len(bespoke_slots) < shape["min_seats"]:
        scored = sorted(cards, key=lambda c: _relevance(c, task_kws), reverse=True)
        for c in scored:
            if len(roster) + len(bespoke_slots) >= shape["min_seats"]:
                break
            if c["name"] in seated_names or _relevance(c, task_kws) < 2:
                continue
            if group_count.get(c["domain_group"], 0) >= shape["cap"]:
                continue
            cc = dict(c)
            cc["bespoke"] = False
            cc["covers_domain"] = "task-core"
            roster.append(cc)
            seated_names.add(cc["name"])
            group_count[cc["domain_group"]] = group_count.get(cc["domain_group"], 0) + 1
        # Still short (truly uncovered territory): order a second bespoke lens.
        while len(roster) + len(bespoke_slots) < shape["min_seats"]:
            bespoke_slots.append({
                "domain_needed": f"complementary lens on: {task}",
                "why_thin": "panel below minimum seats after roster + domain pass",
            })

    # 3) Governor slot pre-assignment (workflow may adjust, but no slot doubles).
    members: List[Dict] = []
    for c in roster:
        members.append({
            "name": c["name"],
            "bespoke": False,
            "domain_group": c["domain_group"],
            "covers_domain": c.get("covers_domain", ""),
            "core_method": c["core_method"],
            "lens": c["best_for"],
            "genius_path": _genius_path(c, slugs),
            "is_user": False,
        })
    for b in bespoke_slots:
        members.append({
            "name": None,  # named at Forge time
            "bespoke": True,
            "domain_needed": b["domain_needed"],
            "why_thin": b["why_thin"],
            "genius_path": None,
            "is_user": False,
        })
    for i, m in enumerate(members):
        m["slot"] = GOVERNOR_SLOTS[i % len(GOVERNOR_SLOTS)]

    owner = dict(FARRICE_SEAT)
    owner["slot"] = "Function Owner"
    owner["bespoke"] = False
    members.append(owner)

    return {
        "task": task,
        "mode": mode,
        "required_domains": domains,
        "coverage": coverage,
        "seats_total": len(members) - 1,  # excl. Farrice
        "roster_seats": len(roster),
        "bespoke_seats": len(bespoke_slots),
        "bespoke_slots": bespoke_slots,
        "panel": members,
    }


def validate_panel_plan(plan: Dict) -> List[str]:
    """Validate that a panel plan is well-formed. Returns [] if valid, else list of errors."""
    errors = []

    # Required top-level fields.
    required_fields = ["task", "mode", "panel", "coverage", "seats_total",
                      "roster_seats", "bespoke_seats"]
    for field in required_fields:
        if field not in plan:
            errors.append(f"Missing required field: {field}")

    # Panel must be non-empty.
    panel = plan.get("panel", [])
    if not panel:
        errors.append("Panel is empty (no members seated)")

    # Governor slots must be assigned (except for very small panels).
    for i, member in enumerate(panel):
        if "slot" not in member:
            errors.append(f"Panel member {i} (name={member.get('name')}) missing 'slot' assignment")

    # Must have at least one Function Owner (Farrice).
    owners = [m for m in panel if m.get("slot") == "Function Owner"]
    if not owners:
        errors.append("No Function Owner (Farrice) seated on panel")
    if len(owners) > 1:
        errors.append(f"Multiple Function Owners seated (expected 1, got {len(owners)})")

    # Bespoke slots must be marked correctly.
    bespoke_slots = plan.get("bespoke_slots", [])
    bespoke_members = [m for m in panel if m.get("bespoke")]
    if len(bespoke_members) != len(bespoke_slots):
        errors.append(f"Mismatch: {len(bespoke_slots)} bespoke_slots but {len(bespoke_members)} bespoke members")

    # Coverage must match required_domains.
    coverage = plan.get("coverage", [])
    required_domains = plan.get("required_domains", [])
    if len(coverage) != len(required_domains):
        errors.append(f"Coverage mismatch: {len(required_domains)} domains, {len(coverage)} coverage reports")

    return errors


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser(prog="panel_cast.py")
    p.add_argument("task")
    p.add_argument("--domains", default="",
                   help="comma-separated required domains (from the Scope phase)")
    p.add_argument("--mode", default="panel", choices=list(PANEL_SHAPE.keys()))
    p.add_argument("--validate", action="store_true",
                   help="Validate plan structure and exit (do not print JSON)")
    a = p.parse_args()

    # Validate task.
    if not a.task or not a.task.strip():
        print("ERROR: Task cannot be empty", file=sys.stderr)
        sys.exit(1)

    # Parse and validate domains.
    doms = [d.strip() for d in a.domains.split(",") if d.strip()]

    # Build the plan.
    plan = build_panel_plan(a.task, doms, a.mode)

    # Validate structure.
    errors = validate_panel_plan(plan)
    if errors:
        print("VALIDATION FAILED:", file=sys.stderr)
        for err in errors:
            print(f"  • {err}", file=sys.stderr)
        sys.exit(1)

    if a.validate:
        print(f"✓ Panel plan is valid (mode={a.mode}, seats={plan['seats_total']}, bespoke={plan['bespoke_seats']})")
        sys.exit(0)

    # Output the plan as JSON.
    print(json.dumps(plan, indent=2))
