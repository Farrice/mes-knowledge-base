---
thread: gigi-concept
status: active
resume_hint: Gigi Mironova concept build — research DONE, design floor banked
branch: worktree-jen-fhv-design-fixes
pin: true
---

# Gigi Mironova concept build

Build a presentable concept that makes **Gigi Mironova** — an agent on Jen Santulan's team
at Equity Union / My House Sellers — want to hire Farrice for a content package. Warm
relationship; this is a gift-with-an-offer, never a teardown.

## Read these two first, in this order

1. `_active/clients/_shared/realtor-editorial-system/GIGI-KICKOFF.md`
   — research, diagnosis, the wedge, and a BINDING fair-housing constraint.
2. `_active/clients/_shared/realtor-editorial-system/DESIGN.md`
   — the design floor. Farrice's explicit standard, in his words: *"this should be the
   floor… premium, high taste, quality, done right."* Below it is a regression.

## Research is DONE — do not re-scrape

Observed live, logged-in, 2026-08-30:
- `@gigimironova_realestate` · **624 posts · 1,252 followers · 835 following**
- Bio states "English & Russian | Buyers & Sellers"; card adds "SERVING SAN FERNANDO VALLEY
  & CONEJO VALLEY"; 818-826-9998; gigi.mironova@equityunion.com
- Brokerage lockup (HouseSellers × Equity Union) outranks her own name on nearly every graphic
- ~90% of the feed is inventory broadcast (JUST LISTED / SOLD / FOR LEASE / PRICE IMPROVEMENT)
- Territory scattered: SFV + Conejo + Wilmington + **Fresno**
- Best post on the feed, and an outlier: *"I work hard because I can't f*ck up. I don't have
  anyone to fall back on. I'm the back up."*
- Two of her listings already have verified material on disk: 6853 Willis Ave (the Willis
  Receipts audit) and 1654 Moonseed Ln.

**UNCONFIRMED — verify or drop, never repeat as fact:** the AI-generated-imagery thesis.
~40 grid posts reviewed, no obviously generated photography found.

## The wedge

Russian-language LA real estate content. Stated in her bio, worked nowhere. The one
advantage a competitor cannot copy by hiring better help.

**Fair housing is binding here.** Language is a service claim and is fine. National origin
is a protected class: no "where Russians buy," no demographic descriptions of areas, no
steering in either language. Safe frame — she explains the American transaction to people
fluent in life but not in this system. Lint via `_active/clients/re-compliance/`.

## Do NOT rebuild

The design system, the imagery pipeline (`fetch_bank.py` → `sweep.py` → `contact_sheet.py`
→ `make_shortlist.py` → `prepare.py`), and the First Home Valley reference deck are shipped.
Extend them. `/arsenal <task>` before building anything.

Reference deck: `_active/clients/jen-santulan/production/first-home-valley/canvas-v2/`
Live canvas: https://claude.ai/code/artifact/577da36e-85d2-482c-bcf4-6cc99b0a1652
Offer already written: `_active/clients/jen-team-pilot/OFFER-BRIEF.md` ($200 founding rate)

## Standards

Real photographs only, CC0/PDM, provenance recorded. Client-facing artifact carries zero
operator language — no diagnosis of her mistakes inside anything she sees; operator notes
go in a separate paired file. Label VERIFIED / UNCONFIRMED on every claim about her business.
