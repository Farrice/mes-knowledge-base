# PROVENANCE.md — context-profile-architect repair

Anchor → source file + location, for every quote/claim added or relied on in this repair. All source files read in full before citing (sizes recorded in `references/source-ledger.md`).

## Anti-Patterns (Sourced) — genius.md new section

| # | Anti-pattern | Quote used | Anchor (file : line, pre-repair numbering) |
|---|---|---|---|
| 1 | Building the JSON on first read | "Never build the JSON on first read" | `skills/context-profile-architect/genius.md` line 18 (Pattern: Five-Pass Extraction, **Execute**) |
| 2 | Stopping the psychological dig at Layer 1 | "Never stop at Layer 1" | `skills/context-profile-architect/genius.md` line 65 (Hidden Knowledge > Depth Is the Moat, **Deploy**) |
| 3 | Flattening a feeling to a bare string | 'The failure mode most engineers fall into is stripping emotion to make data "clean."' | `skills/context-profile-architect/genius.md` line 68 (Hidden Knowledge > Semantic-Preserving Structure, Not Sterile Data, **Insight**) |
| 4 | Shipping a data point that serves only one purpose | "If a data point powers only one thing, it's under-engineered." | `skills/context-profile-architect/genius.md` line 30 (Pattern: Compound Leverage Design, **Execute**) |
| 5 | Rebuilding context for every single output | "If you're rebuilding context for each output, you skipped the architecture." | `skills/context-profile-architect/genius.md` line 57 (Hidden Knowledge > The Profile IS the Product, **Deploy**) |
| 6 | Adding more words instead of restructuring | "the fix is reorganization into clear parent-child relationships, not more words" | `skills/context-profile-architect/genius.md` line 60 (Hidden Knowledge > Structure Beats Prompting, **Insight**) |
| 7 | Over-engineering a profile past the point a team can use it | "over-engineered → team can't use" | `skills/context-profile-architect/workflows/03-evolve-profile-version.md` line 17 (Phase 1: Feedback Integration) |

Date anchor "2026-07-01" used on every bullet: `skills/context-profile-architect/SKILL.md` line 7, frontmatter `source: "claude.ai project export (2026-07-01)"` — verbatim.

## Recognition Test — genius.md new section

| Quote used | Anchor |
|---|---|
| "Can AI generate the target output with no additional context?" | `skills/context-profile-architect/genius.md` line 73 (Hidden Knowledge > Iteration Over Perfection; Validation Determines Value, **Deploy**) |
| "entrepreneurs, 30-45, wants to grow revenue" (illustrative counter-example) | Constructed by this repair as an illustrative single-adjective-tier persona description, contrasting the "Our target is entrepreneurs" example already at `skills/context-profile-architect/genius.md` line 22 (Pattern: Recursive Depth Mining) — labeled as illustrative, not a quote from a real source. |

## Named-entity floor fixes — one added sentence per failing pattern section

| Section | Quote/number added | Anchor |
|---|---|---|
| ARCHITECT Framework™ 2.0 | "150-400 lines" | `skills/context-profile-architect/workflows/01-architect-context-profile.md` line 53 (Output Contract: "typically 150-400 lines") |
| Pattern: Five-Pass Extraction | "resolved to at least Layer 4 (unconscious driver), not a single-adjective description" | `skills/context-profile-architect/workflows/01-architect-context-profile.md` line 57 (Quality Gate) |
| Pattern: Clean JSON Codification | "nesting 2-5 levels, never deeper" | `skills/context-profile-architect/workflows/01-architect-context-profile.md` line 53 (Output Contract) |
| Pattern: Transformation Architecture | "current_state vs desired_state across external/internal/self-narrative/market/team/life + gap_analysis + bridge_requirements" | `skills/context-profile-architect/workflows/01-architect-context-profile.md` line 39 (Phase 2) |
| Hidden Knowledge > Structure Beats Prompting | "Can AI generate the target output with no additional context?" | `skills/context-profile-architect/genius.md` line 73 (self-citation, Iteration Over Perfection) |
| Hidden Knowledge > Depth Is the Moat | "psychological archaeology wins — the gold is buried 3-5 layers deep, and surface wants ≠ hidden needs ≠ core drivers" | `skills/context-profile-architect/workflows/02-excavate-psychological-layers.md` line 10 (Role) |
| Hidden Knowledge > The Redaction Convention | 'the source is dated "claude.ai project export (2026-07-01)"' | `skills/context-profile-architect/SKILL.md` line 7 (frontmatter) |

## How to Use This Skill (Model Calibration) — genius.md new section

Modeled on `skills/ben-watkins-storytelling/genius.md` lines 7-16 (structure only: intuition-primitives framing, never-announce-the-machinery, expert-specific texture, polish-is-the-tell warning) — read once for structure, written fresh for this expert's actual craft (JSON data-architecture, not conversational storytelling). No text copied from the Watkins file.

## Absence verification (Rule 2 of the envelope)

Before writing "no source exists" anywhere in this repair, the following reads/searches were performed and their sizes recorded (see `references/source-ledger.md` for the full list): `extractions/` directory listing + grep (zero hits), repo-wide filename search for export-style files (zero hits outside skill/agent/command files), `agents/context-profile-architect/memory/context.md` (139 bytes, read in full — scaffold only), `.claude/commands/context-profile.md` (1,241 bytes, read in full), `.claude/commands/context-profile-architect.md` (1,523 bytes, read in full), `agents/context-profile-architect/AGENT.md` (5,519 bytes, read in full).
