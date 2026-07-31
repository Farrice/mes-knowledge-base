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

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cos_reminders import render_reminders  # noqa: E402  (dated tickler, stdlib-only)

REPO_ROOT = Path(__file__).resolve().parents[1]
COS = REPO_ROOT / ".agent" / "cos"
BRIEFS = COS / "briefs"
JOURNAL = COS / "journal"
WORLD = COS / "world"
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
            # Actual items, not just a count (Farrice 2026-07-14): a due list
            # he can't see is a due list he can't close.
            result["due_items"] = [
                {"deliverable": o.get("deliverable", ""),
                 "check_in_date": o.get("check_in_date", "")}
                for o in due[:5]
            ]
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
    for item in loop.get("due_items", []):
        name = item.get("deliverable", "")
        short = name if len(name) <= 60 else name[:57] + "…"
        lines.append(
            f"  - [{item.get('check_in_date', '')}] {short}\n"
            f"    ↳ close: `python3 execution/revenue_tracker.py log \"{name}\" "
            f"--revenue <$> --outcome \"<what happened, or 'dead: reason'>\"`")
    if loop.get("never_logged"):
        lines.append(f"- {loop['never_logged']} deliverable{'s' if loop['never_logged'] != 1 else ''} shipped, never logged")
    lines.append(f"- Lifetime revenue collected: ${loop.get('lifetime_revenue', 0):,.2f}")
    lines.append("- Data: [revenue-outcomes.json](.agent/revenue-outcomes.json) · "
                 "`python3 execution/revenue_tracker.py checkin` walks the due list one by one")
    # Outcome-chase drafts (2026-07-21 ladder-audit build): link, never a task.
    try:
        chases = sorted(COS.glob("outcome-chase-*.md"),
                        key=lambda p: p.stat().st_mtime, reverse=True)
        if chases and (datetime.now().timestamp() - chases[0].stat().st_mtime) < 7 * 86400:
            lines.append(f"- Drafted check-ins ready for review: [{chases[0].name}](.agent/cos/{chases[0].name})")
    except Exception:
        pass
    return lines


def gather_system_vitals() -> dict:
    """System-health signal for the '🩺 System Vitals' brief section. Reads the
    pre-computed .agent/health/latest.json written by health_metrics.py
    (launchd com.antigravity.health-metrics, daily 06:15 — 30 min before this
    runs). Missing/broken snapshot degrades to a staleness warning rather than
    an empty dict — a DEAD health collector is itself the #1 health finding
    (the guard lives in the consumer so it fires even when the collector
    can't). Diagnostic, never a gate (Compass-not-Cage)."""
    latest = REPO_ROOT / ".agent" / "health" / "latest.json"
    try:
        m = json.loads(latest.read_text())
        age_h = (datetime.now() - datetime.fromisoformat(m["ts"])).total_seconds() / 3600
        if age_h > 48:
            return {"dead_collector_days": round(age_h / 24, 1)}
        ci = m.get("context_injection", {})
        return {
            "date": m.get("date", "?"),
            "deep": bool(m.get("deep")),
            "flags": m.get("flags", []),
            "pending": m.get("pending_review", {}).get("pending", 0),
            "ctx_kb": round(ci.get("total_bytes", 0) / 1e3),
            "tmp_mb": round(m.get("tmp", {}).get("bytes", 0) / 1e6),
            "skills": m.get("assets", {}).get("skills", 0),
            "deep_path": f".agent/health/{m.get('date')}-deep.json" if m.get("deep") else "",
        }
    except Exception:
        return {"dead_collector_days": -1}


def render_system_vitals(vitals: dict) -> list:
    """≤8-line brief section. Green day = one line. Flag day = one line per
    flag (each already carries its tradeoff). Never renders empty-but-padded;
    never blocks anything."""
    if not vitals:
        return []
    lines = ["", "## 🩺 System Vitals"]
    dead = vitals.get("dead_collector_days")
    if dead is not None:
        since = "has never run" if dead == -1 else f"hasn't run in {dead}d"
        lines.append(f"- ⚠️ health collector {since} — check `launchctl list "
                     f"com.antigravity.health-metrics`; a dark health loop hides every other problem")
        return lines
    if not vitals.get("flags") and not vitals.get("pending"):
        lines.append(f"- ✅ all green — ctx {vitals['ctx_kb']}KB · .tmp {vitals['tmp_mb']}MB · "
                     f"{vitals['skills']} skills · 0 pending removals "
                     f"([latest.json](.agent/health/latest.json))")
        return lines
    for fl in vitals.get("flags", [])[:6]:
        lines.append(f"- ⚑ {fl}")
    if vitals.get("pending"):
        lines.append(f"- 🗂 {vitals['pending']} removal proposal(s) awaiting your yes — "
                     f"[pending-review.md](.agent/health/pending-review.md); nothing moves without it")
    if vitals.get("deep_path"):
        lines.append(f"- Sunday deep report: [{vitals['deep_path']}]({vitals['deep_path']})")
    return lines


