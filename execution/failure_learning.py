#!/usr/bin/env python3
"""failure_learning.py — turn recurring failures into written prevention rules.

WHY (Farrice, 2026-07-27): "I never want to be running into failure modes and
failures anymore as an issue... The system should be learning and improving and
doing better every time a failure mode pops up."

THE FINDING THAT MADE THIS NECESSARY. The learning loop already existed and had
never once run:

    evolution/failure-registry.md    19 lines, template only, 0 rules
    evolution/mission-log.md         25 lines, 0 entries
    /aar (the only writer)           0 uses since install
    all of it last touched           2026-04-04 — 115 days

Same root cause as every other dead channel found this session: `/aar` is a
workflow a human has to REMEMBER to invoke, so it never fired, so 115 days of
failures taught the system nothing. Worse, the JCC orchestrator agent embeds
that empty file under the heading "Active Failure Prevention Rules" — every
deployment loads zero learned rules and treats that as the state of the art.

THIS MODULE IS NOT A WORKFLOW. It is called from self_heal.py's heal path and
from the end-session closeout spine. No invocation, no reminder, no LLM. It
reads `.agent/health/self-heal.jsonl` — which self_heal already writes on every
heal outcome — and converts recurrence into rules in the registry's own
documented schema.

RECURRENCE RULES
    heal_failed >= 3x for one id        CHRONIC — the fix does not work; stop
                                        retrying it and say why
    healed >= 5x across >= 5 days       RECURRING — the repair sticks but the
                                        CAUSE is upstream and unaddressed
    JUDGMENT id open >= 7 days          ROTTING — a decision nobody made

HARD RULES
  1. Append-only within the sentinel. Existing rules are NEVER rewritten; a
     repeat occurrence updates only that rule's `Last Triggered` line.
  2. One rule per failure signature. The signature is the healer id — writing
     a second rule for the same id is how a registry becomes noise.
  3. Deterministic. No model call, no judgment, no prose generation beyond the
     evidence already in the log.
  4. Never raises. A learner that breaks a heal is worse than no learner.

Usage:
    python3 execution/failure_learning.py            # learn + print what changed
    python3 execution/failure_learning.py --report   # read-only, write nothing
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEAL_LOG = ROOT / ".agent" / "health" / "self-heal.jsonl"
REPORT_CACHE = ROOT / ".agent" / "health" / "self-heal-report.json"
LATEST = ROOT / ".agent" / "health" / "self-heal-latest.json"

# CANONICAL registry home. It previously lived only at
# ~/.claude/plugins/installed/jarvis-command-center/evolution/failure-registry.md
# — inside a plugin directory a plugin update can replace. Learning data does
# not belong in a wipeable cache, so the canonical copy is here, git-tracked and
# covered by the auto-push backup. The plugin path is kept as a mirror so JCC
# keeps loading (see mirror_to_plugin()).
REGISTRY = ROOT / "evolution_store" / "failure-registry.md"
PLUGIN_MIRROR = (Path.home() / ".claude" / "plugins" / "installed"
                 / "jarvis-command-center" / "evolution" / "failure-registry.md")

SENTINEL = "<!-- Rules below this line -->"

CHRONIC_FAILS = 3       # heal_failed occurrences before a fix is declared broken
RECURRING_HEALS = 5     # successful repeats before the CAUSE is called upstream
RECURRING_DAYS = 5
ROTTING_DAYS = 7        # an open JUDGMENT item this old is a decision not made


def _rows() -> list[dict]:
    out = []
    try:
        with HEAL_LOG.open() as f:
            for line in f:
                try:
                    out.append(json.loads(line))
                except ValueError:
                    continue
    except OSError:
        pass
    return out


def _ts(row: dict) -> datetime | None:
    try:
        return datetime.fromisoformat(str(row.get("ts", "")))
    except ValueError:
        return None


def analyse() -> list[dict]:
    """Pure function of the log + caches. Returns findings, writes nothing."""
    rows = _rows()
    by_id: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        if r.get("id"):
            by_id[str(r["id"])].append(r)

    findings = []
    for fid, rs in sorted(by_id.items()):
        fails = [r for r in rs if r.get("action") == "heal_failed"]
        heals = [r for r in rs if r.get("action") == "healed"]

        if len(fails) >= CHRONIC_FAILS:
            notes = [str(r.get("note", ""))[:90] for r in fails[-2:]]
            findings.append({
                "kind": "CHRONIC", "id": fid, "count": len(fails),
                "what": f"the automated fix has failed {len(fails)} times",
                "cause": notes[-1] if notes else "(no note recorded)",
                "rule": (f"Do not retry the {fid} healer — its fix is broken, not its "
                         f"detection. Demote it to a classifier and repair the "
                         f"underlying tool before re-promoting."),
                "last": max((_ts(r) for r in fails if _ts(r)), default=None),
            })

        if len(heals) >= RECURRING_HEALS:
            stamps = sorted(t for t in (_ts(r) for r in heals) if t)
            if stamps and (stamps[-1] - stamps[0]) >= timedelta(days=RECURRING_DAYS):
                findings.append({
                    "kind": "RECURRING", "id": fid, "count": len(heals),
                    "what": (f"repaired {len(heals)} times over "
                             f"{(stamps[-1] - stamps[0]).days} days — the repair holds "
                             f"but the cause regenerates"),
                    "cause": "upstream producer re-dirties this state after each repair",
                    "rule": (f"Treat recurring {fid} as a symptom. Find what re-dirties "
                             f"it between runs and fix THAT; a healer firing every day "
                             f"is a workaround, not a solution."),
                    "last": stamps[-1],
                })

    # Rotting JUDGMENT items — read from whichever cache is fresher.
    open_rows, cache_ts = [], None
    for p in (REPORT_CACHE, LATEST):
        try:
            d = json.loads(p.read_text())
        except Exception:
            continue
        t = str(d.get("ts", ""))
        if cache_ts is None or t > cache_ts:
            open_rows, cache_ts = d.get("rows") or [], t
    for r in open_rows:
        if r.get("cls") != "JUDGMENT":
            continue
        fid = str(r.get("id", ""))
        first = min((t for t in (_ts(x) for x in by_id.get(fid, [])) if t), default=None)
        if first and (datetime.now() - first) >= timedelta(days=ROTTING_DAYS):
            findings.append({
                "kind": "ROTTING", "id": fid,
                "count": (datetime.now() - first).days,
                "what": f"open for {(datetime.now() - first).days} days with no decision",
                "cause": str(r.get("what", ""))[:140],
                "rule": (f"Decide {fid} or explicitly park it. An escalation nobody "
                         f"answers is indistinguishable from a check nobody runs."),
                "last": datetime.now(),
            })
    return findings


def _existing_rules(text: str) -> dict[str, tuple[int, int]]:
    """Map failure-signature -> (start, end) char offsets of its rule block."""
    out = {}
    for m in re.finditer(r"^### \[([A-Z]+)\]: (\S+)$", text, re.M):
        nxt = text.find("\n### ", m.end())
        out[m.group(2)] = (m.start(), nxt if nxt > 0 else len(text))
    return out


def _render_rule(f: dict) -> str:
    last = (f["last"] or datetime.now()).date().isoformat()
    return (
        f"### [{f['kind']}]: {f['id']}\n"
        f"- **Added:** {datetime.now().date().isoformat()}\n"
        f"- **What Happened:** {f['what']}\n"
        f"- **Root Cause:** {f['cause']}\n"
        f"- **Prevention Rule:** {f['rule']}\n"
        f"- **Occurrences:** {f['count']}\n"
        f"- **Last Triggered:** {last}\n"
        f"- **Status:** ACTIVE\n"
        f"- **Source:** deterministic, from .agent/health/self-heal.jsonl "
        f"(execution/failure_learning.py) — no human invocation required\n"
    )


def _ensure_registry() -> str:
    if REGISTRY.exists():
        return REGISTRY.read_text()
    header = (
        "# Failure Registry\n\n"
        "Prevention rules derived from real failures. **Written automatically** by\n"
        "`execution/failure_learning.py` off `.agent/health/self-heal.jsonl` — no\n"
        "`/aar` invocation, no human memory required.\n\n"
        "History: this registry lived in a plugin directory and sat empty from\n"
        "2026-04-04 to 2026-07-27 because its only writer was a slash command\n"
        "nobody remembered to run. 115 days of failures taught the system nothing.\n\n"
        "One rule per failure signature. Repeat occurrences update `Last Triggered`\n"
        "and `Occurrences` in place — rules are never duplicated or rewritten.\n\n"
        "---\n\n"
        f"{SENTINEL}\n"
    )
    return header


def learn(dry_run: bool = False) -> list[dict]:
    """Write/refresh registry rules for every finding. Never raises."""
    try:
        findings = analyse()
        if not findings:
            return []
        text = _ensure_registry()
        if SENTINEL not in text:
            text = text.rstrip() + f"\n\n{SENTINEL}\n"
        existing = _existing_rules(text)
        changed = []
        for f in findings:
            block = _render_rule(f)
            if f["id"] in existing:
                s, e = existing[f["id"]]
                old = text[s:e]
                # Refresh ONLY the volatile lines; the rule's prose is preserved.
                new = re.sub(r"- \*\*Last Triggered:\*\* .*",
                             f"- **Last Triggered:** {(f['last'] or datetime.now()).date().isoformat()}", old)
                new = re.sub(r"- \*\*Occurrences:\*\* .*",
                             f"- **Occurrences:** {f['count']}", new)
                if new != old:
                    text = text[:s] + new + text[e:]
                    existing = _existing_rules(text)
                    changed.append({**f, "action": "refreshed"})
            else:
                text = text.rstrip() + "\n\n" + block
                existing = _existing_rules(text)
                changed.append({**f, "action": "recorded"})
        if changed and not dry_run:
            REGISTRY.parent.mkdir(parents=True, exist_ok=True)
            REGISTRY.write_text(text)
            mirror_to_plugin(text)
        return changed
    except Exception:  # noqa: BLE001 — a learner must never break a heal
        return []


def mirror_to_plugin(text: str) -> None:
    """Keep the JCC plugin copy readable so `/solo` and `/aar` still resolve.
    Best-effort: the canonical copy is the repo one."""
    try:
        if PLUGIN_MIRROR.parent.exists():
            PLUGIN_MIRROR.write_text(text)
    except OSError:
        pass


def render(changed: list[dict]) -> str:
    if not changed:
        return "FAILURE LEARNING — no recurring failure patterns; nothing to record."
    L = [f"FAILURE LEARNING — {len(changed)} rule(s) written to "
         f"{REGISTRY.relative_to(ROOT)}"]
    for c in changed:
        L.append(f"  [{c['action'].upper()}] {c['kind']}: {c['id']} — {c['what']}")
    return "\n".join(L)


def main() -> int:
    dry = "--report" in sys.argv
    changed = learn(dry_run=dry)
    print(render(changed) + ("  [--report: nothing written]" if dry and changed else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
