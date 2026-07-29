# Global Artifact Organization

Last updated: 2026-07-29T04:08:19+00:00
Total indexed files: 31161

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
- `_active`: 6519
- `.agent`: 3639
- `extractions`: 2908
- `projects`: 2751
- `.agents`: 1041
- `agents`: 442
- `execution`: 409
- `deliverables`: 215
- `knowledge`: 195
- `directives`: 107
- `docs`: 94
- `research_outputs`: 89
- `_system`: 59
- `semantic_libraries`: 35
- `documents_codex`: 32
- `strategy_briefs`: 10

## Counts By Domain

- `System`: 13207
- `Creative`: 1343
- `Extraction`: 11641
- `Revenue`: 187
- `Client`: 1067
- `Research`: 2417
- `Content`: 889
- `Ops`: 197
- `Personal`: 213

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
