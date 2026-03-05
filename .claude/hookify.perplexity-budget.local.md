---
name: perplexity-budget-check
enabled: true
event: bash
pattern: perplexity|deep.research
action: warn
---

**Perplexity Budget Check**: $10/month budget. Before this call, verify remaining budget in `.agent/perplexity-usage.json`. Use Sonar for most queries; Deep Research for critical only. Batch queries when possible. Full policy: `directives/perplexity-usage-policy.md`.
