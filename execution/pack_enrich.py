#!/usr/bin/env python3
"""
pack_enrich.py — deterministic half of manual-fire signal-pack enrichment ($0, offline).

Enrichment turns Growth Blueprint artifacts from educated guesses into
data-enriched ones by writing live-market evidence INTO the existing signal
pack — one data spine, no parallel enrichment path. Every consumer
(gb-* artifacts AND the lead-magnet mini-report) inherits from the same block.
The assistant layer does the research (see
skills/growth-blueprint-os/workflows/gb-enrich.md); this script only PLANS the
slots and MERGES the results. It never makes a network call.

Commands:
    plan  --niche <slug> [--pack <path>]
        Read the pack, print the enrichment slots as JSON (per-slot suggested
        lane + estimated cost) plus current Perplexity ledger spend. $0.

    merge --niche <slug> --in <enrichment.json> [--pack <path>]
        Validate the enrichment payload against the schema below, snapshot the
        pack to a dated sibling, merge the additive `enrichment` block into the
        pack (bumping nothing else), print a one-line receipt.
        Fabrication is rejected STRUCTURALLY: every entry must carry >=1
        http(s) source URL and a label (VERIFIED/LIKELY/UNCONFIRMED); entries
        without both are dropped with a visible count. Zero valid entries
        overall -> nothing is written, exit 2.

Enrichment block schema (additive key `enrichment` on the pack; the pack
contract's own fields are never touched — see
execution/specs/outlier-radar-pack.schema.md §Enrichment):

    enrichment: {
      generated_at: ISO-8601 UTC,          # when the research was collected
      lanes_used: ["tavily" | "perplexity" | "research.py" | ...],
      cost_usd_est: float,                 # honest estimate, stated as estimate
      topics: [{                           # demand/freshness per leaderboard topic
        topic: str,
        demand_note: str,                  # reader-grade language (flows into client artifacts)
        trend_direction: "rising" | "flat" | "falling" | "unknown",
        sources: [{url: str, title: str}], # >=1 required
        label: "VERIFIED" | "LIKELY" | "UNCONFIRMED"
      }],
      buyer_language: [{                   # sourced verbatim buyer quotes (plan asks for >=3)
        quote: str, context: str, url: str, label: str
      }],
      market_pulse: [{                     # what changed in the niche last ~30d
        note: str, url: str, label: str
      }]
    }

Cost estimates (stated as estimates, never actuals): Tavily ~= $0.00-0.01 per
search; Perplexity ~= $0.005-0.02 per call (policy: directives/perplexity-usage-policy.md,
ledger: .agent/perplexity-usage.json, $30/mo). Manual-fire only — never scheduled.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKS_DIR = ROOT / ".agent" / "outlier-radar" / "packs"
PPLX_LEDGER = ROOT / ".agent" / "perplexity-usage.json"

PLAN_TOPIC_CAP = 5
LABELS = ("VERIFIED", "LIKELY", "UNCONFIRMED")
TREND_DIRECTIONS = ("rising", "flat", "falling", "unknown")

TAVILY_EST = "$0.00-0.01/search (estimate)"
PPLX_EST = "$0.005-0.02/call (estimate)"


# ------------------------------------------------------------------ pack I/O

def pack_path_for(niche: str, override: str | None) -> Path:
    return Path(override) if override else PACKS_DIR / niche / "latest.json"


def load_pack(path: Path) -> dict:
    if not path.exists():
        raise SystemExit(f"[pack_enrich] FAIL — pack missing: {path}")
    try:
        pack = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        raise SystemExit(f"[pack_enrich] FAIL — pack unreadable: {e.__class__.__name__}: {e}")
    if not isinstance(pack, dict) or "niche_slug" not in pack:
        raise SystemExit(f"[pack_enrich] FAIL — not a signal pack: {path}")
    return pack


def ledger_spend() -> dict:
    """Current Perplexity ledger state, or an honest 'unreadable' marker. Never raises."""
    try:
        data = json.loads(PPLX_LEDGER.read_text(encoding="utf-8"))
        limit = float(data.get("monthly_limit_usd", 0.0))
        spent = float((data.get("usage") or {}).get("estimated_cost_usd", 0.0))
        return {
            "readable": True,
            "month": data.get("current_month"),
            "monthly_limit_usd": limit,
            "spent_usd": round(spent, 2),
            "remaining_usd": round(limit - spent, 2),
        }
    except Exception as e:
        return {"readable": False, "reason": f"{e.__class__.__name__}"}


# ----------------------------------------------------------------------- plan

def build_plan(pack: dict) -> dict:
    slug = pack.get("niche_slug")
    label = pack.get("niche_label") or slug
    topics = [
        t.get("topic")
        for t in ((pack.get("leaderboard") or {}).get("topics") or [])
        if isinstance(t, dict) and t.get("topic")
    ][:PLAN_TOPIC_CAP]

    slots = []
    for topic in topics:
        slots.append({
            "slot_id": f"topic-demand:{topic}",
            "kind": "topic_demand_freshness",
            "topic": topic,
            "ask": (f"Current demand + freshness read on '{topic}' inside the {label} niche: "
                    "is interest rising/flat/falling, and what published evidence says so?"),
            "writes_to": "enrichment.topics[]",
            "requires": ">=1 source URL + label per entry",
            "suggested_lane": "tavily (or execution/research.py --depth quick)",
            "est_cost": TAVILY_EST,
        })
    slots.append({
        "slot_id": "buyer-language",
        "kind": "buyer_language",
        "ask": (f"Verbatim buyer/audience language in the {label} niche — how real people phrase "
                "the pain and the want (forums, comments, reviews). Quotes exactly as written."),
        "writes_to": "enrichment.buyer_language[]",
        "requires": ">=3 sourced quotes; each entry needs quote + context + url + label",
        "suggested_lane": "tavily (or execution/research.py --depth standard)",
        "est_cost": TAVILY_EST,
    })
    slots.append({
        "slot_id": "market-pulse",
        "kind": "market_pulse",
        "ask": (f"What changed in the {label} niche in the last 30 days — platform shifts, "
                "notable launches, algorithm/policy moves, format waves. Dated evidence only."),
        "writes_to": "enrichment.market_pulse[]",
        "requires": ">=1 note; each entry needs note + url + label",
        "suggested_lane": "perplexity (sonar, recency filter) — freshness needs a recency-aware lane",
        "est_cost": PPLX_EST,
    })

    return {
        "niche_slug": slug,
        "niche_label": label,
        "pack_generated_at": pack.get("generated_at"),
        "pack_status": pack.get("status"),
        "existing_enrichment": (pack.get("enrichment") or {}).get("generated_at"),
        "slots": slots,
        "cost_note": ("All figures are ESTIMATES. Tavily ~= $0.00-0.01/search; Perplexity ~= "
                      "$0.005-0.02/call. Ahrefs is UNFUNDED — never route to it. State the total "
                      "estimate BEFORE any paid call (cost-transparency binding)."),
        "perplexity_ledger": ledger_spend(),
        "draft_path": f".agent/outlier-radar/packs/{slug}/enrichment-draft.json",
        "merge_command": f".venv/bin/python3 execution/pack_enrich.py merge --niche {slug} --in .agent/outlier-radar/packs/{slug}/enrichment-draft.json",
    }


# ---------------------------------------------------------------- validation

def _valid_url(url) -> bool:
    return isinstance(url, str) and url.startswith(("http://", "https://"))


def _norm_label(entry: dict):
    label = str(entry.get("label", "")).upper()
    return label if label in LABELS else None


def _clean_sources(raw) -> list:
    out = []
    for s in (raw if isinstance(raw, list) else []):
        if isinstance(s, dict) and _valid_url(s.get("url")):
            out.append({"url": s["url"], "title": str(s.get("title") or "")})
    return out


def normalize_enrichment(payload: dict) -> tuple[dict, int, list]:
    """Return (clean_block, dropped_count, warnings). Structural fabrication
    rejection: entries without >=1 source URL + a valid label are dropped."""
    if not isinstance(payload, dict):
        raise SystemExit("[pack_enrich] FAIL — enrichment payload is not a JSON object")

    dropped = 0
    warnings: list[str] = []

    topics = []
    for t in (payload.get("topics") if isinstance(payload.get("topics"), list) else []):
        if not isinstance(t, dict):
            dropped += 1
            continue
        sources = _clean_sources(t.get("sources"))
        label = _norm_label(t)
        if not t.get("topic") or not sources or label is None:
            dropped += 1
            continue
        direction = t.get("trend_direction")
        if direction not in TREND_DIRECTIONS:
            warnings.append(f"topics['{t.get('topic')}'] trend_direction {direction!r} -> 'unknown'")
            direction = "unknown"
        topics.append({
            "topic": str(t["topic"]),
            "demand_note": str(t.get("demand_note") or ""),
            "trend_direction": direction,
            "sources": sources,
            "label": label,
        })

    buyer_language = []
    for q in (payload.get("buyer_language") if isinstance(payload.get("buyer_language"), list) else []):
        if not isinstance(q, dict):
            dropped += 1
            continue
        label = _norm_label(q)
        if not q.get("quote") or not _valid_url(q.get("url")) or label is None:
            dropped += 1
            continue
        buyer_language.append({
            "quote": str(q["quote"]),
            "context": str(q.get("context") or ""),
            "url": q["url"],
            "label": label,
        })
    if buyer_language and len(buyer_language) < 3:
        warnings.append(f"buyer_language has {len(buyer_language)} sourced quote(s); the slot asks for >=3")

    market_pulse = []
    for m in (payload.get("market_pulse") if isinstance(payload.get("market_pulse"), list) else []):
        if not isinstance(m, dict):
            dropped += 1
            continue
        label = _norm_label(m)
        if not m.get("note") or not _valid_url(m.get("url")) or label is None:
            dropped += 1
            continue
        market_pulse.append({
            "note": str(m["note"]),
            "url": m["url"],
            "label": label,
        })

    generated_at = payload.get("generated_at")
    if not isinstance(generated_at, str) or not generated_at:
        generated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    lanes = [str(x) for x in payload.get("lanes_used", []) if x] if isinstance(payload.get("lanes_used"), list) else []
    try:
        cost = round(float(payload.get("cost_usd_est", 0.0)), 4)
    except (TypeError, ValueError):
        cost = 0.0
        warnings.append("cost_usd_est unparseable -> 0.0")

    block = {
        "generated_at": generated_at,
        "lanes_used": lanes,
        "cost_usd_est": cost,
        "topics": topics,
        "buyer_language": buyer_language,
        "market_pulse": market_pulse,
    }
    return block, dropped, warnings


# ---------------------------------------------------------------------- merge

def snapshot_pack(pack_file: Path) -> Path:
    """Copy the pack to a dated sibling before touching it (RECORD file)."""
    now = datetime.now(timezone.utc)
    dest = pack_file.parent / f"{now:%Y-%m-%d}-pre-enrich-{now:%H%M%S}.json"
    dest.write_bytes(pack_file.read_bytes())
    return dest


def atomic_write(path: Path, text: str) -> None:
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(text)
        os.replace(tmp, path)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise


def cmd_merge(args) -> int:
    pack_file = pack_path_for(args.niche, args.pack)
    pack = load_pack(pack_file)

    src = Path(getattr(args, "in"))
    if not src.exists():
        raise SystemExit(f"[pack_enrich] FAIL — enrichment file missing: {src}")
    try:
        payload = json.loads(src.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        raise SystemExit(f"[pack_enrich] FAIL — enrichment unreadable: {e.__class__.__name__}: {e}")

    block, dropped, warnings = normalize_enrichment(payload)
    kept = len(block["topics"]) + len(block["buyer_language"]) + len(block["market_pulse"])
    for w in warnings:
        print(f"[pack_enrich] WARN — {w}", file=sys.stderr)
    if kept == 0:
        print(f"[pack_enrich] REJECTED — 0 valid entries after validation "
              f"({dropped} dropped: missing source URL and/or label). Nothing written to {pack_file}.",
              file=sys.stderr)
        return 2

    snap = snapshot_pack(pack_file)
    pack["enrichment"] = block  # additive; nothing else on the pack is bumped
    atomic_write(pack_file, json.dumps(pack, indent=2, ensure_ascii=False) + "\n")

    lanes = ",".join(block["lanes_used"]) or "-"
    print(f"[pack_enrich] merged enrichment into {pack_file} — "
          f"topics={len(block['topics'])} buyer_quotes={len(block['buyer_language'])} "
          f"pulse={len(block['market_pulse'])} dropped_sourceless={dropped} "
          f"lanes={lanes} est_cost=${block['cost_usd_est']:.2f} snapshot={snap.name}")
    return 0


def cmd_plan(args) -> int:
    pack = load_pack(pack_path_for(args.niche, args.pack))
    print(json.dumps(build_plan(pack), indent=2, ensure_ascii=False))
    return 0


# ------------------------------------------------------------------------ CLI

def main() -> int:
    ap = argparse.ArgumentParser(
        description="Deterministic side of manual-fire pack enrichment: plan slots, merge validated results. $0, offline.")
    sub = ap.add_subparsers(dest="command", required=True)

    p_plan = sub.add_parser("plan", help="Print enrichment slots for a niche pack as JSON ($0).")
    p_plan.add_argument("--niche", required=True, help="Niche slug (pack at .agent/outlier-radar/packs/<slug>/latest.json)")
    p_plan.add_argument("--pack", default=None, help="Pack path override (fixtures/tests)")
    p_plan.set_defaults(func=cmd_plan)

    p_merge = sub.add_parser("merge", help="Validate an enrichment JSON and merge it into the pack.")
    p_merge.add_argument("--niche", required=True, help="Niche slug")
    p_merge.add_argument("--in", required=True, help="Path to enrichment.json (see schema in module docstring)")
    p_merge.add_argument("--pack", default=None, help="Pack path override (fixtures/tests)")
    p_merge.set_defaults(func=cmd_merge)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
