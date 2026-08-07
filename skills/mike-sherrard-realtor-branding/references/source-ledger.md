# Mike Sherrard — Source Ledger

Claim-by-claim provenance for `genius.md`. Labels: **VERIFIED** (verbatim or
near-verbatim in a source transcript, transcription artifacts aside),
**LIKELY** (source-consistent synthesis/execution-layer construction with no
single verbatim anchor), **UNCONFIRMED** (no supporting text found in any
source file located this pass — none exist in this ledger; flagged here as a
standing instruction for future passes).

## Sources Consulted

Ground truth = two YouTube-transcript conversations pulled from
`_archive/claude-export-2026-07-01.tar.gz` (confirmed present via
`python3 -m tarfile`/`tarfile` per-member scan on conversation IDs named in
`_active/harness/claude-export/harvest/gap3-input.json`, which lists exactly these two
`.mds` for `skill: mike-sherrard-realtor-branding`). Both extracted to the
repair scratchpad and read in full this session; sizes below are `wc -c` on
the extracted files, matching the tarfile member sizes exactly (no
truncation).

| ID | File (as cited in this ledger) | Size | Title | Captured |
|----|------|------|------|------|
| S1 | `90pct-zero-leads.md` (tar member `claude-export/normalized/conversations/1804507d-a25e-415b-916b-1b04822b03cd.md`) | 32,129 bytes | "Mike Sherrard: Why 90% of Realtors Get ZERO Leads From Social Media (How to Fix it FAST)" | 2025-06-20 |
| S2 | `hormozi-25k-branding.md` (tar member `claude-export/normalized/conversations/327fae11-77f5-4cae-9a5a-6f10a08639e5.md`) | 42,523 bytes | "10-29-25 Mike Sherrard: REVEALING Alex Hormozi's $25,000 Personal Branding Strategy for Real Estate Agents" | 2025-10-29 |

