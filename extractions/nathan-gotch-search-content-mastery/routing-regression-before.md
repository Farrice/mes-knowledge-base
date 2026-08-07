# Routing Regression — Before Build

Date: 2026-08-04

## Natural-Language Request

> Build a source-grounded Search Content Mastery OS from Nathan Gotch videos with SEO AEO GEO evaluation, import-first outcome measurement, and Health Performance pilot.

## Observed Wrong Behavior

- `execution/codex_operator_preflight.py` chose `/health-check`.
- `execution/virtuoso_orchestration.py` classified the request as `health-check-status` with `0.94` confidence and assigned Health Check as owner.
- The same traces also found `source-to-skill-system` as the source-to-system handoff and retrieved Nathan Gotch and Ethan Smith context.
- `execution/workflow_router.py` surfaced `/geo-content`, `/aeo-content-weaponization-plan`, and `/gotch-content-engine`, but no unified command.

## Expected Behavior After Build

The exact request and closely related phrases must surface `/search-content-mastery` first. Health checks remain available for genuine read-only harness-status requests.

## Regression Boundary

Do not repair this by globally hijacking the word `health`. Match the combined intent shape: search/SEO/AEO/GEO plus project-system verbs such as build, audit, plan, create, score, measure, evaluate, or service.

