#!/usr/bin/env python3
"""find_skill.py — Local skill discovery via BM25 keyword search.

Why this exists: Claude Code's skill auto-fire uses keyword matching against a
character-budgeted listing (default ~1% of context). With 257 skills, most
descriptions get truncated to ~30 chars at session start, so auto-fire is
unreliable for anything but the first few skills loaded. This script bypasses
auto-fire entirely — user types a natural utterance, gets back top matches
with slash commands they can copy-paste to invoke reliably.

Usage:
    python3 execution/find_skill.py "my agent forgets stuff between sessions"
    python3 execution/find_skill.py --top 3 "..."
    python3 execution/find_skill.py --rebuild-index "..."  # force rebuild
    python3 execution/find_skill.py --json "..."           # machine-readable

Index cached at .agent/skill-index.json, keyed by per-file mtime.
"""

import argparse
import hashlib
import json
import math
import os
import re
import sys
import time
from collections import Counter
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Need PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
# Vendored third-party skills (Scrapes Skill Systems, 2026-09-02). Claude Code
# mounts each as /<name>; indexing them here is what lets the per-prompt router
# suggest them from intent instead of only on an explicit slash. Symlinks are
# skipped (the .agents/skills mirror would double-index).
VENDOR_SKILLS_DIR = REPO_ROOT / ".claude" / "skills"
INDEX_PATH = REPO_ROOT / ".agent" / "skill-index.json"


def _skill_md_paths() -> list[Path]:
    paths = list(SKILLS_DIR.glob("*/SKILL.md"))
    if VENDOR_SKILLS_DIR.is_dir():
        paths += [p for p in VENDOR_SKILLS_DIR.glob("*/SKILL.md") if not p.parent.is_symlink()]
    return sorted(paths)

STOPWORDS = {
    "a","an","the","and","or","but","if","then","of","on","in","to","for","with",
    "from","by","as","is","are","was","were","be","been","being","have","has","had",
    "do","does","did","will","would","should","could","may","might","i","you","we",
    "they","it","this","that","these","those","my","your","our","their","its",
    "use","using","used","when","where","what","which","who","how","why","just",
    "into","out","up","down","over","about","like","get","got","make","made",
}


