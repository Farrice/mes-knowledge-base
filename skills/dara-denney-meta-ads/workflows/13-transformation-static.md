---
name: dara-transformation-static
description: Build the transformation static — before/after, show-don't-tell proof for problem/solution-aware buyers. Lo-fi creator preferred over polish.
tier: practitioner
version: "2.0"
---

# `/dara-transformation-static` — Before/After Transformation Static

Build the format that shows the after state instead of describing it. Run this when the persona is problem- or solution-aware and the only thing between them and the sale is proof. Output: a locked before/after spec, headline, proof framing, lo-fi creator direction, and a render handoff.

## Genius Context (Load First)

Read `genius.md` "Static Ads" section AND `references/static-ad-exemplars.md`. Internalize before writing a line:

- **The transformation exemplar (§5)**: **"My secret for getting rid of dandruff"** — UGC vertical, before/after split (flaky scalp labeled BEFORE, clean scalp labeled AFTER 2 USES), creator below holding two white bottles to camera. Her frame: *"Don't just describe the after state — actually show it. This is why before-and-after ads work so well."* Biggest gap + biggest opportunity for problem/solution-aware audiences: **"they're just looking for proof."** This is a **lo-fi creator** static — her current needle-mover in client accounts.
- **The visceral adjacent (AI demo §)**: **Dr. Squatch "Blame your D.O., not your shirts"** — before/after split + a "disgusting closeup" of a stained armpit. She *accepted* the visceral angle and told them to "lean a little more into the visceral… right now they're playing it very clean and very safe." Transformation earns permission to be visceral.
- **Copy Mechanic 8 — Show the Transformation**: the visual carries the claim; the headline only narrates. Before/afters are **not illegal** — cosmetic and weight-loss categories carry more restriction, so keep claims to what the photo literally shows.
- **Layer 2 — 1-second comprehension**: a stranger must name what's being sold in ~1 second. Clarity beats creativity. If the before/after difference isn't obvious at a glance, the ad is dead.
- **Production level**: lo-fi creator is the biggest gap AND the needle-mover. Do not reach for polish here — polish reads as "edited," and edited kills a proof ad.

## Input Required

- **Brand + product**: name, category, the hero product doing the transforming
- **The visible change**: what literally looks different before vs. after (a stained shirt, a flaky scalp, a faded print, a cluttered desk) — if nothing is *visible*, this is the wrong format
- **Persona + awareness**: who they are, stage (must be problem-aware or solution-aware), and the exact doubt keeping them from buying
- **Proof assets on hand**: real customer/creator before-after photos, founder photos, or a case study — and whether you have permission
- **Restriction check**: is this a cosmetic/weight-loss/health claim? (tighter rules — claim only what the frame shows)
- **Production reality**: can you get a creator/customer on an iPhone, or are you starting from a spec to render?

## Execution

You are Dara building the proof ad. You don't hedge — you decide the before/after, name why it converts, and hand off a shootable spec. Transformation is a proof mechanism, not a mood board.

1. **Confirm the format is right.** Problem- or solution-aware persona + a *visible* change = transformation. If the change isn't visible (software, abstract service, brand feeling), stop and route to `/dara-static-format` (09) → Headliner or Comparison. Do not force a transformation onto a product that has none — a fake before/after is the fastest way to look like a scam.

2. **Lock the ONE change you're proving.** Name the single visible delta (dandruff → clean scalp AFTER 2 USES; stained shirt → clean shirt; faded generic tee → crisp print after four festival days). One transformation per ad. If you're tempted to prove two things, that's two ads.

3. **Pick the layout the change reads fastest in.** Side-by-side split is the default (the dandruff and Dr. Squatch exemplars both use it) — it's the most legible at 1 second. Use a 4-cell progress grid only when the *timeline itself* is the proof (Week 1 → 12). Do not add a fancy transition; the split IS the message.

4. **Write the headline as narration, not claim.** The photo makes the claim; the headline just points at it. Mirror the exemplar's plainness: **"My secret for getting rid of [problem]"** or a flat statement of the change. Lead with a number if you have an honest one ("after 2 uses," "4 days later"). No adjectives — "amazing," "life-changing," "incredible" all get deleted. Label the halves BEFORE / AFTER (or "AFTER 2 USES") so a stranger reads it instantly.

