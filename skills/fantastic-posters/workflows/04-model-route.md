---
description: Route every divergence direction to the model that actually renders it best — a per-direction Routing Table (service · why · est cost · exact pre-flight command) that takes the whole creative surface instead of defaulting to GPT Image 2.
---

# 04 — Model Route (/fantastic-model-route)

> The instrument-picker. Satori decided *what* the design must do; this stage decides *which tool renders each direction* and prices the spread — so a photoreal person never gets forced through a poster model and a typographic drop never wastes a Soul credit.

The whole point of this build is to stop the one-tool reflex. fantastic-posters made GPT Image 2 the hammer and every direction the nail. This stage restores the full surface: Fal poster/edit/rembg, Higgsfield Soul/Nano/Cinema, Kling, Seedance, Veo — each direction routed to the cheapest-good-enough instrument for *that* payload, with the exact cost gate command attached so nothing fires blind.

## Pre-Flight Gate

**Use this when**:
- You have a set of **divergence directions** (the WF-03 spread) and need each one matched to a tool before anyone spends a cent.
- A single direction is about to be generated and you want to confirm GPT Image 2 is actually the right model — not the default.
- A spread mixes payload types (a typographic hero, a photoreal lifestyle shot, a logo cutout, a motion teaser) and you need one table that prices the whole run.
- You inherited a Studio Job that routed everything to `fal-poster` and you smell the one-tool reflex.

**Do NOT use this when**:
- There are no directions yet — go back and run `/fantastic-diverge` (WF-03). Routing an empty spread produces a table of nothing.
- The concept/brief isn't locked — routing before the Satori Production Brief exists means you're pricing guesses. Run `/satori-design-think` (WF-20) → `/fantastic-studio-brief` (WF-01) first.
- You already have a committed one-direction, one-model plan and just need to fire it — skip to `/fantastic-generate` (WF-05); this stage is overhead when there's nothing to route.
- The output is pure copy/headline/script — that's `gemini-text`, not an image/motion model. Route it to the writing roster, not here.

**Hard rule this stage enforces**: routing **plans and prices — it never fires a paid API.** Every command written into the table is a *pre-flight* `check`, never an `approve` and never a generation call. The human reads the table, approves the total, and only then does WF-05 trigger generation behind the cost gate.

## Skill Acquisition

```
Load: skills/fantastic-posters/genius.md
  ├─ The Capability Decision Tree ...... the routing spine (mirrored below — genius.md is canonical)
  ├─ The One-Tool Reflex (Anti-Pattern) . why defaulting to GPT Image 2 is the failure this stage fixes
  ├─ The 38 Styles as Primitives ....... fal-poster is ONE service with 38 art-direction primitives, not 38 services
  └─ Reference-Dependency Ledger ....... which routes need an asset before they can generate

Composes (load as needed — Tier 1.5 hot-context; skip re-read if already loaded):
  skills/satori-graphics/workflows/20-design-think.md → /satori-design-think  (the brief this stage prices)
  skills/creative-direction/…                         → /art-direct           (upstream art direction for Higgsfield/Kittl/Flux routes)

Drives (the REAL code — read to confirm flags, never invent them):
  execution/creative_router.py    → the transparent routing table (route --task "<dir>" --json)
  skills/fantastic-posters/generate.js → the fal-poster/edit/rembg surface (--style/--refs/--template/--input/--mask/--rembg/--variants)
  skills/fantastic-posters/styles.js   → the 38 style primitives (needsPhoto flag = reference required)
  execution/cost_gate.py          → the mandatory pre-flight (check --service <id>)
  execution/fal_budget_guard.py   → video double-gate (check --mode=kling|seedance-720p --duration=N)
  execution/higgsfield_budget_guard.py → Higgsfield credit gate (check --operation image_preview|marketing_studio_video)
```

## The Capability Decision Tree (canonical in genius.md — mirrored here)

Classify each direction by its **payload**, not its vibe. First branch that fits wins.

