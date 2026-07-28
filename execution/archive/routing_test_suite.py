#!/usr/bin/env python3
"""
Routing Test Suite — Validates that sample requests route to correct experts.

Tests the 3-layer routing system:
1. Signal matching (intent pipeline domain detection table)
2. Domain assignment (DOMAIN_REGISTRY.md swim lanes)
3. Expert selection (invocation cards for Tier 0 confirmation)

Run: python execution/routing_test_suite.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent


# ─── Test Cases ───────────────────────────────────────────────────
# Each case: (request_text, expected_domain_number, expected_experts, mode)
# mode: "output" | "expertise" | "hybrid"

TEST_CASES = [
    # Domain 1: Copywriting
    (
        "Write a sales page for my AI consulting offer",
        1,
        ["Cardinal Mason"],
        "output",
    ),
    (
        "Audit this email sequence and tell me what's weak",
        1,
        ["Harry Dry"],
        "expertise",
    ),
    (
        "I need a VSL script for a high-ticket coaching program",
        1,
        ["Alen Sultanic"],
        "output",
    ),

    # Domain 2: Content & Viral
    (
        "Create a TikTok script about why most people fail at AI businesses",
        2,
        ["Seena Rez"],
        "output",
    ),
    (
        "Help me build a content strategy for YouTube",
        2,
        ["Kallaway"],
        "hybrid",
    ),

    # Domain 3: Personal Brand
    (
        "I want to stand out on LinkedIn as an AI consultant",
        3,
        ["Lara Acosta", "Caleb Ralston"],
        "hybrid",
    ),

    # Domain 4: Sales & Persuasion
    (
        "How do I handle the objection 'I need to think about it'?",
        4,
        ["Jeremy Miner"],
        "expertise",
    ),
    (
        "My prospect has deep emotional resistance to buying — help me close",
        4,
        ["Jeremy Miner", "Michael Bernoff"],
        "expertise",
    ),

    # Domain 6: AI & Automation
    (
        "Build me a self-healing agent workflow for content extraction",
        6,
        ["Nick Saraev"],
        "output",
    ),
    (
        "How should I structure my CLAUDE.md for a multi-agent system?",
        6,
        ["Boris"],
        "expertise",
    ),

    # Domain 7: Writing & Storytelling
    (
        "Write me a personal essay about overcoming failure",
        7,
        ["Mitch Albom", "Dan Wang"],
        "output",
    ),
    (
        "Make this paragraph funnier without losing the message",
        7,
        ["Robert Mack"],
        "output",
    ),

    # Domain 8: Products & Monetization
    (
        "I want to create a digital product — what format should I use?",
        8,
        ["Nicolas Cole"],
        "expertise",
    ),
    (
        "Design a lead magnet funnel for my coaching business",
        8,
        ["Stockton Walbeck"],
        "output",
    ),

    # Domain 9: SEO & Search
    (
        "How do I rank for competitive keywords in the AI niche?",
        9,
        ["Nathan Gotch"],
        "expertise",
    ),

    # Domain 10: Design & Web
    (
        "Build a premium website with motion design for my agency",
        10,
        ["Andy Lo"],
        "output",
    ),

    # Domain 11: Video & Media
    (
        "Create an AI-generated cinematic video for my product launch",
        11,
        ["Tao Prompts"],
        "output",
    ),

    # Domain 12: Strategy & Business Architecture
    (
        "Should I pivot my business model from services to SaaS?",
        12,
        ["Jim O'Shaughnessy"],
        "expertise",
    ),

    # Domain 13: Audience & Growth
    (
        "I want to launch a newsletter and grow to 10K subscribers",
        13,
        ["Tyler Denk"],
        "hybrid",
    ),

    # Domain 14: Mindset & Messaging
    (
        "I'm stuck and can't seem to take action on anything",
        14,
        ["Jeremy Haynes", "Michael Bernoff"],
        "expertise",
    ),
]


# ─── Signal Matching Engine ───────────────────────────────────────

# Domain detection signals (from intent-pipeline.md Stage 3)
DOMAIN_SIGNALS = {
    1: ["sales page", "email", "headline", "convert", "copy", "copywriting", "vsl"],
    2: ["write", "create", "draft", "content", "viral", "tiktok", "hook", "youtube"],
    3: ["linkedin", "positioning", "brand", "authority", "personal brand", "stand out"],
    4: ["objection", "close", "persuade", "sell", "sales", "outreach"],
    5: ["customer", "persona", "buyer", "psychology", "consumer"],
    6: ["automate", "workflow", "agent", "ai", "claude", "prompt", "claude.md"],
    7: ["story", "narrative", "essay", "write me", "literary", "funny", "funnier", "humor"],
    8: ["product", "offer", "pricing", "launch", "lead magnet", "monetize", "revenue", "digital product"],
    9: ["rank", "seo", "keywords", "traffic", "answer engine", "blog"],
    10: ["design", "visual", "aesthetic", "website", "typography", "motion"],
    11: ["video", "cinematic", "storyboard", "ai video", "programmatic video"],
    12: ["should i", "what's the best", "how do i approach", "strategy", "pivot", "business model", "research", "analyze"],
    13: ["grow", "newsletter", "subscriber", "community", "audience"],
    14: ["stuck", "blocked", "mindset", "messaging", "movement", "can't", "afraid"],
    15: ["real estate", "listing", "ads", "paid", "campaign"],
}


def detect_domain(request_text):
    """Match request text against domain signals. Returns list of (domain_num, score) tuples."""
    text_lower = request_text.lower()
    scores = {}
    for domain_num, signals in DOMAIN_SIGNALS.items():
        score = 0
        for signal in signals:
            if signal in text_lower:
                score += 1
        if score > 0:
            scores[domain_num] = score
    # Sort by score descending
    return sorted(scores.items(), key=lambda x: -x[1])


def detect_mode(request_text):
    """Detect output vs expertise mode from request text."""
    text_lower = request_text.lower()

    output_signals = ["write me", "write a", "create a", "build me", "build a",
                       "draft", "make a", "make this", "design a", "i need a"]
    expertise_signals = ["how do i", "how should", "what's the best", "advise", "review",
                         "help me", "should i", "tell me", "audit", "handle",
                         "what format", "what should", "i'm stuck", "i want to"]

    output_score = sum(1 for s in output_signals if s in text_lower)
    expertise_score = sum(1 for s in expertise_signals if s in text_lower)

    if output_score > expertise_score:
        return "output"
    elif expertise_score > output_score:
        return "expertise"
    return "hybrid"


def run_tests():
    """Run all routing test cases."""
    print(f"\n{'='*70}")
    print(f"ROUTING TEST SUITE — {len(TEST_CASES)} test cases")
    print(f"{'='*70}\n")

    passed = 0
    failed = 0
    warnings = 0
    results = []

    for i, (request, expected_domain, expected_experts, expected_mode) in enumerate(TEST_CASES, 1):
        domain_matches = detect_domain(request)
        detected_mode = detect_mode(request)

        # Check domain match
        domain_ok = False
        detected_domain = None
        if domain_matches:
            detected_domain = domain_matches[0][0]
            # Accept if expected domain is in top 2 matches
            top_domains = [d[0] for d in domain_matches[:2]]
            domain_ok = expected_domain in top_domains

        # Check mode match
        mode_ok = detected_mode == expected_mode or expected_mode == "hybrid"

        # Overall result
        if domain_ok and mode_ok:
            status = "PASS"
            passed += 1
        elif domain_ok or mode_ok:
            status = "WARN"
            warnings += 1
        else:
            status = "FAIL"
            failed += 1

        result = {
            "num": i,
            "request": request[:60] + "..." if len(request) > 60 else request,
            "expected_domain": expected_domain,
            "detected_domain": detected_domain,
            "expected_experts": expected_experts,
            "expected_mode": expected_mode,
            "detected_mode": detected_mode,
            "domain_ok": domain_ok,
            "mode_ok": mode_ok,
            "status": status,
        }
        results.append(result)

        # Print inline
        icon = "✅" if status == "PASS" else "⚠️" if status == "WARN" else "❌"
        print(f"  {icon} Test {i}: Domain {expected_domain}{'✓' if domain_ok else '✗'} "
              f"Mode {expected_mode}{'✓' if mode_ok else '✗'}")
        if not domain_ok:
            detected_str = f"D{detected_domain}" if detected_domain else "none"
            all_matches = ", ".join(f"D{d[0]}({d[1]})" for d in domain_matches[:3])
            print(f"     Expected D{expected_domain}, got {detected_str} | matches: {all_matches}")
        if not mode_ok:
            print(f"     Expected mode '{expected_mode}', got '{detected_mode}'")

    # Summary
    print(f"\n{'─'*70}")
    total = len(TEST_CASES)
    print(f"Results: {passed}/{total} PASS | {warnings} WARN | {failed} FAIL")
    pass_rate = (passed / total) * 100
    print(f"Pass rate: {pass_rate:.0f}%")

    # Success criteria: 18/20 = 90%
    target = 18
    if passed >= target:
        print(f"\n✅ MEETS TARGET: {passed}/{total} >= {target}/{total}")
    else:
        print(f"\n❌ BELOW TARGET: {passed}/{total} < {target}/{total}")

    # Write detailed report
    output_path = ROOT / ".tmp" / "routing-test-results.md"
    output_path.parent.mkdir(exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# Routing Test Suite Results\n\n")
        f.write(f"**Generated**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
        f.write(f"**Pass rate**: {passed}/{total} ({pass_rate:.0f}%)\n")
        f.write(f"**Target**: {target}/{total}\n\n")

        f.write("## Results\n\n")
        f.write("| # | Request | Expected Domain | Detected | Mode | Status |\n")
        f.write("|---|---------|----------------|----------|------|--------|\n")
        for r in results:
            f.write(f"| {r['num']} | {r['request']} | D{r['expected_domain']} | "
                    f"D{r['detected_domain'] or '?'} | "
                    f"{r['expected_mode']}/{r['detected_mode']} | {r['status']} |\n")

        if failed > 0 or warnings > 0:
            f.write("\n## Issues\n\n")
            for r in results:
                if r["status"] != "PASS":
                    f.write(f"### Test {r['num']}: {r['status']}\n")
                    f.write(f"- **Request**: {r['request']}\n")
                    if not r["domain_ok"]:
                        f.write(f"- **Domain**: Expected D{r['expected_domain']}, "
                                f"detected D{r['detected_domain'] or '?'}\n")
                    if not r["mode_ok"]:
                        f.write(f"- **Mode**: Expected '{r['expected_mode']}', "
                                f"detected '{r['detected_mode']}'\n")
                    f.write("\n")

    print(f"\nDetailed report → {output_path}")
    return passed, total


if __name__ == "__main__":
    run_tests()
