---
name: performance-log-reminder
enabled: true
event: stop
action: warn
conditions:
  - field: transcript
    operator: contains_any
    pattern: genius.md|SKILL.md|workflows/extract|workflows/brief|workflows/council|workflows/ghostwrite|workflows/storybrand|workflows/ad-script|workflows/nuclear-vsl|workflows/full-stack-ad|workflows/icp-deep-dive|workflows/brand-arena|workflows/campaign-architect
  - field: transcript
    operator: not_contains
    pattern: log_performance|Performance Log|performance_log
---

**Performance Log Missing**: A major workflow or expert skill was used but no performance log entry was created. Log the output quality to feed the autoresearch feedback loop:

```bash
python execution/log_performance.py log "Brief description of what was produced" --skill SKILL_NAME --type TYPE --quality SCORE --status Keep
```

Without performance data, Skill Evolution (Phase 2), Cross-Pollination (Phase 3), and Gap Detection (Phase 4) cannot activate. Protocol: `directives/feedback-ratchet.md`.
