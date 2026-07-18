# Source Ledger — sean-kochel-ai-business

Every source consulted while repairing this skill (Wave 3 Lane 4 Batch 15), labeled
VERIFIED / LIKELY / UNCONFIRMED, claim-by-claim. "VERIFIED" means the exact text was
opened and read in this repair session and the quote used in genius.md matches it
verbatim. "LIKELY" means the source is real and on-topic but the specific claim built
from it was not cross-checked word-for-word. "UNCONFIRMED" means no source file could
be located for the claim — it predates this repair and is flagged, not deleted.

## Primary sources (read in full this session)

1. **`_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/f551b192-de2c-4e6f-a552-66b97aebfd03.md`**
   Conversation title: "Sean Kochel | These 5 Books Reveal Why Most AI Products Don't
   Sell | Ai Business Mastery." Created 2026-01-30T12:08:43Z. Contains the full verbatim
   YouTube transcript (human turn, ~2,000 words) covering Eugene Schwartz (awareness/
   sophistication), Robert Cialdini (7 principles), "Yes! 50 Scientifically Proven Ways
   to Be Persuasive," Kyle Milligan's NESB, and Blair Warren's One Sentence Persuasion
   Course, plus Kochel's live teardown of Pick Key and Postsyncer landing pages.
   — **VERIFIED**: every quote cited from this file in genius.md's new Anti-Patterns
     section and How to Use This Skill section (Pick Key critique, Postsyncer critique,
     "join thousands"/"join founders like you," "don't litter"/"most people don't
     litter here") was matched verbatim against this file's text.
   — This is the direct ground-truth source for the skill's title framing ("The 5 books
     that reveal why most AI products don't sell") and for crown_jewel prompts 1-7
     (Diagnostic, Headlines, Cialdini, NESB, Identity, Sophistication, Commitment).
   — This file was NOT present under `extractions/sean-kochel/` (that directory holds
     only the `sean-kochel-design-first-build` transcript — confirmed by
     `extractions/sean-kochel/extraction-report-design-first-build.md` line 12: "NO
     overlap with this content"). It was located only via the mandated tarball content
     scan of `_archive/claude-export-2026-07-01.tar.gz` (332MB, 7,720 members scanned
     with a Python `tarfile` per-member content grep for "kochel", case-insensitive).

2. **`_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/23c8f9f6-e3e3-4aca-b0cf-7f2080e6b351.md`**
   Conversation title: "10-29-25 Sean Kochel: Better features don't get users—this
   psychology does." Created 2025-10-28T22:45:02Z. Verbatim timestamped transcript
   applying Cialdini's principles to product-building, with the Quibi ($1.75B raised,
   died in 6 months), Dropbox (500MB referral, 3,900% growth), Notion (onboarding
   checklist, 3-of-7 steps), and Stripe (Y Combinator authority-borrowing) examples.
   — **VERIFIED**: the Quibi/Cialdini opening quote cited in genius.md's Anti-Patterns
     section was matched verbatim (transcript auto-caption artifacts "Quibby" and
     "Chelini" preserved as-quoted, glossed in brackets).
   — Directly informs crown_jewel prompts covering social proof, reciprocity,
     commitment/consistency, and authority in a product-building (not just landing-page)
     context.

## Skill-internal sources (already inside the skill; re-verified this session)

3. **`skills/sean-kochel-ai-business/references/prompts-v2/*.md`** (23 files, "structure-pure v2,"
   `refactored: 2026-07-11` per frontmatter) — **VERIFIED**. Read `crown_jewel_01_diagnostic.md`
   and `crown_jewel_03_cialdini.md` in full; grepped all 23 files for the anti-fabrication
   guardrail language ("fabricat", "invent") cited in the new Anti-Patterns section —
   confirmed present verbatim at the cited files/lines. These guardrail lines do NOT
   exist in the pre-refactor originals at `references/prompts/` (confirmed by diff-grep),
   i.e. they were authored during the 2026-07-11 v2 refactor, not carried from source.
4. **`skills/sean-kochel-ai-business/genius.md`** (pre-repair version) — **VERIFIED** via
   `git blame`: "AI Moat Decay Analysis" section added 2026-04-09 (commit `a49fda981`),
   "Anti-Exemplar: Generic AI Adoption Advice" added 2026-03-20 (commit `d2688cf27`) as
   part of a 148-skill savant-enrichment pass.

## Checked and ruled out

5. **`extractions/sean-kochel/transcript.txt`** and
   **`extractions/sean-kochel/extraction-report-design-first-build.md`** — read in full
   this session; both are exclusively about `sean-kochel-design-first-build` (Google
   Stitch / research-design-build landing-page pipeline). File sizes: transcript.txt =
   17,843 bytes (`wc -c`), extraction-report = 13,417 bytes (`wc -c`) — both nonzero and
   readable, not the "0-byte/unrecoverable" failure mode this batch was warned about.
   **N/A to sean-kochel-ai-business** — the report explicitly states "NO overlap with
   this content" (line 12). Not cited in this skill's genius.md.
6. **Four additional archive hits** for "kochel" (`8a979329-88ea-482f-85a9-83b3171bcf67.md`
   — "Mid-Conversation Confabulation Audit"; `666e79b1-d1fe-40fe-a737-c67577928e97.md` —
   "Artifact & Document Quality Validator"; `9a64f0a0-8696-47d0-85dd-54bb8b8f5817.md` —
   prompt-engineering/AI-thinking-limits video; `a32286d5-e800-49b4-a12a-8e8772d1d1b6.md`
   — Stanford 7-word prompting formula) — titles/headers confirmed via grep, full bodies
   **not** read this session (out of scope for the failing checks; flagged honestly
   rather than silently read or silently ignored). **UNCONFIRMED relevance** to the
   ai-business persuasion/positioning domain specifically — do not cite as sources for
   any claim in this skill until read.

## Framework attributions (named books/authors inside the skill's prompts)

7. Eugene Schwartz, *Breakthrough Advertising*; Robert Cialdini, *Influence*; Noah
   Goldstein/Steve Martin/Robert Cialdini, *Yes! 50 Scientifically Proven Ways to Be
   Persuasive*; Kyle Milligan, *Take Their Money*; Blair Warren, *The One Sentence
   Persuasion Course* — **LIKELY**. These are real, independently known published works
   (general knowledge) and match Kochel's own framing of them in source #1 above.
   The specific mechanics attributed to each (awareness/sophistication stages, 7
   principles, NESB, 5 identity hooks) were verified against Kochel's *description* of
   the books in the transcript (source #1), not against the books' primary text
   directly — hence LIKELY rather than VERIFIED for book-level claims.

## Not sourced / synthesized (pre-existing, flagged not removed)

8. **genius.md "Hall of Fame Exemplars" 1 & 2** (AI Customer Service Transformation
   Plan; 5-Pillar Validation Matrix) and the **Expert-Specific Quality Rubric** table —
   **UNCONFIRMED**. No verbatim Kochel quote or source file backs these specific
   illustrative outputs; they read as stylistically-consistent synthesis, not
   extraction. Preserved as-is (they were already passing `verbatim_exemplars` and
   `named_entity_floor`, and this batch's scope is additive-first) but flagged here so
   they are not mistaken for sourced claims.
