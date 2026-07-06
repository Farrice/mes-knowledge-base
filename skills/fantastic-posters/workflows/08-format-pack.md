---
description: Press ONE locked, critique-passed concept into the full deployment set — feed / story / hero / print / transparent cutout / motion — by varying --size and reframe mode over the same brief, so the concept survives every crop and the 10/5/1 ladder is re-checked per aspect.
---

# 08 — Format Pack (/fantastic-format-pack)

> The deployment stage. The concept is already won; only the frame changes. This presses the single locked winner into every surface it ships to — exploiting the `--size`, `--rembg`, and video levers the skill has always had but never orchestrated — without letting any format quietly re-design the idea.

Stages 1–7 fought to lock one concept the studio believes in. This stage refuses to throw that away at the last mile — where most pipelines hand you a beautiful 2:3 poster and a shrug when the client asks for a 9:16 story, a site banner, and a transparent logo. Format Pack derives the format set from the *deployment surface*, re-runs the same compiled brief (or reframes the winning PNG) at each aspect, and re-checks the recognition ladder every time — because a crop is a hierarchy change, not a resize. **Satori decided, the router picked the instrument, the studio critiqued its own work; this presses the survivor into every frame it has to live in.**

## Pre-Flight Gate

**Use this when**:
- Stage 7 (`/fantastic-critique-refine`) named ONE locked winner and it now has to ship into more than one aspect ratio or medium — feed, story, hero/banner, print, a transparent cutout, a motion cut.
- You have a single approved still (from this skill or anywhere) and need the full deployment set derived and staged, not hand-improvised one size at a time.
- A deliverable spans surfaces (an IG post + a story + a LinkedIn banner + a print A-frame) and you want one plan that reframes the *same* concept, gated, instead of six ad-hoc generations that drift apart.

**Do NOT use this when**:
- There is no locked winner yet. A format pack multiplies whatever you feed it — feed it an un-critiqued render and you mass-produce a flaw across six sizes at six times the cost. Go back to `/fantastic-critique-refine` (WF-07).
- You need a *different concept* for a different surface (e.g. the story wants its own idea, not a reframe of the poster). That's a new divergence, not a format — run `/fantastic-studio` (WF-00) for that surface.
- You only need one size at one aspect — just stage that single gated `generate.js` call; the pack is overhead when there's one frame.
- The winner is pure copy/headline — text has no aspect ratio. Route to the writing roster.

**Hard rule this stage enforces**: Format Pack **PLANS and STAGES the reframe commands — it never auto-fires a paid API.** Every format re-render is fresh paid generation and re-enters the Stage 6 cost gate. The output is a table of gated, copy-pasteable commands; the human pulls each trigger. And it packs **only the winner** — the format pack is a post-critique privilege, never run across the divergence spread.

## Skill Acquisition

```
Load: skills/fantastic-posters/genius.md
  ├─ The Capability Map (generate.js) ...... every --size preset, --rembg, the video bridge (the levers this stage exploits)
  ├─ Transferability (Critique Rubric, LIFT-T) . "holds across thumbnail + light/dark + ≥2 formats" — the standard a pack must meet
  ├─ Under-Used Hands (Anti-Pattern #6) .... never reaching for non-portrait sizes / --rembg / the video bridge = the failure this stage fixes
  └─ Cost Discipline ....................... draft cheap, promote the winner; every reframe is gated

Composes (load as needed — Tier 1.5 hot-context; skip re-read if already loaded):
  skills/satori-graphics/workflows/01-lift-audit.md → /satori-lift-audit  (re-run the T/Transferability lens per aspect — Step 4)
  skills/satori-graphics/genius.md GP-06           → the 10/5/1 recognition ladder the crop re-checks against

Drives (the REAL code — read to confirm flags, never invent them):
  skills/fantastic-posters/generate.js  → --size presets (portrait|landscape|square|banner-3to1|hero-2to1|poster-xl|WxH), --input/--mask reframe, --rembg, --brief, --quality
  skills/fantastic-posters/styles.js    → the winner's style id (reuse the SAME primitive across every format)
  execution/creative_router.py          → route the motion format (route --task "<motion cut>" --json)
  execution/cost_gate.py                → mandatory pre-flight per format (check --service <id> --request)
  execution/fal_budget_guard.py         → video double-gate (check --mode=kling|seedance-720p --duration=N)
  execution/fal_video_kling.py · fal_video_seedance.py → animate the locked still into a motion format
```

