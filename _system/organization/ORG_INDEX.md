# Global Artifact Organization

Last updated: 2026-07-15T18:26:29+00:00
Total indexed files: 27440

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

- `skills`: 11365
- `_active`: 6405
- `projects`: 2751
- `.agent`: 2296
- `extractions`: 2074
- `.agents`: 1041
- `agents`: 430
- `execution`: 364
- `deliverables`: 207
- `knowledge`: 188
- `directives`: 98
- `research_outputs`: 74
- `docs`: 50
- `semantic_libraries`: 35
- `documents_codex`: 32
- `_system`: 21
- `strategy_briefs`: 9

## Counts By Domain

- `System`: 11499
- `Creative`: 1283
- `Extraction`: 9982
- `Revenue`: 172
- `Client`: 1006
- `Research`: 2373
- `Content`: 810
- `Ops`: 126
- `Personal`: 189

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
