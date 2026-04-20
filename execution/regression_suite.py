#!/usr/bin/env python3
"""
Regression Suite — Golden-set silent-degradation detector for Antigravity.

Phase 2 (Skill Evolution) currently shows a 100% KEEP rate across 100+ cycles.
Either the system is genuinely perfect (unlikely) or silent degradation is
going undetected. Per Nate B Jones GP-12 (Silent Degradation): quality erosion
that persists undetected because monitoring wasn't designed for autonomous edits.

This module implements a canonical golden-set regression audit:
  • GOLDEN_SET is a permanent artifact — 5-7 canonical tasks per domain
  • Each task carries an expected_range (min, target) — tight enough to catch
    regression, loose enough to absorb normal variance
  • Audits compare current-state scores against expected_min
  • Results are logged as v3 traces via evolution_tracer so regressions feed
    back into the Karpathy search set

Usage:
    python execution/regression_suite.py audit                      # full audit
    python execution/regression_suite.py audit --domain copywriting # single domain
    python execution/regression_suite.py audit --dry-run            # inventory only
    python execution/regression_suite.py history --limit 10         # recent audits
    python execution/regression_suite.py trend --domain content     # trend analysis
    python execution/regression_suite.py log-result --audit-id X \
        --domain copywriting --task-idx 0 --score 7.8               # manual score
"""

import os
import json
import argparse
from datetime import datetime, timedelta, date
from pathlib import Path
from typing import Optional

# ─── Paths & imports ────────────────────────────────────────────
PROJECT_ROOT = Path(__file__).parent.parent
AUDIT_DIR = PROJECT_ROOT / "evolution_store" / "regression_audits"
BASELINE_FILE = AUDIT_DIR / "baseline.json"
AUDIT_DIR.mkdir(parents=True, exist_ok=True)

import sys
sys.path.insert(0, str(Path(__file__).parent))


# ─── Golden Set — canonical tasks per domain ────────────────────
# Each task represents a core competence, not an edge case. expected_range
# = (minimum_acceptable, expected_target). Scores at or above expected_min
# PASS; 0-0.5 below = WARNING; more than 0.5 below = REGRESSION.
#
# Tasks are DISTINCT from skill_benchmark.BENCHMARK_TASKS — those drive
# evolution, these detect regression. No overlap.
#
# expected_range authoring: upper bound = score an expert workflow should
# hit on a calibrated day; lower bound = expected - 1.0 (absorbs variance).

