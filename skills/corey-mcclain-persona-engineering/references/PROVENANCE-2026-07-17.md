# PROVENANCE — corey-mcclain-persona-engineering repair

Anchor → source file + location. All quotes verified verbatim via `grep -F` against
`extractions/corey-mcclain/transcript.txt` (29,994 bytes, confirmed with `wc -c` —
the sole extraction source for this expert) before use.

| Anchor (as written in repaired files) | Source | Location |
|---|---|---|
| "if thinking about it as a layer is not helpful, it may be more helpful to think about it as a container" | transcript.txt | Persona-as-container passage (mid-transcript, after "It sits on top of everything...") |
| "the thing about setting these up in workspaces is the fact that they just get better, right?" | transcript.txt | Steady-state vs. transistory passage |
| "I can take two different people with two different world views and give them the same problem and the results you get will be completely different, they're going to reach completely different audiences" | transcript.txt | Worldview-implies-decisions passage |
| "Maybe it's the first thing it references, maybe it's the last thing it references. That's your choice." | transcript.txt | Router-integration / two-install-methods passage |
| "quality control every single time" | transcript.txt | Library-layer passage (source contains a transcription artifact rendering "few-shot" as "fot" — quote uses only the clean surrounding clause) |
| "not the memory that Open AI, Claude or Gemini gives you, but your own personal memory base with its own tagging system" | transcript.txt | Memory-layer definition passage |
| "It's almost like a booster pack that just improves the performance of the logic in the library." | transcript.txt | Persona-layer definition passage |
| "created in 60 seconds with zero planning" (Aar Vance freestyle timing) | pre-existing genius.md, Hall of Fame Exemplar 2 | Already-shipped skill content; cross-checked against transcript's Transistory Freestyle description |
| "$6,500 floral-print dress" / Prada.com | transcript.txt | Prada Principle / luxury-restraint passage |
| "a dress to women 25 to 35" | transcript.txt | Marketing-asset task framing (both vanilla and Vance runs) |
| "I've deleted both conversations so that we can't be tainted by the image that was generated" | transcript.txt | Controlled Delete / clean-room testing passage |
| "the logic, the library are obviously more important than anything else... then the memory and then finally the personality profile was installed on top of that" | transcript.txt | LLMP build-order passage |
| "Not act as a social media manager, not act as a YouTube channel manager, not act as a business consultant, but actually this is who you are" | transcript.txt | Identity-vs-role-play passage |
| "Claw never talks about his personality when it responds to you" | transcript.txt | Persona-leakage / Claude-as-reference passage (source transcription renders "Claude" as "Claw"/"Clawude" — a transcription artifact, not an invented name) |
| "The persona document is NEVER compressed... compressing it destroys the container effect." | `skills/corey-mcclain-persona-engineering/workflows/mcclain-nate-full-agent.md`, Step 5 | Pre-existing skill content — in-skill cross-reference, not an expert quote |
| "if I was creating a persona for a marketing agent, then that persona would be generated in a fashion that the marketing assets... is going to appeal to that audience" | transcript.txt (also pre-existing genius.md Hidden Knowledge #6) | Worldview-audience-alignment passage |
| 17 Output Schema sections | Each workflow's own pre-existing internal templates (Report Template, Construct Assembly, Identity Profile Assembly, Architecture Presentation, Voice Integration template, BELIEF/IMPLIES/TESTS-AS template, etc.) | Structural restatement of already-shipped step content, not new invented claims — see `REPAIR-NOTES.md` for per-file mapping |

## Absence Claims

None made. Single-source expert (`ls extractions/ | grep -i mcclain` → one directory,
one 29,994-byte file, fully read). No "source unrecoverable" or "0-byte" claim appears
anywhere in this repair.
