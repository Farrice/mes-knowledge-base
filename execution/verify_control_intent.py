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
    # ---- MUST fire: repeatability lane ----
    ("we lost the magic from the previous session import, the revision got worse", "repeatability-spine"),
]


def main() -> int:
    failures = []
    for prompt, expected in GOLDEN:
        result = classify_control_intent(prompt)
        got = result["route"]
        if got != expected:
            failures.append((prompt, expected, got, result["evidence"]))
    if failures:
        print(f"FAIL — {len(failures)}/{len(GOLDEN)} golden cases regressed:")
        for prompt, expected, got, evidence in failures:
            print(f"  expected={expected or '-'} got={got or '-'} ev={evidence[:5]}")
            print(f"    prompt: {prompt}")
        return 1
    print(f"PASS — {len(GOLDEN)}/{len(GOLDEN)} control-intent golden cases hold.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
