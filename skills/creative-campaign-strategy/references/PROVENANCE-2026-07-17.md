# Provenance — creative-campaign-strategy (Ron Lynch) repair

Ground-truth check (2026-07-17): `ls extractions/ | grep -i lynch` → one hit,
`extractions/ron-lynch/transcript.txt`. `wc -c` on that file returned 67,446
bytes — read in full (not truncated, not assumed-absent). No second source
file exists for this expert.

## Anti-Patterns section (genius.md, new — "## Anti-Patterns (Source-Verified Failure Modes)")

| Anti-pattern item | Anchors to |
|---|---|
| Never lead with amenities over identity | transcript.txt, vacation-destination exchange — verbatim: "Nine out of 10 agency campaigns would show the unique features, the location. They'd show the pool. They'd show the bar." |
| Never hold the "I can't" filter open | transcript.txt, receptive-filter exchange — verbatim: "You will never come up with that as long as you say I can never do that because you've now turned off a filter of acceptance in your mind." |
| Never launch on hypothesis and stay there | transcript.txt, George Foreman Grill passage — verbatim: "it was the antithesis of families" |
| Never mistake optimization for strategy | transcript.txt, strategist-vs-copywriter exchange — verbatim: "they think strategy means looking at existing campaign data and deciding which winners were the winners and then writing more like that... That's copywriting." |
| Never stop at the copy column out of fear of production | transcript.txt, "write the other side of the column" passage — verbatim: "that's the thing that terrifies copywriters is, 'Oh my god, I got to leave my bedroom and work with other people and interact'" |
| Never advertise the literal user behavior | transcript.txt, Coca-Cola passage — verbatim: "what do Coca-Cola drinkers really do? They sit on couches and get fat." |
| Never stop at optimizing cost-of-acquisition | transcript.txt, cost-of-acquisition passage — verbatim: "a great business goes one step further and says it's not about my cost of acquisition. I want to get my cost of acquisition to zero." |

## Recognition Test section (genius.md, new — "## Recognition Test")

Not a sourced-claim section (verification framing, not a factual claim).
Built from patterns already VERIFIED elsewhere in this file: identity-first
naming (GoPro "bravery"), the 14-20 page brief standard (LIKELY — see
references/source-ledger.md), and the customer-as-media mechanism (100,000
UGC commercials, VERIFIED).

## How to Use This Skill (Model Calibration) section (genius.md, new)

Not a sourced-claim section — modeled structurally on
`skills/ben-watkins-storytelling/genius.md` lines 7-16 (intuition-primitives
framing, "would [X] recognize this as theirs" test, polish-is-the-tell
warning) but written fresh against Ron Lynch's actual documented patterns:
the two-column script (copy + visuals), the "write in the customer's voice"
principle, and the 14-20 page brief density standard — all already present
and sourced elsewhere in genius.md before this repair pass.

## Named-entity-floor enrichments (genius.md, existing sections, minimal-touch additions)

| Section | Entity added | Anchor |
|---|---|---|
| Core Genius | "$600K to $6M...year one and $16M...year two" | transcript.txt, GoPro opening passage (already used elsewhere in file; reused for this section's own body) |
| GP-9 (Advertising/Marketing Distinction) | "$10,000...60 days" radio-station case | transcript.txt, radio-station mystery-contest passage — VERIFIED (see source-ledger.md) |
| GP-12 (George Foreman Discovery) | "antithesis of families" quote | transcript.txt, George Foreman Grill passage |
| Level 1: Identity Architecture | "yoga lady...crystals and the beads" quote | transcript.txt, 5-6-product identity-stack passage |
| Level 2: Campaign Ecosystem Design | "$300 camera...super cheap advertising" | transcript.txt, contest-mechanism passage |
| Level 4: Business Operations Integration | "$80M/year for five years...$20-30K/month" | transcript.txt, cooking-appliance royalty passage |
| Level 5: Career Architecture | "$100,000 a year...over a million dollars a year" quote | transcript.txt, age-34-vs-36 passage |
| Product Selection Criteria | "$300 price point," "pretty inferior" quote | transcript.txt, GoPro-product-quality passage |
| HK-12 (Incubation Pipeline) | UNCONFIRMED flag + file-size anchor (67,446 bytes) | Bonfire Enterprises / Guthy-Renker Ventures naming not in transcript.txt — flagged in place, underlying incubation *behavior* remains VERIFIED via the "copywriting is a hijack" passage |
| Big Baby Agency Operational Model (section intro) | UNCONFIRMED flag + file-size anchor (67,446 bytes) | Big Baby Agency branding, BigBabyAgency.com, "Marketing Mercenary" 9-week specifics, and the book title are not in transcript.txt — flagged in place |

## Exemplar 4 (Billy Mays) — pre-existing content, flagged not rewritten

`extractions/ron-lynch/transcript.txt` contains no mention of Billy Mays,
Total Trolley, or the quote "very good creative." This is the clearest
provenance gap found in this repair pass. Per the additive-first boundary the
exemplar was not deleted (it may be true and simply outside this single
source file); instead an inline **Provenance flag (UNCONFIRMED)** was added
directly under the exemplar, plus the corresponding row in
`references/source-ledger.md`, so no reader encounters it as verified.

## Files NOT modified (already passing, left untouched per additive-first boundary)

- SKILL.md (recognition_test now satisfied via genius.md — no edit needed; SKILL.md already carried `verbatim_exemplars` and `workflow_contracts` passes and was not touched)
- workflows/*.md (17 files — `workflow_contracts` already PASS; not implicated by any failing check; not copied into this output directory since unchanged)
- references/customer-as-media.md, references/identity-architecture.md, references/prompts-v2/*.md (not implicated by any failing check; not copied)
