# Jason Fladlien — Repair Provenance

Anchor → source file/location table for the two changes made in this repair pass. Full claim-by-claim provenance for genius.md's existing pattern content lives in `references/source-ledger.md` (new file, this repair).

## Change 1: `## How to Use This Skill (Model Calibration)` section (genius.md)

Not a factual claim about Fladlien — this is a model-instruction section (how to deploy the skill), modeled structurally on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per the envelope's instruction, but written fresh for Fladlien's own craft texture. Every specific claim embedded in it is separately anchored:

| Line in new section | Anchor |
|---|---|
| "naming a fear reduces its intensity" | `extractions/jason-fladlien/transcript.txt`, verbatim: "if you label and call out the fear, you reduce its intensity" — same source as genius.md Hidden Knowledge §8 |
| "his entire physics is subtraction" | `extractions/Jason Fladlien/transcript.txt`, verbatim: "there's a physics that's pushing back against us" + genius.md Pattern §1 (Success by Subtraction), both already source-anchored |
| "I know you're skeptical, I was too" (named as a weak/shallow move) | `extractions/jason-fladlien/transcript.txt`, verbatim: "There are a few copyrighters that will say, 'I know you're skeptical. I was too.'" |
| "$5,000/hour" | `extractions/jason-fladlien/transcript.txt`, verbatim: "Now I charge $5,000 an hour." |
| "I'm going to sell you a PDF for $49. No bonuses, no extra goodies involved." | genius.md's existing Hall of Fame Exemplar 2 (Radical Candor PDF Lead) — carried forward verbatim from the pre-existing file, re-verified as consistent with the verbatim-confirmed Radical Candor as Scarcity pattern (§13) |

## Change 2: `references/source-ledger.md` (new file)

See the file itself — it is the provenance table for the rest of genius.md and is structured as claim → status → anchor throughout. Not duplicated here to avoid drift between two copies of the same table.

## Verification method

1. Confirmed both primary transcripts exist and are non-empty via `ls -la` (89,783 bytes and 91,973 bytes) before making any claim about source availability.
2. Extracted the 89 Jason-Fladlien-titled conversation files from `_archive/claude-export-2026-07-01.tar.gz` directly (not relying on the prior extraction's summary) and grepped them for specific quoted claims in genius.md.
3. Where an exact quote could not be located, labeled UNCONFIRMED rather than inventing an anchor (see source-ledger.md: Bhagavad Gita comparison, China Concierge Program name, Cost-Has-Three-Currencies ranking) or flagged a discrepancy where the cited source contains a *different* analogy than the one quoted (Brown Paper Bag Beta — source uses a "Xerox copy of the Mona Lisa" analogy, not "brown paper bag").
