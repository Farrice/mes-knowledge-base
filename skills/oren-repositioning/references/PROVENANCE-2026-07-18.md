# PROVENANCE — oren-repositioning repair pass

Anchor → source file+location table for every addition/change made in this repair pass. Full claim-by-claim ledger (including pre-existing UNCONFIRMED items not touched) is at `references/source-ledger.md`.

| Anchor (where added) | Text added | Source file + location |
|---|---|---|
| genius.md, Pattern 1 Application | `"People can describe your brand without mentioning any competitor"` | extractions/oren/extraction-report-repositioning.md, line 30 (Pattern 1 Success Metric) |
| genius.md, Pattern 4 Application | `"Fans describe the brand as a 'world' or 'vibe' rather than a product or person"` | extractions/oren/extraction-report-repositioning.md, line 48 (Pattern 4 Success Metric) — quote marks normalized from " to ' for nesting inside the sentence |
| genius.md, Pattern 8 Application | `"did both sides leave with more fame, recognition, and creative capability than they entered with?"` | extractions/oren/extraction-report-repositioning.md, line 69 (Pattern 8 body) |
| genius.md, Hidden Knowledge intro | `"the sales material must itself be the proof of the capability being sold"` | extractions/oren/extraction-report-repositioning.md, line 99 (Hidden Knowledge #5) |
| genius.md, Hidden Knowledge #3 (Squad Algorithm) | `"a stable creative dyad generates compounding algorithmic distribution that a solo creator cannot access regardless of content quality"` | extractions/oren/extraction-report-repositioning.md, line 89 (Hidden Knowledge #3) |
| genius.md, new `## Anti-Patterns` section (6 items) | 6 quotes, one per bullet | extractions/oren/extraction-report-repositioning.md — lines 104–106 (HK#6), 51 (Pattern 5), 88–91 (HK#3), 108–111 (HK#7), 78–81 (HK#1), 69 (Pattern 8) — line cited inline on each bullet |
| genius.md, `## How to Use This Skill (Model Calibration)` | Upgraded in place (renamed from "Opus 4.7 Calibration"); added texture + polish-is-the-tell bullets | Modeled on skills/ben-watkins-storytelling/genius.md lines 7–16 per ENVELOPE.md batch instruction; texture content synthesized from Oren's own patterns already in this file (House of Errors counter-signaling, Hidden Knowledge #7 discomfort test) — not a new external source |
| references/genius-patterns.md, references/hidden-knowledge.md | Same 5 quote insertions mirrored | Same anchors as above — kept duplicate reference files in sync with genius.md |
| references/source-ledger.md | New file | Synthesized from cross-referencing every genius.md claim against extractions/oren/*.md via grep + full read of extractions/oren/transcript.txt (confirmed off-topic — different Oren video) |

## Verification method
Every quote above was located via `grep -n` against `extractions/oren/extraction-report-repositioning.md` and confirmed to match the genius.md insertion character-for-character (aside from the one documented "→'" quote-nesting normalization). `extractions/oren/transcript.txt` (29,376 bytes) was read in full and confirmed to cover a different Oren video (brand-archetypes, not repositioning) — recorded in source-ledger.md rather than asserted without evidence.