def gather_self_heal() -> dict:
    """Self-heal signal for the '🔧 Self-Heal' brief section (Farrice 2026-07-27).

    "What good does it do that we're logging these things if they don't get
    fixed and healed and corrected?" — so the daily `cos_prep.py prep` run
    APPLIES the auto-fixes, and the brief reports only what genuinely needed
    a human. A green day renders one line; a clean day renders nothing.

    Read-only here (`report`); the healing happens in prep(). Degrades to a
    warning rather than silence — a dead healer is itself a finding.

    Reads the CACHE at .agent/health/self-heal-latest.json, written by the
    `heal` run in prep(). It must never scan inline: a live scan runs
    verify_system.py plus verify_born_intent_drift.py over 6,596 anchors and
    pushed this brief past 120s the first time it was wired that way.
    """
    health = REPO_ROOT / ".agent" / "health"
    # Prefer the fresh observation (report cache); fall back to the heal record.
    # These are separate files on purpose — a report must never overwrite the
    # record of what was actually repaired (D1, 2026-07-27).
    rows, ts = None, None
    for p in (health / "self-heal-report.json", health / "self-heal-latest.json"):
        try:
            d = json.loads(p.read_text())
        except Exception:
            continue
        if ts is None or str(d.get("ts", "")) > ts:
            rows, ts = d.get("rows") or [], str(d.get("ts", ""))
    if rows is None or not ts:
        return {"dead": True}
    try:
        age_h = (datetime.now() - datetime.fromisoformat(ts)).total_seconds() / 3600
        if age_h > 48:
            return {"dead": True, "stale_h": round(age_h)}
    except ValueError:
        return {"dead": True}
    judgment = [x for x in rows if x.get("cls") == "JUDGMENT"]
    fixable = [x for x in rows if x.get("cls") != "JUDGMENT"]
    healed_today = 0
    try:
        today = _today()
        with (REPO_ROOT / ".agent" / "health" / "self-heal.jsonl").open() as f:
            healed_today = sum(1 for ln in f
                               if today in ln and '"action": "healed"' in ln)
    except OSError:
        pass
    return {"judgment": judgment, "fixable": fixable, "healed_today": healed_today}


def render_self_heal(sh: dict) -> list:
    """<=6 lines. Auto-healed items are COUNTED, never itemised — the whole
    point is that they stopped needing his attention."""
    if not sh:
        return []
    lines = ["", "## 🔧 Self-Heal"]
    if sh.get("dead"):
        age = sh.get("stale_h")
        why = f"last ran {age}h ago" if age else "has never run"
        lines.append(f"- ⚠️ self-heal {why} — `python3 execution/self_heal.py heal`; "
                     "a dead healer silently stops healing")
        return lines
    n_healed, judgment = sh.get("healed_today", 0), sh.get("judgment") or []
    if n_healed:
        lines.append(f"- ✅ {n_healed} issue(s) auto-repaired today, no action needed "
                     f"([log](.agent/health/self-heal.jsonl))")
    if sh.get("fixable"):
        lines.append(f"- 🔧 {len(sh['fixable'])} fixable but unapplied — "
                     f"`python3 execution/self_heal.py heal`")
    if not judgment:
        if not n_healed and not sh.get("fixable"):
            lines.append("- ✅ nothing to heal, nothing waiting on you")
        return lines
    lines.append(f"- 🧠 {len(judgment)} need your judgment (never auto-healed):")
    for j in judgment[:4]:
        lines.append(f"  - **{j.get('id')}** — {str(j.get('what', ''))[:150]}")
    if len(judgment) > 4:
        lines.append(f"  - +{len(judgment) - 4} more — `python3 execution/self_heal.py report`")
    return lines


def gather_memory_review() -> dict:
    """Pending distilled-rule signal for the '🧠 Memory Review' brief section
    (loop-repair #7, 2026-07-24 — pull-surface half only; auto-approval stays
    NO, Farrice's taste is the filter). Reads flagged_review in the sovereign
    DB read-only; any failure degrades to empty dict — diagnostic, never a
    gate."""
    result = {}
    try:
        import sqlite3
        db = REPO_ROOT / ".memory" / "sovereign.db"
        if not db.exists():
            return result
        conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT id, judge_score, created_at, proposed_content FROM flagged_review "
            "WHERE status = 'pending' ORDER BY judge_score DESC LIMIT 50"
        ).fetchall()
        # Act-then-veto lane (Farrice 2026-07-24): surface auto-promotions so
        # every provisional rule gets seen for veto/bless.
        prov = conn.execute(
            "SELECT id, judge_score, proposed_content FROM flagged_review "
            "WHERE status = 'approved' AND proposed_content LIKE '[PROVISIONAL%' "
            "ORDER BY reviewed_at DESC LIMIT 5"
        ).fetchall()
        conn.close()
        if not rows and not prov:
            return result
        result["provisional"] = [
            {"id": p["id"], "score": p["judge_score"],
             "line": (p["proposed_content"] or "").split("]\n")[-1].split("**Why:**")[0].split(". ")[0].strip()[:120]}
            for p in prov
        ]
        top3 = []
        for r in rows[:3]:
            # Layman rendering: first sentence only, boilerplate stripped
            # (Farrice 2026-07-24: review from the brief, not the database).
            body = (r["proposed_content"] or "").strip()
            first = body.split("**Why:**")[0].split(".\n")[0].split(". ")[0].strip().rstrip(".")
            top3.append({"id": r["id"], "score": r["judge_score"], "line": first[:140]})
        result["count"] = len(rows)
        result["oldest"] = (min(r["created_at"] or "" for r in rows)[:10] if rows else "")
        result["top3"] = top3
    except Exception:
        pass
    return result


