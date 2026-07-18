# dan-koe-ai-leverage — Repair Provenance

Anchor → source file + location, for every new claim/quote added in this repair
pass (2026-07-17, Wave 3 Lane 4 Batch 4). Pre-existing content (unchanged) is
not re-listed here; see `references/source-ledger.md` for the full
claim-by-claim table including inherited content.

| Anchor (in repaired genius.md) | Source | Location |
|---|---|---|
| "So the four C's are context, clarification, creation, and concerns..." | extractions/dan-koe/transcript.txt | ~char 2906 (verified via `str.find`) |
| "You're gambling at that point." | extractions/dan-koe/transcript.txt | ~char 4299 |
| "custom agents inside of Eden that hook up via Telegram in like a week or so, maybe less" | extractions/dan-koe/transcript.txt | ~char 7254 |
| "It's no wonder you can't get results with AI because you're not treating it like an employee that you have to train." | extractions/dan-koe/transcript.txt | ~char 8151 |
| "This is arguably the most important part of conversing with AI" | extractions/dan-koe/transcript.txt | ~char 8521 |
| "this is where you learn the most" | extractions/dan-koe/transcript.txt | ~char 8867 |
| "sometimes the ideas that come to my brain that I just want to tweet out or write about aren't those things" | extractions/dan-koe/transcript.txt | ~char 12946 |
| "you can choose whatever model you want" | extractions/dan-koe/transcript.txt | ~char 13985 |
| "Reading good prompts helps you create better prompts and you start to pick up little ideas..." | extractions/dan-koe/transcript.txt | ~char 18834 |
| "Phase one establishes a strategic foundation... Phase two executes the 30-day action plan, so on and so forth." | extractions/dan-koe/transcript.txt | ~char 18548–18627 |
| "You're waiting for someone like me in this video to give you a step-by-step framework rather than going in tinkering..." | extractions/dan-koe/transcript.txt | ~char 6469 |
| "~20-minute, 5,165-word tutorial" | extractions/dan-koe/extraction-report-ai-leverage.md | line 6 ("Source: YouTube tutorial video (~20 min), 5,165 words") |
| Curated sources: Matt Gray, Seth Godin (transcript: "Seth Goden"), Caleb Ralston (transcript: "Caleb Rston") | extractions/dan-koe/transcript.txt | ~char 7900–8050 (names appear together) |
| "Score 4 (Acceptable) / Score 7 (Good) / Score 10 (Savant)" rubric anchors | skills/dan-koe-ai-leverage/references/quality-rubric.md | table header row, "Score 4 (Acceptable)" / "Score 7 (Good)" / "Score 10 (Savant)" columns |

## Verification Method

All quote anchors were confirmed with an exact Python substring search
(`quote in open(transcript_path).read()`) against
`extractions/dan-koe/transcript.txt` before being written into genius.md.
Character offsets are from `str.find()` on that read and are approximate
locators for a human/adversarial reviewer to re-find the passage quickly —
the transcript file itself is a single unbroken paragraph (0 newlines,
confirmed via `wc -l`), so there are no line numbers to cite instead.

Two quotes present in the *prior* version of genius.md/quality-rubric.md
were checked and found NOT verbatim in transcript.txt:
- "If you don't have taste and preferences, AI is going to suck." — not
  found; likely a paraphrase/invention. NOT carried into the repaired
  Anti-Patterns section.
- "The Knowledge Alchemy Pipeline has 3 stages for a reason." — not a
  Dan Koe quote (it's the skill's own architecture description); left
  unquoted where it appears in inherited content, not re-anchored as a
  a source quote.
These are flagged, not deleted (additive-first / minimal-touch per the
envelope) — the pre-existing "Anti-Patterns: What Dan Koe Would Never Do"
section in `references/quality-rubric.md` (not genius.md, so not itself
audited) was left as-is; only genius.md was edited, using freshly
re-verified quotes rather than reusing the rubric file's unverified ones.
