---
name: jen-santulan-listing-content
description: Produces warm, conversational real-estate content for Jennifer Santulan's @realestatewithjing Instagram — Reels hooks, Story sequences, and Carousels targeting San Fernando Valley first-time buyers ($800K-1.2M range, currently renting $2.5-3.5K/mo, age 30-42, $100-200K HHI). Use when working on Jen Santulan's listings/social content, drafting listing reels or stories for SFV properties, generating real-estate Instagram hooks, or any task in _active/jen-listings/ or projects/jen-*/ directories. Trigger this proactively even when the user just shares an MLS listing or a property photo without naming Jen — her listing pipeline is the default real-estate context.
paths:
  - "_active/jen-listings/**"
  - "projects/jen-*/**"
when_to_use: User is producing Instagram content for Jen Santulan's real-estate practice OR working with a SFV property listing OR drafting first-time-buyer-targeted real-estate copy. Specifically NOT for generic real-estate marketing — Jen's voice (warm, enthusiastic, emoji-rich, "Let's check it out!" closers, #realestatewithjing) is distinct and brand-specific.
version: "2.1"
format: completion-engine
workflows: 3
expert: Jennifer Santulan (@realestatewithjing)
domain: Real estate social media (LA / San Fernando Valley specialist)
---

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
| **01** | `listing-content` | 6 video hooks per property (Reels) | New listing hits market — need scrollable hook variants |
| **02** | `buyer-education-story` | Educational Reels / Stories for FTHBs | Authority + DM list growth, NOT tied to specific listing |
| **03** | `neighborhood-deep-dive-carousel` | 7-slide SFV neighborhood carousels | SFV specialist positioning, save-rate optimization |

### Workflow Selection

**Got a new listing?** → Workflow 01 (listing-content)
**Want to build trust without a property?** → Workflow 02 (buyer-education-story)
**Want to own a neighborhood in search/saves?** → Workflow 03 (neighborhood-deep-dive-carousel)

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
