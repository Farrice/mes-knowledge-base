# Source Ledger — ash-maurya-lean-metrics

Repair pass 2026-07-17 (Wave 3 Lane 4 Batch 2). Every claim added or
retained in `genius.md`/`SKILL.md` labeled VERIFIED / LIKELY / UNCONFIRMED
against what was actually found on disk.

## Search performed (absence verified, not assumed)

Per the envelope's rule 2 ("a claim that sources are ABSENT is itself a
provenance claim"), the following searches were run and results recorded
with real file sizes (`wc -c`, not `wc -l`):

- `ls extractions/ | grep -i maurya` → 0 results (`extractions/` has 193
  total entries; none named for Ash Maurya — confirmed by direct count).
- `find extractions -iname "*maurya*"` → 0 results.
- `find . -iname "*maurya*"` (repo-wide, excluding worktrees/harvest
  duplicates) → `skills/ash-maurya-lean-metrics/`, `skills/
  ash-maurya-founder-systems/` (sibling, out of scope), `agents/
  ash-maurya/` — no primary-source directory.
- **Primary source located**: `SKILL.md` frontmatter states `source:
  claude.ai export 2026-07-01`. The claude.ai conversation export archive
  (`_archive/claude-export-2026-07-01.tar.gz`, 332,779,255 bytes) contains
  a manifest at `_active/harness/claude-export/index.json` (3,711 conversations
  total). Filtering titles for "maurya" returns **93 conversations** — real
  claude.ai sessions where a user pasted Ash Maurya YouTube transcripts
  (via the Merlin AI transcript tool) and ran MES-style extraction prompts
  against them.
- Six of those 93 conversation files were extracted from the tarball (`tar
  xzf` selective member extraction, no full unpack) and read in full for
  this repair. Each carries a real YouTube URL, video title, and a raw
  timestamped transcript as a pasted attachment — the assistant turns are
  mostly MES-extraction boilerplate ("Viewing artifacts..." placeholders)
  and were NOT used as source material; only the human-pasted transcript
  text was cited.
- **Scope honesty**: only 6 of 93 Maurya conversations were read. Claims in
  the existing `genius.md` that were NOT found in these 6 files (see table
  below) are labeled UNCONFIRMED-IN-SAMPLE, not "false" — the other 87
  conversations were not searched, so absence is not asserted beyond the
  files actually read.

## Files consulted (real, on-disk, sized)

