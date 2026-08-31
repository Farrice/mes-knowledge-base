---
name: "Jack Roberts: Design Mastery"
description: "Code-first design system that codifies visual excellence into reusable DESIGN.md files, enabling one-command production of websites, presentations, brand assets, and visual systems at world-class quality."
version: "2.1"
format: "completion-engine"
workflows: 16
---

# Jack Roberts: Design Mastery

> Codify once, replicate infinitely. Design is not an art form reserved for specialists — it's a system that can be encoded. The future is code-first design.
> Source: "Claude Code Just Became the World's #1 Design Tool" — YouTube, Jack Roberts.

**Core Philosophy:** If you can explain to an AI what great design looks like, you can produce it on demand, in any style, as many times as you want. The 5-Step System: Pick Format → Equip Integrations → Define Excellence → Generate & Refine → Enshrine as Skill.

## Core Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| forge | [Design System Forge](workflows/design-system-forge.md) | Complete DESIGN.md file with full visual language specification | Creating a new design system from scratch or from brand references |
| extract | [Brand DNA Extraction](workflows/brand-dna-extraction.md) | Brand identity package: colors, typography, logos, component patterns | You need to capture an existing brand's exact visual identity for replication |
| website | [Website Build](workflows/website-build.md) | Production-ready website using DESIGN.md design system | Building a new website or landing page with a specific brand aesthetic |
| presentation | [Presentation Build](workflows/presentation-build.md) | Interactive HTML slide deck with brand consistency | Creating presentations, pitch decks, or educational slide content |
| philosophy | [Design Philosophy Architect](workflows/design-philosophy-architect.md) | Written design philosophy document defining what excellence means | Starting a new project and needing to define the aesthetic direction before any visual work |
| anti-slop | [Anti-Slop Audit](workflows/anti-slop-audit.md) | Scored diagnostic with specific anti-slop prescriptions | Evaluating any AI-generated design for generic patterns and AI tells |
| reference | [Reference Collection Sprint](workflows/reference-collection-sprint.md) | Curated reference library with extracted design patterns | Gathering inspiration and establishing excellence benchmarks for a design project |
| iterate | [Design Iteration Loop](workflows/design-iteration-loop.md) | Refined design output matching the user's standard of excellence | You have a first draft that needs structured micro-polishing to reach production quality |
| gauntlet | [Design Gauntlet](workflows/design-gauntlet.md) | Screenshot-evidenced before/after design with a bounded repair log and surviving-risk report | A taste-bearing visual draft must improve against a named reference without regressing its system |
| enshrine | [Design Skill Enshrine](workflows/design-skill-enshrine.md) | Reusable SKILL.md file that reproduces the design at one-command quality | You've perfected a design workflow and want to make it permanently reproducible |
| multi | [Multi-Format Deploy](workflows/multi-format-deploy.md) | Same design system expressed across multiple formats (web, slides, graphics) | Deploying one brand's visual language across all your design touchpoints |
| library | [Design Library Import](workflows/design-library-import.md) | Customized DESIGN.md forked from awesome-design-md (55+ brands, 56k+ stars) | You want a proven starting point instead of building from scratch |

## Application Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| proposal | [Visual Proposal Build](workflows/visual-proposal-build.md) | Branded HTML proposal deck in the prospect's own visual language | Sending a proposal that demonstrates your production quality before the client hires |
| package | [Branded Deliverable Package](workflows/branded-deliverable-package.md) | White-labeled client deliverables (strategy docs, reports, audits) in client brand | Any client deliverable that should look premium and worth the price |
| box | [Brand-in-a-Box](workflows/brand-in-a-box.md) | Complete productized design system (DESIGN.md + website + deck + social templates) | Selling code-first design as a $2,500-$5,000 productized service |
| content | [Content Brand Forge](workflows/content-brand-forge.md) | Personal content brand DESIGN.md with cross-platform templates | Building visual brand recognition for your content across platforms |

## Stacking Chains (Cross-Expert)

