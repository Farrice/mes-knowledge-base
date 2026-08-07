# Template Runbook

## Route

Primary invocation:

```text
/oren-solo-ai-marketing-machine [client/service business context]
```

Load this bundle when the target is a client or service business and the goal is a reusable operating template, diagnostic sprint, or client-facing handoff.

## Step Order

1. Confirm service-business fit.
2. Fill the intake in `04-deliverables/internal-operator-template.md`.
3. Use the referral gate before adding channels.
4. Build the message board from proof, objections, and buyer questions.
5. Set up the AI copy-machine brief.
6. Allocate the weekly calendar around available hours.
7. Produce the first 7-day sprint.
8. Convert the internal output into `04-deliverables/client-facing-operating-template.md` when client-facing handoff is needed.
9. Use `04-deliverables/48-72h-proof-sprint.md` when packaging the work as a paid diagnostic or implementation path.

## Service-Business Defaults

Prioritize:

1. referrals,
2. sales collateral,
3. email and follow-up,
4. proof assets,
5. landing page and message match,
6. LinkedIn or relevant organic validation,
7. paid and creator work only after the funnel can catch demand.

## Validation

Run:

```bash
python3 execution/command_menu.py search "client service business solo AI marketing"
python3 execution/workflow_router.py search "one person marketing operating template service business"
python3 execution/context_retriever.py search "Oren solo AI marketing client service template" --top 5
python3 execution/artifact_frontmatter_guard.py _active/oren-solo-ai-marketing-client-service-os/04-deliverables/*.md
python3 execution/artifact_surface_guard.py _active/oren-solo-ai-marketing-client-service-os/04-deliverables/*.md
python3 execution/export_format_guard.py _active/oren-solo-ai-marketing-client-service-os/04-deliverables/*.md
python3 execution/artifact_router.py enforce _active/oren-solo-ai-marketing-client-service-os/04-deliverables/client-facing-operating-template.md
```

After workflow reference changes, also run:

```bash
python3 execution/generate_codex_indexes.py
python3 execution/context_retriever.py index
python3 execution/verify_codex_indexes.py
python3 execution/codex_harness_check.py
```

## Behavior Proof

Use `02-research/cold-start-fixture.md`. A passing run should produce:

- referral outreach packet,
- proof-backed landing page or PDF improvement,
- first follow-up/email sequence or sales collateral asset,
- client-facing operating handoff,
- deferred paid/creator work until the funnel can catch demand.
