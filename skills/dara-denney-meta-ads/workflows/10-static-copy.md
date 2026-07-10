---
name: dara-static-copy
description: Layer-3 copy engine — apply Dara's 8 static copy mechanics to produce headline + supporting-copy variants (incl. the review-CSV golden-nugget mine). Output: tagged copy options ready for production.
tier: "Tier 1 (Static) — Layer 3 Copy"
version: "2.0"
---

# `/dara-static-copy` — Static Copy Engine (Layer 3)

Run after Layer 1 (strategy) and Layer 2 (design) are buttoned up. This is the copy layer — the most important layer. It applies the 8 static copy mechanics to produce headline + supporting-copy variants, each tagged by mechanic, and includes the golden-nugget review-CSV mine. Output: a small set of production-ready copy options for one static ad.

## Genius Context (Load First)

Read `genius.md` → **"Static Ads"** section, and `references/static-ad-exemplars.md` (frame-grounded, verbatim). Internalize before writing a line:

- **The 8 copy mechanics** — Be Specific · Call Out the Audience by Name · Lean Into the Taboo · Tap a Primal Desire · Open a Curiosity Loop · Negative Marketing · Borrow From Customers · Show the Transformation. Copy is Layer 3, and it is the layer that decides.
- **The exemplars you write toward** (never invent past these): Wandering Bear **"SO GOOD IT SHOULD BE BAD FOR YOU"**; TIME/supplement **"…the closest we've gotten to a fountain of youth"** + **"USE CODE TRY25 FOR 20% OFF"**; Sweetgreen **"The Economics of $15 Salads"**; Happy Tuesdays **"The cheat code to your big weekend."**; GRO **"GRO Shampoo & Conditioner"** vs **"Other Hair Growth Products"** (✓/✗ grid); **"My secret for getting rid of dandruff"** (before/after, 2 uses); **"MEET THE Cook & Bake Set"** ($1,090 → $632); totallee **"iPhone Cases Are Weird."**; Dr. Squatch **"Blame your D.O., not your shirts."**
- **The rule that overrides taste**: clarity always beats creativity. A stranger names what's sold in ~1 second, or the copy is dead. Less is more — one focal message, not "this and this and this."
- **The headline sells a desire/outcome, not a spec.** Product is the mechanism; the desire is the headline.

## Input Required

- **Locked strategy** (from `/dara-static-engine`): the single goal, the specific persona (stage + objection), the awareness level, the proof mechanism.
- **Locked format** (from `/dara-static-format`): which of the 7 archetypes + production level (lo-fi creator / graphic-style / hi-fi).
- **Persona vocabulary**: the words the buyer actually uses (from research or the review CSV).
- **Review CSV** (optional but high-yield): an export of customer reviews to mine for golden-nugget testimonials.

If strategy or format isn't locked, stop and run `/dara-static-engine` → `/dara-static-format` first. Copy without a locked goal makes one ad do two jobs, which is how ads die.

---

## The 8 Copy Mechanics

Each mechanic answers a specific objection. **Stack at most 2 per ad** — one focal, one support. More than two and you lose the focal point.

### 1. Be Specific
Name the demographic, give exact numbers, and lead with a number that communicates **time, effort, or cost**. Vague is invisible; a number stops the scroll and lets the reader do the value math in their head.
- **Dara's live examples**: "five minutes," "under $5," "2 inches in just one use."
- **Solves**: cost / time / efficacy doubt.
- **Use**: any awareness level — it's a utility mechanic that compounds with the others.
- **Avoid**: pure luxury/aspiration, where a hard number can feel cheap.

### 2. Call Out the Audience by Name
Self-selection is a copy mechanic, not just a vibe — naming the exact person improves targeting by getting the right person to raise their hand and the wrong person to scroll past. Persona drives the vocabulary.
- **Shape**: "For [hyper-specific persona/philosophy]" or a direct address in the buyer's own words.
- **Solves**: "is this for me?" identity doubt.
- **Use**: niche positioning, culture-as-moat brands. **Avoid**: unaware audiences who won't yet self-identify.

### 3. Lean Into the Taboo
Say the thing competitors are too polite to say. Taboo lands as instant recognition ("yes, that's me") and signals no-BS authenticity.
- **Exemplars**: Wandering Bear **"SO GOOD IT SHOULD BE BAD FOR YOU"** (permission to indulge); Dr. Squatch **"Blame your D.O., not your shirts."**
- **Solves**: identity / status doubt, guilt around the purchase.
- **Best home**: the Headliner format. **Avoid**: cold trust-building before any proof exists.

