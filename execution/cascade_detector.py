#!/usr/bin/env python3
"""
Cascade Detector — Cross-skill downstream-impact monitor for Antigravity.

When Phase 2 KEEPs a variant, the change can silently regress related skills
through four channels:
  1. Same-expert siblings (they share genius.md references)
  2. Shared reference files (both skills load the same references/*.md)
  3. Cross-pollination history (pattern family transfer)
  4. Explicit stacking (SKILL.md Stacking Guide declarations)

Per Nate B Jones GP-12 Compounding Errors: "Bad optimization in one system
can cascade into a bunch of interconnected business processes." Phase 2
previously had no cross-skill regression check after KEEP.

This module is ADDITIVE — cascade audits surface candidates for human
inspection, never auto-revert. Non-blocking on first implementation per
Upgrade 5 constraints.

Usage:
    python execution/cascade_detector.py check <skill-name>
    python execution/cascade_detector.py related <skill-name>
    python execution/cascade_detector.py history --limit 20
    python execution/cascade_detector.py graph               # (re)generate cache
"""

import os
import re
import json
import argparse
from datetime import datetime
from pathlib import Path
from typing import Optional

PROJECT_ROOT = Path(__file__).parent.parent
SKILLS_DIR = PROJECT_ROOT / "skills"
KNOWLEDGE_PATTERNS_DIR = PROJECT_ROOT / "knowledge" / "patterns"
CASCADE_DIR = PROJECT_ROOT / "evolution_store" / "cascade_audits"
CASCADE_GRAPH = CASCADE_DIR / "cascade_graph.json"
CASCADE_DIR.mkdir(parents=True, exist_ok=True)

import sys
sys.path.insert(0, str(Path(__file__).parent))


# ─── Relationship confidence weights (from spec) ────────────────
SAME_EXPERT_WEIGHT = 3.0
SHARED_REF_WEIGHT = 2.0  # per overlapping reference file
STACKING_WEIGHT = 2.5
PATTERN_TRANSFER_WEIGHT = 1.5


# ─── Expert prefix extraction ───────────────────────────────────

def _all_skill_names() -> list:
    """All skill directory names (skips dotfiles and files)."""
    return sorted([
        p.name for p in SKILLS_DIR.iterdir()
        if p.is_dir() and not p.name.startswith('.')
    ])


def extract_expert(skill_name: str, all_skills: Optional[list] = None) -> Optional[str]:
    """Return the longest leading prefix (≥2 tokens) shared with ≥1 other skill.

    Examples:
      nate-b-jones-auto-improvement-loops → "nate-b-jones" (has 6 siblings)
      luke-iha-copy-blocks → "luke-iha" (has 10 siblings)
      standalone-unique-skill → None (no siblings)
    """
    if all_skills is None:
        all_skills = _all_skill_names()

    tokens = skill_name.split('-')
    # Try longest-first (most specific expert match)
    for cut in range(min(len(tokens) - 1, 5), 1, -1):
        prefix = '-'.join(tokens[:cut])
        siblings = [
            s for s in all_skills
            if s != skill_name and s.startswith(prefix + '-')
        ]
        if siblings:
            return prefix
    return None


def find_expert_siblings(skill_name: str, all_skills: Optional[list] = None) -> list:
    """Return all other skills sharing the same expert prefix."""
    if all_skills is None:
        all_skills = _all_skill_names()
    expert = extract_expert(skill_name, all_skills)
    if not expert:
        return []
    return [
        s for s in all_skills
        if s != skill_name and s.startswith(expert + '-')
    ]


# ─── Reference file parsing ─────────────────────────────────────

_REF_PATTERN = re.compile(r'references/([A-Za-z0-9_\-./]+\.md)')


def parse_references(skill_name: str) -> set:
    """Scan a skill's workflows + SKILL.md for references/<file>.md mentions.

    Returns set of reference filenames (basenames, not full paths).
    """
    skill_dir = SKILLS_DIR / skill_name
    if not skill_dir.exists():
        return set()

    refs = set()
    candidates = []
    candidates.extend(skill_dir.glob("workflows/*.md"))
    skill_md = skill_dir / "SKILL.md"
    if skill_md.exists():
        candidates.append(skill_md)

    for path in candidates:
        if path.name.endswith('.variant.md'):
            continue
        try:
            text = path.read_text()
        except Exception:
            continue
        for match in _REF_PATTERN.findall(text):
            refs.add(os.path.basename(match))
    return refs


def build_reference_index() -> dict:
    """Reverse index: reference filename → [skills that load it]."""
    index: dict[str, list[str]] = {}
    for skill in _all_skill_names():
        for ref in parse_references(skill):
            index.setdefault(ref, []).append(skill)
    return index


