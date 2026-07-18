# Source Ledger — /verticalize

Every claim in `genius.md` and the 4 workflow files is checked against a real, readable source. `verticalize` is a system/methodology skill (Farrice's own orchestration conductor, not a third-party expert extraction) — ground truth is its own workflow contract, the resolver code that routes into it, and the two named-failure feedback cards it was built to prevent. No `extractions/` folder exists for this skill (confirmed: `ls extractions/ | grep -i vertical` returns nothing) because there is no external expert being extracted here.

## Primary sources (in-repo, read in full)

| Source | Path | Size | Role |
|---|---|---|---|
| Skill contract | `skills/verticalize/SKILL.md` | 7,019 bytes | Own anti-patterns list, phase summary, "why Phase 2.5" rationale |
| Full workflow | `.agent/workflows/verticalize.md` | 12,260 bytes | 8-phase step-by-step, gate script text, stop conditions |
| Slash command shim | `.claude/commands/verticalize.md` | — | Confirms the workflow file is the executable contract |
| Resolver code | `execution/intent_to_package.py` lines 203-224, 657-702 | — | `VERTICAL_BOOTSTRAP_SIGNALS`, `_resolve_vertical_bootstrap` (class 10, dated 2026-05-25 in the docstring) |
| Domain registry | `execution/ground_truth.py` lines 85-171 | — | `init_domain()` slug validation regex, registration fields |
| Gate convention | `directives/workflow-gate-convention.md` | — | Rubber-stamp-gate anti-pattern, skip-syntax rule, dated 2026-05-12 |

## External sources (outside repo tree, user's memory store — read in full)

| Source | Path | Role |
|---|---|---|
| Ground-truth calibration lesson | `/Users/farricecain/.claude/projects/-Users-farricecain-Google-Antigravity/memory/feedback_auto-evolution-cant-substitute-for-ground-truth.md` | Origin of the Phase 2.5 non-skippable rule; dated 2026-05-03, origin session `0da86f83-e5ba-4a65-b3ed-7fc56ef23947` |
| Naming cultural-connotation failure | `/Users/farricecain/.claude/projects/-Users-farricecain-Google-Antigravity/memory/feedback_naming-cultural-connotation-failure.md` | Origin of Phase 2.5's third gate question; dated 2026-04-11, origin session `aa770f34-ded9-4525-8a4d-f0d9c71b8f95` |

Both memory cards carry the harness's own staleness warning ("This memory is 75/97 days old... verify against current code before asserting as fact"). Their quoted text is used here as historical record of a named incident (what happened, when, what changed), not as a live claim about current code state — that distinction is preserved throughout `genius.md`.

## Claim-by-claim verification

| Claim | Source | Status | Notes |
|---|---|---|---|
| "the calibration cost of un-validated ground truth is permanent" | `skills/verticalize/SKILL.md`, Anti-patterns §1 | VERIFIED | Verbatim in SKILL.md line 106 |
| "Don't auto-edit `routing_enforcer.py`. Phase 4 proposes; the user applies." | `skills/verticalize/SKILL.md`, Anti-patterns §2 | VERIFIED | Verbatim, line 107 |
| "If fewer than 5 samples reach user-approved PASS, halt." | `.agent/workflows/verticalize.md`, Phase 3 stop condition | VERIFIED | Verbatim, line 141 |
| "Don't duplicate brand bibles in the per-project CLAUDE.md." | `skills/verticalize/SKILL.md`, Anti-patterns §4 | VERIFIED | Verbatim, line 109 |
| "Does NOT support 'verticalize at scale' (5+ verticals in parallel) in v1." | `.agent/workflows/verticalize.md`, "What This Workflow Does NOT Do" | VERIFIED | Verbatim, line 234 |
| "Do not auto-advance. Wait for explicit user signal." | `.agent/workflows/verticalize.md`, Phase 2.5 | VERIFIED | Verbatim, line 112 |
| "the skip flag must be passed explicitly — not inferred" | `.agent/workflows/verticalize.md`, Phase 2.5 skip-syntax note | VERIFIED | Verbatim, line 114, itself citing `directives/workflow-gate-convention.md` |
| "Anti-pattern: rubber-stamp gates ('Looks good, proceed?') with no structured halt path. These train Claude and the user to auto-click yes, defeating the gate." | `directives/workflow-gate-convention.md` | VERIFIED | Verbatim, lines 22-22 (Anti-pattern block) |
| "the system averages toward the model's own preferences and calls that 9/10" | `feedback_auto-evolution-cant-substitute-for-ground-truth.md` | VERIFIED | Verbatim quote, read in full 2026-07-18 |
| "94-99% of finalize traces scored 8+" (2026-04-24 audit) | same card | VERIFIED | Verbatim figure in card body |
| "Farrice (30-year Chicago resident) rated them 2/10... worse than a bad name is a bad name presented as a great one" | `feedback_naming-cultural-connotation-failure.md` | VERIFIED | Verbatim quote, read in full 2026-07-18 |
| "NEVER present names for a geographically-rooted brand without validating cultural connotation with someone who has lived experience in the target geography" | same card | VERIFIED | Verbatim, card's opening rule |
| "Confidence must track output quality, not process adherence." | same card | VERIFIED | Verbatim, card's how-to-apply §4 |
| `init_domain` slug regex `^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$` | `execution/ground_truth.py` line 146 | VERIFIED | Read directly in source, 2026-07-18 |
| `_registered_domains.json` currently `{}` (no vertical has completed the phase in production) | `knowledge/expert-benchmarks/_registered_domains.json` | VERIFIED | Read directly, 2 bytes, contents `{}` |
| Class 10 resolver shipped "2026-05-25" | `execution/intent_to_package.py` line 203 comment | VERIFIED | Read directly in source |
| Plan file `/Users/farricecain/.claude/plans/i-think-the-biggest-virtual-emerson.md` exists at the path SKILL.md cites | `skills/verticalize/SKILL.md` "Related primitives" + "v1 status" | UNCONFIRMED | File does not exist on disk at that path (checked directly, 2026-07-18) — SKILL.md's own citation is stale. Flagged, not silently repeated as fact in `genius.md`. |
| Archive conversation export contains prior discussion of THIS skill specifically | `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes) | UNCONFIRMED (absence) | Full per-member content scan run 2026-07-18 (7,720 files scanned, tarfile read to completion). 13 files matched "verticaliz" as a substring, but all 13 use "verticalization"/"verticalized" as a generic business-strategy term in unrelated conversations (e.g. `claude-export/normalized/conversations/1a51d877-038c-4733-8037-c23b098d8b81.md`, 45,220 bytes — "Innovation #1: Verticalized AI Platforms," a DTC-scaling conversation with no connection to this skill). No archive conversation discusses the `/verticalize` skill, its phases, or its build session. Absence verified by full scan, not assumed. |

## Anti-Patterns table

| Anti-Pattern (as written in `genius.md`) | Source | Status |
|---|---|---|
| Skipping Phase 2.5 under time pressure | `skills/verticalize/SKILL.md` Anti-pattern §1 + `feedback_auto-evolution-cant-substitute-for-ground-truth.md` | VERIFIED |
| Auto-editing `routing_enforcer.py` | `skills/verticalize/SKILL.md` Anti-pattern §2 + `.agent/workflows/verticalize.md` Phase 4 | VERIFIED |
| Shipping <5 PASS samples | `skills/verticalize/SKILL.md` Anti-pattern §3 + Phase 3 stop condition | VERIFIED |
| Duplicating brand bible into child CLAUDE.md | `skills/verticalize/SKILL.md` Anti-pattern §4 | VERIFIED |
| Parallel bootstrap of 5+ verticals | `skills/verticalize/SKILL.md` Anti-pattern §5 + workflow file's "does NOT support" note | VERIFIED |
| Rubber-stamp gate answers | `directives/workflow-gate-convention.md` | VERIFIED |
| Inferring `--skip-2.5` from tone | `.agent/workflows/verticalize.md` Phase 2.5 skip-syntax note | VERIFIED |
| High confidence + zero flagged uncertainty as a false "clean build" signal | `feedback_naming-cultural-connotation-failure.md` | VERIFIED |
| Skipping lived-experience validation on geography/subculture claims | `feedback_naming-cultural-connotation-failure.md` | VERIFIED |

## What was NOT invented

- No quote in `genius.md` or the workflow files was written and then attributed to a source — every quoted string was located first, then used.
- The "first real end-to-end run... happens in a follow-on session" framing and the empty `_registered_domains.json` are both stated plainly in `genius.md`'s closing section rather than papered over — this skill has no completed production run to draw a "caught in the field" anti-pattern list from (unlike `brand-operating-system`'s Resonance-sourced list), so the anti-patterns here are drawn from the skill's own written rules and the two named incidents that motivated them, not from a fabricated deployment history.