### 4. Tap a Primal Desire
Write to a primal motivation — **status, sex, belonging, safety, approval**. The product is the mechanism; the desire is the headline.
- **Exemplar**: TIME/supplement **"…the closest we've gotten to a fountain of youth"** — the desire (youth/status) is the whole headline; the capsule is just the mechanism.
- **Solves**: emotional efficacy ("will this make me feel the way I want to feel?").
- **Use**: transformation, lifestyle, premium/aspiration. **Avoid**: feature-heavy or unaware-audience education.

### 5. Open a Curiosity Loop
Show the setup, hide the payoff through the click, then satisfy it on the landing page. Curiosity is one of the highest-converting drivers — but you must pay it off, or you burn trust.
- **Exemplars**: Sweetgreen **"The Economics of $15 Salads"** (you don't know the number — click); Happy Tuesdays **"The cheat code to your big weekend."** (what's the cheat code?).
- **Solves**: unaware / problem-aware gaps.
- **Avoid**: decision-stage buyers who need proof now, not mystery. Never bait a loop you don't close.

### 6. Negative Marketing
Say things in the negative — name what the audience is afraid of, or what the alternative fails to do. Negative frames are stickier than positive ones. "Not X" reads as more credible than "premium quality."
- **Exemplar**: GRO **"GRO Shampoo & Conditioner"** vs **"Other Hair Growth Products,"** ✓/✗ rows ("No harmful side effects," "Hormone free," "Visible results in 90 days," "Certified vegan & clean").
- **Solves**: comparison doubt, cost-vs-cheaper-option doubt.
- **Best home**: the Comparison / us-vs-them format. **Avoid**: unaware audiences who don't know the alternatives yet.

### 7. Borrow From Customers (Golden-Nugget Mine)
Your best copy is already written — by your customers. Run a **CSV of reviews through your LLM** and pull the golden-nugget testimonials: the ultra-specific, insider-sounding lines no copywriter would think to write. Then slide the nugget straight into the headline.

> **The move.** Export reviews to CSV → feed the LLM this prompt:
> *"Here is a CSV of customer reviews. Find the 5–10 'golden nugget' lines — hyper-specific, benefit-forward, written in the customer's own voice, that a copywriter would never think to write. No generic 'life-changing' / '10/10' fluff. Return each verbatim quote + the specific objection it defuses + the exact phrase I could lift into a headline."*

- **Adjacent form**: borrow a *third-party authority's* words — TIME's **"fountain of youth"** is a borrowed quote doing the persuading; the brand just frames it.
- **Solves**: efficacy + trust (proof from a peer, not the company).
- **Dara's taboo here**: she rejects review-collage / quote-heavy social-proof statics — "I don't really love how those always turn out." So mine many, ship **one** nugget as the headline. One knife, not a drawer of them.

### 8. Show the Transformation
Don't just describe the after state — **show it**. Before/after is why this format works; the image carries the proof and the copy gets out of the way.
- **Exemplar**: **"My secret for getting rid of dandruff"** — before/after split (flaky scalp BEFORE → clean AFTER 2 USES), creator holding the two bottles (lo-fi creator).
- **Solves**: skepticism for problem/solution-aware buyers "just looking for proof."
- **Note**: before/afters are not illegal; cosmetic/weight-loss categories carry more restriction — write to the claim you can defend.

---

## Mechanic Selection Matrix

Match awareness level + primary objection to the strongest mechanic(s). ★★ = lead, ★ = support.

| Awareness | Primary objection | Lead mechanic(s) | Support |
|---|---|---|---|
| **Unaware** | Doesn't know the problem exists | ★★ Curiosity Loop | ★ Primal Desire |
| **Problem-Aware** | Doesn't know solutions exist | ★★ Curiosity Loop · ★ Be Specific | ★ Taboo / Primal Desire |
| **Solution-Aware** | Comparing alternatives | ★★ Negative Marketing · ★★ Be Specific | ★ Show the Transformation · ★ Borrow From Customers |
| **Brand-Aware** | Making the final call | ★★ Borrow From Customers · ★★ Show the Transformation | ★ Call Out by Name · ★ Be Specific |

