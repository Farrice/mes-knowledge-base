# Mark Kashef Silver Platter Agentic OS - Genius Patterns

## Source Thesis

An agentic OS fails when the agent spends most of the session retrieving and organizing data instead of reasoning over clean inputs. The leverage move is to do the hard back-of-house work first: map data sources, pre-aggregate the important numbers, create summary tables, and let agents analyze clean context.

## Patterns

### 1. The 80 Before The 20

The hidden 80 percent is data prep: exports, APIs, conversion hooks, summary files, rules, and audit logs. Agents are the visible 20 percent. Do not build a chief-of-staff agent until the briefs it reads exist.

### 2. Pantry -> Prep -> Plate

- Pantry: raw tools and data sources.
- Prep: silver platters, meaning clean recurring summary briefs.
- Plate: human-facing outputs and decisions.

This structure keeps the operator from confusing "having tools" with "having an operating system."

### 3. Summary Tables Beat Context Drag

When an agent must pull raw data for 80 percent of the session, the useful reasoning happens late, under pressure, and with higher hallucination risk. Deterministic prep should create compact tables first, then hand those tables to agents.

### 4. Orchestrator Above Specialists

The operator should not manage a flat row of specialists. A chief-of-staff or orchestrator receives the human question, chooses the specialist, and passes only the needed context. This reduces cold-start mismatch and agent overlap.

### 5. Hooks Are The Unsexy Multipliers

SessionStart conversion hooks, PostToolUse audit hooks, Stop approval nudges, and post-compaction context hooks are not flashy, but they make the OS reliable. Treat hooks as trust and continuity infrastructure, not decoration.

### 6. Regulated Data Comes First

For law, healthcare, wealth, and other sensitive domains, model containment and data scoping precede automation. Bedrock or equivalent approved deployment, path-scoped rules, audit logs, and approval gates are prerequisites, not enhancements.

### 7. Skills Are Infinite Games

A skill is started, used, corrected, and improved. The skill system should capture wrong turns, update critical paths, and make repeatable routes easier over time.

## Anti-Patterns

- Building a generic "agentic OS" agent before mapping the data.
- Asking operators schema-shaped questions they cannot answer.
- Producing a beautiful dashboard without an executable build order.
- Treating a regulated workflow as if "be careful" is enough.
- Creating another Mark Kashef expert instead of extending the existing Mark orchestration family.

