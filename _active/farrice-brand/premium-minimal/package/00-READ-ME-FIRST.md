# Farrice Cain Premium Minimal — Portable Design System

**Package version:** 0.9 review candidate  
**Approved visual parent:** P2-01 Premium Minimal V1  
**Protected copy primary:** P1 Variant B  
**Package state:** P3 translation awaiting Farrice Cain's final taste decision  
**External action:** Not authorized by this package

## What this package is

This is the portable source of truth for creating coherent Farrice Cain and The Angle Map assets without access to the original project or conversation.

It is designed for:

- Farrice Cain;
- a human designer or creative partner;
- Claude Design;
- Codex;
- another capable AI design or layout system; or
- an agency receiving a bounded brand handoff.

The package contains the strategic hierarchy, design tokens, layout rules, editable templates, exports, examples, AI prompts, approval states, identity constraints, and quality gates required to reproduce the system.

## Fastest AI handoff

Give the AI these files first, in this order:

1. `00-READ-ME-FIRST.md`
2. `01-BRAND-FOUNDATION.md`
3. `02-DESIGN-CONTRACT.md`
4. `03-ASSET-STATE-LEDGER.md`
5. `tokens/design-tokens.json`
6. `tokens/asset-recipes.json`
7. `ai/UNIVERSAL-AI-BRAND-DIRECTOR-PROMPT.md`
8. the closest relevant file from `templates/`

Then complete `ai/REQUEST-BRIEF-TEMPLATE.md` for the asset being requested.

## The five rules that matter most

1. **Farrice Cain is the master brand.** The Angle Map is the flagship paid offer inside it.
2. **Use one visual law.** Helvetica Neue, near-monochrome color, open grid, thin rules, generous space, and one dominant idea.
3. **Restraint is the premium signal.** Structure, judgment, and editing replace decorative “luxury” effects.
4. **Do not fabricate authority.** Lived experience is category fluency—not performance, legal, scientific, medical, or compliance proof.
5. **Approval is explicit.** A technically finished asset remains `review` until Farrice promotes that exact asset.

## Current decision still open

The existing Angle Map banner is the approved launch-mode baseline. Farrice has not yet decided whether it should remain the standing profile banner or whether an evergreen `FARRICE CAIN` banner should replace it later.

Do not invent the evergreen banner proposition or silently promote a candidate.

## Folder map

| Folder | Contents |
|---|---|
| `tokens/` | Machine-readable colors, typography, grid, components, and surface recipes |
| `ai/` | Universal and tool-specific handoff instructions plus a reusable request brief |
| `templates/banner/` | Approved banner source, upload export, and required texture layer |
| `templates/static/` | Editable SVG and PNG examples for core LinkedIn formats |
| `templates/carousel/` | Four editable SVG page sources, PNG exports, review PDF, and a flat-page PPTX sequencing container |
| `templates/field-guide/` | Twelve-page brand guide in PDF and editable PPTX |
| `identity/` | Private-identity add-on instructions; the portrait itself is packaged separately |
| `content/` | Protected P1 LinkedIn copy master |
| `examples/` | Contact sheets and profile-system preview |
| `quality/` | Visual, claim, identity, approval, and export gates |

## Required output from any collaborator

For every requested asset, return:

1. the editable source;
2. the platform-ready export;
3. the exact dimensions;
4. the source copy used;
5. alt text when relevant;
6. the approval state: `draft`, `review`, or `approved`; and
7. a short QA receipt against `quality/QA-CHECKLIST.md`.

## Font dependency

Helvetica Neue font files are not bundled. They are proprietary and must be legally available in the production environment. See `LICENSE-AND-USAGE.md` before editing or exporting.

## Package integrity

`MANIFEST.json` inventories every payload file and intentionally excludes `MANIFEST.json` and `CHECKSUMS.sha256` to avoid recursive hashing. `CHECKSUMS.sha256` verifies every payload file plus the manifest itself.