def render_memory_review(mem: dict) -> list:
    """≤7-line brief section; silent no-op when the queue is empty. Each rule
    is a plain one-liner with its approve/reject commands prefilled — the
    review should cost ~60 seconds from the brief itself."""
    if not mem:
        return []
    lines = ["", "## 🧠 Memory Review"]
    if mem.get("count"):
        lines.append(f"- {mem['count']} distilled rule{'s' if mem['count'] != 1 else ''} "
                     f"pending (oldest {mem.get('oldest', '?')}). Gut call per line — "
                     "agree = approve, off = reject:")
        for t in mem.get("top3", []):
            lines.append(f"  - ({t['score']}) \"{t['line']}\" → "
                         f"`python3 execution/memory_review.py approve {t['id']}` / `... reject {t['id']}`")
        if mem["count"] > len(mem.get("top3", [])):
            lines.append(f"  - +{mem['count'] - len(mem['top3'])} more: `python3 execution/memory_review.py list`")
    for p in mem.get("provisional", []):
        lines.append(f"  - ⚡ AUTO-ACTIVATED (provisional, {p['score']}): \"{p['line']}\" → "
                     f"`python3 execution/memory_review.py bless {p['id']}` / `... veto {p['id']}`")
    return lines


def gather_evolution() -> dict:
    """Nightly evolution-report signal for the '\U0001f9ec Evolution' brief
    section. Reads the newest evolution_store/traces/daily_evolution_*.md,
    cheap string-matched headlines (no fancy parsing). Missing/broken reports
    degrade to an empty dict — the section is diagnostic, never a gate
    (Compass-not-Cage). cos_prep runs at 06:45, before the 07:00 evolution
    run, so this usually surfaces yesterday's report — that's expected."""
    result = {}
    try:
        traces_dir = REPO_ROOT / "evolution_store" / "traces"
        reports = sorted(traces_dir.glob("daily_evolution_*.md"))
        if not reports:
            return result
        latest = reports[-1]
        m = re.search(r"daily_evolution_(\d{4}-\d{2}-\d{2})\.md$", latest.name)
        date_str = m.group(1) if m else "?"
        hours_stale = (datetime.now().timestamp() - latest.stat().st_mtime) / 3600
        stale = hours_stale > 48
        days_stale = _days_since(date_str) if date_str != "?" else NEVER_DAYS
        text = latest.read_text()

        headlines = []
        pm = re.search(r"## Phase 2 Queue.*?\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
        if pm:
            queue_lines = [l for l in pm.group(1).splitlines()
                          if l.strip().startswith("- ") and "(none)" not in l]
            if queue_lines:
                n = len(queue_lines)
                headlines.append(f"{n} skill{'s' if n != 1 else ''} flagged for Phase 2 human review")
        rm = re.search(r"## Routing Learning.*?\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
        if rm:
            nudge_lines = [l.strip("- ").strip() for l in rm.group(1).splitlines()
                          if l.strip().startswith("- ")]
            if nudge_lines:
                n = len(nudge_lines)
                headlines.append(f"Routing learning: {n} weight nudge{'s' if n != 1 else ''} (e.g. {nudge_lines[0]})")
        if len(headlines) < 2:
            dm = re.search(r"## Platform Constitution Drift\n(.*?)(?=\n## |\Z)", text, re.DOTALL)
            if dm:
                drift_lines = [l for l in dm.group(1).splitlines()
                              if l.strip().startswith("- ") and "(clean)" not in l]
                if drift_lines:
                    n = len(drift_lines)
                    headlines.append(f"{n} constitution file{'s' if n != 1 else ''} drifted since last bless")

        result = {
            "date": date_str,
            "path": str(latest.relative_to(REPO_ROOT)),
            "stale": stale,
            "days_stale": days_stale,
            "headlines": headlines[:2],
        }
    except Exception:
        pass
    return result


def render_evolution(evo: dict) -> list:
    """≤5-line brief section pointing to the latest nightly evolution
    report. Silent no-op (empty list) if no reports exist yet — mirrors
    render_outer_loop's silent-empty behavior."""
    if not evo:
        return []
    lines = ["", f"## \U0001f9ec Evolution (latest: {evo.get('date', '?')})"]
    if evo.get("stale"):
        days = evo.get("days_stale", "?")
        lines.append(f"- ⚠️ NO REPORT IN {days} DAYS — evolution loop may be dark; "
                     f"run: python3 execution/evolution_orchestrator.py auto")
    else:
        headlines = evo.get("headlines", [])
        if headlines:
            lines.extend(f"- {h}" for h in headlines)
        else:
            lines.append("- clean run, no flags")
    path = evo.get("path", "")
    lines.append(f"- Full report: [{path}]({path}) — FYI only; nothing to do unless a ⚠️ shows")
    return lines


def render_world_pulse(pulse: dict) -> list:
    """≤8-line brief section for world pulse (top 5 items: headline + one-line
    why + source). Silent no-op (empty list) if the pulse never ran — but when
    a pulse file EXISTS and zero items cleared the recency bar, say so honestly
    (Farrice 2026-07-14: never pad, never silently omit what was attempted)."""
    items = (pulse or {}).get("items", [])
    if not items:
        if (pulse or {}).get("none_cleared"):
            lines = ["", "## 🌍 World pulse — nothing cleared the bar today",
                     "- Items were found but none passed the recency bar "
                     "(≤14 days, current-year) — stale pulse is noise, not signal."]
            if pulse.get("path"):
                lines.append(f"- Raw (ungated): [{pulse['path']}]({pulse['path']})")
            return lines
        return []
    lines = ["", "## 🌍 World pulse"]
    for item in items[:5]:
        title = item.get("title", "")
        why = f" — {item['why']}" if item.get("why") else ""
        lines.append(f"- **{title}**{why} ({item.get('url', '')})")
    if pulse.get("path"):
        lines.append(f"- Full pulse: [{pulse['path']}]({pulse['path']})")
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


def open_loops() -> tuple:
    """(loops, source_relpath) from the most recent journal entry before today.
    The source path rides along so the brief can show WHERE each loop came
    from — a loop without provenance reads as invented (Farrice, 2026-07-08)."""
    try:
        entries = sorted(JOURNAL.glob("*.md"), reverse=True)
        for entry in entries:
            if entry.stem >= _today():
                continue
            text = entry.read_text()
            src = str(entry.relative_to(REPO_ROOT))
            m = re.search(r"^## Open loops\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL)
            if m:
                loops = [l.strip("- ").strip() for l in m.group(1).splitlines()
                         if l.strip().startswith("- ")]
                return [l for l in loops if l][:3], src
            return [], src
    except Exception:
        pass
    return [], ""


def ensure_world_pulse() -> None:
    """If today's world file is missing, try to generate it via world_pulse_research.py
    (deep_research_engine: Gemini + Perplexity, cost-gated, honest-receipt research).
    Fallback to world_brief.py (Tavily floor, $0) if unavailable. Wrapped so ANY
    failure (missing script, no network, timeout) degrades gracefully: the
    brief simply renders without the section."""
    try:
        if (WORLD / f"{_today()}.md").exists():
            return
        # Try primary research loop (deep_research_engine + Gemini/Perplexity)
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "execution" / "world_pulse_research.py"), "run"],
            capture_output=True, text=True, timeout=240, cwd=REPO_ROOT,
        )
        if result.returncode == 0:
            return
        # Fallback to Tavily floor if primary unavailable
        subprocess.run(
            [sys.executable, str(REPO_ROOT / "execution" / "world_brief.py"), "generate"],
            capture_output=True, text=True, timeout=240, cwd=REPO_ROOT,
        )
    except Exception:
        pass