# ─── Stacking Guide parsing ─────────────────────────────────────

_STACKING_SECTION_PATTERNS = [
    re.compile(r'##+\s*Stacking Guide\s*\n(.*?)(?=\n##|\Z)', re.DOTALL | re.IGNORECASE),
    re.compile(r'##+\s*Stacks? with\s*\n(.*?)(?=\n##|\Z)', re.DOTALL | re.IGNORECASE),
    re.compile(r'##+\s*Compounds? with\s*\n(.*?)(?=\n##|\Z)', re.DOTALL | re.IGNORECASE),
]

_STACKING_SKILL_PATTERN = re.compile(r'`([a-z0-9][a-z0-9\-]+)`|\[([a-z0-9][a-z0-9\-]+)\]')


def parse_stacking_guide(skill_name: str) -> list:
    """Extract skills named in SKILL.md Stacking Guide (if present)."""
    skill_md = SKILLS_DIR / skill_name / "SKILL.md"
    if not skill_md.exists():
        return []
    try:
        text = skill_md.read_text()
    except Exception:
        return []

    section = None
    for pat in _STACKING_SECTION_PATTERNS:
        m = pat.search(text)
        if m:
            section = m.group(1)
            break
    if not section:
        return []

    all_skills = set(_all_skill_names())
    found = set()
    for m in _STACKING_SKILL_PATTERN.findall(section):
        cand = m[0] or m[1]
        if cand and cand in all_skills and cand != skill_name:
            found.add(cand)
    return sorted(found)


# ─── Cross-pollination history ──────────────────────────────────

def read_pattern_transfers() -> list:
    """Parse knowledge/patterns/*.md for source→target transfers.

    Expected frontmatter fields: `source:` (or `skill:`), `target:` or
    `transferred_to:`. Best-effort; missing fields are silently skipped.
    """
    if not KNOWLEDGE_PATTERNS_DIR.exists():
        return []
    transfers = []
    for pattern_file in sorted(KNOWLEDGE_PATTERNS_DIR.glob("*.md")):
        try:
            text = pattern_file.read_text()
        except Exception:
            continue
        if not text.startswith('---'):
            continue
        fm_end = text.find('---', 3)
        if fm_end == -1:
            continue
        frontmatter = text[3:fm_end]
        fields = {}
        for line in frontmatter.strip().splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                fields[k.strip().lower()] = v.strip()
        source = fields.get('source') or fields.get('skill')
        target = fields.get('target') or fields.get('transferred_to')
        if source and target:
            transfers.append({'source': source, 'target': target, 'file': pattern_file.name})
    return transfers


# ─── Core: downstream discovery ─────────────────────────────────

def find_downstream_skills(skill_kept: str, max_results: int = 5) -> list:
    """Identify skills potentially affected by a change to `skill_kept`.

    Returns a ranked list of dicts:
      [{skill, confidence, reasons: [...]}, ...]

    Ranking by confidence (weighted sum across 4 relationship types).
    """
    all_skills = _all_skill_names()
    scores: dict[str, float] = {}
    reasons: dict[str, list[str]] = {}

    def _bump(skill: str, weight: float, reason: str) -> None:
        scores[skill] = scores.get(skill, 0.0) + weight
        reasons.setdefault(skill, []).append(reason)

    # 1. Same expert
    for sibling in find_expert_siblings(skill_kept, all_skills):
        _bump(sibling, SAME_EXPERT_WEIGHT, 'same-expert')

    # 2. Shared reference files
    kept_refs = parse_references(skill_kept)
    if kept_refs:
        for other in all_skills:
            if other == skill_kept:
                continue
            other_refs = parse_references(other)
            overlap = kept_refs & other_refs
            if overlap:
                _bump(other, SHARED_REF_WEIGHT * len(overlap),
                      f"shared-refs:{','.join(sorted(overlap))}")

    # 3. Cross-pollination history
    for t in read_pattern_transfers():
        if t['source'] == skill_kept and t['target'] != skill_kept and t['target'] in all_skills:
            _bump(t['target'], PATTERN_TRANSFER_WEIGHT,
                  f"pattern-transfer:{t['file']}")

    # 4. Explicit stacking
    for partner in parse_stacking_guide(skill_kept):
        _bump(partner, STACKING_WEIGHT, 'stacking-declared')

    ranked = [
        {'skill': s, 'confidence': round(scores[s], 2), 'reasons': reasons[s]}
        for s in sorted(scores, key=lambda k: -scores[k])
    ]
    return ranked[:max_results]