# Domain-specific aliases — maps Farrice's idiom → canonical search terms.
# This is the high-leverage spot to customize. When the matcher whiffs, the
# fix is almost always "add the user's natural phrasing here, pointing at the
# words that actually appear in the matching skill's description."
SYNONYMS = {
    # Agent / memory / context
    "forgets": ["memory", "persistence", "context", "persistent"],
    "remembers": ["memory", "persistence", "context"],
    "loses": ["memory", "context", "compression"],
    "bloat": ["context", "compression", "memory"],
    "compression": ["compression", "context", "memory"],
    # Strategy / business
    "stuck": ["constraint", "bottleneck", "plateau", "positioning"],
    "plateau": ["plateau", "constraint", "stuck"],
    "pricing": ["pricing", "positioning", "commoditization"],
    "differentiate": ["differentiation", "positioning", "sacrifice"],
    # Persuasion mechanics (Sean Macintyre — wired per 2026-06-09 deployment audit)
    "armor": ["armor", "resistance", "skepticism", "persuasion", "macintyre"],
    "skeptical": ["armor", "resistance", "scrutiny", "persuasion"],
    "mechanism": ["mechanism", "persuasion", "proof", "macintyre"],
    "scrutiny": ["scrutiny", "adversarial", "persuasion", "macintyre"],
    "guru": ["guru", "authority", "persuasion", "macintyre"],
    # Content
    "viral": ["viral", "reverse-engineer", "breakdown", "shareable"],
    "headline": ["headline", "hook", "title", "linkedin"],
    "hook": ["hook", "headline", "vicious"],
    "post": ["post", "linkedin", "content", "ghostwrite"],
    "substack": ["substack", "newsletter", "parallax"],
    "newsletter": ["newsletter", "substack", "email"],
    # Visual / creative
    "poster": ["poster", "image", "visual", "stylized", "fantastic-posters"],
    "video": ["video", "animation", "kling", "seedance"],
    "image": ["image", "poster", "visual", "generate"],
    "vintage": ["vintage", "poster", "stylized"],
    # Brand
    "brand": ["brand", "positioning", "identity", "voice"],
    "voice": ["voice", "tone", "ghostwriting"],
    "tone": ["tone", "voice", "calibrate"],
    # Real estate (Jen)
    "listing": ["listing", "real-estate", "property"],
    "buyer": ["buyer", "real-estate", "first-time"],
    # Sports betting
    "picks": ["picks", "nba", "betting", "prizepicks"],
    "betting": ["betting", "picks", "nba", "edge"],
    # System / agents
    "evolve": ["evolve", "self-improving", "metaharness", "karpathy"],
    "orchestrate": ["orchestration", "multi-agent", "swarm", "dpvi"],
    "swarm": ["swarm", "parallel", "agents", "orchestration"],
    "deploy": ["deploy", "production", "harness"],
    # Spoken communication / presence / persuasion (Bayer, Chase Hughes, Miner)
    "keynote": ["spoken", "communication", "presence", "speaking", "stage", "bayer"],
    "speak": ["spoken", "communication", "presence", "speaking", "bayer"],
    "speech": ["spoken", "communication", "presence", "bayer"],
    "stage": ["spoken", "presence", "speaking", "bayer"],
    "presence": ["presence", "spoken", "authority", "bayer"],
    "grounded": ["presence", "spoken", "authentic", "bayer"],
    "authentic": ["authenticity", "presence", "voice", "bayer"],
    "persuade": ["persuasion", "influence", "framing"],
    "influence": ["influence", "persuasion", "conversational"],
    "pitch": ["pitch", "positioning", "persuasion", "sales"],
    "negotiate": ["negotiation", "influence", "power", "presence"],
    # Copywriting (the cluster is large; route the common idioms)
    "copy": ["copywriting", "copy", "dopamine", "direct-response"],
    "ad": ["ad", "ads", "advertising", "creative"],
    "ads": ["ads", "advertising", "creative", "meta"],
    "sales": ["sales", "persuasion", "closing", "offer"],
    "offer": ["offer", "pricing", "positioning", "product"],
    "vsl": ["vsl", "video-sales-letter", "lead"],
    # Positioning / brand strategy
    "positioning": ["positioning", "differentiation", "brand"],
    "niche": ["niche", "positioning", "specificity", "multipassionate"],
    "story": ["story", "storytelling", "narrative"],
    "storytelling": ["storytelling", "narrative", "story"],
    # Memoir / literary / narrative prose (Lamott, Ocean Vuong, Connelly, Wright Thompson)
    "memoir": ["memoir", "narrative", "personal", "lamott", "interiority"],
    "father": ["memoir", "personal", "narrative"],
    "mother": ["memoir", "personal", "narrative"],
    "essay": ["essay", "narrative", "writing", "prose"],
    "chapter": ["memoir", "narrative", "book", "writing"],
    "book": ["book", "narrative", "memoir", "writing"],
    "prose": ["prose", "writing", "sentence", "literary"],
    "literary": ["literary", "prose", "narrative", "perceptual"],
    "write": ["writing", "prose", "craft"],
    "writing": ["writing", "prose", "craft", "narrative"],
    # Brand identity / design / luxury / visual
    "identity": ["identity", "brand", "design", "visual"],
    "luxury": ["luxury", "premium", "positioning", "oren"],
    "premium": ["premium", "luxury", "positioning"],
    "logo": ["logo", "design", "visual", "composition"],
    "design": ["design", "visual", "brand", "system"],
    "skincare": ["brand", "luxury", "dtc", "ecommerce"],
    "fashion": ["fashion", "brand", "shopify", "dtc"],
}


def _stem(t: str) -> str:
    """Light suffix stripping so 'communication'~'communicate', 'authentic'~'authenticity'.
    Conservative: only strips when >=4 chars remain, avoids over-collapsing."""
    for suf in ("ization", "ation", "ing", "ed", "ly", "ity", "es", "s"):
        if len(t) - len(suf) >= 4 and t.endswith(suf):
            return t[: -len(suf)]
    return t