**Rule:** max 2 mechanics per ad. Combine to amplify (e.g., Be Specific + Show the Transformation on a before/after: "2 inches — after 1 use").

---

## Format → Copy Formula

Each of the 7 archetypes has a native copy shape. Write toward the real exemplar, never past it.

| Format | Copy shape | Real exemplar | Mechanic priority |
|---|---|---|---|
| **Educational infographic** | Curiosity-gap title over a data/chart look | "The Economics of $15 Salads" | Curiosity Loop → Be Specific |
| **Headliner** | One big message = the focal point | "SO GOOD IT SHOULD BE BAD FOR YOU" · "The cheat code to your big weekend." | Taboo / Primal Desire → Be Specific |
| **Benefits callout** | Top headline taps the core desire; or a golden nugget as the headline | (test core-desire vs generic; slide a testimonial in) | Call Out by Name → Borrow From Customers |
| **Comparison / us-vs-them** | Us column vs them column, ✓/✗ rows | "GRO Shampoo & Conditioner" vs "Other Hair Growth Products" | Negative Marketing → Be Specific |
| **Transformation** | Quote/claim over a before/after split | "My secret for getting rid of dandruff" (AFTER 2 USES) | Show the Transformation → Be Specific |
| **Grid static** | Set name + price anchor over a product grid | "MEET THE Cook & Bake Set" $1,090 → $632 | Be Specific → Show the Transformation |
| **Text-only** | Founder's-letter opener line + short body | "iPhone Cases Are Weird." (totallee) | Taboo → Call Out by Name |

---

## Execution

You are Dara writing the copy layer. Pick, justify in one line, move. Don't lecture the mechanics — deploy them.

1. **Restate the locked strategy** in one line: goal · persona (stage + objection) · awareness · proof mechanism · format · production level. If any is missing, stop — don't paper over a soft strategy with clever copy.
2. **Mine the reviews (if a CSV exists).** Run the golden-nugget prompt (Mechanic 7). Keep the top 1–2 verbatim nuggets + the objection each defuses. This is the highest-leverage 5 minutes in the workflow — real customer language beats invented copy every time.
3. **Pick the mechanic(s).** Cross the persona's objection + awareness against the Matrix. Name the ★★ lead. Add at most one ★ support only if it amplifies the same focal point.
4. **Write 3 headline variants**, tagged by mechanic, using the Format → Copy Formula:
   - Var A = lead mechanic, cleanest expression.
   - Var B = a different angle on the same desire (or the golden nugget as headline).
   - Var C = lead + support fused (only if it stays one focal message).
   Reject em dashes in headlines, fix any misspelling, and cut any second idea. Less is more.
5. **Run the 1-second test** on each: would a stranger, glancing for one second, name what's sold *and* feel the benefit? If not, it's not clever — it's dead. Rewrite or cut. Pick the one that wins the glance, not the one that's most "creative."
6. **Write the supporting copy** the format needs (sub-head, ✓/✗ rows, price anchor, CTA) — only what the format actually carries. Note what the *image* must carry so copy doesn't over-explain.
7. **Lock the spec card** (Output Schema). Tag every line with its mechanic so production knows what's load-bearing.

---

## Output Schema

```markdown
# Static Copy Spec — [Brand] · [Format]

## Strategy (locked)
- Goal: [offer / education / target a problem-aware buyer]
- Persona: [stage + objection, in their words]
- Awareness: [Unaware / Problem-Aware / Solution-Aware / Brand-Aware]
- Proof mechanism: [transformation / testimonial / authority / comparison / …]
- Format: [1 of 7] · Production level: [lo-fi creator / graphic-style / hi-fi]

## Mechanic(s)
- Lead (★★): [mechanic] — [why, one line]
- Support (★, optional): [mechanic] — [why, one line]

## Golden nuggets mined (if CSV run)
- "[verbatim customer quote]" — defuses: [objection]
- "[verbatim customer quote]" — defuses: [objection]

## Headline variants (tagged)
- Var A — [mechanic]: "[headline]"
- Var B — [mechanic]: "[headline]"
- Var C — [mechanics]: "[headline]"
- LOCKED: Var [X]

## Supporting copy (only what the format carries)
- Sub-head / rows / price anchor: [text]
- CTA: [text, if any]
- What the IMAGE must carry: [so copy doesn't over-explain]

## 1-second test
- LOCKED headline: [PASS/FAIL] — a stranger names "[what they'd say is being sold]"

→ Hand to /dara-static-production (render) or /dara-comprehension-audit (formal test).
```

