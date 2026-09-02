#!/usr/bin/env python3
"""
PSA Prompt Audit Tool
Analyzes prompts against the 5-dimension diagnostic framework.
"""

import json
import sys
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class DimensionScore:
    dimension: str
    score: int
    findings: List[str]
    recommendations: List[str]

def analyze_context_clarity(prompt: str) -> DimensionScore:
    """Analyze Layer 1: Context Foundation"""
    findings = []
    recommendations = []
    score = 5
    
    # Check for role definition
    role_indicators = ['you are', 'act as', 'your role', 'as a', 'expert in']
    if not any(indicator in prompt.lower() for indicator in role_indicators):
        score -= 1
        findings.append("No explicit role definition found")
        recommendations.append("Add: 'You are [SPECIFIC ROLE] with expertise in [DOMAINS]'")
    
    # Check for audience awareness
    audience_indicators = ['audience', 'reader', 'user', 'customer', 'they care', 'speaking to']
    if not any(indicator in prompt.lower() for indicator in audience_indicators):
        score -= 1
        findings.append("No audience awareness embedded")
        recommendations.append("Add: 'Your audience is [PROFILE] who [CHARACTERISTICS]'")
    
    # Check for domain constraints
    constraint_indicators = ['never', 'avoid', 'do not', "don't", 'boundary', 'constraint']
    if not any(indicator in prompt.lower() for indicator in constraint_indicators):
        score -= 1
        findings.append("No explicit constraints or boundaries")
        recommendations.append("Add: 'Never [ANTI-PATTERNS]' or 'Avoid [BEHAVIORS]'")
    
    # Check for quality standards
    quality_indicators = ['quality', 'standard', 'criteria', 'must', 'requirement']
    if not any(indicator in prompt.lower() for indicator in quality_indicators):
        score -= 1
        findings.append("No quality standards defined")
        recommendations.append("Add: 'Quality means [SPECIFIC CRITERIA]'")
    
    # Check for specificity
    vague_patterns = ['helpful assistant', 'be professional', 'engaging content', 'good quality']
    if any(pattern in prompt.lower() for pattern in vague_patterns):
        score -= 1
        findings.append("Contains vague, generic descriptors")
        recommendations.append("Replace generic terms with specific, measurable criteria")
    
    return DimensionScore(
        dimension="Context Clarity",
        score=max(1, score),
        findings=findings or ["Context foundation is well-defined"],
        recommendations=recommendations
    )

def analyze_process_structure(prompt: str) -> DimensionScore:
    """Analyze Layer 2: Process Architecture"""
    findings = []
    recommendations = []
    score = 5
    
    # Check for reasoning sequence
    sequence_indicators = ['first', 'then', 'before', 'after', 'step', '1.', '2.', 'analyze', 'plan']
    if not any(indicator in prompt.lower() for indicator in sequence_indicators):
        score -= 2
        findings.append("No defined reasoning sequence")
        recommendations.append("Add: 'Before generating output: 1. [ANALYZE] 2. [PLAN] 3. [EXECUTE]'")
    
    # Check for decision framework
    decision_indicators = ['choose', 'decide', 'prioritize', 'when', 'if']
    if not any(indicator in prompt.lower() for indicator in decision_indicators):
        score -= 1
        findings.append("No decision framework specified")
        recommendations.append("Add guidance for handling choices and edge cases")
    
    # Check for checkpoints
    checkpoint_indicators = ['verify', 'check', 'confirm', 'validate', 'ensure']
    if not any(indicator in prompt.lower() for indicator in checkpoint_indicators):
        score -= 1
        findings.append("No checkpoint gates defined")
        recommendations.append("Add verification steps within the process")
    
    # Check if it jumps straight to output
    direct_commands = ['write', 'create', 'generate', 'make']
    has_process = any(ind in prompt.lower() for ind in sequence_indicators)
    starts_with_command = any(prompt.lower().strip().startswith(cmd) for cmd in direct_commands)
    
    if starts_with_command and not has_process:
        score -= 1
        findings.append("Jumps directly to output without process")
        recommendations.append("Add thinking/planning steps before execution")
    
    return DimensionScore(
        dimension="Process Structure",
        score=max(1, score),
        findings=findings or ["Process architecture is well-defined"],
        recommendations=recommendations
    )

