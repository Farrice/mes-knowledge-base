# Source Ledger — Sabrina Ramonov: AI Monetization & Learn-in-Public Strategy

Every source consulted for this skill's repair pass (Wave 3 Lane 4 Batch 15), with a
claim-by-claim confidence label. Ground truth = files under `extractions/sabrina-ramonov/`
(the only extraction material found for this expert; searched via `ls extractions/ | grep
-i ramonov` and `grep -i sabrina`, both hits below — no `_archive/claude-export-2026-07-01.tar.gz`
scan was needed because primary-source files were found directly under `extractions/`).

## Sources Consulted

| Source | Size | Role |
|---|---|---|
| `extractions/sabrina-ramonov/transcript-zero-to-1m.txt` | 18,394 bytes (`wc -c`) | Primary — full raw transcript of "If I Had to Make $1M From $0" |
| `extractions/sabrina-ramonov/extraction-report.md` | 14,149 bytes (`wc -c`) | Secondary — prior extraction pass derived from the transcript |
| `skills/sabrina-ramonov-ai-monetization/genius.md` (pre-repair) | — | Existing skill content, cross-checked against the transcript |
| `skills/sabrina-ramonov-ai-monetization/SKILL.md` (pre-repair) | — | Existing skill content, cross-checked against the transcript |
| https://www.youtube.com/watch?v=WvsWbgE_kWg | — | Cited as the transcript's origin inside the transcript file header; not independently re-fetched by this repair pass |

## Claim-by-Claim Labels

- **VERIFIED** — "It is so tempting to switch... The trap that people fall into again and again is chasing the next shiny object when you truly haven't given yourself enough time runway" — verbatim in `transcript-zero-to-1m.txt`.
- **VERIFIED** — "they spend months building courses or products that nobody buys, or starting agencies that bleed customers every single month" — verbatim in `transcript-zero-to-1m.txt`.
- **VERIFIED** — "if you wait until you're ready, honestly, you're giving it yourself an excuse to never get started" — verbatim in `transcript-zero-to-1m.txt`.
- **VERIFIED** — "AI startups in particular flush with cash. So they're throwing money at any AI influencer that's willing to take it" — verbatim in `transcript-zero-to-1m.txt`.
- **VERIFIED** — "the vast majority of courses are not recurring revenue... because you pay once for the course and honestly it's like goodbye" — verbatim in `transcript-zero-to-1m.txt`.
- **VERIFIED** — "people have the tendency to listen to a podcast or see something on Instagram and then like completely change their strategy" — verbatim in `transcript-zero-to-1m.txt`.
- **VERIFIED** — "A lot of people are concerned if I post too much then I'm going to like overwhelm my audience" — verbatim in `transcript-zero-to-1m.txt`.
- **VERIFIED** — "the reason why I'm 100% confident in this path when you invest first in building a brand, you have so many more opportunities for monetization that open up" — verbatim in `transcript-zero-to-1m.txt`.
- **VERIFIED** — "anybody can come into your community and honestly just clone all of your courses. But it's very difficult to clone the people in your community and the wins and success that they're having" — verbatim in `transcript-zero-to-1m.txt`.
- **VERIFIED** — "there's a lot of excitements in the market and there's a lot of money flowing into something already... those dollars are going into educating your potential customers and prospects" — verbatim in `transcript-zero-to-1m.txt`.
- **VERIFIED** — "in 99% of the failed stories I hear about, truthfully, the entrepreneur would have been successful if they just did things in the right order and stuck with it for longer" — verbatim in `transcript-zero-to-1m.txt`.
- **VERIFIED** — "Competitors can copy your curriculum; they can't copy your members' wins" — verbatim in `extraction-report.md` (Hidden Knowledge #3), itself a direct synthesis of the transcript's moat language.
- **VERIFIED** — Skool platform has "over 20 million users" — verbatim in `transcript-zero-to-1m.txt`.
- **VERIFIED** — the $50K/month-in-6-months entrepreneur example: "I recently saw one entrepreneur go from zero to $50,000 per month in 6 months" — verbatim in `transcript-zero-to-1m.txt`.
- **VERIFIED** — $50/month starting community price: "usually you'll start at something low like let's say 50 bucks per month" — verbatim in `transcript-zero-to-1m.txt`.
- **VERIFIED** — Sabrina's self-framing: "By the way, I am not a guru" and "I previously built and sold an AI company for millions of dollars" — verbatim in `transcript-zero-to-1m.txt`.
- **LIKELY** — "built AI SaaS to $1M+" (as stated in `extraction-report.md` and echoed in `SKILL.md`'s description) — the transcript itself only says "sold an AI company for millions of dollars," not an exact "$1M+" figure; the extraction report's rounding is a reasonable but not verbatim inference.
- **UNCONFIRMED** — "sabrina.dev" as her platform, and "now teaching 1 million people AI at sabrina.dev" (`SKILL.md` description; also named in `genius.md` Hall of Fame Exemplar #2) — this URL and the "1 million people" framing do **not** appear anywhere in `transcript-zero-to-1m.txt`. The transcript says only "now I teach AI 100% for free to millions of people," with no domain named. This claim predates this repair pass (pre-existing content, left in place per additive-only boundaries) and could not be corroborated against the one source file available to this worker — flagged here rather than silently treated as fact.
- **LIKELY** — the YouTube URL `https://www.youtube.com/watch?v=WvsWbgE_kWg` as the transcript's true origin — taken from the transcript file's own header metadata, not independently re-fetched/re-watched by this repair pass.

## Gap Named

No archive scan of `_archive/claude-export-2026-07-01.tar.gz` was required: `extractions/sabrina-ramonov/`
contained the primary transcript and a prior extraction report directly, so absence was never
claimed for any quote used in this repair. The one open gap is the `sabrina.dev` / "1 million
people" claim above, which is pre-existing skill content (not introduced by this repair) and is
UNCONFIRMED against the only source file on file for this expert.
