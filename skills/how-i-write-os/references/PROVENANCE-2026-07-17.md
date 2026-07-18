# PROVENANCE — how-i-write-os repair (Wave 3 Lane 3)

Anchor → source file + location, for every quote/claim added or reformatted during this
repair. `how-i-write-os` is a conductor skill (composes 14 already-extracted experts;
owns no craft of its own) — confirmed no `extractions/how-i-write*` file exists
(`ls extractions/ | grep -iE "how|write"` = zero hits, checked before writing this
file). Ground truth is therefore the constituent expert skills' own genius.md files
(already-extracted, already-audited elsewhere) plus two real repo-memory feedback
records used as the OS's own calibration evidence.

| Anchor / quote used | Where added (this skill) | Source file | Location |
|---|---|---|---|
| "reads like AI slapped together disjointed, unflowing pieces... went completely backwards" (4/10 vs adversarial 8.6, tested 2026-06-20) | genius.md § Anti-Patterns, § Lane Map intro (Output Receipt intro), § How to Use This Skill | `feedback_diandra-hooks-only-separation.md` | user memory store, `/Users/farricecain/.claude/projects/-Users-farricecain-Google-Antigravity/memory/feedback_diandra-hooks-only-separation.md`, lines 12-15 (read verbatim this session) |
| "changed too much in the original... hallucinated or misplaced or got broken in the tone" (3/10 vs system 7.25-8.6, bake-off 2026-06-22) | genius.md § Anti-Patterns, § Lane Map intro | `feedback_multi-engine-rebuild-degrades-elevated-content.md` | user memory store, same path, lines 12, 17 (read verbatim this session) |
| "you don't want to describe stuff for the sake of describing" / "two-to-three vivid descriptors, then get on with it" | genius.md § Anti-Patterns, § Nonfiction mid-layer table lead-in | `skills/bill-browder-high-stakes-narrative/genius.md` | lines 13-14 |
| "the stench of inauthenticity that is very easy to smell" | genius.md § Nonfiction mid-layer table lead-in | `skills/susan-orlean-narrative-nonfiction/genius.md` | line 15 |
| "clean lines... informed by a few flourishes" | genius.md § Nonfiction mid-layer table lead-in | `skills/dan-wang-literary-analysis/genius.md` | line 19 |
| "I write really fast and then edit slow" | genius.md § Nonfiction mid-layer table lead-in | `skills/wright-thompson-mastery/genius.md` | line 28 |
| "Good Place to Stop" Test / "if the reader can find a comfortable stopping point, you've failed" | genius.md § Perception/scene-voice table lead-in | `skills/michael-connelly-vivid-writing/genius.md` | line 50 |
| "hate clutter" | genius.md § Perception/scene-voice table lead-in | `skills/paul-harding-lyric-prose/genius.md` | line 15 |
| "I'm not arguing for maximalist sentences. I'm arguing for idiosyncrasy and strangeness" | genius.md § Perception/scene-voice table lead-in, § Anti-Patterns | `skills/ocean-vuong-perceptual-writing/genius.md` | line 25 |
| "God is in the details. The wonder is in the details" | genius.md § Perception/scene-voice table lead-in | `skills/henry-shukman-contemplative-writing/genius.md` | line 15 |
| "Name the machinery on the page and you break the spell" | genius.md § Anti-Patterns | `skills/ben-watkins-storytelling/genius.md` | line 14 |
| Recognition-test phrasing pattern (model, not copied verbatim) | genius.md § How to Use This Skill (Model Calibration) | `skills/ben-watkins-storytelling/genius.md` | lines 7-16 (structural model per ENVELOPE instruction, reworded for this OS's composition craft, not copied) |
| 2 v2 traces exist, both composite 7.25, both `workflow: extract-forge` (build-time, not production signal) | references/source-ledger.md | `evolution_store/v2_traces/trace_20260626_030339_how-i-write-os.json`, `trace_20260626_030352_how-i-write-os.json` | full files read |
| Front-door command spot-checks (`/browder-drama-excavation`, `/orlean-telling-subject`, `/connelly-rewrite`, `/estrangement-engine`) resolve to real workflow files | references/source-ledger.md | `skills/bill-browder-high-stakes-narrative/workflows/browder-drama-excavation.md`, `skills/susan-orlean-narrative-nonfiction/workflows/orlean-telling-subject.md`, `skills/michael-connelly-vivid-writing/workflows/connelly-rewrite-protocol.md`, `skills/ocean-vuong-perceptual-writing/workflows/estrangement-engine.md` | confirmed via `find` this session |
| workflows/how-i-write.md content | new workflow file (relocation, not new authorship) | `skills/how-i-write-os/references/prompts-v2/composed-writing-piece-and-receipt.md` | entire file (born-v2, `refactored: 2026-07-13`) — body copied verbatim; only the frontmatter block was rewritten (added a `description:` field matching house convention, kept the original `source_prompt`/`skill`/`standard`/`forged`/`refactored` fields, added `relocated: 2026-07-17`) |

## UNCONFIRMED / explicitly flagged (not anchored, and said so)

- Full 14-expert front-door command list was NOT individually re-verified against
  every target skill this session — only 4 spot-checked (see above). Flagged as
  LIKELY, not VERIFIED, in `references/source-ledger.md`.
- The two extract-forge traces are explicitly labeled UNCONFIRMED as evidence of
  production quality (they are build-time self-certification, per
  `execution/skill_auditor.py` `BUILD_WORKFLOWS` exclusion, line 388) — do not let a
  future reader cite `7.25` as a live-deployment score.
