---
description: Compile each direction's Art-Direction Spec into a model-specific, richly-specified production prompt — a Fal --brief JSON, a Higgsfield Soul/Nano prompt shape, a describe-only-the-change edit instruction, or a video motion prompt — Virgil-tested and tagged for stage 6.
---

# 05 — Prompt Compile (/fantastic-prompt-compile)

> Translate every locked Art-Direction Spec into the exact prompt its target model was built to read — rich single-scene specification, never a stack of keywords — and hand stage 6 a generation-ready Compiled Prompts block.

This is the translation stage. Stage 3 chose the instrument, Stage 4 wrote the decisions (subject, LIFT hierarchy, hex tokens, feeling, memory hook, anti-slop moves). Stage 5 does one thing: render those decisions into the grammar the chosen model actually parses. A keyword-stuffed template ("moody, cinematic, professional, high-quality, 4k") throws every decision away and lets the model default. A compiled prompt encodes the decisions as a scene the model can only render one way. **Satori decided, the router picked the instrument — here the studio speaks the instrument's language.**

## Pre-Flight Gate

**Run this when:**
- Stage 4 (`/fantastic-art-direct`) has produced one or more **locked** Art-Direction Specs, and each direction carries a **model tag** from Stage 3's route (fal-poster / fal-edit / higgsfield-soul / higgsfield-nano / fal-kling / fal-seedance-720p / higgsfield-cinema).
- You want the prompt to *carry* the hierarchy, palette, and hook — not restate them as adjectives.

**Route elsewhere when:**
- **No Art-Direction Spec yet** → run `/fantastic-art-direct` (WF-04) first. A spec-less compile invents its own hierarchy and every downstream pixel inherits the guess.
- **The model tag is missing or contested** → confirm it before you shape a prompt for the wrong model: `python3 execution/creative_router.py route --task "<direction description>" --json`.
- **The brief itself is unclear** (no communication problem, no hidden truth) → back up to `/satori-design-think`. You cannot compile a prompt for a concept that does not exist.
- **You only want to nudge one already-generated image** and there is no spec behind the change → that is a stage-6 re-run, not a compile. (If a spec *does* exist, use the EDIT recipe below.)

**Hard rule:** one compiled prompt per direction per model. Never merge two directions into a single prompt "to save a call" — divergence between directions is the point, and a blended prompt averages them into mush. Never compile a direction whose model tag you have not confirmed against `creative_router.py`.

## Skill Acquisition

```
Load: skills/fantastic-posters/genius.md
  ├─ The Translation Principle ..... a prompt encodes decisions, not adjectives
  ├─ Scaffold-vs-Spec .............. Fal styles are FIXED frames; the brief fills the SLOTS
  ├─ Anti-Keyword-Soup ............. one fully-realised scene beats ten stacked descriptors
  └─ The Virgil Test ............... POV · tension · cultural anchor · one-line concept

Composed brain (Satori already decided — read the spec, do NOT re-derive it):
  /satori-design-think (WF-20) ..... the Production Brief that feeds Stage 4
  /satori-color (WF-17) ............ hex tokens → Fal `palette` key / Higgsfield colour line
  /satori-lift-audit (WF-01) ....... the leverage point + 10/5/1 ladder → the composition line
  /satori-anti-ai-slop (WF-09) ..... the imperfection moves → texture/tilt/off-register clauses

Real code this stage DRIVES (it writes the exact invocation — it never fires it):
  generate.js ...... --brief=<name>.json  keys: style, subject, title, subtitle, body, footer, palette, logo
  styles.js ........ the 38 scaffolds; run `node generate.js --list` to confirm ids + needsPhoto flags
  execution/creative_router.py ......... confirms each direction's model tag
  execution/fal_video_kling.py / fal_video_seedance.py ... the video-direction wrappers
  Higgsfield MCP (via ToolSearch): mcp__claude_ai_Higgsfield__generate_image / generate_video / models_explore
```

## Execution

Nine steps. Steps 1-2 set up, Steps 3-7 are the five model recipes (run only the ones your directions are tagged for), Step 8 is the taste gate, Step 9 assembles.

### Step 1 — Inventory the directions and re-confirm every model tag

List the locked directions from Stage 4. For each, state its model tag in one line and confirm it against the router (the tag is only trustworthy if the router still agrees):