def gather_world_pulse() -> dict:
    """World-pulse for the brief: {"items": [{title, why, url}], "path": str}.
    Reads today's world file, falling back to yesterday's. Missing files and
    DEGRADED files yield {} — the section is diagnostic, never a gate, and an
    item without a real http(s) source never reaches the brief."""
    try:
        candidates = [WORLD / f"{_today()}.md",
                      WORLD / f"{(datetime.now().date() - timedelta(days=1)).isoformat()}.md"]
        pulse_file = next((p for p in candidates if p.exists()), None)
        if pulse_file is None:
            return {}
        text = pulse_file.read_text()
        status_m = re.search(r"^status: (.+)$", text, re.MULTILINE)
        if status_m and status_m.group(1).strip().startswith("DEGRADED"):
            return {}
        items = []
        rejected_stale = 0
        for m in re.finditer(r"^## \d+\. (.+?)$", text, re.MULTILINE):
            title = m.group(1).strip()
            start = m.end()
            next_match = re.search(r"^## ", text[start:], re.MULTILINE)
            end = start + next_match.start() if next_match else len(text)
            block = text[start:end]
            src_match = re.search(r"\*\*Sources?:\*\* .*?(https?://[^\s)]+)", block)
            if not src_match:
                continue  # unsourced item never reaches the brief
            why_match = re.search(r"\*\*Why it matters:\*\* (.+?)(?:\n|$)", block)
            what_match = re.search(r"\*\*What happened:\*\* (.+?)(?:\n|$)", block)
            item = {
                "title": title,
                "why": why_match.group(1).strip() if why_match else "",
                "what": what_match.group(1).strip() if what_match else "",
                "url": src_match.group(1).strip().rstrip(".,;"),
            }
            if _pulse_item_stale(item):
                rejected_stale += 1
                continue  # recency bar (Farrice 2026-07-14): stale pulse = noise
            items.append(item)
        path = str(pulse_file.relative_to(REPO_ROOT))
        if not items:
            if rejected_stale:
                return {"items": [], "path": path, "none_cleared": True}
            return {}
        return {"items": items[:8], "path": path}
    except Exception:
        return {}


