# Demand Engineering — Parallax ICP Intelligence™

**Premise (Priestley):** Capacity × 50 = required monthly aware prospects. Scarcity is legitimate only when capacity is legitimate. Fake urgency is rejected on sight by Avatar 02 and Avatar 03 (both explicitly allergic to "only 3 spots left" theater).

**Premise (Monk.Ai):** Demand and supply are one system. When demand outpaces supply, raise price or add cohort structure. When supply outpaces demand, close the waitlist and invest in signal volume. Do not discount to force demand — it breaks trust gradient.

---

## CAPACITY MATH (Farrice, solo, current state)

### Per-tier time cost

| Tier | Farrice hours per engagement | Max concurrent |
|---|---|---|
| Crystal ($1,497, 7 days) | ~6 hours (3 calls + 2 hours judgment pass + 1 hour finalize) | 4 |
| Architecture ($2,997, 14 days) | ~11 hours (4 calls + 5 hours judgment + 2 hours finalize) | 2 |
| Launch ($4,997, 21 days) | ~20 hours (6 calls + 10 hours voice-pass + 4 hours finalize) | 1 |

### Monthly capacity limits (solo Farrice, with 2-day buffer between engagements)

| Configuration | Monthly revenue |
|---|---|
| 4 Crystals + 2 Architectures + 1 Launch | 4×$1,497 + 2×$2,997 + 1×$4,997 = **$16,979** |
| 8 Crystals only | $11,976 |
| 3 Architectures + 1 Launch | $13,988 |
| 2 Launches + 2 Crystals | $12,988 |

**Sustainable operating point:** ~$12K-$17K/month solo. This is the realistic ceiling with current capacity.

### Required signal volume (Priestley's 50x rule)

- Crystal conversion target: 4/month → 200 aware prospects/month required
- Architecture: 2/month → 100 aware prospects/month required
- Launch: 1/month → 50 aware prospects/month required

**Aggregate:** ~350 aware prospects/month across all tiers to run at full capacity.

This is WS4's North Star metric. Awareness, not "leads." Someone who's seen Farrice's work twice and knows Parallax exists.

---

## BATCH CADENCE

**Not continuous intake. Monthly cohorts.**

### The rhythm

- **Intake window:** Day 1-7 of each month (application form open, ICP Tell calls scheduled)
- **Delivery window:** Day 8-end of month (engagements active)
- **Close window:** Last 3 days of each month (intake closed, applications roll to next month)

### Why batched (not continuous)

Three reasons:
1. **Farrice capacity protection** — running 4 Crystals simultaneously beats running them staggered. Same synthesis sprint can serve multiple clients when batched.
2. **Demand clarity** — monthly cohorts let waitlist numbers create real (not fake) scarcity. When November's cohort fills in Week 1, December's waitlist is provably tighter.
3. **Content rhythm** — a month-end "cohort closing Friday" is a legitimate posting hook. Continuous intake has no rhythm.

### What if someone wants to start mid-month?

They go on the next month's list. Exceptions only for Avatar 03 Launch engagements with a hard external deadline (grant application, scheduled product drop) — and that's priced at the premium tier anyway.

---

## WAITLIST MECHANICS

### What waitlist members get

**Automatically:**
1. First-access to next month's intake window (48-hour head start before public opens)
2. Monthly "field notes from the cohort" — 500-word note from Farrice about what he noticed in that month's engagements (no client names, pattern-level)
3. The ICP Tell call booking link, always open (free diagnosis is not capacity-bound)

### What waitlist members DO NOT get

- No email nurture sequences
- No "3 reasons you should buy now" drip
- No retargeting pixel drama
- No free PDF downloads disguised as lead magnets

The waitlist is an invitation to a small thing, not a gauntlet of pre-sales.

### Waitlist triggers

- Missed the current month's intake window
- Not yet ready (e.g., under 1,000 subscribers)
- Wants Launch tier but Farrice is at Launch capacity
- "Just curious" — put them on waitlist, send monthly notes, let the notes convert

### Signal that waitlist is working

When 40%+ of Crystal buyers came from the waitlist (not from first-touch cold traffic), the system is working. It means awareness is converting to qualified patience instead of high-friction closes.

---

## HONEST SCARCITY LANGUAGE

### Language to use (truthful, anchored in capacity)

- "We take 4 Crystals per month. November is closed. December opens [date]." (Factual.)
- "Launch tier accepts 1 engagement/month. Current available month: [month]." (Factual.)
- "Waitlist currently: 23 people. [Month]'s cohort: 4 spots remaining." (Verifiable.)
- "Farrice is the one running every engagement. That's why the number is small." (The honesty about WHY scarcity exists is itself a trust signal.)

