---
name: run-folder-is-the-state
problem_signature: "a door's receipts are printed to chat and lost; the page the operator judges is regenerated from hand-edited tables; a second harness (Codex) cannot reproduce the run because the state lives in Claude-only tools"
domain: harness
tags: [jen, receipts, run-manifest, codex-parity, scrapes-import, valley-os]
date: 2026-09-09
status: active
session: dazzling-elgamal-72830b (IMPORT-LIST.md #1)
---

## Problem
`/jen` printed nine receipt lines into chat; nothing persisted them. The Valley OS page was rebuilt from four Python tables in `jen_os_page.py` that duplicated the post data already in `build_weeks.py`. Farrice: "I'm not fully able to track everything… make sure it works on both services." The Scrapes pipelines keep `post.yaml` + `pipeline-log.md` inside `{date}/{slug}/` and every reader reads the folder.

## Approach That Worked
1. **One stdlib script, three verbs.** `execution/run_log.py receipt|manifest|check`. `receipt` appends `- <stamp> · STEP: text` (+ `Reasoning:`) to `<run>/pipeline-log.md`; `manifest` merges `run.yaml` atomically; `check` fails when a receipt is missing or out of order or a required key is absent. Works under `/usr/bin/python3` without PyYAML (own subset reader, cross-checked against PyYAML in tests).
2. **The renderer writes the manifest from its own data.** `build_weeks.py` emits `run.yaml` per week from the `WEEKS` list it rendered (posts, hooks, captions, photos with an honest `(hers)` flag, routing) and a `<id>-cover.png` still per reel so the page shows reels without the mp4s that live only in Drive. Status and receipts are the door's and survive re-renders (merge, never overwrite).
3. **The page reads the folder.** `jen_os_page.py` globs `week-of-*/run.yaml`, shows each week's receipts and the gate verdict, and reads her asset inventory from a living `VALLEY-OS-ASSETS.yaml`. No per-run data is typed into it (a test greps the source for the old table names).
4. **The door writes receipts as shell commands**, so Codex runs the same lines. The only Claude-only action (Artifact publish) is marked with its Codex fallback (leave the HTML path in the receipt, next Claude session republishes).
5. **Prove it on a real week.** Week 2 re-ran through all nine steps; the rules that fire on every run changed the copy (her close 3/3 → 1, "my DMs are open" 3/3 → 1, two number-first hooks re-opened on the reader); stamp-lint went FAIL → PASS; `run_log.py check` PASS; page republished to the same URL with zero table edits.

## Dead Ends
- PyYAML reads a bare `2026-09-09` as a date and a `|` block keeps its trailing newline: quote date-like strings, emit `|-`.
- `HERE.parents[3]` for the repo root breaks in a lane; walk up until `execution/run_log.py` exists.
- `html.count("gate pass")` matched the lede sentence "whether the run gate passes"; count the tag boundary `>gate pass<`.
- The classifier reads the operator's `COPY.md` (beats and slides as a bulleted list) as parallel structure (8/10) while `captions.txt` is CLEAN (1.5/10): run it on what posts.

## Verification
`uv run --with pytest --with pyyaml python -m pytest tests/test_run_log.py tests/test_jen_os_page.py tests/test_scrapes_routing.py` → 40 passed. `/usr/bin/python3 execution/run_log.py check <week>` → PASS. Page built under both interpreters is identical once the same receipts are on disk.

## Weaker-Model Trap
A mid-tier model "saves time" by writing the receipts at the end of the run in one go, or types a post into the page because "the manifest is missing a field." Tell it: a receipt is written when its step ends; a missing field is fixed in `build_weeks.py` (the renderer), never in the page.

## Pointers
`execution/run_log.py` · `.agent/workflows/jen.md` · `execution/jen_os_page.py` · `_active/clients/jen-listings/06-system/VALLEY-OS-ASSETS.yaml` · `_active/clients/jen-listings/04-deliverables/2026-09-06-engine-v2-weeks-1-2/week-of-2026-09-14/{run.yaml,pipeline-log.md,READ.md,AMPLIFY.md}` · `_active/harness/scrapes-skill-systems/IMPORT-LIST.md` #1
