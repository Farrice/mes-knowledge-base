# Tool Router Agent Blueprint

> Design a dynamic tool selection architecture that loads only task-relevant tool definitions into the agent's context window. Eliminates prompt bloat from unused tool schemas.

## Prerequisites
- Inventory of all available tools/MCP servers with schemas
- Embedding model access (or simple TF-IDF as MVP)
- Understanding of typical task distribution (what tools get used most)

## Steps

### Step 1 — Tool Inventory
Catalog every available tool:

```
Tool Name          | Source        | Description (1-line)       | Avg Monthly Use | Schema Size (tokens)
create_file        | Core         | Create new files           | High            | ~150
run_command        | Core         | Execute terminal commands  | High            | ~200
browser_subagent   | Core         | Browser automation tasks   | Medium          | ~300
notion_search      | Notion MCP   | Search Notion by title     | Medium          | ~200
notion_create_page | Notion MCP   | Create new Notion page     | Low             | ~250
firebase_deploy    | Firebase MCP | Deploy to Firebase         | Low             | ~200
...
```

Calculate: total tool schema tokens if all loaded simultaneously.
This is your "before" baseline.

### Step 2 — Tool Clustering
Group tools by functional domain:

- **File Operations**: create_file, view_file, replace_file, multi_replace, write_to_file
- **Terminal**: run_command, command_status, send_command_input
- **Browser**: browser_subagent
- **Search**: search_web, grep_search, read_url_content
- **Notion**: All notion tools (search, create, query, update, etc.)
- **Image**: generate_image
- **Research**: perplexity_ask
- **Cloud**: firebase, cloudrun tools
- **Design**: pencil tools

### Step 3 — Design the Selection Architecture

**Option A — Rule-Based Router (MVP, deploy in hours)**
```python
TOOL_CLUSTERS = {
    "write_code": ["file_ops", "terminal", "search"],
    "research": ["search", "research", "browser"],
    "notion_work": ["notion", "file_ops"],
    "design": ["design", "image", "browser"],
    "deploy": ["cloud", "terminal", "file_ops"],
    "content": ["file_ops", "search", "image"],
}

def select_tools(task_intent: str) -> list[str]:
    """Classify task intent → return relevant tool clusters."""
    # Keyword matching as MVP
    # Later: embed task intent and match against cluster descriptions
    ...
```

**Option B — Semantic Router (production, deploy in days)**
```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# Pre-computed tool embeddings
tool_embeddings = {
    tool_name: model.encode(tool_description)
    for tool_name, tool_description in tool_catalog.items()
}

def select_tools(task_intent: str, top_k: int = 5) -> list[str]:
    """Embed task intent, find most similar tool descriptions."""
    task_embedding = model.encode(task_intent)
    similarities = {
        name: np.dot(task_embedding, emb) / (np.linalg.norm(task_embedding) * np.linalg.norm(emb))
        for name, emb in tool_embeddings.items()
    }
    return sorted(similarities, key=similarities.get, reverse=True)[:top_k]
```

**Option C — Hybrid (recommended)**
Core tools (file ops, terminal, search) always loaded + semantic selection for specialized tools.

### Step 4 — Define the Always-On Set
Tools that are ALWAYS included regardless of task intent:
- `write_to_file` / `replace_file_content` / `multi_replace_file_content` / `view_file`
- `run_command` / `command_status`
- `grep_search` / `list_dir`
- `search_web`

These are foundational capabilities. Estimated: ~1500 tokens.
Everything else is loaded on demand.

### Step 5 — Design the Fallback Mechanism
If the agent tries to use a tool not in its current set:
1. Detect the tool request (tool name not in loaded set)
2. Query the full tool index for the requested tool
3. Inject the requested tool's schema into the next turn
4. Log the "cache miss" for future routing improvement

Track cache miss rate over time. If a tool consistently causes misses, add it to a broader cluster or to the always-on set.

### Step 6 — Token Math & Validation

```
Current State:
  - All tools loaded: ~100 definitions × ~200 tokens = 20,000 tokens

Target State:
  - Always-on set: ~8 tools × ~200 tokens = 1,600 tokens
  - Dynamic set: ~5 tools × ~200 tokens = 1,000 tokens
  - Total: ~2,600 tokens

  Reduction: 87% of tool token overhead
```

Validate:
- [ ] Run 20 representative tasks with Tool Router
- [ ] Measure cache miss rate (target: <10%)
- [ ] Compare task success rate vs. all-tools-loaded baseline
- [ ] Measure latency improvement from reduced context

### Step 7 — Implementation Plan

**Day 1**: Catalog all tools, measure current token overhead
**Day 2**: Implement Option A (rule-based) as MVP
**Day 3**: Test on 10 representative tasks, measure miss rate
**Day 4**: Refine clusters based on miss patterns
**Day 5**: If miss rate >10%, implement Option B (semantic) for specialized tools
**Week 2**: Monitor in production, track miss rate, adjust always-on set

## Output Schema

**Contract**: Tool Router architecture with dynamically-loaded tool selection based on task intent, designed to reduce context overhead from 20K to 2.6K tokens while maintaining <10% cache miss rate.

**Deliverables**:
1. Tool Inventory Table — complete catalog with schema sizes (tokens) and usage frequency
2. Tool Clustering Map — functional domains and tool groupings
3. Selection Algorithm Specification — chosen router (MVP/Production/Hybrid) with inline Python pseudocode
4. Always-On Set Definition — 8 core tools that load regardless of task
5. Fallback Mechanism — handling out-of-set tool requests; cache-miss tracking
6. Token Math Comparison — before (20K all-tools) vs. after (2.6K dynamic)
7. Validation Checklist — pass/fail criteria for 20-task test suite with measurements

**Quality Gates**:
- [ ] Tool inventory covers 100%+ of available tool definitions (Notion, Core, MCP servers)
- [ ] Clustering rationale is explicit — no orphan tools
- [ ] Selection algorithm chosen with clear reasoning (MVP vs. production vs. hybrid)
- [ ] Token math is conservative (no inflated baseline, realistic schema sizing)
- [ ] Fallback mechanism handles missing tools without agent breakage
- [ ] Validation results show <10% cache miss rate on test suite (or clear path to <10%)
- [ ] Implementation timeline is realistic (scope/hours explicitly stated)

**Output Format**: Architecture document (markdown) + token math spreadsheet (CSV).

## Output Format
Deliver as an architecture document with:
- Complete tool inventory with usage frequency and schema sizes
- Clustering map
- Selection algorithm specification (chosen option with rationale)
- Always-on set definition
- Fallback mechanism design
- Token math (before/after)
- Validation results (miss rate, task success rate)
- Implementation timeline
