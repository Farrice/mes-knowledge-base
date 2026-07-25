---
thread: bc-arsenal-install
status: ready
resume_hint: Farrice blind-pass a fresh /bc-win-audit output (A-tier gate), then draft the Monday 'I stopped saying personal brand' post from the week-1 slate
unfinished: A-tier blind pass pending Farrice's verdict; LinkedIn baseline dashboard unfilled; 2 mis-scrape Notion pages need deleting
branch: main
pin: true
---

# Briar Cochran Content Science — Forge Extraction + LinkedIn Arsenal Install (week-1 slate)

## Purpose

- **Next session should do:** (1) Farrice-judged A-tier blind pass on a `/bc-*` output vs Briar's
  real transcripts, (2) draft the Monday LinkedIn post from the week-1 arsenal slate, (3) delete
  the 2 mis-scrape pages sitting in the Social Intelligence Notion DB.
- **Not in scope:** rebuilding any part of the skill (extend only), re-scraping Briar (corpus is
  banked), re-solving the `/scrape-creator` bugs (both fixed and carded).

## Load First

- `skills/briar-cochran-content-science/SKILL.md` + `genius.md` — the 12-workflow OS; genius.md is
  the decision framework every `/bc-*` run loads.
- `_active/linkedin-launch/04-content-os/BC-ARSENAL-INSTALL-2026-07-25.md` — the install pack:
  through-line, 14-entry keyword ledger, five-input source map, cold-start arsenal ledger,
  week-1 slate, baseline capture dashboard, anti-pattern contract.
- `extractions/briar-cochran-content-science/reference-corpus/` (2 transcripts) +
  `blind-pass-sample-win-audit.md` — the side-by-side pair for the A-tier judgment.
- `_active/farrice-brand/voice/VOICE-CARD.md` §4 (LinkedIn register) + `PLATFORM-NARRATIVE-CARD.md`
  §2 (LinkedIn = I-story arc, FULL, polished, HOT) — both required before drafting any post.
- `docs/solutions/2026-07-25-social-intel-date-normalization-and-watch-url-parse.md` — what broke
  and why it can't recur.

## Current State

- **Objective:** ship Briar Cochran's data-backed ideation + testing-arsenal system as a callable
  OS, then run it once against Farrice's real LinkedIn launch.
- **What is already done:**
  - `/watch` on both source videos (frames + transcripts, whiteboard frameworks captured in
    `extractions/briar-cochran/visual-context.md`).
  - `/scrape-creator` → Social Intelligence DB batch `briar-2026-07-25`: 4 Briar pages with
    metrics + transcripts + grounded per-post analyses; 2 source videos flagged Extract Candidate.
  - Full `/extract-forge`: vision, MES 3.0 Deep report (13 genius patterns, 3 exemplars +
    anti-exemplar, 6 signature moves, 8-criterion rubric), genius.md, 12 workflows in 3 tiers
    (`/bc-*`), 8 born-v2 prompts (renaissance audit 3715 pass / 0 fail), AGENT.md, front door
    `/briar-cochran`, registries synced. Heartbeat gate 6/6. Blind pass EVAL-056 model-judged PASS.
  - Two `execution/social_intel.py` fixes, both tested: `_to_date()` normalizes human/epoch/
    YYYYMMDD dates instead of truncating (was causing Notion to reject whole pages); `clean_handle()`
    now resolves single-video URLs to the uploader handle via yt-dlp or exits loudly.
  - `/bc-arsenal-install` run for Farrice's LinkedIn (install pack above).
  - Commits `b81935566` + follow-up on `main`, pushed; session lock released.
- **What is uncertain or stale:**
  - **Tier is B, not A.** Model-judged PASS only — A-tier promotion requires Farrice's own blind
    pass (`execution/blind_pass.py record` again with his verdict).
  - **No LinkedIn baseline exists.** Nobody in the system can read Farrice's analytics; the
    dashboard in the install pack is an unfilled 5-minute capture protocol. Week 1 is all-test
    so the slate does not depend on it, but outlier thresholds stay uncomputable until he fills it.
  - **Briar's self-reported stats are UNCONFIRMED and internally inconsistent** (250M views/mo in
    one video vs ~1B/yr in another). Claim-hygiene note lives in `references/source-quotes.md` —
    never cite his numbers as fact.
  - 2 junk Notion pages renamed `🗑️ [MIS-SCRAPE — SAFE TO DELETE]` — deletion needs Farrice
    (archive call was permission-blocked; Notion MCP cannot trash).
  - Subreddit member counts in the five-input map are candidates, flagged verify-first.
- **Latest proof/receipt:** `python3 execution/skill_auditor.py check --skill
  briar-cochran-content-science` → 0/6 failing, GATE clear · `renaissance_audit.py` → 0 fail ·
  blind-pass ledger `extractions/briar-cochran-content-science/blind-pass-log.md` (EVAL-056).

## Suggested Skills / Workflows

- `/bc-win-audit` or `/bc-idea-gate` — generate the fresh output for Farrice's blind pass (Tier-1
  workflows are the fair test).
- `/ghostwrite` + `/writers-room` — Monday post production; writers-room is the DEFAULT for
  content ≥500 chars per the farrice-brand override list.
- `/voice-ratchet` — bank Farrice's felt verdicts on the slate posts as they land.
- `/bc-ideation-hour` → `/bc-arsenal-week` — the Sunday sacred hour that produces week 2.
- `/riley-lara-amplifier` — bank a non-sponsored LinkedIn exemplar corpus before the ideation hour.

## Exact Next Prompt

```text
Two things. First, generate a fresh /bc-win-audit output so I can blind-pass it against Briar's
real transcripts — show me the generated piece and the reference side by side, then record my
verdict. Second, draft the Monday post from the week-1 slate ("I stopped saying personal brand")
— full BLEND voice, writers-room diagnosis-first, reader-contract check before you hand it over.
```

## Acceptance Criteria

- Farrice's own PASS/FAIL recorded via `blind_pass.py record` (A-tier promotion or a named gap).
- Monday post drafted at production grade: statement hook, front-loaded concrete detail, no
  banned moves, CTA in first comment only, reader-contract trio passed.
- The 2 mis-scrape pages gone from the Social Intelligence DB.

## Risk Notes

- **Voice risk:** the Monday post subverts a BURNED keyword ("personal brand"). It must read as
  Farrice's reframe, never as him adopting the term — wince test applies.
- **Privacy law:** the $14K niche-down scene is cleared corpus; family specifics (father, mother,
  brother) are not. Dramatize the pattern, never the family autobiography.
- **Grade-inflation risk:** the skill is B-tier. Do not describe it as A-tier anywhere until
  Farrice's blind pass lands.
- **Claim risk:** any client-facing use of Briar's methodology must not carry his view numbers.
