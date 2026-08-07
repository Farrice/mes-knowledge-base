# Behavior Proof — KDP Book One Cold Start

## Input tested

> I have no audience, no ad budget, and no book idea. Help me create a useful nonfiction ebook under a market-first pen name, make it good enough that a reader would recommend it, and prepare it for Amazon KDP without publishing anything until I approve.

## Weakness diagnosed

The previous operating path could treat a rank heuristic as demand proof, move directly into a fast AI draft, imply that editing alone settled copyright eligibility, reduce the ebook upload decision to PDF export, and use review tactics that could cross Amazon's review-integrity boundary. It also had no durable separation between production progress, local capability proof, marketplace events, and upload permission.

## Source mechanics used

- Sean Dollwet's demand-first sequence: choose one buyer problem, validate before drafting, build a controlled outline, produce section by section, package deliberately, and launch organically before scaling.
- The 11-video corpus delta: a rolling context packet, claim/source ledger, five anti-slop gates, preview and upload-format checks, cover geometry, metadata checks, and dated marketplace observations.
- Current official boundaries: disclose AI-generated text, images, or translations to KDP; retain rights evidence; avoid manipulated or compensated reviews; treat KDP Select, pricing, formats, and metadata as separate decisions; do not claim copyright eligibility from a generic “humanizing” pass.
- Evidence discipline: a dated rank or review observation is a signal, not a revenue calculation; production, capability, market, and permission advance on independent ledgers.

## Output produced

- Function owner: `.agent/workflows/kdp-engine.md`
- Conductor: `skills/sean-dollwet-kdp-publishing/workflows/00-book-one-pilot.md`
- Operator cockpit prompt: `skills/sean-dollwet-kdp-publishing/references/prompts-v2/book-one-pilot-cockpit.md`
- Persistent state machine: `execution/kdp_book_one.py`
- Policy boundary: `skills/sean-dollwet-kdp-publishing/references/kdp-policy-and-evidence-boundary.md`
- Deterministic verifier: `execution/verify_kdp_book_one_system.py`

## Behavior delta

| Before | After |
|---|---|
| Generate topics, infer demand, begin drafting | Initialize a persistent dossier, run the operator interview, and collect 5–10 dated candidates before approving one niche |
| Treat BSR or competitor reviews as a sales estimate | Record rank, format, price, review, and listing observations separately; leave revenue `UNCONFIRMED` without a defensible model |
| Ask AI for a whole book and polish it afterward | Lock reader, problem, promise, source dossier, outline, and one gold-standard chapter before staged drafting |
| Use a vague “humanize” step | Require claim support, originality, redundancy, reader-value, design, disclosure, rights, and preview gates |
| Prepare to publish once files exist | Return `HOLD`, `BLOCKED`, `READY_FOR_APPROVAL`, or `READY_TO_SUBMIT`; upload permission is an explicit, evidence-backed checkpoint |
| Let production progress imply success | Keep marketplace proof at `NO_EVENT` until discovery, sale, and net collection are observed |

## Validation run

- `python3 execution/skill_auditor.py check --skill sean-dollwet-kdp-publishing`
- `python3 execution/verify_kdp_book_one_system.py --write-receipt`
- `python3 execution/renaissance_audit.py`
- Natural-language cold queries through `execution/command_menu.py` and `execution/workflow_router.py`
- Detached fresh-context probe recorded in `detached-runtime-receipt.json`

Structural verification passes. The machine receipt is `cold-start-receipt.json`, and the fresh-context receipt is `detached-runtime-receipt.json`. The detached probe promotes only local behavior capability to `RUNTIME_OBSERVED`; it does not promote marketplace proof.

## Remaining risk

- No niche has yet passed the live market dossier.
- No manuscript, cover, preview, or KDP upload package exists for Book One.
- No KDP account action or upload has been authorized.
- No buyer has discovered or purchased the book; market state is `NO_EVENT`.
- No royalty has been paid or collected; the income thesis remains `UNTESTED`.
- Current KDP policy and marketplace conditions can change and must be rechecked at the upload gate.
