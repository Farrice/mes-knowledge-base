# Source Ledger — ali-abdaal-action-bias

Repair pass 2026-07-17 (Wave 3 Lane 4 Batch 1). Every claim in
`SKILL.md` and `genius.md` labeled VERIFIED / LIKELY / UNCONFIRMED
against what was actually found on disk.

## Search performed (absence verified, not assumed)

Per the envelope's rule 2 ("a claim that sources are ABSENT is itself a
provenance claim"), the following searches were run and their results
recorded with real file sizes (`wc -c`, not `wc -l`):

- `ls extractions/ | grep -i abdaal` → 0 results (extractions/ has 193
  total entries; none named for Ali Abdaal).
- `find extractions -iname "*abdaal*"` → 0 results.
- `find . -iname "*abdaal*"` (repo-wide, excluding worktrees) → 7 hits,
  all listed below with sizes. None is a primary transcript, interview,
  or podcast source — all are derivative skill/agent/command files
  generated from (or duplicating) the same unsourced content.

## Files consulted (real, on-disk, sized)

| File | Size (wc -c) | What it is |
|---|---|---|
| `skills/ali-abdaal-action-bias/SKILL.md` | 5,621 bytes | Current skill card (this repair's baseline) |
| `skills/ali-abdaal-action-bias/genius.md` | 8,070 bytes | Current genius file (this repair's baseline) |
| `skills/ali-abdaal-action-bias/SKILL.md.old` | 2,668 bytes | Prior skill-card version; same framework claims, no additional sourcing |
| `agents/ali-abdaal/AGENT.md` | 1,639 bytes | Agent persona card; source of the "Two-Way Door," "70% confident," and "Overthinking Tax" phrasing used in genius.md patterns |
| `_active/codex-harvest-2026-06-11/skills/ali-abdaal-action-bias/SKILL.md` | 1,874 bytes | Harvested duplicate, same claims, no citations |
| `_active/codex-harvest-2026-06-11/agents/ali-abdaal/AGENT.md` | 2,353 bytes | Harvested duplicate of AGENT.md + a generic "Routing Interop" block (diffed against current AGENT.md — the only delta, unrelated to sourcing) |
| `evolution_store/v2_variants/genius_compressed/ali-abdaal-action-bias_genius.md` | 4,395 bytes | Compressed variant of genius.md; independently states "No genius patterns extracted yet" — corroborates that no primary extraction ever ran |
| `.agents/skills/source-command-ali-abdaal/SKILL.md` | 1,399 bytes | Auto-generated command shim (`sync_registries.py`); points back at the same SKILL.md/genius.md, adds no source |
| `.claude/commands/ali-abdaal-action-bias.md`, `.claude/commands/ali-abdaal.md` | 1,230 / 1,331 bytes | Slash-command wrappers; no independent content |

**Conclusion**: this skill was built without a primary Ali Abdaal
transcript, interview, or podcast file ever entering the repo. The
`genius.md` file's own placeholder text ("No genius patterns extracted
yet. Run extraction to populate.") — echoed independently in the
`evolution_store` compressed variant — is direct evidence of this, not
an oversight to paper over.

## Claim-by-claim labels

| Claim | Label | Basis |
|---|---|---|
| Ali Abdaal is a real productivity-content creator this extraction is modeled on | LIKELY | Public figure, consistent with general knowledge; not independently re-verified via web search in this repair pass (out of scope — this repair touches provenance labeling, not fresh research) |
| "Most decisions are reversible—treat them that way" (Two-Way Door) | UNCONFIRMED | Present verbatim in `agents/ali-abdaal/AGENT.md`; no transcript/interview file exists to confirm it is an actual Ali Abdaal quote vs. paraphrase-as-extraction |
| "70% confident = enough to act" (Certainty Threshold) | UNCONFIRMED | Same basis as above — present in AGENT.md, no primary source |
| "Inaction has a cost; calculate it" (Overthinking Tax) | UNCONFIRMED | Same basis — present in AGENT.md, no primary source |
| Experiment Cycle: Hypothesis → Minimum test → Learn → Iterate | UNCONFIRMED (but internally consistent) | Recurs identically across SKILL.md, SKILL.md.old, AGENT.md — cross-file consistency is evidence of deliberate design, not evidence of a verified external quote |
| "Two-Minute Rule" exemplar excerpt | UNCONFIRMED | No transcript file locatable; excerpt is illustrative extraction-era prose, not a citable verbatim quote |
| "Minimum Viable Output" podcast exemplar excerpt | UNCONFIRMED | Same basis |
| "Perfect Plan Trap" anti-exemplar excerpt | UNCONFIRMED | Same basis |
| 2026-04-09 Evolution Log entry (Diagnostic Action Sequencing, 5.7→8.3) | VERIFIED | Internal to this repo — the benchmark scores and hypothesis are this system's own evolution-run record, not an Abdaal attribution; verifiable by reading `genius.md`'s own Evolution Log section, which predates this repair |
| Workflow files carry Output Schema + Quality Gate | VERIFIED | Confirmed by `execution/skill_auditor.py` heartbeat check (workflow_contracts: PASS, unchanged by this repair) |

## What this repair did NOT do

- Did not invent a new Ali Abdaal quote, date, or episode citation to
  make the anti-pattern/entity checks pass artificially — every added
  anchor points to a real on-disk file (SKILL.md, AGENT.md, genius.md's
  own rubric) rather than a fabricated external source.
- Did not attempt a fresh web/transcript search to backfill a primary
  source — out of scope for a heartbeat-check repair; flagged here as a
  gap for a future extraction pass (`/extract-forge ali-abdaal` against
  a real source video/podcast would close it).
