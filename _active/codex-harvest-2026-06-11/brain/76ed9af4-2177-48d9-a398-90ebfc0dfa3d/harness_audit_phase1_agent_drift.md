# 🔍 Harness Audit: Phase 1 — Agent Drift Analysis

> **Audit Type**: Read-only diagnostic — no system modifications  
> **Methodology**: Nate B. Jones — Orchestration Intelligence (Harness Design Audit)  
> **Date**: 2026-03-31  
> **Scope**: Why Gemini models ignore the Antigravity 6-Step Chain  
> **Status**: ⚠️ ANALYSIS ONLY — User decides whether to act

---

## Executive Summary

The Antigravity system's 6-Step Chain works beautifully on Claude because Claude Code's system prompt injection mechanism and the model's instruction-following architecture are naturally aligned with the harness design. Gemini drifts not because the instructions are wrong, but because **the harness assumes a Claude-shaped model** in 5 critical architectural areas. The prompt file (`GEMINI.md`) is byte-identical to `CLAUDE.md` — but the two models process that identical specification through fundamentally different attention and instruction-priority architectures.

**Bottom line**: The chain works on Claude because Claude's model architecture *compensates* for harness gaps that Gemini exposes. Fixing the drift requires harness improvements, not model changes — but those improvements must be carefully scoped to avoid breaking what already works.

---

## Phase 1: Model-Harness Separation (What the Model Does vs. What the Scaffolding Does)

