# Design Gauntlet

> A reference-anchored, screenshot-first repair loop for taste-bearing design. It combines Jack Roberts' codify-and-iterate method with the local Blind Bar, Design Library, and Asset Command Center. It is not a critic swarm and it never hides weak evidence behind a score.

## Deploy When

Use this workflow when all three are present:

1. a renderable visual draft or stable preview;
2. a named primary reference, approved style recipe, or prior winning artifact;
3. permission to modify the artifact locally.

If the draft is missing, return to the relevant build workflow. If the bar is missing, run `reference-collection-sprint.md` or search `knowledge/design-libraries/INDEX.md`. If the artifact cannot be rendered, run a deterministic structure review and mark visual judgment `UNVERIFIED`; do not manufacture a Gauntlet pass.

## Preservation Lock

Before editing, record the artifact path or URL and a recoverable baseline; the primary reference and why it is the bar; brand/project DESIGN.md, tokens, fonts, and required components; intended audience, action, format, and hierarchy; explicit anti-targets; and the best prior iteration. Never overwrite the current best version without a recoverable copy or version-control diff.

## Choose One Mutation Mode

| Mode | Allowed change | Preservation boundary |
|---|---|---|
| **Precision Polish** | CSS, spacing, type, alignment, states, responsive repair | Structure, content, and brand tokens stay fixed unless broken |
| **Theme-Respect Elevate** | Token refinement, layout hierarchy, components, imagery treatment | Brand recognition and content intent stay fixed |
| **Creative Unleash** | Bold composition and art-direction changes | Required content, audience job, accessibility, and explicit anti-targets stay fixed |

Name the mode before editing. A DESIGN.md is source truth in Precision Polish; in the other modes it is an inherited premise that may be deliberately evolved. Any change to it must be called out, not silently smuggled in as polish.

## Phase 1 — Context Fingerprint

```markdown
Artifact: [path/URL]
Mode: [Precision Polish | Theme-Respect Elevate | Creative Unleash]
Primary bar: [reference path/URL + selected traits]
Supporting references: [0-3]
System source: [DESIGN.md / tokens / brand files]
Audience action: [what the design must make easier or more desirable]
Preserve: [locked elements]
Never do: [anti-targets]
Prior assets/styles checked: [query + result or N/A]
```

Search existing material before generating more:

```bash
python3 execution/design_md_brand_lookup.py search "[aesthetic or brand query]"
python3 execution/asset_gallery.py
```

Use the gallery's prompt, style, project, and tag search when an interactive view is available. Reuse a prior asset or style recipe only when its provenance and rights fit the current work.

## Phase 2 — Reality Before Taste

Run the artifact's existing build, lint, type, or validation commands first. Inspect broken assets and font failures; overflow, clipping, contrast, and keyboard traps; rogue tokens; responsive failures at 1440×900, 768×1024, and 375×667; and required content or states missing from the render. A critical functional or accessibility failure caps the result at `FAIL` until closed. “Addressed” is not “closed”: re-run the failed check.

## Phase 3 — Screenshot Baseline

Capture the current artifact at desktop, tablet, and mobile. When practical, also capture semantic landmarks (hero, proof, main interaction, CTA) and meaningful states (default, hover/focus, error, empty, loading).

Preferred evidence order:

1. live browser screenshots plus accessibility snapshot;
2. local headless-browser screenshots;
3. user-supplied screenshots;
4. source-only inspection, explicitly marked `VISUAL UNVERIFIED`.

Preserve screenshots under the task's existing evidence or proof directory. Do not start the taste pass until the baseline is visible.

## Phase 4 — Reference-Anchored Blind Bar

Apply `directives/blind-bar-protocol.md`. Compare the draft and primary bar side by side. If filenames, history, or authorship would bias the judgment, use neutral labels A/B. Evaluate only traits the reference actually demonstrates: composition and eye path; typography hierarchy and rhythm; color, contrast, and material treatment; visual identity and specificity; responsive behavior and interaction polish.

