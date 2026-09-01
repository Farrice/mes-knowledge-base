#!/usr/bin/env python3
"""Advisory Signal Fidelity checks for explicitly supplied local packets.

This prototype is deliberately non-blocking. It performs deterministic marker
checks and proof-state comparisons, writes no state, and never claims semantic
equivalence. Human review remains authoritative.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


MODE = "SHADOW"
CORE_FIELDS = (
    "recipient",
    "intended_change",
    "source_of_conviction",
    "promise",
    "limit",
    "proof_state",
    "human_owner",
    "source_path",
)
VALID_SURFACES = {"artifact", "playback"}
VALID_MATCH_POLICIES = {"literal", "manual"}


class PacketError(ValueError):
    """The packet cannot be evaluated without inventing structure."""


def normalized(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold()).strip()


def nonempty(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return bool(value)
    return value is not None


def marker_present(text: str, markers: list[str]) -> bool:
    haystack = normalized(text)
    return any(normalized(marker) in haystack for marker in markers if marker.strip())


def validate_packet(packet: Any) -> dict[str, Any]:
    if not isinstance(packet, dict):
        raise PacketError("packet root must be a JSON object")
    contract = packet.get("signal_contract")
    if not isinstance(contract, dict):
        raise PacketError("signal_contract must be a JSON object")
    for text_field in ("artifact_text", "playback_text"):
        value = packet.get(text_field, "")
        if not isinstance(value, str):
            raise PacketError(f"{text_field} must be a string")
    must_survive = contract.get("must_survive", [])
    if not isinstance(must_survive, list):
        raise PacketError("signal_contract.must_survive must be a list")
    approved = packet.get("owner_approved_changes", [])
    if not isinstance(approved, list) or any(not isinstance(item, str) for item in approved):
        raise PacketError("owner_approved_changes must be a list of ids or field names")
    selected = packet.get("selected_for_review", True)
    if not isinstance(selected, bool):
        raise PacketError("selected_for_review must be a boolean when supplied")
    return packet


def issue(distortion_class: str, code: str, field: str, evidence: str) -> dict[str, str]:
    return {
        "class": distortion_class,
        "code": code,
        "field": field,
        "evidence": evidence,
        "certainty": "hypothesis",
    }


def unique_records(records: list[dict[str, str]]) -> list[dict[str, str]]:
    """Preserve order while removing duplicate advisory rows."""
    seen: set[tuple[tuple[str, str], ...]] = set()
    unique: list[dict[str, str]] = []
    for record in records:
        key = tuple(sorted(record.items()))
        if key in seen:
            continue
        seen.add(key)
        unique.append(record)
    return unique


def coalesce_approved_changes(records: list[dict[str, str]]) -> list[dict[str, str]]:
    by_field: dict[str, list[str]] = {}
    order: list[str] = []
    for record in records:
        field = record["field"]
        if field not in by_field:
            by_field[field] = []
            order.append(field)
        reason = record["reason"]
        if reason not in by_field[field]:
            by_field[field].append(reason)
    return [
        {"field": field, "reason": "; ".join(by_field[field])}
        for field in order
    ]


def evaluate(packet: dict[str, Any]) -> dict[str, Any]:
    packet = validate_packet(packet)
    contract = packet["signal_contract"]
    if packet.get("selected_for_review", True) is False:
        return {
            "mode": MODE,
            "decision": "NOT_RUN",
            "enforcement": False,
            "can_block": False,
            "human_owner": contract.get("human_owner", ""),
            "distortion_hypotheses": [],
            "preserved": [],
            "approved_changes": [],
            "manual_checks": [],
            "uncertainty": [
                "Packet was explicitly marked outside the selected SHADOW review; no fidelity judgment was attempted."
            ],
            "human_review": [],
        }
    artifact_text = packet.get("artifact_text", "")
    playback_text = packet.get("playback_text", "")
    approved = set(packet.get("owner_approved_changes", []))

    issues: list[dict[str, str]] = []
    preserved: list[dict[str, str]] = []
    approved_changes: list[dict[str, str]] = []
    manual_checks: list[dict[str, str]] = []
    uncertainties = [
        "Marker coverage is not semantic equivalence.",
        "Playback accuracy does not prove truth, taste, trust, adoption, or commercial value.",
    ]

    for field in CORE_FIELDS:
        if nonempty(contract.get(field)):
            continue
        if field in approved:
            approved_changes.append({"field": field, "reason": "owner-approved field change or omission"})
        else:
            issues.append(
                issue(
                    "source_distortion",
                    "signal_field_missing",
                    field,
                    f"Signal Contract does not make {field} inspectable.",
                )
            )

    must_survive = contract.get("must_survive", [])
    if not must_survive:
        issues.append(
            issue(
                "source_distortion",
                "must_survive_missing",
                "must_survive",
                "No unaverageable or boundary detail was named for downstream checking.",
            )
        )

    for index, item in enumerate(must_survive):
        if not isinstance(item, dict):
            issues.append(
                issue(
                    "source_distortion",
                    "must_survive_item_invalid",
                    f"must_survive[{index}]",
                    "Item is not an object and cannot be checked.",
                )
            )
            continue
        item_id = str(item.get("id") or f"item-{index + 1}")
        markers = item.get("markers", [])
        required_in = item.get("required_in", ["artifact", "playback"])
        kind = str(item.get("kind") or "detail")
        match_policy = str(item.get("match_policy") or "literal")
        if not isinstance(markers, list) or not markers or any(not isinstance(marker, str) for marker in markers):
            issues.append(
                issue(
                    "source_distortion",
                    "markers_missing",
                    item_id,
                    "Must-survive item has no usable observable markers.",
                )
            )
            continue
        if not isinstance(required_in, list) or any(surface not in VALID_SURFACES for surface in required_in):
            issues.append(
                issue(
                    "source_distortion",
                    "required_surface_invalid",
                    item_id,
                    "required_in must contain only artifact or playback.",
                )
            )
            continue
        if match_policy not in VALID_MATCH_POLICIES:
            issues.append(
                issue(
                    "source_distortion",
                    "match_policy_invalid",
                    item_id,
                    "match_policy must be literal or manual.",
                )
            )
            continue
        if match_policy == "manual":
            manual_checks.append(
                {
                    "field": item_id,
                    "reason": "Meaning may be expressed through metaphor, ambiguity, voice, or deliberate reframing; exact marker absence was not scored as distortion.",
                }
            )
            continue

        for surface in required_in:
            text = artifact_text if surface == "artifact" else playback_text
            if marker_present(text, markers):
                preserved.append({"field": item_id, "surface": surface})
                continue
            approval_key = item_id
            if approval_key in approved:
                approved_changes.append(
                    {
                        "field": item_id,
                        "reason": "owner-approved change; declared marker may be absent from transformed surfaces",
                    }
                )
                continue
            if surface == "playback" and not playback_text.strip():
                continue
            if surface == "playback":
                distortion_class = "playback_gap"
                code = "recipient_did_not_recover_marker"
            elif kind == "limit":
                distortion_class = "machine_distortion"
                code = "limit_missing_from_artifact"
            else:
                distortion_class = "handoff_distortion"
                code = "must_survive_missing_from_artifact"
            issues.append(
                issue(
                    distortion_class,
                    code,
                    item_id,
                    f"None of the declared markers appeared in {surface}.",
                )
            )

    expected_proof = str(contract.get("proof_state") or "").strip().upper()
    artifact_proof = str(packet.get("artifact_proof_state") or expected_proof).strip().upper()
    if expected_proof and artifact_proof != expected_proof:
        if "proof_state" in approved:
            approved_changes.append(
                {
                    "field": "proof_state",
                    "reason": f"owner-approved change from {expected_proof} to {artifact_proof}",
                }
            )
        else:
            issues.append(
                issue(
                    "machine_distortion",
                    "proof_state_changed",
                    "proof_state",
                    f"Artifact proof state is {artifact_proof}; contract proof state is {expected_proof}.",
                )
            )

    if not playback_text.strip():
        uncertainties.append("No cold-recipient playback was supplied; recipient comprehension remains untested.")

    issues = unique_records(issues)
    preserved = unique_records(preserved)
    approved_changes = coalesce_approved_changes(approved_changes)

    if issues or approved_changes or manual_checks:
        decision = "REVIEW"
    elif not playback_text.strip():
        decision = "INSUFFICIENT_EVIDENCE"
    else:
        decision = "CLEAR"

    review_questions: list[str] = []
    if issues:
        review_questions.append("Which reported gaps are materially different from what the human owner intended?")
    if approved_changes:
        review_questions.append("Do the recorded adaptations preserve a newly approved promise, limit, and proof state?")
    if manual_checks:
        review_questions.append("Does the human owner recognize the intended meaning in the manually reviewed creative language?")
    if not playback_text.strip():
        review_questions.append("What does an unfamiliar recipient say this is for, why it matters, and where its limit is?")

    return {
        "mode": MODE,
        "decision": decision,
        "enforcement": False,
        "can_block": False,
        "human_owner": contract.get("human_owner", ""),
        "distortion_hypotheses": issues,
        "preserved": preserved,
        "approved_changes": approved_changes,
        "manual_checks": manual_checks,
        "uncertainty": uncertainties,
        "human_review": review_questions,
    }


def render_plain(report: dict[str, Any]) -> str:
    lines = [
        "Signal Fidelity SHADOW",
        f"Decision: {report['decision']} (advisory; cannot block)",
        f"Human owner: {report.get('human_owner') or 'not supplied'}",
    ]
    issues = report.get("distortion_hypotheses", [])
    if issues:
        lines.append("Possible distortion:")
        for item in issues:
            lines.append(f"- {item['class']} / {item['field']}: {item['evidence']}")
    else:
        lines.append("Possible distortion: none detected by declared markers")
    if report.get("approved_changes"):
        lines.append("Owner-approved adaptations:")
        for item in report["approved_changes"]:
            lines.append(f"- {item['field']}: {item['reason']}")
    if report.get("manual_checks"):
        lines.append("Manual meaning checks:")
        for item in report["manual_checks"]:
            lines.append(f"- {item['field']}: {item['reason']}")
    lines.append("Uncertainty:")
    lines.extend(f"- {item}" for item in report.get("uncertainty", []))
    if report.get("human_review"):
        lines.append("Human review:")
        lines.extend(f"- {item}" for item in report["human_review"])
    return "\n".join(lines)


def load_packet(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PacketError(f"packet not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise PacketError(f"packet is not valid JSON: {exc}") from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("packet", type=Path, help="Local Signal Fidelity packet JSON")
    parser.add_argument("--format", choices=("plain", "json"), default="plain")
    args = parser.parse_args()
    try:
        report = evaluate(load_packet(args.packet))
    except PacketError as exc:
        print(f"Signal Fidelity packet error: {exc}", file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_plain(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
