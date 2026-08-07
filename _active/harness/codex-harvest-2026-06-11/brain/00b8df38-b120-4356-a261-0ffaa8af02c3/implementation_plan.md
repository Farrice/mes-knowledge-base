# Research Findings & Implementation Plan: Kimi 2.6 MoE Orchestration vs. Antigravity

This document outlines the findings of our deep research into Moonshot AI's **Kimi 2.6** model and its **Agent Swarm** orchestration layer. Based on this research, I have identified architectural gaps within the Antigravity framework and proposed concrete implementation steps to integrate Kimi's innovations into your system.

## Research Findings: Kimi 2.6 Architecture

The Kimi 2.6 system shifts orchestration from an external wrapper to a native model property using an advanced Mixture of Experts (MoE) architecture. 

**Core Kimi 2.6 Capabilities:**
1. **MoE Scale:** 1 Trillion total parameters, activating only 32 Billion per token. It routes to 8 out of 384 specialized experts (plus 1 shared expert). Instead of routing strictly for language prediction, its MoE router identifies task types and routes to "agent profiles" implicitly.
2. **Horizontal Swarm Parallelization:** The "Agent Swarm" seamlessly scales up to **300 sub-agents** coordinating across **4,000 continuous steps** (e.g., 13-hour autonomous coding loops or generating 100 job-tailored resumes in parallel).
3. **Dynamic Task Decompositon:** Instead of static workflows, the orchestrator generates a live **Task Graph (DAG)** on the fly for complex requests, breaking them into parallel and sequential nodes.
4. **Automatic Failure Detection & Reassignment:** The orchestrator proactively acts as a watchdog. If a sub-agent stalls or provides bad output, it instantly kills the agent and reassigns the node without waiting for the entire chain to fail.
5. **Claw Groups (Heterogeneous Agents):** A BYOA (Bring Your Own Agent) feature that allows Kimi to coordinate external agents across any device (local laptop, mobile edge inference) into the global task graph.

---

## Architectural Gaps in Antigravity

Comparing Kimi 2.6 to the **Antigravity Agentic Framework** (specifically `expert_router.py`, `tool_router.py`, and your `DOMAIN_REGISTRY.md`), we find the following gaps:

1. **Static Lanes vs. Dynamic Graphs:** Antigravity relies heavily on static "Swim Lanes" and explicit handoff protocols (`/workflows`). Kimi treats complex queries as a live graph calculation.
2. **Sequential vs. Mass Parallel Validation:** Antigravity's "Validation Stack" (Sabri Suby -> Dai Media -> Samuel Thompson -> Cardinal Mason) acts sequentially. Kimi can spawn 300 instances simultaneously for validation and reduce latency.
3. **Reactive vs. Proactive Failure:** Your `chain_runner.py` uses the 1-10 scoring system to abort at the `FINALIZE` step if an expert scores < 6. Kimi detects failures *during* the execution of parallel arms and re-spawns them inline.
4. **Closed vs. Open Topology:** Antigravity is a strictly local Python/Markdown environment. Kimi's "Claw Groups" concept permits off-system orchestration.

---

## User Review Required

> [!WARNING]
> Please review the proposed changes below. Upgrading `/swarm` to use dynamic task graphs will fundamentally alter how Antigravity coordinates multi-expert strategies. 
> 
> **Decision Point:** Should we prioritize upgrading the **Task Graph Generator (Swarm)**, the **Proactive Watchdog (Execution)**, or the **Memory Management MoE Simulation** first?

---

## Proposed Changes (Antigravity Enhancements)

Below is the implementation plan to integrate Kimi 2.6-style MoE Swarm logic into Antigravity's Python execution layer.

### 1. Dynamic Task Graph (DAG) for `/swarm`

Summary: Overhaul the `/swarm` feature and `expert_router.py` to generate a directed acyclic graph mapping out sub-steps and parallel dependencies before execution.

#### [MODIFY] `execution/expert_router.py`
- Add a new argument `graph "query"` to dynamically decompose a user request into independent subtasks.
- Map the subtasks to specific expert combinations from `DOMAIN_REGISTRY.md`.
- Ensure output is a DAG configuration (e.g., JSON structure of tasks and dependencies).

#### [MODIFY] `execution/chain_runner.py`
- Implement DAG concurrency using `asyncio.gather` for parallelized execution where branch dependencies allow, transitioning from sequential chains to mass-parallel swarms.

### 2. Inline Proactive Failure Watchdog

Summary: Move quality assurance from the end of the ` chain_runner` loop to be an active, concurrent watchdog for each swarm node.

#### [MODIFY] `execution/chain_runner.py`
- Introduce a watchdog process that evaluates sub-agent output streams.
- If a sub-task violates the `qa/mandates.md` (e.g., using "slop" words like "delve", or generating phantom research), throw an immediate `AgentStallException` and automatically retry on a fresh thread to mimic Kimi 2.6's failure reallocation.

### 3. Local "Claw Group" Extensibility

Summary: Allow Antigravity to treat external tools/MCPs or other local devices as "Virtual Experts" inside the `DOMAIN_REGISTRY.md`.

#### [MODIFY] `execution/expert_router.py`
- Extend the routing payload to map external APIs (like Notion or existing MCP servers) not just to tools, but as autonomous MoE nodes in the swarm graph.

### 4. MoE-Style "Selective Context" Routing

Summary: Align context delivery with Kimi's "activate 8 out of 384 experts" strategy by hyper-optimizing memory allocation.

#### [MODIFY] `execution/context_retriever.py`
- Rather than cascading T1 -> T2 -> T3, build a true "Sparse Gating" function. For a specific task node, the retriever dynamically scores all 96 `SKILL.md` chunks and injects *only* the top $K$ relevant expert chunks into that swarm node's memory context.

---

## Open Questions

1. **Token Budgets:** Scaling parallel swarms significantly increases LLM API calls. Should I implement hard token caps on dynamic swarm task graphs?
2. **Current Swarm Flow:** Does your current `/swarm` command run via a single Python script or does it rely on sequential Claude system prompt loading?

## Verification Plan

### Automated Tests
- Run `python3 execution/expert_router.py graph "Launch a high-ticket ghostwriting service"` and verify that the system successfully returns a multi-node parallel workflow map rather than a single expert.

### Manual Verification
- Deploy a simulated `/swarm` and forcefully fail one node to ensure the new `chain_runner.py` watchdog instantly reassigns and retries the specific node without killing the swarm process.