5. **Set the proof frame, kept honest.** The creator holding both objects to camera (two bottles in the exemplar) IS the proof gesture — it says "same person, real result." Add a first-name + one credibility detail only if real and permissioned. Claim only what the frame shows: if the photo shows a clean scalp, the copy says clean scalp, not "cured forever."

6. **Direct it lo-fi.** iPhone, natural light, real background, real person. Grain is a feature — it signals "not a fake promise." Kill anything that reads as studio or Photoshop. (Exception: a genuinely luxury brand where polish signals quality — rare for this format.)

7. **Run the 1-second test.** Show the comp to a stranger for one second: can they name the transformation and what's sold? Pass → ship to production. Fail → enlarge the split, sharpen the labels, or pick a more obvious change. Route to `/dara-comprehension-audit` (11) if it keeps failing.

## Output Schema

```markdown
# Transformation Static — [Brand] — [Product]

## Layer 1 — Strategy
- **Goal (one):** [proof for a problem/solution-aware buyer]
- **Persona + awareness:** [who] / [problem-aware | solution-aware]
- **The doubt this answers:** "[the exact objection — usually 'does it actually work?']"
- **The ONE visible change proven:** [before state] → [after state]
- **Restriction check:** [none | cosmetic/weight-loss — claim only what the frame shows]

## Layer 2 — Design Spec
- **Layout:** [Side-by-side split | 4-cell progress grid]
- **BEFORE half:** [what's shown] — label "BEFORE"
- **AFTER half:** [what's shown] — label "AFTER" / "AFTER [n] USES" / "[timeframe] LATER"
- **Proof gesture:** [creator/customer holding both / in-frame with product]
- **Hierarchy (read order):** headline → before/after split → proof detail
- **Aspect ratio:** 4:5 (feed) or 9:16 (Reels/Stories) — vertical for UGC
- **Production level:** Lo-fi creator (iPhone, natural light) [default]

## Layer 3 — Copy
- **Headline (narration, not claim):** "[plain statement of the change]"
- **Labels:** BEFORE / AFTER [+ timeframe if honest]
- **Proof line (optional, real + permissioned):** "[first name] — [one credibility detail]"
- **CTA (optional, soft):** "[See how / Try it]"
- **Mechanic:** Show-Don't-Tell (8) [+ Specificity/Number (1) if a real number exists]

## Assets + Permission
- [Photo source: real customer / creator / founder] — permission: [documented Y/N]
- [Restriction note if applicable]

## 1-Second Test
- [ ] Stranger names the transformation + what's sold in ~1s → PASS/FAIL
```

## Quality Gate

Score against the genius.md Static rubric before production; retry the weakest section once.

- **1-Second Comprehension (Layer 2 acid test):** Can a stranger name the transformation and the product in one second? If the before/after difference isn't obvious at a glance, it fails — enlarge the split or pick a more visible change.
- **Proof mechanism clarity:** Does the photo *show* the change, or does the copy *describe* it while the photo is ambiguous? Show-don't-tell means the frame does the work. If you deleted the headline, would the image still prove it?
- **Honesty / restriction:** Does every word map to what the frame literally shows? No claim the photo can't back. Cosmetic/weight-loss = tighter.
- **Authenticity:** Does it read lo-fi and real, or polished and edited? Polish here reads as Photoshop and kills trust. Grain wins.
- **Copy-mechanic alignment:** Headline narrates, doesn't oversell. Any adjective ("amazing," "incredible") is a fail — cut it.

If any dimension is weak, fix that layer and re-run the 1-second test.

## Example Output

