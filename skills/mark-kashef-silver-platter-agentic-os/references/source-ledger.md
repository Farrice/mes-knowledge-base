# Source Ledger — Mark Kashef Silver Platter Agentic OS

Claim-by-claim provenance for every quote, timestamp, and factual assertion added in this repair pass. Labels: VERIFIED (read the exact source, quote matched verbatim), LIKELY (source strongly implies it but not verbatim-matched), UNCONFIRMED (no source found — flagged, not anchored).

| # | Claim / Quote | Source | Location | Label |
|---|---|---|---|---|
| 1 | "So when it comes to the actual valuable part... you're bloating it with things that don't matter." | `extractions/video-context/-WCNwxz3uoM/transcript.txt` | ~00:04:12–00:04:26 | VERIFIED — grep-matched verbatim |
| 2 | "one of the many ways you could solve this is through summary files or summary tables, where you distill the core information, the core KPIs" | same transcript | ~00:04:36–00:04:43 | VERIFIED — grep-matched verbatim |
| 3 | "have Cloud Code create summary tables... it will use Python deterministic, so we're not risking an AI agent hallucinating." | same transcript | ~00:16:23–00:16:32 | VERIFIED — grep-matched verbatim |
| 4 | "there's a reason why you typically see the configuration here on the right-hand side where you have an orchestrator or a chief of staff managing the other agents... cold starting conversations with your agent teams having a mismatch or overlap of which agent should fire at the right time." | same transcript | ~00:08:50–00:09:16 | VERIFIED — grep-matched verbatim |
| 5 | "You don't want to have agents for the sake of having agents. You want to hire agents like someone would hire employees at a bootstrapped company. You don't hire five people all at once." | same transcript | ~00:14:40–00:14:50 | VERIFIED — grep-matched verbatim ("for the sake of having agents" confirmed via grep) |
| 6 | "A skill is an infinite game. It's not a finite game. You don't finish making a skill, you start a skill, and you keep improving it over time." | same transcript | ~00:18:59–00:19:06 | VERIFIED — grep-matched verbatim |
| 7 | "unlike a solopreneur, she can't just tell Claude Code, 'Don't make mistakes.' She might need to fully isolate each one of these data sets and create a unique set of hooks, Claude MDs, for each and every domain." | same transcript | ~00:20:34–00:20:45 | VERIFIED — grep-matched verbatim |
| 8 | Amazon Bedrock named for confidential law-firm data | same transcript | ~00:18:19 | VERIFIED — confirmed present in `extraction-brief.md` "Observed Spoken Claims" list, cross-checked against transcript context around 00:18:19 |
| 9 | Video title "Build Your Agentic OS Better Than The 99%", channel Mark Kashef, published 2026-05-09, 22:31 runtime | `extractions/mark-kashef-perfect-agentic-os-kit/extraction-brief.md` | Source Evidence section | VERIFIED — read directly |
| 10 | Build-Shape Verdict: "Build as a Codex skill system companion, not a duplicate Mark Kashef expert" | `extractions/mark-kashef-perfect-agentic-os-kit/extraction-brief.md` | Build-Shape Verdict section | VERIFIED — read directly |
| 11 | Validation date 2026-05-10, "5 example data maps validated", "7 checks" passed | `extractions/mark-kashef-perfect-agentic-os-kit/validation-report.md` | Status + Validation Commands table | VERIFIED — read directly |
| 12 | Component Order steps 1-8 (Audit -> Classify -> Interview -> Assemble -> Render -> Render OPPORTUNITIES -> Render handoff -> Checkpoint) | `skills/mark-kashef-silver-platter-agentic-os/SKILL.md` | Component Order section | VERIFIED — read directly, already-passing content, unmodified |
| 13 | `references/prompts-v2/*.md` all six carry Output Contract + Quality Gate sections already | `skills/mark-kashef-silver-platter-agentic-os/references/prompts-v2/*.md` | all 6 files | VERIFIED — grepped directly, confirmed pre-existing (not touched by this repair) |
| 14 | Visual/on-screen text (e.g. any UI labels shown in the video) | `extractions/video-context/-WCNwxz3uoM/uncertainty-report.md` | full file | UNCONFIRMED by design — the extraction brief itself states "Frame extraction was skipped because the requested source preservation used transcript mode... Visual claims must not be treated as observed." No visual/OCR claim is made anywhere in this repair; this row exists to document the boundary, not to anchor a claim. |

## Files touched this repair

- `genius.md` — new file (did not exist before this repair). Every quote/timestamp above is VERIFIED against `extractions/video-context/-WCNwxz3uoM/transcript.txt`.
- `workflows/audit-and-classify.md`, `workflows/assemble-and-render-data-map.md`, `workflows/opportunities-and-handoff.md` — new files (no `workflows/` directory existed before this repair). Content derives from already-shipped `references/prompts-v2/*.md` files (VERIFIED, read directly) and `SKILL.md` Component Order (VERIFIED, unmodified).
- `SKILL.md`, `references/prompts-v2/*.md`, `references/archetypes.md`, `references/genius-patterns.md`, all `examples/`, `scripts/`, and `bridges-source-command-silver-platter.SKILL.md` — **not modified**. Passing content preserved per envelope's additive-first rule.
