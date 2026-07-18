---
name: Transistory Install
command: /mcclain-transistory-install
expert: Corey McClain
category: Practitioner
description: Quick in-prompt persona installation for rapid testing and one-off tasks
inputs: Task description, desired output quality direction
outputs: In-prompt persona + task execution in a single message
---

# Transistory Install

Install a persona directly in a prompt for one-off use. Disposable, fast, no setup. The transistory method is best for testing whether a persona approach will improve output quality for a specific task type before committing to a full steady-state build. Corey's freestyle example proved that even a 60-second improvised backstory outperforms vanilla prompts.

## Workflow

### Step 1 — Task Clarity

Before writing the persona, be precise about the task:
- What exactly does the agent need to produce?
- What does "good" look like for this output?
- Who's the audience?
- What's the quality gap between what vanilla gives you and what you actually need?

### Step 2 — Freestyle Persona

In the same prompt as your task, add a persona section. Write it conversationally — don't over-engineer. Cover:

1. **Who they are**: Name, age, role, location (2-3 sentences)
2. **How they got here**: Quick backstory — struggles, achievements, formation (3-5 sentences)
3. **Messy details**: Daily life, habits, relationships, small anxieties (3-5 sentences)
4. **What they value**: 1-2 worldview beliefs relevant to the task quality you want

**Template** (adapt freely):

```
You are [Name], a [age]-year-old [craft/role] based in [location]. You [origin — where you came from, what went wrong, how you found your way]. You've worked at [career progression — specific, not generic]. Outside of work, you [3-4 daily life details — specific and mundane]. Your [family detail — a relationship that creates mild tension]. You believe [1-2 convictions about your craft]. [Current life situation — something unresolved].

Now, [TASK DESCRIPTION].
```

### Step 3 — Execute and Evaluate

Run the prompt. Then evaluate:
- Is the output noticeably different from what vanilla would produce?
- Is it more distinctive, opinionated, or textured?
- Would you be satisfied deploying this output as-is?

### Step 4 — Promote or Discard

**If the output is strong**: Save the persona text. Refine it. Move it to a markdown file. Promote to steady-state via `/mcclain-steady-state-install`.

**If the output is mediocre**: Try a different persona — different origin, different worldview, different messy details. The persona-quality gap depends heavily on the specifics.

**If the output is the same as vanilla**: The task may not benefit from persona installation (utility tasks, data processing, etc.). Or the persona is too thin — add more contradictions and messy details.

---

## Output Schema

A single **in-prompt persona block**, following the Step 2 template exactly (`You are [Name], a [age]-year-old [craft/role]...`), immediately followed by the task instruction in the same message. Disposable by design — not saved as a file unless the Step 4 decision is "promote," in which case it becomes the input to `/mcclain-steady-state-install`.

## Quality Gate

- [ ] Persona was written in 2-5 minutes (if it takes longer, you're over-engineering)
- [ ] Persona includes at least 3 messy details with zero task relevance
- [ ] Output was compared against vanilla (even mentally)
- [ ] Decision was made: promote, iterate, or discard
