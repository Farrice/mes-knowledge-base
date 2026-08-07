# Daniel Pink — Source Ledger

Claim-by-claim provenance for `skills/daniel-pink-writing-structure/`. Unlike several
skills in this repair wave, actual ground truth for this expert WAS located and read in
full this session — the "no extractions/ folder" fact is real, but it does not mean the
source is absent. See "Source Recovery" below for the full trail, run 2026-07-17.

## Source Recovery (run 2026-07-17)

| Check | Method | Result |
|---|---|---|
| `extractions/` directory for Daniel Pink | `ls extractions/ \| grep -i pink` (193 total extraction dirs) | 0 hits — no dedicated extraction folder for this expert |
| Codex-harvest extractions | `ls _active/harness/codex-harvest-2026-06-11/extractions/ \| grep -i pink` | 0 hits |
| Repo-wide search for a landed raw-source file | `grep -ril "daniel pink" --include="*.md" .` | Only the skill's own files (`SKILL.md`, `genius.md`, workflows, prompts-v2), `agents/daniel-pink/`, `SKILL_INDEX.md`, `SLASH_COMMANDS.md`, `invocation-cards.md` — no separate raw-transcript file exists anywhere in the checked-out repo tree |
| Archived claude.ai export tarball | `tar -tzf _archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, 3,864 entries, confirmed listable) — then extracted `claude-export/normalized/{conversations,memories,projects}/` (275 MB) to scratchpad and grepped for `daniel pink\|kakistocracy\|Charlie Yarnoff\|fresh yet familiar\|The Invisible Present` (case-insensitive) | 9 files matched; 2 are the actual Pink source conversations (below), the rest are incidental hits |
| Primary source conversation | `claude-export/normalized/conversations/2bf2299f-cbfd-4936-8b08-2bee19fc22e2.md` (95,102 bytes) | title: "✍️ 💎💡 Daniel Pink \| How to Write Something Truly Useful" — a YouTube transcript (Merlin AI auto-transcription of `youtube.com/watch?v=gCNNwjyQQIA`) pasted as a claude.ai attachment; conversation created 2026-01-14, updated 2026-01-18. Read in full this session (~5,600 words of Pink's actual speech). |
| Duplicate re-extraction attempt | `claude-export/normalized/conversations/2d9a5291-20b3-4cbb-9b36-d6cf57a8d180.md` (71,251 bytes) | title: "Daniel Pink \| How to Write Structurally Well \| Writing Mastery" — the SAME underlying transcript re-pasted into a fresh conversation 2026-02-12. The assistant's extraction artifacts from that session ("Part 1 of 5" etc.) did not survive the export — each shows as a placeholder ("This block is not supported on your current device yet."), so this file contributes no NEW source text, but it confirms the transcript is the sole source both times Pink was extracted, and that `genius.md`'s two-title frontmatter note is accurate, not invented. |

**Conclusion**: `genius.md`'s existing frontmatter ("Source: Pink's long-form interview...
'How to Write Something Truly Useful' / 'How to Write Structurally Well', extracted from
Farrice's claude.ai export") is accurate and verifiable. The source is real, was located
this session, and every quote below — pre-existing and newly added — was checked against
it word-for-word (auto-transcription artifacts like "brakes/breaks" and "kac
kacistocracy" noted where relevant).

## Claims

| Claim / Quote | Label | Basis |
|---|---|---|
| Structure-before-sentences: months of research to find the skeleton, whiteboard/post-its, swivel chair | VERIFIED | Verbatim at conversation `2bf2299f`; pre-existing in `genius.md` Pattern 1 |
| *When* structure hunt — "day, week, month, year" then domains, both failed: "I have nothing to say" | VERIFIED | Verbatim at `2bf2299f`; pre-existing in `genius.md` Pattern 1 |
| Breaks-chapter ballooning: "there's a shitload to say about breaks" | VERIFIED (spelling normalized) | Transcript alternates "brakes"/"breaks" — an auto-transcription artifact, not a Pink error; genius.md correctly resolves to "breaks." Pre-existing, Pattern 2 |
| Proposal-as-test: "if this idea can't withstand a 30-page proposal, it's not going to withstand a 300-page book" | VERIFIED | Near-verbatim (source: "...it's not going to be able to withstand a 300page book"); pre-existing, Pattern 3 |
| The Invisible Present kill, 10 days in, "You guys can come home now" | VERIFIED | Verbatim at `2bf2299f`; pre-existing, Pattern 3 |
| "totally fresh but also totally familiar" / *When* pitch ("we have lots of how-to books... a when-to book") | VERIFIED | Verbatim at `2bf2299f`; pre-existing, Pattern 4 |
| Socialization / "dead in the eyes... that's interesting, I disagree" | VERIFIED | Verbatim at `2bf2299f`; pre-existing, Pattern 5 |
| Consilience: ~600 studies, chronobiologists / JDM scholars / sports psychologists | VERIFIED | Verbatim ("something like 600 studies about timing"); pre-existing, Pattern 6 |
| Research saturation + green-socks skepticism + regret-in-children compression | VERIFIED | Verbatim at `2bf2299f`; pre-existing, Pattern 7 |
| Engagement density: David Zucker / *Airplane!* 25-30 second rule; laugh-density analysis on his plays | VERIFIED | Verbatim at `2bf2299f`; pre-existing, Pattern 8 |
| Charlie Yarnoff, "~38 years ago," "Sometimes you have to write to figure it out" | VERIFIED | Verbatim ("38 years ago, and I still live by... Sometimes you have to write to figure it out"); pre-existing, Pattern 9 |
| Tyler Cowen — write the strongest case against your own view | VERIFIED | Verbatim at `2bf2299f`; pre-existing, Pattern 9 |
| Reader promise: $25 / nine hours / "would I want to read it the first week" | VERIFIED | Verbatim at `2bf2299f`; pre-existing, Pattern 10 |
| Word-count ritual: 22 steps to the garage, 500-800 words, "the tortoise won" | VERIFIED | Verbatim at `2bf2299f`; pre-existing, Pattern 11 |
| Breaks are performance infrastructure (motion/outside/social/detached) | VERIFIED | Verbatim at `2bf2299f`; pre-existing, Hidden Knowledge #1 |
| Side-project signal: op-eds, George magazine, "step outside yourself and watch what you do" | VERIFIED | Verbatim at `2bf2299f`; pre-existing, Hidden Knowledge #2 |
| Commonplace book, 8 years; "kakistocracy" | VERIFIED (spelling normalized) | Raw transcript shows a stutter/mis-transcription ("kac kacistocracy" — Merlin AI auto-transcription artifact); Pink defines the real word correctly on the recording ("ruled by the least competent, least desirable people"). genius.md's spelling is the correct dictionary form, not an invented quote. Pre-existing, Hidden Knowledge #3 |
| "the water got poisoned and we got used to the taste" (contemporary Oedipus play) | VERIFIED | Verbatim at `2bf2299f`; pre-existing, Hidden Knowledge #3 |
| House vs. watch: book tolerates a misplaced powder room, play must mesh like gears | VERIFIED | Verbatim at `2bf2299f`; pre-existing, Hidden Knowledge #4 |
| Watch-the-audience-not-the-speaker; arrives 11am for a 3pm slot | VERIFIED | Verbatim at `2bf2299f`; pre-existing, Hidden Knowledge #5 |
| "a mistake that some authors [make]... the world starts kind of pushing them in this direction... it might not be a good idea for them" | VERIFIED | Verbatim (compressed with ellipsis) at `2bf2299f`; **new** Anti-Pattern #1 (this repair) |
| "day, week, month, year" / domain filing failure, "I have nothing to say" (reused as anti-pattern framing) | VERIFIED | Verbatim at `2bf2299f`; **new** Anti-Pattern #2 (this repair) |
| "The biggest lie that writers will tell themselves is ah I'll remember that later" | VERIFIED | Verbatim at `2bf2299f`; **new** Anti-Pattern #3 (this repair) |
| "You had me till the present thing... that's a little too clever" | VERIFIED | Verbatim (compressed) at `2bf2299f`; **new** Anti-Pattern #4 (this repair) |
| "If I see one paper from an obscure journal... wearing green socks makes you more creative... a little bit more skeptical" | VERIFIED | Verbatim (compressed) at `2bf2299f`; **new** Anti-Pattern #5 (this repair) |
| "if you listen to a transcript of people actually talking, that's totally boring" | VERIFIED | Verbatim at `2bf2299f`; **new** Anti-Pattern #6 (this repair) |
| "many writers delude themselves into thinking their audience is everybody, and it's never everybody" | VERIFIED | Verbatim at `2bf2299f`; **new** Anti-Pattern #7 (this repair) |

No claim in this skill is UNCONFIRMED — the source transcript was recovered, opened,
and every quote (pre-existing and new) checked against it directly. The only normalized
detail is spelling ("breaks" for the transcript's inconsistent "brakes/breaks," and
"kakistocracy" for the transcript's stuttered "kac kacistocracy"), both flagged above.

## What This Repair Changed vs. Left Alone

- **Added** (this repair): `## How to Use This Skill (Model Calibration)` section and
  `## Anti-Patterns` section (7 sourced items) in `genius.md`, plus this ledger and
  `PROVENANCE.md`. All new Pink quotes were pulled from the same recovered transcript —
  none invented.
- **Untouched**: `SKILL.md`, all 3 workflow files, all 3 `references/prompts-v2/*.md`
  files, and every pre-existing `genius.md` Genius Pattern / Hidden Knowledge entry
  (each independently re-verified against the recovered transcript during this repair,
  not merely trusted).
