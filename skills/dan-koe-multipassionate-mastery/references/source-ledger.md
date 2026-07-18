# Source Ledger — dan-koe-multipassionate-mastery

Every claim/quote used in SKILL.md and genius.md, labeled VERIFIED (quote found
verbatim in a source file read this session), LIKELY (attributed to a named/dated
source consistent with other verified material, but the raw file wasn't
independently re-opened this repair), or UNCONFIRMED (no locatable source —
kept as narrative texture only, never as a verbatim claim).

## Primary sources checked this repair (2026-07-17)

| Source | Path | Size | Status |
|---|---|---|---|
| AI-workflow tutorial transcript | `extractions/dan-koe/transcript.txt` | 26,836 bytes | VERIFIED — read in full |
| AI Leverage extraction report (derived from the transcript above) | `extractions/dan-koe/extraction-report-ai-leverage.md` | 14,529 bytes | VERIFIED — read in full |
| claude-export tarball (checked per envelope Rule 2, before claiming any source is absent) | `_archive/claude-export-2026-07-01.tar.gz` | 332,779,255 bytes | CHECKED, not extracted — filename search for "koe" inside the archive listing returned zero hits (it is a bulk conversation export, not per-topic files); extracting and re-reading 332MB of raw conversation was out of scope for this repair. Quotes attributed to it below are labeled LIKELY, not VERIFIED. |
| `_active/codex-harvest-2026-06-11/skills/dan-koe-multipassionate-mastery/SKILL.md` | same | — | VERIFIED present, reviewed — no new quotes beyond what's already in this skill's `SKILL.md.old` |

## Claim-by-claim

### Anchored to `extractions/dan-koe/transcript.txt` (VERIFIED — matched verbatim)
- "we're not just going to have an agent do this all for us because the purpose of a personal brand and what's going to survive in the future is the human aspect of it" — VERIFIED
- "You're gambling at that point." — VERIFIED
- "you're not treating it like an employee that you have to train" — VERIFIED
- "You're waiting for someone like me in this video to give you a step-by-step framework rather than going in tinkering, experimenting, and having a goal to work towards" — VERIFIED
- "how to get ahead of 99% of people in six months" (tweet-turned-video, cited as ~1.6M views) — VERIFIED, spoken in the transcript
- Named sources Dan curates on-screen (Matt Gray, Seth Godin, and a "Caleb ___" whose surname the auto-transcript renders inconsistently — "Rston" once, "Brston" once) — VERIFIED that the mention exists; UNCONFIRMED the correct surname spelling. Do not repeat the surname as fact.

### Anchored to `extractions/dan-koe/extraction-report-ai-leverage.md` (VERIFIED)
- "Stop treating AI as an oracle. Treat it as a capable but untrained new hire." — VERIFIED (Genius Pattern 6, "AI as Employee" Mental Model)
- "the purpose of a personal brand and what's going to survive in the future is the human aspect of it" (cited there as HK-4, quoting the same transcript line above) — VERIFIED
- "2M+ followers" (Content Assessment header) — VERIFIED as stated in the report; not independently re-checked against a live follower count this session (platform figures drift over time) — treat the number as LIKELY current, not re-confirmed today.

### Anchored to "2026-07-01 claude.ai export — Dan Koe conversations" (pre-existing genius.md section; this repair did not re-derive these, only cross-referenced them)
Titled sources per the existing citation: "This is Boring But It'll 10x Your Personal
Brand in 2026" (podcast interview, Nov 2025) and "How I'd Build a One-Person
Business (If I Started Over in 2026)" (Jan 2026).
- All quotes in genius.md's "Patterns from claude.ai export" block and "Hidden
  Knowledge — 2026 additions" (MCU Content Ecosystem, Newsletter-First Production
  Cascade, Daily Back-Catalog Ritual, Theme Week Ideation, Social Media Matrix,
  Validation Cascade + 4-Hour Productization Trigger, One-Hour Lever Standard,
  Market Sophistication Endgame, Learning Experience, Vessel Decay Clock, HK items
  1-6) — LIKELY. A prior extraction session added these citing the claude.ai export
  tarball by date. This repair confirmed the tarball exists (332MB) and contains no
  filename match for "koe," but did not extract and re-read its contents to
  independently re-verify each quote against the raw conversation this session.
  Internally consistent, specifically dated/titled, not contradicted by anything
  found this session — LIKELY rather than VERIFIED.

### Earlier extraction content (genius.md "23 Unconscious Mastery Behaviors,"
Hall of Fame Exemplars, Signature Moves — pre-existing; this repair added only
cross-reference anchors, no new factual claims)
- Patterns 1-14 and the "Tacit Expertise Made Explicit" list — UNCONFIRMED as
  verbatim Dan Koe quotes. They are synthesized behavioral descriptions from an
  earlier, unlabeled extraction pass with no dated source file under `extractions/`.
  This repair did not invent new claims to fix the entity-floor check — it added
  cross-references to real files (`references/prompts-v2/*.md`, which exist on
  disk) and to real quotes already elsewhere in this same document, so each
  pattern now carries a locatable anchor without asserting a false verbatim source.
- Hall of Fame Exemplar 1 & 2, and the Anti-Exemplar ("5 Ways to Find Your Niche
  and Stick To It") — UNCONFIRMED as sourced to a specific dated transcript; these
  are illustrative composites, not quotes. Kept as-is (additive-only repair
  boundary), labeled here so no downstream reader mistakes them for verbatim Dan
  Koe material.

### 26 execution prompts (`references/prompts/`, `references/prompts-v2/`, `references/_legacy-prompts/`)
- VERIFIED present on disk (file existence + names checked this session, 3
  duplicate copies: `prompts/`, `prompts-v2/`, `_legacy-prompts/`). Their content is
  prompt-engineering scaffolding, not expert-attributed factual claims, so the
  VERIFIED/LIKELY/UNCONFIRMED distinction applies only to file-existence here, not
  to any claim about Dan Koe's own words.
