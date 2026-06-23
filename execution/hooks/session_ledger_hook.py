#!/usr/bin/env python3
"""session_ledger_hook.py — deterministic session ledger for finalize debt,
sub-agent spawn truth, routing warnings, and outer-loop staleness.

WHY: chain_runner.py finalize() is "non-negotiable" but only fired when Claude
remembered (the banned AI-memory-dependent pattern). This ledger makes the
obligation physical: expert-skill loads + produced artifacts accrue DEBT; a
Bash run of finalize clears it; the Stop hook blocks turn-end ONCE while debt
is unpaid (then yields with a loud warning — never traps a session).

Modes (argv[1]):
    prompt    UserPromptSubmit — accrue workflow debt, warn on routing
              violations (NEVER blocks), inject outer-loop staleness, prune.
    posttool  PostToolUse — accrue skill-load debt, mark artifacts produced,
              count true sub-agent spawns, detect finalize runs.
    stop      Stop — block once on ripened debt (LEDGER_ENFORCE=1), else
              observe-log + warn. Logs sub-agent misses with measured counts.

Debt RIPENS only when an expert skill was loaded AND a file artifact was
produced — answering questions about a skill never blocks.

Enforcement flag: LEDGER_ENFORCE=1 in the hook env → Stop blocks once.
Default (unset/0) = observe-only: would-block events go to
.agent/sessions/observe-log.jsonl for false-positive review.

FAIL-SAFE: any exception → exit 0. A broken ledger must never trap a session.
Wired via .claude/settings.local.json. User decision 2026-06-09: hard block
(after observe window).
"""

import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SESSIONS_DIR = REPO_ROOT / ".agent" / "sessions"
OBSERVE_LOG = SESSIONS_DIR / "observe-log.jsonl"
MISSES_LOG = REPO_ROOT / "evolution_store" / "sub_agent_misses.jsonl"
ORCH_STATE = REPO_ROOT / "evolution_store" / "orchestrator_state.json"
REVENUE = REPO_ROOT / ".agent" / "revenue-outcomes.json"
SKILLS_DIR = REPO_ROOT / "skills"

ENFORCE = os.environ.get("LEDGER_ENFORCE", "0") == "1"

# Internal paths whose writes never count as "produced a deliverable".
INTERNAL_WRITE = re.compile(r"/\.(agent|claude|tmp|memory)/|\.json$|\.jsonl$|/memory/")


def _now() -> str:
    return datetime.now().isoformat()


def _qualifying_workflows():
    try:
        sys.path.insert(0, str(REPO_ROOT / "execution"))
        from chain_runner import _SUB_AGENT_QUALIFYING_WORKFLOWS
        return set(_SUB_AGENT_QUALIFYING_WORKFLOWS)
    except Exception:
        return {"parallax", "extract-forge", "writers-room", "build-bos",
                "deep-research", "avatar-machine", "council", "campaign"}


def _ledger_path(session_id: str) -> Path:
    safe = re.sub(r"[^A-Za-z0-9_-]", "_", session_id or "unknown")[:64]
    return SESSIONS_DIR / f"ledger-{safe}.json"


def _load(session_id: str) -> dict:
    p = _ledger_path(session_id)
    if p.exists():
        try:
            return json.loads(p.read_text())
        except Exception:
            pass
    return {
        "session_id": session_id, "debts": [], "produced": False,
        "produced_paths": [], "subagent_spawns": 0, "finalized_at": None,
        "last_debt_at": None, "stop_blocked_once": False,
        "staleness_warned": False, "miss_logged": False,
        "handoff_pending": False, "handoff_warned": False,
        "session_pinned": False, "session_pinned_at": None, "pin_nudged": False,
    }


def _save(ledger: dict) -> None:
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    _ledger_path(ledger["session_id"]).write_text(json.dumps(ledger, indent=1))


def _prune() -> None:
    cutoff = time.time() - 7 * 86400
    try:
        for f in SESSIONS_DIR.glob("ledger-*.json"):
            if f.stat().st_mtime < cutoff:
                f.unlink()
    except Exception:
        pass


def _is_expert_skill(name: str) -> bool:
    """Expert skills carry a genius.md; utility skills don't."""
    return (SKILLS_DIR / name / "genius.md").exists()


def _add_debt(ledger: dict, dtype: str, name: str) -> None:
    if any(d["type"] == dtype and d["name"] == name for d in ledger["debts"]):
        return
    ledger["debts"].append({"type": dtype, "name": name, "ts": _now()})
    ledger["last_debt_at"] = _now()