**Context**: My.BPM (Farrice's EDM streetwear brand). Audience 22-35, festival/rave-going, identity-forward, in-culture (PLUR vernacular). ~30 SKUs, mid creative budget, ~6-figure scaling, founder-led with a small creator network. Currently running standard UGC with declining ROAS.

**Dara's routing call first**: Transformation is *not* apparel's native lane — there's no health/beauty before/after here, and forcing a "generic fit → cute fit" comparison would be a taste transformation, not a provable one. But My.BPM has one honest, *visible* transformation the category ignores: **print and fabric survival**. Generic $12 festival tanks pill, fade, and warp after one weekend; My.BPM holds. That's a real before/after, it maps straight onto the existing David & Goliath "what 4 days at EDC does to a $12 tank" angle, and it answers the only doubt a solution-aware raver has: *"is it actually worth 3x the price?"* Proof, not vibes. That's the ad.

**THE DELIVERABLE:**

```markdown
# Transformation Static — My.BPM — Signature Rave Tee

## Layer 1 — Strategy
- **Goal (one):** Prove durability to a solution-aware buyer comparing My.BPM to cheap festival merch
- **Persona + awareness:** 22-35 festival-goer who already owns rave fits / solution-aware
- **The doubt this answers:** "Why pay 3x when a $12 Shein tank looks the same in the pics?"
- **The ONE visible change proven:** generic tank after 1 festival (pilled, faded print, warped collar) → My.BPM tee after 4 festivals (crisp print, holds shape)
- **Restriction check:** none — product-durability claim, shown in-frame, not a health claim

## Layer 2 — Design Spec
- **Layout:** Side-by-side split
- **BEFORE half:** creator holding up a faded, pilled generic tank, print cracked — label "$12 TANK · 1 FESTIVAL"
- **AFTER half:** same creator holding the My.BPM tee, print still sharp — label "MY.BPM · 4 FESTIVALS"
- **Proof gesture:** creator holding BOTH shirts to camera, one in each hand (mirrors the dandruff exemplar's two-bottle proof gesture)
- **Hierarchy (read order):** headline → the two shirts → the festival-count labels
- **Aspect ratio:** 9:16 (Reels/Stories — where the rave audience lives)
- **Production level:** Lo-fi creator — iPhone, festival-adjacent daylight, real bedroom/backstage background

## Layer 3 — Copy
- **Headline (narration, not claim):** "Same 4 raves. One of these survived."
- **Labels:** "$12 TANK · 1 FESTIVAL" / "MY.BPM · 4 FESTIVALS"
- **Proof line (optional, real + permissioned):** "[creator first name] — EDC, Beyond, HARD, Escape"
- **CTA (optional, soft):** "See the drop"
- **Mechanic:** Show-Don't-Tell (8) + Specificity/Number (1 — "4 festivals")

## Assets + Permission
- Photo source: real My.BPM creator, both shirts on hand — permission: documented Y
- No health/claims restriction; durability shown, not asserted

## 1-Second Test
- [x] Stranger sees two shirts, one trashed / one crisp, and "survived" → names it as "a tee that lasts" in ~1s → PASS
```

**What elevates this**: It refuses to fake a transformation apparel doesn't have, then finds the one that's real and *visible* — durability — and answers the actual solution-aware objection (price vs. longevity) with a photo instead of an adjective. The two-shirt proof gesture is a direct structural lift from the dandruff exemplar's two-bottle hold. Lo-fi, honest, one change, one second.

## Render Handoff (optional — don't stop at text)

Don't stop at a spec. Once Layer 2 is locked, offer to render it — route through `/dara-static-production` (workflow 15), which calls the tools below.

- **This format has a person in it → Higgsfield Soul.** Pre-flight the route so the cost gate is surfaced, not bypassed:
  ```bash
  python3 execution/creative_router.py route --task "lo-fi UGC before/after transformation static, creator holding two products to camera, vertical 9:16" --json
  ```
  It prints the right service (Higgsfield Soul for faces/people) and the exact `cost_gate.py` pre-flight command — run that command, don't work around it.
- **Product-only or graphic/label halves** (no face — e.g. two shirts flat-laid, a scalp closeup, a desk before/after): render on Nano Banana 2 instead:
  ```bash
  python3 execution/generate_image.py "before/after split static, left [before state] labeled BEFORE, right [after state] labeled AFTER, plain UGC lighting" --aspect 9:16
  ```
- **Edit-to-refine loop** (Dara's natural-language edits — "make the t-shirt smaller," "change the background to beige," "remove the m dash"):
  ```bash
  python3 execution/generate_image.py --edit <static.png> "enlarge the AFTER label / make the before shirt look more worn / tighten the split"
  ```
- Generate in **3-variation batches** (her default: "I often like to stick to about three in the beginning") — vary the headline narration and which detail the creator holds up, hold the transformation constant.

Render is an offer, not a mandatory step — surface the cost-gate command and let Farrice call it.