| The payload is… | Route to | Service id | Instrument |
|---|---|---|---|
| **Typographic poster · text-in-image · stylized/branded graphic** | fantastic-posters | `fal-poster` | GPT Image 2, 38 style primitives |
| **Photoreal + PEOPLE · product hero · character consistency** | Higgsfield Soul | `higgsfield-soul` | Soul 2.0 (best photoreal; ref for character) |
| **Cheap/fast iteration · concept sketch · throwaway variation** | Higgsfield Nano | `higgsfield-nano` | Nano Banana Pro (fastest/cheapest) |
| **Edit an existing image** (swap/replace/inpaint/outpaint) | Fal edit | `fal-edit` | GPT Image 2 edit — needs `--input` (+ `--mask` for surgical) |
| **Transparency · logo cutout · alpha PNG** | Fal rembg | `fal-rembg` | background removal (chain via `--rembg`, +~$0.005) |
| **Motion — multi-shot / cuts / sequence** | Kling | `fal-kling` | Kling v3 Pro (handles cuts) |
| **Motion — cinematic single shot, 5–10s** | Higgsfield Cinema | `higgsfield-cinema` | Cinema Studio 3.5 |
| **Motion — cheap single-shot clip** | Seedance 720p | `fal-seedance-720p` | 720p only — **1080p HARD-BLOCKED** |
| **Motion — premium hero spot** | Veo | `veo-3` | Veo 3.1, Ultra quota ($0 marginal, sparingly) |
| **Predict engagement / hook strength** | Higgsfield virality | `higgsfield-virality` | virality predictor (analysis, not gen) |
| **Copy / headline / script** | Gemini text | `gemini-text` | route to writing roster |

> **Unsure between Higgsfield models (Soul vs Nano vs Cinema)?** Do not guess. Call `mcp Higgsfield models_explore action:recommend` with the goal + input context and let it pick.

## Execution

Nine directions or one, the loop is the same: **classify → confirm with the router → resolve ambiguity → flag references → price + gate → table it.** Each step forces a decision you must be able to defend.

### Step 1 — Load the Divergence Spread
Pull every direction out of the Studio Job's `## Divergence Spread` block (WF-03). Each direction is a named angle with a subject and an intent (e.g. *"D2 · Founder-in-gym lifestyle shot, resistance bands, trust-building"*). If the block is missing or empty, **halt and run `/fantastic-diverge`** — routing nothing produces nothing.

### Step 2 — Classify the payload (decide before you touch the router)
For each direction, answer one question out loud and write it down: **is the payload TEXT-IN-IMAGE, PHOTOREAL-PEOPLE, ITERATION, EDIT, TRANSPARENCY, or MOTION?** This is the decision the tree keys on. Committing to the payload class *before* running the router is what stops you rubber-stamping whatever the first regex matches.

### Step 3 — Confirm with the router (real command)
Run the transparent router for each direction:
```bash
python3 execution/creative_router.py route --task "<direction description>" --json
```
Read the returned `service`, `reason`, `matched_pattern`, and `cost_gate_cmd`. The router is **first-match-wins on signal words** — if it disagrees with your Step-2 payload class, that almost always means your task string lacked a signal word (e.g. you meant photoreal-people but never wrote "photoreal"/"product hero"). **Sharpen the description and re-run** rather than overriding blindly. Your payload classification wins on the *kind* of asset; the router's job is to name the service and hand you the exact pre-flight string.

### Step 4 — Resolve Higgsfield ambiguity (don't guess Soul vs Nano vs Cinema)
When a direction is photoreal or motion and the right Higgsfield model isn't obvious, call:
```
mcp Higgsfield models_explore  action: recommend   (goal + input context)
```
Use its recommendation. Soul for finished photoreal + people/character; Nano for cheap fast iteration; Cinema for cinematic single-shot motion. Never spend a Soul credit on a throwaway concept sketch, never ship a Nano frame as a product hero.

### Step 5 — Flag reference dependencies
Mark every direction whose best model **needs an asset that must exist before generation**:
- **`higgsfield-soul` character consistency** → needs a Soul reference element / character. Upload first via `mcp Higgsfield media_upload` (or `media_upload_widget` for a local file), then generate against it.
- **`fal-poster --template=<png>`** → needs the existing poster whose layout you're replicating.
- **`fal-poster --refs=hero.jpg,brand.pdf,logo.png`** or **`--logo=<path>`** → needs those brand assets on disk.
- **`fal-edit --input=<url|path>`** (+ optional **`--mask`**) → needs the source image (and a B/W mask for surgical region edits).
- **A style with `needsPhoto`** (see `styles.js`) → needs `--ref`.

For each flagged direction, name the asset and where it comes from. A route that silently assumes a missing reference will fail at generation — surface it now.

### Step 6 — Price it and attach the exact pre-flight command
Write the per-image / per-clip est cost (table below) and the **exact** gate command(s) for each direction. Do not collapse two directions onto one service without re-pricing — three directions on `fal-poster --quality=high` is 3 × $0.17, not $0.17.

- **Every paid direction** gets the cost-gate check the router already handed you:
  ```bash
  python3 execution/cost_gate.py check --service <id> --request "<direction>"
  ```
