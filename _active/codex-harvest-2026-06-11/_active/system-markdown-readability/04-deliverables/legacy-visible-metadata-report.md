# Legacy Visible Metadata Report

## Summary

The universal Markdown readability guard was upgraded to prevent human-facing Markdown from opening as metadata records. During rollout, the scan found two classes of existing files:

| Class | Count | Action |
|---|---:|---|
| Generated capture files under `brain/**/.system_generated/` | 14 | Treated as legacy machine-generated capture material and excluded from blocking closeout. |
| Active readable deliverable under `deliverables/carousel_scripts/` | 1 | Migrated visible metadata to sidecar JSON and made the Markdown open with a readable H1. |

## Active Cleanup Completed

Cleaned:

```text
deliverables/carousel_scripts/authenticity_trap_v2.md
```

Sidecar created:

```text
deliverables/carousel_scripts/authenticity_trap_v2.md.metadata.json
```

The Markdown now starts with:

```text
# The Authenticity Trap
```

## Legacy Files Reported But Not Rewritten

The remaining matches were browser/research capture files in `brain/**/.system_generated/steps/**/content.md`. They contain source metadata such as title, description, and URL. Because they are generated capture material rather than active readable deliverables, the guard now treats `.system_generated` as a machine-readable exception.

## Guard Status After Cleanup

The following broad scan passes:

```bash
python3 execution/artifact_frontmatter_guard.py _active brain deliverables research_outputs strategy_briefs
```

This means active readable Markdown surfaces are now guarded against visible metadata headers, while parser-dependent system files remain valid.
