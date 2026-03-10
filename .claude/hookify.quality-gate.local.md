---
name: quality-gate-enforcement
enabled: true
event: stop
action: warn
conditions:
  - field: transcript
    operator: contains_any
    pattern: genius.md|SKILL.md|expert_auto_routing|invocation-cards
  - field: transcript
    operator: not_contains
    pattern: Quality Gate|quality_score|Intent Alignment|Expert Standard|Adversarial Resilience|score.*\/10
---

**Quality Gate Required**: An expert skill was loaded this session but no quality gate check was detected. Before delivering this output, run the 3-point silent check:

1. **Intent Alignment** (1-10): Does the output match what the user actually asked for?
2. **Expert Standard** (1-10): Would the real expert behind this skill approve this output?
3. **Adversarial Resilience** (1-10): Would this hold up under scrutiny?

Then log via `python execution/log_performance.py log "description" --skill SKILL --type TYPE --quality SCORE --status Keep`. Protocol: `directives/quality_gate.md`.
