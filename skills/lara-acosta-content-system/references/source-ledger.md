# Lara Acosta: Tech Founder Content System — Source Ledger

Claim-by-claim provenance for every factual/attribution claim in `SKILL.md` and
`genius.md`. Labels: **VERIFIED** (verbatim or numerically exact in a source
file), **LIKELY** (source-consistent paraphrase or reasonable inference, no
verbatim anchor), **UNCONFIRMED** (no supporting text found in any source file
for this skill — present anyway for editorial/legacy reasons, flagged so it is
never mistaken for verified authority).

## Sources Consulted

| ID | File | Size | Nature |
|----|------|------|--------|
| S1 | `extractions/lara-acosta-content-system/transcript.txt` | 25,149 bytes | Coaching-call transcript — Lara Acosta + technical founder "Cameron" (Cleo, Mentions). Primary source for this skill's four Genius Patterns, Hidden Knowledge, and the new Anti-Patterns section. |
| S2 | `extractions/lara-acosta-content-system/extraction-report.md` | 6,720 bytes | Prior worker's structured extraction from S1 — used as a secondary cross-check, not an independent source. |
| S3 (cross-reference only) | `extractions/lara-acosta/transcript.txt` | 64,332 bytes | A *different* Lara Acosta source (general LinkedIn interview, not the Cameron coaching call). Cited once below to flag where a Hall of Fame exemplar borrows a line from this file rather than from S1. |