GOLDEN_SET = {
    'copywriting': [
        {
            'task': 'Write a direct-response sales letter opener (first 200 words) for a $97 info product on email deliverability, cold traffic.',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'Classic DR fundamentals — should score strong on hook, pattern interrupt, problem agitation.',
        },
        {
            'task': 'Draft a cold outreach email to a VP Marketing at a Series B SaaS (ARR ~$30M) pitching a $5K/mo content retainer. Single email, <150 words, must earn a reply.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Specificity test — generic cold email patterns fail this; domain voice + proof signals succeed.',
        },
        {
            'task': 'Write a 3-line PPC ad (headline, body, CTA) for a $27/mo stock research tool targeting retail investors aged 35-55 worried about market volatility.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Constrained character-count copy — tests brevity + emotional precision.',
        },
        {
            'task': 'Rewrite this weak subject line into 5 variations that maintain the offer but escalate curiosity: "Our new product launch is here."',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'Diagnostic — weak input forces the writer to carry the load. Expert copy shows range.',
        },
        {
            'task': 'Write the opening 150 words of a VSL for a $497 info product on "how to land your first consulting client in 30 days" — cold traffic, warm avatar (laid-off middle manager).',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'Full-stack copy test — hook + pattern interrupt + identity mirror must fire in first 15 seconds.',
        },
        {
            'task': 'Turn this raw testimonial into a two-sentence social proof callout for a landing page: "Before I started using this, I was spending 10 hours a week on reports. Now I spend 2. My boss actually noticed and gave me the promotion I had been chasing for 2 years."',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Proof compression test — specificity + transformation arc must survive the cut.',
        },
    ],

    'content': [
        {
            'task': 'Write a LinkedIn post (180-220 words) for a solo consultant sharing a counterintuitive lesson from a client engagement. Must drive substantive comments, not reactions.',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'LinkedIn-native content test — platform constraints + psychological specificity.',
        },
        {
            'task': 'Write a Twitter/X thread opener (first 3 posts) on "the real reason most creators plateau at 10K followers" — must sound like a practitioner, not a guru.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Voice calibration test — generic advice fails, lived-experience signals succeed.',
        },
        {
            'task': 'Draft a TikTok hook + opening 15 seconds for a personal finance creator targeting renters in their late 20s who feel locked out of homeownership.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Short-form video hook test — pattern interrupt + scroll-stop mechanics.',
        },
        {
            'task': 'Write a YouTube video title + 3 thumbnail-text candidates for a 12-minute video titled "Why I Fired My First Three Clients."',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Packaging test — title/thumbnail is 80% of YT performance.',
        },
        {
            'task': 'Outline a 400-word newsletter edition on "the compounding cost of saying yes to the wrong clients" — tone: dispatches from a practitioner, not a lecturer.',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'Long-form content architecture test — structure + voice must both fire.',
        },
        {
            'task': 'Generate 5 hooks for a single insight: "most productivity advice is solving the wrong problem — the issue is not time management, it is energy management."',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'Hook volume test — weak writers produce variations on one angle, expert writers produce range.',
        },
    ],

    'strategy': [
        {
            'task': 'Write a one-page positioning statement (~300 words) for a solo fractional CMO targeting Series A-B SaaS companies spending $20K-$80K/mo on content but seeing <2x pipeline contribution.',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'Positioning test — specificity of ICP + mechanism + differentiation must all land.',
        },
        {
            'task': 'Design a 60-day go-to-market plan for a $2,997 cohort course teaching AI automation to marketing operators, zero prior audience, founder has 8 years of in-house ops experience.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'GTM test — constrained inputs force strategy not template. Audience-build vs. authority-build tradeoff must surface.',
        },
        {
            'task': 'Identify the 3 biggest structural weaknesses in Zapier\'s positioning for solo operators in 2026, and propose how a new entrant could exploit them.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Competitive intelligence test — observable market dynamics, not generic SWOT.',
        },
        {
            'task': 'Write a pricing architecture (tiers, anchors, upsells) for a productized ghostwriting service selling to Series A-B founders. Target ARPU $8K/mo.',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'Monetization architecture test — tiers must encode different buyer psychology, not just price points.',
        },
        {
            'task': 'Diagnose why a $500K-ARR personal-brand consultancy has been stuck at the same revenue for 18 months, given: founder is the only operator, inbound driven, 60% closing rate on qualified calls, 2-3 calls/week.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Business diagnosis test — constraint analysis + intervention sequencing.',
        },
    ],

    'sales': [
        {
            'task': 'Handle this live objection: "I need to think about it" — prospect is a $2M-ARR founder evaluating a $15K/mo content retainer. You are on a Zoom call, already 45 min in.',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'Live objection handling — real-talk vs. scripted manipulation separates expert from generic.',
        },
        {
            'task': 'Write a 4-email nurture sequence for a lead who downloaded a free guide titled "5 Mistakes First-Time SaaS Founders Make With Pricing." Goal: book a $1K strategy call.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Email sequence architecture — each email must earn the next open, escalate commitment.',
        },
        {
            'task': 'Design a 30-minute discovery call outline for qualifying leads for a $50K 6-month consulting engagement. Must eliminate tire-kickers by minute 15.',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'Discovery call design — budget/authority/need/timing must surface naturally, not interrogatively.',
        },
        {
            'task': 'Write a cold LinkedIn DM opener (<80 words) to a VP of Sales at a 300-employee B2B SaaS, pitching a $30K annual sales-enablement audit.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Cold DM test — must earn the second message, not pitch the product.',
        },
        {
            'task': 'Turn this live call objection into a reframe: "Honestly, my CEO said no to budget increases this quarter." — you are pitching a $6K/mo retainer.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Reframe mechanics — budget objection is rarely a budget objection. Expert salesperson isolates the real constraint.',
        },
    ],

    'research': [
        {
            'task': 'Build a consumer persona for a first-time buyer of a $3K+ productivity coaching program. Focus on the pre-purchase window: triggers, objections, emotional state, search behavior.',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'Persona depth test — generic demographic vs. psychographic specificity separates junior from expert research.',
        },
        {
            'task': 'Map the top 3 underserved niches in the AI-automation market where Zapier and Make have structural weaknesses. Include TAM estimate + entry cost for each.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Market intelligence test — structural reasoning, not surface trend-spotting.',
        },
        {
            'task': 'Conduct a competitive analysis of the 5 largest AI writing tools for marketing teams in 2026. Identify the dimension of differentiation each is implicitly competing on.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Positioning analysis test — "what game are they actually playing" is the tier-1 question.',
        },
        {
            'task': 'Validate the thesis that "first-time home buyers in LA earning $150K+ household income are increasingly delaying purchase past age 38" — use public data + stated behavior + revealed behavior.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Multi-source validation test — triangulation beats single-source.',
        },
        {
            'task': 'Write a 400-word market synthesis on how the productized-services category is likely to evolve 2026-2028 given AI coding + commoditization of agency deliverables.',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'Synthesis test — compresses multiple trend vectors into actionable foresight.',
        },
    ],

    'brand': [
        {
            'task': 'Develop a positioning statement for the personal brand of a corporate lawyer pivoting to content creation about M&A deal structure, targeting mid-market founders ($10M-$100M ARR).',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'Pivot positioning — credibility transfer + audience-narrowing test.',
        },
        {
            'task': 'Write a 250-word brand voice guide for a $497/mo paid community for female founders scaling $1M→$10M ARR. Must avoid both hustle-culture and soft-empowerment tropes.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Voice precision test — negative constraints force specificity.',
        },
        {
            'task': 'Design a 4-pillar content strategy for an ex-FAANG engineering leader building a personal brand on AI engineering + founder storytelling, targeting CTOs and VPs of Engineering.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Pillar architecture test — pillars must be non-overlapping, non-redundant, audience-serving.',
        },
        {
            'task': 'Write the About section (300 words, second-person) for the personal website of a freelance creative strategist who has worked on campaigns for Liquid Death, Duolingo, and Notion.',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'About section craft — reader-as-protagonist test. Writing about the writer fails this.',
        },
        {
            'task': 'Create a naming shortlist (5 candidates) for a new newsletter about "the quiet craft of running a profitable solo business" targeting practitioners $200K-$1M ARR.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Naming craft — memorability + category signal + ownability all required.',
        },
    ],

    'default': [
        {
            'task': 'Write a one-page executive summary (400 words) of your domain expertise tailored to a CEO who has 3 minutes to read it and must decide whether to engage your services.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Executive-summary test — compression + credibility + CTA discipline.',
        },
        {
            'task': 'Design a 5-question self-assessment a prospect could take to determine if they need your services. Each question must segment seriously vs casually interested.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Qualification mechanism test — good questions force honest self-diagnosis.',
        },
        {
            'task': 'Write a "first 30 days" document for a new client who just hired you. Sequenced, actionable, demonstrates domain mastery without being rote.',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'Onboarding artifact — proves delivery craft, sets expectations, reduces buyer\'s remorse.',
        },
        {
            'task': 'Outline a 20-minute talk you would give at a professional conference to introduce your domain expertise to adjacent professionals. 3 main beats, 1 memorable example per beat.',
            'expected_range': (7.0, 8.5),
            'authored_date': '2026-04-20',
            'notes': 'Teaching architecture — structure + memorability + applicability for non-specialist audience.',
        },
        {
            'task': 'Write a 250-word manifesto for the point of view your practice is built on. Must state what you believe, why, and what you refuse to do because of that belief.',
            'expected_range': (7.5, 9.0),
            'authored_date': '2026-04-20',
            'notes': 'Conviction test — bland affirmations fail. Real practitioners have real refusals.',
        },
    ],
}