Both files are the raw Merlin-AI YouTube transcript (timestamped, verbatim
speech-to-text) plus the human's `/extract-deep` prompts and the assistant's
own meta-commentary about building extraction artifacts. **The actual
MES-framework extraction artifacts referenced in the assistant turns were
never captured in the export** — every artifact-creation turn is a stub
("Viewing artifacts created via the Analysis Tool web feature preview isn't
yet supported on mobile"). This means `skills/mike-sherrard-realtor-branding/`
was built directly from the raw transcripts (or a prior pass's reading of
them), not from a lost intermediate extraction-report file — there is no
missing extraction-report.md to search for; the transcripts themselves are
the only ground truth, and they are intact, non-empty, and readable.

No `extractions/` directory exists for this expert (`ls extractions/ | grep -i
sherrard` returns nothing) — this is expected and not a gap; the source lives
in the claude-export archive, not the extractions/ tree, consistent with the
`source: claude.ai export 2026-07-01` frontmatter tag already on `SKILL.md`.

## Claims — genius.md, Genius Patterns (1–10)

| Claim | Label | Anchor |
|---|---|---|
| Message Before Microphone — "your brand is the messaging. The marketing is the microphone... a whole lot of nothing to a whole lot of people" | VERIFIED | S2 timestamp 6:25–6:37 (verbatim, near-exact including the "whole lot of nothing" phrase). |
| Four-Criteria Niche Test — pain/purchasing power/targetability/growth, first-time-buyer worked example | VERIFIED | S2 timestamp 7:24–10:19 (all four criteria named and applied to first-time buyers with identical figures: $300–600K range, 25–35 renters, "how to buy a home," millennials + Gen Z over 50% of new mortgages). |
| The No-One Audience — three circles, "connecting with no one," neurosurgeon vs. general practitioner | VERIFIED | S2 timestamp 17:01–18:53 (verbatim "connecting with no one"; neurosurgeon/GP comparison at 18:42–18:49). |
| Local Resource for the 99% — restaurants, events, "things to do," relocation content | VERIFIED | S1 timestamp 2:53–3:43 (verbatim "restaurants... local events... things to do... sharable with the general public"). |
| Facts Tell, Stories Sell — Control the Narrative — "rates hit 6.8%," buyer/seller translation, client-panic story | VERIFIED | S1 timestamp 3:55–6:00 (verbatim story example: "My client panicked over the rates. Here's how we got creative."; "market is always going to be good for somebody"). |
| Short Interest Span, Not Attention Span — HVC framework, fear/misconception hooks | VERIFIED | S1 timestamp 7:19–10:08 (verbatim "short interest span" reframe; HVC breakdown). Fear/misconception hook examples cross-verified against S2 timestamp 12:54–14:00. |
| The First-Three-Photos Identity Test — mom's dream car, terminal-cancer kid + Lamborghini, Hawaii | VERIFIED | S1 timestamp 11:00–12:02 (verbatim: all three photo examples present in that exact order). |
| The Bouquet — Packaged Associations — six-flower analogy, partner list | VERIFIED | S2 timestamp 14:53–16:00 (verbatim bouquet analogy; partner list — moving companies, title, mortgage reps, credit repair, insurance, utility setup, home warranty, inspectors, contractors, home decor — matches nearly word for word). |
| Cross-Platform Consistency as an Algorithm Signal — ChatGPT/Google recommendation criteria | VERIFIED | S2 timestamp 19:57–20:11 (verbatim: "if you want to artificial intelligence like Chat GBT and Google to recommend you, they look for consistency across all platforms and a strong brand. It's one of the top criterias they look for." — "Chat GBT" is the transcript's own speech-to-text artifact for ChatGPT). |
| Invest in the Name — You Only Get One — "you only get one name," ~7 deals LTV | VERIFIED | S2 timestamp 1:16–1:20 (verbatim "you only get one name. So, invest accordingly.") and 3:14–3:18 (verbatim "approximately seven deals over the lifespan of your career"). |

## Claims — genius.md, Hidden Knowledge (1–5)

| Claim | Label | Anchor |
|---|---|---|
| The Realtor-Follower Diagnostic — agent-heavy followers as a targeting confession | VERIFIED (core claim) / LIKELY (the "confession" framing and "compounding" mechanism) | S1 timestamp 1:04–1:24 (verbatim: "the only other people that are following them are other realtors... it's catered toward what other agents would want to engage with"). The algorithmic-compounding explanation is the extraction layer's synthesis of S1's engagement-signal logic (1:57–2:14), not a separate Sherrard quote — LIKELY. |
| The Capture Asset Is the Missing Link, Not the Content — lead magnets + keyword DM automation | VERIFIED | S1 timestamp 13:38–16:05 (ManyChat keyword-DM mechanic, verbatim examples "comment the word buy," "DM me the word event"; YouTube description-link and lead-magnet mechanic at 14:44–16:05). |
| Fear Outconverts Aspiration in Hooks — "mistakes to avoid," pain > pleasure | VERIFIED | S2 timestamp 12:54–13:51 (verbatim "don't make these three mistakes. It'll cost you thousands of dollars"; "fear-based curiosity") and 13:39–14:53 (verbatim "people want to run away... from pain more than they want to run toward pleasure... highest click-through rate"). |
| Educational Search Content Is Niche Targeting — search-phrase list as content calendar | VERIFIED | S2 timestamp 11:31–12:04 (verbatim list: "how much can I afford," "how to buy a home with little to[e] no money down," "first-time home buyer mistakes to avoid," "rent versus buy," "FHA," "should I buy a house in the specific year" — minor transcript artifact "little toe, no money down" for "little to no money down"). |
| The Brand Build Has an Order — strategy → mood board → stylesheet/kit → optimization → conversion system → 12-month plan | VERIFIED | S2 timestamp 19:09–24:06 (sequence matches: onboarding call → strategy → mood boards → blueprint/stylesheet → social media kit/templates → conversion system (VSL, funnel, lead magnets) → 12-month video plan, in that order). |

## Claims — genius.md, new "Anti-Patterns (Sourced)" section (this repair pass)

All seven items were written for this repair pass and quote the raw
transcripts directly (see the bullets themselves in `genius.md` for the
per-item timestamp/date anchors). Cross-checked here against the extracted
files a second time for this ledger:

| Claim | Label | Anchor |
|---|---|---|
| "posting for views instead of posting for clients" | VERIFIED | S1 timestamp 0:59–1:01, verbatim. |
| "the only other people that are following them are other realtors" | VERIFIED | S1 timestamp 1:04–1:09, verbatim. |
| "a lot of agents are sharing facts with no context" | VERIFIED | S1 timestamp 3:58–4:02, verbatim (reconstructed across adjacent transcript timestamp lines, no words altered or added). |
| "mistake number three is going to be no structure" | VERIFIED | S1 timestamp 7:06–7:10, verbatim (reconstructed across adjacent transcript timestamp lines). |
| "the average agent only posts listings and no human connection" | VERIFIED | S1 timestamp 10:56–11:03, verbatim (reconstructed across adjacent transcript timestamp lines). |
| "if you're trying to speak to everyone, you end up connecting with no one" | VERIFIED | S2 timestamp 17:12–17:18, verbatim (reconstructed across adjacent transcript timestamp lines). |
| "you don't want to choose a niche who doesn't have the money to actually purchase frequent properties, who is not easy to target and is shrinking" | VERIFIED | S2 timestamp 7:36–7:45, verbatim (reconstructed across adjacent transcript timestamp lines). |

Note on "reconstructed across adjacent transcript timestamp lines": the
Merlin-AI transcript format breaks sentences across multiple `M:SS -` lines
mid-word/mid-clause (raw speech-to-text segmentation). Every quote above is
the unmodified, unreordered concatenation of consecutive transcript
fragments — no words were changed, dropped, or added in stitching them into
a single sentence.

## Claims — genius.md, "How to Use This Skill (Model Calibration)" (new section, this repair pass)

This section is craft/voice guidance authored for this repair pass (modeled
on `skills/ben-watkins-storytelling/genius.md` lines 7–16 per the batch
envelope), not a factual claim about Mike Sherrard — no VERIFIED/LIKELY/
UNCONFIRMED label applies to the calibration instructions themselves. It
introduces no new factual claims about Sherrard beyond what's already
tabulated above (four-criteria filter, HVC structure, "message with no
microphone" framing — all VERIFIED).

## Summary

- **VERIFIED**: 22 claims (10 Genius Patterns + 4 of 5 Hidden Knowledge core
  claims + 7 new Anti-Patterns + 1 Hidden Knowledge partial), all anchored to
  verbatim or near-verbatim transcript text in S1 or S2, both confirmed
  present and correctly sized (32,129 bytes / 42,523 bytes) via a
  `python3 tarfile`-per-member scan of `_archive/claude-export-2026-07-01.tar.gz`
  this session — not asserted from memory.
- **LIKELY**: 1 claim (the algorithmic-compounding mechanism inside the
  Realtor-Follower Diagnostic — a reasonable synthesis of S1's engagement-
  signal logic, no single verbatim anchor for the "compounding" framing
  itself).
- **UNCONFIRMED**: none found this pass. No claim in `genius.md` was
  fabricated or carried an invented provenance anchor; every quote traces to
  a specific timestamp in one of the two source transcripts, both of which
  were opened and read in full during this session (2026-07-18).
