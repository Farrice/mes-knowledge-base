# Coaching Business OS — Source Ledger

This hub is a conductor/system skill (no single expert persona) that synthesizes three named source talks compressed into `references/field-guide.md`. No file under `extractions/` matches any of these names — confirmed by direct search, not assumed absent (see Absence Check below). Ground truth for this repair is therefore: (a) the compressed quotes already inside `references/field-guide.md` and `genius.md`, both same-repo skill files, and (b) the raw harvest archive that both files claim as origin.

## Primary Source Corpus

| Source | Claimed date | Where cited in-repo | Label |
|---|---|---|---|
| `claude.ai export, 2026-07-01` (SKILL.md frontmatter `source:` field) | 2026-07-01 | `skills/coaching-business-os/SKILL.md` line 7 | LIKELY — the archive itself is VERIFIED to exist (`_archive/claude-export-2026-07-01.tar.gz`, 332,779,255 bytes, confirmed via `ls -la` 2026-07-17); the specific Smith/Elkaim/Mast conversations inside it were NOT re-extracted for this repair (332MB tarball, out of scope for a targeted heartbeat fix), so the compressed extract in `field-guide.md` was not independently re-verified against the raw export text. |
| James Smith, "How to get content ideas so good you can't stop going viral" (live ideation session with editor Declan) | Aug 2025 | `references/field-guide.md` lines 24-38 | LIKELY — internally consistent, dated, named source; no raw transcript file present in repo to check verbatim. |
| Yuri Elkaim (Healthpreneur), "How to get high-paying clients for your online health coaching business" (jug-and-four-cups talk) | May 2025 | `references/field-guide.md` lines 42-57 | LIKELY — same as above. field-guide.md itself flags an ASR artifact: "the ASR transcript renders the speaker's name as 'Ariel Kim'" — this note is VERIFIED as present in-repo; the underlying raw ASR transcript was not located to independently confirm the mis-rendering. |
| Jonathan Mast, NotebookLM training webinar (Whitebeard Strategies) | Dec 2025 | `references/field-guide.md` lines 7-20 | LIKELY — same as above; the "Natalie" prompt-writing GPT layer is VERIFIED as stated in-repo, UNCONFIRMED as an externally real tool (no web check run — out of scope). |

## Claim-by-Claim (facts repeated in genius.md / SKILL.md, checked against field-guide.md)

| Claim | In-repo anchor | Label |
|---|---|---|
| "Ads guarantee visibility, NOT conversions" (Elkaim) | `references/field-guide.md` line 48 (verbatim); paraphrased in `genius.md` Quick Reference and Hidden Knowledge | VERIFIED (verbatim, in-repo) |
| Generalists "lose their shirt very quickly" on ads (Elkaim) | `references/field-guide.md` line 53 | VERIFIED (verbatim, in-repo) |
| Smith's product list: $2,500 mentorship / $99 content mastery / $99 PT kit | `references/field-guide.md` line 30; `genius.md` Revenue-Backwards pattern | VERIFIED (verbatim, in-repo, restated identically in two skill files) |
| Dance-floor analogy, "converts ~1 in 100" | `references/field-guide.md` line 31; `genius.md` Buy-a-Drink-First pattern | VERIFIED (verbatim, in-repo) |
| Teach to Sell explicitly "not teach to teach" | `references/field-guide.md` line 49; `genius.md` Teach to Sell pattern | VERIFIED (verbatim, in-repo) |
| Healthpreneur ran "multiple seven figures" on one pipeline, no social channels, 3 years | `references/field-guide.md` line 55; `genius.md` One Pipeline pattern | VERIFIED (verbatim, in-repo) |
| "accumulated expertise becomes unfindable" (Mast) | `references/field-guide.md` line 11 | VERIFIED (verbatim, in-repo) |
| "if you're charging five, seven, even $10K... you're still undercharging" (Elkaim) | `genius.md` Hidden Knowledge, High-Ticket Pricing insight | VERIFIED (verbatim, in-repo) |
| Email list grows "hundreds per week" regardless of bookings (Elkaim) | `references/field-guide.md` line 55; `genius.md` Hidden Knowledge, Email List insight | VERIFIED (verbatim, in-repo) |
| 30-40% of edit budget on first 30 seconds / half of reel production time on first 3-5 seconds (Smith) | `references/field-guide.md` line 34; `genius.md` Packaging Before Production pattern + Hidden Knowledge Attention Allocation insight | VERIFIED (verbatim, in-repo) |
| Routing-map lane ownership (7 lanes named in SKILL.md rows 18-24) | Directory existence checked directly: `skills/taylor-welch-wealthy-consultant/`, `skills/jay-hiette-coaching-positioning/`, `skills/gabe-novotny-fitness-content-business/`, `skills/yuri-elkaim-health-coaching-business/`, `skills/steven-kotler-flow-performance/`, `skills/nir-eyal-habit-design/`, `skills/mark-manson-values-psychology/` — all 7 confirmed to exist via `find`/`test -d`, 2026-07-17 | VERIFIED (directory existence) |
| Peer skill mention "greg-hickman" in SKILL.md Quick Reference | Actual directory is `skills/greg-hickman-service-scaling/` (`skills/greg-hickman/` does not exist) | UNCONFIRMED as written — imprecise short-name reference. Flagged here, not corrected: renaming SKILL.md prose is outside the three failing checks this repair targets (minimal-touch boundary per envelope) and the peer-skill line already passes existing checks. |

## Absence Check (Rule 2 — verified, not assumed)

- `ls extractions/ | grep -i -E "smith|elkaim|mast|healthpreneur"` → no output (run 2026-07-17). `ls extractions/ | wc -l` → 193 entries total, none matching. Confirmed absent by direct read, not inferred.
- `grep -rli "healthpreneur|jug.and.four.cups|whitebeard|perfect client pipeline"` across the repo (excluding this skill and its `yuri-elkaim-health-coaching-business` sibling) → only hits inside `.claude/worktrees/w3-lane3-repair-execution/` (a mirrored worktree copy of the same skill files, not an independent raw source).
- No raw transcript file for any of the three talks exists under `extractions/`, `research_outputs/`, or elsewhere in the repo as of 2026-07-17 — the compressed `field-guide.md` extract is the only in-repo primary artifact.
