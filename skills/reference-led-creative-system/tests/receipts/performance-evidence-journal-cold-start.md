# Performance Evidence Journal Cold-Start Replay

## Purpose

Prove that the original three Refero directions can be recovered into a visible local choice surface instead of relying on remote Markdown hotlinks.

## Good Example

- Performance Evidence Journal — Alpine Bio
- Peak State Cinema — 21 TSI
- Private Performance House — Oura

The source UUIDs and preview URLs are preserved in `../fixtures/performance-evidence-journal.json`.

## Primary Failure Class

`code/workflow regression` — the prior user-facing choice surface embedded remote Refero image URLs. Those URLs remained useful as provenance but did not render for the user, so the visual decision was made from names and recommendation rather than inspectable evidence.

## Before

- Three remote image hotlinks
- No local copies
- No contact sheet
- No visibility receipt
- The workflow could ask for a choice even when the images were not visible

## After

- Three local 1440 × 900 JPEG previews
- One local contact sheet
- SHA-256 checksums for every image
- Deterministic verification of file presence, image readability, dimensions, and checksums
- Choice gate remains `VISIBLE · UNCHOSEN` until a human verdict is actually made

## Replay

```bash
python3 skills/reference-led-creative-system/scripts/direction_pack.py capture \
  --manifest skills/reference-led-creative-system/tests/fixtures/performance-evidence-journal.json \
  --output-dir .tmp/reference-led-creative-system/performance-evidence-journal-cold-start

python3 skills/reference-led-creative-system/scripts/direction_pack.py verify \
  --manifest skills/reference-led-creative-system/tests/fixtures/performance-evidence-journal.json \
  --output-dir .tmp/reference-led-creative-system/performance-evidence-journal-cold-start
```

## Result

`PASS — 3 local previews + contact sheet verified`

- Alpine Bio normalized checksum: `2202e9478f796b732ce72a40339f9aa27591a88879401dced2d542d0e3f22eef`
- 21 TSI normalized checksum: `282939d54ce5cf1ee5dbff942aa6f32d9ac9970390d28e2c9c447d6a34f64802`
- Oura normalized checksum: `c2c75d66639c61bb957564611ea81dec3bc1320385ffa2b23771b721513991bc`
- Contact-sheet checksum: `6af84c17f035b7abdf992b0d97993b5c09b285dae258c115be506f733db0707a`

The local artifacts live under `.tmp/` and are intentionally regenerated rather than committed. The manifest and this receipt are the durable replay evidence.

## Negative Control

The automated test supplies a remote-only manifest with `--no-network`. The capture must return a failure and create no valid direction pack. This proves the system rejects an invisible decision surface rather than silently claiming success.

## Proof Boundary

This receipt proves local visibility, integrity, and replayability. It does not prove that the selected direction is the strongest taste choice, fits a future brand, or improves market performance. Those require human review and project-specific evidence.
