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
import subprocess
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


def _under_codex(payload: dict) -> bool:
    """True when the hook is being fired by Codex (the runner sets
    CODEX_PROJECT_DIR; the Desktop app sets CODEX_HOME/CODEX_CLI_PATH).
    Claude Code sets none of these."""
    # The Codex runner (.codex/tools/codex_hook_runner.py) sets these two;
    # Claude Code sets neither. They win over any inherited shell state.
    if os.environ.get("ANTIGRAVITY_HARNESS", "").lower() == "codex":
        return True
    if os.environ.get("CODEX_PROJECT_DIR"):
        return True
    if str(payload.get("harness") or "").lower() == "codex":
        return True
    if os.environ.get("CLAUDE_CODE_ENTRYPOINT"):
        return False
    return bool(os.environ.get("CODEX_HOME") or os.environ.get("CODEX_CLI_PATH"))


def _codex_config_model() -> str:
    """Read `model = "..."` from the Codex config: repo `.codex/config.toml`
    overrides `~/.codex/config.toml`. Plain regex, no toml dependency."""
    candidates = [REPO_ROOT / ".codex" / "config.toml",
                  Path.home() / ".codex" / "config.toml"]
    for cfg in candidates:
        try:
            text = cfg.read_text(errors="replace")
        except Exception:
            continue
        mm = re.search(r'^\s*model\s*=\s*"([^"]+)"', text, re.M)
        if mm:
            return mm.group(1).strip()
    return ""


def _active_model(payload: dict) -> str:
    """Resolve the ACTIVE model id. Order: payload → env → transcript →
    cache → default seat. Never raises. Under Codex (2026-09-09, the
    gpt-6-astra port): payload → Codex config.toml → "" (honest silence —
    the Claude default seat must never inject an Opus card at a GPT model)."""
    m = payload.get("model")
    if isinstance(m, dict):
        m = m.get("id") or m.get("model")
    if _under_codex(payload):
        if not m:
            m = _codex_config_model()
        return str(m or "")
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
                if pat and model_id and str(pat) in model_id:
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
    r"\bmode (build-new|refine-existing|ideate|decide|capture|job-handoff)\b", re.I)


# ── Job-shaped handoff detector (2026-09-09, Nate B Jones manager loop) ──
# Fires on the ask that is bigger than a prompt: a delegation verb + breadth
# (several deliverables, several systems, or a sequence). The card it emits is
# the brief — the manager loop runs until job_board.py says MAY END. Scar:
# 54 open missions, oldest 41d, compiled by /go and never driven. Deterministic,
# nudge-not-cage; `mode job-handoff` forces it, feedback turns never reach it.
_JOB_VERB_RE = re.compile(
    r"\b(handle|take care of|own (this|it)|run (this|it|the whole|the entire)|"
    r"end.to.end|soup to nuts|from start to finish|see it through|"
    r"until (it'?s |it is )?done|get (this|it|all of (this|it)) done|make (this|it) happen|"
    r"hand(ing)? (this|it|that) (off|over)|hands.off|manage (it|this|yourself)|"
    r"go (out|off) and|cover (all|every) (the )?gaps?|take (this|it) (from here|over)|"
    r"set (you|fable|astra|codex) (off|loose) on)\b")
_JOB_SYSTEM_RE = re.compile(
    r"\b(linkedin|substack|notion|gmail|email|calendar|shopify|github|codex|claude code|"
    r"website|drive|stripe|canva|instagram|youtube|dropbox|airtable|slack|harness|"
    r"the repo|worktree|homebase)\b")
_JOB_SEQ_RE = re.compile(
    r"\b(then|after that|once .{0,40}?(done|ready|approved)|finally|first .{0,60}? then|"
    r"step (one|two|1|2)|phase (one|two|1|2))\b")