# ─── Status classification ──────────────────────────────────────

def _classify_status(current_score: Optional[float], expected_min: float) -> str:
    """PASS / WARNING / REGRESSION / NO_DATA based on current vs expected_min."""
    if current_score is None:
        return "NO_DATA"
    if current_score >= expected_min:
        return "PASS"
    if current_score >= expected_min - 0.5:
        return "WARNING"
    return "REGRESSION"


# ─── Proxy scoring from Performance Log ─────────────────────────

def _get_domain_proxy_score(domain: str, days: int = 30) -> Optional[float]:
    """Pull the rolling average quality_score for a domain from Performance Log.

    Used as a proxy when no task-specific score is available. Proxy is
    informational, flagged via scoring_method="proxy_from_log".

    Returns None if Notion is unreachable or no data. Silent fallback —
    regression suite should not break on infrastructure issues.
    """
    try:
        from skill_benchmark import detect_domain
        from notion_api import NotionAPI
        db_id = os.getenv("NOTION_DB_PERFORMANCE", "31f49875a89781dbb599dee5e7961b5c")
        api = NotionAPI()
        cutoff = (date.today() - timedelta(days=days)).isoformat()
        result = api.query_database(
            db_id,
            filter={
                "and": [
                    {"property": "Date", "date": {"after": cutoff}},
                    {"property": "Quality Score", "number": {"is_not_empty": True}},
                ]
            },
            page_size=100,
        )
        scores = []
        for page in result.get("results", []):
            props = page.get("properties", {})
            skill_text = ""
            skill_prop = props.get("Skill", {})
            if skill_prop.get("rich_text"):
                skill_text = skill_prop["rich_text"][0].get("plain_text", "")
            if skill_text and detect_domain(skill_text) != domain:
                continue
            q = props.get("Quality Score", {}).get("number")
            if q is not None:
                scores.append(q)
        if not scores:
            return None
        return round(sum(scores) / len(scores), 2)
    except Exception:
        return None


