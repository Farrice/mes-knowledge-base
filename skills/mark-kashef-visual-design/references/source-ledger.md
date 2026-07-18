# Source Ledger — mark-kashef-visual-design

Repair pass: Wave 3 Lane 4 Batch 11. Ground truth = files under `extractions/`
matching this expert, verified by direct file read + `wc -c` (sizes below),
plus content already inside the skill files before this repair.

## Files consulted (all read in full this pass)

| File | Size (`wc -c`) | Role |
|---|---|---|
| `extractions/mark-kashef-visual-design/extraction-report.md` | 12,587 bytes | PRIMARY source. Synthesized extraction from "ASCII Art Wireframing for Claude Code," ~15 min YouTube video. |
| `extractions/mark-kashef-visual-design/transcript.txt` | 17,259 bytes | RAW verbatim transcript of the same video. Read in full this pass — every new quote added below was `grep -F` matched against this file before being placed in genius.md. |

Both files are non-zero, both were read start to finish. No "unrecoverable/0-byte" claim is made anywhere in this pass. Note: an unrelated `extractions/mark-kashef/` folder also exists (a different video, "7 Agent Team Use Cases") — checked and confirmed it is NOT the source for this skill (no wireframe/ASCII/visual-contract content); not used here.

## Claim-by-claim labels

