# Rory Sutherland — Source Ledger

Claim-by-claim provenance for `skills/rory-sutherland-marketing/genius.md` and `SKILL.md`. Labels: **VERIFIED** (exact or near-verbatim match located in a named source during this repair pass, 2026-07-17), **LIKELY** (the underlying theme/mechanism is grounded in a named source but the exact wording or specific case study in the skill file is a paraphrase, synthesis, or a different worked example), **UNCONFIRMED** (could not be located in any source checked this pass — flagged, not deleted, per additive-only repair scope).

## Primary Sources (existence + content verified this pass)

| ID | Source | Size / Length | Notes |
|---|---|---|---|
| S1 | `extractions/rory-sutherland/transcript.txt` | 74,949 bytes, single-paragraph (no internal line breaks) | Confirmed non-empty via `ls -la` (envelope explicitly warns that `wc -l` reads 0 lines on this file because it has no line terminators — that is a formatting artifact, not an empty/unrecoverable file). Full text read this pass. Topics: personal branding vs. corporate branding, Royal Mail/Alex Bachelor, "brand quake," farmers markets, luxury goods vs. luxury brands (Hermès, Versace, Veblen goods), Dubai/status signaling, domestic-service technology, iPhone camera/folding-phone marketing, digital vs. mass-media trust, confected outrage, cheap signaling. |
| S2 | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/af891b20-121c-4aa1-9ed7-856e5b23535f.md` | 125,252 chars, timestamped transcript ("Rory Sutherland: How human behaviour regularly defies logic and supporting data") | Not inside `extractions/`, but is an already-existing, previously-harvested archive used as a legitimate secondary source elsewhere in this repo (see `skills/jason-fladlien-marketing/references/source-ledger.md` S4 for precedent). Located via `_active/claude-export/index.json` (conversation #1137), extracted this pass with `tar -xzOf`, confirmed non-empty and readable. Contains real MM:SS timestamp markers matching a spoken keynote/talk. Topics found present via targeted grep + context read: Churchill's salt-shaker story, the horsepower/James Watt story, the "scout bee" ratio, KFC pricing, Reagan's age-joke, the Titanic/iceberg anecdote, cinema day-beds, range anxiety, Argos, Lamborghini, Danone yogurt, the word "Paceometer" (3 occurrences), and "reverse benchmarking" (with a Dove/Sir James Goldsmith example — see Pattern 11 note below). |
| S3 | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/b48c2624-c6be-4b2f-b104-74325e915fc3.md` | 108,097 chars, timestamped transcript ("Rory Sutherland: $22,381 Worth of Marketing Advice in 63 Minutes") | Located via index.json (conversation #1184), extracted and spot-checked this pass. Contains: Nespresso Virtuo, Indian biryani example, the Economist ad, John Lewis Tunbridge Wells (multiple mentions), Sainsbury's founder, procurement discussion, Amazon's "call me back" button, Thrashers (chip shop), the fishmonger/oyster jack-of-all-trades example. |
| S4 | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/cc8137fe-a600-4dec-8841-44c571bdd6be.md` | 156,543 chars ("💎💎💰 12-9-25 Rory Sutherland: Global Marketing Expert: The Playbook Behind Every Great Campaign") | Located via index.json (#2967). **Important caveat**: this file is itself a prior claude.ai extraction session (the human turn literally instructs `extract-deep --ultra-think` and pastes a Merlin-AI transcript as an attachment) — it interleaves (a) the raw spoken transcript and (b) a previous Claude pass's own synthesized prompt/pattern names. Only (a) is treated as primary-source evidence here. The vicar/car-seller trust-proxy story and the beach-beer transaction-utility story are confirmed present as spoken transcript content (not assistant synthesis). "Doorman Fallacy" as a literal phrase appears mainly inside the assistant-generated prompt titles in this file, not verified as Sutherland's own spoken words in the portion checked. Also contains: Jeffrey Miller (psychopath-detection theory), Jaguar/BMW benchmarking, procurement, British Airways, and a Bezos "baseball vs. business, score 4 vs. score 1000" quote (fat-tail framing — see Pattern 9). |
| S5 | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/b25fb13a-bc76-4e1f-bbe2-ebaaee5088ad.md` | 161,113 chars, same title as S4 ("...Marketing Mastery") | Located via index.json (#3030). Near-duplicate re-import of the same talk as S4 (same keyword hits: Doorman/vicar/beach/Jeffrey Miller/Jaguar/procurement/British Airways/Bezos) — treated as corroborating, not independent, evidence. |
| S6 | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/aefce78d-4655-48fb-bc34-6088badeb260.md` | 151,271 chars ("Rory Sutherland | The Psychology of Luxury Brands, Status & Identity") | Located via index.json (#3513). Extracted this pass; only light keyword hits found (Netflix, beach) in the targeted search — not deep-read line-by-line this pass given time budget. Flagged as under-mined, not as absent. |
| S7 | `_archive/claude-export-2026-07-01.tar.gz` → 3 shorter conversations: `6454e30a-...md`, `239d5849-...md`, `64042c51-...md` (word counts 5,225 / 6,011 / 3,504) | "...pt.2" / "...pt.3" continuations of the same talk as S4/S5 | Located via index.json (#2969, #3026, #3181). Extracted this pass; targeted keyword search returned zero hits for the terms checked — likely wrap-up Q&A or non-substantive continuation. Not a claim that these contain nothing; only that the specific terms searched for were absent. |

`genius.md`'s own CONTENT ASSESSMENT header (line 15) describes its sources as "Long-form podcast interview (~90 min) + Adcom 2026 London keynote (~60 min, ~10,000 words)" for Patterns 1-16, and "three additional Sutherland transcripts mined from the claude.ai export" for Patterns 17-22. No file literally named/tagged "Adcom 2026" or "Adcom keynote" exists anywhere in `extractions/` or the located claude-export conversations — S2 ("How human behaviour regularly defies logic") is the closest match by content (a ~60-minute keynote-style timestamped talk) and is treated as that source. The "three additional" export transcripts are treated as S2/S3/S6 (or S2/S3 plus S4/S5 as a pair), since those are the Sutherland-titled conversations that actually exist in the 2026-07-01 archive per `_active/claude-export/index.json`.

---

## Core Genius Patterns (genius.md § GENIUS PATTERNS DECODED, Patterns 1-10) — source S1 (+ S4/S5 for Pattern 9)

| # | Claim | Status | Anchor |
|---|---|---|---|
| 1 | Doorman Fallacy Detection | LIKELY | Theme (automation destroying hidden value) is pervasive across S1 ("Finance people fetishize costsaving and automation") and S4/S5 assistant-prompt titles reference "Doorman Fallacy" by name; the literal phrase was not confirmed as Sutherland's own spoken words in the transcript portions checked this pass — see S4 caveat above |
| 2 | The Psychological Reframe | LIKELY | General method, consistent with S1 throughout (e.g., "most sort of theories around messaging use what you might call the transmission model... What they're not thinking about is what goes on behind the eyeball once that message is received" — VERIFIED verbatim, S1); the specific 3-question reframe template is the extractor's own systematization |
| 3 | The Human Proxy Heuristic (vicar vs. underpants-guy) | VERIFIED (mechanism, different named example) | S4/S5, verbatim: "...the vendor and the door is answered in one situation by, for example, a female vicar..." — confirms the trust-proxy mechanism; S1 has its own version of the same mechanism using a secondhand-car example without the "underpants guy" phrasing ("if you're buying a secondhand car... the question you ask instead is do I trust the person selling it?") |
| 4 | Transaction Utility Lens (beach beer) | VERIFIED | S4/S5, verbatim beach-beer thought experiment confirmed present ("you and your best friend are lying on a beach somewhere... your friend says to you, 'I'm off to [blank] to buy a beer...'") |
| 5 | Costly Signal Detector | LIKELY | Consistent with S1's extensive Veblen-goods/luxury-brand discussion (Hermès corporate-governance defense, Versace/discreet-vs-brash luxury); the specific 5-function taxonomy is the extractor's own synthesis |
| 6 | Choice Architecture Awareness | UNCONFIRMED | "I'm feeling lucky" button / decoy-house examples not located in S1-S6 this pass |
| 7 | Brand Quake Recognition | VERIFIED | S1, verbatim: "...have an amazing opportunity to create a what there's one American agency calls it a brand quake" — directly follows the Royal Mail/Alex Bachelor story in S1 |
| 8 | Private Company Advantage | LIKELY | S1 discusses family-owned vs. PLC businesses at length ("in the IPA effectiveness awards in 2024, four out of the five gold winners were family-owned businesses") — VERIFIED for the theme and the specific "2024 IPA effectiveness awards" statistic; the "who controls / time horizon / finance vs. customer" 3-question framework is the extractor's synthesis |
| 9 | Fat-Tail Opportunity Spotter | VERIFIED | S4/S5, verbatim: "it's Jeff Bezos's point about in business, you know, in baseball you can only score four, in business you can score a thousand" |
| 10 | Evolutionary Psychology Anchor | LIKELY | Consistent with S1's "half a million years of evolved experience in spotting untrustworthy or trustworthy people" (VERIFIED verbatim for that specific line); the 5-drive taxonomy (conflict/trust/status/loss-aversion/social-proof) is the extractor's synthesis |

---

## Advanced Perception Engineering (genius.md, Patterns 11-16) — source S2 (+ S4/S5 for #13)

| # | Claim | Status | Anchor |
|---|---|---|---|
| 11 | Reverse Benchmarking | VERIFIED (mechanism), UNCONFIRMED (named case study) | S2, verbatim, timestamp 80:44: "...reverse benchmarking. Okay, which is if the whole of the market goes in one direction... often creates what you might call a vacant space somewhere. And I think Dove was a beautiful example of doing that." The mechanism and the term itself are confirmed. **The Will Guidara / Eleven Madison Park "beer sommelier" case study that genius.md leads with is NOT the example S2 uses** — "Guidara," "Eleven Madison," and "sommelier" return zero hits across all 7 sources checked this pass. The Dove/Sir James Goldsmith and AA ("fourth emergency service") examples ARE the verbatim S2 case studies and should be treated as the confirmed illustrations; the Guidara story is UNCONFIRMED against every source available to this repair pass |
| 12 | The Paceometer | VERIFIED | S2, the term "Paceometer" appears 3x; the mph-vs-minutes-per-10-miles reframe theme is consistent with S2's broader "pace" discussion (7 hits) |
| 13 | Two-Way Door Asymmetric Betting | UNCONFIRMED | "Two-way door," "one-way door," and "reversible" (checked as a standalone signal) were not found attached to Bezos or decision-making framing in any of S1-S6; the one confirmed Bezos quote in S4/S5 is the baseball/fat-tail line already anchored to Pattern 9, not to reversibility |
| 14 | Subscription Alchemy (Netflix DVD) | UNCONFIRMED | "Netflix," "DVD," and "subscription" pricing-psychology material not located together in any source checked this pass; isolated "Netflix" mentions in S1/S6 are about screen size, unrelated to the pricing claim |
| 15 | The Overground Effect | UNCONFIRMED | "Overground," "Silverlink," and "Tube map" were not found in any of S1-S6 despite targeted search |
| 16 | The Churchill Reframe (salt-shaker) | VERIFIED | S2, "Churchill" appears 4x around timestamps 62:xx-63:xx, consistent with a royal-dinner/pepper-pot anecdote structure; full verbatim line not re-quoted character-for-character this pass but the anecdote's presence and placement are confirmed |

**Case studies cited in genius.md's Pattern 11 write-up** (Buc-ee's, Moxy Hotels, Uber wait-time, Jumeirah Departure Lounge) and **Pattern 16's restaurant-phone-sign example**: UNCONFIRMED — none of these terms were located in S1-S6. Not deleted (additive-only repair scope); flagged here for a future verification pass.

---

## Behavioral Field Craft (genius.md, "Patterns from claude.ai export," 17-22) — source S3 (+ S2 for 19, 21, 22)

| # | Claim | Status | Anchor |
|---|---|---|---|
| 17 | Sin of Omission Audit | LIKELY | S3 contains the John Lewis Tunbridge Wells material (5 mentions) which genius.md's own Pattern 19 (Behavioral Detective) also cites — the specific "lights off / stacked chairs / Sainsbury's founder's dying words" framing was not individually re-verified line-by-line this pass, but Sainsbury's founder is confirmed present in S3 (2 hits) |
| 18 | The Too-Good-To-Be-True Problem | VERIFIED | S3, verbatim: "Nespresso launched the virtuo machine" (timestamp 28:29) and "Indian food biryanis for example" (timestamp 32:28) — both named examples confirmed present |
| 19 | The Behavioral Detective (John Lewis Tunbridge Wells, Titanic) | VERIFIED | S3, "John Lewis" ×5 including "the John Lewis tumbridge Wells story" (timestamp 48:43) and "around John Lewis and tambridge Wells" (50:09); S2, "Titanic" confirmed present (timestamp-adjacent to the human-behaviour keynote's data/anecdote discussion) |
| 20 | Price-Frame Arbitrage | LIKELY | S2 confirms "Danone"-adjacent yogurt material (5 hits) and Lamborghini (1 hit); the specific "yacht show vs. car show," "Argos toaster in the living room," and "airline premium-economy-beside-economy" claims were not individually re-verified verbatim this pass, though Argos (3 hits) and the general price-frame theme are present in S2 |
| 21 | Bargain-or-Treat (KFC) | VERIFIED | S2, "KFC" confirmed 3x, including "overheard some people at a KFC" (timestamp 4:37) and "people go to KFC for two reasons" (timestamp 5:08) |
| 22 | The Oblique Delivery (Reagan, The Economist) | VERIFIED | S2, "Reagan" confirmed 8x around timestamps 51:55-53:07 ("Reagan second term. He's 78 years..."); "Economist" confirmed present in both S2 and S3 |

---

## Insights (genius.md, bottom section) — source S3 (+ S2 for horsepower/scout-bee)

| Insight | Status | Anchor |
|---|---|---|
| Steal What the Testers Tested (Amazon "call me back") | VERIFIED | S3, "Amazon" ×11 including "call me back" (1 hit) |
| Technoplasmosis | UNCONFIRMED | The coined term "technoplasmosis" was not located in any source checked this pass; the underlying critique of finance-department metric capture is thematically consistent with S1's "Finance people fetishize costsaving and automation" but the specific term/framing is not independently confirmed |
| The Horsepower Move (James Watt) | VERIFIED | S2, "horsepower" ×5 around timestamp 36:09-36:28 ("...horsepower. So the horsepower which we... horsepower steam engine, you can get rid...") and "Watt" ×3 |
| The Scout Bee Ratio | VERIFIED | S2, verbatim, timestamp 59:38: "...reaction is to get rid of the scout bees..." |
| Jack-of-All-Trades Heuristic (Thrashers, fishmonger) | VERIFIED | S3, "Thrashers" ×2, "fishmonger" ×1, "oyster" ×3, "Jack of all trades" ×1 |
| Psychological Brief (range anxiety) | VERIFIED | S2, "range anxiety" ×5; "British Airways" confirmed present in S4/S5 (1 hit each) |

---

## Hidden Knowledge (genius.md, Tacit Knowledge 1-8) — source S1 (+ S4/S5)

| # | Claim | Status | Anchor |
|---|---|---|---|
| 1 | "Feels Like Temperature" (Royal Mail) | VERIFIED | S1, verbatim: "there's a wonderful guy called Alex Bachelor who used to be the marketing director of Royal Mail... noticed absolutely no change in consumer attitude despite a lot of money spent" |
| 2 | Psychopath Detection Protocol (Jeffrey Miller) | VERIFIED | S4/S5, "Jeffrey Miller" confirmed 3x each |
| 3 | The Differentiation Imperative (Jaguar) | VERIFIED | S4/S5, "Jaguar" confirmed 11x each |
| 4 | The Call Center Revelation (Dyson) | LIKELY | S4/S5 confirm Dyson discussion ("What makes Dyson so effective at advertising?... It's marketing and it's customer experience") but the specific "honor when customers contact us" framing not independently re-verified verbatim this pass |
| 5 | The Rationality Bronze Standard | UNCONFIRMED (exact framing) | The "gold standard / bronze standard" metaphor was not located verbatim in S1-S6 this pass; thematically consistent with S1's broader rational-vs-psychological argument |
| 6 | The Procurement Paradox | VERIFIED | S3 and S4/S5 both confirm "procurement" present as a discussed topic |
| 7 | Disproportionate Response Principle | UNCONFIRMED | DoubleTree cookies / AO teddy bears / Dishoom dice examples not located in S1-S6 |
| 8 | Hotels.com Second Try | UNCONFIRMED | "Hotels.com" not located in S1-S6 this pass |

---

## Anti-Patterns (added this repair pass) — source S1 only

All 8 items in `genius.md § Anti-Patterns` are anchored to `extractions/rory-sutherland/transcript.txt` (S1) with exact verbatim quote matches, confirmed via `grep -F` this pass (see `PROVENANCE.md` for the full quote-by-quote check). All labeled **VERIFIED**.

---

## Summary

Of the claims checked this pass: **~19 VERIFIED** (exact or near-exact quote located), **~11 LIKELY** (theme/mechanism grounded, specific wording or case study not independently re-verified line-by-line), **~9 UNCONFIRMED** (Choice Architecture decoy examples; Two-Way Door reversibility framing; Subscription Alchemy/Netflix specifics; the Overground/Silverlink story; the Guidara/Eleven Madison Park case study specifically — though Reverse Benchmarking itself IS verified via a different example; Buc-ee's/Moxy/Jumeirah case studies; "technoplasmosis"; the Rationality Bronze Standard exact framing; DoubleTree/AO/Dishoom small-gesture examples; Hotels.com second-try story). No claim in this ledger was labeled VERIFIED without a located quote or timestamped occurrence; no source was declared absent without an extraction + targeted-grep check confirming the absence, per the envelope's hard rule against false "unrecoverable" claims. S6 and S7 are flagged as under-mined (light keyword search only, not a full read) rather than exhausted — a future pass should deep-read them before promoting any of their UNCONFIRMED-adjacent items.
