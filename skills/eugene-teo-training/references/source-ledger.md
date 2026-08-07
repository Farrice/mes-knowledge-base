# Eugene Teo — Source Ledger

Claim-by-claim provenance for `SKILL.md` and `genius.md`. Labels: **VERIFIED**
(verbatim or numerically exact in a source transcript), **LIKELY**
(source-consistent paraphrase, synthesis of two adjacent transcript beats, or
reasonable extrapolation with no single verbatim anchor), **UNCONFIRMED** (no
supporting text found in any source file located for this repair pass —
carried forward anyway, flagged so it is never mistaken for verified
authority).

## Sources Consulted

Ground truth = two YouTube transcripts (Merlin AI auto-transcription), each
pasted into claude.ai as the seed of an extraction conversation, then
re-extracted 2-3 times in separate sessions. No `extractions/eugene-teo*`
directory exists on disk (`ls extractions/ | grep -i teo` and `| grep -i
eugene` both return nothing) — every source file lives inside the
claude.ai-export archive, located via `_active/harness/claude-export/index.json`
(conversation index) and pulled from `_archive/claude-export-2026-07-01.tar.gz`
(`claude-export/normalized/conversations/<id>.md`). All five files were opened
and read in full this session; none were 0 bytes or unrecoverable.

| ID | File (path inside the tar) | Size | Video | Created |
|----|------|------|-------|---------|
| S1 | `claude-export/normalized/conversations/e1467ecf-3d23-459d-9405-288897f11799.md` | 134,857 bytes | "I cut my training by 70% (and got better results)" — youtube.com/watch?v=8o51DYWBj3s | 2025-04-28 |
| S2 | `claude-export/normalized/conversations/8b2453c0-eca7-4e67-aa3b-3ebf8804c070.md` | 61,937 bytes | same video as S1 (re-extraction) | 2025-06-02 |
| S3 | `claude-export/normalized/conversations/9f6977e3-ff9b-46ff-b704-9521cf04e2e7.md` | 61,821 bytes | same video as S1 (re-extraction, Sonnet 4.5) | 2025-10-11 |
| S4 | `claude-export/normalized/conversations/6f64e7f8-abe0-4a32-8cb4-b82c28458103.md` | 149,748 bytes | "The only workout I do now (takes 40 mins)" w/ Matt D'Avella — youtube.com/watch?v=WLgcXwpVvlA | 2025-05-30 |
| S5 | `claude-export/normalized/conversations/e4953b15-38e5-4145-89ac-a1c046ed1989.md` | 75,416 bytes | same video as S4 (re-extraction, "MES 3.0") | 2025-07-02 |

S1/S2/S3 carry an identical underlying transcript (same raw paste, re-run
through different extraction prompts across three sessions); S4/S5 likewise
share one transcript. All quote/timestamp anchors below cite whichever of the
duplicate files was open at verification time — the same text is present in
its sibling(s).

## Claims — SKILL.md

| Claim | Label | Anchor |
|---|---|---|
| "strength coach and educator, 20-year competitive-bodybuilding background" | VERIFIED | S2 @ 1:43 ("Eugene is a strength coach and educator") + S2 @ 4:41 ("When I first started bodybuilding, this is nearly 20 years ago...") + S2 @ 4:01 ("As a competitive bodybuilder, he obsessed over every variable..."). |
| "stop chasing the 1% marginal gains, master the 99% foundations" | VERIFIED | S2 @ 3:56-4:15: "For most of his life, Eugene was focused on chasing the 1% gains... But now his focus has shifted to the 99%. He's more interested in the foundations: movement quality, longevity, recovery..." |
| "'suboptimal on any single axis, but still highly effective, and you cover all your bases'" | LIKELY | Synthesized phrasing; the underlying trade-off is VERIFIED (see genius.md Hidden Knowledge "Suboptimal-but-Effective Beats Optimal-but-Narrow" below), but this exact sentence is not a single verbatim line in any transcript — it compresses two separate beats. |
| Five qualities (hypertrophy, strength, power, mobility, endurance) trained together in 30-40 min, 2-5 days/week | LIKELY | Session length ("takes 40 mins") is the video title itself (S4/S5); "2-5 days" and the specific five-quality list are the extraction author's structuring of material spread across both transcripts, not a single verbatim enumeration by Teo. |
| "One exercise per movement pattern instead of four. One effortful set instead of three token ones." | VERIFIED | S2 @ 12:39 (movement-pattern consolidation) + S2 @ 17:29-17:56 ("the science is pretty clear... even just one set is enough... not the three sets you've been doing" / "three sets of 10, four sets of eight, five sets of five... just token rep schemes"). |

