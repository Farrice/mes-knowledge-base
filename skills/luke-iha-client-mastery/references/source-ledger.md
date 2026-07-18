# Source Ledger — luke-iha-client-mastery

Single source of record for every factual/methodology claim this skill carries. Labels per
`directives/verification-agent-protocol.md`: VERIFIED (directly present in the primary source
material, independently read for this repair pass), LIKELY (consistent with the primary
material but not itself stated verbatim), UNCONFIRMED (asserted by this skill's own files but
not found in any Luke Iha extraction read for this pass — quarantined, cite as "as documented
in the skill" rather than fact).

## Source Manifest

All files below live under `extractions/luke-iha*/` and were read directly for this repair
pass (2026-07-18). Sizes via `wc -c`.

| # | File | Size (bytes) | Status |
|---|---|---|---|
| 1 | `extractions/luke-iha-client-acquisition/transcript.txt` | 20,329 | VERIFIED — full transcript read. Primary source for CR × OU formula, Paid to Feel / nervous-system framing, Meta Andromeda, "creative is the new targeting" |
| 2 | `extractions/luke-iha-creative-strategist/transcript.txt` | 32,648 | VERIFIED — full transcript read. Primary source for the 7-Rung Proof Ladder, POP stack (Positioning × Offer × Proof), testimonial ghost-write method, blue-chip halo effect (VS Shred / Spartan Hair examples), track record, case studies |
| 3 | `extractions/luke-iha/extraction-report.md` | 7,915 | Read — general Luke Iha extraction report; no client-mastery-specific claims found beyond what's covered in #1-#2 |
| 4 | `extractions/luke-iha/video-8-proof-ladder/extraction-report.md` | 17,119 | Checked (grep pass) — proof-ladder adjacent, overlaps with #2's ladder content; no additional claims used |
| 5 | `extractions/luke-iha/video-1-proof-mechanisms/extraction-report.md` | 6,936 | Checked (grep pass) — proof-mechanisms adjacent (belongs primarily to sibling skill `luke-iha-proof-mechanisms`); no client-mastery-specific claims pulled |
| 6 | `extractions/luke-iha-hooks/transcript.txt` | 25,569 | Checked (grep pass) — hooks/copy domain, not client-acquisition; no claims pulled |
| 7 | `extractions/luke-iha-insight-mastery/transcript.txt` | 20,035 | Checked (grep pass) — insight-vectors domain, not client-acquisition; no claims pulled |
| 8 | `extractions/luke-iha-avatar-machine/Copy_of_SOP_for_Swiping.txt` | 18,226 | Checked (grep pass) — belongs to sibling skill `luke-iha-avatar-machine`; referenced once below as circumstantial (not primary) support for an UNCONFIRMED claim |

## Claim Ledger

| Claim (genius.md pattern) | Label | Basis |
|---|---|---|
| Paid to Feel — "AI doesn't have a nervous system," judgment via bodily sensation (chest/gut/neck) | VERIFIED | `extractions/luke-iha-client-acquisition/transcript.txt` — full section on the headline-feeling exercise, "AI doesn't have a nervous system" quoted verbatim |
| CR × OU Formula — Clients = Conversion Rate × Outreach Units, 5-10 outreach/day | VERIFIED | `extractions/luke-iha-client-acquisition/transcript.txt` ("your OU, which basically translates to... outreach units") and `extractions/luke-iha-creative-strategist/transcript.txt` ("How many clients you get is equal to your conversion percentage times your OU") — stated in both sources |
| 7-Rung Proof Ladder (Resume → Samples → Certifications → Testimonials → Track Record → Case Studies → Blue-Chip) with per-rung timelines | VERIFIED | `extractions/luke-iha-creative-strategist/transcript.txt` — full walkthrough of all 7 rungs with timeline estimates (1-2 hrs, 1-2 days, 1-7 days, 1-4 wks, etc.) |
| Testimonial Ghost-Write Method (write it yourself, "not too insanely glowing," follow up 4-5x, $50-for-testimonial hustle) | VERIFIED | `extractions/luke-iha-creative-strategist/transcript.txt` — testimonials section, "I used to go on Upwork and tell people, 'I'll pay you $50 to work for you'" quoted near-verbatim (transcript: "I'll pay you $50 to work work for you") |
| Blue-Chip Halo Effect — funneloftheweek.com, VS Shred ($300M company), Spartan Hair | VERIFIED | `extractions/luke-iha-creative-strategist/transcript.txt` — blue-chip section names all three specifically |
| Creative Is the New Targeting (Post-Andromeda) — Meta Andromeda, three forces (AI production ease, Andromeda creative-diversity mandate, DTC shift to performance marketing) | VERIFIED | `extractions/luke-iha-client-acquisition/transcript.txt` — full Andromeda explanation section |
| POP Stack — CR = Positioning × Offer × Proof, proof = 80-90% of conversion | VERIFIED | `extractions/luke-iha-creative-strategist/transcript.txt` — "your conversion rate is made up of three different things... by far 80 to 90% of this depends on your proof" |
| Assembly-First Innovation (start with market assembly, deconstruct/reconstruct) | **UNCONFIRMED** | Not located verbatim in any of the 8 files read for this pass. Directionally adjacent to the Swiping SOP's "build from real market copy, don't invent" instruction (`extractions/luke-iha-avatar-machine/Copy_of_SOP_for_Swiping.txt`), but that file belongs to a different Iha extraction/skill and does not use "assembly-first" framing. Flagged UNCONFIRMED in genius.md itself; kept (not deleted) per additive-first repair policy, with an explicit provenance caveat attached in-place |
| "How I" Case Study Narrative template | VERIFIED | `extractions/luke-iha-creative-strategist/transcript.txt` — case studies section: "case studies is what happens when you stack your track records together... you're basically telling a story about how you impacted a brand" |
| Burnout Prevention (5 full-time jobs compressed, sprint-then-maintain) | **UNCONFIRMED** | Not located verbatim in any of the 8 files read for this pass. No transcript names a "5 jobs" or burnout-prevention framing. Flagged UNCONFIRMED in genius.md itself; kept (not deleted) per additive-first repair policy, with an explicit provenance caveat attached in-place |
| Signature Moves (Nervous System Scan, Proof Ladder Blueprint, CR × OU Diagnostic, "How I" Narrative Frame, Blue-Chip Sprint) | VERIFIED (as summaries of already-verified patterns above) | Each signature move restates a VERIFIED pattern above; no new claims introduced |

## Coverage Caveat (honest gap)

This skill's SKILL.md and genius.md draw exclusively on two primary transcripts
(`luke-iha-client-acquisition` and `luke-iha-creative-strategist`) — both are single-video
YouTube transcripts (~20-33K bytes each), not multi-session workshop material like the sibling
`luke-iha-avatar-machine` skill's 14-file corpus. Two genius.md patterns (Assembly-First
Innovation, Burnout Prevention) have no located source anywhere across the 8 Luke Iha
extraction files checked for this pass and are labeled UNCONFIRMED in-place rather than
removed. If a future extraction surfaces primary material for either, update this ledger and
strike the UNCONFIRMED label.

## Recognition Test

Would Luke Iha recognize this skill's output as his own client-acquisition system? The test:
does the output state CR × OU as a literal formula (not a vague "do more outreach" gesture),
walk the proof ladder in strict rung order with nothing skipped, treat proof as 80-90% of
conversion weight, and frame creative judgment as a felt bodily signal rather than a data
preference? If it reads as generic freelance-coaching advice wearing his terminology
(vocabulary present, no formula math, no rung sequencing, no felt-sense instruction), it fails
the test even if every term is spelled correctly.
