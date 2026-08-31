# Operator notes — format-playbook + format-matrix (client copies purity-scrubbed)

## Refresh
- Pack: `python3 execution/outlier_radar.py refresh --niche farrice-parallax` (ttl_days 60)
- Re-run workflow: `gb-format-find` → re-render: `python3 execution/render_brief.py growth-lab/farrice-parallax/exports/briefs/format-playbook.json --out-dir growth-lab/farrice-parallax/exports --client --no-index`; sync top-level; re-bake PDF. Interactive `exports/format-matrix.html` is hand-maintained.

## Tier ledger
- data_tier: fresh · pack generated 2026-08-27T19:38:33Z · produced 2026-08-27T21:40:00Z · ttl 60d

## Pending
- Matrix rows marked "OPEN · invented row" (The Witness) are labeled bets, not measured pairs — 0 specimen links by design; they harden or die on batch results.

## First-sale recalibration checklist
- [ ] After 2 batches: score the 3 picks (2 proven pairs + 1 labeled bet) on outlier multiplier vs channel baseline; kill the bet if it never clears 3×.