# ─── Audit core ──────────────────────────────────────────────────

def run_regression_audit(
    domains: Optional[list] = None,
    sample_per_domain: int = 3,
    use_proxy: bool = True,
) -> dict:
    """Run golden-set tasks against current skills in the specified domains.

    Deterministic sampling: selects the first `sample_per_domain` tasks per
    domain so audits are comparable across runs. Override by rotating later
    if needed.

    Scoring is non-executing by design: pulls proxy scores from the most
    recent Performance Log entries in each domain. Manual scores can be
    merged via `log_regression_result`.

    Returns:
      {
        'timestamp': iso, 'audit_id': str, 'audit_type': 'regression',
        'results': [{domain, task, expected_min, expected_target,
                     current_score, delta, status, scoring_method}, ...],
        'summary': {total_run, passed, warnings, regressions, no_data},
        'blocking': bool,  # any regression
      }
    """
    timestamp = datetime.now().isoformat()
    audit_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    target_domains = domains if domains else list(GOLDEN_SET.keys())
    results = []

    # Cache proxy scores per domain to avoid repeated Notion calls
    proxy_cache: dict[str, Optional[float]] = {}

    for dom in target_domains:
        if dom not in GOLDEN_SET:
            continue
        tasks = GOLDEN_SET[dom][:sample_per_domain]

        if use_proxy and dom not in proxy_cache:
            proxy_cache[dom] = _get_domain_proxy_score(dom)
        proxy = proxy_cache.get(dom) if use_proxy else None

        for task_spec in tasks:
            expected_min, expected_target = task_spec['expected_range']
            current_score = proxy  # will be overridden by manual scores via log_regression_result
            status = _classify_status(current_score, expected_min)
            delta = round((current_score - expected_min), 2) if current_score is not None else None

            results.append({
                'domain': dom,
                'task': task_spec['task'],
                'expected_min': expected_min,
                'expected_target': expected_target,
                'current_score': current_score,
                'delta': delta,
                'status': status,
                'scoring_method': 'proxy_from_log' if current_score is not None else 'pending_manual',
                'notes': task_spec.get('notes', ''),
            })

    summary = {
        'total_run': len(results),
        'passed': sum(1 for r in results if r['status'] == 'PASS'),
        'warnings': sum(1 for r in results if r['status'] == 'WARNING'),
        'regressions': sum(1 for r in results if r['status'] == 'REGRESSION'),
        'no_data': sum(1 for r in results if r['status'] == 'NO_DATA'),
    }

    return {
        'timestamp': timestamp,
        'audit_id': audit_id,
        'audit_type': 'regression',
        'domains_audited': target_domains,
        'sample_per_domain': sample_per_domain,
        'results': results,
        'summary': summary,
        'blocking': summary['regressions'] > 0,
    }


