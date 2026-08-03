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

# ── Bound injector (Model-Dialect Adaptation Layer, 2026-07-28) ──────────
# Reads the ACTIVE model's machine-dialect block from its card and injects
# per-prompt what that model won't infer. Model swap = new card, not new code.
# Kill switch: DIALECT_INJECTOR_OFF=1 or .agent/dialect-injector.off.
DIALECT_CARDS_DIR = REPO_ROOT / "directives" / "model-dialects"
DIALECT_OFF_FILE = AGENT_DIR / "dialect-injector.off"
ACTIVE_MODEL_CACHE = AGENT_DIR / "active-model.json"
DIALECT_BEGIN = "<!-- BEGIN:machine-dialect -->"
DIALECT_END = "<!-- END:machine-dialect -->"
# Default seat when nothing resolves (first prompt of a fresh session, no
# transcript yet): the system default seat per CLAUDE.md. A resolved model
# with NO card injects nothing — honest silence beats wrong corrections.
DIALECT_DEFAULT_MODEL = "claude-opus-5"

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
# Bound injector (Model-Dialect Adaptation Layer)
# ──────────────────────────────────────────────────────────────────
def _dialect_injector_off() -> bool:
    if os.environ.get("DIALECT_INJECTOR_OFF") == "1":
        return True
    try:
        return DIALECT_OFF_FILE.exists()
    except Exception:
        return False


def _dialect_cards_dir() -> Path:
    d = os.environ.get("DIALECT_CARDS_DIR")
    return Path(d) if d else DIALECT_CARDS_DIR


def _active_model(payload: dict) -> str:
    """Resolve the ACTIVE model id. Order: payload → env → transcript →
    cache → default seat. Never raises."""
    m = payload.get("model")
    if isinstance(m, dict):
        m = m.get("id") or m.get("model")
    if not m:
        m = os.environ.get("CLAUDE_MODEL") or os.environ.get("ANTHROPIC_MODEL")
    if not m:
        tp = payload.get("transcript_path")
        if tp:
            try:
                lines = Path(tp).read_text(errors="replace").splitlines()
                for line in reversed(lines[-400:]):
                    if '"assistant"' not in line:
                        continue
                    try:
                        rec = json.loads(line)
                    except Exception:
                        continue
                    if isinstance(rec, dict) and rec.get("type") == "assistant":
                        mm = (rec.get("message") or {}).get("model")
                        if mm:
                            m = mm
                            break
            except Exception:
                pass
    if m:
        try:
            AGENT_DIR.mkdir(parents=True, exist_ok=True)
            ACTIVE_MODEL_CACHE.write_text(
                json.dumps({"model": str(m), "ts": _now_iso()}))
        except Exception:
            pass
        return str(m)
    try:
        cached = json.loads(ACTIVE_MODEL_CACHE.read_text())
        if cached.get("model"):
            return str(cached["model"])
    except Exception:
        pass
    return DIALECT_DEFAULT_MODEL


def _load_dialect(model_id: str):
    """Find the dialect card whose machine-dialect block matches model_id.
    Returns the parsed dict, or None (missing/malformed = honest silence)."""
    try:
        for card in sorted(_dialect_cards_dir().glob("*.md")):
            try:
                text = card.read_text(errors="replace")
            except Exception:
                continue
            if DIALECT_BEGIN not in text or DIALECT_END not in text:
                continue
            block = text.split(DIALECT_BEGIN, 1)[1].split(DIALECT_END, 1)[0]
            block = re.sub(r"^\s*```(json)?\s*$", "", block, flags=re.M)
            try:
                data = json.loads(block)
            except Exception:
                continue
            if not isinstance(data, dict):
                continue
            for pat in data.get("model_match") or []:
                if pat and str(pat) in model_id:
                    return data
    except Exception:
        return None
    return None


