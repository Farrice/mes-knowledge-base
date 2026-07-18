# Nicolas Cole — Client Acquisition — Source Ledger

Claim-by-claim provenance for `genius.md` (primarily the Anti-Patterns section added/repaired
2026-07-18) and a status note on the rest of the skill's sourced content.

- **GW1** = `extractions/nicolas-cole-ghostwriting-v1/transcript.txt` — "If I was starting over,
  this would be my 30-day plan to land writing clients ASAP" (Nicolas Cole, single continuous
  transcript, no embedded timestamps). This is the source video behind `extraction-report.md`'s
  Genius Patterns 1, 4, 5, 8 (Removal List, Leaks & Faucets, Free Consulting, Educate Don't Sell)
  even though no transcript file was saved under `extractions/nicolas-cole-client-acquisition/`
  itself — confirmed by direct-quote match, not assumed.
- **GW2** = `extractions/nicolas-cole-ghostwriting-v2/transcript.txt` — "There are five ways that
  you can land ghostwriting clients without needing a portfolio, case studies, or testimonials"
  (Nicolas Cole, single continuous transcript, no embedded timestamps). Source video behind
  Genius Patterns 3, 6, 7 (Power-Leveling/Self-as-Case-Study, NDA Deflection, Pitch in Public).
- **CE** = `extractions/nicolas-cole-client-acquisition/extraction-report.md` — the original
  extraction writeup (no raw transcript saved alongside it); used for pattern framing/wording,
  not as a primary-quote source.
- **CX-2026-07-01** = claude.ai conversation export cited inline at `genius.md` (New Patterns
  9-19 / New Hidden Knowledge section header): "8 Services To Make $10k/Mo As A Writer," "How to
  Make $10k/Month as a Writer," "5 Ways To Make $1 Million As A Writer" Pts 1-2. Pre-existing
  content, not modified in this repair pass; not present under `extractions/` as a re-checkable
  file, so it is not re-verified here (its own header already discloses the MES-embellishment
  discard it went through — see genius.md).

Labels: **VERIFIED** = quote confirmed verbatim (or with only whitespace/filler normalization)
in the cited file. **LIKELY** = concept confirmed in source, wording in the skill is a paraphrase
or elaboration. **UNCONFIRMED** = no anchor found in any `extractions/` file for this expert.

---

## Anti-Patterns (genius.md — repaired this pass, all 7 items)

| # | Anti-Pattern | Status | Anchor |
|---|---|---|---|
| 1 | Chase credentials/portfolio before clients | VERIFIED | GW2 — "The client does not care how much quote unquote industry credibility you have... does not care how big your portfolio is... does not care if you have a gazillion testimonials or one testimonial or zero testimonials. The client doesn't care." |
| 2 | Spray-and-pray outreach | VERIFIED | GW1 — "this is not about spray and prey. This is not about creating a message and copy pasting... They take a high quality approach to outreach. They do not take a spray and pray approach." (transcript spells it "spray and prey" once, "spray and pray" once — both preserved as they appear) |
| 3 | Give up after one follow-up | VERIFIED | GW1 — "they talk themselves out of ever following up... 'Oh, if I follow up, I'm going to be seen as annoying.'... These things are not true. You have made them up... follow up with them in 24 to 48 hour increments at least five times." |
| 4 | Lead with achievements, not the prospect's problem | VERIFIED | GW2 — "your credibility is irrelevant and I can demonstrate credibility much better by articulating your problem in detail... What matters to you is my ability to articulate the problem." |
| 5 | Wait for the "right" forever niche | VERIFIED | GW1 — "This is not your forever niche. This is your first niche... It almost doesn't matter what industry you pick in the beginning. Your goal is I just want a client." |
| 6 | Treat free work as charity | VERIFIED | GW1 — "Don't look at it as free work. Look at it as a marketing cost." |
| 7 | Confuse psychology with reality | VERIFIED | GW1 — "When you're doing something and it's not working, you think you're an idiot... The mentality is what shifts back and forth. The thing that doesn't actually change is the action. And as long as you are doing the right inputs, the outputs take care of themselves." (the Idiot-Genius Roller Coaster) |

## Genius Patterns 1-8 (genius.md — pre-existing, spot-checked this pass, not modified)

Not required by the failing checks (only `anti_patterns_sourced` and `recognition_test` and
`workflow_contracts` failed on this skill), but spot-checked while reading GW1/GW2 for the
anti-pattern anchors above, since these two transcripts turned out to be the actual (previously
uncited-by-file) source:

| # | Pattern | Status | Anchor |
|---|---|---|---|
| 1 | The Removal List | LIKELY | GW1 — the "pull the future forward" / "what am I willing to give up" framing is present verbatim; "removal list" as a named term is the skill's own compression, not Cole's exact phrase in this transcript. |
| 4 | Leaks & Faucets Network Mapping | VERIFIED | GW1 — "I build my list of leaks. I build my list of faucets. I follow up with everyone five times." |
| 6 | The NDA Deflection | VERIFIED | GW2 — "As a ghost writer, the nature of the work that I do... is confidential. So, I'm not uh at liberty to share..." + "one out of a hundred people" pushed back, matching the skill's "99/100." |
| 7 | Pitch in Public | VERIFIED | GW2 — "It's called pitch in public... case studies and testimonials and a portfolio, what are those really trying to achieve? All they're trying to achieve is demonstrating... that you can do what you say you're going to do." |
| 8 | Educate, Don't Sell | VERIFIED | GW2 — "The only thing the client cares about is you educating them on a problem they know they have in their business but haven't gotten around to solving." |

Patterns 2, 3, 5 (Service-First Niching, Power-Leveling/7-Day Guinea Pig, Free Consulting) were
not re-verified line-by-line this pass — extraction-report.md already carries adequate framing
and no failing check required it; flagged here as **not re-checked**, not as UNCONFIRMED.

## New Patterns 9-19 / New Hidden Knowledge (genius.md — untouched this pass)

Status: **not re-verified**. Sourced inline to CX-2026-07-01 (claude.ai export), which is not a
file under `extractions/` and was not re-derivable this pass. Carries its own disclosed caveat
in genius.md ("MES-era embellishments... were checked against the transcripts and discarded").
Left exactly as found — additive-first boundary, no failing check touched this section.

## Not used / not consulted this pass

- `extractions/nicolas-cole-digital-products/transcript.txt`, `extractions/nicolas-cole/transcript.txt`
  — different domain (digital products / offer stacking), out of scope for client-acquisition
  anti-patterns; not searched.
