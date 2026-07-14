---
name: book-doctor
description: Diagnostic audit for a stalled or underperforming KDP book (own or competitor) — runs the 8-mistake checklist as a triage instrument, reads ad data to localize the funnel leak, out-products it against page-one incumbents, and returns a ranked defect list, fix sequence, and a reposition-vs-push verdict.
expert: Sean Dollwet
load_context: genius.md + references/prompt-chain.md + references/price-sheet.md
---

# Book Doctor — Stalled-Book Diagnostic Audit

## Pre-Flight Gate

Run this when a book is **live but underperforming** — publishing before the launch honeymoon closes, sales flat after 30 days, ads spending with nothing back, or a competitor teardown to find where to attack. This is a diagnosis, not a rebuild.

Do NOT run this when:
- The topic was never validated (no 3+ books under 80,000 BSR, paperback). That is not a stalled book, it is a dead-demand book — the fix lives in `01-validate-book-topic`, and pouring diagnostics at it violates **Anti-Pattern: write-first-validate-never**. Book Doctor's very first test (below) catches this.
- The book has zero reviews and has never been marketed. That is not "stalled," it is an un-launched book — route to `03-launch-and-multiply`. Marketing before the 15-review gate is the mistake, not the symptom.
- The book has fewer than ~30 days live. Do not diagnose a book still inside its 30-day honeymoon; let velocity data accumulate first (Pattern 13).

Governing frame (genius Pattern 2): **"It's not the topic, it's the book."** Relocate every failure from demand (uncontrollable) to a nameable, controllable listing defect — cover, title, reviews, content, or price. If a defect can't be named, you haven't finished diagnosing.

## Skill Acquisition

Load, in order:
1. `genius.md` — Patterns 2, 4, 12, 14 (ads-as-diagnostic), 15 (price-vs-conveyed-value); Hidden Insight 3 (doubled price = doubled conveyance), 11 (26-review signal); Exemplar A (Money Tree vs Money Skills), E (decluttering BSR cliff); the Quality Rubric and Anti-Pattern kill list.
2. `references/prompt-chain.md` — the title taste-test rubric and the TOC-stalking / review-mining method (used to compare against incumbents).
3. `references/price-sheet.md` — BSR→revenue benchmarks (80k ≈ $500/mo), launch pricing, cover/formatting outsource floors (for the fix sequence).

## Execution

### Step 1 — The ranking-without-sales red-flag test (run first, it can end the audit)
Search the book's **primary keyword** on Amazon (category = Books, paperback). Read where the book ranks:
- **Ranks #1–2 for its own keyword and still isn't selling** → the topic failed proof-of-concept. Nobody searches or buys this concept; being first in an empty niche is *why* it was empty. **Verdict: REPOSITION, not push.** Marketing dead demand wastes money. Kick to `01-validate-book-topic` to find a proven adjacent keyword. Stop the audit here — no listing fix rescues absent demand.
- **Ranks poorly against page-one books that ARE selling** (3+ competitors under 80,000 BSR present) → demand is real, this is an execution defect. Proceed to Step 2.

### Step 2 — Run the 8-mistake checklist as a diagnostic instrument
For each mistake, log the detection signal if present, then the counter-move. Every mistake firing = one line in the ranked defect list.

| # | Mistake | Detection signal | Counter-move |
|---|---------|------------------|--------------|
| 1 | Action, not iteration | One rushed book, still consuming tutorials | Ship + improve; this book is data, not a verdict |
| 2 | Wrote the book *they* wanted | 3+ months on a passion topic, never checked demand | Validate — DS Amazon Quick View, 3+ books < 80,000 BSR (paperback) |
| 3 | Fancy title, no keyword | Clever/abstract title; low impressions; blank data dashes | Exact buyer phrase in title; keywords to subtitle; sell with the rest |
| 4 | AI paste, not elevate | AI-cover artifacts, ChatGPT-flat interior, "feels made up" reviews | Right tool per stage; humanize + fact-check; deliver transformation, not information |
| 5 | Volume over quality | Large catalog, poor covers, zero reviews, "rank not found" | Small catalog of professional books; let reviews compound |
| 6 | Cheap/DIY cover | Loses a side-by-side line-up; low clicks despite impressions | Outsource $10–$20+ or generate a pro cover that *stands out* (never clone) |
| 7 | No review plan (wasted honeymoon) | Upload-and-pray; <10 reviews month one; velocity stalls at 30 days | 15+ reviews (acquaintances, niche groups, Book Bounty/Reverb) + $3–5/day ads + $0.99 / $5.99–6.99 launch pricing |
| 8 | Not investing in guidance | Tutorial-hopping, contradictory mental models, no progress | Structured course; coach who sees the actual books; don't over-invest pre-first-dollar |

