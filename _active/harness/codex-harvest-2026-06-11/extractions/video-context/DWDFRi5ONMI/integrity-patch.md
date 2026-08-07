# Oren Solo AI Marketing Machine Source Integrity Patch

## Patch Verdict

This video source package is safe to use as trusted Tier A capability evidence
when the source package verifier, cold-start firing probe, active proof bundle,
and this package-local integrity patch are all present.

## Source Boundary

- Source package: `extractions/video-context/DWDFRi5ONMI/`
- Source mode: transcript-backed with sampled frames.
- Clean source state: `transcript.txt` and `transcript_segments.json` were
  regenerated from preserved VTT files.
- Current verifier counts: 860 transcript segments, 6051 clean transcript
  words, and 1718 observed spoken ledger rows.
- Visual boundary: 10 sampled frames exist, but OCR is unavailable.
- Uncertainty: exact whiteboard, screen, or onscreen-text claims remain blocked
  unless a frame was inspected directly or future OCR/vision evidence is added.

## Build Shape Decision

- Build shape decision: companion workflow inside the existing Oren archetype
  social strategy skill.
- Existing owner: `/oren-solo-ai-marketing-machine`.
- Duplicate route check: use
  `skills/oren-archetype-social-strategy/workflows/oren-solo-ai-marketing-machine.md`
  and the active client/service-business bundle
  `_active/oren-solo-ai-marketing-client-service-os/`.
- Rejected duplicate surfaces: do not create another hot Oren expert, another
  one-person marketer skill, or a replacement marketing planner.
- Companion fit: the source enriches the existing Oren stack with constrained
  solo operator execution, AI copy machine, referral gate, message loop,
  funnel/email/collateral, creator, organic, and remarketing cadence.

## Practitioner First-Run Path

Inputs:

- Offer or business model.
- Primary 30-90 day sales goal.
- Current channels and rough performance.
- Customer, referral, and proof asset status.
- Existing sales, landing page, email, CRM, ad, creator, or analytics surfaces.
- Available weekly marketing hours.
- Budget and AI/tool access.

Step order:

1. Set the solo operator constraint.
2. Run the referral and word-of-mouth gate.
3. Build the monthly message intelligence board.
4. Set up the AI brand-voice and copy machine.
5. Build the weekly solo marketing calendar.
6. Connect the remarketing and reuse loop.
7. Produce the first 7-day sprint.
8. Write the do-not-do list and scale trigger.

Outputs:

- Solo operator constraint.
- Referral and word-of-mouth gate.
- Monthly message board.
- AI brand-voice and copy machine setup.
- Weekly marketing calendar.
- Creative, performance, funnel, email, creator, and organic lane plan.
- Remarketing and reuse loop.
- First 7-day sprint.
- Do-not-do list.
- Scale trigger.

Quality gate:

- The workflow fails if it only gives marketing ideas.
- It passes when the operator can open a calendar, AI project, creator tracker,
  landing page backlog, email plan, and ad/account learning log and know what
  to do next.

Failure modes:

- If the user has under 20 weekly hours, preserve order and compress capacity.
- Do not add new channels before referral, message, creative, funnel/email, and
  current conversion paths are graded.
- Do not claim OCR-backed visual evidence from this source.

## Cold-Start Firing Proof

Natural-language probe:

`one person marketing machine`

Observed route result after repair:

| Surface | First route |
|---|---|
| command menu | `oren-solo-ai-marketing-machine` |
| workflow router | `oren-solo-ai-marketing-machine` |
| routing governor | `oren-solo-ai-marketing-machine` |

## Behavior Proof

Applied scenario proof bundle:

- Cold-start fixture:
  `_active/oren-solo-ai-marketing-client-service-os/02-research/cold-start-fixture.md`
- Behavior proof sample run:
  `_active/oren-solo-ai-marketing-client-service-os/02-research/behavior-proof-sample-run.md`
- Behavior proof ledger:
  `_active/oren-solo-ai-marketing-client-service-os/02-research/behavior-proof-ledger.md`

Before:

- A generic service-business plan would say ask for referrals, improve the
  website, post on LinkedIn, build case studies, and start email follow-up.

After:

- The workflow produces an exact referral ask, proof-backed message board, AI
  copy context with review gate, 25-hour calendar, first 7-day sprint,
  client-facing handoff, and implementation upsell path.

Behavior delta:

- The output changes from broad marketing advice into ordered assets,
  constraints, and operating decisions that a solo operator can execute.

## Validation Coverage

Verifier coverage:

```bash
python3 execution/verify_video_context_source_package.py extractions/video-context/DWDFRi5ONMI
python3 execution/verify_behavior_changing_extraction_contract.py
python3 execution/verify_skill_system_contract.py
python3 execution/command_menu.py search "one person marketing machine"
python3 execution/workflow_router.py search "one person marketing machine"
python3 execution/audit_extraction_integrity.py --since 2026-05-01 --until 2026-06-11 --out _active/extraction-engine-drift-audit/04-deliverables/may-june-extraction-integrity-ledger.json
```
