---
name: anchor-named-discipline
enabled: false
event: stop
action: warn
conditions:
  - field: transcript
    operator: contains_any
    pattern: "--intent 8|--intent 9|--intent 10|--expert-score 8|--expert-score 9|--expert-score 10|--adversarial 8|--adversarial 9|--adversarial 10|expert_standard.*[89]\\.\\d|composite_score.*[89]\\.\\d"
  - field: transcript
    operator: not_contains
    pattern: "--anchor-named|anchor_named=True|anchor_named.*true|Anchor 9|Anchor 8|matches the Anchor"
---

**Anchor-Named**: a finalize self-scored ≥8 without `--anchor-named` or a named rubric anchor — the taste filter already capped it at 7.5 (`taste_signature.py` Rule 2); either name the anchor and re-finalize, or accept the cap silently. Can't name it → the score was aspiration, not measurement (`evolution_store/ground_truth/rubric_v1.md`).
