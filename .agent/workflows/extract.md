---
description: Extract expert knowledge — adaptive forge-grade pipeline
---

# /extract — Mastery Extraction Workflow (v3.0 — One Spine, One Dial)

Extract expert knowledge from any source and produce a deployable completion-engine skill at **forge shape by default**: tiered workflows, ≥7 born-v2 prompts when the corpus supports it, mandatory references, agent, and an asset scan. The output size is DERIVED (`execution/extraction_manifest.py`), never asserted. Thin sources are auto-enriched from the same expert before anyone settles for a small manifest; if enrichment is exhausted the run ships the honest count with `fidelity: low` — floors are earned, never padded.

**vs `/extract-forge`**: same quality gates, same build standards (they share the directives). The forge is the explicit full-ceremony session — full Vision document, 3 human checkpoints, 2-4h, for when Farrice wants control at every stage. `/extract` v3.0 reaches the same output shape adaptively in one pass. Elevation decisions: Farrice 2026-07-23 (floor fusion, auto-enrich, forge-scale extensions, asset scan).

## Usage

```
/extract [source — URL, transcript paste, or file] 
```

Options: `light extract` (explicit small-run override — skips enrichment, ships MES Light honestly) · `deep extract` (force Deep tier) · `skip validation`.

## Phases

### P0 — Lock the Tree
A full or extension build writes >3 files. Claim before building (merge-discipline Law 0):
```bash
python3 execution/session_lock.py claim "extract: <expert> <mode>"
```
Fresh foreign lock → coordinate or move to a worktree; never build unlocked next to a live sibling.

### P1 — Source Acquisition + Expert ID
Unchanged from v2.1:
- YouTube → `python3 execution/fetch-transcript.py "<url>" "<expert-name>"` → `extractions/<slug>/`
- Video → visual context in parallel: `python3 execution/fetch-video-context.py "<url>" "<expert-name>" || true` (see `directives/video-vision-protocol.md`); if `visual-context.md` lands, load it for all downstream passes. If the `/watch` plugin already ran this session, save its transcript into `extractions/<slug>/` and reuse the frames already in context.
- **Expert ID (CRITICAL)**: "by [Name]" in headers is often the transcription tool. Check title/channel/content; if ambiguous, ask. Check `AGENT_INDEX.md`: existing expert → **Extension Mode** (P4 note). Record `Expert: [Name] | Transcribed by: [Tool]`.

### P1.5 — Corpus Gate + Auto-Enrichment (NEW)
```bash
python3 execution/extraction_manifest.py corpus --dir extractions/<slug>
```
- **RICH (≥8,000 words)** → proceed.
- **MID/THIN** → auto-enrich from the SAME expert before accepting a small manifest:
  1. Discover 2-4 more sources: `yt-dlp --flat-playlist` on the channel, WebSearch for articles/podcasts/interviews. **Free tooling only** — never budget-gated APIs (cost gate).
  2. Dedup against files already in `extractions/<slug>/`.
  3. Fetch transcripts (`fetch-transcript.py`; captions via yt-dlp). Hard caps: ≤4 added sources, stop as soon as RICH.
  4. Re-run `corpus`. Record an **enrichment ledger** (added / failed / skipped-dup) for the P10 report.
- Still THIN after enrichment → continue with `fidelity: low`; the manifest will size honestly.
- **Extension Mode**: target enrichment at the NEW layer's topic (same expert, that theme).
- Set aside 2 enrichment sources NOT quoted in the skill as blind-pass reference-corpus candidates (`extractions/<skill-dir>/reference-corpus/`) — this pre-solves the P9 corpus gate.

