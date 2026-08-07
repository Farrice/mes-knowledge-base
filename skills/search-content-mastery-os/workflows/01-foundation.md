---
description: "Create or validate the portable search project truth pack before analysis or production."
menu_exempt: "Routed through /search-content-mastery foundation."
---

# Search Content Mastery — Foundation

## Diagnose Before Treat

Determine whether the current project already has explicit entity, brand/offer/audience/voice, source, claim, competitor, search-input, and operator-taste records. Do not treat prose in the current chat as portable truth.

## Execution

1. Load `references/data-contract.md`.
2. Create the pack:

   ```bash
   python3 execution/search_content_mastery.py foundation --project <path> --name <name> --vertical <vertical> [--context <strict.json>]
   ```

3. Fill missing context through explicit files. Never guess unknown project facts.
4. Validate with `foundation --resume` and then run `audit`.
5. Keep all external actions `NO PERMISSION`.

## Output Schema

- Manifest path and project ID.
- Context-file inventory with populated/gap state.
- Boundaries and proof state.
- First downstream audit command.

## Quality Gate

- Every context reference exists and parses.
- Project truth is separate from source inference.
- Outcome and recommendation ledgers are append-only.
- No external connector, scheduler, publisher, or payment surface exists.

Execution prompt: `references/prompts-v2/search-project-foundation.md` — honor its Output Contract.

