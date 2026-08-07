# KDP Policy and Evidence Boundary

Checked 2026-08-04. Re-check official pages before upload because platform rules and interfaces can change.

## Truth order

1. `OFFICIAL`: current KDP or government source.
2. `OBSERVED`: directly present in a source or artifact.
3. `SOURCE_REPORTED`: creator claim, including BSR, pricing, review, timing, income, and algorithm claims.
4. `OPERATOR_HEURISTIC`: reversible pilot choice such as Amazon-first, organic-only, or the Day-14 default.
5. `UNTESTED`: no Book One runtime or buyer evidence.

Official policy overrides every video tactic.

## Publication preflight

1. **Account** — one KDP account; legal identity, tax, bank, and verification complete. A pen name belongs in book metadata, not the KDP account identity.
2. **Rights** — evidence for manuscript, quotations, cover, interior images, fonts, stock, freelancers, territories, formats, privacy/publicity, and trademarks.
3. **AI assets** — classify text, cover, interior art, translations, and metadata copy separately. If AI created the actual asset, KDP calls it AI-generated even after substantial editing and requires disclosure. [KDP Content Guidelines](https://kdp.amazon.com/en_US/help/topic/G200672390)
4. **Human authorship** — copyright protects qualifying human expression, arrangement, and modifications case by case; prompts and cleanup do not automatically protect the whole output. [USCO Part 2](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf)
5. **Originality and quality** — fact-check, similarity, repetition, misleading claims, file integrity, and reader experience. Recycled or disappointing content can be rejected. [KDP Quality](https://kdp.amazon.com/en_US/help/topic/G200952510)
6. **Metadata** — cover and interior match; title plus subtitle stay under 200 characters; author, contributors, keywords, categories, audience, and claims are accurate. [KDP Metadata](https://kdp.amazon.com/en_US/help/topic/G201097560)
7. **Files** — narrative ebook defaults to reflowable DOCX, KPF, or EPUB and passes Kindle Previewer. Print uses a separate print-ready PDF. [KDP Formats](https://kdp.amazon.com/en_US/help/topic/G200634390)
8. **Reviews** — a free/discounted copy is allowed only when a review is neither required nor influenced. No payment, points, gift cards, reciprocity, close relationships, or positive-conditioned follow-up. [KDP Reviews](https://kdp.amazon.com/en_US/help/topic/G202101910)
9. **Distribution** — KDP Select is opt-in, binds the Kindle ebook to 90-day digital exclusivity, and auto-renews unless disabled. It stays off for Book One unless Farrice separately approves it. [KDP Select](https://kdp.amazon.com/en_US/help/topic/GD9PMU58BV24QFZ7)

## AI asset and rights row

`asset_id, asset_type, version_hash, creator, tool_model, creation_mode, source_inputs, human_contribution, ai_material_description, kdp_disclosure_required, disclosure_answer, rights_basis, rights_holder, license_evidence, permitted_formats, territories, attribution, privacy_publicity_trademark_check, registration_material_excluded, evidence_path, reviewer, reviewed_at, status`

Allowed `creation_mode`: `human`, `ai_assisted`, `ai_generated`, `third_party`.

## Automatic failures

- AI-generated asset marked as not requiring disclosure.
- Missing rights or commercial-use evidence.
- Competitor wording, distinctive sequence, examples, or substantial similarity retained.
- Paid, points-based, reciprocal, required, influenced, or insider review plan.
- KDP Select plus a conflicting digital download or wide-distribution plan.
- Narrative ebook supplied only as an unpreviewed PDF.
- Unsupported health, legal, financial, or income outcomes.
- Reused chapters or lightly varied books across the catalog.

## Proof states

- Production: `NO_EVENT → DRAFTED → QA_PASSED → UPLOAD_READY → SUBMITTED → LIVE`
- Capability: `SOURCE_CAPTURED → STRUCTURAL_PASS → ORCHESTRATOR_ATTESTED → RUNTIME_OBSERVED`
- Market: `NO_EVENT → DISCOVERED → SOLD → NET_COLLECTED`
- Permission: `NO_PERMISSION → APPROVED`

Progress on one axis never implies progress on another.
