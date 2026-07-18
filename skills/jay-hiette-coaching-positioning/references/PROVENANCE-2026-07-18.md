# PROVENANCE — jay-hiette-coaching-positioning repair (Wave 3 Lane 4 Batch 7)

Anchor → source table for every claim added or verified in this repair. Full source chain and absence-check detail: `source-ledger.md` in this same directory.

| Anchor (in repaired genius.md) | Source file + location | Verification method |
|---|---|---|
| Model Calibration section — "80-hour agency years," "cold outreach" | `8e18a4b6-fae7-4f41-9fe5-133a1613b3a1.md`, human turn 2026-02-04T05:49:07Z | Direct re-read of extracted transcript; matches "working 80our weeks busting my ass... doing a lot of cold outreach" |
| Model Calibration — "$500 spend → $14K in 2 weeks," "290 → 23,000 followers" | Same file | Pre-existing genius.md figures, cross-checked verbatim against transcript ("$500 in ad spend, which is a 25x return"; "290 followers to 23,000 in a very short time within a month") |
| Anti-Pattern 1 — "post more organic content... complete BS" | `8e18a4b6-...md`, same human turn (single-block transcript, no internal line numbers — transcript is one continuous paragraph) | Exact-string match confirmed via `grep` against the extracted file |
| Anti-Pattern 2 — "800,000 followers... €8,000 in a few weeks" | Same file | Exact-string match confirmed via `grep` |
| Anti-Pattern 3 — "gaining body fat, lack of leads... every time you walk in the kitchen" | Same file | Exact-string match confirmed via `grep` |
| Anti-Pattern 4 — "not running ads directly to a book call" | Same file | Exact-string match confirmed via `grep` |
| Anti-Pattern 5 — "getting clear with the foundations and the message before you integrate the ads" | Same file | Exact-string match confirmed via `grep` |
| Anti-Pattern 6 — "You copy others to try to fit in" | `a54b5e3f-2b1a-4dca-87fd-272df45486a6.md`, human turn 2026-02-22T11:53:26Z | Exact-string match confirmed via `grep` |
| Archive existence/size | `_archive/claude-export-2026-07-01.tar.gz` | `ls -la` → 332,779,255 bytes, confirmed 2026-07-17 |
| Conversation existence/size in tarball | `tar tzf` listing + `tar xzf ... -O <path> \| wc -c` | 58,164 bytes and 53,884 bytes respectively — non-empty, real content |
| `extractions/` has no Jay Hiette file | `ls extractions/ \| grep -i hiette` | No output — confirmed absent, not assumed |
| codex-harvest has no Jay Hiette content | `grep -ril "hiette" _active/codex-harvest-2026-06-11` | No output — confirmed absent, not assumed |

No quote in this repair was written without first being located verbatim in the extracted transcript text. No source was declared absent without a direct search command being run first (see Absence Check in `source-ledger.md`).
