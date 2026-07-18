#!/usr/bin/env python3
"""mission_runner.py — AFK overnight mission-runner CORE (T1-only).

Born 2026-07-18 (Wave 7, Frontier Elevation Program) to let /go Mission Cards
run unattended overnight without a human in the loop, while keeping every
outward/paid/destructive action behind the same gates a human conductor would
respect. Encodes orchestration-doctrine.md's Blast-Radius Autonomy Tiers
(Law: T1 auto-run, T2/T3 always wait) as a mechanism, not a hope:

  - concurrent-session collision (the "apply one fix, another breaks" failure,
    root-caused 2026-06-30 / doctrine Law 5): guarded by claiming
    execution/session_lock.py before touching any card, released in a
    `finally` block so a crashed run never bricks the tree.
  - T2/T3 auto-execution while no human is watching: guarded by parsing the
    card's declared Tier line and refusing to invoke `claude -p` on anything
    but T1 — T2/T3 cards move to parked/ UNTOUCHED (file body never rewritten).
  - autonomous publish/send/spend: guarded by a regex refusal net that parks
    ANY card (T1 included) whose text matches publish/send/post-to/payment/
    purchase/deploy, with the matched word recorded as the parking reason —
    this runner produces drafts, never actions with outward or financial
    effect.
  - silent overnight failure: guarded by the `receipt` command, which turns
    done/ + parked/ into a single COS-readable morning brief, never leaving
    Farrice to reconstruct what ran from raw transcripts.

Usage:
    python3 execution/mission_runner.py queue <card.md>
    python3 execution/mission_runner.py run [--dry-run] [--timeout SECONDS]
    python3 execution/mission_runner.py status
    python3 execution/mission_runner.py receipt

--queue-dir / --cos-dir (all subcommands) override the default repo-root
locations — used by execution/verify_mission_runner.py to run the fixture
against a temp queue instead of the real overnight queue.

Exit codes (run): 0 = completed (T1 cards may still have failed — see receipt/
transcripts), 1 = lock held by another session, no cards touched.
"""
from __future__ import annotations

import argparse
import datetime
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUEUE_DIR = ROOT / ".agent" / "mission-queue"
DEFAULT_COS_DIR = ROOT / ".agent" / "cos"
LOCK_SCRIPT = ROOT / "execution" / "session_lock.py"

TIER_RE = re.compile(r"Tier:\s*\**\s*(T[123])", re.IGNORECASE)
# Refusal net (Blast-Radius Autonomy Tier T2/T3 outward actions, doctrine):
# a card matching any of these never auto-executes, regardless of its
# declared tier — a mis-tiered card is not an excuse to publish/send/spend.
FORBIDDEN_RE = re.compile(r"\b(publish|send|post to|payment|purchase|deploy)\b", re.IGNORECASE)

DEFAULT_TIMEOUT = 3600


def _queue_paths(args: argparse.Namespace) -> tuple[Path, Path, Path]:
    base = Path(args.queue_dir)
    return base / "pending", base / "parked", base / "done"


def _cos_dir(args: argparse.Namespace) -> Path:
    return Path(args.cos_dir)


def _ensure_dirs(pending: Path, parked: Path, done: Path) -> None:
    for d in (pending, parked, done):
        d.mkdir(parents=True, exist_ok=True)


def _unique_dest(dest_dir: Path, name: str) -> Path:
    """Prevents a same-named card silently clobbering an already-queued one."""
    dest = dest_dir / name
    if not dest.exists():
        return dest
    stamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    stem = Path(name).stem
    suffix = Path(name).suffix or ".md"
    return dest_dir / f"{stem}-{stamp}{suffix}"


def cmd_queue(args: argparse.Namespace) -> int:
    pending, parked, done = _queue_paths(args)
    _ensure_dirs(pending, parked, done)
    src = Path(args.card).expanduser().resolve()
    if not src.is_file():
        print(f"NO CARD: {src} does not exist")
        return 1
    dest = _unique_dest(pending, src.name)
    shutil.copy2(src, dest)
    print(f"queued: {dest}")
    return 0


