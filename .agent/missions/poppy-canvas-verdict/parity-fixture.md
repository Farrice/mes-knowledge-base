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

## Jen board, observed 2026-09-10 (Chrome read-only screenshot, board "Salmon Jackal")
- Sources: IG / TikTok / YouTube cards — reels, "The Instagram DM Strategy For Re…", "The 6 Figure DM Script"; an Auto Refresh profile node (creator feed that re-pulls).
- Chat: two conversations, "Homebuyer Con…" and "Instagram Agen…"; Sonnet 5 High; skill "Jen Santulan | SFV…" attached from the vault.
- Reply shape (verbatim fragments): beat-labelled annotated draft ("[DE-RISKED CTA] → tell me your number, i'll tell you your zip code. dm me BUYER"), then "Clean final version (what actually goes in Canva)", then "Reusable-beats flag — e.g. the PRINCIPLE line works alone as a caption closer or quote graphic; AHA #1+#2 could become a standalone comment-bait stat post."
- Claude's closer: "just tell me the format + topic and I'll always generate both versions this way — annotated so you can diagnose/remix, and clean so you can paste immediately… saved as a skill in the vault."
- Read: the thing that made it work = one saved skill (system prompt) + always-on sources + iterate in one thread. Maps to: per-chat-node system prompt on /canvas + profile node + one board per client.

### Screen 2 — "Homebuyer Content …" conversation, expanded (2026-09-10)
Content matrix Claude built (rows = buyer segment, cols = pillar). Cells observed:
| segment | Myth-Bust | Neighborhood/Numbers | Programs/Proof | Personal |
|---|---|---|---|---|
| Rent-trapped renter | "20% down is a myth" | Reseda/Panorama City price tiers | rent vs buy exact math | — |
| Space-starved family | "you need a mansion to have a yard" | Sylmar/Winnetka ADU stock | cost of waiting 1 year with a growing family | toddler-mom content |
| Gig/1099 earner | "self-employed = disqualified" myth | — | how lenders calculate 1099 income | — |
| Family-pooled buyer | "gift funds are complicated" myth | Pacoima/San Fernando | how FHA/CalHFA treat gift funds | community/family content |
| Move-up alumni | — | — | referral proof, "5 years later" case study | client success story |
| Raver/music parent crossover | — | — | — | My.BPM x realtor life crossover content |
Closer: "This is the format-agnostic engine — every cell can become a carousel, a B-roll+text reel, a 40-50 sec yap, or a listing/motion video. Refresh one real number monthly (a new FHA limit, a new median price, a new grant deadline) and the matrix never runs dry."
Conversations in this chat: "Homebuyer Content …", "Instagram Agent Pos…". Skill attached: "Jen Santulan | SFV …". Model: Sonnet 5 High.

## Run 2 — 2026-09-10, board `jen-sfv` (YOUR fixture: the Poppy Jen thread, read in full)
Inputs: the 5 videos from the Poppy board (Broke Agent ×2, Nicolas Cole, SooWei Goh, Kallaway) + Jen voice profile as a note. Full Poppy thread + second conversation saved beside this file.
Ask: your Poppy asks 2, 3, 4 verbatim + the beat-map master prompt Poppy saved as a skill.
| step | Poppy (his thread) | Canvas |
|---|---|---|
| ingest 5 videos | credits | 7.4 s, $0 |
| context | their cap | 77K tokens actual (est. undercounted at 50K) |
| reply | streamed, Sonnet 5 High, iterative over ~9 turns | one shot, 355 s, est $5.13 on the Claude plan |
| output | 4 carousels annotated + clean, avatars, language bank, matrix, Notion vault (27 pages), saved skill | 4 carousels annotated + clean, Cole niche breakdown, 3 ICP dossiers + 2 bonus, verbatim map, 5 pillars, mapping matrix, insight vault |
| cited sources | calhfa ×6, mortgage sites (web search on) | [S1]–[S5] inline; every $ figure marked [UNCONFIRMED] — no web tool in the seat |
| voice discipline | lowercase, warm; used "your first home" freely | flagged voice card's banned phrase "your first home" and the $800K+ vs first-time-buyer conflict, resolved from her audience_awareness field — Poppy never caught either |
| miss vs Poppy | — | live numbers (FHA limit, CalHFA caps, medians) and the Notion push |
Bug found + fixed: `claude -p` thrashed on a 77K prompt at effort high because ~/.claude/settings.json sets CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=50; the seat now runs with DISABLE_AUTO_COMPACT=1.
Verdict on the run: same mechanism, stricter grounding, slower. The one capability gap is web research inside the chat seat (Poppy's Sonnet searched; ours was tools-off). That is a `--tools WebSearch,WebFetch` toggle per chat node, not a rebuild.
