from pathlib import Path
import hashlib
import json
import shutil
import sys
from datetime import datetime,timezone
PACKAGE=Path(__file__).resolve().parent.parent
WORK=Path('/Users/farricecain/Work')
SUPPORT=WORK/'50 Reference'/'Asset Filing'
HOME=WORK/'30 Business'/'asset-filing-setup'
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
backup=SUPPORT/'99-archive'/stamp
backup.mkdir(parents=True)
root_guide=WORK/'ASSET-FILING.md'
assert not root_guide.is_symlink()
for path in (root_guide,SUPPORT/'asset_filing.py',SUPPORT/'SETUP-RECEIPT.md'):
    shutil.copy2(path,backup/path.name)
for name in ('asset_filing.py','document_history.py'):
    shutil.copy2(PACKAGE/'06-system'/name,SUPPORT/name)
sys.path.insert(0,str(SUPPORT))
import asset_filing as f
import document_history as h
old='05-assets/asset-filing-setup-filing-guide-v01-review.md'
assert f.digest(root_guide)==f.digest(HOME/old)
h.transition(HOME,'filing-guide','Existing installed filing guide; baseline preserved before requested history upgrade',0,path=old)
filed=f.file_asset(PACKAGE/'ASSET-FILING.md',HOME,'filing-guide',status='review')
new=str(Path(filed['path']).relative_to(HOME))
h.transition(HOME,'filing-guide','Farrice approved global activation and requested current anchors, archive retirement, and protection against old offers on 2026-09-12 in task 01a097c8-631e-7763-9ca7-9ae0e63735ba',1,path=new)
entry=HOME/'00-start-here'/'filing-guide.md'
link=root_guide.with_name('ASSET-FILING.pending-link')
link.symlink_to(entry)
link.replace(root_guide)
assert root_guide.resolve()==(HOME/new).resolve()
state=h.current(HOME,True)
assert state['documents']['filing-guide']['verification']=='verified'
assert len(f.find_assets('asset-filing-setup',verify=True))==1
old_archive=HOME/state['documents']['filing-guide']['history'][0]['path']
assert f.digest(old_archive)==f.digest(backup/'ASSET-FILING.md')
assert 'superseded' not in json.dumps(h.current(HOME))
start=WORK/'START-HERE.md'
s=start.read_text().replace('Global Codex activation and additional folder permissions are pending explicit approval; see SETUP-RECEIPT.md there.', 'The global filing instruction and scoped folder settings are saved. The guide now follows its current version; retired copies are historical only. See SETUP-RECEIPT.md for live-test limits.')
start.write_text(s)
receipt={'global_config_saved':True,'global_instruction_saved':True,'local_asset_tests':9,'document_history_tests':15,'native_inventory_tests':4,'current_guide':str(root_guide.resolve()),'stable_guide':str(root_guide),'historical_guide':str(old_archive),'current_guide_sha256':f.digest(root_guide),'archived_original_matches':True,'default_search_current_only':True,'personal_downloads_changed':False,'browser_transfer_test':'NOT_RUN','fresh_task_instruction_activation':'NOT_RUN','source_upgrade_backup':str(backup),'native_generator_integration':'PENDING_LANE_MERGE'}
(SUPPORT/'installation.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
