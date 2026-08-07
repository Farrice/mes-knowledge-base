#!/usr/bin/env python3
"""
Context Retriever — Semantic skill chunk retrieval for dynamic context loading.

Instead of loading full SKILL.md/genius.md files (~3900 tokens per expert),
this retriever chunks files on H2/H3 headers, indexes them, and returns only
the most relevant chunks for a given task intent.

Uses pure-Python TF-IDF (no sklearn dependency) for MVP similarity matching.

Usage:
    python3 execution/context_retriever.py index                           # Build chunk index
    python3 execution/context_retriever.py search "memory compression"     # Search all chunks
    python3 execution/context_retriever.py search "belief change" --expert david-mcraney
    python3 execution/context_retriever.py search "hooks" --top 10
    python3 execution/context_retriever.py stats                           # Index statistics
"""

import sys
import os
import re
import json
import math
import argparse
from pathlib import Path
from collections import Counter, defaultdict

# ─────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────

SKILLS_DIR = Path(__file__).parent.parent / "skills"
INDEX_PATH = Path(__file__).parent / "skill_chunks.json"

# Chunking thresholds (in words, approximating tokens)
MAX_CHUNK_WORDS = 500
MIN_CHUNK_WORDS = 30

# TF-IDF stop words (minimal set for domain relevance)
STOP_WORDS = frozenset([
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "it", "as", "be", "was", "are",
    "were", "been", "being", "have", "has", "had", "do", "does", "did",
    "will", "would", "could", "should", "may", "might", "can", "shall",
    "this", "that", "these", "those", "not", "no", "nor", "if", "then",
    "else", "when", "where", "which", "who", "whom", "what", "how", "why",
    "all", "each", "every", "both", "few", "more", "most", "other", "some",
    "such", "than", "too", "very", "just", "also", "about", "up", "out",
    "so", "its", "into", "over", "after", "before", "between", "through",
    "during", "under", "above", "below", "use", "using", "used",
    "your", "you", "they", "them", "their", "we", "our", "he", "she",
    "him", "her", "my", "me", "i", "any", "here", "there", "only",
])


# ─────────────────────────────────────────────────────────
# CHUNKING PIPELINE
# ─────────────────────────────────────────────────────────

def extract_expert_name(filepath):
    """Extract expert name from skill directory name."""
    return filepath.parent.name


def word_count(text):
    """Approximate word count."""
    return len(text.split())


def chunk_on_headers(content, header_pattern):
    """Split content on a markdown header pattern, returning (header, body) pairs."""
    sections = re.split(r'\n' + header_pattern + r' ', content)
    results = []

    for i, section in enumerate(sections):
        if i == 0:
            # Everything before first header
            results.append(("Overview", section.strip()))
        else:
            lines = section.split('\n', 1)
            header = lines[0].strip().rstrip('#').strip()
            body = lines[1].strip() if len(lines) > 1 else ""
            results.append((header, body))

    return results


def chunk_skill_file(filepath):
    """Split a skill file into retrievable chunks."""
    try:
        content = filepath.read_text(encoding='utf-8')
    except (UnicodeDecodeError, FileNotFoundError):
        return []

    if not content.strip():
        return []

    expert = extract_expert_name(filepath)
    skill_name = filepath.parent.name
    file_type = filepath.name  # SKILL.md or genius.md

    chunks = []

    # Split on H2 headers
    h2_sections = chunk_on_headers(content, '##')

    for h2_header, h2_body in h2_sections:
        if not h2_body.strip():
            continue

        wc = word_count(h2_body)

        if wc > MAX_CHUNK_WORDS:
            # Sub-split on H3 headers
            h3_sections = chunk_on_headers(h2_body, '###')
            for h3_header, h3_body in h3_sections:
                if not h3_body.strip() or word_count(h3_body) < MIN_CHUNK_WORDS:
                    continue

                section_label = f"{h2_header} > {h3_header}" if h3_header != "Overview" else h2_header
                chunk_content = f"## {h2_header}\n### {h3_header}\n{h3_body}" if h3_header != "Overview" else f"## {h2_header}\n{h3_body}"

                chunks.append({
                    "source": str(filepath.relative_to(SKILLS_DIR.parent)),
                    "expert": expert,
                    "skill": skill_name,
                    "file_type": file_type,
                    "section": section_label,
                    "content": chunk_content.strip(),
                    "word_count": word_count(h3_body),
                })
        elif wc >= MIN_CHUNK_WORDS:
            chunk_content = f"## {h2_header}\n{h2_body}" if h2_header != "Overview" else h2_body

            chunks.append({
                "source": str(filepath.relative_to(SKILLS_DIR.parent)),
                "expert": expert,
                "skill": skill_name,
                "file_type": file_type,
                "section": h2_header,
                "content": chunk_content.strip(),
                "word_count": wc,
            })

    return chunks


