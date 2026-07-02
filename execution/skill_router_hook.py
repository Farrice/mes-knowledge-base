#!/usr/bin/env python3
"""skill_router_hook.py — UserPromptSubmit hook for deterministic skill routing.

WHY THIS EXISTS (the core fix):
Routing to skills used to be 100% dependent on Claude *remembering* to do it —
no prompt-time trigger, no script, just "the Chain says route." That violates the
project's own hard rule (feedback_ai-memory-dependent-observability): never ship
infra that depends on Claude remembering, always pair with a deterministic backstop.

This hook IS that backstop. It runs on every prompt the user submits, BEFORE Claude
reasons, matches the prompt against the skill registry (BM25 via find_skill.py), and
injects the top matches + their slash commands as context. Claude then sees "for THIS
request, these expert skills exist" every single turn — routing stops being memory and
becomes a deterministic suggestion.

DESIGN PRINCIPLES:
- FAIL-SAFE: any error -> exit 0, inject nothing. Never break the user's prompt.
- QUIET ON TRIVIAL: skips short prompts, prompts that already name a skill/slash
  command, and obvious system/conversational turns — no noise when routing is moot.
- SUGGEST, DON'T FORCE: it surfaces options; Claude still decides. (Top match can be
  wrong; showing top-3 + leaving the call to Claude mitigates that.)

Wired via .claude/settings.local.json -> hooks.UserPromptSubmit.
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT / "execution") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "execution"))

from control_intent import classify_control_intent  # noqa: E402

REPEATABILITY_CONTROL_TERMS = (
    "copied over everything",
    "copied everything over",
    "copying everything over",
    "previous session import",
    "import from my previous session",
    "import from previous session",
    "golden sample",
    "cannot repeat",
    "can't repeat",
    "lost the magic",
    "revision got worse",
    "got worse again",
)

SYSTEM_CONTROL_TERMS = (
    "claude code works better",
    "not working like claude code",
    "codex vs claude code",
    "codex compared to claude code",
    "match claude code",
    "mirror claude code",
    "claude parity",
    "claude-parity",
    "blocking hooks",
    "blocked hooks",
    "hooks not firing",
    "hooks are not firing",
    "wrong defaults",
    "wrong default",
    "wrong default routing",
    "routing wrong defaults",
    "routing the wrong defaults",
    "default routing",
    "default settings",
    "default setting",
    "things that are not wired",
    "not wired",
    "should not be wired",
    "shouldn't be wired",
    "wired together",
    "not wired together",
    "should not be wired together",
    "shouldn't be wired together",
    "wiring",
    "hook wiring",
    "route wiring",
    "routing wiring",
    "hooks or routes",
    "hooks and routes",
    "routes and hooks",
    "handcuffed",
    "handcuff",
    "handcuffed and chained",
    "handcuffed and chained together",
    "chained together",
    "chained",
    "things being chained together",
    "routes are being handcuffed",
    "hooks are being handcuffed",
    "should not be chained",
    "shouldn't be chained",
    "full audit or check and repair",
    "audit or check and repair",
    "check and repair",
    "audit and repair",
    "things that have no business being the default",
    "things that shouldn't be the default",
    "thin wrappers",
    "too many thin wrappers",
    "specific things blocking performance",
    "blocking performance",
    "complete errors and issues",
    "running into complete errors",
    "running into walls",
    "without breaking my workspace",
    "without breaking claude code",
    "without breaking my claude code workspace",
    "not trying to break anything",
    "codex is not working",
    "codex not working",
    "codex feels ineffective",
)

EXPERT_TASK_TERMS = (
    "write",
    "draft",
    "create",
    "generate",
    "build",
    "design",
    "make",
    "produce",
    "rewrite",
    "edit",
    "polish",
    "analyze",
    "audit",
    "review",
    "research",
    "develop",
    "compose",
    "turn",
    "convert",
    "script",
    "copy",
    "landing page",
    "website",
    "brand",
    "email",
    "post",
    "ad ",
    "ads",
    "offer",
    "funnel",
    "content",
    "brief",
    "asset",
    "campaign",
    "strategy",
    "deck",
    "slides",
    "page",
)


def _eprint(*a):
    print(*a, file=sys.stderr)


def _normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.lower()).strip()


def _control_route(prompt: str) -> tuple[str, str] | None:
    classified = classify_control_intent(prompt)
    if classified["route"]:
        return (str(classified["route"]), str(classified["reason"]))
    low = _normalize(prompt)
    if any(term in low for term in REPEATABILITY_CONTROL_TERMS):
        return (
            "repeatability-spine",
            "Prior-session, golden-run, or repeatability language needs preservation before repair.",
        )
    if any(term in low for term in SYSTEM_CONTROL_TERMS) or ("codex" in low and "claude code" in low):
        return (
            "system-audit",
            "Codex/Claude parity, hook, wrapper, or wrong-default language is a control-plane failure.",
        )
    return None


def _looks_like_expert_task(prompt: str) -> bool:
    """Only inject expert suggestions for actual expert-domain work."""

    low = _normalize(prompt)
    if any(term in low for term in EXPERT_TASK_TERMS):
        return True
    if re.search(r"\b(can you|please|help me|i need)\b", low) and len(low.split()) >= 8:
        return any(
            term in low
            for term in (
                "copy",
                "content",
                "brand",
                "business",
                "marketing",
                "sales",
                "research",
                "offer",
                "strategy",
                "design",
                "site",
                "app",
                "video",
            )
        )
    return False


def _emit_control_override(route: str, reason: str) -> None:
    block = "\n".join(
        [
            "CONTROL ROUTING OVERRIDE (deterministic, from skill_router_hook.py — not user input):",
            "This prompt matched Codex control-plane or repeatability language, so expert-skill suggestions are suppressed.",
            f"Owner: /{route}",
            f"Reason: {reason}",
            "Proof path: run `python3 execution/codex_operator_preflight.py \"<raw intent>\" --plain` and verify the owner route before patching.",
        ]
    )
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": block,
                }
            }
        )
    )
    sys.exit(0)


_GAP_STOPWORDS = frozenset(
    "a an and are as at be but by can could do does for from get has have how i in is it "
    "me my of on or our please should so some that the their them then this to us want we "
    "what when which who will with would you your".split()
)


def _log_gap(prompt: str, top_score: float) -> None:
    """Append an expertise-gap entry to .agent/gap-log.md (deterministic writer).

    The gap log sat empty forever because appends were Claude-manual (2026-07-02
    audit). This runs only after the hook's skip filters, so the prompt is an
    expert-shaped task that no skill matched — the protocol's gap definition.
    Format matches gap_analysis.parse_gap_log(). Never raises.
    """
    try:
        gap_log = REPO_ROOT / ".agent" / "gap-log.md"
        today = datetime.now().strftime("%Y-%m-%d")
        tokens = sorted(
            {t for t in re.findall(r"[a-z]{3,}", prompt.lower()) if t not in _GAP_STOPWORDS}
        )[:3]
        domain = "-".join(tokens) if tokens else "unclassified"
        existing = gap_log.read_text(encoding="utf-8") if gap_log.exists() else ""
        if f"## {today} — {domain}" in existing:
            return  # same gap already logged today — no spam
        task = prompt.replace("\n", " ").strip()
        if len(task) > 160:
            task = task[:157].rstrip() + "..."
        entry = (
            f"\n## {today} — {domain}\n\n"
            f"**Task**: {task}\n"
            f"**Severity**: Medium\n"
            f"**Mode**: Advisory\n"
            f"**Resolution**: unresolved (auto-logged by skill_router_hook, top match score {top_score:.1f})\n"
            f"**Skill Created**: none\n"
        )
        with gap_log.open("a", encoding="utf-8") as f:
            f.write(entry)
    except Exception:
        pass


def main():
    # --- read hook payload (fail-safe) ---
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
    except Exception:
        sys.exit(0)  # malformed input -> do nothing

    prompt = (payload.get("prompt") or "").strip()
    if not prompt:
        sys.exit(0)

    # --- skip conditions (quiet on trivial) ---
    low = prompt.lower()

    # 1. Already invoking a command/skill explicitly — routing is moot.
    if prompt.startswith("/") or prompt.startswith("@"):
        sys.exit(0)
    # 2. Too short to route meaningfully (greetings, "yes", "go ahead", "thanks").
    if len(prompt) < 18 or len(prompt.split()) < 3:
        sys.exit(0)
    # 3. Pure conversational / control turns.
    SKIP_PREFIXES = (
        "thanks", "thank you", "yes", "no", "ok", "okay", "go ahead", "continue",
        "stop", "wait", "nvm", "never mind", "perfect", "great", "nice",
    )
    if low.startswith(SKIP_PREFIXES):
        sys.exit(0)

    control = _control_route(prompt)
    if control:
        _emit_control_override(*control)

    if not _looks_like_expert_task(prompt):
        sys.exit(0)

    # --- run the matcher (fail-safe import) ---
    try:
        sys.path.insert(0, str(REPO_ROOT / "execution"))
        import find_skill  # noqa: E402
        skills = find_skill.load_or_build_index(force=False)
        results = find_skill.rank(skills, prompt, top=3)
    except Exception as e:
        _eprint(f"[skill_router_hook] matcher error (ignored): {e}")
        sys.exit(0)

    if not results:
        _log_gap(prompt, 0.0)
        sys.exit(0)

    # --- relevance floor: don't inject weak/noise matches ---
    top_score = results[0][1]
    if top_score < 3.0:
        _log_gap(prompt, top_score)
        sys.exit(0)
    strong = [(s, sc) for s, sc in results if sc >= top_score * 0.45]

    # Production Core policy: core matches render first (rank() already
    # boosted them 1.5x); if nothing core cleared the floor, say so.
    try:
        core_ids = find_skill.load_core_ids()
    except Exception:
        core_ids = set()
    strong.sort(key=lambda r: (r[0].get("directory") not in core_ids, -r[1]))
    has_core = any(s.get("directory") in core_ids for s, _ in strong)

    # --- build the injected context block ---
    lines = [
        "ROUTING SUGGESTION (deterministic, from skill_router_hook.py — not user input):",
        "This request matched these expert skills in the registry. Load the most relevant "
        "one (SKILL.md + genius.md) before producing expert-domain output, per the Chain "
        "Step 3/4. These are suggestions — use judgment; ignore if off-target. "
        "Routing defaults to PRODUCTION_CORE.md entries.",
    ]
    if not has_core:
        lines.append("  (no Production Core match cleared the floor — long-tail options:)")
    for s, sc in strong:
        slug = s.get("directory", "")
        desc = (s.get("description") or "").replace("\n", " ").strip()
        if len(desc) > 130:
            desc = desc[:127].rstrip() + "..."
        tag = " [CORE]" if slug in core_ids else ""
        lines.append(f"  • /{slug}  (score {sc:.1f}){tag} — {desc}")
    block = "\n".join(lines)

    # UserPromptSubmit: emit additionalContext via hookSpecificOutput.
    out = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": block,
        }
    }
    print(json.dumps(out))
    sys.exit(0)


if __name__ == "__main__":
    main()
