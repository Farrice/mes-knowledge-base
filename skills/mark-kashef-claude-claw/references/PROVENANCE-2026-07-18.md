# Provenance — mark-kashef-claude-claw repair pass

Anchor → source file + location, for every quote/claim added or upgraded this pass.

| Anchor (as it appears in genius.md) | Source file | Location | Verified how |
|---|---|---|---|
| "am I building a derivative of a derivative of a derivative?" | extractions/mark-kashef-claude-claw/extraction-report.md | Genius Pattern 1 (line 25) | `grep -F` exact match |
| "the ongoing cost of keeping them in sync" / "is invisible until it compounds into abandonment" | extractions/mark-kashef-claude-claw/extraction-report.md | Hidden Knowledge 1 (line 75) | `grep -F` exact match |
| "An API call gives you intelligence; a subprocess gives you capability." | extractions/mark-kashef-claude-claw/extraction-report.md | Hidden Knowledge 2 (line 80) | `grep -F` exact match |
| "SQLite over Supabase. Local file system over cloud storage." | extractions/mark-kashef-claude-claw/extraction-report.md | Genius Pattern 4 (line 43) | `grep -F` exact match |
| "anything that seems to be noise" / "fluid and buttery" | extractions/mark-kashef-claude-claw/extraction-report.md | Hidden Knowledge 3 (line 85) | `grep -F` exact match |
| "the architecture documentation AND the build instructions AND the interactive wizard, all compressed into one artifact" | extractions/mark-kashef-claude-claw/extraction-report.md | Hidden Knowledge 5 (line 95) | `grep -F` exact match |
| "Telegram could be swapped for WhatsApp; Claude Code could be swapped for Codex or Gemini CLI" | extractions/mark-kashef-claude-claw/extraction-report.md | Genius Pattern 8 (line 67) | `grep -F` exact match |
| "24-Hour Quickstart" / "7-Day Sprint" / "30-Day Integration" | extractions/mark-kashef-claude-claw/extraction-report.md | Implementation Pathway (lines 150–152) | `grep -F` exact match |
| "<5 seconds for text, 30-40 seconds for video interpretation" | extractions/mark-kashef-claude-claw/extraction-report.md | Methodology, Stage 8 latency note (line 117) | `grep -F` exact match |
| "The most important magic words you always need to say is create an agent team or spawn an agent team. If you just say spawn agents, it could get confused between sub aents..." | extractions/mark-kashef/transcript.txt | Full transcript, ~1/3 through (single-block transcript, no line numbers) | `grep -F` exact match, including the source's own "sub aents" typo (marked `[sic]` in genius.md so it is never mistaken for a transcription error introduced by this repair) |
| File-added date "2026-03-02" used in one anchor | git history | `git log --diff-filter=A --date=short -- extractions/mark-kashef-claude-claw/extraction-report.md` | Command output: `2026-03-02 3d4ee6e8f` (same commit added all three source files used this pass) |
| File sizes cited in references/source-ledger.md | filesystem | `wc -c` on all three source files | extraction-report.md (claw) = 14,288 bytes; extraction-report.md (mark-kashef) = 6,254 bytes; transcript.txt (mark-kashef) = 27,910 bytes — all non-zero, no "unrecoverable" claim made |
| Hall of Fame Exemplars 1 & 2, Anti-Exemplar narrative, Signature Moves, Quality Rubric | N/A — searched, not found | `grep -n "Monolithic Cloud Bot\|Custom Claude Code CLI\|Cross-Platform AI Assistant Bridge\|Signature Moves\|Expert-Specific Quality Rubric"` against both extraction-report.md files returned no hits | Confirmed absent, not "unread" — labeled UNCONFIRMED (constructed) in source-ledger.md rather than silently left unlabeled |
