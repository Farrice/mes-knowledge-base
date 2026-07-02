#!/usr/bin/env python3
"""
skill_census.py — E2 vintage-stratified embodiment census over skills/.

Implements the seven mechanical heuristics derived in the E1 factory audit
(_active/elevation-track/E1-factory-audit.md). Deterministic, read-only,
offline. Calibrated against the 8 E1-labeled skills before trusting output.

Grades:
  heartbeat-candidate  rich taste machinery + dense verbatim/entity anchoring
  solid                entity-dense, some machinery missing
  thin                 too little material to embody anything
  hollow-flag          E1 hollowness signature hit (summary without source)
  no-genius            no genius.md — embodiment unmeasurable (structural gap)

Usage:
  python3 execution/skill_census.py run [--json PATH] [--report PATH]
"""

import argparse
import json
import re
import subprocess
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
TRACES = ROOT / "evolution_store" / "v2_traces"

# H6 vintage strata (E1: hollowness tracks the 2026-01 bulk import)
BULK_CUTOFF = "2026-02-15"
HARVEST_START = "2026-06-25"

SECTION_RE = re.compile(r"^#{2,3}\s+", re.M)
# H1 substantive entities (E1: study names, dollar figures, tools, verbatim
# quotes). Bare single digits excluded — "Pattern 3" numbering is not evidence.
ENTITY_RE = re.compile(
    r"\$\d"                                   # dollar figures
    r"|\d+%"                                  # percentages
    r"|\d{2,}"                                # multi-digit numbers
    r"|\d+\s?(?:x|lb|kg|kcal|min|hr|k)\b"     # unit-bearing figures
    r"|[\"“][^\"”\n]{6,}[\"”]"                # verbatim quoted spans
    r"|https?://")                            # sources
# (proper-noun bigrams tried and removed: template labels like "Success
# Metric" match, masking the Enfroy hollow core — calibration 2026-07-02)
NUMBERING_RE = re.compile(r"\b(?:pattern|step|phase|tier|level|check|rule)\s+\d+\b", re.I)
INLINE_QUOTE_RE = re.compile(r"[\"“][^\"”\n]{10,}[\"”]")
QUOTE_LINE_RE = re.compile(r"^\s*>", re.M)
# H2 sections workflows commonly cross-reference in genius.md
XREF_TITLES = ["Decision Framework", "Anti-Patterns", "Voice DNA",
               "Signature Moves", "Operating Principles"]
# H3 "N criteria/rules" mentions
CRITERIA_RE = re.compile(
    r"(?:all|the)?\s*(\d+|three|four|five|six|seven)\s+(?:validation\s+)?"
    r"(criteria|rules|checks|tests|principles)\b", re.I)
LIST_ITEM_RE = re.compile(r"^\s*(?:[-*]|\d+\.)\s+", re.M)
ANTI_RE = re.compile(r"anti-pattern|would never|never do|failure mode", re.I)
# Assembly artifacts: leaked LLM meta-text / self-labeled invented exemplars
# (found in blind validation 2026-07-02: bond-halbert genius.md:205)
ARTIFACT_RE = re.compile(
    r"This response will provide|adhering to all output rules"
    r"|\(Reconstructed|Reconstructed example|Imagine a long-form", re.I)
# Provenance markers: named transcripts/videos/episodes (E1 feature #8 lite)
PROVENANCE_RE = re.compile(
    r"\btranscripts?\b|\bepisodes?\b|\binterviews?\b|\bpodcasts?\b"
    r"|\bmasterclass\b|youtube\.com|youtu\.be|\bmined from\b|\bsource:\s", re.I)
RECOG_RE = re.compile(r"recognize this as|distinguish (?:this|it) from", re.I)
RUBRIC_RE = re.compile(r"\b4/7/10\b|named? the anchor|anchor(?:ed)? at", re.I)


def sh(cmd):
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True).stdout


