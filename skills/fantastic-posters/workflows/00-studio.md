---
description: The flagship front-door orchestrator — turns any visual brief into a reference-grounded, Satori-art-directed, self-critiqued generation plan across the right models, then executes cost-gated generation and a refine loop on human approval.
---

# 00 — Fantastic Studio (/fantastic-studio)

> The command the whole skill orbits. One brief in → a routed, orthogonally-diverse, art-directed generation plan out, with the paid trigger left in a human's hand. **Satori decides, the router picks the instrument, the studio critiques its own work.**

This is the end-to-end. It does not force a single style keyword-match (that's `pickStyle()`, the redundancy problem this build exists to fix), and it does not fire a model on its own (that's a cost-gated human decision). It **composes** the eight `/fantastic-*` stage workflows — `/fantastic-reference-ground` (WF-01), `/fantastic-art-direct` (WF-02), `/fantastic-divergence` (WF-03), `/fantastic-model-route` (WF-04), `/fantastic-prompt-compile` (WF-05), `/fantastic-generate-run` (WF-06), `/fantastic-critique-refine` (WF-07), `/fantastic-format-pack` (WF-08) — and assembles their outputs into one **Studio Job** document.

The whole design is anti-two-failures:
- **Anti-generic** — a Satori Production Brief (WF-02) replaces model-default aesthetics with a hidden truth, a LIFT hierarchy, strategic color tokens, and named anti-slop moves. The brain decides before a pixel exists.
- **Anti-redundant** — a Divergence Spread (WF-03) generates N *orthogonally distinct* directions (different concept × art-movement × composition × model), not `generate.js --n`, which fires N separate calls that each apply a colour-and-framing nudge to **the same prompt** (siblings, not strangers). The studio produces strangers.

## Pre-Flight Gate

**Use this when**:
- You have a fresh visual brief (poster, logo, social asset, photoreal product/lifestyle shot, packaging, video) and want to go from one sentence to a routed, generation-ready plan in one pass.
- You have a Satori Production Brief already (from `/satori-design-think`) and want to carry it into real generation across the right models without losing the thinking.
- A first batch came back generic or same-y and you want to rebuild from concept and diverge *orthogonally* instead of nudging tints.
- You want one defensible artifact — the Studio Job — that a teammate or Farrice reviews **before** a cent is spent on Fal or Higgsfield.

**Do NOT use this when**:
- You only need ONE stage. Run it directly (`/fantastic-model-route` to just pick a tool, `/fantastic-format-pack` to just resize a locked concept). The full pipeline is overhead when the concept is already locked.
- The brief itself is unwritten or contradictory — the pipeline stalls at Stage 0. Reduce it to one sentence first, or run `/satori-comms-brief` alone.
- It's pure copy/headline work → route to `gemini-text` and the writing roster, not here.
- It's DESIGN.md token codification or a UI build → `/design-md-extract` / `/product-build`. Satori's `/satori-design-md-grid` carries color tokens across if you need both.

**Hard rule this workflow enforces**: the pipeline **produces the Studio Job and stages the exact generation commands — it never auto-fires a paid or cost-gated API.** Fal (fantastic-posters, video wrappers) and Higgsfield are hard-gated in this repo by the PreToolUse cost-gate hook. Stages 0–5 and 8 are pure planning. Only Stage 6 (and the re-render half of Stage 7) touch paid generation, and only after `cost_gate.py` approves and a human says yes. See Cost & Safety.

## Skill Acquisition