### Step 3 — Read the ads data to localize the leak (Pattern 14)
If a $3–5/day campaign has run, read impressions vs clicks vs sales — the funnel leaks at exactly one place:
- **High impressions, low/no clicks** → the buyer sees the ad and scrolls past. Defect is **cover, title, or review count** (the three things visible before the click). The cover fails the snap-test, or the title lacks the searched keyword, or the review pile is thin. Fix these before spending another dollar.
- **Clicks but no sales** → the buyer clicks in and bounces. Defect is on the product page: **Look Inside preview** (weak opening, AI-flat interior), **price** (above category norm without conveyed value), or **reviews** (too few to clear the trust threshold). Fix the page.
- **Converting profitably** → not a defect, a scaling opportunity. Raise budget *only* from a profitable baseline (Pattern 14). No fix needed; the problem was budget, not the book.
- **No ads have run** → prescribe the $3–5/day diagnostic campaign as the first fix-action; you cannot localize the leak blind.

### Step 4 — Out-product audit against page-one incumbents
Line the book up beside the 3+ page-one competitors and score it defect-by-defect on the buyer's actual decision path (**cover → title → Look Inside → reviews → price**):
- **Cover modernity** — does it lose the 3-second snap-test line-up? Text-forward covers now beat realistic-image covers in self-help; a cover "designed in 2002" is a weak spot even at 3,000 reviews (window-thesis Door B).
- **Title keyword match** — does the exact searched phrase appear verbatim? A keyword-less title is the Money Tree failure ($0 vs $45/day on the identical topic — Exemplar A).
- **Subtitle benefit density** — does the subtitle stack 3–4 concrete, pain-sourced benefits with a number, or is it empty free selling space? A missing subtitle is forfeited conversion.
- **Review count vs quality** — count is only a moat when cover/title/content are also strong (Pattern 12). A weak-but-reviewed incumbent is beatable; an incumbent with only ~26–300 reviews is a green-flag opening, not a wall.
- **Content freshness** — is the interior stale, thin, or raw-AI (unbroken ChatGPT prose, no stories)? Content that hasn't been touched in years is Door B.
- **Price vs conveyed value** — the load-bearing insight: **a doubled price demands doubled *conveyed* value.** If the book is priced above the category norm while showing the same-looking cover, fewer reviews, and a comparable subtitle, it simply won't sell. Either the listing must *visibly* justify the premium (stronger cover, denser subtitle, more reviews than page-one peers) or the price must drop to launch levels ($0.99 ebook / $5.99–6.99 paperback) to harvest proof first.

### Step 5 — Verdict
Assemble: **ranked defect list** (worst first, each tied to its detection signal) → **fix sequence** (cheapest-highest-leverage first; cover/title clicks precede price and content) → **reposition-vs-push decision** (Step 1's dead-demand verdict overrides everything; otherwise push with the fix sequence).

## Content Type Adaptations

| Type | Adaptation |
|------|------------|
| High-content (nonfiction/fiction) | Full audit; content-freshness and Look-Inside quality carry heavy weight (interior is the click-to-sale defect). Fix sequence can include a humanize/re-edit pass on stale AI chapters. |
| Low-content (journals/planners) | Content-freshness test collapses to cover + interior-design + review count; there's no prose to re-edit. Snap-test cover and title keyword do the heavy lifting; price ceiling is tight ($9.99 band). |
| Medium-content (workbooks, prompt books) | Weight the subtitle benefit-density and Look-Inside preview; buyers pay for perceived organization, so the price-vs-conveyed-value test is decisive. |
| Sprint vs standard | Sprint: run Steps 1, 3, 4 only, deliver the top 3 defects + one fix each. Standard: full 8-mistake pass + complete out-product scorecard + fix sequence. |

## Output Requirements

Deliver:
1. **Red-flag verdict** (Step 1): reposition or diagnose, with the keyword-rank evidence.
2. **Ranked defect list** — each defect: name · detection signal observed · which of the 8 mistakes / audit dimensions it maps to.
3. **Ads-leak reading** (if data exists) — impressions/clicks/sales classification and the localized fix.
4. **Out-product scorecard** — this book vs 3+ incumbents across cover / title / subtitle / reviews / content / price, with the specific weak spot per incumbent named.
5. **Fix sequence** — ordered, cheapest-highest-leverage first, each priced from `references/price-sheet.md`, each a time-or-money lane.
6. **Reposition-vs-push decision** with the reasoning trail.

No fabricated BSR, revenue, or review numbers — flag any data the user didn't supply as unverified.

Execution prompt: references/prompts-v2/book-doctor-report.md

## Quality Gate

- [ ] Step 1 ranking-without-sales test run before any listing fix is prescribed (Rubric 7, sequencing).
- [ ] Every named defect traces to a detection signal, not a hunch (Pattern 2 — failure relocated to a controllable cause).
- [ ] Ads data read as diagnostic first; scaling recommended only from a profitable baseline (Rubric — no aggressive-budget default; Anti-Pattern: scaling an unprofitable book).
- [ ] Out-product scorecard names each incumbent's specific weak spot (Rubric 9, attack-surface named).
- [ ] Price-vs-conveyed-value tested — no premium price passes without visibly conveyed extra value (Insight 3).
- [ ] Title checked for verbatim keyword + decode-in-one-read; any artsy/keyword-less title flagged (Rubric 4, Anti-Pattern: artsy titles).
- [ ] Verdict names reposition-vs-push explicitly; dead-demand overrides push (Anti-Pattern: marketing dead demand).
- [ ] No fabricated numbers; unverified data labeled (Rubric — no phantom figures).
