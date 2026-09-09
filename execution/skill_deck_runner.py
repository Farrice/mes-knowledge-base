#!/usr/bin/env python3
"""skill_deck_runner.py — guarded headless skill runs for the Homebase deck
(2026-08-21, ARMS-video harvest: trigger skills from the dashboard via
`claude -p`, with model + effort chosen per run).

Security contract (stress-test 2026-08-21 — this verb has the highest blast
radius on the board, so every wall is here):
- Parameters are INDICES, never text: card_id must exist in the curated
  .agent/homebase/skills-deck.json (re-read server-side on every run), and
  model/effort must be in that card's own allowlists ∩ the global enums.
  No user string ever reaches the prompt.
- mission_runner.FORBIDDEN_RE is imported verbatim (never forked) and applied
  to the card's command + blurb — publish/send/pay-shaped cards refuse to run.
- session_lock.py claim is mandatory; a fresh foreign lock aborts with a
  receipt, never queues.
- Cost is MEASURED, not estimated: runs use --output-format json and the
  receipt records total_cost_usd (cost-transparency binding, 2026-08-01).
  mission_runner deliberately punts on cost; the deck must not.

Receipts land in .agent/homebase/deck-runs/<ts>-<id>.json + a markdown report
artifact; the run regenerates the homebase at the end so an open page reloads
itself with the fresh receipt (mtime flip → /ping → reload).
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "execution"))

from mission_runner import FORBIDDEN_RE  # noqa: E402 — one refusal net, never forked

DECK_FILE = os.path.join(ROOT, ".agent", "homebase", "skills-deck.json")
RUNS_DIR = os.path.join(ROOT, ".agent", "homebase", "deck-runs")
LOCK_SCRIPT = os.path.join(ROOT, "execution", "session_lock.py")
PY = sys.executable or "python3"

MODELS = {"haiku", "sonnet", "opus", "fable"}
EFFORTS = {"low", "medium", "high", "xhigh"}
TIMEOUT_S = 30 * 60


def load_deck():
    return json.load(open(DECK_FILE, encoding="utf-8"))


def validate(card_id, model, effort):
    """(card | None, error | None). Everything is checked against the curated
    file — the POST payload is treated as untrusted indices."""
    try:
        deck = load_deck()
    except (OSError, ValueError) as e:
        return None, f"deck file unreadable: {e}"
    card = next((c for c in deck.get("cards", []) if c.get("id") == card_id), None)
    if card is None:
        return None, "unknown card"
    if model not in MODELS or model not in set(card.get("models") or []):
        return None, "model not allowed for this card"
    if effort not in EFFORTS or effort not in set(card.get("efforts") or []):
        return None, "effort not allowed for this card"
    cmd = str(card.get("command") or "")
    if not cmd.startswith("/"):
        return None, "card command must be a slash command"
    hit = FORBIDDEN_RE.search(cmd + " " + str(card.get("blurb") or ""))
    if hit:
        return None, f"refused: card matches forbidden pattern '{hit.group(0)}'"
    return card, None


def _receipt_path(ts, card_id):
    return os.path.join(RUNS_DIR, f"{ts}-{card_id}.json")


def _write(receipt, path):
    os.makedirs(RUNS_DIR, exist_ok=True)
    json.dump(receipt, open(path, "w", encoding="utf-8"), indent=1)


def _regen_homebase():
    try:
        subprocess.run([PY, os.path.join(ROOT, "execution", "homebase_board.py")],
                       capture_output=True, text=True, timeout=90)
    except Exception:
        pass


def run(card_id, model, effort):
    card, err = validate(card_id, model, effort)
    ts = time.strftime("%Y%m%d-%H%M%S")
    rpath = _receipt_path(ts, card_id if card else "invalid")
    receipt = {"card_id": card_id, "model": model, "effort": effort,
               "started": time.strftime("%Y-%m-%dT%H:%M:%S"), "state": "running"}
    if err:
        receipt.update(state="failed", error=err,
                       ended=time.strftime("%Y-%m-%dT%H:%M:%S"))
        _write(receipt, rpath)
        print(f"REFUSED: {err}", file=sys.stderr)
        return 1
    receipt["command"] = card["command"]

    lock_name = f"deck-{card_id}"
    lock = subprocess.run([PY, LOCK_SCRIPT, "claim", lock_name],
                          capture_output=True, text=True)
    if lock.returncode != 0:
        receipt.update(state="failed", error="session lock held",
                       ended=time.strftime("%Y-%m-%dT%H:%M:%S"))
        _write(receipt, rpath)
        print("BLOCKED: session lock held", file=sys.stderr)
        return 1
    # release is token-based ("claimed: <token>"); a lane tree prints "clear"
    # with no token and needs no release
    m = re.search(r"claimed:\s+([0-9a-f]{12})", lock.stdout or "")
    lock_token = m.group(1) if m else None

    _write(receipt, rpath)
    t0 = time.time()
    try:
        result = subprocess.run(
            ["claude", "-p", card["command"], "--model", model, "--effort", effort,
             "--output-format", "json", "--permission-mode", "acceptEdits"],
            capture_output=True, text=True, timeout=TIMEOUT_S, cwd=ROOT)
        out = result.stdout or ""
        cost = None
        text = out
        try:
            j = json.loads(out)
            cost = j.get("total_cost_usd")
            text = j.get("result") or out
        except ValueError:
            pass
        report_rel = f".agent/homebase/deck-runs/{ts}-{card_id}.md"
        report = (f"# Deck run · {card['command']}\n\n"
                  f"- model: {model} · effort: {effort}\n"
                  f"- started: {receipt['started']} · duration: {int(time.time() - t0)}s\n"
                  f"- measured cost: "
                  f"{f'${cost:.4f}' if isinstance(cost, (int, float)) else 'n/a'}\n\n---\n\n"
                  + text)
        (Path(ROOT) / report_rel).write_text(report, encoding="utf-8")
        receipt.update(state="done" if result.returncode == 0 else "failed",
                       ended=time.strftime("%Y-%m-%dT%H:%M:%S"),
                       duration_s=int(time.time() - t0),
                       total_cost_usd=cost, report_rel=report_rel)
        if result.returncode != 0:
            receipt["error"] = (result.stderr or "")[-300:]
    except FileNotFoundError:
        receipt.update(state="failed", error="claude CLI not found on PATH",
                       ended=time.strftime("%Y-%m-%dT%H:%M:%S"))
    except subprocess.TimeoutExpired:
        receipt.update(state="failed", error=f"timed out after {TIMEOUT_S}s",
                       ended=time.strftime("%Y-%m-%dT%H:%M:%S"),
                       duration_s=int(time.time() - t0))
    finally:
        _write(receipt, rpath)
        if lock_token:
            subprocess.run([PY, LOCK_SCRIPT, "release", lock_token],
                           capture_output=True, text=True)
        _regen_homebase()
    cost = receipt.get("total_cost_usd")
    print(f"deck run {receipt['state']}: {card['command']} on {model}/{effort} — "
          f"cost {f'${cost:.4f}' if isinstance(cost, (int, float)) else 'n/a'} "
          f"→ {rpath}")
    return 0 if receipt["state"] == "done" else 1


def main():
    ap = argparse.ArgumentParser(description="Guarded headless deck runs.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("card_id")
    r.add_argument("--model", required=True)
    r.add_argument("--effort", required=True)
    v = sub.add_parser("validate")
    v.add_argument("card_id")
    v.add_argument("--model", required=True)
    v.add_argument("--effort", required=True)
    sub.add_parser("list")
    args = ap.parse_args()
    if args.cmd == "list":
        deck = load_deck()
        for c in deck.get("cards", []):
            print(f"{c['id']}: {c['command']} — models {c.get('models')} efforts {c.get('efforts')}")
        return 0
    if args.cmd == "validate":
        card, err = validate(args.card_id, args.model, args.effort)
        print("OK" if card else f"REFUSED: {err}")
        return 0 if card else 1
    return run(args.card_id, args.model, args.effort)


if __name__ == "__main__":
    raise SystemExit(main())
