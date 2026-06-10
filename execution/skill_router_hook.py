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
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def _eprint(*a):
    print(*a, file=sys.stderr)


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
        sys.exit(0)

    # --- relevance floor: don't inject weak/noise matches ---
    top_score = results[0][1]
    if top_score < 3.0:
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
