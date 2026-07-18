# Source Ledger — harry-dry-copywriting (Wave 3 Lane 4 repair, 2026-07-18)

Ground truth for this repair pass is a single file — no other Harry Dry
extraction exists in the repo (confirmed: `ls extractions/ | grep -i dry`
returns nothing; `find . -iname "*harry*dry*"` surfaces only skill/agent/
research/swarm-output files that reuse this one extraction, plus this
extraction itself under two additional worktree/harvest copies of the
same file).

## VERIFIED

- **knowledge/extractions/inbox/Claude-💎💎💰 Harry Dry ! Learn Copywriting in 76 Minutes.md**
  — size 274,481 bytes (`wc -c`), 6,729 lines (`wc -l`). Full Claude-generated
  extraction transcript covering the 20 Genius Patterns, Hidden Knowledge,
  Hall of Fame Exemplars, and ~14 practitioner prompts with worked examples.
  Every new quote added to `genius.md` in this repair pass (Anti-Patterns
  section + 14 zero-entity enrichments) is a verbatim or verbatim-with-
  ellipsis substring of this file, checked programmatically against the raw
  file text before delivery. Line numbers cited inline next to each quote.

## LIKELY

- Attributions inside the transcript that read as **worked exercise output**
  rather than Harry Dry's own historical ad copy — e.g. the SaaS Falsifiability
  Filter rewrite ("NPS of 72..."), the finance-app Conflict Injection rewrite
  ("You don't have a spending problem..."), the EV-truck juxtaposition line
  ("Tougher than an F-150..."), the newsletter openers ("It's 11:43 p.m...",
  "I reviewed 47 landing pages..."), and the law-firm credibility stack
  ("127 years of combined experience..."). These are the extraction's own
  demonstration text for how Harry's frameworks apply — genuinely present in
  the source, genuinely illustrative of his method, but not verified as real
  ads Harry personally shipped. Labeled "worked example" / "deploy example"
  in `genius.md`, never presented as historical fact.

## VERIFIED (real, externally documented ads referenced by name in the transcript)

- Apple iPod, "1,000 songs in your pocket" (2001) — referenced at transcript
  lines 177 (existing Exemplar), 2175, 6146.
- The Economist, "management trainee, aged 42" — referenced at line 6146.
  Well-documented real Economist print campaign.
- Volkswagen, "Lemon" — referenced at line 3430. Well-documented real 1960s
  VW ad (Doyle Dane Bernbach).

## UNCONFIRMED

- None added in this pass. No claim in the new content lacks a locatable
  source string in the transcript above.

## Pre-existing (unchanged by this repair)

- `references/prompts-v2/example-mining.md` — carries its own CONFIRMED/
  UNCONFIRMED verification-status language for the Example Mining Protocol
  workflow. Not touched in this repair (source_ledger check already passed).
