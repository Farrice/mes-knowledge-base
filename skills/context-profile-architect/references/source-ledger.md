# Source Ledger — context-profile-architect

Claim-by-claim provenance for the Context Profile Architect 2.0 skill. This is a **METHOD skill** (a synthetic/meta expert per `agents/context-profile-architect/AGENT.md` line 9: "Synthetic/meta expert"), not a person extraction — there is no interview transcript, video, or podcast to check quotes against. Ground truth = the skill's own files, which are themselves presented as the extracted artifact.

## What was searched (verified by actual reads/sizes, not assumed absent)

- `extractions/` — searched full directory listing (`ls extractions/`, 100+ entries) and grepped for "context-profile", "context.profile", "ARCHITECT Framework", "Context Profile Architect" across all files. **Zero matches.** No raw claude.ai project export exists in `extractions/`.
- Repo-wide search for `*context-profile*export*` and `*claude.ai*export*` filenames — **zero matches** outside the skill/agent/command files themselves.
- `agents/context-profile-architect/memory/context.md` — read in full. 139 bytes. Contains only unpopulated scaffold headers ("Active Projects (None yet)", "User/Brand Context (To be populated)", "Learnings (To be populated)"). No source material.
- `.claude/commands/context-profile.md` (1,241 bytes) and `.claude/commands/context-profile-architect.md` (1,523 bytes) — read in full. Both are `sync_registries.py` auto-generated skill-command shims that point back to `SKILL.md`/`genius.md`. No independent source content.
- `agents/context-profile-architect/AGENT.md` (5,519 bytes) — read in full. A synthesis of the skill's own genius.md content, explicitly labels the expert "Synthetic/meta expert." No new source material beyond what's in genius.md.

**Conclusion**: SKILL.md's frontmatter states `source: "claude.ai project export (2026-07-01)"`, but no raw export file backs that claim anywhere in this repo. The skill's own SKILL.md, genius.md, and workflows/*.md **are** the only extant artifact of that export — they are both the "extraction" and the source simultaneously. Every quote cited in genius.md's new Anti-Patterns and Recognition Test sections is drawn from these files directly (self-referential, file-verified), not from an external transcript.

## Claim-by-claim labels

| Claim | Label | Basis |
|---|---|---|
| A raw claude.ai project export file exists in this repo, distinct from SKILL.md/genius.md | **UNCONFIRMED** | Searched `extractions/`, repo-wide filename search, `.claude/commands/`, `agents/context-profile-architect/`. None found. Cannot rule out it exists off-repo, but nothing in-repo substantiates it. |
| The export is dated 2026-07-01 | **VERIFIED** | Literal text in `skills/context-profile-architect/SKILL.md` line 7: `source: "claude.ai project export (2026-07-01)"`. |
| "Context Profile Architect 2.0" is a synthetic/meta expert, not a real named person | **VERIFIED** | `agents/context-profile-architect/AGENT.md` line 9 states this explicitly: "Synthetic/meta expert." |
| The ARCHITECT Framework™ 2.0 (four phases, letters A-R-C-H-I-T-E-C-T) as documented | **VERIFIED** | Verbatim structure present in `skills/context-profile-architect/genius.md` lines 6-13 (this repair's baseline read). |
| All 7 Genius Patterns (Five-Pass Extraction, Recursive Depth Mining, Psychological Archaeology, Compound Leverage Design, Dynamic Field Architecture, Semantic Preservation at Scale, Clean JSON Codification) | **VERIFIED** | Present verbatim in `genius.md` prior to this repair; unmodified except for one added anchor sentence per pattern (see PROVENANCE.md). |
| All 6 Hidden Knowledge entries (The Profile IS the Product, Structure Beats Prompting, Depth Is the Moat, Semantic-Preserving Structure Not Sterile Data, Iteration Over Perfection, The Redaction Convention) | **VERIFIED** | Present verbatim in `genius.md` prior to this repair. |
| The 3 workflow files' Output Contracts and Quality Gates (150-400 line JSON target, nesting 2-5 levels, Completeness/Reusability/Quality test batteries, etc.) | **VERIFIED** | Read in full: `workflows/01-architect-context-profile.md`, `workflows/02-excavate-psychological-layers.md`, `workflows/03-evolve-profile-version.md`. All cited quotes in this repair's Anti-Patterns/Recognition Test sections were checked against these files verbatim before use. |
| Whether the original claude.ai export used a "™" trademark symbol on "ARCHITECT Framework" | **UNCONFIRMED** | No raw export exists to check the symbol's origin against; it appears consistently in this skill's own files, which is the only evidence available. |
| Any real-world outcome, client, or performance number (e.g. "100-1000x," "40% → 5% edit-rate") reflects an actual measured result rather than an illustrative framework example | **UNCONFIRMED** | These read as illustrative teaching examples embedded in the method's own text (e.g. genius.md's Systematic Improvement Loops pattern), not sourced to any named case study, client, or dated event. Treat as illustrative, not as a verified performance claim. |

## Anchors used in this repair (genius.md additions)

Every quote added to genius.md's Anti-Patterns and Recognition Test sections was located and verbatim-checked in the cited file before use — see `PROVENANCE.md` for the file+line table.
