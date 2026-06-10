# Mandatory Workflow Routing — Full Bindings Table

> Extracted from CLAUDE.md 2026-06-09 (rebuild). **Enforcement is deterministic**: the
> UserPromptSubmit hook (`session_ledger_hook.py prompt`) runs `routing_enforcer.check_routing`
> on every explicit workflow invocation and injects violations as context; `finalize()` runs the
> post-hoc check. Machine source of truth: `execution/routing_enforcer.py BINDINGS`.
> **Update BINDINGS and this table together.**

If the task matches a domain below, deploy the bound workflow **even if the user names a different one**. System wins; explain the override in one sentence. Origin: 2026-04-21 session degraded to 6/10 because `writers-room` was used instead of `/parallax`.

| Domain signal | Mandatory workflow | Never substitute |
|---|---|---|
| Parallax Substack editions | `/parallax` | `writers-room` (diagnostic-on-draft only) |
| LinkedIn post from scratch | `/ghostwrite` or Lara Acosta skill | `writers-room` (refinement only) |
| Writers' room refinement of existing draft | `writers-room` | Production workflows |
| DESIGN.md authoring / extract / synthesize / brand-system | `/design-md-synthesize` or `-extract` or `/brand-library` | Generic Tailwind/CSS |
| UI / component code from DESIGN.md | `/product-build` or `/component-build` | Hand-rolling without DESIGN.md |
| DESIGN.md lint / WCAG / refinement | `/design-md-validate` | Eyeballing — always run `npx @google/design.md lint` |
| Competitive intel needing JS-rendered pages / screenshots | `/competitor-intel` or `/spy-market` + Playwright | WebFetch (returns hydration shells) |
| Login-gated source verification | Playwright per `directives/browser-automation-safety.md` | WebFetch (returns login wall) |
| Video source material (23 video-aware workflows) | `python3 execution/fetch-video-context.py` per `directives/video-vision-protocol.md` | Transcript-only ingestion (visual hooks = 30-50% of meaning) |
| Brand Operating System / "BOS" / 6-layer brand build | `/build-bos` (7-phase via `skills/brand-operating-system/`) | Single-component skills alone |
| Multi-deliverable marketing/creative mission | `/supercomputer` (anchor-memory + cost gate) | Single-skill execution alone. Triggers: `directives/supercomputer-mode.md` |
| Gate-suppressed orchestration ("autopilot", "no gates", "just execute") | `/autopilot` — 3 gates only: G1 (intent <=2), G2 (cost >$5), G3 (prose FLAGGED at Expert Standard >=7) | `/supercomputer`, `/jcc-deploy` etc. |
| Context engineering / "engineer the conditions" / "make the behavior automatic" | `/ce-design` (Context Engineering OS in `skills/chase-hughes-context-engineering/`) | Single-tactic copy/LinkedIn workflow alone. Ethics gate: `execution/context_ethics_gate.py` |
| Build an avatar / ICP / manifold from scratch · "plot the market" · cold-start buyer intelligence | `/avatar-machine` (full cold-start → finished copy) or `/avatar-manifold` (intelligence only). **Phase 0 GROUND auto-fires** (`execution/avatar_manifold_runner.py`, gated by `research_quality_gate.py --strict`). Skip only with `--no-ground` + `--voc-file` | `icp-build`/`icp-research`/`icp-deep-dive` (reasoning-only; modeled language fails rubric crit 6) |
| Cold-start → converting copy (VSL/ad/email/landing from blank page) | `/copy-engine` — **Ground Once, Refine Free.** Grounds ONCE via `avatar_manifold_runner.py` (WARM reuse = $0), writes `warm_core`, assembles the 6 copy blocks, gates proof via `verify_proof_ledger.py`. Later iterations reuse the cache at $0 | Writing copy from ungrounded context. Refinement of EXISTING copy uses standalone copy-blocks workflows at $0 |
| Multi-expert / collaborative / council work | `/convene` → `collective-genius-council.workflow.js` (presets: `/council` `/roundtable` `/strike` `/campaign` `/deploy-council`) | JCC plugin stubs, `execution/parallel_swarm.py` (deprecated) |
| Generic research · "deep research on X" · strategic intelligence | **Unified Research Engine** `execution/research.py`. Deep/max: native expert SWARM (`.agent/workflows/deep-research-swarm.workflow.js` via Workflow tool), $0 incremental. Quick/standard: `python3 execution/research.py "<q>" --depth <tier>`. Every result carries a **Research Receipt** | Answering research from training memory |
| New expert extraction ("extract this expert", `/extract`, `/extract-forge`) | `/extract` or `/extract-forge` directly — **never gated** (Farrice's standing decision 2026-06-09). `forge_gate.py status/record` = telemetry only | — |

## Non-Optional Phase Gates

**Avatar Machine Phase 0 GROUND is non-optional for cold-start builds.** Gemini Deep Research foundation + Apify VOC mining + FB Ad Library hooks + Recall grounding, floor-checked (≥15 source URLs, zero `[MODELED]`) by `research_quality_gate.py --strict`. Skip only with `--no-ground` + `--voc-file` (the "import, don't regenerate" path). Binding: `avatar_manifold_coldstart`.

**Parallax Phase 2.5 GROUND + ZEITGEIST is non-optional for Editions 02+.** Claim extraction, budget-tiered verification (Recall -> Perplexity), zeitgeist scan, halt/proceed gate. Skip only with explicit `--no-ground` (pure memoir, zero external factual surface). Origin: Edition 02 shipped 7 fabrications.

**Extractions are never gated** (standing decision 2026-06-09 — the freeze concept shipped and was reversed the same day at Farrice's direction). `forge_gate.py` survives only as usage telemetry: `status` shows the last extraction's production-use count in the monthly closeout; `record` registers a new extraction. Neither blocks anything.

## Manual Pre-Flight (when composing workflows yourself)

```bash
python3 execution/routing_enforcer.py check --request "<user request>" --workflow <chosen-workflow> --quiet
```

Non-zero exit = violation. `finalize()` also runs a post-hoc check.