# Domains trusted enough to carry a dated-but-older item when it also touches
# an active goal (the ONLY exception to the recency bar). Tune freely.
CREDIBLE_PULSE_DOMAINS = (
    "anthropic.com", "claude.com", "openai.com", "support.claude.com",
    "linkedin.com", "substack.com",
)


def _pulse_item_stale(item: dict) -> bool:
    """Recency bar (Farrice 2026-07-14): a pulse item must read CURRENT —
    published within ~2 weeks, current-year. Deterministic heuristics only:
    - any pre-current-year token (2010-2025) in title/what/url with no
      current-year token alongside → stale
    - a detectable full date older than 14 days → stale
    - no date signal at all → passes (upstream engines already filter to 14d)
    Exception: credible domain AND the item text touches an active goal id."""
    current_year = int(_today()[:4])
    text = " ".join([item.get("title", ""), item.get("what", ""),
                     item.get("why", ""), item.get("url", "")])
    years = {int(y) for y in re.findall(r"\b(20[12]\d)\b", text)}
    stale = False
    if years and max(years) < current_year:
        stale = True
    # Explicit ISO or "Month D, YYYY" dates older than 14 days
    dates = []
    for iso in re.findall(r"\b(\d{4}-\d{2}-\d{2})\b", text):
        dates.append(iso)
    for mon, day, year in re.findall(
            r"\b(January|February|March|April|May|June|July|August|September|"
            r"October|November|December)\s+(\d{1,2}),\s*(\d{4})\b", text):
        try:
            dates.append(datetime.strptime(f"{mon} {day} {year}", "%B %d %Y")
                         .date().isoformat())
        except ValueError:
            pass
    if dates:
        newest = max(dates)
        cutoff = (datetime.now().date() - timedelta(days=14)).isoformat()
        if newest < cutoff:
            stale = True
    if not stale:
        return False
    # Exception path: credible source AND goal-relevant (both required)
    url = item.get("url", "")
    if any(dom in url for dom in CREDIBLE_PULSE_DOMAINS):
        try:
            goal_ids = [g.get("id", "") for g in load_goals()]
            low = text.lower()
            if any(gid and gid.replace("-", " ") in low.replace("-", " ")
                   for gid in goal_ids):
                return False
        except Exception:
            pass
    return True


# ── question generation (v2: thread-connecting, archetype rotation) ───────────────────────────────────────────


def _yesterday_brief_text() -> str:
    try:
        y = (datetime.now().date() - timedelta(days=1)).isoformat()
        return (BRIEFS / f"{y}.md").read_text()
    except Exception:
        return ""


def _prior_questions() -> set:
    """Exact question texts asked in yesterday's brief — never repeated today."""
    m = re.search(r"^## Your .*questions\n(.*)", _yesterday_brief_text(),
                  re.MULTILINE | re.DOTALL)
    qs = set()
    if m:
        for line in m.group(1).splitlines():
            lm = re.match(r"^\d+\.\s+(.+)$", line.strip())
            if lm:
                qs.add(lm.group(1).strip())
    return qs


def _pick_fresh(options: list, avoid: set, *seed_parts: str) -> str:
    """Stable-hashed pick that skips anything in `avoid` (yesterday's questions
    + today's already-chosen ones). Returns "" when every option is stale."""
    if not options:
        return ""
    digest = int(hashlib.md5("|".join(seed_parts).encode()).hexdigest(), 16)
    for i in range(len(options)):
        cand = options[(digest + i) % len(options)]
        if cand and cand not in avoid:
            return cand
    return ""


def _clip(text: str, limit: int = 70) -> str:
    text = re.sub(r"\s+", " ", str(text)).strip()
    return text[: limit - 1] + "…" if len(text) > limit else text


