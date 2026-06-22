---
description: Phase 4 Step 2 engine — build the gap table (Pain/Job → Current Fix → The Gap → Gap-Width 1–5), sourcing Current Fix from competitor products + the map's ⚠ WORKAROUND DIY fixes, then sort descending by gap width. The widest-gap rows are the named shortlist passed to /ctm-to-copy, /ctm-to-content, and /ctm-to-offer.
---

# /ctm-gaps — Map the Gaps (Phase 4, Step 2)

This workflow turns a pile of complaints into a **ranked view of where to act.** Take the pains and the jobs from `/ctm-jobs`, lay each against how the customer handles it today (competitor products + DIY workarounds), name where that fix falls short, and score the gap width. Fire this after `/ctm-jobs`, as the last build step before the Phase-5 apply layer.

The principle is **widest-gap-first** (`../genius.md` Genius Pattern 7): refuse to treat all pains equally. The rows with the widest gaps are the shortlist — what to lead with in copy, what to build content around, where a new or repositioned offer meets real demand. A better message or a better offer lands hardest exactly where the current fix frustrates most.

## Pre-Flight Gate

Load [`../genius.md`](../genius.md) if it is not already hot in this conversation. Do not build a single row before these are answered — they are the Decision Framework from `../genius.md`, narrowed to what Phase 4 Step 2 consumes.

1. **Jobs + map in hand?** Is there a jobs list from `/ctm-jobs` and a saved map from `/ctm-map` (with `⚠ WORKAROUND` tags)? Missing either → run the upstream phase first. This workflow ranks gaps from real pains/jobs; it never invents a pain or a gap.
2. **Are the workarounds carried over?** The map's `⚠ WORKAROUND` tags are the DIY half of the Current Fix column — each is "a problem someone cared about enough to solve badly." If they were dropped, recover them from the map before building.
3. **Competitor fixes named honestly?** The Current Fix column also lists actual competitor products. Any real-world claim about what a competitor does or doesn't do must be verifiable — route it through the Step 5.5 Verification protocol if a claim rides along, don't assert it from memory.
4. **Which output is this feeding?** The widest-gap rows become the explicit shortlist for `/ctm-to-copy`, `/ctm-to-content`, `/ctm-to-offer`. Rank with that hand-off in mind.

## Skill Acquisition

- **Always:** [`../genius.md`](../genius.md) (Genius Pattern 7 "widest-gap-first prioritization," Pattern 5 "the Do-category goldmine," Signature Move 4 "rank by gap width," Quality Rubric criterion 7 Gap Ranking).
- **The canonical method:** [`../references/customer-truth-map-guide.md`](../references/customer-truth-map-guide.md) Phase 4 Step 2 — the primary truth; where this workflow diverges, the guide wins.
- **The exact prompt:** [`../references/prompt-library.md`](../references/prompt-library.md) **P6** (expert verbatim 3-column table + the enhanced 4th column Gap Width 1–5, sorted descending, with the shortlist hand-off).
- **Upstream input:** `/ctm-jobs` (jobs list) + `/ctm-map` (the `⚠ WORKAROUND` tags and PAINS).
- **Adjacent gate:** the Step 5.5 Verification protocol (`directives/verification-agent-protocol.md`) — confirm any real competitor claim before it goes in the Current Fix column.
- **Downstream:** the named widest-gap shortlist hands off to `/ctm-to-copy`, `/ctm-to-content`, `/ctm-to-offer`.

## Execution

Each numbered step has a move, a diagnostic, and a template marked *vary, never verbatim*. A worked thread runs through all of them — audience: **solo bookkeepers who just lost a big client.**

### 1. Assemble Pain/Job rows and run P6

**Move.** Seed the table from the jobs list (each job carries its source pain). Run prompt **P6** from [`../references/prompt-library.md`](../references/prompt-library.md): build a table with **Pain/Job → Current Fix → The Gap**, focused on the rows where the gap is widest.

**Diagnostic:** Does every row start from a real pain/job, or did AI introduce a row no quote supports? Every Pain/Job cell must trace to the map.

