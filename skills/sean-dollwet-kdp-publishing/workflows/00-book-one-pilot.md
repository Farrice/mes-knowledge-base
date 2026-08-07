---
name: book-one-pilot
description: Amazon KDP first-book and AI ebook without slop — start from scratch with a pen name, market research, world-class manuscript and cover, current policy, organic no-ads launch, upload-readiness, and honest proof.
produces: Persistent Book One cockpit, approved stage artifacts, compliance verdict, and separate production/market proof ledger
expert: Sean Dollwet
load_context: genius.md
---

# Book One Pilot — Zero to Upload-Ready Without Slop

## Pre-Flight Gate

Use this for a first book, a zero-to-KDP request, an AI ebook that must not read like AI, or a request to harmonize the 7-, 14-, and 30-day lanes. This workflow conducts existing components; it does not replace them.

Before execution, read:

- `extractions/sean-dollwet-kdp-book-one-system/skill-system-contract.md`
- `extractions/sean-dollwet-kdp-book-one-system/source-ledger.md`
- `references/kdp-policy-and-evidence-boundary.md`

Initialize or resume the cockpit with `python3 execution/kdp_book_one.py init --project _active/publishing/kdp-book-one-pilot --pace launch_14`. Never overwrite an existing pilot. Use `status` when it already exists.

Do not publish, open the KDP account, spend money, enroll in Select, contact readers, or create a client/factory layer without separate permission.

## Operating Doctrine

- Demand precedes drafting, but BSR is one dated marketplace signal—not a revenue oracle.
- The first book is one problem for one reader in a low-risk lane.
- AI may help research, organize, question, edit, and draft. Every asset still needs truthful AI classification, rights evidence, human judgment, and reader QA.
- A schedule can expand; a quality gate cannot shrink.
- Production proof, capability proof, market proof, and permission are recorded separately.

## Pace Profiles

| Profile | Intended use | Rule |
|---|---|---|
| `rapid_7` | A narrow, well-sourced book with unusually complete inputs | Day 7 is only an upload-readiness checkpoint. Any failed gate escalates to Day 14. |
| `launch_14` | Default first-book launch build | Daily checkpoints through research, gold chapter, manuscript, cover, and preflight. |
| `editorial_30` | Evidence-heavy, interview-heavy, or revision-heavy book | Remains open until every quality and policy gate passes. No forced ship date. |

## Execution

### 1. Deep operator interview

Capture only facts the system cannot research: lived experience, useful mistakes, reader empathy, stories, boundaries, desired anonymity, voice, and taste. Establish excluded lanes: medical treatment, legal advice, investing/tax advice, mental-health treatment, or other high-stakes claims unless a qualified reviewer owns accuracy.

Default identity is a market-first pen name. Do not invent credentials, biography, or lived experience.

### 2. Current 5–10-topic market scan

Run workflow 01 across 5–10 candidates. For every observation, record date, marketplace, format, query, title/ASIN, visible rank/reviews/price, source URL or screenshot path, and uncertainty. Add independent corroboration such as recurring reader questions, search language, or current community pain. AI-generated topic lists do not count as validation.

Checkpoint: Farrice approves one `GO`, chooses a `CONDITIONAL`, or sends the scan back. Record the decision; do not draft before approval.

### 3. Source dossier and blueprint

Run workflow 02. Abstract competitor coverage themes and complaint patterns; never copy wording, structure, examples, or distinctive sequencing. Build the claim ledger, source plan, interview/story inventory, title clearance notes, reader promise, outline, metadata draft, cover brief, and AI/rights plan.

Checkpoint: approve the outline and reader promise.

### 4. Gold chapter before full manuscript

Run workflow 03 on one representative chapter. Apply five separate gates:

1. Every factual claim is supported or removed.
2. The chapter adds real depth, not surface paraphrase.
3. Information and phrasing do not loop.
4. Voice sounds like a specific, competent human—not a textbook or model default.
5. The edit burden is acceptable for scaling across the manuscript.