# ─── Baseline lookup (from Performance Log) ─────────────────────

def _get_skill_baseline(skill_name: str, window: int = 5) -> Optional[float]:
    """Pull rolling quality_score baseline for a skill from Performance Log.

    Returns mean of last `window` entries, or None if unavailable.
    """
    try:
        from skill_benchmark import get_performance_history
        history = get_performance_history(skill_name, limit=window)
        scores = [e.get('Quality Score') for e in history if e.get('Quality Score') is not None]
        if not scores:
            return None
        return round(sum(scores) / len(scores), 2)
    except Exception:
        return None


def _get_skill_current_score(skill_name: str) -> Optional[float]:
    """Single most-recent quality score for a skill."""
    try:
        from skill_benchmark import get_performance_history
        history = get_performance_history(skill_name, limit=1)
        for e in history:
            q = e.get('Quality Score')
            if q is not None:
                return float(q)
        return None
    except Exception:
        return None


# ─── Core: cascade impact check ─────────────────────────────────

def check_cascade_impact(skill_kept: str, sample_size: int = 3,
                         regression_threshold: float = 0.5) -> dict:
    """After KEEPing a variant in `skill_kept`, sample downstream skills
    and flag any whose current score has dropped >threshold below baseline.

    Returns:
      {
        skill_kept, downstream_checked: [...],
        regressions: [{skill, current_score, baseline_score, delta, reasons}],
        sampled: [...full detail for each sampled skill],
        flag: bool  # True if any regression
      }
    """
    timestamp = datetime.now().isoformat()
    audit_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    candidates = find_downstream_skills(skill_kept, max_results=sample_size * 2)
    sampled = candidates[:sample_size]

    regressions = []
    detail = []
    for c in sampled:
        skill = c['skill']
        baseline = _get_skill_baseline(skill, window=5)
        current = _get_skill_current_score(skill)
        delta = (current - baseline) if (current is not None and baseline is not None) else None

        entry = {
            'skill': skill,
            'confidence': c['confidence'],
            'reasons': c['reasons'],
            'baseline_score': baseline,
            'current_score': current,
            'delta': round(delta, 2) if delta is not None else None,
        }
        detail.append(entry)

        if delta is not None and delta < -regression_threshold:
            regressions.append({
                'skill': skill,
                'current_score': current,
                'baseline_score': baseline,
                'delta': round(delta, 2),
                'reasons': c['reasons'],
            })

    return {
        'timestamp': timestamp,
        'audit_id': audit_id,
        'skill_kept': skill_kept,
        'sample_size': sample_size,
        'regression_threshold': regression_threshold,
        'downstream_checked': [c['skill'] for c in sampled],
        'sampled': detail,
        'regressions': regressions,
        'flag': len(regressions) > 0,
    }


def log_cascade_audit(result: dict) -> Path:
    """Persist cascade audit to evolution_store/cascade_audits/ and mirror
    into v3 trace log for Karpathy search-set integration.
    """
    audit_id = result.get('audit_id') or datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"audit_{audit_id}.json"
    filepath = CASCADE_DIR / filename

    with open(filepath, 'w') as f:
        json.dump(result, f, indent=2)

    # Mirror into v3 tracer
    try:
        from evolution_tracer import log_trace
        failure_signals = [
            {
                'step': 'cascade_audit',
                'signal_type': 'downstream_regression',
                'severity': 'major',
                'description': f"{r['skill']}: baseline {r['baseline_score']} → current {r['current_score']} (delta {r['delta']}); reasons {r['reasons']}",
            }
            for r in result.get('regressions', [])
        ]
        composite = 10.0 if not result.get('flag') else max(
            0.0,
            round(10.0 - 2.0 * len(result.get('regressions', [])), 2),
        )
        log_trace(
            component=f"cascade_audit/{audit_id}",
            operation='cascade_audit',
            quality_score=composite,
            notes=(
                f"Cascade audit for {result.get('skill_kept')}: "
                f"sampled {len(result.get('downstream_checked', []))}, "
                f"{len(result.get('regressions', []))} regression(s)"
            ),
            failure_signals=failure_signals,
            context={
                'audit_id': audit_id,
                'skill_kept': result.get('skill_kept'),
                'downstream_checked': result.get('downstream_checked', []),
                'flag': result.get('flag', False),
            },
        )
    except Exception as e:
        print(f"  ⚠️  Could not mirror to evolution_tracer: {e}")

    return filepath


