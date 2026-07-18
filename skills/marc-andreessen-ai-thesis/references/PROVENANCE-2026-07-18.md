# PROVENANCE — marc-andreessen-ai-thesis repair (Wave 3 Lane 4 Batch 10)

Anchor → source file + location. All quotes verbatim from
`extractions/marc-andreessen/transcript.txt` (137,689 bytes, `wc -c`
confirmed), the Lenny Rachitsky interview transcript named as this skill's
ground truth in `SKILL.md` line 11.

| Anchor (in genius.md) | Source location | Verbatim text |
|---|---|---|
| Anti-Pattern #1 ("wrong frame") | transcript.txt, ~char offset located via `grep -o '.\{300\}kind of the wrong frame.\{400\}'` | "a lot of people in the industry have kind of what I would describe as this one-dimensional thing which is okay as a result of the technology not working AI just kind of sweeps sweeps the world and changes everything. And I think that's that's kind of the wrong that's kind of the wrong frame." |
| Anti-Pattern #2 (task loss) | transcript.txt, located via `grep -o '.\{200\}task loss.\{300\}'` | "Everybody wants to talk about job loss but really what you want to look at is task loss. The job persists longer than the individual tasks." |
| Anti-Pattern #3 (indeterminate optimism) | transcript.txt, located via `grep -o '.\{150\}indeterminate.\{200\}'` + full search around "Peter Teal formulation" | "Silicon Valley is characterized by in too much what he calls indeterminant optimism" + "what the world needs more is determinant optimists which are people who are like no the world is going to be better because I'm going to do this specific thing." Correction made during this repair: an initial draft misread a later, more nuanced line ("I would put myself firmly on the side of the indeterminate optimist") as Andreessen self-identifying as determinate — re-reading the full passage shows he places *himself as a VC* on the indeterminate side and reserves the determinate-optimist requirement for *founders*. Fixed before delivery; see source-ledger.md. |
| Anti-Pattern #4 (media middle) | transcript.txt, located via `grep -o '.\{200\}barbell.\{400\}'` | "I always describe it as I have like a almost a perfect barbell strategy... it's sort of everything in the middle I'm always like much more skeptical about." |
| Anti-Pattern #5 (moat/open source) | transcript.txt, located via full-text search from "is there a moat" | "within within a year of GPT3 coming out, there were their open source GP3s running on a fraction of the hardware, right? That were available for free." |
| Anti-Pattern #6 (panic/demographics) | transcript.txt, opening lines | "If we didn't have AI, we'd be in a panic right now about what's going to happen to the economy... in the face of declining population growth." |
| Model Calibration section, self-deprecation texture note | transcript.txt, located via `grep -o '.\{150\}mistake.\{150\}'` | "I should start by saying I've been wrong about tons of things, but you know, I buried those out back behind the shed." |
| Hidden Knowledge #7 provenance flag | full-text search: "flat earth", "illiterate", "learn to read" — all 0 matches in transcript.txt | No verbatim source located. See `references/source-ledger.md`. |
| Hidden Knowledge #5 flag ("curiosity") | full-text search: "curiosity" — 0 matches | No verbatim source located. See `references/source-ledger.md`. |
| Hidden Knowledge #6 flag ("wetware", "40,000 years") | full-text search — 0 matches | No verbatim source located. See `references/source-ledger.md`. |

## Method

All quotes located by direct `grep -o` context-window search and Python
substring search against the raw transcript file (not paraphrased from
memory, not pulled from genius.md's pre-existing prose). File sizes recorded
via `wc -c` before any claim of source absence — no "unrecoverable/0-byte"
claims made anywhere in this repair.