| Claim / anchor | Label | Basis |
|---|---|---|
| 8 Genius Patterns (Visual Contract Protocol, Assumption Assassin, Token Economist, Taste Arbitrage, Progressive Refinement Engine, Complexity Equalizer, Multi-Vertical Blueprint, Orchestrator Identity Shift) | LIKELY | Verbatim paraphrase match to `extraction-report.md` "Genius Patterns" section (lines 24-70). The report itself is a synthesis of the transcript, not a literal transcription, so the *pattern names and framing* are LIKELY rather than VERIFIED even though several of the underlying claims are independently VERIFIED below. |
| 6 Hidden Knowledge items (Lazy Prompt Firewall, Figma Killer Insight, Secret Slide Deck Revenue Play, Visualization-as-Understanding, Vibe Coding Horror Stories Root Cause, Skills From Diagrams) | LIKELY (framing) / **VERIFIED** (quotes) | The item titles and their surrounding framing are LIKELY (report synthesis). The direct quotes inside them — see below — are VERIFIED against the raw transcript. |
| "I've actually been using this for slide decks for clients for the past six months secretly" | **VERIFIED** | `grep -F` exact match, `transcript.txt`, slide-deck section. |
| "I use this day-to-day to better understand every single new feature and concept that comes out" | **VERIFIED** | `grep -F` exact match, `transcript.txt`, closing section. |
| "I even created a bunch of skills from them because this gives you the power to have full visualization and understanding of each and every part of an intricate system" | **VERIFIED** | `grep -F` exact match, `transcript.txt`, closing section. |
| "you can then be the orchestrator, the conductor" | **VERIFIED** | `grep -F` exact match, `transcript.txt`, database section. |
| "before writing any code create a ask key wireframe of a SAS analytics dashboard. Put a sidebar stat cards two charts side by side and a data table below" | **VERIFIED** | `grep -F` exact match (each clause independently confirmed), `transcript.txt`, dashboard section. |
| "the same way we used to go on whiteboards and doodle and then send that doodle to our design team and then that design team would create a Figma" | **VERIFIED** | `grep -F` exact match, `transcript.txt`, landing-page section. |
| "Build me a SAS dashboard. I want a sidebar, some stat cards, a couple charts, and a data table" | **VERIFIED** | `grep -F` exact match, `transcript.txt`, dashboard "lazy prompt" experiment. |
| "a fairly ugly vibecoded icon looking sidebar" | **VERIFIED** | `grep -F` exact match, `transcript.txt`, same experiment, describing the resulting output. |
| "I can already see it's proposing some vibecoded icons" | **VERIFIED** | `grep -F` exact match, `transcript.txt`, landing-page section. |
| "make this diagram as if you're in seventh grade" | **VERIFIED** | `grep -F` exact match, `transcript.txt`, database/SQL section. |
| "the average person who is non-technical just assumes that the database created is perfect and doesn't really get into the weeds as to how different things are stored" | **VERIFIED** | `grep -F` exact match, `transcript.txt`, database section. |
| "A lot of vibe coding horror stories just come from poor planning" | **VERIFIED** | `grep -F` exact match, `transcript.txt`, slide-deck section (already present in genius.md pre-repair; re-confirmed this pass). |
| "the coloring is not ideal" / "this looks more of a therapeutic reading based website" / "it just doesn't look clean" | **VERIFIED** | `grep -F` exact match (each clause), `transcript.txt`, landing-page lazy-prompt comparison. |
| "very token intensive" | **VERIFIED** | `grep -F` exact match, `transcript.txt`, slide-deck section. |
| "5-6 iterations at the code layer can exhaust context windows entirely" | LIKELY | Present verbatim in `extraction-report.md`, Genius Pattern 3 ("The Token Economist"). Not a direct transcript quote — the transcript says slides are "very token intensive" and describes running "out of tokens" across "five, six, seven" iterations; the report's phrasing compresses this. Labeled LIKELY, not VERIFIED, because the exact sentence is the report's synthesis, not Kashef's own words. |
| "~50 tokens per change" / "~5,000 tokens per change" / "60-80%" token reduction | LIKELY | Present verbatim in `extraction-report.md`, Genius Pattern 3 and Executive Summary. No exact dollar/token figures are spoken in the raw transcript (Kashef discusses token cost qualitatively — "very token intensive," running "out of tokens" — the specific numbers are the extraction pass's own estimate). |
| "$50K+/year design pipeline role" (Figma Killer Insight) | LIKELY | Present verbatim in `extraction-report.md`, Hidden Knowledge 2. Not spoken in the transcript — the transcript describes the whiteboard→Figma→dev pipeline qualitatively without a dollar figure. This is the report's own estimate. |
| Hall of Fame Exemplars 1 & 2 (Executive Dashboard Blueprint, Complex System Diagram) | **UNCONFIRMED (constructed)** | Searched both `extraction-report.md` and `transcript.txt` in full — neither wireframe artifact (with these exact labels, metrics, or layouts) appears in the source material. These are illustrative compositions built from the Genius Patterns by a prior enrichment pass, not reproduced transcript content. Flagged here so this is never mistaken for sourced case history; the source's own two worked wireframes (SaaS dashboard, SaaS landing page) are the transcript-grounded equivalents, referenced inline in the Genius Patterns and Anti-Patterns sections above instead. |
| Anti-Exemplar "Vague Marketing Landing Page Request" (the specific prompt string) | **UNCONFIRMED (constructed)** | Not found in either source file — grepped for "sleek and modern landing page," "super engaging," no hits. This is an illustrative composition. A provenance note was added directly above it in genius.md pointing to the transcript-verified equivalent in the new Anti-Patterns (Sourced) section. |
| Signature Moves section (4 items) | **UNCONFIRMED (derived)** | Restates Genius Patterns 1, 4, 5, 8 in a "Deploy when" format; not a new claim, no new provenance risk, but not itself transcript-verbatim. |
| Expert-Specific Quality Rubric | **UNCONFIRMED (derived, not a factual claim)** | Synthesized scoring rubric from the Genius Patterns and their Success Metrics — not a claim about what Kashef said, so VERIFIED/LIKELY/UNCONFIRMED provenance labeling doesn't strictly apply; labeled UNCONFIRMED here to flag it as a derived artifact rather than sourced content. |

## Repair-pass additions (this batch)

New inline VERIFIED quotes were added to 7 of the 8 previously zero-entity
sections (The Core Insight, Visual Contract Protocol, Taste Arbitrage,
Orchestrator Identity Shift, The Secret Slide Deck Revenue Play,
Visualization-as-Understanding, Skills From Diagrams) plus a token-economics
cross-reference to the 8th (Stacking Protocol). Every quote was `grep -F`
verified against `extractions/mark-kashef-visual-design/transcript.txt`
verbatim before being placed in genius.md — none were invented,
paraphrased-then-quoted, or reconstructed from memory. The new
`## Anti-Patterns (Sourced)` section (6 items) uses six additional
transcript-VERIFIED quotes plus one extraction-report LIKELY anchor, all
cited inline on the bullet line itself.
