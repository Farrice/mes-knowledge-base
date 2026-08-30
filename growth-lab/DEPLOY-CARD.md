# Growth Blueprint OS — Deploy Card (cold-start safe, 2026-08-27)

Fire any of these in a fresh session. Each produces its artifact standalone (three forms: working md → `growth-lab/<niche>/`, client HTML → `exports/`, PDF via packager). State lives on disk, not in chat — any session picks up where the last left off via `/gb-orchestrate`.

## The deck

| Command | Produces | Data needed |
|---|---|---|
| `/gb-interview` | Positioning Dossier (identity-layer avatar, receipted pain bank) | none — interview + research |
| `/gb-whitespace` | Whitespace Map + Positioning Wheel | pack (fresh best) |
| `/gb-bullseye` | Bullseye + Revenue Overlay (3 visualizations) | dossier + whitespace |
| `/gb-topic-scan` | Topic Buckets + live Top-50 table | pack (required) |
| `/gb-format-find` | Format Playbook + structure×visual Matrix | top-50 |
| `/growth-blueprint` | **The flagship** — assembles everything into the sellable Content Growth Blueprint (front door; also loads the whole skill for any single ask) | all five |
| `/gb-enrich` | Data enrichment INTO the pack (demand, buyer quotes, market pulse — shows cost before spending, ~pennies) | pack; manual-fire only |
| `/gb-refresh` | Staleness + drift report, refresh order | — |
| `/gb-orchestrate` | "What's next / where was I" router | — |

## Supporting commands (terminal)

```bash
# Refresh the data pack for a niche ($0, keyless)
python3 execution/outlier_radar.py refresh --niche <slug>

# Add channels to a niche watchlist
python3 execution/outlier_radar.py add-channels --niche <slug> @handle1 @handle2

# Bake the lead magnet (step-down) from a pack
python3 execution/build_lead_magnet.py --pack .agent/outlier-radar/packs/<slug>/latest.json --niche-label "<Label>" --cta-url "<url>" --out <out.html>

# One HTML → PDF
python3 execution/export_growth_package.py pdf <file.html>

# Full client package (HTML + PDFs + client-clean CONTENTS + zip)
python3 execution/export_growth_package.py package --niche <slug>
```

## Client intake (front door — spec: `growth-lab/intake/INTAKE-ENGINE.md`)

| Command | Does |
|---|---|
| `/gb-intake` | Manual fire: intake-pack → free personalized mini → Gmail DRAFT (never sends); paid chain only on Farrice's call |

```bash
# New submissions + 48h clock (writes .agent/intake/pending.json for the Homebase line)
.venv/bin/python3 execution/intake_bridge.py status --sheet <id>    # or --csv <export.csv>

# One submission -> growth-lab/<slug>/intake-pack.md (frozen shape) + manifest block + fire commands
.venv/bin/python3 execution/intake_bridge.py pull --row N --csv <export.csv> --slug <client-slug>

# Re-bake the six landing faces after editing growth-lab/intake/faces-config.json
.venv/bin/python3 execution/build_intake_faces.py
```

Faces (prospect-facing, reader-pure, offline): `growth-lab/intake/faces/face-{positioning-dossier,whitespace-map,bullseye,topic-scan,format-playbook,growth-blueprint}.html` · form kit: `growth-lab/intake/google-form-kit.md` · operator to-do: `growth-lab/intake/operator/FARRICE-WHEN-BACK.md`

## Live example (built + verified today)
`growth-lab/farrice-parallax/` — full engagement on the supplement/performance-brand niche: 12-channel watchlist, 50 receipted rows, all six artifacts + lead magnet. Judging surface vs Kallaway's baseline pending Farrice's verdict.

## Rules that ride along
Reader-purity (client artifacts carry zero operator language — operator notes are separate files) · three-tier honesty (fresh/stale/absent, never fabricate) · enrichment is manual-fire, never scheduled · TikTok/IG decision card: `growth-lab/DECISION-CARD-tiktok-ig-data.md` · auto-refresh job staged UNARMED: `.scratch/kallaway-sandcastles-forge/outlier-radar-refresh.UNARMED.md`