Use interview-sourced stories, cases, examples, and analogies. Never fabricate a personal anecdote.

Checkpoint: approve, revise, or reject the gold chapter. The rest of the manuscript inherits this standard.

### 5. Full manuscript and reader QA

Draft in sections with a rolling context packet: promise, reader, outline, claims already made, open claims, terminology, examples used, and repetition watchlist. Complete developmental edit, claim check, structural-tempo pass, information-redundancy pass, line/copy edit, originality review, and beta/reader QA. Zero `[AUTHOR STORY]`, citation, or fact-check placeholders may remain at `QA_PASSED`.

### 6. Cover and listing package

Produce a locked cover brief, then concepts. Check thumbnail legibility, category fit, title hierarchy, distinctive-but-relevant positioning, wrap geometry, trim/page-count/spine, bleed/safe zones, resolution, fonts, stock licenses, AI disclosure, and metadata match.

Checkpoint: approve one cover and its rights receipt.

### 7. Compliance and upload-readiness

Prepare a reflowable DOCX/KPF/EPUB for the ebook, a separate print-ready PDF if print is in scope, and Kindle Previewer/link receipts. Run `python3 execution/kdp_book_one.py preflight --project _active/publishing/kdp-book-one-pilot --json`.

- `HOLD`: a remediable artifact or quality gap exists.
- `BLOCKED`: rights, policy, or excluded-risk failure exists.
- `READY_FOR_APPROVAL`: the package passes but upload permission is absent.
- `READY_TO_SUBMIT`: the package passes and explicit upload approval is recorded.

The workflow stops at `READY_FOR_APPROVAL` unless Farrice gives a separate upload instruction.

### 8. Organic launch and measurement

After publication permission and a live listing, run workflow 06 as experiments rather than guarantees. Neutral review requests may invite feedback or a review without obligation, influence, compensation, reciprocity, or sentiment filtering. Record posts, attributed discovery, sales, refunds, and net collection separately. No ads in Book One.

## Daily Checkpoint Map

| Day | Default checkpoint |
|---:|---|
| 1 | Interview, constraints, risk exclusions, pen-name direction |
| 2 | Candidate market evidence |
| 3 | Niche approval |
| 4 | Reader promise, source plan, and outline |
| 5 | Outline approval and gold-chapter brief |
| 6–7 | Gold chapter and Day-7 conditional gate |
| 8–10 | Full draft in controlled sections |
| 11 | Developmental and claim review |
| 12 | Line/copy edit, redundancy, originality, reader QA |
| 13 | Cover and listing package |
| 14 | Compliance and upload-readiness gate |
| 15–30 | Only when needed: interviews, qualified review, rewrites, beta feedback, or rights remediation |

## Output Requirements

Return the current cockpit, evidence-backed decision, approvals, blocking gate, exact next action, and proof state. Every claim is labeled `OFFICIAL`, `OBSERVED`, `SOURCE_REPORTED`, `OPERATOR_HEURISTIC`, or `UNTESTED` where ambiguity matters.

`Execution prompt: references/prompts-v2/book-one-pilot-cockpit.md`

## Quality Gate

- [ ] The source ledger and policy boundary were loaded.
- [ ] A current 5–10-topic scan precedes drafting.
- [ ] Niche, outline, gold chapter, cover, and upload are separate approvals.
- [ ] The manuscript passes all five AI-failure gates plus claim, originality, redundancy, and reader QA.
- [ ] AI asset classification and rights evidence exist for text, cover, interiors, translations, and metadata.
- [ ] Review tactics contain no exchange, payment, points, influence, reciprocity, or close relationships.
- [ ] Ebook and print artifacts are format-specific and previewed.
- [ ] Pace escalation never bypasses a gate.
- [ ] No production event is reported as a discovery, sale, or collection event.
- [ ] No external action occurs without explicit permission.
