#!/usr/bin/env python3
"""cos_prep.py — deterministic prep engine for the Chief of Staff OS (/cos).

Subcommands:
    prep [--force] [--dry-run]      Build today's morning brief + nudge line
    nudge                           Print current nudge line (empty if none due)
    capture --text T [--route journal|inbox]
                                    Append to today's journal; --route inbox also
                                    mirrors to the thought-bank inbox (creative
                                    material ONLY — personal/family stays in journal)
    mark daily|weekly               Record completion, update streak, clear nudge
    status                          JSON state for /cos workflow routing

No LLM calls. Stdlib only. All writes stay under .agent/cos/ (gitignored)
except the explicit thought-bank inbox mirror.
"""

import argparse
import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
COS = REPO_ROOT / ".agent" / "cos"
BRIEFS = COS / "briefs"
JOURNAL = COS / "journal"
STATE_PATH = COS / "state.json"
GOALS_PATH = COS / "goals.json"
LIFE_PATH = COS / "life-context.md"
REVENUE = REPO_ROOT / ".agent" / "revenue-outcomes.json"
HANDOFF_STORE = REPO_ROOT / "execution" / "handoff_store.py"
THOUGHT_INBOX = REPO_ROOT / "_active" / "farrice-brand" / "thought-bank" / "inbox"

STATE_DEFAULTS = {
    "last_daily": "",
    "last_weekly": "",
    "streak": 0,
    "weekly_day": "monday",
    "nudge_line": "",
    "nudge_date": "",
    "last_prep": "",
}

WEEKLY_EVERY_DAYS = 7
REENTRY_GAP_DAYS = 3
NEVER_DAYS = 9999

# Per-section question banks. Rotation is stable-hashed on (date, section) so the
# wording varies day to day but is deterministic for a given day.
LIFE_QUESTIONS = {
    "JJ": [
        "What did you notice about JJ this week that you want to remember?",
        "What's JJ into right now — anything new since we last talked about him?",
        "One JJ moment from the last few days worth keeping?",
        "What did JJ do lately that surprised you?",
        "When did you last get real, unhurried time with JJ — and what happened in it?",
    ],
    "Jen & Family": [
        "How are things with Jen? Anything she's carrying that I should know about?",
        "Family pulse — anything happening with Jen or the family this week?",
        "What's one thing going on in Jen's world right now?",
        "Anything with the wider family that's sitting in the back of your mind?",
        "What would Jen say is going on with YOU this week, if I asked her?",
    ],
    "Health": [
        "One honest sentence: how's the body?",
        "Sleep, training, food — which one needs attention this week?",
        "How are you feeling physically, actually?",
        "What did sleep look like the last few nights?",
        "When did you last train — and how did it feel?",
    ],
    "Mindset": [
        "Where's your head at today — clear, foggy, or spinning?",
        "What's taking up mental space right now that shouldn't be?",
        "What are you avoiding thinking about?",
        "What's pulling you in different directions today — name the pulls?",
        "If today went perfectly, what would have happened by tonight?",
    ],
    "Creative": [
        "Any ideas rattling around that haven't been written down yet?",
        "What's the most alive creative thread in your head right now?",
        "Anything you read/watched lately that sparked something?",
        "What's a half-thought you've had this week that deserves a full thought?",
        "Anything from real life lately that felt like content?",
    ],
}


def _today() -> str:
    return datetime.now().date().isoformat()


def _days_since(date_str: str) -> int:
    if not date_str or date_str == "never":
        return NEVER_DAYS
    try:
        return (datetime.now().date() - datetime.fromisoformat(date_str).date()).days
    except ValueError:
        return NEVER_DAYS


def _stable_pick(options: list, *seed_parts: str):
    digest = hashlib.md5("|".join(seed_parts).encode()).hexdigest()
    return options[int(digest, 16) % len(options)]


