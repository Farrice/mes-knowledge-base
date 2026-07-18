# Phases 0-2 — Signal Capture, ICP, Voice Document

**Duration**: the bulk of the 1-2 hour target (vs. 1-2 weeks bespoke per vertical, per SKILL.md's "Why this skill exists"). Required before Phase 2.5 can fire.

## Required inputs

- A domain name or short description from the user (e.g., "AI-for-construction consulting," "real estate SFV").
- Optionally: 1-3 `--reference-creator` URLs for later ground-truth extraction.
- Optionally: `--icp-sketch <path>` (skips Phase 1's first half) or `--voice-samples <path>` (speeds Phase 2).

## Steps

### Phase 0 — Signal capture & slug validation

1. Slugify the name (lowercase, hyphens; reject reserved names) and check it isn't already registered:
   ```bash
   python3 execution/ground_truth.py domains | grep -i "<slug>"
   ```
   `execution/ground_truth.py:init_domain` validates the same pattern mechanically (`^[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$`) and raises `ValueError` if the slug is already registered — if the manual check misses a collision, the Phase 4 registration call will hard-fail on it.
2. Capture target-audience snapshot (1 paragraph), 3-5 known pain points, and a 1-paragraph picture of customer success.
3. Write the capture to `projects/<slug>/_working/phase-0-capture.md`.

### Phase 1 — ICP construction

Invoke `/icp-deep-dive` (or `/mcraney-deep-canvass` for low-data verticals) against the Phase 0 capture. Output: `projects/<slug>/00-foundation/02-icp-master.md`, containing identity-level resistance, the articulation gap, audience-state mapping, and a language map (use/avoid). Stop condition: if the ICP draft scores below 7 on Expert Standard via the eval_harness anchor lookup, re-run Phase 1 with a sharper Phase 0 capture before proceeding — do not carry a sub-7 ICP into Phase 2.

### Phase 2 — Voice document

Invoke `/voice-document` with the Phase 0 capture, any `--voice-samples`, and the Phase 1 ICP (voice is partly a function of audience). Output: `projects/<slug>/00-foundation/03-voice-document.md`, containing a one-sentence voice test, tone calibration anchors, vertical-specific banned patterns, and 3-5 worked examples.

## Output Schema

Two artifacts hand off to Phase 2.5, plus one working file that never leaves the project folder:

- **`projects/<slug>/_working/phase-0-capture.md`** — audience snapshot + 3-5 pain points + success picture. Internal scaffolding; not read by the founder.
- **`projects/<slug>/00-foundation/02-icp-master.md`** — must name the identity-level resistance and the language map explicitly, not just demographic facts. A profile with no "avoid" words listed hasn't done the McRaney-grade pass the phase calls for.
- **`projects/<slug>/00-foundation/03-voice-document.md`** — must include a one-sentence voice test that resolves yes/no on a candidate line, plus 3-5 worked examples specific to this vertical (not generic tone adjectives).

## Quality Gate

Before Phase 2.5 can fire:
- [ ] Phase 0 capture exists with all three required elements (audience snapshot, pain points, success picture)
- [ ] ICP master scored ≥7 on Expert Standard via eval_harness anchor lookup (re-run Phase 1 if below)
- [ ] Voice document's one-sentence voice test actually resolves yes/no on a sample line — not a vague tone description
- [ ] Both `02-icp-master.md` and `03-voice-document.md` are registered via `anchor_memory.py anchor <slug> --type icp|voice --ref-for finalize`

If any item is unchecked, do not advance to Phase 2.5 — the gate is meant to review a complete pair, not a partial one.