```bash
python3 execution/creative_router.py route --task "<one-line description of this direction>" --json
```

**Decision forced:** for each direction, is the Stage-3 tag still correct, or did the spec drift toward a different instrument (e.g., a "photoreal founder" direction that Stage 4 turned into a typographic treatment now belongs to fal-poster, not higgsfield-soul)? Retag before compiling. A prompt shaped for the wrong model is wasted work no matter how good the writing.

### Step 2 — Branch each direction to its recipe

| Model tag | Recipe | Deliverable of the compile |
|---|---|---|
| `fal-poster` | Step 3 | a `--brief=<name>.json` (the JSON emitted in full) + run command |
| `higgsfield-soul` | Step 4 | a photoreal prompt in Soul's shape + reference plan |
| `higgsfield-nano` | Step 5 | a short Nano prompt for cheap iteration |
| `fal-edit` | Step 6 | an `--input` + describe-only-the-change instruction (+ `--mask` if surgical) |
| `fal-kling` / `fal-seedance-720p` / `higgsfield-cinema` | Step 7 | a start-frame + motion/camera prompt + wrapper command |

### Step 3 — FAL / GPT Image 2 → the `--brief` JSON

GPT Image 2 is fed through a **style scaffold**: each of the 38 styles in `styles.js` is a fixed aesthetic frame (`build(i)`) with variable slots (`subject`, `title`, `subtitle`, `body`, `footer`) that your brief fills. Compiling means choosing the scaffold whose *fixed* language matches the spec, then loading every slot with fully-specified content. Force these decisions in order:

1. **Pick the scaffold, don't keyword-match it.** `node generate.js --list` shows all 38 ids and their `needsPhoto` flags. Choose the style whose hardcoded framing (orientation, medium, grid, whitespace) already agrees with the Art-Direction Spec — then you're overriding slots, not fighting the frame. (The auto-picker `pickStyle()` grabs the first keyword hit; you are doing better than that on purpose.) If the scaffold needs a photo (`needsPhoto: true`, e.g. `luxury-real-estate`), the direction requires a `--refs=<hero>.jpg` and you flag it.
2. **Write `subject` as ONE fully-realised scene.** This is the payload — a sentence to a short paragraph that names the subject, states the **composition and leverage point** (what dominates and where), and traces the eye. Bake the **10/5/1 ladder** straight in: the largest element is the 10 m read, the mid element the 5 m pull, the fine detail the 1 m reward. Fold the Stage-4 **anti-slop moves** in here as concrete clauses — one per zone, never clustered (a 2-7° tilt near the hero, an off-register edge in a secondary zone, a hand-drawn line at texture level). Name **texture** and **negative space** explicitly. This single scene replaces every loose adjective.
3. **Set the lettering slots to exact copy.** `title`, `subtitle`, `body`, `footer` render as literal type. Keep `title` to **≤6 words** — GPT Image 2's lettering is reliable up to ~6 words and drifts into typos past that (SKILL: "If a title has more than ~6 words, expect typos"). Footer is always last: date · venue · price/credit.
4. **Set `palette` to the Satori hex tokens**, comma-separated. This is injected as a *strict* override that beats the scaffold's defaults, so the Stage-4 color decision wins.
5. **Handle the wordmark honestly.** If the direction needs an exact logo, set `logo` to the asset **path** — it routes to the edit endpoint and auto-adds the "do NOT redraw" clause. Then **flag it**: logo placement fidelity is imperfect even on the edit endpoint and needs a human eyeball post-gen. If no exact mark is required, leave `logo: ""` and let the type render as lettering.
6. **Choose aspect via `--size`**, matched to the viewing context: `portrait` (wall/feed poster), `landscape`, `square`, `banner-3to1`, `hero-2to1`, `poster-xl`, or `WxH` (multiples of 16, ≤3:1, 655K-8.3MP).

**Emit the full JSON** and the run command. Worked example (a My.BPM drop-teaser direction — the hoodie as artifact):

