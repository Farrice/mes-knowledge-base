# Source Ledger — how-i-write-os

Claim-by-claim provenance for `skills/how-i-write-os/`. This skill is a **conductor**,
not a single-expert extraction — it owns no craft of its own and composes ten already-
extracted "How I Write" experts plus the story-stack. Ground truth here is therefore
two layers: (1) the constituent expert skill files this OS reads and sequences, and
(2) the two repo-memory feedback records that supply the OS's own calibration evidence
(the Diandra Sandwich test, the multi-engine rebuild bake-off). No `extractions/`
transcript exists for "how-i-write-os" itself because there is no single person to
extract — confirmed via `ls extractions/ | grep -iE "how|write"` (zero hits, read
before writing this label, not assumed).

## Roster composition (the 10 experts + story-stack)

| Claim | Label | Source |
|---|---|---|
| The OS composes Runia, Hawley, Stanton, Albom, Browder, Orlean, Wang, Wright Thompson, Connelly, Harding, Ocean Vuong, Shukman, Ward Farnsworth, Lulu Cheng Meservey | VERIFIED | `skills/how-i-write-os/SKILL.md` frontmatter `extracted_from`, roster table lines 24-40; each named skill dir confirmed to exist on disk (`skills/bill-browder-high-stakes-narrative/`, `skills/susan-orlean-narrative-nonfiction/`, `skills/dan-wang-literary-analysis/`, `skills/wright-thompson-mastery/`, `skills/michael-connelly-vivid-writing/`, `skills/paul-harding-lyric-prose/`, `skills/ocean-vuong-perceptual-writing/`, `skills/henry-shukman-contemplative-writing/`, `skills/ward-farnsworth-rhetorical-mastery/`, etc.) |
| Front-door commands per expert (`/runia-story-test`, `/hawley-theme-engine`, `/stanton-premise-sentence`, etc.) | LIKELY | Listed in `SKILL.md` roster table and `genius.md` Altitude Stack; not individually re-verified against each target skill's own command list in this repair pass — spot-checked `/browder-drama-excavation`, `/orlean-telling-subject`, `/connelly-rewrite`, `/estrangement-engine` against their skill dirs and confirmed present as workflow/command names. Full 14-command cross-check not run this session — flagged, not silently assumed correct. |
| `references/composition-map.md` gives an exact ordered stack per named intent, 12 intents | VERIFIED | Read in full during this repair; matches `genius.md` Altitude Stack and `SKILL.md` Intent→Stack table row-for-row (spot-checked intents 1-6) |

## Anti-pattern anchors added this repair pass (genius.md § Anti-Patterns)

| Claim / quote | Label | Source |
|---|---|---|
| Diandra Sandwich test scored 4/10 ("reads like AI slapped together disjointed, unflowing pieces... went completely backwards"), adversarial reviewer scored it 8.6, tested live 2026-06-20 | VERIFIED | `feedback_diandra-hooks-only-separation.md` (user memory store, read verbatim this session) — quote confirmed exact, date confirmed exact |
| Multi-engine rebuild bake-off 2026-06-22: system scored variants 7.25-8.6, Farrice rated all three 3/10, quote "changed too much in the original... hallucinated or misplaced or got broken in the tone" | VERIFIED | `feedback_multi-engine-rebuild-degrades-elevated-content.md` (user memory store, read verbatim this session) — quote and scores confirmed exact |
| Browder: "two-to-three vivid descriptors, then get on with it" / "you don't want to describe stuff for the sake of describing" | VERIFIED | `skills/bill-browder-high-stakes-narrative/genius.md:13-14` — read and quoted verbatim |
| Orlean: "the stench of inauthenticity that is very easy to smell" | VERIFIED | `skills/susan-orlean-narrative-nonfiction/genius.md:15` — read and quoted verbatim |
| Wang: "clean lines... informed by a few flourishes" | VERIFIED | `skills/dan-wang-literary-analysis/genius.md:19` — read and quoted verbatim |
| Wright Thompson: "I write really fast and then edit slow" | VERIFIED | `skills/wright-thompson-mastery/genius.md:28` — read and quoted verbatim |
| Connelly: "Good Place to Stop" test / "if the reader can find a comfortable stopping point, you've failed" | VERIFIED | `skills/michael-connelly-vivid-writing/genius.md:50` — read and quoted verbatim (paraphrase of surrounding sentence, bolded term quoted exactly) |
| Harding: "hate clutter" | VERIFIED | `skills/paul-harding-lyric-prose/genius.md:15` — read and quoted verbatim |
| Ocean Vuong: "I'm not arguing for maximalist sentences. I'm arguing for idiosyncrasy and strangeness" | VERIFIED | `skills/ocean-vuong-perceptual-writing/genius.md:25` — read and quoted verbatim |
| Shukman: "God is in the details. The wonder is in the details" | VERIFIED | `skills/henry-shukman-contemplative-writing/genius.md:15` — read and quoted verbatim |
| Ben Watkins: "name the machinery on the page and you break the spell" (paraphrased as "Name the machinery...") | VERIFIED | `skills/ben-watkins-storytelling/genius.md:14` — read and quoted (original: "Name the machinery on the page and you break the spell.") |

## Production-use / trace evidence

| Claim | Label | Source |
|---|---|---|
| how-i-write-os has 2 recorded v2 traces, both composite 7.25, both `workflow: extract-forge` | VERIFIED | `evolution_store/v2_traces/trace_20260626_030339_how-i-write-os.json`, `trace_20260626_030352_how-i-write-os.json` — read directly |
| Those traces certify production deployment quality | UNCONFIRMED — explicitly false if implied. `skill_auditor.py` (`BUILD_WORKFLOWS = {"extract-forge", "extract"}`, `execution/skill_auditor.py:388`) excludes `extract-forge` traces from the production-use trace signal precisely because they score the extraction/build itself, not a real deployment. Do not cite these two traces as evidence the OS performs well in live use — they are build-time scores only. |
| how-i-write-os has been invoked in live production missions beyond the two build traces | UNCONFIRMED | No trace files with `workflow` other than `extract-forge` were found under `evolution_store/v2_traces/*how-i-write-os*` at time of this repair (verified via directory listing, not assumed) |

## Structural / cross-reference claims

| Claim | Label | Source |
|---|---|---|
| `skills/writing-depth-layer` and `stanton-produce` share the same "conductor, owns no craft" posture cited repeatedly in this skill | LIKELY | `skills/writing-depth-layer/SKILL.md` and `skills/andrew-stanton-audience-engineering/workflows/stanton-produce.md` both self-describe as orchestrators of existing engines (spot-read during this repair); full line-by-line parity with how-i-write-os's phrasing not exhaustively diffed |
| The Output Receipt format mirrors "the Writing Depth Layer's receipt pattern" | LIKELY | `skills/writing-depth-layer/` workflow files (e.g. `depth-inject.md`) use an analogous "name every move, prove restraint" receipt block; not diffed field-by-field against this skill's receipt this session |

## What this ledger does NOT cover

This skill has no single expert biography, career facts, or public claims of its own
to verify (it is pure composition logic) — the claim inventory above is exhaustive for
what genius.md/SKILL.md assert as fact. Craft claims belonging to each of the 14
constituent experts (their own biographical facts, book titles, career history) are
governed by that expert's own `references/source-ledger.md` or equivalent, not
duplicated here.
