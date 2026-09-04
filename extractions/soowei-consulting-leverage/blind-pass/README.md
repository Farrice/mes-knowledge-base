# SooWei A-Tier Blind Pass

Status: **PREPARED — fresh generation and human judgment pending**

## State

- Reference corpus: READY, 2/2.
- Generator packet: SEALED.
- Generated candidates: NOT RUN.
- Side-by-side comparison: NOT RUN.
- Farrice verdict: NOT RECORDED.
- Integration: HELD.

## Files

- `generator-packet.md` — the only task brief a fresh generator receives.
- `source-integrity-audit.md` — provenance, completeness, hashes, and contamination receipt.
- `judgment-sheet.md` — the comparison rubric and verdict surface.
- `generated/` — destination for two fresh-context candidates.

## Required Sequence

1. Run the generator packet in a fresh task or explicitly authorized clean-room worker.
2. Confirm the generation receipt lists only the allowed files.
3. Place the two outputs under `generated/`.
4. Assemble each output beside its matching real piece without identifying which is real.
5. Farrice judges recognizability, decision fidelity, texture, and preference.
6. Only after Farrice says PASS, record the verdict with both generated and reference paths.

Do not run `blind_pass.py record` from a corpus-ready result alone.
