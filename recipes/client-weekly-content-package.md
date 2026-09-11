---
job: client-weekly-content-package
name: Client weekly content package (Jen)
family: client-content
tier_default: T2
runs: 0
last_ratchet: never
---

## The job
One week of Jen's content, research to rendered assets to Drive, in her voice and register, fair-housing clean, with her only touch a thumbs-up.

## Sub-jobs / lanes
- L1 Load canon — the eight files in `/jen` LOAD order (`06-system/ENGINE-V2.md`, `CONTENT-MIX.md`, `VAULT.md`, voice profile, calibration log, client `CLAUDE.md`, `pulse/latest.md`, `WINNERS.md`); receipt in `<week>/pipeline-log.md` [parallel]
- L2 Read the week — one line in `<week>/READ.md` from `CONTENT-MIX.md` + pulse [after: L1]
- L3 Research facts — extend `04-deliverables/…/FACTS.md`; realism gate per claim; labels VERIFIED/LIKELY/UNCONFIRMED [after: L2]
- L4 Write — edit the `WEEKS` list in `build_weeks.py`; never hand-edit `COPY.md` [after: L3]
- L5 Amplify — one pen (`/alyssa-stalker-hook-reframe` + Luke Iha) + one Jen-as-herself check [after: L4]
- L6 Lint gates — `execution/fair_housing_lint.py check --file "$WEEK/COPY.md"`, `execution/prose_classifier.py check`, `execution/jen_stamp_lint.py` [after: L5]
- L7 Render — `build_weeks.py [--no-video]`; editions via `06-system/valley-editions/editions.py`; B-roll per `build_reel.py` spec [after: L6]
- L8 Deliver — `jen_os_page_thumbs.py`, `jen_os_page.py`, Drive `04 · ready to post / week-of-…`, `run_log.py manifest --set status=delivered`, `day-plan.txt` [after: L7]

## Ask me first
- Q: Any verdict on last week's posts that changes this week's mix? · look first: `jen-calibration-log.md`, `06-system/pulse/latest.md`
- Q: Which specimen is the current bar for hooks? · look first: `06-system/WINNERS.md`, memory `feedback_jen-reel-look-baseline`
- Q: Any photo or listing that must appear this week? · look first: Drive `03 · assets`, `PHOTO-SWAP.md`

## Handles alone
Canon load, research, drafting, amplification, all lints, render, thumbnails, Drive folder, day plan, run log receipts, pipeline log.

## Comes back when
- Two rejected takes on one asset (spiral brake) — packet with both takes + the brief fix
- A fact the realism gate cannot verify and the post depends on it
- The register ladder call is ambiguous ($2M+ "quiet flex" vs FTHB calm-warm)

## Needs approval
Publishing the Valley OS artifact page · anything posted publicly (Jen's own thumbs-up is the deal — never bypassed) · any paid image/video generation.

## Needs
`_active/clients/jen-listings/` tree · Drive access (`gws`) · `.venv` · her photos in Drive 03 · `build_weeks.py` for the current weeks file.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| stamp line repeats | fix in WRITE (L4), rerun `jen_stamp_lint.py` | never — it's mechanical |
| fair-housing lint exit 2 | rewrite the line, rerun; never ship over it | the claim itself is the post's point |
| placeholder photo reaching Drive | map in `PHOTO-SWAP.md`, hold the asset | no real photo exists for the slot |
| hand-edited COPY.md found | re-render from `build_weeks.py` | never |
| Drive export fails | `project_drive-export-via-mcp-fallback` route | both routes fail |

## Done means
`python3 execution/run_log.py check "$WEEK"` → PASS (9 receipts + run.yaml) · Valley OS page updated · Drive week folder populated with covers, captions, day plan, saved replies.

## Ratchet log
- none yet