def generate_questions_v2(today: str, staleness: list, due_goals: list, loops: list,
                          weekly_due: bool, threads: list, world_items: list,
                          loops_src: str = "", world_path: str = "") -> list:
    """Question engine v2 — three archetypes, one question each, every day:

      1. decision-forcing   ("X or Y — pick") anchored to an open loop, a due
                            goal, or a world-pulse item
      2. connection-surfacing  must reference TWO distinct live threads/loops
      3. life/chairman      from the stalest life-context section's bank

    Every question references something specific; none repeats yesterday's
    exact text. When inputs are thin (no loops/threads/world), each slot falls
    back to the legacy behavior via the same banks the v1 engine used.
    Only open-loop lines are quoted — journal `## Raw` content never leaks in.

    Returns a list of (question, source) tuples — every question carries a
    provenance string the brief renders under it, so Farrice never has to ask
    "where are you getting that from?" (binding feedback, 2026-07-08).
    """
    threads = threads or []
    world_items = world_items or []
    avoid = _prior_questions()
    questions: list = []

    journal_src = (f"open loop · [journal {Path(loops_src).stem}]({loops_src})"
                   if loops_src else "open loop")
    goals_src = "goal registry · [goals.json](.agent/cos/goals.json)"
    world_src = (f"world pulse · [{Path(world_path).stem}]({world_path})"
                 if world_path else "world pulse")

    # ── Archetype 1: decision-forcing ────────────────────────────
    # His own commitments (loops, due goals) outrank world items — a $-attached
    # open loop always beats an article as the thing to force a pick on.
    decision_opts, decision_anchors, decision_srcs = [], [], []
    for loop in loops:
        decision_opts.append(
            f'Open loop: "{_clip(loop, 80)}" — one concrete move on it today, or kill it and free the slot. Pick.')
        decision_anchors.append(_clip(loop, 60))
        decision_srcs.append(journal_src)
    for g in due_goals:
        decision_opts.append(
            f'Goal "{g["id"]}" review is due — recommit as-is or renegotiate the number. Pick one.')
        decision_anchors.append(g["id"])
        decision_srcs.append(goals_src)
    if not decision_opts:
        for item in world_items[:3]:
            if item.get("title"):
                decision_opts.append(
                    f'World pulse: "{_clip(item["title"], 70)}" — worth 30 focused minutes this week, or noise to ignore? Decide.')
                decision_anchors.append(_clip(item["title"], 60))
                decision_srcs.append(world_src)
    q = _pick_fresh(decision_opts, avoid, today, "decision")
    used_anchor = ""
    if q:
        questions.append((q, decision_srcs[decision_opts.index(q)]))
        avoid.add(q)
        used_anchor = decision_anchors[decision_opts.index(q)]

    # ── Archetype 2: connection-surfacing (two DISTINCT refs) ────
    # Primary pool is his live threads + open loops (the spec: TWO distinct
    # threads/loops). World items and goals only backfill when that pool is thin.
    refs = []  # (kind, text) — order matters for deterministic pairing
    refs += [("thread", _clip(t, 60)) for t in threads]
    refs += [("loop", _clip(l, 60)) for l in loops]
    if len({t for _, t in refs if t}) < 2:
        refs += [("world", _clip(item["title"], 60)) for item in world_items if item.get("title")]
        refs += [("goal", g["id"]) for g in due_goals]
    seen_txt, uniq = set(), []
    for kind, txt in refs:
        if txt and txt not in seen_txt:
            seen_txt.add(txt)
            uniq.append((kind, txt))
    # Don't re-anchor on what Q1 already forced a decision about (if the pool allows).
    if used_anchor and len([r for r in uniq if r[1] != used_anchor]) >= 2:
        uniq = [r for r in uniq if r[1] != used_anchor]
    if len(uniq) >= 2:
        digest = int(hashlib.md5(f"{today}|pair".encode()).hexdigest(), 16)
        a = uniq[digest % len(uniq)]
        rest = [r for r in uniq if r[1] != a[1]]
        b = next((r for r in rest if r[0] != a[0]), rest[0])  # prefer a different kind
        conn_opts = [t.format(a=a[1], b=b[1]) for t in (
            'Hold "{a}" against "{b}" — is there one move that advances both, or are they competing for the same hours?',
            '"{a}" and "{b}" are both live. What does the first know that the second needs?',
            'Where do "{a}" and "{b}" secretly overlap — is there a single artifact that serves both?',
        )]
        q = _pick_fresh(conn_opts, avoid, today, "connect")
        if q:
            kind_src = {"thread": "live threads · `python3 execution/handoff_store.py threads`",
                        "loop": journal_src, "world": world_src, "goal": goals_src}
            questions.append((q, f"connects {kind_src[a[0]]} × {kind_src[b[0]]}"))
            avoid.add(q)

    # ── Archetype 3: life/chairman (stalest section first) ───────
    onboarded = any(days < NEVER_DAYS for _, days in staleness)
    ytext = _yesterday_brief_text()
    ordered = staleness
    if ytext:  # sections asked yesterday go to the back of the line
        asked_yday = {s for s, _ in staleness
                      if any(qq in ytext for qq in LIFE_QUESTIONS.get(s, []))}
        ordered = ([x for x in staleness if x[0] not in asked_yday]
                   + [x for x in staleness if x[0] in asked_yday])
    used_section = ""
    for section, days in ordered:
        bank = LIFE_QUESTIONS.get(section)
        if not bank:
            continue
        if days >= 2 or not onboarded:
            q = _pick_fresh(bank, avoid, today, section)
            if q:
                stale = "never updated" if days >= NEVER_DAYS else f"{days}d since update"
                questions.append((q, f"[life-context.md § {section}](.agent/cos/life-context.md) · {stale}"))
                avoid.add(q)
                used_section = section
                break

    # ── Fallback fill (thin inputs) — legacy v1 behavior ─────────
    if len(questions) < 3 and due_goals:
        g = due_goals[0]
        days = _days_since(g.get("last_reviewed", ""))
        ago = "never been reviewed" if days >= NEVER_DAYS else f"not been reviewed in {days}d"
        q = f'Goal "{g["id"]}" has {ago} — still the target, or renegotiate?'
        if q not in avoid:
            questions.append((q, goals_src))
            avoid.add(q)
    if len(questions) < 3 and weekly_due:
        q = "Board sits today — what's the one thing you don't want to say out loud to it?"
        if q not in avoid:
            questions.append((q, "board cadence · [state.json](.agent/cos/state.json)"))
            avoid.add(q)
    fill = 0
    while len(questions) < 3 and fill < 10:
        q = _pick_fresh(LIFE_QUESTIONS["Mindset"], avoid, today, f"filler{fill}")
        fill += 1
        if q:
            questions.append((q, "[life-context.md § Mindset](.agent/cos/life-context.md) · rotation"))
            avoid.add(q)
        else:
            break
    while len(questions) < 3:  # bank fully exhausted — repeat rather than crash
        questions.append((_stable_pick(LIFE_QUESTIONS["Mindset"], today, f"exhausted{len(questions)}"),
                          "question bank · rotation"))

    # ── Optional extras 4-5 (Farrice, 2026-07-08: "I don't mind answering
    # more questions") — only when real material exists; never bank-padded
    # just to hit five. 3 stays the floor, 5 the ceiling.
    if len(questions) >= 3:
        for section, days in ordered:  # 4th: next genuinely-stale life section
            if len(questions) >= 5:
                break
            if section == used_section or days < 2:
                continue
            bank = LIFE_QUESTIONS.get(section)
            if not bank:
                continue
            q = _pick_fresh(bank, avoid, today, f"{section}|extra")
            if q:
                stale = "never updated" if days >= NEVER_DAYS else f"{days}d since update"
                questions.append((q, f"[life-context.md § {section}](.agent/cos/life-context.md) · {stale}"))
                avoid.add(q)
                break
        if len(questions) < 5:  # 5th: a world-pulse worth-it-or-noise decision
            for item in world_items[:3]:
                title = _clip(item.get("title", ""), 70)
                if not title or title == used_anchor:
                    continue
                q = (f'World pulse: "{title}" — worth 30 focused minutes '
                     f'this week, or noise to ignore? Decide.')
                if q not in avoid:
                    questions.append((q, world_src))
                    avoid.add(q)
                    break
    return questions[:5]


