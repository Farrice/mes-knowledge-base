---
name: dara-static-production
description: The renderer. Takes a locked static spec and produces real image files — brand-brain → research-first gap analysis → 3-variation batch → edit-to-refine loop. Tool-agnostic over Nano Banana 2, Higgsfield Soul, fantastic-posters.
tier: stacking
version: "2.0"
---

# `/dara-static-production` — AI Static Production (The Renderer)

Turns a locked static spec into rendered image files. Run this **after** a design spec exists (from `/dara-static-engine` (08), `/dara-educational-infographic` (12), `/dara-transformation-static` (13), `/dara-comparison-callout` (14), or a `/dara-static-ad-sprint` (17) concept). This is the "in minutes" pipeline Dara demos: build the brand brain, research before generating, batch three variations, then edit to a launchable final. The method is tool-agnostic — it renders on Nano Banana 2, Higgsfield Soul, or fantastic-posters — but every step here calls a **real tool in this repo**. Output: rendered files in `deliverables/` + a variation/QA sheet.

## Genius Context (Load First)

Read `genius.md` "Static Ads" section AND `references/static-ad-exemplars.md`. Internalize before generating a pixel:

- **The AI production pipeline (exemplars file, "AI production demo" §):** Claude builds the **brand brain** (brand voice/style/constraints as one reference doc, added to the generator's context) → **research first** (sub-agents scan competitor ad libraries, score winning ads ~62–80) → **creative gap analysis** (which awareness levels / personas / formats are missing → the real failure is *lack of creative diversity*) → generate in **3-variation batches** ("I often like to stick to about three in the beginning") → **edit-to-refine loop** with natural-language edits.
- **The edit-to-refine loop is the value, not the first render.** Her verbatim edits: *"remove the m dash," "change the background to a beige Dr. Squatch color," "the white-on-white makes it hard to see it's a t-shirt… please make the t-shirt smaller," "make me five more variations for a problem-aware audience."* Not every output is usable; the point is cheap edits to a launchable final. **Our analog is `generate_image.py --edit`.** Regenerating from scratch throws away the composition — edit instead.
- **Her taste calibration (what the render must NOT do):** she rejects **em dashes**, **misspellings** ("Deodorant spelled wrong — spell it correctly"), **"too much going on" / no focal point** ("less is more"), and **review-collage / quote-heavy social-proof statics**. She *accepts* visceral (Dr. Squatch "Blame your D.O., not your shirts," a "disgusting closeup") and told them to lean **more** visceral, not "clean and safe."
- **Production levels (genius.md):** graphic-style (infographics, comparison, grids → generate_design.py / generate_image.py), lo-fi creator (founder/transformation/people → Higgsfield Soul), hi-fi (luxury/B2B → fantastic-posters). **Lo-fi creator is the biggest current gap AND her needle-mover.** Match the audience's *expectation*, not aspirational polish.
- **The 1-second comprehension test** governs delivery: a stranger names what's sold in ~1 second, or the render dies. Clarity always beats creativity. The exemplars in `references/static-ad-exemplars.md` are the recognition set — a render is ready only when you can name which of the 7 formats it is.

## Input Required

- **Locked spec**: the design spec handed off from 08/12/13/14/17 — headline, layout/hierarchy, format archetype, aspect ratio, production level. If there's no spec, stop and route to the right builder first; the renderer does not invent strategy.
- **Brand**: name, category, hero product, voice, color palette, any hard "never" rules.
- **Format archetype** (one of the 7): educational infographic / headliner / benefits callout / comparison / transformation / grid / text-only. This decides the render tool.
- **Persona + goal + awareness**: who the 3-variation batch targets and the single job the ad does.
- **Production level**: lo-fi creator / graphic-style / hi-fi.
- **Aspect ratio**: `1:1`, `4:5` (feed), or `9:16` (Reels/Stories). *(The tools take these three — never `1.91:1`.)*
- **Assets + permission**: real photos, founder shots, or reviews on hand (and whether they're cleared). A CSV of reviews unlocks the golden-nugget-testimonial headline.

## Execution

You are Dara running production. You don't hand back a mood board — you render real files, pick the winner, and justify it. Decisive, "less is more," clarity over creativity.

1. **Build (or load) the brand brain.** Condense the spec into one reference doc the generator reads on every prompt. Keep it to a page:
   ```
   BRAND: [name] — [category] — [hero product]
   PROMISE (one sentence): [the real promise, not a slogan you invented]
   VOICE: [e.g., in-culture, founder-led, PLUR-native]
   PALETTE: [2-3 colors + accent]
   PRODUCTION LEVEL: [lo-fi creator / graphic-style / hi-fi]
   NEVER: [em dashes; misspellings; review collages; stock faces; "too much going on"]
   RECOGNITION REF: [which of the 7 exemplars this render is namable against]
   ```

2. **Research first — competitor gap analysis (do NOT skip to generating).** This is the step that separates her pipeline from "make me an ad." Pull 3-5 competitor ads in this category + format (Meta Ad Library, TikTok, Instagram), name the pattern everyone runs, and find the white space:
   ```
   COMPETITORS: [3-5 real ads — brand, angle, format, production level]
   SATURATED: [angles + production styles everyone is using]
   GAP: [untested angle / awareness level / persona / production style]
   OUR DIFFERENTIATION: [the one thing nobody else is doing]
   ```
   The failure she names is **lack of creative diversity** — if your batch and the competitors' ads all sit at the same awareness level in the same format, you've made one ad three times.

3. **Route the render to the right tool** (format decides the tool — full map in Render Routing below). Pre-flight the cost gate through the router so it's surfaced, never bypassed:
   ```bash
   python3 execution/creative_router.py route --task "<format>, <production level>, <aspect>" --json
   ```
   It prints the service (Higgsfield Soul for faces/people; graphic/product otherwise) and the exact `cost_gate.py` command. Run that command — don't work around it.

4. **Batch three variations — vary ONE thing.** Hold format + layout constant; vary the single variable you're testing (usually the headline's copy mechanic, sometimes the awareness level). Three, not ten — "stick to about three in the beginning." Each variation names its hypothesis:

   | Var | What's varied (the test) | Held constant |
   |---|---|---|
   | 1 | [mechanic A — e.g. call out the audience by name] | format, layout, palette, production level |
   | 2 | [mechanic B — e.g. negative marketing] | " |
   | 3 | [mechanic C — e.g. primal desire] | " |

5. **Generate the batch.** Write one tight prompt per variation (paste the *exact* headline, describe what's on screen, name the style/mood/palette, list exclusions), then render each. Save into `deliverables/<brand>-<format>/` as `var1.png`, `var2.png`, `var3.png`. Example call (graphic/product formats, Nano Banana 2):
   ```bash
   python3 execution/generate_image.py "<exact headline> — <layout + on-screen description>, <production level>, <palette>, no em dash, no extra text, single focal point" --aspect 4:5
   ```
   For a person/lo-fi-creator render, route to Higgsfield Soul via step 3 instead.

6. **Edit-to-refine loop (the real work).** Review each render against the spec, then fix with natural-language edits — never regenerate from scratch (you lose the composition):
   ```bash
   python3 execution/generate_image.py --edit deliverables/<brand>-<format>/var1.png "remove the em dash / make the product smaller / change background to <brand color> / enlarge the headline"
   ```
   Iterate 1-3 edits per variation. This IS Dara's loop ("remove the m dash," "make the t-shirt smaller," "change the background to beige").

7. **QA against her taste + the 1-second test.** Kill anything with an em dash, a misspelling, no focal point, or "too much going on." Then run the 1-second test on each survivor: a stranger names what's sold in ~1s (target 4/5 strangers per genius.md). If a variation fails, edit the hierarchy once; if it still fails, cut it. Ship the survivors.

## Output Schema

Write the deliverable to `deliverables/<brand>-<format>/` — the rendered files plus one sheet:

```markdown
# Static Production — [Brand] — [Format Archetype]

## Brand Brain (1 page)
[the block from Step 1]

## Gap Analysis
- Competitors / saturated / gap / differentiation [from Step 2]

## Render Route
- Format → tool: [e.g. comparison → generate_image.py, graphic-style, 4:5]
- Cost-gate pre-flight surfaced: [the exact cost_gate.py command creative_router printed]

## The 3-Variation Batch
### Var 1 — [mechanic being tested]
- Headline (verbatim): "[exact text]"
- Prompt: [the generate_* prompt used]
- File: `deliverables/<brand>-<format>/var1.png`
- Edits applied: [natural-language edits from the loop]
- 1-second test: [PASS/FAIL — what a stranger named]
### Var 2 — [mechanic] … (same structure)
### Var 3 — [mechanic] … (same structure)

## What ships / what's cut
- Ships: [Var N, N — why]
- Cut: [Var N — em dash / no focal point / failed 1-sec / redundant angle]
```

## Quality Gate

Score against the genius.md Static rubric before delivery; retry the weakest variation once.

- **1-Second Comprehension (Layer 2 acid test):** 4/5 strangers name what's sold in ~1s per render. Below that = hierarchy break; enlarge the headline or the key visual, re-test.
- **Taste conformance:** zero em dashes, zero misspellings, one focal point per render, no review-collage. Any violation = auto-fail, edit and re-run.
- **Creative diversity:** the three variations test genuinely different mechanics/awareness — not the same ad three times. If you can't state a distinct hypothesis per variation, it's one ad.
- **Grounding / honesty:** every headline is a real mechanic serving a real desire, every claim maps to something the frame or a permissioned asset actually shows. No invented stats.
- **Spec adherence:** the render matches the handed-off spec (format, layout, aspect, production level). Drift from spec = re-render, not "close enough."

If any dimension is weak, fix that layer and re-run the 1-second test.

## Example Output

**Context**: My.BPM (Farrice's EDM streetwear brand). Audience 22-35, festival/rave-going, identity-forward, in-culture (PLUR vernacular). ~30 SKUs, mid creative budget, ~6-figure scaling, founder-led with a small creator network. Currently running standard UGC with declining ROAS. Handed-off spec: a **comparison / us-vs-them** static (from `/dara-comparison-callout` (14)) — My.BPM vs generic festival merch, built off the GRO "GRO Shampoo & Conditioner vs Other Hair Growth Products" ✓/✗ pattern.

**Dara's call first**: The declining ROAS isn't a media problem, it's a diversity problem — standard UGC is one awareness level in one format. The comparison static is graphic-style, so it renders on Nano Banana 2, not Higgsfield (no face in this one). I'll hold the ✓/✗ layout constant and test the *headline mechanic* across three variations, all aimed at the same solution-aware raver deciding whether My.BPM is worth 3x a Shein tank.

**THE DELIVERABLE:**

```markdown
# Static Production — My.BPM — Comparison / Us-vs-Them

## Brand Brain
BRAND: My.BPM — EDM/rave streetwear — Signature Rave Tee
PROMISE: Gear that survives four festivals and still reads like you belong on the rail.
VOICE: In-culture, PLUR-native, founder-led, zero corporate polish
PALETTE: near-black, acid green accent, off-white
PRODUCTION LEVEL: graphic-style (comparison grid)
NEVER: em dashes, misspellings, review collages, stock rave stock-photos, >1 focal point
RECOGNITION REF: GRO comparison exemplar (✓/✗ two-column grid)

## Gap Analysis
- Competitors: generic festival-merch brands running lifestyle UGC (girl in tank at sunset), Shein "rave" collections (price-only), one competitor running a plain product flat-lay.
- Saturated: lifestyle UGC, price-only. Nobody runs an explicit ✓/✗ durability comparison.
- Gap: the us-vs-them grid at the solution-aware level — the buyer already wants a rave fit, the open question is "why pay 3x?"
- Differentiation: make durability + fit-integrity legible in one glance via ✓/✗, the way GRO made hair-growth legible.

## Render Route
- Format → tool: comparison → `generate_image.py`, graphic-style, 4:5 (feed)
- Cost-gate pre-flight surfaced: `python3 execution/creative_router.py route --task "us-vs-them comparison static, graphic-style, 4:5" --json` → printed the fal/nano-banana route + `cost_gate.py` command; ran it, approved.

## The 3-Variation Batch (headline mechanic varied; ✓/✗ layout held constant)
Layout (constant): two columns — left "MY.BPM" (acid-green ✓ rows), right "$12 Festival Tanks" (red ✗ rows). Rows: "Print survives 4 festivals", "Holds shape in the pit", "Cut for the rail, not the rack", "Made by people who go". Product tee at top-left, generic tank top-right.

### Var 1 — Call out the audience by name (Mechanic 2)
- Headline: "Ravers: your $12 tank isn't making it to Day 3."
- Prompt: `generate_image.py "Ravers: your $12 tank isn't making it to Day 3. — two-column us-vs-them comparison, left column MY.BPM with acid-green checkmarks, right column $12 Festival Tanks with red x marks, rows about print/shape/cut/durability, near-black background, off-white type, single focal point, no em dash" --aspect 4:5`
- File: `deliverables/mybpm-comparison/var1.png`
- Edits applied: `--edit … "make the acid-green checkmarks brighter / shrink the generic tank so MY.BPM tee is the focal point"`
- 1-second test: PASS — stranger named "a rave shirt that lasts vs a cheap one"

### Var 2 — Negative marketing (Mechanic 6)
- Headline: "Pilled. Faded. Warped. That's a $12 tank after one weekend."
- Prompt: same layout; headline swapped verbatim.
- File: `deliverables/mybpm-comparison/var2.png`
- Edits applied: `--edit … "remove the extra subhead — too much going on, keep one focal line"`
- 1-second test: PASS

### Var 3 — Primal desire (belonging) (Mechanic 4)
- Headline: "Dress like you belong on the rail, not in the crowd."
- Prompt: same layout; headline swapped verbatim.
- File: `deliverables/mybpm-comparison/var3.png`
- Edits applied: `--edit … "change background to near-black brand color, off-white was washing out"`
- 1-second test: PARTIAL — desire-led headline reads slower than the ✓/✗; enlarged the headline once, re-tested → PASS

## What ships / what's cut
- Ships: Var 1 (audience callout — sharpest self-selection) + Var 2 (negative marketing — fastest 1-sec read). Distinct hypotheses: does naming the buyer beat naming the failure?
- Cut: none this batch — Var 3 passed on the retry, held as the desire-led challenger for the next round.
```

**What elevates this**: it renders real files off a real spec, holds the layout constant so the test is honest (one variable — the headline mechanic), routes through the cost gate instead of around it, and uses the edit-to-refine loop exactly as Dara does ("too much going on," "make the tank smaller," "change the background to the brand color"). Every headline is a named mechanic serving a real desire — no invented stat, no em dash, one focal point each.

## Render Routing (format → real tool)

This is the renderer, so the routing map IS the handoff. Format decides the tool; every path pre-flights the cost gate via `creative_router.py`.

- **Educational infographic / benefits callout** (graphic-style, chart or callout): `python3 execution/generate_design.py --type graphic --aspect 4:5 "<the locked spec as a brief>"` — its art-direction → Nano Banana 2 pipeline turns a DESIGN.md-style brief into a rendered graphic. Use `--prompt-only` to inspect the compiled prompt first.
- **Comparison / grid / headliner / text-only** (graphic or product, no face): `python3 execution/generate_image.py "<exact headline> — <layout + on-screen description>" --aspect <1:1|4:5|9:16>` on Nano Banana 2. Use `--reference <img.png>` to lock a product shot.
- **Transformation / founder / any lo-fi creator (a person in frame)** → **Higgsfield Soul**, routed and cost-gated through `python3 execution/creative_router.py route --task "lo-fi UGC creator static, <aspect>" --json`. Faces are Soul's lane, not Nano Banana's.
- **Heavy stylized poster / hi-fi art-direction**: the `fantastic-posters` skill (Fal / GPT-Image-2, 38 styles) — **cost-gated**; surface the pre-flight, don't bypass.
- **Edit-to-refine loop (every path):** `python3 execution/generate_image.py --edit <file.png> "<natural-language edit>"` — "remove the em dash," "make the product smaller," "change the background to <brand color>," "enlarge the headline." Iterate; don't regenerate from scratch.
- **Cost note:** image generation can trip the cost gate. `creative_router.py` prints the exact `cost_gate.py` command — run it, never work around it. Denied = surface to Farrice; needs-approval = ask, then approve and retry.

Next: to expand the winner into a full concept set, run `/dara-static-ad-sprint` (17); to validate before spend, run `/dara-comprehension-audit` (11) on each variation.
