# Provenance — ali-abdaal-action-bias repair (2026-07-17)

Anchor → source file + location table for every new/changed claim.
Full claim-by-claim labeling lives in `references/source-ledger.md`;
this table is the quick anchor lookup.

| Anchor in repaired genius.md | Source file | Location |
|---|---|---|
| "Most decisions are reversible—treat them that way" | `agents/ali-abdaal/AGENT.md` | Core Philosophy bullet list, line 11 |
| "70% confident = enough to act" | `agents/ali-abdaal/AGENT.md` | Core Philosophy bullet list, line 14 |
| "Inaction has a cost; calculate it" | `agents/ali-abdaal/AGENT.md` | Core Philosophy bullet list, line 12 |
| "Gently challenging without judgment" | `agents/ali-abdaal/AGENT.md` | Voice & Style bullet list, line 22 |
| Experiment Cycle (Hypothesis → Minimum test → Learn → Iterate) | `skills/ali-abdaal-action-bias/SKILL.md`, `SKILL.md.old`, `agents/ali-abdaal/AGENT.md` | SKILL.md intro paragraph; SKILL.md.old "Key Frameworks"; AGENT.md Core Philosophy — identical phrasing in all three |
| Two-Minute Rule / Minimum Viable Output / Perfect Plan Trap exemplars | `skills/ali-abdaal-action-bias/genius.md` (pre-repair) | Hall of Fame Exemplars section — carried forward unchanged, provenance note added |
| Score-4 rubric rows (used as Anti-Pattern anchors) | `skills/ali-abdaal-action-bias/genius.md` (pre-repair) | Expert-Specific Quality Rubric table, "Score 4 (Acceptable)" column — carried forward unchanged |
| 2026-04-09 Evolution Log entry (5.7→8.3) | `skills/ali-abdaal-action-bias/genius.md` (pre-repair) | Evolution Log section — carried forward unchanged |
| "No genius patterns extracted yet" corroboration | `evolution_store/v2_variants/genius_compressed/ali-abdaal-action-bias_genius.md` | Line 13, "Genius Patterns (Compressed)" section — independent file stating the same absence |
| 193-entry `extractions/` count, 0 Abdaal matches | Direct `ls extractions/ \| wc -l` + `grep -i abdaal` run this session | Recorded in `references/source-ledger.md` |
| File sizes (SKILL.md 5,621B, genius.md 8,070B, AGENT.md 1,639B, etc.) | Direct `wc -c` run this session | Recorded in `references/source-ledger.md` table |

No anchor in this table cites a primary Ali Abdaal transcript, podcast,
or interview — none exists in this repo. Every anchor is a real,
on-disk repo file. Where the underlying claim (a "quote" attributed to
Ali Abdaal) cannot itself be verified against a primary source, it is
labeled UNCONFIRMED in `genius.md` and `references/source-ledger.md`,
not silently presented as verified.
