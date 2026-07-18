# Rachel Woods — Source Ledger

Every source consulted for this repair pass, labeled VERIFIED / LIKELY / UNCONFIRMED
per claim. Ground truth = `extractions/rachel-woods/` (3 raw transcripts, no timestamps
in the source files — locators below are word-position, not clock time). All file
sizes confirmed by direct read, not assumed.

## Sources Consulted

| File | Size | Role |
|---|---|---|
| `extractions/rachel-woods/transcript-v1-ai-operations.txt` | 48,875 bytes (~9,178 words) | Primary — "AI Operations" interview |
| `extractions/rachel-woods/transcript-v2-ai-first-company.txt` | 45,596 bytes (~8,592 words) | Primary — "AI-First Company" interview |
| `extractions/rachel-woods/transcript-v3-high-paying-ai-job.txt` | 53,713 bytes (~10,242 words) | Primary — "High-Paying AI Job" interview |
| `extractions/rachel-woods/extraction-report.md` | 17,434 bytes | Secondary — MES 3.0 synthesis document built from the three transcripts above; its own quoted blocks are the extractor's paraphrase/reconstruction, not independently verified against transcript text by this repair pass unless noted below |

## Claim-by-Claim Labels

### Anti-Patterns (genius.md, new section)

| Claim | Label | Basis |
|---|---|---|
| "tinkering with it, random acts of ai" caps gains at "~30% more productive" | VERIFIED | Exact substring match in transcript-v2-ai-first-company.txt (confirmed via direct text search, offset 2496 and 2576) |
| "the problem with that is that you're not building something that's like reusable in the future" | VERIFIED | Exact substring match in transcript-v1-ai-operations.txt (offset 38783) |
| "One of the most common pitfalls is people will have that implement role also be the AI operator role" + "so in the technical weeds and details that they might miss out on the process" | VERIFIED | Exact substring match in transcript-v3-high-paying-ai-job.txt (offset 240 and 358 — this is literally the cold-open of the video) |
| "creatively, spontaneously creating stuff randomly outta your brain" + "someone else could leverage" | VERIFIED | Exact substring match in transcript-v1-ai-operations.txt (offset 42127 and 42371) |
| "AI shouldn't just be something you're trying to like catch up on all the time. You should feel like you're winning because you're using ai" | VERIFIED | Exact substring match in transcript-v2-ai-first-company.txt (offset 15742 and 15821) |
| "Process Before Prompts" as the single most expensive AI-adoption mistake | LIKELY | This is the extraction-report.md author's synthesis label (Layer 3 §7) built across all three transcripts' recurring "map the process first" theme. Searched all three transcripts for the report's exact quoted sentence ("The biggest mistake companies make is starting with the AI...") — **not found verbatim in any transcript**. The underlying sequencing claim (process → decision points → quality bar → AI) is well-supported by the transcripts' repeated content, but the specific sentence as quoted in extraction-report.md is a paraphrase/reconstruction, not a literal transcript quote. Labeled LIKELY, not VERIFIED, and flagged as such inline in genius.md. |

### Pre-existing genius.md content (not modified this pass, inherited as-is)

| Claim | Label | Basis |
|---|---|---|
| "Your AI Edge is the intersection of your unique expertise, your unique data, and a process that would be impossibly expensive to do manually." (extraction-report.md blockquote) | UNCONFIRMED | Not independently re-verified against transcript text this pass — carried over from the prior extraction without re-audit. Flagging honestly rather than assuming it is verbatim. |
| "AI doesn't save you time. AI gives you unlimited time..." (extraction-report.md blockquote) | UNCONFIRMED | Same — not re-verified this pass. The underlying "unlimited time" concept IS heavily attested in all three transcripts (dozens of hits), but this specific quoted sentence was not re-confirmed verbatim. |
| "Most companies see about a 30% productivity improvement from AI. That's the ceiling..." (extraction-report.md blockquote) | LIKELY | Directionally matches transcript-v2's "you're probably about like 30% more productive than you are without it" but is not a verbatim match — a compressed paraphrase. |
| Rachel Woods bio facts (founder of The AI Exchange, Divvy Up, ex-Facebook R&D/ads-ranking data scientist) | VERIFIED | Stated directly by the interview hosts and by Rachel herself in transcript-v1-ai-operations.txt (opening ~200 words) and transcript-v3-high-paying-ai-job.txt (opening ~200 words) |
| 47-step client onboarding case study, boutique investment firm case study (genius.md Hall of Fame Exemplars) | UNCONFIRMED | These are composite/illustrative exemplars built by the original extraction to demonstrate pattern application — not claims about a specific real company verified in the transcripts. Treat as illustrative, not factual case history. |

## What This Repair Pass Did Not Re-Verify

Per the "no invented provenance" rule, this pass only re-verified the six new
anti-pattern quotes added to genius.md (all VERIFIED via direct substring search,
shown above) and the one new LIKELY-labeled synthesis claim. It did NOT re-audit
every pre-existing quote and case study already in genius.md/references/ — those
are inventoried above with an honest UNCONFIRMED/LIKELY label rather than a false
VERIFIED, since re-confirming them was out of scope for this repair (see
REPAIR-NOTES.md gap note).
