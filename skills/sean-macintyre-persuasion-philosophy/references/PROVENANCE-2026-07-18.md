# PROVENANCE — sean-macintyre-persuasion-philosophy repair (Wave 3 Lane 4 Batch 15)

Anchor → source file + location table. Ground truth = `extractions/sean-macintyre/` (found on first `ls extractions/ | grep -i macintyre` — no archive-tarball scan needed; the extraction was present and non-empty, confirmed with `wc -c`).

| # | Anchor text (as written in genius.md) | Source file | Location |
|---|---|---|---|
| 1 | "Why are you using problem agitate solution when the market's already level four sophistication? ... why don't you use a mechanism lead or something" | `extractions/sean-macintyre/transcript-consolidated.md` | line 57 (00:17:21-00:17:34) |
| 2 | "If you come up with it out of thin air, the second people start digging, they don't find any substance and then they're like their ad skepticism" | `extractions/sean-macintyre/transcript-consolidated.md` | line 43 (00:09:19-00:09:29) |
| 3 | "David is looking to music and seeing, okay, what can I learn from this field that I can apply to my copy to make it better?" | `extractions/sean-macintyre/transcript-consolidated.md` | line 171 (01:13:49-01:15:10) |
| 4 | "[Hormozi's books] are great if you are selling something that people already want. They are not great if you're reaching somebody who doesn't realize they have a problem" | `extractions/sean-macintyre/transcript-consolidated.md` | line 29 (00:05:25-00:05:44) |
| 5 | "a realization smacked me in the face like a wet bag of burritos..." | `extractions/sean-macintyre/transcript-consolidated.md` | line 101 (00:40:12-00:40:21) |
| 6 | "What if I just not spend that and go read a goddamn book?" | `extractions/sean-macintyre/transcript-consolidated.md` | line 173 (01:15:32-01:16:20) |
| 7 | "every time you inspire yourself about a particular topic, diminishing returns..." | `extractions/sean-macintyre/transcript-consolidated.md` | line 139 (01:00:12-01:00:25) |
| 8 | "I'm not enjoying Spanish anymore when I was just learning it" | `extractions/sean-macintyre/transcript-consolidated.md` | line 185 (01:22:47-01:23:22) |
| 9 | "...only gets you through the first five pages of a 70-page promo" | `extractions/sean-macintyre/transcript-consolidated.md` | line 15 (00:01:06-00:01:47) |
| 10 | "It's only for some people that habit eventually transmogrifies into passion..." | `extractions/sean-macintyre/transcript-consolidated.md` | line 143 (01:01:47) |
| 11 | Interview title, host, date, video ID | `extractions/sean-macintyre/source-metadata.md` | lines 1-16 |

## Source-search discipline followed

- `ls extractions/ | grep -i -E "macintyre|mcintyre"` → hit on first try: `extractions/sean-macintyre/`.
- File sizes recorded with `wc -c` (never `wc -l`): `transcript-consolidated.md` = 37,446 bytes; `source-metadata.md` = 1,933 bytes. Both well above zero — no "unrecoverable/0-byte" claim needed, so the `_archive/claude-export-2026-07-01.tar.gz` fallback scan was not required.
- Every quote used in the Anti-Patterns rewrite was located verbatim in `transcript-consolidated.md` via `grep -n` before being placed in genius.md (see `references/source-ledger.md` claim table).
- The one anti-pattern item without a direct verbatim Sean quote ("citing cross-domain references without applying them") is labeled as an inference in `references/source-ledger.md`, not dressed up as a direct quote.
