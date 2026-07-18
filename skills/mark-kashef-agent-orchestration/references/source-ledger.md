# Source Ledger — mark-kashef-agent-orchestration

Repair pass 2026-07-18 (Wave 3 Lane 4 Batch 10). Every claim added or
touched by this repair in `genius.md` is labeled VERIFIED / LIKELY /
UNCONFIRMED against what was actually found on disk. Pre-existing
content not modified by this pass is noted but not re-graded unless it
was directly implicated by a failing check.

## Search performed (absence verified, not assumed)

Per the envelope's rule 2 ("a claim that sources are ABSENT is itself
a provenance claim"), the following searches were run before writing
anything:

- `ls extractions/ | grep -i kashef` → 5 hits: `mark-kashef`,
  `mark-kashef-banana-squad`, `mark-kashef-claude-claw`,
  `mark-kashef-perfect-agentic-os-kit`, `mark-kashef-visual-design`.
  Only `extractions/mark-kashef/` maps to this skill (agent
  orchestration / agent teams); the other four belong to sibling
  skills being repaired in parallel this batch and were NOT read.
- `grep -in "circuit breaker\|tripwire\|checkpoint\|blast radius\|degradation\|fallback" extractions/mark-kashef/transcript.txt extractions/mark-kashef/extraction-report.md`
  → zero hits in either file. This confirms the pre-existing "Circuit
  Breaker Architecture" section in `genius.md` (lines ~71-93 in the
  pre-repair file) is NOT drawn from the Kashef source material —
  flagged below, not silently anchored.
