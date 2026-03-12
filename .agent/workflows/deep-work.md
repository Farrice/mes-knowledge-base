# Deep Work — Full Chain Strategic Session

> **Invocation**: `/deep-work` | `@deep-work` | "run deep-work" | "deep work session"
> **Purpose**: Produce high-stakes content or deliverables with the full chain, multi-expert loading, writers' room, and complete quality gate.
> **When**: Profile copy, launch posts, offer pages, client deliverables, strategic content that needs to be exceptional.

---

## How It Works

This runs the full 7-step chain from CLAUDE.md. It's the system at maximum power — multiple experts, writers' room treatment, scored quality gate, complete logging. Use this for pieces where quality matters more than speed.

---

## Step 1: Score Intent (Chain Step 1)

Score the request 1-5 on the DICE dimensions:
+1 Deliverable | +1 Audience | +1 Context/constraints | +1 End state | +1 Specific language

If Score ≤ 3 → Sharpen with DICE (Chain Step 2). One round max.

---

## Step 2: Route to Experts (Chain Step 3)

Match domain → experts using `directives/intent-pipeline.md` Stage 3.
Check `FARRICE.md` proactive deployment table for auto-deploy signals.
Multi-domain? Check `directives/expert_auto_routing.md` for ensemble patterns.

Load 2-3 experts minimum. For strategic content, load 3.

---

## Step 3: Load via Context Engine (Chain Step 4)

Tier 2 minimum for deep work: SKILL.md + genius.md + relevant workflow.
Content creation gate: minimum 2 expert skill files loaded per `directives/content_creation_gate.md`.

Always load: `FARRICE.md` for voice reference.

---

## Step 4: Produce (Chain Step 5)

For content ≥ 500 chars: **Run writers' room as default** (`.agent/workflows/writers-room.md`).

Apply loaded expert frameworks — their thinking, not their terminology.
Enforce `directives/quality_assurance.md` anti-patterns during production.

Generate 3 variants when appropriate (especially for LinkedIn posts, profile copy, strategic pieces). Each variant leans into a different strength. Include a mixing guide.

---

## Step 5: Quality Gate (Chain Step 6)

Score 1-10 on all 3 dimensions:
1. **Intent Alignment** — Does the output match what was actually asked for?
2. **Expert Standard** — Would the real expert behind this skill approve? ("Would [expert name] be proud of this?")
3. **Adversarial Resilience** — Would this hold up under domain scrutiny?

Composite < 7 OR any dimension < 6 → retry weakest section (1 retry max).

---

## Step 6: Auto-Log (Chain Step 7)

```bash
python execution/log_performance.py log "[Deliverable description]" \
    --skill [primary-skill] \
    --agent [primary-agent] \
    --workflow [workflow-used] \
    --type [Content|Strategy|Client Work|Creative] \
    --quality [composite 1-10] \
    --intent [1-10] \
    --expert [1-10] \
    --adversarial [1-10] \
    --status [Keep|Needs Improvement] \
    --notes "[What worked, what didn't, Farrice feedback]"
```

**The AI proposes the scores. Farrice confirms or adjusts.**

---

## When to Use Deep Work vs. Other Workflows

| Use `/deep-work` for | Use `/ship` instead | Use `/content-sprint` instead |
|----------------------|--------------------|-----------------------------|
| Profile/About sections | Daily LinkedIn posts | Standard content with research phase |
| Launch posts (transition, arc chapters) | Quick takes, engagement replies | Serial narrative chapters |
| Offer pages, sales copy | Repurposed content | Topic-driven content with ICP research |
| Client deliverables | Comments, DMs | Full content pipeline execution |
| Strategic positioning pieces | Anything you'd normally overthink | — |
