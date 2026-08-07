# Source Ledger — oren-content-team-architecture

Compiled during Wave 3 Lane 4 Batch 13 repair, 2026-07-18. Every claim/pattern group in this skill, labeled VERIFIED / LIKELY / UNCONFIRMED. Ground-truth search performed against `extractions/` (all folders matching `oren*`), `_active/harness/claude-export/` (441 files, unpacked), and `_archive/claude-export-2026-07-01.tar.gz` (332MB, not extracted — MEMORY.md flags this archive "don't re-import"; file sizes recorded below for the folders that WERE checked).

## Files examined (with sizes, per the "record file sizes before claiming absence" rule)

| File | Size (wc -c) | Relevance |
|---|---|---|
| `extractions/oren/extraction-report.md` | 23,343 | Luxury Branding psychology — different domain, no content-team-architecture material |
| `extractions/oren/extraction-report-repositioning.md` | 21,509 | Repositioning — different domain |
| `extractions/oren/oren-systems-extraction-report.md` | 14,668 | Operational systems (reference repos, weekly updates) — adjacent but does NOT cover pod architecture, media-company flywheel, or the Represent/Flamingo Estate/Cheese Store exemplar set |
| `extractions/oren/transcript.txt` | 29,376 | Source for the Luxury Branding extraction — confirmed no pod/flywheel/media-company content |
| `extractions/oren-1person-ai-marketing/mastery-extraction.md` | 56,878 | 1-person AI marketing — different domain |
| `extractions/oren-1person-ai-marketing/transcript.txt` | 33,026 | Same as above |
| `extractions/transcripts/1kcxUhjuW_0.txt` / `_0_1.txt` | 19,502 each | Confirmed = the Luxury Branding raw transcript, not content-team-architecture |
| `_active/harness/claude-export/` (441 files) | — | Searched for "oren" — zero matches |

## Claim groups

### 1. Patterns 1-13 (Pod Architecture, Marketing World Flywheel, Media Company Diagnostic, Signature Series Protocol, Pod Cadence, 10-Asset Standard, Tiered Brand Exemplar Matrix, External Creator Integration, Founder-as-Character, Anchor Strategy, Anti-Overproduction, Agency Integration, Multi-Pod Scaling)

**Label: UNCONFIRMED.** No raw source file (transcript, extraction report, or export conversation) covering these patterns could be located anywhere under `extractions/` or the unpacked `_active/harness/claude-export/`. The only unopened candidate is `_archive/claude-export-2026-07-01.tar.gz` (332MB) — not extracted this session per the standing "don't re-import" note in MEMORY.md (`project_claude-export-harvest.md`) and because a 332MB extraction is out of scope for a minimal-touch repair pass. These patterns were already shipped content in this skill prior to this repair (not introduced by this worker) — this ledger surfaces the gap honestly rather than retroactively inventing a citation. Named brand exemplars (Represent, Flamingo Estate, Cheese Store of Beverly Hills, Chunky Fit Cookie, Tracksmith, Rarify, Dark Room, Ladder, Rapha, Cluey) are real, publicly-known brands but their specific content-strategy claims in this skill are unverified against a primary Oren source.

**Recommendation**: flag for a follow-up sourcing pass — either locate the original video/transcript this skill was built from, or re-extract from `_archive/claude-export-2026-07-01.tar.gz` with a scoped/targeted extraction (grep for "Represent" or "pod" inside the tarball without a full unpack).

### 2. "Patterns from claude.ai export — Oren John conversations (2026-07-01)" section (The 60-Day Bar, AI Hooks Not AI Videos, Production Elevation Math, Virality-First TOF, The Midfunnel Shift, Hidden Knowledge)

**Label: LIKELY.** These quotes and patterns were already present in the skill (dated, cited to "Oren John's '2026 Creative Trend Predictions' talk," extracted from a claude.ai export dated 2026-07-01). The quotes read as genuine spoken-transcript material (colloquial, imperfect grammar — "it's literally everyone is getting better," "we test everything — that does not work super well"), which is consistent with real extraction rather than fabrication. However, the underlying raw export file could not be located in the currently-unpacked `_active/harness/claude-export/` (441 files, zero "oren" matches) — it likely lives inside the unextracted `_archive/claude-export-2026-07-01.tar.gz`. Not independently re-verified against a primary file this session; hence LIKELY, not VERIFIED.

### 3. Anti-Patterns (Sourced) section (new, added this repair)

**Label: LIKELY**, matching claim group 2 above — every anti-pattern bullet quotes verbatim from the already-existing, dated Oren John section (claim group 2) rather than introducing any new quote or claim.

### 4. Named brand exemplars (Represent, Flamingo Estate, Tracksmith, Cheese Store of Beverly Hills, Chunky Fit Cookie, Dark Room, Ladder, Rapha, Cluey, Rarify)

**Label: UNCONFIRMED** for the specific content-strategy claims attributed to them in this skill (e.g., "Represent's founders" as Evangelist archetype, "Chunky Fit's founder journey"). These are real, identifiable brands, but no source file in this repo confirms Oren specifically taught these examples — they were already shipped content, carried forward as-is per the additive-first/no-delete boundary.

## What this means for delivery

This skill's Patterns 1-13 should be treated as strong synthesized operating doctrine in Oren's voice/domain rather than verbatim-sourced teaching, until a follow-up sourcing pass locates the original material. The claude.ai export section (2026-07-01) and everything derived from it (including the new Anti-Patterns section) is LIKELY-grade — quoted material is internally consistent and dated but not independently re-verified against a primary file this session.