def _ripened(ledger: dict) -> bool:
    if not ledger["debts"] or not ledger["produced"]:
        return False
    if ledger["finalized_at"] and ledger["finalized_at"] >= (ledger["last_debt_at"] or ""):
        return False
    return True


def _staleness_line() -> str:
    parts = []
    try:
        state = json.loads(ORCH_STATE.read_text()).get("state", {})
        last_weekly = state.get("last_weekly", "")
        if last_weekly:
            days = (datetime.now() - datetime.fromisoformat(last_weekly)).days
            if days > 7:
                parts.append(f"evolution weekly {days}d stale")
    except Exception:
        pass
    try:
        d = json.loads(REVENUE.read_text())
        outs = d.get("outcomes", d if isinstance(d, list) else [])
        pending = [o for o in outs if o.get("outcome_type") == "pending"]
        today = datetime.now().date().isoformat()
        due = sum(1 for o in pending if o.get("check_in_date") and o["check_in_date"] <= today)
        if due:
            parts.append(f"{due} outcome check-in{'s' if due != 1 else ''} due — "
                         f"run `python3 execution/revenue_tracker.py due`")
        if len(pending) > 10:
            parts.append(f"{len(pending)} deliverables awaiting revenue/outcome data")
    except Exception:
        pass
    if not parts:
        return ""
    return ("OUTER LOOP STALE (" + "; ".join(parts) +
            ") — suggest running /weekly-closeout (~20 min) when convenient.")


# ──────────────────────────────────────────────────────────────────
# prompt
# ──────────────────────────────────────────────────────────────────
def handle_prompt(payload: dict) -> None:
    session_id = payload.get("session_id", "unknown")
    prompt = (payload.get("prompt") or "").strip()
    ledger = _load(session_id)
    _prune()

    context_lines = []

    # Outer-loop staleness — once per session.
    if not ledger["staleness_warned"]:
        line = _staleness_line()
        if line:
            context_lines.append(line)
            ledger["staleness_warned"] = True

    # Explicit workflow invocation -> debt + routing warn.
    m = re.match(r"^[/@]([a-z0-9][a-z0-9-]+)\b\s*(.*)", prompt, re.IGNORECASE | re.DOTALL)
    if m:
        name, remainder = m.group(1).lower(), m.group(2)
        if name in _qualifying_workflows():
            _add_debt(ledger, "qualifying_workflow", name)
        # Routing warn (NEVER blocks — 2026-05-23 false-halt precedent).
        try:
            sys.path.insert(0, str(REPO_ROOT / "execution"))
            from routing_enforcer import check_routing
            v = check_routing(remainder or prompt, name)
            if not v.get("valid"):
                context_lines.append(
                    "ROUTING WARNING (deterministic, routing_enforcer binding "
                    f"'{v.get('binding_matched')}'): {v.get('violation_reason')}"
                    + (f" {v.get('advisory')}" if v.get("advisory") else "")
                )
        except Exception:
            pass

    _save(ledger)
    if context_lines:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "UserPromptSubmit",
                "additionalContext": "\n".join(context_lines),
            }
        }))
    sys.exit(0)


