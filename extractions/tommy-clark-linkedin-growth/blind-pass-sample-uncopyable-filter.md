# Blind-Pass Sample — Uncopyable Post Filter output (Tier 1)

Generated 2026-07-15 by running `workflows/uncopyable-post-filter.md` + `references/prompts-v2/uncopyable-post-audit.md` on a synthetic-but-realistic input: a generic agency-founder hiring post draft.

**Test input draft**: "We're hiring! Compound-style content agencies live and die by their writers. 5 things we look for when hiring content strategists: 1) Writing samples over resumes 2) Curiosity 3) B2B experience 4) Speed 5) Taste. DM me if interested."
**Raw material inventory supplied**: agency is 3 years old; founder + head of content handled all client services themselves until this quarter; regularly gets DMs asking about freelance roles; two strategist hires already made this year.

---

## Moat Audit
| Moat | Present? | Evidence |
|---|---|---|
| Narrative | NO | Generic listicle criteria — any agency could post this |
| Data | NO | No proprietary numbers |
| Physical | NO | No IRL asset |

**Claude Test**: FAIL — "write me a hiring post for a content agency" produces this post nearly verbatim.

## Injection Plan
Anecdote injection (cheapest): the founder's own operating history — three years of doing client services personally, the standing freelance-DM stream, the two hires already made. All verifiable company history no LLM could invent.

## Rewritten Post

We just made our 3rd and 4th hires of the year at our agency.

Kind of surreal to type that.

For the first 3 years, me and my head of content WERE the client services team. Every deliverable review, every "quick call?", every fire drill — us. As we mature past 30 accounts, it's time to change that.

So we're bringing on 2 more content strategists.

What we actually screen for (in order):

- Writing samples. I have never once read a resume first.
- You've sat in the B2B founder's seat with a client before — you know what a pipeline conversation sounds like.
- Speed without hand-holding.

Also: I get DMs every week asking if we take freelance writers. For the first time — yes. We're opening a freelance bench alongside these full-time roles.

If you've read this far and thought "that's me," my DMs are open. Show me something you wrote.

## Moat Declaration
Narrative moat — the "first 3 years we WERE client services" line and the freelance-DM stream are verifiable company history; no bare prompt produces them.

## Relevance Verdict
Story source: company operating history — squarely ICP-relevant (founders evaluating whether this agency knows their world). Not engagement bait.

---

## Side-by-side judgment (vs reference corpus, model-judged)

Reference pieces: `reference-corpus/founder-led-content-is-no-longer-enough.txt` (2026-07-06), `reference-corpus/2026-content-bets.txt`.

**What held**: (1) Anecdote-as-moat structure matches his stated method and his own hiring post described in the source video (the sample's company-history lines are the same move as his "de facto head of client services" line). (2) Casual, peer-voice register with short punch paragraphs matches corpus rhythm ("Kind of surreal to type that." ≈ corpus "Long, long gone."). (3) Specific counts and ordinal facts over rounded claims. (4) The corpus independently uses "content moat" framing — the extraction's Three-Moat System is his real, current vocabulary, not an imposed frame.

**What gave it away / gaps**: The corpus voice carries more irreverence and cultural asides ("in the year of our Lord, 2026," World Cup riffs, "Marketers ruin everything") than the sample; a Farrice-judged pass on client-grade output should stretch that register. Newsletter-length pieces also show named third-party examples (Clay, Perspective) — the sample's single-company scope didn't exercise that.

**Verdict**: PASS (model-judged; B-tier appropriate — A-tier promotion requires a Farrice-judged pass per embodiment-standard).
