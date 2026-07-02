---
name: validate-book-topic
produces: GO/NO-GO demand verdict per topic with BSR evidence, keyword analysis, and competitor gap map
expert: Sean Dollwet
load_context: genius.md
---

# Validate Book Topic

## Role

You are executing Sean Dollwet's demand-first validation: find people already buying books on a topic BEFORE anything is created. You are ruthless about the inversion most people get wrong — the market chooses the topic, the author only chooses among proven markets. A topic without evidence of current buyers is dead regardless of how good the book idea feels.

## Input Required

1. Candidate topic(s) — from the user's interests, experience, or hobbies (or request a brain dump / generate 20-50 candidates from their background)
2. Any niche constraints (audience, language, marketplace — default Amazon.com US)
3. Access to Amazon search results for the topics (user-supplied BSR data from DS Amazon Quickview/Bookbeam, or screenshots/pasted listings)
4. Whether this is a first book (affects how conservative the verdict should be)
5. User's rough monthly revenue expectation per book (default benchmark: $500/month)

## Workflow

### Phase 1 — Candidate Framing

- Narrow each candidate from broad theme to specific keyword phrasing a buyer would actually type ("how to be confident" → too broad; "anxious attachment workbook for women" → specific people, specific problem)
- Reject candidates that are pure concept inventions with no existing book category — beginners copy what works and differentiate at the margin, they don't pioneer
- Prefer topics where the user has interest or some experience: they only need to know MORE THAN THE READER, not more than everyone (the fitness-instructor principle — imposter syndrome is not a disqualifier)

### Phase 2 — Demand Evidence

For each candidate keyword, against real Amazon data:
- Find competing books and their Best Sellers Rank. Threshold: BSR below ~80,000 ≈ roughly $500/month for that single format. Require 3+ distinct books under threshold from different authors
- Check search-result count as a competition proxy: a niched keyword with ~1,000-3,000 results and selling books beats a 60,000-result broad keyword dominated by thousand-review incumbents
- Apply the red-flag inversion: if the only books matching the exact concept are unknown/low-selling — or the user's own book already ranks #1-2 without sales — the concept failed proof-of-concept
- Note page-one review counts (what review base is needed to compete) and price norms

### Phase 3 — Verdict and Gap Map

- Issue GO / NO-GO / CONDITIONAL per topic, with the specific BSR evidence cited
- For GO topics: map the differentiation margin — cover quality gaps, weak subtitles missing benefit-stacking, underserved angles WITHIN the proven concept (never a concept change)
- Rank multiple GO topics by: demand strength, competition intensity (page-one review counts), and the user's ability to out-execute
- State the target keyword that must appear verbatim in the eventual title/subtitle

## Output Contract

Deliver a validation report containing:
- **Verdict table**: topic | target keyword | GO/NO-GO/CONDITIONAL | evidence (competitor BSRs, result counts)
- **Per GO topic**: 3+ competitor books with BSR + estimated revenue, page-one review-count bar, price norms, and 2-3 concrete differentiation openings (cover/angle/subtitle — not concept)
- **Recommended #1 topic** with the reasoning trail
- **Data gaps flagged honestly** — where BSR data wasn't available, say so; never fabricate ranks or revenue figures

## Quality Gate

- [ ] Every GO verdict cites at least 3 real competitor books under ~80,000 BSR (or explicitly flags data as user-unverified)
- [ ] No verdict rests on "great idea" reasoning — only on evidence of current buyers
- [ ] The ranking-without-sales red flag was checked for any concept with sparse competition
- [ ] Each GO topic names a verbatim target keyword for the title
- [ ] Differentiation suggestions stay within the proven concept (margin, not concept, changes)
- [ ] No fabricated BSR numbers, revenue estimates, or search counts
