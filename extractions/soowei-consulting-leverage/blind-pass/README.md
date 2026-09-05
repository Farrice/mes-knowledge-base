# SooWei A-Tier Blind Pass

Status: **READY FOR HUMAN JUDGMENT — verdict pending**

## State

- Reference corpus: READY, 2/2.
- Generator packet: SEALED.
- Contracted workflow candidates: COMPLETE, 2/2.
- Matched-form spoken specimens: COMPLETE, 2/2.
- Clean-room access audit: PASS.
- Randomized side-by-side comparison: READY, 2/2.
- Farrice verdict: NOT RECORDED.
- Integration: HELD.

## Files

- `generator-packet.md` — the sealed workflow-artifact brief a fresh generator receives.
- `matched-form-addendum.md` — the sealed format-matching correction, run in the same clean room with no new reads.
- `source-integrity-audit.md` — provenance, completeness, hashes, and contamination receipt.
- `generated/` — two workflow artifacts plus two matched-form transcript specimens.
- `review/judgment-sheet.md` — the live A-tier comparison surface.
- `review/assembly-receipt.md` — normalization, randomization, and public hashes without identity disclosure.
- `.sealed-mapping.json` — randomized identity key; do not open before Farrice records the verdict.

## Required Sequence

1. Open `review/judgment-sheet.md`; do not open `.sealed-mapping.json`.
2. Read both samples in Pair 1 and score them.
3. Read both samples in Pair 2 and score them.
4. Record preferred sample, real-SooWei guess, weakest tell, and PASS/FAIL.
5. Only after Farrice submits the judgment, reveal the mapping and record the verdict.

Do not run `blind_pass.py record` or reveal the mapping from a corpus-ready result alone.
