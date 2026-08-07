---
name: produce-manuscript
description: Build and approve a gold chapter, then produce a sourced, human-authored, AI-disclosed manuscript through controlled sections, rolling context, five anti-slop gates, and full editorial/reader QA.
produces: QA-passed manuscript package, claim ledger, authorship/AI receipt, originality receipt, and reader-quality receipt
expert: Sean Dollwet
load_context: genius.md
---

# Produce Manuscript — Gold Chapter to Reader-Ready Book

## Pre-Flight Gate

Run only after the blueprint and outline are approved. A deadline never overrides a claim, rights, originality, reader, or disclosure gate. Load the blueprint, `genius.md`, `references/prompt-chain.md`, `references/kdp-policy-and-evidence-boundary.md`, and the Book One cockpit.

## Execution

### 1. Interview for human material

Collect the operator's real stories, mistakes, decisions, examples, language, and useful frameworks. Ask only for material the system cannot research. Never invent lived experience, credentials, testimonials, or case outcomes.

### 2. Build one gold chapter

Draft one representative section at a time. AI may assist, but the human author owns the promise, source choices, analysis, examples, exercises, language, and final expression. Maintain a rolling packet containing reader, promise, outline, terminology, claims made, sources, examples used, open facts, and repetition watchlist.

Apply five independent gates:

1. **Truth** — every factual claim is supported, qualified, or cut.
2. **Depth** — the chapter explains mechanisms, decisions, examples, and use; no surface paraphrase.
3. **Non-repetition** — information and phrasing advance rather than loop.
4. **Voice** — concrete, specific, and human; no textbook/default-model tone.
5. **Editability** — the remaining manuscript can meet this standard without hiding unsolved debt.

Checkpoint: Farrice approves, revises, or rejects the gold chapter.

### 3. Draft the full manuscript in controlled sections

Generate or write one section at a time using the rolling packet. Update the claim ledger, source links, cross-references, terminology, examples, and repetition watchlist after each section. Stop when a source, story, permission, or expert-review gap appears.

### 4. Run the editorial stack

- Developmental edit: promise, transformation, missing logic, chapter order, usefulness.
- Claim/source audit: every factual statement and outcome claim.
- Information-redundancy map and structural-tempo pass.
- Line and copy edit for clarity, rhythm, consistency, grammar, and accessibility.
- Originality and similarity review, with human judgment and rights follow-up.
- Beta/reader QA against the target reader and promised use.

No `[AUTHOR STORY]`, citation, verification, permission, or fact-check placeholder survives `QA_PASSED`.

### 5. Close authorship and AI evidence

Classify every actual text/image/translation/metadata asset as human, AI-assisted, AI-generated, or third-party. If AI created the actual asset, record KDP disclosure even after substantial edits. Document qualifying human contributions without making a blanket copyright claim.

### 6. Prepare format-specific outputs

Create a reflowable DOCX/KPF/EPUB for the Kindle ebook. Print, if in scope, gets a separate print-ready PDF. Both move to Previewer/print proof only after manuscript QA.

## Pace Rule

`rapid_7`, `launch_14`, and `editorial_30` use the same gates. Failure at Day 7 escalates to Day 14; failure at Day 14 remains open through Day 30.

## Output Requirements

- Approved gold chapter and approval receipt.
- Full manuscript plus rolling-context and revision records.
- Final claim/source ledger.
- Developmental, redundancy, line/copy, originality, and reader QA receipts.
- Asset-level AI/authorship/rights ledger.
- Reflowable ebook source and separate print file when applicable.

`Execution prompt: references/prompts-v2/book-production-package.md`

## Quality Gate

- [ ] Gold chapter approved before full drafting.
- [ ] No fabricated story, credential, fact, citation, review, or case result.
- [ ] Every claim is supported, qualified, or removed.
- [ ] All five anti-slop gates pass.
- [ ] Developmental, redundancy, line/copy, originality, and target-reader QA pass.
- [ ] Zero placeholders remain.
- [ ] AI disclosure and human contribution are recorded per asset.
- [ ] Pace never overrides quality.
- [ ] Ebook and print outputs are format-specific.
