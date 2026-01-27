# 🧭 Antigravity Workspace Navigator

> Quick reference for finding everything in your AI workspace.

---

## 🔍 Quick Lookup Table

| Looking for... | Go to... | Example |
|----------------|----------|---------|
| Past research & insights | `~/.gemini/antigravity/knowledge/` | Consumer postures, expert methodologies |
| What we built in a conversation | `~/.gemini/antigravity/brain/<id>/` | Plans, walkthroughs, task lists |
| Expert prompt packs | `~/Google Antigravity/skills/` | Jeremy Miner, Cardinal Mason prompts |
| Autonomous expert agents | `~/Google Antigravity/agents/` | Agent personas with memory |
| How-to instructions | `~/Google Antigravity/directives/` | SOPs for recurring tasks |
| Automation scripts | `~/Google Antigravity/execution/` | Python tools for execution |
| Workflow commands | `~/Google Antigravity/.agent/workflows/` | /council, /convert-extraction, etc. |

---

## 📚 Knowledge Items (Your Second Brain)

**Path:** `~/.gemini/antigravity/knowledge/`

This is where **distilled expertise** lives. Each folder contains:
- `metadata.json` → Summary, timestamps, references
- `artifacts/` → The actual content files

### Current Knowledge Items

| Category | Knowledge Items |
|----------|----------------|
| **Expert Systems** | Cardinal Mason, Jeremy Miner, Samuel Thompson, Dai Media, Lulu Cheng Meservey, Andrew Wilkinson, Mark Kashef, Heath Brothers, Dan Wang, Oscar Höglund, Nate B Jones, Kittl, Erica Mallett, Darrel Wilson, Futurepedia, Manus.ai, Alex Copper |
| **Frameworks** | Antigravity Agentic Framework, Experts Index |
| **Research** | Multi-Passionate Entrepreneurs Niche |

### Quick Access Commands

```bash
# List all knowledge items
ls ~/.gemini/antigravity/knowledge/

# Read a specific KI overview
cat ~/.gemini/antigravity/knowledge/antigravity_expert_jeremy_miner_persuasion/artifacts/overview.md

# Find all prompts across KIs
find ~/.gemini/antigravity/knowledge -name "*.md" -path "*/prompts/*"
```

---

## 🛠️ Skills Library

**Path:** `~/Google Antigravity/skills/`

Production-ready prompt packs with:
- `SKILL.md` → Overview & workflow
- `references/genius-patterns.md` → Expert patterns
- `references/prompts/` → Individual prompts

### Deployed Skills

| Skill | Domain |
|-------|--------|
| `andrew-wilkinson-ai-entrepreneurship` | Vibe coding, $30K products |
| `cardinal-mason-ai-copywriting` | Conversion copy, sales pages |
| `dai-media-consumer-posture` | Consumer psychology |
| `heath-brothers-messaging` | Made to Stick, SUCCESs |
| `jeremy-miner-identity-persuasion` | Sales, objection handling |
| `jim-oshaughnessy-philosopher-financier` | Strategic synthesis |
| `lulu-cheng-meservey-communications` | PR, founder narrative |
| `mark-kashef-ai-councils` | Multi-agent orchestration |
| `mitch-albom-writing-mastery` | Premium writing, storytelling |
| `samuel-thompson-product-launch` | Info products, shadow markets |
| `seena-rez-tiktok-commerce` | Viral hooks, TikTok |

---

## 🤖 Expert Agents

**Path:** `~/Google Antigravity/agents/`

Autonomous personas with persistent memory:
- `AGENT.md` → Persona definition & capabilities
- `memory/context.md` → Persistent project context

### How to Invoke

Mention by name or use their domain:
- `@cardinal-mason` or "write sales copy"
- `@jeremy-miner` or "handle objections"
- `@revenue-council` for multi-expert councils

---

## 📋 Workflow Commands

**Path:** `~/Google Antigravity/.agent/workflows/`

| Command | Purpose |
|---------|---------|
| `/convert-extraction` | Turn MES 3.0 extraction → skill |
| `/create-agent` | Build autonomous expert agent |
| `/council` | Spin up AI council for decisions |
| `/deploy-skill` | Execute specific skill prompts |
| `/research-topic` | Deep research with deliverable |

---

## 🗂️ Conversation Artifacts

**Path:** `~/.gemini/antigravity/brain/<conversation-id>/`

Each conversation can produce:
- `task.md` → Checklist of work items
- `implementation_plan.md` → Technical approach
- `walkthrough.md` → Summary of completed work

### Find Recent Conversations

```bash
# List recent conversation folders (sorted by modification)
ls -lt ~/.gemini/antigravity/brain/ | head -10
```

---

## 🔎 Universal Search Commands

```bash
# Find any file by name
find ~/Google\ Antigravity -name "*keyword*"

# Search inside files for content
grep -r "search term" ~/Google\ Antigravity --include="*.md"

# Find all prompts
find ~/Google\ Antigravity/skills -name "*.md" -path "*/prompts/*"
```

---

## 💡 Pro Tips

1. **Start with Knowledge Items** → They're indexed and summarized
2. **Use Skills for execution** → Prompts are ready to deploy
3. **Check Agents for personas** → When you need sustained expert voice
4. **Workflows automate patterns** → Use `/` commands for recurring tasks

---

*Last updated: January 24, 2026*