# ──────────────────────────────────────────────────────────────────
# posttool
# ──────────────────────────────────────────────────────────────────
def handle_posttool(payload: dict) -> None:
    session_id = payload.get("session_id", "unknown")
    tool = payload.get("tool_name", "")
    tin = payload.get("tool_input") or {}
    ledger = _load(session_id)
    changed = False

    if tool == "Read":
        fp = str(tin.get("file_path", ""))
        m = re.search(r"/skills/([^/]+)/(SKILL|genius)\.md$", fp)
        if m and _is_expert_skill(m.group(1)):
            _add_debt(ledger, "skill_loaded", m.group(1))
            changed = True
    elif tool == "Skill":
        name = str(tin.get("skill", "")).split(":")[-1]
        if name == "handoff":
            ledger["handoff_pending"] = True
            changed = True
        if name and _is_expert_skill(name):
            _add_debt(ledger, "skill_loaded", name)
            changed = True
    elif tool in ("Write", "Edit", "NotebookEdit"):
        fp = str(tin.get("file_path", tin.get("notebook_path", "")))
        if fp and not INTERNAL_WRITE.search(fp):
            ledger["produced"] = True
            if fp not in ledger["produced_paths"]:
                ledger["produced_paths"] = (ledger["produced_paths"] + [fp])[-10:]
            changed = True
    elif tool in ("Task", "Agent"):
        ledger["subagent_spawns"] += 1
        changed = True
    elif tool == "Bash":
        blob = json.dumps(payload.get("tool_response", "")) + str(tin.get("command", ""))
        if "chain_runner.py" in blob and "finalize" in blob:
            if "CHAIN FINALIZE" in blob:
                ledger["finalized_at"] = _now()
                changed = True
            elif "FINALIZE FAILED" in blob:
                ledger.setdefault("finalize_failures", 0)
                ledger["finalize_failures"] += 1
                changed = True
        if "handoff_store.py" in blob and ("saved:" in blob or "already stored" in blob):
            ledger["handoff_pending"] = False
            ledger["handoff_saved_at"] = _now()
            # Any successful handoff save makes the work recoverable by name in
            # /resume — that satisfies the pin backstop (it can't be lost), pinned
            # or not. The dedicated pin paths below are the explicit/floated cases.
            ledger["session_pinned"] = True
            ledger["session_pinned_at"] = _now()
            changed = True
        # Pin detection for the non-"saved:" paths: annotate --pin (prints
        # "annotated"), the bare `pin` subcommand (prints "pinned:"), and
        # chain_runner's auto-pin inside finalize (prints "CHAIN PINNED"). Keeps the
        # Stop hook's pin backstop quiet. Mirrors the finalize-detection pattern above.
        _cmd = str(tin.get("command", ""))
        _pin_via_store = (
            "handoff_store.py" in _cmd
            and ("--pin" in _cmd or bool(re.search(r"handoff_store\.py\s+pin\b", _cmd)))
            and ("annotated" in blob or ("pinned:" in blob and "unpinned:" not in blob))
        )
        if _pin_via_store or "CHAIN PINNED" in blob:
            ledger["session_pinned"] = True
            ledger["session_pinned_at"] = _now()
            changed = True

    if changed:
        _save(ledger)
    sys.exit(0)


# ──────────────────────────────────────────────────────────────────
# stop
# ──────────────────────────────────────────────────────────────────
def _prefilled_finalize(ledger: dict) -> str:
    skills = [d["name"] for d in ledger["debts"] if d["type"] == "skill_loaded"]
    wfs = [d["name"] for d in ledger["debts"] if d["type"] == "qualifying_workflow"]
    skill = skills[-1] if skills else "<skill-dir>"
    wf = wfs[-1] if wfs else (skills[-1] if skills else "<workflow>")
    content = ledger["produced_paths"][-1] if ledger["produced_paths"] else ""
    cmd = (f'python3 execution/chain_runner.py finalize "<one-line description of what was produced>" '
           f"--expert {skill} --skill {skill} --workflow {wf} "
           f"--type Content --intent <1-10> --expert-score <1-10> --adversarial <1-10> "
           f"--sub-agents {ledger['subagent_spawns']} "
           f'--notes "<what worked/didn\'t> | Factual Grounding: <1-10 or N/A> | Verification: <PASS/FAIL/N/A>"')
    if content:
        cmd += f' --content-file "{content}"'
    return cmd


def _suggest_pin_title(ledger: dict) -> str:
    paths = ledger.get("produced_paths") or []
    stem = Path(paths[-1]).stem if paths else "session"
    return f"{datetime.now().strftime('%Y-%m-%d')} · {stem}"


