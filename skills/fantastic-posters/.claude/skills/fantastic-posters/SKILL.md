---
name: fantastic-posters
description: 'Generates, edits, and transparency-strips images across 38 visual styles via GPT Image 2 (Fal), and animates poster outputs into video via Seedance 2.0 + Kling v3 Pro. Full GPT-Image-2 surface — text-to-image, mask-based edits (--input + --mask), multi-variant batching (--variants 1-4 in one API call), background removal (--rembg → transparent PNG), dimensions up to 3840×2160. 5 typography-first presets (chalkboard, store window, menu, packaging, UI mockup) where the lettering IS the picture. Image-to-video bridge — any poster output becomes a video input frame. Use when the user says "make a poster", "edit this poster", "swap the headline", "make a transparent logo", "make a video", "animate this poster", "image to video", "video trailer", or names any of the 38 styles (vintage, Swiss, Ukiyo-e, brutalism, neon-noir, editorial). Trigger proactively whenever the user shares a brand and asks to "visualize" it — stylized image generation is this skill, not Canva or generic image tools.'
---

# Fantastic Posters (+ Video)

A poster generator with a curated catalog of 38 visual styles (33 original + 5 typography-first harvested from `robonuggets/gpt-image-2-skill`). The agent picks the style that fits the brief, builds the prompt, and generates with GPT Image 2 (via Fal). Multi-reference uploads, brand-book PDFs, structured briefs, batch generation, template replication, mask-based edits, multi-variant batching, and chained background removal are all first-class.

