#!/usr/bin/env python3
"""Deterministic readiness gate for the JW Three-Asset Close workflow."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


CORE_FIELDS = (
    "buyer",
    "painful_job",
    "failed_game",
    "new_belief",
    "vehicle",
    "offer",
    "proof",
    "fit",
    "required_inputs",
    "claim_constraints",
    "capacity",
    "payment",
    "awareness",
)


def present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict)):
        return bool(value)
    return True


def evaluate(packet: dict[str, Any]) -> dict[str, Any]:
    missing = [field for field in CORE_FIELDS if not present(packet.get(field))]
    rejections: list[str] = []
    discovery: list[str] = []
    holds: list[str] = []

    if packet.get("purchase_type") != "considered":
        rejections.append("purchase_type must be considered")
    if packet.get("requires_pre_sale_call") is True:
        rejections.append("buying process requires a pre-sale call")
    if packet.get("guaranteed_outcome") is True:
        rejections.append("offer requires a guaranteed outcome")
    if packet.get("unsafe_or_unsupported_claim") is True:
        rejections.append("unsafe or unsupported claim is required")
    if packet.get("false_scarcity") is True:
        rejections.append("false scarcity is required")

    offer = packet.get("offer") if isinstance(packet.get("offer"), dict) else {}
    for field in ("price", "terms", "timing", "deliverables"):
        if not present(offer.get(field)):
            holds.append(f"offer.{field}")

    proof = packet.get("proof") if isinstance(packet.get("proof"), dict) else {}
    for field in ("real", "gaps", "prohibited"):
        if not present(proof.get(field)):
            holds.append(f"proof.{field}")

    acquisition = packet.get("acquisition") if isinstance(packet.get("acquisition"), dict) else {}
    if not present(acquisition.get("source")):
        discovery.append("qualified attention source")

    if packet.get("requires_current_control") is True and not present(packet.get("current_control")):
        discovery.append("current control")
    if packet.get("requires_account_evidence") is True and not present(packet.get("account_evidence")):
        discovery.append("account evidence or accepted UNVERIFIED baseline")

    payment = packet.get("payment") if isinstance(packet.get("payment"), dict) else {}
    if payment.get("route_state") != "VERIFIED":
        holds.append("verified payment route")

    if rejections:
        asset_build = "REJECT"
    elif missing or holds:
        asset_build = "HOLD"
    elif discovery:
        asset_build = "DISCOVER_FIRST"
    else:
        asset_build = "BUILD"

    # A complete system may be built locally even while commercial activation or
    # client delivery remains gated. Preserve the three layers explicitly.
    local_build = "REJECT" if rejections else ("HOLD" if missing else "BUILD")
    commercial_activation = "REJECT" if rejections else ("HOLD" if "verified payment route" in holds else "BUILD")
    client_delivery = "REJECT" if rejections else ("DISCOVER_FIRST" if discovery else ("HOLD" if holds else "BUILD"))

    return {
        "schema_version": "jw-three-asset-readiness/v1",
        "verdict": asset_build,
        "layers": {
            "local_asset_build": local_build,
            "commercial_activation": commercial_activation,
            "client_delivery": client_delivery,
        },
        "missing_core_fields": missing,
        "discovery_needed": sorted(set(discovery)),
        "holds": sorted(set(holds)),
        "rejections": sorted(set(rejections)),
        "no_pre_sale_call": True,
    }


def self_test() -> int:
    complete = {
        field: "present" for field in CORE_FIELDS
    }
    complete.update(
        {
            "purchase_type": "considered",
            "offer": {"price": 500, "terms": "prepaid", "timing": "72 hours", "deliverables": ["model"]},
            "proof": {"real": ["receipt"], "gaps": ["market proof"], "prohibited": ["guarantee"]},
            "payment": {"route_state": "VERIFIED"},
            "acquisition": {"source": "qualified referral"},
            "requires_pre_sale_call": False,
        }
    )
    cases = [
        ("complete", complete, "BUILD"),
        ("impulse", {**complete, "purchase_type": "impulse"}, "REJECT"),
        ("call-required", {**complete, "requires_pre_sale_call": True}, "REJECT"),
        ("no-traffic", {**complete, "acquisition": {}}, "DISCOVER_FIRST"),
        ("no-control", {**complete, "requires_current_control": True}, "DISCOVER_FIRST"),
        ("no-proof", {**complete, "proof": {}}, "HOLD"),
        ("unsafe-claim", {**complete, "unsafe_or_unsupported_claim": True}, "REJECT"),
    ]
    failures: list[str] = []
    for name, packet, expected in cases:
        actual = evaluate(packet)["verdict"]
        if actual != expected:
            failures.append(f"{name}: expected {expected}, got {actual}")
    if failures:
        print("FAIL: " + "; ".join(failures), file=sys.stderr)
        return 1
    print(f"PASS: {len(cases)} readiness and negative-control cases")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", nargs="?", type=Path, help="Offer Truth Packet JSON")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    if args.packet is None:
        parser.error("packet is required unless --self-test is used")
    try:
        packet = json.loads(args.packet.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"error": str(exc)}, indent=2))
        return 2
    print(json.dumps(evaluate(packet), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
