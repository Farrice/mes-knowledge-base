# Global Artifact Organization

Last updated: 2026-09-12T04:34:57+00:00
Total indexed files: 40706

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

- `skills`: 13554
- `_active`: 10124
- `.agent`: 4579
- `extractions`: 4352
- `.agents`: 2713
- `documents_codex`: 2652
- `deliverables`: 752
- `execution`: 658
- `agents`: 458
- `knowledge`: 206
- `docs`: 162
- `directives`: 118
- `projects`: 110
- `_system`: 104
- `research_outputs`: 100
- `semantic_libraries`: 54
- `strategy_briefs`: 10

## Counts By Domain

- `System`: 18810
- `Creative`: 2953
- `Extraction`: 12877
- `Revenue`: 1933
- `Client`: 1078
- `Research`: 811
- `Content`: 1363
- `Ops`: 240
- `Personal`: 641

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
