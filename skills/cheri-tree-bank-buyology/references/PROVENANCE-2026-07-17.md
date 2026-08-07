# PROVENANCE — cheri-tree-bank-buyology repair

Anchor → source file + location. All sources are files already inside this repo,
verified present via direct file reads (not assumed). No `extractions/`-top-level
entry exists for this expert; ground truth used instead is the skill's own existing
reference files plus the codex-harvest architecture/vision docs.

| Anchor text used in genius.md | Source file | Location |
|---|---|---|
| "the four B.A.N.K. types: Blueprint, Action, Nurturing, Knowledge" | `skills/cheri-tree-bank-buyology/references/source-notes.md` | line 9 |
| "Use only short calibration excerpts if needed. Most outputs should be transformed methodology, original business assets, and operational prompts." | `skills/cheri-tree-bank-buyology/references/source-notes.md` | line 17 |
| "A person's full code is an ordered stack, not a single label." | `skills/cheri-tree-bank-buyology/references/bank-code-field-guide.md` | "Code Order" section, line ~45 |
| Blueprint Avoid list quote ("chaos, delays, exaggeration...") | `skills/cheri-tree-bank-buyology/references/bank-code-field-guide.md` | "Blueprint" section, line 9 |
| Action Avoid list quote ("boredom, budgets, details...") | `skills/cheri-tree-bank-buyology/references/bank-code-field-guide.md` | "Action" section, line 19 |
| Nurturing Avoid list quote ("arguments, coldness, deceit...") | `skills/cheri-tree-bank-buyology/references/bank-code-field-guide.md` | "Nurturing" section, line 29 |
| Knowledge Avoid list quote ("blanket statements, drama...") | `skills/cheri-tree-bank-buyology/references/bank-code-field-guide.md` | "Knowledge" section, line 39 |
| "A pitch delivered before code diagnosis is a guess." | `skills/cheri-tree-bank-buyology/references/genius-patterns.md` | Pattern 1, line 5 |
| "The method should help the right buyer understand the right offer. It should not pressure a poor-fit buyer into a bad decision." | `skills/cheri-tree-bank-buyology/references/genius-patterns.md` | Pattern 10, lines 59-60 |
| "If code insights stay in the seller's head, they disappear. If code is stored and routed, the whole business can send better messages." | `skills/cheri-tree-bank-buyology/references/hidden-knowledge.md` | "CRM Is Where B.A.N.K. Becomes Compounding", lines 33-34 |
| "12" downstream workflows claim | `skills/cheri-tree-bank-buyology/SKILL.md` | workflow table, 12 rows counted directly |
| Extraction dating "2026-06-11" | `_active/harness/codex-harvest-2026-06-11/extractions/cheri-tree-bank-buyology/architecture.md`, `vision.md` | Directory name + `git log --diff-filter=A --date=short` confirms both files added 2026-06-11 |
| Reference-file dating "2026-07-02" | `skills/cheri-tree-bank-buyology/references/*.md`, `genius.md` | `git log --diff-filter=A --date=short` confirms all added 2026-07-02 |

## Absence verification (per envelope hard rule 2)

Claim: no `extractions/` coverage exists for this expert.

Verification performed:
- `ls extractions/ | grep -i cheri` → empty (193 total top-level entries in `extractions/`)
- `find . -iname "*why they buy*"` and `find . -iname "*.pdf"` (filtered buy/bank/tree) → zero hits, run 2026-07-17
- Found instead: `_active/harness/codex-harvest-2026-06-11/extractions/cheri-tree-bank-buyology/` (a different, non-top-level path) containing `architecture.md` (771 bytes) and `vision.md` (997 bytes) — both read in full. Neither contains a verbatim quote from *Why They Buy*; both are structural/synthesis notes (workflow list, capability-gap framing).
- File sizes recorded via `wc -c`, not `wc -l`, per envelope instruction.

Conclusion: absence of a primary-source extraction is real, not an unread-file false
claim. Ground truth for this repair is the skill's own existing reference files
(committed 2026-07-02), which are themselves AI-synthesized field notes, not the
original book text.