- **Video directions** get a second gate (budget guard):
  ```bash
  python3 execution/fal_budget_guard.py check --mode=kling --duration=<N> --audio=off
  python3 execution/fal_budget_guard.py check --mode=seedance-720p --duration=<N>
  ```
- **Higgsfield directions** (Soul/Nano/Cinema) get the credit gate:
  ```bash
  python3 execution/higgsfield_budget_guard.py check --operation image_preview --count <N>
  python3 execution/higgsfield_budget_guard.py check --operation marketing_studio_video --count <N>
  ```

### Step 7 — Assemble the Routing Table + total
Collate every direction into the Routing Table (template in Output Requirements), sum the est spend across the spread, and subtotal by service. **This total is the number the human approves at the WF-05 generation gate.** A spread that has quietly ballooned to $9 in video should be visible here, before a single frame renders.

## Cost Reference (grounded — confirm the live numbers, never invent)

| Service | Est cost | Notes |
|---|---|---|
| `fal-poster` / `fal-edit` | per image: low **$0.011** · medium **$0.04** · high **$0.17** | `--variants=N` = N images in ONE call but still billed N×; `--n=N` = N separate calls. Medium for first pass, high only for finals. |
| `fal-rembg` | **+~$0.005** / image | chained via `--rembg` alongside a poster, or standalone for a cutout. |
| `higgsfield-soul` | est **$0.10** / image, ceiling **$0.50** | credit-metered; character consistency needs a reference element. |
| `higgsfield-nano` | cheapest Higgsfield tier (credit-metered) | confirm exact credits via `mcp Higgsfield show_plans_and_credits` / `balance`. |
| `higgsfield-cinema` | est **$1.50** / clip (5–10s) | for longer / multi-shot prefer Kling. |
| `fal-kling` | est **$2.00** / clip | budget guard returns the precise per-duration figure (e.g. ~$0.84 @ 5s). |
| `fal-seedance-720p` | ceiling **$3.00** (~10s max) | **1080p HARD-BLOCKED** — never route to 1080p. |
| `veo-3` | **$0** marginal (Ultra quota) | premium hero spots only; quota is limited per day. |

## Content-Type Adaptations

| Content type | Default route | Why | Reference needed? |
|---|---|---|---|
| **Poster / print** | `fal-poster` (style primitive) | Text-in-image + typographic control is GPT Image 2's home turf; the 38 styles are art-direction primitives, not a keyword menu. | Only if replicating a layout (`--template`) or brand-locking (`--refs`/`--logo`). |
| **Logo / identity** | `fal-poster --logo` → chain `fal-rembg` | Exact wordmark stays intact (`--logo` = no redraw); rembg yields the transparent alpha. | **Yes** — the wordmark file for `--logo`. |
| **Social / feed** | `fal-poster` (static) · `higgsfield-cinema`/`fal-kling` (motion) | Thumbnail-legible typographic frame for static; short motion for scroll-stop. Confirm square↔vertical holds. | No for static; motion may want a Soul keyframe. |
| **Product / photoreal** | `higgsfield-soul` | Best photoreal + people/product-hero; Nano only for the cheap first-look. | **Yes for character/product consistency** — a Soul reference element. |
| **Packaging** | `fal-poster` (dieline art) · `higgsfield-soul` (photoreal mockup) | Flat stylized panel from Fal; photoreal shelf/hero render from Soul. | Photoreal mockup wants a reference; dieline art usually doesn't. |
| **Video / motion** | `fal-kling` (cuts) · `higgsfield-cinema` (single cinematic) · `fal-seedance-720p` (cheap) · `veo-3` (hero) | Match to shot structure: sequence→Kling, one cinematic take→Cinema, budget clip→Seedance 720p, premium→Veo. | Image-to-video routes want a keyframe (often a Soul/poster still). |

## Output Requirements

This stage writes exactly one named block into the accumulating **Studio Job**, consumed by `/fantastic-generate` (WF-05):

```markdown
## Routing Table (WF-04 · /fantastic-model-route)

| # | Direction | Service | Why (payload → tool) | Ref needed? | Est cost | Pre-flight command |
|---|---|---|---|---|---|---|
| D1 | [angle] | fal-poster | text-in-image → GPT Image 2 | — | $0.04 (med) | `python3 execution/cost_gate.py check --service fal-poster --request "D1 …"` |
| D2 | [angle] | higgsfield-soul | photoreal person → Soul | ⚑ Soul ref element | $0.10 (ceil $0.50) | `python3 execution/cost_gate.py check --service higgsfield-soul --request "D2 …"` + `python3 execution/higgsfield_budget_guard.py check --operation image_preview --count 1` |
| D3 | [angle] | fal-kling | multi-shot motion → Kling | ⚑ keyframe still | ~$2.00 / clip | `python3 execution/cost_gate.py check --service fal-kling --request "D3 …"` + `python3 execution/fal_budget_guard.py check --mode=kling --duration=5 --audio=off` |

**Reference-dependency flags**: [list every ⚑ direction + the asset that must exist first + where it comes from]

**Subtotal by service**: fal-poster $X · higgsfield-soul $Y · fal-kling $Z
**TOTAL ESTIMATED SPEND (spread)**: $N.NN  — approved by the human at the WF-05 gate before any generation fires.
⚠️ This table PLANS and PRICES. It fires nothing. Every command above is a `check`, not an `approve` or a generation call.
```