## The Size Surface (grounded — from generate.js `resolveSize`; confirm, never invent)

`generate.js` resolves these presets; any `WxH` is snapped to a multiple of 16 and validated (aspect ≤ 3:1, pixels between 655,360 and 8,294,400, max edge 3840). Snapped values below are what the generator actually renders.

| Format lever | `--size` flag | Renders at | Aspect | Primary deployment |
|---|---|---|---|---|
| Feed 4:5 (portrait post) | `--size=1024x1280` | 1024×1280 | 4:5 | IG / LinkedIn in-feed portrait |
| Feed square | `--size=square` | 1024×1024 | 1:1 | IG grid tile, avatar-safe crop |
| Story / Reel 9:16 | `--size=1080x1920` | **1088×1920** (1080 snaps to 1088) | ~9:16 | IG / TikTok / Shorts story |
| Portrait 2:3 (built-in) | `--size=portrait` | 1024×1536 | 2:3 | default poster portrait |
| Landscape 3:2 | `--size=landscape` | 1536×1024 | 3:2 | slide, blog inline |
| Link-preview / OG | `--size=1200x630` | **1200×624** (630 snaps to 624) | ~1.9:1 | Open Graph / share card |
| Wide hero 2:1 | `--size=hero-2to1` | 2560×1280 | 2:1 | site header, LinkedIn banner, email hero |
| Ultra-wide banner 3:1 | `--size=banner-3to1` | 3072×1024 | 3:1 (**max allowed**) | YouTube / site banner strip |
| Print poster XL | `--size=poster-xl` | 2048×3072 | 2:3 | large-format print |
| Transparent cutout | any size **+ `--rembg`** | `<file>_alpha.png` | — | logo / sticker / PDP cutout |
| Motion | route to a video service | MP4 | — | reel / trailer from the locked still |

> Anything beyond 3:1 (e.g. a true 4:1 skyscraper) is **rejected by `generate.js`** — `banner-3to1` is the widest legal frame. Push wider only by compositing two exports, never by an invalid `--size`.

## Execution

Seven steps. Each forces a decision and, where it touches generation, stages the exact gated command — nothing here fires a paid API.

### Step 1 — Confirm a LOCKED winner (the entry gate)
Pull the one winner from the Studio Job's `## 7 · Critique + Refine Log`: its render path (`out/<winner>.png`), its `.brief.json` (from WF-05), its `styles.js` id, and its color tokens. **If no single winner is locked, HALT and run `/fantastic-critique-refine`.** Packing an un-critiqued render just multiplies its flaw. Only the winner is packed — never the spread.

### Step 2 — Derive the format set from the deployment surface (not a checklist)
Name every place this concept actually ships, then map each to a row of the Size Surface table above. Force a needed/skip decision per row — a print A-frame needs `poster-xl`, not a 9:16 story; a paid-social concept needs feed 4:5 + story 9:16 + maybe an OG card, not a 2048×3072 print file. Over-packing is wasted spend; under-packing is a re-brief next week. Write the chosen subset; that subset *is* the pack.

### Step 3 — Choose the reframe mode per format (concept-survives vs composition-survives)
A reframe is not a resize. Pick one of two tactics per format, based on what must survive the crop:

| Mode | Command shape | Survives | Use when |
|---|---|---|---|
| **Re-brief** (recompose) | reuse the winner's `.brief.json` + new `--size` | the *concept* (model recomposes for the new aspect) | typographic posters, where the idea matters more than pixel-identical layout; the cleanest reframe |
| **Edit-reframe** (preserve) | `--input=out/<winner>.png [--mask]` + new `--size` | the *exact winning composition* (extend / crop the frozen pixels) | hard-won photoreal or collage frames where the specific render must carry across |

