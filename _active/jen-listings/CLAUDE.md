# Jen Santulan — Project Context

> **Inherits from**: `/Users/farricecain/Google Antigravity/CLAUDE.md` (The Chain, Architecture, Skill tiers, Quality Gate)
> **Active since**: 2026-03 (skill pack + listing engine live)
> **Source of truth**: `skills/jen-santulan-listing-content/` (SKILL.md, genius.md, workflows/)
> **Domain**: LA real estate, San Fernando Valley specialist, Instagram-first (@realestatewithjing)

---

## Brand Identity (One Paragraph)

**Jennifer Santulan** is Farrice's wife and an LA real estate agent specializing in the San Fernando Valley. Her deliberate niche: first-time home buyers (dual-income couples, age 30-42, $100K-$200K HHI, $800K+ budget, currently renting $2.5K-$3.5K/mo). The voice is **warm, enthusiastic, conversational** — telling your best friend about a listing she can't stop thinking about. Educational and encouraging, never high-pressure, never brochure-copy. Emoji-rich. Question openings. "Let's check it out!" closers. #realestatewithjing.

---

## Voice Test (Apply to Every Line)

**"Would Jen say this to her best friend over coffee?"**
- If yes → ship
- If no → rewrite

Specific cues:
- Warm, enthusiastic, conversational (NOT cynical / staccato / adversarial)
- Educational, not transactional
- Excitement about properties, not pressure to buy
- First-person observations ("when I walked in...")
- Question openings ("Looking for a starter home in SFV?")
- Closers like "Let's check it out!" or "DM me 'TOUR' for a walkthrough"

---

## When to Load Full Context

| Task | Load |
|------|------|
| New listing → social content | `skills/jen-santulan-listing-content/workflows/01-listing-content.md` |
| Educational content (no specific listing) | `workflows/02-buyer-education-story.md` |
| SFV neighborhood content | `workflows/03-neighborhood-deep-dive-carousel.md` |
| Voice deep dive | `skills/jen-santulan-listing-content/genius.md` |
| ICP details | `strategy_briefs/Strategy_Brief_First_Time_Home_Buyers_in_SoCal.md` |

---

## Override List (Where This Project Diverges from Root CLAUDE.md)

- **Hooks are warm-opener, NOT vicious-hook style.** Default Antigravity hook-forge workflows lean adversarial / pattern-interrupt. Jen's hooks open with curiosity + warmth, never confrontation. If a workflow produces a "WHY YOUR REALTOR IS LYING TO YOU"-style hook, reject and rewrite.
- **Emojis ARE part of voice, not slop.** Root CLAUDE.md guidance to minimize emojis does NOT apply to Jen's Instagram content. Use them; don't strip them.
- **Skip Step 5.5 verification for stylistic/creative content.** Jen's content rarely has factual claims requiring verification (property facts come from MLS, not invented). Factual Grounding scoring usually = N/A.
- **First-time-home-buyer empathy frame.** Anti-jargon. Anti-acronym-without-explanation (DTI, LTV, PMI, etc. — always define on first use). Anti-"you should already know this" tone.
- **California / SFV-specific.** Generic real estate advice that ignores California market realities (Prop 13, supply constraints, $800K+ starter homes) is wrong by default.

---

## Anti-Patterns Specific to This Client

- ❌ "Dangerous in a room" / agency-tier copywriter jargon — Jen doesn't talk like that
- ❌ Forced authority moves ("As a top 1% agent...") — humility is on-brand
- ❌ Urgency manufacturing ("THIS WON'T LAST", "ACT NOW") — wrong vibe for first-time buyers
- ❌ Ignoring the underlying ICP fear (am I being financially irresponsible? am I ready?)
- ❌ Generic "amenities listing" prose — show specific moments / details

---

## Cross-References

- ICP profile: `strategy_briefs/Strategy_Brief_First_Time_Home_Buyers_in_SoCal.md`
- Voice rules: `skills/jen-santulan-listing-content/genius.md` (full DNA)
- Memory anchor: `MEMORY.md` → "Jennifer (Jen) Santulan — Real Estate Content"
