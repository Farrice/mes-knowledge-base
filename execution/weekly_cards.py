#!/usr/bin/env python3
"""
weekly_cards.py — Mint the two weekly self-improvement mission cards.

Born 2026-08-06, God Agent delta moves #2 and #3. Deterministic minter (no LLM):
the intelligence runs at 2 AM when execution/mission_runner.py picks the cards
up under its existing T1-only gates. Cost to run: $0 at mint; two T1 cards/week
of Claude plan usage at execution.

Card 1 — HARNESS EVALS (move #2): run evolution_store/harness_evals/eval_set_v1.md,
grade observed runs PASS/FAIL/NOT_RUN/BLOCKED, report-only scorecard.

Card 2 — VERDICT-TO-DIFF (move #3): aggregate the week's low-composite finalize
rows + fresh feedback memories + failure-registry entries into PROPOSED skill-file
diffs (reviewable file, human-approved, never auto-applied). Their nightly
thumbs-down job (39:09) fused with our taste ledger.

Usage:
    python3 execution/weekly_cards.py mint          # both (idempotent per ISO week)
    python3 execution/weekly_cards.py mint --card evals|diffs
"""

import argparse
import os
import re
from datetime import datetime, timedelta

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PENDING = os.path.join(ROOT, '.agent', 'mission-queue', 'pending')
DONE = os.path.join(ROOT, '.agent', 'mission-queue', 'done')
MEMORY_DIR = os.path.expanduser(
    '~/.claude/projects/-Users-farricecain-Google-Antigravity/memory')


def week_tag():
    return datetime.now().strftime('%G-W%V')


def already_minted(stub):
    """Idempotent per ISO week across pending AND done."""
    name = f"card-{stub}-{week_tag()}.md"
    return any(os.path.exists(os.path.join(d, name)) for d in (PENDING, DONE)), name


def write_card(name, lines):
    os.makedirs(PENDING, exist_ok=True)
    path = os.path.join(PENDING, name)
    with open(path, 'w') as f:
        f.write('\n'.join(lines) + '\n')
    return path


def recent_low_scores(days=7):
    """Pull finalize rows under 7.0 composite from knowledge/log.md, last N days."""
    log = os.path.join(ROOT, 'knowledge', 'log.md')
    if not os.path.exists(log):
        return []
    cutoff = datetime.now() - timedelta(days=days)
    rows = []
    for line in open(log):
        m = re.match(r"- `\[(\d{4}-\d{2}-\d{2})[^\]]*\]` \*\*finalize\*\* \| (.+?) — composite:([\d.]+)", line)
        if not m:
            continue
        try:
            d = datetime.strptime(m.group(1), '%Y-%m-%d')
        except ValueError:
            continue
        if d >= cutoff and float(m.group(3)) < 7.0:
            rows.append(f"  - {m.group(1)} | composite {m.group(3)} | {m.group(2)[:140]}")
    return rows[-15:]


def fresh_feedback_memories(days=7):
    if not os.path.isdir(MEMORY_DIR):
        return []
    cutoff = datetime.now().timestamp() - days * 86400
    out = []
    for f in os.listdir(MEMORY_DIR):
        p = os.path.join(MEMORY_DIR, f)
        if f.startswith('feedback') and f.endswith('.md') and os.path.getmtime(p) > cutoff:
            out.append(f"  - {f}")
    return out


