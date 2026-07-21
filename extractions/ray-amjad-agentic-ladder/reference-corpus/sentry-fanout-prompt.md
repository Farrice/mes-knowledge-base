# Ray Amjad — Sentry Fan-Out Prompt (real artifact, from screen + narration)

> Source: video XLA-sTSJ-Wc, ~27:45-29:55. The prompt he sent to Percy (his Slack-native Claude harness) to demonstrate "let Claude kick off Claude" — one coordinator instance spawning and shepherding worker instances of itself. Corpus piece for blind-pass calibration.

```
Can you load in all the issues on Sentry affecting more than 10 users and then
send a message to the [demo] Slack channel, tagging Percy and specifying the
issue. Tell Percy to first verify the bug exists, then go all the way to
opening up a PR for that particular issue. Each instance should be a new Percy.
If Percy gets stuck, help me get unstuck and continue until all the PRs are
open. If you can't help Percy get unstuck, send me a notification to my phone
to tell me "hey, Percy is stuck on this, I can't help it."

/loop 10 minute — loop every 10 minutes until all PRs are open.
```

Observed outcome (shown on screen): ~10 Percy instances spawned, each working an issue to PR; the coordinator Percy answered workers' questions and pushed them to completion; one worker surfaced a missing-environment blocker (no Xcode/Swift toolchain) — flagged rather than faked; one anomalous output flagged for later investigation before running the next batch.

Percy harness context (his own Claude Tag equivalent): Claude Code + Codex running on cloud; skills = send-messages-via-Slack, verification, full task lifecycle, codex-second-opinion. Chosen over Claude Tag for customizability (LiveKit CLI, Playwright, custom harness) and cloud persistence (~2-hour lifecycles survive laptop shutdown). Enterprise parallels he cites: Stripe minions, Shopify River.