Re-brief (recompose):
```bash
node skills/fantastic-posters/generate.js --brief=<winner>.brief.json --size=1080x1920 --quality=medium
```
Edit-reframe (preserve the winning pixels; mask is B/W — white = fill/extend, black = preserve the leverage element):
```bash
node skills/fantastic-posters/generate.js "extend the field to the sides, keep the hero mark centered and untouched" \
  --input=out/<winner>.png --mask=<protect>.png --size=hero-2to1 --quality=high
```
`--mask` requires an edit-mode reference (`--input`/`--refs`/`--template`) — the generator ignores a bare mask. On the photoreal/Higgsfield lane, Higgsfield's purpose-built `outpaint_image` (uncrop a still) and `reframe` (re-aspect a video) are the cleaner extend tools — both gated by `higgsfield_budget_guard.py`.

### Step 4 — Re-check the 10/5/1 ladder per aspect (the taste gate of this stage)
**A new aspect is a new hierarchy.** For every target format, re-run the Transferability lens (`/satori-lift-audit`, LIFT's T) against the recognition ladder: what wins at 10 m (thumbnail / across-the-room), 5 m (pull-closer), 1 m (reward-the-read)? A concept engineered vertical (2:3 poster, leverage top-center) can *die* when squeezed to 3:1 banner (eye now travels left→right, vertical stacking collapses) or cropped to 1:1 (edges lost). For each format decide: does the leverage point still dominate after the crop?
- **Holds** → a straight `--size` re-brief is enough.
- **Breaks** → the reframe needs a *recomposition directive* in the prompt (move the leverage, re-stack the type, re-balance negative space for the new axis), not just a size flag. Note that directive in the row. A story that shrinks a wall-poster to unreadable is a T-veto — recompose, don't just resize.

### Step 5 — Set quality per use (draft social low, print final high)
Match `--quality` to how the format is consumed, and price the pack:

| Consumption | `--quality` | Cost/img | Formats |
|---|---|---|---|
| Throwaway / social draft | `low` | ~$0.011 | first-look feed/story checks |
| Social final | `medium` | ~$0.04 | shipped feed 4:5, story 9:16, OG card |
| Print / hero final | `high` | ~$0.17 | `poster-xl`, `hero-2to1`, client-facing banner |

`--variants=1..4` gives cheap siblings of one format in a single API call (still billed N×) when you want alternates of a crop; reserve `--n=N` (N separate calls, per-call diversity nudge) only if you genuinely want variation — cross-format variety already came from the surface, so `--variants` is usually the right lever here.

### Step 6 — Stage the transparent + motion extensions
Two deployment levers the v1 skill never reached for:
- **Transparent cutout** — append `--rembg` to any generation to chain background removal and write `<file>_alpha.png` alongside (+~$0.005). This is the logo/sticker/PDP-cutout format. Pair with `--logo=<path>` when an exact wordmark must survive untouched.
  ```bash
  node skills/fantastic-posters/generate.js --brief=<winner>.brief.json --size=square --rembg --quality=high
  ```
- **Motion** — the locked still becomes a video start-frame. Route the motion cut through the router first, then double-gate it:
  ```bash
  python3 execution/creative_router.py route --task "<5s reveal animating the locked winner>" --json
  # multi-shot / cuts → fal-kling · cheap single clip → fal-seedance-720p · cinematic single → higgsfield-cinema · premium hero → veo-3
  python3 execution/fal_video_kling.py --prompt "<motion beat>" --start-image "out/<winner>.png" --duration 5 --audio off
  ```
  Motion never routes to `generate.js`. Seedance 1080p is HARD-BLOCKED — motion is 720p or Kling.

### Step 7 — Assemble the Format Pack Plan block
Collate every chosen format into the block (template in Output Requirements): one row per format = `--size` flag · resolved px · use · quality · full gated command · reframe mode · ladder verdict. Mark needed vs skipped for the Stage 0 surface, and restate the pack's total estimated spend. This block is the deliverable — the exports are downstream of a human running the gated commands it stages.

## Content-Type Adaptations

The concept is fixed; which formats a surface actually *needs* — and how the crop threatens hierarchy — shifts by content type.

| Surface | Formats the pack leans on | Reframe risk (Step 4) | Cutout / motion |
|---|---|---|---|
| **Poster / print** | `poster-xl` (final, `high`), `hero-2to1` (digital hero), `portrait` (proof) | Vertical hero-read must survive a wall at 10 m; do NOT force it into 3:1 — recompose or skip | rarely `--rembg`; motion = a slow print-to-screen trailer |
| **Logo / identity** | `square` + **`--rembg`** (alpha), `1024x1280` lockup, one-color check | Mark must read at 64 px thumbnail AND on light/dark; if it dies small, it's not transferable — back to WF-07 | `--rembg` IS the deliverable; `--logo=` holds the exact wordmark; motion = a build-on reveal |
| **Social / feed** | feed `1024x1280` (4:5), story `1080x1920` (9:16), `square`, OG `1200x630` | Leverage must live in the top-third for the story thumbnail; 4:5↔9:16 transfer is non-negotiable | motion cut (`fal-kling`/`higgsfield-cinema`) is often the hero asset, not the still |
| **Product / photoreal** | `hero-2to1` (PDP hero), `1024x1280` (feed), `square` + `--rembg` (PDP cutout) | Prefer **edit-reframe** (`--input`) or Higgsfield `outpaint_image` to hold the exact photoreal frame; a re-brief may re-roll the product | `--rembg` for the on-white PDP cutout; motion = a Soul/Seedance product reveal |
| **Packaging** | `poster-xl` (dieline panel), `hero-2to1` (shelf/hero mockup), `--refs=` a dieline template | Panel proportions are fixed by the dieline — reframe via `--template`/`--refs`, not a free `--size` | photoreal shelf mockup → Higgsfield Soul, not `generate.js` |
| **Video / motion** | motion is the primary format; still exports are keyframes only | aspect is set by the platform (9:16 reel vs 16:9 hero) — `fal_budget_guard.py` pre-flight per duration | route via `creative_router.py`; Higgsfield `reframe` to re-aspect an existing clip (gated) |

## Output Requirements

This stage writes exactly one named block into the accumulating **Studio Job**, closing it out:

```markdown
## 8 · Format Pack Plan (WF-08 · /fantastic-format-pack)

**Locked winner**: [direction name] · render `out/<winner>.png` · brief `<winner>.brief.json` · style `<styles.js id>`
**Deployment surface**: [where this concept ships]

| Format | --size flag | Renders at | Use | Quality | Reframe mode | Ladder verdict (10/5/1) | Gated command | Needed? |
|---|---|---|---|---|---|---|---|---|
| Feed 4:5 | `--size=1024x1280` | 1024×1280 | IG/LI in-feed | medium | re-brief | holds | `python3 execution/cost_gate.py check --service fal-poster --request "feed 4:5"` → approve → `node skills/fantastic-posters/generate.js --brief=<winner>.brief.json --size=1024x1280 --quality=medium` → log | ✓ |
| Story 9:16 | `--size=1080x1920` | 1088×1920 | IG/TikTok story | medium | re-brief + recompose (leverage → top third) | recompose | `… --service fal-poster …` → `… --brief=<winner>.brief.json --size=1080x1920 --quality=medium` | ✓ |
| Hero 2:1 | `--size=hero-2to1` | 2560×1280 | site / LI banner | high | edit-reframe (`--input` + `--mask`) | recompose (horizontal eye journey) | `… --input=out/<winner>.png --mask=<protect>.png --size=hero-2to1 --quality=high` | ✓ |
| Print XL | `--size=poster-xl` | 2048×3072 | large-format print | high | re-brief | holds | `… --brief=<winner>.brief.json --size=poster-xl --quality=high` | ✓ |
| Transparent | `--rembg` | `_alpha.png` | logo / PDP cutout | high | + `--rembg` | n/a | `… --size=square --rembg --quality=high` | ○ |
| Motion | video service | MP4 | reel / trailer | n/a | still → start-frame | n/a | `python3 execution/fal_budget_guard.py check --mode=kling --duration=5 --audio=off` → `python3 execution/fal_video_kling.py --start-image out/<winner>.png …` | ○ |

**Reframe-mode notes**: [which formats recompose vs hold; recomposition directives per broken aspect]
**TOTAL ESTIMATED SPEND (pack)**: $N.NN — approved by the human before any reframe fires.
⚠️ This plan STAGES reframe commands off ONE locked concept. It fires nothing. Every row starts with a `cost_gate.py check` (video adds `fal_budget_guard.py`). No format silently re-designs the idea.
```

The block is complete only when: every format derives from the *same* locked winner (a shared `.brief.json` / `styles.js` id, not a new concept), every row carries its resolved pixel size + quality + the full three-step gated command, every non-holding aspect has a recomposition directive from Step 4, the cutout uses `--rembg` and motion routes to a video service (never `generate.js`), and the pack total is summed and visible.

## Cost & Safety

This stage **PLANS and STAGES**. Every format is fresh paid generation and is **cost-gated + human-triggered** — WF-08 never fires a paid API and never runs `approve`.

- **Every** format pre-flights the cost gate, then (only on an explicit human yes to a needs-approval) approves, runs, and logs:
  ```bash
  python3 execution/cost_gate.py check   --service fal-poster --request "<format> reframe of <winner>"
  python3 execution/cost_gate.py approve --service fal-poster          # ONLY after Farrice says yes (15-min token)
  node skills/fantastic-posters/generate.js --brief=<winner>.brief.json --size=<preset> --quality=<q>
  python3 execution/cost_gate.py log     --service fal-poster --status success --actual-cost <n>
  ```
- **Motion formats are double-gated** — cost gate *and* budget guard:
  ```bash
  python3 execution/fal_budget_guard.py check --mode=kling --duration=<N> --audio=off
  python3 execution/fal_budget_guard.py check --mode=seedance-720p --duration=<N>
  ```
  **Seedance 1080p is HARD-BLOCKED** — reframe motion to 720p or Kling, never 1080p.
- **Higgsfield reframe/outpaint** (`outpaint_image`, `reframe`, `generate_video`) is credit-gated via `python3 execution/higgsfield_budget_guard.py check --operation image_preview|marketing_studio_video --count <N>` before any call.
- **Pack the winner only, at the right quality**: `low` for draft social, `medium` for shipped social, `high` reserved for print/hero finals. Never run a format pack across the divergence spread — that is where a $0.30 concept becomes an $8 mistake. Denied gate → surface to Farrice and stop; do not retry.

The human reviews the Format Pack Plan, then pulls each trigger behind the cost gate. Satori decided, the router picked the instrument, the studio critiqued its own work — this stage just presses the survivor into every frame it has to live in, one gated command at a time.

## Related Workflows

**The Fantastic Studio stack** (this stage sits at position 8, the deployment close):
- `/fantastic-critique-refine` (WF-07) — locks the ONE winner this stage packs (hard upstream dependency)
- `/fantastic-prompt-compile` (WF-05) — produced the `<winner>.brief.json` every format reuses
- `/fantastic-model-route` (WF-04) — the routing table this stage reuses for the motion format
- `/fantastic-studio` (WF-00) — the front-door orchestrator that runs all eight stages and embeds this block

**Composed thinking** (Step 4 transferability re-check): `/satori-lift-audit` (LIFT-T against the 10/5/1 ladder) · `/satori-perception-gap` (does the reframed reading still match intent?).

**Legacy format/deploy patterns this stage generalizes** (concrete, brand-bound recipes to lift commands from):
- `workflows/poster-to-video.md` — the poster→video bridge (Kling / Seedance presets, budget envelopes) for the motion format
- `workflows/kling-multishot.md` — multi-shot narrative reframe (3-act trailer from one still)
- `workflows/deliverable-cover.md` — the print-final `--quality=high` cover pattern (poster-xl / portrait)
- `workflows/mybpm-products.md` — brand-guardrail drops with `--palette` + `--rembg` cutouts across social sizes

**Adjacent Creative Director** (when a motion or photoreal reframe leaves the poster lane): `/art-direct` · `/storyboard` for Higgsfield sequences; `execution/creative_router.py` is the shared switchboard.

**Downstream generation** (human-triggered, cost-gated): `generate.js` (Fal, every `--size`/`--rembg` reframe) · `fal_video_kling.py` / `fal_video_seedance.py` (motion) · Higgsfield MCP `generate_image` / `generate_video` / `outpaint_image` / `reframe` (photoreal/video reframe) · `veo-3` via Google Flow (premium motion).