When the largest visible gap is compositional, run `/satori-composition-brief` as a bounded diagnosis of leverage, internal rhythm/eye path, grid commitment, movement, friction, and transfer. The primary reference remains the taste bar and Jack Roberts remains the repair owner; the Satori packet explains the composition change to make, not a new aesthetic to impose. For exact-pixel or non-layout repairs, record `Composition: SKIPPED — [reason]` and continue.

For every finding, record the visible evidence and viewport/state. Critical findings are explicit: broken hierarchy, illegible text, brand violation, missing content, interaction failure, or a dominant AI-default pattern that contradicts the reference.

Commit to one verdict before proposing edits:

```markdown
Verdict: [A | B | TIE | INCOMPARABLE]
Single biggest visible gap: [one specific gap]
Evidence: [viewport/state + observable difference]
Preserve from current best: [what must not regress]
```

No universal taste score can replace this verdict. A numerical score may summarize already-recorded evidence, but it cannot create evidence.

## Phase 5 — Bounded Repair

Repair the single biggest visible gap or one tightly related batch. Then re-run affected deterministic checks, re-render the same viewports and states, compare against both the primary bar and prior best, keep the new candidate only if the visible delta is positive with no preservation regression, and log the change, evidence, and remaining risk.

Default maximum: **two repair rounds**. Stop earlier on PASS, plateau, oscillation, or regression. If Round 2 does not clearly beat the prior best, restore the best version and report the surviving gap. More than two rounds, or worker/critic fleets, require Farrice's explicit approval under the full-gauntlet boundary.

## Phase 6 — Truth And Preference Gates

- Claims, statistics, dates, and named facts follow the workspace factual-veto path. Use deterministic or source-grounded verification; real subagents are optional and approval-gated, never mandatory.
- Human preference remains the final lock for high-taste work. Codex may produce the evidence and a verdict; it must not convert inferred taste into permanent doctrine without approval.
- Only after the winner is preference-locked may the system enshrine a new or revised DESIGN.md/style recipe and register reusable assets in the existing Asset Command Center.

## Output Contract

Deliver the best artifact version with recovery path; before/after screenshots at tested viewports or `VISUAL UNVERIFIED`; deterministic check results; Blind Bar verdict and single biggest gap per round; change log and re-verification; surviving risks and human preference checkpoint; and status `PASS`, `PARTIAL`, or `FAIL`.

## Output Skeleton

```markdown
# Design Gauntlet Result — [artifact]
Mode: [mode]
Primary bar: [reference]
Status: [PASS | PARTIAL | FAIL]

## Preservation Lock
[locked elements + recoverable baseline]
## Reality Checks
- [check]: [PASS/FAIL + evidence]
## Baseline Evidence
- Desktop: [path/status]
- Tablet: [path/status]
- Mobile: [path/status]
## Repair Round [1-2]
- Blind verdict: [candidate/bar/tie/incomparable]
- Single biggest gap: [gap]
- Change: [narrow repair]
- Re-verification: [evidence]
- Delta: [improved/plateau/regressed]
## Best Version
[artifact + why it survived]
## Surviving Risks
- [risk or NONE]
## Human Checkpoint
[preference decision needed or N/A]
## Reuse Hook
[existing recipe/design system/asset registration updated, queued, or N/A]
```

## Quality Gate

- A named primary bar and baseline exist before edits.
- One mutation mode and preservation boundary are explicit.
- Functional/accessibility failures are re-verified, not merely described as fixed.
- Every taste finding points to visible evidence at a viewport/state.
- Each repair attacks one biggest gap or one coherent batch.
- The new candidate is compared with the prior best; regression restores the prior best.
- The loop stops at two repair rounds unless Farrice explicitly approves a full gauntlet.
- The result exposes surviving risk and preference uncertainty; it never declares victory from a bare score.

## Source And Integration Notes

This workflow harvests bounded, evidence-first mechanics from Jack Roberts' August 2026 design-system video, `haneystrategy/gauntlet` (CC BY 4.0, inspected at commit `851071b7f2ced48b8a1347d70deaccc7bbb4798a`), and `tonymfer/design-loop` (MIT, inspected at commit `1d740bc429d58f23d613e875b3ad4f42c5b447cc`). It deliberately reuses local infrastructure instead of importing either external system wholesale.
