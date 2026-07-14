---
name: higgsfield-creative-studio
description: Orchestrates GPT Image 2.0 still-image prompts and Higgsfield Marketing Studio video-ad prompts into a cohesive AI ad production workflow. Use when the user asks for a full ad asset system, still-to-video campaign package, Higgsfield ad concept, Marketing Studio prompt stack, GPT Image 2 key visual plus video prompt, UGC/video ad prompt pack, product creative system, or wants the Higgsfield and GPT Image 2 prompt directors to work together with marketing, brand, copy, or design strategy.
---

# Higgsfield Creative Studio

Use this skill as the routing and stacking layer for AI ad assets. Keep the source prompt directors strict:

- For GPT Image 2.0 stills, load `skills/gpt-image-2-director/SKILL.md` and obey its output format.
- For Higgsfield Marketing Studio videos, load `skills/marketing-studio-director/SKILL.md` and obey its output format.
- If the user asks for a combined system, produce a compact asset package instead of forcing either source skill's single-prompt output format.
- Before any real Higgsfield generation through CLI or MCP, follow `directives/higgsfield-usage-policy.md` and run `python3 execution/higgsfield_budget_guard.py check`. After generation, log with `python3 execution/higgsfield_budget_guard.py log`.

## Credit Guard

Default to prompt-only ideation first. Real generation is budget-gated.

- Prompt-only Creative Capsules are free and do not need user approval.
- Use the guard before any `mcp__higgsfield__generate_image`, `mcp__higgsfield__generate_video`, `show_marketing_studio` fetch-to-video flow, Soul-ID training, CLI `higgsfield generate create`, product photoshoot, or marketplace cards command.
- If the guard returns approval required, ask for explicit approval before generating.
- If the guard denies, do not generate; offer a cheaper route such as fewer variants, shorter video, prompt-only package, or next-day run.
- Client work defaults to fewer, stronger outputs. Personal work defaults to quick preview then winner selection.

## Router

Choose the path from the user's request:

| Request shape | Load | Output |
|---|---|---|
| GPT Image 2 prompt, key visual, poster, landing page mockup, infographic, product frame, storyboard still, character sheet | `gpt-image-2-director` | Finished GPT Image 2 prompt in the correct source-skill format |
| Higgsfield, Marketing Studio, UGC, Tutorial, Unboxing, Hyper Motion, Product Review, TV Spot, Wild Card, Virtual Try On, video ad prompt | `marketing-studio-director` | Finished Marketing Studio paragraph plus generation link |
| Photoreal character build, face lock, character sheet, outfit swap, persistent character | `skills/banana-pro-director/SKILL.md` | Higgsfield still prompt in Banana Pro grammar (18% gray flat plates, Mode 0→1→2A order) |
| Seedance cinematic video prompt | `skills/cinema-worldbuilder-pro/SKILL.md` | Block-structured Seedance prompt (@tags on Higgsfield surface only) |
| Full ad asset system, still-to-video pack, campaign creative kit, prompt stack | This skill + both source skills as needed | Strategy notes, still prompt, video prompt, QA checklist |
| User asks to actually render/generate/show result | This skill + Higgsfield MCP/CLI bridge | Guarded preview/final generation with logged credit use |

Disambiguation: Higgsfield GPT-2 (face-fidelity image model, credit-heavy — banana-pro-director's escalation path) ≠ OpenAI GPT Image 2 (`gpt-image-2-director` — layout/typography king, weak faces).

## Tool Routing

- Use MCP for in-app widgets, Marketing Studio library/fetch, Soul-ID list/status/training flows, job display, and direct image/video generation when the user benefits from UI.
- Use CLI for local files, account/credit checks, `higgsfield generate cost`, product photoshoot backend enhancement, marketplace cards, and repeatable batch workflows.
- For CLI-supported model generation, run `higgsfield generate cost ...` first and pass that credit estimate to the guard.
- For product photoshoot, marketplace, Soul-ID, or MCP generation where exact preflight cost is unavailable, use the conservative operation estimates in `.agent/higgsfield-usage.json`.

## Stacking Order

Use only the stack layers needed for the request.

1. **Strategy**: Load `skills/luke-iha-creative-strategy/SKILL.md` for audience, angle, offer, and what-to-say clarity. Load `skills/greg-hoffman-brand-mastery/SKILL.md` instead when the request is campaign-level, brand-level, or emotional-positioning-led.
2. **Copy**: Load `skills/luke-iha-copy-blocks/SKILL.md` when hooks, spoken UGC lines, captions, CTAs, or ad beat language matters.
3. **Visual Direction**: Load `skills/creative-direction/SKILL.md` for art direction, mood, platform prompt QA, storyboarding, and visual coherence.
4. **Prompt Production**: Load `gpt-image-2-director` for stills and `marketing-studio-director` for videos.
5. **Design QA**: Load `skills/satori-graphics-design-mastery/SKILL.md` for visual communication, layout flow, anti-AI-slop, and message clarity. Use `skills/jack-roberts-design-mastery/SKILL.md` when the output must align to a reusable design system or multi-format brand package.

## Combined Asset Package

When the user asks for both still and video outputs, return:

```markdown
## Strategy Spine
[1-3 bullets: audience, angle, emotional target]

## Key Visual Prompt
[GPT Image 2.0 prompt. Use a fenced code block and preserve the source skill's JSON/prose/meta-prompt rules.]

## Marketing Studio Prompt
[One flowing paragraph, then blank line, then the Generate link exactly as required by marketing-studio-director.]

## QA Pass
[3-5 checks covering product fidelity, avatar fidelity if applicable, visual hierarchy, brand consistency, and ad clarity.]

## Preview Recommendation
[One guarded first render recommendation: operation, count, duration/resolution if video, and why this is the lowest useful preview.]
```

Do not add the package wrapper when the user asked only for a single GPT Image 2.0 prompt or a single Marketing Studio prompt. In those cases, follow the source skill's output format exactly.

## Image Reference Handling

If product or avatar images are attached:

- Preserve the Marketing Studio fidelity rules: exact product packaging, color, logo placement, proportions, avatar face/build, and user-specified wardrobe.
- Pass image references through with `<<<image_n>>>` labels when writing Marketing Studio prompts.
- Do not infer unsupported product claims from images.
- Do not use age markers for avatars.

## Quality Gate

Before responding, check:

- The request was routed to the correct source prompt director.
- Any user-specified camera, preset, product, avatar, dialogue, dimensions, or layout requirements survived into the final prompt.
- Combined packages include both still and video prompts only when requested or clearly useful.
- Strict source output formats remain intact for single-prompt requests.
- Any real generation has a guard check and a post-generation log plan.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

2 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Higgsfield Creative Studio — Combined Asset Package** — `skills/higgsfield-creative-studio/references/prompts-v2/combined-asset-package.md`
- **Higgsfield Creative Studio — Guarded Generation Request** — `skills/higgsfield-creative-studio/references/prompts-v2/guarded-generation-request.md`

<!-- END:execution-prompts -->
