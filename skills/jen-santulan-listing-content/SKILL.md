---
name: jen-santulan-listing-content
description: Produces register-aware real-estate content for Jennifer Santulan's Instagram — Reels hooks, scripts, captions, and full sendable listing packages. Two registers by listing tier — FTHB/everyday (<$1.5M, warm-friend voice, SFV first-time buyers) and luxury (≥$2M, "Quiet Flex Elite Advisor" authority-POV). Use when working on Jen Santulan's listings/social content, when the user drops ANY listing URL (Zillow/Redfin/realtor), an MLS listing, or a property address/photo — her listing pipeline is the default real-estate context; /listing-package is the URL→sendable-package front door.
paths:
  - "_active/clients/jen-listings/**"
  - "projects/jen-*/**"
when_to_use: User drops a listing URL or property address for content OR is producing Instagram content for Jen Santulan's real-estate practice OR needs a full listing package (hooks + scripts + caption + forwardable send text) OR is drafting SFV/LA real-estate copy for Jen. Specifically NOT for generic real-estate marketing — Jen's registers are brand-specific and tier-gated (_active/clients/jen-listings/CLAUDE.md ladder).
version: "3.0"
format: completion-engine
workflows: 4
expert: Jennifer Santulan (@_jiing)
domain: Real estate social media (LA / San Fernando Valley specialist)
routing: long-tail
scope_note: "2026-09-02 reset: Convert district only (her own listings, /listing-package). Never the front door for Jen content; that is /jen (.agent/workflows/jen.md), which loads references/jen-real-voice-profile.md + jen-calibration-log.md as the voice source. The 'warm-enthusiastic, emoji-rich' voice below is the March floor; the July scrape and Sept voice memos (calm-warm lowercase) win on conflict."
---

> **SCOPE (2026-09-02):** Convert district only. Front door for everything Jen is `/jen`. Voice source of truth is `references/jen-real-voice-profile.md`, not the paragraph below.


# Jen Santulan Listing Content Engine

> Expert-powered viral mechanics calibrated to Jen's authentic warm-friend voice. Two-pass architecture across all workflows: expert engineering → Jen voice polish.

## Domain

**Real estate social media** — Instagram-first content for Jen Santulan, an LA real estate agent specializing in the San Fernando Valley with a deliberate niche in first-time home buyers (dual-income couples, $100K-$200K HHI, $800K+ budget, currently renting).

## Voice Foundation

Jen sounds like a warm, knowledgeable friend telling you about a listing she just saw and can't stop thinking about. Educational, encouraging, and genuinely excited — never the high-pressure salesperson, never the brochure copy.

**The voice test**: read every line out loud. If Jen wouldn't say it to her best friend over coffee, rewrite it.

Full voice DNA, signature patterns, anti-patterns, and quality bar in `genius.md`.

## Workflows

| # | Workflow | Produces | When to Use |
|---|---|---|---|
| **04** | `listing-package` | **Full pipeline: URL → verified facts + claims ledger → register-aware hooks + scripts + caption + forwardable send text, ONE SHOT — judge the finished brief** | Any listing URL/address drop; the default for new listings (supersedes 01 as the front door) |
| **01** | `listing-content` | 6 video hooks per property (Reels) | Quick hooks-only pass; a sitting listing needing a fresh angle set |
| **02** | `buyer-education-story` | Educational Reels / Stories for FTHBs | Authority + DM list growth, NOT tied to specific listing |
| **03** | `neighborhood-deep-dive-carousel` | 7-slide SFV neighborhood carousels | SFV specialist positioning, save-rate optimization |

### Workflow Selection

**Got a listing URL or a shoot coming up?** → Workflow 04 (listing-package) — the end-to-end engine
**Just need hook variants fast?** → Workflow 01 (listing-content)
**Want to build trust without a property?** → Workflow 02 (buyer-education-story)
**Want to own a neighborhood in search/saves?** → Workflow 03 (neighborhood-deep-dive-carousel)

### Register Ladder (binding — Jen's own verdict, 2026-08-05)

Tier decides register BEFORE any generation (canon: `_active/clients/jen-listings/CLAUDE.md` Override List; calibration: `references/jen-calibration-log.md`):
- **<$1.5M (FTHB/everyday):** warm-friend voice, FTHB-Permission hook mandatory.
- **≥$2M (luxury):** "Quiet Flex Elite Advisor" — authority-POV hooks (market thesis, property as evidence), FTHB-Permission hook forbidden.
- Fair-housing floor on all spoken text: `execution/fair_housing_lint.py` (no safe/family/great-for-kids, schools off camera).

