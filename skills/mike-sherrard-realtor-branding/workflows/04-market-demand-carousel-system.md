# Workflow 04 — Market-Demand Carousel System

**Source**: Sherrard, "Claude Design for Real Estate" (YouTube uuHoj4FMZFI, 2026 — watched, frames + transcript in `extractions/real-estate-offer-enrichment/`).
**Produces**: a set of 5-10 branded Instagram carousels/graphics for one agent, built from live market-demand research, in the agent's brand system — not templates.
**Why it works**: content answers what buyers/sellers/relocators in THAT market are searching THIS month (demand-backed, not assumed), and the design pass runs under an editorial contract so output reads studio-made, not AI-default. Sherrard replaced a $5K/mo design team with this pipeline.

---

## Stage 1 — Agent context (the "brain")

Never generate from a cold start. Load the agent's brand + market file first — in our harness this is the completed `AGENT-INTAKE` (brand tokens, voice register, niche, market) plus their voice card. Missing intake = stop and collect it; generic output is the failure mode this whole system exists to kill.

## Stage 2 — Market demand research

Research what people in the agent's market are actively searching NOW. Use real research (`execution/research.py` / web search) — never training memory. Collect, with evidence:

- **Buyer searches** — live questions ("are prices going to crash," "should I wait for rates," local tax/insurance quirks)
- **Seller searches** — what would-be sellers ask before listing
- **Relocation searches** — exact phrases + the worry underneath each (the content's job is to give ease, not hype)
- **This month's market news** — local, current
- **Questions nobody's answering** — the 5 highest-demand questions with no good local content. These are the priority queue; answering them is the lead engine.

Validate before using: each item needs a source, not a vibe. Output: one research doc per agent per month.

## Stage 3 — Content plan + scripts (when video is in scope)

Turn research into a sequenced plan (what to post, in order, by week), then scripts: hook + word-for-word script + bullet-point version + captions written per platform (Instagram / TikTok / Shorts optimize differently). For kit delivery this merges with the Teleprompter Pack; for carousel-only delivery, skip to Stage 4 pulling directly from research.

## Stage 4 — The design pass (the contract that beats generic)

Pull the **10 strongest VISUAL ideas** from the plan/research — stats, myth-busts, checklists, comparisons, before/afters. Ideas that are inherently visual, not paragraphs.

Then run the design under this contract (Sherrard's prompt, verbatim discipline):

1. **Brand first, ask before designing**: colors, fonts, logo, market + audience, platform, single-image vs. carousel. Options to pick from, never open-ended questions. (Our harness: pre-answered by AGENT-INTAKE.)
2. **2-3 DISTINCT design directions** for the set — different type treatments, layouts, color use; NOT three versions of one idea. Agent picks one; it applies across the whole set so 10 graphics read as one brand.
3. **Approve graphic #1 before building the rest.** Never batch-produce unapproved direction.
4. **Quality bar**: studio-made, editorial grade — confident typography, real grid, generous whitespace, deliberate spacing. "If it looks like default AI output, redo it."
5. **One dominant element per graphic**, clear hierarchy, readable in 3 seconds on a phone mid-scroll.
6. **Typography does the heavy lifting**: max 2 fonts, dramatic scale contrast headline-vs-support, tight tracking on big headlines, nothing centered by default.
7. **Color with restraint**: controlled palette, ONE accent used sparingly, strong contrast, backgrounds that let type breathe.
8. **Stats become shapes**: bars, comparisons, proportional visuals — never a big number floating in space.
9. **Banned**: cheesy stock photos, emojis as design elements, gradients, drop shadows, clip art, text touching edges, more than one idea per graphic.

## The carousel grammar (from Sherrard's live outputs)

Every carousel: **Hook card** (a bold claim or objection flip — "A buydown isn't a discount. It's a price.") → **numbered value slides** (01/02/03, one idea each, dark editorial fields with the accent reserved for emphasis) → **keyword CTA card** ("DM me 'AUSTIN'") in the accent color. The CTA card is the only loud slide in the set.

## Cadence + economics

Sherrard posts ~3 carousels/week from this system. Per-agent marginal cost in our harness: one research run + one design session ≈ 60-90 min for a monthly set. Fair-housing floor applies to every slide: `python3 execution/fair_housing_lint.py check --text "..." --context script`.

## Anti-patterns

- Designing before research: pretty content nobody searched for is decoration, not leads.
- Skipping the direction-pick step: output drifts generic within 3 graphics.
- Letting the accent color spread: one accent, sparingly, or the set reads as template.
- Answering the intake yourself: brand facts come from the agent's intake, never invented.