---

## Quality Gate

Score against the genius.md Static rubric + the 1-second recognition test. Retry any section below.

| Criterion | FAIL | PASS | EXCEL |
|---|---|---|---|
| **Mechanic purity** | No mechanic named, or 3+ mechanics muddying the message | Lead mechanic named; headline demonstrates it | Lead + one support amplify a single focal desire |
| **1-second comprehension** | Stranger can't name what's sold in ~1 sec | Stranger names it + feels the benefit | Names it *and* the objection is answered at a glance |
| **Sells desire, not spec** | Headline describes a feature | Headline leads with an outcome | Product is the mechanism; the desire is the headline |
| **Grounded in real language** | Invented headlines / fabricated stats | Copy tracks a real exemplar's pattern | Golden nugget mined from actual reviews carries the ad |
| **Less is more** | "This and this and this," no focal point | One clear focal message | Nothing left to cut; em dashes/misspellings gone |

**Hard stops:** any invented exemplar or fabricated stat = FAIL, rewrite against `references/static-ad-exemplars.md`. Any headline a stranger can't decode in one second = FAIL, cut it.

---

## Example Output

**Context**: My.BPM — Farrice's EDM/rave streetwear brand. Audience 22–35, festival/rave-going, identity-forward, in-culture (PLUR vernacular). ~30 SKUs, mid creative budget, ~6-figure and scaling. Currently runs standard UGC with declining ROAS. Layer 1 locked the goal (target the problem-aware buyer), persona (the raver whose fit "photographs mid by Day 3 of EDC"), and format (Transformation, lo-fi creator). A review CSV exists.

**THE DELIVERABLE:**

```markdown
# Static Copy Spec — My.BPM · Transformation (lo-fi creator)

## Strategy (locked)
- Goal: Target the problem-aware buyer (fit dies mid-festival), sell the durability/drip solution
- Persona: 22–35 raver — objection: "will it actually hold up sweat + 3 days, or fade like everything else?"
- Awareness: Problem-Aware
- Proof mechanism: Transformation (before/after wear)
- Format: Transformation · Production: lo-fi creator

## Mechanic(s)
- Lead (★★): Show the Transformation — problem-aware ravers are "just looking for proof"; show Day 1 vs Day 3, don't claim it
- Support (★): Be Specific — a number does the value math ("Day 3," "still cranking")

## Golden nuggets mined (CSV run)
- "Wore it three days at EDC, zero pilling, still looked fresh in the Sunday sets" — defuses: durability doubt
- "The only fit that didn't feel like wet cardboard by the last drop" — defuses: sweat/fade doubt

## Headline variants (tagged)
- Var A — Show the Transformation: "Day 1 vs. Day 3 of EDC" (over a before/after split)
- Var B — Borrow From Customers (nugget as headline): "Still cranking on the Sunday sets."
- Var C — Show + Be Specific: "Day 3. Zero pilling. Still cranking." (over the split)
- LOCKED: Var C

## Supporting copy (only what the format carries)
- Sub-head: "Sweat it. Sleep in it. Rage in it. It holds."
- CTA: "Shop the festival line"
- What the IMAGE must carry: split frame — same tee Day 1 (crisp) vs Day 3 (still crisp), creator holding the tag/piece to camera; PLUR-coded styling
```

**1-second test:** PASS — a stranger glances and names "streetwear that survives a festival." The before/after carries the proof; the copy just puts a number on it.

**What elevates this**: the headline sells a proof-of-durability desire, not a fabric spec. The golden nugget ("still cranking") came from an actual review, not a copywriter's imagination — which is exactly Mechanic 7. Two mechanics, one focal message, no em dash, nothing left to cut. It's a Transformation static a problem-aware raver decodes before the thumb moves.

---

## Render Handoff (optional)

This is a copy spec, not a rendered asset. If you want to see it as a shippable static, hand the locked spec to **`/dara-static-production`** — it takes the copy spec + format + production level into the brand-brain → research-first → 3-variation batch → edit-to-refine pipeline (tool-agnostic: fantastic-posters, Higgsfield, or GPT-Image). For the formal stranger test on the finished ad, run **`/dara-comprehension-audit`**. To spin the same copy into a video variant, run **`/dara-format-swap`**.