### 2. Fill Current Fix from competitors + ⚠ WORKAROUND DIY fixes

**Move.** The Current Fix column has two halves: (a) **competitor products** the customer uses today (verifiable, fact-checked claims only), and (b) the **DIY workarounds** pulled straight from the map's `⚠ WORKAROUND` tags. The workaround is the louder signal — it's the customer telling you, in their own behavior, exactly where every existing solution failed them.

**Diagnostic:** For each row, is the DIY workaround from the map actually represented? A row whose Current Fix lists only a competitor and ignores a tagged workaround has thrown away the best evidence.

**Template (vary):** *Current Fix: "[Competitor app X] for invoicing; plus the customer's own messy spreadsheet re-checked every Monday (⚠ WORKAROUND from map)."*

### 3. Name The Gap (where the fix falls short)

**Move.** For each row, name precisely where the current fix falls short, frustrates, or leaves them wanting. The gap is the wedge — the space a better message or offer fills. State it in the customer's reality, not in your product's language.

**Diagnostic:** Could you read the gap aloud to the customer and have them say "yes, exactly"? If it sounds like a product pitch, it's not a gap — it's a feature you wish they wanted.

**Template (vary):** *The Gap: "Every tool handles the books; none handle the panic. The Monday spreadsheet exists because nothing tells them whether they're actually safe."*

### 4. Score Gap Width (1–5) and sort descending (the ranking move)

**Move — this is what makes the table a decision, not a list.** Add the 4th column **Gap Width (1–5)** and **sort the whole table descending** by it. Width = how badly the current fix fails × how much the customer cares (a deeply-felt pain with a duct-tape-only fix scores 5; a mild annoyance with a decent competitor solution scores 1–2).

**Diagnostic:** Does the #1 row have both a vivid pain *and* a `⚠ WORKAROUND` (a cared-about problem solved badly)? Those two co-occurring is the classic widest-gap signature.

**Template (vary):** a width score per row, with a one-line reason tying the number to evidence (vivid pain + DIY-only fix = 5).

### 5. Name the widest-gap shortlist (the hand-off)

**Move.** Take the top rows (typically the 3–5 widest) and name them explicitly as the **shortlist** passed downstream. State, per shortlisted gap, which output it's best suited to feed — copy lead, content topic, or offer/positioning wedge. This is the deliverable's point: a pile of complaints turned into a ranked, named set of places to act.

**Diagnostic:** Could `/ctm-to-offer` pick up the shortlist and know exactly which gap to build an offer around, with the real quote behind it? If the shortlist isn't named and routed, the ranking didn't finish.

### Worked thread — solo bookkeeper, the gap table (sorted)

| # | Pain / Job | Current Fix | The Gap | Gap Width |
|---|---|---|---|---|
| 1 | *"i lost my biggest client friday…"* → Job: rebuild predictable revenue without panic-pitching | Competitor invoicing apps; plus the customer's *"messy spreadsheet re-checked every monday"* (⚠ WORKAROUND) | Tools manage the books; nothing manages the revenue panic or tells them they're safe. The Monday spreadsheet exists because no product addresses the fear. | **5** (vivid pain + DIY-only fix) |
| 2 | *"not even sure what id say to land another one this size"* → Job: pitch confidently at the high tier | Generic "how to get clients" content; trial-and-error pitching | Advice is generic; nothing teaches pitching *at the tier they just lost.* No fix targets the confidence gap. | **4** (deep pain, weak generic fixes) |
| 3 | wants cleaner monthly close | Existing software does this adequately | Minor friction; competitors largely solve it | **2** (mild pain, decent fix) |

**Named shortlist (widest first):**
- **Gap #1 (width 5) → `/ctm-to-offer` + `/ctm-to-copy`.** The "manage the panic, not just the books" wedge — strongest offer/positioning candidate; the Monday-spreadsheet line is the copy hook.
- **Gap #2 (width 4) → `/ctm-to-content`.** "How to pitch at the tier you just lost" — content series + lead magnet.

