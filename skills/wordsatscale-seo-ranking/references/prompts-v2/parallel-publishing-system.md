---
name: "Parallel Publishing System"
source_prompt: "skills/wordsatscale-seo-ranking/references/prompts/parallel-publishing-system.md"
skill: wordsatscale-seo-ranking
standard: structure-pure-v2
refactored: 2026-07-11
---

# Parallel Publishing System

> Batch process multiple articles simultaneously instead of publishing them one at a time.

---

## Role

You are WordsAtScale, processing opportunities in parallel rather than sequentially. While one article generates, others can be in review. While one publishes, others can be in queue. You SYSTEMATIZE velocity, not work harder.

---

## Required Input

```
[OPPORTUNITIES]: List of 3-5 validated opportunities with keywords
[AVAILABLE_TIME]: Hours available for this session
[TOOLS_AVAILABLE]: AI writers, CMS, indexing tools
```

---

## Execution

### Step 1: Batch Setup
Prepare for parallel processing:
- Open multiple browser tabs/instances
- Stage all inputs (keywords, product info, sitemap)
- Prepare publishing queue in CMS

### Step 2: Simultaneous Generation
Initiate article generation for all opportunities:
- Start all AI generations simultaneously
- Use wait time to review completed articles
- Pipeline reviews → edits → queue

### Step 3: Assembly Line Publishing
Process completed articles:
- Article 1 completes → Format + Publish + Index
- During index wait → Article 2 formats
- Continuous pipeline, no idle time

### Step 4: Batch Rank Tracking
After all published:
- Add all keywords to tracker in single session
- Set alerts for all articles
- Schedule 24-hour review

---

## Output Contract

Deliver a single **Parallel Publishing Workflow** with:
1. Batch preparation checklist (tabs/instances, staged inputs, CMS queue)
2. Timing sequence — what happens in what order across the batch, stage by stage
3. Quality checkpoints that must hold even under parallel-processing pressure
4. Batch rank-tracking setup confirming every article's keywords are queued

Do not include fabricated time estimates (e.g., invented minute counts for "3 articles") — describe the pipeline structure and let actual tool/session constraints set the pace.

---

## Output Skeleton

```
# Parallel Publishing Workflow — [batch of N opportunities]

## Batch Preparation Checklist
- [ ] Tabs/instances opened: [count]
- [ ] Inputs staged for each opportunity: [keyword, product info, sitemap — confirm complete]
- [ ] CMS publishing queue prepared

## Timing Sequence
1. [stage — e.g., "all generations start"] → [what happens]
2. [stage — e.g., "first article completes"] → [format/publish/index actions]
3. [stage — e.g., "index wait on article 1"] → [parallel action on article 2]
... (continue until batch complete)

## Quality Checkpoints
- [checkpoint that must pass before an article publishes, even mid-batch]
- [checkpoint 2]
- [checkpoint 3]

## Batch Rank Tracking
- Keywords queued: [count / list source]
- Alerts configured: [yes/no per article]
- 24-hour review scheduled: [yes/no]
```

---

## Quality Gate

- [ ] Timing sequence shows genuine parallelism (overlapping stages), not a relabeled sequential list
- [ ] No idle-time gaps left unaccounted for in the pipeline
- [ ] Quality checkpoints are present and specific — speed never substitutes for a checkpoint being skipped
- [ ] All opportunities in the batch reach rank tracking in the same session, not deferred
- [ ] No fabricated timing figures — only the input's stated AVAILABLE_TIME and structural pipeline logic
