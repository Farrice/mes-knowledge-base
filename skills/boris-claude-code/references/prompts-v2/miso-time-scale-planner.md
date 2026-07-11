---
name: "miso-time-scale-planner"
source_prompt: "skills/boris-claude-code/references/prompts/miso-time-scale-planner.md"
skill: "boris-claude-code"
standard: structure-pure-v2
refactored: "2026-07-11"
fidelity: "standard"
---



## Input Required
- **Project Substrate**: The current state of your codebase or product (e.g., "A CLI tool for local data analysis with 500 active users").
- **Latent Demand Signals**: Observations of "product abuse"—how users are hacking your tool to do things it wasn't built for (e.g., "Users are piping SQL queries through our terminal UI to generate genomic maps").
- **The 6-Month Delta**: Your prediction of what the next frontier model (e.g., Claude 4 or equivalent) will do natively that your current "scaffolding" handles manually.
- **Underfunding Constraint**: The specific headcount or resource limit you are intentionally imposing to force AI automation.



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
