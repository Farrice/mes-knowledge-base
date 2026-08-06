---
thread: marketing-intelligence-engine
status: ready
resume_hint: Fill listening-creators.md (10-20 real creators via /creator-aperture) then first full scout run + Organic Engine v1 pen card
unfinished: Real creator list; Organic Engine v1; verify first unattended zeitgeist + angle-brief receipts; payment URL still blocks mission 2b
branch: main
pin: true
---

# Mark Forsyth Forge — Enchantment OS Shipped (16 workflows, /enchant live, merged to main)

## Purpose

- **Next session should do:** run `/enchant elevate` on Farrice's full LinkedIn profile copy — headline,
  About, and the Experience entries — starting with the misquote test on the headline. He asked for this at
  the end of the build session; the command did not exist yet in the main checkout, so it did not run.
- **Not in scope:** rebuilding the profile's *structure*, offer, or positioning. `/enchant elevate` treats
  line, sound and voice-texture only. If the audit finds the spine is what's wrong, it must stop and say so
  rather than rebuild — that is written into the workflow's scope discipline.

## Load First

- `_active/linkedin-launch/03-launch/2026-07-30-LINKEDIN-PROFILE-COPY-PASTE-MASTER.md` — the canonical
  working doc. Section 4 is the headline; the About section follows. Blocks marked **PASTE** are the live copy.
- `skills/mark-forsyth-rhetoric/genius.md` — the method. 24 figures, the enchantment thesis, the announcer rule.
- `skills/mark-forsyth-rhetoric/references/figure-catalog.md` — working cheat sheet, own-names not Greek.
- `skills/mark-forsyth-rhetoric/references/lane-contract.md` — **binding.** Which gates suspend inside
  `/enchant` and which never do; the never-both rules against `/how-i-write` Layer 5 and Farnsworth.
- `_active/farrice-brand/voice/VOICE-CARD.md` — load as a layer first. Forsyth supplies shapes; the voice
  card supplies the person.
- `extractions/mark-forsyth/SOURCE-MANIFEST.md` — read before quoting anything as verbatim Forsyth.

## Current State

- **Objective:** deployable, provable writing mastery in the harness — and the ability to write whole pieces
  in Forsyth's method, not just repair lines.
- **What is already done:**
  - Both Perell interviews fetched and **retained** (22,367 words) at `extractions/mark-forsyth/`. This
    closes the founding defect: the pre-forge source-ledger said "no raw source material exists for this
    expert." All 10 prior genius patterns were re-checked against real text and all 10 hold.
  - Skill 3 → **16 workflows**, 24 figures, the enchantment thesis, the grammar/glamour etymology.
  - `/enchant` front door live with two modes: `compose` (raw intent → finished piece, single author) and
    `elevate` (existing draft's line/sound/voice layer).
  - Four integrations wired without editing a single Farnsworth file: `/how-i-write` Layer 5 (with a new
    Lane Map section naming the split), `/writers-room` roster at card tier, `/high-taste-writing-os`
    adversarial pass (the enchantment check).
  - New: `lens-card.md`, `references/figure-catalog.md`, `references/lane-contract.md`, 3 born-v2 prompts.
  - **Merged to main and pushed** — `fd6ebf817`. Verified fireable from the main checkout.
  - Root-caused and fixed a real bug: `.agent/session.lock` was tracked in git, so every new worktree was
    born holding a phantom lock from whichever session last committed it. Now gitignored.
- **What is uncertain or stale:**
  - **The ornament ceiling is deliberately unresolved.** The two interviews contradict each other (2024:
    "I've never seen somebody overusing the figures of rhetoric"; 2026: "too many chilies and now you're
    ill"). Farrice's decision: `/enchant` stages **two takes** — full-ornament and gate-clean — and his gut
    verdict banks to `.agent/jam/taste-ledger.jsonl` under `domain: "enchantment"`. **No default until ~10
    verdicts accumulate. Do not set one silently.**
  - The blind pass is **B+, not A** — it passed only on retry, and the residual gap is named in the log.
  - The pure-vs-composed bake-off has not run.
- **Latest proof/receipt:** `skill_auditor.py check --skill mark-forsyth-rhetoric` → **7/7, gate clear**.
  `renaissance_audit.py` → 3,829 pass / 0 fail. Blind pass recorded as EVAL-063 in
  `evolution_store/ground_truth/eval_set_v1.jsonl`; ledger line in
  `extractions/mark-forsyth-rhetoric/blind-pass-log.md`.

## Suggested Skills / Workflows

- `/enchant elevate` — the route for this job. Runs audit → announcer map → figure diagnostic → forge →
  run-up rewrite, single author.
- `/mark-forsyth-enchantment-audit` — if you want the diagnosis alone before committing to a treatment pass.
- `/mark-forsyth-figure-diagnostic` is reachable through `/enchant`; there is no standalone shim for it or
  for `write-to-enchant` (the minter judged both reachable via the front door).
- **Do not** also run `/how-i-write` Layer 5 or `/ward-rhetorical-engine` on the same passage — double-picked
  lane, explicitly forbidden by the lane contract.

## Exact Next Prompt

```text
/enchant elevate on my LinkedIn profile copy — headline, About, and the Experience entries — in
_active/linkedin-launch/03-launch/2026-07-30-LINKEDIN-PROFILE-COPY-PASTE-MASTER.md

Start with the misquote test on the headline. Load VOICE-CARD.md as a layer first. Two takes on
anything taste-bearing, and tell me which one you believe in before I pick.
```

## Acceptance Criteria

- The headline gets an explicit misquote-test verdict with reasoning — PASS or FAIL, not an adjective.
- Ornament lands at 2–4 stakes moments across the whole profile; the connective copy stays plain, and what
  stays plain is defended in one line.
- Two takes staged for the headline and the About opener, with a stated preference, and the verdict banked
  to `.agent/jam/taste-ledger.jsonl`.
- Fair-housing-style compliance language and any hard claim (18 yrs, 1,000+ clients) is classed INSTRUCTION
  by Step 0 and left untouched.
- No Greek terminology anywhere in delivered copy.

## Risk Notes

- **Spiral risk is the real one here.** There are already eight profile-copy versions on disk (v3 through
  v8, plus this master), and the v3 run is a logged scar. The standing rule applies: **two rejected takes on
  one artifact = stop producing and go back to the input.** If the first `/enchant` pass gets a flat verdict,
  do not produce a v10 — return to the ICP language and the offer.
- **Scope creep into rebuild.** `/enchant elevate` must not restructure the profile. The offer and
  positioning are settled elsewhere (`project_proof-to-market-path-a`). Treat lines, not strategy.
- **Claim integrity.** "18 yrs human performance · 1,000+ clients" are factual claims on a public profile.
  The factual veto never suspends inside `/enchant`; no figure may be applied to a number.
- **Starting observation, already made:** the current headline is
  `Claims your buyers believe | Creative strategy & positioning for supplement, recovery & performance
  brands | 18 yrs human performance · 1,000+ clients · Free teardown` — a pipe-delimited keyword stack.
  Competent, conventional, and it fails the misquote test on sight: nobody would ever correct a flat
  paraphrase *into* it. That is the diagnosis to confirm and treat, not to re-derive from scratch.
- **Codex parity not run** for the new commands — `AGENTS.md` has not been updated for `/enchant`. Separate pass.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
