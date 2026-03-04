# Parallelism Cheat Sheet

> Quick reference for choosing the right parallel execution pattern. Full protocol: `directives/sub_agent_protocol.md`

---

## Which Command Do I Use?

| I want to... | Command | Speed vs Sequential |
|--------------|---------|-------------------|
| Produce content for every platform at once | `/launch-day` | ~5x faster |
| Repurpose one piece into 11 derivatives | `/atomize` | ~4x faster |
| Study viral content and create my version | `/watch-and-remix` | ~3x faster |
| Research a business decision from 3 angles | `/research-sprint` | ~3x faster |
| Design a complete offer + funnel | `/design-offer` | ~3x faster |
| Get expert opinions without anchoring bias | `/roundtable` | ~2x faster (Round 1) |
| Plan my week in 30 minutes | `/weekly-pulse` | ~3x faster |
| 5-10+ expert perspectives with real data | `/parallel-swarm --research` | ~$0.30-0.50 |
| Batch-extract from multiple sources | `/parallel-extract` | ~3x faster |
| 5-10+ expert perspectives cheaply | `/parallel-swarm` | ~$0.15 total |

---

## The 3 Tiers

| Tier | What | When | Max Agents |
|------|------|------|-----------|
| **1: Parallel Task Calls** | Multiple Task tools in one message, agents work independently | Agents don't need each other's output | 5 |
| **2: Agent Teams** | TeamCreate + SendMessage, agents can talk to each other | Agent B needs Agent A's output, or a reviewer/synthesizer coordinates | 5-6 |
| **3: Gemini Swarm** | `execution/parallel_swarm.py`, cheap API calls | 5+ experts needed, cost-sensitive, no tool access needed | 10+ |

---

## Decision Flowchart

```
Can I split this into independent pieces?
├── NO → Run sequentially (single expert or embodiment)
└── YES → Do agents need to talk to each other?
    ├── YES → Agent Teams (Tier 2): /launch-day, /research-sprint
    └── NO → How many agents?
        ├── 2-5 → Parallel Task Calls (Tier 1): /atomize, /roundtable, /parallel-*
        └── 6+ → Gemini Swarm (Tier 3): /swarm --gemini
```

---

## Rules

1. **Max 5 parallel Task calls** — more than 5 = resource contention
2. **Each agent writes to its own file** — no shared state
3. **Always synthesize** — parallel outputs need a collection step, don't dump raw
4. **Multiple Task calls in one message** = parallel. One per message = sequential.
5. **If one agent fails, others continue** — report the gap, don't retry the whole batch

---

*Reference: `directives/sub_agent_protocol.md` for full protocol, templates, and anti-patterns.*