_DELIVERABLE_RE = re.compile(
    r"\b(write|draft|rewrite|revise|build|create|design|implement|fix|refactor|"
    r"extract|audit|research|analy[sz]e|plan|produce|generate|ship|post|edition|"
    r"newsletter|email|copy|content|hook|headline|offer|brand|voice|strategy|"
    r"script|carousel|deck|proposal|report|workflow|skill|agent|page|landing|"
    r"bio|profile|deliverable|campaign|funnel)\b")


def _dialect_class(prompt: str):
    """deliverable | conversational | None (skip). Slash/bare-name workflow
    invocations count as deliverable — workflows produce deliverables."""
    p = prompt.strip()
    if len(p) < 5:
        return None
    pl = p.lower()
    if pl.startswith("/steering-loop"):
        return None
    if p.startswith(("/", "@")) or pl.startswith("run "):
        return "deliverable"
    return "deliverable" if _DELIVERABLE_RE.search(pl) else "conversational"


def _dialect_block(payload: dict, prompt: str) -> str:
    """Render the active model's pathology corrections for this prompt class.
    Empty string on: kill switch, no class, no card for the model. Never raises."""
    if _dialect_injector_off():
        return ""
    klass = _dialect_class(prompt)
    if not klass:
        return ""
    model = _active_model(payload)
    dialect = _load_dialect(model)
    if not dialect:
        return ""
    inject = dialect.get("inject") or {}
    lines = [str(x) for x in (inject.get(klass) or [])]
    if klass == "deliverable":
        lines += [str(x) for x in (inject.get("delegation") or [])]
    if not lines:
        return ""
    nb = str(dialect.get("negative_brief") or "")
    lines = [ln.replace("{negative_brief}", nb) for ln in lines]
    # Amnesty 2026-07-29: header compressed (LEAN ruling). "card:", "class:"
    # and the bounds-win phrase stay — they are verify_dialect_injector pins.
    header = (
        f"MODEL DIALECT (card: {model}, class: {klass} — nudge, not cage; "
        "Farrice's explicit bounds always win):")
    return header + "\n" + "\n".join(f"- {ln}" for ln in lines) + "\n"


# ──────────────────────────────────────────────────────────────────
# Co-Creation Enforcement Layer (Farrice 2026-07-28)
# ──────────────────────────────────────────────────────────────────
# WHY: the co-creation doctrine (verify → align → act) lived as prose and the
# model still produced 5 renditions of one About on educated guesses while
# Farrice directed everything (2026-07-28 About session; 2026-07-27 headline
# session = same failure). A doctrine without a counter is a vibe. This layer
# adds STATE (renditions per artifact stem from the session ledger, rejections
# per stem, feedback-turn tracking) and injects three deterministic mechanisms:
#   1. SPIRAL BRAKE — 2 rejected takes or 3+ renditions of one stem → stop
#      producing variants; fresh crack / gut-check / pick.
#   2. FEEDBACK-TURN PROTOCOL — critique-shaped prompt → restate verdicts,
#      ONE AskUserQuestion on ambiguity BEFORE producing, ratchet, ONE take.
#   3. WORK-MODE FRONT DOOR — raw un-slash-commanded input → operating card
#      at workflow standard (REFINE/BUILD/IDEATE/DECIDE/CAPTURE), overridable
#      with one word ("mode X").
# Compass doctrine holds: instructs the MODEL, never blocks Farrice.
# Kill switch: CO_CREATION_OFF=1 or .agent/co-creation.off.

CC_STATE_PATH = AGENT_DIR / "co-creation-state.json"
CC_OFF_FILE = AGENT_DIR / "co-creation.off"


def _cc_off() -> bool:
    if os.environ.get("CO_CREATION_OFF") == "1":
        return True
    try:
        return CC_OFF_FILE.exists()
    except Exception:
        return False


def _cc_load() -> dict:
    try:
        if CC_STATE_PATH.exists():
            data = json.loads(CC_STATE_PATH.read_text())
            if isinstance(data, dict):
                return data
    except Exception:
        pass
    return {}


def _cc_save(state: dict) -> None:
    try:
        AGENT_DIR.mkdir(parents=True, exist_ok=True)
        state = _prune_state(state)
        CC_STATE_PATH.write_text(json.dumps(state, indent=1))
    except Exception:
        pass


