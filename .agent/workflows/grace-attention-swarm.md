---
description: "Attention layer optimization swarm — parallel experts optimize hooks for each platform anchored in city map strategy"
---

# /grace-attention-swarm — Platform Attention Optimization

Deploy platform-specific hook experts in parallel against Grace's attention district. Each expert optimizes hooks for their platform while maintaining strategic coherence with the city map.

**Why a swarm?** Each platform has its own attention grammar. A TikTok hook is structurally different from a LinkedIn hook, which is different from a YouTube thumbnail. Asking one expert (or one brain) to optimize across all simultaneously produces generic, platform-agnostic hooks that underperform everywhere.

## Usage

```
/grace-attention-swarm [brand/topic]
/grace-attention-swarm "AI coaching for solopreneurs" --platforms "youtube,linkedin,tiktok,newsletter"
```

## Steps

### 1. Load Grace Context
Read these files:
1. `skills/grace-andrews-media-company/SKILL.md`
2. `skills/grace-andrews-media-company/genius.md`
3. `skills/grace-andrews-media-company/workflows/08-attention-capture-map.md`

Read the city map if it exists, or define the Grand Central Station and attention district inline.

### 2. Define Attention District Context

Before firing the swarm, create a shared context brief that every agent receives:

```
## BRAND CONTEXT
Brand: [Name]
Grand Central Mission: [Core editorial mission]
Attention District Goal: [What does "capturing attention" mean for this brand? Subscribers? Views? Shares?]
Target Audience: [Who are we trying to reach in the attention stage?]
Key Topics: [3-5 topics this brand owns]
Voice Register (Attention Stage): [Energy level, proof density, assertion style]
```

### 3. Deploy Parallel Swarm

// turbo
```bash
python /Users/farricecain/Google\ Antigravity/execution/parallel_swarm.py --grounded \
  --agents "seena-rez,lara-acosta,kallaway,harry-dry" \
  "[BRAND CONTEXT from Step 2]
  
  YOUR TASK: Generate 10 attention hooks for [brand] optimized for YOUR specific platform expertise.
  Each hook must:
  1. Stop the scroll / earn the click / earn the open
  2. Connect to the brand's Grand Central mission (not just random engagement bait)
  3. Create a bridge to deeper content (attention → discovery)
  4. Be specific (numbers, results, timeframes) not vague
  
  Score each hook 1-10 on: Specificity, Curiosity Gap, Proof Signal, Platform-Native Fit"
```

**Agent assignments**:
| Agent | Platform Expertise | Hook Style |
|-------|-------------------|------------|
| **Seena Rez** | TikTok / Short-form | Visual-first, trend-riding, pattern-interrupt |
| **Lara Acosta** | LinkedIn | Trapdoor posts, authority hooks, contrarian takes |
| **Kallaway** | YouTube | Curiosity gap + proof, dopamine promise titles |
| **Harry Dry** | General Copy / Social | Marketing frameworks, One-liner hooks, proven patterns |

### 4. Collect & Cross-Reference Outputs

After the swarm returns:
1. Read all agent outputs from `swarm_outputs/latest/agent_outputs/`
2. For each platform, select the top 5 hooks (scored ≥7/10)
3. Cross-reference: Do the hooks across platforms tell a coherent brand story? Or are they pulling in different directions?
4. If incoherent: revise hooks that don't align with Grand Central

### 5. Trust Bridge Audit

For each winning hook, define the next step:
```
HOOK: [The attention hook]
PLATFORM: [Platform]
WHAT HAPPENS NEXT: [Where does the person go after engaging?]
BRIDGE: [The content piece that converts attention → discovery]
```

**Quality gate**: If any hook has no bridge → it's engagement bait, not strategy. Fix or kill.

### 6. Assemble Attention Playbook

Package into a platform-organized playbook with:
- Top 5 hooks per platform (scored and annotated)
- Trust bridges for each hook
- A/B test recommendations (which hooks to test first)
- Content calendar showing when to deploy each hook

### 7. Save Output
Save to `.tmp/grace-andrews/attention-swarm-[brand-slug].md`
