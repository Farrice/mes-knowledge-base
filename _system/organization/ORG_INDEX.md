# Global Artifact Organization

Last updated: 2026-09-13T12:34:05+00:00
Total indexed files: 51713

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

- `_active`: 18062
- `skills`: 13692
- `extractions`: 5953
- `.agent`: 5879
- `.agents`: 2713
- `documents_codex`: 2652
- `deliverables`: 779
- `execution`: 658
- `agents`: 458
- `knowledge`: 206
- `docs`: 162
- `directives`: 119
- `projects`: 110
- `_system`: 106
- `research_outputs`: 100
- `semantic_libraries`: 54
- `strategy_briefs`: 10

## Counts By Domain

- `System`: 21629
- `Creative`: 7767
- `Extraction`: 14578
- `Revenue`: 1933
- `Client`: 1110
- `Research`: 2248
- `Content`: 1370
- `Ops`: 252
- `Personal`: 826

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
