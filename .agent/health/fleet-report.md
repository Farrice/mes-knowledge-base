# Fleet Verification Report
**Generated**: 2026-08-08T12:28:18.096787

**Verifiers run**: 84 · FAIL 23 · PASS 55 · TIMEOUT 6

## ⚠️ Stale or missing aggregate inputs (NOT merged)

- **loop-integrity** — STALE, mtime 2026-07-28T09:31 (266.9h before this run)
- **core-surface** — STALE, mtime 2026-07-28T09:31 (266.9h before this run)
- **birth-wiring** — STALE, mtime 2026-07-28T09:36 (266.8h before this run)

## 🚨 Verifiers not passing

- **verify_activation_governor.py** — FAIL: - dependency import failed: No module named 'dotenv'
- **verify_antigravity_global_access.py** — FAIL: AssertionError: workflow router did not bind the mixed request to /system-audit
- **verify_artifact_router.py** — TIMEOUT: exceeded 90s
- **verify_autopilot_routing.py** — TIMEOUT: exceeded 90s
- **verify_autopilot_runtime_preflight.py** — TIMEOUT: exceeded 90s
- **verify_codex_claude_parity.py** — FAIL: ImportError: cannot import name 'strip_explicit_invocation_artifacts' from 'control_intent' (/Users/farricecain/Google Antigravity/execution/control_intent.py)
- **verify_codex_end_session.py** — FAIL: TypeError: cannot unpack non-iterable PosixPath object
- **verify_control_intent.py** — FAIL:     text: draft a post about how neurons are chained into circuits
- **verify_convene.py** — FAIL: ModuleNotFoundError: No module named 'execution'
- **verify_dhar_mann_transformational_content_factory.py** — FAIL: - NOTE: direct command search surfaces Dhar factory
- **verify_google_operator_core.py** — FAIL: ImportError: cannot import name 'strip_explicit_invocation_artifacts' from 'control_intent' (/Users/farricecain/Google Antigravity/execution/control_intent.py)
- **verify_health_performance_geo_prompt.py** — FAIL: FAIL: missing prompt: /Users/farricecain/Google Antigravity/_active/health-performance-ip-library/AUTOMATION_PROMPT.md
- **verify_memory_stack.py** — FAIL: - genai_import: No module named 'google'
- **verify_operator_cockpit.py** — TIMEOUT: exceeded 90s
- **verify_operator_core_extraction_governor_agent.py** — FAIL: AssertionError: workflow_router expected /autopilot first for 'extraction-governor-agent is broken and writes state automatically'; got /system-audit                             — Control-plane audit 
- **verify_operator_core_fast_proof.py** — TIMEOUT: exceeded 90s
- **verify_operator_core_health_check.py** — FAIL:   /mission                                  — Mission OS - plan, validate, execute, and govern long-running agent work
- **verify_operator_core_knowledge_librarian.py** — FAIL: AssertionError: workflow_router expected /autopilot first for 'the knowledge library routing is broken'; got /system-audit                             — Control-plane audit for Autopilot, routing, bri
- **verify_operator_core_routing_intelligence.py** — FAIL: AssertionError: workflow_router expected /autopilot first for 'the router is broken and routing intelligence is wrong'; got /system-audit                             — Control-plane audit for Autopilo
- **verify_operator_core_skill_anneal.py** — FAIL: AssertionError: workflow_router expected /autopilot first for 'skill-anneal is broken and rewriting everything'; got /system-audit                             — Control-plane audit for Autopilot, rout
- **verify_operator_core_source_to_skill_system.py** — FAIL: AssertionError: workflow_router expected /autopilot first for 'source-to-skill-system is broken and creates bloat'; got /system-audit                             — Control-plane audit for Autopilot, r
- **verify_performance_evidence_gate.py** — FAIL: ModuleNotFoundError: No module named 'dotenv'
- **verify_proof_ledger.py** — FAIL: verify_proof_ledger.py: error: the following arguments are required: --draft, --ledger
- **verify_savant_control_room.py** — TIMEOUT: exceeded 90s
- **verify_search_content_mastery.py** — FAIL: }
- **verify_skill_evolution_candidate_freshness.py** — FAIL: - safe refresh command: python3 execution/skill_evolution_candidates.py scan --write
- **verify_skill_evolution_local_first.py** — FAIL: ModuleNotFoundError: No module named 'dotenv'
- **verify_system_control_plane.py** — FAIL: AssertionError: workflow_router source-command-health-check-status expected first route in ['health-check'], got /system-audit
- **verify_video_context_source_package.py** — FAIL: verify_video_context_source_package.py: error: the following arguments are required: package