# ── legacy question generation (v1) — kept as the documented fallback shape ──
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


LISTENING_CUT = REPO_ROOT / "_active" / "health-performance-ip-library" / "daily" / "LATEST-EXEC-CUT.md"


def gather_listening() -> dict:
    """Angle Map Listening Engine exec cut (v4 fusion, 2026-07-31): inline the
    <=6-line daily cut when fresh (written today or yesterday by the 05:30
    listening run); silently absent otherwise — never a broken section."""
    try:
        if not LISTENING_CUT.exists():
            return {}
        age = (datetime.now() - datetime.fromtimestamp(LISTENING_CUT.stat().st_mtime)).days
        if age > 1:
            return {}
        lines = [l.rstrip() for l in LISTENING_CUT.read_text().splitlines() if l.strip()][:7]
        return {"lines": lines} if lines else {}
    except Exception:
        return {}


def render_listening(listening) -> list:
    """🎧 Industry listening — the Angle Map Listening Engine's morning cut."""
    cut = listening.get("lines") if listening else None
    if not cut:
        return []
    rel = "_active/health-performance-ip-library/daily/LATEST-EXEC-CUT.md"
    out = ["", f"## 🎧 Industry listening — [exec cut]({rel})"]
    for l in cut:
        if l.startswith("#"):
            out.append(f"- **{l.lstrip('# ').strip()}**")
        elif l.startswith("-"):
            out.append(l)
        else:
            out.append(f"- {l}")
    return out


def render_brief(state, goals, due_goals, revenue_due, threads, loops, questions, weekly_line,
                 outer_loop=None, evolution=None, world_pulse=None, loops_src="",
                 system_vitals=None, memory_review=None, self_heal=None, listening=None) -> str:
    """Self-contained brief (Farrice, 2026-07-08, binding): every section names
    its source as a clickable repo-relative link, every question carries a
    provenance line. He should never have to ask where a line came from."""
    today = _today()
    weekday = datetime.now().strftime("%A")
    lines = ["<!-- cos:v3-data-appendix — raw data bundle for the Standing Board; "
             "the session composes the Operator Primer on top of this -->",
             f"# Morning Brief — {today} ({weekday})", ""]
    streak = state.get("streak", 0)
    lines.append(f"**Streak:** {streak} · **Board:** {weekly_line}")
    if goals:
        lines.append("")
        lines.append("## Goal pulse — [goals.json](.agent/cos/goals.json)")
        due_ids = {g["id"] for g in due_goals}
        for g in goals:
            if g["id"] in due_ids:
                flag = "🔍 review due"
            else:
                days = _days_since(g.get("last_reviewed", ""))
                flag = "never reviewed" if days >= NEVER_DAYS else f"reviewed {days}d ago"
            lines.append(f"- {g['id']} — {flag}")
    deck = []
    if revenue_due:
        deck.append(f"{revenue_due} outcome check-in{'s' if revenue_due != 1 else ''} due "
                    f"(`python3 execution/revenue_tracker.py due`)")
    if threads:
        deck.append("Top threads: " + ", ".join(threads)
                    + " — from `python3 execution/handoff_store.py threads`")
    if deck:
        lines.append("")
        lines.append("## On deck")
        lines.extend(f"- {d}" for d in deck)
    if loops:
        lines.append("")
        header = "## Yesterday's open loops"
        if loops_src:
            header += f" — from [{Path(loops_src).stem}]({loops_src})"
        lines.append(header)
        lines.extend(f"- {l}" for l in loops)
    lines.extend(render_reminders())
    if listening:
        lines.extend(render_listening(listening))
    if world_pulse:
        lines.extend(render_world_pulse(world_pulse))
    if outer_loop:
        lines.extend(render_outer_loop(outer_loop))
    if evolution:
        lines.extend(render_evolution(evolution))
    if system_vitals:
        lines.extend(render_system_vitals(system_vitals))
    if self_heal:
        lines.extend(render_self_heal(self_heal))
    if memory_review:
        lines.extend(render_memory_review(memory_review))
    lines.append("")
    n_words = {3: "three", 4: "four", 5: "five"}
    lines.append(f"## Your {n_words.get(len(questions), len(questions))} questions")
    for i, q in enumerate(questions, 1):
        if isinstance(q, tuple):
            text, src = q
            lines.append(f"{i}. {text}")
            if src:
                lines.append(f"   ↳ from: {src}")
        else:
            lines.append(f"{i}. {q}")
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