def retrieval_file_names(skill_dir):
    """Return the files safe to place in preselection retrieval for a skill.

    Skills with ``context_retrieval: skill-only-until-selected`` keep their
    deeper ``genius.md`` methodology out of the general retrieval index. The
    selected workflow may still load that file explicitly after its decision
    gate.
    """
    default = ["SKILL.md", "genius.md"]
    skill_path = skill_dir / "SKILL.md"
    try:
        content = skill_path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, FileNotFoundError):
        return default

    if not content.startswith("---"):
        return default
    closing = content.find("\n---", 3)
    if closing == -1:
        return default

    frontmatter = content[3:closing]
    match = re.search(
        r"(?m)^context_retrieval:\s*[\"']?([a-z0-9-]+)",
        frontmatter,
    )
    if match and match.group(1) == "skill-only-until-selected":
        return ["SKILL.md"]
    return default


def build_index():
    """Scan all skill files and build the chunk index."""
    all_chunks = []
    file_count = 0
    errors = []

    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir() or skill_dir.name.startswith('.'):
            continue

        for filename in retrieval_file_names(skill_dir):
            filepath = skill_dir / filename
            if filepath.exists():
                file_count += 1
                chunks = chunk_skill_file(filepath)
                all_chunks.extend(chunks)

    # Assign IDs
    for i, chunk in enumerate(all_chunks):
        chunk["id"] = i

    # Save index
    index_data = {
        "version": 1,
        "file_count": file_count,
        "chunk_count": len(all_chunks),
        "chunks": all_chunks,
    }

    INDEX_PATH.write_text(json.dumps(index_data, indent=2), encoding='utf-8')
    return index_data


# ─────────────────────────────────────────────────────────
# PURE PYTHON TF-IDF ENGINE
# ─────────────────────────────────────────────────────────

def tokenize(text):
    """Tokenize text into lowercase stems, removing stop words."""
    words = re.findall(r'[a-z][a-z0-9\-]+', text.lower())
    return [_stem(w) for w in words if w not in STOP_WORDS and len(w) > 2]


def _stem(word):
    """Minimal suffix-strip stemmer (matching expert_router.py)."""
    for suffix in ("ing", "tion", "ness", "ally", "ment", "ive", "ity", "ly", "ed", "er", "es", "s"):
        if len(word) > len(suffix) + 3 and word.endswith(suffix):
            return word[: -len(suffix)]
    return word


def compute_tf(tokens):
    """Compute term frequency for a token list."""
    counts = Counter(tokens)
    total = len(tokens) if tokens else 1
    return {term: count / total for term, count in counts.items()}


def compute_idf(corpus_tokens):
    """Compute inverse document frequency across a corpus."""
    n_docs = len(corpus_tokens)
    if n_docs == 0:
        return {}

    # Count documents containing each term
    doc_freq = Counter()
    for tokens in corpus_tokens:
        unique = set(tokens)
        for term in unique:
            doc_freq[term] += 1

    # IDF with smoothing
    return {
        term: math.log((n_docs + 1) / (freq + 1)) + 1
        for term, freq in doc_freq.items()
    }


def tfidf_similarity(query_tokens, doc_tf, idf):
    """Compute TF-IDF cosine similarity between query and document."""
    if not query_tokens or not doc_tf:
        return 0.0

    query_tf = compute_tf(query_tokens)

    # Build TF-IDF vectors
    all_terms = set(query_tf.keys()) | set(doc_tf.keys())

    q_vec = []
    d_vec = []
    for term in all_terms:
        term_idf = idf.get(term, 1.0)
        q_vec.append(query_tf.get(term, 0) * term_idf)
        d_vec.append(doc_tf.get(term, 0) * term_idf)

    # Cosine similarity
    dot = sum(a * b for a, b in zip(q_vec, d_vec))
    norm_q = math.sqrt(sum(a * a for a in q_vec)) or 1
    norm_d = math.sqrt(sum(a * a for a in d_vec)) or 1

    return dot / (norm_q * norm_d)


# ─────────────────────────────────────────────────────────
# RETRIEVAL
# ─────────────────────────────────────────────────────────

def load_index():
    """Load the chunk index from disk."""
    if not INDEX_PATH.exists():
        print(f"Index not found at {INDEX_PATH}. Run: python3 execution/context_retriever.py index")
        sys.exit(1)

    data = json.loads(INDEX_PATH.read_text(encoding='utf-8'))
    return data


