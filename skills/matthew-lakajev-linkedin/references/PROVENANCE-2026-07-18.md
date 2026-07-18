# Provenance — Anti-Pattern Anchors (matthew-lakajev-linkedin)

All 20 source files below are pasted YouTube-transcript conversations recovered from
`_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, verified non-empty),
path prefix `claude-export/normalized/conversations/`. Found via a full byte-level
tarfile scan (7,719 members, name-fragment match `lakajev` / `sixfigure creators`, no
punctuation), not filename search alone. Extracted copies used for this repair sit in
this worker's scratchpad only; nothing was written back to `_archive/` or `extractions/`.

| Anchor (genius.md Anti-Patterns bullet) | Source conversation | Source file (tar member) | created | Size (bytes, extracted copy) | Location |
|---|---|---|---|---|---|
| 1. "Never start a newsletter" | Matthew K: If I started on LinkedIn from 0, here's what I'd do | .../1a379676-f87a-4cd3-bc3c-9d0ae610ea5e.md | 2025-03-12T00:55:08Z | wc -c = 33,984 | transcript timestamp ~33:44-33:50 |
| 2. "Never use a calendar link as primary CTA" | (same conversation) | .../1a379676-f87a-4cd3-bc3c-9d0ae610ea5e.md | 2025-03-12T00:55:08Z | 33,984 | ~11:10-11:14 |
| 3. "Never launch an offer without PMF" | (same conversation) | .../1a379676-f87a-4cd3-bc3c-9d0ae610ea5e.md | 2025-03-12T00:55:08Z | 33,984 | ~3:37-3:43 |
| 4. "Never invent a new category (sell a vitamin)" | Matthew Lakajev \| How to create an offer to sell on LinkedIn | .../78f0523c-8d9f-4eae-9f59-6b613851aa42.md | 2026-01-28T13:22:56Z | wc -c = 47,663 | "painkiller not vitamin" passage, early-section |
| 5. "Never open with cold outreach" | Mattew Lakajev \| How To Get Your First Client On LinkedIn - FREE 4 HOUR FULL COURSE | .../8ff69dde-4fe4-4a84-9b3a-ecafba07dde6.md | 2026-01-12T04:49:13Z | wc -c = 42,155 | "December 2022... cold cold outreach" passage |
| 6. "Never rush a high-C prospect" | Matthew Lakajev: How I sell on LinkedIn using Ai & Brain Chemistry | .../21bd3a63-31cc-4ae9-bb57-ee7676763c32.md | 2025-05-29T06:38:18Z | wc -c = 21,203 | ~11:43-11:48 |
| 7. "Never run a dodgy/unprofessional profile photo" | Matthew Lakajev \| How to build trust and sell online | .../a0c86979-2464-4b3f-92a2-83d09f2b76da.md | 2026-01-29T14:40:56Z | wc -c = 62,041 | "dodgy ass photo that's all grayed out" passage |

## Verification method (per ENVELOPE.md discipline)

1. Name-fragment search without punctuation: `'lakajev' in member.name.lower()` — 0
   filename hits (conversation IDs are UUIDs, not descriptive filenames).
2. Content scan, not name-only: opened every member <5MB (7,719 total) via Python
   `tarfile`, read bytes, checked `b'lakajev' in data.lower()` — 20 hits, all `.md`
   conversation exports.
3. Sizes recorded via `wc -c` equivalent (Python `len(data)`) on the extracted copies
   before any quote was pulled — confirms these are real, populated transcripts, not
   empty/truncated files.
4. Every quote used in genius.md's Anti-Patterns section was located by direct string
   search inside the extracted file text (not paraphrased from memory) before being
   copied verbatim into the skill.
5. One claim ("Golden Gaytime" email story, pre-existing in genius.md before this
   repair) was searched for across the FULL archive (all 7,719 members, not just the 20
   Lakajev-tagged ones) and returned zero hits — labeled UNCONFIRMED in
   `references/source-ledger.md`, not silently dropped.
