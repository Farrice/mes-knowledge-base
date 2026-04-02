# Claude Code Harness Analysis

> **Reference only.** This project folder contains publicly archived copies of the Claude Code v2.1.88 source leak from March 31, 2026. It exists for study, comparison, and learning — NOT for integration into our system.

## ⚠️ Safety Notice
- These repos are **isolated reference material** — do not run, install, or import any code
- Do NOT `npm install` anything from this folder
- The source code is Anthropic's intellectual property archived for educational research

---

## What's In Here

### 1. `source-code-v2.1.88/` — Full TypeScript Source (1,904 files)
The complete agentic harness from npm package `@anthropic-ai/claude-code` v2.1.88.
- **`src/tools/`** — ~40 discrete tools (BashTool, FileWriteTool, WebFetchTool, MCPTool, WebSearchTool, TeamCreateTool, etc.)
- **`src/tasks/`** — Task orchestration (DreamTask/KAIROS, RemoteAgentTask, LocalAgentTask, InProcessTeammateTask, LocalShellTask)
- **`src/assistant/`** — Core assistant/query engine
- **`src/ink/`** — Terminal UI (React Ink components, hooks, layout)
- **`src/migrations/`** — Schema migrations

### 2. `system-prompts/` — 30 Extracted System Prompts
The full system prompt library, cleanly extracted:
| # | Prompt | Purpose |
|---|--------|---------|
| 01 | Main System Prompt | Core agent persona + behavior |
| 02 | Simple Mode | Reduced capability mode |
| 03 | Default Agent Prompt | Base agent scaffolding |
| 04 | Cyber Risk Instruction | Security guardrails |
| 05 | Coordinator System Prompt | Multi-agent orchestration |
| 06 | Teammate Prompt Addendum | Worker agent instructions |
| 07 | Verification Agent | Output verification |
| 08 | Explore Agent | Codebase exploration |
| 09 | Agent Creation Architect | Agent spawning |
| 10 | Statusline Setup Agent | UI configuration |
| 11-30 | Various | Permissions, YOLO mode, memory, compact, skills, etc. |

### 3. `kuberwastaken-analysis/` — Rust Rewrite + Analysis
Community breakdown with extracted constants, system prompt reconstruction, and a Rust reimplementation.

---

## Key Architecture Insights (For Our System)

### 1. Memory Architecture (3-Layer)
```
Layer 1: MEMORY.md → Lightweight pointer index (~150 chars/entry), always in context
Layer 2: Topic Files → On-demand project knowledge, never all loaded at once
Layer 3: Raw Transcripts → Grep-only, never re-read fully
```
**Key principle: "Strict Write Discipline"** — memory updates only after confirmed successful writes. Agent treats its own memory as "hints" and verifies against codebase.

### 2. Tool System (~40 tools, ~29K lines)
Plugin-style architecture. Each tool has:
- Own permission model
- Validation logic
- Output formatting
- Safety guards (BashTool has shell execution safeguards)

### 3. Multi-Agent Orchestration
- **Coordinator Mode** — One Claude spawning and managing multiple worker Claudes in parallel
- **Task distribution, result aggregation, and conflict resolution** between workers
- Task types: `RemoteAgentTask`, `LocalAgentTask`, `InProcessTeammateTask`

### 4. Hidden Features (Unreleased)
- **KAIROS** — Autonomous background daemon with `autoDream` for nightly memory consolidation
- **ULTRAPLAN** — 30-min remote Opus planning sessions in cloud containers
- **BUDDY** — Tamagotchi-style AI pet (18 species, rarity tiers)

### 5. Anti-Distillation Defenses
- Fake tool injection against traffic recording
- Cryptographically signed reasoning summaries
- Server-side connector-text summarization

### 6. Frustration Detection
Regex-based user frustration detection in `userPromptKeywords.ts` — practical over elegant.

---

## Relevance to Antigravity

| Claude Code Pattern | Our Equivalent | Learning Opportunity |
|---|---|---|
| 3-layer memory | `.agent/session-state.md` + KIs | Claude's pointer-based MEMORY.md is more granular |
| Tool system (40 tools) | Execution scripts + MCP tools | Their permission model per tool is sophisticated |
| Coordinator Mode | `/parallel-swarm`, `/swarm` | Study their task distribution + conflict resolution |
| KAIROS (autoDream) | `/self-evolve`, harness commands | Nightly autonomous memory consolidation |
| System prompts (30) | `CLAUDE.md` / `GEMINI.md` | Their prompt decomposition is extremely modular |
| Frustration detection | — | Could add user-state awareness |
| Anti-distillation | — | Interesting defensive posture |

---

## How to Use This

1. **Read the system prompts first** — `system-prompts/prompts/01_main_system_prompt.md` is the crown jewel
2. **Study the tool architecture** — `source-code-v2.1.88/src/tools/` for permission models
3. **Analyze the orchestration** — `source-code-v2.1.88/src/tasks/` for multi-agent patterns
4. **Compare with our system** — Use the relevance table above as a study guide

## Source
- Leak date: March 31, 2026 (~04:23 UTC)  
- Cause: `.npmignore` misconfiguration shipped `main.js.map` with source references
- 512,000 lines of TypeScript, 1,906 files
- Original discovery: @Fried_rice (Chaofan Shou)