def analyze_output_precision(prompt: str) -> DimensionScore:
    """Analyze Layer 3: Output Specification"""
    findings = []
    recommendations = []
    score = 5
    
    # Check for structure definition
    structure_indicators = ['structure', 'format', 'section', 'include', 'contain', 'must have']
    if not any(indicator in prompt.lower() for indicator in structure_indicators):
        score -= 1
        findings.append("No output structure defined")
        recommendations.append("Add: 'Output must include: [ELEMENTS]'")
    
    # Check for tone specification
    tone_indicators = ['tone', 'voice', 'style', 'sound', 'feel']
    if not any(indicator in prompt.lower() for indicator in tone_indicators):
        score -= 1
        findings.append("No tone/style specification")
        recommendations.append("Add: 'Tone: [SPECIFIC DESCRIPTORS]'")
    
    # Check for length/format requirements
    format_indicators = ['word', 'length', 'paragraph', 'sentence', 'character', 'short', 'long']
    if not any(indicator in prompt.lower() for indicator in format_indicators):
        score -= 1
        findings.append("No format/length requirements")
        recommendations.append("Add specific length and format constraints")
    
    # Check for examples
    example_indicators = ['example', 'like this', 'such as', 'for instance', 'sample']
    if not any(indicator in prompt.lower() for indicator in example_indicators):
        score -= 1
        findings.append("No quality anchor/example provided")
        recommendations.append("Add: 'Example of target quality: [CONCRETE EXAMPLE]'")
    
    # Check for vague quality descriptors
    vague_quality = ['engaging', 'professional', 'high-quality', 'compelling', 'interesting']
    specific_indicators = ['specific', 'concrete', 'measurable', 'exactly', 'precisely']
    if any(vq in prompt.lower() for vq in vague_quality):
        if not any(si in prompt.lower() for si in specific_indicators):
            score -= 1
            findings.append("Uses vague quality descriptors without specificity")
            recommendations.append("Define what 'engaging' or 'professional' means concretely")
    
    return DimensionScore(
        dimension="Output Precision",
        score=max(1, score),
        findings=findings or ["Output specification is well-defined"],
        recommendations=recommendations
    )

def analyze_voice_preservation(prompt: str) -> DimensionScore:
    """Analyze Layer 3b: Voice Preservation"""
    findings = []
    recommendations = []
    score = 5
    
    # Check for voice characteristics
    voice_indicators = ['voice', 'sounds like', 'personality', 'characteristic']
    if not any(indicator in prompt.lower() for indicator in voice_indicators):
        score -= 1
        findings.append("No voice characteristics defined")
        recommendations.append("Add: 'Voice characteristics: [SPECIFIC PATTERNS]'")
    
    # Check for anti-patterns
    antipattern_indicators = ['never use', 'avoid saying', "don't say", 'banned', 'forbidden']
    if not any(indicator in prompt.lower() for indicator in antipattern_indicators):
        score -= 1
        findings.append("No voice anti-patterns identified")
        recommendations.append("Add: 'Never uses: [BANNED PHRASES/PATTERNS]'")
    
    # Check for concrete voice examples
    voice_example_indicators = ['sounds like', 'would say', 'signature', 'typical']
    if not any(indicator in prompt.lower() for indicator in voice_example_indicators):
        score -= 1
        findings.append("No concrete voice examples")
        recommendations.append("Add examples of authentic voice patterns")
    
    # Check for brand match instruction
    generic_voice = ['match our brand', 'brand voice', 'company tone']
    detailed_voice = ['confident but', 'warm but', 'uses', 'avoids']
    if any(gv in prompt.lower() for gv in generic_voice):
        if not any(dv in prompt.lower() for dv in detailed_voice):
            score -= 2
            findings.append("References brand voice without defining it")
            recommendations.append("Replace 'match brand voice' with specific voice characteristics")
    
    return DimensionScore(
        dimension="Voice Preservation",
        score=max(1, score),
        findings=findings or ["Voice preservation is well-defined"],
        recommendations=recommendations
    )

