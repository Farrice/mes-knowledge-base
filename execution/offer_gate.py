#!/usr/bin/env python3
"""Offer-truth gate — $0 deterministic anti-echo-chamber check for offer-shaped work.

Born 2026-07-21 from the Alignment Audit red team (docs/solutions/
2026-07-21-alignment-audit-red-team-verdict.md). Farrice's mandate: "not an echo
chamber... catches these issues and actually has my best interests at heart."

ADVISORY, never blocking (compass-not-cage, Farrice 2026-07-05). Exit 0 always.
Three checks from the re-solve guard:
  1. Concrete outcome — process-benefits (clarity, alignment, awareness...) are
     not purchased outcomes; buyers pay for assets, clients, revenue, rankings.
  2. Demand receipt — at least one named external evidence source that someone
     PAYS for this shape (a URL, a named competitor's pricing, a job-post count).
  3. Units sold — has one unit of THIS offer actually transacted?

Usage:
  python3 execution/offer_gate.py check --offer "Alignment Audit" \
      --outcome "clarity on their positioning" \
      --demand-receipt "" --units-sold 0
  python3 execution/offer_gate.py history   # recent gate fires

Stdlib only. Fires logged to .agent/offer-gate-log.jsonl.
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(ROOT, ".agent", "offer-gate-log.jsonl")
SOLUTION_CARD = "docs/solutions/2026-07-21-alignment-audit-red-team-verdict.md"

# Words that describe process-benefits, not purchasable outcomes.
PROCESS_BENEFIT_WORDS = {
    "clarity", "alignment", "understanding", "awareness", "insight",
    "confidence", "mindset", "empowerment", "transformation", "journey",
    "potential", "unlock", "elevate", "optimize yourself", "self-knowledge",
}

CONCRETE_HINTS = {
    "client", "clients", "revenue", "sales", "leads", "booked", "ranking",
    "rankings", "cited", "citations", "rewritten", "rewrite", "posts",
    "assets", "asset", "profile", "page", "campaign", "pipeline", "deal",
    "deals", "interviews", "placements", "traffic", "conversions", "delivered",
    "document", "system installed", "retainer",
}


def _check(offer: str, outcome: str, demand_receipt: str, units_sold: int) -> dict:
    flags = []
    outcome_l = outcome.lower()

    hit_process = sorted(w for w in PROCESS_BENEFIT_WORDS if w in outcome_l)
    hit_concrete = sorted(w for w in CONCRETE_HINTS if w in outcome_l)
    if hit_process and not hit_concrete:
        flags.append(
            f"outcome reads as a process-benefit ({', '.join(hit_process)}) with no "
            f"concrete deliverable named — buyers pay for the fix, not the finding"
        )
    elif not outcome.strip():
        flags.append("no outcome stated — an offer whose outcome can't be stated in one sentence dies in a cold DM")

    if not demand_receipt.strip():
        flags.append(
            "no demand receipt — zero named evidence anyone PAYS for this shape; "
            "run the evidence sweep before building anything on it"
        )

    if units_sold <= 0:
        flags.append(
            "zero units sold — treat every downstream artifact (dossiers, prospect "
            "lists, funnels) as speculative until one unit transacts or /offer-redteam passes"
        )

    return {
        "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "offer": offer,
        "outcome": outcome,
        "demand_receipt": demand_receipt,
        "units_sold": units_sold,
        "verdict": "PASS" if not flags else "FLAG",
        "flags": flags,
    }


def cmd_check(args: argparse.Namespace) -> int:
    result = _check(args.offer, args.outcome, args.demand_receipt, args.units_sold)
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(result) + "\n")

    if result["verdict"] == "PASS":
        print(f"OFFER GATE PASS — '{args.offer}': outcome concrete, demand evidenced, ≥1 unit sold.")
    else:
        print(f"OFFER GATE FLAG — '{args.offer}' ({len(result['flags'])} issue(s), advisory only):")
        for f in result["flags"]:
            print(f"  ⚑ {f}")
        print(f"  → heavy loop: /offer-redteam · precedent: {SOLUTION_CARD}")
    return 0  # advisory, never blocks


def cmd_history(args: argparse.Namespace) -> int:
    if not os.path.exists(LOG_PATH):
        print("no gate fires logged yet")
        return 0
    with open(LOG_PATH, encoding="utf-8") as fh:
        lines = fh.readlines()[-args.limit:]
    for line in lines:
        try:
            r = json.loads(line)
            print(f"[{r['ts']}] {r['verdict']:4s} {r['offer']} — {len(r.get('flags', []))} flag(s)")
        except json.JSONDecodeError:
            continue
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("check", help="run the three-question gate on an offer")
    c.add_argument("--offer", required=True)
    c.add_argument("--outcome", default="", help="what the buyer walks away WITH, one sentence")
    c.add_argument("--demand-receipt", default="", help="named external evidence someone pays for this shape")
    c.add_argument("--units-sold", type=int, default=0)
    c.set_defaults(func=cmd_check)

    h = sub.add_parser("history", help="recent gate fires")
    h.add_argument("--limit", type=int, default=10)
    h.set_defaults(func=cmd_history)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