def load_vintages():
    """First-add date per skills/<dir>, one git call. Log is newest-first,
    so the LAST occurrence seen per dir is the original add."""
    out = sh(["git", "log", "--diff-filter=A", "--date=short",
              "--format=C|%ad", "--name-only", "--", "skills/"])
    vintages = {}
    cur = None
    for line in out.splitlines():
        if line.startswith("C|"):
            cur = line[2:]
        elif line.startswith("skills/") and cur:
            parts = line.split("/")
            if len(parts) >= 2:
                vintages[parts[1]] = cur  # overwrite → oldest wins
    return vintages


def load_usage():
    """Trace-filename usage counts: trace_<ts>_<name>.json."""
    counts = Counter()
    if TRACES.exists():
        for f in TRACES.glob("trace_*.json"):
            parts = f.stem.split("_", 3)  # trace_<date>_<time>_<name>
            if len(parts) == 4:
                counts[parts[3]] += 1
    return counts


def read(p):
    try:
        return p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def sections_zero_entity(genius: str):
    """H1: split genius.md on ##/### headers; ratio of sections w/o entities."""
    idx = [m.start() for m in SECTION_RE.finditer(genius)]
    if not idx:
        return 0, 0.0
    idx.append(len(genius))
    total, zero = 0, 0
    for a, b in zip(idx, idx[1:]):
        body = genius[a:b]
        if len(body.strip()) < 80:
            continue
        # strip the header line + structural numbering ("Pattern 3") so
        # section numbering can't masquerade as substantive evidence
        body = "\n".join(body.splitlines()[1:])
        body = NUMBERING_RE.sub("", body)
        total += 1
        if not ENTITY_RE.search(body):
            zero += 1
    return total, (zero / total if total else 0.0)


def dangling_refs(workflow_texts, genius: str):
    """H2: workflow cites a genius.md section title that doesn't exist."""
    glow = genius.lower()
    dangling = set()
    for txt in workflow_texts:
        if "genius.md" not in txt and "§" not in txt:
            continue
        for title in XREF_TITLES:
            if title.lower() in txt.lower() and title.lower() not in glow:
                dangling.add(title)
    return sorted(dangling)


def uninstantiated_criteria(genius: str):
    """H3: 'N criteria' mentions with no list within the next ~30 lines."""
    flags = 0
    lines = genius.splitlines()
    joined_pos = 0
    for m in CRITERIA_RE.finditer(genius):
        line_no = genius[:m.start()].count("\n")
        window = "\n".join(lines[line_no:line_no + 30])
        if len(LIST_ITEM_RE.findall(window)) < 3:
            flags += 1
    return flags


def skeleton_similarity(workflow_texts):
    """H4: mean pairwise Jaccard of normalized header sets."""
    skels = []
    for txt in workflow_texts:
        heads = frozenset(
            re.sub(r"[^a-z ]", "", h.lower()).strip()
            for h in re.findall(r"^#{1,3}\s+(.+)$", txt, re.M))
        if heads:
            skels.append(heads)
    if len(skels) < 4:
        return 0.0
    sims = []
    for i in range(len(skels)):
        for j in range(i + 1, len(skels)):
            u = skels[i] | skels[j]
            if u:
                sims.append(len(skels[i] & skels[j]) / len(u))
    return round(sum(sims) / len(sims), 3) if sims else 0.0


