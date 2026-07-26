# Depth Fix: Proof Run

**Date:** 2026-07-26 · **Purpose:** verify the research-stack fix works. Stopped deliberately after the sweep and gap-fill wave 1, before the 20-agent verify phase, to keep usage proportional to a proof.

---

## What ran

20 agents: 12 sweep (10 questions + 2 Playwright primary-source), 1 Gemini background start, 1 completeness critic, ~5 gap-fill follow-ups, 1 in flight at stop. Output: **234 KB across 12 findings files** in `.tmp/research/offer-validation-deep/`.

---

## The measured comparison

| | Round 1 (2026-07-25) | Round 2 (fixed stack) |
|---|---|---|
| Distinct sources | 87 | **296** |
| Distinct domains | 79 | **155** |
| Sources per question | ~14.5 | **~25** |
| Evidence depth | search snippets | **full-page reads** |
| Rounds | 1 (single pass) | **2 (sweep + gap-fill)** |
| Primary sources behind JS | unreachable | **Playwright lane, 2 agents** |
| URLs surviving into the decision artifact | **0** | pending synthesis |

---

## A correction I owe, because it changes what you should trust

I told you Round 1 was "roughly six search snippets per question." **That was wrong, and I should have measured before saying it.** Round 1 actually pulled 87 distinct sources across 79 domains, which is real breadth.

The failure was never breadth. It was four other things, and the fourth is the one that nearly cost you a decision:

1. **Snippet-depth, not page-depth.** 400-character excerpts standing in for read pages.
2. **Single pass.** No gap-check ran, so whatever the first search surfaced became the finding.
3. **Evidence never attacked.** The three killers stress-tested the offer *paths*, and nobody attacked the sweeps underneath them. VERIFIED labels were self-assigned by the agents that found the claims.
4. **Zero URLs survived into RESULTS.md.** 87 sources were gathered and *none of them made it into the document you were going to decide from.* The evidence existed in agent memory and died there. That is why the new gate fails that file at `0 sources / 0 domains`: it isn't measuring the research, it's measuring what reached you.

That fourth failure matters most, and it's the one the depth gate now catches automatically.

---

## Proof the Playwright lane reaches what nothing else could

**PW1, Meta Ad Library, live and read-only.** 13 brands confirmed with 15+ simultaneously active US ads, found in roughly ten minutes: Omni Creatine ~750 active ads, Legion ~330, Crave Creatine ~290 (ads live continuously since Jul 2025), plus GNC, AG1, Orgain, BulkSupplements, Naked Nutrition and others. It also found ads running **since Dec 2023**, which is 2.5 years live.

The empirical verdict on your buyer filter: *"YES — emphatically. The 15-ad bar is low for this market; a 50–100+ bar would still leave a full prospect list."* And it does real sorting: Vital Proteins (~21) and Greens First (~11) sit at or below the line.

**PW2, live pricing pages, captured verbatim.** CREVARI's $1,000 Creative Autopsy confirmed still live today, with exact terms captured word for word, including the pilot's guarantee mechanics ("beat your account-average CPA in 90 days or we keep building free").

Neither of those was reachable by the old stack. Both are now first-class evidence.

---

## The gate is not rubber-stamping

Run against the new Tier-1 findings files at deep contract:

- **Depth contract: PASSED** on all four (sources and domains clear 15/6 comfortably).
- **Still FAILS overall** on Q1, Q2, Q4, on provenance (42% of data claims attributed) plus naked-claim and recency flags.

That's the gate working correctly. These are working-notes files, not the final report, and the gate is telling the truth about them: over half the data claims in Q1 don't carry an inline URL. Under the old system that file would have flowed into a synthesis and out the other side wearing a 9.

---

## What did NOT run, and what that means

The independent verification phase never executed. Under the standard we just built, **a claim labeled VERIFIED by the agent that found it counts as UNCONFIRMED.** So every claim in this corpus is currently finder-labeled and unverified.

Which means this corpus is **⚠️ RECON-GRADE — not decision-grade.** Good raw material, high breadth, real primary sources, and zero independent attack. Do not make the offer call on it.

To promote it: re-run the verify phase (up to 20 refuters) and the synthesis, then gate the report and finalize with `--depth-receipt`. That's a bounded run whenever you want it, rather than something to spend on today, when the point was proving the machine works.

The findings are preserved at `.tmp/research/offer-validation-deep/` and cost nothing to sit there.