def load_state() -> dict:
    state = dict(STATE_DEFAULTS)
    try:
        state.update(json.loads(STATE_PATH.read_text()))
    except Exception:
        pass
    return state


def save_state(state: dict) -> None:
    COS.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n")


def load_goals() -> list:
    try:
        goals = json.loads(GOALS_PATH.read_text()).get("goals", [])
        return [g for g in goals if g.get("status") == "active"]
    except Exception:
        return []


# ── gatherers (all fail-safe) ─────────────────────────────────────


def gather_revenue_due() -> int:
    try:
        d = json.loads(REVENUE.read_text())
        outs = d.get("outcomes", d if isinstance(d, list) else [])
        pending = [o for o in outs if o.get("outcome_type") == "pending"]
        today = _today()
        return sum(1 for o in pending if o.get("check_in_date") and o["check_in_date"] <= today)
    except Exception:
        return 0


def gather_outer_loop() -> dict:
    """Deterministic revenue-loop signal for the '💰 Outer Loop' brief
    section. Every field defaults safe; a broken/missing revenue-outcomes.json
    or a failing pipeline subprocess degrades this to an empty dict — the
    section is diagnostic, never a gate (Compass-not-Cage)."""
    result = {"due_count": 0, "oldest_due": "", "lifetime_revenue": 0.0, "never_logged": None}
    try:
        d = json.loads(REVENUE.read_text())
        outs = d.get("outcomes", d if isinstance(d, list) else [])
        pending = [o for o in outs if o.get("outcome_type") == "pending"]
        today = _today()
        due = sorted(
            [o for o in pending if o.get("check_in_date") and o["check_in_date"] <= today],
            key=lambda o: o.get("check_in_date", ""),
        )
        result["due_count"] = len(due)
        if due:
            result["oldest_due"] = due[0].get("check_in_date", "")
        result["lifetime_revenue"] = d.get("total_revenue", 0.0)
    except Exception:
        pass
    try:
        out = subprocess.run(
            [sys.executable, "execution/revenue_tracker.py", "pipeline"],
            capture_output=True, text=True, timeout=20, cwd=REPO_ROOT,
        ).stdout
        m = re.search(r"(\d+) deliverables? need outcome tracking", out)
        if m:
            result["never_logged"] = int(m.group(1))
    except Exception:
        pass
    return result


def render_outer_loop(loop: dict) -> list:
    """≤6-line brief section. Silent no-op (empty list) if there's nothing
    to say — never pad the brief with zeros to look busy."""
    if not loop.get("due_count") and not loop.get("never_logged") and not loop.get("lifetime_revenue"):
        return []
    lines = ["", "## \U0001f4b0 Outer Loop"]
    if loop.get("due_count"):
        oldest = f" (oldest: {loop['oldest_due']})" if loop.get("oldest_due") else ""
        lines.append(f"- {loop['due_count']} outcome check-in{'s' if loop['due_count'] != 1 else ''} overdue{oldest}")
    if loop.get("never_logged"):
        lines.append(f"- {loop['never_logged']} deliverable{'s' if loop['never_logged'] != 1 else ''} shipped, never logged")
    lines.append(f"- Lifetime revenue collected: ${loop.get('lifetime_revenue', 0):,.2f}")
    lines.append("- `python3 execution/revenue_tracker.py checkin` — walks the due list one by one")
    return lines


def gather_threads(limit: int = 3) -> list:
    try:
        out = subprocess.run(
            [sys.executable, str(HANDOFF_STORE), "threads"],
            capture_output=True, text=True, timeout=20, cwd=REPO_ROOT,
        ).stdout
        threads = []
        for line in out.splitlines():
            parts = line.split()
            if len(parts) >= 2:
                threads.append(f"{parts[0]} ({parts[1]})")
            if len(threads) >= limit:
                break
        return threads
    except Exception:
        return []


