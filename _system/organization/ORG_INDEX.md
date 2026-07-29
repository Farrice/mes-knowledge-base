# Global Artifact Organization

Last updated: 2026-07-29T04:49:36+00:00
Total indexed files: 31236

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

- `skills`: 12616
- `_active`: 9245
- `.agent`: 3747
- `extractions`: 2908
- `.agents`: 1041
- `agents`: 442
- `execution`: 411
- `knowledge`: 195
- `deliverables`: 186
- `directives`: 107
- `docs`: 94
- `research_outputs`: 89
- `_system`: 69
- `semantic_libraries`: 35
- `documents_codex`: 32
- `strategy_briefs`: 10
- `projects`: 9

## Counts By Domain

- `System`: 13322
- `Creative`: 1342
- `Extraction`: 11639
- `Revenue`: 192
- `Client`: 1025
- `Research`: 2438
- `Content`: 893
- `Ops`: 171
- `Personal`: 214

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
