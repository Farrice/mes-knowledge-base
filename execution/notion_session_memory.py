#!/usr/bin/env python3
"""Privacy-gated local outbox for Notion Session Memory.

Closeout always queues locally. Only explicitly approved rows are eligible for
network sync. The nightly Notion mirror drains approved rows before pulling the
remote databases back into sovereign memory.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Optional

from notion_api import NotionAPI


ROOT = Path(__file__).resolve().parents[1]
OUTBOX_PATH = ROOT / ".agent" / "sessions" / "notion-session-memory-outbox.jsonl"
EVENTS_PATH = ROOT / ".agent" / "sessions" / "notion-session-memory-events.jsonl"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(row, dict):
            rows.append(row)
    return rows


def _append(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")


def make_key(source_key: str, title: str, date_str: str) -> str:
    raw = f"{source_key}\n{date_str}\n{title}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:20]


def queue_record(*, title: str, key_decisions: str, pickup_prompt: str,
                 mode: str, source_key: str, date_str: Optional[str] = None) -> dict[str, Any]:
    date_str = date_str or date.today().isoformat()
    key = make_key(source_key, title, date_str)
    existing = {row.get("key"): row for row in _read_jsonl(OUTBOX_PATH)}
    if key in existing:
        return {**existing[key], "duplicate": True}
    row = {
        "key": key,
        "queued_at": _now(),
        "status": "pending_review",
        "title": (title or "Session closeout")[:200],
        "date": date_str,
        "mode": (mode or "Codex")[:100],
        "key_decisions": (key_decisions or "")[:1900],
        "pickup_prompt": (pickup_prompt or "")[:1900],
        "source_key": source_key,
    }
    _append(OUTBOX_PATH, row)
    return row


def records() -> dict[str, dict[str, Any]]:
    state = {row["key"]: dict(row) for row in _read_jsonl(OUTBOX_PATH) if row.get("key")}
    for event in _read_jsonl(EVENTS_PATH):
        key = event.get("key")
        if key not in state:
            continue
        action = event.get("action")
        if action in {"approved", "rejected", "synced"}:
            state[key]["status"] = action
        elif action == "sync_failed":
            state[key]["last_sync_error"] = event.get("error", "unknown")
        state[key]["last_event_at"] = event.get("at")
        if event.get("url"):
            state[key]["notion_url"] = event["url"]
    return state


def _resolve_key(prefix: str) -> str:
    matches = [key for key in records() if key.startswith(prefix)]
    if not matches:
        raise KeyError(f"No Session Memory row matches '{prefix}'")
    if len(matches) > 1:
        raise KeyError(f"Ambiguous key prefix '{prefix}'")
    return matches[0]


def set_review_status(prefix: str, action: str) -> dict[str, Any]:
    if action not in {"approved", "rejected"}:
        raise ValueError("action must be approved or rejected")
    key = _resolve_key(prefix)
    current = records()[key]
    if current["status"] == "synced":
        return current
    event = {"key": key, "action": action, "at": _now()}
    _append(EVENTS_PATH, event)
    return records()[key]


def sync_approved(*, dry_run: bool = False, only_key: str = "",
                  api: Optional[NotionAPI] = None) -> dict[str, Any]:
    state = records()
    selected = []
    resolved_only = _resolve_key(only_key) if only_key else ""
    for key, row in state.items():
        if resolved_only and key != resolved_only:
            continue
        if row.get("status") == "approved":
            selected.append(row)
    result = {"eligible": len(selected), "synced": 0, "failed": 0, "dry_run": dry_run}
    if dry_run or not selected:
        return result
    api = api or NotionAPI()
    for row in selected:
        try:
            existing = api.find_session_memory(
                row["title"], row["date"], row["key_decisions"], row["pickup_prompt"]
            )
            url = existing or api.push_session_memory(
                row["title"], row["key_decisions"], pickup_prompt=row["pickup_prompt"],
                mode=row["mode"], date_str=row["date"],
            )
            _append(EVENTS_PATH, {
                "key": row["key"], "action": "synced", "at": _now(),
                "url": url, "deduplicated": bool(existing),
            })
            result["synced"] += 1
        except Exception as exc:
            _append(EVENTS_PATH, {
                "key": row["key"], "action": "sync_failed", "at": _now(),
                "error": f"{type(exc).__name__}: {exc}"[:500],
            })
            result["failed"] += 1
    return result


def status_payload() -> dict[str, Any]:
    state = records()
    counts: dict[str, int] = {}
    for row in state.values():
        status = row.get("status", "unknown")
        counts[status] = counts.get(status, 0) + 1
    return {"total": len(state), "counts": counts, "records": list(state.values())}


def main() -> int:
    parser = argparse.ArgumentParser(description="Privacy-gated Notion Session Memory outbox")
    sub = parser.add_subparsers(dest="command", required=True)
    queue = sub.add_parser("queue")
    queue.add_argument("title")
    queue.add_argument("--decisions", required=True)
    queue.add_argument("--pickup", default="")
    queue.add_argument("--mode", default="Codex")
    queue.add_argument("--source-key", required=True)
    queue.add_argument("--date", default=None)
    for action in ("approve", "reject"):
        cmd = sub.add_parser(action)
        cmd.add_argument("key")
    sync = sub.add_parser("sync")
    sync.add_argument("--key", default="")
    sync.add_argument("--dry-run", action="store_true")
    status = sub.add_parser("status")
    status.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.command == "queue":
        out = queue_record(
            title=args.title, key_decisions=args.decisions, pickup_prompt=args.pickup,
            mode=args.mode, source_key=args.source_key, date_str=args.date,
        )
    elif args.command in {"approve", "reject"}:
        out = set_review_status(args.key, "approved" if args.command == "approve" else "rejected")
    elif args.command == "sync":
        out = sync_approved(dry_run=args.dry_run, only_key=args.key)
    else:
        out = status_payload()
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 1 if isinstance(out, dict) and out.get("failed", 0) else 0


if __name__ == "__main__":
    raise SystemExit(main())
