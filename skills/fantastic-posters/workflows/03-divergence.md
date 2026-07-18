---
description: Generate 3-5 genuinely distinct creative directions from one art-direction spec by varying orthogonal axes — the anti-redundancy core that replaces generate.js --n's colour-and-framing tint.
---

# 03 — Divergence Spread (/fantastic-divergence)

> One spec in, several genuinely different ideas out — distinct in *concept*, not in colour tint. This is the direct fix for the studio's redundancy problem: `--n` nudges colour and framing; divergence changes the idea.

This stage takes the locked art-direction spec (the Satori Production Brief the studio ingested upstream) and fans it into 3-5 directions that a stranger could tell apart with the sound off. It is not variation and it is not iteration. It is the deliberate act of asking "what are the *materially different* ways to solve this one communication problem?" — then proving the answers don't collapse into each other.

**The redundancy it exists to kill.** `generate.js --n=N` runs N separate API calls, and the generator appends to every prompt after the first: `(variant N: subtly shift colour accent and framing)`. That is a tint — same idea, same lineage, same composition, a different paint bucket. `--variants=1..4` is worse for divergence: siblings of *one* prompt in a single call. Both are the right tool for "give me options on a direction I already chose." Neither generates *directions*. This workflow does, by compiling each direction into its **own** invocation — a different `--style`, a different structured `--brief`, or a different model entirely.

**The through-line.** Satori decides the concepts, the router picks the instrument, the studio critiques its own spread before a cent is spent.

## Pre-Flight Gate

