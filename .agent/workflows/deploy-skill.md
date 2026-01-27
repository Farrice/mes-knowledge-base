---
description: Deploy any skill's prompts to execute a specific task
---

# /deploy-skill

Use this workflow to leverage any skill in your library for a specific task.

## Usage

```
/deploy-skill [skill-name] [task-description]
```

**Examples:**
- `/deploy-skill jeremy-miner Create a pre-frame for my webinar on AI automation`
- `/deploy-skill dai-media Build a consumer posture for remote team managers`
- `/deploy-skill mitch-albom Write a story about a founder's comeback`

---

## Workflow Steps

### 1. Identify the Skill
// turbo
- List available skills in `/Users/farricecain/Google Antigravity/skills/`
- Confirm the requested skill exists
- If skill name is ambiguous, show options and ask for clarification

### 2. Load Skill Context
// turbo
- Read the skill's `SKILL.md` to understand capabilities
- Review the workflow decision tree (if present)
- Identify which prompt(s) best match the user's task

### 3. Select Optimal Prompt
- Based on the task description, select the most appropriate prompt
- If multiple prompts could work, briefly explain options and recommend one
- If user's task doesn't match any prompt, explain what the skill CAN do

### 4. Gather Required Inputs
- Read the selected prompt file to understand required inputs
- Check if user provided all needed inputs in their task description
- If inputs are missing, ask for them concisely (batch all questions)

### 5. Execute the Prompt
// turbo
- Run the prompt with the user's inputs
- Follow the prompt's execution protocol exactly
- Generate the full deliverable as specified in the prompt

### 6. Deliver Output
- Present the output in the format specified by the prompt
- Offer to refine, iterate, or apply additional prompts if relevant

---

## Available Skills

The agent will dynamically list skills, but common ones include:
- `jeremy-miner-identity-persuasion` — Sales psychology, identity framing, objection prevention
- `dai-media` — Consumer posture, viral engineering, brand strategy
- `mitch-albom` — Storytelling, narrative architecture, theme-driven content
- `samuel-thompson` — AI product launches, shadow markets, info products
- `seena-rez` — TikTok commerce, short-form content, viral hooks

---

## Notes

- Skills are located in: `/Users/farricecain/Google Antigravity/skills/`
- Each skill contains a `SKILL.md` with overview and prompt library
- Prompts are typically in `references/prompts/` within each skill
- If a skill hasn't been created yet, suggest using `/convert-extraction` first
