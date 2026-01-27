# Meta-Prompt Synthesizer

Combine expert framework + context into optimal execution prompt.

## Role

You are synthesizing all inputs into a master prompt that AI will use to produce expert-level, personalized output.

## Required Input

- **[EXPERT_ANCHOR]**: Extracted framework from Step 1
- **[CONTEXT_FILE]**: Compiled context from Step 2
- **[DESIRED_OUTPUT]**: What you want the final AI to produce

## RICECO Framework

Structure the synthesized prompt using:
- **R**ole: Who the AI should be
- **I**nstruction: What it should do  
- **C**ontext: Relevant background (from context file)
- **E**xamples: Sample outputs if helpful
- **C**onstraints: What to avoid
- **O**utput: Exact format wanted

## Prompt Template

```
<expert_anchor>
[Paste extracted framework here]
</expert_anchor>

<context_file>
[Paste compiled context here]
</context_file>

Synthesize these blocks into a single master execution prompt using the RICECO framework (Role, Instruction, Context, Examples, Constraints, Output).

Do not execute the plan yet. 

Simply output the final prompt for me to use in a clean session.
```

## Output

Complete master prompt ready for deployment in fresh chat session.

## Key Insight

"AI models are trained on all the best prompting techniques, so they're usually better at writing instructions for themselves than we are."
