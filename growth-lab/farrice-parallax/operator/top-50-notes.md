# Operator notes — top-50 (client copy purity-scrubbed)

## Refresh
- Pack: `python3 execution/outlier_radar.py refresh --niche farrice-parallax` (ttl_days 45)
- Produced by workflow `gb-topic-scan` alongside topic-buckets. `exports/top-50-client.html` is hand-maintained (no brief JSON) — edit it directly, then re-bake its PDF via `execution/export_growth_package.py pdf`.

## Consumers + provenance (moved out of top-50.md by the 2026-08-28 register pass)
- Read by: gb-format-find, gb-blueprint (+ Wave-2: engine-builder, topic-brainstormer, video-maker).
- Source pack: `.agent/outlier-radar/packs/farrice-parallax/latest.json` · generated_at 2026-08-27T19:38:33Z · run receipt: `.agent/outlier-radar/receipts/farrice-parallax-2026-08-27-123632.json` · lookback: each channel's recent uploads (flat dump, cap per channel), scored against its own baseline. Pack caps ranked rows at 50 — no backfill pool beyond it.

## Tier ledger
- data_tier: fresh · pack generated 2026-08-27T19:38:33Z · produced 2026-08-27T21:10:00Z · ttl 45d
- Client chip now reads "evidence current as of Aug 27, 2026" (was "Data tier: FRESH").
- Verified 2026-08-27: all 50 rows carry pack video ids + URLs; multipliers and comma-formatted views match `.agent/outlier-radar/packs/farrice-parallax/latest.json` exactly.

## Pending
- Velocity column: pending a second pack snapshot ≥24h out (current snapshots 64 min apart).

## First-sale recalibration checklist
- [ ] On refresh, struck rows (25) keep their strike reasons — re-check them against the new pack rather than regenerating blind.
