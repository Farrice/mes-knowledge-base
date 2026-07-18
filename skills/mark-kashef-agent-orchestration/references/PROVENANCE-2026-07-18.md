# Provenance — mark-kashef-agent-orchestration repair

Anchor → source file + location. Every row is a claim newly added by
this repair to `genius.md`. Pre-existing content is not re-listed here
(see `references/source-ledger.md` for its honest labels).

| # | Anchor (as it appears in `genius.md`) | Source file | Location in source |
|---|---|---|---|
| 1 | "If you just say spawn agents, it could get confused between sub agents, which are very different in the way they work versus agent teams." | `extractions/mark-kashef/transcript.txt` | ~char offset 1690, opening third of the transcript (right after "the most important magic words you always need to say is create an agent team or spawn an agent team") |
| 2 | "the rule of thumb, by the way, from anthropic is three to five agents is the sweet spot. Anything beyond that can lead to diminishing returns, overengineering, overthinking, and most importantly, a huge consumption of tokens." | `extractions/mark-kashef/transcript.txt` | ~char offset 8570-8720, pitch-deck use-case section, right after the three agents (researcher/slidewriter/designer) spin up |
| 3 | "Looks decent, but still AI... it's not completely AI slop, but you could desopify it with the right instructions." | `extractions/mark-kashef/transcript.txt` | ~char offset 22818-23090, marketing-campaign use-case, Kashef reviewing the generated email sequence |
| 4 | "it might make more sense to maybe spin up sub agents to make edits in parallel since they don't need to speak to each other if you can identify independently what needs to change." | `extractions/mark-kashef/transcript.txt` | ~char offset ~5250 area, content-repurposing use-case, discussing post-delivery edits |
| 5 | "the less thinking you have to make cloud code do, the more accurate the results." | `extractions/mark-kashef/transcript.txt` | ~char offset 7600-7620, pitch-deck use-case, right after "Now this is overkill. It would figure it out on its own." |
| 6 | "invoke[s] what's called the ask user input tool" / "approve as is, approve with notes, or reject with some rework" | `extractions/mark-kashef/transcript.txt` | ~char offset 7804-8300, pitch-deck use-case, Human Tollbooth walkthrough |
| 7 | "150,000 tokens" | `extractions/mark-kashef/transcript.txt` | ~char offset 9397, pitch-deck use-case, post-build token count |
| 8 | "180,000 tokens" | `extractions/mark-kashef/transcript.txt` | ~char offset 13622, RFP use-case, post-build token count |
| 9 | "you can always hover over this URL, click it, open up this pitch deck" | `extractions/mark-kashef/transcript.txt` | pitch-deck use-case, immediately after the token-count line above |
| 10 | "It's not going to be absolutely beautiful, but it's respectable" | `extractions/mark-kashef/transcript.txt` | pitch-deck use-case, Kashef's quality verdict on the finished deck |
| 11 | Model-Calibration texture cues: "TLDDR," "let's dive in" | `extractions/mark-kashef/transcript.txt` | opening lines of the transcript (video intro) |
| 12 | Provenance notes flagging "Circuit Breaker Architecture" / "Quality Tripwires" / "Blast Radius Containment" as absent from source | `extractions/mark-kashef/transcript.txt` + `extractions/mark-kashef/extraction-report.md` | negative result — confirmed via `grep -in "circuit breaker\|tripwire\|checkpoint\|blast radius\|degradation\|fallback"` returning zero hits in both files |
| 13 | Provenance note on the "Monolithic Prompt Failure" Anti-Exemplar (not a verbatim Kashef line) | `extractions/mark-kashef/transcript.txt` | negative result — the exact prompt snippet string is not present; confirmed by direct search |
| 14 | Provenance note on the "claude.ai export" section (2026-07-01) | `_archive/claude-export-2026-07-01.tar.gz` | file exists, 332,779,255 bytes, not re-opened this pass — size recorded, absence of re-verification stated honestly |

Anti-Pattern date anchor ("2026-03-02"): `git log -1 --format=%ad --
extractions/mark-kashef/transcript.txt` → `Mon Mar 2 04:36:56 2026
-0800` (commit-add date, not a claimed video-publish date).
