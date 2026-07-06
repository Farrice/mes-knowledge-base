---
description: Anchors a design brief in real high-craft lineage — 2-4 named references, their transferable moves, and a fit-in/break-away call — before any prompt is written, so output isn't generic-model-default.
---

# 01 — Reference Grounding (/fantastic-reference-ground)

> Before a single prompt exists, decide whose shoulders this stands on. Satori has already decided *what to say*; this stage decides *what visual tradition says it with authority* — and whether to join that tradition or break from it on purpose.

The current skill only gestures at lineage (its "out of left field" mode and a `pickStyle()` that keyword-locks exactly ONE of the 38 styles). That is the redundancy this stage fixes: it replaces a single reflexive style match with a *researched* Reference Anchor — real movements, real designers, real archives — plus a deliberate call to fit in, break away, or break the category's visual monopoly. Generic output is almost always ungrounded output. Ground it here.

## Pre-Flight Gate

**Use this when**:
- A Satori Production Brief is locked (concept, feeling, color tokens, surface) and you are about to build a generation prompt — anchor the lineage *first*.
- Output came back generic / AI-default and you need to inject a real craft tradition instead of patching the surface.
- The brief targets a niche visual heritage the 38 primitives don't cover — Polish poster school (Lenica, Tomaszewski), Japanese graphic (Yokoo, Sugiura), Experimental Jetset, AIGA poster-annual editorial, a specific masthead lineage — and you need real names, not vibes.
- You want a defensible fit-in vs break-away decision against the category's visual monopoly before spending a cent on generation.

**Do NOT use this when**:
- There is no Satori brief yet — the anchor will float. Run `/satori-design-think` (WF-20) first, then return.
- You're doing an exact template replication (`--template`) — layout is already fixed by the source; lineage is inherited, not chosen.
- You're anchoring an exact wordmark (`--logo`) where redraw is forbidden — the logo IS the reference; skip to generation.
- It's a pure surgical edit of an existing asset (`--input` + `--mask`) whose visual world is already set — route to the generate/edit stage.

**Hard rule**: this stage **produces a Reference Anchor and never fires a paid API.** The only commands it runs are free reads (`node generate.js --list`) and web research (WebSearch / WebFetch). Generation is downstream, human-triggered, and cost-gated.

## Skill Acquisition

```
Load: skills/fantastic-posters/genius.md
  ├─ Reference-grounding principle ...... lineage-before-prompt (this stage)
  ├─ 38 styles = lineage primitives ..... blend 1-3, never keyword-lock ONE
  └─ Fit-in / Break-away / Monopoly-break decision

Composes (Tier 1.5 hot-context — skip re-read if already loaded):
  /satori-design-think  (WF-20) — the Production Brief this stage INGESTS
  /satori-color         (WF-17) — competitive color / GP-15, drives the fit/break call

Drives (real code — read to confirm the surface before you cite a flag):
  skills/fantastic-posters/styles.js   — the 38 lineage primitives + pickStyle() (node generate.js --list)
  skills/fantastic-posters/generate.js — downstream consumers: --refs (mood/style), --style, --palette
  execution/creative_router.py         — instrument pick (a later stage, previewed here)
```

## Execution

Seven steps. Each forces one decision and writes one line into the accumulating **Studio Job**. Do not advance on a "TBD" — an ungrounded anchor contaminates every prompt built on it.

### Step 1 — Ingest the Satori Production Brief

Pull five things from the brief and restate them at the top of the anchor: the **communication problem**, the **concept / hidden truth**, the **target feeling**, the **strategic color tokens** (hex), and the **surface** (poster / logo / social / product / packaging / video). If any is missing, halt and route to `/satori-design-think` — reference grounding without a decided message is decoration.

### Step 2 — Name the closest high-craft lineage (2-4 real references)

Force the decision: *which real movement, designer, or archive is the closest high-taste ancestor of THIS communication problem — not this aesthetic?* Name 2-4. Prefer specificity (a designer + a piece) over a genre label.

- If the lineage is in your knowledge cold, name it directly (Müller-Brockmann grid rationalism; Saul Bass reductive metaphor; A.M. Cassandre depth).
- If it's niche or you're guessing, **research it — do not fabricate names**. Run `WebSearch` for the tradition, then `WebFetch` (or `/tavily-research`) an authoritative source (AIGA archives, Letterform Archive, a monograph). Confirm names, dates, and the piece before you cite it. A hallucinated designer is worse than a genre label.

Write each as: `[Movement / designer / archive] — [the piece or era]`.

### Step 3 — Extract the TRANSFERABLE moves

