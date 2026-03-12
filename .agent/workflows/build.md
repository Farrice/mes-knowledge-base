# Build — System Improvement Session

> **Invocation**: `/build` | `@build` | "run build" | "build session"
> **Purpose**: Extractions, agent creation, skill building, workflow development, system architecture.
> **When**: You want to add capability to the system — new agents, skills, workflows, or infrastructure.

---

## How It Works

Full access to everything. Extractions, skill conversion, agent creation, architecture changes. No restrictions. Auto-logged at session end.

---

## Step 1: What Are We Building?

Identify the deliverable:

| Building... | Start With |
|------------|-----------|
| New agent extraction | `/extract` workflow |
| New skill from extraction | `execution/skill_converter.py` or manual |
| Workflow creation | Template from existing `.agent/workflows/` |
| System architecture | Read `directives/` for current protocols |
| Database/integration | Check `execution/` for existing scripts |

---

## Step 2: Check for Existing Coverage

**Anti-Hoarding Protocol** (from FARRICE.md):
- Before building anything new, check if a skill already covers this domain
- Search `SKILL_INDEX.md` and `AGENT_INDEX.md`
- Search `DOMAIN_REGISTRY.md` for swim lane coverage
- If coverage exists, enhance rather than duplicate

---

## Step 3: Build

Execute the build task. Use existing patterns:
- Agents follow `agents/_framework/AGENT_TEMPLATE.md`
- Skills follow completion engine format: `SKILL.md` + `genius.md` + `workflows/`
- Register in `SKILL_INDEX.md`, `AGENT_INDEX.md`, `SLASH_COMMANDS.md`
- Run `python execution/verify_system.py` after structural changes

---

## Step 4: Auto-Log

At session end, log the build output:

```bash
python execution/log_performance.py log "[What was built]" \
    --skill [relevant-skill-or-system] \
    --type System \
    --quality [1-10] \
    --intent [1-10] \
    --expert [1-10] \
    --adversarial [1-10] \
    --status Keep \
    --notes "[What was built, why, what it enables]"
```

---

## Guardrail

If you find yourself in a build session when you came to ship content — catch it. That's the 90% pattern. The system is good enough. Go ship.
