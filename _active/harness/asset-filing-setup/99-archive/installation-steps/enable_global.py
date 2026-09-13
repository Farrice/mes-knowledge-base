"""Activate the exact global filing scope approved by Farrice in this task."""
from pathlib import Path
from datetime import datetime, timezone
import json
import shutil
import tomllib
WORK=Path('/Users/farricecain/Work')
CONFIG=Path('/Users/farricecain/.codex/config.toml')
GLOBAL=Path('/Users/farricecain/.codex/AGENTS.md')
roots=[str(WORK/p) for p in ('20 Clients','30 Business','40 Creative','50 Reference/Asset Filing')]
old=CONFIG.read_text()
parsed=tomllib.loads(old)
assert parsed.get('sandbox_mode')=='workspace-write'
assert 'default_permissions' not in parsed and 'sandbox_workspace_write' not in parsed
new=old.rstrip()+'\n\n# Approved asset-filing project/support folders; Downloads is unchanged.\n[sandbox_workspace_write]\nwritable_roots = '+json.dumps(roots)+'\n'
checked=tomllib.loads(new)
assert {k:v for k,v in checked.items() if k!='sandbox_workspace_write'}==parsed
old_rules=GLOBAL.read_text()
assert '<!-- BEGIN:asset-filing-default -->' not in old_rules
new_rules=old_rules.rstrip()+'''

<!-- BEGIN:asset-filing-default -->
## Task Asset and Document Filing

When an authorized task downloads, creates, uploads, files, or reuses project assets or documents, read `/Users/farricecain/Work/ASSET-FILING.md` and apply its task-time filing, current-document, archive, and retrieval steps. Keep Chrome's default destination as Downloads. File only assets whose ownership is established for the current task; preserve unrelated and original downloads. Reuse established project homes and artifact-router/worktree rules. Resolve the current authority from the project's living CANON/index and explicit user decisions before drafting; parked, superseded, archived, and unreviewed material is never a default anchor. Reconcile updates before completion and preserve history with provenance and a successor pointer. Never choose authority by modification time or search rank. This authorizes no background sweep, broader upload destination, publication, spending, deletion, or security bypass. The guide and helper add no new approval policy.
<!-- END:asset-filing-default -->
'''
for p in (CONFIG,GLOBAL):
    assert not p.is_symlink()
backup=Path('/Users/farricecain/.codex/backups')/('asset-filing-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ'))
backup.mkdir(parents=True,mode=0o700)
for p in (CONFIG,GLOBAL):
    dest=backup/p.name
    shutil.copy2(p,dest)
    dest.chmod(0o600)
assert CONFIG.read_text()==old and GLOBAL.read_text()==old_rules
for p,content in ((CONFIG,new),(GLOBAL,new_rules)):
    temp=p.with_name(p.name+'.asset-filing-pending')
    with temp.open('x') as out:
        out.write(content)
    temp.chmod(p.stat().st_mode & 0o777)
    temp.replace(p)
assert tomllib.loads(CONFIG.read_text())==checked and GLOBAL.read_text()==new_rules
print(json.dumps({'config_saved':True,'global_pointer_saved':True,'writable_roots':roots,'backup':str(backup),'fresh_task_activation':'NOT_YET_TESTED'},indent=2))
