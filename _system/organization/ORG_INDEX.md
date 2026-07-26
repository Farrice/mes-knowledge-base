# Global Artifact Organization

Last updated: 2026-07-26T13:52:18+00:00
Total indexed files: 31009

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

- `skills`: 12573
- `_active`: 6493
- `.agent`: 3617
- `extractions`: 2897
- `projects`: 2751
- `.agents`: 1041
- `agents`: 441
- `execution`: 389
- `deliverables`: 215
- `knowledge`: 193
- `directives`: 104
- `research_outputs`: 87
- `docs`: 78
- `_system`: 53
- `semantic_libraries`: 35
- `documents_codex`: 32
- `strategy_briefs`: 10

## Counts By Domain

- `System`: 13159
- `Creative`: 1342
- `Extraction`: 11602
- `Revenue`: 182
- `Client`: 1048
- `Research`: 2413
- `Content`: 869
- `Ops`: 184
- `Personal`: 210

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
