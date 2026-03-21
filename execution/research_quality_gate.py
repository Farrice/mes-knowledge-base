#!/usr/bin/env python3
"""
Research Quality Gate — Validates research output before downstream use.

Checks:
  - Source count (minimum 5 for Standard, 15 for Deep)
  - Provenance audit (every claim must have a source URL)
  - Recency check (flags data older than 12 months for time-sensitive topics)
  - Echo chamber detection (flags when all sources say the same thing)
  - Confidence scoring
  - Naked claim detection (claims without any evidence)

Usage:
    python execution/research_quality_gate.py validate .tmp/research/report.md
    python execution/research_quality_gate.py validate .tmp/research/report.md --strict

Usage (Python):
    from research_quality_gate import QualityGate
    gate = QualityGate()
    report = gate.validate_markdown(Path(".tmp/research/report.md"))
    print(report.to_markdown())
"""

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


# ---------------------------------------------------------------------------
# Data Structures
# ---------------------------------------------------------------------------

@dataclass
class QualityIssue:
    """A single quality issue found in research output."""
    severity: str  # "critical", "warning", "info"
    category: str  # "provenance", "recency", "diversity", "echo_chamber", "naked_claim"
    message: str
    line_number: Optional[int] = None
    suggestion: str = ""


@dataclass
class QualityReport:
    """Complete quality assessment of a research document."""
    file_path: str = ""
    issues: List[QualityIssue] = field(default_factory=list)
    metrics: Dict[str, Any] = field(default_factory=dict)
    overall_pass: bool = False
    overall_score: int = 0  # 0-100

    def to_markdown(self) -> str:
        lines = []
        status = "✅ PASS" if self.overall_pass else "❌ FAIL"
        lines.append(f"# Research Quality Report — {status} ({self.overall_score}/100)")
        lines.append("")
        if self.file_path:
            lines.append(f"**File**: {self.file_path}")
        lines.append("")

        # Metrics summary
        if self.metrics:
            lines.append("## Metrics")
            for k, v in self.metrics.items():
                lines.append(f"- **{k}**: {v}")
            lines.append("")

        # Issues by severity
        for sev in ["critical", "warning", "info"]:
            sev_issues = [i for i in self.issues if i.severity == sev]
            if sev_issues:
                icon = {"critical": "🔴", "warning": "🟡", "info": "ℹ️"}[sev]
                lines.append(f"## {icon} {sev.title()} Issues ({len(sev_issues)})")
                for issue in sev_issues:
                    lines.append(f"- **[{issue.category}]** {issue.message}")
                    if issue.suggestion:
                        lines.append(f"  - Fix: {issue.suggestion}")
                lines.append("")

        if not self.issues:
            lines.append("## No issues found ✨")
            lines.append("")

        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Quality Gate
# ---------------------------------------------------------------------------