def _job_shaped(pl: str) -> bool:
    """A job-shaped ask: ≥200 chars, a delegation verb, and breadth ≥2 of
    {≥2 deliverable words, ≥2 systems, ≥2 sequence markers}. Never fires on a
    bare `run <workflow>`."""
    if len(pl) < 200 or re.match(r"^\s*run \S+\s*$", pl):
        return False
    if not _JOB_VERB_RE.search(pl):
        return False
    deliverables = {m.group(0) for m in _DELIVERABLE_RE.finditer(pl)}
    systems = {m.group(0) for m in _JOB_SYSTEM_RE.finditer(pl)}
    seq = _JOB_SEQ_RE.findall(pl)
    breadth = (len(deliverables) >= 2) + (len(systems) >= 2) + (len(seq) >= 2)
    return breadth >= 2


# ── Explicit /job invocation (2026-09-11, JJ-3 invitation scar) ──────────
# `[$job](…SKILL.md)` + a short ask + an image on Codex: the card above only
# fired on the ≥200-char heuristic, and `_cc_prompt_block` returns "" for any
# "/" prompt — so an EXPLICIT /job got no card at all. Astra read the skill
# prose and went straight to Photoshop: no board entry, no plan, no questions
# (`job-plan-not-shown` logged 8× on the Cooz job, read by nobody). Explicit
# invocation now always fires, the hook does the deterministic pre-work (recipe
# match + open jobs) so the first tool call is `open`, and last turn's observer
# events are relayed as one visible line. Nudge, never a cage.
_JOB_EXPLICIT_RE = re.compile(
    r"(?:^|\n|## My request:)\s*(?:<command-message>job</command-message>\s*"
    r"<command-name>/job</command-name>\s*(?:<command-args>)?|\[\$job\]\([^)]*\)|"
    r"\$job\b|/job\b|job:)\s*", re.I)
_JOB_SUBCMD_RE = re.compile(
    r"^(resume|status|next|packet|handoff|close|recipes|plan|trace|go|lanes|log)\b", re.I)
_JOB_TASTE_RE = re.compile(
    r"\b(invitation|invite|design|logo|poster|flyer|banner|layout|mockup|copy|headline|"
    r"hook|voice|tagline|caption|script|visual|illustration|thumbnail|brand look|"
    r"party pack|carousel|reel)\b", re.I)
_JOB_SLUG_STOP = {"the", "a", "an", "and", "for", "with", "this", "that", "into", "from", "of",
                  "to", "my", "our", "i", "we", "you", "it", "is", "are", "be", "need", "want",
                  "us", "on", "in", "me", "please", "can", "could", "would", "like", "get",
                  "make", "just", "then", "there", "here", "have", "has", "all", "some"}


def _explicit_job(prompt: str):
    """(is_explicit, subcommand|None, ask) — the ask with every $skill mention stripped."""
    m = _JOB_EXPLICIT_RE.search(prompt or "")
    if not m:
        return False, None, ""
    rest = prompt[m.end():]
    rest = re.sub(r"\[\$[\w-]+\]\([^)]*\)|\$[\w-]+\b", " ", rest)
    rest = re.sub(r"</?command-args>", " ", rest)
    rest = " ".join(rest.split())
    sm = _JOB_SUBCMD_RE.match(rest)
    return True, (sm.group(1).lower() if sm else None), rest


def _job_slug_suggestion(ask: str) -> str:
    words = [w for w in re.findall(r"[a-z0-9]+", ask.lower()) if w not in _JOB_SLUG_STOP]
    return "-".join(words[:4]) or "new-job"