> Every quote above is `[illustrative]` — placeholders for format only. **A real run ranks gaps from harvested verbatim pains/workarounds only**, each traceable to a gate-passed, source-tagged quote in the map; competitor fixes are fact-verified, never asserted from memory.

## Content-Type Adaptations

The 4-column table is universal; *what dominates the Current Fix column and how width is read* shifts by category.

| Category | How the gap table changes |
|---|---|
| **Mature / crowded category** | Current Fix is competitor-heavy; gaps are narrow and live in the *unaddressed emotion* or edge case. `⚠ WORKAROUND` rows are the rare wide gaps — competitors solved the obvious, the workaround marks what they missed. |
| **Emerging / underserved category** | Current Fix is DIY-heavy (few real products); gaps are wide by default. Width comes from how painful the workaround is — a daily duct-tape routine scores 5. |
| **B2B / high-consideration** | Width factors in switching cost and risk; a gap a buyer can't act on (procurement-blocked) scores lower even if the pain is real. Note the blocker in The Gap cell. |
| **B2C / impulse** | Width tracks emotional intensity over functional shortfall; a vivid felt pain with any DIY coping = wide gap. The customer's exact emotional phrasing carries the row. |
| **Service / agency offers** | DIY workaround = "they're doing it themselves badly" → strongest offer-extension gap. These rows route preferentially to `/ctm-to-offer`. |
| **Triangulated (multi-source)** | Score width higher when the gap appears across sources (Consistent Truth); flag single-source gaps as lower-confidence even if individually vivid. Pre-stages `/ctm-triangulate`. |

## Output Requirements

Return, in this order:

1. **The gap table** — 4 columns (Pain/Job → Current Fix → The Gap → Gap Width 1–5), **sorted descending by gap width.** Every Pain/Job cell traces to a real, source-tagged quote; Current Fix includes the map's `⚠ WORKAROUND` DIY fixes alongside fact-verified competitor products.
2. **A one-line width rationale per row** — tying the score to evidence (intensity of pain × failure of current fix).
3. **The named widest-gap shortlist** — the top 3–5 rows, each routed to its best-fit downstream workflow (`/ctm-to-copy`, `/ctm-to-content`, `/ctm-to-offer`) with the real quote behind it.
4. **One-line honesty confirmation:** that every row traces to real customer language, every workaround came from the map, and every competitor claim is verifiable (or flagged for the Step 5.5 Verification protocol).

If the jobs list or the map's workaround tags were missing, return that as the blocker and route to `/ctm-jobs` / `/ctm-map` rather than ranking imagined gaps.

## Quality Gate

Score against the `../genius.md` Quality Rubric. This workflow **owns criterion 7 (Gap Ranking)** and must also clear:

- **Gap Ranking (rubric 7):** the gap table is built and sorted descending; the widest rows are identified as the named shortlist with a reason. A table that isn't ranked, or a shortlist that isn't routed downstream, caps the score.
- **Do-Category Mining (rubric 5):** the map's `⚠ WORKAROUND` fixes are represented in the Current Fix column and drive the widest-gap scoring. A wide gap whose DIY workaround was ignored is a miss.
- **Verbatim Integrity (rubric 1) — the veto.** Every Pain/Job cell traces to a real, source-tagged quote; no row, gap, or competitor claim is invented. **A gap built on a fabricated pain or an unverified competitor claim is an automatic fail, regardless of every other score.**

**Honesty Spine (non-negotiable).** The customer's words are the gold; AI sorts the gold from the pebbles — **organizing, never inventing.** The ranking organizes real pains, real workarounds, and verifiable competitor fixes into a decision; it never invents a gap to make the table look fuller or asserts a competitor weakness it can't back. Any real-world claim that rides along is fact-checked, or it doesn't ship.

**Self-check (one line):** *Does every row trace to real customer language, is the table ranked by gap width, and is the widest-gap shortlist named and routed?* If yes, the shortlist ships to the Phase-5 apply layer. If no, the failing row goes back — either trace it to a real quote or cut it.
