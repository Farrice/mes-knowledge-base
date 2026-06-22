# Worked Exemplar — Customer Truth Map: First-Time Homebuyers (for Jen Santulan)

> **This is a REAL map built from real, verified customer language**, not an illustration. It was
> produced by a live smoke-test run of this skill on 2026-06-21 to prove the wiring end-to-end.
> Every quote below was scraped from public Reddit via `apify_client.py` and passed the deterministic
> Verbatim-Integrity gate (`execution/ctm_verbatim_check.py`) against the raw corpus — **18/18 real
> quotes verified; a planted fabrication was caught and rejected.** Scope is intentionally small (a
> smoke test, not a full map): 2 sources, ~65 signal lines, total cost **$0.065**. A production map
> would mine more communities + Jen's own call/DM data and run `/ctm-triangulate` across all of them.

**Audience (narrowed):** first-time homebuyers, working/lower-middle income, buying at the edge of
affordability (the "we can make ends meet but it's a stretch" buyer). Jen's FTHB lead engine ICP.
**Sources:** `r/FirstTimeHomeBuyer` (subreddit pull, 40 items) + a `reddit:"first time home buyer
overwhelmed"` keyword pull (25 items). **Method:** `/ctm-gather` (Apify) → `/ctm-clean` (verbatim
gate) → `/ctm-map` → `/ctm-jobs` → `/ctm-gaps` → put-to-work.

## Change Log (model the freshness discipline)
- **2026-06-21** — Initial smoke-test build. 2 Reddit sources, 18 verified quotes. Dominant signal:
  *post-close cost shock* + *approval-vs-affordability confusion* + *emotional whiplash (excited →
  defeated)*. Next refresh: add Jen's own discovery-call language + a local SFV/LA source, then
  triangulate.

---

## The Map

### SAY (stated directly)
- *"This would be our first time buying a house, so any insight is appreciated!"* — [r/FirstTimeHomeBuyer]
- *"Anyone else who's been through this or something similar, how did you handle the stress?"* — [r/FirstTimeHomeBuyer]

### THINK (implied, not said)
- That the lender's approval number *is* what they can afford — surfaced by the corrective reply
  *"not necessarily the maximum amount the lender will approve you for."* — [r/FirstTimeHomeBuyer]
  (the belief is visible in the confusion the reply is correcting).
- That a paid inspection protects them from big surprises — held right up until *"The home was a flip,
  so we knew it could have some lurking issues."* — [reddit overwhelmed] became a $20K reality.

### FEEL (emotions)
- Hope → *"My fiance (28M) and I (28F) were so excited to be homeowners."* — [reddit overwhelmed]
- Betrayal → *"My fiancé and I feel so taken advantage of and defeated."* — [reddit overwhelmed]
- Resentment → *"I can't help but feel resentful for this purchase as a new homeowner."* — [reddit overwhelmed]
- Financial strain → *"We can make ends meet to afford it but it's a strettttch."* — [reddit overwhelmed]
- Stress, seeking reassurance → *"…how did you handle the stress?"* — [r/FirstTimeHomeBuyer]

### DO (actions + ⚠ workarounds)
- ⚠ **WORKAROUND** — DIY savings routine: *"about $5k saved and adding 10% of each paycheck every pay
  day"* — [r/FirstTimeHomeBuyer]
- ⚠ **WORKAROUND** — distrust-driven quote-shopping: *"the overwhelming advice was to get multiple
  opinions, which we are pursuing."* — [reddit overwhelmed]
- Community advice they act on: *"you should call a few mortgage brokers/lenders and see what they
  say."* + *"I recommend getting your debt paid off before buying."* — [r/FirstTimeHomeBuyer]
- Bought despite a known risk → *"We close on the house and within two days, the AC stops cooling."* — [reddit overwhelmed]

### PAINS
- Post-close cost shock → *"we would be hit with another 20K to replace the entire AC system that was
  otherwise working prior to close."* — [reddit overwhelmed]
- Ongoing-cost surprise → *"the maintenance costs have been a surprise for me."* + *"Just keep in mind
  that maintenance costs don't scale to the price of the house."* — [r/FirstTimeHomeBuyer]