def _job_prework_block(prompt: str) -> list[str]:
    """Deterministic pre-work for a job turn: recipe match verdict, open jobs that
    look like this ask, slug suggestion, the exact first command, taste shape check."""
    explicit, sub_, ask = _explicit_job(prompt)
    if not explicit:
        ask = " ".join((prompt or "").split())
    if sub_:
        return [f"JOB CONTINUE (explicit /job {sub_}): FIRST tool call this turn = "
                f"`python3 execution/job_board.py {sub_} …` (resume reloads from disk, never from "
                "the transcript); the reply is its output plus every LANE RECEIPT and packet this "
                "turn produces; end only on MAY END."]
    exe = Path(__file__).resolve().parents[1]
    out = ["JOB PRE-WORK (deterministic — the hook already ran these; do not skip to the work):"]
    try:
        r = subprocess.run([sys.executable, str(exe / "recipe_cards.py"), "match", ask[:600], "--json"],
                           capture_output=True, text=True, timeout=8, cwd=str(REPO_ROOT))
        d = json.loads(r.stdout or "{}")
        v = d.get("verdict") or {}
        rows = d.get("rows") or []
        top = rows[0] if rows else None
        if top and v.get("confident"):
            out.append(f"  recipe: CONFIDENT MATCH {top['slug']} ({v.get('reason', '')}) → open on it")
        elif top:
            out.append(f"  recipe: WEAK MATCH (top {top['slug']} score {top.get('score')}; {v.get('reason', '')}) "
                       f"→ FORGE a card first (recipes/<slug>.md with Ask-me-first filled, "
                       f"recipe-card-forge.md); never run {top['slug']}'s lanes on this ask")
        else:
            out.append("  recipe: no match → forge a card first (recipe-card-forge.md)")
    except Exception:
        out.append("  recipe: matcher unavailable → run python3 execution/recipe_cards.py match \"<ask>\"")
    try:
        r = subprocess.run([sys.executable, str(exe / "job_board.py"), "status", "--json"],
                           capture_output=True, text=True, timeout=8, cwd=str(REPO_ROOT))
        jobs = [j for j in json.loads(r.stdout or "[]")
                if j.get("status") not in ("complete", "closed", "parked")]
        terms = set(re.findall(r"[a-z]{4,}", ask.lower())) - _JOB_SLUG_STOP
        hits = []
        for j in jobs:
            jt = set(re.findall(r"[a-z]{4,}", ((j.get("slug") or "") + " " + (j.get("recipe") or "")).replace("-", " ")))
            if len(terms & jt) >= 2:
                hits.append(j["slug"])
        if hits:
            out.append("  open jobs that look like this ask: " + ", ".join(hits) +
                       " → CONTINUE that one (python3 execution/job_board.py resume <slug>); never open a second job for it")
        elif jobs:
            out.append(f"  open jobs: {len(jobs)} ({', '.join(j['slug'] for j in jobs[:5])}) — none match this ask; a new job is right")
        else:
            out.append("  open jobs: none")
    except Exception:
        pass
    out.append(f"  slug suggestion: {_job_slug_suggestion(ask)}")
    out.append("  FIRST tool call this turn = `python3 execution/job_board.py open <slug> --recipe <recipe> "
               "--goal \"<his outcome sentence>\" [--found \"<path>: <answer>\" …] [--ask \"<question>\" …]` "
               "— the JOB PLAN it prints IS the reply, carrying an INTERVIEW block (Found on disk: … / "
               "Questions: … or 'none, because …'). No file is touched and no lane runs before that plan "
               "is on screen; the turn ends at PLAN PENDING.")
    if _JOB_TASTE_RE.search(ask):
        out.append("  Shape check: this reads as TASTE work (design/copy/voice). Still open the board — it is "
                   "the trace — but run the lanes as visible beats (one take → his verdict → next), never "
                   "hands-off; /jam is the right engine for the taste lanes.")
    return out


def _job_context_line(prompt: str) -> str:
    """One line carrying the open job into a PLAIN prompt (no /job typed): a pending
    plan (his reply is probably the go), open packets (record the answer), runnable
    lanes (this is not new work). Answers "do I have to fire /job every time?" — no:
    the board follows him. Jobs touched in the last 24h only; never on a /job prompt."""
    try:
        if _explicit_job(prompt)[0] or (prompt or "").strip().startswith(("/", "@")):
            return ""
        exe = Path(__file__).resolve().parents[1]
        r = subprocess.run([sys.executable, str(exe / "job_board.py"), "status", "--json"],
                           capture_output=True, text=True, timeout=8, cwd=str(REPO_ROOT))
        jobs = [j for j in json.loads(r.stdout or "[]") if j.get("status") not in ("complete", "closed", "parked")]
        now = datetime.now(timezone.utc)
        parts = []
        # most recently written job first — the one he is most likely replying to
        jobs.sort(key=lambda j: str(j.get("last") or "").split(" ")[0], reverse=True)
        for j in jobs:
            last = str(j.get("last") or "")
            try:
                ts = datetime.fromisoformat(last.split(" ")[0].strip())
                if ts.tzinfo is None:
                    ts = ts.astimezone()
                if (now - ts).total_seconds() > 86400:
                    continue
            except Exception:
                continue
            s = j.get("slug")
            if j.get("plan") == "pending":
                parts.append(f"{s}: PLAN PENDING — if this reply is his go/edit: `python3 execution/job_board.py go {s} --note \"<his words>\"` then run the lanes")
            elif int(j.get("packets") or 0) > 0:
                parts.append(f"{s}: {j['packets']} packet(s) open — if this reply answers one: `python3 execution/job_board.py packet {s} answer <n> \"<his words>\"`, unblock, continue")
            elif int(j.get("runnable") or 0) > 0:
                parts.append(f"{s}: {j['runnable']} runnable lane(s) — this is not new work: `python3 execution/job_board.py next {s}` and keep the loop moving")
        if not parts:
            return ""
        return "JOB CONTEXT (board, deterministic): " + " · ".join(parts[:3]) + "\n"
    except Exception:
        return ""


