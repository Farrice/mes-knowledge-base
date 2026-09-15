#!/usr/bin/env python3
"""Check recovery integrity and frozen boundaries; does not certify live learning."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
errors = []
rows = json.loads((HERE / 'restored-files.json').read_text())
for item in rows:
    path = ROOT / item['path']
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
        errors.append('Restored bytes missing or changed: ' + item['path'])
checks = {
    '.agent/workflows/operator-school.md': ['## Explicit Embody Mode', 'never auto-fires'],
    '.agent/workflows/source-to-skill-system.md': ['mastery-transfer-proof-spine.md', 'highest contiguous earned state', 'only if the package is restored'],
    'CODEX.md': ['`/embody` is intentionally explicit-only and logically cold'],
    'SLASH_COMMANDS.md': ['| `/embody` |'],
    'semantic_libraries/antigravity/primitives/skill-system-contract.md': ['mastery-transfer-proof-spine.md', '## Signal Fidelity Handoff (SHADOW)'],
    'semantic_libraries/antigravity/primitives/behavior-changing-extraction-contract.md': ['## Proof Ceiling And Handoff'],
    'skills/extract-mastery/workflows/03-design-transcendence-path.md': ['TARGET HYPOTHESIS', 'SURPASSING'],
}
for name, markers in checks.items():
    text = (ROOT / name).read_text()
    errors.extend(name + ': missing ' + marker for marker in markers if marker not in text)
cycle = json.loads((ROOT / 'extractions/mastery-transfer-proof-spine/three-capability-shadow-observation-cycle-v1.json').read_text())
assert cycle['status'] == 'DESIGNED_NOT_RUN'
for key in ['promotion_eligible', 'automatic_enforcement', 'canonical_state_mutation_allowed', 'subagents_authorized']:
    assert cycle[key] is False, key
assert all(v == 0 for v in cycle['events'].values())
assert len(cycle['capabilities']) == 3
for capability in cycle['capabilities']:
    errors.extend('Missing historical cycle evidence: ' + p for p in capability['evidence'] if not (ROOT / p).exists())
if errors:
    print('RECOVERY INTEGRITY FAIL\n' + '\n'.join(errors))
    raise SystemExit(1)
print(f'RECOVERY INTEGRITY PASS: {len(rows)} original files hash-identical; seven integrations present; all 14 cycle evidence paths available; observation remains inert.')
print('Proof ceiling: structural integrity and historical evidence availability only; live operator learning and universal firing NOT_RUN/UNCONFIRMED.')
