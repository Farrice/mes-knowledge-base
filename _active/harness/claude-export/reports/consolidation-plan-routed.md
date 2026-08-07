# Claude Export — ROUTED Consolidation Plan

**43 unique systems** routed against the existing 273 skills.
Route counts: {'FLAGSHIP': 2, 'BUILD_NEW': 10, 'MERGE': 15, 'REFERENCE_ONLY': 8, 'SKIP': 8}

> Disagreement = two routing agents split (surfaced for your call). Kept the higher-value read; the alternative is noted.

## 🟢 BUILD_NEW — genuinely novel systems → `/convert-prompt` (Path B)

| value | system | theme | chars | proposed skill | disagree | md_path |
|-------|--------|-------|-------|----------------|----------|---------|
| 9 | Intelligence Architecture Studio V3 | misc | 9124 | intelligence-architecture-domain-agent-design | ⚠️ BUILD_NEW/REFERENCE_ONLY | `.tmp/claude-export/normalized/projects/0196ae4b-a14d-7703-8313-6927ec14badc.md` |
| 9 | 3.7 KACE: Knowledge Acquisition & Comman | knowledge-arch | 8461 | kace-mastery-architecture |  | `.tmp/claude-export/normalized/projects/038a72b6-c840-4830-9621-d63cb0a759f4.md` |
| 8 | Context Profile Architect 2.0 | context-architect | 62399 | context-profile-architect |  | `.tmp/claude-export/normalized/projects/0199f2e9-533d-7501-ac3c-be9063fd4475.md` |
| 8 | Josh and Katie Fitness Hub | misc | 15375 | andy-galpin-training-intelligence |  | `.tmp/claude-export/normalized/projects/019b8ed3-762d-7004-9128-965a47f1b582.md` |
| 8 | Craig Clemens Marketing Machine | copywriting | 14789 | craig-clemens-copywriting | ⚠️ BUILD_NEW/MERGE | `.tmp/claude-export/normalized/projects/6b98866c-3ae8-4bbc-ae8b-aef963ef49e5.md` |
| 8 | LinkedIn: Coach Cooz Hub | coaching | 9126 | coach-cooz-revenue-system | ⚠️ BUILD_NEW/MERGE | `.tmp/claude-export/normalized/projects/bea5cffa-bb4c-44fb-adb9-cc8b4512222c.md` |
| 8 | Enhanced Unified Expert Transformation & | coaching | 8317 | expert-transformation-engine | ⚠️ BUILD_NEW/REFERENCE_ONLY | `.tmp/claude-export/normalized/projects/f4506a88-bdb0-4f2e-9062-7e0365e78bd4.md` |
| 8 | COGNITIVE ENGAGEMENT OPTIMIZATION SYSTEM | misc | 10259 | cognitive-engagement-optimizer |  | `.tmp/claude-export/normalized/projects/a03a0133-9a87-4705-9975-37bc6ffccf5e.md` |
| 7 | PROSPERITY COACH SYSTEM | coaching | 34666 | prosperity-coach-system |  | `.tmp/claude-export/normalized/projects/0198ed9a-7175-769c-9230-b32b41f7e64f.md` |
| 6 | Fitness Ai Agent | prompt-engineering | 289 | fitness-ai-agent |  | `.tmp/claude-export/normalized/projects/80677e89-3bf4-4b88-a629-6b171a667c74.md` |

## ⭐ FLAGSHIP — collapse a family into one canonical skill

| value | system | proposed skill | md_path |
|-------|--------|----------------|---------|
| 10 | MES 3.0 - Virtuoso Extraction |  | `.tmp/claude-export/normalized/projects/019997d0-5251-74be-b6d9-4bee93c460bc.md` |
| 9 | Mastery Extraction System 3.0 - Expert Repli | extract-mastery | `.tmp/claude-export/normalized/projects/019722eb-6fe2-70e7-b383-482af4bb707c.md` |

## 🔵 MERGE — add into an existing skill → `/convert-prompt --add-to` / `/extract-amplify`