- `find . -iname "*claude-export*"` → the "claude.ai export" section
  already in `genius.md` (§ "Patterns from claude.ai export — Mark
  Kashef conversations, 2026-07-01") draws from
  `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes). This
  archive was NOT re-opened this pass (out of scope for a targeted
  repair; unpacking a 332MB archive to re-verify pre-existing,
  already-passing content is not required by the failing checks).
  That section is pre-existing and untouched by this repair; labeled
  UNCONFIRMED (not reverified this pass) rather than claimed VERIFIED.

## Files consulted (real, on-disk, sized)

| File | Size (bytes) | What it is |
|---|---|---|
| `extractions/mark-kashef/transcript.txt` | 27,910 | **Primary source for this repair.** Full verbatim transcript of a ~20-minute YouTube video, "7 Agent Team Use Cases" (per `extraction-report.md`). Every new quote in this repair traces to this file. |
| `extractions/mark-kashef/extraction-report.md` | 6,254 | Mastery Extraction report derived from the transcript above (4 Genius Patterns, 3 Hidden Knowledge items — matches the pre-existing `genius.md` content). Used to cross-check framing, not quoted directly. |
| `skills/mark-kashef-agent-orchestration/genius.md` | pre-repair baseline (~9,900 bytes) | Baseline this repair extends. Not deleted or rewritten — additive only. |
| `_archive/claude-export-2026-07-01.tar.gz` | 332,779,255 | Source of the pre-existing "claude.ai export" section (lines ~101-159 pre-repair). NOT opened this pass — see above. |

Git history check: `git log -1 --format=%ad -- extractions/mark-kashef/transcript.txt`
returns `Mon Mar 2 04:36:56 2026 -0800` — the date used in this
repair's Anti-Pattern anchors ("added to repo 2026-03-02 per git
log") is this commit date, not a claimed video-publish date (the
video's actual publish date is not recorded anywhere in the source
files and is NOT claimed).

## Claim-by-claim labels (this repair's additions)

| Claim / quote | Label | Basis |
|---|---|---|
| "If you just say spawn agents, it could get confused between sub aents [sic], which are very different in the way they work versus agent teams." | VERIFIED | Verbatim in `transcript.txt` (rendered "sub agents" in this repair's prose; the transcript itself has the ASR typo "sub aents" — noted, not silently corrected in the source claim). |
| "the rule of thumb, by the way, from anthropic is three to five agents is the sweet spot. Anything beyond that can lead to diminishing returns, overengineering, overthinking, and most importantly, a huge consumption of tokens." | VERIFIED | Verbatim in `transcript.txt`. |
| "Looks decent, but still AI... it's not completely AI slop, but you could desopify it with the right instructions." | VERIFIED | Verbatim in `transcript.txt` (two adjacent sentences from the same passage, condensed with `...`; both halves independently confirmed present). |
| "it might make more sense to maybe spin up sub agents to make edits in parallel since they don't need to speak to each other if you can identify independently what needs to change." | VERIFIED | Verbatim in `transcript.txt`. |
| "the less thinking you have to make cloud code do, the more accurate the results." | VERIFIED | Verbatim in `transcript.txt`, immediately following Kashef's own "this is overkill" self-assessment of his Python-build instruction. |
| "invoke[s] what's called the ask user input tool" / "approve as is, approve with notes, or reject with some rework" | VERIFIED | Both phrases verbatim in `transcript.txt` (the bracketed `[s]` is a repair-added grammatical bridge, not part of the quote; source reads "it will actually usually invoke what's called the ask user input tool"). |
| "150,000 tokens" (pitch-deck build) | VERIFIED | Verbatim in `transcript.txt`: "This still took 150,000 tokens, but it was very efficient." |
| "180,000 tokens" (RFP build) | VERIFIED | Verbatim in `transcript.txt`: "this took around 180,000 tokens." |
| "you can always hover over this URL, click it, open up this pitch deck" | VERIFIED | Verbatim in `transcript.txt`. |
| "It's not going to be absolutely beautiful, but it's respectable" | VERIFIED | Verbatim in `transcript.txt`. |
| "Circuit Breaker Architecture" / "Quality Tripwires" / "Blast Radius Containment" / "Degradation Signals" as Kashef's own terminology | UNCONFIRMED (pre-existing, not this repair's addition) | These terms do not appear anywhere in `transcript.txt` or `extraction-report.md` (confirmed by direct grep, see above). This repair did NOT invent this framework — it pre-dates this pass — but explicitly flags it in `genius.md` itself (new "Provenance note" callouts) rather than let the missing sourcing pass silently, per the envelope's rule 2. |
| The "Monolithic Prompt Failure" Anti-Exemplar prompt snippet ("Act as a market researcher, strategist, copywriter, and designer...") | UNCONFIRMED as a verbatim Kashef quote (pre-existing) | Not found in `transcript.txt`. It is a constructed illustrative bad-example, consistent with Kashef's verified principle (single-role prompts dilute context) but not something he said on camera. Flagged in `genius.md` with a new "Provenance note" line added this pass. |
| "Patterns from claude.ai export — Mark Kashef conversations (2026-07-01)" section (all sub-patterns/insights) | UNCONFIRMED (not reverified this pass) | Pre-existing content sourced to `_archive/claude-export-2026-07-01.tar.gz`, not re-opened this repair (see Search Performed above). Not modified; a provenance note was added to the section's italic source line pointing here. |

## What this repair did NOT do

- Did not invent a new quote, date, or figure to make `anti_patterns_sourced`
  or `named_entity_floor` pass artificially — every added sentence
  traces to a verbatim line in `extractions/mark-kashef/transcript.txt`,
  cited inline in `genius.md`, and reproduced in the table above.
- Did not delete or rewrite any passing content (Genius Patterns,
  Hidden Knowledge, Hall of Fame Exemplars, Signature Moves, Circuit
  Breaker Architecture, Quality Rubric, or the claude.ai-export
  section) — only additive sentences and explicit provenance notes.
- Did not claim the Circuit Breaker Architecture framework, the
  Monolithic Prompt Failure exemplar, or the claude.ai-export section
  as freshly VERIFIED — each carries an honest label above instead of
  a manufactured anchor.
- Did not touch `SKILL.md`, any `workflows/*.md` file, or any other
  `references/*` file — those checks (`workflow_contracts`,
  `verbatim_exemplars`) were already passing and out of scope.
- Did not touch any sibling `mark-kashef-*` skill.
