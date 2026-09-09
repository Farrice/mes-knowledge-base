# Operator notes — bullseye (+ 3-2-1 mix, sourcing map; client copies purity-scrubbed)

## Refresh
- Pack: `python3 execution/outlier_radar.py refresh --niche farrice-parallax`
- Re-run workflow: `gb-bullseye` → re-render: `python3 execution/render_brief.py growth-lab/farrice-parallax/exports/briefs/bullseye.json --out-dir growth-lab/farrice-parallax/exports --client --no-index`; sync `exports/bullseye-client.html`; re-bake PDF. Interactive trio (`bullseye.html`, `bullseye-321-mix.html`, `bullseye-sourcing-map.html`) is hand-maintained; the 3-2-1 bench-swap state is in-page only (BUCKETS `pick` flags reset on reload — by design).

## Tier ledger
- data_tier: fresh · pack generated 2026-08-27T19:38:33Z · produced 2026-08-27T20:40:00Z · ttl 90d

## [NEED] items (client copies now say "pending"/"assumption base")
- DM-qualified-inquiry → Angle Map close rate. Placeholder: 20%. Every lead value scales linearly with it; hardens after first 10 logged sends.
- Angle Map → Sprint upgrade rate. Placeholder: 30%. Governs whether conversion buckets point at the Map or the Sprint.
- Ring 2/3 audience sizes beyond subscriber proxies. A keyword-volume pull (Gemini/Perplexity lane, pennies) would harden the size column; decides how much reach weight Ring 4 deserves.
- Velocity fields unreadable this pack (snapshots 64 minutes apart) — needs a second snapshot ≥24h out.

## First-sale recalibration checklist (values MODELED until real sends)
- [ ] First 10 sends: replace 20% close assumption with observed; recompute $300/qualified-inquiry ($750×20% + $2,500×20%×30%).
- [ ] First sale: replace 30% upgrade assumption; re-check bucket kill/keep lines (some trigger on per-batch DM counts).
- [ ] Re-render bullseye-client + growth-blueprint-client after recalibration.