def _park(card: Path, parked: Path, reason: str) -> None:
    """Moves the card body UNTOUCHED into parked/ and records why alongside it
    — the card's content is never rewritten (a T2/T3 card is not a T1 card
    with edits, it is a card someone still needs to look at)."""
    dest = _unique_dest(parked, card.name)
    shutil.move(str(card), dest)
    reason_path = dest.with_suffix(dest.suffix + ".reason.txt")
    reason_path.write_text(f"{reason}\nparked: {datetime.datetime.now().isoformat(timespec='seconds')}\n")
    print(f"PARKED {card.name}: {reason}")


def _execute_t1(card: Path, done: Path, dry_run: bool, timeout: int) -> None:
    """Runs a T1 card headless. dry-run skips the actual `claude -p` spawn
    (never recurse a live agent into a fresh claude process just to prove the
    plumbing works) and writes a stub transcript instead."""
    body = card.read_text()
    transcript = done / f"{card.stem}-transcript.md"
    if dry_run:
        transcript.write_text(
            f"# DRY-RUN STUB TRANSCRIPT\ncard: {card.name}\n"
            f"claude -p invocation skipped (--dry-run)\n"
            f"would run: claude -p <card body, {len(body)} chars> --permission-mode acceptEdits\n"
        )
        outcome = "DRY-RUN STUB"
    else:
        try:
            result = subprocess.run(
                ["claude", "-p", body, "--permission-mode", "acceptEdits"],
                cwd=ROOT, capture_output=True, text=True, timeout=timeout,
            )
            out = result.stdout
            if result.stderr:
                out += f"\n\n---STDERR---\n{result.stderr}"
            transcript.write_text(out)
            outcome = "COMPLETED" if result.returncode == 0 else f"EXIT {result.returncode}"
        except subprocess.TimeoutExpired:
            transcript.write_text(f"TIMEOUT after {timeout}s — card: {card.name}\n")
            outcome = f"TIMEOUT ({timeout}s)"
        except FileNotFoundError:
            transcript.write_text("claude CLI not found on PATH — cannot execute headless.\n")
            outcome = "CLI NOT FOUND"
    shutil.move(str(card), done / card.name)
    print(f"T1 EXECUTED {card.name}: {outcome} -> {transcript}")


def cmd_run(args: argparse.Namespace) -> int:
    pending, parked, done = _queue_paths(args)
    _ensure_dirs(pending, parked, done)
    lock = subprocess.run(
        [sys.executable, str(LOCK_SCRIPT), "claim", "mission_runner overnight run"],
        cwd=ROOT, capture_output=True, text=True,
    )
    if lock.returncode != 0:
        print("ABORT: session lock held by another driver — one driver per tree "
              "(orchestration-doctrine.md Law 5). No cards touched.")
        print(lock.stdout.strip())
        return 1
    token_match = re.search(r"claimed:\s*([0-9a-f]+)", lock.stdout)
    token = token_match.group(1) if token_match else None
    print(lock.stdout.strip())

    try:
        cards = sorted(p for p in pending.glob("*.md"))
        if not cards:
            print("no pending cards")
        for card in cards:
            text = card.read_text()
            forbidden = FORBIDDEN_RE.search(text)
            if forbidden:
                _park(card, parked, f"refused: matched outward-action pattern '{forbidden.group(0)}' "
                                     f"(publish/send/post-to/payment/purchase/deploy are never auto-run)")
                continue
            tier_match = TIER_RE.search(text)
            tier = tier_match.group(1).upper() if tier_match else None
            if tier != "T1":
                reason = (f"tier {tier} requires Farrice's nod (T2/T3 never auto-run)"
                          if tier else "no Tier: line found — treated as non-T1, requires review")
                _park(card, parked, reason)
                continue
            _execute_t1(card, done, dry_run=args.dry_run, timeout=args.timeout)
        return 0
    finally:
        if token:
            rel = subprocess.run(
                [sys.executable, str(LOCK_SCRIPT), "release", token],
                cwd=ROOT, capture_output=True, text=True,
            )
            print(rel.stdout.strip() or rel.stderr.strip())