```json
{
  "style": "streetwear-lookbook",
  "subject": "A single heavyweight cream boxy hoodie hung on a bent steel hook against a raw concrete wall. One hard diagonal shaft of daylight rakes across it from the upper-left, catching the fabric weave and a small embroidered chest mark. The hoodie is the only lit object; floor and ceiling fall into deep shadow so the eye lands on the garment silhouette first from across a room, is pulled in by the light shaft, and finally rewards a close read on the embroidery. The hook hangs at a deliberate 3-degree tilt, breaking the grid. Fine concrete grain, one soft dust mote drifting in the light.",
  "title": "DROP FOUR",
  "subtitle": "MY.BPM · SS26",
  "footer": "FRI 12 SEPT · ONLINE 09:00",
  "palette": "#0E0E10,#F2E9DC,#C6462E",
  "logo": ""
}
```

```bash
# Review pass (medium). Escalate to --quality=high only for the locked final.
node generate.js --brief=briefs/mybpm-drop4.json --size=portrait --quality=medium
```

Optional overrides that stay available on the same command: `--variants=1..4` (siblings in one API call), `--n=N` (N separate calls with a diversity nudge), `--rembg` (transparent `*_alpha.png` for cutouts), `--template=<png>` (replicate an existing layout — then the prompt names ONLY what changes).

### Step 4 — HIGGSFIELD SOUL → photoreal prompt shape

Soul (best photoreal + people/character) reads a prose prompt, not a scaffold. Compile the spec into Soul's seven-part shape, one clause each:

- **Subject** — who/what, in specific nouns.
- **Wardrobe / character** — garments, materials, physical detail that make it *this* person/object.
- **Environment** — the place, with depth cues.
- **Lighting** — direction *and* quality (e.g., "hard key from camera-left, soft bounce fill, late-afternoon warmth").
- **Lens / DoF** — focal length + depth of field (e.g., "85mm, shallow, background falls to bokeh").
- **Mood** — the Stage-1 target feeling, in one word plus a supporting image.
- **Color** — the Stage-4 hex tokens described as a grade (warm/cool, saturated/muted).

**Decision forced:** does character consistency matter across this direction (or across a set)? If yes, attach a **character reference** — confirm the right model and reference handling first, then compile the reference into the plan:

```
# via ToolSearch → load, then call:
mcp__claude_ai_Higgsfield__models_explore   action:recommend   (goal + input context)
mcp__claude_ai_Higgsfield__generate_image   (prompt + reference image)   # STAGE 6 fires this, not this stage
```

Write the prompt and the reference plan into the block; do not call the tool here (gated by `higgsfield_budget_guard.py`).

### Step 5 — HIGGSFIELD NANO → short iteration prompt

Nano Banana Pro is the fastest/cheapest instrument — use it to lock composition *before* spending Soul budget. Compress the Soul shape to its load-bearing three: **subject + one or two defining attributes + one lighting/mood cue**. Drop lens/grade detail; Nano's job is to answer "is the composition right?", not to finish. Note in the block that a Nano pass typically precedes a Soul pass for the same direction.

### Step 6 — EDIT direction → describe-only-the-change

An edit direction starts from an existing image (a prior stage-6 output or a supplied asset). Compile to an `--input` plus an instruction that describes **only the change** — never restate the whole scene, or the model redraws everything and drifts.

```bash
# Whole-image change (re-lettering, recolour, object swap):
node generate.js "change the headline to read TONIGHT, keep everything else identical" --input=out/mybpm-drop4_v1.png

# Surgical, region-locked change — add a B/W mask (white = edit, black = preserve, same dims as input):
node generate.js "replace only the garment colour with deep oxblood" --input=out/mybpm-drop4_v1.png --mask=masks/garment.png
```

**Decision forced:** is the change global or region-local? Global → `--input` alone. Local → add `--mask`. If you find yourself describing more than the change, the direction is a fresh generation (Step 3), not an edit.

### Step 7 — VIDEO direction → start-frame + motion prompt

A video direction animates a still. Compile to two things: the **start-frame image** (a locked stage-6 poster output) and a **motion/camera prompt** that says what moves and how the camera behaves — physics, not free-for-all. Pick the wrapper by the Stage-3 tag:

