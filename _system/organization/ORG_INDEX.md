# Global Artifact Organization

Last updated: 2026-08-04T23:19:15+00:00
Total indexed files: 33638

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

- `skills`: 12782
- `_active`: 9387
- `.agent`: 4254
- `extractions`: 3001
- `documents_codex`: 1501
- `.agents`: 1041
- `agents`: 442
- `execution`: 420
- `knowledge`: 195
- `deliverables`: 186
- `directives`: 108
- `docs`: 100
- `research_outputs`: 91
- `_system`: 75
- `semantic_libraries`: 36
- `strategy_briefs`: 10
- `projects`: 9

## Counts By Domain

- `System`: 14843
- `Creative`: 1546
- `Extraction`: 11869
- `Revenue`: 299
- `Client`: 1053
- `Research`: 2470
- `Content`: 1049
- `Ops`: 188
- `Personal`: 321

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
