#!/usr/bin/env python3
"""steering_loop_hook.py — deterministic steering-loop nudge + compliance observer.

WHY: "Close every substantive reply with a Next Moves block + Operator Lesson"
is a standing behavioral ask (directives/steering-loop.md) that only holds if
Claude remembers it turn after turn — the banned AI-memory-dependent pattern.
This hook makes the reminder physical (UserPromptSubmit) and the compliance
check deterministic (Stop, observe-only — it never blocks a turn).

Modes (argv[1]):
    prompt    UserPromptSubmit — increments the per-session exchange counter
              and prints the steering-loop reminder block + a rotating
              harness tip. Silent on empty prompts / `/steering-loop` itself.
    stop      Stop — reads the transcript, checks the last assistant message
              for a "Next Moves" block. Missing on a substantive (>=400 char)
              reply -> one line appended to the observe log. Never prints to
              stdout, never blocks, never exits nonzero.
    status    Manual CLI check — one-line summary (enabled/disabled, sessions
              tracked, total misses logged).

Toggle off: STEERING_LOOP_OFF=1 env or `.agent/steering-loop.off` file ->
both hook modes go silent (status still reports the state).

FAIL-SAFE: any exception -> exit 0. A broken nudge hook must never trap a
session. Wired via .claude/settings.json.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# ──────────────────────────────────────────────────────────────────
# Paths
# ──────────────────────────────────────────────────────────────────
_env_root = os.environ.get("CLAUDE_PROJECT_DIR")
REPO_ROOT = Path(_env_root) if _env_root else Path(__file__).resolve().parents[2]

AGENT_DIR = REPO_ROOT / ".agent"
SESSIONS_DIR = AGENT_DIR / "sessions"
STATE_PATH = AGENT_DIR / "steering-loop-state.json"
OBSERVE_LOG = SESSIONS_DIR / "steering-observe.jsonl"
OFF_FILE = AGENT_DIR / "steering-loop.off"

MAX_SESSIONS = 10

TIPS = [
    "/resume surfaces last session's pinned handoffs by name — start there instead of re-explaining context.",
    "python3 execution/memory_facade.py \"<intent>\" --top 10 searches ALL memory stores (sovereign, episodic, wiki, solutions) in one call.",
    "/go \"<messy thought>\" compiles raw intent into a routed run packet — you never have to pre-sharpen your ask.",
    "/convene runs a multi-expert council; presets: /council /roundtable /strike /campaign.",
    "Fable orchestrates, Sonnet executes — say 'dispatch agents for X' to fan grunt work out and keep the main thread for judgment.",
    "/extract-approach banks a cracked problem as a Solution Card so it auto-resurfaces before you ever re-solve it.",
    "execution/research.py is receipt-carrying research — never accept a research answer given from training memory.",
    "/dump captures a loose thought to the COS inbox without derailing the current session.",
    "/wargame-run banks frontier judgment as failure-maps so cheaper executor models can run blind later.",
    "/weekly-closeout (~20 min) drains overdue outcome check-ins and calibration drift.",
    "/system-audit owns any 'route/hook/wiring feels off' complaint — describe the symptom, not the fix.",
    "Workflows answer to bare names too — 'run parallax' works without the slash.",
    "/handoff writes a titled session handoff so the next session picks up by name via /resume.",
    "python3 execution/contextual_next_prompts.py --objective \"...\" renders a deterministic next-prompt set on demand.",
    "/fantastic-studio is the front door for image/video generation — never hand a bare prompt to a raw generator.",
]


# ──────────────────────────────────────────────────────────────────
# Shared helpers
# ──────────────────────────────────────────────────────────────────
def _toggle_off() -> bool:
    if os.environ.get("STEERING_LOOP_OFF") == "1":
        return True
    try:
        return OFF_FILE.exists()
    except Exception:
        return False


def _now_iso() -> str:
    return datetime.now().isoformat()


def _now_iso_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def _load_state() -> dict:
    try:
        if STATE_PATH.exists():
            data = json.loads(STATE_PATH.read_text())
            if isinstance(data, dict):
                return data
    except Exception:
        pass
    return {}


def _prune_state(state: dict, keep: int = MAX_SESSIONS) -> dict:
    if len(state) <= keep:
        return state
    try:
        items = sorted(state.items(), key=lambda kv: (kv[1] or {}).get("updated", ""))
    except Exception:
        items = list(state.items())
    drop = len(items) - keep
    for key, _ in items[:drop]:
        state.pop(key, None)
    return state


def _save_state(state: dict) -> None:
    try:
        AGENT_DIR.mkdir(parents=True, exist_ok=True)
        STATE_PATH.write_text(json.dumps(state, indent=1))
    except Exception:
        pass


def _append_observe(record: dict) -> None:
    try:
        SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
        with open(OBSERVE_LOG, "a") as f:
            f.write(json.dumps(record) + "\n")
    except Exception:
        pass


def _extract_text(content) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                parts.append(str(item.get("text", "")))
        return "".join(parts)
    return ""


# ──────────────────────────────────────────────────────────────────
# prompt (UserPromptSubmit)
# ──────────────────────────────────────────────────────────────────
def handle_prompt(payload: dict) -> None:
    session_id = payload.get("session_id") or "unknown"
    prompt = payload.get("prompt") or ""

    state = _load_state()
    entry = state.get(session_id) or {"count": 0, "updated": ""}
    entry["count"] = int(entry.get("count", 0)) + 1
    entry["updated"] = _now_iso()
    state[session_id] = entry
    count = entry["count"]
    _prune_state(state)
    _save_state(state)

    if not prompt.strip() or prompt.strip().startswith("/steering-loop"):
        sys.exit(0)

    # ── Co-Creation Step 0 injection (Farrice 2026-07-27) ─────────────────
    # The PARTNER dial was "always-on" in CLAUDE.md for 11 days and fired
    # zero times, because a file pointer (and later inline prose) is not a
    # mechanism. This is: a per-prompt classifier that injects the dial when
    # the ask is taste-bearing. Same delivery channel as the steering block,
    # which demonstrably fires every exchange. Fail-safe by contract.
    co_creation = ""
    try:
        p = prompt.lower()
        _taste = re.search(
            r"\b(headline|hook|about section|profile|bio|position|positioning|"
            r"offer|brand|voice|tone|rewrite|draft|post|copy|content|edition|"
            r"newsletter|write|messaging|angle|tagline|name for|naming|story|"
            r"strategy|taste|creative)\b", p)
        _execute = (
            re.search(r"\b(just do it|just run|just fix|go ahead|proceed|ship it|"
                      r"commit|push|no questions|execute)\b", p)
            or p.strip().startswith(("/", "run ", "@"))
        )
        _foggy = re.search(r"\b(not sure|don'?t know|feel like|something is off|"
                           r"help me figure|what do you think|foggy|stuck)\b", p)
        if (_taste or _foggy) and not _execute:
            co_creation = (
                "CO-CREATION STEP 0 (deterministic, from steering_loop_hook.py): "
                "taste-bearing or foggy ask detected → PARTNER dial is ON.\n"
                "1) Load memory + canonical files FIRST (FARRICE-MASTER-CONTEXT.md is "
                "canonical for identity/voice/offer work — read before writing).\n"
                "2) Ask ONE question aimed past his current frame BEFORE producing. "
                "Wait for the answer. Never interview about what's already on disk.\n"
                "3) Then produce at ship standard.\n"
                "Iteration brake: TWO rejected takes on the same artifact = stop "
                "producing variants and go back to the source input.\n"
                "Override: he says 'just do it' / scores 4-5 sharp → EXECUTE dial, "
                "act now, refine after.\n"
            )
    except Exception:
        co_creation = ""

    tip = TIPS[(count - 1) % len(TIPS)]
    # Loop-repair #10 (2026-07-24): the hook reads its own miss log — ≥2 misses
    # this session escalates the reminder from passive to imperative.
    session_misses = 0
    try:
        if OBSERVE_LOG.exists():
            with open(OBSERVE_LOG) as f:
                session_misses = sum(1 for line in f if f'"{session_id}"' in line)
    except Exception:
        session_misses = 0
    escalation = (
        f"ESCALATION: {session_misses} Next-Moves misses already logged for THIS session — "
        "the closing block is NOT optional on the next substantive reply.\n"
        if session_misses >= 2 else ""
    )
    block = (
        co_creation +
        "STEERING LOOP (deterministic, from steering_loop_hook.py — not user input):\n"
        + escalation +
        f"Exchange {count}. Close any substantive reply with a **Next Moves** block "
        "(3 copy-paste prompts: Deepen / Adjacent / Act) + a 1-line Operator Lesson. "
        "Skip only for terse asks or pure system commands. Spec: directives/steering-loop.md.\n"
        "Forge Radar: if this session shows a repeated problem, a manual loop, or a "
        "missing tool, flag it in ONE line naming the build + tradeoff — never block "
        "on it. PoC gate applies.\n"
        f"Harness tip: {tip}"
    )
    print(block)
    sys.exit(0)


# ──────────────────────────────────────────────────────────────────
# stop (Stop — observe only)
# ──────────────────────────────────────────────────────────────────
def handle_stop(payload: dict) -> None:
    if bool(payload.get("stop_hook_active")):
        sys.exit(0)

    session_id = payload.get("session_id") or "unknown"
    transcript_path = payload.get("transcript_path")
    if not transcript_path:
        sys.exit(0)

    try:
        raw = Path(transcript_path).read_text(errors="replace")
    except Exception:
        sys.exit(0)

    found_any = False
    last_text = ""
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except Exception:
            continue
        if not isinstance(record, dict) or record.get("type") != "assistant":
            continue
        message = record.get("message") or {}
        if not isinstance(message, dict):
            continue
        found_any = True
        last_text = _extract_text(message.get("content")) or ""

    if not found_any or len(last_text) < 400:
        sys.exit(0)

    if "next moves" in last_text.lower():
        sys.exit(0)

    state = _load_state()
    exchange = 0
    try:
        exchange = int((state.get(session_id) or {}).get("count", 0))
    except Exception:
        exchange = 0

    _append_observe({
        "ts": _now_iso_utc(),
        "session_id": session_id,
        "exchange": exchange,
        "event": "next-moves-missing",
        "chars": len(last_text),
    })

    # Wave-2 flip #4 (dormant until .agent/enforce-trials/steering.json activates):
    # while the trial enforces, a substantive reply missing the Next Moves block is
    # blocked ONCE (stop_hook_active guard above prevents loops — the retried stop
    # passes through). Observe-only remains the shipped default.
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from enforce_trial import active_trial
        trial = active_trial("steering")
    except Exception:
        trial = None
    if trial:
        print(json.dumps({"decision": "block", "reason": (
            f"STEERING LOOP ENFORCED (trial to {trial.get('ends')}): this substantive "
            "reply is missing the Next Moves block (3 copy-paste prompts: Deepen / "
            "Adjacent / Act) + 1-line Operator Lesson per directives/steering-loop.md. "
            "Add it and finish the turn. Revert: set active:false in "
            ".agent/enforce-trials/steering.json."
        )}))
    sys.exit(0)


# ──────────────────────────────────────────────────────────────────
# status
# ──────────────────────────────────────────────────────────────────
def handle_status() -> None:
    off = _toggle_off()
    state = _load_state()
    sessions = len(state)
    misses = 0
    try:
        if OBSERVE_LOG.exists():
            with open(OBSERVE_LOG) as f:
                misses = sum(1 for _ in f)
    except Exception:
        misses = 0
    word = "disabled" if off else "enabled"
    print(f"steering-loop: {word} | sessions tracked: {sessions} | misses logged: {misses}")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    try:
        if mode == "status":
            handle_status()
            sys.exit(0)

        if _toggle_off():
            sys.exit(0)

        try:
            raw = sys.stdin.read()
            payload = json.loads(raw) if raw.strip() else {}
            if not isinstance(payload, dict):
                payload = {}
        except Exception:
            payload = {}

        if mode == "prompt":
            handle_prompt(payload)
        elif mode == "stop":
            handle_stop(payload)
    except SystemExit:
        raise
    except Exception:
        pass
    sys.exit(0)


if __name__ == "__main__":
    main()
