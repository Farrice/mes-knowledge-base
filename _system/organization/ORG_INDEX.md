# Global Artifact Organization

Last updated: 2026-08-30T12:32:06+00:00
Total indexed files: 46010

## Permitted Project Shape (instantiated only when populated)

Active projects live under `_active/<project-slug>/`. These are the *permitted* folders — each is created only when a file actually lands in it. Never pre-create the set: an empty subfolder is a lie about content.

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

- `_active`: 15601
- `skills`: 13292
- `.agent`: 5359
- `extractions`: 4608
- `.agents`: 2591
- `documents_codex`: 2373
- `execution`: 539
- `deliverables`: 476
- `agents`: 455
- `knowledge`: 205
- `docs`: 132
- `directives`: 113
- `research_outputs`: 100
- `_system`: 98
- `semantic_libraries`: 49
- `strategy_briefs`: 10
- `projects`: 9

## Counts By Domain

- `System`: 20174
- `Creative`: 6587
- `Extraction`: 13177
- `Revenue`: 1040
- `Client`: 966
- `Research`: 1947
- `Content`: 1115
- `Ops`: 238
- `Personal`: 766

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
