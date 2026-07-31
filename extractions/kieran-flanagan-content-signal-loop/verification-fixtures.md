# Content Signal Loop Verification Fixtures

These ten fixtures are the regression contract approved at the Architecture Checkpoint. They test the behavior encoded in the workflow, born-v2 prompt, wrapper, and monthly feedback seams.

| # | Fixture | Failure being prevented | Required behavior |
|---|---|---|---|
| 1 | Platform omission | Idea cards appear without a recommended platform | Every idea card names a platform and platform rationale |
| 2 | No metrics | Human approval or corpus volume is mislabeled as engagement performance | Profile becomes PROVISIONAL and invents no performance |
| 3 | Stale profile | Old audience or winning-pattern context receives full confidence | Staleness warning propagates and lowers confidence |
| 4 | Pattern not topic | An old winner is paraphrased rather than structurally transferred | Repeated topic is rejected |
| 5 | Human gate | Ideation adds ideas before creator selection | Ideation stops; only selected IDs may enter queue |
| 6 | Tombstone | Killed ideas disappear and return unchanged | Compact killed-item fingerprint remains |
| 7 | Trend window | Old or undated material is presented as current | Out-of-window evidence is rejected or labeled historical |
| 8 | Finished-content veto | Ideation produces a post, script, newsletter, or carousel | Workflow stops at idea building blocks |
| 9 | Cross-session state | Queue depends on one chat's memory | All workflows resolve explicit `STATE_ROOT` assets |
| 10 | Monthly delta | Feedback silently rewrites the Winning Content Profile | Feedback proposes; monthly review approves and versions |

Run:

```text
python3 extractions/kieran-flanagan-content-signal-loop/verify_content_signal_loop.py
```

The verifier is deterministic and dependency-free. It checks the live production files, not copies stored in the extraction folder.
