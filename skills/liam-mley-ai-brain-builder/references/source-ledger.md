# Source Ledger — liam-mley-ai-brain-builder

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 9). Every claim added or
retained in `genius.md` and the workflow files labeled VERIFIED /
LIKELY / UNCONFIRMED against what was actually found on disk (plus
one live web check, logged below, used only to resolve the
name-spelling question — no other external research was run).

## Search performed (absence verified, not assumed)

Per the envelope's rule 2 ("a claim that sources are ABSENT is itself
a provenance claim"), the following searches were run and results
recorded with real file sizes:

- `ls extractions/ | grep -i liam` / `grep -i mley` / `grep -i ottley`
  → 0 direct hits on "liam"/"mley" as a folder name; `extractions/ai-brain-os/`
  is the actual folder name (topic-named, not name-named) and is the
  primary source — found via a broader `grep -ril "AI Brain\|AIOS" extractions/`
  sweep, not the name search.
- `grep -ril "liam mley" --include="*.md" .` (repo-wide, excluding
  `.claude/worktrees/`) → hits in `AGENT_INDEX.md`, `SKILL_INDEX.md`,
  `SLASH_COMMANDS.md` (auto-generated registries pointing back at this
  skill) and `_active/codex-harvest-2026-06-11/agents/liam-mley/AGENT.md`
  (a duplicate persona card, same claims, no independent sourcing).
- `grep -ril "liam ottley" --include="*.md" .` → hits are all for the
  **sibling skill** `liam-ottley-linkedin-lead-magnet` (different topic,
  LinkedIn lead-gen, NOT touched by this repair) plus one video-context
  folder (`extractions/video-context/3iR3kHxCwfo/`) that is about a
  *different* Liam Ottley video (LinkedIn content), not AIOS — read and
  ruled out as a source for this skill.
- `find extractions -iname "*mley*"` / `*ottley*` / `*liam*` → 0 results
  under `extractions/` proper (the transcript folder is topic-named).

## Files consulted (real, on-disk, sized)

| File | Size (bytes) | What it is |
|---|---|---|
| `extractions/ai-brain-os/transcript.txt` | 20,268 | **Primary source.** Full verbatim transcript of a ~20-min YouTube talk on "AI Operating Systems," speaker self-identifies (per transcript) as "Leam Mley," 4 companies (agency/media/education/SaaS), New Zealand dollars mentioned. This is the source every quote in this repair is drawn from. |
| `extractions/ai-brain-os/extraction-report.md` | 10,847 | Mastery Extraction report derived from the transcript above (8 Genius Patterns, 6 Hidden Knowledge items). Internally consistent with the transcript except one compression flagged below (line 61, the "$1M in 7 days" framing). |
| `skills/liam-mley-ai-brain-builder/SKILL.md` | ~1,800 (unread-modified, baseline) | Current skill card — not modified by this repair. |
| `skills/liam-mley-ai-brain-builder/genius.md` | ~9,200 (baseline, pre-repair) | Baseline genius file this repair extends. |
| `_active/codex-harvest-2026-06-11/agents/liam-mley/AGENT.md` | ~4,700 | Duplicate persona card; same claims as genius.md, no independent citations — corroborates the extraction's own framing but adds no new source. |

## Live web check (2026-07-18, one query, used only for identity resolution)