def tokenize(text: str) -> list[str]:
    """Lowercase, split on non-word, ALSO split hyphenated compounds into subtokens,
    drop stopwords + short tokens, then light-stem.

    The hyphen-split is the key recall fix: skill descriptions are dense with
    compounds like 'spoken-communication', 'authenticity-as-status', 'power-presence'.
    Without splitting, a user typing 'communication' or 'authentic' never matches them.
    We keep BOTH the whole compound and its parts so exact-compound matches still score.
    """
    text = text.lower()
    raw = re.findall(r"[a-z0-9\-]+", text)
    out = []
    for t in raw:
        pieces = [t] + t.split("-") if "-" in t else [t]
        for p in pieces:
            if p not in STOPWORDS and len(p) > 2:
                out.append(_stem(p))
    return out


def expand(tokens: list[str]) -> list[str]:
    """Expand query tokens with synonyms — only on the query side, not the doc side."""
    out = []
    seen = set()
    for t in tokens:
        if t not in seen:
            out.append(t)
            seen.add(t)
        for alias in SYNONYMS.get(t, []):
            if alias not in seen:
                out.append(alias)
                seen.add(alias)
    return out


def parse_skill(path: Path) -> dict | None:
    """Parse one SKILL.md into a searchable record. Returns None if frontmatter broken."""
    text = path.read_text(errors="ignore")
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    try:
        meta = yaml.safe_load(parts[1])
    except yaml.YAMLError:
        return None
    if not isinstance(meta, dict):
        return None
    body = parts[2]
    # Pull the "When to Use" / "When This Skill" section — high-signal trigger surface
    when_to_use = ""
    m = re.search(r"##\s+[Ww]hen[^\n]*\n(.+?)(?=\n##|\Z)", body, re.DOTALL)
    if m:
        when_to_use = m.group(1).strip()[:1200]
    return {
        "name": str(meta.get("name") or path.parent.name),
        "directory": path.parent.name,
        "description": str(meta.get("description", "")),
        "when_to_use": when_to_use,
        "mtime": path.stat().st_mtime,
        "slash": f"/{path.parent.name}",
        # Routing policy (Production Core rebuild 2026-06-09):
        #   routing: long-tail  -> demoted in rank(); explicit invocation preferred
        #   status: archived    -> de-indexed entirely (skill stays on disk)
        "routing": str(meta.get("routing", "")),
        "status": str(meta.get("status", "")),
    }


def build_index() -> list[dict]:
    skills = []
    for skill_md in _skill_md_paths():
        parsed = parse_skill(skill_md)
        if parsed and parsed.get("status") != "archived":
            if skill_md.is_relative_to(VENDOR_SKILLS_DIR):
                parsed["vendor"] = "scrapes"
            skills.append(parsed)
    return skills


# ── Production Core (PRODUCTION_CORE.md / .agent/production-core.json) ──
# Core entries get a multiplicative rank boost so routing DEFAULTS to the
# evidence-backed ~25; long-tail still surfaces when it decisively outranks.
CORE_PATH = REPO_ROOT / ".agent" / "production-core.json"
CORE_BOOST = 1.5
LONG_TAIL_DEMOTE = 0.6

# ── Learned routing weights (evolution_orchestrator.run_routing_learning) ──
# Stored SEPARATELY from the skill index on purpose: the index rebuilds any
# time a SKILL.md's mtime changes (load_or_build_index), and rebuilds always
# regenerate every record from disk. If learned weights lived inside the
# index they'd be clobbered on the next rebuild. Keeping them in their own
# file means index rebuilds and weight learning never step on each other.
WEIGHTS_PATH = REPO_ROOT / ".agent" / "skill-weights.json"

# ── Hybrid retrieval: BM25 + Gemini embeddings (Wave 3 deferred item, shipped
# 2026-07-06) ──
# DEFAULT OFF behind SKILL_ROUTER_EMBED=1 — enable only after
# benchmark_router_retrieval.py shows evidence (see that script). Cache lives
# in its OWN file for the same reason skill-weights.json is separate from the
# index: load_or_build_index() regenerates every record from disk on any
# SKILL.md mtime change, and that rebuild must never clobber embeddings that
# took real API calls to produce.
EMBED_PATH = REPO_ROOT / ".agent" / "skill-embeddings.json"
EMBED_MODEL = "gemini-embedding-001"  # matches execution/memory_embed.py
EMBED_DIM = 768
EMBED_COST_PER_1M_TOKENS = 0.15
EMBED_QUERY_TIMEOUT_MS = 3000  # hard client-side cap; hook budget is 10s total