- Affordability at the edge → *"…it's a strettttch."* — [reddit overwhelmed]

### GAINS (wished-for outcomes)
- Relief / stability → *"It will be a huge stress reliever once you get into a home of your own."* — [r/FirstTimeHomeBuyer]
- The identity win → *"…so excited to be homeowners."* — [reddit overwhelmed]

### Patterns (named)
1. **The week-one money shock** (repeated, vivid) — the gap between "we made it to closing" and "now we
   owe thousands we didn't plan for." Strongest, most emotional pattern.
2. **Approval ≠ affordability** — buyers conflate the lender's max with what's safe to spend.
3. **Emotional whiplash** — excitement → defeated/resentful; buying is a *stress event*, and they
   crowdsource emotional reassurance from strangers.
4. **Trust deficit** — "get multiple opinions," distrust of a single inspector/quote.

---

## Jobs-to-be-Done (pains reframed)
- **True cost of ownership.** *When I'm budgeting for my first home, I want to know the real ongoing
  cost of owning it (not just the mortgage), so I can buy without a post-close money shock.*
- **Inspection trust on older/flip homes.** *When I'm closing on an older or flipped home, I want to
  trust that the inspection actually surfaces the expensive failures, so I'm not blindsided in week
  one.*
- **Safe affordability.** *When a lender approves me for an amount, I want to know what I can actually
  afford safely, so I shop in a range that won't strap me.*

## Gap Table (widest first → the shortlist)
| Pain / Job | Current Fix | The Gap | Width |
|---|---|---|---|
| True cost of ownership | budgeting calculators, generic "save for maintenance" advice | calculators give a target %, never the real line items → "surprise" is the norm | **5** |
| Inspection trust (older/flip) | standard inspection + extra paid inspections | inspection is "visual only," still missed a $20K AC failure → buyer feels duped | **5** |
| Approval vs. safe affordability | the lender's max number | buyers can't separate max-approved from safe-spend → strain | **4** |
| Process stress / overwhelm | asking strangers "how did you handle the stress?" | no trusted guide → emotional reassurance crowdsourced from a subreddit | **4** |

**Shortlist (lead with these):** the *week-one money shock* and *inspection trust* gaps — both score 5
and carry the most vivid, repeated, emotional language.

---

## Put the Map to Work (for Jen, a realtor) — all grounded in real quotes
**Copy — headline candidates** (from FEEL + PAINS, customer's register):
- "Know what you can actually afford — not just what the bank approves." *(grounded: "not necessarily
  the maximum amount the lender will approve you for")*
- "The cost no one warns first-time buyers about — and it's not the down payment." *(grounded:
  "maintenance costs have been a surprise")*

**Content idea** (grounded, one quote attached):
- *"The week-one money shock: why your inspection won't catch the $20K problem — and the 3 questions to
  ask before you waive anything."* — built on *"…hit with another 20K to replace the entire AC system…"*

**Positioning angle for Jen** (targets the widest gap):
- *"I map your true cost of ownership before you fall in love with a house — so closing day isn't the
  start of a money surprise."* (One sentence that makes the buyer feel understood.)

**Offer extension** (tied to a real gap):
- A **"First 90 Days" cost map + vetted inspector/HVAC shortlist** — directly answers the *surprise
  cost* + *trust deficit* gaps. Simple to add; high felt-value for this exact ICP.

## Triangulation note (Phase 6, 2 sources)
- **CONSISTENT TRUTH (high-confidence):** the post-close cost shock + the stress/overwhelm of the
  process appear in *both* sources → build core messaging here.
- **SOURCE-SPECIFIC (hold looser):** the flip-home / inspection-betrayal narrative was strongest in the
  "overwhelmed" keyword pull → powerful for that sub-segment, lower-confidence as a universal claim
  until confirmed in more sources.

---
*Provenance: `apify_client.py reddit` (2 pulls, $0.065), cleaned + verified via
`ctm_verbatim_check.py` (18/18 verbatim, 1 fabrication rejected). Raw corpus retained at
`.tmp/ctm-fthb/` for this run. This is a demonstration-scale map; run `/customer-truth-map BUILD` with
Jen's own call/DM data + a local source for a production map.*