## Expert Frameworks Embedded

Across all 3 workflows, viral mechanics are powered by:

| Expert | Contribution |
|---|---|
| **Kallaway** | Dopamine Ladder (scrollstop), Curiosity Loop, Contrast Mapping |
| **Brock Johnson** | Share Hierarchy (5 triggers), Pattern Interrupt, Save-Worthy Density |
| **Seena Rez** | Hyperdopamine Hook Architecture, 3-second scrollstop |
| **Shaan Puri** | One Emotion Rule, Frame > Hook |
| **Harry Dry** | Three Rules Test (visualize, falsify, uniqueness) |
| **Made to Stick** | Concrete + Emotional principle (Workflow 02 educational frames) |

The mechanics are invisible to viewers — they only feel Jen's warmth and genuine excitement. Pass 1 engineers the structure. Pass 2 polishes into voice.

## ICP — The "Trapped Millennial" Buyer

| Attribute | Detail |
|---|---|
| Age | 30-42 (median FTHB nationally is 40) |
| Income | $100K-$200K dual-income |
| Current rent | $2,500-$3,500/mo |
| Emotional state | Frustrated, "priced out," scrolling Zillow at midnight |
| Primary fear | Stuck renting into retirement |
| Primary hope | A program, neighborhood, or path they didn't know about |

Strategy brief: `strategy_briefs/Strategy_Brief_First_Time_Home_Buyers_in_SoCal.md`

## What Makes This Skill Different

1. **Voice authenticity** — every line passes the "would Jen say this to a friend" test
2. **Trust-first** — genuine scarcity only, math transparency, never manufactured urgency
3. **FTHB Permission Mechanic** — niche-specific move that names midnight pain → flips with proof → invites action (genius.md Section 8)
4. **SFV specialist depth** — sub-neighborhoods, local landmarks, cross-neighborhood comps, FTHB programs (HOP80/120, LIPA, Greenline, MyHome)
5. **Educational surplus** — every piece teaches something the buyer didn't expect

## Quality Gate

Before publishing anything from this skill, run against `genius.md` Section 10 quality bar:
- Voice (6 checks — must pass all)
- Trust (4 checks — must pass all for FTHB content)
- SFV Authority (3+ of 5)
- Engagement Mechanics (2+ of 4)

## Quick Start

```
/listing-package [url | address | --paste]              # Workflow 04 — the end-to-end engine
/listing-content [address]                              # Workflow 01
/buyer-education-story [topic angle]                    # Workflow 02
/neighborhood-deep-dive-carousel [neighborhood]         # Workflow 03
```

Or invoke directly via skill files:
```
Load: skills/jen-santulan-listing-content/genius.md
Execute: skills/jen-santulan-listing-content/workflows/0[N]-[name].md
```

## Related Skills

- `voice-calibrate` — for content authored by other experts that needs Jen-voice polish
- `kallaway-addictive-storytelling` — deeper dopamine/curiosity engineering
- `brock-johnson-shareworthy-content` — share-trigger architecture
- `nicolas-cole-newsletter-flywheel` — if Jen ever wants long-form content (out of scope here)

## Files

- `SKILL.md` — this file
- `genius.md` — voice DNA, signature patterns, quality bar
- `PROMPT.md` — original master prompt (reference; superseded by workflow 01)
- `workflows/01-listing-content.md` — listing video hooks
- `workflows/02-buyer-education-story.md` — FTHB educational content
- `workflows/03-neighborhood-deep-dive-carousel.md` — SFV neighborhood authority
- `workflows/listing-package.md` — URL → sendable package (full pipeline; the front door)
- `references/jen-real-voice-profile.md` — scraped voice floor (@_jiing) · `references/jen-calibration-log.md` — felt-verdict ratchet (outranks defaults)
- `references/send-package-template.md` — the forwardable-text shape

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

4 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **[Topic] — Educational Content Pack** — `skills/jen-santulan-listing-content/references/prompts-v2/buyer-education-content.md`
- **[Address] — Listing Hook Set** — `skills/jen-santulan-listing-content/references/prompts-v2/listing-hook-set.md`
- **Jennifer Santulan — Listing Send Package (One Forwardable Text)** — `skills/jen-santulan-listing-content/references/prompts-v2/listing-send-package.md`
- **[Neighborhood] Carousel — [Sub-angle]** — `skills/jen-santulan-listing-content/references/prompts-v2/neighborhood-deep-dive-carousel.md`

<!-- END:execution-prompts -->