```
Load: skills/fantastic-posters/genius.md
  ├─ The Divergence Doctrine ...... Stage 3 (orthogonal, not tinted)
  ├─ The Style-as-Primitive Rule .. Stage 2/5 (38 styles are art-direction primitives, not a menu)
  ├─ Router-Owns-the-Instrument ... Stage 4 (Satori picks the concept, the router picks the tool)
  ├─ The Anti-Slop Bank ........... Stage 2/7 (human imperfection over template polish)
  └─ Cost-Gate Discipline ......... Stage 6/7 (plan free, fire gated)

Composed /fantastic-* stages (load each as its stage runs — hot-context; if already loaded, skip re-read):
  workflows/01-reference-ground.md  → /fantastic-reference-ground  (Stage 1)
  workflows/02-art-direct.md        → /fantastic-art-direct        (Stage 2)
  workflows/03-divergence.md        → /fantastic-divergence        (Stage 3)
  workflows/04-model-route.md       → /fantastic-model-route       (Stage 4)
  workflows/05-prompt-compile.md    → /fantastic-prompt-compile    (Stage 5)
  workflows/06-generate-run.md      → /fantastic-generate-run      (Stage 6)
  workflows/07-critique-refine.md   → /fantastic-critique-refine   (Stage 7)
  workflows/08-format-pack.md       → /fantastic-format-pack       (Stage 8)

Composed Satori brain (Stage 2 ingests or runs these):
  /satori-design-think — full Production Brief (the whole art-direction layer in one call)
  /satori-concept · /satori-color · /satori-lift-audit · /satori-anti-ai-slop · /satori-perception-gap

Real code this pipeline drives (read to confirm flags — never invent):
  skills/fantastic-posters/generate.js   — the Fal GPT Image 2 generator (run from repo root, FAL_KEY in env)
  skills/fantastic-posters/styles.js     — 38 art-direction primitives ({label, build, needsPhoto?, experimental?})
  execution/creative_router.py           — route --task "<desc>" [--json]  (11 services, first match wins)
  execution/cost_gate.py                 — check / approve / log  (mandatory pre-flight for paid gen)
  execution/fal_budget_guard.py          — check --mode=<kling|seedance-720p> --duration=<N>  (video only)
  execution/fal_video_kling.py · fal_video_seedance.py — video render wrappers (FAL_KEY, upload, MP4 download)
```

## Execution

The pipeline runs nine stages (Frame + WF-01 through WF-08). Each stage **composes** a workflow, **forces one decision**, and **appends one named block** to the accumulating Studio Job. Do not advance until the current block is written — a stage that outputs "TBD" contaminates every stage downstream (a fuzzy concept produces same-y directions; a same-y spread wastes the router and the wallet).

### Stage 0 — FRAME the run (setup, ~2 min)

Lock three things before Stage 1:

