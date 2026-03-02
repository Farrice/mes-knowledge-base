# Portable Architecture Bundle

## What This Is

This bundle contains the orchestration architecture built for MES 3.0. It's designed to be analyzed and potentially implemented in any Claude environment that has expert extractions.

**Origin:** Built by synthesizing methodologies from Boris (Claude Code creator), Mark Kashef (AI Council), and Lance & Yichao (Context Engineering).

---

## Contents

| File | Purpose |
|------|---------|
| `NATURAL-LANGUAGE-ACTIVATION.md` | Intent recognition patterns — how Claude auto-deploys capabilities based on how the user talks |
| `CREATIVE-ASSEMBLY-SKILL.md` | Multi-expert production pipeline — parallel execution, handoffs, refinement |
| `WIDE-RESEARCH-SKILL.md` | Manus-style parallel research — scouts, social listening, pattern detection, verification |
| `COLLABORATION-PROTOCOL.md` | Anti-sycophancy mandate — clarifying questions, honest confidence, pushback, healing loop |
| `RESEARCH-SUBAGENTS/` | 5 subagent definitions for the Wide Research system |

---

## How The Systems Work

### 1. Natural Language Activation
User just talks. Claude recognizes intent and deploys:
- "Write me..." → Creative Assembly
- "Research..." → Wide Research
- "Should I..." → Council mode

No commands needed.

### 2. Creative Assembly
Multiple experts work in parallel on creative tasks:
```
DECOMPOSE → ASSIGN EXPERTS → PARALLEL PRODUCE → ASSEMBLE → EDIT → DELIVER
```

Two modes:
- **Full Assembly:** One polished piece returned
- **Selection Assembly:** ("show me options") Multiple versions, user picks, then polish

### 3. Wide Research
Parallel subagents gather intelligence:
```
DECOMPOSE → DEPLOY SCOUTS → GATHER → SYNTHESIZE → VERIFY → DELIVER
```

Subagents:
- Research Scout — focused gathering
- Social Listener — voice-of-customer mining
- Pattern Hunter — signal detection
- Verification Agent — fact checking
- Synthesis Engine — insight extraction

### 4. Collaboration Protocol
Claude operates as creative partner:
- Asks clarifying questions when uncertain
- Signals confidence levels honestly
- Self-corrects through healing loop
- Pushes back when approach seems suboptimal

---

## To Implement

1. **Review each file** — Evaluate fit for your environment
2. **Customize expert names** — Swap placeholders for your actual extractions
3. **Adapt domain routing** — Match your coverage areas
4. **Integrate into CLAUDE.md** — Or equivalent configuration

---

## Dependencies

- Expert extractions (you provide these)
- Claude Code or Claude environment that reads CLAUDE.md
- Task tool access for parallel subagent execution

---

## What This Enables

- Eliminates manual prompt orchestration
- Parallel expert execution (not sequential)
- Structured handoffs prevent context pollution
- Quality gates catch issues before delivery
- Research-informed creative production
- Anti-sycophancy built into operating behavior

---

*Built from MES 3.0 — ready for evaluation and adaptation.*