def _job_observer_relay(session_id: str, since_iso: str) -> str:
    """One visible line for last turn's job observer events (plan never shown / turn
    ended with runnable lanes and no packet). Scar 2026-09-11: eight
    job-plan-not-shown events on one job, read by nobody."""
    try:
        if not OBSERVE_LOG.exists():
            return ""
        since = None
        if since_iso:
            try:
                since = datetime.fromisoformat(since_iso)
                if since.tzinfo is None:
                    since = since.astimezone()
            except Exception:
                since = None
        now = datetime.now(timezone.utc)
        hits = {}
        for ln in OBSERVE_LOG.read_text(errors="replace").splitlines()[-300:]:
            try:
                rec = json.loads(ln)
            except Exception:
                continue
            ev = rec.get("event")
            if ev not in ("job-plan-not-shown", "job-turn-ended-unblocked"):
                continue
            if rec.get("session_id") != session_id:
                continue
            try:
                ts = datetime.fromisoformat(rec.get("ts", ""))
                if ts.tzinfo is None:
                    ts = ts.astimezone()
            except Exception:
                continue
            if since is not None and ts <= since:
                continue
            if (now - ts).total_seconds() > 86400:
                continue
            hits[(rec.get("job") or "?", ev)] = rec
        if not hits:
            return ""
        parts = []
        for job, ev in hits:
            if ev == "job-plan-not-shown":
                parts.append(f"{job}: the JOB PLAN was never shown → show it now "
                             f"(python3 execution/job_board.py plan {job}) and wait for his go")
            else:
                parts.append(f"{job}: last turn ended with runnable lanes and no packet → continue them "
                             f"(python3 execution/job_board.py next {job}) or write the packet")
        return "⚠ LAST TURN (job observer, deterministic): " + " · ".join(parts) + "\n"
    except Exception:
        return ""


def _cc_work_mode(prompt: str, is_feedback: bool):
    """JOB-HANDOFF | BUILD-NEW | REFINE-EXISTING | IDEATE | DECIDE | CAPTURE | None."""
    pl = prompt.lower().strip()
    m = _CC_MODE_OVERRIDE_RE.search(pl)
    if m:
        return m.group(1).upper()
    if _explicit_job(prompt)[0]:
        return "JOB-HANDOFF"
    if is_feedback:
        return "REFINE-EXISTING"
    if _job_shaped(pl):
        return "JOB-HANDOFF"
    if re.search(r"\b(should (i|we)|which (one|of these|way|take)|pick (one|a|the)|"
                 r"choose|decide|gut.?check|or should)\b", pl):
        return "DECIDE"
    if re.search(r"\b(ideas?|angles?|options|variations?|brainstorm|riff|ideate|"
                 r"ways we could)\b", pl):
        return "IDEATE"
    if _DELIVERABLE_RE.search(pl):
        return "BUILD-NEW"
    # 2026-09-09 scar (Madison/DSC session on Codex): a long approval of a
    # brief ("This does match the scope and brief… I want to send them
    # something now") classified as CAPTURE, and Astra obeyed the card to
    # the letter — ran thought_bank capture, replied "Captured verbatim",
    # did nothing. An approval, a go, or a stated want is an instruction to
    # act, never a dump. Those words route to BUILD-NEW; CAPTURE keeps only
    # the genuine reflective dump.
    if _CC_APPROVAL_RE.search(pl):
        return "BUILD-NEW"
    if len(pl) > 400 and "?" not in pl and not re.search(
            r"\b(can you|please|need you|help me)\b", pl):
        return "CAPTURE"
    return None


