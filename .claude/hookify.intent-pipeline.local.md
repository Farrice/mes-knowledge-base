---
name: intent-pipeline-check
enabled: true
event: stop
action: warn
conditions:
  - field: transcript
    operator: contains_any
    pattern: genius.md|SKILL.md|invocation-cards|expert_auto_routing|DOMAIN_REGISTRY
  - field: transcript
    operator: not_contains
    pattern: Score.*\/5|intent.*score|DICE.*score|sharpness|Stage 1|SCORE.*intent
---

**Intent Pipeline Skipped**: An expert was routed but no intent scoring (Stage 1 SCORE) was detected. For non-trivial requests, score intent sharpness 1-5 before routing:

Has deliverable? (+1) | Audience? (+1) | Context/constraints? (+1) | End state? (+1) | Specific language? (+1)

Skip conditions: trivial questions, follow-ups, "just do it", bug fixes. Protocol: `directives/intent-pipeline.md`.