## Claims — genius.md, Genius Patterns

| Claim | Label | Anchor |
|---|---|---|
| Redundancy Removal — movement patterns list (squat/hinge/lunge/horiz. push/horiz. pull/vert. push/vert. pull + shoulder raise/elbow bend) | VERIFIED | S2 @ 12:30-12:39: "shoulder raise or bend the elbow... exercise per movement pattern." |
| "switching a dumbbell fly for a cable fly is a 1-10% change" | LIKELY | S2 region ~15:00-15:22 confirms the underlying claim (complex muscles get "slightly different" stimulus from a second angle, "not wrong," but optional) — the specific "1-10%" figure and the fly-vs-fly example are the extraction author's illustrative gloss, not Teo's verbatim numbers. |
| One Effortful Set — "the science shows a single hard set is enough... Dorian Yates, 6× Mr. Olympia, did one working set" | VERIFIED | S2 @ 18:03-18:21: "Dorian Yates, six time Mr. Olympia winner. He would just do one set for an exercise... he wasn't an anomaly. There were many people who were doing very similar approaches with very very low volume." |
| "as the sets drop, intensity must rise" | VERIFIED | S2 @ 18:24-18:35: "as that comes down sets the intensity must come up. You got to make sure you're squeezing every single last bit of effort out of your body." |
| Effort Miscalibration — 100kg/10-rep self-report vs. 20 actual reps (~10 in reserve) | VERIFIED | S1 @ 21:08-21:32 ("some research done with hundreds of participants... trained individuals... 'I might do 100 kilos'... you get 20... you're actually got 10 reps left in reserve"). |
| "~3 reps shy of failure gives a nearly identical hypertrophy response with far less fatigue" | VERIFIED | S1 @ 20:30-20:57: "modern research has also shown that if you train within about three reps shy of that absolute breaking point, you can get very similar responses for muscle building... the magnitude of fatigue and recovery debt... is significantly more." |
| Progressive Overload — "next time you train... can you do more" as the non-negotiable test | LIKELY | No single verbatim line states this exact test; it is a reasonable synthesis of the transcript's repeated progression language ("Let's record what you're doing and if it's going up over time over the next few months, happy days" — S1 @ 22:06-22:15) and the E2MOM "minimum standard you must beat" framing (S2 @ 27:56-28:24). Core idea VERIFIED across both citations; the specific framing as a named "test" is the extraction author's construction. |
| Time-Cap Everything — 12-minute E2MOM, sets of five paired lifts, "stolen from CrossFit" | VERIFIED | S2 @ 28:41-29:23: "we're going to use a 12 minute timer... this is something that I stole from CrossFit. They use a lot of E-OMs or E E2Ms... every 2 minute interval... a set of five on squats and a set of five on the overhead press." |
| "warm up over the first 3-4 of the 6 rounds... find a real working weight (~70-80% of a hard single)" | LIKELY | S4 @ 7:36-7:47 gives an absolute example weight for that specific session ("we'll air on the side of caution like 70 to 80 kilos tops") and confirms warm-up-into-work-set structure ("we'll gradually warm up till maybe uh set three or four out of the six total") — the genius.md conversion of that one anecdotal number into a general "~70-80% of a hard single" percentage rule is the extraction author's generalization, not a stated percentage rule in the transcript. Downgraded from VERIFIED to LIKELY here; flag for correction on next full pass. |
| "CrossFit's timed sets get hated on because they have no progression baked in" | VERIFIED | S2 @ 30:01-30:09: "Crossfit gets hated on a lot for these kinds of timed sets because they don't necessarily have a progression in mind." |
| Active Rest — "~70% of gym time is rest," scapular push-ups / hamstring stretch between sets | LIKELY (70% figure) / VERIFIED (scapular push-up as active-rest example) | The "~70%" rest-time figure is not stated as a number in any transcript located — LIKELY, an editorial estimate. The scapular-push-up active-rest example is VERIFIED: S4 @ 19:01-19:15 ("we're going to do one active rest thing... push-up position... Scapular push-up... this is something that's getting us into what's called protraction"). |
| Convergent Exercise Design — katana extension (Deadpool sword-unsheathe imagery, shoulder-mobility stretch) | VERIFIED | S2 @ 12:59-13:36: "The katana extension... imagine you are Deadpool and you are unsheathing a katana... Not for any gains whatsoever [as a joke about the name]... using this another opportunity to really open your shoulder mobility... imagine you're trying to scratch your back." |
| "seated/Z-press overhead press removes the lower-back arch compensation" | VERIFIED | S4 @ 6:57 ("a seated on the floor Z press") + S4 @ 9:42-9:52: "Often when you're doing an overhead press like seated on a bench or even standing, you'll compensate by leaning back a lot and really arching your back... this also challenges [you not to]." |
| "bro curl performed in a deep squat (Franco Columbu's move)" — front-loaded bias, opens hips while curling | VERIFIED (the move itself) / **UNCONFIRMED** (the "Franco Columbu" attribution) | S4 @ 24:20-25:13 verifies the move verbatim: "instead of doing just a regular standing curl, I'm going to get you to sit down to a squat position... This is a bro curl... it helps us open up your hips whilst getting the curl gains." No transcript located names Franco Columbu as the originator of this move — that attribution does not appear in S1-S5 and could not be verified this pass. Recommend downgrading the Franco Columbu credit to UNCONFIRMED in the next content pass (out of scope for this repair — additive-only). |
| Copenhagen plank ("never-touched adductors") | VERIFIED | S4 @ 39:42-39:57: "Have you ever done a Copenhagen plank before?... we are working the inner thigh muscles here, the adductors. Something that people just don't touch whatsoever in their training." |
| "partial reps at true end-range... on isolation work" litmus test | LIKELY | No single transcript line states the "partials as an effort litmus test" framing directly; it is a reasonable synthesis of the katana-extension stretch/stability discussion (S2 @ 13:36-13:44: "the more we can find ways to stabilize your body and the moving joints, the better because you can push harder") combined with the general effort-calibration material above. Core mechanism plausible and consistent with his stated logic; not independently verbatim-anchored. |
| Strategic Warm-Up — squat day targets ankles/hips/lower back; 5-minute window; plyometrics/pogos for tendon stiffness; deep hip-flexion (knees-to-chest) drills | VERIFIED | S4 @ 2:48-4:34: "how can we strategically use this 5-minute period... we want ankles today. We want your hips... your lower back prepared for squatting... some very, very basic plyometrics, some pogos... pull your knees in towards chest as much as you can... that's where you're going to be in the bottom of the squat." |
| "deadlift day: shoulders, lower-back/core" as the parallel warm-up target | **UNCONFIRMED** | No transcript segment locates a second, explicitly-named "deadlift day" warm-up target list analogous to the squat-day one above. S1-S5 contain plenty of deadlift-adjacent content (hinge pattern, pull-ups) but not this specific tissue-target enumeration. Flag for verification against a source not captured in this archive (possible ebook/program material referenced but not transcribed, e.g. S2 @ 23:44-23:52 mentions "the ebook covers all of that" as a separate paid asset never pasted into these conversations). |
| "scapular pull-ups and hollow-body holds to prep the pulling and trunk" | LIKELY (scapular work) / **UNCONFIRMED** (hollow-body holds) | Scapular work is VERIFIED as an active-rest movement (see Active Rest row above) but appears in the transcript as a **scapular push-up**, not a scapular pull-up, and in an active-rest context, not the dedicated warm-up. "Hollow-body holds" as a named drill does not appear in any of S1-S5. |