# Version-marker suffixes stripped repeatedly to find an artifact's stem:
# about_v13 / about_v12_L1 / about-final / draft_2 → "about". A strip that
# would empty the stem is rejected (take_a stays take_a rather than "").
_CC_SUFFIXES = [
    re.compile(r"[_\-. ]v(er(sion)?)?\d+$", re.I),
    re.compile(r"[_\-. ](final|draft|rev|copy|edit)\d*$", re.I),
    re.compile(r"[_\-. ]l\d+$", re.I),
    re.compile(r"[_\-. ]\d{1,3}$"),
]


def _cc_stem(path_str: str) -> str:
    try:
        base = Path(str(path_str)).name
        base = base.rsplit(".", 1)[0].lower()
        changed = True
        while changed:
            changed = False
            for rx in _CC_SUFFIXES:
                stripped = rx.sub("", base)
                if stripped and stripped != base:
                    base = stripped
                    changed = True
        return base.strip("_-. ")
    except Exception:
        return ""


def _cc_renditions(session_id: str) -> dict:
    """{stem: distinct-rendition-count} from this session's ledger
    produced_paths (maintained by session_ledger_hook). Never raises."""
    try:
        safe = re.sub(r"[^A-Za-z0-9_-]", "_", session_id or "unknown")[:64]
        ledger_path = SESSIONS_DIR / f"ledger-{safe}.json"
        if not ledger_path.exists():
            return {}
        data = json.loads(ledger_path.read_text())
        seen: dict = {}
        for p in (data.get("produced_paths") or []):
            s = _cc_stem(p)
            if not s:
                continue
            seen.setdefault(s, set()).add(Path(str(p)).name.lower())
        return {s: len(names) for s, names in seen.items()}
    except Exception:
        return {}


_CC_CRITIQUE_RE = re.compile(
    r"\b(edits?|change|remove|cut|don'?t like|didn'?t like|not working|weird|"
    r"disjointed|flat|bland|generic|too safe|better (way|delivery|version)|"
    r"needs? to be|i feel like|rework|redo|revise|another (crack|pass|try)|"
    r"instead of|payoff|punchier|beaten? (it )?down|restructure|not landing|"
    r"reads? (a little )?(weird|off)|final edits)\b")

_CC_REFERENT_RE = re.compile(
    r"\b(this|that|the) (version|draft|piece|post|about|copy|take|one|part|"
    r"section|line)\b|\bv\d+\b|\"[^\"]{8,}\"|“[^”]{8,}”")


def _cc_feedback(prompt: str, stems: dict) -> bool:
    """Critique-shaped prompt aimed at an existing artifact."""
    p = prompt.strip()
    if len(p) < 180:
        return False
    pl = p.lower()
    if not _CC_CRITIQUE_RE.search(pl):
        return False
    if _CC_REFERENT_RE.search(pl):
        return True
    return any(s in pl for s in stems if len(s) >= 4)


_CC_MODE_OVERRIDE_RE = re.compile(
    r"\bmode (build-new|refine-existing|ideate|decide|capture)\b", re.I)


def _cc_work_mode(prompt: str, is_feedback: bool):
    """BUILD-NEW | REFINE-EXISTING | IDEATE | DECIDE | CAPTURE | None."""
    pl = prompt.lower().strip()
    m = _CC_MODE_OVERRIDE_RE.search(pl)
    if m:
        return m.group(1).upper()
    if is_feedback:
        return "REFINE-EXISTING"
    if re.search(r"\b(should (i|we)|which (one|of these|way|take)|pick (one|a|the)|"
                 r"choose|decide|gut.?check|or should)\b", pl):
        return "DECIDE"
    if re.search(r"\b(ideas?|angles?|options|variations?|brainstorm|riff|ideate|"
                 r"ways we could)\b", pl):
        return "IDEATE"
    if _DELIVERABLE_RE.search(pl):
        return "BUILD-NEW"
    if len(pl) > 400 and "?" not in pl and not re.search(
            r"\b(can you|please|need you|help me)\b", pl):
        return "CAPTURE"
    return None


