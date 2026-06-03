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
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Need PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
INDEX_PATH = REPO_ROOT / ".agent" / "skill-index.json"

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
    }


def build_index() -> list[dict]:
    skills = []
    for skill_md in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        parsed = parse_skill(skill_md)
        if parsed:
            skills.append(parsed)
    return skills


def load_or_build_index(force: bool = False) -> list[dict]:
    if not force and INDEX_PATH.exists():
        try:
            cached = json.loads(INDEX_PATH.read_text())
        except json.JSONDecodeError:
            cached = None
        if cached:
            cached_by_dir = {s["directory"]: s for s in cached}
            current_paths = list(SKILLS_DIR.glob("*/SKILL.md"))
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
    scored = []
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
        if score > 0:
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
    out = [f"Top {len(results)} matches for: {query!r}", ""]
    for i, (s, score) in enumerate(results, 1):
        desc = (s["description"] or "(no description)").replace("\n", " ")
        snip = desc[:160] + ("…" if len(desc) > 160 else "")
        out.append(f"{i}. {s['directory']}   score {score:.1f}")
        out.append(f"   → {s['slash']}")
        out.append(f"   {snip}")
        out.append("")
    out.append("Invoke by typing the slash command above.")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Find the right skill via local keyword search.")
    ap.add_argument("query", nargs="+", help="What you want to do, in natural language.")
    ap.add_argument("--top", type=int, default=5, help="Max results (default 5).")
    ap.add_argument("--rebuild-index", action="store_true", help="Force rebuild of skill index.")
    ap.add_argument("--json", action="store_true", help="Output JSON instead of formatted text.")
    args = ap.parse_args()
    query = " ".join(args.query)
    skills = load_or_build_index(force=args.rebuild_index)
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