1. **The surface.** Poster/print · logo/identity · social/feed · product/photoreal · packaging · video/motion. The surface drives the Content-Type Adaptations (below), which stage *leads*, and the final format pack. If the job spans surfaces (a whole brand system), run the pipeline once per surface and keep the **concept** (Stage 2) shared.
2. **The one-sentence brief.** Format: *"A [thing] that [verb] [audience] [outcome/feeling]."* If you can't write it, you're not ready to generate — gather intent first.
3. **Existing Satori brief?** If the user already ran `/satori-design-think`, **ingest that brief** at Stage 2 rather than re-running it (don't pay the thinking tax twice). If not, Stage 2 runs it fresh.

Write all three to the Studio Job header. Every later decision is checked against the one-sentence brief; a decision that contradicts it is wrong, not the sentence.

### Stage 1 — REFERENCE-GROUND (composes `/fantastic-reference-ground`, WF-01)

**Decision forced**: What real high-taste lineage does this sit in — so the output anchors to a *tradition*, not a model default?

Run WF-01 to name 2–4 concrete reference points: a design movement, a named studio/art-director, a specific artifact ("the 1968 Mexico Olympics identity," not "vintage"). Models regress to the mean of their training data; a named lineage pulls the output off that mean and toward taste. Where a physical reference asset exists (a hero photo, a brand book PDF, a logo), note the file path now — it becomes a `--refs=` / `--logo=` input at Stage 5.

**Writes to Studio Job**: `## 1 · Reference Ground` — 2–4 named lineage anchors (movement · studio/AD · specific artifact) + any on-disk reference asset paths.
**Gate**: Every anchor is a *specific* thing you could show someone, not an adjective. "Swiss" fails; "Josef Müller-Brockmann grid posters" passes.

### Stage 2 — ART-DIRECT (composes `/fantastic-art-direct`, WF-02 → the SATORI brain)

**Decision forced**: What is the hidden truth, the hierarchy, the color, the feeling, the memory hook, and the anti-slop discipline — locked before any prompt exists? **This is THE anti-generic move.**

Two paths:
- **Ingest** — the user brought a `/satori-design-think` Production Brief. Load it, verify it against the Stage 0 surface and Stage 1 lineage, carry its sections forward verbatim.
- **Run** — no brief exists. Run `/satori-design-think` now (or its parts: `/satori-concept` for the hidden truth, `/satori-lift-audit` for hierarchy, `/satori-color` for the 4-role hex palette, `/satori-anti-ai-slop` for imperfection moves, `/satori-perception-gap` for the reading check).

Either way, you end Stage 2 holding: **communication problem · hidden truth/concept · LIFT hierarchy (leverage point + eye journey) · strategic color tokens (4 roles, hex) · feeling spec · memory hook · anti-slop moves · recognition ladder (10/5/1)**.

**Writes to Studio Job**: `## 2 · Art Direction (Satori Brief)` — the full brief, or a pointer to the ingested file plus its concept/hierarchy/color/feeling/hook/anti-slop lines pasted in (the compiler at Stage 5 reads from here, so it must be present, not linked).
**Gate**: The concept survives being described in one sentence without naming a font or color. If it can't, it's decoration, not a concept — re-run.

### Stage 3 — DIVERGENCE SPREAD (composes `/fantastic-divergence`, WF-03) — THE anti-redundancy move

**Decision forced**: What are the N *orthogonally distinct* directions the one locked concept could take — each a genuine stranger to the others?

This is the stage that separates the studio from the toy. `generate.js --n=4` fires four **separate** API calls, and each appends `"(variant N: subtly shift colour accent and framing)"` to the **same prompt** — four siblings of one idea, a colour-nudge spread. That is the redundancy problem. WF-03 instead varies **four axes at once** so no two directions share a lane:

| Axis | What varies |
|---|---|
| **Concept angle** | a different facet of the Stage 2 hidden truth |
| **Art movement** | a different Stage 1 lineage (Swiss vs Ukiyo-e vs brutalist vs riso) → a different `styles.js` primitive |
| **Composition** | different leverage point / eye journey / crop |
| **Model** | different tool where the direction demands it (a photoreal take → Soul; a typographic take → Fal) |

Generate 3–5 such directions. For each, name it, state its distinct concept angle, its art-movement/style primitive, its composition move, and — provisionally — the model it wants (confirmed at Stage 4). Reject any two directions that could be swapped by a colour override; those are tints, re-diverge.

**Writes to Studio Job**: `## 3 · Divergence Spread` — the divergence table below, one row per direction. This is the spine of the whole Studio Job.

```
| # | Direction name | Concept angle (facet of hidden truth) | Art movement / style primitive | Composition move | Provisional model |
|---|---|---|---|---|---|
| A | ... | ... | e.g. swiss-grid | leverage = ... | fal-poster |
| B | ... | ... | e.g. ukiyo-e | leverage = ... | higgsfield-soul |
| C | ... | ... | e.g. brutalist-web | leverage = ... | fal-poster |
```

**Gate**: The Orthogonality Test — for every pair of directions, name the axis on which they *fundamentally* differ (not "different color"). Can't name one? Collapse them and add a genuinely new direction. Minimum three strangers.

### Stage 4 — MODEL ROUTE (composes `/fantastic-model-route`, WF-04)

**Decision forced**: For each direction, which tool on the real model surface renders it best — and what does that route cost?

Run the router per direction; do not guess:

```bash
python3 execution/creative_router.py route --task "<the direction's one-line description>" --json
```

First match wins, specific patterns first. The surface the router owns:
- **fal-poster** — GPT Image 2 posters / typographic / stylized / packaging / menu / UI-mockup (drives `generate.js`).
- **fal-edit** — mask-aware image edit (drives `generate.js --input [--mask]`).
- **fal-rembg** — transparency / cutout (drives `generate.js --rembg`).
- **higgsfield-soul** — best photoreal + PEOPLE/character (est $0.10, ceiling $0.50).
- **higgsfield-nano** — Nano Banana Pro, fastest/cheapest iteration (use for cheap first-look drafts).
- **higgsfield-cinema** ($1.50) · **fal-kling** (multi-shot, $2.00) · **fal-seedance-720p** ($3.00 ceiling; 1080p HARD-BLOCKED) — video.
- **higgsfield-virality** (predict engagement) · **veo-3** (premium cinema, Ultra quota) · **gemini-text** (copy).

Take full advantage of the surface: a spread of five directions might legitimately route to `fal-poster` ×2, `higgsfield-soul` ×1 (the photoreal/people take), `higgsfield-nano` ×1 (a cheap concept probe), and `fal-kling` ×1 (a motion take). One brief, several instruments. Override the router only with a stated reason (write it in the row).

**Writes to Studio Job**: `## 4 · Model Route` — extend the divergence table with **confirmed service · est. cost · router reason (or override reason)** per direction, plus a **total estimated cost** line.
**Gate**: Every direction has a confirmed service and a cost number. Any video direction also notes it needs the `fal_budget_guard.py` pre-flight (Stage 6).

### Stage 5 — PROMPT COMPILE (composes `/fantastic-prompt-compile`, WF-05)

**Decision forced**: How does each direction's art-direction spec become a *model-specific* prompt the tool actually consumes?

Compile per direction, format matched to the routed model:

- **fal-poster / fal-edit / fal-rembg (`generate.js`)** — compile into a **structured brief JSON** the generator ingests via `--brief=`. The generator reads these keys: `style` (a `styles.js` id — the Stage 3 primitive, not a keyword guess), `subject`/`headline`, `subtitle`, `body`, `details`, `footer`, `palette` (from Stage 2 color tokens), `logo` (path from Stage 1). Passing `--brief=` hands the rich Satori spec to the generator instead of hoping `pickStyle()` guesses right. Write one `<direction>.brief.json` per Fal direction.
- **higgsfield-soul / higgsfield-nano / higgsfield-cinema / veo-3** — compile into a prose prompt (subject + lineage + composition + feeling + palette-in-words) for `mcp__claude_ai_Higgsfield__generate_image` / `generate_video`. When unsure of the exact model, `mcp__claude_ai_Higgsfield__models_explore` with `action: "recommend"` and the direction as context.
- **fal-kling / fal-seedance-720p** — compile a motion prompt + shot count + duration for `fal_video_kling.py` / `fal_video_seedance.py`.

Every compiled prompt must carry the Stage 2 concept, the Stage 1 lineage, the leverage point, the palette, and at least one named anti-slop move — otherwise the model regresses to default.

**Writes to Studio Job**: `## 5 · Compiled Prompts` — one labeled block per direction: the exact prompt text (or the `.brief.json` path + its contents) ready for its routed tool.
**Gate**: A second operator could paste each compiled prompt into its tool without re-asking. Fal directions have a real `.brief.json` with a valid `style` id from `styles.js` (`node generate.js --list` to confirm ids).

### Stage 6 — GENERATE (composes `/fantastic-generate-run`, WF-06) — COST-GATED, NEVER AUTO-FIRE

**Decision forced**: Assemble the exact, gated command block — then stop and hand the trigger to the human.

This stage **writes the runbook; it does not run it.** For each direction, stage the three-step gated sequence:

```bash
# 1 — MANDATORY pre-flight (blocks if over budget / needs approval)
python3 execution/cost_gate.py check --service <service> --request "<direction description>"

#     Video directions ALSO pre-flight the wallet guard:
python3 execution/fal_budget_guard.py check --mode=<kling|seedance-720p> --duration=<N>

# 2 — ONLY after cost_gate returns approved (or Farrice explicitly says yes to needs-approval):
python3 execution/cost_gate.py approve --service <service>

# 3 — THEN run the generation, THEN log actual spend:
#   Fal poster/edit/rembg (run from repo root, FAL_KEY in env):
node skills/fantastic-posters/generate.js --brief=<direction>.brief.json --size=<preset> --quality=medium
#   Fal video:
python3 execution/fal_video_kling.py ...    # or fal_video_seedance.py ...
#   Higgsfield: mcp__claude_ai_Higgsfield__generate_image / generate_video  (gated by higgsfield_budget_guard.py)

python3 execution/cost_gate.py log --service <service> --status success --actual-cost <n>
```

Quality discipline from the generator itself: `--quality=medium` (~$0.04/img) for the divergence first-look; reserve `--quality=high` (~$0.17/img) for the one locked winner. Prefer `--variants=1..4` (N images in ONE API call, cheaper siblings) for within-direction options, and reserve `--n=N` (N separate calls) only when you genuinely want the built-in per-call diversity nudge — but note the *cross-direction* diversity already came from Stage 3, so `--variants` is usually the right lever here.

**Writes to Studio Job**: `## 6 · Generation Runbook (COST-GATED — HUMAN-TRIGGERED)` — the full command block per direction, with services and sizes filled in, and the total estimated spend restated at the top.
**Gate**: Not a single generation command has been executed by the pipeline. The block is copy-pasteable and each command begins with a `cost_gate.py check`. If any command would fire paid gen without a preceding gate, the block is wrong — fix before handing off.

### Stage 7 — CRITIQUE + REFINE (composes `/fantastic-critique-refine`, WF-07) — the closed loop

**Decision forced**: After the human runs Stage 6, where does each render fall short of the brief — and what surgical edit fixes it?

Once real renders exist, critique each against four lenses: **Virgil** (does it read as intentional design or AI output?), **LIFT** (is the leverage point unmistakable, the eye journey clean?), **type** (legible at the 10/5/1 ladder, no melted glyphs?), **anti-slop** (did the intended imperfection land, or did it template out?). Then convert each defect into a **targeted mask edit** rather than a full re-roll:

```bash
# Surgical region fix (B/W mask: white = edit, black = preserve) — re-render only the broken zone:
node skills/fantastic-posters/generate.js "<describe ONLY the change>" \
  --input=out/<render>.png --mask=<mask>.png --size=<same preset> --quality=high
```

`--mask` requires an edit-mode reference (`--input`, `--refs`, or `--template`) — the generator ignores a mask without one. This re-render is paid gen, so it re-enters the Stage 6 gate: `cost_gate.py check` → approve → run → log. Loop until the render passes all four lenses or you decide the *direction* is wrong (kill it, promote another from the spread).

**Writes to Studio Job**: `## 7 · Critique + Refine Log` — per surviving render: the four-lens verdict, the specific defect, the mask-edit command (gated), and pass/fail after re-render. Ends by naming **the one locked winner**.
**Gate**: The winner passes all four lenses. A render that only "looks fine" but fails a lens is not locked — refine or replace before Stage 8.

### Stage 8 — FORMAT PACK (composes `/fantastic-format-pack`, WF-08)

**Decision forced**: Take the one locked concept and press it into every delivery format the surface needs — without re-designing.

The concept is locked; only the frame changes. Stage the format pack off the winner's brief (reuse its `.brief.json`, vary `--size`) or off the winner PNG (`--template` to hold layout, `--input`+`--mask` to adapt):

| Format | Command lever (real flags) |
|---|---|
| Feed 4:5 | `--size=1024x1280` (portrait-ish; snaps to /16) |
| Story / reel 9:16 | `--size=portrait` (1024×1536) |
| Hero / header 2:1 | `--size=hero-2to1` (2560×1280) |
| Print poster XL | `--size=poster-xl` (2048×3072) |
| Transparent cutout | `--rembg` → writes `*_alpha.png` (logos, product cutouts) |
| Animated | route to `fal-kling` / `higgsfield-cinema` — motion from the locked still |

Every format re-render is paid gen → back through the Stage 6 gate. Ultra-wide `banner-3to1` (3072×1024) exists for hero banners; aspect must stay ≤3:1 or `generate.js` rejects the size.

**Writes to Studio Job**: `## 8 · Format Pack Plan` — the format table filled for this surface, each row a gated command; note which formats are needed vs skipped for the Stage 0 surface.
**Gate**: Every needed format has a real, gated command derived from the *same* locked concept — no format silently re-designs. Cutout uses `--rembg`; animation routes to a video service, not `generate.js`.

### Stage 9 — ASSEMBLE THE STUDIO JOB

Collate Stages 0–8 into the single Studio Job artifact (template in Output Requirements). Fold Stage 7's winner decision back into the header. Restate total estimated cost. Attach the Cost & Safety note. The Studio Job is the deliverable — the renders are downstream of a human pulling the trigger on the runbook it stages.

## Content-Type Adaptations

The pipeline runs all nine stages every time; which stage **leads** shifts by surface. This is the table the Studio Job embeds so the reviewer sees where the weight sits.

| Surface | Leading stages | Divergence axis that matters most | Default routes (Stage 4) | Format pack (Stage 8) leans |
|---|---|---|---|---|
| **Poster / print** | 2 (concept) · 3 (orthogonal directions) · 7 (anti-slop survives a wall) | Art movement — each direction a distinct lineage/style primitive | `fal-poster` (mostly); a photoreal take → `higgsfield-soul` | `poster-xl`, `hero-2to1` |
| **Logo / identity** | 1 (lineage) · 2 (memory hook) · 8 (`--rembg` transparency) | Concept angle — the hook varies, not the palette | `fal-poster` + `fal-rembg`; `--logo=` to hold an exact wordmark | `--rembg` cutout, `square`, one-color check |
| **Social / feed** | 2 (thumbnail hierarchy) · 3 (scroll-stopping strangers) · 8 (4:5 ↔ 9:16) | Composition — thumbnail-legible crops differ | `fal-poster`; motion take → `fal-kling`/`higgsfield-cinema` | feed 4:5, story 9:16, animated |
| **Product / photoreal** | 1 (real reference asset) · 4 (route to Soul) · 7 (critique realism) | Model — photoreal directions to Soul, stylized to Fal | `higgsfield-soul` (people/product), `higgsfield-nano` (cheap probe) | `hero-2to1`, `--rembg` for PDP cutout |
| **Packaging** | 2 (color = shelf differentiation) · 4 · 7 (shelf-distance perception) | Art movement + composition (shelf block) | `fal-poster` (dieline/mockup); Soul for photoreal mockup | `poster-xl`, `--refs=` a dieline template |
| **Video / motion** | 3 (motion concept) · 4 (Kling vs Cinema vs Seedance vs Veo) · 6 (double gate) | Model — the video service is the decision | `fal-kling` (multi-shot), `higgsfield-cinema`, `fal-seedance-720p`; `veo-3` for hero | motion from a locked still; `fal_budget_guard.py` pre-flight |

## Output Requirements

The deliverable is a **single Studio Job** — one artifact, contradiction-free, generation-ready, with the paid trigger un-pulled. It contains, in order:

```markdown
# Studio Job — [job name / surface]

**One-sentence brief**: A [thing] that [verb] [audience] [outcome/feeling].
**Surface**: [poster / logo / social / product / packaging / video]
**Existing Satori brief ingested?**: [yes → path | no → run at Stage 2]
**Locked winner**: [named after Stage 7]  ·  **Total est. cost**: $[…]

## 1 · Reference Ground (Stage 1 · WF-01)
- Lineage anchors: [movement · studio/AD · specific artifact] ×2–4
- On-disk reference assets: [paths for --refs / --logo, or none]

## 2 · Art Direction — Satori Brief (Stage 2 · WF-02)
- Communication problem · Hidden truth/concept (one sentence)
- LIFT hierarchy: leverage point · eye journey 1→2→3
- Color tokens: | role | hex | usage | (Dominant/Secondary/Accent/Neutral)
- Feeling spec · Memory hook · Anti-slop moves (3+) · Recognition ladder 10/5/1

## 3 · Divergence Spread (Stage 3 · WF-03)
| # | Direction | Concept angle | Art movement / style primitive | Composition | Provisional model |
[3–5 orthogonal rows — each a stranger, not a tint]

## 4 · Model Route (Stage 4 · WF-04)
| # | Confirmed service | Est. cost | Router reason / override |
[per direction] · Total est. cost: $[…]

## 5 · Compiled Prompts (Stage 5 · WF-05)
- [Direction A] → Fal: `A.brief.json` { style, subject, subtitle, body, palette, logo }
- [Direction B] → Higgsfield prose prompt: "…"
- [Direction C] → …
[each carries concept + lineage + leverage + palette + ≥1 anti-slop move]

## 6 · Generation Runbook — COST-GATED, HUMAN-TRIGGERED (Stage 6 · WF-06)
[per direction: cost_gate.py check → (fal_budget_guard for video) → approve → run → log]
⚠️ Nothing here has been executed. Each command starts with a gate.

## 7 · Critique + Refine Log (Stage 7 · WF-07)
[per render: Virgil/LIFT/type/anti-slop verdict → mask-edit command (gated) → pass/fail]
→ Locked winner: [direction]

## 8 · Format Pack Plan (Stage 8 · WF-08)
| Format | Command (gated) | Needed? |
[feed 4:5 · story 9:16 · hero 2:1 · poster-xl · --rembg cutout · animated]

## Cost & Safety
⚠️ This Studio Job PLANS and STAGES. Generation is HUMAN-TRIGGERED and COST-GATED
(Fal + Higgsfield hard-gated by the PreToolUse cost-gate hook). No paid API was fired.
```

The Studio Job is complete only when: the divergence spread has ≥3 orthogonal directions, every direction has a confirmed route + cost, every Fal direction has a valid `styles.js` id in its `.brief.json`, the generation runbook is fully gated and un-executed, and the Cost & Safety note is present. Composes WF-01 through WF-08 and the Satori brain.

## Quality Gate

Before the Studio Job ships, verify:

- [ ] **Concept before pixels** — Stage 2 Satori brief locked (hidden truth in one sentence) before any prompt was compiled. Aesthetic-first ordering is an auto-reject.
- [ ] **Orthogonal, not tinted** — Stage 3 directions each fail the swap test (name the differing axis per pair). No direction is another with a `--palette` override. This is the whole point vs `generate.js --n`.
- [ ] **Router owns the instrument** — Stage 4 routed each direction via `creative_router.py`; overrides carry a written reason. The model surface was actually used (not everything defaulted to `fal-poster`).
- [ ] **Prompts are model-specific** — Fal directions have real `.brief.json` with valid `styles.js` ids; Higgsfield/video directions have their own prompt shape. Each carries concept + lineage + leverage + palette + ≥1 anti-slop move.
- [ ] **Runbook is gated and cold** — every Stage 6 command starts with `cost_gate.py check`; video adds `fal_budget_guard.py`; nothing was auto-fired.
- [ ] **Critique is closed-loop** — Stage 7 used four lenses and mask edits (not full re-rolls), and named one locked winner that passes all four.
- [ ] **Format pack, not re-design** — Stage 8 formats all derive from the one locked concept; cutout uses `--rembg`, animation routes to a video service.
- [ ] **No invented flags** — every command matches `generate.js` / `creative_router.py` / `cost_gate.py` / `fal_budget_guard.py` exactly.
- [ ] **Cost-gate honored** — the Job recommends and stages commands; it states generation is human-triggered; it fired nothing.

**Pass criteria**: all checked. Any unchecked box = the offending stage re-runs before handoff. A Studio Job that "looks comprehensive" but fails a box is a system failure regardless of length — the point is the single locked concept delivered through the right instruments with the trigger in a human's hand.

## Cost & Safety

This workflow **plans and stages; it never auto-fires a paid or cost-gated API.** Stages 0–5 and 8 are pure planning. Stage 6 and the re-render half of Stage 7 touch paid generation and are **hard-gated**:

- **Every** paid call pre-flights `python3 execution/cost_gate.py check --service <id> --request "<task>"`. Denied → surface to Farrice, do not retry. Needs-approval → ask Farrice; ONLY after an explicit yes run `python3 execution/cost_gate.py approve --service <id>`, then the generation, then `python3 execution/cost_gate.py log --service <id> --status success --actual-cost <n>`.
- **Video** additionally pre-flights `python3 execution/fal_budget_guard.py check --mode=<kling|seedance-720p> --duration=<N>`. Seedance 1080p is HARD-BLOCKED; 720p ceiling $3.00.
- **Higgsfield** MCP tools (`generate_image` / `generate_video`) are gated by `higgsfield_budget_guard.py`.
- Cost discipline: `--quality=medium` for the divergence first-look, `--quality=high` reserved for the locked winner and finals; `--variants=1..4` (one API call) over `--n=N` (N calls) unless you specifically want the per-call diversity nudge.

The human reviews the Studio Job, then pulls the trigger on the runbook — and only after the repo cost gate approves. Satori decides, the router picks the instrument, the studio critiques its own work; a human hand fires the shot.

## Related Workflows

**Composed by this pipeline** (run standalone when you need just one stage):
- `/fantastic-reference-ground` (WF-01) — anchor in real high-taste lineage
- `/fantastic-art-direct` (WF-02) — run/ingest the Satori brain (the anti-generic layer)
- `/fantastic-divergence` (WF-03) — N orthogonal directions, not colour-nudge tints (the anti-redundancy layer)
- `/fantastic-model-route` (WF-04) — route each direction via `creative_router.py`
- `/fantastic-prompt-compile` (WF-05) — art-direction spec → model-specific prompt / `--brief=.json`
- `/fantastic-generate-run` (WF-06) — the cost-gated, human-triggered runbook
- `/fantastic-critique-refine` (WF-07) — Virgil × LIFT × type × anti-slop → mask edits → re-render
- `/fantastic-format-pack` (WF-08) — one locked concept → every delivery format

**Composed Satori brain** (Stage 2): `/satori-design-think` (full brief) · `/satori-concept` · `/satori-color` · `/satori-lift-audit` · `/satori-anti-ai-slop` · `/satori-perception-gap`.

**Adjacent Creative Director** (when a direction leaves the poster lane): `/art-direct` · `/mood-board` · `/storyboard` for Higgsfield sequences; `creative_router.py` is the shared switchboard.

**Downstream generation** (human-triggered, cost-gated): `generate.js` (Fal) · `fal_video_kling.py` / `fal_video_seedance.py` · Higgsfield MCP (`generate_image` / `generate_video`) · `veo-3` via Google Flow.