# Amnesty 2026-07-29: cards compressed to one line each (LEAN ruling). The
# mechanisms are unchanged; only the lecture went. Full specs live in
# directives/steering-loop.md — the card is a reminder, not the manual.
_CC_MODE_CARDS = {
    "REFINE-EXISTING": (
        "Feedback turn: restate his verdicts first; conflicting verdicts → ONE "
        "question before producing; log felt verdicts (voice_ratchet.py add); "
        "then ONE take by ONE pen."),
    "BUILD-NEW": (
        "Name the route/expert in one line (redirectable), load the expert "
        "files before producing, finalize after."),
    "IDEATE": (
        "Diverge before converging — offer /ideate or /jam on taste-bearing "
        "work; no premature single answer."),
    "DECIDE": (
        "Name the fork first, recommend one side, let him pick — artifact "
        "comes after the decision."),
    "CAPTURE": (
        "Thought dump: capture verbatim (thought_bank.py capture), confirm in "
        "ONE line, no unpacking unless asked."),
}


# ── Universal Intent Mirror (Farrice ruling 2026-08-02: "Mirror + one push-back") ──
# Every raw/word-vomit ask, ANY domain, gets a ≤5-line "what I heard" card plus
# exactly one senior-partner push-back BEFORE work starts. Sharp, specific asks
# skip the mirror (never the judgment). Deterministic detector, stateless,
# nudge-not-cage per Compass. Ruling record: memory
# feedback_production-grade-floor-craft-gate; queued in
# extractions/master-hunt-2026-08-02-creative-floor-dossier.md §Next-session.

_MIRROR_RAMBLE_RE = re.compile(
    r"\b(i want|i think|i've been|i was thinking|i don't know|i just|"
    r"kind of|sort of|you know|stuff like that|things like that|or something)\b")
_MIRROR_MULTI_ASK_RE = re.compile(
    r"\b(also|additionally|another thing|and then|on top of that|one more thing|"
    r"oh and|plus)\b")


def _mirror_signals(prompt: str) -> int:
    """Count word-vomit signals. 2+ (with length) = raw dump."""
    pl = prompt.lower()
    signals = 0
    if len(_MIRROR_RAMBLE_RE.findall(pl)) >= 2:
        signals += 1
    if len(_MIRROR_MULTI_ASK_RE.findall(pl)) >= 2:
        signals += 1
    if pl.count("?") >= 3:
        signals += 1
    if len(re.findall(r"[.!?]\s", prompt)) >= 6 or prompt.count("\n\n") >= 2:
        signals += 1
    return signals


def _mirror_block(prompt: str, mode) -> str:
    """The Mirror + one push-back card, or '' when the ask is sharp.

    Skips: short prompts (<350 chars — sharp asks are compact), CAPTURE mode
    (thought dumps park verbatim, they don't get interrogated), and prompts
    with fewer than 2 vomit signals.
    """
    if len(prompt.strip()) < 350 or mode == "CAPTURE":
        return ""
    if _mirror_signals(prompt) < 2:
        return ""
    return (
        "🪞 INTENT MIRROR (raw dump detected — Farrice ruling 2026-08-02, "
        "\"Mirror + one push-back\"): BEFORE producing, reflect back in ≤5 "
        "lines — deliverable+format · felt standard · references/assets in "
        "play · budget/constraints · the one detail that makes it HIS — then "
        "add exactly ONE senior-partner push-back or sharpening question "
        "(not a soft clarifier; the question a partner with skin in the game "
        "would ask). Proceed on his confirm or visible non-objection. Nudge, "
        "never a cage: if the ask is genuinely sharp despite its length, say "
        "so in one line and go.")