For each reference, extract **what makes it great and how it transfers** — never "copy this artist." Cover the four levers:

- **Composition** — grid logic, asymmetry, negative-space discipline, focal geometry.
- **Color logic** — palette size, contrast strategy, the one restricted accent.
- **Type treatment** — weight, case, tightness, image-as-type, hand vs. set.
- **Texture** — print artifact, registration offset, grain, ink bleed, paper.

State each as a move, not a name: *"Tomaszewski move: a single hand-torn metaphor carrying the whole message, imperfect edge left visible"* — a move you can execute, not an artist you can only admire.

### Step 4 — Call FIT-IN vs BREAK-AWAY vs break the monopoly (satori GP-15)

Look at the category's **visual monopoly** — what every competitor in this space already looks like (their default color, their default composition). Then decide, in one sentence with the reasoning:

- **FIT-IN** — borrow the tradition's authority because the audience needs the genre signal (a wine bar that must read "wine bar").
- **BREAK-AWAY** — own an adjacent lane the category has abandoned.
- **BREAK THE MONOPOLY** — invert the category's default color/composition to be the one thing that doesn't look like the others (GP-15 competitive color: if everyone is blue, the memorable one isn't).

Tie the call to the Step 1 color tokens — if `/satori-color` already chose a competitive palette, this call must agree with it or the two stages are fighting.

### Step 5 — Map to the 38 primitives (blend, don't keyword-lock)

Run the catalog and pick the **closest 1-3** style IDs as starting DNA — to *blend*, not to keyword-match:

```bash
node generate.js --list
```

The 38 styles ARE curated lineage primitives (`swiss-minimal-typo` = Müller-Brockmann; `saul-bass-minimal` = Bass; `bauhaus-geometric` = Bayer/Moholy-Nagy; `ukiyo-e` = Hokusai; `psychedelic-60s` = Fillmore; `absurd-transit-map` = Vignelli; `art-deco` = Cassandre-era). `pickStyle()` snaps to exactly ONE on a keyword — that is the redundancy this stage overrides. Name 1-3 to combine (e.g. "`swiss-minimal-typo` grid discipline + `indie-gig-riso` print texture"). If NONE of the 38 fit the researched lineage, say so — that's the signal to lead with reference *images* (Step 6) and a custom style clause rather than a `--style=` lock.

### Step 6 — Assemble reference images (optional, for --refs)

If real reference images will sharpen the anchor beyond words, collect their paths for downstream generation. Note the exact consumer behavior so the next stage uses them correctly:

- Feeding images via `--refs=` switches `generate.js` into multi-reference **edit** mode. Order is load-bearing: **image 1 = hero, image 2 = brand book (PDF auto-renders page 1), image 3+ = logos.** For pure mood/style refs, put the strongest style exemplar first.
- For a people/photoreal surface, the reference instead feeds Higgsfield Soul's image input (previewed at Step 7 routing), not `--refs`.

Record paths only; do not upload or generate here.

### Step 7 — Write the Reference Anchor into the Studio Job

Assemble Steps 1-6 into the named block (template in Output Requirements) and hand it forward. Optionally preview the instrument the router will pick, so the next stage isn't surprised:

```bash
python3 execution/creative_router.py route --task "<surface + subject from the brief>" --json
```

That preview is read-only telemetry — it picks the *instrument* (fal-poster · higgsfield-soul · higgsfield-nano · fal-edit), not the moment to fire it.

## Content-Type Adaptations

| Surface | Where the lineage lever leans | Closest 38-primitive DNA | Downstream instrument |
|---|---|---|---|
| **Poster / print** | Full lineage weight — composition + type + print texture all transfer. Physical distance is real; the tradition must survive a wall. | `swiss-minimal-typo`, `saul-bass-minimal`, `art-deco`, `indie-gig-riso`, `bauhaus-geometric` | fal-poster |
| **Logo / identity** | Lineage of *reduction* — mark-making, silhouette, one-color survival. Type treatment > color; skip texture. Break-away often wins (a logo must not look like the category). | `swiss-minimal-typo`, `bauhaus-geometric`, `saul-bass-minimal` | fal-poster + `--rembg` for transparency; Creative Director to codify |
| **Social / feed** | Thumbnail-first lineage — the reference must hold at 64px. Break-the-monopoly color earns the scroll-stop. Transferability across square↔vertical is the gate. | `vaporwave-synth`, `pop-art-comic`, `memphis-80s`, `streetwear-lookbook` | fal-poster (static) · Higgsfield (motion) |
| **Product / photoreal** | Lineage of *photography*, not illustration — lighting school, lens, grade (Magnum reportage, keynote-stage product). References feed Higgsfield Soul's image input, not `--refs` style. | `minimal-tech-keynote`, `documentary-portrait`, `editorial-fashion`, `packaging-mockup` | higgsfield-soul (people/photoreal) · higgsfield-nano (cheap iteration) |
| **Packaging** | Lineage of *shelf presence* — label typographic tradition + material/finish + shelf-block color (GP-15 shelf differentiation is decisive). | `packaging-mockup`, `emerald-nocturne`, `menu-board` | fal-poster; dieline to production |
| **Video / motion** | Anchor the *still frame first* (this stage), then the motion lineage (cinematographer / title-sequence tradition) for the animate stage. The poster IS the video's input frame. | Anchor via any still primitive → `poster-to-video` | fal-kling · fal-seedance-720p · higgsfield-cinema (all budget-gated) |

## Output Requirements

This stage writes exactly one named block — **§1 of the accumulating Studio Job** — which the compile stage consumes verbatim:

```markdown
## STUDIO JOB — §1 · Reference Anchor

**From Satori brief**: problem [...] · concept/hidden-truth [...] · feeling [...] · color tokens [#___, #___] · surface [poster/logo/social/product/packaging/video]

**Lineage (2-4 named, real)**:
1. [Movement / designer / archive] — [piece or era] — verified via [knowledge / WebFetch source]
2. [...]

**Transferable moves**:
- Composition: [move, not a name]
- Color logic: [move]
- Type treatment: [move]
- Texture: [move]

**Fit / Break call**: [FIT-IN | BREAK-AWAY | BREAK-MONOPOLY] — because [category monopoly + GP-15 color reasoning, agreeing with §color tokens]

**Closest 38-primitive DNA (blend, don't keyword-lock)**: [style-id] + [style-id] (+ [style-id])   — or "NONE fit → lead with reference images + custom clause"

**Reference images (for --refs, order = hero, brand, logo+)**: [path1, path2, ...]  — or NONE

**Instrument preview (creative_router)**: [fal-poster | higgsfield-soul | ...]

→ Handoff: consumed by the prompt-compile stage (§2).
```

Complete only when: lineage names are real (researched, not invented), every reference carries a transferable *move* (not just a name), the fit/break call names the category monopoly and agrees with the color tokens, and the primitive DNA is 1-3 IDs to blend (or an honest "none fit").

## Cost & Safety

**This stage PLANS. It fires no paid API.** Its only commands are free: `node generate.js --list` (local catalog read) and `WebSearch` / `WebFetch` (research). No image is generated here.

The **downstream** generation stage that consumes this anchor is cost-gated and human-triggered. When it runs, it must clear the gate first — never auto-fire:

```bash
# pre-flight (mandatory) for the poster/image gen this anchor feeds:
python3 execution/cost_gate.py check --service fal-poster --request "<task>"
# if needs-approval → ask Farrice; ONLY after an explicit yes:
python3 execution/cost_gate.py approve --service fal-poster
# then generate, then:
python3 execution/cost_gate.py log --service fal-poster --status success --actual-cost <n>
```

For a photoreal/people route the service is `higgsfield-soul` (gated by `higgsfield_budget_guard.py`); for the video route, add `python3 execution/fal_budget_guard.py check --mode=<kling|seedance-720p> --duration=<N>`. This stage names those gates; it does not clear them.

## Related Workflows

**Next in the Fantastic Studio pipeline**:
- `/fantastic-brief-compile` (§2) — folds this anchor + the Satori brief into a `generate.js` structured brief (`--brief=studio-job.md`)
- `/fantastic-route` (§3) — `creative_router.py` picks the instrument
- `/fantastic-generate` (§4) — the cost-gated, human-triggered call
- `/fantastic-studio-critique` (§5) — runs `/satori-lift-audit` + `/satori-flip-test` on the *generated* output, closing the "studio critiques its own work" loop

**Composed here**: `/satori-design-think` (WF-20, the brief this ingests) · `/satori-color` (WF-17, the GP-15 fit/break call) · `/satori-anti-ai-slop` (WF-09, the break-away lane) · `/satori-perception-gap` (WF-18, downstream check)

**Creative Director alternatives** (when the lineage work wants a mood-board, not a prompt): `/mood-board` · `/art-direct` · `/storyboard` · `/taste-lineage` · `/references`

**Existing generation workflows** this anchor eventually feeds: `poster-to-video` · `kling-multishot` · `seedance-cinematic` · `deliverable-cover`.

> The through-line: **Satori decides, the router picks the instrument, the studio critiques its own work** — and reference grounding is the studio's taste, made explicit and real before a pixel is spent.
