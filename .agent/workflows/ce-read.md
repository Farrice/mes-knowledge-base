---
description: Behavioral read — change-cluster-context, likelihood not verdict
---

## Workflow: Behavioral Read (`/ce-read`)

**Expert**: Chase Hughes (Context Engineering)
**Skill**: `skills/chase-hughes-context-engineering/`

Read a person, transcript, or video by change-cluster-context: baseline → deviations (blink rate, lip compression, tongue jut, tense-shift, artery cluster, need-asymmetry), rewind ~10-15s to the trigger. Likelihood, never verdict — "there's no behavior for deception, zero."

### Steps

1. Read the skill files:
   - `skills/chase-hughes-context-engineering/SKILL.md`
   - `skills/chase-hughes-context-engineering/genius.md`
   - `skills/chase-hughes-context-engineering/references/behavior-suite.md`

2. If the source is a **video**, ground it first (per `directives/video-vision-protocol.md`):
   ```bash
   python3 execution/fetch-video-context.py "<video_url>" "subject"
   ```

3. Read and execute the workflow:
   - `skills/chase-hughes-context-engineering/workflows/ce-read.md`

4. Quality gate: Any "this means they're lying" certainty = automatic fail. Output must be a baseline + deviation clusters + a LIKELIHOOD statement, not a verdict.
