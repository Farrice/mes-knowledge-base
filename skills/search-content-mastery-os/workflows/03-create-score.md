---
description: "Route an approved SearchBrief to existing producers, then create a transparent cross-format score receipt."
menu_exempt: "Routed through /search-content-mastery create or score."
---

# Search Content Mastery — Create And Score

## Diagnose Before Treat

Confirm the SearchBrief is `APPROVED`, its sources still resolve, and the selected channel/object matches the intent. Do not start production from a topic alone.

## Execution

1. Create the production handoff:

   ```bash
   python3 execution/search_content_mastery.py create --project <path> --brief <brief.json>
   ```

2. Load the routed producer and matching craft master. For Farrice-authored content, load the Voice Card first.
3. Production ends at a local artifact. Paid generation and external publication require explicit approval.
4. Score the artifact:

   ```bash
   python3 execution/search_content_mastery.py score --project <path> --brief <brief.json> --content <asset> [--expert-judgment <judgment.json>] [--override <override.json>]
   ```

5. Return weak dimensions to the exact producer; do not rebuild unaffected sections.

## Output Schema

- Production handoff path and route.
- Local asset path.
- Deterministic checks per dimension.
- Bounded expert judgment.
- Original composite, optional operator override, and final composite.
- `PREDICTED` proof state and remaining market gap.

## Quality Gate

- Brief approval is explicit.
- Matching craft instructions were loaded.
- Original score survives an override.
- Score does not create an outcome event.
- Claims and CTA respect the brief boundary.

Execution prompt: `references/prompts-v2/content-score-receipt.md` — honor its Output Contract.

