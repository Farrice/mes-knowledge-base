# PROVENANCE — forge-os repair (Wave 3 Lane 4 Batch 6)

Anchor → source file + location, for every quote/date/citation added in this pass. All sizes are
real `wc -c` byte counts taken 2026-07-17 (never `wc -l`). No `extractions/` file exists for
forge-os — this is a system skill, confirmed by `ls extractions/ | grep -iE "forge"` (zero hits).

| Anchor (as it appears in genius.md / workflows/) | File | Location | Size (`wc -c`) |
|---|---|---|---|
| SKILL.md epigraph blockquote | `skills/forge-os/SKILL.md` | lines 8-13 | 8,877 |
| "Forging from training memory is prohibited" | `skills/forge-os/SKILL.md` | line 39-40 | 8,877 |
| "very straightforward and to the point… didn't capture the style and essence… I wouldn't be able to use any of this to see results" | `docs/solutions/2026-07-07-transcript-only-extraction-generic-output.md` | line 13 | 3,417 |
| "7 real defects (undefined wiring steps, dangling F1 reference...)" | `docs/solutions/2026-07-14-cold-start-probe-anneals-new-engine-prompts.md` | lines 32-37 | 2,805 |
| "exposure risk is the one irreversible item" | `skills/forge-os/references/plugin-forge-lift-plan.md` | line 47 | 5,065 |
| "lift partially — local-only, no marketplace, effective only when all four fixtures pass in a single run" | `skills/forge-os/references/plugin-forge-lift-plan.md` | line 51 | 5,065 |
| "delivers an output that is patched together, overconfident, or still generic" | `docs/solutions/expert-composition-standard.md` | line 7 | 2,233 |
| "running it without `--depth quick` at $0 tier is a tier violation" | `skills/forge-os/references/prompts-v2/grounding-sprint.md` | line 30 | 7,279 |
| refactored: 2026-07-15 (frontmatter date) | `skills/forge-os/references/prompts-v2/grounding-sprint.md` | line 7 (frontmatter) | 7,279 |
| "14 of luke-iha-vicious-hooks' 'missing' workflow contracts existed under `## Output Contract`..." | `docs/solutions/2026-07-17-repair-fleet-poc-three-failure-shapes.md` | lines 19-21 | 5,899 |
| Label semantics blockquote (VERIFIED/LIKELY/UNCONFIRMED definitions) | `skills/forge-os/references/prompts-v2/grounding-sprint.md` | lines 57-61 | 7,279 |
| `agents/forge-os/AGENT.md` exists (Agent Forge lane self-proof) | `agents/forge-os/AGENT.md` | file presence + size only | 10,620 |
| Each `workflows/*.md` Output Schema/Quality Gate content | Corresponding `skills/forge-os/references/prompts-v2/<lane>.md` `## Output Contract`/`## Output Skeleton`/`## Quality Gate` sections | see per-file `grep -n "^## "` in REPAIR-NOTES.md | 4,299–8,263 (range across the 6 prompts-v2 files) |

## Recognition-test / calibration section provenance

The "How to Use This Skill (Model Calibration)" and "Recognition Test" sections in `genius.md`
are written fresh for Forge OS's own texture (contract-first forging, fidelity honesty, spine
discipline) — modeled on the STRUCTURE of `skills/ben-watkins-storytelling/genius.md` lines 7-16
(intuition primitives / never announce the machinery / this skill's specific texture /
polish-is-the-tell), never on its content. No claim in either section asserts a fact about a real
person; both ground in this skill's own documented spine (`SKILL.md`) and F-stage naming
(F0-F7, `SKILL.md` lines 33-58), which pre-exist this repair and are quoted/paraphrased, not
invented.