# Strong approval / go signals only — a reflective dump can say "make it
# smaller" or "I want to be visible"; those are not instructions to act.
_CC_APPROVAL_RE = re.compile(
    r"(\bmatch(es)? the (scope|brief)\b|\bapproved\b|\bgo ahead\b|\bproceed\b|"
    r"\bexecute\b|\bship it\b|\bjust do it\b|\blet'?s (go|do this|build|send|start)\b|"
    r"\b(i|we) want (you|us) to\b|\bi want to send\b|\bthis is it[.!]|"
    r"\bperfect[.!]|^yes[.!,]|\byes,? (do|go|send|build)\b)")


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


# JOB-HANDOFF cards — one per harness (Astra follows cards literally, 2026-09-09
# scar: a Claude-shaped "dispatch an executor" line becomes a full stop on Codex).
_JOB_CARDS = {
    "claude": (
        "Job-shaped ask → /job (Nate manager loop): match a recipe "
        "(python3 execution/recipe_cards.py match \"<ask>\") — a WEAK MATCH means forge a "
        "card from the workflows that already run the job, never run the matched card's "
        "lanes; interview ONCE (batched, ≤5 questions, disk-first, only what changes "
        "execution); python3 execution/job_board.py open — it prints a JOB PLAN; THE OPENING "
        "TURN'S REPLY IS THAT PLAN (goal, lanes as what-I'll-do, questions, approvals) and "
        "the turn ends there; lanes start next turn after `job_board.py go <slug>` records "
        "his nod (`open --go` only when he said 'just do it'). Then run the manager loop — "
        "keep every unblocked lane moving (writes = you, serial; read-only lanes = "
        "background Sonnet seats carrying the negative brief), close every lane with "
        "`lane … --status --did \"what was done / found / skipped\" --evidence` and ECHO its "
        "LANE RECEIPT line in the reply, batch questions into DECISION PACKETS "
        "(job_board.py packet add), and END THE TURN ONLY when `job_board.py next` prints "
        "MAY END. Deliver plan → receipts → packets, never bare status. This card IS the "
        "brief — no separate brief card, no fresh-pen dispatch."),
    "codex": (
        "Job-shaped ask → /job (Nate manager loop; single seat): match a recipe "
        "(python3 execution/recipe_cards.py match) — WEAK MATCH = forge a card, never run "
        "the matched card's lanes; interview ONCE (batched, ≤5, disk-first); python3 "
        "execution/job_board.py open — it prints a JOB PLAN; REPLY WITH THAT PLAN AND END "
        "THE TURN (lanes start only after `job_board.py go <slug>` records his nod; "
        "`open --go` only when he said 'just do it'). After go: run the lanes IN ORDER OF "
        "READINESS IN THIS TURN — a lane that ends in a diagnosis is not done: build it, or "
        "mark it `--status blocked --blocker \"<decision needed>\"` with a DECISION PACKET; "
        "close every lane with `--did \"what was done / found / skipped\" --evidence` and "
        "ECHO its LANE RECEIPT line; end the turn only when `job_board.py next` prints MAY "
        "END, closing with the packets + receipts. This card IS the brief."),
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
    """The intent mirror — UNIVERSAL since 2026-08-03 (Farrice: 'locked
    universally… I waste so much time going back and forth because my intent
    isn't clear sometimes, and then we're just taking misaligned action').

    Two intensities:
    - raw dump (2+ vomit signals) → full ≤5-line mirror + ONE push-back
    - any other substantive ask → compact 1-3 line mirror; push-back only
      when a real fork is live; sharp ask = one line and go.
    Skips: short/conversational (<120 chars), CAPTURE (dumps park verbatim),
    REFINE-EXISTING (its card already mandates restating his verdicts —
    that IS the mirror for feedback turns).
    """
    if len(prompt.strip()) < 120 or mode in ("CAPTURE", "REFINE-EXISTING", "JOB-HANDOFF"):
        return ""
    # 2026-09-09 (Madison/DSC scar, Codex): when he has CONFIRMED a brief
    # ("this does match the scope and brief… execute"), the confirm beat is
    # over. Re-issuing the INTENT BRIEF card here told Astra to compile
    # another brief and wait — the echo he saw. Approval = execute now.
    if _CC_APPROVAL_RE.search(prompt.lower()):
        return (
            "✅ BRIEF CONFIRMED (his words): the confirm beat is done. Execute "
            "the brief in THIS turn — no new brief, no re-mirror beyond one "
            "line, no capture. Fold any refinement he added into the work and "
            "end with the artifact path + receipts.")
    if _mirror_signals(prompt) >= 2:
        # Upgraded 2026-08-20 (Farrice, approved plan "Intent Brief Default"):
        # raw intent → compiled brief → his confirm → fresh-context execution.
        # He self-diagnosed: best work in planning mode, worst on free-run;
        # blind A/B proved quality = settled brief + clean head, not model.
        return (
            "📋 INTENT BRIEF (raw ask — 2026-08-20 ruling): do NOT produce "
            "yet. Compile a ≤10-line brief from his raw intent — Deliverable+"
            "size · Outcome/felt standard · Constraints · Sources to load · "
            "Taste bar (voice/register rules in play) · Pen seat (Executor "
            "Registry) · Open questions (ONLY ones that change execution) — "
            "and present it for confirm/edit, plus ONE senior-partner "
            "push-back if a real fork is live. "
            + ("On his confirm or edit: execute the brief YOURSELF in the "
               "next turn, in full, to a file (Codex: no executor dispatch, "
               "no subagent you wait on); he iterates on the FINAL product — "
               "rejection = fix the brief, rewrite from it. \"Just do it\" = "
               "skip the confirm beat."
               if _CODEX else
               "On his confirm or edit: artifact-shaped work dispatches to "
               "ONE fresh-context executor carrying \"no Chain, no finalize, "
               "no Notion, no Next Moves, return only the artifact\"; he "
               "iterates on the FINAL product — rejection = fix the brief, "
               "dispatch fresh, never iterate in-thread. \"Just do it\" = "
               "skip the confirm beat, never the fresh dispatch."))
    return (
        "🪞 INTENT MIRROR (universal — every substantive ask): open the reply "
        "with a 1-3 line mirror of what you're reading — deliverable · "
        "standard · the constraint that matters — plus ONE push-back if any "
        "real fork is live. If the ask is sharp, one line (\"reading this as "
        "X — proceeding\") and go. Misalignment dies at line one, never at "
        "deliverable three.")


def _cc_prompt_block(session_id: str, prompt: str, count: int) -> str:
    """Assemble mode card + spiral brake; update rejection state. Never raises."""
    # Slash/system commands already name their route — a mode card is redundant
    # and the brake is noise there (live-fire calibration, first firing was on
    # /end-session). Bare-name workflow invocations still pass through.
    if prompt.strip().startswith(("/", "@")) and not _explicit_job(prompt)[0]:
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
        if mode == "JOB-HANDOFF":
            card = _JOB_CARDS["codex" if _CODEX else "claude"]
        lines.append(f"MODE {mode} (say 'mode X' to override): {card}".rstrip())
        if mode == "JOB-HANDOFF":
            try:
                lines.extend(_job_prework_block(prompt))
            except Exception:
                pass

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
            moves = (
                "(a) fresh crack from SOURCE INPUT with a different "
                "architecture, (b) ONE question to Farrice on the fork, (c) "
                "present existing takes for a pick, (d) restart from the "
                "source in a clean thread with the brief rewritten (2 "
                "rejections on taste work = the brief is the problem)."
                if _CODEX else
                "(a) fresh crack from SOURCE INPUT with a different "
                "architecture, (b) ONE AskUserQuestion gut-check on the fork, "
                "(c) present existing takes for a pick, (d) /fresh-pen — "
                "compile a run packet and move the mission to a clean session "
                "(2 rejections on taste work = the pen is the problem).")
            lines.append(
                f"🛑 SPIRAL BRAKE (deterministic): '{s}' is at rendition {n} "
                f"with {rej} rejected take(s) this session. {prefix}Do NOT "
                f"produce another variant. Allowed moves: {moves} Name the "
                "rendition count to Farrice out loud.")
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
_CODEX = False  # set per prompt by handle_prompt; card text adapts to the harness


def handle_prompt(payload: dict) -> None:
    global _CODEX
    _CODEX = _under_codex(payload)
    session_id = payload.get("session_id") or "unknown"
    prompt = payload.get("prompt") or ""

    state = _load_state()
    entry = state.get(session_id) or {"count": 0, "updated": ""}
    prev_updated = str(entry.get("updated") or "")
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
            if _CODEX:
                # Astra already over-asks (OpenAI's Astra guide); a question
                # gate before producing turns into a clarification stall.
                co_creation = (
                    "CO-CREATION (taste-bearing/foggy ask): load memory + canonical "
                    "files first (FARRICE-MASTER-CONTEXT.md for identity/voice/offer); "
                    "state the ONE assumption that matters in a line, then produce; "
                    "two rejected takes = back to source input.\n")
            else:
                co_creation = (
                    "CO-CREATION (taste-bearing/foggy ask): load memory + canonical "
                    "files first (FARRICE-MASTER-CONTEXT.md for identity/voice/offer); "
                    "ask ONE question past his frame before producing; two rejected "
                    "takes = back to source input. 'Just do it' = EXECUTE dial.\n")
    except Exception:
        co_creation = ""

    # ── Fresh Pen Protocol (Farrice 2026-08-20) ───────────────────────────
    # Blind 3-seat A/B proved artifact quality comes from a clean one-shot
    # brief executed in a FRESH context, not from the conversation seat
    # (scar: 2026-07-27 eight in-thread headline rounds; ruling: 2026-08-20
    # "Take B" test, dialect card § Fable-Seat Re-probe). Nudge, not cage:
    # "just do it" skips the veto beat, never the fresh dispatch.
    fresh_pen = ""
    try:
        # Suppress when the INTENT BRIEF card already fired this prompt —
        # that card carries the same dispatch rule (approved plan 2026-08-20).
        if _CODEX and "INTENT BRIEF" not in cc_block and "MODE JOB-HANDOFF" not in cc_block and _CC_APPROVAL_RE.search(prompt.lower()) is None:
            # Codex has no Opus/Sonnet executor seat. The Claude FRESH PEN
            # card ("never produce in-thread, dispatch an executor") made
            # Astra spawn a subagent and wait_agent-timeout twice (Madison/
            # DSC, 2026-09-09). On Codex the model IS the pen.
            _pl = prompt.lower()
            if re.search(
                r"\b(write|draft|ghostwrite|rewrite|revise|produce|generate|"
                r"build)\b.{0,60}\b(post|copy|email|edition|newsletter|caption|"
                r"script|headline|hook|bio|carousel|about section|sales page|"
                r"landing|opener|thread|article|essay|brief|report|analysis|"
                r"doc|deck|page|plan|extraction|one.?pager|proposal)\b", _pl):
                fresh_pen = (
                    "PEN (Codex): you are the pen. Write the artifact yourself in "
                    "THIS turn, to a file; no executor dispatch, no subagent you "
                    "then wait on. A subagent only for independent research you "
                    "do not block on.\n")
        elif "INTENT BRIEF" not in cc_block and "MODE JOB-HANDOFF" not in cc_block:
            _pl = prompt.lower()
            _pen_execute = re.search(
                r"\b(just do it|just run|go ahead|proceed|ship it|no questions|"
                r"execute)\b", _pl)
            _artifact = re.search(
                r"\b(write|draft|ghostwrite|rewrite|revise|produce|generate|"
                r"build)\b.{0,60}\b(post|copy|email|edition|newsletter|caption|"
                r"script|headline|hook|bio|carousel|about section|sales page|"
                r"landing|opener|thread|article|essay|brief|report|analysis|"
                r"doc|deck|page|plan|extraction|one.?pager)\b"
                r"|\b(linkedin post|cold email|substack edition|listing copy|"
                r"research brief)\b", _pl)
            if _artifact and _pen_execute:
                fresh_pen = (
                    "FRESH PEN (execute dial): skip the veto beat — compile "
                    "the brief silently and dispatch the fresh-context "
                    "executor (seat per Executor Registry, negative brief) "
                    "now; still never produce the artifact in-thread.\n")
            elif _artifact:
                fresh_pen = (
                    "FRESH PEN PROTOCOL (artifact-shaped ask — 2026-08-20 "
                    "blind-test ruling): do NOT produce the artifact in this "
                    "thread. Compile the ≤10-line brief (deliverable+size · "
                    "outcome · constraints · sources · taste bar · pen seat · "
                    "open questions), show it for a quick veto, then dispatch "
                    "ONE fresh-context executor seated per "
                    "directives/orchestration-doctrine.md Executor Registry "
                    "(creative prose: Opus 5, blind-verified 2026-08-20; "
                    "mechanical/grind: Sonnet 5) carrying \"no Chain, no "
                    "finalize, no Notion, no Next Moves, return only the "
                    "artifact\". Rejected take → fix the BRIEF and dispatch "
                    "fresh; never iterate the same executor in-thread.\n")
    except Exception:
        fresh_pen = ""

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
    if count % 5 == 1 and not _CODEX:  # tips are Claude-flavored (Fable/Sonnet seats)
        tip = f"Harness tip: {TIPS[(count - 1) % len(TIPS)]}"
    relay = ""
    try:
        relay = _job_observer_relay(session_id, prev_updated)
    except Exception:
        relay = ""
    jobctx = ""
    try:
        if "MODE JOB-HANDOFF" not in cc_block:
            jobctx = _job_context_line(prompt)
    except Exception:
        jobctx = ""
    block = (relay + jobctx + cc_block + co_creation + fresh_pen + dialect + steering + tip).rstrip()
    if block:
        print(block)
    sys.exit(0)


# ──────────────────────────────────────────────────────────────────
# stop (Stop — observe only)
# ──────────────────────────────────────────────────────────────────

def _job_stop_observe(session_id: str, last_text: str, exchange: int) -> None:
    """Observe-only (2026-09-09, manager loop): when an open job still has a
    runnable lane and the turn ended without a DECISION PACKET, log it. Never
    blocks — the log is what makes the "hand it back every turn" habit visible."""
    try:
        board = Path(__file__).resolve().parents[1] / "job_board.py"
        if not board.exists():
            return
        # 2026-09-10: ask the board for the open jobs — it resolves to the MAIN
        # checkout's state from any lane, so this observer sees the same board
        # every session sees (a lane-local directory scan missed jobs opened elsewhere)
        raw = subprocess.run([sys.executable, str(board), "status", "--json"],
                             capture_output=True, text=True, timeout=15).stdout
        try:
            jobs = [j for j in json.loads(raw or "[]") if j.get("status") not in ("complete", "closed", "parked")]
        except Exception:
            jobs = []
        if not jobs:
            return
        for j in jobs:
            name = j.get("slug") or ""
            if not name:
                continue
            out = subprocess.run([sys.executable, str(board), "next", name],
                                 capture_output=True, text=True, timeout=10).stdout
            if "TURN MUST CONTINUE" in out and "DECISION PACKET" not in (last_text or ""):
                _append_observe({
                    "ts": _now_iso_utc(), "session_id": session_id, "exchange": exchange,
                    "event": "job-turn-ended-unblocked", "job": name,
                    "runnable": out.splitlines()[0][:160] if out else "",
                })
            # 2026-09-10: a job whose plan is still pending must have been SHOWN — the
            # reply carries the JOB PLAN block. Observe-only, like everything here.
            if out.startswith("PLAN PENDING") and "JOB PLAN" not in (last_text or ""):
                _append_observe({
                    "ts": _now_iso_utc(), "session_id": session_id, "exchange": exchange,
                    "event": "job-plan-not-shown", "job": name,
                })
    except Exception:
        return

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

    # Manager-loop observer (2026-09-09): a job turn that ended with runnable
    # lanes and no DECISION PACKET is the exact habit this build exists to end.
    try:
        _job_stop_observe(session_id, last_text, exchange)
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