```bash
# Multi-shot narrative (Kling): 2-4 distinct beats, cuts between them.
python3 execution/fal_video_kling.py \
    --prompt="slow push-in on the hoodie, dust drifts through the light shaft, the embroidery catches a glint, restrained" \
    --start-image="skills/fantastic-posters/out/mybpm-drop4_v1.png" \
    --duration=5 --audio=on

# Single-shot cinematic / start→end morph (Seedance 720p): add --end-image for a transformation.
python3 execution/fal_video_seedance.py \
    --prompt="camera holds, garment settles as the light warms toward dusk, no people" \
    --image="skills/fantastic-posters/out/mybpm-drop4_v1.png" \
    --duration=6 --resolution=720p --aspect=9:16 --audio=on
```

**Decision forced:** multi-beat story (Kling, `--multi-prompt`) or single continuous move / A→B morph (Seedance, `--end-image`)? Keep the motion inside the physics implied by the start frame — Seedance interpolates, it does not invent new objects. Match POV and lighting between start and end frames.

### Step 8 — Virgil test every compiled prompt

Before a prompt is locked, run the four-question Virgil pass — the studio critiquing its own work. Each is a yes/no; any **no** sends you back to revise (almost always the `subject`/scene line), then re-test:

1. **POV** — does the prompt bake in a *point of view* (whose eyes, what stance), or is it a generic "a poster of…"? If there's no POV, add one; a viewpoint is what separates a picture from a product.
2. **Tension** — is there a friction or contradiction that gives it charge (a quiet garment shouting a drop; luxury framing on a cheap object)? Frictionless prompts render wallpaper.
3. **Cultural anchor** — does it stand on a reference the audience already holds (a form they recognise), then shift it? The recognisable-but-altered read is what makes it legible *and* new.
4. **One-sentence concept** — can you say what it IS in one line **without naming a font or a colour**? If the only description is aesthetic, the concept never made it into the prompt.

Record the verdict (PASS, or the failed axis + the fix) per direction.

### Step 9 — Assemble the Compiled Prompts block

Collate every direction into the block schema (Output Requirements) and append it to the Studio Job. One card per direction — model-tagged, run-command-ready, Virgil-stamped, flags surfaced.

## Content-Type Adaptations

The recipe shifts by what's being made. Weight the named clauses; keep the rest lean.

| Content type | Primary recipe | What the compile weights | Aspect / `--size` | Key caveat |
|---|---|---|---|---|
| **Poster / print** | Step 3 (fal-poster) | `subject` scene + leverage point + 10/5/1 ladder carry it; anti-slop clauses distributed | `portrait` / `poster-xl` | `title` ≤6 words or expect typos |
| **Logo / identity** | Step 3 + `--rembg`, or Step 6 (edit) | scaffold minimal, concept in `subject`; transparency for placement | `square` | logo fidelity imperfect — flag for human review |
| **Social / feed** | Step 3, or Step 7 (motion) | thumbnail-legible 10 m read; hook in the first clause; square↔vertical transfer | `square` → `hero-2to1`; video `9:16` | build for the thumbnail, not the full-size read |
| **Product / photoreal** | Step 4 (Soul), Step 5 (Nano) first | wardrobe/character + lighting direction+quality + lens/DoF | Soul-native | attach a character reference if consistency matters |
| **Packaging** | Step 3 (`packaging-mockup` scaffold) | label typography legible at thumbnail; material/finish in `subject` | `portrait` | every label word must survive at thumbnail scale |
| **Video / motion** | Step 7 (Kling / Seedance / Cinema) | start-frame first, then physics-bound motion + camera behaviour | match start frame | Seedance interpolates — no new objects mid-shot |

## Output Requirements

This stage appends a single **Compiled Prompts** block to the accumulating Studio Job — one card per direction, in this exact shape. Stage 6 reads nothing else to generate.

```markdown
## Compiled Prompts  (Stage 5 · /fantastic-prompt-compile)

### Direction [N] — [name]
- **Model tag:** [fal-poster | fal-edit | higgsfield-soul | higgsfield-nano | fal-kling | fal-seedance-720p | higgsfield-cinema]  (router-confirmed: yes)
- **Compiled prompt / brief:**
  - Fal → the full `--brief` JSON (below) + the run command
  - Higgsfield → the prose prompt in the model's shape + reference plan
  - Edit → `--input=<path>` + the change-only instruction (+ `--mask` if surgical)
  - Video → start-frame path + motion/camera prompt + wrapper command
- **Run command (for the human to trigger in Stage 6):** `[exact command, real flags only]`
- **Virgil verdict:** PASS  |  or: [failed axis] → [fix applied]
- **Flags:** [title ≤6 words ✓ / logo needs review / needsPhoto ref required / quality tier / size]

<!-- For every fal-poster direction, the exact JSON, ready to write to briefs/<name>.json: -->
```json
{ "style": "...", "subject": "...", "title": "...", "subtitle": "...",
  "body": "...", "footer": "...", "palette": "#hex,#hex,#hex", "logo": "" }
