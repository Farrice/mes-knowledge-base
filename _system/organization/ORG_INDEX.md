# Global Artifact Organization

Last updated: 2026-06-30T19:31:36+00:00
Total indexed files: 19797

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

- `skills`: 6851
- `_active`: 5482
- `projects`: 2673
- `.agent`: 1541
- `.agents`: 1038
- `extractions`: 1016
- `execution`: 295
- `agents`: 293
- `deliverables`: 205
- `knowledge`: 186
- `directives`: 82
- `research_outputs`: 66
- `semantic_libraries`: 33
- `docs`: 15
- `_system`: 13
- `strategy_briefs`: 8
- `brain`: 0
- `documents_codex`: 0

## Counts By Domain

- `System`: 9556
- `Creative`: 811
- `Extraction`: 5851
- `Revenue`: 134
- `Client`: 754
- `Research`: 1825
- `Content`: 624
- `Ops`: 68
- `Personal`: 174

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
