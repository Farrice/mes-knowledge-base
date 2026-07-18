# Provenance — mark-kashef-visual-design repair pass

Anchor → source file + location, for every quote/claim added or upgraded this pass. All rows `grep -F` verified against the raw transcript unless noted.

| Anchor (as it appears in genius.md) | Source file | Location | Verified how |
|---|---|---|---|
| "the same way we used to go on whiteboards and doodle and then send that doodle to our design team and then that design team would create a Figma" | extractions/mark-kashef-visual-design/transcript.txt | landing-page section, ~1/3 through | `grep -F` exact match |
| "before writing any code create a ask key wireframe of a SAS analytics dashboard. Put a sidebar stat cards two charts side by side and a data table below" | extractions/mark-kashef-visual-design/transcript.txt | dashboard section | `grep -F` exact match (each clause) |
| "put a sidebar stat cards two charts side by side and a data table below" (Taste Arbitrage anchor) | extractions/mark-kashef-visual-design/transcript.txt | dashboard section | `grep -F` exact match |
| "you can then be the orchestrator, the conductor" | extractions/mark-kashef-visual-design/transcript.txt | database/SQL section, near close | `grep -F` exact match |
| "I've actually been using this for slide decks for clients for the past six months secretly" | extractions/mark-kashef-visual-design/transcript.txt | slide-deck section | `grep -F` exact match |
| "I use this day-to-day to better understand every single new feature and concept that comes out" | extractions/mark-kashef-visual-design/transcript.txt | closing section | `grep -F` exact match |
| "I even created a bunch of skills from them because this gives you the power to have full visualization and understanding of each and every part of an intricate system" | extractions/mark-kashef-visual-design/transcript.txt | closing section | `grep -F` exact match |
| "Build me a SAS dashboard. I want a sidebar, some stat cards, a couple charts, and a data table" | extractions/mark-kashef-visual-design/transcript.txt | dashboard "lazy prompt" experiment | `grep -F` exact match |
| "a fairly ugly vibecoded icon looking sidebar" | extractions/mark-kashef-visual-design/transcript.txt | same experiment, output description | `grep -F` exact match |
| "I can already see it's proposing some vibecoded icons" | extractions/mark-kashef-visual-design/transcript.txt | landing-page section | `grep -F` exact match |
| "make this diagram as if you're in seventh grade" | extractions/mark-kashef-visual-design/transcript.txt | database/SQL section | `grep -F` exact match |
| "the average person who is non-technical just assumes that the database created is perfect and doesn't really get into the weeds as to how different things are stored" | extractions/mark-kashef-visual-design/transcript.txt | database section | `grep -F` exact match |
| "the coloring is not ideal" / "this looks more of a therapeutic reading based website" / "it just doesn't look clean" | extractions/mark-kashef-visual-design/transcript.txt | landing-page lazy-prompt comparison | `grep -F` exact match, each clause |
| "very token intensive" | extractions/mark-kashef-visual-design/transcript.txt | slide-deck section | `grep -F` exact match |
| "5-6 iterations at the code layer can exhaust context windows entirely" | extractions/mark-kashef-visual-design/extraction-report.md | Genius Pattern 3 ("The Token Economist") | `grep -F` exact match in the report; labeled LIKELY (report synthesis, not spoken verbatim in transcript) |
| File sizes cited in references/source-ledger.md | filesystem | `wc -c` on both source files | extraction-report.md = 12,587 bytes; transcript.txt = 17,259 bytes — both non-zero, no "unrecoverable" claim made |
| Hall of Fame Exemplars 1 & 2, Anti-Exemplar prompt string, Signature Moves, Quality Rubric (pre-existing content) | N/A — searched, not found | `grep -n "Executive Dashboard - Q3\|Simplified API Workflow\|sleek and modern landing page\|super engaging"` against both source files returned no hits | Confirmed absent, not "unread" — labeled UNCONFIRMED (constructed) in source-ledger.md; a provenance note was also added inline in genius.md above the Anti-Exemplar pointing to the transcript-verified equivalent |