def rebuild_cascade_graph() -> dict:
    """Full cascade relationship graph across all skills. Cached for later reads."""
    all_skills = _all_skill_names()
    graph = {
        'generated_at': datetime.now().isoformat(),
        'skill_count': len(all_skills),
        'reference_index': {k: sorted(v) for k, v in build_reference_index().items() if len(v) > 1},
        'expert_clusters': {},
    }
    clusters: dict[str, list[str]] = {}
    for s in all_skills:
        expert = extract_expert(s, all_skills)
        if expert:
            clusters.setdefault(expert, []).append(s)
    graph['expert_clusters'] = {k: sorted(v) for k, v in clusters.items() if len(v) > 1}
    CASCADE_GRAPH.write_text(json.dumps(graph, indent=2))
    return graph


# ─── Pretty printing ─────────────────────────────────────────────

def _print_related(skill: str, related: list) -> None:
    print(f"\n{'='*66}")
    print(f"  DOWNSTREAM SKILLS — {skill}")
    print(f"{'='*66}")
    if not related:
        print("  No downstream relationships detected.")
    else:
        for r in related:
            print(f"  {r['confidence']:>5.2f}  {r['skill']}")
            for reason in r['reasons']:
                print(f"         └─ {reason}")
    print(f"{'='*66}\n")


def _print_cascade_audit(audit: dict) -> None:
    flag = "🚨 REGRESSION DETECTED" if audit['flag'] else "✅"
    print(f"\n{'='*66}")
    print(f"  CASCADE AUDIT — {audit['audit_id']}  {flag}")
    print(f"{'='*66}")
    print(f"  KEPT skill:   {audit['skill_kept']}")
    print(f"  Sampled:      {len(audit['sampled'])} downstream skills")
    print(f"  Regressions:  {len(audit['regressions'])}")
    print(f"{'─'*66}")
    for s in audit['sampled']:
        base = s['baseline_score'] if s['baseline_score'] is not None else '—'
        cur = s['current_score'] if s['current_score'] is not None else '—'
        delta = s['delta'] if s['delta'] is not None else '—'
        marker = '🔴' if (s['delta'] is not None and s['delta'] < -0.5) else '✅' if s['delta'] is not None else '⚪'
        print(f"  {marker} {s['skill']:45} base {base}  cur {cur}  Δ {delta}")
    print(f"{'='*66}\n")


def _print_history(limit: int = 20) -> None:
    files = sorted(CASCADE_DIR.glob("audit_*.json"), reverse=True)[:limit]
    if not files:
        print("  No cascade audits found.")
        return
    print(f"\n{'='*66}")
    print(f"  CASCADE AUDIT HISTORY ({len(files)} most recent)")
    print(f"{'='*66}")
    for f in files:
        try:
            a = json.loads(f.read_text())
        except Exception:
            continue
        flag = '🚨' if a.get('flag') else '✅'
        print(f"  {flag} {a.get('audit_id','?')} | kept: {a.get('skill_kept','?'):40} | regressions: {len(a.get('regressions', []))}")
    print(f"{'='*66}\n")


# ─── CLI ────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Cascade Detector CLI")
    sub = parser.add_subparsers(dest='command')

    check_p = sub.add_parser('check', help='Run cascade impact check for a skill')
    check_p.add_argument('skill', help='Skill that was just KEPT')
    check_p.add_argument('--sample', type=int, default=3, help='Downstream sample size')
    check_p.add_argument('--no-log', action='store_true', help='Do not persist result')

    rel_p = sub.add_parser('related', help='Show downstream graph for a skill')
    rel_p.add_argument('skill', help='Skill to analyze')
    rel_p.add_argument('--max', type=int, default=10, help='Max downstream skills to return')

    hist_p = sub.add_parser('history', help='Recent cascade audits')
    hist_p.add_argument('--limit', type=int, default=20)

    sub.add_parser('graph', help='Rebuild cascade relationship graph cache')

    args = parser.parse_args()

    if args.command == 'check':
        audit = check_cascade_impact(args.skill, sample_size=args.sample)
        _print_cascade_audit(audit)
        if not args.no_log:
            path = log_cascade_audit(audit)
            print(f"  Logged: {path.name}")

    elif args.command == 'related':
        related = find_downstream_skills(args.skill, max_results=args.max)
        _print_related(args.skill, related)

    elif args.command == 'history':
        _print_history(args.limit)

    elif args.command == 'graph':
        graph = rebuild_cascade_graph()
        print(f"  Cascade graph rebuilt: {CASCADE_GRAPH}")
        print(f"  Skills:              {graph['skill_count']}")
        print(f"  Expert clusters:     {len(graph['expert_clusters'])}")
        print(f"  Shared-ref files:    {len(graph['reference_index'])}")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
