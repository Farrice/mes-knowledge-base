# Source Ledger — Dr. Mike Israetel Hypertrophy Skill

Every factual/quantitative claim in `SKILL.md` and `genius.md`, graded VERIFIED / LIKELY /
UNCONFIRMED against primary source. Written 2026-07-17 as part of Wave 3 Batch 2 heartbeat
repair (`.tmp/wave3-batch2/ENVELOPE.md`).

## Primary source — found, not absent

No `extractions/` folder exists for Israetel (`ls extractions/ | grep -i israetel` returns
zero matches). But the primary source is **not absent** — it is the two claude.ai
conversations referenced by `_active/claude-export/index.json`, whose transcripts are inside
the archive `_archive/claude-export-2026-07-01.tar.gz` (confirmed by `tar -tzf` listing and
extraction; file sizes below, not "0-byte"/"unrecoverable"):

| Conversation | File in archive | Extracted size |
|---|---|---|
| Pt.1 — "The Muscle Building Expert: They're Lying To You About Workout Hours! Pt.1" (2025-08-08) | `claude-export/normalized/conversations/715413da-8a4d-4388-9199-8ab7111661f5.md` | 167,160 bytes |
| Pt.2 — same title, Pt.2 (2025-08-10) | `claude-export/normalized/conversations/5405342c-7ba5-4d1c-9e74-76567eb75cbc.md` | 229,737 bytes |

Both files open with a Merlin AI YouTube-transcript attachment of the video
"[The Muscle Building Expert: They're Lying To You About Workout Hours! Dr Michael Israetel](https://www.youtube.com/watch?v=OTrTqs9FLq0)"
(the two conversations are two separate Claude sessions run against the same underlying
transcript — Pt.2 duplicates the opening ~80 minutes verbatim and extends further, into the
creatine/supplement/steroid segment used below). Both files were extracted to a scratchpad,
read in full, and every quote below was checked against the extracted text before being cited.
This ledger corrects the assumption (visible in the sibling `strength-conditioning-os` skill's
ledger, written earlier the same day) that "no raw transcript source exists" for Israetel —
that was true only in the sense that no `extractions/` folder exists; the raw transcript itself
is recoverable from the claude-export archive and was used here as primary ground truth.

VERIFIED = exact or near-verbatim (ASR transcription noise / filler words only) match found in
the transcript at the cited timestamp. LIKELY = the number/claim is consistent with what the
transcript states but involves a paraphrase, unit conversion, or rounding not itself dictated
by the transcript. UNCONFIRMED = a claim in the skill files that could not be located in either
transcript and is not disprovable, but also not directly evidenced — none found this pass; any
future addition to this skill that can't be pinned to transcript text should be labeled here
before shipping.

---

## Anti-Patterns (Sourced) — genius.md, new section added this repair

All 10 items added to close the `anti_patterns_sourced` heartbeat check. Every quote below was
re-checked verbatim against the extracted transcript text (not reconstructed from memory).

