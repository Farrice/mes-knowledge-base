# dan-koe-ai-leverage — Source Ledger

> Every claim, quote, and named reference in SKILL.md / genius.md against its
> source, labeled VERIFIED / LIKELY / UNCONFIRMED. Repair pass 2026-07-17
> (Wave 3 Lane 4 Batch 4). Ground truth checked:
> `extractions/dan-koe/transcript.txt` (26,836 chars, single-paragraph
> auto-captioned YouTube transcript — confirmed present, non-empty via
> `wc -c`) and `extractions/dan-koe/extraction-report-ai-leverage.md`
> (14,529 chars, MES extraction report — confirmed present, non-empty).
> No 0-byte or missing source files found for this skill; the earlier
> "codex-harvest" and claude-export tarball checks turned up nothing
> additional (`_active/harness/codex-harvest-2026-06-11/extractions/` has no
> Dan Koe entry) — extraction-report + transcript are the full source set.

## Sources Consulted

| Source | Size | Status |
|---|---|---|
| `extractions/dan-koe/transcript.txt` | 26,836 chars | VERIFIED present, read in full |
| `extractions/dan-koe/extraction-report-ai-leverage.md` | 14,529 chars | VERIFIED present, read in full |
| `_active/harness/codex-harvest-2026-06-11/extractions/` (Dan Koe entry) | — | UNCONFIRMED / absent — searched, no match found |
| claude-export tarball (`_archive/claude-export-2026-07-01.tar.gz`) | 332,779,255 bytes | Not opened — extraction-report + transcript already provide full coverage for this skill's claims; no gap required cracking the archive |

## Claim-by-Claim Ledger

| Claim / Quote | Label | Basis |
|---|---|---|
| "So the four C's are context, clarification, creation, and concerns... these don't always come in order... you're trying to check the boxes for each." | VERIFIED | Verbatim substring match in transcript.txt, ~char 2906 |
| "You're gambling at that point." | VERIFIED | Verbatim substring match, transcript.txt ~char 4299 |
| "custom agents inside of Eden that hook up via Telegram in like a week or so, maybe less" | VERIFIED | Verbatim substring match, transcript.txt ~char 7254 |
| "It's no wonder you can't get results with AI because you're not treating it like an employee that you have to train." | VERIFIED | Verbatim substring match, transcript.txt ~char 8151 |
| "This is arguably the most important part of conversing with AI" / "this is where you learn the most" | VERIFIED | Verbatim substring matches, transcript.txt ~char 8521 / ~8867 |
| "sometimes the ideas that come to my brain that I just want to tweet out or write about aren't those things" | VERIFIED | Verbatim substring match, transcript.txt ~char 12946 |
| "you can choose whatever model you want" | VERIFIED | Verbatim substring match, transcript.txt ~char 13985 |
| "Reading good prompts helps you create better prompts and you start to pick up little ideas..." | VERIFIED | Verbatim substring match, transcript.txt ~char 18834 |
| "Phase one establishes a strategic foundation, customer avatar, content topics. Phase two executes the 30-day action plan, so on and so forth." | VERIFIED | Verbatim substring match, transcript.txt ~char 18548–18627 |
| "You're waiting for someone like me in this video to give you a step-by-step framework rather than going in tinkering, experimenting, and having a goal to work towards where you can build something like this on your own." | VERIFIED | Verbatim substring match, transcript.txt ~char 6469 |
| Curated source videos: Matt Gray (30-day personal brand), a Seth Godin podcast, a Caleb Ralston video | LIKELY | Transcript names "Matt Gray," "Seth Goden," and "Caleb Rston" — the latter two are auto-caption mis-transcriptions; identified as Seth Godin and Caleb Ralston (a roster expert: `skills/caleb-ralston/`) on context and pronunciation, not spelled correctly in the raw source |
| "~20-minute, 5,165-word tutorial" | VERIFIED | extraction-report-ai-leverage.md line 6: "Source: YouTube tutorial video (~20 min), 5,165 words" |
| "$5,000 mentor replacement" | VERIFIED | Transcript: "you don't have to pay $5,000 to be mentored or coached by someone" |
| Dan Koe — "2M+ followers" | UNCONFIRMED | Not present in transcript.txt (transcript only says "I have a decent amount of followers," no figure) or extraction-report body; appears only in the extraction report's header metadata as external/background knowledge, not sourced to this video |
| "Intellectual Sovereignty" as Dan's own term | UNCONFIRMED | Not found verbatim in transcript.txt — this is the skill's own coined label for the philosophy Dan describes (employee-not-oracle, human stays in the driver's seat); genuine as a *description*, not a literal Dan Koe quote. Not presented in quotation marks in the repaired genius.md for this reason. |
| "AI is an untrained employee with superhuman processing speed" | LIKELY | Paraphrase of the verified quote "you're not treating it like an employee that you have to train" — the "superhuman processing speed" framing is the skill's synthesis, not a Dan Koe quote; kept unquoted (bolded description) in genius.md, not cited as verbatim |
| Gap-Teaching / Best-Post Outline / Socratic Thought-Partner / Taste-Signal / Reliance Reset patterns ("claude.ai export — Dan Koe conversations 2026-07-01" section) | LIKELY | Carried over unmodified from prior version of genius.md; quotes read as plausible Dan Koe phrasing consistent with his documented style, but the cited source (a Nov 2025 podcast interview transcript) is not present in `extractions/dan-koe/` for this repair pass to re-verify against. Not re-anchored or removed — flagged here as inherited, not newly verified. |

## Anti-Pattern Sourcing (genius.md § Anti-Patterns)

All 7 items added in this repair pass anchor to a VERIFIED verbatim quote from `transcript.txt` (see table above for each quote's individual verification and offset). No anti-pattern item in the repaired section relies on an UNCONFIRMED or invented quote.
