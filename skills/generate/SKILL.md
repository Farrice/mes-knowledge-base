---
name: generate
description: 'The /generate front door — in-house, pay-as-you-go creative generation (Higgsfield replacement). One command for image, video, and audio: routes each request to the right model recipe (skills/generate/models/*.json), defers to binding creative_router lanes (people → fal-people, style-family → fantastic-posters; Higgsfield fully retired 2026-08-06), quotes paid video before running, honors prompt-level budgets ("total budget $3"), runs comparison batches across models, logs every prompt beside its asset, and auto-refreshes the Asset Command Center (/assets-board). Use when the user says "generate", "make an image/video/voiceover", "create ads/assets/creative", names a model (recraft, kling, seedance, nano banana, gpt image), or asks for a multi-model comparison. Source: RoboNuggets 9C4TRbucmhQ, rebuilt on our fal-first stack.'
---

# /generate — Creative Generation Front Door

Flow (from the source, kept): **Route Model → Prep References → Generate Media → Log + Gallery.**
Everything already indexed lands on the board: `open .agent/assets/assets-board.html` (or `/assets-board`).

## Step 1 — Route model

1. **Binding lanes first** (user feedback, never skip): run
   `python3 execution/creative_router.py route --task "<brief>"` —
   PEOPLE/photoreal → `fal-people` (nano-banana-2 w/ reference; Higgsfield retired 2026-08-06) · style-family/poster words → `fantastic-posters` ·
   persistent character/world → `/jcin-pipeline`. Follow what it says.
2. Otherwise pick by media type (defaults, cheapest-capable-first) or by the model Farrice names:

| Ask | Default recipe | Route |
|---|---|---|
| image (styled/poster/ad) | `gpt-image-2` | wrapper: `gen.sh` (fantastic-posters) |
| image (cheap draft/iterate) | `nano-banana-2` | wrapper: `generate_image.py` |
| image (vector/SVG/text-heavy) | `recraft-v3` | `generate_media.py run` |
| video (default) | `seedance-480p` (720p on quality ask) | wrapper: `fal_video_seedance.py` |
| video (multi-shot/narrative) | `kling-v3` | wrapper: `fal_video_kling.py` |
| voiceover / TTS | `minimax-speech` | `generate_media.py run` |
| music / jingle | audio music recipe | `generate_media.py run` |

`python3 execution/generate_media.py models` shows the live registry. Recipes live in
`skills/generate/models/*.json` — adding a model = adding one recipe file (verify endpoint +
price on fal.ai/models first; `status: "deferred"` stubs refuse to run until filled).

## Step 2 — Prep references

- Brand refs / product shots: pass into the wrapper's own flags (`--refs/--logo/--input/--mask`
  for gen.sh · `--reference/--edit` for generate_image.py · `--image/--end-image` for video) or
  `--ref <path>` on `generate_media.py run` (recipes declare `ref_param`).
- Styles registry: `skills/generate/styles/<slug>/` (prompt.md + reference images) — browsable
  and click-to-copy on the board's Styles tab. fantastic-posters' 38 styles remain its own catalog.
- Anything in Farrice's voice/brand → load `_active/farrice-brand/voice/VOICE-CARD.md` first
  (standing routing anchor).

## Step 3 — Generate (HARD RULES)

0a. **REALISM FLOOR — every photographic generation (Farrice ruling 2026-08-10, after the COA
   plate hit 8/10: "make sure this is embedded so the floor is here no matter what work we're
   doing").** Lint the prompt before you send it:

   ```bash
   python3 execution/style_vault.py lint "<prompt>" --strict
   ```

   Eight layers, each a physical cause: **capture · light · black_point · atmosphere ·
   imperfection · provenance · material_response · micro_surface**, plus a ban on
   quality-assertion words (`8k`, `cinematic`, `stunning`, `hyperrealistic`…). Every missing
   layer is one the model fills with its own averaged default — which is what slop is. Also
   binding: **generate ≥4 and select** (one image per concept is a first take, not a sweep).
   Full doctrine + what takes a plate past 8/10: `skills/style-vault/references/realism-floor.md`.
   Non-photographic lanes (vector, flat illustration, diagram) are exempt — say so out loud
   when you skip it.

0. **CRAFT PASS — every generation, paid or free (Farrice ruling 2026-08-02: full pipeline,
   always).** Before writing ANY prompt, load the matching master per
   `skills/generate/references/craft-map.md` and author the prompt through its grammar; run the
   doctor pass; on raw/foggy creative asks, run the craft-map's intent mirror first. A freehand
   prompt into a generator is a defect even when the output is cheap — production-grade is the
   floor, not the ceiling. For paid video, show the crafted prompt WITH the quote.
1. **Paid video always quotes first and waits for Farrice's explicit go.**
   `python3 execution/fal_budget_guard.py check --mode=<kling|seedance-480p|seedance-720p> --duration=N`
   — show the number, get the yes. (Recipes carry `quote_required: true`.)
2. **`seedance-1080p` is hard-blocked everywhere. Never work around it.**
3. **Prompt-level budget** ("total budget $3"): pass `--run-id gen-<ts> --run-budget 3.00` on
   every `generate_media.py run` in the batch; for wrapper calls, do the arithmetic in the run
   plan and stop when the remainder can't cover the next call. The ceiling came from Farrice's
   prompt — never raise it yourself.
4. **One code path per model**: `run` on a wrapper-backed recipe refuses and prints the wrapper
   command. Use the wrapper, then `index` the output (Step 4).
5. The cost gate (PreToolUse hook + `cost_gate.py`) fires on every paid invocation — denied =
   surface to Farrice, never retry.

**Comparison runs** (the source's signature move): same brief → 2-4 recipes, budget split across
them, then present a variants table — `name | model | ratio | concept one-liner | cost | path` —
and let Farrice pick the winner before any refinement round.

## Step 4 — Log + Gallery

- `generate_media.py run` does this automatically (sidecar JSON + manifest line + board refresh).
- After any WRAPPER run, index the output so it hits the board with provenance:
  `python3 execution/generate_media.py index --file <output> --model <recipe-id> --prompt "..." [--cost N] [--project <slug>]`
- `--project <slug>` routes new assets to `_active/<slug>/05-assets/generated/` (client work);
  default is `deliverables/generations/`.

## Cheat table

```bash
python3 execution/generate_media.py models                                    # registry
python3 execution/generate_media.py quote --model recraft-v3 --n 2 --prompt "…"   # never spends
python3 execution/generate_media.py run --model recraft-v3 --prompt "…" \
    --run-id gen-0802 --run-budget 3.00 --project linkedin-launch            # generate + log + board
python3 execution/generate_media.py index --file <path> --model gpt-image-2 \
    --prompt "…" --cost 0.16                                                 # adopt wrapper output
python3 execution/asset_gallery.py --quick                                   # manual board refresh
```

Known gap (flagged, not fixed here): Higgsfield MCP spend is logged (`mcp_spend_log_hook`) but
ungated — those credits remain a manual-judgment lane while the wallet lasts.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

3 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Generate — Comparison Run Report** — `skills/generate/references/prompts-v2/comparison-run-report.md`
- **Generate — Cost Quote Block** — `skills/generate/references/prompts-v2/cost-quote-block.md`
- **Generate — Generation Run Plan** — `skills/generate/references/prompts-v2/generation-run-plan.md`

<!-- END:execution-prompts -->
