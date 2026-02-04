# Genius Patterns: Swarm Commander

These patterns are synthesized from Boris, Lance & Yichao, and Mark Kashef—the three experts whose methodologies form the Swarm Commander architecture.

---

## From Boris: Multi-Instance Orchestration

### 1. Work Order Minimalism
**Behavior**: Generates the smallest possible context for each agent to execute successfully.
**Execution**: Work orders contain only: objective, constraints, output schema, and critical context. No conversation history, no redundant background.

### 2. Assignment Briefing Pattern
**Behavior**: Treats each agent as an employee receiving a job brief, not a conversationalist.
**Execution**: Structured handoff with clear success criteria before execution begins.

### 3. Role-Based Instance Typing
**Behavior**: Assigns explicit instance roles (Primary, Research, Review, Specialist).
**Execution**: Each agent knows its archetype and adjusts confidence/depth accordingly.

### 4. Meta-Instance Orchestration
**Behavior**: Uses a dedicated instance to manage other instances.
**Execution**: Swarm Commander is the "meta" layer—it doesn't do the work, it coordinates those who do.

---

## From Lance & Yichao: Context Engineering

### 5. Agent-as-Tool Isolation
**Behavior**: Wraps complex operations into single function calls with structured outputs.
**Execution**: Each agent execution is a tool call that returns schema-compliant output; messy intermediate state never pollutes the main context.

### 6. File System as Coordination Layer
**Behavior**: Uses files instead of messages for inter-agent communication.
**Execution**: Agents write to `agent_outputs/[name].md`. Synthesizer reads files, not chat history.

### 7. Schema-as-Contract
**Behavior**: Pre-defines exact output structure before spawning sub-agents.
**Execution**: Every work order includes OUTPUT_SCHEMA with required fields. Non-compliant outputs are rejected.

### 8. Compaction Before Synthesis
**Behavior**: Compacts agent outputs to essential elements before aggregation.
**Execution**: Each output file has COMPACT and FULL sections. Synthesis uses COMPACT; FULL available for deep-dives.

### 9. Reversibility Principle
**Behavior**: Every condensation preserves recovery path.
**Execution**: Compact representations include file paths, agent IDs, and timestamps for full reconstruction.

---

## From Mark Kashef: Council Orchestration

### 10. Intelligent Agent Selection
**Behavior**: Matches task requirements to expert capabilities, not just names.
**Execution**: Uses DOMAIN_REGISTRY.md to identify which experts have genuine authority in required areas.

### 11. Tension Design
**Behavior**: Deliberately selects agents who will disagree productively.
**Execution**: For complex decisions, includes at least one contrarian/skeptic agent.

### 12. Behavioral Mandates
**Behavior**: Defines what agents MUST DO before concluding, not just personality.
**Execution**: Each work order includes MANDATE: "Before completing, you MUST [specific action]."

### 13. Provenance Tracking
**Behavior**: Every conclusion traces to which expert generated it.
**Execution**: Synthesis includes attribution: "Cardinal Mason emphasized...", "Seena Rez recommends..."

### 14. Minority Report Preservation
**Behavior**: Dissenting views are captured, not suppressed.
**Execution**: Final synthesis includes MINORITY_POSITIONS section with full reasoning.

---

## Swarm-Specific Patterns

### 15. Dependency Graph Mapping
**Behavior**: Identifies which agents can run "in parallel" vs which need sequential input.
**Execution**: Phase 1 produces dependency graph before execution begins.

### 16. Batch Optimization
**Behavior**: Groups independent agents into execution batches.
**Execution**: If 5 agents have no dependencies, they execute as one conceptual batch.

### 17. Progressive Synthesis
**Behavior**: Synthesizes as batches complete, not just at the end.
**Execution**: Sequential batches feed into rolling synthesis for faster time-to-first-insight.

### 18. Swarm Scaling Intelligence
**Behavior**: Adjusts agent count based on task complexity, not arbitrary.
**Execution**: Squad (3-5) for focused, Army (26-50) for exhaustive—never over-engineer.