### P2 — Leverage Brief (compressed Vision)
One page inline, no checkpoint (the forge's full Vision doc + checkpoint is the ceremony difference): **Uniqueness** (what only this expert does) · **Business leverage** (which active projects/clients this feeds) · **Stacking partners** (2-4 named roster experts) · **Gap fill** (what the roster lacks that this adds). The brief steers P3 emphasis and seeds Tier-3 workflows.

### P3 — Deep Extraction
Run `directives/mes-3.0-extract.md`. Tier is derived from the **post-enrichment** corpus: RICH → **Deep forced** (10+ genius patterns, ≥3 Hall-of-Fame exemplars, ≥5 signature moves, 7+ rubric criteria); MID → Standard; THIN → Standard with fidelity flag. Validate per `directives/mes-3.0-validate.md` (skippable by explicit "skip validation").

### P4 — Derived Manifest — CHECKPOINT 1
```bash
python3 execution/extraction_manifest.py derive --patterns N --hidden N --exemplars N \
    --deliverables N --corpus-words N --stacking-hits N [--extension] --out .tmp/manifest-<slug>.json
```
Present the manifest table: workflows by tier (named, one line each), prompt count, references, orchestrator/agent verdicts, fidelity flag, enrichment ledger.
- **Interactive session**: wait for approval (adjust/scale requests welcome).
- **Autonomous session**: auto-approve AT the derived manifest — never below its floors — and log the auto-approval in the report.
- **Extension Mode**: manifest derives from NEW-layer yields (`--extension`: 2-5 workflows, ≥5 prompts for a 5+-pattern layer). One-workflow extensions are reserved for genuinely single-pattern layers — "extend, don't rebuild" governs *where* assets live (inside the existing skill), never *how few* to build.

### P5 — Build (forge structure mandatory)
Per `directives/skill-craft-standard.md` + `directives/embodiment-standard.md`:
- `skills/<skill-name>/genius.md` — patterns + hidden knowledge + exemplars + signature moves + rubric, model-calibration header ("execute the trigger, never announce it" register).
- `SKILL.md` — completion-engine frontmatter, **tiered workflow table** (Foundation / Practitioner / Stacking), **stacking guide** naming roster partners from P2.
- `references/` — **mandatory**: `source-quotes.md` (verbatim quote bank + claims ledger with VERIFIED/LIKELY/UNCONFIRMED labels), `cross-domain-patterns.md`, provenance ledger (grep-verify every anti-pattern/exemplar anchor against `extractions/<slug>/` before use), `genius-patterns.md`, `hidden-knowledge.md`.
- `workflows/*.md` per manifest — each with Pre-Flight (gate + genius.md load), Input Required, Steps, **Content Type Adaptations**, Output Schema, Example Output (≥2 workflows with worked examples + "What makes this excellent"), Quality Gate.

### P5.5 — Forge Execution Prompts (MANDATORY — `directives/prompt-forging-spec.md`)
One born-v2 structure-pure prompt per distinct deliverable, count from the manifest (floor 7 full-skill RICH/MID; ≥5 forge-scale extension) → `references/prompts-v2/`. Then wire — all four, non-optional:
```bash
python3 execution/renaissance_audit.py        # must be 0 fail
python3 execution/prompt_library.py build
python3 execution/wire_prompt_pointers.py --write
# + add "Execution prompt: references/prompts-v2/<file>.md" under each workflow's output step
```

### P6 — Agent + Registration
- `agents/<expert>/AGENT.md` + `memory/context.md` (extension: append pins, don't recreate).
- **Per-workflow wrappers + shims are minted for you** — the Arsenal Loop owns this now
  (`directives/arsenal-loop.md`, 2026-07-25). The end-session spine mints at close and the 06:40
  sweep catches the rest; the PostToolUse hook flags it at write time. Do NOT hand-write wrappers.
- Want them fireable before you finish the session? One command:
```bash
python3 execution/mint_menu_wrappers.py --scope skill <skill-name> --apply
python3 execution/skill_auditor.py check --skill <skill-name>   # check 7 = menu_parity; must PASS
```

### P7 — Amplify Scan
Post-build, in the same run (from `/extract-amplify`): **Gap scan** (source material not yet operationalized) · **Depth scan** (workflows that deserve a split) · **Stacking scan** (cross-expert chains worth a Tier-3 workflow). Execute quick wins now; park the rest as named options in the report.

### P8 — Asset Scan (close-out verdicts — evaluate ALL, build what fits)
| Asset | Rule |
|---|---|
| **Agent** | Already shipped (P6) — confirm front door lists the skill |
| **Orchestrator** | BUILD `/[x]-os` when ≥8 workflows or a natural pipeline exists (per `/merch-os` precedent) |
| **Plugin** | RECOMMEND-only with evidence — Plugin Forge is hard-gated behind Farrice's operator-lift token; never auto-build |
| **Council seat** | RECOMMEND when the expert fills a `COUNCIL.md`/domain gap named in P2 |

Verdicts table goes in the P10 report even when everything is "not warranted."

### P9 — Verification (instrumented)
```bash
python3 execution/blind_pass.py prepare --expert <skill-dir>   # corpus: use the 2 unquoted enrichment sources
# side-by-side judgment per directives/embodiment-standard.md; then:
python3 execution/blind_pass.py record --expert <skill-dir> --verdict PASS|FAIL --notes "..." --generated <p> --reference <p>
python3 execution/skill_auditor.py check --skill <skill-dir>                       # ≥2 fails = B-cap
python3 execution/extraction_manifest.py check --skill skills/<skill-dir> --manifest .tmp/manifest-<slug>.json
```

### P10 — Finalize + Wiki + Report
- `chain_runner.py finalize` — evidence-based scores, `--anchor-named` for any ≥8, blind-pass verdict or `--skip-blind-pass` with the reason.
- `knowledge_compiler.py log ingest ... && knowledge_compiler.py briefing`.
- Release the lock: `python3 execution/session_lock.py release <token>`.
- **Report must contain**: manifest-vs-shipped table · enrichment ledger · asset-scan verdicts · per-workflow one-liners (what each covers) · parked amplify options. This is the "what did it actually do" contract.

## Modes summary

| Mode | Trigger | Output shape |
|---|---|---|
| Full (default) | New expert | Manifest-derived: 8-15 wf RICH / 4-7 MID / honest THIN; ≥7 prompts RICH-MID; references + agent + asset scan |
| **Extension** | Expert exists in `AGENT_INDEX.md` | Forge-scaled layer: 2-5 wf + ≥5 prompts into the existing skill; version bump; provenance append |
| Light | Explicit "light extract" only | MES Light (patterns + 1-3 crown-jewel prompts); no enrichment; never the default for short sources |

## Options
- **"light extract" / "skip validation" / "deep extract"** — as above.
- **/validate [skill]** — validation-only pass on an existing extraction.
- **/parallel-extract** — 2-5 extractions via sub-agents, fresh context each.
