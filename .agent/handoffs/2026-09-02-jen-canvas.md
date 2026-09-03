---
thread: jen-canvas
status: active
resume_hint: Scrapes skills merged; Jen carousel v2 + canvas awaiting verdict; Farrice must git merge --abort then merge codex/scrapes-trial; next = real Scrapes execution engine for Jen after her six intake inputs
branch: main
pin: false
---

## Purpose
Vendored Simon Scrapes' Skill Systems (36 skills + 4 workers) into the harness, then ran the first client carousel for Jen through it: the Scrapes content phases for structure, our pens (Alyssa hook-reframe + Luke Iha) for copy, her own renderer and a Claude Design canvas for execution.

## Current State
- Merged to main (commit c1d967154): 36 Scrapes skills in `.claude/skills/`, Codex symlinks in `.agents/skills/`, `brand_context/` (Farrice, from canon), arsenal index, constitution block, PRECEDENCE-MAP + INTEGRATION in `_active/harness/scrapes-skill-systems/`, hook log untracked.
- Lane `codex/scrapes-trial` PARKED with 6 more commits (OpenAI $15/mo budget guard + cost_gate service `openai-image`; Jen sibling `brand_context/` with voice-profile/icp/refs/INTAKE-PROMPT-PACK.md; Jen run `projects/00-social-content/2026-09-02/jen-priced-out/` v1 + v2 + `v2/canvas/` artboards). Main is MID-MERGE from the journal lane (40 conflicts, mostly generated research-brief HTML); guard blocks Claude from `git merge --abort`. Farrice must run: `git merge --abort` then `worktree_lane.py merge --lane codex/scrapes-trial`. Journal lane `codex/health-performance-evidence-journal` still needs a conflict sitting.
- Jen carousel: Farrice picked cover A ("you saved the down payment. / then stopped looking."); v1 rated 6/10, v2 (Alyssa+Luke+Scrapes formulas) awaiting his verdict. Canvas published: https://claude.ai/code/artifact/084b1bd6-f6b0-4a4a-b1dd-9ddb6d611fb1 (six artboards to the Travel Moments reference grammar in her palette; source in `v2/canvas/`, working copies in scratchpad `jen-canvas/`). Cost of all renders: $0 (local Chromium); one Perplexity search ~1¢.
- Uncertain: LA median rent $3,800 is single-source (soften or re-verify before post day); frame 3 plate (Van Nuys street) is the weakest, wants one of her real neighborhood house photos; cover footer in editions.py hardcodes "01 / 05".
- OpenAI key verified live in `.env` (never in chat); GitHub + npm tokens pasted in chat earlier were flagged for rotation.

## Remaining Priority
Farrice runs the two main commands (abort, merge scrapes-trial), forwards INTAKE-PROMPT-PACK.md to Jen, and the next sitting runs the real Scrapes execution engine for her: mkt-visual-identity Import from her DESIGN.md + refs → ssc-template-builder ×6 → Template Studio approval → 00-social-content → ssc-designer → ssc-image-generator (the blind bar he named as the biggest leverage).

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
