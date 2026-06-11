---
description: Campaign preset - wide council first, then Codex-native execution handoff
---

# /campaign

`/campaign` is a `/convene` preset for cross-domain campaigns with multiple deliverables.

Run the wide council first:

```bash
python3 execution/convene.py plan "[campaign mission]" --mode wide --json
```

Then use `/virtuoso` to choose the execution route for the approved deliverables:

```bash
python3 execution/virtuoso_orchestration.py "[approved campaign deliverables]" --json --workflow
```

This replaces the old JCC plugin-forwarding stub. The council creates the strategy, forks, and "what we would have missed"; Codex-native routes handle execution after Farrice chooses the fork.