def log_regression_result(result: dict) -> Path:
    """Persist audit result to evolution_store/regression_audits/ and
    mirror into v3 trace log for Karpathy search-set integration.
    """
    audit_id = result.get('audit_id') or datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"audit_{audit_id}.json"
    filepath = AUDIT_DIR / filename

    with open(filepath, 'w') as f:
        json.dump(result, f, indent=2)

    # Update rolling baseline if audit passed
    if not result.get('blocking'):
        _update_baseline(result)

    # Mirror into v3 tracer so regressions feed into Karpathy search set
    try:
        from evolution_tracer import log_trace
        summary = result.get('summary', {})
        composite = _summary_to_composite(summary)
        failure_signals = [
            {
                'step': 'regression_audit',
                'signal_type': 'domain_regression',
                'severity': 'major' if r['status'] == 'REGRESSION' else 'minor',
                'description': f"{r['domain']}: current {r['current_score']} vs expected_min {r['expected_min']} (delta {r.get('delta')})",
            }
            for r in result.get('results', [])
            if r['status'] == 'REGRESSION'
        ]
        log_trace(
            component=f"regression_audit/{audit_id}",
            operation='regression_audit',
            quality_score=composite,
            notes=(
                f"Regression audit: {summary.get('passed',0)} pass / "
                f"{summary.get('warnings',0)} warn / {summary.get('regressions',0)} regress / "
                f"{summary.get('no_data',0)} no-data"
            ),
            failure_signals=failure_signals,
            context={
                'audit_id': audit_id,
                'domains': result.get('domains_audited', []),
                'blocking': result.get('blocking', False),
            },
        )
    except Exception as e:
        print(f"  ⚠️  Could not mirror to evolution_tracer: {e}")

    return filepath


def _summary_to_composite(summary: dict) -> float:
    """Rough composite for trace logging — proportion of PASS out of run."""
    total = summary.get('total_run', 0)
    if not total:
        return 0.0
    passed = summary.get('passed', 0)
    warnings = summary.get('warnings', 0)
    return round(10.0 * (passed + 0.5 * warnings) / total, 2)


def _update_baseline(result: dict) -> None:
    """Update the rolling baseline with this passing audit's scores."""
    baseline = {}
    if BASELINE_FILE.exists():
        try:
            baseline = json.loads(BASELINE_FILE.read_text())
        except Exception:
            baseline = {}
    baseline.setdefault('history', []).append({
        'audit_id': result.get('audit_id'),
        'timestamp': result.get('timestamp'),
        'summary': result.get('summary'),
    })
    # Keep last 50
    baseline['history'] = baseline['history'][-50:]
    baseline['last_passing'] = result.get('audit_id')
    baseline['last_updated'] = datetime.now().isoformat()
    BASELINE_FILE.write_text(json.dumps(baseline, indent=2))


