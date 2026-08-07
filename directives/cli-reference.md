# CLI Reference — Execution Scripts

> Extracted from CLAUDE.md 2026-06-09 (rebuild). Pure reference — read on demand.
> All commands run from project root. Check `execution/` for existing tools before creating new ones.

## Core Scripts

```bash
python execution/notion_api.py query <database_id>
python execution/notion_api.py capture "Title" "Body" --type Task --tags Revenue,Urgent
python execution/generate_image.py "prompt"
python execution/skill_converter.py
python execution/sync_registries.py
python execution/fetch-transcript.py "<youtube_url>" "<expert>"          # transcript-only
python execution/fetch-video-context.py "<video_url>" "<expert>"          # frame-grounded vision (claude-video wrapper)
python3 execution/signal_scout.py [--creators a,b | --posts url,..]       # LinkedIn listening: engager roster + resonance (LISTENING-ONLY, never contacts; feeds Angle Brief Mon/Thu via execution/angle_brief_run.sh)
python3 execution/render_brief.py <brief.json> [--open|--gdoc]            # research-brief JSON → house-style HTML on the briefs board
```

(`execution/parallel_swarm.py` is deprecated — superseded by `/convene` and the Workflow-tool swarms.)

## Calibration & Quality Tools

```bash
python execution/ground_truth.py gap-report          # Expert benchmark coverage
python execution/ground_truth.py compare <domain> <ai_output>  # Blind comparison
python execution/ground_truth.py add <domain> <file> --expert <name>  # Add sample
python execution/revenue_tracker.py pipeline          # Deliverables needing outcome data
python execution/revenue_tracker.py log "deliverable" --revenue 500 --outcome "result"
python execution/revenue_tracker.py report            # ROI by skill/expert
python execution/prose_classifier.py check <file>     # AI-prose detection
python execution/prose_classifier.py scan deliverables/  # Batch scan
```

**Ground Truth** (`knowledge/expert-benchmarks/`): 7 domains, 16 experts. Blind comparison feeds feedback ratchet.
**Revenue Tracker** (`.agent/revenue-outcomes.json`): Connects quality scores to business outcomes. Drained weekly via `/weekly-closeout`.
**Prose Classifier**: Integrated into `chain_runner.py` — warns if Expert Standard inflated by AI-prose patterns.

## Audit & Enforcement Infrastructure

```bash
# Routing enforcement
python3 execution/routing_enforcer.py check --request "..." --workflow <name> --quiet
python3 execution/routing_enforcer.py list

# Extraction usage telemetry (NEVER a gate — Farrice's standing decision 2026-06-09)
python3 execution/forge_gate.py status                               # production-use count of last extraction
python3 execution/forge_gate.py record <skill-dir> --expert <name>   # at end of extraction

# Cost gate (HARD-enforced by PreToolUse hook)
python3 execution/cost_gate.py check --service <id> --request "..."
python3 execution/cost_gate.py approve --service <id> --request "..."   # ONLY after explicit user yes; 15-min token
python3 execution/cost_gate.py status

# Recall grounding observability
python3 execution/recall_logger.py log --status fired|skipped|failed [...]
python3 execution/recall_logger.py report --days 7

# Calibrated rubric + eval harness
python3 execution/eval_harness.py status
python3 execution/eval_harness.py calibrate --days 7
python3 execution/eval_harness.py anchor --dimension <d> --score <n>

# Evolution orchestrator (auto-scheduled daily 07:00 via launchd com.antigravity.evolution-auto)
python3 execution/evolution_orchestrator.py auto|daily|weekly|monthly|status|queue

# Skill auditor
python3 execution/skill_auditor.py audit|duplication
python3 execution/skill_auditor.py update-index --apply
python3 execution/skill_auditor.py archive --tier REVIEW --names a,b --annotate --apply  # de-index in place (preferred)
python3 execution/skill_auditor.py archive --tier C --apply  # physical move — PREVIEW FIRST
```

**Read `_active/harness/system-audit/audit-2026-04-24.md` before significantly changing the system.** Directive nav: `directives/INDEX.md`.

## Knowledge Compiler — Karpathy Wiki Engine

```bash
python execution/knowledge_compiler.py stats|full|briefing|inventory|index|lint|stale|overlap
python execution/knowledge_compiler.py auto-archive [--execute]
python execution/knowledge_compiler.py log <action> "title" --domain X --expert Y
python execution/knowledge_compiler.py archive "query" result.md --domain X
```

240+ files, 1.8M+ words across `knowledge/`, `extractions/`, `research_outputs/`. Three operations: **ingest** (cascade updates), **query** (search write-back), **lint** (contradictions, orphans, stale). Living index: `knowledge/index.md`. Log: `knowledge/log.md`. Reflection: `/reflect` → `knowledge/synthesis/`.

**Notion Vault Sync**: `python execution/notion_api.py vault-create "Title" --expert X --domain Y` — auto-triggered by `finalize` for quality >= 7.
**Autofill Config**: `directives/notion-autofill-guide.md`.

## Evolution Direction

`directives/evolution-direction.md`: Single source of truth for what to evolve. Read before `/skill-evolution`. Updated after every cycle.
