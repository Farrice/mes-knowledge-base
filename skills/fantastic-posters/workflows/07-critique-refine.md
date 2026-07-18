---
description: Score each rendered output on four lenses (Virgil / LIFT / type-legibility / anti-slop), then make TARGETED mask-based edits and re-render — the closed loop that turns a first render into something remarkable instead of shipping the first result.
---

# 07 — Critique + Refine (/fantastic-critique-refine)

> The self-judgment stage. The router picked the instrument and WF-05 pulled the trigger; now the studio critiques its own work — scores it against a real rubric, and either ships it, surgically repairs it with a `--mask` edit, or sends the concept back. Satori decides, the router picks the instrument, the studio critiques its own work.

This is the loop the v1 skill lacked. `pickStyle` → render → accept was the whole flow, so the first output was the only output. This stage refuses that. Every render is a candidate, not a deliverable. It gets four lenses of scrutiny, a verdict, and — where the verdict is REFINE — a mask that fixes the one broken zone without re-rolling the parts that worked.

## Pre-Flight Gate

**Use this when**:
- WF-05 (`/fantastic-generate`) just rendered one or more outputs and none has earned "ship" yet.
- A render is *mostly* right but has a fixable flaw — garbled title lettering, one weak element, a symmetry that reads AI-default, an accent doing its job in the wrong place.
- You inherited a poster someone accepted on the first roll and you smell one-shot acceptance (Anti-Pattern #4).
- You want a defensible, scored reason to ship or re-spend — not a gut "looks fine."

**Do NOT use this when**:
- Nothing has been rendered yet — there's nothing to critique. Run `/fantastic-generate` (WF-05) first; critiquing a plan is WF-04's job, not this stage's.
- The **concept** is what failed (wrong idea, wrong lineage, no POV) — a mask can't rescue a broken concept. Go back to `/fantastic-diverge` (WF-03) or the Satori brief, not to a refine command.
- You're on refine pass 3 and it's still failing — stop looping. Three passes with no convergence means the concept or the model route is wrong; escalate to WF-03/WF-04, don't burn a fourth edit.
- The output is pure motion/video — the four lenses here are tuned for static frames; audit a clip against its storyboard and shot list, not this rubric.

**Hard rule this stage enforces**: **REFINE beats REGENERATE.** A targeted `--mask` edit (repair the text region, evict one weak element, adjust one zone) is cheaper than a re-roll and preserves everything that already worked. Only regenerate when the *concept itself* failed. And every refine render is still a paid call — it goes through the cost gate, human-triggered, exactly like the first one.

## Skill Acquisition

```
Load: skills/fantastic-posters/genius.md
  ├─ The Critique Rubric (WF-07) ........ the four lenses + SHIP/REFINE/REGENERATE (canonical — mirrored below)
  ├─ Anti-Patterns #4, #9 ............... one-shot acceptance · title >~6 words garbles (mask-fix, don't re-roll)
  ├─ Cost Discipline .................... draft cheap, promote the winner; every refine is a gated paid call
  └─ Art-Direction Prompt Architecture .. the "describe only the change" grammar edits depend on

Composes (load as needed — Tier 1.5 hot-context; skip re-read if already loaded):
  skills/satori-graphics/workflows/01-lift-audit.md → /satori-lift-audit     (Lens 2 — L/I/F/T scored diagnostic)
  skills/satori-graphics/workflows/09-anti-ai-slop.md → /satori-anti-ai-slop (Lens 4 — human-imperfection audit)
  skills/creative-direction/…                       → /art-direct (creative-director) (Lens 1 — the Virgil Test)

Drives (the REAL code — read to confirm flags, never invent them):
  skills/fantastic-posters/generate.js → the edit surface: --input (edit mode) · --mask (surgical region) · --quality (escalation)
  execution/cost_gate.py               → mandatory pre-flight for every refine render (check → approve → log)
  execution/creative_router.py         → confirms the refine service id (route --task "edit …" → fal-edit)
```

## The Critique Rubric (canonical in genius.md — mirrored here)

Never accept the first render. Score each output on four lenses (1-10 each), then decide **SHIP · REFINE · REGENERATE**. A naked verdict is not allowed — each lens gets a score *and* a specific finding.

| # | Lens | Composes | The questions it forces |
|---|---|---|---|
| 1 | **Virgil Test** | creative-director (`/art-direct`) | Clear POV? Real tension? A *named* cultural anchor (not generically "nice")? Concept stated in one sentence? Would removing an element strengthen it? Is it interesting *without* the logo? |
| 2 | **LIFT audit** | `/satori-lift-audit` | Leverage point wins in <2s? Eye journey choreographed 1-2-3? Friction serves the leverage (not noise)? Transfers to thumbnail + light/dark + ≥2 formats? |
| 3 | **Type / legibility** | (native) | Title ≤6 words rendered clean? Hierarchy readable at 10/5/1? Any garbled lettering? — GPT Image 2's known weak spot: fix via masked re-render, never a full re-roll. |
| 4 | **Anti-slop** | `/satori-anti-ai-slop` | AI-perfect symmetry/gloss? ≥3 human-imperfection moves actually present in the pixels? Memory hook intact and legible? |

## Execution

One render or nine, the loop is the same: **score four lenses → decide the verdict → (if REFINE) write the exact edit + mask → re-render behind the gate → re-critique → escalate quality only on survivors.**

### Step 1 — Pull the render(s) and the intent to judge against

Locate the output files (WF-05 writes them to `skills/fantastic-posters/out/`). For each, put the **Satori Production Brief** (or the WF-01 Studio Job's concept/color/feeling locks) next to it. You are not scoring "do I like it" — you are scoring "does this render deliver the *decided* concept, hierarchy, feeling, and hook." Without the brief in view, critique collapses into taste roulette. If several variants exist, critique each separately — variants diverge on ≥2 axes, so they earn different verdicts.

### Step 2 — Score the four lenses (score + finding, no naked numbers)

Run each lens against the render. Compose the satori/creative-director workflow where the lens names one — don't re-derive it from scratch.

- **Lens 1 · Virgil Test** — apply the creative-director gate (`/art-direct`). Write the concept the render actually communicates in one sentence; if you can't, that's the finding. Name the cultural anchor it lands on (or "none — generic default," which is Anti-Pattern #5). Ask the removal question: which single element, removed, would make it stronger? Score 1-10.
- **Lens 2 · LIFT audit** — run `/satori-lift-audit` on the frame: L (leverage point recognized in <2s?), I (eye journey), F (friction serves), T (thumbnail + light/dark + ≥2 formats). Use its veto rule — any dimension ≤4 caps the grade. Score 1-10 (carry the LIFT composite as the finding).
- **Lens 3 · Type / legibility** — read the rendered lettering at three distances (10 m thumbnail / 5 m headline / 1 m detail). Flag any garbled, doubled, or invented glyphs (GPT Image 2's signature failure on long strings). Note if the title exceeds ~6 words — that's the *cause* of most garble (Anti-Pattern #9). Score 1-10.
- **Lens 4 · Anti-slop** — run `/satori-anti-ai-slop` in audit mode: count the human-imperfection moves *actually visible* in the render (asymmetric crop, off-rotation glyph, hand-line, negative-space asymmetry). Fewer than 3, or a plastic AI-perfect symmetry/gloss, is the finding. Confirm the memory hook survived rendering. Score 1-10.

### Step 3 — Decide the verdict

Read the four scores and findings together:

| Verdict | When | What it means for the next move |
|---|---|---|
| **SHIP** | All four lenses ≥7 and no single lens ≤5. Concept, hierarchy, type, and character all hold. | Promote to final quality (Step 6), then hand off. Done. |
| **REFINE** | The concept holds (Lens 1 ≥7) but ONE–TWO zones fail — garbled text (Lens 3), a weak element or wrong-place accent (Lens 2), thin imperfection (Lens 4). | Write a targeted edit + mask (Step 4). The parts that worked stay untouched. |
| **REGENERATE** | The concept itself failed (Lens 1 ≤5), or three-plus lenses are broken, or the wrong model rendered it. No mask can save it. | Do NOT edit. Return to `/fantastic-diverge` (WF-03) or `/fantastic-model-route` (WF-04); WF-05 re-renders the corrected direction. |

Bias hard toward REFINE over REGENERATE: a mask edit is one cheap gated call and preserves the 80% that's right; a re-roll throws it all away and re-rolls the dice on the parts that already landed. Only concept failure earns a regenerate.

### Step 4 — (REFINE) Write the targeted edit + author the mask

A refine is a **surgical instruction, not a re-description of the whole poster** — with `--input`, the shortest prompt naming *only the change* wins (Anti-Pattern #7; verbose specs make the model drift and repaint what was fine).

1. **Name the one change per pass.** "Re-render the title lettering clean, same font weight and position." "Remove the floating third badge, extend the background texture into the gap." "Rotate the accent stripe 4° and confine it to the lower-left." One zone, one instruction.
2. **Author the mask** (surgical edits only). The mask is a **B/W PNG the same dimensions as the render: white = repaint this region, black = preserve exactly.** Paint white only over the failing zone (e.g. the title box) on an otherwise-black canvas — any editor works (Preview/Photoshop/Canva), or lift a region from the `poster-to-layers` pipeline. A generous white margin around a garbled title gives the model room to re-letter; a tight mask keeps a neighbouring element untouched.
3. **Global edit without a mask** is valid when the change is whole-frame (regrade the palette, shift overall framing) — pass `--input` alone, no `--mask`.

The real refine command (run from repo root, `FAL_KEY` in env; `--input` is edit mode, so the service is `fal-edit`):

```bash
# Surgical: repair only the masked region (e.g. garbled title), preserve the rest
node skills/fantastic-posters/generate.js \
  "re-render the title text clean, exact same wording, weight, and placement" \
  --input=skills/fantastic-posters/out/<render>.png \
  --mask=<title-region-mask>.png \
  --quality=medium

# Global: whole-frame change, no mask
node skills/fantastic-posters/generate.js \
  "warm the palette toward the brief's amber accent, keep composition identical" \
  --input=skills/fantastic-posters/out/<render>.png \
  --quality=medium
```

**Cost-gate it first — a refine is a paid render like any other** (see Cost & Safety). Confirm the service the router assigns:

```bash
python3 execution/creative_router.py route --task "edit the title region of an existing poster" --json   # → fal-edit
python3 execution/cost_gate.py check --service fal-edit --request "WF-07 refine — repair title region on <render>"
```

### Step 5 — Re-critique the refined render (close the loop)

Do NOT accept the refined output on faith — that would just be one-shot acceptance one layer down. Re-run Step 2's four lenses on the new render. Two outcomes:
- **The fixed zone now passes and nothing else regressed** → advance to Step 6 (or SHIP).
- **The fix broke a neighbour, or the zone still fails** → tighten/loosen the mask or re-word the change, and refine again.

**Loop max 2–3 passes.** If pass 3 hasn't converged, the flaw is upstream (concept or model route), not in the pixels — stop refining and escalate to WF-03/WF-04. Each pass is a fresh gated paid call; log every one.

### Step 6 — Escalate quality only on survivors

Draft cheap, promote the winner (genius.md Cost Discipline). Quality escalates **only after a direction survives critique** — never render a low-confidence idea at high:

`--quality=low` (scout / cheap iteration, ~$0.011) → `--quality=medium` (review-grade, ~$0.04) → `--quality=high` (final only, ~$0.17).

When a render reaches SHIP at medium, do the final render/refine at `--quality=high` — then, if print/large-format needs more resolution, upscale **externally** (Topaz / Real-ESRGAN), which is out of this skill's surface. Never open at high on a direction the critique hasn't already validated.

## Content-Type Adaptations

The four lenses run every time; the **weighting** and the **default refine move** shift by surface.

| Surface | Lens that carries the verdict | Typical REFINE move (mask target) |
|---|---|---|
| **Poster / print** | Lens 2 (single dominant leverage at wall distance) + Lens 3 (headline legibility) | Mask the title box → re-letter clean; mask a competing element → evict and extend background (rent test). |
| **Logo / identity** | Lens 1 (concept/POV survives one-color) + Lens 4 (memory hook intact) | Global `--input` edit to simplify; `--rembg` for the transparent cutout is a *finishing* step, not a fix. Never mask-patch a wordmark — regenerate the mark if it's wrong. |
| **Social / feed** | Lens 2 T-dimension (thumbnail + square↔vertical) + Lens 3 (hook line legible at 10 m) | Mask the hook-text zone → enlarge/re-letter; confirm the refined frame still holds cropped to the other aspect ratio. |
| **Product / photoreal** | Lens 1 (does it read as a real hero, not AI-plastic) + Lens 4 (anti-slop) | This is usually a REGENERATE-to-Higgsfield-Soul, not a Fal mask edit — a photoreal person/product refine routes back through WF-04, not `fal-edit`. |
| **Packaging** | Lens 2 (shelf-distance block) + Lens 3 (brand + product legible at 5 m) | Mask the panel copy region → re-render; mask the color block → adjust to shelf-differentiation hex from the brief. |
| **Video / motion** | (rubric doesn't apply frame-by-frame) | Critique the clip against its storyboard/shot list; a bad shot re-renders through the video route (Kling/Cinema/Seedance) via WF-04, never a poster mask. |

## Output Requirements

This stage writes exactly one named block per render into the accumulating **Studio Job** — the **Critique Ledger** the front-door orchestrator (WF-00 `/fantastic-studio`) reads to decide the run is done:

```markdown
## Critique Ledger — <render filename> (WF-07 · /fantastic-critique-refine)

**Judged against**: <concept / feeling / hook from the Satori brief or WF-01 Studio Job>

| Lens | Score | Finding |
|---|---|---|
| 1 · Virgil Test | n/10 | concept-in-one-sentence: "…" · anchor: <named or "generic"> · remove-to-strengthen: <element> |
| 2 · LIFT audit | n/10 | L… I… F… T… (composite n/40, veto: <yes/no>) |
| 3 · Type / legibility | n/10 | title <=6 words? <y/n> · garble at <zone/distance>? <finding> |
| 4 · Anti-slop | n/10 | imperfection moves present: <count> · memory hook intact? <y/n> |

**VERDICT**: SHIP · REFINE · REGENERATE  — <one-line reason keyed to the failing lens>

**Refine directive** (if REFINE): change = "<the one change>" · mask = <region / "global, no mask">
**Exact refine command**:
`node skills/fantastic-posters/generate.js "<change only>" --input=out/<render>.png [--mask=<region>.png] --quality=<low|medium|high>`
**Gate**: `python3 execution/cost_gate.py check --service fal-edit --request "WF-07 refine — <render>"`

**Pass**: <1 of max 3> · **Escalation**: <low→medium→high, current tier>
⚠️ This ledger SCORES and PRESCRIBES. The refine render is HUMAN-TRIGGERED and COST-GATED — this stage does not fire it.
```

The ledger is complete only when: every render has four scored lenses each with a specific finding (no naked numbers), a verdict keyed to the failing lens, and — for any REFINE — the exact one-change command + mask target + gate string. The loop verdict for the whole Studio Job is: **all candidates SHIP, or the surviving winner is named and the rest are marked REGENERATE (back to WF-03/04) or retired.**

## Quality Gate

Before the Critique Ledger closes a render's loop, verify:

- [ ] **All four lenses scored with a finding, not a naked number** — Virgil / LIFT / type-legibility / anti-slop each carry a specific reason, not just "7/10."
- [ ] **Verdict is keyed to the failing lens** — SHIP / REFINE / REGENERATE names *which* lens failed, not a vibe call.
- [ ] **REFINE is a targeted mask edit, not a full re-roll** — the one-change instruction + mask target + gate string are all present; a full re-generation disguised as a "refine" is wrong.
- [ ] **Refine render is gated like any other** — `cost_gate.py check` → (approve on human yes) → run → log; the loop does not treat editing as free.
- [ ] **Loop capped at 2-3 passes** — escalation (low→medium→high) only on survivors; a render still failing after 3 passes gets retired or the direction regenerated, not looped indefinitely.
- [ ] **A winner is named** — the Studio Job's front door (WF-00) needs one locked render passing all four lenses, not a pile of "pretty good" candidates.

**Pass criteria**: all checked. A ledger that scores renders but never names a winner, or that treats a mask edit as free, fails this gate.

## Cost & Safety

This stage **SCORES and PRESCRIBES**. It does not fire generation. But note the asymmetry from earlier stages: **a REFINE render is itself a paid API call** — the loop cannot pretend editing is free.

- **Every refine render is gated, human-triggered, exactly like the first render**:
  ```bash
  python3 execution/cost_gate.py check --service fal-edit --request "WF-07 refine — <render/zone>"
  ```
- On `needs-approval`: surface to Farrice; only after an explicit yes run `python3 execution/cost_gate.py approve --service fal-edit` (15-min token), then the `generate.js --input …` refine, then log it:
  ```bash
  python3 execution/cost_gate.py log --service fal-edit --status success --actual-cost <n>
  ```
- **Never auto-fire.** A denied gate = surface and stop, do not retry.
- **Refine is cheaper than regenerate** — one masked `fal-edit` at medium (~$0.04) beats re-rolling a full spread — but "cheaper" is not "free." Cap the loop at 2-3 passes; each pass is a separate gated, logged call.
- **Escalate quality only on survivors** — `--quality=high` (~$0.17) is for a direction the critique already validated, never a scouting render. Final high-res beyond that is external upscaling, out of this skill.
- REGENERATE routes back through WF-04/WF-05, where the original service's gate (fal-poster / higgsfield-soul + `higgsfield_budget_guard.py`) applies again — this stage never re-fires it directly.

## Related Workflows

**The Fantastic Studio stack** (this stage closes the loop — Satori decides, the router picks the instrument, the studio critiques its own work):
- `/fantastic-studio` (WF-00) — the front-door orchestrator that reads this Critique Ledger to call the run done
- `/fantastic-studio-brief` (WF-01) / `01-reference-ground` — the concept/lineage locks this stage judges against
- `/fantastic-primitive-select` (WF-02) / `02-art-direct` — the style-primitive + prompt architecture a refine edits within
- `/fantastic-diverge` (WF-03) / `03-divergence` — where a REGENERATE verdict sends a failed concept
- `/fantastic-model-route` (WF-04) / `04-model-route` — where a photoreal/motion regenerate re-routes to the right instrument
- `/fantastic-generate` (WF-05) — the human-triggered render this stage critiques (and re-fires on REGENERATE)

**Composed (the lenses)**:
- `/art-direct` (creative-director) — Lens 1, the Virgil Test
- `/satori-lift-audit` — Lens 2, L/I/F/T scored diagnostic with the ≤4 veto
- `/satori-anti-ai-slop` — Lens 4, human-imperfection audit + memory-hook check

**Adjacent**:
- `/satori-flip-test` — a fast 90-sec structural second-opinion to run alongside the LIFT lens
- `poster-to-layers` — split a render into editable regions when authoring a precise mask
