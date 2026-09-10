# Parity fixture — "the Poppy job"

Stand-in until Farrice grants a look at his Poppy tab or names his real URLs + ask
(packet 1). Built from the job he described: feed a creator's videos into a chat,
have it read them without him explaining anything, then write in that pattern.

## Inputs
Alex Hormozi, four latest long-form videos (pulled free by `yt-dlp --flat-playlist` in 1 s):
- https://www.youtube.com/watch?v=uaLNfijnp-8 — "This Video Should Be Required Viewing for Business" (37 min)
- https://www.youtube.com/watch?v=o64cI6tebnU — "How I Would Build a $10M Service Business" (27 min)
- https://www.youtube.com/watch?v=SCi464zfAUM — "If I Started A Personal Brand In 2026" (14 min)
- https://www.youtube.com/watch?v=mRlSb0O5QNU — "How to Get Rich for Service-Based Businesses" (39 min)

## The ask (verbatim, one chat node, Sonnet / medium)
"These are Alex Hormozi's four latest videos. 1) What hook structure do the openings share — quote the first line of each. 2) Write three new hooks in that exact structure for a solo brand strategist selling a $2,500 ten-day sprint to supplement brands. Keep it under 200 words."

## A good answer contains
- The actual first lines, quoted, not paraphrased
- The pattern named in one line
- Three hooks that keep the structure and swap the subject
- Any transcript garble flagged rather than repeated as fact

## Run 1 — 2026-09-10, board `hormozi-test`
| step | result |
|---|---|
| ingest 4 videos | 16 s total (11.3 / 1.6 / 1.2 / 1.6 s), 34,380 tokens of context |
| reply | 15.2 s, Sonnet medium, est $0.32 on the Claude plan |
| quoted first lines | yes — "I'm about to help a complete stranger build a $15 million per year business." (S1), $7M (S2), and flagged S4's "$55 per year" as a caption garble |
| pattern | "[I'm about to / going to] help a complete stranger build a $X business" + timeframe check-in |
| three hooks | delivered, structure held, subject swapped to the $2,500 sprint |
| felt gap vs Poppy | reply arrives whole after 15 s instead of streaming; no thumbnails on the source cards |

Verdict on the run: the mechanism is the same as Poppy's. What differs is polish, not capability.
