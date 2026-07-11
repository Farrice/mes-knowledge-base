---
name: "plan-mode-architect"
source_prompt: "skills/boris-claude-code/references/prompts/plan-mode-architect.md"
skill: "boris-claude-code"
standard: structure-pure-v2
refactored: "2026-07-11"
fidelity: "standard"
---



## Input Required
- **Project Objective**: The high-level goal (e.g., "Build a CLI tool that converts raw Slack telemetry into actionable GitHub Issues").
- **Technical Substrate**: The tech stack, existing infrastructure, and model constraints (e.g., TypeScript, Claude 3.5 Sonnet, 200k context window).
- **Latent Demand/Abuse Patterns**: How users are currently "hacking" the system or what the telemetry says they actually need (e.g., "Users are copy-pasting logs into ChatGPT manually because our current dashboard is too slow").
- **Constraints**: Performance targets, security requirements, or "Strategic Underfunding" parameters (e.g., "Must run as a single-person operation using parallel agents").



## Output Contract

**Deliverable**: Structured framework/system responding to input requirements
**Format**: Strategic guide with sections and actionable components
**Length**: 2,000–5,000 words
**Core components**: 
- System overview or architecture
- Step-by-step execution protocol
- Implementation templates or worksheets
- Quick-reference guide or checklist

## Output Skeleton

```
[SYSTEM NAME]
├─ Overview / Core Principle
├─ Layer 1: [Foundational Layer Name]
│   └─ [Layer components described in general terms]
├─ Layer 2: [Process Layer Name]
│   └─ [Step 1, Step 2, Step 3... placeholders only]
├─ Layer 3: [Application/Integration]
│   └─ [How to deploy described generically]
├─ Implementation Worksheet
│   └─ [Input fields / decision points only]
└─ Quality Checklist
    └─ [Verify steps: generic criteria only]
```

**Note**: All section titles, component names, and examples are placeholders. User provides specific context; output fills structure accordingly.

## Quality Gate

Verify all v2 outputs against these checkpoints:

1. **Methodology Integrity**: All execution steps from original are preserved; no thin gaps where examples were stripped.
2. **No Fabricated Specifics**: Zero invented statistics, case studies, client names, or results presented as real.
3. **Input-Output Traceability**: Every input required maps to output components; logic is transparent.
4. **Actionability**: User can reasonably execute or adapt steps without domain expertise beyond the original intent.
5. **Tone Alignment**: Maintains expert confidence and activation stance without padding or unverifiable claims.
