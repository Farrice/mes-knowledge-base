---
description: Budget-guarded Higgsfield creative system for GPT Image 2 stills, Marketing Studio video ads, product photoshoots, marketplace cards, Soul-ID, MCP, and CLI generation
---

# /higgsfield-studio

Build a cohesive prompt package or guarded Higgsfield generation workflow for GPT Image 2.0, Higgsfield Marketing Studio, Product Photoshoot, Marketplace Cards, and Soul-ID.

## Execution

1. Read `skills/higgsfield-creative-studio/SKILL.md` and `directives/higgsfield-usage-policy.md`.
2. For prompt-only ideation, return a Creative Capsule:
   - Strategy spine
   - Visual direction
   - GPT Image 2 still prompt when useful
   - Marketing Studio video prompt when useful
   - Preview recommendation
   - QA pass
3. Load source prompt directors as needed:
   - `skills/gpt-image-2-director/SKILL.md`
   - `skills/marketing-studio-director/SKILL.md`
   - Persistent character / world production path: `skills/story-bible-builder/SKILL.md` (canon) → `skills/banana-pro-director/SKILL.md` (face lock → outfit base → 3-panel sheet → scene plates) → `skills/cinema-worldbuilder-pro/SKILL.md` (block-structured Seedance shot prompts). Front door: `/jcin-pipeline`. Higgsfield GPT-2 (faces) ≠ OpenAI GPT Image 2 (`gpt-image-2-director`, layout/text).
4. Add strategy or QA layers only when they materially improve the request:
   - `skills/luke-iha-creative-strategy/SKILL.md`
   - `skills/luke-iha-copy-blocks/SKILL.md`
   - `skills/greg-hoffman-brand-mastery/SKILL.md`
   - `skills/creative-direction/SKILL.md`
   - `skills/satori-graphics-design-mastery/SKILL.md`
   - `skills/jack-roberts-design-mastery/SKILL.md`
5. For generation requests, route by surface:
   - In-app Marketing Studio widgets, library, URL fetch, Soul-ID, job display, direct image/video generation → Higgsfield MCP.
   - Local files, account checks, cost estimates, product photoshoot, marketplace cards, repeatable batch runs → Higgsfield CLI.
6. Before any MCP or CLI generation, run `python3 execution/higgsfield_budget_guard.py check` with the relevant operation and estimate.
7. If the guard returns approval required, ask for explicit approval before generating. If denied, do not generate.
8. After generation, run `python3 execution/higgsfield_budget_guard.py log` with status, estimate, actual credits if known, job id, and output URL if available.
9. For single-prompt requests, obey the relevant source skill output format exactly.

## Quality Gate

- Keep still and video prompts visually coherent.
- Preserve source skill output constraints.
- Preserve image reference fidelity and pass `<<<image_n>>>` labels through when present.
- Tie every asset to the same strategy spine when a campaign package is requested.
- Avoid endless loops: one preview pass, one refinement pass, then ask the user to select a winner before final render.
- Client-facing work uses fewer, stronger outputs and stricter QA; personal work uses faster previews and fewer questions.
