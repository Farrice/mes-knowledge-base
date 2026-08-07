# Delivery Blueprint: Claim-Safe AEO Ladder, Solo, 1-3 Hrs/Day

Scope line for every deliverable: *marketing-side claim hygiene, not legal advice.* No paid AEO monitoring tools at pilot pricing: citation checks run off a manual spreadsheet, not Otterly/Scrunch-class tools.

---

## Rung 1: Claim-Safe Citation Audit ($500 pilot, 3 slots, 5-business-day turnaround)

**Inputs from client (3 fields, DM or short form, no logins, no analytics access):**
1. Site URL: homepage + one product page they most want to win on.
2. Category, one line ("magnesium glycinate for sleep, sold to stressed 30-45 professionals").
3. One named competitor URL.

**Claim-classification pass**: run `claim-safe-health-marketing` workflows in order:
- `/claim-audit` on up to 8 claims pulled verbatim from the two pages → sorts each into the 5-bucket risk taxonomy (GP-01). Bucket 1/2 (disease express/implied) is a hard stop, flagged not fixed.
- `/claim-substantiation-map` (GP-02) on the same set → claim strength vs. evidence tier actually shown, ingredient evidence not silently counted as product evidence.
- Every finding labeled VERIFIED / LIKELY / `[VERIFY LIVE]`. Nothing asserted from memory.

**Manual AI-citation-check cadence (spreadsheet SOP, no paid tools):**
- Build the money-query set at intake: 6 buyer questions in 3 shapes (category / comparison / decision).
- One Google Sheet, columns: `Date | Engine | Query | Brand Named (Y/N) | Domains Cited | Notes`.
- Check ChatGPT, Perplexity, Google AI Overview: 3 engines × 6 queries = 18 rows, one pass each, ~35-40 min total including logging.
- This is a single snapshot for the audit (not the weekly cadence; that starts at the retainer). State plainly in the deliverable that one pass is directional, not proof of a trend.

**Deliverable template outline** (reuse `_active/linkedin/02-offer/claim-safe-citation-audit-TEMPLATE.md` as the fulfillment script; do not rebuild it):
1-page scorecard (5 scored sections /10, composite /50) → AI-Citation Visibility → Claim-Safety Map → Proof-Carry Gap → Sameness/Angle Gap → Divergence + Named Position. Guardrail paragraph restated verbatim on every audit. Ends with the retainer bridge line, never a hard pitch.

**Hours budget (target ≈6 hrs across 5 days, ~1-1.2 hr/day):**

| Task | Hrs |
|---|---|
| Intake review + claim inventory pull | 0.5 |
| `/claim-audit` (up to 8 claims) | 1.5 |
| `/claim-substantiation-map` | 1.0 |
| Manual 3-engine citation snapshot | 1.0 |
| Proof-carry + sameness read | 1.0 |
| Divergence angles + scorecard writeup | 1.0 |

Effective rate ≈$83/hr. That is deliberately thin: the audit is priced as the door-opener into the sprint, not a profit center. If it runs past 8 hrs on any single client, stop and ship what's scored; do not chase completeness.

---

## Rung 2: Trust-Layer Install Sprint ($2,000-2,500 pilot / $3,500 standard, 2 weeks / 10 business days)

**Scope fence (state in the SOW):**
- In: rewrite up to 15-20 claims to compliant-but-converting language, one claim-safe hooks batch (10-15 hooks), one proof-carry structuring checklist (entity authority + off-site seeding *recommendations*, not execution), before/after citation snapshot, 2 revision rounds.
- Out: paid ad management, full website rebuild, ongoing monitoring (that's the retainer), legal signoff of any kind, more than 2 revision rounds without a change order.
- One sprint active at a time. A second client waits for a start date; never run two sprints concurrently at pilot stage.

**Day-by-day plan (engines named per task):**

| Days | Work | Engine/skill |
|---|---|---|
| 1-2 | Kickoff, expand claim inventory to 15-20, full substantiation map | `claim-safe-health-marketing` `/claim-audit` + `/claim-substantiation-map` |
| 3-4 | Compliant rewrite pass on flagged claims; dry-run pre-launch gate | `/compliant-rewrite`, `/pre-launch-compliance-gate` |
| 5-6 | Claim-safe hooks for top 3 buyer-question angles; expand into landing/social copy | `/claim-safe-hooks` → `/copy-engine` |
| 7 | Proof-carry structuring recs (entity authority, off-site seeding plan) | manual, informed by audit's Section 3 findings |
| 8 | Client review checkpoint: send draft package | – |
| 9 | Revisions (round 1, built into price) | – |
| 10 | Final delivery: updated scorecard, before/after citation snapshot, handoff doc, retainer bridge | – |

**Hours budget:** ~15-18 hrs over 10 days (1.5-1.8 hr/day, inside the 1-3 hr window). Effective rate ≈$130-165/hr at pilot pricing.

---

## Rung 3: GEO Authority Retainer ($2,500-3,500/mo pilot, escalates only after a shipped case study)

**Monthly cadence:** 8-12 founder posts + claim-safe copy assets, delivered in one batch mid-month; 2 revision rounds built in; a monthly citation-trend report rolled up from the weekly spreadsheet log (not a new tool; same 3-engine × money-query sheet, now run weekly instead of once).

**Weekly citation cadence:** narrow to the 3-4 highest-commercial-intent money-queries (not the full 6) × 3 engines = 9-12 checks/week, ~20-25 min. Log feeds the monthly trend line client sees.

**Queue rules:** one active onboarding/sprint at a time; retainer delivery batches are staggered across active clients, never stacked on the same week.

**Client-approval loop:** batch sent by a fixed day each month → client has 5 business days to mark up → one revision round → ship. Anything beyond round 2 in a month is billed as an add-on, not absorbed.

**Capacity cap (name the number):** **2 concurrent retainer clients at pilot pricing.** This is not a guess: it's the ceiling the refuter review named directly, a solo operator running two specialist workstreams (claims-literate content + multi-engine citation tracking) monthly, on 1-3 hrs/day, erodes past 2-3 clients. Cap at 2 until a case study exists to justify hiring/contracting help.

**Price response at the cap:** a 3rd prospect does not get a waitlist promise; it gets a price quote at standard, not pilot ($4,000-6,000/mo), positioned as "the next open slot is priced at standard." That price increase is the queue-management mechanism, not a sales tactic bolted on after the fact.

---

## Flag-for-Counsel Escalation Path (every rung)

Any claim landing in Bucket 1 or 2 of the risk taxonomy (disease express/implied), or failing the two-experts test (GP-08: would a regulatory attorney and a DR copywriter both sign off unchanged?), gets a standing note in the deliverable: *"This claim is flagged for your counsel's review before it ships; it is outside what a marketing-side audit can clear."* Farrice never rewrites a Bucket 1/2 claim into a "safer" version and calls it cleared. The rewrite offered, if any, is the fallback claim once counsel confirms the original is off the table, never a substitute for that confirmation.
