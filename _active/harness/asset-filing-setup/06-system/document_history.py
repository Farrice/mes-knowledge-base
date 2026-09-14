#!/usr/bin/env python3
"""Decision-led document anchors and reversible retirement; no global sweep."""
import argparse
import fcntl
import json
import subprocess
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
import asset_filing as filing

MARKER='<!-- managed-by: document_history.py -->'
HISTORICAL={'parked','superseded','archived'}


def home_path(value):
    home=Path(value).resolve(strict=True)
    try:
        return filing.safe_home(home)
    except ValueError:
        # Existing repository projects are writable only inside the caller's lane.
        cwd=Path.cwd().resolve()
        result=subprocess.run(['git','-C',str(cwd),'rev-parse','--show-toplevel'],capture_output=True,text=True)
        root=Path(result.stdout.strip()) if result.returncode==0 else None
        if root and (root/'.git').is_file() and home.is_relative_to(root) and cwd.is_relative_to(root):
            return home
        raise ValueError('Use a Work project or cd into the owning Git worktree. Integration main and unrelated workspaces are read-only here.')


def state_path(home):
    return filing.child(home,'06-system/document-state.json')


def pending_path(home):
    return filing.child(home,'06-system/document-transition.pending.json')


def read_state(home):
    path=state_path(home)
    if path.exists():
        state=json.loads(path.read_text())
        if state.get('schema')!=1:
            raise ValueError('Unsupported document-state schema.')
        return state
    canon=filing.child(home,'CANON.md')
    if canon.exists():
        raise ValueError('An existing CANON.md owns authority. Reconcile it explicitly; never replace it automatically.')
    return {'schema':1,'revision':0,'documents':{}}


def atomic_json(path,data):
    temporary=path.with_name(path.name+'.pending-write')
    with temporary.open('x') as out:
        out.write(json.dumps(data,indent=2)+'\n')
    temporary.replace(path)


