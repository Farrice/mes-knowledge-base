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
    stop      Stop — AUTO-PIN the session under a convention-shaped title if a
              durable artifact shipped unpinned (forgotten close); then block once on
              ripened finalize debt (LEDGER_ENFORCE=1), else observe-log + warn. Logs
              sub-agent misses with measured counts.

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
        "pending_routing": None, "closeout_ran": False,
        "bash_fail_streak": 0, "learning_debt": [], "solution_cards_saved": 0,
        "learning_debt_nudged": False,
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


ROUTING_TRIAL_FILE = Path(__file__).resolve().parents[2] / ".agent" / "routing-enforce-trial.json"
ROUTING_ENFORCE_LOG = SESSIONS_DIR / "routing-enforce-log.jsonl"


def _routing_enforce_trial() -> dict | None:
    """Active, unexpired Wave-2 routing-enforcement trial, else None.

    The trial file IS the flip switch: active:false (or deleting the file, or
    passing its 'ends' date) reverts to warn-only with no code change.
    """
    try:
        t = json.loads(ROUTING_TRIAL_FILE.read_text())
        if not t.get("active"):
            return None
        if datetime.now().strftime("%Y-%m-%d") > str(t.get("ends", "9999-12-31")):
            return None  # trial auto-expires; weekly review decides permanence
        return t
    except (OSError, ValueError):
        return None


def _log_routing_enforce(ledger: dict, binding, chosen, v: dict, action: str) -> None:
    try:
        ROUTING_ENFORCE_LOG.parent.mkdir(parents=True, exist_ok=True)
        with ROUTING_ENFORCE_LOG.open("a") as f:
            f.write(json.dumps({
                "ts": datetime.now().isoformat(),
                "session_id": ledger.get("session_id"),
                "binding": binding,
                "chosen_workflow": chosen,
                "mandatory_workflow": v.get("mandatory_workflow"),
                "action": action,
            }) + "\n")
    except OSError:
        pass