def compare_to_baseline(domain: str, task: str, limit: int = 5) -> dict:
    """Given a domain+task, read last N regression audits and return trend."""
    matches = []
    for audit_file in sorted(AUDIT_DIR.glob("audit_*.json"), reverse=True):
        try:
            audit = json.loads(audit_file.read_text())
        except Exception:
            continue
        for r in audit.get('results', []):
            if r.get('domain') == domain and r.get('task', '').strip() == task.strip():
                matches.append({
                    'audit_id': audit.get('audit_id'),
                    'timestamp': audit.get('timestamp'),
                    'current_score': r.get('current_score'),
                    'status': r.get('status'),
                })
                break
        if len(matches) >= limit:
            break

    trend = 'insufficient_data'
    scores = [m['current_score'] for m in matches if m['current_score'] is not None]
    if len(scores) >= 3:
        recent = sum(scores[:len(scores)//2]) / max(len(scores)//2, 1)
        older = sum(scores[len(scores)//2:]) / max(len(scores) - len(scores)//2, 1)
        delta = recent - older
        if delta > 0.3:
            trend = 'improving'
        elif delta < -0.3:
            trend = 'declining'
        else:
            trend = 'stable'

    return {
        'domain': domain,
        'task': task,
        'sample_size': len(matches),
        'scores': scores,
        'trend': trend,
        'matches': matches,
    }


def merge_manual_score(audit_id: str, domain: str, task_idx: int, score: float, scorer: str = '') -> dict:
    """Update a saved audit with a manually-scored result."""
    filepath = AUDIT_DIR / f"audit_{audit_id}.json"
    if not filepath.exists():
        raise FileNotFoundError(f"No audit found with id {audit_id}")
    audit = json.loads(filepath.read_text())

    # Find the target result by domain + index
    domain_indices = [i for i, r in enumerate(audit['results']) if r['domain'] == domain]
    if task_idx >= len(domain_indices):
        raise IndexError(f"task_idx {task_idx} out of range for domain {domain} (has {len(domain_indices)} tasks)")

    target = audit['results'][domain_indices[task_idx]]
    target['current_score'] = score
    target['delta'] = round(score - target['expected_min'], 2)
    target['status'] = _classify_status(score, target['expected_min'])
    target['scoring_method'] = 'manual'
    if scorer:
        target['scorer'] = scorer

    # Recompute summary + blocking
    audit['summary'] = {
        'total_run': len(audit['results']),
        'passed': sum(1 for r in audit['results'] if r['status'] == 'PASS'),
        'warnings': sum(1 for r in audit['results'] if r['status'] == 'WARNING'),
        'regressions': sum(1 for r in audit['results'] if r['status'] == 'REGRESSION'),
        'no_data': sum(1 for r in audit['results'] if r['status'] == 'NO_DATA'),
    }
    audit['blocking'] = audit['summary']['regressions'] > 0
    audit['last_updated'] = datetime.now().isoformat()

    filepath.write_text(json.dumps(audit, indent=2))
    return audit


# ─── Pretty printing ─────────────────────────────────────────────

def _print_audit(audit: dict) -> None:
    s = audit['summary']
    blocker = "🚨 BLOCKING" if audit['blocking'] else "✅"
    print(f"\n{'='*66}")
    print(f"  REGRESSION AUDIT — {audit['audit_id']}  {blocker}")
    print(f"{'='*66}")
    print(f"  Domains: {', '.join(audit['domains_audited'])}")
    print(f"  Tasks:   {s['total_run']}  |  PASS {s['passed']}  WARN {s['warnings']}  REGRESS {s['regressions']}  NO_DATA {s['no_data']}")
    print(f"{'─'*66}")
    for r in audit['results']:
        marker = {'PASS': '✅', 'WARNING': '🟡', 'REGRESSION': '🔴', 'NO_DATA': '⚪'}[r['status']]
        score = f"{r['current_score']}" if r['current_score'] is not None else "—"
        expected = f"[{r['expected_min']}-{r['expected_target']}]"
        print(f"  {marker} {r['domain']:13} {score:>5}/10 exp {expected:13} | {r['task'][:55]}")
    print(f"{'='*66}\n")


def _print_inventory() -> None:
    print(f"\n{'='*66}")
    print(f"  GOLDEN SET INVENTORY")
    print(f"{'='*66}")
    total = 0
    for dom, tasks in GOLDEN_SET.items():
        print(f"  {dom:13} {len(tasks):>2} tasks")
        total += len(tasks)
    print(f"{'─'*66}")
    print(f"  TOTAL        {total:>2} tasks across {len(GOLDEN_SET)} domains")
    print(f"{'='*66}\n")


def _print_history(limit: int = 10) -> None:
    files = sorted(AUDIT_DIR.glob("audit_*.json"), reverse=True)[:limit]
    if not files:
        print("  No prior audits found.")
        return
    print(f"\n{'='*66}")
    print(f"  REGRESSION AUDIT HISTORY ({len(files)} most recent)")
    print(f"{'='*66}")
    for f in files:
        try:
            a = json.loads(f.read_text())
        except Exception:
            continue
        s = a.get('summary', {})
        blocker = "🚨" if a.get('blocking') else "✅"
        print(f"  {blocker} {a.get('audit_id','?')} | {s.get('passed',0)}P/{s.get('warnings',0)}W/{s.get('regressions',0)}R/{s.get('no_data',0)}N | {len(a.get('domains_audited',[]))} domains")
    print(f"{'='*66}\n")


# ─── CLI ────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Regression Suite CLI")
    sub = parser.add_subparsers(dest='command')

    audit_p = sub.add_parser('audit', help='Run regression audit')
    audit_p.add_argument('--domain', default=None, help='Single domain (default: all)')
    audit_p.add_argument('--sample', type=int, default=3, help='Tasks per domain (default 3)')
    audit_p.add_argument('--dry-run', action='store_true', help='Inventory only, no scoring')
    audit_p.add_argument('--no-proxy', action='store_true', help='Skip proxy-score lookup')
    audit_p.add_argument('--no-log', action='store_true', help='Do not persist result')

    hist_p = sub.add_parser('history', help='Show prior audit results')
    hist_p.add_argument('--limit', type=int, default=10)

    trend_p = sub.add_parser('trend', help='Trend analysis')
    trend_p.add_argument('--domain', required=True)
    trend_p.add_argument('--task-idx', type=int, default=0, help='Which task (0-based)')
    trend_p.add_argument('--limit', type=int, default=5)

    log_p = sub.add_parser('log-result', help='Merge a manually-scored result')
    log_p.add_argument('--audit-id', required=True)
    log_p.add_argument('--domain', required=True)
    log_p.add_argument('--task-idx', type=int, required=True)
    log_p.add_argument('--score', type=float, required=True)
    log_p.add_argument('--scorer', default='')

    args = parser.parse_args()

    if args.command == 'audit':
        if args.dry_run:
            _print_inventory()
            return
        domains = [args.domain] if args.domain else None
        audit = run_regression_audit(
            domains=domains,
            sample_per_domain=args.sample,
            use_proxy=not args.no_proxy,
        )
        _print_audit(audit)
        if not args.no_log:
            path = log_regression_result(audit)
            print(f"  Logged: {path.name}")
            if audit['blocking']:
                print(f"  🚨 BLOCKING: {audit['summary']['regressions']} domain regression(s) detected.")

    elif args.command == 'history':
        _print_history(args.limit)

    elif args.command == 'trend':
        if args.domain not in GOLDEN_SET:
            print(f"  Unknown domain: {args.domain}. Valid: {list(GOLDEN_SET.keys())}")
            return
        task = GOLDEN_SET[args.domain][args.task_idx]['task']
        trend = compare_to_baseline(args.domain, task, limit=args.limit)
        print(f"\n  Domain: {trend['domain']}")
        print(f"  Task:   {trend['task'][:70]}…")
        print(f"  Sample: {trend['sample_size']} audits | Scores: {trend['scores']}")
        print(f"  Trend:  {trend['trend']}\n")

    elif args.command == 'log-result':
        updated = merge_manual_score(
            args.audit_id, args.domain, args.task_idx, args.score, args.scorer
        )
        print(f"  Updated audit {args.audit_id}")
        _print_audit(updated)

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
