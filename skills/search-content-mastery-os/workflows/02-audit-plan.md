---
description: "Audit project readiness and turn one opportunity into a source-referenced SearchBrief."
menu_exempt: "Routed through /search-content-mastery audit or plan."
---

# Search Content Mastery — Audit And Plan

## Diagnose Before Treat

Find the upstream constraint first: eligibility, live intent, wrong object/page type, missing source, weak information gain, channel mismatch, conversion leak, or measurement gap.

## Execution

1. Validate project truth:

   ```bash
   python3 execution/search_content_mastery.py audit --project <path>
   ```

2. Load only the relevant Nathan or Ethan workflow and exact evidence rows.
3. Evaluate core surfaces first; activate local, ecommerce, YouTube/social, or app branches only when the project requires them.
4. Produce a strict SearchBrief input with target query, intent, audience, gain, sources, structural pattern, channel, CTA, risk, and falsifiable measurement hypothesis.
5. Create the record:

   ```bash
   python3 execution/search_content_mastery.py plan --project <path> --input <brief-input.json>
   ```

## Output Schema

- Baseline audit receipt.
- One opportunity decision and rejected alternatives.
- SearchBrief ID/path.
- Source and risk receipts.
- Next approval gate.

## Quality Gate

- Live/source evidence chose the object.
- Information gain is explicit.
- Unknown data is labeled, not inferred.
- Measurement hypothesis includes a falsifier and window.
- No outcome guarantee appears.

Execution prompt: `references/prompts-v2/search-audit-opportunity-map.md` and `references/prompts-v2/search-brief.md` — honor their Output Contracts.

