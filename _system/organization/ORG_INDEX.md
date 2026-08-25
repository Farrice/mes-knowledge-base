# Global Artifact Organization

Last updated: 2026-08-25T04:52:37+00:00
Total indexed files: 44822

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

- `_active`: 15294
- `skills`: 13245
- `.agent`: 5255
- `extractions`: 4267
- `.agents`: 2569
- `documents_codex`: 2058
- `execution`: 530
- `agents`: 453
- `deliverables`: 448
- `knowledge`: 205
- `docs`: 128
- `directives`: 113
- `research_outputs`: 99
- `_system`: 90
- `semantic_libraries`: 49
- `strategy_briefs`: 10
- `projects`: 9

## Counts By Domain

- `System`: 19979
- `Creative`: 6545
- `Extraction`: 12824
- `Revenue`: 1025
- `Client`: 945
- `Research`: 1939
- `Content`: 800
- `Ops`: 230
- `Personal`: 535

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