def _reconcile_routing_feedback(ledger: dict, loaded_dir: str) -> bool:
    """Close the suggest -> load -> outcome loop (Wave 3, 2026-07).

    skill_router_hook.py stashes a "pending_routing" entry (routing_id +
    suggested_dirs) into this same ledger whenever it emits a suggestion.
    When an expert skill actually loads, compare it against that pending
    entry: if the loaded skill was one of the suggestions -> auto_match, else
    -> auto_miss. Logged to routing_intelligence.log_feedback(); the loaded
    skill is always passed as `correction` (even on auto_match) so
    evolution_orchestrator.run_routing_learning() has a clean, structured
    field to nudge weights from in both directions.

    Fires once: the pending entry is cleared (set to None) whether or not
    the routing_intelligence write itself succeeds — a dead pending entry
    must never retry forever. Returns True if the ledger was mutated
    (caller is responsible for _save()). Never raises.
    """
    pending = ledger.get("pending_routing")
    if not pending or not pending.get("routing_id"):
        return False
    try:
        sys.path.insert(0, str(REPO_ROOT / "execution"))
        import routing_intelligence  # noqa: E402

        suggested = pending.get("suggested_dirs") or []
        matched = loaded_dir in suggested
        rating = "auto_match" if matched else "auto_miss"
        notes = (
            f"expert skill '{loaded_dir}' loaded "
            f"{'matching' if matched else 'not matching'} suggestion {suggested}"
        )
        routing_intelligence.log_feedback(
            routing_id=pending["routing_id"],
            rating=rating,
            session_id=ledger.get("session_id", ""),
            correction=loaded_dir,
            notes=notes,
        )
    except Exception:
        pass
    finally:
        ledger["pending_routing"] = None
    return True


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

    # COS morning-brief nudge — read-only (line precomputed by cos_prep.py prep),
    # once per DAY per session (date-stamped so long-lived sessions re-nudge each
    # morning), self-suppressing after `cos_prep.py mark daily`.
    try:
        today = datetime.now().date().isoformat()
        if ledger.get("cos_nudged") != today:
            cs = json.loads((REPO_ROOT / ".agent" / "cos" / "state.json").read_text())
            if (cs.get("nudge_date") == today and cs.get("last_daily") != today
                    and cs.get("nudge_line")):
                context_lines.append(
                    "COS BRIEFING NUDGE (deterministic — relay this to Farrice at the "
                    "top of your reply): " + cs["nudge_line"]
                )
                ledger["cos_nudged"] = today
    except Exception:
        pass

    # Explicit workflow invocation -> debt + routing check (warn or enforce).
    m = re.match(r"^[/@]([a-z0-9][a-z0-9-]+)\b\s*(.*)", prompt, re.IGNORECASE | re.DOTALL)
    if m:
        name, remainder = m.group(1).lower(), m.group(2)
        if name in _qualifying_workflows():
            _add_debt(ledger, "qualifying_workflow", name)
        # Routing check. Default = warn-only (2026-05-23 false-halt precedent).
        # Wave 2 flip (2026-07-17, Farrice-approved graduated enforcement): while
        # .agent/routing-enforce-trial.json is active and unexpired, EXPLICIT
        # domain-binding violations block with a documented override token.
        # The fuzzy control_intent_classifier binding stays warn-only always —
        # it false-positived on /resume the very day of the flip (exempt list).
        try:
            sys.path.insert(0, str(REPO_ROOT / "execution"))
            from routing_enforcer import check_routing
            v = check_routing(remainder or prompt, name)
            if not v.get("valid"):
                trial = _routing_enforce_trial()
                binding = v.get("binding_matched")
                warn_line = (
                    "ROUTING WARNING (deterministic, routing_enforcer binding "
                    f"'{binding}'): {v.get('violation_reason')}"
                    + (f" {v.get('advisory')}" if v.get("advisory") else "")
                )
                if not trial or binding in trial.get("exempt_bindings", []):
                    context_lines.append(warn_line)
                    if trial:
                        _log_routing_enforce(ledger, binding, name, v, "warned_exempt")
                else:
                    token = trial.get("override_token", "!route")
                    if token.lower() in prompt.lower():
                        _log_routing_enforce(ledger, binding, name, v, "override")
                        context_lines.append(
                            f"ROUTING OVERRIDE logged ({token}) — binding '{binding}' "
                            f"wanted {v.get('mandatory_workflow')}; proceeding with /{name}."
                        )
                    else:
                        _log_routing_enforce(ledger, binding, name, v, "blocked")
                        _save(ledger)
                        print(json.dumps({"decision": "block", "reason": (
                            f"ROUTING BINDING ENFORCED (trial to {trial.get('ends')}, "
                            f"routing_enforcer binding '{binding}'): "
                            f"{v.get('violation_reason')} "
                            f"Mandatory route: {v.get('mandatory_workflow')}. "
                            f"To proceed with /{name} anyway, resend with '{token}' in the "
                            f"prompt (logged override — compass, not cage). Trial revert: "
                            f"set active:false in .agent/routing-enforce-trial.json."
                        )}))
                        sys.exit(0)
        except SystemExit:
            raise
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
    loaded_expert_skill = None

    if tool == "Read":
        fp = str(tin.get("file_path", ""))
        m = re.search(r"/skills/([^/]+)/(SKILL|genius)\.md$", fp)
        if m and _is_expert_skill(m.group(1)):
            _add_debt(ledger, "skill_loaded", m.group(1))
            loaded_expert_skill = m.group(1)
            changed = True
    elif tool == "Skill":
        name = str(tin.get("skill", "")).split(":")[-1]
        if name == "handoff":
            ledger["handoff_pending"] = True
            changed = True
        if name and _is_expert_skill(name):
            _add_debt(ledger, "skill_loaded", name)
            loaded_expert_skill = name
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
        tool_response = payload.get("tool_response", "")
        blob = json.dumps(tool_response) + str(tin.get("command", ""))
        _cmd = str(tin.get("command", ""))

        # Cracked-problem detection (Solution Recorder, 2026-07-07): a fail ->
        # fail -> ... -> success streak on Bash is the deterministic signature
        # of a hard problem getting solved. Booking it as learning_debt makes
        # "capture the fix" a physical nudge instead of something Claude has
        # to remember. Never raises — this whole hook is fail-safe by contract.
        #
        # Failure signal, in authority order (verified against the harness
        # source: projects/Claude Code Harness Analysis/source-code-v2.1.88/
        # src/tools/BashTool/{BashTool.tsx,commandSemantics.ts} — the Bash
        # tool_response schema is {stdout, stderr, interrupted, isImage,
        # returnCodeInterpretation, ...}; there is NO is_error key, ever):
        #   1. interrupted: true -> failure.
        #   2. returnCodeInterpretation (when present) is AUTHORITATIVE. Its
        #      only possible values are commandSemantics messages: "No matches
        #      found" (grep/rg exit 1), "Some directories were inaccessible"
        #      (find 1), "Files differ" (diff 1), "Condition is false"
        #      (test/[ 1) — all non-error semantics -> SUCCESS — and the
        #      default-semantic "Command failed with exit code N" -> failure.
        #   3. Fallback ONLY when that field is absent: conservative marker
        #      match against the RESPONSE OUTPUT (stdout+stderr fields only).
        #      Never the command text — `grep -rn "Error:"` must not self-flag.
        _resp = tool_response if isinstance(tool_response, dict) else None
        _resp_out = ((str(_resp.get("stdout", "")) + "\n" + str(_resp.get("stderr", "")))
                     if _resp is not None else str(tool_response))
        _is_error = None
        if _resp is not None:
            if _resp.get("interrupted") is True:
                _is_error = True
            else:
                _rci = _resp.get("returnCodeInterpretation")
                if isinstance(_rci, str) and _rci:
                    _is_error = _rci.startswith("Command failed")
        if _is_error is None:
            _fail_markers = (
                "command not found", "Traceback (most recent call last)",
                "Error:", "FAILED", "fatal:", "No such file or directory",
                "Permission denied", "ModuleNotFoundError", "SyntaxError",
            )
            _is_error = any(marker in _resp_out for marker in _fail_markers)

        if _is_error:
            ledger["bash_fail_streak"] = ledger.get("bash_fail_streak", 0) + 1
            changed = True
        else:
            _streak = ledger.get("bash_fail_streak", 0)
            if _streak >= 3:
                _entry = {"ts": _now(), "evidence": _cmd[:120], "streak": _streak}
                ledger["learning_debt"] = (ledger.get("learning_debt", []) + [_entry])[-5:]
                changed = True
            if ledger.get("bash_fail_streak", 0) != 0:
                ledger["bash_fail_streak"] = 0
                changed = True

        # Solution Card saved -> the debt this streak represents is captured;
        # clear it entirely (mirrors the finalize-clears-debt pattern below).
        # Strict on purpose: the COMMAND must be a solution_recorder save AND
        # the response output must carry the marker at line start — so
        # cat-ing/grep-ing a file that merely CONTAINS the marker text can
        # never false-clear real debt.
        if ("solution_recorder.py" in _cmd and "save" in _cmd
                and re.search(r"^SOLUTION CARD SAVED: docs/solutions/", _resp_out, re.MULTILINE)):
            if ledger.get("learning_debt"):
                ledger["learning_debt"] = []
            ledger["solution_cards_saved"] = ledger.get("solution_cards_saved", 0) + 1
            changed = True

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
        _pin_via_store = (
            "handoff_store.py" in _cmd
            and ("--pin" in _cmd or bool(re.search(r"handoff_store\.py\s+pin\b", _cmd)))
            and ("annotated" in blob or ("pinned:" in blob and "unpinned:" not in blob))
        )
        if _pin_via_store or "CHAIN PINNED" in blob:
            ledger["session_pinned"] = True
            ledger["session_pinned_at"] = _now()
            changed = True
        # Closeout-spine detection — mirrors the finalize-detection pattern above.
        # Lets the SessionEnd hook backstop (session_end_hook.py) know the spine
        # already ran this session, so it doesn't re-run in degraded mode.
        if "CLOSEOUT SPINE COMPLETE" in blob or "end_session_closeout.py" in _cmd:
            ledger["closeout_ran"] = True
            changed = True

    if loaded_expert_skill and _reconcile_routing_feedback(ledger, loaded_expert_skill):
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


