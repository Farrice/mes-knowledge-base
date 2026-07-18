# Provenance — chris-do-design-business repair

Ground-truth check (2026-07-17): `ls extractions/` (193 entries) + `grep -i "chris\|do\|futur"` returned zero matches. No `extractions/` file exists for Chris Do / The Futur. All anchors below therefore point to the skill's own pre-existing files (frontmatter-dated `claude.ai export 2026-07-01`), not to an independent transcript.

## Anti-Patterns section (genius.md, new)

| Anti-pattern item | Anchors to |
|---|---|
| Fighting the fact instead of reframing it | genius.md original lines 7-10, "Pattern: Reframing as the Master Move" (paint/gallery quote verbatim from that pattern) |
| Positioning without naming the real competitor | genius.md original lines 12-15, "Pattern: Pick a Fight You Can Win" (Scope/Listerine, 7UP examples verbatim from that pattern) |
| Pricing bottom-up from hours or costs | genius.md original lines 17-20, "Pattern: Price as Positioning Instrument" ("no time sheets, outcomes only" verbatim) |
| Pitching instead of diagnosing on a sales call | SKILL.md original line 52, Quick Reference "Sales (the kind way)" ("whoever asks more questions is in control of the relationship" verbatim) |
| Skipping to content tactics before the acceptance layer | genius.md original lines 32-35, "Pattern: Know → Accept → Express" ("the paint is dry," "your words shape your world" verbatim) |
| Leading a strategy deck with research instead of conviction | genius.md original lines 66-68, "Insight: Future-first, data-second" ("data is a story of the past; disruption is a story about the future" verbatim) |

## How to Use This Skill (Model Calibration) section (genius.md, new)

Not a sourced-claim section (calibration guidance, not a factual claim) — modeled structurally on `skills/ben-watkins-storytelling/genius.md` lines 7-16 (intuition-primitives framing, "would [X] recognize this as theirs" test, polish-is-the-tell warning) but written fresh against Chris Do's actual patterns already documented in this same genius.md (Socratic reframing, know→accept→express, plain/specific-over-polished teaching style — see Pattern list above for the underlying material each calibration bullet references).

## Source Ledger (references/source-ledger.md, new)

Every row cross-references either (a) a real, independently-checkable public fact/book/artifact (labeled VERIFIED), (b) content consistent with Chris Do's/The Futur's known public teaching but unconfirmed against a primary transcript in this repo (labeled LIKELY), or (c) a specific number/quote/named-collaborator claim with no source file to check (labeled UNCONFIRMED). No claim in the ledger was invented for this repair — every row corresponds to a claim already present in the pre-existing SKILL.md or genius.md text before this repair pass touched them.

## Files NOT modified (already passing, left untouched per additive-first boundary)

- SKILL.md (recognition_test now satisfied via genius.md instead — no edit needed)
- workflows/01-position-and-price-premium.md, 02-run-kind-sales-call.md, 03-build-personal-brand-engine.md (workflow_contracts already PASS)
- references/prompts-v2/*.md (not implicated by any failing check)
