# Global Artifact Organization

Last updated: 2026-08-08T19:25:03+00:00
Total indexed files: 40430

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

- `_active`: 15194
- `skills`: 13168
- `.agent`: 5167
- `extractions`: 3903
- `.agents`: 1051
- `execution`: 490
- `agents`: 450
- `deliverables`: 331
- `knowledge`: 203
- `docs`: 125
- `directives`: 112
- `research_outputs`: 92
- `_system`: 78
- `semantic_libraries`: 47
- `strategy_briefs`: 10
- `projects`: 9

## Counts By Domain

- `System`: 17024
- `Creative`: 6206
- `Extraction`: 12473
- `Revenue`: 1035
- `Client`: 371
- `Research`: 1861
- `Content`: 702
- `Ops`: 203
- `Personal`: 555

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