## Claims — genius.md, Hidden Knowledge

| Claim | Label | Anchor |
|---|---|---|
| The 60-Minute Health Ceiling — mortality-risk benefits tap out ~60 min/week; cultural belief is ~5 hrs/week | VERIFIED | S2 @ 31:19-31:47: "How many hours do you think you need to be spending with resistance exercise... Probably what I was doing before I became a parent, which was like 5 days a week, 1 hour a day... 5 hours of resistance training per week. Surprisingly, all the health benefits like lower mortality risk, they tap out after 60 minutes per week." |
| "spread across five days that's ~10-20 minutes a session" | LIKELY | S2 @ 31:47-31:53 gives "20 minutes or so... even less, 10 minutes" as an in-the-moment estimate during the conversation, not a precise stated protocol — directionally VERIFIED, exact range is an approximation carried from a loosely-stated on-camera guess. |
| 99% of Programs Are Bodybuilding in Disguise — "perpetuated from big bodybuilder... not malicious, just what we've known" | VERIFIED (with one transcription-artifact caveat) | S2 @ 6:46-7:05: "most of what we're doing is perpetuated from big bodybuilder, like big pharma. Not in a malicious way, but it's just from what we've known as a culture." Note: the Merlin-AI auto-transcript renders this as "big pharma" (not "big farmer" — corrected after re-reading; the genius.md quote matches the transcript verbatim). |
| Suboptimal-but-Effective Beats Optimal-but-Narrow — "80% of the powerlifting gains... happy days" | LIKELY | No single verbatim "80% + happy days" sentence located; it synthesizes the 60-minute-ceiling "happy days" phrasing (S2 @ 22:13-22:15, said in a different context — one-set progression) with the general suboptimal-but-covers-all-bases framing that runs throughout both transcripts. The specific "80%" figure is not stated by Teo as a number in S1-S5. |
| "for a competing powerlifter... concurrent conditioning is a bad idea" | LIKELY | Consistent extrapolation from the "weight training and endurance training... you're probably going to do them both suboptimally" line (S4 @ 26:56-27:14) applied to the specialist-athlete case; not a verbatim powerlifter-specific statement in the transcripts read. |
| Range Is Exercise-Specific — deadlift doesn't get true full range without a deficit | VERIFIED | S4 @ 35:58-36:05: "we're not getting full range of motion... high deficit and you'd be reaching down... true full range. So, we pick it based on..." |
| Tempo demystified — "adding 5 extra seconds to the lowering does nothing... super-slow reps are fashionable, not more effective" | VERIFIED | S4 @ 25:17-25:48 (quoted in full in the new Anti-Patterns section below). |
| Complementary vs. Non-Competing Supersets — reverse lunge + Copenhagen plank as intentional fatigue carryover; overhead press + squat as non-competing | VERIFIED | S4 @ 41:03-41:11 ("we're doing a paired superset of the same muscle group") + S4 @ 40:42-40:58 ("this is now complementary where there could be some fatigue carrying over but I kind of want that... yesterday for the superset we did chest presses and legs, completely opposite non-related muscle groups") + S2 @ 28:54-29:04 (deadlifts + pull-ups pairing example). |
| Cardio Deficit Hides Behind Strength — "you're strong, but your heart... just isn't there" | LIKELY | No single verbatim line locates this exact phrasing across S1-S5; it is directionally consistent with the density-work/conditioning discussion (S4 @ 26:56-27:14 and the Copenhagen-plank heart-rate beat at S4 @ 41:22-41:28: "you will find just your heart rate jacks up so much") but is a synthesized insight rather than a direct quote. |

