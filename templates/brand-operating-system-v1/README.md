# Brand Operating System Template v1

This is the deployable template for any future BOS build — a 6-layer architecture (43 docs) that produces an AI-handoff-first brand system at the same quality bar as the Resonance reference at `_active/andrea-dj/brand-operating-system/`.

## Philosophy

The template is **Resonance with identity tokens stripped**, not abstract blanks. Reading the template gives you a concrete worked example of every section. The build workflow overwrites the brand-specific content during Phase A-B; everything else stays.

This is a deliberate choice. Empty templates with `[FILL THIS IN]` placeholders teach nothing. A worked example with named tokens teaches the pattern and the bar at the same time.

## What gets substituted vs. overwritten

**Identity tokens** (substituted by `bos_scaffold.py`):
- `{{BRAND_NAME}}`, `{{BRAND_NAME_LOWER}}`, `{{FOUNDER_NAME}}`, `{{CITY}}`, `{{SPINE_LINE}}`, `{{ONE_LINER}}`, `{{SUCCESS_METRIC}}`, `{{SPINE_FRAME}}`, plus the recommended set in `TOKENS.md`.
- These run at scaffold time. The output is "Resonance's structure + your identity."

**Brand-specific content sections** (overwritten by workflow phases):
- The 12 non-negotiables (`05-non-negotiables.md`)
- The 6 voice patterns (`03-voice-document.md`)
- The 3 ICP profiles (`02-icp-master.md`)
- The 9 sections of the brand bible (`01-brand-bible.md`)
- The content pillars, hooks, drift signals, success metrics, etc.
- Each phase workflow specifies which sections in which files to regenerate.

**Structural skeleton** (always preserved):
- Section order, headers, paste-in conventions
- The Master Creative Brief Template's 10 sections
- The AI Brain Master's 8 compressed sections + 4K token ceiling
- The ops protocol structure (drift signals readback, change log format, exit interview question bank)

## Folder structure

```
templates/brand-operating-system-v1/
├── 00-foundation/        Spine docs (brand bible, voice, ICP, positioning, non-negotiables, master index)
├── 01-visual/            DESIGN.md + photography rules + component tokens + brand library + aesthetics
├── 02-briefs/            Master template + 9 per-asset briefs (IG×3, email, flyer, ticket, venue, press, DJ)
├── 03-marketing/         Pillars, hooks, channels, curation, crisis, why-gate, funnel, offer card
├── 04-ai-handoff/        AI Brain Master, Claude Pro setup, prompt library, image formulas, Canva spec
├── 05-ops/               Update protocol, change log, handoff checklist, drift signals, metrics, exit interviews, run-of-show
├── _working/             Intermediate artifacts (A1 reconciliation, A3 discovery, G1 adversarial review, G2 prose scan)
├── _source/              Placeholder for client's canonical inputs
├── README.md             This file
└── TOKENS.md             Token manifest
```

## How to deploy

```bash
# 1. Scaffold the project from this template
python3 execution/bos_scaffold.py \
    --template templates/brand-operating-system-v1/ \
    --output projects/<client-slug>/brand-operating-system/ \
    --tokens-file scratch/<client>-tokens.json

# 2. Run the orchestrated build
/build-bos --name "<Brand>" --source <path-to-canonical-doc> \
    --output projects/<client-slug>/brand-operating-system/

# 3. (optional) Auto-upload to Drive as native Google Docs + pageless
/build-bos ... --drive-parent <google-drive-folder-id>
```

## Reference implementation

Live: `_active/andrea-dj/brand-operating-system/` — Resonance v1 (shipped 2026-05-04, all 43 docs, Drive + native Google Docs + pageless).

The template is a derivative of this reference. When the template amends, Resonance gets back-applied or explicitly diverged — see `directives/brand-operating-system-protocol.md` for the discipline.

## Versioning

Template version: **v1**. Bumped to v2 when the structural skeleton itself changes (new layer, new master template section, new phase). Identity-token additions are minor versions (v1.1, v1.2). Track in `directives/brand-operating-system-protocol.md` change log.
