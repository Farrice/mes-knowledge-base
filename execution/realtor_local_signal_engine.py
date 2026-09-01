#!/usr/bin/env python3
"""Deterministic selection guard for the Realtor Local-Signal Content System.

This module does not write creative content. It rejects unsafe or incoherent
signal candidates, scores the survivors, and validates the handoff fields that
the Enrico workflow uses to create a Local Content Card.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


SCORE_FIELDS = (
    "local_specificity",
    "audience_relevance",
    "creator_conviction",
    "conversation_potential",
    "production_fit",
)

AGENT_REQUIRED = (
    "name",
    "market",
    "niche",
    "target_person",
    "voice_markers",
    "genuine_interests",
    "production_comfort",
    "max_posts_per_week",
    "offer",
    "compliance_boundaries",
)

CARD_REQUIRED = (
    "title",
    "target_person",
    "recognizable_tension",
    "source",
    "evidence_status",
    "original_pov",
    "hook",
    "beat_map",
    "visual_plan",
    "cta",
    "human_response_path",
    "real_estate_memory",
    "attention_metrics",
    "pipeline_metrics",
    "voice_approved",
    "cadence",
)

FAIR_HOUSING_PATTERNS = (
    r"\bperfect for families\b",
    r"\bfamily[- ]friendly\b",
    r"\bsafe neighborhood\b",
    r"\bgreat schools?\b",
    r"\bideal for (?:families|couples|young professionals|retirees)\b",
    r"\byoung professionals\b",
    r"\bquiet neighborhood\b",
    r"\bcrime[- ]free\b",
)


def compact_text(value: Any) -> str:
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (list, tuple)):
        return " ".join(str(item) for item in value)
    if isinstance(value, dict):
        return " ".join(f"{key} {item}" for key, item in value.items())
    return str(value or "").strip()


def validate_agent(agent: dict[str, Any]) -> list[str]:
    missing = [field for field in AGENT_REQUIRED if not agent.get(field)]
    errors = [f"missing_agent_field:{field}" for field in missing]
    max_posts = agent.get("max_posts_per_week")
    if max_posts is not None and (not isinstance(max_posts, int) or max_posts < 1):
        errors.append("invalid_agent_field:max_posts_per_week")
    return errors


def fair_housing_hits(text: str) -> list[str]:
    lowered = text.lower()
    return [pattern for pattern in FAIR_HOUSING_PATTERNS if re.search(pattern, lowered)]


def score_inputs(signal: dict[str, Any]) -> tuple[dict[str, int], list[str]]:
    raw = signal.get("score_inputs") or {}
    scores: dict[str, int] = {}
    errors: list[str] = []
    for field in SCORE_FIELDS:
        value = raw.get(field)
        if not isinstance(value, int) or value not in (0, 1, 2):
            errors.append(f"invalid_score:{field}")
            continue
        scores[field] = value
    return scores, errors


def evaluate_signal(agent: dict[str, Any], signal: dict[str, Any]) -> dict[str, Any]:
    """Return a stable acceptance, score, and rejection receipt for one signal."""

    reasons = validate_agent(agent)
    scores, score_errors = score_inputs(signal)
    reasons.extend(score_errors)

    target_person = compact_text(signal.get("target_person"))
    source = compact_text(signal.get("source"))
    evidence_status = compact_text(signal.get("evidence_status")).upper()
    transfer_scope = compact_text(signal.get("transfer_scope")).lower()
    original_pov = compact_text(signal.get("original_pov"))
    signal_market = compact_text(signal.get("market"))
    agent_market = compact_text(agent.get("market"))
    source_type = compact_text(signal.get("source_type")).lower()
    all_text = " ".join(
        (
            compact_text(signal.get("title")),
            compact_text(signal.get("claim")),
            original_pov,
            compact_text(signal.get("draft_language")),
        )
    )

    if not target_person:
        reasons.append("missing_target_person")
    if source_type in {"local_source", "performance_reference"} and (
        not source or evidence_status not in {"VERIFIED", "SYNTHETIC"}
    ):
        reasons.append("unsourced_factual_claim")
    if fair_housing_hits(all_text) or signal.get("fair_housing_risk"):
        reasons.append("fair_housing_steering")
    if transfer_scope == "verbatim" or signal.get("copied_language"):
        reasons.append("verbatim_imitation")
    if not original_pov or signal.get("voice_match") is False:
        reasons.append("generic_or_unapproved_voice")
    if signal.get("supported_by_agent_fit") is False or scores.get("creator_conviction") == 0:
        reasons.append("artificial_opinion")

    if signal_market and agent_market and signal_market.casefold() != agent_market.casefold():
        localized_market = compact_text(signal.get("localized_market"))
        if transfer_scope != "format_only" or localized_market.casefold() != agent_market.casefold():
            reasons.append("wrong_market_or_audience")

    # Reach can annotate a qualified candidate; it cannot reverse a rejection.
    total = sum(scores.values()) if len(scores) == len(SCORE_FIELDS) else 0
    unique_reasons = list(dict.fromkeys(reasons))
    return {
        "id": compact_text(signal.get("id")) or "unnamed-signal",
        "accepted": not unique_reasons,
        "score": total if not unique_reasons else None,
        "scores": scores,
        "rejection_reasons": unique_reasons,
        "tie_break": {
            "creator_conviction": scores.get("creator_conviction", 0),
            "production_fit": scores.get("production_fit", 0),
        },
        "reach_evidence": signal.get("reach_evidence") or "NO EVENT",
    }


def rank_signals(agent: dict[str, Any], signals: list[dict[str, Any]]) -> dict[str, Any]:
    evaluated = [evaluate_signal(agent, signal) for signal in signals]
    accepted = sorted(
        (row for row in evaluated if row["accepted"]),
        key=lambda row: (
            row["score"],
            row["tie_break"]["creator_conviction"],
            row["tie_break"]["production_fit"],
            row["id"],
        ),
        reverse=True,
    )
    rejected = [row for row in evaluated if not row["accepted"]]
    return {"accepted": accepted, "rejected": rejected}


def validate_content_card(agent: dict[str, Any], card: dict[str, Any]) -> list[str]:
    errors = [f"missing_card_field:{field}" for field in CARD_REQUIRED if not card.get(field)]
    combined = " ".join(compact_text(card.get(field)) for field in CARD_REQUIRED)
    if fair_housing_hits(combined):
        errors.append("fair_housing_steering")
    if compact_text(card.get("evidence_status")).upper() not in {
        "VERIFIED",
        "SYNTHETIC",
        "LIKELY",
        "UNCONFIRMED",
    }:
        errors.append("invalid_evidence_status")
    if not compact_text(card.get("human_response_path")):
        errors.append("cta_without_human_response_path")
    if not compact_text(card.get("real_estate_memory")):
        errors.append("lifestyle_without_real_estate_memory")
    if card.get("voice_approved") is not True:
        errors.append("voice_not_approved")

    cadence = compact_text(card.get("cadence")).lower()
    if cadence == "daily" and int(agent.get("max_posts_per_week") or 0) < 7:
        errors.append("forced_daily_cadence")

    attention = set(card.get("attention_metrics") or [])
    pipeline = set(card.get("pipeline_metrics") or [])
    if not attention or not pipeline:
        errors.append("missing_metric_ledger")
    if attention & pipeline:
        errors.append("attention_pipeline_metric_overlap")
    return list(dict.fromkeys(errors))


def load_payload(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("payload must be a JSON object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("payload", type=Path, help="JSON object containing agent and signals")
    args = parser.parse_args()
    payload = load_payload(args.payload)
    agent = payload.get("agent") or {}
    signals = payload.get("signals") or []
    result = rank_signals(agent, signals)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if not validate_agent(agent) else 1


if __name__ == "__main__":
    raise SystemExit(main())
