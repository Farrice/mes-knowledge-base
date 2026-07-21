# Global Artifact Organization

Last updated: 2026-07-21T15:53:22+00:00
Total indexed files: 29764

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
- `.agent`: 2735
- `.agents`: 1041
- `agents`: 438
- `execution`: 377
- `deliverables`: 214
- `knowledge`: 192
- `directives`: 103
- `research_outputs`: 86
- `docs`: 65
- `_system`: 41
- `semantic_libraries`: 35
- `documents_codex`: 32
- `strategy_briefs`: 10

## Counts By Domain

- `System`: 12210
- `Creative`: 1338
- `Extraction`: 11397
- `Revenue`: 179
- `Client`: 1029
- `Research`: 2404
- `Content`: 846
- `Ops`: 161
- `Personal`: 200

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
