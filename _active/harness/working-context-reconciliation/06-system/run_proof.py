"""Replay protocol checks and inspect the known Jen failure without mutating it."""
import hashlib
import json
from pathlib import Path
import unittest
from datetime import datetime, timezone
from reconciliation_model import inspect_legacy, initial, receive, reconcile, packet, digest

HERE = Path(__file__).resolve().parent
JEN = Path('/Users/farricecain/Google Antigravity/.tmp/codex-worktrees/jen-icp-review-0914/_active/clients/jen-listings/03-working-drafts/2026-09-14-icp-review/CAROUSEL-CURRENT.md')
HISTORICAL_JEN = JEN.parent / '99-archive/reconciliation-20260914-231237/CAROUSEL-CURRENT.md'
ROLLOUT = Path('/Users/farricecain/.codex/sessions/2026/09/14/rollout-2026-09-14T14-44-23-01a0a1e0-dcd8-7683-aa4f-31d2fe5096b0.jsonl')


def main():
    result = unittest.TextTestRunner(verbosity=1).run(unittest.defaultTestLoader.discover(str(HERE), pattern='test_*.py'))
    source = HISTORICAL_JEN.read_bytes()
    live_before = JEN.read_bytes()
    scan = inspect_legacy(source.decode())
    if scan['finding'] != 'COMPETING_CURRENT_LABELS':
        raise RuntimeError('The archived failure no longer reproduces; investigate rather than weakening the test.')
    # Exact observed feedback; semantic mapping below is supplied by this audit,
    # not inferred by the reducer or attributed to a fresh-context executor.
    quotes = [
        "It's how people talk, so let's lock that in.",
        "What are you hoping the next house would change?",
        "The copy still doesn't work:",
    ]
    matches = {}
    outcome = None
    restoration = None
    for n, line in enumerate(ROLLOUT.open(), 1):
        entry = json.loads(line)
        payload = entry.get('payload', {})
        if entry.get('type') != 'response_item' or payload.get('role') != 'user':
            continue
        text = '\n'.join(c.get('text', '') for c in payload.get('content', []) if isinstance(c, dict))
        if 'Version 9 is okay' in text:
            restoration = {'line': n, 'timestamp': entry.get('timestamp'), 'quote': 'Version 9 is okay',
                           'source': str(ROLLOUT), 'interpretation': 'Later deliberate re-selection as useful baseline, not full approval.'}
        if 'omg this is it so much better 9/10' in text:
            outcome = {'line': n, 'timestamp': entry.get('timestamp'),
                       'quote': 'omg this is it so much better 9/10 thank you thank you!',
                       'source': str(ROLLOUT),
                       'interpretation': 'Positive human verdict after reconciliation; not a controlled causal experiment.'}
        for quote in quotes:
            if quote in text:
                matches[quote] = {'line': n, 'timestamp': entry.get('timestamp'), 'quote': quote,
                                  'source': str(ROLLOUT), 'full_turn_sha256': hashlib.sha256(text.encode()).hexdigest()}
    if len(matches) != len(quotes):
        raise RuntimeError('Expected real feedback provenance is missing; do not invent it.')
    state = initial('jen-offline-proof', 'one-carousel',
                    'Help a financially ready first-time buyer understand the fear of committing before a better house appears; one coherent conversation with an earned useful payoff.')
    for number, quote in enumerate(quotes, 1):
        state = receive(state, {'id': str(number), 'text': quote,
                                'source': str(ROLLOUT) + ':' + str(matches[quote]['line'])})
    opening = {'id': 'opening', 'slot': 'opening', 'path': 'fixture:approved-opening',
               'sha256': digest('what if a better house comes along? / it might.'),
               'status': 'approved', 'approved_excerpt': 'what if a better house comes along? / it might.',
               'decision': {'event': '1', 'quote': quotes[0]}}
    retired = [{'id': name, 'slot': 'middle', 'path': 'fixture:' + name, 'sha256': digest(name),
                'status': 'rejected', 'decision': {'event': eid, 'quote': quote}}
               for name, eid, quote in [('v07-consultation', '2', quotes[1]), ('v09-pagination', '3', quotes[2])]]
    state = reconcile(state, {'items': [opening, *retired],
                             'resolutions': [{'event': str(i), 'quote': quote,
                                              'effect': effect} for i, (quote, effect) in enumerate(zip(quotes, [
                                                  'Preserve the approved opening, not the whole draft.',
                                                  'Retire the consultation interpretation; keep original buyer fear.',
                                                  'Retire the pagination candidate; do not apply it or fall back to an older middle.']), 1)],
                             'next_action': {'text': 'Recompose the middle toward the whole buyer-fear objective, preserving the approved opening and consulting the full positive reference.',
                                             'targets': ['opening']}},
                      owner='jen-offline-proof', purpose='one-carousel', expected_revision=state['revision'])
    out = packet(state, {i['path']: i['sha256'] for i in state['items'].values()})
    if [i['id'] for i in out['active']] != ['opening'] or 'v09' in str(out['next_action']):
        raise RuntimeError('Rejected creative state leaked into the active packet.')
    receipt = {
        'created_at': datetime.now(timezone.utc).isoformat(),
        'scope': 'OFFLINE PROTOCOL PROOF; no runtime installation or live Jen edits',
        'tests': {'run': result.testsRun, 'failures': len(result.failures), 'errors': len(result.errors),
                  'passed': result.wasSuccessful(), 'cross_domain_subcases': 5},
        'legacy_file': {'path': str(HISTORICAL_JEN), 'sha256': hashlib.sha256(source).hexdigest(), **scan},
        'live_scan': {'path': str(JEN), 'sha256': hashlib.sha256(live_before).hexdigest(),
                      **inspect_legacy(live_before.decode())},
        'feedback_provenance': list(matches.values()),
        'replay': {'scope': 'Historical state at the 22:57 rejection, not the later live direction.',
                   'semantic_mapping': 'MANUALLY SUPPLIED; not autonomous language interpretation',
                   'result': out},
        'subsequent_restoration': restoration,
        'subsequent_human_outcome': outcome,
        'source_preservation': {'jen_file_unchanged': JEN.read_bytes() == live_before,
                                'archived_jen_file_unchanged': HISTORICAL_JEN.read_bytes() == source},
        'not_proven': ['native hooks firing', 'every-turn host coverage', 'autonomous semantic reconciliation',
                       'transaction/crash/concurrent filesystem safety', 'global activation',
                       'compaction survival', 'creative quality improvement'],
    }
    (HERE / 'proof.json').write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({'tests_passed': result.wasSuccessful(), 'tests_run': result.testsRun,
                      'legacy_scan': scan['finding'], 'active_replay_items': [i['id'] for i in out['active']],
                      'live_jen_unchanged': receipt['source_preservation']['jen_file_unchanged'],
                      'global_activation': 'NOT_INSTALLED'}))
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())
