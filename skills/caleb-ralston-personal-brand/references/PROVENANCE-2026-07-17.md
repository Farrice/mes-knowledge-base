# Provenance — caleb-ralston-personal-brand repair (Wave 3 Lane 4 Batch 2)

Sources consulted (both files under `extractions/` matching this expert; both read in full, sizes recorded via `wc -c`):
- `extractions/caleb-ralston/transcript.txt` — 65,808 bytes
- `extractions/caleb-ralston/caleb-ralston-2026-extraction-report.md` — 13,878 bytes
- `skills/caleb-ralston-personal-brand/references/genius-patterns.md` — verbatim mirror of genius.md's Pattern 1-17, checked, no independent sourcing value

Full claim-by-claim VERIFIED/LIKELY/UNCONFIRMED table: `references/source-ledger.md` in this output directory.

## Anchor table — every new quote/claim added this pass

| Added to | Claim/quote | Anchor | Verified via |
|---|---|---|---|
| genius.md § Core Philosophy | "I don't optimize for going viral. I optimize for solving your problems." | transcript.txt | `grep -qF` exact match |
| genius.md § Pattern 1 | "we have almost 90,000 subscribers on YouTube within the first year or 53,000 people on our email list" | transcript.txt | `grep -qF` exact match |
| genius.md § Pattern 2 | "If you've gone from A to B, you are qualified to help people go..." | transcript.txt | `grep -qF` exact match |
| genius.md § Pattern 5 | (no quote added — honest UNCONFIRMED/LIKELY grounding note instead) | n/a | full-text search of both files, no match found |
| genius.md § Pattern 6 | "You draw a line down a piece of paper and you're going to have two columns..." | transcript.txt | `grep -qF` exact match |
| genius.md § Pattern 7 | "branding is just simply a pairing of things and good branding is an intentional pairing of relevant things consistently" | transcript.txt | `grep -qF` exact match |
| genius.md § Pattern 8 | "if you give them a learning in the opening 30 seconds..." | transcript.txt | `grep -qF` exact match |
| genius.md § Pattern 9 | "followers don't matter... indicator that they want more" | transcript.txt | `grep -qF` exact match |
| genius.md § Pattern 10 | "I don't like chasing virality." | transcript.txt | `grep -qF` exact match |
| genius.md § Pattern 15 | "a problem, a painful problem that my customer faces plus my unique solution. I call that a gift." | transcript.txt | `grep -qF` exact match |
| genius.md § Pattern 16 | "predicts a wave of these resets in 2026" / "engineer a reset: public acknowledgment, apology, and documented transformation" | caleb-ralston-2026-extraction-report.md | `grep -qF` exact match |
| genius.md § Pattern 18 | "I call that a gift. That's why I use the wrapping term..." | transcript.txt | `grep -qF` exact match (reused from Pattern 15's anchor, applied to the term-origin claim specifically) |
| genius.md § Pattern 19 | "call out, your credibility, your compass, and your core learning" (live 4C label variant) | transcript.txt | `grep -qF` exact match |
| genius.md § Pattern 23 | "a lot of people prefer Instagram because of the DMs and the messaging..." | transcript.txt | `grep -qF` exact match |
| genius.md § Anti-Patterns (7 items) | see genius.md for full quotes | transcript.txt (6) + caleb-ralston-2026-extraction-report.md (1) | each `grep -qF` exact match before writing |
| genius.md § The Quality Tests → Accordion Test | "every video averages 103 views and then one video gets 417" | transcript.txt | `grep -qF` exact match |
| genius.md § Hall of Fame Exemplars | Provenance note added — Exemplars 1, 2, 4 flagged UNCONFIRMED; Exemplar 4's "Verbatim" heading label flagged as overstated; Exemplar 5's dialogue flagged UNCONFIRMED (concept independently verified) | both files | full-text search, no match on the exemplar dialogue text |

## Discovery flagged, not fixed (out of scope for this pass, named honestly)

Full-text search of both extraction files found **no verbatim match** for several pre-existing quoted/labeled claims already in genius.md before this repair pass began (i.e., not introduced by this worker):
- Pattern 5's "loose cannon" framing
- Pattern 24's "60/40 ratio," "I only talk about email marketing," and "Harley B-roll" quoted contrast
- Pattern 25 (Signature Paradox Engine) — no anchor in either extraction file (added in a prior evolution cycle per the existing Evolution Log entry dated 2026-04-09)
- Hall of Fame Exemplars 1, 2, and 4's illustrative dialogue, and Exemplar 5's central "gift/wrapping" line
- Pattern 3's "Would I text this to my friends?" exact phrasing (concept is real; this specific wording isn't in either source file)

None of this pre-existing content was deleted or rewritten (out of scope — these checks were already passing, and the envelope requires preserving passing content). Each is now honestly labeled in `references/source-ledger.md` and, where it sits inside a section this repair touched, flagged inline in genius.md itself.