| # | Anti-pattern | Quote cited | Source | Confidence |
|---|---|---|---|---|
| 1 | Assuming transformation needs a big time budget | "two super common ones are I don't have the time to work out and into that time to work out is included I don't have regular gym access" | Pt.1 transcript, 3:44–3:52 | VERIFIED — exact string match |
| 2 | Treating "clean eating" fears as legitimate | "organic artificial sweeteners are bad glutenfree GMOs" / "Notions" (Sowell's term) | Pt.1 transcript, 5:34 and 6:38–6:43 | VERIFIED — exact string match |
| 3 | High protein damages healthy kidneys | "excessive protein as a health malady has been a myth the entire time" | Pt.1 transcript, 47:25–47:31 | VERIFIED — exact string match |
| 4 | Dismissing calories-in/calories-out | "it's totally myth it doesn't work no no it works great" | Pt.1 transcript, 53:58–54:03 | VERIFIED — exact string match |
| 5 | All-or-nothing dieting after one lapse | "if I'm off my diet not only am I bad but as soon as I'm off my diet I have sinned and there is no Solace for me" | Pt.1 transcript, 63:43–63:48 | VERIFIED — exact string match |
| 6 | Same plan to lose weight and to maintain it | "a huge myth is the fact that... once you've gotten to that weight you both need some time... at maintenance" | Pt.1 transcript, 65:51–66:08 | VERIFIED — exact string match (ellipsis marks elided words, no altered words) |
| 7 | Cardio to outrun a bad diet | "the average person will burn something like 100 to 150 calories per mile run" / "a doughnut has 300 calories" | Pt.1 transcript, 68:56–69:17 | VERIFIED — exact string match |
| 8 | Creatine loading protocol | "that's basically like a corporate scam that's just trying to get you to consume more creatine" | Pt.2 transcript, 75:52–75:56 | VERIFIED — exact string match |
| 9 | Supplement stack for a beginner | "supplements are just not in the conversation for important things" / "supplements are insanely overrated as a general rule" | Pt.2 transcript, 76:58–77:20 | VERIFIED — exact string match |
| 10 | Sloppy technique that still "feels like work" | "one of them is a failure to pay attention to good technique" | Pt.1 transcript, 43:58–44:00 | VERIFIED — exact string match |

## Genius Patterns (genius.md, pre-existing this repair) — spot-verified

| Pattern | Key claim | Quote/number checked | Source | Confidence |
|---|---|---|---|---|
| Needs Analysis Before Anything | Car-dealership analogy for open-ended goals | "walking into a car dealership and being like I want a car" | Pt.1 transcript, ~14:53–15:28 | VERIFIED |
| Specificity Is The #1 Principle | "Most important principle in all of exercise science" | "specificity it's the most important principle in all of sport painting [sic, ASR: 'training'] and exercise science" | Pt.1 transcript, 23:56–24:00 | VERIFIED (one ASR mis-transcription noted: "painting"→"training") |
| Overload | "Teeny dose of trepidation" | "approaching every real set with just a teeny teeny dose of trepidation" | Pt.1 transcript, 25:05–25:14 | VERIFIED (genius.md drops one repeated "teeny" — cosmetic, not a claim change) |
| Rep Range Is Wide, Not Magic | 5–30 reps statistically undifferentiated over "8-16 weeks" | "training for sets of roughly five reps and another group training for sets of roughly 30 reps and their change in muscle growth over 8 12 16 weeks is statistically undifferenced" | Pt.1 transcript, 743–748 | LIKELY — core claim (5 vs. 30 reps, no significant difference) is VERIFIED; the duration phrase "8 12 16 weeks" is ASR-garbled (likely "8, 12, 16 weeks" as separate study lengths) and genius.md's "8–16 weeks" is a reasonable but not exact rendering |
| Frequency Over Heroic Single Sessions | 2×/week floor, 2–4×/week best overall, exponential de-escalation | "twice is our minimum two to four times a week is what I say is kind of the best overall recommendation per muscle group" | Pt.1 transcript, 29:07–29:13 | VERIFIED |
| Minimal Effective Dose | Beginner: 2 sessions/wk, 2–3 sets/muscle; "20 min ×2/wk" | "two sessions a week with two to three sets per session... months and months and months of consistent progress" / "if you work out for 20 minutes twice a week you're going to get great gains" | Pt.1 transcript, 27:31–27:35 and 27:53 | VERIFIED |
| Minimal Effective Dose (SKILL.md figure) | "5–10 lb muscle gained and 5–15 lb fat lost over 6 months" | Transcript: "gain 5 to 10 lounds [pounds] of muscle" (matches) but "lose... five to 7 and 1 12 [likely 'seven and a half'] kilos of fat" — 5–7.5 kg ≈ 11–16.5 lb, not 5–15 lb | Pt.1 transcript, 530–539 | LIKELY — muscle-gain figure (5–10 lb) is VERIFIED verbatim; the fat-loss figure in SKILL.md/genius.md ("5–15 lb") does not cleanly match the transcript's kilogram figure once converted (≈11–16.5 lb) — flagging rather than silently correcting, since the original unit-handling (kg→lb) is ambiguous in the ASR transcript itself |
| Growth Happens Outside The Gym | "~80% of the stimulus" from tension-sensing; peaks 0.5–1.5 days, tapers ~4 days | "at least 80% of the muscle growth anyone will see is because of those receptors for tension" / "Peaks about half a day to a day and a half" / "half a week later it'll drop off back to Baseline" | Pt.1 transcript, 876–879, 898–900, 906–908 | VERIFIED (genius.md's "~4 days" taper is a reasonable rounding of "half a week," both consistent with the transcript's separate "four days afterwards" reference at 933–934) |
| Volume Landmarks & The Deload (MEV/MAV/MRV) | RP framework terminology and ramp-then-deload logic | Not a direct quote — "periodization" and "hypertrophy training" as terms are VERIFIED in transcript (22:33–24:00); the specific MEV/MAV/MRV vocabulary and deload mechanics are RP's published training-volume framework, not stated by name in this interview | Pt.1 transcript, 22:33–23:31 (periodization/hypertrophy terms only) | LIKELY — the MEV/MAV/MRV/deload terminology itself is not spoken in this transcript; it is Renaissance Periodization's well-documented public framework (RP Hypertrophy training app/guides), consistent with but not sourced verbatim to this interview |
| Calories Are The Engine, Macros Steer | "80/20" diet-vs-exercise heuristic; 100–150 cal/mile vs. 300-cal donut; CICO "incontrovertible" | "diet has a bigger effect than exercise as a heuristic I'm very comfortable with 8020" / "no one has ever violated laws of thermodynamic[s]" | Pt.1 transcript, 51:49–51:53 (CICO) and 67:00–67:16 (80/20) | VERIFIED |
| Phase The Diet, Build Habits Not Restriction | "~3 months hard cut → 2–3 months maintenance" | "roughly every 3 months that you diet hard to lose weight you should be taking about at least two months at maintenance" | Pt.1 transcript, 66:01–66:08 | VERIFIED (transcript says "at least two months," genius.md's "~2–3 months" is a slightly widened but directionally consistent range) |

## Hidden Knowledge (genius.md, pre-existing) — spot-verified

| Insight | Quote checked | Source | Confidence |
|---|---|---|---|
| Beliefs Are "Notions" | "Thomas soell [Sowell] calls them Notions" | Pt.1 transcript, 5:34 | VERIFIED |
| Warm-Up Is Nervous-System Priming | Light→medium→heavy ramp, "12/8/4" set pattern | "you want to do very lightweight... a set of 12... 10 or 15 lb dumbbells you do a set of eight reps... the 20 pounders... a set of two to four reps" | Pt.1 transcript, 38:52–39:41 | VERIFIED |
| Technique = Target, Consistency, Stretch | Curl-arc and squat-depth examples | "if you do a curl that arcs up it does a lot of bicep if you do a curl that arcs back this way... it ends up doing more of stabilizing contraction" | Pt.1 transcript, 44:17–44:35 | VERIFIED |
| Retraining Is ~10× Faster | 2-week no-loss window; "order of magnitude... factor of 10ish" | "within about two weeks of not training it the first reduction in muscle that is detected" / "it's going to take you an order of magnitude a factor of 10ish or so less time to get it back" | Pt.1 transcript, 33:49–33:57 and 36:45–36:48 | VERIFIED |
| Sell The Result, Titrate The Complexity | "12 reps at 50 lb" app example | "the hypertrophy app says first set is 12 reps at 50 pounds" | Pt.1 transcript, 21:58–22:03 | VERIFIED |
| Supplements Are Round-Off Error | Creatine 5 g/day, no loading; "not in the top 10" | "five grams per day for most people of creatine monohydrate" / "supplements are just not in the conversation for important things" | Pt.2 transcript, 75:44–75:46 and 76:58 | VERIFIED |

## SKILL.md — Quick Reference bullets

Every bullet is a compressed restatement of a genius.md pattern verified above; no new
quantitative claim appears in SKILL.md that isn't already covered by the tables above, except
the fat-loss figure flagged LIKELY above (which SKILL.md repeats).

## Out of scope for this ledger

`workflows/*.md` and `references/prompts-v2/*.md` are operational deliverable templates
(needs-analysis brief format, mesocycle skeleton, nutrition-plan skeleton) — they encode the
*process* from the Genius Patterns above but make no additional factual claims about Israetel
or exercise science that require independent sourcing. `workflow_contracts` and
`named_entity_floor` heartbeat checks were already passing before this repair and were not
modified (additive-first, minimal-touch per the repair envelope).

## Recognition-test language (genius.md, new this repair)

The "How to Use This Skill (Model Calibration)" section added to `genius.md` states: "would
Israetel recognize this as a program he'd actually assign a real client with a real time
budget — or as someone using RP vocabulary... without ever running the needs analysis." This
is original framing written for this repair, modeled structurally on
`skills/ben-watkins-storytelling/genius.md` lines 7–16 (per repair envelope instruction) —
not a quote attributed to Israetel himself, and not labeled as one.
