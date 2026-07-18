# Forge OS — Source Ledger (repair-pass additions)

> forge-os is a SYSTEM skill (the live `/forge` front door), not a person extraction — verified
> by `ls extractions/ | grep -iE "forge"` (real read, 2026-07-17): zero hits. Ground truth for
> this repair is the skill's own build history: dated `docs/solutions/*.md` cards, the Wave 3
> `plugin-forge-lift-plan.md` decision doc, and the engine prompts under
> `references/prompts-v2/*.md` themselves. Every file below was opened and its byte size recorded
> with `wc -c` (never `wc -l`) at repair time, 2026-07-17. This ledger covers claims added by this
> repair pass; the pre-existing `source_ledger` check already passes via
> `references/prompts-v2/grounding-sprint.md`'s own VERIFIED/LIKELY/UNCONFIRMED label section —
> untouched by this pass.

| # | Claim | Label | Source (file : size, real `wc -c`) |
|---|---|---|---|
| 1 | SKILL.md epigraph ("The system already forges world-class artifacts FROM artifacts...") quoted verbatim as the skill's own framing | VERIFIED | `skills/forge-os/SKILL.md` (8,877 bytes), lines 8-13 — read directly, quoted character-for-character in `genius.md`. |
| 2 | "Forging from training memory is prohibited" is the skill's own stated F1 GROUND rule, tied to a 2026-07-07 failure | VERIFIED | `skills/forge-os/SKILL.md` line 39-40 (pre-existing) — "**Forging from training memory is prohibited** (docs/solutions/2026-07-07-transcript-only-extraction-generic-output.md)." |
| 3 | The Alex Suzuki DWA transcript-only extraction produced generic output; operator quote "very straightforward and to the point… didn't capture the style and essence… I wouldn't be able to use any of this to see results" | VERIFIED | `docs/solutions/2026-07-07-transcript-only-extraction-generic-output.md` (3,417 bytes) — read directly, quote confirmed verbatim (straight quotes, ellipsis character, no nested curly quotes) via direct byte inspection. |
| 4 | Prompt Forge's own engine (`prompt-forge.md`) shipped 7 hidden defects caught by a 2026-07-14 cold-start probe, fixed same-session | VERIFIED | `docs/solutions/2026-07-14-cold-start-probe-anneals-new-engine-prompts.md` (2,805 bytes) — "surfaced 7 real defects (undefined wiring steps, dangling F1 reference, frontmatter semantics only in the upstream spec, fidelity-key contradiction, ambiguous fixture placement, no rule for prompts with no owning workflow, no mechanism for the no-owning-skill case). All 7 fixed before the engine shipped." |
| 5 | Plugin Forge packaging lift was explicitly deferred/gated in the Wave 3 decision doc; "Lift now (full)" rejected because "exposure risk is the one irreversible item" | VERIFIED | `skills/forge-os/references/plugin-forge-lift-plan.md` (5,065 bytes), section 4 — read directly, both phrases quoted verbatim from the file. |
| 6 | Expert Composition Standard names "expert soup" (patched-together, overconfident, or still-generic output) as the failure F2 COMPOSE exists to prevent | VERIFIED | `docs/solutions/expert-composition-standard.md` (2,233 bytes) — "delivers an output that is patched together, overconfident, or still generic," quoted verbatim. |
| 7 | Grounding Sprint's $0-tier research call must use `--depth quick`; running the default depth is a tier violation; file was refactored 2026-07-15 | VERIFIED | `skills/forge-os/references/prompts-v2/grounding-sprint.md` (7,279 bytes), frontmatter `refactored: 2026-07-15` + line 30 — "running it without `--depth quick` at $0 tier is a tier violation," quoted verbatim. |
| 8 | The heartbeat auditor's `workflow_contracts` regex missed `## Output Contract` headings (only matched Schema/Format/Requirements), a defect caught 2026-07-17 in a different skill (luke-iha-vicious-hooks) and directly explaining why forge-os itself scored 0 workflow files pre-repair | VERIFIED | `docs/solutions/2026-07-17-repair-fleet-poc-three-failure-shapes.md` (5,899 bytes), item 1 — "14 of luke-iha-vicious-hooks' 'missing' workflow contracts existed under `## Output Contract`; the auditor regex only matches `Output Schema/Format/Requirements`," quoted verbatim. Cross-checked against `execution/skill_auditor.py` `_HB_OUTPUT_SCHEMA_RE` (line 232), which DOES accept "Output Contract" as of the current script — confirming the regex was already fixed upstream of this repair pass; forge-os's own gap was the missing `workflows/` directory, not a regex miss (see REPAIR-NOTES.md). |
| 9 | `agents/forge-os/AGENT.md` exists as the live Wave 2 self-promotion proof of the Agent Forge lane | VERIFIED | `agents/forge-os/AGENT.md` (10,620 bytes) confirmed present on disk via direct `ls`/`wc -c`; contents not line-audited in this pass (out of scope — additive skill-doc repair, not an agent-quality review). |
| 10 | Each of the 5 lane engine files (`prompt-forge.md`, `workflow-forge.md`, `grounding-sprint.md`, `agent-forge.md`, `plugin-forge.md`) already carries its own `## Output Contract` / `## Output Skeleton` / `## Quality Gate` sections, which the new `workflows/*.md` files summarize (never duplicate boilerplate-identical) | VERIFIED | All 5 files read directly at repair time; exact section content for the Output Schema / Quality Gate text in each new `workflows/*.md` file is paraphrased/cited from the corresponding engine file's real sections, confirmed via `grep -n "^## "` against each file. |

## Sizes referenced (repeat of the table above, `wc -c` re-run 2026-07-17 for this ledger)

```
    8877 skills/forge-os/SKILL.md
    7279 skills/forge-os/references/prompts-v2/grounding-sprint.md
    5065 skills/forge-os/references/plugin-forge-lift-plan.md
    3417 docs/solutions/2026-07-07-transcript-only-extraction-generic-output.md
    2805 docs/solutions/2026-07-14-cold-start-probe-anneals-new-engine-prompts.md
    5899 docs/solutions/2026-07-17-repair-fleet-poc-three-failure-shapes.md
    2233 docs/solutions/expert-composition-standard.md
   10620 agents/forge-os/AGENT.md
```
