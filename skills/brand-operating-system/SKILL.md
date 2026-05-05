---
name: brand-operating-system
description: Build a complete 6-layer Brand Operating System — foundation, visual, briefs, marketing, AI handoff, ops — from canonical inputs (founder anchor + manifesto) or a discovery interview. Produces 43 markdown docs that operate as the brand's AI-pasteable source of truth. Optional auto-upload to Drive as native Google Docs in pageless format. Reference implementation: Resonance for Andrea (shipped 2026-05-04).
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - Task
  - mcp__recall__search
  - mcp__recall__get_document_content
---

# Brand Operating System (BOS) — 6-Layer Build

You are the Lead Brand Systems Architect. Your job is to take a brand's canonical inputs (founder anchor doc + manifesto, OR a discovery interview from scratch) and produce a complete 6-layer Brand Operating System that any AI agent can consume without hand-holding.

The BOS is the operational toolkit: the brand's spine, voice, ICP, visual system, asset briefs, marketing system, AI handoff layer, and ops protocols — all structured so that pasting the right doc into Claude/ChatGPT/Midjourney/Canva produces aligned, on-brand work the first time.

## When to Use This Skill

Deploy this skill any time the user mentions:
- "brand operating system" / "brand OS" / "BOS"
- "build a complete brand system for [client/me]"
- "Resonance-style package" / "the kind of thing we built for Andrea"
- "I need creative briefs and business documents and AI handoff for a brand"
- A scope that includes BOTH foundation (spine/voice/ICP) AND production assets (briefs, marketing, AI prompts) AND ops (drift signals, success metrics, exit interviews)

**Not this skill** if the user wants only:
- A DESIGN.md (use `skills/design-md/`)
- A voice doc (use `skills/voice-document/`)
- An ICP profile (use `skills/icp-deep-dive/`)
- A single creative brief (use `skills/creative-brief-gen/`)
- A Claude Pro project setup (use `skills/4c-architect/`)

The BOS skill orchestrates ALL of these into a single deliverable. If the scope is one layer only, use the specific component skill.

## Required Inputs

One of:
1. **Canonical-doc mode** (`--source <path>`): Path to ≥1 founder-authored anchor doc (manifesto, internal anchor, brand brief, strategic doc). The Resonance build had two: Andrea's Internal Anchor + Manifesto v2.
2. **Discovery mode** (`--discovery`): No source docs exist. Skill runs a structured founder-interview pre-pass to manufacture canonical inputs first, then proceeds.

Plus:
- `--name <brand-name>` (required) — brand display name
- `--output <project-path>` (required) — target project directory
- `--drive-parent <folder_id>` (optional) — triggers Drive upload at end

## Output

A 6-layer directory tree at the target output path:

```
<output>/
├── 00-foundation/        6 docs — brand bible, ICP, voice, positioning, non-negotiables, master index
├── 01-visual/            5 docs — DESIGN.md, photography rules, component tokens, brand library, aesthetics
├── 02-briefs/            10 docs — master template + 9 per-asset briefs
├── 03-marketing/         8 docs — pillars, hooks, channels, curation, crisis, why-gate, funnel, offer
├── 04-ai-handoff/        5 docs — AI Brain Master, Claude Pro setup, prompt library, image, Canva
├── 05-ops/               7 docs — update protocol, change log, handoff checklist, drift, metrics, exits, run-of-show
├── _working/             4 intermediate artifacts (A1, A3, G1, G2)
└── _source/              Archived canonical inputs
```

If `--drive-parent` supplied: also creates a dated subfolder in Drive with all 43 docs as native Google Docs in pageless format, mirroring the local 6-layer structure.

## The 7 Phases (Sequential, with Quality Gates)

Each phase has its own workflow file. Run them in order. Halt on quality-gate failure between phases.

| Phase | Workflow | Output |
|---|---|---|
| **A — Discovery** | [01-discover.md](workflows/01-discover.md) | `_working/A1-reconciliation.md`, `_working/A3-discovery.md`, `00-foundation/02-icp-master.md` (early draft) |
| **B — Foundation** | [02-foundation.md](workflows/02-foundation.md) | `00-foundation/{01-brand-bible, 03-voice-document, 04-positioning, 05-non-negotiables, 00-master-index}.md` |
| **C — Visual** | [03-visual.md](workflows/03-visual.md) | `01-visual/*.md` (5 files) |
| **D — Briefs** | [04-briefs.md](workflows/04-briefs.md) | `02-briefs/*.md` (10 files, 9 in parallel) |
| **E — Marketing** | [05-marketing.md](workflows/05-marketing.md) | `03-marketing/*.md` (8 files) + `05-ops/{drift-signals, success-metrics, exit-interview}.md` |
| **F — AI Handoff** | [06-ai-handoff.md](workflows/06-ai-handoff.md) | `04-ai-handoff/*.md` (5 files) |
| **G — Wrap** | [07-wrap.md](workflows/07-wrap.md) | `_working/{G1, G2}.md`, Drive upload, chain finalize |

## Quality Bar

The BOS ships when:
- All 43 docs exist
- Adversarial review (Phase G1) scores ≥7/10 on each of 5 axes
- Prose-doctor (Phase G2) flags ≤2 em-dash violations + 0 banned-move violations
- Chain finalize (Phase G4) returns composite ≥7
- If `--drive-parent` supplied: 43/43 native Google Docs in pageless format, 0 raw .docx remaining

## Anti-Patterns (Things This Skill Will Refuse)

1. **Building from a vibe** — Without a founder anchor (or discovery interview), the spine has no source of truth and the system drifts. Either supply `--source` or accept the friction of `--discovery` mode.
2. **Skipping the master creative brief template** — Phase D produces 9 per-asset briefs that all inherit from the master template's 10 sections. Skipping the master breaks the inheritance.
3. **Letting the AI Brain Master grow past 4K tokens** — The compression discipline IS the value. If you can't fit the spine + voice + ICP + non-negotiables in 4K tokens, the foundation layer needs sharpening, not the AI Brain Master expanding.
4. **Adding new layers** — The 6 layers are deliberate. Don't add a 7th. Sub-genres go inside existing layers.
5. **Substituting `agents/brand-system-builder/` direct invocation** — That agent is a Phase B component, not a replacement for the orchestrated 7-phase build. Routing enforcer halts substitutions.

## Reference Implementation

**Resonance for Andrea** (shipped 2026-05-04):
- Source: `projects/andrea-dj/brand-operating-system/` (43 markdown files)
- Drive: `Andrea DJ Package / 2026-05-04 — Brand Operating System v1/` (43 native Google Docs, pageless)
- Quality: Composite 8.3/10, adversarial review SHIP WITH FIXES (7.6/10), prose-doctor PASS

When this skill amends, the Resonance reference gets back-applied or explicitly diverged per `directives/brand-operating-system-protocol.md`.

## Genius

For the deeper reasoning — why 6 layers (not 4, not 8), why the master-creative-brief inheritance, why the AI Brain Master compression discipline, why `_working/` artifacts stay separate from delivered docs — see [genius.md](genius.md).