def retrieve_context(task_intent, expert=None, top_k=5):
    """
    Retrieve the most relevant skill chunks for a task.

    Args:
        task_intent: Natural language description of the task
        expert: Optional expert name to filter by
        top_k: Number of results to return

    Returns:
        List of (score, chunk) tuples sorted by relevance
    """
    index_data = load_index()
    chunks = index_data["chunks"]

    # Filter by expert if specified
    if expert:
        expert_lower = expert.lower()
        chunks = [c for c in chunks if expert_lower in c["expert"].lower()]
        if not chunks:
            print(f"No chunks found for expert '{expert}'")
            return []

    # Tokenize all chunks and query
    corpus_tokens = [tokenize(c["content"]) for c in chunks]
    query_tokens = tokenize(task_intent)

    if not query_tokens:
        print("Query produced no searchable tokens.")
        return []

    # Compute IDF across corpus
    idf = compute_idf(corpus_tokens)

    # Pre-compute TF for each document
    doc_tfs = [compute_tf(tokens) for tokens in corpus_tokens]

    # Score each chunk
    scored = []
    for i, (chunk, doc_tf) in enumerate(zip(chunks, doc_tfs)):
        score = tfidf_similarity(query_tokens, doc_tf, idf)

        # Boost: exact query terms in section header
        section_lower = chunk["section"].lower()
        header_bonus = sum(
            0.1 for qt in query_tokens
            if qt in section_lower or _stem(qt) in section_lower
        )
        score += header_bonus

        if score > 0.01:
            scored.append((score, chunk))

    scored.sort(key=lambda x: -x[0])
    return scored[:top_k]


def format_retrieval_output(results, task_intent, expert=None):
    """Format retrieval results for display."""
    if not results:
        filter_msg = f" for expert '{expert}'" if expert else ""
        print(f"No relevant chunks found{filter_msg}.")
        return

    print(f"Query: \"{task_intent}\"")
    if expert:
        print(f"Expert filter: {expert}")
    print(f"Results: {len(results)} chunks\n")
    print("-" * 80)

    for rank, (score, chunk) in enumerate(results, 1):
        print(f"\n[{rank}] Score: {score:.4f}")
        print(f"    Expert:  {chunk['expert']}")
        print(f"    Source:  {chunk['source']} ({chunk['file_type']})")
        print(f"    Section: {chunk['section']}")
        print(f"    Words:   {chunk['word_count']}")

        # Show content preview (first 200 chars)
        preview = chunk["content"][:200].replace('\n', ' ')
        if len(chunk["content"]) > 200:
            preview += "..."
        print(f"    Preview: {preview}")
        print("-" * 80)


def show_stats():
    """Show index statistics."""
    index_data = load_index()
    chunks = index_data["chunks"]

    total_words = sum(c["word_count"] for c in chunks)
    experts = set(c["expert"] for c in chunks)
    skills = set(c["skill"] for c in chunks)

    by_expert = defaultdict(int)
    by_file_type = defaultdict(int)
    for c in chunks:
        by_expert[c["expert"]] += 1
        by_file_type[c["file_type"]] += 1

    print(f"Index version:   {index_data['version']}")
    print(f"Files indexed:   {index_data['file_count']}")
    print(f"Total chunks:    {index_data['chunk_count']}")
    print(f"Total words:     {total_words:,}")
    print(f"Unique experts:  {len(experts)}")
    print(f"Unique skills:   {len(skills)}")
    print(f"\nBy file type:")
    for ft, count in sorted(by_file_type.items()):
        print(f"  {ft:15s} {count:4d} chunks")

    print(f"\nTop 20 experts by chunk count:")
    top = sorted(by_expert.items(), key=lambda x: -x[1])[:20]
    for expert, count in top:
        print(f"  {expert:40s} {count:4d} chunks")

    print(f"\nChunk size distribution:")
    sizes = [c["word_count"] for c in chunks]
    if sizes:
        print(f"  Min:    {min(sizes)} words")
        print(f"  Max:    {max(sizes)} words")
        print(f"  Mean:   {sum(sizes) // len(sizes)} words")
        print(f"  Median: {sorted(sizes)[len(sizes) // 2]} words")


def main():
    parser = argparse.ArgumentParser(description="Context Retriever — Semantic skill chunk retrieval")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("index", help="Build/rebuild the chunk index from all skill files")

    search_p = sub.add_parser("search", help="Search for relevant skill chunks")
    search_p.add_argument("query", help="Task description or search query")
    search_p.add_argument("--expert", "-e", help="Filter by expert name")
    search_p.add_argument("--top", "-n", type=int, default=5, help="Number of results (default: 5)")

    sub.add_parser("stats", help="Show index statistics")

    args = parser.parse_args()

    if args.command == "index":
        print("Building chunk index...")
        data = build_index()
        print(f"Done. Indexed {data['file_count']} files → {data['chunk_count']} chunks")
        print(f"Saved to {INDEX_PATH}")

    elif args.command == "search":
        results = retrieve_context(args.query, expert=args.expert, top_k=args.top)
        format_retrieval_output(results, args.query, expert=args.expert)

    elif args.command == "stats":
        show_stats()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
