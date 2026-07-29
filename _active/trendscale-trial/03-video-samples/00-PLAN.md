# TrendScale Video Samples — Master Plan

**Trigger:** Recruiter (Mihaila) reply, 2026-07-09: client wants finished video content, not screenshots/stills.
**Strategic frame:** She already has the two written briefs. The videos are the *executed versions of those exact briefs* — JCKED "Locked Vault" and Puravita "The Battery You Can't See." Nobody else in the pipeline can show the loop closed: strategy doc → finished ad, same concept, same hooks. That is the hire-me argument.

---

## What gets sent (target: 2–4 finished videos)

| # | Asset | Length | Priority | Why |
|---|---|---|---|---|
| 1 | JCKED final cut, Hook 3 (mechanism-curiosity) | ~75–85s VSL cut, 9:16 | MUST | The signature concept ad; mechanism-led, matches the brief she's holding |
| 2 | Puravita final cut, Hook 1 (battery analogy) | ~100–110s VSL cut, 9:16 | MUST | Second brand = range; quiet register proves tonal control |
| 3 | JCKED hook teaser, Hook 4 (loud control) | 12–15s | STRONG | Shows iteration thinking: same body, different hook, test-plan mindset |
| 4 | Puravita hook teaser, Hook 3 (partner-POV) | 12–15s | OPTIONAL | The "my wife says she misses me" line is the most memorable 8 words in either brief |

**Runtime honesty (both builders flagged it, resolved here):** the verbatim VO runs longer than the briefs' ~35s/~50s targets at a natural pace. Do not cut words to hit the old number. Ship the full cuts as what they are — VSL-length cold-traffic ads (60–110s is standard Meta VSL territory and matches the mechanism-led format) — and let the 12–15s teasers be the tight feed cuts. The pairing itself demonstrates test-plan thinking: one angle, two lengths. If a hard cutdown is ever demanded, Puravita Body 3 is the first trim candidate (flagged in its kit); JCKED trims breath gaps only.

Statics (in `statics/`) are a bonus attachment only if the thread invites it — the ask is video; don't dilute.

## Generation routes (cost-ranked — default to $0)

1. **Google Flow / Veo 3.1 (Gemini Ultra plan — $0 incremental).** Primary route. Veo clips cap ~8s, so full cuts are built scene-by-scene per the kit cards, assembled in CapCut. Veo does native audio + spoken dialogue: the narrator clips can come out talking.
2. **Higgsfield Marketing Studio (credits — budget-gated).** Best single-generation quality for the 12–15s hook teasers (one prompt = one finished micro-ad). Run `python3 execution/higgsfield_budget_guard.py check` first; generation only after explicit approval. If credits are tight: generate teasers #3/#4 here only, full cuts via Flow.
3. **HeyGen (existing plan per brief)** for the narrator UGC segments if avatar consistency across clips beats Veo's per-clip narrator.

## Build order (fastest finished sample first)

1. Render the two hook teasers (one generation each) — a finished, sendable micro-ad within the hour.
2. Render start frames (GPT Image 2 cards) for the shared body scenes — these anchor product fidelity and become Veo/Higgsfield image-to-video inputs.
3. Render body clips scene-by-scene per kit cards; narrator clips last (HeyGen or Veo-native).
4. Assemble per runbook: captions (Inter Tight, bottom third, ≤6 words/frame; amber = JCKED enzyme+dose only; sage = Puravita callouts), music −18 dB, silence on final CTA, export 1080×1920.
5. Run each cut through the kit QA checklist + `python3 execution/prose_classifier.py check` on caption text.

## Product fidelity (non-negotiable)

Pull real bottle photography before generating anything product-visible:
- JCKED: https://jcked.com/products/liquid-l-carnitine-4000mg
- Puravita: https://shoppuravita.com/products/puravita%C2%AE-magnesium-complex
Attach as `<<<image_1>>>` in every Marketing Studio prompt and as reference image in Flow. Never let a model invent a label.

## Reply to Mihaila (send WITH links, not before)

> Hi Mihaila. Done. Instead of sending generic samples, I produced the two briefs you already have as finished ads: the JCKED "Locked Vault" spot and the Puravita "Battery You Can't See" spot, plus a short alternate-hook cut of each so the client can see how I test angles, not just make one video.
>
> [Drive folder link: 4 files, 9:16, feed-ready]
>
> Everything matches the briefs. Same hooks, same visual system, same test plan. Happy to walk the client through how each was made and what week one of testing looks like.
>
> Farrice

(One Drive folder, filenames like `JCKED_LockedVault_Hook3_35s.mp4`. WhatsApp: 778-322-4478.)

## Kit locations

- `jcked/JCKED-VIDEO-KIT.md` — shot list, per-clip start-frame + Higgsfield + Veo prompts, narrator card, teasers, runbook
- `puravita/PURAVITA-VIDEO-KIT.md` — same structure, ~50s build
- `statics/STATIC-ADS-KIT.md` — 4 statics per brand, GPT Image 2 prompts with overlay copy

## Open decisions carried from `rework-v2/PRIVATE-STRATEGIST-NOTES.md` §8

Hook 3 Puravita uses the Huberman/Attia beat in the shared body — the name-free fallback exists if Farrice decides against named persons before rendering VO. Decide before generating the "why the test missed it" clip; everything else is unaffected.
