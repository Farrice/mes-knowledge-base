# PROVENANCE — dan-bolton-coaching-offers repair

Anchor → source file/location table for every new claim/anchor added in this repair pass
(genius.md Anti-Patterns section + references/source-ledger.md). Full claim-by-claim
ledger for pre-existing pattern content lives in `references/source-ledger.md`; this file
is the compact anchor index.

| Anchor used in genius.md | Points to | Verified how |
|---|---|---|
| "Shutting Down a $100k a Month (Profit) Coaching Business w/ Dan Bolton" (YouTube, youtube.com/watch?v=RgPeMjbEJtM) | Real YouTube video, title confirmed | WebSearch (2026-07-17) surfaced the title; WebFetch on the URL returned only page chrome, not transcript — title-level VERIFIED, content-level UNCONFIRMED |
| Zander Fryer podcast, "032: Dan Bolton — Rising from Rock-Bottom," zanderfryer.com/podcast/032-dan-bolton-rising-from-rock-bottom/, 2021-09 | Real podcast episode, show-notes text | WebFetch on the URL returned the show description and "key learning points" verbatim as published on the site |
| danbolton.co, "you. me. 8 weeks. magic." $8,000 offer | Real live website | WebFetch on danbolton.co returned this offer text directly |
| "Scale School with Dan Bolton" podcast, podcasts.apple.com/podcast/scale-school-with-dan-bolton/id1671250753 | Real, ongoing podcast series | Existence confirmed via WebSearch; episodes not individually opened |
| `extractions/dan-bolton*` absence claim | No such file/dir | `ls extractions/ | grep -i bolton` (0 results, 193 total entries checked) + `grep -ril bolton extractions/` (0 results) |
| `_active/harness/codex-harvest-2026-06-11/extractions/` absence claim | No such file | `ls _active/harness/codex-harvest-2026-06-11/extractions/ | grep -i bolton` (0 results) |
| `_archive/claude-export-2026-07-01.tar.gz` absence claim | No filename match inside archive | `wc -c` → 332,779,255 bytes (real, non-empty); `tar tzf ... | grep -i bolton` → 0 results |
| Pre-existing genius.md claims (Three I Framework name, client Jason $103K, 700+ GPT chats, "bored out of my brains," Coach-the-Gut quotes, mini-VSL 10,000-views/4-hour-shoot figures) | Unresolved — no primary source located | Multiple WebSearch queries (Three I Framework, mini-VSL, GPT infrastructure, co-creation) returned no matches to Bolton specifically; carried forward as UNCONFIRMED per the envelope's Rule 1 (no quote gets a fabricated anchor) |

No quote in the new Anti-Patterns section was invented — every bullet either cites a
directly-fetched external source (S1–S3 in the source ledger) or explicitly labels itself
as carried-forward pre-existing content with an UNCONFIRMED tag and the absence-check
evidence inline.
