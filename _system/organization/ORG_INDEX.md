# Global Artifact Organization

Last updated: 2026-07-21T16:24:52+00:00
Total indexed files: 29773

## Canonical Project Shape

Active projects live under `_active/<project-slug>/` with:

- `00-start-here/`
- `01-source/`
- `02-research/`
- `03-working-drafts/`
- `04-deliverables/`
- `05-assets/`
- `06-system/`
- `90-exports/`
- `99-archive/`

## Counts By Root

- `skills`: 12440
- `_active`: 6451
- `extractions`: 2753
- `projects`: 2751
- `.agent`: 2738
- `.agents`: 1041
- `agents`: 438
- `execution`: 378
- `deliverables`: 214
- `knowledge`: 192
- `directives`: 103
- `research_outputs`: 86
- `docs`: 66
- `_system`: 45
- `semantic_libraries`: 35
- `documents_codex`: 32
- `strategy_briefs`: 10

## Counts By Domain

- `System`: 12215
- `Creative`: 1338
- `Extraction`: 11397
- `Revenue`: 179
- `Client`: 1031
- `Research`: 2404
- `Content`: 846
- `Ops`: 162
- `Personal`: 201

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
