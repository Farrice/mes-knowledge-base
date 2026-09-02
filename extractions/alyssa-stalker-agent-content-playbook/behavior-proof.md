# Behavior Proof: alyssa-stalker-agent-content-playbook

Contract: `semantic_libraries/antigravity/primitives/behavior-changing-extraction-contract.md` (content source, so the proof is a before/after transformation). Produced copy alone lives in `blind-pass/proof-copy-only.md` for the prose classifier.

## Proof 1. Broad local hook to Topic + Who + Lens (`03-hook-reframe`)

**Input tested.** A realistic Jen Santulan local hook in the register her account already uses: "3 things to do in the Valley this weekend 🌞"

**Weakness diagnosed.** Topic only. No who, no lens. It is the exact shape Alyssa names as "very broad" [12:12–12:17]. Under 2026 interest-test distribution it lands in front of no one in particular [12:35–13:05].

**Source mechanics used.** Append the who-clause and the lens [12:12–12:32]. Housing-safe framing (system layer) because Jen's audience is housing-adjacent. Jen FTHB register: calm-warm lowercase, curiosity opener, no urgency (`_active/clients/jen-listings/CLAUDE.md`).

**Output produced (recommended row of the Hook Reframe Set).**

> the valley this weekend if you just signed another lease and told yourself "one more year." three spots that make it feel less like waiting.

Mechanism: private state (the lease, the "one more year"). Lens: "feel less like waiting" is comfort, not urgency. Format fit: carousel slide 1 or B-roll text hook. Alternates in the set: insider ("...that don't show up when you search 'things to do sherman oaks'"), habit ("...for the sunday-farmers-market people who haven't tried the one in encino"), comfort variant ("self-care as someone who's toured 14 open houses and bought zero").

**Behavior delta.** Before, jen-engine Stage 3 produced three hook variants tagged pattern-interrupt, stakes, and specificity, all still addressed to "SFV renters" as a segment. After, every hook names one person's private state plus the agent's framing, and the fair-housing filter is explicit. The topic did not change. The addressee did.

**Validation run.** `python3 execution/prose_classifier.py check extractions/alyssa-stalker-agent-content-playbook/blind-pass/proof-copy-only.md` (result in the build report). Voice test: coffee-table read passes; no brochure adjectives, no urgency.

**Remaining risk.** Unposted, so no first-party performance data. Next gate: post the recommended hook as a carousel and as a B-roll reel (A/B per [10:37–10:41]), 14-day window, compare reach and follows against Jen's flatline from `01-outlier-audit`.

## Proof 2. FTHB education post to comfort carousel (`04-comfort-content-engine`)

**Input tested.** The default FTHB education shape Jen's calendar drifts toward: "5 things first-time buyers in LA need to know before they start 🏡" with five bullet facts (DTI, PMI, pre-approval, closing costs, inspection).

**Weakness diagnosed.** This is the "chat GPT script first-time buyer education... five different statistics that no one really cares about" shape [24:43–24:57]. It lectures an audience whose real state is shame and fatigue ("we make good money but still can't afford. It's humiliating," Jen genius §3), and it opens with information instead of recognition.

**Source mechanics used.** Comfort creator structure [16:35–21:40]. Consumer flip with the offer last, as permission [20:10–20:51]. Share test [23:36–23:46]. Lo-fi spec [37:14–37:18]. Jen Pillar C: "you CAN," never "you SHOULD."

**Output produced (carousel 1 of 3, state = ashamed).**

| Slide | Text | Beat |
|---|---|---|
| 1 | self-care as someone who's 34, makes good money, and still hasn't bought in LA | private state |
| 2 | you know the one. zillow open at 11:40pm. saved search named "someday." tab closed before you do the math. | recognition |
| 3 | step one: stop doing the 20%-down math. nobody in the valley buys through that door. | cheeky |
| 4 | step two: text the friend who bought last year and ask what they actually put down. you'll feel better in 30 seconds. | supportive |
| 5 | step three: let the spreadsheet be wrong for a week. rest is allowed before the plan. | supportive |
| 6 | you're not behind. half my clients started exactly here. that's exactly who i help. | permission as offer |
| 7 | if you want the real number instead of the scary one, reply "someday" and i'll send it. | CTA |

Caption: "no lecture today. just the part nobody says out loud, and the part that comes after it 🤍". Visual: camera-roll photo of a Valley street at dusk, plain type, one line per slide. Share test: partner-send passes ("this is us"). Anti-FOMO: no deadline, no rent-shaming, no "act now."

**Behavior delta.** Before, the system shipped information first and treated the buyer's fear as a caption afterthought. After, the buyer's private state is slide 1, education is compressed to three doable moves in the middle, and Jen's offer appears only on slide 6 as permission. The Stacked-Door fact from her existing lead copy (20% is the front door nobody uses) is preserved but moved to the cheeky beat, where it lands as relief instead of a stat.

**Validation run.** Prose classifier on the slide text (see report). Jen CLAUDE.md anti-pattern scan: no "top 1%," no urgency, no steering language. The line "half my clients" is a claim Jen must confirm or soften before posting; flagged.

**Remaining risk.** The "half my clients" line is unverified against Jen's actual book. The carousel is unposted. Next gate: Jen's thumbs-up on slide 1 wording, then one post, 14-day window, with saves and DM replies as the convert metric.

## Negative control: what the skill refuses

Input: "Rates are only going up. If you don't buy before school starts you'll regret it 😬 DM me NOW."

Result: `03-hook-reframe` and `04-comfort-content-engine` both stop at the anti-FOMO gate [20:52–21:01] and return the comfort variant instead. The skill does not improve urgency copy. It replaces the mechanism.

## Verdict

The extracted intelligence changes a realistic Jen input in a way the prior system did not. The addressee moves from segment to person. The offer moves from first to last. The fair-housing frame is explicit. Proof is unposted, so performance claims stay UNTESTED until the 14-day gates run.
