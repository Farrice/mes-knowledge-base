# PROVENANCE — andrew-wilkinson-ai-entrepreneurship repair

Anchor → source file/location table. Full claim-by-claim ledger with VERIFIED/LIKELY/
UNCONFIRMED labels lives in `references/source-ledger.md` — this file maps each anchor
used inside `genius.md` back to where it came from.

| Anchor used in genius.md | Points to | Verified how |
|---|---|---|
| "Every.to transcript, 2026-01-21" | https://every.to/podcast/transcript-opus-4-5-changed-how-andrew-wilkinson-works-and-lives | WebFetch of the URL, prompted for verbatim quotes; publication date confirmed in the same fetch. |
| "Lenny's Newsletter, 2025-07-03" | https://www.lennysnewsletter.com/p/ive-run-75-businesses-andrew-wilkinson | WebFetch of the URL, prompted for verbatim quotes; publication date confirmed in the same fetch. |
| "Founder's Journal, 2024-03-15" | https://foundersjournalpod.morningbrew.com/how-i-lost-10000000/ | WebFetch of the URL, prompted for verbatim quotes; publication date confirmed in the same fetch. |
| "X/@awilkinson, status 2001685012559913044" | https://x.com/awilkinson/status/2001685012559913044 | Surfaced verbatim in WebSearch result snippet (X post not independently WebFetched — X blocks unauthenticated fetch). |
| "X/@awilkinson, status 2012559525811814442" | https://x.com/awilkinson/status/2012559525811814442 | Surfaced verbatim in WebSearch result snippet. |
| "X/@awilkinson, status 1856066444678836401" | https://x.com/awilkinson/status/1856066444678836401 | Surfaced verbatim in WebSearch result snippet. |
| "Hacker News thread 33630016, 2011" | https://news.ycombinator.com/item?id=33630016 | Surfaced in WebSearch as the general-idiom source for "pennies in front of a steamroller" — used only to show the phrase's real origin is NOT Wilkinson, i.e. to justify the UNCONFIRMED label on Pattern 8 / Tacit 4. |
| `extractions/` absence claim | `extractions/` directory (repo) | `ls extractions/ | grep -i wilkinson` (no results) + `grep -ril wilkinson extractions/` (one unrelated cross-reference hit, read and confirmed unrelated) — both run 2026-07-17, logged in source-ledger.md. |
| File-size claims (SKILL.md 3866B, genius.md 12459B pre-repair, etc.) | `skills/andrew-wilkinson-ai-entrepreneurship/*` | `wc -c` on each file, run 2026-07-17, logged in source-ledger.md — confirms no file is 0-byte/corrupt, ruling out a false "unrecoverable" claim. |

## What was NOT independently re-verified

Quotes attributed to S1–S3 (Every.to, Lenny's, Founder's Journal) were extracted via
WebFetch's summarization pass over each URL, not by reading raw transcript HTML directly
in this session. This is disclosed in `references/source-ledger.md` under "Primary sources
consulted." If an adversarial verifier needs byte-exact transcript text, re-fetch the URLs
directly rather than trusting the summarized quotes as a final citation.
