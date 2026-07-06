---
description: Translate a Satori Production Brief into a rich Art-Direction Spec — concept, composition, color-to-hex, type treatment, memory hook, and anti-slop moves — the block stages 3-5 diverge, route, and compile from.
---

# 02 — Art Direction (/fantastic-art-direct)

> Where the SATORI BRAIN enters the studio. This stage kills "generic template + your text" by refusing to hand a keyword-matched style straight to the generator. It produces an ART-DIRECTION SPEC grounded in a hidden truth, a composition, a color system, and a feeling — the thing prompts compile FROM. Satori decides, the router picks the instrument, the studio critiques its own work.

## Pre-Flight Gate

**Use this when**:
- You have a design task and a concept must be locked before any pixel is priced. This is the second stage of the Fantastic Studio (after WF-01 intake, before WF-03 divergence).
- A prior generation came back as AI-perfect template slop and you need to rebuild from the communication problem up, not repaint the surface.
- A `/satori-design-think` Production Brief exists and needs translating into concrete VISUAL direction (subject, composition, hex, type treatment, lighting) a generator can execute.

**Do NOT use this when**:
- You only need one isolated decision — run the specific Satori workflow directly (`/satori-color` for palette, `/satori-lift-audit` for hierarchy). The full spec is overhead if the concept is already locked.
- You're auditing a *finished* render — that's `/satori-flip-test` / `/satori-lift-audit` on the output, not this pre-generation spec.
- The intent itself is unwritten. A spec built on a vague brief inherits the vagueness. Fix the brief first (`/satori-comms-brief`, or a one-sentence reduction per genius.md GP-08).
- It's pure DESIGN.md token codification or a UI build — route to `/design-md-extract` / `/product-build`.

**Hard rule**: this stage PLANS. It writes a spec and names the downstream generation command. It never fires a paid or cost-gated API. Generation is human-triggered in WF-03+ behind the repo cost gate.

## Skill Acquisition

```
Load: skills/fantastic-posters/genius.md          ← the studio brain (written in parallel)
  ├─ The Satori-first doctrine (concept before style-pick)
  ├─ Type-as-image primitives (the 5 typography-first presets)
  ├─ GP-11 mirror — anti-AI-slop moves at art-direction time
  └─ The Virgil Test (self-critique gate)

Compose (load each as its section runs — Tier 1.5 hot-context; skip re-read if already hot):
  skills/satori-graphics/workflows/20-design-think.md  → /satori-design-think  (INGEST the Production Brief)
  skills/satori-graphics/workflows/16-concept.md       → /satori-concept       (hidden truth, if no brief)
  skills/satori-graphics/workflows/17-strategic-color.md → /satori-color        (palette → hex, if no brief)
  skills/satori-graphics/workflows/01-lift-audit.md    → /satori-lift-audit     (hierarchy / leverage point)
  skills/satori-graphics/workflows/09-anti-ai-slop.md  → /satori-anti-ai-slop   (GP-11 imperfection moves)
  skills/satori-graphics/workflows/18-perception-gap.md → /satori-perception-gap (intended vs perceived)
  skills/creative-direction/genius.md                  → the Virgil Abloh Method (§ The Virgil Test)

Drives (real code — READ to confirm the surface, do NOT fire here):
  skills/fantastic-posters/styles.js       — 38 art-direction primitives (the 5 typo-first presets live here)
  skills/fantastic-posters/generate.js     — the generator this spec eventually compiles into
  execution/creative_router.py             — instrument selection (route --task)
  execution/cost_gate.py                   — pre-flight gate for any downstream paid gen
```

## Execution

Seven moves. Each forces a decision and writes one fragment of the accumulating Art-Direction Spec. Do not advance on a "TBD" — a blank fragment contaminates the compile in stages 3-5.

### 1 — INGEST or RUN the Satori brief (the concept floor)

**Decision forced**: Is there a hidden truth, or am I about to keyword-match a template?

- **If a `/satori-design-think` Production Brief exists**: ingest it and lift these eight fields verbatim — communication problem · hidden truth/concept · LIFT hierarchy + leverage point · strategic color tokens (role + hex) · feeling spec · memory hook · anti-slop moves · viewing-context 10/5/1 ladder. Do not re-derive what the brief already locked; this stage TRANSLATES, it doesn't re-decide.
- **If no brief exists**: run the three load-bearing decisions inline before proceeding —
  - `/satori-concept` → the hidden truth (one sentence, survives being described over the phone).
  - `/satori-color` → the 4-role palette with real hex.
  - `/satori-lift-audit` → the leverage point + eye journey.

**Gate**: you cannot leave move 1 without a one-sentence hidden truth and four hex tokens. No concept = no spec.

### 2 — SUBJECT / SCENE

**Decision forced**: What is literally in frame, and what is deliberately absent?

