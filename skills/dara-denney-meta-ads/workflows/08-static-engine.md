---
description: Front door for static ads — run the full 3-Layer build (Strategy → Design → Copy) and output one production-ready static-ad design spec.
---

# `/dara-static-engine` — The 3-Layer Static Ad Build

The flagship static workflow. If you only run one, run this. It takes a brand + persona and produces a single, production-ready static-ad spec: headline, visual hierarchy, copy, format, aspect ratio, and production level — built the way Dara builds them, Strategy → Design → Copy, each layer gating the next.

## Genius Context (Load First)

Read `skills/dara-denney-meta-ads/genius.md` — the **Static Ads** section — and internalize:
- The **3-Layer System** (Strategy → Design → Copy) and why Layer 1 gets buttoned up *before* a line of copy is written
- **Objection-to-Format matching** (pick the format from the persona's objection, not your product's benefit)
- **Format → Awareness matching logic** and the **8 copy mechanics** ranked by objection type
- The **3 production levels** (lo-fi creator / graphic-style / hi-fi) and the "match audience expectation, not aspirational polish" rule

Then read `skills/dara-denney-meta-ads/references/static-ad-exemplars.md` — the **frame-grounded** exemplar set. This is your source of truth for any example. Every static you build should be namable against one of these seven:
1. Educational infographic — Sweetgreen **"The Economics of $15 Salads"**
2. Headliner — Happy Tuesdays **"The cheat code to your big weekend."** / Wandering Bear **"SO GOOD IT SHOULD BE BAD FOR YOU"** / TIME **"…the closest we've gotten to a fountain of youth"**
3. Benefits callout — headline-at-top; test core-desire vs generic; slot a golden-nugget testimonial into the headline
4. Comparison / us-vs-them — **"GRO Shampoo & Conditioner"** vs **"Other Hair Growth Products"** (green ✓ / red ✗)
5. Transformation — **"My secret for getting rid of dandruff"** before/after, lo-fi creator holding two bottles
6. Grid static — **"MEET THE Cook & Bake Set"** $1,090 → $632, ~9 product tiles
7. Text-only — totallee **"iPhone Cases Are Weird."** founder's-letter

> Do not invent headlines. If you need an example, pull one of the seven above. A converting static is one you can name against this set.

## Input Required

- **Brand**: name, category, hero product/offer in one sentence
- **ONE goal**: pick a single action — offer/purchase, lead capture, or educate a problem-aware buyer. One ad does one job. Do not make it do two.
- **Specific persona**: stage + objection (NOT "small business owners"). The objection drives vocabulary, proof, and format.
- **Awareness level** (if known): unaware / problem-aware / solution-aware / brand-aware / decision-stage. If unknown, infer it from the objection.
- **Production budget/constraint** (optional): tells you lo-fi vs graphic-style vs hi-fi.
- **Customer reviews CSV** (optional, high-value): for golden-nugget testimonial mining.

If the persona is still "business owners" or the goal is a list, stop and sharpen — a vague Layer 1 poisons everything downstream. `/avatar-machine` sharpens persona; `/awareness-ladder` maps the goal to a stage.

## Execution

You are Dara. You don't lecture the layers — you make the three decisions, name why, and hand back a spec someone can shoot or render from. Less is more. Clarity beats creativity every time.

### Step 1 — Layer 1: Strategy (button this up first)
1. **Lock ONE goal.** Offer ad, education, or target a problem-aware buyer — one job. Write it as a single action ("first purchase of the hero tee," not "awareness + sales").
2. **Write the persona as stage + objection**, in one visceral sentence. The objection is the load-bearing part — it decides which of the seven formats you reach for and which copy mechanics fire.
3. **Pick the format FROM the objection**, not the product:
   - "I didn't know this was a problem" → **Educational infographic** (Sweetgreen)
   - "Why yours vs theirs? / does it last?" → **Comparison / us-vs-them** (GRO)
   - "Does it actually work? show me" → **Transformation** before/after (dandruff)
   - "Sell me the feeling" → **Headliner** (Wandering Bear / Happy Tuesdays)
   - "I've got range/value objections" → **Grid static** (Cook & Bake) or **Benefits callout**
   - "Ads feel fake to me" → **Text-only** founder's letter (totallee)
4. **Match the awareness level** — it's the bridge connecting persona + goal to the format. Problem/solution-aware buyers "are just looking for proof" → transformation/comparison. Unaware → educational.
5. **Write the one-paragraph strategy brief**: *"For [persona + objection], at [awareness level], to drive [one goal], using [format]."*

