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
- LEARNS (Wave 3, 2026-07): every emitted suggestion is logged to
  routing_intelligence and stashed as "pending_routing" in the session ledger
  (execution/hooks/session_ledger_hook.py). When the ledger later sees an expert
  skill actually load, it reconciles that load against the pending suggestion
  (auto_match / auto_miss) and evolution_orchestrator.run_routing_learning()
  turns that feedback into per-skill rank-weight nudges nightly
  (.agent/skill-weights.json, applied in find_skill.rank()). None of this ever
  gates the suggestion itself — it's all best-effort, try/except-wrapped.

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
from control_intent import strip_explicit_invocation_artifacts  # noqa: E402

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


def _has_explicit_skill_invocation(prompt: str) -> bool:
    """Detect user-provided skill/app invocation links so routing stays quiet."""

    low = prompt.lower()
    if re.search(r"\[[^\]]+\]\((?:app://|[^)]*(?:/skills/|skill\.md))[^)]*\)", low):
        return True
    if re.search(r"/\S*(?:\.codex|\.agents)?/skills/\S*/skill\.md", low):
        return True
    return False


def _looks_like_expert_task(prompt: str) -> bool:
    """Soft signal only (Wave 3, 2026-07) — no longer gates whether ranking
    runs at all. Every prompt that clears the earlier skip filters gets
    ranked via find_skill.rank() regardless of this signal. This function
    now only lowers the relevance floor slightly when the prompt reads as
    expert-shaped, so genuinely ambiguous prompts still need a stronger BM25
    match before a suggestion gets injected."""

    low = _normalize(strip_explicit_invocation_artifacts(prompt))
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


def _emit_abstention(top_score: float) -> None:
    """Visible-but-quiet abstention (Wave 3, 2026-07). Previously the
    below-floor path exited with zero signal — Claude had no way to tell
    "no skill matched" apart from "hook didn't run." One short line closes
    that gap without becoming noise: no list, no suggestion, just the miss."""
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": (
                        f"Router: no expert matched (top score {top_score:.1f}) — "
                        "generalist mode; log a gap if this deserved an expert."
                    ),
                }
            }
        )
    )


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


def _log_routing_decision(prompt: str, session_id: str, suggested_dirs: list[str]) -> str | None:
    """Best-effort routing_intelligence log at suggestion-emit time. Returns
    the routing_id on success, None on any failure — never raises."""
    try:
        import routing_intelligence  # noqa: E402

        return routing_intelligence.log_routing_decision(
            request_summary=prompt,
            intent_score=0,  # not chain-scored at router time; analytics only
            domain_detected=suggested_dirs[0] if suggested_dirs else "unknown",
            experts_deployed=suggested_dirs,
            tier_loaded=0,
            mode="hybrid",
            workflow_used=suggested_dirs[0] if suggested_dirs else "",
            ensemble=len(suggested_dirs) > 1,
            compound_pairing=" + ".join(suggested_dirs) if len(suggested_dirs) > 1 else "",
            session_id=session_id,
        )
    except Exception as e:
        _eprint(f"[skill_router_hook] routing_intelligence log failed (ignored): {e}")
        return None


def _stash_pending_routing(session_id: str, routing_id: str, suggested_dirs: list[str]) -> None:
    """Stash {routing_id, suggested_dirs, ts} into the session ledger so
    session_ledger_hook.py's PostToolUse handler can reconcile it against
    whatever expert skill actually loads next. Loads session_ledger_hook.py
    by file path (no package __init__.py in execution/hooks/) to reuse its
    _load/_save instead of duplicating the ledger schema. Best-effort only."""
    try:
        import importlib.util

        spec = importlib.util.spec_from_file_location(
            "_session_ledger_hook_ref",
            REPO_ROOT / "execution" / "hooks" / "session_ledger_hook.py",
        )
        slh = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(slh)
        ledger = slh._load(session_id)
        ledger["pending_routing"] = {
            "routing_id": routing_id,
            "suggested_dirs": suggested_dirs,
            "ts": datetime.now().isoformat(),
        }
        slh._save(ledger)
    except Exception as e:
        _eprint(f"[skill_router_hook] pending-routing stash failed (ignored): {e}")


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

    if _has_explicit_skill_invocation(prompt):
        sys.exit(0)

    # Soft signal only (Wave 3, 2026-07): expert-shaped phrasing no longer
    # gates whether ranking runs — every prompt that reaches here gets
    # ranked. It only lowers the relevance floor, so ambiguous prompts still
    # need a stronger BM25 match to trigger an injected suggestion.
    expert_signal = _looks_like_expert_task(prompt)
    floor = 2.5 if expert_signal else 3.0

    # --- run the matcher (fail-safe import) ---
    try:
        sys.path.insert(0, str(REPO_ROOT / "execution"))
        import find_skill  # noqa: E402
        skills = find_skill.load_or_build_index(force=False)
        results = find_skill.rank(skills, prompt, top=3)
    except Exception as e:
        _eprint(f"[skill_router_hook] matcher error (ignored): {e}")
        sys.exit(0)

    top_score = results[0][1] if results else 0.0

    # --- relevance floor: don't inject weak/noise matches ---
    if top_score < floor:
        _log_gap(prompt, top_score)
        _emit_abstention(top_score)
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

    # --- feedback loop (Wave 3, 2026-07): log the decision + stash pending
    # state so the session ledger can reconcile it against whatever expert
    # skill actually loads next (suggest -> load -> outcome). Best-effort
    # only — never blocks or alters the suggestion that's about to print.
    session_id = payload.get("session_id", "unknown")
    suggested_dirs = [s.get("directory", "") for s, _ in strong]
    routing_id = _log_routing_decision(prompt, payload.get("session_id", ""), suggested_dirs)
    if routing_id:
        _stash_pending_routing(session_id, routing_id, suggested_dirs)

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