```
```

The block is complete only when: every direction has a router-confirmed model tag, a full compiled prompt (Fal directions include the literal JSON), a run command using **only real flags**, a Virgil PASS (or a logged fix), and its caveat flags surfaced. A direction missing any of these does not advance to Stage 6.

## Quality Gate

Before the Compiled Prompts block hands off to WF-06, verify:

- [ ] **Model tag re-confirmed, not inherited blind** — each direction's tag was re-checked against `creative_router.py` at Step 1, not assumed from Stage 3.
- [ ] **One direction, one prompt** — no two directions merged into a single call to save a run; a blended prompt averages the divergence away.
- [ ] **Fal directions carry the literal `--brief` JSON** — a real scaffold id from `styles.js --list`, `subject` as one fully-realised scene (not a keyword stack), `title` ≤6 words, `palette` set to the Satori hex tokens.
- [ ] **Edit directions describe only the change** — no restated whole-scene prompt riding along with `--input`.
- [ ] **Virgil-tested** — POV, tension, cultural anchor, one-sentence concept all answered per direction; any "no" was fixed and re-tested, not shipped with a failing axis.
- [ ] **Run command uses real flags only** — no invented flag; a second operator could paste it and fire it as written.

**Pass criteria**: all checked. A prompt shaped for the wrong model, or a keyword-stuffed prompt that throws Stage 4's decisions away, does not advance to Stage 6 regardless of how polished the JSON looks.

## Cost & Safety

**This stage PLANS. It writes exact invocations and fires nothing.** Generation is human-triggered and cost-gated at Stage 6. When the human runs a compiled command, the mandatory pre-flights are:

```bash
# Every paid image/edit gen (fal-poster, fal-edit, fal-rembg, higgsfield-soul, higgsfield-nano, higgsfield-cinema):
python3 execution/cost_gate.py check --service <id> --request "<task>"
#   needs-approval → ask Farrice; ONLY after an explicit yes:
python3 execution/cost_gate.py approve --service <id>   # then run the command, then:
python3 execution/cost_gate.py log --service <id> --status success --actual-cost <n>

# Video directions ALSO require the budget guard before the wrapper runs:
python3 execution/fal_budget_guard.py check --mode=<kling|seedance-720p> --duration=<N> [--audio=<off|on|voice_control>]

# Higgsfield MCP image/video tools are additionally gated by:
python3 execution/higgsfield_budget_guard.py   # (seedance-1080p is HARD-BLOCKED; never route to it)
```

The compiler never runs a cost-gate `approve`, never fires `generate.js`, never calls a Higgsfield MCP generate tool. It hands the human a set of ready-to-run commands and stops.

## Related Workflows

**Pipeline siblings (the Fantastic Studio stages):**
- `/fantastic-model-route` (WF-03) — assigns each direction its model tag; re-confirm here via `creative_router.py`
- `/fantastic-art-direct` (WF-04) — writes the Art-Direction Spec this stage consumes
- `/fantastic-generate` (WF-06) — the human-triggered, cost-gated generation this block feeds
- `/fantastic-studio-critique` (WF-07) — runs `/satori-lift-audit` + flip-test on the generated output

**Composed brain (Satori decides):**
- `/satori-design-think` (WF-20) — the Production Brief upstream of Stage 4
- `/satori-color` (WF-17) — the hex tokens that land in the Fal `palette` key
- `/satori-lift-audit` (WF-01) — the leverage point + 10/5/1 ladder the `subject` line encodes
- `/satori-anti-ai-slop` (WF-09) — the imperfection moves compiled into texture clauses

**Adjacent creative tooling:**
- `/art-direct`, `/mood-board`, `/storyboard` (Creative Director) — for Higgsfield/cinematic directions and reference frames
- `execution/creative_router.py` — the transparent model-routing table behind the tags
