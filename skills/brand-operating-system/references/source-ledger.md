# Source Ledger — brand-operating-system

Every source consulted for this repair pass, claim-by-claim, with confidence labels. `brand-operating-system` is a methodology skill (6-layer BOS architecture), not a single-person extraction — its ground truth is the skill's own shipped proof (the Resonance build for Andrea) plus the skill's existing SKILL.md/genius.md/workflow files. Labels: **VERIFIED** (I opened the file and the claim/quote is exactly there) / **LIKELY** (internally consistent with a source I read, not independently cross-checked outside this repo) / **UNCONFIRMED** (could not locate verbatim; not used as an anchor).

---

## Primary sources (read in full, quotes checked verbatim)

| # | Source | What it grounds | Label |
|---|---|---|---|
| 1 | `skills/brand-operating-system/SKILL.md` (git HEAD) | Skill scope, 6-layer output tree, 7-phase table, existing anti-patterns list | VERIFIED |
| 2 | `skills/brand-operating-system/genius.md` (git HEAD, pre-repair) | Baseline for all genius.md additions — architecture rationale, phase sequencing, `_working/` rationale | VERIFIED |
| 3 | `skills/brand-operating-system/workflows/01-discover.md` … `07-wrap.md` (git HEAD, all 7) | Baseline for every new Output Schema section — restates only what the Steps sections already document, formalized | VERIFIED |
| 4 | `_active/andrea-dj/brand-operating-system/_working/G1-adversarial-review.md` | All 5 dated/quoted anti-pattern items in genius.md's new "Anti-Patterns — Caught in the Field" section (Fixes 1-5, Axis scores, survival tests) | VERIFIED — every quote below was matched character-for-character against this file |
| 5 | `_active/andrea-dj/brand-operating-system/_working/A1-reconciliation.md` | 6th anti-pattern item (Section 3, conflict #6 — "the couple is residue" vs. "we count the couples") | VERIFIED |
| 6 | `_active/andrea-dj/CLAUDE.md` | Confirms Resonance is the live, canonical, currently-operated BOS instance (not archived) | VERIFIED |
| 7 | `_active/andrea-dj/brand-operating-system/` directory listing (43 files, `find` output) | Confirms the "43 markdown documents" claim already in SKILL.md is accurate to the actual shipped tree | VERIFIED |
| 8 | `execution/skill_auditor.py` (`_anti_pattern_items`, `_HB_SOURCE_ATTR_RE`, `_HB_RECOG_RE`, `_HB_OUTPUT_SCHEMA_RE`, `_sections_zero_entity`) | The exact check logic this repair targets — read to confirm every fix actually satisfies the auditor's regexes, not just "looks right" | VERIFIED (also re-implemented locally and dry-ran against the repaired files before finalizing) |
| 9 | `skills/ben-watkins-storytelling/genius.md`, lines 1-30 | Style model for the new "How to Use This Skill (Model Calibration)" section, per ENVELOPE instruction — structure adapted, no text copied | VERIFIED |

## Quote-by-quote verification (the 6 sourced anti-pattern items in genius.md)

| Quote used | Exact match found in | Label |
|---|---|---|
| "every paste-in session would have hit broken paths" | `G1-adversarial-review.md`, Axis 4 | VERIFIED |
| Brand Bible §1 em-dash count / voice rule ≤2 | `G1-adversarial-review.md`, Axis 3 / Fix 2 | VERIFIED |
| "Sponsor decision template is abstract — doesn't anticipate the most likely real offer (wellness-aligned brand, $5K-10K product placement + 30-second stage acknowledgment)" | `G1-adversarial-review.md`, Fix 3 | VERIFIED |
| "Brand Bible §1 cites legacy `01-pulse-brand.md` while AI Brain Master bans the term 'Pulse.'" | `G1-adversarial-review.md`, Axis 2 / Fix 4 | VERIFIED |
| "if a photo could have been taken at 11pm, it fails" | `G1-adversarial-review.md`, Axis 1 (also appears in SKILL.md and original genius.md, all consistent) | VERIFIED |
| "the experience is the point; the couple is the residue" / "We count the couples, not the followers." | `A1-reconciliation.md`, Section 3, conflict #6 | VERIFIED |

## Sources surveyed for this skill but NOT incorporated (scoping decision, recorded for auditability)

The dispatch note for this repair flagged `extractions/` files matching "oren" and "brand" as possible grounding. I read all of the following and made a deliberate decision not to use them as anchors in the final genius.md, for the reason stated:

| Source | Why surveyed | Why not used |
|---|---|---|
| `extractions/oren/extraction-report.md`, `oren-systems-extraction-report.md`, `extraction-report-repositioning.md`, `transcript.txt` | Candidate "brand" expert grounding | The extraction identifies this creator only as "Oren" — first name only, no surname anywhere in the file or transcript (confirmed via `grep -ril "klaff" extractions/` returning zero hits). His domain (luxury purchase psychology, operational systems for creative freelancers) is real and well-documented but does not overlap with the BOS's specific 6-layer documentation architecture — force-fitting a citation here would be a manufactured connection, not a genuine one |
| `extractions/oren-1person-ai-marketing/` | Same creator, different video | Same reasoning — different domain (1-person AI marketing ops), not BOS architecture |
| `extractions/oren-identity-brand-os/reference-corpus/the-7-levels-of-brand-building.md` (source: youtube.com/watch?v=UBDpGwdkiz4, "orenmeetsworld" channel, published 2025-09-23) | Titled "brand building" — closest surface match to this skill's name | Describes a 7-*stage* commerce-brand growth ladder (channel-finding → foundation → multiplier → crossover → secret sauce → scale → staying interesting) — a business-maturity framework, not a documentation-layer architecture. Distinct from this skill's 6 *layers* (Foundation/Visual/Briefs/Marketing/AI-Handoff/Ops). Citing it as "the source of the 6-layer structure" would be false — the 6-layer structure comes from the Resonance build itself (see primary sources above) |
| `extractions/oren-identity-brand-os/reference-corpus/creatives-guide-to-personal-branding.md`, `blind-pass-log.md`, `blind-pass-candidate-driver-diagnostic.md` | Same creator/skill cluster | Personal-branding/creative-career domain, not BOS-relevant |
| `extractions/oren-john-identity-marketing/` (mastery-extraction.md, source-transcript.md, companion-brand-archetypes.md, companion-stussy-art-direction.md, vision.md, arsenal-map.md) | Name overlap ("identity", "brand") | Different extraction subject (brand archetypes / streetwear art direction) — not consulted for BOS methodology; not read in full for this pass, flagging as UNCONFIRMED relevance rather than claiming review |
| `extractions/brand-master/extraction-report.md` (Greg Hoffman, former Nike Global CMO, "Emotion by Design") | Named, credentialed brand expert — real person, verifiable public figure | Read in full; genuinely strong material (Seen→Felt→Proven, Overground/On-the-Ground/Underground). Not used as an anchor in genius.md because none of its patterns map onto the specific checks this repair targets, and forcing a citation in to "look sourced" would be exactly the padding this repair is supposed to avoid. Flagged here so a future amender knows it was read and is available for a real (non-forced) synthesis pass |
| `extractions/BitBranding/transcript.txt` | Name match ("brand") | Skimmed; not brand-architecture-relevant to this skill's scope (BitBranding covers a different niche) — not used |

**Labeling note on the surveyed-but-unused row for Greg Hoffman**: the biographical claims in `extractions/brand-master/extraction-report.md` ("Former Global CMO, Nike," "27 years," authored "Emotion by Design") are LIKELY — consistent with the extraction file's own stated sourcing (a 505 Podcast Ep. 197 transcript) but not independently web-verified in this session, and not relied upon anywhere in the shipped repair.

## UNCONFIRMED (explicitly not used as anchors anywhere in this repair)

None. Every quote and dated claim used in the repaired genius.md and workflow files was verified against a primary file read in this session (see table above). No claim in the delivered files carries an UNCONFIRMED label because no UNCONFIRMED claim was used — anything I could not verify verbatim was left out rather than softened into the deliverable.