## Claims — genius.md, Anti-Patterns (new section, this repair pass)

All eight items in the new "Anti-Patterns" section carry their own inline
quote + timestamp + conversation-file citation and are **VERIFIED** against
S1/S2/S4 as cited in place — not re-tabulated here to avoid duplication. See
`genius.md` → "Anti-Patterns (What Teo Explicitly Rejects)".

## Claims — genius.md, "How to Use This Skill (Model Calibration)" (new section, this repair pass)

This section is craft/voice guidance authored for this repair pass (modeled
on `skills/ben-watkins-storytelling/genius.md` lines 7-16 per the batch
envelope), not a factual claim about Teo — no VERIFIED/LIKELY/UNCONFIRMED
label applies to the calibration instructions themselves. The four illustrative
quotes embedded in it ("Slow it down a bit for me... making that stretch
out," "The limit does not exist... probably past 20 reps," "ankles today,
hips, lower back prepared for squatting," "as sets drop, intensity must
rise") are each VERIFIED against S4 @ 25:17 / S4 @ 28:06-28:17 / S4 @ 3:09-3:14
/ S2 @ 18:24 respectively — all already anchored in the rows above.

## Summary

- **VERIFIED**: 20 claims (transcript-anchored, verbatim or numerically exact).
- **LIKELY**: 11 claims (source-consistent synthesis, editorial estimate, or
  extrapolation with no single verbatim anchor).
- **UNCONFIRMED**: 3 claims — the "Franco Columbu" attribution on the
  bro-curl-in-squat move, the "deadlift day: shoulders, lower-back/core"
  warm-up target list, and "hollow-body holds" as a named warm-up drill. None
  were invented this pass; all three were already present in genius.md before
  this repair and are flagged here for the first time rather than silently
  carried forward.

No claim in this ledger was fabricated for this repair pass. Every VERIFIED
row was checked against the live transcript text pulled fresh from
`_archive/claude-export-2026-07-01.tar.gz` during this session (2026-07-17);
timestamps given are the transcript's own mm:ss markers, not file offsets.