| value | system | → target skill | disagree | md_path |
|-------|--------|----------------|----------|---------|
| 8 | Skill Download MES 3.0 | mas-3-extraction |  | `.tmp/claude-export/normalized/projects/019b1175-792d-7652-a454-6c66ce4a418c.md` |
| 8 | CopyBlocks - Writing and Storytelling  | luke-iha-copy-blocks | ⚠️ MERGE/SKIP | `.tmp/claude-export/normalized/projects/296ceb70-93ae-4a83-a0ef-35dde37dd431.md` |
| 7 | Skill Architect | skill-creator |  | `.tmp/claude-export/normalized/projects/0199fb72-214c-7703-9bac-1b1f449212e6.md` |
| 7 | META-PROMPT ARCHITECTURE MASTERY SYSTE | futurepedia-prompt-engineering |  | `.tmp/claude-export/normalized/projects/01998b4c-9f91-71f5-b870-43988ec815fb.md` |
| 6 | Farrice Cain-Premium Ghostwriter | ghostwriting-voice-engine |  | `.tmp/claude-export/normalized/projects/0199a003-a855-7326-9495-91a7966a9d62.md` |
| 6 | Collaborative Copywriting and Marketin | chris-cimorelli-copywriting |  | `.tmp/claude-export/normalized/projects/b50d34fe-def2-419f-ba0e-5a6ef31f5674.md` |
| 6 | New-OHKIF Knowledge Architecture Studi | extract-forge |  | `.tmp/claude-export/normalized/projects/bf2b6df4-ed36-4597-8287-a464af4c91c6.md` |
| 6 | PROMETHEAN 2.0: Advanced Prompt Engine | futurepedia-prompt-engineering | ⚠️ MERGE/REFERENCE_ONLY | `.tmp/claude-export/normalized/projects/0198d7d6-5ae7-774f-bfd1-ec46c209aa0c.md` |
| 6 | LinkedIn 2025 - Jasmin Alic System | jasmin-alic-linkedin-growth | ⚠️ MERGE/SKIP | `.tmp/claude-export/normalized/projects/c10c06cd-f085-4387-97c7-8cfc09affbbb.md` |
| 6 | Enhanced Custom Instructions with Expe | futurepedia-prompt-engineering | ⚠️ MERGE/REFERENCE_ONLY | `.tmp/claude-export/normalized/projects/36cfdfba-db69-41e0-8479-825baea924a1.md` |
| 5 | Maria $600K System | maria-wendt-digital-products |  | `.tmp/claude-export/normalized/projects/019913ab-c28e-7734-8a27-8ebbe8e895ff.md` |
| 5 | Modular Adaptive Prompt Engineering (M | futurepedia-prompt-engineering | ⚠️ MERGE/REFERENCE_ONLY | `.tmp/claude-export/normalized/projects/e67652ae-3dd1-48c6-a3e5-84e37a3191e8.md` |
| 4 | Custom Instructions Poe.ai 3.5 Sonnet  | futurepedia-prompt-engineering |  | `.tmp/claude-export/normalized/projects/2ddb6ee8-dcdf-4818-a0ff-e2b05c0e56aa.md` |
| 4 | Expert Panel-Prompt Engineer System Em | futurepedia-prompt-engineering |  | `.tmp/claude-export/normalized/projects/7eae875e-83c3-4bee-8c06-83cd2f921ed9.md` |
| 4 | Farrice Brainstorming Hub | seth-godin-philosophy |  | `.tmp/claude-export/normalized/projects/019ba2fe-a705-743d-b45e-d06b225801d1.md` |

## ⚪ REFERENCE_ONLY (8) — keep searchable in memory, no skill

- KACE-OHKIF Unified Knowledge Architecture (knowledge-arch, 12035 chars) — The foundational command-based knowledge architecture framework (KACE, OHKIF, /e
- Notion Prompt Librarian-Fresh OS System Transfer H (misc, 8737 chars) — Infrastructure/workflow automation for personal prompt database organization; sp
- Supreme Creative Solutions System - Master Configu (misc, 8851 chars) — Generic expert panel assembly system; standard pattern covered by multiple exist
- Improving the 27 Copy Codes Prompt Course (prompt-engineering, 3398 chars) — Expert Panel prompt engineering system that overlaps with existing /futurepedia-
- Prosperity Algorithm Context Profile (extraction-mes, 26157 chars) — MES 3.0 extraction of Fladlien's system; 6+ competing MES 3.0 extractions exist 
- Complete Final Enhanced Unified CAPS Transformatio (coaching, 8741 chars) — Domain-agnostic content transformation system with generic enhancement protocols
- Autonomous Knowledge Extraction & Repurposing Syst (extraction-mes, 1599 chars) — Minimal extraction/MES variant (1.6k chars); user already has robust MES 3.0 sys
- Enhanced Expert Panel & Deep Reasoning v4 (prompt-engineering, 15490 chars) — Part of generic expert-panel family; weaker than better-architected extraction s

## ⚫ SKIP (8) — test/experiment/exact-dupe, drop

- Version 1: Complete Original System as Custom Inst — Early version of expert panel collaborative framework; superseded by r
- OmniFlow Supreme 4.0 — Personal AI assistant orchestration with memory/retrieval and expert p
- Apex Co-Creator v2.0 — Generic multi-tool orchestration assistant that remixes common Claude 
- Testing grounds for Ai Custom Instructions Effecti — Explicit test-experiment project for brainstorming and prompt engineer
- Logline test instructions — Test-experiment theme with narrow screenwriting focus; overlaps /eric-
- (RAPES) Testing system — Marked as test-experiment theme; experimental RAPES framework not prod
- Cooz podcast content — Tiny personal brand voice guide (979 chars) for Coach Cooz; non-genera
- Coach Fresh 5.2 Testing — Marked test-experiment; unstable iteration of multi-expert orchestrato