**Use this when**:
- You have a locked art-direction spec (Satori Production Brief, or the studio's ingested brief block) and need real options, not tints.
- A first pass came back and every option "looks kind of the same" — that's the `--n` tint failure; run divergence instead.
- Stakes justify a genuine spread: a launch key visual, a brand's first poster, a pitch where you present three defensible territories.
- You want a defensible artifact showing you explored the space, not just defaulted to the first style `pickStyle()` keyword-matched.

**Do NOT use this when**:
- The concept is already chosen and you want *renders of it* — that's exactly what `--n=4` and `--variants=4` are for. Divergence here is overhead.
- There is no spec yet. Divergence without a communication problem is random-style roulette. Route to `/satori-design-think` (or the upstream `/fantastic-brief` ingest) first — a spread built on "TBD" fans out noise.
- You need a surgical edit of one existing asset (route to `--input`/`--mask` edit mode) or a background cutout (`--rembg`).
- The surface can only carry one honest idea (a strict logo lockup, a legally-fixed pack panel). Force 5 directions there and 3 will be tints by construction — reduce N and say so.

**Hard rule this stage enforces**: two directions that differ **only** on colour (axis A4) are **one direction**. A spread that fans out on colour alone is auto-rejected as a tint at the diversity self-check, and the collapsing direction regenerates on fresh axes before this stage hands off.

## Skill Acquisition

```
Load: skills/fantastic-posters/genius.md
  ├─ The redundancy diagnosis ...... why pickStyle() + --n produce near-duplicates
  ├─ The Orthogonality Principle .... directions must differ on independent axes, not one dial
  ├─ The Six Divergence Axes ........ A1 concept · A2 lineage · A3 composition · A4 colour · A5 model · A6 register
  └─ The Collapse Test .............. any two directions reducible to one ⇒ kill and regenerate

Composed Satori workflows (the brain — run each as its axis is assigned; hot-context, skip re-read if loaded):
  /satori-concept            → A1  seven-technique ideation (hidden-truth · one-big-idea · what-if · emotion-over-info · literal · tiny-detail)
  /satori-lift-audit         → A3  LIFT leverage strategy per direction
  /satori-color              → A4  5-layer × 4-role palette, per direction, with hex
  /satori-feeling-calibrate  → A6  register lock (premium-restrained · loud · playful · eerie)

Real code this stage drives (planning only — fires nothing):
  execution/creative_router.py       → A5  route each direction to its instrument (route is FREE)
  skills/fantastic-posters/styles.js → A2  the 38 lineage primitives (the id catalogue below)
  skills/fantastic-posters/generate.js → the compile target (--style / --brief / --variants)
  execution/cost_gate.py             → mandatory pre-flight before ANY direction is generated (downstream)
```

## Execution

Divergence runs in seven steps. The engine is Step 3: assign **orthogonal** axes so no two directions share the same three dials. The discipline is Step 7: prove they didn't collapse.

### Step 1 — Ingest the spec (decision: what is fixed vs free?)

Pull from the upstream art-direction spec and write them at the top of the working block. These are the **invariants** — every direction must still solve them:

- **Communication problem** (the one thing all directions must accomplish).
- **Hidden truth / concept seed** (the insight the design makes visible).
- **Leverage point + recognition ladder** (10 m / 5 m / 1 m — what must read at distance).
- **Feeling target**, **surface**, and any hard brand tokens (logo, one non-negotiable colour, format).

If any invariant is "TBD", **halt** — you have nothing to diverge *from*. Route to `/satori-design-think`. Divergence keeps the problem fixed and varies the *solution*; a floating problem gives you scatter, not a spread.

### Step 2 — Set N (decision: how wide is the real space?)

Default **N = 3**. Go to **4-5** only when the concept space is genuinely wide (a new brand with no visual equity) or the stakes justify presenting territories. On constrained surfaces (logo, regulated pack) drop to **3** or fewer and note why — padding N with tints is the exact failure this stage exists to prevent.

### Step 3 — Assign the six orthogonal axes (the anti-redundancy engine)

For each direction, pick a **distinct** value on the three *idea* axes (A1, A2, A3) and diversify the three *expression* axes (A4, A5, A6). The binding rule:

> **Any two directions must differ on at least 2-3 axes — and at least one of those must be an idea axis (A1/A2/A3).** Differ only on A4 (colour) and they are the same direction wearing two coats — the `--n` tint, rejected.

| Axis | What varies | How to assign | Reject-if |
|---|---|---|---|
| **A1 Concept angle** | The creative technique / which hidden truth | Run `/satori-concept`; give each direction a *different* technique (hidden-truth vs what-if vs emotion-over-info vs literal vs tiny-detail vs one-big-idea) | Two directions argue the same insight |
| **A2 Art lineage** | The reference movement | Map to a *different cluster* of the 38 styles (table below) — not two neighbours in one cluster | Both directions pull from the same cluster |
| **A3 Composition / leverage** | The LIFT strategy | Compose `/satori-lift-audit`: type-dominant · image-dominant · negative-space · asymmetric-collage · symmetric — one each | Two directions share a layout skeleton |
| **A4 Colour strategy** | The 5-layer colour job | Compose `/satori-color`: fit-in (category-native) vs stand-out (disruptive) vs monochrome vs high-contrast | *Colour is the ONLY difference* → tint |
| **A5 Model / medium** | The generator | `creative_router.py route` per direction (Step 5) — GPT Image 2 typographic vs Higgsfield Soul photoreal/people vs Nano quick iteration | All directions on one model *and* one lineage |
| **A6 Register / feeling** | Emotional pitch | Compose `/satori-feeling-calibrate`: premium-restrained vs loud vs playful vs eerie | Two directions carry the same feeling |

**A2 lineage clusters (the 38 real style ids — pick across clusters, never two from one):**

- **Swiss / International** — `swiss-minimal-typo` · `minimal-tech-keynote` · `saul-bass-minimal`
- **Modernist geometric** — `bauhaus-geometric` · `memphis-80s` · `art-deco`
- **Japanese** — `ukiyo-e` · `sumi-e-zen`
- **Editorial / fashion** — `editorial-fashion` · `streetwear-lookbook` · `album-cover-portrait`
- **Riso / indie / folk** — `indie-gig-riso` · `pop-art-comic` · `loteria-folk`
- **Brutalist / broadcast** — `brutalist-broadcast` · `tech-conf-darkmode`
- **Cinematic / noir** — `cinematic-neonoir` · `neon-noir-cyberpunk` · `emerald-nocturne`
- **Photoreal / documentary** — `documentary-portrait` · `sports-action-hero` · `luxury-real-estate` · `luxury-estate-cover`
- **Surreal / retro-trip** — `surreal-dreamscape` · `psychedelic-60s` · `vaporwave-synth`
- **Calm / mindful** — `pastel-mindful` · `symmetric-storybook`
- **Vintage / travel** — `vintage-travel`
- **Adventure / genre** — `post-apoc-sword` · `lone-traveler-cargo`
- **Typographic-first commercial** — `chalkboard-sign` · `store-window` · `menu-board` · `packaging-mockup` · `ui-mockup`
- **Info / systems** — `absurd-transit-map` · `corporate-report`

### Step 4 — Name each direction and write its one-sentence concept

A direction earns a **name** (a handle the room can say aloud) and a **one-sentence concept** that survives the phone test — describable without naming a font or a hex. Then note the axis values you assigned. If the sentence needs a colour to distinguish it from another direction, it isn't a direction — return to Step 3.

### Step 5 — Route each direction to its instrument (A5, and it's free)

Run the router per direction — this both diversifies the spread **and** exploits the full model surface:

```bash
python3 execution/creative_router.py route --task "<direction's concept + surface + lineage>" --json
```

The router is the arbiter (first match wins). The instruments this stage draws on:

- **`fal-poster`** — GPT Image 2 typographic / stylized posters (the studio spine; compiles to a `--style` or `--brief`).
- **`higgsfield-soul`** — best photoreal + **people/character** directions (est $0.10, ceiling $0.50).
- **`higgsfield-nano`** — Nano Banana Pro, fastest/cheapest for a rough-cut direction you're not sure survives.
- **`fal-edit` / `fal-rembg`** — only if a direction is an edit or needs transparency.

Do not hand-pick the model past the router unless you have a reason the router can't see; if you override, write the reason.

### Step 6 — Compile each direction to its OWN invocation (never one --n call)

This is the mechanical contrast with the redundancy. Each direction is a separate command:

```bash
# Direction built on a lineage primitive — its own style, from repo root, FAL_KEY in env:
node skills/fantastic-posters/generate.js "<concept, subject, headline>" \
  --style=swiss-minimal-typo --quality=medium --size=portrait

# A richer direction — hand Satori's spec to the generator as a structured brief
# (keys: style, subject, title, subtitle, body, footer, palette, logo):
node skills/fantastic-posters/generate.js --brief=.tmp/divergence/dir-02-ukiyoe.md --quality=medium

# A photoreal/people direction — router → higgsfield-soul (MCP), NOT generate.js:
#   mcp__claude_ai_Higgsfield__generate_image  (gated by higgsfield_budget_guard.py)
```

Once a direction is chosen and you want *renders of it*, **then** `--variants=4` (four siblings, one cheap call) or `--n=4` (four calls with the colour/framing nudge) is correct. Divergence produces the directions; those flags multiply the winner.

### Step 7 — Diversity self-check (the studio critiques its own work)

Before the spread leaves this stage, run the **collapse test** on every pair:

1. For each pair of directions, count how many of the six axes actually differ.
2. **Require ≥ 2 distinct axes per pair, ≥ 1 of them an idea axis (A1/A2/A3).**
3. Any pair that differs only on A4 (colour), or that a cold viewer would describe with the same sentence, **collapses** — kill the weaker direction and regenerate it on fresh axes (return to Step 3 for that slot only).
4. Also fail a spread where all directions ride one model *and* one lineage cluster — that's a palette swap masquerading as a spread.

Write the **verdict**: `PASS` (hand off) · `TINT-FAIL: [direction] collapses into [direction] on [axes] — regenerating`. Do not hand off a TINT-FAIL.

## Content-Type Adaptations

Divergence runs on every surface; which axes carry the spread shifts. Lean on the named axes, ease off the rest.

| Surface | Axes that carry divergence | Model spine (A5) | Note |
|---|---|---|---|
| **Poster / print** | A2 lineage + A3 composition + A1 concept — the full six-axis fan | `fal-poster` (`--style`/`--brief`) | Each direction's 10 m read must be *different*; physical distance is real. N up to 5. |
| **Logo / identity** | A1 concept + A3 mark-construction + A6 register; **skip A2** (a logo shouldn't chase art movements) | `fal-poster` + `--rembg` for transparency; `--logo=` to anchor an exact wordmark | Diverge on *idea of the mark*, not on style veneer. N = 3, and say if fewer honest. |
| **Social / feed** | A6 register + A3 thumbnail composition + A1 hook angle | `higgsfield-nano` for rough directions, `fal-poster` for finals | Every direction must survive 64×64 px; a direction that dies at thumbnail is dead. |
| **Product / photoreal** | A6 register + A3 framing/scene + A1 angle; **de-weight A2** typographic lineage | `higgsfield-soul` (people/product) — router will pick it | Diverge on scene and pitch, not on poster style. Transparency via `remove_background`. |
| **Packaging** | A4 shelf-differentiation colour + A2 lineage + A3 block strategy | `fal-poster` `--style=packaging-mockup` | Here A4 *is* a legitimate idea axis (shelf-standout is strategy) — but still pair it with A2/A3 so directions aren't tints. |
| **Video / motion** | A1 concept + A3 shot design; expression axes carry less | Router → `higgsfield-cinema` / `fal-kling` / `veo-3`; feed each into `/storyboard` | Cost per direction is 30-200× a poster — cap N at 3, and diverge at the *concept/shot* level, not the grade. |

## Output Requirements

This stage appends one block — the **Divergence Spread** — to the accumulating **Studio Job**. The next stage (critique / selection / generation) consumes it verbatim.

```markdown
## Divergence Spread — [job name / surface]   (Stage 03 · /fantastic-divergence)

**Invariants (from the spec, fixed across all directions):**
- Communication problem: [...]
- Hidden-truth seed: [...]  · Leverage: [...]  · Feeling: [...]  · Surface: [...]
- N chosen: [3-5]  (reason if <3 or >4)

### Divergence Table
| # | Direction (name) | Concept (1 sentence) | Axes varied | Art lineage (style id / cluster) | Composition (LIFT) | Model (router) | Why distinct |
|---|---|---|---|---|---|---|---|
| 1 | [name] | [one sentence] | A1,A2,A3,A6 | swiss-minimal-typo / Swiss | type-dominant | fal-poster | [what only this one does] |
| 2 | [name] | [one sentence] | A1,A2,A3,A5,A6 | ukiyo-e / Japanese | negative-space | fal-poster (--brief) | [...] |
| 3 | [name] | [one sentence] | A1,A2,A3,A5 | documentary-portrait / Photoreal | image-dominant | higgsfield-soul | [...] |

### Compiled invocations (each its OWN command — human-triggered downstream)
1. `node skills/fantastic-posters/generate.js "..." --style=... --quality=medium`
2. `node skills/fantastic-posters/generate.js --brief=.tmp/divergence/dir-02.md --quality=medium`
3. router → `higgsfield-soul` via `mcp__claude_ai_Higgsfield__generate_image`

### Diversity self-check
- Pairwise distinct-axis counts: 1↔2 = [n] · 1↔3 = [n] · 2↔3 = [n]  (all must be ≥2, ≥1 idea axis)
- All-on-one-model-and-lineage? [no / FAIL]
- **Verdict:** PASS  |  TINT-FAIL: [dir] collapses into [dir] on [axes] — regenerated
```

The block is complete only when: N directions each have a distinct name, a one-sentence concept, ≥2 varied axes vs every sibling, a routed model, and its own compiled command — and the verdict reads PASS. A TINT-FAIL is not an output; it's a return to Step 3.

## Quality Gate

Before the Divergence Spread hands off to WF-04, verify:

- [ ] **N justified, not padded** — 3 by default, 4-5 only when the concept space is genuinely wide; a constrained surface (logo, regulated pack) states why N is lower.
- [ ] **Every pair clears the collapse test** — ≥2 distinct axes per pair, ≥1 of them an idea axis (A1/A2/A3). A pair differing only on A4 (color) is a tint, not a direction.
- [ ] **No single-model, single-lineage spread** — the six axes actually span more than one `styles.js` cluster and, where warranted, more than one instrument.
- [ ] **Each direction has its own compiled invocation** — never one `--n=N` call standing in for divergence; each direction is a separate command with a separate prompt.
- [ ] **Verdict is explicit** — PASS or TINT-FAIL is written; a TINT-FAIL direction was regenerated on fresh axes before handoff, not shipped anyway.

**Pass criteria**: all checked. A spread that "produced N images" but collapses on the pairwise test is the exact redundancy failure this stage exists to kill.

## Cost & Safety

This stage **plans and compiles — it fires nothing.** It writes N directions and their ready-to-run commands into the Studio Job; a human triggers generation later.

- `creative_router.py route` is **free** (planning only — it prints a route and a pre-flight command, spends nothing).
- Before **any** direction is generated downstream, the mandatory pre-flight is:

  ```bash
  python3 execution/cost_gate.py check --service <fal-poster|higgsfield-soul|higgsfield-nano|...> --request "<direction concept>"
  ```

  If it returns `needs-approval`, surface to Farrice; only after an explicit yes run `cost_gate.py approve --service <id>`, then generate, then `cost_gate.py log --service <id> --status success --actual-cost <n>`. Denied = surface, do not retry.
- Cost awareness while setting N: `fal-poster` runs ~$0.011 (low) / ~$0.04 (medium) / ~$0.17 (high) **per direction per image**; `higgsfield-soul` est $0.10 (ceiling $0.50). A 5-direction medium spread rendered at `--variants=4` each is 20 billed images — plan N with that in view.
- Higgsfield image/video directions run through the MCP tools (`mcp__claude_ai_Higgsfield__generate_image` / `generate_video`), gated by `higgsfield_budget_guard.py`. Never auto-fire.

Satori decides, the router picks the instrument, the human pulls the trigger.

## Related Workflows

**Studio pipeline siblings** (`/fantastic-*`):
- **Upstream** — `/fantastic-brief` / `/satori-design-think` produce the spec this stage ingests. No spec, no divergence.
- **Downstream** — the critique/selection stage runs the collapse test's cousin on the *generated* frames, then the human-triggered generation stage renders the chosen direction (`--variants` / `--n` for options *within* it).

**Composed Satori brain** (`/satori-*`):
- `/satori-concept` (A1) · `/satori-lift-audit` (A3) · `/satori-color` (A4) · `/satori-feeling-calibrate` (A6) · `/satori-anti-ai-slop` (apply to each surviving direction before render).

**Adjacent creative** (`/creative-*`, `/art-*`):
- `/creative-diversity` — the general-purpose divergence engine this stage specializes for the poster studio.
- `/art-direct` · `/mood-board` · `/storyboard` — Creative Director hand-off for photoreal/people and motion directions the router sends to Higgsfield.
