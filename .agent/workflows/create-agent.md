---
description: Create an expert agent from an existing skill or directly from an extraction
---

# /create-agent

Convert a skill into an autonomous expert agent, or create an agent directly from an extraction.

## Usage

**From existing skill:**
```
/create-agent [skill-name]
```

**From extraction (creates skill first, then agent):**
```
/create-agent
```
Then provide extraction file path and expert details when prompted.

## Steps

### Option A: From Existing Skill

1. **Verify skill exists** at `skills/[skill-name]/`

2. **Derive agent name** from skill name:
   - `seena-rez-tiktok-commerce` → `seena-rez`
   - `samuel-thompson-product-launch` → `samuel-thompson`

3. **Create agent directory** at `agents/[agent-name]/`

4. **Read skill files** to understand the expert:
   - `SKILL.md` for capabilities and workflow
   - `references/genius-patterns.md` for competencies
   - `references/prompts/` for available skills

5. **Generate AGENT.md** using `agents/_framework/AGENT_TEMPLATE.md`:
   - Extract expert persona from skill content
   - List core competencies from genius patterns
   - Map available skills from prompts
   - Create decision framework from implementation
   - Define approval gates for high-stakes actions
   - Define handoff protocol for multi-agent scenarios

6. **Create memory directory** at `agents/[agent-name]/memory/`

7. **Create initial context.md** with empty template:
   ```markdown
   # [Agent Name] Memory

   ## Active Projects
   (None yet)

   ## User/Brand Context
   (To be populated as work proceeds)

   ## Learnings
   (To be populated from completed work)

   ## Past Work Reference
   (To be populated from completed work)
   ```

8. **Create symlink** from `agents/[agent-name]/skills` → `skills/[skill-name]/references/prompts`

9. **Report completion** with summary of agent capabilities

### Option B: From Extraction (No Skill Exists Yet)

1. **Run /convert-extraction first** to create the skill

2. **Then proceed with Option A** using the newly created skill

## Example

```
User: /create-agent seena-rez-tiktok-commerce

Agent: Creating expert agent from seena-rez-tiktok-commerce skill...

✅ Agent created: seena-rez

Location: agents/seena-rez/
- AGENT.md (persona, capabilities, decision framework)
- memory/context.md (empty, ready for project context)
- skills/ → skills/seena-rez-tiktok-commerce/references/prompts/

To invoke: "@seena-rez" or describe viral content / TikTok commerce work
```

## Agent Naming Convention

| Skill Name | Agent Name |
|------------|------------|
| seena-rez-tiktok-commerce | seena-rez |
| samuel-thompson-product-launch | samuel-thompson |
| [expert-name]-[domain] | [expert-name] |

## Files Reference

- **Template**: `agents/_framework/AGENT_TEMPLATE.md`
- **Orchestration**: `agents/_framework/orchestrator.md`
- **Memory Protocol**: `agents/_framework/memory-protocol.md`
