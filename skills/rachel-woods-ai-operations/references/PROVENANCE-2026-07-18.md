# PROVENANCE — rachel-woods-ai-operations repair

Anchor → source file + location. All offsets are Python `str.find()` character
offsets into the raw `.txt` file, confirmed by direct read (no timestamps exist
in these transcripts — they are plain auto-transcribed text).

| Anchor (genius.md "Anti-Patterns (Sourced)") | Source file | Char offset | Verbatim confirmed |
|---|---|---|---|
| "tinkering with it, random acts of ai" | transcript-v2-ai-first-company.txt | 2496 | Yes — direct substring match |
| "you're probably about like 30% more productive than you are without it" | transcript-v2-ai-first-company.txt | 2576 | Yes |
| "the problem with that is that you're not building something that's like reusable in the future" | transcript-v1-ai-operations.txt | 38783 | Yes |
| "One of the most common pitfalls is people will have that implement role also be the AI operator role" | transcript-v3-high-paying-ai-job.txt | 240 (cold-open) | Yes |
| "your implementation person is going to be so in the technical weeds and details that they might miss out on the process" | transcript-v3-high-paying-ai-job.txt | 358 | Yes |
| "creatively, spontaneously creating stuff randomly outta your brain" | transcript-v1-ai-operations.txt | 42127 | Yes |
| "someone else could leverage" | transcript-v1-ai-operations.txt | 42371 | Yes |
| "AI shouldn't just be something you're trying to like catch up on all the time" | transcript-v2-ai-first-company.txt | 15742 | Yes |
| "You should feel like you're winning because you're using ai" | transcript-v2-ai-first-company.txt | 15821 | Yes |
| "Process Before Prompts" / prompt-first-sequencing claim | extraction-report.md, Layer 3 §7 | n/a (synthesis doc) | No — searched all 3 transcripts for the report's exact quoted sentence, not found verbatim; labeled LIKELY in source-ledger.md, not treated as a verbatim anchor |

## File sizes (confirmed by direct `ls -la` / `du -sh`, not assumed)

- `extractions/rachel-woods/extraction-report.md` — 17,434 bytes
- `extractions/rachel-woods/transcript-v1-ai-operations.txt` — 48,875 bytes (~9,178 words)
- `extractions/rachel-woods/transcript-v2-ai-first-company.txt` — 45,596 bytes (~8,592 words)
- `extractions/rachel-woods/transcript-v3-high-paying-ai-job.txt` — 53,713 bytes (~10,242 words)

All four files read directly this session — none absent, none 0-byte, no
"unrecoverable" claim made anywhere in this repair.
