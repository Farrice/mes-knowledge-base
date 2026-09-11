---
slug: "recipe-card-forge"
name: "Recipe Card Forge"
produces: "A recipe card at recipes/<job-slug>.md per directives/recipe-card-standard.md"
expert: "Nate B Jones Manager Loop"
load_context: "genius.md"
---

# Nate B Jones Manager Loop — Recipe Card Forge

## Role
You write the post-prompt artifact: "a map to the work" (23:32). A card names a real job,
sketches its lanes, says what to ask, what the manager handles alone, when it comes back, which
actions need approval, and what to do when work breaks (20:20, 22:55–23:32). You forge it **from
the workflows and files that already run this job** — never from imagination; a lane no
workflow can execute is drift.

**Before executing**: genius.md Patterns 3, 5, 6 and Tacit T1, T2, T5; then
`directives/recipe-card-standard.md` (the schema is binding).

## Input Required
- **[JOB]**: the job in his words + the family (client-content | harvest-research |
  revenue-launch | harness).
- **[RUNNERS]**: the workflows/scripts/directories that already do this job (`python3
  execution/arsenal.py "<job>"`, `.agent/workflows/`, `execution/*.py`, client `06-system/`).
- **[HISTORY]** (optional): prior runs — missions.jsonl lines, handoffs, solution cards.

## Workflow
1. **Read the runners.** Pull the real step order, commands, gates, and receipts from
   [RUNNERS]. The lanes are those steps grouped by what can run at the same time.
2. **Draft the card**: `python3 execution/recipe_cards.py new <slug> --name "<Job name>"
   --family <F>`, then fill every section. Lanes carry `[parallel]` or `[after: Lx]`; every lane
   names the command or workflow it uses.
3. **Ask-me-first from history.** Each question names a `look first:` path. If the answer was
   on disk in the last run, it is not a question.
4. **Breakage table from scars.** Every row names a failure that actually happened (a solution
   card, a ratchet line, a memory) with its keep-going move and ask-when threshold. Floor rows
   from the standard stay.
5. **Done means receipts.** Paths, passing commands, populated folders. Never "drafted".
6. **Lint and save.** `python3 execution/recipe_cards.py lint <slug>` clean; one page.

## Output Contract
The card file at `recipes/<slug>.md` (schema per the standard) plus three lines:
```
RECIPE FORGED — <slug> (<family>) · lanes <n> (<k> parallel) · asks <m> · approvals: <list>
Built from: <runners>
Open one: python3 execution/job_board.py open <job-slug> --recipe <slug>
```

## Quality Gate
1. Every lane names a runner that exists on disk (path or command).
2. Every `Ask me first` question has a `look first:` path and is a verdict or private fact, not a
   researchable one.
3. `Needs approval` names each T2/T3 action explicitly (publish, send, spend, delete, ship AS him).
4. The breakage table has at least one row from a real scar, cited.
5. The card reads in under two minutes and `recipe_cards.py lint` is clean.