@contextmanager
def locked(home):
    filing.child(home,'06-system').mkdir(exist_ok=True)
    with filing.child(home,'06-system/asset-filing.lock').open('a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        if pending_path(home).exists():
            raise ValueError('Interrupted transition: inspect document-transition.pending.json before using any anchor.')
        yield


def check_revision(state,expected):
    if state['revision']!=expected:
        raise ValueError(f'Stale task: expected revision {expected}, current is {state["revision"]}. Re-read CANON and reconcile; do not retry with a new revision blindly.')


def render(home,state):
    canon=filing.child(home,'CANON.md')
    if canon.exists() and MARKER not in canon.read_text():
        raise ValueError('Existing human-owned CANON.md requires reconciliation.')
    current=['# Current Documents', '', MARKER, '', f'Revision: {state["revision"]}', '', 'Use only the CURRENT entries below as anchors. History never becomes current because it is newer or ranks higher in search.', '']
    history=['# Document History', '', MARKER, '', 'Historical reference only. Do not use as a current offer, plan, or instruction. See [current documents](../CANON.md).', '']
    for key,record in sorted(state['documents'].items()):
        # Stable project entry point follows the decision, not a copied document.
        filing.child(home, '00-start-here').mkdir(exist_ok=True)
        role = home / '00-start-here' / (key + '.md')
        pending = role.with_name(role.name + '.pending-pointer')
        if record.get('current'):
            pending.symlink_to('../' + record['current']['path'])
        else:
            pending.write_text('# No current document\n\n' + MARKER + '\n\nThis direction is ' + record['state'] + '. Read CANON.md; do not resume from history.\n')
        pending.replace(role)
        current += [f'## {key}', '']
        active=record.get('current')
        if active:
            current += [f'CURRENT: [{Path(active["path"]).name}]({quote(active["path"])})', '', f'Decision: {active["decision"]}', '']
        else:
            current += [f'NO CURRENT DOCUMENT — {record.get("state", "unresolved").upper()}. Do not reactivate a historical version.', '']
        for old in record.get('history',[]):
            history += [f'- **{old["state"].upper()}** [{Path(old["path"]).name}]({quote(str(Path(old["path"]).relative_to("99-archive")))}) — {old["decision"]}']
    canon.write_text('\n'.join(current)+'\n')
    if any(r.get('history') for r in state['documents'].values()):
        filing.child(home,'99-archive').mkdir(exist_ok=True)
        filing.child(home,'99-archive/INDEX.md').write_text('\n'.join(history)+'\n')


def retire_file(home,active,state,decision,successor,revision):
    source=filing.child(home,active['path'])
    if not source.is_file() or filing.digest(source)!=active['sha256']:
        raise ValueError('Anchor missing or changed; preserve and reconcile before retirement.')
    rel=Path('99-archive')/f'{datetime.now(timezone.utc).date()}-r{revision:04d}'/active['path']
    target=filing.child(home,rel)
    if target.exists():
        raise ValueError('Archive destination already exists; no overwrite permitted.')
    source_meta=filing.child(home,active['path']+'.metadata.json')
    meta=json.loads(source_meta.read_text()) if source_meta.exists() else {}
    target.parent.mkdir(parents=True,exist_ok=True)
    source.rename(target)
    assert filing.digest(target)==active['sha256']
    old={**active,'path':str(rel),'previous_path':active['path'],'state':state,'decision':decision,'superseded_by':successor}
    meta.update(status=state,superseded_by=successor,previous_path=active['path'],sha256=active['sha256'],decision=decision)
    atomic_json(Path(str(target)+'.metadata.json'),meta)
    redirect=f'# Historical document — {state.upper()}\n\nThis file is no longer an anchor. Read CANON.md at the project root before continuing.\n\nCurrent successor: {successor or "None; this direction is parked or retired."}\n\nHistorical copy: {rel}\n'
    # A short redirect preserves old links without preserving stale offer content in active search.
    source.write_text(redirect)
    atomic_json(source_meta,meta)
    rows=filing.records(home)
    changed=[{**r,'path':str(rel),'lifecycle':state,'superseded_by':successor} for r in rows if r['path']==active['path']]
    if changed:
        with filing.child(home,'06-system/asset-register.jsonl').open('a') as out:
            for row in changed:
                out.write(json.dumps(row)+'\n')
        filing.write_index(home,filing.records(home))
    return old


def transition(home_value,key,decision,expected,path=None,retire=None):
    home=home_path(home_value)
    key=filing.slug(key)
    if not decision.strip():
        raise ValueError('Record the user decision or approved replacement evidence.')
    with locked(home):
        state=read_state(home)
        check_revision(state,expected)
        canon=filing.child(home,'CANON.md')
        if canon.exists() and MARKER not in canon.read_text():
            raise ValueError('Reconcile the human-owned CANON before mutation.')
        record=state['documents'].setdefault(key,{'current':None,'history':[]})
        active=record['current']
        roles = filing.child(home, '00-start-here')
        role = roles / (key + '.md')
        if role.exists() or role.is_symlink():
            if role.is_symlink():
                if not active or role.readlink() != Path('../' + active['path']):
                    raise ValueError('Existing role link differs from current state; reconcile it first.')
            elif active or MARKER not in role.read_text():
                raise ValueError('Existing role document is human-owned; preserve it.')
        if path is not None:
            candidate=filing.child(home,path)
            if not candidate.is_file() or Path(path).is_absolute() or '99-archive' in Path(path).parts or str(path).endswith('.metadata.json') or Path(path).name in {'CANON.md','INDEX.md','ASSET-INDEX.md'} or '06-system' in Path(path).parts:
                raise ValueError('Choose a versioned document outside archive and system indexes.')
            meta=Path(str(candidate)+'.metadata.json')
            if meta.exists() and json.loads(meta.read_text()).get('status') in HISTORICAL:
                raise ValueError('Historical redirects cannot become anchors. Restore an explicit versioned copy first.')
            if active and active['path']==str(path):
                raise ValueError('Already current. Changed content needs a new version, not an overwrite.')
            new={'path':str(path),'sha256':filing.digest(candidate),'decision':decision}
        else:
            if retire not in HISTORICAL or not active:
                raise ValueError('Retirement requires a current anchor and a historical state.')
            new=None
        # Validate the outgoing file before any journal or file mutation.
        if active and (not filing.child(home,active['path']).is_file() or filing.digest(filing.child(home,active['path']))!=active['sha256']):
            raise ValueError('Outgoing anchor changed; reconcile it first.')
        atomic_json(pending_path(home),{'before':state,'requested':{'key':key,'new':new,'retire':retire,'decision':decision}})
        if active:
            record['history'].append(retire_file(home,active,retire or 'superseded',decision,new['path'] if new else None,expected+1))
        record['current']=new
        record['state']='current' if new else retire
        state['revision']+=1
        atomic_json(state_path(home),state)
        render(home,state)
        pending_path(home).unlink()  # Own transaction marker only; never user content.
        return state


def current(home_value,include_history=False):
    home=home_path(home_value)
    with locked(home):
        state=read_state(home)
        result={'revision':state['revision'],'documents':{}}
        for key,record in state['documents'].items():
            active=record['current']
            item={'state':record['state'],'current':active}
            if active:
                path=filing.child(home,active['path'])
                item['verification']='verified' if path.is_file() and filing.digest(path)==active['sha256'] else 'CHANGED_OR_MISSING_DO_NOT_USE'
            if include_history:
                item['history']=record['history']
            result['documents'][key]=item
        return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('command',choices=['current','promote','retire'])
    p.add_argument('--project-home',required=True)
    p.add_argument('--key')
    p.add_argument('--path')
    p.add_argument('--state',choices=sorted(HISTORICAL))
    p.add_argument('--decision')
    p.add_argument('--expect-revision',type=int)
    p.add_argument('--include-history',action='store_true')
    a=p.parse_args()
    try:
        if a.command=='current':
            result=current(a.project_home,a.include_history)
        else:
            if a.key is None or a.decision is None or a.expect_revision is None or (a.command=='promote' and a.path is None) or (a.command=='retire' and a.state is None):
                p.error('Mutations require key, decision, expect-revision, and path (promote) or state (retire).')
            result=transition(a.project_home,a.key,a.decision,a.expect_revision,a.path if a.command=='promote' else None,a.state if a.command=='retire' else None)
        print(json.dumps(result,indent=2))
    except (ValueError,OSError,RuntimeError) as error:
        p.exit(1,f'Not changed/usable: {error}\n')


if __name__=='__main__':
    main()
