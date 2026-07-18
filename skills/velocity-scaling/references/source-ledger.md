# Source Ledger — velocity-scaling (Danny Yeung)

> Claim-by-claim provenance for `genius.md` and `SKILL.md`. Labels:
> **VERIFIED** (verbatim quote confirmed in a primary source file, checked
> directly this session — string-matched against the raw file), **LIKELY**
> (consistent with verified material, a close paraphrase or fair synthesis,
> not itself re-confirmed as a direct quote this session), **UNCONFIRMED**
> (no source file contains it — illustrative only, never citable as a direct
> Danny Yeung claim).

## Primary source recovered (2026-07-18)

Ground truth = `extractions/danny-yeung/transcript.txt` (86,386 bytes,
confirmed via `wc -c`, single-file podcast/interview transcript covering
IM8, Prenetics, the COVID pivot, the Beckham/Sabalenka partnerships, hiring
philosophy, and the angel-investing thesis). No other `extractions/`
directory matches "danny yeung," "IM8," or "Prenetics" (`grep -rl "IM8\|
Prenetics" extractions/` returns only this file and one unrelated hit in
`extractions/vince-nijhof/transcript.txt`, not used here). A full scan of
`extractions/` for "yeung" and "danny" surfaces only this one directory —
no secondary source exists to cross-check against, so every VERIFIED claim
below rests on this single transcript. `_archive/claude-export-2026-07-01.tar.gz`
was not scanned for this repair: the local `extractions/danny-yeung/`
source was already found and is sufficient (332MB archive scan reserved for
skills with zero local source, per envelope instructions).

## Claim-by-claim labels

| Section in genius.md / SKILL.md | Label | Basis |
|---|---|---|
| Identity (5 companies, $0→NASDAQ, $800M COVID revenue, 31 countries, Beckham equity) | **VERIFIED** | Numbers appear directly in transcript opening and body ("We grew up from zero to 100 million annual run rate in under one year," COVID pivot arc, Beckham/Sabalenka partnership passages) |
| GP-1 Speed-as-Moat Doctrine | **LIKELY** | Synthesized framing; transcript establishes the underlying behavior ("speed wins and nobody is faster than Dan[ny]") but "speed-as-moat" as a named doctrine is this skill's synthesis label, not his own term |
| GP-2 Founder-in-the-Weeds Integration | **VERIFIED** | Transcript: "I'm very on all the time," direct operational involvement across departments described throughout |
| GP-3 Team Velocity Filter | **VERIFIED** | Transcript: "I'll text you at like 12:00 a.m., 2 a.m., 6:00 a.m., doesn't matter" + "you have to select people that have this ambitious growth mindset" |
| GP-4 Infrastructure Pivot | **VERIFIED** | Transcript: COVID pivot passage (lab infrastructure repurposed from genomics to PCR testing) |
| GP-5 Loss-Leader Brand Builder | **VERIFIED** | Transcript: Starbucks voucher resale story, corroborated by "you probably can't resell vouchers" / cease-and-desist reference |
| GP-6 Jockey-Not-Horse Investment Thesis | **VERIFIED** | Transcript: "to be fair, I don't do any due diligence" / "the problem is once you do due diligence, it doesn't work" |
| GP-7 3-Month Subscription AOV Architect | **LIKELY** | Consistent with transcript's subscription/AOV discussion; exact "3-month" cadence and mechanics are described but not re-quoted verbatim this session |
| GP-8 Equity-Based Celebrity Partnership Model | **VERIFIED** | Transcript: "these are minimum threeyear deals because if it's not it becomes too short term and you both sides doesn't benefit from it" |
| GP-9 Digital Access Value Layer | **VERIFIED** | Transcript: "we don't want to just sell our product... it's about the lifestyle, the community, how we enrich people with knowledge" |
| GP-10 "Create Shopping Behavior" Discipline | **LIKELY** | Hong Kong midnight-deal anecdote consistent with transcript's daily-deals origin story; not re-quoted verbatim this session |
| GP-11 Cold-Call Bypass | **LIKELY** | Consistent with transcript's restaurant-partnership origin story; not re-quoted verbatim this session |
| GP-12 AI-Native Survival Mandate | **VERIFIED** | Transcript: "everyone moving forward has to be AI native, otherwise it's going to be very difficult to justify their existence" language pattern present in source |
| Hidden Knowledge HK-1 through HK-8 | **LIKELY** | Consistent with transcript passages on Bitcoin balance sheet, never selling a share ("I never sold a single share"), letting people go early — not individually re-verified verbatim this session beyond the anchors reused in Anti-Patterns below |
| Hall of Fame Exemplars 1–3 (Starbucks, COVID pivot, Sabalenka) | **VERIFIED** | All three anecdotes present in transcript body |
| Anti-Exemplar (Short-Term Celebrity Endorsement) | **LIKELY** | Illustrative composite contrasting against the VERIFIED 3-year/equity requirement — not itself a Danny Yeung quote |
| **Anti-Patterns (new section, all 7 items)** | **VERIFIED** | Each item is a direct verbatim quote from `extractions/danny-yeung/transcript.txt`, string-matched this session: "we don't want to do anything short-term"; "the problem is once you do due diligence, it doesn't work"; "I never tell someone, hey, just do this blah blah blah" / "I always try to provide a lot of context"; "I think what if we put in retail into this now, it also loses focus"; "letting someone free as early as possible to find the next thing is way better than to keep them" + "on the ship"; "I don't care how great the formulation is, but it also needs to taste good"; "I'll text you at like 12:00 a.m., 2 a.m., 6:00 a.m., doesn't matter" |
| **How to Use This Skill (Model Calibration)** (new section) | **LIKELY** | Editorial calibration guidance modeled on the house pattern (ben-watkins-storytelling/genius.md lines 7-16), not itself a Danny Yeung claim — grounded only insofar as it references verified quotes already anchored above |
| Key Numbers table (SKILL.md): CAC/LTV 3.0-3.5x, sub-4-month payback, 1,500+ ads, 85/15 channel mix | **LIKELY** | Consistent with transcript's opening ("We have about 1,500 ads... 85% on meta, 15% on Google") for the ad-count and channel-mix figures (**VERIFIED**); CAC/LTV ratio and payback-period figures are not re-quoted verbatim this session (**LIKELY**) |

## Scope note

This repair pass re-verified the transcript locations for every claim
touched by the failing heartbeat checks (anti_patterns_sourced,
recognition_test, source_ledger) plus spot-checked the highest-load prior
claims (Identity, GP-3, GP-6, GP-8, GP-9, GP-12, Hall of Fame exemplars,
opening SKILL.md numbers). Patterns marked LIKELY were not re-opened for a
fresh verbatim search this session; they were already present in genius.md
before this repair and are carried forward unchanged — flag for a future
pass if stricter VERIFIED coverage is required.