def _cc_prompt_block(session_id: str, prompt: str, count: int) -> str:
    """Assemble mode card + spiral brake; update rejection state. Never raises."""
    # Slash/system commands already name their route — a mode card is redundant
    # and the brake is noise there (live-fire calibration, first firing was on
    # /end-session). Bare-name workflow invocations still pass through.
    if prompt.strip().startswith(("/", "@")):
        return ""
    renditions = _cc_renditions(session_id)
    is_feedback = _cc_feedback(prompt, renditions)

    state = _cc_load()
    entry = state.get(session_id) or {"stems": {}, "updated": ""}
    stems_state = entry.get("stems") or {}

    if is_feedback:
        pl = prompt.lower()
        targets = [s for s in renditions if len(s) >= 4 and s in pl]
        if not targets:
            multi = [s for s, n in renditions.items() if n >= 2]
            if len(multi) == 1:
                targets = multi
        for s in targets:
            rec = stems_state.get(s) or {"rejections": 0}
            rec["rejections"] = int(rec.get("rejections", 0)) + 1
            stems_state[s] = rec

    entry["stems"] = stems_state
    entry["last_feedback_exchange"] = count if is_feedback else int(
        entry.get("last_feedback_exchange") or 0)
    entry["updated"] = _now_iso()
    state[session_id] = entry
    _cc_save(state)

    lines = []
    mode = _cc_work_mode(prompt, is_feedback)
    if mode:
        card = _CC_MODE_CARDS.get(mode) or ""
        lines.append(f"MODE {mode} (say 'mode X' to override): {card}".rstrip())

    mirror = _mirror_block(prompt, mode)
    if mirror:
        lines.append(mirror)

    # Spiral brake: his stated rule made physical — 2 rejected takes on one
    # stem, or 3+ renditions, means variants stop.
    for s, n in sorted(renditions.items(), key=lambda kv: -kv[1]):
        rej = int((stems_state.get(s) or {}).get("rejections", 0))
        if rej >= 2 or n >= 3:
            hot = (n >= 5 or rej >= 3)
            prefix = ("ESCALATION — this loop has already burned "
                      f"{n} renditions. " if hot else "")
            lines.append(
                f"🛑 SPIRAL BRAKE (deterministic): '{s}' is at rendition {n} "
                f"with {rej} rejected take(s) this session. {prefix}Do NOT "
                "produce another variant. Allowed moves: (a) fresh crack from "
                "SOURCE INPUT with a different architecture, (b) ONE "
                "AskUserQuestion gut-check on the fork, (c) present existing "
                "takes for a pick, (d) /fresh-pen — compile a run packet and "
                "move the mission to a clean session (2 rejections on taste "
                "work = the pen is the problem). Name the rendition count to "
                "Farrice out loud.")
            if hot:
                _append_observe({
                    "ts": _now_iso_utc(), "session_id": session_id,
                    "exchange": count, "event": "spiral", "stem": s,
                    "renditions": n, "rejections": rej})
            break  # one brake per prompt — the loudest stem

    return ("\n".join(lines) + "\n") if lines else ""


