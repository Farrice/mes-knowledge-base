#!/usr/bin/env python3
"""voice_ratchet.py — deterministic capture spine for the Voice OS calibration log.

Voice OS (skills/voice-os/) needs a physical write path for felt verdicts —
the moment Farrice reacts to a line (praise or wince) — so calibration data
never depends on an agent remembering to log it mid-conversation. Same law as
`thought_bank.py`: infra must never depend on a human or model remembering a
step (feedback `ai-memory-dependent-observability`).

This CLI is the ONE writer of `_active/farrice-brand/voice/calibration-log.md`.
It does no LLM work — verdict classification, rewrites, and the actual card
recompile are all judgment calls the `/voice-compile` workflow makes; this
script only tracks state: append rows, count them, mark the last compile
point.

Subcommands:
    add --verdict {pass,fail} --line "..." --why "..." [--source "..."]
                                Append one row to the calibration log (today's
                                date, pipe-escaped fields). Deduped on exact
                                line text — skip + warn if already present.
    status                      Card version (if VOICE-CARD.md exists), total
                                PASS/FAIL counts, entries since last compile,
                                and a RECOMPILE RECOMMENDED flag at >=5 pending.
    mark-compiled                Record the current entry count as the compile
                                point (state lives in .agent/voice-ratchet-state.json).

Usage:
    python3 execution/voice_ratchet.py add --verdict fail --line "..." --why "..." --source "LinkedIn draft 07-07"
    python3 execution/voice_ratchet.py status
    python3 execution/voice_ratchet.py mark-compiled
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

REPO_ROOT = Path(__file__).resolve().parents[1]
VOICE_DIR = REPO_ROOT / "_active" / "farrice-brand" / "voice"
CALIBRATION_LOG = VOICE_DIR / "calibration-log.md"
VOICE_CARD = VOICE_DIR / "VOICE-CARD.md"
STATE_FILE = REPO_ROOT / ".agent" / "voice-ratchet-state.json"

# Per-client ratchets (2026-08-05, listing-package pipeline): same capture spine,
# different log. Default (no --client) is Farrice's Voice OS — behavior unchanged.
# A client entry maps to its calibration log + the "card" its skill compiles into.
CLIENTS = {
    "jen": {
        "log": REPO_ROOT / "skills" / "jen-santulan-listing-content" / "references" / "jen-calibration-log.md",
        "card": REPO_ROOT / "skills" / "jen-santulan-listing-content" / "references" / "jen-real-voice-profile.md",
        "title": "Jen Listing-Content Calibration Log",
        "blurb": (
            "Felt verdicts on Jen listing hooks/scripts/captions — Farrice's taste calls "
            "and Jen's own picks/rejections. Consumed by prompts-v2/listing-hook-set.md "
            "(calibration outranks defaults); register ladder canon lives in "
            "_active/clients/jen-listings/CLAUDE.md."
        ),
    },
}


def _apply_client(client: Optional[str]) -> None:
    """Rewire the module's log/card/state paths for a per-client ratchet.
    No-op for the default (Farrice) so existing callers are untouched."""
    global CALIBRATION_LOG, VOICE_CARD, STATE_FILE, _LOG_TITLE, _LOG_BLURB
    if not client:
        return
    cfg = CLIENTS.get(client)
    if cfg is None:
        raise SystemExit(f"Unknown --client '{client}' (known: {', '.join(sorted(CLIENTS))})")
    CALIBRATION_LOG = cfg["log"]
    VOICE_CARD = cfg["card"]
    STATE_FILE = REPO_ROOT / ".agent" / f"voice-ratchet-state-{client}.json"
    _LOG_TITLE = cfg["title"]
    _LOG_BLURB = cfg["blurb"]


_LOG_TITLE = "Voice Calibration Log"
_LOG_BLURB = (
    "Felt verdicts on lines Farrice reacted to — praise or wince — captured "
    "verbatim via `/voice-ratchet`. Source for VOICE-CARD.md §6 Calibration "
    "Bank; recompiled via `/voice-compile`."
)

TABLE_HEADER = "| date | verdict | line | why | source |"
TABLE_DIVIDER = "|------|---------|------|-----|--------|"

ROW_RE = re.compile(r"^\|(.+)\|\s*$")


def _today() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def _escape(text: str) -> str:
    return text.strip().replace("|", "\\|")


def _unescape(text: str) -> str:
    return text.replace("\\|", "|").strip()


def _split_row(row: str) -> List[str]:
    """Split a markdown table row on unescaped pipes, unescape each cell."""
    cells = re.split(r"(?<!\\)\|", row.strip().strip("|"))
    return [_unescape(c) for c in cells]


def _ensure_log() -> None:
    if CALIBRATION_LOG.exists():
        return
    CALIBRATION_LOG.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "---\n"
        f"created: {_today()}\n"
        "---\n\n"
        f"# {_LOG_TITLE}\n\n"
        f"{_LOG_BLURB}\n\n"
        f"{TABLE_HEADER}\n{TABLE_DIVIDER}\n"
    )
    CALIBRATION_LOG.write_text(header)


def read_rows() -> List[Dict[str, str]]:
    """Parse all data rows from the calibration log table. Empty list if the
    file doesn't exist yet or has no table."""
    if not CALIBRATION_LOG.exists():
        return []
    rows: List[Dict[str, str]] = []
    for line in CALIBRATION_LOG.read_text().splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        cells = _split_row(line)
        if len(cells) != 5:
            continue
        if cells[0].strip().lower() == "date" or set(cells[0].strip()) <= {"-"}:
            continue  # header or divider row
        rows.append({
            "date": cells[0],
            "verdict": cells[1],
            "line": cells[2],
            "why": cells[3],
            "source": cells[4],
        })
    return rows


