#!/usr/bin/env python3
"""Verify the overnight sprint's explicit artifact and quota contract."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def table_rows_between(text: str, start: str, end: str | None) -> int:
    block = text.split(start, 1)[1]
    if end:
        block = block.split(end, 1)[0]
    return sum(1 for line in block.splitlines() if re.match(r"^\|\s*\d+\s*\|", line))


def main() -> int:
    market = (HERE / "market-evidence-ledger.md").read_text()
    language = (HERE / "buyer-language-bank.md").read_text()
    prospects = (HERE / "public-prospect-candidates.md").read_text()
    linkedin = (HERE / "linkedin-launch-kit.md").read_text()
    tournament = (HERE / "offer-tournament.md").read_text()
    landing = (HERE / "landing-page.html").read_text()
    room_path = ROOT / "deliverables/research-briefs/index.html"
    room = room_path.read_text()
    demo = json.loads((HERE / "demo/demo-test-receipt.json").read_text())
    hygiene = json.loads((HERE / "offer-cluster-hygiene-receipt.json").read_text())

    actual = {
        "service_buyer_signals": table_rows_between(market, "## Service-business buyer signals", "## Competing offers"),
        "competitor_offers": table_rows_between(market, "## Competing offers", "## Supplement-brand"),
        "supplement_signals": table_rows_between(market, "## Supplement-brand buyer signals", "## Authoritative"),
        "authoritative_sources": market.split("## Authoritative reports and rules", 1)[1].split("## Decision", 1)[0].count("| ["),
        "buyer_phrases": table_rows_between(language, "# Buyer Language Bank", None),
        "public_candidates": table_rows_between(prospects, "# 30 Public Prospect Candidates", "## Qualification rule"),
        "linkedin_posts": len(re.findall(r"^### Day \d+:", linkedin, re.MULTILINE)),
        "video_scripts": len(re.findall(r"^### Video \d+:", linkedin, re.MULTILINE)),
        "offer_candidates": len(re.findall(r"^\| [^|]+ \| \d", tournament.split("## Verdict", 1)[0], re.MULTILINE)),
        "demo_cases": demo.get("cases"),
        "demo_failed": demo.get("failed"),
    }
    minimums = {
        "service_buyer_signals": 30,
        "competitor_offers": 15,
        "supplement_signals": 10,
        "authoritative_sources": 5,
        "buyer_phrases": 50,
        "public_candidates": 30,
        "linkedin_posts": 10,
        "video_scripts": 3,
        "offer_candidates": 6,
        "demo_cases": 18,
    }
    checks = {name: actual.get(name, 0) >= floor for name, floor in minimums.items()}
    checks.update({
        "demo_zero_failures": actual["demo_failed"] == 0,
        "demo_human_hold": demo.get("all_human_holds_worked") is True,
        "offer_cluster_hygiene": hygiene.get("verdict") == "PASS",
        "landing_price": "$1,500" in landing and "To begin" in landing and "$750" in landing,
        "landing_proof_disclosure": "exact Farrice Cain offer remains unvalidated" in landing,
        "landing_risk_reversal": "owe no final balance" in landing,
        "landing_placeholder": "Booking destination intentionally not connected" in landing,
        "landing_parallax_identity": "parallax-design-system/assets/wordmark.svg" in landing,
        "landing_parallax_palette": all(token in landing for token in ("#1C1C1E", "#7B61FF", "#F5F0EB")),
        "landing_no_retired_palette": not any(token in landing for token in ("#14202b", "#526d82", "#275d4b")),
        "room_index_exists": room_path.is_file(),
    })
    briefs = ["work-recovery-command-board", "market-proof-dossier", "offer-launch-kit", "demo-test-receipt"]
    route_files = []
    for slug in briefs:
        base = ROOT / "deliverables/research-briefs" / slug
        expected = [base / f"{slug}-{suffix}" for suffix in ("brief.html", "brief.md", "context.json")]
        route_files.extend(expected)
        checks[f"brief_{slug}"] = all(path.is_file() for path in expected)
        checks[f"room_card_{slug}"] = (
            f'data-repo-path="deliverables/research-briefs/{slug}/{slug}-brief.html"' in room
        )

    old_temp_root = ".tmp/codex-worktrees/zero-momentum-offer"
    inspected = [room_path, HERE / "landing-page.html", *route_files]
    checks["no_retired_worktree_paths"] = all(
        old_temp_root not in path.read_text(errors="ignore") for path in inspected if path.is_file()
    )

    failed = [name for name, passed in checks.items() if not passed]
    receipt = {"verdict": "PASS" if not failed else "FAIL", "actual": actual, "minimums": minimums, "checks": checks, "failed": failed}
    (HERE / "acceptance-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