### Step 2 — Layer 2: Design (visual hierarchy + the 1-second test)
1. **Order the hierarchy, headline first.** The headline does the targeting, so it leads — it's the focal point ~9 times out of 10. Then the product/key visual. Then supporting elements (proof, price, badge, CTA). Rank them; don't assign percentages — Dara never did.
2. **Set the focal point on the messaging**, not the aesthetic. If the headline and the product fight, the headline wins.
3. **Run the 1-second comprehension test.** Show it to a stranger for one second, cover it, ask "what is this selling?" If they can't answer, kill the design and re-stack the hierarchy. If they get the *what* but miss the *differentiator*, the proof element is too small — pull it up.
4. **Clarity > creativity.** No overlapping text-on-visual, no trendy type that sacrifices readability, high contrast, one primary font. If it reads as "this and this and this and this" with no focal point, it's the ad Dara scraps.

### Step 3 — Layer 3: Copy (the most important layer)
Reach for the mechanics the objection calls for — usually 1-2, rarely 3+ (stacking past three is cognitive overload):
1. **Be specific.** Name the demographic, give exact numbers, lead with a number that communicates time/effort/cost ("five minutes," "under $5," "2 inches in one use").
2. **Call out the audience by name.** Self-selection is a targeting mechanic — it improves who clicks.
3. **Lean into the taboo.** Say what politer competitors won't (Wandering Bear: "SO GOOD IT SHOULD BE BAD FOR YOU").
4. **Tap a primal desire** (status, sex, belonging, safety, approval). Product = the mechanism; the *desire* is the headline. TIME's "fountain of youth" sells youth, not capsules.
5. **Open a curiosity loop.** Show the setup, hide the payoff through the click; satisfy it on the landing page. Use on education; skip on hard-offer product ads.
6. **Negative marketing.** Name what the audience is afraid of; say it in the negative aspect (the GRO ✗ column, the dandruff BEFORE).
7. **Borrow from customers.** Run the reviews CSV through the LLM and pull the golden-nugget testimonials — verbatim customer language, then hand-curate (LLMs surface ~40% generic praise).
8. **Show the transformation.** Don't describe the after — show it. Before/after is why those ads work. (Before/afters aren't illegal; cosmetic/weight-loss carry more restriction.)

Then apply the omission pass: if you can delete a word and still get the benefit, delete it.

### Step 4 — Assemble the production spec + pick the level
1. Fold Layers 1-3 into the **Output Schema** below.
2. **Pick the production level** by matching audience expectation, not aspirational polish: **lo-fi creator** (founder/customer, real environments — the current needle-mover for problem/solution-aware proof), **graphic-style** (infographics, comparison grids, feature layouts), or **hi-fi** (luxury/B2B where polish signals credibility).
3. **Set the aspect ratio** for placement: `1:1` or `4:5` for feed (mobile-first), `9:16` for stories/reels.
4. Name the **exemplar** this ad mirrors and what it borrows from it.

## Output Schema

```markdown
# Static Ad Spec — [Brand] · [Format]

## Layer 1 — Strategy
- **Goal (one):** [single action]
- **Persona (stage + objection):** [one visceral sentence]
- **Awareness level:** [unaware / problem / solution / brand / decision]
- **Format:** [one of the 7] — chosen because the objection is "[…]"
- **Exemplar mirrored:** [named exemplar] → borrowing [what]

## Layer 2 — Design (visual hierarchy, top → bottom)
1. **Headline** (focal point): [placement — leads]
2. **Key visual / product:** [what, where]
3. **Supporting:** [proof / price / badge / CTA — placement]
- **Contrast + type:** [high-contrast scheme, one primary font]
- **1-second test:** a stranger names "[what's sold]" in ~1s → PASS/FAIL
- **Differentiator visible at a glance?** [yes / pull it up]

## Layer 3 — Copy
- **Headline:** [final]
- **Sub / proof line:** [customer language or specific stat]
- **CTA:** [one action, if space]
- **Mechanics used:** [1-2, named]

## Production
- **Level:** [lo-fi / graphic-style / hi-fi] — because [audience expectation]
- **Aspect ratio:** [1:1 / 4:5 / 9:16]
- **Placement / audience:** [feed / stories; targeting note]
```

## Quality Gate

Score against the genius.md **Static Quality Rubric** (1-Second Comprehension, Proof-Mechanism Clarity, Visual-Hierarchy Adherence, Copy-Mechanic Alignment) plus:
- **1-second recognition test** — can a stranger name what's sold in ~1 second? If not, the hierarchy is broken; re-stack Layer 2 before anything else. This vetoes the ad regardless of the rest.
- **Format is named** — the spec maps to one of the seven exemplars, not a vibe.
- **Headline sells a desire/outcome, not a spec.**
- **Objection → format → mechanic form one chain** — the format answers the objection; the mechanic is the one that objection calls for.

If any dimension scores <7, retry the weakest layer once (usually Layer 3 copy or the Layer 2 focal point), then re-run the 1-second test.

## Example Output

**Context:** My.BPM — Farrice's EDM/rave streetwear brand. Audience 22-35, festival/rave-going, identity-forward, PLUR vernacular, ~30 SKUs, mid creative budget, ~6-figure and scaling. Currently runs standard UGC with declining ROAS. Goal for this ad: first-purchase conversion on the hero festival tee.

