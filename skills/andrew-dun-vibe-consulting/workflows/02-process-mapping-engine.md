# Workflow 02: Process Mapping Engine

> Document exactly what happens vs. what leadership thinks happens — every click, every tab, every handoff.

## Prerequisites
- **Load**: [genius.md](../genius.md)
- **Input Required**: Discovery notes from Workflow 01, access to operators for follow-up questions
- **Dependencies**: Best after Workflow 01 discovery interviews

## Produces
1. End-to-end process maps for each core business function
2. Sub-task decomposition per role (the "assumption decomposition")
3. Time-per-step measurements
4. Bottleneck root cause identification
5. Data flow diagram showing system-to-system handoffs

---

## Step 1: Identify Core Processes to Map

```
PROCESS INVENTORY

From discovery interviews, list every process that touches revenue or costs:

| # | Process | Department | Owner | Executive Estimate | Priority |
|---|---------|-----------|-------|-------------------|----------|
| 1 | [e.g., Lead → Close] | Sales | [Name] | [X min] | [H/M/L] |
| 2 | [e.g., Onboarding] | Ops | [Name] | [X min] | [H/M/L] |
| 3 | [e.g., Invoicing] | Finance | [Name] | [X min] | [H/M/L] |
...

PRIORITY CRITERIA:
- HIGH: Touches revenue directly, involves 3+ people, done daily
- MEDIUM: Supporting process, involves 2+ people, done weekly
- LOW: Administrative, involves 1 person, done monthly
```

---

## Step 2: Decompose Each Process

For every HIGH priority process, apply the Assumption Decomposition:

```
PROCESS DECOMPOSITION: [Process Name]

What the executive said: "[Their 1-sentence description]"

ACTUAL STEPS (from operator narration):
| Step | Action | Tool/System | Time | Who | Notes |
|------|--------|------------|------|-----|-------|
| 1 | [Specific action] | [App/tool] | [X min] | [Role] | |
| 2 | [Specific action] | [App/tool] | [X min] | [Role] | |
| 3 | [Specific action] | [App/tool] | [X min] | [Role] | |
...

TOTAL ACTUAL TIME: [X min] (vs executive estimate of [Y min])
GAP: [X]x longer than leadership believed
PEOPLE INVOLVED: [X]
SYSTEM HANDOFFS: [X] (data moves between [X] different tools)

BOTTLENECKS IDENTIFIED:
- [Bottleneck 1]: [Description + root cause]
- [Bottleneck 2]: [Description + root cause]

AI SUITABILITY FILTER (all 4 must pass):
□ Structured input?
□ Rule-based decisions?
□ Predictable output?
□ Repeated often?
RESULT: [SUITABLE / PARTIAL / NOT SUITABLE]
```

---

## Step 3: Data Flow Mapping

```
DATA FLOW DIAGRAM

For each mapped process, trace where data moves:

[System A] → manual entry → [System B] → copy/paste → [System C]
     ↓                           ↓
  [Export CSV]              [Email to team]

SYSTEM INVENTORY:
| System | Purpose | Data Enters From | Data Goes To | Manual? |
|--------|---------|------------------|-------------|---------|
| [Tool] | [Use] | [Source] | [Destination] | [Y/N] |
...

FRAGMENTATION SCORE: [X] disconnected systems
MANUAL HANDOFF COUNT: [X] points where humans move data between systems
CHASSIS ASSESSMENT: [Adequate / Needs Integration / Needs Centralization]
```

---

## Step 4: Compile Master Process Map

```
MASTER PROCESS MAP — [Company Name]

PROCESS 1: [Name]
├── Steps: [X] (executive believed [Y])
├── Time per cycle: [X min] (executive believed [Y min])
├── People involved: [X]
├── Bottlenecks: [X identified]
├── AI Suitability: [Score]
└── Preliminary waste: $[X]/year

PROCESS 2: [Name]
[Same structure]
...

SUMMARY:
- Total processes mapped: [X]
- Total steps documented: [X]
- Average executive estimation gap: [X]x
- Total bottlenecks identified: [X]
- Processes suitable for AI: [X of Y]
```

---

## Output Schema

The deliverable is a **Master Process Map** document containing, per mapped process:

```
- Process Inventory table (# | Process | Department | Owner | Executive Estimate | Priority)
- Per-HIGH-priority process: Process Decomposition block
    (executive's 1-sentence description → actual step table → TOTAL ACTUAL TIME
     vs. executive estimate → GAP multiple → bottlenecks list → 4-question AI
     Suitability result: SUITABLE / PARTIAL / NOT SUITABLE)
- Data Flow Diagram + System Inventory table + Fragmentation Score + Chassis Assessment
- Master Process Map summary block (per Step 4 template) with:
    Total processes mapped, total steps documented, average executive
    estimation gap (as a multiple, e.g. "3.2x"), total bottlenecks,
    processes suitable for AI (X of Y)
```

Minimum bar: every HIGH priority process from the inventory gets a full decomposition block — partial coverage is not a complete deliverable.

## Quality Gate

- [ ] Every "one task" decomposed into actual sub-steps (minimum 4 per process)
- [ ] Time-per-step measured from operator narration (not executive estimates)
- [ ] System-to-system handoffs documented with manual/automated distinction
- [ ] AI suitability filter applied to every bottleneck (4-question test)
- [ ] Executive estimation gap calculated for each process
- [ ] Data flow shows where information moves and where it gets stuck
