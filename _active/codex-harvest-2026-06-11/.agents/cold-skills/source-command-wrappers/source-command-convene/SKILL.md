---
name: "source-command-convene"
description: "Cold bridge for /convene Collective Genius Council"
---

# source-command-convene

Use this skill when the user asks to run the migrated source command `convene`.

## Command Template

Read and execute the workflow at `.agent/workflows/convene.md`.

This wrapper is intentionally cold-quarantined. `/convene` is deployable through
the workflow surface, but it is not hot-promoted unless later proof justifies it.