def grade(rec):
    if not rec["has_genius"]:
        return "no-genius"
    if rec["genius_kb"] < 2 or rec["sections"] < 3:
        return "thin"
    # Assembly artifacts = fabrication evidence; instant flag regardless of
    # entity density (fabricated numbers defeat density checks — Bond case)
    if rec["assembly_artifacts"]:
        return "hollow-flag"
    # Provenance ladder (E1 heartbeat feature #8): a timestamp source-ledger
    # fully exempts (evidence lives in the ledger — Lamott case); named-source
    # markers downgrade conviction to review (Craig case); neither → hollow
    if rec["zero_entity_ratio"] >= 0.45 and not rec["has_source_ledger"]:
        return "hybrid-flag" if rec["provenance_markers"] >= 2 else "hollow-flag"
    # Enfroy pattern: dense bolt-on masking a hollow core — mid ratio plus
    # template-stamp evidence (dangling refs / uninstantiated criteria)
    if rec["zero_entity_ratio"] >= 0.2 and (
            rec["dangling_refs"] or rec["uninstantiated_criteria"] >= 2):
        return "hybrid-flag"
    heartbeat = (rec["has_anti_patterns"]
                 and (rec["has_recognition_test"] or rec["has_rubric_anchors"])
                 and rec["zero_entity_ratio"] <= 0.2
                 and rec["inline_quotes"] >= 5)
    return "heartbeat-candidate" if heartbeat else "solid"


def stratum(vintage):
    if not vintage:
        return "unknown"
    if vintage <= BULK_CUTOFF:
        return "bulk-2026-01"
    if vintage >= HARVEST_START:
        return "harvest-2026-07"
    return "mid-period"


def census():
    vintages = load_vintages()
    usage = load_usage()
    records = []
    for d in sorted(SKILLS.iterdir()):
        if not d.is_dir() or d.name.endswith(".skill"):
            continue
        skill_md = read(d / "SKILL.md")
        genius = read(d / "genius.md")
        wf_texts = [read(f) for f in sorted(d.glob("workflows/*.md"))]
        combined = skill_md + "\n" + genius
        sections, zero_ratio = sections_zero_entity(genius)
        rec = {
            "skill": d.name,
            "vintage": vintages.get(d.name),
            "stratum": stratum(vintages.get(d.name)),
            "usage_traces": usage.get(d.name, 0),
            "has_skill_md": bool(skill_md),
            "has_genius": bool(genius),
            "genius_kb": round(len(genius) / 1024, 1),
            "workflow_count": len(wf_texts),
            "sections": sections,
            "zero_entity_ratio": round(zero_ratio, 3),
            "quote_lines": len(QUOTE_LINE_RE.findall(genius)),
            "inline_quotes": len(INLINE_QUOTE_RE.findall(genius))
                             + len(QUOTE_LINE_RE.findall(genius)),
            "dangling_refs": dangling_refs(wf_texts, genius),
            "uninstantiated_criteria": uninstantiated_criteria(genius),
            "skeleton_similarity": skeleton_similarity(wf_texts),
            "has_anti_patterns": bool(ANTI_RE.search(combined)),
            "has_recognition_test": bool(RECOG_RE.search(combined)),
            "has_rubric_anchors": bool(RUBRIC_RE.search(combined)),
            "has_source_ledger": (d / "source-ledger.md").exists()
                                 or "source-ledger" in combined,
            "assembly_artifacts": bool(ARTIFACT_RE.search(genius)),
            "provenance_markers": len(PROVENANCE_RE.findall(genius)),
        }
        rec["grade"] = grade(rec)
        records.append(rec)
    return records


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", nargs="?", default="run", choices=["run"])
    ap.add_argument("--json", default=str(ROOT / "_active/elevation-track/E2-census.json"))
    args = ap.parse_args()

    records = census()
    Path(args.json).parent.mkdir(parents=True, exist_ok=True)
    Path(args.json).write_text(json.dumps(
        {"generated": date.today().isoformat(), "records": records}, indent=1))

    by_grade = Counter(r["grade"] for r in records)
    print(f"skills: {len(records)}")
    for g, n in by_grade.most_common():
        print(f"  {g}: {n}")
    print("\nby stratum × grade:")
    strata = sorted({r["stratum"] for r in records})
    for s in strata:
        sub = [r for r in records if r["stratum"] == s]
        gs = Counter(r["grade"] for r in sub)
        print(f"  {s} ({len(sub)}): " + ", ".join(f"{g}={n}" for g, n in gs.most_common()))
    print(f"\nJSON → {args.json}")


if __name__ == "__main__":
    main()
