# Latest Handoff

**Thread:** sam-vander-wielen-forge  
**Full path:** .agent/handoffs/2026-08-06-sam-vander-wielen-forge.md  
**Date:** 2026-08-06 (today)  
**Status:** ready  
**Title:** Sam Vander Wielen Launch OS — Watch + Forge + Skill System (12 workflows)

> Not auto-loaded. Run `/resume` to choose any thread, or `/resume sam-vander-wielen-forge` for this one.

---

---
thread: sam-vander-wielen-forge
status: ready
resume_hint: Merge claude/vanderland-webinar-launch-forge into main — regenerate registries, do not hand-merge them
unfinished: Blind pass not run: need 2 verbatim Sam's Sidebar issues in reference-corpus/, then judge + record
branch: claude/vanderland-webinar-launch-forge
pin: true
---

# Sam Vander Wielen Launch OS — Watch + Forge + Skill System (12 workflows)

## Purpose

- **Next session should do:** merge `claude/vanderland-webinar-launch-forge` into main (a **registry reconcile is required** — see Risk Notes), then close the blind pass by saving 2 verbatim *Sam's Sidebar* issues into the reference corpus and running the judge.
- **Not in scope:** extending the skill, running a real launch, or re-watching the source video. The extraction is complete and carded — extend, never rebuild.

## Load First

- `skills/sam-vander-wielen/SKILL.md` — the manifest; 12 workflows in 3 tiers, "When NOT to Use" table
- `skills/sam-vander-wielen/genius.md` — Recognition Test, 5-level named rubric, 10 sourced anti-patterns. **Load before any workflow.**
- `skills/sam-vander-wielen/references/source-ledger.md` — 35-claim provenance; contains the **name-correction table** and the 2 UNCONFIRMED legal claims that must never be asserted
- `extractions/sam-vander-wielen/reference-corpus/README.md` — the exact blind-pass gap + close procedure + the 2 target URLs
- `skills/sam-vander-wielen/references/skill-system-contract.md` — `/source-to-skill-system` contract + behavior-changing before/after proof
- `docs/solutions/2026-08-06-auto-caption-proper-nouns-poison-extraction-slug.md` — the scar carded this session

## Current State

