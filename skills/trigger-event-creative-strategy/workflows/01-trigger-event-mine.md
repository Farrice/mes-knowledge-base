---
name: "Trigger-Event Miner"
produces: "Trigger-Event Evidence Bank"
load_context: "genius.md"
---

# Trigger-Event Miner

## Input

Voice-of-customer corpus, product/offer context, audience, source labels, and claim constraints.

## Workflow

1. Recall approved project lessons with `creative_intelligence.py recall`.
2. When the corpus is CSV, run `python3 execution/review_miner.py <csv> --out .tmp/review-mine/` and inspect `trigger-event-candidates.md`.
3. Test each candidate for event, prior problem, intolerance transition, subsequent action, and provenance.
4. Separate `VERIFIED`, `LIKELY`, and `UNCONFIRMED`; reject generic benefits and invented connective tissue.
5. Rank by recognition, specificity, consequence, audience fit, and claim safety.
6. Produce the Evidence Bank and hand its top events to Workflow 02.

Execution prompt: `references/prompts-v2/trigger-event-evidence-bank.md` — honor its Output Contract.

## Quality Gate

- Every selected event has exact evidence.
- Generic benefit language is rejected.
- Inference is visible.
- No quote is polished into a different story.