The table is complete only when: every direction has a service justified by its payload class (not vibe), every ⚑ reference dependency names its asset, every paid row carries the exact `cost_gate.py check` string (plus the video/Higgsfield second gate where it applies), and the total is summed and visible.

## Quality Gate

Before the Routing Table hands off to WF-05, verify:

- [ ] **Payload classified before routing** — TEXT-IN-IMAGE / PHOTOREAL-PEOPLE / ITERATION / EDIT / TRANSPARENCY / MOTION decided per direction, not inferred backward from whichever service `creative_router.py` happened to match.
- [ ] **Router confirmed, not overridden blind** — every row's service matches `creative_router.py route --task ... --json`, or carries a written override reason.
- [ ] **Not everything defaulted to fal-poster** — the one-tool reflex this stage exists to kill; a spread with real photoreal/motion directions shows real Higgsfield/Kling/Seedance rows.
- [ ] **Every ⚑ reference dependency is named** — the asset and its source, so generation doesn't fail on a missing ref it could have flagged now.
- [ ] **Every paid row carries its exact gate command(s)** — `cost_gate.py check`, plus `fal_budget_guard.py` / `higgsfield_budget_guard.py` where the service requires it — and the subtotal + total are visible.

**Pass criteria**: all checked. A table that "looks routed" but silently sends a photoreal-people direction to `fal-poster` fails this gate regardless of how complete it looks.

## Cost & Safety

This stage **PLANS**. Generation is **cost-gated and human-triggered** — WF-04 never fires a paid API and never runs `approve`.

- Mandatory pre-flight for any paid gen (the router hands you this string; the human runs it at WF-05):
  ```bash
  python3 execution/cost_gate.py check --service <id> --request "<direction>"
  ```
- **Never auto-fire the cost gate.** On `needs-approval`, surface to Farrice; only after an explicit yes does WF-05 run `cost_gate.py approve --service <id>` (15-min token), generate, then `cost_gate.py log --service <id> --status success --actual-cost <n>`.
- **Video is double-gated** — cost gate *and* budget guard:
  ```bash
  python3 execution/fal_budget_guard.py check --mode=kling --duration=<N> --audio=off
  python3 execution/fal_budget_guard.py check --mode=seedance-720p --duration=<N>
  ```
  **Seedance 1080p is HARD-BLOCKED** — route motion to 720p or Kling, never 1080p.
- **Higgsfield is credit-gated** via `higgsfield_budget_guard.py check --operation image_preview|marketing_studio_video --count <N>` before any Soul/Nano/Cinema/MCP generation.
- The Routing Table's TOTAL is the single number the human approves. If it surprises you, the spread is wrong — return to `/fantastic-diverge`, not to a bigger budget.

## Related Workflows

**The Fantastic Studio stack** (this stage sits at position 4 — Satori decides, the router picks the instrument, the studio critiques its own work):
- `/fantastic-studio-brief` (WF-01) — ingest the Satori Production Brief into the Studio Job
- `/fantastic-primitive-select` (WF-02) — map the concept to the 38 style primitives (not a keyword match)
- `/fantastic-diverge` (WF-03) — the Divergence Spread this stage consumes
- **`/fantastic-model-route` (WF-04) — this stage**
- `/fantastic-generate` (WF-05) — human-triggered, cost-gated generation of the approved table
- `/fantastic-self-critique` (WF-06) — LIFT / flip audit of the rendered output

**Composed / upstream (Satori is the brain)**:
- `/satori-design-think` (WF-20) — the end-to-end brief that feeds the whole studio
- `/satori-color` (WF-17) · `/satori-lift-audit` (WF-01) — tokens + hierarchy the routes render

**Adjacent creative routing**:
- `/art-direct`, `/mood-board`, `/storyboard` (Creative Director) — art direction for the Higgsfield / Kittl / Flux routes before generation
- `execution/creative_router.py rules` — inspect or tune the full routing table Farrice owns
