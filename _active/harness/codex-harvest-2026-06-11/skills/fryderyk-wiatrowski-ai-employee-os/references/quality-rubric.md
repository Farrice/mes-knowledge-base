# AI Employee OS Quality Rubric

| Criterion | Weak | Good | Excellent |
|---|---|---|---|
| Role definition | Generic assistant | Named role and job | Job, non-job, owner, escalation, cadence |
| Surface fit | New app by default | Surface named | Surface expectations, latency, and events mapped |
| Context isolation | Mixed context | Basic boundaries | Tested partitions, leakage checks, and handoffs |
| Integrations | Tool list | Scoped tools | Owner, permissions, approvals, audit, revocation |
| Event handling | Last prompt only | Threads considered | Edits/deletes/reactions/thread drift mapped |
| Proactivity | Interrupts freely | Suggests with care | Trust ladder with kill switches |
| Regression | Tests output only | Tests model quality | Tests task, tone, trust, leakage, and drift |
| Rollout | Big launch | Small pilot | Evidence-backed staged activation |