> **Upstream credit (2026-04-30)**: Edit-endpoint patterns, multi-variant batching (`num_images`), large-dimension support (up to 3840×2160), `rembg` chaining for transparency, and the 5 typography-first style presets were harvested from [`robonuggets/gpt-image-2-skill`](https://github.com/robonuggets/gpt-image-2-skill) (MIT) into the existing fantastic-posters skill rather than installed as a parallel skill. One skill, full GPT-Image-2 surface — see `directives/fal-edit-mode-guide.md` for edit-mode usage and `directives/fal-usage-policy.md` for budget gating.

**Video extension (added 2026-04-30)**: Posters can be animated into video via Seedance 2.0 (cinematic + audio) or Kling v3 Pro (multi-shot narrative). The bridge pattern — poster output as video input frame — is the killer use case. See `workflows/poster-to-video.md`, `workflows/kling-multishot.md`, `workflows/seedance-cinematic.md`.

After generation, layer separation is handled outside this skill — open the PNG in Canva and use Magic / Smart Layers to split foreground/background/text.

---

## ⭐ The Studio Pipeline (v2, 2026-07-04) — use this for anything that must be *remarkable*, not just rendered

**Load [`genius.md`](../../../genius.md) first.** It is the brain this skill never had. The bare "brief → pickStyle → render" path produces generic, redundant output; the **Studio** produces concept-first, non-redundant, multi-model, self-critiqued work.

> **Satori decides. The router picks the instrument. The studio critiques its own work.**

Run **`/fantastic-studio`** (`workflows/00-studio.md`) to orchestrate the full pipeline, or invoke a single stage:

| # | Stage | Command | Does |
|---|---|---|---|
| 00 | **Studio (front door)** | `/fantastic-studio` | Runs 1–8 → a routed generation plan |
| 01 | Reference-ground | `/fantastic-reference-ground` | Anchor in real high-taste lineage (not model default) |
| 02 | **Art-direct** | `/fantastic-art-direct` | Ingest/run the **satori brain** → art-direction spec (kills generic) |
| 03 | **Divergence spread** | `/fantastic-divergence` | N *orthogonally distinct* directions (kills redundancy) |
| 04 | Model route | `/fantastic-model-route` | Each direction → GPT Image 2 / Higgsfield Soul / Nano / video |
| 05 | Prompt compile | `/fantastic-prompt-compile` | Spec → model-specific prompt (+ Fal `--brief` JSON) |
| 06 | Generate run | `/fantastic-generate-run` | Cost-gated, human-triggered runbook |
| 07 | **Critique + refine** | `/fantastic-critique-refine` | Virgil × LIFT × type × anti-slop → `--mask` edits (first output → remarkable) |
| 08 | Format pack | `/fantastic-format-pack` | One concept → feed/story/hero/print/cutout/motion |

**When to skip the Studio**: a one-off quick draft, or a `--template` replicate of a proven layout. Everything client-facing or brand-defining runs the Studio.

**Multi-model** (the router picks): `python3 execution/creative_router.py route --task "<direction>"`. Posters/typographic → `fal-poster` (this skill). Photoreal + people → `higgsfield-soul`. Cheap iteration → `higgsfield-nano`. Motion → `fal-kling` / `higgsfield-cinema` / `seedance-720p`.

**Handoff from the design brain**: `/satori-design-think` produces the concept and strategic Production Brief; `/satori-composition-brief` locks leverage, internal rhythm/eye path, grid, movement, friction, and transfer adaptations for layout-bearing work. `/fantastic-art-direct` ingests both directly — Satori is the brain, this skill is the hands. Standalone non-layout imagery and locked template replications may use the companion's explicit skip path.

## Video Generation (Mode-Aware Budget Required)

Three video modes, each with its own budget ceiling enforced by `execution/fal_budget_guard.py`:

| Mode | Endpoint | Per-call ceiling | Use |
|---|---|---|---|
| `kling` | `fal-ai/kling-video/v3/pro/image-to-video` | $2.00 | Multi-shot narratives, character consistency, default for most cases |
| `seedance-720p` | `bytedance/seedance-2.0/image-to-video` | $3.00 | Cinematic single-shot, lipsync-grade audio, start→end frame transitions |
| `seedance-480p` | same | $1.50 | Budget option for quick experiments |
| `seedance-1080p` | same | **HARD-BLOCKED** | Single 15s call ~$10; refused at script level |

**MANDATORY pre-flight** before any video call:
```bash
python3 execution/fal_budget_guard.py check --mode=<kling|seedance-720p|...> --duration=<N> [--audio=<off|on|voice_control>]
```

**Wrappers** (handle FAL_KEY loading from project root .env, image upload to Fal storage, MP4 download):
- `python3 execution/fal_video_kling.py --prompt="..." --start-image="<path|url>" --duration=5 --audio=on`
- `python3 execution/fal_video_seedance.py --prompt="..." --image="<path|url>" --duration=6 --resolution=720p`

## How to Run

`generate.js` lives at the project root (alongside `styles.js`).

```bash
cd <repo-root>
node generate.js "<brief>"                                     # auto-pick, 1 image
node generate.js "<brief>" --style=<style_id>                  # force a style
node generate.js "<brief>" --n=3                               # 3 variations (3 separate API calls)
node generate.js "<brief>" --variants=4                        # 4 variants in 1 API call (cheaper, faster)
node generate.js "<brief>" --refs=hero.jpg,brand.pdf,logo.png  # multi-ref edit
node generate.js "<brief>" --logo=<path>                       # logo-anchored edit
node generate.js --brief=path/to/brief.{md,yaml}               # structured brief
node generate.js --batch=path/to/listings.json                 # iterate many briefs
node generate.js --template=existing.png "<brief>"             # replicate-template

# Harvested from gpt-image-2-skill (2026-04-30):
node generate.js "<edit instruction>" --input=<url|path>       # explicit edit mode (no style needed)
node generate.js "<edit instruction>" --input=<url> --mask=<url>  # surgical mask-based edit
node generate.js "<brief>" --rembg                             # chain background removal → *_alpha.png alongside original
node generate.js "<brief>" --size=banner-3to1                  # 3072×1024 ultra-wide hero
node generate.js "<brief>" --size=hero-2to1                    # 2560×1280 wide social header
node generate.js "<brief>" --size=poster-xl                    # 2048×3072 large-print poster
node generate.js "<brief>" --size=3840x1280                    # custom (multiples of 16, ≤3:1 aspect, ≤8.3MP)
```

Flags: `--size=portrait|landscape|square|banner-3to1|hero-2to1|poster-xl|WxH`, `--quality=low|medium|high`, `--palette="#hex,..."`, `--yes`, `--include-experimental`, `--variants=N` (1-4), `--input=<url|path>`, `--mask=<url|path>`, `--rembg`.

The script reads `FAL_KEY` (and optional `KIE_KEY`) from `.env` at the project root. Output PNGs go to `./out/`. When `--rembg` is set, transparent variants are saved as `<original>_alpha.png` alongside.

### When to use the new flags

- **`--input` (explicit edit mode)**: User wants to modify an existing image. Pass the image URL/path and describe ONLY the change. Example: `"swap the headline to 'TONIGHT'" --input=https://.../poster.png`. See `directives/fal-edit-mode-guide.md` for full guidance.
- **`--mask` (surgical edit)**: Pair with `--input` (or `--refs`/`--template`) when the change is region-specific. Mask is B/W: white = edit, black = preserve. Same dimensions as input.
- **`--variants=N` (cheap multi-variant)**: Use when you want N siblings of the same prompt (1 API call, N images, total cost N × per-image). For diverse interpretations, use `--n=N` instead (N separate API calls with per-call diversity nudge).
- **`--rembg` (transparency)**: Use for logos, stickers, cutouts. Adds ~$0.005/image. Requires a separate budget guard log entry under `--mode=rembg` per `directives/fal-usage-policy.md`.
- **`--size=banner-3to1|hero-2to1|poster-xl|WxH`**: Use for hero banners, large social headers, billboards. Cost is the same regardless of dimensions — only `--quality` changes the price. Invalid sizes (>3840 edge, aspect >3:1, pixels outside [655K, 8.3M]) rejected before the API call.

## When the User Says "Make a Poster"

1. Read the brief. Identify mood (calm / vibrant / nostalgic / mystical / luxury / corporate / playful) and subject (event / product / album / movie / listing / retreat).
2. Pick the best matching style from the catalog using the **Style Picker** rules below.
3. **Show the relevant `examples/<style-id>.png` to the user before generating** — never regenerate the catalog showcase. The reference render is the baseline.
4. Tell the user which style you picked and why (one sentence).
5. Run `generate.js`. Default to `--n=1`. If they say "more designs" or "variations", run with `--n=3`.
6. The script will print an estimated cost and ask for confirmation. For >=5 images or `--quality=high` it always prompts regardless of `--yes`.
7. After it saves, give them the file path and remind them: **open in Canva and use Magic Layers if they want to edit text or swap the subject.**

## Reference Image Order (for `--refs`)

Multi-reference uploads follow this convention:

1. **Image 1 — hero photo** (the main subject)
2. **Image 2 — brand book** (PDF auto-renders to PNG page 1 at 2x DPI)
3. **Image 3+ — logos**

For `--template` mode the order is: template (1st) → new hero photo (2nd) → optional logos.

## Style Picker (auto-match by brief intent)

| If the brief is about... | Pick |
|---|---|
| moody crime / thriller / dark cinematic | `cinematic-neonoir` |
| travel / destination / vintage tourism | `vintage-travel` |
| design lecture / minimal swiss / typography | `swiss-minimal-typo` |
| tech conference / agentic web / dev event | `tech-conf-darkmode` |
| annual report / executive / finance | `corporate-report` |
| live music / DIY gig / underground band | `indie-gig-riso` |
| home listing / open house with photo | `luxury-real-estate` |
| luxury estate brochure / architectural retreat | `luxury-estate-cover` |
| art deco / Gatsby / 1920s glam | `art-deco` |
| Bauhaus / primary geometric / design school | `bauhaus-geometric` |
| Japanese woodblock / Edo / classical Japan | `ukiyo-e` |
| sixties rock / Fillmore / hippie concert | `psychedelic-60s` |
| synthwave / retro futurism / 80s sunset | `vaporwave-synth` |
| minimalist film / cut-paper / Hitchcock vibe | `saul-bass-minimal` |
| 80s postmodern / playful clashing patterns | `memphis-80s` |
| high fashion magazine / editorial cover | `editorial-fashion` |
| symmetric pastel / dollhouse / storybook film | `symmetric-storybook` |
| comic / Ben-Day dots / pop art | `pop-art-comic` |
| wellness / meditation / retreat / soft calm | `pastel-mindful` |
| zen / Japanese ink / monastic minimal | `sumi-e-zen` |
| Día de los Muertos / Mexican folk / festival | `loteria-folk` |
| surreal / Magritte / dreamlike | `surreal-dreamscape` |
| documentary / Magnum reportage / photo essay | `documentary-portrait` |
| stadium / race / athletic event campaign | `sports-action-hero` |
| album cover / vinyl / soul-funk debut | `album-cover-portrait` |
| post-apocalyptic action game key art | `post-apoc-sword` |
| melancholic sci-fi wanderer / cargo / Iceland | `lone-traveler-cargo` |
| cyberpunk / neon noir / dystopian megacity | `neon-noir-cyberpunk` |
| streetwear lookbook / drop / collection | `streetwear-lookbook` |
| tech product reveal / keynote / Apple-style | `minimal-tech-keynote` |
| brutalist / broadcast / jersey-number / HYROX-style | `brutalist-broadcast` |
| restaurant / wine bar / jazz lounge / brasserie / hospitality | `emerald-nocturne` |
| absurd transit map / mood diagram *(experimental)* | `absurd-transit-map` |

If nothing matches confidently, ask the user to pick from a 3-option shortlist.

## Out-of-Left-Field Mode

When the user asks for "out of left field", "weird", "different", "surprise me", or "experimental" ideas, default catalog picks are forbidden. Instead:

1. **Vary palette and typography away from catalog defaults.** Don't reach for the obvious one.
2. **Pull inspiration from less-obvious design references via online research.** Web search/fetch from: Polish theatre poster archives (Jan Lenica, Henryk Tomaszewski), Japanese book covers (Kohei Sugiura, Tadanori Yokoo), Czech New Wave film posters, AIGA poster annuals, Dribbble's experimental tag.
3. **Propose 5+ ideas with a one-line vibe each BEFORE generating.** Let the user pick.
4. **Never default to safe catalog picks for these requests.**

## Logo Handling Protocol

- Pass logos as base64 data URIs (handled automatically when you supply `--logo=<path>`), never as a local path string.
- Use the `gpt-image-2/edit` endpoint when a logo is supplied (handled automatically).
- Add the "do NOT redraw, recolour, or modify proportions" clause to the prompt (handled automatically).
- When a brief specifies "mark on black panel" or "mark on white panel" (HYROX-affiliate work), enforce it in the prompt.
- For **dual-wordmark** layouts (client + partner), specify equal visual weight, separated by a hairline rule, never combined into a single lockup.
- Logo placement reliability is imperfect even with the edit endpoint — review the rendered logo carefully before delivering.

## Trust the Reference

When using `--template` or any multi-ref edit mode, **the shortest prompt that names ONLY what changes outperforms verbose specs.** Trust the reference image to carry layout, typography, palette, and logo. Don't restate what the reference already shows. Verbose specs make the model drift.

## What References Can and Can't Do

- References guide style/content, not pixel-copy templates.
- Exact font reproduction is unreliable past ~6 words. Shorten titles.
- Logos may be subtly redrawn — pass them as a separate ref for stronger anchor (`--logo=`) or composite in Canva afterward.
- Output aspect follows `image_size` (the `--size` flag), not the reference image. For `--template` mode, set `--size` to match the template's aspect manually.

## Generation Settings (cost table)

| Quality | $/image | Time | When to use |
|---|---|---|---|
| `low` | ~$0.011 | 10-15s | drafts, exploring directions |
| `medium` | ~$0.04 | 25-40s | client review |
| `high` | ~$0.17 | 60-90s | final delivery (then upscale externally) |

Default `--size=portrait` is 1024x1536 (max 1536/side). For A2 print at 300 DPI, upscale externally with Topaz Photo AI or Real-ESRGAN.

For >=5 images or `--quality=high`, the CLI always prompts for confirmation regardless of `--yes`.

## Subagent Fan-Out (canonical bulk pattern)

For 10+ briefs, use Claude's Agent tool to fan out — one subagent per brief, each running this skill independently. Example:

```
Spawn N subagents. Each runs:
  fantastic-posters --brief=briefs/{client}.md --refs=hero.jpg,brand.pdf,logo.png
```

Subagents are how this skill produces real-client batches at speed.

## Rules

- **Use real brand names when supplied.** Real-client work is the primary use case. Only anonymise for generic demos.
- **Don't oversell calm styles** — for `pastel-mindful` and `sumi-e-zen`, restraint is the whole point.
- **Footer billing line** is always last — date · venue · price/credit.
- **Title rendering** — GPT Image 2 is strong on typography but not perfect. If a title has more than ~6 words, expect typos.
- **Variations** — when running `--n=3`, vary the subject slightly rather than the same prompt 3x.
- **Show, don't regenerate.** When auto-picking a style, show `examples/<style-id>.png` first — never regenerate the catalog.

## Out of Scope

- **No PSD layering in this skill.** Direct the user to **Canva → Magic / Smart Layers**. PSD-layering is available via the adjacent `poster-to-layers` pipeline if Photoshop is preferred.
- **No upscaling in this skill.** Point users to Topaz Photo AI or Real-ESRGAN for print-resolution output.
- **No animation.** Still images only.

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

6 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Fantastic Posters — Client Deliverable Cover Frame** — `skills/fantastic-posters/references/prompts-v2/client-deliverable-cover.md`
- **Fantastic Studio — Critique + Refine Ledger** — `skills/fantastic-posters/references/prompts-v2/critique-refine-ledger.md`
- **Fantastic Studio — Format Pack (Multi-Format Deployment Plan)** — `skills/fantastic-posters/references/prompts-v2/format-pack-plan.md`
- **Fantastic Posters — Poster-to-Video Animation Plan** — `skills/fantastic-posters/references/prompts-v2/poster-to-video-animation-plan.md`
- **Fantastic Posters — Quick Poster / Image Generation** — `skills/fantastic-posters/references/prompts-v2/quick-poster-generation.md`
- **Studio Job — [job name / surface]** — `skills/fantastic-posters/references/prompts-v2/studio-job.md`

<!-- END:execution-prompts -->