def _cc_stop_observe(session_id: str, raw: str, exchange: int) -> None:
    """Observe-only: on a feedback-turn exchange, did the reply verify before
    producing (AskUserQuestion or a verdict-restate before the first
    Write/Edit)? Miss → observe log. Never raises, never blocks."""
    state = _cc_load()
    entry = state.get(session_id) or {}
    if int(entry.get("last_feedback_exchange") or 0) != exchange or not exchange:
        return

    last_user_idx = -1
    records = []
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except Exception:
            continue
        if not isinstance(rec, dict):
            continue
        records.append(rec)
        if rec.get("type") == "user":
            content = (rec.get("message") or {}).get("content")
            is_tool_result = isinstance(content, list) and any(
                isinstance(c, dict) and c.get("type") == "tool_result"
                for c in content)
            if not is_tool_result:
                last_user_idx = len(records) - 1

    asked = False
    produced = False
    restated = False
    for rec in records[last_user_idx + 1:]:
        if rec.get("type") != "assistant":
            continue
        content = (rec.get("message") or {}).get("content")
        if not isinstance(content, list):
            continue
        for item in content:
            if not isinstance(item, dict):
                continue
            if item.get("type") == "tool_use":
                name = str(item.get("name") or "")
                if name == "AskUserQuestion":
                    asked = True
                elif name in ("Write", "Edit") and not (asked or restated):
                    produced = True
            elif item.get("type") == "text":
                if re.search(r"\bverdicts?\b", str(item.get("text") or ""),
                             re.I) and not produced:
                    restated = True

    if produced and not (asked or restated):
        _append_observe({
            "ts": _now_iso_utc(), "session_id": session_id,
            "exchange": exchange, "event": "feedback-turn-blind-produce"})


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
    # ── Co-Creation Enforcement Layer (2026-07-28) ────────────────────────
    # Mode card + spiral brake + feedback-turn protocol. When a work mode
    # resolves, its card REPLACES the generic PARTNER-dial text below (the
    # specific instruction wins; injection stays compact). Fail-safe.
    cc_block = ""
    try:
        if not _cc_off():
            cc_block = _cc_prompt_block(session_id, prompt, count)
    except Exception:
        cc_block = ""

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
        # Amnesty 2026-07-29: compressed + now respects the co-creation off
        # switch (previously CO_CREATION_OFF re-enabled this longer block —
        # the off switch ADDED words; the trap is fixed here).
        if (_taste or _foggy) and not _execute and not cc_block and not _cc_off():
            co_creation = (
                "CO-CREATION (taste-bearing/foggy ask): load memory + canonical "
                "files first (FARRICE-MASTER-CONTEXT.md for identity/voice/offer); "
                "ask ONE question past his frame before producing; two rejected "
                "takes = back to source input. 'Just do it' = EXECUTE dial.\n")
    except Exception:
        co_creation = ""

    # ── Bound injector (Model-Dialect Adaptation Layer, 2026-07-28) ───────
    # Injects the ACTIVE model's pathology corrections (from its dialect
    # card's machine-dialect block) for this prompt's class. Fail-safe: any
    # problem = empty string, never a broken session.
    dialect = ""
    try:
        dialect = _dialect_block(payload, prompt)
    except Exception:
        dialect = ""

    # Compass retune (Farrice, 2026-07-28): Next Moves reminder fires only on
    # deliverable-classified exchanges. Amnesty 2026-07-29 (LEAN ruling):
    # compressed to one line — the spec lives in directives/steering-loop.md.
    steering = ""
    if _dialect_class(prompt) == "deliverable":
        steering = (
            f"STEERING LOOP (exchange {count}): ships something → close with "
            "Next Moves (Deepen/Adjacent/Act) + 1-line Operator Lesson; skip "
            "on answers, diagnostics, corrections (directives/steering-loop.md). "
            "Forge Radar: repeated problem/missing tool → flag in ONE line, "
            "never block.\n")
    # Amnesty 2026-07-29: tip fires 1-in-5 prompts, not every prompt.
    tip = ""
    if count % 5 == 1:
        tip = f"Harness tip: {TIPS[(count - 1) % len(TIPS)]}"
    block = (cc_block + co_creation + dialect + steering + tip).rstrip()
    if block:
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

    state = _load_state()
    exchange = 0
    try:
        exchange = int((state.get(session_id) or {}).get("count", 0))
    except Exception:
        exchange = 0

    # Co-Creation feedback-turn observer (2026-07-28, observe-only) — runs
    # regardless of Next-Moves compliance, BEFORE the early exits below.
    try:
        if not _cc_off():
            _cc_stop_observe(session_id, raw, exchange)
    except Exception:
        pass

    if not found_any or len(last_text) < 400:
        sys.exit(0)

    if "next moves" in last_text.lower():
        sys.exit(0)

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

        if mode == "test-mirror":
            sample = sys.stdin.read()
            wm = _cc_work_mode(sample, False)
            block = _mirror_block(sample, wm)
            print(f"work-mode: {wm} | signals: {_mirror_signals(sample)} | "
                  f"fires: {'YES' if block else 'no'}")
            if block:
                print(block)
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