class QualityGate:
    """Validates research output against quality standards."""

    # Time-sensitive topics that need recent data
    TIME_SENSITIVE_KEYWORDS = [
        "market size", "pricing", "revenue", "trend", "growth", "forecast",
        "salary", "rate", "cost", "percentage", "statistics", "2024", "2025",
        "2026", "current", "latest", "recent", "today", "now",
    ]

    def validate_markdown(self, path: Path, strict: bool = False) -> QualityReport:
        """Validate a markdown research document."""
        if not path.exists():
            report = QualityReport(file_path=str(path))
            report.issues.append(QualityIssue(
                severity="critical",
                category="file",
                message=f"Research file not found: {path}",
            ))
            return report

        text = path.read_text()
        return self.validate_text(text, file_path=str(path), strict=strict)

    def validate_text(self, text: str, file_path: str = "",
                      strict: bool = False) -> QualityReport:
        """Validate research text against quality standards."""
        report = QualityReport(file_path=file_path)
        lines = text.split("\n")

        # Run all checks
        self._check_source_count(text, lines, report, strict)
        self._check_provenance(text, lines, report)
        self._check_recency(text, lines, report)
        self._check_echo_chamber(text, lines, report)
        self._check_naked_claims(text, lines, report)
        self._check_hedge_language(text, lines, report)

        # Calculate overall score
        critical_count = sum(1 for i in report.issues if i.severity == "critical")
        warning_count = sum(1 for i in report.issues if i.severity == "warning")

        report.overall_score = max(0, 100 - (critical_count * 25) - (warning_count * 10))
        report.overall_pass = critical_count == 0 and report.overall_score >= 60

        return report

    # ----- Checks -----

    def _check_source_count(self, text: str, lines: List[str],
                            report: QualityReport, strict: bool):
        """Check minimum source count."""
        # Count unique URLs
        urls = set(re.findall(r"https?://[^\s\)\"'>]+", text))
        unique_domains = set()
        for url in urls:
            match = re.match(r"https?://([^/]+)", url)
            if match:
                unique_domains.add(match.group(1))

        report.metrics["total_urls"] = len(urls)
        report.metrics["unique_domains"] = len(unique_domains)

        # Determine expected depth from content
        if "deep" in text.lower()[:200]:
            min_sources = 15 if strict else 10
            depth = "deep"
        elif "standard" in text.lower()[:200]:
            min_sources = 8 if strict else 5
            depth = "standard"
        else:
            min_sources = 3
            depth = "unknown"

        report.metrics["detected_depth"] = depth
        report.metrics["min_sources_expected"] = min_sources

        if len(urls) < min_sources:
            report.issues.append(QualityIssue(
                severity="critical",
                category="provenance",
                message=f"Only {len(urls)} sources found (minimum {min_sources} for {depth} depth)",
                suggestion="Increase research depth or add more search queries",
            ))

        if len(unique_domains) < 3:
            report.issues.append(QualityIssue(
                severity="critical" if strict else "warning",
                category="diversity",
                message=f"Only {len(unique_domains)} unique domains (minimum 3 needed)",
                suggestion="Diversify sources — search with different query angles",
            ))

    def _check_provenance(self, text: str, lines: List[str], report: QualityReport):
        """Check that claims have source attribution."""
        # Find claim-like sentences (statements that assert facts)
        claim_patterns = [
            r"(?:market size|revenue|growth|valued at|worth|estimated).*?[\$€£]\d",
            r"\d+%",
            r"\d+ (?:billion|million|thousand)",
            r"according to",
            r"research (?:shows|indicates|suggests|finds)",
        ]

        claims_without_sources = 0
        claims_with_sources = 0

        for i, line in enumerate(lines):
            line_lower = line.lower()
            is_claim = any(re.search(p, line_lower) for p in claim_patterns)

            if is_claim:
                # Check if this line or the next 2 lines have a URL
                context = "\n".join(lines[max(0, i-1):min(len(lines), i+3)])
                has_source = bool(re.search(r"https?://", context))

                if has_source:
                    claims_with_sources += 1
                else:
                    claims_without_sources += 1

        total = claims_with_sources + claims_without_sources
        if total > 0:
            pct = round(claims_with_sources / total * 100)
            report.metrics["claim_sourcing_rate"] = f"{pct}% ({claims_with_sources}/{total})"

            if pct < 60:
                report.issues.append(QualityIssue(
                    severity="critical",
                    category="provenance",
                    message=f"Only {pct}% of data claims have source attribution",
                    suggestion="Run grounding pass to attach sources to naked claims",
                ))
            elif pct < 80:
                report.issues.append(QualityIssue(
                    severity="warning",
                    category="provenance",
                    message=f"{pct}% of data claims sourced (target: 80%+)",
                    suggestion="Some claims need source verification",
                ))

    def _check_recency(self, text: str, lines: List[str], report: QualityReport):
        """Check if time-sensitive claims use recent data."""
        is_time_sensitive = any(
            kw in text.lower() for kw in self.TIME_SENSITIVE_KEYWORDS
        )

        if not is_time_sensitive:
            return

        # Look for old year references
        current_year = datetime.now().year
        old_years = []
        for year in range(2018, current_year - 1):
            if str(year) in text:
                count = text.count(str(year))
                old_years.append((year, count))

        if old_years:
            years_str = ", ".join(f"{y[0]} ({y[1]}x)" for y in old_years)
            report.issues.append(QualityIssue(
                severity="warning",
                category="recency",
                message=f"Time-sensitive topic references old data: {years_str}",
                suggestion="Verify these findings are still current or find updated sources",
            ))

    def _check_echo_chamber(self, text: str, lines: List[str], report: QualityReport):
        """Detect echo chamber — all sources saying the exact same thing."""
        # Find all URLs and check domain diversity
        urls = re.findall(r"https?://([^/\s\)\"'>]+)", text)
        if len(urls) < 3:
            return

        # Check for lack of contrarian/alternative viewpoints
        contrarian_signals = [
            "however", "on the other hand", "critics", "counterpoint",
            "disagree", "debate", "controversial", "alternative view",
            "some argue", "contrarian", "risk", "downside", "limitation",
        ]
        contrarian_count = sum(1 for s in contrarian_signals if s in text.lower())

        if contrarian_count == 0 and len(urls) >= 5:
            report.issues.append(QualityIssue(
                severity="warning",
                category="echo_chamber",
                message="No contrarian perspectives found — possible echo chamber",
                suggestion="Search for '[topic] criticism' or '[topic] risks downsides'",
            ))

    def _check_naked_claims(self, text: str, lines: List[str], report: QualityReport):
        """Detect bold claims without any supporting evidence."""
        naked_claim_patterns = [
            (r"(?:the best|the most|the only|the top|the leading|the fastest)", "superlative"),
            (r"(?:always|never|everyone|nobody|guaranteed|proven)", "absolute"),
            (r"(?:experts agree|it's well known|studies show|research proves)", "vague_authority"),
        ]

        naked_claims = []
        for i, line in enumerate(lines):
            for pattern, ptype in naked_claim_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    # Check if there's a source nearby
                    context = "\n".join(lines[max(0, i-1):min(len(lines), i+3)])
                    if not re.search(r"https?://", context):
                        naked_claims.append((i + 1, line.strip()[:80], ptype))

        if naked_claims:
            report.metrics["naked_claims"] = len(naked_claims)
            for line_num, claim, ptype in naked_claims[:5]:
                report.issues.append(QualityIssue(
                    severity="warning",
                    category="naked_claim",
                    message=f"Line {line_num}: Unsourced {ptype} claim: '{claim}...'",
                    line_number=line_num,
                    suggestion="Add a source URL or soften the language",
                ))

    def _check_hedge_language(self, text: str, lines: List[str], report: QualityReport):
        """Detect excessive hedge language that may indicate ungrounded content."""
        hedge_words = [
            "might", "could potentially", "it seems", "perhaps",
            "it appears", "one could argue", "it's possible that",
            "there may be", "it's conceivable",
        ]

        hedge_count = sum(text.lower().count(h) for h in hedge_words)
        word_count = len(text.split())
        hedge_ratio = hedge_count / max(word_count, 1) * 1000  # per 1000 words

        report.metrics["hedge_ratio"] = f"{hedge_ratio:.1f} per 1000 words"

        if hedge_ratio > 10:
            report.issues.append(QualityIssue(
                severity="warning",
                category="provenance",
                message=f"High hedge language ratio ({hedge_ratio:.1f}/1000 words) — "
                        f"may indicate ungrounded speculation",
                suggestion="Replace hedged claims with sourced facts or remove them",
            ))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Research Quality Gate — validate research output"
    )
    parser.add_argument("action", choices=["validate"],
                       help="Action to perform")
    parser.add_argument("file", help="Path to research markdown file")
    parser.add_argument("--strict", action="store_true",
                       help="Apply stricter quality thresholds")

    args = parser.parse_args()
    gate = QualityGate()

    path = Path(args.file)
    report = gate.validate_markdown(path, strict=args.strict)
    print(report.to_markdown())

    # Exit with non-zero if critical issues found
    critical = sum(1 for i in report.issues if i.severity == "critical")
    sys.exit(1 if critical > 0 else 0)


if __name__ == "__main__":
    main()