def cmd_status(args: argparse.Namespace) -> int:
    pending, parked, done = _queue_paths(args)
    _ensure_dirs(pending, parked, done)
    for label, d in (("pending", pending), ("parked", parked), ("done", done)):
        files = sorted(d.glob("*.md"))
        print(f"{label} ({len(files)}):")
        for f in files:
            tier_match = TIER_RE.search(f.read_text()) if f.exists() else None
            tier = tier_match.group(1).upper() if tier_match else "?"
            print(f"  [{tier}] {f.name}")
    return 0


def cmd_receipt(args: argparse.Namespace) -> int:
    pending, parked, done = _queue_paths(args)
    _ensure_dirs(pending, parked, done)
    cos_dir = _cos_dir(args)
    cos_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.date.today().isoformat()
    out_path = cos_dir / f"overnight-receipt-{today}.md"

    done_cards = sorted(p for p in done.glob("*.md") if not p.name.endswith("-transcript.md"))
    parked_cards = sorted(p for p in parked.glob("*.md"))

    lines = [
        f"# Overnight Mission Receipt — {today}",
        "",
        "**Drafts-only disclaimer**: everything below is local, in-repo output from "
        "T1 (reversible, in-repo, $0) cards only. Nothing was published, sent, "
        "deployed, or paid for by this run — those actions are always parked for "
        "a human nod (orchestration-doctrine.md Blast-Radius Tiers).",
        "",
        f"## Executed (T1) — {len(done_cards)}",
    ]
    if not done_cards:
        lines.append("_none this run_")
    for card in done_cards:
        transcript = done / f"{card.stem}-transcript.md"
        if transcript.exists():
            stub = "DRY-RUN STUB" in transcript.read_text()[:200]
            tag = "dry-run stub" if stub else "executed"
            lines.append(f"- `{card.name}` ({tag}) — transcript: `{transcript}`")
        else:
            lines.append(f"- `{card.name}` — NO TRANSCRIPT FOUND")

    lines += ["", f"## Parked (needs a nod) — {len(parked_cards)}"]
    if not parked_cards:
        lines.append("_none this run_")
    for card in parked_cards:
        reason_path = card.with_suffix(card.suffix + ".reason.txt")
        reason = reason_path.read_text().splitlines()[0] if reason_path.exists() else "reason unknown"
        lines.append(f"- `{card.name}` — {reason}")

    lines += [
        "",
        "## Token / cost",
        "Not available: transcripts are captured as plain stdout text, not "
        "`--output-format json`, so no per-run cost metadata exists to report "
        "honestly. Phase 2 candidate if cost visibility becomes worth the "
        "structured-output plumbing.",
        "",
        f"_generated by execution/mission_runner.py receipt — {datetime.datetime.now().isoformat(timespec='seconds')}_",
    ]

    out_path.write_text("\n".join(lines) + "\n")
    print(f"receipt written: {out_path}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--queue-dir", default=str(DEFAULT_QUEUE_DIR),
                     help="override .agent/mission-queue base (pending/parked/done live under it)")
    ap.add_argument("--cos-dir", default=str(DEFAULT_COS_DIR), help="override .agent/cos (receipt target)")
    sub = ap.add_subparsers(dest="command", required=True)

    p_queue = sub.add_parser("queue", help="copy a Mission Card into pending/")
    p_queue.add_argument("card", help="path to the Mission Card .md file")
    p_queue.set_defaults(func=cmd_queue)

    p_run = sub.add_parser("run", help="overnight entry: claim lock, execute T1 cards only")
    p_run.add_argument("--dry-run", action="store_true", help="skip the actual claude -p spawn, write a stub transcript")
    p_run.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help=f"seconds per T1 card (default {DEFAULT_TIMEOUT})")
    p_run.set_defaults(func=cmd_run)

    p_status = sub.add_parser("status", help="list pending/parked/done queues")
    p_status.set_defaults(func=cmd_status)

    p_receipt = sub.add_parser("receipt", help="write the morning COS receipt")
    p_receipt.set_defaults(func=cmd_receipt)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
