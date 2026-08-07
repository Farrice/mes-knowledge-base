# PROVENANCE — sam-parr-copywriting-mechanics repair

Anchor → source file + location, for every new claim/quote added this pass. Full claim-by-claim labels live in `references/source-ledger.md`; this table is the quick anchor→location index the envelope asks for.

| Anchor (as written in genius.md) | Source File | Location |
|---|---|---|
| "You're reading this not because you want to..." | `extractions/sam-parr/transcript.txt` | First ~250 bytes of file (opening line) |
| "Good copywriting means getting what's in my head into yours..." | `extractions/sam-parr/transcript.txt` | Early in file, "Tweet number two" quote (immediately after the interview's opening bio voiceover) |
| "Story, story, story, story..." | `extractions/sam-parr/transcript.txt` | Mid-file, host's question "what's the one change that would most improve most people's copy" |
| "Did you know that there's more Ecoli..." | `extractions/sam-parr/transcript.txt` | Mid-file, Tupperware/Caraway live-rewrite segment, one line after "I'm going to make up all the details" |
| "Nightly Rest is within arms reach." | `extractions/sam-parr/transcript.txt` | Mid-file, AGZ sleep-supplement weak-ad segment |
| "No one will read this or watch this. This is too long..." | `extractions/sam-parr/transcript.txt` | First ~350 bytes of file, host's opening objection |
| "everything I just said was fake. I don't know if that's true." | `extractions/sam-parr/transcript.txt` | End of the AGZ live-rewrite segment |
| "He doesn't say they're waterproof..." | `extractions/sam-parr/transcript.txt` | Objection-handling segment, shoe-anecdote example |
| "write drunk and edit sober" / "I'm a [ __ ] writer. I'm a great editor." | `extractions/sam-parr/transcript.txt` | Editing-discipline segment, "cut a third" discussion |
| "testing the water with jokes..." | `extractions/sam-parr/transcript.txt` | Opening dating-story segment (chickpea/lentil anecdote) |
| `00:00:41`, `00:01:01`, `00:01:19`, `00:35:17`, `00:02:26`, `00:11:50`, `00:03:01`, `00:04:24` (Genius Patterns 1–4, spot-checked) | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/uf4fR3qcDkU/transcript.txt` | Timestamped raw-caption lines matching each anchor; e.g. `00:01:01.270`–`00:01:01.280` = "Tweet number two. Good copywriting means getting what's in my head into..." |
| Evidence limit (transcript-only, no visual/OCR) | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/uf4fR3qcDkU/ocr-notes.md`, `frame-notes.md`, `uncertainty-report.md` | Full file contents (each under 2.5 KB) |
| Sam Parr bio (Hustle founder, MFM co-host) | `extractions/sam-parr/transcript.txt` | First ~450 bytes, interview's own intro voiceover |

## The predecessor's real source, confirmed

The dispatch note said a predecessor worker had located "a real timestamped transcript source" in the archive before being killed mid-task. That source is `_active/harness/codex-harvest-2026-06-11/extractions/video-context/uf4fR3qcDkU/transcript.txt` (265,316 bytes, 3,988 timestamped rolling-caption rows, format `[HH:MM:SS.mmm] <text>`). It is real, not a stub — confirmed via `wc -c` and direct read. It is the origin of the `00:MM:SS`-style anchors already present in genius.md's Genius Patterns section (pre-existing content, not authored this pass). It lives outside canonical `extractions/` (under a Codex-harvest staging directory), which is why SKILL.md already carries an accurate "NOT YET PORTED" caveat. This repair did not port it — that's a canonical-`extractions/` write, out of scope for an output-directory-only repair — but did spot-check 8 of its timestamp anchors against the corresponding genius.md patterns; all 8 checked out.