Name the subject or scene the concept demands — a product, a figure, a typographic field, an object-as-metaphor. State what is NOT in frame (subtraction buys hierarchy; genius.md, and satori GP-01 rent test). If the subject is a person or needs photoreal fidelity, flag it now — it changes the instrument in move 8 (Higgsfield Soul, not Fal).

### 3 — COMPOSITION + LEVERAGE POINT

**Decision forced**: What does the eye hit FIRST, and what got quieted so it dominates?

- Name the **leverage point** — the single element carrying the concept, recognizable at the 10 m rung of the ladder.
- List what you MUTE, DEMOTE, or EVICT so the leverage point wins (subtraction before amplification).
- Trace the eye journey 1st → 2nd → 3rd, ending at the desired action/feeling beat.
- Specify negative space as an active element, not leftover margin.

### 4 — COLOR ROLES → HEX

**Decision forced**: What job does each color do, and where does the accent land?

Carry the Satori tokens into a role table. Every color earns a role or is cut. The accent points AT the leverage point and appears in ONE location only.

| Role | Hex | Job |
|---|---|---|
| Dominant | #______ | the field the eye rests in (~60%) |
| Secondary | #______ | structure / support (~30%) |
| Accent | #______ | ONE location, points at the leverage point (~10%) |
| Neutral/base | #______ | ground, type surface, breathing room |

These exact hex values become the generator payload: `--palette="#hex,#hex,#hex,#hex"` in WF-03+, or the `palette:` key of a `--brief=spec.md` structured brief.

### 5 — TYPE TREATMENT (type-as-image where the lettering IS the picture)

**Decision forced**: Is type a label on the image, or is type the image itself?

Decide weight, contrast, case, and rhythm against the 10/5/1 ladder (recognition distance sizes type before taste does). Then decide the treatment mode:

- **Type-as-image** — when the lettering carries the whole concept, cite one of the **5 typography-first presets** in `styles.js` (these are built so the type IS the composition):
  - `chalkboard-sign` — hand-lettered chalk field, cafe/artisanal
  - `store-window` — painted storefront glass, retail/announcement
  - `menu-board` — structured menu typography, list/price hierarchy
  - `packaging-mockup` — type wrapped on a product surface
  - `ui-mockup` — type inside an app/screen frame
- **Type-as-caption** — when an image leads and type labels it — name the placement, hierarchy, and which of the 33 non-experimental primitives frames it.

### 6 — LIGHTING / LENS / TEXTURE + THE MEMORY HOOK (rendered visually)

**Decision forced**: What does the light/lens/surface do, and what single thing must the viewer RESOLVE?

- Lighting (key/fill/mood), lens (focal length, DOF, angle), texture/finish (matte/gloss, grain/clean, material implication). Each line ties back to the feeling spec.
- The **memory hook** from Satori (metaphor substitution · absence-as-presence · conceptual swap · controlled imbalance) rendered as a concrete VISUAL instruction — not "make it memorable" but "the negative space between the two forms reads as a third object." If you cannot render it concretely, leave it BLANK and flag it (a faked hook is worse than none).

### 7 — ANTI-AI-SLOP MOVES (satori GP-11, mirrored at art-direction time)

**Decision forced**: Which 3+ human-imperfection moves lift this out of the AI-perfect template lane?

Name a minimum of **three** deliberate imperfections, each paying rent (concept / hierarchy / psychology) and honoring the locked concept + palette. Distribute — one at/near the leverage point, one in a secondary zone, one at texture level. Common moves: asymmetric crop · off-rotation glyph (2-7°) · element creep past a margin · tapered gradient · single color-punctuation hit · hand-drawn line · intentional imperfect alignment · negative-space asymmetry. Soften to 2 only if the surface demands clinical sterility (medical/financial) — note why.

### The Virgil Test (self-critique gate — from creative-direction / creative-director)

Before the spec ships, run it through the creative director's gate (`skills/creative-direction/genius.md` § The Virgil Abloh Method — 3% Rule, Readymade, Selection-as-creative-act). Answer all six honestly:

1. **Clear POV?** — could a stranger name the point of view in one line?
2. **Tension?** — is there a friction the design resolves, or is it merely pretty?
3. **Named cultural anchor?** — what specific reference/lineage does it stand on (the "3% change of an existing thing")?
4. **One-sentence concept?** — restate the hidden truth without naming a color or font.
5. **Would removing an element make it stronger?** — if yes, remove it now, before compile.
6. **Interesting without the logo?** — strip the wordmark; does anything remain?

Any "no" sends the offending move back for a rewrite. A spec that fails the Virgil Test but "looks comprehensive" is a system failure regardless of length.

## Content-Type Adaptations

