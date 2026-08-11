# Global Artifact Organization

Last updated: 2026-08-11T02:12:27+00:00
Total indexed files: 32409

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

- `skills`: 13057
- `_active`: 7449
- `.agent`: 4108
- `extractions`: 2699
- `documents_codex`: 2028
- `.agents`: 1051
- `execution`: 503
- `agents`: 452
- `deliverables`: 366
- `knowledge`: 203
- `docs`: 126
- `directives`: 113
- `research_outputs`: 96
- `_system`: 92
- `semantic_libraries`: 47
- `strategy_briefs`: 10
- `projects`: 9

## Counts By Domain

- `System`: 15697
- `Creative`: 1662
- `Extraction`: 11164
- `Revenue`: 1009
- `Client`: 929
- `Research`: 484
- `Content`: 753
- `Ops`: 204
- `Personal`: 507

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
