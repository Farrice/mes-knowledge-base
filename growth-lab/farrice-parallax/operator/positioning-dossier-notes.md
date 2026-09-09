# Operator notes — positioning-dossier (client copies are purity-scrubbed; this file keeps the system language)

## Refresh
- Pack: `python3 execution/outlier_radar.py refresh --niche farrice-parallax` (TTL 12h; artifact ttl_days 90)
- Re-run workflow: `gb-interview` → re-render client form: `python3 execution/render_brief.py growth-lab/farrice-parallax/exports/briefs/positioning-dossier.json --out-dir growth-lab/farrice-parallax/exports --client --no-index`, then copy `exports/positioning-dossier/positioning-dossier-brief-client.html` over `exports/positioning-dossier-client.html` and re-bake the PDF via `execution/export_growth_package.py pdf`.

## Tier ledger
- data_tier: fresh · pack `.agent/outlier-radar/packs/farrice-parallax/latest.json` generated 2026-08-27T19:38:33Z · produced 2026-08-27T19:55:00Z · ttl 90d
- Coverage: YouTube measured; TikTok/IG none; LinkedIn outside radar. Client copies say "evidence current as of Aug 27, 2026" — that maps to this ledger row.

## [NEED] items (removed from client copies as "pending" language)
- Real close-rate and pipeline numbers: 0 sent / 0 sold on the current ladder; every downstream lead value is list price × assumed close rate.
- Consumer-side verbatims (supplement end-buyer, seed #10): this run mined founder/operator surfaces only. Close with Amazon-review + r/Supplements mining pass.
- LinkedIn-native pain language: pack covers YouTube only; the motion is DM-led on LinkedIn. Structured pull required to close.

## First-sale recalibration checklist (lead values are MODELED until real sends)
- [ ] At first 10 sends: log outcomes per send; replace 20% inquiry→Angle Map assumption with the observed rate.
- [ ] At first sale: replace 30% Map→Sprint upgrade assumption; recompute the ~$300/qualified-inquiry figure everywhere it appears (bullseye, blueprint, 3-2-1 mix).
- [ ] Re-render all client artifacts after recalibration so no client copy still carries the assumption base.