def _hybrid_enabled() -> bool:
    return os.environ.get("SKILL_ROUTER_EMBED") == "1"


def _skill_hash(s: dict) -> str:
    """Content hash for change detection — only re-embed skills whose
    name/description/when_to_use actually changed since the last build."""
    basis = f"{s.get('name', '')}\x1f{s.get('description', '')}\x1f{s.get('when_to_use', '')}"
    return hashlib.sha1(basis.encode("utf-8")).hexdigest()


def load_embed_cache() -> dict:
    try:
        return json.loads(EMBED_PATH.read_text())
    except Exception:
        return {}


def save_embed_cache(cache: dict) -> None:
    EMBED_PATH.parent.mkdir(parents=True, exist_ok=True)
    EMBED_PATH.write_text(json.dumps(cache))


def build_embeddings(skills: list[dict] | None = None) -> dict:
    """Embed every skill whose content hash changed since the last cache
    write. Skips unchanged skills entirely (hash match). Returns a report
    dict — never raises; a hard failure just means 0 embedded."""
    if skills is None:
        skills = load_or_build_index()
    cache = load_embed_cache()
    to_embed = []
    for s in skills:
        h = _skill_hash(s)
        cached = cache.get(s["directory"])
        if not cached or cached.get("hash") != h:
            to_embed.append((s, h))

    report = {
        "total_skills": len(skills),
        "unchanged": len(skills) - len(to_embed),
        "to_embed": len(to_embed),
        "embedded": 0,
        "failed": 0,
        "est_cost_usd": 0.0,
        "seconds": 0.0,
    }
    if not to_embed:
        return report

    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import memory_embed  # reuse house embedding client + model pattern
    except Exception as e:
        report["error"] = f"memory_embed import failed: {e}"
        return report

    texts = [
        f"{s['name']}. {s['description']} {s['when_to_use']}"[:8000]
        for s, _ in to_embed
    ]
    total_chars = sum(len(t) for t in texts)
    report["est_cost_usd"] = round(
        (total_chars / 4 / 1_000_000) * EMBED_COST_PER_1M_TOKENS, 4
    )

    start = time.time()
    batch_size = 20
    for i in range(0, len(to_embed), batch_size):
        chunk = to_embed[i : i + batch_size]
        chunk_texts = texts[i : i + batch_size]
        try:
            vectors = memory_embed.embed_batch(chunk_texts, task_type="RETRIEVAL_DOCUMENT")
        except Exception as e:
            report.setdefault("errors", []).append(str(e))
            vectors = [None] * len(chunk)
        for (s, h), vec in zip(chunk, vectors):
            if vec is None:
                report["failed"] += 1
                continue
            cache[s["directory"]] = {"hash": h, "vector": vec}
            report["embedded"] += 1
        if i + batch_size < len(to_embed):
            time.sleep(0.3)
    report["seconds"] = round(time.time() - start, 1)
    save_embed_cache(cache)
    return report


def _embed_query(text: str) -> list[float] | None:
    """Embed the incoming QUERY for hybrid rank(). Hard-capped at
    EMBED_QUERY_TIMEOUT_MS client-side so a slow/hanging network call can
    never blow the hook's 10s budget. ANY failure (missing lib, missing key,
    network, timeout) returns None — caller falls back to pure BM25."""
    try:
        from google import genai
        from google.genai import types

        env_path = REPO_ROOT / ".env"
        if env_path.exists():
            for line in env_path.read_text().splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, _, v = line.partition("=")
                    os.environ.setdefault(k.strip(), v.strip())
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            return None

        client = genai.Client(
            api_key=api_key,
            http_options=types.HttpOptions(timeout=EMBED_QUERY_TIMEOUT_MS),
        )
        resp = client.models.embed_content(
            model=EMBED_MODEL,
            contents=text[:8000],
            config={"task_type": "RETRIEVAL_QUERY", "output_dimensionality": EMBED_DIM},
        )
        if hasattr(resp, "embeddings") and resp.embeddings:
            return list(resp.embeddings[0].values)
        return None
    except Exception:
        return None


def _cosine(a: list[float], b: list[float]) -> float:
    if not a or not b:
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0.0 or nb == 0.0:
        return 0.0
    return dot / (na * nb)


