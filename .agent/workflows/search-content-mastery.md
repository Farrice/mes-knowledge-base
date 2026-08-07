---
description: "One evidence-bounded SEO, AEO, GEO, search-everywhere and content-evaluation front door for project foundation, site/content audit, keyword and opportunity planning, content/media creation handoff, scoring, import-first measurement, and service delivery."
---

# /search-content-mastery — Search Content Mastery OS

## Invocation

```bash
/search-content-mastery [foundation|audit|plan|create|score|measure|service] [project/context]
```

Use this command first when a natural-language request combines search/SEO/AEO/GEO with establishing a project, auditing, planning, creating, rating/scoring, measuring, experimenting, or delivering a service.

Do not route these requests to `/health-check`; that command owns read-only harness status.

## Objective

Run source-grounded search work from project truth through a measurable handoff while preserving:

- creator/source evidence versus system inference;
- deterministic checks versus expert judgment;
- Farrice's override versus the original score;
- predicted readiness versus independent observed outcomes;
- local capability proof versus market proof.

## Pre-Flight

Read:

1. `skills/search-content-mastery-os/SKILL.md`
2. `skills/search-content-mastery-os/genius.md`
3. `skills/search-content-mastery-os/references/skill-system-contract.md`
4. `skills/search-content-mastery-os/references/data-contract.md`
5. The exact mode workflow only
6. The exact project manifest and current record

Then load only the needed component:

- Nathan Gotch for traditional, on-page, audit, keyword, category, local, ecommerce, authority, or cross-platform mechanics.
- Ethan Smith for information gain, answer-engine questions, citation tests, control groups, or multi-surface AEO/GEO experiments.
- `/create` and its selected producer only after a SearchBrief is approved.
- Voice Card before anything published in Farrice's voice.
- Matching media craft master before generator prompts; paid generation remains cost-gated.

## Mode Router

| Mode | Owner workflow | Required input | Stops at |
|---|---|---|---|
| `foundation` | `workflows/01-foundation.md` | Project name, vertical, known context | Valid portable project pack |
| `audit` | `workflows/02-audit-plan.md` | Manifest and source/import evidence | Baseline receipt and opportunity decision |
| `plan` | `workflows/02-audit-plan.md` | Selected opportunity | Versioned SearchBrief |
| `create` | `workflows/03-create-score.md` | Approved SearchBrief | Local producer handoff/asset |
| `score` | `workflows/03-create-score.md` | Brief and local asset | ContentScoreReceipt |
| `measure` | `workflows/04-measure-service.md` | Local export/manual observation | Import receipt, optional SearchEvent/proposal |
| `service` | `workflows/04-measure-service.md` | Nine-artifact map | ServiceReceipt for internal review |

## Runtime

```bash
python3 execution/search_content_mastery.py <mode> --project <path> [...]
```

The runtime uses local files only. `batch --file <jobs.json>` supports ordered local batches. V1 has no live API, scheduler, publisher, outreach, deployment, payment, or autonomous mutation.

## Composition Rule

**Owner:** Search Content Mastery OS.  
**Mechanism:** Nathan Gotch, one exact lane at a time.  
**Differentiator:** Ethan Smith only where AEO/GEO experiment mechanics change the decision.  
**Craft:** one channel-native producer.  
**Risk gate:** source ledger, claim policy, strict schema/runtime checks, and explicit proof state.

Skip any expert who cannot name the exact record or decision they change.

## Result Surface

Return:

1. Mode and selected route.
2. Input record and source evidence.
3. Output record/artifact path.
4. Validation result.
5. Original judgment, override if any, and independent outcome state.
6. Remaining proof gap.
7. Exact next local command or approval boundary.

## Stop Rules

Stop and request explicit approval before:

- publishing or external distribution;
- outreach or connector writes;
- paid generation or quota-heavy research;
- payment creation or public offer activation;
- promoting a learning proposal into a skill/workflow/router;
- replacing The Angle Map canon;
- destructive cleanup, push, or merge.

## Validation

```bash
python3 execution/verify_search_content_mastery.py
python3 execution/validate_skill.py search-content-mastery-os
python3 execution/validate_skill.py source-command-search-content-mastery
python3 execution/verify_skill_system_contract.py
python3 execution/workflow_router.py search "build a source-grounded SEO AEO GEO content system that can audit plan create score and measure"
```

Promote the capability to `RUNTIME_OBSERVED` only when the custom verifier, three cold starts, routing regression, prompt gate, command parity, and relevant harness checks pass. Market effects remain `UNTESTED`.

