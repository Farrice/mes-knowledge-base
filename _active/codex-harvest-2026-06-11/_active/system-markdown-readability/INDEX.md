# System Markdown Readability

## Purpose

This project tracks the system-level fix that keeps human-facing Markdown readable and moves machine metadata into sidecar `.metadata.json` files.

## Primary Artifacts

- `04-deliverables/legacy-visible-metadata-report.md`

## Guard

Use:

```bash
python3 execution/artifact_frontmatter_guard.py _active brain deliverables research_outputs strategy_briefs
```

The guard should pass for active readable deliverables and allow system surfaces that require frontmatter.