def _minmax(values: list[float]) -> list[float]:
    if not values:
        return []
    lo, hi = min(values), max(values)
    if hi - lo < 1e-9:
        return [0.0 for _ in values]
    return [(v - lo) / (hi - lo) for v in values]


def load_core_ids() -> set:
    try:
        d = json.loads(CORE_PATH.read_text())
        return {e["id"] for k in ("skills", "workflows") for e in d.get(k, [])}
    except Exception:
        return set()


def load_skill_weights() -> dict:
    """Per-skill rank multipliers learned nightly from routing feedback
    (auto_match/auto_miss). Missing or corrupt file -> empty dict -> every
    skill defaults to weight 1.0 (no-op)."""
    try:
        return json.loads(WEIGHTS_PATH.read_text())
    except Exception:
        return {}


def load_or_build_index(force: bool = False) -> list[dict]:
    if not force and INDEX_PATH.exists():
        try:
            cached = json.loads(INDEX_PATH.read_text())
        except json.JSONDecodeError:
            cached = None
        if cached:
            cached_by_dir = {s["directory"]: s for s in cached}
            current_paths = _skill_md_paths()
            current_dirs = {p.parent.name for p in current_paths}
            if set(cached_by_dir) == current_dirs:
                stale = False
                for p in current_paths:
                    if cached_by_dir[p.parent.name]["mtime"] < p.stat().st_mtime:
                        stale = True
                        break
                if not stale:
                    return cached
    index = build_index()
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(index, indent=2))
    return index


K1 = 1.5
B = 0.75


def rank(skills: list[dict], query: str, top: int = 5, name_weight: int = 3) -> list[tuple[dict, float]]:
    """Rank skills against query using BM25. Name tokens get repeated for boost."""
    docs = []
    for s in skills:
        name_tokens = tokenize(s["name"]) + tokenize(s["directory"])
        body_tokens = tokenize(s["description"]) + tokenize(s["when_to_use"])
        docs.append(name_tokens * name_weight + body_tokens)
    N = len(docs)
    if N == 0:
        return []
    df = Counter()
    for d in docs:
        for t in set(d):
            df[t] += 1
    idf = {t: math.log((N - n + 0.5) / (n + 0.5) + 1.0) for t, n in df.items()}
    avgdl = sum(len(d) for d in docs) / N
    q_tokens = expand(tokenize(query))
    core = load_core_ids()
    weights = load_skill_weights()

    # Raw BM25 score per skill (unfiltered — needed for every skill so the
    # hybrid min-max normalization below has a full population to work from).
    bm25_raw = []
    for s, d in zip(skills, docs):
        counter = Counter(d)
        doc_len = len(d)
        score = 0.0
        for q in q_tokens:
            if q not in idf:
                continue
            tf = counter[q]
            if tf == 0:
                continue
            norm = K1 * ((1 - B) + B * doc_len / avgdl)
            score += idf[q] * (tf * (K1 + 1)) / (tf + norm)
        bm25_raw.append(score)

    # Hybrid path (SKILL_ROUTER_EMBED=1 only). Any failure at any stage —
    # import, cache read, network, timeout — falls back to pure bm25_raw
    # silently (one stderr line, never a crash). Non-hybrid behavior above
    # this point is byte-identical to the pre-hybrid implementation.
    blended = bm25_raw
    if _hybrid_enabled():
        try:
            cache = load_embed_cache()
            if cache:
                query_vec = _embed_query(query)
                if query_vec is not None:
                    cos_raw = [
                        _cosine(query_vec, (cache.get(s.get("directory", "")) or {}).get("vector"))
                        for s in skills
                    ]
                    bm25_norm = _minmax(bm25_raw)
                    cos_norm = _minmax(cos_raw)
                    # Rescale the [0,1] blend back to BM25's native magnitude.
                    # skill_router_hook.py's relevance floor (2.5-3.0) and the
                    # 0.45x "strong match" cutoff are both calibrated against
                    # raw BM25 scores (typically 5-40). Leaving the blend in
                    # [0,1] would make every hybrid query look like a miss to
                    # that caller without touching skill_router_hook.py itself.
                    scale = max(bm25_raw) if bm25_raw and max(bm25_raw) > 0 else 1.0
                    blended = [(0.6 * b + 0.4 * c) * scale for b, c in zip(bm25_norm, cos_norm)]
        except Exception as e:
            print(f"[find_skill] hybrid retrieval failed, falling back to BM25: {e}", file=sys.stderr)
            blended = bm25_raw

    scored = []
    for s, score in zip(skills, blended):
        if score > 0:
            # Production Core policy: boost core, demote long-tail. Boost is
            # multiplicative, NOT a filter — a decisively stronger long-tail
            # match still wins (preserves intentional deployments).
            if s.get("directory") in core:
                score *= CORE_BOOST
            elif s.get("routing") == "long-tail":
                score *= LONG_TAIL_DEMOTE
            # Learned weight (MoE-style nightly nudge, default 1.0 = no-op).
            score *= weights.get(s.get("directory", ""), 1.0)
            scored.append((s, score))
    scored.sort(key=lambda x: -x[1])
    return scored[:top]