| This Workflow | × Expert | Produces |
|--------------|----------|----------|
| `/design-system-forge` | Oren `/taste-cev` | Taste-calibrated DESIGN.md |
| `/website-build` | Kochel `/design-first-build` | Research-validated + designed website |
| `/presentation-build` | Runia `/story-compass` | Narrative-structured presentations |
| `/anti-slop-audit` | Kallaway `/five-input-content-gate` | Visual + content psychology gate |
| `/multi-format-deploy` | Hoffman `/emotional-value` | Emotionally consistent cross-format brand |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Source Transcript**: `extractions/jack-roberts/transcript.txt`
- **Design Library**: `skills/design-md/` — Stitch-format DESIGN.md generator
- **Local Reference Library**: `knowledge/design-libraries/INDEX.md` — curated DESIGN.md systems, searchable with `python3 execution/design_md_brand_lookup.py search "[query]"`
- **Asset Command Center**: `.agent/assets/manifest.jsonl` + `execution/asset_gallery.py` — searchable prior prompts, styles, and visual assets; reuse before regenerating
- **Blind Bar**: `directives/blind-bar-protocol.md` — reference-anchored, capped comparison protocol used by `/design-gauntlet`
- **awesome-design-md**: `github.com/xb1g/awesome-design-md` — 55+ pre-built brand DESIGN.md files (56k+ stars)
- **Complementary Skills**: `canvas-design` (art objects), `kittl-graphic-design` (typography), `sean-kochel-design-first-build` (landing pages)

<!-- BEGIN:execution-prompts (generated by execution/wire_prompt_pointers.py — do not hand-edit; re-run to refresh) -->

## Execution Prompts (structure-pure v2)

14 deterministic practitioner prompts — each carries an Output Contract, Output Skeleton, and Quality Gate. When a deliverable matches one, Read it and honor its contract instead of improvising the output shape.

- **Jack Roberts — Anti-Slop Audit** — `skills/jack-roberts-design-mastery/references/prompts-v2/anti-slop-audit.md`
- **Jack Roberts — Brand-in-a-Box Package** — `skills/jack-roberts-design-mastery/references/prompts-v2/brand-in-a-box-package.md`
- **Jack Roberts — Branded Deliverable Package** — `skills/jack-roberts-design-mastery/references/prompts-v2/branded-deliverable-package.md`
- **Content Brand Design System: [Name]** — `skills/jack-roberts-design-mastery/references/prompts-v2/content-brand-forge.md`
- **Design Gauntlet Result — [artifact]** — `skills/jack-roberts-design-mastery/references/prompts-v2/design-gauntlet.md`
- **Jack Roberts — Design Iteration Loop** — `skills/jack-roberts-design-mastery/references/prompts-v2/design-iteration-loop.md`
- **Design System: [Project/Brand Name]** — `skills/jack-roberts-design-mastery/references/prompts-v2/design-md-construction.md`
- **Jack Roberts — Design Philosophy Document** — `skills/jack-roberts-design-mastery/references/prompts-v2/design-philosophy-document.md`
- **[Format] Design Skill: [Name]** — `skills/jack-roberts-design-mastery/references/prompts-v2/design-skill-enshrine.md`
- **Jack Roberts — Multi-Format Brand Deployment** — `skills/jack-roberts-design-mastery/references/prompts-v2/multi-format-brand-deployment.md`
- **Jack Roberts — Presentation Deck Build** — `skills/jack-roberts-design-mastery/references/prompts-v2/presentation-deck-build.md`
- **Design Reference Package: [Project Name]** — `skills/jack-roberts-design-mastery/references/prompts-v2/reference-collection-package.md`
- **Jack Roberts — Visual Proposal Deck** — `skills/jack-roberts-design-mastery/references/prompts-v2/visual-proposal-deck.md`
- **Jack Roberts — Website Build** — `skills/jack-roberts-design-mastery/references/prompts-v2/website-build.md`

<!-- END:execution-prompts -->
