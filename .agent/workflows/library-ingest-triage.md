---
description: "/library-ingest-triage — confidence-gated review lane for ingest: Recommended/Needs-Review/Skipped, typed cards with metadata, nothing silently written (Kieran Flanagan)."
---

# Ingest Triage (Simon — Better Creating)

Deepen `/library-ingest` with a human-in-the-loop, confidence-gated review lane that kills silent-write decay.

## Steps
1. Load the Simon spine: read `skills/simon-intellectual-library-os/genius.md` (inversion, 6-property schema, §Second-Brain Expansion §Confidence-Gated Ingest Triage, decision framework, anti-patterns, rubric).
2. Read and execute the full workflow at `skills/simon-intellectual-library-os/workflows/library-ingest-triage.md` exactly as documented (Pre-Flight, Skill Acquisition, Execution, Output Requirements). Honor the Execution prompt at `references/prompts-v2/ingest-triage-review-lane.md`.
3. Run the Quality Gate (`genius.md` § Anti-Patterns + § Expert-Specific Quality Rubric) before delivering — no card writes without accept/re-route.