def handle_stop(payload: dict) -> None:
    session_id = payload.get("session_id", "unknown")
    stop_active = bool(payload.get("stop_hook_active"))
    ledger = _load(session_id)

    # Handoff persistence nudge — independent of finalize debt. Fires when the
    # /handoff skill ran but the durable `handoff_store.py save` never did, so
    # the handoff lives only in the ephemeral temp dir (lost on reboot).
    if ledger.get("handoff_pending") and not ledger.get("handoff_warned"):
        ledger["handoff_warned"] = True
        _save(ledger)
        ho_reason = (
            "HANDOFF NOT PERSISTED — the /handoff skill ran but the durable save "
            "never did, so the handoff lives only in the ephemeral temp dir (cleared "
            "on reboot). Persist it now so /session-kickoff can resume it:\n\n"
            "    python execution/handoff_store.py save --from-temp"
        )
        try:
            SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
            with open(OBSERVE_LOG, "a") as f:
                f.write(json.dumps({"ts": _now(), "session_id": session_id,
                                    "event": "handoff_unpersisted", "enforce": ENFORCE}) + "\n")
        except Exception:
            pass
        if ENFORCE and not stop_active:
            print(json.dumps({"decision": "block", "reason": ho_reason}))
            sys.exit(0)
        print(f"[ledger observe] {ho_reason}", file=sys.stderr)
        # fall through to finalize-debt logic

    # Session-pin nudge — independent of finalize debt. Fires when a durable artifact
    # shipped but no titled pin was recorded, so the work won't surface in the /resume
    # menu by name. Deterministic backstop for the auto-pin happy-paths (chain_runner
    # finalize / end-session --pin / /pin-session); never depends on Claude remembering.
    if (ledger.get("produced") and ledger.get("produced_paths")
            and not ledger.get("session_pinned") and not ledger.get("pin_nudged")):
        ledger["pin_nudged"] = True
        _save(ledger)
        _pt = _suggest_pin_title(ledger)
        pin_reason = (
            "SESSION NOT PINNED — a durable artifact shipped this session "
            f"({ledger['produced_paths'][-3:]}) but no titled pin was recorded, so this "
            "work won't surface in the /resume menu by name. Pin it (the title becomes "
            "the retrieval handle):\n\n"
            f'    /pin-session "{_pt}"\n\n'
            "or directly (slug = thread for idempotency):\n"
            f'    python3 execution/handoff_store.py save <artifact-or-pointer.md> '
            f'--thread <thread-slug> --slug <thread-slug> --status active '
            f'--hint "{_pt}" --pin --overwrite'
        )
        try:
            SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
            with open(OBSERVE_LOG, "a") as f:
                f.write(json.dumps({"ts": _now(), "session_id": session_id,
                                    "event": "session_unpinned", "enforce": ENFORCE}) + "\n")
        except Exception:
            pass
        if ENFORCE and not stop_active:
            print(json.dumps({"decision": "block", "reason": pin_reason}))
            sys.exit(0)
        print(f"[ledger observe] {pin_reason}", file=sys.stderr)
        # fall through to finalize-debt logic

    if not _ripened(ledger):
        sys.exit(0)

    # Sub-agent miss: qualifying workflow ran with zero measured spawns.
    wfs = [d["name"] for d in ledger["debts"] if d["type"] == "qualifying_workflow"]
    miss_line = ""
    if wfs and ledger["subagent_spawns"] == 0 and not ledger["miss_logged"]:
        try:
            MISSES_LOG.parent.mkdir(parents=True, exist_ok=True)
            with open(MISSES_LOG, "a") as f:
                f.write(json.dumps({
                    "timestamp": _now(), "workflow": wfs[-1], "skill": "",
                    "expert": "", "task_type": "", "qualifying": True,
                    "sub_agents_spawned": 0, "source": "stop_hook",
                }) + "\n")
            ledger["miss_logged"] = True
            miss_line = (f"\nALSO: qualifying workflow '{wfs[-1]}' ran with 0 measured "
                         f"sub-agent spawns — miss logged (source: stop_hook).")
        except Exception:
            pass

    reason = (
        "FINALIZE DEBT UNPAID — expert skill(s) "
        f"{[d['name'] for d in ledger['debts']]} were loaded and artifacts were produced "
        f"({ledger['produced_paths'][-3:]}), but chain_runner finalize never ran. "
        "Run Chain Step 6 now (fill in the scores honestly — name the rubric anchor for any 8+):\n\n"
        + _prefilled_finalize(ledger) + miss_line
    )

    if ENFORCE and not stop_active and not ledger["stop_blocked_once"]:
        ledger["stop_blocked_once"] = True
        _save(ledger)
        print(json.dumps({"decision": "block", "reason": reason}))
        sys.exit(0)

    # Observe mode / second stop: log + warn loudly, never trap.
    _save(ledger)
    try:
        SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
        with open(OBSERVE_LOG, "a") as f:
            f.write(json.dumps({
                "ts": _now(), "session_id": session_id,
                "would_block": not ledger["stop_blocked_once"], "enforce": ENFORCE,
                "debts": ledger["debts"], "produced_paths": ledger["produced_paths"][-3:],
                "subagent_spawns": ledger["subagent_spawns"],
            }) + "\n")
    except Exception:
        pass
    print(f"[ledger observe] {reason}", file=sys.stderr)
    sys.exit(0)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
    except Exception:
        sys.exit(0)
    try:
        if mode == "prompt":
            handle_prompt(payload)
        elif mode == "posttool":
            handle_posttool(payload)
        elif mode == "stop":
            handle_stop(payload)
    except SystemExit:
        raise
    except Exception:
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
