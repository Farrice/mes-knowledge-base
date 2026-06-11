# Kishotenketsu Contrast Storytelling Integrity Patch

## Patch Verdict

This package is safe to use as a trusted Tier A capability when source package
verification, cold-start firing, the proof lab, and this package-local
integrity patch are all present.

## Source Boundary

- Source package: `extractions/video-context/0eIN-Zdt39Q/`
- Source mode: transcript-backed.
- Clean source state: `transcript.txt` and `transcript_segments.json` were
  regenerated from preserved VTT files.
- Current verifier counts: 445 transcript segments, 2706 clean transcript
  words, and 888 observed spoken ledger rows.
- Uncertainty: frame extraction was skipped and OCR is unavailable for this
  package.
- Source boundary: no visual claim, cultural claim, or exact scene claim should
  be treated as observed unless it appears in the transcript ledger or a future
  captured visual/OCR evidence row.

## Build Shape Decision

- Build shape decision: companion workflow and semantic primitive inside the
  existing Lucas Alpay storytelling system.
- Existing owner: `/kishotenketsu-contrast-storytelling`.
- Duplicate route check: use the existing workflow
  `skills/lucas-alpay-storytelling/workflows/kishotenketsu-contrast-story-system.md`
  and primitive
  `semantic_libraries/antigravity/primitives/kishotenketsu-contrast-storytelling-contract.md`.
- Rejected duplicate surfaces: do not create a separate hot skill, generic story
  expert, or replacement copywriting route for this mechanic.
- Companion fit: use as a contrast/story engine that can stack with proof,
  voice, conversion, positioning, or publishable-copy gates when those are the
  real blockers.

## Practitioner First-Run Path

Inputs:

- Draft, idea, scene, post, page, ad, campaign, media script, messaging note,
  positioning note, product/service/concept brief, or ghostwriting source.
- Audience or reader.
- Desired action, feeling, or interpretation.
- Proof assets or voice source when the output is revenue-facing, public, or
  ghostwritten.

Step order:

1. Diagnose the current engine: conflict, contrast, proof, clarity, or voice.
2. Build the Ki world.
3. Turn Sho into process-as-plot.
4. Introduce the Ten shift as a variable, point of view, memory, time jump, or
   recontextualizing information.
5. Integrate with Ketsu.
6. Apply the next gate: proof, voice, conversion, audience, platform,
   positioning, or publishable-copy review.

Outputs:

- Engine diagnosis.
- Ki world.
- Sho process.
- Ten shift.
- Ketsu integration.
- Rewritten output.
- Behavior delta.
- Deployment surface.
- Next gate and remaining risk.

Quality gate:

- Pass only when the rewrite visibly improves reader movement: inhabit, deepen,
  reframe, integrate.
- Fail if section labels replace a felt turn, if removing a villain removes all
  stakes, if texture is decorative, or if revenue copy loses proof and CTA.

Failure modes:

- If proof or offer clarity is the blocker, route to the proof or copy gate
  before rewriting.
- If voice fidelity is the blocker, load voice source before changing prose.
- If source/cultural claims exceed transcript evidence, mark them as inference.

## Cold-Start Firing Proof

Natural-language probe:

`kishotenketsu contrast storytelling variable over villain`

Observed route result after repair:

| Surface | First route |
|---|---|
| command menu | `kishotenketsu-contrast-storytelling` |
| workflow router | `kishotenketsu-contrast-storytelling` |
| routing governor | `kishotenketsu-contrast-storytelling` |

## Behavior Proof

Before/after proof lab:

- Model proof surface:
  `_active/kishotenketsu-storytelling-os/07-before-after-proof-lab.md`
- Proof scenarios: fiction scene, LinkedIn/social, brand page, ghostwriting,
  sales/copy, ads/media, and messaging/positioning/concept.
- Behavior delta: outputs shift from forced conflict, generic advice, and
  abstract promise into texture, contrast, process-as-plot, perspective shift,
  and integration.

Required proof dimensions:

1. More specific texture.
2. Stronger contrast.
3. Clear process-as-plot.
4. Meaningful perspective shift.
5. Integration that changes interpretation or action.

## Validation Coverage

Verifier coverage:

```bash
python3 execution/verify_video_context_source_package.py extractions/video-context/0eIN-Zdt39Q
python3 execution/verify_behavior_changing_extraction_contract.py
python3 execution/verify_skill_system_contract.py
python3 execution/command_menu.py search "kishotenketsu contrast storytelling variable over villain"
python3 execution/workflow_router.py search "kishotenketsu contrast storytelling variable over villain"
python3 execution/audit_extraction_integrity.py --since 2026-05-01 --until 2026-06-11 --out _active/extraction-engine-drift-audit/04-deliverables/may-june-extraction-integrity-ledger.json
```