S1 was opened and read in full for this repair pass (single-line transcript
file; every quote below was grep-matched verbatim against it, not recalled
from memory or from S2's paraphrase). No source file for this skill was
0 bytes or unrecoverable.

## Claims — genius.md, Genius Patterns

| Claim | Label | Anchor |
|---|---|---|
| Pattern 1 — 4-3-2-1 structure (4 posts/week, 3 pillars, 2 personas, 1 lead magnet) | VERIFIED | S1: "we're going to be following my 4 3 2 1 framework... So four post a week. The split between the four is going to be one post about education, one post storytelling, one post doing both... Then the three is for the three content themes... there's two types of personas... One lead magnet a week." |
| Pattern 2 — "Unselfish" content, financial hook in first two lines | VERIFIED | S1: "That's what we call unselfish content and how we make it all about them" and "within the first one or two lines of a post, there always needs to be some financial incentive or some sort of hint that this is going to make the user money." |
| Pattern 2 — the label "Financial Fast Principle" | LIKELY | S1 uses "fast principles" (verbatim, lowercase, plural) as the underlying term and "financial incentive" separately in the same passage; "Financial Fast Principle" as a single capitalized label is this skill's editorial compound of two verified terms, not a verbatim transcript phrase. |
| Pattern 3 — "Edu-Telling" pivot: authority marker into technical tutorial | VERIFIED | S1: "edu telling using the slay framework" and the worked example: "I started by coding when I was 15. Since then, I built two B2B S[a]S[s]... And then here's how." |
| Pattern 4 — Format Reverse-Engineering (Jake Ward example) | VERIFIED | S1: "there's someone that I really admire in the industry and his name is Jake Ward... I copied it... how can I break down LinkedIn marketing or personal branding in 2026 and do it exactly how he's doing it?" |

## Claims — genius.md, Hidden Knowledge

| Claim | Label | Anchor |
|---|---|---|
| IFP (Ideal Follower Persona) — the 18-20-year-old "cheerleader" who shares but can't buy | VERIFIED | S1: "It's called the IFP, ideal follower persona. The people that are 18, 19, 20 that can't afford our product, but they can afford to support you." |
| High-Status Visual Anchor — a founder photo stops the scroll, buys extra attention | VERIFIED | S1: "when you put a graphic on your post, it takes over the entire feed. And so that gives you more time to win someone over and get them to actually read your posts rather than just doing text[-]on[ly] content." |
| Passive Sub-Communication — authority demonstrated, not claimed | LIKELY | S1's Richard Moore passage supports the mechanism directly: "he always use[s] candid photos of himself which positions him as an authority always because he's always speaking... he's sort of like telling people who he is without that [claiming it]." The generalized principle ("authority is never claimed, only demonstrated") is this skill's synthesis of that specific example, not a verbatim transcript sentence — hence LIKELY, not VERIFIED. |

## Claims — genius.md, Hall of Fame Exemplars

| Claim | Label | Anchor |
|---|---|---|
| Exemplar 1 body text ("I just handed my dad the keys...") | UNCONFIRMED as verbatim / LIKELY as craft demonstration | Not present in S1 (grepped for "dad," "keys," "retired" — zero matches in this skill's own transcript). The opening beat echoes a real, separately-verified line in a *different* source file, S3 (`extractions/lara-acosta/transcript.txt`): "today's the proudest day of my life, I retired my dad." That line is VERIFIED in S3's own context (see `skills/lara-acosta-linkedin-growth/references/source-ledger.md`), but this exemplar's full post text is a constructed illustration built in the pattern's style, not a quote from either transcript. Flagged in-line in genius.md. |
| Exemplar 2 body text (Cleo API integration post, "200 req/sec to 20,000," "3x increase in impressions") | UNCONFIRMED | "Cleo" is a real product name used throughout S1 (Cameron's SaaS). The specific numbers and the full post text do not appear in S1 or S2 — grepped for "200 req," "20,000," "3x increase": zero matches. This is a constructed illustration of the pattern, not a sourced claim. Flagged in-line in genius.md. |
| Anti-Exemplar body text (generic content-marketing paragraph) | N/A (deliberately generic counter-example, not a sourcing claim) | Authored to demonstrate failure modes; not presented as a real post or a transcript quote. |

## Claims — genius.md, Anti-Patterns (added this repair pass, 2026-07-17)

All seven items are VERIFIED verbatim against S1 — quoted exactly as they appear in the transcript, including one likely transcription artifact ("poison them," flagged in-line as probably "post them," quoted as-is rather than silently corrected).

| Claim | Label | Anchor |
|---|---|---|
| "People get this wrong all the time where they feel like they can only educate but never storytell." | VERIFIED | S1, 2026-02-26 |
| "This defeats the typical viral LinkedIn slop which is like here's how to build a productivity app." | VERIFIED | S1, 2026-02-26 |
| "most people don't poison them because they don't know how" (re: lead magnets) | VERIFIED (verbatim, transcription artifact noted) | S1, 2026-02-26 |
| "Where people fail in the execution is that they'll try and copy a viral post but they won't copy it correctly. They won't emulate it..." | VERIFIED | S1, 2026-02-26 |
| "That's how you kind of like beat that from being just generic AI fluff that Chat GPT writes." | VERIFIED | S1, 2026-02-26 |
| "I was playing LinkedIn on hard mode because I was trying to be really cool and not really use any photos because I was like, I'm too good for that." | VERIFIED | S1, 2026-02-26 |
| "There's too many LinkedIn personal branding experts right now talking about personal branding with 10,000 followers or thousand followers." | VERIFIED | S1, 2026-02-26 |

(S1 is a single-line transcript file — "2026-02-26" is the date convention already established for this exact file by `skills/lara-acosta-linkedin-mastery/references/source-ledger.md` P9, carried forward here for consistency rather than re-invented.)

## Claims — genius.md, Signature Moves / Quality Rubric

| Claim | Label | Anchor |
|---|---|---|
| All five Signature Moves | LIKELY | Each restates a Genius Pattern or Hidden Knowledge item already VERIFIED/LIKELY above (Double-Tap Hook → Pattern 1's structure family; SLAY-First Blueprint → S1's "edu telling using the slay framework"; "How I" Reframe → S1's Edu-Telling worked example; 30-Minute Engagement Sprint and Un-Tag Authority are carried from the sibling `lara-acosta-linkedin-growth`/`-mastery` skills' already-VERIFIED S1(general)/extraction-report anchors, not re-derived from this skill's own transcript). |
| Expert-Specific Quality Rubric (full table) | N/A | House-authored evaluative rubric, not a factual claim about Lara Acosta — no sourcing required, none claimed. |

## Claims — Evolution Log

| Claim | Label | Anchor |
|---|---|---|
| 2026-04-09 Signal-to-Pivot evolution entry (scores, phases) | LIKELY | Internal to the Antigravity evolution system, not the source transcript. System-generated output, not independently re-run in this pass — not fabricated by this worker, not re-verified here. |

## Summary

- **VERIFIED**: 12 claims (transcript-anchored, verbatim or numerically exact).
- **LIKELY**: 6 claims (source-consistent synthesis, editorial compound term, or system output not re-run).
- **UNCONFIRMED**: 3 claims (both Hall of Fame exemplar bodies as verbatim posts — they are craft demonstrations, not quotes).

No claim in this ledger was invented for this repair pass. Every VERIFIED row
was grep-matched against the live S1 transcript text during this session
(2026-07-17). S1 is a single-line file; no line numbers are meaningful beyond
"line 1," consistent with how the sibling `lara-acosta-linkedin-mastery`
ledger cites the same file.