**THE DELIVERABLE:**

```markdown
# Static Ad Spec — My.BPM · Comparison / us-vs-them

## Layer 1 — Strategy
- **Goal (one):** First purchase of the hero festival tee (cold traffic → PDP).
- **Persona (stage + objection):** The Day-3 raver — "By the last night of EDC my fit is pilled, faded, and sweated-through; I've been burned by $12 Shein 'rave' tanks that die after one wear. Why would yours be different?"
- **Awareness level:** Solution-aware — she knows festival streetwear exists; she's looking for proof it lasts.
- **Format:** Comparison / us-vs-them. Chosen because the objection is "why yours vs the cheap stuff / does it survive?" — that's a ✓/✗ decision, not a feeling.
- **Exemplar mirrored:** "GRO Shampoo & Conditioner" vs "Other Hair Growth Products" → borrowing the two-column green-✓/red-✗ grid that makes the advantage legible in one glance, with negative marketing baked in.

## Layer 2 — Design (visual hierarchy, top → bottom)
1. **Headline** (focal point, leads): top band, call-out-by-name — largest text on the frame.
2. **Key visual:** two columns. Left "My.BPM" (the tee, crisp after four days). Right "Generic Rave Merch" (faded, pilling tank). Product second to the message.
3. **Supporting:** four ✓/✗ rows down the middle; small "Shop the fit" button bottom-right.
- **Contrast + type:** near-black background, acid-green ✓ vs muted-red ✗, one bold condensed sans (in-culture, flyer-adjacent). High contrast; no text over the garment.
- **1-second test:** stranger names "festival shirt that lasts vs cheap ones" in ~1s → PASS.
- **Differentiator visible at a glance?** Yes — the ✓/✗ column reads before the copy does.

## Layer 3 — Copy
- **Headline:** "Ravers: your fit shouldn't die before the encore."
- **✓/✗ rows (My.BPM ✓ / Generic ✗):** "Survives 4 days of EDC" · "Sweat-proof color — won't fade" · "Reinforced seams, no Day-3 pilling" · "Cut for the pit, not the mall"
- **CTA:** "Shop the fit."
- **Mechanics used:** Call out the audience by name ("Ravers") for self-selection + negative marketing (the ✗ column names exactly what she's afraid of). Specificity anchors the top ✓ ("4 days").

## Production
- **Level:** Graphic-style — comparison grids are a graphic-style format; the persuasion is the layout, not photographic polish. (Budget-efficient; leaves lo-fi creator budget for the transformation variant next.)
- **Aspect ratio:** 4:5 — mobile-first feed for a 22-35 audience.
- **Placement / audience:** IG/FB feed, cold prospecting; problem/solution-aware lookalikes off past festival-season purchasers.
```

**What elevates this:** the format wasn't a vibe — it was reverse-engineered from one objection ("does it last?"), which is a comparison decision, so it maps to GRO's ✓/✗ grid. The headline sells the *outcome* (surviving the night, being seen) and names the audience so it self-selects. The proof (the ✗ column) is visible before the copy, so it clears the 1-second test. And it names the next variant — a lo-fi creator transformation static — instead of pretending one ad does every job.

## Render Handoff (optional — don't stop at text)

Once the spec is locked, offer to render it — don't force it. The clean handoff is `/dara-static-production` (workflow 15), which routes through the repo's real tools and surfaces the cost-gate pre-flight. For **this** workflow's default (comparison / grid / graphic-style layouts), the direct route is:

```bash
# Graphic comparison/grid layout — text + product tiles, not a photoreal person
python3 execution/generate_image.py "My.BPM festival-tee comparison static: near-black bg, two columns 'My.BPM' vs 'Generic Rave Merch', acid-green checks vs muted-red x's, headline 'Ravers: your fit shouldn't die before the encore', bold condensed sans, high contrast" --aspect 4:5
```

Format-specific routing:
- **Infographic / comparison / grid / text-only** → `generate_image.py` (or `generate_design.py --type ... "<brief>"` for an art-directed graphic-style pass).
- **Transformation or founder static with a real person/face** → route through `python3 execution/creative_router.py route --task "<lo-fi creator before/after>"` → **Higgsfield Soul** for the person.
- **Heavy art-direction / stylized poster** → `fantastic-posters` skill (cost-gated).

**Edit-to-refine loop** (Dara's natural-language edits, our analog): iterate on the render without rebuilding —
```bash
python3 execution/generate_image.py --edit out.png "make the t-shirt smaller, change the background to a deeper black, remove the em dash"
```
Generate in **3-variation batches** ("stick to about three in the beginning"), not one-shot. If a render step trips the cost gate, `creative_router.py` prints the exact `cost_gate.py` pre-flight — surface it to Farrice, never bypass it.