def _humanize(s: str) -> str:
    s = re.sub(r"^\d{4}[-\d]*\s*", "", s)      # strip a leading date
    s = re.sub(r"[-_]+", " ", s).strip()
    return s.title() if s else s


def _derive_title_thread(ledger: dict):
    """Best-effort, convention-shaped Title + stable thread slug from the produced
    paths. Convention (shared with /end-session + /pin-session):
        '[Project or Client] — [Work Type]'
    The RICH semantic title comes from the happy-paths (chain_runner.finalize /
    /end-session), which have the LLM's understanding of the session. This is the
    deterministic backstop for a session closed without any of them — it guarantees a
    consistent, retrievable name, not a perfect one."""
    paths = ledger.get("produced_paths") or []
    p = paths[-1] if paths else ""
    m = re.search(r"(?:^|/)(?:projects|_active|deliverables|products|clients)/([^/]+)/", p)
    if m:
        thread = m.group(1)
        project = _humanize(thread)
    else:
        parent = Path(p).parent.name if p else ""
        thread = (re.sub(r"[^a-z0-9-]+", "-", parent.lower()).strip("-") or "session")
        project = _humanize(parent) or "Session"
    worktype = _humanize(Path(p).stem) if p else ""
    if worktype and worktype.lower() != project.lower():
        title = f"{project} — {worktype}"
    else:
        title = project or worktype or "Session"
    return title, thread


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

    # Learning-debt nudge (Solution Recorder, 2026-07-07) — independent of
    # finalize debt. Fires once per session when a hard-won fix (3+ Bash
    # fail->success streak) never got captured as a Solution Card. Observe-only
    # — mirrors the finalize-debt observe-mode style, never blocks.
    if ledger.get("learning_debt") and ledger.get("produced") and not ledger.get("learning_debt_nudged"):
        ledger["learning_debt_nudged"] = True
        _save(ledger)
        ld_reason = (
            f"LEARNING DEBT: a hard problem was cracked this session "
            f"({len(ledger['learning_debt'])} fail→success streak(s)) with no Solution Card. "
            "Run /extract-approach — incomplete capture is unfinished work."
        )
        try:
            SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
            with open(OBSERVE_LOG, "a") as f:
                f.write(json.dumps({"ts": _now(), "session_id": session_id,
                                    "event": "learning_debt_open",
                                    "learning_debt": ledger["learning_debt"],
                                    "enforce": ENFORCE}) + "\n")
        except Exception:
            pass
        print(f"[ledger observe] {ld_reason}", file=sys.stderr)
        # fall through — this never blocks (observe-only per Farrice's ask)

    # Session AUTO-PIN backstop — independent of finalize debt. Fires when a durable
    # artifact shipped but no titled pin was recorded (chain_runner.finalize /
    # /end-session / /pin-session all set session_pinned). Rather than just nudging,
    # this AUTO-PINS the session under a convention-shaped title so a forgotten close
    # never loses the work — it always surfaces in /resume by name. The rich semantic
    # title still comes from the happy-paths; this is the deterministic safety net.
    # Farrice's ask (2026): never hand-type or rename a session. Fail-safe: any error
    # falls back to the old nudge so the work is still recoverable.
    if (ledger.get("produced") and ledger.get("produced_paths")
            and not ledger.get("session_pinned") and not ledger.get("pin_nudged")):
        ledger["pin_nudged"] = True
        title, thread = _derive_title_thread(ledger)
        auto_ok = False
        try:
            import subprocess
            SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
            ptr = SESSIONS_DIR / f"autopin-{re.sub(r'[^A-Za-z0-9_-]', '-', thread)[:48]}.md"
            ptr.write_text(
                f"# {title}\n\n"
                "**Auto-pinned by the Stop-hook backstop** — this session closed without "
                "/end-session, /pin-session, or chain finalize, so the deterministic net "
                "titled and pinned it to keep the work retrievable.\n\n"
                f"**Artifacts:** {', '.join(ledger['produced_paths'][-5:])}\n\n"
                f"**Retrieve:** `/resume {thread}`. Re-title with `/pin-session` if you want "
                "a sharper name (idempotent — overwrites this one row).\n"
            )
            r = subprocess.run(
                [sys.executable, str(REPO_ROOT / "execution" / "handoff_store.py"),
                 "save", str(ptr), "--thread", thread, "--slug", thread,
                 "--status", "active", "--hint", title, "--pin", "--overwrite"],
                capture_output=True, text=True, timeout=20, cwd=str(REPO_ROOT))
            auto_ok = "saved:" in ((r.stdout or "") + (r.stderr or ""))
        except Exception:
            auto_ok = False
        if auto_ok:
            ledger["session_pinned"] = True
            ledger["session_pinned_at"] = _now()
        _save(ledger)
        try:
            SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
            with open(OBSERVE_LOG, "a") as f:
                f.write(json.dumps({"ts": _now(), "session_id": session_id,
                                    "event": "session_autopinned" if auto_ok else "session_unpinned",
                                    "title": title, "thread": thread, "enforce": ENFORCE}) + "\n")
        except Exception:
            pass
        if auto_ok:
            print(f'[ledger] AUTO-PINNED this session as "{title}" (thread {thread}). '
                  f"Retrieve with /resume {thread}. Re-title with /pin-session for a sharper name.",
                  file=sys.stderr)
        else:
            pin_reason = (
                "SESSION NOT PINNED — a durable artifact shipped "
                f"({ledger['produced_paths'][-3:]}) but the auto-pin failed. Pin it "
                "(the title becomes the retrieval handle):\n\n"
                f'    /pin-session "{title}"'
            )
            if ENFORCE and not stop_active:
                print(json.dumps({"decision": "block", "reason": pin_reason}))
                sys.exit(0)
            print(f"[ledger observe] {pin_reason}", file=sys.stderr)
        # fall through to finalize-debt logic

    if not _ripened(ledger):
        # Next-Prompts steering nudge — warn-only, fires once per session when
        # a finalize ran and this stop is NOT itself blocking. GEMINI.md/
        # AGENTS.md carry the Operator Lesson / 3 Next-Prompts steering spec
        # for Codex/Gemini surfaces; CLAUDE.md sessions never had a
        # deterministic backstop for it (2026-07-06 gap-fix).
        if ledger.get("finalized_at") and not ledger.get("next_prompts_nudged"):
            ledger["next_prompts_nudged"] = True
            _save(ledger)
            print(
                "Operator Lesson: emit 3 Next-Prompts (deepen / adjacent / "
                "next-milestone) if not already given.",
                file=sys.stderr,
            )
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
