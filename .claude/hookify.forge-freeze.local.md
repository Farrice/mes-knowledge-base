---
name: forge-freeze-check
enabled: true
event: stop
action: warn
conditions:
  - field: transcript
    operator: contains_any
    pattern: "/extract-forge|/extract |extract-forge|forge extraction"
  - field: transcript
    operator: not_contains
    pattern: "forge_gate\\.py|FORGE GATE"
---

**Forge Gate Skipped**: An extraction workflow ran but `execution/forge_gate.py check` was never invoked.

The extraction freeze is non-optional: no new extraction until the most recent one has ≥3 production uses (Sean Macintyre: 17 workflows, 0 uses in 6 weeks; audit 2026-04-24: "the growth curve has flipped from accretive to dilutive").

Run now and present the result:

```bash
python3 execution/forge_gate.py check
```

If the gate is closed, the extraction should not have happened — surface this to Farrice with the gate's options (deploy the last extraction / enrich an A-tier genius.md / logged `--force` override). Also confirm `forge_gate.py record <skill-dir>` ran if an extraction completed.
