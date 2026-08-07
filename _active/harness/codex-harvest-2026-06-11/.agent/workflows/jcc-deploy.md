---
description: JCC compatibility preset mapped to /deploy-council
---

# /jcc-deploy

`/jcc-deploy` is retained as a compatibility alias for users who remember the old JCC command. In Codex, it maps to `/deploy-council` and the `/convene` deploy mode.

Run:

```bash
python3 execution/convene.py plan "[mission]" --mode deploy --json
```

For multi-deliverable execution after the council strategy lands, hand off through existing Codex routes chosen by `/virtuoso` rather than a missing external JCC plugin.
