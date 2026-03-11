---
description: Run a universal structural integrity audit across all skills, agents, indexes, workflows, and registries
---

# /verify — Universal System Verification

Cross-reference ALL registries against the filesystem. Catches orphaned entries, missing files, broken command mappings, and registry drift.

// turbo-all

## Steps

### 1. Run the Verification Script
```bash
python execution/verify_system.py
```

### 2. Present the Report
Display findings grouped by phase with severity badges:
- **❌ ERROR** — Broken references, phantom entries, missing critical files
- **⚠️ WARNING** — Missing optional files, structural concerns
- **ℹ️ INFO** — Nice-to-have improvements

### 3. Auto-Fix (if needed)
If index sync errors are found, offer to run:
```bash
python execution/sync_registries.py
```
Then re-verify:
```bash
python execution/verify_system.py
```

## When to Run
- After adding/removing skills, agents, or workflows
- After running `sync_registries.py` or `skill_converter.py`
- After batch operations (extractions, conversions)
- Weekly maintenance alongside `/system-audit` and `/health-check`
- When something feels "off" or routing fails unexpectedly