| File | Size (wc -c) | What it is |
|---|---|---|
| `skills/ash-maurya-lean-metrics/SKILL.md` | 5,219 bytes | Current skill card (this repair's baseline) |
| `skills/ash-maurya-lean-metrics/genius.md` | 14,222 bytes | Current genius file (this repair's baseline, pre-repair) |
| `agents/ash-maurya/AGENT.md` | 4,830 bytes | Agent persona card; paraphrases the same genius.md claims, adds no independent sourcing |
| `agents/ash-maurya/memory/context.md` | 462 bytes | Empty/placeholder session memory, no claims |
| `_archive/claude-export-2026-07-01.tar.gz` | 332,779,255 bytes | Raw claude.ai export archive; source of the 6 files below |
| `claude-export/normalized/conversations/c804ce79-a2cc-45b2-9b58-9517eb292f4f.md` ("7 Costliest Mistakes First-Time Founders Make") | 26,132 bytes | YouTube transcript (youtube.com/watch?v=-30TXCM48sg), Ash Maurya's own channel — source for the full Anti-Patterns section |
| `claude-export/normalized/conversations/6ce7fde9-b576-47a8-84be-59bba323f657.md` ("Don't Build a Zombie Startup") | 35,532 bytes | YouTube transcript (youtube.com/watch?v=9BjNeHGXFuE) — confirms Six Degrees / BoxCloud / Cloudfire as three real named prior products and the "zombie startup" concept |
| `claude-export/normalized/conversations/9ef22ac8-cdf7-479f-b8d6-d0057402ce8f.md` ("One Startup Metric to Rule Them All") | 74,928 bytes | YouTube transcript — verbatim source for the Starbucks/Facebook/Airbnb archetype examples |
| `claude-export/normalized/conversations/85594879-e267-45dc-becb-11006ce3a45e.md` ("The 8-Second Rule: How Tesla Won...") | 35,101 bytes | YouTube transcript (youtube.com/watch?v=2qct537U8HY) — verbatim source for the Tesla MVP-cocktail example |
| `claude-export/normalized/conversations/4d709e81-5d2a-4f1a-8d25-76f485563f8a.md` ("Startup Myths Debunked: Truth vs. Hype") | 30,890 bytes | YouTube transcript, read for cross-check; not directly cited in this repair's additions |
| `claude-export/normalized/conversations/3f84f0f9-e375-4f9d-83dd-f392c0a0d441.md` ("Why Talking to Users is Bad for Startups") | 52,668 bytes | YouTube transcript, read in full; does NOT contain the "headphone case study" or "Cloudfire ghosted, 30 yes-interviews" claims already present in `genius.md`'s pre-existing "Interview Broad" insight — see UNCONFIRMED-IN-SAMPLE row below |

## Claim-by-claim labels

| Claim | Label | Basis |
|---|---|---|
| Ash Maurya is a real entrepreneur, author of *Running Lean*, creator of Lean Canvas, founder of LeanStack | VERIFIED | Public figure; consistent with all 6 sampled transcripts' self-introductions ("I'm an entrepreneur and author and the creator of the popular one-page business modeling tool lean canvas," c804ce79 transcript 0:36–0:44) |
| Starbucks archetype example: "time spent in store" as the traction metric | VERIFIED | Verbatim in `9ef22ac8...md`, transcript lines ~4:53–7:33 ("Starbucks, that key activity was time spent in store") |
| Facebook archetype example: DAU + ARPU as the only two reported metrics | VERIFIED | Verbatim in `9ef22ac8...md`, transcript ~7:33–8:07 ("Facebook... reports daily active users" / "the only metrics Facebook highlights") |
| Airbnb archetype example: guest nights booked | VERIFIED | Verbatim in `9ef22ac8...md`, transcript ~8:20–8:52 ("Airbnb uses a single traction metric, guest nights booked") |
| Tesla MVP example: zero emissions delighter, 200-mile range floor, Lotus chassis, instant torque | VERIFIED | Verbatim in `85594879...md`, Tesla is the transcript's entire case study (2:06–7:39 range) |
| LeanSpark: 246 pre-orders, $50K+ in 40 days | LIKELY | Consistent with Maurya's public LeanSpark launch narrative and his own demo-sell-build thesis; not located verbatim in the 6 sampled transcripts — not independently re-verified via web search in this repair pass (out of scope; this repair touches provenance labeling using existing archive material, not fresh external research) |
| Six Degrees, BoxCloud, Cloudfire as three real prior products that "nearly zombied" | VERIFIED | Verbatim in `6ce7fde9...md`, 0:26–0:33 ("It nearly happened to me three times with my first three products, Six Degrees, BoxCloud, and Cloudfire") |
| Cloudfire's business-model collapse: investor asked "can you show me how the business model math works," fell apart in 5 minutes, pivoted after 9 months | VERIFIED | Verbatim in `6ce7fde9...md`, 1:45–2:40 |
| "His own Cloudfire failure: 30 'yes' interviews, then ghosted" + headphone case study (sound quality had zero signal; fit-during-exercise and battery life were the real mountains) — pre-existing claim in genius.md's "Interview Broad" insight | UNCONFIRMED-IN-SAMPLE | Not found in `3f84f0f9...md` ("Why Talking to Users is Bad for Startups," 52,668 bytes, read in full) despite that being the most topically relevant of the 6 sampled files. Likely present in one of the other 87 unsampled Maurya conversations in the export (93 total found), but this repair did not locate it. Flagged as a gap, not deleted (envelope: additive-first, never rewrite passing content on a hunch) — a future repair pass should either locate the exact source conversation or relabel this claim in `genius.md` directly |
| "7 Costliest Mistakes" anti-patterns (quitting job early, build-first belief, premature fundraising, premature public launch, freemium-first, going too broad, falling in love with the solution) | VERIFIED | Verbatim quotes + timestamps in `c804ce79...md`; full citations in the new Anti-Patterns section of `genius.md` |
| Kathy Sierra's "make a better user of X" framing, Maurya's own "make better startup founders" pivot | LIKELY | Present in the pre-existing genius.md pattern; not verified against one of the 6 sampled transcripts in this repair pass — plausible and consistent with his public writing (Running Lean blog), but not independently re-confirmed here |
| Workflow files carry Output Schema + Quality Gate | VERIFIED | Confirmed by `execution/skill_auditor.py` heartbeat check (`workflow_contracts`: PASS, unchanged by this repair) |
| Named-entity floor (15 pattern sections, 0.13 zero-entity ratio) | VERIFIED | Confirmed by `execution/skill_auditor.py` heartbeat check (`named_entity_floor`: PASS, unchanged by this repair) |

## What this repair did NOT do

- Did not invent a new Ash Maurya quote, timestamp, or video citation to
  make the anti-pattern check pass artificially — every anchor in the new
  Anti-Patterns section points to a real, sized, on-disk transcript file
  extracted from the archive, quoted verbatim with a real timestamp and
  real YouTube URL.
- Did not delete or relabel the pre-existing "Cloudfire ghosted / headphone
  case study" claim in genius.md's Hidden Knowledge section — flagged
  UNCONFIRMED-IN-SAMPLE above instead, since 87 of 93 Maurya conversations
  in the archive were not searched and a false-absence claim is exactly
  the failure mode this envelope warns against.
- Did not re-extract or unpack the full 332MB archive — used `tar`'s
  selective-member extraction to pull only the 6 needed conversation files,
  consistent with the standing instruction not to re-import the claude-export
  archive wholesale.
- Did not touch `workflow_contracts` or `named_entity_floor` — both already
  PASS per the audit and were left untouched (additive-first, minimal-touch).