### Language to never use

- "Only 3 spots left!" (without context, reads as theater)
- "This offer ends at midnight!" (false urgency)
- "This won't be available at this price for long!" (desperation)
- "Thousands of writers have already..." (fake social proof)
- Scarcity emojis (🔥, ⏰, ⚡) in any context

### The "why we're not always available" page

A small page on the website titled something like **"Why Parallax is capacity-limited."** Three paragraphs, Farrice's voice, explaining:
1. Every engagement is run by Farrice personally (no junior operators)
2. Judgment at specific checkpoints is non-delegatable
3. Taking more would degrade the work. Taking less would be underused capacity.

This page converts skeptics. It's the opposite of a sales page — and that's precisely why it sells.

---

## WHAT HAPPENS AT CAPACITY (and how to know you're there)

### Signals you've hit capacity

1. Three consecutive cohorts fill within the 7-day intake window
2. Waitlist has 30+ people
3. Farrice is working past 55 hours/week on engagements (not content, not admin)
4. Quality scores from chain_runner.py finalize start dropping into 7s when they were 8-9s

### Sequential response protocol

**Stage 1: Raise prices.**
The first lever is price, not capacity. When demand is provably outpacing supply, raise Crystal from $1,497 to $1,997. Architecture from $2,997 to $3,997. Launch from $4,997 to $6,997. This prices for the trust-gradient inflation that comes with a filling waitlist.

**When to trigger:** After the SECOND consecutive cohort sells out in under 5 days, or when the waitlist passes 25.

**Stage 2: Add a higher tier.**
At sustained demand, add Parallax Cohort or Parallax Retainer tiers ABOVE Launch — group-based programs at $7,500+ or ongoing retainers at $2,500/month. This absorbs demand that can't be served at Launch capacity.

**When to trigger:** When the waitlist contains 10+ Launch-qualified prospects willing to wait 60+ days.

**Stage 3: Staff the delivery.**
Train a second operator to run Tier 1 (Crystal) under Farrice's supervision. Farrice's judgment checkpoints (from delivery-spec.md) remain with Farrice. Synthesis, intake, drafting can be delegated. The 9 non-delegatable moments remain with Farrice.

**When to trigger:** When raising prices and adding tiers still leaves a 60-day waitlist. Not before.

**Stage 4: Close the list.**
When capacity + price + added-tiers still produce more demand than supply, the correct move is close the list for 90 days. Publicly. Farrice announces "Parallax intake closed until [month]." This is the most powerful scarcity signal available — and it's only legitimate when it's literally true.

### What NEVER to do

- Offshore delivery
- White-label to a second "Parallax operator" without Farrice judgment
- Create a "lite" tier to serve the overflow
- Accept engagements you can't personally deliver

Each of these breaks the trust gradient that makes the premium pricing work.

---

## SIGNAL VOLUME ENGINEERING (ties to WS4)

### The math flips WS4's strategy

If Parallax needs 350 aware prospects/month and current awareness is (estimate) 20-50/month via Farrice's network:
- **Month 1:** Ship to network. 30-50 awareness. 2-3 Crystal sales possible ($3K-$5K).
- **Month 2:** Ship cold content (HVC case study, Josh case study) to Substack Notes + LinkedIn. Awareness grows to 80-150. 3-5 Crystals + 1 Architecture possible ($7K-$10K).
- **Month 3:** Substack growth + 1-2 guest posts in Avatar 02 territory. Awareness grows to 200-350. 4-6 Crystals + 1-2 Architectures + 0-1 Launch possible ($12K-$17K).

**Awareness-to-revenue lag is ~45 days.** The content shipped in Month 1 converts in Month 2-3.

### WS4 should track (per week, not per post)

- Unique net-new followers on Substack Notes / LinkedIn: target 50/week by Month 2
- ICP Tell applications submitted: target 10/week by Month 2
- ICP Tell calls booked: target 5/week by Month 2
- Tier 1 closes: target 1-2/week by Month 3

If these numbers hold, capacity fills in Month 3 and Stage 1 price-raise triggers around Month 5.

---

## THE BATCH CADENCE AS PRODUCT FEATURE

Final non-obvious frame: the monthly cadence IS part of the product.

Most "done-with-you" services compete on being always-available. Parallax competes on being rhythmically-available. The monthly cohort creates:

1. A natural anchor for Farrice's own content ("November cohort closing Friday")
2. A legible finish line for buyers ("I'm in the December cohort")
3. Shared experience across cohort members (pattern-level, no client sharing)
4. Predictable revenue ($12K-$17K/month ceiling forces product evolution, not just capacity expansion)

The rhythm is the product. It's also the signal that Farrice runs a practice, not a hustle.
