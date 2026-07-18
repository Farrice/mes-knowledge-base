# Source Ledger — kj-rainey-copywriting

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 8). Ground-truth search performed:
`extractions/` (full directory listing + `grep -ril "rainey\|copy elite"` — zero hits) and
`_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, 3,864 archive entries; the
`normalized/conversations/` subtree — 3,712 files, 272MB — was extracted in full to a
scratchpad directory and grepped for "Rainey," "Copy Elite," and every distinctive quote
fragment named in `genius.md`). One primary source located. No second source found for
any of the six named frameworks despite the exhaustive search — this is recorded as the
gap, not asserted as proof nothing exists (per the envelope's rule 2: an absence claim is
itself a provenance claim).

## Primary source located

**File**: `claude-export/normalized/conversations/27625845-1f83-4282-869a-4f52267514a1.md`
(inside `_archive/claude-export-2026-07-01.tar.gz`)
**Title**: "KJ Rainey: the highest-rated coaching call in copy elite history."
**Size**: 101,615 bytes / 2,298 lines / 19,742 words (per file frontmatter)
**Date**: conversation created 2025-07-14T02:31:03Z; source YouTube video by Merlin AI
transcription, embedded as a `paste.txt` attachment inside the conversation.
**Content**: a ~74-minute "life and Christian entrepreneurship" coaching call transcript
(mindset, purpose, faith, work/rest balance, gaming) plus a Claude extraction attempt
(MES 3.0 protocol) that self-reports fabricating "7 virtuoso prompt artifacts" and "12
transcendence opportunities" worth "$100M+" — those downstream artifacts were never
captured in the export (the tool-render blocks read "Viewing artifacts... isn't yet
supported on mobile"), so nothing past the raw transcript is available to verify against.

## Claim-by-claim ledger

| Claim (SKILL.md / genius.md) | Label | Basis |
|---|---|---|
| KJ Rainey is the founder of Copy Elite | **VERIFIED** | Video title + transcript throughout ("in Copy, we have these things called... freestyle Friday calls... copy elite," lines 26-36); KJ is the main speaker addressed by name by call participants (line 686, 1132, 1191). |
| Copy Elite is a coaching community with numbered "principles" | **VERIFIED** | "Number eight, principles of copy lead my company. It says, 'Give it your all, but remember, perfection doesn't exist on this earth. Perfection is a lie. It doesn't exist.'" (lines 1065-1069). |
| "So many people are so focused on the numbers you forget that there's every one of those numbers is a human being on the other side." | **VERIFIED** | Direct KJ quote, lines 815-819. |
| Business scale reference | **VERIFIED, but conflicts with SKILL.md's stated number** | Transcript states "$60K a month" twice (line 599, "my business was like sitting at 60k a month"; line 2226, extraction summary "$60K/month"). SKILL.md/genius.md instead claim "$500K+/year." $60K/mo annualizes to ~$720K/yr, so the two are not necessarily contradictory, but no single source confirms "$500K+/year" as KJ's own stated figure — flagged, not corrected (additive-only repair). |
| "$1,600/month... reading $100M Offers sick in bed at Christmas... 'we're going to be millionaires'" origin story | **UNCONFIRMED** | Not present in the located transcript; no second source found. |
| "if you have a good product, not trying to sell it is unethical" | **LIKELY** (not VERIFIED) | Present verbatim at lines 762-763, but the transcript has no speaker diarization — surrounding context suggests a call participant ("Mr. T" / another member) sharing a realization, echoing KJ's teaching rather than a direct KJ quote. Treated as Copy Elite house philosophy, attribution to KJ personally not certain. |
| Pattern: Objection Archaeology / 100-Reasons Framework (incl. "a year's amount of work... untouchable," "has no choice but to convert," "25x outreach conversion") | **UNCONFIRMED** | Zero matches on distinctive phrases in the located transcript; no second source found. |
| Pattern: Pain-of-Inaction Formula (hand-on-stove analogy) | **UNCONFIRMED** | Not present in located transcript; generic direct-response concept (predates KJ in the broader copywriting canon) attributed here without a KJ-specific source. |
| Pattern: Situation + Feeling Pain Equation (incl. "75 of those big plans fail") | **UNCONFIRMED** | Not present in located transcript. |
| Pattern: Core-Desire Targeting via Maslow (~80% status/freedom weighting) | **UNCONFIRMED** | Not present in located transcript; the underlying Maslow-derived "core desires" list is standard direct-response teaching (echoes Eugene Schwartz/Gary Halbert lineage), not verified as KJ's own framing. |
| Pattern: The 5-Step Value Chain (incl. "$540K in a year" chain example) | **UNCONFIRMED** | Not present in located transcript. |
| Pattern: Business-Owner Fear Quartet (incl. "$500K for a quick $50K") | **UNCONFIRMED** | Not present in located transcript. |
| Pattern: One-Word Exit Guarantee ("I would pay 20K...") | **UNCONFIRMED** | Not present in located transcript. |
| Pattern: Reply-Yes Middle Rung + Notion lead-magnet origin story | **UNCONFIRMED** | Not present in located transcript. |
| Pattern: The Iceberg Doctrine ("Stop asking ChatGPT... good thinker," "$100M Offers" tactics-vs-principles framing) | **UNCONFIRMED** | Not present in located transcript. |
| Hidden Knowledge: Firing Is Emotional, Goodwill Sponge ("$30K in a week," "juicing the sponge"), Believability Ceiling, Conditions Deck, Buy Speed With Money ("$100 expense," DoorDash), Don't Overdose the Pain, SUCCESS/Cialdini/50 Scientifically Proven Ways reading list | **UNCONFIRMED** (all 6 insights) | None of the distinctive phrases appear in the located transcript; no second source found. |
| Workflow files (`01-forge-irresistible-offer.md`, `02-write-pain-driven-copy.md`, `03-build-value-chain.md`) — role framing, Mark's email-marketing-offer example | **UNCONFIRMED** | Same status as the frameworks they operationalize; not modified in this repair pass (workflow_contracts check already passed pre-repair). |

## What this means for use

Treat the identity/bio layer (KJ Rainey, Copy Elite, first-principles/no-guru-speak
mindset, "perfection is a lie," people-over-numbers) as grounded. Treat every named
framework (Objection Archaeology, Pain-of-Inaction Formula, Pain Equation, Core-Desire
Maslow Targeting, 5-Step Value Chain, Business-Owner Fear Quartet, One-Word Exit,
Reply-Yes Middle Rung, Iceberg Doctrine) and its dollar figures as **skill-internal
content carried forward from a prior extraction pass, not independently re-verified in
this repair**. If a client-facing deliverable needs to cite KJ Rainey by name with a
specific number or quote, re-verify against the original video/course material first —
do not present the UNCONFIRMED rows above as sourced fact.