def _measured_harness_block():
    """Pre-fill E1/E2/E5 evidence with execution/harness_behavior_report.py
    numbers (7d window) so the weekly eval grades against measured deltas,
    never bare instructions or file presence (the 2026-09-07 evidence-
    correction scar this eval set already carries). UNKNOWN — no db, no
    readable archives — degrades to an explicit unavailable line in that
    slot, never a PASS."""
    try:
        from harness_behavior_report import summary as _hb_summary
        hb = _hb_summary(days=7)
    except Exception as e:
        hb = {"status": "UNKNOWN", "reason": f"{type(e).__name__}: {e}"}

    if hb.get("status") == "UNKNOWN":
        unavailable = f"MEASUREMENT UNAVAILABLE: {hb.get('reason', 'no reason given')}"
        return [
            "## Measured (harness_behavior_report, 7d)",
            unavailable,
            "",
            f"- E1 evidence (router fires / calls-per-turn): {unavailable}",
            f"- E2 evidence (intent mirror / turns needing >3 calls): {unavailable}",
            f"- E5 evidence (verbosity register / prose per call): {unavailable}",
        ]

    lines = [
        "## Measured (harness_behavior_report, 7d)",
        f"Generated {hb['generated']} · window: {hb['window']} — grade E1/E2/E5 against",
        "these measured deltas, not instructions or file presence.",
        "",
        "| model | harness | turns | calls/turn | writes/turn | prose/call | %<=3 calls | %final w/ path |",
        "|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for model, mm in sorted(hb["by_model"].items(), key=lambda kv: -kv[1]["turns"]):
        lines.append(
            f"| {model} | {mm['harness']} | {mm['turns']} | {mm['calls_per_turn']} | "
            f"{mm['writes_per_turn']} | {mm['prose_chars_per_call']} | "
            f"{mm['pct_turns_le3_calls']}% | {mm['pct_final_with_artifact_path']}% |"
        )
    if hb.get("flags"):
        lines += ["", "Flags (>30% calls/turn drop vs 14d baseline):"]
        lines += [f"- {f}" for f in hb["flags"]]
    lines.append("")

    top_model, top_stats = max(hb["by_model"].items(), key=lambda kv: kv[1]["turns"])
    baseline = (hb.get("baseline_14d") or {}).get(top_model)
    lines += [
        f"- E1 evidence (router fires / calls-per-turn): {top_model} calls/turn "
        f"{top_stats['calls_per_turn']}"
        + (f" vs 14d median {baseline}" if baseline is not None else " (no 14d baseline yet)")
        + " — a collapse toward 0 is a routing regression; the number alone is not proof of a pass.",
        f"- E2 evidence (intent mirror / turns needing >3 calls): {top_model} "
        f"{top_stats['pct_turns_le3_calls']}% of turns needed <=3 calls — read alongside the "
        "actual transcript; a high share with no mirror text argues against E2, not for it.",
        f"- E5 evidence (verbosity register / prose per call): {top_model} "
        f"{top_stats['prose_chars_per_call']} chars/call — compare against E5's <=120-word "
        "(~700 char) expectation; a rising figure flags register drift.",
    ]
    return lines


def mint_evals():
    exists, name = already_minted('harness-evals')
    if exists:
        return None
    measured = _measured_harness_block()
    return write_card(name, [
        f"# Mission Card — Weekly harness behavioral evals ({week_tag()})",
        "Tier: T1",
        f"Produced: {datetime.now().strftime('%Y-%m-%d')} (queued by execution/weekly_cards.py)",
        "",
        "## Objective",
        "Run every eval in `evolution_store/harness_evals/eval_set_v1.md` exactly as specified",
        "and write the scorecard in the format that file defines. Report-only: failing evals",
        "nudge, they never block or modify anything. Do not edit any skill, directive, or hook",
        "from inside this mission — findings only.",
        "",
        "## Context to load first",
        "- `evolution_store/harness_evals/eval_set_v1.md` (the eval definitions + scorecard format)",
        "",
        *measured,
        "",
        "## Constraints",
        "- DRAFTS AND FILES ONLY. Nothing transmitted, posted, or purchased.",
        "- E4 runs against a TEMP copy only — never touch the real queue's cards.",
        "- PASS/FAIL requires an actual run and linked response or tool-output evidence; source instructions are not proof.",
        "- Mark unexecuted cases NOT_RUN or BLOCKED with a reason; do not launch unapproved models, tasks or subagents.",
        "- Save the JSON evidence sidecar and run execution/verify_harness_eval_evidence.py against it.",
        "- Report PASS/FAIL/NOT_RUN/BLOCKED counts separately; no notifications or other external writes.",
    ])


def mint_diffs():
    exists, name = already_minted('verdict-to-diff')
    if exists:
        return None
    lows = recent_low_scores()
    feedback = fresh_feedback_memories()
    if not lows and not feedback:
        return None  # nothing to compile this week — mint nothing, not an empty ritual
    return write_card(name, [
        f"# Mission Card — Verdict-to-diff compiler ({week_tag()})",
        "Tier: T1",
        f"Produced: {datetime.now().strftime('%Y-%m-%d')} (queued by execution/weekly_cards.py)",
        "",
        "## Objective",
        "The week's quality verdicts are below. For each pattern that repeats (not one-offs),",
        "PROPOSE a concrete skill-file or directive edit as a unified diff or exact",
        "before/after block. Write ALL proposals to",
        f"`evolution_store/proposed-diffs/{datetime.now().strftime('%Y-%m-%d')}.md`,",
        "one block per proposal: root pattern -> file -> proposed edit -> expected effect.",
        "NEVER apply any edit. Farrice (or a session he directs) reviews and applies.",
        "",
        "### Low-composite finalize rows (last 7d, <7.0)",
        *(lows or ["  - none"]),
        "",
        "### Feedback memories touched in the last 7d",
        *(feedback or ["  - none"]),
        "",
        "## Context to load first",
        "- `evolution_store/failure-registry.md` (recent entries only)",
        "- `evolution_store/ground_truth/rubric_v1.md` (what the scores mean)",
        "",
        "## Constraints",
        "- DRAFTS AND FILES ONLY. Proposals, never applications.",
        "- Max 5 proposals; repeated patterns only; density over completeness.",
    ])


def main():
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest='command')
    pm = sub.add_parser('mint')
    pm.add_argument('--card', choices=['evals', 'diffs'], default=None)
    args = p.parse_args()
    if args.command != 'mint':
        p.print_help()
        return
    minted = []
    if args.card in (None, 'evals'):
        r = mint_evals()
        if r:
            minted.append(r)
    if args.card in (None, 'diffs'):
        r = mint_diffs()
        if r:
            minted.append(r)
    print({'minted': [os.path.basename(m) for m in minted] or 'nothing (already minted this week or no material)'})


if __name__ == '__main__':
    main()
