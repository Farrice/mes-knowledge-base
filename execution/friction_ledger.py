#!/usr/bin/env python3
"""Friction ledger for intent-to-outcome harness runs."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / ".agent" / "friction-ledger.jsonl"

ALLOWED_KINDS = {
    "extra-pass",
    "failed-route",
    "weak-output",
    "missing-prompt",
    "unclear-approval",
    "stale-recommendation",
    "verifier-failure",
    "blocked-risk",
    "needs-judgment",
    "misroute",
    "user-struggle",
    "retrieval-failure",
    "stuck-verifier",
    # 2026-07-15: real friction/v2 entries (Apify actor deaths, pointer
    # drift) were written with this kind on 2026-07-07 — the reader enum
    # lagged its own writers and crashed every consumer of the ledger.
    "tooling-fault",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def read_events() -> list[dict[str, Any]]:
    if not LEDGER.exists():
        return []
    events: list[dict[str, Any]] = []
    for lineno, line in enumerate(LEDGER.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid friction ledger JSON on line {lineno}") from exc
    return events


def stable_event_id(*parts: str) -> str:
    normalized = "|".join(" ".join(part.lower().split()) for part in parts if part)
    return hashlib.sha1(normalized.encode("utf-8")).hexdigest()[:16]


def event_exists(event_id: str) -> bool:
    return any(event.get("event_id") == event_id for event in read_events())


def append_event(event: dict[str, Any]) -> dict[str, Any]:
    kind = event.get("kind", "")
    if kind not in ALLOWED_KINDS:
        raise ValueError(f"Unsupported friction kind: {kind}")
    base = {
        "timestamp": now_iso(),
        "kind": kind,
        "severity": event.get("severity", "P2"),
        "route": event.get("route", ""),
        "summary": event.get("summary", ""),
        "evidence": event.get("evidence", ""),
        "next_action": event.get("next_action", ""),
    }
    v2_keys = ("event_id", "trigger", "failure_class", "user_signal", "source_session", "owner", "status")
    if any(key in event for key in v2_keys):
        event_id = event.get("event_id") or stable_event_id(kind, event.get("route", ""), event.get("summary", ""))
        base.update(
            {
                "schema_version": "friction/v2",
                "event_id": event_id,
                "trigger": event.get("trigger", kind),
                "failure_class": event.get("failure_class", kind),
                "user_signal": event.get("user_signal", event.get("summary", "")),
                "source_session": event.get("source_session", "operator-cockpit"),
                "owner": event.get("owner", ""),
                "status": event.get("status", "captured"),
            }
        )
    event = base
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, ensure_ascii=False) + "\n")
    return event


def summarize(events: list[dict[str, Any]]) -> dict[str, Any]:
    by_kind: dict[str, int] = {}
    by_route: dict[str, int] = {}
    for event in events:
        by_kind[event.get("kind", "")] = by_kind.get(event.get("kind", ""), 0) + 1
        route = event.get("route") or "unrouted"
        by_route[route] = by_route.get(route, 0) + 1
    return {
        "ledger": str(LEDGER.relative_to(ROOT)),
        "events": len(events),
        "by_kind": by_kind,
        "by_route": by_route,
    }


def verify() -> None:
    events = read_events()
    for index, event in enumerate(events, 1):
        missing = [key for key in ("timestamp", "kind", "summary", "next_action") if key not in event]
        if missing:
            raise ValueError(f"Friction event {index} missing: {', '.join(missing)}")
        if event["kind"] not in ALLOWED_KINDS:
            raise ValueError(f"Friction event {index} has unsupported kind: {event['kind']}")
        if event.get("schema_version") == "friction/v2":
            v2_missing = [
                key
                for key in ("event_id", "trigger", "failure_class", "user_signal", "source_session", "owner", "status")
                if key not in event
            ]
            if v2_missing:
                raise ValueError(f"Friction event {index} missing v2 fields: {', '.join(v2_missing)}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Track harness friction for self-evolution.")
    sub = parser.add_subparsers(dest="command")

    log = sub.add_parser("log", help="Append a friction event.")
    log.add_argument("--kind", required=True, choices=sorted(ALLOWED_KINDS))
    log.add_argument("--summary", required=True)
    log.add_argument("--route", default="")
    log.add_argument("--severity", default="P2")
    log.add_argument("--evidence", default="")
    log.add_argument("--next-action", required=True)
    log.add_argument("--trigger", default="")
    log.add_argument("--failure-class", default="")
    log.add_argument("--user-signal", default="")
    log.add_argument("--source-session", default="")
    log.add_argument("--owner", default="")
    log.add_argument("--status", default="")

    sub.add_parser("report", help="Summarize the ledger.")
    sub.add_parser("verify", help="Validate ledger schema.")

    args = parser.parse_args()
    if args.command == "log":
        event = append_event(
            {
                "kind": args.kind,
                "summary": args.summary,
                "route": args.route,
                "severity": args.severity,
                "evidence": args.evidence,
                "next_action": args.next_action,
                "trigger": args.trigger,
                "failure_class": args.failure_class,
                "user_signal": args.user_signal,
                "source_session": args.source_session,
                "owner": args.owner,
                "status": args.status,
            }
        )
        print(json.dumps(event, indent=2, ensure_ascii=False))
    elif args.command == "report":
        print(json.dumps(summarize(read_events()), indent=2, ensure_ascii=False))
    elif args.command == "verify":
        verify()
        print("FRICTION LEDGER VERIFICATION PASS")
    else:
        parser.print_help()
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
