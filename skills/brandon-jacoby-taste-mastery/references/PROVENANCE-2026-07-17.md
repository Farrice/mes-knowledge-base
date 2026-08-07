# Provenance: brandon-jacoby-taste-mastery repair

All anchors trace to two files, both verified present via direct read + `wc -c` on 2026-07-17 (no root-level `extractions/brandon-jacoby-taste-mastery/` exists; the repo's live copy is under the codex-harvest mirror):

- `_active/harness/codex-harvest-2026-06-11/extractions/brandon-jacoby-taste-mastery/transcript.txt` — 56,449 bytes
- `_active/harness/codex-harvest-2026-06-11/extractions/brandon-jacoby-taste-mastery/source-metadata.md` — 741 bytes

Every quote inserted into `genius.md` (Core Genius, Master Principle, Genius Patterns 1-10, Signature Moves, Anti-Patterns, Verbatim Exemplars, Stacking Notes) is an exact contiguous substring of `transcript.txt`, checked by manual string comparison against the full transcript read into context during this repair. Full claim-by-claim table with VERIFIED/LIKELY/UNCONFIRMED labels: `references/source-ledger.md`.

No anchor in this repair depends on inference, paraphrase-as-quote, or an unread file. Two items are explicitly flagged UNCONFIRMED rather than silently asserted: the video's original publish date (not in source-metadata.md), and the accuracy of Jacoby's "two-thirds of the world" iPhone-ownership figure as an external fact (the quote itself is verified; the underlying statistic was not independently fact-checked).
