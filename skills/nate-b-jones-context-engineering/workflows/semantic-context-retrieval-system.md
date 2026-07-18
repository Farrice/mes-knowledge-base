# Semantic Context Retrieval System

> Replace static file loading (read full SKILL.md/genius.md) with embedding-based chunk retrieval that loads only task-relevant sections. Delivers 40-60% reduction in skill context tokens.

## Prerequisites
- All SKILL.md and genius.md files in the system
- Embedding model (text-embedding-3-small or all-MiniLM-L6-v2 for local)
- Vector database (pgvector, ChromaDB, or Pinecone)
- Current context loading pipeline understood

## Steps

### Step 1 — File Audit & Chunking Strategy

**Audit all skill files:**
```bash
find skills/ -name "SKILL.md" -o -name "genius.md" | wc -l
find skills/ -name "SKILL.md" -o -name "genius.md" | xargs wc -c | sort -rn | head -20
```

**Chunking rules:**
- Split on `## ` headers (H2 level) — each section becomes one chunk
- If a section exceeds 500 tokens, split on `### ` headers (H3 level)
- Each chunk includes:
  - Source file path
  - Section hierarchy (skill > section > subsection)
  - Expert name
  - Domain tags
- **Overlap**: Include 1 sentence from adjacent chunks for coherence
- **Minimum chunk**: 50 tokens (don't split atomic rules)
- **Maximum chunk**: 500 tokens (split larger sections)

### Step 2 — Chunking Pipeline

```python
import re
from pathlib import Path

def chunk_skill_file(filepath: Path) -> list[dict]:
    """Split a skill file into retrievable chunks."""
    content = filepath.read_text()
    chunks = []

    # Extract metadata
    expert = extract_expert_name(content)
    skill_name = filepath.parent.name

    # Split on H2 headers
    sections = re.split(r'\n## ', content)

    for i, section in enumerate(sections):
        if i == 0:
            # Frontmatter/intro
            header = "Overview"
            body = section
        else:
            lines = section.split('\n', 1)
            header = lines[0].strip()
            body = lines[1] if len(lines) > 1 else ""

        # Check if section needs sub-splitting
        if count_tokens(body) > 500:
            sub_chunks = split_on_h3(body, header)
            chunks.extend(sub_chunks)
        else:
            chunks.append({
                "source": str(filepath),
                "expert": expert,
                "skill": skill_name,
                "section": header,
                "content": f"## {header}\n{body}" if i > 0 else body,
                "token_count": count_tokens(body),
            })

    return chunks
```

### Step 3 — Embedding Generation

```python
from openai import OpenAI  # or local model

client = OpenAI()

def embed_chunks(chunks: list[dict]) -> list[dict]:
    """Generate embeddings for all chunks."""
    texts = [c["content"] for c in chunks]

    # Batch embed (API limit: 2048 per batch)
    embeddings = []
    for i in range(0, len(texts), 100):
        batch = texts[i:i+100]
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=batch,
        )
        embeddings.extend([e.embedding for e in response.data])

    for chunk, embedding in zip(chunks, embeddings):
        chunk["embedding"] = embedding

    return chunks
```

### Step 4 — Vector Store Setup

**PostgreSQL + pgvector:**
```sql
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE skill_chunks (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    source TEXT NOT NULL,
    expert TEXT NOT NULL,
    skill TEXT NOT NULL,
    section TEXT NOT NULL,
    content TEXT NOT NULL,
    token_count INTEGER NOT NULL,
    embedding vector(1536),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX ON skill_chunks USING ivfflat (embedding vector_cosine_ops)
    WITH (lists = 100);
```

**ChromaDB (simpler, local):**
```python
import chromadb

client = chromadb.PersistentClient(path="./skill_embeddings")
collection = client.get_or_create_collection(
    name="skill_chunks",
    metadata={"hnsw:space": "cosine"}
)
```

### Step 5 — Retrieval Integration

Replace the current static loading in the context pipeline:

**Current flow:**
```
Expert routed → Load full SKILL.md (~1350 tokens) → Load full genius.md (~2550 tokens)
Total per expert: ~3900 tokens
```

**New flow:**
```
Expert routed → Extract task intent → Embed task intent →
  Query skill_chunks WHERE expert = routed_expert →
  Return top 5 chunks by cosine similarity →
  Inject chunks into context (~1000-1500 tokens)
Total per expert: ~1000-1500 tokens (60-75% reduction)
```

```python
def retrieve_context(task_intent: str, expert: str, top_k: int = 5) -> str:
    """Retrieve the most relevant skill chunks for a task."""
    task_embedding = embed_text(task_intent)

    results = collection.query(
        query_embeddings=[task_embedding],
        n_results=top_k,
        where={"expert": expert},
    )

    # Format for context injection
    context_block = "## Retrieved Expert Context\n\n"
    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
        context_block += f"**[{meta['skill']} > {meta['section']}]**\n{doc}\n\n"

    return context_block
```

### Step 6 — Hybrid Retrieval (Recommended)
Pure semantic retrieval can miss critical structural context. Use hybrid:

1. **Always load**: Skill name, expert name, core capability statement, workflow list (from SKILL.md header) — ~200 tokens
2. **Semantically retrieve**: Top 5 chunks from genius.md based on task intent — ~800-1200 tokens
3. **On-demand expand**: If agent requests more context, retrieve next 5 chunks — ~800-1200 tokens

Total: ~1000-1400 tokens baseline, expandable to ~2000+

### Step 7 — Freshness & Update Pipeline
When skill files are updated:
1. Detect file change (git diff or file watcher)
2. Re-chunk the changed file
3. Re-embed changed chunks
4. Upsert into vector store (replace old chunks by source + section)
5. Log the update

Run as a pre-commit hook or nightly cron.

### Step 8 — Validation
- [ ] Run 10 representative tasks per expert (sample 5 experts)
- [ ] Compare outputs: full-file-loaded vs. semantic-retrieval
- [ ] Measure: task success rate, output quality, instruction compliance
- [ ] Measure: token reduction per expert invocation
- [ ] Measure: retrieval latency (target: <200ms)
- [ ] Check: are critical frameworks/patterns consistently retrieved for relevant tasks?
- [ ] Check: any "lost knowledge" — information that was important but not retrieved?

## Output Schema

**Contract**: Semantic retrieval architecture replacing static SKILL.md/genius.md loading with embedding-based chunk retrieval, achieving 40-60% context reduction while maintaining output quality parity.

**Deliverables**:
1. Chunking Strategy Specification — H2/H3 split rules, chunk token bounds (50-500), overlap/metadata
2. Embedding Pipeline Design — batch embedding process (OpenAI or local model) with architecture diagram
3. Vector Store Schema — PostgreSQL + pgvector (or ChromaDB) schema with indices and retention policy
4. Retrieval Integration Code — Python implementation for query-embedding → top-k chunk retrieval
5. Hybrid Loading Architecture — always-load baseline (~200 tokens) + semantic retrieval (~800-1200 tokens) + on-demand expand
6. Update Pipeline Design — file-change detection → re-chunk → re-embed → upsert workflow (pre-commit or nightly cron)
7. Validation Results — 10-task comparison (full-load vs. semantic) measuring quality parity, token reduction, retrieval latency

**Quality Gates**:
- [ ] Chunking strategy is deterministic (no lossy splitting, no critical sections fragmented)
- [ ] Embedding pipeline handles batch processing; API cost is transparent (if paid model)
- [ ] Vector store schema supports fast queries (<200ms target) and version tracking
- [ ] Hybrid loading balances baseline context (core skill info) with semantic retrieval (task-specific)
- [ ] Retrieval latency <200ms on 5-chunk query
- [ ] Validation shows ≥95% quality parity between full-load and semantic output
- [ ] Migration path is clear (existing SKILL.md → chunks, existing genius.md → chunks, no knowledge loss)

**Output Format**: Architecture document (markdown) + schema SQL definitions + Python reference implementation.

## Output Format
Deliver as a technical architecture document with:
- Chunking strategy specification
- Embedding pipeline design
- Vector store schema
- Retrieval integration code
- Hybrid loading architecture
- Update pipeline design
- Validation results (quality parity, token reduction, latency)
- Migration plan from static loading
