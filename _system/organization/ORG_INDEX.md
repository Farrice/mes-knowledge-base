# Global Artifact Organization

Last updated: 2026-07-24T22:42:37+00:00
Total indexed files: 30090

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

- `skills`: 12504
- `_active`: 6474
- `extractions`: 2884
- `.agent`: 2818
- `projects`: 2751
- `.agents`: 1041
- `agents`: 440
- `execution`: 383
- `deliverables`: 214
- `knowledge`: 193
- `directives`: 103
- `research_outputs`: 87
- `docs`: 72
- `_system`: 49
- `semantic_libraries`: 35
- `documents_codex`: 32
- `strategy_briefs`: 10

## Counts By Domain

- `System`: 12330
- `Creative`: 1338
- `Extraction`: 11548
- `Revenue`: 179
- `Client`: 1040
- `Research`: 2411
- `Content`: 860
- `Ops`: 177
- `Personal`: 207

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
