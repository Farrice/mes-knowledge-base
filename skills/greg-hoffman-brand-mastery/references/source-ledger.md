# Source Ledger — Greg Hoffman: Brand Mastery

> Claim-by-claim provenance for every framework, quote, and named entity used in `genius.md` and `SKILL.md`. Labels: **VERIFIED** (verbatim in a source file, checked by direct grep/read), **LIKELY** (a real concept from the source, restated/named by the extractor rather than quoted verbatim), **UNCONFIRMED** (no source file substantiates it — flagged, not invented).

## Primary Sources Consulted

| Source | Path | Size | Status |
|---|---|---|---|
| Interview transcript, "505 Podcast Ep. 197" (~60 min, per extraction-report metadata) | `extractions/brand-master/transcript.txt` | 108,208 bytes (`wc -c`) | VERIFIED — read in full, all quotes below grepped against this file |
| Extraction report (12 Genius Patterns, 8 Hidden Knowledge items, methodology) | `extractions/brand-master/extraction-report.md` | 21,783 bytes (`wc -c`) | VERIFIED — read in full |
| Codex-harvest duplicate skill (SKILL.md) | `_active/codex-harvest-2026-06-11/skills/greg-hoffman-brand-mastery/SKILL.md` | 4,111 bytes | VERIFIED (checked, content near-identical to live SKILL.md — no new claims found) |
| Codex-harvest AGENT.md (unsourced anti-pattern list) | `_active/codex-harvest-2026-06-11/agents/greg-hoffman/AGENT.md` | 3,487 bytes | VERIFIED as existing, but its own Anti-Patterns list carries no anchors — used only as corroboration, never as an anchor source. All anchors in this skill's genius.md instead trace to the transcript or extraction-report. |
| Book: *Emotion by Design* (Hoffman's book, referenced in SKILL.md intro) | Not present in `extractions/` or `_active/` — no book text file found in repo | **UNCONFIRMED** — the book's existence and authorship is corroborated by the transcript's own introduction ("author of *Emotion by Design*" — not a literal transcript quote, this is host/producer framing, not searched as book content), but no chapter/page-level claim in this skill is sourced FROM the book itself. Any future claim attributed to specific book content must be labeled UNCONFIRMED until the book text is available in-repo. |

## Note on the Transcript File Format
`transcript.txt` is a single unbroken line (no line breaks), so file:line citations are not possible. All anchors below cite the exact verbatim substring instead — each was confirmed present via direct string match against the file at repair time (2026-07-17).

## Claim-by-Claim Ledger

| # | Claim / Quote | Status | Anchor |
|---|---|---|---|
| 1 | "Seen, felt, proven" — Hoffman's own three-word brand definition | VERIFIED | `transcript.txt`: "I use a a three-word principle. Seen, felt, proven." |
| 2 | Seen → Felt → Proven arc definitions (name/symbol → emotional memory → earned value) | VERIFIED | `transcript.txt`: "seen is your brand starts as a name or a symbol... Felt is... creating an emotional memory... proven... the value of your brand is earned through consistent behavior" |
| 3 | Self-Reflection Brand Question ("how people feel about themselves") | VERIFIED | `transcript.txt`: "how do we want people to feel about themselves when they engage with our products and services" |
| 4 | "it's an unselfish question" | VERIFIED | `transcript.txt` verbatim substring |
| 5 | Observation → Insight → POV → Medium → Market chain; Jordan "9,000 missed shots" example | LIKELY | `extraction-report.md` GP-3 — extractor's synthesis of the transcript's storytelling discussion; exact "9,000" figure not independently re-verified against transcript in this repair pass (extraction-report is the anchor, not the raw transcript) |
| 6 | Overground / On-the-Ground / Underground framework, incl. 80% On-the-Ground allocation | VERIFIED (terms) / LIKELY (80% figure) | `transcript.txt` uses "on the ground," "overground," "underground" verbatim (multiple hits); the specific "80%" split is the extractor's paraphrase of Hoffman's budget-allocation discussion, not a verbatim percentage Hoffman states — labeled LIKELY |
| 7 | Innovation Transference — Savile Row, Octavio Campo, hospitality → training app | VERIFIED | `transcript.txt`: "I took my team to Savile Row... on this particular street are the finest suit makers in the world"; "Mexican surrealist painter named Octavio Campo" — both verbatim |
| 8 | 4-Shot Innovation Offense — 4 unbriefed concepts, "one out of four" hit rate | VERIFIED | `transcript.txt`: "create four breakthrough consumer engagement concepts that we weren't briefed... the success rate that we expected was maybe to hit one out of four" |
| 9 | Power of Three (3 distinct concepts per brief) | VERIFIED (term) | `transcript.txt` contains "power of three" (2 hits); specific "fairway of possibility" phrasing and "hundredth logo attempt" framing are extractor synthesis — LIKELY |
| 10 | Lead From the Front / Prefontaine Principle | VERIFIED | `transcript.txt`: "Lead from the front, right?" and "the late great middle distance runner Steve Prefontaine, who always went out first in those races" |
| 11 | Brand as Club — 2-3x repeat purchasing power of members | VERIFIED (concept) | `transcript.txt`: "Members oftent times having two 3x um the repeat purchasing power of anonymous customers" (transcription artifact "oftent times" preserved as spoken) |
| 12 | Partner With Culture, Don't Chase It — Gap × Cats example | VERIFIED | `transcript.txt`: "when I say partner with culture don't chase it that's a that's an example of that"; "collaborating with the musical group cats"; "you're not doing collaboration as a stunt" |
| 13 | Functional Purity — AF1, Levi's 501, Porsche 911, "can't chase cool" | VERIFIED | `transcript.txt`: "you can't chase cool. Like because if you're chasing it, you won't get it"; "None of them were chasing cool. They were born out of trying to create functional excellence" |
| 14 | Evolve Immediately — complacency kills creativity, Lego Ideas platform | VERIFIED (complacency line) / UNCONFIRMED (Lego Ideas) | `transcript.txt`: "complacency and comfort always kills creativity and ingenuity" is verbatim. No mention of "Lego" or "Ideas platform" found anywhere in transcript.txt or extraction-report.md — this specific example is UNCONFIRMED; flagged for removal or re-sourcing in a future pass. |
| 15 | Contrary Truth as Creative Engine — street football campaign | VERIFIED | `transcript.txt`: "first find a truth that's somewhat contrary to the ongoing conversation"; humiliation-of-opponent description present verbatim |
| 16 | Taste is a Trainable Muscle | VERIFIED | `transcript.txt`: "just like you would train a muscle"; "one of the most in-demand jobs over the next one two three years will be the role of a brand creative director" |
| 17 | Humanity Supercharged by Technology — anti-algorithm conviction | VERIFIED | `transcript.txt`: "I absolutely do not believe that the most successful brands in the future will be defined or won by algorithms" (opening line, exact) |
| 18 | Products as Identity Uniforms — "uniform of sport without having to wear it" | VERIFIED | `transcript.txt` verbatim substring |
| 19 | Edition-Based Storytelling — AF1 has no evergreen campaign, only limited editions | LIKELY | Extractor synthesis (`extraction-report.md` HK-8); general AF1-editions discussion present in transcript but the specific "no evergreen campaign" framing is the extractor's phrasing, not a Hoffman quote |
| 20 | Resources don't substitute for permission culture | VERIFIED | `transcript.txt`: "resources don't necessarily make you more innovative or more creative" |
| 21 | Brand-category filter test (gambling app / high-sugar beverage example) | VERIFIED | `transcript.txt`: "...doesn't align with if what I am and what I mean to people that believe in me is someone who is living a high performance lifestyle, shouldn't that act as a filter to everything" (filler words "uh"/stutters trimmed from paraphrase around the verbatim anchor "shouldn't that act as a filter to everything") |
| 22 | Author of *Emotion by Design*, former Global CMO of Nike, "nearly 30 years" / "27 years" tenure | LIKELY | `transcript.txt` intro states "for nearly 30 years"; SKILL.md's "27-year" figure comes from `extraction-report.md` Content Assessment block ("27 years") — the two sources use different round numbers; both plausible, neither independently verified against an external bio, so treated as LIKELY not VERIFIED |

## Honest Gaps
- No specific air date for the "505 Podcast Ep. 197" episode was found in either source file — any date-stamped citation of this interview should read "undated per available source" rather than inventing a publish date.
- The Anti-Patterns list in `_active/codex-harvest-2026-06-11/agents/greg-hoffman/AGENT.md` names the same failure modes this ledger sources independently, but that file itself carries zero anchors — it was NOT used as a source-of-record for any anchor in genius.md, only as directional confirmation that the pattern names are stable across the two extraction lineages.
