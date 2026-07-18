# PROVENANCE — brand-operating-system repair (Wave 3 Batch 2)

Anchor → source file + location, for every claim/quote added in this repair pass. All locations verified by direct file read in this session (see `references/source-ledger.md` for the full survey, including sources considered and rejected).

## genius.md — "How to Use This Skill (Model Calibration)" section

| Anchor in new text | Source | Location |
|---|---|---|
| "the founder pasting that doc into Claude should feel like they're reading their own brand's voice" | Derived from the skill's own stated design goal | `skills/brand-operating-system/genius.md` (HEAD), "Why the AI Brain Master compression discipline" section, point 1 ("Cold-context AI") |
| "13 explicit conflicts between the founder's own docs and a prior vendor deliverable, plus 9 open questions" | `projects/andrea-dj/brand-operating-system/_working/A1-reconciliation.md` | Section 3 (13-row conflict table), Section 7 (9 numbered open questions) — row/item counts verified by direct count, not estimated |
| "Resonance's Brand Bible earns its ~4,000 words; its AI Brain Master earns its one paragraph" | `skills/brand-operating-system/genius.md` (HEAD) | "Why the AI Brain Master compression discipline" section, paragraph 2 |
| Style/structure model ("intuition primitives, not a checklist"; "polish is the tell") | `skills/ben-watkins-storytelling/genius.md` | Lines 7-16, per explicit ENVELOPE instruction — structure adapted to BOS-specific content, no sentences copied verbatim |

## genius.md — "Anti-Patterns — Caught in the Field (Resonance v1, dated)" section

| Anchor | Source file | Location | Verbatim quote used |
|---|---|---|---|
| File-numbering drift (CRITICAL, Fix 1) | `projects/andrea-dj/brand-operating-system/_working/G1-adversarial-review.md` | Axis 4 — Structural Soundness / "Top 5 Fixes" → Fix 1 | "every paste-in session would have hit broken paths" |
| Em-dash rule violation (Fix 2) | same file | Axis 3 — Voice Alignment / Fix 2 | "Brand Bible §1 uses 5+ em-dashes in its first paragraph, contradicting voice rule #3 (≤2 per piece)" |
| Abstract sponsor template (Fix 3) | same file | Axis 5 — Market Resilience / Fix 3 | "Sponsor decision template is abstract — doesn't anticipate the most likely real offer (wellness-aligned brand, $5K-10K product placement + 30-second stage acknowledgment)" |
| Legacy "Pulse" citation drift (Fix 4) | same file | Axis 2 — Evidence Quality / Fix 4 | "Brand Bible §1 cites legacy `01-pulse-brand.md` while AI Brain Master bans the term 'Pulse.'" |
| Golden-hour metaphor vs. literal mechanic (Fix 5) | same file | Axis 1 — Premise Integrity / Fix 5 | "if a photo could have been taken at 11pm, it fails" |
| Prior-vendor framing surviving founder override | `projects/andrea-dj/brand-operating-system/_working/A1-reconciliation.md` | Section 3, conflict row #6 ("Success metric") | "the experience is the point; the couple is the residue" (Monday Package, retired) vs. "We count the couples, not the followers." (Manifesto v2, canonical) |

## workflows/*.md — Output Schema sections

Every Output Schema section is a formalization of content already present in that same workflow file's `## Steps` section — no new external facts introduced, so the anchor for each is the file itself (git HEAD baseline, captured via `git show HEAD:skills/brand-operating-system/workflows/<file>.md` before any concurrent modification could contaminate the read — see REPAIR-NOTES.md for why that precaution was necessary).

| File | Output Schema derived from |
|---|---|
| `01-discover.md` | Steps A0-A3 (same file, HEAD) |
| `02-foundation.md` | Steps B1-B6 (same file, HEAD) |
| `03-visual.md` | Steps C1-C3 (same file, HEAD) |
| `04-briefs.md` | Steps D1, D2-D10 + asset table (same file, HEAD) |
| `05-marketing.md` | Steps E1-E4 (same file, HEAD) |
| `07-wrap.md` | Steps G1-G4 (same file, HEAD) |

## references/source-ledger.md

Self-anchoring — the ledger IS the provenance record for the survey. See that file directly for the full VERIFIED/LIKELY/UNCONFIRMED breakdown, including the extractions surveyed and explicitly not used (Oren corpus, Greg Hoffman/brand-master).
