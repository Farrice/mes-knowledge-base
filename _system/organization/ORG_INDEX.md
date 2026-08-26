# Global Artifact Organization

Last updated: 2026-08-26T07:22:39+00:00
Total indexed files: 44914

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

- `_active`: 15299
- `skills`: 13245
- `.agent`: 5255
- `extractions`: 4267
- `.agents`: 2569
- `documents_codex`: 2124
- `execution`: 530
- `deliverables`: 463
- `agents`: 453
- `knowledge`: 205
- `docs`: 129
- `directives`: 113
- `research_outputs`: 100
- `_system`: 94
- `semantic_libraries`: 49
- `strategy_briefs`: 10
- `projects`: 9

## Counts By Domain

- `System`: 19996
- `Creative`: 6548
- `Extraction`: 12827
- `Revenue`: 1027
- `Client`: 945
- `Research`: 1940
- `Content`: 861
- `Ops`: 231
- `Personal`: 539

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
