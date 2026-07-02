# Global Artifact Organization

Last updated: 2026-07-01T19:54:36+00:00
Total indexed files: 20457

## Canonical Project Shape

Active projects live under `_active/<project-slug>/` with:

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

- `skills`: 6916
- `_active`: 5936
- `projects`: 2673
- `.agent`: 1644
- `.agents`: 1039
- `extractions`: 1016
- `agents`: 315
- `execution`: 305
- `deliverables`: 205
- `knowledge`: 186
- `directives`: 82
- `research_outputs`: 66
- `semantic_libraries`: 34
- `docs`: 17
- `_system`: 15
- `strategy_briefs`: 8

## Counts By Domain

- `System`: 9747
- `Creative`: 811
- `Extraction`: 5886
- `Revenue`: 130
- `Client`: 755
- `Research`: 2243
- `Content`: 640
- `Ops`: 71
- `Personal`: 174

## Router Commands

- `python3 execution/artifact_router.py inventory`
- `python3 execution/artifact_router.py classify <path>`
- `python3 execution/artifact_router.py plan`
- `python3 execution/artifact_router.py apply --plan <plan.json>`
- `python3 execution/artifact_router.py enforce <path...>`

## Policy

Project ownership wins over broad category. Unknown, duplicate, referenced, or low-confidence files go to the inbox instead of being moved automatically.