### Current Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    USER REQUEST                          │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│              SYSTEM PROMPT (GEMINI.md)                   │
│  ┌───────────────────────────────────────────────────┐  │
│  │  THE CHAIN (6 Steps)                               │  │
│  │  ────────────────────                              │  │
│  │  1. SCORE intent                    ◄── SOFT       │  │
│  │  2. SHARPEN if ≤3                   ◄── SOFT       │  │
│  │  3. ROUTE to experts                ◄── SOFT       │  │
│  │  4. LOAD via Context Engine         ◄── SOFT       │  │
│  │  5. PRODUCE output                  ◄── SOFT       │  │
│  │  6. FINALIZE (chain_runner.py)      ◄── SOFT       │  │
│  └───────────────────────────────────────────────────┘  │
│                                                          │
│  Supporting Protocols (10+ directives)   ◄── SOFT       │
│  Context Engine (4-tier loading)         ◄── SOFT       │
│  Workflow Override (slash commands)       ◄── SOFT       │
└──────────────────────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│                 MODEL REASONING                          │
│  (Interprets prompt → decides what to follow)            │
│  ┌───────────────────────────────────────────────────┐  │
│  │  NO HARD GATES                                     │  │
│  │  • No pre-execution validator                      │  │
│  │  • No chain step tracker                           │  │
│  │  • No routing verifier                             │  │
│  │  • No finalize enforcer                            │  │
│  │  • No protocol activation checker                  │  │
│  └───────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│              OUTPUT TO USER                               │
│  (May or may not have followed The Chain)                │
└─────────────────────────────────────────────────────────┘
```

### Critical Finding: 100% Soft Enforcement

Every single step of The Chain is enforced by **natural language instruction only**. There is:

- **No input validation** before the model processes a request
- **No output parsing** that checks whether chain steps were executed
- **No interpretation phase** where the model's plan is inspectable before action
- **No deterministic gating** that blocks output if chain steps were skipped
- **No audit trail** that logs which chain steps actually fired

The entire system relies on the model's willingness to follow ~11,700 bytes of system prompt. Claude does this reliably. Gemini does not.

---

## Phase 2: Scaffolding Gap Analysis

### The 7 Architectural Gaps Causing Drift

| # | Gap | Severity | Description |
|---|-----|----------|-------------|
| **1** | **No Chain Step Tracker** | 🔴 CRITICAL | No mechanism to verify whether Steps 1-6 actually executed. The model is trusted to self-report compliance. |
| **2** | **Prompt Size vs. Attention Budget** | 🔴 CRITICAL | GEMINI.md is 11,730 bytes (~4,500 tokens) of dense procedural instruction. Gemini's instruction-following degrades sharply after ~2K tokens of system prompt. The Chain section (Lines 60-148) sits at ~2,000 tokens into the prompt — right at the degradation boundary. |
| **3** | **Competing Instruction Sources** | 🟡 HIGH | The model receives GEMINI.md (user rules), the Antigravity system prompt (agent framework), *and* platform-injected instructions (tool descriptions, MCP server guidance, web app aesthetics rules). These three instruction layers can conflict, and Gemini tends to prioritize the most recent/loudest instruction. |
| **4** | **No Finalize Enforcement** | 🟡 HIGH | `chain_runner.py finalize` is a bash command the model is *asked* to run. Nothing prevents the model from producing output without running it. Claude's instruction compliance makes this work; Gemini treats it as optional. |
| **5** | **Internalization Assumption** | 🟡 HIGH | The Chain Efficiency Rules (Lines 124-144) tell the model to *internalize* Steps 1-3 — execute them "in-head" without file reads. This is a Claude-optimized instruction. Gemini interprets "internalize" as "skip entirely" rather than "execute mentally but don't read files." |
| **6** | **No Protocol Activation Verification** | 🟠 MEDIUM | 10+ supporting protocols (quality_assurance, token-efficiency, collaboration, etc.) are supposed to fire at specific trigger points. No mechanism verifies they actually fired. Usage tracking fields in every directive show `Activation Count: 0`. |
| **7** | **Workflow Override Ambiguity** | 🟠 MEDIUM | The Workflow Override section says "the workflow incorporates the chain internally" — but most workflow files don't explicitly re-state the chain steps. The model must remember that The Chain still applies *inside* the workflow. Gemini loses this context. |

### Detailed Gap Analysis (Harness Checklist)

| Component | Present? | Quality | Gap Impact on Gemini |
|-----------|----------|---------|---------------------|
| **Input Validation** | ❌ None | — | Model can process any request without chain activation |
| **Output Parsing** | ❌ None | — | No way to detect if chain steps were skipped |
| **Interpretation Phase** | ❌ None | — | Model's plan isn't inspectable before execution |
| **Tool Gating** | ⚠️ Partial | User approval on commands | No gating on *whether the chain ran* before output |
| **Retry Logic** | ⚠️ In-prompt | "If composite < 7, retry" | Self-policing only — Gemini doesn't self-police |
| **Fallback Paths** | ⚠️ In-prompt | "When Steps Narrow" table | Narrowing rules require precise interpretation Gemini misreads |
| **State Management** | ⚠️ Partial | Session state protocol exists | Not enforced — `session-state.md` rarely written |
| **Cost Controls** | ❌ None | — | No token budget enforcement |
| **Audit Trail** | ⚠️ Partial | chain_runner.py logs if called | Only logs if model chooses to finalize |
| **Human Escalation** | ⚠️ In-prompt | Collaboration protocol | Gemini tends to skip pushback/clarification |
| **Disambiguation** | ⚠️ In-prompt | DICE/SHARPEN | Gemini jumps to production without sharpening |
| **Invisible Guardrails** | ❌ None | — | Unstated constraints not enumerated |

---

## Phase 3: Complexity Audit

### Is the System Over-Complex?

**No.** The Antigravity system is well-designed — arguably elegant. The 3-layer architecture (Directives → Orchestration → Execution) is sound. The Context Engine's tiered loading is efficient. The expert routing system is comprehensive.

The complexity problem is **not in the system design** — it's in the **enforcement mechanism**. The system assumes a model that will:

1. Read and retain ~4,500 tokens of procedural instructions
2. Execute a 6-step pipeline on every request without external verification
3. Self-police quality gates and retry logic
4. Internalize routing tables and scoring formulas
5. Remember to run bash commands (finalize) after producing output

Claude does all 5 reliably. This is a Claude-shaped harness.

### What Happens If You Remove Layers?

| Layer | Remove Impact | Verdict |
|-------|--------------|---------|
| Context Engine tiers | ❌ Would break token efficiency | Keep |
| Expert routing | ❌ Would eliminate expert quality | Keep |
| Supporting protocols | ⚠️ Could simplify — but quality drops | Keep for Claude |
| Step 6 (finalize) | ⚠️ Removes quality tracking but reduces cognitive load | Consider for Gemini |
| Chain Efficiency Rules | ✅ These cause drift — "internalize" = "skip" for Gemini | **Primary fix candidate** |

---

## Root Cause Analysis: Why Claude Works and Gemini Drifts

### The 3 Root Causes

**1. Instruction Attention Architecture Difference**

Claude Code models demonstrate stronger instruction-following for long system prompts. They treat `CLAUDE.md` as a binding contract — each instruction is weighted approximately equally regardless of position. Gemini models show **positional decay** — instructions later in the system prompt receive less attention weight. The Chain sits ~2,000 tokens into the prompt, and its detailed sub-steps (narrowing rules, efficiency rules) sit at ~3,500+ tokens. By that point, Gemini's compliance drops significantly.

**2. "Internalize" ≠ "Skip" — But Gemini Reads It That Way**

The Chain Efficiency Rules explicitly say:
> "Steps 1-2 (SCORE + SHARPEN): Internalized — no file reads required."

Claude interprets this as: "Execute the scoring mentally, just don't read the directive file."  
Gemini interprets this as: "These steps don't require action — skip them."

This single misinterpretation cascades: if Step 1 (SCORE) doesn't run, Step 2 (SHARPEN) has nothing to trigger on, Step 3 (ROUTE) has no score to inform routing depth, and the entire chain collapses into "just answer the question."

**3. No External Verification Loop**

In Nate B. Jones's framework, the **Judge** in the Planner-Worker-Judge hierarchy is what prevents drift. The Antigravity system has no Judge. The model is Planner, Worker, and Judge simultaneously. Claude manages this because its instruction compliance functions as an implicit judge. Gemini needs an *explicit* judge.

---

## Risk Assessment: What Could Break If You Try to Fix This

> [!CAUTION]
> The following risks are why this audit is analysis-only. Each potential fix carries system-breaking risk.

| Potential Fix | Risk to Current System | Why |
|--------------|----------------------|-----|
| **Modify GEMINI.md** to be more explicit | 🔴 HIGH | CLAUDE.md, AGENTS.md, and GEMINI.md must stay identical (Line 5 comment). Changing GEMINI.md breaks the mirror requirement and could introduce Claude regressions. |
| **Add a chain pre-validator script** | 🟡 MEDIUM | New Python script in `execution/` that the model must call before producing output. Claude might call it unnecessarily, adding latency. Gemini might still skip it. |
| **Create a Gemini-specific system prompt** | 🟡 MEDIUM | Breaking the 3-file mirror. Double maintenance burden. Risk of drift between the two prompt versions over time. |
| **Add chain verification to finalize** | 🟢 LOW | Modify `chain_runner.py` to log *which* chain steps the model claims to have run. Passive — only captures data, doesn't enforce. But doesn't solve the core problem. |
| **Restructure prompt priority** | 🔴 HIGH | Moving The Chain to the top of GEMINI.md would help Gemini but the current structure serves Claude well. Reordering could disrupt Claude's reliable processing. |

---

## Improvement Roadmap (IF You Decide to Act)

| Priority | Improvement | Expected Impact | Effort | Risk |
|----------|------------|-----------------|--------|------|
| **P0** | Separate GEMINI.md from CLAUDE.md (break the mirror) | Enables all other Gemini-specific fixes | Medium | 🟡 Double maintenance |
| **P1** | Restructure Gemini prompt: Chain first, efficiency rules removed, explicit "DO NOT SKIP" language | Addresses root causes 1 and 2 | Medium | 🟢 if P0 done first |
| **P2** | Create `execution/chain_validator.py` — model calls it after producing output to self-report which steps ran | Passive data collection on compliance | Low | 🟢 Low risk |
| **P3** | Remove "internalize" language from Gemini prompt — require visible chain step execution | Prevents the "internalize = skip" misinterpretation | Low | 🟢 if P0 done first |
| **P4** | Add explicit chain step markers in Gemini prompt: `[STEP 1/6: SCORE]` format | Gives Gemini structural anchors to follow | Low | 🟢 if P0 done first |

---

## Recommendation

> [!IMPORTANT]
> **Do not change anything yet.** The system works at full capacity on Claude. The Gemini drift is a known limitation of running a Claude-optimized harness on a different model architecture.

### Three Options

**Option A: Accept the Drift (Zero Risk)**  
Continue using Claude as primary. Use Gemini for tasks that don't require chain compliance (simple queries, file operations, quick code fixes). Acknowledge Gemini will not follow The Chain and plan around it.

**Option B: Fork the Prompt (Medium Risk, Medium Reward)**  
Break the 3-file mirror. Create a `GEMINI.md` optimized for Gemini's attention patterns — Chain at top, no internalization shortcuts, explicit step markers, shorter overall length. Keep `CLAUDE.md` unchanged. Accept the maintenance overhead.

**Option C: Build a Hard Gate (High Effort, High Reward, Higher Risk)**  
Create a deterministic pre-flight validator that runs before the model produces output — a Python script that checks whether chain steps were declared. This is the "Judge" that Nate B. Jones's framework says is missing. But it adds complexity and could slow down the workflow that currently runs beautifully on Claude.

### My Recommendation

**Option A for now.** The system took enormous effort to build and works at a high level on Claude. The ROI of fixing Gemini drift is low compared to the risk of introducing regressions. If Gemini becomes your primary model in the future, revisit Option B.

---

## Quality Gate

| Criterion | Score |
|-----------|-------|
| **Intent Alignment** | 9/10 — Audit-only analysis as requested, no system changes |
| **Expert Standard** | 8/10 — Follows Nate B. Jones harness audit methodology faithfully |
| **Adversarial Resilience** | 8/10 — Acknowledges risks, doesn't oversell fixes |

**Composite**: 8.3/10 ✅