The transcript's self-identification ("my name is Leam Mley") does not
match any known public figure. The content is highly specific and
independently checkable: 4 businesses (AI consulting/dev agency +
media company + education/info business + AI SaaS), the "AIOS"
5-layer framing, a free live "AIOS Blueprint" workshop with a 7-day
roadmap, Claude Code as the build tool marketed as requiring no
coding, and New Zealand dollars in the revenue claim (implying an NZ
speaker). A single web search ("Liam Ottley AI Operating System AIOS
four companies agency media education SaaS Claude Code") returned
`aios.liamottley.com` (a live "AIOS Blueprint" free workshop page) and
independent write-ups describing Liam Ottley as a New Zealand-based
founder of Morningside AI (AI Automation Agency model) plus an
education arm (AAA Accelerator) — matching the transcript's business
mix point-for-point.

**Conclusion**: "Liam Mley" is LIKELY an ASR (automatic speech
recognition) mis-transcription of **Liam Ottley** — the transcript
file itself was almost certainly auto-generated from audio and never
corrected. This is a naming-accuracy finding, not a content-accuracy
one: the quotes, numbers, and methodology in this repair are drawn
directly from the transcript file as it exists on disk, so they are
VERIFIED as file content regardless of the speaker-name question. This
repair does NOT rename the skill or fold it into the sibling
`liam-ottley-linkedin-lead-magnet` skill — that is a scope decision for
the conductor, not this worker (envelope: "touch ONLY yours").

## Claim-by-claim labels

| Claim | Label | Basis |
|---|---|---|
| The 5-Layer AIOS Architecture (Context → Data → Intelligence → Automate → Build), in that order | VERIFIED | Verbatim sequence in `extractions/ai-brain-os/transcript.txt`: "let me walk you through these five different layers. The first layer is context... The second layer is data... The third layer is intelligence... the fourth layer... is automate... the fifth layer is build" |
| "over 60 people across all of them" (team size, run from a phone) | VERIFIED | Verbatim in transcript.txt: "The ability to manage the four companies, over 60 people across all of them. I can run it literally from my phone if I wanted to." |
| "it used to be seven or eight different platforms" (Data layer pain point) | VERIFIED | Verbatim in transcript.txt |
| "This is not a chatbot... it's not one single SAS tool" (Anti-SaaS positioning) | VERIFIED | Verbatim in transcript.txt (transcribed "SAS," genius.md/SKILL.md correctly render as "SaaS") |
| "none of it gives you a unifying system to add it to... they're creators and not founders" | VERIFIED | Verbatim in transcript.txt |
| "you now ask your AI system or AIOS, hey, which of these can AI help me to do or fully do for me? And it can categorize it into yes or partially or no" (Task Audit) | VERIFIED | Verbatim in transcript.txt |
| "do you want to keep expanding... or do you want to use that extra bandwidth to step back and actually enjoy the freedom" (Bandwidth → Choice) | VERIFIED | Verbatim in transcript.txt |
| 20-30% must-dos / 70-80% strategic bandwidth target | VERIFIED | Verbatim in transcript.txt: "I can do like 20 to 30% of my work is like must dos and the rest of it is like open space" |
| "idea → $1M webinar in 7 days" as literally collected cash | UNCONFIRMED / corrected | `extraction-report.md` line 61 phrases it as "collected the revenue in just 7 days." The verbatim transcript is more precise and less certain: "we generated enough deposits, bookings, and pips that will accumulate to over a million New Zealand dollars in sales over the next 7 days" — i.e., a projected/booked NZD pipeline forecast to accumulate over a *further* 7 days, not USD cash already banked inside the sprint window. Flagged as its own Anti-Pattern entry in `genius.md` (overclaiming) rather than silently repeated. |
| Speaker's name is "Liam Mley" | UNCONFIRMED (LIKELY ASR error for "Liam Ottley") | See Live web check above. Not corrected in this repair (out of scope — naming/identity is a conductor-level decision); flagged honestly instead. |
| "3 historical shifts" framing (Industrial Revolution → Internet → AIOS) | VERIFIED | Verbatim in transcript.txt |
| "the most addicting video game I've ever played" | VERIFIED | Verbatim in transcript.txt, used in AGENT.md signature phrases |

## What this repair did NOT do

- Did not invent a new quote, date, or figure to make the anti-pattern
  or entity checks pass artificially — every added sentence traces to
  a verbatim line in `extractions/ai-brain-os/transcript.txt`, cited
  inline in `genius.md`.
- Did not rename the skill, merge it with `liam-ottley-linkedin-lead-magnet`,
  or touch any file under that sibling skill's directory.
- Did not claim the name correction as VERIFIED fact about the
  speaker's real identity — labeled LIKELY/UNCONFIRMED per the actual
  confidence level (one web search, not a primary-source confirmation
  such as the creator's own channel metadata).