def cmd_prep(force: bool, dry_run: bool, date_str: str = None) -> int:
    for d in (COS, BRIEFS, JOURNAL, WORLD):
        d.mkdir(parents=True, exist_ok=True)
    today = date_str if date_str else _today()
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
    loops, loops_src = open_loops()
    ensure_world_pulse()  # generate today's world file if missing (fail-safe)
    world_pulse = gather_world_pulse()
    world_items = world_pulse.get("items", [])
    weekly_due, weekly_overdue = weekly_status(state)
    if weekly_due:
        weekly_line = f"{weekly_overdue}d overdue" if weekly_overdue > 0 else "due today"
    else:
        next_in = WEEKLY_EVERY_DAYS - _days_since(state.get("last_weekly", ""))
        weekly_line = f"in {next_in}d"
    # Question engine v2: three archetypes (decision-forcing / connection-
    # surfacing / life-chairman), no repeat of yesterday's exact questions.
    questions = generate_questions_v2(today, life_staleness(), due_goals, loops,
                                      weekly_due, threads, world_items,
                                      loops_src=loops_src,
                                      world_path=world_pulse.get("path", ""))
    outer_loop = gather_outer_loop()
    evolution = gather_evolution()
    system_vitals = gather_system_vitals()
    memory_review = gather_memory_review()
    listening = gather_listening()
    # OBSERVATION ONLY (Farrice, 2026-07-27, binding): session-end closeout is
    # the PRIMARY healing mechanism — failures get swept and repaired in the
    # session that produced them, not on a timetable that is inconvenient when
    # he is creating at speed. The daily brief only reports what is still open.
    # `report` runs the detectors (~2s) and never writes the heal record.
    if not dry_run:
        try:
            subprocess.run([sys.executable,
                            str(REPO_ROOT / 'execution' / 'self_heal.py'), 'report'],
                           capture_output=True, text=True, timeout=180,
                           cwd=str(REPO_ROOT))
        except Exception:
            pass
    self_heal = gather_self_heal()
    brief = render_brief(state, goals, due_goals, revenue_due, threads, loops,
                         questions, weekly_line, outer_loop, evolution, world_pulse,
                         loops_src=loops_src, system_vitals=system_vitals,
                         memory_review=memory_review, self_heal=self_heal,
                         listening=listening)

    if dry_run:
        print(brief)
        return 0

    brief_path.write_text(brief)
    state["nudge_line"] = compose_nudge(state, questions, revenue_due, weekly_due, weekly_overdue)
    state["nudge_date"] = today
    state["last_prep"] = datetime.now().isoformat(timespec="seconds")
    # Apex W1 (2026-07-29): the COS gets debt numbers, not just cadence —
    # open missions + stale handoffs were structurally invisible to it.
    try:
        from pulse_dashboard import open_missions as _om
        state["open_missions"] = len(_om())
    except Exception:
        pass
    try:
        from handoff_store import threads as _threads, _stale as _hs_stale
        state["stale_handoffs"] = sum(1 for m in _threads() if _hs_stale(m.get("date", "")))
    except Exception:
        pass
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
    p_prep.add_argument("--date", help="YYYY-MM-DD (default: today)")
    sub.add_parser("nudge", help="print current nudge line")
    p_cap = sub.add_parser("capture", help="append capture to journal (+ inbox mirror)")
    p_cap.add_argument("--text", required=True)
    p_cap.add_argument("--route", choices=["journal", "inbox"], default="journal")
    p_mark = sub.add_parser("mark", help="record daily/weekly completion")
    p_mark.add_argument("kind", choices=["daily", "weekly"])
    sub.add_parser("status", help="JSON state for workflow routing")
    args = parser.parse_args()

    if args.cmd == "prep":
        return cmd_prep(args.force, args.dry_run, args.date if hasattr(args, 'date') else None)
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
