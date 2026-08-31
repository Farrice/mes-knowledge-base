# Gigi Mironova — session kickoff brief

**Goal:** a finished, presentable concept that makes Gigi want to hire Farrice for a content
package. Not a proposal. A built thing she can see working, at the standard set in
`DESIGN.md` in this folder — that deck is the floor.

**Relationship:** warm. She is on Jen's team at My House Sellers / Equity Union, Jen rates
her highly, and Farrice wants her to win. This is a gift-with-an-offer, not a cold pitch.
Nothing in the artifact may read as a teardown of her work.

---

## Research — observed 2026-08-30

All VERIFIED items were read directly off her live profile in a logged-in session.

### Identity
- `@gigimironova_realestate` — "GIGI MIRONOVA | LA & SFV REALTOR®"
- **624 posts · 1,252 followers · 835 following**
- Bio: *🏡 Helping you navigate LA Real Estate / 🔑 English & Russian | Buyers & Sellers /
  📍 Los Angeles + San Fernando Valley / 📲 DM "HOME" To Get Started⬇️*
- Link: `myhousesellers.com/contact-us`
- Followed by `_jiing` (Jen) and `myhousesellers`
- Brokerage: **Equity Union Real Estate**, on the **My House Sellers** team
- From her own in-feed contact card: **818-826-9998**, `gigi.mironova@equityunion.com`,
  *"SERVING SAN FERNANDO VALLEY & CONEJO VALLEY"*, **"ENGLISH & RUSSIAN SPEAKING"**
- Highlights: OPEN HOUSES · CLOSED · STATS · ALERION · UPDATES · STATS *(duplicated)* ·
  MYHOUSESELLERS · TEAM · TIPS — every cover is the identical brokerage badge

### Territory actually worked (from her posts)
Van Nuys · Porter Ranch · Chatsworth · Calabasas · Reseda · Tarzana · Simi Valley ·
**Wilmington (South Bay)** · **Fresno**

### Team proof available to her
Post: Equity Union congratulates My House Sellers — **#1 medium team in Calabasas by
transaction sides AND by sales volume**, RealTrends verified.

### Overlap with work already on disk
Two listings on her feed are already in this repo:
`6853 Willis Ave, Van Nuys` (price improvement) — there is a full fact-checked audit at
the **Willis Receipts** artifact — and `1654 Moonseed Ln, Simi Valley`
(`_active/clients/jen-listings/1654-moonseed-simi-valley`). Free, verified raw material.

### UNCONFIRMED — verify before building on any of it
- **The AI-slop imagery claim.** Roughly 40 grid posts were reviewed and no obviously
  AI-generated photography appeared. Her graphics are template overlays on real listing
  photos. Confirm or drop this thesis; do not repeat it as fact.
- Per-post engagement — individual posts were not opened.
- Whether any Russian-language content exists — none appeared in the grid.

---

## Diagnosis

**The headline number: 624 posts bought 1,252 followers.** Roughly two followers per post.
That is not a talent problem or an effort problem — she out-works most agents. It is a
compounding problem, and it is the whole pitch. Lead with it as a fact about the *system*,
never about her.

Four causes, in order:

1. **She is building her brokerage's brand, not her own.** The HouseSellers × Equity Union
   lockup sits on nearly every graphic, usually larger than her name. Every post is an
   advertisement for the team.
2. **~90% of the feed is inventory broadcast** — JUST LISTED, JUST SOLD, FOR LEASE, PRICE
   IMPROVEMENT. Inventory content only reaches people already shopping, which is the
   smallest audience there is, and it expires the day the listing closes. Nothing accrues.
3. **The territory is scattered.** SFV plus Conejo plus Wilmington plus *Fresno* — 200+
   miles apart. Local authority cannot form across that spread. This is the
   whatever-deal-I-can-get pattern Farrice named, showing up in the content.
4. **Her one genuinely personal post is the best thing on the feed** and it is an outlier:
   a portrait beside the line *"I work hard because I can't f*ck up. I don't have anyone to
   fall back on. **I'm the back up.**"* That is real voice, earned, unmistakably hers. The
   system she is using has no place for it.

---

## The wedge

**Russian-language real estate content for Los Angeles.**

She states "English & Russian" in her bio and on her card, and then does nothing with it.
It is a line of collateral, not a content lane. Almost no one is producing quality
real-estate content in Russian for the LA market, and it is the one advantage a competitor
cannot copy by hiring better help.

Everything else about her is contested. This is not.

### Fair-housing constraint — BINDING, read before writing a word

National origin is a protected class. The line is bright and it matters for her licence
and for Farrice's liability:

- **Allowed:** publishing in Russian. Saying she speaks Russian. Explaining American
  escrow, credit, agency, or financing to an audience in their own language. Language is a
  service.
- **Never:** implying a neighborhood is for, popular with, or suited to any national-origin
  group. No "where Russians buy." No demographic descriptions of areas. No steering, in
  either language.

The safe and stronger frame: **she explains the American transaction to people who are
fluent in life but not in this system.** That is a service claim, not a demographic claim,
and it is a better story anyway.

Run everything through `_active/clients/re-compliance/` and the don't-say list before it
ships.

---

## What to build

A concept in the `DESIGN.md` system, carrying her identity rather than Jen's. Suggested
shape — the executing session should exercise judgment, not follow this literally:

1. **A positioning line** that replaces "Helping you navigate LA Real Estate." Her own
   "I'm the back up" is the seed and it is already good.
2. **One 6-slide carousel** in the house grammar, on a first-transaction question that
   matters to a Russian-speaking buyer or seller — bilingual, or a matched Russian pair.
3. **Reel covers** in her palette, not Jen's navy. See recommendation #2 in `DESIGN.md`:
   keying the duotone to a different hue per agent is the cheapest real differentiation and
   it is exactly what this call needs.
4. **A profile rebuild** — bio, the nine highlight covers (currently nine identical badges,
   which is free ground), and the DM keyword.
5. **The offer**, sized to what she can actually pay. The Listing Launch Kit at the $200
   founding rate already exists at `_active/clients/jen-team-pilot/OFFER-BRIEF.md`.

### Standards
- Real photographs only, CC0/PDM, provenance recorded — `DESIGN.md` § Imagery sourcing.
- Never assert an unverified fact about her business. Label VERIFIED / UNCONFIRMED.
- Client-facing artifact carries **zero operator language**. No diagnosis of her mistakes
  inside anything she sees. Operator notes go in a separate paired file.
- Fair-housing lint before delivery.

### Do not rebuild
The design system, the imagery pipeline, and the First Home Valley reference deck are done.
Extend them. Run `/arsenal <task>` first.

---

## Starting the session

```bash
cd "/Users/farricecain/Google Antigravity" && claude
```

Then: `/resume gigi-concept` — or paste this file's path and say *build the Gigi concept
from this brief.*
