# PROVENANCE — seena-rez-tiktok-commerce repair (Wave 3 Lane 4 Batch 15)

No `extractions/` directory exists for this skill (checked: `ls extractions/ |
grep -i seena`, `ls extractions/ | grep -i rez` — zero results). Ground truth
was recovered from `_archive/claude-export-2026-07-01.tar.gz` (332,779,255
bytes) via a Python `tarfile` per-member content scan (see method below).
Every quote placed in `genius.md` was located verbatim in the extracted
member with `grep -n` before use — line numbers below are from the extracted
`.md` file, matched against the tarball path.

## Method

1. `ls extractions/ | grep -i "seena\|rez"` → no matches.
2. Wrote a Python script using `tarfile.open(path, "r:gz")`, iterated all
   7,720 members, read each file's raw bytes, regex-searched for
   `seena|rez|high smile|hyperdopamine|psaep` (case-insensitive, byte-level,
   not filename-based). 13 members matched.
3. Extracted the 9 conversation-scoped matches (`claude-export/normalized/
   conversations/*.md`) with `tf.extractfile(member).read()`, wrote to
   scratchpad, recorded byte sizes with Python's `len(data)` (equivalent to
   `wc -c`, never `wc -l` — these are single-paragraph transcript files that
   would misleadingly read as ~30 lines despite tens of thousands of words).
4. Read each extracted file in full; identified 3 primary sources (S1, S2,
   S3 below) as genuine YouTube-transcript extraction conversations with
   real video titles, YouTube URLs, and Claude.ai MES 3.0 extraction
   timestamps from Jan-Feb 2026.
5. Every quote used in `genius.md` was grep-verified against the extracted
   file text before being written — table below cites file + line number
   for each.

## Anchor → Source Table

| Anchor text (as it appears in genius.md) | Source file (tar path) | Line | Video title / date |
|---|---|---|---|
| "But you know what's also based upon real science?" | `claude-export/normalized/conversations/b6ee8a13-8ddc-4130-ba5d-8471c4b8b5c7.md` | 30 | "$1.8m tiktok dropshipping in 30 days," 2026-01-05 |
| "Apparently, the aging filter is based upon real science." | same file | 30 | same |
| "Since our text is going to turn white, we don't want it to be white. So, we're going to turn into yellow." | same file | 30 | same |
| "Basically just putting it all over the screen very quickly. People will assume that this stuff is legit." | same file | 30 | same |
| "5% of the people who visited my store out of 700,000 bought my product." | same file | 30 | same |
| "It was only the 1.4 and the 1.8 million video that went viral." | same file | 30 | same |
| "this is the mistake that most people make when they're creating Tik Tok videos... 'I guess now what I have to do is come up with a completely new video idea.' Wrong. That is a mistake." | same file | 30 | same |
| "make sure not to be a noob and do this. It's what a noob does. This is what a pro does. They create variations." | same file | 30 | same |
| "you literally just have to do 0.1% of what they were able to do" | same file | 30 | same |
| "Sounds good in theory, but we do not want to do this. It adds complexity that we're not really looking for." | `claude-export/normalized/conversations/aa769dc9-d497-4189-9400-5cf55a42b865.md` | 30 | "$49,140 tiktok dropshipping in 7 days from scratch," 2026-01-05 |
| "Most people have you think that you need to spend $200 on a paid Shopify theme or get a web designer. A lot of those people are trying to give you their affiliate link, I believe." | same file | 30 | same |
| "I haven't sold the product yet. I haven't even named the product yet. I'm using its conventional name, not my brand name. This is because I don't want the content to seem like an ad." | same file | 30 | same |
| "You don't want to go any lower than 3:1." | same file | 30 | same |
| "You don't want to be getting into a stagnating or declining market because there's no opportunity there." | `claude-export/normalized/conversations/a9726445-2215-4e8e-af15-c125a7073060.md` | 30 | "how I built a $2.7M brand using a.i," 2026-02-05 |

## Files searched but not used as anchors (recorded, not silently dropped)

| File | Size (`wc -c` equivalent) | Why not cited |
|---|---|---|
| `claude-export/normalized/conversations/5010ad67-e3de-4aa0-b715-2df2a8872701.md` | 6,969 bytes | Prompt-continuation scaffolding for S1, no new transcript content. |
| `claude-export/normalized/conversations/ece83bcc-5004-481a-a086-125f6438e75a.md` | 12,864 bytes | Same — continuation of S1's crown-jewel prompt generation, no new factual claims. |
| `claude-export/normalized/conversations/8db41cd0-017d-4397-9bb9-2ce427feea80.md` | 49,712 bytes | Duplicate extraction pass over the same transcript as S3; read in full, cross-checked, no unique quotes taken from it. |
| `claude-export/normalized/conversations/5ac8b179-fbd9-4a7d-9bfa-1d1186207997.md` | 31,255 bytes | Mentions "Seena Rez" only as one of several named extraction arsenals in an unrelated integration-planning conversation; no transcript content. |
| `claude-export/normalized/conversations/7778381e-dd03-4ea9-af31-9fec6326fefc.md` | 158,057 bytes | Matched on `\brez\b` (a stray word match, not "Seena Rez" — verified false positive: "unlock the Pria Seena which is the is a" appears at a different context, unrelated content). |
| `claude-export/normalized/conversations/84baadf5-c791-44c2-a71a-4ff537d919fa.md` | 2,070 bytes | Meta-conversation asking Claude to list prior Seena Rez conversation URLs — used only to cross-confirm S1/S2/S3 exist as real threads, not quoted. |
| `claude-export/raw/batch-0001/conversations.json` | 867,859,945 bytes | Raw un-normalized export containing every conversation in the archive (superset of the normalized files above); not opened directly — the normalized `.md` files are the readable, line-addressable form of the same data. |

## UNCONFIRMED items (no anchor exists — flagged, not fabricated)

- Numeric "Success Metric" thresholds on all 14 Genius Patterns (e.g. "50%+
  retention past 3-second mark," "3%+ click-through rate," "Paid ROAS above
  3x," "10x average view count") — searched all 3 primary transcripts for
  these figures; not present verbatim. Labeled UNCONFIRMED in
  `references/source-ledger.md`, left in place as practitioner targets
  (additive-first — not deleted), but must not be attributed to Seena Rez as
  his own stated numbers in downstream output.
- The three "Hall of Fame Exemplars" ("YouthRestore Serum," "Celebrity Secret
  Jawline Tool," "Generic Coffee Maker Ad") — composite teaching examples
  from the original extraction, no matching product/brand found in S1/S2/S3.
  Labeled UNCONFIRMED.
