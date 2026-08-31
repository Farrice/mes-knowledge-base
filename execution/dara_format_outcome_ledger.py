#!/usr/bin/env python3
"""Append-only outcome ledger for Dara Denney creative-format tests.

The ledger separates measured observations from explicit human decisions.
It never promotes a format from hook rate alone and never rewrites history.
All operations use the Python standard library.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import uuid
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LEDGER = ROOT / ".agent" / "dara-format-outcomes.jsonl"
SCHEMA_VERSION = "dara-format-outcome/v1"

FORMAT_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{1,79}$")
DECISIONS = {"observe", "hold", "promote", "demote", "retire"}
FATIGUE_STATES = {"unknown", "fresh", "watch", "fatigued", "recovered"}
CONVERSION_EVIDENCE_STATES = {
    "none",
    "directional",
    "platform-attributed",
    "first-party-confirmed",
    "revenue-confirmed",
}
EVIDENCE_RANK = {
    "none": 0,
    "directional": 1,
    "platform-attributed": 2,
    "first-party-confirmed": 3,
    "revenue-confirmed": 4,
}


class LedgerError(ValueError):
    """Raised when an event would weaken ledger truth."""


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _nonempty(value: str, field: str) -> str:
    clean = " ".join((value or "").split())
    if not clean:
        raise LedgerError(f"{field} is required")
    return clean


def _nonnegative(value: float | int, field: str) -> float:
    number = float(value)
    if number < 0:
        raise LedgerError(f"{field} must be non-negative")
    return number


def _common_event(args: argparse.Namespace, event_type: str) -> dict[str, Any]:
    format_id = _nonempty(args.format_id, "format_id").lower()
    if not FORMAT_ID_RE.fullmatch(format_id):
        raise LedgerError("format_id must be a lowercase slug (2-80 characters)")
    return {
        "schema_version": SCHEMA_VERSION,
        "event_id": str(uuid.uuid4()),
        "timestamp": now_iso(),
        "event_type": event_type,
        "format_id": format_id,
        "format_label": _nonempty(args.format_label, "format_label"),
        "source_prior_tier": args.source_prior_tier or "",
        "campaign_id": args.campaign_id or "",
        "asset_id": args.asset_id or "",
        "message_id": args.message_id or "",
        "category": _nonempty(args.category, "category"),
        "persona": _nonempty(args.persona, "persona"),
        "channel": args.channel or "",
        "funnel_stage": args.funnel_stage or "",
        "notes": args.notes or "",
    }


def build_observation(args: argparse.Namespace) -> dict[str, Any]:
    event = _common_event(args, "observation")
    spend = _nonnegative(args.spend, "spend")
    currency = _nonempty(args.currency, "currency").upper()
    if not re.fullmatch(r"[A-Z]{3}", currency):
        raise LedgerError("currency must be a three-letter code such as USD")

    hook_events = args.hook_events
    hook_opportunities = args.hook_opportunities
    hook_rate = args.hook_rate
    if hook_events is not None:
        hook_events = int(_nonnegative(hook_events, "hook_events"))
    if hook_opportunities is not None:
        hook_opportunities = int(_nonnegative(hook_opportunities, "hook_opportunities"))
        if hook_opportunities == 0:
            raise LedgerError("hook_opportunities must be greater than zero when supplied")
    if hook_events is not None and hook_opportunities is None:
        raise LedgerError("hook_events requires hook_opportunities")
    if hook_rate is not None and hook_opportunities is None:
        raise LedgerError("hook_rate requires hook_opportunities for weighted comparison")
    if hook_events is not None and hook_opportunities is not None:
        computed = hook_events / hook_opportunities
        if hook_rate is not None and abs(float(hook_rate) - computed) > 0.0005:
            raise LedgerError("hook_rate does not match hook_events / hook_opportunities")
        hook_rate = computed
    if hook_rate is not None and not 0 <= float(hook_rate) <= 1:
        raise LedgerError("hook_rate must be a decimal from 0 to 1")
    if hook_rate is not None:
        _nonempty(args.hook_rate_definition, "hook_rate_definition")

    conversion_count = int(_nonnegative(args.conversion_count, "conversion_count"))
    conversion_value = _nonnegative(args.conversion_value, "conversion_value")
    conversion_state = args.conversion_evidence_state
    if conversion_state not in CONVERSION_EVIDENCE_STATES:
        raise LedgerError(f"unsupported conversion evidence state: {conversion_state}")
    if conversion_count > 0 and conversion_state == "none":
        raise LedgerError("conversion_count above zero requires conversion evidence")
    if conversion_state != "none" and not args.evidence:
        raise LedgerError("non-none conversion evidence requires --evidence")

    fatigue_state = args.fatigue_state
    if fatigue_state not in FATIGUE_STATES:
        raise LedgerError(f"unsupported fatigue state: {fatigue_state}")
    frequency = None if args.frequency is None else _nonnegative(args.frequency, "frequency")

    event.update(
        {
            "spend": spend,
            "currency": currency,
            "hook_rate": None if hook_rate is None else round(float(hook_rate), 6),
            "hook_rate_definition": args.hook_rate_definition or "",
            "hook_events": hook_events,
            "hook_opportunities": hook_opportunities,
            "conversion_event": args.conversion_event or "",
            "conversion_count": conversion_count,
            "conversion_value": conversion_value,
            "conversion_evidence_state": conversion_state,
            "attribution_window": args.attribution_window or "",
            "evidence": args.evidence or "",
            "fatigue_state": fatigue_state,
            "fatigue_window": args.fatigue_window or "",
            "frequency": frequency,
        }
    )
    validate_event(event)
    return event


def build_decision(args: argparse.Namespace) -> dict[str, Any]:
    event = _common_event(args, "decision")
    if args.decision not in DECISIONS:
        raise LedgerError(f"unsupported decision: {args.decision}")
    event.update(
        {
            "decision": args.decision,
            "decision_reason": _nonempty(args.decision_reason, "decision_reason"),
            "decision_evidence": _nonempty(args.decision_evidence, "decision_evidence"),
            "decided_by": _nonempty(args.decided_by, "decided_by"),
        }
    )
    validate_event(event)
    return event


def validate_event(event: dict[str, Any]) -> None:
    required = {
        "schema_version",
        "event_id",
        "timestamp",
        "event_type",
        "format_id",
        "format_label",
        "category",
        "persona",
    }
    missing = sorted(key for key in required if key not in event)
    if missing:
        raise LedgerError(f"event missing fields: {', '.join(missing)}")
    if event["schema_version"] != SCHEMA_VERSION:
        raise LedgerError(f"unsupported schema_version: {event['schema_version']}")
    if event["event_type"] not in {"observation", "decision"}:
        raise LedgerError(f"unsupported event_type: {event['event_type']}")
    if not FORMAT_ID_RE.fullmatch(str(event["format_id"])):
        raise LedgerError(f"invalid format_id: {event['format_id']}")
    for field in ("format_label", "category", "persona"):
        if not str(event[field]).strip():
            raise LedgerError(f"event has blank {field}")
    try:
        uuid.UUID(str(event["event_id"]))
    except ValueError as exc:
        raise LedgerError(f"invalid event_id: {event['event_id']}") from exc
    try:
        parsed_timestamp = datetime.fromisoformat(str(event["timestamp"]).replace("Z", "+00:00"))
    except ValueError as exc:
        raise LedgerError(f"invalid timestamp: {event['timestamp']}") from exc
    if parsed_timestamp.tzinfo is None:
        raise LedgerError("timestamp must include a timezone")

    if event["event_type"] == "observation":
        for field in ("spend", "currency", "conversion_count", "conversion_evidence_state", "fatigue_state"):
            if field not in event:
                raise LedgerError(f"observation missing field: {field}")
        if event["conversion_evidence_state"] not in CONVERSION_EVIDENCE_STATES:
            raise LedgerError("observation has invalid conversion evidence state")
        if event["fatigue_state"] not in FATIGUE_STATES:
            raise LedgerError("observation has invalid fatigue state")
        if float(event["spend"]) < 0:
            raise LedgerError("observation spend must be non-negative")
        if not re.fullmatch(r"[A-Z]{3}", str(event["currency"])):
            raise LedgerError("observation currency must be a three-letter code")
        conversion_count = int(event["conversion_count"])
        conversion_value = float(event.get("conversion_value", 0))
        if conversion_count < 0 or conversion_value < 0:
            raise LedgerError("conversion count and value must be non-negative")
        conversion_state = event["conversion_evidence_state"]
        if (conversion_count > 0 or conversion_value > 0) and conversion_state == "none":
            raise LedgerError("conversion results require conversion evidence")
        if conversion_state != "none" and not str(event.get("evidence", "")).strip():
            raise LedgerError("non-none conversion evidence requires a receipt")
        rate = event.get("hook_rate")
        opportunities = event.get("hook_opportunities")
        if rate is not None and (opportunities is None or int(opportunities) <= 0):
            raise LedgerError("hook_rate requires positive hook_opportunities")
        if rate is not None and not 0 <= float(rate) <= 1:
            raise LedgerError("hook_rate must be a decimal from 0 to 1")
        hook_events = event.get("hook_events")
        if hook_events is not None:
            if opportunities is None:
                raise LedgerError("hook_events requires hook_opportunities")
            if int(hook_events) < 0:
                raise LedgerError("hook_events must be non-negative")
            computed_rate = int(hook_events) / int(opportunities)
            if rate is None or abs(float(rate) - computed_rate) > 0.0005:
                raise LedgerError("hook_rate does not match hook event counts")
    else:
        for field in ("decision", "decision_reason", "decision_evidence", "decided_by"):
            if not event.get(field):
                raise LedgerError(f"decision missing field: {field}")
        if event["decision"] not in DECISIONS:
            raise LedgerError("decision event has invalid decision")


def read_events(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    events: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            event = json.loads(line)
            validate_event(event)
        except (json.JSONDecodeError, LedgerError) as exc:
            raise LedgerError(f"invalid ledger row {line_number}: {exc}") from exc
        events.append(event)
    return events


def append_event(path: Path, event: dict[str, Any]) -> None:
    validate_event(event)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = (json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8")
    descriptor = os.open(path, os.O_APPEND | os.O_CREAT | os.O_WRONLY, 0o644)
    try:
        os.write(descriptor, payload)
    finally:
        os.close(descriptor)


def _matches(event: dict[str, Any], args: argparse.Namespace) -> bool:
    for field in ("format_id", "category", "persona", "campaign_id"):
        wanted = getattr(args, f"filter_{field}", "")
        if wanted and event.get(field, "").lower() != wanted.lower():
            return False
    return True


def _group_key(event: dict[str, Any], group_by: str) -> tuple[str, ...]:
    if group_by == "format":
        return (event["format_id"],)
    if group_by == "category":
        return (event["category"],)
    if group_by == "persona":
        return (event["persona"],)
    return (event["format_id"], event["category"], event["persona"])


def summarize(events: Iterable[dict[str, Any]], group_by: str) -> list[dict[str, Any]]:
    groups: dict[tuple[str, ...], dict[str, Any]] = defaultdict(
        lambda: {
            "observations": 0,
            "spend_by_currency": defaultdict(float),
            "hook_events": 0,
            "hook_opportunities": 0,
            "conversion_count": 0,
            "conversion_value": 0.0,
            "conversion_events": defaultdict(int),
            "strongest_conversion_evidence": "none",
            "latest_fatigue_state": "unknown",
            "latest_decision": "",
            "latest_decision_reason": "",
            "latest_timestamp": "",
        }
    )

    for event in sorted(events, key=lambda row: row["timestamp"]):
        key = _group_key(event, group_by)
        row = groups[key]
        row["group"] = " | ".join(key)
        row["latest_timestamp"] = event["timestamp"]
        if event["event_type"] == "observation":
            row["observations"] += 1
            row["spend_by_currency"][event["currency"]] += float(event.get("spend", 0))
            if event.get("hook_events") is not None and event.get("hook_opportunities") is not None:
                row["hook_events"] += int(event["hook_events"])
                row["hook_opportunities"] += int(event["hook_opportunities"])
            row["conversion_count"] += int(event.get("conversion_count", 0))
            row["conversion_value"] += float(event.get("conversion_value", 0))
            conversion_event = event.get("conversion_event") or "unspecified"
            row["conversion_events"][conversion_event] += int(event.get("conversion_count", 0))
            state = event.get("conversion_evidence_state", "none")
            if EVIDENCE_RANK[state] > EVIDENCE_RANK[row["strongest_conversion_evidence"]]:
                row["strongest_conversion_evidence"] = state
            row["latest_fatigue_state"] = event.get("fatigue_state", "unknown")
        else:
            row["latest_decision"] = event["decision"]
            row["latest_decision_reason"] = event["decision_reason"]

    output: list[dict[str, Any]] = []
    for row in groups.values():
        opportunities = row["hook_opportunities"]
        row["weighted_hook_rate"] = (
            round(row["hook_events"] / opportunities, 6) if opportunities else None
        )
        row["spend_by_currency"] = {
            currency: round(amount, 2)
            for currency, amount in sorted(row["spend_by_currency"].items())
        }
        if len(row["spend_by_currency"]) == 1:
            row["currency"], row["spend"] = next(iter(row["spend_by_currency"].items()))
        else:
            row["currency"], row["spend"] = "MIXED", None
        row["conversion_value"] = round(row["conversion_value"], 2)
        row["conversion_events"] = dict(sorted(row["conversion_events"].items()))
        output.append(row)
    return sorted(output, key=lambda row: row["group"])


def render_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "No matching Dara format outcome events."
    lines = [
        "| Group | Obs | Spend | Hook rate | Conversions | Evidence | Fatigue | Decision |",
        "|---|---:|---:|---:|---:|---|---|---|",
    ]
    for row in rows:
        rate = "NO DATA" if row["weighted_hook_rate"] is None else f"{row['weighted_hook_rate'] * 100:.2f}%"
        decision = row["latest_decision"] or "NO DECISION"
        spend = "; ".join(
            f"{currency} {amount:.2f}" for currency, amount in row["spend_by_currency"].items()
        ) or "NO DATA"
        lines.append(
            f"| {row['group']} | {row['observations']} | {spend} | {rate} | "
            f"{row['conversion_count']} | {row['strongest_conversion_evidence']} | "
            f"{row['latest_fatigue_state']} | {decision} |"
        )
    return "\n".join(lines)


def add_common_arguments(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--format-id", required=True)
    parser.add_argument("--format-label", required=True)
    parser.add_argument("--source-prior-tier", choices=["S", "A", "B", "C", "D", "E", "F"], default="")
    parser.add_argument("--campaign-id", default="")
    parser.add_argument("--asset-id", default="")
    parser.add_argument("--message-id", default="")
    parser.add_argument("--category", required=True)
    parser.add_argument("--persona", required=True)
    parser.add_argument("--channel", default="")
    parser.add_argument("--funnel-stage", default="")
    parser.add_argument("--notes", default="")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Record and inspect Dara creative-format outcomes.")
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    sub = parser.add_subparsers(dest="command", required=True)

    record = sub.add_parser("record", help="Append one performance observation.")
    add_common_arguments(record)
    record.add_argument("--spend", type=float, required=True)
    record.add_argument("--currency", default="USD")
    record.add_argument("--hook-rate", type=float)
    record.add_argument("--hook-rate-definition", default="")
    record.add_argument("--hook-events", type=int)
    record.add_argument("--hook-opportunities", type=int)
    record.add_argument("--conversion-event", default="")
    record.add_argument("--conversion-count", type=int, default=0)
    record.add_argument("--conversion-value", type=float, default=0.0)
    record.add_argument(
        "--conversion-evidence-state",
        choices=sorted(CONVERSION_EVIDENCE_STATES),
        default="none",
    )
    record.add_argument("--attribution-window", default="")
    record.add_argument("--evidence", default="")
    record.add_argument("--fatigue-state", choices=sorted(FATIGUE_STATES), default="unknown")
    record.add_argument("--fatigue-window", default="")
    record.add_argument("--frequency", type=float)

    decide = sub.add_parser("decide", help="Append an explicit promotion/demotion decision.")
    add_common_arguments(decide)
    decide.add_argument("--decision", required=True, choices=sorted(DECISIONS))
    decide.add_argument("--decision-reason", required=True)
    decide.add_argument("--decision-evidence", required=True)
    decide.add_argument("--decided-by", required=True)

    scoreboard = sub.add_parser("scoreboard", help="Aggregate observations and show latest explicit decision.")
    scoreboard.add_argument(
        "--group-by",
        choices=["format", "category", "persona", "format-category-persona"],
        default="format",
    )
    scoreboard.add_argument("--format-id", dest="filter_format_id", default="")
    scoreboard.add_argument("--category", dest="filter_category", default="")
    scoreboard.add_argument("--persona", dest="filter_persona", default="")
    scoreboard.add_argument("--campaign-id", dest="filter_campaign_id", default="")
    scoreboard.add_argument("--json", action="store_true")

    sub.add_parser("verify", help="Validate every JSONL row and report counts.")
    sub.add_parser("schema", help="Print the ledger enums and evidence policy.")
    return parser


def schema_summary() -> dict[str, Any]:
    return {
        "schema_version": SCHEMA_VERSION,
        "default_ledger": str(DEFAULT_LEDGER.relative_to(ROOT)),
        "event_types": ["observation", "decision"],
        "decisions": sorted(DECISIONS),
        "fatigue_states": sorted(FATIGUE_STATES),
        "conversion_evidence_states": sorted(CONVERSION_EVIDENCE_STATES, key=EVIDENCE_RANK.get),
        "rules": [
            "hook_rate requires a denominator and a named definition",
            "conversion evidence above none requires a receipt path or URL",
            "promotion and demotion are explicit decision events, never inferred from hook rate",
            "format, message, persona, category, and channel stay separate",
        ],
    }


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    path = args.ledger.expanduser().resolve()
    try:
        if args.command == "record":
            event = build_observation(args)
            append_event(path, event)
            print(json.dumps(event, indent=2, ensure_ascii=False))
        elif args.command == "decide":
            event = build_decision(args)
            append_event(path, event)
            print(json.dumps(event, indent=2, ensure_ascii=False))
        elif args.command == "scoreboard":
            events = [event for event in read_events(path) if _matches(event, args)]
            rows = summarize(events, args.group_by)
            print(json.dumps(rows, indent=2, ensure_ascii=False) if args.json else render_table(rows))
        elif args.command == "verify":
            events = read_events(path)
            observations = sum(event["event_type"] == "observation" for event in events)
            decisions = sum(event["event_type"] == "decision" for event in events)
            print(
                f"DARA FORMAT OUTCOME LEDGER PASS | events={len(events)} "
                f"observations={observations} decisions={decisions}"
            )
        elif args.command == "schema":
            print(json.dumps(schema_summary(), indent=2, ensure_ascii=False))
    except LedgerError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
