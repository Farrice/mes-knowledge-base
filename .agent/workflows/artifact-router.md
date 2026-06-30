---
description: Global artifact organization router for files, documents, artifacts, project folders, deliverables, staged cleanup, canonical placement, and enforcement.
---

# /artifact-router

Use this when files, deliverables, reports, project folders, or generated artifacts need a canonical home without broad cleanup.

## Source Of Truth

Run the local router in `execution/artifact_router.py`. It owns inventory, classification, staged move plans, dated backlog maps, placement enforcement, and the organization manifest under `_system/organization/`.

## Operating Rules

- Default to read-only inventory, classification, or staged plans.
- Do not apply moves, delete files, archive broadly, or reorganize the workspace without explicit approval.
- Keep project ownership first and domain retrieval second.
- Unknown, duplicate, referenced, or low-confidence files go to review/inbox instead of automatic movement.

## Commands

```bash
python3 execution/artifact_router.py inventory
python3 execution/artifact_router.py classify <path>
python3 execution/artifact_router.py plan
python3 execution/artifact_router.py backlog-map
python3 execution/artifact_router.py enforce <path...>
```

## Verification

```bash
python3 execution/verify_artifact_router.py
python3 execution/verify_operator_cockpit.py
```
