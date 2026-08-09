#!/usr/bin/env python3
"""verify_control_intent.py — golden-set regression gate for the shared
control-intent classifier (execution/control_intent.py).

WHY: 2026-07-08 root cause — classify_control_intent routed content/client
work to /system-audit whenever one ambiguous surface word ("hook", "chain",
"agent", "default") co-occurred with an everyday problem word ("why",
"issue", "wrong"). In this workspace those are content-craft vocabulary.
Both harnesses import this classifier (skill_router_hook.py on the Claude
side, codex_operator_preflight.py / workflow_router.py on the Codex side),
so misfires showed up everywhere at once.

Run: python3 execution/verify_control_intent.py
Exit 0 = all golden cases pass; exit 1 = regressions, printed per case.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from control_intent import classify_control_intent  # noqa: E402
from routing_enforcer import match_bindings  # noqa: E402

# (prompt, expected_route) — expected_route "" means "must NOT fire".
GOLDEN: list[tuple[str, str]] = [
    # ---- Must NOT fire: content / client / deliverable work ----
    ("build me a skill for writing LinkedIn hooks", ""),
    ("why is this post not converting, check the hook in line 1", ""),
    ("repair the Willis recording pack, the ADU section is wrong", ""),
    (
        "fix the Health Performance GEO automation prompt, it's hyper-focused on GLP-1",
        "",
    ),
    ("create a workflow for Jen's listing content", ""),
    ("the chain of emails has an issue with the default greeting", ""),
    (
        "what's going on with my agents in the fitness program, the workouts look wrong",
        "",
    ),
    ("draft a post about why most coaches fail", ""),
    ("audit this sales page copy", ""),
    ("why wasn't the email fixed like I asked, nothing changed in the draft", ""),
    ("the hook on the reel isn't gripping, rewrite it", ""),
    (
        "I want a follow-up prompt engine that suggests skills and agents that are high leverage for what I'm working on",
        "",
    ),
    # 2026-08-08: capability-use prompts can contain the grammatical shape
    # "show + changed + not" without reporting a failed control-plane repair.
    (
        "Apply the Systems Thinking Expertise Intelligence Overlay to this mission in SHADOW mode. "
        "Show the Zoom/Craft/Pave/Own/Learn trace, what changed, and production receipt one. "
        "Do not promote or add enforcement",
        "",
    ),
    ("Use the source-to-skill system and show what changed. Do not promote it.", ""),
    ("Run the health check and show what is working; do not repair anything.", ""),
    ("Show what changed in this result, but do not promote it yet.", ""),
    # ---- MUST fire: real control-plane complaints -> system-audit ----
    ("hooks are not firing in codex, something is broken in the wiring", "system-audit"),
    (
        "the router keeps routing wrong defaults, system-audit fires for no reason",
        "system-audit",
    ),
    ("codex and claude code parity is drifted, hooks not firing", "system-audit"),
    (
        "why does the skill router hook keep injecting system-audit as owner, fix the routing",
        "system-audit",
    ),
    ("check and repair the hook wiring, defaults are wrong", "system-audit"),
    ("the cost gate hook keeps blocking free scripts, diagnose it", "system-audit"),
    (
        "my skills and workflows are broken after the migration, diagnose and repair them",
        "system-audit",
    ),
    (
        "so what was done here? from the looks nothing was fixed that I wanted",
        "system-audit",
    ),
    ("The hook repair is still broken; explain why nothing changed", "system-audit"),
    # ---- MUST fire: repeatability lane ----
    ("we lost the magic from the previous session import, the revision got worse", "repeatability-spine"),
    # ---- Must NOT fire: explicit workflow invocation + deliverable mission ----
    # 2026-07-13 root cause: an /extract-forge mission carrying "orchestrate"
    # (broad surface) + "not doing" (substring problem term, from "we're not
    # doing 12 separate workflows!") routed to /autopilot as a broken-system
    # complaint. The broad front-door branch checked neither deliverable/content
    # context nor explicit slash-invocation.
    (
        "run /extract-forge on this youtube video and /watch https://www.youtube.com/watch?v=abc "
        "I believe we have this expert in our arsenal already. We'll make sure we orchestrate it "
        "properly through the right channels to the right models. We'll also make it smart, where "
        "the prompts, the skills, the workflows, everything that's created is at the highest level "
        "and a unified system. We're not doing 12 separate workflows for every single video!",
        "",
    ),
    (
        "run /kdp-engine and orchestrate the book pipeline through the right models for this niche",
        "",
    ),
    # ---- MUST still fire: genuine router complaints (incl. the fix request itself) ----
    (
        "fully look into why the control router is mismatching and misfiring on the wrong thing, "
        "patch that and fix it permanently",
        "system-audit",
    ),
    ("autopilot is broken, everything it suggests is wrong and useless", "autopilot"),
]

# Golden set for routing_enforcer.match_bindings — the OTHER misfire surface.
# (text, binding_id_expected) — "" means "no binding may fire on this text".
# 2026-07-13 root cause: operator_system_audit fired on bare "wiring"/"chained"
# substrings, hitting research missions and finalize notes that merely
# mentioned wiring as a build aspiration, not a control-plane complaint.
BINDINGS_GOLDEN: list[tuple[str, str]] = [
    # ---- Must NOT fire: research / build-aspiration language ----
    (
        "portability research: do Codex and Gemini CLI now support hooks or "
        "fleet orchestration worth wiring into the ladder?",
        "",
    ),
    (
        "Portability research brief: Codex CLI + Gemini CLI hooks/fleet "
        "orchestration state, with Conductor Ladder wiring recommendations",
        "",
    ),
    # 2026-08-08: content_production_live_grounding (Farrice-ratified 2026-08-05,
    # suggestion-only live-grounding nudge) legitimately fires on "draft a post".
    # The original scar — operator_system_audit firing on "chained" — is still
    # guarded by the global check below: operator_system_audit may never fire on
    # any case that doesn't expect it.
    ("draft a post about how neurons are chained into circuits", "content_production_live_grounding"),
    # ---- MUST fire: real control-plane complaints ----
    (
        "Codex is blocking hooks and routing wrong defaults; match Claude Code "
        "without breaking my workspace",
        "operator_system_audit",
    ),
    (
        "do a full audit or check and repair on things that are not wired or "
        "should not be wired together",
        "operator_system_audit",
    ),
    (
        "routes are being handcuffed and chained together for no reason",
        "operator_system_audit",
    ),
    ("the hook wiring is broken, defaults are wrong", "operator_system_audit"),
]


def main() -> int:
    failures = []
    for prompt, expected in GOLDEN:
        result = classify_control_intent(prompt)
        got = result["route"]
        if got != expected:
            failures.append((prompt, expected, got, result["evidence"]))
    binding_failures = []
    for text, expected_id in BINDINGS_GOLDEN:
        hits = match_bindings(text)
        got_ids = [h["binding_id"] for h in hits]
        if expected_id and expected_id not in got_ids:
            binding_failures.append((text, expected_id, got_ids))
        elif not expected_id and got_ids:
            binding_failures.append((text, "-", got_ids))
        # Scar guard (2026-07-13): the control-plane audit binding must NEVER
        # fire on text that doesn't expect it — regardless of what suggestion
        # bindings are added later.
        if expected_id != "operator_system_audit" and "operator_system_audit" in got_ids:
            binding_failures.append((text, f"{expected_id or '-'} (no operator_system_audit)", got_ids))
    if failures or binding_failures:
        if failures:
            print(f"FAIL — {len(failures)}/{len(GOLDEN)} classifier golden cases regressed:")
            for prompt, expected, got, evidence in failures:
                print(f"  expected={expected or '-'} got={got or '-'} ev={evidence[:5]}")
                print(f"    prompt: {prompt}")
        if binding_failures:
            print(f"FAIL — {len(binding_failures)}/{len(BINDINGS_GOLDEN)} bindings golden cases regressed:")
            for text, expected, got in binding_failures:
                print(f"  expected={expected} got={got or '-'}")
                print(f"    text: {text}")
        return 1
    print(
        f"PASS — {len(GOLDEN)}/{len(GOLDEN)} classifier + "
        f"{len(BINDINGS_GOLDEN)}/{len(BINDINGS_GOLDEN)} bindings golden cases hold."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