- **Objective:** turn a 61-minute Nathan Barry Show interview into a deployable live-webinar launch capability the arsenal did not have.
- **What is already done:**
  - `/watch` — full timestamped transcript (334 turns, 14,627 words) + 34 frames. Finding: **visual channel carries no extractable craft** (two camera setups, zero slides/graphics/b-roll). Checked, not assumed; recorded in `visual-context.md`.
  - `/extract-forge` — Deep tier. 12 workflows (4 foundation / 4 practitioner / 4 stacking), 20 genius patterns, 6 hidden-knowledge insights, 3 exemplars + 2 anti-exemplars, 12 born-v2 prompts, `AGENT.md`, front door `/sam-vander-wielen`, 35-claim ledger.
  - `/source-to-skill-system` — build shape = **skill system** (not a companion OS layer; this is domain expertise, not harness behavior). Contract verification PASS with the required behavior-changing before/after proof.
  - **Name correction executed**: auto-captions mangled her surname as "Vanderland" across all 2,093 segments. Verified off-source as **Sam Vander Wielen** on five identifiers (domain, On Your Terms®, Ultimate Bundle, Sam's Sidebar Tuesday cadence, book ISBN 9781538767382). Full rename; `transcript.md` deliberately left unedited as the raw caption record.
  - 3 commits on `claude/vanderland-webinar-launch-forge`, worktree clean.
- **What is uncertain or stale:**
  - **Blind pass NOT run** — ships B-tier. Corpus unmet because the available fetch tool returns summaries, not verbatim body copy. Judging voice against a summary would be a false pass.
  - Single-source extraction, no cross-enrichment. A second source (her podcast, her book, Nathan Barry ep. 74) would raise confidence on briefly-described mechanics.
  - All figures are **self-reported by Sam** and are hers, never a user's projection. Enforced in every workflow Quality Gate.
  - `/sv-ai-objection-kill` is reachable via the front door but has no direct command; the minter reports nothing to do and hand-writing wrappers is banned (arsenal-loop Invariant 2).
- **Latest proof/receipt:** `skill_auditor.py check --skill sam-vander-wielen` → **7/7 PASS, gate clear** · `renaissance_audit.py` → 0 fail (3838 files) · `verify_skill_system_contract.py` → PASS · menu parity 12/12 · `forge_gate.py record` logged 2026-08-06T14:04.

## Suggested Skills / Workflows

- `/resolving-merge-conflicts` — the merge needs a registry reconcile, not a blind merge
- `/sv-subject-line-hero` — cheapest first real proof of the system (one Parallax email, measurable open delta, $0)
- `/sv-launch-teardown` — apply to the LinkedIn Cash Launch campaign
- `/extract` Extension Mode — the only correct route for future Sam Vander Wielen material (never a second extraction; the slug already exists)

## Exact Next Prompt

```text
Merge the sam-vander-wielen forge branch into main, then close its blind pass.

1. The branch claude/vanderland-webinar-launch-forge (worktree at
   /private/tmp/antigravity-vanderland-forge, 3 commits, clean) is based on
   b49f407dc. Main has since advanced to c8f605811 (the edit-bay taste-layer
   commit). Both touched generated registries — SKILL_INDEX.md,
   AGENT_INDEX.md, SLASH_COMMANDS.md, .agent/prompt-index.json,
   .agent/arsenal-index.json, agents/_framework/invocation-cards.md.
   Do NOT hand-merge those. Take main's side on every generated file, then
   REGENERATE:
     python3 execution/sync_registries.py
     python3 execution/mint_menu_wrappers.py --scope skill sam-vander-wielen --apply
     python3 execution/prompt_library.py build
     python3 execution/wire_prompt_pointers.py --write
     python3 execution/generate_slash_commands.py
   Then confirm: python3 execution/skill_auditor.py check --skill sam-vander-wielen
   must report 7/7 PASS before you commit the merge.

2. Close the blind pass. Save the FULL VERBATIM body copy of these two real
   Sam's Sidebar issues into
   extractions/sam-vander-wielen/reference-corpus/ as .md, each with a
   provenance line (URL + date) at the top:
     https://mailing.samvanderwielen.com/posts/the-lesson-i-needed-to-learn
     https://mailing.samvanderwielen.com/posts/my-wake-up-call-about-online-safety
   WebFetch returns summaries — get the real text (Playwright, or paste it in).
   A summary is NOT acceptable; it would produce a false pass.
   Then:
     python3 execution/blind_pass.py prepare --expert sam-vander-wielen
     # generate 1-2 Tier-1 workflow outputs, judge side by side vs the real issues
     python3 execution/blind_pass.py record --expert sam-vander-wielen \
       --verdict PASS|FAIL --notes "..." --generated [path] --reference [path]

Do not extend or rebuild the skill. It is complete and carded.
```

## Acceptance Criteria

- `git log` on main contains the forge commits, and `skill_auditor.py check --skill sam-vander-wielen` reports **7/7 PASS** post-merge
- `/sam-vander-wielen` and the 11 `/sv-*` commands fire from a fresh session
- `reference-corpus/` holds ≥2 provenance-lined **verbatim** issues and `blind_pass.py prepare` reports corpus ready
- A recorded blind-pass verdict exists in `eval_set_v1.jsonl`; tier moves off B **only** if it passed
- No generated registry file was hand-merged — all regenerated

## Risk Notes

- **Merge is not clean-by-default.** Branch base `b49f407dc` vs. main `c8f605811`; both sessions regenerated the same registries. Blind-merging generated files will corrupt indexes. Regenerate, don't reconcile by hand.
- **Never `merge -s ours`** to silence a divergence alarm — that is how the 07-14 brief was lost. Recover files first.
- **Two UNCONFIRMED legal claims** in the source (AI chat-log discoverability; lawyers sanctioned for fabricated citations — no case named). Flagged in `source-ledger.md` claims 34–35. Never assert them; the skill's core AI-objection mechanic requires no legal claim, which is why it's the durable asset.
- **Sam's figures are self-reported and hers.** Any client-facing use must carry the label. Enforced in every workflow Quality Gate; don't let a downstream asset strip it.
- **Fair-housing / compliance**: the disqualification and buyer-temperament mechanics carry real regulatory risk in housing, lending, and employment. `/sv-customer-personality-lock` and `/sv-webinar-script` both flag it — do not transfer that language into Jen's listing copy without review.
- **Tier is B, honestly.** Do not promote to A on the strength of the 7/7 heartbeat alone; A-tier requires a real blind pass plus a Farrice-judged verdict.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.