def goals_due(goals: list) -> list:
    return [g for g in goals
            if _days_since(g.get("last_reviewed", "")) >= g.get("review_cadence_days", 7)]


def life_staleness() -> list:
    """[(section, days_stale)] sorted stalest-first. 'never' -> NEVER_DAYS."""
    try:
        text = LIFE_PATH.read_text()
    except Exception:
        return []
    sections = []
    for m in re.finditer(r"^## (.+?)\s*\n<!-- updated: (\S+) -->", text, re.MULTILINE):
        sections.append((m.group(1).strip(), _days_since(m.group(2))))
    sections.sort(key=lambda s: s[1], reverse=True)
    return sections


def open_loops() -> list:
    """Open loops from the most recent journal entry before today."""
    try:
        entries = sorted(JOURNAL.glob("*.md"), reverse=True)
        for entry in entries:
            if entry.stem >= _today():
                continue
            text = entry.read_text()
            m = re.search(r"^## Open loops\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
            if m:
                loops = [l.strip("- ").strip() for l in m.group(1).splitlines()
                         if l.strip().startswith("- ")]
                return [l for l in loops if l][:3]
            return []
    except Exception:
        pass
    return []


# ── question generation ───────────────────────────────────────────


def _yesterday_brief_text() -> str:
    try:
        y = (datetime.now().date() - timedelta(days=1)).isoformat()
        return (BRIEFS / f"{y}.md").read_text()
    except Exception:
        return ""


def generate_questions(staleness, due_goals, loops, weekly_due, today) -> list:
    questions = []
    if loops:
        loop = _stable_pick(loops, today, "loop")
        questions.append(f'Yesterday you flagged: "{loop}" — did it move, or does it die?')
    onboarded = any(days < NEVER_DAYS for _, days in staleness)
    # Sections asked yesterday go to the back of the line (still stale = still
    # eligible, but the rotation breathes instead of nagging the same topic).
    ytext = _yesterday_brief_text()
    if ytext:
        asked_yday = {s for s, _ in staleness
                      if any(q in ytext for q in LIFE_QUESTIONS.get(s, []))}
        staleness = ([x for x in staleness if x[0] not in asked_yday]
                     + [x for x in staleness if x[0] in asked_yday])
    for section, days in staleness:
        if len(questions) >= 3:
            break
        bank = LIFE_QUESTIONS.get(section)
        if not bank:
            continue
        # Pre-onboarding everything is 'never'-stale; still ask, that IS the onboarding.
        if days >= 2 or not onboarded:
            questions.append(_stable_pick(bank, today, section))
    if len(questions) < 3 and due_goals:
        g = due_goals[0]
        days = _days_since(g.get("last_reviewed", ""))
        ago = "never been reviewed" if days >= NEVER_DAYS else f"not been reviewed in {days}d"
        questions.append(f'Goal "{g["id"]}" has {ago} — still the target, or renegotiate?')
    if len(questions) < 3 and weekly_due:
        questions.append("Board sits today — what's the one thing you don't want to say out loud to it?")
    while len(questions) < 3:
        questions.append(_stable_pick(LIFE_QUESTIONS["Mindset"], today, f"filler{len(questions)}"))
    return questions[:3]


# ── brief rendering ───────────────────────────────────────────────


def render_brief(state, goals, due_goals, revenue_due, threads, loops, questions, weekly_line,
                 outer_loop=None) -> str:
    today = _today()
    weekday = datetime.now().strftime("%A")
    lines = [f"# Morning Brief — {today} ({weekday})", ""]
    streak = state.get("streak", 0)
    lines.append(f"**Streak:** {streak} · **Board:** {weekly_line}")
    if goals:
        lines.append("")
        lines.append("## Goal pulse")
        due_ids = {g["id"] for g in due_goals}
        for g in goals:
            flag = "🔍 review due" if g["id"] in due_ids else "on track"
            lines.append(f"- {g['id']} — {flag}")
    deck = []
    if revenue_due:
        deck.append(f"{revenue_due} outcome check-in{'s' if revenue_due != 1 else ''} due "
                    f"(`python3 execution/revenue_tracker.py due`)")
    if threads:
        deck.append("Top threads: " + ", ".join(threads))
    if deck:
        lines.append("")
        lines.append("## On deck")
        lines.extend(f"- {d}" for d in deck)
    if loops:
        lines.append("")
        lines.append("## Yesterday's open loops")
        lines.extend(f"- {l}" for l in loops)
    if outer_loop:
        lines.extend(render_outer_loop(outer_loop))
    lines.append("")
    lines.append("## Your three questions")
    lines.extend(f"{i}. {q}" for i, q in enumerate(questions, 1))
    return "\n".join(lines) + "\n"


def compose_nudge(state, questions, revenue_due, weekly_due, weekly_overdue) -> str:
    gap = _days_since(state.get("last_daily", ""))
    if state.get("last_daily") and REENTRY_GAP_DAYS < gap < NEVER_DAYS:
        line = f"COS: been {gap}d since your last check-in — 90 seconds to reset? Run /cos"
    else:
        due_part = f", {revenue_due} check-ins due" if revenue_due else ""
        line = f"COS: morning brief ready ({len(questions)} questions{due_part}) — run /cos (~2 min)"
    if weekly_due:
        overdue_part = f" ({weekly_overdue}d overdue)" if weekly_overdue > 0 else ""
        line += f"; board session due{overdue_part} — /cos weekly (~15 min)"
    return line


# ── commands ──────────────────────────────────────────────────────


def weekly_status(state):
    days = _days_since(state.get("last_weekly", ""))
    due = days >= WEEKLY_EVERY_DAYS
    overdue = max(0, days - WEEKLY_EVERY_DAYS) if days < NEVER_DAYS else 0
    return due, overdue


def cmd_prep(force: bool, dry_run: bool) -> int:
    for d in (COS, BRIEFS, JOURNAL):
        d.mkdir(parents=True, exist_ok=True)
    today = _today()
    state = load_state()
    brief_path = BRIEFS / f"{today}.md"

    if brief_path.exists() and not force and not dry_run:
        if state.get("nudge_date") != today:
            state["nudge_date"] = today
            save_state(state)
        print(f"Brief already exists: {brief_path} (use --force to regenerate)")
        return 0

    goals = load_goals()
    due_goals = goals_due(goals)
    revenue_due = gather_revenue_due()
    threads = gather_threads()
    loops = open_loops()
    weekly_due, weekly_overdue = weekly_status(state)
    if weekly_due:
        weekly_line = f"{weekly_overdue}d overdue" if weekly_overdue > 0 else "due today"
    else:
        next_in = WEEKLY_EVERY_DAYS - _days_since(state.get("last_weekly", ""))
        weekly_line = f"in {next_in}d"
    questions = generate_questions(life_staleness(), due_goals, loops, weekly_due, today)
    outer_loop = gather_outer_loop()
    brief = render_brief(state, goals, due_goals, revenue_due, threads, loops,
                         questions, weekly_line, outer_loop)

    if dry_run:
        print(brief)
        return 0

    brief_path.write_text(brief)
    state["nudge_line"] = compose_nudge(state, questions, revenue_due, weekly_due, weekly_overdue)
    state["nudge_date"] = today
    state["last_prep"] = datetime.now().isoformat(timespec="seconds")
    save_state(state)
    print(f"Brief written: {brief_path}")
    return 0


def cmd_nudge() -> int:
    state = load_state()
    today = _today()
    if state.get("nudge_date") == today and state.get("last_daily") != today:
        print(state.get("nudge_line", ""))
    return 0


def cmd_capture(text: str, route: str) -> int:
    JOURNAL.mkdir(parents=True, exist_ok=True)
    today = _today()
    stamp = datetime.now().strftime("%H:%M")
    jpath = JOURNAL / f"{today}.md"
    if not jpath.exists():
        jpath.write_text(f"# Journal — {today}\n\n## Captured\n")
    content = jpath.read_text()
    if "## Captured" not in content:
        content += "\n## Captured\n"
    content += f"- [{stamp}] {text}\n"
    jpath.write_text(content)
    if route == "inbox":
        # 2026-07-06: delegates to thought_bank.py — the single deterministic
        # writer of the thought-bank inbox (timestamped ## headers + sovereign
        # mirror for weekly distill). Was a second, differently-formatted
        # writer of the same file; this collapses it to one format, one path.
        try:
            sys.path.insert(0, str(REPO_ROOT / "execution"))
            from thought_bank import capture as tb_capture  # noqa: E402
            result = tb_capture(text, source="cos", silent=True)
            if result.get("skipped"):
                print(f"Captured to journal: {jpath.name} (thought-bank: duplicate, skipped)")
            else:
                print(f"Captured to journal: {jpath.name} + thought-bank inbox: "
                      f"{Path(result['file']).name}")
        except Exception as e:
            # thought_bank.py unavailable — journal write above already succeeded;
            # fail loud but don't lose the journal capture.
            print(f"Captured to journal: {jpath.name} (thought-bank mirror FAILED: {e})")
    else:
        print(f"Captured to journal: {jpath.name}")
    return 0


def cmd_mark(kind: str) -> int:
    state = load_state()
    today = _today()
    if kind == "daily":
        if state.get("last_daily") != today:
            yesterday = (datetime.now().date() - timedelta(days=1)).isoformat()
            state["streak"] = state.get("streak", 0) + 1 if state.get("last_daily") == yesterday else 1
            state["last_daily"] = today
        state["nudge_line"] = ""
    elif kind == "weekly":
        state["last_weekly"] = today
    save_state(state)
    print(f"Marked {kind} done for {today} (streak: {state['streak']})")
    return 0


def cmd_status() -> int:
    state = load_state()
    today = _today()
    brief_path = BRIEFS / f"{today}.md"
    weekly_due, weekly_overdue = weekly_status(state)
    staleness = life_staleness()
    first_run = bool(staleness) and all(days >= NEVER_DAYS for _, days in staleness)
    print(json.dumps({
        "today": today,
        "brief_path": str(brief_path),
        "brief_exists": brief_path.exists(),
        "daily_done": state.get("last_daily") == today,
        "weekly_due": weekly_due,
        "weekly_overdue_days": weekly_overdue,
        "streak": state.get("streak", 0),
        "first_run": first_run,
        "goals_active": len(load_goals()),
        "revenue_check_ins_due": gather_revenue_due(),
        "last_prep": state.get("last_prep", ""),
    }, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_prep = sub.add_parser("prep", help="build today's brief + nudge")
    p_prep.add_argument("--force", action="store_true")
    p_prep.add_argument("--dry-run", action="store_true")
    sub.add_parser("nudge", help="print current nudge line")
    p_cap = sub.add_parser("capture", help="append capture to journal (+ inbox mirror)")
    p_cap.add_argument("--text", required=True)
    p_cap.add_argument("--route", choices=["journal", "inbox"], default="journal")
    p_mark = sub.add_parser("mark", help="record daily/weekly completion")
    p_mark.add_argument("kind", choices=["daily", "weekly"])
    sub.add_parser("status", help="JSON state for workflow routing")
    args = parser.parse_args()

    if args.cmd == "prep":
        return cmd_prep(args.force, args.dry_run)
    if args.cmd == "nudge":
        return cmd_nudge()
    if args.cmd == "capture":
        return cmd_capture(args.text, args.route)
    if args.cmd == "mark":
        return cmd_mark(args.kind)
    if args.cmd == "status":
        return cmd_status()
    return 1


if __name__ == "__main__":
    sys.exit(main())
