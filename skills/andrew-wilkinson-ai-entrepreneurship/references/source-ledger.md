# Source Ledger — Andrew Wilkinson AI Entrepreneurship

Claim-by-claim provenance for every factual/quote claim used or referenced in `genius.md`
and `SKILL.md`. Labels: **VERIFIED** (exact quote confirmed against a primary source),
**LIKELY** (concept/quote confirmed but combined, paraphrased, or approximate), **UNCONFIRMED**
(no primary source found for this specific claim as of this repair pass).

## Absence check (run before writing anything else)

`extractions/` was searched for Andrew Wilkinson source material before this repair:

```
ls extractions/ | grep -i wilkinson       → no results
grep -ril "wilkinson" extractions/         → extractions/mike-foutia-marketing-tools/extraction-report.md
                                              (a cross-reference to THIS skill, not a source for it)
```

No `extractions/andrew-wilkinson*` directory or transcript exists in this repo. This is a
confirmed absence, not an unread gap — verified by a real directory listing and a
recursive grep on 2026-07-17. The skill's own pre-existing files were then checked for size
(so "no source" claims aren't confused with "empty/corrupt file" claims):

```
wc -c skills/andrew-wilkinson-ai-entrepreneurship/SKILL.md                          → 3866 bytes
wc -c skills/andrew-wilkinson-ai-entrepreneurship/genius.md                         → 12459 bytes (pre-repair)
wc -c skills/andrew-wilkinson-ai-entrepreneurship/references/genius-patterns.md     → 1921 bytes
wc -c skills/andrew-wilkinson-ai-entrepreneurship/references/hidden-knowledge.md    → 1775 bytes
wc -c skills/andrew-wilkinson-ai-entrepreneurship/references/implementation.md      → 1498 bytes
```

All non-empty. None of them cite an external source for any claim — the skill was built
without a source ledger. This repair grounds it against four external primary sources
found via live web search/fetch on 2026-07-17, since no local transcript exists.

## Primary sources consulted (2026-07-17 search/fetch pass)

| # | Source | Type | Date | URL |
|---|--------|------|------|-----|
| S1 | "Opus 4.5 Changed How Andrew Wilkinson Works and Lives" — *AI & I* podcast, Every.to | Podcast transcript | 2026-01-21 | https://every.to/podcast/transcript-opus-4-5-changed-how-andrew-wilkinson-works-and-lives |
| S2 | "I've run 75+ businesses. Here's why you're probably chasing the wrong idea." — Lenny's Newsletter | Interview | 2025-07-03 | https://www.lennysnewsletter.com/p/ive-run-75-businesses-andrew-wilkinson |
| S3 | "How I Lost $10,000,000" — *Founder's Journal*, Morning Brew | Podcast | 2024-03-15 | https://foundersjournalpod.morningbrew.com/how-i-lost-10000000/ |
| S4 | Andrew Wilkinson, @awilkinson | X posts | 2026 (various) | https://x.com/awilkinson/status/2001685012559913044, https://x.com/awilkinson/status/2012559525811814442, https://x.com/awilkinson/status/1856066444678836401 |

Note: content behind S1–S4 was retrieved via WebFetch/WebSearch summarization, not read as
raw HTML/transcript text in full — treat quoted strings below as accurately extracted by
that pass, not independently re-verified character-for-character against the original
audio/video. This is disclosed, not hidden.

## Claim ledger

| Claim (as it appears in genius.md) | Label | Source | Note |
|---|---|---|---|
| "I'm paying them like $40 a day. It's crazy." | VERIFIED | S1 | Direct quote per fetch. |
| "I have 30 free employees and they're just working 24/7" | VERIFIED | S1 | Direct quote per fetch. |
| "a $100,000 a month payroll of engineers working for me 24/7" | VERIFIED | S1 | Direct quote per fetch. |
| "Claude Code turned a $5M engineering department into a $50k line item." | VERIFIED | S4 | X post title/text surfaced directly in search result. |
| Skill's own line: "With Claude Code, I feel like I have 30 new employees for $40/day" | LIKELY | S1 | Conflates two separate S1 statements above into one sentence; not found as a single verbatim quote. |
| "I can really move at the speed of thought... I have 30 free employees and they're just working 24/7" | VERIFIED | S1 | Direct quote per fetch. |
| "you can't inject any of your own opinion into the prompt... You have to analyze every single word" | VERIFIED | S1 | Direct quote per fetch, re: a self-described failed audit ("I prompted it the wrong way"). |
| "unless you have a distribution moat or a hardware moat or something like that... most software businesses are just thin wrappers" | VERIFIED | S1 | Direct quote per fetch. |
| "Programming is hard to learn... and now it's basically free. So your moat has to come from something else." | VERIFIED | S1 | Direct quote per fetch. |
| "I think a lot of them will probably go to blue collar work... when 100 people all start an HVAC company... the margins go to zero" | VERIFIED | S1 | Direct quote per fetch. |
| Deep Personality: self-built personality/relationship assessment, "I've just been loving that and I'm actually releasing that to the public really soon" | VERIFIED | S1 | Direct quote per fetch. |
| Deep Personality would have cost "$20,000-$25,000" with a hired designer | LIKELY | S1 | Per fetch summary; not the $25-30K figure the pre-existing skill attaches to "Relationship OS." |
| "Relationship OS" as a named product; "$25-30K" valuation | UNCONFIRMED | — | Not found in S1–S4 or any search pass. Closest verified analog is Deep Personality (different name, different number — see above). Pre-existing skill content; flagged, not deleted (additive-only repair boundary). |
| "Manipulation detection" / psychological-safety-net AI feature | UNCONFIRMED | — | Not found in S1–S4. Pre-existing skill content; flagged, not deleted. |
| "Choose-your-own-adventure" email triage feature; "80%+" response-time drop | UNCONFIRMED | — | Not found in S1–S4. Pre-existing skill content; flagged, not deleted. |
| MCP-specific commentary from Wilkinson | UNCONFIRMED | — | Not found in S1–S4. Inferred only from general Claude Code usage. |
| "Pennies in front of a steamroller" as Wilkinson's own phrase | UNCONFIRMED | — | Confirmed as a general finance idiom (Hacker News thread 33630016, 2011: https://news.ycombinator.com/item?id=33630016) with no Wilkinson-AI attribution found. The underlying commoditization warning IS verified (see moat quotes above); the specific idiom is not. |
| Context sync across devices as a named principle | UNCONFIRMED | — | Not found in S1–S4. |
| Compute ownership as a portfolio hedge | UNCONFIRMED | — | Not found in S1–S4. |
| Personal brand AI / voice-consistency suite | UNCONFIRMED | — | Not found in S1–S4. Loosely adjacent to a friend's AI journaling workflow he amplified (S4, X status 1856066444678836401), which is about journaling, not brand voice. |
| "If you're competing on features, it never stops and is an ever-increasing line item" | VERIFIED | S3 | Direct quote per fetch. |
| "Don't bring a knife to a gunfight" | VERIFIED | S3 | Direct quote per fetch, re: competing in a VC-funded space without raising money. |
| "I was consistently spending two to three times our monthly revenue... out of my personal bank account" | VERIFIED | S3 | Direct quote per fetch. |
| Flow: $10M+ lost over 12 years; peak ARR $3M; current ARR ~$900K; peak burn $150K/month | VERIFIED | S3 | Per fetch summary of the episode's stated figures. |
| "Money is just 'Europe for your anxiety.'" | VERIFIED | S2 | Direct quote per fetch. |
| ~30% of entrepreneurs report ADHD symptoms vs. ~5% general population | VERIFIED | S2 | Per fetch summary of the interview's stated figures. |
| "Fish where the fish are" / form-filling software generating ~$30M/year | VERIFIED | S2 | Per fetch summary. |
| "I underestimated how emotional the impact of AI would be. For a decade, I was depressed about work." | VERIFIED | S4 | X post text surfaced directly in search result. |
| Portfolio (Tiny): 75+ businesses run, ~$300M/year sales, personal net worth >$1B at one point | LIKELY | S2 | Per fetch summary; not independently cross-checked against a second source. |

## Skill-level verdict

The pre-existing skill (`SKILL.md`, `genius.md` before this repair) was written with zero
external sourcing — every pattern read as plausible Wilkinson-adjacent content with no
citation trail. This repair did NOT delete or rewrite that content (additive-only boundary);
it added a `**Source**:` line to every Pattern/Tacit/Exemplar section with an honest
VERIFIED/LIKELY/UNCONFIRMED label and, where UNCONFIRMED, said so plainly rather than
inventing an anchor. Nine of nineteen Pattern/Tacit/Exemplar sections (Pattern 5 Psychological Safety Net,
Pattern 6 Choose-Your-Own-Adventure Email, Pattern 7 MCP Extensibility, Tacit 1 $30K
Product Recognition, Tacit 3 Context Sync, Tacit 7 Compute Ownership, Tacit 8 Personal
Brand AI Suite, Exemplar 1 "Relationship OS", Exemplar 2 Podcast Prototype) remain
UNCONFIRMED and should be treated as speculative until a primary source is found.
