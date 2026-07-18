# Dai Media — Consumer Posture Framework — Source Ledger

Claim-by-claim provenance for `genius.md` (and its condensed twin,
`references/genius-patterns.md` / `references/hidden-knowledge.md`, which
carry the same 14 Patterns / 5 Tacit Knowledge items in shorter form).

## Primary source

- **EXT** = `knowledge/extractions/inbox/Claude-💎💎💎💡 Dai Media !
  Identity Persona Mastery ! demographics are dumb and outdated.md`
  (482,651 bytes, 9,792 lines) — a Claude.ai chat export dated 1/6/2026,
  the MES 3.0 `/architect-enhanced` extraction session that produced this
  skill. Confirmed by `agents/dai-media/AGENT.md` line 156: "Source: Dai
  Media MES 3.0 Extraction (Parts 1-2)." This file contains the full
  Content Assessment ("Video Transcript - Brand Strategy Masterclass,
  ~12 min"), the 14 Genius Patterns, the 5 Tacit Knowledge points, and
  the Crown Jewel practitioner-prompt examples (MATTE & CO, Meridian
  Electronics) that genius.md draws worked examples from.
- **EXT2** = the companion file `...outdated pt.2.md` (318,967 bytes,
  6,374 lines) — read in full; searched for "Solitude Journeys," "Gadget
  X," "Hall of Fame," "Signature Moves," and "Quality Rubric." Zero
  matches.

**Important scope note**: neither `EXT` nor `EXT2` lives under
`extractions/` (the canonical location named in the repair envelope) —
`ls extractions/ | grep -i dai` returns nothing. `EXT`/`EXT2` live under
`knowledge/extractions/inbox/`, the pre-triage inbox. This is the
skill's real, verifiable origin (matches `agents/dai-media/AGENT.md`
verbatim), so it is used here as ground truth rather than inventing a
different source or declaring the skill unsourceable. The raw underlying
video transcript itself is NOT present in `EXT`/`EXT2` — the export shows
only `> File: ` with the attachment content stripped. Everything in `EXT`
is Claude's own extraction analysis of that (unpreserved) video, written
in its own words rather than verbatim transcript excerpts. Where `EXT`
itself uses quotation marks around a phrase (e.g. "by the tail," "cool
shit," "we don't need your attention. We're not thirsty"), those are
presented in `EXT` as Dai's own words and are treated as VERIFIED against
`EXT` — but note this is one level removed from the primary video, not a
timestamped transcript.

Labels: **VERIFIED** = text in `genius.md` matches `EXT` verbatim or
near-verbatim (confirmed via `grep -F`/`grep -n`, cited by line number
above). **LIKELY** = the underlying pattern/mechanic is confirmed in
`EXT`, but the specific worked example, narrative wrapper, or scoring
language in `genius.md` is a later elaboration built on top of the
verified pattern, not itself present in `EXT`. **UNCONFIRMED** = no
anchor found in `EXT`, `EXT2`, or any other `extractions/`-adjacent file
matching "dai."

---

## Genius Patterns 1-14

| # | Pattern | Status | Anchor |
|---|---------|--------|--------|
| 1 | The Living Brand Metaphor | VERIFIED | EXT line 151: "Dai consistently frames brands as living organisms with heartbeats, weather systems, and environmental conditions." Worked example (Meridian Electronics, "47-year-old organism," "CRAFT EXCELLENCE IN SOUND" heartbeat, "ARRHYTHMIC" status) VERIFIED at EXT lines 3820, 3833, 3835. |
| 2 | Individual Before Community Inversion | VERIFIED | EXT line 164: "When tempted to describe your consumer as 'people who...' or 'the community that...', stop." Reinforced at line 7383. |
| 3 | The Kristen Stewart Test | VERIFIED | EXT lines 173-175: "When studio execs used demographics to define gay identity to an actual gay woman, it revealed the absurdity of category-based thinking... If an actual gay woman wouldn't recognize the demographic portrait of a gay woman, the portrait is worthless." |
| 4 | Consumer Posture Architecture (Occupation/Activity/Thought Process) | VERIFIED | EXT lines 176-180 (extraction-report Pattern 4). Worked example (MATTE & CO / Sara, "the only time in her day when nothing is optimized") VERIFIED at EXT line 691. |
| 5 | The Row Reverse-Engineering Method | VERIFIED | EXT lines 190-195 (extraction-report Pattern 5). |
| 6 | The "No Phone Policy" Principle | VERIFIED | EXT line 209: "Dai identifies that The Row's physical policies (no phones in stores, no phones at runway shows) are consumer education disguised as rules." |
| 7 | Emotional Outcome Over Problem-Solution | VERIFIED | EXT line 222: "reject functional explanations ('they need clothes') in favor of emotional outcomes ('they want to feel unreachably polished and mysteriously withdrawn')." |
| 8 | The Trend-Hopper Rejection Filter | VERIFIED | EXT line 233: "Is this person trend-hopping, or is this how they fundamentally see themselves? Only individuals in the second category are worth building a brand around." |
| 9 | The Groupthink Diagnosis | VERIFIED | EXT line 244: "Before any strategic decision driven by 'what I see happening online,' pause." |
| 10 | The Algorithm Mirror Inversion | VERIFIED | EXT line 253-255 (extraction-report Pattern 10: brands should predict resonance "like an algorithm, but for identity rather than engagement"). |
| 11 | The Stunned Brand Owner Test | VERIFIED | EXT lines 261-266 (extraction-report Pattern 11) + EXT line 1211 (Crown Jewel #3 prompt): "most brand owners are stunned into silence when asked specific questions... they go blank." |
| 12 | The "By The Tail" Methodology | VERIFIED | EXT lines 274-275: consumer understanding gives you the consumer "by the tail"—"total strategic control because you can predict and lead behavior." |
| 13 | The Content Impossibility Diagnosis | VERIFIED | EXT line 288: "When stuck on content, never ask 'What content should I make?' Instead ask 'What does my individual consumer think about this topic?'" |
| 14 | The Analog Identity Marker | VERIFIED | EXT line 297: "Dai identifies that The Row's consumer is 'analog'—not obsessed with phones and social media—and this single insight explains their entire social media strategy." |

## Tacit Knowledge 1-5

| # | Item | Status | Anchor |
|---|------|--------|--------|
| 1 | Demographics Are Performance Metrics, Not Consumer Truth | VERIFIED | EXT line 310: "demographics are useful only for media buying and ad targeting efficiency—they tell you where to place ads, not who you're speaking to." |
| 2 | The Row Doesn't Have Customers—They Have Co-Conspirators | VERIFIED | EXT line 317: "'private, withdrawn, separate, operating outside the feed'... The Row and their consumers are conspiring together against noise, overexposure, and trend-chasing." |
| 3 | The Consumer Is Waiting to Be Articulated | VERIFIED | EXT §"Tacit Knowledge 3" (extraction-report): "consumers are 'waiting for somebody to express what they can't say.'" |
| 4 | Brand World Design Precedes Brand Marketing | VERIFIED | EXT §"Tacit Knowledge 4": "The Row doesn't market to consumers—they design a world, and consumers enter it." |
| 5 | Socials Can Be Anti-Social | VERIFIED | EXT lines 338, 340: "'cool shit'... 'We don't need your attention. We're not thirsty.'... Desperate? Thirsty? Trying to hard?" (genius.md corrects the source's typo "Trying to hard" → "Trying too hard.") |

## Hall of Fame Exemplars

| Exemplar | Status | Notes |
|---|---|---|
| 1. The Row | LIKELY | The underlying facts genuinely quoted inside the "Dai Media Analysis" paragraph ("private, withdrawn, separate, operating outside the feed"; Tacit 2/3/4/5 callouts) are VERIFIED against EXT (see Tacit Knowledge table above). The connective analysis prose itself ("Their success is a masterclass in designing a world...") is not a verbatim EXT passage — it is a later synthesis built on top of verified tacit knowledge. Not fabricated (every factual claim traces to a VERIFIED item), but the exemplar-writeup format is downstream elaboration, not primary source. |
| 2. Solitude Journeys | UNCONFIRMED (as a named company) | Searched EXT and EXT2 for "Solitude Journeys" — zero matches. This is a constructed illustrative example, not a company Dai discussed. The *pattern application* it demonstrates (Pattern 6 "No Phone Policy," Pattern 7 "Emotional Outcome") is independently VERIFIED — see those rows above — but the specific company and its details ("digital detox... no-phone zones," "booking interview") are Claude's invention for illustration, not sourced fact. Left in place per additive-first boundary; flagged here rather than silently presented as a real case study. |
| Anti-Exemplar: "Gadget X" | UNCONFIRMED (as a named company) | Searched EXT and EXT2 for "Gadget X" — zero matches. Constructed illustrative counter-example; the pattern-violation logic it demonstrates (Patterns 3, 7, 8, 9, 13 + Tacit 1) is independently VERIFIED, the specific brand is not real. |

## Signature Moves

All 5 Signature Moves restate a Genius Pattern or Tacit Knowledge item already tabled above and inherit that item's status:

| Move | Restates | Status |
|---|---|---|
| "Who is Kristen Stewart?" Pre-Mortem | Pattern 3 | VERIFIED |
| "Brand as Organism" Unpacking | Pattern 1 | VERIFIED |
| "Co-Conspirator Call-Out" | Tacit Knowledge 2 | VERIFIED |
| "Inverse Consumer Revelation" | Pattern 11 | VERIFIED |
| "Unarticulated Feeling" Probe | Tacit Knowledge 3 | VERIFIED |

## Expert-Specific Quality Rubric

**LIKELY** — every row measures a VERIFIED Pattern (Individual Posture
Articulation → Patterns 2-3; Emotional Outcome Clarity → Pattern 7;
Predictive Power → Pattern 12; Trend-Resistance → Pattern 8; Inverse
Psychology Depth → Pattern 11; Brand World Coherence → Tacit 4;
Unarticulated Identity Resonance → Tacit 3), but the 4/7/10 scoring
language and column structure itself is a rubric construction, not
verbatim EXT text. Concept fully grounded, exact wording is elaboration.

## Anti-Patterns (genius.md, new section — 8 items)

All 8 items VERIFIED against EXT — see inline citations in `genius.md` §
Anti-Patterns for the exact quote + line number per item. Every quote was
re-checked with `grep -n` against the live file at the cited line before
being written into genius.md.

## How to Use This Skill (Model Calibration)

New section — editorial/methodological framing for the model, not a
factual claim about Dai Media requiring its own VERIFIED/LIKELY label.
Every specific example it references (MATTE & CO / Sara, the
demographic-vs-psychographic distinction) is independently VERIFIED
above (Pattern 4, Tacit Knowledge 1).

## Not used / not consulted

- No file under `extractions/` matches "dai" (`ls extractions/ | grep -i
  dai` returns nothing) — confirmed before falling back to
  `knowledge/extractions/inbox/`.
- `research_outputs/ai_authority_architect_agents/dai_media.md` — a
  DIFFERENT artifact (an ICP/avatar-profile output built using the Dai
  Media framework, not a source of Dai's own patterns). Not drawn on for
  this ledger; it's downstream application, not upstream provenance.
- `evolution_store/v2_variants/genius_compressed/dai-media-consumer-posture_genius.md`
  and `swarm_outputs/20260306_183945/agent_outputs/dai-media.md` — build
  artifacts from prior pipeline runs, not primary source; not consulted.
