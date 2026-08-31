---
date: 2026-07-25
session: dara-creative-strategy-harvest
problem_class: extraction / productization / client-deliverable-systems
problem_signature: "an expert's client-deliverable SOP exists only as documents shown on screen in their videos — transcript-only extraction returns patterns instead of the replicable system (templates, client package, business model), and the obvious route demands their paid course and tool stack"
tags: [extract-forge, watch, frame-grounding, notion-template, persona-intelligence, dara-denney, sop-harvest, spec-work]
---

# Harvesting an expert's client-deliverable SOP into a sellable in-house package (one session)

## The problem

An expert shows their actual agency SOP documents *on screen* in YouTube videos (Dara Denney's creative-strategy research SOP + strategist business model). The goal wasn't "extract patterns" — it was **replicate the deliverable system itself**: the SOPs, the document templates, the client package, a Notion template, and the business model to sell it — without paying for her course or her tool stack (Motion/Foreplay/Particle), and without inventing what wasn't shown.

## The crack

**Transcript alone would have failed** — the deliverable structures (her Notion SOP page, the persona deck cover line, the testing-roadmap columns) exist only visually. The recipe:

1. **Dual capture**: `fetch-transcript.py` per video (rename outputs immediately — it always writes `transcript.txt` and WILL clobber prior extractions; restore casualties via `git checkout`), then `/watch` at `--detail efficient --max-frames 36 --resolution 1024` on the doc-showing video only. 1024px is what makes on-screen document text readable; keyframe mode lands on slide/screen cuts. Skip frames for talking-head videos — transcript suffices, tokens saved.
2. **Read frames for STRUCTURE, not vibes**: the frames yielded her SOP's exact resource list, step names ("Persona and Desire Segmentation", "Create the Mission Doc"), card contents verbatim, deck cover line ("Named personas from 1,079 customer reviews + 424 survey responses"), and sheet columns (Test/Concept/Variations/Winning Element/Type). Write a `visual-context-*.md` immediately — frames are session-ephemeral, the notes are the asset.
3. **Extend, never rebuild**: new layer went into the existing expert skill as **Tier 0** (workflows 18-26 above the production tiers), matching her own thesis ("strategy is the layer before format selection"). Deliverables became `references/templates/*.md` (fill-in scaffolds), the moat got its own spec (`persona-intelligence-moat.md` with productization shapes).
4. **Deterministic tool where judgment ISN'T**: her explicit automation boundary ("machines compile, humans pick golden nuggets") mapped to `execution/review_miner.py` — stdlib CSV pre-pass (product ranking + nugget candidates via emotion/specificity heuristics), $0, leaving selection to judgment.
5. **Notion template via the pinned API**: Knowledge Vault hub page + one child page per deliverable, template bodies as chunked markdown code blocks (fidelity-preserving, duplication-friendly). Child pages need raw `_request("POST", "/pages", {"parent": {"page_id": …}})` — `notion_api.py`'s `create_page()` only takes database parents.
6. **Tool-stack mapping table** kills the paid-tool reflex: her Motion/Foreplay/Particle functions map to ad_spy/social_intel/client-exports at ~$0. Total run cost: $0.005 (one Apify metrics pull).

## Wiring gotchas (cost of skipping: B-tier cap)

- `skill_auditor.py check` fails `workflow_contracts` on any workflow whose output section isn't literally headed "Output Schema".
- Menu parity: wrappers are MINTED (`python3 execution/mint_menu_wrappers.py --scope skill <skill> --apply`), never hand-written; the PostToolUse hook alone didn't mint mid-session.
- Prompt wiring is 4 steps, all mandatory: renaissance_audit → prompt_library build → wire_prompt_pointers --write → per-workflow pointer lines.

## Re-solve guard

Next "harvest this expert's client system" request: this exact pipeline, in this order — transcripts+rename → frames-on-doc-video-only @1024 → visual-context notes → Tier-0 extension + templates + moat reference → deterministic tool at the judgment boundary → Notion hub deploy → mint + audit. Do not re-derive; do not build a new skill beside an existing expert.
