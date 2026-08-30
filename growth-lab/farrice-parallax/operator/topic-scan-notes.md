# Operator notes — topic-scan / topic-buckets (client copies purity-scrubbed)

## Refresh
- Pack: `python3 execution/outlier_radar.py refresh --niche farrice-parallax` (ttl_days 45 on this artifact)
- Re-run workflow: `gb-topic-scan` → re-render: `python3 execution/render_brief.py growth-lab/farrice-parallax/exports/briefs/topic-scan.json --out-dir growth-lab/farrice-parallax/exports --client --no-index`; sync top-level; re-bake PDF. Interactive `exports/topic-scan.html` is hand-maintained.

## Tier ledger
- data_tier: fresh · pack generated 2026-08-27T19:38:33Z · produced 2026-08-27T21:10:00Z · ttl 45d
- Run receipt: `.agent/outlier-radar/receipts/farrice-parallax-2026-08-27-123632.json` (removed from client export row).

## [NEED] / pending items
- Velocity trend per bucket: snapshots 64 minutes apart are unreadable; needs a ≥24h second snapshot before any velocity claim.
- Conversion evidence: the scan sees views, not conversions — bucket "working =" lines are the observable proxies until DMs are logged.

## First-sale recalibration checklist
- [ ] After batch 1: check ≥30% of engagers are Rings 2–4 for the reach bucket before keeping it.
- [ ] Bucket demotion only after batches 2–3, never on a 24-hour read.
