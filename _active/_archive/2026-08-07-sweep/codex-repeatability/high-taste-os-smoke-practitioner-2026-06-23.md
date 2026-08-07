# High-Taste OS Smoke Test: Practitioner Strategy Artifact

Date: 2026-06-23
Command: `/high-taste-os --practitioner`

## Raw Intent

Create a client-facing strategy artifact for a wellness brand that knows buyers
are asking AI tools for recommendations but has no proof the brand is being
named, compared, or trusted.

## Context Load Packet

| Field | Loaded Value |
| --- | --- |
| Mode | Practitioner smoke test |
| Owner route | `/high-taste-writing-os` |
| Route proof | V4, high-taste, remarkable-output language maps to the High-Taste OS route instead of generic taste routes. |
| Required files loaded | `.agent/workflows/high-taste-writing-os.md`, `.agents/skills/source-command-high-taste-writing-os/SKILL.md`, `_active/_archive/2026-08-07-sweep/codex-repeatability/v4-high-taste-output-os.md` |
| Support lanes | Retrieval logic, buyer trust, offer packaging, prose gate |
| Rejected routes | `taste-name`, `taste-stage`, broad expert panel |
| Verification plan | Route proof, content finish gate, prose classifier, grounding guard, finalize receipt |

## Reader Contract

This artifact is for a founder, CMO, or growth lead at a wellness, supplement,
fitness, or performance brand. It should make one problem concrete:

Buyers can now ask an answer engine what to buy before they ever reach the
brand's site. If the brand is missing from those answers, or present without
trust signals, demand can leak before the funnel starts.

The output should leave the operator with a first sprint they can approve this
week.

## Material Ledger

| Material | Status | Use |
| --- | --- | --- |
| Raw operator intent | Present | Defines the client-facing strategy request. |
| V4 quality bar | Present | Requires source spine, human stakes, one composer, and receipt. |
| External web research | Not used | This smoke test avoids outside claims. |
| Client site and category | Missing | Needed before a real audit. |
| Competitor set | Missing | Needed before a real benchmark. |

## Human Wound And Stakes

The brand thinks this is an SEO problem.

The more uncomfortable version is simpler: a buyer may already be asking an AI
tool which product to trust, and the brand may not even be in the room.

That creates a quiet loss. There is no rejected cart or failed checkout for the
team to inspect. Analytics may look calm while a buyer who was ready to compare
options never sees a reason to consider you.

## Practitioner Artifact

### AI Visibility And Trust Layer Sprint

The first move is not a new blog calendar.

The first move is to see what answer engines already believe about the category.

Run the brand through three layers:

1. **Prompt Reality**
   Test the prompts a serious buyer would ask before purchase:
   - "best [category] for [specific use case]"
   - "[ingredient/product] vs [alternative]"
   - "is [brand] worth it"
   - "what should I look for in [category]"
   - "which [category] brands are trusted by [audience]"

2. **Answer Position**
   Capture whether the brand is named, ignored, misdescribed, or mentioned
   without a reason to trust it.

3. **Trust Layer**
   Check the proof a skeptical buyer can see after the answer:
   named humans, product mechanisms, claims boundaries, ingredient logic,
   third-party proof, founder accountability, and comparison clarity.

The sprint output is a working map:

| Gap | What It Means | First Fix |
| --- | --- | --- |
| Not cited | The brand is absent from category memory. | Build source-worthy category assets. |
| Cited weakly | The brand is known but not trusted. | Add proof pages and named mechanisms. |
| Misdescribed | The market has the wrong mental model. | Publish correction assets and comparison pages. |
| Trusted off-site only | Borrowed authority is doing the work. | Bring proof back onto owned surfaces. |

This turns "AI SEO" from a buzzword into an operator decision:

Where are we invisible?
Where are we untrusted?
Where are we misunderstood?
What proof would make the next answer safer to cite?

## Claim/Proof Ledger

| Claim | Status | Proof |
| --- | --- | --- |
| Buyers may ask answer engines before visiting a brand site. | LIKELY | Operating hypothesis for the smoke test; verify with live prompt research before client use. |
| Absence or weak citation can create demand leakage. | LIKELY | Strategic inference; validate with prompt captures and referral data. |
| The proposed sprint can be run without client case studies. | VERIFIED | It depends on public prompt testing, owned-site review, and observable proof gaps. |

## Taste Evidence Ledger

| Before Pattern Avoided | Replacement |
| --- | --- |
| Generic "AI SEO is the future" framing | A buyer scene where the brand is missing from the comparison. |
| Expert soup | One operator spine with bounded support lanes. |
| Consultant-clean abstraction | Specific audit moves, prompt types, and fix paths. |
| Unproven authority claim | Public diagnostic method that proves judgment through the work. |

## Orchestration Receipt

| Field | Result |
| --- | --- |
| Intent score | 4/5 |
| Owner workflow | `/high-taste-writing-os` |
| Route proof | Router and Codex preflight select high-taste over generic taste routes. |
| Files loaded | Canonical workflow, source-command wrapper, V4 repeatability packet. |
| Extracted patterns | Source spine, human stakes, one composer, ledgers, receipt. |
| Support lanes | Retrieval, trust, offer packaging, prose gate. |
| Rejected routes | `taste-name`, `taste-stage`, broad expert panel. |
| Verifier results | `verify_high_taste_os`: PASS; `grounding_guard`: PASS; `content_finish_gate`: WARN only; `prose_classifier`: WARNING due Markdown ledger/list repetition. |
| Finalize status | PASS. `chain_runner.py finalize` composite 8.0/10 with Notion logging skipped. Remote regression lookup was unavailable in the restricted local run and did not block the local quality gate. |