def format_results(query: str, results: list[tuple[dict, float]]) -> str:
    if not results:
        return (
            f"No skills matched '{query}'.\n"
            "Try different keywords, or add this phrasing to the SYNONYMS map\n"
            "in execution/find_skill.py if it's something you'd say repeatedly."
        )
    core = load_core_ids()
    out = [f"Top {len(results)} matches for: {query!r}", ""]
    for i, (s, score) in enumerate(results, 1):
        desc = (s["description"] or "(no description)").replace("\n", " ")
        snip = desc[:160] + ("…" if len(desc) > 160 else "")
        tag = ("[CORE]" if s.get("directory") in core
               else "[long-tail]" if s.get("routing") == "long-tail" else "")
        out.append(f"{i}. {s['directory']}   score {score:.1f}  {tag}".rstrip())
        out.append(f"   → {s['slash']}")
        out.append(f"   {snip}")
        out.append("")
    out.append("Invoke by typing the slash command above.")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Find the right skill via local keyword search.")
    ap.add_argument("query", nargs="*", help="What you want to do, in natural language.")
    ap.add_argument("--top", type=int, default=5, help="Max results (default 5).")
    ap.add_argument("--rebuild-index", action="store_true", help="Force rebuild of skill index.")
    ap.add_argument("--json", action="store_true", help="Output JSON instead of formatted text.")
    ap.add_argument(
        "--include-workflows",
        action="store_true",
        help="Also rank the ~2,500 workflows INSIDE skills (via .agent/arsenal-index.json). "
        "CLI-only: skill_router_hook imports rank()/load_or_build_index() directly, so this "
        "never changes routing behavior or the hook's calibrated relevance floor.",
    )
    ap.add_argument(
        "--build-embeddings",
        action="store_true",
        help="Embed skills whose content changed into .agent/skill-embeddings.json, then exit "
        "(feeds the SKILL_ROUTER_EMBED=1 hybrid rank() path — off by default).",
    )
    args = ap.parse_args()

    if args.build_embeddings:
        skills = load_or_build_index(force=args.rebuild_index)
        report = build_embeddings(skills)
        print(json.dumps(report, indent=2))
        return

    if not args.query:
        ap.error("query is required unless --build-embeddings is passed")
    query = " ".join(args.query)
    skills = load_or_build_index(force=args.rebuild_index)
    if args.include_workflows:
        # Widen the corpus for this CLI run only. A skill answers "who knows
        # about this"; a workflow answers "what do I actually run" — the second
        # question is the one that stops assets being rebuilt.
        try:
            import arsenal_index
            for e in arsenal_index.load_or_build()["entries"]:
                if e["kind"] != "skill-workflow" or e["menu_status"] == "exempt":
                    continue
                skills.append({
                    "name": e["id"].replace("-", " "),
                    "directory": e["skill"],
                    "description": e.get("description") or "",
                    "when_to_use": "",
                    "routing": "",
                    # e["command"], never e["id"] — the minter prefixes numbered
                    # stems, so the file stem is often not the firing command.
                    "slash": f"/{e['command']}" if e.get("command") else f"({e['path']})",
                    "status": "",
                })
        except Exception as exc:
            print(f"[find_skill] --include-workflows unavailable: {exc}", file=sys.stderr)
    results = rank(skills, query, top=args.top)
    if args.json:
        print(json.dumps(
            [{**s, "score": score} for s, score in results],
            indent=2,
        ))
    else:
        print(format_results(query, results))


if __name__ == "__main__":
    main()