def _load_state() -> Dict:
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text())
    except (json.JSONDecodeError, OSError):
        return {}


def _save_state(state: Dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2) + "\n")


def cmd_add(args) -> int:
    _ensure_log()
    rows = read_rows()
    line_norm = " ".join(args.line.strip().lower().split())
    for row in rows:
        if " ".join(row["line"].strip().lower().split()) == line_norm:
            print(f"Already logged (exact line match) — skipping: \"{args.line.strip()[:80]}\"")
            _print_counts(read_rows())
            return 0

    verdict = args.verdict.upper()
    new_row = (
        f"| {_today()} | {verdict} | {_escape(args.line)} | "
        f"{_escape(args.why)} | {_escape(args.source or '-')} |\n"
    )
    with CALIBRATION_LOG.open("a") as f:
        f.write(new_row)

    print(f"Logged {verdict}: \"{args.line.strip()[:80]}\"")
    _print_counts(read_rows())
    return 0


def _print_counts(rows: List[Dict[str, str]]) -> None:
    passes = sum(1 for r in rows if r["verdict"].strip().upper() == "PASS")
    fails = sum(1 for r in rows if r["verdict"].strip().upper() == "FAIL")
    state = _load_state()
    compiled_at = state.get("entries_at_compile", 0)
    pending = max(0, len(rows) - compiled_at)
    print(f"Total: {len(rows)} ({passes} PASS / {fails} FAIL) | Pending since last compile: {pending}")


def _card_version() -> Optional[str]:
    if not VOICE_CARD.exists():
        return None
    text = VOICE_CARD.read_text()
    fm = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not fm:
        return None
    m = re.search(r"^version:\s*[\"']?([^\"'\n]+)[\"']?\s*$", fm.group(1), re.MULTILINE)
    return m.group(1).strip() if m else None


def cmd_status(_args) -> int:
    rows = read_rows()
    passes = sum(1 for r in rows if r["verdict"].strip().upper() == "PASS")
    fails = sum(1 for r in rows if r["verdict"].strip().upper() == "FAIL")
    state = _load_state()
    compiled_at = state.get("entries_at_compile", 0)
    last_compiled = state.get("last_compiled_at", "never")
    pending = max(0, len(rows) - compiled_at)

    version = _card_version()
    print("Voice Ratchet Status")
    print("---------------------")
    if VOICE_CARD.exists():
        print(f"VOICE-CARD.md version: {version or '(no version field found)'}")
    else:
        print("VOICE-CARD.md: not found — card not yet compiled")
    print(f"Calibration log: {CALIBRATION_LOG if CALIBRATION_LOG.exists() else '(not yet created)'}")
    print(f"Total entries: {len(rows)} ({passes} PASS / {fails} FAIL)")
    print(f"Last compiled: {last_compiled} (at {compiled_at} entries)")
    print(f"Pending since last compile: {pending}")
    if pending >= 5:
        print("\nRECOMPILE RECOMMENDED — run /voice-compile")
    return 0


def cmd_mark_compiled(_args) -> int:
    rows = read_rows()
    state = {
        "last_compiled_at": datetime.now().isoformat(timespec="seconds"),
        "entries_at_compile": len(rows),
    }
    _save_state(state)
    print(f"Marked compiled at {len(rows)} entries ({state['last_compiled_at']}).")
    return 0


def cmd_nudge(args) -> int:
    """Apex W2 (2026-07-29): the ratchet's own >=5 recompile threshold existed
    with no trigger — 16 rows sat pending while the pen briefed from a stale
    card. House style: silent when healthy, one line when not, exit 0 always."""
    try:
        state = _load_state()
        pending = len(read_rows()) - int(state.get("entries_at_compile", 0))
        if pending >= 5:
            print(f"VOICE RATCHET: {pending} felt verdicts pending compile — "
                  "run /voice-compile before the next pen session "
                  "(a stale card briefs the pen against an old bar).")
    except Exception as e:
        # never break SessionStart, but never hide the break either (W0.1 scar)
        print(f"VOICE RATCHET nudge error (non-blocking): {type(e).__name__}: {e}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Voice OS calibration-log ratchet")
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--client", default=None,
                        help=f"Per-client ratchet (known: {', '.join(sorted(CLIENTS))}). Default: Farrice Voice OS.")
    sub = parser.add_subparsers(dest="command", required=True)

    pa = sub.add_parser("add", parents=[common], help="Append a felt-verdict row to the calibration log")
    pa.add_argument("--verdict", required=True, choices=["pass", "fail"])
    pa.add_argument("--line", required=True, help="Verbatim line Farrice reacted to")
    pa.add_argument("--why", required=True, help="Why it passed/failed")
    pa.add_argument("--source", default="", help="Where the line came from (piece, channel, date)")
    pa.set_defaults(func=cmd_add)

    ps = sub.add_parser("status", parents=[common], help="Show card version + calibration-log counts")
    ps.set_defaults(func=cmd_status)

    pc = sub.add_parser("mark-compiled", parents=[common], help="Record the current entry count as the compile point")
    pc.set_defaults(func=cmd_mark_compiled)

    pn = sub.add_parser("nudge", parents=[common], help="One line if >=5 verdicts pending compile; silent otherwise (SessionStart-safe)")
    pn.set_defaults(func=cmd_nudge)

    args = parser.parse_args()
    _apply_client(getattr(args, "client", None))
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
