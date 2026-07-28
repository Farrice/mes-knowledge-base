#!/usr/bin/env python3
"""
Tier 2 Core-Surface Detector — verify deliverables match skill loads.

Problem solved: "What good does it do that we're logging these things if they 
don't get fixed?" Measurement across 400 transcripts showed 43 sessions shipped 
deliverables but 29 read <2 skill files, 13 read zero. Core-surface audit catches 
the gap between "output shipped" and "expert loaded."

Audits (from execution_receipt.py manifest):
  1. Read session ledger (Session.json manifest from session_ledger_hook.py)
  2. For each session with a deliverable:
     - Extract domain (inferred from expert loaded or manifest tag)
     - List skills actually loaded (genius_read field)
     - Check PRODUCTION_CORE.md for that domain
     - Classify: ALIGNED (expert loaded), UNDERLOADED (expert not loaded), ORPHAN (no domain match)

Classification:
  ALIGNED — expert for domain was loaded; deliverable + skill match
  UNDERLOADED — deliverable produced but expert skills not loaded (GAP)
  ORPHAN — deliverable domain has no entry in PRODUCTION_CORE.md
  
Exit: always 0 (audit-only, never blocks)
Writes: .agent/health/core-surface.json + .agent/health/core-surface-report.md
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path("/Users/farricecain/Google Antigravity")
HEALTH_DIR = REPO_ROOT / ".agent/health"
SESSIONS_DIR = REPO_ROOT / ".agent/sessions"
OUTPUT_JSON = HEALTH_DIR / "core-surface.json"
OUTPUT_MD = HEALTH_DIR / "core-surface-report.md"


class CoreSurfaceAuditor:
    def __init__(self):
        self.findings = []
        self.timestamp = datetime.now().isoformat()
        self.production_core = self._load_production_core()
        
    def _load_production_core(self):
        """Load PRODUCTION_CORE.md and extract domain -> skills mapping"""
        core_path = REPO_ROOT / "PRODUCTION_CORE.md"
        core_map = {}
        
        if not core_path.exists():
            return core_map
        
        try:
            with open(core_path) as f:
                content = f.read()
            
            # Parse domain blocks (pattern: `## Domain Name` followed by skill files)
            # Example:
            # ## Content Creation
            # - skills/copywriter/SKILL.md
            # - skills/editor/SKILL.md
            
            domain_pattern = r"^## (.+?)$"
            skill_pattern = r"^\s*-\s+skills/([^/]+)/SKILL\.md"
            
            current_domain = None
            for line in content.split("\n"):
                domain_match = re.match(domain_pattern, line)
                if domain_match:
                    current_domain = domain_match.group(1).strip().lower()
                    core_map[current_domain] = []
                    continue
                
                if current_domain:
                    skill_match = re.match(skill_pattern, line)
                    if skill_match:
                        skill_name = skill_match.group(1)
                        core_map[current_domain].append(skill_name)
        
        except Exception:
            pass
        
        return core_map
    
    def _load_session_manifests(self):
        """Load session ledger manifests from .agent/sessions/"""
        manifests = []
        
        if not SESSIONS_DIR.exists():
            return manifests
        
        for manifest_file in sorted(SESSIONS_DIR.glob("ledger-*.json")):
            try:
                with open(manifest_file) as f:
                    data = json.load(f)
                    manifests.append(data)
            except Exception:
                continue
        
        return manifests
    
    def _infer_domain_from_deliverables(self, deliverables):
        """Infer primary domain from deliverable paths"""
        domain_patterns = {
            "content": ["parallax", "substack", "linkedin", "article"],
            "copy": ["email", "sales", "landing", "adcopy", "headline"],
            "brand": ["logo", "brand", "identity", "palette"],
            "research": ["research", "brief", "report"],
            "video": ["video", "youtube", "thumbnail"],
            "extraction": ["extraction", "extract", "skill"],
        }
        
        inferred = set()
        for deliv in deliverables:
            deliv_lower = deliv.lower()
            for domain, patterns in domain_patterns.items():
                if any(p in deliv_lower for p in patterns):
                    inferred.add(domain)
        
        return list(inferred) if inferred else ["unknown"]
    
    def audit_sessions(self):
        """Audit each session's expert loading vs deliverables"""
        manifests = self._load_session_manifests()
        
        if not manifests:
            self.findings.append({
                "tier": "sessions",
                "classification": "INFO",
                "message": "No session manifests found",
                "count": 0
            })
            return
        
        aligned_count = 0
        underloaded_count = 0
        orphan_count = 0
        
        for manifest in manifests:
            session_id = manifest.get("session_id", "unknown")
            deliverables = manifest.get("deliverables", [])
            genius_read = manifest.get("genius_read", [])
            
            if not deliverables:
                continue  # Skip sessions with no deliverables
            
            domains = self._infer_domain_from_deliverables(deliverables)
            
            # Extract skill names from genius_read paths
            loaded_skills = set()
            for read_path in genius_read:
                # Pattern: skills/skillname/genius.md
                match = re.search(r"skills/([^/]+)/", read_path)
                if match:
                    loaded_skills.add(match.group(1))
            
            # Check each domain against PRODUCTION_CORE
            for domain in domains:
                domain_key = domain.lower()
                
                if domain_key not in self.production_core:
                    self.findings.append({
                        "tier": "core_surface",
                        "classification": "ORPHAN",
                        "session_id": session_id,
                        "domain": domain,
                        "deliverables": deliverables[:2],  # First 2 as examples
                        "message": f"Domain '{domain}' has no entry in PRODUCTION_CORE.md",
                        "severity": "medium"
                    })
                    orphan_count += 1
                    continue
                
                required_skills = set(self.production_core[domain_key])
                intersection = loaded_skills & required_skills
                
                if len(intersection) >= max(1, len(required_skills) * 0.5):
                    aligned_count += 1
                    self.findings.append({
                        "tier": "core_surface",
                        "classification": "ALIGNED",
                        "session_id": session_id,
                        "domain": domain,
                        "loaded": sorted(list(intersection)),
                        "message": f"Domain '{domain}': {len(intersection)}/{len(required_skills)} core skills loaded"
                    })
                else:
                    underloaded_count += 1
                    missing = required_skills - loaded_skills
                    self.findings.append({
                        "tier": "core_surface",
                        "classification": "UNDERLOADED",
                        "session_id": session_id,
                        "domain": domain,
                        "loaded": sorted(list(intersection)),
                        "missing": sorted(list(missing)),
                        "message": f"Domain '{domain}': only {len(intersection)}/{len(required_skills)} core skills loaded",
                        "severity": "high"
                    })
        
        self.findings.insert(0, {
            "tier": "sessions",
            "classification": "SUMMARY",
            "sessions_audited": len(manifests),
            "aligned": aligned_count,
            "underloaded": underloaded_count,
            "orphan": orphan_count,
            "message": f"Core-surface audit: {aligned_count} aligned, {underloaded_count} underloaded, {orphan_count} orphan"
        })
    
    def write_json_report(self):
        """Write findings to .agent/health/core-surface.json"""
        HEALTH_DIR.mkdir(parents=True, exist_ok=True)
        
        aligned = len([f for f in self.findings if f.get("classification") == "ALIGNED"])
        underloaded = len([f for f in self.findings if f.get("classification") == "UNDERLOADED"])
        orphan = len([f for f in self.findings if f.get("classification") == "ORPHAN"])
        
        report = {
            "timestamp": self.timestamp,
            "summary": {
                "total_findings": len(self.findings),
                "aligned": aligned,
                "underloaded": underloaded,
                "orphan": orphan
            },
            "production_core_domains": len(self.production_core),
            "findings": self.findings
        }
        
        with open(OUTPUT_JSON, "w") as f:
            json.dump(report, f, indent=2)
    
    def write_markdown_report(self):
        """Write findings to .agent/health/core-surface-report.md"""
        HEALTH_DIR.mkdir(parents=True, exist_ok=True)
        
        lines = [
            "# Core-Surface Audit Report",
            f"**Generated**: {self.timestamp}",
            "",
            "## Summary",
            ""
        ]
        
        summary = next((f for f in self.findings if f.get("classification") == "SUMMARY"), {})
        if summary:
            lines.append(f"- **Aligned** (expert loaded, core skills present): {summary.get('aligned', 0)}")
            lines.append(f"- **Underloaded** (deliverables shipped, core skills missing): {summary.get('underloaded', 0)}")
            lines.append(f"- **Orphan** (domain not in PRODUCTION_CORE.md): {summary.get('orphan', 0)}")
            lines.append("")
        
        underloaded = [f for f in self.findings if f.get("classification") == "UNDERLOADED"]
        if underloaded:
            lines.append("## ⚠️ Underloaded Sessions")
            lines.append("")
            lines.append("These sessions shipped deliverables without loading core skills:")
            lines.append("")
            for finding in underloaded[:10]:  # Show first 10
                session_id = finding.get("session_id", "?")
                domain = finding.get("domain", "?")
                loaded = finding.get("loaded", [])
                missing = finding.get("missing", [])
                lines.append(f"**{session_id}** — {domain}")
                if loaded:
                    lines.append(f"  - Loaded: {', '.join(loaded)}")
                if missing:
                    lines.append(f"  - Missing: {', '.join(missing)}")
                lines.append("")
        
        aligned = [f for f in self.findings if f.get("classification") == "ALIGNED"]
        if aligned:
            lines.append("## ✅ Aligned Sessions")
            lines.append("")
            for finding in aligned[:5]:  # Show first 5
                session_id = finding.get("session_id", "?")
                domain = finding.get("domain", "?")
                lines.append(f"- {session_id} — {domain}")
            lines.append("")
        
        lines.append("## 📋 Production Core Domains")
        lines.append("")
        for domain, skills in sorted(self.production_core.items()):
            lines.append(f"### {domain.title()}")
            for skill in sorted(skills):
                lines.append(f"- {skill}")
            lines.append("")
        
        with open(OUTPUT_MD, "w") as f:
            f.write("\n".join(lines))
    
    def run(self):
        """Run all audits"""
        self.audit_sessions()
        self.write_json_report()
        self.write_markdown_report()
        
        return 0  # Always exit 0 (audit-only, never blocks)


if __name__ == "__main__":
    auditor = CoreSurfaceAuditor()
    exit(auditor.run())
