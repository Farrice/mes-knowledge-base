---
name: connected-mood-board-front-door-orchestrator
problem_signature: "A mood-board front door exists, but generic brief routes outrank it and its text-only output never composes the reference, taste, visual-production, proving-surface, and downstream capabilities already built."
domain: system
tags: [moodboard, creative-direction, routing, orchestration, regression, taste]
date: 2026-09-01
status: active
session: "Creative: Moodboard System Regression - Preserve Better Standard"
---

## Problem

`/mood-board` existed as a five-layer written brief, while the useful capabilities were scattered across creative direction, Oren taste development, reference acquisition, visual production, proving surfaces, and downstream design-system owners. Natural requests such as “turn discovery notes into a moodboard” were therefore routed to generic creative briefs or component workflows, and a prose description could pass as a finished moodboard.

## Root Cause

The system had ingredients but no paved path with one function owner. Route vocabulary described the noun `moodboard` without encoding the real job: acquire references, build three materially different visual territories, render actual boards, compare them on one proving surface, make a blind taste decision, and hand only the winner downstream.

## Approach That Worked

1. Preserve the stronger prior standard before editing: distinct A/B/C directions, real visual references, blind choice, and no accidental replacement of existing expert owners.
2. Keep `creative-direction` as the sole function owner and turn `/mood-board` into a seven-phase conductor. Compose Refero or other approved reference sources, Oren taste judgment, actual visual-board construction, comparative proving surfaces, blind selection, and bounded downstream handoffs.
3. Make completion truth explicit. A text-only brief is `PARTIAL`; a described proving surface is `UNBUILT`; the workflow is complete only when three inspectable boards and the shared comparison surface exist.
4. Add one narrow routing binding for discovery-to-moodboard language. Protect adjacent owners with negative signals for library sweeps, approved-board production, and full Brand Operating System builds.
5. Add a dedicated cold-start verifier that tests both natural-language discovery requests and rejection controls across the command menu, workflow router, binding enforcer, workflow structure, bridges, and downstream ownership.

## Dead Ends

- Creating a new command or mega-skill would duplicate the capabilities already built and split craft ownership.
- Making Andrew Lane the moodboard owner would move a downstream brand-decision documentation capability ahead of visual exploration and taste selection.
- Binding on the bare word `moodboard` would hijack style-library sweeps, approved-board production, and full BOS requests.
- Schema-only validation would prove that files exist, not that natural language reaches the right front door or that adjacent routes remain protected.
- The legacy `validate_skill.py` does not model the creative-direction folder's current v2 prompt layout. Use the born-v2 audit, dedicated behavior verifier, and live routing checks instead.

## Verification

- Dedicated orchestrator verifier: PASS — 8 positive routes, 4 negative controls, 101 structure and proof assertions.
- Control-intent regression: PASS — 33/33 classifier and 7/7 binding golden cases.
- Born-v2 prompt audit: PASS — 3,953/3,953 prompt files.
- Skill-system contract, Codex authority, Autopilot runtime preflight, subagent approval language, platform lint, harness check, Operator Core status, run receipt, and diff hygiene: PASS.
- Human blind taste selection, revision-count reduction, client approval drift, and production performance remain `UNTESTED` until a real brand pilot runs.

## Weaker-Model Trap

A weaker model will improve the prose template, add more style adjectives, or make a broad keyword route that looks discoverable in one happy-path query. The correct repair is behavioral: one owner composes the existing specialists, visual artifacts are required, all territories face the same test, a blind human decision selects the winner, and negative controls prove the front door does not steal downstream work.

## Pointers

- `.agent/workflows/mood-board.md`
- `skills/creative-direction/references/prompts-v2/mood-board.md`
- `execution/routing_enforcer.py`
- `execution/verify_mood_board_orchestrator.py`
- `docs/mission-artifacts/mood-board-orchestrator-repair/CONTRACT.md`
- `docs/mission-artifacts/mood-board-orchestrator-repair/COLD-START-PROOF.md`