def analyze_reliability_mechanisms(prompt: str) -> DimensionScore:
    """Analyze Layer 4: Feedback Loops"""
    findings = []
    recommendations = []
    score = 5
    
    # Check for self-review
    review_indicators = ['before final', 'verify', 'check', 'validate', 'review', 'ensure']
    if not any(indicator in prompt.lower() for indicator in review_indicators):
        score -= 2
        findings.append("No self-review mechanism")
        recommendations.append("Add: 'Before finalizing, verify: [CHECKLIST]'")
    
    # Check for quality checklist
    checklist_indicators = ['□', '[ ]', 'checklist', 'criteria']
    numbered_checks = any(f'{i}.' in prompt for i in range(1, 10))
    if not any(indicator in prompt for indicator in checklist_indicators) and not numbered_checks:
        score -= 1
        findings.append("No explicit quality checklist")
        recommendations.append("Add checkboxes or numbered quality criteria")
    
    # Check for failure recovery
    failure_indicators = ['if stuck', 'when uncertain', 'fallback', 'if unable', 'recovery']
    if not any(indicator in prompt.lower() for indicator in failure_indicators):
        score -= 1
        findings.append("No failure recovery protocol")
        recommendations.append("Add: 'If stuck or uncertain: [RECOVERY STEPS]'")
    
    # Check for iteration trigger
    iteration_indicators = ['revise', 'iterate', 'improve', 'refine', 'if any fail']
    if not any(indicator in prompt.lower() for indicator in iteration_indicators):
        score -= 1
        findings.append("No iteration triggers defined")
        recommendations.append("Add: 'If any check fails, revise accordingly'")
    
    return DimensionScore(
        dimension="Reliability Mechanisms",
        score=max(1, score),
        findings=findings or ["Reliability mechanisms are well-defined"],
        recommendations=recommendations
    )

def run_audit(prompt: str) -> dict:
    """Run full PSA audit on a prompt"""
    dimensions = [
        analyze_context_clarity(prompt),
        analyze_process_structure(prompt),
        analyze_output_precision(prompt),
        analyze_voice_preservation(prompt),
        analyze_reliability_mechanisms(prompt)
    ]
    
    total_score = sum(d.score for d in dimensions)
    
    if total_score >= 20:
        category = "Production-ready"
    elif total_score >= 15:
        category = "Functional with gaps"
    elif total_score >= 10:
        category = "Needs architectural work"
    else:
        category = "Rebuild recommended"
    
    return {
        "total_score": total_score,
        "max_score": 25,
        "category": category,
        "dimensions": [
            {
                "name": d.dimension,
                "score": d.score,
                "findings": d.findings,
                "recommendations": d.recommendations
            }
            for d in dimensions
        ],
        "top_3_improvements": get_top_improvements(dimensions)
    }

def get_top_improvements(dimensions: List[DimensionScore]) -> List[str]:
    """Extract top 3 most impactful improvements"""
    all_recommendations = []
    for d in dimensions:
        for rec in d.recommendations:
            all_recommendations.append({
                "dimension": d.dimension,
                "score": d.score,
                "recommendation": rec
            })
    
    # Sort by lowest score (highest impact)
    all_recommendations.sort(key=lambda x: x["score"])
    
    return [
        f"[{r['dimension']}] {r['recommendation']}"
        for r in all_recommendations[:3]
    ]

def main():
    if len(sys.argv) > 1:
        # Read prompt from file
        with open(sys.argv[1], 'r') as f:
            prompt = f.read()
    else:
        # Read from stdin
        print("Paste your prompt (Ctrl+D when done):")
        prompt = sys.stdin.read()
    
    result = run_audit(prompt)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