| Content type | Where the spec leans | Instrument tilt (move 8, downstream) |
|---|---|---|
| **Poster / print** | Move 3 (single dominant leverage point survives a wall) + move 7 (anti-slop). 10 m read must hold. | `generate.js` (Fal) — `--size=poster-xl`, quality per print need |
| **Logo / identity** | Move 5 (type-as-image) + move 6 (memory hook) are everything; palette must survive one-color. | Creative Director `/art-direct`; `--logo=<path>` to anchor an exact wordmark, `--rembg` for transparency |
| **Social / feed** | Move 3 thumbnail hierarchy + move 6 scroll-stopping hook. Transfers square↔vertical. | `generate.js --size=square|portrait`; `--variants=1..4` for sibling takes |
| **Product / photoreal** | Move 2 (subject fidelity) + move 6 (lighting/lens). Flag person/photoreal here. | Router → `higgsfield-soul` (people/photoreal), NOT Fal template |
| **Packaging** | Move 4 (color = shelf differentiation) + move 5 (`packaging-mockup` type-on-surface) + move 6 (material). | `generate.js --style=packaging-mockup`; `--refs=` for brand book |
| **Video / motion** | Lock the KEY FRAME spec here (moves 2-6); motion beats belong to the video stage. | Router → `higgsfield-cinema` / `fal-kling` / `fal-seedance-720p` (all cost-gated + `fal_budget_guard.py`) |

## Output Requirements

This stage writes ONE named block — the **Art-Direction Spec** — into the accumulating Studio Job. Stages 3-5 diverge, route, and compile from it; nothing downstream re-derives concept.

```markdown
## ART-DIRECTION SPEC — [design name / surface]

- One-sentence concept + hidden truth: [survives the phone test, no color/font named]
- Composition / leverage: [leverage point · what's quieted/evicted · eye journey 1-2-3 · negative space]
- Color tokens:
  | Role | Hex | Job |
  |---|---|---|
  | Dominant | #______ | ~60% field |
  | Secondary | #______ | ~30% structure |
  | Accent | #______ | ~10%, ONE location, points at leverage |
  | Neutral/base | #______ | ground / type surface |
- Type treatment: [as-image (cite preset: chalkboard-sign|store-window|menu-board|packaging-mockup|ui-mockup) OR as-caption + primitive] · sized against 10/5/1
- Lighting / lens / texture: [key/mood · focal/DOF/angle · finish/material]
- Memory hook (visual): [concrete render instruction]  (or BLANK + flag)
- Anti-slop moves: 1) [move — rent — location]  2) [...]  3) [...]
- Cultural anchor: [named reference / lineage — the 3%]
- Virgil Test: [PASS, or the box that failed + the fix applied]
```

The spec is complete only when: the hidden truth is one sentence, all four hex tokens are real, the type mode is decided (as-image vs as-caption), the memory hook is concrete or honestly blanked, ≥3 anti-slop moves each pay rent, the cultural anchor is named, and the Virgil Test passes. This block — not a prose paragraph — is the WF-03 input.

## Cost & Safety

This stage PLANS. No generation fires here. When stages 3-5 compile this spec into a generation command, the operator runs the mandatory pre-flight — this stage does NOT auto-fire it:

```bash
# instrument selection (free, read-only)
python3 /Users/farricecain/Google Antigravity/execution/creative_router.py route --task "<one-sentence concept + surface>" --json

# mandatory pre-flight before ANY paid gen (NEVER auto-fire; ask Farrice on needs-approval)
python3 /Users/farricecain/Google Antigravity/execution/cost_gate.py check --service <fal-poster|higgsfield-soul|...> --request "<task>"

# video also needs the budget guard
python3 /Users/farricecain/Google Antigravity/execution/fal_budget_guard.py check --mode=<kling|seedance-720p> --duration=<N>
```

seedance-1080p is HARD-BLOCKED. On `needs-approval`: surface to Farrice, and only after explicit yes run `cost_gate.py approve --service <id>`, then generate, then `cost_gate.py log --service <id> --status success --actual-cost <n>`. Satori is the brain; a human hand pulls the trigger.

## Related Workflows

**Studio stages** (this is WF-02):
- WF-01 — intake / brief lock (upstream)
- WF-03 — divergence (compiles this spec into `--n` / `--variants` / multi-style takes)
- WF-04 — routing (`creative_router.py` → the instrument)
- WF-05 — critique / compile (self-review, then the cost-gated generate)

**Composed Satori** (`skills/satori-graphics/workflows/`): `/satori-design-think` (WF-20) · `/satori-concept` (WF-16) · `/satori-color` (WF-17) · `/satori-lift-audit` (WF-01) · `/satori-anti-ai-slop` (WF-09) · `/satori-perception-gap` (WF-18) · `/satori-feeling-calibrate` (WF-19) · `/satori-memory-encoding` (WF-08).

**Composed Creative Direction**: `/art-direct` · `/mood-board` · `/storyboard` (`skills/creative-direction/`, `agents/creative-director/`) — the Virgil Test and photoreal/people routing live here.
