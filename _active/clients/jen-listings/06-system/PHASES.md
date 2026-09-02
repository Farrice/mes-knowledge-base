# PHASES — the audit of what survives, and the restart from here (living; update in place)

Farrice, 2026-09-02 (second pass): "We had things that worked, including a voice profile for her and recent voice memos from her... too many refinements became direct changes that shouldn't have... expert soup and too many things, and the orchestration is being poorly executed. I need us to do an audit and keep what's working, but then also zoom out and start from here."

Rule for every phase: nothing from a later phase is touched until the current phase has her thumbs-up and his triad. One lane. One pen. Zero recurring asks on Jen.

## The audit

**Keep** (it works; Phase 1 uses it)

| Asset | Why it stays | Where |
|---|---|---|
| Her real voice profile (July scrape) + the five voice memos (Sept 1) + calibration log | the only things on disk that are HER; every line she has said verbatim | `skills/jen-santulan-listing-content/references/jen-real-voice-profile.md`, `jen-calibration-log.md` |
| The dated facts ledger + realism gate | every number sourced and dated; the condo lesson | `04-deliverables/2026-09-06-engine-v2-weeks-1-2/FACTS.md`, `ENGINE-V2.md` §3 |
| The saved replies + "the door open" ask | the reply layer C&C doesn't have; her same-evening habit | weeks folder `saved-replies.txt`, `ENGINE-V2.md` §9 |
| The weekly renderer (one family) | cards and reels from her photos, already proven | `build_weeks.py` → `gen_photo.py` / `build_reel.py` |
| The read loop | Monday public numbers + monthly outlier audit; the evidence that life-first hooks win | `execution/jen_pulse.py`, `04-deliverables/jen-outlier-audit.md` |
| The hook rule | her own numbers: the house is never the hook | `CONTENT-MIX.md` §"The hook rule" |
| Stamp-lint + fair-housing lint | mechanical, two-direction tested, no taste | `execution/jen_stamp_lint.py`, `execution/fair_housing_lint.py` |
| The deal | thumbs-up + reply DMs; she said yes to this shape | `ENGINE-V2.md` §2, the reset memo |
| The one-page readout | the only form he could judge | `execution/jen_os_page.py` → The Valley OS |

**Freeze** (built, not wrong, not now)

| Asset | Returns when | Where |
|---|---|---|
| District shares (Attract 45 / Connect 25 / Position 15 / Convert 15) | after the first monthly read; Phase 1 = three unlabeled slots | `CONTENT-MIX.md` |
| Valley Editions (six Canva grammars, editions.py, Edition 01), AI plates, Canva route | Phase 3, as vault material | `06-system/valley-editions/` |
| Connect set 02–04, funnel math, FUNNEL ramp | Phase 2 (Connect) / Phase 3 (funnel), once her four numbers exist | `04-deliverables/connect-posts-01/`, `FUNNEL-MATH.md` |
| Alyssa Stalker skill beyond two files | only `01-outlier-audit` (monthly) and `03-hook-reframe` (the pen) stay in play | `skills/alyssa-stalker-agent-content-playbook/` |
| The 6.66% rate post, Armida, Moonseed, Willis packs | banked in VAULT; a slot when a listing or a month asks for it | `VAULT.md` |
| Deep research record | reference; VERIFY before any number reaches a post | `2026-09-02-deep-research-what-works-valley-agents.md` |

**Cut** (stepping on each other; done today or listed for Farrice)

| Asset | Verdict | Status |
|---|---|---|
| `skills/jen-engine` (intake questionnaire + 20 talking-head videos) | she refused both premises | archived by frontmatter |
| `skills/jen-shortform-carousel-engine` (zero workflows, unminted commands) | dead surface | archived by frontmatter |
| The six-seat "amplify room" (Alyssa, Luke Iha, Sam Parr, Kallaway, Georgi + Jen) | expert soup, added today, removed today | `/jen` step 4 = one pen + one check |
| Every other skill that routes to "Jen" (enrico, sherrard, satori listing frame, meg listing copy, jenny hoyos, the old listing wrappers) | not loaded in Phase 1; `/jen` is the only door | routing left as-is; the door is the fix |
| Eight Jen branches, three generators of `new_set.py`, tracked `.reel_tmp` renders | fragmentation | branches: Farrice deletes on main; copies: leave, never run |
| The March "warm-enthusiastic, emoji-rich, @realestatewithjing" voice paragraph | wrong voice; the July scrape and Sept memos win | rewritten in client `CLAUDE.md` |

## Phase 0 · her own words, from her own account (this week, before any post)

Run the extraction pack in her ChatGPT (`JEN-CHATGPT-PROMPTS.md`): Farrice pastes the prompts with her login, once. The outputs land in `06-system/jen-chatgpt-outputs/` as six files with fixed names. One merge pass folds them into `jen-real-voice-profile.md` as a new section, **additive, never overwriting the memo lines**; contradictions go to the calibration log as rows for her "that's me / not me." No ask on Jen except reading the merged profile once.

Done when: the profile has her ChatGPT-era lines, her ICP in her words, her ten stories, and her never-say list, each quote marked HERS or INFERRED.

## Phase 1 · one week, one pen (the week after Phase 0)

Three posts. `/jen` with the Phase-1 shape: LOAD (profile + memos + extraction outputs + facts) → RESEARCH (ledger rows) → WRITE (one pen, hook rule, voice bank once) → CHECK (fair-housing, stamp-lint) → RENDER (her photos where they exist) → DELIVER (the page, then the Drive folder). Three unlabeled slots; no districts, no mix ratios, no room. Her thumbs-up, his triad. Two rejected takes on one post = back to the input.

Done when: she posts three and replies from the saved replies. That is the first real number.

## Phase 2 · the read (weeks 2–4)

Monday pulse each week. Weeks 2–3 re-run through the same door (they still carry the old stamp). First-of-month outlier audit names the attribute. Only then: district labels and shares come back, set by her numbers, not the extractions. Connect set enters as the evidence allows.

## Phase 3 · the system she can keep (month 2+)

Valley Editions and plates as vault material. Funnel math with her four numbers. The port decision: her ChatGPT (a Project carrying the profile, the ledger shape, the prompts) versus a Codex account running this repo's Jen lane. Decided by what she actually touches in months one and two, not designed now.

## What changed in this pass (2026-09-02, second pass)

- `/jen` step 4: six seats → one pen + one check.
- `CONTENT-MIX.md`: shares frozen; hook rule and capture rule stay.
- Client `CLAUDE.md`: amplify line rewritten; points here.
- New: this file, `JEN-CHATGPT-PROMPTS.md`.
- Untouched: everything in Keep. Nothing in Freeze was deleted.
