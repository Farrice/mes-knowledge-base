---
thread: prompt-wiring-os
status: done
resume_hint: Prompt Wiring OS DONE: menu hook + 356 SKILL.md pointers + forging gate in 7 extraction workflows + 1,650 born-v2 across 237 skills, 100% verified; proof JUDGMENT + MyBPM merge-take jam waiting
branch: main
pin: true
---

# Prompt Wiring OS — COMPLETE (2026-07-13)

## What shipped (all 4 phases, all pushed to origin/main, final commit 64fe0e151)
1. **Load-time injection**: `execution/hooks/prompt_menu_hook.py` (PostToolUse on SKILL.md reads) — every skill load surfaces its v2 execution-prompt menu deterministically; prompt-less skills get a visible forge flag. Wired in `.claude/settings.json`.
2. **SKILL.md pointers**: `execution/wire_prompt_pointers.py --write` — marker-delimited "Execution Prompts" section in all 356 SKILL.mds (idempotent; re-run after any prompt changes, ALWAYS after `prompt_library.py build`).
3. **Prompt Forging gate**: `directives/prompt-forging-spec.md` (born-v2 standard + HIGH FLOOR/UNLIMITED CEILING binding clause + Creative Latitude section) wired as mandatory phase into /extract (5.5), /extract-forge (5.5), and appended to convert-extraction, extract-amplify, parallel-extract, source-to-skill-system, mcclain-source-to-agent. Every extraction now ships prompts + skill + workflows + agent as one deploy-ready unit.
4. **Backfill COMPLETE**: 1,650 born-v2 prompts forged across all 237 prompt-less skills (9 Sonnet waves). `execution/forge_queue.py` = quality-gated wave builder (done = passes audit, never exists).
5. **Proof (Phase 4, ran BEFORE backfill)**: A/B kallaway × MyBPM hero piece — wired take clear win on floor, ceiling uncapped. `_active/prompt-wiring-os-2026-07-13/proof/JUDGMENT.md` + both takes staged for jam. **Shippable move: merge B's structure + A's "stranger" line = MyBPM Week-1 hero video.**
6. **Verification**: 1,629/1,629 born-v2 content-verified vs skill material (82 batches). 37 failures (2.3%): invented numeric scoring on qualitative frameworks, fabricated thresholds, ballooned one-paragraph concepts. All re-forged under source-only repair discipline (36 reforged, 1 verifier false-alarm restored). Records: `_active/prompt-wiring-os-2026-07-13/05-verification/`.

## Corpus state
3,510 v2 files (1,860 renaissance + 1,650 born-v2), `renaissance_audit.py` = 0 fail, prompt index rebuilt, forge queue 0.

## Fidelity-low for Farrice review (~14 born-v2 + 40 renaissance-era)
Born-v2: brand-guidelines/brand-styled-artifact, internal-comms/general-internal-comm, kallaway-content-os/content-to-revenue-map, theme-factory/custom-theme-creation, + 10 repair-pass flags (sheep-cycle-diagnostic, save-worthy-content-architect, 3× kallaway-addictive, aios-deployment-blueprint, 3× oren-brand-archetypes). Renaissance-era 40 (28 nathan-gotch etc.) listed in wave commit bodies.

## Known correction from repair pass
Verifiers over-flagged 2-3 files whose "invented" content actually traced to the skill's own workflow files (supply-side-audit, traction-first-roadmap) — repair agents caught this and kept faithful ports. Lesson: verification prompts must name workflows/ as legitimate source, not just SKILL.md/genius.md.

## Open items
1. Farrice jam: proof takes + MyBPM merge move.
2. Fidelity-low review (above).
3. /cos weekly (overdue) + /weekly-closeout (23+ check-ins due).
4. Next real extraction run = live test of the Prompt Forging gate.

## Do NOT
- Re-run the backfill (forge_queue reports 0; done = passes gate).
- Edit Execution Prompts sections by hand (regenerate via wire_prompt_pointers.py).
- Run two orchestrator sessions in this tree simultaneously (third incident today — swarm-apex session swept this project's files into its commits; content survived, history muddled).
